# SNMP MIB module (SW34XXPRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW34XXPRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:42 2024
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

_Dlink_ProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dlink_ProjectXStackIISeriesProd = _Dlink_ProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70)
)
_Dlink_Dgs3426_ObjectIdentity = ObjectIdentity
dlink_Dgs3426 = _Dlink_Dgs3426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 1)
)
_Dlink_Dgs3427_ObjectIdentity = ObjectIdentity
dlink_Dgs3427 = _Dlink_Dgs3427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 2)
)
_Dlink_Dgs3450_ObjectIdentity = ObjectIdentity
dlink_Dgs3450 = _Dlink_Dgs3450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 3)
)
_Dlink_Dgs3426p_ObjectIdentity = ObjectIdentity
dlink_Dgs3426p = _Dlink_Dgs3426p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 7)
)
_Dlink_Dgs3426g_ObjectIdentity = ObjectIdentity
dlink_Dgs3426g = _Dlink_Dgs3426g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 70, 11)
)
_DgsProjectXStackIISeriesProd_ObjectIdentity = ObjectIdentity
dgsProjectXStackIISeriesProd = _DgsProjectXStackIISeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70)
)
_Dgs3426_ObjectIdentity = ObjectIdentity
dgs3426 = _Dgs3426_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 1)
)
_Dgs3427_ObjectIdentity = ObjectIdentity
dgs3427 = _Dgs3427_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 2)
)
_Dgs3450_ObjectIdentity = ObjectIdentity
dgs3450 = _Dgs3450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 3)
)
_Dgs3426p_ObjectIdentity = ObjectIdentity
dgs3426p = _Dgs3426p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 7)
)
_Dgs3426g_ObjectIdentity = ObjectIdentity
dgs3426g = _Dgs3426g_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 70, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW34XXPRIMGMT-MIB",
    **{"dlink-ProjectXStackIISeriesProd": dlink_ProjectXStackIISeriesProd,
       "dlink-Dgs3426": dlink_Dgs3426,
       "dlink-Dgs3427": dlink_Dgs3427,
       "dlink-Dgs3450": dlink_Dgs3450,
       "dlink-Dgs3426p": dlink_Dgs3426p,
       "dlink-Dgs3426g": dlink_Dgs3426g,
       "dgsProjectXStackIISeriesProd": dgsProjectXStackIISeriesProd,
       "dgs3426": dgs3426,
       "dgs3427": dgs3427,
       "dgs3450": dgs3450,
       "dgs3426p": dgs3426p,
       "dgs3426g": dgs3426g}
)
