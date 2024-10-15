# SNMP MIB module (OMNITEK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNITEK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:42 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class AudioStatus(Integer32):
    """Custom type AudioStatus based on Integer32"""
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
        *(("active", 3),
          ("missing", 1),
          ("peak", 4),
          ("silent", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Omnitek_ObjectIdentity = ObjectIdentity
omnitek = _Omnitek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458)
)
_Videostatus_ObjectIdentity = ObjectIdentity
videostatus = _Videostatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 1)
)


class _VideoStandard_Type(Integer32):
    """Custom type videoStandard based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("format1035i59", 7),
          ("format1035i60", 8),
          ("format1080i50", 13),
          ("format1080i59", 15),
          ("format1080i60", 17),
          ("format1080p23", 10),
          ("format1080p24", 12),
          ("format1080p25", 14),
          ("format1080p29", 16),
          ("format1080p30", 18),
          ("format1080sf23", 9),
          ("format1080sf23rgb444lin", 27),
          ("format1080sf23rgb444log", 26),
          ("format1080sf23yuv444", 28),
          ("format1080sf24", 11),
          ("format1080sf24rgb444lin", 30),
          ("format1080sf24rgb444log", 29),
          ("format1080sf24yuv444", 31),
          ("format486i59", 1),
          ("format486p59", 2),
          ("format576i50", 3),
          ("format576p50", 4),
          ("format720p23", 19),
          ("format720p24", 20),
          ("format720p25", 21),
          ("format720p29", 22),
          ("format720p30", 23),
          ("format720p50", 24),
          ("format720p59", 5),
          ("format720p60", 6))
    )


_VideoStandard_Type.__name__ = "Integer32"
_VideoStandard_Object = MibScalar
videoStandard = _VideoStandard_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 1),
    _VideoStandard_Type()
)
videoStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoStandard.setStatus("mandatory")


class _DigitalInput_Type(Integer32):
    """Custom type digitalInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("missing", 1),
          ("ok", 3))
    )


_DigitalInput_Type.__name__ = "Integer32"
_DigitalInput_Object = MibScalar
digitalInput = _DigitalInput_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 2),
    _DigitalInput_Type()
)
digitalInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInput.setStatus("mandatory")


class _DigitalInputB_Type(Integer32):
    """Custom type digitalInputB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("missing", 1),
          ("ok", 3))
    )


_DigitalInputB_Type.__name__ = "Integer32"
_DigitalInputB_Object = MibScalar
digitalInputB = _DigitalInputB_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 3),
    _DigitalInputB_Type()
)
digitalInputB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalInputB.setStatus("mandatory")


class _MotionContent_Type(Integer32):
    """Custom type motionContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("frozen", 1))
    )


_MotionContent_Type.__name__ = "Integer32"
_MotionContent_Object = MibScalar
motionContent = _MotionContent_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 4),
    _MotionContent_Type()
)
motionContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motionContent.setStatus("mandatory")


class _LumaContent_Type(Integer32):
    """Custom type lumaContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("black", 1))
    )


_LumaContent_Type.__name__ = "Integer32"
_LumaContent_Object = MibScalar
lumaContent = _LumaContent_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 5),
    _LumaContent_Type()
)
lumaContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lumaContent.setStatus("mandatory")


class _ChromaContent_Type(Integer32):
    """Custom type chromaContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("monochrome", 1))
    )


_ChromaContent_Type.__name__ = "Integer32"
_ChromaContent_Object = MibScalar
chromaContent = _ChromaContent_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 6),
    _ChromaContent_Type()
)
chromaContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chromaContent.setStatus("mandatory")


class _SyncStatus_Type(Integer32):
    """Custom type syncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("missing", 1),
          ("ok", 3))
    )


_SyncStatus_Type.__name__ = "Integer32"
_SyncStatus_Object = MibScalar
syncStatus = _SyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 18458, 1, 7),
    _SyncStatus_Type()
)
syncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syncStatus.setStatus("mandatory")
_Videoindex_ObjectIdentity = ObjectIdentity
videoindex = _Videoindex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 2)
)
_ActiveFormat_Type = DisplayString
_ActiveFormat_Object = MibScalar
activeFormat = _ActiveFormat_Object(
    (1, 3, 6, 1, 4, 1, 18458, 2, 1),
    _ActiveFormat_Type()
)
activeFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFormat.setStatus("mandatory")
_CodedFrame_Type = DisplayString
_CodedFrame_Object = MibScalar
codedFrame = _CodedFrame_Object(
    (1, 3, 6, 1, 4, 1, 18458, 2, 2),
    _CodedFrame_Type()
)
codedFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codedFrame.setStatus("mandatory")
_ComponentSet_Type = DisplayString
_ComponentSet_Object = MibScalar
componentSet = _ComponentSet_Object(
    (1, 3, 6, 1, 4, 1, 18458, 2, 3),
    _ComponentSet_Type()
)
componentSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentSet.setStatus("mandatory")
_SampleStructure_Type = DisplayString
_SampleStructure_Object = MibScalar
sampleStructure = _SampleStructure_Object(
    (1, 3, 6, 1, 4, 1, 18458, 2, 4),
    _SampleStructure_Type()
)
sampleStructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sampleStructure.setStatus("mandatory")
_Wss_ObjectIdentity = ObjectIdentity
wss = _Wss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 3)
)


class _WssReadType_Type(Integer32):
    """Custom type wssReadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ardspec", 2),
          ("en300294", 1))
    )


