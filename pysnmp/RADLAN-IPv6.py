# SNMP MIB module (RADLAN-IPv6) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-IPv6
# Produced by pysmi-1.5.4 at Mon Oct 14 22:42:30 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(IANAtunnelType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAtunnelType")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

(inetCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteEntry")

(ipAddressEntry,
 ipNetToPhysicalEntry,
 ipv6InterfaceEntry,
 ipv6RouterAdvertEntry) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAddressEntry",
    "ipNetToPhysicalEntry",
    "ipv6InterfaceEntry",
    "ipv6RouterAdvertEntry")

(ipSpec,) = mibBuilder.importSymbols(
    "RADLAN-IP",
    "ipSpec")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

rlIPv6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 129)
)
rlIPv6.setRevisions(
        ("2008-09-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlIpAddressTable_Object = MibTable
rlIpAddressTable = _RlIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 19)
)
if mibBuilder.loadTexts:
    rlIpAddressTable.setStatus("current")
_RlIpAddressEntry_Object = MibTableRow
rlIpAddressEntry = _RlIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 19, 1)
)
if mibBuilder.loadTexts:
    rlIpAddressEntry.setStatus("current")


class _RlIpAddressPrefixLength_Type(InetAddressPrefixLength):
    """Custom type rlIpAddressPrefixLength based on InetAddressPrefixLength"""
    defaultValue = 64


_RlIpAddressPrefixLength_Object = MibTableColumn
rlIpAddressPrefixLength = _RlIpAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 19, 1, 1),
    _RlIpAddressPrefixLength_Type()
)
rlIpAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpAddressPrefixLength.setStatus("current")


class _RlIpAddressType_Type(Integer32):
    """Custom type rlIpAddressType based on Integer32"""
    defaultValue = 1

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
        *(("anycast", 2),
          ("broadcast", 3),
          ("multicast", 4),
          ("unicast", 1))
    )


_RlIpAddressType_Type.__name__ = "Integer32"
_RlIpAddressType_Object = MibTableColumn
rlIpAddressType = _RlIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 19, 1, 2),
    _RlIpAddressType_Type()
)
rlIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpAddressType.setStatus("current")
_Rlipv6InterfaceTable_Object = MibTable
rlipv6InterfaceTable = _Rlipv6InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20)
)
if mibBuilder.loadTexts:
    rlipv6InterfaceTable.setStatus("current")
_Rlipv6InterfaceEntry_Object = MibTableRow
rlipv6InterfaceEntry = _Rlipv6InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1)
)
if mibBuilder.loadTexts:
    rlipv6InterfaceEntry.setStatus("current")


class _Rlipv6InterfaceNdDadAttemps_Type(Integer32):
    """Custom type rlipv6InterfaceNdDadAttemps based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Rlipv6InterfaceNdDadAttemps_Type.__name__ = "Integer32"
_Rlipv6InterfaceNdDadAttemps_Object = MibTableColumn
rlipv6InterfaceNdDadAttemps = _Rlipv6InterfaceNdDadAttemps_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 1),
    _Rlipv6InterfaceNdDadAttemps_Type()
)
rlipv6InterfaceNdDadAttemps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceNdDadAttemps.setStatus("current")


class _Rlipv6InterfaceAutoconfigEnable_Type(Integer32):
    """Custom type rlipv6InterfaceAutoconfigEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Rlipv6InterfaceAutoconfigEnable_Type.__name__ = "Integer32"
_Rlipv6InterfaceAutoconfigEnable_Object = MibTableColumn
rlipv6InterfaceAutoconfigEnable = _Rlipv6InterfaceAutoconfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 2),
    _Rlipv6InterfaceAutoconfigEnable_Type()
)
rlipv6InterfaceAutoconfigEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceAutoconfigEnable.setStatus("current")


class _Rlipv6InterfaceIcmpUnreachSendEnable_Type(Integer32):
    """Custom type rlipv6InterfaceIcmpUnreachSendEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Rlipv6InterfaceIcmpUnreachSendEnable_Type.__name__ = "Integer32"
_Rlipv6InterfaceIcmpUnreachSendEnable_Object = MibTableColumn
rlipv6InterfaceIcmpUnreachSendEnable = _Rlipv6InterfaceIcmpUnreachSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 3),
    _Rlipv6InterfaceIcmpUnreachSendEnable_Type()
)
rlipv6InterfaceIcmpUnreachSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceIcmpUnreachSendEnable.setStatus("current")


class _Rlipv6InterfaceLinkMTU_Type(Unsigned32):
    """Custom type rlipv6InterfaceLinkMTU based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1280, 65535),
    )


_Rlipv6InterfaceLinkMTU_Type.__name__ = "Unsigned32"
_Rlipv6InterfaceLinkMTU_Object = MibTableColumn
rlipv6InterfaceLinkMTU = _Rlipv6InterfaceLinkMTU_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 4),
    _Rlipv6InterfaceLinkMTU_Type()
)
rlipv6InterfaceLinkMTU.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceLinkMTU.setStatus("current")


class _Rlipv6InterfaceMLDVersion_Type(Unsigned32):
    """Custom type rlipv6InterfaceMLDVersion based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Rlipv6InterfaceMLDVersion_Type.__name__ = "Unsigned32"
_Rlipv6InterfaceMLDVersion_Object = MibTableColumn
rlipv6InterfaceMLDVersion = _Rlipv6InterfaceMLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 5),
    _Rlipv6InterfaceMLDVersion_Type()
)
rlipv6InterfaceMLDVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceMLDVersion.setStatus("current")


class _Rlipv6InterfaceRetransmitTime_Type(Unsigned32):
    """Custom type rlipv6InterfaceRetransmitTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1000, 3600000),
    )


_Rlipv6InterfaceRetransmitTime_Type.__name__ = "Unsigned32"
_Rlipv6InterfaceRetransmitTime_Object = MibTableColumn
rlipv6InterfaceRetransmitTime = _Rlipv6InterfaceRetransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 6),
    _Rlipv6InterfaceRetransmitTime_Type()
)
rlipv6InterfaceRetransmitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceRetransmitTime.setStatus("current")
if mibBuilder.loadTexts:
    rlipv6InterfaceRetransmitTime.setUnits("milliseconds")


class _Rlipv6InterfaceIcmpRedirectSendEnable_Type(Integer32):
    """Custom type rlipv6InterfaceIcmpRedirectSendEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Rlipv6InterfaceIcmpRedirectSendEnable_Type.__name__ = "Integer32"
_Rlipv6InterfaceIcmpRedirectSendEnable_Object = MibTableColumn
rlipv6InterfaceIcmpRedirectSendEnable = _Rlipv6InterfaceIcmpRedirectSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 20, 1, 7),
    _Rlipv6InterfaceIcmpRedirectSendEnable_Type()
)
rlipv6InterfaceIcmpRedirectSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlipv6InterfaceIcmpRedirectSendEnable.setStatus("current")
_RlinetCidrRouteTable_Object = MibTable
rlinetCidrRouteTable = _RlinetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 21)
)
if mibBuilder.loadTexts:
    rlinetCidrRouteTable.setStatus("current")
_RlinetCidrRouteEntry_Object = MibTableRow
rlinetCidrRouteEntry = _RlinetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 21, 1)
)
if mibBuilder.loadTexts:
    rlinetCidrRouteEntry.setStatus("current")


class _RlinetCidrRouteLifetime_Type(Unsigned32):
    """Custom type rlinetCidrRouteLifetime based on Unsigned32"""
    defaultValue = 4294967295


_RlinetCidrRouteLifetime_Object = MibTableColumn
rlinetCidrRouteLifetime = _RlinetCidrRouteLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 21, 1, 1),
    _RlinetCidrRouteLifetime_Type()
)
rlinetCidrRouteLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlinetCidrRouteLifetime.setStatus("current")
if mibBuilder.loadTexts:
    rlinetCidrRouteLifetime.setUnits("seconds")


class _RlinetCidrRouteInfo_Type(Integer32):
    """Custom type rlinetCidrRouteInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ospfExternalType1", 3),
          ("ospfExternalType2", 4),
          ("ospfInterArea", 2),
          ("ospfIntraArea", 1))
    )


_RlinetCidrRouteInfo_Type.__name__ = "Integer32"
_RlinetCidrRouteInfo_Object = MibTableColumn
rlinetCidrRouteInfo = _RlinetCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 21, 1, 2),
    _RlinetCidrRouteInfo_Type()
)
rlinetCidrRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlinetCidrRouteInfo.setStatus("current")
_RlipNetToPhysicalTable_Object = MibTable
rlipNetToPhysicalTable = _RlipNetToPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 22)
)
if mibBuilder.loadTexts:
    rlipNetToPhysicalTable.setStatus("current")
_RlipNetToPhysicalEntry_Object = MibTableRow
rlipNetToPhysicalEntry = _RlipNetToPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 22, 1)
)
if mibBuilder.loadTexts:
    rlipNetToPhysicalEntry.setStatus("current")
_RlipNetToPhysicalIsRouter_Type = TruthValue
_RlipNetToPhysicalIsRouter_Object = MibTableColumn
rlipNetToPhysicalIsRouter = _RlipNetToPhysicalIsRouter_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 22, 1, 1),
    _RlipNetToPhysicalIsRouter_Type()
)
rlipNetToPhysicalIsRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlipNetToPhysicalIsRouter.setStatus("current")
_RlipNetToPhysicalReachableConfirmed_Type = Unsigned32
_RlipNetToPhysicalReachableConfirmed_Object = MibTableColumn
rlipNetToPhysicalReachableConfirmed = _RlipNetToPhysicalReachableConfirmed_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 22, 1, 2),
    _RlipNetToPhysicalReachableConfirmed_Type()
)
rlipNetToPhysicalReachableConfirmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlipNetToPhysicalReachableConfirmed.setStatus("current")
_RlInetStaticRouteTable_Object = MibTable
rlInetStaticRouteTable = _RlInetStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28)
)
if mibBuilder.loadTexts:
    rlInetStaticRouteTable.setStatus("current")
