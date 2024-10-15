# SNMP MIB module (HM2-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:28 2024
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

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

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

hm2ProductsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2)
)
hm2ProductsMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2ProductFamily_ObjectIdentity = ObjectIdentity
hm2ProductFamily = _Hm2ProductFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hm2ProductFamily.setStatus("current")
_Ees_ObjectIdentity = ObjectIdentity
ees = _Ees_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ees.setStatus("current")
_Ees20_0600_ObjectIdentity = ObjectIdentity
ees20_0600 = _Ees20_0600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ees20_0600.setStatus("current")
_Ees25_0600_ObjectIdentity = ObjectIdentity
ees25_0600 = _Ees25_0600_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ees25_0600.setStatus("current")
_Rsp_ObjectIdentity = ObjectIdentity
rsp = _Rsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rsp.setStatus("current")
_Rsp20_11003z6tt_ObjectIdentity = ObjectIdentity
rsp20_11003z6tt = _Rsp20_11003z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsp20_11003z6tt.setStatus("current")
_Rsp20_11003z6zt_ObjectIdentity = ObjectIdentity
rsp20_11003z6zt = _Rsp20_11003z6zt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsp20_11003z6zt.setStatus("current")
_Rsp25_11003z6tt_ObjectIdentity = ObjectIdentity
rsp25_11003z6tt = _Rsp25_11003z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rsp25_11003z6tt.setStatus("current")
_Rsp25_11003z6zt_ObjectIdentity = ObjectIdentity
rsp25_11003z6zt = _Rsp25_11003z6zt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    rsp25_11003z6zt.setStatus("current")
_Rsp30_08033o6tt_ObjectIdentity = ObjectIdentity
rsp30_08033o6tt = _Rsp30_08033o6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rsp30_08033o6tt.setStatus("current")
_Rsp30_08033o6zt_ObjectIdentity = ObjectIdentity
rsp30_08033o6zt = _Rsp30_08033o6zt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    rsp30_08033o6zt.setStatus("current")
_Rsp35_08033o6tt_ObjectIdentity = ObjectIdentity
rsp35_08033o6tt = _Rsp35_08033o6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    rsp35_08033o6tt.setStatus("current")
_Rsp35_08033o6zt_ObjectIdentity = ObjectIdentity
rsp35_08033o6zt = _Rsp35_08033o6zt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 2, 8)
)
if mibBuilder.loadTexts:
    rsp35_08033o6zt.setStatus("current")
_Eagle_ObjectIdentity = ObjectIdentity
eagle = _Eagle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eagle.setStatus("current")
_Eagle20_0400999TT999_ObjectIdentity = ObjectIdentity
eagle20_0400999TT999 = _Eagle20_0400999TT999_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT999.setStatus("current")
_Eagle20_0400999TTC99_ObjectIdentity = ObjectIdentity
eagle20_0400999TTC99 = _Eagle20_0400999TTC99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTC99.setStatus("current")
_Eagle20_0400999TTCAA_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCAA = _Eagle20_0400999TTCAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCAA.setStatus("current")
_Eagle20_0400999TTCAB_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCAB = _Eagle20_0400999TTCAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 4)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCAB.setStatus("current")
_Eagle20_0400999TTCVA_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCVA = _Eagle20_0400999TTCVA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 5)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCVA.setStatus("current")
_Eagle20_0400999TTCVB_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCVB = _Eagle20_0400999TTCVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 6)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCVB.setStatus("current")
_Eagle20_0400999TTCH2_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCH2 = _Eagle20_0400999TTCH2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 7)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCH2.setStatus("current")
_Eagle20_0400999TTCP2_ObjectIdentity = ObjectIdentity
eagle20_0400999TTCP2 = _Eagle20_0400999TTCP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 8)
)
if mibBuilder.loadTexts:
    eagle20_0400999TTCP2.setStatus("current")
_Eagle20_0400999TT9AA_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9AA = _Eagle20_0400999TT9AA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 20)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9AA.setStatus("current")
_Eagle20_0400999TT9AB_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9AB = _Eagle20_0400999TT9AB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 21)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9AB.setStatus("current")
_Eagle20_0400999TT9VA_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9VA = _Eagle20_0400999TT9VA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 22)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9VA.setStatus("current")
_Eagle20_0400999TT9VB_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9VB = _Eagle20_0400999TT9VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 23)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9VB.setStatus("current")
_Eagle20_0400999TT9H2_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9H2 = _Eagle20_0400999TT9H2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 24)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9H2.setStatus("current")
_Eagle20_0400999TT9P2_ObjectIdentity = ObjectIdentity
eagle20_0400999TT9P2 = _Eagle20_0400999TT9P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 25)
)
if mibBuilder.loadTexts:
    eagle20_0400999TT9P2.setStatus("current")
