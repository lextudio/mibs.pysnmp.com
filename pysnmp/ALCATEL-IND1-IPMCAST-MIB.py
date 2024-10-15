# SNMP MIB module (ALCATEL-IND1-IPMCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-IPMCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:14 2024
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

(routingIND1Ipmrm,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Ipmrm")

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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

alaIpMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2)
)
alaIpMcastMIB.setRevisions(
        ("2007-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlaIpMcastMIBObjects_ObjectIdentity = ObjectIdentity
alaIpMcastMIBObjects = _AlaIpMcastMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1)
)
_AlaIpMcast_ObjectIdentity = ObjectIdentity
alaIpMcast = _AlaIpMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1)
)


class _AlaIpMcastEnable_Type(Integer32):
    """Custom type alaIpMcastEnable based on Integer32"""
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


_AlaIpMcastEnable_Type.__name__ = "Integer32"
_AlaIpMcastEnable_Object = MibScalar
alaIpMcastEnable = _AlaIpMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 1),
    _AlaIpMcastEnable_Type()
)
alaIpMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpMcastEnable.setStatus("current")
_AlaIpMcastRouteTable_Object = MibTable
alaIpMcastRouteTable = _AlaIpMcastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpMcastRouteTable.setStatus("current")
_AlaIpMcastRouteEntry_Object = MibTableRow
alaIpMcastRouteEntry = _AlaIpMcastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1)
)
alaIpMcastRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteGroupAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteGroup"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteGroupPrefixLength"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteSourceAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteSource"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteSourcePrefixLength"),
)
if mibBuilder.loadTexts:
    alaIpMcastRouteEntry.setStatus("current")
_AlaIpMcastRouteGroupAddressType_Type = InetAddressType
_AlaIpMcastRouteGroupAddressType_Object = MibTableColumn
alaIpMcastRouteGroupAddressType = _AlaIpMcastRouteGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 1),
    _AlaIpMcastRouteGroupAddressType_Type()
)
alaIpMcastRouteGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteGroupAddressType.setStatus("current")


class _AlaIpMcastRouteGroup_Type(InetAddress):
    """Custom type alaIpMcastRouteGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastRouteGroup_Type.__name__ = "InetAddress"
_AlaIpMcastRouteGroup_Object = MibTableColumn
alaIpMcastRouteGroup = _AlaIpMcastRouteGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 2),
    _AlaIpMcastRouteGroup_Type()
)
alaIpMcastRouteGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteGroup.setStatus("current")


class _AlaIpMcastRouteGroupPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIpMcastRouteGroupPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaIpMcastRouteGroupPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIpMcastRouteGroupPrefixLength_Object = MibTableColumn
alaIpMcastRouteGroupPrefixLength = _AlaIpMcastRouteGroupPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 3),
    _AlaIpMcastRouteGroupPrefixLength_Type()
)
alaIpMcastRouteGroupPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteGroupPrefixLength.setStatus("current")
_AlaIpMcastRouteSourceAddressType_Type = InetAddressType
_AlaIpMcastRouteSourceAddressType_Object = MibTableColumn
alaIpMcastRouteSourceAddressType = _AlaIpMcastRouteSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 4),
    _AlaIpMcastRouteSourceAddressType_Type()
)
alaIpMcastRouteSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteSourceAddressType.setStatus("current")


class _AlaIpMcastRouteSource_Type(InetAddress):
    """Custom type alaIpMcastRouteSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastRouteSource_Type.__name__ = "InetAddress"
_AlaIpMcastRouteSource_Object = MibTableColumn
alaIpMcastRouteSource = _AlaIpMcastRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 5),
    _AlaIpMcastRouteSource_Type()
)
alaIpMcastRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteSource.setStatus("current")


class _AlaIpMcastRouteSourcePrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIpMcastRouteSourcePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaIpMcastRouteSourcePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIpMcastRouteSourcePrefixLength_Object = MibTableColumn
alaIpMcastRouteSourcePrefixLength = _AlaIpMcastRouteSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 6),
    _AlaIpMcastRouteSourcePrefixLength_Type()
)
alaIpMcastRouteSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteSourcePrefixLength.setStatus("current")
_AlaIpMcastRouteUpstreamNeighborType_Type = InetAddressType
_AlaIpMcastRouteUpstreamNeighborType_Object = MibTableColumn
alaIpMcastRouteUpstreamNeighborType = _AlaIpMcastRouteUpstreamNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 7),
    _AlaIpMcastRouteUpstreamNeighborType_Type()
)
alaIpMcastRouteUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteUpstreamNeighborType.setStatus("current")
_AlaIpMcastRouteUpstreamNeighbor_Type = InetAddress
_AlaIpMcastRouteUpstreamNeighbor_Object = MibTableColumn
alaIpMcastRouteUpstreamNeighbor = _AlaIpMcastRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 8),
    _AlaIpMcastRouteUpstreamNeighbor_Type()
)
alaIpMcastRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteUpstreamNeighbor.setStatus("current")
_AlaIpMcastRouteInIfIndex_Type = InterfaceIndexOrZero
_AlaIpMcastRouteInIfIndex_Object = MibTableColumn
alaIpMcastRouteInIfIndex = _AlaIpMcastRouteInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 9),
    _AlaIpMcastRouteInIfIndex_Type()
)
alaIpMcastRouteInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteInIfIndex.setStatus("current")
_AlaIpMcastRouteTimeStamp_Type = TimeStamp
_AlaIpMcastRouteTimeStamp_Object = MibTableColumn
alaIpMcastRouteTimeStamp = _AlaIpMcastRouteTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 10),
    _AlaIpMcastRouteTimeStamp_Type()
)
alaIpMcastRouteTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteTimeStamp.setStatus("current")
_AlaIpMcastRouteExpiryTime_Type = TimeTicks
_AlaIpMcastRouteExpiryTime_Object = MibTableColumn
alaIpMcastRouteExpiryTime = _AlaIpMcastRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 11),
    _AlaIpMcastRouteExpiryTime_Type()
)
alaIpMcastRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteExpiryTime.setStatus("current")
_AlaIpMcastRoutePkts_Type = Counter32
_AlaIpMcastRoutePkts_Object = MibTableColumn
alaIpMcastRoutePkts = _AlaIpMcastRoutePkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 12),
    _AlaIpMcastRoutePkts_Type()
)
alaIpMcastRoutePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRoutePkts.setStatus("current")
_AlaIpMcastRouteDifferentInIfPackets_Type = Counter32
_AlaIpMcastRouteDifferentInIfPackets_Object = MibTableColumn
alaIpMcastRouteDifferentInIfPackets = _AlaIpMcastRouteDifferentInIfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 13),
    _AlaIpMcastRouteDifferentInIfPackets_Type()
)
alaIpMcastRouteDifferentInIfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteDifferentInIfPackets.setStatus("current")
_AlaIpMcastRouteOctets_Type = Counter32
_AlaIpMcastRouteOctets_Object = MibTableColumn
alaIpMcastRouteOctets = _AlaIpMcastRouteOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 14),
    _AlaIpMcastRouteOctets_Type()
)
alaIpMcastRouteOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteOctets.setStatus("current")
_AlaIpMcastRouteProtocol_Type = IANAipMRouteProtocol
_AlaIpMcastRouteProtocol_Object = MibTableColumn
alaIpMcastRouteProtocol = _AlaIpMcastRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 15),
    _AlaIpMcastRouteProtocol_Type()
)
alaIpMcastRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteProtocol.setStatus("current")
_AlaIpMcastRouteRtProtocol_Type = IANAipRouteProtocol
_AlaIpMcastRouteRtProtocol_Object = MibTableColumn
alaIpMcastRouteRtProtocol = _AlaIpMcastRouteRtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 16),
    _AlaIpMcastRouteRtProtocol_Type()
)
alaIpMcastRouteRtProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteRtProtocol.setStatus("current")
_AlaIpMcastRouteRtAddressType_Type = InetAddressType
_AlaIpMcastRouteRtAddressType_Object = MibTableColumn
alaIpMcastRouteRtAddressType = _AlaIpMcastRouteRtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 17),
    _AlaIpMcastRouteRtAddressType_Type()
)
alaIpMcastRouteRtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteRtAddressType.setStatus("current")
_AlaIpMcastRouteRtAddress_Type = InetAddress
_AlaIpMcastRouteRtAddress_Object = MibTableColumn
alaIpMcastRouteRtAddress = _AlaIpMcastRouteRtAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 18),
    _AlaIpMcastRouteRtAddress_Type()
)
alaIpMcastRouteRtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteRtAddress.setStatus("current")


class _AlaIpMcastRouteRtPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIpMcastRouteRtPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaIpMcastRouteRtPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIpMcastRouteRtPrefixLength_Object = MibTableColumn
alaIpMcastRouteRtPrefixLength = _AlaIpMcastRouteRtPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 19),
    _AlaIpMcastRouteRtPrefixLength_Type()
)
alaIpMcastRouteRtPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteRtPrefixLength.setStatus("current")


class _AlaIpMcastRouteRtType_Type(Integer32):
    """Custom type alaIpMcastRouteRtType based on Integer32"""
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


