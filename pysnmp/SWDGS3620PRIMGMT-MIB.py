# SNMP MIB module (SWDGS3620PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWDGS3620PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:30 2024
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

_Dlink_Dgs3620Prod_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod = _Dlink_Dgs3620Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118)
)
_Dlink_Dgs3620Prod_Dgs3620_28TC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_28TC = _Dlink_Dgs3620Prod_Dgs3620_28TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 1)
)
_Dlink_Dgs3620Prod_Dgs3620_28SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_28SC = _Dlink_Dgs3620Prod_Dgs3620_28SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 2)
)
_Dlink_Dgs3620Prod_Dgs3620_28PC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_28PC = _Dlink_Dgs3620Prod_Dgs3620_28PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 3)
)
_Dlink_Dgs3620Prod_Dgs3620_52T_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_52T = _Dlink_Dgs3620Prod_Dgs3620_52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 4)
)
_Dlink_Dgs3620Prod_Dgs3620_52P_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_52P = _Dlink_Dgs3620Prod_Dgs3620_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 5)
)
_Dlink_Dgs3620Prod_Dgs3620_28TC_DC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_28TC_DC = _Dlink_Dgs3620Prod_Dgs3620_28TC_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 8)
)
_Dlink_Dgs3620Prod_Dgs3620_28SC_DC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Prod_Dgs3620_28SC_DC = _Dlink_Dgs3620Prod_Dgs3620_28SC_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 118, 9)
)
_Dlink_Dgs3620Proj_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj = _Dlink_Dgs3620Proj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118)
)
_Dlink_Dgs3620Proj_Dgs3620_28TC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_28TC = _Dlink_Dgs3620Proj_Dgs3620_28TC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 1)
)
_Dlink_Dgs3620Proj_Dgs3620_28SC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_28SC = _Dlink_Dgs3620Proj_Dgs3620_28SC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 2)
)
_Dlink_Dgs3620Proj_Dgs3620_28PC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_28PC = _Dlink_Dgs3620Proj_Dgs3620_28PC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 3)
)
_Dlink_Dgs3620Proj_Dgs3620_52T_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_52T = _Dlink_Dgs3620Proj_Dgs3620_52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 4)
)
_Dlink_Dgs3620Proj_Dgs3620_52P_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_52P = _Dlink_Dgs3620Proj_Dgs3620_52P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 5)
)
_Dlink_Dgs3620Proj_Dgs3620_28TC_DC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_28TC_DC = _Dlink_Dgs3620Proj_Dgs3620_28TC_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 8)
)
_Dlink_Dgs3620Proj_Dgs3620_28SC_DC_ObjectIdentity = ObjectIdentity
dlink_Dgs3620Proj_Dgs3620_28SC_DC = _Dlink_Dgs3620Proj_Dgs3620_28SC_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 118, 9)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWDGS3620PRIMGMT-MIB",
    **{"dlink-Dgs3620Prod": dlink_Dgs3620Prod,
       "dlink-Dgs3620Prod-Dgs3620-28TC": dlink_Dgs3620Prod_Dgs3620_28TC,
       "dlink-Dgs3620Prod-Dgs3620-28SC": dlink_Dgs3620Prod_Dgs3620_28SC,
       "dlink-Dgs3620Prod-Dgs3620-28PC": dlink_Dgs3620Prod_Dgs3620_28PC,
       "dlink-Dgs3620Prod-Dgs3620-52T": dlink_Dgs3620Prod_Dgs3620_52T,
       "dlink-Dgs3620Prod-Dgs3620-52P": dlink_Dgs3620Prod_Dgs3620_52P,
       "dlink-Dgs3620Prod-Dgs3620-28TC-DC": dlink_Dgs3620Prod_Dgs3620_28TC_DC,
       "dlink-Dgs3620Prod-Dgs3620-28SC-DC": dlink_Dgs3620Prod_Dgs3620_28SC_DC,
       "dlink-Dgs3620Proj": dlink_Dgs3620Proj,
       "dlink-Dgs3620Proj-Dgs3620-28TC": dlink_Dgs3620Proj_Dgs3620_28TC,
       "dlink-Dgs3620Proj-Dgs3620-28SC": dlink_Dgs3620Proj_Dgs3620_28SC,
       "dlink-Dgs3620Proj-Dgs3620-28PC": dlink_Dgs3620Proj_Dgs3620_28PC,
       "dlink-Dgs3620Proj-Dgs3620-52T": dlink_Dgs3620Proj_Dgs3620_52T,
       "dlink-Dgs3620Proj-Dgs3620-52P": dlink_Dgs3620Proj_Dgs3620_52P,
       "dlink-Dgs3620Proj-Dgs3620-28TC-DC": dlink_Dgs3620Proj_Dgs3620_28TC_DC,
       "dlink-Dgs3620Proj-Dgs3620-28SC-DC": dlink_Dgs3620Proj_Dgs3620_28SC_DC}
)
