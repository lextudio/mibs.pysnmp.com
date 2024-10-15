# SNMP MIB module (IP-FORWARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IP-FORWARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:13 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
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

(ip,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ip")

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

ipForward = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24)
)
ipForward.setRevisions(
        ("2006-02-01 00:00",
         "1996-09-19 00:00",
         "1992-07-02 21:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpForwardNumber_Type = Gauge32
_IpForwardNumber_Object = MibScalar
ipForwardNumber = _IpForwardNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 1),
    _IpForwardNumber_Type()
)
ipForwardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNumber.setStatus("obsolete")
_IpForwardTable_Object = MibTable
ipForwardTable = _IpForwardTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2)
)
if mibBuilder.loadTexts:
    ipForwardTable.setStatus("obsolete")
_IpForwardEntry_Object = MibTableRow
ipForwardEntry = _IpForwardEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1)
)
ipForwardEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "ipForwardDest"),
    (0, "IP-FORWARD-MIB", "ipForwardProto"),
    (0, "IP-FORWARD-MIB", "ipForwardPolicy"),
    (0, "IP-FORWARD-MIB", "ipForwardNextHop"),
)
if mibBuilder.loadTexts:
    ipForwardEntry.setStatus("obsolete")
_IpForwardDest_Type = IpAddress
_IpForwardDest_Object = MibTableColumn
ipForwardDest = _IpForwardDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 1),
    _IpForwardDest_Type()
)
ipForwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardDest.setStatus("obsolete")


class _IpForwardMask_Type(IpAddress):
    """Custom type ipForwardMask based on IpAddress"""
    defaultHexValue = "00000000"


_IpForwardMask_Object = MibTableColumn
ipForwardMask = _IpForwardMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 2),
    _IpForwardMask_Type()
)
ipForwardMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMask.setStatus("obsolete")


