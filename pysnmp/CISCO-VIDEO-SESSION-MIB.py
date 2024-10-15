# SNMP MIB module (CISCO-VIDEO-SESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VIDEO-SESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:05 2024
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

(cCallHistoryIndex,) = mibBuilder.importSymbols(
    "CISCO-DIAL-CONTROL-MIB",
    "cCallHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CvcVideoCodecAnnexMap,
 CvcVideoLevel,
 CvcVideoProfile,
 CvcVideoRtpPayloadFormat) = mibBuilder.importSymbols(
    "CISCO-VIDEO-TC",
    "CvcVideoCodecAnnexMap",
    "CvcVideoLevel",
    "CvcVideoProfile",
    "CvcVideoRtpPayloadFormat")

(CvcCallReferenceIdOrZero,
 CvcGUid,
 CvcVideoCoderRate) = mibBuilder.importSymbols(
    "CISCO-VOICE-COMMON-DIAL-CONTROL-MIB",
    "CvcCallReferenceIdOrZero",
    "CvcGUid",
    "CvcVideoCoderRate")

(AbsoluteCounter32,
 callActiveIndex,
 callActiveSetupTime) = mibBuilder.importSymbols(
    "DIAL-CONTROL-MIB",
    "AbsoluteCounter32",
    "callActiveIndex",
    "callActiveSetupTime")

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

ciscoVideoSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753)
)
ciscoVideoSessionMIB.setRevisions(
        ("2011-04-20 00:00",
         "2010-07-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvcVoIPCallServiceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("conferenceCall", 1),
          ("monitoredCall", 3),
          ("other", 255),
          ("pointToPointCall", 2))
    )



class CvcVideoLevel(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12,
              13,
              20,
              21,
              22,
              30,
              31,
              32,
              40,
              41,
              42,
              50,
              51,
              255)
        )
    )
    namedValues = NamedValues(
        *(("level1", 10),
          ("level11", 11),
          ("level12", 12),
          ("level13", 13),
          ("level1b", 9),
          ("level2", 20),
          ("level21", 21),
          ("level22", 22),
          ("level3", 30),
          ("level31", 31),
          ("level32", 32),
          ("level4", 40),
          ("level41", 41),
          ("level42", 42),
          ("level5", 50),
          ("level51", 51),
          ("other", 255))
    )



class CvcVideoProfile(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              255)
        )
    )
    namedValues = NamedValues(
        *(("h263Profile0", 10),
          ("h263Profile1", 11),
          ("h263Profile2", 12),
          ("h263Profile3", 13),
          ("h263Profile4", 14),
          ("h263Profile5", 15),
          ("h263Profile6", 16),
          ("h263Profile7", 17),
          ("h263Profile8", 18),
          ("h264ProfileBaseline", 100),
          ("h264ProfileCavlc444Intra", 110),
          ("h264ProfileExtended", 102),
          ("h264ProfileHigh", 103),
          ("h264ProfileHigh10", 104),
          ("h264ProfileHigh10Intra", 107),
          ("h264ProfileHigh422", 105),
          ("h264ProfileHigh422Intra", 108),
          ("h264ProfileHigh444Intra", 109),
          ("h264ProfileHigh444Predictive", 106),
          ("h264ProfileMain", 101),
          ("other", 255))
    )



class CvcVideoCodecAnnexMap(Bits, TextualConvention):
    status = "deprecated"


