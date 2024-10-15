# SNMP MIB module (CPS6000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPS6000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:49 2024
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

cps6000 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1)
)
cps6000.setRevisions(
        ("2009-06-18 16:17",
         "2009-05-27 22:43",
         "2007-03-21 21:56",
         "2006-01-20 16:18",
         "2005-10-11 18:47")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Teps_ObjectIdentity = ObjectIdentity
teps = _Teps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520)
)
_Controllermibs_ObjectIdentity = ObjectIdentity
controllermibs = _Controllermibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2)
)
_Release_ObjectIdentity = ObjectIdentity
release = _Release_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1)
)
_Cps6000Dc1_ObjectIdentity = ObjectIdentity
cps6000Dc1 = _Cps6000Dc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1)
)
_Cps6000Dc1Ide_Type = DisplayString
_Cps6000Dc1Ide_Object = MibScalar
cps6000Dc1Ide = _Cps6000Dc1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 1),
    _Cps6000Dc1Ide_Type()
)
cps6000Dc1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Ide.setStatus("current")
_Cps6000Dc1Des_Type = DisplayString
_Cps6000Dc1Des_Object = MibScalar
cps6000Dc1Des = _Cps6000Dc1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 2),
    _Cps6000Dc1Des_Type()
)
cps6000Dc1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Des.setStatus("current")
_Cps6000Dc1Typ_Type = DisplayString
_Cps6000Dc1Typ_Object = MibScalar
cps6000Dc1Typ = _Cps6000Dc1Typ_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 3),
    _Cps6000Dc1Typ_Type()
)
cps6000Dc1Typ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Typ.setStatus("current")
_Cps6000Dc1Stt_Type = DisplayString
_Cps6000Dc1Stt_Object = MibScalar
cps6000Dc1Stt = _Cps6000Dc1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 4),
    _Cps6000Dc1Stt_Type()
)
cps6000Dc1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Stt.setStatus("current")
_Cps6000Dc1Vdc_Type = Integer32
_Cps6000Dc1Vdc_Object = MibScalar
cps6000Dc1Vdc = _Cps6000Dc1Vdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 5),
    _Cps6000Dc1Vdc_Type()
)
cps6000Dc1Vdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Vdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Vdc.setUnits("mV")
_Cps6000Dc1Adc_Type = Integer32
_Cps6000Dc1Adc_Object = MibScalar
cps6000Dc1Adc = _Cps6000Dc1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 6),
    _Cps6000Dc1Adc_Type()
)
cps6000Dc1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Adc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Adc.setUnits("Amps")
_Cps6000Dc1Cap_Type = Integer32
_Cps6000Dc1Cap_Object = MibScalar
cps6000Dc1Cap = _Cps6000Dc1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 7),
    _Cps6000Dc1Cap_Type()
)
cps6000Dc1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Cap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Cap.setUnits("Amps")
_Cps6000Dc1Olcap_Type = Integer32
_Cps6000Dc1Olcap_Object = MibScalar
cps6000Dc1Olcap = _Cps6000Dc1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 8),
    _Cps6000Dc1Olcap_Type()
)
cps6000Dc1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Olcap.setUnits("Amps")
_Cps6000Dc1Scap_Type = Integer32
_Cps6000Dc1Scap_Object = MibScalar
cps6000Dc1Scap = _Cps6000Dc1Scap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 9),
    _Cps6000Dc1Scap_Type()
)
cps6000Dc1Scap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Scap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Scap.setUnits("Amps")
_Cps6000Dc1Nst_Type = Integer32
_Cps6000Dc1Nst_Object = MibScalar
cps6000Dc1Nst = _Cps6000Dc1Nst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 10),
    _Cps6000Dc1Nst_Type()
)
cps6000Dc1Nst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Nst.setStatus("current")
_Cps6000Dc1Cps_Type = Integer32
_Cps6000Dc1Cps_Object = MibScalar
cps6000Dc1Cps = _Cps6000Dc1Cps_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 11),
    _Cps6000Dc1Cps_Type()
)
cps6000Dc1Cps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Cps.setStatus("current")
_Cps6000Dc1Bty_Type = DisplayString
_Cps6000Dc1Bty_Object = MibScalar
cps6000Dc1Bty = _Cps6000Dc1Bty_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 12),
    _Cps6000Dc1Bty_Type()
)
cps6000Dc1Bty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Bty.setStatus("current")
_Cps6000Dc1Trd_Type = Integer32
_Cps6000Dc1Trd_Object = MibScalar
cps6000Dc1Trd = _Cps6000Dc1Trd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 13),
    _Cps6000Dc1Trd_Type()
)
cps6000Dc1Trd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Trd.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Trd.setUnits("Amps")


class _Cps6000Dc1Isd_Type(Integer32):
    """Custom type cps6000Dc1Isd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Dc1Isd_Type.__name__ = "Integer32"
_Cps6000Dc1Isd_Object = MibScalar
cps6000Dc1Isd = _Cps6000Dc1Isd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 14),
    _Cps6000Dc1Isd_Type()
)
cps6000Dc1Isd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Isd.setStatus("current")
_Cps6000Dc1Bod_Type = DisplayString
_Cps6000Dc1Bod_Object = MibScalar
cps6000Dc1Bod = _Cps6000Dc1Bod_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 15),
    _Cps6000Dc1Bod_Type()
)
cps6000Dc1Bod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Bod.setStatus("current")


class _Cps6000Dc1Rss_Type(Integer32):
    """Custom type cps6000Dc1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cps6000Dc1Rss_Type.__name__ = "Integer32"
_Cps6000Dc1Rss_Object = MibScalar
cps6000Dc1Rss = _Cps6000Dc1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 16),
    _Cps6000Dc1Rss_Type()
)
cps6000Dc1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Rss.setStatus("current")


class _Cps6000Dc1Rot_Type(Integer32):
    """Custom type cps6000Dc1Rot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 50000),
    )


_Cps6000Dc1Rot_Type.__name__ = "Integer32"
_Cps6000Dc1Rot_Object = MibScalar
cps6000Dc1Rot = _Cps6000Dc1Rot_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 17),
    _Cps6000Dc1Rot_Type()
)
cps6000Dc1Rot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Rot.setStatus("current")
_Cps6000Dc1Bst_Type = DisplayString
_Cps6000Dc1Bst_Object = MibScalar
cps6000Dc1Bst = _Cps6000Dc1Bst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 18),
    _Cps6000Dc1Bst_Type()
)
cps6000Dc1Bst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Bst.setStatus("current")
_Cps6000Dc1Amj_Type = DisplayString
_Cps6000Dc1Amj_Object = MibScalar
cps6000Dc1Amj = _Cps6000Dc1Amj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 19),
    _Cps6000Dc1Amj_Type()
)
cps6000Dc1Amj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Amj.setStatus("current")
_Cps6000Dc1Epo_Type = DisplayString
_Cps6000Dc1Epo_Object = MibScalar
cps6000Dc1Epo = _Cps6000Dc1Epo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 20),
    _Cps6000Dc1Epo_Type()
)
cps6000Dc1Epo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Epo.setStatus("current")
_Cps6000Dc1Faj_Type = DisplayString
_Cps6000Dc1Faj_Object = MibScalar
cps6000Dc1Faj = _Cps6000Dc1Faj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 21),
    _Cps6000Dc1Faj_Type()
)
cps6000Dc1Faj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Faj.setStatus("current")
_Cps6000Dc1Fan_Type = DisplayString
_Cps6000Dc1Fan_Object = MibScalar
cps6000Dc1Fan = _Cps6000Dc1Fan_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 22),
    _Cps6000Dc1Fan_Type()
)
cps6000Dc1Fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Fan.setStatus("current")
_Cps6000Dc1Vsf_Type = DisplayString
_Cps6000Dc1Vsf_Object = MibScalar
cps6000Dc1Vsf = _Cps6000Dc1Vsf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 23),
    _Cps6000Dc1Vsf_Type()
)
cps6000Dc1Vsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Vsf.setStatus("current")
_Cps6000Dc1Osa_Type = DisplayString
_Cps6000Dc1Osa_Object = MibScalar
cps6000Dc1Osa = _Cps6000Dc1Osa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 24),
    _Cps6000Dc1Osa_Type()
)
cps6000Dc1Osa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Osa.setStatus("current")
_Cps6000Dc1Zid_Type = DisplayString
_Cps6000Dc1Zid_Object = MibScalar
cps6000Dc1Zid = _Cps6000Dc1Zid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 25),
    _Cps6000Dc1Zid_Type()
)
cps6000Dc1Zid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Zid.setStatus("current")
_Cps6000Dc1Tpa_Type = DisplayString
_Cps6000Dc1Tpa_Object = MibScalar
cps6000Dc1Tpa = _Cps6000Dc1Tpa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 26),
    _Cps6000Dc1Tpa_Type()
)
cps6000Dc1Tpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Tpa.setStatus("current")
_Cps6000Dc1Vmf_Type = DisplayString
_Cps6000Dc1Vmf_Object = MibScalar
cps6000Dc1Vmf = _Cps6000Dc1Vmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 27),
    _Cps6000Dc1Vmf_Type()
)
cps6000Dc1Vmf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Vmf.setStatus("current")
_Cps6000Dc1Cma_Type = DisplayString
_Cps6000Dc1Cma_Object = MibScalar
cps6000Dc1Cma = _Cps6000Dc1Cma_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 28),
    _Cps6000Dc1Cma_Type()
)
cps6000Dc1Cma.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Cma.setStatus("current")
_Cps6000Dc1Macf_Type = DisplayString
_Cps6000Dc1Macf_Object = MibScalar
cps6000Dc1Macf = _Cps6000Dc1Macf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 29),
    _Cps6000Dc1Macf_Type()
)
cps6000Dc1Macf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Macf.setStatus("current")
_Cps6000Dc1Mcm_Type = DisplayString
_Cps6000Dc1Mcm_Object = MibScalar
cps6000Dc1Mcm = _Cps6000Dc1Mcm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 30),
    _Cps6000Dc1Mcm_Type()
)
cps6000Dc1Mcm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Mcm.setStatus("current")
_Cps6000Dc1Rfa_Type = DisplayString
_Cps6000Dc1Rfa_Object = MibScalar
cps6000Dc1Rfa = _Cps6000Dc1Rfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 31),
    _Cps6000Dc1Rfa_Type()
)
cps6000Dc1Rfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rfa.setStatus("current")
_Cps6000Dc1Did_Type = DisplayString
_Cps6000Dc1Did_Object = MibScalar
cps6000Dc1Did = _Cps6000Dc1Did_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 32),
    _Cps6000Dc1Did_Type()
)
cps6000Dc1Did.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Did.setStatus("current")
_Cps6000Dc1Clm_Type = DisplayString
_Cps6000Dc1Clm_Object = MibScalar
cps6000Dc1Clm = _Cps6000Dc1Clm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 33),
    _Cps6000Dc1Clm_Type()
)
cps6000Dc1Clm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Clm.setStatus("current")
_Cps6000Dc1Vla_Type = DisplayString
_Cps6000Dc1Vla_Object = MibScalar
cps6000Dc1Vla = _Cps6000Dc1Vla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 34),
    _Cps6000Dc1Vla_Type()
)
cps6000Dc1Vla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Vla.setStatus("current")
_Cps6000Dc1Acf_Type = DisplayString
_Cps6000Dc1Acf_Object = MibScalar
cps6000Dc1Acf = _Cps6000Dc1Acf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 35),
    _Cps6000Dc1Acf_Type()
)
cps6000Dc1Acf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Acf.setStatus("current")
_Cps6000Dc1Man_Type = DisplayString
_Cps6000Dc1Man_Object = MibScalar
cps6000Dc1Man = _Cps6000Dc1Man_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 36),
    _Cps6000Dc1Man_Type()
)
cps6000Dc1Man.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Man.setStatus("current")
_Cps6000Dc1Mman_Type = DisplayString
_Cps6000Dc1Mman_Object = MibScalar
cps6000Dc1Mman = _Cps6000Dc1Mman_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 37),
    _Cps6000Dc1Mman_Type()
)
cps6000Dc1Mman.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Mman.setStatus("current")
_Cps6000Dc1Mfa_Type = DisplayString
_Cps6000Dc1Mfa_Object = MibScalar
cps6000Dc1Mfa = _Cps6000Dc1Mfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 38),
    _Cps6000Dc1Mfa_Type()
)
cps6000Dc1Mfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Mfa.setStatus("current")
_Cps6000Dc1Rtl_Type = DisplayString
_Cps6000Dc1Rtl_Object = MibScalar
cps6000Dc1Rtl = _Cps6000Dc1Rtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 39),
    _Cps6000Dc1Rtl_Type()
)
cps6000Dc1Rtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rtl.setStatus("current")
_Cps6000Dc1Rrtl_Type = DisplayString
_Cps6000Dc1Rrtl_Object = MibScalar
cps6000Dc1Rrtl = _Cps6000Dc1Rrtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 40),
    _Cps6000Dc1Rrtl_Type()
)
cps6000Dc1Rrtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rrtl.setStatus("current")
_Cps6000Dc1Rls_Type = DisplayString
_Cps6000Dc1Rls_Object = MibScalar
cps6000Dc1Rls = _Cps6000Dc1Rls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 41),
    _Cps6000Dc1Rls_Type()
)
cps6000Dc1Rls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rls.setStatus("current")
_Cps6000Dc1Bda_Type = DisplayString
_Cps6000Dc1Bda_Object = MibScalar
cps6000Dc1Bda = _Cps6000Dc1Bda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 42),
    _Cps6000Dc1Bda_Type()
)
cps6000Dc1Bda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Bda.setStatus("current")
_Cps6000Dc1Hva_Type = DisplayString
_Cps6000Dc1Hva_Object = MibScalar
cps6000Dc1Hva = _Cps6000Dc1Hva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 43),
    _Cps6000Dc1Hva_Type()
)
cps6000Dc1Hva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Hva.setStatus("current")
_Cps6000Dc1Hfv_Type = DisplayString
_Cps6000Dc1Hfv_Object = MibScalar
cps6000Dc1Hfv = _Cps6000Dc1Hfv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 44),
    _Cps6000Dc1Hfv_Type()
)
cps6000Dc1Hfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Hfv.setStatus("current")
_Cps6000Dc1Ron_Type = Integer32
_Cps6000Dc1Ron_Object = MibScalar
cps6000Dc1Ron = _Cps6000Dc1Ron_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 45),
    _Cps6000Dc1Ron_Type()
)
cps6000Dc1Ron.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Ron.setStatus("current")


class _Cps6000Dc1Rsq_Type(Integer32):
    """Custom type cps6000Dc1Rsq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Dc1Rsq_Type.__name__ = "Integer32"
_Cps6000Dc1Rsq_Object = MibScalar
cps6000Dc1Rsq = _Cps6000Dc1Rsq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 46),
    _Cps6000Dc1Rsq_Type()
)
cps6000Dc1Rsq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Rsq.setStatus("current")
_Cps6000Dc1Rtm_Type = DisplayString
_Cps6000Dc1Rtm_Object = MibScalar
cps6000Dc1Rtm = _Cps6000Dc1Rtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 47),
    _Cps6000Dc1Rtm_Type()
)
cps6000Dc1Rtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rtm.setStatus("current")
_Cps6000Dc1Icr_Type = DisplayString
_Cps6000Dc1Icr_Object = MibScalar
cps6000Dc1Icr = _Cps6000Dc1Icr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 48),
    _Cps6000Dc1Icr_Type()
)
cps6000Dc1Icr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Icr.setStatus("current")
_Cps6000Dc1Rfn_Type = DisplayString
_Cps6000Dc1Rfn_Object = MibScalar
cps6000Dc1Rfn = _Cps6000Dc1Rfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 49),
    _Cps6000Dc1Rfn_Type()
)
cps6000Dc1Rfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Rfn.setStatus("current")
_Cps6000Dc1Emd_Type = DisplayString
_Cps6000Dc1Emd_Object = MibScalar
cps6000Dc1Emd = _Cps6000Dc1Emd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 50),
    _Cps6000Dc1Emd_Type()
)
cps6000Dc1Emd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Emd.setStatus("current")


class _Cps6000Dc1Mls_Type(Integer32):
    """Custom type cps6000Dc1Mls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Dc1Mls_Type.__name__ = "Integer32"
_Cps6000Dc1Mls_Object = MibScalar
cps6000Dc1Mls = _Cps6000Dc1Mls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 51),
    _Cps6000Dc1Mls_Type()
)
cps6000Dc1Mls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Mls.setStatus("current")
_Cps6000Dc1Bdt_Type = DisplayString
_Cps6000Dc1Bdt_Object = MibScalar
cps6000Dc1Bdt = _Cps6000Dc1Bdt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 52),
    _Cps6000Dc1Bdt_Type()
)
cps6000Dc1Bdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Bdt.setStatus("current")
_Cps6000Dc1Ems_Type = DisplayString
_Cps6000Dc1Ems_Object = MibScalar
cps6000Dc1Ems = _Cps6000Dc1Ems_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 53),
    _Cps6000Dc1Ems_Type()
)
cps6000Dc1Ems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Ems.setStatus("current")


class _Cps6000Dc1Eme_Type(Integer32):
    """Custom type cps6000Dc1Eme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Dc1Eme_Type.__name__ = "Integer32"
_Cps6000Dc1Eme_Object = MibScalar
cps6000Dc1Eme = _Cps6000Dc1Eme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 54),
    _Cps6000Dc1Eme_Type()
)
cps6000Dc1Eme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Eme.setStatus("current")


class _Cps6000Dc1Emt_Type(Integer32):
    """Custom type cps6000Dc1Emt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 95),
    )


_Cps6000Dc1Emt_Type.__name__ = "Integer32"
_Cps6000Dc1Emt_Object = MibScalar
cps6000Dc1Emt = _Cps6000Dc1Emt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 55),
    _Cps6000Dc1Emt_Type()
)
cps6000Dc1Emt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Emt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Emt.setUnits("%")


class _Cps6000Dc1Emo_Type(Integer32):
    """Custom type cps6000Dc1Emo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_Cps6000Dc1Emo_Type.__name__ = "Integer32"
_Cps6000Dc1Emo_Object = MibScalar
cps6000Dc1Emo = _Cps6000Dc1Emo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 56),
    _Cps6000Dc1Emo_Type()
)
cps6000Dc1Emo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dc1Emo.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Emo.setUnits("%")
_Cps6000Dc1Poc_Type = DisplayString
_Cps6000Dc1Poc_Object = MibScalar
cps6000Dc1Poc = _Cps6000Dc1Poc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 57),
    _Cps6000Dc1Poc_Type()
)
cps6000Dc1Poc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Poc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Dc1Poc.setUnits("%")
_Cps6000Dc1Lsf_Type = DisplayString
_Cps6000Dc1Lsf_Object = MibScalar
cps6000Dc1Lsf = _Cps6000Dc1Lsf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 1, 58),
    _Cps6000Dc1Lsf_Type()
)
cps6000Dc1Lsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dc1Lsf.setStatus("current")
_Cps6000Ps1_ObjectIdentity = ObjectIdentity
cps6000Ps1 = _Cps6000Ps1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2)
)
_Cps6000Ps1Ide_Type = DisplayString
_Cps6000Ps1Ide_Object = MibScalar
cps6000Ps1Ide = _Cps6000Ps1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 1),
    _Cps6000Ps1Ide_Type()
)
cps6000Ps1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ide.setStatus("current")
_Cps6000Ps1Des_Type = DisplayString
_Cps6000Ps1Des_Object = MibScalar
cps6000Ps1Des = _Cps6000Ps1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 2),
    _Cps6000Ps1Des_Type()
)
cps6000Ps1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Des.setStatus("current")
_Cps6000Ps1Sid_Type = DisplayString
_Cps6000Ps1Sid_Object = MibScalar
cps6000Ps1Sid = _Cps6000Ps1Sid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 3),
    _Cps6000Ps1Sid_Type()
)
cps6000Ps1Sid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Sid.setStatus("current")
_Cps6000Ps1Sde_Type = DisplayString
_Cps6000Ps1Sde_Object = MibScalar
cps6000Ps1Sde = _Cps6000Ps1Sde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 4),
    _Cps6000Ps1Sde_Type()
)
cps6000Ps1Sde.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Sde.setStatus("current")
_Cps6000Ps1Swv_Type = DisplayString
_Cps6000Ps1Swv_Object = MibScalar
cps6000Ps1Swv = _Cps6000Ps1Swv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 5),
    _Cps6000Ps1Swv_Type()
)
cps6000Ps1Swv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Swv.setStatus("current")
_Cps6000Ps1Verb_Type = DisplayString
_Cps6000Ps1Verb_Object = MibScalar
cps6000Ps1Verb = _Cps6000Ps1Verb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 6),
    _Cps6000Ps1Verb_Type()
)
cps6000Ps1Verb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Verb.setStatus("current")
_Cps6000Ps1Verw_Type = DisplayString
_Cps6000Ps1Verw_Object = MibScalar
cps6000Ps1Verw = _Cps6000Ps1Verw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 7),
    _Cps6000Ps1Verw_Type()
)
cps6000Ps1Verw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Verw.setStatus("current")
_Cps6000Ps1Verd_Type = DisplayString
_Cps6000Ps1Verd_Object = MibScalar
cps6000Ps1Verd = _Cps6000Ps1Verd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 8),
    _Cps6000Ps1Verd_Type()
)
cps6000Ps1Verd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Verd.setStatus("current")
_Cps6000Ps1Dflt_Type = DisplayString
_Cps6000Ps1Dflt_Object = MibScalar
cps6000Ps1Dflt = _Cps6000Ps1Dflt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 9),
    _Cps6000Ps1Dflt_Type()
)
cps6000Ps1Dflt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Dflt.setStatus("current")
_Cps6000Ps1Brc_Type = DisplayString
_Cps6000Ps1Brc_Object = MibScalar
cps6000Ps1Brc = _Cps6000Ps1Brc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 10),
    _Cps6000Ps1Brc_Type()
)
cps6000Ps1Brc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Brc.setStatus("current")
_Cps6000Ps1Sn_Type = DisplayString
_Cps6000Ps1Sn_Object = MibScalar
cps6000Ps1Sn = _Cps6000Ps1Sn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 11),
    _Cps6000Ps1Sn_Type()
)
cps6000Ps1Sn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Sn.setStatus("current")


class _Cps6000Ps1Usl_Type(Integer32):
    """Custom type cps6000Ps1Usl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("uninstall", 1)
    )


_Cps6000Ps1Usl_Type.__name__ = "Integer32"
_Cps6000Ps1Usl_Object = MibScalar
cps6000Ps1Usl = _Cps6000Ps1Usl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 12),
    _Cps6000Ps1Usl_Type()
)
cps6000Ps1Usl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Usl.setStatus("current")
_Cps6000Ps1Dat_Type = DisplayString
_Cps6000Ps1Dat_Object = MibScalar
cps6000Ps1Dat = _Cps6000Ps1Dat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 13),
    _Cps6000Ps1Dat_Type()
)
cps6000Ps1Dat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Dat.setStatus("current")
_Cps6000Ps1Dtf_Type = DisplayString
_Cps6000Ps1Dtf_Object = MibScalar
cps6000Ps1Dtf = _Cps6000Ps1Dtf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 14),
    _Cps6000Ps1Dtf_Type()
)
cps6000Ps1Dtf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Dtf.setStatus("current")
_Cps6000Ps1Tim_Type = DisplayString
_Cps6000Ps1Tim_Object = MibScalar
cps6000Ps1Tim = _Cps6000Ps1Tim_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 15),
    _Cps6000Ps1Tim_Type()
)
cps6000Ps1Tim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Tim.setStatus("current")


class _Cps6000Ps1Tmf_Type(Integer32):
    """Custom type cps6000Ps1Tmf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(12,
              24)
        )
    )
    namedValues = NamedValues(
        *(("h12", 12),
          ("h24", 24))
    )


_Cps6000Ps1Tmf_Type.__name__ = "Integer32"
_Cps6000Ps1Tmf_Object = MibScalar
cps6000Ps1Tmf = _Cps6000Ps1Tmf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 16),
    _Cps6000Ps1Tmf_Type()
)
cps6000Ps1Tmf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Tmf.setStatus("current")


class _Cps6000Ps1Dls_Type(Integer32):
    """Custom type cps6000Ps1Dls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cps6000Ps1Dls_Type.__name__ = "Integer32"
_Cps6000Ps1Dls_Object = MibScalar
cps6000Ps1Dls = _Cps6000Ps1Dls_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 17),
    _Cps6000Ps1Dls_Type()
)
cps6000Ps1Dls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Dls.setStatus("current")
_Cps6000Ps1Lng_Type = DisplayString
_Cps6000Ps1Lng_Object = MibScalar
cps6000Ps1Lng = _Cps6000Ps1Lng_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 18),
    _Cps6000Ps1Lng_Type()
)
cps6000Ps1Lng.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Lng.setStatus("current")
_Cps6000Ps1Ptt_Type = DisplayString
_Cps6000Ps1Ptt_Object = MibScalar
cps6000Ps1Ptt = _Cps6000Ps1Ptt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 19),
    _Cps6000Ps1Ptt_Type()
)
cps6000Ps1Ptt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Ptt.setStatus("current")
_Cps6000Ps1Amt_Type = DisplayString
_Cps6000Ps1Amt_Object = MibScalar
cps6000Ps1Amt = _Cps6000Ps1Amt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 20),
    _Cps6000Ps1Amt_Type()
)
cps6000Ps1Amt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Amt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Ps1Amt.setUnits("C")
_Cps6000Ps1Tun_Type = DisplayString
_Cps6000Ps1Tun_Object = MibScalar
cps6000Ps1Tun = _Cps6000Ps1Tun_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 21),
    _Cps6000Ps1Tun_Type()
)
cps6000Ps1Tun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Tun.setStatus("current")


class _Cps6000Ps1Usr_Type(Integer32):
    """Custom type cps6000Ps1Usr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ps1Usr_Type.__name__ = "Integer32"
_Cps6000Ps1Usr_Object = MibScalar
cps6000Ps1Usr = _Cps6000Ps1Usr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 22),
    _Cps6000Ps1Usr_Type()
)
cps6000Ps1Usr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Usr.setStatus("current")


class _Cps6000Ps1Poe_Type(Integer32):
    """Custom type cps6000Ps1Poe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ps1Poe_Type.__name__ = "Integer32"
_Cps6000Ps1Poe_Object = MibScalar
cps6000Ps1Poe = _Cps6000Ps1Poe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 23),
    _Cps6000Ps1Poe_Type()
)
cps6000Ps1Poe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Poe.setStatus("current")


class _Cps6000Ps1Fpc_Type(Integer32):
    """Custom type cps6000Ps1Fpc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ps1Fpc_Type.__name__ = "Integer32"
_Cps6000Ps1Fpc_Object = MibScalar
cps6000Ps1Fpc = _Cps6000Ps1Fpc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 24),
    _Cps6000Ps1Fpc_Type()
)
cps6000Ps1Fpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Fpc.setStatus("current")


class _Cps6000Ps1Rrf_Type(Integer32):
    """Custom type cps6000Ps1Rrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ps1Rrf_Type.__name__ = "Integer32"
_Cps6000Ps1Rrf_Object = MibScalar
cps6000Ps1Rrf = _Cps6000Ps1Rrf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 25),
    _Cps6000Ps1Rrf_Type()
)
cps6000Ps1Rrf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Rrf.setStatus("current")
_Cps6000Ps1Amth_Type = DisplayString
_Cps6000Ps1Amth_Object = MibScalar
cps6000Ps1Amth = _Cps6000Ps1Amth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 26),
    _Cps6000Ps1Amth_Type()
)
cps6000Ps1Amth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Amth.setStatus("current")
_Cps6000Ps1Amtl_Type = DisplayString
_Cps6000Ps1Amtl_Object = MibScalar
cps6000Ps1Amtl = _Cps6000Ps1Amtl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 27),
    _Cps6000Ps1Amtl_Type()
)
cps6000Ps1Amtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Amtl.setStatus("current")
_Cps6000Ps1Bbl_Type = DisplayString
_Cps6000Ps1Bbl_Object = MibScalar
cps6000Ps1Bbl = _Cps6000Ps1Bbl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 28),
    _Cps6000Ps1Bbl_Type()
)
cps6000Ps1Bbl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Bbl.setStatus("current")
_Cps6000Ps1Cch_Type = DisplayString
_Cps6000Ps1Cch_Object = MibScalar
cps6000Ps1Cch = _Cps6000Ps1Cch_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 29),
    _Cps6000Ps1Cch_Type()
)
cps6000Ps1Cch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Cch.setStatus("current")
_Cps6000Ps1Clc_Type = DisplayString
_Cps6000Ps1Clc_Object = MibScalar
cps6000Ps1Clc = _Cps6000Ps1Clc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 30),
    _Cps6000Ps1Clc_Type()
)
cps6000Ps1Clc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Clc.setStatus("current")
_Cps6000Ps1Epr_Type = DisplayString
_Cps6000Ps1Epr_Object = MibScalar
cps6000Ps1Epr = _Cps6000Ps1Epr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 31),
    _Cps6000Ps1Epr_Type()
)
cps6000Ps1Epr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Epr.setStatus("current")
_Cps6000Ps1Exl_Type = DisplayString
_Cps6000Ps1Exl_Object = MibScalar
cps6000Ps1Exl = _Cps6000Ps1Exl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 32),
    _Cps6000Ps1Exl_Type()
)
cps6000Ps1Exl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Exl.setStatus("current")
_Cps6000Ps1Hcl_Type = DisplayString
_Cps6000Ps1Hcl_Object = MibScalar
cps6000Ps1Hcl = _Cps6000Ps1Hcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 33),
    _Cps6000Ps1Hcl_Type()
)
cps6000Ps1Hcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Hcl.setStatus("current")
_Cps6000Ps1Pfd_Type = DisplayString
_Cps6000Ps1Pfd_Object = MibScalar
cps6000Ps1Pfd = _Cps6000Ps1Pfd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 34),
    _Cps6000Ps1Pfd_Type()
)
cps6000Ps1Pfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Pfd.setStatus("current")
_Cps6000Ps1Pht_Type = DisplayString
_Cps6000Ps1Pht_Object = MibScalar
cps6000Ps1Pht = _Cps6000Ps1Pht_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 35),
    _Cps6000Ps1Pht_Type()
)
cps6000Ps1Pht.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Pht.setStatus("current")
_Cps6000Ps1Stf_Type = DisplayString
_Cps6000Ps1Stf_Object = MibScalar
cps6000Ps1Stf = _Cps6000Ps1Stf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 36),
    _Cps6000Ps1Stf_Type()
)
cps6000Ps1Stf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Stf.setStatus("current")
_Cps6000Ps1Pgi_Type = DisplayString
_Cps6000Ps1Pgi_Object = MibScalar
cps6000Ps1Pgi = _Cps6000Ps1Pgi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 37),
    _Cps6000Ps1Pgi_Type()
)
cps6000Ps1Pgi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Pgi.setStatus("current")
_Cps6000Ps1Ax1_Type = DisplayString
_Cps6000Ps1Ax1_Object = MibScalar
cps6000Ps1Ax1 = _Cps6000Ps1Ax1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 38),
    _Cps6000Ps1Ax1_Type()
)
cps6000Ps1Ax1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax1.setStatus("current")
_Cps6000Ps1Ax2_Type = DisplayString
_Cps6000Ps1Ax2_Object = MibScalar
cps6000Ps1Ax2 = _Cps6000Ps1Ax2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 39),
    _Cps6000Ps1Ax2_Type()
)
cps6000Ps1Ax2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax2.setStatus("current")
_Cps6000Ps1Ax3_Type = DisplayString
_Cps6000Ps1Ax3_Object = MibScalar
cps6000Ps1Ax3 = _Cps6000Ps1Ax3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 40),
    _Cps6000Ps1Ax3_Type()
)
cps6000Ps1Ax3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax3.setStatus("current")
_Cps6000Ps1Ax4_Type = DisplayString
_Cps6000Ps1Ax4_Object = MibScalar
cps6000Ps1Ax4 = _Cps6000Ps1Ax4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 41),
    _Cps6000Ps1Ax4_Type()
)
cps6000Ps1Ax4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax4.setStatus("current")
_Cps6000Ps1Ax5_Type = DisplayString
_Cps6000Ps1Ax5_Object = MibScalar
cps6000Ps1Ax5 = _Cps6000Ps1Ax5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 42),
    _Cps6000Ps1Ax5_Type()
)
cps6000Ps1Ax5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax5.setStatus("current")
_Cps6000Ps1Ax6_Type = DisplayString
_Cps6000Ps1Ax6_Object = MibScalar
cps6000Ps1Ax6 = _Cps6000Ps1Ax6_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 43),
    _Cps6000Ps1Ax6_Type()
)
cps6000Ps1Ax6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ax6.setStatus("current")


class _Cps6000Ps1Rss_Type(Integer32):
    """Custom type cps6000Ps1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_Cps6000Ps1Rss_Type.__name__ = "Integer32"
_Cps6000Ps1Rss_Object = MibScalar
cps6000Ps1Rss = _Cps6000Ps1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 44),
    _Cps6000Ps1Rss_Type()
)
cps6000Ps1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Rss.setStatus("current")
_Cps6000Ps1Sys_Type = DisplayString
_Cps6000Ps1Sys_Object = MibScalar
cps6000Ps1Sys = _Cps6000Ps1Sys_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 45),
    _Cps6000Ps1Sys_Type()
)
cps6000Ps1Sys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Sys.setStatus("current")
_Cps6000Ps1Lngl_Type = DisplayString
_Cps6000Ps1Lngl_Object = MibScalar
cps6000Ps1Lngl = _Cps6000Ps1Lngl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 46),
    _Cps6000Ps1Lngl_Type()
)
cps6000Ps1Lngl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Lngl.setStatus("current")
_Cps6000Ps1Fst_Type = DisplayString
_Cps6000Ps1Fst_Object = MibScalar
cps6000Ps1Fst = _Cps6000Ps1Fst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 47),
    _Cps6000Ps1Fst_Type()
)
cps6000Ps1Fst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Fst.setStatus("current")
_Cps6000Ps1Fstl_Type = DisplayString
_Cps6000Ps1Fstl_Object = MibScalar
cps6000Ps1Fstl = _Cps6000Ps1Fstl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 48),
    _Cps6000Ps1Fstl_Type()
)
cps6000Ps1Fstl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Fstl.setStatus("current")


