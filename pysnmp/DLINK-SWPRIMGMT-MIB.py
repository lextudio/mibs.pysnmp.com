# SNMP MIB module (DLINK-SWPRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-SWPRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:50 2024
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
_Dlink_des3010xProd_ObjectIdentity = ObjectIdentity
dlink_des3010xProd = _Dlink_des3010xProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 1)
)
_Dlink_des3010FProd_ObjectIdentity = ObjectIdentity
dlink_des3010FProd = _Dlink_des3010FProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 1)
)
_Dlink_des3010GProd_ObjectIdentity = ObjectIdentity
dlink_des3010GProd = _Dlink_des3010GProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 1, 2)
)
_Dlink_des3018Prod_ObjectIdentity = ObjectIdentity
dlink_des3018Prod = _Dlink_des3018Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 2)
)
_Dlink_des3026Prod_ObjectIdentity = ObjectIdentity
dlink_des3026Prod = _Dlink_des3026Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 3)
)
_Dlink_des3010FLProd_ObjectIdentity = ObjectIdentity
dlink_des3010FLProd = _Dlink_des3010FLProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 4)
)
_Dlink_des3016Prod_ObjectIdentity = ObjectIdentity
dlink_des3016Prod = _Dlink_des3016Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 63, 10)
)
_Des30xxSeriesProd_ObjectIdentity = ObjectIdentity
des30xxSeriesProd = _Des30xxSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63)
)
_Des3010_ObjectIdentity = ObjectIdentity
des3010 = _Des3010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 1)
)
_Des3010f_ObjectIdentity = ObjectIdentity
des3010f = _Des3010f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 1)
)
_Des3010g_ObjectIdentity = ObjectIdentity
des3010g = _Des3010g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 1, 2)
)
_Des3018_ObjectIdentity = ObjectIdentity
des3018 = _Des3018_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 2)
)
_Des3026_ObjectIdentity = ObjectIdentity
des3026 = _Des3026_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 3)
)
_Des3010fl_ObjectIdentity = ObjectIdentity
des3010fl = _Des3010fl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 4)
)
_Des3016_ObjectIdentity = ObjectIdentity
des3016 = _Des3016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 63, 10)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-SWPRIMGMT-MIB",
    **{"dlink-des30xxproductProd": dlink_des30xxproductProd,
       "dlink-des3010xProd": dlink_des3010xProd,
       "dlink-des3010FProd": dlink_des3010FProd,
       "dlink-des3010GProd": dlink_des3010GProd,
       "dlink-des3018Prod": dlink_des3018Prod,
       "dlink-des3026Prod": dlink_des3026Prod,
       "dlink-des3010FLProd": dlink_des3010FLProd,
       "dlink-des3016Prod": dlink_des3016Prod,
       "des30xxSeriesProd": des30xxSeriesProd,
       "des3010": des3010,
       "des3010f": des3010f,
       "des3010g": des3010g,
       "des3018": des3018,
       "des3026": des3026,
       "des3010fl": des3010fl,
       "des3016": des3016}
)
