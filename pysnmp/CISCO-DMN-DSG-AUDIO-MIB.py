# SNMP MIB module (CISCO-DMN-DSG-AUDIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-AUDIO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:15 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoDSGAudio = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15)
)
ciscoDSGAudio.setRevisions(
        ("2013-07-10 12:20",
         "2012-03-07 05:00",
         "2010-08-30 05:00",
         "2010-05-24 06:30",
         "2010-05-21 16:45",
         "2010-04-12 05:00",
         "2010-03-22 05:00",
         "2010-02-12 15:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AudioCtrlTable_Object = MibTable
audioCtrlTable = _AudioCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1)
)
if mibBuilder.loadTexts:
    audioCtrlTable.setStatus("current")
_AudioCtrlEntry_Object = MibTableRow
audioCtrlEntry = _AudioCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1)
)
audioCtrlEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-AUDIO-MIB", "audioSelKey"),
)
if mibBuilder.loadTexts:
    audioCtrlEntry.setStatus("current")


class _AudioSelKey_Type(Integer32):
    """Custom type audioSelKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AudioSelKey_Type.__name__ = "Integer32"
_AudioSelKey_Object = MibTableColumn
audioSelKey = _AudioSelKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 1),
    _AudioSelKey_Type()
)
audioSelKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSelKey.setStatus("current")


class _AudioMode_Type(Integer32):
    """Custom type audioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("lMono", 3),
          ("mixed", 2),
          ("rMono", 4),
          ("stereo", 1))
    )


_AudioMode_Type.__name__ = "Integer32"
_AudioMode_Object = MibTableColumn
audioMode = _AudioMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 2),
    _AudioMode_Type()
)
audioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioMode.setStatus("current")


class _AudioDolbyDigitalComp_Type(Integer32):
    """Custom type audioDolbyDigitalComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("custom0", 4),
          ("custom1", 3),
          ("lineMode", 2),
          ("rfMode", 1))
    )


_AudioDolbyDigitalComp_Type.__name__ = "Integer32"
_AudioDolbyDigitalComp_Object = MibTableColumn
audioDolbyDigitalComp = _AudioDolbyDigitalComp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 3),
    _AudioDolbyDigitalComp_Type()
)
audioDolbyDigitalComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDolbyDigitalComp.setStatus("current")


class _AudioConsumerVolLeft_Type(Integer32):
    """Custom type audioConsumerVolLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AudioConsumerVolLeft_Type.__name__ = "Integer32"
_AudioConsumerVolLeft_Object = MibTableColumn
audioConsumerVolLeft = _AudioConsumerVolLeft_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 4),
    _AudioConsumerVolLeft_Type()
)
audioConsumerVolLeft.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioConsumerVolLeft.setStatus("current")


class _AudioConsumerVolRight_Type(Integer32):
    """Custom type audioConsumerVolRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AudioConsumerVolRight_Type.__name__ = "Integer32"
_AudioConsumerVolRight_Object = MibTableColumn
audioConsumerVolRight = _AudioConsumerVolRight_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 5),
    _AudioConsumerVolRight_Type()
)
audioConsumerVolRight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioConsumerVolRight.setStatus("current")


class _AudioProfAttenuationLeft_Type(Integer32):
    """Custom type audioProfAttenuationLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AudioProfAttenuationLeft_Type.__name__ = "Integer32"
_AudioProfAttenuationLeft_Object = MibTableColumn
audioProfAttenuationLeft = _AudioProfAttenuationLeft_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 6),
    _AudioProfAttenuationLeft_Type()
)
audioProfAttenuationLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioProfAttenuationLeft.setStatus("current")


