# SNMP MIB module (COLUBRIS-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:09 2024
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

colubris = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisProducts_ObjectIdentity = ObjectIdentity
colubrisProducts = _ColubrisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 1)
)
if mibBuilder.loadTexts:
    colubrisProducts.setStatus("current")
_ColubrisMgmt_ObjectIdentity = ObjectIdentity
colubrisMgmt = _ColubrisMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 2)
)
if mibBuilder.loadTexts:
    colubrisMgmt.setStatus("deprecated")
_ColubrisExperiment_ObjectIdentity = ObjectIdentity
colubrisExperiment = _ColubrisExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 3)
)
if mibBuilder.loadTexts:
    colubrisExperiment.setStatus("current")
_ColubrisModules_ObjectIdentity = ObjectIdentity
colubrisModules = _ColubrisModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 4)
)
if mibBuilder.loadTexts:
    colubrisModules.setStatus("current")
_ColubrisMgmtV2_ObjectIdentity = ObjectIdentity
colubrisMgmtV2 = _ColubrisMgmtV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5)
)
if mibBuilder.loadTexts:
    colubrisMgmtV2.setStatus("current")
_Extensions_ObjectIdentity = ObjectIdentity
extensions = _Extensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 6)
)
if mibBuilder.loadTexts:
    extensions.setStatus("current")
_Variation_ObjectIdentity = ObjectIdentity
variation = _Variation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 7)
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
    "COLUBRIS-SMI",
    **{"colubris": colubris,
       "colubrisProducts": colubrisProducts,
       "colubrisMgmt": colubrisMgmt,
       "colubrisExperiment": colubrisExperiment,
       "colubrisModules": colubrisModules,
       "colubrisMgmtV2": colubrisMgmtV2,
       "extensions": extensions,
       "variation": variation}
)