class _Cps6000Ps1Fpe_Type(Integer32):
    """Custom type cps6000Ps1Fpe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ps1Fpe_Type.__name__ = "Integer32"
_Cps6000Ps1Fpe_Object = MibScalar
cps6000Ps1Fpe = _Cps6000Ps1Fpe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 49),
    _Cps6000Ps1Fpe_Type()
)
cps6000Ps1Fpe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Fpe.setStatus("current")
_Cps6000Ps1Fpt_Type = Integer32
_Cps6000Ps1Fpt_Object = MibScalar
cps6000Ps1Fpt = _Cps6000Ps1Fpt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 50),
    _Cps6000Ps1Fpt_Type()
)
cps6000Ps1Fpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Fpt.setStatus("current")
_Cps6000Ps1Ast_Type = DisplayString
_Cps6000Ps1Ast_Object = MibScalar
cps6000Ps1Ast = _Cps6000Ps1Ast_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 51),
    _Cps6000Ps1Ast_Type()
)
cps6000Ps1Ast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ps1Ast.setStatus("current")
_Cps6000Ps1Dss_Type = DisplayString
_Cps6000Ps1Dss_Object = MibScalar
cps6000Ps1Dss = _Cps6000Ps1Dss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 52),
    _Cps6000Ps1Dss_Type()
)
cps6000Ps1Dss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Dss.setStatus("current")
_Cps6000Ps1Dse_Type = DisplayString
_Cps6000Ps1Dse_Object = MibScalar
cps6000Ps1Dse = _Cps6000Ps1Dse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 2, 53),
    _Cps6000Ps1Dse_Type()
)
cps6000Ps1Dse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ps1Dse.setStatus("current")
_Cps6000At1_ObjectIdentity = ObjectIdentity
cps6000At1 = _Cps6000At1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3)
)
_Cps6000At1Ide_Type = DisplayString
_Cps6000At1Ide_Object = MibScalar
cps6000At1Ide = _Cps6000At1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 1),
    _Cps6000At1Ide_Type()
)
cps6000At1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000At1Ide.setStatus("current")
_Cps6000At1Des_Type = DisplayString
_Cps6000At1Des_Object = MibScalar
cps6000At1Des = _Cps6000At1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 2),
    _Cps6000At1Des_Type()
)
cps6000At1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Des.setStatus("current")


class _Cps6000At1Stt_Type(Integer32):
    """Custom type cps6000At1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000At1Stt_Type.__name__ = "Integer32"
_Cps6000At1Stt_Object = MibScalar
cps6000At1Stt = _Cps6000At1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 3),
    _Cps6000At1Stt_Type()
)
cps6000At1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Stt.setStatus("current")
_Cps6000At1Stg_Type = DisplayString
_Cps6000At1Stg_Object = MibScalar
cps6000At1Stg = _Cps6000At1Stg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 4),
    _Cps6000At1Stg_Type()
)
cps6000At1Stg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000At1Stg.setStatus("current")


class _Cps6000At1Lte_Type(Integer32):
    """Custom type cps6000At1Lte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000At1Lte_Type.__name__ = "Integer32"
_Cps6000At1Lte_Object = MibScalar
cps6000At1Lte = _Cps6000At1Lte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 5),
    _Cps6000At1Lte_Type()
)
cps6000At1Lte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Lte.setStatus("current")


class _Cps6000At1Dur_Type(Integer32):
    """Custom type cps6000At1Dur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Cps6000At1Dur_Type.__name__ = "Integer32"
_Cps6000At1Dur_Object = MibScalar
cps6000At1Dur = _Cps6000At1Dur_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 6),
    _Cps6000At1Dur_Type()
)
cps6000At1Dur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Dur.setStatus("current")
if mibBuilder.loadTexts:
    cps6000At1Dur.setUnits("Seconds")


class _Cps6000At1Pmj_Type(Integer32):
    """Custom type cps6000At1Pmj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1Pmj_Type.__name__ = "Integer32"
_Cps6000At1Pmj_Object = MibScalar
cps6000At1Pmj = _Cps6000At1Pmj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 7),
    _Cps6000At1Pmj_Type()
)
cps6000At1Pmj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Pmj.setStatus("current")


class _Cps6000At1Pmn_Type(Integer32):
    """Custom type cps6000At1Pmn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1Pmn_Type.__name__ = "Integer32"
_Cps6000At1Pmn_Object = MibScalar
cps6000At1Pmn = _Cps6000At1Pmn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 8),
    _Cps6000At1Pmn_Type()
)
cps6000At1Pmn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Pmn.setStatus("current")


class _Cps6000At1R1_Type(Integer32):
    """Custom type cps6000At1R1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1R1_Type.__name__ = "Integer32"
_Cps6000At1R1_Object = MibScalar
cps6000At1R1 = _Cps6000At1R1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 9),
    _Cps6000At1R1_Type()
)
cps6000At1R1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1R1.setStatus("current")


class _Cps6000At1R2_Type(Integer32):
    """Custom type cps6000At1R2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1R2_Type.__name__ = "Integer32"
_Cps6000At1R2_Object = MibScalar
cps6000At1R2 = _Cps6000At1R2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 10),
    _Cps6000At1R2_Type()
)
cps6000At1R2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1R2.setStatus("current")


class _Cps6000At1R3_Type(Integer32):
    """Custom type cps6000At1R3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1R3_Type.__name__ = "Integer32"
_Cps6000At1R3_Object = MibScalar
cps6000At1R3 = _Cps6000At1R3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 11),
    _Cps6000At1R3_Type()
)
cps6000At1R3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1R3.setStatus("current")


class _Cps6000At1R4_Type(Integer32):
    """Custom type cps6000At1R4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000At1R4_Type.__name__ = "Integer32"
_Cps6000At1R4_Object = MibScalar
cps6000At1R4 = _Cps6000At1R4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 12),
    _Cps6000At1R4_Type()
)
cps6000At1R4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1R4.setStatus("current")
_Cps6000At1Ata_Type = DisplayString
_Cps6000At1Ata_Object = MibScalar
cps6000At1Ata = _Cps6000At1Ata_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 13),
    _Cps6000At1Ata_Type()
)
cps6000At1Ata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000At1Ata.setStatus("current")
_Cps6000At1Atb_Type = DisplayString
_Cps6000At1Atb_Object = MibScalar
cps6000At1Atb = _Cps6000At1Atb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 14),
    _Cps6000At1Atb_Type()
)
cps6000At1Atb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000At1Atb.setStatus("current")


class _Cps6000At1Ets_Type(Integer32):
    """Custom type cps6000At1Ets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_Cps6000At1Ets_Type.__name__ = "Integer32"
_Cps6000At1Ets_Object = MibScalar
cps6000At1Ets = _Cps6000At1Ets_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 15),
    _Cps6000At1Ets_Type()
)
cps6000At1Ets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Ets.setStatus("current")
_Cps6000At1Ems_Type = DisplayString
_Cps6000At1Ems_Object = MibScalar
cps6000At1Ems = _Cps6000At1Ems_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 16),
    _Cps6000At1Ems_Type()
)
cps6000At1Ems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000At1Ems.setStatus("current")
_Cps6000At1Irt_Type = DisplayString
_Cps6000At1Irt_Object = MibScalar
cps6000At1Irt = _Cps6000At1Irt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 3, 17),
    _Cps6000At1Irt_Type()
)
cps6000At1Irt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000At1Irt.setStatus("current")
_Cps6000Dct1_ObjectIdentity = ObjectIdentity
cps6000Dct1 = _Cps6000Dct1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 4)
)
_Cps6000Dct1Ide_Type = DisplayString
_Cps6000Dct1Ide_Object = MibScalar
cps6000Dct1Ide = _Cps6000Dct1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 4, 1),
    _Cps6000Dct1Ide_Type()
)
cps6000Dct1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Dct1Ide.setStatus("current")
_Cps6000Dct1Des_Type = DisplayString
_Cps6000Dct1Des_Object = MibScalar
cps6000Dct1Des = _Cps6000Dct1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 4, 2),
    _Cps6000Dct1Des_Type()
)
cps6000Dct1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dct1Des.setStatus("current")
_Cps6000Dct1Src_Type = DisplayString
_Cps6000Dct1Src_Object = MibScalar
cps6000Dct1Src = _Cps6000Dct1Src_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 4, 3),
    _Cps6000Dct1Src_Type()
)
cps6000Dct1Src.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Dct1Src.setStatus("current")
_Cps6000Gm1_ObjectIdentity = ObjectIdentity
cps6000Gm1 = _Cps6000Gm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5)
)
_Cps6000Gm1Ide_Type = DisplayString
_Cps6000Gm1Ide_Object = MibScalar
cps6000Gm1Ide = _Cps6000Gm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 1),
    _Cps6000Gm1Ide_Type()
)
cps6000Gm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Gm1Ide.setStatus("current")
_Cps6000Gm1Des_Type = DisplayString
_Cps6000Gm1Des_Object = MibScalar
cps6000Gm1Des = _Cps6000Gm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 2),
    _Cps6000Gm1Des_Type()
)
cps6000Gm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Des.setStatus("current")


class _Cps6000Gm1Lse_Type(Integer32):
    """Custom type cps6000Gm1Lse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Gm1Lse_Type.__name__ = "Integer32"
_Cps6000Gm1Lse_Object = MibScalar
cps6000Gm1Lse = _Cps6000Gm1Lse_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 3),
    _Cps6000Gm1Lse_Type()
)
cps6000Gm1Lse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Lse.setStatus("current")


class _Cps6000Gm1Fsd_Type(Integer32):
    """Custom type cps6000Gm1Fsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25000, 60000),
    )


_Cps6000Gm1Fsd_Type.__name__ = "Integer32"
_Cps6000Gm1Fsd_Object = MibScalar
cps6000Gm1Fsd = _Cps6000Gm1Fsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 4),
    _Cps6000Gm1Fsd_Type()
)
cps6000Gm1Fsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Fsd.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Fsd.setUnits("mV")


class _Cps6000Gm1Bsd_Type(Integer32):
    """Custom type cps6000Gm1Bsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(26000, 60000),
    )


_Cps6000Gm1Bsd_Type.__name__ = "Integer32"
_Cps6000Gm1Bsd_Object = MibScalar
cps6000Gm1Bsd = _Cps6000Gm1Bsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 5),
    _Cps6000Gm1Bsd_Type()
)
cps6000Gm1Bsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Bsd.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Bsd.setUnits("mV")


class _Cps6000Gm1Fsp_Type(Integer32):
    """Custom type cps6000Gm1Fsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 56000),
    )


_Cps6000Gm1Fsp_Type.__name__ = "Integer32"
_Cps6000Gm1Fsp_Object = MibScalar
cps6000Gm1Fsp = _Cps6000Gm1Fsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 6),
    _Cps6000Gm1Fsp_Type()
)
cps6000Gm1Fsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Fsp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Fsp.setUnits("mV")


class _Cps6000Gm1Bsp_Type(Integer32):
    """Custom type cps6000Gm1Bsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 60000),
    )


_Cps6000Gm1Bsp_Type.__name__ = "Integer32"
_Cps6000Gm1Bsp_Object = MibScalar
cps6000Gm1Bsp = _Cps6000Gm1Bsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 7),
    _Cps6000Gm1Bsp_Type()
)
cps6000Gm1Bsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Bsp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Bsp.setUnits("mV")


class _Cps6000Gm1Fcl_Type(Integer32):
    """Custom type cps6000Gm1Fcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 110),
    )


_Cps6000Gm1Fcl_Type.__name__ = "Integer32"
_Cps6000Gm1Fcl_Object = MibScalar
cps6000Gm1Fcl = _Cps6000Gm1Fcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 8),
    _Cps6000Gm1Fcl_Type()
)
cps6000Gm1Fcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Fcl.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Fcl.setUnits("%")


class _Cps6000Gm1Bcl_Type(Integer32):
    """Custom type cps6000Gm1Bcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 110),
    )


_Cps6000Gm1Bcl_Type.__name__ = "Integer32"
_Cps6000Gm1Bcl_Object = MibScalar
cps6000Gm1Bcl = _Cps6000Gm1Bcl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 9),
    _Cps6000Gm1Bcl_Type()
)
cps6000Gm1Bcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Bcl.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Gm1Bcl.setUnits("%")


class _Cps6000Gm1Rme_Type(Integer32):
    """Custom type cps6000Gm1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Gm1Rme_Type.__name__ = "Integer32"
_Cps6000Gm1Rme_Object = MibScalar
cps6000Gm1Rme = _Cps6000Gm1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 5, 10),
    _Cps6000Gm1Rme_Type()
)
cps6000Gm1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Gm1Rme.setStatus("current")
_Cps6000RecTable_Object = MibTable
cps6000RecTable = _Cps6000RecTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cps6000RecTable.setStatus("current")
_Cps6000RecEntry_Object = MibTableRow
cps6000RecEntry = _Cps6000RecEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1)
)
cps6000RecEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000RecEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000RecEntry.setStatus("current")


class _Cps6000RecEntryIndex_Type(Integer32):
    """Custom type cps6000RecEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000RecEntryIndex_Type.__name__ = "Integer32"
_Cps6000RecEntryIndex_Object = MibTableColumn
cps6000RecEntryIndex = _Cps6000RecEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 1),
    _Cps6000RecEntryIndex_Type()
)
cps6000RecEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryIndex.setStatus("current")
_Cps6000RecEntryIde_Type = DisplayString
_Cps6000RecEntryIde_Object = MibTableColumn
cps6000RecEntryIde = _Cps6000RecEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 2),
    _Cps6000RecEntryIde_Type()
)
cps6000RecEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryIde.setStatus("current")
_Cps6000RecEntryDes_Type = DisplayString
_Cps6000RecEntryDes_Object = MibTableColumn
cps6000RecEntryDes = _Cps6000RecEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 3),
    _Cps6000RecEntryDes_Type()
)
cps6000RecEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RecEntryDes.setStatus("current")
_Cps6000RecEntryTyp_Type = DisplayString
_Cps6000RecEntryTyp_Object = MibTableColumn
cps6000RecEntryTyp = _Cps6000RecEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 4),
    _Cps6000RecEntryTyp_Type()
)
cps6000RecEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RecEntryTyp.setStatus("current")
_Cps6000RecEntryAdc_Type = DisplayString
_Cps6000RecEntryAdc_Object = MibTableColumn
cps6000RecEntryAdc = _Cps6000RecEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 5),
    _Cps6000RecEntryAdc_Type()
)
cps6000RecEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryAdc.setUnits("Amps")
_Cps6000RecEntryVdc_Type = DisplayString
_Cps6000RecEntryVdc_Object = MibTableColumn
cps6000RecEntryVdc = _Cps6000RecEntryVdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 6),
    _Cps6000RecEntryVdc_Type()
)
cps6000RecEntryVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryVdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryVdc.setUnits("Volts")
_Cps6000RecEntryStt_Type = DisplayString
_Cps6000RecEntryStt_Object = MibTableColumn
cps6000RecEntryStt = _Cps6000RecEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 7),
    _Cps6000RecEntryStt_Type()
)
cps6000RecEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RecEntryStt.setStatus("current")
_Cps6000RecEntryCap_Type = DisplayString
_Cps6000RecEntryCap_Object = MibTableColumn
cps6000RecEntryCap = _Cps6000RecEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 8),
    _Cps6000RecEntryCap_Type()
)
cps6000RecEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryCap.setUnits("Amps")
_Cps6000RecEntryTmp_Type = DisplayString
_Cps6000RecEntryTmp_Object = MibTableColumn
cps6000RecEntryTmp = _Cps6000RecEntryTmp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 9),
    _Cps6000RecEntryTmp_Type()
)
cps6000RecEntryTmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryTmp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryTmp.setUnits("C")


class _Cps6000RecEntrySeq_Type(Integer32):
    """Custom type cps6000RecEntrySeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000RecEntrySeq_Type.__name__ = "Integer32"
_Cps6000RecEntrySeq_Object = MibTableColumn
cps6000RecEntrySeq = _Cps6000RecEntrySeq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 10),
    _Cps6000RecEntrySeq_Type()
)
cps6000RecEntrySeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RecEntrySeq.setStatus("current")
_Cps6000RecEntryRfa_Type = DisplayString
_Cps6000RecEntryRfa_Object = MibTableColumn
cps6000RecEntryRfa = _Cps6000RecEntryRfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 11),
    _Cps6000RecEntryRfa_Type()
)
cps6000RecEntryRfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryRfa.setStatus("current")
_Cps6000RecEntryAcf_Type = DisplayString
_Cps6000RecEntryAcf_Object = MibTableColumn
cps6000RecEntryAcf = _Cps6000RecEntryAcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 12),
    _Cps6000RecEntryAcf_Type()
)
cps6000RecEntryAcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryAcf.setStatus("current")
_Cps6000RecEntryMan_Type = DisplayString
_Cps6000RecEntryMan_Object = MibTableColumn
cps6000RecEntryMan = _Cps6000RecEntryMan_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 13),
    _Cps6000RecEntryMan_Type()
)
cps6000RecEntryMan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryMan.setStatus("current")
_Cps6000RecEntryDid_Type = DisplayString
_Cps6000RecEntryDid_Object = MibTableColumn
cps6000RecEntryDid = _Cps6000RecEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 14),
    _Cps6000RecEntryDid_Type()
)
cps6000RecEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryDid.setStatus("current")
_Cps6000RecEntryClm_Type = DisplayString
_Cps6000RecEntryClm_Object = MibTableColumn
cps6000RecEntryClm = _Cps6000RecEntryClm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 15),
    _Cps6000RecEntryClm_Type()
)
cps6000RecEntryClm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryClm.setStatus("current")
_Cps6000RecEntryRcf_Type = DisplayString
_Cps6000RecEntryRcf_Object = MibTableColumn
cps6000RecEntryRcf = _Cps6000RecEntryRcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 16),
    _Cps6000RecEntryRcf_Type()
)
cps6000RecEntryRcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryRcf.setStatus("current")
_Cps6000RecEntryRfn_Type = DisplayString
_Cps6000RecEntryRfn_Object = MibTableColumn
cps6000RecEntryRfn = _Cps6000RecEntryRfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 17),
    _Cps6000RecEntryRfn_Type()
)
cps6000RecEntryRfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryRfn.setStatus("current")
_Cps6000RecEntrySn_Type = DisplayString
_Cps6000RecEntrySn_Object = MibTableColumn
cps6000RecEntrySn = _Cps6000RecEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 18),
    _Cps6000RecEntrySn_Type()
)
cps6000RecEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntrySn.setStatus("current")
_Cps6000RecEntryVac_Type = Integer32
_Cps6000RecEntryVac_Object = MibTableColumn
cps6000RecEntryVac = _Cps6000RecEntryVac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 19),
    _Cps6000RecEntryVac_Type()
)
cps6000RecEntryVac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryVac.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryVac.setUnits("Volts")
_Cps6000RecEntryAac_Type = Integer32
_Cps6000RecEntryAac_Object = MibTableColumn
cps6000RecEntryAac = _Cps6000RecEntryAac_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 6, 1, 20),
    _Cps6000RecEntryAac_Type()
)
cps6000RecEntryAac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RecEntryAac.setStatus("current")
if mibBuilder.loadTexts:
    cps6000RecEntryAac.setUnits("mA")
_Cps6000Cp1_ObjectIdentity = ObjectIdentity
cps6000Cp1 = _Cps6000Cp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7)
)
_Cps6000Cp1Ide_Type = DisplayString
_Cps6000Cp1Ide_Object = MibScalar
cps6000Cp1Ide = _Cps6000Cp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 1),
    _Cps6000Cp1Ide_Type()
)
cps6000Cp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Ide.setStatus("current")
_Cps6000Cp1Des_Type = DisplayString
_Cps6000Cp1Des_Object = MibScalar
cps6000Cp1Des = _Cps6000Cp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 2),
    _Cps6000Cp1Des_Type()
)
cps6000Cp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Des.setStatus("current")
_Cps6000Cp1Vdc_Type = DisplayString
_Cps6000Cp1Vdc_Object = MibScalar
cps6000Cp1Vdc = _Cps6000Cp1Vdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 3),
    _Cps6000Cp1Vdc_Type()
)
cps6000Cp1Vdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Vdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Vdc.setUnits("Volts")
_Cps6000Cp1Adc_Type = DisplayString
_Cps6000Cp1Adc_Object = MibScalar
cps6000Cp1Adc = _Cps6000Cp1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 4),
    _Cps6000Cp1Adc_Type()
)
cps6000Cp1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Adc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Adc.setUnits("Amps")
_Cps6000Cp1Cap_Type = DisplayString
_Cps6000Cp1Cap_Object = MibScalar
cps6000Cp1Cap = _Cps6000Cp1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 5),
    _Cps6000Cp1Cap_Type()
)
cps6000Cp1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Cap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Cap.setUnits("Amps")


class _Cps6000Cp1Vsp_Type(Integer32):
    """Custom type cps6000Cp1Vsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48000, 52000),
    )


_Cps6000Cp1Vsp_Type.__name__ = "Integer32"
_Cps6000Cp1Vsp_Object = MibScalar
cps6000Cp1Vsp = _Cps6000Cp1Vsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 6),
    _Cps6000Cp1Vsp_Type()
)
cps6000Cp1Vsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Vsp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Vsp.setUnits("mV")


class _Cps6000Cp1Dth_Type(Integer32):
    """Custom type cps6000Cp1Dth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 25000),
    )


_Cps6000Cp1Dth_Type.__name__ = "Integer32"
_Cps6000Cp1Dth_Object = MibScalar
cps6000Cp1Dth = _Cps6000Cp1Dth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 7),
    _Cps6000Cp1Dth_Type()
)
cps6000Cp1Dth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Dth.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Dth.setUnits("mV")


class _Cps6000Cp1Rth_Type(Integer32):
    """Custom type cps6000Cp1Rth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 27000),
    )


_Cps6000Cp1Rth_Type.__name__ = "Integer32"
_Cps6000Cp1Rth_Object = MibScalar
cps6000Cp1Rth = _Cps6000Cp1Rth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 8),
    _Cps6000Cp1Rth_Type()
)
cps6000Cp1Rth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Rth.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Rth.setUnits("mV")


class _Cps6000Cp1Lvd_Type(Integer32):
    """Custom type cps6000Cp1Lvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Cp1Lvd_Type.__name__ = "Integer32"
_Cps6000Cp1Lvd_Object = MibScalar
cps6000Cp1Lvd = _Cps6000Cp1Lvd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 9),
    _Cps6000Cp1Lvd_Type()
)
cps6000Cp1Lvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Lvd.setStatus("current")
_Cps6000Cp1Cfa_Type = DisplayString
_Cps6000Cp1Cfa_Object = MibScalar
cps6000Cp1Cfa = _Cps6000Cp1Cfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 10),
    _Cps6000Cp1Cfa_Type()
)
cps6000Cp1Cfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Cfa.setStatus("current")
_Cps6000Cp1Dfa_Type = DisplayString
_Cps6000Cp1Dfa_Object = MibScalar
cps6000Cp1Dfa = _Cps6000Cp1Dfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 11),
    _Cps6000Cp1Dfa_Type()
)
cps6000Cp1Dfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Dfa.setStatus("current")
_Cps6000Cp1Did_Type = DisplayString
_Cps6000Cp1Did_Object = MibScalar
cps6000Cp1Did = _Cps6000Cp1Did_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 12),
    _Cps6000Cp1Did_Type()
)
cps6000Cp1Did.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Did.setStatus("current")
_Cps6000Cp1Mfa_Type = DisplayString
_Cps6000Cp1Mfa_Object = MibScalar
cps6000Cp1Mfa = _Cps6000Cp1Mfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 13),
    _Cps6000Cp1Mfa_Type()
)
cps6000Cp1Mfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Mfa.setStatus("current")
_Cps6000Cp1Cfn_Type = DisplayString
_Cps6000Cp1Cfn_Object = MibScalar
cps6000Cp1Cfn = _Cps6000Cp1Cfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 14),
    _Cps6000Cp1Cfn_Type()
)
cps6000Cp1Cfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Cfn.setStatus("current")
_Cps6000Cp1Cfj_Type = DisplayString
_Cps6000Cp1Cfj_Object = MibScalar
cps6000Cp1Cfj = _Cps6000Cp1Cfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 15),
    _Cps6000Cp1Cfj_Type()
)
cps6000Cp1Cfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Cfj.setStatus("current")
_Cps6000Cp1Icc_Type = DisplayString
_Cps6000Cp1Icc_Object = MibScalar
cps6000Cp1Icc = _Cps6000Cp1Icc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 16),
    _Cps6000Cp1Icc_Type()
)
cps6000Cp1Icc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Icc.setStatus("current")
_Cps6000Cp1Hva_Type = DisplayString
_Cps6000Cp1Hva_Object = MibScalar
cps6000Cp1Hva = _Cps6000Cp1Hva_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 17),
    _Cps6000Cp1Hva_Type()
)
cps6000Cp1Hva.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Hva.setStatus("current")
_Cps6000Cp1Hfv_Type = DisplayString
_Cps6000Cp1Hfv_Object = MibScalar
cps6000Cp1Hfv = _Cps6000Cp1Hfv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 18),
    _Cps6000Cp1Hfv_Type()
)
cps6000Cp1Hfv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Hfv.setStatus("current")
_Cps6000Cp1Vla_Type = DisplayString
_Cps6000Cp1Vla_Object = MibScalar
cps6000Cp1Vla = _Cps6000Cp1Vla_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 19),
    _Cps6000Cp1Vla_Type()
)
cps6000Cp1Vla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Vla.setStatus("current")
_Cps6000Cp1Rl_Type = DisplayString
_Cps6000Cp1Rl_Object = MibScalar
cps6000Cp1Rl = _Cps6000Cp1Rl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 20),
    _Cps6000Cp1Rl_Type()
)
cps6000Cp1Rl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Rl.setStatus("current")
_Cps6000Cp1Typ_Type = DisplayString
_Cps6000Cp1Typ_Object = MibScalar
cps6000Cp1Typ = _Cps6000Cp1Typ_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 21),
    _Cps6000Cp1Typ_Type()
)
cps6000Cp1Typ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Typ.setStatus("current")
_Cps6000Cp1Olcap_Type = Integer32
_Cps6000Cp1Olcap_Object = MibScalar
cps6000Cp1Olcap = _Cps6000Cp1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 22),
    _Cps6000Cp1Olcap_Type()
)
cps6000Cp1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cp1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Olcap.setUnits("Amps")


class _Cps6000Cp1Vsd_Type(Integer32):
    """Custom type cps6000Cp1Vsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48000, 52000),
    )


_Cps6000Cp1Vsd_Type.__name__ = "Integer32"
_Cps6000Cp1Vsd_Object = MibScalar
cps6000Cp1Vsd = _Cps6000Cp1Vsd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 23),
    _Cps6000Cp1Vsd_Type()
)
cps6000Cp1Vsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Vsd.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Vsd.setUnits("mV")


class _Cps6000Cp1Clm_Type(Integer32):
    """Custom type cps6000Cp1Clm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_Cps6000Cp1Clm_Type.__name__ = "Integer32"
_Cps6000Cp1Clm_Object = MibScalar
cps6000Cp1Clm = _Cps6000Cp1Clm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 24),
    _Cps6000Cp1Clm_Type()
)
cps6000Cp1Clm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Clm.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cp1Clm.setUnits("%")


class _Cps6000Cp1Rof_Type(Integer32):
    """Custom type cps6000Cp1Rof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Cp1Rof_Type.__name__ = "Integer32"
_Cps6000Cp1Rof_Object = MibScalar
cps6000Cp1Rof = _Cps6000Cp1Rof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 25),
    _Cps6000Cp1Rof_Type()
)
cps6000Cp1Rof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Rof.setStatus("current")


class _Cps6000Cp1Rme_Type(Integer32):
    """Custom type cps6000Cp1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Cp1Rme_Type.__name__ = "Integer32"
_Cps6000Cp1Rme_Object = MibScalar
cps6000Cp1Rme = _Cps6000Cp1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 26),
    _Cps6000Cp1Rme_Type()
)
cps6000Cp1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Rme.setStatus("current")


class _Cps6000Cp1Rss_Type(Integer32):
    """Custom type cps6000Cp1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_Cps6000Cp1Rss_Type.__name__ = "Integer32"
_Cps6000Cp1Rss_Object = MibScalar
cps6000Cp1Rss = _Cps6000Cp1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 7, 27),
    _Cps6000Cp1Rss_Type()
)
cps6000Cp1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cp1Rss.setStatus("current")
_Cps6000DccTable_Object = MibTable
cps6000DccTable = _Cps6000DccTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cps6000DccTable.setStatus("current")
_Cps6000DccEntry_Object = MibTableRow
cps6000DccEntry = _Cps6000DccEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1)
)
cps6000DccEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000DccEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000DccEntry.setStatus("current")


class _Cps6000DccEntryIndex_Type(Integer32):
    """Custom type cps6000DccEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000DccEntryIndex_Type.__name__ = "Integer32"
_Cps6000DccEntryIndex_Object = MibTableColumn
cps6000DccEntryIndex = _Cps6000DccEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 1),
    _Cps6000DccEntryIndex_Type()
)
cps6000DccEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryIndex.setStatus("current")
_Cps6000DccEntryIde_Type = DisplayString
_Cps6000DccEntryIde_Object = MibTableColumn
cps6000DccEntryIde = _Cps6000DccEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 2),
    _Cps6000DccEntryIde_Type()
)
cps6000DccEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryIde.setStatus("current")
_Cps6000DccEntryDes_Type = DisplayString
_Cps6000DccEntryDes_Object = MibTableColumn
cps6000DccEntryDes = _Cps6000DccEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 3),
    _Cps6000DccEntryDes_Type()
)
cps6000DccEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DccEntryDes.setStatus("current")
_Cps6000DccEntryTyp_Type = DisplayString
_Cps6000DccEntryTyp_Object = MibTableColumn
cps6000DccEntryTyp = _Cps6000DccEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 4),
    _Cps6000DccEntryTyp_Type()
)
cps6000DccEntryTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryTyp.setStatus("current")
_Cps6000DccEntryAdc_Type = DisplayString
_Cps6000DccEntryAdc_Object = MibTableColumn
cps6000DccEntryAdc = _Cps6000DccEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 5),
    _Cps6000DccEntryAdc_Type()
)
cps6000DccEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000DccEntryAdc.setUnits("Amps")
_Cps6000DccEntryCap_Type = DisplayString
_Cps6000DccEntryCap_Object = MibTableColumn
cps6000DccEntryCap = _Cps6000DccEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 6),
    _Cps6000DccEntryCap_Type()
)
cps6000DccEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000DccEntryCap.setUnits("Amps")
_Cps6000DccEntryStt_Type = DisplayString
_Cps6000DccEntryStt_Object = MibTableColumn
cps6000DccEntryStt = _Cps6000DccEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 7),
    _Cps6000DccEntryStt_Type()
)
cps6000DccEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DccEntryStt.setStatus("current")
_Cps6000DccEntryCfa_Type = DisplayString
_Cps6000DccEntryCfa_Object = MibTableColumn
cps6000DccEntryCfa = _Cps6000DccEntryCfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 8),
    _Cps6000DccEntryCfa_Type()
)
cps6000DccEntryCfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryCfa.setStatus("current")
_Cps6000DccEntryDfa_Type = DisplayString
_Cps6000DccEntryDfa_Object = MibTableColumn
cps6000DccEntryDfa = _Cps6000DccEntryDfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 9),
    _Cps6000DccEntryDfa_Type()
)
cps6000DccEntryDfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryDfa.setStatus("current")
_Cps6000DccEntryDid_Type = DisplayString
_Cps6000DccEntryDid_Object = MibTableColumn
cps6000DccEntryDid = _Cps6000DccEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 10),
    _Cps6000DccEntryDid_Type()
)
cps6000DccEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryDid.setStatus("current")
_Cps6000DccEntryCcf_Type = DisplayString
_Cps6000DccEntryCcf_Object = MibTableColumn
cps6000DccEntryCcf = _Cps6000DccEntryCcf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 11),
    _Cps6000DccEntryCcf_Type()
)
cps6000DccEntryCcf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryCcf.setStatus("current")
_Cps6000DccEntryCfn_Type = DisplayString
_Cps6000DccEntryCfn_Object = MibTableColumn
cps6000DccEntryCfn = _Cps6000DccEntryCfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 12),
    _Cps6000DccEntryCfn_Type()
)
cps6000DccEntryCfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntryCfn.setStatus("current")
_Cps6000DccEntrySn_Type = DisplayString
_Cps6000DccEntrySn_Object = MibTableColumn
cps6000DccEntrySn = _Cps6000DccEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 8, 1, 13),
    _Cps6000DccEntrySn_Type()
)
cps6000DccEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DccEntrySn.setStatus("current")
_Cps6000Bs1_ObjectIdentity = ObjectIdentity
cps6000Bs1 = _Cps6000Bs1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9)
)
_Cps6000Bs1Ide_Type = DisplayString
_Cps6000Bs1Ide_Object = MibScalar
cps6000Bs1Ide = _Cps6000Bs1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 1),
    _Cps6000Bs1Ide_Type()
)
cps6000Bs1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Bs1Ide.setStatus("current")
_Cps6000Bs1Des_Type = DisplayString
_Cps6000Bs1Des_Object = MibScalar
cps6000Bs1Des = _Cps6000Bs1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 2),
    _Cps6000Bs1Des_Type()
)
cps6000Bs1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Bs1Des.setStatus("current")
_Cps6000Bs1Stt_Type = DisplayString
_Cps6000Bs1Stt_Object = MibScalar
cps6000Bs1Stt = _Cps6000Bs1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 3),
    _Cps6000Bs1Stt_Type()
)
cps6000Bs1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Bs1Stt.setStatus("current")
_Cps6000Bs1Atm_Type = DisplayString
_Cps6000Bs1Atm_Object = MibScalar
cps6000Bs1Atm = _Cps6000Bs1Atm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 4),
    _Cps6000Bs1Atm_Type()
)
cps6000Bs1Atm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Bs1Atm.setStatus("current")


class _Cps6000Bs1Tmd_Type(Integer32):
    """Custom type cps6000Bs1Tmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 80),
    )


_Cps6000Bs1Tmd_Type.__name__ = "Integer32"
_Cps6000Bs1Tmd_Object = MibScalar
cps6000Bs1Tmd = _Cps6000Bs1Tmd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 5),
    _Cps6000Bs1Tmd_Type()
)
cps6000Bs1Tmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Bs1Tmd.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Bs1Tmd.setUnits("Hours")


class _Cps6000Bs1Amf_Type(Integer32):
    """Custom type cps6000Bs1Amf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Cps6000Bs1Amf_Type.__name__ = "Integer32"
_Cps6000Bs1Amf_Object = MibScalar
cps6000Bs1Amf = _Cps6000Bs1Amf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 6),
    _Cps6000Bs1Amf_Type()
)
cps6000Bs1Amf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Bs1Amf.setStatus("current")


class _Cps6000Bs1Cta_Type(Integer32):
    """Custom type cps6000Bs1Cta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cps6000Bs1Cta_Type.__name__ = "Integer32"
