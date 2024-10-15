# SNMP MIB module (ENTERASYS-DNS-RESOLVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-DNS-RESOLVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:47 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

etsysDnsResolverMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63)
)
etsysDnsResolverMIB.setRevisions(
        ("2008-08-11 15:48",
         "2008-06-18 20:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysDnsResolverObjects_ObjectIdentity = ObjectIdentity
etsysDnsResolverObjects = _EtsysDnsResolverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1)
)
_EtsysDnsResolverSystem_ObjectIdentity = ObjectIdentity
etsysDnsResolverSystem = _EtsysDnsResolverSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1)
)


class _EtsysDnsResolverServiceType_Type(Integer32):
    """Custom type etsysDnsResolverServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iterativeOnly", 2),
          ("recursiveAndIterative", 3),
          ("recursiveOnly", 1))
    )


_EtsysDnsResolverServiceType_Type.__name__ = "Integer32"
_EtsysDnsResolverServiceType_Object = MibScalar
etsysDnsResolverServiceType = _EtsysDnsResolverServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 1),
    _EtsysDnsResolverServiceType_Type()
)
etsysDnsResolverServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDnsResolverServiceType.setStatus("current")


class _EtsysDnsResolverDomainName_Type(SnmpAdminString):
    """Custom type etsysDnsResolverDomainName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysDnsResolverDomainName_Object = MibScalar
etsysDnsResolverDomainName = _EtsysDnsResolverDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 2),
    _EtsysDnsResolverDomainName_Type()
)
etsysDnsResolverDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverDomainName.setStatus("current")


class _EtsysDnsResolverPrimaryServerAddrType_Type(InetAddressType):
    """Custom type etsysDnsResolverPrimaryServerAddrType based on InetAddressType"""


_EtsysDnsResolverPrimaryServerAddrType_Object = MibScalar
etsysDnsResolverPrimaryServerAddrType = _EtsysDnsResolverPrimaryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 3),
    _EtsysDnsResolverPrimaryServerAddrType_Type()
)
etsysDnsResolverPrimaryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverPrimaryServerAddrType.setStatus("current")


class _EtsysDnsResolverPrimaryServerAddr_Type(InetAddress):
    """Custom type etsysDnsResolverPrimaryServerAddr based on InetAddress"""
    defaultHexValue = ""


_EtsysDnsResolverPrimaryServerAddr_Object = MibScalar
etsysDnsResolverPrimaryServerAddr = _EtsysDnsResolverPrimaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 4),
    _EtsysDnsResolverPrimaryServerAddr_Type()
)
etsysDnsResolverPrimaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverPrimaryServerAddr.setStatus("current")


class _EtsysDnsResolverSecondaryServerAddrType_Type(InetAddressType):
    """Custom type etsysDnsResolverSecondaryServerAddrType based on InetAddressType"""


_EtsysDnsResolverSecondaryServerAddrType_Object = MibScalar
etsysDnsResolverSecondaryServerAddrType = _EtsysDnsResolverSecondaryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 5),
    _EtsysDnsResolverSecondaryServerAddrType_Type()
)
etsysDnsResolverSecondaryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverSecondaryServerAddrType.setStatus("current")


class _EtsysDnsResolverSecondaryServerAddr_Type(InetAddress):
    """Custom type etsysDnsResolverSecondaryServerAddr based on InetAddress"""
    defaultHexValue = ""


_EtsysDnsResolverSecondaryServerAddr_Object = MibScalar
etsysDnsResolverSecondaryServerAddr = _EtsysDnsResolverSecondaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 6),
    _EtsysDnsResolverSecondaryServerAddr_Type()
)
etsysDnsResolverSecondaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverSecondaryServerAddr.setStatus("current")


class _EtsysDnsResolverTertiaryServerAddrType_Type(InetAddressType):
    """Custom type etsysDnsResolverTertiaryServerAddrType based on InetAddressType"""


_EtsysDnsResolverTertiaryServerAddrType_Object = MibScalar
etsysDnsResolverTertiaryServerAddrType = _EtsysDnsResolverTertiaryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 7),
    _EtsysDnsResolverTertiaryServerAddrType_Type()
)
etsysDnsResolverTertiaryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverTertiaryServerAddrType.setStatus("current")


class _EtsysDnsResolverTertiaryServerAddr_Type(InetAddress):
    """Custom type etsysDnsResolverTertiaryServerAddr based on InetAddress"""
    defaultHexValue = ""


_EtsysDnsResolverTertiaryServerAddr_Object = MibScalar
etsysDnsResolverTertiaryServerAddr = _EtsysDnsResolverTertiaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 8),
    _EtsysDnsResolverTertiaryServerAddr_Type()
)
etsysDnsResolverTertiaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverTertiaryServerAddr.setStatus("current")


