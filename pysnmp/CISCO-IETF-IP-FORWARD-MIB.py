# SNMP MIB module (CISCO-IETF-IP-FORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-IP-FORWARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:34 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetAutonomousSystemNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetAutonomousSystemNumber")

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

ciscoIetfIpForward = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 85)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CIpForwardNumber_Type = Gauge32
_CIpForwardNumber_Object = MibScalar
cIpForwardNumber = _CIpForwardNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 1),
    _CIpForwardNumber_Type()
)
cIpForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardNumber.setStatus("obsolete")
_CIpForwardTable_Object = MibTable
cIpForwardTable = _CIpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2)
)
if mibBuilder.loadTexts:
    cIpForwardTable.setStatus("obsolete")
_CIpForwardEntry_Object = MibTableRow
cIpForwardEntry = _CIpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1)
)
cIpForwardEntry.setIndexNames(
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpForwardDest"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpForwardProto"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpForwardPolicy"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpForwardNextHop"),
)
if mibBuilder.loadTexts:
    cIpForwardEntry.setStatus("obsolete")
_CIpForwardDest_Type = IpAddress
_CIpForwardDest_Object = MibTableColumn
cIpForwardDest = _CIpForwardDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 1),
    _CIpForwardDest_Type()
)
cIpForwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardDest.setStatus("obsolete")


class _CIpForwardMask_Type(IpAddress):
    """Custom type cIpForwardMask based on IpAddress"""
    defaultHexValue = "00000000"


_CIpForwardMask_Object = MibTableColumn
cIpForwardMask = _CIpForwardMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 2),
    _CIpForwardMask_Type()
)
cIpForwardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMask.setStatus("obsolete")


class _CIpForwardPolicy_Type(Integer32):
    """Custom type cIpForwardPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpForwardPolicy_Type.__name__ = "Integer32"
_CIpForwardPolicy_Object = MibTableColumn
cIpForwardPolicy = _CIpForwardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 3),
    _CIpForwardPolicy_Type()
)
cIpForwardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardPolicy.setStatus("obsolete")
_CIpForwardNextHop_Type = IpAddress
_CIpForwardNextHop_Object = MibTableColumn
cIpForwardNextHop = _CIpForwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 4),
    _CIpForwardNextHop_Type()
)
cIpForwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardNextHop.setStatus("obsolete")


class _CIpForwardIfIndex_Type(Integer32):
    """Custom type cIpForwardIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpForwardIfIndex_Type.__name__ = "Integer32"
_CIpForwardIfIndex_Object = MibTableColumn
cIpForwardIfIndex = _CIpForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 5),
    _CIpForwardIfIndex_Type()
)
cIpForwardIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardIfIndex.setStatus("obsolete")


class _CIpForwardType_Type(Integer32):
    """Custom type cIpForwardType based on Integer32"""
    defaultValue = 2

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
        *(("invalid", 2),
          ("local", 3),
          ("other", 1),
          ("remote", 4))
    )


_CIpForwardType_Type.__name__ = "Integer32"
_CIpForwardType_Object = MibTableColumn
cIpForwardType = _CIpForwardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 6),
    _CIpForwardType_Type()
)
cIpForwardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardType.setStatus("obsolete")


class _CIpForwardProto_Type(Integer32):
    """Custom type cIpForwardProto based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_CIpForwardProto_Type.__name__ = "Integer32"
_CIpForwardProto_Object = MibTableColumn
cIpForwardProto = _CIpForwardProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 7),
    _CIpForwardProto_Type()
)
cIpForwardProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardProto.setStatus("obsolete")


class _CIpForwardAge_Type(Integer32):
    """Custom type cIpForwardAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpForwardAge_Type.__name__ = "Integer32"
_CIpForwardAge_Object = MibTableColumn
cIpForwardAge = _CIpForwardAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 8),
    _CIpForwardAge_Type()
)
cIpForwardAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpForwardAge.setStatus("obsolete")
_CIpForwardInfo_Type = ObjectIdentifier
_CIpForwardInfo_Object = MibTableColumn
cIpForwardInfo = _CIpForwardInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 9),
    _CIpForwardInfo_Type()
)
cIpForwardInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardInfo.setStatus("obsolete")