_Cps6000Bs1Cta_Object = MibScalar
cps6000Bs1Cta = _Cps6000Bs1Cta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 7),
    _Cps6000Bs1Cta_Type()
)
cps6000Bs1Cta.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Bs1Cta.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Bs1Cta.setUnits("Amps")
_Cps6000Bs1Bsa_Type = DisplayString
_Cps6000Bs1Bsa_Object = MibScalar
cps6000Bs1Bsa = _Cps6000Bs1Bsa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 9, 8),
    _Cps6000Bs1Bsa_Type()
)
cps6000Bs1Bsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Bs1Bsa.setStatus("current")
_Cps6000Sc1_ObjectIdentity = ObjectIdentity
cps6000Sc1 = _Cps6000Sc1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10)
)
_Cps6000Sc1Ide_Type = DisplayString
_Cps6000Sc1Ide_Object = MibScalar
cps6000Sc1Ide = _Cps6000Sc1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 1),
    _Cps6000Sc1Ide_Type()
)
cps6000Sc1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Sc1Ide.setStatus("current")
_Cps6000Sc1Des_Type = DisplayString
_Cps6000Sc1Des_Object = MibScalar
cps6000Sc1Des = _Cps6000Sc1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 2),
    _Cps6000Sc1Des_Type()
)
cps6000Sc1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Des.setStatus("current")


class _Cps6000Sc1Stt_Type(Integer32):
    """Custom type cps6000Sc1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Sc1Stt_Type.__name__ = "Integer32"
_Cps6000Sc1Stt_Object = MibScalar
cps6000Sc1Stt = _Cps6000Sc1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 3),
    _Cps6000Sc1Stt_Type()
)
cps6000Sc1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Stt.setStatus("current")


class _Cps6000Sc1Rve_Type(Integer32):
    """Custom type cps6000Sc1Rve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Sc1Rve_Type.__name__ = "Integer32"
_Cps6000Sc1Rve_Object = MibScalar
cps6000Sc1Rve = _Cps6000Sc1Rve_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 4),
    _Cps6000Sc1Rve_Type()
)
cps6000Sc1Rve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Rve.setStatus("current")
_Cps6000Sc1Ltt_Type = Integer32
_Cps6000Sc1Ltt_Object = MibScalar
cps6000Sc1Ltt = _Cps6000Sc1Ltt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 5),
    _Cps6000Sc1Ltt_Type()
)
cps6000Sc1Ltt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Ltt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Ltt.setUnits("C")
_Cps6000Sc1Ntt_Type = Integer32
_Cps6000Sc1Ntt_Object = MibScalar
cps6000Sc1Ntt = _Cps6000Sc1Ntt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 6),
    _Cps6000Sc1Ntt_Type()
)
cps6000Sc1Ntt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Ntt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Ntt.setUnits("C")
_Cps6000Sc1Utt_Type = Integer32
_Cps6000Sc1Utt_Object = MibScalar
cps6000Sc1Utt = _Cps6000Sc1Utt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 7),
    _Cps6000Sc1Utt_Type()
)
cps6000Sc1Utt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Utt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Utt.setUnits("C")
_Cps6000Sc1Spt_Type = Integer32
_Cps6000Sc1Spt_Object = MibScalar
cps6000Sc1Spt = _Cps6000Sc1Spt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 8),
    _Cps6000Sc1Spt_Type()
)
cps6000Sc1Spt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Spt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Spt.setUnits("C")
_Cps6000Sc1Lsp_Type = Integer32
_Cps6000Sc1Lsp_Object = MibScalar
cps6000Sc1Lsp = _Cps6000Sc1Lsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 9),
    _Cps6000Sc1Lsp_Type()
)
cps6000Sc1Lsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Lsp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Lsp.setUnits("mV/C/Cell")
_Cps6000Sc1Usp_Type = Integer32
_Cps6000Sc1Usp_Object = MibScalar
cps6000Sc1Usp = _Cps6000Sc1Usp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 10, 10),
    _Cps6000Sc1Usp_Type()
)
cps6000Sc1Usp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Sc1Usp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Sc1Usp.setUnits("mV/C/Cell")
_Cps6000BtdTable_Object = MibTable
cps6000BtdTable = _Cps6000BtdTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cps6000BtdTable.setStatus("current")
_Cps6000BtdEntry_Object = MibTableRow
cps6000BtdEntry = _Cps6000BtdEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1)
)
cps6000BtdEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000BtdEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000BtdEntry.setStatus("current")


class _Cps6000BtdEntryIndex_Type(Integer32):
    """Custom type cps6000BtdEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000BtdEntryIndex_Type.__name__ = "Integer32"
_Cps6000BtdEntryIndex_Object = MibTableColumn
cps6000BtdEntryIndex = _Cps6000BtdEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 1),
    _Cps6000BtdEntryIndex_Type()
)
cps6000BtdEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000BtdEntryIndex.setStatus("current")
_Cps6000BtdEntryIde_Type = DisplayString
_Cps6000BtdEntryIde_Object = MibTableColumn
cps6000BtdEntryIde = _Cps6000BtdEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 2),
    _Cps6000BtdEntryIde_Type()
)
cps6000BtdEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000BtdEntryIde.setStatus("current")
_Cps6000BtdEntryDes_Type = DisplayString
_Cps6000BtdEntryDes_Object = MibTableColumn
cps6000BtdEntryDes = _Cps6000BtdEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 3),
    _Cps6000BtdEntryDes_Type()
)
cps6000BtdEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000BtdEntryDes.setStatus("current")
_Cps6000BtdEntryBty_Type = DisplayString
_Cps6000BtdEntryBty_Object = MibTableColumn
cps6000BtdEntryBty = _Cps6000BtdEntryBty_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 4),
    _Cps6000BtdEntryBty_Type()
)
cps6000BtdEntryBty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000BtdEntryBty.setStatus("current")
_Cps6000BtdEntryBtc_Type = DisplayString
_Cps6000BtdEntryBtc_Object = MibTableColumn
cps6000BtdEntryBtc = _Cps6000BtdEntryBtc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 5),
    _Cps6000BtdEntryBtc_Type()
)
cps6000BtdEntryBtc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000BtdEntryBtc.setStatus("current")
_Cps6000BtdEntryCap_Type = DisplayString
_Cps6000BtdEntryCap_Object = MibTableColumn
cps6000BtdEntryCap = _Cps6000BtdEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 11, 1, 6),
    _Cps6000BtdEntryCap_Type()
)
cps6000BtdEntryCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000BtdEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000BtdEntryCap.setUnits("Amps")
_Cps6000Br1_ObjectIdentity = ObjectIdentity
cps6000Br1 = _Cps6000Br1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12)
)
_Cps6000Br1Ide_Type = DisplayString
_Cps6000Br1Ide_Object = MibScalar
cps6000Br1Ide = _Cps6000Br1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 1),
    _Cps6000Br1Ide_Type()
)
cps6000Br1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Ide.setStatus("current")
_Cps6000Br1Des_Type = DisplayString
_Cps6000Br1Des_Object = MibScalar
cps6000Br1Des = _Cps6000Br1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 2),
    _Cps6000Br1Des_Type()
)
cps6000Br1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Des.setStatus("current")
_Cps6000Br1Hbt_Type = DisplayString
_Cps6000Br1Hbt_Object = MibScalar
cps6000Br1Hbt = _Cps6000Br1Hbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 3),
    _Cps6000Br1Hbt_Type()
)
cps6000Br1Hbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Hbt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Hbt.setUnits("C")
_Cps6000Br1Adc_Type = DisplayString
_Cps6000Br1Adc_Object = MibScalar
cps6000Br1Adc = _Cps6000Br1Adc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 4),
    _Cps6000Br1Adc_Type()
)
cps6000Br1Adc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Adc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Adc.setUnits("Amps")
_Cps6000Br1Cap_Type = DisplayString
_Cps6000Br1Cap_Object = MibScalar
cps6000Br1Cap = _Cps6000Br1Cap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 5),
    _Cps6000Br1Cap_Type()
)
cps6000Br1Cap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Cap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Cap.setUnits("Amps")
_Cps6000Br1Olcap_Type = DisplayString
_Cps6000Br1Olcap_Object = MibScalar
cps6000Br1Olcap = _Cps6000Br1Olcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 6),
    _Cps6000Br1Olcap_Type()
)
cps6000Br1Olcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Olcap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Olcap.setUnits("Amps")


class _Cps6000Br1Bts_Type(Integer32):
    """Custom type cps6000Br1Bts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000Br1Bts_Type.__name__ = "Integer32"
_Cps6000Br1Bts_Object = MibScalar
cps6000Br1Bts = _Cps6000Br1Bts_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 7),
    _Cps6000Br1Bts_Type()
)
cps6000Br1Bts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Bts.setStatus("current")


class _Cps6000Br1Scd_Type(Integer32):
    """Custom type cps6000Br1Scd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Br1Scd_Type.__name__ = "Integer32"
_Cps6000Br1Scd_Object = MibScalar
cps6000Br1Scd = _Cps6000Br1Scd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 8),
    _Cps6000Br1Scd_Type()
)
cps6000Br1Scd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Scd.setStatus("current")


class _Cps6000Br1Scv_Type(Integer32):
    """Custom type cps6000Br1Scv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 3000),
    )


_Cps6000Br1Scv_Type.__name__ = "Integer32"
_Cps6000Br1Scv_Object = MibScalar
cps6000Br1Scv = _Cps6000Br1Scv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 9),
    _Cps6000Br1Scv_Type()
)
cps6000Br1Scv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Scv.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Scv.setUnits("mV")
_Cps6000Br1Ntm_Type = Integer32
_Cps6000Br1Ntm_Object = MibScalar
cps6000Br1Ntm = _Cps6000Br1Ntm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 10),
    _Cps6000Br1Ntm_Type()
)
cps6000Br1Ntm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Ntm.setStatus("current")
_Cps6000Br1Nvm_Type = Integer32
_Cps6000Br1Nvm_Object = MibScalar
cps6000Br1Nvm = _Cps6000Br1Nvm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 11),
    _Cps6000Br1Nvm_Type()
)
cps6000Br1Nvm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Nvm.setStatus("current")


class _Cps6000Br1Cle_Type(Integer32):
    """Custom type cps6000Br1Cle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Br1Cle_Type.__name__ = "Integer32"
_Cps6000Br1Cle_Object = MibScalar
cps6000Br1Cle = _Cps6000Br1Cle_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 12),
    _Cps6000Br1Cle_Type()
)
cps6000Br1Cle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Cle.setStatus("current")


class _Cps6000Br1Clt_Type(Integer32):
    """Custom type cps6000Br1Clt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_Cps6000Br1Clt_Type.__name__ = "Integer32"
_Cps6000Br1Clt_Object = MibScalar
cps6000Br1Clt = _Cps6000Br1Clt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 13),
    _Cps6000Br1Clt_Type()
)
cps6000Br1Clt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Clt.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Clt.setUnits("Amps")
_Cps6000Br1Mtt_Type = DisplayString
_Cps6000Br1Mtt_Object = MibScalar
cps6000Br1Mtt = _Cps6000Br1Mtt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 14),
    _Cps6000Br1Mtt_Type()
)
cps6000Br1Mtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Mtt.setStatus("current")
_Cps6000Br1Bte_Type = DisplayString
_Cps6000Br1Bte_Object = MibScalar
cps6000Br1Bte = _Cps6000Br1Bte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 15),
    _Cps6000Br1Bte_Type()
)
cps6000Br1Bte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Bte.setStatus("current")
_Cps6000Br1Atd_Type = DisplayString
_Cps6000Br1Atd_Object = MibScalar
cps6000Br1Atd = _Cps6000Br1Atd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 16),
    _Cps6000Br1Atd_Type()
)
cps6000Br1Atd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Atd.setStatus("current")


class _Cps6000Br1Ath_Type(Integer32):
    """Custom type cps6000Br1Ath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Cps6000Br1Ath_Type.__name__ = "Integer32"
_Cps6000Br1Ath_Object = MibScalar
cps6000Br1Ath = _Cps6000Br1Ath_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 17),
    _Cps6000Br1Ath_Type()
)
cps6000Br1Ath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Ath.setStatus("current")


class _Cps6000Br1Atw_Type(Integer32):
    """Custom type cps6000Br1Atw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Cps6000Br1Atw_Type.__name__ = "Integer32"
_Cps6000Br1Atw_Object = MibScalar
cps6000Br1Atw = _Cps6000Br1Atw_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 18),
    _Cps6000Br1Atw_Type()
)
cps6000Br1Atw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Atw.setStatus("current")


class _Cps6000Br1Tin_Type(Integer32):
    """Custom type cps6000Br1Tin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_Cps6000Br1Tin_Type.__name__ = "Integer32"
_Cps6000Br1Tin_Object = MibScalar
cps6000Br1Tin = _Cps6000Br1Tin_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 19),
    _Cps6000Br1Tin_Type()
)
cps6000Br1Tin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Tin.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Tin.setUnits("Months")
_Cps6000Br1Tmd_Type = DisplayString
_Cps6000Br1Tmd_Object = MibScalar
cps6000Br1Tmd = _Cps6000Br1Tmd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 20),
    _Cps6000Br1Tmd_Type()
)
cps6000Br1Tmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Tmd.setStatus("current")


class _Cps6000Br1Tev_Type(Integer32):
    """Custom type cps6000Br1Tev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(36000, 48000),
    )


_Cps6000Br1Tev_Type.__name__ = "Integer32"
_Cps6000Br1Tev_Object = MibScalar
cps6000Br1Tev = _Cps6000Br1Tev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 21),
    _Cps6000Br1Tev_Type()
)
cps6000Br1Tev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Tev.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Tev.setUnits("mV")


class _Cps6000Br1Btv_Type(Integer32):
    """Custom type cps6000Br1Btv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(42000, 52000),
    )


_Cps6000Br1Btv_Type.__name__ = "Integer32"
_Cps6000Br1Btv_Object = MibScalar
cps6000Br1Btv = _Cps6000Br1Btv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 22),
    _Cps6000Br1Btv_Type()
)
cps6000Br1Btv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Btv.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Btv.setUnits("mV")


class _Cps6000Br1Tth_Type(Integer32):
    """Custom type cps6000Br1Tth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 194),
    )


_Cps6000Br1Tth_Type.__name__ = "Integer32"
_Cps6000Br1Tth_Object = MibScalar
cps6000Br1Tth = _Cps6000Br1Tth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 23),
    _Cps6000Br1Tth_Type()
)
cps6000Br1Tth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Tth.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Tth.setUnits("C")


class _Cps6000Br1Cev_Type(Integer32):
    """Custom type cps6000Br1Cev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1750, 1950),
    )


_Cps6000Br1Cev_Type.__name__ = "Integer32"
_Cps6000Br1Cev_Object = MibScalar
cps6000Br1Cev = _Cps6000Br1Cev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 24),
    _Cps6000Br1Cev_Type()
)
cps6000Br1Cev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Br1Cev.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Br1Cev.setUnits("mV")
_Cps6000Br1Btr_Type = DisplayString
_Cps6000Br1Btr_Object = MibScalar
cps6000Br1Btr = _Cps6000Br1Btr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 25),
    _Cps6000Br1Btr_Type()
)
cps6000Br1Btr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Btr.setStatus("current")
_Cps6000Br1Bta_Type = DisplayString
_Cps6000Br1Bta_Object = MibScalar
cps6000Br1Bta = _Cps6000Br1Bta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 26),
    _Cps6000Br1Bta_Type()
)
cps6000Br1Bta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Bta.setStatus("current")
_Cps6000Br1Bfa_Type = DisplayString
_Cps6000Br1Bfa_Object = MibScalar
cps6000Br1Bfa = _Cps6000Br1Bfa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 27),
    _Cps6000Br1Bfa_Type()
)
cps6000Br1Bfa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Bfa.setStatus("current")
_Cps6000Br1Btha_Type = DisplayString
_Cps6000Br1Btha_Object = MibScalar
cps6000Br1Btha = _Cps6000Br1Btha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 28),
    _Cps6000Br1Btha_Type()
)
cps6000Br1Btha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Btha.setStatus("current")
_Cps6000Br1Isda_Type = DisplayString
_Cps6000Br1Isda_Object = MibScalar
cps6000Br1Isda = _Cps6000Br1Isda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 29),
    _Cps6000Br1Isda_Type()
)
cps6000Br1Isda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Isda.setStatus("current")
_Cps6000Br1Mdp_Type = DisplayString
_Cps6000Br1Mdp_Object = MibScalar
cps6000Br1Mdp = _Cps6000Br1Mdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 30),
    _Cps6000Br1Mdp_Type()
)
cps6000Br1Mdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Mdp.setStatus("current")
_Cps6000Br1Mzd_Type = DisplayString
_Cps6000Br1Mzd_Object = MibScalar
cps6000Br1Mzd = _Cps6000Br1Mzd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 31),
    _Cps6000Br1Mzd_Type()
)
cps6000Br1Mzd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Mzd.setStatus("current")
_Cps6000Br1Scda_Type = DisplayString
_Cps6000Br1Scda_Object = MibScalar
cps6000Br1Scda = _Cps6000Br1Scda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 12, 32),
    _Cps6000Br1Scda_Type()
)
cps6000Br1Scda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Br1Scda.setStatus("current")
_Cps6000CntTable_Object = MibTable
cps6000CntTable = _Cps6000CntTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cps6000CntTable.setStatus("current")
_Cps6000CntEntry_Object = MibTableRow
cps6000CntEntry = _Cps6000CntEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1)
)
cps6000CntEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000CntEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000CntEntry.setStatus("current")


class _Cps6000CntEntryIndex_Type(Integer32):
    """Custom type cps6000CntEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000CntEntryIndex_Type.__name__ = "Integer32"
_Cps6000CntEntryIndex_Object = MibTableColumn
cps6000CntEntryIndex = _Cps6000CntEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 1),
    _Cps6000CntEntryIndex_Type()
)
cps6000CntEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryIndex.setStatus("current")
_Cps6000CntEntryIde_Type = DisplayString
_Cps6000CntEntryIde_Object = MibTableColumn
cps6000CntEntryIde = _Cps6000CntEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 2),
    _Cps6000CntEntryIde_Type()
)
cps6000CntEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryIde.setStatus("current")
_Cps6000CntEntryDes_Type = DisplayString
_Cps6000CntEntryDes_Object = MibTableColumn
cps6000CntEntryDes = _Cps6000CntEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 3),
    _Cps6000CntEntryDes_Type()
)
cps6000CntEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryDes.setStatus("current")
_Cps6000CntEntryStt_Type = DisplayString
_Cps6000CntEntryStt_Object = MibTableColumn
cps6000CntEntryStt = _Cps6000CntEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 4),
    _Cps6000CntEntryStt_Type()
)
cps6000CntEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryStt.setStatus("current")


class _Cps6000CntEntryEna_Type(Integer32):
    """Custom type cps6000CntEntryEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000CntEntryEna_Type.__name__ = "Integer32"
_Cps6000CntEntryEna_Object = MibTableColumn
cps6000CntEntryEna = _Cps6000CntEntryEna_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 5),
    _Cps6000CntEntryEna_Type()
)
cps6000CntEntryEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryEna.setStatus("current")


class _Cps6000CntEntryDth_Type(Integer32):
    """Custom type cps6000CntEntryDth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20000, 50000),
    )


_Cps6000CntEntryDth_Type.__name__ = "Integer32"
_Cps6000CntEntryDth_Object = MibTableColumn
cps6000CntEntryDth = _Cps6000CntEntryDth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 6),
    _Cps6000CntEntryDth_Type()
)
cps6000CntEntryDth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryDth.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryDth.setUnits("mV")


class _Cps6000CntEntryDdy_Type(Integer32):
    """Custom type cps6000CntEntryDdy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Cps6000CntEntryDdy_Type.__name__ = "Integer32"
_Cps6000CntEntryDdy_Object = MibTableColumn
cps6000CntEntryDdy = _Cps6000CntEntryDdy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 7),
    _Cps6000CntEntryDdy_Type()
)
cps6000CntEntryDdy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryDdy.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryDdy.setUnits("Minutes")


class _Cps6000CntEntryDam_Type(Integer32):
    """Custom type cps6000CntEntryDam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("voltage", 1),
          ("voltageAndTime", 2))
    )


_Cps6000CntEntryDam_Type.__name__ = "Integer32"
_Cps6000CntEntryDam_Object = MibTableColumn
cps6000CntEntryDam = _Cps6000CntEntryDam_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 8),
    _Cps6000CntEntryDam_Type()
)
cps6000CntEntryDam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryDam.setStatus("current")
_Cps6000CntEntryDtm_Type = Integer32
_Cps6000CntEntryDtm_Object = MibTableColumn
cps6000CntEntryDtm = _Cps6000CntEntryDtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 9),
    _Cps6000CntEntryDtm_Type()
)
cps6000CntEntryDtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryDtm.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryDtm.setUnits("Minutes")


class _Cps6000CntEntryRth_Type(Integer32):
    """Custom type cps6000CntEntryRth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22000, 55000),
    )


_Cps6000CntEntryRth_Type.__name__ = "Integer32"
_Cps6000CntEntryRth_Object = MibTableColumn
cps6000CntEntryRth = _Cps6000CntEntryRth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 10),
    _Cps6000CntEntryRth_Type()
)
cps6000CntEntryRth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryRth.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryRth.setUnits("mV")


class _Cps6000CntEntryRdy_Type(Integer32):
    """Custom type cps6000CntEntryRdy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_Cps6000CntEntryRdy_Type.__name__ = "Integer32"
_Cps6000CntEntryRdy_Object = MibTableColumn
cps6000CntEntryRdy = _Cps6000CntEntryRdy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 11),
    _Cps6000CntEntryRdy_Type()
)
cps6000CntEntryRdy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryRdy.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryRdy.setUnits("Seconds")


class _Cps6000CntEntryRam_Type(Integer32):
    """Custom type cps6000CntEntryRam based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("voltage", 1),
          ("voltageAndTime", 2))
    )


_Cps6000CntEntryRam_Type.__name__ = "Integer32"
_Cps6000CntEntryRam_Object = MibTableColumn
cps6000CntEntryRam = _Cps6000CntEntryRam_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 12),
    _Cps6000CntEntryRam_Type()
)
cps6000CntEntryRam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CntEntryRam.setStatus("current")
_Cps6000CntEntryRtm_Type = Integer32
_Cps6000CntEntryRtm_Object = MibTableColumn
cps6000CntEntryRtm = _Cps6000CntEntryRtm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 13),
    _Cps6000CntEntryRtm_Type()
)
cps6000CntEntryRtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryRtm.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CntEntryRtm.setUnits("Seconds")
_Cps6000CntEntryCno_Type = DisplayString
_Cps6000CntEntryCno_Object = MibTableColumn
cps6000CntEntryCno = _Cps6000CntEntryCno_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 14),
    _Cps6000CntEntryCno_Type()
)
cps6000CntEntryCno.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryCno.setStatus("current")
_Cps6000CntEntryCnf_Type = DisplayString
_Cps6000CntEntryCnf_Object = MibTableColumn
cps6000CntEntryCnf = _Cps6000CntEntryCnf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 13, 1, 15),
    _Cps6000CntEntryCnf_Type()
)
cps6000CntEntryCnf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CntEntryCnf.setStatus("current")
_Cps6000DcnTable_Object = MibTable
cps6000DcnTable = _Cps6000DcnTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14)
)
if mibBuilder.loadTexts:
    cps6000DcnTable.setStatus("current")
_Cps6000DcnEntry_Object = MibTableRow
cps6000DcnEntry = _Cps6000DcnEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1)
)
cps6000DcnEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000DcnEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000DcnEntry.setStatus("current")


class _Cps6000DcnEntryIndex_Type(Integer32):
    """Custom type cps6000DcnEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000DcnEntryIndex_Type.__name__ = "Integer32"
_Cps6000DcnEntryIndex_Object = MibTableColumn
cps6000DcnEntryIndex = _Cps6000DcnEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 1),
    _Cps6000DcnEntryIndex_Type()
)
cps6000DcnEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcnEntryIndex.setStatus("current")
_Cps6000DcnEntryIde_Type = DisplayString
_Cps6000DcnEntryIde_Object = MibTableColumn
cps6000DcnEntryIde = _Cps6000DcnEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 2),
    _Cps6000DcnEntryIde_Type()
)
cps6000DcnEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcnEntryIde.setStatus("current")
_Cps6000DcnEntryDes_Type = DisplayString
_Cps6000DcnEntryDes_Object = MibTableColumn
cps6000DcnEntryDes = _Cps6000DcnEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 3),
    _Cps6000DcnEntryDes_Type()
)
cps6000DcnEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DcnEntryDes.setStatus("current")
_Cps6000DcnEntryStt_Type = DisplayString
_Cps6000DcnEntryStt_Object = MibTableColumn
cps6000DcnEntryStt = _Cps6000DcnEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 4),
    _Cps6000DcnEntryStt_Type()
)
cps6000DcnEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcnEntryStt.setStatus("current")
_Cps6000DcnEntryTyp_Type = DisplayString
_Cps6000DcnEntryTyp_Object = MibTableColumn
cps6000DcnEntryTyp = _Cps6000DcnEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 5),
    _Cps6000DcnEntryTyp_Type()
)
cps6000DcnEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DcnEntryTyp.setStatus("current")
_Cps6000DcnEntrySn_Type = DisplayString
_Cps6000DcnEntrySn_Object = MibTableColumn
cps6000DcnEntrySn = _Cps6000DcnEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 6),
    _Cps6000DcnEntrySn_Type()
)
cps6000DcnEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcnEntrySn.setStatus("current")
_Cps6000DcnEntryBrc_Type = DisplayString
_Cps6000DcnEntryBrc_Object = MibTableColumn
cps6000DcnEntryBrc = _Cps6000DcnEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 14, 1, 7),
    _Cps6000DcnEntryBrc_Type()
)
cps6000DcnEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcnEntryBrc.setStatus("current")
_Cps6000DcmTable_Object = MibTable
cps6000DcmTable = _Cps6000DcmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cps6000DcmTable.setStatus("current")
_Cps6000DcmEntry_Object = MibTableRow
cps6000DcmEntry = _Cps6000DcmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1)
)
cps6000DcmEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000DcmEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000DcmEntry.setStatus("current")


class _Cps6000DcmEntryIndex_Type(Integer32):
    """Custom type cps6000DcmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000DcmEntryIndex_Type.__name__ = "Integer32"
_Cps6000DcmEntryIndex_Object = MibTableColumn
cps6000DcmEntryIndex = _Cps6000DcmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 1),
    _Cps6000DcmEntryIndex_Type()
)
cps6000DcmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntryIndex.setStatus("current")
_Cps6000DcmEntryIde_Type = DisplayString
_Cps6000DcmEntryIde_Object = MibTableColumn
cps6000DcmEntryIde = _Cps6000DcmEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 2),
    _Cps6000DcmEntryIde_Type()
)
cps6000DcmEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntryIde.setStatus("current")
_Cps6000DcmEntryDes_Type = DisplayString
_Cps6000DcmEntryDes_Object = MibTableColumn
cps6000DcmEntryDes = _Cps6000DcmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 3),
    _Cps6000DcmEntryDes_Type()
)
cps6000DcmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DcmEntryDes.setStatus("current")
_Cps6000DcmEntryStt_Type = DisplayString
_Cps6000DcmEntryStt_Object = MibTableColumn
cps6000DcmEntryStt = _Cps6000DcmEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 4),
    _Cps6000DcmEntryStt_Type()
)
cps6000DcmEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntryStt.setStatus("current")
_Cps6000DcmEntryTyp_Type = DisplayString
_Cps6000DcmEntryTyp_Object = MibTableColumn
cps6000DcmEntryTyp = _Cps6000DcmEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 5),
    _Cps6000DcmEntryTyp_Type()
)
cps6000DcmEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DcmEntryTyp.setStatus("current")
_Cps6000DcmEntryVal_Type = Integer32
_Cps6000DcmEntryVal_Object = MibTableColumn
cps6000DcmEntryVal = _Cps6000DcmEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 6),
    _Cps6000DcmEntryVal_Type()
)
cps6000DcmEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntryVal.setStatus("current")
if mibBuilder.loadTexts:
    cps6000DcmEntryVal.setUnits("Amps x 1000")
_Cps6000DcmEntrySha_Type = Integer32
_Cps6000DcmEntrySha_Object = MibTableColumn
cps6000DcmEntrySha = _Cps6000DcmEntrySha_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 7),
    _Cps6000DcmEntrySha_Type()
)
cps6000DcmEntrySha.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DcmEntrySha.setStatus("current")
if mibBuilder.loadTexts:
    cps6000DcmEntrySha.setUnits("Amps")
_Cps6000DcmEntrySn_Type = DisplayString
_Cps6000DcmEntrySn_Object = MibTableColumn
cps6000DcmEntrySn = _Cps6000DcmEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 8),
    _Cps6000DcmEntrySn_Type()
)
cps6000DcmEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntrySn.setStatus("current")
_Cps6000DcmEntryBrc_Type = DisplayString
_Cps6000DcmEntryBrc_Object = MibTableColumn
cps6000DcmEntryBrc = _Cps6000DcmEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 15, 1, 9),
    _Cps6000DcmEntryBrc_Type()
)
cps6000DcmEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DcmEntryBrc.setStatus("current")
_Cps6000UdeTable_Object = MibTable
cps6000UdeTable = _Cps6000UdeTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cps6000UdeTable.setStatus("current")
_Cps6000UdeEntry_Object = MibTableRow
cps6000UdeEntry = _Cps6000UdeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1)
)
cps6000UdeEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000UdeEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000UdeEntry.setStatus("current")


class _Cps6000UdeEntryIndex_Type(Integer32):
    """Custom type cps6000UdeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000UdeEntryIndex_Type.__name__ = "Integer32"
_Cps6000UdeEntryIndex_Object = MibTableColumn
cps6000UdeEntryIndex = _Cps6000UdeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 1),
    _Cps6000UdeEntryIndex_Type()
)
cps6000UdeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000UdeEntryIndex.setStatus("current")
_Cps6000UdeEntryIde_Type = DisplayString
_Cps6000UdeEntryIde_Object = MibTableColumn
cps6000UdeEntryIde = _Cps6000UdeEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 2),
    _Cps6000UdeEntryIde_Type()
)
cps6000UdeEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000UdeEntryIde.setStatus("current")
_Cps6000UdeEntryDes_Type = DisplayString
_Cps6000UdeEntryDes_Object = MibTableColumn
cps6000UdeEntryDes = _Cps6000UdeEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 3),
    _Cps6000UdeEntryDes_Type()
)
cps6000UdeEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryDes.setStatus("current")
_Cps6000UdeEntryAst_Type = DisplayString
_Cps6000UdeEntryAst_Object = MibTableColumn
cps6000UdeEntryAst = _Cps6000UdeEntryAst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 4),
    _Cps6000UdeEntryAst_Type()
)
cps6000UdeEntryAst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000UdeEntryAst.setStatus("current")
_Cps6000UdeEntrySev_Type = DisplayString
_Cps6000UdeEntrySev_Object = MibTableColumn
cps6000UdeEntrySev = _Cps6000UdeEntrySev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 5),
    _Cps6000UdeEntrySev_Type()
)
cps6000UdeEntrySev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntrySev.setStatus("current")
_Cps6000UdeEntryPrg_Type = DisplayString
_Cps6000UdeEntryPrg_Object = MibTableColumn
cps6000UdeEntryPrg = _Cps6000UdeEntryPrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 6),
    _Cps6000UdeEntryPrg_Type()
)
cps6000UdeEntryPrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryPrg.setStatus("current")
_Cps6000UdeEntryDur_Type = DisplayString
_Cps6000UdeEntryDur_Object = MibTableColumn
cps6000UdeEntryDur = _Cps6000UdeEntryDur_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 7),
    _Cps6000UdeEntryDur_Type()
)
cps6000UdeEntryDur.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryDur.setStatus("current")
if mibBuilder.loadTexts:
    cps6000UdeEntryDur.setUnits("Seconds")


class _Cps6000UdeEntryLat_Type(Integer32):
    """Custom type cps6000UdeEntryLat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000UdeEntryLat_Type.__name__ = "Integer32"
_Cps6000UdeEntryLat_Object = MibTableColumn
cps6000UdeEntryLat = _Cps6000UdeEntryLat_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 8),
    _Cps6000UdeEntryLat_Type()
)
cps6000UdeEntryLat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryLat.setStatus("current")
_Cps6000UdeEntryAcc_Type = DisplayString
_Cps6000UdeEntryAcc_Object = MibTableColumn
cps6000UdeEntryAcc = _Cps6000UdeEntryAcc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 9),
    _Cps6000UdeEntryAcc_Type()
)
cps6000UdeEntryAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryAcc.setStatus("current")


class _Cps6000UdeEntryDly_Type(Integer32):
    """Custom type cps6000UdeEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 540),
    )


_Cps6000UdeEntryDly_Type.__name__ = "Integer32"
_Cps6000UdeEntryDly_Object = MibTableColumn
cps6000UdeEntryDly = _Cps6000UdeEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 10),
    _Cps6000UdeEntryDly_Type()
)
cps6000UdeEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryDly.setStatus("current")
if mibBuilder.loadTexts:
    cps6000UdeEntryDly.setUnits("Seconds")


class _Cps6000UdeEntryNoo_Type(Integer32):
    """Custom type cps6000UdeEntryNoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000UdeEntryNoo_Type.__name__ = "Integer32"
_Cps6000UdeEntryNoo_Object = MibTableColumn
cps6000UdeEntryNoo = _Cps6000UdeEntryNoo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 11),
    _Cps6000UdeEntryNoo_Type()
)
cps6000UdeEntryNoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryNoo.setStatus("current")


class _Cps6000UdeEntryNor_Type(Integer32):
    """Custom type cps6000UdeEntryNor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000UdeEntryNor_Type.__name__ = "Integer32"
_Cps6000UdeEntryNor_Object = MibTableColumn
cps6000UdeEntryNor = _Cps6000UdeEntryNor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 12),
    _Cps6000UdeEntryNor_Type()
)
cps6000UdeEntryNor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryNor.setStatus("current")


