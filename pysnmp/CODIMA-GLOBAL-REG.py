# SNMP MIB module (CODIMA-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CODIMA-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:06 2024
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

codimaRegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 1, 1)
)
codimaRegMIB.setRevisions(
        ("2003-05-29 15:50",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codima_ObjectIdentity = ObjectIdentity
codima = _Codima_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226)
)
if mibBuilder.loadTexts:
    codima.setStatus("current")
_CodimaReg_ObjectIdentity = ObjectIdentity
codimaReg = _CodimaReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1)
)
if mibBuilder.loadTexts:
    codimaReg.setStatus("current")
_CodimaModules_ObjectIdentity = ObjectIdentity
codimaModules = _CodimaModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 1)
)
if mibBuilder.loadTexts:
    codimaModules.setStatus("current")
_NetworkManagementProducts_ObjectIdentity = ObjectIdentity
networkManagementProducts = _NetworkManagementProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2)
)
if mibBuilder.loadTexts:
    networkManagementProducts.setStatus("current")
_ExpressConsoleManagerReg_ObjectIdentity = ObjectIdentity
expressConsoleManagerReg = _ExpressConsoleManagerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 1)
)
if mibBuilder.loadTexts:
    expressConsoleManagerReg.setStatus("current")
_ExpressFoundationManagerReg_ObjectIdentity = ObjectIdentity
expressFoundationManagerReg = _ExpressFoundationManagerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 2)
)
if mibBuilder.loadTexts:
    expressFoundationManagerReg.setStatus("current")
_ExpressFProbeReg_ObjectIdentity = ObjectIdentity
expressFProbeReg = _ExpressFProbeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 3)
)
if mibBuilder.loadTexts:
    expressFProbeReg.setStatus("current")
_ExpressSProbeReg_ObjectIdentity = ObjectIdentity
expressSProbeReg = _ExpressSProbeReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 4)
)
if mibBuilder.loadTexts:
    expressSProbeReg.setStatus("current")
_ExpressPortableAnalyzerReg_ObjectIdentity = ObjectIdentity
expressPortableAnalyzerReg = _ExpressPortableAnalyzerReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 5)
)
if mibBuilder.loadTexts:
    expressPortableAnalyzerReg.setStatus("current")
_ExpressDeveloperReg_ObjectIdentity = ObjectIdentity
expressDeveloperReg = _ExpressDeveloperReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 1, 2, 6)
)
if mibBuilder.loadTexts:
    expressDeveloperReg.setStatus("current")
_CodimaGeneric_ObjectIdentity = ObjectIdentity
codimaGeneric = _CodimaGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 2)
)
if mibBuilder.loadTexts:
    codimaGeneric.setStatus("current")
_CodimaProducts_ObjectIdentity = ObjectIdentity
codimaProducts = _CodimaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 3)
)
if mibBuilder.loadTexts:
    codimaProducts.setStatus("current")
_CodimaCaps_ObjectIdentity = ObjectIdentity
codimaCaps = _CodimaCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 4)
)
if mibBuilder.loadTexts:
    codimaCaps.setStatus("current")
_CodimaReqs_ObjectIdentity = ObjectIdentity
codimaReqs = _CodimaReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 5)
)
if mibBuilder.loadTexts:
    codimaReqs.setStatus("current")
_CodimaExpr_ObjectIdentity = ObjectIdentity
codimaExpr = _CodimaExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 226, 6)
)
if mibBuilder.loadTexts:
    codimaExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CODIMA-GLOBAL-REG",
    **{"codima": codima,
       "codimaReg": codimaReg,
       "codimaModules": codimaModules,
       "codimaRegMIB": codimaRegMIB,
       "networkManagementProducts": networkManagementProducts,
       "expressConsoleManagerReg": expressConsoleManagerReg,
       "expressFoundationManagerReg": expressFoundationManagerReg,
       "expressFProbeReg": expressFProbeReg,
       "expressSProbeReg": expressSProbeReg,
       "expressPortableAnalyzerReg": expressPortableAnalyzerReg,
       "expressDeveloperReg": expressDeveloperReg,
       "codimaGeneric": codimaGeneric,
       "codimaProducts": codimaProducts,
       "codimaCaps": codimaCaps,
       "codimaReqs": codimaReqs,
       "codimaExpr": codimaExpr}
)