class _AudioProfAttenuationRight_Type(Integer32):
    """Custom type audioProfAttenuationRight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AudioProfAttenuationRight_Type.__name__ = "Integer32"
_AudioProfAttenuationRight_Object = MibTableColumn
audioProfAttenuationRight = _AudioProfAttenuationRight_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 7),
    _AudioProfAttenuationRight_Type()
)
audioProfAttenuationRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioProfAttenuationRight.setStatus("current")


class _AudioPmtSource_Type(Integer32):
    """Custom type audioPmtSource based on Integer32"""
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
              51,
              52,
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
              65)
        )
    )
    namedValues = NamedValues(
        *(("aud1", 2),
          ("aud10", 11),
          ("aud11", 12),
          ("aud12", 13),
          ("aud13", 14),
          ("aud14", 15),
          ("aud15", 16),
          ("aud16", 17),
          ("aud17", 18),
          ("aud18", 19),
          ("aud19", 20),
          ("aud2", 3),
          ("aud20", 21),
          ("aud21", 22),
          ("aud22", 23),
          ("aud23", 24),
          ("aud24", 25),
          ("aud25", 26),
          ("aud26", 27),
          ("aud27", 28),
          ("aud28", 29),
          ("aud29", 30),
          ("aud3", 4),
          ("aud30", 31),
          ("aud31", 32),
          ("aud32", 33),
          ("aud33", 34),
          ("aud34", 35),
          ("aud35", 36),
          ("aud36", 37),
          ("aud37", 38),
          ("aud38", 39),
          ("aud39", 40),
          ("aud4", 5),
          ("aud40", 41),
          ("aud41", 42),
          ("aud42", 43),
          ("aud43", 44),
          ("aud44", 45),
          ("aud45", 46),
          ("aud46", 47),
          ("aud47", 48),
          ("aud48", 49),
          ("aud49", 50),
          ("aud5", 6),
          ("aud50", 51),
          ("aud51", 52),
          ("aud52", 53),
          ("aud53", 54),
          ("aud54", 55),
          ("aud55", 56),
          ("aud56", 57),
          ("aud57", 58),
          ("aud58", 59),
          ("aud59", 60),
          ("aud6", 7),
          ("aud60", 61),
          ("aud61", 62),
          ("aud62", 63),
          ("aud63", 64),
          ("aud64", 65),
          ("aud7", 8),
          ("aud8", 9),
          ("aud9", 10),
          ("none", 1))
    )


_AudioPmtSource_Type.__name__ = "Integer32"
_AudioPmtSource_Object = MibTableColumn
audioPmtSource = _AudioPmtSource_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 8),
    _AudioPmtSource_Type()
)
audioPmtSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioPmtSource.setStatus("current")


class _AudioMuted_Type(Integer32):
    """Custom type audioMuted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AudioMuted_Type.__name__ = "Integer32"
_AudioMuted_Object = MibTableColumn
audioMuted = _AudioMuted_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 9),
    _AudioMuted_Type()
)
audioMuted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioMuted.setStatus("current")


class _AudioDigitalComp_Type(Integer32):
    """Custom type audioDigitalComp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compressed", 2),
          ("pcm", 1))
    )


_AudioDigitalComp_Type.__name__ = "Integer32"
_AudioDigitalComp_Object = MibTableColumn
audioDigitalComp = _AudioDigitalComp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 10),
    _AudioDigitalComp_Type()
)
audioDigitalComp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDigitalComp.setStatus("current")


class _AudioDolbyDigitalPlusMode_Type(Integer32):
    """Custom type audioDolbyDigitalPlusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("passthrough", 2),
          ("transcoding", 1))
    )


_AudioDolbyDigitalPlusMode_Type.__name__ = "Integer32"
_AudioDolbyDigitalPlusMode_Object = MibTableColumn
audioDolbyDigitalPlusMode = _AudioDolbyDigitalPlusMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 11),
    _AudioDolbyDigitalPlusMode_Type()
)
audioDolbyDigitalPlusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDolbyDigitalPlusMode.setStatus("current")