class _Cps6000UdeEntryNag_Type(Integer32):
    """Custom type cps6000UdeEntryNag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000UdeEntryNag_Type.__name__ = "Integer32"
_Cps6000UdeEntryNag_Object = MibTableColumn
cps6000UdeEntryNag = _Cps6000UdeEntryNag_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 13),
    _Cps6000UdeEntryNag_Type()
)
cps6000UdeEntryNag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryNag.setStatus("current")
_Cps6000UdeEntryDst_Type = DisplayString
_Cps6000UdeEntryDst_Object = MibTableColumn
cps6000UdeEntryDst = _Cps6000UdeEntryDst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 14),
    _Cps6000UdeEntryDst_Type()
)
cps6000UdeEntryDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryDst.setStatus("current")
_Cps6000UdeEntryFds_Type = DisplayString
_Cps6000UdeEntryFds_Object = MibTableColumn
cps6000UdeEntryFds = _Cps6000UdeEntryFds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 16, 1, 15),
    _Cps6000UdeEntryFds_Type()
)
cps6000UdeEntryFds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000UdeEntryFds.setStatus("current")
_Cps6000Cm1_ObjectIdentity = ObjectIdentity
cps6000Cm1 = _Cps6000Cm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17)
)
_Cps6000Cm1Ide_Type = DisplayString
_Cps6000Cm1Ide_Object = MibScalar
cps6000Cm1Ide = _Cps6000Cm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 1),
    _Cps6000Cm1Ide_Type()
)
cps6000Cm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cm1Ide.setStatus("current")
_Cps6000Cm1Des_Type = DisplayString
_Cps6000Cm1Des_Object = MibScalar
cps6000Cm1Des = _Cps6000Cm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 2),
    _Cps6000Cm1Des_Type()
)
cps6000Cm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cm1Des.setStatus("current")


class _Cps6000Cm1Ngi_Type(Integer32):
    """Custom type cps6000Cm1Ngi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_Cps6000Cm1Ngi_Type.__name__ = "Integer32"
_Cps6000Cm1Ngi_Object = MibScalar
cps6000Cm1Ngi = _Cps6000Cm1Ngi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 3),
    _Cps6000Cm1Ngi_Type()
)
cps6000Cm1Ngi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cm1Ngi.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Cm1Ngi.setUnits("Minutes")
_Cps6000Cm1Cof_Type = DisplayString
_Cps6000Cm1Cof_Object = MibScalar
cps6000Cm1Cof = _Cps6000Cm1Cof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 4),
    _Cps6000Cm1Cof_Type()
)
cps6000Cm1Cof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cm1Cof.setStatus("current")
_Cps6000Cm1Cor_Type = DisplayString
_Cps6000Cm1Cor_Object = MibScalar
cps6000Cm1Cor = _Cps6000Cm1Cor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 5),
    _Cps6000Cm1Cor_Type()
)
cps6000Cm1Cor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cm1Cor.setStatus("current")
_Cps6000Cm1Nnc_Type = DisplayString
_Cps6000Cm1Nnc_Object = MibScalar
cps6000Cm1Nnc = _Cps6000Cm1Nnc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 17, 6),
    _Cps6000Cm1Nnc_Type()
)
cps6000Cm1Nnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cm1Nnc.setStatus("current")
_Cps6000CopTable_Object = MibTable
cps6000CopTable = _Cps6000CopTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cps6000CopTable.setStatus("current")
_Cps6000CopEntry_Object = MibTableRow
cps6000CopEntry = _Cps6000CopEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1)
)
cps6000CopEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000CopEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000CopEntry.setStatus("current")


class _Cps6000CopEntryIndex_Type(Integer32):
    """Custom type cps6000CopEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000CopEntryIndex_Type.__name__ = "Integer32"
_Cps6000CopEntryIndex_Object = MibTableColumn
cps6000CopEntryIndex = _Cps6000CopEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 1),
    _Cps6000CopEntryIndex_Type()
)
cps6000CopEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CopEntryIndex.setStatus("current")
_Cps6000CopEntryIde_Type = DisplayString
_Cps6000CopEntryIde_Object = MibTableColumn
cps6000CopEntryIde = _Cps6000CopEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 2),
    _Cps6000CopEntryIde_Type()
)
cps6000CopEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CopEntryIde.setStatus("current")
_Cps6000CopEntryDes_Type = DisplayString
_Cps6000CopEntryDes_Object = MibTableColumn
cps6000CopEntryDes = _Cps6000CopEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 3),
    _Cps6000CopEntryDes_Type()
)
cps6000CopEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryDes.setStatus("current")
_Cps6000CopEntryTyp_Type = DisplayString
_Cps6000CopEntryTyp_Object = MibTableColumn
cps6000CopEntryTyp = _Cps6000CopEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 4),
    _Cps6000CopEntryTyp_Type()
)
cps6000CopEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryTyp.setStatus("current")
_Cps6000CopEntryPhn_Type = DisplayString
_Cps6000CopEntryPhn_Object = MibTableColumn
cps6000CopEntryPhn = _Cps6000CopEntryPhn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 5),
    _Cps6000CopEntryPhn_Type()
)
cps6000CopEntryPhn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryPhn.setStatus("current")


class _Cps6000CopEntryBdr_Type(Integer32):
    """Custom type cps6000CopEntryBdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000CopEntryBdr_Type.__name__ = "Integer32"
_Cps6000CopEntryBdr_Object = MibTableColumn
cps6000CopEntryBdr = _Cps6000CopEntryBdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 6),
    _Cps6000CopEntryBdr_Type()
)
cps6000CopEntryBdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryBdr.setStatus("current")


class _Cps6000CopEntryDbt_Type(Integer32):
    """Custom type cps6000CopEntryDbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Cps6000CopEntryDbt_Type.__name__ = "Integer32"
_Cps6000CopEntryDbt_Object = MibTableColumn
cps6000CopEntryDbt = _Cps6000CopEntryDbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 7),
    _Cps6000CopEntryDbt_Type()
)
cps6000CopEntryDbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryDbt.setStatus("current")
_Cps6000CopEntryPry_Type = DisplayString
_Cps6000CopEntryPry_Object = MibTableColumn
cps6000CopEntryPry = _Cps6000CopEntryPry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 8),
    _Cps6000CopEntryPry_Type()
)
cps6000CopEntryPry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryPry.setStatus("current")


class _Cps6000CopEntrySbt_Type(Integer32):
    """Custom type cps6000CopEntrySbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Cps6000CopEntrySbt_Type.__name__ = "Integer32"
_Cps6000CopEntrySbt_Object = MibTableColumn
cps6000CopEntrySbt = _Cps6000CopEntrySbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 9),
    _Cps6000CopEntrySbt_Type()
)
cps6000CopEntrySbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntrySbt.setStatus("current")


class _Cps6000CopEntryDly_Type(Integer32):
    """Custom type cps6000CopEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Cps6000CopEntryDly_Type.__name__ = "Integer32"
_Cps6000CopEntryDly_Object = MibTableColumn
cps6000CopEntryDly = _Cps6000CopEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 10),
    _Cps6000CopEntryDly_Type()
)
cps6000CopEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryDly.setStatus("current")
_Cps6000CopEntryPgr_Type = DisplayString
_Cps6000CopEntryPgr_Object = MibTableColumn
cps6000CopEntryPgr = _Cps6000CopEntryPgr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 11),
    _Cps6000CopEntryPgr_Type()
)
cps6000CopEntryPgr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryPgr.setStatus("current")
_Cps6000CopEntryMsg_Type = DisplayString
_Cps6000CopEntryMsg_Object = MibTableColumn
cps6000CopEntryMsg = _Cps6000CopEntryMsg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 18, 1, 12),
    _Cps6000CopEntryMsg_Type()
)
cps6000CopEntryMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CopEntryMsg.setStatus("current")
_Cps6000CoeTable_Object = MibTable
cps6000CoeTable = _Cps6000CoeTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19)
)
if mibBuilder.loadTexts:
    cps6000CoeTable.setStatus("current")
_Cps6000CoeEntry_Object = MibTableRow
cps6000CoeEntry = _Cps6000CoeEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1)
)
cps6000CoeEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000CoeEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000CoeEntry.setStatus("current")


class _Cps6000CoeEntryIndex_Type(Integer32):
    """Custom type cps6000CoeEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000CoeEntryIndex_Type.__name__ = "Integer32"
_Cps6000CoeEntryIndex_Object = MibTableColumn
cps6000CoeEntryIndex = _Cps6000CoeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1, 1),
    _Cps6000CoeEntryIndex_Type()
)
cps6000CoeEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CoeEntryIndex.setStatus("current")
_Cps6000CoeEntryIde_Type = DisplayString
_Cps6000CoeEntryIde_Object = MibTableColumn
cps6000CoeEntryIde = _Cps6000CoeEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1, 2),
    _Cps6000CoeEntryIde_Type()
)
cps6000CoeEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CoeEntryIde.setStatus("current")
_Cps6000CoeEntryDes_Type = DisplayString
_Cps6000CoeEntryDes_Object = MibTableColumn
cps6000CoeEntryDes = _Cps6000CoeEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1, 3),
    _Cps6000CoeEntryDes_Type()
)
cps6000CoeEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CoeEntryDes.setStatus("current")
_Cps6000CoeEntryAdr_Type = DisplayString
_Cps6000CoeEntryAdr_Object = MibTableColumn
cps6000CoeEntryAdr = _Cps6000CoeEntryAdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1, 4),
    _Cps6000CoeEntryAdr_Type()
)
cps6000CoeEntryAdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CoeEntryAdr.setStatus("current")
_Cps6000CoeEntryTyp_Type = DisplayString
_Cps6000CoeEntryTyp_Object = MibTableColumn
cps6000CoeEntryTyp = _Cps6000CoeEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 19, 1, 5),
    _Cps6000CoeEntryTyp_Type()
)
cps6000CoeEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CoeEntryTyp.setStatus("current")
_Cps6000SndTable_Object = MibTable
cps6000SndTable = _Cps6000SndTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20)
)
if mibBuilder.loadTexts:
    cps6000SndTable.setStatus("current")
_Cps6000SndEntry_Object = MibTableRow
cps6000SndEntry = _Cps6000SndEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1)
)
cps6000SndEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000SndEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000SndEntry.setStatus("current")


class _Cps6000SndEntryIndex_Type(Integer32):
    """Custom type cps6000SndEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000SndEntryIndex_Type.__name__ = "Integer32"
_Cps6000SndEntryIndex_Object = MibTableColumn
cps6000SndEntryIndex = _Cps6000SndEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1, 1),
    _Cps6000SndEntryIndex_Type()
)
cps6000SndEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000SndEntryIndex.setStatus("current")
_Cps6000SndEntryIde_Type = DisplayString
_Cps6000SndEntryIde_Object = MibTableColumn
cps6000SndEntryIde = _Cps6000SndEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1, 2),
    _Cps6000SndEntryIde_Type()
)
cps6000SndEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000SndEntryIde.setStatus("current")
_Cps6000SndEntryDes_Type = DisplayString
_Cps6000SndEntryDes_Object = MibTableColumn
cps6000SndEntryDes = _Cps6000SndEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1, 3),
    _Cps6000SndEntryDes_Type()
)
cps6000SndEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000SndEntryDes.setStatus("current")
_Cps6000SndEntryIp_Type = DisplayString
_Cps6000SndEntryIp_Object = MibTableColumn
cps6000SndEntryIp = _Cps6000SndEntryIp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1, 4),
    _Cps6000SndEntryIp_Type()
)
cps6000SndEntryIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000SndEntryIp.setStatus("current")
_Cps6000SndEntryCs_Type = DisplayString
_Cps6000SndEntryCs_Object = MibTableColumn
cps6000SndEntryCs = _Cps6000SndEntryCs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 20, 1, 5),
    _Cps6000SndEntryCs_Type()
)
cps6000SndEntryCs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000SndEntryCs.setStatus("current")
_Cps6000Po1_ObjectIdentity = ObjectIdentity
cps6000Po1 = _Cps6000Po1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21)
)
_Cps6000Po1Ide_Type = DisplayString
_Cps6000Po1Ide_Object = MibScalar
cps6000Po1Ide = _Cps6000Po1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 1),
    _Cps6000Po1Ide_Type()
)
cps6000Po1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Po1Ide.setStatus("current")
_Cps6000Po1Des_Type = DisplayString
_Cps6000Po1Des_Object = MibScalar
cps6000Po1Des = _Cps6000Po1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 2),
    _Cps6000Po1Des_Type()
)
cps6000Po1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Des.setStatus("current")
_Cps6000Po1Phn_Type = DisplayString
_Cps6000Po1Phn_Object = MibScalar
cps6000Po1Phn = _Cps6000Po1Phn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 3),
    _Cps6000Po1Phn_Type()
)
cps6000Po1Phn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Phn.setStatus("current")


class _Cps6000Po1Bdr_Type(Integer32):
    """Custom type cps6000Po1Bdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Po1Bdr_Type.__name__ = "Integer32"
_Cps6000Po1Bdr_Object = MibScalar
cps6000Po1Bdr = _Cps6000Po1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 4),
    _Cps6000Po1Bdr_Type()
)
cps6000Po1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Bdr.setStatus("current")


class _Cps6000Po1Dbt_Type(Integer32):
    """Custom type cps6000Po1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Cps6000Po1Dbt_Type.__name__ = "Integer32"
_Cps6000Po1Dbt_Object = MibScalar
cps6000Po1Dbt = _Cps6000Po1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 5),
    _Cps6000Po1Dbt_Type()
)
cps6000Po1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Dbt.setStatus("current")
_Cps6000Po1Pry_Type = DisplayString
_Cps6000Po1Pry_Object = MibScalar
cps6000Po1Pry = _Cps6000Po1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 6),
    _Cps6000Po1Pry_Type()
)
cps6000Po1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Pry.setStatus("current")


class _Cps6000Po1Sbt_Type(Integer32):
    """Custom type cps6000Po1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Cps6000Po1Sbt_Type.__name__ = "Integer32"
_Cps6000Po1Sbt_Object = MibScalar
cps6000Po1Sbt = _Cps6000Po1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 7),
    _Cps6000Po1Sbt_Type()
)
cps6000Po1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Sbt.setStatus("current")
_Cps6000Po1Int_Type = DisplayString
_Cps6000Po1Int_Object = MibScalar
cps6000Po1Int = _Cps6000Po1Int_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 8),
    _Cps6000Po1Int_Type()
)
cps6000Po1Int.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Int.setStatus("current")
_Cps6000Po1Tim_Type = DisplayString
_Cps6000Po1Tim_Object = MibScalar
cps6000Po1Tim = _Cps6000Po1Tim_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 9),
    _Cps6000Po1Tim_Type()
)
cps6000Po1Tim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Tim.setStatus("current")
_Cps6000Po1Cl01_Type = DisplayString
_Cps6000Po1Cl01_Object = MibScalar
cps6000Po1Cl01 = _Cps6000Po1Cl01_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 10),
    _Cps6000Po1Cl01_Type()
)
cps6000Po1Cl01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl01.setStatus("current")
_Cps6000Po1Cl02_Type = DisplayString
_Cps6000Po1Cl02_Object = MibScalar
cps6000Po1Cl02 = _Cps6000Po1Cl02_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 11),
    _Cps6000Po1Cl02_Type()
)
cps6000Po1Cl02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl02.setStatus("current")
_Cps6000Po1Cl03_Type = DisplayString
_Cps6000Po1Cl03_Object = MibScalar
cps6000Po1Cl03 = _Cps6000Po1Cl03_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 12),
    _Cps6000Po1Cl03_Type()
)
cps6000Po1Cl03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl03.setStatus("current")
_Cps6000Po1Cl04_Type = DisplayString
_Cps6000Po1Cl04_Object = MibScalar
cps6000Po1Cl04 = _Cps6000Po1Cl04_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 13),
    _Cps6000Po1Cl04_Type()
)
cps6000Po1Cl04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl04.setStatus("current")
_Cps6000Po1Cl05_Type = DisplayString
_Cps6000Po1Cl05_Object = MibScalar
cps6000Po1Cl05 = _Cps6000Po1Cl05_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 14),
    _Cps6000Po1Cl05_Type()
)
cps6000Po1Cl05.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl05.setStatus("current")
_Cps6000Po1Cl06_Type = DisplayString
_Cps6000Po1Cl06_Object = MibScalar
cps6000Po1Cl06 = _Cps6000Po1Cl06_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 15),
    _Cps6000Po1Cl06_Type()
)
cps6000Po1Cl06.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl06.setStatus("current")
_Cps6000Po1Cl07_Type = DisplayString
_Cps6000Po1Cl07_Object = MibScalar
cps6000Po1Cl07 = _Cps6000Po1Cl07_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 16),
    _Cps6000Po1Cl07_Type()
)
cps6000Po1Cl07.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl07.setStatus("current")
_Cps6000Po1Cl08_Type = DisplayString
_Cps6000Po1Cl08_Object = MibScalar
cps6000Po1Cl08 = _Cps6000Po1Cl08_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 17),
    _Cps6000Po1Cl08_Type()
)
cps6000Po1Cl08.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl08.setStatus("current")
_Cps6000Po1Cl09_Type = DisplayString
_Cps6000Po1Cl09_Object = MibScalar
cps6000Po1Cl09 = _Cps6000Po1Cl09_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 18),
    _Cps6000Po1Cl09_Type()
)
cps6000Po1Cl09.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl09.setStatus("current")
_Cps6000Po1Cl10_Type = DisplayString
_Cps6000Po1Cl10_Object = MibScalar
cps6000Po1Cl10 = _Cps6000Po1Cl10_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 19),
    _Cps6000Po1Cl10_Type()
)
cps6000Po1Cl10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Po1Cl10.setStatus("current")
_Cps6000Po1Por_Type = DisplayString
_Cps6000Po1Por_Object = MibScalar
cps6000Po1Por = _Cps6000Po1Por_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 21, 20),
    _Cps6000Po1Por_Type()
)
cps6000Po1Por.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Po1Por.setStatus("current")
_Cps6000Cb1_ObjectIdentity = ObjectIdentity
cps6000Cb1 = _Cps6000Cb1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22)
)
_Cps6000Cb1Ide_Type = DisplayString
_Cps6000Cb1Ide_Object = MibScalar
cps6000Cb1Ide = _Cps6000Cb1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 1),
    _Cps6000Cb1Ide_Type()
)
cps6000Cb1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Cb1Ide.setStatus("current")
_Cps6000Cb1Des_Type = DisplayString
_Cps6000Cb1Des_Object = MibScalar
cps6000Cb1Des = _Cps6000Cb1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 2),
    _Cps6000Cb1Des_Type()
)
cps6000Cb1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Des.setStatus("current")


class _Cps6000Cb1Stt_Type(Integer32):
    """Custom type cps6000Cb1Stt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Cps6000Cb1Stt_Type.__name__ = "Integer32"
_Cps6000Cb1Stt_Object = MibScalar
cps6000Cb1Stt = _Cps6000Cb1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 3),
    _Cps6000Cb1Stt_Type()
)
cps6000Cb1Stt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Stt.setStatus("current")
_Cps6000Cb1Ph1_Type = DisplayString
_Cps6000Cb1Ph1_Object = MibScalar
cps6000Cb1Ph1 = _Cps6000Cb1Ph1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 4),
    _Cps6000Cb1Ph1_Type()
)
cps6000Cb1Ph1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Ph1.setStatus("current")


class _Cps6000Cb1Br1_Type(Integer32):
    """Custom type cps6000Cb1Br1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Cb1Br1_Type.__name__ = "Integer32"
_Cps6000Cb1Br1_Object = MibScalar
cps6000Cb1Br1 = _Cps6000Cb1Br1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 5),
    _Cps6000Cb1Br1_Type()
)
cps6000Cb1Br1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Br1.setStatus("current")
_Cps6000Cb1Ph2_Type = DisplayString
_Cps6000Cb1Ph2_Object = MibScalar
cps6000Cb1Ph2 = _Cps6000Cb1Ph2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 6),
    _Cps6000Cb1Ph2_Type()
)
cps6000Cb1Ph2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Ph2.setStatus("current")


class _Cps6000Cb1Br2_Type(Integer32):
    """Custom type cps6000Cb1Br2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Cb1Br2_Type.__name__ = "Integer32"
_Cps6000Cb1Br2_Object = MibScalar
cps6000Cb1Br2 = _Cps6000Cb1Br2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 7),
    _Cps6000Cb1Br2_Type()
)
cps6000Cb1Br2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Br2.setStatus("current")
_Cps6000Cb1Ph3_Type = DisplayString
_Cps6000Cb1Ph3_Object = MibScalar
cps6000Cb1Ph3 = _Cps6000Cb1Ph3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 8),
    _Cps6000Cb1Ph3_Type()
)
cps6000Cb1Ph3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Ph3.setStatus("current")


class _Cps6000Cb1Br3_Type(Integer32):
    """Custom type cps6000Cb1Br3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Cb1Br3_Type.__name__ = "Integer32"
_Cps6000Cb1Br3_Object = MibScalar
cps6000Cb1Br3 = _Cps6000Cb1Br3_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 9),
    _Cps6000Cb1Br3_Type()
)
cps6000Cb1Br3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Br3.setStatus("current")
_Cps6000Cb1Ph4_Type = DisplayString
_Cps6000Cb1Ph4_Object = MibScalar
cps6000Cb1Ph4 = _Cps6000Cb1Ph4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 10),
    _Cps6000Cb1Ph4_Type()
)
cps6000Cb1Ph4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Ph4.setStatus("current")


class _Cps6000Cb1Br4_Type(Integer32):
    """Custom type cps6000Cb1Br4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Cb1Br4_Type.__name__ = "Integer32"
_Cps6000Cb1Br4_Object = MibScalar
cps6000Cb1Br4 = _Cps6000Cb1Br4_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 11),
    _Cps6000Cb1Br4_Type()
)
cps6000Cb1Br4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Br4.setStatus("current")
_Cps6000Cb1Ph5_Type = DisplayString
_Cps6000Cb1Ph5_Object = MibScalar
cps6000Cb1Ph5 = _Cps6000Cb1Ph5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 12),
    _Cps6000Cb1Ph5_Type()
)
cps6000Cb1Ph5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Ph5.setStatus("current")


class _Cps6000Cb1Br5_Type(Integer32):
    """Custom type cps6000Cb1Br5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Cb1Br5_Type.__name__ = "Integer32"
_Cps6000Cb1Br5_Object = MibScalar
cps6000Cb1Br5 = _Cps6000Cb1Br5_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 22, 13),
    _Cps6000Cb1Br5_Type()
)
cps6000Cb1Br5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Cb1Br5.setStatus("current")
_Cps6000Mp1_ObjectIdentity = ObjectIdentity
cps6000Mp1 = _Cps6000Mp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23)
)
_Cps6000Mp1Ide_Type = DisplayString
_Cps6000Mp1Ide_Object = MibScalar
cps6000Mp1Ide = _Cps6000Mp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 1),
    _Cps6000Mp1Ide_Type()
)
cps6000Mp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Mp1Ide.setStatus("current")
_Cps6000Mp1Des_Type = DisplayString
_Cps6000Mp1Des_Object = MibScalar
cps6000Mp1Des = _Cps6000Mp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 2),
    _Cps6000Mp1Des_Type()
)
cps6000Mp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Des.setStatus("current")
_Cps6000Mp1Stt_Type = DisplayString
_Cps6000Mp1Stt_Object = MibScalar
cps6000Mp1Stt = _Cps6000Mp1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 3),
    _Cps6000Mp1Stt_Type()
)
cps6000Mp1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Mp1Stt.setStatus("current")


class _Cps6000Mp1Dbt_Type(Integer32):
    """Custom type cps6000Mp1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Cps6000Mp1Dbt_Type.__name__ = "Integer32"
_Cps6000Mp1Dbt_Object = MibScalar
cps6000Mp1Dbt = _Cps6000Mp1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 4),
    _Cps6000Mp1Dbt_Type()
)
cps6000Mp1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Dbt.setStatus("current")


class _Cps6000Mp1Bdr_Type(Integer32):
    """Custom type cps6000Mp1Bdr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              1200,
              2400,
              4800,
              9600,
              19200)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b300", 300),
          ("b4800", 4800),
          ("b9600", 9600))
    )


_Cps6000Mp1Bdr_Type.__name__ = "Integer32"
_Cps6000Mp1Bdr_Object = MibScalar
cps6000Mp1Bdr = _Cps6000Mp1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 5),
    _Cps6000Mp1Bdr_Type()
)
cps6000Mp1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Bdr.setStatus("current")
_Cps6000Mp1Pry_Type = DisplayString
_Cps6000Mp1Pry_Object = MibScalar
cps6000Mp1Pry = _Cps6000Mp1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 6),
    _Cps6000Mp1Pry_Type()
)
cps6000Mp1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Pry.setStatus("current")


class _Cps6000Mp1Sbt_Type(Integer32):
    """Custom type cps6000Mp1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Cps6000Mp1Sbt_Type.__name__ = "Integer32"
_Cps6000Mp1Sbt_Object = MibScalar
cps6000Mp1Sbt = _Cps6000Mp1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 7),
    _Cps6000Mp1Sbt_Type()
)
cps6000Mp1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Sbt.setStatus("current")


class _Cps6000Mp1Tmo_Type(Integer32):
    """Custom type cps6000Mp1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_Cps6000Mp1Tmo_Type.__name__ = "Integer32"
_Cps6000Mp1Tmo_Object = MibScalar
cps6000Mp1Tmo = _Cps6000Mp1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 8),
    _Cps6000Mp1Tmo_Type()
)
cps6000Mp1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Tmo.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Mp1Tmo.setUnits("Minutes")
_Cps6000Mp1Hsh_Type = DisplayString
_Cps6000Mp1Hsh_Object = MibScalar
cps6000Mp1Hsh = _Cps6000Mp1Hsh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 9),
    _Cps6000Mp1Hsh_Type()
)
cps6000Mp1Hsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Hsh.setStatus("current")


class _Cps6000Mp1Nrg_Type(Integer32):
    """Custom type cps6000Mp1Nrg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 15),
    )


_Cps6000Mp1Nrg_Type.__name__ = "Integer32"
_Cps6000Mp1Nrg_Object = MibScalar
cps6000Mp1Nrg = _Cps6000Mp1Nrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 10),
    _Cps6000Mp1Nrg_Type()
)
cps6000Mp1Nrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Nrg.setStatus("current")


class _Cps6000Mp1Wre_Type(Integer32):
    """Custom type cps6000Mp1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Mp1Wre_Type.__name__ = "Integer32"
_Cps6000Mp1Wre_Object = MibScalar
cps6000Mp1Wre = _Cps6000Mp1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 11),
    _Cps6000Mp1Wre_Type()
)
cps6000Mp1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Wre.setStatus("current")
_Cps6000Mp1Ins_Type = DisplayString
_Cps6000Mp1Ins_Object = MibScalar
cps6000Mp1Ins = _Cps6000Mp1Ins_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 23, 12),
    _Cps6000Mp1Ins_Type()
)
cps6000Mp1Ins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Mp1Ins.setStatus("current")
_Cps6000Lp1_ObjectIdentity = ObjectIdentity
cps6000Lp1 = _Cps6000Lp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24)
)
_Cps6000Lp1Ide_Type = DisplayString
_Cps6000Lp1Ide_Object = MibScalar
cps6000Lp1Ide = _Cps6000Lp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 1),
    _Cps6000Lp1Ide_Type()
)
cps6000Lp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Lp1Ide.setStatus("current")
_Cps6000Lp1Des_Type = DisplayString
_Cps6000Lp1Des_Object = MibScalar
cps6000Lp1Des = _Cps6000Lp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 2),
    _Cps6000Lp1Des_Type()
)
cps6000Lp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Des.setStatus("current")
_Cps6000Lp1Stt_Type = DisplayString
_Cps6000Lp1Stt_Object = MibScalar
cps6000Lp1Stt = _Cps6000Lp1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 3),
    _Cps6000Lp1Stt_Type()
)
cps6000Lp1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Lp1Stt.setStatus("current")
_Cps6000Lp1Bdr_Type = DisplayString
_Cps6000Lp1Bdr_Object = MibScalar
cps6000Lp1Bdr = _Cps6000Lp1Bdr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 4),
    _Cps6000Lp1Bdr_Type()
)
cps6000Lp1Bdr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Bdr.setStatus("current")


class _Cps6000Lp1Dbt_Type(Integer32):
    """Custom type cps6000Lp1Dbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("d7", 7),
          ("d8", 8))
    )


_Cps6000Lp1Dbt_Type.__name__ = "Integer32"
_Cps6000Lp1Dbt_Object = MibScalar
cps6000Lp1Dbt = _Cps6000Lp1Dbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 5),
    _Cps6000Lp1Dbt_Type()
)
cps6000Lp1Dbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Dbt.setStatus("current")
_Cps6000Lp1Pry_Type = DisplayString
_Cps6000Lp1Pry_Object = MibScalar
cps6000Lp1Pry = _Cps6000Lp1Pry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 6),
    _Cps6000Lp1Pry_Type()
)
cps6000Lp1Pry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Pry.setStatus("current")


class _Cps6000Lp1Sbt_Type(Integer32):
    """Custom type cps6000Lp1Sbt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_Cps6000Lp1Sbt_Type.__name__ = "Integer32"
_Cps6000Lp1Sbt_Object = MibScalar
cps6000Lp1Sbt = _Cps6000Lp1Sbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 7),
    _Cps6000Lp1Sbt_Type()
)
cps6000Lp1Sbt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Sbt.setStatus("current")


class _Cps6000Lp1Tmo_Type(Integer32):
    """Custom type cps6000Lp1Tmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 45),
    )


_Cps6000Lp1Tmo_Type.__name__ = "Integer32"
_Cps6000Lp1Tmo_Object = MibScalar
cps6000Lp1Tmo = _Cps6000Lp1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 8),
    _Cps6000Lp1Tmo_Type()
)
cps6000Lp1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Tmo.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Lp1Tmo.setUnits("Minutes")
_Cps6000Lp1Hsh_Type = DisplayString
_Cps6000Lp1Hsh_Object = MibScalar
cps6000Lp1Hsh = _Cps6000Lp1Hsh_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 9),
    _Cps6000Lp1Hsh_Type()
)
cps6000Lp1Hsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Hsh.setStatus("current")
_Cps6000Lp1App_Type = DisplayString
_Cps6000Lp1App_Object = MibScalar
cps6000Lp1App = _Cps6000Lp1App_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 10),
    _Cps6000Lp1App_Type()
)
cps6000Lp1App.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1App.setStatus("current")


class _Cps6000Lp1Wre_Type(Integer32):
    """Custom type cps6000Lp1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Lp1Wre_Type.__name__ = "Integer32"
_Cps6000Lp1Wre_Object = MibScalar
cps6000Lp1Wre = _Cps6000Lp1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 24, 11),
    _Cps6000Lp1Wre_Type()
)
cps6000Lp1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Lp1Wre.setStatus("current")
_Cps6000Tlm1_ObjectIdentity = ObjectIdentity
cps6000Tlm1 = _Cps6000Tlm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25)
)
_Cps6000Tlm1Ide_Type = DisplayString
_Cps6000Tlm1Ide_Object = MibScalar
cps6000Tlm1Ide = _Cps6000Tlm1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 1),
    _Cps6000Tlm1Ide_Type()
)
cps6000Tlm1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Tlm1Ide.setStatus("current")
_Cps6000Tlm1Des_Type = DisplayString
_Cps6000Tlm1Des_Object = MibScalar
cps6000Tlm1Des = _Cps6000Tlm1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 2),
    _Cps6000Tlm1Des_Type()
)
cps6000Tlm1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tlm1Des.setStatus("current")


class _Cps6000Tlm1Aue_Type(Integer32):
    """Custom type cps6000Tlm1Aue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Tlm1Aue_Type.__name__ = "Integer32"
_Cps6000Tlm1Aue_Object = MibScalar
cps6000Tlm1Aue = _Cps6000Tlm1Aue_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 3),
    _Cps6000Tlm1Aue_Type()
)
cps6000Tlm1Aue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tlm1Aue.setStatus("current")


class _Cps6000Tlm1Cts_Type(Integer32):
    """Custom type cps6000Tlm1Cts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Tlm1Cts_Type.__name__ = "Integer32"
_Cps6000Tlm1Cts_Object = MibScalar
cps6000Tlm1Cts = _Cps6000Tlm1Cts_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 4),
    _Cps6000Tlm1Cts_Type()
)
cps6000Tlm1Cts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tlm1Cts.setStatus("current")


class _Cps6000Tlm1Dsr_Type(Integer32):
    """Custom type cps6000Tlm1Dsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Tlm1Dsr_Type.__name__ = "Integer32"
_Cps6000Tlm1Dsr_Object = MibScalar
cps6000Tlm1Dsr = _Cps6000Tlm1Dsr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 5),
    _Cps6000Tlm1Dsr_Type()
)
cps6000Tlm1Dsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tlm1Dsr.setStatus("current")
_Cps6000Tlm1Prt_Type = Integer32
_Cps6000Tlm1Prt_Object = MibScalar
cps6000Tlm1Prt = _Cps6000Tlm1Prt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 25, 6),
    _Cps6000Tlm1Prt_Type()
)
cps6000Tlm1Prt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tlm1Prt.setStatus("current")
_Cps6000Tl1Table_Object = MibTable
cps6000Tl1Table = _Cps6000Tl1Table_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26)
)
if mibBuilder.loadTexts:
    cps6000Tl1Table.setStatus("current")
_Cps6000Tl1Entry_Object = MibTableRow
cps6000Tl1Entry = _Cps6000Tl1Entry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1)
)
cps6000Tl1Entry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000Tl1EntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000Tl1Entry.setStatus("current")


class _Cps6000Tl1EntryIndex_Type(Integer32):
    """Custom type cps6000Tl1EntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000Tl1EntryIndex_Type.__name__ = "Integer32"
