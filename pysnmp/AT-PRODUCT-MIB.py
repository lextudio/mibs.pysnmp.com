# SNMP MIB module (AT-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-PRODUCT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:29 2024
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

(alliedTelesis,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "alliedTelesis")

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

products = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
products.setRevisions(
        ("2013-08-01 00:00",
         "2013-07-09 00:00",
         "2013-04-02 00:00",
         "2012-03-22 00:00",
         "2011-12-18 05:00",
         "2011-09-15 00:00",
         "2011-09-14 00:00",
         "2011-09-05 00:00",
         "2011-04-04 00:00",
         "2010-10-12 00:00",
         "2010-09-20 00:00",
         "2010-09-07 00:00",
         "2010-08-19 00:00",
         "2010-07-22 00:00",
         "2010-06-15 00:15",
         "2009-05-19 00:00",
         "2009-05-15 00:00",
         "2008-03-06 13:00",
         "2007-11-15 00:00",
         "2007-03-21 00:00",
         "2007-02-07 00:00",
         "2006-06-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BridgeRouter_ObjectIdentity = ObjectIdentity
bridgeRouter = _BridgeRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1)
)
if mibBuilder.loadTexts:
    bridgeRouter.setStatus("current")
_CentreCOM_AR300Router_ObjectIdentity = ObjectIdentity
centreCOM_AR300Router = _CentreCOM_AR300Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 8)
)
_CentreCOM_AR720Router_ObjectIdentity = ObjectIdentity
centreCOM_AR720Router = _CentreCOM_AR720Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 11)
)
_CentreCOM_AR300LRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300LRouter = _CentreCOM_AR300LRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 12)
)
_CentreCOM_AR310Router_ObjectIdentity = ObjectIdentity
centreCOM_AR310Router = _CentreCOM_AR310Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 13)
)
_CentreCOM_AR300LURouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300LURouter = _CentreCOM_AR300LURouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 14)
)
_CentreCOM_AR300URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR300URouter = _CentreCOM_AR300URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 15)
)
_CentreCOM_AR310URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR310URouter = _CentreCOM_AR310URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 16)
)
_CentreCOM_AR350Router_ObjectIdentity = ObjectIdentity
centreCOM_AR350Router = _CentreCOM_AR350Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 17)
)
_CentreCOM_AR370Router_ObjectIdentity = ObjectIdentity
centreCOM_AR370Router = _CentreCOM_AR370Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 18)
)
_CentreCOM_AR330Router_ObjectIdentity = ObjectIdentity
centreCOM_AR330Router = _CentreCOM_AR330Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 19)
)
_CentreCOM_AR395Router_ObjectIdentity = ObjectIdentity
centreCOM_AR395Router = _CentreCOM_AR395Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 20)
)
_CentreCOM_AR390Router_ObjectIdentity = ObjectIdentity
centreCOM_AR390Router = _CentreCOM_AR390Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 21)
)
_CentreCOM_AR370URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR370URouter = _CentreCOM_AR370URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 22)
)
_CentreCOM_AR740Router_ObjectIdentity = ObjectIdentity
centreCOM_AR740Router = _CentreCOM_AR740Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 23)
)
_CentreCOM_AR140SRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR140SRouter = _CentreCOM_AR140SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 24)
)
_CentreCOM_AR140URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR140URouter = _CentreCOM_AR140URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 25)
)
_CentreCOM_AR320Router_ObjectIdentity = ObjectIdentity
centreCOM_AR320Router = _CentreCOM_AR320Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 26)
)
_CentreCOM_AR130SRouter_ObjectIdentity = ObjectIdentity
centreCOM_AR130SRouter = _CentreCOM_AR130SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 27)
)
_CentreCOM_AR130URouter_ObjectIdentity = ObjectIdentity
centreCOM_AR130URouter = _CentreCOM_AR130URouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 28)
)
_CentreCOM_AR160Router_ObjectIdentity = ObjectIdentity
centreCOM_AR160Router = _CentreCOM_AR160Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 29)
)
_At_AR740RouterDC_ObjectIdentity = ObjectIdentity
at_AR740RouterDC = _At_AR740RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 43)
)
_CentreCOM_AR120Router_ObjectIdentity = ObjectIdentity
centreCOM_AR120Router = _CentreCOM_AR120Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 44)
)
_At_AR410Router_ObjectIdentity = ObjectIdentity
at_AR410Router = _At_AR410Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 47)
)
_At_AR725Router_ObjectIdentity = ObjectIdentity
at_AR725Router = _At_AR725Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 48)
)
_At_AR745Router_ObjectIdentity = ObjectIdentity
at_AR745Router = _At_AR745Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 49)
)
_At_AR410v2Router_ObjectIdentity = ObjectIdentity
at_AR410v2Router = _At_AR410v2Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 50)
)
_At_AR410v3Router_ObjectIdentity = ObjectIdentity
at_AR410v3Router = _At_AR410v3Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 51)
)
_At_AR725RouterDC_ObjectIdentity = ObjectIdentity
at_AR725RouterDC = _At_AR725RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 52)
)
_At_AR745RouterDC_ObjectIdentity = ObjectIdentity
at_AR745RouterDC = _At_AR745RouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 53)
)
_At_AR450Router_ObjectIdentity = ObjectIdentity
at_AR450Router = _At_AR450Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 54)
)
_At_AR450DualRouter_ObjectIdentity = ObjectIdentity
at_AR450DualRouter = _At_AR450DualRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 55)
)
_At_AR440Router_ObjectIdentity = ObjectIdentity
at_AR440Router = _At_AR440Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 59)
)
_At_AR441Router_ObjectIdentity = ObjectIdentity
at_AR441Router = _At_AR441Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 60)
)
_At_AR442Router_ObjectIdentity = ObjectIdentity
at_AR442Router = _At_AR442Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 61)
)
_At_AR443Router_ObjectIdentity = ObjectIdentity
at_AR443Router = _At_AR443Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 62)
)
_At_AR444Router_ObjectIdentity = ObjectIdentity
at_AR444Router = _At_AR444Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 63)
)
_At_AR420Router_ObjectIdentity = ObjectIdentity
at_AR420Router = _At_AR420Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 64)
)
_At_AR415SRouter_ObjectIdentity = ObjectIdentity
at_AR415SRouter = _At_AR415SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 71)
)
_At_AR415SRouterDC_ObjectIdentity = ObjectIdentity
at_AR415SRouterDC = _At_AR415SRouterDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 72)
)
_At_AR550Router_ObjectIdentity = ObjectIdentity
at_AR550Router = _At_AR550Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 73)
)
_At_AR551Router_ObjectIdentity = ObjectIdentity
at_AR551Router = _At_AR551Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 74)
)
_At_AR552Router_ObjectIdentity = ObjectIdentity
at_AR552Router = _At_AR552Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 75)
)
_At_AR550SRouterDP_ObjectIdentity = ObjectIdentity
at_AR550SRouterDP = _At_AR550SRouterDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 76)
)
_At_AR570Router_ObjectIdentity = ObjectIdentity
at_AR570Router = _At_AR570Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 78)
)
_At_AR770Router_ObjectIdentity = ObjectIdentity
at_AR770Router = _At_AR770Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 79)
)
_At_AR750SRouterDP_ObjectIdentity = ObjectIdentity
at_AR750SRouterDP = _At_AR750SRouterDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 80)
)
_At_AR560SRouter_ObjectIdentity = ObjectIdentity
at_AR560SRouter = _At_AR560SRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 1, 81)
)
_Swhub_ObjectIdentity = ObjectIdentity
swhub = _Swhub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
if mibBuilder.loadTexts:
    swhub.setStatus("current")