class _CIpForwardNextHopAS_Type(Integer32):
    """Custom type cIpForwardNextHopAS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpForwardNextHopAS_Type.__name__ = "Integer32"
_CIpForwardNextHopAS_Object = MibTableColumn
cIpForwardNextHopAS = _CIpForwardNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 10),
    _CIpForwardNextHopAS_Type()
)
cIpForwardNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardNextHopAS.setStatus("obsolete")


class _CIpForwardMetric1_Type(Integer32):
    """Custom type cIpForwardMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpForwardMetric1_Type.__name__ = "Integer32"
_CIpForwardMetric1_Object = MibTableColumn
cIpForwardMetric1 = _CIpForwardMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 11),
    _CIpForwardMetric1_Type()
)
cIpForwardMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMetric1.setStatus("obsolete")


class _CIpForwardMetric2_Type(Integer32):
    """Custom type cIpForwardMetric2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpForwardMetric2_Type.__name__ = "Integer32"
_CIpForwardMetric2_Object = MibTableColumn
cIpForwardMetric2 = _CIpForwardMetric2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 12),
    _CIpForwardMetric2_Type()
)
cIpForwardMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMetric2.setStatus("obsolete")


class _CIpForwardMetric3_Type(Integer32):
    """Custom type cIpForwardMetric3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpForwardMetric3_Type.__name__ = "Integer32"
_CIpForwardMetric3_Object = MibTableColumn
cIpForwardMetric3 = _CIpForwardMetric3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 13),
    _CIpForwardMetric3_Type()
)
cIpForwardMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMetric3.setStatus("obsolete")


class _CIpForwardMetric4_Type(Integer32):
    """Custom type cIpForwardMetric4 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpForwardMetric4_Type.__name__ = "Integer32"
_CIpForwardMetric4_Object = MibTableColumn
cIpForwardMetric4 = _CIpForwardMetric4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 14),
    _CIpForwardMetric4_Type()
)
cIpForwardMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMetric4.setStatus("obsolete")


class _CIpForwardMetric5_Type(Integer32):
    """Custom type cIpForwardMetric5 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpForwardMetric5_Type.__name__ = "Integer32"
_CIpForwardMetric5_Object = MibTableColumn
cIpForwardMetric5 = _CIpForwardMetric5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 2, 1, 15),
    _CIpForwardMetric5_Type()
)
cIpForwardMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpForwardMetric5.setStatus("obsolete")
_CIpCidrRouteNumber_Type = Gauge32
_CIpCidrRouteNumber_Object = MibScalar
cIpCidrRouteNumber = _CIpCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 3),
    _CIpCidrRouteNumber_Type()
)
cIpCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteNumber.setStatus("deprecated")
_CIpCidrRouteTable_Object = MibTable
cIpCidrRouteTable = _CIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4)
)
if mibBuilder.loadTexts:
    cIpCidrRouteTable.setStatus("deprecated")
_CIpCidrRouteEntry_Object = MibTableRow
cIpCidrRouteEntry = _CIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1)
)
cIpCidrRouteEntry.setIndexNames(
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteDest"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMask"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteTos"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    cIpCidrRouteEntry.setStatus("deprecated")
_CIpCidrRouteDest_Type = IpAddress
_CIpCidrRouteDest_Object = MibTableColumn
cIpCidrRouteDest = _CIpCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 1),
    _CIpCidrRouteDest_Type()
)
cIpCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteDest.setStatus("deprecated")
_CIpCidrRouteMask_Type = IpAddress
_CIpCidrRouteMask_Object = MibTableColumn
cIpCidrRouteMask = _CIpCidrRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 2),
    _CIpCidrRouteMask_Type()
)
cIpCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteMask.setStatus("deprecated")