_WssReadType_Type.__name__ = "Integer32"
_WssReadType_Object = MibScalar
wssReadType = _WssReadType_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 1),
    _WssReadType_Type()
)
wssReadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wssReadType.setStatus("mandatory")
_AspectRatioEN300294_Type = DisplayString
_AspectRatioEN300294_Object = MibScalar
aspectRatioEN300294 = _AspectRatioEN300294_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 2),
    _AspectRatioEN300294_Type()
)
aspectRatioEN300294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioEN300294.setStatus("mandatory")
_EnhancedServicesEN300294_Type = DisplayString
_EnhancedServicesEN300294_Object = MibScalar
enhancedServicesEN300294 = _EnhancedServicesEN300294_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 3),
    _EnhancedServicesEN300294_Type()
)
enhancedServicesEN300294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enhancedServicesEN300294.setStatus("mandatory")
_SubtitlesEN300294_Type = DisplayString
_SubtitlesEN300294_Object = MibScalar
subtitlesEN300294 = _SubtitlesEN300294_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 4),
    _SubtitlesEN300294_Type()
)
subtitlesEN300294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subtitlesEN300294.setStatus("mandatory")
_OthersEN300294_Type = DisplayString
_OthersEN300294_Object = MibScalar
othersEN300294 = _OthersEN300294_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 5),
    _OthersEN300294_Type()
)
othersEN300294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    othersEN300294.setStatus("mandatory")
_AspectRatioARDSPEC_Type = DisplayString
_AspectRatioARDSPEC_Object = MibScalar
aspectRatioARDSPEC = _AspectRatioARDSPEC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 6),
    _AspectRatioARDSPEC_Type()
)
aspectRatioARDSPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioARDSPEC.setStatus("mandatory")
_ActiveFormatARDSPEC_Type = DisplayString
_ActiveFormatARDSPEC_Object = MibScalar
activeFormatARDSPEC = _ActiveFormatARDSPEC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 7),
    _ActiveFormatARDSPEC_Type()
)
activeFormatARDSPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFormatARDSPEC.setStatus("mandatory")
_ParityBitsARDSPEC_Type = DisplayString
_ParityBitsARDSPEC_Object = MibScalar
parityBitsARDSPEC = _ParityBitsARDSPEC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 8),
    _ParityBitsARDSPEC_Type()
)
parityBitsARDSPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parityBitsARDSPEC.setStatus("mandatory")
_EnhancedServicesARDSPEC_Type = DisplayString
_EnhancedServicesARDSPEC_Object = MibScalar
enhancedServicesARDSPEC = _EnhancedServicesARDSPEC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 9),
    _EnhancedServicesARDSPEC_Type()
)
enhancedServicesARDSPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enhancedServicesARDSPEC.setStatus("mandatory")
_ReservedARDSPEC_Type = DisplayString
_ReservedARDSPEC_Object = MibScalar
reservedARDSPEC = _ReservedARDSPEC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 3, 10),
    _ReservedARDSPEC_Type()
)
reservedARDSPEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reservedARDSPEC.setStatus("mandatory")
_Teletext_ObjectIdentity = ObjectIdentity
teletext = _Teletext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 4)
)


class _Present_Type(Integer32):
    """Custom type present based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 1),
          ("present", 2))
    )


_Present_Type.__name__ = "Integer32"
_Present_Object = MibScalar
present = _Present_Object(
    (1, 3, 6, 1, 4, 1, 18458, 4, 1),
    _Present_Type()
)
present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    present.setStatus("mandatory")
_Closedcaptions_ObjectIdentity = ObjectIdentity
closedcaptions = _Closedcaptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 5)
)


class _ClosedCaptionAnc608_Type(Integer32):
    """Custom type closedCaptionAnc608 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 1),
          ("present", 2))
    )


_ClosedCaptionAnc608_Type.__name__ = "Integer32"
_ClosedCaptionAnc608_Object = MibScalar
closedCaptionAnc608 = _ClosedCaptionAnc608_Object(
    (1, 3, 6, 1, 4, 1, 18458, 5, 1),
    _ClosedCaptionAnc608_Type()
)
closedCaptionAnc608.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    closedCaptionAnc608.setStatus("mandatory")


class _ClosedCaptionAnc708_Type(Integer32):
    """Custom type closedCaptionAnc708 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 1),
          ("present", 2))
    )


_ClosedCaptionAnc708_Type.__name__ = "Integer32"
_ClosedCaptionAnc708_Object = MibScalar
closedCaptionAnc708 = _ClosedCaptionAnc708_Object(
    (1, 3, 6, 1, 4, 1, 18458, 5, 2),
    _ClosedCaptionAnc708_Type()
)
closedCaptionAnc708.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    closedCaptionAnc708.setStatus("mandatory")


class _ClosedCaptionLine21_Type(Integer32):
    """Custom type closedCaptionLine21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 1),
          ("present", 2))
    )