class CvcRtpPayloadFormat(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 255),
          ("rfc2190", 1),
          ("rfc2429", 2),
          ("rfc3984", 4),
          ("rfc4629", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVideoSessionMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVideoSessionMIBNotifs = _CiscoVideoSessionMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 0)
)
_CiscoVideoSessionMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVideoSessionMIBObjects = _CiscoVideoSessionMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1)
)
_CVideoSessionHistory_ObjectIdentity = ObjectIdentity
cVideoSessionHistory = _CVideoSessionHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1)
)
_CVideoCommonHistoryTable_Object = MibTable
cVideoCommonHistoryTable = _CVideoCommonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cVideoCommonHistoryTable.setStatus("current")
_CVideoCommonHistoryEntry_Object = MibTableRow
cVideoCommonHistoryEntry = _CVideoCommonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1)
)
cVideoCommonHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cVideoCommonHistoryEntry.setStatus("current")
_CVideoCommonHistoryConnectionId_Type = CvcGUid
_CVideoCommonHistoryConnectionId_Object = MibTableColumn
cVideoCommonHistoryConnectionId = _CVideoCommonHistoryConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 1),
    _CVideoCommonHistoryConnectionId_Type()
)
cVideoCommonHistoryConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryConnectionId.setStatus("current")
_CVideoCommonHistoryCallReferenceId_Type = CvcCallReferenceIdOrZero
_CVideoCommonHistoryCallReferenceId_Object = MibTableColumn
cVideoCommonHistoryCallReferenceId = _CVideoCommonHistoryCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 2),
    _CVideoCommonHistoryCallReferenceId_Type()
)
cVideoCommonHistoryCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryCallReferenceId.setStatus("current")
_CVideoCommonHistoryCallType_Type = CvcVoIPCallServiceType
_CVideoCommonHistoryCallType_Object = MibTableColumn
cVideoCommonHistoryCallType = _CVideoCommonHistoryCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 3),
    _CVideoCommonHistoryCallType_Type()
)
cVideoCommonHistoryCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryCallType.setStatus("current")
_CVideoCommonHistoryTxCodec_Type = CvcVideoCoderRate
_CVideoCommonHistoryTxCodec_Object = MibTableColumn
cVideoCommonHistoryTxCodec = _CVideoCommonHistoryTxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 4),
    _CVideoCommonHistoryTxCodec_Type()
)
cVideoCommonHistoryTxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxCodec.setStatus("current")
_CVideoCommonHistoryTxPictureWidth_Type = Unsigned32
_CVideoCommonHistoryTxPictureWidth_Object = MibTableColumn
cVideoCommonHistoryTxPictureWidth = _CVideoCommonHistoryTxPictureWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 5),
    _CVideoCommonHistoryTxPictureWidth_Type()
)
cVideoCommonHistoryTxPictureWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPictureWidth.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPictureWidth.setUnits("pixels")
_CVideoCommonHistoryTxPictureHeight_Type = Unsigned32
_CVideoCommonHistoryTxPictureHeight_Object = MibTableColumn
cVideoCommonHistoryTxPictureHeight = _CVideoCommonHistoryTxPictureHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 6),
    _CVideoCommonHistoryTxPictureHeight_Type()
)
cVideoCommonHistoryTxPictureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPictureHeight.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPictureHeight.setUnits("pixels")
_CVideoCommonHistoryTxConfigFrameRate_Type = Unsigned32
_CVideoCommonHistoryTxConfigFrameRate_Object = MibTableColumn
cVideoCommonHistoryTxConfigFrameRate = _CVideoCommonHistoryTxConfigFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 7),
    _CVideoCommonHistoryTxConfigFrameRate_Type()
)
cVideoCommonHistoryTxConfigFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxConfigFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxConfigFrameRate.setUnits("frames per second")
_CVideoCommonHistoryTxConfigBitrate_Type = Unsigned32
_CVideoCommonHistoryTxConfigBitrate_Object = MibTableColumn
cVideoCommonHistoryTxConfigBitrate = _CVideoCommonHistoryTxConfigBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 8),
    _CVideoCommonHistoryTxConfigBitrate_Type()
)
cVideoCommonHistoryTxConfigBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxConfigBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxConfigBitrate.setUnits("kilobits per second")
_CVideoCommonHistoryTxPayloadFormat_Type = CvcVideoRtpPayloadFormat
_CVideoCommonHistoryTxPayloadFormat_Object = MibTableColumn
cVideoCommonHistoryTxPayloadFormat = _CVideoCommonHistoryTxPayloadFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 9),
    _CVideoCommonHistoryTxPayloadFormat_Type()
)
cVideoCommonHistoryTxPayloadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPayloadFormat.setStatus("current")
_CVideoCommonHistoryTxAnnex_Type = CvcVideoCodecAnnexMap
_CVideoCommonHistoryTxAnnex_Object = MibTableColumn
cVideoCommonHistoryTxAnnex = _CVideoCommonHistoryTxAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 10),
    _CVideoCommonHistoryTxAnnex_Type()
)
cVideoCommonHistoryTxAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxAnnex.setStatus("current")
_CVideoCommonHistoryTxProfile_Type = CvcVideoProfile
_CVideoCommonHistoryTxProfile_Object = MibTableColumn
cVideoCommonHistoryTxProfile = _CVideoCommonHistoryTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 11),
    _CVideoCommonHistoryTxProfile_Type()
)
cVideoCommonHistoryTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxProfile.setStatus("current")
_CVideoCommonHistoryTxLevel_Type = CvcVideoLevel
_CVideoCommonHistoryTxLevel_Object = MibTableColumn
cVideoCommonHistoryTxLevel = _CVideoCommonHistoryTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 12),
    _CVideoCommonHistoryTxLevel_Type()
)
cVideoCommonHistoryTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxLevel.setStatus("current")
_CVideoCommonHistoryTxPackets_Type = AbsoluteCounter32
_CVideoCommonHistoryTxPackets_Object = MibTableColumn
cVideoCommonHistoryTxPackets = _CVideoCommonHistoryTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 13),
    _CVideoCommonHistoryTxPackets_Type()
)
cVideoCommonHistoryTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxPackets.setUnits("packets")
_CVideoCommonHistoryTxBytes_Type = Counter64
_CVideoCommonHistoryTxBytes_Object = MibTableColumn
cVideoCommonHistoryTxBytes = _CVideoCommonHistoryTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 14),
    _CVideoCommonHistoryTxBytes_Type()
)
cVideoCommonHistoryTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxBytes.setUnits("bytes")
_CVideoCommonHistoryTxDuration_Type = Unsigned32
_CVideoCommonHistoryTxDuration_Object = MibTableColumn
cVideoCommonHistoryTxDuration = _CVideoCommonHistoryTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 15),
    _CVideoCommonHistoryTxDuration_Type()
)
cVideoCommonHistoryTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryTxDuration.setUnits("seconds")
_CVideoCommonHistoryRxCodec_Type = CvcVideoCoderRate
_CVideoCommonHistoryRxCodec_Object = MibTableColumn
cVideoCommonHistoryRxCodec = _CVideoCommonHistoryRxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 16),
    _CVideoCommonHistoryRxCodec_Type()
)
cVideoCommonHistoryRxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxCodec.setStatus("current")
_CVideoCommonHistoryRxPictureWidth_Type = Unsigned32
_CVideoCommonHistoryRxPictureWidth_Object = MibTableColumn
cVideoCommonHistoryRxPictureWidth = _CVideoCommonHistoryRxPictureWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 17),
    _CVideoCommonHistoryRxPictureWidth_Type()
)
cVideoCommonHistoryRxPictureWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPictureWidth.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPictureWidth.setUnits("pixels")
_CVideoCommonHistoryRxPictureHeight_Type = Unsigned32
_CVideoCommonHistoryRxPictureHeight_Object = MibTableColumn
cVideoCommonHistoryRxPictureHeight = _CVideoCommonHistoryRxPictureHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 18),
    _CVideoCommonHistoryRxPictureHeight_Type()
)
cVideoCommonHistoryRxPictureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPictureHeight.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPictureHeight.setUnits("pixels")
_CVideoCommonHistoryRxConfigFrameRate_Type = Unsigned32
_CVideoCommonHistoryRxConfigFrameRate_Object = MibTableColumn
cVideoCommonHistoryRxConfigFrameRate = _CVideoCommonHistoryRxConfigFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 19),
    _CVideoCommonHistoryRxConfigFrameRate_Type()
)
cVideoCommonHistoryRxConfigFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxConfigFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxConfigFrameRate.setUnits("frames per second")
_CVideoCommonHistoryRxConfigBitrate_Type = Unsigned32
_CVideoCommonHistoryRxConfigBitrate_Object = MibTableColumn
cVideoCommonHistoryRxConfigBitrate = _CVideoCommonHistoryRxConfigBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 20),
    _CVideoCommonHistoryRxConfigBitrate_Type()
)
cVideoCommonHistoryRxConfigBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxConfigBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxConfigBitrate.setUnits("kilobits per second")
_CVideoCommonHistoryRxPayloadFormat_Type = CvcVideoRtpPayloadFormat
_CVideoCommonHistoryRxPayloadFormat_Object = MibTableColumn
cVideoCommonHistoryRxPayloadFormat = _CVideoCommonHistoryRxPayloadFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 21),
    _CVideoCommonHistoryRxPayloadFormat_Type()
)
cVideoCommonHistoryRxPayloadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPayloadFormat.setStatus("current")
_CVideoCommonHistoryRxAnnex_Type = CvcVideoCodecAnnexMap
_CVideoCommonHistoryRxAnnex_Object = MibTableColumn
cVideoCommonHistoryRxAnnex = _CVideoCommonHistoryRxAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 22),
    _CVideoCommonHistoryRxAnnex_Type()
)
cVideoCommonHistoryRxAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxAnnex.setStatus("current")
_CVideoCommonHistoryRxProfile_Type = CvcVideoProfile
_CVideoCommonHistoryRxProfile_Object = MibTableColumn
cVideoCommonHistoryRxProfile = _CVideoCommonHistoryRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 23),
    _CVideoCommonHistoryRxProfile_Type()
)
cVideoCommonHistoryRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxProfile.setStatus("current")
_CVideoCommonHistoryRxLevel_Type = CvcVideoLevel
_CVideoCommonHistoryRxLevel_Object = MibTableColumn
cVideoCommonHistoryRxLevel = _CVideoCommonHistoryRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 24),
    _CVideoCommonHistoryRxLevel_Type()
)
cVideoCommonHistoryRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxLevel.setStatus("current")
_CVideoCommonHistoryRxPackets_Type = AbsoluteCounter32
_CVideoCommonHistoryRxPackets_Object = MibTableColumn
cVideoCommonHistoryRxPackets = _CVideoCommonHistoryRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 25),
    _CVideoCommonHistoryRxPackets_Type()
)
cVideoCommonHistoryRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxPackets.setUnits("packets")
_CVideoCommonHistoryRxBytes_Type = Counter64
_CVideoCommonHistoryRxBytes_Object = MibTableColumn
cVideoCommonHistoryRxBytes = _CVideoCommonHistoryRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 26),
    _CVideoCommonHistoryRxBytes_Type()
)
cVideoCommonHistoryRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxBytes.setUnits("bytes")
_CVideoCommonHistoryRxDuration_Type = Unsigned32
_CVideoCommonHistoryRxDuration_Object = MibTableColumn
cVideoCommonHistoryRxDuration = _CVideoCommonHistoryRxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 27),
    _CVideoCommonHistoryRxDuration_Type()
)
cVideoCommonHistoryRxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonHistoryRxDuration.setUnits("seconds")
_CVideoCommonHistorySessionId_Type = Unsigned32
_CVideoCommonHistorySessionId_Object = MibTableColumn
cVideoCommonHistorySessionId = _CVideoCommonHistorySessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 1, 1, 28),
    _CVideoCommonHistorySessionId_Type()
)
cVideoCommonHistorySessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonHistorySessionId.setStatus("current")
_CVideoConfereeHistoryTable_Object = MibTable
cVideoConfereeHistoryTable = _CVideoConfereeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTable.setStatus("current")
_CVideoConfereeHistoryEntry_Object = MibTableRow
cVideoConfereeHistoryEntry = _CVideoConfereeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1)
)
cVideoConfereeHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cVideoConfereeHistoryEntry.setStatus("current")
_CVideoConfereeHistoryTotalDroppedPackets_Type = AbsoluteCounter32
_CVideoConfereeHistoryTotalDroppedPackets_Object = MibTableColumn
cVideoConfereeHistoryTotalDroppedPackets = _CVideoConfereeHistoryTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 1),
    _CVideoConfereeHistoryTotalDroppedPackets_Type()
)
cVideoConfereeHistoryTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalDroppedPackets.setUnits("packets")
_CVideoConfereeHistoryMaxJitter_Type = Gauge32
_CVideoConfereeHistoryMaxJitter_Object = MibTableColumn
cVideoConfereeHistoryMaxJitter = _CVideoConfereeHistoryMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 2),
    _CVideoConfereeHistoryMaxJitter_Type()
)
cVideoConfereeHistoryMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxJitter.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxJitter.setUnits("milliseconds")
_CVideoConfereeHistoryMaxDelay_Type = Gauge32
_CVideoConfereeHistoryMaxDelay_Object = MibTableColumn
cVideoConfereeHistoryMaxDelay = _CVideoConfereeHistoryMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 3),
    _CVideoConfereeHistoryMaxDelay_Type()
)
cVideoConfereeHistoryMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxDelay.setUnits("milliseconds")
_CVideoConfereeHistoryTotalOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoConfereeHistoryTotalOutOfOrderPackets_Object = MibTableColumn
cVideoConfereeHistoryTotalOutOfOrderPackets = _CVideoConfereeHistoryTotalOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 4),
    _CVideoConfereeHistoryTotalOutOfOrderPackets_Type()
)
cVideoConfereeHistoryTotalOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalOutOfOrderPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalOutOfOrderPackets.setUnits("packets")
_CVideoConfereeHistoryMaxOutOfSyncDelay_Type = Gauge32
_CVideoConfereeHistoryMaxOutOfSyncDelay_Object = MibTableColumn
cVideoConfereeHistoryMaxOutOfSyncDelay = _CVideoConfereeHistoryMaxOutOfSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 5),
    _CVideoConfereeHistoryMaxOutOfSyncDelay_Type()
)
cVideoConfereeHistoryMaxOutOfSyncDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxOutOfSyncDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryMaxOutOfSyncDelay.setUnits("milliseconds")
_CVideoConfereeHistoryTotalLostPackets_Type = AbsoluteCounter32
_CVideoConfereeHistoryTotalLostPackets_Object = MibTableColumn
cVideoConfereeHistoryTotalLostPackets = _CVideoConfereeHistoryTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 2, 1, 6),
    _CVideoConfereeHistoryTotalLostPackets_Type()
)
cVideoConfereeHistoryTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeHistoryTotalLostPackets.setUnits("packets")
_CVideoCallHistoryTable_Object = MibTable
cVideoCallHistoryTable = _CVideoCallHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cVideoCallHistoryTable.setStatus("current")
_CVideoCallHistoryEntry_Object = MibTableRow
cVideoCallHistoryEntry = _CVideoCallHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1)
)
cVideoCallHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cVideoCallHistoryEntry.setStatus("current")
_CVideoCallHistoryTxMacroblocksConcealed_Type = AbsoluteCounter32
_CVideoCallHistoryTxMacroblocksConcealed_Object = MibTableColumn
cVideoCallHistoryTxMacroblocksConcealed = _CVideoCallHistoryTxMacroblocksConcealed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 1),
    _CVideoCallHistoryTxMacroblocksConcealed_Type()
)
cVideoCallHistoryTxMacroblocksConcealed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxMacroblocksConcealed.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxMacroblocksConcealed.setUnits("macroblocks")
_CVideoCallHistoryTxFramesConcealed_Type = AbsoluteCounter32
_CVideoCallHistoryTxFramesConcealed_Object = MibTableColumn
cVideoCallHistoryTxFramesConcealed = _CVideoCallHistoryTxFramesConcealed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 2),
    _CVideoCallHistoryTxFramesConcealed_Type()
)
cVideoCallHistoryTxFramesConcealed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxFramesConcealed.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxFramesConcealed.setUnits("frames")
_CVideoCallHistoryTxBadHeaderPackets_Type = AbsoluteCounter32
_CVideoCallHistoryTxBadHeaderPackets_Object = MibTableColumn
cVideoCallHistoryTxBadHeaderPackets = _CVideoCallHistoryTxBadHeaderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 3),
    _CVideoCallHistoryTxBadHeaderPackets_Type()
)
cVideoCallHistoryTxBadHeaderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxBadHeaderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxBadHeaderPackets.setUnits("packets")
_CVideoCallHistoryTxOverflowPackets_Type = AbsoluteCounter32
_CVideoCallHistoryTxOverflowPackets_Object = MibTableColumn
cVideoCallHistoryTxOverflowPackets = _CVideoCallHistoryTxOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 4),
    _CVideoCallHistoryTxOverflowPackets_Type()
)
cVideoCallHistoryTxOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxOverflowPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxOverflowPackets.setUnits("packets")
_CVideoCallHistoryTxOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoCallHistoryTxOutOfOrderPackets_Object = MibTableColumn
cVideoCallHistoryTxOutOfOrderPackets = _CVideoCallHistoryTxOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 5),
    _CVideoCallHistoryTxOutOfOrderPackets_Type()
)
cVideoCallHistoryTxOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxOutOfOrderPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxOutOfOrderPackets.setUnits("packets")
_CVideoCallHistoryTxLostPackets_Type = AbsoluteCounter32
_CVideoCallHistoryTxLostPackets_Object = MibTableColumn
cVideoCallHistoryTxLostPackets = _CVideoCallHistoryTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 3, 1, 6),
    _CVideoCallHistoryTxLostPackets_Type()
)
cVideoCallHistoryTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoCallHistoryTxLostPackets.setUnits("packets")
_CVideoCommonStatsHistoryTable_Object = MibTable
cVideoCommonStatsHistoryTable = _CVideoCommonStatsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTable.setStatus("current")
_CVideoCommonStatsHistoryEntry_Object = MibTableRow
cVideoCommonStatsHistoryEntry = _CVideoCommonStatsHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1)
)
cVideoCommonStatsHistoryEntry.setIndexNames(
    (0, "CISCO-DIAL-CONTROL-MIB", "cCallHistoryIndex"),
)
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryEntry.setStatus("current")
_CVideoCommonStatsHistoryTxTotalLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsHistoryTxTotalLostPackets_Object = MibTableColumn
cVideoCommonStatsHistoryTxTotalLostPackets = _CVideoCommonStatsHistoryTxTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 1),
    _CVideoCommonStatsHistoryTxTotalLostPackets_Type()
)
cVideoCommonStatsHistoryTxTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxTotalLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxTotalLostPackets.setUnits("packets")


