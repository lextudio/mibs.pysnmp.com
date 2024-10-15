# SNMP MIB module (CISCO-IETF-IPMROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-IPMROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:36 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(IANAipMRouteProtocol,
 IANAipRouteProtocol) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

(LanguageTag,) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "LanguageTag")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfIpMRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117)
)
ciscoIetfIpMRouteMIB.setRevisions(
        ("2006-08-24 00:00",
         "2004-12-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CIpMRouteMIBObjects_ObjectIdentity = ObjectIdentity
cIpMRouteMIBObjects = _CIpMRouteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1)
)
_CIpMRoute_ObjectIdentity = ObjectIdentity
cIpMRoute = _CIpMRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1)
)


class _CIpMRouteEnable_Type(Integer32):
    """Custom type cIpMRouteEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_CIpMRouteEnable_Type.__name__ = "Integer32"
_CIpMRouteEnable_Object = MibScalar
cIpMRouteEnable = _CIpMRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 1),
    _CIpMRouteEnable_Type()
)
cIpMRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpMRouteEnable.setStatus("current")
_CIpMRouteTable_Object = MibTable
cIpMRouteTable = _CIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cIpMRouteTable.setStatus("current")
_CIpMRouteEntry_Object = MibTableRow
cIpMRouteEntry = _CIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1)
)
cIpMRouteEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteAddrType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteGroup"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteSource"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    cIpMRouteEntry.setStatus("current")
_CIpMRouteAddrType_Type = InetAddressType
_CIpMRouteAddrType_Object = MibTableColumn
cIpMRouteAddrType = _CIpMRouteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 1),
    _CIpMRouteAddrType_Type()
)
cIpMRouteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteAddrType.setStatus("current")


class _CIpMRouteGroup_Type(InetAddress):
    """Custom type cIpMRouteGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteGroup_Type.__name__ = "InetAddress"
_CIpMRouteGroup_Object = MibTableColumn
cIpMRouteGroup = _CIpMRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 2),
    _CIpMRouteGroup_Type()
)
cIpMRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteGroup.setStatus("current")


class _CIpMRouteSource_Type(InetAddress):
    """Custom type cIpMRouteSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteSource_Type.__name__ = "InetAddress"
_CIpMRouteSource_Object = MibTableColumn
cIpMRouteSource = _CIpMRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 3),
    _CIpMRouteSource_Type()
)
cIpMRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteSource.setStatus("current")
_CIpMRouteSourceMask_Type = InetAddressPrefixLength
_CIpMRouteSourceMask_Object = MibTableColumn
cIpMRouteSourceMask = _CIpMRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 4),
    _CIpMRouteSourceMask_Type()
)
cIpMRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteSourceMask.setStatus("current")


class _CIpMRouteUpstreamNeighbor_Type(InetAddress):
    """Custom type cIpMRouteUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteUpstreamNeighbor_Type.__name__ = "InetAddress"
_CIpMRouteUpstreamNeighbor_Object = MibTableColumn
cIpMRouteUpstreamNeighbor = _CIpMRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 5),
    _CIpMRouteUpstreamNeighbor_Type()
)
cIpMRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteUpstreamNeighbor.setStatus("current")
_CIpMRouteInIfIndex_Type = InterfaceIndexOrZero
_CIpMRouteInIfIndex_Object = MibTableColumn
cIpMRouteInIfIndex = _CIpMRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 6),
    _CIpMRouteInIfIndex_Type()
)
cIpMRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInIfIndex.setStatus("current")
_CIpMRouteUpTime_Type = TimeTicks
_CIpMRouteUpTime_Object = MibTableColumn
cIpMRouteUpTime = _CIpMRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 7),
    _CIpMRouteUpTime_Type()
)
cIpMRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteUpTime.setStatus("current")
_CIpMRouteExpiryTime_Type = TimeTicks
_CIpMRouteExpiryTime_Object = MibTableColumn
cIpMRouteExpiryTime = _CIpMRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 8),
    _CIpMRouteExpiryTime_Type()
)
cIpMRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteExpiryTime.setStatus("current")
_CIpMRoutePkts_Type = Counter32
_CIpMRoutePkts_Object = MibTableColumn
cIpMRoutePkts = _CIpMRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 9),
    _CIpMRoutePkts_Type()
)
cIpMRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRoutePkts.setStatus("current")
_CIpMRouteDifferentInIfPackets_Type = Counter32
_CIpMRouteDifferentInIfPackets_Object = MibTableColumn
cIpMRouteDifferentInIfPackets = _CIpMRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 10),
    _CIpMRouteDifferentInIfPackets_Type()
)
cIpMRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteDifferentInIfPackets.setStatus("current")
_CIpMRouteOctets_Type = Counter32
_CIpMRouteOctets_Object = MibTableColumn
cIpMRouteOctets = _CIpMRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 11),
    _CIpMRouteOctets_Type()
)
cIpMRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteOctets.setStatus("current")
_CIpMRouteProtocol_Type = IANAipMRouteProtocol
_CIpMRouteProtocol_Object = MibTableColumn
cIpMRouteProtocol = _CIpMRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 12),
    _CIpMRouteProtocol_Type()
)
cIpMRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteProtocol.setStatus("current")
_CIpMRouteRtProto_Type = IANAipRouteProtocol
_CIpMRouteRtProto_Object = MibTableColumn
cIpMRouteRtProto = _CIpMRouteRtProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 13),
    _CIpMRouteRtProto_Type()
)
cIpMRouteRtProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteRtProto.setStatus("current")


