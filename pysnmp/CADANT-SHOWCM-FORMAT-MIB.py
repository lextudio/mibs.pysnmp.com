# SNMP MIB module (CADANT-SHOWCM-FORMAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-SHOWCM-FORMAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:12 2024
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

(cadExperimental,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadExperimental")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cadShowCmFormatMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20)
)
cadShowCmFormatMib.setRevisions(
        ("2015-09-21 00:00",
         "2013-07-03 00:00",
         "2013-05-31 00:00",
         "2011-12-01 00:00",
         "2010-10-14 00:00",
         "2010-01-28 00:00",
         "2010-01-12 00:00",
         "2009-09-16 00:00",
         "2009-05-15 00:00",
         "2009-04-23 00:00",
         "2008-12-15 00:00",
         "2008-07-16 00:00",
         "2007-12-09 00:00",
         "2006-12-14 00:00",
         "2006-10-16 00:00",
         "2006-04-13 00:00",
         "2006-03-08 00:00",
         "2005-12-21 00:00",
         "2005-11-30 00:00",
         "2005-11-18 00:00",
         "2005-10-18 00:00",
         "2005-09-29 00:00",
         "2005-06-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ShowCmFormatColumnName(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78)
        )
    )
    namedValues = NamedValues(
        *(("bonded", 49),
          ("bonded-actual", 68),
          ("bpi", 56),
          ("cable-mac", 50),
          ("cm-cfg-file", 2),
          ("cm-cfg-file-long", 48),
          ("cm-cpe-ip", 61),
          ("cm-down-pwr", 3),
          ("cm-down-snr", 4),
          ("cm-ip", 63),
          ("cm-mac", 64),
          ("cm-microreflec", 5),
          ("cm-sysdesc", 6),
          ("cm-time-polled", 7),
          ("cm-timing", 8),
          ("cm-type", 43),
          ("cm-up-pwr", 9),
          ("congest-down", 10),
          ("congest-up", 11),
          ("cpe", 12),
          ("cpe-count", 62),
          ("cpe-ip", 58),
          ("cpe-mac", 59),
          ("cpe-type", 60),
          ("crc", 13),
          ("docsis-capability", 39),
          ("docsis-provisioned", 40),
          ("docsis-reg", 14),
          ("ds-last-penalty-time", 71),
          ("ds-penalty-count", 72),
          ("fec-corrected", 15),
          ("fec-good", 16),
          ("fec-percent-uncorrected", 65),
          ("fec-uncorrected", 17),
          ("fec-unerrored", 57),
          ("filter-cm", 41),
          ("flap-last-flap", 18),
          ("flap-prev-state", 19),
          ("flaps-prov", 20),
          ("flaps-ranging", 21),
          ("flaps-reg", 22),
          ("flex-path-id", 42),
          ("fpccm-online", 44),
          ("fpcm-cpe", 53),
          ("fpcm-qos", 45),
          ("fpcm-us-ds-counts", 47),
          ("hcs", 23),
          ("interface", 24),
          ("ip", 25),
          ("l2vpn-id", 66),
          ("l2vpn-qtag", 67),
          ("load-balance-group", 46),
          ("mac", 26),
          ("microreflec", 27),
          ("multiple-uchan", 1),
          ("none", 0),
          ("ofdm-ds-frequency-supported", 77),
          ("ofdm-ds-profiles", 75),
          ("ofdm-modulation-supported", 76),
          ("policed-down", 28),
          ("power-adj", 29),
          ("qos", 30),
          ("qos-primary", 69),
          ("rec-pwr", 31),
          ("response-percent", 32),
          ("service-type-curr", 55),
          ("service-type-prov", 54),
          ("sid", 33),
          ("snr", 34),
          ("state", 35),
          ("timing", 36),
          ("tx-pwr", 70),
          ("uptime", 37),
          ("us-frequency-supported", 78),
          ("us-last-penalty-time", 73),
          ("us-penalty-count", 74),
          ("vendor", 38))
    )



# MIB Managed Objects in the order of their OIDs

_CadShowCmFormatTable_Object = MibTable
cadShowCmFormatTable = _CadShowCmFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1)
)
if mibBuilder.loadTexts:
    cadShowCmFormatTable.setStatus("current")
_CadShowCmFormatEntry_Object = MibTableRow
cadShowCmFormatEntry = _CadShowCmFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1)
)
cadShowCmFormatEntry.setIndexNames(
    (0, "CADANT-SHOWCM-FORMAT-MIB", "cadShowCmFormatName"),
)
if mibBuilder.loadTexts:
    cadShowCmFormatEntry.setStatus("current")