class _CVideoCommonStatsHistoryTxPercentLostPackets_Type(Unsigned32):
    """Custom type cVideoCommonStatsHistoryTxPercentLostPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CVideoCommonStatsHistoryTxPercentLostPackets_Type.__name__ = "Unsigned32"
_CVideoCommonStatsHistoryTxPercentLostPackets_Object = MibTableColumn
cVideoCommonStatsHistoryTxPercentLostPackets = _CVideoCommonStatsHistoryTxPercentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 2),
    _CVideoCommonStatsHistoryTxPercentLostPackets_Type()
)
cVideoCommonStatsHistoryTxPercentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxPercentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxPercentLostPackets.setUnits("percent")
_CVideoCommonStatsHistoryTxTotalOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoCommonStatsHistoryTxTotalOutOfOrderPackets_Object = MibTableColumn
cVideoCommonStatsHistoryTxTotalOutOfOrderPackets = _CVideoCommonStatsHistoryTxTotalOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 3),
    _CVideoCommonStatsHistoryTxTotalOutOfOrderPackets_Type()
)
cVideoCommonStatsHistoryTxTotalOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxTotalOutOfOrderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxTotalOutOfOrderPackets.setUnits("packets")
_CVideoCommonStatsHistoryTxMaxJitter_Type = Gauge32
_CVideoCommonStatsHistoryTxMaxJitter_Object = MibTableColumn
cVideoCommonStatsHistoryTxMaxJitter = _CVideoCommonStatsHistoryTxMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 4),
    _CVideoCommonStatsHistoryTxMaxJitter_Type()
)
cVideoCommonStatsHistoryTxMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxMaxJitter.setUnits("milliseconds")
_CVideoCommonStatsHistoryTxAvgJitter_Type = Gauge32
_CVideoCommonStatsHistoryTxAvgJitter_Object = MibTableColumn
cVideoCommonStatsHistoryTxAvgJitter = _CVideoCommonStatsHistoryTxAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 5),
    _CVideoCommonStatsHistoryTxAvgJitter_Type()
)
cVideoCommonStatsHistoryTxAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxAvgJitter.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxAvgJitter.setUnits("milliseconds")
_CVideoCommonStatsHistoryTxMaxDelay_Type = Gauge32
_CVideoCommonStatsHistoryTxMaxDelay_Object = MibTableColumn
cVideoCommonStatsHistoryTxMaxDelay = _CVideoCommonStatsHistoryTxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 6),
    _CVideoCommonStatsHistoryTxMaxDelay_Type()
)
cVideoCommonStatsHistoryTxMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxMaxDelay.setUnits("milliseconds")
_CVideoCommonStatsHistoryTxAvgDelay_Type = Gauge32
_CVideoCommonStatsHistoryTxAvgDelay_Object = MibTableColumn
cVideoCommonStatsHistoryTxAvgDelay = _CVideoCommonStatsHistoryTxAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 7),
    _CVideoCommonStatsHistoryTxAvgDelay_Type()
)
cVideoCommonStatsHistoryTxAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryTxAvgDelay.setUnits("milliseconds")
_CVideoCommonStatsHistoryRxTotalLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsHistoryRxTotalLostPackets_Object = MibTableColumn
cVideoCommonStatsHistoryRxTotalLostPackets = _CVideoCommonStatsHistoryRxTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 8),
    _CVideoCommonStatsHistoryRxTotalLostPackets_Type()
)
cVideoCommonStatsHistoryRxTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryRxTotalLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryRxTotalLostPackets.setUnits("packets")


class _CVideoCommonStatsHistoryRxPercentLostPackets_Type(Unsigned32):
    """Custom type cVideoCommonStatsHistoryRxPercentLostPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CVideoCommonStatsHistoryRxPercentLostPackets_Type.__name__ = "Unsigned32"
