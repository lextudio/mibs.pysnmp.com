# SNMP MIB module (CACHEFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CACHEFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:20 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cacheFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1)
)
_Cache_ObjectIdentity = ObjectIdentity
cache = _Cache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1)
)
_CacheFlow1000_ObjectIdentity = ObjectIdentity
cacheFlow1000 = _CacheFlow1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 1)
)
_CacheFlow100_ObjectIdentity = ObjectIdentity
cacheFlow100 = _CacheFlow100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 2)
)
_CacheFlow500_ObjectIdentity = ObjectIdentity
cacheFlow500 = _CacheFlow500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 3)
)
_CacheFlow2000_ObjectIdentity = ObjectIdentity
cacheFlow2000 = _CacheFlow2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 4)
)
_CacheFlow5000_ObjectIdentity = ObjectIdentity
cacheFlow5000 = _CacheFlow5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 5)
)
_CacheFlow500A_ObjectIdentity = ObjectIdentity
cacheFlow500A = _CacheFlow500A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 6)
)
_CacheFlow3000_ObjectIdentity = ObjectIdentity
cacheFlow3000 = _CacheFlow3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 7)
)
_CacheFlow5x5_ObjectIdentity = ObjectIdentity
cacheFlow5x5 = _CacheFlow5x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 8)
)
_CacheFlow110_ObjectIdentity = ObjectIdentity
cacheFlow110 = _CacheFlow110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 9)
)
_CacheFlow600_ObjectIdentity = ObjectIdentity
cacheFlow600 = _CacheFlow600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 10)
)
_CacheFlow6000_ObjectIdentity = ObjectIdentity
cacheFlow6000 = _CacheFlow6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 11)
)
_CacheFlow610_ObjectIdentity = ObjectIdentity
cacheFlow610 = _CacheFlow610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 12)
)
_CacheFlow6x5_ObjectIdentity = ObjectIdentity
cacheFlow6x5 = _CacheFlow6x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 13)
)
_CacheFlow3000s_ObjectIdentity = ObjectIdentity
cacheFlow3000s = _CacheFlow3000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 14)
)
_CacheFlow5000s_ObjectIdentity = ObjectIdentity
cacheFlow5000s = _CacheFlow5000s_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 15)
)
_CacheFlow7x5_ObjectIdentity = ObjectIdentity
cacheFlow7x5 = _CacheFlow7x5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 16)
)
_CacheFlow710_ObjectIdentity = ObjectIdentity
cacheFlow710 = _CacheFlow710_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 17)
)
_CacheFlow7000_ObjectIdentity = ObjectIdentity
cacheFlow7000 = _CacheFlow7000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 18)
)
_CacheFlow611_ObjectIdentity = ObjectIdentity
cacheFlow611 = _CacheFlow611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 19)
)
_CacheFlow800_ObjectIdentity = ObjectIdentity
cacheFlow800 = _CacheFlow800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 1, 1, 20)
)
_CacheFlowMgmt_ObjectIdentity = ObjectIdentity
cacheFlowMgmt = _CacheFlowMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CACHEFLOW-MIB",
    **{"cacheFlow": cacheFlow,
       "products": products,
       "cache": cache,
       "cacheFlow1000": cacheFlow1000,
       "cacheFlow100": cacheFlow100,
       "cacheFlow500": cacheFlow500,
       "cacheFlow2000": cacheFlow2000,
       "cacheFlow5000": cacheFlow5000,
       "cacheFlow500A": cacheFlow500A,
       "cacheFlow3000": cacheFlow3000,
       "cacheFlow5x5": cacheFlow5x5,
       "cacheFlow110": cacheFlow110,
       "cacheFlow600": cacheFlow600,
       "cacheFlow6000": cacheFlow6000,
       "cacheFlow610": cacheFlow610,
       "cacheFlow6x5": cacheFlow6x5,
       "cacheFlow3000s": cacheFlow3000s,
       "cacheFlow5000s": cacheFlow5000s,
       "cacheFlow7x5": cacheFlow7x5,
       "cacheFlow710": cacheFlow710,
       "cacheFlow7000": cacheFlow7000,
       "cacheFlow611": cacheFlow611,
       "cacheFlow800": cacheFlow800,
       "cacheFlowMgmt": cacheFlowMgmt}
)
