# SNMP MIB module (LEXMARK-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEXMARK-TC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:49 2024
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

(lexmarkModules,) = mibBuilder.importSymbols(
    "LEXMARK-ROOT-MIB",
    "lexmarkModules")

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

lexmarkTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 641, 4, 2)
)
lexmarkTCMIB.setRevisions(
        ("2010-12-20 23:00",
         "2009-11-24 20:40")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UnitsTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41)
        )
    )
    namedValues = NamedValues(
        *(("centimeters", 17),
          ("days", 38),
          ("feet", 20),
          ("grams", 21),
          ("hours", 37),
          ("inches", 19),
          ("items", 3),
          ("meters", 18),
          ("microseconds", 33),
          ("millimeters", 16),
          ("milliseconds", 34),
          ("minutes", 36),
          ("months", 40),
          ("nanoseconds", 32),
          ("other", 2),
          ("ounces", 22),
          ("seconds", 35),
          ("sheets", 5),
          ("sides", 4),
          ("unknown", 1),
          ("weeks", 39),
          ("years", 41))
    )



class PaperSizeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              32,
              33,
              34,
              35,
              36,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              136,
              137,
              138,
              139,
              140,
              141,
              142)
        )
    )
    namedValues = NamedValues(
        *(("bookOriginal", 19),
          ("businessCard", 15),
          ("card3x5", 17),
          ("card4x6", 18),
          ("custom", 4),
          ("envelope10", 34),
          ("envelope7threequarters", 32),
          ("envelope9", 33),
          ("envelopeDL", 35),
          ("envelopeOther", 36),
          ("executive", 10),
          ("folio", 11),
          ("hagaki", 20),
          ("idCard", 16),
          ("isoA0", 64),
          ("isoA1", 65),
          ("isoA2", 66),
          ("isoA3", 67),
          ("isoA4", 68),
          ("isoA5", 69),
          ("isoA6", 70),
          ("isoB0", 72),
          ("isoB1", 73),
          ("isoB2", 74),
          ("isoB3", 75),
          ("isoB4", 76),
          ("isoB5", 77),
          ("isoB6", 78),
          ("isoC0", 80),
          ("isoC1", 81),
          ("isoC2", 82),
          ("isoC3", 83),
          ("isoC4", 84),
          ("isoC5", 85),
          ("isoC6", 86),
          ("isoEnvelopeA0", 96),
          ("isoEnvelopeA1", 97),
          ("isoEnvelopeA2", 98),
          ("isoEnvelopeA3", 99),
          ("isoEnvelopeA4", 100),
          ("isoEnvelopeA5", 101),
          ("isoEnvelopeA6", 102),
          ("isoEnvelopeB0", 104),
          ("isoEnvelopeB1", 105),
          ("isoEnvelopeB2", 106),
          ("isoEnvelopeB3", 107),
          ("isoEnvelopeB4", 108),
          ("isoEnvelopeB5", 109),
          ("isoEnvelopeB6", 110),
          ("isoEnvelopeC0", 112),
          ("isoEnvelopeC1", 113),
          ("isoEnvelopeC2", 114),
          ("isoEnvelopeC3", 115),
          ("isoEnvelopeC4", 116),
          ("isoEnvelopeC5", 117),
          ("isoEnvelopeC6", 118),
          ("jisB0", 136),
          ("jisB1", 137),
          ("jisB2", 138),
          ("jisB3", 139),
          ("jisB4", 140),
          ("jisB5", 141),
          ("jisB6", 142),
          ("legal", 9),
          ("letter", 8),
          ("oficio", 13),
          ("other", 2),
          ("statement", 12),
          ("tabloid", 14),
          ("universal", 3),
          ("unknown", 1))
    )



class PaperTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bond", 9),
          ("cardstock", 4),
          ("colored", 12),
          ("customtype1", 32),
          ("customtype2", 33),
          ("customtype3", 34),
          ("customtype4", 35),
          ("customtype5", 36),
          ("customtype6", 37),
          ("envelope", 16),
          ("heavy", 14),
          ("labels", 7),
          ("letterhead", 10),
          ("light", 13),
          ("other", 2),
          ("plain", 3),
          ("preprinted", 11),
          ("recycled", 6),
          ("roughOrCotton", 15),
          ("transparancy", 5),
          ("unknown", 1),
          ("vinylLabels", 8))
    )



class AdminStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 5),
          ("other", 3),
          ("unknown", 1),
          ("up", 4))
    )



class StatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              17,
              18,
              19,
              20,
              21,
              22,
              33,
              34,
              35,
              36,
              37,
              38,
              97,
              98,
              99,
              100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("broken", 6),
          ("disabledBroken", 22),
          ("disabledOffline", 20),
          ("disabledOk", 19),
          ("disabledOther", 18),
          ("disabledUnknown", 17),
          ("disabledWarning", 21),
          ("licensedBroken", 102),
          ("licensedOffline", 100),
          ("licensedOk", 99),
          ("licensedOther", 98),
          ("licensedUnknown", 97),
          ("licensedWarning", 101),
          ("offline", 4),
          ("ok", 3),
          ("other", 2),
          ("unknown", 1),
          ("unlicensedBroken", 38),
          ("unlicensedOffline", 36),
          ("unlicensedOk", 35),
          ("unlicensedOther", 34),
          ("unlicensedUnknown", 33),
          ("unlicensedWarning", 37),
          ("warning", 5))
    )



class KeyValueTC(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEXMARK-TC-MIB",
    **{"UnitsTC": UnitsTC,
       "PaperSizeTC": PaperSizeTC,
       "PaperTypeTC": PaperTypeTC,
       "AdminStatusTC": AdminStatusTC,
       "StatusTC": StatusTC,
       "KeyValueTC": KeyValueTC,
       "lexmarkTCMIB": lexmarkTCMIB}
)