_CVideoCommonStatsHistoryRxPercentLostPackets_Object = MibTableColumn
cVideoCommonStatsHistoryRxPercentLostPackets = _CVideoCommonStatsHistoryRxPercentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 1, 4, 1, 9),
    _CVideoCommonStatsHistoryRxPercentLostPackets_Type()
)
cVideoCommonStatsHistoryRxPercentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryRxPercentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsHistoryRxPercentLostPackets.setUnits("percent")
_CVideoSessionActive_ObjectIdentity = ObjectIdentity
cVideoSessionActive = _CVideoSessionActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2)
)
_CVideoCommonActiveTable_Object = MibTable
cVideoCommonActiveTable = _CVideoCommonActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cVideoCommonActiveTable.setStatus("current")
_CVideoCommonActiveEntry_Object = MibTableRow
cVideoCommonActiveEntry = _CVideoCommonActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1)
)
cVideoCommonActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cVideoCommonActiveEntry.setStatus("current")
_CVideoCommonActiveConnectionId_Type = CvcGUid
_CVideoCommonActiveConnectionId_Object = MibTableColumn
cVideoCommonActiveConnectionId = _CVideoCommonActiveConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 1),
    _CVideoCommonActiveConnectionId_Type()
)
cVideoCommonActiveConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveConnectionId.setStatus("current")
_CVideoCommonActiveCallReferenceId_Type = CvcCallReferenceIdOrZero
_CVideoCommonActiveCallReferenceId_Object = MibTableColumn
cVideoCommonActiveCallReferenceId = _CVideoCommonActiveCallReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 2),
    _CVideoCommonActiveCallReferenceId_Type()
)
cVideoCommonActiveCallReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveCallReferenceId.setStatus("current")
_CVideoCommonActiveCallType_Type = CvcVoIPCallServiceType
_CVideoCommonActiveCallType_Object = MibTableColumn
cVideoCommonActiveCallType = _CVideoCommonActiveCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 3),
    _CVideoCommonActiveCallType_Type()
)
cVideoCommonActiveCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveCallType.setStatus("current")
_CVideoCommonActiveTxCodec_Type = CvcVideoCoderRate
_CVideoCommonActiveTxCodec_Object = MibTableColumn
cVideoCommonActiveTxCodec = _CVideoCommonActiveTxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 4),
    _CVideoCommonActiveTxCodec_Type()
)
cVideoCommonActiveTxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxCodec.setStatus("current")
_CVideoCommonActiveTxPictureWidth_Type = Unsigned32
_CVideoCommonActiveTxPictureWidth_Object = MibTableColumn
cVideoCommonActiveTxPictureWidth = _CVideoCommonActiveTxPictureWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 5),
    _CVideoCommonActiveTxPictureWidth_Type()
)
cVideoCommonActiveTxPictureWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPictureWidth.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPictureWidth.setUnits("pixels")
_CVideoCommonActiveTxPictureHeight_Type = Unsigned32
_CVideoCommonActiveTxPictureHeight_Object = MibTableColumn
cVideoCommonActiveTxPictureHeight = _CVideoCommonActiveTxPictureHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 6),
    _CVideoCommonActiveTxPictureHeight_Type()
)
cVideoCommonActiveTxPictureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPictureHeight.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPictureHeight.setUnits("pixels")
_CVideoCommonActiveTxConfigFrameRate_Type = Unsigned32
_CVideoCommonActiveTxConfigFrameRate_Object = MibTableColumn
cVideoCommonActiveTxConfigFrameRate = _CVideoCommonActiveTxConfigFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 7),
    _CVideoCommonActiveTxConfigFrameRate_Type()
)
cVideoCommonActiveTxConfigFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxConfigFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxConfigFrameRate.setUnits("frames per second")
_CVideoCommonActiveTxConfigBitrate_Type = Unsigned32
_CVideoCommonActiveTxConfigBitrate_Object = MibTableColumn
cVideoCommonActiveTxConfigBitrate = _CVideoCommonActiveTxConfigBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 8),
    _CVideoCommonActiveTxConfigBitrate_Type()
)
cVideoCommonActiveTxConfigBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxConfigBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxConfigBitrate.setUnits("kilobits per second")
_CVideoCommonActiveTxPayloadFormat_Type = CvcVideoRtpPayloadFormat
_CVideoCommonActiveTxPayloadFormat_Object = MibTableColumn
cVideoCommonActiveTxPayloadFormat = _CVideoCommonActiveTxPayloadFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 9),
    _CVideoCommonActiveTxPayloadFormat_Type()
)
cVideoCommonActiveTxPayloadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPayloadFormat.setStatus("current")
_CVideoCommonActiveTxAnnex_Type = CvcVideoCodecAnnexMap
_CVideoCommonActiveTxAnnex_Object = MibTableColumn
cVideoCommonActiveTxAnnex = _CVideoCommonActiveTxAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 10),
    _CVideoCommonActiveTxAnnex_Type()
)
cVideoCommonActiveTxAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxAnnex.setStatus("current")
_CVideoCommonActiveTxProfile_Type = CvcVideoProfile
_CVideoCommonActiveTxProfile_Object = MibTableColumn
cVideoCommonActiveTxProfile = _CVideoCommonActiveTxProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 11),
    _CVideoCommonActiveTxProfile_Type()
)
cVideoCommonActiveTxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxProfile.setStatus("current")
_CVideoCommonActiveTxLevel_Type = CvcVideoLevel
_CVideoCommonActiveTxLevel_Object = MibTableColumn
cVideoCommonActiveTxLevel = _CVideoCommonActiveTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 12),
    _CVideoCommonActiveTxLevel_Type()
)
cVideoCommonActiveTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxLevel.setStatus("current")
_CVideoCommonActiveTxPackets_Type = AbsoluteCounter32
_CVideoCommonActiveTxPackets_Object = MibTableColumn
cVideoCommonActiveTxPackets = _CVideoCommonActiveTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 13),
    _CVideoCommonActiveTxPackets_Type()
)
cVideoCommonActiveTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxPackets.setUnits("packets")
_CVideoCommonActiveTxBytes_Type = Counter64
_CVideoCommonActiveTxBytes_Object = MibTableColumn
cVideoCommonActiveTxBytes = _CVideoCommonActiveTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 14),
    _CVideoCommonActiveTxBytes_Type()
)
cVideoCommonActiveTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxBytes.setUnits("bytes")
_CVideoCommonActiveTxDuration_Type = Unsigned32
_CVideoCommonActiveTxDuration_Object = MibTableColumn
cVideoCommonActiveTxDuration = _CVideoCommonActiveTxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 15),
    _CVideoCommonActiveTxDuration_Type()
)
cVideoCommonActiveTxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveTxDuration.setUnits("seconds")
_CVideoCommonActiveRxCodec_Type = CvcVideoCoderRate
_CVideoCommonActiveRxCodec_Object = MibTableColumn
cVideoCommonActiveRxCodec = _CVideoCommonActiveRxCodec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 16),
    _CVideoCommonActiveRxCodec_Type()
)
cVideoCommonActiveRxCodec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxCodec.setStatus("current")
_CVideoCommonActiveRxPictureWidth_Type = Unsigned32
_CVideoCommonActiveRxPictureWidth_Object = MibTableColumn
cVideoCommonActiveRxPictureWidth = _CVideoCommonActiveRxPictureWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 17),
    _CVideoCommonActiveRxPictureWidth_Type()
)
cVideoCommonActiveRxPictureWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPictureWidth.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPictureWidth.setUnits("pixels")
_CVideoCommonActiveRxPictureHeight_Type = Unsigned32
_CVideoCommonActiveRxPictureHeight_Object = MibTableColumn
cVideoCommonActiveRxPictureHeight = _CVideoCommonActiveRxPictureHeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 18),
    _CVideoCommonActiveRxPictureHeight_Type()
)
cVideoCommonActiveRxPictureHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPictureHeight.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPictureHeight.setUnits("pixels")
_CVideoCommonActiveRxConfigFrameRate_Type = Unsigned32
_CVideoCommonActiveRxConfigFrameRate_Object = MibTableColumn
cVideoCommonActiveRxConfigFrameRate = _CVideoCommonActiveRxConfigFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 19),
    _CVideoCommonActiveRxConfigFrameRate_Type()
)
cVideoCommonActiveRxConfigFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxConfigFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxConfigFrameRate.setUnits("frames per second")
_CVideoCommonActiveRxConfigBitrate_Type = Unsigned32
_CVideoCommonActiveRxConfigBitrate_Object = MibTableColumn
cVideoCommonActiveRxConfigBitrate = _CVideoCommonActiveRxConfigBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 20),
    _CVideoCommonActiveRxConfigBitrate_Type()
)
cVideoCommonActiveRxConfigBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxConfigBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxConfigBitrate.setUnits("kilobits per second")
_CVideoCommonActiveRxPayloadFormat_Type = CvcVideoRtpPayloadFormat
_CVideoCommonActiveRxPayloadFormat_Object = MibTableColumn
cVideoCommonActiveRxPayloadFormat = _CVideoCommonActiveRxPayloadFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 21),
    _CVideoCommonActiveRxPayloadFormat_Type()
)
cVideoCommonActiveRxPayloadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPayloadFormat.setStatus("current")
_CVideoCommonActiveRxAnnex_Type = CvcVideoCodecAnnexMap
_CVideoCommonActiveRxAnnex_Object = MibTableColumn
cVideoCommonActiveRxAnnex = _CVideoCommonActiveRxAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 22),
    _CVideoCommonActiveRxAnnex_Type()
)
cVideoCommonActiveRxAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxAnnex.setStatus("current")
_CVideoCommonActiveRxProfile_Type = CvcVideoProfile
_CVideoCommonActiveRxProfile_Object = MibTableColumn
cVideoCommonActiveRxProfile = _CVideoCommonActiveRxProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 23),
    _CVideoCommonActiveRxProfile_Type()
)
cVideoCommonActiveRxProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxProfile.setStatus("current")
_CVideoCommonActiveRxLevel_Type = CvcVideoLevel
_CVideoCommonActiveRxLevel_Object = MibTableColumn
cVideoCommonActiveRxLevel = _CVideoCommonActiveRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 24),
    _CVideoCommonActiveRxLevel_Type()
)
cVideoCommonActiveRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxLevel.setStatus("current")
_CVideoCommonActiveRxPackets_Type = AbsoluteCounter32
_CVideoCommonActiveRxPackets_Object = MibTableColumn
cVideoCommonActiveRxPackets = _CVideoCommonActiveRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 25),
    _CVideoCommonActiveRxPackets_Type()
)
cVideoCommonActiveRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxPackets.setUnits("packets")
_CVideoCommonActiveRxBytes_Type = Counter64
_CVideoCommonActiveRxBytes_Object = MibTableColumn
cVideoCommonActiveRxBytes = _CVideoCommonActiveRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 26),
    _CVideoCommonActiveRxBytes_Type()
)
cVideoCommonActiveRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxBytes.setUnits("bytes")
_CVideoCommonActiveRxDuration_Type = Unsigned32
_CVideoCommonActiveRxDuration_Object = MibTableColumn
cVideoCommonActiveRxDuration = _CVideoCommonActiveRxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 27),
    _CVideoCommonActiveRxDuration_Type()
)
cVideoCommonActiveRxDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxDuration.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonActiveRxDuration.setUnits("seconds")
_CVideoCommonActiveSessionId_Type = Unsigned32
_CVideoCommonActiveSessionId_Object = MibTableColumn
cVideoCommonActiveSessionId = _CVideoCommonActiveSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 1, 1, 28),
    _CVideoCommonActiveSessionId_Type()
)
cVideoCommonActiveSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonActiveSessionId.setStatus("current")
_CVideoConfereeActiveTable_Object = MibTable
cVideoConfereeActiveTable = _CVideoConfereeActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cVideoConfereeActiveTable.setStatus("current")
_CVideoConfereeActiveEntry_Object = MibTableRow
cVideoConfereeActiveEntry = _CVideoConfereeActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1)
)
cVideoConfereeActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cVideoConfereeActiveEntry.setStatus("current")
_CVideoConfereeActiveActualFrameRate_Type = Unsigned32
_CVideoConfereeActiveActualFrameRate_Object = MibTableColumn
cVideoConfereeActiveActualFrameRate = _CVideoConfereeActiveActualFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 1),
    _CVideoConfereeActiveActualFrameRate_Type()
)
cVideoConfereeActiveActualFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveActualFrameRate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeActiveActualFrameRate.setUnits("frames per second")
_CVideoConfereeActiveActualBitrate_Type = Unsigned32
_CVideoConfereeActiveActualBitrate_Object = MibTableColumn
cVideoConfereeActiveActualBitrate = _CVideoConfereeActiveActualBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 2),
    _CVideoConfereeActiveActualBitrate_Type()
)
cVideoConfereeActiveActualBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveActualBitrate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveActualBitrate.setUnits("kilobits per second")
_CVideoConfereeActiveTotalDroppedPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveTotalDroppedPackets_Object = MibTableColumn
cVideoConfereeActiveTotalDroppedPackets = _CVideoConfereeActiveTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 3),
    _CVideoConfereeActiveTotalDroppedPackets_Type()
)
cVideoConfereeActiveTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalDroppedPackets.setUnits("packets")
_CVideoConfereeActiveCurrentDroppedPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveCurrentDroppedPackets_Object = MibTableColumn
cVideoConfereeActiveCurrentDroppedPackets = _CVideoConfereeActiveCurrentDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 4),
    _CVideoConfereeActiveCurrentDroppedPackets_Type()
)
cVideoConfereeActiveCurrentDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentDroppedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentDroppedPackets.setUnits("packets")
_CVideoConfereeActiveTotalOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveTotalOutOfOrderPackets_Object = MibTableColumn
cVideoConfereeActiveTotalOutOfOrderPackets = _CVideoConfereeActiveTotalOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 5),
    _CVideoConfereeActiveTotalOutOfOrderPackets_Type()
)
cVideoConfereeActiveTotalOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalOutOfOrderPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalOutOfOrderPackets.setUnits("packets")
_CVideoConfereeActiveCurrentOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveCurrentOutOfOrderPackets_Object = MibTableColumn
cVideoConfereeActiveCurrentOutOfOrderPackets = _CVideoConfereeActiveCurrentOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 6),
    _CVideoConfereeActiveCurrentOutOfOrderPackets_Type()
)
cVideoConfereeActiveCurrentOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentOutOfOrderPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentOutOfOrderPackets.setUnits("packets")
_CVideoConfereeActiveTotalLostPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveTotalLostPackets_Object = MibTableColumn
cVideoConfereeActiveTotalLostPackets = _CVideoConfereeActiveTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 7),
    _CVideoConfereeActiveTotalLostPackets_Type()
)
cVideoConfereeActiveTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveTotalLostPackets.setUnits("packets")
_CVideoConfereeActiveCurrentLostPackets_Type = AbsoluteCounter32
_CVideoConfereeActiveCurrentLostPackets_Object = MibTableColumn
cVideoConfereeActiveCurrentLostPackets = _CVideoConfereeActiveCurrentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 8),
    _CVideoConfereeActiveCurrentLostPackets_Type()
)
cVideoConfereeActiveCurrentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentLostPackets.setUnits("packets")
_CVideoConfereeActiveMaxJitter_Type = Gauge32
_CVideoConfereeActiveMaxJitter_Object = MibTableColumn
cVideoConfereeActiveMaxJitter = _CVideoConfereeActiveMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 9),
    _CVideoConfereeActiveMaxJitter_Type()
)
cVideoConfereeActiveMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxJitter.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxJitter.setUnits("milliseconds")
_CVideoConfereeActiveCurrentJitter_Type = Gauge32
_CVideoConfereeActiveCurrentJitter_Object = MibTableColumn
cVideoConfereeActiveCurrentJitter = _CVideoConfereeActiveCurrentJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 10),
    _CVideoConfereeActiveCurrentJitter_Type()
)
cVideoConfereeActiveCurrentJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentJitter.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentJitter.setUnits("milliseconds")
_CVideoConfereeActiveMaxDelay_Type = Gauge32
_CVideoConfereeActiveMaxDelay_Object = MibTableColumn
cVideoConfereeActiveMaxDelay = _CVideoConfereeActiveMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 11),
    _CVideoConfereeActiveMaxDelay_Type()
)
cVideoConfereeActiveMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxDelay.setUnits("milliseconds")
_CVideoConfereeActiveCurrentDelay_Type = Gauge32
_CVideoConfereeActiveCurrentDelay_Object = MibTableColumn
cVideoConfereeActiveCurrentDelay = _CVideoConfereeActiveCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 12),
    _CVideoConfereeActiveCurrentDelay_Type()
)
cVideoConfereeActiveCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentDelay.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentDelay.setUnits("milliseconds")
_CVideoConfereeActiveMaxOutOfSyncDelay_Type = Gauge32
_CVideoConfereeActiveMaxOutOfSyncDelay_Object = MibTableColumn
cVideoConfereeActiveMaxOutOfSyncDelay = _CVideoConfereeActiveMaxOutOfSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 13),
    _CVideoConfereeActiveMaxOutOfSyncDelay_Type()
)
cVideoConfereeActiveMaxOutOfSyncDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxOutOfSyncDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeActiveMaxOutOfSyncDelay.setUnits("milliseconds")
_CVideoConfereeActiveCurrentOutOfSyncDelay_Type = Gauge32
_CVideoConfereeActiveCurrentOutOfSyncDelay_Object = MibTableColumn
cVideoConfereeActiveCurrentOutOfSyncDelay = _CVideoConfereeActiveCurrentOutOfSyncDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 14),
    _CVideoConfereeActiveCurrentOutOfSyncDelay_Type()
)
cVideoConfereeActiveCurrentOutOfSyncDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentOutOfSyncDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoConfereeActiveCurrentOutOfSyncDelay.setUnits("milliseconds")
_CVideoConfereeActiveFastVideoUpdateRate_Type = AbsoluteCounter32
_CVideoConfereeActiveFastVideoUpdateRate_Object = MibTableColumn
cVideoConfereeActiveFastVideoUpdateRate = _CVideoConfereeActiveFastVideoUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 2, 1, 15),
    _CVideoConfereeActiveFastVideoUpdateRate_Type()
)
cVideoConfereeActiveFastVideoUpdateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoConfereeActiveFastVideoUpdateRate.setStatus("current")
_CVideoCallActiveTable_Object = MibTable
cVideoCallActiveTable = _CVideoCallActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cVideoCallActiveTable.setStatus("current")
_CVideoCallActiveEntry_Object = MibTableRow
cVideoCallActiveEntry = _CVideoCallActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1)
)
cVideoCallActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cVideoCallActiveEntry.setStatus("current")
_CVideoCallActiveRxActualBitrate_Type = Unsigned32
_CVideoCallActiveRxActualBitrate_Object = MibTableColumn
cVideoCallActiveRxActualBitrate = _CVideoCallActiveRxActualBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 1),
    _CVideoCallActiveRxActualBitrate_Type()
)
cVideoCallActiveRxActualBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveRxActualBitrate.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoCallActiveRxActualBitrate.setUnits("kilobits per second")
_CVideoCallActiveTxMacroblocksConcealed_Type = AbsoluteCounter32
_CVideoCallActiveTxMacroblocksConcealed_Object = MibTableColumn
cVideoCallActiveTxMacroblocksConcealed = _CVideoCallActiveTxMacroblocksConcealed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 2),
    _CVideoCallActiveTxMacroblocksConcealed_Type()
)
cVideoCallActiveTxMacroblocksConcealed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveTxMacroblocksConcealed.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallActiveTxMacroblocksConcealed.setUnits("macroblocks")
_CVideoCallActiveTxFramesConcealed_Type = AbsoluteCounter32
_CVideoCallActiveTxFramesConcealed_Object = MibTableColumn
cVideoCallActiveTxFramesConcealed = _CVideoCallActiveTxFramesConcealed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 3),
    _CVideoCallActiveTxFramesConcealed_Type()
)
cVideoCallActiveTxFramesConcealed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveTxFramesConcealed.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallActiveTxFramesConcealed.setUnits("frames")
_CVideoCallActiveTxBadHeaderPackets_Type = AbsoluteCounter32
_CVideoCallActiveTxBadHeaderPackets_Object = MibTableColumn
cVideoCallActiveTxBadHeaderPackets = _CVideoCallActiveTxBadHeaderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 4),
    _CVideoCallActiveTxBadHeaderPackets_Type()
)
cVideoCallActiveTxBadHeaderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveTxBadHeaderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallActiveTxBadHeaderPackets.setUnits("packets")
_CVideoCallActiveTxOverflowPackets_Type = AbsoluteCounter32
_CVideoCallActiveTxOverflowPackets_Object = MibTableColumn
cVideoCallActiveTxOverflowPackets = _CVideoCallActiveTxOverflowPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 5),
    _CVideoCallActiveTxOverflowPackets_Type()
)
cVideoCallActiveTxOverflowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveTxOverflowPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCallActiveTxOverflowPackets.setUnits("packets")
_CVideoCallActiveTxLostPackets_Type = AbsoluteCounter32
_CVideoCallActiveTxLostPackets_Object = MibTableColumn
cVideoCallActiveTxLostPackets = _CVideoCallActiveTxLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 3, 1, 6),
    _CVideoCallActiveTxLostPackets_Type()
)
cVideoCallActiveTxLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCallActiveTxLostPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cVideoCallActiveTxLostPackets.setUnits("packets")
_CVideoCommonStatsActiveTable_Object = MibTable
cVideoCommonStatsActiveTable = _CVideoCommonStatsActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTable.setStatus("current")
_CVideoCommonStatsActiveEntry_Object = MibTableRow
cVideoCommonStatsActiveEntry = _CVideoCommonStatsActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1)
)
cVideoCommonStatsActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveEntry.setStatus("current")
_CVideoCommonStatsActiveTxActualBitrate_Type = Unsigned32
_CVideoCommonStatsActiveTxActualBitrate_Object = MibTableColumn
cVideoCommonStatsActiveTxActualBitrate = _CVideoCommonStatsActiveTxActualBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 1),
    _CVideoCommonStatsActiveTxActualBitrate_Type()
)
cVideoCommonStatsActiveTxActualBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxActualBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxActualBitrate.setUnits("kilobits per second")
_CVideoCommonStatsActiveTxTotalLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveTxTotalLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveTxTotalLostPackets = _CVideoCommonStatsActiveTxTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 2),
    _CVideoCommonStatsActiveTxTotalLostPackets_Type()
)
cVideoCommonStatsActiveTxTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxTotalLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxTotalLostPackets.setUnits("packets")