class _IpForwardPolicy_Type(Integer32):
    """Custom type ipForwardPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpForwardPolicy_Type.__name__ = "Integer32"
_IpForwardPolicy_Object = MibTableColumn
ipForwardPolicy = _IpForwardPolicy_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 3),
    _IpForwardPolicy_Type()
)
ipForwardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardPolicy.setStatus("obsolete")
_IpForwardNextHop_Type = IpAddress
_IpForwardNextHop_Object = MibTableColumn
ipForwardNextHop = _IpForwardNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 4),
    _IpForwardNextHop_Type()
)
ipForwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardNextHop.setStatus("obsolete")


class _IpForwardIfIndex_Type(Integer32):
    """Custom type ipForwardIfIndex based on Integer32"""
    defaultValue = 0


_IpForwardIfIndex_Object = MibTableColumn
ipForwardIfIndex = _IpForwardIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 5),
    _IpForwardIfIndex_Type()
)
ipForwardIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardIfIndex.setStatus("obsolete")


class _IpForwardType_Type(Integer32):
    """Custom type ipForwardType based on Integer32"""
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


_IpForwardType_Type.__name__ = "Integer32"
_IpForwardType_Object = MibTableColumn
ipForwardType = _IpForwardType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 6),
    _IpForwardType_Type()
)
ipForwardType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardType.setStatus("obsolete")


class _IpForwardProto_Type(Integer32):
    """Custom type ipForwardProto based on Integer32"""
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


_IpForwardProto_Type.__name__ = "Integer32"
_IpForwardProto_Object = MibTableColumn
ipForwardProto = _IpForwardProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 7),
    _IpForwardProto_Type()
)
ipForwardProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardProto.setStatus("obsolete")


class _IpForwardAge_Type(Integer32):
    """Custom type ipForwardAge based on Integer32"""
    defaultValue = 0


_IpForwardAge_Object = MibTableColumn
ipForwardAge = _IpForwardAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 8),
    _IpForwardAge_Type()
)
ipForwardAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardAge.setStatus("obsolete")
_IpForwardInfo_Type = ObjectIdentifier
_IpForwardInfo_Object = MibTableColumn
ipForwardInfo = _IpForwardInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 9),
    _IpForwardInfo_Type()
)
ipForwardInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardInfo.setStatus("obsolete")


class _IpForwardNextHopAS_Type(Integer32):
    """Custom type ipForwardNextHopAS based on Integer32"""
    defaultValue = 0


_IpForwardNextHopAS_Object = MibTableColumn
ipForwardNextHopAS = _IpForwardNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 10),
    _IpForwardNextHopAS_Type()
)
ipForwardNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardNextHopAS.setStatus("obsolete")


class _IpForwardMetric1_Type(Integer32):
    """Custom type ipForwardMetric1 based on Integer32"""
    defaultValue = -1


_IpForwardMetric1_Object = MibTableColumn
ipForwardMetric1 = _IpForwardMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 11),
    _IpForwardMetric1_Type()
)
ipForwardMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric1.setStatus("obsolete")


class _IpForwardMetric2_Type(Integer32):
    """Custom type ipForwardMetric2 based on Integer32"""
    defaultValue = -1


_IpForwardMetric2_Object = MibTableColumn
ipForwardMetric2 = _IpForwardMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 12),
    _IpForwardMetric2_Type()
)
ipForwardMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric2.setStatus("obsolete")


class _IpForwardMetric3_Type(Integer32):
    """Custom type ipForwardMetric3 based on Integer32"""
    defaultValue = -1


_IpForwardMetric3_Object = MibTableColumn
ipForwardMetric3 = _IpForwardMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 13),
    _IpForwardMetric3_Type()
)
ipForwardMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric3.setStatus("obsolete")


class _IpForwardMetric4_Type(Integer32):
    """Custom type ipForwardMetric4 based on Integer32"""
    defaultValue = -1


_IpForwardMetric4_Object = MibTableColumn
ipForwardMetric4 = _IpForwardMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 14),
    _IpForwardMetric4_Type()
)
ipForwardMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric4.setStatus("obsolete")


class _IpForwardMetric5_Type(Integer32):
    """Custom type ipForwardMetric5 based on Integer32"""
    defaultValue = -1


_IpForwardMetric5_Object = MibTableColumn
ipForwardMetric5 = _IpForwardMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 15),
    _IpForwardMetric5_Type()
)
ipForwardMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipForwardMetric5.setStatus("obsolete")
_IpCidrRouteNumber_Type = Gauge32
_IpCidrRouteNumber_Object = MibScalar
ipCidrRouteNumber = _IpCidrRouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 3),
    _IpCidrRouteNumber_Type()
)
ipCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteNumber.setStatus("deprecated")
_IpCidrRouteTable_Object = MibTable
ipCidrRouteTable = _IpCidrRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4)
)
if mibBuilder.loadTexts:
    ipCidrRouteTable.setStatus("deprecated")
_IpCidrRouteEntry_Object = MibTableRow
ipCidrRouteEntry = _IpCidrRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1)
)
ipCidrRouteEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "ipCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteMask"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteTos"),
    (0, "IP-FORWARD-MIB", "ipCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    ipCidrRouteEntry.setStatus("deprecated")
_IpCidrRouteDest_Type = IpAddress
_IpCidrRouteDest_Object = MibTableColumn
ipCidrRouteDest = _IpCidrRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 1),
    _IpCidrRouteDest_Type()
)
ipCidrRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteDest.setStatus("deprecated")
_IpCidrRouteMask_Type = IpAddress
_IpCidrRouteMask_Object = MibTableColumn
ipCidrRouteMask = _IpCidrRouteMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 2),
    _IpCidrRouteMask_Type()
)
ipCidrRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteMask.setStatus("deprecated")


class _IpCidrRouteTos_Type(Integer32):
    """Custom type ipCidrRouteTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpCidrRouteTos_Type.__name__ = "Integer32"