_Cps6000Tl1EntryIndex_Object = MibTableColumn
cps6000Tl1EntryIndex = _Cps6000Tl1EntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 1),
    _Cps6000Tl1EntryIndex_Type()
)
cps6000Tl1EntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Tl1EntryIndex.setStatus("current")
_Cps6000Tl1EntryIde_Type = DisplayString
_Cps6000Tl1EntryIde_Object = MibTableColumn
cps6000Tl1EntryIde = _Cps6000Tl1EntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 2),
    _Cps6000Tl1EntryIde_Type()
)
cps6000Tl1EntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Tl1EntryIde.setStatus("current")
_Cps6000Tl1EntryDes_Type = DisplayString
_Cps6000Tl1EntryDes_Object = MibTableColumn
cps6000Tl1EntryDes = _Cps6000Tl1EntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 3),
    _Cps6000Tl1EntryDes_Type()
)
cps6000Tl1EntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntryDes.setStatus("current")
_Cps6000Tl1EntryCds_Type = DisplayString
_Cps6000Tl1EntryCds_Object = MibTableColumn
cps6000Tl1EntryCds = _Cps6000Tl1EntryCds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 4),
    _Cps6000Tl1EntryCds_Type()
)
cps6000Tl1EntryCds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntryCds.setStatus("current")
_Cps6000Tl1EntryAid_Type = DisplayString
_Cps6000Tl1EntryAid_Object = MibTableColumn
cps6000Tl1EntryAid = _Cps6000Tl1EntryAid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 5),
    _Cps6000Tl1EntryAid_Type()
)
cps6000Tl1EntryAid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntryAid.setStatus("current")
_Cps6000Tl1EntryCnd_Type = DisplayString
_Cps6000Tl1EntryCnd_Object = MibTableColumn
cps6000Tl1EntryCnd = _Cps6000Tl1EntryCnd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 6),
    _Cps6000Tl1EntryCnd_Type()
)
cps6000Tl1EntryCnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntryCnd.setStatus("current")


class _Cps6000Tl1EntrySaf_Type(Integer32):
    """Custom type cps6000Tl1EntrySaf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000Tl1EntrySaf_Type.__name__ = "Integer32"
_Cps6000Tl1EntrySaf_Object = MibTableColumn
cps6000Tl1EntrySaf = _Cps6000Tl1EntrySaf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 7),
    _Cps6000Tl1EntrySaf_Type()
)
cps6000Tl1EntrySaf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntrySaf.setStatus("current")
_Cps6000Tl1EntryRpt_Type = DisplayString
_Cps6000Tl1EntryRpt_Object = MibTableColumn
cps6000Tl1EntryRpt = _Cps6000Tl1EntryRpt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 26, 1, 8),
    _Cps6000Tl1EntryRpt_Type()
)
cps6000Tl1EntryRpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Tl1EntryRpt.setStatus("current")
_Cps6000Net1_ObjectIdentity = ObjectIdentity
cps6000Net1 = _Cps6000Net1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27)
)
_Cps6000Net1Ide_Type = DisplayString
_Cps6000Net1Ide_Object = MibScalar
cps6000Net1Ide = _Cps6000Net1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 1),
    _Cps6000Net1Ide_Type()
)
cps6000Net1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Net1Ide.setStatus("current")
_Cps6000Net1Des_Type = DisplayString
_Cps6000Net1Des_Object = MibScalar
cps6000Net1Des = _Cps6000Net1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 2),
    _Cps6000Net1Des_Type()
)
cps6000Net1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Des.setStatus("current")
_Cps6000Net1Ead_Type = DisplayString
_Cps6000Net1Ead_Object = MibScalar
cps6000Net1Ead = _Cps6000Net1Ead_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 3),
    _Cps6000Net1Ead_Type()
)
cps6000Net1Ead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Net1Ead.setStatus("current")


class _Cps6000Net1Dhcp_Type(Integer32):
    """Custom type cps6000Net1Dhcp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Net1Dhcp_Type.__name__ = "Integer32"
_Cps6000Net1Dhcp_Object = MibScalar
cps6000Net1Dhcp = _Cps6000Net1Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 4),
    _Cps6000Net1Dhcp_Type()
)
cps6000Net1Dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Dhcp.setStatus("current")
_Cps6000Net1Ip_Type = DisplayString
_Cps6000Net1Ip_Object = MibScalar
cps6000Net1Ip = _Cps6000Net1Ip_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 5),
    _Cps6000Net1Ip_Type()
)
cps6000Net1Ip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Ip.setStatus("current")
_Cps6000Net1Wip_Type = DisplayString
_Cps6000Net1Wip_Object = MibScalar
cps6000Net1Wip = _Cps6000Net1Wip_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 6),
    _Cps6000Net1Wip_Type()
)
cps6000Net1Wip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Net1Wip.setStatus("current")
_Cps6000Net1Sub_Type = DisplayString
_Cps6000Net1Sub_Object = MibScalar
cps6000Net1Sub = _Cps6000Net1Sub_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 7),
    _Cps6000Net1Sub_Type()
)
cps6000Net1Sub.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Sub.setStatus("current")
_Cps6000Net1Gtwy_Type = DisplayString
_Cps6000Net1Gtwy_Object = MibScalar
cps6000Net1Gtwy = _Cps6000Net1Gtwy_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 8),
    _Cps6000Net1Gtwy_Type()
)
cps6000Net1Gtwy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Gtwy.setStatus("current")
_Cps6000Net1Host_Type = DisplayString
_Cps6000Net1Host_Object = MibScalar
cps6000Net1Host = _Cps6000Net1Host_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 9),
    _Cps6000Net1Host_Type()
)
cps6000Net1Host.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Host.setStatus("current")
_Cps6000Net1Dom_Type = DisplayString
_Cps6000Net1Dom_Object = MibScalar
cps6000Net1Dom = _Cps6000Net1Dom_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 10),
    _Cps6000Net1Dom_Type()
)
cps6000Net1Dom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Dom.setStatus("current")
_Cps6000Net1Dns_Type = DisplayString
_Cps6000Net1Dns_Object = MibScalar
cps6000Net1Dns = _Cps6000Net1Dns_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 11),
    _Cps6000Net1Dns_Type()
)
cps6000Net1Dns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Dns.setStatus("current")


class _Cps6000Net1Wre_Type(Integer32):
    """Custom type cps6000Net1Wre based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Net1Wre_Type.__name__ = "Integer32"
_Cps6000Net1Wre_Object = MibScalar
cps6000Net1Wre = _Cps6000Net1Wre_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 12),
    _Cps6000Net1Wre_Type()
)
cps6000Net1Wre.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Wre.setStatus("current")
_Cps6000Net1Tmo_Type = Integer32
_Cps6000Net1Tmo_Object = MibScalar
cps6000Net1Tmo = _Cps6000Net1Tmo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 13),
    _Cps6000Net1Tmo_Type()
)
cps6000Net1Tmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Tmo.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Net1Tmo.setUnits("Minutes")
_Cps6000Net1Msrv_Type = DisplayString
_Cps6000Net1Msrv_Object = MibScalar
cps6000Net1Msrv = _Cps6000Net1Msrv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 27, 14),
    _Cps6000Net1Msrv_Type()
)
cps6000Net1Msrv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Net1Msrv.setStatus("current")
_Cps6000DrcTable_Object = MibTable
cps6000DrcTable = _Cps6000DrcTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28)
)
if mibBuilder.loadTexts:
    cps6000DrcTable.setStatus("current")
_Cps6000DrcEntry_Object = MibTableRow
cps6000DrcEntry = _Cps6000DrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1)
)
cps6000DrcEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000DrcEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000DrcEntry.setStatus("current")


class _Cps6000DrcEntryIndex_Type(Integer32):
    """Custom type cps6000DrcEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000DrcEntryIndex_Type.__name__ = "Integer32"
_Cps6000DrcEntryIndex_Object = MibTableColumn
cps6000DrcEntryIndex = _Cps6000DrcEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 1),
    _Cps6000DrcEntryIndex_Type()
)
cps6000DrcEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DrcEntryIndex.setStatus("current")
_Cps6000DrcEntryIde_Type = DisplayString
_Cps6000DrcEntryIde_Object = MibTableColumn
cps6000DrcEntryIde = _Cps6000DrcEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 2),
    _Cps6000DrcEntryIde_Type()
)
cps6000DrcEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DrcEntryIde.setStatus("current")
_Cps6000DrcEntryDes_Type = DisplayString
_Cps6000DrcEntryDes_Object = MibTableColumn
cps6000DrcEntryDes = _Cps6000DrcEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 3),
    _Cps6000DrcEntryDes_Type()
)
cps6000DrcEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DrcEntryDes.setStatus("current")
_Cps6000DrcEntryVal_Type = DisplayString
_Cps6000DrcEntryVal_Object = MibTableColumn
cps6000DrcEntryVal = _Cps6000DrcEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 4),
    _Cps6000DrcEntryVal_Type()
)
cps6000DrcEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000DrcEntryVal.setStatus("current")
_Cps6000DrcEntryPrg_Type = DisplayString
_Cps6000DrcEntryPrg_Object = MibTableColumn
cps6000DrcEntryPrg = _Cps6000DrcEntryPrg_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 5),
    _Cps6000DrcEntryPrg_Type()
)
cps6000DrcEntryPrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DrcEntryPrg.setStatus("current")
_Cps6000DrcEntryUni_Type = DisplayString
_Cps6000DrcEntryUni_Object = MibTableColumn
cps6000DrcEntryUni = _Cps6000DrcEntryUni_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 28, 1, 6),
    _Cps6000DrcEntryUni_Type()
)
cps6000DrcEntryUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000DrcEntryUni.setStatus("current")
_Cps6000InpTable_Object = MibTable
cps6000InpTable = _Cps6000InpTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29)
)
if mibBuilder.loadTexts:
    cps6000InpTable.setStatus("current")
_Cps6000InpEntry_Object = MibTableRow
cps6000InpEntry = _Cps6000InpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1)
)
cps6000InpEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000InpEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000InpEntry.setStatus("current")


class _Cps6000InpEntryIndex_Type(Integer32):
    """Custom type cps6000InpEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000InpEntryIndex_Type.__name__ = "Integer32"
_Cps6000InpEntryIndex_Object = MibTableColumn
cps6000InpEntryIndex = _Cps6000InpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 1),
    _Cps6000InpEntryIndex_Type()
)
cps6000InpEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000InpEntryIndex.setStatus("current")
_Cps6000InpEntryIde_Type = DisplayString
_Cps6000InpEntryIde_Object = MibTableColumn
cps6000InpEntryIde = _Cps6000InpEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 2),
    _Cps6000InpEntryIde_Type()
)
cps6000InpEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000InpEntryIde.setStatus("current")
_Cps6000InpEntryDes_Type = DisplayString
_Cps6000InpEntryDes_Object = MibTableColumn
cps6000InpEntryDes = _Cps6000InpEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 3),
    _Cps6000InpEntryDes_Type()
)
cps6000InpEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000InpEntryDes.setStatus("current")


class _Cps6000InpEntryStt_Type(Integer32):
    """Custom type cps6000InpEntryStt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarming", 1),
          ("nonAlarming", 0))
    )


_Cps6000InpEntryStt_Type.__name__ = "Integer32"
_Cps6000InpEntryStt_Object = MibTableColumn
cps6000InpEntryStt = _Cps6000InpEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 4),
    _Cps6000InpEntryStt_Type()
)
cps6000InpEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000InpEntryStt.setStatus("current")
_Cps6000InpEntryTyp_Type = DisplayString
_Cps6000InpEntryTyp_Object = MibTableColumn
cps6000InpEntryTyp = _Cps6000InpEntryTyp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 5),
    _Cps6000InpEntryTyp_Type()
)
cps6000InpEntryTyp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000InpEntryTyp.setStatus("current")
_Cps6000InpEntryPol_Type = DisplayString
_Cps6000InpEntryPol_Object = MibTableColumn
cps6000InpEntryPol = _Cps6000InpEntryPol_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 6),
    _Cps6000InpEntryPol_Type()
)
cps6000InpEntryPol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000InpEntryPol.setStatus("current")
_Cps6000InpEntrySn_Type = DisplayString
_Cps6000InpEntrySn_Object = MibTableColumn
cps6000InpEntrySn = _Cps6000InpEntrySn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 7),
    _Cps6000InpEntrySn_Type()
)
cps6000InpEntrySn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000InpEntrySn.setStatus("current")
_Cps6000InpEntryBrc_Type = DisplayString
_Cps6000InpEntryBrc_Object = MibTableColumn
cps6000InpEntryBrc = _Cps6000InpEntryBrc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 29, 1, 8),
    _Cps6000InpEntryBrc_Type()
)
cps6000InpEntryBrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000InpEntryBrc.setStatus("current")
_Cps6000Rp1_ObjectIdentity = ObjectIdentity
cps6000Rp1 = _Cps6000Rp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30)
)
_Cps6000Rp1Ide_Type = DisplayString
_Cps6000Rp1Ide_Object = MibScalar
cps6000Rp1Ide = _Cps6000Rp1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 1),
    _Cps6000Rp1Ide_Type()
)
cps6000Rp1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Ide.setStatus("current")
_Cps6000Rp1Des_Type = DisplayString
_Cps6000Rp1Des_Object = MibScalar
cps6000Rp1Des = _Cps6000Rp1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 2),
    _Cps6000Rp1Des_Type()
)
cps6000Rp1Des.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Des.setStatus("current")


class _Cps6000Rp1Frq_Type(Integer32):
    """Custom type cps6000Rp1Frq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 50),
    )


_Cps6000Rp1Frq_Type.__name__ = "Integer32"
_Cps6000Rp1Frq_Object = MibScalar
cps6000Rp1Frq = _Cps6000Rp1Frq_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 3),
    _Cps6000Rp1Frq_Type()
)
cps6000Rp1Frq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Frq.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Rp1Frq.setUnits("Hz")


class _Cps6000Rp1Vsp_Type(Integer32):
    """Custom type cps6000Rp1Vsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 100),
    )


_Cps6000Rp1Vsp_Type.__name__ = "Integer32"
_Cps6000Rp1Vsp_Object = MibScalar
cps6000Rp1Vsp = _Cps6000Rp1Vsp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 4),
    _Cps6000Rp1Vsp_Type()
)
cps6000Rp1Vsp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Vsp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Rp1Vsp.setUnits("Volts")


class _Cps6000Rp1Ofe_Type(Integer32):
    """Custom type cps6000Rp1Ofe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Rp1Ofe_Type.__name__ = "Integer32"
_Cps6000Rp1Ofe_Object = MibScalar
cps6000Rp1Ofe = _Cps6000Rp1Ofe_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 5),
    _Cps6000Rp1Ofe_Type()
)
cps6000Rp1Ofe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Ofe.setStatus("current")


class _Cps6000Rp1Rme_Type(Integer32):
    """Custom type cps6000Rp1Rme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Rp1Rme_Type.__name__ = "Integer32"
_Cps6000Rp1Rme_Object = MibScalar
cps6000Rp1Rme = _Cps6000Rp1Rme_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 6),
    _Cps6000Rp1Rme_Type()
)
cps6000Rp1Rme.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Rme.setStatus("current")


class _Cps6000Rp1Rss_Type(Integer32):
    """Custom type cps6000Rp1Rss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_Cps6000Rp1Rss_Type.__name__ = "Integer32"
_Cps6000Rp1Rss_Object = MibScalar
cps6000Rp1Rss = _Cps6000Rp1Rss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 7),
    _Cps6000Rp1Rss_Type()
)
cps6000Rp1Rss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Rp1Rss.setStatus("current")
_Cps6000Rp1Rf_Type = DisplayString
_Cps6000Rp1Rf_Object = MibScalar
cps6000Rp1Rf = _Cps6000Rp1Rf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 8),
    _Cps6000Rp1Rf_Type()
)
cps6000Rp1Rf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rf.setStatus("current")
_Cps6000Rp1Rpff_Type = DisplayString
_Cps6000Rp1Rpff_Object = MibScalar
cps6000Rp1Rpff = _Cps6000Rp1Rpff_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 9),
    _Cps6000Rp1Rpff_Type()
)
cps6000Rp1Rpff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rpff.setStatus("current")
_Cps6000Rp1Rpxj_Type = DisplayString
_Cps6000Rp1Rpxj_Object = MibScalar
cps6000Rp1Rpxj = _Cps6000Rp1Rpxj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 10),
    _Cps6000Rp1Rpxj_Type()
)
cps6000Rp1Rpxj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rpxj.setStatus("current")
_Cps6000Rp1Rpxn_Type = DisplayString
_Cps6000Rp1Rpxn_Object = MibScalar
cps6000Rp1Rpxn = _Cps6000Rp1Rpxn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 11),
    _Cps6000Rp1Rpxn_Type()
)
cps6000Rp1Rpxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rpxn.setStatus("current")
_Cps6000Rp1Rprl_Type = DisplayString
_Cps6000Rp1Rprl_Object = MibScalar
cps6000Rp1Rprl = _Cps6000Rp1Rprl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 12),
    _Cps6000Rp1Rprl_Type()
)
cps6000Rp1Rprl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rprl.setStatus("current")
_Cps6000Rp1Rpfj_Type = DisplayString
_Cps6000Rp1Rpfj_Object = MibScalar
cps6000Rp1Rpfj = _Cps6000Rp1Rpfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 13),
    _Cps6000Rp1Rpfj_Type()
)
cps6000Rp1Rpfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rpfj.setStatus("current")
_Cps6000Rp1Rcdp_Type = DisplayString
_Cps6000Rp1Rcdp_Object = MibScalar
cps6000Rp1Rcdp = _Cps6000Rp1Rcdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 30, 14),
    _Cps6000Rp1Rcdp_Type()
)
cps6000Rp1Rcdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Rp1Rcdp.setStatus("current")
_Cps6000RchTable_Object = MibTable
cps6000RchTable = _Cps6000RchTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31)
)
if mibBuilder.loadTexts:
    cps6000RchTable.setStatus("current")
_Cps6000RchEntry_Object = MibTableRow
cps6000RchEntry = _Cps6000RchEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1)
)
cps6000RchEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000RchEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000RchEntry.setStatus("current")


class _Cps6000RchEntryIndex_Type(Integer32):
    """Custom type cps6000RchEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000RchEntryIndex_Type.__name__ = "Integer32"
_Cps6000RchEntryIndex_Object = MibTableColumn
cps6000RchEntryIndex = _Cps6000RchEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 1),
    _Cps6000RchEntryIndex_Type()
)
cps6000RchEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryIndex.setStatus("current")
_Cps6000RchEntryIde_Type = DisplayString
_Cps6000RchEntryIde_Object = MibTableColumn
cps6000RchEntryIde = _Cps6000RchEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 2),
    _Cps6000RchEntryIde_Type()
)
cps6000RchEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryIde.setStatus("current")
_Cps6000RchEntryDes_Type = DisplayString
_Cps6000RchEntryDes_Object = MibTableColumn
cps6000RchEntryDes = _Cps6000RchEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 3),
    _Cps6000RchEntryDes_Type()
)
cps6000RchEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RchEntryDes.setStatus("current")
_Cps6000RchEntryStt_Type = DisplayString
_Cps6000RchEntryStt_Object = MibTableColumn
cps6000RchEntryStt = _Cps6000RchEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 4),
    _Cps6000RchEntryStt_Type()
)
cps6000RchEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000RchEntryStt.setStatus("current")
_Cps6000RchEntryVa_Type = Integer32
_Cps6000RchEntryVa_Object = MibTableColumn
cps6000RchEntryVa = _Cps6000RchEntryVa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 5),
    _Cps6000RchEntryVa_Type()
)
cps6000RchEntryVa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryVa.setStatus("current")
_Cps6000RchEntryPri_Type = DisplayString
_Cps6000RchEntryPri_Object = MibTableColumn
cps6000RchEntryPri = _Cps6000RchEntryPri_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 6),
    _Cps6000RchEntryPri_Type()
)
cps6000RchEntryPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryPri.setStatus("current")
_Cps6000RchEntrySec_Type = DisplayString
_Cps6000RchEntrySec_Object = MibTableColumn
cps6000RchEntrySec = _Cps6000RchEntrySec_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 7),
    _Cps6000RchEntrySec_Type()
)
cps6000RchEntrySec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntrySec.setStatus("current")


class _Cps6000RchEntryRf_Type(Integer32):
    """Custom type cps6000RchEntryRf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRf_Type.__name__ = "Integer32"
_Cps6000RchEntryRf_Object = MibTableColumn
cps6000RchEntryRf = _Cps6000RchEntryRf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 8),
    _Cps6000RchEntryRf_Type()
)
cps6000RchEntryRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRf.setStatus("current")


class _Cps6000RchEntryRpff_Type(Integer32):
    """Custom type cps6000RchEntryRpff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRpff_Type.__name__ = "Integer32"
_Cps6000RchEntryRpff_Object = MibTableColumn
cps6000RchEntryRpff = _Cps6000RchEntryRpff_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 9),
    _Cps6000RchEntryRpff_Type()
)
cps6000RchEntryRpff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRpff.setStatus("current")


class _Cps6000RchEntryRpxj_Type(Integer32):
    """Custom type cps6000RchEntryRpxj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRpxj_Type.__name__ = "Integer32"
_Cps6000RchEntryRpxj_Object = MibTableColumn
cps6000RchEntryRpxj = _Cps6000RchEntryRpxj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 10),
    _Cps6000RchEntryRpxj_Type()
)
cps6000RchEntryRpxj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRpxj.setStatus("current")


class _Cps6000RchEntryRpxn_Type(Integer32):
    """Custom type cps6000RchEntryRpxn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRpxn_Type.__name__ = "Integer32"
_Cps6000RchEntryRpxn_Object = MibTableColumn
cps6000RchEntryRpxn = _Cps6000RchEntryRpxn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 11),
    _Cps6000RchEntryRpxn_Type()
)
cps6000RchEntryRpxn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRpxn.setStatus("current")


class _Cps6000RchEntryRprl_Type(Integer32):
    """Custom type cps6000RchEntryRprl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRprl_Type.__name__ = "Integer32"
_Cps6000RchEntryRprl_Object = MibTableColumn
cps6000RchEntryRprl = _Cps6000RchEntryRprl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 12),
    _Cps6000RchEntryRprl_Type()
)
cps6000RchEntryRprl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRprl.setStatus("current")


class _Cps6000RchEntryRpfj_Type(Integer32):
    """Custom type cps6000RchEntryRpfj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRpfj_Type.__name__ = "Integer32"
_Cps6000RchEntryRpfj_Object = MibTableColumn
cps6000RchEntryRpfj = _Cps6000RchEntryRpfj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 13),
    _Cps6000RchEntryRpfj_Type()
)
cps6000RchEntryRpfj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRpfj.setStatus("current")


class _Cps6000RchEntryRcdp_Type(Integer32):
    """Custom type cps6000RchEntryRcdp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000RchEntryRcdp_Type.__name__ = "Integer32"
_Cps6000RchEntryRcdp_Object = MibTableColumn
cps6000RchEntryRcdp = _Cps6000RchEntryRcdp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 31, 1, 14),
    _Cps6000RchEntryRcdp_Type()
)
cps6000RchEntryRcdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000RchEntryRcdp.setStatus("current")
_Cps6000AlarmTable_Object = MibTable
cps6000AlarmTable = _Cps6000AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32)
)
if mibBuilder.loadTexts:
    cps6000AlarmTable.setStatus("current")
_Cps6000AlarmEntry_Object = MibTableRow
cps6000AlarmEntry = _Cps6000AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1)
)
cps6000AlarmEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000AlarmEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000AlarmEntry.setStatus("current")


class _Cps6000AlarmEntryIndex_Type(Integer32):
    """Custom type cps6000AlarmEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000AlarmEntryIndex_Type.__name__ = "Integer32"
_Cps6000AlarmEntryIndex_Object = MibTableColumn
cps6000AlarmEntryIndex = _Cps6000AlarmEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 1),
    _Cps6000AlarmEntryIndex_Type()
)
cps6000AlarmEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000AlarmEntryIndex.setStatus("current")
_Cps6000AlarmEntryDes_Type = DisplayString
_Cps6000AlarmEntryDes_Object = MibTableColumn
cps6000AlarmEntryDes = _Cps6000AlarmEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 2),
    _Cps6000AlarmEntryDes_Type()
)
cps6000AlarmEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryDes.setStatus("current")


class _Cps6000AlarmEntryAst_Type(Integer32):
    """Custom type cps6000AlarmEntryAst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000AlarmEntryAst_Type.__name__ = "Integer32"
_Cps6000AlarmEntryAst_Object = MibTableColumn
cps6000AlarmEntryAst = _Cps6000AlarmEntryAst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 3),
    _Cps6000AlarmEntryAst_Type()
)
cps6000AlarmEntryAst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000AlarmEntryAst.setStatus("current")
_Cps6000AlarmEntrySev_Type = DisplayString
_Cps6000AlarmEntrySev_Object = MibTableColumn
cps6000AlarmEntrySev = _Cps6000AlarmEntrySev_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 4),
    _Cps6000AlarmEntrySev_Type()
)
cps6000AlarmEntrySev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntrySev.setStatus("current")
_Cps6000AlarmEntryAcc_Type = DisplayString
_Cps6000AlarmEntryAcc_Object = MibTableColumn
cps6000AlarmEntryAcc = _Cps6000AlarmEntryAcc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 5),
    _Cps6000AlarmEntryAcc_Type()
)
cps6000AlarmEntryAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryAcc.setStatus("current")
_Cps6000AlarmEntryThr_Type = DisplayString
_Cps6000AlarmEntryThr_Object = MibTableColumn
cps6000AlarmEntryThr = _Cps6000AlarmEntryThr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 6),
    _Cps6000AlarmEntryThr_Type()
)
cps6000AlarmEntryThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryThr.setStatus("current")
_Cps6000AlarmEntryFth_Type = DisplayString
_Cps6000AlarmEntryFth_Object = MibTableColumn
cps6000AlarmEntryFth = _Cps6000AlarmEntryFth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 7),
    _Cps6000AlarmEntryFth_Type()
)
cps6000AlarmEntryFth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryFth.setStatus("current")
_Cps6000AlarmEntryBth_Type = DisplayString
_Cps6000AlarmEntryBth_Object = MibTableColumn
cps6000AlarmEntryBth = _Cps6000AlarmEntryBth_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 8),
    _Cps6000AlarmEntryBth_Type()
)
cps6000AlarmEntryBth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryBth.setStatus("current")


class _Cps6000AlarmEntryDly_Type(Integer32):
    """Custom type cps6000AlarmEntryDly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 540),
    )


_Cps6000AlarmEntryDly_Type.__name__ = "Integer32"
_Cps6000AlarmEntryDly_Object = MibTableColumn
cps6000AlarmEntryDly = _Cps6000AlarmEntryDly_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 9),
    _Cps6000AlarmEntryDly_Type()
)
cps6000AlarmEntryDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryDly.setStatus("current")


class _Cps6000AlarmEntryNoo_Type(Integer32):
    """Custom type cps6000AlarmEntryNoo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000AlarmEntryNoo_Type.__name__ = "Integer32"
_Cps6000AlarmEntryNoo_Object = MibTableColumn
cps6000AlarmEntryNoo = _Cps6000AlarmEntryNoo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 10),
    _Cps6000AlarmEntryNoo_Type()
)
cps6000AlarmEntryNoo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryNoo.setStatus("current")


class _Cps6000AlarmEntryNor_Type(Integer32):
    """Custom type cps6000AlarmEntryNor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000AlarmEntryNor_Type.__name__ = "Integer32"
_Cps6000AlarmEntryNor_Object = MibTableColumn
cps6000AlarmEntryNor = _Cps6000AlarmEntryNor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 11),
    _Cps6000AlarmEntryNor_Type()
)
cps6000AlarmEntryNor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryNor.setStatus("current")


class _Cps6000AlarmEntryNag_Type(Integer32):
    """Custom type cps6000AlarmEntryNag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Cps6000AlarmEntryNag_Type.__name__ = "Integer32"
_Cps6000AlarmEntryNag_Object = MibTableColumn
cps6000AlarmEntryNag = _Cps6000AlarmEntryNag_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 12),
    _Cps6000AlarmEntryNag_Type()
)
cps6000AlarmEntryNag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryNag.setStatus("current")
_Cps6000AlarmEntryDst_Type = DisplayString
_Cps6000AlarmEntryDst_Object = MibTableColumn
cps6000AlarmEntryDst = _Cps6000AlarmEntryDst_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 13),
    _Cps6000AlarmEntryDst_Type()
)
cps6000AlarmEntryDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryDst.setStatus("current")
_Cps6000AlarmEntryFds_Type = DisplayString
_Cps6000AlarmEntryFds_Object = MibTableColumn
cps6000AlarmEntryFds = _Cps6000AlarmEntryFds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 32, 1, 14),
    _Cps6000AlarmEntryFds_Type()
)
cps6000AlarmEntryFds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000AlarmEntryFds.setStatus("current")
_Cps6000Trap_ObjectIdentity = ObjectIdentity
cps6000Trap = _Cps6000Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33)
)
_TrapInfo_Type = DisplayString
_TrapInfo_Object = MibScalar
trapInfo = _TrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 34),
    _TrapInfo_Type()
)
trapInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapInfo.setStatus("current")
_Cps6000Retire_ObjectIdentity = ObjectIdentity
cps6000Retire = _Cps6000Retire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35)
)
_Cps6000MsvTable_Object = MibTable
cps6000MsvTable = _Cps6000MsvTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36)
)
if mibBuilder.loadTexts:
    cps6000MsvTable.setStatus("current")
_Cps6000MsvEntry_Object = MibTableRow
cps6000MsvEntry = _Cps6000MsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1)
)
cps6000MsvEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000MsvEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000MsvEntry.setStatus("current")


class _Cps6000MsvEntryIndex_Type(Integer32):
    """Custom type cps6000MsvEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000MsvEntryIndex_Type.__name__ = "Integer32"
_Cps6000MsvEntryIndex_Object = MibTableColumn
cps6000MsvEntryIndex = _Cps6000MsvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 1),
    _Cps6000MsvEntryIndex_Type()
)
cps6000MsvEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000MsvEntryIndex.setStatus("current")
_Cps6000MsvEntryIde_Type = DisplayString
_Cps6000MsvEntryIde_Object = MibTableColumn
cps6000MsvEntryIde = _Cps6000MsvEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 2),
    _Cps6000MsvEntryIde_Type()
)
cps6000MsvEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000MsvEntryIde.setStatus("current")
_Cps6000MsvEntryDes_Type = DisplayString
_Cps6000MsvEntryDes_Object = MibTableColumn
cps6000MsvEntryDes = _Cps6000MsvEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 3),
    _Cps6000MsvEntryDes_Type()
)
cps6000MsvEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000MsvEntryDes.setStatus("current")
_Cps6000MsvEntryStt_Type = DisplayString
_Cps6000MsvEntryStt_Object = MibTableColumn
cps6000MsvEntryStt = _Cps6000MsvEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 4),
    _Cps6000MsvEntryStt_Type()
)
cps6000MsvEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000MsvEntryStt.setStatus("current")
_Cps6000MsvEntryVal_Type = DisplayString
_Cps6000MsvEntryVal_Object = MibTableColumn
cps6000MsvEntryVal = _Cps6000MsvEntryVal_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 5),
    _Cps6000MsvEntryVal_Type()
)
cps6000MsvEntryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000MsvEntryVal.setStatus("current")
if mibBuilder.loadTexts:
    cps6000MsvEntryVal.setUnits("Volts")
_Cps6000MsvEntryDid_Type = DisplayString
_Cps6000MsvEntryDid_Object = MibTableColumn
cps6000MsvEntryDid = _Cps6000MsvEntryDid_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 36, 1, 6),
    _Cps6000MsvEntryDid_Type()
)
cps6000MsvEntryDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000MsvEntryDid.setStatus("current")
_Cps6000Ft1_ObjectIdentity = ObjectIdentity
cps6000Ft1 = _Cps6000Ft1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37)
)
_Cps6000Ft1Ide_Type = DisplayString
_Cps6000Ft1Ide_Object = MibScalar
cps6000Ft1Ide = _Cps6000Ft1Ide_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 1),
    _Cps6000Ft1Ide_Type()
)
cps6000Ft1Ide.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Ide.setStatus("current")
_Cps6000Ft1Des_Type = DisplayString
_Cps6000Ft1Des_Object = MibScalar
cps6000Ft1Des = _Cps6000Ft1Des_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 2),
    _Cps6000Ft1Des_Type()
)
cps6000Ft1Des.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Des.setStatus("current")
_Cps6000Ft1Stt_Type = DisplayString
_Cps6000Ft1Stt_Object = MibScalar
cps6000Ft1Stt = _Cps6000Ft1Stt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 3),
    _Cps6000Ft1Stt_Type()
)
cps6000Ft1Stt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Stt.setStatus("current")
_Cps6000Ft1Iadc_Type = DisplayString
_Cps6000Ft1Iadc_Object = MibScalar
cps6000Ft1Iadc = _Cps6000Ft1Iadc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 4),
    _Cps6000Ft1Iadc_Type()
)
cps6000Ft1Iadc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Iadc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Ft1Iadc.setUnits("Amps")


class _Cps6000Ft1Lte_Type(Integer32):
    """Custom type cps6000Ft1Lte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ft1Lte_Type.__name__ = "Integer32"
_Cps6000Ft1Lte_Object = MibScalar
cps6000Ft1Lte = _Cps6000Ft1Lte_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 5),
    _Cps6000Ft1Lte_Type()
)
cps6000Ft1Lte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Lte.setStatus("current")
_Cps6000Ft1Ltf_Type = DisplayString
_Cps6000Ft1Ltf_Object = MibScalar
cps6000Ft1Ltf = _Cps6000Ft1Ltf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 6),
    _Cps6000Ft1Ltf_Type()
)
cps6000Ft1Ltf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Ltf.setStatus("current")
if mibBuilder.loadTexts:
    cps6000Ft1Ltf.setUnits("Days")
_Cps6000Ft1Fmi_Type = DisplayString
_Cps6000Ft1Fmi_Object = MibScalar
cps6000Ft1Fmi = _Cps6000Ft1Fmi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 7),
    _Cps6000Ft1Fmi_Type()
)
cps6000Ft1Fmi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Fmi.setStatus("current")
_Cps6000Ft1Fmj_Type = DisplayString
_Cps6000Ft1Fmj_Object = MibScalar
cps6000Ft1Fmj = _Cps6000Ft1Fmj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 8),
    _Cps6000Ft1Fmj_Type()
)
cps6000Ft1Fmj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Fmj.setStatus("current")
_Cps6000Ft1Ipi_Type = DisplayString
_Cps6000Ft1Ipi_Object = MibScalar
cps6000Ft1Ipi = _Cps6000Ft1Ipi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 9),
    _Cps6000Ft1Ipi_Type()
)
cps6000Ft1Ipi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Ipi.setStatus("current")
_Cps6000Ft1Ipj_Type = DisplayString
_Cps6000Ft1Ipj_Object = MibScalar
cps6000Ft1Ipj = _Cps6000Ft1Ipj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 10),
    _Cps6000Ft1Ipj_Type()
)
cps6000Ft1Ipj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Ipj.setStatus("current")
_Cps6000Ft1Cbt_Type = DisplayString
_Cps6000Ft1Cbt_Object = MibScalar
cps6000Ft1Cbt = _Cps6000Ft1Cbt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 11),
    _Cps6000Ft1Cbt_Type()
)
cps6000Ft1Cbt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Cbt.setStatus("current")
_Cps6000Ft1Ctf_Type = DisplayString
_Cps6000Ft1Ctf_Object = MibScalar
cps6000Ft1Ctf = _Cps6000Ft1Ctf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 12),
    _Cps6000Ft1Ctf_Type()
)
cps6000Ft1Ctf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Ctf.setStatus("current")
_Cps6000Ft1Mctf_Type = DisplayString
_Cps6000Ft1Mctf_Object = MibScalar
cps6000Ft1Mctf = _Cps6000Ft1Mctf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 13),
    _Cps6000Ft1Mctf_Type()
)
cps6000Ft1Mctf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Mctf.setStatus("current")
_Cps6000Ft1Lor_Type = DisplayString
_Cps6000Ft1Lor_Object = MibScalar
cps6000Ft1Lor = _Cps6000Ft1Lor_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 14),
    _Cps6000Ft1Lor_Type()
)
cps6000Ft1Lor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Lor.setStatus("current")
_Cps6000Ft1Lda_Type = DisplayString
_Cps6000Ft1Lda_Object = MibScalar
cps6000Ft1Lda = _Cps6000Ft1Lda_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 15),
    _Cps6000Ft1Lda_Type()
)
cps6000Ft1Lda.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Lda.setStatus("current")
_Cps6000Ft1Lsa_Type = DisplayString
_Cps6000Ft1Lsa_Object = MibScalar
cps6000Ft1Lsa = _Cps6000Ft1Lsa_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 16),
    _Cps6000Ft1Lsa_Type()
)
cps6000Ft1Lsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Lsa.setStatus("current")
_Cps6000Ft1Lta_Type = DisplayString
_Cps6000Ft1Lta_Object = MibScalar
cps6000Ft1Lta = _Cps6000Ft1Lta_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 17),
    _Cps6000Ft1Lta_Type()
)
cps6000Ft1Lta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000Ft1Lta.setStatus("current")


class _Cps6000Ft1Rem_Type(Integer32):
    """Custom type cps6000Ft1Rem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Cps6000Ft1Rem_Type.__name__ = "Integer32"