class _CIpMRouteRtAddress_Type(InetAddress):
    """Custom type cIpMRouteRtAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteRtAddress_Type.__name__ = "InetAddress"
_CIpMRouteRtAddress_Object = MibTableColumn
cIpMRouteRtAddress = _CIpMRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 14),
    _CIpMRouteRtAddress_Type()
)
cIpMRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteRtAddress.setStatus("current")
_CIpMRouteRtMask_Type = InetAddressPrefixLength
_CIpMRouteRtMask_Object = MibTableColumn
cIpMRouteRtMask = _CIpMRouteRtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 15),
    _CIpMRouteRtMask_Type()
)
cIpMRouteRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteRtMask.setStatus("current")


class _CIpMRouteRtType_Type(Integer32):
    """Custom type cIpMRouteRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 2),
          ("unicast", 1))
    )


_CIpMRouteRtType_Type.__name__ = "Integer32"
_CIpMRouteRtType_Object = MibTableColumn
cIpMRouteRtType = _CIpMRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 16),
    _CIpMRouteRtType_Type()
)
cIpMRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteRtType.setStatus("current")
_CIpMRouteHCOctets_Type = Counter64
_CIpMRouteHCOctets_Object = MibTableColumn
cIpMRouteHCOctets = _CIpMRouteHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 2, 1, 17),
    _CIpMRouteHCOctets_Type()
)
cIpMRouteHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteHCOctets.setStatus("current")
_CIpMRouteNextHopTable_Object = MibTable
cIpMRouteNextHopTable = _CIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cIpMRouteNextHopTable.setStatus("current")
_CIpMRouteNextHopEntry_Object = MibTableRow
cIpMRouteNextHopEntry = _CIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1)
)
cIpMRouteNextHopEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopAddrType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopGroup"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopSource"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopSourceMask"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopIfIndex"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    cIpMRouteNextHopEntry.setStatus("current")
_CIpMRouteNextHopAddrType_Type = InetAddressType
_CIpMRouteNextHopAddrType_Object = MibTableColumn
cIpMRouteNextHopAddrType = _CIpMRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 1),
    _CIpMRouteNextHopAddrType_Type()
)
cIpMRouteNextHopAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopAddrType.setStatus("current")


class _CIpMRouteNextHopGroup_Type(InetAddress):
    """Custom type cIpMRouteNextHopGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteNextHopGroup_Type.__name__ = "InetAddress"
_CIpMRouteNextHopGroup_Object = MibTableColumn
cIpMRouteNextHopGroup = _CIpMRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 2),
    _CIpMRouteNextHopGroup_Type()
)
cIpMRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopGroup.setStatus("current")


class _CIpMRouteNextHopSource_Type(InetAddress):
    """Custom type cIpMRouteNextHopSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteNextHopSource_Type.__name__ = "InetAddress"
_CIpMRouteNextHopSource_Object = MibTableColumn
cIpMRouteNextHopSource = _CIpMRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 3),
    _CIpMRouteNextHopSource_Type()
)
cIpMRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopSource.setStatus("current")
_CIpMRouteNextHopSourceMask_Type = InetAddressPrefixLength
_CIpMRouteNextHopSourceMask_Object = MibTableColumn
cIpMRouteNextHopSourceMask = _CIpMRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 4),
    _CIpMRouteNextHopSourceMask_Type()
)
cIpMRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopSourceMask.setStatus("current")
_CIpMRouteNextHopIfIndex_Type = InterfaceIndex
_CIpMRouteNextHopIfIndex_Object = MibTableColumn
cIpMRouteNextHopIfIndex = _CIpMRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 5),
    _CIpMRouteNextHopIfIndex_Type()
)
cIpMRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopIfIndex.setStatus("current")