_RlInetStaticRouteEntry_Object = MibTableRow
rlInetStaticRouteEntry = _RlInetStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1)
)
rlInetStaticRouteEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlInetStaticRouteDestType"),
    (0, "RADLAN-IPv6", "rlInetStaticRouteDest"),
    (0, "RADLAN-IPv6", "rlInetStaticRoutePfxLen"),
    (0, "RADLAN-IPv6", "rlInetStaticRouteNextHopType"),
    (0, "RADLAN-IPv6", "rlInetStaticRouteNextHop"),
    (0, "RADLAN-IPv6", "rlInetStaticRouteIfIndex"),
)
if mibBuilder.loadTexts:
    rlInetStaticRouteEntry.setStatus("current")
_RlInetStaticRouteDestType_Type = InetAddressType
_RlInetStaticRouteDestType_Object = MibTableColumn
rlInetStaticRouteDestType = _RlInetStaticRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 1),
    _RlInetStaticRouteDestType_Type()
)
rlInetStaticRouteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetStaticRouteDestType.setStatus("current")
_RlInetStaticRouteDest_Type = InetAddress
_RlInetStaticRouteDest_Object = MibTableColumn
rlInetStaticRouteDest = _RlInetStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 2),
    _RlInetStaticRouteDest_Type()
)
rlInetStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInetStaticRouteDest.setStatus("current")
_RlInetStaticRoutePfxLen_Type = InetAddressPrefixLength
_RlInetStaticRoutePfxLen_Object = MibTableColumn
rlInetStaticRoutePfxLen = _RlInetStaticRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 3),
    _RlInetStaticRoutePfxLen_Type()
)
rlInetStaticRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInetStaticRoutePfxLen.setStatus("current")
_RlInetStaticRouteNextHopType_Type = InetAddressType
_RlInetStaticRouteNextHopType_Object = MibTableColumn
rlInetStaticRouteNextHopType = _RlInetStaticRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 4),
    _RlInetStaticRouteNextHopType_Type()
)
rlInetStaticRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInetStaticRouteNextHopType.setStatus("current")
_RlInetStaticRouteNextHop_Type = InetAddress
_RlInetStaticRouteNextHop_Object = MibTableColumn
rlInetStaticRouteNextHop = _RlInetStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 5),
    _RlInetStaticRouteNextHop_Type()
)
rlInetStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInetStaticRouteNextHop.setStatus("current")


class _RlInetStaticRouteIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlInetStaticRouteIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlInetStaticRouteIfIndex_Object = MibTableColumn
rlInetStaticRouteIfIndex = _RlInetStaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 6),
    _RlInetStaticRouteIfIndex_Type()
)
rlInetStaticRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInetStaticRouteIfIndex.setStatus("current")


class _RlInetStaticRoutePathCost_Type(Unsigned32):
    """Custom type rlInetStaticRoutePathCost based on Unsigned32"""
    defaultValue = 1


_RlInetStaticRoutePathCost_Object = MibTableColumn
rlInetStaticRoutePathCost = _RlInetStaticRoutePathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 7),
    _RlInetStaticRoutePathCost_Type()
)
rlInetStaticRoutePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetStaticRoutePathCost.setStatus("current")


class _RlInetStaticRouteType_Type(Integer32):
    """Custom type rlInetStaticRouteType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 5),
          ("local", 3),
          ("nd", 6),
          ("reject", 2),
          ("remote", 4))
    )


_RlInetStaticRouteType_Type.__name__ = "Integer32"
_RlInetStaticRouteType_Object = MibTableColumn
rlInetStaticRouteType = _RlInetStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 8),
    _RlInetStaticRouteType_Type()
)
rlInetStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetStaticRouteType.setStatus("current")


class _RlInetStaticRouteOwner_Type(Integer32):
    """Custom type rlInetStaticRouteOwner based on Integer32"""
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
        *(("default", 3),
          ("dhcp", 2),
          ("icmp", 4),
          ("static", 1))
    )


_RlInetStaticRouteOwner_Type.__name__ = "Integer32"
_RlInetStaticRouteOwner_Object = MibTableColumn
rlInetStaticRouteOwner = _RlInetStaticRouteOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 9),
    _RlInetStaticRouteOwner_Type()
)
rlInetStaticRouteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetStaticRouteOwner.setStatus("current")
_RlInetStaticRouteRowStatus_Type = RowStatus
_RlInetStaticRouteRowStatus_Object = MibTableColumn
rlInetStaticRouteRowStatus = _RlInetStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 10),
    _RlInetStaticRouteRowStatus_Type()
)
rlInetStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetStaticRouteRowStatus.setStatus("current")


class _RlInetStaticRouteForwardingStatus_Type(Integer32):
    """Custom type rlInetStaticRouteForwardingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlInetStaticRouteForwardingStatus_Type.__name__ = "Integer32"
_RlInetStaticRouteForwardingStatus_Object = MibTableColumn
rlInetStaticRouteForwardingStatus = _RlInetStaticRouteForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 28, 1, 11),
    _RlInetStaticRouteForwardingStatus_Type()
)
rlInetStaticRouteForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetStaticRouteForwardingStatus.setStatus("current")
_RlInetRoutingDistanceTable_Object = MibTable
rlInetRoutingDistanceTable = _RlInetRoutingDistanceTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29)
)
if mibBuilder.loadTexts:
    rlInetRoutingDistanceTable.setStatus("current")
_RlInetRoutingDistanceEntry_Object = MibTableRow
rlInetRoutingDistanceEntry = _RlInetRoutingDistanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1)
)
rlInetRoutingDistanceEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlInetRoutingDistanceType"),
)
if mibBuilder.loadTexts:
    rlInetRoutingDistanceEntry.setStatus("current")


class _RlInetRoutingDistanceType_Type(Integer32):
    """Custom type rlInetRoutingDistanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_RlInetRoutingDistanceType_Type.__name__ = "Integer32"
_RlInetRoutingDistanceType_Object = MibTableColumn
rlInetRoutingDistanceType = _RlInetRoutingDistanceType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 1),
    _RlInetRoutingDistanceType_Type()
)
rlInetRoutingDistanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceType.setStatus("current")


class _RlInetRoutingDistanceConnected_Type(Integer32):
    """Custom type rlInetRoutingDistanceConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlInetRoutingDistanceConnected_Type.__name__ = "Integer32"
_RlInetRoutingDistanceConnected_Object = MibTableColumn
rlInetRoutingDistanceConnected = _RlInetRoutingDistanceConnected_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 2),
    _RlInetRoutingDistanceConnected_Type()
)
rlInetRoutingDistanceConnected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceConnected.setStatus("current")


class _RlInetRoutingDistanceStatic_Type(Integer32):
    """Custom type rlInetRoutingDistanceStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlInetRoutingDistanceStatic_Type.__name__ = "Integer32"
_RlInetRoutingDistanceStatic_Object = MibTableColumn
rlInetRoutingDistanceStatic = _RlInetRoutingDistanceStatic_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 3),
    _RlInetRoutingDistanceStatic_Type()
)
rlInetRoutingDistanceStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceStatic.setStatus("current")


class _RlInetRoutingDistanceRip_Type(Integer32):
    """Custom type rlInetRoutingDistanceRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlInetRoutingDistanceRip_Type.__name__ = "Integer32"
_RlInetRoutingDistanceRip_Object = MibTableColumn
rlInetRoutingDistanceRip = _RlInetRoutingDistanceRip_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 4),
    _RlInetRoutingDistanceRip_Type()
)
rlInetRoutingDistanceRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceRip.setStatus("current")


class _RlInetRoutingDistanceOspfInternal_Type(Integer32):
    """Custom type rlInetRoutingDistanceOspfInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlInetRoutingDistanceOspfInternal_Type.__name__ = "Integer32"
_RlInetRoutingDistanceOspfInternal_Object = MibTableColumn
rlInetRoutingDistanceOspfInternal = _RlInetRoutingDistanceOspfInternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 5),
    _RlInetRoutingDistanceOspfInternal_Type()
)
rlInetRoutingDistanceOspfInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceOspfInternal.setStatus("current")


class _RlInetRoutingDistanceOspfExternal_Type(Integer32):
    """Custom type rlInetRoutingDistanceOspfExternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlInetRoutingDistanceOspfExternal_Type.__name__ = "Integer32"
_RlInetRoutingDistanceOspfExternal_Object = MibTableColumn
rlInetRoutingDistanceOspfExternal = _RlInetRoutingDistanceOspfExternal_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 29, 1, 6),
    _RlInetRoutingDistanceOspfExternal_Type()
)
rlInetRoutingDistanceOspfExternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInetRoutingDistanceOspfExternal.setStatus("current")
_RlInternInetCidrRouteTable_Object = MibTable
rlInternInetCidrRouteTable = _RlInternInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30)
)
if mibBuilder.loadTexts:
    rlInternInetCidrRouteTable.setStatus("current")