_Cps6000Ft1Rem_Object = MibScalar
cps6000Ft1Rem = _Cps6000Ft1Rem_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 18),
    _Cps6000Ft1Rem_Type()
)
cps6000Ft1Rem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ft1Rem.setStatus("current")


class _Cps6000Ft1Tof_Type(Integer32):
    """Custom type cps6000Ft1Tof based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("faulted", 1),
          ("faultedAndNoLoad", 2))
    )


_Cps6000Ft1Tof_Type.__name__ = "Integer32"
_Cps6000Ft1Tof_Object = MibScalar
cps6000Ft1Tof = _Cps6000Ft1Tof_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 37, 19),
    _Cps6000Ft1Tof_Type()
)
cps6000Ft1Tof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000Ft1Tof.setStatus("current")
_Cps6000GrpTable_Object = MibTable
cps6000GrpTable = _Cps6000GrpTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38)
)
if mibBuilder.loadTexts:
    cps6000GrpTable.setStatus("current")
_Cps6000GrpEntry_Object = MibTableRow
cps6000GrpEntry = _Cps6000GrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1)
)
cps6000GrpEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000GrpEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000GrpEntry.setStatus("current")


class _Cps6000GrpEntryIndex_Type(Integer32):
    """Custom type cps6000GrpEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000GrpEntryIndex_Type.__name__ = "Integer32"
_Cps6000GrpEntryIndex_Object = MibTableColumn
cps6000GrpEntryIndex = _Cps6000GrpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 1),
    _Cps6000GrpEntryIndex_Type()
)
cps6000GrpEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryIndex.setStatus("current")
_Cps6000GrpEntryIde_Type = DisplayString
_Cps6000GrpEntryIde_Object = MibTableColumn
cps6000GrpEntryIde = _Cps6000GrpEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 2),
    _Cps6000GrpEntryIde_Type()
)
cps6000GrpEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryIde.setStatus("current")
_Cps6000GrpEntryDes_Type = DisplayString
_Cps6000GrpEntryDes_Object = MibTableColumn
cps6000GrpEntryDes = _Cps6000GrpEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 3),
    _Cps6000GrpEntryDes_Type()
)
cps6000GrpEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000GrpEntryDes.setStatus("current")
_Cps6000GrpEntryCct_Type = DisplayString
_Cps6000GrpEntryCct_Object = MibTableColumn
cps6000GrpEntryCct = _Cps6000GrpEntryCct_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 4),
    _Cps6000GrpEntryCct_Type()
)
cps6000GrpEntryCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryCct.setStatus("current")
_Cps6000GrpEntryTadc_Type = DisplayString
_Cps6000GrpEntryTadc_Object = MibTableColumn
cps6000GrpEntryTadc = _Cps6000GrpEntryTadc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 5),
    _Cps6000GrpEntryTadc_Type()
)
cps6000GrpEntryTadc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryTadc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000GrpEntryTadc.setUnits("mA")
_Cps6000GrpEntryAadc_Type = DisplayString
_Cps6000GrpEntryAadc_Object = MibTableColumn
cps6000GrpEntryAadc = _Cps6000GrpEntryAadc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 6),
    _Cps6000GrpEntryAadc_Type()
)
cps6000GrpEntryAadc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryAadc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000GrpEntryAadc.setUnits("mA")
_Cps6000GrpEntryCap_Type = DisplayString
_Cps6000GrpEntryCap_Object = MibTableColumn
cps6000GrpEntryCap = _Cps6000GrpEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 7),
    _Cps6000GrpEntryCap_Type()
)
cps6000GrpEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000GrpEntryCap.setUnits("mA")
_Cps6000GrpEntryLrs_Type = DisplayString
_Cps6000GrpEntryLrs_Object = MibTableColumn
cps6000GrpEntryLrs = _Cps6000GrpEntryLrs_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 8),
    _Cps6000GrpEntryLrs_Type()
)
cps6000GrpEntryLrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryLrs.setStatus("current")
_Cps6000GrpEntryOlcap_Type = DisplayString
_Cps6000GrpEntryOlcap_Object = MibTableColumn
cps6000GrpEntryOlcap = _Cps6000GrpEntryOlcap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 38, 1, 9),
    _Cps6000GrpEntryOlcap_Type()
)
cps6000GrpEntryOlcap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000GrpEntryOlcap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000GrpEntryOlcap.setUnits("mA")
_Cps6000ShfTable_Object = MibTable
cps6000ShfTable = _Cps6000ShfTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39)
)
if mibBuilder.loadTexts:
    cps6000ShfTable.setStatus("current")
_Cps6000ShfEntry_Object = MibTableRow
cps6000ShfEntry = _Cps6000ShfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1)
)
cps6000ShfEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000ShfEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000ShfEntry.setStatus("current")


class _Cps6000ShfEntryIndex_Type(Integer32):
    """Custom type cps6000ShfEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000ShfEntryIndex_Type.__name__ = "Integer32"
_Cps6000ShfEntryIndex_Object = MibTableColumn
cps6000ShfEntryIndex = _Cps6000ShfEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 1),
    _Cps6000ShfEntryIndex_Type()
)
cps6000ShfEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIndex.setStatus("current")
_Cps6000ShfEntryIde_Type = DisplayString
_Cps6000ShfEntryIde_Object = MibTableColumn
cps6000ShfEntryIde = _Cps6000ShfEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 2),
    _Cps6000ShfEntryIde_Type()
)
cps6000ShfEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIde.setStatus("current")
_Cps6000ShfEntryDes_Type = DisplayString
_Cps6000ShfEntryDes_Object = MibTableColumn
cps6000ShfEntryDes = _Cps6000ShfEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 3),
    _Cps6000ShfEntryDes_Type()
)
cps6000ShfEntryDes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryDes.setStatus("current")
_Cps6000ShfEntryStt_Type = DisplayString
_Cps6000ShfEntryStt_Object = MibTableColumn
cps6000ShfEntryStt = _Cps6000ShfEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 4),
    _Cps6000ShfEntryStt_Type()
)
cps6000ShfEntryStt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryStt.setStatus("current")
_Cps6000ShfEntryIadc_Type = DisplayString
_Cps6000ShfEntryIadc_Object = MibTableColumn
cps6000ShfEntryIadc = _Cps6000ShfEntryIadc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 5),
    _Cps6000ShfEntryIadc_Type()
)
cps6000ShfEntryIadc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIadc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000ShfEntryIadc.setUnits("Amps")


class _Cps6000ShfEntryIa1_Type(Integer32):
    """Custom type cps6000ShfEntryIa1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryIa1_Type.__name__ = "Integer32"
_Cps6000ShfEntryIa1_Object = MibTableColumn
cps6000ShfEntryIa1 = _Cps6000ShfEntryIa1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 6),
    _Cps6000ShfEntryIa1_Type()
)
cps6000ShfEntryIa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIa1.setStatus("current")


class _Cps6000ShfEntryIa2_Type(Integer32):
    """Custom type cps6000ShfEntryIa2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryIa2_Type.__name__ = "Integer32"
_Cps6000ShfEntryIa2_Object = MibTableColumn
cps6000ShfEntryIa2 = _Cps6000ShfEntryIa2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 7),
    _Cps6000ShfEntryIa2_Type()
)
cps6000ShfEntryIa2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIa2.setStatus("current")


class _Cps6000ShfEntryIb1_Type(Integer32):
    """Custom type cps6000ShfEntryIb1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryIb1_Type.__name__ = "Integer32"
_Cps6000ShfEntryIb1_Object = MibTableColumn
cps6000ShfEntryIb1 = _Cps6000ShfEntryIb1_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 8),
    _Cps6000ShfEntryIb1_Type()
)
cps6000ShfEntryIb1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIb1.setStatus("current")


class _Cps6000ShfEntryIb2_Type(Integer32):
    """Custom type cps6000ShfEntryIb2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryIb2_Type.__name__ = "Integer32"
_Cps6000ShfEntryIb2_Object = MibTableColumn
cps6000ShfEntryIb2 = _Cps6000ShfEntryIb2_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 9),
    _Cps6000ShfEntryIb2_Type()
)
cps6000ShfEntryIb2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryIb2.setStatus("current")


class _Cps6000ShfEntryUfn_Type(Integer32):
    """Custom type cps6000ShfEntryUfn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryUfn_Type.__name__ = "Integer32"
_Cps6000ShfEntryUfn_Object = MibTableColumn
cps6000ShfEntryUfn = _Cps6000ShfEntryUfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 10),
    _Cps6000ShfEntryUfn_Type()
)
cps6000ShfEntryUfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryUfn.setStatus("current")


class _Cps6000ShfEntryLfn_Type(Integer32):
    """Custom type cps6000ShfEntryLfn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryLfn_Type.__name__ = "Integer32"
_Cps6000ShfEntryLfn_Object = MibTableColumn
cps6000ShfEntryLfn = _Cps6000ShfEntryLfn_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 11),
    _Cps6000ShfEntryLfn_Type()
)
cps6000ShfEntryLfn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryLfn.setStatus("current")


class _Cps6000ShfEntryCba_Type(Integer32):
    """Custom type cps6000ShfEntryCba based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryCba_Type.__name__ = "Integer32"
_Cps6000ShfEntryCba_Object = MibTableColumn
cps6000ShfEntryCba = _Cps6000ShfEntryCba_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 12),
    _Cps6000ShfEntryCba_Type()
)
cps6000ShfEntryCba.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryCba.setStatus("current")


class _Cps6000ShfEntryCbb_Type(Integer32):
    """Custom type cps6000ShfEntryCbb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryCbb_Type.__name__ = "Integer32"
_Cps6000ShfEntryCbb_Object = MibTableColumn
cps6000ShfEntryCbb = _Cps6000ShfEntryCbb_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 13),
    _Cps6000ShfEntryCbb_Type()
)
cps6000ShfEntryCbb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryCbb.setStatus("current")


class _Cps6000ShfEntryCvj_Type(Integer32):
    """Custom type cps6000ShfEntryCvj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryCvj_Type.__name__ = "Integer32"
_Cps6000ShfEntryCvj_Object = MibTableColumn
cps6000ShfEntryCvj = _Cps6000ShfEntryCvj_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 14),
    _Cps6000ShfEntryCvj_Type()
)
cps6000ShfEntryCvj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryCvj.setStatus("current")


class _Cps6000ShfEntryCvi_Type(Integer32):
    """Custom type cps6000ShfEntryCvi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000ShfEntryCvi_Type.__name__ = "Integer32"
_Cps6000ShfEntryCvi_Object = MibTableColumn
cps6000ShfEntryCvi = _Cps6000ShfEntryCvi_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 15),
    _Cps6000ShfEntryCvi_Type()
)
cps6000ShfEntryCvi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryCvi.setStatus("current")
_Cps6000ShfEntryNoc_Type = Integer32
_Cps6000ShfEntryNoc_Object = MibTableColumn
cps6000ShfEntryNoc = _Cps6000ShfEntryNoc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 39, 1, 16),
    _Cps6000ShfEntryNoc_Type()
)
cps6000ShfEntryNoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000ShfEntryNoc.setStatus("current")
_Cps6000CctTable_Object = MibTable
cps6000CctTable = _Cps6000CctTable_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40)
)
if mibBuilder.loadTexts:
    cps6000CctTable.setStatus("current")
_Cps6000CctEntry_Object = MibTableRow
cps6000CctEntry = _Cps6000CctEntry_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1)
)
cps6000CctEntry.setIndexNames(
    (0, "CPS6000-MIB", "cps6000CctEntryIndex"),
)
if mibBuilder.loadTexts:
    cps6000CctEntry.setStatus("current")


class _Cps6000CctEntryIndex_Type(Integer32):
    """Custom type cps6000CctEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Cps6000CctEntryIndex_Type.__name__ = "Integer32"
_Cps6000CctEntryIndex_Object = MibTableColumn
cps6000CctEntryIndex = _Cps6000CctEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 1),
    _Cps6000CctEntryIndex_Type()
)
cps6000CctEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryIndex.setStatus("current")
_Cps6000CctEntryIde_Type = DisplayString
_Cps6000CctEntryIde_Object = MibTableColumn
cps6000CctEntryIde = _Cps6000CctEntryIde_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 2),
    _Cps6000CctEntryIde_Type()
)
cps6000CctEntryIde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryIde.setStatus("current")
_Cps6000CctEntryDes_Type = DisplayString
_Cps6000CctEntryDes_Object = MibTableColumn
cps6000CctEntryDes = _Cps6000CctEntryDes_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 3),
    _Cps6000CctEntryDes_Type()
)
cps6000CctEntryDes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CctEntryDes.setStatus("current")
_Cps6000CctEntryVdc_Type = DisplayString
_Cps6000CctEntryVdc_Object = MibTableColumn
cps6000CctEntryVdc = _Cps6000CctEntryVdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 4),
    _Cps6000CctEntryVdc_Type()
)
cps6000CctEntryVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryVdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryVdc.setUnits("Volts")
_Cps6000CctEntryAdc_Type = DisplayString
_Cps6000CctEntryAdc_Object = MibTableColumn
cps6000CctEntryAdc = _Cps6000CctEntryAdc_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 5),
    _Cps6000CctEntryAdc_Type()
)
cps6000CctEntryAdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryAdc.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryAdc.setUnits("mA")
_Cps6000CctEntryStt_Type = DisplayString
_Cps6000CctEntryStt_Object = MibTableColumn
cps6000CctEntryStt = _Cps6000CctEntryStt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 6),
    _Cps6000CctEntryStt_Type()
)
cps6000CctEntryStt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cps6000CctEntryStt.setStatus("current")
_Cps6000CctEntryTmp_Type = DisplayString
_Cps6000CctEntryTmp_Object = MibTableColumn
cps6000CctEntryTmp = _Cps6000CctEntryTmp_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 7),
    _Cps6000CctEntryTmp_Type()
)
cps6000CctEntryTmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryTmp.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryTmp.setUnits("C")
_Cps6000CctEntryCap_Type = DisplayString
_Cps6000CctEntryCap_Object = MibTableColumn
cps6000CctEntryCap = _Cps6000CctEntryCap_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 8),
    _Cps6000CctEntryCap_Type()
)
cps6000CctEntryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryCap.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryCap.setUnits("mA")
_Cps6000CctEntryCli_Type = DisplayString
_Cps6000CctEntryCli_Object = MibTableColumn
cps6000CctEntryCli = _Cps6000CctEntryCli_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 9),
    _Cps6000CctEntryCli_Type()
)
cps6000CctEntryCli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryCli.setStatus("current")
_Cps6000CctEntrySnm_Type = DisplayString
_Cps6000CctEntrySnm_Object = MibTableColumn
cps6000CctEntrySnm = _Cps6000CctEntrySnm_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 10),
    _Cps6000CctEntrySnm_Type()
)
cps6000CctEntrySnm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntrySnm.setStatus("current")
_Cps6000CctEntryMdl_Type = DisplayString
_Cps6000CctEntryMdl_Object = MibTableColumn
cps6000CctEntryMdl = _Cps6000CctEntryMdl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 11),
    _Cps6000CctEntryMdl_Type()
)
cps6000CctEntryMdl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryMdl.setStatus("current")
_Cps6000CctEntryCcd_Type = DisplayString
_Cps6000CctEntryCcd_Object = MibTableColumn
cps6000CctEntryCcd = _Cps6000CctEntryCcd_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 12),
    _Cps6000CctEntryCcd_Type()
)
cps6000CctEntryCcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryCcd.setStatus("current")


class _Cps6000CctEntryCfl_Type(Integer32):
    """Custom type cps6000CctEntryCfl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryCfl_Type.__name__ = "Integer32"
_Cps6000CctEntryCfl_Object = MibTableColumn
cps6000CctEntryCfl = _Cps6000CctEntryCfl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 13),
    _Cps6000CctEntryCfl_Type()
)
cps6000CctEntryCfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryCfl.setStatus("current")


class _Cps6000CctEntryOv_Type(Integer32):
    """Custom type cps6000CctEntryOv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryOv_Type.__name__ = "Integer32"
_Cps6000CctEntryOv_Object = MibTableColumn
cps6000CctEntryOv = _Cps6000CctEntryOv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 14),
    _Cps6000CctEntryOv_Type()
)
cps6000CctEntryOv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryOv.setStatus("current")


class _Cps6000CctEntryCl_Type(Integer32):
    """Custom type cps6000CctEntryCl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryCl_Type.__name__ = "Integer32"
_Cps6000CctEntryCl_Object = MibTableColumn
cps6000CctEntryCl = _Cps6000CctEntryCl_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 15),
    _Cps6000CctEntryCl_Type()
)
cps6000CctEntryCl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryCl.setStatus("current")


class _Cps6000CctEntryGf_Type(Integer32):
    """Custom type cps6000CctEntryGf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryGf_Type.__name__ = "Integer32"
_Cps6000CctEntryGf_Object = MibTableColumn
cps6000CctEntryGf = _Cps6000CctEntryGf_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 16),
    _Cps6000CctEntryGf_Type()
)
cps6000CctEntryGf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryGf.setStatus("current")


class _Cps6000CctEntryUv_Type(Integer32):
    """Custom type cps6000CctEntryUv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryUv_Type.__name__ = "Integer32"
_Cps6000CctEntryUv_Object = MibTableColumn
cps6000CctEntryUv = _Cps6000CctEntryUv_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 17),
    _Cps6000CctEntryUv_Type()
)
cps6000CctEntryUv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryUv.setStatus("current")


class _Cps6000CctEntryOt_Type(Integer32):
    """Custom type cps6000CctEntryOt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryOt_Type.__name__ = "Integer32"
_Cps6000CctEntryOt_Object = MibTableColumn
cps6000CctEntryOt = _Cps6000CctEntryOt_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 18),
    _Cps6000CctEntryOt_Type()
)
cps6000CctEntryOt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryOt.setStatus("current")


class _Cps6000CctEntryLds_Type(Integer32):
    """Custom type cps6000CctEntryLds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryLds_Type.__name__ = "Integer32"
_Cps6000CctEntryLds_Object = MibTableColumn
cps6000CctEntryLds = _Cps6000CctEntryLds_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 19),
    _Cps6000CctEntryLds_Type()
)
cps6000CctEntryLds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryLds.setStatus("current")


class _Cps6000CctEntryLss_Type(Integer32):
    """Custom type cps6000CctEntryLss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryLss_Type.__name__ = "Integer32"
_Cps6000CctEntryLss_Object = MibTableColumn
cps6000CctEntryLss = _Cps6000CctEntryLss_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 20),
    _Cps6000CctEntryLss_Type()
)
cps6000CctEntryLss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryLss.setStatus("current")