_AlaIpMcastRouteRtType_Type.__name__ = "Integer32"
_AlaIpMcastRouteRtType_Object = MibTableColumn
alaIpMcastRouteRtType = _AlaIpMcastRouteRtType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 20),
    _AlaIpMcastRouteRtType_Type()
)
alaIpMcastRouteRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteRtType.setStatus("current")
_AlaIpMcastRouteHCOctets_Type = Counter64
_AlaIpMcastRouteHCOctets_Object = MibTableColumn
alaIpMcastRouteHCOctets = _AlaIpMcastRouteHCOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 21),
    _AlaIpMcastRouteHCOctets_Type()
)
alaIpMcastRouteHCOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteHCOctets.setStatus("current")
_AlaIpMcastRouteDifferentInIfOctets_Type = Counter32
_AlaIpMcastRouteDifferentInIfOctets_Object = MibTableColumn
alaIpMcastRouteDifferentInIfOctets = _AlaIpMcastRouteDifferentInIfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 22),
    _AlaIpMcastRouteDifferentInIfOctets_Type()
)
alaIpMcastRouteDifferentInIfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteDifferentInIfOctets.setStatus("current")
_AlaIpMcastRouteTtlDropPackets_Type = Counter32
_AlaIpMcastRouteTtlDropPackets_Object = MibTableColumn
alaIpMcastRouteTtlDropPackets = _AlaIpMcastRouteTtlDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 23),
    _AlaIpMcastRouteTtlDropPackets_Type()
)
alaIpMcastRouteTtlDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteTtlDropPackets.setStatus("current")
_AlaIpMcastRouteTtlDropOctets_Type = Counter32
_AlaIpMcastRouteTtlDropOctets_Object = MibTableColumn
alaIpMcastRouteTtlDropOctets = _AlaIpMcastRouteTtlDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 2, 1, 24),
    _AlaIpMcastRouteTtlDropOctets_Type()
)
alaIpMcastRouteTtlDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteTtlDropOctets.setStatus("current")
_AlaIpMcastRouteNextHopTable_Object = MibTable
alaIpMcastRouteNextHopTable = _AlaIpMcastRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopTable.setStatus("current")
_AlaIpMcastRouteNextHopEntry_Object = MibTableRow
alaIpMcastRouteNextHopEntry = _AlaIpMcastRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1)
)
alaIpMcastRouteNextHopEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopGroupAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopGroup"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopSourceAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopSource"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopSourcePrefixLength"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopIfIndex"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopEntry.setStatus("current")
_AlaIpMcastRouteNextHopGroupAddressType_Type = InetAddressType
_AlaIpMcastRouteNextHopGroupAddressType_Object = MibTableColumn
alaIpMcastRouteNextHopGroupAddressType = _AlaIpMcastRouteNextHopGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 1),
    _AlaIpMcastRouteNextHopGroupAddressType_Type()
)
alaIpMcastRouteNextHopGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopGroupAddressType.setStatus("current")


class _AlaIpMcastRouteNextHopGroup_Type(InetAddress):
    """Custom type alaIpMcastRouteNextHopGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastRouteNextHopGroup_Type.__name__ = "InetAddress"
_AlaIpMcastRouteNextHopGroup_Object = MibTableColumn
alaIpMcastRouteNextHopGroup = _AlaIpMcastRouteNextHopGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 2),
    _AlaIpMcastRouteNextHopGroup_Type()
)
alaIpMcastRouteNextHopGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopGroup.setStatus("current")
_AlaIpMcastRouteNextHopSourceAddressType_Type = InetAddressType
_AlaIpMcastRouteNextHopSourceAddressType_Object = MibTableColumn
alaIpMcastRouteNextHopSourceAddressType = _AlaIpMcastRouteNextHopSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 3),
    _AlaIpMcastRouteNextHopSourceAddressType_Type()
)
alaIpMcastRouteNextHopSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopSourceAddressType.setStatus("current")


class _AlaIpMcastRouteNextHopSource_Type(InetAddress):
    """Custom type alaIpMcastRouteNextHopSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastRouteNextHopSource_Type.__name__ = "InetAddress"
_AlaIpMcastRouteNextHopSource_Object = MibTableColumn
alaIpMcastRouteNextHopSource = _AlaIpMcastRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 4),
    _AlaIpMcastRouteNextHopSource_Type()
)
alaIpMcastRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopSource.setStatus("current")


class _AlaIpMcastRouteNextHopSourcePrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIpMcastRouteNextHopSourcePrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaIpMcastRouteNextHopSourcePrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIpMcastRouteNextHopSourcePrefixLength_Object = MibTableColumn
alaIpMcastRouteNextHopSourcePrefixLength = _AlaIpMcastRouteNextHopSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 5),
    _AlaIpMcastRouteNextHopSourcePrefixLength_Type()
)
alaIpMcastRouteNextHopSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopSourcePrefixLength.setStatus("current")
_AlaIpMcastRouteNextHopIfIndex_Type = InterfaceIndex
_AlaIpMcastRouteNextHopIfIndex_Object = MibTableColumn
alaIpMcastRouteNextHopIfIndex = _AlaIpMcastRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 6),
    _AlaIpMcastRouteNextHopIfIndex_Type()
)
alaIpMcastRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopIfIndex.setStatus("current")
_AlaIpMcastRouteNextHopAddressType_Type = InetAddressType
_AlaIpMcastRouteNextHopAddressType_Object = MibTableColumn
alaIpMcastRouteNextHopAddressType = _AlaIpMcastRouteNextHopAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 7),
    _AlaIpMcastRouteNextHopAddressType_Type()
)
alaIpMcastRouteNextHopAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopAddressType.setStatus("current")


