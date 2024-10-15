# SNMP MIB module (NTWS-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NTWS-ROOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:50 2024
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

ntwsRootMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1)
)
ntwsRootMib.setRevisions(
        ("2007-08-15 00:04",
         "2006-03-31 00:03",
         "2005-04-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtwsProducts_ObjectIdentity = ObjectIdentity
ntwsProducts = _NtwsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 1)
)
_NtwsTemporary_ObjectIdentity = ObjectIdentity
ntwsTemporary = _NtwsTemporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 2)
)
_NtwsRegistration_ObjectIdentity = ObjectIdentity
ntwsRegistration = _NtwsRegistration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 3)
)
_NtwsMibs_ObjectIdentity = ObjectIdentity
ntwsMibs = _NtwsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 4)
)
_NtwsTraps_ObjectIdentity = ObjectIdentity
ntwsTraps = _NtwsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 6, 1, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTWS-ROOT-MIB",
    **{"ntwsRootMib": ntwsRootMib,
       "ntwsProducts": ntwsProducts,
       "ntwsTemporary": ntwsTemporary,
       "ntwsRegistration": ntwsRegistration,
       "ntwsMibs": ntwsMibs,
       "ntwsTraps": ntwsTraps}
)