_RlInternInetCidrRouteEntry_Object = MibTableRow
rlInternInetCidrRouteEntry = _RlInternInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1)
)
rlInternInetCidrRouteEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlInternInetCidrRouteDestType"),
    (0, "RADLAN-IPv6", "rlInternInetCidrRouteDest"),
    (0, "RADLAN-IPv6", "rlInternInetCidrRoutePfxLen"),
    (0, "RADLAN-IPv6", "rlInternInetCidrRoutePolicy"),
    (0, "RADLAN-IPv6", "rlInternInetCidrRouteNextHopType"),
    (0, "RADLAN-IPv6", "rlInternInetCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    rlInternInetCidrRouteEntry.setStatus("current")
_RlInternInetCidrRouteDestType_Type = InetAddressType
_RlInternInetCidrRouteDestType_Object = MibTableColumn
rlInternInetCidrRouteDestType = _RlInternInetCidrRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 1),
    _RlInternInetCidrRouteDestType_Type()
)
rlInternInetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteDestType.setStatus("current")
_RlInternInetCidrRouteDest_Type = InetAddress
_RlInternInetCidrRouteDest_Object = MibTableColumn
rlInternInetCidrRouteDest = _RlInternInetCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 2),
    _RlInternInetCidrRouteDest_Type()
)
rlInternInetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteDest.setStatus("current")
_RlInternInetCidrRoutePfxLen_Type = InetAddressPrefixLength
_RlInternInetCidrRoutePfxLen_Object = MibTableColumn
rlInternInetCidrRoutePfxLen = _RlInternInetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 3),
    _RlInternInetCidrRoutePfxLen_Type()
)
rlInternInetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRoutePfxLen.setStatus("current")
_RlInternInetCidrRoutePolicy_Type = ObjectIdentifier
_RlInternInetCidrRoutePolicy_Object = MibTableColumn
rlInternInetCidrRoutePolicy = _RlInternInetCidrRoutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 4),
    _RlInternInetCidrRoutePolicy_Type()
)
rlInternInetCidrRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRoutePolicy.setStatus("current")
_RlInternInetCidrRouteNextHopType_Type = InetAddressType
_RlInternInetCidrRouteNextHopType_Object = MibTableColumn
rlInternInetCidrRouteNextHopType = _RlInternInetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 5),
    _RlInternInetCidrRouteNextHopType_Type()
)
rlInternInetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteNextHopType.setStatus("current")
_RlInternInetCidrRouteNextHop_Type = InetAddress
_RlInternInetCidrRouteNextHop_Object = MibTableColumn
rlInternInetCidrRouteNextHop = _RlInternInetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 6),
    _RlInternInetCidrRouteNextHop_Type()
)
rlInternInetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteNextHop.setStatus("current")
_RlInternInetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_RlInternInetCidrRouteIfIndex_Object = MibTableColumn
rlInternInetCidrRouteIfIndex = _RlInternInetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 7),
    _RlInternInetCidrRouteIfIndex_Type()
)
rlInternInetCidrRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteIfIndex.setStatus("current")


class _RlInternInetCidrRouteType_Type(Integer32):
    """Custom type rlInternInetCidrRouteType based on Integer32"""
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
        *(("blackhole", 5),
          ("local", 3),
          ("other", 1),
          ("reject", 2),
          ("remote", 4))
    )


_RlInternInetCidrRouteType_Type.__name__ = "Integer32"
_RlInternInetCidrRouteType_Object = MibTableColumn
rlInternInetCidrRouteType = _RlInternInetCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 8),
    _RlInternInetCidrRouteType_Type()
)
rlInternInetCidrRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteType.setStatus("current")
_RlInternInetCidrRouteProto_Type = IANAipRouteProtocol
_RlInternInetCidrRouteProto_Object = MibTableColumn
rlInternInetCidrRouteProto = _RlInternInetCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 9),
    _RlInternInetCidrRouteProto_Type()
)
rlInternInetCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteProto.setStatus("current")
_RlInternInetCidrRouteAge_Type = Gauge32
_RlInternInetCidrRouteAge_Object = MibTableColumn
rlInternInetCidrRouteAge = _RlInternInetCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 10),
    _RlInternInetCidrRouteAge_Type()
)
rlInternInetCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteAge.setStatus("current")


class _RlInternInetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type rlInternInetCidrRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_RlInternInetCidrRouteNextHopAS_Object = MibTableColumn
rlInternInetCidrRouteNextHopAS = _RlInternInetCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 11),
    _RlInternInetCidrRouteNextHopAS_Type()
)
rlInternInetCidrRouteNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteNextHopAS.setStatus("current")


class _RlInternInetCidrRouteMetric1_Type(Integer32):
    """Custom type rlInternInetCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_RlInternInetCidrRouteMetric1_Object = MibTableColumn
rlInternInetCidrRouteMetric1 = _RlInternInetCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 12),
    _RlInternInetCidrRouteMetric1_Type()
)
rlInternInetCidrRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteMetric1.setStatus("current")


class _RlInternInetCidrRouteMetric2_Type(Integer32):
    """Custom type rlInternInetCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_RlInternInetCidrRouteMetric2_Object = MibTableColumn
rlInternInetCidrRouteMetric2 = _RlInternInetCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 13),
    _RlInternInetCidrRouteMetric2_Type()
)
rlInternInetCidrRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteMetric2.setStatus("current")


class _RlInternInetCidrRouteMetric3_Type(Integer32):
    """Custom type rlInternInetCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_RlInternInetCidrRouteMetric3_Object = MibTableColumn
rlInternInetCidrRouteMetric3 = _RlInternInetCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 14),
    _RlInternInetCidrRouteMetric3_Type()
)
rlInternInetCidrRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteMetric3.setStatus("current")


class _RlInternInetCidrRouteMetric4_Type(Integer32):
    """Custom type rlInternInetCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_RlInternInetCidrRouteMetric4_Object = MibTableColumn
rlInternInetCidrRouteMetric4 = _RlInternInetCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 15),
    _RlInternInetCidrRouteMetric4_Type()
)
rlInternInetCidrRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteMetric4.setStatus("current")


class _RlInternInetCidrRouteMetric5_Type(Integer32):
    """Custom type rlInternInetCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_RlInternInetCidrRouteMetric5_Object = MibTableColumn
rlInternInetCidrRouteMetric5 = _RlInternInetCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 16),
    _RlInternInetCidrRouteMetric5_Type()
)
rlInternInetCidrRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteMetric5.setStatus("current")
_RlInternInetCidrRouteStatus_Type = RowStatus
_RlInternInetCidrRouteStatus_Object = MibTableColumn
rlInternInetCidrRouteStatus = _RlInternInetCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 17),
    _RlInternInetCidrRouteStatus_Type()
)
rlInternInetCidrRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteStatus.setStatus("current")


class _RlInternInetCidrRouteLifetime_Type(Unsigned32):
    """Custom type rlInternInetCidrRouteLifetime based on Unsigned32"""
    defaultValue = 4294967295


_RlInternInetCidrRouteLifetime_Object = MibTableColumn
rlInternInetCidrRouteLifetime = _RlInternInetCidrRouteLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 18),
    _RlInternInetCidrRouteLifetime_Type()
)
rlInternInetCidrRouteLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteLifetime.setStatus("current")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteLifetime.setUnits("seconds")


class _RlInternInetCidrRouteInfo_Type(Integer32):
    """Custom type rlInternInetCidrRouteInfo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("ospfExternalType1", 3),
          ("ospfExternalType2", 4),
          ("ospfInterArea", 2),
          ("ospfIntraArea", 1))
    )


_RlInternInetCidrRouteInfo_Type.__name__ = "Integer32"
_RlInternInetCidrRouteInfo_Object = MibTableColumn
rlInternInetCidrRouteInfo = _RlInternInetCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 30, 1, 19),
    _RlInternInetCidrRouteInfo_Type()
)
rlInternInetCidrRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetCidrRouteInfo.setStatus("current")
_RlInternInetStaticRouteTable_Object = MibTable
rlInternInetStaticRouteTable = _RlInternInetStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31)
)
if mibBuilder.loadTexts:
    rlInternInetStaticRouteTable.setStatus("current")
_RlInternInetStaticRouteEntry_Object = MibTableRow
rlInternInetStaticRouteEntry = _RlInternInetStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1)
)
rlInternInetStaticRouteEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlInternInetStaticRouteDestType"),
    (0, "RADLAN-IPv6", "rlInternInetStaticRouteDest"),
    (0, "RADLAN-IPv6", "rlInternInetStaticRoutePfxLen"),
    (0, "RADLAN-IPv6", "rlInternInetStaticRouteNextHopType"),
    (0, "RADLAN-IPv6", "rlInternInetStaticRouteNextHop"),
    (0, "RADLAN-IPv6", "rlInternInetStaticRouteIfIndex"),
)
if mibBuilder.loadTexts:
    rlInternInetStaticRouteEntry.setStatus("current")
_RlInternInetStaticRouteDestType_Type = InetAddressType
_RlInternInetStaticRouteDestType_Object = MibTableColumn
rlInternInetStaticRouteDestType = _RlInternInetStaticRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 1),
    _RlInternInetStaticRouteDestType_Type()
)
rlInternInetStaticRouteDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteDestType.setStatus("current")
_RlInternInetStaticRouteDest_Type = InetAddress
_RlInternInetStaticRouteDest_Object = MibTableColumn
rlInternInetStaticRouteDest = _RlInternInetStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 2),
    _RlInternInetStaticRouteDest_Type()
)
rlInternInetStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteDest.setStatus("current")
_RlInternInetStaticRoutePfxLen_Type = InetAddressPrefixLength
_RlInternInetStaticRoutePfxLen_Object = MibTableColumn
rlInternInetStaticRoutePfxLen = _RlInternInetStaticRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 3),
    _RlInternInetStaticRoutePfxLen_Type()
)
rlInternInetStaticRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetStaticRoutePfxLen.setStatus("current")
_RlInternInetStaticRouteNextHopType_Type = InetAddressType
_RlInternInetStaticRouteNextHopType_Object = MibTableColumn
rlInternInetStaticRouteNextHopType = _RlInternInetStaticRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 4),
    _RlInternInetStaticRouteNextHopType_Type()
)
rlInternInetStaticRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteNextHopType.setStatus("current")
_RlInternInetStaticRouteNextHop_Type = InetAddress
_RlInternInetStaticRouteNextHop_Object = MibTableColumn
rlInternInetStaticRouteNextHop = _RlInternInetStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 5),
    _RlInternInetStaticRouteNextHop_Type()
)
rlInternInetStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteNextHop.setStatus("current")


class _RlInternInetStaticRouteIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlInternInetStaticRouteIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlInternInetStaticRouteIfIndex_Object = MibTableColumn
rlInternInetStaticRouteIfIndex = _RlInternInetStaticRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 6),
    _RlInternInetStaticRouteIfIndex_Type()
)
rlInternInetStaticRouteIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteIfIndex.setStatus("current")
_RlInternInetStaticRoutePathCost_Type = Unsigned32
_RlInternInetStaticRoutePathCost_Object = MibTableColumn
rlInternInetStaticRoutePathCost = _RlInternInetStaticRoutePathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 7),
    _RlInternInetStaticRoutePathCost_Type()
)
rlInternInetStaticRoutePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInternInetStaticRoutePathCost.setStatus("current")


class _RlInternInetStaticRouteType_Type(Integer32):
    """Custom type rlInternInetStaticRouteType based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 5),
          ("local", 3),
          ("nd", 6),
          ("reject", 2),
          ("remote", 4))
    )


_RlInternInetStaticRouteType_Type.__name__ = "Integer32"
_RlInternInetStaticRouteType_Object = MibTableColumn
rlInternInetStaticRouteType = _RlInternInetStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 8),
    _RlInternInetStaticRouteType_Type()
)
rlInternInetStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteType.setStatus("current")


class _RlInternInetStaticRouteOwner_Type(Integer32):
    """Custom type rlInternInetStaticRouteOwner based on Integer32"""
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
        *(("default", 3),
          ("dhcp", 2),
          ("icmp", 4),
          ("static", 1))
    )


_RlInternInetStaticRouteOwner_Type.__name__ = "Integer32"
_RlInternInetStaticRouteOwner_Object = MibTableColumn
rlInternInetStaticRouteOwner = _RlInternInetStaticRouteOwner_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 9),
    _RlInternInetStaticRouteOwner_Type()
)
rlInternInetStaticRouteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteOwner.setStatus("current")
_RlInternInetStaticRouteRowStatus_Type = RowStatus
_RlInternInetStaticRouteRowStatus_Object = MibTableColumn
rlInternInetStaticRouteRowStatus = _RlInternInetStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 10),
    _RlInternInetStaticRouteRowStatus_Type()
)
rlInternInetStaticRouteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteRowStatus.setStatus("current")


class _RlInternInetStaticRouteForwardingStatus_Type(Integer32):
    """Custom type rlInternInetStaticRouteForwardingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RlInternInetStaticRouteForwardingStatus_Type.__name__ = "Integer32"
_RlInternInetStaticRouteForwardingStatus_Object = MibTableColumn
rlInternInetStaticRouteForwardingStatus = _RlInternInetStaticRouteForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 26, 31, 1, 11),
    _RlInternInetStaticRouteForwardingStatus_Type()
)
rlInternInetStaticRouteForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlInternInetStaticRouteForwardingStatus.setStatus("current")


class _Rlipv6IcmpErrorRatelimitInterval_Type(TimeInterval):
    """Custom type rlipv6IcmpErrorRatelimitInterval based on TimeInterval"""
    defaultValue = 100


_Rlipv6IcmpErrorRatelimitInterval_Object = MibScalar
rlipv6IcmpErrorRatelimitInterval = _Rlipv6IcmpErrorRatelimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 1),
    _Rlipv6IcmpErrorRatelimitInterval_Type()
)
rlipv6IcmpErrorRatelimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6IcmpErrorRatelimitInterval.setStatus("current")


class _Rlipv6IcmpErrorRatelimitBucketSize_Type(Integer32):
    """Custom type rlipv6IcmpErrorRatelimitBucketSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_Rlipv6IcmpErrorRatelimitBucketSize_Type.__name__ = "Integer32"
_Rlipv6IcmpErrorRatelimitBucketSize_Object = MibScalar
rlipv6IcmpErrorRatelimitBucketSize = _Rlipv6IcmpErrorRatelimitBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 2),
    _Rlipv6IcmpErrorRatelimitBucketSize_Type()
)
rlipv6IcmpErrorRatelimitBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6IcmpErrorRatelimitBucketSize.setStatus("current")


class _Rlipv6LLDefaultZone_Type(InterfaceIndexOrZero):
    """Custom type rlipv6LLDefaultZone based on InterfaceIndexOrZero"""
    defaultValue = 0


_Rlipv6LLDefaultZone_Object = MibScalar
rlipv6LLDefaultZone = _Rlipv6LLDefaultZone_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 3),
    _Rlipv6LLDefaultZone_Type()
)
rlipv6LLDefaultZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6LLDefaultZone.setStatus("current")
_RlIpv6GeneralPrefixTable_Object = MibTable
rlIpv6GeneralPrefixTable = _RlIpv6GeneralPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4)
)
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixTable.setStatus("current")
_RlIpv6GeneralPrefixEntry_Object = MibTableRow
rlIpv6GeneralPrefixEntry = _RlIpv6GeneralPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1)
)
rlIpv6GeneralPrefixEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpv6GeneralPrefixName"),
)
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixEntry.setStatus("current")
_RlIpv6GeneralPrefixName_Type = DisplayString
_RlIpv6GeneralPrefixName_Object = MibTableColumn
rlIpv6GeneralPrefixName = _RlIpv6GeneralPrefixName_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 1),
    _RlIpv6GeneralPrefixName_Type()
)
rlIpv6GeneralPrefixName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixName.setStatus("current")
_RlIpv6GeneralPrefixInetAddrType_Type = InetAddressType
_RlIpv6GeneralPrefixInetAddrType_Object = MibTableColumn
rlIpv6GeneralPrefixInetAddrType = _RlIpv6GeneralPrefixInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 2),
    _RlIpv6GeneralPrefixInetAddrType_Type()
)
rlIpv6GeneralPrefixInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixInetAddrType.setStatus("current")
_RlIpv6GeneralPrefixInetAddr_Type = InetAddress
_RlIpv6GeneralPrefixInetAddr_Object = MibTableColumn
rlIpv6GeneralPrefixInetAddr = _RlIpv6GeneralPrefixInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 3),
    _RlIpv6GeneralPrefixInetAddr_Type()
)
rlIpv6GeneralPrefixInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixInetAddr.setStatus("current")
_RlIpv6GeneralPrefixInetAddrPrefixLength_Type = InetAddressPrefixLength
_RlIpv6GeneralPrefixInetAddrPrefixLength_Object = MibTableColumn
rlIpv6GeneralPrefixInetAddrPrefixLength = _RlIpv6GeneralPrefixInetAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 4),
    _RlIpv6GeneralPrefixInetAddrPrefixLength_Type()
)
rlIpv6GeneralPrefixInetAddrPrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixInetAddrPrefixLength.setStatus("current")
_RlIpv6GeneralPrefixInterfaceId_Type = Unsigned32
_RlIpv6GeneralPrefixInterfaceId_Object = MibTableColumn
rlIpv6GeneralPrefixInterfaceId = _RlIpv6GeneralPrefixInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 5),
    _RlIpv6GeneralPrefixInterfaceId_Type()
)
rlIpv6GeneralPrefixInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixInterfaceId.setStatus("current")
_RlIpv6GeneralPrefixRowStatus_Type = RowStatus
_RlIpv6GeneralPrefixRowStatus_Object = MibTableColumn
rlIpv6GeneralPrefixRowStatus = _RlIpv6GeneralPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 4, 1, 6),
    _RlIpv6GeneralPrefixRowStatus_Type()
)
rlIpv6GeneralPrefixRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6GeneralPrefixRowStatus.setStatus("current")


class _Rlipv6MaximumHopsNumber_Type(Integer32):
    """Custom type rlipv6MaximumHopsNumber based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Rlipv6MaximumHopsNumber_Type.__name__ = "Integer32"
