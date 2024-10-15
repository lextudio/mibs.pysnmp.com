# SNMP MIB module (SW3500PRIMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW3500PRIMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:36 2024
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

_Dlink_des3500SeriesProd_ObjectIdentity = ObjectIdentity
dlink_des3500SeriesProd = _Dlink_des3500SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 64)
)
_Dlink_des3526Prod_ObjectIdentity = ObjectIdentity
dlink_des3526Prod = _Dlink_des3526Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 64, 1)
)
_Dlink_des3550Prod_ObjectIdentity = ObjectIdentity
dlink_des3550Prod = _Dlink_des3550Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 64, 2)
)
_Des3500SeriesProd_ObjectIdentity = ObjectIdentity
des3500SeriesProd = _Des3500SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 64)
)
_Des3526_ObjectIdentity = ObjectIdentity
des3526 = _Des3526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 64, 1)
)
_Des3550_ObjectIdentity = ObjectIdentity
des3550 = _Des3550_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 64, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW3500PRIMGMT-MIB",
    **{"dlink-des3500SeriesProd": dlink_des3500SeriesProd,
       "dlink-des3526Prod": dlink_des3526Prod,
       "dlink-des3550Prod": dlink_des3550Prod,
       "des3500SeriesProd": des3500SeriesProd,
       "des3526": des3526,
       "des3550": des3550}
)