class _CIpMRouteNextHopAddress_Type(InetAddress):
    """Custom type cIpMRouteNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteNextHopAddress_Type.__name__ = "InetAddress"
_CIpMRouteNextHopAddress_Object = MibTableColumn
cIpMRouteNextHopAddress = _CIpMRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 6),
    _CIpMRouteNextHopAddress_Type()
)
cIpMRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteNextHopAddress.setStatus("current")


class _CIpMRouteNextHopState_Type(Integer32):
    """Custom type cIpMRouteNextHopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 2),
          ("pruned", 1))
    )


_CIpMRouteNextHopState_Type.__name__ = "Integer32"
_CIpMRouteNextHopState_Object = MibTableColumn
cIpMRouteNextHopState = _CIpMRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 7),
    _CIpMRouteNextHopState_Type()
)
cIpMRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopState.setStatus("current")
_CIpMRouteNextHopUpTime_Type = TimeTicks
_CIpMRouteNextHopUpTime_Object = MibTableColumn
cIpMRouteNextHopUpTime = _CIpMRouteNextHopUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 8),
    _CIpMRouteNextHopUpTime_Type()
)
cIpMRouteNextHopUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopUpTime.setStatus("current")
_CIpMRouteNextHopExpiryTime_Type = TimeTicks
_CIpMRouteNextHopExpiryTime_Object = MibTableColumn
cIpMRouteNextHopExpiryTime = _CIpMRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 9),
    _CIpMRouteNextHopExpiryTime_Type()
)
cIpMRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopExpiryTime.setStatus("current")


class _CIpMRouteNextHopClosestHops_Type(Integer32):
    """Custom type cIpMRouteNextHopClosestHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIpMRouteNextHopClosestHops_Type.__name__ = "Integer32"
_CIpMRouteNextHopClosestHops_Object = MibTableColumn
cIpMRouteNextHopClosestHops = _CIpMRouteNextHopClosestHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 10),
    _CIpMRouteNextHopClosestHops_Type()
)
cIpMRouteNextHopClosestHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopClosestHops.setStatus("current")
_CIpMRouteNextHopProtocol_Type = IANAipMRouteProtocol
_CIpMRouteNextHopProtocol_Object = MibTableColumn
cIpMRouteNextHopProtocol = _CIpMRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 11),
    _CIpMRouteNextHopProtocol_Type()
)
cIpMRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopProtocol.setStatus("current")
_CIpMRouteNextHopPkts_Type = Counter32
_CIpMRouteNextHopPkts_Object = MibTableColumn
cIpMRouteNextHopPkts = _CIpMRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 3, 1, 12),
    _CIpMRouteNextHopPkts_Type()
)
cIpMRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteNextHopPkts.setStatus("current")
_CIpMRouteInterfaceTable_Object = MibTable
cIpMRouteInterfaceTable = _CIpMRouteInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cIpMRouteInterfaceTable.setStatus("current")
_CIpMRouteInterfaceEntry_Object = MibTableRow
cIpMRouteInterfaceEntry = _CIpMRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1)
)
cIpMRouteInterfaceEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceIfIndex"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceIPVersion"),
)
if mibBuilder.loadTexts:
    cIpMRouteInterfaceEntry.setStatus("current")
_CIpMRouteInterfaceIfIndex_Type = InterfaceIndex
_CIpMRouteInterfaceIfIndex_Object = MibTableColumn
cIpMRouteInterfaceIfIndex = _CIpMRouteInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 1),
    _CIpMRouteInterfaceIfIndex_Type()
)
cIpMRouteInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceIfIndex.setStatus("current")
_CIpMRouteInterfaceIPVersion_Type = InetVersion
_CIpMRouteInterfaceIPVersion_Object = MibTableColumn
cIpMRouteInterfaceIPVersion = _CIpMRouteInterfaceIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 2),
    _CIpMRouteInterfaceIPVersion_Type()
)
cIpMRouteInterfaceIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceIPVersion.setStatus("current")


class _CIpMRouteInterfaceTtl_Type(Integer32):
    """Custom type cIpMRouteInterfaceTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIpMRouteInterfaceTtl_Type.__name__ = "Integer32"
