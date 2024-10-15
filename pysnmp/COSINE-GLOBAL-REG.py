# SNMP MIB module (COSINE-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COSINE-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:06 2024
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

cosineGlobalRegMod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 1, 1, 1)
)
cosineGlobalRegMod.setRevisions(
        ("1998-03-24 13:55",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CsRoot_ObjectIdentity = ObjectIdentity
csRoot = _CsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085)
)
if mibBuilder.loadTexts:
    csRoot.setStatus("current")
_CsReg_ObjectIdentity = ObjectIdentity
csReg = _CsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 1)
)
if mibBuilder.loadTexts:
    csReg.setStatus("current")
_CsModules_ObjectIdentity = ObjectIdentity
csModules = _CsModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 1, 1)
)
if mibBuilder.loadTexts:
    csModules.setStatus("current")
_CsGeneric_ObjectIdentity = ObjectIdentity
csGeneric = _CsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 2)
)
if mibBuilder.loadTexts:
    csGeneric.setStatus("current")
_CsProduct_ObjectIdentity = ObjectIdentity
csProduct = _CsProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3)
)
if mibBuilder.loadTexts:
    csProduct.setStatus("current")
_CsOrionMIB_ObjectIdentity = ObjectIdentity
csOrionMIB = _CsOrionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 1)
)
if mibBuilder.loadTexts:
    csOrionMIB.setStatus("current")
_CsInVisionMIB_ObjectIdentity = ObjectIdentity
csInVisionMIB = _CsInVisionMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 3, 2)
)
if mibBuilder.loadTexts:
    csInVisionMIB.setStatus("current")
_CsCaps_ObjectIdentity = ObjectIdentity
csCaps = _CsCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 4)
)
if mibBuilder.loadTexts:
    csCaps.setStatus("current")
_CsReqs_ObjectIdentity = ObjectIdentity
csReqs = _CsReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 5)
)
if mibBuilder.loadTexts:
    csReqs.setStatus("current")
_CsExpr_ObjectIdentity = ObjectIdentity
csExpr = _CsExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3085, 6)
)
if mibBuilder.loadTexts:
    csExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COSINE-GLOBAL-REG",
    **{"csRoot": csRoot,
       "csReg": csReg,
       "csModules": csModules,
       "cosineGlobalRegMod": cosineGlobalRegMod,
       "csGeneric": csGeneric,
       "csProduct": csProduct,
       "csOrionMIB": csOrionMIB,
       "csInVisionMIB": csInVisionMIB,
       "csCaps": csCaps,
       "csReqs": csReqs,
       "csExpr": csExpr}
)
