# SNMP MIB module (HP-ICF-IP-ROUTING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-IP-ROUTING
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:35 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(HpInetCidrRouteState,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "HpInetCidrRouteState")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(inetCidrRouteDestType,
 inetCidrRouteEntry,
 ipCidrRouteEntry) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "inetCidrRouteDestType",
    "inetCidrRouteEntry",
    "ipCidrRouteEntry")

(ipDefaultRouterEntry,
 ipv6RouterAdvertEntry) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipDefaultRouterEntry",
    "ipv6RouterAdvertEntry")

(Metric,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "Metric")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfIpRouting = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15)
)
hpicfIpRouting.setRevisions(
        ("2016-12-02 00:00",
         "2016-11-09 00:00",
         "2016-03-18 00:00",
         "2016-02-17 00:00",
         "2014-08-26 00:00",
         "2013-06-03 00:00",
         "2012-10-20 00:00",
         "2011-11-10 00:00",
         "2011-08-30 00:00",
         "2010-11-29 00:00",
         "2010-05-27 00:00",
         "2009-11-05 00:00",
         "2009-10-12 00:00",
         "2008-12-19 00:00",
         "2008-04-08 00:00",
         "2008-03-04 00:00",
         "2007-04-20 00:00",
         "2005-08-13 02:28",
         "2005-08-05 00:00",
         "2003-05-13 02:28",
         "2002-10-31 23:53",
         "2002-05-23 17:38",
         "2000-07-15 00:22")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfIpRouteProtoName(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              15,
              17,
              18,
              22,
              23,
              24,
              25,
              27,
              32,
              33,
              40,
              42)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 10),
          ("connected", 1),
          ("igmpv3", 32),
          ("ipv4", 18),
          ("ipv6", 7),
          ("isis", 15),
          ("mpls", 40),
          ("mroute", 27),
          ("ospf2", 24),
          ("ospf2ase", 8),
          ("ospf2nssa", 25),
          ("pim", 22),
          ("pim6", 33),
          ("rdisc", 23),
          ("rdisc6", 11),
          ("rip", 9),
          ("ripng", 17),
          ("snmp", 13),
          ("static", 12),
          ("vrrp2", 42))
    )



class HpicfIpv6RouteProtoName(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              15,
              17,
              18,
              22,
              23,
              24,
              25,
              27,
              32,
              33,
              40,
              42)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 10),
          ("connected", 1),
          ("igmpv3", 32),
          ("ipv4", 18),
          ("ipv6", 7),
          ("isis", 15),
          ("mpls", 40),
          ("mroute", 27),
          ("ospf2", 24),
          ("ospf2ase", 8),
          ("ospf2nssa", 25),
          ("ospf3", 4),
          ("ospf3ase", 5),
          ("ospf3nssa", 6),
          ("pim", 22),
          ("pim6", 33),
          ("rdisc", 23),
          ("rdisc6", 11),
          ("rip", 9),
          ("ripng", 17),
          ("snmp", 13),
          ("static", 12),
          ("vrrp2", 42))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfIpRoutingObjects_ObjectIdentity = ObjectIdentity
hpicfIpRoutingObjects = _HpicfIpRoutingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1)
)
_HpicfIcmpRdisc_ObjectIdentity = ObjectIdentity
hpicfIcmpRdisc = _HpicfIcmpRdisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1)
)


class _HpicfRdiscAdminStatus_Type(Integer32):
    """Custom type hpicfRdiscAdminStatus based on Integer32"""
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


_HpicfRdiscAdminStatus_Type.__name__ = "Integer32"
_HpicfRdiscAdminStatus_Object = MibScalar
hpicfRdiscAdminStatus = _HpicfRdiscAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 1),
    _HpicfRdiscAdminStatus_Type()
)
hpicfRdiscAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscAdminStatus.setStatus("current")
_HpicfRdiscIfCfgTable_Object = MibTable
hpicfRdiscIfCfgTable = _HpicfRdiscIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfRdiscIfCfgTable.setStatus("current")
_HpicfRdiscIfCfgEntry_Object = MibTableRow
hpicfRdiscIfCfgEntry = _HpicfRdiscIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1)
)
hpicfRdiscIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfRdiscIfCfgEntry.setStatus("current")


class _HpicfRdiscIfAdminStatus_Type(Integer32):
    """Custom type hpicfRdiscIfAdminStatus based on Integer32"""
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


_HpicfRdiscIfAdminStatus_Type.__name__ = "Integer32"
_HpicfRdiscIfAdminStatus_Object = MibTableColumn
hpicfRdiscIfAdminStatus = _HpicfRdiscIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 1),
    _HpicfRdiscIfAdminStatus_Type()
)
hpicfRdiscIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfAdminStatus.setStatus("current")


class _HpicfRdiscIfAdvertAddress_Type(Integer32):
    """Custom type hpicfRdiscIfAdvertAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 1))
    )


_HpicfRdiscIfAdvertAddress_Type.__name__ = "Integer32"
_HpicfRdiscIfAdvertAddress_Object = MibTableColumn
hpicfRdiscIfAdvertAddress = _HpicfRdiscIfAdvertAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 2),
    _HpicfRdiscIfAdvertAddress_Type()
)
hpicfRdiscIfAdvertAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfAdvertAddress.setStatus("current")


class _HpicfRdiscIfMaxAdvertInterval_Type(Integer32):
    """Custom type hpicfRdiscIfMaxAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1800),
    )


_HpicfRdiscIfMaxAdvertInterval_Type.__name__ = "Integer32"
_HpicfRdiscIfMaxAdvertInterval_Object = MibTableColumn
hpicfRdiscIfMaxAdvertInterval = _HpicfRdiscIfMaxAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 3),
    _HpicfRdiscIfMaxAdvertInterval_Type()
)
hpicfRdiscIfMaxAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfMaxAdvertInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRdiscIfMaxAdvertInterval.setUnits("seconds")


class _HpicfRdiscIfMinAdvertInterval_Type(Integer32):
    """Custom type hpicfRdiscIfMinAdvertInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1800),
    )


_HpicfRdiscIfMinAdvertInterval_Type.__name__ = "Integer32"
_HpicfRdiscIfMinAdvertInterval_Object = MibTableColumn
hpicfRdiscIfMinAdvertInterval = _HpicfRdiscIfMinAdvertInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 4),
    _HpicfRdiscIfMinAdvertInterval_Type()
)
hpicfRdiscIfMinAdvertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfMinAdvertInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRdiscIfMinAdvertInterval.setUnits("seconds")


class _HpicfRdiscIfAdvertLifetime_Type(Integer32):
    """Custom type hpicfRdiscIfAdvertLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 9000),
    )


_HpicfRdiscIfAdvertLifetime_Type.__name__ = "Integer32"
_HpicfRdiscIfAdvertLifetime_Object = MibTableColumn
hpicfRdiscIfAdvertLifetime = _HpicfRdiscIfAdvertLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 5),
    _HpicfRdiscIfAdvertLifetime_Type()
)
hpicfRdiscIfAdvertLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfAdvertLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfRdiscIfAdvertLifetime.setUnits("seconds")
_HpicfRdiscIfPreference_Type = Integer32
_HpicfRdiscIfPreference_Object = MibTableColumn
hpicfRdiscIfPreference = _HpicfRdiscIfPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 1, 2, 1, 6),
    _HpicfRdiscIfPreference_Type()
)
hpicfRdiscIfPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfRdiscIfPreference.setStatus("current")
_HpicfIcmpRateLimits_ObjectIdentity = ObjectIdentity
hpicfIcmpRateLimits = _HpicfIcmpRateLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2)
)
_HpicfIcmpBoxLimits_ObjectIdentity = ObjectIdentity
hpicfIcmpBoxLimits = _HpicfIcmpBoxLimits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1)
)


class _HpicfIcmpReplyLimitEnable_Type(Integer32):
    """Custom type hpicfIcmpReplyLimitEnable based on Integer32"""
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


_HpicfIcmpReplyLimitEnable_Type.__name__ = "Integer32"
_HpicfIcmpReplyLimitEnable_Object = MibScalar
hpicfIcmpReplyLimitEnable = _HpicfIcmpReplyLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 1),
    _HpicfIcmpReplyLimitEnable_Type()
)
hpicfIcmpReplyLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpReplyLimitEnable.setStatus("current")