_CIpMRouteInterfaceTtl_Object = MibTableColumn
cIpMRouteInterfaceTtl = _CIpMRouteInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 3),
    _CIpMRouteInterfaceTtl_Type()
)
cIpMRouteInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceTtl.setStatus("current")
_CIpMRouteInterfaceProtocol_Type = IANAipMRouteProtocol
_CIpMRouteInterfaceProtocol_Object = MibTableColumn
cIpMRouteInterfaceProtocol = _CIpMRouteInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 4),
    _CIpMRouteInterfaceProtocol_Type()
)
cIpMRouteInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceProtocol.setStatus("current")


class _CIpMRouteInterfaceRateLimit_Type(Integer32):
    """Custom type cIpMRouteInterfaceRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496295),
    )


_CIpMRouteInterfaceRateLimit_Type.__name__ = "Integer32"
_CIpMRouteInterfaceRateLimit_Object = MibTableColumn
cIpMRouteInterfaceRateLimit = _CIpMRouteInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 5),
    _CIpMRouteInterfaceRateLimit_Type()
)
cIpMRouteInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceRateLimit.setStatus("current")
_CIpMRouteInterfaceInMcastPkts_Type = Counter32
_CIpMRouteInterfaceInMcastPkts_Object = MibTableColumn
cIpMRouteInterfaceInMcastPkts = _CIpMRouteInterfaceInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 6),
    _CIpMRouteInterfaceInMcastPkts_Type()
)
cIpMRouteInterfaceInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceInMcastPkts.setStatus("current")
_CIpMRouteInterfaceOutMcastPkts_Type = Counter32
_CIpMRouteInterfaceOutMcastPkts_Object = MibTableColumn
cIpMRouteInterfaceOutMcastPkts = _CIpMRouteInterfaceOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 7),
    _CIpMRouteInterfaceOutMcastPkts_Type()
)
cIpMRouteInterfaceOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceOutMcastPkts.setStatus("current")
_CIpMRouteInterfaceInMcastOctets_Type = Counter32
_CIpMRouteInterfaceInMcastOctets_Object = MibTableColumn
cIpMRouteInterfaceInMcastOctets = _CIpMRouteInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 8),
    _CIpMRouteInterfaceInMcastOctets_Type()
)
cIpMRouteInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceInMcastOctets.setStatus("current")
_CIpMRouteInterfaceOutMcastOctets_Type = Counter32
_CIpMRouteInterfaceOutMcastOctets_Object = MibTableColumn
cIpMRouteInterfaceOutMcastOctets = _CIpMRouteInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 9),
    _CIpMRouteInterfaceOutMcastOctets_Type()
)
cIpMRouteInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceOutMcastOctets.setStatus("current")
_CIpMRouteInterfaceHCInMOctets_Type = Counter64
_CIpMRouteInterfaceHCInMOctets_Object = MibTableColumn
cIpMRouteInterfaceHCInMOctets = _CIpMRouteInterfaceHCInMOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 10),
    _CIpMRouteInterfaceHCInMOctets_Type()
)
cIpMRouteInterfaceHCInMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceHCInMOctets.setStatus("current")
_CIpMRouteInterfaceHCOutMOctets_Type = Counter64
_CIpMRouteInterfaceHCOutMOctets_Object = MibTableColumn
cIpMRouteInterfaceHCOutMOctets = _CIpMRouteInterfaceHCOutMOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 11),
    _CIpMRouteInterfaceHCOutMOctets_Type()
)
cIpMRouteInterfaceHCOutMOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceHCOutMOctets.setStatus("current")
_CIpMRouteInterfaceHCInMPkts_Type = Counter64
_CIpMRouteInterfaceHCInMPkts_Object = MibTableColumn
cIpMRouteInterfaceHCInMPkts = _CIpMRouteInterfaceHCInMPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 12),
    _CIpMRouteInterfaceHCInMPkts_Type()
)
cIpMRouteInterfaceHCInMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceHCInMPkts.setStatus("current")
_CIpMRouteInterfaceHCOutMPkts_Type = Counter64
_CIpMRouteInterfaceHCOutMPkts_Object = MibTableColumn
cIpMRouteInterfaceHCOutMPkts = _CIpMRouteInterfaceHCOutMPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 4, 1, 13),
    _CIpMRouteInterfaceHCOutMPkts_Type()
)
cIpMRouteInterfaceHCOutMPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteInterfaceHCOutMPkts.setStatus("current")
_CIpMRouteBoundaryTable_Object = MibTable
cIpMRouteBoundaryTable = _CIpMRouteBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cIpMRouteBoundaryTable.setStatus("current")
_CIpMRouteBoundaryEntry_Object = MibTableRow
cIpMRouteBoundaryEntry = _CIpMRouteBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1)
)
cIpMRouteBoundaryEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryScopeId"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryIfIndex"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryAddressType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryAddress"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryAddressMask"),
)
if mibBuilder.loadTexts:
    cIpMRouteBoundaryEntry.setStatus("current")


class _CIpMRouteBoundaryScopeId_Type(Integer32):
    """Custom type cIpMRouteBoundaryScopeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CIpMRouteBoundaryScopeId_Type.__name__ = "Integer32"