class _CadShowCmFormatName_Type(DisplayString):
    """Custom type cadShowCmFormatName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CadShowCmFormatName_Type.__name__ = "DisplayString"
_CadShowCmFormatName_Object = MibTableColumn
cadShowCmFormatName = _CadShowCmFormatName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 1),
    _CadShowCmFormatName_Type()
)
cadShowCmFormatName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cadShowCmFormatName.setStatus("current")


class _CadShowCmFormatCol1_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol1 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol1_Object = MibTableColumn
cadShowCmFormatCol1 = _CadShowCmFormatCol1_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 2),
    _CadShowCmFormatCol1_Type()
)
cadShowCmFormatCol1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol1.setStatus("current")


class _CadShowCmFormatCol2_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol2 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol2_Object = MibTableColumn
cadShowCmFormatCol2 = _CadShowCmFormatCol2_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 3),
    _CadShowCmFormatCol2_Type()
)
cadShowCmFormatCol2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol2.setStatus("current")


class _CadShowCmFormatCol3_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol3 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol3_Object = MibTableColumn
cadShowCmFormatCol3 = _CadShowCmFormatCol3_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 4),
    _CadShowCmFormatCol3_Type()
)
cadShowCmFormatCol3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol3.setStatus("current")


class _CadShowCmFormatCol4_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol4 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol4_Object = MibTableColumn
cadShowCmFormatCol4 = _CadShowCmFormatCol4_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 5),
    _CadShowCmFormatCol4_Type()
)
cadShowCmFormatCol4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol4.setStatus("current")


class _CadShowCmFormatCol5_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol5 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol5_Object = MibTableColumn
cadShowCmFormatCol5 = _CadShowCmFormatCol5_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 6),
    _CadShowCmFormatCol5_Type()
)
cadShowCmFormatCol5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol5.setStatus("current")


class _CadShowCmFormatCol6_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol6 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol6_Object = MibTableColumn
cadShowCmFormatCol6 = _CadShowCmFormatCol6_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 7),
    _CadShowCmFormatCol6_Type()
)
cadShowCmFormatCol6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol6.setStatus("current")


class _CadShowCmFormatCol7_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol7 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol7_Object = MibTableColumn
cadShowCmFormatCol7 = _CadShowCmFormatCol7_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 8),
    _CadShowCmFormatCol7_Type()
)
cadShowCmFormatCol7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol7.setStatus("current")


class _CadShowCmFormatCol8_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol8 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol8_Object = MibTableColumn
cadShowCmFormatCol8 = _CadShowCmFormatCol8_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 9),
    _CadShowCmFormatCol8_Type()
)
cadShowCmFormatCol8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol8.setStatus("current")


class _CadShowCmFormatCol9_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol9 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol9_Object = MibTableColumn
cadShowCmFormatCol9 = _CadShowCmFormatCol9_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 10),
    _CadShowCmFormatCol9_Type()
)
cadShowCmFormatCol9.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol9.setStatus("current")


class _CadShowCmFormatCol10_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol10 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol10_Object = MibTableColumn
cadShowCmFormatCol10 = _CadShowCmFormatCol10_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 11),
    _CadShowCmFormatCol10_Type()
)
cadShowCmFormatCol10.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol10.setStatus("current")


class _CadShowCmFormatCol11_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol11 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol11_Object = MibTableColumn
cadShowCmFormatCol11 = _CadShowCmFormatCol11_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 12),
    _CadShowCmFormatCol11_Type()
)
cadShowCmFormatCol11.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol11.setStatus("current")


class _CadShowCmFormatCol12_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol12 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol12_Object = MibTableColumn
cadShowCmFormatCol12 = _CadShowCmFormatCol12_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 13),
    _CadShowCmFormatCol12_Type()
)
cadShowCmFormatCol12.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol12.setStatus("current")


class _CadShowCmFormatCol13_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol13 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol13_Object = MibTableColumn
cadShowCmFormatCol13 = _CadShowCmFormatCol13_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 14),
    _CadShowCmFormatCol13_Type()
)
cadShowCmFormatCol13.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol13.setStatus("current")


class _CadShowCmFormatCol14_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol14 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol14_Object = MibTableColumn
cadShowCmFormatCol14 = _CadShowCmFormatCol14_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 15),
    _CadShowCmFormatCol14_Type()
)
cadShowCmFormatCol14.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol14.setStatus("current")


class _CadShowCmFormatCol15_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol15 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol15_Object = MibTableColumn
cadShowCmFormatCol15 = _CadShowCmFormatCol15_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 16),
    _CadShowCmFormatCol15_Type()
)
cadShowCmFormatCol15.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol15.setStatus("current")


class _CadShowCmFormatCol16_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol16 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol16_Object = MibTableColumn
cadShowCmFormatCol16 = _CadShowCmFormatCol16_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 17),
    _CadShowCmFormatCol16_Type()
)
cadShowCmFormatCol16.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol16.setStatus("current")


class _CadShowCmFormatCol17_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol17 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol17_Object = MibTableColumn
cadShowCmFormatCol17 = _CadShowCmFormatCol17_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 18),
    _CadShowCmFormatCol17_Type()
)
cadShowCmFormatCol17.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol17.setStatus("current")


class _CadShowCmFormatCol18_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol18 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol18_Object = MibTableColumn
cadShowCmFormatCol18 = _CadShowCmFormatCol18_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 19),
    _CadShowCmFormatCol18_Type()
)
cadShowCmFormatCol18.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol18.setStatus("current")


class _CadShowCmFormatCol19_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol19 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol19_Object = MibTableColumn
cadShowCmFormatCol19 = _CadShowCmFormatCol19_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 20),
    _CadShowCmFormatCol19_Type()
)
cadShowCmFormatCol19.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol19.setStatus("current")


class _CadShowCmFormatCol20_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol20 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol20_Object = MibTableColumn
cadShowCmFormatCol20 = _CadShowCmFormatCol20_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 21),
    _CadShowCmFormatCol20_Type()
)
cadShowCmFormatCol20.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol20.setStatus("current")


class _CadShowCmFormatCol21_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol21 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol21_Object = MibTableColumn
cadShowCmFormatCol21 = _CadShowCmFormatCol21_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 22),
    _CadShowCmFormatCol21_Type()
)
cadShowCmFormatCol21.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol21.setStatus("current")


class _CadShowCmFormatCol22_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol22 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol22_Object = MibTableColumn
cadShowCmFormatCol22 = _CadShowCmFormatCol22_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 23),
    _CadShowCmFormatCol22_Type()
)
cadShowCmFormatCol22.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol22.setStatus("current")


class _CadShowCmFormatCol23_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol23 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol23_Object = MibTableColumn
cadShowCmFormatCol23 = _CadShowCmFormatCol23_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 24),
    _CadShowCmFormatCol23_Type()
)
cadShowCmFormatCol23.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol23.setStatus("current")


class _CadShowCmFormatCol24_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol24 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol24_Object = MibTableColumn
cadShowCmFormatCol24 = _CadShowCmFormatCol24_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 25),
    _CadShowCmFormatCol24_Type()
)
cadShowCmFormatCol24.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol24.setStatus("current")


class _CadShowCmFormatCol25_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol25 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol25_Object = MibTableColumn
cadShowCmFormatCol25 = _CadShowCmFormatCol25_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 26),
    _CadShowCmFormatCol25_Type()
)
cadShowCmFormatCol25.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol25.setStatus("current")


class _CadShowCmFormatCol26_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol26 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol26_Object = MibTableColumn
cadShowCmFormatCol26 = _CadShowCmFormatCol26_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 27),
    _CadShowCmFormatCol26_Type()
)
cadShowCmFormatCol26.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol26.setStatus("current")


class _CadShowCmFormatCol27_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol27 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol27_Object = MibTableColumn
cadShowCmFormatCol27 = _CadShowCmFormatCol27_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 28),
    _CadShowCmFormatCol27_Type()
)
cadShowCmFormatCol27.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol27.setStatus("current")


class _CadShowCmFormatCol28_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol28 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol28_Object = MibTableColumn
cadShowCmFormatCol28 = _CadShowCmFormatCol28_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 29),
    _CadShowCmFormatCol28_Type()
)
cadShowCmFormatCol28.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol28.setStatus("current")


class _CadShowCmFormatCol29_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol29 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol29_Object = MibTableColumn
cadShowCmFormatCol29 = _CadShowCmFormatCol29_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 30),
    _CadShowCmFormatCol29_Type()
)
cadShowCmFormatCol29.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol29.setStatus("current")


class _CadShowCmFormatCol30_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol30 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol30_Object = MibTableColumn
cadShowCmFormatCol30 = _CadShowCmFormatCol30_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 31),
    _CadShowCmFormatCol30_Type()
)
cadShowCmFormatCol30.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol30.setStatus("current")


class _CadShowCmFormatCol31_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol31 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol31_Object = MibTableColumn
cadShowCmFormatCol31 = _CadShowCmFormatCol31_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 32),
    _CadShowCmFormatCol31_Type()
)
cadShowCmFormatCol31.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol31.setStatus("current")


class _CadShowCmFormatCol32_Type(ShowCmFormatColumnName):
    """Custom type cadShowCmFormatCol32 based on ShowCmFormatColumnName"""


_CadShowCmFormatCol32_Object = MibTableColumn
cadShowCmFormatCol32 = _CadShowCmFormatCol32_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 33),
    _CadShowCmFormatCol32_Type()
)
cadShowCmFormatCol32.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatCol32.setStatus("current")


class _CadShowCmFormatMultiRows_Type(Integer32):
    """Custom type cadShowCmFormatMultiRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("multiple-uchan", 1)
    )