_Rlipv6MaximumHopsNumber_Object = MibScalar
rlipv6MaximumHopsNumber = _Rlipv6MaximumHopsNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 5),
    _Rlipv6MaximumHopsNumber_Type()
)
rlipv6MaximumHopsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6MaximumHopsNumber.setStatus("current")
_RlIpv6RouterAdvertPrefixTable_Object = MibTable
rlIpv6RouterAdvertPrefixTable = _RlIpv6RouterAdvertPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6)
)
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixTable.setStatus("current")
_RlIpv6RouterAdvertPrefixEntry_Object = MibTableRow
rlIpv6RouterAdvertPrefixEntry = _RlIpv6RouterAdvertPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1)
)
rlIpv6RouterAdvertPrefixEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpv6RouterAdvertPrefixIfIndex"),
    (0, "RADLAN-IPv6", "rlIpv6RouterAdvertPrefixIsDefault"),
    (0, "RADLAN-IPv6", "rlIpv6RouterAdvertPrefixInetAddrType"),
    (0, "RADLAN-IPv6", "rlIpv6RouterAdvertPrefixInetAddr"),
    (0, "RADLAN-IPv6", "rlIpv6RouterAdvertPrefixInetAddrPrefixLength"),
)
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixEntry.setStatus("current")
_RlIpv6RouterAdvertPrefixIfIndex_Type = InterfaceIndex
_RlIpv6RouterAdvertPrefixIfIndex_Object = MibTableColumn
rlIpv6RouterAdvertPrefixIfIndex = _RlIpv6RouterAdvertPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 1),
    _RlIpv6RouterAdvertPrefixIfIndex_Type()
)
rlIpv6RouterAdvertPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixIfIndex.setStatus("current")
_RlIpv6RouterAdvertPrefixIsDefault_Type = TruthValue
_RlIpv6RouterAdvertPrefixIsDefault_Object = MibTableColumn
rlIpv6RouterAdvertPrefixIsDefault = _RlIpv6RouterAdvertPrefixIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 2),
    _RlIpv6RouterAdvertPrefixIsDefault_Type()
)
rlIpv6RouterAdvertPrefixIsDefault.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixIsDefault.setStatus("current")
_RlIpv6RouterAdvertPrefixInetAddrType_Type = InetAddressType
_RlIpv6RouterAdvertPrefixInetAddrType_Object = MibTableColumn
rlIpv6RouterAdvertPrefixInetAddrType = _RlIpv6RouterAdvertPrefixInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 3),
    _RlIpv6RouterAdvertPrefixInetAddrType_Type()
)
rlIpv6RouterAdvertPrefixInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixInetAddrType.setStatus("current")
_RlIpv6RouterAdvertPrefixInetAddr_Type = InetAddress
_RlIpv6RouterAdvertPrefixInetAddr_Object = MibTableColumn
rlIpv6RouterAdvertPrefixInetAddr = _RlIpv6RouterAdvertPrefixInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 4),
    _RlIpv6RouterAdvertPrefixInetAddr_Type()
)
rlIpv6RouterAdvertPrefixInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixInetAddr.setStatus("current")
_RlIpv6RouterAdvertPrefixInetAddrPrefixLength_Type = InetAddressPrefixLength
_RlIpv6RouterAdvertPrefixInetAddrPrefixLength_Object = MibTableColumn
rlIpv6RouterAdvertPrefixInetAddrPrefixLength = _RlIpv6RouterAdvertPrefixInetAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 5),
    _RlIpv6RouterAdvertPrefixInetAddrPrefixLength_Type()
)
rlIpv6RouterAdvertPrefixInetAddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixInetAddrPrefixLength.setStatus("current")


class _RlIpv6RouterAdvertPrefixAdminStatus_Type(Integer32):
    """Custom type rlIpv6RouterAdvertPrefixAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_RlIpv6RouterAdvertPrefixAdminStatus_Type.__name__ = "Integer32"
_RlIpv6RouterAdvertPrefixAdminStatus_Object = MibTableColumn
rlIpv6RouterAdvertPrefixAdminStatus = _RlIpv6RouterAdvertPrefixAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 6),
    _RlIpv6RouterAdvertPrefixAdminStatus_Type()
)
rlIpv6RouterAdvertPrefixAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdminStatus.setStatus("current")


class _RlIpv6RouterAdvertPrefixAdvertise_Type(TruthValue):
    """Custom type rlIpv6RouterAdvertPrefixAdvertise based on TruthValue"""


_RlIpv6RouterAdvertPrefixAdvertise_Object = MibTableColumn
rlIpv6RouterAdvertPrefixAdvertise = _RlIpv6RouterAdvertPrefixAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 7),
    _RlIpv6RouterAdvertPrefixAdvertise_Type()
)
rlIpv6RouterAdvertPrefixAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdvertise.setStatus("current")


class _RlIpv6RouterAdvertPrefixOnLinkStatus_Type(Integer32):
    """Custom type rlIpv6RouterAdvertPrefixOnLinkStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-onlink", 2),
          ("off-link", 3),
          ("onlink", 1))
    )


_RlIpv6RouterAdvertPrefixOnLinkStatus_Type.__name__ = "Integer32"
_RlIpv6RouterAdvertPrefixOnLinkStatus_Object = MibTableColumn
rlIpv6RouterAdvertPrefixOnLinkStatus = _RlIpv6RouterAdvertPrefixOnLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 8),
    _RlIpv6RouterAdvertPrefixOnLinkStatus_Type()
)
rlIpv6RouterAdvertPrefixOnLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixOnLinkStatus.setStatus("current")


class _RlIpv6RouterAdvertPrefixAutonomousFlag_Type(TruthValue):
    """Custom type rlIpv6RouterAdvertPrefixAutonomousFlag based on TruthValue"""


_RlIpv6RouterAdvertPrefixAutonomousFlag_Object = MibTableColumn
rlIpv6RouterAdvertPrefixAutonomousFlag = _RlIpv6RouterAdvertPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 9),
    _RlIpv6RouterAdvertPrefixAutonomousFlag_Type()
)
rlIpv6RouterAdvertPrefixAutonomousFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAutonomousFlag.setStatus("current")


class _RlIpv6RouterAdvertPrefixAdvPreferredLifetime_Type(Unsigned32):
    """Custom type rlIpv6RouterAdvertPrefixAdvPreferredLifetime based on Unsigned32"""
    defaultValue = 604800


_RlIpv6RouterAdvertPrefixAdvPreferredLifetime_Object = MibTableColumn
rlIpv6RouterAdvertPrefixAdvPreferredLifetime = _RlIpv6RouterAdvertPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 10),
    _RlIpv6RouterAdvertPrefixAdvPreferredLifetime_Type()
)
rlIpv6RouterAdvertPrefixAdvPreferredLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdvPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdvPreferredLifetime.setUnits("seconds")


class _RlIpv6RouterAdvertPrefixAdvValidLifetime_Type(Unsigned32):
    """Custom type rlIpv6RouterAdvertPrefixAdvValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_RlIpv6RouterAdvertPrefixAdvValidLifetime_Object = MibTableColumn
rlIpv6RouterAdvertPrefixAdvValidLifetime = _RlIpv6RouterAdvertPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 11),
    _RlIpv6RouterAdvertPrefixAdvValidLifetime_Type()
)
rlIpv6RouterAdvertPrefixAdvValidLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdvValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixAdvValidLifetime.setUnits("seconds")
_RlIpv6RouterAdvertPrefixRowStatus_Type = RowStatus
_RlIpv6RouterAdvertPrefixRowStatus_Object = MibTableColumn
rlIpv6RouterAdvertPrefixRowStatus = _RlIpv6RouterAdvertPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 6, 1, 12),
    _RlIpv6RouterAdvertPrefixRowStatus_Type()
)
rlIpv6RouterAdvertPrefixRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertPrefixRowStatus.setStatus("current")
_RlIpv6RouterAdvertTable_Object = MibTable
rlIpv6RouterAdvertTable = _RlIpv6RouterAdvertTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 7)
)
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertTable.setStatus("current")
_RlIpv6RouterAdvertEntry_Object = MibTableRow
rlIpv6RouterAdvertEntry = _RlIpv6RouterAdvertEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 7, 1)
)
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertEntry.setStatus("current")


class _RlIpv6RouterAdvertAdvIntervalOption_Type(TruthValue):
    """Custom type rlIpv6RouterAdvertAdvIntervalOption based on TruthValue"""


_RlIpv6RouterAdvertAdvIntervalOption_Object = MibTableColumn
rlIpv6RouterAdvertAdvIntervalOption = _RlIpv6RouterAdvertAdvIntervalOption_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 7, 1, 1),
    _RlIpv6RouterAdvertAdvIntervalOption_Type()
)
rlIpv6RouterAdvertAdvIntervalOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertAdvIntervalOption.setStatus("current")


class _RlIpv6RouterAdvertRouterPreference_Type(Integer32):
    """Custom type rlIpv6RouterAdvertRouterPreference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_RlIpv6RouterAdvertRouterPreference_Type.__name__ = "Integer32"
_RlIpv6RouterAdvertRouterPreference_Object = MibTableColumn
rlIpv6RouterAdvertRouterPreference = _RlIpv6RouterAdvertRouterPreference_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 7, 1, 2),
    _RlIpv6RouterAdvertRouterPreference_Type()
)
rlIpv6RouterAdvertRouterPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertRouterPreference.setStatus("current")


class _RlIpv6RouterAdvertIsCurHopLimitUserConfigured_Type(TruthValue):
    """Custom type rlIpv6RouterAdvertIsCurHopLimitUserConfigured based on TruthValue"""


_RlIpv6RouterAdvertIsCurHopLimitUserConfigured_Object = MibTableColumn
rlIpv6RouterAdvertIsCurHopLimitUserConfigured = _RlIpv6RouterAdvertIsCurHopLimitUserConfigured_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 7, 1, 3),
    _RlIpv6RouterAdvertIsCurHopLimitUserConfigured_Type()
)
rlIpv6RouterAdvertIsCurHopLimitUserConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6RouterAdvertIsCurHopLimitUserConfigured.setStatus("current")
_Rlipv6InetCidrTableClear_Type = Integer32
_Rlipv6InetCidrTableClear_Object = MibScalar
rlipv6InetCidrTableClear = _Rlipv6InetCidrTableClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 8),
    _Rlipv6InetCidrTableClear_Type()
)
rlipv6InetCidrTableClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6InetCidrTableClear.setStatus("current")
_RlIpv6PathMtuTable_Object = MibTable
rlIpv6PathMtuTable = _RlIpv6PathMtuTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9)
)
if mibBuilder.loadTexts:
    rlIpv6PathMtuTable.setStatus("current")