class _CIpCidrRouteTos_Type(Integer32):
    """Custom type cIpCidrRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpCidrRouteTos_Type.__name__ = "Integer32"
_CIpCidrRouteTos_Object = MibTableColumn
cIpCidrRouteTos = _CIpCidrRouteTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 3),
    _CIpCidrRouteTos_Type()
)
cIpCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteTos.setStatus("deprecated")
_CIpCidrRouteNextHop_Type = IpAddress
_CIpCidrRouteNextHop_Object = MibTableColumn
cIpCidrRouteNextHop = _CIpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 4),
    _CIpCidrRouteNextHop_Type()
)
cIpCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteNextHop.setStatus("deprecated")


class _CIpCidrRouteIfIndex_Type(Integer32):
    """Custom type cIpCidrRouteIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpCidrRouteIfIndex_Type.__name__ = "Integer32"
_CIpCidrRouteIfIndex_Object = MibTableColumn
cIpCidrRouteIfIndex = _CIpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 5),
    _CIpCidrRouteIfIndex_Type()
)
cIpCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteIfIndex.setStatus("deprecated")


class _CIpCidrRouteType_Type(Integer32):
    """Custom type cIpCidrRouteType based on Integer32"""
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


_CIpCidrRouteType_Type.__name__ = "Integer32"
_CIpCidrRouteType_Object = MibTableColumn
cIpCidrRouteType = _CIpCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 6),
    _CIpCidrRouteType_Type()
)
cIpCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteType.setStatus("deprecated")


class _CIpCidrRouteProto_Type(Integer32):
    """Custom type cIpCidrRouteProto based on Integer32"""
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


_CIpCidrRouteProto_Type.__name__ = "Integer32"
_CIpCidrRouteProto_Object = MibTableColumn
cIpCidrRouteProto = _CIpCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 7),
    _CIpCidrRouteProto_Type()
)
cIpCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteProto.setStatus("deprecated")


class _CIpCidrRouteAge_Type(Integer32):
    """Custom type cIpCidrRouteAge based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpCidrRouteAge_Type.__name__ = "Integer32"
_CIpCidrRouteAge_Object = MibTableColumn
cIpCidrRouteAge = _CIpCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 8),
    _CIpCidrRouteAge_Type()
)
cIpCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpCidrRouteAge.setStatus("deprecated")
_CIpCidrRouteInfo_Type = ObjectIdentifier
_CIpCidrRouteInfo_Object = MibTableColumn
cIpCidrRouteInfo = _CIpCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 9),
    _CIpCidrRouteInfo_Type()
)
cIpCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteInfo.setStatus("deprecated")


class _CIpCidrRouteNextHopAS_Type(Integer32):
    """Custom type cIpCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CIpCidrRouteNextHopAS_Type.__name__ = "Integer32"
_CIpCidrRouteNextHopAS_Object = MibTableColumn
cIpCidrRouteNextHopAS = _CIpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 10),
    _CIpCidrRouteNextHopAS_Type()
)
cIpCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteNextHopAS.setStatus("deprecated")


class _CIpCidrRouteMetric1_Type(Integer32):
    """Custom type cIpCidrRouteMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpCidrRouteMetric1_Type.__name__ = "Integer32"
_CIpCidrRouteMetric1_Object = MibTableColumn
cIpCidrRouteMetric1 = _CIpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 11),
    _CIpCidrRouteMetric1_Type()
)
cIpCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteMetric1.setStatus("deprecated")


class _CIpCidrRouteMetric2_Type(Integer32):
    """Custom type cIpCidrRouteMetric2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpCidrRouteMetric2_Type.__name__ = "Integer32"
_CIpCidrRouteMetric2_Object = MibTableColumn
cIpCidrRouteMetric2 = _CIpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 12),
    _CIpCidrRouteMetric2_Type()
)
cIpCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteMetric2.setStatus("deprecated")