_Eagle30_04022O6TT999_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT999 = _Eagle30_04022O6TT999_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 40)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT999.setStatus("current")
_Eagle30_04022O6TTC99_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTC99 = _Eagle30_04022O6TTC99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 41)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTC99.setStatus("current")
_Eagle30_04022O6TTCAA_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCAA = _Eagle30_04022O6TTCAA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 42)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCAA.setStatus("current")
_Eagle30_04022O6TTCAB_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCAB = _Eagle30_04022O6TTCAB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 43)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCAB.setStatus("current")
_Eagle30_04022O6TTCVA_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCVA = _Eagle30_04022O6TTCVA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 44)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCVA.setStatus("current")
_Eagle30_04022O6TTCVB_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCVB = _Eagle30_04022O6TTCVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 45)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCVB.setStatus("current")
_Eagle30_04022O6TTCH2_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCH2 = _Eagle30_04022O6TTCH2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 46)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCH2.setStatus("current")
_Eagle30_04022O6TTCP2_ObjectIdentity = ObjectIdentity
eagle30_04022O6TTCP2 = _Eagle30_04022O6TTCP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 47)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TTCP2.setStatus("current")
_Eagle30_04022O6TT9AA_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9AA = _Eagle30_04022O6TT9AA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 60)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9AA.setStatus("current")
_Eagle30_04022O6TT9AB_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9AB = _Eagle30_04022O6TT9AB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 61)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9AB.setStatus("current")
_Eagle30_04022O6TT9VA_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9VA = _Eagle30_04022O6TT9VA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 62)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9VA.setStatus("current")
_Eagle30_04022O6TT9VB_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9VB = _Eagle30_04022O6TT9VB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 63)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9VB.setStatus("current")
_Eagle30_04022O6TT9H2_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9H2 = _Eagle30_04022O6TT9H2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 64)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9H2.setStatus("current")
_Eagle30_04022O6TT9P2_ObjectIdentity = ObjectIdentity
eagle30_04022O6TT9P2 = _Eagle30_04022O6TT9P2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 3, 65)
)
if mibBuilder.loadTexts:
    eagle30_04022O6TT9P2.setStatus("current")
_Msp_ObjectIdentity = ObjectIdentity
msp = _Msp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4)
)
if mibBuilder.loadTexts:
    msp.setStatus("current")
_Msp30_0804_ObjectIdentity = ObjectIdentity
msp30_0804 = _Msp30_0804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    msp30_0804.setStatus("current")
_Msp32_0804_ObjectIdentity = ObjectIdentity
msp32_0804 = _Msp32_0804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 2)
)
if mibBuilder.loadTexts:
    msp32_0804.setStatus("current")
_Msp30_1604_ObjectIdentity = ObjectIdentity
msp30_1604 = _Msp30_1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 3)
)
if mibBuilder.loadTexts:
    msp30_1604.setStatus("current")
_Msp32_1604_ObjectIdentity = ObjectIdentity
msp32_1604 = _Msp32_1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 4)
)
if mibBuilder.loadTexts:
    msp32_1604.setStatus("current")
_Msp30_2404_ObjectIdentity = ObjectIdentity
msp30_2404 = _Msp30_2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 5)
)
if mibBuilder.loadTexts:
    msp30_2404.setStatus("current")
_Msp32_2404_ObjectIdentity = ObjectIdentity
msp32_2404 = _Msp32_2404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 4, 6)
)
if mibBuilder.loadTexts:
    msp32_2404.setStatus("current")
_Rsps_ObjectIdentity = ObjectIdentity
rsps = _Rsps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5)
)
if mibBuilder.loadTexts:
    rsps.setStatus("current")
