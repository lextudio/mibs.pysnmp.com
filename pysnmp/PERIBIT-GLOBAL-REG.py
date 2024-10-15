# SNMP MIB module (PERIBIT-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PERIBIT-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:25 2024
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

pnGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 1)
)
pnGlobalRegModule.setRevisions(
        ("2004-03-15 14:00",
         "2003-06-26 20:00",
         "2001-07-29 22:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PeribitRoot_ObjectIdentity = ObjectIdentity
peribitRoot = _PeribitRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239)
)
if mibBuilder.loadTexts:
    peribitRoot.setStatus("current")
_PnReg_ObjectIdentity = ObjectIdentity
pnReg = _PnReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1)
)
if mibBuilder.loadTexts:
    pnReg.setStatus("current")
_PnModules_ObjectIdentity = ObjectIdentity
pnModules = _PnModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1)
)
if mibBuilder.loadTexts:
    pnModules.setStatus("current")
_PnProductSr_ObjectIdentity = ObjectIdentity
pnProductSr = _PnProductSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2)
)
if mibBuilder.loadTexts:
    pnProductSr.setStatus("current")
_PnProductSr50_ObjectIdentity = ObjectIdentity
pnProductSr50 = _PnProductSr50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pnProductSr50.setStatus("current")
_PnProductSr55_ObjectIdentity = ObjectIdentity
pnProductSr55 = _PnProductSr55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pnProductSr55.setStatus("current")
_PnProductSr20_ObjectIdentity = ObjectIdentity
pnProductSr20 = _PnProductSr20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pnProductSr20.setStatus("current")
_PnProductSr80_ObjectIdentity = ObjectIdentity
pnProductSr80 = _PnProductSr80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pnProductSr80.setStatus("current")
_PnProductSr100_ObjectIdentity = ObjectIdentity
pnProductSr100 = _PnProductSr100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 5)
)
if mibBuilder.loadTexts:
    pnProductSr100.setStatus("current")
_PnProductSm500_ObjectIdentity = ObjectIdentity
pnProductSm500 = _PnProductSm500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 6)
)
if mibBuilder.loadTexts:
    pnProductSm500.setStatus("current")
_PnProductSr15_ObjectIdentity = ObjectIdentity
pnProductSr15 = _PnProductSr15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 2, 7)
)
if mibBuilder.loadTexts:
    pnProductSr15.setStatus("current")
_PnMibs_ObjectIdentity = ObjectIdentity
pnMibs = _PnMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2)
)
if mibBuilder.loadTexts:
    pnMibs.setStatus("current")
_PnCommonMib_ObjectIdentity = ObjectIdentity
pnCommonMib = _PnCommonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 1)
)
if mibBuilder.loadTexts:
    pnCommonMib.setStatus("current")
_PnSpecificMib_ObjectIdentity = ObjectIdentity
pnSpecificMib = _PnSpecificMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2)
)
if mibBuilder.loadTexts:
    pnSpecificMib.setStatus("current")
_PnCaps_ObjectIdentity = ObjectIdentity
pnCaps = _PnCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 3)
)
if mibBuilder.loadTexts:
    pnCaps.setStatus("current")
_PnReqs_ObjectIdentity = ObjectIdentity
pnReqs = _PnReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 4)
)
if mibBuilder.loadTexts:
    pnReqs.setStatus("current")
_PnExpr_ObjectIdentity = ObjectIdentity
pnExpr = _PnExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 5)
)
if mibBuilder.loadTexts:
    pnExpr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERIBIT-GLOBAL-REG",
    **{"peribitRoot": peribitRoot,
       "pnReg": pnReg,
       "pnModules": pnModules,
       "pnGlobalRegModule": pnGlobalRegModule,
       "pnProductSr": pnProductSr,
       "pnProductSr50": pnProductSr50,
       "pnProductSr55": pnProductSr55,
       "pnProductSr20": pnProductSr20,
       "pnProductSr80": pnProductSr80,
       "pnProductSr100": pnProductSr100,
       "pnProductSm500": pnProductSm500,
       "pnProductSr15": pnProductSr15,
       "pnMibs": pnMibs,
       "pnCommonMib": pnCommonMib,
       "pnSpecificMib": pnSpecificMib,
       "pnCaps": pnCaps,
       "pnReqs": pnReqs,
       "pnExpr": pnExpr}
)