_RlIpv6PathMtuEntry_Object = MibTableRow
rlIpv6PathMtuEntry = _RlIpv6PathMtuEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9, 1)
)
rlIpv6PathMtuEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpv6PathMtuEntryInetDestAddrType"),
    (0, "RADLAN-IPv6", "rlIpv6PathMtuEntryInetDestAddr"),
)
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntry.setStatus("current")
_RlIpv6PathMtuEntryInetDestAddrType_Type = InetAddressType
_RlIpv6PathMtuEntryInetDestAddrType_Object = MibTableColumn
rlIpv6PathMtuEntryInetDestAddrType = _RlIpv6PathMtuEntryInetDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9, 1, 1),
    _RlIpv6PathMtuEntryInetDestAddrType_Type()
)
rlIpv6PathMtuEntryInetDestAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntryInetDestAddrType.setStatus("current")
_RlIpv6PathMtuEntryInetDestAddr_Type = InetAddress
_RlIpv6PathMtuEntryInetDestAddr_Object = MibTableColumn
rlIpv6PathMtuEntryInetDestAddr = _RlIpv6PathMtuEntryInetDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9, 1, 2),
    _RlIpv6PathMtuEntryInetDestAddr_Type()
)
rlIpv6PathMtuEntryInetDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntryInetDestAddr.setStatus("current")
_RlIpv6PathMtuEntryMtu_Type = Unsigned32
_RlIpv6PathMtuEntryMtu_Object = MibTableColumn
rlIpv6PathMtuEntryMtu = _RlIpv6PathMtuEntryMtu_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9, 1, 3),
    _RlIpv6PathMtuEntryMtu_Type()
)
rlIpv6PathMtuEntryMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntryMtu.setStatus("current")
_RlIpv6PathMtuEntryAge_Type = Unsigned32
_RlIpv6PathMtuEntryAge_Object = MibTableColumn
rlIpv6PathMtuEntryAge = _RlIpv6PathMtuEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 9, 1, 4),
    _RlIpv6PathMtuEntryAge_Type()
)
rlIpv6PathMtuEntryAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntryAge.setStatus("current")
if mibBuilder.loadTexts:
    rlIpv6PathMtuEntryAge.setUnits("seconds")
_RlIpNetToPhysicalTableClearTable_Object = MibTable
rlIpNetToPhysicalTableClearTable = _RlIpNetToPhysicalTableClearTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 10)
)
if mibBuilder.loadTexts:
    rlIpNetToPhysicalTableClearTable.setStatus("current")
_RlIpNetToPhysicalTableClearEntry_Object = MibTableRow
rlIpNetToPhysicalTableClearEntry = _RlIpNetToPhysicalTableClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 10, 1)
)
rlIpNetToPhysicalTableClearEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpNetToPhysicalTableClearIfIndex"),
)
if mibBuilder.loadTexts:
    rlIpNetToPhysicalTableClearEntry.setStatus("current")
_RlIpNetToPhysicalTableClearIfIndex_Type = InterfaceIndexOrZero
_RlIpNetToPhysicalTableClearIfIndex_Object = MibTableColumn
rlIpNetToPhysicalTableClearIfIndex = _RlIpNetToPhysicalTableClearIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 10, 1, 1),
    _RlIpNetToPhysicalTableClearIfIndex_Type()
)
rlIpNetToPhysicalTableClearIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpNetToPhysicalTableClearIfIndex.setStatus("current")


class _RlIpNetToPhysicalTableClearScope_Type(Integer32):
    """Custom type rlIpNetToPhysicalTableClearScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("dynamicOnly", 2),
          ("staticOnly", 3))
    )


_RlIpNetToPhysicalTableClearScope_Type.__name__ = "Integer32"
_RlIpNetToPhysicalTableClearScope_Object = MibTableColumn
rlIpNetToPhysicalTableClearScope = _RlIpNetToPhysicalTableClearScope_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 10, 1, 2),
    _RlIpNetToPhysicalTableClearScope_Type()
)
rlIpNetToPhysicalTableClearScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpNetToPhysicalTableClearScope.setStatus("current")
_RlIpv6HostForwardingTable_Object = MibTable
rlIpv6HostForwardingTable = _RlIpv6HostForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11)
)
if mibBuilder.loadTexts:
    rlIpv6HostForwardingTable.setStatus("current")
_RlIpv6HostForwardingEntry_Object = MibTableRow
rlIpv6HostForwardingEntry = _RlIpv6HostForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1)
)
rlIpv6HostForwardingEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingDestType"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingDest"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingPfxLen"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingNextHopType"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingNextHop"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingIfIndex"),
    (0, "RADLAN-IPv6", "rlIpv6HostForwardingType"),
)
if mibBuilder.loadTexts:
    rlIpv6HostForwardingEntry.setStatus("current")
_RlIpv6HostForwardingDestType_Type = InetAddressType
_RlIpv6HostForwardingDestType_Object = MibTableColumn
rlIpv6HostForwardingDestType = _RlIpv6HostForwardingDestType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 1),
    _RlIpv6HostForwardingDestType_Type()
)
rlIpv6HostForwardingDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingDestType.setStatus("current")
_RlIpv6HostForwardingDest_Type = InetAddress
_RlIpv6HostForwardingDest_Object = MibTableColumn
rlIpv6HostForwardingDest = _RlIpv6HostForwardingDest_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 2),
    _RlIpv6HostForwardingDest_Type()
)
rlIpv6HostForwardingDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingDest.setStatus("current")
_RlIpv6HostForwardingPfxLen_Type = InetAddressPrefixLength
_RlIpv6HostForwardingPfxLen_Object = MibTableColumn
rlIpv6HostForwardingPfxLen = _RlIpv6HostForwardingPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 3),
    _RlIpv6HostForwardingPfxLen_Type()
)
rlIpv6HostForwardingPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingPfxLen.setStatus("current")
_RlIpv6HostForwardingNextHopType_Type = InetAddressType
_RlIpv6HostForwardingNextHopType_Object = MibTableColumn
rlIpv6HostForwardingNextHopType = _RlIpv6HostForwardingNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 4),
    _RlIpv6HostForwardingNextHopType_Type()
)
rlIpv6HostForwardingNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingNextHopType.setStatus("current")
_RlIpv6HostForwardingNextHop_Type = InetAddress
_RlIpv6HostForwardingNextHop_Object = MibTableColumn
rlIpv6HostForwardingNextHop = _RlIpv6HostForwardingNextHop_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 5),
    _RlIpv6HostForwardingNextHop_Type()
)
rlIpv6HostForwardingNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingNextHop.setStatus("current")


class _RlIpv6HostForwardingIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rlIpv6HostForwardingIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlIpv6HostForwardingIfIndex_Object = MibTableColumn
rlIpv6HostForwardingIfIndex = _RlIpv6HostForwardingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 6),
    _RlIpv6HostForwardingIfIndex_Type()
)
rlIpv6HostForwardingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingIfIndex.setStatus("current")


class _RlIpv6HostForwardingType_Type(Integer32):
    """Custom type rlIpv6HostForwardingType based on Integer32"""
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
        *(("local", 2),
          ("nd", 3),
          ("redirect", 1),
          ("remote-dynamic", 5),
          ("remote-static", 4))
    )


_RlIpv6HostForwardingType_Type.__name__ = "Integer32"
_RlIpv6HostForwardingType_Object = MibTableColumn
rlIpv6HostForwardingType = _RlIpv6HostForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 7),
    _RlIpv6HostForwardingType_Type()
)
rlIpv6HostForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingType.setStatus("current")
_RlIpv6HostForwardingPathCost_Type = Unsigned32
_RlIpv6HostForwardingPathCost_Object = MibTableColumn
rlIpv6HostForwardingPathCost = _RlIpv6HostForwardingPathCost_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 11, 1, 8),
    _RlIpv6HostForwardingPathCost_Type()
)
rlIpv6HostForwardingPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpv6HostForwardingPathCost.setStatus("current")


class _Rlipv6EnabledByDefaultRemovedIfindex_Type(Integer32):
    """Custom type rlipv6EnabledByDefaultRemovedIfindex based on Integer32"""
    defaultValue = 0


_Rlipv6EnabledByDefaultRemovedIfindex_Object = MibScalar
rlipv6EnabledByDefaultRemovedIfindex = _Rlipv6EnabledByDefaultRemovedIfindex_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 12),
    _Rlipv6EnabledByDefaultRemovedIfindex_Type()
)
rlipv6EnabledByDefaultRemovedIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlipv6EnabledByDefaultRemovedIfindex.setStatus("current")
_RlManagementIpv6_Type = InetAddress
_RlManagementIpv6_Object = MibScalar
rlManagementIpv6 = _RlManagementIpv6_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 13),
    _RlManagementIpv6_Type()
)
rlManagementIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlManagementIpv6.setStatus("current")


class _RlManagementIpv6Action_Type(Integer32):
    """Custom type rlManagementIpv6Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_RlManagementIpv6Action_Type.__name__ = "Integer32"
_RlManagementIpv6Action_Object = MibScalar
rlManagementIpv6Action = _RlManagementIpv6Action_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 14),
    _RlManagementIpv6Action_Type()
)
rlManagementIpv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlManagementIpv6Action.setStatus("current")
_RlIpv6TunnelToIPv6DbTable_Object = MibTable
rlIpv6TunnelToIPv6DbTable = _RlIpv6TunnelToIPv6DbTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15)
)
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6DbTable.setStatus("current")
_RlIpv6TunnelToIPv6DbEntry_Object = MibTableRow
rlIpv6TunnelToIPv6DbEntry = _RlIpv6TunnelToIPv6DbEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1)
)
rlIpv6TunnelToIPv6DbEntry.setIndexNames(
    (0, "RADLAN-IPv6", "rlIpv6TunnelToIPv6IfIndex"),
)
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6DbEntry.setStatus("current")
_RlIpv6TunnelToIPv6IfIndex_Type = InterfaceIndex
_RlIpv6TunnelToIPv6IfIndex_Object = MibTableColumn
rlIpv6TunnelToIPv6IfIndex = _RlIpv6TunnelToIPv6IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 1),
    _RlIpv6TunnelToIPv6IfIndex_Type()
)
rlIpv6TunnelToIPv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6IfIndex.setStatus("current")