_Rsps20_06002z6yt_ObjectIdentity = ObjectIdentity
rsps20_06002z6yt = _Rsps20_06002z6yt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rsps20_06002z6yt.setStatus("current")
_Rsps20_06002z6tt_ObjectIdentity = ObjectIdentity
rsps20_06002z6tt = _Rsps20_06002z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    rsps20_06002z6tt.setStatus("current")
_Rsps20_06002t1tt_ObjectIdentity = ObjectIdentity
rsps20_06002t1tt = _Rsps20_06002t1tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    rsps20_06002t1tt.setStatus("current")
_Rsps25_06002z6yt_ObjectIdentity = ObjectIdentity
rsps25_06002z6yt = _Rsps25_06002z6yt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    rsps25_06002z6yt.setStatus("current")
_Rsps25_06002z6tt_ObjectIdentity = ObjectIdentity
rsps25_06002z6tt = _Rsps25_06002z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    rsps25_06002z6tt.setStatus("current")
_Rsps25_06002t1tt_ObjectIdentity = ObjectIdentity
rsps25_06002t1tt = _Rsps25_06002t1tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    rsps25_06002t1tt.setStatus("current")
_Rspl_ObjectIdentity = ObjectIdentity
rspl = _Rspl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 6)
)
if mibBuilder.loadTexts:
    rspl.setStatus("current")
_Rspl20_08002z6tt_ObjectIdentity = ObjectIdentity
rspl20_08002z6tt = _Rspl20_08002z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    rspl20_08002z6tt.setStatus("current")
_Rspl20_08002z6yt_ObjectIdentity = ObjectIdentity
rspl20_08002z6yt = _Rspl20_08002z6yt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    rspl20_08002z6yt.setStatus("current")
_Rspl30_08022o7yt_ObjectIdentity = ObjectIdentity
rspl30_08022o7yt = _Rspl30_08022o7yt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    rspl30_08022o7yt.setStatus("current")
_Rspl30_08022o7zt_ObjectIdentity = ObjectIdentity
rspl30_08022o7zt = _Rspl30_08022o7zt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    rspl30_08022o7zt.setStatus("current")
_Eesx_ObjectIdentity = ObjectIdentity
eesx = _Eesx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 7)
)
if mibBuilder.loadTexts:
    eesx.setStatus("current")
_Eesx20_0800_ObjectIdentity = ObjectIdentity
eesx20_0800 = _Eesx20_0800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    eesx20_0800.setStatus("current")
_Eesx30_0802_ObjectIdentity = ObjectIdentity
eesx30_0802 = _Eesx30_0802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    eesx30_0802.setStatus("current")
_Rspe_ObjectIdentity = ObjectIdentity
rspe = _Rspe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 8)
)
if mibBuilder.loadTexts:
    rspe.setStatus("current")
_Rspe30_24044O7T99_ObjectIdentity = ObjectIdentity
rspe30_24044O7T99 = _Rspe30_24044O7T99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rspe30_24044O7T99.setStatus("current")
_Rspe32_24044O7T99_ObjectIdentity = ObjectIdentity
rspe32_24044O7T99 = _Rspe32_24044O7T99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    rspe32_24044O7T99.setStatus("current")
_Rspe35_24044O7T99_ObjectIdentity = ObjectIdentity
rspe35_24044O7T99 = _Rspe35_24044O7T99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    rspe35_24044O7T99.setStatus("current")
_Rspe37_24044O7T99_ObjectIdentity = ObjectIdentity
rspe37_24044O7T99 = _Rspe37_24044O7T99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    rspe37_24044O7T99.setStatus("current")
_Tofino_ObjectIdentity = ObjectIdentity
tofino = _Tofino_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 9)
)
if mibBuilder.loadTexts:
    tofino.setStatus("current")
_Grs_ObjectIdentity = ObjectIdentity
grs = _Grs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10)
)
if mibBuilder.loadTexts:
    grs.setStatus("current")
_Grs1020_16t9_ObjectIdentity = ObjectIdentity
grs1020_16t9 = _Grs1020_16t9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    grs1020_16t9.setStatus("current")
_Grs1020_8t8z_ObjectIdentity = ObjectIdentity
grs1020_8t8z = _Grs1020_8t8z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    grs1020_8t8z.setStatus("current")
_Grs1120_16t9_ObjectIdentity = ObjectIdentity
grs1120_16t9 = _Grs1120_16t9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 3)
)
if mibBuilder.loadTexts:
    grs1120_16t9.setStatus("current")
_Grs1120_8t8z_ObjectIdentity = ObjectIdentity
grs1120_8t8z = _Grs1120_8t8z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 4)
)
if mibBuilder.loadTexts:
    grs1120_8t8z.setStatus("current")
_Grs1030_16t9_ObjectIdentity = ObjectIdentity
grs1030_16t9 = _Grs1030_16t9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 5)
)
if mibBuilder.loadTexts:
    grs1030_16t9.setStatus("current")