class _AlaIpMcastRouteNextHopAddress_Type(InetAddress):
    """Custom type alaIpMcastRouteNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastRouteNextHopAddress_Type.__name__ = "InetAddress"
_AlaIpMcastRouteNextHopAddress_Object = MibTableColumn
alaIpMcastRouteNextHopAddress = _AlaIpMcastRouteNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 8),
    _AlaIpMcastRouteNextHopAddress_Type()
)
alaIpMcastRouteNextHopAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopAddress.setStatus("current")


class _AlaIpMcastRouteNextHopState_Type(Integer32):
    """Custom type alaIpMcastRouteNextHopState based on Integer32"""
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


_AlaIpMcastRouteNextHopState_Type.__name__ = "Integer32"
_AlaIpMcastRouteNextHopState_Object = MibTableColumn
alaIpMcastRouteNextHopState = _AlaIpMcastRouteNextHopState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 9),
    _AlaIpMcastRouteNextHopState_Type()
)
alaIpMcastRouteNextHopState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopState.setStatus("current")
_AlaIpMcastRouteNextHopTimeStamp_Type = TimeStamp
_AlaIpMcastRouteNextHopTimeStamp_Object = MibTableColumn
alaIpMcastRouteNextHopTimeStamp = _AlaIpMcastRouteNextHopTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 10),
    _AlaIpMcastRouteNextHopTimeStamp_Type()
)
alaIpMcastRouteNextHopTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopTimeStamp.setStatus("current")
_AlaIpMcastRouteNextHopExpiryTime_Type = TimeTicks
_AlaIpMcastRouteNextHopExpiryTime_Object = MibTableColumn
alaIpMcastRouteNextHopExpiryTime = _AlaIpMcastRouteNextHopExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 11),
    _AlaIpMcastRouteNextHopExpiryTime_Type()
)
alaIpMcastRouteNextHopExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopExpiryTime.setStatus("current")


class _AlaIpMcastRouteNextHopClosestMemberHops_Type(Unsigned32):
    """Custom type alaIpMcastRouteNextHopClosestMemberHops based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaIpMcastRouteNextHopClosestMemberHops_Type.__name__ = "Unsigned32"
_AlaIpMcastRouteNextHopClosestMemberHops_Object = MibTableColumn
alaIpMcastRouteNextHopClosestMemberHops = _AlaIpMcastRouteNextHopClosestMemberHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 12),
    _AlaIpMcastRouteNextHopClosestMemberHops_Type()
)
alaIpMcastRouteNextHopClosestMemberHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopClosestMemberHops.setStatus("current")
_AlaIpMcastRouteNextHopProtocol_Type = IANAipMRouteProtocol
_AlaIpMcastRouteNextHopProtocol_Object = MibTableColumn
alaIpMcastRouteNextHopProtocol = _AlaIpMcastRouteNextHopProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 13),
    _AlaIpMcastRouteNextHopProtocol_Type()
)
alaIpMcastRouteNextHopProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopProtocol.setStatus("current")
_AlaIpMcastRouteNextHopPkts_Type = Counter32
_AlaIpMcastRouteNextHopPkts_Object = MibTableColumn
alaIpMcastRouteNextHopPkts = _AlaIpMcastRouteNextHopPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 14),
    _AlaIpMcastRouteNextHopPkts_Type()
)
alaIpMcastRouteNextHopPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopPkts.setStatus("current")
_AlaIpMcastRouteNextHopOctets_Type = Counter32
_AlaIpMcastRouteNextHopOctets_Object = MibTableColumn
alaIpMcastRouteNextHopOctets = _AlaIpMcastRouteNextHopOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 3, 1, 15),
    _AlaIpMcastRouteNextHopOctets_Type()
)
alaIpMcastRouteNextHopOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteNextHopOctets.setStatus("current")
_AlaIpMcastInterfaceTable_Object = MibTable
alaIpMcastInterfaceTable = _AlaIpMcastInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaIpMcastInterfaceTable.setStatus("current")
_AlaIpMcastInterfaceEntry_Object = MibTableRow
alaIpMcastInterfaceEntry = _AlaIpMcastInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1)
)
alaIpMcastInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    alaIpMcastInterfaceEntry.setStatus("current")
_AlaIpMcastInterfaceIfIndex_Type = InterfaceIndex
_AlaIpMcastInterfaceIfIndex_Object = MibTableColumn
alaIpMcastInterfaceIfIndex = _AlaIpMcastInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 1),
    _AlaIpMcastInterfaceIfIndex_Type()
)
alaIpMcastInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceIfIndex.setStatus("current")


class _AlaIpMcastInterfaceTtl_Type(Unsigned32):
    """Custom type alaIpMcastInterfaceTtl based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaIpMcastInterfaceTtl_Type.__name__ = "Unsigned32"
_AlaIpMcastInterfaceTtl_Object = MibTableColumn
alaIpMcastInterfaceTtl = _AlaIpMcastInterfaceTtl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 2),
    _AlaIpMcastInterfaceTtl_Type()
)
alaIpMcastInterfaceTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceTtl.setStatus("current")
_AlaIpMcastInterfaceProtocol_Type = IANAipMRouteProtocol
_AlaIpMcastInterfaceProtocol_Object = MibTableColumn
alaIpMcastInterfaceProtocol = _AlaIpMcastInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 3),
    _AlaIpMcastInterfaceProtocol_Type()
)
alaIpMcastInterfaceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceProtocol.setStatus("deprecated")


class _AlaIpMcastInterfaceRateLimit_Type(Unsigned32):
    """Custom type alaIpMcastInterfaceRateLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaIpMcastInterfaceRateLimit_Type.__name__ = "Unsigned32"
