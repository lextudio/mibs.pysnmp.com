# SNMP MIB module (ARISTA-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-PRODUCTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:24 2024
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

(aristaModules,
 aristaProducts) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaModules",
    "aristaProducts")

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

aristaProductsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 2, 1)
)
aristaProductsMIB.setRevisions(
        ("2017-03-09 00:00",
         "2017-01-30 00:00",
         "2017-01-03 00:00",
         "2016-12-15 00:00",
         "2016-12-13 00:00",
         "2016-12-02 00:00",
         "2016-11-30 00:00",
         "2016-11-19 00:00",
         "2016-11-14 04:29",
         "2016-11-14 04:24",
         "2016-10-21 00:00",
         "2016-09-08 00:00",
         "2016-08-08 00:00",
         "2016-05-27 00:00",
         "2016-05-11 00:00",
         "2016-03-23 00:00",
         "2016-01-12 00:00",
         "2016-01-05 00:00",
         "2016-01-03 00:00",
         "2015-11-16 00:00",
         "2015-10-28 00:00",
         "2015-10-12 00:00",
         "2015-10-02 17:00",
         "2015-10-02 16:00",
         "2015-09-29 00:00",
         "2015-09-15 00:00",
         "2015-06-03 00:00",
         "2015-05-27 00:00",
         "2015-04-20 00:00",
         "2015-04-10 00:00",
         "2015-03-25 12:00",
         "2015-03-25 00:00",
         "2015-03-19 00:00",
         "2015-02-11 00:00",
         "2015-02-10 00:00",
         "2014-12-02 00:00",
         "2014-08-15 00:00",
         "2014-07-31 09:30",
         "2014-07-18 09:00",
         "2014-05-19 16:00",
         "2014-04-08 16:00",
         "2014-04-04 16:09",
         "2014-04-04 16:08",
         "2014-04-02 12:00",
         "2014-04-02 11:00",
         "2014-03-11 16:00",
         "2014-01-02 16:00",
         "2014-01-01 09:00",
         "2013-11-24 09:30",
         "2013-11-24 09:00",
         "2013-11-24 08:30",
         "2013-11-24 08:00",
         "2013-11-23 12:00",
         "2013-11-23 11:30",
         "2013-11-23 11:00",
         "2013-11-19 08:00",
         "2013-11-13 08:00",
         "2013-11-01 08:00",
         "2013-10-02 08:00",
         "2013-09-26 11:20",
         "2013-06-08 08:00",
         "2013-01-26 08:00",
         "2012-12-12 12:12",
         "2012-11-28 08:00",
         "2012-09-03 08:00",
         "2012-08-31 08:00",
         "2012-04-17 08:00",
         "2012-04-03 08:00",
         "2012-03-09 08:00",
         "2012-02-20 08:00",
         "2012-02-01 08:00",
         "2011-09-01 08:00",
         "2011-08-29 08:00",
         "2011-08-04 08:00",
         "2011-07-16 14:00",
         "2011-06-22 18:00",
         "2011-03-31 13:00",
         "2011-02-24 08:00",
         "2010-10-24 16:00",
         "2010-09-17 20:40",
         "2010-04-05 09:42",
         "2010-04-05 09:41",
         "2009-06-08 15:58",
         "2009-04-17 15:05",
         "2008-09-10 14:15",
         "2008-03-03 12:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaLY6_ObjectIdentity = ObjectIdentity
aristaLY6 = _AristaLY6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 447, 6)
)
_AristaSmallstoneD4040_ObjectIdentity = ObjectIdentity
aristaSmallstoneD4040 = _AristaSmallstoneD4040_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 1470, 1605, 4040)
)
_AristaCVX_ObjectIdentity = ObjectIdentity
aristaCVX = _AristaCVX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 2682)
)
_AristaDCS7010T48_ObjectIdentity = ObjectIdentity
aristaDCS7010T48 = _AristaDCS7010T48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48)
)
_AristaDCS7010T48DC_ObjectIdentity = ObjectIdentity
aristaDCS7010T48DC = _AristaDCS7010T48DC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7010, 427, 48, 2957)
)
_AristaDCS7020TRA48_ObjectIdentity = ObjectIdentity
aristaDCS7020TRA48 = _AristaDCS7020TRA48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 312, 48)
)
_AristaDCS7020TR48_ObjectIdentity = ObjectIdentity
aristaDCS7020TR48 = _AristaDCS7020TR48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7020, 1964, 48)
)
_AristaDCS7048T4S_ObjectIdentity = ObjectIdentity
aristaDCS7048T4S = _AristaDCS7048T4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 4, 3282)
)
_AristaDCS7048TA_ObjectIdentity = ObjectIdentity
aristaDCS7048TA = _AristaDCS7048TA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7048, 427, 3648)
)
_AristaDCS7050T36_ObjectIdentity = ObjectIdentity
aristaDCS7050T36 = _AristaDCS7050T36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 36)
)
_AristaDCS7050T52_ObjectIdentity = ObjectIdentity
aristaDCS7050T52 = _AristaDCS7050T52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52)
)
_AristaDCS7050T52SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050T52SSD = _AristaDCS7050T52SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 52, 761)
)
_AristaDCS7050T64_ObjectIdentity = ObjectIdentity
aristaDCS7050T64 = _AristaDCS7050T64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64)
)
_AristaDCS7050T64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050T64SSD = _AristaDCS7050T64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 427, 64, 761)
)
_AristaDCS7050TX2128_ObjectIdentity = ObjectIdentity
aristaDCS7050TX2128 = _AristaDCS7050TX2128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 2, 128)
)
_AristaDCS7050TX2128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX2128SSD = _AristaDCS7050TX2128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 2, 128, 761)
)
_AristaDCS7050TX48_ObjectIdentity = ObjectIdentity
aristaDCS7050TX48 = _AristaDCS7050TX48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48)
)
_AristaDCS7050TX48SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX48SSD = _AristaDCS7050TX48SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 48, 761)
)
_AristaDCS7050TX64_ObjectIdentity = ObjectIdentity
aristaDCS7050TX64 = _AristaDCS7050TX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64)
)
_AristaDCS7050TX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX64SSD = _AristaDCS7050TX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 64, 761)
)
_AristaDCS7050TX72_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72 = _AristaDCS7050TX72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72)
)
_AristaDCS7050TX72SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72SSD = _AristaDCS7050TX72SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 761)
)
_AristaDCS7050TX72Q_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72Q = _AristaDCS7050TX72Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512)
)
_AristaDCS7050TX72QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX72QSSD = _AristaDCS7050TX72QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 72, 2512, 761)
)
_AristaDCS7050TX96_ObjectIdentity = ObjectIdentity
aristaDCS7050TX96 = _AristaDCS7050TX96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96)
)
_AristaDCS7050TX96SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX96SSD = _AristaDCS7050TX96SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 96, 761)
)
_AristaDCS7050TX128_ObjectIdentity = ObjectIdentity
aristaDCS7050TX128 = _AristaDCS7050TX128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128)
)
_AristaDCS7050TX128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050TX128SSD = _AristaDCS7050TX128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 1958, 128, 761)
)
_AristaDCS7050Q16_ObjectIdentity = ObjectIdentity
aristaDCS7050Q16 = _AristaDCS7050Q16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16)
)
_AristaDCS7050Q16SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050Q16SSD = _AristaDCS7050Q16SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 2512, 16, 761)
)
_AristaDCS7050QX232S_ObjectIdentity = ObjectIdentity
aristaDCS7050QX232S = _AristaDCS7050QX232S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 2, 32, 3282)
)
_AristaDCS7050QX232SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX232SSSD = _AristaDCS7050QX232SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 2, 32, 3282, 761)
)
_AristaDCS7050QX32_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32 = _AristaDCS7050QX32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32)
)
_AristaDCS7050QX32SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32SSD = _AristaDCS7050QX32SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 761)
)
_AristaDCS7050QX32CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32CLSSD = _AristaDCS7050QX32CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 2745, 761)
)
_AristaDCS7050QX32S_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32S = _AristaDCS7050QX32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282)
)
_AristaDCS7050QX32SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050QX32SSSD = _AristaDCS7050QX32SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3095, 32, 3282, 761)
)
_AristaDCS7050S52_ObjectIdentity = ObjectIdentity
aristaDCS7050S52 = _AristaDCS7050S52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52)
)
_AristaDCS7050S52SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050S52SSD = _AristaDCS7050S52SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 52, 761)
)
_AristaDCS7050S64_ObjectIdentity = ObjectIdentity
aristaDCS7050S64 = _AristaDCS7050S64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64)
)
_AristaDCS7050S64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050S64SSD = _AristaDCS7050S64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3282, 64, 761)
)
_AristaDCS7050SX272Q_ObjectIdentity = ObjectIdentity
aristaDCS7050SX272Q = _AristaDCS7050SX272Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 72, 2512)
)
_AristaDCS7050SX272QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX272QSSD = _AristaDCS7050SX272QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 72, 2512, 761)
)
_AristaDCS7050SX2128_ObjectIdentity = ObjectIdentity
aristaDCS7050SX2128 = _AristaDCS7050SX2128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 128)
)
_AristaDCS7050SX2128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX2128SSD = _AristaDCS7050SX2128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 2, 128, 761)
)
_AristaDCS7050SX64_ObjectIdentity = ObjectIdentity
aristaDCS7050SX64 = _AristaDCS7050SX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64)
)
_AristaDCS7050SX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX64SSD = _AristaDCS7050SX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 64, 761)
)
_AristaDCS7050SX72_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72 = _AristaDCS7050SX72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72)
)
_AristaDCS7050SX72SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72SSD = _AristaDCS7050SX72SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 761)
)
_AristaDCS7050SX72Q_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72Q = _AristaDCS7050SX72Q_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512)
)
_AristaDCS7050SX72QSSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX72QSSD = _AristaDCS7050SX72QSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 72, 2512, 761)
)
_AristaDCS7050SX96_ObjectIdentity = ObjectIdentity
aristaDCS7050SX96 = _AristaDCS7050SX96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96)
)
_AristaDCS7050SX96SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX96SSD = _AristaDCS7050SX96SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 96, 761)
)
_AristaDCS7050SX128_ObjectIdentity = ObjectIdentity
aristaDCS7050SX128 = _AristaDCS7050SX128_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128)
)
_AristaDCS7050SX128SSD_ObjectIdentity = ObjectIdentity
aristaDCS7050SX128SSD = _AristaDCS7050SX128SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7050, 3741, 128, 761)
)
_AristaDCS7060CX232S_ObjectIdentity = ObjectIdentity
aristaDCS7060CX232S = _AristaDCS7060CX232S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 2, 32, 3282)
)
_AristaDCS7060CX32S_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32S = _AristaDCS7060CX32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 3282)
)
_AristaDCS7060CX32SSSD_ObjectIdentity = ObjectIdentity
aristaDCS7060CX32SSSD = _AristaDCS7060CX32SSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7060, 2733, 32, 3282, 761)
)
_AristaDCS7120T4S_ObjectIdentity = ObjectIdentity
aristaDCS7120T4S = _AristaDCS7120T4S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7120, 427, 4, 3282)
)
_AristaDCS7124FX_ObjectIdentity = ObjectIdentity
aristaDCS7124FX = _AristaDCS7124FX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312)
)
_AristaDCS7124FXCL_ObjectIdentity = ObjectIdentity
aristaDCS7124FXCL = _AristaDCS7124FXCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 2312, 2745)
)
_AristaDCS7124S_ObjectIdentity = ObjectIdentity
aristaDCS7124S = _AristaDCS7124S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3282)
)
_AristaDCS7124SX_ObjectIdentity = ObjectIdentity
aristaDCS7124SX = _AristaDCS7124SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741)
)
_AristaDCS7124SXSSD_ObjectIdentity = ObjectIdentity
aristaDCS7124SXSSD = _AristaDCS7124SXSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7124, 3741, 761)
)
_AristaDCS7140T8S_ObjectIdentity = ObjectIdentity
aristaDCS7140T8S = _AristaDCS7140T8S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7140, 427, 8, 3282)
)
_AristaDCS7148S_ObjectIdentity = ObjectIdentity
aristaDCS7148S = _AristaDCS7148S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3282)
)
_AristaDCS7148SX_ObjectIdentity = ObjectIdentity
aristaDCS7148SX = _AristaDCS7148SX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7148, 3741)
)
_AristaDCS7150S24_ObjectIdentity = ObjectIdentity
aristaDCS7150S24 = _AristaDCS7150S24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24)
)
_AristaDCS7150S24CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S24CL = _AristaDCS7150S24CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745)
)
_AristaDCS7150S24CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S24CLSSD = _AristaDCS7150S24CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 24, 2745, 761)
)
_AristaDCS7150S52CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S52CL = _AristaDCS7150S52CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745)
)
_AristaDCS7150S52CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S52CLSSD = _AristaDCS7150S52CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 52, 2745, 761)
)
_AristaDCS7150S64CL_ObjectIdentity = ObjectIdentity
aristaDCS7150S64CL = _AristaDCS7150S64CL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745)
)
_AristaDCS7150S64CLSSD_ObjectIdentity = ObjectIdentity
aristaDCS7150S64CLSSD = _AristaDCS7150S64CLSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7150, 3282, 64, 2745, 761)
)
_AristaDCS716032CQ_ObjectIdentity = ObjectIdentity
aristaDCS716032CQ = _AristaDCS716032CQ_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 32, 2726)
)
_AristaDCS716032CQSSD_ObjectIdentity = ObjectIdentity
aristaDCS716032CQSSD = _AristaDCS716032CQSSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 32, 2726, 761)
)
_AristaDCS716048YC6_ObjectIdentity = ObjectIdentity
aristaDCS716048YC6 = _AristaDCS716048YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1654, 6)
)
_AristaDCS716048YC6SSD_ObjectIdentity = ObjectIdentity
aristaDCS716048YC6SSD = _AristaDCS716048YC6SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1654, 6, 761)
)
_AristaDCS716048TC6_ObjectIdentity = ObjectIdentity
aristaDCS716048TC6 = _AristaDCS716048TC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1981, 6)
)
_AristaDCS716048TC6SSD_ObjectIdentity = ObjectIdentity
aristaDCS716048TC6SSD = _AristaDCS716048TC6SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7160, 48, 1981, 6, 761)
)
_AristaDCS7250QX64_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64 = _AristaDCS7250QX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64)
)
_AristaDCS7250QX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64SSD = _AristaDCS7250QX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 761)
)
_AristaDCS7250QX64M_ObjectIdentity = ObjectIdentity
aristaDCS7250QX64M = _AristaDCS7250QX64M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7250, 3095, 64, 972)
)
_AristaDCS7260CX64_ObjectIdentity = ObjectIdentity
aristaDCS7260CX64 = _AristaDCS7260CX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 64)
)
_AristaDCS7260CX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7260CX64SSD = _AristaDCS7260CX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 2733, 64, 761)
)
_AristaDCS7260QX64_ObjectIdentity = ObjectIdentity
aristaDCS7260QX64 = _AristaDCS7260QX64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 3095, 64)
)
_AristaDCS7260QX64SSD_ObjectIdentity = ObjectIdentity
aristaDCS7260QX64SSD = _AristaDCS7260QX64SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7260, 3095, 64, 761)
)
_AristaDCS7280TRA48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280TRA48C6M = _AristaDCS7280TRA48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 312, 48, 2878, 6, 972)
)
_AristaDCS7280SRA48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SRA48C6M = _AristaDCS7280SRA48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1347, 48, 2878, 6, 972)
)
_AristaDCS7280TR48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280TR48C6 = _AristaDCS7280TR48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1964, 48, 2878, 6)
)
_AristaDCS7280TR48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280TR48C6M = _AristaDCS7280TR48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 1964, 48, 2878, 6, 972)
)
_AristaDCS7280QRAC72_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC72 = _AristaDCS7280QRAC72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 72)
)
_AristaDCS7280QRAC72M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRAC72M = _AristaDCS7280QRAC72M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2655, 2878, 72, 972)
)
_AristaDCS7280CR48_ObjectIdentity = ObjectIdentity
aristaDCS7280CR48 = _AristaDCS7280CR48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 48)
)
_AristaDCS7280CR48SSD_ObjectIdentity = ObjectIdentity
aristaDCS7280CR48SSD = _AristaDCS7280CR48SSD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 2727, 48, 761)
)
_AristaDCS7280QRC36_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36 = _AristaDCS7280QRC36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36)
)
_AristaDCS7280QRC36M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36M = _AristaDCS7280QRC36M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 972)
)
_AristaDCS7280QRC36S_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36S = _AristaDCS7280QRC36S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 3282)
)
_AristaDCS7280QRC36SM_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC36SM = _AristaDCS7280QRC36SM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 36, 3282, 972)
)
_AristaDCS7280QRC72_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC72 = _AristaDCS7280QRC72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 72)
)
_AristaDCS7280QRC72M_ObjectIdentity = ObjectIdentity
aristaDCS7280QRC72M = _AristaDCS7280QRC72M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3101, 2878, 72, 972)
)
_AristaDCS7280SE64_ObjectIdentity = ObjectIdentity
aristaDCS7280SE64 = _AristaDCS7280SE64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 64)
)
_AristaDCS7280SE68_ObjectIdentity = ObjectIdentity
aristaDCS7280SE68 = _AristaDCS7280SE68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 68)
)
_AristaDCS7280SE72_ObjectIdentity = ObjectIdentity
aristaDCS7280SE72 = _AristaDCS7280SE72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3714, 72)
)
_AristaDCS7280SR248YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR248YC6 = _AristaDCS7280SR248YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 48, 1654, 6)
)
_AristaDCS7280SR248YC6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR248YC6M = _AristaDCS7280SR248YC6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 48, 1654, 6, 972)
)
_AristaDCS7280SR2A48YC6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2A48YC6 = _AristaDCS7280SR2A48YC6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 3648, 48, 1654, 6)
)
_AristaDCS7280SR2A48YC6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR2A48YC6M = _AristaDCS7280SR2A48YC6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 2, 3648, 48, 1654, 6, 972)
)
_AristaDCS7280SR48C6_ObjectIdentity = ObjectIdentity
aristaDCS7280SR48C6 = _AristaDCS7280SR48C6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 48, 2878, 6)
)
_AristaDCS7280SR48C6M_ObjectIdentity = ObjectIdentity
aristaDCS7280SR48C6M = _AristaDCS7280SR48C6M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7280, 3735, 48, 2878, 6, 972)
)
_AristaDCS7304_ObjectIdentity = ObjectIdentity
aristaDCS7304 = _AristaDCS7304_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7304)
)
_AristaDCS7308_ObjectIdentity = ObjectIdentity
aristaDCS7308 = _AristaDCS7308_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7308)
)
_AristaDCS7316_ObjectIdentity = ObjectIdentity
aristaDCS7316 = _AristaDCS7316_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7316)
)
_AristaDCS7504_ObjectIdentity = ObjectIdentity
aristaDCS7504 = _AristaDCS7504_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504)
)
_AristaDCS7504N_ObjectIdentity = ObjectIdentity
aristaDCS7504N = _AristaDCS7504N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7504, 1359)
)
_AristaDCS7508_ObjectIdentity = ObjectIdentity
aristaDCS7508 = _AristaDCS7508_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508)
)
_AristaDCS7508N_ObjectIdentity = ObjectIdentity
aristaDCS7508N = _AristaDCS7508N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7508, 1359)
)
_AristaDCS7512N_ObjectIdentity = ObjectIdentity
aristaDCS7512N = _AristaDCS7512N_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 1, 3011, 7512, 1359)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-PRODUCTS-MIB",
    **{"aristaLY6": aristaLY6,
       "aristaSmallstoneD4040": aristaSmallstoneD4040,
       "aristaCVX": aristaCVX,
       "aristaDCS7010T48": aristaDCS7010T48,
       "aristaDCS7010T48DC": aristaDCS7010T48DC,
       "aristaDCS7020TRA48": aristaDCS7020TRA48,
       "aristaDCS7020TR48": aristaDCS7020TR48,
       "aristaDCS7048T4S": aristaDCS7048T4S,
       "aristaDCS7048TA": aristaDCS7048TA,
       "aristaDCS7050T36": aristaDCS7050T36,
       "aristaDCS7050T52": aristaDCS7050T52,
       "aristaDCS7050T52SSD": aristaDCS7050T52SSD,
       "aristaDCS7050T64": aristaDCS7050T64,
       "aristaDCS7050T64SSD": aristaDCS7050T64SSD,
       "aristaDCS7050TX2128": aristaDCS7050TX2128,
       "aristaDCS7050TX2128SSD": aristaDCS7050TX2128SSD,
       "aristaDCS7050TX48": aristaDCS7050TX48,
       "aristaDCS7050TX48SSD": aristaDCS7050TX48SSD,
       "aristaDCS7050TX64": aristaDCS7050TX64,
       "aristaDCS7050TX64SSD": aristaDCS7050TX64SSD,
       "aristaDCS7050TX72": aristaDCS7050TX72,
       "aristaDCS7050TX72SSD": aristaDCS7050TX72SSD,
       "aristaDCS7050TX72Q": aristaDCS7050TX72Q,
       "aristaDCS7050TX72QSSD": aristaDCS7050TX72QSSD,
       "aristaDCS7050TX96": aristaDCS7050TX96,
       "aristaDCS7050TX96SSD": aristaDCS7050TX96SSD,
       "aristaDCS7050TX128": aristaDCS7050TX128,
       "aristaDCS7050TX128SSD": aristaDCS7050TX128SSD,
       "aristaDCS7050Q16": aristaDCS7050Q16,
       "aristaDCS7050Q16SSD": aristaDCS7050Q16SSD,
       "aristaDCS7050QX232S": aristaDCS7050QX232S,
       "aristaDCS7050QX232SSSD": aristaDCS7050QX232SSSD,
       "aristaDCS7050QX32": aristaDCS7050QX32,
       "aristaDCS7050QX32SSD": aristaDCS7050QX32SSD,
       "aristaDCS7050QX32CLSSD": aristaDCS7050QX32CLSSD,
       "aristaDCS7050QX32S": aristaDCS7050QX32S,
       "aristaDCS7050QX32SSSD": aristaDCS7050QX32SSSD,
       "aristaDCS7050S52": aristaDCS7050S52,
       "aristaDCS7050S52SSD": aristaDCS7050S52SSD,
       "aristaDCS7050S64": aristaDCS7050S64,
       "aristaDCS7050S64SSD": aristaDCS7050S64SSD,
       "aristaDCS7050SX272Q": aristaDCS7050SX272Q,
       "aristaDCS7050SX272QSSD": aristaDCS7050SX272QSSD,
       "aristaDCS7050SX2128": aristaDCS7050SX2128,
       "aristaDCS7050SX2128SSD": aristaDCS7050SX2128SSD,
       "aristaDCS7050SX64": aristaDCS7050SX64,
       "aristaDCS7050SX64SSD": aristaDCS7050SX64SSD,
       "aristaDCS7050SX72": aristaDCS7050SX72,
       "aristaDCS7050SX72SSD": aristaDCS7050SX72SSD,
       "aristaDCS7050SX72Q": aristaDCS7050SX72Q,
       "aristaDCS7050SX72QSSD": aristaDCS7050SX72QSSD,
       "aristaDCS7050SX96": aristaDCS7050SX96,
       "aristaDCS7050SX96SSD": aristaDCS7050SX96SSD,
       "aristaDCS7050SX128": aristaDCS7050SX128,
       "aristaDCS7050SX128SSD": aristaDCS7050SX128SSD,
       "aristaDCS7060CX232S": aristaDCS7060CX232S,
       "aristaDCS7060CX32S": aristaDCS7060CX32S,
       "aristaDCS7060CX32SSSD": aristaDCS7060CX32SSSD,
       "aristaDCS7120T4S": aristaDCS7120T4S,
       "aristaDCS7124FX": aristaDCS7124FX,
       "aristaDCS7124FXCL": aristaDCS7124FXCL,
       "aristaDCS7124S": aristaDCS7124S,
       "aristaDCS7124SX": aristaDCS7124SX,
       "aristaDCS7124SXSSD": aristaDCS7124SXSSD,
       "aristaDCS7140T8S": aristaDCS7140T8S,
       "aristaDCS7148S": aristaDCS7148S,
       "aristaDCS7148SX": aristaDCS7148SX,
       "aristaDCS7150S24": aristaDCS7150S24,
       "aristaDCS7150S24CL": aristaDCS7150S24CL,
       "aristaDCS7150S24CLSSD": aristaDCS7150S24CLSSD,
       "aristaDCS7150S52CL": aristaDCS7150S52CL,
       "aristaDCS7150S52CLSSD": aristaDCS7150S52CLSSD,
       "aristaDCS7150S64CL": aristaDCS7150S64CL,
       "aristaDCS7150S64CLSSD": aristaDCS7150S64CLSSD,
       "aristaDCS716032CQ": aristaDCS716032CQ,
       "aristaDCS716032CQSSD": aristaDCS716032CQSSD,
       "aristaDCS716048YC6": aristaDCS716048YC6,
       "aristaDCS716048YC6SSD": aristaDCS716048YC6SSD,
       "aristaDCS716048TC6": aristaDCS716048TC6,
       "aristaDCS716048TC6SSD": aristaDCS716048TC6SSD,
       "aristaDCS7250QX64": aristaDCS7250QX64,
       "aristaDCS7250QX64SSD": aristaDCS7250QX64SSD,
       "aristaDCS7250QX64M": aristaDCS7250QX64M,
       "aristaDCS7260CX64": aristaDCS7260CX64,
       "aristaDCS7260CX64SSD": aristaDCS7260CX64SSD,
       "aristaDCS7260QX64": aristaDCS7260QX64,
       "aristaDCS7260QX64SSD": aristaDCS7260QX64SSD,
       "aristaDCS7280TRA48C6M": aristaDCS7280TRA48C6M,
       "aristaDCS7280SRA48C6M": aristaDCS7280SRA48C6M,
       "aristaDCS7280TR48C6": aristaDCS7280TR48C6,
       "aristaDCS7280TR48C6M": aristaDCS7280TR48C6M,
       "aristaDCS7280QRAC72": aristaDCS7280QRAC72,
       "aristaDCS7280QRAC72M": aristaDCS7280QRAC72M,
       "aristaDCS7280CR48": aristaDCS7280CR48,
       "aristaDCS7280CR48SSD": aristaDCS7280CR48SSD,
       "aristaDCS7280QRC36": aristaDCS7280QRC36,
       "aristaDCS7280QRC36M": aristaDCS7280QRC36M,
       "aristaDCS7280QRC36S": aristaDCS7280QRC36S,
       "aristaDCS7280QRC36SM": aristaDCS7280QRC36SM,
       "aristaDCS7280QRC72": aristaDCS7280QRC72,
       "aristaDCS7280QRC72M": aristaDCS7280QRC72M,
       "aristaDCS7280SE64": aristaDCS7280SE64,
       "aristaDCS7280SE68": aristaDCS7280SE68,
       "aristaDCS7280SE72": aristaDCS7280SE72,
       "aristaDCS7280SR248YC6": aristaDCS7280SR248YC6,
       "aristaDCS7280SR248YC6M": aristaDCS7280SR248YC6M,
       "aristaDCS7280SR2A48YC6": aristaDCS7280SR2A48YC6,
       "aristaDCS7280SR2A48YC6M": aristaDCS7280SR2A48YC6M,
       "aristaDCS7280SR48C6": aristaDCS7280SR48C6,
       "aristaDCS7280SR48C6M": aristaDCS7280SR48C6M,
       "aristaDCS7304": aristaDCS7304,
       "aristaDCS7308": aristaDCS7308,
       "aristaDCS7316": aristaDCS7316,
       "aristaDCS7504": aristaDCS7504,
       "aristaDCS7504N": aristaDCS7504N,
       "aristaDCS7508": aristaDCS7508,
       "aristaDCS7508N": aristaDCS7508N,
       "aristaDCS7512N": aristaDCS7512N,
       "aristaProductsMIB": aristaProductsMIB}
)