_Grs1030_8t8z_ObjectIdentity = ObjectIdentity
grs1030_8t8z = _Grs1030_8t8z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 6)
)
if mibBuilder.loadTexts:
    grs1030_8t8z.setStatus("current")
_Grs1130_16t9_ObjectIdentity = ObjectIdentity
grs1130_16t9 = _Grs1130_16t9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 7)
)
if mibBuilder.loadTexts:
    grs1130_16t9.setStatus("current")
_Grs1130_8t8z_ObjectIdentity = ObjectIdentity
grs1130_8t8z = _Grs1130_8t8z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 8)
)
if mibBuilder.loadTexts:
    grs1130_8t8z.setStatus("current")
_Grs1042_at2z_ObjectIdentity = ObjectIdentity
grs1042_at2z = _Grs1042_at2z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 1000)
)
if mibBuilder.loadTexts:
    grs1042_at2z.setStatus("current")
_Grs1142_at2z_ObjectIdentity = ObjectIdentity
grs1142_at2z = _Grs1142_at2z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 1001)
)
if mibBuilder.loadTexts:
    grs1142_at2z.setStatus("current")
_Grs1042_6t6z_ObjectIdentity = ObjectIdentity
grs1042_6t6z = _Grs1042_6t6z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 1002)
)
if mibBuilder.loadTexts:
    grs1042_6t6z.setStatus("current")
_Grs1142_6t6z_ObjectIdentity = ObjectIdentity
grs1142_6t6z = _Grs1142_6t6z_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 10, 1003)
)
if mibBuilder.loadTexts:
    grs1142_6t6z.setStatus("current")
_Octopus_ObjectIdentity = ObjectIdentity
octopus = _Octopus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11)
)
if mibBuilder.loadTexts:
    octopus.setStatus("current")
_Os20_000800_ObjectIdentity = ObjectIdentity
os20_000800 = _Os20_000800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    os20_000800.setStatus("current")
_Os20_001200_ObjectIdentity = ObjectIdentity
os20_001200 = _Os20_001200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    os20_001200.setStatus("current")
_Os20_002000_ObjectIdentity = ObjectIdentity
os20_002000 = _Os20_002000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    os20_002000.setStatus("current")
_Os20_002800_ObjectIdentity = ObjectIdentity
os20_002800 = _Os20_002800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    os20_002800.setStatus("current")
_Os24_111200_ObjectIdentity = ObjectIdentity
os24_111200 = _Os24_111200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    os24_111200.setStatus("current")
_Os24_101200_ObjectIdentity = ObjectIdentity
os24_101200 = _Os24_101200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 6)
)
if mibBuilder.loadTexts:
    os24_101200.setStatus("current")
_Os24_081200_ObjectIdentity = ObjectIdentity
os24_081200 = _Os24_081200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 7)
)
if mibBuilder.loadTexts:
    os24_081200.setStatus("current")
_Os24_152000_ObjectIdentity = ObjectIdentity
os24_152000 = _Os24_152000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 8)
)
if mibBuilder.loadTexts:
    os24_152000.setStatus("current")
_Os24_152800_ObjectIdentity = ObjectIdentity
os24_152800 = _Os24_152800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 9)
)
if mibBuilder.loadTexts:
    os24_152800.setStatus("current")
_Os24_142000_ObjectIdentity = ObjectIdentity
os24_142000 = _Os24_142000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 10)
)
if mibBuilder.loadTexts:
    os24_142000.setStatus("current")
_Os24_142800_ObjectIdentity = ObjectIdentity
os24_142800 = _Os24_142800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 11)
)
if mibBuilder.loadTexts:
    os24_142800.setStatus("current")
_Os24_122000_ObjectIdentity = ObjectIdentity
os24_122000 = _Os24_122000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 12)
)
if mibBuilder.loadTexts:
    os24_122000.setStatus("current")
_Os24_122800_ObjectIdentity = ObjectIdentity
os24_122800 = _Os24_122800_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 13)
)
if mibBuilder.loadTexts:
    os24_122800.setStatus("current")
_Os30_000802_ObjectIdentity = ObjectIdentity
os30_000802 = _Os30_000802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 14)
)
if mibBuilder.loadTexts:
    os30_000802.setStatus("current")