class _CIpCidrRouteMetric3_Type(Integer32):
    """Custom type cIpCidrRouteMetric3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpCidrRouteMetric3_Type.__name__ = "Integer32"
_CIpCidrRouteMetric3_Object = MibTableColumn
cIpCidrRouteMetric3 = _CIpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 13),
    _CIpCidrRouteMetric3_Type()
)
cIpCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteMetric3.setStatus("deprecated")


class _CIpCidrRouteMetric4_Type(Integer32):
    """Custom type cIpCidrRouteMetric4 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpCidrRouteMetric4_Type.__name__ = "Integer32"
_CIpCidrRouteMetric4_Object = MibTableColumn
cIpCidrRouteMetric4 = _CIpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 14),
    _CIpCidrRouteMetric4_Type()
)
cIpCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteMetric4.setStatus("deprecated")


class _CIpCidrRouteMetric5_Type(Integer32):
    """Custom type cIpCidrRouteMetric5 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CIpCidrRouteMetric5_Type.__name__ = "Integer32"
_CIpCidrRouteMetric5_Object = MibTableColumn
cIpCidrRouteMetric5 = _CIpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 15),
    _CIpCidrRouteMetric5_Type()
)
cIpCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteMetric5.setStatus("deprecated")
_CIpCidrRouteStatus_Type = RowStatus
_CIpCidrRouteStatus_Object = MibTableColumn
cIpCidrRouteStatus = _CIpCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 4, 1, 16),
    _CIpCidrRouteStatus_Type()
)
cIpCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIpCidrRouteStatus.setStatus("deprecated")
_CIpForwardConformance_ObjectIdentity = ObjectIdentity
cIpForwardConformance = _CIpForwardConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5)
)
_CIpForwardGroups_ObjectIdentity = ObjectIdentity
cIpForwardGroups = _CIpForwardGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 1)
)
_CIpForwardCompliances_ObjectIdentity = ObjectIdentity
cIpForwardCompliances = _CIpForwardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 2)
)
_CInetCidrRouteNumber_Type = Gauge32
_CInetCidrRouteNumber_Object = MibScalar
cInetCidrRouteNumber = _CInetCidrRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 6),
    _CInetCidrRouteNumber_Type()
)
cInetCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetCidrRouteNumber.setStatus("current")
_CInetCidrRouteTable_Object = MibTable
cInetCidrRouteTable = _CInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7)
)
if mibBuilder.loadTexts:
    cInetCidrRouteTable.setStatus("current")
_CInetCidrRouteEntry_Object = MibTableRow
cInetCidrRouteEntry = _CInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1)
)
cInetCidrRouteEntry.setIndexNames(
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteInstance"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteDestType"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteDest"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRoutePfxLen"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteNextHopType"),
    (0, "CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    cInetCidrRouteEntry.setStatus("current")
_CInetCidrRouteInstance_Type = Unsigned32
_CInetCidrRouteInstance_Object = MibTableColumn
cInetCidrRouteInstance = _CInetCidrRouteInstance_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 1),
    _CInetCidrRouteInstance_Type()
)
cInetCidrRouteInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRouteInstance.setStatus("current")
_CInetCidrRouteDestType_Type = InetAddressType
_CInetCidrRouteDestType_Object = MibTableColumn
cInetCidrRouteDestType = _CInetCidrRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 2),
    _CInetCidrRouteDestType_Type()
)
cInetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRouteDestType.setStatus("current")


class _CInetCidrRouteDest_Type(InetAddress):
    """Custom type cInetCidrRouteDest based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CInetCidrRouteDest_Type.__name__ = "InetAddress"
_CInetCidrRouteDest_Object = MibTableColumn
cInetCidrRouteDest = _CInetCidrRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 3),
    _CInetCidrRouteDest_Type()
)
cInetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRouteDest.setStatus("current")
_CInetCidrRoutePfxLen_Type = InetAddressPrefixLength
_CInetCidrRoutePfxLen_Object = MibTableColumn
cInetCidrRoutePfxLen = _CInetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 4),
    _CInetCidrRoutePfxLen_Type()
)
cInetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRoutePfxLen.setStatus("current")
_CInetCidrRouteNextHopType_Type = InetAddressType
_CInetCidrRouteNextHopType_Object = MibTableColumn
cInetCidrRouteNextHopType = _CInetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 5),
    _CInetCidrRouteNextHopType_Type()
)
cInetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRouteNextHopType.setStatus("current")


