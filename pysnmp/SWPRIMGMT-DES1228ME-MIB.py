# SNMP MIB module (SWPRIMGMT-DES1228ME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWPRIMGMT-DES1228ME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:45 2024
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

_Dlink_des1228MEproductProd_ObjectIdentity = ObjectIdentity
dlink_des1228MEproductProd = _Dlink_des1228MEproductProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 116)
)
_Dlink_des1228MEProd_ObjectIdentity = ObjectIdentity
dlink_des1228MEProd = _Dlink_des1228MEProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 116, 1)
)
_Dlink_des1228MEv2Prod_ObjectIdentity = ObjectIdentity
dlink_des1228MEv2Prod = _Dlink_des1228MEv2Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 116, 2)
)
_Des1228MESeriesProd_ObjectIdentity = ObjectIdentity
des1228MESeriesProd = _Des1228MESeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 116)
)
_Des1228ME_ObjectIdentity = ObjectIdentity
des1228ME = _Des1228ME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 116, 1)
)
_Des1228MEv2_ObjectIdentity = ObjectIdentity
des1228MEv2 = _Des1228MEv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 116, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWPRIMGMT-DES1228ME-MIB",
    **{"dlink-des1228MEproductProd": dlink_des1228MEproductProd,
       "dlink-des1228MEProd": dlink_des1228MEProd,
       "dlink-des1228MEv2Prod": dlink_des1228MEv2Prod,
       "des1228MESeriesProd": des1228MESeriesProd,
       "des1228ME": des1228ME,
       "des1228MEv2": des1228MEv2}
)