_Os30_001602_ObjectIdentity = ObjectIdentity
os30_001602 = _Os30_001602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 15)
)
if mibBuilder.loadTexts:
    os30_001602.setStatus("current")
_Os30_002402_ObjectIdentity = ObjectIdentity
os30_002402 = _Os30_002402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 16)
)
if mibBuilder.loadTexts:
    os30_002402.setStatus("current")
_Os34_100802_ObjectIdentity = ObjectIdentity
os34_100802 = _Os34_100802_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 17)
)
if mibBuilder.loadTexts:
    os34_100802.setStatus("current")
_Os34_141602_ObjectIdentity = ObjectIdentity
os34_141602 = _Os34_141602_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 18)
)
if mibBuilder.loadTexts:
    os34_141602.setStatus("current")
_Os34_142402_ObjectIdentity = ObjectIdentity
os34_142402 = _Os34_142402_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 19)
)
if mibBuilder.loadTexts:
    os34_142402.setStatus("current")
_Os30_000804_ObjectIdentity = ObjectIdentity
os30_000804 = _Os30_000804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 20)
)
if mibBuilder.loadTexts:
    os30_000804.setStatus("current")
_Os30_001604_ObjectIdentity = ObjectIdentity
os30_001604 = _Os30_001604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 21)
)
if mibBuilder.loadTexts:
    os30_001604.setStatus("current")
_Os30_002404_ObjectIdentity = ObjectIdentity
os30_002404 = _Os30_002404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 22)
)
if mibBuilder.loadTexts:
    os30_002404.setStatus("current")
_Os34_110804_ObjectIdentity = ObjectIdentity
os34_110804 = _Os34_110804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 23)
)
if mibBuilder.loadTexts:
    os34_110804.setStatus("current")
_Os34_100804_ObjectIdentity = ObjectIdentity
os34_100804 = _Os34_100804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 24)
)
if mibBuilder.loadTexts:
    os34_100804.setStatus("current")
_Os34_080804_ObjectIdentity = ObjectIdentity
os34_080804 = _Os34_080804_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 25)
)
if mibBuilder.loadTexts:
    os34_080804.setStatus("current")
_Os34_151604_ObjectIdentity = ObjectIdentity
os34_151604 = _Os34_151604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 26)
)
if mibBuilder.loadTexts:
    os34_151604.setStatus("current")
_Os34_152404_ObjectIdentity = ObjectIdentity
os34_152404 = _Os34_152404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 27)
)
if mibBuilder.loadTexts:
    os34_152404.setStatus("current")
_Os34_141604_ObjectIdentity = ObjectIdentity
os34_141604 = _Os34_141604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 28)
)
if mibBuilder.loadTexts:
    os34_141604.setStatus("current")
_Os34_142404_ObjectIdentity = ObjectIdentity
os34_142404 = _Os34_142404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 29)
)
if mibBuilder.loadTexts:
    os34_142404.setStatus("current")
_Os34_121604_ObjectIdentity = ObjectIdentity
os34_121604 = _Os34_121604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 30)
)
if mibBuilder.loadTexts:
    os34_121604.setStatus("current")
_Os34_122404_ObjectIdentity = ObjectIdentity
os34_122404 = _Os34_122404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 11, 31)
)
if mibBuilder.loadTexts:
    os34_122404.setStatus("current")
_Red_ObjectIdentity = ObjectIdentity
red = _Red_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 12)
)
if mibBuilder.loadTexts:
    red.setStatus("current")
_Red25_04002t1tt_ObjectIdentity = ObjectIdentity
red25_04002t1tt = _Red25_04002t1tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    red25_04002t1tt.setStatus("current")
_Red25_04002z6tt_ObjectIdentity = ObjectIdentity
red25_04002z6tt = _Red25_04002z6tt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 12, 2)
)
if mibBuilder.loadTexts:
    red25_04002z6tt.setStatus("current")
_Rdd_ObjectIdentity = ObjectIdentity
rdd = _Rdd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 13)
)
if mibBuilder.loadTexts:
    rdd.setStatus("current")
_Raildatadiodeinput_ObjectIdentity = ObjectIdentity
raildatadiodeinput = _Raildatadiodeinput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    raildatadiodeinput.setStatus("current")
_Raildatadiodeoutput_ObjectIdentity = ObjectIdentity
raildatadiodeoutput = _Raildatadiodeoutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    raildatadiodeoutput.setStatus("current")
_Hm2ModuleFamily_ObjectIdentity = ObjectIdentity
hm2ModuleFamily = _Hm2ModuleFamily_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2)
)
if mibBuilder.loadTexts:
    hm2ModuleFamily.setStatus("current")
