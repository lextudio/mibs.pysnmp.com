# SNMP MIB module (SW3200PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3200PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:32 2024
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

_Dlink_Dgs3200SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Dgs3200SeriesProd = _Dlink_Dgs3200SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101)
)
_Dgs3200_Prod_ObjectIdentity = ObjectIdentity
dgs3200_Prod = _Dgs3200_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 1)
)
_Dgs3216_Prod_ObjectIdentity = ObjectIdentity
dgs3216_Prod = _Dgs3216_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 2)
)
_Dgs3224_Prod_ObjectIdentity = ObjectIdentity
dgs3224_Prod = _Dgs3224_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 101, 3)
)
_Dlink_Dgs3200Series_ObjectIdentity = ObjectIdentity
dlink_Dgs3200Series = _Dlink_Dgs3200Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101)
)
_Dgs3200_ObjectIdentity = ObjectIdentity
dgs3200 = _Dgs3200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 1)
)
_Dgs3216_ObjectIdentity = ObjectIdentity
dgs3216 = _Dgs3216_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 2)
)
_Dgs3224_ObjectIdentity = ObjectIdentity
dgs3224 = _Dgs3224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 101, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3200PRIMGMT-MIB",
    **{"dlink-Dgs3200SeriesProd": dlink_Dgs3200SeriesProd,
       "dgs3200-Prod": dgs3200_Prod,
       "dgs3216-Prod": dgs3216_Prod,
       "dgs3224-Prod": dgs3224_Prod,
       "dlink-Dgs3200Series": dlink_Dgs3200Series,
       "dgs3200": dgs3200,
       "dgs3216": dgs3216,
       "dgs3224": dgs3224}
)
