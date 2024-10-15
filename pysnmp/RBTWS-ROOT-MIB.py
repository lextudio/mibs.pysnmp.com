# SNMP MIB module (RBTWS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBTWS-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:31 2024
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

rbtwsRootMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1)
)
rbtwsRootMib.setRevisions(
        ("2005-05-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_CtronTrapeze_ObjectIdentity = ObjectIdentity
ctronTrapeze = _CtronTrapeze_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15)
)
_RbtwsProducts_ObjectIdentity = ObjectIdentity
rbtwsProducts = _RbtwsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 1)
)
_RbtwsTemporary_ObjectIdentity = ObjectIdentity
rbtwsTemporary = _RbtwsTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 2)
)
_RbtwsRegistration_ObjectIdentity = ObjectIdentity
rbtwsRegistration = _RbtwsRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 3)
)
_RbtwsMibs_ObjectIdentity = ObjectIdentity
rbtwsMibs = _RbtwsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4)
)
_RbtwsTraps_ObjectIdentity = ObjectIdentity
rbtwsTraps = _RbtwsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBTWS-ROOT-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctronTrapeze": ctronTrapeze,
       "rbtwsRootMib": rbtwsRootMib,
       "rbtwsProducts": rbtwsProducts,
       "rbtwsTemporary": rbtwsTemporary,
       "rbtwsRegistration": rbtwsRegistration,
       "rbtwsMibs": rbtwsMibs,
       "rbtwsTraps": rbtwsTraps}
)