_CIpMRouteBoundaryScopeId_Object = MibTableColumn
cIpMRouteBoundaryScopeId = _CIpMRouteBoundaryScopeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 1),
    _CIpMRouteBoundaryScopeId_Type()
)
cIpMRouteBoundaryScopeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryScopeId.setStatus("current")
_CIpMRouteBoundaryIfIndex_Type = InterfaceIndex
_CIpMRouteBoundaryIfIndex_Object = MibTableColumn
cIpMRouteBoundaryIfIndex = _CIpMRouteBoundaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 2),
    _CIpMRouteBoundaryIfIndex_Type()
)
cIpMRouteBoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryIfIndex.setStatus("current")
_CIpMRouteBoundaryAddressType_Type = InetAddressType
_CIpMRouteBoundaryAddressType_Object = MibTableColumn
cIpMRouteBoundaryAddressType = _CIpMRouteBoundaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 3),
    _CIpMRouteBoundaryAddressType_Type()
)
cIpMRouteBoundaryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryAddressType.setStatus("current")


class _CIpMRouteBoundaryAddress_Type(InetAddress):
    """Custom type cIpMRouteBoundaryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteBoundaryAddress_Type.__name__ = "InetAddress"
_CIpMRouteBoundaryAddress_Object = MibTableColumn
cIpMRouteBoundaryAddress = _CIpMRouteBoundaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 4),
    _CIpMRouteBoundaryAddress_Type()
)
cIpMRouteBoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryAddress.setStatus("current")
_CIpMRouteBoundaryAddressMask_Type = InetAddressPrefixLength
_CIpMRouteBoundaryAddressMask_Object = MibTableColumn
cIpMRouteBoundaryAddressMask = _CIpMRouteBoundaryAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 5),
    _CIpMRouteBoundaryAddressMask_Type()
)
cIpMRouteBoundaryAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryAddressMask.setStatus("current")
_CIpMRouteBoundaryNameString_Type = SnmpAdminString
_CIpMRouteBoundaryNameString_Object = MibTableColumn
cIpMRouteBoundaryNameString = _CIpMRouteBoundaryNameString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 6),
    _CIpMRouteBoundaryNameString_Type()
)
cIpMRouteBoundaryNameString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryNameString.setStatus("current")
_CIpMRouteBoundaryStatus_Type = RowStatus
_CIpMRouteBoundaryStatus_Object = MibTableColumn
cIpMRouteBoundaryStatus = _CIpMRouteBoundaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 5, 1, 7),
    _CIpMRouteBoundaryStatus_Type()
)
cIpMRouteBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpMRouteBoundaryStatus.setStatus("current")
_CIpMRouteScopeNameTable_Object = MibTable
cIpMRouteScopeNameTable = _CIpMRouteScopeNameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cIpMRouteScopeNameTable.setStatus("current")
_CIpMRouteScopeNameEntry_Object = MibTableRow
cIpMRouteScopeNameEntry = _CIpMRouteScopeNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1)
)
cIpMRouteScopeNameEntry.setIndexNames(
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameAddressType"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameAddress"),
    (0, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameAddressMask"),
    (1, "CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameLanguage"),
)
if mibBuilder.loadTexts:
    cIpMRouteScopeNameEntry.setStatus("current")
_CIpMRouteScopeNameAddressType_Type = InetAddressType
_CIpMRouteScopeNameAddressType_Object = MibTableColumn
cIpMRouteScopeNameAddressType = _CIpMRouteScopeNameAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 1),
    _CIpMRouteScopeNameAddressType_Type()
)
cIpMRouteScopeNameAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameAddressType.setStatus("current")


class _CIpMRouteScopeNameAddress_Type(InetAddress):
    """Custom type cIpMRouteScopeNameAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CIpMRouteScopeNameAddress_Type.__name__ = "InetAddress"