_ClosedCaptionLine21_Type.__name__ = "Integer32"
_ClosedCaptionLine21_Object = MibScalar
closedCaptionLine21 = _ClosedCaptionLine21_Object(
    (1, 3, 6, 1, 4, 1, 18458, 5, 3),
    _ClosedCaptionLine21_Type()
)
closedCaptionLine21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    closedCaptionLine21.setStatus("mandatory")
_Errors_ObjectIdentity = ObjectIdentity
errors = _Errors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 6)
)
_CrcErrors_Type = Integer32
_CrcErrors_Object = MibScalar
crcErrors = _CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 1),
    _CrcErrors_Type()
)
crcErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcErrors.setStatus("mandatory")
_CrcBErrors_Type = Integer32
_CrcBErrors_Object = MibScalar
crcBErrors = _CrcBErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 2),
    _CrcBErrors_Type()
)
crcBErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crcBErrors.setStatus("mandatory")
_RgbRangeErrors_Type = Integer32
_RgbRangeErrors_Object = MibScalar
rgbRangeErrors = _RgbRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 3),
    _RgbRangeErrors_Type()
)
rgbRangeErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgbRangeErrors.setStatus("mandatory")
_RgbRangeMin_Type = Integer32
_RgbRangeMin_Object = MibScalar
rgbRangeMin = _RgbRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 4),
    _RgbRangeMin_Type()
)
rgbRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgbRangeMin.setStatus("mandatory")
_RgbRangeMax_Type = Integer32
_RgbRangeMax_Object = MibScalar
rgbRangeMax = _RgbRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 5),
    _RgbRangeMax_Type()
)
rgbRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rgbRangeMax.setStatus("mandatory")
_YcbcrRangeErrors_Type = Integer32
_YcbcrRangeErrors_Object = MibScalar
ycbcrRangeErrors = _YcbcrRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 6),
    _YcbcrRangeErrors_Type()
)
ycbcrRangeErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ycbcrRangeErrors.setStatus("mandatory")
_YRangeMin_Type = Integer32
_YRangeMin_Object = MibScalar
yRangeMin = _YRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 7),
    _YRangeMin_Type()
)
yRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    yRangeMin.setStatus("mandatory")
_YRrangeMax_Type = Integer32
_YRrangeMax_Object = MibScalar
yRrangeMax = _YRrangeMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 8),
    _YRrangeMax_Type()
)
yRrangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    yRrangeMax.setStatus("mandatory")
_URangeMin_Type = Integer32
_URangeMin_Object = MibScalar
uRangeMin = _URangeMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 9),
    _URangeMin_Type()
)
uRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uRangeMin.setStatus("mandatory")
_URangeMax_Type = Integer32
_URangeMax_Object = MibScalar
uRangeMax = _URangeMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 10),
    _URangeMax_Type()
)
uRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uRangeMax.setStatus("mandatory")
_VRangeMin_Type = Integer32
_VRangeMin_Object = MibScalar
vRangeMin = _VRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 11),
    _VRangeMin_Type()
)
vRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRangeMin.setStatus("mandatory")
_VRangeMax_Type = Integer32
_VRangeMax_Object = MibScalar
vRangeMax = _VRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 12),
    _VRangeMax_Type()
)
vRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRangeMax.setStatus("mandatory")
_TrsErrors_Type = Integer32
_TrsErrors_Object = MibScalar
trsErrors = _TrsErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 13),
    _TrsErrors_Type()
)
trsErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsErrors.setStatus("mandatory")
_TrsBErrors_Type = Integer32
_TrsBErrors_Object = MibScalar
trsBErrors = _TrsBErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 14),
    _TrsBErrors_Type()
)
trsBErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trsBErrors.setStatus("mandatory")
_AncErrors_Type = Integer32
_AncErrors_Object = MibScalar
ancErrors = _AncErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 15),
    _AncErrors_Type()
)
ancErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ancErrors.setStatus("mandatory")
_AncBErrors_Type = Integer32
_AncBErrors_Object = MibScalar
ancBErrors = _AncBErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 16),
    _AncBErrors_Type()
)
ancBErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ancBErrors.setStatus("mandatory")
_LineErrors_Type = Integer32
_LineErrors_Object = MibScalar
lineErrors = _LineErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 17),
    _LineErrors_Type()
)
lineErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineErrors.setStatus("mandatory")
_LineBErrors_Type = Integer32
_LineBErrors_Object = MibScalar
lineBErrors = _LineBErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 18),
    _LineBErrors_Type()
)
lineBErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBErrors.setStatus("mandatory")
_FrozenVITC_Type = Integer32
_FrozenVITC_Object = MibScalar
frozenVITC = _FrozenVITC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 19),
    _FrozenVITC_Type()
)
frozenVITC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frozenVITC.setStatus("mandatory")
_SkippedVITC_Type = Integer32
_SkippedVITC_Object = MibScalar
skippedVITC = _SkippedVITC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 20),
    _SkippedVITC_Type()
)
skippedVITC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skippedVITC.setStatus("mandatory")
_FrozenATC_Type = Integer32
_FrozenATC_Object = MibScalar
frozenATC = _FrozenATC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 21),
    _FrozenATC_Type()
)
frozenATC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frozenATC.setStatus("mandatory")
_SkippedATC_Type = Integer32
_SkippedATC_Object = MibScalar
skippedATC = _SkippedATC_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 22),
    _SkippedATC_Type()
)
skippedATC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    skippedATC.setStatus("mandatory")
_CompRangeErrors_Type = Integer32
_CompRangeErrors_Object = MibScalar
compRangeErrors = _CompRangeErrors_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 23),
    _CompRangeErrors_Type()
)
compRangeErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compRangeErrors.setStatus("mandatory")
_CompRangeMin_Type = Integer32
_CompRangeMin_Object = MibScalar
compRangeMin = _CompRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 24),
    _CompRangeMin_Type()
)
compRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compRangeMin.setStatus("mandatory")
_CompRangeMax_Type = Integer32
_CompRangeMax_Object = MibScalar
compRangeMax = _CompRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 25),
    _CompRangeMax_Type()
)
compRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compRangeMax.setStatus("mandatory")
_EdhError_Type = Integer32
_EdhError_Object = MibScalar
edhError = _EdhError_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 26),
    _EdhError_Type()
)
edhError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edhError.setStatus("mandatory")
_EdhInvalid_Type = Integer32
_EdhInvalid_Object = MibScalar
edhInvalid = _EdhInvalid_Object(
    (1, 3, 6, 1, 4, 1, 18458, 6, 27),
    _EdhInvalid_Type()
)
edhInvalid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edhInvalid.setStatus("mandatory")
_Timecode_ObjectIdentity = ObjectIdentity
timecode = _Timecode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 7)
)
_Vitc_Type = DisplayString
_Vitc_Object = MibScalar
vitc = _Vitc_Object(
    (1, 3, 6, 1, 4, 1, 18458, 7, 1),
    _Vitc_Type()
)
vitc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vitc.setStatus("mandatory")
_Atc_Type = DisplayString
_Atc_Object = MibScalar
atc = _Atc_Object(
    (1, 3, 6, 1, 4, 1, 18458, 7, 2),
    _Atc_Type()
)
atc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atc.setStatus("mandatory")
_Audio_ObjectIdentity = ObjectIdentity
audio = _Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 8)
)
_UsageGroup1_Type = DisplayString
_UsageGroup1_Object = MibScalar
usageGroup1 = _UsageGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 1),
    _UsageGroup1_Type()
)
usageGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageGroup1.setStatus("mandatory")
_UsageGroup2_Type = DisplayString
_UsageGroup2_Object = MibScalar
usageGroup2 = _UsageGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 2),
    _UsageGroup2_Type()
)
usageGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageGroup2.setStatus("mandatory")
_UsageGroup3_Type = DisplayString
_UsageGroup3_Object = MibScalar
usageGroup3 = _UsageGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 3),
    _UsageGroup3_Type()
)
usageGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageGroup3.setStatus("mandatory")
_UsageGroup4_Type = DisplayString
_UsageGroup4_Object = MibScalar
usageGroup4 = _UsageGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 4),
    _UsageGroup4_Type()
)
usageGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usageGroup4.setStatus("mandatory")