class _EtsysDnsResolverQuaternaryServerAddrType_Type(InetAddressType):
    """Custom type etsysDnsResolverQuaternaryServerAddrType based on InetAddressType"""


_EtsysDnsResolverQuaternaryServerAddrType_Object = MibScalar
etsysDnsResolverQuaternaryServerAddrType = _EtsysDnsResolverQuaternaryServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 9),
    _EtsysDnsResolverQuaternaryServerAddrType_Type()
)
etsysDnsResolverQuaternaryServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverQuaternaryServerAddrType.setStatus("current")


class _EtsysDnsResolverQuaternaryServerAddr_Type(InetAddress):
    """Custom type etsysDnsResolverQuaternaryServerAddr based on InetAddress"""
    defaultHexValue = ""


_EtsysDnsResolverQuaternaryServerAddr_Object = MibScalar
etsysDnsResolverQuaternaryServerAddr = _EtsysDnsResolverQuaternaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 10),
    _EtsysDnsResolverQuaternaryServerAddr_Type()
)
etsysDnsResolverQuaternaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverQuaternaryServerAddr.setStatus("current")


class _EtsysDnsResolverIpv4DnsZone_Type(SnmpAdminString):
    """Custom type etsysDnsResolverIpv4DnsZone based on SnmpAdminString"""
    defaultValue = OctetString("in-addr.arpa")


_EtsysDnsResolverIpv4DnsZone_Object = MibScalar
etsysDnsResolverIpv4DnsZone = _EtsysDnsResolverIpv4DnsZone_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 11),
    _EtsysDnsResolverIpv4DnsZone_Type()
)
etsysDnsResolverIpv4DnsZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverIpv4DnsZone.setStatus("current")


class _EtsysDnsResolverIpv6DnsZone_Type(SnmpAdminString):
    """Custom type etsysDnsResolverIpv6DnsZone based on SnmpAdminString"""
    defaultValue = OctetString("ip6.arpa")


_EtsysDnsResolverIpv6DnsZone_Object = MibScalar
etsysDnsResolverIpv6DnsZone = _EtsysDnsResolverIpv6DnsZone_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 12),
    _EtsysDnsResolverIpv6DnsZone_Type()
)
etsysDnsResolverIpv6DnsZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverIpv6DnsZone.setStatus("current")


class _EtsysDnsResolverServerPortNumber_Type(InetPortNumber):
    """Custom type etsysDnsResolverServerPortNumber based on InetPortNumber"""
    defaultValue = 53


_EtsysDnsResolverServerPortNumber_Object = MibScalar
etsysDnsResolverServerPortNumber = _EtsysDnsResolverServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 13),
    _EtsysDnsResolverServerPortNumber_Type()
)
etsysDnsResolverServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverServerPortNumber.setStatus("current")


class _EtsysDnsResolverQueryTimeout_Type(Unsigned32):
    """Custom type etsysDnsResolverQueryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EtsysDnsResolverQueryTimeout_Type.__name__ = "Unsigned32"
_EtsysDnsResolverQueryTimeout_Object = MibScalar
etsysDnsResolverQueryTimeout = _EtsysDnsResolverQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 14),
    _EtsysDnsResolverQueryTimeout_Type()
)
etsysDnsResolverQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverQueryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysDnsResolverQueryTimeout.setUnits("seconds")


class _EtsysDnsResolverQueryRetries_Type(Unsigned32):
    """Custom type etsysDnsResolverQueryRetries based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_EtsysDnsResolverQueryRetries_Type.__name__ = "Unsigned32"
_EtsysDnsResolverQueryRetries_Object = MibScalar
etsysDnsResolverQueryRetries = _EtsysDnsResolverQueryRetries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 15),
    _EtsysDnsResolverQueryRetries_Type()
)
etsysDnsResolverQueryRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverQueryRetries.setStatus("current")


class _EtsysDnsResolverEnableStatus_Type(Integer32):
    """Custom type etsysDnsResolverEnableStatus based on Integer32"""
    defaultValue = 1

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