_CIpMRouteScopeNameAddress_Object = MibTableColumn
cIpMRouteScopeNameAddress = _CIpMRouteScopeNameAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 2),
    _CIpMRouteScopeNameAddress_Type()
)
cIpMRouteScopeNameAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameAddress.setStatus("current")
_CIpMRouteScopeNameAddressMask_Type = InetAddressPrefixLength
_CIpMRouteScopeNameAddressMask_Object = MibTableColumn
cIpMRouteScopeNameAddressMask = _CIpMRouteScopeNameAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 3),
    _CIpMRouteScopeNameAddressMask_Type()
)
cIpMRouteScopeNameAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameAddressMask.setStatus("current")
_CIpMRouteScopeNameLanguage_Type = LanguageTag
_CIpMRouteScopeNameLanguage_Object = MibTableColumn
cIpMRouteScopeNameLanguage = _CIpMRouteScopeNameLanguage_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 4),
    _CIpMRouteScopeNameLanguage_Type()
)
cIpMRouteScopeNameLanguage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameLanguage.setStatus("current")
_CIpMRouteScopeNameString_Type = SnmpAdminString
_CIpMRouteScopeNameString_Object = MibTableColumn
cIpMRouteScopeNameString = _CIpMRouteScopeNameString_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 5),
    _CIpMRouteScopeNameString_Type()
)
cIpMRouteScopeNameString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameString.setStatus("current")


class _CIpMRouteScopeNameDefault_Type(TruthValue):
    """Custom type cIpMRouteScopeNameDefault based on TruthValue"""


_CIpMRouteScopeNameDefault_Object = MibTableColumn
cIpMRouteScopeNameDefault = _CIpMRouteScopeNameDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 6),
    _CIpMRouteScopeNameDefault_Type()
)
cIpMRouteScopeNameDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameDefault.setStatus("current")
_CIpMRouteScopeNameStatus_Type = RowStatus
_CIpMRouteScopeNameStatus_Object = MibTableColumn
cIpMRouteScopeNameStatus = _CIpMRouteScopeNameStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 6, 1, 7),
    _CIpMRouteScopeNameStatus_Type()
)
cIpMRouteScopeNameStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpMRouteScopeNameStatus.setStatus("current")
_CIpMRouteEntryCount_Type = Gauge32
_CIpMRouteEntryCount_Object = MibScalar
cIpMRouteEntryCount = _CIpMRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 1, 1, 7),
    _CIpMRouteEntryCount_Type()
)
cIpMRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpMRouteEntryCount.setStatus("current")
_CIpMRouteMIBConformance_ObjectIdentity = ObjectIdentity
cIpMRouteMIBConformance = _CIpMRouteMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2)
)
_CIpMRouteMIBCompliances_ObjectIdentity = ObjectIdentity
cIpMRouteMIBCompliances = _CIpMRouteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 1)
)
_CIpMRouteMIBGroups_ObjectIdentity = ObjectIdentity
cIpMRouteMIBGroups = _CIpMRouteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2)
)

# Managed Objects groups

cIpMRouteMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 1)
)
cIpMRouteMIBBasicGroup.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteEnable"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteEntryCount"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteUpstreamNeighbor"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInIfIndex"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteUpTime"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteExpiryTime"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopState"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopUpTime"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopExpiryTime"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopProtocol"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceTtl"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceProtocol"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceRateLimit"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceInMcastPkts"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceOutMcastPkts"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceInMcastOctets"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceOutMcastOctets"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteProtocol"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBBasicGroup.setStatus("current")

cIpMRouteMIBHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 2)
)
cIpMRouteMIBHopCountGroup.setObjects(
    ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopClosestHops")
)
if mibBuilder.loadTexts:
    cIpMRouteMIBHopCountGroup.setStatus("current")

cIpMRouteMIBBoundaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 3)
)
cIpMRouteMIBBoundaryGroup.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryStatus"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameString"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameDefault"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteScopeNameStatus"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteBoundaryNameString"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBBoundaryGroup.setStatus("current")

cIpMRouteMIBPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 4)
)
cIpMRouteMIBPktsOutGroup.setObjects(
    ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteNextHopPkts")
)
if mibBuilder.loadTexts:
    cIpMRouteMIBPktsOutGroup.setStatus("current")

cIpMRouteMIBHCInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 5)
)
cIpMRouteMIBHCInterfaceGroup.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceHCInMOctets"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceHCOutMOctets"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteHCOctets"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBHCInterfaceGroup.setStatus("current")

cIpMRouteMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 6)
)
cIpMRouteMIBRouteGroup.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteRtProto"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteRtAddress"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteRtMask"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteRtType"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBRouteGroup.setStatus("current")

cIpMRouteMIBPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 7)
)
cIpMRouteMIBPktsGroup.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRoutePkts"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteDifferentInIfPackets"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteOctets"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBPktsGroup.setStatus("current")

cIpMRouteMIBHCInterfaceGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 2, 8)
)
cIpMRouteMIBHCInterfaceGroupSup1.setObjects(
      *(("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceHCInMPkts"),
        ("CISCO-IETF-IPMROUTE-MIB", "cIpMRouteInterfaceHCOutMPkts"))
)
if mibBuilder.loadTexts:
    cIpMRouteMIBHCInterfaceGroupSup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cIpMRouteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cIpMRouteMIBCompliance.setStatus(
        "deprecated"
    )

cIpMRouteMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 117, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cIpMRouteMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-IPMROUTE-MIB",
    **{"ciscoIetfIpMRouteMIB": ciscoIetfIpMRouteMIB,
       "cIpMRouteMIBObjects": cIpMRouteMIBObjects,
       "cIpMRoute": cIpMRoute,
       "cIpMRouteEnable": cIpMRouteEnable,
       "cIpMRouteTable": cIpMRouteTable,
       "cIpMRouteEntry": cIpMRouteEntry,
       "cIpMRouteAddrType": cIpMRouteAddrType,
       "cIpMRouteGroup": cIpMRouteGroup,
       "cIpMRouteSource": cIpMRouteSource,
       "cIpMRouteSourceMask": cIpMRouteSourceMask,
       "cIpMRouteUpstreamNeighbor": cIpMRouteUpstreamNeighbor,
       "cIpMRouteInIfIndex": cIpMRouteInIfIndex,
       "cIpMRouteUpTime": cIpMRouteUpTime,
       "cIpMRouteExpiryTime": cIpMRouteExpiryTime,
       "cIpMRoutePkts": cIpMRoutePkts,
       "cIpMRouteDifferentInIfPackets": cIpMRouteDifferentInIfPackets,
       "cIpMRouteOctets": cIpMRouteOctets,
       "cIpMRouteProtocol": cIpMRouteProtocol,
       "cIpMRouteRtProto": cIpMRouteRtProto,
       "cIpMRouteRtAddress": cIpMRouteRtAddress,
       "cIpMRouteRtMask": cIpMRouteRtMask,
       "cIpMRouteRtType": cIpMRouteRtType,
       "cIpMRouteHCOctets": cIpMRouteHCOctets,
       "cIpMRouteNextHopTable": cIpMRouteNextHopTable,
       "cIpMRouteNextHopEntry": cIpMRouteNextHopEntry,
       "cIpMRouteNextHopAddrType": cIpMRouteNextHopAddrType,
       "cIpMRouteNextHopGroup": cIpMRouteNextHopGroup,
       "cIpMRouteNextHopSource": cIpMRouteNextHopSource,
       "cIpMRouteNextHopSourceMask": cIpMRouteNextHopSourceMask,
       "cIpMRouteNextHopIfIndex": cIpMRouteNextHopIfIndex,
       "cIpMRouteNextHopAddress": cIpMRouteNextHopAddress,
       "cIpMRouteNextHopState": cIpMRouteNextHopState,
       "cIpMRouteNextHopUpTime": cIpMRouteNextHopUpTime,
       "cIpMRouteNextHopExpiryTime": cIpMRouteNextHopExpiryTime,
       "cIpMRouteNextHopClosestHops": cIpMRouteNextHopClosestHops,
       "cIpMRouteNextHopProtocol": cIpMRouteNextHopProtocol,
       "cIpMRouteNextHopPkts": cIpMRouteNextHopPkts,
       "cIpMRouteInterfaceTable": cIpMRouteInterfaceTable,
       "cIpMRouteInterfaceEntry": cIpMRouteInterfaceEntry,
       "cIpMRouteInterfaceIfIndex": cIpMRouteInterfaceIfIndex,
       "cIpMRouteInterfaceIPVersion": cIpMRouteInterfaceIPVersion,
       "cIpMRouteInterfaceTtl": cIpMRouteInterfaceTtl,
       "cIpMRouteInterfaceProtocol": cIpMRouteInterfaceProtocol,
       "cIpMRouteInterfaceRateLimit": cIpMRouteInterfaceRateLimit,
       "cIpMRouteInterfaceInMcastPkts": cIpMRouteInterfaceInMcastPkts,
       "cIpMRouteInterfaceOutMcastPkts": cIpMRouteInterfaceOutMcastPkts,
       "cIpMRouteInterfaceInMcastOctets": cIpMRouteInterfaceInMcastOctets,
       "cIpMRouteInterfaceOutMcastOctets": cIpMRouteInterfaceOutMcastOctets,
       "cIpMRouteInterfaceHCInMOctets": cIpMRouteInterfaceHCInMOctets,
       "cIpMRouteInterfaceHCOutMOctets": cIpMRouteInterfaceHCOutMOctets,
       "cIpMRouteInterfaceHCInMPkts": cIpMRouteInterfaceHCInMPkts,
       "cIpMRouteInterfaceHCOutMPkts": cIpMRouteInterfaceHCOutMPkts,
       "cIpMRouteBoundaryTable": cIpMRouteBoundaryTable,
       "cIpMRouteBoundaryEntry": cIpMRouteBoundaryEntry,
       "cIpMRouteBoundaryScopeId": cIpMRouteBoundaryScopeId,
       "cIpMRouteBoundaryIfIndex": cIpMRouteBoundaryIfIndex,
       "cIpMRouteBoundaryAddressType": cIpMRouteBoundaryAddressType,
       "cIpMRouteBoundaryAddress": cIpMRouteBoundaryAddress,
       "cIpMRouteBoundaryAddressMask": cIpMRouteBoundaryAddressMask,
       "cIpMRouteBoundaryNameString": cIpMRouteBoundaryNameString,
       "cIpMRouteBoundaryStatus": cIpMRouteBoundaryStatus,
       "cIpMRouteScopeNameTable": cIpMRouteScopeNameTable,
       "cIpMRouteScopeNameEntry": cIpMRouteScopeNameEntry,
       "cIpMRouteScopeNameAddressType": cIpMRouteScopeNameAddressType,
       "cIpMRouteScopeNameAddress": cIpMRouteScopeNameAddress,
       "cIpMRouteScopeNameAddressMask": cIpMRouteScopeNameAddressMask,
       "cIpMRouteScopeNameLanguage": cIpMRouteScopeNameLanguage,
       "cIpMRouteScopeNameString": cIpMRouteScopeNameString,
       "cIpMRouteScopeNameDefault": cIpMRouteScopeNameDefault,
       "cIpMRouteScopeNameStatus": cIpMRouteScopeNameStatus,
       "cIpMRouteEntryCount": cIpMRouteEntryCount,
       "cIpMRouteMIBConformance": cIpMRouteMIBConformance,
       "cIpMRouteMIBCompliances": cIpMRouteMIBCompliances,
       "cIpMRouteMIBCompliance": cIpMRouteMIBCompliance,
       "cIpMRouteMIBComplianceRev1": cIpMRouteMIBComplianceRev1,
       "cIpMRouteMIBGroups": cIpMRouteMIBGroups,
       "cIpMRouteMIBBasicGroup": cIpMRouteMIBBasicGroup,
       "cIpMRouteMIBHopCountGroup": cIpMRouteMIBHopCountGroup,
       "cIpMRouteMIBBoundaryGroup": cIpMRouteMIBBoundaryGroup,
       "cIpMRouteMIBPktsOutGroup": cIpMRouteMIBPktsOutGroup,
       "cIpMRouteMIBHCInterfaceGroup": cIpMRouteMIBHCInterfaceGroup,
       "cIpMRouteMIBRouteGroup": cIpMRouteMIBRouteGroup,
       "cIpMRouteMIBPktsGroup": cIpMRouteMIBPktsGroup,
       "cIpMRouteMIBHCInterfaceGroupSup1": cIpMRouteMIBHCInterfaceGroupSup1}
)