class _HpicfIcmpReplyLimit_Type(Integer32):
    """Custom type hpicfIcmpReplyLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HpicfIcmpReplyLimit_Type.__name__ = "Integer32"
_HpicfIcmpReplyLimit_Object = MibScalar
hpicfIcmpReplyLimit = _HpicfIcmpReplyLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 2),
    _HpicfIcmpReplyLimit_Type()
)
hpicfIcmpReplyLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpReplyLimit.setStatus("current")


class _HpicfIcmpRedirectEnable_Type(Integer32):
    """Custom type hpicfIcmpRedirectEnable based on Integer32"""
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


_HpicfIcmpRedirectEnable_Type.__name__ = "Integer32"
_HpicfIcmpRedirectEnable_Object = MibScalar
hpicfIcmpRedirectEnable = _HpicfIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 3),
    _HpicfIcmpRedirectEnable_Type()
)
hpicfIcmpRedirectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpRedirectEnable.setStatus("current")


class _HpicfIcmpDestUnreachEnable_Type(Integer32):
    """Custom type hpicfIcmpDestUnreachEnable based on Integer32"""
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


_HpicfIcmpDestUnreachEnable_Type.__name__ = "Integer32"
_HpicfIcmpDestUnreachEnable_Object = MibScalar
hpicfIcmpDestUnreachEnable = _HpicfIcmpDestUnreachEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 4),
    _HpicfIcmpDestUnreachEnable_Type()
)
hpicfIcmpDestUnreachEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpDestUnreachEnable.setStatus("current")


class _HpicfIcmpAddrMaskReplyEnable_Type(Integer32):
    """Custom type hpicfIcmpAddrMaskReplyEnable based on Integer32"""
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


_HpicfIcmpAddrMaskReplyEnable_Type.__name__ = "Integer32"
_HpicfIcmpAddrMaskReplyEnable_Object = MibScalar
hpicfIcmpAddrMaskReplyEnable = _HpicfIcmpAddrMaskReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 5),
    _HpicfIcmpAddrMaskReplyEnable_Type()
)
hpicfIcmpAddrMaskReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpAddrMaskReplyEnable.setStatus("current")


class _HpicfIcmpEchoBroadcastReplyEnable_Type(Integer32):
    """Custom type hpicfIcmpEchoBroadcastReplyEnable based on Integer32"""
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


_HpicfIcmpEchoBroadcastReplyEnable_Type.__name__ = "Integer32"
_HpicfIcmpEchoBroadcastReplyEnable_Object = MibScalar
hpicfIcmpEchoBroadcastReplyEnable = _HpicfIcmpEchoBroadcastReplyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 2, 1, 6),
    _HpicfIcmpEchoBroadcastReplyEnable_Type()
)
hpicfIcmpEchoBroadcastReplyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIcmpEchoBroadcastReplyEnable.setStatus("current")
_HpicfGlobalIpConfig_ObjectIdentity = ObjectIdentity
hpicfGlobalIpConfig = _HpicfGlobalIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 3)
)


class _HpicfDBroadcastFwdEnable_Type(Integer32):
    """Custom type hpicfDBroadcastFwdEnable based on Integer32"""
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


_HpicfDBroadcastFwdEnable_Type.__name__ = "Integer32"
_HpicfDBroadcastFwdEnable_Object = MibScalar
hpicfDBroadcastFwdEnable = _HpicfDBroadcastFwdEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 3, 1),
    _HpicfDBroadcastFwdEnable_Type()
)
hpicfDBroadcastFwdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDBroadcastFwdEnable.setStatus("current")


class _HpicfSourceRouteEnable_Type(Integer32):
    """Custom type hpicfSourceRouteEnable based on Integer32"""
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


_HpicfSourceRouteEnable_Type.__name__ = "Integer32"
_HpicfSourceRouteEnable_Object = MibScalar
hpicfSourceRouteEnable = _HpicfSourceRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 3, 2),
    _HpicfSourceRouteEnable_Type()
)
hpicfSourceRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSourceRouteEnable.setStatus("current")
_HpicfIpMaximumPaths_Type = Integer32
_HpicfIpMaximumPaths_Object = MibScalar
hpicfIpMaximumPaths = _HpicfIpMaximumPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 3, 3),
    _HpicfIpMaximumPaths_Type()
)
hpicfIpMaximumPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpMaximumPaths.setStatus("current")


class _HpicfDBroadcastFwdAcl_Type(SnmpAdminString):
    """Custom type hpicfDBroadcastFwdAcl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDBroadcastFwdAcl_Type.__name__ = "SnmpAdminString"
_HpicfDBroadcastFwdAcl_Object = MibScalar
hpicfDBroadcastFwdAcl = _HpicfDBroadcastFwdAcl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 3, 4),
    _HpicfDBroadcastFwdAcl_Type()
)
hpicfDBroadcastFwdAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDBroadcastFwdAcl.setStatus("current")
_HpicfIpStaticRouteConfig_ObjectIdentity = ObjectIdentity
hpicfIpStaticRouteConfig = _HpicfIpStaticRouteConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4)
)
_HpicfIpStaticRouteTable_Object = MibTable
hpicfIpStaticRouteTable = _HpicfIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteTable.setStatus("current")
_HpicfIpStaticRouteEntry_Object = MibTableRow
hpicfIpStaticRouteEntry = _HpicfIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1)
)
hpicfIpStaticRouteEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefixType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefix"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefixLength"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdAddrType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdAddr"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteEntry.setStatus("current")
_HpicfIpStaticRoutePrefixType_Type = InetAddressType
_HpicfIpStaticRoutePrefixType_Object = MibTableColumn
hpicfIpStaticRoutePrefixType = _HpicfIpStaticRoutePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 1),
    _HpicfIpStaticRoutePrefixType_Type()
)
hpicfIpStaticRoutePrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRoutePrefixType.setStatus("current")


class _HpicfIpStaticRoutePrefix_Type(InetAddress):
    """Custom type hpicfIpStaticRoutePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_HpicfIpStaticRoutePrefix_Type.__name__ = "InetAddress"
_HpicfIpStaticRoutePrefix_Object = MibTableColumn
hpicfIpStaticRoutePrefix = _HpicfIpStaticRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 2),
    _HpicfIpStaticRoutePrefix_Type()
)
hpicfIpStaticRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRoutePrefix.setStatus("current")
_HpicfIpStaticRoutePrefixLength_Type = InetAddressPrefixLength
_HpicfIpStaticRoutePrefixLength_Object = MibTableColumn
hpicfIpStaticRoutePrefixLength = _HpicfIpStaticRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 3),
    _HpicfIpStaticRoutePrefixLength_Type()
)
hpicfIpStaticRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRoutePrefixLength.setStatus("current")
_HpicfIpStaticRouteFwdAddrType_Type = InetAddressType
_HpicfIpStaticRouteFwdAddrType_Object = MibTableColumn
hpicfIpStaticRouteFwdAddrType = _HpicfIpStaticRouteFwdAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 4),
    _HpicfIpStaticRouteFwdAddrType_Type()
)
hpicfIpStaticRouteFwdAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteFwdAddrType.setStatus("current")


class _HpicfIpStaticRouteFwdAddr_Type(InetAddress):
    """Custom type hpicfIpStaticRouteFwdAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_HpicfIpStaticRouteFwdAddr_Type.__name__ = "InetAddress"
_HpicfIpStaticRouteFwdAddr_Object = MibTableColumn
hpicfIpStaticRouteFwdAddr = _HpicfIpStaticRouteFwdAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 5),
    _HpicfIpStaticRouteFwdAddr_Type()
)
hpicfIpStaticRouteFwdAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteFwdAddr.setStatus("current")
_HpicfIpStaticRouteFwdIfIndex_Type = InterfaceIndexOrZero
_HpicfIpStaticRouteFwdIfIndex_Object = MibTableColumn
hpicfIpStaticRouteFwdIfIndex = _HpicfIpStaticRouteFwdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 6),
    _HpicfIpStaticRouteFwdIfIndex_Type()
)
hpicfIpStaticRouteFwdIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteFwdIfIndex.setStatus("current")


class _HpicfIpStaticRouteType_Type(Integer32):
    """Custom type hpicfIpStaticRouteType based on Integer32"""
    defaultValue = 4

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


_HpicfIpStaticRouteType_Type.__name__ = "Integer32"
_HpicfIpStaticRouteType_Object = MibTableColumn
hpicfIpStaticRouteType = _HpicfIpStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 7),
    _HpicfIpStaticRouteType_Type()
)
hpicfIpStaticRouteType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteType.setStatus("current")


class _HpicfIpStaticRouteDistance_Type(Integer32):
    """Custom type hpicfIpStaticRouteDistance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfIpStaticRouteDistance_Type.__name__ = "Integer32"
_HpicfIpStaticRouteDistance_Object = MibTableColumn
hpicfIpStaticRouteDistance = _HpicfIpStaticRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 8),
    _HpicfIpStaticRouteDistance_Type()
)
hpicfIpStaticRouteDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteDistance.setStatus("current")


class _HpicfIpStaticRouteTag_Type(Unsigned32):
    """Custom type hpicfIpStaticRouteTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpicfIpStaticRouteTag_Type.__name__ = "Unsigned32"
_HpicfIpStaticRouteTag_Object = MibTableColumn
hpicfIpStaticRouteTag = _HpicfIpStaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 9),
    _HpicfIpStaticRouteTag_Type()
)
hpicfIpStaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteTag.setStatus("current")
_HpicfIpStaticRouteStatus_Type = RowStatus
_HpicfIpStaticRouteStatus_Object = MibTableColumn
hpicfIpStaticRouteStatus = _HpicfIpStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 10),
    _HpicfIpStaticRouteStatus_Type()
)
hpicfIpStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteStatus.setStatus("current")


class _HpicfIpStaticRouteMetric_Type(Metric):
    """Custom type hpicfIpStaticRouteMetric based on Metric"""
    defaultValue = 1


_HpicfIpStaticRouteMetric_Object = MibTableColumn
hpicfIpStaticRouteMetric = _HpicfIpStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 11),
    _HpicfIpStaticRouteMetric_Type()
)
hpicfIpStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteMetric.setStatus("current")
_HpicfIpStaticRouteName_Type = DisplayString
_HpicfIpStaticRouteName_Object = MibTableColumn
hpicfIpStaticRouteName = _HpicfIpStaticRouteName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 12),
    _HpicfIpStaticRouteName_Type()
)
hpicfIpStaticRouteName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteName.setStatus("current")


class _HpicfIpStaticRouteLogging_Type(Integer32):
    """Custom type hpicfIpStaticRouteLogging based on Integer32"""
    defaultValue = 2

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


_HpicfIpStaticRouteLogging_Type.__name__ = "Integer32"
_HpicfIpStaticRouteLogging_Object = MibTableColumn
hpicfIpStaticRouteLogging = _HpicfIpStaticRouteLogging_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 13),
    _HpicfIpStaticRouteLogging_Type()
)
hpicfIpStaticRouteLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteLogging.setStatus("current")


class _HpicfIpStaticRouteBfdEnable_Type(TruthValue):
    """Custom type hpicfIpStaticRouteBfdEnable based on TruthValue"""


