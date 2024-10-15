# SNMP MIB module (SW3800PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3800PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:50 2024
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

_Dlink_des3800SeriesProd_ObjectIdentity = ObjectIdentity
dlink_des3800SeriesProd = _Dlink_des3800SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69)
)
_Dlink_des3828Prod_ObjectIdentity = ObjectIdentity
dlink_des3828Prod = _Dlink_des3828Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69, 1)
)
_Dlink_des3828DCProd_ObjectIdentity = ObjectIdentity
dlink_des3828DCProd = _Dlink_des3828DCProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69, 2)
)
_Dlink_des3828PProd_ObjectIdentity = ObjectIdentity
dlink_des3828PProd = _Dlink_des3828PProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69, 3)
)
_Dlink_des3852Prod_ObjectIdentity = ObjectIdentity
dlink_des3852Prod = _Dlink_des3852Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69, 4)
)
_Dlink_des3852PProd_ObjectIdentity = ObjectIdentity
dlink_des3852PProd = _Dlink_des3852PProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 69, 5)
)
_Des3800SeriesProd_ObjectIdentity = ObjectIdentity
des3800SeriesProd = _Des3800SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69)
)
_Des3828_ObjectIdentity = ObjectIdentity
des3828 = _Des3828_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 1)
)
_Des3828DC_ObjectIdentity = ObjectIdentity
des3828DC = _Des3828DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 2)
)
_Des3828P_ObjectIdentity = ObjectIdentity
des3828P = _Des3828P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 3)
)
_Des3852_ObjectIdentity = ObjectIdentity
des3852 = _Des3852_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 4)
)
_Des3852P_ObjectIdentity = ObjectIdentity
des3852P = _Des3852P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 69, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3800PRIMGMT-MIB",
    **{"dlink-des3800SeriesProd": dlink_des3800SeriesProd,
       "dlink-des3828Prod": dlink_des3828Prod,
       "dlink-des3828DCProd": dlink_des3828DCProd,
       "dlink-des3828PProd": dlink_des3828PProd,
       "dlink-des3852Prod": dlink_des3852Prod,
       "dlink-des3852PProd": dlink_des3852PProd,
       "des3800SeriesProd": des3800SeriesProd,
       "des3828": des3828,
       "des3828DC": des3828DC,
       "des3828P": des3828P,
       "des3852": des3852,
       "des3852P": des3852P}
)
