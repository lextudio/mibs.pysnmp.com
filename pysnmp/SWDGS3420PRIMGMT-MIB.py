# SNMP MIB module (SWDGS3420PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWDGS3420PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:13 2024
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

_Dlink_Dgs3420Prod_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod = _Dlink_Dgs3420Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119)
)
_Dlink_Dgs3420Prod_Dgs3420_28TC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_28TC = _Dlink_Dgs3420Prod_Dgs3420_28TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 1)
)
_Dlink_Dgs3420Prod_Dgs3420_28SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_28SC = _Dlink_Dgs3420Prod_Dgs3420_28SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 2)
)
_Dlink_Dgs3420Prod_Dgs3420_28PC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_28PC = _Dlink_Dgs3420Prod_Dgs3420_28PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 3)
)
_Dlink_Dgs3420Prod_Dgs3420_52T_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_52T = _Dlink_Dgs3420Prod_Dgs3420_52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 4)
)
_Dlink_Dgs3420Prod_Dgs3420_52P_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_52P = _Dlink_Dgs3420Prod_Dgs3420_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 5)
)
_Dlink_Dgs3420Prod_Dgs3420_26SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Prod_Dgs3420_26SC = _Dlink_Dgs3420Prod_Dgs3420_26SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 119, 6)
)
_Dlink_Dgs3420Proj_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj = _Dlink_Dgs3420Proj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119)
)
_Dlink_Dgs3420Proj_Dgs3420_28TC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_28TC = _Dlink_Dgs3420Proj_Dgs3420_28TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 1)
)
_Dlink_Dgs3420Proj_Dgs3420_28SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_28SC = _Dlink_Dgs3420Proj_Dgs3420_28SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 2)
)
_Dlink_Dgs3420Proj_Dgs3420_28PC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_28PC = _Dlink_Dgs3420Proj_Dgs3420_28PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 3)
)
_Dlink_Dgs3420Proj_Dgs3420_52T_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_52T = _Dlink_Dgs3420Proj_Dgs3420_52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 4)
)
_Dlink_Dgs3420Proj_Dgs3420_52P_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_52P = _Dlink_Dgs3420Proj_Dgs3420_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 5)
)
_Dlink_Dgs3420Proj_Dgs3420_26SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3420Proj_Dgs3420_26SC = _Dlink_Dgs3420Proj_Dgs3420_26SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 119, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWDGS3420PRIMGMT-MIB",
    **{"dlink-Dgs3420Prod": dlink_Dgs3420Prod,
       "dlink-Dgs3420Prod-Dgs3420-28TC": dlink_Dgs3420Prod_Dgs3420_28TC,
       "dlink-Dgs3420Prod-Dgs3420-28SC": dlink_Dgs3420Prod_Dgs3420_28SC,
       "dlink-Dgs3420Prod-Dgs3420-28PC": dlink_Dgs3420Prod_Dgs3420_28PC,
       "dlink-Dgs3420Prod-Dgs3420-52T": dlink_Dgs3420Prod_Dgs3420_52T,
       "dlink-Dgs3420Prod-Dgs3420-52P": dlink_Dgs3420Prod_Dgs3420_52P,
       "dlink-Dgs3420Prod-Dgs3420-26SC": dlink_Dgs3420Prod_Dgs3420_26SC,
       "dlink-Dgs3420Proj": dlink_Dgs3420Proj,
       "dlink-Dgs3420Proj-Dgs3420-28TC": dlink_Dgs3420Proj_Dgs3420_28TC,
       "dlink-Dgs3420Proj-Dgs3420-28SC": dlink_Dgs3420Proj_Dgs3420_28SC,
       "dlink-Dgs3420Proj-Dgs3420-28PC": dlink_Dgs3420Proj_Dgs3420_28PC,
       "dlink-Dgs3420Proj-Dgs3420-52T": dlink_Dgs3420Proj_Dgs3420_52T,
       "dlink-Dgs3420Proj-Dgs3420-52P": dlink_Dgs3420Proj_Dgs3420_52P,
       "dlink-Dgs3420Proj-Dgs3420-26SC": dlink_Dgs3420Proj_Dgs3420_26SC}
)
