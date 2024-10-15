# SNMP MIB module (CISCO-DMN-DSG-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:38 2024
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

ciscoDSGVideo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14)
)
ciscoDSGVideo.setRevisions(
        ("2010-10-13 08:00",
         "2010-08-30 11:00",
         "2010-03-22 05:00",
         "2010-02-12 12:00",
         "2009-12-07 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VideoCtrlTable_Object = MibTable
videoCtrlTable = _VideoCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1)
)
if mibBuilder.loadTexts:
    videoCtrlTable.setStatus("current")
_VideoCtrlEntry_Object = MibTableRow
videoCtrlEntry = _VideoCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1)
)
videoCtrlEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-VIDEO-MIB", "videoCtrlInstance"),
)
if mibBuilder.loadTexts:
    videoCtrlEntry.setStatus("current")


class _VideoCtrlInstance_Type(Integer32):
    """Custom type videoCtrlInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_VideoCtrlInstance_Type.__name__ = "Integer32"
_VideoCtrlInstance_Object = MibTableColumn
videoCtrlInstance = _VideoCtrlInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 1),
    _VideoCtrlInstance_Type()
)
videoCtrlInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    videoCtrlInstance.setStatus("current")


class _VideoPVFormat_Type(Integer32):
    """Custom type videoPVFormat based on Integer32"""
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
        *(("auto", 1),
          ("hd1080i", 2),
          ("hd720p", 3),
          ("sd", 4))
    )


_VideoPVFormat_Type.__name__ = "Integer32"
_VideoPVFormat_Object = MibTableColumn
videoPVFormat = _VideoPVFormat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 2),
    _VideoPVFormat_Type()
)
videoPVFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPVFormat.setStatus("current")


class _VideoSDFormat_Type(Integer32):
    """Custom type videoSDFormat based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("ntsc", 2),
          ("ntscJ", 8),
          ("palBG", 3),
          ("palD", 4),
          ("palI", 5),
          ("palM", 6),
          ("palNAR", 7))
    )


_VideoSDFormat_Type.__name__ = "Integer32"
_VideoSDFormat_Object = MibTableColumn
videoSDFormat = _VideoSDFormat_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 3),
    _VideoSDFormat_Type()
)
videoSDFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSDFormat.setStatus("current")


class _VideoTriSynch_Type(Integer32):
    """Custom type videoTriSynch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VideoTriSynch_Type.__name__ = "Integer32"
_VideoTriSynch_Object = MibTableColumn
videoTriSynch = _VideoTriSynch_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 4),
    _VideoTriSynch_Type()
)
videoTriSynch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoTriSynch.setStatus("current")


class _VideoCutoff_Type(Integer32):
    """Custom type videoCutoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VideoCutoff_Type.__name__ = "Integer32"
_VideoCutoff_Object = MibTableColumn
videoCutoff = _VideoCutoff_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 5),
    _VideoCutoff_Type()
)
videoCutoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoCutoff.setStatus("current")


class _AspectRatioSD_Type(Integer32):
    """Custom type aspectRatioSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourThird", 1),
          ("sixteenNinth", 2))
    )


_AspectRatioSD_Type.__name__ = "Integer32"
_AspectRatioSD_Object = MibTableColumn
aspectRatioSD = _AspectRatioSD_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 6),
    _AspectRatioSD_Type()
)
aspectRatioSD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aspectRatioSD.setStatus("current")


class _AspectRatioSelection_Type(Integer32):
    """Custom type aspectRatioSelection based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("autoAFD", 3),
          ("fourByThreeCCO", 7),
          ("fourByThreePillarBox", 5),
          ("fourteenByNine", 6),
          ("none", 1),
          ("sixteenByNineLetterBox", 4),
          ("sixteenByNineSCALE", 8))
    )


_AspectRatioSelection_Type.__name__ = "Integer32"
_AspectRatioSelection_Object = MibTableColumn
aspectRatioSelection = _AspectRatioSelection_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 7),
    _AspectRatioSelection_Type()
)
aspectRatioSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aspectRatioSelection.setStatus("current")


class _ClosedCaptionPrefMode_Type(Integer32):
    """Custom type closedCaptionPrefMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dvs157", 8),
          ("eia708", 3),
          ("reserved", 7),
          ("saCustom", 2),
          ("type3", 4),
          ("type4ATSC", 6),
          ("type4SA", 5))
    )


_ClosedCaptionPrefMode_Type.__name__ = "Integer32"
_ClosedCaptionPrefMode_Object = MibTableColumn
closedCaptionPrefMode = _ClosedCaptionPrefMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 1, 1, 8),
    _ClosedCaptionPrefMode_Type()
)
closedCaptionPrefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    closedCaptionPrefMode.setStatus("current")
_VideoStatusTable_Object = MibTable
videoStatusTable = _VideoStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2)
)
if mibBuilder.loadTexts:
    videoStatusTable.setStatus("current")
_VideoStatusEntry_Object = MibTableRow
videoStatusEntry = _VideoStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1)
)
videoStatusEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-VIDEO-MIB", "videoStatusInstance"),
)
if mibBuilder.loadTexts:
    videoStatusEntry.setStatus("current")


class _VideoStatusInstance_Type(Integer32):
    """Custom type videoStatusInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_VideoStatusInstance_Type.__name__ = "Integer32"