_HpicfIpStaticRouteBfdEnable_Object = MibTableColumn
hpicfIpStaticRouteBfdEnable = _HpicfIpStaticRouteBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 1, 1, 14),
    _HpicfIpStaticRouteBfdEnable_Type()
)
hpicfIpStaticRouteBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdEnable.setStatus("current")
_HpicfIpStaticNeighborTable_Object = MibTable
hpicfIpStaticNeighborTable = _HpicfIpStaticNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborTable.setStatus("current")
_HpicfIpStaticNeighborEntry_Object = MibTableRow
hpicfIpStaticNeighborEntry = _HpicfIpStaticNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1)
)
hpicfIpStaticNeighborEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticNeighborIfIndex"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticNeighborNetAddrType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticNeighborNetAddress"),
)
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborEntry.setStatus("current")
_HpicfIpStaticNeighborIfIndex_Type = InterfaceIndex
_HpicfIpStaticNeighborIfIndex_Object = MibTableColumn
hpicfIpStaticNeighborIfIndex = _HpicfIpStaticNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1, 1),
    _HpicfIpStaticNeighborIfIndex_Type()
)
hpicfIpStaticNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborIfIndex.setStatus("current")
_HpicfIpStaticNeighborNetAddrType_Type = InetAddressType
_HpicfIpStaticNeighborNetAddrType_Object = MibTableColumn
hpicfIpStaticNeighborNetAddrType = _HpicfIpStaticNeighborNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1, 2),
    _HpicfIpStaticNeighborNetAddrType_Type()
)
hpicfIpStaticNeighborNetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborNetAddrType.setStatus("current")
_HpicfIpStaticNeighborNetAddress_Type = InetAddress
_HpicfIpStaticNeighborNetAddress_Object = MibTableColumn
hpicfIpStaticNeighborNetAddress = _HpicfIpStaticNeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1, 3),
    _HpicfIpStaticNeighborNetAddress_Type()
)
hpicfIpStaticNeighborNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborNetAddress.setStatus("current")
_HpicfIpStaticNeighborPhysAddress_Type = PhysAddress
_HpicfIpStaticNeighborPhysAddress_Object = MibTableColumn
hpicfIpStaticNeighborPhysAddress = _HpicfIpStaticNeighborPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1, 4),
    _HpicfIpStaticNeighborPhysAddress_Type()
)
hpicfIpStaticNeighborPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborPhysAddress.setStatus("current")
_HpicfIpStaticNeighborStatus_Type = RowStatus
_HpicfIpStaticNeighborStatus_Object = MibTableColumn
hpicfIpStaticNeighborStatus = _HpicfIpStaticNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 2, 1, 5),
    _HpicfIpStaticNeighborStatus_Type()
)
hpicfIpStaticNeighborStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborStatus.setStatus("current")
_HpicfIpStaticRouteBfdTable_Object = MibTable
hpicfIpStaticRouteBfdTable = _HpicfIpStaticRouteBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdTable.setStatus("current")
_HpicfIpStaticRouteBfdEntry_Object = MibTableRow
hpicfIpStaticRouteBfdEntry = _HpicfIpStaticRouteBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1)
)
hpicfIpStaticRouteBfdEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefixType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefix"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRoutePrefixLength"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdAddrType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdAddr"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpStaticRouteFwdIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdEntry.setStatus("current")
_HpicfIpStaticRouteBfdSrcAddrType_Type = InetAddressType
_HpicfIpStaticRouteBfdSrcAddrType_Object = MibTableColumn
hpicfIpStaticRouteBfdSrcAddrType = _HpicfIpStaticRouteBfdSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1, 1),
    _HpicfIpStaticRouteBfdSrcAddrType_Type()
)
hpicfIpStaticRouteBfdSrcAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdSrcAddrType.setStatus("current")
_HpicfIpStaticRouteBfdSrcAddr_Type = InetAddress
_HpicfIpStaticRouteBfdSrcAddr_Object = MibTableColumn
hpicfIpStaticRouteBfdSrcAddr = _HpicfIpStaticRouteBfdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1, 2),
    _HpicfIpStaticRouteBfdSrcAddr_Type()
)
hpicfIpStaticRouteBfdSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdSrcAddr.setStatus("current")
_HpicfIpStaticRouteBfdDstAddrType_Type = InetAddressType
_HpicfIpStaticRouteBfdDstAddrType_Object = MibTableColumn
hpicfIpStaticRouteBfdDstAddrType = _HpicfIpStaticRouteBfdDstAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1, 3),
    _HpicfIpStaticRouteBfdDstAddrType_Type()
)
hpicfIpStaticRouteBfdDstAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdDstAddrType.setStatus("current")
_HpicfIpStaticRouteBfdDstAddr_Type = InetAddress
_HpicfIpStaticRouteBfdDstAddr_Object = MibTableColumn
hpicfIpStaticRouteBfdDstAddr = _HpicfIpStaticRouteBfdDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1, 4),
    _HpicfIpStaticRouteBfdDstAddr_Type()
)
hpicfIpStaticRouteBfdDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdDstAddr.setStatus("current")
_HpicfIpStaticRouteBfdStatus_Type = RowStatus
_HpicfIpStaticRouteBfdStatus_Object = MibTableColumn
hpicfIpStaticRouteBfdStatus = _HpicfIpStaticRouteBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 4, 3, 1, 5),
    _HpicfIpStaticRouteBfdStatus_Type()
)
hpicfIpStaticRouteBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdStatus.setStatus("current")
_HpicfIpRouteStats_ObjectIdentity = ObjectIdentity
hpicfIpRouteStats = _HpicfIpRouteStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5)
)
_HpicfIpCidrRouteTable_Object = MibTable
hpicfIpCidrRouteTable = _HpicfIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hpicfIpCidrRouteTable.setStatus("current")
_HpicfIpCidrRouteEntry_Object = MibTableRow
hpicfIpCidrRouteEntry = _HpicfIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpCidrRouteEntry.setStatus("current")


class _HpicfIpCidrRouteDistance_Type(Integer32):
    """Custom type hpicfIpCidrRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfIpCidrRouteDistance_Type.__name__ = "Integer32"
_HpicfIpCidrRouteDistance_Object = MibTableColumn
hpicfIpCidrRouteDistance = _HpicfIpCidrRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 1, 1, 1),
    _HpicfIpCidrRouteDistance_Type()
)
hpicfIpCidrRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpCidrRouteDistance.setStatus("current")
_HpicfInetCidrRouteTable_Object = MibTable
hpicfInetCidrRouteTable = _HpicfInetCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteTable.setStatus("current")
_HpicfInetCidrRouteEntry_Object = MibTableRow
hpicfInetCidrRouteEntry = _HpicfInetCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteEntry.setStatus("current")


class _HpicfInetCidrRouteDistance_Type(Integer32):
    """Custom type hpicfInetCidrRouteDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfInetCidrRouteDistance_Type.__name__ = "Integer32"
_HpicfInetCidrRouteDistance_Object = MibTableColumn
hpicfInetCidrRouteDistance = _HpicfInetCidrRouteDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 2, 1, 1),
    _HpicfInetCidrRouteDistance_Type()
)
hpicfInetCidrRouteDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInetCidrRouteDistance.setStatus("current")
_HpicfInetCidrRouteInfo_Type = ObjectIdentifier
_HpicfInetCidrRouteInfo_Object = MibTableColumn
hpicfInetCidrRouteInfo = _HpicfInetCidrRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 2, 1, 2),
    _HpicfInetCidrRouteInfo_Type()
)
hpicfInetCidrRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInetCidrRouteInfo.setStatus("current")
_HpicfInetCidrRouteState_Type = HpInetCidrRouteState
_HpicfInetCidrRouteState_Object = MibTableColumn
hpicfInetCidrRouteState = _HpicfInetCidrRouteState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 2, 1, 3),
    _HpicfInetCidrRouteState_Type()
)
hpicfInetCidrRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInetCidrRouteState.setStatus("current")
_HpicfInetCidrRouteStatsTable_Object = MibTable
hpicfInetCidrRouteStatsTable = _HpicfInetCidrRouteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteStatsTable.setStatus("current")
_HpicfInetCidrRouteStatsEntry_Object = MibTableRow
hpicfInetCidrRouteStatsEntry = _HpicfInetCidrRouteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 3, 1)
)
hpicfInetCidrRouteStatsEntry.setIndexNames(
    (0, "IP-FORWARD-MIB", "inetCidrRouteDestType"),
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteStatsEntry.setStatus("current")
_HpicfInetCidrNumRouteDestinations_Type = Counter32
_HpicfInetCidrNumRouteDestinations_Object = MibTableColumn
hpicfInetCidrNumRouteDestinations = _HpicfInetCidrNumRouteDestinations_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 3, 1, 1),
    _HpicfInetCidrNumRouteDestinations_Type()
)
hpicfInetCidrNumRouteDestinations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInetCidrNumRouteDestinations.setStatus("current")
_HpicfInetCidrNumRouteRoutes_Type = Counter32
_HpicfInetCidrNumRouteRoutes_Object = MibTableColumn
hpicfInetCidrNumRouteRoutes = _HpicfInetCidrNumRouteRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 5, 3, 1, 2),
    _HpicfInetCidrNumRouteRoutes_Type()
)
hpicfInetCidrNumRouteRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfInetCidrNumRouteRoutes.setStatus("current")
_HpicfArpInfo_ObjectIdentity = ObjectIdentity
hpicfArpInfo = _HpicfArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 6)
)


