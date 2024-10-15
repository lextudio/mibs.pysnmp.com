# SNMP MIB module (INCOGNITO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INCOGNITO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:04 2024
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

incognito = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3606)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IncognitoSNMPObjects_ObjectIdentity = ObjectIdentity
incognitoSNMPObjects = _IncognitoSNMPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 1)
)
if mibBuilder.loadTexts:
    incognitoSNMPObjects.setStatus("obsolete")
_IncognitoReg_ObjectIdentity = ObjectIdentity
incognitoReg = _IncognitoReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 2)
)
if mibBuilder.loadTexts:
    incognitoReg.setStatus("current")
_IncognitoGeneric_ObjectIdentity = ObjectIdentity
incognitoGeneric = _IncognitoGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 3)
)
if mibBuilder.loadTexts:
    incognitoGeneric.setStatus("current")
_IncognitoProducts_ObjectIdentity = ObjectIdentity
incognitoProducts = _IncognitoProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 4)
)
if mibBuilder.loadTexts:
    incognitoProducts.setStatus("current")
_IncognitoCaps_ObjectIdentity = ObjectIdentity
incognitoCaps = _IncognitoCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 5)
)
if mibBuilder.loadTexts:
    incognitoCaps.setStatus("current")
_IncognitoReqs_ObjectIdentity = ObjectIdentity
incognitoReqs = _IncognitoReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 6)
)
if mibBuilder.loadTexts:
    incognitoReqs.setStatus("current")
_IncognitoExpr_ObjectIdentity = ObjectIdentity
incognitoExpr = _IncognitoExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3606, 7)
)
if mibBuilder.loadTexts:
    incognitoExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INCOGNITO-MIB",
    **{"incognito": incognito,
       "incognitoSNMPObjects": incognitoSNMPObjects,
       "incognitoReg": incognitoReg,
       "incognitoGeneric": incognitoGeneric,
       "incognitoProducts": incognitoProducts,
       "incognitoCaps": incognitoCaps,
       "incognitoReqs": incognitoReqs,
       "incognitoExpr": incognitoExpr}
)
