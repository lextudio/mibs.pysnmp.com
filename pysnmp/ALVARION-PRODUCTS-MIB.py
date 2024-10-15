# SNMP MIB module (ALVARION-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:39 2024
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

(alvarionModules,
 alvarionProducts) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionModules",
    "alvarionProducts")

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

alvarionProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionWI2CTRL40_ObjectIdentity = ObjectIdentity
alvarionWI2CTRL40 = _AlvarionWI2CTRL40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 25)
)
_AlvarionWI2CTRL200_ObjectIdentity = ObjectIdentity
alvarionWI2CTRL200 = _AlvarionWI2CTRL200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 27)
)
_AlvarionWI2CTRL10_ObjectIdentity = ObjectIdentity
alvarionWI2CTRL10 = _AlvarionWI2CTRL10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 35)
)
_AlvarionWI2SR1_ObjectIdentity = ObjectIdentity
alvarionWI2SR1 = _AlvarionWI2SR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 36)
)
_AlvarionWI2DR1_ObjectIdentity = ObjectIdentity
alvarionWI2DR1 = _AlvarionWI2DR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1, 37)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-PRODUCTS-MIB",
    **{"alvarionWI2CTRL40": alvarionWI2CTRL40,
       "alvarionWI2CTRL200": alvarionWI2CTRL200,
       "alvarionWI2CTRL10": alvarionWI2CTRL10,
       "alvarionWI2SR1": alvarionWI2SR1,
       "alvarionWI2DR1": alvarionWI2DR1,
       "alvarionProductsMIB": alvarionProductsMIB}
)
