# SNMP MIB module (SWPRIMGMT-DES30XXP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWPRIMGMT-DES30XXP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:05 2024
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

(dlink_mgmt,
 dlink_products) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-mgmt",
    "dlink-products")

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

_Dlink_des30xxproductProd_ObjectIdentity = ObjectIdentity
dlink_des30xxproductProd = _Dlink_des30xxproductProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63)
)
_Dlink_des3028Prod_ObjectIdentity = ObjectIdentity
dlink_des3028Prod = _Dlink_des3028Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 6)
)
_Dlink_des3028PProd_ObjectIdentity = ObjectIdentity
dlink_des3028PProd = _Dlink_des3028PProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 7)
)
_Dlink_des3052Prod_ObjectIdentity = ObjectIdentity
dlink_des3052Prod = _Dlink_des3052Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 8)
)
_Dlink_des3052PProd_ObjectIdentity = ObjectIdentity
dlink_des3052PProd = _Dlink_des3052PProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 9)
)
_Des30xxSeriesProd_ObjectIdentity = ObjectIdentity
des30xxSeriesProd = _Des30xxSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63)
)
_Des3028_ObjectIdentity = ObjectIdentity
des3028 = _Des3028_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 6)
)
_Des3028p_ObjectIdentity = ObjectIdentity
des3028p = _Des3028p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 7)
)
_Des3052_ObjectIdentity = ObjectIdentity
des3052 = _Des3052_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 8)
)
_Des3052p_ObjectIdentity = ObjectIdentity
des3052p = _Des3052p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 9)
)
_Des3028g_ObjectIdentity = ObjectIdentity
des3028g = _Des3028g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWPRIMGMT-DES30XXP-MIB",
    **{"dlink-des30xxproductProd": dlink_des30xxproductProd,
       "dlink-des3028Prod": dlink_des3028Prod,
       "dlink-des3028PProd": dlink_des3028PProd,
       "dlink-des3052Prod": dlink_des3052Prod,
       "dlink-des3052PProd": dlink_des3052PProd,
       "des30xxSeriesProd": des30xxSeriesProd,
       "des3028": des3028,
       "des3028p": des3028p,
       "des3052": des3052,
       "des3052p": des3052p,
       "des3028g": des3028g}
)