_Msm_ObjectIdentity = ObjectIdentity
msm = _Msm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1)
)
if mibBuilder.loadTexts:
    msm.setStatus("current")
_Msm_4tx_ObjectIdentity = ObjectIdentity
msm_4tx = _Msm_4tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    msm_4tx.setStatus("current")
_Msm_3tx_1fx_ObjectIdentity = ObjectIdentity
msm_3tx_1fx = _Msm_3tx_1fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    msm_3tx_1fx.setStatus("current")
_Msm_2tx_2fx_ObjectIdentity = ObjectIdentity
msm_2tx_2fx = _Msm_2tx_2fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    msm_2tx_2fx.setStatus("current")
_Msm_1tx_3fx_ObjectIdentity = ObjectIdentity
msm_1tx_3fx = _Msm_1tx_3fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    msm_1tx_3fx.setStatus("current")
_Msm_4fx_ObjectIdentity = ObjectIdentity
msm_4fx = _Msm_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    msm_4fx.setStatus("current")
_Msm_4txfx_ObjectIdentity = ObjectIdentity
msm_4txfx = _Msm_4txfx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    msm_4txfx.setStatus("current")
_Msm_4io_ObjectIdentity = ObjectIdentity
msm_4io = _Msm_4io_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 1, 100)
)
if mibBuilder.loadTexts:
    msm_4io.setStatus("current")
_Rspm_ObjectIdentity = ObjectIdentity
rspm = _Rspm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rspm.setStatus("current")
_Rspm20_8tx_ObjectIdentity = ObjectIdentity
rspm20_8tx = _Rspm20_8tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rspm20_8tx.setStatus("current")
_Rspm22_8tx_ObjectIdentity = ObjectIdentity
rspm22_8tx = _Rspm22_8tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rspm22_8tx.setStatus("current")
_Rspm20_4tx_4fx_ObjectIdentity = ObjectIdentity
rspm20_4tx_4fx = _Rspm20_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rspm20_4tx_4fx.setStatus("current")
_Rspm22_4tx_4fx_ObjectIdentity = ObjectIdentity
rspm22_4tx_4fx = _Rspm22_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    rspm22_4tx_4fx.setStatus("current")
_Rspm20_8fx_ObjectIdentity = ObjectIdentity
rspm20_8fx = _Rspm20_8fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    rspm20_8fx.setStatus("current")
_Grm_ObjectIdentity = ObjectIdentity
grm = _Grm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 3)
)
if mibBuilder.loadTexts:
    grm.setStatus("current")
_Grm20_8tx_ObjectIdentity = ObjectIdentity
grm20_8tx = _Grm20_8tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    grm20_8tx.setStatus("current")
_Grm20_8fx_ObjectIdentity = ObjectIdentity
grm20_8fx = _Grm20_8fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    grm20_8fx.setStatus("current")
_Grm20_4tx_4fx_ObjectIdentity = ObjectIdentity
grm20_4tx_4fx = _Grm20_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    grm20_4tx_4fx.setStatus("current")
_Gmm_ObjectIdentity = ObjectIdentity
gmm = _Gmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4)
)
if mibBuilder.loadTexts:
    gmm.setStatus("current")
_Gmm20_8fx_ObjectIdentity = ObjectIdentity
gmm20_8fx = _Gmm20_8fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    gmm20_8fx.setStatus("current")
_Gmm30_4tx_4fx_ObjectIdentity = ObjectIdentity
gmm30_4tx_4fx = _Gmm30_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 2)
)
if mibBuilder.loadTexts:
    gmm30_4tx_4fx.setStatus("current")
_Gmm32_4tx_4fx_ObjectIdentity = ObjectIdentity
gmm32_4tx_4fx = _Gmm32_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    gmm32_4tx_4fx.setStatus("current")
_Gmm40_4tx_4fx_ObjectIdentity = ObjectIdentity
gmm40_4tx_4fx = _Gmm40_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 4)
)
if mibBuilder.loadTexts:
    gmm40_4tx_4fx.setStatus("current")
_Gmm40_8fx_ObjectIdentity = ObjectIdentity
gmm40_8fx = _Gmm40_8fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 5)
)
if mibBuilder.loadTexts:
    gmm40_8fx.setStatus("current")