class _SampleGroup1_Type(Integer32):
    """Custom type sampleGroup1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 2))
    )


_SampleGroup1_Type.__name__ = "Integer32"
_SampleGroup1_Object = MibScalar
sampleGroup1 = _SampleGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 5),
    _SampleGroup1_Type()
)
sampleGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sampleGroup1.setStatus("mandatory")


class _SampleGroup2_Type(Integer32):
    """Custom type sampleGroup2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 2))
    )


_SampleGroup2_Type.__name__ = "Integer32"
_SampleGroup2_Object = MibScalar
sampleGroup2 = _SampleGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 6),
    _SampleGroup2_Type()
)
sampleGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sampleGroup2.setStatus("mandatory")


class _SampleGroup3_Type(Integer32):
    """Custom type sampleGroup3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 2))
    )


_SampleGroup3_Type.__name__ = "Integer32"
_SampleGroup3_Object = MibScalar
sampleGroup3 = _SampleGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 7),
    _SampleGroup3_Type()
)
sampleGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sampleGroup3.setStatus("mandatory")


class _SampleGroup4_Type(Integer32):
    """Custom type sampleGroup4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audio", 1),
          ("data", 2))
    )


_SampleGroup4_Type.__name__ = "Integer32"
_SampleGroup4_Object = MibScalar
sampleGroup4 = _SampleGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 8),
    _SampleGroup4_Type()
)
sampleGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sampleGroup4.setStatus("mandatory")


class _EmphasisGroup1_Type(Integer32):
    """Custom type emphasisGroup1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EmphasisGroup1_Type.__name__ = "Integer32"
_EmphasisGroup1_Object = MibScalar
emphasisGroup1 = _EmphasisGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 9),
    _EmphasisGroup1_Type()
)
emphasisGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emphasisGroup1.setStatus("mandatory")


class _EmphasisGroup2_Type(Integer32):
    """Custom type emphasisGroup2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EmphasisGroup2_Type.__name__ = "Integer32"
_EmphasisGroup2_Object = MibScalar
emphasisGroup2 = _EmphasisGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 10),
    _EmphasisGroup2_Type()
)
emphasisGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emphasisGroup2.setStatus("mandatory")


class _EmphasisGroup3_Type(Integer32):
    """Custom type emphasisGroup3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EmphasisGroup3_Type.__name__ = "Integer32"
_EmphasisGroup3_Object = MibScalar
emphasisGroup3 = _EmphasisGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 11),
    _EmphasisGroup3_Type()
)
emphasisGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emphasisGroup3.setStatus("mandatory")


class _EmphasisGroup4_Type(Integer32):
    """Custom type emphasisGroup4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EmphasisGroup4_Type.__name__ = "Integer32"
_EmphasisGroup4_Object = MibScalar
emphasisGroup4 = _EmphasisGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 12),
    _EmphasisGroup4_Type()
)
emphasisGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emphasisGroup4.setStatus("mandatory")


class _LockGroup1_Type(Integer32):
    """Custom type lockGroup1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LockGroup1_Type.__name__ = "Integer32"
_LockGroup1_Object = MibScalar
lockGroup1 = _LockGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 13),
    _LockGroup1_Type()
)
lockGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockGroup1.setStatus("mandatory")


class _LockGroup2_Type(Integer32):
    """Custom type lockGroup2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LockGroup2_Type.__name__ = "Integer32"
_LockGroup2_Object = MibScalar
lockGroup2 = _LockGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 14),
    _LockGroup2_Type()
)
lockGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockGroup2.setStatus("mandatory")


class _LockGroup3_Type(Integer32):
    """Custom type lockGroup3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LockGroup3_Type.__name__ = "Integer32"
_LockGroup3_Object = MibScalar
lockGroup3 = _LockGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 15),
    _LockGroup3_Type()
)
lockGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockGroup3.setStatus("mandatory")


class _LockGroup4_Type(Integer32):
    """Custom type lockGroup4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_LockGroup4_Type.__name__ = "Integer32"
_LockGroup4_Object = MibScalar
lockGroup4 = _LockGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 16),
    _LockGroup4_Type()
)
lockGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lockGroup4.setStatus("mandatory")


class _FrequencyGroup1_Type(Integer32):
    """Custom type frequencyGroup1 based on Integer32"""
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
        *(("default48khz", 1),
          ("freq32khz", 4),
          ("freq441khz", 3),
          ("manual48khz", 2))
    )


_FrequencyGroup1_Type.__name__ = "Integer32"
_FrequencyGroup1_Object = MibScalar
frequencyGroup1 = _FrequencyGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 17),
    _FrequencyGroup1_Type()
)
frequencyGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyGroup1.setStatus("mandatory")


class _FrequencyGroup2_Type(Integer32):
    """Custom type frequencyGroup2 based on Integer32"""
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
        *(("default48khz", 1),
          ("freq32khz", 4),
          ("freq441khz", 3),
          ("manual48khz", 2))
    )


_FrequencyGroup2_Type.__name__ = "Integer32"
_FrequencyGroup2_Object = MibScalar
frequencyGroup2 = _FrequencyGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 18),
    _FrequencyGroup2_Type()
)
frequencyGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyGroup2.setStatus("mandatory")


class _FrequencyGroup3_Type(Integer32):
    """Custom type frequencyGroup3 based on Integer32"""
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
        *(("default48khz", 1),
          ("freq32khz", 4),
          ("freq441khz", 3),
          ("manual48khz", 2))
    )


_FrequencyGroup3_Type.__name__ = "Integer32"
_FrequencyGroup3_Object = MibScalar
frequencyGroup3 = _FrequencyGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 19),
    _FrequencyGroup3_Type()
)
frequencyGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyGroup3.setStatus("mandatory")


class _FrequencyGroup4_Type(Integer32):
    """Custom type frequencyGroup4 based on Integer32"""
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
        *(("default48khz", 1),
          ("freq32khz", 4),
          ("freq441khz", 3),
          ("manual48khz", 2))
    )