class _CVideoCommonStatsActiveTxPercentLostPackets_Type(Unsigned32):
    """Custom type cVideoCommonStatsActiveTxPercentLostPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CVideoCommonStatsActiveTxPercentLostPackets_Type.__name__ = "Unsigned32"
_CVideoCommonStatsActiveTxPercentLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveTxPercentLostPackets = _CVideoCommonStatsActiveTxPercentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 3),
    _CVideoCommonStatsActiveTxPercentLostPackets_Type()
)
cVideoCommonStatsActiveTxPercentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxPercentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxPercentLostPackets.setUnits("percent")
_CVideoCommonStatsActiveTxCurrentLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveTxCurrentLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveTxCurrentLostPackets = _CVideoCommonStatsActiveTxCurrentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 4),
    _CVideoCommonStatsActiveTxCurrentLostPackets_Type()
)
cVideoCommonStatsActiveTxCurrentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentLostPackets.setUnits("packets")
_CVideoCommonStatsActiveTxTotalOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveTxTotalOutOfOrderPackets_Object = MibTableColumn
cVideoCommonStatsActiveTxTotalOutOfOrderPackets = _CVideoCommonStatsActiveTxTotalOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 5),
    _CVideoCommonStatsActiveTxTotalOutOfOrderPackets_Type()
)
cVideoCommonStatsActiveTxTotalOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxTotalOutOfOrderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxTotalOutOfOrderPackets.setUnits("packets")
_CVideoCommonStatsActiveTxCurrentOutOfOrderPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveTxCurrentOutOfOrderPackets_Object = MibTableColumn
cVideoCommonStatsActiveTxCurrentOutOfOrderPackets = _CVideoCommonStatsActiveTxCurrentOutOfOrderPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 6),
    _CVideoCommonStatsActiveTxCurrentOutOfOrderPackets_Type()
)
cVideoCommonStatsActiveTxCurrentOutOfOrderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentOutOfOrderPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentOutOfOrderPackets.setUnits("packets")
_CVideoCommonStatsActiveTxMaxJitter_Type = Gauge32
_CVideoCommonStatsActiveTxMaxJitter_Object = MibTableColumn
cVideoCommonStatsActiveTxMaxJitter = _CVideoCommonStatsActiveTxMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 7),
    _CVideoCommonStatsActiveTxMaxJitter_Type()
)
cVideoCommonStatsActiveTxMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxMaxJitter.setUnits("milliseconds")
_CVideoCommonStatsActiveTxAvgJitter_Type = Gauge32
_CVideoCommonStatsActiveTxAvgJitter_Object = MibTableColumn
cVideoCommonStatsActiveTxAvgJitter = _CVideoCommonStatsActiveTxAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 8),
    _CVideoCommonStatsActiveTxAvgJitter_Type()
)
cVideoCommonStatsActiveTxAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxAvgJitter.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxAvgJitter.setUnits("milliseconds")
_CVideoCommonStatsActiveTxCurrentJitter_Type = Gauge32
_CVideoCommonStatsActiveTxCurrentJitter_Object = MibTableColumn
cVideoCommonStatsActiveTxCurrentJitter = _CVideoCommonStatsActiveTxCurrentJitter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 9),
    _CVideoCommonStatsActiveTxCurrentJitter_Type()
)
cVideoCommonStatsActiveTxCurrentJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentJitter.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentJitter.setUnits("milliseconds")
_CVideoCommonStatsActiveTxMaxDelay_Type = Gauge32
_CVideoCommonStatsActiveTxMaxDelay_Object = MibTableColumn
cVideoCommonStatsActiveTxMaxDelay = _CVideoCommonStatsActiveTxMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 10),
    _CVideoCommonStatsActiveTxMaxDelay_Type()
)
cVideoCommonStatsActiveTxMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxMaxDelay.setUnits("milliseconds")
_CVideoCommonStatsActiveTxAvgDelay_Type = Gauge32
_CVideoCommonStatsActiveTxAvgDelay_Object = MibTableColumn
cVideoCommonStatsActiveTxAvgDelay = _CVideoCommonStatsActiveTxAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 11),
    _CVideoCommonStatsActiveTxAvgDelay_Type()
)
cVideoCommonStatsActiveTxAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxAvgDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxAvgDelay.setUnits("milliseconds")
_CVideoCommonStatsActiveTxCurrentDelay_Type = Gauge32
_CVideoCommonStatsActiveTxCurrentDelay_Object = MibTableColumn
cVideoCommonStatsActiveTxCurrentDelay = _CVideoCommonStatsActiveTxCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 12),
    _CVideoCommonStatsActiveTxCurrentDelay_Type()
)
cVideoCommonStatsActiveTxCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentDelay.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveTxCurrentDelay.setUnits("milliseconds")
_CVideoCommonStatsActiveRxActualBitrate_Type = Unsigned32
_CVideoCommonStatsActiveRxActualBitrate_Object = MibTableColumn
cVideoCommonStatsActiveRxActualBitrate = _CVideoCommonStatsActiveRxActualBitrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 13),
    _CVideoCommonStatsActiveRxActualBitrate_Type()
)
cVideoCommonStatsActiveRxActualBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxActualBitrate.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxActualBitrate.setUnits("kilobits per second")
_CVideoCommonStatsActiveRxTotalLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveRxTotalLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveRxTotalLostPackets = _CVideoCommonStatsActiveRxTotalLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 14),
    _CVideoCommonStatsActiveRxTotalLostPackets_Type()
)
cVideoCommonStatsActiveRxTotalLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxTotalLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxTotalLostPackets.setUnits("packets")


class _CVideoCommonStatsActiveRxPercentLostPackets_Type(Unsigned32):
    """Custom type cVideoCommonStatsActiveRxPercentLostPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CVideoCommonStatsActiveRxPercentLostPackets_Type.__name__ = "Unsigned32"
_CVideoCommonStatsActiveRxPercentLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveRxPercentLostPackets = _CVideoCommonStatsActiveRxPercentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 15),
    _CVideoCommonStatsActiveRxPercentLostPackets_Type()
)
cVideoCommonStatsActiveRxPercentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxPercentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxPercentLostPackets.setUnits("percent")
_CVideoCommonStatsActiveRxCurrentLostPackets_Type = AbsoluteCounter32
_CVideoCommonStatsActiveRxCurrentLostPackets_Object = MibTableColumn
cVideoCommonStatsActiveRxCurrentLostPackets = _CVideoCommonStatsActiveRxCurrentLostPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 1, 2, 4, 1, 16),
    _CVideoCommonStatsActiveRxCurrentLostPackets_Type()
)
cVideoCommonStatsActiveRxCurrentLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxCurrentLostPackets.setStatus("current")
if mibBuilder.loadTexts:
    cVideoCommonStatsActiveRxCurrentLostPackets.setUnits("packets")
_CiscoVideoSessionMIBConform_ObjectIdentity = ObjectIdentity
ciscoVideoSessionMIBConform = _CiscoVideoSessionMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2)
)
_CiscoVideoSessionMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVideoSessionMIBCompliances = _CiscoVideoSessionMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 1)
)
_CiscoVideoSessionMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVideoSessionMIBGroups = _CiscoVideoSessionMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2)
)

