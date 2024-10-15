# SNMP MIB module (LANTRONIX-SLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LANTRONIX-SLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:20 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(products,) = mibBuilder.importSymbols(
    "LANTRONIX-MIB",
    "products")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

slc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1)
)
slc.setRevisions(
        ("2016-04-17 00:00",
         "2015-02-24 00:00",
         "2014-07-10 00:00",
         "2013-12-06 00:00",
         "2013-02-20 00:00",
         "2010-04-07 00:00",
         "2010-01-19 00:00",
         "2009-12-09 00:00",
         "2008-01-09 00:00",
         "2007-06-25 00:00",
         "2007-02-20 00:00",
         "2007-02-07 00:00",
         "2006-10-20 00:00",
         "2006-07-14 00:00",
         "2006-05-12 00:00",
         "2006-02-13 00:00",
         "2005-10-03 00:00",
         "2005-06-09 00:00",
         "2004-12-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )



class AuthOrder(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )



class SyslogLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("debug", 5),
          ("error", 4),
          ("info", 2),
          ("off", 1),
          ("warning", 3))
    )



class UserGroup(Integer32, TextualConvention):
    status = "current"
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
        *(("administrators", 3),
          ("custom", 4),
          ("default", 1),
          ("power", 2))
    )



class UserRights(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class TimeoutDataDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bothDirections", 3),
          ("incomingNetwork", 1),
          ("outgoingNetwork", 2))
    )



class RPMTowerIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )



class RPMOutletIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )



# MIB Managed Objects in the order of their OIDs

_SlcEvents_ObjectIdentity = ObjectIdentity
slcEvents = _SlcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0)
)
_SlcNetwork_ObjectIdentity = ObjectIdentity
slcNetwork = _SlcNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1)
)
_SlcNetEth_ObjectIdentity = ObjectIdentity
slcNetEth = _SlcNetEth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1)
)


class _SlcNetEthIfNumber_Type(Integer32):
    """Custom type slcNetEthIfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlcNetEthIfNumber_Type.__name__ = "Integer32"
_SlcNetEthIfNumber_Object = MibScalar
slcNetEthIfNumber = _SlcNetEthIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 1),
    _SlcNetEthIfNumber_Type()
)
slcNetEthIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfNumber.setStatus("current")
_SlcNetEthIfTable_Object = MibTable
slcNetEthIfTable = _SlcNetEthIfTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    slcNetEthIfTable.setStatus("current")
_SlcNetEthIfEntry_Object = MibTableRow
slcNetEthIfEntry = _SlcNetEthIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1)
)
slcNetEthIfEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcNetEthIfIndex"),
)
if mibBuilder.loadTexts:
    slcNetEthIfEntry.setStatus("current")


class _SlcNetEthIfIndex_Type(Integer32):
    """Custom type slcNetEthIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlcNetEthIfIndex_Type.__name__ = "Integer32"
_SlcNetEthIfIndex_Object = MibTableColumn
slcNetEthIfIndex = _SlcNetEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 1),
    _SlcNetEthIfIndex_Type()
)
slcNetEthIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfIndex.setStatus("current")


class _SlcNetEthIfSource_Type(Integer32):
    """Custom type slcNetEthIfSource based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 2),
          ("disabled", 1),
          ("static", 4))
    )


_SlcNetEthIfSource_Type.__name__ = "Integer32"
_SlcNetEthIfSource_Object = MibTableColumn
slcNetEthIfSource = _SlcNetEthIfSource_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 2),
    _SlcNetEthIfSource_Type()
)
slcNetEthIfSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfSource.setStatus("current")


class _SlcNetEthIfMode_Type(Integer32):
    """Custom type slcNetEthIfMode based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex1000mbit", 7),
          ("fullDuplex100mbit", 5),
          ("fullDuplex10mbit", 3),
          ("halfDuplex1000mbit", 6),
          ("halfDuplex100mbit", 4),
          ("halfDuplex10mbit", 2))
    )


_SlcNetEthIfMode_Type.__name__ = "Integer32"
_SlcNetEthIfMode_Object = MibTableColumn
slcNetEthIfMode = _SlcNetEthIfMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 3),
    _SlcNetEthIfMode_Type()
)
slcNetEthIfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfMode.setStatus("current")
_SlcNetEthIfIPv6Addr_Type = Ipv6Address
_SlcNetEthIfIPv6Addr_Object = MibTableColumn
slcNetEthIfIPv6Addr = _SlcNetEthIfIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 4),
    _SlcNetEthIfIPv6Addr_Type()
)
slcNetEthIfIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfIPv6Addr.setStatus("current")


class _SlcNetEthIfIPv6PrefixLength_Type(Integer32):
    """Custom type slcNetEthIfIPv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlcNetEthIfIPv6PrefixLength_Type.__name__ = "Integer32"
_SlcNetEthIfIPv6PrefixLength_Object = MibTableColumn
slcNetEthIfIPv6PrefixLength = _SlcNetEthIfIPv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 5),
    _SlcNetEthIfIPv6PrefixLength_Type()
)
slcNetEthIfIPv6PrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slcNetEthIfIPv6PrefixLength.setStatus("current")
_SlcNetEthIfMTU_Type = Integer32
_SlcNetEthIfMTU_Object = MibTableColumn
slcNetEthIfMTU = _SlcNetEthIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 6),
    _SlcNetEthIfMTU_Type()
)
slcNetEthIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfMTU.setStatus("current")
_SlcNetEthIfMacAddress_Type = MacAddress
_SlcNetEthIfMacAddress_Object = MibTableColumn
slcNetEthIfMacAddress = _SlcNetEthIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 2, 1, 7),
    _SlcNetEthIfMacAddress_Type()
)
slcNetEthIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIfMacAddress.setStatus("current")
_SlcNetEthGateway_Type = IpAddress
_SlcNetEthGateway_Object = MibScalar
slcNetEthGateway = _SlcNetEthGateway_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 3),
    _SlcNetEthGateway_Type()
)
slcNetEthGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthGateway.setStatus("current")


class _SlcNetEthGatewayPrecedence_Type(Integer32):
    """Custom type slcNetEthGatewayPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 2),
          ("dhcp", 1),
          ("gprs", 3))
    )


_SlcNetEthGatewayPrecedence_Type.__name__ = "Integer32"
_SlcNetEthGatewayPrecedence_Object = MibScalar
slcNetEthGatewayPrecedence = _SlcNetEthGatewayPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 4),
    _SlcNetEthGatewayPrecedence_Type()
)
slcNetEthGatewayPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthGatewayPrecedence.setStatus("current")


class _SlcNetEthKeepaliveStartProbes_Type(Integer32):
    """Custom type slcNetEthKeepaliveStartProbes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99999),
    )


_SlcNetEthKeepaliveStartProbes_Type.__name__ = "Integer32"
_SlcNetEthKeepaliveStartProbes_Object = MibScalar
slcNetEthKeepaliveStartProbes = _SlcNetEthKeepaliveStartProbes_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 5),
    _SlcNetEthKeepaliveStartProbes_Type()
)
slcNetEthKeepaliveStartProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthKeepaliveStartProbes.setStatus("current")


class _SlcNetEthKeepaliveNumberOfProbes_Type(Integer32):
    """Custom type slcNetEthKeepaliveNumberOfProbes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_SlcNetEthKeepaliveNumberOfProbes_Type.__name__ = "Integer32"
_SlcNetEthKeepaliveNumberOfProbes_Object = MibScalar
slcNetEthKeepaliveNumberOfProbes = _SlcNetEthKeepaliveNumberOfProbes_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 6),
    _SlcNetEthKeepaliveNumberOfProbes_Type()
)
slcNetEthKeepaliveNumberOfProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthKeepaliveNumberOfProbes.setStatus("current")


class _SlcNetEthKeepaliveInterval_Type(Integer32):
    """Custom type slcNetEthKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_SlcNetEthKeepaliveInterval_Type.__name__ = "Integer32"
_SlcNetEthKeepaliveInterval_Object = MibScalar
slcNetEthKeepaliveInterval = _SlcNetEthKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 7),
    _SlcNetEthKeepaliveInterval_Type()
)
slcNetEthKeepaliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthKeepaliveInterval.setStatus("current")
_SlcNetEthIPForwarding_Type = EnabledState
_SlcNetEthIPForwarding_Object = MibScalar
slcNetEthIPForwarding = _SlcNetEthIPForwarding_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 8),
    _SlcNetEthIPForwarding_Type()
)
slcNetEthIPForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIPForwarding.setStatus("current")
_SlcNetEthDNS1_Type = IpAddress
_SlcNetEthDNS1_Object = MibScalar
slcNetEthDNS1 = _SlcNetEthDNS1_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 9),
    _SlcNetEthDNS1_Type()
)
slcNetEthDNS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS1.setStatus("current")
_SlcNetEthDNS2_Type = IpAddress
_SlcNetEthDNS2_Object = MibScalar
slcNetEthDNS2 = _SlcNetEthDNS2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 10),
    _SlcNetEthDNS2_Type()
)
slcNetEthDNS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS2.setStatus("current")
_SlcNetEthDNS3_Type = IpAddress
_SlcNetEthDNS3_Object = MibScalar
slcNetEthDNS3 = _SlcNetEthDNS3_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 11),
    _SlcNetEthDNS3_Type()
)
slcNetEthDNS3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS3.setStatus("current")
_SlcNetEthDomain_Type = OctetString
_SlcNetEthDomain_Object = MibScalar
slcNetEthDomain = _SlcNetEthDomain_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 12),
    _SlcNetEthDomain_Type()
)
slcNetEthDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDomain.setStatus("current")
_SlcNetEthAlternateGateway_Type = IpAddress
_SlcNetEthAlternateGateway_Object = MibScalar
slcNetEthAlternateGateway = _SlcNetEthAlternateGateway_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 13),
    _SlcNetEthAlternateGateway_Type()
)
slcNetEthAlternateGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthAlternateGateway.setStatus("current")
_SlcNetEthPingIPAddress_Type = IpAddress
_SlcNetEthPingIPAddress_Object = MibScalar
slcNetEthPingIPAddress = _SlcNetEthPingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 14),
    _SlcNetEthPingIPAddress_Type()
)
slcNetEthPingIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthPingIPAddress.setStatus("current")


class _SlcNetEthPingInterface_Type(Integer32):
    """Custom type slcNetEthPingInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet1", 1),
          ("ethernet2", 2))
    )


_SlcNetEthPingInterface_Type.__name__ = "Integer32"
_SlcNetEthPingInterface_Object = MibScalar
slcNetEthPingInterface = _SlcNetEthPingInterface_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 15),
    _SlcNetEthPingInterface_Type()
)
slcNetEthPingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthPingInterface.setStatus("current")


class _SlcNetEthPingDelay_Type(Integer32):
    """Custom type slcNetEthPingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SlcNetEthPingDelay_Type.__name__ = "Integer32"
_SlcNetEthPingDelay_Object = MibScalar
slcNetEthPingDelay = _SlcNetEthPingDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 16),
    _SlcNetEthPingDelay_Type()
)
slcNetEthPingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthPingDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcNetEthPingDelay.setUnits("seconds")


class _SlcNetEthPingFailed_Type(Integer32):
    """Custom type slcNetEthPingFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_SlcNetEthPingFailed_Type.__name__ = "Integer32"
_SlcNetEthPingFailed_Object = MibScalar
slcNetEthPingFailed = _SlcNetEthPingFailed_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 17),
    _SlcNetEthPingFailed_Type()
)
slcNetEthPingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthPingFailed.setStatus("current")


class _SlcNetEthBonding_Type(Integer32):
    """Custom type slcNetEthBonding based on Integer32"""
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
        *(("activeBackup", 2),
          ("adaptiveLoadBalancing", 4),
          ("aggregation", 3),
          ("disabled", 1))
    )


_SlcNetEthBonding_Type.__name__ = "Integer32"
_SlcNetEthBonding_Object = MibScalar
slcNetEthBonding = _SlcNetEthBonding_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 18),
    _SlcNetEthBonding_Type()
)
slcNetEthBonding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthBonding.setStatus("current")
_SlcNetEthIPv6_Type = EnabledState
_SlcNetEthIPv6_Object = MibScalar
slcNetEthIPv6 = _SlcNetEthIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 19),
    _SlcNetEthIPv6_Type()
)
slcNetEthIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthIPv6.setStatus("current")
_SlcNetEthGatewayIPv6_Type = Ipv6Address
_SlcNetEthGatewayIPv6_Object = MibScalar
slcNetEthGatewayIPv6 = _SlcNetEthGatewayIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 20),
    _SlcNetEthGatewayIPv6_Type()
)
slcNetEthGatewayIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthGatewayIPv6.setStatus("current")
_SlcNetEthDNS1IPv6_Type = Ipv6Address
_SlcNetEthDNS1IPv6_Object = MibScalar
slcNetEthDNS1IPv6 = _SlcNetEthDNS1IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 21),
    _SlcNetEthDNS1IPv6_Type()
)
slcNetEthDNS1IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS1IPv6.setStatus("current")
_SlcNetEthDNS2IPv6_Type = Ipv6Address
_SlcNetEthDNS2IPv6_Object = MibScalar
slcNetEthDNS2IPv6 = _SlcNetEthDNS2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 22),
    _SlcNetEthDNS2IPv6_Type()
)
slcNetEthDNS2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS2IPv6.setStatus("current")
_SlcNetEthDNS3IPv6_Type = Ipv6Address
_SlcNetEthDNS3IPv6_Object = MibScalar
slcNetEthDNS3IPv6 = _SlcNetEthDNS3IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 23),
    _SlcNetEthDNS3IPv6_Type()
)
slcNetEthDNS3IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthDNS3IPv6.setStatus("current")
_SlcNetEthPreferIPv4DNS_Type = EnabledState
_SlcNetEthPreferIPv4DNS_Object = MibScalar
slcNetEthPreferIPv4DNS = _SlcNetEthPreferIPv4DNS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 1, 24),
    _SlcNetEthPreferIPv4DNS_Type()
)
slcNetEthPreferIPv4DNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetEthPreferIPv4DNS.setStatus("current")
_SlcNetFirewall_ObjectIdentity = ObjectIdentity
slcNetFirewall = _SlcNetFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2)
)
_SlcNetFirewallState_Type = EnabledState
_SlcNetFirewallState_Object = MibScalar
slcNetFirewallState = _SlcNetFirewallState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 1),
    _SlcNetFirewallState_Type()
)
slcNetFirewallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallState.setStatus("current")


class _SlcNetFirewallReject_Type(Integer32):
    """Custom type slcNetFirewallReject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("return", 1))
    )


_SlcNetFirewallReject_Type.__name__ = "Integer32"
_SlcNetFirewallReject_Object = MibScalar
slcNetFirewallReject = _SlcNetFirewallReject_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 2),
    _SlcNetFirewallReject_Type()
)
slcNetFirewallReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallReject.setStatus("obsolete")
_SlcNetFirewallPing_Type = EnabledState
_SlcNetFirewallPing_Object = MibScalar
slcNetFirewallPing = _SlcNetFirewallPing_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 3),
    _SlcNetFirewallPing_Type()
)
slcNetFirewallPing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallPing.setStatus("obsolete")
_SlcNetFirewallSSH_Type = EnabledState
_SlcNetFirewallSSH_Object = MibScalar
slcNetFirewallSSH = _SlcNetFirewallSSH_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 4),
    _SlcNetFirewallSSH_Type()
)
slcNetFirewallSSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallSSH.setStatus("obsolete")
_SlcNetFirewallTelnet_Type = EnabledState
_SlcNetFirewallTelnet_Object = MibScalar
slcNetFirewallTelnet = _SlcNetFirewallTelnet_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 5),
    _SlcNetFirewallTelnet_Type()
)
slcNetFirewallTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallTelnet.setStatus("obsolete")
_SlcNetFirewallHTTP_Type = EnabledState
_SlcNetFirewallHTTP_Object = MibScalar
slcNetFirewallHTTP = _SlcNetFirewallHTTP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 6),
    _SlcNetFirewallHTTP_Type()
)
slcNetFirewallHTTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallHTTP.setStatus("obsolete")
_SlcNetFirewallHTTPS_Type = EnabledState
_SlcNetFirewallHTTPS_Object = MibScalar
slcNetFirewallHTTPS = _SlcNetFirewallHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 7),
    _SlcNetFirewallHTTPS_Type()
)
slcNetFirewallHTTPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallHTTPS.setStatus("obsolete")
_SlcNetFirewallSMBCIFS_Type = EnabledState
_SlcNetFirewallSMBCIFS_Object = MibScalar
slcNetFirewallSMBCIFS = _SlcNetFirewallSMBCIFS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 8),
    _SlcNetFirewallSMBCIFS_Type()
)
slcNetFirewallSMBCIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallSMBCIFS.setStatus("obsolete")


class _SlcNetFirewallRulesetNumber_Type(Integer32):
    """Custom type slcNetFirewallRulesetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlcNetFirewallRulesetNumber_Type.__name__ = "Integer32"
_SlcNetFirewallRulesetNumber_Object = MibScalar
slcNetFirewallRulesetNumber = _SlcNetFirewallRulesetNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 9),
    _SlcNetFirewallRulesetNumber_Type()
)
slcNetFirewallRulesetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallRulesetNumber.setStatus("current")
_SlcNetFirewallRulesetTable_Object = MibTable
slcNetFirewallRulesetTable = _SlcNetFirewallRulesetTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10)
)
if mibBuilder.loadTexts:
    slcNetFirewallRulesetTable.setStatus("current")
_SlcNetFirewallRulesetEntry_Object = MibTableRow
slcNetFirewallRulesetEntry = _SlcNetFirewallRulesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10, 1)
)
slcNetFirewallRulesetEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcNetFirewallRulesetIndex"),
)
if mibBuilder.loadTexts:
    slcNetFirewallRulesetEntry.setStatus("current")


class _SlcNetFirewallRulesetIndex_Type(Integer32):
    """Custom type slcNetFirewallRulesetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlcNetFirewallRulesetIndex_Type.__name__ = "Integer32"
_SlcNetFirewallRulesetIndex_Object = MibTableColumn
slcNetFirewallRulesetIndex = _SlcNetFirewallRulesetIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10, 1, 1),
    _SlcNetFirewallRulesetIndex_Type()
)
slcNetFirewallRulesetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallRulesetIndex.setStatus("current")
_SlcNetFirewallRulesetName_Type = OctetString
_SlcNetFirewallRulesetName_Object = MibTableColumn
slcNetFirewallRulesetName = _SlcNetFirewallRulesetName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10, 1, 2),
    _SlcNetFirewallRulesetName_Type()
)
slcNetFirewallRulesetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallRulesetName.setStatus("current")


class _SlcNetFirewallRulesetNumRules_Type(Integer32):
    """Custom type slcNetFirewallRulesetNumRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SlcNetFirewallRulesetNumRules_Type.__name__ = "Integer32"
_SlcNetFirewallRulesetNumRules_Object = MibTableColumn
slcNetFirewallRulesetNumRules = _SlcNetFirewallRulesetNumRules_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10, 1, 3),
    _SlcNetFirewallRulesetNumRules_Type()
)
slcNetFirewallRulesetNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallRulesetNumRules.setStatus("current")
_SlcNetFirewallRulesetRules_Type = OctetString
_SlcNetFirewallRulesetRules_Object = MibTableColumn
slcNetFirewallRulesetRules = _SlcNetFirewallRulesetRules_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 10, 1, 4),
    _SlcNetFirewallRulesetRules_Type()
)
slcNetFirewallRulesetRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallRulesetRules.setStatus("current")
_SlcNetFirewallMappingNumber_Type = Integer32
_SlcNetFirewallMappingNumber_Object = MibScalar
slcNetFirewallMappingNumber = _SlcNetFirewallMappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 11),
    _SlcNetFirewallMappingNumber_Type()
)
slcNetFirewallMappingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallMappingNumber.setStatus("current")
_SlcNetFirewallMappingTable_Object = MibTable
slcNetFirewallMappingTable = _SlcNetFirewallMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    slcNetFirewallMappingTable.setStatus("current")
_SlcNetFirewallMappingEntry_Object = MibTableRow
slcNetFirewallMappingEntry = _SlcNetFirewallMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12, 1)
)
slcNetFirewallMappingEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcNetFirewallMappingIndex"),
)
if mibBuilder.loadTexts:
    slcNetFirewallMappingEntry.setStatus("current")


class _SlcNetFirewallMappingIndex_Type(Integer32):
    """Custom type slcNetFirewallMappingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlcNetFirewallMappingIndex_Type.__name__ = "Integer32"
_SlcNetFirewallMappingIndex_Object = MibTableColumn
slcNetFirewallMappingIndex = _SlcNetFirewallMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12, 1, 1),
    _SlcNetFirewallMappingIndex_Type()
)
slcNetFirewallMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallMappingIndex.setStatus("current")


class _SlcNetFirewallMappingIfac_Type(Integer32):
    """Custom type slcNetFirewallMappingIfac based on Integer32"""
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
        *(("devicePort", 5),
          ("ethernet1", 1),
          ("ethernet2", 2),
          ("internalModem", 7),
          ("lowerPCCard", 4),
          ("upperPCCard", 3),
          ("usbPort", 6))
    )


_SlcNetFirewallMappingIfac_Type.__name__ = "Integer32"
_SlcNetFirewallMappingIfac_Object = MibTableColumn
slcNetFirewallMappingIfac = _SlcNetFirewallMappingIfac_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12, 1, 2),
    _SlcNetFirewallMappingIfac_Type()
)
slcNetFirewallMappingIfac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallMappingIfac.setStatus("current")


class _SlcNetFirewallMappingIfacId_Type(Integer32):
    """Custom type slcNetFirewallMappingIfacId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SlcNetFirewallMappingIfacId_Type.__name__ = "Integer32"
_SlcNetFirewallMappingIfacId_Object = MibTableColumn
slcNetFirewallMappingIfacId = _SlcNetFirewallMappingIfacId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12, 1, 3),
    _SlcNetFirewallMappingIfacId_Type()
)
slcNetFirewallMappingIfacId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallMappingIfacId.setStatus("current")
_SlcNetFirewallMappingRuleset_Type = OctetString
_SlcNetFirewallMappingRuleset_Object = MibTableColumn
slcNetFirewallMappingRuleset = _SlcNetFirewallMappingRuleset_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 2, 12, 1, 4),
    _SlcNetFirewallMappingRuleset_Type()
)
slcNetFirewallMappingRuleset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetFirewallMappingRuleset.setStatus("current")
_SlcNetRouting_ObjectIdentity = ObjectIdentity
slcNetRouting = _SlcNetRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3)
)
_SlcNetRouteRIPState_Type = EnabledState
_SlcNetRouteRIPState_Object = MibScalar
slcNetRouteRIPState = _SlcNetRouteRIPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 1),
    _SlcNetRouteRIPState_Type()
)
slcNetRouteRIPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteRIPState.setStatus("current")


class _SlcNetRouteRIPVersion_Type(Integer32):
    """Custom type slcNetRouteRIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("oneAndTwo", 3),
          ("two", 2))
    )


_SlcNetRouteRIPVersion_Type.__name__ = "Integer32"
_SlcNetRouteRIPVersion_Object = MibScalar
slcNetRouteRIPVersion = _SlcNetRouteRIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 2),
    _SlcNetRouteRIPVersion_Type()
)
slcNetRouteRIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteRIPVersion.setStatus("current")
_SlcNetRouteStaticState_Type = EnabledState
_SlcNetRouteStaticState_Object = MibScalar
slcNetRouteStaticState = _SlcNetRouteStaticState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 3),
    _SlcNetRouteStaticState_Type()
)
slcNetRouteStaticState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticState.setStatus("current")


class _SlcNetRouteStaticNumber_Type(Integer32):
    """Custom type slcNetRouteStaticNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SlcNetRouteStaticNumber_Type.__name__ = "Integer32"
_SlcNetRouteStaticNumber_Object = MibScalar
slcNetRouteStaticNumber = _SlcNetRouteStaticNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 4),
    _SlcNetRouteStaticNumber_Type()
)
slcNetRouteStaticNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticNumber.setStatus("current")
_SlcNetRouteStaticTable_Object = MibTable
slcNetRouteStaticTable = _SlcNetRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    slcNetRouteStaticTable.setStatus("current")
_SlcNetRouteStaticEntry_Object = MibTableRow
slcNetRouteStaticEntry = _SlcNetRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5, 1)
)
slcNetRouteStaticEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcNetRouteStaticIndex"),
)
if mibBuilder.loadTexts:
    slcNetRouteStaticEntry.setStatus("current")


class _SlcNetRouteStaticIndex_Type(Integer32):
    """Custom type slcNetRouteStaticIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SlcNetRouteStaticIndex_Type.__name__ = "Integer32"
_SlcNetRouteStaticIndex_Object = MibTableColumn
slcNetRouteStaticIndex = _SlcNetRouteStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5, 1, 1),
    _SlcNetRouteStaticIndex_Type()
)
slcNetRouteStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticIndex.setStatus("current")
_SlcNetRouteStaticIP_Type = IpAddress
_SlcNetRouteStaticIP_Object = MibTableColumn
slcNetRouteStaticIP = _SlcNetRouteStaticIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5, 1, 2),
    _SlcNetRouteStaticIP_Type()
)
slcNetRouteStaticIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticIP.setStatus("current")
_SlcNetRouteStaticMask_Type = IpAddress
_SlcNetRouteStaticMask_Object = MibTableColumn
slcNetRouteStaticMask = _SlcNetRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5, 1, 3),
    _SlcNetRouteStaticMask_Type()
)
slcNetRouteStaticMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticMask.setStatus("current")
_SlcNetRouteStaticGateway_Type = IpAddress
_SlcNetRouteStaticGateway_Object = MibTableColumn
slcNetRouteStaticGateway = _SlcNetRouteStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 3, 5, 1, 4),
    _SlcNetRouteStaticGateway_Type()
)
slcNetRouteStaticGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetRouteStaticGateway.setStatus("current")
_SlcNetVPN_ObjectIdentity = ObjectIdentity
slcNetVPN = _SlcNetVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4)
)
_SlcNetVPNTunnel_Type = EnabledState
_SlcNetVPNTunnel_Object = MibScalar
slcNetVPNTunnel = _SlcNetVPNTunnel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 1),
    _SlcNetVPNTunnel_Type()
)
slcNetVPNTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNTunnel.setStatus("current")
_SlcNetVPNStatus_Type = OctetString
_SlcNetVPNStatus_Object = MibScalar
slcNetVPNStatus = _SlcNetVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 2),
    _SlcNetVPNStatus_Type()
)
slcNetVPNStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNStatus.setStatus("current")


class _SlcNetVPNName_Type(OctetString):
    """Custom type slcNetVPNName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlcNetVPNName_Type.__name__ = "OctetString"
_SlcNetVPNName_Object = MibScalar
slcNetVPNName = _SlcNetVPNName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 3),
    _SlcNetVPNName_Type()
)
slcNetVPNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNName.setStatus("current")


class _SlcNetVPNEthPort_Type(Integer32):
    """Custom type slcNetVPNEthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet1", 1),
          ("ethernet2", 2))
    )


_SlcNetVPNEthPort_Type.__name__ = "Integer32"
_SlcNetVPNEthPort_Object = MibScalar
slcNetVPNEthPort = _SlcNetVPNEthPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 4),
    _SlcNetVPNEthPort_Type()
)
slcNetVPNEthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNEthPort.setStatus("current")
_SlcNetVPNRemoteHost_Type = IpAddress
_SlcNetVPNRemoteHost_Object = MibScalar
slcNetVPNRemoteHost = _SlcNetVPNRemoteHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 5),
    _SlcNetVPNRemoteHost_Type()
)
slcNetVPNRemoteHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNRemoteHost.setStatus("current")


class _SlcNetVPNRemoteId_Type(OctetString):
    """Custom type slcNetVPNRemoteId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlcNetVPNRemoteId_Type.__name__ = "OctetString"
_SlcNetVPNRemoteId_Object = MibScalar
slcNetVPNRemoteId = _SlcNetVPNRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 6),
    _SlcNetVPNRemoteId_Type()
)
slcNetVPNRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNRemoteId.setStatus("current")
_SlcNetVPNRemoteHop_Type = IpAddress
_SlcNetVPNRemoteHop_Object = MibScalar
slcNetVPNRemoteHop = _SlcNetVPNRemoteHop_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 7),
    _SlcNetVPNRemoteHop_Type()
)
slcNetVPNRemoteHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNRemoteHop.setStatus("current")
_SlcNetVPNRemoteSubnet_Type = OctetString
_SlcNetVPNRemoteSubnet_Object = MibScalar
slcNetVPNRemoteSubnet = _SlcNetVPNRemoteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 8),
    _SlcNetVPNRemoteSubnet_Type()
)
slcNetVPNRemoteSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNRemoteSubnet.setStatus("current")


class _SlcNetVPNLocalId_Type(OctetString):
    """Custom type slcNetVPNLocalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlcNetVPNLocalId_Type.__name__ = "OctetString"
_SlcNetVPNLocalId_Object = MibScalar
slcNetVPNLocalId = _SlcNetVPNLocalId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 9),
    _SlcNetVPNLocalId_Type()
)
slcNetVPNLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNLocalId.setStatus("current")
_SlcNetVPNLocalHop_Type = IpAddress
_SlcNetVPNLocalHop_Object = MibScalar
slcNetVPNLocalHop = _SlcNetVPNLocalHop_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 10),
    _SlcNetVPNLocalHop_Type()
)
slcNetVPNLocalHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNLocalHop.setStatus("current")
_SlcNetVPNLocalSubnet_Type = OctetString
_SlcNetVPNLocalSubnet_Object = MibScalar
slcNetVPNLocalSubnet = _SlcNetVPNLocalSubnet_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 11),
    _SlcNetVPNLocalSubnet_Type()
)
slcNetVPNLocalSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNLocalSubnet.setStatus("current")


class _SlcNetVPNIKENegotiation_Type(Integer32):
    """Custom type slcNetVPNIKENegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aggressive", 2),
          ("main", 1))
    )


_SlcNetVPNIKENegotiation_Type.__name__ = "Integer32"
_SlcNetVPNIKENegotiation_Object = MibScalar
slcNetVPNIKENegotiation = _SlcNetVPNIKENegotiation_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 12),
    _SlcNetVPNIKENegotiation_Type()
)
slcNetVPNIKENegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNIKENegotiation.setStatus("current")


class _SlcNetVPNIKEEncryption_Type(Integer32):
    """Custom type slcNetVPNIKEEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("any", 1),
          ("tripledes", 2))
    )


_SlcNetVPNIKEEncryption_Type.__name__ = "Integer32"
_SlcNetVPNIKEEncryption_Object = MibScalar
slcNetVPNIKEEncryption = _SlcNetVPNIKEEncryption_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 13),
    _SlcNetVPNIKEEncryption_Type()
)
slcNetVPNIKEEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNIKEEncryption.setStatus("current")


class _SlcNetVPNIKEAuthentication_Type(Integer32):
    """Custom type slcNetVPNIKEAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("md5", 3),
          ("sha1", 2))
    )


_SlcNetVPNIKEAuthentication_Type.__name__ = "Integer32"
_SlcNetVPNIKEAuthentication_Object = MibScalar
slcNetVPNIKEAuthentication = _SlcNetVPNIKEAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 14),
    _SlcNetVPNIKEAuthentication_Type()
)
slcNetVPNIKEAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNIKEAuthentication.setStatus("current")


class _SlcNetVPNIKEDHGroup_Type(Integer32):
    """Custom type slcNetVPNIKEDHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dhg2", 2),
          ("dhg5", 3))
    )


_SlcNetVPNIKEDHGroup_Type.__name__ = "Integer32"
_SlcNetVPNIKEDHGroup_Object = MibScalar
slcNetVPNIKEDHGroup = _SlcNetVPNIKEDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 15),
    _SlcNetVPNIKEDHGroup_Type()
)
slcNetVPNIKEDHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNIKEDHGroup.setStatus("current")


class _SlcNetVPNESPEncryption_Type(Integer32):
    """Custom type slcNetVPNESPEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("any", 1),
          ("tripledes", 2))
    )


_SlcNetVPNESPEncryption_Type.__name__ = "Integer32"
_SlcNetVPNESPEncryption_Object = MibScalar
slcNetVPNESPEncryption = _SlcNetVPNESPEncryption_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 16),
    _SlcNetVPNESPEncryption_Type()
)
slcNetVPNESPEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNESPEncryption.setStatus("current")


class _SlcNetVPNESPAuthentication_Type(Integer32):
    """Custom type slcNetVPNESPAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("md5", 3),
          ("sha1", 2))
    )


_SlcNetVPNESPAuthentication_Type.__name__ = "Integer32"
_SlcNetVPNESPAuthentication_Object = MibScalar
slcNetVPNESPAuthentication = _SlcNetVPNESPAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 17),
    _SlcNetVPNESPAuthentication_Type()
)
slcNetVPNESPAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNESPAuthentication.setStatus("current")


class _SlcNetVPNESPDHGroup_Type(Integer32):
    """Custom type slcNetVPNESPDHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("dhg2", 2),
          ("dhg5", 3))
    )


_SlcNetVPNESPDHGroup_Type.__name__ = "Integer32"
_SlcNetVPNESPDHGroup_Object = MibScalar
slcNetVPNESPDHGroup = _SlcNetVPNESPDHGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 18),
    _SlcNetVPNESPDHGroup_Type()
)
slcNetVPNESPDHGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNESPDHGroup.setStatus("current")


class _SlcNetVPNAuthentication_Type(Integer32):
    """Custom type slcNetVPNAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("preSharedKey", 2),
          ("rsaPublicKey", 1))
    )


_SlcNetVPNAuthentication_Type.__name__ = "Integer32"
_SlcNetVPNAuthentication_Object = MibScalar
slcNetVPNAuthentication = _SlcNetVPNAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 19),
    _SlcNetVPNAuthentication_Type()
)
slcNetVPNAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNAuthentication.setStatus("current")
_SlcNetVPNPerfectForwardSecrecy_Type = EnabledState
_SlcNetVPNPerfectForwardSecrecy_Object = MibScalar
slcNetVPNPerfectForwardSecrecy = _SlcNetVPNPerfectForwardSecrecy_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 20),
    _SlcNetVPNPerfectForwardSecrecy_Type()
)
slcNetVPNPerfectForwardSecrecy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNPerfectForwardSecrecy.setStatus("current")
_SlcNetVPNModeConfigClient_Type = EnabledState
_SlcNetVPNModeConfigClient_Object = MibScalar
slcNetVPNModeConfigClient = _SlcNetVPNModeConfigClient_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 21),
    _SlcNetVPNModeConfigClient_Type()
)
slcNetVPNModeConfigClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNModeConfigClient.setStatus("current")
_SlcNetVPNXAUTHClient_Type = EnabledState
_SlcNetVPNXAUTHClient_Object = MibScalar
slcNetVPNXAUTHClient = _SlcNetVPNXAUTHClient_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 22),
    _SlcNetVPNXAUTHClient_Type()
)
slcNetVPNXAUTHClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNXAUTHClient.setStatus("current")
_SlcNetVPNXAUTHClientLogin_Type = OctetString
_SlcNetVPNXAUTHClientLogin_Object = MibScalar
slcNetVPNXAUTHClientLogin = _SlcNetVPNXAUTHClientLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 4, 23),
    _SlcNetVPNXAUTHClientLogin_Type()
)
slcNetVPNXAUTHClientLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetVPNXAUTHClientLogin.setStatus("current")
_SlcNetSecurity_ObjectIdentity = ObjectIdentity
slcNetSecurity = _SlcNetSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 5)
)
_SlcNetSecurityFIPSMode_Type = EnabledState
_SlcNetSecurityFIPSMode_Object = MibScalar
slcNetSecurityFIPSMode = _SlcNetSecurityFIPSMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 1, 5, 1),
    _SlcNetSecurityFIPSMode_Type()
)
slcNetSecurityFIPSMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcNetSecurityFIPSMode.setStatus("current")
_SlcServices_ObjectIdentity = ObjectIdentity
slcServices = _SlcServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2)
)
_SlcServNTP_ObjectIdentity = ObjectIdentity
slcServNTP = _SlcServNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1)
)
_SlcServNTPState_Type = EnabledState
_SlcServNTPState_Object = MibScalar
slcServNTPState = _SlcServNTPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 1),
    _SlcServNTPState_Type()
)
slcServNTPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPState.setStatus("current")


class _SlcServNTPSynchronize_Type(Integer32):
    """Custom type slcServNTPSynchronize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("poll", 2))
    )


_SlcServNTPSynchronize_Type.__name__ = "Integer32"
_SlcServNTPSynchronize_Object = MibScalar
slcServNTPSynchronize = _SlcServNTPSynchronize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 2),
    _SlcServNTPSynchronize_Type()
)
slcServNTPSynchronize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPSynchronize.setStatus("current")


class _SlcServNTPPoll_Type(Integer32):
    """Custom type slcServNTPPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("public", 2))
    )


_SlcServNTPPoll_Type.__name__ = "Integer32"
_SlcServNTPPoll_Object = MibScalar
slcServNTPPoll = _SlcServNTPPoll_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 3),
    _SlcServNTPPoll_Type()
)
slcServNTPPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPPoll.setStatus("current")
_SlcServNTPServer_Type = IpAddress
_SlcServNTPServer_Object = MibScalar
slcServNTPServer = _SlcServNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 4),
    _SlcServNTPServer_Type()
)
slcServNTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPServer.setStatus("current")
_SlcServNTPLocalServer2_Type = IpAddress
_SlcServNTPLocalServer2_Object = MibScalar
slcServNTPLocalServer2 = _SlcServNTPLocalServer2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 5),
    _SlcServNTPLocalServer2_Type()
)
slcServNTPLocalServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPLocalServer2.setStatus("current")
_SlcServNTPLocalServer3_Type = IpAddress
_SlcServNTPLocalServer3_Object = MibScalar
slcServNTPLocalServer3 = _SlcServNTPLocalServer3_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 6),
    _SlcServNTPLocalServer3_Type()
)
slcServNTPLocalServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPLocalServer3.setStatus("current")
_SlcServNTPServerIPv6_Type = Ipv6Address
_SlcServNTPServerIPv6_Object = MibScalar
slcServNTPServerIPv6 = _SlcServNTPServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 7),
    _SlcServNTPServerIPv6_Type()
)
slcServNTPServerIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPServerIPv6.setStatus("current")
_SlcServNTPLocalServer2IPv6_Type = Ipv6Address
_SlcServNTPLocalServer2IPv6_Object = MibScalar
slcServNTPLocalServer2IPv6 = _SlcServNTPLocalServer2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 8),
    _SlcServNTPLocalServer2IPv6_Type()
)
slcServNTPLocalServer2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPLocalServer2IPv6.setStatus("current")
_SlcServNTPLocalServer3IPv6_Type = Ipv6Address
_SlcServNTPLocalServer3IPv6_Object = MibScalar
slcServNTPLocalServer3IPv6 = _SlcServNTPLocalServer3IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 1, 9),
    _SlcServNTPLocalServer3IPv6_Type()
)
slcServNTPLocalServer3IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNTPLocalServer3IPv6.setStatus("current")
_SlcServSyslog_ObjectIdentity = ObjectIdentity
slcServSyslog = _SlcServSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2)
)
_SlcServSysNetworkLevel_Type = SyslogLevel
_SlcServSysNetworkLevel_Object = MibScalar
slcServSysNetworkLevel = _SlcServSysNetworkLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 1),
    _SlcServSysNetworkLevel_Type()
)
slcServSysNetworkLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysNetworkLevel.setStatus("current")
_SlcServSysServicesLevel_Type = SyslogLevel
_SlcServSysServicesLevel_Object = MibScalar
slcServSysServicesLevel = _SlcServSysServicesLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 2),
    _SlcServSysServicesLevel_Type()
)
slcServSysServicesLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysServicesLevel.setStatus("current")
_SlcServSysAuthLevel_Type = SyslogLevel
_SlcServSysAuthLevel_Object = MibScalar
slcServSysAuthLevel = _SlcServSysAuthLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 3),
    _SlcServSysAuthLevel_Type()
)
slcServSysAuthLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysAuthLevel.setStatus("current")
_SlcServSysDevPortLevel_Type = SyslogLevel
_SlcServSysDevPortLevel_Object = MibScalar
slcServSysDevPortLevel = _SlcServSysDevPortLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 4),
    _SlcServSysDevPortLevel_Type()
)
slcServSysDevPortLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysDevPortLevel.setStatus("current")
_SlcServSysDiagLevel_Type = SyslogLevel
_SlcServSysDiagLevel_Object = MibScalar
slcServSysDiagLevel = _SlcServSysDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 5),
    _SlcServSysDiagLevel_Type()
)
slcServSysDiagLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysDiagLevel.setStatus("current")
_SlcServSysGeneralLevel_Type = SyslogLevel
_SlcServSysGeneralLevel_Object = MibScalar
slcServSysGeneralLevel = _SlcServSysGeneralLevel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 6),
    _SlcServSysGeneralLevel_Type()
)
slcServSysGeneralLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysGeneralLevel.setStatus("current")
_SlcServSysRemoteServer_Type = IpAddress
_SlcServSysRemoteServer_Object = MibScalar
slcServSysRemoteServer = _SlcServSysRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 7),
    _SlcServSysRemoteServer_Type()
)
slcServSysRemoteServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysRemoteServer.setStatus("current")
_SlcServSysRemoteServer2_Type = IpAddress
_SlcServSysRemoteServer2_Object = MibScalar
slcServSysRemoteServer2 = _SlcServSysRemoteServer2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 8),
    _SlcServSysRemoteServer2_Type()
)
slcServSysRemoteServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysRemoteServer2.setStatus("current")
_SlcServSysRemoteServerIPv6_Type = Ipv6Address
_SlcServSysRemoteServerIPv6_Object = MibScalar
slcServSysRemoteServerIPv6 = _SlcServSysRemoteServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 9),
    _SlcServSysRemoteServerIPv6_Type()
)
slcServSysRemoteServerIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysRemoteServerIPv6.setStatus("current")
_SlcServSysRemoteServer2IPv6_Type = Ipv6Address
_SlcServSysRemoteServer2IPv6_Object = MibScalar
slcServSysRemoteServer2IPv6 = _SlcServSysRemoteServer2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 10),
    _SlcServSysRemoteServer2IPv6_Type()
)
slcServSysRemoteServer2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysRemoteServer2IPv6.setStatus("current")


class _SlcServSysRPMLogSize_Type(Integer32):
    """Custom type slcServSysRPMLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_SlcServSysRPMLogSize_Type.__name__ = "Integer32"
_SlcServSysRPMLogSize_Object = MibScalar
slcServSysRPMLogSize = _SlcServSysRPMLogSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 11),
    _SlcServSysRPMLogSize_Type()
)
slcServSysRPMLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysRPMLogSize.setStatus("current")
if mibBuilder.loadTexts:
    slcServSysRPMLogSize.setUnits("Kilobytes")


class _SlcServSysOtherLogSize_Type(Integer32):
    """Custom type slcServSysOtherLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_SlcServSysOtherLogSize_Type.__name__ = "Integer32"
_SlcServSysOtherLogSize_Object = MibScalar
slcServSysOtherLogSize = _SlcServSysOtherLogSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 2, 12),
    _SlcServSysOtherLogSize_Type()
)
slcServSysOtherLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSysOtherLogSize.setStatus("current")
if mibBuilder.loadTexts:
    slcServSysOtherLogSize.setUnits("Kilobytes")
_SlcServAuditLog_ObjectIdentity = ObjectIdentity
slcServAuditLog = _SlcServAuditLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 3)
)
_SlcServAuditState_Type = EnabledState
_SlcServAuditState_Object = MibScalar
slcServAuditState = _SlcServAuditState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 3, 1),
    _SlcServAuditState_Type()
)
slcServAuditState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServAuditState.setStatus("current")


class _SlcServAuditSize_Type(Integer32):
    """Custom type slcServAuditSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_SlcServAuditSize_Type.__name__ = "Integer32"
_SlcServAuditSize_Object = MibScalar
slcServAuditSize = _SlcServAuditSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 3, 2),
    _SlcServAuditSize_Type()
)
slcServAuditSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServAuditSize.setStatus("current")
if mibBuilder.loadTexts:
    slcServAuditSize.setUnits("Kilobytes")
_SlcServAuditIncludeCLI_Type = EnabledState
_SlcServAuditIncludeCLI_Object = MibScalar
slcServAuditIncludeCLI = _SlcServAuditIncludeCLI_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 3, 3),
    _SlcServAuditIncludeCLI_Type()
)
slcServAuditIncludeCLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServAuditIncludeCLI.setStatus("current")
_SlcServAuditInSystemLog_Type = EnabledState
_SlcServAuditInSystemLog_Object = MibScalar
slcServAuditInSystemLog = _SlcServAuditInSystemLog_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 3, 4),
    _SlcServAuditInSystemLog_Type()
)
slcServAuditInSystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServAuditInSystemLog.setStatus("current")
_SlcServSSH_ObjectIdentity = ObjectIdentity
slcServSSH = _SlcServSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4)
)
_SlcServSSHState_Type = EnabledState
_SlcServSSHState_Object = MibScalar
slcServSSHState = _SlcServSSHState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 1),
    _SlcServSSHState_Type()
)
slcServSSHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHState.setStatus("current")


class _SlcServSSHTimeout_Type(Integer32):
    """Custom type slcServSSHTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcServSSHTimeout_Type.__name__ = "Integer32"
_SlcServSSHTimeout_Object = MibScalar
slcServSSHTimeout = _SlcServSSHTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 2),
    _SlcServSSHTimeout_Type()
)
slcServSSHTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcServSSHTimeout.setUnits("minutes")
_SlcServSSHWebSSH_Type = EnabledState
_SlcServSSHWebSSH_Object = MibScalar
slcServSSHWebSSH = _SlcServSSHWebSSH_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 3),
    _SlcServSSHWebSSH_Type()
)
slcServSSHWebSSH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHWebSSH.setStatus("current")


class _SlcServSSHPort_Type(Integer32):
    """Custom type slcServSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcServSSHPort_Type.__name__ = "Integer32"
_SlcServSSHPort_Object = MibScalar
slcServSSHPort = _SlcServSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 4),
    _SlcServSSHPort_Type()
)
slcServSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHPort.setStatus("current")
_SlcServSSHV1Incoming_Type = EnabledState
_SlcServSSHV1Incoming_Object = MibScalar
slcServSSHV1Incoming = _SlcServSSHV1Incoming_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 5),
    _SlcServSSHV1Incoming_Type()
)
slcServSSHV1Incoming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHV1Incoming.setStatus("current")
_SlcServSSHTimeoutDataDirection_Type = TimeoutDataDirection
_SlcServSSHTimeoutDataDirection_Object = MibScalar
slcServSSHTimeoutDataDirection = _SlcServSSHTimeoutDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 6),
    _SlcServSSHTimeoutDataDirection_Type()
)
slcServSSHTimeoutDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHTimeoutDataDirection.setStatus("current")
_SlcServSSHDSAKeys_Type = EnabledState
_SlcServSSHDSAKeys_Object = MibScalar
slcServSSHDSAKeys = _SlcServSSHDSAKeys_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 4, 7),
    _SlcServSSHDSAKeys_Type()
)
slcServSSHDSAKeys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSSHDSAKeys.setStatus("current")
_SlcServTelnet_ObjectIdentity = ObjectIdentity
slcServTelnet = _SlcServTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5)
)
_SlcServTelnetState_Type = EnabledState
_SlcServTelnetState_Object = MibScalar
slcServTelnetState = _SlcServTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5, 1),
    _SlcServTelnetState_Type()
)
slcServTelnetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServTelnetState.setStatus("current")


class _SlcServTelnetTimeout_Type(Integer32):
    """Custom type slcServTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcServTelnetTimeout_Type.__name__ = "Integer32"
_SlcServTelnetTimeout_Object = MibScalar
slcServTelnetTimeout = _SlcServTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5, 2),
    _SlcServTelnetTimeout_Type()
)
slcServTelnetTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServTelnetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcServTelnetTimeout.setUnits("minutes")
_SlcServTelnetWebTelnet_Type = EnabledState
_SlcServTelnetWebTelnet_Object = MibScalar
slcServTelnetWebTelnet = _SlcServTelnetWebTelnet_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5, 3),
    _SlcServTelnetWebTelnet_Type()
)
slcServTelnetWebTelnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServTelnetWebTelnet.setStatus("current")
_SlcServTelnetTelnetOut_Type = EnabledState
_SlcServTelnetTelnetOut_Object = MibScalar
slcServTelnetTelnetOut = _SlcServTelnetTelnetOut_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5, 4),
    _SlcServTelnetTelnetOut_Type()
)
slcServTelnetTelnetOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServTelnetTelnetOut.setStatus("current")
_SlcServTelnetTimeoutDataDirection_Type = TimeoutDataDirection
_SlcServTelnetTimeoutDataDirection_Object = MibScalar
slcServTelnetTimeoutDataDirection = _SlcServTelnetTimeoutDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 5, 5),
    _SlcServTelnetTimeoutDataDirection_Type()
)
slcServTelnetTimeoutDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServTelnetTimeoutDataDirection.setStatus("current")
_SlcServSNMP_ObjectIdentity = ObjectIdentity
slcServSNMP = _SlcServSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6)
)
_SlcServSNMPState_Type = EnabledState
_SlcServSNMPState_Object = MibScalar
slcServSNMPState = _SlcServSNMPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 1),
    _SlcServSNMPState_Type()
)
slcServSNMPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPState.setStatus("current")
_SlcServSNMPTraps_Type = EnabledState
_SlcServSNMPTraps_Object = MibScalar
slcServSNMPTraps = _SlcServSNMPTraps_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 2),
    _SlcServSNMPTraps_Type()
)
slcServSNMPTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPTraps.setStatus("current")
_SlcServSNMPNMS_Type = IpAddress
_SlcServSNMPNMS_Object = MibScalar
slcServSNMPNMS = _SlcServSNMPNMS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 3),
    _SlcServSNMPNMS_Type()
)
slcServSNMPNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPNMS.setStatus("current")
_SlcServSNMPLocation_Type = OctetString
_SlcServSNMPLocation_Object = MibScalar
slcServSNMPLocation = _SlcServSNMPLocation_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 4),
    _SlcServSNMPLocation_Type()
)
slcServSNMPLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPLocation.setStatus("current")
_SlcServSNMPContact_Type = OctetString
_SlcServSNMPContact_Object = MibScalar
slcServSNMPContact = _SlcServSNMPContact_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 5),
    _SlcServSNMPContact_Type()
)
slcServSNMPContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPContact.setStatus("current")


class _SlcServSNMPv3User_Type(OctetString):
    """Custom type slcServSNMPv3User based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcServSNMPv3User_Type.__name__ = "OctetString"
_SlcServSNMPv3User_Object = MibScalar
slcServSNMPv3User = _SlcServSNMPv3User_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 6),
    _SlcServSNMPv3User_Type()
)
slcServSNMPv3User.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv3User.setStatus("current")
_SlcServSNMPReadOnlyCommunity_Type = OctetString
_SlcServSNMPReadOnlyCommunity_Object = MibScalar
slcServSNMPReadOnlyCommunity = _SlcServSNMPReadOnlyCommunity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 7),
    _SlcServSNMPReadOnlyCommunity_Type()
)
slcServSNMPReadOnlyCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPReadOnlyCommunity.setStatus("current")
_SlcServSNMPReadWriteCommunity_Type = OctetString
_SlcServSNMPReadWriteCommunity_Object = MibScalar
slcServSNMPReadWriteCommunity = _SlcServSNMPReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 8),
    _SlcServSNMPReadWriteCommunity_Type()
)
slcServSNMPReadWriteCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPReadWriteCommunity.setStatus("current")
_SlcServSNMPTrapCommunity_Type = OctetString
_SlcServSNMPTrapCommunity_Object = MibScalar
slcServSNMPTrapCommunity = _SlcServSNMPTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 9),
    _SlcServSNMPTrapCommunity_Type()
)
slcServSNMPTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPTrapCommunity.setStatus("current")
_SlcServSNMPAlarmDelay_Type = Integer32
_SlcServSNMPAlarmDelay_Object = MibScalar
slcServSNMPAlarmDelay = _SlcServSNMPAlarmDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 10),
    _SlcServSNMPAlarmDelay_Type()
)
slcServSNMPAlarmDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPAlarmDelay.setStatus("current")


class _SlcServSNMPv3ReadWriteUser_Type(OctetString):
    """Custom type slcServSNMPv3ReadWriteUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcServSNMPv3ReadWriteUser_Type.__name__ = "OctetString"
_SlcServSNMPv3ReadWriteUser_Object = MibScalar
slcServSNMPv3ReadWriteUser = _SlcServSNMPv3ReadWriteUser_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 11),
    _SlcServSNMPv3ReadWriteUser_Type()
)
slcServSNMPv3ReadWriteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv3ReadWriteUser.setStatus("current")


class _SlcServSNMPv3Security_Type(Integer32):
    """Custom type slcServSNMPv3Security based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authEncrypt", 3),
          ("authNoEncrypt", 2),
          ("noAuthNoEncrypt", 1))
    )


_SlcServSNMPv3Security_Type.__name__ = "Integer32"
_SlcServSNMPv3Security_Object = MibScalar
slcServSNMPv3Security = _SlcServSNMPv3Security_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 12),
    _SlcServSNMPv3Security_Type()
)
slcServSNMPv3Security.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv3Security.setStatus("current")


class _SlcServSNMPv3Authentication_Type(Integer32):
    """Custom type slcServSNMPv3Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 1),
          ("sha", 2))
    )


_SlcServSNMPv3Authentication_Type.__name__ = "Integer32"
_SlcServSNMPv3Authentication_Object = MibScalar
slcServSNMPv3Authentication = _SlcServSNMPv3Authentication_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 13),
    _SlcServSNMPv3Authentication_Type()
)
slcServSNMPv3Authentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv3Authentication.setStatus("current")


class _SlcServSNMPv3Encryption_Type(Integer32):
    """Custom type slcServSNMPv3Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("des", 1))
    )


_SlcServSNMPv3Encryption_Type.__name__ = "Integer32"
_SlcServSNMPv3Encryption_Object = MibScalar
slcServSNMPv3Encryption = _SlcServSNMPv3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 14),
    _SlcServSNMPv3Encryption_Type()
)
slcServSNMPv3Encryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv3Encryption.setStatus("current")
_SlcServSNMPv1v2_Type = EnabledState
_SlcServSNMPv1v2_Object = MibScalar
slcServSNMPv1v2 = _SlcServSNMPv1v2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 15),
    _SlcServSNMPv1v2_Type()
)
slcServSNMPv1v2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPv1v2.setStatus("current")
_SlcServSNMPNMS2_Type = IpAddress
_SlcServSNMPNMS2_Object = MibScalar
slcServSNMPNMS2 = _SlcServSNMPNMS2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 16),
    _SlcServSNMPNMS2_Type()
)
slcServSNMPNMS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPNMS2.setStatus("current")
_SlcServSNMPNMSIPv6_Type = Ipv6Address
_SlcServSNMPNMSIPv6_Object = MibScalar
slcServSNMPNMSIPv6 = _SlcServSNMPNMSIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 17),
    _SlcServSNMPNMSIPv6_Type()
)
slcServSNMPNMSIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPNMSIPv6.setStatus("current")
_SlcServSNMPNMS2IPv6_Type = Ipv6Address
_SlcServSNMPNMS2IPv6_Object = MibScalar
slcServSNMPNMS2IPv6 = _SlcServSNMPNMS2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 6, 18),
    _SlcServSNMPNMS2IPv6_Type()
)
slcServSNMPNMS2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSNMPNMS2IPv6.setStatus("current")
_SlcServSMTP_ObjectIdentity = ObjectIdentity
slcServSMTP = _SlcServSMTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 7)
)
_SlcServSMTPServer_Type = IpAddress
_SlcServSMTPServer_Object = MibScalar
slcServSMTPServer = _SlcServSMTPServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 7, 1),
    _SlcServSMTPServer_Type()
)
slcServSMTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSMTPServer.setStatus("current")
_SlcServSMTPSender_Type = OctetString
_SlcServSMTPSender_Object = MibScalar
slcServSMTPSender = _SlcServSMTPSender_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 7, 2),
    _SlcServSMTPSender_Type()
)
slcServSMTPSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSMTPSender.setStatus("current")
_SlcServNFS_ObjectIdentity = ObjectIdentity
slcServNFS = _SlcServNFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8)
)
_SlcServNFSMountTable_Object = MibTable
slcServNFSMountTable = _SlcServNFSMountTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    slcServNFSMountTable.setStatus("current")
_SlcServNFSMountEntry_Object = MibTableRow
slcServNFSMountEntry = _SlcServNFSMountEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1)
)
slcServNFSMountEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcServNFSMountIndex"),
)
if mibBuilder.loadTexts:
    slcServNFSMountEntry.setStatus("current")


class _SlcServNFSMountIndex_Type(Integer32):
    """Custom type slcServNFSMountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SlcServNFSMountIndex_Type.__name__ = "Integer32"
_SlcServNFSMountIndex_Object = MibTableColumn
slcServNFSMountIndex = _SlcServNFSMountIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1, 1),
    _SlcServNFSMountIndex_Type()
)
slcServNFSMountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNFSMountIndex.setStatus("current")
_SlcServNFSMountRemoteDir_Type = OctetString
_SlcServNFSMountRemoteDir_Object = MibTableColumn
slcServNFSMountRemoteDir = _SlcServNFSMountRemoteDir_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1, 2),
    _SlcServNFSMountRemoteDir_Type()
)
slcServNFSMountRemoteDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNFSMountRemoteDir.setStatus("current")
_SlcServNFSMountLocalDir_Type = OctetString
_SlcServNFSMountLocalDir_Object = MibTableColumn
slcServNFSMountLocalDir = _SlcServNFSMountLocalDir_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1, 3),
    _SlcServNFSMountLocalDir_Type()
)
slcServNFSMountLocalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNFSMountLocalDir.setStatus("current")
_SlcServNFSMountReadWrite_Type = EnabledState
_SlcServNFSMountReadWrite_Object = MibTableColumn
slcServNFSMountReadWrite = _SlcServNFSMountReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1, 4),
    _SlcServNFSMountReadWrite_Type()
)
slcServNFSMountReadWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNFSMountReadWrite.setStatus("current")
_SlcServNFSMountMount_Type = EnabledState
_SlcServNFSMountMount_Object = MibTableColumn
slcServNFSMountMount = _SlcServNFSMountMount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 8, 1, 1, 5),
    _SlcServNFSMountMount_Type()
)
slcServNFSMountMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServNFSMountMount.setStatus("current")
_SlcServCIFS_ObjectIdentity = ObjectIdentity
slcServCIFS = _SlcServCIFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 9)
)
_SlcServCIFSState_Type = EnabledState
_SlcServCIFSState_Object = MibScalar
slcServCIFSState = _SlcServCIFSState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 9, 1),
    _SlcServCIFSState_Type()
)
slcServCIFSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServCIFSState.setStatus("current")
_SlcServCIFSEth1_Type = EnabledState
_SlcServCIFSEth1_Object = MibScalar
slcServCIFSEth1 = _SlcServCIFSEth1_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 9, 2),
    _SlcServCIFSEth1_Type()
)
slcServCIFSEth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServCIFSEth1.setStatus("current")
_SlcServCIFSEth2_Type = EnabledState
_SlcServCIFSEth2_Object = MibScalar
slcServCIFSEth2 = _SlcServCIFSEth2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 9, 3),
    _SlcServCIFSEth2_Type()
)
slcServCIFSEth2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServCIFSEth2.setStatus("current")


class _SlcServCIFSWorkgroup_Type(OctetString):
    """Custom type slcServCIFSWorkgroup based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SlcServCIFSWorkgroup_Type.__name__ = "OctetString"
_SlcServCIFSWorkgroup_Object = MibScalar
slcServCIFSWorkgroup = _SlcServCIFSWorkgroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 9, 4),
    _SlcServCIFSWorkgroup_Type()
)
slcServCIFSWorkgroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServCIFSWorkgroup.setStatus("current")
_SlcServSLCNetwork_ObjectIdentity = ObjectIdentity
slcServSLCNetwork = _SlcServSLCNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10)
)


class _SlcServSLCNetSearch_Type(Integer32):
    """Custom type slcServSLCNetSearch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("manual", 3),
          ("subnet", 2))
    )


_SlcServSLCNetSearch_Type.__name__ = "Integer32"
_SlcServSLCNetSearch_Object = MibScalar
slcServSLCNetSearch = _SlcServSLCNetSearch_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 1),
    _SlcServSLCNetSearch_Type()
)
slcServSLCNetSearch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSLCNetSearch.setStatus("current")


class _SlcServSLCNetNumber_Type(Integer32):
    """Custom type slcServSLCNetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_SlcServSLCNetNumber_Type.__name__ = "Integer32"
_SlcServSLCNetNumber_Object = MibScalar
slcServSLCNetNumber = _SlcServSLCNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 2),
    _SlcServSLCNetNumber_Type()
)
slcServSLCNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSLCNetNumber.setStatus("current")
_SlcServSLCNetTable_Object = MibTable
slcServSLCNetTable = _SlcServSLCNetTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    slcServSLCNetTable.setStatus("current")
_SlcServSLCNetEntry_Object = MibTableRow
slcServSLCNetEntry = _SlcServSLCNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 3, 1)
)
slcServSLCNetEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcServSLCNetIndex"),
)
if mibBuilder.loadTexts:
    slcServSLCNetEntry.setStatus("current")


class _SlcServSLCNetIndex_Type(Integer32):
    """Custom type slcServSLCNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_SlcServSLCNetIndex_Type.__name__ = "Integer32"
_SlcServSLCNetIndex_Object = MibTableColumn
slcServSLCNetIndex = _SlcServSLCNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 3, 1, 1),
    _SlcServSLCNetIndex_Type()
)
slcServSLCNetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSLCNetIndex.setStatus("current")
_SlcServSLCNetIP_Type = IpAddress
_SlcServSLCNetIP_Object = MibTableColumn
slcServSLCNetIP = _SlcServSLCNetIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 10, 3, 1, 2),
    _SlcServSLCNetIP_Type()
)
slcServSLCNetIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSLCNetIP.setStatus("current")
_SlcServPhoneHome_ObjectIdentity = ObjectIdentity
slcServPhoneHome = _SlcServPhoneHome_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 11)
)
_SlcServPhoneHomeState_Type = EnabledState
_SlcServPhoneHomeState_Object = MibScalar
slcServPhoneHomeState = _SlcServPhoneHomeState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 11, 1),
    _SlcServPhoneHomeState_Type()
)
slcServPhoneHomeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServPhoneHomeState.setStatus("current")
_SlcServPhoneHomeIP_Type = IpAddress
_SlcServPhoneHomeIP_Object = MibScalar
slcServPhoneHomeIP = _SlcServPhoneHomeIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 11, 2),
    _SlcServPhoneHomeIP_Type()
)
slcServPhoneHomeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServPhoneHomeIP.setStatus("current")
_SlcServHostList_ObjectIdentity = ObjectIdentity
slcServHostList = _SlcServHostList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12)
)


class _SlcServHostListNumber_Type(Integer32):
    """Custom type slcServHostListNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SlcServHostListNumber_Type.__name__ = "Integer32"
_SlcServHostListNumber_Object = MibScalar
slcServHostListNumber = _SlcServHostListNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 1),
    _SlcServHostListNumber_Type()
)
slcServHostListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListNumber.setStatus("current")
_SlcServHostListTable_Object = MibTable
slcServHostListTable = _SlcServHostListTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    slcServHostListTable.setStatus("current")
_SlcServHostListEntry_Object = MibTableRow
slcServHostListEntry = _SlcServHostListEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1)
)
slcServHostListEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcServHostListIndex"),
)
if mibBuilder.loadTexts:
    slcServHostListEntry.setStatus("current")


class _SlcServHostListIndex_Type(Integer32):
    """Custom type slcServHostListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SlcServHostListIndex_Type.__name__ = "Integer32"
_SlcServHostListIndex_Object = MibTableColumn
slcServHostListIndex = _SlcServHostListIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 1),
    _SlcServHostListIndex_Type()
)
slcServHostListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListIndex.setStatus("current")
_SlcServHostListName_Type = OctetString
_SlcServHostListName_Object = MibTableColumn
slcServHostListName = _SlcServHostListName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 2),
    _SlcServHostListName_Type()
)
slcServHostListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListName.setStatus("current")
_SlcServHostListRetryCount_Type = Integer32
_SlcServHostListRetryCount_Object = MibTableColumn
slcServHostListRetryCount = _SlcServHostListRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 3),
    _SlcServHostListRetryCount_Type()
)
slcServHostListRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListRetryCount.setStatus("current")
_SlcServHostListAuth_Type = EnabledState
_SlcServHostListAuth_Object = MibTableColumn
slcServHostListAuth = _SlcServHostListAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 4),
    _SlcServHostListAuth_Type()
)
slcServHostListAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListAuth.setStatus("current")


class _SlcServHostListNumHosts_Type(Integer32):
    """Custom type slcServHostListNumHosts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlcServHostListNumHosts_Type.__name__ = "Integer32"
_SlcServHostListNumHosts_Object = MibTableColumn
slcServHostListNumHosts = _SlcServHostListNumHosts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 5),
    _SlcServHostListNumHosts_Type()
)
slcServHostListNumHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListNumHosts.setStatus("current")
_SlcServHostListHosts_Type = OctetString
_SlcServHostListHosts_Object = MibTableColumn
slcServHostListHosts = _SlcServHostListHosts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 12, 2, 1, 6),
    _SlcServHostListHosts_Type()
)
slcServHostListHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServHostListHosts.setStatus("current")
_SlcServWebTerm_ObjectIdentity = ObjectIdentity
slcServWebTerm = _SlcServWebTerm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 13)
)


class _SlcServWebTermDeployment_Type(Integer32):
    """Custom type slcServWebTermDeployment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("applet", 2),
          ("javaWebStart", 1))
    )


_SlcServWebTermDeployment_Type.__name__ = "Integer32"
_SlcServWebTermDeployment_Object = MibScalar
slcServWebTermDeployment = _SlcServWebTermDeployment_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 13, 1),
    _SlcServWebTermDeployment_Type()
)
slcServWebTermDeployment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServWebTermDeployment.setStatus("current")


class _SlcServWebTermBufSize_Type(Integer32):
    """Custom type slcServWebTermBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 5000),
    )


_SlcServWebTermBufSize_Type.__name__ = "Integer32"
_SlcServWebTermBufSize_Object = MibScalar
slcServWebTermBufSize = _SlcServWebTermBufSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 13, 2),
    _SlcServWebTermBufSize_Type()
)
slcServWebTermBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServWebTermBufSize.setStatus("current")
_SlcServSite_ObjectIdentity = ObjectIdentity
slcServSite = _SlcServSite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14)
)


class _SlcServSiteNumber_Type(Integer32):
    """Custom type slcServSiteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SlcServSiteNumber_Type.__name__ = "Integer32"
_SlcServSiteNumber_Object = MibScalar
slcServSiteNumber = _SlcServSiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 1),
    _SlcServSiteNumber_Type()
)
slcServSiteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteNumber.setStatus("current")
_SlcServSiteTable_Object = MibTable
slcServSiteTable = _SlcServSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    slcServSiteTable.setStatus("current")
_SlcServSiteEntry_Object = MibTableRow
slcServSiteEntry = _SlcServSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1)
)
slcServSiteEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcServSiteIndex"),
)
if mibBuilder.loadTexts:
    slcServSiteEntry.setStatus("current")


class _SlcServSiteIndex_Type(Integer32):
    """Custom type slcServSiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SlcServSiteIndex_Type.__name__ = "Integer32"
_SlcServSiteIndex_Object = MibTableColumn
slcServSiteIndex = _SlcServSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 1),
    _SlcServSiteIndex_Type()
)
slcServSiteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteIndex.setStatus("current")
_SlcServSiteName_Type = OctetString
_SlcServSiteName_Object = MibTableColumn
slcServSiteName = _SlcServSiteName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 2),
    _SlcServSiteName_Type()
)
slcServSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteName.setStatus("current")


class _SlcServSitePort_Type(Integer32):
    """Custom type slcServSitePort based on Integer32"""
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
        *(("devicePort", 2),
          ("internalModem", 6),
          ("lowerPCCard", 4),
          ("none", 1),
          ("upperPCCard", 3),
          ("usbPort", 5))
    )


_SlcServSitePort_Type.__name__ = "Integer32"
_SlcServSitePort_Object = MibTableColumn
slcServSitePort = _SlcServSitePort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 3),
    _SlcServSitePort_Type()
)
slcServSitePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSitePort.setStatus("current")


class _SlcServSitePortId_Type(Integer32):
    """Custom type slcServSitePortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_SlcServSitePortId_Type.__name__ = "Integer32"
_SlcServSitePortId_Object = MibTableColumn
slcServSitePortId = _SlcServSitePortId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 4),
    _SlcServSitePortId_Type()
)
slcServSitePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSitePortId.setStatus("current")
_SlcServSiteLoginHost_Type = OctetString
_SlcServSiteLoginHost_Object = MibTableColumn
slcServSiteLoginHost = _SlcServSiteLoginHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 5),
    _SlcServSiteLoginHost_Type()
)
slcServSiteLoginHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteLoginHost.setStatus("current")
_SlcServSiteCHAPSecret_Type = OctetString
_SlcServSiteCHAPSecret_Object = MibTableColumn
slcServSiteCHAPSecret = _SlcServSiteCHAPSecret_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 6),
    _SlcServSiteCHAPSecret_Type()
)
slcServSiteCHAPSecret.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteCHAPSecret.setStatus("current")


class _SlcServSiteTimeout_Type(Integer32):
    """Custom type slcServSiteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcServSiteTimeout_Type.__name__ = "Integer32"
_SlcServSiteTimeout_Object = MibTableColumn
slcServSiteTimeout = _SlcServSiteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 7),
    _SlcServSiteTimeout_Type()
)
slcServSiteTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcServSiteTimeout.setUnits("minutes")
_SlcServSiteLocalIP_Type = IpAddress
_SlcServSiteLocalIP_Object = MibTableColumn
slcServSiteLocalIP = _SlcServSiteLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 8),
    _SlcServSiteLocalIP_Type()
)
slcServSiteLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteLocalIP.setStatus("current")
_SlcServSiteRemoteIP_Type = IpAddress
_SlcServSiteRemoteIP_Object = MibTableColumn
slcServSiteRemoteIP = _SlcServSiteRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 9),
    _SlcServSiteRemoteIP_Type()
)
slcServSiteRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteRemoteIP.setStatus("current")
_SlcServSiteStaticRouteIP_Type = IpAddress
_SlcServSiteStaticRouteIP_Object = MibTableColumn
slcServSiteStaticRouteIP = _SlcServSiteStaticRouteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 10),
    _SlcServSiteStaticRouteIP_Type()
)
slcServSiteStaticRouteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteStaticRouteIP.setStatus("current")
_SlcServSiteStaticRouteMask_Type = IpAddress
_SlcServSiteStaticRouteMask_Object = MibTableColumn
slcServSiteStaticRouteMask = _SlcServSiteStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 11),
    _SlcServSiteStaticRouteMask_Type()
)
slcServSiteStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteStaticRouteMask.setStatus("current")
_SlcServSiteStaticRouteGateway_Type = IpAddress
_SlcServSiteStaticRouteGateway_Object = MibTableColumn
slcServSiteStaticRouteGateway = _SlcServSiteStaticRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 12),
    _SlcServSiteStaticRouteGateway_Type()
)
slcServSiteStaticRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteStaticRouteGateway.setStatus("current")
_SlcServSiteDialoutNum_Type = OctetString
_SlcServSiteDialoutNum_Object = MibTableColumn
slcServSiteDialoutNum = _SlcServSiteDialoutNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 13),
    _SlcServSiteDialoutNum_Type()
)
slcServSiteDialoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialoutNum.setStatus("current")


class _SlcServSiteDialoutLogin_Type(OctetString):
    """Custom type slcServSiteDialoutLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcServSiteDialoutLogin_Type.__name__ = "OctetString"
_SlcServSiteDialoutLogin_Object = MibTableColumn
slcServSiteDialoutLogin = _SlcServSiteDialoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 14),
    _SlcServSiteDialoutLogin_Type()
)
slcServSiteDialoutLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialoutLogin.setStatus("current")
_SlcServSiteDialback_Type = EnabledState
_SlcServSiteDialback_Object = MibTableColumn
slcServSiteDialback = _SlcServSiteDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 15),
    _SlcServSiteDialback_Type()
)
slcServSiteDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialback.setStatus("current")
_SlcServSiteDialbackNum_Type = OctetString
_SlcServSiteDialbackNum_Object = MibTableColumn
slcServSiteDialbackNum = _SlcServSiteDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 16),
    _SlcServSiteDialbackNum_Type()
)
slcServSiteDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialbackNum.setStatus("current")
_SlcServSiteDialbackDelay_Type = Integer32
_SlcServSiteDialbackDelay_Object = MibTableColumn
slcServSiteDialbackDelay = _SlcServSiteDialbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 17),
    _SlcServSiteDialbackDelay_Type()
)
slcServSiteDialbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcServSiteDialbackDelay.setUnits("seconds")
_SlcServSiteIdleTimeout_Type = Integer32
_SlcServSiteIdleTimeout_Object = MibTableColumn
slcServSiteIdleTimeout = _SlcServSiteIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 18),
    _SlcServSiteIdleTimeout_Type()
)
slcServSiteIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcServSiteIdleTimeout.setUnits("seconds")
_SlcServSiteRestartDelay_Type = Integer32
_SlcServSiteRestartDelay_Object = MibTableColumn
slcServSiteRestartDelay = _SlcServSiteRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 19),
    _SlcServSiteRestartDelay_Type()
)
slcServSiteRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcServSiteRestartDelay.setUnits("seconds")
_SlcServSiteCBCPServerAllowNoCallback_Type = EnabledState
_SlcServSiteCBCPServerAllowNoCallback_Object = MibTableColumn
slcServSiteCBCPServerAllowNoCallback = _SlcServSiteCBCPServerAllowNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 20),
    _SlcServSiteCBCPServerAllowNoCallback_Type()
)
slcServSiteCBCPServerAllowNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteCBCPServerAllowNoCallback.setStatus("current")
_SlcServSiteNATState_Type = EnabledState
_SlcServSiteNATState_Object = MibTableColumn
slcServSiteNATState = _SlcServSiteNATState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 21),
    _SlcServSiteNATState_Type()
)
slcServSiteNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteNATState.setStatus("current")
_SlcServSiteDialbackRetries_Type = Integer32
_SlcServSiteDialbackRetries_Object = MibTableColumn
slcServSiteDialbackRetries = _SlcServSiteDialbackRetries_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 2, 14, 2, 1, 22),
    _SlcServSiteDialbackRetries_Type()
)
slcServSiteDialbackRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcServSiteDialbackRetries.setStatus("current")
_SlcAuth_ObjectIdentity = ObjectIdentity
slcAuth = _SlcAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3)
)
_SlcAuthLocal_ObjectIdentity = ObjectIdentity
slcAuthLocal = _SlcAuthLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1)
)


class _SlcAuthLocalNumber_Type(Integer32):
    """Custom type slcAuthLocalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlcAuthLocalNumber_Type.__name__ = "Integer32"
_SlcAuthLocalNumber_Object = MibScalar
slcAuthLocalNumber = _SlcAuthLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 1),
    _SlcAuthLocalNumber_Type()
)
slcAuthLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalNumber.setStatus("current")
_SlcAuthLocalUsersTable_Object = MibTable
slcAuthLocalUsersTable = _SlcAuthLocalUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    slcAuthLocalUsersTable.setStatus("current")
_SlcAuthLocalUserEntry_Object = MibTableRow
slcAuthLocalUserEntry = _SlcAuthLocalUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1)
)
slcAuthLocalUserEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcAuthLocalUserIndex"),
)
if mibBuilder.loadTexts:
    slcAuthLocalUserEntry.setStatus("current")


class _SlcAuthLocalUserIndex_Type(Integer32):
    """Custom type slcAuthLocalUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlcAuthLocalUserIndex_Type.__name__ = "Integer32"
_SlcAuthLocalUserIndex_Object = MibTableColumn
slcAuthLocalUserIndex = _SlcAuthLocalUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 1),
    _SlcAuthLocalUserIndex_Type()
)
slcAuthLocalUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserIndex.setStatus("current")


class _SlcAuthLocalUserLogin_Type(OctetString):
    """Custom type slcAuthLocalUserLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_SlcAuthLocalUserLogin_Type.__name__ = "OctetString"
_SlcAuthLocalUserLogin_Object = MibTableColumn
slcAuthLocalUserLogin = _SlcAuthLocalUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 2),
    _SlcAuthLocalUserLogin_Type()
)
slcAuthLocalUserLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserLogin.setStatus("current")
_SlcAuthLocalUserUID_Type = Unsigned32
_SlcAuthLocalUserUID_Object = MibTableColumn
slcAuthLocalUserUID = _SlcAuthLocalUserUID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 3),
    _SlcAuthLocalUserUID_Type()
)
slcAuthLocalUserUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserUID.setStatus("current")
_SlcAuthLocalUserListenPorts_Type = OctetString
_SlcAuthLocalUserListenPorts_Object = MibTableColumn
slcAuthLocalUserListenPorts = _SlcAuthLocalUserListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 4),
    _SlcAuthLocalUserListenPorts_Type()
)
slcAuthLocalUserListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserListenPorts.setStatus("current")
_SlcAuthLocalUserDataPorts_Type = OctetString
_SlcAuthLocalUserDataPorts_Object = MibTableColumn
slcAuthLocalUserDataPorts = _SlcAuthLocalUserDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 5),
    _SlcAuthLocalUserDataPorts_Type()
)
slcAuthLocalUserDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserDataPorts.setStatus("current")
_SlcAuthLocalUserClearPorts_Type = OctetString
_SlcAuthLocalUserClearPorts_Object = MibTableColumn
slcAuthLocalUserClearPorts = _SlcAuthLocalUserClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 6),
    _SlcAuthLocalUserClearPorts_Type()
)
slcAuthLocalUserClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserClearPorts.setStatus("current")
_SlcAuthLocalUserEscapeSeq_Type = OctetString
_SlcAuthLocalUserEscapeSeq_Object = MibTableColumn
slcAuthLocalUserEscapeSeq = _SlcAuthLocalUserEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 7),
    _SlcAuthLocalUserEscapeSeq_Type()
)
slcAuthLocalUserEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserEscapeSeq.setStatus("current")
_SlcAuthLocalUserBreakSeq_Type = OctetString
_SlcAuthLocalUserBreakSeq_Object = MibTableColumn
slcAuthLocalUserBreakSeq = _SlcAuthLocalUserBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 8),
    _SlcAuthLocalUserBreakSeq_Type()
)
slcAuthLocalUserBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserBreakSeq.setStatus("current")
_SlcAuthLocalUserMenu_Type = OctetString
_SlcAuthLocalUserMenu_Object = MibTableColumn
slcAuthLocalUserMenu = _SlcAuthLocalUserMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 9),
    _SlcAuthLocalUserMenu_Type()
)
slcAuthLocalUserMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserMenu.setStatus("current")
_SlcAuthLocalUserDialback_Type = EnabledState
_SlcAuthLocalUserDialback_Object = MibTableColumn
slcAuthLocalUserDialback = _SlcAuthLocalUserDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 10),
    _SlcAuthLocalUserDialback_Type()
)
slcAuthLocalUserDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserDialback.setStatus("current")
_SlcAuthLocalUserDialbackNum_Type = OctetString
_SlcAuthLocalUserDialbackNum_Object = MibTableColumn
slcAuthLocalUserDialbackNum = _SlcAuthLocalUserDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 11),
    _SlcAuthLocalUserDialbackNum_Type()
)
slcAuthLocalUserDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserDialbackNum.setStatus("current")
_SlcAuthLocalUserGroup_Type = UserGroup
_SlcAuthLocalUserGroup_Object = MibTableColumn
slcAuthLocalUserGroup = _SlcAuthLocalUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 12),
    _SlcAuthLocalUserGroup_Type()
)
slcAuthLocalUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserGroup.setStatus("current")
_SlcAuthLocalUserRights_Type = UserRights
_SlcAuthLocalUserRights_Object = MibTableColumn
slcAuthLocalUserRights = _SlcAuthLocalUserRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 13),
    _SlcAuthLocalUserRights_Type()
)
slcAuthLocalUserRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserRights.setStatus("current")
_SlcAuthLocalUserPwdExpires_Type = EnabledState
_SlcAuthLocalUserPwdExpires_Object = MibTableColumn
slcAuthLocalUserPwdExpires = _SlcAuthLocalUserPwdExpires_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 14),
    _SlcAuthLocalUserPwdExpires_Type()
)
slcAuthLocalUserPwdExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserPwdExpires.setStatus("current")
_SlcAuthLocalUserChangePwd_Type = EnabledState
_SlcAuthLocalUserChangePwd_Object = MibTableColumn
slcAuthLocalUserChangePwd = _SlcAuthLocalUserChangePwd_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 15),
    _SlcAuthLocalUserChangePwd_Type()
)
slcAuthLocalUserChangePwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserChangePwd.setStatus("current")
_SlcAuthLocalUserChangePwdNextLogin_Type = EnabledState
_SlcAuthLocalUserChangePwdNextLogin_Object = MibTableColumn
slcAuthLocalUserChangePwdNextLogin = _SlcAuthLocalUserChangePwdNextLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 2, 1, 16),
    _SlcAuthLocalUserChangePwdNextLogin_Type()
)
slcAuthLocalUserChangePwdNextLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUserChangePwdNextLogin.setStatus("current")
_SlcAuthLocalState_Type = EnabledState
_SlcAuthLocalState_Object = MibScalar
slcAuthLocalState = _SlcAuthLocalState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 3),
    _SlcAuthLocalState_Type()
)
slcAuthLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalState.setStatus("current")
_SlcAuthLocalOrder_Type = AuthOrder
_SlcAuthLocalOrder_Object = MibScalar
slcAuthLocalOrder = _SlcAuthLocalOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 4),
    _SlcAuthLocalOrder_Type()
)
slcAuthLocalOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalOrder.setStatus("current")
_SlcAuthLocalComplexPasswords_Type = EnabledState
_SlcAuthLocalComplexPasswords_Object = MibScalar
slcAuthLocalComplexPasswords = _SlcAuthLocalComplexPasswords_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 5),
    _SlcAuthLocalComplexPasswords_Type()
)
slcAuthLocalComplexPasswords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalComplexPasswords.setStatus("current")
_SlcAuthLocalUseNextMethod_Type = EnabledState
_SlcAuthLocalUseNextMethod_Object = MibScalar
slcAuthLocalUseNextMethod = _SlcAuthLocalUseNextMethod_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 6),
    _SlcAuthLocalUseNextMethod_Type()
)
slcAuthLocalUseNextMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalUseNextMethod.setStatus("current")
_SlcAuthLocalAllowReuse_Type = EnabledState
_SlcAuthLocalAllowReuse_Object = MibScalar
slcAuthLocalAllowReuse = _SlcAuthLocalAllowReuse_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 7),
    _SlcAuthLocalAllowReuse_Type()
)
slcAuthLocalAllowReuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalAllowReuse.setStatus("current")


class _SlcAuthLocalReuseHistory_Type(Integer32):
    """Custom type slcAuthLocalReuseHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SlcAuthLocalReuseHistory_Type.__name__ = "Integer32"
_SlcAuthLocalReuseHistory_Object = MibScalar
slcAuthLocalReuseHistory = _SlcAuthLocalReuseHistory_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 8),
    _SlcAuthLocalReuseHistory_Type()
)
slcAuthLocalReuseHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalReuseHistory.setStatus("current")


class _SlcAuthLocalPasswordLifetime_Type(Integer32):
    """Custom type slcAuthLocalPasswordLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 365),
    )


_SlcAuthLocalPasswordLifetime_Type.__name__ = "Integer32"
_SlcAuthLocalPasswordLifetime_Object = MibScalar
slcAuthLocalPasswordLifetime = _SlcAuthLocalPasswordLifetime_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 9),
    _SlcAuthLocalPasswordLifetime_Type()
)
slcAuthLocalPasswordLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalPasswordLifetime.setStatus("current")
if mibBuilder.loadTexts:
    slcAuthLocalPasswordLifetime.setUnits("days")


class _SlcAuthLocalWarningPeriod_Type(Integer32):
    """Custom type slcAuthLocalWarningPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_SlcAuthLocalWarningPeriod_Type.__name__ = "Integer32"
_SlcAuthLocalWarningPeriod_Object = MibScalar
slcAuthLocalWarningPeriod = _SlcAuthLocalWarningPeriod_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 10),
    _SlcAuthLocalWarningPeriod_Type()
)
slcAuthLocalWarningPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalWarningPeriod.setStatus("current")
if mibBuilder.loadTexts:
    slcAuthLocalWarningPeriod.setUnits("days")


class _SlcAuthLocalMaxLoginAttempts_Type(Integer32):
    """Custom type slcAuthLocalMaxLoginAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SlcAuthLocalMaxLoginAttempts_Type.__name__ = "Integer32"
_SlcAuthLocalMaxLoginAttempts_Object = MibScalar
slcAuthLocalMaxLoginAttempts = _SlcAuthLocalMaxLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 11),
    _SlcAuthLocalMaxLoginAttempts_Type()
)
slcAuthLocalMaxLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalMaxLoginAttempts.setStatus("current")


class _SlcAuthLocalLockoutPeriod_Type(Integer32):
    """Custom type slcAuthLocalLockoutPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_SlcAuthLocalLockoutPeriod_Type.__name__ = "Integer32"
_SlcAuthLocalLockoutPeriod_Object = MibScalar
slcAuthLocalLockoutPeriod = _SlcAuthLocalLockoutPeriod_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 12),
    _SlcAuthLocalLockoutPeriod_Type()
)
slcAuthLocalLockoutPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalLockoutPeriod.setStatus("current")
if mibBuilder.loadTexts:
    slcAuthLocalLockoutPeriod.setUnits("minutes")
_SlcAuthLocalMultipleSysadminLogins_Type = EnabledState
_SlcAuthLocalMultipleSysadminLogins_Object = MibScalar
slcAuthLocalMultipleSysadminLogins = _SlcAuthLocalMultipleSysadminLogins_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 13),
    _SlcAuthLocalMultipleSysadminLogins_Type()
)
slcAuthLocalMultipleSysadminLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalMultipleSysadminLogins.setStatus("current")
_SlcAuthLocalSysadminConsoleOnly_Type = EnabledState
_SlcAuthLocalSysadminConsoleOnly_Object = MibScalar
slcAuthLocalSysadminConsoleOnly = _SlcAuthLocalSysadminConsoleOnly_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 1, 14),
    _SlcAuthLocalSysadminConsoleOnly_Type()
)
slcAuthLocalSysadminConsoleOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLocalSysadminConsoleOnly.setStatus("current")
_SlcAuthNIS_ObjectIdentity = ObjectIdentity
slcAuthNIS = _SlcAuthNIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2)
)
_SlcAuthNISState_Type = EnabledState
_SlcAuthNISState_Object = MibScalar
slcAuthNISState = _SlcAuthNISState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 1),
    _SlcAuthNISState_Type()
)
slcAuthNISState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISState.setStatus("current")
_SlcAuthNISOrder_Type = AuthOrder
_SlcAuthNISOrder_Object = MibScalar
slcAuthNISOrder = _SlcAuthNISOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 2),
    _SlcAuthNISOrder_Type()
)
slcAuthNISOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISOrder.setStatus("current")


class _SlcAuthNISDomain_Type(OctetString):
    """Custom type slcAuthNISDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlcAuthNISDomain_Type.__name__ = "OctetString"
_SlcAuthNISDomain_Object = MibScalar
slcAuthNISDomain = _SlcAuthNISDomain_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 3),
    _SlcAuthNISDomain_Type()
)
slcAuthNISDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISDomain.setStatus("current")
_SlcAuthNISBroadcast_Type = EnabledState
_SlcAuthNISBroadcast_Object = MibScalar
slcAuthNISBroadcast = _SlcAuthNISBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 4),
    _SlcAuthNISBroadcast_Type()
)
slcAuthNISBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISBroadcast.setStatus("current")
_SlcAuthNISMaster_Type = IpAddress
_SlcAuthNISMaster_Object = MibScalar
slcAuthNISMaster = _SlcAuthNISMaster_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 5),
    _SlcAuthNISMaster_Type()
)
slcAuthNISMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISMaster.setStatus("current")
_SlcAuthNISSlave1_Type = IpAddress
_SlcAuthNISSlave1_Object = MibScalar
slcAuthNISSlave1 = _SlcAuthNISSlave1_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 6),
    _SlcAuthNISSlave1_Type()
)
slcAuthNISSlave1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISSlave1.setStatus("current")
_SlcAuthNISSlave2_Type = IpAddress
_SlcAuthNISSlave2_Object = MibScalar
slcAuthNISSlave2 = _SlcAuthNISSlave2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 7),
    _SlcAuthNISSlave2_Type()
)
slcAuthNISSlave2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISSlave2.setStatus("current")
_SlcAuthNISSlave3_Type = IpAddress
_SlcAuthNISSlave3_Object = MibScalar
slcAuthNISSlave3 = _SlcAuthNISSlave3_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 8),
    _SlcAuthNISSlave3_Type()
)
slcAuthNISSlave3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISSlave3.setStatus("current")
_SlcAuthNISGroup_Type = UserGroup
_SlcAuthNISGroup_Object = MibScalar
slcAuthNISGroup = _SlcAuthNISGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 9),
    _SlcAuthNISGroup_Type()
)
slcAuthNISGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISGroup.setStatus("current")
_SlcAuthNISRights_Type = UserRights
_SlcAuthNISRights_Object = MibScalar
slcAuthNISRights = _SlcAuthNISRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 10),
    _SlcAuthNISRights_Type()
)
slcAuthNISRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISRights.setStatus("current")
_SlcAuthNISMenu_Type = OctetString
_SlcAuthNISMenu_Object = MibScalar
slcAuthNISMenu = _SlcAuthNISMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 11),
    _SlcAuthNISMenu_Type()
)
slcAuthNISMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISMenu.setStatus("current")
_SlcAuthNISListenPorts_Type = OctetString
_SlcAuthNISListenPorts_Object = MibScalar
slcAuthNISListenPorts = _SlcAuthNISListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 12),
    _SlcAuthNISListenPorts_Type()
)
slcAuthNISListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISListenPorts.setStatus("current")
_SlcAuthNISDataPorts_Type = OctetString
_SlcAuthNISDataPorts_Object = MibScalar
slcAuthNISDataPorts = _SlcAuthNISDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 13),
    _SlcAuthNISDataPorts_Type()
)
slcAuthNISDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISDataPorts.setStatus("current")
_SlcAuthNISClearPorts_Type = OctetString
_SlcAuthNISClearPorts_Object = MibScalar
slcAuthNISClearPorts = _SlcAuthNISClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 14),
    _SlcAuthNISClearPorts_Type()
)
slcAuthNISClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISClearPorts.setStatus("current")
_SlcAuthNISSlave4_Type = IpAddress
_SlcAuthNISSlave4_Object = MibScalar
slcAuthNISSlave4 = _SlcAuthNISSlave4_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 15),
    _SlcAuthNISSlave4_Type()
)
slcAuthNISSlave4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISSlave4.setStatus("current")
_SlcAuthNISSlave5_Type = IpAddress
_SlcAuthNISSlave5_Object = MibScalar
slcAuthNISSlave5 = _SlcAuthNISSlave5_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 16),
    _SlcAuthNISSlave5_Type()
)
slcAuthNISSlave5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISSlave5.setStatus("current")
_SlcAuthNISEscapeSeq_Type = OctetString
_SlcAuthNISEscapeSeq_Object = MibScalar
slcAuthNISEscapeSeq = _SlcAuthNISEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 17),
    _SlcAuthNISEscapeSeq_Type()
)
slcAuthNISEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISEscapeSeq.setStatus("current")
_SlcAuthNISBreakSeq_Type = OctetString
_SlcAuthNISBreakSeq_Object = MibScalar
slcAuthNISBreakSeq = _SlcAuthNISBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 18),
    _SlcAuthNISBreakSeq_Type()
)
slcAuthNISBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISBreakSeq.setStatus("current")
_SlcAuthNISDialback_Type = EnabledState
_SlcAuthNISDialback_Object = MibScalar
slcAuthNISDialback = _SlcAuthNISDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 19),
    _SlcAuthNISDialback_Type()
)
slcAuthNISDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISDialback.setStatus("current")
_SlcAuthNISDialbackNum_Type = OctetString
_SlcAuthNISDialbackNum_Object = MibScalar
slcAuthNISDialbackNum = _SlcAuthNISDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 2, 20),
    _SlcAuthNISDialbackNum_Type()
)
slcAuthNISDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthNISDialbackNum.setStatus("current")
_SlcAuthLDAP_ObjectIdentity = ObjectIdentity
slcAuthLDAP = _SlcAuthLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3)
)
_SlcAuthLDAPState_Type = EnabledState
_SlcAuthLDAPState_Object = MibScalar
slcAuthLDAPState = _SlcAuthLDAPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 1),
    _SlcAuthLDAPState_Type()
)
slcAuthLDAPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPState.setStatus("current")
_SlcAuthLDAPOrder_Type = AuthOrder
_SlcAuthLDAPOrder_Object = MibScalar
slcAuthLDAPOrder = _SlcAuthLDAPOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 2),
    _SlcAuthLDAPOrder_Type()
)
slcAuthLDAPOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPOrder.setStatus("current")
_SlcAuthLDAPServer_Type = IpAddress
_SlcAuthLDAPServer_Object = MibScalar
slcAuthLDAPServer = _SlcAuthLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 3),
    _SlcAuthLDAPServer_Type()
)
slcAuthLDAPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPServer.setStatus("current")


class _SlcAuthLDAPBase_Type(OctetString):
    """Custom type slcAuthLDAPBase based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlcAuthLDAPBase_Type.__name__ = "OctetString"
_SlcAuthLDAPBase_Object = MibScalar
slcAuthLDAPBase = _SlcAuthLDAPBase_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 4),
    _SlcAuthLDAPBase_Type()
)
slcAuthLDAPBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPBase.setStatus("current")


class _SlcAuthLDAPBindName_Type(OctetString):
    """Custom type slcAuthLDAPBindName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlcAuthLDAPBindName_Type.__name__ = "OctetString"
_SlcAuthLDAPBindName_Object = MibScalar
slcAuthLDAPBindName = _SlcAuthLDAPBindName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 5),
    _SlcAuthLDAPBindName_Type()
)
slcAuthLDAPBindName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPBindName.setStatus("current")


class _SlcAuthLDAPPort_Type(Integer32):
    """Custom type slcAuthLDAPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcAuthLDAPPort_Type.__name__ = "Integer32"
_SlcAuthLDAPPort_Object = MibScalar
slcAuthLDAPPort = _SlcAuthLDAPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 6),
    _SlcAuthLDAPPort_Type()
)
slcAuthLDAPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPPort.setStatus("current")
_SlcAuthLDAPADSupport_Type = EnabledState
_SlcAuthLDAPADSupport_Object = MibScalar
slcAuthLDAPADSupport = _SlcAuthLDAPADSupport_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 7),
    _SlcAuthLDAPADSupport_Type()
)
slcAuthLDAPADSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPADSupport.setStatus("current")
_SlcAuthLDAPGroup_Type = UserGroup
_SlcAuthLDAPGroup_Object = MibScalar
slcAuthLDAPGroup = _SlcAuthLDAPGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 8),
    _SlcAuthLDAPGroup_Type()
)
slcAuthLDAPGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPGroup.setStatus("current")
_SlcAuthLDAPRights_Type = UserRights
_SlcAuthLDAPRights_Object = MibScalar
slcAuthLDAPRights = _SlcAuthLDAPRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 9),
    _SlcAuthLDAPRights_Type()
)
slcAuthLDAPRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPRights.setStatus("current")
_SlcAuthLDAPMenu_Type = OctetString
_SlcAuthLDAPMenu_Object = MibScalar
slcAuthLDAPMenu = _SlcAuthLDAPMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 10),
    _SlcAuthLDAPMenu_Type()
)
slcAuthLDAPMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPMenu.setStatus("current")
_SlcAuthLDAPListenPorts_Type = OctetString
_SlcAuthLDAPListenPorts_Object = MibScalar
slcAuthLDAPListenPorts = _SlcAuthLDAPListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 11),
    _SlcAuthLDAPListenPorts_Type()
)
slcAuthLDAPListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPListenPorts.setStatus("current")
_SlcAuthLDAPDataPorts_Type = OctetString
_SlcAuthLDAPDataPorts_Object = MibScalar
slcAuthLDAPDataPorts = _SlcAuthLDAPDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 12),
    _SlcAuthLDAPDataPorts_Type()
)
slcAuthLDAPDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPDataPorts.setStatus("current")
_SlcAuthLDAPClearPorts_Type = OctetString
_SlcAuthLDAPClearPorts_Object = MibScalar
slcAuthLDAPClearPorts = _SlcAuthLDAPClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 13),
    _SlcAuthLDAPClearPorts_Type()
)
slcAuthLDAPClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPClearPorts.setStatus("current")
_SlcAuthLDAPEncrypt_Type = EnabledState
_SlcAuthLDAPEncrypt_Object = MibScalar
slcAuthLDAPEncrypt = _SlcAuthLDAPEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 14),
    _SlcAuthLDAPEncrypt_Type()
)
slcAuthLDAPEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPEncrypt.setStatus("current")
_SlcAuthLDAPEscapeSeq_Type = OctetString
_SlcAuthLDAPEscapeSeq_Object = MibScalar
slcAuthLDAPEscapeSeq = _SlcAuthLDAPEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 15),
    _SlcAuthLDAPEscapeSeq_Type()
)
slcAuthLDAPEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPEscapeSeq.setStatus("current")
_SlcAuthLDAPBreakSeq_Type = OctetString
_SlcAuthLDAPBreakSeq_Object = MibScalar
slcAuthLDAPBreakSeq = _SlcAuthLDAPBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 16),
    _SlcAuthLDAPBreakSeq_Type()
)
slcAuthLDAPBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPBreakSeq.setStatus("current")
_SlcAuthLDAPBindWithLogin_Type = EnabledState
_SlcAuthLDAPBindWithLogin_Object = MibScalar
slcAuthLDAPBindWithLogin = _SlcAuthLDAPBindWithLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 17),
    _SlcAuthLDAPBindWithLogin_Type()
)
slcAuthLDAPBindWithLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPBindWithLogin.setStatus("current")
_SlcAuthLDAPUseLDAPSchema_Type = EnabledState
_SlcAuthLDAPUseLDAPSchema_Object = MibScalar
slcAuthLDAPUseLDAPSchema = _SlcAuthLDAPUseLDAPSchema_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 18),
    _SlcAuthLDAPUseLDAPSchema_Type()
)
slcAuthLDAPUseLDAPSchema.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPUseLDAPSchema.setStatus("current")
_SlcAuthLDAPDialback_Type = EnabledState
_SlcAuthLDAPDialback_Object = MibScalar
slcAuthLDAPDialback = _SlcAuthLDAPDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 19),
    _SlcAuthLDAPDialback_Type()
)
slcAuthLDAPDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPDialback.setStatus("current")
_SlcAuthLDAPDialbackNum_Type = OctetString
_SlcAuthLDAPDialbackNum_Object = MibScalar
slcAuthLDAPDialbackNum = _SlcAuthLDAPDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 20),
    _SlcAuthLDAPDialbackNum_Type()
)
slcAuthLDAPDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPDialbackNum.setStatus("current")
_SlcAuthLDAPUserFilter_Type = OctetString
_SlcAuthLDAPUserFilter_Object = MibScalar
slcAuthLDAPUserFilter = _SlcAuthLDAPUserFilter_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 21),
    _SlcAuthLDAPUserFilter_Type()
)
slcAuthLDAPUserFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPUserFilter.setStatus("current")
_SlcAuthLDAPGroupFilter_Type = OctetString
_SlcAuthLDAPGroupFilter_Object = MibScalar
slcAuthLDAPGroupFilter = _SlcAuthLDAPGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 22),
    _SlcAuthLDAPGroupFilter_Type()
)
slcAuthLDAPGroupFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPGroupFilter.setStatus("current")
_SlcAuthLDAPGroupMembershipAttr_Type = OctetString
_SlcAuthLDAPGroupMembershipAttr_Object = MibScalar
slcAuthLDAPGroupMembershipAttr = _SlcAuthLDAPGroupMembershipAttr_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 23),
    _SlcAuthLDAPGroupMembershipAttr_Type()
)
slcAuthLDAPGroupMembershipAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPGroupMembershipAttr.setStatus("current")
_SlcAuthLDAPGroupMembershipDN_Type = EnabledState
_SlcAuthLDAPGroupMembershipDN_Object = MibScalar
slcAuthLDAPGroupMembershipDN = _SlcAuthLDAPGroupMembershipDN_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 24),
    _SlcAuthLDAPGroupMembershipDN_Type()
)
slcAuthLDAPGroupMembershipDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPGroupMembershipDN.setStatus("current")
_SlcAuthLDAPServer2_Type = IpAddress
_SlcAuthLDAPServer2_Object = MibScalar
slcAuthLDAPServer2 = _SlcAuthLDAPServer2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 25),
    _SlcAuthLDAPServer2_Type()
)
slcAuthLDAPServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPServer2.setStatus("current")
_SlcAuthLDAPServerIPv6_Type = Ipv6Address
_SlcAuthLDAPServerIPv6_Object = MibScalar
slcAuthLDAPServerIPv6 = _SlcAuthLDAPServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 26),
    _SlcAuthLDAPServerIPv6_Type()
)
slcAuthLDAPServerIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPServerIPv6.setStatus("current")
_SlcAuthLDAPServer2IPv6_Type = Ipv6Address
_SlcAuthLDAPServer2IPv6_Object = MibScalar
slcAuthLDAPServer2IPv6 = _SlcAuthLDAPServer2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 3, 27),
    _SlcAuthLDAPServer2IPv6_Type()
)
slcAuthLDAPServer2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthLDAPServer2IPv6.setStatus("current")
_SlcAuthRADIUS_ObjectIdentity = ObjectIdentity
slcAuthRADIUS = _SlcAuthRADIUS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4)
)
_SlcAuthRADIUSState_Type = EnabledState
_SlcAuthRADIUSState_Object = MibScalar
slcAuthRADIUSState = _SlcAuthRADIUSState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 1),
    _SlcAuthRADIUSState_Type()
)
slcAuthRADIUSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSState.setStatus("current")
_SlcAuthRADIUSOrder_Type = AuthOrder
_SlcAuthRADIUSOrder_Object = MibScalar
slcAuthRADIUSOrder = _SlcAuthRADIUSOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 2),
    _SlcAuthRADIUSOrder_Type()
)
slcAuthRADIUSOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSOrder.setStatus("current")


class _SlcAuthRADIUSTimeout_Type(Integer32):
    """Custom type slcAuthRADIUSTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcAuthRADIUSTimeout_Type.__name__ = "Integer32"
_SlcAuthRADIUSTimeout_Object = MibScalar
slcAuthRADIUSTimeout = _SlcAuthRADIUSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 3),
    _SlcAuthRADIUSTimeout_Type()
)
slcAuthRADIUSTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcAuthRADIUSTimeout.setUnits("seconds")
_SlcAuthRADIUSServerTable_Object = MibTable
slcAuthRADIUSServerTable = _SlcAuthRADIUSServerTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    slcAuthRADIUSServerTable.setStatus("current")
_SlcAuthRADIUSServerEntry_Object = MibTableRow
slcAuthRADIUSServerEntry = _SlcAuthRADIUSServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4, 1)
)
slcAuthRADIUSServerEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcAuthRADIUSServerIndex"),
)
if mibBuilder.loadTexts:
    slcAuthRADIUSServerEntry.setStatus("current")


class _SlcAuthRADIUSServerIndex_Type(Integer32):
    """Custom type slcAuthRADIUSServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlcAuthRADIUSServerIndex_Type.__name__ = "Integer32"
_SlcAuthRADIUSServerIndex_Object = MibTableColumn
slcAuthRADIUSServerIndex = _SlcAuthRADIUSServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4, 1, 1),
    _SlcAuthRADIUSServerIndex_Type()
)
slcAuthRADIUSServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSServerIndex.setStatus("current")
_SlcAuthRADIUSServer_Type = IpAddress
_SlcAuthRADIUSServer_Object = MibTableColumn
slcAuthRADIUSServer = _SlcAuthRADIUSServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4, 1, 2),
    _SlcAuthRADIUSServer_Type()
)
slcAuthRADIUSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSServer.setStatus("current")


class _SlcAuthRADIUSPort_Type(Integer32):
    """Custom type slcAuthRADIUSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcAuthRADIUSPort_Type.__name__ = "Integer32"
_SlcAuthRADIUSPort_Object = MibTableColumn
slcAuthRADIUSPort = _SlcAuthRADIUSPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4, 1, 3),
    _SlcAuthRADIUSPort_Type()
)
slcAuthRADIUSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSPort.setStatus("current")
_SlcAuthRADIUSServerIPv6_Type = Ipv6Address
_SlcAuthRADIUSServerIPv6_Object = MibTableColumn
slcAuthRADIUSServerIPv6 = _SlcAuthRADIUSServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 4, 1, 4),
    _SlcAuthRADIUSServerIPv6_Type()
)
slcAuthRADIUSServerIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSServerIPv6.setStatus("current")
_SlcAuthRADIUSGroup_Type = UserGroup
_SlcAuthRADIUSGroup_Object = MibScalar
slcAuthRADIUSGroup = _SlcAuthRADIUSGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 5),
    _SlcAuthRADIUSGroup_Type()
)
slcAuthRADIUSGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSGroup.setStatus("current")
_SlcAuthRADIUSRights_Type = UserRights
_SlcAuthRADIUSRights_Object = MibScalar
slcAuthRADIUSRights = _SlcAuthRADIUSRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 6),
    _SlcAuthRADIUSRights_Type()
)
slcAuthRADIUSRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSRights.setStatus("current")
_SlcAuthRADIUSMenu_Type = OctetString
_SlcAuthRADIUSMenu_Object = MibScalar
slcAuthRADIUSMenu = _SlcAuthRADIUSMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 7),
    _SlcAuthRADIUSMenu_Type()
)
slcAuthRADIUSMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSMenu.setStatus("current")
_SlcAuthRADIUSListenPorts_Type = OctetString
_SlcAuthRADIUSListenPorts_Object = MibScalar
slcAuthRADIUSListenPorts = _SlcAuthRADIUSListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 8),
    _SlcAuthRADIUSListenPorts_Type()
)
slcAuthRADIUSListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSListenPorts.setStatus("current")
_SlcAuthRADIUSDataPorts_Type = OctetString
_SlcAuthRADIUSDataPorts_Object = MibScalar
slcAuthRADIUSDataPorts = _SlcAuthRADIUSDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 9),
    _SlcAuthRADIUSDataPorts_Type()
)
slcAuthRADIUSDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSDataPorts.setStatus("current")
_SlcAuthRADIUSClearPorts_Type = OctetString
_SlcAuthRADIUSClearPorts_Object = MibScalar
slcAuthRADIUSClearPorts = _SlcAuthRADIUSClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 10),
    _SlcAuthRADIUSClearPorts_Type()
)
slcAuthRADIUSClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSClearPorts.setStatus("current")
_SlcAuthRADIUSEscapeSeq_Type = OctetString
_SlcAuthRADIUSEscapeSeq_Object = MibScalar
slcAuthRADIUSEscapeSeq = _SlcAuthRADIUSEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 11),
    _SlcAuthRADIUSEscapeSeq_Type()
)
slcAuthRADIUSEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSEscapeSeq.setStatus("current")
_SlcAuthRADIUSBreakSeq_Type = OctetString
_SlcAuthRADIUSBreakSeq_Object = MibScalar
slcAuthRADIUSBreakSeq = _SlcAuthRADIUSBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 12),
    _SlcAuthRADIUSBreakSeq_Type()
)
slcAuthRADIUSBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSBreakSeq.setStatus("current")
_SlcAuthRADIUSDialback_Type = EnabledState
_SlcAuthRADIUSDialback_Object = MibScalar
slcAuthRADIUSDialback = _SlcAuthRADIUSDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 13),
    _SlcAuthRADIUSDialback_Type()
)
slcAuthRADIUSDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSDialback.setStatus("current")
_SlcAuthRADIUSDialbackNum_Type = OctetString
_SlcAuthRADIUSDialbackNum_Object = MibScalar
slcAuthRADIUSDialbackNum = _SlcAuthRADIUSDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 14),
    _SlcAuthRADIUSDialbackNum_Type()
)
slcAuthRADIUSDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSDialbackNum.setStatus("current")
_SlcAuthRADIUSUseVSA_Type = EnabledState
_SlcAuthRADIUSUseVSA_Object = MibScalar
slcAuthRADIUSUseVSA = _SlcAuthRADIUSUseVSA_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 4, 15),
    _SlcAuthRADIUSUseVSA_Type()
)
slcAuthRADIUSUseVSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRADIUSUseVSA.setStatus("current")
_SlcAuthKerberos_ObjectIdentity = ObjectIdentity
slcAuthKerberos = _SlcAuthKerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5)
)
_SlcAuthKerbState_Type = EnabledState
_SlcAuthKerbState_Object = MibScalar
slcAuthKerbState = _SlcAuthKerbState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 1),
    _SlcAuthKerbState_Type()
)
slcAuthKerbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbState.setStatus("current")
_SlcAuthKerbOrder_Type = AuthOrder
_SlcAuthKerbOrder_Object = MibScalar
slcAuthKerbOrder = _SlcAuthKerbOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 2),
    _SlcAuthKerbOrder_Type()
)
slcAuthKerbOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbOrder.setStatus("current")


class _SlcAuthKerbRealm_Type(OctetString):
    """Custom type slcAuthKerbRealm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlcAuthKerbRealm_Type.__name__ = "OctetString"
_SlcAuthKerbRealm_Object = MibScalar
slcAuthKerbRealm = _SlcAuthKerbRealm_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 3),
    _SlcAuthKerbRealm_Type()
)
slcAuthKerbRealm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbRealm.setStatus("current")


class _SlcAuthKerbKDC_Type(OctetString):
    """Custom type slcAuthKerbKDC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SlcAuthKerbKDC_Type.__name__ = "OctetString"
_SlcAuthKerbKDC_Object = MibScalar
slcAuthKerbKDC = _SlcAuthKerbKDC_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 4),
    _SlcAuthKerbKDC_Type()
)
slcAuthKerbKDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbKDC.setStatus("current")
_SlcAuthKerbKDCIP_Type = IpAddress
_SlcAuthKerbKDCIP_Object = MibScalar
slcAuthKerbKDCIP = _SlcAuthKerbKDCIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 5),
    _SlcAuthKerbKDCIP_Type()
)
slcAuthKerbKDCIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbKDCIP.setStatus("current")


class _SlcAuthKerbKDCPort_Type(Integer32):
    """Custom type slcAuthKerbKDCPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcAuthKerbKDCPort_Type.__name__ = "Integer32"
_SlcAuthKerbKDCPort_Object = MibScalar
slcAuthKerbKDCPort = _SlcAuthKerbKDCPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 6),
    _SlcAuthKerbKDCPort_Type()
)
slcAuthKerbKDCPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbKDCPort.setStatus("current")
_SlcAuthKerbUseLDAP_Type = EnabledState
_SlcAuthKerbUseLDAP_Object = MibScalar
slcAuthKerbUseLDAP = _SlcAuthKerbUseLDAP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 7),
    _SlcAuthKerbUseLDAP_Type()
)
slcAuthKerbUseLDAP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbUseLDAP.setStatus("current")
_SlcAuthKerbGroup_Type = UserGroup
_SlcAuthKerbGroup_Object = MibScalar
slcAuthKerbGroup = _SlcAuthKerbGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 8),
    _SlcAuthKerbGroup_Type()
)
slcAuthKerbGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbGroup.setStatus("current")
_SlcAuthKerbRights_Type = UserRights
_SlcAuthKerbRights_Object = MibScalar
slcAuthKerbRights = _SlcAuthKerbRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 9),
    _SlcAuthKerbRights_Type()
)
slcAuthKerbRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbRights.setStatus("current")
_SlcAuthKerbMenu_Type = OctetString
_SlcAuthKerbMenu_Object = MibScalar
slcAuthKerbMenu = _SlcAuthKerbMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 10),
    _SlcAuthKerbMenu_Type()
)
slcAuthKerbMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbMenu.setStatus("current")
_SlcAuthKerbListenPorts_Type = OctetString
_SlcAuthKerbListenPorts_Object = MibScalar
slcAuthKerbListenPorts = _SlcAuthKerbListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 11),
    _SlcAuthKerbListenPorts_Type()
)
slcAuthKerbListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbListenPorts.setStatus("current")
_SlcAuthKerbDataPorts_Type = OctetString
_SlcAuthKerbDataPorts_Object = MibScalar
slcAuthKerbDataPorts = _SlcAuthKerbDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 12),
    _SlcAuthKerbDataPorts_Type()
)
slcAuthKerbDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbDataPorts.setStatus("current")
_SlcAuthKerbClearPorts_Type = OctetString
_SlcAuthKerbClearPorts_Object = MibScalar
slcAuthKerbClearPorts = _SlcAuthKerbClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 13),
    _SlcAuthKerbClearPorts_Type()
)
slcAuthKerbClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbClearPorts.setStatus("current")
_SlcAuthKerbEscapeSeq_Type = OctetString
_SlcAuthKerbEscapeSeq_Object = MibScalar
slcAuthKerbEscapeSeq = _SlcAuthKerbEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 14),
    _SlcAuthKerbEscapeSeq_Type()
)
slcAuthKerbEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbEscapeSeq.setStatus("current")
_SlcAuthKerbBreakSeq_Type = OctetString
_SlcAuthKerbBreakSeq_Object = MibScalar
slcAuthKerbBreakSeq = _SlcAuthKerbBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 15),
    _SlcAuthKerbBreakSeq_Type()
)
slcAuthKerbBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbBreakSeq.setStatus("current")
_SlcAuthKerbDialback_Type = EnabledState
_SlcAuthKerbDialback_Object = MibScalar
slcAuthKerbDialback = _SlcAuthKerbDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 16),
    _SlcAuthKerbDialback_Type()
)
slcAuthKerbDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbDialback.setStatus("current")
_SlcAuthKerbDialbackNum_Type = OctetString
_SlcAuthKerbDialbackNum_Object = MibScalar
slcAuthKerbDialbackNum = _SlcAuthKerbDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 17),
    _SlcAuthKerbDialbackNum_Type()
)
slcAuthKerbDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbDialbackNum.setStatus("current")
_SlcAuthKerbKDCIPv6_Type = Ipv6Address
_SlcAuthKerbKDCIPv6_Object = MibScalar
slcAuthKerbKDCIPv6 = _SlcAuthKerbKDCIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 5, 18),
    _SlcAuthKerbKDCIPv6_Type()
)
slcAuthKerbKDCIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthKerbKDCIPv6.setStatus("current")
_SlcAuthTACACS_ObjectIdentity = ObjectIdentity
slcAuthTACACS = _SlcAuthTACACS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6)
)
_SlcAuthTACACSState_Type = EnabledState
_SlcAuthTACACSState_Object = MibScalar
slcAuthTACACSState = _SlcAuthTACACSState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 1),
    _SlcAuthTACACSState_Type()
)
slcAuthTACACSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSState.setStatus("current")
_SlcAuthTACACSOrder_Type = AuthOrder
_SlcAuthTACACSOrder_Object = MibScalar
slcAuthTACACSOrder = _SlcAuthTACACSOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 2),
    _SlcAuthTACACSOrder_Type()
)
slcAuthTACACSOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSOrder.setStatus("current")
_SlcAuthTACACSServer_Type = IpAddress
_SlcAuthTACACSServer_Object = MibScalar
slcAuthTACACSServer = _SlcAuthTACACSServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 3),
    _SlcAuthTACACSServer_Type()
)
slcAuthTACACSServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServer.setStatus("current")
_SlcAuthTACACSEncrypt_Type = EnabledState
_SlcAuthTACACSEncrypt_Object = MibScalar
slcAuthTACACSEncrypt = _SlcAuthTACACSEncrypt_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 4),
    _SlcAuthTACACSEncrypt_Type()
)
slcAuthTACACSEncrypt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSEncrypt.setStatus("current")
_SlcAuthTACACSGroup_Type = UserGroup
_SlcAuthTACACSGroup_Object = MibScalar
slcAuthTACACSGroup = _SlcAuthTACACSGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 5),
    _SlcAuthTACACSGroup_Type()
)
slcAuthTACACSGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSGroup.setStatus("current")
_SlcAuthTACACSRights_Type = UserRights
_SlcAuthTACACSRights_Object = MibScalar
slcAuthTACACSRights = _SlcAuthTACACSRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 6),
    _SlcAuthTACACSRights_Type()
)
slcAuthTACACSRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSRights.setStatus("current")
_SlcAuthTACACSMenu_Type = OctetString
_SlcAuthTACACSMenu_Object = MibScalar
slcAuthTACACSMenu = _SlcAuthTACACSMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 7),
    _SlcAuthTACACSMenu_Type()
)
slcAuthTACACSMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSMenu.setStatus("current")
_SlcAuthTACACSListenPorts_Type = OctetString
_SlcAuthTACACSListenPorts_Object = MibScalar
slcAuthTACACSListenPorts = _SlcAuthTACACSListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 8),
    _SlcAuthTACACSListenPorts_Type()
)
slcAuthTACACSListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSListenPorts.setStatus("current")
_SlcAuthTACACSDataPorts_Type = OctetString
_SlcAuthTACACSDataPorts_Object = MibScalar
slcAuthTACACSDataPorts = _SlcAuthTACACSDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 9),
    _SlcAuthTACACSDataPorts_Type()
)
slcAuthTACACSDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSDataPorts.setStatus("current")
_SlcAuthTACACSClearPorts_Type = OctetString
_SlcAuthTACACSClearPorts_Object = MibScalar
slcAuthTACACSClearPorts = _SlcAuthTACACSClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 10),
    _SlcAuthTACACSClearPorts_Type()
)
slcAuthTACACSClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSClearPorts.setStatus("current")
_SlcAuthTACACSServer2_Type = IpAddress
_SlcAuthTACACSServer2_Object = MibScalar
slcAuthTACACSServer2 = _SlcAuthTACACSServer2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 11),
    _SlcAuthTACACSServer2_Type()
)
slcAuthTACACSServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServer2.setStatus("current")
_SlcAuthTACACSServer3_Type = IpAddress
_SlcAuthTACACSServer3_Object = MibScalar
slcAuthTACACSServer3 = _SlcAuthTACACSServer3_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 12),
    _SlcAuthTACACSServer3_Type()
)
slcAuthTACACSServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServer3.setStatus("current")
_SlcAuthTACACSEscapeSeq_Type = OctetString
_SlcAuthTACACSEscapeSeq_Object = MibScalar
slcAuthTACACSEscapeSeq = _SlcAuthTACACSEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 13),
    _SlcAuthTACACSEscapeSeq_Type()
)
slcAuthTACACSEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSEscapeSeq.setStatus("current")
_SlcAuthTACACSBreakSeq_Type = OctetString
_SlcAuthTACACSBreakSeq_Object = MibScalar
slcAuthTACACSBreakSeq = _SlcAuthTACACSBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 14),
    _SlcAuthTACACSBreakSeq_Type()
)
slcAuthTACACSBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSBreakSeq.setStatus("current")
_SlcAuthTACACSDialback_Type = EnabledState
_SlcAuthTACACSDialback_Object = MibScalar
slcAuthTACACSDialback = _SlcAuthTACACSDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 15),
    _SlcAuthTACACSDialback_Type()
)
slcAuthTACACSDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSDialback.setStatus("current")
_SlcAuthTACACSDialbackNum_Type = OctetString
_SlcAuthTACACSDialbackNum_Object = MibScalar
slcAuthTACACSDialbackNum = _SlcAuthTACACSDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 16),
    _SlcAuthTACACSDialbackNum_Type()
)
slcAuthTACACSDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSDialbackNum.setStatus("current")


class _SlcAuthTACACSAuthService_Type(Integer32):
    """Custom type slcAuthTACACSAuthService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asciiLogin", 3),
          ("pppCHAP", 2),
          ("pppPAP", 1))
    )


_SlcAuthTACACSAuthService_Type.__name__ = "Integer32"
_SlcAuthTACACSAuthService_Object = MibScalar
slcAuthTACACSAuthService = _SlcAuthTACACSAuthService_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 17),
    _SlcAuthTACACSAuthService_Type()
)
slcAuthTACACSAuthService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSAuthService.setStatus("current")
_SlcAuthTACACSServerIPv6_Type = Ipv6Address
_SlcAuthTACACSServerIPv6_Object = MibScalar
slcAuthTACACSServerIPv6 = _SlcAuthTACACSServerIPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 18),
    _SlcAuthTACACSServerIPv6_Type()
)
slcAuthTACACSServerIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServerIPv6.setStatus("current")
_SlcAuthTACACSServer2IPv6_Type = Ipv6Address
_SlcAuthTACACSServer2IPv6_Object = MibScalar
slcAuthTACACSServer2IPv6 = _SlcAuthTACACSServer2IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 19),
    _SlcAuthTACACSServer2IPv6_Type()
)
slcAuthTACACSServer2IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServer2IPv6.setStatus("current")
_SlcAuthTACACSServer3IPv6_Type = Ipv6Address
_SlcAuthTACACSServer3IPv6_Object = MibScalar
slcAuthTACACSServer3IPv6 = _SlcAuthTACACSServer3IPv6_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 6, 20),
    _SlcAuthTACACSServer3IPv6_Type()
)
slcAuthTACACSServer3IPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthTACACSServer3IPv6.setStatus("current")
_SlcAuthRemote_ObjectIdentity = ObjectIdentity
slcAuthRemote = _SlcAuthRemote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7)
)


class _SlcAuthRemoteNumber_Type(Integer32):
    """Custom type slcAuthRemoteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SlcAuthRemoteNumber_Type.__name__ = "Integer32"
_SlcAuthRemoteNumber_Object = MibScalar
slcAuthRemoteNumber = _SlcAuthRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 1),
    _SlcAuthRemoteNumber_Type()
)
slcAuthRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteNumber.setStatus("current")
_SlcAuthRemoteUsersTable_Object = MibTable
slcAuthRemoteUsersTable = _SlcAuthRemoteUsersTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2)
)
if mibBuilder.loadTexts:
    slcAuthRemoteUsersTable.setStatus("current")
_SlcAuthRemoteUserEntry_Object = MibTableRow
slcAuthRemoteUserEntry = _SlcAuthRemoteUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1)
)
slcAuthRemoteUserEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcAuthRemoteUserIndex"),
)
if mibBuilder.loadTexts:
    slcAuthRemoteUserEntry.setStatus("current")


class _SlcAuthRemoteUserIndex_Type(Integer32):
    """Custom type slcAuthRemoteUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlcAuthRemoteUserIndex_Type.__name__ = "Integer32"
_SlcAuthRemoteUserIndex_Object = MibTableColumn
slcAuthRemoteUserIndex = _SlcAuthRemoteUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 1),
    _SlcAuthRemoteUserIndex_Type()
)
slcAuthRemoteUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserIndex.setStatus("current")


class _SlcAuthRemoteUserLogin_Type(OctetString):
    """Custom type slcAuthRemoteUserLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlcAuthRemoteUserLogin_Type.__name__ = "OctetString"
_SlcAuthRemoteUserLogin_Object = MibTableColumn
slcAuthRemoteUserLogin = _SlcAuthRemoteUserLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 2),
    _SlcAuthRemoteUserLogin_Type()
)
slcAuthRemoteUserLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserLogin.setStatus("current")
_SlcAuthRemoteUserGroup_Type = UserGroup
_SlcAuthRemoteUserGroup_Object = MibTableColumn
slcAuthRemoteUserGroup = _SlcAuthRemoteUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 3),
    _SlcAuthRemoteUserGroup_Type()
)
slcAuthRemoteUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserGroup.setStatus("current")
_SlcAuthRemoteUserRights_Type = UserRights
_SlcAuthRemoteUserRights_Object = MibTableColumn
slcAuthRemoteUserRights = _SlcAuthRemoteUserRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 4),
    _SlcAuthRemoteUserRights_Type()
)
slcAuthRemoteUserRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserRights.setStatus("current")
_SlcAuthRemoteUserListenPorts_Type = OctetString
_SlcAuthRemoteUserListenPorts_Object = MibTableColumn
slcAuthRemoteUserListenPorts = _SlcAuthRemoteUserListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 5),
    _SlcAuthRemoteUserListenPorts_Type()
)
slcAuthRemoteUserListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserListenPorts.setStatus("current")
_SlcAuthRemoteUserDataPorts_Type = OctetString
_SlcAuthRemoteUserDataPorts_Object = MibTableColumn
slcAuthRemoteUserDataPorts = _SlcAuthRemoteUserDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 6),
    _SlcAuthRemoteUserDataPorts_Type()
)
slcAuthRemoteUserDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserDataPorts.setStatus("current")
_SlcAuthRemoteUserClearPorts_Type = OctetString
_SlcAuthRemoteUserClearPorts_Object = MibTableColumn
slcAuthRemoteUserClearPorts = _SlcAuthRemoteUserClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 7),
    _SlcAuthRemoteUserClearPorts_Type()
)
slcAuthRemoteUserClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserClearPorts.setStatus("current")
_SlcAuthRemoteUserEscapeSeq_Type = OctetString
_SlcAuthRemoteUserEscapeSeq_Object = MibTableColumn
slcAuthRemoteUserEscapeSeq = _SlcAuthRemoteUserEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 8),
    _SlcAuthRemoteUserEscapeSeq_Type()
)
slcAuthRemoteUserEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserEscapeSeq.setStatus("current")
_SlcAuthRemoteUserBreakSeq_Type = OctetString
_SlcAuthRemoteUserBreakSeq_Object = MibTableColumn
slcAuthRemoteUserBreakSeq = _SlcAuthRemoteUserBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 9),
    _SlcAuthRemoteUserBreakSeq_Type()
)
slcAuthRemoteUserBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserBreakSeq.setStatus("current")
_SlcAuthRemoteUserMenu_Type = OctetString
_SlcAuthRemoteUserMenu_Object = MibTableColumn
slcAuthRemoteUserMenu = _SlcAuthRemoteUserMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 10),
    _SlcAuthRemoteUserMenu_Type()
)
slcAuthRemoteUserMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserMenu.setStatus("current")
_SlcAuthRemoteUserLocked_Type = EnabledState
_SlcAuthRemoteUserLocked_Object = MibTableColumn
slcAuthRemoteUserLocked = _SlcAuthRemoteUserLocked_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 11),
    _SlcAuthRemoteUserLocked_Type()
)
slcAuthRemoteUserLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserLocked.setStatus("current")
_SlcAuthRemoteUserDialback_Type = EnabledState
_SlcAuthRemoteUserDialback_Object = MibTableColumn
slcAuthRemoteUserDialback = _SlcAuthRemoteUserDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 12),
    _SlcAuthRemoteUserDialback_Type()
)
slcAuthRemoteUserDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserDialback.setStatus("current")
_SlcAuthRemoteUserDialbackNum_Type = OctetString
_SlcAuthRemoteUserDialbackNum_Object = MibTableColumn
slcAuthRemoteUserDialbackNum = _SlcAuthRemoteUserDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 2, 1, 13),
    _SlcAuthRemoteUserDialbackNum_Type()
)
slcAuthRemoteUserDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteUserDialbackNum.setStatus("current")
_SlcAuthRemoteAuthListOnly_Type = EnabledState
_SlcAuthRemoteAuthListOnly_Object = MibScalar
slcAuthRemoteAuthListOnly = _SlcAuthRemoteAuthListOnly_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 7, 3),
    _SlcAuthRemoteAuthListOnly_Type()
)
slcAuthRemoteAuthListOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthRemoteAuthListOnly.setStatus("current")
_SlcAuthGroups_ObjectIdentity = ObjectIdentity
slcAuthGroups = _SlcAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8)
)


class _SlcAuthGroupsNumber_Type(Integer32):
    """Custom type slcAuthGroupsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_SlcAuthGroupsNumber_Type.__name__ = "Integer32"
_SlcAuthGroupsNumber_Object = MibScalar
slcAuthGroupsNumber = _SlcAuthGroupsNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 1),
    _SlcAuthGroupsNumber_Type()
)
slcAuthGroupsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupsNumber.setStatus("current")
_SlcAuthGroupsTable_Object = MibTable
slcAuthGroupsTable = _SlcAuthGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2)
)
if mibBuilder.loadTexts:
    slcAuthGroupsTable.setStatus("current")
_SlcAuthGroupEntry_Object = MibTableRow
slcAuthGroupEntry = _SlcAuthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1)
)
slcAuthGroupEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcAuthGroupIndex"),
)
if mibBuilder.loadTexts:
    slcAuthGroupEntry.setStatus("current")


class _SlcAuthGroupIndex_Type(Integer32):
    """Custom type slcAuthGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SlcAuthGroupIndex_Type.__name__ = "Integer32"
_SlcAuthGroupIndex_Object = MibTableColumn
slcAuthGroupIndex = _SlcAuthGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 1),
    _SlcAuthGroupIndex_Type()
)
slcAuthGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupIndex.setStatus("current")


class _SlcAuthGroupName_Type(OctetString):
    """Custom type slcAuthGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SlcAuthGroupName_Type.__name__ = "OctetString"
_SlcAuthGroupName_Object = MibTableColumn
slcAuthGroupName = _SlcAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 2),
    _SlcAuthGroupName_Type()
)
slcAuthGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupName.setStatus("current")
_SlcAuthGroupRights_Type = UserRights
_SlcAuthGroupRights_Object = MibTableColumn
slcAuthGroupRights = _SlcAuthGroupRights_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 3),
    _SlcAuthGroupRights_Type()
)
slcAuthGroupRights.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupRights.setStatus("current")
_SlcAuthGroupListenPorts_Type = OctetString
_SlcAuthGroupListenPorts_Object = MibTableColumn
slcAuthGroupListenPorts = _SlcAuthGroupListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 4),
    _SlcAuthGroupListenPorts_Type()
)
slcAuthGroupListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupListenPorts.setStatus("current")
_SlcAuthGroupDataPorts_Type = OctetString
_SlcAuthGroupDataPorts_Object = MibTableColumn
slcAuthGroupDataPorts = _SlcAuthGroupDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 5),
    _SlcAuthGroupDataPorts_Type()
)
slcAuthGroupDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupDataPorts.setStatus("current")
_SlcAuthGroupClearPorts_Type = OctetString
_SlcAuthGroupClearPorts_Object = MibTableColumn
slcAuthGroupClearPorts = _SlcAuthGroupClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 6),
    _SlcAuthGroupClearPorts_Type()
)
slcAuthGroupClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupClearPorts.setStatus("current")
_SlcAuthGroupEscapeSeq_Type = OctetString
_SlcAuthGroupEscapeSeq_Object = MibTableColumn
slcAuthGroupEscapeSeq = _SlcAuthGroupEscapeSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 7),
    _SlcAuthGroupEscapeSeq_Type()
)
slcAuthGroupEscapeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupEscapeSeq.setStatus("current")
_SlcAuthGroupBreakSeq_Type = OctetString
_SlcAuthGroupBreakSeq_Object = MibTableColumn
slcAuthGroupBreakSeq = _SlcAuthGroupBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 8),
    _SlcAuthGroupBreakSeq_Type()
)
slcAuthGroupBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupBreakSeq.setStatus("current")
_SlcAuthGroupMenu_Type = OctetString
_SlcAuthGroupMenu_Object = MibTableColumn
slcAuthGroupMenu = _SlcAuthGroupMenu_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 9),
    _SlcAuthGroupMenu_Type()
)
slcAuthGroupMenu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupMenu.setStatus("current")
_SlcAuthGroupDialback_Type = EnabledState
_SlcAuthGroupDialback_Object = MibTableColumn
slcAuthGroupDialback = _SlcAuthGroupDialback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 10),
    _SlcAuthGroupDialback_Type()
)
slcAuthGroupDialback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupDialback.setStatus("current")
_SlcAuthGroupDialbackNum_Type = OctetString
_SlcAuthGroupDialbackNum_Object = MibTableColumn
slcAuthGroupDialbackNum = _SlcAuthGroupDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 3, 8, 2, 1, 11),
    _SlcAuthGroupDialbackNum_Type()
)
slcAuthGroupDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcAuthGroupDialbackNum.setStatus("current")
_SlcDevices_ObjectIdentity = ObjectIdentity
slcDevices = _SlcDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4)
)
_SlcDevConsolePort_ObjectIdentity = ObjectIdentity
slcDevConsolePort = _SlcDevConsolePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1)
)


class _SlcDevConBaud_Type(Integer32):
    """Custom type slcDevConBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SlcDevConBaud_Type.__name__ = "Integer32"
_SlcDevConBaud_Object = MibScalar
slcDevConBaud = _SlcDevConBaud_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 1),
    _SlcDevConBaud_Type()
)
slcDevConBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConBaud.setStatus("current")


class _SlcDevConDataBits_Type(Integer32):
    """Custom type slcDevConDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(8, 8),
    )


_SlcDevConDataBits_Type.__name__ = "Integer32"
_SlcDevConDataBits_Object = MibScalar
slcDevConDataBits = _SlcDevConDataBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 2),
    _SlcDevConDataBits_Type()
)
slcDevConDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConDataBits.setStatus("current")


class _SlcDevConStopBits_Type(Integer32):
    """Custom type slcDevConStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SlcDevConStopBits_Type.__name__ = "Integer32"
_SlcDevConStopBits_Object = MibScalar
slcDevConStopBits = _SlcDevConStopBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 3),
    _SlcDevConStopBits_Type()
)
slcDevConStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConStopBits.setStatus("current")


class _SlcDevConParity_Type(Integer32):
    """Custom type slcDevConParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_SlcDevConParity_Type.__name__ = "Integer32"
_SlcDevConParity_Object = MibScalar
slcDevConParity = _SlcDevConParity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 4),
    _SlcDevConParity_Type()
)
slcDevConParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConParity.setStatus("current")


class _SlcDevConFlowControl_Type(Integer32):
    """Custom type slcDevConFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rtscts", 3),
          ("xonxoff", 2))
    )


_SlcDevConFlowControl_Type.__name__ = "Integer32"
_SlcDevConFlowControl_Object = MibScalar
slcDevConFlowControl = _SlcDevConFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 5),
    _SlcDevConFlowControl_Type()
)
slcDevConFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConFlowControl.setStatus("current")


class _SlcDevConTimeout_Type(Integer32):
    """Custom type slcDevConTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcDevConTimeout_Type.__name__ = "Integer32"
_SlcDevConTimeout_Object = MibScalar
slcDevConTimeout = _SlcDevConTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 6),
    _SlcDevConTimeout_Type()
)
slcDevConTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevConTimeout.setUnits("minutes")
_SlcDevConShowLines_Type = EnabledState
_SlcDevConShowLines_Object = MibScalar
slcDevConShowLines = _SlcDevConShowLines_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 7),
    _SlcDevConShowLines_Type()
)
slcDevConShowLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConShowLines.setStatus("current")


class _SlcDevConNumberShowLines_Type(Integer32):
    """Custom type slcDevConNumberShowLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SlcDevConNumberShowLines_Type.__name__ = "Integer32"
_SlcDevConNumberShowLines_Object = MibScalar
slcDevConNumberShowLines = _SlcDevConNumberShowLines_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 8),
    _SlcDevConNumberShowLines_Type()
)
slcDevConNumberShowLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConNumberShowLines.setStatus("current")
_SlcDevConGroup_Type = OctetString
_SlcDevConGroup_Object = MibScalar
slcDevConGroup = _SlcDevConGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 1, 9),
    _SlcDevConGroup_Type()
)
slcDevConGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevConGroup.setStatus("current")
_SlcDevDevicePorts_ObjectIdentity = ObjectIdentity
slcDevDevicePorts = _SlcDevDevicePorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2)
)
_SlcDevPortGlobal_ObjectIdentity = ObjectIdentity
slcDevPortGlobal = _SlcDevPortGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1)
)
_SlcDevGlobalListenPorts_Type = OctetString
_SlcDevGlobalListenPorts_Object = MibScalar
slcDevGlobalListenPorts = _SlcDevGlobalListenPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 1),
    _SlcDevGlobalListenPorts_Type()
)
slcDevGlobalListenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalListenPorts.setStatus("obsolete")
_SlcDevGlobalDataPorts_Type = OctetString
_SlcDevGlobalDataPorts_Object = MibScalar
slcDevGlobalDataPorts = _SlcDevGlobalDataPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 2),
    _SlcDevGlobalDataPorts_Type()
)
slcDevGlobalDataPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalDataPorts.setStatus("obsolete")
_SlcDevGlobalClearPorts_Type = OctetString
_SlcDevGlobalClearPorts_Object = MibScalar
slcDevGlobalClearPorts = _SlcDevGlobalClearPorts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 3),
    _SlcDevGlobalClearPorts_Type()
)
slcDevGlobalClearPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalClearPorts.setStatus("obsolete")


class _SlcDevGlobalStartTelnetPort_Type(Integer32):
    """Custom type slcDevGlobalStartTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcDevGlobalStartTelnetPort_Type.__name__ = "Integer32"
_SlcDevGlobalStartTelnetPort_Object = MibScalar
slcDevGlobalStartTelnetPort = _SlcDevGlobalStartTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 4),
    _SlcDevGlobalStartTelnetPort_Type()
)
slcDevGlobalStartTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalStartTelnetPort.setStatus("current")


class _SlcDevGlobalStartSSHPort_Type(Integer32):
    """Custom type slcDevGlobalStartSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcDevGlobalStartSSHPort_Type.__name__ = "Integer32"
_SlcDevGlobalStartSSHPort_Object = MibScalar
slcDevGlobalStartSSHPort = _SlcDevGlobalStartSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 5),
    _SlcDevGlobalStartSSHPort_Type()
)
slcDevGlobalStartSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalStartSSHPort.setStatus("current")


class _SlcDevGlobalStartTCPPort_Type(Integer32):
    """Custom type slcDevGlobalStartTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SlcDevGlobalStartTCPPort_Type.__name__ = "Integer32"
_SlcDevGlobalStartTCPPort_Object = MibScalar
slcDevGlobalStartTCPPort = _SlcDevGlobalStartTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 6),
    _SlcDevGlobalStartTCPPort_Type()
)
slcDevGlobalStartTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalStartTCPPort.setStatus("current")


class _SlcDevGlobalMaxDirect_Type(Integer32):
    """Custom type slcDevGlobalMaxDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SlcDevGlobalMaxDirect_Type.__name__ = "Integer32"
_SlcDevGlobalMaxDirect_Object = MibScalar
slcDevGlobalMaxDirect = _SlcDevGlobalMaxDirect_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 1, 7),
    _SlcDevGlobalMaxDirect_Type()
)
slcDevGlobalMaxDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevGlobalMaxDirect.setStatus("obsolete")
_SlcDevPortConfig_ObjectIdentity = ObjectIdentity
slcDevPortConfig = _SlcDevPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2)
)


class _SlcDevPortCfgNumber_Type(Integer32):
    """Custom type slcDevPortCfgNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(48, 48),
    )


_SlcDevPortCfgNumber_Type.__name__ = "Integer32"
_SlcDevPortCfgNumber_Object = MibScalar
slcDevPortCfgNumber = _SlcDevPortCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 1),
    _SlcDevPortCfgNumber_Type()
)
slcDevPortCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNumber.setStatus("current")
_SlcDevPortCfgTable_Object = MibTable
slcDevPortCfgTable = _SlcDevPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    slcDevPortCfgTable.setStatus("current")
_SlcDevPortCfgEntry_Object = MibTableRow
slcDevPortCfgEntry = _SlcDevPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1)
)
slcDevPortCfgEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevPortId"),
)
if mibBuilder.loadTexts:
    slcDevPortCfgEntry.setStatus("current")


class _SlcDevPortId_Type(Integer32):
    """Custom type slcDevPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlcDevPortId_Type.__name__ = "Integer32"
_SlcDevPortId_Object = MibTableColumn
slcDevPortId = _SlcDevPortId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 1),
    _SlcDevPortId_Type()
)
slcDevPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortId.setStatus("current")


class _SlcDevPortCfgName_Type(OctetString):
    """Custom type slcDevPortCfgName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SlcDevPortCfgName_Type.__name__ = "OctetString"
_SlcDevPortCfgName_Object = MibTableColumn
slcDevPortCfgName = _SlcDevPortCfgName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 2),
    _SlcDevPortCfgName_Type()
)
slcDevPortCfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgName.setStatus("current")


class _SlcDevPortCfgDevice_Type(Integer32):
    """Custom type slcDevPortCfgDevice based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rpm", 10),
          ("sensorsoft", 8),
          ("servertech", 9),
          ("slp16", 3),
          ("slp16Exp16", 7),
          ("slp16Exp8", 6),
          ("slp8", 2),
          ("slp8Exp16", 5),
          ("slp8Exp8", 4))
    )


_SlcDevPortCfgDevice_Type.__name__ = "Integer32"
_SlcDevPortCfgDevice_Object = MibTableColumn
slcDevPortCfgDevice = _SlcDevPortCfgDevice_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 3),
    _SlcDevPortCfgDevice_Type()
)
slcDevPortCfgDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevice.setStatus("current")


class _SlcDevPortCfgDevLogin_Type(OctetString):
    """Custom type slcDevPortCfgDevLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcDevPortCfgDevLogin_Type.__name__ = "OctetString"
_SlcDevPortCfgDevLogin_Object = MibTableColumn
slcDevPortCfgDevLogin = _SlcDevPortCfgDevLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 4),
    _SlcDevPortCfgDevLogin_Type()
)
slcDevPortCfgDevLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevLogin.setStatus("current")
_SlcDevPortCfgBreakSeq_Type = OctetString
_SlcDevPortCfgBreakSeq_Object = MibTableColumn
slcDevPortCfgBreakSeq = _SlcDevPortCfgBreakSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 5),
    _SlcDevPortCfgBreakSeq_Type()
)
slcDevPortCfgBreakSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgBreakSeq.setStatus("current")
_SlcDevPortCfgTelnetState_Type = EnabledState
_SlcDevPortCfgTelnetState_Object = MibTableColumn
slcDevPortCfgTelnetState = _SlcDevPortCfgTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 6),
    _SlcDevPortCfgTelnetState_Type()
)
slcDevPortCfgTelnetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetState.setStatus("current")


class _SlcDevPortCfgTelnetPort_Type(Integer32):
    """Custom type slcDevPortCfgTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevPortCfgTelnetPort_Type.__name__ = "Integer32"
_SlcDevPortCfgTelnetPort_Object = MibTableColumn
slcDevPortCfgTelnetPort = _SlcDevPortCfgTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 7),
    _SlcDevPortCfgTelnetPort_Type()
)
slcDevPortCfgTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetPort.setStatus("current")
_SlcDevPortCfgTelnetAuth_Type = EnabledState
_SlcDevPortCfgTelnetAuth_Object = MibTableColumn
slcDevPortCfgTelnetAuth = _SlcDevPortCfgTelnetAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 8),
    _SlcDevPortCfgTelnetAuth_Type()
)
slcDevPortCfgTelnetAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetAuth.setStatus("current")
_SlcDevPortCfgSSHState_Type = EnabledState
_SlcDevPortCfgSSHState_Object = MibTableColumn
slcDevPortCfgSSHState = _SlcDevPortCfgSSHState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 9),
    _SlcDevPortCfgSSHState_Type()
)
slcDevPortCfgSSHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHState.setStatus("current")


class _SlcDevPortCfgSSHPort_Type(Integer32):
    """Custom type slcDevPortCfgSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevPortCfgSSHPort_Type.__name__ = "Integer32"
_SlcDevPortCfgSSHPort_Object = MibTableColumn
slcDevPortCfgSSHPort = _SlcDevPortCfgSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 10),
    _SlcDevPortCfgSSHPort_Type()
)
slcDevPortCfgSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHPort.setStatus("current")
_SlcDevPortCfgSSHAuth_Type = EnabledState
_SlcDevPortCfgSSHAuth_Object = MibTableColumn
slcDevPortCfgSSHAuth = _SlcDevPortCfgSSHAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 11),
    _SlcDevPortCfgSSHAuth_Type()
)
slcDevPortCfgSSHAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHAuth.setStatus("current")
_SlcDevPortCfgTCPState_Type = EnabledState
_SlcDevPortCfgTCPState_Object = MibTableColumn
slcDevPortCfgTCPState = _SlcDevPortCfgTCPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 12),
    _SlcDevPortCfgTCPState_Type()
)
slcDevPortCfgTCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPState.setStatus("current")


class _SlcDevPortCfgTCPPort_Type(Integer32):
    """Custom type slcDevPortCfgTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevPortCfgTCPPort_Type.__name__ = "Integer32"
_SlcDevPortCfgTCPPort_Object = MibTableColumn
slcDevPortCfgTCPPort = _SlcDevPortCfgTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 13),
    _SlcDevPortCfgTCPPort_Type()
)
slcDevPortCfgTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPPort.setStatus("current")
_SlcDevPortCfgTCPAuth_Type = EnabledState
_SlcDevPortCfgTCPAuth_Object = MibTableColumn
slcDevPortCfgTCPAuth = _SlcDevPortCfgTCPAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 14),
    _SlcDevPortCfgTCPAuth_Type()
)
slcDevPortCfgTCPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPAuth.setStatus("current")
_SlcDevPortCfgIP_Type = IpAddress
_SlcDevPortCfgIP_Object = MibTableColumn
slcDevPortCfgIP = _SlcDevPortCfgIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 15),
    _SlcDevPortCfgIP_Type()
)
slcDevPortCfgIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgIP.setStatus("current")


class _SlcDevPortCfgBaud_Type(Integer32):
    """Custom type slcDevPortCfgBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SlcDevPortCfgBaud_Type.__name__ = "Integer32"
_SlcDevPortCfgBaud_Object = MibTableColumn
slcDevPortCfgBaud = _SlcDevPortCfgBaud_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 16),
    _SlcDevPortCfgBaud_Type()
)
slcDevPortCfgBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgBaud.setStatus("current")


class _SlcDevPortCfgDataBits_Type(Integer32):
    """Custom type slcDevPortCfgDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(8, 8),
    )


_SlcDevPortCfgDataBits_Type.__name__ = "Integer32"
_SlcDevPortCfgDataBits_Object = MibTableColumn
slcDevPortCfgDataBits = _SlcDevPortCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 17),
    _SlcDevPortCfgDataBits_Type()
)
slcDevPortCfgDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDataBits.setStatus("current")


class _SlcDevPortCfgStopBits_Type(Integer32):
    """Custom type slcDevPortCfgStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SlcDevPortCfgStopBits_Type.__name__ = "Integer32"
_SlcDevPortCfgStopBits_Object = MibTableColumn
slcDevPortCfgStopBits = _SlcDevPortCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 18),
    _SlcDevPortCfgStopBits_Type()
)
slcDevPortCfgStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgStopBits.setStatus("current")


class _SlcDevPortCfgParity_Type(Integer32):
    """Custom type slcDevPortCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_SlcDevPortCfgParity_Type.__name__ = "Integer32"
_SlcDevPortCfgParity_Object = MibTableColumn
slcDevPortCfgParity = _SlcDevPortCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 19),
    _SlcDevPortCfgParity_Type()
)
slcDevPortCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgParity.setStatus("current")


class _SlcDevPortCfgFlowControl_Type(Integer32):
    """Custom type slcDevPortCfgFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rtscts", 3),
          ("xonxoff", 2))
    )


_SlcDevPortCfgFlowControl_Type.__name__ = "Integer32"
_SlcDevPortCfgFlowControl_Object = MibTableColumn
slcDevPortCfgFlowControl = _SlcDevPortCfgFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 20),
    _SlcDevPortCfgFlowControl_Type()
)
slcDevPortCfgFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgFlowControl.setStatus("current")
_SlcDevPortCfgLogins_Type = EnabledState
_SlcDevPortCfgLogins_Object = MibTableColumn
slcDevPortCfgLogins = _SlcDevPortCfgLogins_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 21),
    _SlcDevPortCfgLogins_Type()
)
slcDevPortCfgLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgLogins.setStatus("current")
_SlcDevPortCfgConnectDSR_Type = EnabledState
_SlcDevPortCfgConnectDSR_Object = MibTableColumn
slcDevPortCfgConnectDSR = _SlcDevPortCfgConnectDSR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 22),
    _SlcDevPortCfgConnectDSR_Type()
)
slcDevPortCfgConnectDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgConnectDSR.setStatus("current")
_SlcDevPortCfgDisconnectDSR_Type = EnabledState
_SlcDevPortCfgDisconnectDSR_Object = MibTableColumn
slcDevPortCfgDisconnectDSR = _SlcDevPortCfgDisconnectDSR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 23),
    _SlcDevPortCfgDisconnectDSR_Type()
)
slcDevPortCfgDisconnectDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDisconnectDSR.setStatus("current")


class _SlcDevPortCfgModemState_Type(Integer32):
    """Custom type slcDevPortCfgModemState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cbcpClient", 9),
          ("cbcpServer", 8),
          ("dialback", 4),
          ("dialin", 3),
          ("dialinAndDialondemand", 6),
          ("dialinHostList", 7),
          ("dialondemand", 5),
          ("dialout", 2),
          ("disabled", 1))
    )


_SlcDevPortCfgModemState_Type.__name__ = "Integer32"
_SlcDevPortCfgModemState_Object = MibTableColumn
slcDevPortCfgModemState = _SlcDevPortCfgModemState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 24),
    _SlcDevPortCfgModemState_Type()
)
slcDevPortCfgModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgModemState.setStatus("current")


class _SlcDevPortCfgModemMode_Type(Integer32):
    """Custom type slcDevPortCfgModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("text", 2))
    )


_SlcDevPortCfgModemMode_Type.__name__ = "Integer32"
_SlcDevPortCfgModemMode_Object = MibTableColumn
slcDevPortCfgModemMode = _SlcDevPortCfgModemMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 25),
    _SlcDevPortCfgModemMode_Type()
)
slcDevPortCfgModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgModemMode.setStatus("current")
_SlcDevPortCfgLocalIP_Type = IpAddress
_SlcDevPortCfgLocalIP_Object = MibTableColumn
slcDevPortCfgLocalIP = _SlcDevPortCfgLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 26),
    _SlcDevPortCfgLocalIP_Type()
)
slcDevPortCfgLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgLocalIP.setStatus("current")
_SlcDevPortCfgRemoteIP_Type = IpAddress
_SlcDevPortCfgRemoteIP_Object = MibTableColumn
slcDevPortCfgRemoteIP = _SlcDevPortCfgRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 27),
    _SlcDevPortCfgRemoteIP_Type()
)
slcDevPortCfgRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgRemoteIP.setStatus("current")


class _SlcDevPortCfgAuth_Type(Integer32):
    """Custom type slcDevPortCfgAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcDevPortCfgAuth_Type.__name__ = "Integer32"
_SlcDevPortCfgAuth_Object = MibTableColumn
slcDevPortCfgAuth = _SlcDevPortCfgAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 28),
    _SlcDevPortCfgAuth_Type()
)
slcDevPortCfgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgAuth.setStatus("current")
_SlcDevPortCfgCHAPHost_Type = OctetString
_SlcDevPortCfgCHAPHost_Object = MibTableColumn
slcDevPortCfgCHAPHost = _SlcDevPortCfgCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 29),
    _SlcDevPortCfgCHAPHost_Type()
)
slcDevPortCfgCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCHAPHost.setStatus("current")
_SlcDevPortCfgInitScript_Type = OctetString
_SlcDevPortCfgInitScript_Object = MibTableColumn
slcDevPortCfgInitScript = _SlcDevPortCfgInitScript_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 30),
    _SlcDevPortCfgInitScript_Type()
)
slcDevPortCfgInitScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgInitScript.setStatus("current")


class _SlcDevPortCfgTimeout_Type(Integer32):
    """Custom type slcDevPortCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcDevPortCfgTimeout_Type.__name__ = "Integer32"
_SlcDevPortCfgTimeout_Object = MibTableColumn
slcDevPortCfgTimeout = _SlcDevPortCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 31),
    _SlcDevPortCfgTimeout_Type()
)
slcDevPortCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgTimeout.setUnits("minutes")
_SlcDevPortCfgDialoutNum_Type = OctetString
_SlcDevPortCfgDialoutNum_Object = MibTableColumn
slcDevPortCfgDialoutNum = _SlcDevPortCfgDialoutNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 32),
    _SlcDevPortCfgDialoutNum_Type()
)
slcDevPortCfgDialoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialoutNum.setStatus("current")


class _SlcDevPortCfgDialoutLogin_Type(OctetString):
    """Custom type slcDevPortCfgDialoutLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcDevPortCfgDialoutLogin_Type.__name__ = "OctetString"
_SlcDevPortCfgDialoutLogin_Object = MibTableColumn
slcDevPortCfgDialoutLogin = _SlcDevPortCfgDialoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 33),
    _SlcDevPortCfgDialoutLogin_Type()
)
slcDevPortCfgDialoutLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialoutLogin.setStatus("current")


class _SlcDevPortCfgDialbackMode_Type(Integer32):
    """Custom type slcDevPortCfgDialbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("usernumber", 1))
    )


_SlcDevPortCfgDialbackMode_Type.__name__ = "Integer32"
_SlcDevPortCfgDialbackMode_Object = MibTableColumn
slcDevPortCfgDialbackMode = _SlcDevPortCfgDialbackMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 34),
    _SlcDevPortCfgDialbackMode_Type()
)
slcDevPortCfgDialbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialbackMode.setStatus("current")
_SlcDevPortCfgDialbackNum_Type = OctetString
_SlcDevPortCfgDialbackNum_Object = MibTableColumn
slcDevPortCfgDialbackNum = _SlcDevPortCfgDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 35),
    _SlcDevPortCfgDialbackNum_Type()
)
slcDevPortCfgDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialbackNum.setStatus("current")
_SlcDevPortCfgNATState_Type = EnabledState
_SlcDevPortCfgNATState_Object = MibTableColumn
slcDevPortCfgNATState = _SlcDevPortCfgNATState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 36),
    _SlcDevPortCfgNATState_Type()
)
slcDevPortCfgNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNATState.setStatus("current")
_SlcDevPortCfgLocalState_Type = EnabledState
_SlcDevPortCfgLocalState_Object = MibTableColumn
slcDevPortCfgLocalState = _SlcDevPortCfgLocalState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 37),
    _SlcDevPortCfgLocalState_Type()
)
slcDevPortCfgLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgLocalState.setStatus("current")
_SlcDevPortCfgNFSFileState_Type = EnabledState
_SlcDevPortCfgNFSFileState_Object = MibTableColumn
slcDevPortCfgNFSFileState = _SlcDevPortCfgNFSFileState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 38),
    _SlcDevPortCfgNFSFileState_Type()
)
slcDevPortCfgNFSFileState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNFSFileState.setStatus("current")
_SlcDevPortCfgNFSDir_Type = OctetString
_SlcDevPortCfgNFSDir_Object = MibTableColumn
slcDevPortCfgNFSDir = _SlcDevPortCfgNFSDir_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 39),
    _SlcDevPortCfgNFSDir_Type()
)
slcDevPortCfgNFSDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNFSDir.setStatus("current")
_SlcDevPortCfgNFSMaxFiles_Type = Integer32
_SlcDevPortCfgNFSMaxFiles_Object = MibTableColumn
slcDevPortCfgNFSMaxFiles = _SlcDevPortCfgNFSMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 40),
    _SlcDevPortCfgNFSMaxFiles_Type()
)
slcDevPortCfgNFSMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNFSMaxFiles.setStatus("current")
_SlcDevPortCfgNFSMaxSize_Type = Integer32
_SlcDevPortCfgNFSMaxSize_Object = MibTableColumn
slcDevPortCfgNFSMaxSize = _SlcDevPortCfgNFSMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 41),
    _SlcDevPortCfgNFSMaxSize_Type()
)
slcDevPortCfgNFSMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNFSMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgNFSMaxSize.setUnits("bytes")
_SlcDevPortCfgEmailState_Type = EnabledState
_SlcDevPortCfgEmailState_Object = MibTableColumn
slcDevPortCfgEmailState = _SlcDevPortCfgEmailState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 42),
    _SlcDevPortCfgEmailState_Type()
)
slcDevPortCfgEmailState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailState.setStatus("current")


class _SlcDevPortCfgEmailTrigger_Type(Integer32):
    """Custom type slcDevPortCfgEmailTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytecnt", 1),
          ("textstring", 2))
    )


_SlcDevPortCfgEmailTrigger_Type.__name__ = "Integer32"
_SlcDevPortCfgEmailTrigger_Object = MibTableColumn
slcDevPortCfgEmailTrigger = _SlcDevPortCfgEmailTrigger_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 43),
    _SlcDevPortCfgEmailTrigger_Type()
)
slcDevPortCfgEmailTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailTrigger.setStatus("current")
_SlcDevPortCfgEmailByteThresh_Type = Integer32
_SlcDevPortCfgEmailByteThresh_Object = MibTableColumn
slcDevPortCfgEmailByteThresh = _SlcDevPortCfgEmailByteThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 44),
    _SlcDevPortCfgEmailByteThresh_Type()
)
slcDevPortCfgEmailByteThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailByteThresh.setStatus("current")
_SlcDevPortCfgEmailDelay_Type = Integer32
_SlcDevPortCfgEmailDelay_Object = MibTableColumn
slcDevPortCfgEmailDelay = _SlcDevPortCfgEmailDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 45),
    _SlcDevPortCfgEmailDelay_Type()
)
slcDevPortCfgEmailDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailDelay.setUnits("seconds")
_SlcDevPortCfgEmailRestartDelay_Type = Integer32
_SlcDevPortCfgEmailRestartDelay_Object = MibTableColumn
slcDevPortCfgEmailRestartDelay = _SlcDevPortCfgEmailRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 46),
    _SlcDevPortCfgEmailRestartDelay_Type()
)
slcDevPortCfgEmailRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailRestartDelay.setUnits("seconds")
_SlcDevPortCfgEmailTextString_Type = OctetString
_SlcDevPortCfgEmailTextString_Object = MibTableColumn
slcDevPortCfgEmailTextString = _SlcDevPortCfgEmailTextString_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 47),
    _SlcDevPortCfgEmailTextString_Type()
)
slcDevPortCfgEmailTextString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailTextString.setStatus("current")
_SlcDevPortCfgEmailTo_Type = OctetString
_SlcDevPortCfgEmailTo_Object = MibTableColumn
slcDevPortCfgEmailTo = _SlcDevPortCfgEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 48),
    _SlcDevPortCfgEmailTo_Type()
)
slcDevPortCfgEmailTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailTo.setStatus("current")
_SlcDevPortCfgEmailSubject_Type = OctetString
_SlcDevPortCfgEmailSubject_Object = MibTableColumn
slcDevPortCfgEmailSubject = _SlcDevPortCfgEmailSubject_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 49),
    _SlcDevPortCfgEmailSubject_Type()
)
slcDevPortCfgEmailSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailSubject.setStatus("current")
_SlcDevPortCfgPCCardState_Type = EnabledState
_SlcDevPortCfgPCCardState_Object = MibTableColumn
slcDevPortCfgPCCardState = _SlcDevPortCfgPCCardState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 50),
    _SlcDevPortCfgPCCardState_Type()
)
slcDevPortCfgPCCardState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPCCardState.setStatus("current")


class _SlcDevPortCfgPCCardLogTo_Type(Integer32):
    """Custom type slcDevPortCfgPCCardLogTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerSlot", 2),
          ("upperSlot", 1))
    )


_SlcDevPortCfgPCCardLogTo_Type.__name__ = "Integer32"
_SlcDevPortCfgPCCardLogTo_Object = MibTableColumn
slcDevPortCfgPCCardLogTo = _SlcDevPortCfgPCCardLogTo_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 51),
    _SlcDevPortCfgPCCardLogTo_Type()
)
slcDevPortCfgPCCardLogTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPCCardLogTo.setStatus("current")
_SlcDevPortCfgPCCardMaxFiles_Type = Integer32
_SlcDevPortCfgPCCardMaxFiles_Object = MibTableColumn
slcDevPortCfgPCCardMaxFiles = _SlcDevPortCfgPCCardMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 52),
    _SlcDevPortCfgPCCardMaxFiles_Type()
)
slcDevPortCfgPCCardMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPCCardMaxFiles.setStatus("current")
_SlcDevPortCfgPCCardMaxSize_Type = Integer32
_SlcDevPortCfgPCCardMaxSize_Object = MibTableColumn
slcDevPortCfgPCCardMaxSize = _SlcDevPortCfgPCCardMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 53),
    _SlcDevPortCfgPCCardMaxSize_Type()
)
slcDevPortCfgPCCardMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPCCardMaxSize.setStatus("current")


class _SlcDevPortCfgAction_Type(Integer32):
    """Custom type slcDevPortCfgAction based on Integer32"""
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
        *(("clearLocalLog", 3),
          ("noAction", 1),
          ("terminateConnections", 4),
          ("zeroPortCounters", 2))
    )


_SlcDevPortCfgAction_Type.__name__ = "Integer32"
_SlcDevPortCfgAction_Object = MibTableColumn
slcDevPortCfgAction = _SlcDevPortCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 54),
    _SlcDevPortCfgAction_Type()
)
slcDevPortCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcDevPortCfgAction.setStatus("current")


class _SlcDevPortCfgEmailSend_Type(Integer32):
    """Custom type slcDevPortCfgEmailSend based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("email", 1),
          ("snmptrap", 2))
    )


_SlcDevPortCfgEmailSend_Type.__name__ = "Integer32"
_SlcDevPortCfgEmailSend_Object = MibTableColumn
slcDevPortCfgEmailSend = _SlcDevPortCfgEmailSend_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 55),
    _SlcDevPortCfgEmailSend_Type()
)
slcDevPortCfgEmailSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgEmailSend.setStatus("current")
_SlcDevPortCfgBanner_Type = OctetString
_SlcDevPortCfgBanner_Object = MibTableColumn
slcDevPortCfgBanner = _SlcDevPortCfgBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 56),
    _SlcDevPortCfgBanner_Type()
)
slcDevPortCfgBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgBanner.setStatus("current")
_SlcDevPortCfgIdleTimeout_Type = Integer32
_SlcDevPortCfgIdleTimeout_Object = MibTableColumn
slcDevPortCfgIdleTimeout = _SlcDevPortCfgIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 57),
    _SlcDevPortCfgIdleTimeout_Type()
)
slcDevPortCfgIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgIdleTimeout.setUnits("seconds")
_SlcDevPortCfgRestartDelay_Type = Integer32
_SlcDevPortCfgRestartDelay_Object = MibTableColumn
slcDevPortCfgRestartDelay = _SlcDevPortCfgRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 58),
    _SlcDevPortCfgRestartDelay_Type()
)
slcDevPortCfgRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgRestartDelay.setUnits("seconds")
_SlcDevPortCfgCallerIdLogging_Type = EnabledState
_SlcDevPortCfgCallerIdLogging_Object = MibTableColumn
slcDevPortCfgCallerIdLogging = _SlcDevPortCfgCallerIdLogging_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 59),
    _SlcDevPortCfgCallerIdLogging_Type()
)
slcDevPortCfgCallerIdLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCallerIdLogging.setStatus("current")
_SlcDevPortCfgCallerIdATCmd_Type = OctetString
_SlcDevPortCfgCallerIdATCmd_Object = MibTableColumn
slcDevPortCfgCallerIdATCmd = _SlcDevPortCfgCallerIdATCmd_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 60),
    _SlcDevPortCfgCallerIdATCmd_Type()
)
slcDevPortCfgCallerIdATCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCallerIdATCmd.setStatus("current")


class _SlcDevPortCfgDODAuth_Type(Integer32):
    """Custom type slcDevPortCfgDODAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcDevPortCfgDODAuth_Type.__name__ = "Integer32"
_SlcDevPortCfgDODAuth_Object = MibTableColumn
slcDevPortCfgDODAuth = _SlcDevPortCfgDODAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 61),
    _SlcDevPortCfgDODAuth_Type()
)
slcDevPortCfgDODAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDODAuth.setStatus("current")
_SlcDevPortCfgDODCHAPHost_Type = OctetString
_SlcDevPortCfgDODCHAPHost_Object = MibTableColumn
slcDevPortCfgDODCHAPHost = _SlcDevPortCfgDODCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 62),
    _SlcDevPortCfgDODCHAPHost_Type()
)
slcDevPortCfgDODCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDODCHAPHost.setStatus("current")
_SlcDevPortCfgSLMLoggingState_Type = EnabledState
_SlcDevPortCfgSLMLoggingState_Object = MibTableColumn
slcDevPortCfgSLMLoggingState = _SlcDevPortCfgSLMLoggingState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 63),
    _SlcDevPortCfgSLMLoggingState_Type()
)
slcDevPortCfgSLMLoggingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMLoggingState.setStatus("current")
_SlcDevPortCfgSLMNMS_Type = OctetString
_SlcDevPortCfgSLMNMS_Object = MibTableColumn
slcDevPortCfgSLMNMS = _SlcDevPortCfgSLMNMS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 64),
    _SlcDevPortCfgSLMNMS_Type()
)
slcDevPortCfgSLMNMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMNMS.setStatus("current")
_SlcDevPortCfgSLMByteThresh_Type = Integer32
_SlcDevPortCfgSLMByteThresh_Object = MibTableColumn
slcDevPortCfgSLMByteThresh = _SlcDevPortCfgSLMByteThresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 65),
    _SlcDevPortCfgSLMByteThresh_Type()
)
slcDevPortCfgSLMByteThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMByteThresh.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMByteThresh.setUnits("bytes")
_SlcDevPortCfgSLMTimeFrame_Type = Integer32
_SlcDevPortCfgSLMTimeFrame_Object = MibTableColumn
slcDevPortCfgSLMTimeFrame = _SlcDevPortCfgSLMTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 66),
    _SlcDevPortCfgSLMTimeFrame_Type()
)
slcDevPortCfgSLMTimeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMTimeFrame.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgSLMTimeFrame.setUnits("seconds")
_SlcDevPortCfgWebColumns_Type = Integer32
_SlcDevPortCfgWebColumns_Object = MibTableColumn
slcDevPortCfgWebColumns = _SlcDevPortCfgWebColumns_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 67),
    _SlcDevPortCfgWebColumns_Type()
)
slcDevPortCfgWebColumns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgWebColumns.setStatus("current")
_SlcDevPortCfgWebRows_Type = Integer32
_SlcDevPortCfgWebRows_Object = MibTableColumn
slcDevPortCfgWebRows = _SlcDevPortCfgWebRows_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 68),
    _SlcDevPortCfgWebRows_Type()
)
slcDevPortCfgWebRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgWebRows.setStatus("current")
_SlcDevPortCfgSyslogState_Type = EnabledState
_SlcDevPortCfgSyslogState_Object = MibTableColumn
slcDevPortCfgSyslogState = _SlcDevPortCfgSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 69),
    _SlcDevPortCfgSyslogState_Type()
)
slcDevPortCfgSyslogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSyslogState.setStatus("current")
_SlcDevPortCfgHostList_Type = OctetString
_SlcDevPortCfgHostList_Object = MibTableColumn
slcDevPortCfgHostList = _SlcDevPortCfgHostList_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 70),
    _SlcDevPortCfgHostList_Type()
)
slcDevPortCfgHostList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgHostList.setStatus("current")
_SlcDevPortCfgDevLowTemp_Type = Integer32
_SlcDevPortCfgDevLowTemp_Object = MibTableColumn
slcDevPortCfgDevLowTemp = _SlcDevPortCfgDevLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 71),
    _SlcDevPortCfgDevLowTemp_Type()
)
slcDevPortCfgDevLowTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevLowTemp.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgDevLowTemp.setUnits("Celsius")
_SlcDevPortCfgDevHighTemp_Type = Integer32
_SlcDevPortCfgDevHighTemp_Object = MibTableColumn
slcDevPortCfgDevHighTemp = _SlcDevPortCfgDevHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 72),
    _SlcDevPortCfgDevHighTemp_Type()
)
slcDevPortCfgDevHighTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevHighTemp.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgDevHighTemp.setUnits("Celsius")
_SlcDevPortCfgDevTemperature_Type = OctetString
_SlcDevPortCfgDevTemperature_Object = MibTableColumn
slcDevPortCfgDevTemperature = _SlcDevPortCfgDevTemperature_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 73),
    _SlcDevPortCfgDevTemperature_Type()
)
slcDevPortCfgDevTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevTemperature.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgDevTemperature.setUnits("Celsius")
_SlcDevPortCfgDevLowHumidity_Type = Integer32
_SlcDevPortCfgDevLowHumidity_Object = MibTableColumn
slcDevPortCfgDevLowHumidity = _SlcDevPortCfgDevLowHumidity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 74),
    _SlcDevPortCfgDevLowHumidity_Type()
)
slcDevPortCfgDevLowHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevLowHumidity.setStatus("current")
_SlcDevPortCfgDevHighHumidity_Type = Integer32
_SlcDevPortCfgDevHighHumidity_Object = MibTableColumn
slcDevPortCfgDevHighHumidity = _SlcDevPortCfgDevHighHumidity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 75),
    _SlcDevPortCfgDevHighHumidity_Type()
)
slcDevPortCfgDevHighHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevHighHumidity.setStatus("current")
_SlcDevPortCfgDevHumidity_Type = OctetString
_SlcDevPortCfgDevHumidity_Object = MibTableColumn
slcDevPortCfgDevHumidity = _SlcDevPortCfgDevHumidity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 76),
    _SlcDevPortCfgDevHumidity_Type()
)
slcDevPortCfgDevHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevHumidity.setStatus("current")
_SlcDevPortCfgDevTraps_Type = EnabledState
_SlcDevPortCfgDevTraps_Object = MibTableColumn
slcDevPortCfgDevTraps = _SlcDevPortCfgDevTraps_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 77),
    _SlcDevPortCfgDevTraps_Type()
)
slcDevPortCfgDevTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevTraps.setStatus("current")
_SlcDevPortCfgShowLines_Type = EnabledState
_SlcDevPortCfgShowLines_Object = MibTableColumn
slcDevPortCfgShowLines = _SlcDevPortCfgShowLines_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 78),
    _SlcDevPortCfgShowLines_Type()
)
slcDevPortCfgShowLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgShowLines.setStatus("current")


class _SlcDevPortCfgNumberShowLines_Type(Integer32):
    """Custom type slcDevPortCfgNumberShowLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_SlcDevPortCfgNumberShowLines_Type.__name__ = "Integer32"
_SlcDevPortCfgNumberShowLines_Object = MibTableColumn
slcDevPortCfgNumberShowLines = _SlcDevPortCfgNumberShowLines_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 79),
    _SlcDevPortCfgNumberShowLines_Type()
)
slcDevPortCfgNumberShowLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNumberShowLines.setStatus("current")
_SlcDevPortCfgViewPortLog_Type = EnabledState
_SlcDevPortCfgViewPortLog_Object = MibTableColumn
slcDevPortCfgViewPortLog = _SlcDevPortCfgViewPortLog_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 80),
    _SlcDevPortCfgViewPortLog_Type()
)
slcDevPortCfgViewPortLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgViewPortLog.setStatus("current")
_SlcDevPortCfgPortLogSeq_Type = OctetString
_SlcDevPortCfgPortLogSeq_Object = MibTableColumn
slcDevPortCfgPortLogSeq = _SlcDevPortCfgPortLogSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 81),
    _SlcDevPortCfgPortLogSeq_Type()
)
slcDevPortCfgPortLogSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPortLogSeq.setStatus("current")
_SlcDevPortCfgMaxDirectConnects_Type = Integer32
_SlcDevPortCfgMaxDirectConnects_Object = MibTableColumn
slcDevPortCfgMaxDirectConnects = _SlcDevPortCfgMaxDirectConnects_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 82),
    _SlcDevPortCfgMaxDirectConnects_Type()
)
slcDevPortCfgMaxDirectConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgMaxDirectConnects.setStatus("current")


class _SlcDevPortCfgTelnetTimeout_Type(Integer32):
    """Custom type slcDevPortCfgTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SlcDevPortCfgTelnetTimeout_Type.__name__ = "Integer32"
_SlcDevPortCfgTelnetTimeout_Object = MibTableColumn
slcDevPortCfgTelnetTimeout = _SlcDevPortCfgTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 83),
    _SlcDevPortCfgTelnetTimeout_Type()
)
slcDevPortCfgTelnetTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetTimeout.setUnits("seconds")


class _SlcDevPortCfgSSHTimeout_Type(Integer32):
    """Custom type slcDevPortCfgSSHTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SlcDevPortCfgSSHTimeout_Type.__name__ = "Integer32"
_SlcDevPortCfgSSHTimeout_Object = MibTableColumn
slcDevPortCfgSSHTimeout = _SlcDevPortCfgSSHTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 84),
    _SlcDevPortCfgSSHTimeout_Type()
)
slcDevPortCfgSSHTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHTimeout.setUnits("seconds")


class _SlcDevPortCfgTCPTimeout_Type(Integer32):
    """Custom type slcDevPortCfgTCPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SlcDevPortCfgTCPTimeout_Type.__name__ = "Integer32"
_SlcDevPortCfgTCPTimeout_Object = MibTableColumn
slcDevPortCfgTCPTimeout = _SlcDevPortCfgTCPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 85),
    _SlcDevPortCfgTCPTimeout_Type()
)
slcDevPortCfgTCPTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPTimeout.setUnits("seconds")


class _SlcDevPortCfgCBCPClientType_Type(Integer32):
    """Custom type slcDevPortCfgCBCPClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminDefined", 1),
          ("userDefined", 2))
    )


_SlcDevPortCfgCBCPClientType_Type.__name__ = "Integer32"
_SlcDevPortCfgCBCPClientType_Object = MibTableColumn
slcDevPortCfgCBCPClientType = _SlcDevPortCfgCBCPClientType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 86),
    _SlcDevPortCfgCBCPClientType_Type()
)
slcDevPortCfgCBCPClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCBCPClientType.setStatus("current")
_SlcDevPortCfgCBCPServerAllowNoCallback_Type = EnabledState
_SlcDevPortCfgCBCPServerAllowNoCallback_Object = MibTableColumn
slcDevPortCfgCBCPServerAllowNoCallback = _SlcDevPortCfgCBCPServerAllowNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 87),
    _SlcDevPortCfgCBCPServerAllowNoCallback_Type()
)
slcDevPortCfgCBCPServerAllowNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCBCPServerAllowNoCallback.setStatus("current")
_SlcDevPortCfgDialbackDelay_Type = Integer32
_SlcDevPortCfgDialbackDelay_Object = MibTableColumn
slcDevPortCfgDialbackDelay = _SlcDevPortCfgDialbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 88),
    _SlcDevPortCfgDialbackDelay_Type()
)
slcDevPortCfgDialbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgDialbackDelay.setUnits("seconds")
_SlcDevPortCfgUSBState_Type = EnabledState
_SlcDevPortCfgUSBState_Object = MibTableColumn
slcDevPortCfgUSBState = _SlcDevPortCfgUSBState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 89),
    _SlcDevPortCfgUSBState_Type()
)
slcDevPortCfgUSBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBState.setStatus("current")
_SlcDevPortCfgUSBLogTo_Type = Integer32
_SlcDevPortCfgUSBLogTo_Object = MibTableColumn
slcDevPortCfgUSBLogTo = _SlcDevPortCfgUSBLogTo_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 90),
    _SlcDevPortCfgUSBLogTo_Type()
)
slcDevPortCfgUSBLogTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBLogTo.setStatus("current")
_SlcDevPortCfgUSBMaxFiles_Type = Integer32
_SlcDevPortCfgUSBMaxFiles_Object = MibTableColumn
slcDevPortCfgUSBMaxFiles = _SlcDevPortCfgUSBMaxFiles_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 91),
    _SlcDevPortCfgUSBMaxFiles_Type()
)
slcDevPortCfgUSBMaxFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBMaxFiles.setStatus("current")
_SlcDevPortCfgUSBMaxSize_Type = Integer32
_SlcDevPortCfgUSBMaxSize_Object = MibTableColumn
slcDevPortCfgUSBMaxSize = _SlcDevPortCfgUSBMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 92),
    _SlcDevPortCfgUSBMaxSize_Type()
)
slcDevPortCfgUSBMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBMaxSize.setUnits("bytes")
_SlcDevPortCfgCHAPAuthLocalUsers_Type = EnabledState
_SlcDevPortCfgCHAPAuthLocalUsers_Object = MibTableColumn
slcDevPortCfgCHAPAuthLocalUsers = _SlcDevPortCfgCHAPAuthLocalUsers_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 93),
    _SlcDevPortCfgCHAPAuthLocalUsers_Type()
)
slcDevPortCfgCHAPAuthLocalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgCHAPAuthLocalUsers.setStatus("current")
_SlcDevPortCfgUseSites_Type = EnabledState
_SlcDevPortCfgUseSites_Object = MibTableColumn
slcDevPortCfgUseSites = _SlcDevPortCfgUseSites_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 94),
    _SlcDevPortCfgUseSites_Type()
)
slcDevPortCfgUseSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUseSites.setStatus("current")
_SlcDevPortCfgDialbackRetries_Type = Integer32
_SlcDevPortCfgDialbackRetries_Object = MibTableColumn
slcDevPortCfgDialbackRetries = _SlcDevPortCfgDialbackRetries_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 95),
    _SlcDevPortCfgDialbackRetries_Type()
)
slcDevPortCfgDialbackRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDialbackRetries.setStatus("current")
_SlcDevPortCfgGroup_Type = OctetString
_SlcDevPortCfgGroup_Object = MibTableColumn
slcDevPortCfgGroup = _SlcDevPortCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 96),
    _SlcDevPortCfgGroup_Type()
)
slcDevPortCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgGroup.setStatus("current")
_SlcDevPortCfgIPMask_Type = IpAddress
_SlcDevPortCfgIPMask_Object = MibTableColumn
slcDevPortCfgIPMask = _SlcDevPortCfgIPMask_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 97),
    _SlcDevPortCfgIPMask_Type()
)
slcDevPortCfgIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgIPMask.setStatus("current")
_SlcDevPortCfgDevPrompt_Type = OctetString
_SlcDevPortCfgDevPrompt_Object = MibTableColumn
slcDevPortCfgDevPrompt = _SlcDevPortCfgDevPrompt_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 98),
    _SlcDevPortCfgDevPrompt_Type()
)
slcDevPortCfgDevPrompt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevPrompt.setStatus("current")
_SlcDevPortCfgDevNumOutlets_Type = Integer32
_SlcDevPortCfgDevNumOutlets_Object = MibTableColumn
slcDevPortCfgDevNumOutlets = _SlcDevPortCfgDevNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 99),
    _SlcDevPortCfgDevNumOutlets_Type()
)
slcDevPortCfgDevNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevNumOutlets.setStatus("current")
_SlcDevPortCfgDevNumExpOutlets_Type = Integer32
_SlcDevPortCfgDevNumExpOutlets_Object = MibTableColumn
slcDevPortCfgDevNumExpOutlets = _SlcDevPortCfgDevNumExpOutlets_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 100),
    _SlcDevPortCfgDevNumExpOutlets_Type()
)
slcDevPortCfgDevNumExpOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgDevNumExpOutlets.setStatus("current")
_SlcDevPortCfgReversePinout_Type = EnabledState
_SlcDevPortCfgReversePinout_Object = MibTableColumn
slcDevPortCfgReversePinout = _SlcDevPortCfgReversePinout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 101),
    _SlcDevPortCfgReversePinout_Type()
)
slcDevPortCfgReversePinout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgReversePinout.setStatus("current")
_SlcDevPortCfgUSBVBUS_Type = EnabledState
_SlcDevPortCfgUSBVBUS_Object = MibTableColumn
slcDevPortCfgUSBVBUS = _SlcDevPortCfgUSBVBUS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 102),
    _SlcDevPortCfgUSBVBUS_Type()
)
slcDevPortCfgUSBVBUS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgUSBVBUS.setStatus("current")
_SlcDevPortCfgAssertDTR_Type = EnabledState
_SlcDevPortCfgAssertDTR_Object = MibTableColumn
slcDevPortCfgAssertDTR = _SlcDevPortCfgAssertDTR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 103),
    _SlcDevPortCfgAssertDTR_Type()
)
slcDevPortCfgAssertDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgAssertDTR.setStatus("current")


class _SlcDevPortCfgPortType_Type(Integer32):
    """Custom type slcDevPortCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rj45", 1),
          ("usb", 2))
    )


_SlcDevPortCfgPortType_Type.__name__ = "Integer32"
_SlcDevPortCfgPortType_Object = MibTableColumn
slcDevPortCfgPortType = _SlcDevPortCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 104),
    _SlcDevPortCfgPortType_Type()
)
slcDevPortCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPortType.setStatus("current")
_SlcDevPortCfgTelnetTimeoutDataDirection_Type = TimeoutDataDirection
_SlcDevPortCfgTelnetTimeoutDataDirection_Object = MibTableColumn
slcDevPortCfgTelnetTimeoutDataDirection = _SlcDevPortCfgTelnetTimeoutDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 105),
    _SlcDevPortCfgTelnetTimeoutDataDirection_Type()
)
slcDevPortCfgTelnetTimeoutDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetTimeoutDataDirection.setStatus("current")
_SlcDevPortCfgSSHTimeoutDataDirection_Type = TimeoutDataDirection
_SlcDevPortCfgSSHTimeoutDataDirection_Object = MibTableColumn
slcDevPortCfgSSHTimeoutDataDirection = _SlcDevPortCfgSSHTimeoutDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 106),
    _SlcDevPortCfgSSHTimeoutDataDirection_Type()
)
slcDevPortCfgSSHTimeoutDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSSHTimeoutDataDirection.setStatus("current")
_SlcDevPortCfgTCPTimeoutDataDirection_Type = TimeoutDataDirection
_SlcDevPortCfgTCPTimeoutDataDirection_Object = MibTableColumn
slcDevPortCfgTCPTimeoutDataDirection = _SlcDevPortCfgTCPTimeoutDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 107),
    _SlcDevPortCfgTCPTimeoutDataDirection_Type()
)
slcDevPortCfgTCPTimeoutDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTCPTimeoutDataDirection.setStatus("current")
_SlcDevPortCfgIdleTimeoutMessage_Type = EnabledState
_SlcDevPortCfgIdleTimeoutMessage_Object = MibTableColumn
slcDevPortCfgIdleTimeoutMessage = _SlcDevPortCfgIdleTimeoutMessage_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 108),
    _SlcDevPortCfgIdleTimeoutMessage_Type()
)
slcDevPortCfgIdleTimeoutMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgIdleTimeoutMessage.setStatus("current")
_SlcDevPortCfgNumberOfSessionsMessage_Type = EnabledState
_SlcDevPortCfgNumberOfSessionsMessage_Object = MibTableColumn
slcDevPortCfgNumberOfSessionsMessage = _SlcDevPortCfgNumberOfSessionsMessage_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 109),
    _SlcDevPortCfgNumberOfSessionsMessage_Type()
)
slcDevPortCfgNumberOfSessionsMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgNumberOfSessionsMessage.setStatus("current")
_SlcDevPortCfgMinimizeLatency_Type = EnabledState
_SlcDevPortCfgMinimizeLatency_Object = MibTableColumn
slcDevPortCfgMinimizeLatency = _SlcDevPortCfgMinimizeLatency_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 110),
    _SlcDevPortCfgMinimizeLatency_Type()
)
slcDevPortCfgMinimizeLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgMinimizeLatency.setStatus("current")
_SlcDevPortCfgTelnetSoftIAC_Type = EnabledState
_SlcDevPortCfgTelnetSoftIAC_Object = MibTableColumn
slcDevPortCfgTelnetSoftIAC = _SlcDevPortCfgTelnetSoftIAC_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 111),
    _SlcDevPortCfgTelnetSoftIAC_Type()
)
slcDevPortCfgTelnetSoftIAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTelnetSoftIAC.setStatus("current")
_SlcDevPortCfgSendTermString_Type = EnabledState
_SlcDevPortCfgSendTermString_Object = MibTableColumn
slcDevPortCfgSendTermString = _SlcDevPortCfgSendTermString_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 112),
    _SlcDevPortCfgSendTermString_Type()
)
slcDevPortCfgSendTermString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgSendTermString.setStatus("current")
_SlcDevPortCfgTerminationString_Type = OctetString
_SlcDevPortCfgTerminationString_Object = MibTableColumn
slcDevPortCfgTerminationString = _SlcDevPortCfgTerminationString_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 113),
    _SlcDevPortCfgTerminationString_Type()
)
slcDevPortCfgTerminationString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTerminationString.setStatus("current")
_SlcDevPortCfgPowerManagementSeq_Type = OctetString
_SlcDevPortCfgPowerManagementSeq_Object = MibTableColumn
slcDevPortCfgPowerManagementSeq = _SlcDevPortCfgPowerManagementSeq_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 114),
    _SlcDevPortCfgPowerManagementSeq_Type()
)
slcDevPortCfgPowerManagementSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPowerManagementSeq.setStatus("current")
_SlcDevPortCfgPowerSupplies_Type = OctetString
_SlcDevPortCfgPowerSupplies_Object = MibTableColumn
slcDevPortCfgPowerSupplies = _SlcDevPortCfgPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 115),
    _SlcDevPortCfgPowerSupplies_Type()
)
slcDevPortCfgPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgPowerSupplies.setStatus("current")
_SlcDevPortCfgToggleDTR_Type = EnabledState
_SlcDevPortCfgToggleDTR_Object = MibTableColumn
slcDevPortCfgToggleDTR = _SlcDevPortCfgToggleDTR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 116),
    _SlcDevPortCfgToggleDTR_Type()
)
slcDevPortCfgToggleDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgToggleDTR.setStatus("current")
_SlcDevPortCfgTokenAction_Type = OctetString
_SlcDevPortCfgTokenAction_Object = MibTableColumn
slcDevPortCfgTokenAction = _SlcDevPortCfgTokenAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 117),
    _SlcDevPortCfgTokenAction_Type()
)
slcDevPortCfgTokenAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTokenAction.setStatus("current")
_SlcDevPortCfgTokenSendString_Type = OctetString
_SlcDevPortCfgTokenSendString_Object = MibTableColumn
slcDevPortCfgTokenSendString = _SlcDevPortCfgTokenSendString_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 118),
    _SlcDevPortCfgTokenSendString_Type()
)
slcDevPortCfgTokenSendString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTokenSendString.setStatus("current")
_SlcDevPortCfgTokenPowerSupply_Type = OctetString
_SlcDevPortCfgTokenPowerSupply_Object = MibTableColumn
slcDevPortCfgTokenPowerSupply = _SlcDevPortCfgTokenPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 119),
    _SlcDevPortCfgTokenPowerSupply_Type()
)
slcDevPortCfgTokenPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTokenPowerSupply.setStatus("current")


class _SlcDevPortCfgTokenPowerAction_Type(Integer32):
    """Custom type slcDevPortCfgTokenPowerAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cyclePower", 3),
          ("turnOff", 1),
          ("turnOn", 2))
    )


_SlcDevPortCfgTokenPowerAction_Type.__name__ = "Integer32"
_SlcDevPortCfgTokenPowerAction_Object = MibTableColumn
slcDevPortCfgTokenPowerAction = _SlcDevPortCfgTokenPowerAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 2, 2, 1, 120),
    _SlcDevPortCfgTokenPowerAction_Type()
)
slcDevPortCfgTokenPowerAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortCfgTokenPowerAction.setStatus("current")
_SlcDevPortState_ObjectIdentity = ObjectIdentity
slcDevPortState = _SlcDevPortState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3)
)


class _SlcDevPortStateNumber_Type(Integer32):
    """Custom type slcDevPortStateNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 8),
        ValueRangeConstraint(16, 16),
        ValueRangeConstraint(24, 24),
        ValueRangeConstraint(32, 32),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(48, 48),
    )


_SlcDevPortStateNumber_Type.__name__ = "Integer32"
_SlcDevPortStateNumber_Object = MibScalar
slcDevPortStateNumber = _SlcDevPortStateNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 1),
    _SlcDevPortStateNumber_Type()
)
slcDevPortStateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateNumber.setStatus("current")
_SlcDevPortStateTable_Object = MibTable
slcDevPortStateTable = _SlcDevPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    slcDevPortStateTable.setStatus("current")
_SlcDevPortStateEntry_Object = MibTableRow
slcDevPortStateEntry = _SlcDevPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1)
)
slcDevPortStateEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevPortStateIndex"),
)
if mibBuilder.loadTexts:
    slcDevPortStateEntry.setStatus("current")


class _SlcDevPortStateIndex_Type(Integer32):
    """Custom type slcDevPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_SlcDevPortStateIndex_Type.__name__ = "Integer32"
_SlcDevPortStateIndex_Object = MibTableColumn
slcDevPortStateIndex = _SlcDevPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 1),
    _SlcDevPortStateIndex_Type()
)
slcDevPortStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateIndex.setStatus("current")
_SlcDevPortStateBytesInput_Type = Integer32
_SlcDevPortStateBytesInput_Object = MibTableColumn
slcDevPortStateBytesInput = _SlcDevPortStateBytesInput_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 2),
    _SlcDevPortStateBytesInput_Type()
)
slcDevPortStateBytesInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateBytesInput.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortStateBytesInput.setUnits("bytes")
_SlcDevPortStateBytesOutput_Type = Integer32
_SlcDevPortStateBytesOutput_Object = MibTableColumn
slcDevPortStateBytesOutput = _SlcDevPortStateBytesOutput_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 3),
    _SlcDevPortStateBytesOutput_Type()
)
slcDevPortStateBytesOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateBytesOutput.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortStateBytesOutput.setUnits("bytes")
_SlcDevPortStateFramingErrors_Type = Integer32
_SlcDevPortStateFramingErrors_Object = MibTableColumn
slcDevPortStateFramingErrors = _SlcDevPortStateFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 4),
    _SlcDevPortStateFramingErrors_Type()
)
slcDevPortStateFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateFramingErrors.setStatus("current")
_SlcDevPortStateParityErrors_Type = Integer32
_SlcDevPortStateParityErrors_Object = MibTableColumn
slcDevPortStateParityErrors = _SlcDevPortStateParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 5),
    _SlcDevPortStateParityErrors_Type()
)
slcDevPortStateParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateParityErrors.setStatus("current")
_SlcDevPortStateOverrunErrors_Type = Integer32
_SlcDevPortStateOverrunErrors_Object = MibTableColumn
slcDevPortStateOverrunErrors = _SlcDevPortStateOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 6),
    _SlcDevPortStateOverrunErrors_Type()
)
slcDevPortStateOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateOverrunErrors.setStatus("current")
_SlcDevPortStateFlowControlViolations_Type = Integer32
_SlcDevPortStateFlowControlViolations_Object = MibTableColumn
slcDevPortStateFlowControlViolations = _SlcDevPortStateFlowControlViolations_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 7),
    _SlcDevPortStateFlowControlViolations_Type()
)
slcDevPortStateFlowControlViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateFlowControlViolations.setStatus("current")
_SlcDevPortStateDSR_Type = EnabledState
_SlcDevPortStateDSR_Object = MibTableColumn
slcDevPortStateDSR = _SlcDevPortStateDSR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 8),
    _SlcDevPortStateDSR_Type()
)
slcDevPortStateDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateDSR.setStatus("current")
_SlcDevPortStateDTR_Type = EnabledState
_SlcDevPortStateDTR_Object = MibTableColumn
slcDevPortStateDTR = _SlcDevPortStateDTR_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 9),
    _SlcDevPortStateDTR_Type()
)
slcDevPortStateDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateDTR.setStatus("current")
_SlcDevPortStateCTS_Type = EnabledState
_SlcDevPortStateCTS_Object = MibTableColumn
slcDevPortStateCTS = _SlcDevPortStateCTS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 10),
    _SlcDevPortStateCTS_Type()
)
slcDevPortStateCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateCTS.setStatus("current")
_SlcDevPortStateRTS_Type = EnabledState
_SlcDevPortStateRTS_Object = MibTableColumn
slcDevPortStateRTS = _SlcDevPortStateRTS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 11),
    _SlcDevPortStateRTS_Type()
)
slcDevPortStateRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateRTS.setStatus("current")
_SlcDevPortStateCD_Type = EnabledState
_SlcDevPortStateCD_Object = MibTableColumn
slcDevPortStateCD = _SlcDevPortStateCD_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 2, 3, 2, 1, 12),
    _SlcDevPortStateCD_Type()
)
slcDevPortStateCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStateCD.setStatus("current")
_SlcDevPCCard_ObjectIdentity = ObjectIdentity
slcDevPCCard = _SlcDevPCCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3)
)
_SlcPCCardCfgTable_Object = MibTable
slcPCCardCfgTable = _SlcPCCardCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    slcPCCardCfgTable.setStatus("current")
_SlcPCCardCfgEntry_Object = MibTableRow
slcPCCardCfgEntry = _SlcPCCardCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1)
)
slcPCCardCfgEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcPCCardCfgIndex"),
)
if mibBuilder.loadTexts:
    slcPCCardCfgEntry.setStatus("current")


class _SlcPCCardCfgIndex_Type(Integer32):
    """Custom type slcPCCardCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SlcPCCardCfgIndex_Type.__name__ = "Integer32"
_SlcPCCardCfgIndex_Object = MibTableColumn
slcPCCardCfgIndex = _SlcPCCardCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 1),
    _SlcPCCardCfgIndex_Type()
)
slcPCCardCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgIndex.setStatus("current")


class _SlcPCCardCfgCardType_Type(Integer32):
    """Custom type slcPCCardCfgCardType based on Integer32"""
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
        *(("gsmmodem", 6),
          ("isdn", 4),
          ("modem", 3),
          ("none", 1),
          ("storage", 2),
          ("wireless", 5))
    )


_SlcPCCardCfgCardType_Type.__name__ = "Integer32"
_SlcPCCardCfgCardType_Object = MibTableColumn
slcPCCardCfgCardType = _SlcPCCardCfgCardType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 2),
    _SlcPCCardCfgCardType_Type()
)
slcPCCardCfgCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCardType.setStatus("current")
_SlcPCCardCfgCardId_Type = OctetString
_SlcPCCardCfgCardId_Object = MibTableColumn
slcPCCardCfgCardId = _SlcPCCardCfgCardId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 3),
    _SlcPCCardCfgCardId_Type()
)
slcPCCardCfgCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCardId.setStatus("current")


class _SlcPCCardCfgBaud_Type(Integer32):
    """Custom type slcPCCardCfgBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SlcPCCardCfgBaud_Type.__name__ = "Integer32"
_SlcPCCardCfgBaud_Object = MibTableColumn
slcPCCardCfgBaud = _SlcPCCardCfgBaud_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 4),
    _SlcPCCardCfgBaud_Type()
)
slcPCCardCfgBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgBaud.setStatus("current")


class _SlcPCCardCfgDataBits_Type(Integer32):
    """Custom type slcPCCardCfgDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(8, 8),
    )


_SlcPCCardCfgDataBits_Type.__name__ = "Integer32"
_SlcPCCardCfgDataBits_Object = MibTableColumn
slcPCCardCfgDataBits = _SlcPCCardCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 5),
    _SlcPCCardCfgDataBits_Type()
)
slcPCCardCfgDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDataBits.setStatus("current")


class _SlcPCCardCfgStopBits_Type(Integer32):
    """Custom type slcPCCardCfgStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SlcPCCardCfgStopBits_Type.__name__ = "Integer32"
_SlcPCCardCfgStopBits_Object = MibTableColumn
slcPCCardCfgStopBits = _SlcPCCardCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 6),
    _SlcPCCardCfgStopBits_Type()
)
slcPCCardCfgStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgStopBits.setStatus("current")


class _SlcPCCardCfgParity_Type(Integer32):
    """Custom type slcPCCardCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_SlcPCCardCfgParity_Type.__name__ = "Integer32"
_SlcPCCardCfgParity_Object = MibTableColumn
slcPCCardCfgParity = _SlcPCCardCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 7),
    _SlcPCCardCfgParity_Type()
)
slcPCCardCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgParity.setStatus("current")


class _SlcPCCardCfgFlowControl_Type(Integer32):
    """Custom type slcPCCardCfgFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rtscts", 3),
          ("xonxoff", 2))
    )


_SlcPCCardCfgFlowControl_Type.__name__ = "Integer32"
_SlcPCCardCfgFlowControl_Object = MibTableColumn
slcPCCardCfgFlowControl = _SlcPCCardCfgFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 8),
    _SlcPCCardCfgFlowControl_Type()
)
slcPCCardCfgFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgFlowControl.setStatus("current")


class _SlcPCCardCfgModemState_Type(Integer32):
    """Custom type slcPCCardCfgModemState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cbcpClient", 9),
          ("cbcpServer", 8),
          ("dialback", 4),
          ("dialin", 3),
          ("dialinAndDialondemand", 6),
          ("dialinHostList", 7),
          ("dialondemand", 5),
          ("dialout", 2),
          ("disabled", 1))
    )


_SlcPCCardCfgModemState_Type.__name__ = "Integer32"
_SlcPCCardCfgModemState_Object = MibTableColumn
slcPCCardCfgModemState = _SlcPCCardCfgModemState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 9),
    _SlcPCCardCfgModemState_Type()
)
slcPCCardCfgModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgModemState.setStatus("current")


class _SlcPCCardCfgModemMode_Type(Integer32):
    """Custom type slcPCCardCfgModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("text", 2))
    )


_SlcPCCardCfgModemMode_Type.__name__ = "Integer32"
_SlcPCCardCfgModemMode_Object = MibTableColumn
slcPCCardCfgModemMode = _SlcPCCardCfgModemMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 10),
    _SlcPCCardCfgModemMode_Type()
)
slcPCCardCfgModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgModemMode.setStatus("current")
_SlcPCCardCfgLocalIP_Type = IpAddress
_SlcPCCardCfgLocalIP_Object = MibTableColumn
slcPCCardCfgLocalIP = _SlcPCCardCfgLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 11),
    _SlcPCCardCfgLocalIP_Type()
)
slcPCCardCfgLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgLocalIP.setStatus("current")
_SlcPCCardCfgRemoteIP_Type = IpAddress
_SlcPCCardCfgRemoteIP_Object = MibTableColumn
slcPCCardCfgRemoteIP = _SlcPCCardCfgRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 12),
    _SlcPCCardCfgRemoteIP_Type()
)
slcPCCardCfgRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgRemoteIP.setStatus("current")


class _SlcPCCardCfgAuth_Type(Integer32):
    """Custom type slcPCCardCfgAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcPCCardCfgAuth_Type.__name__ = "Integer32"
_SlcPCCardCfgAuth_Object = MibTableColumn
slcPCCardCfgAuth = _SlcPCCardCfgAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 13),
    _SlcPCCardCfgAuth_Type()
)
slcPCCardCfgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgAuth.setStatus("current")
_SlcPCCardCfgCHAPHost_Type = OctetString
_SlcPCCardCfgCHAPHost_Object = MibTableColumn
slcPCCardCfgCHAPHost = _SlcPCCardCfgCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 14),
    _SlcPCCardCfgCHAPHost_Type()
)
slcPCCardCfgCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCHAPHost.setStatus("current")
_SlcPCCardCfgInitScript_Type = OctetString
_SlcPCCardCfgInitScript_Object = MibTableColumn
slcPCCardCfgInitScript = _SlcPCCardCfgInitScript_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 15),
    _SlcPCCardCfgInitScript_Type()
)
slcPCCardCfgInitScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgInitScript.setStatus("current")


class _SlcPCCardCfgTimeout_Type(Integer32):
    """Custom type slcPCCardCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcPCCardCfgTimeout_Type.__name__ = "Integer32"
_SlcPCCardCfgTimeout_Object = MibTableColumn
slcPCCardCfgTimeout = _SlcPCCardCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 16),
    _SlcPCCardCfgTimeout_Type()
)
slcPCCardCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcPCCardCfgTimeout.setUnits("minutes")
_SlcPCCardCfgDialoutNum_Type = OctetString
_SlcPCCardCfgDialoutNum_Object = MibTableColumn
slcPCCardCfgDialoutNum = _SlcPCCardCfgDialoutNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 17),
    _SlcPCCardCfgDialoutNum_Type()
)
slcPCCardCfgDialoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialoutNum.setStatus("current")


class _SlcPCCardCfgDialoutLogin_Type(OctetString):
    """Custom type slcPCCardCfgDialoutLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcPCCardCfgDialoutLogin_Type.__name__ = "OctetString"
_SlcPCCardCfgDialoutLogin_Object = MibTableColumn
slcPCCardCfgDialoutLogin = _SlcPCCardCfgDialoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 18),
    _SlcPCCardCfgDialoutLogin_Type()
)
slcPCCardCfgDialoutLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialoutLogin.setStatus("current")


class _SlcPCCardCfgDialbackMode_Type(Integer32):
    """Custom type slcPCCardCfgDialbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("usernumber", 1))
    )


_SlcPCCardCfgDialbackMode_Type.__name__ = "Integer32"
_SlcPCCardCfgDialbackMode_Object = MibTableColumn
slcPCCardCfgDialbackMode = _SlcPCCardCfgDialbackMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 19),
    _SlcPCCardCfgDialbackMode_Type()
)
slcPCCardCfgDialbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialbackMode.setStatus("current")
_SlcPCCardCfgDialbackNum_Type = OctetString
_SlcPCCardCfgDialbackNum_Object = MibTableColumn
slcPCCardCfgDialbackNum = _SlcPCCardCfgDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 20),
    _SlcPCCardCfgDialbackNum_Type()
)
slcPCCardCfgDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialbackNum.setStatus("current")
_SlcPCCardCfgNATState_Type = EnabledState
_SlcPCCardCfgNATState_Object = MibTableColumn
slcPCCardCfgNATState = _SlcPCCardCfgNATState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 21),
    _SlcPCCardCfgNATState_Type()
)
slcPCCardCfgNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgNATState.setStatus("current")


class _SlcPCCardCfgStorageFS_Type(Integer32):
    """Custom type slcPCCardCfgStorageFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ext2", 2),
          ("fat", 3),
          ("notmounted", 1))
    )


_SlcPCCardCfgStorageFS_Type.__name__ = "Integer32"
_SlcPCCardCfgStorageFS_Object = MibTableColumn
slcPCCardCfgStorageFS = _SlcPCCardCfgStorageFS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 22),
    _SlcPCCardCfgStorageFS_Type()
)
slcPCCardCfgStorageFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgStorageFS.setStatus("current")
_SlcPCCardCfgISDNChannel_Type = Integer32
_SlcPCCardCfgISDNChannel_Object = MibTableColumn
slcPCCardCfgISDNChannel = _SlcPCCardCfgISDNChannel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 23),
    _SlcPCCardCfgISDNChannel_Type()
)
slcPCCardCfgISDNChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgISDNChannel.setStatus("current")
_SlcPCCardCfgISDNChannelNum_Type = OctetString
_SlcPCCardCfgISDNChannelNum_Object = MibTableColumn
slcPCCardCfgISDNChannelNum = _SlcPCCardCfgISDNChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 24),
    _SlcPCCardCfgISDNChannelNum_Type()
)
slcPCCardCfgISDNChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgISDNChannelNum.setStatus("current")
_SlcPCCardCfgTelnetState_Type = EnabledState
_SlcPCCardCfgTelnetState_Object = MibTableColumn
slcPCCardCfgTelnetState = _SlcPCCardCfgTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 25),
    _SlcPCCardCfgTelnetState_Type()
)
slcPCCardCfgTelnetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTelnetState.setStatus("current")


class _SlcPCCardCfgTelnetPort_Type(Integer32):
    """Custom type slcPCCardCfgTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcPCCardCfgTelnetPort_Type.__name__ = "Integer32"
_SlcPCCardCfgTelnetPort_Object = MibTableColumn
slcPCCardCfgTelnetPort = _SlcPCCardCfgTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 26),
    _SlcPCCardCfgTelnetPort_Type()
)
slcPCCardCfgTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTelnetPort.setStatus("current")
_SlcPCCardCfgTelnetAuth_Type = EnabledState
_SlcPCCardCfgTelnetAuth_Object = MibTableColumn
slcPCCardCfgTelnetAuth = _SlcPCCardCfgTelnetAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 27),
    _SlcPCCardCfgTelnetAuth_Type()
)
slcPCCardCfgTelnetAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTelnetAuth.setStatus("current")
_SlcPCCardCfgSSHState_Type = EnabledState
_SlcPCCardCfgSSHState_Object = MibTableColumn
slcPCCardCfgSSHState = _SlcPCCardCfgSSHState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 28),
    _SlcPCCardCfgSSHState_Type()
)
slcPCCardCfgSSHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgSSHState.setStatus("current")


class _SlcPCCardCfgSSHPort_Type(Integer32):
    """Custom type slcPCCardCfgSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcPCCardCfgSSHPort_Type.__name__ = "Integer32"
_SlcPCCardCfgSSHPort_Object = MibTableColumn
slcPCCardCfgSSHPort = _SlcPCCardCfgSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 29),
    _SlcPCCardCfgSSHPort_Type()
)
slcPCCardCfgSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgSSHPort.setStatus("current")
_SlcPCCardCfgSSHAuth_Type = EnabledState
_SlcPCCardCfgSSHAuth_Object = MibTableColumn
slcPCCardCfgSSHAuth = _SlcPCCardCfgSSHAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 30),
    _SlcPCCardCfgSSHAuth_Type()
)
slcPCCardCfgSSHAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgSSHAuth.setStatus("current")
_SlcPCCardCfgTCPState_Type = EnabledState
_SlcPCCardCfgTCPState_Object = MibTableColumn
slcPCCardCfgTCPState = _SlcPCCardCfgTCPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 31),
    _SlcPCCardCfgTCPState_Type()
)
slcPCCardCfgTCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTCPState.setStatus("current")


class _SlcPCCardCfgTCPPort_Type(Integer32):
    """Custom type slcPCCardCfgTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcPCCardCfgTCPPort_Type.__name__ = "Integer32"
_SlcPCCardCfgTCPPort_Object = MibTableColumn
slcPCCardCfgTCPPort = _SlcPCCardCfgTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 32),
    _SlcPCCardCfgTCPPort_Type()
)
slcPCCardCfgTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTCPPort.setStatus("current")
_SlcPCCardCfgTCPAuth_Type = EnabledState
_SlcPCCardCfgTCPAuth_Object = MibTableColumn
slcPCCardCfgTCPAuth = _SlcPCCardCfgTCPAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 33),
    _SlcPCCardCfgTCPAuth_Type()
)
slcPCCardCfgTCPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgTCPAuth.setStatus("current")
_SlcPCCardCfgGSMPIN_Type = OctetString
_SlcPCCardCfgGSMPIN_Object = MibTableColumn
slcPCCardCfgGSMPIN = _SlcPCCardCfgGSMPIN_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 34),
    _SlcPCCardCfgGSMPIN_Type()
)
slcPCCardCfgGSMPIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMPIN.setStatus("current")
_SlcPCCardCfgGSMNetworkName_Type = OctetString
_SlcPCCardCfgGSMNetworkName_Object = MibTableColumn
slcPCCardCfgGSMNetworkName = _SlcPCCardCfgGSMNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 35),
    _SlcPCCardCfgGSMNetworkName_Type()
)
slcPCCardCfgGSMNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMNetworkName.setStatus("obsolete")
_SlcPCCardCfgGSMPPPCompression_Type = EnabledState
_SlcPCCardCfgGSMPPPCompression_Object = MibTableColumn
slcPCCardCfgGSMPPPCompression = _SlcPCCardCfgGSMPPPCompression_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 36),
    _SlcPCCardCfgGSMPPPCompression_Type()
)
slcPCCardCfgGSMPPPCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMPPPCompression.setStatus("current")
_SlcPCCardCfgGSMAutoAcquireDNS_Type = EnabledState
_SlcPCCardCfgGSMAutoAcquireDNS_Object = MibTableColumn
slcPCCardCfgGSMAutoAcquireDNS = _SlcPCCardCfgGSMAutoAcquireDNS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 37),
    _SlcPCCardCfgGSMAutoAcquireDNS_Type()
)
slcPCCardCfgGSMAutoAcquireDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMAutoAcquireDNS.setStatus("current")


class _SlcPCCardCfgGSMDialoutMode_Type(Integer32):
    """Custom type slcPCCardCfgGSMDialoutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gprs", 1),
          ("gsm", 2))
    )


_SlcPCCardCfgGSMDialoutMode_Type.__name__ = "Integer32"
_SlcPCCardCfgGSMDialoutMode_Object = MibTableColumn
slcPCCardCfgGSMDialoutMode = _SlcPCCardCfgGSMDialoutMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 38),
    _SlcPCCardCfgGSMDialoutMode_Type()
)
slcPCCardCfgGSMDialoutMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMDialoutMode.setStatus("current")
_SlcPCCardCfgGSMContextID_Type = OctetString
_SlcPCCardCfgGSMContextID_Object = MibTableColumn
slcPCCardCfgGSMContextID = _SlcPCCardCfgGSMContextID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 39),
    _SlcPCCardCfgGSMContextID_Type()
)
slcPCCardCfgGSMContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMContextID.setStatus("current")
_SlcPCCardCfgGSMBearerService_Type = OctetString
_SlcPCCardCfgGSMBearerService_Object = MibTableColumn
slcPCCardCfgGSMBearerService = _SlcPCCardCfgGSMBearerService_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 40),
    _SlcPCCardCfgGSMBearerService_Type()
)
slcPCCardCfgGSMBearerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGSMBearerService.setStatus("current")
_SlcPCCardCfgIdleTimeout_Type = Integer32
_SlcPCCardCfgIdleTimeout_Object = MibTableColumn
slcPCCardCfgIdleTimeout = _SlcPCCardCfgIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 41),
    _SlcPCCardCfgIdleTimeout_Type()
)
slcPCCardCfgIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgIdleTimeout.setStatus("current")
_SlcPCCardCfgRestartDelay_Type = Integer32
_SlcPCCardCfgRestartDelay_Object = MibTableColumn
slcPCCardCfgRestartDelay = _SlcPCCardCfgRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 42),
    _SlcPCCardCfgRestartDelay_Type()
)
slcPCCardCfgRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcPCCardCfgRestartDelay.setUnits("seconds")
_SlcPCCardCfgCallerIdLogging_Type = EnabledState
_SlcPCCardCfgCallerIdLogging_Object = MibTableColumn
slcPCCardCfgCallerIdLogging = _SlcPCCardCfgCallerIdLogging_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 43),
    _SlcPCCardCfgCallerIdLogging_Type()
)
slcPCCardCfgCallerIdLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCallerIdLogging.setStatus("current")
_SlcPCCardCfgCallerIdATCmd_Type = OctetString
_SlcPCCardCfgCallerIdATCmd_Object = MibTableColumn
slcPCCardCfgCallerIdATCmd = _SlcPCCardCfgCallerIdATCmd_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 44),
    _SlcPCCardCfgCallerIdATCmd_Type()
)
slcPCCardCfgCallerIdATCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCallerIdATCmd.setStatus("current")


class _SlcPCCardCfgDODAuth_Type(Integer32):
    """Custom type slcPCCardCfgDODAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcPCCardCfgDODAuth_Type.__name__ = "Integer32"
_SlcPCCardCfgDODAuth_Object = MibTableColumn
slcPCCardCfgDODAuth = _SlcPCCardCfgDODAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 45),
    _SlcPCCardCfgDODAuth_Type()
)
slcPCCardCfgDODAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDODAuth.setStatus("current")
_SlcPCCardCfgDODCHAPHost_Type = OctetString
_SlcPCCardCfgDODCHAPHost_Object = MibTableColumn
slcPCCardCfgDODCHAPHost = _SlcPCCardCfgDODCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 46),
    _SlcPCCardCfgDODCHAPHost_Type()
)
slcPCCardCfgDODCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDODCHAPHost.setStatus("current")
_SlcPCCardCfgHostList_Type = OctetString
_SlcPCCardCfgHostList_Object = MibTableColumn
slcPCCardCfgHostList = _SlcPCCardCfgHostList_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 47),
    _SlcPCCardCfgHostList_Type()
)
slcPCCardCfgHostList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgHostList.setStatus("current")


class _SlcPCCardCfgCBCPClientType_Type(Integer32):
    """Custom type slcPCCardCfgCBCPClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminDefined", 1),
          ("userDefined", 2))
    )


_SlcPCCardCfgCBCPClientType_Type.__name__ = "Integer32"
_SlcPCCardCfgCBCPClientType_Object = MibTableColumn
slcPCCardCfgCBCPClientType = _SlcPCCardCfgCBCPClientType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 48),
    _SlcPCCardCfgCBCPClientType_Type()
)
slcPCCardCfgCBCPClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCBCPClientType.setStatus("current")
_SlcPCCardCfgCBCPServerAllowNoCallback_Type = EnabledState
_SlcPCCardCfgCBCPServerAllowNoCallback_Object = MibTableColumn
slcPCCardCfgCBCPServerAllowNoCallback = _SlcPCCardCfgCBCPServerAllowNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 49),
    _SlcPCCardCfgCBCPServerAllowNoCallback_Type()
)
slcPCCardCfgCBCPServerAllowNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCBCPServerAllowNoCallback.setStatus("current")
_SlcPCCardCfgDialbackDelay_Type = Integer32
_SlcPCCardCfgDialbackDelay_Object = MibTableColumn
slcPCCardCfgDialbackDelay = _SlcPCCardCfgDialbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 50),
    _SlcPCCardCfgDialbackDelay_Type()
)
slcPCCardCfgDialbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcPCCardCfgDialbackDelay.setUnits("seconds")
_SlcPCCardCfgCHAPAuthLocalUsers_Type = EnabledState
_SlcPCCardCfgCHAPAuthLocalUsers_Object = MibTableColumn
slcPCCardCfgCHAPAuthLocalUsers = _SlcPCCardCfgCHAPAuthLocalUsers_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 51),
    _SlcPCCardCfgCHAPAuthLocalUsers_Type()
)
slcPCCardCfgCHAPAuthLocalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgCHAPAuthLocalUsers.setStatus("current")
_SlcPCCardCfgUseSites_Type = EnabledState
_SlcPCCardCfgUseSites_Object = MibTableColumn
slcPCCardCfgUseSites = _SlcPCCardCfgUseSites_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 52),
    _SlcPCCardCfgUseSites_Type()
)
slcPCCardCfgUseSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgUseSites.setStatus("current")
_SlcPCCardCfgDialbackRetries_Type = Integer32
_SlcPCCardCfgDialbackRetries_Object = MibTableColumn
slcPCCardCfgDialbackRetries = _SlcPCCardCfgDialbackRetries_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 53),
    _SlcPCCardCfgDialbackRetries_Type()
)
slcPCCardCfgDialbackRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgDialbackRetries.setStatus("current")
_SlcPCCardCfgGroup_Type = OctetString
_SlcPCCardCfgGroup_Object = MibTableColumn
slcPCCardCfgGroup = _SlcPCCardCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 3, 1, 1, 54),
    _SlcPCCardCfgGroup_Type()
)
slcPCCardCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardCfgGroup.setStatus("current")
_SlcDevPowerSupply_ObjectIdentity = ObjectIdentity
slcDevPowerSupply = _SlcDevPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 4)
)


class _SlcDevPowerSupplyType_Type(Integer32):
    """Custom type slcDevPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acOnePowerSupply", 1),
          ("acTwoPowerSupplies", 2),
          ("dcTwoPowerSupplies", 3))
    )


_SlcDevPowerSupplyType_Type.__name__ = "Integer32"
_SlcDevPowerSupplyType_Object = MibScalar
slcDevPowerSupplyType = _SlcDevPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 4, 1),
    _SlcDevPowerSupplyType_Type()
)
slcDevPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPowerSupplyType.setStatus("current")


class _SlcDevPowerSupplyA_Type(Integer32):
    """Custom type slcDevPowerSupplyA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_SlcDevPowerSupplyA_Type.__name__ = "Integer32"
_SlcDevPowerSupplyA_Object = MibScalar
slcDevPowerSupplyA = _SlcDevPowerSupplyA_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 4, 2),
    _SlcDevPowerSupplyA_Type()
)
slcDevPowerSupplyA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPowerSupplyA.setStatus("current")


class _SlcDevPowerSupplyB_Type(Integer32):
    """Custom type slcDevPowerSupplyB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notInstalled", 3),
          ("up", 1))
    )


_SlcDevPowerSupplyB_Type.__name__ = "Integer32"
_SlcDevPowerSupplyB_Object = MibScalar
slcDevPowerSupplyB = _SlcDevPowerSupplyB_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 4, 3),
    _SlcDevPowerSupplyB_Type()
)
slcDevPowerSupplyB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPowerSupplyB.setStatus("current")
_SlcDevUSB_ObjectIdentity = ObjectIdentity
slcDevUSB = _SlcDevUSB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5)
)
_SlcDevUSBState_Type = EnabledState
_SlcDevUSBState_Object = MibScalar
slcDevUSBState = _SlcDevUSBState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 1),
    _SlcDevUSBState_Type()
)
slcDevUSBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBState.setStatus("current")
_SlcDevUSBCfgTable_Object = MibTable
slcDevUSBCfgTable = _SlcDevUSBCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2)
)
if mibBuilder.loadTexts:
    slcDevUSBCfgTable.setStatus("current")
_SlcDevUSBCfgEntry_Object = MibTableRow
slcDevUSBCfgEntry = _SlcDevUSBCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1)
)
slcDevUSBCfgEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevUSBId"),
)
if mibBuilder.loadTexts:
    slcDevUSBCfgEntry.setStatus("current")


class _SlcDevUSBId_Type(Integer32):
    """Custom type slcDevUSBId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SlcDevUSBId_Type.__name__ = "Integer32"
_SlcDevUSBId_Object = MibTableColumn
slcDevUSBId = _SlcDevUSBId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 1),
    _SlcDevUSBId_Type()
)
slcDevUSBId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBId.setStatus("current")


class _SlcDevUSBCfgCardType_Type(Integer32):
    """Custom type slcDevUSBCfgCardType based on Integer32"""
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
        *(("gsmmodem", 6),
          ("isdn", 4),
          ("modem", 3),
          ("none", 1),
          ("storage", 2),
          ("wireless", 5))
    )


_SlcDevUSBCfgCardType_Type.__name__ = "Integer32"
_SlcDevUSBCfgCardType_Object = MibTableColumn
slcDevUSBCfgCardType = _SlcDevUSBCfgCardType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 2),
    _SlcDevUSBCfgCardType_Type()
)
slcDevUSBCfgCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCardType.setStatus("current")
_SlcDevUSBCfgCardId_Type = OctetString
_SlcDevUSBCfgCardId_Object = MibTableColumn
slcDevUSBCfgCardId = _SlcDevUSBCfgCardId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 3),
    _SlcDevUSBCfgCardId_Type()
)
slcDevUSBCfgCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCardId.setStatus("current")


class _SlcDevUSBCfgStorageFS_Type(Integer32):
    """Custom type slcDevUSBCfgStorageFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ext2", 2),
          ("fat", 3),
          ("notmounted", 1))
    )


_SlcDevUSBCfgStorageFS_Type.__name__ = "Integer32"
_SlcDevUSBCfgStorageFS_Object = MibTableColumn
slcDevUSBCfgStorageFS = _SlcDevUSBCfgStorageFS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 4),
    _SlcDevUSBCfgStorageFS_Type()
)
slcDevUSBCfgStorageFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgStorageFS.setStatus("current")


class _SlcDevUSBCfgBaud_Type(Integer32):
    """Custom type slcDevUSBCfgBaud based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 300),
        ValueRangeConstraint(600, 600),
        ValueRangeConstraint(1200, 1200),
        ValueRangeConstraint(2400, 2400),
        ValueRangeConstraint(4800, 4800),
        ValueRangeConstraint(9600, 9600),
        ValueRangeConstraint(19200, 19200),
        ValueRangeConstraint(38400, 38400),
        ValueRangeConstraint(57600, 57600),
        ValueRangeConstraint(115200, 115200),
    )


_SlcDevUSBCfgBaud_Type.__name__ = "Integer32"
_SlcDevUSBCfgBaud_Object = MibTableColumn
slcDevUSBCfgBaud = _SlcDevUSBCfgBaud_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 5),
    _SlcDevUSBCfgBaud_Type()
)
slcDevUSBCfgBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgBaud.setStatus("current")


class _SlcDevUSBCfgDataBits_Type(Integer32):
    """Custom type slcDevUSBCfgDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 7),
        ValueRangeConstraint(8, 8),
    )


_SlcDevUSBCfgDataBits_Type.__name__ = "Integer32"
_SlcDevUSBCfgDataBits_Object = MibTableColumn
slcDevUSBCfgDataBits = _SlcDevUSBCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 6),
    _SlcDevUSBCfgDataBits_Type()
)
slcDevUSBCfgDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDataBits.setStatus("current")


class _SlcDevUSBCfgStopBits_Type(Integer32):
    """Custom type slcDevUSBCfgStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_SlcDevUSBCfgStopBits_Type.__name__ = "Integer32"
_SlcDevUSBCfgStopBits_Object = MibTableColumn
slcDevUSBCfgStopBits = _SlcDevUSBCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 7),
    _SlcDevUSBCfgStopBits_Type()
)
slcDevUSBCfgStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgStopBits.setStatus("current")


class _SlcDevUSBCfgParity_Type(Integer32):
    """Custom type slcDevUSBCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_SlcDevUSBCfgParity_Type.__name__ = "Integer32"
_SlcDevUSBCfgParity_Object = MibTableColumn
slcDevUSBCfgParity = _SlcDevUSBCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 8),
    _SlcDevUSBCfgParity_Type()
)
slcDevUSBCfgParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgParity.setStatus("current")


class _SlcDevUSBCfgFlowControl_Type(Integer32):
    """Custom type slcDevUSBCfgFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rtscts", 3),
          ("xonxoff", 2))
    )


_SlcDevUSBCfgFlowControl_Type.__name__ = "Integer32"
_SlcDevUSBCfgFlowControl_Object = MibTableColumn
slcDevUSBCfgFlowControl = _SlcDevUSBCfgFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 9),
    _SlcDevUSBCfgFlowControl_Type()
)
slcDevUSBCfgFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgFlowControl.setStatus("current")


class _SlcDevUSBCfgModemState_Type(Integer32):
    """Custom type slcDevUSBCfgModemState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("cbcpClient", 9),
          ("cbcpServer", 8),
          ("dialback", 4),
          ("dialin", 3),
          ("dialinAndDialondemand", 6),
          ("dialinHostList", 7),
          ("dialondemand", 5),
          ("dialout", 2),
          ("disabled", 1))
    )


_SlcDevUSBCfgModemState_Type.__name__ = "Integer32"
_SlcDevUSBCfgModemState_Object = MibTableColumn
slcDevUSBCfgModemState = _SlcDevUSBCfgModemState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 10),
    _SlcDevUSBCfgModemState_Type()
)
slcDevUSBCfgModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgModemState.setStatus("current")


class _SlcDevUSBCfgModemMode_Type(Integer32):
    """Custom type slcDevUSBCfgModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("text", 2))
    )


_SlcDevUSBCfgModemMode_Type.__name__ = "Integer32"
_SlcDevUSBCfgModemMode_Object = MibTableColumn
slcDevUSBCfgModemMode = _SlcDevUSBCfgModemMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 11),
    _SlcDevUSBCfgModemMode_Type()
)
slcDevUSBCfgModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgModemMode.setStatus("current")
_SlcDevUSBCfgLocalIP_Type = IpAddress
_SlcDevUSBCfgLocalIP_Object = MibTableColumn
slcDevUSBCfgLocalIP = _SlcDevUSBCfgLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 12),
    _SlcDevUSBCfgLocalIP_Type()
)
slcDevUSBCfgLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgLocalIP.setStatus("current")
_SlcDevUSBCfgRemoteIP_Type = IpAddress
_SlcDevUSBCfgRemoteIP_Object = MibTableColumn
slcDevUSBCfgRemoteIP = _SlcDevUSBCfgRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 13),
    _SlcDevUSBCfgRemoteIP_Type()
)
slcDevUSBCfgRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgRemoteIP.setStatus("current")


class _SlcDevUSBCfgAuth_Type(Integer32):
    """Custom type slcDevUSBCfgAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcDevUSBCfgAuth_Type.__name__ = "Integer32"
_SlcDevUSBCfgAuth_Object = MibTableColumn
slcDevUSBCfgAuth = _SlcDevUSBCfgAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 14),
    _SlcDevUSBCfgAuth_Type()
)
slcDevUSBCfgAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgAuth.setStatus("current")
_SlcDevUSBCfgCHAPHost_Type = OctetString
_SlcDevUSBCfgCHAPHost_Object = MibTableColumn
slcDevUSBCfgCHAPHost = _SlcDevUSBCfgCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 15),
    _SlcDevUSBCfgCHAPHost_Type()
)
slcDevUSBCfgCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCHAPHost.setStatus("current")


class _SlcDevUSBCfgDODAuth_Type(Integer32):
    """Custom type slcDevUSBCfgDODAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcDevUSBCfgDODAuth_Type.__name__ = "Integer32"
_SlcDevUSBCfgDODAuth_Object = MibTableColumn
slcDevUSBCfgDODAuth = _SlcDevUSBCfgDODAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 16),
    _SlcDevUSBCfgDODAuth_Type()
)
slcDevUSBCfgDODAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDODAuth.setStatus("current")
_SlcDevUSBCfgDODCHAPHost_Type = OctetString
_SlcDevUSBCfgDODCHAPHost_Object = MibTableColumn
slcDevUSBCfgDODCHAPHost = _SlcDevUSBCfgDODCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 17),
    _SlcDevUSBCfgDODCHAPHost_Type()
)
slcDevUSBCfgDODCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDODCHAPHost.setStatus("current")
_SlcDevUSBCfgInitScript_Type = OctetString
_SlcDevUSBCfgInitScript_Object = MibTableColumn
slcDevUSBCfgInitScript = _SlcDevUSBCfgInitScript_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 18),
    _SlcDevUSBCfgInitScript_Type()
)
slcDevUSBCfgInitScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgInitScript.setStatus("current")


class _SlcDevUSBCfgTimeout_Type(Integer32):
    """Custom type slcDevUSBCfgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcDevUSBCfgTimeout_Type.__name__ = "Integer32"
_SlcDevUSBCfgTimeout_Object = MibTableColumn
slcDevUSBCfgTimeout = _SlcDevUSBCfgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 19),
    _SlcDevUSBCfgTimeout_Type()
)
slcDevUSBCfgTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevUSBCfgTimeout.setUnits("minutes")
_SlcDevUSBCfgDialoutNum_Type = OctetString
_SlcDevUSBCfgDialoutNum_Object = MibTableColumn
slcDevUSBCfgDialoutNum = _SlcDevUSBCfgDialoutNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 20),
    _SlcDevUSBCfgDialoutNum_Type()
)
slcDevUSBCfgDialoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialoutNum.setStatus("current")


class _SlcDevUSBCfgDialoutLogin_Type(OctetString):
    """Custom type slcDevUSBCfgDialoutLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcDevUSBCfgDialoutLogin_Type.__name__ = "OctetString"
_SlcDevUSBCfgDialoutLogin_Object = MibTableColumn
slcDevUSBCfgDialoutLogin = _SlcDevUSBCfgDialoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 21),
    _SlcDevUSBCfgDialoutLogin_Type()
)
slcDevUSBCfgDialoutLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialoutLogin.setStatus("current")


class _SlcDevUSBCfgDialbackMode_Type(Integer32):
    """Custom type slcDevUSBCfgDialbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("usernumber", 1))
    )


_SlcDevUSBCfgDialbackMode_Type.__name__ = "Integer32"
_SlcDevUSBCfgDialbackMode_Object = MibTableColumn
slcDevUSBCfgDialbackMode = _SlcDevUSBCfgDialbackMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 22),
    _SlcDevUSBCfgDialbackMode_Type()
)
slcDevUSBCfgDialbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialbackMode.setStatus("current")
_SlcDevUSBCfgDialbackNum_Type = OctetString
_SlcDevUSBCfgDialbackNum_Object = MibTableColumn
slcDevUSBCfgDialbackNum = _SlcDevUSBCfgDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 23),
    _SlcDevUSBCfgDialbackNum_Type()
)
slcDevUSBCfgDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialbackNum.setStatus("current")
_SlcDevUSBCfgDialbackDelay_Type = Integer32
_SlcDevUSBCfgDialbackDelay_Object = MibTableColumn
slcDevUSBCfgDialbackDelay = _SlcDevUSBCfgDialbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 24),
    _SlcDevUSBCfgDialbackDelay_Type()
)
slcDevUSBCfgDialbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialbackDelay.setUnits("seconds")
_SlcDevUSBCfgNATState_Type = EnabledState
_SlcDevUSBCfgNATState_Object = MibTableColumn
slcDevUSBCfgNATState = _SlcDevUSBCfgNATState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 25),
    _SlcDevUSBCfgNATState_Type()
)
slcDevUSBCfgNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgNATState.setStatus("current")
_SlcDevUSBCfgIdleTimeout_Type = Integer32
_SlcDevUSBCfgIdleTimeout_Object = MibTableColumn
slcDevUSBCfgIdleTimeout = _SlcDevUSBCfgIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 26),
    _SlcDevUSBCfgIdleTimeout_Type()
)
slcDevUSBCfgIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevUSBCfgIdleTimeout.setUnits("seconds")
_SlcDevUSBCfgRestartDelay_Type = Integer32
_SlcDevUSBCfgRestartDelay_Object = MibTableColumn
slcDevUSBCfgRestartDelay = _SlcDevUSBCfgRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 27),
    _SlcDevUSBCfgRestartDelay_Type()
)
slcDevUSBCfgRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevUSBCfgRestartDelay.setUnits("seconds")
_SlcDevUSBCfgCallerIdLogging_Type = EnabledState
_SlcDevUSBCfgCallerIdLogging_Object = MibTableColumn
slcDevUSBCfgCallerIdLogging = _SlcDevUSBCfgCallerIdLogging_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 28),
    _SlcDevUSBCfgCallerIdLogging_Type()
)
slcDevUSBCfgCallerIdLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCallerIdLogging.setStatus("current")
_SlcDevUSBCfgCallerIdATCmd_Type = OctetString
_SlcDevUSBCfgCallerIdATCmd_Object = MibTableColumn
slcDevUSBCfgCallerIdATCmd = _SlcDevUSBCfgCallerIdATCmd_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 29),
    _SlcDevUSBCfgCallerIdATCmd_Type()
)
slcDevUSBCfgCallerIdATCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCallerIdATCmd.setStatus("current")
_SlcDevUSBCfgHostList_Type = OctetString
_SlcDevUSBCfgHostList_Object = MibTableColumn
slcDevUSBCfgHostList = _SlcDevUSBCfgHostList_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 30),
    _SlcDevUSBCfgHostList_Type()
)
slcDevUSBCfgHostList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgHostList.setStatus("current")


class _SlcDevUSBCfgCBCPClientType_Type(Integer32):
    """Custom type slcDevUSBCfgCBCPClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminDefined", 1),
          ("userDefined", 2))
    )


_SlcDevUSBCfgCBCPClientType_Type.__name__ = "Integer32"
_SlcDevUSBCfgCBCPClientType_Object = MibTableColumn
slcDevUSBCfgCBCPClientType = _SlcDevUSBCfgCBCPClientType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 31),
    _SlcDevUSBCfgCBCPClientType_Type()
)
slcDevUSBCfgCBCPClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCBCPClientType.setStatus("current")
_SlcDevUSBCfgCBCPServerAllowNoCallback_Type = EnabledState
_SlcDevUSBCfgCBCPServerAllowNoCallback_Object = MibTableColumn
slcDevUSBCfgCBCPServerAllowNoCallback = _SlcDevUSBCfgCBCPServerAllowNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 32),
    _SlcDevUSBCfgCBCPServerAllowNoCallback_Type()
)
slcDevUSBCfgCBCPServerAllowNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCBCPServerAllowNoCallback.setStatus("current")
_SlcDevUSBCfgTelnetState_Type = EnabledState
_SlcDevUSBCfgTelnetState_Object = MibTableColumn
slcDevUSBCfgTelnetState = _SlcDevUSBCfgTelnetState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 33),
    _SlcDevUSBCfgTelnetState_Type()
)
slcDevUSBCfgTelnetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTelnetState.setStatus("current")


class _SlcDevUSBCfgTelnetPort_Type(Integer32):
    """Custom type slcDevUSBCfgTelnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevUSBCfgTelnetPort_Type.__name__ = "Integer32"
_SlcDevUSBCfgTelnetPort_Object = MibTableColumn
slcDevUSBCfgTelnetPort = _SlcDevUSBCfgTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 34),
    _SlcDevUSBCfgTelnetPort_Type()
)
slcDevUSBCfgTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTelnetPort.setStatus("current")
_SlcDevUSBCfgTelnetAuth_Type = EnabledState
_SlcDevUSBCfgTelnetAuth_Object = MibTableColumn
slcDevUSBCfgTelnetAuth = _SlcDevUSBCfgTelnetAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 35),
    _SlcDevUSBCfgTelnetAuth_Type()
)
slcDevUSBCfgTelnetAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTelnetAuth.setStatus("current")
_SlcDevUSBCfgSSHState_Type = EnabledState
_SlcDevUSBCfgSSHState_Object = MibTableColumn
slcDevUSBCfgSSHState = _SlcDevUSBCfgSSHState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 36),
    _SlcDevUSBCfgSSHState_Type()
)
slcDevUSBCfgSSHState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgSSHState.setStatus("current")


class _SlcDevUSBCfgSSHPort_Type(Integer32):
    """Custom type slcDevUSBCfgSSHPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevUSBCfgSSHPort_Type.__name__ = "Integer32"
_SlcDevUSBCfgSSHPort_Object = MibTableColumn
slcDevUSBCfgSSHPort = _SlcDevUSBCfgSSHPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 37),
    _SlcDevUSBCfgSSHPort_Type()
)
slcDevUSBCfgSSHPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgSSHPort.setStatus("current")
_SlcDevUSBCfgSSHAuth_Type = EnabledState
_SlcDevUSBCfgSSHAuth_Object = MibTableColumn
slcDevUSBCfgSSHAuth = _SlcDevUSBCfgSSHAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 38),
    _SlcDevUSBCfgSSHAuth_Type()
)
slcDevUSBCfgSSHAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgSSHAuth.setStatus("current")
_SlcDevUSBCfgTCPState_Type = EnabledState
_SlcDevUSBCfgTCPState_Object = MibTableColumn
slcDevUSBCfgTCPState = _SlcDevUSBCfgTCPState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 39),
    _SlcDevUSBCfgTCPState_Type()
)
slcDevUSBCfgTCPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTCPState.setStatus("current")


class _SlcDevUSBCfgTCPPort_Type(Integer32):
    """Custom type slcDevUSBCfgTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SlcDevUSBCfgTCPPort_Type.__name__ = "Integer32"
_SlcDevUSBCfgTCPPort_Object = MibTableColumn
slcDevUSBCfgTCPPort = _SlcDevUSBCfgTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 40),
    _SlcDevUSBCfgTCPPort_Type()
)
slcDevUSBCfgTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTCPPort.setStatus("current")
_SlcDevUSBCfgTCPAuth_Type = EnabledState
_SlcDevUSBCfgTCPAuth_Object = MibTableColumn
slcDevUSBCfgTCPAuth = _SlcDevUSBCfgTCPAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 41),
    _SlcDevUSBCfgTCPAuth_Type()
)
slcDevUSBCfgTCPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgTCPAuth.setStatus("current")
_SlcDevUSBCfgGSMPIN_Type = OctetString
_SlcDevUSBCfgGSMPIN_Object = MibTableColumn
slcDevUSBCfgGSMPIN = _SlcDevUSBCfgGSMPIN_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 42),
    _SlcDevUSBCfgGSMPIN_Type()
)
slcDevUSBCfgGSMPIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMPIN.setStatus("current")
_SlcDevUSBCfgGSMPPPCompression_Type = EnabledState
_SlcDevUSBCfgGSMPPPCompression_Object = MibTableColumn
slcDevUSBCfgGSMPPPCompression = _SlcDevUSBCfgGSMPPPCompression_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 43),
    _SlcDevUSBCfgGSMPPPCompression_Type()
)
slcDevUSBCfgGSMPPPCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMPPPCompression.setStatus("current")
_SlcDevUSBCfgGSMAutoAcquireDNS_Type = EnabledState
_SlcDevUSBCfgGSMAutoAcquireDNS_Object = MibTableColumn
slcDevUSBCfgGSMAutoAcquireDNS = _SlcDevUSBCfgGSMAutoAcquireDNS_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 44),
    _SlcDevUSBCfgGSMAutoAcquireDNS_Type()
)
slcDevUSBCfgGSMAutoAcquireDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMAutoAcquireDNS.setStatus("current")


class _SlcDevUSBCfgGSMDialoutMode_Type(Integer32):
    """Custom type slcDevUSBCfgGSMDialoutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gprs", 1),
          ("gsm", 2))
    )


_SlcDevUSBCfgGSMDialoutMode_Type.__name__ = "Integer32"
_SlcDevUSBCfgGSMDialoutMode_Object = MibTableColumn
slcDevUSBCfgGSMDialoutMode = _SlcDevUSBCfgGSMDialoutMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 45),
    _SlcDevUSBCfgGSMDialoutMode_Type()
)
slcDevUSBCfgGSMDialoutMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMDialoutMode.setStatus("current")
_SlcDevUSBCfgGSMContextID_Type = OctetString
_SlcDevUSBCfgGSMContextID_Object = MibTableColumn
slcDevUSBCfgGSMContextID = _SlcDevUSBCfgGSMContextID_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 46),
    _SlcDevUSBCfgGSMContextID_Type()
)
slcDevUSBCfgGSMContextID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMContextID.setStatus("current")
_SlcDevUSBCfgGSMBearerService_Type = OctetString
_SlcDevUSBCfgGSMBearerService_Object = MibTableColumn
slcDevUSBCfgGSMBearerService = _SlcDevUSBCfgGSMBearerService_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 47),
    _SlcDevUSBCfgGSMBearerService_Type()
)
slcDevUSBCfgGSMBearerService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGSMBearerService.setStatus("current")
_SlcDevUSBCfgCHAPAuthLocalUsers_Type = EnabledState
_SlcDevUSBCfgCHAPAuthLocalUsers_Object = MibTableColumn
slcDevUSBCfgCHAPAuthLocalUsers = _SlcDevUSBCfgCHAPAuthLocalUsers_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 48),
    _SlcDevUSBCfgCHAPAuthLocalUsers_Type()
)
slcDevUSBCfgCHAPAuthLocalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgCHAPAuthLocalUsers.setStatus("current")
_SlcDevUSBCfgUseSites_Type = EnabledState
_SlcDevUSBCfgUseSites_Object = MibTableColumn
slcDevUSBCfgUseSites = _SlcDevUSBCfgUseSites_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 49),
    _SlcDevUSBCfgUseSites_Type()
)
slcDevUSBCfgUseSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgUseSites.setStatus("current")
_SlcDevUSBCfgDialbackRetries_Type = Integer32
_SlcDevUSBCfgDialbackRetries_Object = MibTableColumn
slcDevUSBCfgDialbackRetries = _SlcDevUSBCfgDialbackRetries_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 50),
    _SlcDevUSBCfgDialbackRetries_Type()
)
slcDevUSBCfgDialbackRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialbackRetries.setStatus("current")


class _SlcDevUSBCfgDialtoneCheck_Type(Integer32):
    """Custom type slcDevUSBCfgDialtoneCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SlcDevUSBCfgDialtoneCheck_Type.__name__ = "Integer32"
_SlcDevUSBCfgDialtoneCheck_Object = MibTableColumn
slcDevUSBCfgDialtoneCheck = _SlcDevUSBCfgDialtoneCheck_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 51),
    _SlcDevUSBCfgDialtoneCheck_Type()
)
slcDevUSBCfgDialtoneCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialtoneCheck.setStatus("current")
if mibBuilder.loadTexts:
    slcDevUSBCfgDialtoneCheck.setUnits("minutes")
_SlcDevUSBCfgGroup_Type = OctetString
_SlcDevUSBCfgGroup_Object = MibTableColumn
slcDevUSBCfgGroup = _SlcDevUSBCfgGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 5, 2, 1, 52),
    _SlcDevUSBCfgGroup_Type()
)
slcDevUSBCfgGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevUSBCfgGroup.setStatus("current")
_SlcDevIntModem_ObjectIdentity = ObjectIdentity
slcDevIntModem = _SlcDevIntModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6)
)


class _SlcDevIntModemModemState_Type(Integer32):
    """Custom type slcDevIntModemModemState based on Integer32"""
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
        *(("dialback", 4),
          ("dialin", 3),
          ("dialout", 2),
          ("disabled", 1))
    )


_SlcDevIntModemModemState_Type.__name__ = "Integer32"
_SlcDevIntModemModemState_Object = MibScalar
slcDevIntModemModemState = _SlcDevIntModemModemState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 1),
    _SlcDevIntModemModemState_Type()
)
slcDevIntModemModemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemModemState.setStatus("current")


class _SlcDevIntModemModemMode_Type(Integer32):
    """Custom type slcDevIntModemModemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 1),
          ("text", 2))
    )


_SlcDevIntModemModemMode_Type.__name__ = "Integer32"
_SlcDevIntModemModemMode_Object = MibScalar
slcDevIntModemModemMode = _SlcDevIntModemModemMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 2),
    _SlcDevIntModemModemMode_Type()
)
slcDevIntModemModemMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemModemMode.setStatus("current")
_SlcDevIntModemLocalIP_Type = IpAddress
_SlcDevIntModemLocalIP_Object = MibScalar
slcDevIntModemLocalIP = _SlcDevIntModemLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 3),
    _SlcDevIntModemLocalIP_Type()
)
slcDevIntModemLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemLocalIP.setStatus("current")
_SlcDevIntModemRemoteIP_Type = IpAddress
_SlcDevIntModemRemoteIP_Object = MibScalar
slcDevIntModemRemoteIP = _SlcDevIntModemRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 4),
    _SlcDevIntModemRemoteIP_Type()
)
slcDevIntModemRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemRemoteIP.setStatus("current")


class _SlcDevIntModemAuth_Type(Integer32):
    """Custom type slcDevIntModemAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("chap", 2),
          ("pap", 1))
    )


_SlcDevIntModemAuth_Type.__name__ = "Integer32"
_SlcDevIntModemAuth_Object = MibScalar
slcDevIntModemAuth = _SlcDevIntModemAuth_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 5),
    _SlcDevIntModemAuth_Type()
)
slcDevIntModemAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemAuth.setStatus("current")
_SlcDevIntModemCHAPHost_Type = OctetString
_SlcDevIntModemCHAPHost_Object = MibScalar
slcDevIntModemCHAPHost = _SlcDevIntModemCHAPHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 6),
    _SlcDevIntModemCHAPHost_Type()
)
slcDevIntModemCHAPHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemCHAPHost.setStatus("current")
_SlcDevIntModemInitScript_Type = OctetString
_SlcDevIntModemInitScript_Object = MibScalar
slcDevIntModemInitScript = _SlcDevIntModemInitScript_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 7),
    _SlcDevIntModemInitScript_Type()
)
slcDevIntModemInitScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemInitScript.setStatus("current")


class _SlcDevIntModemTimeout_Type(Integer32):
    """Custom type slcDevIntModemTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_SlcDevIntModemTimeout_Type.__name__ = "Integer32"
_SlcDevIntModemTimeout_Object = MibScalar
slcDevIntModemTimeout = _SlcDevIntModemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 8),
    _SlcDevIntModemTimeout_Type()
)
slcDevIntModemTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevIntModemTimeout.setUnits("minutes")
_SlcDevIntModemDialoutNum_Type = OctetString
_SlcDevIntModemDialoutNum_Object = MibScalar
slcDevIntModemDialoutNum = _SlcDevIntModemDialoutNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 9),
    _SlcDevIntModemDialoutNum_Type()
)
slcDevIntModemDialoutNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialoutNum.setStatus("current")


class _SlcDevIntModemDialoutLogin_Type(OctetString):
    """Custom type slcDevIntModemDialoutLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcDevIntModemDialoutLogin_Type.__name__ = "OctetString"
_SlcDevIntModemDialoutLogin_Object = MibScalar
slcDevIntModemDialoutLogin = _SlcDevIntModemDialoutLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 10),
    _SlcDevIntModemDialoutLogin_Type()
)
slcDevIntModemDialoutLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialoutLogin.setStatus("current")


class _SlcDevIntModemDialbackMode_Type(Integer32):
    """Custom type slcDevIntModemDialbackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("usernumber", 1))
    )


_SlcDevIntModemDialbackMode_Type.__name__ = "Integer32"
_SlcDevIntModemDialbackMode_Object = MibScalar
slcDevIntModemDialbackMode = _SlcDevIntModemDialbackMode_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 11),
    _SlcDevIntModemDialbackMode_Type()
)
slcDevIntModemDialbackMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialbackMode.setStatus("current")
_SlcDevIntModemDialbackNum_Type = OctetString
_SlcDevIntModemDialbackNum_Object = MibScalar
slcDevIntModemDialbackNum = _SlcDevIntModemDialbackNum_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 12),
    _SlcDevIntModemDialbackNum_Type()
)
slcDevIntModemDialbackNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialbackNum.setStatus("current")
_SlcDevIntModemDialbackRetries_Type = Integer32
_SlcDevIntModemDialbackRetries_Object = MibScalar
slcDevIntModemDialbackRetries = _SlcDevIntModemDialbackRetries_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 13),
    _SlcDevIntModemDialbackRetries_Type()
)
slcDevIntModemDialbackRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialbackRetries.setStatus("current")
_SlcDevIntModemDialbackDelay_Type = Integer32
_SlcDevIntModemDialbackDelay_Object = MibScalar
slcDevIntModemDialbackDelay = _SlcDevIntModemDialbackDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 14),
    _SlcDevIntModemDialbackDelay_Type()
)
slcDevIntModemDialbackDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialbackDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevIntModemDialbackDelay.setUnits("seconds")
_SlcDevIntModemCallerIdLogging_Type = EnabledState
_SlcDevIntModemCallerIdLogging_Object = MibScalar
slcDevIntModemCallerIdLogging = _SlcDevIntModemCallerIdLogging_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 15),
    _SlcDevIntModemCallerIdLogging_Type()
)
slcDevIntModemCallerIdLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemCallerIdLogging.setStatus("current")
_SlcDevIntModemCallerIdATCmd_Type = OctetString
_SlcDevIntModemCallerIdATCmd_Object = MibScalar
slcDevIntModemCallerIdATCmd = _SlcDevIntModemCallerIdATCmd_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 16),
    _SlcDevIntModemCallerIdATCmd_Type()
)
slcDevIntModemCallerIdATCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemCallerIdATCmd.setStatus("current")
_SlcDevIntModemUseSites_Type = EnabledState
_SlcDevIntModemUseSites_Object = MibScalar
slcDevIntModemUseSites = _SlcDevIntModemUseSites_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 17),
    _SlcDevIntModemUseSites_Type()
)
slcDevIntModemUseSites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemUseSites.setStatus("current")
_SlcDevIntModemGroup_Type = OctetString
_SlcDevIntModemGroup_Object = MibScalar
slcDevIntModemGroup = _SlcDevIntModemGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 18),
    _SlcDevIntModemGroup_Type()
)
slcDevIntModemGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemGroup.setStatus("current")
_SlcDevIntModemIdleTimeout_Type = Integer32
_SlcDevIntModemIdleTimeout_Object = MibScalar
slcDevIntModemIdleTimeout = _SlcDevIntModemIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 19),
    _SlcDevIntModemIdleTimeout_Type()
)
slcDevIntModemIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcDevIntModemIdleTimeout.setUnits("seconds")
_SlcDevIntModemRestartDelay_Type = Integer32
_SlcDevIntModemRestartDelay_Object = MibScalar
slcDevIntModemRestartDelay = _SlcDevIntModemRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 20),
    _SlcDevIntModemRestartDelay_Type()
)
slcDevIntModemRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcDevIntModemRestartDelay.setUnits("seconds")
_SlcDevIntModemNATState_Type = EnabledState
_SlcDevIntModemNATState_Object = MibScalar
slcDevIntModemNATState = _SlcDevIntModemNATState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 21),
    _SlcDevIntModemNATState_Type()
)
slcDevIntModemNATState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemNATState.setStatus("current")


class _SlcDevIntModemDialtoneCheck_Type(Integer32):
    """Custom type slcDevIntModemDialtoneCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SlcDevIntModemDialtoneCheck_Type.__name__ = "Integer32"
_SlcDevIntModemDialtoneCheck_Object = MibScalar
slcDevIntModemDialtoneCheck = _SlcDevIntModemDialtoneCheck_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 6, 22),
    _SlcDevIntModemDialtoneCheck_Type()
)
slcDevIntModemDialtoneCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevIntModemDialtoneCheck.setStatus("current")
if mibBuilder.loadTexts:
    slcDevIntModemDialtoneCheck.setUnits("minutes")
_SlcDevRPM_ObjectIdentity = ObjectIdentity
slcDevRPM = _SlcDevRPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7)
)
_SlcDevRPMCfgTable_Object = MibTable
slcDevRPMCfgTable = _SlcDevRPMCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    slcDevRPMCfgTable.setStatus("current")
_SlcDevRPMCfgEntry_Object = MibTableRow
slcDevRPMCfgEntry = _SlcDevRPMCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1)
)
slcDevRPMCfgEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevRPMId"),
)
if mibBuilder.loadTexts:
    slcDevRPMCfgEntry.setStatus("current")


class _SlcDevRPMId_Type(Integer32):
    """Custom type slcDevRPMId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_SlcDevRPMId_Type.__name__ = "Integer32"
_SlcDevRPMId_Object = MibTableColumn
slcDevRPMId = _SlcDevRPMId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 1),
    _SlcDevRPMId_Type()
)
slcDevRPMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMId.setStatus("current")


class _SlcDevRPMName_Type(OctetString):
    """Custom type slcDevRPMName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SlcDevRPMName_Type.__name__ = "OctetString"
_SlcDevRPMName_Object = MibTableColumn
slcDevRPMName = _SlcDevRPMName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 2),
    _SlcDevRPMName_Type()
)
slcDevRPMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMName.setStatus("current")
_SlcDevRPMVendorModel_Type = OctetString
_SlcDevRPMVendorModel_Object = MibTableColumn
slcDevRPMVendorModel = _SlcDevRPMVendorModel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 3),
    _SlcDevRPMVendorModel_Type()
)
slcDevRPMVendorModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMVendorModel.setStatus("current")


class _SlcDevRPMManagedVia_Type(Integer32):
    """Custom type slcDevRPMManagedVia based on Integer32"""
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
        *(("network", 2),
          ("serial", 1),
          ("snmp", 3),
          ("usb", 4))
    )


_SlcDevRPMManagedVia_Type.__name__ = "Integer32"
_SlcDevRPMManagedVia_Object = MibTableColumn
slcDevRPMManagedVia = _SlcDevRPMManagedVia_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 4),
    _SlcDevRPMManagedVia_Type()
)
slcDevRPMManagedVia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMManagedVia.setStatus("current")
_SlcDevRPMIPAddress_Type = IpAddress
_SlcDevRPMIPAddress_Object = MibTableColumn
slcDevRPMIPAddress = _SlcDevRPMIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 5),
    _SlcDevRPMIPAddress_Type()
)
slcDevRPMIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMIPAddress.setStatus("current")
_SlcDevRPMPort_Type = Integer32
_SlcDevRPMPort_Object = MibTableColumn
slcDevRPMPort = _SlcDevRPMPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 6),
    _SlcDevRPMPort_Type()
)
slcDevRPMPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMPort.setStatus("current")
_SlcDevRPMDriverOpts_Type = OctetString
_SlcDevRPMDriverOpts_Object = MibTableColumn
slcDevRPMDriverOpts = _SlcDevRPMDriverOpts_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 7),
    _SlcDevRPMDriverOpts_Type()
)
slcDevRPMDriverOpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMDriverOpts.setStatus("current")
_SlcDevRPMStatus_Type = OctetString
_SlcDevRPMStatus_Object = MibTableColumn
slcDevRPMStatus = _SlcDevRPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 8),
    _SlcDevRPMStatus_Type()
)
slcDevRPMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMStatus.setStatus("current")
_SlcDevRPMFirmwareVersion_Type = OctetString
_SlcDevRPMFirmwareVersion_Object = MibTableColumn
slcDevRPMFirmwareVersion = _SlcDevRPMFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 9),
    _SlcDevRPMFirmwareVersion_Type()
)
slcDevRPMFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMFirmwareVersion.setStatus("current")
_SlcDevRPMSerialNumber_Type = OctetString
_SlcDevRPMSerialNumber_Object = MibTableColumn
slcDevRPMSerialNumber = _SlcDevRPMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 10),
    _SlcDevRPMSerialNumber_Type()
)
slcDevRPMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMSerialNumber.setStatus("current")
_SlcDevRPMMACAddress_Type = OctetString
_SlcDevRPMMACAddress_Object = MibTableColumn
slcDevRPMMACAddress = _SlcDevRPMMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 11),
    _SlcDevRPMMACAddress_Type()
)
slcDevRPMMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMMACAddress.setStatus("current")


class _SlcDevRPMNumOutlets_Type(Integer32):
    """Custom type slcDevRPMNumOutlets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_SlcDevRPMNumOutlets_Type.__name__ = "Integer32"
_SlcDevRPMNumOutlets_Object = MibTableColumn
slcDevRPMNumOutlets = _SlcDevRPMNumOutlets_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 12),
    _SlcDevRPMNumOutlets_Type()
)
slcDevRPMNumOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMNumOutlets.setStatus("current")


class _SlcDevRPMOutletsOn_Type(Integer32):
    """Custom type slcDevRPMOutletsOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 120),
    )


_SlcDevRPMOutletsOn_Type.__name__ = "Integer32"
_SlcDevRPMOutletsOn_Object = MibTableColumn
slcDevRPMOutletsOn = _SlcDevRPMOutletsOn_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 13),
    _SlcDevRPMOutletsOn_Type()
)
slcDevRPMOutletsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMOutletsOn.setStatus("current")


class _SlcDevRPMSNMPReadComm_Type(OctetString):
    """Custom type slcDevRPMSNMPReadComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SlcDevRPMSNMPReadComm_Type.__name__ = "OctetString"
_SlcDevRPMSNMPReadComm_Object = MibTableColumn
slcDevRPMSNMPReadComm = _SlcDevRPMSNMPReadComm_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 14),
    _SlcDevRPMSNMPReadComm_Type()
)
slcDevRPMSNMPReadComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMSNMPReadComm.setStatus("current")


class _SlcDevRPMAdminLogin_Type(OctetString):
    """Custom type slcDevRPMAdminLogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SlcDevRPMAdminLogin_Type.__name__ = "OctetString"
_SlcDevRPMAdminLogin_Object = MibTableColumn
slcDevRPMAdminLogin = _SlcDevRPMAdminLogin_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 15),
    _SlcDevRPMAdminLogin_Type()
)
slcDevRPMAdminLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMAdminLogin.setStatus("current")


class _SlcDevRPMLogStatus_Type(Integer32):
    """Custom type slcDevRPMLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_SlcDevRPMLogStatus_Type.__name__ = "Integer32"
_SlcDevRPMLogStatus_Object = MibTableColumn
slcDevRPMLogStatus = _SlcDevRPMLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 16),
    _SlcDevRPMLogStatus_Type()
)
slcDevRPMLogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMLogStatus.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMLogStatus.setUnits("minutes")
_SlcDevRPMCriticalSNMPTraps_Type = EnabledState
_SlcDevRPMCriticalSNMPTraps_Object = MibTableColumn
slcDevRPMCriticalSNMPTraps = _SlcDevRPMCriticalSNMPTraps_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 17),
    _SlcDevRPMCriticalSNMPTraps_Type()
)
slcDevRPMCriticalSNMPTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMCriticalSNMPTraps.setStatus("current")
_SlcDevRPMCriticalEmails_Type = OctetString
_SlcDevRPMCriticalEmails_Object = MibTableColumn
slcDevRPMCriticalEmails = _SlcDevRPMCriticalEmails_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 18),
    _SlcDevRPMCriticalEmails_Type()
)
slcDevRPMCriticalEmails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMCriticalEmails.setStatus("current")
_SlcDevRPMProvidesSLCPower_Type = EnabledState
_SlcDevRPMProvidesSLCPower_Object = MibTableColumn
slcDevRPMProvidesSLCPower = _SlcDevRPMProvidesSLCPower_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 19),
    _SlcDevRPMProvidesSLCPower_Type()
)
slcDevRPMProvidesSLCPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMProvidesSLCPower.setStatus("current")


class _SlcDevRPMOnLowBattery_Type(Integer32):
    """Custom type slcDevRPMOnLowBattery based on Integer32"""
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
        *(("allowBatteryToFail", 3),
          ("shutdownAllUPS", 2),
          ("shutdownSLCUPS", 4),
          ("shutdownThisUPS", 1))
    )


_SlcDevRPMOnLowBattery_Type.__name__ = "Integer32"
_SlcDevRPMOnLowBattery_Object = MibTableColumn
slcDevRPMOnLowBattery = _SlcDevRPMOnLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 20),
    _SlcDevRPMOnLowBattery_Type()
)
slcDevRPMOnLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMOnLowBattery.setStatus("current")


class _SlcDevRPMShutdownOrder_Type(Integer32):
    """Custom type slcDevRPMShutdownOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_SlcDevRPMShutdownOrder_Type.__name__ = "Integer32"
_SlcDevRPMShutdownOrder_Object = MibTableColumn
slcDevRPMShutdownOrder = _SlcDevRPMShutdownOrder_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 21),
    _SlcDevRPMShutdownOrder_Type()
)
slcDevRPMShutdownOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMShutdownOrder.setStatus("current")


class _SlcDevRPMLoad_Type(Integer32):
    """Custom type slcDevRPMLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_SlcDevRPMLoad_Type.__name__ = "Integer32"
_SlcDevRPMLoad_Object = MibTableColumn
slcDevRPMLoad = _SlcDevRPMLoad_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 22),
    _SlcDevRPMLoad_Type()
)
slcDevRPMLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMLoad.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMLoad.setUnits("tenths of a percent")


class _SlcDevRPMLoadOverThreshold_Type(Integer32):
    """Custom type slcDevRPMLoadOverThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_SlcDevRPMLoadOverThreshold_Type.__name__ = "Integer32"
_SlcDevRPMLoadOverThreshold_Object = MibTableColumn
slcDevRPMLoadOverThreshold = _SlcDevRPMLoadOverThreshold_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 23),
    _SlcDevRPMLoadOverThreshold_Type()
)
slcDevRPMLoadOverThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMLoadOverThreshold.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMLoadOverThreshold.setUnits("tenths of a percent")


class _SlcDevRPMBatteryCharge_Type(Integer32):
    """Custom type slcDevRPMBatteryCharge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )


_SlcDevRPMBatteryCharge_Type.__name__ = "Integer32"
_SlcDevRPMBatteryCharge_Object = MibTableColumn
slcDevRPMBatteryCharge = _SlcDevRPMBatteryCharge_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 24),
    _SlcDevRPMBatteryCharge_Type()
)
slcDevRPMBatteryCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMBatteryCharge.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMBatteryCharge.setUnits("tenths of a percent")
_SlcDevRPMBatteryRuntime_Type = TimeTicks
_SlcDevRPMBatteryRuntime_Object = MibTableColumn
slcDevRPMBatteryRuntime = _SlcDevRPMBatteryRuntime_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 25),
    _SlcDevRPMBatteryRuntime_Type()
)
slcDevRPMBatteryRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMBatteryRuntime.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMBatteryRuntime.setUnits("hundredths of seconds")
_SlcDevRPMBeeperStatus_Type = EnabledState
_SlcDevRPMBeeperStatus_Object = MibTableColumn
slcDevRPMBeeperStatus = _SlcDevRPMBeeperStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 26),
    _SlcDevRPMBeeperStatus_Type()
)
slcDevRPMBeeperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMBeeperStatus.setStatus("current")
_SlcDevRPMTemperature_Type = Integer32
_SlcDevRPMTemperature_Object = MibTableColumn
slcDevRPMTemperature = _SlcDevRPMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 27),
    _SlcDevRPMTemperature_Type()
)
slcDevRPMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMTemperature.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMTemperature.setUnits("Celsius")
_SlcDevRPMUptime_Type = TimeTicks
_SlcDevRPMUptime_Object = MibTableColumn
slcDevRPMUptime = _SlcDevRPMUptime_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 1, 1, 28),
    _SlcDevRPMUptime_Type()
)
slcDevRPMUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMUptime.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMUptime.setUnits("hundredths of seconds")
_SlcDevRPMStatusTable_Object = MibTable
slcDevRPMStatusTable = _SlcDevRPMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2)
)
if mibBuilder.loadTexts:
    slcDevRPMStatusTable.setStatus("current")
_SlcDevRPMStatusEntry_Object = MibTableRow
slcDevRPMStatusEntry = _SlcDevRPMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1)
)
slcDevRPMStatusEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevRPMId"),
    (0, "LANTRONIX-SLC-MIB", "RPMTowerIndex"),
)
if mibBuilder.loadTexts:
    slcDevRPMStatusEntry.setStatus("current")
_SlcDevRPMCurrent_Type = Integer32
_SlcDevRPMCurrent_Object = MibTableColumn
slcDevRPMCurrent = _SlcDevRPMCurrent_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 1),
    _SlcDevRPMCurrent_Type()
)
slcDevRPMCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMCurrent.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMCurrent.setUnits("tenths of Amps")
_SlcDevRPMInputVoltage_Type = Integer32
_SlcDevRPMInputVoltage_Object = MibTableColumn
slcDevRPMInputVoltage = _SlcDevRPMInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 2),
    _SlcDevRPMInputVoltage_Type()
)
slcDevRPMInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMInputVoltage.setUnits("tenths of Volts")
_SlcDevRPMApparentPower_Type = Integer32
_SlcDevRPMApparentPower_Object = MibTableColumn
slcDevRPMApparentPower = _SlcDevRPMApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 3),
    _SlcDevRPMApparentPower_Type()
)
slcDevRPMApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMApparentPower.setUnits("tenths of Volt-Amps")
_SlcDevRPMNominalApparentPower_Type = Integer32
_SlcDevRPMNominalApparentPower_Object = MibTableColumn
slcDevRPMNominalApparentPower = _SlcDevRPMNominalApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 4),
    _SlcDevRPMNominalApparentPower_Type()
)
slcDevRPMNominalApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMNominalApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMNominalApparentPower.setUnits("tenths of Volt-Amps")
_SlcDevRPMRealPower_Type = Integer32
_SlcDevRPMRealPower_Object = MibTableColumn
slcDevRPMRealPower = _SlcDevRPMRealPower_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 5),
    _SlcDevRPMRealPower_Type()
)
slcDevRPMRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMRealPower.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMRealPower.setUnits("tenths of Watts")
_SlcDevRPMNominalRealPower_Type = Integer32
_SlcDevRPMNominalRealPower_Object = MibTableColumn
slcDevRPMNominalRealPower = _SlcDevRPMNominalRealPower_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 2, 1, 6),
    _SlcDevRPMNominalRealPower_Type()
)
slcDevRPMNominalRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMNominalRealPower.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMNominalRealPower.setUnits("tenths of Watts")
_SlcDevRPMOutletTable_Object = MibTable
slcDevRPMOutletTable = _SlcDevRPMOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    slcDevRPMOutletTable.setStatus("current")
_SlcDevRPMOutletEntry_Object = MibTableRow
slcDevRPMOutletEntry = _SlcDevRPMOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3, 1)
)
slcDevRPMOutletEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcDevRPMId"),
    (0, "LANTRONIX-SLC-MIB", "RPMOutletIndex"),
)
if mibBuilder.loadTexts:
    slcDevRPMOutletEntry.setStatus("current")
_SlcDevRPMOutletName_Type = OctetString
_SlcDevRPMOutletName_Object = MibTableColumn
slcDevRPMOutletName = _SlcDevRPMOutletName_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3, 1, 1),
    _SlcDevRPMOutletName_Type()
)
slcDevRPMOutletName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMOutletName.setStatus("current")


class _SlcDevRPMOutletState_Type(Integer32):
    """Custom type slcDevRPMOutletState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("unknown", 1))
    )


_SlcDevRPMOutletState_Type.__name__ = "Integer32"
_SlcDevRPMOutletState_Object = MibTableColumn
slcDevRPMOutletState = _SlcDevRPMOutletState_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3, 1, 2),
    _SlcDevRPMOutletState_Type()
)
slcDevRPMOutletState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMOutletState.setStatus("current")
_SlcDevRPMOutletCurrent_Type = Integer32
_SlcDevRPMOutletCurrent_Object = MibTableColumn
slcDevRPMOutletCurrent = _SlcDevRPMOutletCurrent_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3, 1, 3),
    _SlcDevRPMOutletCurrent_Type()
)
slcDevRPMOutletCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevRPMOutletCurrent.setStatus("current")
if mibBuilder.loadTexts:
    slcDevRPMOutletCurrent.setUnits("tenths of Amps")


class _SlcDevRPMOutletAction_Type(Integer32):
    """Custom type slcDevRPMOutletAction based on Integer32"""
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
        *(("cyclePower", 4),
          ("noAction", 1),
          ("turnOff", 2),
          ("turnOn", 3))
    )


_SlcDevRPMOutletAction_Type.__name__ = "Integer32"
_SlcDevRPMOutletAction_Object = MibTableColumn
slcDevRPMOutletAction = _SlcDevRPMOutletAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 4, 7, 3, 1, 4),
    _SlcDevRPMOutletAction_Type()
)
slcDevRPMOutletAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcDevRPMOutletAction.setStatus("current")
_SlcConnections_ObjectIdentity = ObjectIdentity
slcConnections = _SlcConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5)
)
_SlcConnNumber_Type = Integer32
_SlcConnNumber_Object = MibScalar
slcConnNumber = _SlcConnNumber_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 1),
    _SlcConnNumber_Type()
)
slcConnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnNumber.setStatus("current")
_SlcConnTable_Object = MibTable
slcConnTable = _SlcConnTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    slcConnTable.setStatus("current")
_SlcConnEntry_Object = MibTableRow
slcConnEntry = _SlcConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1)
)
slcConnEntry.setIndexNames(
    (0, "LANTRONIX-SLC-MIB", "slcConnIndex"),
)
if mibBuilder.loadTexts:
    slcConnEntry.setStatus("current")


class _SlcConnIndex_Type(Integer32):
    """Custom type slcConnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SlcConnIndex_Type.__name__ = "Integer32"
_SlcConnIndex_Object = MibTableColumn
slcConnIndex = _SlcConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 1),
    _SlcConnIndex_Type()
)
slcConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnIndex.setStatus("current")
_SlcConnEndPt1_Type = OctetString
_SlcConnEndPt1_Object = MibTableColumn
slcConnEndPt1 = _SlcConnEndPt1_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 2),
    _SlcConnEndPt1_Type()
)
slcConnEndPt1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnEndPt1.setStatus("current")
_SlcConnEndPt2_Type = OctetString
_SlcConnEndPt2_Object = MibTableColumn
slcConnEndPt2 = _SlcConnEndPt2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 3),
    _SlcConnEndPt2_Type()
)
slcConnEndPt2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnEndPt2.setStatus("current")


class _SlcConnFlow_Type(Integer32):
    """Custom type slcConnFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 1),
          ("endpt1toendpt2", 2),
          ("endpt2toendpt1", 3))
    )


_SlcConnFlow_Type.__name__ = "Integer32"
_SlcConnFlow_Object = MibTableColumn
slcConnFlow = _SlcConnFlow_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 4),
    _SlcConnFlow_Type()
)
slcConnFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnFlow.setStatus("current")


class _SlcConnUser_Type(OctetString):
    """Custom type slcConnUser based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlcConnUser_Type.__name__ = "OctetString"
_SlcConnUser_Object = MibTableColumn
slcConnUser = _SlcConnUser_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 5),
    _SlcConnUser_Type()
)
slcConnUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnUser.setStatus("current")
_SlcConnDuration_Type = Integer32
_SlcConnDuration_Object = MibTableColumn
slcConnDuration = _SlcConnDuration_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 6),
    _SlcConnDuration_Type()
)
slcConnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnDuration.setStatus("current")
if mibBuilder.loadTexts:
    slcConnDuration.setUnits("seconds")
_SlcConnDurationStr_Type = OctetString
_SlcConnDurationStr_Object = MibTableColumn
slcConnDurationStr = _SlcConnDurationStr_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 7),
    _SlcConnDurationStr_Type()
)
slcConnDurationStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnDurationStr.setStatus("current")
_SlcConnIdle_Type = Integer32
_SlcConnIdle_Object = MibTableColumn
slcConnIdle = _SlcConnIdle_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 8),
    _SlcConnIdle_Type()
)
slcConnIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnIdle.setStatus("current")
if mibBuilder.loadTexts:
    slcConnIdle.setUnits("seconds")
_SlcConnIdleStr_Type = OctetString
_SlcConnIdleStr_Object = MibTableColumn
slcConnIdleStr = _SlcConnIdleStr_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 9),
    _SlcConnIdleStr_Type()
)
slcConnIdleStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnIdleStr.setStatus("current")
_SlcConnSourceIP_Type = IpAddress
_SlcConnSourceIP_Object = MibTableColumn
slcConnSourceIP = _SlcConnSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 5, 2, 1, 10),
    _SlcConnSourceIP_Type()
)
slcConnSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcConnSourceIP.setStatus("current")
_SlcSystem_ObjectIdentity = ObjectIdentity
slcSystem = _SlcSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6)
)
_SlcSystemModel_Type = OctetString
_SlcSystemModel_Object = MibScalar
slcSystemModel = _SlcSystemModel_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 1),
    _SlcSystemModel_Type()
)
slcSystemModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemModel.setStatus("current")
_SlcSystemSerialNo_Type = OctetString
_SlcSystemSerialNo_Object = MibScalar
slcSystemSerialNo = _SlcSystemSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 2),
    _SlcSystemSerialNo_Type()
)
slcSystemSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemSerialNo.setStatus("current")
_SlcSystemFWRev_Type = OctetString
_SlcSystemFWRev_Object = MibScalar
slcSystemFWRev = _SlcSystemFWRev_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 3),
    _SlcSystemFWRev_Type()
)
slcSystemFWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemFWRev.setStatus("current")


class _SlcSystemLoadVia_Type(Integer32):
    """Custom type slcSystemLoadVia based on Integer32"""
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
        *(("ftp", 1),
          ("https", 5),
          ("nfs", 6),
          ("pccard", 7),
          ("sftp", 3),
          ("slm", 4),
          ("tftp", 2))
    )


_SlcSystemLoadVia_Type.__name__ = "Integer32"
_SlcSystemLoadVia_Object = MibScalar
slcSystemLoadVia = _SlcSystemLoadVia_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 4),
    _SlcSystemLoadVia_Type()
)
slcSystemLoadVia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLoadVia.setStatus("current")
_SlcSystemFTPServer_Type = IpAddress
_SlcSystemFTPServer_Object = MibScalar
slcSystemFTPServer = _SlcSystemFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 5),
    _SlcSystemFTPServer_Type()
)
slcSystemFTPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemFTPServer.setStatus("current")
_SlcSystemFTPPath_Type = OctetString
_SlcSystemFTPPath_Object = MibScalar
slcSystemFTPPath = _SlcSystemFTPPath_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 6),
    _SlcSystemFTPPath_Type()
)
slcSystemFTPPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemFTPPath.setStatus("current")
_SlcSystemKeypadLock_Type = EnabledState
_SlcSystemKeypadLock_Object = MibScalar
slcSystemKeypadLock = _SlcSystemKeypadLock_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 7),
    _SlcSystemKeypadLock_Type()
)
slcSystemKeypadLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemKeypadLock.setStatus("current")
_SlcSystemTimeZone_Type = OctetString
_SlcSystemTimeZone_Object = MibScalar
slcSystemTimeZone = _SlcSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 8),
    _SlcSystemTimeZone_Type()
)
slcSystemTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemTimeZone.setStatus("current")
_SlcSystemWelcomeBanner_Type = OctetString
_SlcSystemWelcomeBanner_Object = MibScalar
slcSystemWelcomeBanner = _SlcSystemWelcomeBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 9),
    _SlcSystemWelcomeBanner_Type()
)
slcSystemWelcomeBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWelcomeBanner.setStatus("current")
_SlcSystemLoginBanner_Type = OctetString
_SlcSystemLoginBanner_Object = MibScalar
slcSystemLoginBanner = _SlcSystemLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 10),
    _SlcSystemLoginBanner_Type()
)
slcSystemLoginBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLoginBanner.setStatus("current")
_SlcSystemLogoutBanner_Type = OctetString
_SlcSystemLogoutBanner_Object = MibScalar
slcSystemLogoutBanner = _SlcSystemLogoutBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 11),
    _SlcSystemLogoutBanner_Type()
)
slcSystemLogoutBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLogoutBanner.setStatus("current")


class _SlcSystemWebTimeout_Type(Integer32):
    """Custom type slcSystemWebTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 120),
    )


_SlcSystemWebTimeout_Type.__name__ = "Integer32"
_SlcSystemWebTimeout_Object = MibScalar
slcSystemWebTimeout = _SlcSystemWebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 12),
    _SlcSystemWebTimeout_Type()
)
slcSystemWebTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemWebTimeout.setUnits("minutes")
_SlcSystemWebGadget_Type = EnabledState
_SlcSystemWebGadget_Object = MibScalar
slcSystemWebGadget = _SlcSystemWebGadget_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 13),
    _SlcSystemWebGadget_Type()
)
slcSystemWebGadget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebGadget.setStatus("current")


class _SlcSystemAction_Type(Integer32):
    """Custom type slcSystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("rebootSLC", 2),
          ("shutdownSLC", 3))
    )


_SlcSystemAction_Type.__name__ = "Integer32"
_SlcSystemAction_Object = MibScalar
slcSystemAction = _SlcSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 14),
    _SlcSystemAction_Type()
)
slcSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slcSystemAction.setStatus("current")
_SlcSystemSSHPreAuthBanner_Type = OctetString
_SlcSystemSSHPreAuthBanner_Object = MibScalar
slcSystemSSHPreAuthBanner = _SlcSystemSSHPreAuthBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 15),
    _SlcSystemSSHPreAuthBanner_Type()
)
slcSystemSSHPreAuthBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemSSHPreAuthBanner.setStatus("current")


class _SlcSystemSiteRackRow_Type(Integer32):
    """Custom type slcSystemSiteRackRow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SlcSystemSiteRackRow_Type.__name__ = "Integer32"
_SlcSystemSiteRackRow_Object = MibScalar
slcSystemSiteRackRow = _SlcSystemSiteRackRow_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 16),
    _SlcSystemSiteRackRow_Type()
)
slcSystemSiteRackRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemSiteRackRow.setStatus("current")


class _SlcSystemSiteRackCluster_Type(Integer32):
    """Custom type slcSystemSiteRackCluster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SlcSystemSiteRackCluster_Type.__name__ = "Integer32"
_SlcSystemSiteRackCluster_Object = MibScalar
slcSystemSiteRackCluster = _SlcSystemSiteRackCluster_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 17),
    _SlcSystemSiteRackCluster_Type()
)
slcSystemSiteRackCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemSiteRackCluster.setStatus("current")


class _SlcSystemSiteRack_Type(Integer32):
    """Custom type slcSystemSiteRack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SlcSystemSiteRack_Type.__name__ = "Integer32"
_SlcSystemSiteRack_Object = MibScalar
slcSystemSiteRack = _SlcSystemSiteRack_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 18),
    _SlcSystemSiteRack_Type()
)
slcSystemSiteRack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemSiteRack.setStatus("current")
_SlcSystemLCDScreens_Type = OctetString
_SlcSystemLCDScreens_Object = MibScalar
slcSystemLCDScreens = _SlcSystemLCDScreens_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 19),
    _SlcSystemLCDScreens_Type()
)
slcSystemLCDScreens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDScreens.setStatus("current")
_SlcSystemLCDUserStrLine1_Type = OctetString
_SlcSystemLCDUserStrLine1_Object = MibScalar
slcSystemLCDUserStrLine1 = _SlcSystemLCDUserStrLine1_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 20),
    _SlcSystemLCDUserStrLine1_Type()
)
slcSystemLCDUserStrLine1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDUserStrLine1.setStatus("current")
_SlcSystemLCDUserStrLine2_Type = OctetString
_SlcSystemLCDUserStrLine2_Object = MibScalar
slcSystemLCDUserStrLine2 = _SlcSystemLCDUserStrLine2_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 21),
    _SlcSystemLCDUserStrLine2_Type()
)
slcSystemLCDUserStrLine2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDUserStrLine2.setStatus("current")
_SlcSystemLCDScrolling_Type = EnabledState
_SlcSystemLCDScrolling_Object = MibScalar
slcSystemLCDScrolling = _SlcSystemLCDScrolling_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 22),
    _SlcSystemLCDScrolling_Type()
)
slcSystemLCDScrolling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDScrolling.setStatus("current")


class _SlcSystemLCDScrollDelay_Type(Integer32):
    """Custom type slcSystemLCDScrollDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SlcSystemLCDScrollDelay_Type.__name__ = "Integer32"
_SlcSystemLCDScrollDelay_Object = MibScalar
slcSystemLCDScrollDelay = _SlcSystemLCDScrollDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 23),
    _SlcSystemLCDScrollDelay_Type()
)
slcSystemLCDScrollDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDScrollDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemLCDScrollDelay.setUnits("seconds")


class _SlcSystemLCDIdleDelay_Type(Integer32):
    """Custom type slcSystemLCDIdleDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_SlcSystemLCDIdleDelay_Type.__name__ = "Integer32"
_SlcSystemLCDIdleDelay_Object = MibScalar
slcSystemLCDIdleDelay = _SlcSystemLCDIdleDelay_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 24),
    _SlcSystemLCDIdleDelay_Type()
)
slcSystemLCDIdleDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemLCDIdleDelay.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemLCDIdleDelay.setUnits("seconds")
_SlcSystemInternalTemp_Type = Integer32
_SlcSystemInternalTemp_Object = MibScalar
slcSystemInternalTemp = _SlcSystemInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 25),
    _SlcSystemInternalTemp_Type()
)
slcSystemInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemInternalTemp.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemInternalTemp.setUnits("Celsius")


class _SlcSystemWebProtocol_Type(Integer32):
    """Custom type slcSystemWebProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tlsv1SSLv3", 1),
          ("tlsv1SSLv3SSLv2", 2))
    )


_SlcSystemWebProtocol_Type.__name__ = "Integer32"
_SlcSystemWebProtocol_Object = MibScalar
slcSystemWebProtocol = _SlcSystemWebProtocol_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 26),
    _SlcSystemWebProtocol_Type()
)
slcSystemWebProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebProtocol.setStatus("current")


class _SlcSystemWebCipher_Type(Integer32):
    """Custom type slcSystemWebCipher based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("highMedium", 1),
          ("highMediumLow", 2))
    )


_SlcSystemWebCipher_Type.__name__ = "Integer32"
_SlcSystemWebCipher_Object = MibScalar
slcSystemWebCipher = _SlcSystemWebCipher_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 27),
    _SlcSystemWebCipher_Type()
)
slcSystemWebCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebCipher.setStatus("current")
_SlcSystemModelString_Type = OctetString
_SlcSystemModelString_Object = MibScalar
slcSystemModelString = _SlcSystemModelString_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 28),
    _SlcSystemModelString_Type()
)
slcSystemModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemModelString.setStatus("current")
_SlcSystemWebGroup_Type = OctetString
_SlcSystemWebGroup_Object = MibScalar
slcSystemWebGroup = _SlcSystemWebGroup_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 29),
    _SlcSystemWebGroup_Type()
)
slcSystemWebGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebGroup.setStatus("current")
_SlcSystemWebInterface_Type = OctetString
_SlcSystemWebInterface_Object = MibScalar
slcSystemWebInterface = _SlcSystemWebInterface_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 30),
    _SlcSystemWebInterface_Type()
)
slcSystemWebInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebInterface.setStatus("current")
_SlcSystemWebBanner_Type = OctetString
_SlcSystemWebBanner_Object = MibScalar
slcSystemWebBanner = _SlcSystemWebBanner_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 31),
    _SlcSystemWebBanner_Type()
)
slcSystemWebBanner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebBanner.setStatus("current")
_SlcSystemInternalTempLow_Type = Integer32
_SlcSystemInternalTempLow_Object = MibScalar
slcSystemInternalTempLow = _SlcSystemInternalTempLow_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 32),
    _SlcSystemInternalTempLow_Type()
)
slcSystemInternalTempLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemInternalTempLow.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemInternalTempLow.setUnits("Celsius")
_SlcSystemInternalTempHigh_Type = Integer32
_SlcSystemInternalTempHigh_Object = MibScalar
slcSystemInternalTempHigh = _SlcSystemInternalTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 33),
    _SlcSystemInternalTempHigh_Type()
)
slcSystemInternalTempHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemInternalTempHigh.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemInternalTempHigh.setUnits("Celsius")
_SlcSystemCalibrateTemp_Type = Integer32
_SlcSystemCalibrateTemp_Object = MibScalar
slcSystemCalibrateTemp = _SlcSystemCalibrateTemp_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 34),
    _SlcSystemCalibrateTemp_Type()
)
slcSystemCalibrateTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemCalibrateTemp.setStatus("current")
if mibBuilder.loadTexts:
    slcSystemCalibrateTemp.setUnits("Celsius")
_SlcSystemWebServer_Type = EnabledState
_SlcSystemWebServer_Object = MibScalar
slcSystemWebServer = _SlcSystemWebServer_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 6, 35),
    _SlcSystemWebServer_Type()
)
slcSystemWebServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSystemWebServer.setStatus("current")
_SlcEventObjects_ObjectIdentity = ObjectIdentity
slcEventObjects = _SlcEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7)
)


class _SlcPowerSupplyId_Type(Integer32):
    """Custom type slcPowerSupplyId based on Integer32"""
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
        *(("powerSupplyA", 1),
          ("powerSupplyB", 2),
          ("primaryInlet", 3),
          ("secondaryInlet", 4))
    )


_SlcPowerSupplyId_Type.__name__ = "Integer32"
_SlcPowerSupplyId_Object = MibScalar
slcPowerSupplyId = _SlcPowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 1),
    _SlcPowerSupplyId_Type()
)
slcPowerSupplyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPowerSupplyId.setStatus("current")


class _SlcPowerSupplyAction_Type(Integer32):
    """Custom type slcPowerSupplyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerSupplyFailed", 1),
          ("powerSupplyRestored", 2))
    )


_SlcPowerSupplyAction_Type.__name__ = "Integer32"
_SlcPowerSupplyAction_Object = MibScalar
slcPowerSupplyAction = _SlcPowerSupplyAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 2),
    _SlcPowerSupplyAction_Type()
)
slcPowerSupplyAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPowerSupplyAction.setStatus("current")
_SlcDevPortNumBytes_Type = Integer32
_SlcDevPortNumBytes_Object = MibScalar
slcDevPortNumBytes = _SlcDevPortNumBytes_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 3),
    _SlcDevPortNumBytes_Type()
)
slcDevPortNumBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortNumBytes.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortNumBytes.setUnits("bytes")
_SlcDevPortData_Type = OctetString
_SlcDevPortData_Object = MibScalar
slcDevPortData = _SlcDevPortData_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 4),
    _SlcDevPortData_Type()
)
slcDevPortData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortData.setStatus("current")
_SlcDevPortStartByte_Type = Integer32
_SlcDevPortStartByte_Object = MibScalar
slcDevPortStartByte = _SlcDevPortStartByte_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 5),
    _SlcDevPortStartByte_Type()
)
slcDevPortStartByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortStartByte.setStatus("current")
_SlcDevPortTimeFrame_Type = Integer32
_SlcDevPortTimeFrame_Object = MibScalar
slcDevPortTimeFrame = _SlcDevPortTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 6),
    _SlcDevPortTimeFrame_Type()
)
slcDevPortTimeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortTimeFrame.setStatus("current")
if mibBuilder.loadTexts:
    slcDevPortTimeFrame.setUnits("seconds")


class _SlcDevPortDeviceErrorStatus_Type(Integer32):
    """Custom type slcDevPortDeviceErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("damageOrTamper", 2),
          ("lowPower", 1))
    )


_SlcDevPortDeviceErrorStatus_Type.__name__ = "Integer32"
_SlcDevPortDeviceErrorStatus_Object = MibScalar
slcDevPortDeviceErrorStatus = _SlcDevPortDeviceErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 7),
    _SlcDevPortDeviceErrorStatus_Type()
)
slcDevPortDeviceErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortDeviceErrorStatus.setStatus("current")
_SlcHostname_Type = OctetString
_SlcHostname_Object = MibScalar
slcHostname = _SlcHostname_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 8),
    _SlcHostname_Type()
)
slcHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcHostname.setStatus("current")


class _SlcPCCardSlot_Type(Integer32):
    """Custom type slcPCCardSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lowerSlot", 2),
          ("upperSlot", 1))
    )


_SlcPCCardSlot_Type.__name__ = "Integer32"
_SlcPCCardSlot_Object = MibScalar
slcPCCardSlot = _SlcPCCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 9),
    _SlcPCCardSlot_Type()
)
slcPCCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardSlot.setStatus("current")


class _SlcPCCardAction_Type(Integer32):
    """Custom type slcPCCardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cardInserted", 1),
          ("cardRemoved", 2))
    )


_SlcPCCardAction_Type.__name__ = "Integer32"
_SlcPCCardAction_Object = MibScalar
slcPCCardAction = _SlcPCCardAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 10),
    _SlcPCCardAction_Type()
)
slcPCCardAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardAction.setStatus("current")


class _SlcPCCardType_Type(Integer32):
    """Custom type slcPCCardType based on Integer32"""
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
        *(("gsmmodem", 6),
          ("isdn", 4),
          ("modem", 3),
          ("none", 1),
          ("storage", 2),
          ("wireless", 5))
    )


_SlcPCCardType_Type.__name__ = "Integer32"
_SlcPCCardType_Object = MibScalar
slcPCCardType = _SlcPCCardType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 11),
    _SlcPCCardType_Type()
)
slcPCCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcPCCardType.setStatus("current")


class _SlcUSBAction_Type(Integer32):
    """Custom type slcUSBAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deviceInserted", 1),
          ("deviceRemoved", 2),
          ("noModemDialTone", 3))
    )


_SlcUSBAction_Type.__name__ = "Integer32"
_SlcUSBAction_Object = MibScalar
slcUSBAction = _SlcUSBAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 12),
    _SlcUSBAction_Type()
)
slcUSBAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcUSBAction.setStatus("current")


class _SlcUSBType_Type(Integer32):
    """Custom type slcUSBType based on Integer32"""
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
        *(("gsmmodem", 6),
          ("isdn", 4),
          ("modem", 3),
          ("none", 1),
          ("storage", 2),
          ("wireless", 5))
    )


_SlcUSBType_Type.__name__ = "Integer32"
_SlcUSBType_Object = MibScalar
slcUSBType = _SlcUSBType_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 13),
    _SlcUSBType_Type()
)
slcUSBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcUSBType.setStatus("current")


class _SlcDevPortErrorStatus_Type(Integer32):
    """Custom type slcDevPortErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataDrop", 1),
          ("errorIOModules", 3),
          ("invalidIOConfiguration", 2))
    )


_SlcDevPortErrorStatus_Type.__name__ = "Integer32"
_SlcDevPortErrorStatus_Object = MibScalar
slcDevPortErrorStatus = _SlcDevPortErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 14),
    _SlcDevPortErrorStatus_Type()
)
slcDevPortErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcDevPortErrorStatus.setStatus("current")


class _SlcSDCardAction_Type(Integer32):
    """Custom type slcSDCardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceInserted", 1),
          ("deviceRemoved", 2))
    )


_SlcSDCardAction_Type.__name__ = "Integer32"
_SlcSDCardAction_Object = MibScalar
slcSDCardAction = _SlcSDCardAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 15),
    _SlcSDCardAction_Type()
)
slcSDCardAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcSDCardAction.setStatus("current")
_SlcRPMAction_Type = OctetString
_SlcRPMAction_Object = MibScalar
slcRPMAction = _SlcRPMAction_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 16),
    _SlcRPMAction_Type()
)
slcRPMAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcRPMAction.setStatus("current")
_SlcEventHost_Type = OctetString
_SlcEventHost_Object = MibScalar
slcEventHost = _SlcEventHost_Object(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 7, 17),
    _SlcEventHost_Type()
)
slcEventHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slcEventHost.setStatus("current")

# Managed Objects groups


# Notification objects

slcEventPowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 1)
)
slcEventPowerSupply.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcPowerSupplyId"),
        ("LANTRONIX-SLC-MIB", "slcPowerSupplyAction"))
)
if mibBuilder.loadTexts:
    slcEventPowerSupply.setStatus(
        "current"
    )

slcEventSysadminPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 2)
)
if mibBuilder.loadTexts:
    slcEventSysadminPassword.setStatus(
        "current"
    )

slcEventSLCShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 3)
)
if mibBuilder.loadTexts:
    slcEventSLCShutdown.setStatus(
        "current"
    )

slcEventDevicePortData = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 4)
)
slcEventDevicePortData.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortNumBytes"),
        ("LANTRONIX-SLC-MIB", "slcDevPortData"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgEmailTextString"),
        ("LANTRONIX-SLC-MIB", "slcHostname"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortData.setStatus(
        "current"
    )

slcEventDevicePortSLMData = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 5)
)
slcEventDevicePortSLMData.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortNumBytes"),
        ("LANTRONIX-SLC-MIB", "slcDevPortStartByte"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortSLMData.setStatus(
        "current"
    )

slcEventDevicePortSLMConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 6)
)
slcEventDevicePortSLMConfig.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortNumBytes"),
        ("LANTRONIX-SLC-MIB", "slcDevPortTimeFrame"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortSLMConfig.setStatus(
        "current"
    )

slcEventDevicePortDeviceLowTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 7)
)
slcEventDevicePortDeviceLowTemp.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevTemperature"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevLowTemp"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortDeviceLowTemp.setStatus(
        "current"
    )

slcEventDevicePortDeviceHighTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 8)
)
slcEventDevicePortDeviceHighTemp.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevTemperature"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevHighTemp"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortDeviceHighTemp.setStatus(
        "current"
    )

slcEventDevicePortDeviceLowHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 9)
)
slcEventDevicePortDeviceLowHumidity.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevHumidity"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevLowHumidity"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortDeviceLowHumidity.setStatus(
        "current"
    )

slcEventDevicePortDeviceHighHumidity = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 10)
)
slcEventDevicePortDeviceHighHumidity.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevHumidity"),
        ("LANTRONIX-SLC-MIB", "slcDevPortCfgDevHighHumidity"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortDeviceHighHumidity.setStatus(
        "current"
    )

slcEventDevicePortDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 11)
)
slcEventDevicePortDeviceError.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortDeviceErrorStatus"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortDeviceError.setStatus(
        "current"
    )

slcEventPCCardAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 12)
)
slcEventPCCardAction.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcPCCardSlot"),
        ("LANTRONIX-SLC-MIB", "slcPCCardAction"),
        ("LANTRONIX-SLC-MIB", "slcPCCardType"))
)
if mibBuilder.loadTexts:
    slcEventPCCardAction.setStatus(
        "current"
    )

slcEventSLCInternalTemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 13)
)
slcEventSLCInternalTemp.setObjects(
    ("LANTRONIX-SLC-MIB", "slcSystemInternalTemp")
)
if mibBuilder.loadTexts:
    slcEventSLCInternalTemp.setStatus(
        "current"
    )

slcEventUSBAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 14)
)
slcEventUSBAction.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevUSBId"),
        ("LANTRONIX-SLC-MIB", "slcUSBAction"),
        ("LANTRONIX-SLC-MIB", "slcUSBType"))
)
if mibBuilder.loadTexts:
    slcEventUSBAction.setStatus(
        "current"
    )

slcEventDevicePortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 15)
)
slcEventDevicePortError.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevPortId"),
        ("LANTRONIX-SLC-MIB", "slcDevPortErrorStatus"))
)
if mibBuilder.loadTexts:
    slcEventDevicePortError.setStatus(
        "current"
    )

slcEventSDCardAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 16)
)
slcEventSDCardAction.setObjects(
    ("LANTRONIX-SLC-MIB", "slcSDCardAction")
)
if mibBuilder.loadTexts:
    slcEventSDCardAction.setStatus(
        "current"
    )

slcEventNoDialToneAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 17)
)
if mibBuilder.loadTexts:
    slcEventNoDialToneAlarm.setStatus(
        "current"
    )

slcEventRPMAction = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 18)
)
slcEventRPMAction.setObjects(
      *(("LANTRONIX-SLC-MIB", "slcDevRPMName"),
        ("LANTRONIX-SLC-MIB", "slcRPMAction"))
)
if mibBuilder.loadTexts:
    slcEventRPMAction.setStatus(
        "current"
    )

slcEventPingHostFails = NotificationType(
    (1, 3, 6, 1, 4, 1, 244, 1, 1, 0, 19)
)
slcEventPingHostFails.setObjects(
    ("LANTRONIX-SLC-MIB", "slcEventHost")
)
if mibBuilder.loadTexts:
    slcEventPingHostFails.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANTRONIX-SLC-MIB",
    **{"EnabledState": EnabledState,
       "AuthOrder": AuthOrder,
       "SyslogLevel": SyslogLevel,
       "UserGroup": UserGroup,
       "UserRights": UserRights,
       "TimeoutDataDirection": TimeoutDataDirection,
       "RPMTowerIndex": RPMTowerIndex,
       "RPMOutletIndex": RPMOutletIndex,
       "slc": slc,
       "slcEvents": slcEvents,
       "slcEventPowerSupply": slcEventPowerSupply,
       "slcEventSysadminPassword": slcEventSysadminPassword,
       "slcEventSLCShutdown": slcEventSLCShutdown,
       "slcEventDevicePortData": slcEventDevicePortData,
       "slcEventDevicePortSLMData": slcEventDevicePortSLMData,
       "slcEventDevicePortSLMConfig": slcEventDevicePortSLMConfig,
       "slcEventDevicePortDeviceLowTemp": slcEventDevicePortDeviceLowTemp,
       "slcEventDevicePortDeviceHighTemp": slcEventDevicePortDeviceHighTemp,
       "slcEventDevicePortDeviceLowHumidity": slcEventDevicePortDeviceLowHumidity,
       "slcEventDevicePortDeviceHighHumidity": slcEventDevicePortDeviceHighHumidity,
       "slcEventDevicePortDeviceError": slcEventDevicePortDeviceError,
       "slcEventPCCardAction": slcEventPCCardAction,
       "slcEventSLCInternalTemp": slcEventSLCInternalTemp,
       "slcEventUSBAction": slcEventUSBAction,
       "slcEventDevicePortError": slcEventDevicePortError,
       "slcEventSDCardAction": slcEventSDCardAction,
       "slcEventNoDialToneAlarm": slcEventNoDialToneAlarm,
       "slcEventRPMAction": slcEventRPMAction,
       "slcEventPingHostFails": slcEventPingHostFails,
       "slcNetwork": slcNetwork,
       "slcNetEth": slcNetEth,
       "slcNetEthIfNumber": slcNetEthIfNumber,
       "slcNetEthIfTable": slcNetEthIfTable,
       "slcNetEthIfEntry": slcNetEthIfEntry,
       "slcNetEthIfIndex": slcNetEthIfIndex,
       "slcNetEthIfSource": slcNetEthIfSource,
       "slcNetEthIfMode": slcNetEthIfMode,
       "slcNetEthIfIPv6Addr": slcNetEthIfIPv6Addr,
       "slcNetEthIfIPv6PrefixLength": slcNetEthIfIPv6PrefixLength,
       "slcNetEthIfMTU": slcNetEthIfMTU,
       "slcNetEthIfMacAddress": slcNetEthIfMacAddress,
       "slcNetEthGateway": slcNetEthGateway,
       "slcNetEthGatewayPrecedence": slcNetEthGatewayPrecedence,
       "slcNetEthKeepaliveStartProbes": slcNetEthKeepaliveStartProbes,
       "slcNetEthKeepaliveNumberOfProbes": slcNetEthKeepaliveNumberOfProbes,
       "slcNetEthKeepaliveInterval": slcNetEthKeepaliveInterval,
       "slcNetEthIPForwarding": slcNetEthIPForwarding,
       "slcNetEthDNS1": slcNetEthDNS1,
       "slcNetEthDNS2": slcNetEthDNS2,
       "slcNetEthDNS3": slcNetEthDNS3,
       "slcNetEthDomain": slcNetEthDomain,
       "slcNetEthAlternateGateway": slcNetEthAlternateGateway,
       "slcNetEthPingIPAddress": slcNetEthPingIPAddress,
       "slcNetEthPingInterface": slcNetEthPingInterface,
       "slcNetEthPingDelay": slcNetEthPingDelay,
       "slcNetEthPingFailed": slcNetEthPingFailed,
       "slcNetEthBonding": slcNetEthBonding,
       "slcNetEthIPv6": slcNetEthIPv6,
       "slcNetEthGatewayIPv6": slcNetEthGatewayIPv6,
       "slcNetEthDNS1IPv6": slcNetEthDNS1IPv6,
       "slcNetEthDNS2IPv6": slcNetEthDNS2IPv6,
       "slcNetEthDNS3IPv6": slcNetEthDNS3IPv6,
       "slcNetEthPreferIPv4DNS": slcNetEthPreferIPv4DNS,
       "slcNetFirewall": slcNetFirewall,
       "slcNetFirewallState": slcNetFirewallState,
       "slcNetFirewallReject": slcNetFirewallReject,
       "slcNetFirewallPing": slcNetFirewallPing,
       "slcNetFirewallSSH": slcNetFirewallSSH,
       "slcNetFirewallTelnet": slcNetFirewallTelnet,
       "slcNetFirewallHTTP": slcNetFirewallHTTP,
       "slcNetFirewallHTTPS": slcNetFirewallHTTPS,
       "slcNetFirewallSMBCIFS": slcNetFirewallSMBCIFS,
       "slcNetFirewallRulesetNumber": slcNetFirewallRulesetNumber,
       "slcNetFirewallRulesetTable": slcNetFirewallRulesetTable,
       "slcNetFirewallRulesetEntry": slcNetFirewallRulesetEntry,
       "slcNetFirewallRulesetIndex": slcNetFirewallRulesetIndex,
       "slcNetFirewallRulesetName": slcNetFirewallRulesetName,
       "slcNetFirewallRulesetNumRules": slcNetFirewallRulesetNumRules,
       "slcNetFirewallRulesetRules": slcNetFirewallRulesetRules,
       "slcNetFirewallMappingNumber": slcNetFirewallMappingNumber,
       "slcNetFirewallMappingTable": slcNetFirewallMappingTable,
       "slcNetFirewallMappingEntry": slcNetFirewallMappingEntry,
       "slcNetFirewallMappingIndex": slcNetFirewallMappingIndex,
       "slcNetFirewallMappingIfac": slcNetFirewallMappingIfac,
       "slcNetFirewallMappingIfacId": slcNetFirewallMappingIfacId,
       "slcNetFirewallMappingRuleset": slcNetFirewallMappingRuleset,
       "slcNetRouting": slcNetRouting,
       "slcNetRouteRIPState": slcNetRouteRIPState,
       "slcNetRouteRIPVersion": slcNetRouteRIPVersion,
       "slcNetRouteStaticState": slcNetRouteStaticState,
       "slcNetRouteStaticNumber": slcNetRouteStaticNumber,
       "slcNetRouteStaticTable": slcNetRouteStaticTable,
       "slcNetRouteStaticEntry": slcNetRouteStaticEntry,
       "slcNetRouteStaticIndex": slcNetRouteStaticIndex,
       "slcNetRouteStaticIP": slcNetRouteStaticIP,
       "slcNetRouteStaticMask": slcNetRouteStaticMask,
       "slcNetRouteStaticGateway": slcNetRouteStaticGateway,
       "slcNetVPN": slcNetVPN,
       "slcNetVPNTunnel": slcNetVPNTunnel,
       "slcNetVPNStatus": slcNetVPNStatus,
       "slcNetVPNName": slcNetVPNName,
       "slcNetVPNEthPort": slcNetVPNEthPort,
       "slcNetVPNRemoteHost": slcNetVPNRemoteHost,
       "slcNetVPNRemoteId": slcNetVPNRemoteId,
       "slcNetVPNRemoteHop": slcNetVPNRemoteHop,
       "slcNetVPNRemoteSubnet": slcNetVPNRemoteSubnet,
       "slcNetVPNLocalId": slcNetVPNLocalId,
       "slcNetVPNLocalHop": slcNetVPNLocalHop,
       "slcNetVPNLocalSubnet": slcNetVPNLocalSubnet,
       "slcNetVPNIKENegotiation": slcNetVPNIKENegotiation,
       "slcNetVPNIKEEncryption": slcNetVPNIKEEncryption,
       "slcNetVPNIKEAuthentication": slcNetVPNIKEAuthentication,
       "slcNetVPNIKEDHGroup": slcNetVPNIKEDHGroup,
       "slcNetVPNESPEncryption": slcNetVPNESPEncryption,
       "slcNetVPNESPAuthentication": slcNetVPNESPAuthentication,
       "slcNetVPNESPDHGroup": slcNetVPNESPDHGroup,
       "slcNetVPNAuthentication": slcNetVPNAuthentication,
       "slcNetVPNPerfectForwardSecrecy": slcNetVPNPerfectForwardSecrecy,
       "slcNetVPNModeConfigClient": slcNetVPNModeConfigClient,
       "slcNetVPNXAUTHClient": slcNetVPNXAUTHClient,
       "slcNetVPNXAUTHClientLogin": slcNetVPNXAUTHClientLogin,
       "slcNetSecurity": slcNetSecurity,
       "slcNetSecurityFIPSMode": slcNetSecurityFIPSMode,
       "slcServices": slcServices,
       "slcServNTP": slcServNTP,
       "slcServNTPState": slcServNTPState,
       "slcServNTPSynchronize": slcServNTPSynchronize,
       "slcServNTPPoll": slcServNTPPoll,
       "slcServNTPServer": slcServNTPServer,
       "slcServNTPLocalServer2": slcServNTPLocalServer2,
       "slcServNTPLocalServer3": slcServNTPLocalServer3,
       "slcServNTPServerIPv6": slcServNTPServerIPv6,
       "slcServNTPLocalServer2IPv6": slcServNTPLocalServer2IPv6,
       "slcServNTPLocalServer3IPv6": slcServNTPLocalServer3IPv6,
       "slcServSyslog": slcServSyslog,
       "slcServSysNetworkLevel": slcServSysNetworkLevel,
       "slcServSysServicesLevel": slcServSysServicesLevel,
       "slcServSysAuthLevel": slcServSysAuthLevel,
       "slcServSysDevPortLevel": slcServSysDevPortLevel,
       "slcServSysDiagLevel": slcServSysDiagLevel,
       "slcServSysGeneralLevel": slcServSysGeneralLevel,
       "slcServSysRemoteServer": slcServSysRemoteServer,
       "slcServSysRemoteServer2": slcServSysRemoteServer2,
       "slcServSysRemoteServerIPv6": slcServSysRemoteServerIPv6,
       "slcServSysRemoteServer2IPv6": slcServSysRemoteServer2IPv6,
       "slcServSysRPMLogSize": slcServSysRPMLogSize,
       "slcServSysOtherLogSize": slcServSysOtherLogSize,
       "slcServAuditLog": slcServAuditLog,
       "slcServAuditState": slcServAuditState,
       "slcServAuditSize": slcServAuditSize,
       "slcServAuditIncludeCLI": slcServAuditIncludeCLI,
       "slcServAuditInSystemLog": slcServAuditInSystemLog,
       "slcServSSH": slcServSSH,
       "slcServSSHState": slcServSSHState,
       "slcServSSHTimeout": slcServSSHTimeout,
       "slcServSSHWebSSH": slcServSSHWebSSH,
       "slcServSSHPort": slcServSSHPort,
       "slcServSSHV1Incoming": slcServSSHV1Incoming,
       "slcServSSHTimeoutDataDirection": slcServSSHTimeoutDataDirection,
       "slcServSSHDSAKeys": slcServSSHDSAKeys,
       "slcServTelnet": slcServTelnet,
       "slcServTelnetState": slcServTelnetState,
       "slcServTelnetTimeout": slcServTelnetTimeout,
       "slcServTelnetWebTelnet": slcServTelnetWebTelnet,
       "slcServTelnetTelnetOut": slcServTelnetTelnetOut,
       "slcServTelnetTimeoutDataDirection": slcServTelnetTimeoutDataDirection,
       "slcServSNMP": slcServSNMP,
       "slcServSNMPState": slcServSNMPState,
       "slcServSNMPTraps": slcServSNMPTraps,
       "slcServSNMPNMS": slcServSNMPNMS,
       "slcServSNMPLocation": slcServSNMPLocation,
       "slcServSNMPContact": slcServSNMPContact,
       "slcServSNMPv3User": slcServSNMPv3User,
       "slcServSNMPReadOnlyCommunity": slcServSNMPReadOnlyCommunity,
       "slcServSNMPReadWriteCommunity": slcServSNMPReadWriteCommunity,
       "slcServSNMPTrapCommunity": slcServSNMPTrapCommunity,
       "slcServSNMPAlarmDelay": slcServSNMPAlarmDelay,
       "slcServSNMPv3ReadWriteUser": slcServSNMPv3ReadWriteUser,
       "slcServSNMPv3Security": slcServSNMPv3Security,
       "slcServSNMPv3Authentication": slcServSNMPv3Authentication,
       "slcServSNMPv3Encryption": slcServSNMPv3Encryption,
       "slcServSNMPv1v2": slcServSNMPv1v2,
       "slcServSNMPNMS2": slcServSNMPNMS2,
       "slcServSNMPNMSIPv6": slcServSNMPNMSIPv6,
       "slcServSNMPNMS2IPv6": slcServSNMPNMS2IPv6,
       "slcServSMTP": slcServSMTP,
       "slcServSMTPServer": slcServSMTPServer,
       "slcServSMTPSender": slcServSMTPSender,
       "slcServNFS": slcServNFS,
       "slcServNFSMountTable": slcServNFSMountTable,
       "slcServNFSMountEntry": slcServNFSMountEntry,
       "slcServNFSMountIndex": slcServNFSMountIndex,
       "slcServNFSMountRemoteDir": slcServNFSMountRemoteDir,
       "slcServNFSMountLocalDir": slcServNFSMountLocalDir,
       "slcServNFSMountReadWrite": slcServNFSMountReadWrite,
       "slcServNFSMountMount": slcServNFSMountMount,
       "slcServCIFS": slcServCIFS,
       "slcServCIFSState": slcServCIFSState,
       "slcServCIFSEth1": slcServCIFSEth1,
       "slcServCIFSEth2": slcServCIFSEth2,
       "slcServCIFSWorkgroup": slcServCIFSWorkgroup,
       "slcServSLCNetwork": slcServSLCNetwork,
       "slcServSLCNetSearch": slcServSLCNetSearch,
       "slcServSLCNetNumber": slcServSLCNetNumber,
       "slcServSLCNetTable": slcServSLCNetTable,
       "slcServSLCNetEntry": slcServSLCNetEntry,
       "slcServSLCNetIndex": slcServSLCNetIndex,
       "slcServSLCNetIP": slcServSLCNetIP,
       "slcServPhoneHome": slcServPhoneHome,
       "slcServPhoneHomeState": slcServPhoneHomeState,
       "slcServPhoneHomeIP": slcServPhoneHomeIP,
       "slcServHostList": slcServHostList,
       "slcServHostListNumber": slcServHostListNumber,
       "slcServHostListTable": slcServHostListTable,
       "slcServHostListEntry": slcServHostListEntry,
       "slcServHostListIndex": slcServHostListIndex,
       "slcServHostListName": slcServHostListName,
       "slcServHostListRetryCount": slcServHostListRetryCount,
       "slcServHostListAuth": slcServHostListAuth,
       "slcServHostListNumHosts": slcServHostListNumHosts,
       "slcServHostListHosts": slcServHostListHosts,
       "slcServWebTerm": slcServWebTerm,
       "slcServWebTermDeployment": slcServWebTermDeployment,
       "slcServWebTermBufSize": slcServWebTermBufSize,
       "slcServSite": slcServSite,
       "slcServSiteNumber": slcServSiteNumber,
       "slcServSiteTable": slcServSiteTable,
       "slcServSiteEntry": slcServSiteEntry,
       "slcServSiteIndex": slcServSiteIndex,
       "slcServSiteName": slcServSiteName,
       "slcServSitePort": slcServSitePort,
       "slcServSitePortId": slcServSitePortId,
       "slcServSiteLoginHost": slcServSiteLoginHost,
       "slcServSiteCHAPSecret": slcServSiteCHAPSecret,
       "slcServSiteTimeout": slcServSiteTimeout,
       "slcServSiteLocalIP": slcServSiteLocalIP,
       "slcServSiteRemoteIP": slcServSiteRemoteIP,
       "slcServSiteStaticRouteIP": slcServSiteStaticRouteIP,
       "slcServSiteStaticRouteMask": slcServSiteStaticRouteMask,
       "slcServSiteStaticRouteGateway": slcServSiteStaticRouteGateway,
       "slcServSiteDialoutNum": slcServSiteDialoutNum,
       "slcServSiteDialoutLogin": slcServSiteDialoutLogin,
       "slcServSiteDialback": slcServSiteDialback,
       "slcServSiteDialbackNum": slcServSiteDialbackNum,
       "slcServSiteDialbackDelay": slcServSiteDialbackDelay,
       "slcServSiteIdleTimeout": slcServSiteIdleTimeout,
       "slcServSiteRestartDelay": slcServSiteRestartDelay,
       "slcServSiteCBCPServerAllowNoCallback": slcServSiteCBCPServerAllowNoCallback,
       "slcServSiteNATState": slcServSiteNATState,
       "slcServSiteDialbackRetries": slcServSiteDialbackRetries,
       "slcAuth": slcAuth,
       "slcAuthLocal": slcAuthLocal,
       "slcAuthLocalNumber": slcAuthLocalNumber,
       "slcAuthLocalUsersTable": slcAuthLocalUsersTable,
       "slcAuthLocalUserEntry": slcAuthLocalUserEntry,
       "slcAuthLocalUserIndex": slcAuthLocalUserIndex,
       "slcAuthLocalUserLogin": slcAuthLocalUserLogin,
       "slcAuthLocalUserUID": slcAuthLocalUserUID,
       "slcAuthLocalUserListenPorts": slcAuthLocalUserListenPorts,
       "slcAuthLocalUserDataPorts": slcAuthLocalUserDataPorts,
       "slcAuthLocalUserClearPorts": slcAuthLocalUserClearPorts,
       "slcAuthLocalUserEscapeSeq": slcAuthLocalUserEscapeSeq,
       "slcAuthLocalUserBreakSeq": slcAuthLocalUserBreakSeq,
       "slcAuthLocalUserMenu": slcAuthLocalUserMenu,
       "slcAuthLocalUserDialback": slcAuthLocalUserDialback,
       "slcAuthLocalUserDialbackNum": slcAuthLocalUserDialbackNum,
       "slcAuthLocalUserGroup": slcAuthLocalUserGroup,
       "slcAuthLocalUserRights": slcAuthLocalUserRights,
       "slcAuthLocalUserPwdExpires": slcAuthLocalUserPwdExpires,
       "slcAuthLocalUserChangePwd": slcAuthLocalUserChangePwd,
       "slcAuthLocalUserChangePwdNextLogin": slcAuthLocalUserChangePwdNextLogin,
       "slcAuthLocalState": slcAuthLocalState,
       "slcAuthLocalOrder": slcAuthLocalOrder,
       "slcAuthLocalComplexPasswords": slcAuthLocalComplexPasswords,
       "slcAuthLocalUseNextMethod": slcAuthLocalUseNextMethod,
       "slcAuthLocalAllowReuse": slcAuthLocalAllowReuse,
       "slcAuthLocalReuseHistory": slcAuthLocalReuseHistory,
       "slcAuthLocalPasswordLifetime": slcAuthLocalPasswordLifetime,
       "slcAuthLocalWarningPeriod": slcAuthLocalWarningPeriod,
       "slcAuthLocalMaxLoginAttempts": slcAuthLocalMaxLoginAttempts,
       "slcAuthLocalLockoutPeriod": slcAuthLocalLockoutPeriod,
       "slcAuthLocalMultipleSysadminLogins": slcAuthLocalMultipleSysadminLogins,
       "slcAuthLocalSysadminConsoleOnly": slcAuthLocalSysadminConsoleOnly,
       "slcAuthNIS": slcAuthNIS,
       "slcAuthNISState": slcAuthNISState,
       "slcAuthNISOrder": slcAuthNISOrder,
       "slcAuthNISDomain": slcAuthNISDomain,
       "slcAuthNISBroadcast": slcAuthNISBroadcast,
       "slcAuthNISMaster": slcAuthNISMaster,
       "slcAuthNISSlave1": slcAuthNISSlave1,
       "slcAuthNISSlave2": slcAuthNISSlave2,
       "slcAuthNISSlave3": slcAuthNISSlave3,
       "slcAuthNISGroup": slcAuthNISGroup,
       "slcAuthNISRights": slcAuthNISRights,
       "slcAuthNISMenu": slcAuthNISMenu,
       "slcAuthNISListenPorts": slcAuthNISListenPorts,
       "slcAuthNISDataPorts": slcAuthNISDataPorts,
       "slcAuthNISClearPorts": slcAuthNISClearPorts,
       "slcAuthNISSlave4": slcAuthNISSlave4,
       "slcAuthNISSlave5": slcAuthNISSlave5,
       "slcAuthNISEscapeSeq": slcAuthNISEscapeSeq,
       "slcAuthNISBreakSeq": slcAuthNISBreakSeq,
       "slcAuthNISDialback": slcAuthNISDialback,
       "slcAuthNISDialbackNum": slcAuthNISDialbackNum,
       "slcAuthLDAP": slcAuthLDAP,
       "slcAuthLDAPState": slcAuthLDAPState,
       "slcAuthLDAPOrder": slcAuthLDAPOrder,
       "slcAuthLDAPServer": slcAuthLDAPServer,
       "slcAuthLDAPBase": slcAuthLDAPBase,
       "slcAuthLDAPBindName": slcAuthLDAPBindName,
       "slcAuthLDAPPort": slcAuthLDAPPort,
       "slcAuthLDAPADSupport": slcAuthLDAPADSupport,
       "slcAuthLDAPGroup": slcAuthLDAPGroup,
       "slcAuthLDAPRights": slcAuthLDAPRights,
       "slcAuthLDAPMenu": slcAuthLDAPMenu,
       "slcAuthLDAPListenPorts": slcAuthLDAPListenPorts,
       "slcAuthLDAPDataPorts": slcAuthLDAPDataPorts,
       "slcAuthLDAPClearPorts": slcAuthLDAPClearPorts,
       "slcAuthLDAPEncrypt": slcAuthLDAPEncrypt,
       "slcAuthLDAPEscapeSeq": slcAuthLDAPEscapeSeq,
       "slcAuthLDAPBreakSeq": slcAuthLDAPBreakSeq,
       "slcAuthLDAPBindWithLogin": slcAuthLDAPBindWithLogin,
       "slcAuthLDAPUseLDAPSchema": slcAuthLDAPUseLDAPSchema,
       "slcAuthLDAPDialback": slcAuthLDAPDialback,
       "slcAuthLDAPDialbackNum": slcAuthLDAPDialbackNum,
       "slcAuthLDAPUserFilter": slcAuthLDAPUserFilter,
       "slcAuthLDAPGroupFilter": slcAuthLDAPGroupFilter,
       "slcAuthLDAPGroupMembershipAttr": slcAuthLDAPGroupMembershipAttr,
       "slcAuthLDAPGroupMembershipDN": slcAuthLDAPGroupMembershipDN,
       "slcAuthLDAPServer2": slcAuthLDAPServer2,
       "slcAuthLDAPServerIPv6": slcAuthLDAPServerIPv6,
       "slcAuthLDAPServer2IPv6": slcAuthLDAPServer2IPv6,
       "slcAuthRADIUS": slcAuthRADIUS,
       "slcAuthRADIUSState": slcAuthRADIUSState,
       "slcAuthRADIUSOrder": slcAuthRADIUSOrder,
       "slcAuthRADIUSTimeout": slcAuthRADIUSTimeout,
       "slcAuthRADIUSServerTable": slcAuthRADIUSServerTable,
       "slcAuthRADIUSServerEntry": slcAuthRADIUSServerEntry,
       "slcAuthRADIUSServerIndex": slcAuthRADIUSServerIndex,
       "slcAuthRADIUSServer": slcAuthRADIUSServer,
       "slcAuthRADIUSPort": slcAuthRADIUSPort,
       "slcAuthRADIUSServerIPv6": slcAuthRADIUSServerIPv6,
       "slcAuthRADIUSGroup": slcAuthRADIUSGroup,
       "slcAuthRADIUSRights": slcAuthRADIUSRights,
       "slcAuthRADIUSMenu": slcAuthRADIUSMenu,
       "slcAuthRADIUSListenPorts": slcAuthRADIUSListenPorts,
       "slcAuthRADIUSDataPorts": slcAuthRADIUSDataPorts,
       "slcAuthRADIUSClearPorts": slcAuthRADIUSClearPorts,
       "slcAuthRADIUSEscapeSeq": slcAuthRADIUSEscapeSeq,
       "slcAuthRADIUSBreakSeq": slcAuthRADIUSBreakSeq,
       "slcAuthRADIUSDialback": slcAuthRADIUSDialback,
       "slcAuthRADIUSDialbackNum": slcAuthRADIUSDialbackNum,
       "slcAuthRADIUSUseVSA": slcAuthRADIUSUseVSA,
       "slcAuthKerberos": slcAuthKerberos,
       "slcAuthKerbState": slcAuthKerbState,
       "slcAuthKerbOrder": slcAuthKerbOrder,
       "slcAuthKerbRealm": slcAuthKerbRealm,
       "slcAuthKerbKDC": slcAuthKerbKDC,
       "slcAuthKerbKDCIP": slcAuthKerbKDCIP,
       "slcAuthKerbKDCPort": slcAuthKerbKDCPort,
       "slcAuthKerbUseLDAP": slcAuthKerbUseLDAP,
       "slcAuthKerbGroup": slcAuthKerbGroup,
       "slcAuthKerbRights": slcAuthKerbRights,
       "slcAuthKerbMenu": slcAuthKerbMenu,
       "slcAuthKerbListenPorts": slcAuthKerbListenPorts,
       "slcAuthKerbDataPorts": slcAuthKerbDataPorts,
       "slcAuthKerbClearPorts": slcAuthKerbClearPorts,
       "slcAuthKerbEscapeSeq": slcAuthKerbEscapeSeq,
       "slcAuthKerbBreakSeq": slcAuthKerbBreakSeq,
       "slcAuthKerbDialback": slcAuthKerbDialback,
       "slcAuthKerbDialbackNum": slcAuthKerbDialbackNum,
       "slcAuthKerbKDCIPv6": slcAuthKerbKDCIPv6,
       "slcAuthTACACS": slcAuthTACACS,
       "slcAuthTACACSState": slcAuthTACACSState,
       "slcAuthTACACSOrder": slcAuthTACACSOrder,
       "slcAuthTACACSServer": slcAuthTACACSServer,
       "slcAuthTACACSEncrypt": slcAuthTACACSEncrypt,
       "slcAuthTACACSGroup": slcAuthTACACSGroup,
       "slcAuthTACACSRights": slcAuthTACACSRights,
       "slcAuthTACACSMenu": slcAuthTACACSMenu,
       "slcAuthTACACSListenPorts": slcAuthTACACSListenPorts,
       "slcAuthTACACSDataPorts": slcAuthTACACSDataPorts,
       "slcAuthTACACSClearPorts": slcAuthTACACSClearPorts,
       "slcAuthTACACSServer2": slcAuthTACACSServer2,
       "slcAuthTACACSServer3": slcAuthTACACSServer3,
       "slcAuthTACACSEscapeSeq": slcAuthTACACSEscapeSeq,
       "slcAuthTACACSBreakSeq": slcAuthTACACSBreakSeq,
       "slcAuthTACACSDialback": slcAuthTACACSDialback,
       "slcAuthTACACSDialbackNum": slcAuthTACACSDialbackNum,
       "slcAuthTACACSAuthService": slcAuthTACACSAuthService,
       "slcAuthTACACSServerIPv6": slcAuthTACACSServerIPv6,
       "slcAuthTACACSServer2IPv6": slcAuthTACACSServer2IPv6,
       "slcAuthTACACSServer3IPv6": slcAuthTACACSServer3IPv6,
       "slcAuthRemote": slcAuthRemote,
       "slcAuthRemoteNumber": slcAuthRemoteNumber,
       "slcAuthRemoteUsersTable": slcAuthRemoteUsersTable,
       "slcAuthRemoteUserEntry": slcAuthRemoteUserEntry,
       "slcAuthRemoteUserIndex": slcAuthRemoteUserIndex,
       "slcAuthRemoteUserLogin": slcAuthRemoteUserLogin,
       "slcAuthRemoteUserGroup": slcAuthRemoteUserGroup,
       "slcAuthRemoteUserRights": slcAuthRemoteUserRights,
       "slcAuthRemoteUserListenPorts": slcAuthRemoteUserListenPorts,
       "slcAuthRemoteUserDataPorts": slcAuthRemoteUserDataPorts,
       "slcAuthRemoteUserClearPorts": slcAuthRemoteUserClearPorts,
       "slcAuthRemoteUserEscapeSeq": slcAuthRemoteUserEscapeSeq,
       "slcAuthRemoteUserBreakSeq": slcAuthRemoteUserBreakSeq,
       "slcAuthRemoteUserMenu": slcAuthRemoteUserMenu,
       "slcAuthRemoteUserLocked": slcAuthRemoteUserLocked,
       "slcAuthRemoteUserDialback": slcAuthRemoteUserDialback,
       "slcAuthRemoteUserDialbackNum": slcAuthRemoteUserDialbackNum,
       "slcAuthRemoteAuthListOnly": slcAuthRemoteAuthListOnly,
       "slcAuthGroups": slcAuthGroups,
       "slcAuthGroupsNumber": slcAuthGroupsNumber,
       "slcAuthGroupsTable": slcAuthGroupsTable,
       "slcAuthGroupEntry": slcAuthGroupEntry,
       "slcAuthGroupIndex": slcAuthGroupIndex,
       "slcAuthGroupName": slcAuthGroupName,
       "slcAuthGroupRights": slcAuthGroupRights,
       "slcAuthGroupListenPorts": slcAuthGroupListenPorts,
       "slcAuthGroupDataPorts": slcAuthGroupDataPorts,
       "slcAuthGroupClearPorts": slcAuthGroupClearPorts,
       "slcAuthGroupEscapeSeq": slcAuthGroupEscapeSeq,
       "slcAuthGroupBreakSeq": slcAuthGroupBreakSeq,
       "slcAuthGroupMenu": slcAuthGroupMenu,
       "slcAuthGroupDialback": slcAuthGroupDialback,
       "slcAuthGroupDialbackNum": slcAuthGroupDialbackNum,
       "slcDevices": slcDevices,
       "slcDevConsolePort": slcDevConsolePort,
       "slcDevConBaud": slcDevConBaud,
       "slcDevConDataBits": slcDevConDataBits,
       "slcDevConStopBits": slcDevConStopBits,
       "slcDevConParity": slcDevConParity,
       "slcDevConFlowControl": slcDevConFlowControl,
       "slcDevConTimeout": slcDevConTimeout,
       "slcDevConShowLines": slcDevConShowLines,
       "slcDevConNumberShowLines": slcDevConNumberShowLines,
       "slcDevConGroup": slcDevConGroup,
       "slcDevDevicePorts": slcDevDevicePorts,
       "slcDevPortGlobal": slcDevPortGlobal,
       "slcDevGlobalListenPorts": slcDevGlobalListenPorts,
       "slcDevGlobalDataPorts": slcDevGlobalDataPorts,
       "slcDevGlobalClearPorts": slcDevGlobalClearPorts,
       "slcDevGlobalStartTelnetPort": slcDevGlobalStartTelnetPort,
       "slcDevGlobalStartSSHPort": slcDevGlobalStartSSHPort,
       "slcDevGlobalStartTCPPort": slcDevGlobalStartTCPPort,
       "slcDevGlobalMaxDirect": slcDevGlobalMaxDirect,
       "slcDevPortConfig": slcDevPortConfig,
       "slcDevPortCfgNumber": slcDevPortCfgNumber,
       "slcDevPortCfgTable": slcDevPortCfgTable,
       "slcDevPortCfgEntry": slcDevPortCfgEntry,
       "slcDevPortId": slcDevPortId,
       "slcDevPortCfgName": slcDevPortCfgName,
       "slcDevPortCfgDevice": slcDevPortCfgDevice,
       "slcDevPortCfgDevLogin": slcDevPortCfgDevLogin,
       "slcDevPortCfgBreakSeq": slcDevPortCfgBreakSeq,
       "slcDevPortCfgTelnetState": slcDevPortCfgTelnetState,
       "slcDevPortCfgTelnetPort": slcDevPortCfgTelnetPort,
       "slcDevPortCfgTelnetAuth": slcDevPortCfgTelnetAuth,
       "slcDevPortCfgSSHState": slcDevPortCfgSSHState,
       "slcDevPortCfgSSHPort": slcDevPortCfgSSHPort,
       "slcDevPortCfgSSHAuth": slcDevPortCfgSSHAuth,
       "slcDevPortCfgTCPState": slcDevPortCfgTCPState,
       "slcDevPortCfgTCPPort": slcDevPortCfgTCPPort,
       "slcDevPortCfgTCPAuth": slcDevPortCfgTCPAuth,
       "slcDevPortCfgIP": slcDevPortCfgIP,
       "slcDevPortCfgBaud": slcDevPortCfgBaud,
       "slcDevPortCfgDataBits": slcDevPortCfgDataBits,
       "slcDevPortCfgStopBits": slcDevPortCfgStopBits,
       "slcDevPortCfgParity": slcDevPortCfgParity,
       "slcDevPortCfgFlowControl": slcDevPortCfgFlowControl,
       "slcDevPortCfgLogins": slcDevPortCfgLogins,
       "slcDevPortCfgConnectDSR": slcDevPortCfgConnectDSR,
       "slcDevPortCfgDisconnectDSR": slcDevPortCfgDisconnectDSR,
       "slcDevPortCfgModemState": slcDevPortCfgModemState,
       "slcDevPortCfgModemMode": slcDevPortCfgModemMode,
       "slcDevPortCfgLocalIP": slcDevPortCfgLocalIP,
       "slcDevPortCfgRemoteIP": slcDevPortCfgRemoteIP,
       "slcDevPortCfgAuth": slcDevPortCfgAuth,
       "slcDevPortCfgCHAPHost": slcDevPortCfgCHAPHost,
       "slcDevPortCfgInitScript": slcDevPortCfgInitScript,
       "slcDevPortCfgTimeout": slcDevPortCfgTimeout,
       "slcDevPortCfgDialoutNum": slcDevPortCfgDialoutNum,
       "slcDevPortCfgDialoutLogin": slcDevPortCfgDialoutLogin,
       "slcDevPortCfgDialbackMode": slcDevPortCfgDialbackMode,
       "slcDevPortCfgDialbackNum": slcDevPortCfgDialbackNum,
       "slcDevPortCfgNATState": slcDevPortCfgNATState,
       "slcDevPortCfgLocalState": slcDevPortCfgLocalState,
       "slcDevPortCfgNFSFileState": slcDevPortCfgNFSFileState,
       "slcDevPortCfgNFSDir": slcDevPortCfgNFSDir,
       "slcDevPortCfgNFSMaxFiles": slcDevPortCfgNFSMaxFiles,
       "slcDevPortCfgNFSMaxSize": slcDevPortCfgNFSMaxSize,
       "slcDevPortCfgEmailState": slcDevPortCfgEmailState,
       "slcDevPortCfgEmailTrigger": slcDevPortCfgEmailTrigger,
       "slcDevPortCfgEmailByteThresh": slcDevPortCfgEmailByteThresh,
       "slcDevPortCfgEmailDelay": slcDevPortCfgEmailDelay,
       "slcDevPortCfgEmailRestartDelay": slcDevPortCfgEmailRestartDelay,
       "slcDevPortCfgEmailTextString": slcDevPortCfgEmailTextString,
       "slcDevPortCfgEmailTo": slcDevPortCfgEmailTo,
       "slcDevPortCfgEmailSubject": slcDevPortCfgEmailSubject,
       "slcDevPortCfgPCCardState": slcDevPortCfgPCCardState,
       "slcDevPortCfgPCCardLogTo": slcDevPortCfgPCCardLogTo,
       "slcDevPortCfgPCCardMaxFiles": slcDevPortCfgPCCardMaxFiles,
       "slcDevPortCfgPCCardMaxSize": slcDevPortCfgPCCardMaxSize,
       "slcDevPortCfgAction": slcDevPortCfgAction,
       "slcDevPortCfgEmailSend": slcDevPortCfgEmailSend,
       "slcDevPortCfgBanner": slcDevPortCfgBanner,
       "slcDevPortCfgIdleTimeout": slcDevPortCfgIdleTimeout,
       "slcDevPortCfgRestartDelay": slcDevPortCfgRestartDelay,
       "slcDevPortCfgCallerIdLogging": slcDevPortCfgCallerIdLogging,
       "slcDevPortCfgCallerIdATCmd": slcDevPortCfgCallerIdATCmd,
       "slcDevPortCfgDODAuth": slcDevPortCfgDODAuth,
       "slcDevPortCfgDODCHAPHost": slcDevPortCfgDODCHAPHost,
       "slcDevPortCfgSLMLoggingState": slcDevPortCfgSLMLoggingState,
       "slcDevPortCfgSLMNMS": slcDevPortCfgSLMNMS,
       "slcDevPortCfgSLMByteThresh": slcDevPortCfgSLMByteThresh,
       "slcDevPortCfgSLMTimeFrame": slcDevPortCfgSLMTimeFrame,
       "slcDevPortCfgWebColumns": slcDevPortCfgWebColumns,
       "slcDevPortCfgWebRows": slcDevPortCfgWebRows,
       "slcDevPortCfgSyslogState": slcDevPortCfgSyslogState,
       "slcDevPortCfgHostList": slcDevPortCfgHostList,
       "slcDevPortCfgDevLowTemp": slcDevPortCfgDevLowTemp,
       "slcDevPortCfgDevHighTemp": slcDevPortCfgDevHighTemp,
       "slcDevPortCfgDevTemperature": slcDevPortCfgDevTemperature,
       "slcDevPortCfgDevLowHumidity": slcDevPortCfgDevLowHumidity,
       "slcDevPortCfgDevHighHumidity": slcDevPortCfgDevHighHumidity,
       "slcDevPortCfgDevHumidity": slcDevPortCfgDevHumidity,
       "slcDevPortCfgDevTraps": slcDevPortCfgDevTraps,
       "slcDevPortCfgShowLines": slcDevPortCfgShowLines,
       "slcDevPortCfgNumberShowLines": slcDevPortCfgNumberShowLines,
       "slcDevPortCfgViewPortLog": slcDevPortCfgViewPortLog,
       "slcDevPortCfgPortLogSeq": slcDevPortCfgPortLogSeq,
       "slcDevPortCfgMaxDirectConnects": slcDevPortCfgMaxDirectConnects,
       "slcDevPortCfgTelnetTimeout": slcDevPortCfgTelnetTimeout,
       "slcDevPortCfgSSHTimeout": slcDevPortCfgSSHTimeout,
       "slcDevPortCfgTCPTimeout": slcDevPortCfgTCPTimeout,
       "slcDevPortCfgCBCPClientType": slcDevPortCfgCBCPClientType,
       "slcDevPortCfgCBCPServerAllowNoCallback": slcDevPortCfgCBCPServerAllowNoCallback,
       "slcDevPortCfgDialbackDelay": slcDevPortCfgDialbackDelay,
       "slcDevPortCfgUSBState": slcDevPortCfgUSBState,
       "slcDevPortCfgUSBLogTo": slcDevPortCfgUSBLogTo,
       "slcDevPortCfgUSBMaxFiles": slcDevPortCfgUSBMaxFiles,
       "slcDevPortCfgUSBMaxSize": slcDevPortCfgUSBMaxSize,
       "slcDevPortCfgCHAPAuthLocalUsers": slcDevPortCfgCHAPAuthLocalUsers,
       "slcDevPortCfgUseSites": slcDevPortCfgUseSites,
       "slcDevPortCfgDialbackRetries": slcDevPortCfgDialbackRetries,
       "slcDevPortCfgGroup": slcDevPortCfgGroup,
       "slcDevPortCfgIPMask": slcDevPortCfgIPMask,
       "slcDevPortCfgDevPrompt": slcDevPortCfgDevPrompt,
       "slcDevPortCfgDevNumOutlets": slcDevPortCfgDevNumOutlets,
       "slcDevPortCfgDevNumExpOutlets": slcDevPortCfgDevNumExpOutlets,
       "slcDevPortCfgReversePinout": slcDevPortCfgReversePinout,
       "slcDevPortCfgUSBVBUS": slcDevPortCfgUSBVBUS,
       "slcDevPortCfgAssertDTR": slcDevPortCfgAssertDTR,
       "slcDevPortCfgPortType": slcDevPortCfgPortType,
       "slcDevPortCfgTelnetTimeoutDataDirection": slcDevPortCfgTelnetTimeoutDataDirection,
       "slcDevPortCfgSSHTimeoutDataDirection": slcDevPortCfgSSHTimeoutDataDirection,
       "slcDevPortCfgTCPTimeoutDataDirection": slcDevPortCfgTCPTimeoutDataDirection,
       "slcDevPortCfgIdleTimeoutMessage": slcDevPortCfgIdleTimeoutMessage,
       "slcDevPortCfgNumberOfSessionsMessage": slcDevPortCfgNumberOfSessionsMessage,
       "slcDevPortCfgMinimizeLatency": slcDevPortCfgMinimizeLatency,
       "slcDevPortCfgTelnetSoftIAC": slcDevPortCfgTelnetSoftIAC,
       "slcDevPortCfgSendTermString": slcDevPortCfgSendTermString,
       "slcDevPortCfgTerminationString": slcDevPortCfgTerminationString,
       "slcDevPortCfgPowerManagementSeq": slcDevPortCfgPowerManagementSeq,
       "slcDevPortCfgPowerSupplies": slcDevPortCfgPowerSupplies,
       "slcDevPortCfgToggleDTR": slcDevPortCfgToggleDTR,
       "slcDevPortCfgTokenAction": slcDevPortCfgTokenAction,
       "slcDevPortCfgTokenSendString": slcDevPortCfgTokenSendString,
       "slcDevPortCfgTokenPowerSupply": slcDevPortCfgTokenPowerSupply,
       "slcDevPortCfgTokenPowerAction": slcDevPortCfgTokenPowerAction,
       "slcDevPortState": slcDevPortState,
       "slcDevPortStateNumber": slcDevPortStateNumber,
       "slcDevPortStateTable": slcDevPortStateTable,
       "slcDevPortStateEntry": slcDevPortStateEntry,
       "slcDevPortStateIndex": slcDevPortStateIndex,
       "slcDevPortStateBytesInput": slcDevPortStateBytesInput,
       "slcDevPortStateBytesOutput": slcDevPortStateBytesOutput,
       "slcDevPortStateFramingErrors": slcDevPortStateFramingErrors,
       "slcDevPortStateParityErrors": slcDevPortStateParityErrors,
       "slcDevPortStateOverrunErrors": slcDevPortStateOverrunErrors,
       "slcDevPortStateFlowControlViolations": slcDevPortStateFlowControlViolations,
       "slcDevPortStateDSR": slcDevPortStateDSR,
       "slcDevPortStateDTR": slcDevPortStateDTR,
       "slcDevPortStateCTS": slcDevPortStateCTS,
       "slcDevPortStateRTS": slcDevPortStateRTS,
       "slcDevPortStateCD": slcDevPortStateCD,
       "slcDevPCCard": slcDevPCCard,
       "slcPCCardCfgTable": slcPCCardCfgTable,
       "slcPCCardCfgEntry": slcPCCardCfgEntry,
       "slcPCCardCfgIndex": slcPCCardCfgIndex,
       "slcPCCardCfgCardType": slcPCCardCfgCardType,
       "slcPCCardCfgCardId": slcPCCardCfgCardId,
       "slcPCCardCfgBaud": slcPCCardCfgBaud,
       "slcPCCardCfgDataBits": slcPCCardCfgDataBits,
       "slcPCCardCfgStopBits": slcPCCardCfgStopBits,
       "slcPCCardCfgParity": slcPCCardCfgParity,
       "slcPCCardCfgFlowControl": slcPCCardCfgFlowControl,
       "slcPCCardCfgModemState": slcPCCardCfgModemState,
       "slcPCCardCfgModemMode": slcPCCardCfgModemMode,
       "slcPCCardCfgLocalIP": slcPCCardCfgLocalIP,
       "slcPCCardCfgRemoteIP": slcPCCardCfgRemoteIP,
       "slcPCCardCfgAuth": slcPCCardCfgAuth,
       "slcPCCardCfgCHAPHost": slcPCCardCfgCHAPHost,
       "slcPCCardCfgInitScript": slcPCCardCfgInitScript,
       "slcPCCardCfgTimeout": slcPCCardCfgTimeout,
       "slcPCCardCfgDialoutNum": slcPCCardCfgDialoutNum,
       "slcPCCardCfgDialoutLogin": slcPCCardCfgDialoutLogin,
       "slcPCCardCfgDialbackMode": slcPCCardCfgDialbackMode,
       "slcPCCardCfgDialbackNum": slcPCCardCfgDialbackNum,
       "slcPCCardCfgNATState": slcPCCardCfgNATState,
       "slcPCCardCfgStorageFS": slcPCCardCfgStorageFS,
       "slcPCCardCfgISDNChannel": slcPCCardCfgISDNChannel,
       "slcPCCardCfgISDNChannelNum": slcPCCardCfgISDNChannelNum,
       "slcPCCardCfgTelnetState": slcPCCardCfgTelnetState,
       "slcPCCardCfgTelnetPort": slcPCCardCfgTelnetPort,
       "slcPCCardCfgTelnetAuth": slcPCCardCfgTelnetAuth,
       "slcPCCardCfgSSHState": slcPCCardCfgSSHState,
       "slcPCCardCfgSSHPort": slcPCCardCfgSSHPort,
       "slcPCCardCfgSSHAuth": slcPCCardCfgSSHAuth,
       "slcPCCardCfgTCPState": slcPCCardCfgTCPState,
       "slcPCCardCfgTCPPort": slcPCCardCfgTCPPort,
       "slcPCCardCfgTCPAuth": slcPCCardCfgTCPAuth,
       "slcPCCardCfgGSMPIN": slcPCCardCfgGSMPIN,
       "slcPCCardCfgGSMNetworkName": slcPCCardCfgGSMNetworkName,
       "slcPCCardCfgGSMPPPCompression": slcPCCardCfgGSMPPPCompression,
       "slcPCCardCfgGSMAutoAcquireDNS": slcPCCardCfgGSMAutoAcquireDNS,
       "slcPCCardCfgGSMDialoutMode": slcPCCardCfgGSMDialoutMode,
       "slcPCCardCfgGSMContextID": slcPCCardCfgGSMContextID,
       "slcPCCardCfgGSMBearerService": slcPCCardCfgGSMBearerService,
       "slcPCCardCfgIdleTimeout": slcPCCardCfgIdleTimeout,
       "slcPCCardCfgRestartDelay": slcPCCardCfgRestartDelay,
       "slcPCCardCfgCallerIdLogging": slcPCCardCfgCallerIdLogging,
       "slcPCCardCfgCallerIdATCmd": slcPCCardCfgCallerIdATCmd,
       "slcPCCardCfgDODAuth": slcPCCardCfgDODAuth,
       "slcPCCardCfgDODCHAPHost": slcPCCardCfgDODCHAPHost,
       "slcPCCardCfgHostList": slcPCCardCfgHostList,
       "slcPCCardCfgCBCPClientType": slcPCCardCfgCBCPClientType,
       "slcPCCardCfgCBCPServerAllowNoCallback": slcPCCardCfgCBCPServerAllowNoCallback,
       "slcPCCardCfgDialbackDelay": slcPCCardCfgDialbackDelay,
       "slcPCCardCfgCHAPAuthLocalUsers": slcPCCardCfgCHAPAuthLocalUsers,
       "slcPCCardCfgUseSites": slcPCCardCfgUseSites,
       "slcPCCardCfgDialbackRetries": slcPCCardCfgDialbackRetries,
       "slcPCCardCfgGroup": slcPCCardCfgGroup,
       "slcDevPowerSupply": slcDevPowerSupply,
       "slcDevPowerSupplyType": slcDevPowerSupplyType,
       "slcDevPowerSupplyA": slcDevPowerSupplyA,
       "slcDevPowerSupplyB": slcDevPowerSupplyB,
       "slcDevUSB": slcDevUSB,
       "slcDevUSBState": slcDevUSBState,
       "slcDevUSBCfgTable": slcDevUSBCfgTable,
       "slcDevUSBCfgEntry": slcDevUSBCfgEntry,
       "slcDevUSBId": slcDevUSBId,
       "slcDevUSBCfgCardType": slcDevUSBCfgCardType,
       "slcDevUSBCfgCardId": slcDevUSBCfgCardId,
       "slcDevUSBCfgStorageFS": slcDevUSBCfgStorageFS,
       "slcDevUSBCfgBaud": slcDevUSBCfgBaud,
       "slcDevUSBCfgDataBits": slcDevUSBCfgDataBits,
       "slcDevUSBCfgStopBits": slcDevUSBCfgStopBits,
       "slcDevUSBCfgParity": slcDevUSBCfgParity,
       "slcDevUSBCfgFlowControl": slcDevUSBCfgFlowControl,
       "slcDevUSBCfgModemState": slcDevUSBCfgModemState,
       "slcDevUSBCfgModemMode": slcDevUSBCfgModemMode,
       "slcDevUSBCfgLocalIP": slcDevUSBCfgLocalIP,
       "slcDevUSBCfgRemoteIP": slcDevUSBCfgRemoteIP,
       "slcDevUSBCfgAuth": slcDevUSBCfgAuth,
       "slcDevUSBCfgCHAPHost": slcDevUSBCfgCHAPHost,
       "slcDevUSBCfgDODAuth": slcDevUSBCfgDODAuth,
       "slcDevUSBCfgDODCHAPHost": slcDevUSBCfgDODCHAPHost,
       "slcDevUSBCfgInitScript": slcDevUSBCfgInitScript,
       "slcDevUSBCfgTimeout": slcDevUSBCfgTimeout,
       "slcDevUSBCfgDialoutNum": slcDevUSBCfgDialoutNum,
       "slcDevUSBCfgDialoutLogin": slcDevUSBCfgDialoutLogin,
       "slcDevUSBCfgDialbackMode": slcDevUSBCfgDialbackMode,
       "slcDevUSBCfgDialbackNum": slcDevUSBCfgDialbackNum,
       "slcDevUSBCfgDialbackDelay": slcDevUSBCfgDialbackDelay,
       "slcDevUSBCfgNATState": slcDevUSBCfgNATState,
       "slcDevUSBCfgIdleTimeout": slcDevUSBCfgIdleTimeout,
       "slcDevUSBCfgRestartDelay": slcDevUSBCfgRestartDelay,
       "slcDevUSBCfgCallerIdLogging": slcDevUSBCfgCallerIdLogging,
       "slcDevUSBCfgCallerIdATCmd": slcDevUSBCfgCallerIdATCmd,
       "slcDevUSBCfgHostList": slcDevUSBCfgHostList,
       "slcDevUSBCfgCBCPClientType": slcDevUSBCfgCBCPClientType,
       "slcDevUSBCfgCBCPServerAllowNoCallback": slcDevUSBCfgCBCPServerAllowNoCallback,
       "slcDevUSBCfgTelnetState": slcDevUSBCfgTelnetState,
       "slcDevUSBCfgTelnetPort": slcDevUSBCfgTelnetPort,
       "slcDevUSBCfgTelnetAuth": slcDevUSBCfgTelnetAuth,
       "slcDevUSBCfgSSHState": slcDevUSBCfgSSHState,
       "slcDevUSBCfgSSHPort": slcDevUSBCfgSSHPort,
       "slcDevUSBCfgSSHAuth": slcDevUSBCfgSSHAuth,
       "slcDevUSBCfgTCPState": slcDevUSBCfgTCPState,
       "slcDevUSBCfgTCPPort": slcDevUSBCfgTCPPort,
       "slcDevUSBCfgTCPAuth": slcDevUSBCfgTCPAuth,
       "slcDevUSBCfgGSMPIN": slcDevUSBCfgGSMPIN,
       "slcDevUSBCfgGSMPPPCompression": slcDevUSBCfgGSMPPPCompression,
       "slcDevUSBCfgGSMAutoAcquireDNS": slcDevUSBCfgGSMAutoAcquireDNS,
       "slcDevUSBCfgGSMDialoutMode": slcDevUSBCfgGSMDialoutMode,
       "slcDevUSBCfgGSMContextID": slcDevUSBCfgGSMContextID,
       "slcDevUSBCfgGSMBearerService": slcDevUSBCfgGSMBearerService,
       "slcDevUSBCfgCHAPAuthLocalUsers": slcDevUSBCfgCHAPAuthLocalUsers,
       "slcDevUSBCfgUseSites": slcDevUSBCfgUseSites,
       "slcDevUSBCfgDialbackRetries": slcDevUSBCfgDialbackRetries,
       "slcDevUSBCfgDialtoneCheck": slcDevUSBCfgDialtoneCheck,
       "slcDevUSBCfgGroup": slcDevUSBCfgGroup,
       "slcDevIntModem": slcDevIntModem,
       "slcDevIntModemModemState": slcDevIntModemModemState,
       "slcDevIntModemModemMode": slcDevIntModemModemMode,
       "slcDevIntModemLocalIP": slcDevIntModemLocalIP,
       "slcDevIntModemRemoteIP": slcDevIntModemRemoteIP,
       "slcDevIntModemAuth": slcDevIntModemAuth,
       "slcDevIntModemCHAPHost": slcDevIntModemCHAPHost,
       "slcDevIntModemInitScript": slcDevIntModemInitScript,
       "slcDevIntModemTimeout": slcDevIntModemTimeout,
       "slcDevIntModemDialoutNum": slcDevIntModemDialoutNum,
       "slcDevIntModemDialoutLogin": slcDevIntModemDialoutLogin,
       "slcDevIntModemDialbackMode": slcDevIntModemDialbackMode,
       "slcDevIntModemDialbackNum": slcDevIntModemDialbackNum,
       "slcDevIntModemDialbackRetries": slcDevIntModemDialbackRetries,
       "slcDevIntModemDialbackDelay": slcDevIntModemDialbackDelay,
       "slcDevIntModemCallerIdLogging": slcDevIntModemCallerIdLogging,
       "slcDevIntModemCallerIdATCmd": slcDevIntModemCallerIdATCmd,
       "slcDevIntModemUseSites": slcDevIntModemUseSites,
       "slcDevIntModemGroup": slcDevIntModemGroup,
       "slcDevIntModemIdleTimeout": slcDevIntModemIdleTimeout,
       "slcDevIntModemRestartDelay": slcDevIntModemRestartDelay,
       "slcDevIntModemNATState": slcDevIntModemNATState,
       "slcDevIntModemDialtoneCheck": slcDevIntModemDialtoneCheck,
       "slcDevRPM": slcDevRPM,
       "slcDevRPMCfgTable": slcDevRPMCfgTable,
       "slcDevRPMCfgEntry": slcDevRPMCfgEntry,
       "slcDevRPMId": slcDevRPMId,
       "slcDevRPMName": slcDevRPMName,
       "slcDevRPMVendorModel": slcDevRPMVendorModel,
       "slcDevRPMManagedVia": slcDevRPMManagedVia,
       "slcDevRPMIPAddress": slcDevRPMIPAddress,
       "slcDevRPMPort": slcDevRPMPort,
       "slcDevRPMDriverOpts": slcDevRPMDriverOpts,
       "slcDevRPMStatus": slcDevRPMStatus,
       "slcDevRPMFirmwareVersion": slcDevRPMFirmwareVersion,
       "slcDevRPMSerialNumber": slcDevRPMSerialNumber,
       "slcDevRPMMACAddress": slcDevRPMMACAddress,
       "slcDevRPMNumOutlets": slcDevRPMNumOutlets,
       "slcDevRPMOutletsOn": slcDevRPMOutletsOn,
       "slcDevRPMSNMPReadComm": slcDevRPMSNMPReadComm,
       "slcDevRPMAdminLogin": slcDevRPMAdminLogin,
       "slcDevRPMLogStatus": slcDevRPMLogStatus,
       "slcDevRPMCriticalSNMPTraps": slcDevRPMCriticalSNMPTraps,
       "slcDevRPMCriticalEmails": slcDevRPMCriticalEmails,
       "slcDevRPMProvidesSLCPower": slcDevRPMProvidesSLCPower,
       "slcDevRPMOnLowBattery": slcDevRPMOnLowBattery,
       "slcDevRPMShutdownOrder": slcDevRPMShutdownOrder,
       "slcDevRPMLoad": slcDevRPMLoad,
       "slcDevRPMLoadOverThreshold": slcDevRPMLoadOverThreshold,
       "slcDevRPMBatteryCharge": slcDevRPMBatteryCharge,
       "slcDevRPMBatteryRuntime": slcDevRPMBatteryRuntime,
       "slcDevRPMBeeperStatus": slcDevRPMBeeperStatus,
       "slcDevRPMTemperature": slcDevRPMTemperature,
       "slcDevRPMUptime": slcDevRPMUptime,
       "slcDevRPMStatusTable": slcDevRPMStatusTable,
       "slcDevRPMStatusEntry": slcDevRPMStatusEntry,
       "slcDevRPMCurrent": slcDevRPMCurrent,
       "slcDevRPMInputVoltage": slcDevRPMInputVoltage,
       "slcDevRPMApparentPower": slcDevRPMApparentPower,
       "slcDevRPMNominalApparentPower": slcDevRPMNominalApparentPower,
       "slcDevRPMRealPower": slcDevRPMRealPower,
       "slcDevRPMNominalRealPower": slcDevRPMNominalRealPower,
       "slcDevRPMOutletTable": slcDevRPMOutletTable,
       "slcDevRPMOutletEntry": slcDevRPMOutletEntry,
       "slcDevRPMOutletName": slcDevRPMOutletName,
       "slcDevRPMOutletState": slcDevRPMOutletState,
       "slcDevRPMOutletCurrent": slcDevRPMOutletCurrent,
       "slcDevRPMOutletAction": slcDevRPMOutletAction,
       "slcConnections": slcConnections,
       "slcConnNumber": slcConnNumber,
       "slcConnTable": slcConnTable,
       "slcConnEntry": slcConnEntry,
       "slcConnIndex": slcConnIndex,
       "slcConnEndPt1": slcConnEndPt1,
       "slcConnEndPt2": slcConnEndPt2,
       "slcConnFlow": slcConnFlow,
       "slcConnUser": slcConnUser,
       "slcConnDuration": slcConnDuration,
       "slcConnDurationStr": slcConnDurationStr,
       "slcConnIdle": slcConnIdle,
       "slcConnIdleStr": slcConnIdleStr,
       "slcConnSourceIP": slcConnSourceIP,
       "slcSystem": slcSystem,
       "slcSystemModel": slcSystemModel,
       "slcSystemSerialNo": slcSystemSerialNo,
       "slcSystemFWRev": slcSystemFWRev,
       "slcSystemLoadVia": slcSystemLoadVia,
       "slcSystemFTPServer": slcSystemFTPServer,
       "slcSystemFTPPath": slcSystemFTPPath,
       "slcSystemKeypadLock": slcSystemKeypadLock,
       "slcSystemTimeZone": slcSystemTimeZone,
       "slcSystemWelcomeBanner": slcSystemWelcomeBanner,
       "slcSystemLoginBanner": slcSystemLoginBanner,
       "slcSystemLogoutBanner": slcSystemLogoutBanner,
       "slcSystemWebTimeout": slcSystemWebTimeout,
       "slcSystemWebGadget": slcSystemWebGadget,
       "slcSystemAction": slcSystemAction,
       "slcSystemSSHPreAuthBanner": slcSystemSSHPreAuthBanner,
       "slcSystemSiteRackRow": slcSystemSiteRackRow,
       "slcSystemSiteRackCluster": slcSystemSiteRackCluster,
       "slcSystemSiteRack": slcSystemSiteRack,
       "slcSystemLCDScreens": slcSystemLCDScreens,
       "slcSystemLCDUserStrLine1": slcSystemLCDUserStrLine1,
       "slcSystemLCDUserStrLine2": slcSystemLCDUserStrLine2,
       "slcSystemLCDScrolling": slcSystemLCDScrolling,
       "slcSystemLCDScrollDelay": slcSystemLCDScrollDelay,
       "slcSystemLCDIdleDelay": slcSystemLCDIdleDelay,
       "slcSystemInternalTemp": slcSystemInternalTemp,
       "slcSystemWebProtocol": slcSystemWebProtocol,
       "slcSystemWebCipher": slcSystemWebCipher,
       "slcSystemModelString": slcSystemModelString,
       "slcSystemWebGroup": slcSystemWebGroup,
       "slcSystemWebInterface": slcSystemWebInterface,
       "slcSystemWebBanner": slcSystemWebBanner,
       "slcSystemInternalTempLow": slcSystemInternalTempLow,
       "slcSystemInternalTempHigh": slcSystemInternalTempHigh,
       "slcSystemCalibrateTemp": slcSystemCalibrateTemp,
       "slcSystemWebServer": slcSystemWebServer,
       "slcEventObjects": slcEventObjects,
       "slcPowerSupplyId": slcPowerSupplyId,
       "slcPowerSupplyAction": slcPowerSupplyAction,
       "slcDevPortNumBytes": slcDevPortNumBytes,
       "slcDevPortData": slcDevPortData,
       "slcDevPortStartByte": slcDevPortStartByte,
       "slcDevPortTimeFrame": slcDevPortTimeFrame,
       "slcDevPortDeviceErrorStatus": slcDevPortDeviceErrorStatus,
       "slcHostname": slcHostname,
       "slcPCCardSlot": slcPCCardSlot,
       "slcPCCardAction": slcPCCardAction,
       "slcPCCardType": slcPCCardType,
       "slcUSBAction": slcUSBAction,
       "slcUSBType": slcUSBType,
       "slcDevPortErrorStatus": slcDevPortErrorStatus,
       "slcSDCardAction": slcSDCardAction,
       "slcRPMAction": slcRPMAction,
       "slcEventHost": slcEventHost}
)