class _Cps6000CctEntryLts_Type(Integer32):
    """Custom type cps6000CctEntryLts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_Cps6000CctEntryLts_Type.__name__ = "Integer32"
_Cps6000CctEntryLts_Object = MibTableColumn
cps6000CctEntryLts = _Cps6000CctEntryLts_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 21),
    _Cps6000CctEntryLts_Type()
)
cps6000CctEntryLts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryLts.setStatus("current")
_Cps6000CctEntryIlr_Type = DisplayString
_Cps6000CctEntryIlr_Object = MibTableColumn
cps6000CctEntryIlr = _Cps6000CctEntryIlr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 22),
    _Cps6000CctEntryIlr_Type()
)
cps6000CctEntryIlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryIlr.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryIlr.setUnits("Ohms")
_Cps6000CctEntryAlr_Type = DisplayString
_Cps6000CctEntryAlr_Object = MibTableColumn
cps6000CctEntryAlr = _Cps6000CctEntryAlr_Object(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 40, 1, 23),
    _Cps6000CctEntryAlr_Type()
)
cps6000CctEntryAlr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cps6000CctEntryAlr.setStatus("current")
if mibBuilder.loadTexts:
    cps6000CctEntryAlr.setUnits("Ohms")
_Prototypes_ObjectIdentity = ObjectIdentity
prototypes = _Prototypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10520, 2, 2)
)

# Managed Objects groups


# Notification objects

cps6000TrapDc1Amj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 1)
)
cps6000TrapDc1Amj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Amj.setStatus(
        "current"
    )

cps6000TrapDc1Epo = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 2)
)
cps6000TrapDc1Epo.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Epo.setStatus(
        "current"
    )

cps6000TrapDc1Faj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 3)
)
cps6000TrapDc1Faj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Faj.setStatus(
        "current"
    )

cps6000TrapDc1Fan = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 4)
)
cps6000TrapDc1Fan.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Fan.setStatus(
        "current"
    )

cps6000TrapDc1Vsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 5)
)
cps6000TrapDc1Vsf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Vsf.setStatus(
        "current"
    )

cps6000TrapDc1Osa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 6)
)
cps6000TrapDc1Osa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Osa.setStatus(
        "current"
    )

cps6000TrapDc1Zid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 7)
)
cps6000TrapDc1Zid.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Zid.setStatus(
        "current"
    )

cps6000TrapDc1Tpa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 8)
)
cps6000TrapDc1Tpa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Tpa.setStatus(
        "current"
    )

cps6000TrapDc1Vmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 9)
)
cps6000TrapDc1Vmf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Vmf.setStatus(
        "current"
    )

cps6000TrapDc1Cma = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 10)
)
cps6000TrapDc1Cma.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Cma.setStatus(
        "current"
    )

cps6000TrapDc1Macf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 11)
)
cps6000TrapDc1Macf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Macf.setStatus(
        "current"
    )

cps6000TrapDc1Mcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 12)
)
cps6000TrapDc1Mcm.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Mcm.setStatus(
        "current"
    )

cps6000TrapDc1Rfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 13)
)
cps6000TrapDc1Rfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Rfa.setStatus(
        "current"
    )

cps6000TrapDc1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 14)
)
cps6000TrapDc1Did.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Did.setStatus(
        "current"
    )

cps6000TrapDc1Clm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 15)
)
cps6000TrapDc1Clm.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Clm.setStatus(
        "current"
    )

cps6000TrapDc1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 16)
)
cps6000TrapDc1Vla.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Vla.setStatus(
        "current"
    )

cps6000TrapDc1Acf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 17)
)
cps6000TrapDc1Acf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Acf.setStatus(
        "current"
    )

cps6000TrapDc1Man = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 18)
)
cps6000TrapDc1Man.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Man.setStatus(
        "current"
    )

cps6000TrapDc1Mman = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 19)
)
cps6000TrapDc1Mman.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Mman.setStatus(
        "current"
    )

cps6000TrapDc1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 20)
)
cps6000TrapDc1Mfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Mfa.setStatus(
        "current"
    )

cps6000TrapDc1Rtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 21)
)
cps6000TrapDc1Rtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Rtl.setStatus(
        "current"
    )

cps6000TrapDc1Rrtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 22)
)
cps6000TrapDc1Rrtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Rrtl.setStatus(
        "current"
    )

cps6000TrapDc1Rls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 23)
)
cps6000TrapDc1Rls.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Rls.setStatus(
        "current"
    )

cps6000TrapDc1Bda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 24)
)
cps6000TrapDc1Bda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Bda.setStatus(
        "current"
    )

cps6000TrapDc1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 25)
)
cps6000TrapDc1Hva.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Hva.setStatus(
        "current"
    )

cps6000TrapDc1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 26)
)
cps6000TrapDc1Hfv.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Hfv.setStatus(
        "current"
    )

cps6000TrapPs1Amth = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 27)
)
cps6000TrapPs1Amth.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Amth.setStatus(
        "current"
    )

cps6000TrapPs1Amtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 28)
)
cps6000TrapPs1Amtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Amtl.setStatus(
        "current"
    )

cps6000TrapPs1Bbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 29)
)
cps6000TrapPs1Bbl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Bbl.setStatus(
        "current"
    )

cps6000TrapPs1Cch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 30)
)
cps6000TrapPs1Cch.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Cch.setStatus(
        "current"
    )

cps6000TrapPs1Clc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 31)
)
cps6000TrapPs1Clc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Clc.setStatus(
        "current"
    )

cps6000TrapPs1Epr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 32)
)
cps6000TrapPs1Epr.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Epr.setStatus(
        "current"
    )

cps6000TrapPs1Exl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 33)
)
cps6000TrapPs1Exl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Exl.setStatus(
        "current"
    )

cps6000TrapPs1Hcl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 34)
)
cps6000TrapPs1Hcl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Hcl.setStatus(
        "current"
    )

cps6000TrapPs1Pfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 35)
)
cps6000TrapPs1Pfd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Pfd.setStatus(
        "current"
    )

cps6000TrapPs1Pht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 36)
)
cps6000TrapPs1Pht.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Pht.setStatus(
        "current"
    )

cps6000TrapPs1Stf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 37)
)
cps6000TrapPs1Stf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Stf.setStatus(
        "current"
    )

cps6000TrapPs1Pgi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 38)
)
cps6000TrapPs1Pgi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Pgi.setStatus(
        "current"
    )

cps6000TrapPs1Ax1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 39)
)
cps6000TrapPs1Ax1.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax1.setStatus(
        "current"
    )

cps6000TrapPs1Ax2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 40)
)
cps6000TrapPs1Ax2.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax2.setStatus(
        "current"
    )

cps6000TrapPs1Ax3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 41)
)
cps6000TrapPs1Ax3.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax3.setStatus(
        "current"
    )

cps6000TrapPs1Ax4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 42)
)
cps6000TrapPs1Ax4.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax4.setStatus(
        "current"
    )

cps6000TrapPs1Ax5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 43)
)
cps6000TrapPs1Ax5.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax5.setStatus(
        "current"
    )

cps6000TrapPs1Ax6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 44)
)
cps6000TrapPs1Ax6.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPs1Ax6.setStatus(
        "current"
    )

cps6000TrapAt1Ata = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 45)
)
cps6000TrapAt1Ata.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapAt1Ata.setStatus(
        "current"
    )

cps6000TrapAt1Atb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 46)
)
cps6000TrapAt1Atb.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapAt1Atb.setStatus(
        "current"
    )

cps6000TrapCp1Cfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 47)
)
cps6000TrapCp1Cfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Cfa.setStatus(
        "current"
    )

cps6000TrapCp1Dfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 48)
)
cps6000TrapCp1Dfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Dfa.setStatus(
        "current"
    )

cps6000TrapCp1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 49)
)
cps6000TrapCp1Did.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Did.setStatus(
        "current"
    )

cps6000TrapCp1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 50)
)
cps6000TrapCp1Mfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Mfa.setStatus(
        "current"
    )

cps6000TrapBs1Bsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 51)
)
cps6000TrapBs1Bsa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBs1Bsa.setStatus(
        "current"
    )

cps6000TrapBr1Bta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 52)
)
cps6000TrapBr1Bta.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Bta.setStatus(
        "current"
    )

cps6000TrapBr1Bfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 53)
)
cps6000TrapBr1Bfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Bfa.setStatus(
        "current"
    )

cps6000TrapBr1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 54)
)
cps6000TrapBr1Btha.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Btha.setStatus(
        "current"
    )

cps6000TrapBr1Isda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 55)
)
cps6000TrapBr1Isda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Isda.setStatus(
        "current"
    )

cps6000TrapCn1Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 56)
)
cps6000TrapCn1Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn1Cno.setStatus(
        "current"
    )

cps6000TrapCn1Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 57)
)
cps6000TrapCn1Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn1Cnf.setStatus(
        "current"
    )

cps6000TrapCn2Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 58)
)
cps6000TrapCn2Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn2Cno.setStatus(
        "current"
    )

cps6000TrapCn2Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 59)
)
cps6000TrapCn2Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn2Cnf.setStatus(
        "current"
    )

cps6000TrapCn3Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 60)
)
cps6000TrapCn3Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn3Cno.setStatus(
        "current"
    )

cps6000TrapCn3Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 61)
)
cps6000TrapCn3Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn3Cnf.setStatus(
        "current"
    )

cps6000TrapCn4Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 62)
)
cps6000TrapCn4Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn4Cno.setStatus(
        "current"
    )

cps6000TrapCn4Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 63)
)
cps6000TrapCn4Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCn4Cnf.setStatus(
        "current"
    )

cps6000TrapCm1Cof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 64)
)
cps6000TrapCm1Cof.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCm1Cof.setStatus(
        "current"
    )

cps6000TrapCm1Cor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 65)
)
cps6000TrapCm1Cor.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCm1Cor.setStatus(
        "current"
    )

cps6000TrapCm1Nnc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 66)
)
cps6000TrapCm1Nnc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCm1Nnc.setStatus(
        "current"
    )

cps6000TrapPo1Por = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 67)
)
cps6000TrapPo1Por.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapPo1Por.setStatus(
        "current"
    )

cps6000TrapRp1Rf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 68)
)
cps6000TrapRp1Rf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rf.setStatus(
        "current"
    )

cps6000TrapRp1Rpff = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 69)
)
cps6000TrapRp1Rpff.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rpff.setStatus(
        "current"
    )

cps6000TrapRp1Rpxj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 70)
)
cps6000TrapRp1Rpxj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rpxj.setStatus(
        "current"
    )

cps6000TrapRp1Rpxn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 71)
)
cps6000TrapRp1Rpxn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rpxn.setStatus(
        "current"
    )

cps6000TrapRp1Rprl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 72)
)
cps6000TrapRp1Rprl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rprl.setStatus(
        "current"
    )

cps6000TrapRp1Rpfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 73)
)
cps6000TrapRp1Rpfj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rpfj.setStatus(
        "current"
    )

cps6000TrapUserDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 74)
)
cps6000TrapUserDefined.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapUserDefined.setStatus(
        "current"
    )

cps6000TrapDc1Icr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 75)
)
cps6000TrapDc1Icr.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Icr.setStatus(
        "current"
    )

cps6000TrapDc1Rfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 76)
)
cps6000TrapDc1Rfn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Rfn.setStatus(
        "current"
    )

cps6000TrapDc1Emd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 77)
)
cps6000TrapDc1Emd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Emd.setStatus(
        "current"
    )

cps6000TrapCp1Cfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 78)
)
cps6000TrapCp1Cfn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Cfn.setStatus(
        "current"
    )

cps6000TrapCp1Cfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 79)
)
cps6000TrapCp1Cfj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Cfj.setStatus(
        "current"
    )

cps6000TrapCp1Icc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 80)
)
cps6000TrapCp1Icc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Icc.setStatus(
        "current"
    )

cps6000TrapCp1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 81)
)
cps6000TrapCp1Hva.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Hva.setStatus(
        "current"
    )

cps6000TrapCp1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 82)
)
cps6000TrapCp1Hfv.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Hfv.setStatus(
        "current"
    )

cps6000TrapCp1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 83)
)
cps6000TrapCp1Vla.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Vla.setStatus(
        "current"
    )

cps6000TrapCp1Rl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 84)
)
cps6000TrapCp1Rl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapCp1Rl.setStatus(
        "current"
    )

cps6000TrapBr1Mdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 85)
)
cps6000TrapBr1Mdp.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Mdp.setStatus(
        "current"
    )

cps6000TrapBr1Mzd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 86)
)
cps6000TrapBr1Mzd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Mzd.setStatus(
        "current"
    )

cps6000TrapBr1Scda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 87)
)
cps6000TrapBr1Scda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapBr1Scda.setStatus(
        "current"
    )

cps6000TrapRp1Rcdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 88)
)
cps6000TrapRp1Rcdp.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapRp1Rcdp.setStatus(
        "current"
    )

cps6000TrapFt1Fmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 89)
)
cps6000TrapFt1Fmi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Fmi.setStatus(
        "current"
    )

cps6000TrapFt1Fmj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 90)
)
cps6000TrapFt1Fmj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Fmj.setStatus(
        "current"
    )

cps6000TrapFt1Ipi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 91)
)
cps6000TrapFt1Ipi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Ipi.setStatus(
        "current"
    )

cps6000TrapFt1Ipj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 92)
)
cps6000TrapFt1Ipj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Ipj.setStatus(
        "current"
    )

cps6000TrapFt1Cbt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 93)
)
cps6000TrapFt1Cbt.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Cbt.setStatus(
        "current"
    )

cps6000TrapFt1Ctf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 94)
)
cps6000TrapFt1Ctf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Ctf.setStatus(
        "current"
    )

cps6000TrapFt1Mctf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 95)
)
cps6000TrapFt1Mctf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Mctf.setStatus(
        "current"
    )

cps6000TrapFt1Lor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 96)
)
cps6000TrapFt1Lor.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Lor.setStatus(
        "current"
    )

cps6000TrapFt1Lda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 97)
)
cps6000TrapFt1Lda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Lda.setStatus(
        "current"
    )

cps6000TrapFt1Lsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 98)
)
cps6000TrapFt1Lsa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Lsa.setStatus(
        "current"
    )

cps6000TrapFt1Lta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 99)
)
cps6000TrapFt1Lta.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapFt1Lta.setStatus(
        "current"
    )

cps6000TrapDc1Lsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 33, 100)
)
cps6000TrapDc1Lsf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000TrapDc1Lsf.setStatus(
        "current"
    )

cps6000RetireDc1Amj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 1)
)
cps6000RetireDc1Amj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Amj.setStatus(
        "current"
    )

cps6000RetireDc1Epo = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 2)
)
cps6000RetireDc1Epo.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Epo.setStatus(
        "current"
    )

cps6000RetireDc1Faj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 3)
)
cps6000RetireDc1Faj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Faj.setStatus(
        "current"
    )

cps6000RetireDc1Fan = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 4)
)
cps6000RetireDc1Fan.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Fan.setStatus(
        "current"
    )

cps6000RetireDc1Vsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 5)
)
cps6000RetireDc1Vsf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Vsf.setStatus(
        "current"
    )

cps6000RetireDc1Osa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 6)
)
cps6000RetireDc1Osa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Osa.setStatus(
        "current"
    )

cps6000RetireDc1Zid = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 7)
)
cps6000RetireDc1Zid.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Zid.setStatus(
        "current"
    )

cps6000RetireDc1Tpa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 8)
)
cps6000RetireDc1Tpa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Tpa.setStatus(
        "current"
    )

cps6000RetireDc1Vmf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 9)
)
cps6000RetireDc1Vmf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Vmf.setStatus(
        "current"
    )

cps6000RetireDc1Cma = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 10)
)
cps6000RetireDc1Cma.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Cma.setStatus(
        "current"
    )

cps6000RetireDc1Macf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 11)
)
cps6000RetireDc1Macf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Macf.setStatus(
        "current"
    )

cps6000RetireDc1Mcm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 12)
)
cps6000RetireDc1Mcm.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Mcm.setStatus(
        "current"
    )

cps6000RetireDc1Rfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 13)
)
cps6000RetireDc1Rfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Rfa.setStatus(
        "current"
    )

cps6000RetireDc1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 14)
)
cps6000RetireDc1Did.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Did.setStatus(
        "current"
    )

cps6000RetireDc1Clm = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 15)
)
cps6000RetireDc1Clm.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Clm.setStatus(
        "current"
    )

cps6000RetireDc1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 16)
)
cps6000RetireDc1Vla.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Vla.setStatus(
        "current"
    )

cps6000RetireDc1Acf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 17)
)
cps6000RetireDc1Acf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Acf.setStatus(
        "current"
    )

cps6000RetireDc1Man = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 18)
)
cps6000RetireDc1Man.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Man.setStatus(
        "current"
    )

cps6000RetireDc1Mman = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 19)
)
cps6000RetireDc1Mman.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Mman.setStatus(
        "current"
    )

cps6000RetireDc1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 20)
)
cps6000RetireDc1Mfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Mfa.setStatus(
        "current"
    )

cps6000RetireDc1Rtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 21)
)
cps6000RetireDc1Rtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Rtl.setStatus(
        "current"
    )

cps6000RetireDc1Rrtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 22)
)
cps6000RetireDc1Rrtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Rrtl.setStatus(
        "current"
    )

cps6000RetireDc1Rls = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 23)
)
cps6000RetireDc1Rls.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Rls.setStatus(
        "current"
    )

cps6000RetireDc1Bda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 24)
)
cps6000RetireDc1Bda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Bda.setStatus(
        "current"
    )

cps6000RetireDc1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 25)
)
cps6000RetireDc1Hva.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Hva.setStatus(
        "current"
    )

cps6000RetireDc1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 26)
)
cps6000RetireDc1Hfv.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Hfv.setStatus(
        "current"
    )

cps6000RetirePs1Amth = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 27)
)
cps6000RetirePs1Amth.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Amth.setStatus(
        "current"
    )

cps6000RetirePs1Amtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 28)
)
cps6000RetirePs1Amtl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Amtl.setStatus(
        "current"
    )

cps6000RetirePs1Bbl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 29)
)
cps6000RetirePs1Bbl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Bbl.setStatus(
        "current"
    )

cps6000RetirePs1Cch = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 30)
)
cps6000RetirePs1Cch.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Cch.setStatus(
        "current"
    )

cps6000RetirePs1Clc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 31)
)
cps6000RetirePs1Clc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Clc.setStatus(
        "current"
    )

cps6000RetirePs1Epr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 32)
)
cps6000RetirePs1Epr.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Epr.setStatus(
        "current"
    )

cps6000RetirePs1Exl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 33)
)
cps6000RetirePs1Exl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Exl.setStatus(
        "current"
    )

cps6000RetirePs1Hcl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 34)
)
cps6000RetirePs1Hcl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Hcl.setStatus(
        "current"
    )

cps6000RetirePs1Pfd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 35)
)
cps6000RetirePs1Pfd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Pfd.setStatus(
        "current"
    )

cps6000RetirePs1Pht = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 36)
)
cps6000RetirePs1Pht.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Pht.setStatus(
        "current"
    )

cps6000RetirePs1Stf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 37)
)
cps6000RetirePs1Stf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Stf.setStatus(
        "current"
    )

cps6000RetirePs1Pgi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 38)
)
cps6000RetirePs1Pgi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Pgi.setStatus(
        "current"
    )

cps6000RetirePs1Ax1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 39)
)
cps6000RetirePs1Ax1.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax1.setStatus(
        "current"
    )

cps6000RetirePs1Ax2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 40)
)
cps6000RetirePs1Ax2.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax2.setStatus(
        "current"
    )

cps6000RetirePs1Ax3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 41)
)
cps6000RetirePs1Ax3.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax3.setStatus(
        "current"
    )

cps6000RetirePs1Ax4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 42)
)
cps6000RetirePs1Ax4.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax4.setStatus(
        "current"
    )

cps6000RetirePs1Ax5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 43)
)
cps6000RetirePs1Ax5.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax5.setStatus(
        "current"
    )

cps6000RetirePs1Ax6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 44)
)
cps6000RetirePs1Ax6.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePs1Ax6.setStatus(
        "current"
    )

cps6000RetireAt1Ata = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 45)
)
cps6000RetireAt1Ata.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireAt1Ata.setStatus(
        "current"
    )

cps6000RetireAt1Atb = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 46)
)
cps6000RetireAt1Atb.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireAt1Atb.setStatus(
        "current"
    )

cps6000RetireCp1Cfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 47)
)
cps6000RetireCp1Cfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Cfa.setStatus(
        "current"
    )

cps6000RetireCp1Dfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 48)
)
cps6000RetireCp1Dfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Dfa.setStatus(
        "current"
    )

cps6000RetireCp1Did = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 49)
)
cps6000RetireCp1Did.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Did.setStatus(
        "current"
    )

cps6000RetireCp1Mfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 50)
)
cps6000RetireCp1Mfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Mfa.setStatus(
        "current"
    )

cps6000RetireBs1Bsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 51)
)
cps6000RetireBs1Bsa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBs1Bsa.setStatus(
        "current"
    )

cps6000RetireBr1Bta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 52)
)
cps6000RetireBr1Bta.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Bta.setStatus(
        "current"
    )

cps6000RetireBr1Bfa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 53)
)
cps6000RetireBr1Bfa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Bfa.setStatus(
        "current"
    )

cps6000RetireBr1Btha = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 54)
)
cps6000RetireBr1Btha.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Btha.setStatus(
        "current"
    )

cps6000RetireBr1Isda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 55)
)
cps6000RetireBr1Isda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Isda.setStatus(
        "current"
    )

cps6000RetireCn1Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 56)
)
cps6000RetireCn1Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn1Cno.setStatus(
        "current"
    )

cps6000RetireCn1Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 57)
)
cps6000RetireCn1Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn1Cnf.setStatus(
        "current"
    )

cps6000RetireCn2Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 58)
)
cps6000RetireCn2Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn2Cno.setStatus(
        "current"
    )

cps6000RetireCn2Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 59)
)
cps6000RetireCn2Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn2Cnf.setStatus(
        "current"
    )

cps6000RetireCn3Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 60)
)
cps6000RetireCn3Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn3Cno.setStatus(
        "current"
    )

cps6000RetireCn3Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 61)
)
cps6000RetireCn3Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn3Cnf.setStatus(
        "current"
    )

cps6000RetireCn4Cno = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 62)
)
cps6000RetireCn4Cno.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn4Cno.setStatus(
        "current"
    )

cps6000RetireCn4Cnf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 63)
)
cps6000RetireCn4Cnf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCn4Cnf.setStatus(
        "current"
    )

cps6000RetireCm1Cof = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 64)
)
cps6000RetireCm1Cof.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCm1Cof.setStatus(
        "current"
    )

cps6000RetireCm1Cor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 65)
)
cps6000RetireCm1Cor.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCm1Cor.setStatus(
        "current"
    )

cps6000RetireCm1Nnc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 66)
)
cps6000RetireCm1Nnc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCm1Nnc.setStatus(
        "current"
    )

cps6000RetirePo1Por = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 67)
)
cps6000RetirePo1Por.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetirePo1Por.setStatus(
        "current"
    )

cps6000RetireRp1Rf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 68)
)
cps6000RetireRp1Rf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rf.setStatus(
        "current"
    )

cps6000RetireRp1Rpff = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 69)
)
cps6000RetireRp1Rpff.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rpff.setStatus(
        "current"
    )

cps6000RetireRp1Rpxj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 70)
)
cps6000RetireRp1Rpxj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rpxj.setStatus(
        "current"
    )

cps6000RetireRp1Rpxn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 71)
)
cps6000RetireRp1Rpxn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rpxn.setStatus(
        "current"
    )

cps6000RetireRp1Rprl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 72)
)
cps6000RetireRp1Rprl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rprl.setStatus(
        "current"
    )

cps6000RetireRp1Rpfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 73)
)
cps6000RetireRp1Rpfj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rpfj.setStatus(
        "current"
    )

cps6000RetireUserDefined = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 74)
)
cps6000RetireUserDefined.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireUserDefined.setStatus(
        "current"
    )

cps6000RetireDc1Icr = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 75)
)
cps6000RetireDc1Icr.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Icr.setStatus(
        "current"
    )

cps6000RetireDc1Rfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 76)
)
cps6000RetireDc1Rfn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Rfn.setStatus(
        "current"
    )

cps6000RetireDc1Emd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 77)
)
cps6000RetireDc1Emd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Emd.setStatus(
        "current"
    )

cps6000RetireCp1Cfn = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 78)
)
cps6000RetireCp1Cfn.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Cfn.setStatus(
        "current"
    )

cps6000RetireCp1Cfj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 79)
)
cps6000RetireCp1Cfj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Cfj.setStatus(
        "current"
    )

cps6000RetireCp1Icc = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 80)
)
cps6000RetireCp1Icc.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Icc.setStatus(
        "current"
    )

cps6000RetireCp1Hva = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 81)
)
cps6000RetireCp1Hva.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Hva.setStatus(
        "current"
    )

cps6000RetireCp1Hfv = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 82)
)
cps6000RetireCp1Hfv.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Hfv.setStatus(
        "current"
    )

cps6000RetireCp1Vla = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 83)
)
cps6000RetireCp1Vla.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Vla.setStatus(
        "current"
    )

cps6000RetireCp1Rl = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 84)
)
cps6000RetireCp1Rl.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireCp1Rl.setStatus(
        "current"
    )

cps6000RetireBr1Mdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 85)
)
cps6000RetireBr1Mdp.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Mdp.setStatus(
        "current"
    )

cps6000RetireBr1Mzd = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 86)
)
cps6000RetireBr1Mzd.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Mzd.setStatus(
        "current"
    )

cps6000RetireBr1Scda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 87)
)
cps6000RetireBr1Scda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireBr1Scda.setStatus(
        "current"
    )

cps6000RetireRp1Rcdp = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 88)
)
cps6000RetireRp1Rcdp.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireRp1Rcdp.setStatus(
        "current"
    )

cps6000RetireFt1Fmi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 89)
)
cps6000RetireFt1Fmi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Fmi.setStatus(
        "current"
    )

cps6000RetireFt1Fmj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 90)
)
cps6000RetireFt1Fmj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Fmj.setStatus(
        "current"
    )

cps6000RetireFt1Ipi = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 91)
)
cps6000RetireFt1Ipi.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Ipi.setStatus(
        "current"
    )

cps6000RetireFt1Ipj = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 92)
)
cps6000RetireFt1Ipj.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Ipj.setStatus(
        "current"
    )

cps6000RetireFt1Cbt = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 93)
)
cps6000RetireFt1Cbt.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Cbt.setStatus(
        "current"
    )

cps6000RetireFt1Ctf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 94)
)
cps6000RetireFt1Ctf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Ctf.setStatus(
        "current"
    )

cps6000RetireFt1Mctf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 95)
)
cps6000RetireFt1Mctf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Mctf.setStatus(
        "current"
    )

cps6000RetireFt1Lor = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 96)
)
cps6000RetireFt1Lor.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Lor.setStatus(
        "current"
    )

cps6000RetireFt1Lda = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 97)
)
cps6000RetireFt1Lda.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Lda.setStatus(
        "current"
    )

cps6000RetireFt1Lsa = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 98)
)
cps6000RetireFt1Lsa.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Lsa.setStatus(
        "current"
    )

cps6000RetireFt1Lta = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 99)
)
cps6000RetireFt1Lta.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireFt1Lta.setStatus(
        "current"
    )

cps6000RetireDc1Lsf = NotificationType(
    (1, 3, 6, 1, 4, 1, 10520, 2, 1, 1, 35, 100)
)
cps6000RetireDc1Lsf.setObjects(
    ("CPS6000-MIB", "trapInfo")
)
if mibBuilder.loadTexts:
    cps6000RetireDc1Lsf.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPS6000-MIB",
    **{"teps": teps,
       "controllermibs": controllermibs,
       "release": release,
       "cps6000": cps6000,
       "cps6000Dc1": cps6000Dc1,
       "cps6000Dc1Ide": cps6000Dc1Ide,
       "cps6000Dc1Des": cps6000Dc1Des,
       "cps6000Dc1Typ": cps6000Dc1Typ,
       "cps6000Dc1Stt": cps6000Dc1Stt,
       "cps6000Dc1Vdc": cps6000Dc1Vdc,
       "cps6000Dc1Adc": cps6000Dc1Adc,
       "cps6000Dc1Cap": cps6000Dc1Cap,
       "cps6000Dc1Olcap": cps6000Dc1Olcap,
       "cps6000Dc1Scap": cps6000Dc1Scap,
       "cps6000Dc1Nst": cps6000Dc1Nst,
       "cps6000Dc1Cps": cps6000Dc1Cps,
       "cps6000Dc1Bty": cps6000Dc1Bty,
       "cps6000Dc1Trd": cps6000Dc1Trd,
       "cps6000Dc1Isd": cps6000Dc1Isd,
       "cps6000Dc1Bod": cps6000Dc1Bod,
       "cps6000Dc1Rss": cps6000Dc1Rss,
       "cps6000Dc1Rot": cps6000Dc1Rot,
       "cps6000Dc1Bst": cps6000Dc1Bst,
       "cps6000Dc1Amj": cps6000Dc1Amj,
       "cps6000Dc1Epo": cps6000Dc1Epo,
       "cps6000Dc1Faj": cps6000Dc1Faj,
       "cps6000Dc1Fan": cps6000Dc1Fan,
       "cps6000Dc1Vsf": cps6000Dc1Vsf,
       "cps6000Dc1Osa": cps6000Dc1Osa,
       "cps6000Dc1Zid": cps6000Dc1Zid,
       "cps6000Dc1Tpa": cps6000Dc1Tpa,
       "cps6000Dc1Vmf": cps6000Dc1Vmf,
       "cps6000Dc1Cma": cps6000Dc1Cma,
       "cps6000Dc1Macf": cps6000Dc1Macf,
       "cps6000Dc1Mcm": cps6000Dc1Mcm,
       "cps6000Dc1Rfa": cps6000Dc1Rfa,
       "cps6000Dc1Did": cps6000Dc1Did,
       "cps6000Dc1Clm": cps6000Dc1Clm,
       "cps6000Dc1Vla": cps6000Dc1Vla,
       "cps6000Dc1Acf": cps6000Dc1Acf,
       "cps6000Dc1Man": cps6000Dc1Man,
       "cps6000Dc1Mman": cps6000Dc1Mman,
       "cps6000Dc1Mfa": cps6000Dc1Mfa,
       "cps6000Dc1Rtl": cps6000Dc1Rtl,
       "cps6000Dc1Rrtl": cps6000Dc1Rrtl,
       "cps6000Dc1Rls": cps6000Dc1Rls,
       "cps6000Dc1Bda": cps6000Dc1Bda,
       "cps6000Dc1Hva": cps6000Dc1Hva,
       "cps6000Dc1Hfv": cps6000Dc1Hfv,
       "cps6000Dc1Ron": cps6000Dc1Ron,
       "cps6000Dc1Rsq": cps6000Dc1Rsq,
       "cps6000Dc1Rtm": cps6000Dc1Rtm,
       "cps6000Dc1Icr": cps6000Dc1Icr,
       "cps6000Dc1Rfn": cps6000Dc1Rfn,
       "cps6000Dc1Emd": cps6000Dc1Emd,
       "cps6000Dc1Mls": cps6000Dc1Mls,
       "cps6000Dc1Bdt": cps6000Dc1Bdt,
       "cps6000Dc1Ems": cps6000Dc1Ems,
       "cps6000Dc1Eme": cps6000Dc1Eme,
       "cps6000Dc1Emt": cps6000Dc1Emt,
       "cps6000Dc1Emo": cps6000Dc1Emo,
       "cps6000Dc1Poc": cps6000Dc1Poc,
       "cps6000Dc1Lsf": cps6000Dc1Lsf,
       "cps6000Ps1": cps6000Ps1,
       "cps6000Ps1Ide": cps6000Ps1Ide,
       "cps6000Ps1Des": cps6000Ps1Des,
       "cps6000Ps1Sid": cps6000Ps1Sid,
       "cps6000Ps1Sde": cps6000Ps1Sde,
       "cps6000Ps1Swv": cps6000Ps1Swv,
       "cps6000Ps1Verb": cps6000Ps1Verb,
       "cps6000Ps1Verw": cps6000Ps1Verw,
       "cps6000Ps1Verd": cps6000Ps1Verd,
       "cps6000Ps1Dflt": cps6000Ps1Dflt,
       "cps6000Ps1Brc": cps6000Ps1Brc,
       "cps6000Ps1Sn": cps6000Ps1Sn,
       "cps6000Ps1Usl": cps6000Ps1Usl,
       "cps6000Ps1Dat": cps6000Ps1Dat,
       "cps6000Ps1Dtf": cps6000Ps1Dtf,
       "cps6000Ps1Tim": cps6000Ps1Tim,
       "cps6000Ps1Tmf": cps6000Ps1Tmf,
       "cps6000Ps1Dls": cps6000Ps1Dls,
       "cps6000Ps1Lng": cps6000Ps1Lng,
       "cps6000Ps1Ptt": cps6000Ps1Ptt,
       "cps6000Ps1Amt": cps6000Ps1Amt,
       "cps6000Ps1Tun": cps6000Ps1Tun,
       "cps6000Ps1Usr": cps6000Ps1Usr,
       "cps6000Ps1Poe": cps6000Ps1Poe,
       "cps6000Ps1Fpc": cps6000Ps1Fpc,
       "cps6000Ps1Rrf": cps6000Ps1Rrf,
       "cps6000Ps1Amth": cps6000Ps1Amth,
       "cps6000Ps1Amtl": cps6000Ps1Amtl,
       "cps6000Ps1Bbl": cps6000Ps1Bbl,
       "cps6000Ps1Cch": cps6000Ps1Cch,
       "cps6000Ps1Clc": cps6000Ps1Clc,
       "cps6000Ps1Epr": cps6000Ps1Epr,
       "cps6000Ps1Exl": cps6000Ps1Exl,
       "cps6000Ps1Hcl": cps6000Ps1Hcl,
       "cps6000Ps1Pfd": cps6000Ps1Pfd,
       "cps6000Ps1Pht": cps6000Ps1Pht,
       "cps6000Ps1Stf": cps6000Ps1Stf,
       "cps6000Ps1Pgi": cps6000Ps1Pgi,
       "cps6000Ps1Ax1": cps6000Ps1Ax1,
       "cps6000Ps1Ax2": cps6000Ps1Ax2,
       "cps6000Ps1Ax3": cps6000Ps1Ax3,
       "cps6000Ps1Ax4": cps6000Ps1Ax4,
       "cps6000Ps1Ax5": cps6000Ps1Ax5,
       "cps6000Ps1Ax6": cps6000Ps1Ax6,
       "cps6000Ps1Rss": cps6000Ps1Rss,
       "cps6000Ps1Sys": cps6000Ps1Sys,
       "cps6000Ps1Lngl": cps6000Ps1Lngl,
       "cps6000Ps1Fst": cps6000Ps1Fst,
       "cps6000Ps1Fstl": cps6000Ps1Fstl,
       "cps6000Ps1Fpe": cps6000Ps1Fpe,
       "cps6000Ps1Fpt": cps6000Ps1Fpt,
       "cps6000Ps1Ast": cps6000Ps1Ast,
       "cps6000Ps1Dss": cps6000Ps1Dss,
       "cps6000Ps1Dse": cps6000Ps1Dse,
       "cps6000At1": cps6000At1,
       "cps6000At1Ide": cps6000At1Ide,
       "cps6000At1Des": cps6000At1Des,
       "cps6000At1Stt": cps6000At1Stt,
       "cps6000At1Stg": cps6000At1Stg,
       "cps6000At1Lte": cps6000At1Lte,
       "cps6000At1Dur": cps6000At1Dur,
       "cps6000At1Pmj": cps6000At1Pmj,
       "cps6000At1Pmn": cps6000At1Pmn,
       "cps6000At1R1": cps6000At1R1,
       "cps6000At1R2": cps6000At1R2,
       "cps6000At1R3": cps6000At1R3,
       "cps6000At1R4": cps6000At1R4,
       "cps6000At1Ata": cps6000At1Ata,
       "cps6000At1Atb": cps6000At1Atb,
       "cps6000At1Ets": cps6000At1Ets,
       "cps6000At1Ems": cps6000At1Ems,
       "cps6000At1Irt": cps6000At1Irt,
       "cps6000Dct1": cps6000Dct1,
       "cps6000Dct1Ide": cps6000Dct1Ide,
       "cps6000Dct1Des": cps6000Dct1Des,
       "cps6000Dct1Src": cps6000Dct1Src,
       "cps6000Gm1": cps6000Gm1,
       "cps6000Gm1Ide": cps6000Gm1Ide,
       "cps6000Gm1Des": cps6000Gm1Des,
       "cps6000Gm1Lse": cps6000Gm1Lse,
       "cps6000Gm1Fsd": cps6000Gm1Fsd,
       "cps6000Gm1Bsd": cps6000Gm1Bsd,
       "cps6000Gm1Fsp": cps6000Gm1Fsp,
       "cps6000Gm1Bsp": cps6000Gm1Bsp,
       "cps6000Gm1Fcl": cps6000Gm1Fcl,
       "cps6000Gm1Bcl": cps6000Gm1Bcl,
       "cps6000Gm1Rme": cps6000Gm1Rme,
       "cps6000RecTable": cps6000RecTable,
       "cps6000RecEntry": cps6000RecEntry,
       "cps6000RecEntryIndex": cps6000RecEntryIndex,
       "cps6000RecEntryIde": cps6000RecEntryIde,
       "cps6000RecEntryDes": cps6000RecEntryDes,
       "cps6000RecEntryTyp": cps6000RecEntryTyp,
       "cps6000RecEntryAdc": cps6000RecEntryAdc,
       "cps6000RecEntryVdc": cps6000RecEntryVdc,
       "cps6000RecEntryStt": cps6000RecEntryStt,
       "cps6000RecEntryCap": cps6000RecEntryCap,
       "cps6000RecEntryTmp": cps6000RecEntryTmp,
       "cps6000RecEntrySeq": cps6000RecEntrySeq,
       "cps6000RecEntryRfa": cps6000RecEntryRfa,
       "cps6000RecEntryAcf": cps6000RecEntryAcf,
       "cps6000RecEntryMan": cps6000RecEntryMan,
       "cps6000RecEntryDid": cps6000RecEntryDid,
       "cps6000RecEntryClm": cps6000RecEntryClm,
       "cps6000RecEntryRcf": cps6000RecEntryRcf,
       "cps6000RecEntryRfn": cps6000RecEntryRfn,
       "cps6000RecEntrySn": cps6000RecEntrySn,
       "cps6000RecEntryVac": cps6000RecEntryVac,
       "cps6000RecEntryAac": cps6000RecEntryAac,
       "cps6000Cp1": cps6000Cp1,
       "cps6000Cp1Ide": cps6000Cp1Ide,
       "cps6000Cp1Des": cps6000Cp1Des,
       "cps6000Cp1Vdc": cps6000Cp1Vdc,
       "cps6000Cp1Adc": cps6000Cp1Adc,
       "cps6000Cp1Cap": cps6000Cp1Cap,
       "cps6000Cp1Vsp": cps6000Cp1Vsp,
       "cps6000Cp1Dth": cps6000Cp1Dth,
       "cps6000Cp1Rth": cps6000Cp1Rth,
       "cps6000Cp1Lvd": cps6000Cp1Lvd,
       "cps6000Cp1Cfa": cps6000Cp1Cfa,
       "cps6000Cp1Dfa": cps6000Cp1Dfa,
       "cps6000Cp1Did": cps6000Cp1Did,
       "cps6000Cp1Mfa": cps6000Cp1Mfa,
       "cps6000Cp1Cfn": cps6000Cp1Cfn,
       "cps6000Cp1Cfj": cps6000Cp1Cfj,
       "cps6000Cp1Icc": cps6000Cp1Icc,
       "cps6000Cp1Hva": cps6000Cp1Hva,
       "cps6000Cp1Hfv": cps6000Cp1Hfv,
       "cps6000Cp1Vla": cps6000Cp1Vla,
       "cps6000Cp1Rl": cps6000Cp1Rl,
       "cps6000Cp1Typ": cps6000Cp1Typ,
       "cps6000Cp1Olcap": cps6000Cp1Olcap,
       "cps6000Cp1Vsd": cps6000Cp1Vsd,
       "cps6000Cp1Clm": cps6000Cp1Clm,
       "cps6000Cp1Rof": cps6000Cp1Rof,
       "cps6000Cp1Rme": cps6000Cp1Rme,
       "cps6000Cp1Rss": cps6000Cp1Rss,
       "cps6000DccTable": cps6000DccTable,
       "cps6000DccEntry": cps6000DccEntry,
       "cps6000DccEntryIndex": cps6000DccEntryIndex,
       "cps6000DccEntryIde": cps6000DccEntryIde,
       "cps6000DccEntryDes": cps6000DccEntryDes,
       "cps6000DccEntryTyp": cps6000DccEntryTyp,
       "cps6000DccEntryAdc": cps6000DccEntryAdc,
       "cps6000DccEntryCap": cps6000DccEntryCap,
       "cps6000DccEntryStt": cps6000DccEntryStt,
       "cps6000DccEntryCfa": cps6000DccEntryCfa,
       "cps6000DccEntryDfa": cps6000DccEntryDfa,
       "cps6000DccEntryDid": cps6000DccEntryDid,
       "cps6000DccEntryCcf": cps6000DccEntryCcf,
       "cps6000DccEntryCfn": cps6000DccEntryCfn,
       "cps6000DccEntrySn": cps6000DccEntrySn,
       "cps6000Bs1": cps6000Bs1,
       "cps6000Bs1Ide": cps6000Bs1Ide,
       "cps6000Bs1Des": cps6000Bs1Des,
       "cps6000Bs1Stt": cps6000Bs1Stt,
       "cps6000Bs1Atm": cps6000Bs1Atm,
       "cps6000Bs1Tmd": cps6000Bs1Tmd,
       "cps6000Bs1Amf": cps6000Bs1Amf,
       "cps6000Bs1Cta": cps6000Bs1Cta,
       "cps6000Bs1Bsa": cps6000Bs1Bsa,
       "cps6000Sc1": cps6000Sc1,
       "cps6000Sc1Ide": cps6000Sc1Ide,
       "cps6000Sc1Des": cps6000Sc1Des,
       "cps6000Sc1Stt": cps6000Sc1Stt,
       "cps6000Sc1Rve": cps6000Sc1Rve,
       "cps6000Sc1Ltt": cps6000Sc1Ltt,
       "cps6000Sc1Ntt": cps6000Sc1Ntt,
       "cps6000Sc1Utt": cps6000Sc1Utt,
       "cps6000Sc1Spt": cps6000Sc1Spt,
       "cps6000Sc1Lsp": cps6000Sc1Lsp,
       "cps6000Sc1Usp": cps6000Sc1Usp,
       "cps6000BtdTable": cps6000BtdTable,
       "cps6000BtdEntry": cps6000BtdEntry,
       "cps6000BtdEntryIndex": cps6000BtdEntryIndex,
       "cps6000BtdEntryIde": cps6000BtdEntryIde,
       "cps6000BtdEntryDes": cps6000BtdEntryDes,
       "cps6000BtdEntryBty": cps6000BtdEntryBty,
       "cps6000BtdEntryBtc": cps6000BtdEntryBtc,
       "cps6000BtdEntryCap": cps6000BtdEntryCap,
       "cps6000Br1": cps6000Br1,
       "cps6000Br1Ide": cps6000Br1Ide,
       "cps6000Br1Des": cps6000Br1Des,
       "cps6000Br1Hbt": cps6000Br1Hbt,
       "cps6000Br1Adc": cps6000Br1Adc,
       "cps6000Br1Cap": cps6000Br1Cap,
       "cps6000Br1Olcap": cps6000Br1Olcap,
       "cps6000Br1Bts": cps6000Br1Bts,
       "cps6000Br1Scd": cps6000Br1Scd,
       "cps6000Br1Scv": cps6000Br1Scv,
       "cps6000Br1Ntm": cps6000Br1Ntm,
       "cps6000Br1Nvm": cps6000Br1Nvm,
       "cps6000Br1Cle": cps6000Br1Cle,
       "cps6000Br1Clt": cps6000Br1Clt,
       "cps6000Br1Mtt": cps6000Br1Mtt,
       "cps6000Br1Bte": cps6000Br1Bte,
       "cps6000Br1Atd": cps6000Br1Atd,
       "cps6000Br1Ath": cps6000Br1Ath,
       "cps6000Br1Atw": cps6000Br1Atw,
       "cps6000Br1Tin": cps6000Br1Tin,
       "cps6000Br1Tmd": cps6000Br1Tmd,
       "cps6000Br1Tev": cps6000Br1Tev,
       "cps6000Br1Btv": cps6000Br1Btv,
       "cps6000Br1Tth": cps6000Br1Tth,
       "cps6000Br1Cev": cps6000Br1Cev,
       "cps6000Br1Btr": cps6000Br1Btr,
       "cps6000Br1Bta": cps6000Br1Bta,
       "cps6000Br1Bfa": cps6000Br1Bfa,
       "cps6000Br1Btha": cps6000Br1Btha,
       "cps6000Br1Isda": cps6000Br1Isda,
       "cps6000Br1Mdp": cps6000Br1Mdp,
       "cps6000Br1Mzd": cps6000Br1Mzd,
       "cps6000Br1Scda": cps6000Br1Scda,
       "cps6000CntTable": cps6000CntTable,
       "cps6000CntEntry": cps6000CntEntry,
       "cps6000CntEntryIndex": cps6000CntEntryIndex,
       "cps6000CntEntryIde": cps6000CntEntryIde,
       "cps6000CntEntryDes": cps6000CntEntryDes,
       "cps6000CntEntryStt": cps6000CntEntryStt,
       "cps6000CntEntryEna": cps6000CntEntryEna,
       "cps6000CntEntryDth": cps6000CntEntryDth,
       "cps6000CntEntryDdy": cps6000CntEntryDdy,
       "cps6000CntEntryDam": cps6000CntEntryDam,
       "cps6000CntEntryDtm": cps6000CntEntryDtm,
       "cps6000CntEntryRth": cps6000CntEntryRth,
       "cps6000CntEntryRdy": cps6000CntEntryRdy,
       "cps6000CntEntryRam": cps6000CntEntryRam,
       "cps6000CntEntryRtm": cps6000CntEntryRtm,
       "cps6000CntEntryCno": cps6000CntEntryCno,
       "cps6000CntEntryCnf": cps6000CntEntryCnf,
       "cps6000DcnTable": cps6000DcnTable,
       "cps6000DcnEntry": cps6000DcnEntry,
       "cps6000DcnEntryIndex": cps6000DcnEntryIndex,
       "cps6000DcnEntryIde": cps6000DcnEntryIde,
       "cps6000DcnEntryDes": cps6000DcnEntryDes,
       "cps6000DcnEntryStt": cps6000DcnEntryStt,
       "cps6000DcnEntryTyp": cps6000DcnEntryTyp,
       "cps6000DcnEntrySn": cps6000DcnEntrySn,
       "cps6000DcnEntryBrc": cps6000DcnEntryBrc,
       "cps6000DcmTable": cps6000DcmTable,
       "cps6000DcmEntry": cps6000DcmEntry,
       "cps6000DcmEntryIndex": cps6000DcmEntryIndex,
       "cps6000DcmEntryIde": cps6000DcmEntryIde,
       "cps6000DcmEntryDes": cps6000DcmEntryDes,
       "cps6000DcmEntryStt": cps6000DcmEntryStt,
       "cps6000DcmEntryTyp": cps6000DcmEntryTyp,
       "cps6000DcmEntryVal": cps6000DcmEntryVal,
       "cps6000DcmEntrySha": cps6000DcmEntrySha,
       "cps6000DcmEntrySn": cps6000DcmEntrySn,
       "cps6000DcmEntryBrc": cps6000DcmEntryBrc,
       "cps6000UdeTable": cps6000UdeTable,
       "cps6000UdeEntry": cps6000UdeEntry,
       "cps6000UdeEntryIndex": cps6000UdeEntryIndex,
       "cps6000UdeEntryIde": cps6000UdeEntryIde,
       "cps6000UdeEntryDes": cps6000UdeEntryDes,
       "cps6000UdeEntryAst": cps6000UdeEntryAst,
       "cps6000UdeEntrySev": cps6000UdeEntrySev,
       "cps6000UdeEntryPrg": cps6000UdeEntryPrg,
       "cps6000UdeEntryDur": cps6000UdeEntryDur,
       "cps6000UdeEntryLat": cps6000UdeEntryLat,
       "cps6000UdeEntryAcc": cps6000UdeEntryAcc,
       "cps6000UdeEntryDly": cps6000UdeEntryDly,
       "cps6000UdeEntryNoo": cps6000UdeEntryNoo,
       "cps6000UdeEntryNor": cps6000UdeEntryNor,
       "cps6000UdeEntryNag": cps6000UdeEntryNag,
       "cps6000UdeEntryDst": cps6000UdeEntryDst,
       "cps6000UdeEntryFds": cps6000UdeEntryFds,
       "cps6000Cm1": cps6000Cm1,
       "cps6000Cm1Ide": cps6000Cm1Ide,
       "cps6000Cm1Des": cps6000Cm1Des,
       "cps6000Cm1Ngi": cps6000Cm1Ngi,
       "cps6000Cm1Cof": cps6000Cm1Cof,
       "cps6000Cm1Cor": cps6000Cm1Cor,
       "cps6000Cm1Nnc": cps6000Cm1Nnc,
       "cps6000CopTable": cps6000CopTable,
       "cps6000CopEntry": cps6000CopEntry,
       "cps6000CopEntryIndex": cps6000CopEntryIndex,
       "cps6000CopEntryIde": cps6000CopEntryIde,
       "cps6000CopEntryDes": cps6000CopEntryDes,
       "cps6000CopEntryTyp": cps6000CopEntryTyp,
       "cps6000CopEntryPhn": cps6000CopEntryPhn,
       "cps6000CopEntryBdr": cps6000CopEntryBdr,
       "cps6000CopEntryDbt": cps6000CopEntryDbt,
       "cps6000CopEntryPry": cps6000CopEntryPry,
       "cps6000CopEntrySbt": cps6000CopEntrySbt,
       "cps6000CopEntryDly": cps6000CopEntryDly,
       "cps6000CopEntryPgr": cps6000CopEntryPgr,
       "cps6000CopEntryMsg": cps6000CopEntryMsg,
       "cps6000CoeTable": cps6000CoeTable,
       "cps6000CoeEntry": cps6000CoeEntry,
       "cps6000CoeEntryIndex": cps6000CoeEntryIndex,
       "cps6000CoeEntryIde": cps6000CoeEntryIde,
       "cps6000CoeEntryDes": cps6000CoeEntryDes,
       "cps6000CoeEntryAdr": cps6000CoeEntryAdr,
       "cps6000CoeEntryTyp": cps6000CoeEntryTyp,
       "cps6000SndTable": cps6000SndTable,
       "cps6000SndEntry": cps6000SndEntry,
       "cps6000SndEntryIndex": cps6000SndEntryIndex,
       "cps6000SndEntryIde": cps6000SndEntryIde,
       "cps6000SndEntryDes": cps6000SndEntryDes,
       "cps6000SndEntryIp": cps6000SndEntryIp,
       "cps6000SndEntryCs": cps6000SndEntryCs,
       "cps6000Po1": cps6000Po1,
       "cps6000Po1Ide": cps6000Po1Ide,
       "cps6000Po1Des": cps6000Po1Des,
       "cps6000Po1Phn": cps6000Po1Phn,
       "cps6000Po1Bdr": cps6000Po1Bdr,
       "cps6000Po1Dbt": cps6000Po1Dbt,
       "cps6000Po1Pry": cps6000Po1Pry,
       "cps6000Po1Sbt": cps6000Po1Sbt,
       "cps6000Po1Int": cps6000Po1Int,
       "cps6000Po1Tim": cps6000Po1Tim,
       "cps6000Po1Cl01": cps6000Po1Cl01,
       "cps6000Po1Cl02": cps6000Po1Cl02,
       "cps6000Po1Cl03": cps6000Po1Cl03,
       "cps6000Po1Cl04": cps6000Po1Cl04,
       "cps6000Po1Cl05": cps6000Po1Cl05,
       "cps6000Po1Cl06": cps6000Po1Cl06,
       "cps6000Po1Cl07": cps6000Po1Cl07,
       "cps6000Po1Cl08": cps6000Po1Cl08,
       "cps6000Po1Cl09": cps6000Po1Cl09,
       "cps6000Po1Cl10": cps6000Po1Cl10,
       "cps6000Po1Por": cps6000Po1Por,
       "cps6000Cb1": cps6000Cb1,
       "cps6000Cb1Ide": cps6000Cb1Ide,
       "cps6000Cb1Des": cps6000Cb1Des,
       "cps6000Cb1Stt": cps6000Cb1Stt,
       "cps6000Cb1Ph1": cps6000Cb1Ph1,
       "cps6000Cb1Br1": cps6000Cb1Br1,
       "cps6000Cb1Ph2": cps6000Cb1Ph2,
       "cps6000Cb1Br2": cps6000Cb1Br2,
       "cps6000Cb1Ph3": cps6000Cb1Ph3,
       "cps6000Cb1Br3": cps6000Cb1Br3,
       "cps6000Cb1Ph4": cps6000Cb1Ph4,
       "cps6000Cb1Br4": cps6000Cb1Br4,
       "cps6000Cb1Ph5": cps6000Cb1Ph5,
       "cps6000Cb1Br5": cps6000Cb1Br5,
       "cps6000Mp1": cps6000Mp1,
       "cps6000Mp1Ide": cps6000Mp1Ide,
       "cps6000Mp1Des": cps6000Mp1Des,
       "cps6000Mp1Stt": cps6000Mp1Stt,
       "cps6000Mp1Dbt": cps6000Mp1Dbt,
       "cps6000Mp1Bdr": cps6000Mp1Bdr,
       "cps6000Mp1Pry": cps6000Mp1Pry,
       "cps6000Mp1Sbt": cps6000Mp1Sbt,
       "cps6000Mp1Tmo": cps6000Mp1Tmo,
       "cps6000Mp1Hsh": cps6000Mp1Hsh,
       "cps6000Mp1Nrg": cps6000Mp1Nrg,
       "cps6000Mp1Wre": cps6000Mp1Wre,
       "cps6000Mp1Ins": cps6000Mp1Ins,
       "cps6000Lp1": cps6000Lp1,
       "cps6000Lp1Ide": cps6000Lp1Ide,
       "cps6000Lp1Des": cps6000Lp1Des,
       "cps6000Lp1Stt": cps6000Lp1Stt,
       "cps6000Lp1Bdr": cps6000Lp1Bdr,
       "cps6000Lp1Dbt": cps6000Lp1Dbt,
       "cps6000Lp1Pry": cps6000Lp1Pry,
       "cps6000Lp1Sbt": cps6000Lp1Sbt,
       "cps6000Lp1Tmo": cps6000Lp1Tmo,
       "cps6000Lp1Hsh": cps6000Lp1Hsh,
       "cps6000Lp1App": cps6000Lp1App,
       "cps6000Lp1Wre": cps6000Lp1Wre,
       "cps6000Tlm1": cps6000Tlm1,
       "cps6000Tlm1Ide": cps6000Tlm1Ide,
       "cps6000Tlm1Des": cps6000Tlm1Des,
       "cps6000Tlm1Aue": cps6000Tlm1Aue,
       "cps6000Tlm1Cts": cps6000Tlm1Cts,
       "cps6000Tlm1Dsr": cps6000Tlm1Dsr,
       "cps6000Tlm1Prt": cps6000Tlm1Prt,
       "cps6000Tl1Table": cps6000Tl1Table,
       "cps6000Tl1Entry": cps6000Tl1Entry,
       "cps6000Tl1EntryIndex": cps6000Tl1EntryIndex,
       "cps6000Tl1EntryIde": cps6000Tl1EntryIde,
       "cps6000Tl1EntryDes": cps6000Tl1EntryDes,
       "cps6000Tl1EntryCds": cps6000Tl1EntryCds,
       "cps6000Tl1EntryAid": cps6000Tl1EntryAid,
       "cps6000Tl1EntryCnd": cps6000Tl1EntryCnd,
       "cps6000Tl1EntrySaf": cps6000Tl1EntrySaf,
       "cps6000Tl1EntryRpt": cps6000Tl1EntryRpt,
       "cps6000Net1": cps6000Net1,
       "cps6000Net1Ide": cps6000Net1Ide,
       "cps6000Net1Des": cps6000Net1Des,
       "cps6000Net1Ead": cps6000Net1Ead,
       "cps6000Net1Dhcp": cps6000Net1Dhcp,
       "cps6000Net1Ip": cps6000Net1Ip,
       "cps6000Net1Wip": cps6000Net1Wip,
       "cps6000Net1Sub": cps6000Net1Sub,
       "cps6000Net1Gtwy": cps6000Net1Gtwy,
       "cps6000Net1Host": cps6000Net1Host,
       "cps6000Net1Dom": cps6000Net1Dom,
       "cps6000Net1Dns": cps6000Net1Dns,
       "cps6000Net1Wre": cps6000Net1Wre,
       "cps6000Net1Tmo": cps6000Net1Tmo,
       "cps6000Net1Msrv": cps6000Net1Msrv,
       "cps6000DrcTable": cps6000DrcTable,
       "cps6000DrcEntry": cps6000DrcEntry,
       "cps6000DrcEntryIndex": cps6000DrcEntryIndex,
       "cps6000DrcEntryIde": cps6000DrcEntryIde,
       "cps6000DrcEntryDes": cps6000DrcEntryDes,
       "cps6000DrcEntryVal": cps6000DrcEntryVal,
       "cps6000DrcEntryPrg": cps6000DrcEntryPrg,
       "cps6000DrcEntryUni": cps6000DrcEntryUni,
       "cps6000InpTable": cps6000InpTable,
       "cps6000InpEntry": cps6000InpEntry,
       "cps6000InpEntryIndex": cps6000InpEntryIndex,
       "cps6000InpEntryIde": cps6000InpEntryIde,
       "cps6000InpEntryDes": cps6000InpEntryDes,
       "cps6000InpEntryStt": cps6000InpEntryStt,
       "cps6000InpEntryTyp": cps6000InpEntryTyp,
       "cps6000InpEntryPol": cps6000InpEntryPol,
       "cps6000InpEntrySn": cps6000InpEntrySn,
       "cps6000InpEntryBrc": cps6000InpEntryBrc,
       "cps6000Rp1": cps6000Rp1,
       "cps6000Rp1Ide": cps6000Rp1Ide,
       "cps6000Rp1Des": cps6000Rp1Des,
       "cps6000Rp1Frq": cps6000Rp1Frq,
       "cps6000Rp1Vsp": cps6000Rp1Vsp,
       "cps6000Rp1Ofe": cps6000Rp1Ofe,
       "cps6000Rp1Rme": cps6000Rp1Rme,
       "cps6000Rp1Rss": cps6000Rp1Rss,
       "cps6000Rp1Rf": cps6000Rp1Rf,
       "cps6000Rp1Rpff": cps6000Rp1Rpff,
       "cps6000Rp1Rpxj": cps6000Rp1Rpxj,
       "cps6000Rp1Rpxn": cps6000Rp1Rpxn,
       "cps6000Rp1Rprl": cps6000Rp1Rprl,
       "cps6000Rp1Rpfj": cps6000Rp1Rpfj,
       "cps6000Rp1Rcdp": cps6000Rp1Rcdp,
       "cps6000RchTable": cps6000RchTable,
       "cps6000RchEntry": cps6000RchEntry,
       "cps6000RchEntryIndex": cps6000RchEntryIndex,
       "cps6000RchEntryIde": cps6000RchEntryIde,
       "cps6000RchEntryDes": cps6000RchEntryDes,
       "cps6000RchEntryStt": cps6000RchEntryStt,
       "cps6000RchEntryVa": cps6000RchEntryVa,
       "cps6000RchEntryPri": cps6000RchEntryPri,
       "cps6000RchEntrySec": cps6000RchEntrySec,
       "cps6000RchEntryRf": cps6000RchEntryRf,
       "cps6000RchEntryRpff": cps6000RchEntryRpff,
       "cps6000RchEntryRpxj": cps6000RchEntryRpxj,
       "cps6000RchEntryRpxn": cps6000RchEntryRpxn,
       "cps6000RchEntryRprl": cps6000RchEntryRprl,
       "cps6000RchEntryRpfj": cps6000RchEntryRpfj,
       "cps6000RchEntryRcdp": cps6000RchEntryRcdp,
       "cps6000AlarmTable": cps6000AlarmTable,
       "cps6000AlarmEntry": cps6000AlarmEntry,
       "cps6000AlarmEntryIndex": cps6000AlarmEntryIndex,
       "cps6000AlarmEntryDes": cps6000AlarmEntryDes,
       "cps6000AlarmEntryAst": cps6000AlarmEntryAst,
       "cps6000AlarmEntrySev": cps6000AlarmEntrySev,
       "cps6000AlarmEntryAcc": cps6000AlarmEntryAcc,
       "cps6000AlarmEntryThr": cps6000AlarmEntryThr,
       "cps6000AlarmEntryFth": cps6000AlarmEntryFth,
       "cps6000AlarmEntryBth": cps6000AlarmEntryBth,
       "cps6000AlarmEntryDly": cps6000AlarmEntryDly,
       "cps6000AlarmEntryNoo": cps6000AlarmEntryNoo,
       "cps6000AlarmEntryNor": cps6000AlarmEntryNor,
       "cps6000AlarmEntryNag": cps6000AlarmEntryNag,
       "cps6000AlarmEntryDst": cps6000AlarmEntryDst,
       "cps6000AlarmEntryFds": cps6000AlarmEntryFds,
       "cps6000Trap": cps6000Trap,
       "cps6000TrapDc1Amj": cps6000TrapDc1Amj,
       "cps6000TrapDc1Epo": cps6000TrapDc1Epo,
       "cps6000TrapDc1Faj": cps6000TrapDc1Faj,
       "cps6000TrapDc1Fan": cps6000TrapDc1Fan,
       "cps6000TrapDc1Vsf": cps6000TrapDc1Vsf,
       "cps6000TrapDc1Osa": cps6000TrapDc1Osa,
       "cps6000TrapDc1Zid": cps6000TrapDc1Zid,
       "cps6000TrapDc1Tpa": cps6000TrapDc1Tpa,
       "cps6000TrapDc1Vmf": cps6000TrapDc1Vmf,
       "cps6000TrapDc1Cma": cps6000TrapDc1Cma,
       "cps6000TrapDc1Macf": cps6000TrapDc1Macf,
       "cps6000TrapDc1Mcm": cps6000TrapDc1Mcm,
       "cps6000TrapDc1Rfa": cps6000TrapDc1Rfa,
       "cps6000TrapDc1Did": cps6000TrapDc1Did,
       "cps6000TrapDc1Clm": cps6000TrapDc1Clm,
       "cps6000TrapDc1Vla": cps6000TrapDc1Vla,
       "cps6000TrapDc1Acf": cps6000TrapDc1Acf,
       "cps6000TrapDc1Man": cps6000TrapDc1Man,
       "cps6000TrapDc1Mman": cps6000TrapDc1Mman,
       "cps6000TrapDc1Mfa": cps6000TrapDc1Mfa,
       "cps6000TrapDc1Rtl": cps6000TrapDc1Rtl,
       "cps6000TrapDc1Rrtl": cps6000TrapDc1Rrtl,
       "cps6000TrapDc1Rls": cps6000TrapDc1Rls,
       "cps6000TrapDc1Bda": cps6000TrapDc1Bda,
       "cps6000TrapDc1Hva": cps6000TrapDc1Hva,
       "cps6000TrapDc1Hfv": cps6000TrapDc1Hfv,
       "cps6000TrapPs1Amth": cps6000TrapPs1Amth,
       "cps6000TrapPs1Amtl": cps6000TrapPs1Amtl,
       "cps6000TrapPs1Bbl": cps6000TrapPs1Bbl,
       "cps6000TrapPs1Cch": cps6000TrapPs1Cch,
       "cps6000TrapPs1Clc": cps6000TrapPs1Clc,
       "cps6000TrapPs1Epr": cps6000TrapPs1Epr,
       "cps6000TrapPs1Exl": cps6000TrapPs1Exl,
       "cps6000TrapPs1Hcl": cps6000TrapPs1Hcl,
       "cps6000TrapPs1Pfd": cps6000TrapPs1Pfd,
       "cps6000TrapPs1Pht": cps6000TrapPs1Pht,
       "cps6000TrapPs1Stf": cps6000TrapPs1Stf,
       "cps6000TrapPs1Pgi": cps6000TrapPs1Pgi,
       "cps6000TrapPs1Ax1": cps6000TrapPs1Ax1,
       "cps6000TrapPs1Ax2": cps6000TrapPs1Ax2,
       "cps6000TrapPs1Ax3": cps6000TrapPs1Ax3,
       "cps6000TrapPs1Ax4": cps6000TrapPs1Ax4,
       "cps6000TrapPs1Ax5": cps6000TrapPs1Ax5,
       "cps6000TrapPs1Ax6": cps6000TrapPs1Ax6,
       "cps6000TrapAt1Ata": cps6000TrapAt1Ata,
       "cps6000TrapAt1Atb": cps6000TrapAt1Atb,
       "cps6000TrapCp1Cfa": cps6000TrapCp1Cfa,
       "cps6000TrapCp1Dfa": cps6000TrapCp1Dfa,
       "cps6000TrapCp1Did": cps6000TrapCp1Did,
       "cps6000TrapCp1Mfa": cps6000TrapCp1Mfa,
       "cps6000TrapBs1Bsa": cps6000TrapBs1Bsa,
       "cps6000TrapBr1Bta": cps6000TrapBr1Bta,
       "cps6000TrapBr1Bfa": cps6000TrapBr1Bfa,
       "cps6000TrapBr1Btha": cps6000TrapBr1Btha,
       "cps6000TrapBr1Isda": cps6000TrapBr1Isda,
       "cps6000TrapCn1Cno": cps6000TrapCn1Cno,
       "cps6000TrapCn1Cnf": cps6000TrapCn1Cnf,
       "cps6000TrapCn2Cno": cps6000TrapCn2Cno,
       "cps6000TrapCn2Cnf": cps6000TrapCn2Cnf,
       "cps6000TrapCn3Cno": cps6000TrapCn3Cno,
       "cps6000TrapCn3Cnf": cps6000TrapCn3Cnf,
       "cps6000TrapCn4Cno": cps6000TrapCn4Cno,
       "cps6000TrapCn4Cnf": cps6000TrapCn4Cnf,
       "cps6000TrapCm1Cof": cps6000TrapCm1Cof,
       "cps6000TrapCm1Cor": cps6000TrapCm1Cor,
       "cps6000TrapCm1Nnc": cps6000TrapCm1Nnc,
       "cps6000TrapPo1Por": cps6000TrapPo1Por,
       "cps6000TrapRp1Rf": cps6000TrapRp1Rf,
       "cps6000TrapRp1Rpff": cps6000TrapRp1Rpff,
       "cps6000TrapRp1Rpxj": cps6000TrapRp1Rpxj,
       "cps6000TrapRp1Rpxn": cps6000TrapRp1Rpxn,
       "cps6000TrapRp1Rprl": cps6000TrapRp1Rprl,
       "cps6000TrapRp1Rpfj": cps6000TrapRp1Rpfj,
       "cps6000TrapUserDefined": cps6000TrapUserDefined,
       "cps6000TrapDc1Icr": cps6000TrapDc1Icr,
       "cps6000TrapDc1Rfn": cps6000TrapDc1Rfn,
       "cps6000TrapDc1Emd": cps6000TrapDc1Emd,
       "cps6000TrapCp1Cfn": cps6000TrapCp1Cfn,
       "cps6000TrapCp1Cfj": cps6000TrapCp1Cfj,
       "cps6000TrapCp1Icc": cps6000TrapCp1Icc,
       "cps6000TrapCp1Hva": cps6000TrapCp1Hva,
       "cps6000TrapCp1Hfv": cps6000TrapCp1Hfv,
       "cps6000TrapCp1Vla": cps6000TrapCp1Vla,
       "cps6000TrapCp1Rl": cps6000TrapCp1Rl,
       "cps6000TrapBr1Mdp": cps6000TrapBr1Mdp,
       "cps6000TrapBr1Mzd": cps6000TrapBr1Mzd,
       "cps6000TrapBr1Scda": cps6000TrapBr1Scda,
       "cps6000TrapRp1Rcdp": cps6000TrapRp1Rcdp,
       "cps6000TrapFt1Fmi": cps6000TrapFt1Fmi,
       "cps6000TrapFt1Fmj": cps6000TrapFt1Fmj,
       "cps6000TrapFt1Ipi": cps6000TrapFt1Ipi,
       "cps6000TrapFt1Ipj": cps6000TrapFt1Ipj,
       "cps6000TrapFt1Cbt": cps6000TrapFt1Cbt,
       "cps6000TrapFt1Ctf": cps6000TrapFt1Ctf,
       "cps6000TrapFt1Mctf": cps6000TrapFt1Mctf,
       "cps6000TrapFt1Lor": cps6000TrapFt1Lor,
       "cps6000TrapFt1Lda": cps6000TrapFt1Lda,
       "cps6000TrapFt1Lsa": cps6000TrapFt1Lsa,
       "cps6000TrapFt1Lta": cps6000TrapFt1Lta,
       "cps6000TrapDc1Lsf": cps6000TrapDc1Lsf,
       "trapInfo": trapInfo,
       "cps6000Retire": cps6000Retire,
       "cps6000RetireDc1Amj": cps6000RetireDc1Amj,
       "cps6000RetireDc1Epo": cps6000RetireDc1Epo,
       "cps6000RetireDc1Faj": cps6000RetireDc1Faj,
       "cps6000RetireDc1Fan": cps6000RetireDc1Fan,
       "cps6000RetireDc1Vsf": cps6000RetireDc1Vsf,
       "cps6000RetireDc1Osa": cps6000RetireDc1Osa,
       "cps6000RetireDc1Zid": cps6000RetireDc1Zid,
       "cps6000RetireDc1Tpa": cps6000RetireDc1Tpa,
       "cps6000RetireDc1Vmf": cps6000RetireDc1Vmf,
       "cps6000RetireDc1Cma": cps6000RetireDc1Cma,
       "cps6000RetireDc1Macf": cps6000RetireDc1Macf,
       "cps6000RetireDc1Mcm": cps6000RetireDc1Mcm,
       "cps6000RetireDc1Rfa": cps6000RetireDc1Rfa,
       "cps6000RetireDc1Did": cps6000RetireDc1Did,
       "cps6000RetireDc1Clm": cps6000RetireDc1Clm,
       "cps6000RetireDc1Vla": cps6000RetireDc1Vla,
       "cps6000RetireDc1Acf": cps6000RetireDc1Acf,
       "cps6000RetireDc1Man": cps6000RetireDc1Man,
       "cps6000RetireDc1Mman": cps6000RetireDc1Mman,
       "cps6000RetireDc1Mfa": cps6000RetireDc1Mfa,
       "cps6000RetireDc1Rtl": cps6000RetireDc1Rtl,
       "cps6000RetireDc1Rrtl": cps6000RetireDc1Rrtl,
       "cps6000RetireDc1Rls": cps6000RetireDc1Rls,
       "cps6000RetireDc1Bda": cps6000RetireDc1Bda,
       "cps6000RetireDc1Hva": cps6000RetireDc1Hva,
       "cps6000RetireDc1Hfv": cps6000RetireDc1Hfv,
       "cps6000RetirePs1Amth": cps6000RetirePs1Amth,
       "cps6000RetirePs1Amtl": cps6000RetirePs1Amtl,
       "cps6000RetirePs1Bbl": cps6000RetirePs1Bbl,
       "cps6000RetirePs1Cch": cps6000RetirePs1Cch,
       "cps6000RetirePs1Clc": cps6000RetirePs1Clc,
       "cps6000RetirePs1Epr": cps6000RetirePs1Epr,
       "cps6000RetirePs1Exl": cps6000RetirePs1Exl,
       "cps6000RetirePs1Hcl": cps6000RetirePs1Hcl,
       "cps6000RetirePs1Pfd": cps6000RetirePs1Pfd,
       "cps6000RetirePs1Pht": cps6000RetirePs1Pht,
       "cps6000RetirePs1Stf": cps6000RetirePs1Stf,
       "cps6000RetirePs1Pgi": cps6000RetirePs1Pgi,
       "cps6000RetirePs1Ax1": cps6000RetirePs1Ax1,
       "cps6000RetirePs1Ax2": cps6000RetirePs1Ax2,
       "cps6000RetirePs1Ax3": cps6000RetirePs1Ax3,
       "cps6000RetirePs1Ax4": cps6000RetirePs1Ax4,
       "cps6000RetirePs1Ax5": cps6000RetirePs1Ax5,
       "cps6000RetirePs1Ax6": cps6000RetirePs1Ax6,
       "cps6000RetireAt1Ata": cps6000RetireAt1Ata,
       "cps6000RetireAt1Atb": cps6000RetireAt1Atb,
       "cps6000RetireCp1Cfa": cps6000RetireCp1Cfa,
       "cps6000RetireCp1Dfa": cps6000RetireCp1Dfa,
       "cps6000RetireCp1Did": cps6000RetireCp1Did,
       "cps6000RetireCp1Mfa": cps6000RetireCp1Mfa,
       "cps6000RetireBs1Bsa": cps6000RetireBs1Bsa,
       "cps6000RetireBr1Bta": cps6000RetireBr1Bta,
       "cps6000RetireBr1Bfa": cps6000RetireBr1Bfa,
       "cps6000RetireBr1Btha": cps6000RetireBr1Btha,
       "cps6000RetireBr1Isda": cps6000RetireBr1Isda,
       "cps6000RetireCn1Cno": cps6000RetireCn1Cno,
       "cps6000RetireCn1Cnf": cps6000RetireCn1Cnf,
       "cps6000RetireCn2Cno": cps6000RetireCn2Cno,
       "cps6000RetireCn2Cnf": cps6000RetireCn2Cnf,
       "cps6000RetireCn3Cno": cps6000RetireCn3Cno,
       "cps6000RetireCn3Cnf": cps6000RetireCn3Cnf,
       "cps6000RetireCn4Cno": cps6000RetireCn4Cno,
       "cps6000RetireCn4Cnf": cps6000RetireCn4Cnf,
       "cps6000RetireCm1Cof": cps6000RetireCm1Cof,
       "cps6000RetireCm1Cor": cps6000RetireCm1Cor,
       "cps6000RetireCm1Nnc": cps6000RetireCm1Nnc,
       "cps6000RetirePo1Por": cps6000RetirePo1Por,
       "cps6000RetireRp1Rf": cps6000RetireRp1Rf,
       "cps6000RetireRp1Rpff": cps6000RetireRp1Rpff,
       "cps6000RetireRp1Rpxj": cps6000RetireRp1Rpxj,
       "cps6000RetireRp1Rpxn": cps6000RetireRp1Rpxn,
       "cps6000RetireRp1Rprl": cps6000RetireRp1Rprl,
       "cps6000RetireRp1Rpfj": cps6000RetireRp1Rpfj,
       "cps6000RetireUserDefined": cps6000RetireUserDefined,
       "cps6000RetireDc1Icr": cps6000RetireDc1Icr,
       "cps6000RetireDc1Rfn": cps6000RetireDc1Rfn,
       "cps6000RetireDc1Emd": cps6000RetireDc1Emd,
       "cps6000RetireCp1Cfn": cps6000RetireCp1Cfn,
       "cps6000RetireCp1Cfj": cps6000RetireCp1Cfj,
       "cps6000RetireCp1Icc": cps6000RetireCp1Icc,
       "cps6000RetireCp1Hva": cps6000RetireCp1Hva,
       "cps6000RetireCp1Hfv": cps6000RetireCp1Hfv,
       "cps6000RetireCp1Vla": cps6000RetireCp1Vla,
       "cps6000RetireCp1Rl": cps6000RetireCp1Rl,
       "cps6000RetireBr1Mdp": cps6000RetireBr1Mdp,
       "cps6000RetireBr1Mzd": cps6000RetireBr1Mzd,
       "cps6000RetireBr1Scda": cps6000RetireBr1Scda,
       "cps6000RetireRp1Rcdp": cps6000RetireRp1Rcdp,
       "cps6000RetireFt1Fmi": cps6000RetireFt1Fmi,
       "cps6000RetireFt1Fmj": cps6000RetireFt1Fmj,
       "cps6000RetireFt1Ipi": cps6000RetireFt1Ipi,
       "cps6000RetireFt1Ipj": cps6000RetireFt1Ipj,
       "cps6000RetireFt1Cbt": cps6000RetireFt1Cbt,
       "cps6000RetireFt1Ctf": cps6000RetireFt1Ctf,
       "cps6000RetireFt1Mctf": cps6000RetireFt1Mctf,
       "cps6000RetireFt1Lor": cps6000RetireFt1Lor,
       "cps6000RetireFt1Lda": cps6000RetireFt1Lda,
       "cps6000RetireFt1Lsa": cps6000RetireFt1Lsa,
       "cps6000RetireFt1Lta": cps6000RetireFt1Lta,
       "cps6000RetireDc1Lsf": cps6000RetireDc1Lsf,
       "cps6000MsvTable": cps6000MsvTable,
       "cps6000MsvEntry": cps6000MsvEntry,
       "cps6000MsvEntryIndex": cps6000MsvEntryIndex,
       "cps6000MsvEntryIde": cps6000MsvEntryIde,
       "cps6000MsvEntryDes": cps6000MsvEntryDes,
       "cps6000MsvEntryStt": cps6000MsvEntryStt,
       "cps6000MsvEntryVal": cps6000MsvEntryVal,
       "cps6000MsvEntryDid": cps6000MsvEntryDid,
       "cps6000Ft1": cps6000Ft1,
       "cps6000Ft1Ide": cps6000Ft1Ide,
       "cps6000Ft1Des": cps6000Ft1Des,
       "cps6000Ft1Stt": cps6000Ft1Stt,
       "cps6000Ft1Iadc": cps6000Ft1Iadc,
       "cps6000Ft1Lte": cps6000Ft1Lte,
       "cps6000Ft1Ltf": cps6000Ft1Ltf,
       "cps6000Ft1Fmi": cps6000Ft1Fmi,
       "cps6000Ft1Fmj": cps6000Ft1Fmj,
       "cps6000Ft1Ipi": cps6000Ft1Ipi,
       "cps6000Ft1Ipj": cps6000Ft1Ipj,
       "cps6000Ft1Cbt": cps6000Ft1Cbt,
       "cps6000Ft1Ctf": cps6000Ft1Ctf,
       "cps6000Ft1Mctf": cps6000Ft1Mctf,
       "cps6000Ft1Lor": cps6000Ft1Lor,
       "cps6000Ft1Lda": cps6000Ft1Lda,
       "cps6000Ft1Lsa": cps6000Ft1Lsa,
       "cps6000Ft1Lta": cps6000Ft1Lta,
       "cps6000Ft1Rem": cps6000Ft1Rem,
       "cps6000Ft1Tof": cps6000Ft1Tof,
       "cps6000GrpTable": cps6000GrpTable,
       "cps6000GrpEntry": cps6000GrpEntry,
       "cps6000GrpEntryIndex": cps6000GrpEntryIndex,
       "cps6000GrpEntryIde": cps6000GrpEntryIde,
       "cps6000GrpEntryDes": cps6000GrpEntryDes,
       "cps6000GrpEntryCct": cps6000GrpEntryCct,
       "cps6000GrpEntryTadc": cps6000GrpEntryTadc,
       "cps6000GrpEntryAadc": cps6000GrpEntryAadc,
       "cps6000GrpEntryCap": cps6000GrpEntryCap,
       "cps6000GrpEntryLrs": cps6000GrpEntryLrs,
       "cps6000GrpEntryOlcap": cps6000GrpEntryOlcap,
       "cps6000ShfTable": cps6000ShfTable,
       "cps6000ShfEntry": cps6000ShfEntry,
       "cps6000ShfEntryIndex": cps6000ShfEntryIndex,
       "cps6000ShfEntryIde": cps6000ShfEntryIde,
       "cps6000ShfEntryDes": cps6000ShfEntryDes,
       "cps6000ShfEntryStt": cps6000ShfEntryStt,
       "cps6000ShfEntryIadc": cps6000ShfEntryIadc,
       "cps6000ShfEntryIa1": cps6000ShfEntryIa1,
       "cps6000ShfEntryIa2": cps6000ShfEntryIa2,
       "cps6000ShfEntryIb1": cps6000ShfEntryIb1,
       "cps6000ShfEntryIb2": cps6000ShfEntryIb2,
       "cps6000ShfEntryUfn": cps6000ShfEntryUfn,
       "cps6000ShfEntryLfn": cps6000ShfEntryLfn,
       "cps6000ShfEntryCba": cps6000ShfEntryCba,
       "cps6000ShfEntryCbb": cps6000ShfEntryCbb,
       "cps6000ShfEntryCvj": cps6000ShfEntryCvj,
       "cps6000ShfEntryCvi": cps6000ShfEntryCvi,
       "cps6000ShfEntryNoc": cps6000ShfEntryNoc,
       "cps6000CctTable": cps6000CctTable,
       "cps6000CctEntry": cps6000CctEntry,
       "cps6000CctEntryIndex": cps6000CctEntryIndex,
       "cps6000CctEntryIde": cps6000CctEntryIde,
       "cps6000CctEntryDes": cps6000CctEntryDes,
       "cps6000CctEntryVdc": cps6000CctEntryVdc,
       "cps6000CctEntryAdc": cps6000CctEntryAdc,
       "cps6000CctEntryStt": cps6000CctEntryStt,
       "cps6000CctEntryTmp": cps6000CctEntryTmp,
       "cps6000CctEntryCap": cps6000CctEntryCap,
       "cps6000CctEntryCli": cps6000CctEntryCli,
       "cps6000CctEntrySnm": cps6000CctEntrySnm,
       "cps6000CctEntryMdl": cps6000CctEntryMdl,
       "cps6000CctEntryCcd": cps6000CctEntryCcd,
       "cps6000CctEntryCfl": cps6000CctEntryCfl,
       "cps6000CctEntryOv": cps6000CctEntryOv,
       "cps6000CctEntryCl": cps6000CctEntryCl,
       "cps6000CctEntryGf": cps6000CctEntryGf,
       "cps6000CctEntryUv": cps6000CctEntryUv,
       "cps6000CctEntryOt": cps6000CctEntryOt,
       "cps6000CctEntryLds": cps6000CctEntryLds,
       "cps6000CctEntryLss": cps6000CctEntryLss,
       "cps6000CctEntryLts": cps6000CctEntryLts,
       "cps6000CctEntryIlr": cps6000CctEntryIlr,
       "cps6000CctEntryAlr": cps6000CctEntryAlr,
       "prototypes": prototypes}
)