_IpCidrRouteTos_Object = MibTableColumn
ipCidrRouteTos = _IpCidrRouteTos_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 3),
    _IpCidrRouteTos_Type()
)
ipCidrRouteTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteTos.setStatus("deprecated")
_IpCidrRouteNextHop_Type = IpAddress
_IpCidrRouteNextHop_Object = MibTableColumn
ipCidrRouteNextHop = _IpCidrRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 4),
    _IpCidrRouteNextHop_Type()
)
ipCidrRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteNextHop.setStatus("deprecated")


class _IpCidrRouteIfIndex_Type(Integer32):
    """Custom type ipCidrRouteIfIndex based on Integer32"""
    defaultValue = 0


_IpCidrRouteIfIndex_Object = MibTableColumn
ipCidrRouteIfIndex = _IpCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 5),
    _IpCidrRouteIfIndex_Type()
)
ipCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteIfIndex.setStatus("deprecated")


class _IpCidrRouteType_Type(Integer32):
    """Custom type ipCidrRouteType based on Integer32"""
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


_IpCidrRouteType_Type.__name__ = "Integer32"
_IpCidrRouteType_Object = MibTableColumn
ipCidrRouteType = _IpCidrRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 6),
    _IpCidrRouteType_Type()
)
ipCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteType.setStatus("deprecated")


class _IpCidrRouteProto_Type(Integer32):
    """Custom type ipCidrRouteProto based on Integer32"""
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


_IpCidrRouteProto_Type.__name__ = "Integer32"
_IpCidrRouteProto_Object = MibTableColumn
ipCidrRouteProto = _IpCidrRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 7),
    _IpCidrRouteProto_Type()
)
ipCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteProto.setStatus("deprecated")


class _IpCidrRouteAge_Type(Integer32):
    """Custom type ipCidrRouteAge based on Integer32"""
    defaultValue = 0


_IpCidrRouteAge_Object = MibTableColumn
ipCidrRouteAge = _IpCidrRouteAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 8),
    _IpCidrRouteAge_Type()
)
ipCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteAge.setStatus("deprecated")
_IpCidrRouteInfo_Type = ObjectIdentifier
_IpCidrRouteInfo_Object = MibTableColumn
ipCidrRouteInfo = _IpCidrRouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 9),
    _IpCidrRouteInfo_Type()
)
ipCidrRouteInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteInfo.setStatus("deprecated")


class _IpCidrRouteNextHopAS_Type(Integer32):
    """Custom type ipCidrRouteNextHopAS based on Integer32"""
    defaultValue = 0


_IpCidrRouteNextHopAS_Object = MibTableColumn
ipCidrRouteNextHopAS = _IpCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 10),
    _IpCidrRouteNextHopAS_Type()
)
ipCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteNextHopAS.setStatus("deprecated")


class _IpCidrRouteMetric1_Type(Integer32):
    """Custom type ipCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric1_Object = MibTableColumn
ipCidrRouteMetric1 = _IpCidrRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 11),
    _IpCidrRouteMetric1_Type()
)
ipCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric1.setStatus("deprecated")


class _IpCidrRouteMetric2_Type(Integer32):
    """Custom type ipCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric2_Object = MibTableColumn
ipCidrRouteMetric2 = _IpCidrRouteMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 12),
    _IpCidrRouteMetric2_Type()
)
ipCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric2.setStatus("deprecated")


class _IpCidrRouteMetric3_Type(Integer32):
    """Custom type ipCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric3_Object = MibTableColumn
ipCidrRouteMetric3 = _IpCidrRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 13),
    _IpCidrRouteMetric3_Type()
)
ipCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric3.setStatus("deprecated")


class _IpCidrRouteMetric4_Type(Integer32):
    """Custom type ipCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric4_Object = MibTableColumn
ipCidrRouteMetric4 = _IpCidrRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 14),
    _IpCidrRouteMetric4_Type()
)
ipCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric4.setStatus("deprecated")


