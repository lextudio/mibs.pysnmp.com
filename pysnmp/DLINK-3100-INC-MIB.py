# SNMP MIB module (DLINK-3100-INC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-3100-INC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:39 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_Dgs3100SeriesProd_ObjectIdentity = ObjectIdentity
dlink_Dgs3100SeriesProd = _Dlink_Dgs3100SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94)
)
_Dgs3124_Prod_ObjectIdentity = ObjectIdentity
dgs3124_Prod = _Dgs3124_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 1)
)
_Dgs3124p_Prod_ObjectIdentity = ObjectIdentity
dgs3124p_Prod = _Dgs3124p_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 2)
)
_Dgs3148_Prod_ObjectIdentity = ObjectIdentity
dgs3148_Prod = _Dgs3148_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 3)
)
_Dgs3148p_Prod_ObjectIdentity = ObjectIdentity
dgs3148p_Prod = _Dgs3148p_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 4)
)
_Dgs3124tg_Prod_ObjectIdentity = ObjectIdentity
dgs3124tg_Prod = _Dgs3124tg_Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 5)
)
_Dgs3100_SWL2MGMT_MIB_ObjectIdentity = ObjectIdentity
dgs3100_SWL2MGMT_MIB = _Dgs3100_SWL2MGMT_MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89)
)
_Rnd_ObjectIdentity = ObjectIdentity
rnd = _Rnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-INC-MIB",
    **{"dlink": dlink,
       "dlink-products": dlink_products,
       "dlink-Dgs3100SeriesProd": dlink_Dgs3100SeriesProd,
       "dgs3124-Prod": dgs3124_Prod,
       "dgs3124p-Prod": dgs3124p_Prod,
       "dgs3148-Prod": dgs3148_Prod,
       "dgs3148p-Prod": dgs3148p_Prod,
       "dgs3124tg-Prod": dgs3124tg_Prod,
       "dgs3100-SWL2MGMT-MIB": dgs3100_SWL2MGMT_MIB,
       "rnd": rnd}
)
