# SNMP MIB module (A3COM-HUAWEI-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:09 2024
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

(huawei,
 hwInternetProtocol,
 hwLocal) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huawei",
    "hwInternetProtocol",
    "hwLocal")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RIp_ObjectIdentity = ObjectIdentity
rIp = _RIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1)
)
_IpTooShorts_Type = Counter32
_IpTooShorts_Object = MibScalar
ipTooShorts = _IpTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 1),
    _IpTooShorts_Type()
)
ipTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTooShorts.setStatus("mandatory")
_IpTooSmalls_Type = Counter32
_IpTooSmalls_Object = MibScalar
ipTooSmalls = _IpTooSmalls_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 2),
    _IpTooSmalls_Type()
)
ipTooSmalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTooSmalls.setStatus("mandatory")
_IpBadVersions_Type = Counter32
_IpBadVersions_Object = MibScalar
ipBadVersions = _IpBadVersions_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 3),
    _IpBadVersions_Type()
)
ipBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBadVersions.setStatus("mandatory")
_IpBadChecksums_Type = Counter32
_IpBadChecksums_Object = MibScalar
ipBadChecksums = _IpBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 4),
    _IpBadChecksums_Type()
)
ipBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBadChecksums.setStatus("mandatory")
_IpBadLens_Type = Counter32
_IpBadLens_Object = MibScalar
ipBadLens = _IpBadLens_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 5),
    _IpBadLens_Type()
)
ipBadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBadLens.setStatus("mandatory")
_IpBadHeadLens_Type = Counter32
_IpBadHeadLens_Object = MibScalar
ipBadHeadLens = _IpBadHeadLens_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 6),
    _IpBadHeadLens_Type()
)
ipBadHeadLens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBadHeadLens.setStatus("mandatory")
_IpBadOptions_Type = Counter32
_IpBadOptions_Object = MibScalar
ipBadOptions = _IpBadOptions_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 7),
    _IpBadOptions_Type()
)
ipBadOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipBadOptions.setStatus("mandatory")
_IpFragDroppeds_Type = Counter32
_IpFragDroppeds_Object = MibScalar
ipFragDroppeds = _IpFragDroppeds_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 8),
    _IpFragDroppeds_Type()
)
ipFragDroppeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragDroppeds.setStatus("mandatory")
_IpRawOuts_Type = Counter32
_IpRawOuts_Object = MibScalar
ipRawOuts = _IpRawOuts_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 9),
    _IpRawOuts_Type()
)
ipRawOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRawOuts.setStatus("mandatory")
_IpRouteBadRedirects_Type = Counter32
_IpRouteBadRedirects_Object = MibScalar
ipRouteBadRedirects = _IpRouteBadRedirects_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 10),
    _IpRouteBadRedirects_Type()
)
ipRouteBadRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteBadRedirects.setStatus("mandatory")
_IpRouteDynamics_Type = Counter32
_IpRouteDynamics_Object = MibScalar
ipRouteDynamics = _IpRouteDynamics_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 11),
    _IpRouteDynamics_Type()
)
ipRouteDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteDynamics.setStatus("mandatory")
_IpRouteNewGateways_Type = Counter32
_IpRouteNewGateways_Object = MibScalar
ipRouteNewGateways = _IpRouteNewGateways_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 12),
    _IpRouteNewGateways_Type()
)
ipRouteNewGateways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteNewGateways.setStatus("mandatory")
_IpRouteUnreachs_Type = Counter32
_IpRouteUnreachs_Object = MibScalar
ipRouteUnreachs = _IpRouteUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 13),
    _IpRouteUnreachs_Type()
)
ipRouteUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteUnreachs.setStatus("mandatory")
_IpRouteWilds_Type = Counter32
_IpRouteWilds_Object = MibScalar
ipRouteWilds = _IpRouteWilds_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 1, 3, 1, 14),
    _IpRouteWilds_Type()
)
ipRouteWilds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteWilds.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IP-MIB",
    **{"rIp": rIp,
       "ipTooShorts": ipTooShorts,
       "ipTooSmalls": ipTooSmalls,
       "ipBadVersions": ipBadVersions,
       "ipBadChecksums": ipBadChecksums,
       "ipBadLens": ipBadLens,
       "ipBadHeadLens": ipBadHeadLens,
       "ipBadOptions": ipBadOptions,
       "ipFragDroppeds": ipFragDroppeds,
       "ipRawOuts": ipRawOuts,
       "ipRouteBadRedirects": ipRouteBadRedirects,
       "ipRouteDynamics": ipRouteDynamics,
       "ipRouteNewGateways": ipRouteNewGateways,
       "ipRouteUnreachs": ipRouteUnreachs,
       "ipRouteWilds": ipRouteWilds}
)