class _IpCidrRouteMetric5_Type(Integer32):
    """Custom type ipCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_IpCidrRouteMetric5_Object = MibTableColumn
ipCidrRouteMetric5 = _IpCidrRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 15),
    _IpCidrRouteMetric5_Type()
)
ipCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteMetric5.setStatus("deprecated")
_IpCidrRouteStatus_Type = RowStatus
_IpCidrRouteStatus_Object = MibTableColumn
ipCidrRouteStatus = _IpCidrRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 16),
    _IpCidrRouteStatus_Type()
)
ipCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipCidrRouteStatus.setStatus("deprecated")
_IpForwardConformance_ObjectIdentity = ObjectIdentity
ipForwardConformance = _IpForwardConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5)
)
_IpForwardGroups_ObjectIdentity = ObjectIdentity
ipForwardGroups = _IpForwardGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1)
)
_IpForwardCompliances_ObjectIdentity = ObjectIdentity
ipForwardCompliances = _IpForwardCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2)
)
_InetCidrRouteNumber_Type = Gauge32
_InetCidrRouteNumber_Object = MibScalar
inetCidrRouteNumber = _InetCidrRouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 6),
    _InetCidrRouteNumber_Type()
)
inetCidrRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteNumber.setStatus("current")
_InetCidrRouteTable_Object = MibTable
inetCidrRouteTable = _InetCidrRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7)
)
if mibBuilder.loadTexts:
    inetCidrRouteTable.setStatus("current")
_InetCidrRouteEntry_Object = MibTableRow
inetCidrRouteEntry = _InetCidrRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1)
)
inetCidrRouteEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "inetCidrRouteDestType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteDest"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"),
    (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"),
    (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"),
)
if mibBuilder.loadTexts:
    inetCidrRouteEntry.setStatus("current")
_InetCidrRouteDestType_Type = InetAddressType
_InetCidrRouteDestType_Object = MibTableColumn
inetCidrRouteDestType = _InetCidrRouteDestType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 1),
    _InetCidrRouteDestType_Type()
)
inetCidrRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteDestType.setStatus("current")
_InetCidrRouteDest_Type = InetAddress
_InetCidrRouteDest_Object = MibTableColumn
inetCidrRouteDest = _InetCidrRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 2),
    _InetCidrRouteDest_Type()
)
inetCidrRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteDest.setStatus("current")
_InetCidrRoutePfxLen_Type = InetAddressPrefixLength
_InetCidrRoutePfxLen_Object = MibTableColumn
inetCidrRoutePfxLen = _InetCidrRoutePfxLen_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 3),
    _InetCidrRoutePfxLen_Type()
)
inetCidrRoutePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRoutePfxLen.setStatus("current")
_InetCidrRoutePolicy_Type = ObjectIdentifier
_InetCidrRoutePolicy_Object = MibTableColumn
inetCidrRoutePolicy = _InetCidrRoutePolicy_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 4),
    _InetCidrRoutePolicy_Type()
)
inetCidrRoutePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRoutePolicy.setStatus("current")
_InetCidrRouteNextHopType_Type = InetAddressType
_InetCidrRouteNextHopType_Object = MibTableColumn
inetCidrRouteNextHopType = _InetCidrRouteNextHopType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 5),
    _InetCidrRouteNextHopType_Type()
)
inetCidrRouteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopType.setStatus("current")
_InetCidrRouteNextHop_Type = InetAddress
_InetCidrRouteNextHop_Object = MibTableColumn
inetCidrRouteNextHop = _InetCidrRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 6),
    _InetCidrRouteNextHop_Type()
)
inetCidrRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    inetCidrRouteNextHop.setStatus("current")
_InetCidrRouteIfIndex_Type = InterfaceIndexOrZero
_InetCidrRouteIfIndex_Object = MibTableColumn
inetCidrRouteIfIndex = _InetCidrRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 7),
    _InetCidrRouteIfIndex_Type()
)
inetCidrRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteIfIndex.setStatus("current")


class _InetCidrRouteType_Type(Integer32):
    """Custom type inetCidrRouteType based on Integer32"""
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


_InetCidrRouteType_Type.__name__ = "Integer32"
_InetCidrRouteType_Object = MibTableColumn
inetCidrRouteType = _InetCidrRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 8),
    _InetCidrRouteType_Type()
)
inetCidrRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteType.setStatus("current")
_InetCidrRouteProto_Type = IANAipRouteProtocol
_InetCidrRouteProto_Object = MibTableColumn
inetCidrRouteProto = _InetCidrRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 9),
    _InetCidrRouteProto_Type()
)
inetCidrRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteProto.setStatus("current")
_InetCidrRouteAge_Type = Gauge32
_InetCidrRouteAge_Object = MibTableColumn
inetCidrRouteAge = _InetCidrRouteAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 10),
    _InetCidrRouteAge_Type()
)
inetCidrRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteAge.setStatus("current")


class _InetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):
    """Custom type inetCidrRouteNextHopAS based on InetAutonomousSystemNumber"""
    defaultValue = 0


_InetCidrRouteNextHopAS_Object = MibTableColumn
inetCidrRouteNextHopAS = _InetCidrRouteNextHopAS_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 11),
    _InetCidrRouteNextHopAS_Type()
)
inetCidrRouteNextHopAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteNextHopAS.setStatus("current")


class _InetCidrRouteMetric1_Type(Integer32):
    """Custom type inetCidrRouteMetric1 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric1_Object = MibTableColumn
