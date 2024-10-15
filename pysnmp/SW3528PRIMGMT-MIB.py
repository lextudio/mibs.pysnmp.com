# SNMP MIB module (SW3528PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3528PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:37 2024
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

_Dlink_Des3528SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Des3528SeriesProd = _Dlink_Des3528SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105)
)
_Des3528Prod_ObjectIdentity = ObjectIdentity
des3528Prod = _Des3528Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 1)
)
_Des3528pProd_ObjectIdentity = ObjectIdentity
des3528pProd = _Des3528pProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 2)
)
_Des3552Prod_ObjectIdentity = ObjectIdentity
des3552Prod = _Des3552Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 3)
)
_Des3552pProd_ObjectIdentity = ObjectIdentity
des3552pProd = _Des3552pProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 4)
)
_Des3528dcProd_ObjectIdentity = ObjectIdentity
des3528dcProd = _Des3528dcProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 105, 5)
)
_Dlink_Des3528Series_ObjectIdentity = ObjectIdentity
dlink_Des3528Series = _Dlink_Des3528Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105)
)
_Des3528_ObjectIdentity = ObjectIdentity
des3528 = _Des3528_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 1)
)
_Des3528p_ObjectIdentity = ObjectIdentity
des3528p = _Des3528p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 2)
)
_Des3552_ObjectIdentity = ObjectIdentity
des3552 = _Des3552_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 3)
)
_Des3552p_ObjectIdentity = ObjectIdentity
des3552p = _Des3552p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 4)
)
_Des3528dc_ObjectIdentity = ObjectIdentity
des3528dc = _Des3528dc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 105, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3528PRIMGMT-MIB",
    **{"dlink-Des3528SeriesProd": dlink_Des3528SeriesProd,
       "des3528Prod": des3528Prod,
       "des3528pProd": des3528pProd,
       "des3552Prod": des3552Prod,
       "des3552pProd": des3552pProd,
       "des3528dcProd": des3528dcProd,
       "dlink-Des3528Series": dlink_Des3528Series,
       "des3528": des3528,
       "des3528p": des3528p,
       "des3552": des3552,
       "des3552p": des3552p,
       "des3528dc": des3528dc}
)