_AlaIpMcastInterfaceRateLimit_Object = MibTableColumn
alaIpMcastInterfaceRateLimit = _AlaIpMcastInterfaceRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 4),
    _AlaIpMcastInterfaceRateLimit_Type()
)
alaIpMcastInterfaceRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceRateLimit.setStatus("current")
_AlaIpMcastInterfaceInMcastOctets_Type = Counter32
_AlaIpMcastInterfaceInMcastOctets_Object = MibTableColumn
alaIpMcastInterfaceInMcastOctets = _AlaIpMcastInterfaceInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 5),
    _AlaIpMcastInterfaceInMcastOctets_Type()
)
alaIpMcastInterfaceInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceInMcastOctets.setStatus("current")
_AlaIpMcastInterfaceOutMcastOctets_Type = Counter32
_AlaIpMcastInterfaceOutMcastOctets_Object = MibTableColumn
alaIpMcastInterfaceOutMcastOctets = _AlaIpMcastInterfaceOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 6),
    _AlaIpMcastInterfaceOutMcastOctets_Type()
)
alaIpMcastInterfaceOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceOutMcastOctets.setStatus("current")
_AlaIpMcastInterfaceInMcastPkts_Type = Counter32
_AlaIpMcastInterfaceInMcastPkts_Object = MibTableColumn
alaIpMcastInterfaceInMcastPkts = _AlaIpMcastInterfaceInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 7),
    _AlaIpMcastInterfaceInMcastPkts_Type()
)
alaIpMcastInterfaceInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceInMcastPkts.setStatus("current")
_AlaIpMcastInterfaceOutMcastPkts_Type = Counter32
_AlaIpMcastInterfaceOutMcastPkts_Object = MibTableColumn
alaIpMcastInterfaceOutMcastPkts = _AlaIpMcastInterfaceOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 8),
    _AlaIpMcastInterfaceOutMcastPkts_Type()
)
alaIpMcastInterfaceOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceOutMcastPkts.setStatus("current")
_AlaIpMcastInterfaceHCInMcastOctets_Type = Counter64
_AlaIpMcastInterfaceHCInMcastOctets_Object = MibTableColumn
alaIpMcastInterfaceHCInMcastOctets = _AlaIpMcastInterfaceHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 9),
    _AlaIpMcastInterfaceHCInMcastOctets_Type()
)
alaIpMcastInterfaceHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceHCInMcastOctets.setStatus("current")
_AlaIpMcastInterfaceHCOutMcastOctets_Type = Counter64
_AlaIpMcastInterfaceHCOutMcastOctets_Object = MibTableColumn
alaIpMcastInterfaceHCOutMcastOctets = _AlaIpMcastInterfaceHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 10),
    _AlaIpMcastInterfaceHCOutMcastOctets_Type()
)
alaIpMcastInterfaceHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceHCOutMcastOctets.setStatus("current")
_AlaIpMcastInterfaceHCInMcastPkts_Type = Counter64
_AlaIpMcastInterfaceHCInMcastPkts_Object = MibTableColumn
alaIpMcastInterfaceHCInMcastPkts = _AlaIpMcastInterfaceHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 11),
    _AlaIpMcastInterfaceHCInMcastPkts_Type()
)
alaIpMcastInterfaceHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceHCInMcastPkts.setStatus("current")
_AlaIpMcastInterfaceHCOutMcastPkts_Type = Counter64
_AlaIpMcastInterfaceHCOutMcastPkts_Object = MibTableColumn
alaIpMcastInterfaceHCOutMcastPkts = _AlaIpMcastInterfaceHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 4, 1, 12),
    _AlaIpMcastInterfaceHCOutMcastPkts_Type()
)
alaIpMcastInterfaceHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastInterfaceHCOutMcastPkts.setStatus("current")
_AlaIpMcastBoundaryTable_Object = MibTable
alaIpMcastBoundaryTable = _AlaIpMcastBoundaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaIpMcastBoundaryTable.setStatus("current")
_AlaIpMcastBoundaryEntry_Object = MibTableRow
alaIpMcastBoundaryEntry = _AlaIpMcastBoundaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1)
)
alaIpMcastBoundaryEntry.setIndexNames(
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryIfIndex"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryAddressType"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryAddress"),
    (0, "ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryAddressPrefixLength"),
)
if mibBuilder.loadTexts:
    alaIpMcastBoundaryEntry.setStatus("current")
_AlaIpMcastBoundaryIfIndex_Type = InterfaceIndex
_AlaIpMcastBoundaryIfIndex_Object = MibTableColumn
alaIpMcastBoundaryIfIndex = _AlaIpMcastBoundaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 1),
    _AlaIpMcastBoundaryIfIndex_Type()
)
alaIpMcastBoundaryIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryIfIndex.setStatus("current")
_AlaIpMcastBoundaryAddressType_Type = InetAddressType
_AlaIpMcastBoundaryAddressType_Object = MibTableColumn
alaIpMcastBoundaryAddressType = _AlaIpMcastBoundaryAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 2),
    _AlaIpMcastBoundaryAddressType_Type()
)
alaIpMcastBoundaryAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryAddressType.setStatus("current")


