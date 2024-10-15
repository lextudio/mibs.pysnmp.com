# SNMP MIB module (TIARA-NETWORKS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:40 2024
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

(tiaraModules,
 tiaraProducts) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraModules",
    "tiaraProducts")


# MODULE-IDENTITY

tiaraProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 3, 1)
)
tiaraProductsMIB.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tiara1400_ObjectIdentity = ObjectIdentity
tiara1400 = _Tiara1400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 1)
)
_Tiara6100_ObjectIdentity = ObjectIdentity
tiara6100 = _Tiara6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 2)
)
_Tiara6200_ObjectIdentity = ObjectIdentity
tiara6200 = _Tiara6200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 3)
)
_Tiara6300_ObjectIdentity = ObjectIdentity
tiara6300 = _Tiara6300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 4)
)
_Tiara1200_ObjectIdentity = ObjectIdentity
tiara1200 = _Tiara1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 5)
)
_Tiara1250_ObjectIdentity = ObjectIdentity
tiara1250 = _Tiara1250_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 6)
)
_Tiara1450_ObjectIdentity = ObjectIdentity
tiara1450 = _Tiara1450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 7)
)
_Tiara7011_ObjectIdentity = ObjectIdentity
tiara7011 = _Tiara7011_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 8)
)
_Tiara7030_ObjectIdentity = ObjectIdentity
tiara7030 = _Tiara7030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 9)
)
_Tiara7050_ObjectIdentity = ObjectIdentity
tiara7050 = _Tiara7050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 10)
)
_Tiara4100_ObjectIdentity = ObjectIdentity
tiara4100 = _Tiara4100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 1, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-PRODUCTS-MIB",
    **{"tiara1400": tiara1400,
       "tiara6100": tiara6100,
       "tiara6200": tiara6200,
       "tiara6300": tiara6300,
       "tiara1200": tiara1200,
       "tiara1250": tiara1250,
       "tiara1450": tiara1450,
       "tiara7011": tiara7011,
       "tiara7030": tiara7030,
       "tiara7050": tiara7050,
       "tiara4100": tiara4100,
       "tiaraProductsMIB": tiaraProductsMIB}
)