class _HpicfArpAgingTime_Type(Integer32):
    """Custom type hpicfArpAgingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16666666),
    )


_HpicfArpAgingTime_Type.__name__ = "Integer32"
_HpicfArpAgingTime_Object = MibScalar
hpicfArpAgingTime = _HpicfArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 6, 1),
    _HpicfArpAgingTime_Type()
)
hpicfArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpAgingTime.setStatus("current")


class _HpicfArpMcastReplies_Type(Integer32):
    """Custom type hpicfArpMcastReplies based on Integer32"""
    defaultValue = 2

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


_HpicfArpMcastReplies_Type.__name__ = "Integer32"
_HpicfArpMcastReplies_Object = MibScalar
hpicfArpMcastReplies = _HpicfArpMcastReplies_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 6, 2),
    _HpicfArpMcastReplies_Type()
)
hpicfArpMcastReplies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpMcastReplies.setStatus("current")
_HpicfIpDefaultRouterPrefixInfo_ObjectIdentity = ObjectIdentity
hpicfIpDefaultRouterPrefixInfo = _HpicfIpDefaultRouterPrefixInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7)
)
_HpicfIpDefaultRouterPrefixTable_Object = MibTable
hpicfIpDefaultRouterPrefixTable = _HpicfIpDefaultRouterPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixTable.setStatus("current")
_HpicfIpDefaultRouterPrefixEntry_Object = MibTableRow
hpicfIpDefaultRouterPrefixEntry = _HpicfIpDefaultRouterPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1)
)
hpicfIpDefaultRouterPrefixEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterAddressType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterAddress"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterIfIndex"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefix"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixLength"),
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixEntry.setStatus("current")
_HpicfIpDefaultRouterAddressType_Type = InetAddressType
_HpicfIpDefaultRouterAddressType_Object = MibTableColumn
hpicfIpDefaultRouterAddressType = _HpicfIpDefaultRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 1),
    _HpicfIpDefaultRouterAddressType_Type()
)
hpicfIpDefaultRouterAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterAddressType.setStatus("current")
_HpicfIpDefaultRouterAddress_Type = InetAddress
_HpicfIpDefaultRouterAddress_Object = MibTableColumn
hpicfIpDefaultRouterAddress = _HpicfIpDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 2),
    _HpicfIpDefaultRouterAddress_Type()
)
hpicfIpDefaultRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterAddress.setStatus("current")
_HpicfIpDefaultRouterIfIndex_Type = InterfaceIndex
_HpicfIpDefaultRouterIfIndex_Object = MibTableColumn
hpicfIpDefaultRouterIfIndex = _HpicfIpDefaultRouterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 3),
    _HpicfIpDefaultRouterIfIndex_Type()
)
hpicfIpDefaultRouterIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterIfIndex.setStatus("current")
_HpicfIpDefaultRouterPrefixType_Type = InetAddressType
_HpicfIpDefaultRouterPrefixType_Object = MibTableColumn
hpicfIpDefaultRouterPrefixType = _HpicfIpDefaultRouterPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 4),
    _HpicfIpDefaultRouterPrefixType_Type()
)
hpicfIpDefaultRouterPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixType.setStatus("current")
_HpicfIpDefaultRouterPrefix_Type = InetAddress
_HpicfIpDefaultRouterPrefix_Object = MibTableColumn
hpicfIpDefaultRouterPrefix = _HpicfIpDefaultRouterPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 5),
    _HpicfIpDefaultRouterPrefix_Type()
)
hpicfIpDefaultRouterPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefix.setStatus("current")
_HpicfIpDefaultRouterPrefixLength_Type = InetAddressPrefixLength
_HpicfIpDefaultRouterPrefixLength_Object = MibTableColumn
hpicfIpDefaultRouterPrefixLength = _HpicfIpDefaultRouterPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 6),
    _HpicfIpDefaultRouterPrefixLength_Type()
)
hpicfIpDefaultRouterPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixLength.setStatus("current")
_HpicfIpDefaultRouterPrefixOnLink_Type = TruthValue
_HpicfIpDefaultRouterPrefixOnLink_Object = MibTableColumn
hpicfIpDefaultRouterPrefixOnLink = _HpicfIpDefaultRouterPrefixOnLink_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 7),
    _HpicfIpDefaultRouterPrefixOnLink_Type()
)
hpicfIpDefaultRouterPrefixOnLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixOnLink.setStatus("current")
_HpicfIpDefaultRouterPrefixAutonomous_Type = TruthValue
_HpicfIpDefaultRouterPrefixAutonomous_Object = MibTableColumn
hpicfIpDefaultRouterPrefixAutonomous = _HpicfIpDefaultRouterPrefixAutonomous_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 8),
    _HpicfIpDefaultRouterPrefixAutonomous_Type()
)
hpicfIpDefaultRouterPrefixAutonomous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixAutonomous.setStatus("current")
_HpicfIpDefaultRouterPrefixValidLifeTime_Type = Unsigned32
_HpicfIpDefaultRouterPrefixValidLifeTime_Object = MibTableColumn
hpicfIpDefaultRouterPrefixValidLifeTime = _HpicfIpDefaultRouterPrefixValidLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 9),
    _HpicfIpDefaultRouterPrefixValidLifeTime_Type()
)
hpicfIpDefaultRouterPrefixValidLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixValidLifeTime.setStatus("current")
_HpicfIpDefaultRouterPrefixPrefdLifeTime_Type = Unsigned32
_HpicfIpDefaultRouterPrefixPrefdLifeTime_Object = MibTableColumn
hpicfIpDefaultRouterPrefixPrefdLifeTime = _HpicfIpDefaultRouterPrefixPrefdLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 7, 1, 1, 10),
    _HpicfIpDefaultRouterPrefixPrefdLifeTime_Type()
)
hpicfIpDefaultRouterPrefixPrefdLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterPrefixPrefdLifeTime.setStatus("current")
_HpicfIpDefaultRouterProperties_ObjectIdentity = ObjectIdentity
hpicfIpDefaultRouterProperties = _HpicfIpDefaultRouterProperties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 8)
)
_HpicfIpDefaultRouterTable_Object = MibTable
hpicfIpDefaultRouterTable = _HpicfIpDefaultRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterTable.setStatus("current")
_HpicfIpDefaultRouterEntry_Object = MibTableRow
hpicfIpDefaultRouterEntry = _HpicfIpDefaultRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterEntry.setStatus("current")
_HpicfIpDefaultRouterMTU_Type = Integer32
_HpicfIpDefaultRouterMTU_Object = MibTableColumn
hpicfIpDefaultRouterMTU = _HpicfIpDefaultRouterMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 8, 1, 1, 1),
    _HpicfIpDefaultRouterMTU_Type()
)
hpicfIpDefaultRouterMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterMTU.setStatus("current")
_HpicfIpDefaultRouterHopLimit_Type = Integer32
_HpicfIpDefaultRouterHopLimit_Object = MibTableColumn
hpicfIpDefaultRouterHopLimit = _HpicfIpDefaultRouterHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 8, 1, 1, 2),
    _HpicfIpDefaultRouterHopLimit_Type()
)
hpicfIpDefaultRouterHopLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterHopLimit.setStatus("current")
_HpicfIpv6ND_ObjectIdentity = ObjectIdentity
hpicfIpv6ND = _HpicfIpv6ND_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9)
)
_HpicfIpv6NDRAAdminStatus_Type = TruthValue
_HpicfIpv6NDRAAdminStatus_Object = MibScalar
hpicfIpv6NDRAAdminStatus = _HpicfIpv6NDRAAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 1),
    _HpicfIpv6NDRAAdminStatus_Type()
)
hpicfIpv6NDRAAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6NDRAAdminStatus.setStatus("current")
_HpicfIpv6RtrAdvPrefixTable_Object = MibTable
hpicfIpv6RtrAdvPrefixTable = _HpicfIpv6RtrAdvPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixTable.setStatus("current")
_HpicfIpv6RtrAdvPrefixEntry_Object = MibTableRow
hpicfIpv6RtrAdvPrefixEntry = _HpicfIpv6RtrAdvPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1)
)
hpicfIpv6RtrAdvPrefixEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixIfIndex"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixType"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixPrefix"),
    (0, "HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixLength"),
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixEntry.setStatus("current")
_HpicfIpv6RtrAdvPrefixIfIndex_Type = InterfaceIndex
_HpicfIpv6RtrAdvPrefixIfIndex_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixIfIndex = _HpicfIpv6RtrAdvPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 1),
    _HpicfIpv6RtrAdvPrefixIfIndex_Type()
)
hpicfIpv6RtrAdvPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixIfIndex.setStatus("current")
_HpicfIpv6RtrAdvPrefixType_Type = InetAddressType
_HpicfIpv6RtrAdvPrefixType_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixType = _HpicfIpv6RtrAdvPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 2),
    _HpicfIpv6RtrAdvPrefixType_Type()
)
hpicfIpv6RtrAdvPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixType.setStatus("current")
_HpicfIpv6RtrAdvPrefixPrefix_Type = InetAddress
_HpicfIpv6RtrAdvPrefixPrefix_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixPrefix = _HpicfIpv6RtrAdvPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 3),
    _HpicfIpv6RtrAdvPrefixPrefix_Type()
)
hpicfIpv6RtrAdvPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixPrefix.setStatus("current")
_HpicfIpv6RtrAdvPrefixLength_Type = InetAddressPrefixLength
_HpicfIpv6RtrAdvPrefixLength_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixLength = _HpicfIpv6RtrAdvPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 4),
    _HpicfIpv6RtrAdvPrefixLength_Type()
)
hpicfIpv6RtrAdvPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixLength.setStatus("current")


class _HpicfIpv6RtrAdvPrefixOnLinkFlag_Type(TruthValue):
    """Custom type hpicfIpv6RtrAdvPrefixOnLinkFlag based on TruthValue"""


_HpicfIpv6RtrAdvPrefixOnLinkFlag_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixOnLinkFlag = _HpicfIpv6RtrAdvPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 5),
    _HpicfIpv6RtrAdvPrefixOnLinkFlag_Type()
)
hpicfIpv6RtrAdvPrefixOnLinkFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixOnLinkFlag.setStatus("current")


class _HpicfIpv6RtrAdvPrefixAutonomousFlag_Type(TruthValue):
    """Custom type hpicfIpv6RtrAdvPrefixAutonomousFlag based on TruthValue"""


_HpicfIpv6RtrAdvPrefixAutonomousFlag_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixAutonomousFlag = _HpicfIpv6RtrAdvPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 6),
    _HpicfIpv6RtrAdvPrefixAutonomousFlag_Type()
)
hpicfIpv6RtrAdvPrefixAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixAutonomousFlag.setStatus("current")


class _HpicfIpv6RtrAdvPrefixLifetimeType_Type(Integer32):
    """Custom type hpicfIpv6RtrAdvPrefixLifetimeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("realTime", 2))
    )