_EtsysDnsResolverEnableStatus_Type.__name__ = "Integer32"
_EtsysDnsResolverEnableStatus_Object = MibScalar
etsysDnsResolverEnableStatus = _EtsysDnsResolverEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 1, 1, 16),
    _EtsysDnsResolverEnableStatus_Type()
)
etsysDnsResolverEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDnsResolverEnableStatus.setStatus("current")
_EtsysDnsResolverConformance_ObjectIdentity = ObjectIdentity
etsysDnsResolverConformance = _EtsysDnsResolverConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2)
)
_EtsysDnsResolverGroups_ObjectIdentity = ObjectIdentity
etsysDnsResolverGroups = _EtsysDnsResolverGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 1)
)
_EtsysDnsResolverCompliances_ObjectIdentity = ObjectIdentity
etsysDnsResolverCompliances = _EtsysDnsResolverCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 2)
)

# Managed Objects groups

etsysDnsResolverPrimaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 1, 1)
)
etsysDnsResolverPrimaryGroup.setObjects(
      *(("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverServiceType"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverDomainName"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverPrimaryServerAddrType"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverPrimaryServerAddr"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverIpv4DnsZone"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverIpv6DnsZone"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverServerPortNumber"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverQueryTimeout"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverQueryRetries"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverEnableStatus"))
)
if mibBuilder.loadTexts:
    etsysDnsResolverPrimaryGroup.setStatus("current")

etsysDnsResolverSecondaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 1, 2)
)
etsysDnsResolverSecondaryGroup.setObjects(
      *(("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverSecondaryServerAddrType"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverSecondaryServerAddr"))
)
if mibBuilder.loadTexts:
    etsysDnsResolverSecondaryGroup.setStatus("current")

etsysDnsResolverTertiaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 1, 3)
)
etsysDnsResolverTertiaryGroup.setObjects(
      *(("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverTertiaryServerAddrType"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverTertiaryServerAddr"))
)
if mibBuilder.loadTexts:
    etsysDnsResolverTertiaryGroup.setStatus("current")

etsysDnsResolverQuaternaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 1, 4)
)
etsysDnsResolverQuaternaryGroup.setObjects(
      *(("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverQuaternaryServerAddrType"),
        ("ENTERASYS-DNS-RESOLVER-MIB", "etsysDnsResolverQuaternaryServerAddr"))
)
if mibBuilder.loadTexts:
    etsysDnsResolverQuaternaryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDnsResolverCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 63, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDnsResolverCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-DNS-RESOLVER-MIB",
    **{"etsysDnsResolverMIB": etsysDnsResolverMIB,
       "etsysDnsResolverObjects": etsysDnsResolverObjects,
       "etsysDnsResolverSystem": etsysDnsResolverSystem,
       "etsysDnsResolverServiceType": etsysDnsResolverServiceType,
       "etsysDnsResolverDomainName": etsysDnsResolverDomainName,
       "etsysDnsResolverPrimaryServerAddrType": etsysDnsResolverPrimaryServerAddrType,
       "etsysDnsResolverPrimaryServerAddr": etsysDnsResolverPrimaryServerAddr,
       "etsysDnsResolverSecondaryServerAddrType": etsysDnsResolverSecondaryServerAddrType,
       "etsysDnsResolverSecondaryServerAddr": etsysDnsResolverSecondaryServerAddr,
       "etsysDnsResolverTertiaryServerAddrType": etsysDnsResolverTertiaryServerAddrType,
       "etsysDnsResolverTertiaryServerAddr": etsysDnsResolverTertiaryServerAddr,
       "etsysDnsResolverQuaternaryServerAddrType": etsysDnsResolverQuaternaryServerAddrType,
       "etsysDnsResolverQuaternaryServerAddr": etsysDnsResolverQuaternaryServerAddr,
       "etsysDnsResolverIpv4DnsZone": etsysDnsResolverIpv4DnsZone,
       "etsysDnsResolverIpv6DnsZone": etsysDnsResolverIpv6DnsZone,
       "etsysDnsResolverServerPortNumber": etsysDnsResolverServerPortNumber,
       "etsysDnsResolverQueryTimeout": etsysDnsResolverQueryTimeout,
       "etsysDnsResolverQueryRetries": etsysDnsResolverQueryRetries,
       "etsysDnsResolverEnableStatus": etsysDnsResolverEnableStatus,
       "etsysDnsResolverConformance": etsysDnsResolverConformance,
       "etsysDnsResolverGroups": etsysDnsResolverGroups,
       "etsysDnsResolverPrimaryGroup": etsysDnsResolverPrimaryGroup,
       "etsysDnsResolverSecondaryGroup": etsysDnsResolverSecondaryGroup,
       "etsysDnsResolverTertiaryGroup": etsysDnsResolverTertiaryGroup,
       "etsysDnsResolverQuaternaryGroup": etsysDnsResolverQuaternaryGroup,
       "etsysDnsResolverCompliances": etsysDnsResolverCompliances,
       "etsysDnsResolverCompliance": etsysDnsResolverCompliance}
)