class _AudioLangMenu_Type(Integer32):
    """Custom type audioLangMenu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("languageEntry", 2),
          ("languageList", 1),
          ("pmtOrder", 3))
    )


_AudioLangMenu_Type.__name__ = "Integer32"
_AudioLangMenu_Object = MibTableColumn
audioLangMenu = _AudioLangMenu_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 12),
    _AudioLangMenu_Type()
)
audioLangMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLangMenu.setStatus("current")


class _AudioLangList_Type(Integer32):
    """Custom type audioLangList based on Integer32"""
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
              43)
        )
    )
    namedValues = NamedValues(
        *(("ara", 1),
          ("ben", 3),
          ("btk", 2),
          ("bul", 4),
          ("chi", 5),
          ("cze", 6),
          ("dan", 7),
          ("dut", 8),
          ("eng", 9),
          ("fin", 10),
          ("fre", 11),
          ("ger", 12),
          ("gre", 13),
          ("heb", 14),
          ("hin", 15),
          ("hun", 16),
          ("ice", 17),
          ("ind", 18),
          ("ita", 19),
          ("jpn", 20),
          ("kor", 21),
          ("may", 22),
          ("mul", 23),
          ("nor", 24),
          ("per", 25),
          ("pol", 26),
          ("por", 27),
          ("rum", 28),
          ("rus", 29),
          ("san", 30),
          ("scc", 31),
          ("sin", 32),
          ("slo", 33),
          ("slv", 34),
          ("som", 35),
          ("spa", 36),
          ("swe", 37),
          ("tai", 38),
          ("tam", 39),
          ("tha", 40),
          ("tur", 41),
          ("ukr", 42),
          ("vie", 43))
    )


_AudioLangList_Type.__name__ = "Integer32"
_AudioLangList_Object = MibTableColumn
audioLangList = _AudioLangList_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 13),
    _AudioLangList_Type()
)
audioLangList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLangList.setStatus("current")


class _AudioManualEntry_Type(DisplayString):
    """Custom type audioManualEntry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AudioManualEntry_Type.__name__ = "DisplayString"
_AudioManualEntry_Object = MibTableColumn
audioManualEntry = _AudioManualEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 1, 1, 14),
    _AudioManualEntry_Type()
)
audioManualEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioManualEntry.setStatus("current")
_AudioStatusTable_Object = MibTable
audioStatusTable = _AudioStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2)
)
if mibBuilder.loadTexts:
    audioStatusTable.setStatus("current")
_AudioStatusEntry_Object = MibTableRow
audioStatusEntry = _AudioStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1)
)
audioStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-AUDIO-MIB", "audioStatusSelKey"),
)
if mibBuilder.loadTexts:
    audioStatusEntry.setStatus("current")


class _AudioStatusSelKey_Type(Integer32):
    """Custom type audioStatusSelKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AudioStatusSelKey_Type.__name__ = "Integer32"
_AudioStatusSelKey_Object = MibTableColumn
audioStatusSelKey = _AudioStatusSelKey_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 1),
    _AudioStatusSelKey_Type()
)
audioStatusSelKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audioStatusSelKey.setStatus("current")


class _AudioStatusFormat_Type(Integer32):
    """Custom type audioStatusFormat based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("adtsAAC", 11),
          ("adtsHEAAC", 13),
          ("beep", 4),
          ("dolbyDigital", 9),
          ("dolbyDigitalPlus", 12),
          ("loasAAC", 10),
          ("loasHEAAC", 14),
          ("mpeg1L1", 5),
          ("mpeg1L2", 6),
          ("mpeg2L1", 7),
          ("mpeg2L2", 8),
          ("none", 1),
          ("pink", 3),
          ("sine", 2))
    )


_AudioStatusFormat_Type.__name__ = "Integer32"
_AudioStatusFormat_Object = MibTableColumn
audioStatusFormat = _AudioStatusFormat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 2),
    _AudioStatusFormat_Type()
)
audioStatusFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusFormat.setStatus("current")


class _AudioStatusBitRate_Type(DisplayString):
    """Custom type audioStatusBitRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AudioStatusBitRate_Type.__name__ = "DisplayString"
_AudioStatusBitRate_Object = MibTableColumn
audioStatusBitRate = _AudioStatusBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 3),
    _AudioStatusBitRate_Type()
)
audioStatusBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusBitRate.setStatus("current")


class _AudioStatusBufferLevel_Type(DisplayString):
    """Custom type audioStatusBufferLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AudioStatusBufferLevel_Type.__name__ = "DisplayString"