_VideoStatusInstance_Object = MibTableColumn
videoStatusInstance = _VideoStatusInstance_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 1),
    _VideoStatusInstance_Type()
)
videoStatusInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    videoStatusInstance.setStatus("current")


class _VideoStream_Type(Integer32):
    """Custom type videoStream based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("hd1080i2500", 7),
          ("hd1080i2997", 8),
          ("hd1080i3000", 9),
          ("hd720p5000", 4),
          ("hd720p5994", 5),
          ("hd720p6000", 6),
          ("sd480i2997", 1),
          ("sd480i3000", 2),
          ("sd576i2500", 3),
          ("unknown", 10),
          ("unsupported", 11))
    )


_VideoStream_Type.__name__ = "Integer32"
_VideoStream_Object = MibTableColumn
videoStream = _VideoStream_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 2),
    _VideoStream_Type()
)
videoStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoStream.setStatus("current")


class _VideoPVOutput_Type(Integer32):
    """Custom type videoPVOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hd1080i", 1),
          ("hd720p", 2))
    )


_VideoPVOutput_Type.__name__ = "Integer32"
_VideoPVOutput_Object = MibTableColumn
videoPVOutput = _VideoPVOutput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 3),
    _VideoPVOutput_Type()
)
videoPVOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoPVOutput.setStatus("current")


class _VideoSDOutput_Type(Integer32):
    """Custom type videoSDOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ntsc", 1),
          ("ntscJ", 7),
          ("palBG", 2),
          ("palD", 3),
          ("palI", 4),
          ("palM", 5),
          ("palNAR", 6))
    )


_VideoSDOutput_Type.__name__ = "Integer32"
_VideoSDOutput_Object = MibTableColumn
videoSDOutput = _VideoSDOutput_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 4),
    _VideoSDOutput_Type()
)
videoSDOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSDOutput.setStatus("current")


class _VideoBitRate_Type(DisplayString):
    """Custom type videoBitRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VideoBitRate_Type.__name__ = "DisplayString"
_VideoBitRate_Object = MibTableColumn
videoBitRate = _VideoBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 5),
    _VideoBitRate_Type()
)
videoBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoBitRate.setStatus("current")


class _Video32PullDown_Type(Integer32):
    """Custom type video32PullDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("recent", 3),
          ("yes", 1))
    )


_Video32PullDown_Type.__name__ = "Integer32"
_Video32PullDown_Object = MibTableColumn
video32PullDown = _Video32PullDown_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 6),
    _Video32PullDown_Type()
)
video32PullDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    video32PullDown.setStatus("current")


class _VideoFPS_Type(DisplayString):
    """Custom type videoFPS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VideoFPS_Type.__name__ = "DisplayString"
_VideoFPS_Object = MibTableColumn
videoFPS = _VideoFPS_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 7),
    _VideoFPS_Type()
)
videoFPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFPS.setStatus("current")


class _VideoSynchMode_Type(Integer32):
    """Custom type videoSynchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_VideoSynchMode_Type.__name__ = "Integer32"
_VideoSynchMode_Object = MibTableColumn
videoSynchMode = _VideoSynchMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 8),
    _VideoSynchMode_Type()
)
videoSynchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSynchMode.setStatus("current")


class _VideoEncoding_Type(Integer32):
    """Custom type videoEncoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("h264", 4),
          ("mpeg1", 2),
          ("mpeg2", 3),
          ("mpeg4p2", 6),
          ("unknown", 1),
          ("vc1", 5))
    )


_VideoEncoding_Type.__name__ = "Integer32"
_VideoEncoding_Object = MibTableColumn
videoEncoding = _VideoEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 9),
    _VideoEncoding_Type()
)
videoEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoEncoding.setStatus("current")


class _AspectRatioConversion_Type(Integer32):
    """Custom type aspectRatioConversion based on Integer32"""
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
        *(("fourByThreeCCO", 6),
          ("fourByThreeLetterBox", 2),
          ("fourByThreePBToFourteenByNinePB", 9),
          ("fourByThreePillarBox", 3),
          ("fourteenByNineLetterBox", 4),
          ("fourteenByNinePillarBox", 5),
          ("none", 1),
          ("sixteenByNineCCO", 7),
          ("sixteenByNineLBToFourteenByNineLB", 8))
    )