_CadShowCmFormatMultiRows_Type.__name__ = "Integer32"
_CadShowCmFormatMultiRows_Object = MibTableColumn
cadShowCmFormatMultiRows = _CadShowCmFormatMultiRows_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 34),
    _CadShowCmFormatMultiRows_Type()
)
cadShowCmFormatMultiRows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatMultiRows.setStatus("current")


class _CadShowCmFormatRowStatus_Type(RowStatus):
    """Custom type cadShowCmFormatRowStatus based on RowStatus"""


_CadShowCmFormatRowStatus_Object = MibTableColumn
cadShowCmFormatRowStatus = _CadShowCmFormatRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 100, 20, 1, 1, 80),
    _CadShowCmFormatRowStatus_Type()
)
cadShowCmFormatRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadShowCmFormatRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-SHOWCM-FORMAT-MIB",
    **{"ShowCmFormatColumnName": ShowCmFormatColumnName,
       "cadShowCmFormatMib": cadShowCmFormatMib,
       "cadShowCmFormatTable": cadShowCmFormatTable,
       "cadShowCmFormatEntry": cadShowCmFormatEntry,
       "cadShowCmFormatName": cadShowCmFormatName,
       "cadShowCmFormatCol1": cadShowCmFormatCol1,
       "cadShowCmFormatCol2": cadShowCmFormatCol2,
       "cadShowCmFormatCol3": cadShowCmFormatCol3,
       "cadShowCmFormatCol4": cadShowCmFormatCol4,
       "cadShowCmFormatCol5": cadShowCmFormatCol5,
       "cadShowCmFormatCol6": cadShowCmFormatCol6,
       "cadShowCmFormatCol7": cadShowCmFormatCol7,
       "cadShowCmFormatCol8": cadShowCmFormatCol8,
       "cadShowCmFormatCol9": cadShowCmFormatCol9,
       "cadShowCmFormatCol10": cadShowCmFormatCol10,
       "cadShowCmFormatCol11": cadShowCmFormatCol11,
       "cadShowCmFormatCol12": cadShowCmFormatCol12,
       "cadShowCmFormatCol13": cadShowCmFormatCol13,
       "cadShowCmFormatCol14": cadShowCmFormatCol14,
       "cadShowCmFormatCol15": cadShowCmFormatCol15,
       "cadShowCmFormatCol16": cadShowCmFormatCol16,
       "cadShowCmFormatCol17": cadShowCmFormatCol17,
       "cadShowCmFormatCol18": cadShowCmFormatCol18,
       "cadShowCmFormatCol19": cadShowCmFormatCol19,
       "cadShowCmFormatCol20": cadShowCmFormatCol20,
       "cadShowCmFormatCol21": cadShowCmFormatCol21,
       "cadShowCmFormatCol22": cadShowCmFormatCol22,
       "cadShowCmFormatCol23": cadShowCmFormatCol23,
       "cadShowCmFormatCol24": cadShowCmFormatCol24,
       "cadShowCmFormatCol25": cadShowCmFormatCol25,
       "cadShowCmFormatCol26": cadShowCmFormatCol26,
       "cadShowCmFormatCol27": cadShowCmFormatCol27,
       "cadShowCmFormatCol28": cadShowCmFormatCol28,
       "cadShowCmFormatCol29": cadShowCmFormatCol29,
       "cadShowCmFormatCol30": cadShowCmFormatCol30,
       "cadShowCmFormatCol31": cadShowCmFormatCol31,
       "cadShowCmFormatCol32": cadShowCmFormatCol32,
       "cadShowCmFormatMultiRows": cadShowCmFormatMultiRows,
       "cadShowCmFormatRowStatus": cadShowCmFormatRowStatus}
)