_FrequencyGroup4_Type.__name__ = "Integer32"
_FrequencyGroup4_Object = MibScalar
frequencyGroup4 = _FrequencyGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 20),
    _FrequencyGroup4_Type()
)
frequencyGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequencyGroup4.setStatus("mandatory")


class _ChannelModeGroup1_Type(Integer32):
    """Custom type channelModeGroup1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dual", 2),
          ("primarysecondary", 4),
          ("single", 3),
          ("stereo", 5))
    )


_ChannelModeGroup1_Type.__name__ = "Integer32"
_ChannelModeGroup1_Object = MibScalar
channelModeGroup1 = _ChannelModeGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 21),
    _ChannelModeGroup1_Type()
)
channelModeGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelModeGroup1.setStatus("mandatory")


class _ChannelModeGroup2_Type(Integer32):
    """Custom type channelModeGroup2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dual", 2),
          ("primarysecondary", 4),
          ("single", 3),
          ("stereo", 5))
    )


_ChannelModeGroup2_Type.__name__ = "Integer32"
_ChannelModeGroup2_Object = MibScalar
channelModeGroup2 = _ChannelModeGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 22),
    _ChannelModeGroup2_Type()
)
channelModeGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelModeGroup2.setStatus("mandatory")


class _ChannelModeGroup3_Type(Integer32):
    """Custom type channelModeGroup3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dual", 2),
          ("primarysecondary", 4),
          ("single", 3),
          ("stereo", 5))
    )


_ChannelModeGroup3_Type.__name__ = "Integer32"
_ChannelModeGroup3_Object = MibScalar
channelModeGroup3 = _ChannelModeGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 23),
    _ChannelModeGroup3_Type()
)
channelModeGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelModeGroup3.setStatus("mandatory")


class _ChannelModeGroup4_Type(Integer32):
    """Custom type channelModeGroup4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("dual", 2),
          ("primarysecondary", 4),
          ("single", 3),
          ("stereo", 5))
    )


_ChannelModeGroup4_Type.__name__ = "Integer32"
_ChannelModeGroup4_Object = MibScalar
channelModeGroup4 = _ChannelModeGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 24),
    _ChannelModeGroup4_Type()
)
channelModeGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelModeGroup4.setStatus("mandatory")


class _WordLengthGroup1_Type(Integer32):
    """Custom type wordLengthGroup1 based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits16", 2),
          ("bits18", 3),
          ("bits19", 4),
          ("bits20", 5),
          ("bits22", 6),
          ("bits23", 7),
          ("bits24", 8),
          ("default", 1),
          ("user", 9))
    )


_WordLengthGroup1_Type.__name__ = "Integer32"
_WordLengthGroup1_Object = MibScalar
wordLengthGroup1 = _WordLengthGroup1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 25),
    _WordLengthGroup1_Type()
)
wordLengthGroup1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordLengthGroup1.setStatus("mandatory")


class _WordLengthGroup2_Type(Integer32):
    """Custom type wordLengthGroup2 based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits16", 2),
          ("bits18", 3),
          ("bits19", 4),
          ("bits20", 5),
          ("bits22", 6),
          ("bits23", 7),
          ("bits24", 8),
          ("default", 1),
          ("user", 9))
    )


_WordLengthGroup2_Type.__name__ = "Integer32"
_WordLengthGroup2_Object = MibScalar
wordLengthGroup2 = _WordLengthGroup2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 26),
    _WordLengthGroup2_Type()
)
wordLengthGroup2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordLengthGroup2.setStatus("mandatory")


class _WordLengthGroup3_Type(Integer32):
    """Custom type wordLengthGroup3 based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits16", 2),
          ("bits18", 3),
          ("bits19", 4),
          ("bits20", 5),
          ("bits22", 6),
          ("bits23", 7),
          ("bits24", 8),
          ("default", 1),
          ("user", 9))
    )


_WordLengthGroup3_Type.__name__ = "Integer32"
_WordLengthGroup3_Object = MibScalar
wordLengthGroup3 = _WordLengthGroup3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 27),
    _WordLengthGroup3_Type()
)
wordLengthGroup3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordLengthGroup3.setStatus("mandatory")


class _WordLengthGroup4_Type(Integer32):
    """Custom type wordLengthGroup4 based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bits16", 2),
          ("bits18", 3),
          ("bits19", 4),
          ("bits20", 5),
          ("bits22", 6),
          ("bits23", 7),
          ("bits24", 8),
          ("default", 1),
          ("user", 9))
    )


