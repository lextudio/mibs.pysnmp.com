# SNMP MIB module (F10-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:28 2024
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

(f10Modules,
 f10Products) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Modules",
    "f10Products")

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

f10FamilyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4, 1)
)
f10FamilyMIB.setRevisions(
        ("2013-10-22 12:00",
         "2011-12-15 12:00",
         "2007-06-15 12:00",
         "2002-01-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10ESeriesProducts_ObjectIdentity = ObjectIdentity
f10ESeriesProducts = _F10ESeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1)
)
if mibBuilder.loadTexts:
    f10ESeriesProducts.setStatus("current")
_E1200_ObjectIdentity = ObjectIdentity
e1200 = _E1200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1, 1)
)
if mibBuilder.loadTexts:
    e1200.setStatus("current")
_E600_ObjectIdentity = ObjectIdentity
e600 = _E600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1, 2)
)
if mibBuilder.loadTexts:
    e600.setStatus("current")
_E300_ObjectIdentity = ObjectIdentity
e300 = _E300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1, 3)
)
if mibBuilder.loadTexts:
    e300.setStatus("current")
_E610_ObjectIdentity = ObjectIdentity
e610 = _E610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1, 4)
)
if mibBuilder.loadTexts:
    e610.setStatus("current")
_E1200i_ObjectIdentity = ObjectIdentity
e1200i = _E1200i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1, 5)
)
if mibBuilder.loadTexts:
    e1200i.setStatus("current")
_F10CSeriesProducts_ObjectIdentity = ObjectIdentity
f10CSeriesProducts = _F10CSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 2)
)
if mibBuilder.loadTexts:
    f10CSeriesProducts.setStatus("current")
_C300_ObjectIdentity = ObjectIdentity
c300 = _C300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 2, 1)
)
if mibBuilder.loadTexts:
    c300.setStatus("current")
_C150_ObjectIdentity = ObjectIdentity
c150 = _C150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 2, 2)
)
if mibBuilder.loadTexts:
    c150.setStatus("current")
_F10SSeriesProducts_ObjectIdentity = ObjectIdentity
f10SSeriesProducts = _F10SSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3)
)
if mibBuilder.loadTexts:
    f10SSeriesProducts.setStatus("current")
_S50_ObjectIdentity = ObjectIdentity
s50 = _S50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1)
)
if mibBuilder.loadTexts:
    s50.setStatus("current")
_S50e_ObjectIdentity = ObjectIdentity
s50e = _S50e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 2)
)
if mibBuilder.loadTexts:
    s50e.setStatus("current")
_S50v_ObjectIdentity = ObjectIdentity
s50v = _S50v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 3)
)
if mibBuilder.loadTexts:
    s50v.setStatus("current")
_S25pac_ObjectIdentity = ObjectIdentity
s25pac = _S25pac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 4)
)
if mibBuilder.loadTexts:
    s25pac.setStatus("current")
_S2410cp_ObjectIdentity = ObjectIdentity
s2410cp = _S2410cp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 5)
)
if mibBuilder.loadTexts:
    s2410cp.setStatus("current")
_S2410p_ObjectIdentity = ObjectIdentity
s2410p = _S2410p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 6)
)
if mibBuilder.loadTexts:
    s2410p.setStatus("current")
_S50nac_ObjectIdentity = ObjectIdentity
s50nac = _S50nac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 7)
)
if mibBuilder.loadTexts:
    s50nac.setStatus("current")
_S50ndc_ObjectIdentity = ObjectIdentity
s50ndc = _S50ndc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 8)
)
if mibBuilder.loadTexts:
    s50ndc.setStatus("current")
_S25pdc_ObjectIdentity = ObjectIdentity
s25pdc = _S25pdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 9)
)
if mibBuilder.loadTexts:
    s25pdc.setStatus("current")
_S25v_ObjectIdentity = ObjectIdentity
s25v = _S25v_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 10)
)
if mibBuilder.loadTexts:
    s25v.setStatus("current")
_S25n_ObjectIdentity = ObjectIdentity
s25n = _S25n_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 11)
)
if mibBuilder.loadTexts:
    s25n.setStatus("current")