_AspectRatioConversion_Type.__name__ = "Integer32"
_AspectRatioConversion_Object = MibTableColumn
aspectRatioConversion = _AspectRatioConversion_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 10),
    _AspectRatioConversion_Type()
)
aspectRatioConversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioConversion.setStatus("current")


class _AspectRatioStreamAR_Type(Integer32):
    """Custom type aspectRatioStreamAR based on Integer32"""
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
        *(("fourByThree", 1),
          ("sixteenByNine", 2),
          ("square", 4),
          ("twoTwentyOneByHundred", 3),
          ("unavailable", 5))
    )


_AspectRatioStreamAR_Type.__name__ = "Integer32"
_AspectRatioStreamAR_Object = MibTableColumn
aspectRatioStreamAR = _AspectRatioStreamAR_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 11),
    _AspectRatioStreamAR_Type()
)
aspectRatioStreamAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioStreamAR.setStatus("current")


class _AspectRatioWSSMode_Type(Integer32):
    """Custom type aspectRatioWSSMode based on Integer32"""
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
        *(("autoCreate", 4),
          ("autoModify", 3),
          ("passthrough", 1),
          ("suppress", 2))
    )


_AspectRatioWSSMode_Type.__name__ = "Integer32"
_AspectRatioWSSMode_Object = MibTableColumn
aspectRatioWSSMode = _AspectRatioWSSMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 12),
    _AspectRatioWSSMode_Type()
)
aspectRatioWSSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aspectRatioWSSMode.setStatus("current")


class _AspectRatioWSSStatus_Type(Integer32):
    """Custom type aspectRatioWSSStatus based on Integer32"""
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
        *(("fourByThreeFullFormat", 1),
          ("fourteenByNineFullFormatCentre", 7),
          ("fourteenByNineLetterBoxCentre", 5),
          ("fourteenByNineLetterBoxTop", 6),
          ("greaterThanSixteenByNineLetterBoxCentre", 4),
          ("sixteenByNineFullFormat", 8),
          ("sixteenByNineLetterBoxCentre", 2),
          ("sixteenByNineLetterBoxTop", 3),
          ("undefined", 9))
    )


_AspectRatioWSSStatus_Type.__name__ = "Integer32"
_AspectRatioWSSStatus_Object = MibTableColumn
aspectRatioWSSStatus = _AspectRatioWSSStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 13),
    _AspectRatioWSSStatus_Type()
)
aspectRatioWSSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aspectRatioWSSStatus.setStatus("current")


class _ClosedCaptionActOP_Type(Integer32):
    """Custom type closedCaptionActOP based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("dvs157", 8),
          ("eia708", 3),
          ("reserved", 7),
          ("saCustom", 2),
          ("type3", 4),
          ("type4ATSC", 6),
          ("type4SA", 5))
    )


_ClosedCaptionActOP_Type.__name__ = "Integer32"
_ClosedCaptionActOP_Object = MibTableColumn
closedCaptionActOP = _ClosedCaptionActOP_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 14, 2, 1, 14),
    _ClosedCaptionActOP_Type()
)
closedCaptionActOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    closedCaptionActOP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-VIDEO-MIB",
    **{"ciscoDSGVideo": ciscoDSGVideo,
       "videoCtrlTable": videoCtrlTable,
       "videoCtrlEntry": videoCtrlEntry,
       "videoCtrlInstance": videoCtrlInstance,
       "videoPVFormat": videoPVFormat,
       "videoSDFormat": videoSDFormat,
       "videoTriSynch": videoTriSynch,
       "videoCutoff": videoCutoff,
       "aspectRatioSD": aspectRatioSD,
       "aspectRatioSelection": aspectRatioSelection,
       "closedCaptionPrefMode": closedCaptionPrefMode,
       "videoStatusTable": videoStatusTable,
       "videoStatusEntry": videoStatusEntry,
       "videoStatusInstance": videoStatusInstance,
       "videoStream": videoStream,
       "videoPVOutput": videoPVOutput,
       "videoSDOutput": videoSDOutput,
       "videoBitRate": videoBitRate,
       "video32PullDown": video32PullDown,
       "videoFPS": videoFPS,
       "videoSynchMode": videoSynchMode,
       "videoEncoding": videoEncoding,
       "aspectRatioConversion": aspectRatioConversion,
       "aspectRatioStreamAR": aspectRatioStreamAR,
       "aspectRatioWSSMode": aspectRatioWSSMode,
       "aspectRatioWSSStatus": aspectRatioWSSStatus,
       "closedCaptionActOP": closedCaptionActOP}
)