class _RlIpv6TunnelToIPv6Action_Type(Integer32):
    """Custom type rlIpv6TunnelToIPv6Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("addAddress", 3),
          ("createTunnel", 1),
          ("deleteAddress", 4),
          ("destroyTunnel", 2),
          ("six2fourCfgClear", 7),
          ("six2fourCfgRestore", 6),
          ("updateAddresses", 5))
    )


_RlIpv6TunnelToIPv6Action_Type.__name__ = "Integer32"
_RlIpv6TunnelToIPv6Action_Object = MibTableColumn
rlIpv6TunnelToIPv6Action = _RlIpv6TunnelToIPv6Action_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 2),
    _RlIpv6TunnelToIPv6Action_Type()
)
rlIpv6TunnelToIPv6Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6Action.setStatus("current")
_RlIpv6TunnelToIPv6TunnelType_Type = IANAtunnelType
_RlIpv6TunnelToIPv6TunnelType_Object = MibTableColumn
rlIpv6TunnelToIPv6TunnelType = _RlIpv6TunnelToIPv6TunnelType_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 3),
    _RlIpv6TunnelToIPv6TunnelType_Type()
)
rlIpv6TunnelToIPv6TunnelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6TunnelType.setStatus("current")
_RlIpv6TunnelToIPv6Address_Type = InetAddress
_RlIpv6TunnelToIPv6Address_Object = MibTableColumn
rlIpv6TunnelToIPv6Address = _RlIpv6TunnelToIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 4),
    _RlIpv6TunnelToIPv6Address_Type()
)
rlIpv6TunnelToIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6Address.setStatus("current")
_RlIpv6TunnelToIPv6PrefixLength_Type = Unsigned32
_RlIpv6TunnelToIPv6PrefixLength_Object = MibTableColumn
rlIpv6TunnelToIPv6PrefixLength = _RlIpv6TunnelToIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 5),
    _RlIpv6TunnelToIPv6PrefixLength_Type()
)
rlIpv6TunnelToIPv6PrefixLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6PrefixLength.setStatus("current")
_RlIpv6TunnelToIPv6Mtu_Type = Unsigned32
_RlIpv6TunnelToIPv6Mtu_Object = MibTableColumn
rlIpv6TunnelToIPv6Mtu = _RlIpv6TunnelToIPv6Mtu_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 6),
    _RlIpv6TunnelToIPv6Mtu_Type()
)
rlIpv6TunnelToIPv6Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6Mtu.setStatus("current")
_RlIpv6TunnelToIPv6MinRtrSolicitationInterval_Type = Unsigned32
_RlIpv6TunnelToIPv6MinRtrSolicitationInterval_Object = MibTableColumn
rlIpv6TunnelToIPv6MinRtrSolicitationInterval = _RlIpv6TunnelToIPv6MinRtrSolicitationInterval_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 7),
    _RlIpv6TunnelToIPv6MinRtrSolicitationInterval_Type()
)
rlIpv6TunnelToIPv6MinRtrSolicitationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6MinRtrSolicitationInterval.setStatus("current")
_RlIpv6TunnelToIPv6LinkLayerIPv4_Type = IpAddress
_RlIpv6TunnelToIPv6LinkLayerIPv4_Object = MibTableColumn
rlIpv6TunnelToIPv6LinkLayerIPv4 = _RlIpv6TunnelToIPv6LinkLayerIPv4_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 15, 1, 8),
    _RlIpv6TunnelToIPv6LinkLayerIPv4_Type()
)
rlIpv6TunnelToIPv6LinkLayerIPv4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6TunnelToIPv6LinkLayerIPv4.setStatus("current")


class _RlIpv6DefaultTC_Type(Integer32):
    """Custom type rlIpv6DefaultTC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlIpv6DefaultTC_Type.__name__ = "Integer32"
_RlIpv6DefaultTC_Object = MibScalar
rlIpv6DefaultTC = _RlIpv6DefaultTC_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 16),
    _RlIpv6DefaultTC_Type()
)
rlIpv6DefaultTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6DefaultTC.setStatus("current")