_HpicfIpv6RtrAdvPrefixLifetimeType_Type.__name__ = "Integer32"
_HpicfIpv6RtrAdvPrefixLifetimeType_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixLifetimeType = _HpicfIpv6RtrAdvPrefixLifetimeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 7),
    _HpicfIpv6RtrAdvPrefixLifetimeType_Type()
)
hpicfIpv6RtrAdvPrefixLifetimeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixLifetimeType.setStatus("current")


class _HpicfIpv6RtrAdvPrefixPreferredLifetime_Type(Unsigned32):
    """Custom type hpicfIpv6RtrAdvPrefixPreferredLifetime based on Unsigned32"""
    defaultValue = 604800


_HpicfIpv6RtrAdvPrefixPreferredLifetime_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixPreferredLifetime = _HpicfIpv6RtrAdvPrefixPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 8),
    _HpicfIpv6RtrAdvPrefixPreferredLifetime_Type()
)
hpicfIpv6RtrAdvPrefixPreferredLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixPreferredLifetime.setUnits("seconds")


class _HpicfIpv6RtrAdvPrefixValidLifetime_Type(Unsigned32):
    """Custom type hpicfIpv6RtrAdvPrefixValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_HpicfIpv6RtrAdvPrefixValidLifetime_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixValidLifetime = _HpicfIpv6RtrAdvPrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 9),
    _HpicfIpv6RtrAdvPrefixValidLifetime_Type()
)
hpicfIpv6RtrAdvPrefixValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixValidLifetime.setUnits("seconds")
_HpicfIpv6RtrAdvPrefixRowStatus_Type = RowStatus
_HpicfIpv6RtrAdvPrefixRowStatus_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixRowStatus = _HpicfIpv6RtrAdvPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 10),
    _HpicfIpv6RtrAdvPrefixRowStatus_Type()
)
hpicfIpv6RtrAdvPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixRowStatus.setStatus("current")


class _HpicfIpv6RtrAdvPrefixAdvertiseFlag_Type(TruthValue):
    """Custom type hpicfIpv6RtrAdvPrefixAdvertiseFlag based on TruthValue"""


_HpicfIpv6RtrAdvPrefixAdvertiseFlag_Object = MibTableColumn
hpicfIpv6RtrAdvPrefixAdvertiseFlag = _HpicfIpv6RtrAdvPrefixAdvertiseFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 2, 1, 11),
    _HpicfIpv6RtrAdvPrefixAdvertiseFlag_Type()
)
hpicfIpv6RtrAdvPrefixAdvertiseFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixAdvertiseFlag.setStatus("current")
_HpicfIpv6RtrAdvTable_Object = MibTable
hpicfIpv6RtrAdvTable = _HpicfIpv6RtrAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 3)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvTable.setStatus("current")
_HpicfIpv6RtrAdvEntry_Object = MibTableRow
hpicfIpv6RtrAdvEntry = _HpicfIpv6RtrAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvEntry.setStatus("current")


class _HpicfIpv6RtrAdvCurHopLimitMode_Type(Integer32):
    """Custom type hpicfIpv6RtrAdvCurHopLimitMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 1),
          ("perInterface", 2))
    )


_HpicfIpv6RtrAdvCurHopLimitMode_Type.__name__ = "Integer32"
_HpicfIpv6RtrAdvCurHopLimitMode_Object = MibTableColumn
hpicfIpv6RtrAdvCurHopLimitMode = _HpicfIpv6RtrAdvCurHopLimitMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 3, 1, 1),
    _HpicfIpv6RtrAdvCurHopLimitMode_Type()
)
hpicfIpv6RtrAdvCurHopLimitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvCurHopLimitMode.setStatus("current")


class _HpicfIpv6RouterAdvertSendDNSAdverts_Type(TruthValue):
    """Custom type hpicfIpv6RouterAdvertSendDNSAdverts based on TruthValue"""


_HpicfIpv6RouterAdvertSendDNSAdverts_Object = MibTableColumn
hpicfIpv6RouterAdvertSendDNSAdverts = _HpicfIpv6RouterAdvertSendDNSAdverts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 3, 1, 2),
    _HpicfIpv6RouterAdvertSendDNSAdverts_Type()
)
hpicfIpv6RouterAdvertSendDNSAdverts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6RouterAdvertSendDNSAdverts.setStatus("current")


class _HpicfIpv6RouterAdvertRtrPreference_Type(Integer32):
    """Custom type hpicfIpv6RouterAdvertRtrPreference based on Integer32"""
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


_HpicfIpv6RouterAdvertRtrPreference_Type.__name__ = "Integer32"
_HpicfIpv6RouterAdvertRtrPreference_Object = MibTableColumn
hpicfIpv6RouterAdvertRtrPreference = _HpicfIpv6RouterAdvertRtrPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 3, 1, 3),
    _HpicfIpv6RouterAdvertRtrPreference_Type()
)
hpicfIpv6RouterAdvertRtrPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6RouterAdvertRtrPreference.setStatus("current")


class _HpicfIpv6NDRADNSAdminStatus_Type(TruthValue):
    """Custom type hpicfIpv6NDRADNSAdminStatus based on TruthValue"""


_HpicfIpv6NDRADNSAdminStatus_Object = MibScalar
hpicfIpv6NDRADNSAdminStatus = _HpicfIpv6NDRADNSAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 9, 4),
    _HpicfIpv6NDRADNSAdminStatus_Type()
)
hpicfIpv6NDRADNSAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpv6NDRADNSAdminStatus.setStatus("current")
_HpicfIpRouteSummary_ObjectIdentity = ObjectIdentity
hpicfIpRouteSummary = _HpicfIpRouteSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 10)
)
_HpicfIpRouteSummaryTable_Object = MibTable
hpicfIpRouteSummaryTable = _HpicfIpRouteSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hpicfIpRouteSummaryTable.setStatus("current")
_HpicfIpRouteEntry_Object = MibTableRow
hpicfIpRouteEntry = _HpicfIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 10, 1, 1)
)
hpicfIpRouteEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpRouteProto"),
)
if mibBuilder.loadTexts:
    hpicfIpRouteEntry.setStatus("current")
_HpicfIpRouteProto_Type = HpicfIpRouteProtoName
_HpicfIpRouteProto_Object = MibTableColumn
hpicfIpRouteProto = _HpicfIpRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 10, 1, 1, 1),
    _HpicfIpRouteProto_Type()
)
hpicfIpRouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpRouteProto.setStatus("current")
_HpicfIpRouteCnt_Type = Unsigned32
_HpicfIpRouteCnt_Object = MibTableColumn
hpicfIpRouteCnt = _HpicfIpRouteCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 10, 1, 1, 2),
    _HpicfIpRouteCnt_Type()
)
hpicfIpRouteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpRouteCnt.setStatus("current")
_HpicfIpv6RouteSummary_ObjectIdentity = ObjectIdentity
hpicfIpv6RouteSummary = _HpicfIpv6RouteSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 11)
)
_HpicfIpv6RouteSummaryTable_Object = MibTable
hpicfIpv6RouteSummaryTable = _HpicfIpv6RouteSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hpicfIpv6RouteSummaryTable.setStatus("current")
_HpicfIpv6RouteEntry_Object = MibTableRow
hpicfIpv6RouteEntry = _HpicfIpv6RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 11, 1, 1)
)
hpicfIpv6RouteEntry.setIndexNames(
    (0, "HP-ICF-IP-ROUTING", "hpicfIpv6RouteProto"),
)
if mibBuilder.loadTexts:
    hpicfIpv6RouteEntry.setStatus("current")
_HpicfIpv6RouteProto_Type = HpicfIpv6RouteProtoName
_HpicfIpv6RouteProto_Object = MibTableColumn
hpicfIpv6RouteProto = _HpicfIpv6RouteProto_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 11, 1, 1, 1),
    _HpicfIpv6RouteProto_Type()
)
hpicfIpv6RouteProto.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpv6RouteProto.setStatus("current")
_HpicfIpv6RouteCnt_Type = Unsigned32
_HpicfIpv6RouteCnt_Object = MibTableColumn
hpicfIpv6RouteCnt = _HpicfIpv6RouteCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 1, 11, 1, 1, 2),
    _HpicfIpv6RouteCnt_Type()
)
hpicfIpv6RouteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpv6RouteCnt.setStatus("current")
_HpicfIpRoutingConformance_ObjectIdentity = ObjectIdentity
hpicfIpRoutingConformance = _HpicfIpRoutingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2)
)
_HpicfIpRoutingGroups_ObjectIdentity = ObjectIdentity
hpicfIpRoutingGroups = _HpicfIpRoutingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1)
)
_HpicfIpRoutingCompliances_ObjectIdentity = ObjectIdentity
hpicfIpRoutingCompliances = _HpicfIpRoutingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2)
)
_HpicfIpRouteBaseScalars_ObjectIdentity = ObjectIdentity
hpicfIpRouteBaseScalars = _HpicfIpRouteBaseScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 3)
)
_HpicfIpRouteCount_Type = Unsigned32
_HpicfIpRouteCount_Object = MibScalar
hpicfIpRouteCount = _HpicfIpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 3, 1),
    _HpicfIpRouteCount_Type()
)
hpicfIpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpRouteCount.setStatus("current")
_HpicfIpRouteNextHopCount_Type = Unsigned32
_HpicfIpRouteNextHopCount_Object = MibScalar
hpicfIpRouteNextHopCount = _HpicfIpRouteNextHopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 3, 2),
    _HpicfIpRouteNextHopCount_Type()
)
hpicfIpRouteNextHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpRouteNextHopCount.setStatus("current")
ipCidrRouteEntry.registerAugmentions(
    ("HP-ICF-IP-ROUTING",
     "hpicfIpCidrRouteEntry")
)
hpicfIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
inetCidrRouteEntry.registerAugmentions(
    ("HP-ICF-IP-ROUTING",
     "hpicfInetCidrRouteEntry")
)
hpicfInetCidrRouteEntry.setIndexNames(*inetCidrRouteEntry.getIndexNames())
ipDefaultRouterEntry.registerAugmentions(
    ("HP-ICF-IP-ROUTING",
     "hpicfIpDefaultRouterEntry")
)
hpicfIpDefaultRouterEntry.setIndexNames(*ipDefaultRouterEntry.getIndexNames())
ipv6RouterAdvertEntry.registerAugmentions(
    ("HP-ICF-IP-ROUTING",
     "hpicfIpv6RtrAdvEntry")
)
hpicfIpv6RtrAdvEntry.setIndexNames(*ipv6RouterAdvertEntry.getIndexNames())