_At_x200_GE52T_ObjectIdentity = ObjectIdentity
at_x200_GE52T = _At_x200_GE52T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 181)
)
_At_x200_GE28T_ObjectIdentity = ObjectIdentity
at_x200_GE28T = _At_x200_GE28T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 182)
)
_At_x210_9GT_ObjectIdentity = ObjectIdentity
at_x210_9GT = _At_x210_9GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 196)
)
_At_x210_16GT_ObjectIdentity = ObjectIdentity
at_x210_16GT = _At_x210_16GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 197)
)
_At_x210_24GT_ObjectIdentity = ObjectIdentity
at_x210_24GT = _At_x210_24GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 198)
)
_At_x310_26FT_ObjectIdentity = ObjectIdentity
at_x310_26FT = _At_x310_26FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 216)
)
_At_x310_50FT_ObjectIdentity = ObjectIdentity
at_x310_50FT = _At_x310_50FT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 217)
)
_At_x310_26FP_ObjectIdentity = ObjectIdentity
at_x310_26FP = _At_x310_26FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 218)
)
_At_x310_50FP_ObjectIdentity = ObjectIdentity
at_x310_50FP = _At_x310_50FP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 219)
)
_At_x310_26GT_ObjectIdentity = ObjectIdentity
at_x310_26GT = _At_x310_26GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 220)
)
_At_x310_50GT_ObjectIdentity = ObjectIdentity
at_x310_50GT = _At_x310_50GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 221)
)
_At_x310_26GP_ObjectIdentity = ObjectIdentity
at_x310_26GP = _At_x310_26GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 222)
)
_At_x310_50GP_ObjectIdentity = ObjectIdentity
at_x310_50GP = _At_x310_50GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 223)
)
_At_x230_10GT_ObjectIdentity = ObjectIdentity
at_x230_10GT = _At_x230_10GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 224)
)
_At_x230_18GT_ObjectIdentity = ObjectIdentity
at_x230_18GT = _At_x230_18GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 225)
)
_At_x230_28GT_ObjectIdentity = ObjectIdentity
at_x230_28GT = _At_x230_28GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 226)
)
_At_x230_52GT_ObjectIdentity = ObjectIdentity
at_x230_52GT = _At_x230_52GT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 227)
)
_At_x230_10GP_ObjectIdentity = ObjectIdentity
at_x230_10GP = _At_x230_10GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 228)
)
_At_x230_18GP_ObjectIdentity = ObjectIdentity
at_x230_18GP = _At_x230_18GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 229)
)
_At_x230_28GP_ObjectIdentity = ObjectIdentity
at_x230_28GP = _At_x230_28GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 230)
)
_At_x230_52GP_ObjectIdentity = ObjectIdentity
at_x230_52GP = _At_x230_52GP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 231)
)
_At_x230_10GPT_ObjectIdentity = ObjectIdentity
at_x230_10GPT = _At_x230_10GPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 232)
)
_RouterSwitch_ObjectIdentity = ObjectIdentity
routerSwitch = _RouterSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14)
)
if mibBuilder.loadTexts:
    routerSwitch.setStatus("current")