_WordLengthGroup4_Type.__name__ = "Integer32"
_WordLengthGroup4_Object = MibScalar
wordLengthGroup4 = _WordLengthGroup4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 28),
    _WordLengthGroup4_Type()
)
wordLengthGroup4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wordLengthGroup4.setStatus("mandatory")
_ChannelStatus1_Type = AudioStatus
_ChannelStatus1_Object = MibScalar
channelStatus1 = _ChannelStatus1_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 29),
    _ChannelStatus1_Type()
)
channelStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus1.setStatus("mandatory")
_ChannelStatus2_Type = AudioStatus
_ChannelStatus2_Object = MibScalar
channelStatus2 = _ChannelStatus2_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 30),
    _ChannelStatus2_Type()
)
channelStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus2.setStatus("mandatory")
_ChannelStatus3_Type = AudioStatus
_ChannelStatus3_Object = MibScalar
channelStatus3 = _ChannelStatus3_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 31),
    _ChannelStatus3_Type()
)
channelStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus3.setStatus("mandatory")
_ChannelStatus4_Type = AudioStatus
_ChannelStatus4_Object = MibScalar
channelStatus4 = _ChannelStatus4_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 32),
    _ChannelStatus4_Type()
)
channelStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus4.setStatus("mandatory")
_ChannelStatus5_Type = AudioStatus
_ChannelStatus5_Object = MibScalar
channelStatus5 = _ChannelStatus5_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 33),
    _ChannelStatus5_Type()
)
channelStatus5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus5.setStatus("mandatory")
_ChannelStatus6_Type = AudioStatus
_ChannelStatus6_Object = MibScalar
channelStatus6 = _ChannelStatus6_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 34),
    _ChannelStatus6_Type()
)
channelStatus6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus6.setStatus("mandatory")
_ChannelStatus7_Type = AudioStatus
_ChannelStatus7_Object = MibScalar
channelStatus7 = _ChannelStatus7_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 35),
    _ChannelStatus7_Type()
)
channelStatus7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus7.setStatus("mandatory")
_ChannelStatus8_Type = AudioStatus
_ChannelStatus8_Object = MibScalar
channelStatus8 = _ChannelStatus8_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 36),
    _ChannelStatus8_Type()
)
channelStatus8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus8.setStatus("mandatory")
_ChannelStatus9_Type = AudioStatus
_ChannelStatus9_Object = MibScalar
channelStatus9 = _ChannelStatus9_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 37),
    _ChannelStatus9_Type()
)
channelStatus9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus9.setStatus("mandatory")
_ChannelStatus10_Type = AudioStatus
_ChannelStatus10_Object = MibScalar
channelStatus10 = _ChannelStatus10_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 38),
    _ChannelStatus10_Type()
)
channelStatus10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus10.setStatus("mandatory")
_ChannelStatus11_Type = AudioStatus
_ChannelStatus11_Object = MibScalar
channelStatus11 = _ChannelStatus11_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 39),
    _ChannelStatus11_Type()
)
channelStatus11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus11.setStatus("mandatory")
_ChannelStatus12_Type = AudioStatus
_ChannelStatus12_Object = MibScalar
channelStatus12 = _ChannelStatus12_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 40),
    _ChannelStatus12_Type()
)
channelStatus12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus12.setStatus("mandatory")
_ChannelStatus13_Type = AudioStatus
_ChannelStatus13_Object = MibScalar
channelStatus13 = _ChannelStatus13_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 41),
    _ChannelStatus13_Type()
)
channelStatus13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus13.setStatus("mandatory")
_ChannelStatus14_Type = AudioStatus
_ChannelStatus14_Object = MibScalar
channelStatus14 = _ChannelStatus14_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 42),
    _ChannelStatus14_Type()
)
channelStatus14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus14.setStatus("mandatory")
_ChannelStatus15_Type = AudioStatus
_ChannelStatus15_Object = MibScalar
channelStatus15 = _ChannelStatus15_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 43),
    _ChannelStatus15_Type()
)
channelStatus15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus15.setStatus("mandatory")
_ChannelStatus16_Type = AudioStatus
_ChannelStatus16_Object = MibScalar
channelStatus16 = _ChannelStatus16_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 44),
    _ChannelStatus16_Type()
)
channelStatus16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus16.setStatus("mandatory")
_AudioMin_Type = Integer32
_AudioMin_Object = MibScalar
audioMin = _AudioMin_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 45),
    _AudioMin_Type()
)
audioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioMin.setStatus("mandatory")
_AudioMax_Type = Integer32
_AudioMax_Object = MibScalar
audioMax = _AudioMax_Object(
    (1, 3, 6, 1, 4, 1, 18458, 8, 46),
    _AudioMax_Type()
)
audioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioMax.setStatus("mandatory")
_Logging_ObjectIdentity = ObjectIdentity
logging = _Logging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 9)
)
_JobId_Type = DisplayString
_JobId_Object = MibScalar
jobId = _JobId_Object(
    (1, 3, 6, 1, 4, 1, 18458, 9, 1),
    _JobId_Type()
)
jobId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    jobId.setStatus("mandatory")
_Generator_ObjectIdentity = ObjectIdentity
generator = _Generator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18458, 10)
)
_IndexPattern_Type = Integer32
_IndexPattern_Object = MibScalar
indexPattern = _IndexPattern_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 1),
    _IndexPattern_Type()
)
indexPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    indexPattern.setStatus("mandatory")
_NextPattern_Type = Integer32
_NextPattern_Object = MibScalar
nextPattern = _NextPattern_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 2),
    _NextPattern_Type()
)
nextPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nextPattern.setStatus("mandatory")
_PrevPattern_Type = Integer32
_PrevPattern_Object = MibScalar
prevPattern = _PrevPattern_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 3),
    _PrevPattern_Type()
)
prevPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    prevPattern.setStatus("mandatory")
_TransportToStart_Type = Integer32
_TransportToStart_Object = MibScalar
transportToStart = _TransportToStart_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 4),
    _TransportToStart_Type()
)
transportToStart.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    transportToStart.setStatus("mandatory")
_TransportJogBack_Type = Integer32
_TransportJogBack_Object = MibScalar
transportJogBack = _TransportJogBack_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 5),
    _TransportJogBack_Type()
)
transportJogBack.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    transportJogBack.setStatus("mandatory")
_TransportPlayReverse_Type = Integer32
_TransportPlayReverse_Object = MibScalar
transportPlayReverse = _TransportPlayReverse_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 6),
    _TransportPlayReverse_Type()
)
transportPlayReverse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportPlayReverse.setStatus("mandatory")
_TransportStop_Type = Integer32
_TransportStop_Object = MibScalar
transportStop = _TransportStop_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 7),
    _TransportStop_Type()
)
transportStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportStop.setStatus("mandatory")
_TransportPlayForward_Type = Integer32
_TransportPlayForward_Object = MibScalar
transportPlayForward = _TransportPlayForward_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 8),
    _TransportPlayForward_Type()
)
transportPlayForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportPlayForward.setStatus("mandatory")
_TransportJogNext_Type = Integer32
_TransportJogNext_Object = MibScalar
transportJogNext = _TransportJogNext_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 9),
    _TransportJogNext_Type()
)
transportJogNext.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    transportJogNext.setStatus("mandatory")
_TransportToEnd_Type = Integer32
_TransportToEnd_Object = MibScalar
transportToEnd = _TransportToEnd_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 10),
    _TransportToEnd_Type()
)
transportToEnd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    transportToEnd.setStatus("mandatory")
_TransportLoop_Type = Integer32
_TransportLoop_Object = MibScalar
transportLoop = _TransportLoop_Object(
    (1, 3, 6, 1, 4, 1, 18458, 10, 11),
    _TransportLoop_Type()
)
transportLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transportLoop.setStatus("mandatory")

# Managed Objects groups


# Notification objects

systemUpTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 0, 1)
)
if mibBuilder.loadTexts:
    systemUpTRAP.setStatus(
        ""
    )

systemDownTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 0, 2)
)
if mibBuilder.loadTexts:
    systemDownTRAP.setStatus(
        ""
    )

videoStandardChangedTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 3)
)
videoStandardChangedTRAP.setObjects(
    ("OMNITEK-MIB", "videoStandard")
)
if mibBuilder.loadTexts:
    videoStandardChangedTRAP.setStatus(
        ""
    )

digitalInputTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 4)
)
digitalInputTRAP.setObjects(
    ("OMNITEK-MIB", "digitalInput")
)
if mibBuilder.loadTexts:
    digitalInputTRAP.setStatus(
        ""
    )

digitalInputBTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 5)
)
digitalInputBTRAP.setObjects(
    ("OMNITEK-MIB", "digitalInputB")
)
if mibBuilder.loadTexts:
    digitalInputBTRAP.setStatus(
        ""
    )

motionContentTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 6)
)
motionContentTRAP.setObjects(
    ("OMNITEK-MIB", "motionContent")
)
if mibBuilder.loadTexts:
    motionContentTRAP.setStatus(
        ""
    )

lumaContentTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 7)
)
lumaContentTRAP.setObjects(
    ("OMNITEK-MIB", "lumaContent")
)
if mibBuilder.loadTexts:
    lumaContentTRAP.setStatus(
        ""
    )

chromaContentTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 8)
)
chromaContentTRAP.setObjects(
    ("OMNITEK-MIB", "chromaContent")
)
if mibBuilder.loadTexts:
    chromaContentTRAP.setStatus(
        ""
    )

syncStatusTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 1, 0, 9)
)
syncStatusTRAP.setObjects(
    ("OMNITEK-MIB", "syncStatus")
)
if mibBuilder.loadTexts:
    syncStatusTRAP.setStatus(
        ""
    )

crcErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 10)
)
crcErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "crcErrors")
)
if mibBuilder.loadTexts:
    crcErrorsTRAP.setStatus(
        ""
    )

crcBErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 11)
)
crcBErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "crcBErrors")
)
if mibBuilder.loadTexts:
    crcBErrorsTRAP.setStatus(
        ""
    )

rgbRangeErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 12)
)
rgbRangeErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "rgbRangeErrors")
)
if mibBuilder.loadTexts:
    rgbRangeErrorsTRAP.setStatus(
        ""
    )

ycbcrRangeErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 13)
)
ycbcrRangeErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "ycbcrRangeErrors")
)
if mibBuilder.loadTexts:
    ycbcrRangeErrorsTRAP.setStatus(
        ""
    )

trsErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 14)
)
trsErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "trsErrors")
)
if mibBuilder.loadTexts:
    trsErrorsTRAP.setStatus(
        ""
    )

trsBErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 15)
)
trsBErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "trsBErrors")
)
if mibBuilder.loadTexts:
    trsBErrorsTRAP.setStatus(
        ""
    )

ancErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 16)
)
ancErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "ancErrors")
)
if mibBuilder.loadTexts:
    ancErrorsTRAP.setStatus(
        ""
    )

ancBErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 17)
)
ancBErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "ancBErrors")
)
if mibBuilder.loadTexts:
    ancBErrorsTRAP.setStatus(
        ""
    )

lineErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 18)
)
lineErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "lineErrors")
)
if mibBuilder.loadTexts:
    lineErrorsTRAP.setStatus(
        ""
    )

lineBErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 19)
)
lineBErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "lineBErrors")
)
if mibBuilder.loadTexts:
    lineBErrorsTRAP.setStatus(
        ""
    )

frozenVITCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 20)
)
frozenVITCTRAP.setObjects(
    ("OMNITEK-MIB", "frozenVITC")
)
if mibBuilder.loadTexts:
    frozenVITCTRAP.setStatus(
        ""
    )

skippedVITCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 21)
)
skippedVITCTRAP.setObjects(
    ("OMNITEK-MIB", "skippedVITC")
)
if mibBuilder.loadTexts:
    skippedVITCTRAP.setStatus(
        ""
    )

frozenATCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 22)
)
frozenATCTRAP.setObjects(
    ("OMNITEK-MIB", "frozenATC")
)
if mibBuilder.loadTexts:
    frozenATCTRAP.setStatus(
        ""
    )

skippedATCTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 23)
)
skippedATCTRAP.setObjects(
    ("OMNITEK-MIB", "skippedATC")
)
if mibBuilder.loadTexts:
    skippedATCTRAP.setStatus(
        ""
    )

compRangeErrorsTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 24)
)
compRangeErrorsTRAP.setObjects(
    ("OMNITEK-MIB", "compRangeErrors")
)
if mibBuilder.loadTexts:
    compRangeErrorsTRAP.setStatus(
        ""
    )

edhErrorTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 25)
)
edhErrorTRAP.setObjects(
    ("OMNITEK-MIB", "edhError")
)
if mibBuilder.loadTexts:
    edhErrorTRAP.setStatus(
        ""
    )

edhInvalidTRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 18458, 6, 0, 26)
)
edhInvalidTRAP.setObjects(
    ("OMNITEK-MIB", "edhInvalid")
)
if mibBuilder.loadTexts:
    edhInvalidTRAP.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNITEK-MIB",
    **{"AudioStatus": AudioStatus,
       "omnitek": omnitek,
       "systemUpTRAP": systemUpTRAP,
       "systemDownTRAP": systemDownTRAP,
       "videostatus": videostatus,
       "videoStandardChangedTRAP": videoStandardChangedTRAP,
       "digitalInputTRAP": digitalInputTRAP,
       "digitalInputBTRAP": digitalInputBTRAP,
       "motionContentTRAP": motionContentTRAP,
       "lumaContentTRAP": lumaContentTRAP,
       "chromaContentTRAP": chromaContentTRAP,
       "syncStatusTRAP": syncStatusTRAP,
       "videoStandard": videoStandard,
       "digitalInput": digitalInput,
       "digitalInputB": digitalInputB,
       "motionContent": motionContent,
       "lumaContent": lumaContent,
       "chromaContent": chromaContent,
       "syncStatus": syncStatus,
       "videoindex": videoindex,
       "activeFormat": activeFormat,
       "codedFrame": codedFrame,
       "componentSet": componentSet,
       "sampleStructure": sampleStructure,
       "wss": wss,
       "wssReadType": wssReadType,
       "aspectRatioEN300294": aspectRatioEN300294,
       "enhancedServicesEN300294": enhancedServicesEN300294,
       "subtitlesEN300294": subtitlesEN300294,
       "othersEN300294": othersEN300294,
       "aspectRatioARDSPEC": aspectRatioARDSPEC,
       "activeFormatARDSPEC": activeFormatARDSPEC,
       "parityBitsARDSPEC": parityBitsARDSPEC,
       "enhancedServicesARDSPEC": enhancedServicesARDSPEC,
       "reservedARDSPEC": reservedARDSPEC,
       "teletext": teletext,
       "present": present,
       "closedcaptions": closedcaptions,
       "closedCaptionAnc608": closedCaptionAnc608,
       "closedCaptionAnc708": closedCaptionAnc708,
       "closedCaptionLine21": closedCaptionLine21,
       "errors": errors,
       "crcErrorsTRAP": crcErrorsTRAP,
       "crcBErrorsTRAP": crcBErrorsTRAP,
       "rgbRangeErrorsTRAP": rgbRangeErrorsTRAP,
       "ycbcrRangeErrorsTRAP": ycbcrRangeErrorsTRAP,
       "trsErrorsTRAP": trsErrorsTRAP,
       "trsBErrorsTRAP": trsBErrorsTRAP,
       "ancErrorsTRAP": ancErrorsTRAP,
       "ancBErrorsTRAP": ancBErrorsTRAP,
       "lineErrorsTRAP": lineErrorsTRAP,
       "lineBErrorsTRAP": lineBErrorsTRAP,
       "frozenVITCTRAP": frozenVITCTRAP,
       "skippedVITCTRAP": skippedVITCTRAP,
       "frozenATCTRAP": frozenATCTRAP,
       "skippedATCTRAP": skippedATCTRAP,
       "compRangeErrorsTRAP": compRangeErrorsTRAP,
       "edhErrorTRAP": edhErrorTRAP,
       "edhInvalidTRAP": edhInvalidTRAP,
       "crcErrors": crcErrors,
       "crcBErrors": crcBErrors,
       "rgbRangeErrors": rgbRangeErrors,
       "rgbRangeMin": rgbRangeMin,
       "rgbRangeMax": rgbRangeMax,
       "ycbcrRangeErrors": ycbcrRangeErrors,
       "yRangeMin": yRangeMin,
       "yRrangeMax": yRrangeMax,
       "uRangeMin": uRangeMin,
       "uRangeMax": uRangeMax,
       "vRangeMin": vRangeMin,
       "vRangeMax": vRangeMax,
       "trsErrors": trsErrors,
       "trsBErrors": trsBErrors,
       "ancErrors": ancErrors,
       "ancBErrors": ancBErrors,
       "lineErrors": lineErrors,
       "lineBErrors": lineBErrors,
       "frozenVITC": frozenVITC,
       "skippedVITC": skippedVITC,
       "frozenATC": frozenATC,
       "skippedATC": skippedATC,
       "compRangeErrors": compRangeErrors,
       "compRangeMin": compRangeMin,
       "compRangeMax": compRangeMax,
       "edhError": edhError,
       "edhInvalid": edhInvalid,
       "timecode": timecode,
       "vitc": vitc,
       "atc": atc,
       "audio": audio,
       "usageGroup1": usageGroup1,
       "usageGroup2": usageGroup2,
       "usageGroup3": usageGroup3,
       "usageGroup4": usageGroup4,
       "sampleGroup1": sampleGroup1,
       "sampleGroup2": sampleGroup2,
       "sampleGroup3": sampleGroup3,
       "sampleGroup4": sampleGroup4,
       "emphasisGroup1": emphasisGroup1,
       "emphasisGroup2": emphasisGroup2,
       "emphasisGroup3": emphasisGroup3,
       "emphasisGroup4": emphasisGroup4,
       "lockGroup1": lockGroup1,
       "lockGroup2": lockGroup2,
       "lockGroup3": lockGroup3,
       "lockGroup4": lockGroup4,
       "frequencyGroup1": frequencyGroup1,
       "frequencyGroup2": frequencyGroup2,
       "frequencyGroup3": frequencyGroup3,
       "frequencyGroup4": frequencyGroup4,
       "channelModeGroup1": channelModeGroup1,
       "channelModeGroup2": channelModeGroup2,
       "channelModeGroup3": channelModeGroup3,
       "channelModeGroup4": channelModeGroup4,
       "wordLengthGroup1": wordLengthGroup1,
       "wordLengthGroup2": wordLengthGroup2,
       "wordLengthGroup3": wordLengthGroup3,
       "wordLengthGroup4": wordLengthGroup4,
       "channelStatus1": channelStatus1,
       "channelStatus2": channelStatus2,
       "channelStatus3": channelStatus3,
       "channelStatus4": channelStatus4,
       "channelStatus5": channelStatus5,
       "channelStatus6": channelStatus6,
       "channelStatus7": channelStatus7,
       "channelStatus8": channelStatus8,
       "channelStatus9": channelStatus9,
       "channelStatus10": channelStatus10,
       "channelStatus11": channelStatus11,
       "channelStatus12": channelStatus12,
       "channelStatus13": channelStatus13,
       "channelStatus14": channelStatus14,
       "channelStatus15": channelStatus15,
       "channelStatus16": channelStatus16,
       "audioMin": audioMin,
       "audioMax": audioMax,
       "logging": logging,
       "jobId": jobId,
       "generator": generator,
       "indexPattern": indexPattern,
       "nextPattern": nextPattern,
       "prevPattern": prevPattern,
       "transportToStart": transportToStart,
       "transportJogBack": transportJogBack,
       "transportPlayReverse": transportPlayReverse,
       "transportStop": transportStop,
       "transportPlayForward": transportPlayForward,
       "transportJogNext": transportJogNext,
       "transportToEnd": transportToEnd,
       "transportLoop": transportLoop}
)