# Managed Objects groups

hpicfRdiscBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 1)
)
hpicfRdiscBaseGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfRdiscAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfRdiscBaseGroup.setStatus("current")

hpicfRdiscIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 2)
)
hpicfRdiscIfCfgGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfRdiscIfAdminStatus"),
        ("HP-ICF-IP-ROUTING", "hpicfRdiscIfAdvertAddress"),
        ("HP-ICF-IP-ROUTING", "hpicfRdiscIfMaxAdvertInterval"),
        ("HP-ICF-IP-ROUTING", "hpicfRdiscIfMinAdvertInterval"),
        ("HP-ICF-IP-ROUTING", "hpicfRdiscIfAdvertLifetime"),
        ("HP-ICF-IP-ROUTING", "hpicfRdiscIfPreference"))
)
if mibBuilder.loadTexts:
    hpicfRdiscIfCfgGroup.setStatus("current")

hpicfIcmpReplyBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 3)
)
hpicfIcmpReplyBaseGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIcmpRedirectEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfIcmpDestUnreachEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfIcmpAddrMaskReplyEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfIcmpEchoBroadcastReplyEnable"))
)
if mibBuilder.loadTexts:
    hpicfIcmpReplyBaseGroup.setStatus("current")

hpicfIcmpReplyLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 4)
)
hpicfIcmpReplyLimitGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIcmpReplyLimitEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfIcmpReplyLimit"))
)
if mibBuilder.loadTexts:
    hpicfIcmpReplyLimitGroup.setStatus("current")

hpicfIpRouteCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 5)
)
hpicfIpRouteCfgGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfDBroadcastFwdEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfSourceRouteEnable"))
)
if mibBuilder.loadTexts:
    hpicfIpRouteCfgGroup.setStatus("current")

hpicfIpStaticRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 6)
)
hpicfIpStaticRouteGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteDistance"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteTag"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteLogging"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteGroup.setStatus("deprecated")

hpicfIpStaticNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 7)
)
hpicfIpStaticNeighborGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpStaticNeighborPhysAddress"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticNeighborStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpStaticNeighborGroup.setStatus("current")

hpicfIpCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 8)
)
hpicfIpCidrRouteGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpCidrRouteDistance")
)
if mibBuilder.loadTexts:
    hpicfIpCidrRouteGroup.setStatus("current")

hpicfInetCidrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 9)
)
hpicfInetCidrRouteGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfInetCidrRouteDistance"),
        ("HP-ICF-IP-ROUTING", "hpicfInetCidrRouteInfo"))
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteGroup.setStatus("current")

hpicfArpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 10)
)
hpicfArpBaseGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfArpAgingTime"),
        ("HP-ICF-IP-ROUTING", "hpicfArpMcastReplies"))
)
if mibBuilder.loadTexts:
    hpicfArpBaseGroup.setStatus("current")

hpicfIpv6RtrAdvPrefixGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 11)
)
hpicfIpv6RtrAdvPrefixGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixOnLinkFlag"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixAutonomousFlag"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixLifetimeType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixPreferredLifetime"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixValidLifetime"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixRowStatus"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvPrefixAdvertiseFlag"))
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixGroup.setStatus("current")

hpicfIpv6RtrAdvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 12)
)
hpicfIpv6RtrAdvGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvCurHopLimitMode")
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvGroup.setStatus("deprecated")

hpicfGlobalIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 13)
)
hpicfGlobalIpConfigGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfDBroadcastFwdEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfSourceRouteEnable"),
        ("HP-ICF-IP-ROUTING", "hpicfIpMaximumPaths"))
)
if mibBuilder.loadTexts:
    hpicfGlobalIpConfigGroup.setStatus("current")

hpicfIpDefaultRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 14)
)
hpicfIpDefaultRouterGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixOnLink"),
        ("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixAutonomous"),
        ("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixValidLifeTime"),
        ("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterPrefixPrefdLifeTime"),
        ("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterMTU"),
        ("HP-ICF-IP-ROUTING", "hpicfIpDefaultRouterHopLimit"))
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterGroup.setStatus("current")

hpicfIpv6NDRAAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 15)
)
hpicfIpv6NDRAAdminGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpv6NDRAAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfIpv6NDRAAdminGroup.setStatus("current")

hpicfIpRouteBaseScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 16)
)
hpicfIpRouteBaseScalarsGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpRouteCount"),
        ("HP-ICF-IP-ROUTING", "hpicfIpRouteNextHopCount"))
)
if mibBuilder.loadTexts:
    hpicfIpRouteBaseScalarsGroup.setStatus("current")

hpicfIpStaticRouteOtherGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 17)
)
hpicfIpStaticRouteOtherGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteMetric")
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteOtherGroup.setStatus("deprecated")

hpicfIpRouteSummaryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 18)
)
hpicfIpRouteSummaryTableGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpRouteCnt")
)
if mibBuilder.loadTexts:
    hpicfIpRouteSummaryTableGroup.setStatus("current")

hpicfInetCidrRouteGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 19)
)
hpicfInetCidrRouteGroup1.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfInetCidrRouteState")
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteGroup1.setStatus("current")

hpicfInetCidrRouteStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 20)
)
hpicfInetCidrRouteStatsGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfInetCidrNumRouteDestinations"),
        ("HP-ICF-IP-ROUTING", "hpicfInetCidrNumRouteRoutes"))
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteStatsGroup.setStatus("current")

hpicfIpv6RtrAdvDNSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 21)
)
hpicfIpv6RtrAdvDNSGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpv6RouterAdvertSendDNSAdverts")
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvDNSGroup.setStatus("current")

hpicfIpv6NDRADNSAdminGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 22)
)
hpicfIpv6NDRADNSAdminGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpv6NDRADNSAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfIpv6NDRADNSAdminGroup.setStatus("current")

hpicfIpStaticRouteNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 23)
)
hpicfIpStaticRouteNameGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteName")
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteNameGroup.setStatus("deprecated")

hpicfIpv6RouteSummaryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 24)
)
hpicfIpv6RouteSummaryTableGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpv6RouteProto"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RouteCnt"))
)
if mibBuilder.loadTexts:
    hpicfIpv6RouteSummaryTableGroup.setStatus("current")

hpicfDBroadcastFwdAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 25)
)
hpicfDBroadcastFwdAclGroup.setObjects(
    ("HP-ICF-IP-ROUTING", "hpicfDBroadcastFwdAcl")
)
if mibBuilder.loadTexts:
    hpicfDBroadcastFwdAclGroup.setStatus("current")

hpicfIpStaticRouteParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 26)
)
hpicfIpStaticRouteParamGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteDistance"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteTag"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteStatus"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteMetric"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteName"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteLogging"))
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteParamGroup.setStatus("deprecated")

hpicfIpv6RtrAdvParamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 27)
)
hpicfIpv6RtrAdvParamGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpv6RtrAdvCurHopLimitMode"),
        ("HP-ICF-IP-ROUTING", "hpicfIpv6RouterAdvertRtrPreference"))
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvParamGroup.setStatus("current")

hpicfIpStaticRouteParamGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 28)
)
hpicfIpStaticRouteParamGroup1.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteDistance"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteTag"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteStatus"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteMetric"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteName"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteLogging"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdEnable"))
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteParamGroup1.setStatus("current")

hpicfIpStaticRouteBfdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 1, 29)
)
hpicfIpStaticRouteBfdGroup.setObjects(
      *(("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdSrcAddrType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdSrcAddr"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdDstAddrType"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdDstAddr"),
        ("HP-ICF-IP-ROUTING", "hpicfIpStaticRouteBfdStatus"))
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteBfdGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfIcmpRdiscCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfIcmpRdiscCompliance.setStatus(
        "current"
    )

hpicfIcmpReplyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfIcmpReplyCompliance.setStatus(
        "current"
    )

hpicfIpRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfIpRouterCompliance.setStatus(
        "deprecated"
    )

hpicfArpInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfArpInfoCompliance.setStatus(
        "current"
    )

hpicfIpv6RtrAdvPrefixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvPrefixCompliance.setStatus(
        "current"
    )

hpicfIpv6RtrAdvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvCompliance.setStatus(
        "deprecated"
    )

hpicfGlobalIpConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfGlobalIpConfigCompliance.setStatus(
        "current"
    )

hpicfIpDefaultRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfIpDefaultRouterCompliance.setStatus(
        "current"
    )

hpicfIpv6NDRAAdminCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfIpv6NDRAAdminCompliance.setStatus(
        "current"
    )

hpicfIpRouteBaseScalarsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 10)
)
if mibBuilder.loadTexts:
    hpicfIpRouteBaseScalarsCompliance.setStatus(
        "current"
    )

hpicfInetCidrRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 11)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteCompliance.setStatus(
        "current"
    )

hpicfIpRouterOtherCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 12)
)
if mibBuilder.loadTexts:
    hpicfIpRouterOtherCompliance.setStatus(
        "deprecated"
    )

hpicfIpRouteSummaryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 13)
)
if mibBuilder.loadTexts:
    hpicfIpRouteSummaryCompliance.setStatus(
        "current"
    )

hpicfInetCidrRouteCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 14)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteCompliance1.setStatus(
        "current"
    )

hpicfInetCidrRouteStatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 15)
)
if mibBuilder.loadTexts:
    hpicfInetCidrRouteStatsCompliance.setStatus(
        "current"
    )

hpicfIpv6RtrAdvDNSCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 16)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvDNSCompliance.setStatus(
        "current"
    )

hpicfIpv6NDRADNSAdminCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 17)
)
if mibBuilder.loadTexts:
    hpicfIpv6NDRADNSAdminCompliance.setStatus(
        "current"
    )

hpicfIpStaticRouteNameCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 18)
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteNameCompliance.setStatus(
        "deprecated"
    )

hpicfIpv6RouteSummaryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 19)
)
if mibBuilder.loadTexts:
    hpicfIpv6RouteSummaryCompliance.setStatus(
        "current"
    )

hpicfIpDBroadcastFwdAclCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 20)
)
if mibBuilder.loadTexts:
    hpicfIpDBroadcastFwdAclCompliance.setStatus(
        "current"
    )

hpicfIpRouteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 21)
)
if mibBuilder.loadTexts:
    hpicfIpRouteCompliance.setStatus(
        "deprecated"
    )

hpicfIpv6RtrAdvParamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 22)
)
if mibBuilder.loadTexts:
    hpicfIpv6RtrAdvParamCompliance.setStatus(
        "current"
    )

hpicfIpStaticRouteCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 15, 2, 2, 23)
)
if mibBuilder.loadTexts:
    hpicfIpStaticRouteCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-IP-ROUTING",
    **{"HpicfIpRouteProtoName": HpicfIpRouteProtoName,
       "HpicfIpv6RouteProtoName": HpicfIpv6RouteProtoName,
       "hpicfIpRouting": hpicfIpRouting,
       "hpicfIpRoutingObjects": hpicfIpRoutingObjects,
       "hpicfIcmpRdisc": hpicfIcmpRdisc,
       "hpicfRdiscAdminStatus": hpicfRdiscAdminStatus,
       "hpicfRdiscIfCfgTable": hpicfRdiscIfCfgTable,
       "hpicfRdiscIfCfgEntry": hpicfRdiscIfCfgEntry,
       "hpicfRdiscIfAdminStatus": hpicfRdiscIfAdminStatus,
       "hpicfRdiscIfAdvertAddress": hpicfRdiscIfAdvertAddress,
       "hpicfRdiscIfMaxAdvertInterval": hpicfRdiscIfMaxAdvertInterval,
       "hpicfRdiscIfMinAdvertInterval": hpicfRdiscIfMinAdvertInterval,
       "hpicfRdiscIfAdvertLifetime": hpicfRdiscIfAdvertLifetime,
       "hpicfRdiscIfPreference": hpicfRdiscIfPreference,
       "hpicfIcmpRateLimits": hpicfIcmpRateLimits,
       "hpicfIcmpBoxLimits": hpicfIcmpBoxLimits,
       "hpicfIcmpReplyLimitEnable": hpicfIcmpReplyLimitEnable,
       "hpicfIcmpReplyLimit": hpicfIcmpReplyLimit,
       "hpicfIcmpRedirectEnable": hpicfIcmpRedirectEnable,
       "hpicfIcmpDestUnreachEnable": hpicfIcmpDestUnreachEnable,
       "hpicfIcmpAddrMaskReplyEnable": hpicfIcmpAddrMaskReplyEnable,
       "hpicfIcmpEchoBroadcastReplyEnable": hpicfIcmpEchoBroadcastReplyEnable,
       "hpicfGlobalIpConfig": hpicfGlobalIpConfig,
       "hpicfDBroadcastFwdEnable": hpicfDBroadcastFwdEnable,
       "hpicfSourceRouteEnable": hpicfSourceRouteEnable,
       "hpicfIpMaximumPaths": hpicfIpMaximumPaths,
       "hpicfDBroadcastFwdAcl": hpicfDBroadcastFwdAcl,
       "hpicfIpStaticRouteConfig": hpicfIpStaticRouteConfig,
       "hpicfIpStaticRouteTable": hpicfIpStaticRouteTable,
       "hpicfIpStaticRouteEntry": hpicfIpStaticRouteEntry,
       "hpicfIpStaticRoutePrefixType": hpicfIpStaticRoutePrefixType,
       "hpicfIpStaticRoutePrefix": hpicfIpStaticRoutePrefix,
       "hpicfIpStaticRoutePrefixLength": hpicfIpStaticRoutePrefixLength,
       "hpicfIpStaticRouteFwdAddrType": hpicfIpStaticRouteFwdAddrType,
       "hpicfIpStaticRouteFwdAddr": hpicfIpStaticRouteFwdAddr,
       "hpicfIpStaticRouteFwdIfIndex": hpicfIpStaticRouteFwdIfIndex,
       "hpicfIpStaticRouteType": hpicfIpStaticRouteType,
       "hpicfIpStaticRouteDistance": hpicfIpStaticRouteDistance,
       "hpicfIpStaticRouteTag": hpicfIpStaticRouteTag,
       "hpicfIpStaticRouteStatus": hpicfIpStaticRouteStatus,
       "hpicfIpStaticRouteMetric": hpicfIpStaticRouteMetric,
       "hpicfIpStaticRouteName": hpicfIpStaticRouteName,
       "hpicfIpStaticRouteLogging": hpicfIpStaticRouteLogging,
       "hpicfIpStaticRouteBfdEnable": hpicfIpStaticRouteBfdEnable,
       "hpicfIpStaticNeighborTable": hpicfIpStaticNeighborTable,
       "hpicfIpStaticNeighborEntry": hpicfIpStaticNeighborEntry,
       "hpicfIpStaticNeighborIfIndex": hpicfIpStaticNeighborIfIndex,
       "hpicfIpStaticNeighborNetAddrType": hpicfIpStaticNeighborNetAddrType,
       "hpicfIpStaticNeighborNetAddress": hpicfIpStaticNeighborNetAddress,
       "hpicfIpStaticNeighborPhysAddress": hpicfIpStaticNeighborPhysAddress,
       "hpicfIpStaticNeighborStatus": hpicfIpStaticNeighborStatus,
       "hpicfIpStaticRouteBfdTable": hpicfIpStaticRouteBfdTable,
       "hpicfIpStaticRouteBfdEntry": hpicfIpStaticRouteBfdEntry,
       "hpicfIpStaticRouteBfdSrcAddrType": hpicfIpStaticRouteBfdSrcAddrType,
       "hpicfIpStaticRouteBfdSrcAddr": hpicfIpStaticRouteBfdSrcAddr,
       "hpicfIpStaticRouteBfdDstAddrType": hpicfIpStaticRouteBfdDstAddrType,
       "hpicfIpStaticRouteBfdDstAddr": hpicfIpStaticRouteBfdDstAddr,
       "hpicfIpStaticRouteBfdStatus": hpicfIpStaticRouteBfdStatus,
       "hpicfIpRouteStats": hpicfIpRouteStats,
       "hpicfIpCidrRouteTable": hpicfIpCidrRouteTable,
       "hpicfIpCidrRouteEntry": hpicfIpCidrRouteEntry,
       "hpicfIpCidrRouteDistance": hpicfIpCidrRouteDistance,
       "hpicfInetCidrRouteTable": hpicfInetCidrRouteTable,
       "hpicfInetCidrRouteEntry": hpicfInetCidrRouteEntry,
       "hpicfInetCidrRouteDistance": hpicfInetCidrRouteDistance,
       "hpicfInetCidrRouteInfo": hpicfInetCidrRouteInfo,
       "hpicfInetCidrRouteState": hpicfInetCidrRouteState,
       "hpicfInetCidrRouteStatsTable": hpicfInetCidrRouteStatsTable,
       "hpicfInetCidrRouteStatsEntry": hpicfInetCidrRouteStatsEntry,
       "hpicfInetCidrNumRouteDestinations": hpicfInetCidrNumRouteDestinations,
       "hpicfInetCidrNumRouteRoutes": hpicfInetCidrNumRouteRoutes,
       "hpicfArpInfo": hpicfArpInfo,
       "hpicfArpAgingTime": hpicfArpAgingTime,
       "hpicfArpMcastReplies": hpicfArpMcastReplies,
       "hpicfIpDefaultRouterPrefixInfo": hpicfIpDefaultRouterPrefixInfo,
       "hpicfIpDefaultRouterPrefixTable": hpicfIpDefaultRouterPrefixTable,
       "hpicfIpDefaultRouterPrefixEntry": hpicfIpDefaultRouterPrefixEntry,
       "hpicfIpDefaultRouterAddressType": hpicfIpDefaultRouterAddressType,
       "hpicfIpDefaultRouterAddress": hpicfIpDefaultRouterAddress,
       "hpicfIpDefaultRouterIfIndex": hpicfIpDefaultRouterIfIndex,
       "hpicfIpDefaultRouterPrefixType": hpicfIpDefaultRouterPrefixType,
       "hpicfIpDefaultRouterPrefix": hpicfIpDefaultRouterPrefix,
       "hpicfIpDefaultRouterPrefixLength": hpicfIpDefaultRouterPrefixLength,
       "hpicfIpDefaultRouterPrefixOnLink": hpicfIpDefaultRouterPrefixOnLink,
       "hpicfIpDefaultRouterPrefixAutonomous": hpicfIpDefaultRouterPrefixAutonomous,
       "hpicfIpDefaultRouterPrefixValidLifeTime": hpicfIpDefaultRouterPrefixValidLifeTime,
       "hpicfIpDefaultRouterPrefixPrefdLifeTime": hpicfIpDefaultRouterPrefixPrefdLifeTime,
       "hpicfIpDefaultRouterProperties": hpicfIpDefaultRouterProperties,
       "hpicfIpDefaultRouterTable": hpicfIpDefaultRouterTable,
       "hpicfIpDefaultRouterEntry": hpicfIpDefaultRouterEntry,
       "hpicfIpDefaultRouterMTU": hpicfIpDefaultRouterMTU,
       "hpicfIpDefaultRouterHopLimit": hpicfIpDefaultRouterHopLimit,
       "hpicfIpv6ND": hpicfIpv6ND,
       "hpicfIpv6NDRAAdminStatus": hpicfIpv6NDRAAdminStatus,
       "hpicfIpv6RtrAdvPrefixTable": hpicfIpv6RtrAdvPrefixTable,
       "hpicfIpv6RtrAdvPrefixEntry": hpicfIpv6RtrAdvPrefixEntry,
       "hpicfIpv6RtrAdvPrefixIfIndex": hpicfIpv6RtrAdvPrefixIfIndex,
       "hpicfIpv6RtrAdvPrefixType": hpicfIpv6RtrAdvPrefixType,
       "hpicfIpv6RtrAdvPrefixPrefix": hpicfIpv6RtrAdvPrefixPrefix,
       "hpicfIpv6RtrAdvPrefixLength": hpicfIpv6RtrAdvPrefixLength,
       "hpicfIpv6RtrAdvPrefixOnLinkFlag": hpicfIpv6RtrAdvPrefixOnLinkFlag,
       "hpicfIpv6RtrAdvPrefixAutonomousFlag": hpicfIpv6RtrAdvPrefixAutonomousFlag,
       "hpicfIpv6RtrAdvPrefixLifetimeType": hpicfIpv6RtrAdvPrefixLifetimeType,
       "hpicfIpv6RtrAdvPrefixPreferredLifetime": hpicfIpv6RtrAdvPrefixPreferredLifetime,
       "hpicfIpv6RtrAdvPrefixValidLifetime": hpicfIpv6RtrAdvPrefixValidLifetime,
       "hpicfIpv6RtrAdvPrefixRowStatus": hpicfIpv6RtrAdvPrefixRowStatus,
       "hpicfIpv6RtrAdvPrefixAdvertiseFlag": hpicfIpv6RtrAdvPrefixAdvertiseFlag,
       "hpicfIpv6RtrAdvTable": hpicfIpv6RtrAdvTable,
       "hpicfIpv6RtrAdvEntry": hpicfIpv6RtrAdvEntry,
       "hpicfIpv6RtrAdvCurHopLimitMode": hpicfIpv6RtrAdvCurHopLimitMode,
       "hpicfIpv6RouterAdvertSendDNSAdverts": hpicfIpv6RouterAdvertSendDNSAdverts,
       "hpicfIpv6RouterAdvertRtrPreference": hpicfIpv6RouterAdvertRtrPreference,
       "hpicfIpv6NDRADNSAdminStatus": hpicfIpv6NDRADNSAdminStatus,
       "hpicfIpRouteSummary": hpicfIpRouteSummary,
       "hpicfIpRouteSummaryTable": hpicfIpRouteSummaryTable,
       "hpicfIpRouteEntry": hpicfIpRouteEntry,
       "hpicfIpRouteProto": hpicfIpRouteProto,
       "hpicfIpRouteCnt": hpicfIpRouteCnt,
       "hpicfIpv6RouteSummary": hpicfIpv6RouteSummary,
       "hpicfIpv6RouteSummaryTable": hpicfIpv6RouteSummaryTable,
       "hpicfIpv6RouteEntry": hpicfIpv6RouteEntry,
       "hpicfIpv6RouteProto": hpicfIpv6RouteProto,
       "hpicfIpv6RouteCnt": hpicfIpv6RouteCnt,
       "hpicfIpRoutingConformance": hpicfIpRoutingConformance,
       "hpicfIpRoutingGroups": hpicfIpRoutingGroups,
       "hpicfRdiscBaseGroup": hpicfRdiscBaseGroup,
       "hpicfRdiscIfCfgGroup": hpicfRdiscIfCfgGroup,
       "hpicfIcmpReplyBaseGroup": hpicfIcmpReplyBaseGroup,
       "hpicfIcmpReplyLimitGroup": hpicfIcmpReplyLimitGroup,
       "hpicfIpRouteCfgGroup": hpicfIpRouteCfgGroup,
       "hpicfIpStaticRouteGroup": hpicfIpStaticRouteGroup,
       "hpicfIpStaticNeighborGroup": hpicfIpStaticNeighborGroup,
       "hpicfIpCidrRouteGroup": hpicfIpCidrRouteGroup,
       "hpicfInetCidrRouteGroup": hpicfInetCidrRouteGroup,
       "hpicfArpBaseGroup": hpicfArpBaseGroup,
       "hpicfIpv6RtrAdvPrefixGroup": hpicfIpv6RtrAdvPrefixGroup,
       "hpicfIpv6RtrAdvGroup": hpicfIpv6RtrAdvGroup,
       "hpicfGlobalIpConfigGroup": hpicfGlobalIpConfigGroup,
       "hpicfIpDefaultRouterGroup": hpicfIpDefaultRouterGroup,
       "hpicfIpv6NDRAAdminGroup": hpicfIpv6NDRAAdminGroup,
       "hpicfIpRouteBaseScalarsGroup": hpicfIpRouteBaseScalarsGroup,
       "hpicfIpStaticRouteOtherGroup": hpicfIpStaticRouteOtherGroup,
       "hpicfIpRouteSummaryTableGroup": hpicfIpRouteSummaryTableGroup,
       "hpicfInetCidrRouteGroup1": hpicfInetCidrRouteGroup1,
       "hpicfInetCidrRouteStatsGroup": hpicfInetCidrRouteStatsGroup,
       "hpicfIpv6RtrAdvDNSGroup": hpicfIpv6RtrAdvDNSGroup,
       "hpicfIpv6NDRADNSAdminGroup": hpicfIpv6NDRADNSAdminGroup,
       "hpicfIpStaticRouteNameGroup": hpicfIpStaticRouteNameGroup,
       "hpicfIpv6RouteSummaryTableGroup": hpicfIpv6RouteSummaryTableGroup,
       "hpicfDBroadcastFwdAclGroup": hpicfDBroadcastFwdAclGroup,
       "hpicfIpStaticRouteParamGroup": hpicfIpStaticRouteParamGroup,
       "hpicfIpv6RtrAdvParamGroup": hpicfIpv6RtrAdvParamGroup,
       "hpicfIpStaticRouteParamGroup1": hpicfIpStaticRouteParamGroup1,
       "hpicfIpStaticRouteBfdGroup": hpicfIpStaticRouteBfdGroup,
       "hpicfIpRoutingCompliances": hpicfIpRoutingCompliances,
       "hpicfIcmpRdiscCompliance": hpicfIcmpRdiscCompliance,
       "hpicfIcmpReplyCompliance": hpicfIcmpReplyCompliance,
       "hpicfIpRouterCompliance": hpicfIpRouterCompliance,
       "hpicfArpInfoCompliance": hpicfArpInfoCompliance,
       "hpicfIpv6RtrAdvPrefixCompliance": hpicfIpv6RtrAdvPrefixCompliance,
       "hpicfIpv6RtrAdvCompliance": hpicfIpv6RtrAdvCompliance,
       "hpicfGlobalIpConfigCompliance": hpicfGlobalIpConfigCompliance,
       "hpicfIpDefaultRouterCompliance": hpicfIpDefaultRouterCompliance,
       "hpicfIpv6NDRAAdminCompliance": hpicfIpv6NDRAAdminCompliance,
       "hpicfIpRouteBaseScalarsCompliance": hpicfIpRouteBaseScalarsCompliance,
       "hpicfInetCidrRouteCompliance": hpicfInetCidrRouteCompliance,
       "hpicfIpRouterOtherCompliance": hpicfIpRouterOtherCompliance,
       "hpicfIpRouteSummaryCompliance": hpicfIpRouteSummaryCompliance,
       "hpicfInetCidrRouteCompliance1": hpicfInetCidrRouteCompliance1,
       "hpicfInetCidrRouteStatsCompliance": hpicfInetCidrRouteStatsCompliance,
       "hpicfIpv6RtrAdvDNSCompliance": hpicfIpv6RtrAdvDNSCompliance,
       "hpicfIpv6NDRADNSAdminCompliance": hpicfIpv6NDRADNSAdminCompliance,
       "hpicfIpStaticRouteNameCompliance": hpicfIpStaticRouteNameCompliance,
       "hpicfIpv6RouteSummaryCompliance": hpicfIpv6RouteSummaryCompliance,
       "hpicfIpDBroadcastFwdAclCompliance": hpicfIpDBroadcastFwdAclCompliance,
       "hpicfIpRouteCompliance": hpicfIpRouteCompliance,
       "hpicfIpv6RtrAdvParamCompliance": hpicfIpv6RtrAdvParamCompliance,
       "hpicfIpStaticRouteCompliance1": hpicfIpStaticRouteCompliance1,
       "hpicfIpRouteBaseScalars": hpicfIpRouteBaseScalars,
       "hpicfIpRouteCount": hpicfIpRouteCount,
       "hpicfIpRouteNextHopCount": hpicfIpRouteNextHopCount}
)