class _RlIpv6DefaultUP_Type(Integer32):
    """Custom type rlIpv6DefaultUP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RlIpv6DefaultUP_Type.__name__ = "Integer32"
_RlIpv6DefaultUP_Object = MibScalar
rlIpv6DefaultUP = _RlIpv6DefaultUP_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 17),
    _RlIpv6DefaultUP_Type()
)
rlIpv6DefaultUP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6DefaultUP.setStatus("current")
_RlIpv6MtuSize_Type = Unsigned32
_RlIpv6MtuSize_Object = MibScalar
rlIpv6MtuSize = _RlIpv6MtuSize_Object(
    (1, 3, 6, 1, 4, 1, 89, 129, 18),
    _RlIpv6MtuSize_Type()
)
rlIpv6MtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpv6MtuSize.setStatus("current")
ipAddressEntry.registerAugmentions(
    ("RADLAN-IPv6",
     "rlIpAddressEntry")
)
rlIpAddressEntry.setIndexNames(*ipAddressEntry.getIndexNames())
ipv6InterfaceEntry.registerAugmentions(
    ("RADLAN-IPv6",
     "rlipv6InterfaceEntry")
)
rlipv6InterfaceEntry.setIndexNames(*ipv6InterfaceEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions(
    ("RADLAN-IPv6",
     "rlinetCidrRouteEntry")
)
rlinetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
ipNetToPhysicalEntry.registerAugmentions(
    ("RADLAN-IPv6",
     "rlipNetToPhysicalEntry")
)
rlipNetToPhysicalEntry.setIndexNames(*ipNetToPhysicalEntry.getIndexNames())
ipv6RouterAdvertEntry.registerAugmentions(
    ("RADLAN-IPv6",
     "rlIpv6RouterAdvertEntry")
)
rlIpv6RouterAdvertEntry.setIndexNames(*ipv6RouterAdvertEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-IPv6",
    **{"rlIpAddressTable": rlIpAddressTable,
       "rlIpAddressEntry": rlIpAddressEntry,
       "rlIpAddressPrefixLength": rlIpAddressPrefixLength,
       "rlIpAddressType": rlIpAddressType,
       "rlipv6InterfaceTable": rlipv6InterfaceTable,
       "rlipv6InterfaceEntry": rlipv6InterfaceEntry,
       "rlipv6InterfaceNdDadAttemps": rlipv6InterfaceNdDadAttemps,
       "rlipv6InterfaceAutoconfigEnable": rlipv6InterfaceAutoconfigEnable,
       "rlipv6InterfaceIcmpUnreachSendEnable": rlipv6InterfaceIcmpUnreachSendEnable,
       "rlipv6InterfaceLinkMTU": rlipv6InterfaceLinkMTU,
       "rlipv6InterfaceMLDVersion": rlipv6InterfaceMLDVersion,
       "rlipv6InterfaceRetransmitTime": rlipv6InterfaceRetransmitTime,
       "rlipv6InterfaceIcmpRedirectSendEnable": rlipv6InterfaceIcmpRedirectSendEnable,
       "rlinetCidrRouteTable": rlinetCidrRouteTable,
       "rlinetCidrRouteEntry": rlinetCidrRouteEntry,
       "rlinetCidrRouteLifetime": rlinetCidrRouteLifetime,
       "rlinetCidrRouteInfo": rlinetCidrRouteInfo,
       "rlipNetToPhysicalTable": rlipNetToPhysicalTable,
       "rlipNetToPhysicalEntry": rlipNetToPhysicalEntry,
       "rlipNetToPhysicalIsRouter": rlipNetToPhysicalIsRouter,
       "rlipNetToPhysicalReachableConfirmed": rlipNetToPhysicalReachableConfirmed,
       "rlInetStaticRouteTable": rlInetStaticRouteTable,
       "rlInetStaticRouteEntry": rlInetStaticRouteEntry,
       "rlInetStaticRouteDestType": rlInetStaticRouteDestType,
       "rlInetStaticRouteDest": rlInetStaticRouteDest,
       "rlInetStaticRoutePfxLen": rlInetStaticRoutePfxLen,
       "rlInetStaticRouteNextHopType": rlInetStaticRouteNextHopType,
       "rlInetStaticRouteNextHop": rlInetStaticRouteNextHop,
       "rlInetStaticRouteIfIndex": rlInetStaticRouteIfIndex,
       "rlInetStaticRoutePathCost": rlInetStaticRoutePathCost,
       "rlInetStaticRouteType": rlInetStaticRouteType,
       "rlInetStaticRouteOwner": rlInetStaticRouteOwner,
       "rlInetStaticRouteRowStatus": rlInetStaticRouteRowStatus,
       "rlInetStaticRouteForwardingStatus": rlInetStaticRouteForwardingStatus,
       "rlInetRoutingDistanceTable": rlInetRoutingDistanceTable,
       "rlInetRoutingDistanceEntry": rlInetRoutingDistanceEntry,
       "rlInetRoutingDistanceType": rlInetRoutingDistanceType,
       "rlInetRoutingDistanceConnected": rlInetRoutingDistanceConnected,
       "rlInetRoutingDistanceStatic": rlInetRoutingDistanceStatic,
       "rlInetRoutingDistanceRip": rlInetRoutingDistanceRip,
       "rlInetRoutingDistanceOspfInternal": rlInetRoutingDistanceOspfInternal,
       "rlInetRoutingDistanceOspfExternal": rlInetRoutingDistanceOspfExternal,
       "rlInternInetCidrRouteTable": rlInternInetCidrRouteTable,
       "rlInternInetCidrRouteEntry": rlInternInetCidrRouteEntry,
       "rlInternInetCidrRouteDestType": rlInternInetCidrRouteDestType,
       "rlInternInetCidrRouteDest": rlInternInetCidrRouteDest,
       "rlInternInetCidrRoutePfxLen": rlInternInetCidrRoutePfxLen,
       "rlInternInetCidrRoutePolicy": rlInternInetCidrRoutePolicy,
       "rlInternInetCidrRouteNextHopType": rlInternInetCidrRouteNextHopType,
       "rlInternInetCidrRouteNextHop": rlInternInetCidrRouteNextHop,
       "rlInternInetCidrRouteIfIndex": rlInternInetCidrRouteIfIndex,
       "rlInternInetCidrRouteType": rlInternInetCidrRouteType,
       "rlInternInetCidrRouteProto": rlInternInetCidrRouteProto,
       "rlInternInetCidrRouteAge": rlInternInetCidrRouteAge,
       "rlInternInetCidrRouteNextHopAS": rlInternInetCidrRouteNextHopAS,
       "rlInternInetCidrRouteMetric1": rlInternInetCidrRouteMetric1,
       "rlInternInetCidrRouteMetric2": rlInternInetCidrRouteMetric2,
       "rlInternInetCidrRouteMetric3": rlInternInetCidrRouteMetric3,
       "rlInternInetCidrRouteMetric4": rlInternInetCidrRouteMetric4,
       "rlInternInetCidrRouteMetric5": rlInternInetCidrRouteMetric5,
       "rlInternInetCidrRouteStatus": rlInternInetCidrRouteStatus,
       "rlInternInetCidrRouteLifetime": rlInternInetCidrRouteLifetime,
       "rlInternInetCidrRouteInfo": rlInternInetCidrRouteInfo,
       "rlInternInetStaticRouteTable": rlInternInetStaticRouteTable,
       "rlInternInetStaticRouteEntry": rlInternInetStaticRouteEntry,
       "rlInternInetStaticRouteDestType": rlInternInetStaticRouteDestType,
       "rlInternInetStaticRouteDest": rlInternInetStaticRouteDest,
       "rlInternInetStaticRoutePfxLen": rlInternInetStaticRoutePfxLen,
       "rlInternInetStaticRouteNextHopType": rlInternInetStaticRouteNextHopType,
       "rlInternInetStaticRouteNextHop": rlInternInetStaticRouteNextHop,
       "rlInternInetStaticRouteIfIndex": rlInternInetStaticRouteIfIndex,
       "rlInternInetStaticRoutePathCost": rlInternInetStaticRoutePathCost,
       "rlInternInetStaticRouteType": rlInternInetStaticRouteType,
       "rlInternInetStaticRouteOwner": rlInternInetStaticRouteOwner,
       "rlInternInetStaticRouteRowStatus": rlInternInetStaticRouteRowStatus,
       "rlInternInetStaticRouteForwardingStatus": rlInternInetStaticRouteForwardingStatus,
       "rlIPv6": rlIPv6,
       "rlipv6IcmpErrorRatelimitInterval": rlipv6IcmpErrorRatelimitInterval,
       "rlipv6IcmpErrorRatelimitBucketSize": rlipv6IcmpErrorRatelimitBucketSize,
       "rlipv6LLDefaultZone": rlipv6LLDefaultZone,
       "rlIpv6GeneralPrefixTable": rlIpv6GeneralPrefixTable,
       "rlIpv6GeneralPrefixEntry": rlIpv6GeneralPrefixEntry,
       "rlIpv6GeneralPrefixName": rlIpv6GeneralPrefixName,
       "rlIpv6GeneralPrefixInetAddrType": rlIpv6GeneralPrefixInetAddrType,
       "rlIpv6GeneralPrefixInetAddr": rlIpv6GeneralPrefixInetAddr,
       "rlIpv6GeneralPrefixInetAddrPrefixLength": rlIpv6GeneralPrefixInetAddrPrefixLength,
       "rlIpv6GeneralPrefixInterfaceId": rlIpv6GeneralPrefixInterfaceId,
       "rlIpv6GeneralPrefixRowStatus": rlIpv6GeneralPrefixRowStatus,
       "rlipv6MaximumHopsNumber": rlipv6MaximumHopsNumber,
       "rlIpv6RouterAdvertPrefixTable": rlIpv6RouterAdvertPrefixTable,
       "rlIpv6RouterAdvertPrefixEntry": rlIpv6RouterAdvertPrefixEntry,
       "rlIpv6RouterAdvertPrefixIfIndex": rlIpv6RouterAdvertPrefixIfIndex,
       "rlIpv6RouterAdvertPrefixIsDefault": rlIpv6RouterAdvertPrefixIsDefault,
       "rlIpv6RouterAdvertPrefixInetAddrType": rlIpv6RouterAdvertPrefixInetAddrType,
       "rlIpv6RouterAdvertPrefixInetAddr": rlIpv6RouterAdvertPrefixInetAddr,
       "rlIpv6RouterAdvertPrefixInetAddrPrefixLength": rlIpv6RouterAdvertPrefixInetAddrPrefixLength,
       "rlIpv6RouterAdvertPrefixAdminStatus": rlIpv6RouterAdvertPrefixAdminStatus,
       "rlIpv6RouterAdvertPrefixAdvertise": rlIpv6RouterAdvertPrefixAdvertise,
       "rlIpv6RouterAdvertPrefixOnLinkStatus": rlIpv6RouterAdvertPrefixOnLinkStatus,
       "rlIpv6RouterAdvertPrefixAutonomousFlag": rlIpv6RouterAdvertPrefixAutonomousFlag,
       "rlIpv6RouterAdvertPrefixAdvPreferredLifetime": rlIpv6RouterAdvertPrefixAdvPreferredLifetime,
       "rlIpv6RouterAdvertPrefixAdvValidLifetime": rlIpv6RouterAdvertPrefixAdvValidLifetime,
       "rlIpv6RouterAdvertPrefixRowStatus": rlIpv6RouterAdvertPrefixRowStatus,
       "rlIpv6RouterAdvertTable": rlIpv6RouterAdvertTable,
       "rlIpv6RouterAdvertEntry": rlIpv6RouterAdvertEntry,
       "rlIpv6RouterAdvertAdvIntervalOption": rlIpv6RouterAdvertAdvIntervalOption,
       "rlIpv6RouterAdvertRouterPreference": rlIpv6RouterAdvertRouterPreference,
       "rlIpv6RouterAdvertIsCurHopLimitUserConfigured": rlIpv6RouterAdvertIsCurHopLimitUserConfigured,
       "rlipv6InetCidrTableClear": rlipv6InetCidrTableClear,
       "rlIpv6PathMtuTable": rlIpv6PathMtuTable,
       "rlIpv6PathMtuEntry": rlIpv6PathMtuEntry,
       "rlIpv6PathMtuEntryInetDestAddrType": rlIpv6PathMtuEntryInetDestAddrType,
       "rlIpv6PathMtuEntryInetDestAddr": rlIpv6PathMtuEntryInetDestAddr,
       "rlIpv6PathMtuEntryMtu": rlIpv6PathMtuEntryMtu,
       "rlIpv6PathMtuEntryAge": rlIpv6PathMtuEntryAge,
       "rlIpNetToPhysicalTableClearTable": rlIpNetToPhysicalTableClearTable,
       "rlIpNetToPhysicalTableClearEntry": rlIpNetToPhysicalTableClearEntry,
       "rlIpNetToPhysicalTableClearIfIndex": rlIpNetToPhysicalTableClearIfIndex,
       "rlIpNetToPhysicalTableClearScope": rlIpNetToPhysicalTableClearScope,
       "rlIpv6HostForwardingTable": rlIpv6HostForwardingTable,
       "rlIpv6HostForwardingEntry": rlIpv6HostForwardingEntry,
       "rlIpv6HostForwardingDestType": rlIpv6HostForwardingDestType,
       "rlIpv6HostForwardingDest": rlIpv6HostForwardingDest,
       "rlIpv6HostForwardingPfxLen": rlIpv6HostForwardingPfxLen,
       "rlIpv6HostForwardingNextHopType": rlIpv6HostForwardingNextHopType,
       "rlIpv6HostForwardingNextHop": rlIpv6HostForwardingNextHop,
       "rlIpv6HostForwardingIfIndex": rlIpv6HostForwardingIfIndex,
       "rlIpv6HostForwardingType": rlIpv6HostForwardingType,
       "rlIpv6HostForwardingPathCost": rlIpv6HostForwardingPathCost,
       "rlipv6EnabledByDefaultRemovedIfindex": rlipv6EnabledByDefaultRemovedIfindex,
       "rlManagementIpv6": rlManagementIpv6,
       "rlManagementIpv6Action": rlManagementIpv6Action,
       "rlIpv6TunnelToIPv6DbTable": rlIpv6TunnelToIPv6DbTable,
       "rlIpv6TunnelToIPv6DbEntry": rlIpv6TunnelToIPv6DbEntry,
       "rlIpv6TunnelToIPv6IfIndex": rlIpv6TunnelToIPv6IfIndex,
       "rlIpv6TunnelToIPv6Action": rlIpv6TunnelToIPv6Action,
       "rlIpv6TunnelToIPv6TunnelType": rlIpv6TunnelToIPv6TunnelType,
       "rlIpv6TunnelToIPv6Address": rlIpv6TunnelToIPv6Address,
       "rlIpv6TunnelToIPv6PrefixLength": rlIpv6TunnelToIPv6PrefixLength,
       "rlIpv6TunnelToIPv6Mtu": rlIpv6TunnelToIPv6Mtu,
       "rlIpv6TunnelToIPv6MinRtrSolicitationInterval": rlIpv6TunnelToIPv6MinRtrSolicitationInterval,
       "rlIpv6TunnelToIPv6LinkLayerIPv4": rlIpv6TunnelToIPv6LinkLayerIPv4,
       "rlIpv6DefaultTC": rlIpv6DefaultTC,
       "rlIpv6DefaultUP": rlIpv6DefaultUP,
       "rlIpv6MtuSize": rlIpv6MtuSize}
)