_AudioStatusBufferLevel_Object = MibTableColumn
audioStatusBufferLevel = _AudioStatusBufferLevel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 4),
    _AudioStatusBufferLevel_Type()
)
audioStatusBufferLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusBufferLevel.setStatus("current")


class _AudioStatusSFR_Type(DisplayString):
    """Custom type audioStatusSFR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AudioStatusSFR_Type.__name__ = "DisplayString"
_AudioStatusSFR_Object = MibTableColumn
audioStatusSFR = _AudioStatusSFR_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 5),
    _AudioStatusSFR_Type()
)
audioStatusSFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusSFR.setStatus("current")


class _AudioStatusMuted_Type(Integer32):
    """Custom type audioStatusMuted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_AudioStatusMuted_Type.__name__ = "Integer32"
_AudioStatusMuted_Object = MibTableColumn
audioStatusMuted = _AudioStatusMuted_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 6),
    _AudioStatusMuted_Type()
)
audioStatusMuted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusMuted.setStatus("current")


class _AudioStatusLanguage_Type(DisplayString):
    """Custom type audioStatusLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AudioStatusLanguage_Type.__name__ = "DisplayString"
_AudioStatusLanguage_Object = MibTableColumn
audioStatusLanguage = _AudioStatusLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 7),
    _AudioStatusLanguage_Type()
)
audioStatusLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusLanguage.setStatus("current")


class _AudioStatusDDPMode_Type(Integer32):
    """Custom type audioStatusDDPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddp", 2),
          ("off", 1))
    )


_AudioStatusDDPMode_Type.__name__ = "Integer32"
_AudioStatusDDPMode_Object = MibTableColumn
audioStatusDDPMode = _AudioStatusDDPMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 8),
    _AudioStatusDDPMode_Type()
)
audioStatusDDPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusDDPMode.setStatus("current")


class _AudioStatusDualMonoMode_Type(Integer32):
    """Custom type audioStatusDualMonoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dualMono", 2),
          ("off", 1))
    )


_AudioStatusDualMonoMode_Type.__name__ = "Integer32"
_AudioStatusDualMonoMode_Object = MibTableColumn
audioStatusDualMonoMode = _AudioStatusDualMonoMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 15, 2, 1, 9),
    _AudioStatusDualMonoMode_Type()
)
audioStatusDualMonoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioStatusDualMonoMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-AUDIO-MIB",
    **{"ciscoDSGAudio": ciscoDSGAudio,
       "audioCtrlTable": audioCtrlTable,
       "audioCtrlEntry": audioCtrlEntry,
       "audioSelKey": audioSelKey,
       "audioMode": audioMode,
       "audioDolbyDigitalComp": audioDolbyDigitalComp,
       "audioConsumerVolLeft": audioConsumerVolLeft,
       "audioConsumerVolRight": audioConsumerVolRight,
       "audioProfAttenuationLeft": audioProfAttenuationLeft,
       "audioProfAttenuationRight": audioProfAttenuationRight,
       "audioPmtSource": audioPmtSource,
       "audioMuted": audioMuted,
       "audioDigitalComp": audioDigitalComp,
       "audioDolbyDigitalPlusMode": audioDolbyDigitalPlusMode,
       "audioLangMenu": audioLangMenu,
       "audioLangList": audioLangList,
       "audioManualEntry": audioManualEntry,
       "audioStatusTable": audioStatusTable,
       "audioStatusEntry": audioStatusEntry,
       "audioStatusSelKey": audioStatusSelKey,
       "audioStatusFormat": audioStatusFormat,
       "audioStatusBitRate": audioStatusBitRate,
       "audioStatusBufferLevel": audioStatusBufferLevel,
       "audioStatusSFR": audioStatusSFR,
       "audioStatusMuted": audioStatusMuted,
       "audioStatusLanguage": audioStatusLanguage,
       "audioStatusDDPMode": audioStatusDDPMode,
       "audioStatusDualMonoMode": audioStatusDualMonoMode}
)