# Managed Objects groups

cVideoSessionHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 1)
)
cVideoSessionHistoryGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryConnectionId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryCallReferenceId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryCallType"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryTotalDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryMaxJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryMaxDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryTotalOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryMaxOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxMacroblocksConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxFramesConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxBadHeaderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxOverflowPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxLostPackets"))
)
if mibBuilder.loadTexts:
    cVideoSessionHistoryGroup.setStatus("deprecated")

cVideoSessionActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 2)
)
cVideoSessionActiveGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveConnectionId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveCallReferenceId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveCallType"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveActualFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveActualBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveTotalDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveTotalOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveMaxJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveMaxDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveMaxOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveFastVideoUpdateRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveRxActualBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxMacroblocksConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxFramesConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxBadHeaderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxOverflowPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxLostPackets"))
)
if mibBuilder.loadTexts:
    cVideoSessionActiveGroup.setStatus("deprecated")

cVideoSessionCommonStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 3)
)
cVideoSessionCommonStatusGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryConnectionId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryCallReferenceId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryCallType"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryTxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistoryRxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonHistorySessionId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveConnectionId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveCallReferenceId"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveCallType"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveTxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxCodec"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPictureWidth"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPictureHeight"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxConfigFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxConfigBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPayloadFormat"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxAnnex"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxProfile"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxLevel"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxBytes"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveRxDuration"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonActiveSessionId"))
)
if mibBuilder.loadTexts:
    cVideoSessionCommonStatusGroup.setStatus("current")

cVideoSessionCommonStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 4)
)
cVideoSessionCommonStatisticsGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxPercentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxTotalOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxMaxJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxAvgJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxMaxDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryTxAvgDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryRxTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsHistoryRxPercentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxActualBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxPercentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxCurrentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxTotalOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxCurrentOutOfOrderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxMaxJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxAvgJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxCurrentJitter"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxMaxDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxAvgDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveTxCurrentDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveRxActualBitrate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveRxTotalLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveRxPercentLostPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCommonStatsActiveRxCurrentLostPackets"))
)
if mibBuilder.loadTexts:
    cVideoSessionCommonStatisticsGroup.setStatus("current")

cVideoSessionCallStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 5)
)
cVideoSessionCallStatisticsGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxMacroblocksConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxFramesConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxBadHeaderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallHistoryTxOverflowPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxMacroblocksConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxFramesConcealed"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxBadHeaderPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoCallActiveTxOverflowPackets"))
)
if mibBuilder.loadTexts:
    cVideoSessionCallStatisticsGroup.setStatus("current")

cVideoSessionConfereeStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 2, 6)
)
cVideoSessionConfereeStatisticsGroup.setObjects(
      *(("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryTotalDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeHistoryMaxOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveActualFrameRate"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveTotalDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentDroppedPackets"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveMaxOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveCurrentOutOfSyncDelay"),
        ("CISCO-VIDEO-SESSION-MIB", "cVideoConfereeActiveFastVideoUpdateRate"))
)
if mibBuilder.loadTexts:
    cVideoSessionConfereeStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cVideoSessionMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cVideoSessionMIBCompliance.setStatus(
        "deprecated"
    )

cVideoSessionMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 753, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cVideoSessionMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VIDEO-SESSION-MIB",
    **{"CvcVoIPCallServiceType": CvcVoIPCallServiceType,
       "CvcVideoLevel": CvcVideoLevel,
       "CvcVideoProfile": CvcVideoProfile,
       "CvcVideoCodecAnnexMap": CvcVideoCodecAnnexMap,
       "CvcRtpPayloadFormat": CvcRtpPayloadFormat,
       "ciscoVideoSessionMIB": ciscoVideoSessionMIB,
       "ciscoVideoSessionMIBNotifs": ciscoVideoSessionMIBNotifs,
       "ciscoVideoSessionMIBObjects": ciscoVideoSessionMIBObjects,
       "cVideoSessionHistory": cVideoSessionHistory,
       "cVideoCommonHistoryTable": cVideoCommonHistoryTable,
       "cVideoCommonHistoryEntry": cVideoCommonHistoryEntry,
       "cVideoCommonHistoryConnectionId": cVideoCommonHistoryConnectionId,
       "cVideoCommonHistoryCallReferenceId": cVideoCommonHistoryCallReferenceId,
       "cVideoCommonHistoryCallType": cVideoCommonHistoryCallType,
       "cVideoCommonHistoryTxCodec": cVideoCommonHistoryTxCodec,
       "cVideoCommonHistoryTxPictureWidth": cVideoCommonHistoryTxPictureWidth,
       "cVideoCommonHistoryTxPictureHeight": cVideoCommonHistoryTxPictureHeight,
       "cVideoCommonHistoryTxConfigFrameRate": cVideoCommonHistoryTxConfigFrameRate,
       "cVideoCommonHistoryTxConfigBitrate": cVideoCommonHistoryTxConfigBitrate,
       "cVideoCommonHistoryTxPayloadFormat": cVideoCommonHistoryTxPayloadFormat,
       "cVideoCommonHistoryTxAnnex": cVideoCommonHistoryTxAnnex,
       "cVideoCommonHistoryTxProfile": cVideoCommonHistoryTxProfile,
       "cVideoCommonHistoryTxLevel": cVideoCommonHistoryTxLevel,
       "cVideoCommonHistoryTxPackets": cVideoCommonHistoryTxPackets,
       "cVideoCommonHistoryTxBytes": cVideoCommonHistoryTxBytes,
       "cVideoCommonHistoryTxDuration": cVideoCommonHistoryTxDuration,
       "cVideoCommonHistoryRxCodec": cVideoCommonHistoryRxCodec,
       "cVideoCommonHistoryRxPictureWidth": cVideoCommonHistoryRxPictureWidth,
       "cVideoCommonHistoryRxPictureHeight": cVideoCommonHistoryRxPictureHeight,
       "cVideoCommonHistoryRxConfigFrameRate": cVideoCommonHistoryRxConfigFrameRate,
       "cVideoCommonHistoryRxConfigBitrate": cVideoCommonHistoryRxConfigBitrate,
       "cVideoCommonHistoryRxPayloadFormat": cVideoCommonHistoryRxPayloadFormat,
       "cVideoCommonHistoryRxAnnex": cVideoCommonHistoryRxAnnex,
       "cVideoCommonHistoryRxProfile": cVideoCommonHistoryRxProfile,
       "cVideoCommonHistoryRxLevel": cVideoCommonHistoryRxLevel,
       "cVideoCommonHistoryRxPackets": cVideoCommonHistoryRxPackets,
       "cVideoCommonHistoryRxBytes": cVideoCommonHistoryRxBytes,
       "cVideoCommonHistoryRxDuration": cVideoCommonHistoryRxDuration,
       "cVideoCommonHistorySessionId": cVideoCommonHistorySessionId,
       "cVideoConfereeHistoryTable": cVideoConfereeHistoryTable,
       "cVideoConfereeHistoryEntry": cVideoConfereeHistoryEntry,
       "cVideoConfereeHistoryTotalDroppedPackets": cVideoConfereeHistoryTotalDroppedPackets,
       "cVideoConfereeHistoryMaxJitter": cVideoConfereeHistoryMaxJitter,
       "cVideoConfereeHistoryMaxDelay": cVideoConfereeHistoryMaxDelay,
       "cVideoConfereeHistoryTotalOutOfOrderPackets": cVideoConfereeHistoryTotalOutOfOrderPackets,
       "cVideoConfereeHistoryMaxOutOfSyncDelay": cVideoConfereeHistoryMaxOutOfSyncDelay,
       "cVideoConfereeHistoryTotalLostPackets": cVideoConfereeHistoryTotalLostPackets,
       "cVideoCallHistoryTable": cVideoCallHistoryTable,
       "cVideoCallHistoryEntry": cVideoCallHistoryEntry,
       "cVideoCallHistoryTxMacroblocksConcealed": cVideoCallHistoryTxMacroblocksConcealed,
       "cVideoCallHistoryTxFramesConcealed": cVideoCallHistoryTxFramesConcealed,
       "cVideoCallHistoryTxBadHeaderPackets": cVideoCallHistoryTxBadHeaderPackets,
       "cVideoCallHistoryTxOverflowPackets": cVideoCallHistoryTxOverflowPackets,
       "cVideoCallHistoryTxOutOfOrderPackets": cVideoCallHistoryTxOutOfOrderPackets,
       "cVideoCallHistoryTxLostPackets": cVideoCallHistoryTxLostPackets,
       "cVideoCommonStatsHistoryTable": cVideoCommonStatsHistoryTable,
       "cVideoCommonStatsHistoryEntry": cVideoCommonStatsHistoryEntry,
       "cVideoCommonStatsHistoryTxTotalLostPackets": cVideoCommonStatsHistoryTxTotalLostPackets,
       "cVideoCommonStatsHistoryTxPercentLostPackets": cVideoCommonStatsHistoryTxPercentLostPackets,
       "cVideoCommonStatsHistoryTxTotalOutOfOrderPackets": cVideoCommonStatsHistoryTxTotalOutOfOrderPackets,
       "cVideoCommonStatsHistoryTxMaxJitter": cVideoCommonStatsHistoryTxMaxJitter,
       "cVideoCommonStatsHistoryTxAvgJitter": cVideoCommonStatsHistoryTxAvgJitter,
       "cVideoCommonStatsHistoryTxMaxDelay": cVideoCommonStatsHistoryTxMaxDelay,
       "cVideoCommonStatsHistoryTxAvgDelay": cVideoCommonStatsHistoryTxAvgDelay,
       "cVideoCommonStatsHistoryRxTotalLostPackets": cVideoCommonStatsHistoryRxTotalLostPackets,
       "cVideoCommonStatsHistoryRxPercentLostPackets": cVideoCommonStatsHistoryRxPercentLostPackets,
       "cVideoSessionActive": cVideoSessionActive,
       "cVideoCommonActiveTable": cVideoCommonActiveTable,
       "cVideoCommonActiveEntry": cVideoCommonActiveEntry,
       "cVideoCommonActiveConnectionId": cVideoCommonActiveConnectionId,
       "cVideoCommonActiveCallReferenceId": cVideoCommonActiveCallReferenceId,
       "cVideoCommonActiveCallType": cVideoCommonActiveCallType,
       "cVideoCommonActiveTxCodec": cVideoCommonActiveTxCodec,
       "cVideoCommonActiveTxPictureWidth": cVideoCommonActiveTxPictureWidth,
       "cVideoCommonActiveTxPictureHeight": cVideoCommonActiveTxPictureHeight,
       "cVideoCommonActiveTxConfigFrameRate": cVideoCommonActiveTxConfigFrameRate,
       "cVideoCommonActiveTxConfigBitrate": cVideoCommonActiveTxConfigBitrate,
       "cVideoCommonActiveTxPayloadFormat": cVideoCommonActiveTxPayloadFormat,
       "cVideoCommonActiveTxAnnex": cVideoCommonActiveTxAnnex,
       "cVideoCommonActiveTxProfile": cVideoCommonActiveTxProfile,
       "cVideoCommonActiveTxLevel": cVideoCommonActiveTxLevel,
       "cVideoCommonActiveTxPackets": cVideoCommonActiveTxPackets,
       "cVideoCommonActiveTxBytes": cVideoCommonActiveTxBytes,
       "cVideoCommonActiveTxDuration": cVideoCommonActiveTxDuration,
       "cVideoCommonActiveRxCodec": cVideoCommonActiveRxCodec,
       "cVideoCommonActiveRxPictureWidth": cVideoCommonActiveRxPictureWidth,
       "cVideoCommonActiveRxPictureHeight": cVideoCommonActiveRxPictureHeight,
       "cVideoCommonActiveRxConfigFrameRate": cVideoCommonActiveRxConfigFrameRate,
       "cVideoCommonActiveRxConfigBitrate": cVideoCommonActiveRxConfigBitrate,
       "cVideoCommonActiveRxPayloadFormat": cVideoCommonActiveRxPayloadFormat,
       "cVideoCommonActiveRxAnnex": cVideoCommonActiveRxAnnex,
       "cVideoCommonActiveRxProfile": cVideoCommonActiveRxProfile,
       "cVideoCommonActiveRxLevel": cVideoCommonActiveRxLevel,
       "cVideoCommonActiveRxPackets": cVideoCommonActiveRxPackets,
       "cVideoCommonActiveRxBytes": cVideoCommonActiveRxBytes,
       "cVideoCommonActiveRxDuration": cVideoCommonActiveRxDuration,
       "cVideoCommonActiveSessionId": cVideoCommonActiveSessionId,
       "cVideoConfereeActiveTable": cVideoConfereeActiveTable,
       "cVideoConfereeActiveEntry": cVideoConfereeActiveEntry,
       "cVideoConfereeActiveActualFrameRate": cVideoConfereeActiveActualFrameRate,
       "cVideoConfereeActiveActualBitrate": cVideoConfereeActiveActualBitrate,
       "cVideoConfereeActiveTotalDroppedPackets": cVideoConfereeActiveTotalDroppedPackets,
       "cVideoConfereeActiveCurrentDroppedPackets": cVideoConfereeActiveCurrentDroppedPackets,
       "cVideoConfereeActiveTotalOutOfOrderPackets": cVideoConfereeActiveTotalOutOfOrderPackets,
       "cVideoConfereeActiveCurrentOutOfOrderPackets": cVideoConfereeActiveCurrentOutOfOrderPackets,
       "cVideoConfereeActiveTotalLostPackets": cVideoConfereeActiveTotalLostPackets,
       "cVideoConfereeActiveCurrentLostPackets": cVideoConfereeActiveCurrentLostPackets,
       "cVideoConfereeActiveMaxJitter": cVideoConfereeActiveMaxJitter,
       "cVideoConfereeActiveCurrentJitter": cVideoConfereeActiveCurrentJitter,
       "cVideoConfereeActiveMaxDelay": cVideoConfereeActiveMaxDelay,
       "cVideoConfereeActiveCurrentDelay": cVideoConfereeActiveCurrentDelay,
       "cVideoConfereeActiveMaxOutOfSyncDelay": cVideoConfereeActiveMaxOutOfSyncDelay,
       "cVideoConfereeActiveCurrentOutOfSyncDelay": cVideoConfereeActiveCurrentOutOfSyncDelay,
       "cVideoConfereeActiveFastVideoUpdateRate": cVideoConfereeActiveFastVideoUpdateRate,
       "cVideoCallActiveTable": cVideoCallActiveTable,
       "cVideoCallActiveEntry": cVideoCallActiveEntry,
       "cVideoCallActiveRxActualBitrate": cVideoCallActiveRxActualBitrate,
       "cVideoCallActiveTxMacroblocksConcealed": cVideoCallActiveTxMacroblocksConcealed,
       "cVideoCallActiveTxFramesConcealed": cVideoCallActiveTxFramesConcealed,
       "cVideoCallActiveTxBadHeaderPackets": cVideoCallActiveTxBadHeaderPackets,
       "cVideoCallActiveTxOverflowPackets": cVideoCallActiveTxOverflowPackets,
       "cVideoCallActiveTxLostPackets": cVideoCallActiveTxLostPackets,
       "cVideoCommonStatsActiveTable": cVideoCommonStatsActiveTable,
       "cVideoCommonStatsActiveEntry": cVideoCommonStatsActiveEntry,
       "cVideoCommonStatsActiveTxActualBitrate": cVideoCommonStatsActiveTxActualBitrate,
       "cVideoCommonStatsActiveTxTotalLostPackets": cVideoCommonStatsActiveTxTotalLostPackets,
       "cVideoCommonStatsActiveTxPercentLostPackets": cVideoCommonStatsActiveTxPercentLostPackets,
       "cVideoCommonStatsActiveTxCurrentLostPackets": cVideoCommonStatsActiveTxCurrentLostPackets,
       "cVideoCommonStatsActiveTxTotalOutOfOrderPackets": cVideoCommonStatsActiveTxTotalOutOfOrderPackets,
       "cVideoCommonStatsActiveTxCurrentOutOfOrderPackets": cVideoCommonStatsActiveTxCurrentOutOfOrderPackets,
       "cVideoCommonStatsActiveTxMaxJitter": cVideoCommonStatsActiveTxMaxJitter,
       "cVideoCommonStatsActiveTxAvgJitter": cVideoCommonStatsActiveTxAvgJitter,
       "cVideoCommonStatsActiveTxCurrentJitter": cVideoCommonStatsActiveTxCurrentJitter,
       "cVideoCommonStatsActiveTxMaxDelay": cVideoCommonStatsActiveTxMaxDelay,
       "cVideoCommonStatsActiveTxAvgDelay": cVideoCommonStatsActiveTxAvgDelay,
       "cVideoCommonStatsActiveTxCurrentDelay": cVideoCommonStatsActiveTxCurrentDelay,
       "cVideoCommonStatsActiveRxActualBitrate": cVideoCommonStatsActiveRxActualBitrate,
       "cVideoCommonStatsActiveRxTotalLostPackets": cVideoCommonStatsActiveRxTotalLostPackets,
       "cVideoCommonStatsActiveRxPercentLostPackets": cVideoCommonStatsActiveRxPercentLostPackets,
       "cVideoCommonStatsActiveRxCurrentLostPackets": cVideoCommonStatsActiveRxCurrentLostPackets,
       "ciscoVideoSessionMIBConform": ciscoVideoSessionMIBConform,
       "ciscoVideoSessionMIBCompliances": ciscoVideoSessionMIBCompliances,
       "cVideoSessionMIBCompliance": cVideoSessionMIBCompliance,
       "cVideoSessionMIBComplianceRev1": cVideoSessionMIBComplianceRev1,
       "ciscoVideoSessionMIBGroups": ciscoVideoSessionMIBGroups,
       "cVideoSessionHistoryGroup": cVideoSessionHistoryGroup,
       "cVideoSessionActiveGroup": cVideoSessionActiveGroup,
       "cVideoSessionCommonStatusGroup": cVideoSessionCommonStatusGroup,
       "cVideoSessionCommonStatisticsGroup": cVideoSessionCommonStatisticsGroup,
       "cVideoSessionCallStatisticsGroup": cVideoSessionCallStatisticsGroup,
       "cVideoSessionConfereeStatisticsGroup": cVideoSessionConfereeStatisticsGroup}
)
