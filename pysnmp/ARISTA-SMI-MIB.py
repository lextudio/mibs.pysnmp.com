# SNMP MIB module (ARISTA-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:15 2024
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

arista = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065)
)
arista.setRevisions(
        ("2014-08-15 00:00",
         "2011-03-31 13:00",
         "2008-10-27 18:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaProducts_ObjectIdentity = ObjectIdentity
aristaProducts = _AristaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1)
)
if mibBuilder.loadTexts:
    aristaProducts.setStatus("current")
_AristaModules_ObjectIdentity = ObjectIdentity
aristaModules = _AristaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 2)
)
if mibBuilder.loadTexts:
    aristaModules.setStatus("current")
_AristaMibs_ObjectIdentity = ObjectIdentity
aristaMibs = _AristaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3)
)
if mibBuilder.loadTexts:
    aristaMibs.setStatus("current")
_AristaExperiment_ObjectIdentity = ObjectIdentity
aristaExperiment = _AristaExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 4)
)
if mibBuilder.loadTexts:
    aristaExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-SMI-MIB",
    **{"arista": arista,
       "aristaProducts": aristaProducts,
       "aristaModules": aristaModules,
       "aristaMibs": aristaMibs,
       "aristaExperiment": aristaExperiment}
)
