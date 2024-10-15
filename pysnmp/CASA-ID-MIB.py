# SNMP MIB module (CASA-ID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CASA-ID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:40 2024
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

(casa,) = mibBuilder.importSymbols(
    "CASA-MIB",
    "casa")

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

casaIdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2)
)
casaIdMib.setRevisions(
        ("1900-04-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Casa2100System_ObjectIdentity = ObjectIdentity
casa2100System = _Casa2100System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 1)
)
_Casa2200System_ObjectIdentity = ObjectIdentity
casa2200System = _Casa2200System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 20)
)
_Casa2300System_ObjectIdentity = ObjectIdentity
casa2300System = _Casa2300System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 30)
)
_Casa2800System_ObjectIdentity = ObjectIdentity
casa2800System = _Casa2800System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 40)
)
_Casa3000System_ObjectIdentity = ObjectIdentity
casa3000System = _Casa3000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 50)
)
_Casa6000System_ObjectIdentity = ObjectIdentity
casa6000System = _Casa6000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 100)
)
_Casa10000System_ObjectIdentity = ObjectIdentity
casa10000System = _Casa10000System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20858, 2, 200)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CASA-ID-MIB",
    **{"casaIdMib": casaIdMib,
       "casa2100System": casa2100System,
       "casa2200System": casa2200System,
       "casa2300System": casa2300System,
       "casa2800System": casa2800System,
       "casa3000System": casa3000System,
       "casa6000System": casa6000System,
       "casa10000System": casa10000System}
)
