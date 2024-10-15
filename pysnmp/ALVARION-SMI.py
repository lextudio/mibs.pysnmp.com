# SNMP MIB module (ALVARION-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:28 2024
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

alvarionWireless = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionProducts_ObjectIdentity = ObjectIdentity
alvarionProducts = _AlvarionProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 1)
)
if mibBuilder.loadTexts:
    alvarionProducts.setStatus("current")
_AlvarionExperiment_ObjectIdentity = ObjectIdentity
alvarionExperiment = _AlvarionExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 3)
)
if mibBuilder.loadTexts:
    alvarionExperiment.setStatus("current")
_AlvarionModules_ObjectIdentity = ObjectIdentity
alvarionModules = _AlvarionModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 4)
)
if mibBuilder.loadTexts:
    alvarionModules.setStatus("current")
_AlvarionMgmtV2_ObjectIdentity = ObjectIdentity
alvarionMgmtV2 = _AlvarionMgmtV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5)
)
if mibBuilder.loadTexts:
    alvarionMgmtV2.setStatus("current")
_Variation_ObjectIdentity = ObjectIdentity
variation = _Variation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 7)
)
if mibBuilder.loadTexts:
    variation.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-SMI",
    **{"alvarionWireless": alvarionWireless,
       "alvarionProducts": alvarionProducts,
       "alvarionExperiment": alvarionExperiment,
       "alvarionModules": alvarionModules,
       "alvarionMgmtV2": alvarionMgmtV2,
       "variation": variation}
)