_S60_ObjectIdentity = ObjectIdentity
s60 = _S60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 12)
)
if mibBuilder.loadTexts:
    s60.setStatus("current")
_S55_ObjectIdentity = ObjectIdentity
s55 = _S55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 13)
)
if mibBuilder.loadTexts:
    s55.setStatus("current")
_S4810_ObjectIdentity = ObjectIdentity
s4810 = _S4810_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 14)
)
if mibBuilder.loadTexts:
    s4810.setStatus("current")
_Z9000_ObjectIdentity = ObjectIdentity
z9000 = _Z9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 15)
)
if mibBuilder.loadTexts:
    z9000.setStatus("current")
_S4820_ObjectIdentity = ObjectIdentity
s4820 = _S4820_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 17)
)
if mibBuilder.loadTexts:
    s4820.setStatus("current")
_S6000_ObjectIdentity = ObjectIdentity
s6000 = _S6000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 18)
)
if mibBuilder.loadTexts:
    s6000.setStatus("current")
_S5000_ObjectIdentity = ObjectIdentity
s5000 = _S5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 19)
)
if mibBuilder.loadTexts:
    s5000.setStatus("current")
_S4810on_ObjectIdentity = ObjectIdentity
s4810on = _S4810on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 20)
)
if mibBuilder.loadTexts:
    s4810on.setStatus("current")
_S6000on_ObjectIdentity = ObjectIdentity
s6000on = _S6000on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 21)
)
if mibBuilder.loadTexts:
    s6000on.setStatus("current")
_S4000_ObjectIdentity = ObjectIdentity
s4000 = _S4000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 22)
)
if mibBuilder.loadTexts:
    s4000.setStatus("current")
_F10MSeriesProducts_ObjectIdentity = ObjectIdentity
f10MSeriesProducts = _F10MSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 4)
)
if mibBuilder.loadTexts:
    f10MSeriesProducts.setStatus("current")
_M_MXL_ObjectIdentity = ObjectIdentity
m_MXL = _M_MXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 4, 1)
)
if mibBuilder.loadTexts:
    m_MXL.setStatus("current")
_M_IOA_ObjectIdentity = ObjectIdentity
m_IOA = _M_IOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 4, 2)
)
if mibBuilder.loadTexts:
    m_IOA.setStatus("current")
_S_IOA_ObjectIdentity = ObjectIdentity
s_IOA = _S_IOA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 4, 3)
)
if mibBuilder.loadTexts:
    s_IOA.setStatus("current")
_F10ZSeriesProducts_ObjectIdentity = ObjectIdentity
f10ZSeriesProducts = _F10ZSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 5)
)
if mibBuilder.loadTexts:
    f10ZSeriesProducts.setStatus("current")
_Z9500_ObjectIdentity = ObjectIdentity
z9500 = _Z9500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 5, 1)
)
if mibBuilder.loadTexts:
    z9500.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-PRODUCTS-MIB",
    **{"f10ESeriesProducts": f10ESeriesProducts,
       "e1200": e1200,
       "e600": e600,
       "e300": e300,
       "e610": e610,
       "e1200i": e1200i,
       "f10CSeriesProducts": f10CSeriesProducts,
       "c300": c300,
       "c150": c150,
       "f10SSeriesProducts": f10SSeriesProducts,
       "s50": s50,
       "s50e": s50e,
       "s50v": s50v,
       "s25pac": s25pac,
       "s2410cp": s2410cp,
       "s2410p": s2410p,
       "s50nac": s50nac,
       "s50ndc": s50ndc,
       "s25pdc": s25pdc,
       "s25v": s25v,
       "s25n": s25n,
       "s60": s60,
       "s55": s55,
       "s4810": s4810,
       "z9000": z9000,
       "s4820": s4820,
       "s6000": s6000,
       "s5000": s5000,
       "s4810on": s4810on,
       "s6000on": s6000on,
       "s4000": s4000,
       "f10MSeriesProducts": f10MSeriesProducts,
       "m-MXL": m_MXL,
       "m-IOA": m_IOA,
       "s-IOA": s_IOA,
       "f10ZSeriesProducts": f10ZSeriesProducts,
       "z9500": z9500,
       "f10FamilyMIB": f10FamilyMIB}
)