class _AlaIpMcastBoundaryAddress_Type(InetAddress):
    """Custom type alaIpMcastBoundaryAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaIpMcastBoundaryAddress_Type.__name__ = "InetAddress"
_AlaIpMcastBoundaryAddress_Object = MibTableColumn
alaIpMcastBoundaryAddress = _AlaIpMcastBoundaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 3),
    _AlaIpMcastBoundaryAddress_Type()
)
alaIpMcastBoundaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryAddress.setStatus("current")


class _AlaIpMcastBoundaryAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaIpMcastBoundaryAddressPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_AlaIpMcastBoundaryAddressPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaIpMcastBoundaryAddressPrefixLength_Object = MibTableColumn
alaIpMcastBoundaryAddressPrefixLength = _AlaIpMcastBoundaryAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 4),
    _AlaIpMcastBoundaryAddressPrefixLength_Type()
)
alaIpMcastBoundaryAddressPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryAddressPrefixLength.setStatus("current")
_AlaIpMcastBoundaryStatus_Type = RowStatus
_AlaIpMcastBoundaryStatus_Object = MibTableColumn
alaIpMcastBoundaryStatus = _AlaIpMcastBoundaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 5),
    _AlaIpMcastBoundaryStatus_Type()
)
alaIpMcastBoundaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryStatus.setStatus("current")


class _AlaIpMcastBoundaryStorageType_Type(StorageType):
    """Custom type alaIpMcastBoundaryStorageType based on StorageType"""


_AlaIpMcastBoundaryStorageType_Object = MibTableColumn
alaIpMcastBoundaryStorageType = _AlaIpMcastBoundaryStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 6),
    _AlaIpMcastBoundaryStorageType_Type()
)
alaIpMcastBoundaryStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryStorageType.setStatus("current")
_AlaIpMcastBoundaryDroppedMcastOctets_Type = Counter32
_AlaIpMcastBoundaryDroppedMcastOctets_Object = MibTableColumn
alaIpMcastBoundaryDroppedMcastOctets = _AlaIpMcastBoundaryDroppedMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 7),
    _AlaIpMcastBoundaryDroppedMcastOctets_Type()
)
alaIpMcastBoundaryDroppedMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryDroppedMcastOctets.setStatus("current")
_AlaIpMcastBoundaryDroppedMcastPkts_Type = Counter32
_AlaIpMcastBoundaryDroppedMcastPkts_Object = MibTableColumn
alaIpMcastBoundaryDroppedMcastPkts = _AlaIpMcastBoundaryDroppedMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 8),
    _AlaIpMcastBoundaryDroppedMcastPkts_Type()
)
alaIpMcastBoundaryDroppedMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryDroppedMcastPkts.setStatus("current")
_AlaIpMcastBoundaryHCDroppedMcastOctets_Type = Counter64
_AlaIpMcastBoundaryHCDroppedMcastOctets_Object = MibTableColumn
alaIpMcastBoundaryHCDroppedMcastOctets = _AlaIpMcastBoundaryHCDroppedMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 9),
    _AlaIpMcastBoundaryHCDroppedMcastOctets_Type()
)
alaIpMcastBoundaryHCDroppedMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryHCDroppedMcastOctets.setStatus("current")
_AlaIpMcastBoundaryHCDroppedMcastPkts_Type = Counter64
_AlaIpMcastBoundaryHCDroppedMcastPkts_Object = MibTableColumn
alaIpMcastBoundaryHCDroppedMcastPkts = _AlaIpMcastBoundaryHCDroppedMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 5, 1, 10),
    _AlaIpMcastBoundaryHCDroppedMcastPkts_Type()
)
alaIpMcastBoundaryHCDroppedMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastBoundaryHCDroppedMcastPkts.setStatus("current")
_AlaIpMcastRouteEntryCount_Type = Gauge32
_AlaIpMcastRouteEntryCount_Object = MibScalar
alaIpMcastRouteEntryCount = _AlaIpMcastRouteEntryCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 1, 1, 7),
    _AlaIpMcastRouteEntryCount_Type()
)
alaIpMcastRouteEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpMcastRouteEntryCount.setStatus("current")
_AlaIpMcastMIBConformance_ObjectIdentity = ObjectIdentity
alaIpMcastMIBConformance = _AlaIpMcastMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2)
)
_AlaIpMcastMIBCompliances_ObjectIdentity = ObjectIdentity
alaIpMcastMIBCompliances = _AlaIpMcastMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 1)
)
_AlaIpMcastMIBGroups_ObjectIdentity = ObjectIdentity
alaIpMcastMIBGroups = _AlaIpMcastMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2)
)

# Managed Objects groups

alaIpMcastMIBMRouteBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 1)
)
alaIpMcastMIBMRouteBasicGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastEnable"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteEntryCount"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteUpstreamNeighborType"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteUpstreamNeighbor"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteInIfIndex"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteTimeStamp"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteExpiryTime"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopState"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopTimeStamp"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopExpiryTime"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopProtocol"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopPkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceTtl"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceProtocol"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceRateLimit"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceInMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceOutMcastOctets"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBMRouteBasicGroup.setStatus("deprecated")

alaIpMcastMIBHopCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 2)
)
alaIpMcastMIBHopCountGroup.setObjects(
    ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopClosestMemberHops")
)
if mibBuilder.loadTexts:
    alaIpMcastMIBHopCountGroup.setStatus("current")

alaIpMcastMIBPktsOutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 3)
)
alaIpMcastMIBPktsOutGroup.setObjects(
    ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopPkts")
)
if mibBuilder.loadTexts:
    alaIpMcastMIBPktsOutGroup.setStatus("current")

alaIpMcastMIBHCInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 4)
)
alaIpMcastMIBHCInterfaceGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceHCInMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceHCOutMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceHCInMcastPkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceHCOutMcastPkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteHCOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryHCDroppedMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryHCDroppedMcastPkts"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBHCInterfaceGroup.setStatus("current")

alaIpMcastMIBRouteProtoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 5)
)
alaIpMcastMIBRouteProtoGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteProtocol"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteRtProtocol"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteRtAddressType"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteRtAddress"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteRtPrefixLength"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteRtType"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBRouteProtoGroup.setStatus("current")

alaIpMcastMIBBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 6)
)
alaIpMcastMIBBasicGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastEnable"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteEntryCount"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBBasicGroup.setStatus("current")

alaIpMcastMIBRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 7)
)
alaIpMcastMIBRouteGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteUpstreamNeighborType"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteUpstreamNeighbor"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteInIfIndex"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteTimeStamp"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteExpiryTime"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRoutePkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteDifferentInIfPackets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopState"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopTimeStamp"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopExpiryTime"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopProtocol"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopPkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceTtl"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceRateLimit"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceInMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceOutMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteTtlDropPackets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteTtlDropOctets"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBRouteGroup.setStatus("current")

alaIpMcastMIBBoundaryIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 10)
)
alaIpMcastMIBBoundaryIfGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryStatus"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryStorageType"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryDroppedMcastOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastBoundaryDroppedMcastPkts"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBBoundaryIfGroup.setStatus("current")

alaIpMcastMIBIfPktsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 12)
)
alaIpMcastMIBIfPktsGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceInMcastPkts"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastInterfaceOutMcastPkts"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBIfPktsGroup.setStatus("current")

alaIpMcastMIBRouteOctetsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 2, 13)
)
alaIpMcastMIBRouteOctetsGroup.setObjects(
      *(("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteNextHopOctets"),
        ("ALCATEL-IND1-IPMCAST-MIB", "alaIpMcastRouteDifferentInIfOctets"))
)
if mibBuilder.loadTexts:
    alaIpMcastMIBRouteOctetsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaIpMcastMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaIpMcastMIBCompliance.setStatus(
        "current"
    )

alaIpMcastMIBMRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 10, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpMcastMIBMRouteCompliance.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-IPMCAST-MIB",
    **{"alaIpMcastMIB": alaIpMcastMIB,
       "alaIpMcastMIBObjects": alaIpMcastMIBObjects,
       "alaIpMcast": alaIpMcast,
       "alaIpMcastEnable": alaIpMcastEnable,
       "alaIpMcastRouteTable": alaIpMcastRouteTable,
       "alaIpMcastRouteEntry": alaIpMcastRouteEntry,
       "alaIpMcastRouteGroupAddressType": alaIpMcastRouteGroupAddressType,
       "alaIpMcastRouteGroup": alaIpMcastRouteGroup,
       "alaIpMcastRouteGroupPrefixLength": alaIpMcastRouteGroupPrefixLength,
       "alaIpMcastRouteSourceAddressType": alaIpMcastRouteSourceAddressType,
       "alaIpMcastRouteSource": alaIpMcastRouteSource,
       "alaIpMcastRouteSourcePrefixLength": alaIpMcastRouteSourcePrefixLength,
       "alaIpMcastRouteUpstreamNeighborType": alaIpMcastRouteUpstreamNeighborType,
       "alaIpMcastRouteUpstreamNeighbor": alaIpMcastRouteUpstreamNeighbor,
       "alaIpMcastRouteInIfIndex": alaIpMcastRouteInIfIndex,
       "alaIpMcastRouteTimeStamp": alaIpMcastRouteTimeStamp,
       "alaIpMcastRouteExpiryTime": alaIpMcastRouteExpiryTime,
       "alaIpMcastRoutePkts": alaIpMcastRoutePkts,
       "alaIpMcastRouteDifferentInIfPackets": alaIpMcastRouteDifferentInIfPackets,
       "alaIpMcastRouteOctets": alaIpMcastRouteOctets,
       "alaIpMcastRouteProtocol": alaIpMcastRouteProtocol,
       "alaIpMcastRouteRtProtocol": alaIpMcastRouteRtProtocol,
       "alaIpMcastRouteRtAddressType": alaIpMcastRouteRtAddressType,
       "alaIpMcastRouteRtAddress": alaIpMcastRouteRtAddress,
       "alaIpMcastRouteRtPrefixLength": alaIpMcastRouteRtPrefixLength,
       "alaIpMcastRouteRtType": alaIpMcastRouteRtType,
       "alaIpMcastRouteHCOctets": alaIpMcastRouteHCOctets,
       "alaIpMcastRouteDifferentInIfOctets": alaIpMcastRouteDifferentInIfOctets,
       "alaIpMcastRouteTtlDropPackets": alaIpMcastRouteTtlDropPackets,
       "alaIpMcastRouteTtlDropOctets": alaIpMcastRouteTtlDropOctets,
       "alaIpMcastRouteNextHopTable": alaIpMcastRouteNextHopTable,
       "alaIpMcastRouteNextHopEntry": alaIpMcastRouteNextHopEntry,
       "alaIpMcastRouteNextHopGroupAddressType": alaIpMcastRouteNextHopGroupAddressType,
       "alaIpMcastRouteNextHopGroup": alaIpMcastRouteNextHopGroup,
       "alaIpMcastRouteNextHopSourceAddressType": alaIpMcastRouteNextHopSourceAddressType,
       "alaIpMcastRouteNextHopSource": alaIpMcastRouteNextHopSource,
       "alaIpMcastRouteNextHopSourcePrefixLength": alaIpMcastRouteNextHopSourcePrefixLength,
       "alaIpMcastRouteNextHopIfIndex": alaIpMcastRouteNextHopIfIndex,
       "alaIpMcastRouteNextHopAddressType": alaIpMcastRouteNextHopAddressType,
       "alaIpMcastRouteNextHopAddress": alaIpMcastRouteNextHopAddress,
       "alaIpMcastRouteNextHopState": alaIpMcastRouteNextHopState,
       "alaIpMcastRouteNextHopTimeStamp": alaIpMcastRouteNextHopTimeStamp,
       "alaIpMcastRouteNextHopExpiryTime": alaIpMcastRouteNextHopExpiryTime,
       "alaIpMcastRouteNextHopClosestMemberHops": alaIpMcastRouteNextHopClosestMemberHops,
       "alaIpMcastRouteNextHopProtocol": alaIpMcastRouteNextHopProtocol,
       "alaIpMcastRouteNextHopPkts": alaIpMcastRouteNextHopPkts,
       "alaIpMcastRouteNextHopOctets": alaIpMcastRouteNextHopOctets,
       "alaIpMcastInterfaceTable": alaIpMcastInterfaceTable,
       "alaIpMcastInterfaceEntry": alaIpMcastInterfaceEntry,
       "alaIpMcastInterfaceIfIndex": alaIpMcastInterfaceIfIndex,
       "alaIpMcastInterfaceTtl": alaIpMcastInterfaceTtl,
       "alaIpMcastInterfaceProtocol": alaIpMcastInterfaceProtocol,
       "alaIpMcastInterfaceRateLimit": alaIpMcastInterfaceRateLimit,
       "alaIpMcastInterfaceInMcastOctets": alaIpMcastInterfaceInMcastOctets,
       "alaIpMcastInterfaceOutMcastOctets": alaIpMcastInterfaceOutMcastOctets,
       "alaIpMcastInterfaceInMcastPkts": alaIpMcastInterfaceInMcastPkts,
       "alaIpMcastInterfaceOutMcastPkts": alaIpMcastInterfaceOutMcastPkts,
       "alaIpMcastInterfaceHCInMcastOctets": alaIpMcastInterfaceHCInMcastOctets,
       "alaIpMcastInterfaceHCOutMcastOctets": alaIpMcastInterfaceHCOutMcastOctets,
       "alaIpMcastInterfaceHCInMcastPkts": alaIpMcastInterfaceHCInMcastPkts,
       "alaIpMcastInterfaceHCOutMcastPkts": alaIpMcastInterfaceHCOutMcastPkts,
       "alaIpMcastBoundaryTable": alaIpMcastBoundaryTable,
       "alaIpMcastBoundaryEntry": alaIpMcastBoundaryEntry,
       "alaIpMcastBoundaryIfIndex": alaIpMcastBoundaryIfIndex,
       "alaIpMcastBoundaryAddressType": alaIpMcastBoundaryAddressType,
       "alaIpMcastBoundaryAddress": alaIpMcastBoundaryAddress,
       "alaIpMcastBoundaryAddressPrefixLength": alaIpMcastBoundaryAddressPrefixLength,
       "alaIpMcastBoundaryStatus": alaIpMcastBoundaryStatus,
       "alaIpMcastBoundaryStorageType": alaIpMcastBoundaryStorageType,
       "alaIpMcastBoundaryDroppedMcastOctets": alaIpMcastBoundaryDroppedMcastOctets,
       "alaIpMcastBoundaryDroppedMcastPkts": alaIpMcastBoundaryDroppedMcastPkts,
       "alaIpMcastBoundaryHCDroppedMcastOctets": alaIpMcastBoundaryHCDroppedMcastOctets,
       "alaIpMcastBoundaryHCDroppedMcastPkts": alaIpMcastBoundaryHCDroppedMcastPkts,
       "alaIpMcastRouteEntryCount": alaIpMcastRouteEntryCount,
       "alaIpMcastMIBConformance": alaIpMcastMIBConformance,
       "alaIpMcastMIBCompliances": alaIpMcastMIBCompliances,
       "alaIpMcastMIBCompliance": alaIpMcastMIBCompliance,
       "alaIpMcastMIBMRouteCompliance": alaIpMcastMIBMRouteCompliance,
       "alaIpMcastMIBGroups": alaIpMcastMIBGroups,
       "alaIpMcastMIBMRouteBasicGroup": alaIpMcastMIBMRouteBasicGroup,
       "alaIpMcastMIBHopCountGroup": alaIpMcastMIBHopCountGroup,
       "alaIpMcastMIBPktsOutGroup": alaIpMcastMIBPktsOutGroup,
       "alaIpMcastMIBHCInterfaceGroup": alaIpMcastMIBHCInterfaceGroup,
       "alaIpMcastMIBRouteProtoGroup": alaIpMcastMIBRouteProtoGroup,
       "alaIpMcastMIBBasicGroup": alaIpMcastMIBBasicGroup,
       "alaIpMcastMIBRouteGroup": alaIpMcastMIBRouteGroup,
       "alaIpMcastMIBBoundaryIfGroup": alaIpMcastMIBBoundaryIfGroup,
       "alaIpMcastMIBIfPktsGroup": alaIpMcastMIBIfPktsGroup,
       "alaIpMcastMIBRouteOctetsGroup": alaIpMcastMIBRouteOctetsGroup}
)
