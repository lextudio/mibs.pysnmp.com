# SNMP MIB module (DELL-NETWORKING-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:58 2024
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

(dellNetModules,
 dellNetProducts) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetModules",
    "dellNetProducts")

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

dellNetFamilyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 4, 1)
)
dellNetFamilyMIB.setRevisions(
        ("2013-10-22 12:00",
         "2011-12-15 12:00",
         "2007-06-15 12:00",
         "2002-01-31 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetESeriesProducts_ObjectIdentity = ObjectIdentity
dellNetESeriesProducts = _DellNetESeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetESeriesProducts.setStatus("current")
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
_DellNetCSeriesProducts_ObjectIdentity = ObjectIdentity
dellNetCSeriesProducts = _DellNetCSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 2)
)
if mibBuilder.loadTexts:
    dellNetCSeriesProducts.setStatus("current")
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
_C9010_ObjectIdentity = ObjectIdentity
c9010 = _C9010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 2, 3)
)
if mibBuilder.loadTexts:
    c9010.setStatus("current")
_DellNetSSeriesProducts_ObjectIdentity = ObjectIdentity
dellNetSSeriesProducts = _DellNetSSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3)
)
if mibBuilder.loadTexts:
    dellNetSSeriesProducts.setStatus("current")
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
_S4048on_ObjectIdentity = ObjectIdentity
s4048on = _S4048on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 22)
)
if mibBuilder.loadTexts:
    s4048on.setStatus("current")
_S3048on_ObjectIdentity = ObjectIdentity
s3048on = _S3048on_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 23)
)
if mibBuilder.loadTexts:
    s3048on.setStatus("current")
_S3148p_ObjectIdentity = ObjectIdentity
s3148p = _S3148p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 24)
)
if mibBuilder.loadTexts:
    s3148p.setStatus("current")
_S3124p_ObjectIdentity = ObjectIdentity
s3124p = _S3124p_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 25)
)
if mibBuilder.loadTexts:
    s3124p.setStatus("current")
_S3124f_ObjectIdentity = ObjectIdentity
s3124f = _S3124f_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 26)
)
if mibBuilder.loadTexts:
    s3124f.setStatus("current")
_S3124_ObjectIdentity = ObjectIdentity
s3124 = _S3124_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 27)
)
if mibBuilder.loadTexts:
    s3124.setStatus("current")
_S6100_ObjectIdentity = ObjectIdentity
s6100 = _S6100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 28)
)
if mibBuilder.loadTexts:
    s6100.setStatus("current")
_S6010_ObjectIdentity = ObjectIdentity
s6010 = _S6010_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 29)
)
if mibBuilder.loadTexts:
    s6010.setStatus("current")
_S4048t_ObjectIdentity = ObjectIdentity
s4048t = _S4048t_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 30)
)
if mibBuilder.loadTexts:
    s4048t.setStatus("current")
_S3148_ObjectIdentity = ObjectIdentity
s3148 = _S3148_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 31)
)
if mibBuilder.loadTexts:
    s3148.setStatus("current")
_DellNetMSeriesProducts_ObjectIdentity = ObjectIdentity
dellNetMSeriesProducts = _DellNetMSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 4)
)
if mibBuilder.loadTexts:
    dellNetMSeriesProducts.setStatus("current")
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
_DellNetZSeriesProducts_ObjectIdentity = ObjectIdentity
dellNetZSeriesProducts = _DellNetZSeriesProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 5)
)
if mibBuilder.loadTexts:
    dellNetZSeriesProducts.setStatus("current")
_Z9500_ObjectIdentity = ObjectIdentity
z9500 = _Z9500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 5, 1)
)
if mibBuilder.loadTexts:
    z9500.setStatus("current")
_Z9100_ObjectIdentity = ObjectIdentity
z9100 = _Z9100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 5, 2)
)
if mibBuilder.loadTexts:
    z9100.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-PRODUCTS-MIB",
    **{"dellNetESeriesProducts": dellNetESeriesProducts,
       "e1200": e1200,
       "e600": e600,
       "e300": e300,
       "e610": e610,
       "e1200i": e1200i,
       "dellNetCSeriesProducts": dellNetCSeriesProducts,
       "c300": c300,
       "c150": c150,
       "c9010": c9010,
       "dellNetSSeriesProducts": dellNetSSeriesProducts,
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
       "s4048on": s4048on,
       "s3048on": s3048on,
       "s3148p": s3148p,
       "s3124p": s3124p,
       "s3124f": s3124f,
       "s3124": s3124,
       "s6100": s6100,
       "s6010": s6010,
       "s4048t": s4048t,
       "s3148": s3148,
       "dellNetMSeriesProducts": dellNetMSeriesProducts,
       "m-MXL": m_MXL,
       "m-IOA": m_IOA,
       "s-IOA": s_IOA,
       "dellNetZSeriesProducts": dellNetZSeriesProducts,
       "z9500": z9500,
       "z9100": z9100,
       "dellNetFamilyMIB": dellNetFamilyMIB}
)