_Gmm40_8tx_ObjectIdentity = ObjectIdentity
gmm40_8tx = _Gmm40_8tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 6)
)
if mibBuilder.loadTexts:
    gmm40_8tx.setStatus("current")
_Gmm42_4tx_4fx_ObjectIdentity = ObjectIdentity
gmm42_4tx_4fx = _Gmm42_4tx_4fx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 7)
)
if mibBuilder.loadTexts:
    gmm42_4tx_4fx.setStatus("current")
_Gmm42_8tx_ObjectIdentity = ObjectIdentity
gmm42_8tx = _Gmm42_8tx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 2, 2, 4, 8)
)
if mibBuilder.loadTexts:
    gmm42_8tx.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PRODUCTS-MIB",
    **{"hm2ProductsMib": hm2ProductsMib,
       "hm2ProductFamily": hm2ProductFamily,
       "ees": ees,
       "ees20-0600": ees20_0600,
       "ees25-0600": ees25_0600,
       "rsp": rsp,
       "rsp20-11003z6tt": rsp20_11003z6tt,
       "rsp20-11003z6zt": rsp20_11003z6zt,
       "rsp25-11003z6tt": rsp25_11003z6tt,
       "rsp25-11003z6zt": rsp25_11003z6zt,
       "rsp30-08033o6tt": rsp30_08033o6tt,
       "rsp30-08033o6zt": rsp30_08033o6zt,
       "rsp35-08033o6tt": rsp35_08033o6tt,
       "rsp35-08033o6zt": rsp35_08033o6zt,
       "eagle": eagle,
       "eagle20-0400999TT999": eagle20_0400999TT999,
       "eagle20-0400999TTC99": eagle20_0400999TTC99,
       "eagle20-0400999TTCAA": eagle20_0400999TTCAA,
       "eagle20-0400999TTCAB": eagle20_0400999TTCAB,
       "eagle20-0400999TTCVA": eagle20_0400999TTCVA,
       "eagle20-0400999TTCVB": eagle20_0400999TTCVB,
       "eagle20-0400999TTCH2": eagle20_0400999TTCH2,
       "eagle20-0400999TTCP2": eagle20_0400999TTCP2,
       "eagle20-0400999TT9AA": eagle20_0400999TT9AA,
       "eagle20-0400999TT9AB": eagle20_0400999TT9AB,
       "eagle20-0400999TT9VA": eagle20_0400999TT9VA,
       "eagle20-0400999TT9VB": eagle20_0400999TT9VB,
       "eagle20-0400999TT9H2": eagle20_0400999TT9H2,
       "eagle20-0400999TT9P2": eagle20_0400999TT9P2,
       "eagle30-04022O6TT999": eagle30_04022O6TT999,
       "eagle30-04022O6TTC99": eagle30_04022O6TTC99,
       "eagle30-04022O6TTCAA": eagle30_04022O6TTCAA,
       "eagle30-04022O6TTCAB": eagle30_04022O6TTCAB,
       "eagle30-04022O6TTCVA": eagle30_04022O6TTCVA,
       "eagle30-04022O6TTCVB": eagle30_04022O6TTCVB,
       "eagle30-04022O6TTCH2": eagle30_04022O6TTCH2,
       "eagle30-04022O6TTCP2": eagle30_04022O6TTCP2,
       "eagle30-04022O6TT9AA": eagle30_04022O6TT9AA,
       "eagle30-04022O6TT9AB": eagle30_04022O6TT9AB,
       "eagle30-04022O6TT9VA": eagle30_04022O6TT9VA,
       "eagle30-04022O6TT9VB": eagle30_04022O6TT9VB,
       "eagle30-04022O6TT9H2": eagle30_04022O6TT9H2,
       "eagle30-04022O6TT9P2": eagle30_04022O6TT9P2,
       "msp": msp,
       "msp30-0804": msp30_0804,
       "msp32-0804": msp32_0804,
       "msp30-1604": msp30_1604,
       "msp32-1604": msp32_1604,
       "msp30-2404": msp30_2404,
       "msp32-2404": msp32_2404,
       "rsps": rsps,
       "rsps20-06002z6yt": rsps20_06002z6yt,
       "rsps20-06002z6tt": rsps20_06002z6tt,
       "rsps20-06002t1tt": rsps20_06002t1tt,
       "rsps25-06002z6yt": rsps25_06002z6yt,
       "rsps25-06002z6tt": rsps25_06002z6tt,
       "rsps25-06002t1tt": rsps25_06002t1tt,
       "rspl": rspl,
       "rspl20-08002z6tt": rspl20_08002z6tt,
       "rspl20-08002z6yt": rspl20_08002z6yt,
       "rspl30-08022o7yt": rspl30_08022o7yt,
       "rspl30-08022o7zt": rspl30_08022o7zt,
       "eesx": eesx,
       "eesx20-0800": eesx20_0800,
       "eesx30-0802": eesx30_0802,
       "rspe": rspe,
       "rspe30-24044O7T99": rspe30_24044O7T99,
       "rspe32-24044O7T99": rspe32_24044O7T99,
       "rspe35-24044O7T99": rspe35_24044O7T99,
       "rspe37-24044O7T99": rspe37_24044O7T99,
       "tofino": tofino,
       "grs": grs,
       "grs1020-16t9": grs1020_16t9,
       "grs1020-8t8z": grs1020_8t8z,
       "grs1120-16t9": grs1120_16t9,
       "grs1120-8t8z": grs1120_8t8z,
       "grs1030-16t9": grs1030_16t9,
       "grs1030-8t8z": grs1030_8t8z,
       "grs1130-16t9": grs1130_16t9,
       "grs1130-8t8z": grs1130_8t8z,
       "grs1042-at2z": grs1042_at2z,
       "grs1142-at2z": grs1142_at2z,
       "grs1042-6t6z": grs1042_6t6z,
       "grs1142-6t6z": grs1142_6t6z,
       "octopus": octopus,
       "os20-000800": os20_000800,
       "os20-001200": os20_001200,
       "os20-002000": os20_002000,
       "os20-002800": os20_002800,
       "os24-111200": os24_111200,
       "os24-101200": os24_101200,
       "os24-081200": os24_081200,
       "os24-152000": os24_152000,
       "os24-152800": os24_152800,
       "os24-142000": os24_142000,
       "os24-142800": os24_142800,
       "os24-122000": os24_122000,
       "os24-122800": os24_122800,
       "os30-000802": os30_000802,
       "os30-001602": os30_001602,
       "os30-002402": os30_002402,
       "os34-100802": os34_100802,
       "os34-141602": os34_141602,
       "os34-142402": os34_142402,
       "os30-000804": os30_000804,
       "os30-001604": os30_001604,
       "os30-002404": os30_002404,
       "os34-110804": os34_110804,
       "os34-100804": os34_100804,
       "os34-080804": os34_080804,
       "os34-151604": os34_151604,
       "os34-152404": os34_152404,
       "os34-141604": os34_141604,
       "os34-142404": os34_142404,
       "os34-121604": os34_121604,
       "os34-122404": os34_122404,
       "red": red,
       "red25-04002t1tt": red25_04002t1tt,
       "red25-04002z6tt": red25_04002z6tt,
       "rdd": rdd,
       "raildatadiodeinput": raildatadiodeinput,
       "raildatadiodeoutput": raildatadiodeoutput,
       "hm2ModuleFamily": hm2ModuleFamily,
       "msm": msm,
       "msm-4tx": msm_4tx,
       "msm-3tx-1fx": msm_3tx_1fx,
       "msm-2tx-2fx": msm_2tx_2fx,
       "msm-1tx-3fx": msm_1tx_3fx,
       "msm-4fx": msm_4fx,
       "msm-4txfx": msm_4txfx,
       "msm-4io": msm_4io,
       "rspm": rspm,
       "rspm20-8tx": rspm20_8tx,
       "rspm22-8tx": rspm22_8tx,
       "rspm20-4tx-4fx": rspm20_4tx_4fx,
       "rspm22-4tx-4fx": rspm22_4tx_4fx,
       "rspm20-8fx": rspm20_8fx,
       "grm": grm,
       "grm20-8tx": grm20_8tx,
       "grm20-8fx": grm20_8fx,
       "grm20-4tx-4fx": grm20_4tx_4fx,
       "gmm": gmm,
       "gmm20-8fx": gmm20_8fx,
       "gmm30-4tx-4fx": gmm30_4tx_4fx,
       "gmm32-4tx-4fx": gmm32_4tx_4fx,
       "gmm40-4tx-4fx": gmm40_4tx_4fx,
       "gmm40-8fx": gmm40_8fx,
       "gmm40-8tx": gmm40_8tx,
       "gmm42-4tx-4fx": gmm42_4tx_4fx,
       "gmm42-8tx": gmm42_8tx}
)