_At_Rapier24_ObjectIdentity = ObjectIdentity
at_Rapier24 = _At_Rapier24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 1)
)
_At_Rapier16fSC_ObjectIdentity = ObjectIdentity
at_Rapier16fSC = _At_Rapier16fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 2)
)
_At_Rapier16fVF_ObjectIdentity = ObjectIdentity
at_Rapier16fVF = _At_Rapier16fVF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 3)
)
_At_Rapier16fMT_ObjectIdentity = ObjectIdentity
at_Rapier16fMT = _At_Rapier16fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 4)
)
_At_Rapier48_ObjectIdentity = ObjectIdentity
at_Rapier48 = _At_Rapier48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 5)
)
_At_Rapier8t8fSC_ObjectIdentity = ObjectIdentity
at_Rapier8t8fSC = _At_Rapier8t8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 6)
)
_At_Rapier8t8fSCi_ObjectIdentity = ObjectIdentity
at_Rapier8t8fSCi = _At_Rapier8t8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 7)
)
_At_Rapier8t8fMT_ObjectIdentity = ObjectIdentity
at_Rapier8t8fMT = _At_Rapier8t8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 8)
)
_At_Rapier8t8fMTi_ObjectIdentity = ObjectIdentity
at_Rapier8t8fMTi = _At_Rapier8t8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 9)
)
_At_Rapier8fSC_ObjectIdentity = ObjectIdentity
at_Rapier8fSC = _At_Rapier8fSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 10)
)
_At_Rapier8fSCi_ObjectIdentity = ObjectIdentity
at_Rapier8fSCi = _At_Rapier8fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 11)
)
_At_Rapier8fMT_ObjectIdentity = ObjectIdentity
at_Rapier8fMT = _At_Rapier8fMT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 12)
)
_At_Rapier8fMTi_ObjectIdentity = ObjectIdentity
at_Rapier8fMTi = _At_Rapier8fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 13)
)
_At_Rapier16fMTi_ObjectIdentity = ObjectIdentity
at_Rapier16fMTi = _At_Rapier16fMTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 14)
)
_At_RapierG6_ObjectIdentity = ObjectIdentity
at_RapierG6 = _At_RapierG6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 15)
)
_At_RapierG6SX_ObjectIdentity = ObjectIdentity
at_RapierG6SX = _At_RapierG6SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 16)
)
_At_RapierG6LX_ObjectIdentity = ObjectIdentity
at_RapierG6LX = _At_RapierG6LX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 17)
)
_At_RapierG6MT_ObjectIdentity = ObjectIdentity
at_RapierG6MT = _At_RapierG6MT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 18)
)
_At_Rapier16fSCi_ObjectIdentity = ObjectIdentity
at_Rapier16fSCi = _At_Rapier16fSCi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 19)
)
_At_Rapier24i_ObjectIdentity = ObjectIdentity
at_Rapier24i = _At_Rapier24i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 20)
)
_At_Rapier48i_ObjectIdentity = ObjectIdentity
at_Rapier48i = _At_Rapier48i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 21)
)
_At_Switchblade4AC_ObjectIdentity = ObjectIdentity
at_Switchblade4AC = _At_Switchblade4AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 22)
)
_At_Switchblade4DC_ObjectIdentity = ObjectIdentity
at_Switchblade4DC = _At_Switchblade4DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 23)
)
_At_Switchblade8AC_ObjectIdentity = ObjectIdentity
at_Switchblade8AC = _At_Switchblade8AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 24)
)
_At_Switchblade8DC_ObjectIdentity = ObjectIdentity
at_Switchblade8DC = _At_Switchblade8DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 25)
)
_At_9816GF_ObjectIdentity = ObjectIdentity
at_9816GF = _At_9816GF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 26)
)
_At_9812TF_ObjectIdentity = ObjectIdentity
at_9812TF = _At_9812TF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 27)
)
_At_9816GB_ObjectIdentity = ObjectIdentity
at_9816GB = _At_9816GB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 28)
)
_At_9812T_ObjectIdentity = ObjectIdentity
at_9812T = _At_9812T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 29)
)
_At_8724XL_ObjectIdentity = ObjectIdentity
at_8724XL = _At_8724XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 30)
)
_At_8748XL_ObjectIdentity = ObjectIdentity
at_8748XL = _At_8748XL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 31)
)
_At_8724XLDC_ObjectIdentity = ObjectIdentity
at_8724XLDC = _At_8724XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 32)
)
_At_8748XLDC_ObjectIdentity = ObjectIdentity
at_8748XLDC = _At_8748XLDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 33)
)
_At_9816GB_DC_ObjectIdentity = ObjectIdentity
at_9816GB_DC = _At_9816GB_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 34)
)
_At_9812T_DC_ObjectIdentity = ObjectIdentity
at_9812T_DC = _At_9812T_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 35)
)
_At_8824_ObjectIdentity = ObjectIdentity
at_8824 = _At_8824_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 36)
)
_At_8848_ObjectIdentity = ObjectIdentity
at_8848 = _At_8848_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 37)
)
_At_8824_DC_ObjectIdentity = ObjectIdentity
at_8824_DC = _At_8824_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 38)
)
_At_8848_DC_ObjectIdentity = ObjectIdentity
at_8848_DC = _At_8848_DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 39)
)
_At_8624XL_80_ObjectIdentity = ObjectIdentity
at_8624XL_80 = _At_8624XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 41)
)
_At_8724XL_80_ObjectIdentity = ObjectIdentity
at_8724XL_80 = _At_8724XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 42)
)
_At_8748XL_80_ObjectIdentity = ObjectIdentity
at_8748XL_80 = _At_8748XL_80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 43)
)
_At_8948EX_ObjectIdentity = ObjectIdentity
at_8948EX = _At_8948EX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 44)
)
_At_8948i_ObjectIdentity = ObjectIdentity
at_8948i = _At_8948i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 45)
)
_At_8624T2M_ObjectIdentity = ObjectIdentity
at_8624T2M = _At_8624T2M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 46)
)
_At_Rapier24i_DC_NEBS_ObjectIdentity = ObjectIdentity
at_Rapier24i_DC_NEBS = _At_Rapier24i_DC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 47)
)
_At_8724XL_DC_NEBS_ObjectIdentity = ObjectIdentity
at_8724XL_DC_NEBS = _At_8724XL_DC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 48)
)
_At_9924T_ObjectIdentity = ObjectIdentity
at_9924T = _At_9924T_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 49)
)
_At_9924SP_ObjectIdentity = ObjectIdentity
at_9924SP = _At_9924SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 50)
)
_At_9924T_4SP_ObjectIdentity = ObjectIdentity
at_9924T_4SP = _At_9924T_4SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 51)
)
_At_9924TEMC_ObjectIdentity = ObjectIdentity
at_9924TEMC = _At_9924TEMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 53)
)
_At_8724MLB_ObjectIdentity = ObjectIdentity
at_8724MLB = _At_8724MLB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 55)
)
_At_8624POE_ObjectIdentity = ObjectIdentity
at_8624POE = _At_8624POE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 56)
)
_At_9924Ts_ObjectIdentity = ObjectIdentity
at_9924Ts = _At_9924Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 57)
)
_At_86482SP_ObjectIdentity = ObjectIdentity
at_86482SP = _At_86482SP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 58)
)
_At_9924Ti_ObjectIdentity = ObjectIdentity
at_9924Ti = _At_9924Ti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 59)
)
_At_9924SPi_ObjectIdentity = ObjectIdentity
at_9924SPi = _At_9924SPi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 60)
)
_At_9924Tsi_ObjectIdentity = ObjectIdentity
at_9924Tsi = _At_9924Tsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 61)
)
_At_9924SPsi_ObjectIdentity = ObjectIdentity
at_9924SPsi = _At_9924SPsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 62)
)
_At_8948i_N_ObjectIdentity = ObjectIdentity
at_8948i_N = _At_8948i_N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 63)
)
_At_9924Tsi_N_ObjectIdentity = ObjectIdentity
at_9924Tsi_N = _At_9924Tsi_N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 64)
)
_At_Rapier48w_ObjectIdentity = ObjectIdentity
at_Rapier48w = _At_Rapier48w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 65)
)
_At_8724SL_V2_ObjectIdentity = ObjectIdentity
at_8724SL_V2 = _At_8724SL_V2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 67)
)
_X900_48FS_ObjectIdentity = ObjectIdentity
x900_48FS = _X900_48FS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 68)
)
_At_SwitchBladex908_ObjectIdentity = ObjectIdentity
at_SwitchBladex908 = _At_SwitchBladex908_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 69)
)
_At_x900_12XTS_ObjectIdentity = ObjectIdentity
at_x900_12XTS = _At_x900_12XTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 70)
)
_At_Rapier48wb_ObjectIdentity = ObjectIdentity
at_Rapier48wb = _At_Rapier48wb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 71)
)
_At_Rapier48w_AC_ObjectIdentity = ObjectIdentity
at_Rapier48w_AC = _At_Rapier48w_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 72)
)
_At_Rapier48wb_AC_ObjectIdentity = ObjectIdentity
at_Rapier48wb_AC = _At_Rapier48wb_AC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 73)
)
_At_x900_24XT_ObjectIdentity = ObjectIdentity
at_x900_24XT = _At_x900_24XT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 75)
)
_At_x900_24XS_ObjectIdentity = ObjectIdentity
at_x900_24XS = _At_x900_24XS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 76)
)
_At_x900_24XT_N_ObjectIdentity = ObjectIdentity
at_x900_24XT_N = _At_x900_24XT_N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 77)
)
_At_x600_24Ts_ObjectIdentity = ObjectIdentity
at_x600_24Ts = _At_x600_24Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 80)
)
_At_x600_24TsXP_ObjectIdentity = ObjectIdentity
at_x600_24TsXP = _At_x600_24TsXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 81)
)
_At_x600_48Ts_ObjectIdentity = ObjectIdentity
at_x600_48Ts = _At_x600_48Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 82)
)
_At_x600_48TsXP_ObjectIdentity = ObjectIdentity
at_x600_48TsXP = _At_x600_48TsXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 83)
)
_At_rapier24ib_NEBS_ObjectIdentity = ObjectIdentity
at_rapier24ib_NEBS = _At_rapier24ib_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 84)
)
_At_rapier24ib_DC_NEBS_ObjectIdentity = ObjectIdentity
at_rapier24ib_DC_NEBS = _At_rapier24ib_DC_NEBS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 85)
)
_At_SBx8112_ObjectIdentity = ObjectIdentity
at_SBx8112 = _At_SBx8112_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 86)
)
_At_SBx81CFC400_ObjectIdentity = ObjectIdentity
at_SBx81CFC400 = _At_SBx81CFC400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 87)
)
_At_SBx81CFC960_ObjectIdentity = ObjectIdentity
at_SBx81CFC960 = _At_SBx81CFC960_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 88)
)
_At_x600_24TsPoE_ObjectIdentity = ObjectIdentity
at_x600_24TsPoE = _At_x600_24TsPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 91)
)
_At_x600_24TsPoEPlus_ObjectIdentity = ObjectIdentity
at_x600_24TsPoEPlus = _At_x600_24TsPoEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 92)
)
_X610_48Ts_X_POEPlus_ObjectIdentity = ObjectIdentity
x610_48Ts_X_POEPlus = _X610_48Ts_X_POEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 93)
)
_X610_48Ts_POEPlus_ObjectIdentity = ObjectIdentity
x610_48Ts_POEPlus = _X610_48Ts_POEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 94)
)
_X610_24Ts_X_POEPlus_ObjectIdentity = ObjectIdentity
x610_24Ts_X_POEPlus = _X610_24Ts_X_POEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 95)
)
_X610_24Ts_POEPlus_ObjectIdentity = ObjectIdentity
x610_24Ts_POEPlus = _X610_24Ts_POEPlus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 96)
)
_X610_48Ts_X_ObjectIdentity = ObjectIdentity
x610_48Ts_X = _X610_48Ts_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 97)
)
_X610_48Ts_ObjectIdentity = ObjectIdentity
x610_48Ts = _X610_48Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 98)
)
_X610_24Ts_X_ObjectIdentity = ObjectIdentity
x610_24Ts_X = _X610_24Ts_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 99)
)
_X610_24Ts_ObjectIdentity = ObjectIdentity
x610_24Ts = _X610_24Ts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 100)
)
_X610_24SP_X_ObjectIdentity = ObjectIdentity
x610_24SP_X = _X610_24SP_X_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 101)
)
_At_RP48xDC_ObjectIdentity = ObjectIdentity
at_RP48xDC = _At_RP48xDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 105)
)
_At_x510_28GTX_ObjectIdentity = ObjectIdentity
at_x510_28GTX = _At_x510_28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 109)
)
_At_x510_28GPX_ObjectIdentity = ObjectIdentity
at_x510_28GPX = _At_x510_28GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 110)
)
_At_x510_28GSX_ObjectIdentity = ObjectIdentity
at_x510_28GSX = _At_x510_28GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 111)
)
_At_x510_52GTX_ObjectIdentity = ObjectIdentity
at_x510_52GTX = _At_x510_52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 112)
)
_At_x510_52GPX_ObjectIdentity = ObjectIdentity
at_x510_52GPX = _At_x510_52GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 113)
)
_At_SBx8106_ObjectIdentity = ObjectIdentity
at_SBx8106 = _At_SBx8106_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 114)
)
_At_x510DP_52GTX_ObjectIdentity = ObjectIdentity
at_x510DP_52GTX = _At_x510DP_52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 116)
)
_At_IX5_28GPX_ObjectIdentity = ObjectIdentity
at_IX5_28GPX = _At_IX5_28GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 117)
)
_At_x930_28GTX_ObjectIdentity = ObjectIdentity
at_x930_28GTX = _At_x930_28GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 118)
)
_At_x930_28GPX_ObjectIdentity = ObjectIdentity
at_x930_28GPX = _At_x930_28GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 119)
)
_At_x930_28GSX_ObjectIdentity = ObjectIdentity
at_x930_28GSX = _At_x930_28GSX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 120)
)
_At_x930_52GTX_ObjectIdentity = ObjectIdentity
at_x930_52GTX = _At_x930_52GTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 121)
)
_At_x930_52GPX_ObjectIdentity = ObjectIdentity
at_x930_52GPX = _At_x930_52GPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 14, 122)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PRODUCT-MIB",
    **{"products": products,
       "bridgeRouter": bridgeRouter,
       "centreCOM_AR300Router": centreCOM_AR300Router,
       "centreCOM_AR720Router": centreCOM_AR720Router,
       "centreCOM_AR300LRouter": centreCOM_AR300LRouter,
       "centreCOM_AR310Router": centreCOM_AR310Router,
       "centreCOM_AR300LURouter": centreCOM_AR300LURouter,
       "centreCOM_AR300URouter": centreCOM_AR300URouter,
       "centreCOM_AR310URouter": centreCOM_AR310URouter,
       "centreCOM_AR350Router": centreCOM_AR350Router,
       "centreCOM_AR370Router": centreCOM_AR370Router,
       "centreCOM_AR330Router": centreCOM_AR330Router,
       "centreCOM_AR395Router": centreCOM_AR395Router,
       "centreCOM_AR390Router": centreCOM_AR390Router,
       "centreCOM_AR370URouter": centreCOM_AR370URouter,
       "centreCOM_AR740Router": centreCOM_AR740Router,
       "centreCOM_AR140SRouter": centreCOM_AR140SRouter,
       "centreCOM_AR140URouter": centreCOM_AR140URouter,
       "centreCOM_AR320Router": centreCOM_AR320Router,
       "centreCOM_AR130SRouter": centreCOM_AR130SRouter,
       "centreCOM_AR130URouter": centreCOM_AR130URouter,
       "centreCOM_AR160Router": centreCOM_AR160Router,
       "at_AR740RouterDC": at_AR740RouterDC,
       "centreCOM_AR120Router": centreCOM_AR120Router,
       "at_AR410Router": at_AR410Router,
       "at_AR725Router": at_AR725Router,
       "at_AR745Router": at_AR745Router,
       "at_AR410v2Router": at_AR410v2Router,
       "at_AR410v3Router": at_AR410v3Router,
       "at_AR725RouterDC": at_AR725RouterDC,
       "at_AR745RouterDC": at_AR745RouterDC,
       "at_AR450Router": at_AR450Router,
       "at_AR450DualRouter": at_AR450DualRouter,
       "at_AR440Router": at_AR440Router,
       "at_AR441Router": at_AR441Router,
       "at_AR442Router": at_AR442Router,
       "at_AR443Router": at_AR443Router,
       "at_AR444Router": at_AR444Router,
       "at_AR420Router": at_AR420Router,
       "at_AR415SRouter": at_AR415SRouter,
       "at_AR415SRouterDC": at_AR415SRouterDC,
       "at_AR550Router": at_AR550Router,
       "at_AR551Router": at_AR551Router,
       "at_AR552Router": at_AR552Router,
       "at_AR550SRouterDP": at_AR550SRouterDP,
       "at_AR570Router": at_AR570Router,
       "at_AR770Router": at_AR770Router,
       "at_AR750SRouterDP": at_AR750SRouterDP,
       "at_AR560SRouter": at_AR560SRouter,
       "swhub": swhub,
       "at_x200_GE52T": at_x200_GE52T,
       "at_x200_GE28T": at_x200_GE28T,
       "at_x210_9GT": at_x210_9GT,
       "at_x210_16GT": at_x210_16GT,
       "at_x210_24GT": at_x210_24GT,
       "at_x310_26FT": at_x310_26FT,
       "at_x310_50FT": at_x310_50FT,
       "at_x310_26FP": at_x310_26FP,
       "at_x310_50FP": at_x310_50FP,
       "at_x310_26GT": at_x310_26GT,
       "at_x310_50GT": at_x310_50GT,
       "at_x310_26GP": at_x310_26GP,
       "at_x310_50GP": at_x310_50GP,
       "at_x230_10GT": at_x230_10GT,
       "at_x230_18GT": at_x230_18GT,
       "at_x230_28GT": at_x230_28GT,
       "at_x230_52GT": at_x230_52GT,
       "at_x230_10GP": at_x230_10GP,
       "at_x230_18GP": at_x230_18GP,
       "at_x230_28GP": at_x230_28GP,
       "at_x230_52GP": at_x230_52GP,
       "at_x230_10GPT": at_x230_10GPT,
       "routerSwitch": routerSwitch,
       "at_Rapier24": at_Rapier24,
       "at_Rapier16fSC": at_Rapier16fSC,
       "at_Rapier16fVF": at_Rapier16fVF,
       "at_Rapier16fMT": at_Rapier16fMT,
       "at_Rapier48": at_Rapier48,
       "at_Rapier8t8fSC": at_Rapier8t8fSC,
       "at_Rapier8t8fSCi": at_Rapier8t8fSCi,
       "at_Rapier8t8fMT": at_Rapier8t8fMT,
       "at_Rapier8t8fMTi": at_Rapier8t8fMTi,
       "at_Rapier8fSC": at_Rapier8fSC,
       "at_Rapier8fSCi": at_Rapier8fSCi,
       "at_Rapier8fMT": at_Rapier8fMT,
       "at_Rapier8fMTi": at_Rapier8fMTi,
       "at_Rapier16fMTi": at_Rapier16fMTi,
       "at_RapierG6": at_RapierG6,
       "at_RapierG6SX": at_RapierG6SX,
       "at_RapierG6LX": at_RapierG6LX,
       "at_RapierG6MT": at_RapierG6MT,
       "at_Rapier16fSCi": at_Rapier16fSCi,
       "at_Rapier24i": at_Rapier24i,
       "at_Rapier48i": at_Rapier48i,
       "at_Switchblade4AC": at_Switchblade4AC,
       "at_Switchblade4DC": at_Switchblade4DC,
       "at_Switchblade8AC": at_Switchblade8AC,
       "at_Switchblade8DC": at_Switchblade8DC,
       "at_9816GF": at_9816GF,
       "at_9812TF": at_9812TF,
       "at_9816GB": at_9816GB,
       "at_9812T": at_9812T,
       "at_8724XL": at_8724XL,
       "at_8748XL": at_8748XL,
       "at_8724XLDC": at_8724XLDC,
       "at_8748XLDC": at_8748XLDC,
       "at_9816GB_DC": at_9816GB_DC,
       "at_9812T_DC": at_9812T_DC,
       "at_8824": at_8824,
       "at_8848": at_8848,
       "at_8824_DC": at_8824_DC,
       "at_8848_DC": at_8848_DC,
       "at_8624XL_80": at_8624XL_80,
       "at_8724XL_80": at_8724XL_80,
       "at_8748XL_80": at_8748XL_80,
       "at_8948EX": at_8948EX,
       "at_8948i": at_8948i,
       "at_8624T2M": at_8624T2M,
       "at_Rapier24i_DC_NEBS": at_Rapier24i_DC_NEBS,
       "at_8724XL_DC_NEBS": at_8724XL_DC_NEBS,
       "at_9924T": at_9924T,
       "at_9924SP": at_9924SP,
       "at_9924T_4SP": at_9924T_4SP,
       "at_9924TEMC": at_9924TEMC,
       "at_8724MLB": at_8724MLB,
       "at_8624POE": at_8624POE,
       "at_9924Ts": at_9924Ts,
       "at_86482SP": at_86482SP,
       "at_9924Ti": at_9924Ti,
       "at_9924SPi": at_9924SPi,
       "at_9924Tsi": at_9924Tsi,
       "at_9924SPsi": at_9924SPsi,
       "at_8948i_N": at_8948i_N,
       "at_9924Tsi_N": at_9924Tsi_N,
       "at_Rapier48w": at_Rapier48w,
       "at_8724SL_V2": at_8724SL_V2,
       "x900_48FS": x900_48FS,
       "at_SwitchBladex908": at_SwitchBladex908,
       "at_x900_12XTS": at_x900_12XTS,
       "at_Rapier48wb": at_Rapier48wb,
       "at_Rapier48w_AC": at_Rapier48w_AC,
       "at_Rapier48wb_AC": at_Rapier48wb_AC,
       "at_x900_24XT": at_x900_24XT,
       "at_x900_24XS": at_x900_24XS,
       "at_x900_24XT_N": at_x900_24XT_N,
       "at_x600_24Ts": at_x600_24Ts,
       "at_x600_24TsXP": at_x600_24TsXP,
       "at_x600_48Ts": at_x600_48Ts,
       "at_x600_48TsXP": at_x600_48TsXP,
       "at-rapier24ib-NEBS": at_rapier24ib_NEBS,
       "at-rapier24ib-DC-NEBS": at_rapier24ib_DC_NEBS,
       "at-SBx8112": at_SBx8112,
       "at-SBx81CFC400": at_SBx81CFC400,
       "at-SBx81CFC960": at_SBx81CFC960,
       "at_x600_24TsPoE": at_x600_24TsPoE,
       "at_x600_24TsPoEPlus": at_x600_24TsPoEPlus,
       "x610_48Ts_X_POEPlus": x610_48Ts_X_POEPlus,
       "x610_48Ts_POEPlus": x610_48Ts_POEPlus,
       "x610_24Ts_X_POEPlus": x610_24Ts_X_POEPlus,
       "x610_24Ts_POEPlus": x610_24Ts_POEPlus,
       "x610_48Ts_X": x610_48Ts_X,
       "x610_48Ts": x610_48Ts,
       "x610_24Ts_X": x610_24Ts_X,
       "x610_24Ts": x610_24Ts,
       "x610_24SP_X": x610_24SP_X,
       "at_RP48xDC": at_RP48xDC,
       "at_x510_28GTX": at_x510_28GTX,
       "at_x510_28GPX": at_x510_28GPX,
       "at_x510_28GSX": at_x510_28GSX,
       "at_x510_52GTX": at_x510_52GTX,
       "at_x510_52GPX": at_x510_52GPX,
       "at_SBx8106": at_SBx8106,
       "at_x510DP_52GTX": at_x510DP_52GTX,
       "at_IX5_28GPX": at_IX5_28GPX,
       "at_x930_28GTX": at_x930_28GTX,
       "at_x930_28GPX": at_x930_28GPX,
       "at_x930_28GSX": at_x930_28GSX,
       "at_x930_52GTX": at_x930_52GTX,
       "at_x930_52GPX": at_x930_52GPX}
)