inetCidrRouteMetric1 = _InetCidrRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 12),
    _InetCidrRouteMetric1_Type()
)
inetCidrRouteMetric1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric1.setStatus("current")


class _InetCidrRouteMetric2_Type(Integer32):
    """Custom type inetCidrRouteMetric2 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric2_Object = MibTableColumn
inetCidrRouteMetric2 = _InetCidrRouteMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 13),
    _InetCidrRouteMetric2_Type()
)
inetCidrRouteMetric2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric2.setStatus("current")


class _InetCidrRouteMetric3_Type(Integer32):
    """Custom type inetCidrRouteMetric3 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric3_Object = MibTableColumn
inetCidrRouteMetric3 = _InetCidrRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 14),
    _InetCidrRouteMetric3_Type()
)
inetCidrRouteMetric3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric3.setStatus("current")


class _InetCidrRouteMetric4_Type(Integer32):
    """Custom type inetCidrRouteMetric4 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric4_Object = MibTableColumn
inetCidrRouteMetric4 = _InetCidrRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 15),
    _InetCidrRouteMetric4_Type()
)
inetCidrRouteMetric4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric4.setStatus("current")


class _InetCidrRouteMetric5_Type(Integer32):
    """Custom type inetCidrRouteMetric5 based on Integer32"""
    defaultValue = -1


_InetCidrRouteMetric5_Object = MibTableColumn
inetCidrRouteMetric5 = _InetCidrRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 16),
    _InetCidrRouteMetric5_Type()
)
inetCidrRouteMetric5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteMetric5.setStatus("current")
_InetCidrRouteStatus_Type = RowStatus
_InetCidrRouteStatus_Object = MibTableColumn
inetCidrRouteStatus = _InetCidrRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 17),
    _InetCidrRouteStatus_Type()
)
inetCidrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    inetCidrRouteStatus.setStatus("current")
_InetCidrRouteDiscards_Type = Counter32
_InetCidrRouteDiscards_Object = MibScalar
inetCidrRouteDiscards = _InetCidrRouteDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 24, 8),
    _InetCidrRouteDiscards_Type()
)
inetCidrRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inetCidrRouteDiscards.setStatus("current")

# Managed Objects groups

ipForwardMultiPathGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 2)
)
ipForwardMultiPathGroup.setObjects(
      *(("IP-FORWARD-MIB", "ipForwardNumber"),
        ("IP-FORWARD-MIB", "ipForwardDest"),
        ("IP-FORWARD-MIB", "ipForwardMask"),
        ("IP-FORWARD-MIB", "ipForwardPolicy"),
        ("IP-FORWARD-MIB", "ipForwardNextHop"),
        ("IP-FORWARD-MIB", "ipForwardIfIndex"),
        ("IP-FORWARD-MIB", "ipForwardType"),
        ("IP-FORWARD-MIB", "ipForwardProto"),
        ("IP-FORWARD-MIB", "ipForwardAge"),
        ("IP-FORWARD-MIB", "ipForwardInfo"),
        ("IP-FORWARD-MIB", "ipForwardNextHopAS"),
        ("IP-FORWARD-MIB", "ipForwardMetric1"),
        ("IP-FORWARD-MIB", "ipForwardMetric2"),
        ("IP-FORWARD-MIB", "ipForwardMetric3"),
        ("IP-FORWARD-MIB", "ipForwardMetric4"),
        ("IP-FORWARD-MIB", "ipForwardMetric5"))
)
if mibBuilder.loadTexts:
    ipForwardMultiPathGroup.setStatus("obsolete")

ipForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 3)
)
ipForwardCidrRouteGroup.setObjects(
      *(("IP-FORWARD-MIB", "ipCidrRouteNumber"),
        ("IP-FORWARD-MIB", "ipCidrRouteDest"),
        ("IP-FORWARD-MIB", "ipCidrRouteMask"),
        ("IP-FORWARD-MIB", "ipCidrRouteTos"),
        ("IP-FORWARD-MIB", "ipCidrRouteNextHop"),
        ("IP-FORWARD-MIB", "ipCidrRouteIfIndex"),
        ("IP-FORWARD-MIB", "ipCidrRouteType"),
        ("IP-FORWARD-MIB", "ipCidrRouteProto"),
        ("IP-FORWARD-MIB", "ipCidrRouteAge"),
        ("IP-FORWARD-MIB", "ipCidrRouteInfo"),
        ("IP-FORWARD-MIB", "ipCidrRouteNextHopAS"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric1"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric2"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric3"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric4"),
        ("IP-FORWARD-MIB", "ipCidrRouteMetric5"),
        ("IP-FORWARD-MIB", "ipCidrRouteStatus"))
)
if mibBuilder.loadTexts:
    ipForwardCidrRouteGroup.setStatus("deprecated")

inetForwardCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 4)
)
inetForwardCidrRouteGroup.setObjects(
      *(("IP-FORWARD-MIB", "inetCidrRouteDiscards"),
        ("IP-FORWARD-MIB", "inetCidrRouteIfIndex"),
        ("IP-FORWARD-MIB", "inetCidrRouteType"),
        ("IP-FORWARD-MIB", "inetCidrRouteProto"),
        ("IP-FORWARD-MIB", "inetCidrRouteAge"),
        ("IP-FORWARD-MIB", "inetCidrRouteNextHopAS"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric1"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric2"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric3"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric4"),
        ("IP-FORWARD-MIB", "inetCidrRouteMetric5"),
        ("IP-FORWARD-MIB", "inetCidrRouteStatus"),
        ("IP-FORWARD-MIB", "inetCidrRouteNumber"))
)
if mibBuilder.loadTexts:
    inetForwardCidrRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipForwardCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 1)
)
if mibBuilder.loadTexts:
    ipForwardCompliance.setStatus(
        "deprecated"
    )

ipForwardOldCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 2)
)
if mibBuilder.loadTexts:
    ipForwardOldCompliance.setStatus(
        "obsolete"
    )

ipForwardFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 3)
)
if mibBuilder.loadTexts:
    ipForwardFullCompliance.setStatus(
        "current"
    )

ipForwardReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 4)
)
if mibBuilder.loadTexts:
    ipForwardReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-FORWARD-MIB",
    **{"ipForward": ipForward,
       "ipForwardNumber": ipForwardNumber,
       "ipForwardTable": ipForwardTable,
       "ipForwardEntry": ipForwardEntry,
       "ipForwardDest": ipForwardDest,
       "ipForwardMask": ipForwardMask,
       "ipForwardPolicy": ipForwardPolicy,
       "ipForwardNextHop": ipForwardNextHop,
       "ipForwardIfIndex": ipForwardIfIndex,
       "ipForwardType": ipForwardType,
       "ipForwardProto": ipForwardProto,
       "ipForwardAge": ipForwardAge,
       "ipForwardInfo": ipForwardInfo,
       "ipForwardNextHopAS": ipForwardNextHopAS,
       "ipForwardMetric1": ipForwardMetric1,
       "ipForwardMetric2": ipForwardMetric2,
       "ipForwardMetric3": ipForwardMetric3,
       "ipForwardMetric4": ipForwardMetric4,
       "ipForwardMetric5": ipForwardMetric5,
       "ipCidrRouteNumber": ipCidrRouteNumber,
       "ipCidrRouteTable": ipCidrRouteTable,
       "ipCidrRouteEntry": ipCidrRouteEntry,
       "ipCidrRouteDest": ipCidrRouteDest,
       "ipCidrRouteMask": ipCidrRouteMask,
       "ipCidrRouteTos": ipCidrRouteTos,
       "ipCidrRouteNextHop": ipCidrRouteNextHop,
       "ipCidrRouteIfIndex": ipCidrRouteIfIndex,
       "ipCidrRouteType": ipCidrRouteType,
       "ipCidrRouteProto": ipCidrRouteProto,
       "ipCidrRouteAge": ipCidrRouteAge,
       "ipCidrRouteInfo": ipCidrRouteInfo,
       "ipCidrRouteNextHopAS": ipCidrRouteNextHopAS,
       "ipCidrRouteMetric1": ipCidrRouteMetric1,
       "ipCidrRouteMetric2": ipCidrRouteMetric2,
       "ipCidrRouteMetric3": ipCidrRouteMetric3,
       "ipCidrRouteMetric4": ipCidrRouteMetric4,
       "ipCidrRouteMetric5": ipCidrRouteMetric5,
       "ipCidrRouteStatus": ipCidrRouteStatus,
       "ipForwardConformance": ipForwardConformance,
       "ipForwardGroups": ipForwardGroups,
       "ipForwardMultiPathGroup": ipForwardMultiPathGroup,
       "ipForwardCidrRouteGroup": ipForwardCidrRouteGroup,
       "inetForwardCidrRouteGroup": inetForwardCidrRouteGroup,
       "ipForwardCompliances": ipForwardCompliances,
       "ipForwardCompliance": ipForwardCompliance,
       "ipForwardOldCompliance": ipForwardOldCompliance,
       "ipForwardFullCompliance": ipForwardFullCompliance,
       "ipForwardReadOnlyCompliance": ipForwardReadOnlyCompliance,
       "inetCidrRouteNumber": inetCidrRouteNumber,
       "inetCidrRouteTable": inetCidrRouteTable,
       "inetCidrRouteEntry": inetCidrRouteEntry,
       "inetCidrRouteDestType": inetCidrRouteDestType,
       "inetCidrRouteDest": inetCidrRouteDest,
       "inetCidrRoutePfxLen": inetCidrRoutePfxLen,
       "inetCidrRoutePolicy": inetCidrRoutePolicy,
       "inetCidrRouteNextHopType": inetCidrRouteNextHopType,
       "inetCidrRouteNextHop": inetCidrRouteNextHop,
       "inetCidrRouteIfIndex": inetCidrRouteIfIndex,
       "inetCidrRouteType": inetCidrRouteType,
       "inetCidrRouteProto": inetCidrRouteProto,
       "inetCidrRouteAge": inetCidrRouteAge,
       "inetCidrRouteNextHopAS": inetCidrRouteNextHopAS,
       "inetCidrRouteMetric1": inetCidrRouteMetric1,
       "inetCidrRouteMetric2": inetCidrRouteMetric2,
       "inetCidrRouteMetric3": inetCidrRouteMetric3,
       "inetCidrRouteMetric4": inetCidrRouteMetric4,
       "inetCidrRouteMetric5": inetCidrRouteMetric5,
       "inetCidrRouteStatus": inetCidrRouteStatus,
       "inetCidrRouteDiscards": inetCidrRouteDiscards}
)