class _CInetCidrRouteNextHop_Type(InetAddress):
    """Custom type cInetCidrRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_CInetCidrRouteNextHop_Type.__name__ = "InetAddress"
_CInetCidrRouteNextHop_Object = MibTableColumn
cInetCidrRouteNextHop = _CInetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 6),
    _CInetCidrRouteNextHop_Type()
)
cInetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cInetCidrRouteNextHop.setStatus("current")
_CInetCidrRouteIfIndex_Type = InterfaceIndex
_CInetCidrRouteIfIndex_Object = MibTableColumn
cInetCidrRouteIfIndex = _CInetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 7),
    _CInetCidrRouteIfIndex_Type()
)
cInetCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteIfIndex.setStatus("current")


class _CInetCidrRouteType_Type(Integer32):
    """Custom type cInetCidrRouteType based on Integer32"""
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


_CInetCidrRouteType_Type.__name__ = "Integer32"
_CInetCidrRouteType_Object = MibTableColumn
cInetCidrRouteType = _CInetCidrRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 8),
    _CInetCidrRouteType_Type()
)
cInetCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteType.setStatus("current")
_CInetCidrRouteProto_Type = IANAipRouteProtocol
_CInetCidrRouteProto_Object = MibTableColumn
cInetCidrRouteProto = _CInetCidrRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 9),
    _CInetCidrRouteProto_Type()
)
cInetCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetCidrRouteProto.setStatus("current")


class _CInetCidrRouteAge_Type(Integer32):
    """Custom type cInetCidrRouteAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CInetCidrRouteAge_Type.__name__ = "Integer32"
_CInetCidrRouteAge_Object = MibTableColumn
cInetCidrRouteAge = _CInetCidrRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 10),
    _CInetCidrRouteAge_Type()
)
cInetCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetCidrRouteAge.setStatus("current")


class _CInetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type cInetCidrRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_CInetCidrRouteNextHopAS_Object = MibTableColumn
cInetCidrRouteNextHopAS = _CInetCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 11),
    _CInetCidrRouteNextHopAS_Type()
)
cInetCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteNextHopAS.setStatus("current")


class _CInetCidrRouteMetric1_Type(Integer32):
    """Custom type cInetCidrRouteMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CInetCidrRouteMetric1_Type.__name__ = "Integer32"
_CInetCidrRouteMetric1_Object = MibTableColumn
cInetCidrRouteMetric1 = _CInetCidrRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 12),
    _CInetCidrRouteMetric1_Type()
)
cInetCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteMetric1.setStatus("current")


class _CInetCidrRouteMetric2_Type(Integer32):
    """Custom type cInetCidrRouteMetric2 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CInetCidrRouteMetric2_Type.__name__ = "Integer32"
_CInetCidrRouteMetric2_Object = MibTableColumn
cInetCidrRouteMetric2 = _CInetCidrRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 13),
    _CInetCidrRouteMetric2_Type()
)
cInetCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteMetric2.setStatus("current")


class _CInetCidrRouteMetric3_Type(Integer32):
    """Custom type cInetCidrRouteMetric3 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CInetCidrRouteMetric3_Type.__name__ = "Integer32"
_CInetCidrRouteMetric3_Object = MibTableColumn
cInetCidrRouteMetric3 = _CInetCidrRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 14),
    _CInetCidrRouteMetric3_Type()
)
cInetCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteMetric3.setStatus("current")


class _CInetCidrRouteMetric4_Type(Integer32):
    """Custom type cInetCidrRouteMetric4 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CInetCidrRouteMetric4_Type.__name__ = "Integer32"
_CInetCidrRouteMetric4_Object = MibTableColumn
cInetCidrRouteMetric4 = _CInetCidrRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 15),
    _CInetCidrRouteMetric4_Type()
)
cInetCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteMetric4.setStatus("current")


class _CInetCidrRouteMetric5_Type(Integer32):
    """Custom type cInetCidrRouteMetric5 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CInetCidrRouteMetric5_Type.__name__ = "Integer32"
_CInetCidrRouteMetric5_Object = MibTableColumn
cInetCidrRouteMetric5 = _CInetCidrRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 16),
    _CInetCidrRouteMetric5_Type()
)
cInetCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteMetric5.setStatus("current")
_CInetCidrRouteStatus_Type = RowStatus
_CInetCidrRouteStatus_Object = MibTableColumn
cInetCidrRouteStatus = _CInetCidrRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 7, 1, 17),
    _CInetCidrRouteStatus_Type()
)
cInetCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cInetCidrRouteStatus.setStatus("current")
_CInetCidrRouteDiscards_Type = Counter32
_CInetCidrRouteDiscards_Object = MibScalar
cInetCidrRouteDiscards = _CInetCidrRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 8),
    _CInetCidrRouteDiscards_Type()
)
cInetCidrRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cInetCidrRouteDiscards.setStatus("current")

# Managed Objects groups

cIpForwardMultiPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 1, 2)
)
cIpForwardMultiPathGroup.setObjects(
      *(("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardNumber"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardDest"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMask"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardPolicy"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardNextHop"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardIfIndex"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardType"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardProto"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardAge"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardInfo"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardNextHopAS"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMetric1"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMetric2"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMetric3"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMetric4"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpForwardMetric5"))
)
if mibBuilder.loadTexts:
    cIpForwardMultiPathGroup.setStatus("obsolete")

cIpForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 1, 3)
)
cIpForwardCidrRouteGroup.setObjects(
      *(("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteNumber"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteDest"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMask"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteTos"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteNextHop"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteIfIndex"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteType"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteProto"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteAge"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteInfo"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteNextHopAS"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMetric1"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMetric2"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMetric3"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMetric4"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteMetric5"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cIpCidrRouteStatus"))
)
if mibBuilder.loadTexts:
    cIpForwardCidrRouteGroup.setStatus("deprecated")

cInetForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 1, 4)
)
cInetForwardCidrRouteGroup.setObjects(
      *(("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteNumber"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteDiscards"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteIfIndex"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteType"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteProto"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteAge"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteNextHopAS"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteMetric1"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteMetric2"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteMetric3"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteMetric4"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteMetric5"),
        ("CISCO-IETF-IP-FORWARD-MIB", "cInetCidrRouteStatus"))
)
if mibBuilder.loadTexts:
    cInetForwardCidrRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cIpForwardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 2, 1)
)
if mibBuilder.loadTexts:
    cIpForwardCompliance.setStatus(
        "deprecated"
    )

cIpForwardOldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 2, 2)
)
if mibBuilder.loadTexts:
    cIpForwardOldCompliance.setStatus(
        "obsolete"
    )

cIpForwardCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 85, 5, 2, 3)
)
if mibBuilder.loadTexts:
    cIpForwardCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-IP-FORWARD-MIB",
    **{"ciscoIetfIpForward": ciscoIetfIpForward,
       "cIpForwardNumber": cIpForwardNumber,
       "cIpForwardTable": cIpForwardTable,
       "cIpForwardEntry": cIpForwardEntry,
       "cIpForwardDest": cIpForwardDest,
       "cIpForwardMask": cIpForwardMask,
       "cIpForwardPolicy": cIpForwardPolicy,
       "cIpForwardNextHop": cIpForwardNextHop,
       "cIpForwardIfIndex": cIpForwardIfIndex,
       "cIpForwardType": cIpForwardType,
       "cIpForwardProto": cIpForwardProto,
       "cIpForwardAge": cIpForwardAge,
       "cIpForwardInfo": cIpForwardInfo,
       "cIpForwardNextHopAS": cIpForwardNextHopAS,
       "cIpForwardMetric1": cIpForwardMetric1,
       "cIpForwardMetric2": cIpForwardMetric2,
       "cIpForwardMetric3": cIpForwardMetric3,
       "cIpForwardMetric4": cIpForwardMetric4,
       "cIpForwardMetric5": cIpForwardMetric5,
       "cIpCidrRouteNumber": cIpCidrRouteNumber,
       "cIpCidrRouteTable": cIpCidrRouteTable,
       "cIpCidrRouteEntry": cIpCidrRouteEntry,
       "cIpCidrRouteDest": cIpCidrRouteDest,
       "cIpCidrRouteMask": cIpCidrRouteMask,
       "cIpCidrRouteTos": cIpCidrRouteTos,
       "cIpCidrRouteNextHop": cIpCidrRouteNextHop,
       "cIpCidrRouteIfIndex": cIpCidrRouteIfIndex,
       "cIpCidrRouteType": cIpCidrRouteType,
       "cIpCidrRouteProto": cIpCidrRouteProto,
       "cIpCidrRouteAge": cIpCidrRouteAge,
       "cIpCidrRouteInfo": cIpCidrRouteInfo,
       "cIpCidrRouteNextHopAS": cIpCidrRouteNextHopAS,
       "cIpCidrRouteMetric1": cIpCidrRouteMetric1,
       "cIpCidrRouteMetric2": cIpCidrRouteMetric2,
       "cIpCidrRouteMetric3": cIpCidrRouteMetric3,
       "cIpCidrRouteMetric4": cIpCidrRouteMetric4,
       "cIpCidrRouteMetric5": cIpCidrRouteMetric5,
       "cIpCidrRouteStatus": cIpCidrRouteStatus,
       "cIpForwardConformance": cIpForwardConformance,
       "cIpForwardGroups": cIpForwardGroups,
       "cIpForwardMultiPathGroup": cIpForwardMultiPathGroup,
       "cIpForwardCidrRouteGroup": cIpForwardCidrRouteGroup,
       "cInetForwardCidrRouteGroup": cInetForwardCidrRouteGroup,
       "cIpForwardCompliances": cIpForwardCompliances,
       "cIpForwardCompliance": cIpForwardCompliance,
       "cIpForwardOldCompliance": cIpForwardOldCompliance,
       "cIpForwardCompliance2": cIpForwardCompliance2,
       "cInetCidrRouteNumber": cInetCidrRouteNumber,
       "cInetCidrRouteTable": cInetCidrRouteTable,
       "cInetCidrRouteEntry": cInetCidrRouteEntry,
       "cInetCidrRouteInstance": cInetCidrRouteInstance,
       "cInetCidrRouteDestType": cInetCidrRouteDestType,
       "cInetCidrRouteDest": cInetCidrRouteDest,
       "cInetCidrRoutePfxLen": cInetCidrRoutePfxLen,
       "cInetCidrRouteNextHopType": cInetCidrRouteNextHopType,
       "cInetCidrRouteNextHop": cInetCidrRouteNextHop,
       "cInetCidrRouteIfIndex": cInetCidrRouteIfIndex,
       "cInetCidrRouteType": cInetCidrRouteType,
       "cInetCidrRouteProto": cInetCidrRouteProto,
       "cInetCidrRouteAge": cInetCidrRouteAge,
       "cInetCidrRouteNextHopAS": cInetCidrRouteNextHopAS,
       "cInetCidrRouteMetric1": cInetCidrRouteMetric1,
       "cInetCidrRouteMetric2": cInetCidrRouteMetric2,
       "cInetCidrRouteMetric3": cInetCidrRouteMetric3,
       "cInetCidrRouteMetric4": cInetCidrRouteMetric4,
       "cInetCidrRouteMetric5": cInetCidrRouteMetric5,
       "cInetCidrRouteStatus": cInetCidrRouteStatus,
       "cInetCidrRouteDiscards": cInetCidrRouteDiscards}
)
