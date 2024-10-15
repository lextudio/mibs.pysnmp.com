# SNMP MIB module (XLDV20PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XLDV20PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:18:44 2024
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

(onu,) = mibBuilder.importSymbols(
    "AN-MIB",
    "onu")

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
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(Unsigned16,
 Xldv20AdminState,
 Xldv20ControlStatus,
 Xldv20FlowDirection,
 xldv20IfIndex,
 xldv20Traps,
 xldv20TvTimeAndDate) = mibBuilder.importSymbols(
    "XLDV20-MIB",
    "Unsigned16",
    "Xldv20AdminState",
    "Xldv20ControlStatus",
    "Xldv20FlowDirection",
    "xldv20IfIndex",
    "xldv20Traps",
    "xldv20TvTimeAndDate")


# MODULE-IDENTITY


# Types definitions



class Xldv20pmIntervalType(Integer32):
    """Custom type Xldv20pmIntervalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("day", 2),
          ("min15", 1))
    )





class Xldv20pmControlReq(Integer32):
    """Custom type Xldv20pmControlReq based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("addEndpoint", 9),
          ("aswTimeout", 17),
          ("atmPmObjectActive", 12),
          ("atmPmObjectNotExists", 13),
          ("commandFailed", 18),
          ("commandSucceeded", 19),
          ("create", 7),
          ("dataDaseMemoryNotAvailable", 6),
          ("delete", 8),
          ("endpointExistsAlready", 14),
          ("indexLimitExceeded", 11),
          ("noRequest", 1),
          ("nrHistEntriesSizeNotAcceptable", 5),
          ("paramFaulty", 4),
          ("removeEndpoint", 10),
          ("requestBusy", 15),
          ("resetIndividCurrent", 2),
          ("setDataFailed", 16),
          ("setNrHistEntriesSize", 3))
    )





class Xldv20pmCounterName(Integer32):
    """Custom type Xldv20pmCounterName based on Integer32"""
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
              47)
        )
    )
    namedValues = NamedValues(
        *(("discardedCells", 32),
          ("feBackgroundBlockErrors", 19),
          ("feCodeViolations", 20),
          ("feCodeViolationsCP", 21),
          ("feCodeViolationsPLCP", 22),
          ("feErroredSeconds", 23),
          ("feErroredSecondsCP", 24),
          ("feErroredSecondsPLCP", 25),
          ("feSas", 26),
          ("feSeverelyErroredSeconds", 27),
          ("feSeverelyErroredSecondsCP", 28),
          ("feSeverelyErroredSecondsPLCP", 29),
          ("feUnavailableSeconds", 30),
          ("feUnavailableSecondsPLCP", 31),
          ("imaGroupNeNumFailures", 34),
          ("imaGroupUnavailSecs", 33),
          ("imaLinkFeRxUnusableSecs", 44),
          ("imaLinkFeSevErroredSecs", 38),
          ("imaLinkFeTxUnusableSecs", 43),
          ("imaLinkFeUnavailSecs", 40),
          ("imaLinkImaViolations", 35),
          ("imaLinkNeRxNumFailures", 46),
          ("imaLinkNeRxUnusableSecs", 42),
          ("imaLinkNeSevErroredSecs", 37),
          ("imaLinkNeTxNumFailures", 45),
          ("imaLinkNeTxUnusableSecs", 41),
          ("imaLinkNeUnavailSecs", 39),
          ("imaLinkOifAnomalies", 36),
          ("maxPmCounter", 47),
          ("neAisSeconds", 16),
          ("neBackgroundBlockErrors", 1),
          ("neCodeViolations", 2),
          ("neCodeViolationsCP", 3),
          ("neCodeViolationsP", 4),
          ("neCodeViolationsPLCP", 5),
          ("neErroredSeconds", 6),
          ("neErroredSecondsCP", 7),
          ("neErroredSecondsPLCP", 8),
          ("neLosSeconds", 18),
          ("neOfsSeconds", 17),
          ("neSas", 9),
          ("neSeverelyErroredFrameSeconds", 10),
          ("neSeverelyErroredSeconds", 11),
          ("neSeverelyErroredSecondsCP", 12),
          ("neSeverelyErroredSecondsPLCP", 13),
          ("neUnavailableSeconds", 14),
          ("neUnavailableSecondsPLCP", 15),
          ("noPmCounter", 0))
    )





class Xldv20pmType(Integer32):
    """Custom type Xldv20pmType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("adcF3PMo", 10),
          ("adcPrM", 15),
          ("atmImaPMo", 20),
          ("d1ImaPMo", 19),
          ("d1ImaPrM", 17),
          ("d3F2PMo", 7),
          ("d3F3PMo", 8),
          ("d3PrM", 14),
          ("e1ImaPMo", 18),
          ("e1ImaPrM", 16),
          ("e3F3PMo", 9),
          ("e3PrM", 13),
          ("maxPmType", 21),
          ("pmTypeUnknown", 0),
          ("s1F1PMo", 1),
          ("s1F2PMo", 2),
          ("s1F3PMo", 3),
          ("s1PrM", 11),
          ("s3F1PMo", 4),
          ("s3F2PMo", 5),
          ("s3F3PMo", 6),
          ("s3PrM", 12))
    )





class Xldv20pmFlowType(Integer32):
    """Custom type Xldv20pmFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("f4EndToEnd", 2),
          ("f4Segment", 1),
          ("f5EndToEnd", 4),
          ("f5Segment", 3),
          ("undefined", 0))
    )





class Xldv20pmSuspectType(Integer32):
    """Custom type Xldv20pmSuspectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reliable", 1),
          ("suspect", 2),
          ("undefined", 0))
    )





class Xldv20pmConnectionIndexType(Integer32):
    """Custom type Xldv20pmConnectionIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("vclNni", 4),
          ("vclUni", 3),
          ("vplNni", 2),
          ("vplUni", 1))
    )





class Xldv20pmRoleType(Integer32):
    """Custom type Xldv20pmRoleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("analyseWithBackwardReporting", 1),
          ("analyseWithoutBackwardReporting", 2),
          ("generateWithCollect", 3),
          ("generateWithoutCollect", 4),
          ("undefined", 0))
    )





class Xldv20pmEndpointType(Integer32):
    """Custom type Xldv20pmEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sink", 2),
          ("source", 1))
    )





class Xldv20pmBlockSizeType(Integer32):
    """Custom type Xldv20pmBlockSizeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("blockSize1024", 1024),
          ("blockSize128", 128),
          ("blockSize256", 256),
          ("blockSize512", 512),
          ("undefined", 0))
    )





class Xldv20pmAtmCounterType(Integer32):
    """Custom type Xldv20pmAtmCounterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lostUserCells", 2),
          ("misinsertedUserCells", 3),
          ("transmittedUserCells", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xldv20Pm_ObjectIdentity = ObjectIdentity
xldv20Pm = _Xldv20Pm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5)
)
_Xldv20pmPerformanceManagementControl_ObjectIdentity = ObjectIdentity
xldv20pmPerformanceManagementControl = _Xldv20pmPerformanceManagementControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1)
)
_Xldv20pmControl_ObjectIdentity = ObjectIdentity
xldv20pmControl = _Xldv20pmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1)
)
_Xldv20pmCoIfIndex_Type = Unsigned16
_Xldv20pmCoIfIndex_Object = MibScalar
xldv20pmCoIfIndex = _Xldv20pmCoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 1),
    _Xldv20pmCoIfIndex_Type()
)
xldv20pmCoIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCoIfIndex.setStatus("mandatory")


class _Xldv20pmCoNrHistEntriesSize_Type(Integer32):
    """Custom type xldv20pmCoNrHistEntriesSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmCoNrHistEntriesSize_Type.__name__ = "Integer32"
_Xldv20pmCoNrHistEntriesSize_Object = MibScalar
xldv20pmCoNrHistEntriesSize = _Xldv20pmCoNrHistEntriesSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 2),
    _Xldv20pmCoNrHistEntriesSize_Type()
)
xldv20pmCoNrHistEntriesSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCoNrHistEntriesSize.setStatus("mandatory")
_Xldv20pmCoIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmCoIntervalType_Object = MibScalar
xldv20pmCoIntervalType = _Xldv20pmCoIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 3),
    _Xldv20pmCoIntervalType_Type()
)
xldv20pmCoIntervalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCoIntervalType.setStatus("mandatory")
_Xldv20pmCoControlReq_Type = Xldv20pmControlReq
_Xldv20pmCoControlReq_Object = MibScalar
xldv20pmCoControlReq = _Xldv20pmCoControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 4),
    _Xldv20pmCoControlReq_Type()
)
xldv20pmCoControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCoControlReq.setStatus("mandatory")
_Xldv20pmCoControlStatus_Type = Xldv20ControlStatus
_Xldv20pmCoControlStatus_Object = MibScalar
xldv20pmCoControlStatus = _Xldv20pmCoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 5),
    _Xldv20pmCoControlStatus_Type()
)
xldv20pmCoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCoControlStatus.setStatus("mandatory")


class _Xldv20pmCoRemainingHistoryEntriesSize_Type(Integer32):
    """Custom type xldv20pmCoRemainingHistoryEntriesSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20pmCoRemainingHistoryEntriesSize_Type.__name__ = "Integer32"
_Xldv20pmCoRemainingHistoryEntriesSize_Object = MibScalar
xldv20pmCoRemainingHistoryEntriesSize = _Xldv20pmCoRemainingHistoryEntriesSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 6),
    _Xldv20pmCoRemainingHistoryEntriesSize_Type()
)
xldv20pmCoRemainingHistoryEntriesSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCoRemainingHistoryEntriesSize.setStatus("mandatory")


class _Xldv20pmCoOAMLevel_Type(Integer32):
    """Custom type xldv20pmCoOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmCoOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmCoOAMLevel_Object = MibScalar
xldv20pmCoOAMLevel = _Xldv20pmCoOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 7),
    _Xldv20pmCoOAMLevel_Type()
)
xldv20pmCoOAMLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCoOAMLevel.setStatus("mandatory")
_Xldv20pmCoControlReqResult_Type = Xldv20pmControlReq
_Xldv20pmCoControlReqResult_Object = MibScalar
xldv20pmCoControlReqResult = _Xldv20pmCoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 8),
    _Xldv20pmCoControlReqResult_Type()
)
xldv20pmCoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCoControlReqResult.setStatus("mandatory")
_Xldv20pmCoControlTimeStamp_Type = TimeTicks
_Xldv20pmCoControlTimeStamp_Object = MibScalar
xldv20pmCoControlTimeStamp = _Xldv20pmCoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 1, 9),
    _Xldv20pmCoControlTimeStamp_Type()
)
xldv20pmCoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCoControlTimeStamp.setStatus("mandatory")
_Xldv20pmAtmControl_ObjectIdentity = ObjectIdentity
xldv20pmAtmControl = _Xldv20pmAtmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2)
)
_Xldv20pmAcoIndex_Type = Unsigned16
_Xldv20pmAcoIndex_Object = MibScalar
xldv20pmAcoIndex = _Xldv20pmAcoIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 1),
    _Xldv20pmAcoIndex_Type()
)
xldv20pmAcoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoIndex.setStatus("mandatory")


class _Xldv20pmAcoNrHistEntriesSize_Type(Integer32):
    """Custom type xldv20pmAcoNrHistEntriesSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmAcoNrHistEntriesSize_Type.__name__ = "Integer32"
_Xldv20pmAcoNrHistEntriesSize_Object = MibScalar
xldv20pmAcoNrHistEntriesSize = _Xldv20pmAcoNrHistEntriesSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 2),
    _Xldv20pmAcoNrHistEntriesSize_Type()
)
xldv20pmAcoNrHistEntriesSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoNrHistEntriesSize.setStatus("mandatory")
_Xldv20pmAcoIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmAcoIntervalType_Object = MibScalar
xldv20pmAcoIntervalType = _Xldv20pmAcoIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 3),
    _Xldv20pmAcoIntervalType_Type()
)
xldv20pmAcoIntervalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoIntervalType.setStatus("mandatory")
_Xldv20pmAcoControlReq_Type = Xldv20pmControlReq
_Xldv20pmAcoControlReq_Object = MibScalar
xldv20pmAcoControlReq = _Xldv20pmAcoControlReq_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 4),
    _Xldv20pmAcoControlReq_Type()
)
xldv20pmAcoControlReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoControlReq.setStatus("mandatory")
_Xldv20pmAcoControlStatus_Type = Xldv20ControlStatus
_Xldv20pmAcoControlStatus_Object = MibScalar
xldv20pmAcoControlStatus = _Xldv20pmAcoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 5),
    _Xldv20pmAcoControlStatus_Type()
)
xldv20pmAcoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcoControlStatus.setStatus("mandatory")


class _Xldv20pmAcoRemainingHistoryEntriesSize_Type(Integer32):
    """Custom type xldv20pmAcoRemainingHistoryEntriesSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Xldv20pmAcoRemainingHistoryEntriesSize_Type.__name__ = "Integer32"
_Xldv20pmAcoRemainingHistoryEntriesSize_Object = MibScalar
xldv20pmAcoRemainingHistoryEntriesSize = _Xldv20pmAcoRemainingHistoryEntriesSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 6),
    _Xldv20pmAcoRemainingHistoryEntriesSize_Type()
)
xldv20pmAcoRemainingHistoryEntriesSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcoRemainingHistoryEntriesSize.setStatus("mandatory")
_Xldv20pmAcoFlowType_Type = Xldv20pmFlowType
_Xldv20pmAcoFlowType_Object = MibScalar
xldv20pmAcoFlowType = _Xldv20pmAcoFlowType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 7),
    _Xldv20pmAcoFlowType_Type()
)
xldv20pmAcoFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoFlowType.setStatus("mandatory")
_Xldv20pmAcoFlowDirection_Type = Xldv20FlowDirection
_Xldv20pmAcoFlowDirection_Object = MibScalar
xldv20pmAcoFlowDirection = _Xldv20pmAcoFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 8),
    _Xldv20pmAcoFlowDirection_Type()
)
xldv20pmAcoFlowDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoFlowDirection.setStatus("mandatory")


class _Xldv20pmAcoConnectionIndex_Type(Integer32):
    """Custom type xldv20pmAcoConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Xldv20pmAcoConnectionIndex_Type.__name__ = "Integer32"
_Xldv20pmAcoConnectionIndex_Object = MibScalar
xldv20pmAcoConnectionIndex = _Xldv20pmAcoConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 9),
    _Xldv20pmAcoConnectionIndex_Type()
)
xldv20pmAcoConnectionIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoConnectionIndex.setStatus("mandatory")
_Xldv20pmAcoConnectionIndexType_Type = Xldv20pmConnectionIndexType
_Xldv20pmAcoConnectionIndexType_Object = MibScalar
xldv20pmAcoConnectionIndexType = _Xldv20pmAcoConnectionIndexType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 10),
    _Xldv20pmAcoConnectionIndexType_Type()
)
xldv20pmAcoConnectionIndexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoConnectionIndexType.setStatus("mandatory")
_Xldv20pmAcoRole_Type = Xldv20pmRoleType
_Xldv20pmAcoRole_Object = MibScalar
xldv20pmAcoRole = _Xldv20pmAcoRole_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 12),
    _Xldv20pmAcoRole_Type()
)
xldv20pmAcoRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoRole.setStatus("mandatory")
_Xldv20pmAcoEndpointType_Type = Xldv20pmEndpointType
_Xldv20pmAcoEndpointType_Object = MibScalar
xldv20pmAcoEndpointType = _Xldv20pmAcoEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 13),
    _Xldv20pmAcoEndpointType_Type()
)
xldv20pmAcoEndpointType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcoEndpointType.setStatus("mandatory")
_Xldv20pmAcoControlReqResult_Type = Xldv20pmControlReq
_Xldv20pmAcoControlReqResult_Object = MibScalar
xldv20pmAcoControlReqResult = _Xldv20pmAcoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 14),
    _Xldv20pmAcoControlReqResult_Type()
)
xldv20pmAcoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcoControlReqResult.setStatus("mandatory")
_Xldv20pmAcoControlTimeStamp_Type = TimeTicks
_Xldv20pmAcoControlTimeStamp_Object = MibScalar
xldv20pmAcoControlTimeStamp = _Xldv20pmAcoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 1, 2, 15),
    _Xldv20pmAcoControlTimeStamp_Type()
)
xldv20pmAcoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcoControlTimeStamp.setStatus("mandatory")
_Xldv20pmPerformanceMonitoring_ObjectIdentity = ObjectIdentity
xldv20pmPerformanceMonitoring = _Xldv20pmPerformanceMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2)
)
_Xldv20pmCommonCurrentTable_Object = MibTable
xldv20pmCommonCurrentTable = _Xldv20pmCommonCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    xldv20pmCommonCurrentTable.setStatus("mandatory")
_Xldv20pmCommonCurrentEntry_Object = MibTableRow
xldv20pmCommonCurrentEntry = _Xldv20pmCommonCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1)
)
xldv20pmCommonCurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmCcIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmCcOAMLevel"),
)
if mibBuilder.loadTexts:
    xldv20pmCommonCurrentEntry.setStatus("mandatory")
_Xldv20pmCcIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmCcIntervalType_Object = MibTableColumn
xldv20pmCcIntervalType = _Xldv20pmCcIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 1),
    _Xldv20pmCcIntervalType_Type()
)
xldv20pmCcIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcIntervalType.setStatus("mandatory")


class _Xldv20pmCcOAMLevel_Type(Integer32):
    """Custom type xldv20pmCcOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmCcOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmCcOAMLevel_Object = MibTableColumn
xldv20pmCcOAMLevel = _Xldv20pmCcOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 2),
    _Xldv20pmCcOAMLevel_Type()
)
xldv20pmCcOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcOAMLevel.setStatus("mandatory")
_Xldv20pmCcAdminState_Type = Xldv20AdminState
_Xldv20pmCcAdminState_Object = MibTableColumn
xldv20pmCcAdminState = _Xldv20pmCcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 3),
    _Xldv20pmCcAdminState_Type()
)
xldv20pmCcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCcAdminState.setStatus("mandatory")
_Xldv20pmCcSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmCcSuspectFlag_Object = MibTableColumn
xldv20pmCcSuspectFlag = _Xldv20pmCcSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 4),
    _Xldv20pmCcSuspectFlag_Type()
)
xldv20pmCcSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcSuspectFlag.setStatus("mandatory")


class _Xldv20pmCcHistEntrySize_Type(Integer32):
    """Custom type xldv20pmCcHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmCcHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmCcHistEntrySize_Object = MibTableColumn
xldv20pmCcHistEntrySize = _Xldv20pmCcHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 5),
    _Xldv20pmCcHistEntrySize_Type()
)
xldv20pmCcHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcHistEntrySize.setStatus("mandatory")


class _Xldv20pmCcNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmCcNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmCcNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmCcNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmCcNrHistEntriesAvailable = _Xldv20pmCcNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 6),
    _Xldv20pmCcNrHistEntriesAvailable_Type()
)
xldv20pmCcNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmCcElapsedTime_Type(Integer32):
    """Custom type xldv20pmCcElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmCcElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmCcElapsedTime_Object = MibTableColumn
xldv20pmCcElapsedTime = _Xldv20pmCcElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 7),
    _Xldv20pmCcElapsedTime_Type()
)
xldv20pmCcElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcElapsedTime.setStatus("mandatory")


class _Xldv20pmCcThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmCcThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmCcThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmCcThresholdLimitIndex_Object = MibTableColumn
xldv20pmCcThresholdLimitIndex = _Xldv20pmCcThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 8),
    _Xldv20pmCcThresholdLimitIndex_Type()
)
xldv20pmCcThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmCcThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmCcNeErroredSeconds_Type = Counter32
_Xldv20pmCcNeErroredSeconds_Object = MibTableColumn
xldv20pmCcNeErroredSeconds = _Xldv20pmCcNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 9),
    _Xldv20pmCcNeErroredSeconds_Type()
)
xldv20pmCcNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcNeErroredSeconds.setStatus("mandatory")
_Xldv20pmCcFeErroredSeconds_Type = Counter32
_Xldv20pmCcFeErroredSeconds_Object = MibTableColumn
xldv20pmCcFeErroredSeconds = _Xldv20pmCcFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 10),
    _Xldv20pmCcFeErroredSeconds_Type()
)
xldv20pmCcFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcFeErroredSeconds.setStatus("mandatory")
_Xldv20pmCcNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmCcNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmCcNeSeverelyErroredSeconds = _Xldv20pmCcNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 11),
    _Xldv20pmCcNeSeverelyErroredSeconds_Type()
)
xldv20pmCcNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmCcFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmCcFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmCcFeSeverelyErroredSeconds = _Xldv20pmCcFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 12),
    _Xldv20pmCcFeSeverelyErroredSeconds_Type()
)
xldv20pmCcFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmCcNeBackgroundBlockErrors_Type = Counter32
_Xldv20pmCcNeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmCcNeBackgroundBlockErrors = _Xldv20pmCcNeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 13),
    _Xldv20pmCcNeBackgroundBlockErrors_Type()
)
xldv20pmCcNeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcNeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmCcFeBackgroundBlockErrors_Type = Counter32
_Xldv20pmCcFeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmCcFeBackgroundBlockErrors = _Xldv20pmCcFeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 14),
    _Xldv20pmCcFeBackgroundBlockErrors_Type()
)
xldv20pmCcFeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcFeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmCcNeUnavailableSeconds_Type = Counter32
_Xldv20pmCcNeUnavailableSeconds_Object = MibTableColumn
xldv20pmCcNeUnavailableSeconds = _Xldv20pmCcNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 15),
    _Xldv20pmCcNeUnavailableSeconds_Type()
)
xldv20pmCcNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmCcFeUnavailableSeconds_Type = Counter32
_Xldv20pmCcFeUnavailableSeconds_Object = MibTableColumn
xldv20pmCcFeUnavailableSeconds = _Xldv20pmCcFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 2, 1, 16),
    _Xldv20pmCcFeUnavailableSeconds_Type()
)
xldv20pmCcFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmCcFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmCommonHistoryTable_Object = MibTable
xldv20pmCommonHistoryTable = _Xldv20pmCommonHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    xldv20pmCommonHistoryTable.setStatus("mandatory")
_Xldv20pmCommonHistoryEntry_Object = MibTableRow
xldv20pmCommonHistoryEntry = _Xldv20pmCommonHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1)
)
xldv20pmCommonHistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmChIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmChOAMLevel"),
    (0, "XLDV20PM-MIB", "xldv20pmChHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmCommonHistoryEntry.setStatus("mandatory")
_Xldv20pmChIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmChIntervalType_Object = MibTableColumn
xldv20pmChIntervalType = _Xldv20pmChIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 1),
    _Xldv20pmChIntervalType_Type()
)
xldv20pmChIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChIntervalType.setStatus("mandatory")


class _Xldv20pmChOAMLevel_Type(Integer32):
    """Custom type xldv20pmChOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmChOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmChOAMLevel_Object = MibTableColumn
xldv20pmChOAMLevel = _Xldv20pmChOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 2),
    _Xldv20pmChOAMLevel_Type()
)
xldv20pmChOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChOAMLevel.setStatus("mandatory")


class _Xldv20pmChHistEntryNr_Type(Integer32):
    """Custom type xldv20pmChHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmChHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmChHistEntryNr_Object = MibTableColumn
xldv20pmChHistEntryNr = _Xldv20pmChHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 3),
    _Xldv20pmChHistEntryNr_Type()
)
xldv20pmChHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChHistEntryNr.setStatus("mandatory")
_Xldv20pmChSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmChSuspectFlag_Object = MibTableColumn
xldv20pmChSuspectFlag = _Xldv20pmChSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 4),
    _Xldv20pmChSuspectFlag_Type()
)
xldv20pmChSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChSuspectFlag.setStatus("mandatory")


class _Xldv20pmChPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmChPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmChPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmChPeriodEndTime_Object = MibTableColumn
xldv20pmChPeriodEndTime = _Xldv20pmChPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 5),
    _Xldv20pmChPeriodEndTime_Type()
)
xldv20pmChPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChPeriodEndTime.setStatus("mandatory")
_Xldv20pmChNeErroredSeconds_Type = Counter32
_Xldv20pmChNeErroredSeconds_Object = MibTableColumn
xldv20pmChNeErroredSeconds = _Xldv20pmChNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 6),
    _Xldv20pmChNeErroredSeconds_Type()
)
xldv20pmChNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChNeErroredSeconds.setStatus("mandatory")
_Xldv20pmChFeErroredSeconds_Type = Counter32
_Xldv20pmChFeErroredSeconds_Object = MibTableColumn
xldv20pmChFeErroredSeconds = _Xldv20pmChFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 7),
    _Xldv20pmChFeErroredSeconds_Type()
)
xldv20pmChFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChFeErroredSeconds.setStatus("mandatory")
_Xldv20pmChNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmChNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmChNeSeverelyErroredSeconds = _Xldv20pmChNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 8),
    _Xldv20pmChNeSeverelyErroredSeconds_Type()
)
xldv20pmChNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmChFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmChFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmChFeSeverelyErroredSeconds = _Xldv20pmChFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 9),
    _Xldv20pmChFeSeverelyErroredSeconds_Type()
)
xldv20pmChFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmChNeBackgroundBlockErrors_Type = Counter32
_Xldv20pmChNeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmChNeBackgroundBlockErrors = _Xldv20pmChNeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 10),
    _Xldv20pmChNeBackgroundBlockErrors_Type()
)
xldv20pmChNeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChNeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmChFeBackgroundBlockErrors_Type = Counter32
_Xldv20pmChFeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmChFeBackgroundBlockErrors = _Xldv20pmChFeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 11),
    _Xldv20pmChFeBackgroundBlockErrors_Type()
)
xldv20pmChFeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChFeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmChNeUnavailableSeconds_Type = Counter32
_Xldv20pmChNeUnavailableSeconds_Object = MibTableColumn
xldv20pmChNeUnavailableSeconds = _Xldv20pmChNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 12),
    _Xldv20pmChNeUnavailableSeconds_Type()
)
xldv20pmChNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmChFeUnavailableSeconds_Type = Counter32
_Xldv20pmChFeUnavailableSeconds_Object = MibTableColumn
xldv20pmChFeUnavailableSeconds = _Xldv20pmChFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 3, 1, 13),
    _Xldv20pmChFeUnavailableSeconds_Type()
)
xldv20pmChFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmChFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS3CurrentTable_Object = MibTable
xldv20pmS3CurrentTable = _Xldv20pmS3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4)
)
if mibBuilder.loadTexts:
    xldv20pmS3CurrentTable.setStatus("mandatory")
_Xldv20pmS3CurrentEntry_Object = MibTableRow
xldv20pmS3CurrentEntry = _Xldv20pmS3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1)
)
xldv20pmS3CurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmS3cIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmS3cOAMLevel"),
)
if mibBuilder.loadTexts:
    xldv20pmS3CurrentEntry.setStatus("mandatory")
_Xldv20pmS3cIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmS3cIntervalType_Object = MibTableColumn
xldv20pmS3cIntervalType = _Xldv20pmS3cIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 1),
    _Xldv20pmS3cIntervalType_Type()
)
xldv20pmS3cIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cIntervalType.setStatus("mandatory")


class _Xldv20pmS3cOAMLevel_Type(Integer32):
    """Custom type xldv20pmS3cOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmS3cOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmS3cOAMLevel_Object = MibTableColumn
xldv20pmS3cOAMLevel = _Xldv20pmS3cOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 2),
    _Xldv20pmS3cOAMLevel_Type()
)
xldv20pmS3cOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cOAMLevel.setStatus("mandatory")
_Xldv20pmS3cAdminState_Type = Xldv20AdminState
_Xldv20pmS3cAdminState_Object = MibTableColumn
xldv20pmS3cAdminState = _Xldv20pmS3cAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 3),
    _Xldv20pmS3cAdminState_Type()
)
xldv20pmS3cAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmS3cAdminState.setStatus("mandatory")
_Xldv20pmS3cSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmS3cSuspectFlag_Object = MibTableColumn
xldv20pmS3cSuspectFlag = _Xldv20pmS3cSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 4),
    _Xldv20pmS3cSuspectFlag_Type()
)
xldv20pmS3cSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cSuspectFlag.setStatus("mandatory")


class _Xldv20pmS3cHistEntrySize_Type(Integer32):
    """Custom type xldv20pmS3cHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmS3cHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmS3cHistEntrySize_Object = MibTableColumn
xldv20pmS3cHistEntrySize = _Xldv20pmS3cHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 5),
    _Xldv20pmS3cHistEntrySize_Type()
)
xldv20pmS3cHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cHistEntrySize.setStatus("mandatory")


class _Xldv20pmS3cNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmS3cNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmS3cNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmS3cNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmS3cNrHistEntriesAvailable = _Xldv20pmS3cNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 6),
    _Xldv20pmS3cNrHistEntriesAvailable_Type()
)
xldv20pmS3cNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmS3cElapsedTime_Type(Integer32):
    """Custom type xldv20pmS3cElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmS3cElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmS3cElapsedTime_Object = MibTableColumn
xldv20pmS3cElapsedTime = _Xldv20pmS3cElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 7),
    _Xldv20pmS3cElapsedTime_Type()
)
xldv20pmS3cElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cElapsedTime.setStatus("mandatory")


class _Xldv20pmS3cThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmS3cThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmS3cThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmS3cThresholdLimitIndex_Object = MibTableColumn
xldv20pmS3cThresholdLimitIndex = _Xldv20pmS3cThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 8),
    _Xldv20pmS3cThresholdLimitIndex_Type()
)
xldv20pmS3cThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmS3cThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmS3cNeErroredSeconds_Type = Counter32
_Xldv20pmS3cNeErroredSeconds_Object = MibTableColumn
xldv20pmS3cNeErroredSeconds = _Xldv20pmS3cNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 9),
    _Xldv20pmS3cNeErroredSeconds_Type()
)
xldv20pmS3cNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNeErroredSeconds.setStatus("mandatory")
_Xldv20pmS3cFeErroredSeconds_Type = Counter32
_Xldv20pmS3cFeErroredSeconds_Object = MibTableColumn
xldv20pmS3cFeErroredSeconds = _Xldv20pmS3cFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 10),
    _Xldv20pmS3cFeErroredSeconds_Type()
)
xldv20pmS3cFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cFeErroredSeconds.setStatus("mandatory")
_Xldv20pmS3cNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS3cNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS3cNeSeverelyErroredSeconds = _Xldv20pmS3cNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 11),
    _Xldv20pmS3cNeSeverelyErroredSeconds_Type()
)
xldv20pmS3cNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS3cFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS3cFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS3cFeSeverelyErroredSeconds = _Xldv20pmS3cFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 12),
    _Xldv20pmS3cFeSeverelyErroredSeconds_Type()
)
xldv20pmS3cFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS3cNeCodeViolations_Type = Counter32
_Xldv20pmS3cNeCodeViolations_Object = MibTableColumn
xldv20pmS3cNeCodeViolations = _Xldv20pmS3cNeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 13),
    _Xldv20pmS3cNeCodeViolations_Type()
)
xldv20pmS3cNeCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNeCodeViolations.setStatus("mandatory")
_Xldv20pmS3cFeCodeViolations_Type = Counter32
_Xldv20pmS3cFeCodeViolations_Object = MibTableColumn
xldv20pmS3cFeCodeViolations = _Xldv20pmS3cFeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 14),
    _Xldv20pmS3cFeCodeViolations_Type()
)
xldv20pmS3cFeCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cFeCodeViolations.setStatus("mandatory")
_Xldv20pmS3cNeUnavailableSeconds_Type = Counter32
_Xldv20pmS3cNeUnavailableSeconds_Object = MibTableColumn
xldv20pmS3cNeUnavailableSeconds = _Xldv20pmS3cNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 15),
    _Xldv20pmS3cNeUnavailableSeconds_Type()
)
xldv20pmS3cNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS3cFeUnavailableSeconds_Type = Counter32
_Xldv20pmS3cFeUnavailableSeconds_Object = MibTableColumn
xldv20pmS3cFeUnavailableSeconds = _Xldv20pmS3cFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 16),
    _Xldv20pmS3cFeUnavailableSeconds_Type()
)
xldv20pmS3cFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS3cNeSeverelyErroredFrameSeconds_Type = Counter32
_Xldv20pmS3cNeSeverelyErroredFrameSeconds_Object = MibTableColumn
xldv20pmS3cNeSeverelyErroredFrameSeconds = _Xldv20pmS3cNeSeverelyErroredFrameSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 4, 1, 17),
    _Xldv20pmS3cNeSeverelyErroredFrameSeconds_Type()
)
xldv20pmS3cNeSeverelyErroredFrameSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3cNeSeverelyErroredFrameSeconds.setStatus("mandatory")
_Xldv20pmS3HistoryTable_Object = MibTable
xldv20pmS3HistoryTable = _Xldv20pmS3HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5)
)
if mibBuilder.loadTexts:
    xldv20pmS3HistoryTable.setStatus("mandatory")
_Xldv20pmS3HistoryEntry_Object = MibTableRow
xldv20pmS3HistoryEntry = _Xldv20pmS3HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1)
)
xldv20pmS3HistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmS3hIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmS3hOAMLevel"),
    (0, "XLDV20PM-MIB", "xldv20pmS3hHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmS3HistoryEntry.setStatus("mandatory")
_Xldv20pmS3hIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmS3hIntervalType_Object = MibTableColumn
xldv20pmS3hIntervalType = _Xldv20pmS3hIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 1),
    _Xldv20pmS3hIntervalType_Type()
)
xldv20pmS3hIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hIntervalType.setStatus("mandatory")


class _Xldv20pmS3hOAMLevel_Type(Integer32):
    """Custom type xldv20pmS3hOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmS3hOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmS3hOAMLevel_Object = MibTableColumn
xldv20pmS3hOAMLevel = _Xldv20pmS3hOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 2),
    _Xldv20pmS3hOAMLevel_Type()
)
xldv20pmS3hOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hOAMLevel.setStatus("mandatory")


class _Xldv20pmS3hHistEntryNr_Type(Integer32):
    """Custom type xldv20pmS3hHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmS3hHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmS3hHistEntryNr_Object = MibTableColumn
xldv20pmS3hHistEntryNr = _Xldv20pmS3hHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 3),
    _Xldv20pmS3hHistEntryNr_Type()
)
xldv20pmS3hHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hHistEntryNr.setStatus("mandatory")
_Xldv20pmS3hSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmS3hSuspectFlag_Object = MibTableColumn
xldv20pmS3hSuspectFlag = _Xldv20pmS3hSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 4),
    _Xldv20pmS3hSuspectFlag_Type()
)
xldv20pmS3hSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hSuspectFlag.setStatus("mandatory")


class _Xldv20pmS3hPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmS3hPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmS3hPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmS3hPeriodEndTime_Object = MibTableColumn
xldv20pmS3hPeriodEndTime = _Xldv20pmS3hPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 5),
    _Xldv20pmS3hPeriodEndTime_Type()
)
xldv20pmS3hPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hPeriodEndTime.setStatus("mandatory")
_Xldv20pmS3hNeErroredSeconds_Type = Counter32
_Xldv20pmS3hNeErroredSeconds_Object = MibTableColumn
xldv20pmS3hNeErroredSeconds = _Xldv20pmS3hNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 6),
    _Xldv20pmS3hNeErroredSeconds_Type()
)
xldv20pmS3hNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hNeErroredSeconds.setStatus("mandatory")
_Xldv20pmS3hFeErroredSeconds_Type = Counter32
_Xldv20pmS3hFeErroredSeconds_Object = MibTableColumn
xldv20pmS3hFeErroredSeconds = _Xldv20pmS3hFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 7),
    _Xldv20pmS3hFeErroredSeconds_Type()
)
xldv20pmS3hFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hFeErroredSeconds.setStatus("mandatory")
_Xldv20pmS3hNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS3hNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS3hNeSeverelyErroredSeconds = _Xldv20pmS3hNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 8),
    _Xldv20pmS3hNeSeverelyErroredSeconds_Type()
)
xldv20pmS3hNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS3hFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS3hFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS3hFeSeverelyErroredSeconds = _Xldv20pmS3hFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 9),
    _Xldv20pmS3hFeSeverelyErroredSeconds_Type()
)
xldv20pmS3hFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS3hNeCodeViolations_Type = Counter32
_Xldv20pmS3hNeCodeViolations_Object = MibTableColumn
xldv20pmS3hNeCodeViolations = _Xldv20pmS3hNeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 10),
    _Xldv20pmS3hNeCodeViolations_Type()
)
xldv20pmS3hNeCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hNeCodeViolations.setStatus("mandatory")
_Xldv20pmS3hFeCodeViolations_Type = Counter32
_Xldv20pmS3hFeCodeViolations_Object = MibTableColumn
xldv20pmS3hFeCodeViolations = _Xldv20pmS3hFeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 11),
    _Xldv20pmS3hFeCodeViolations_Type()
)
xldv20pmS3hFeCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hFeCodeViolations.setStatus("mandatory")
_Xldv20pmS3hNeUnavailableSeconds_Type = Counter32
_Xldv20pmS3hNeUnavailableSeconds_Object = MibTableColumn
xldv20pmS3hNeUnavailableSeconds = _Xldv20pmS3hNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 12),
    _Xldv20pmS3hNeUnavailableSeconds_Type()
)
xldv20pmS3hNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS3hFeUnavailableSeconds_Type = Counter32
_Xldv20pmS3hFeUnavailableSeconds_Object = MibTableColumn
xldv20pmS3hFeUnavailableSeconds = _Xldv20pmS3hFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 13),
    _Xldv20pmS3hFeUnavailableSeconds_Type()
)
xldv20pmS3hFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS3hNeSeverelyErroredFrameSeconds_Type = Counter32
_Xldv20pmS3hNeSeverelyErroredFrameSeconds_Object = MibTableColumn
xldv20pmS3hNeSeverelyErroredFrameSeconds = _Xldv20pmS3hNeSeverelyErroredFrameSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 5, 1, 14),
    _Xldv20pmS3hNeSeverelyErroredFrameSeconds_Type()
)
xldv20pmS3hNeSeverelyErroredFrameSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS3hNeSeverelyErroredFrameSeconds.setStatus("mandatory")
_Xldv20pmD3CurrentTable_Object = MibTable
xldv20pmD3CurrentTable = _Xldv20pmD3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6)
)
if mibBuilder.loadTexts:
    xldv20pmD3CurrentTable.setStatus("mandatory")
_Xldv20pmD3CurrentEntry_Object = MibTableRow
xldv20pmD3CurrentEntry = _Xldv20pmD3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1)
)
xldv20pmD3CurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmD3cIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmD3cOAMLevel"),
)
if mibBuilder.loadTexts:
    xldv20pmD3CurrentEntry.setStatus("mandatory")
_Xldv20pmD3cIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmD3cIntervalType_Object = MibTableColumn
xldv20pmD3cIntervalType = _Xldv20pmD3cIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 1),
    _Xldv20pmD3cIntervalType_Type()
)
xldv20pmD3cIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cIntervalType.setStatus("mandatory")


class _Xldv20pmD3cOAMLevel_Type(Integer32):
    """Custom type xldv20pmD3cOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmD3cOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmD3cOAMLevel_Object = MibTableColumn
xldv20pmD3cOAMLevel = _Xldv20pmD3cOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 2),
    _Xldv20pmD3cOAMLevel_Type()
)
xldv20pmD3cOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cOAMLevel.setStatus("mandatory")
_Xldv20pmD3cAdminState_Type = Xldv20AdminState
_Xldv20pmD3cAdminState_Object = MibTableColumn
xldv20pmD3cAdminState = _Xldv20pmD3cAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 3),
    _Xldv20pmD3cAdminState_Type()
)
xldv20pmD3cAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmD3cAdminState.setStatus("mandatory")
_Xldv20pmD3cSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmD3cSuspectFlag_Object = MibTableColumn
xldv20pmD3cSuspectFlag = _Xldv20pmD3cSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 4),
    _Xldv20pmD3cSuspectFlag_Type()
)
xldv20pmD3cSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cSuspectFlag.setStatus("mandatory")


class _Xldv20pmD3cHistEntrySize_Type(Integer32):
    """Custom type xldv20pmD3cHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmD3cHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmD3cHistEntrySize_Object = MibTableColumn
xldv20pmD3cHistEntrySize = _Xldv20pmD3cHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 5),
    _Xldv20pmD3cHistEntrySize_Type()
)
xldv20pmD3cHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cHistEntrySize.setStatus("mandatory")


class _Xldv20pmD3cNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmD3cNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmD3cNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmD3cNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmD3cNrHistEntriesAvailable = _Xldv20pmD3cNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 6),
    _Xldv20pmD3cNrHistEntriesAvailable_Type()
)
xldv20pmD3cNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmD3cElapsedTime_Type(Integer32):
    """Custom type xldv20pmD3cElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmD3cElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmD3cElapsedTime_Object = MibTableColumn
xldv20pmD3cElapsedTime = _Xldv20pmD3cElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 7),
    _Xldv20pmD3cElapsedTime_Type()
)
xldv20pmD3cElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cElapsedTime.setStatus("mandatory")


class _Xldv20pmD3cThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmD3cThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmD3cThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmD3cThresholdLimitIndex_Object = MibTableColumn
xldv20pmD3cThresholdLimitIndex = _Xldv20pmD3cThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 8),
    _Xldv20pmD3cThresholdLimitIndex_Type()
)
xldv20pmD3cThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmD3cThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmD3cNeErroredSecondsCP_Type = Counter32
_Xldv20pmD3cNeErroredSecondsCP_Object = MibTableColumn
xldv20pmD3cNeErroredSecondsCP = _Xldv20pmD3cNeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 9),
    _Xldv20pmD3cNeErroredSecondsCP_Type()
)
xldv20pmD3cNeErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3cFeErroredSecondsCP_Type = Counter32
_Xldv20pmD3cFeErroredSecondsCP_Object = MibTableColumn
xldv20pmD3cFeErroredSecondsCP = _Xldv20pmD3cFeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 10),
    _Xldv20pmD3cFeErroredSecondsCP_Type()
)
xldv20pmD3cFeErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3cNeErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3cNeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3cNeErroredSecondsPLCP = _Xldv20pmD3cNeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 11),
    _Xldv20pmD3cNeErroredSecondsPLCP_Type()
)
xldv20pmD3cNeErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cFeErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3cFeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3cFeErroredSecondsPLCP = _Xldv20pmD3cFeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 12),
    _Xldv20pmD3cFeErroredSecondsPLCP_Type()
)
xldv20pmD3cFeErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cNeSeverelyErroredSecondsCP_Type = Counter32
_Xldv20pmD3cNeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmD3cNeSeverelyErroredSecondsCP = _Xldv20pmD3cNeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 13),
    _Xldv20pmD3cNeSeverelyErroredSecondsCP_Type()
)
xldv20pmD3cNeSeverelyErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeSeverelyErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3cFeSeverelyErroredSecondsCP_Type = Counter32
_Xldv20pmD3cFeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmD3cFeSeverelyErroredSecondsCP = _Xldv20pmD3cFeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 14),
    _Xldv20pmD3cFeSeverelyErroredSecondsCP_Type()
)
xldv20pmD3cFeSeverelyErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeSeverelyErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3cNeSeverelyErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3cNeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3cNeSeverelyErroredSecondsPLCP = _Xldv20pmD3cNeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 15),
    _Xldv20pmD3cNeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmD3cNeSeverelyErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeSeverelyErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cFeSeverelyErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3cFeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3cFeSeverelyErroredSecondsPLCP = _Xldv20pmD3cFeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 16),
    _Xldv20pmD3cFeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmD3cFeSeverelyErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeSeverelyErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cNeCodeViolationsP_Type = Counter32
_Xldv20pmD3cNeCodeViolationsP_Object = MibTableColumn
xldv20pmD3cNeCodeViolationsP = _Xldv20pmD3cNeCodeViolationsP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 17),
    _Xldv20pmD3cNeCodeViolationsP_Type()
)
xldv20pmD3cNeCodeViolationsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeCodeViolationsP.setStatus("mandatory")
_Xldv20pmD3cNeCodeViolationsCP_Type = Counter32
_Xldv20pmD3cNeCodeViolationsCP_Object = MibTableColumn
xldv20pmD3cNeCodeViolationsCP = _Xldv20pmD3cNeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 18),
    _Xldv20pmD3cNeCodeViolationsCP_Type()
)
xldv20pmD3cNeCodeViolationsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeCodeViolationsCP.setStatus("mandatory")
_Xldv20pmD3cFeCodeViolationsCP_Type = Counter32
_Xldv20pmD3cFeCodeViolationsCP_Object = MibTableColumn
xldv20pmD3cFeCodeViolationsCP = _Xldv20pmD3cFeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 19),
    _Xldv20pmD3cFeCodeViolationsCP_Type()
)
xldv20pmD3cFeCodeViolationsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeCodeViolationsCP.setStatus("mandatory")
_Xldv20pmD3cNeCodeViolationsPLCP_Type = Counter32
_Xldv20pmD3cNeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmD3cNeCodeViolationsPLCP = _Xldv20pmD3cNeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 20),
    _Xldv20pmD3cNeCodeViolationsPLCP_Type()
)
xldv20pmD3cNeCodeViolationsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeCodeViolationsPLCP.setStatus("mandatory")
_Xldv20pmD3cFeCodeViolationsPLCP_Type = Counter32
_Xldv20pmD3cFeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmD3cFeCodeViolationsPLCP = _Xldv20pmD3cFeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 21),
    _Xldv20pmD3cFeCodeViolationsPLCP_Type()
)
xldv20pmD3cFeCodeViolationsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeCodeViolationsPLCP.setStatus("mandatory")
_Xldv20pmD3cNeUnavailableSeconds_Type = Counter32
_Xldv20pmD3cNeUnavailableSeconds_Object = MibTableColumn
xldv20pmD3cNeUnavailableSeconds = _Xldv20pmD3cNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 22),
    _Xldv20pmD3cNeUnavailableSeconds_Type()
)
xldv20pmD3cNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmD3cFeUnavailableSeconds_Type = Counter32
_Xldv20pmD3cFeUnavailableSeconds_Object = MibTableColumn
xldv20pmD3cFeUnavailableSeconds = _Xldv20pmD3cFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 23),
    _Xldv20pmD3cFeUnavailableSeconds_Type()
)
xldv20pmD3cFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmD3cNeUnavailableSecondsPLCP_Type = Counter32
_Xldv20pmD3cNeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmD3cNeUnavailableSecondsPLCP = _Xldv20pmD3cNeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 24),
    _Xldv20pmD3cNeUnavailableSecondsPLCP_Type()
)
xldv20pmD3cNeUnavailableSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeUnavailableSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cFeUnavailableSecondsPLCP_Type = Counter32
_Xldv20pmD3cFeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmD3cFeUnavailableSecondsPLCP = _Xldv20pmD3cFeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 25),
    _Xldv20pmD3cFeUnavailableSecondsPLCP_Type()
)
xldv20pmD3cFeUnavailableSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeUnavailableSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3cNeSas_Type = Counter32
_Xldv20pmD3cNeSas_Object = MibTableColumn
xldv20pmD3cNeSas = _Xldv20pmD3cNeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 26),
    _Xldv20pmD3cNeSas_Type()
)
xldv20pmD3cNeSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cNeSas.setStatus("mandatory")
_Xldv20pmD3cFeSas_Type = Counter32
_Xldv20pmD3cFeSas_Object = MibTableColumn
xldv20pmD3cFeSas = _Xldv20pmD3cFeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 6, 1, 27),
    _Xldv20pmD3cFeSas_Type()
)
xldv20pmD3cFeSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3cFeSas.setStatus("mandatory")
_Xldv20pmD3HistoryTable_Object = MibTable
xldv20pmD3HistoryTable = _Xldv20pmD3HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7)
)
if mibBuilder.loadTexts:
    xldv20pmD3HistoryTable.setStatus("mandatory")
_Xldv20pmD3HistoryEntry_Object = MibTableRow
xldv20pmD3HistoryEntry = _Xldv20pmD3HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1)
)
xldv20pmD3HistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmD3hIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmD3hOAMLevel"),
    (0, "XLDV20PM-MIB", "xldv20pmD3hHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmD3HistoryEntry.setStatus("mandatory")
_Xldv20pmD3hIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmD3hIntervalType_Object = MibTableColumn
xldv20pmD3hIntervalType = _Xldv20pmD3hIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 1),
    _Xldv20pmD3hIntervalType_Type()
)
xldv20pmD3hIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hIntervalType.setStatus("mandatory")


class _Xldv20pmD3hOAMLevel_Type(Integer32):
    """Custom type xldv20pmD3hOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmD3hOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmD3hOAMLevel_Object = MibTableColumn
xldv20pmD3hOAMLevel = _Xldv20pmD3hOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 2),
    _Xldv20pmD3hOAMLevel_Type()
)
xldv20pmD3hOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hOAMLevel.setStatus("mandatory")


class _Xldv20pmD3hHistEntryNr_Type(Integer32):
    """Custom type xldv20pmD3hHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmD3hHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmD3hHistEntryNr_Object = MibTableColumn
xldv20pmD3hHistEntryNr = _Xldv20pmD3hHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 3),
    _Xldv20pmD3hHistEntryNr_Type()
)
xldv20pmD3hHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hHistEntryNr.setStatus("mandatory")
_Xldv20pmD3hSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmD3hSuspectFlag_Object = MibTableColumn
xldv20pmD3hSuspectFlag = _Xldv20pmD3hSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 4),
    _Xldv20pmD3hSuspectFlag_Type()
)
xldv20pmD3hSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hSuspectFlag.setStatus("mandatory")


class _Xldv20pmD3hPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmD3hPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmD3hPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmD3hPeriodEndTime_Object = MibTableColumn
xldv20pmD3hPeriodEndTime = _Xldv20pmD3hPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 5),
    _Xldv20pmD3hPeriodEndTime_Type()
)
xldv20pmD3hPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hPeriodEndTime.setStatus("mandatory")
_Xldv20pmD3hNeErroredSecondsCP_Type = Counter32
_Xldv20pmD3hNeErroredSecondsCP_Object = MibTableColumn
xldv20pmD3hNeErroredSecondsCP = _Xldv20pmD3hNeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 6),
    _Xldv20pmD3hNeErroredSecondsCP_Type()
)
xldv20pmD3hNeErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3hFeErroredSecondsCP_Type = Counter32
_Xldv20pmD3hFeErroredSecondsCP_Object = MibTableColumn
xldv20pmD3hFeErroredSecondsCP = _Xldv20pmD3hFeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 7),
    _Xldv20pmD3hFeErroredSecondsCP_Type()
)
xldv20pmD3hFeErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3hNeErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3hNeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3hNeErroredSecondsPLCP = _Xldv20pmD3hNeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 8),
    _Xldv20pmD3hNeErroredSecondsPLCP_Type()
)
xldv20pmD3hNeErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hFeErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3hFeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3hFeErroredSecondsPLCP = _Xldv20pmD3hFeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 9),
    _Xldv20pmD3hFeErroredSecondsPLCP_Type()
)
xldv20pmD3hFeErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hNeSeverelyErroredSecondsCP_Type = Counter32
_Xldv20pmD3hNeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmD3hNeSeverelyErroredSecondsCP = _Xldv20pmD3hNeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 10),
    _Xldv20pmD3hNeSeverelyErroredSecondsCP_Type()
)
xldv20pmD3hNeSeverelyErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeSeverelyErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3hFeSeverelyErroredSecondsCP_Type = Counter32
_Xldv20pmD3hFeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmD3hFeSeverelyErroredSecondsCP = _Xldv20pmD3hFeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 11),
    _Xldv20pmD3hFeSeverelyErroredSecondsCP_Type()
)
xldv20pmD3hFeSeverelyErroredSecondsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeSeverelyErroredSecondsCP.setStatus("mandatory")
_Xldv20pmD3hNeSeverelyErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3hNeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3hNeSeverelyErroredSecondsPLCP = _Xldv20pmD3hNeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 12),
    _Xldv20pmD3hNeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmD3hNeSeverelyErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeSeverelyErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hFeSeverelyErroredSecondsPLCP_Type = Counter32
_Xldv20pmD3hFeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmD3hFeSeverelyErroredSecondsPLCP = _Xldv20pmD3hFeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 13),
    _Xldv20pmD3hFeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmD3hFeSeverelyErroredSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeSeverelyErroredSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hNeCodeViolationsP_Type = Counter32
_Xldv20pmD3hNeCodeViolationsP_Object = MibTableColumn
xldv20pmD3hNeCodeViolationsP = _Xldv20pmD3hNeCodeViolationsP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 14),
    _Xldv20pmD3hNeCodeViolationsP_Type()
)
xldv20pmD3hNeCodeViolationsP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeCodeViolationsP.setStatus("mandatory")
_Xldv20pmD3hNeCodeViolationsCP_Type = Counter32
_Xldv20pmD3hNeCodeViolationsCP_Object = MibTableColumn
xldv20pmD3hNeCodeViolationsCP = _Xldv20pmD3hNeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 15),
    _Xldv20pmD3hNeCodeViolationsCP_Type()
)
xldv20pmD3hNeCodeViolationsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeCodeViolationsCP.setStatus("mandatory")
_Xldv20pmD3hFeCodeViolationsCP_Type = Counter32
_Xldv20pmD3hFeCodeViolationsCP_Object = MibTableColumn
xldv20pmD3hFeCodeViolationsCP = _Xldv20pmD3hFeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 16),
    _Xldv20pmD3hFeCodeViolationsCP_Type()
)
xldv20pmD3hFeCodeViolationsCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeCodeViolationsCP.setStatus("mandatory")
_Xldv20pmD3hNeCodeViolationsPLCP_Type = Counter32
_Xldv20pmD3hNeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmD3hNeCodeViolationsPLCP = _Xldv20pmD3hNeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 17),
    _Xldv20pmD3hNeCodeViolationsPLCP_Type()
)
xldv20pmD3hNeCodeViolationsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeCodeViolationsPLCP.setStatus("mandatory")
_Xldv20pmD3hFeCodeViolationsPLCP_Type = Counter32
_Xldv20pmD3hFeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmD3hFeCodeViolationsPLCP = _Xldv20pmD3hFeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 18),
    _Xldv20pmD3hFeCodeViolationsPLCP_Type()
)
xldv20pmD3hFeCodeViolationsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeCodeViolationsPLCP.setStatus("mandatory")
_Xldv20pmD3hNeUnavailableSeconds_Type = Counter32
_Xldv20pmD3hNeUnavailableSeconds_Object = MibTableColumn
xldv20pmD3hNeUnavailableSeconds = _Xldv20pmD3hNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 19),
    _Xldv20pmD3hNeUnavailableSeconds_Type()
)
xldv20pmD3hNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmD3hFeUnavailableSeconds_Type = Counter32
_Xldv20pmD3hFeUnavailableSeconds_Object = MibTableColumn
xldv20pmD3hFeUnavailableSeconds = _Xldv20pmD3hFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 20),
    _Xldv20pmD3hFeUnavailableSeconds_Type()
)
xldv20pmD3hFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmD3hNeUnavailableSecondsPLCP_Type = Counter32
_Xldv20pmD3hNeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmD3hNeUnavailableSecondsPLCP = _Xldv20pmD3hNeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 21),
    _Xldv20pmD3hNeUnavailableSecondsPLCP_Type()
)
xldv20pmD3hNeUnavailableSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeUnavailableSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hFeUnavailableSecondsPLCP_Type = Counter32
_Xldv20pmD3hFeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmD3hFeUnavailableSecondsPLCP = _Xldv20pmD3hFeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 22),
    _Xldv20pmD3hFeUnavailableSecondsPLCP_Type()
)
xldv20pmD3hFeUnavailableSecondsPLCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeUnavailableSecondsPLCP.setStatus("mandatory")
_Xldv20pmD3hNeSas_Type = Counter32
_Xldv20pmD3hNeSas_Object = MibTableColumn
xldv20pmD3hNeSas = _Xldv20pmD3hNeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 23),
    _Xldv20pmD3hNeSas_Type()
)
xldv20pmD3hNeSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hNeSas.setStatus("mandatory")
_Xldv20pmD3hFeSas_Type = Counter32
_Xldv20pmD3hFeSas_Object = MibTableColumn
xldv20pmD3hFeSas = _Xldv20pmD3hFeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 7, 1, 24),
    _Xldv20pmD3hFeSas_Type()
)
xldv20pmD3hFeSas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmD3hFeSas.setStatus("mandatory")
_Xldv20pmS1CurrentTable_Object = MibTable
xldv20pmS1CurrentTable = _Xldv20pmS1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8)
)
if mibBuilder.loadTexts:
    xldv20pmS1CurrentTable.setStatus("mandatory")
_Xldv20pmS1CurrentEntry_Object = MibTableRow
xldv20pmS1CurrentEntry = _Xldv20pmS1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1)
)
xldv20pmS1CurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmS1cIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmS1cOAMLevel"),
)
if mibBuilder.loadTexts:
    xldv20pmS1CurrentEntry.setStatus("mandatory")
_Xldv20pmS1cIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmS1cIntervalType_Object = MibTableColumn
xldv20pmS1cIntervalType = _Xldv20pmS1cIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 1),
    _Xldv20pmS1cIntervalType_Type()
)
xldv20pmS1cIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cIntervalType.setStatus("mandatory")


class _Xldv20pmS1cOAMLevel_Type(Integer32):
    """Custom type xldv20pmS1cOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmS1cOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmS1cOAMLevel_Object = MibTableColumn
xldv20pmS1cOAMLevel = _Xldv20pmS1cOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 2),
    _Xldv20pmS1cOAMLevel_Type()
)
xldv20pmS1cOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cOAMLevel.setStatus("mandatory")
_Xldv20pmS1cAdminState_Type = Xldv20AdminState
_Xldv20pmS1cAdminState_Object = MibTableColumn
xldv20pmS1cAdminState = _Xldv20pmS1cAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 3),
    _Xldv20pmS1cAdminState_Type()
)
xldv20pmS1cAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmS1cAdminState.setStatus("mandatory")
_Xldv20pmS1cSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmS1cSuspectFlag_Object = MibTableColumn
xldv20pmS1cSuspectFlag = _Xldv20pmS1cSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 4),
    _Xldv20pmS1cSuspectFlag_Type()
)
xldv20pmS1cSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cSuspectFlag.setStatus("mandatory")


class _Xldv20pmS1cHistEntrySize_Type(Integer32):
    """Custom type xldv20pmS1cHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmS1cHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmS1cHistEntrySize_Object = MibTableColumn
xldv20pmS1cHistEntrySize = _Xldv20pmS1cHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 5),
    _Xldv20pmS1cHistEntrySize_Type()
)
xldv20pmS1cHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cHistEntrySize.setStatus("mandatory")


class _Xldv20pmS1cNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmS1cNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmS1cNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmS1cNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmS1cNrHistEntriesAvailable = _Xldv20pmS1cNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 6),
    _Xldv20pmS1cNrHistEntriesAvailable_Type()
)
xldv20pmS1cNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmS1cElapsedTime_Type(Integer32):
    """Custom type xldv20pmS1cElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmS1cElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmS1cElapsedTime_Object = MibTableColumn
xldv20pmS1cElapsedTime = _Xldv20pmS1cElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 7),
    _Xldv20pmS1cElapsedTime_Type()
)
xldv20pmS1cElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cElapsedTime.setStatus("mandatory")


class _Xldv20pmS1cThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmS1cThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmS1cThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmS1cThresholdLimitIndex_Object = MibTableColumn
xldv20pmS1cThresholdLimitIndex = _Xldv20pmS1cThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 8),
    _Xldv20pmS1cThresholdLimitIndex_Type()
)
xldv20pmS1cThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmS1cThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmS1cNeErroredSeconds_Type = Counter32
_Xldv20pmS1cNeErroredSeconds_Object = MibTableColumn
xldv20pmS1cNeErroredSeconds = _Xldv20pmS1cNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 9),
    _Xldv20pmS1cNeErroredSeconds_Type()
)
xldv20pmS1cNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeErroredSeconds.setStatus("mandatory")
_Xldv20pmS1cFeErroredSeconds_Type = Counter32
_Xldv20pmS1cFeErroredSeconds_Object = MibTableColumn
xldv20pmS1cFeErroredSeconds = _Xldv20pmS1cFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 10),
    _Xldv20pmS1cFeErroredSeconds_Type()
)
xldv20pmS1cFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cFeErroredSeconds.setStatus("mandatory")
_Xldv20pmS1cNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS1cNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS1cNeSeverelyErroredSeconds = _Xldv20pmS1cNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 11),
    _Xldv20pmS1cNeSeverelyErroredSeconds_Type()
)
xldv20pmS1cNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS1cFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS1cFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS1cFeSeverelyErroredSeconds = _Xldv20pmS1cFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 12),
    _Xldv20pmS1cFeSeverelyErroredSeconds_Type()
)
xldv20pmS1cFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS1cNeBackgroundBlockErrors_Type = Counter32
_Xldv20pmS1cNeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmS1cNeBackgroundBlockErrors = _Xldv20pmS1cNeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 13),
    _Xldv20pmS1cNeBackgroundBlockErrors_Type()
)
xldv20pmS1cNeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmS1cFeBackgroundBlockErrors_Type = Counter32
_Xldv20pmS1cFeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmS1cFeBackgroundBlockErrors = _Xldv20pmS1cFeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 14),
    _Xldv20pmS1cFeBackgroundBlockErrors_Type()
)
xldv20pmS1cFeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cFeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmS1cNeUnavailableSeconds_Type = Counter32
_Xldv20pmS1cNeUnavailableSeconds_Object = MibTableColumn
xldv20pmS1cNeUnavailableSeconds = _Xldv20pmS1cNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 15),
    _Xldv20pmS1cNeUnavailableSeconds_Type()
)
xldv20pmS1cNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS1cFeUnavailableSeconds_Type = Counter32
_Xldv20pmS1cFeUnavailableSeconds_Object = MibTableColumn
xldv20pmS1cFeUnavailableSeconds = _Xldv20pmS1cFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 16),
    _Xldv20pmS1cFeUnavailableSeconds_Type()
)
xldv20pmS1cFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS1cNeOfsSeconds_Type = Counter32
_Xldv20pmS1cNeOfsSeconds_Object = MibTableColumn
xldv20pmS1cNeOfsSeconds = _Xldv20pmS1cNeOfsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 17),
    _Xldv20pmS1cNeOfsSeconds_Type()
)
xldv20pmS1cNeOfsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeOfsSeconds.setStatus("mandatory")
_Xldv20pmS1cNeAisSeconds_Type = Counter32
_Xldv20pmS1cNeAisSeconds_Object = MibTableColumn
xldv20pmS1cNeAisSeconds = _Xldv20pmS1cNeAisSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 18),
    _Xldv20pmS1cNeAisSeconds_Type()
)
xldv20pmS1cNeAisSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeAisSeconds.setStatus("mandatory")
_Xldv20pmS1cNeLosSeconds_Type = Counter32
_Xldv20pmS1cNeLosSeconds_Object = MibTableColumn
xldv20pmS1cNeLosSeconds = _Xldv20pmS1cNeLosSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 8, 1, 19),
    _Xldv20pmS1cNeLosSeconds_Type()
)
xldv20pmS1cNeLosSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1cNeLosSeconds.setStatus("mandatory")
_Xldv20pmS1HistoryTable_Object = MibTable
xldv20pmS1HistoryTable = _Xldv20pmS1HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9)
)
if mibBuilder.loadTexts:
    xldv20pmS1HistoryTable.setStatus("mandatory")
_Xldv20pmS1HistoryEntry_Object = MibTableRow
xldv20pmS1HistoryEntry = _Xldv20pmS1HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1)
)
xldv20pmS1HistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmS1hIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmS1hOAMLevel"),
    (0, "XLDV20PM-MIB", "xldv20pmS1hHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmS1HistoryEntry.setStatus("mandatory")
_Xldv20pmS1hIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmS1hIntervalType_Object = MibTableColumn
xldv20pmS1hIntervalType = _Xldv20pmS1hIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 1),
    _Xldv20pmS1hIntervalType_Type()
)
xldv20pmS1hIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hIntervalType.setStatus("mandatory")


class _Xldv20pmS1hOAMLevel_Type(Integer32):
    """Custom type xldv20pmS1hOAMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Xldv20pmS1hOAMLevel_Type.__name__ = "Integer32"
_Xldv20pmS1hOAMLevel_Object = MibTableColumn
xldv20pmS1hOAMLevel = _Xldv20pmS1hOAMLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 2),
    _Xldv20pmS1hOAMLevel_Type()
)
xldv20pmS1hOAMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hOAMLevel.setStatus("mandatory")


class _Xldv20pmS1hHistEntryNr_Type(Integer32):
    """Custom type xldv20pmS1hHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmS1hHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmS1hHistEntryNr_Object = MibTableColumn
xldv20pmS1hHistEntryNr = _Xldv20pmS1hHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 3),
    _Xldv20pmS1hHistEntryNr_Type()
)
xldv20pmS1hHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hHistEntryNr.setStatus("mandatory")
_Xldv20pmS1hSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmS1hSuspectFlag_Object = MibTableColumn
xldv20pmS1hSuspectFlag = _Xldv20pmS1hSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 4),
    _Xldv20pmS1hSuspectFlag_Type()
)
xldv20pmS1hSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hSuspectFlag.setStatus("mandatory")


class _Xldv20pmS1hPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmS1hPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmS1hPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmS1hPeriodEndTime_Object = MibTableColumn
xldv20pmS1hPeriodEndTime = _Xldv20pmS1hPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 5),
    _Xldv20pmS1hPeriodEndTime_Type()
)
xldv20pmS1hPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hPeriodEndTime.setStatus("mandatory")
_Xldv20pmS1hNeErroredSeconds_Type = Counter32
_Xldv20pmS1hNeErroredSeconds_Object = MibTableColumn
xldv20pmS1hNeErroredSeconds = _Xldv20pmS1hNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 6),
    _Xldv20pmS1hNeErroredSeconds_Type()
)
xldv20pmS1hNeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeErroredSeconds.setStatus("mandatory")
_Xldv20pmS1hFeErroredSeconds_Type = Counter32
_Xldv20pmS1hFeErroredSeconds_Object = MibTableColumn
xldv20pmS1hFeErroredSeconds = _Xldv20pmS1hFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 7),
    _Xldv20pmS1hFeErroredSeconds_Type()
)
xldv20pmS1hFeErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hFeErroredSeconds.setStatus("mandatory")
_Xldv20pmS1hNeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS1hNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS1hNeSeverelyErroredSeconds = _Xldv20pmS1hNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 8),
    _Xldv20pmS1hNeSeverelyErroredSeconds_Type()
)
xldv20pmS1hNeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS1hFeSeverelyErroredSeconds_Type = Counter32
_Xldv20pmS1hFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmS1hFeSeverelyErroredSeconds = _Xldv20pmS1hFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 9),
    _Xldv20pmS1hFeSeverelyErroredSeconds_Type()
)
xldv20pmS1hFeSeverelyErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hFeSeverelyErroredSeconds.setStatus("mandatory")
_Xldv20pmS1hNeBackgroundBlockErrors_Type = Counter32
_Xldv20pmS1hNeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmS1hNeBackgroundBlockErrors = _Xldv20pmS1hNeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 10),
    _Xldv20pmS1hNeBackgroundBlockErrors_Type()
)
xldv20pmS1hNeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmS1hFeBackgroundBlockErrors_Type = Counter32
_Xldv20pmS1hFeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmS1hFeBackgroundBlockErrors = _Xldv20pmS1hFeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 11),
    _Xldv20pmS1hFeBackgroundBlockErrors_Type()
)
xldv20pmS1hFeBackgroundBlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hFeBackgroundBlockErrors.setStatus("mandatory")
_Xldv20pmS1hNeUnavailableSeconds_Type = Counter32
_Xldv20pmS1hNeUnavailableSeconds_Object = MibTableColumn
xldv20pmS1hNeUnavailableSeconds = _Xldv20pmS1hNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 12),
    _Xldv20pmS1hNeUnavailableSeconds_Type()
)
xldv20pmS1hNeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS1hFeUnavailableSeconds_Type = Counter32
_Xldv20pmS1hFeUnavailableSeconds_Object = MibTableColumn
xldv20pmS1hFeUnavailableSeconds = _Xldv20pmS1hFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 13),
    _Xldv20pmS1hFeUnavailableSeconds_Type()
)
xldv20pmS1hFeUnavailableSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hFeUnavailableSeconds.setStatus("mandatory")
_Xldv20pmS1hNeOfsSeconds_Type = Counter32
_Xldv20pmS1hNeOfsSeconds_Object = MibTableColumn
xldv20pmS1hNeOfsSeconds = _Xldv20pmS1hNeOfsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 14),
    _Xldv20pmS1hNeOfsSeconds_Type()
)
xldv20pmS1hNeOfsSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeOfsSeconds.setStatus("mandatory")
_Xldv20pmS1hNeAisSeconds_Type = Counter32
_Xldv20pmS1hNeAisSeconds_Object = MibTableColumn
xldv20pmS1hNeAisSeconds = _Xldv20pmS1hNeAisSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 15),
    _Xldv20pmS1hNeAisSeconds_Type()
)
xldv20pmS1hNeAisSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeAisSeconds.setStatus("mandatory")
_Xldv20pmS1hNeLosSeconds_Type = Counter32
_Xldv20pmS1hNeLosSeconds_Object = MibTableColumn
xldv20pmS1hNeLosSeconds = _Xldv20pmS1hNeLosSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 9, 1, 16),
    _Xldv20pmS1hNeLosSeconds_Type()
)
xldv20pmS1hNeLosSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmS1hNeLosSeconds.setStatus("mandatory")
_Xldv20pmAtmObjectsTable_Object = MibTable
xldv20pmAtmObjectsTable = _Xldv20pmAtmObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10)
)
if mibBuilder.loadTexts:
    xldv20pmAtmObjectsTable.setStatus("mandatory")
_Xldv20pmAtmObjectsEntry_Object = MibTableRow
xldv20pmAtmObjectsEntry = _Xldv20pmAtmObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10, 1)
)
xldv20pmAtmObjectsEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmAoIndex"),
)
if mibBuilder.loadTexts:
    xldv20pmAtmObjectsEntry.setStatus("mandatory")


class _Xldv20pmAoIndex_Type(Integer32):
    """Custom type xldv20pmAoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Xldv20pmAoIndex_Type.__name__ = "Integer32"
_Xldv20pmAoIndex_Object = MibTableColumn
xldv20pmAoIndex = _Xldv20pmAoIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10, 1, 1),
    _Xldv20pmAoIndex_Type()
)
xldv20pmAoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAoIndex.setStatus("mandatory")
_Xldv20pmAoFlowType_Type = Xldv20pmFlowType
_Xldv20pmAoFlowType_Object = MibTableColumn
xldv20pmAoFlowType = _Xldv20pmAoFlowType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10, 1, 2),
    _Xldv20pmAoFlowType_Type()
)
xldv20pmAoFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAoFlowType.setStatus("mandatory")
_Xldv20pmAoAdminState_Type = Xldv20AdminState
_Xldv20pmAoAdminState_Object = MibTableColumn
xldv20pmAoAdminState = _Xldv20pmAoAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10, 1, 3),
    _Xldv20pmAoAdminState_Type()
)
xldv20pmAoAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAoAdminState.setStatus("mandatory")
_Xldv20pmAoBlockSize_Type = Xldv20pmBlockSizeType
_Xldv20pmAoBlockSize_Object = MibTableColumn
xldv20pmAoBlockSize = _Xldv20pmAoBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 10, 1, 4),
    _Xldv20pmAoBlockSize_Type()
)
xldv20pmAoBlockSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAoBlockSize.setStatus("mandatory")
_Xldv20pmAtmEndpointsTable_Object = MibTable
xldv20pmAtmEndpointsTable = _Xldv20pmAtmEndpointsTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11)
)
if mibBuilder.loadTexts:
    xldv20pmAtmEndpointsTable.setStatus("mandatory")
_Xldv20pmAtmEndpointsEntry_Object = MibTableRow
xldv20pmAtmEndpointsEntry = _Xldv20pmAtmEndpointsEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1)
)
xldv20pmAtmEndpointsEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmAoIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmAeEndpointType"),
)
if mibBuilder.loadTexts:
    xldv20pmAtmEndpointsEntry.setStatus("mandatory")
_Xldv20pmAeEndpointType_Type = Xldv20pmEndpointType
_Xldv20pmAeEndpointType_Object = MibTableColumn
xldv20pmAeEndpointType = _Xldv20pmAeEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1, 1),
    _Xldv20pmAeEndpointType_Type()
)
xldv20pmAeEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAeEndpointType.setStatus("mandatory")


class _Xldv20pmAeConnectionIndex_Type(Integer32):
    """Custom type xldv20pmAeConnectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Xldv20pmAeConnectionIndex_Type.__name__ = "Integer32"
_Xldv20pmAeConnectionIndex_Object = MibTableColumn
xldv20pmAeConnectionIndex = _Xldv20pmAeConnectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1, 2),
    _Xldv20pmAeConnectionIndex_Type()
)
xldv20pmAeConnectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAeConnectionIndex.setStatus("mandatory")
_Xldv20pmAeConnectionIndexType_Type = Xldv20pmConnectionIndexType
_Xldv20pmAeConnectionIndexType_Object = MibTableColumn
xldv20pmAeConnectionIndexType = _Xldv20pmAeConnectionIndexType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1, 3),
    _Xldv20pmAeConnectionIndexType_Type()
)
xldv20pmAeConnectionIndexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAeConnectionIndexType.setStatus("mandatory")
_Xldv20pmAeRole_Type = Xldv20pmRoleType
_Xldv20pmAeRole_Object = MibTableColumn
xldv20pmAeRole = _Xldv20pmAeRole_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1, 4),
    _Xldv20pmAeRole_Type()
)
xldv20pmAeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAeRole.setStatus("mandatory")
_Xldv20pmAeFlowDirection_Type = Xldv20FlowDirection
_Xldv20pmAeFlowDirection_Object = MibTableColumn
xldv20pmAeFlowDirection = _Xldv20pmAeFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 11, 1, 5),
    _Xldv20pmAeFlowDirection_Type()
)
xldv20pmAeFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAeFlowDirection.setStatus("mandatory")
_Xldv20pmAtmCurrentTable_Object = MibTable
xldv20pmAtmCurrentTable = _Xldv20pmAtmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12)
)
if mibBuilder.loadTexts:
    xldv20pmAtmCurrentTable.setStatus("mandatory")
_Xldv20pmAtmCurrentEntry_Object = MibTableRow
xldv20pmAtmCurrentEntry = _Xldv20pmAtmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1)
)
xldv20pmAtmCurrentEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmAoIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmAcIntervalType"),
)
if mibBuilder.loadTexts:
    xldv20pmAtmCurrentEntry.setStatus("mandatory")
_Xldv20pmAcIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmAcIntervalType_Object = MibTableColumn
xldv20pmAcIntervalType = _Xldv20pmAcIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 1),
    _Xldv20pmAcIntervalType_Type()
)
xldv20pmAcIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcIntervalType.setStatus("mandatory")
_Xldv20pmAcAdminState_Type = Xldv20AdminState
_Xldv20pmAcAdminState_Object = MibTableColumn
xldv20pmAcAdminState = _Xldv20pmAcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 2),
    _Xldv20pmAcAdminState_Type()
)
xldv20pmAcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcAdminState.setStatus("mandatory")
_Xldv20pmAcSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmAcSuspectFlag_Object = MibTableColumn
xldv20pmAcSuspectFlag = _Xldv20pmAcSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 3),
    _Xldv20pmAcSuspectFlag_Type()
)
xldv20pmAcSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcSuspectFlag.setStatus("mandatory")


class _Xldv20pmAcHistEntrySize_Type(Integer32):
    """Custom type xldv20pmAcHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmAcHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmAcHistEntrySize_Object = MibTableColumn
xldv20pmAcHistEntrySize = _Xldv20pmAcHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 4),
    _Xldv20pmAcHistEntrySize_Type()
)
xldv20pmAcHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcHistEntrySize.setStatus("mandatory")


class _Xldv20pmAcNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmAcNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmAcNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmAcNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmAcNrHistEntriesAvailable = _Xldv20pmAcNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 5),
    _Xldv20pmAcNrHistEntriesAvailable_Type()
)
xldv20pmAcNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmAcElapsedTime_Type(Integer32):
    """Custom type xldv20pmAcElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmAcElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmAcElapsedTime_Object = MibTableColumn
xldv20pmAcElapsedTime = _Xldv20pmAcElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 6),
    _Xldv20pmAcElapsedTime_Type()
)
xldv20pmAcElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcElapsedTime.setStatus("mandatory")


class _Xldv20pmAcThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmAcThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmAcThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmAcThresholdLimitIndex_Object = MibTableColumn
xldv20pmAcThresholdLimitIndex = _Xldv20pmAcThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 7),
    _Xldv20pmAcThresholdLimitIndex_Type()
)
xldv20pmAcThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAcThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmAcTransmittedUserCells_Type = Counter32
_Xldv20pmAcTransmittedUserCells_Object = MibTableColumn
xldv20pmAcTransmittedUserCells = _Xldv20pmAcTransmittedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 8),
    _Xldv20pmAcTransmittedUserCells_Type()
)
xldv20pmAcTransmittedUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcTransmittedUserCells.setStatus("mandatory")
_Xldv20pmAcLostUserCells_Type = Counter32
_Xldv20pmAcLostUserCells_Object = MibTableColumn
xldv20pmAcLostUserCells = _Xldv20pmAcLostUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 9),
    _Xldv20pmAcLostUserCells_Type()
)
xldv20pmAcLostUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcLostUserCells.setStatus("mandatory")
_Xldv20pmAcMisinsertedUserCells_Type = Counter32
_Xldv20pmAcMisinsertedUserCells_Object = MibTableColumn
xldv20pmAcMisinsertedUserCells = _Xldv20pmAcMisinsertedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 12, 1, 10),
    _Xldv20pmAcMisinsertedUserCells_Type()
)
xldv20pmAcMisinsertedUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAcMisinsertedUserCells.setStatus("mandatory")
_Xldv20pmAtmHistoryTable_Object = MibTable
xldv20pmAtmHistoryTable = _Xldv20pmAtmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13)
)
if mibBuilder.loadTexts:
    xldv20pmAtmHistoryTable.setStatus("mandatory")
_Xldv20pmAtmHistoryEntry_Object = MibTableRow
xldv20pmAtmHistoryEntry = _Xldv20pmAtmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1)
)
xldv20pmAtmHistoryEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmAoIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmAhIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmAhHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmAtmHistoryEntry.setStatus("mandatory")
_Xldv20pmAhIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmAhIntervalType_Object = MibTableColumn
xldv20pmAhIntervalType = _Xldv20pmAhIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 1),
    _Xldv20pmAhIntervalType_Type()
)
xldv20pmAhIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhIntervalType.setStatus("mandatory")


class _Xldv20pmAhHistEntryNr_Type(Integer32):
    """Custom type xldv20pmAhHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmAhHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmAhHistEntryNr_Object = MibTableColumn
xldv20pmAhHistEntryNr = _Xldv20pmAhHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 2),
    _Xldv20pmAhHistEntryNr_Type()
)
xldv20pmAhHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhHistEntryNr.setStatus("mandatory")
_Xldv20pmAhSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmAhSuspectFlag_Object = MibTableColumn
xldv20pmAhSuspectFlag = _Xldv20pmAhSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 3),
    _Xldv20pmAhSuspectFlag_Type()
)
xldv20pmAhSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhSuspectFlag.setStatus("mandatory")


class _Xldv20pmAhPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmAhPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmAhPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmAhPeriodEndTime_Object = MibTableColumn
xldv20pmAhPeriodEndTime = _Xldv20pmAhPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 4),
    _Xldv20pmAhPeriodEndTime_Type()
)
xldv20pmAhPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhPeriodEndTime.setStatus("mandatory")
_Xldv20pmAhTransmittedUserCells_Type = Counter32
_Xldv20pmAhTransmittedUserCells_Object = MibTableColumn
xldv20pmAhTransmittedUserCells = _Xldv20pmAhTransmittedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 5),
    _Xldv20pmAhTransmittedUserCells_Type()
)
xldv20pmAhTransmittedUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhTransmittedUserCells.setStatus("mandatory")
_Xldv20pmAhLostUserCells_Type = Counter32
_Xldv20pmAhLostUserCells_Object = MibTableColumn
xldv20pmAhLostUserCells = _Xldv20pmAhLostUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 6),
    _Xldv20pmAhLostUserCells_Type()
)
xldv20pmAhLostUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhLostUserCells.setStatus("mandatory")
_Xldv20pmAhMisinsertedUserCells_Type = Counter32
_Xldv20pmAhMisinsertedUserCells_Object = MibTableColumn
xldv20pmAhMisinsertedUserCells = _Xldv20pmAhMisinsertedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 13, 1, 7),
    _Xldv20pmAhMisinsertedUserCells_Type()
)
xldv20pmAhMisinsertedUserCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAhMisinsertedUserCells.setStatus("mandatory")
_Xldv20pmImaGroupCurrentTable_Object = MibTable
xldv20pmImaGroupCurrentTable = _Xldv20pmImaGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14)
)
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentTable.setStatus("mandatory")
_Xldv20pmImaGroupCurrentEntry_Object = MibTableRow
xldv20pmImaGroupCurrentEntry = _Xldv20pmImaGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1)
)
xldv20pmImaGroupCurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmImaGroupCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentEntry.setStatus("mandatory")
_Xldv20pmImaGroupCurrentIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmImaGroupCurrentIntervalType_Object = MibTableColumn
xldv20pmImaGroupCurrentIntervalType = _Xldv20pmImaGroupCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 1),
    _Xldv20pmImaGroupCurrentIntervalType_Type()
)
xldv20pmImaGroupCurrentIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentIntervalType.setStatus("mandatory")
_Xldv20pmImaGroupCurrentAdminState_Type = Xldv20AdminState
_Xldv20pmImaGroupCurrentAdminState_Object = MibTableColumn
xldv20pmImaGroupCurrentAdminState = _Xldv20pmImaGroupCurrentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 2),
    _Xldv20pmImaGroupCurrentAdminState_Type()
)
xldv20pmImaGroupCurrentAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentAdminState.setStatus("mandatory")
_Xldv20pmImaGroupCurrentSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmImaGroupCurrentSuspectFlag_Object = MibTableColumn
xldv20pmImaGroupCurrentSuspectFlag = _Xldv20pmImaGroupCurrentSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 3),
    _Xldv20pmImaGroupCurrentSuspectFlag_Type()
)
xldv20pmImaGroupCurrentSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentSuspectFlag.setStatus("mandatory")


class _Xldv20pmImaGroupCurrentHistEntrySize_Type(Integer32):
    """Custom type xldv20pmImaGroupCurrentHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmImaGroupCurrentHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmImaGroupCurrentHistEntrySize_Object = MibTableColumn
xldv20pmImaGroupCurrentHistEntrySize = _Xldv20pmImaGroupCurrentHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 4),
    _Xldv20pmImaGroupCurrentHistEntrySize_Type()
)
xldv20pmImaGroupCurrentHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentHistEntrySize.setStatus("mandatory")


class _Xldv20pmImaGroupCurrentNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmImaGroupCurrentNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmImaGroupCurrentNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmImaGroupCurrentNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmImaGroupCurrentNrHistEntriesAvailable = _Xldv20pmImaGroupCurrentNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 5),
    _Xldv20pmImaGroupCurrentNrHistEntriesAvailable_Type()
)
xldv20pmImaGroupCurrentNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmImaGroupCurrentElapsedTime_Type(Integer32):
    """Custom type xldv20pmImaGroupCurrentElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmImaGroupCurrentElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmImaGroupCurrentElapsedTime_Object = MibTableColumn
xldv20pmImaGroupCurrentElapsedTime = _Xldv20pmImaGroupCurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 6),
    _Xldv20pmImaGroupCurrentElapsedTime_Type()
)
xldv20pmImaGroupCurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentElapsedTime.setStatus("mandatory")


class _Xldv20pmImaGroupCurrentThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmImaGroupCurrentThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmImaGroupCurrentThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmImaGroupCurrentThresholdLimitIndex_Object = MibTableColumn
xldv20pmImaGroupCurrentThresholdLimitIndex = _Xldv20pmImaGroupCurrentThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 7),
    _Xldv20pmImaGroupCurrentThresholdLimitIndex_Type()
)
xldv20pmImaGroupCurrentThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmImaGroupCurrentUnavailSecs_Type = Gauge32
_Xldv20pmImaGroupCurrentUnavailSecs_Object = MibTableColumn
xldv20pmImaGroupCurrentUnavailSecs = _Xldv20pmImaGroupCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 8),
    _Xldv20pmImaGroupCurrentUnavailSecs_Type()
)
xldv20pmImaGroupCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentUnavailSecs.setStatus("mandatory")
_Xldv20pmImaGroupCurrentNeNumFailures_Type = Gauge32
_Xldv20pmImaGroupCurrentNeNumFailures_Object = MibTableColumn
xldv20pmImaGroupCurrentNeNumFailures = _Xldv20pmImaGroupCurrentNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 14, 1, 9),
    _Xldv20pmImaGroupCurrentNeNumFailures_Type()
)
xldv20pmImaGroupCurrentNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupCurrentNeNumFailures.setStatus("mandatory")
_Xldv20pmImaGroupHistoryTable_Object = MibTable
xldv20pmImaGroupHistoryTable = _Xldv20pmImaGroupHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15)
)
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryTable.setStatus("mandatory")
_Xldv20pmImaGroupHistoryEntry_Object = MibTableRow
xldv20pmImaGroupHistoryEntry = _Xldv20pmImaGroupHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1)
)
xldv20pmImaGroupHistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmImaGroupHistoryIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmImaGroupHistoryHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryEntry.setStatus("mandatory")
_Xldv20pmImaGroupHistoryIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmImaGroupHistoryIntervalType_Object = MibTableColumn
xldv20pmImaGroupHistoryIntervalType = _Xldv20pmImaGroupHistoryIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 1),
    _Xldv20pmImaGroupHistoryIntervalType_Type()
)
xldv20pmImaGroupHistoryIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryIntervalType.setStatus("mandatory")


class _Xldv20pmImaGroupHistoryHistEntryNr_Type(Integer32):
    """Custom type xldv20pmImaGroupHistoryHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmImaGroupHistoryHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmImaGroupHistoryHistEntryNr_Object = MibTableColumn
xldv20pmImaGroupHistoryHistEntryNr = _Xldv20pmImaGroupHistoryHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 2),
    _Xldv20pmImaGroupHistoryHistEntryNr_Type()
)
xldv20pmImaGroupHistoryHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryHistEntryNr.setStatus("mandatory")
_Xldv20pmImaGroupHistorySuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmImaGroupHistorySuspectFlag_Object = MibTableColumn
xldv20pmImaGroupHistorySuspectFlag = _Xldv20pmImaGroupHistorySuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 3),
    _Xldv20pmImaGroupHistorySuspectFlag_Type()
)
xldv20pmImaGroupHistorySuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistorySuspectFlag.setStatus("mandatory")


class _Xldv20pmImaGroupHistoryPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmImaGroupHistoryPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmImaGroupHistoryPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmImaGroupHistoryPeriodEndTime_Object = MibTableColumn
xldv20pmImaGroupHistoryPeriodEndTime = _Xldv20pmImaGroupHistoryPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 4),
    _Xldv20pmImaGroupHistoryPeriodEndTime_Type()
)
xldv20pmImaGroupHistoryPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryPeriodEndTime.setStatus("mandatory")
_Xldv20pmImaGroupHistoryUnavailSecs_Type = Gauge32
_Xldv20pmImaGroupHistoryUnavailSecs_Object = MibTableColumn
xldv20pmImaGroupHistoryUnavailSecs = _Xldv20pmImaGroupHistoryUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 5),
    _Xldv20pmImaGroupHistoryUnavailSecs_Type()
)
xldv20pmImaGroupHistoryUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryUnavailSecs.setStatus("mandatory")
_Xldv20pmImaGroupHistoryNeNumFailures_Type = Gauge32
_Xldv20pmImaGroupHistoryNeNumFailures_Object = MibTableColumn
xldv20pmImaGroupHistoryNeNumFailures = _Xldv20pmImaGroupHistoryNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 15, 1, 6),
    _Xldv20pmImaGroupHistoryNeNumFailures_Type()
)
xldv20pmImaGroupHistoryNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaGroupHistoryNeNumFailures.setStatus("mandatory")
_Xldv20pmImaLinkCurrentTable_Object = MibTable
xldv20pmImaLinkCurrentTable = _Xldv20pmImaLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16)
)
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentTable.setStatus("mandatory")
_Xldv20pmImaLinkCurrentEntry_Object = MibTableRow
xldv20pmImaLinkCurrentEntry = _Xldv20pmImaLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1)
)
xldv20pmImaLinkCurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmImaLinkCurrentIntervalType"),
)
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentEntry.setStatus("mandatory")
_Xldv20pmImaLinkCurrentIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmImaLinkCurrentIntervalType_Object = MibTableColumn
xldv20pmImaLinkCurrentIntervalType = _Xldv20pmImaLinkCurrentIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 1),
    _Xldv20pmImaLinkCurrentIntervalType_Type()
)
xldv20pmImaLinkCurrentIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentIntervalType.setStatus("mandatory")
_Xldv20pmImaLinkCurrentAdminState_Type = Xldv20AdminState
_Xldv20pmImaLinkCurrentAdminState_Object = MibTableColumn
xldv20pmImaLinkCurrentAdminState = _Xldv20pmImaLinkCurrentAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 2),
    _Xldv20pmImaLinkCurrentAdminState_Type()
)
xldv20pmImaLinkCurrentAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentAdminState.setStatus("mandatory")
_Xldv20pmImaLinkCurrentSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmImaLinkCurrentSuspectFlag_Object = MibTableColumn
xldv20pmImaLinkCurrentSuspectFlag = _Xldv20pmImaLinkCurrentSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 3),
    _Xldv20pmImaLinkCurrentSuspectFlag_Type()
)
xldv20pmImaLinkCurrentSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentSuspectFlag.setStatus("mandatory")


class _Xldv20pmImaLinkCurrentHistEntrySize_Type(Integer32):
    """Custom type xldv20pmImaLinkCurrentHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmImaLinkCurrentHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmImaLinkCurrentHistEntrySize_Object = MibTableColumn
xldv20pmImaLinkCurrentHistEntrySize = _Xldv20pmImaLinkCurrentHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 4),
    _Xldv20pmImaLinkCurrentHistEntrySize_Type()
)
xldv20pmImaLinkCurrentHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentHistEntrySize.setStatus("mandatory")


class _Xldv20pmImaLinkCurrentNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmImaLinkCurrentNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmImaLinkCurrentNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmImaLinkCurrentNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmImaLinkCurrentNrHistEntriesAvailable = _Xldv20pmImaLinkCurrentNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 5),
    _Xldv20pmImaLinkCurrentNrHistEntriesAvailable_Type()
)
xldv20pmImaLinkCurrentNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmImaLinkCurrentElapsedTime_Type(Integer32):
    """Custom type xldv20pmImaLinkCurrentElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmImaLinkCurrentElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmImaLinkCurrentElapsedTime_Object = MibTableColumn
xldv20pmImaLinkCurrentElapsedTime = _Xldv20pmImaLinkCurrentElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 6),
    _Xldv20pmImaLinkCurrentElapsedTime_Type()
)
xldv20pmImaLinkCurrentElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentElapsedTime.setStatus("mandatory")


class _Xldv20pmImaLinkCurrentThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmImaLinkCurrentThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmImaLinkCurrentThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmImaLinkCurrentThresholdLimitIndex_Object = MibTableColumn
xldv20pmImaLinkCurrentThresholdLimitIndex = _Xldv20pmImaLinkCurrentThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 7),
    _Xldv20pmImaLinkCurrentThresholdLimitIndex_Type()
)
xldv20pmImaLinkCurrentThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmImaLinkCurrentImaViolations_Type = Gauge32
_Xldv20pmImaLinkCurrentImaViolations_Object = MibTableColumn
xldv20pmImaLinkCurrentImaViolations = _Xldv20pmImaLinkCurrentImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 8),
    _Xldv20pmImaLinkCurrentImaViolations_Type()
)
xldv20pmImaLinkCurrentImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentImaViolations.setStatus("mandatory")
_Xldv20pmImaLinkCurrentOifAnomalies_Type = Gauge32
_Xldv20pmImaLinkCurrentOifAnomalies_Object = MibTableColumn
xldv20pmImaLinkCurrentOifAnomalies = _Xldv20pmImaLinkCurrentOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 9),
    _Xldv20pmImaLinkCurrentOifAnomalies_Type()
)
xldv20pmImaLinkCurrentOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentOifAnomalies.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeSevErroredSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentNeSevErroredSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentNeSevErroredSecs = _Xldv20pmImaLinkCurrentNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 10),
    _Xldv20pmImaLinkCurrentNeSevErroredSecs_Type()
)
xldv20pmImaLinkCurrentNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeSevErroredSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentFeSevErroredSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentFeSevErroredSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentFeSevErroredSecs = _Xldv20pmImaLinkCurrentFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 11),
    _Xldv20pmImaLinkCurrentFeSevErroredSecs_Type()
)
xldv20pmImaLinkCurrentFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentFeSevErroredSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeUnavailSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentNeUnavailSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentNeUnavailSecs = _Xldv20pmImaLinkCurrentNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 12),
    _Xldv20pmImaLinkCurrentNeUnavailSecs_Type()
)
xldv20pmImaLinkCurrentNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeUnavailSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentFeUnavailSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentFeUnavailSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentFeUnavailSecs = _Xldv20pmImaLinkCurrentFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 13),
    _Xldv20pmImaLinkCurrentFeUnavailSecs_Type()
)
xldv20pmImaLinkCurrentFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentFeUnavailSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeTxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentNeTxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentNeTxUnusableSecs = _Xldv20pmImaLinkCurrentNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 14),
    _Xldv20pmImaLinkCurrentNeTxUnusableSecs_Type()
)
xldv20pmImaLinkCurrentNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeTxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeRxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentNeRxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentNeRxUnusableSecs = _Xldv20pmImaLinkCurrentNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 15),
    _Xldv20pmImaLinkCurrentNeRxUnusableSecs_Type()
)
xldv20pmImaLinkCurrentNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeRxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentFeTxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentFeTxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentFeTxUnusableSecs = _Xldv20pmImaLinkCurrentFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 16),
    _Xldv20pmImaLinkCurrentFeTxUnusableSecs_Type()
)
xldv20pmImaLinkCurrentFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentFeTxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentFeRxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkCurrentFeRxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkCurrentFeRxUnusableSecs = _Xldv20pmImaLinkCurrentFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 17),
    _Xldv20pmImaLinkCurrentFeRxUnusableSecs_Type()
)
xldv20pmImaLinkCurrentFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentFeRxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeTxNumFailures_Type = Gauge32
_Xldv20pmImaLinkCurrentNeTxNumFailures_Object = MibTableColumn
xldv20pmImaLinkCurrentNeTxNumFailures = _Xldv20pmImaLinkCurrentNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 18),
    _Xldv20pmImaLinkCurrentNeTxNumFailures_Type()
)
xldv20pmImaLinkCurrentNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeTxNumFailures.setStatus("mandatory")
_Xldv20pmImaLinkCurrentNeRxNumFailures_Type = Gauge32
_Xldv20pmImaLinkCurrentNeRxNumFailures_Object = MibTableColumn
xldv20pmImaLinkCurrentNeRxNumFailures = _Xldv20pmImaLinkCurrentNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 16, 1, 19),
    _Xldv20pmImaLinkCurrentNeRxNumFailures_Type()
)
xldv20pmImaLinkCurrentNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkCurrentNeRxNumFailures.setStatus("mandatory")
_Xldv20pmImaLinkHistoryTable_Object = MibTable
xldv20pmImaLinkHistoryTable = _Xldv20pmImaLinkHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17)
)
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryTable.setStatus("mandatory")
_Xldv20pmImaLinkHistoryEntry_Object = MibTableRow
xldv20pmImaLinkHistoryEntry = _Xldv20pmImaLinkHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1)
)
xldv20pmImaLinkHistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmImaLinkHistoryIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmImaLinkHistoryHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryEntry.setStatus("mandatory")
_Xldv20pmImaLinkHistoryIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmImaLinkHistoryIntervalType_Object = MibTableColumn
xldv20pmImaLinkHistoryIntervalType = _Xldv20pmImaLinkHistoryIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 1),
    _Xldv20pmImaLinkHistoryIntervalType_Type()
)
xldv20pmImaLinkHistoryIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryIntervalType.setStatus("mandatory")


class _Xldv20pmImaLinkHistoryHistEntryNr_Type(Integer32):
    """Custom type xldv20pmImaLinkHistoryHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmImaLinkHistoryHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmImaLinkHistoryHistEntryNr_Object = MibTableColumn
xldv20pmImaLinkHistoryHistEntryNr = _Xldv20pmImaLinkHistoryHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 2),
    _Xldv20pmImaLinkHistoryHistEntryNr_Type()
)
xldv20pmImaLinkHistoryHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryHistEntryNr.setStatus("mandatory")
_Xldv20pmImaLinkHistorySuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmImaLinkHistorySuspectFlag_Object = MibTableColumn
xldv20pmImaLinkHistorySuspectFlag = _Xldv20pmImaLinkHistorySuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 3),
    _Xldv20pmImaLinkHistorySuspectFlag_Type()
)
xldv20pmImaLinkHistorySuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistorySuspectFlag.setStatus("mandatory")


class _Xldv20pmImaLinkHistoryPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmImaLinkHistoryPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmImaLinkHistoryPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmImaLinkHistoryPeriodEndTime_Object = MibTableColumn
xldv20pmImaLinkHistoryPeriodEndTime = _Xldv20pmImaLinkHistoryPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 4),
    _Xldv20pmImaLinkHistoryPeriodEndTime_Type()
)
xldv20pmImaLinkHistoryPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryPeriodEndTime.setStatus("mandatory")
_Xldv20pmImaLinkHistoryImaViolations_Type = Gauge32
_Xldv20pmImaLinkHistoryImaViolations_Object = MibTableColumn
xldv20pmImaLinkHistoryImaViolations = _Xldv20pmImaLinkHistoryImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 5),
    _Xldv20pmImaLinkHistoryImaViolations_Type()
)
xldv20pmImaLinkHistoryImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryImaViolations.setStatus("mandatory")
_Xldv20pmImaLinkHistoryOifAnomalies_Type = Gauge32
_Xldv20pmImaLinkHistoryOifAnomalies_Object = MibTableColumn
xldv20pmImaLinkHistoryOifAnomalies = _Xldv20pmImaLinkHistoryOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 6),
    _Xldv20pmImaLinkHistoryOifAnomalies_Type()
)
xldv20pmImaLinkHistoryOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryOifAnomalies.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeSevErroredSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryNeSevErroredSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryNeSevErroredSecs = _Xldv20pmImaLinkHistoryNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 7),
    _Xldv20pmImaLinkHistoryNeSevErroredSecs_Type()
)
xldv20pmImaLinkHistoryNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeSevErroredSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryFeSevErroredSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryFeSevErroredSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryFeSevErroredSecs = _Xldv20pmImaLinkHistoryFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 8),
    _Xldv20pmImaLinkHistoryFeSevErroredSecs_Type()
)
xldv20pmImaLinkHistoryFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryFeSevErroredSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeUnavailSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryNeUnavailSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryNeUnavailSecs = _Xldv20pmImaLinkHistoryNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 9),
    _Xldv20pmImaLinkHistoryNeUnavailSecs_Type()
)
xldv20pmImaLinkHistoryNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeUnavailSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryFeUnavailSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryFeUnavailSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryFeUnavailSecs = _Xldv20pmImaLinkHistoryFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 10),
    _Xldv20pmImaLinkHistoryFeUnavailSecs_Type()
)
xldv20pmImaLinkHistoryFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryFeUnavailSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeTxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryNeTxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryNeTxUnusableSecs = _Xldv20pmImaLinkHistoryNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 11),
    _Xldv20pmImaLinkHistoryNeTxUnusableSecs_Type()
)
xldv20pmImaLinkHistoryNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeTxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeRxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryNeRxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryNeRxUnusableSecs = _Xldv20pmImaLinkHistoryNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 12),
    _Xldv20pmImaLinkHistoryNeRxUnusableSecs_Type()
)
xldv20pmImaLinkHistoryNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeRxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryFeTxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryFeTxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryFeTxUnusableSecs = _Xldv20pmImaLinkHistoryFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 13),
    _Xldv20pmImaLinkHistoryFeTxUnusableSecs_Type()
)
xldv20pmImaLinkHistoryFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryFeTxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryFeRxUnusableSecs_Type = Gauge32
_Xldv20pmImaLinkHistoryFeRxUnusableSecs_Object = MibTableColumn
xldv20pmImaLinkHistoryFeRxUnusableSecs = _Xldv20pmImaLinkHistoryFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 14),
    _Xldv20pmImaLinkHistoryFeRxUnusableSecs_Type()
)
xldv20pmImaLinkHistoryFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryFeRxUnusableSecs.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeTxNumFailures_Type = Gauge32
_Xldv20pmImaLinkHistoryNeTxNumFailures_Object = MibTableColumn
xldv20pmImaLinkHistoryNeTxNumFailures = _Xldv20pmImaLinkHistoryNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 15),
    _Xldv20pmImaLinkHistoryNeTxNumFailures_Type()
)
xldv20pmImaLinkHistoryNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeTxNumFailures.setStatus("mandatory")
_Xldv20pmImaLinkHistoryNeRxNumFailures_Type = Gauge32
_Xldv20pmImaLinkHistoryNeRxNumFailures_Object = MibTableColumn
xldv20pmImaLinkHistoryNeRxNumFailures = _Xldv20pmImaLinkHistoryNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 2, 17, 1, 16),
    _Xldv20pmImaLinkHistoryNeRxNumFailures_Type()
)
xldv20pmImaLinkHistoryNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmImaLinkHistoryNeRxNumFailures.setStatus("mandatory")
_Xldv20pmProtocolMonitoring_ObjectIdentity = ObjectIdentity
xldv20pmProtocolMonitoring = _Xldv20pmProtocolMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3)
)
_Xldv20pmTcaPrMCurrentTable_Object = MibTable
xldv20pmTcaPrMCurrentTable = _Xldv20pmTcaPrMCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xldv20pmTcaPrMCurrentTable.setStatus("mandatory")
_Xldv20pmTcaPrMCurrentEntry_Object = MibTableRow
xldv20pmTcaPrMCurrentEntry = _Xldv20pmTcaPrMCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1)
)
xldv20pmTcaPrMCurrentEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmTcIntervalType"),
)
if mibBuilder.loadTexts:
    xldv20pmTcaPrMCurrentEntry.setStatus("mandatory")
_Xldv20pmTcIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmTcIntervalType_Object = MibTableColumn
xldv20pmTcIntervalType = _Xldv20pmTcIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 1),
    _Xldv20pmTcIntervalType_Type()
)
xldv20pmTcIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcIntervalType.setStatus("mandatory")
_Xldv20pmTcAdminState_Type = Xldv20AdminState
_Xldv20pmTcAdminState_Object = MibTableColumn
xldv20pmTcAdminState = _Xldv20pmTcAdminState_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 2),
    _Xldv20pmTcAdminState_Type()
)
xldv20pmTcAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmTcAdminState.setStatus("mandatory")
_Xldv20pmTcSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmTcSuspectFlag_Object = MibTableColumn
xldv20pmTcSuspectFlag = _Xldv20pmTcSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 3),
    _Xldv20pmTcSuspectFlag_Type()
)
xldv20pmTcSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcSuspectFlag.setStatus("mandatory")


class _Xldv20pmTcHistEntrySize_Type(Integer32):
    """Custom type xldv20pmTcHistEntrySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmTcHistEntrySize_Type.__name__ = "Integer32"
_Xldv20pmTcHistEntrySize_Object = MibTableColumn
xldv20pmTcHistEntrySize = _Xldv20pmTcHistEntrySize_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 4),
    _Xldv20pmTcHistEntrySize_Type()
)
xldv20pmTcHistEntrySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcHistEntrySize.setStatus("mandatory")


class _Xldv20pmTcNrHistEntriesAvailable_Type(Integer32):
    """Custom type xldv20pmTcNrHistEntriesAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xldv20pmTcNrHistEntriesAvailable_Type.__name__ = "Integer32"
_Xldv20pmTcNrHistEntriesAvailable_Object = MibTableColumn
xldv20pmTcNrHistEntriesAvailable = _Xldv20pmTcNrHistEntriesAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 5),
    _Xldv20pmTcNrHistEntriesAvailable_Type()
)
xldv20pmTcNrHistEntriesAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcNrHistEntriesAvailable.setStatus("mandatory")


class _Xldv20pmTcElapsedTime_Type(Integer32):
    """Custom type xldv20pmTcElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Xldv20pmTcElapsedTime_Type.__name__ = "Integer32"
_Xldv20pmTcElapsedTime_Object = MibTableColumn
xldv20pmTcElapsedTime = _Xldv20pmTcElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 6),
    _Xldv20pmTcElapsedTime_Type()
)
xldv20pmTcElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcElapsedTime.setStatus("mandatory")


class _Xldv20pmTcThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmTcThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmTcThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmTcThresholdLimitIndex_Object = MibTableColumn
xldv20pmTcThresholdLimitIndex = _Xldv20pmTcThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 7),
    _Xldv20pmTcThresholdLimitIndex_Type()
)
xldv20pmTcThresholdLimitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmTcThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmTcDiscardedCells_Type = Counter32
_Xldv20pmTcDiscardedCells_Object = MibTableColumn
xldv20pmTcDiscardedCells = _Xldv20pmTcDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 1, 1, 8),
    _Xldv20pmTcDiscardedCells_Type()
)
xldv20pmTcDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmTcDiscardedCells.setStatus("mandatory")
_Xldv20pmTcaPrMHistoryTable_Object = MibTable
xldv20pmTcaPrMHistoryTable = _Xldv20pmTcaPrMHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xldv20pmTcaPrMHistoryTable.setStatus("mandatory")
_Xldv20pmTcaPrMHistoryEntry_Object = MibTableRow
xldv20pmTcaPrMHistoryEntry = _Xldv20pmTcaPrMHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1)
)
xldv20pmTcaPrMHistoryEntry.setIndexNames(
    (0, "XLDV20-MIB", "xldv20IfIndex"),
    (0, "XLDV20PM-MIB", "xldv20pmThIntervalType"),
    (0, "XLDV20PM-MIB", "xldv20pmThHistEntryNr"),
)
if mibBuilder.loadTexts:
    xldv20pmTcaPrMHistoryEntry.setStatus("mandatory")
_Xldv20pmThIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmThIntervalType_Object = MibTableColumn
xldv20pmThIntervalType = _Xldv20pmThIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1, 1),
    _Xldv20pmThIntervalType_Type()
)
xldv20pmThIntervalType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThIntervalType.setStatus("mandatory")


class _Xldv20pmThHistEntryNr_Type(Integer32):
    """Custom type xldv20pmThHistEntryNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xldv20pmThHistEntryNr_Type.__name__ = "Integer32"
_Xldv20pmThHistEntryNr_Object = MibTableColumn
xldv20pmThHistEntryNr = _Xldv20pmThHistEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1, 2),
    _Xldv20pmThHistEntryNr_Type()
)
xldv20pmThHistEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThHistEntryNr.setStatus("mandatory")
_Xldv20pmThSuspectFlag_Type = Xldv20pmSuspectType
_Xldv20pmThSuspectFlag_Object = MibTableColumn
xldv20pmThSuspectFlag = _Xldv20pmThSuspectFlag_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1, 3),
    _Xldv20pmThSuspectFlag_Type()
)
xldv20pmThSuspectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThSuspectFlag.setStatus("mandatory")


class _Xldv20pmThPeriodEndTime_Type(Integer32):
    """Custom type xldv20pmThPeriodEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThPeriodEndTime_Type.__name__ = "Integer32"
_Xldv20pmThPeriodEndTime_Object = MibTableColumn
xldv20pmThPeriodEndTime = _Xldv20pmThPeriodEndTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1, 4),
    _Xldv20pmThPeriodEndTime_Type()
)
xldv20pmThPeriodEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThPeriodEndTime.setStatus("mandatory")
_Xldv20pmThDiscardedCells_Type = Counter32
_Xldv20pmThDiscardedCells_Object = MibTableColumn
xldv20pmThDiscardedCells = _Xldv20pmThDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 3, 2, 1, 5),
    _Xldv20pmThDiscardedCells_Type()
)
xldv20pmThDiscardedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThDiscardedCells.setStatus("mandatory")
_Xldv20pmThresholding_ObjectIdentity = ObjectIdentity
xldv20pmThresholding = _Xldv20pmThresholding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4)
)
_Xldv20pmThresholdLimitTable_Object = MibTable
xldv20pmThresholdLimitTable = _Xldv20pmThresholdLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    xldv20pmThresholdLimitTable.setStatus("mandatory")
_Xldv20pmThresholdLimitEntry_Object = MibTableRow
xldv20pmThresholdLimitEntry = _Xldv20pmThresholdLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1)
)
xldv20pmThresholdLimitEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmThlThresholdLimitIndex"),
)
if mibBuilder.loadTexts:
    xldv20pmThresholdLimitEntry.setStatus("mandatory")


class _Xldv20pmThlThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmThlThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmThlThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmThlThresholdLimitIndex_Object = MibTableColumn
xldv20pmThlThresholdLimitIndex = _Xldv20pmThlThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 1),
    _Xldv20pmThlThresholdLimitIndex_Type()
)
xldv20pmThlThresholdLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmThlThresholdLimitIndex.setStatus("mandatory")


class _Xldv20pmThlNeBackgroundBlockErrors_Type(Integer32):
    """Custom type xldv20pmThlNeBackgroundBlockErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlNeBackgroundBlockErrors_Type.__name__ = "Integer32"
_Xldv20pmThlNeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmThlNeBackgroundBlockErrors = _Xldv20pmThlNeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 2),
    _Xldv20pmThlNeBackgroundBlockErrors_Type()
)
xldv20pmThlNeBackgroundBlockErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeBackgroundBlockErrors.setStatus("mandatory")


class _Xldv20pmThlNeCodeViolations_Type(Integer32):
    """Custom type xldv20pmThlNeCodeViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlNeCodeViolations_Type.__name__ = "Integer32"
_Xldv20pmThlNeCodeViolations_Object = MibTableColumn
xldv20pmThlNeCodeViolations = _Xldv20pmThlNeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 3),
    _Xldv20pmThlNeCodeViolations_Type()
)
xldv20pmThlNeCodeViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeCodeViolations.setStatus("mandatory")


class _Xldv20pmThlNeCodeViolationsCP_Type(Integer32):
    """Custom type xldv20pmThlNeCodeViolationsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlNeCodeViolationsCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeCodeViolationsCP_Object = MibTableColumn
xldv20pmThlNeCodeViolationsCP = _Xldv20pmThlNeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 4),
    _Xldv20pmThlNeCodeViolationsCP_Type()
)
xldv20pmThlNeCodeViolationsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeCodeViolationsCP.setStatus("mandatory")


class _Xldv20pmThlNeCodeViolationsP_Type(Integer32):
    """Custom type xldv20pmThlNeCodeViolationsP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlNeCodeViolationsP_Type.__name__ = "Integer32"
_Xldv20pmThlNeCodeViolationsP_Object = MibTableColumn
xldv20pmThlNeCodeViolationsP = _Xldv20pmThlNeCodeViolationsP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 5),
    _Xldv20pmThlNeCodeViolationsP_Type()
)
xldv20pmThlNeCodeViolationsP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeCodeViolationsP.setStatus("mandatory")


class _Xldv20pmThlNeCodeViolationsPLCP_Type(Integer32):
    """Custom type xldv20pmThlNeCodeViolationsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlNeCodeViolationsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmThlNeCodeViolationsPLCP = _Xldv20pmThlNeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 6),
    _Xldv20pmThlNeCodeViolationsPLCP_Type()
)
xldv20pmThlNeCodeViolationsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeCodeViolationsPLCP.setStatus("mandatory")


class _Xldv20pmThlNeErroredSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeErroredSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeErroredSeconds_Object = MibTableColumn
xldv20pmThlNeErroredSeconds = _Xldv20pmThlNeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 7),
    _Xldv20pmThlNeErroredSeconds_Type()
)
xldv20pmThlNeErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeErroredSeconds.setStatus("mandatory")


class _Xldv20pmThlNeErroredSecondsCP_Type(Integer32):
    """Custom type xldv20pmThlNeErroredSecondsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeErroredSecondsCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeErroredSecondsCP_Object = MibTableColumn
xldv20pmThlNeErroredSecondsCP = _Xldv20pmThlNeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 8),
    _Xldv20pmThlNeErroredSecondsCP_Type()
)
xldv20pmThlNeErroredSecondsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeErroredSecondsCP.setStatus("mandatory")


class _Xldv20pmThlNeErroredSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlNeErroredSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeErroredSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmThlNeErroredSecondsPLCP = _Xldv20pmThlNeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 9),
    _Xldv20pmThlNeErroredSecondsPLCP_Type()
)
xldv20pmThlNeErroredSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeErroredSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlNeSas_Type(Integer32):
    """Custom type xldv20pmThlNeSas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeSas_Type.__name__ = "Integer32"
_Xldv20pmThlNeSas_Object = MibTableColumn
xldv20pmThlNeSas = _Xldv20pmThlNeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 10),
    _Xldv20pmThlNeSas_Type()
)
xldv20pmThlNeSas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeSas.setStatus("mandatory")


class _Xldv20pmThlNeSeverelyErroredFrameSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeSeverelyErroredFrameSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeSeverelyErroredFrameSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeSeverelyErroredFrameSeconds_Object = MibTableColumn
xldv20pmThlNeSeverelyErroredFrameSeconds = _Xldv20pmThlNeSeverelyErroredFrameSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 11),
    _Xldv20pmThlNeSeverelyErroredFrameSeconds_Type()
)
xldv20pmThlNeSeverelyErroredFrameSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeSeverelyErroredFrameSeconds.setStatus("mandatory")


class _Xldv20pmThlNeSeverelyErroredSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeSeverelyErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeSeverelyErroredSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmThlNeSeverelyErroredSeconds = _Xldv20pmThlNeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 12),
    _Xldv20pmThlNeSeverelyErroredSeconds_Type()
)
xldv20pmThlNeSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeSeverelyErroredSeconds.setStatus("mandatory")


class _Xldv20pmThlNeSeverelyErroredSecondsCP_Type(Integer32):
    """Custom type xldv20pmThlNeSeverelyErroredSecondsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeSeverelyErroredSecondsCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmThlNeSeverelyErroredSecondsCP = _Xldv20pmThlNeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 13),
    _Xldv20pmThlNeSeverelyErroredSecondsCP_Type()
)
xldv20pmThlNeSeverelyErroredSecondsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeSeverelyErroredSecondsCP.setStatus("mandatory")


class _Xldv20pmThlNeSeverelyErroredSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlNeSeverelyErroredSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeSeverelyErroredSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmThlNeSeverelyErroredSecondsPLCP = _Xldv20pmThlNeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 14),
    _Xldv20pmThlNeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmThlNeSeverelyErroredSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeSeverelyErroredSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlNeUnavailableSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeUnavailableSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeUnavailableSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeUnavailableSeconds_Object = MibTableColumn
xldv20pmThlNeUnavailableSeconds = _Xldv20pmThlNeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 15),
    _Xldv20pmThlNeUnavailableSeconds_Type()
)
xldv20pmThlNeUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeUnavailableSeconds.setStatus("mandatory")


class _Xldv20pmThlNeUnavailableSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlNeUnavailableSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeUnavailableSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlNeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmThlNeUnavailableSecondsPLCP = _Xldv20pmThlNeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 16),
    _Xldv20pmThlNeUnavailableSecondsPLCP_Type()
)
xldv20pmThlNeUnavailableSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeUnavailableSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlNeAisSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeAisSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeAisSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeAisSeconds_Object = MibTableColumn
xldv20pmThlNeAisSeconds = _Xldv20pmThlNeAisSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 17),
    _Xldv20pmThlNeAisSeconds_Type()
)
xldv20pmThlNeAisSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeAisSeconds.setStatus("mandatory")


class _Xldv20pmThlNeOfsSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeOfsSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeOfsSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeOfsSeconds_Object = MibTableColumn
xldv20pmThlNeOfsSeconds = _Xldv20pmThlNeOfsSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 18),
    _Xldv20pmThlNeOfsSeconds_Type()
)
xldv20pmThlNeOfsSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeOfsSeconds.setStatus("mandatory")


class _Xldv20pmThlNeLosSeconds_Type(Integer32):
    """Custom type xldv20pmThlNeLosSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlNeLosSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlNeLosSeconds_Object = MibTableColumn
xldv20pmThlNeLosSeconds = _Xldv20pmThlNeLosSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 19),
    _Xldv20pmThlNeLosSeconds_Type()
)
xldv20pmThlNeLosSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlNeLosSeconds.setStatus("mandatory")


class _Xldv20pmThlFeBackgroundBlockErrors_Type(Integer32):
    """Custom type xldv20pmThlFeBackgroundBlockErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlFeBackgroundBlockErrors_Type.__name__ = "Integer32"
_Xldv20pmThlFeBackgroundBlockErrors_Object = MibTableColumn
xldv20pmThlFeBackgroundBlockErrors = _Xldv20pmThlFeBackgroundBlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 20),
    _Xldv20pmThlFeBackgroundBlockErrors_Type()
)
xldv20pmThlFeBackgroundBlockErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeBackgroundBlockErrors.setStatus("mandatory")


class _Xldv20pmThlFeCodeViolations_Type(Integer32):
    """Custom type xldv20pmThlFeCodeViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlFeCodeViolations_Type.__name__ = "Integer32"
_Xldv20pmThlFeCodeViolations_Object = MibTableColumn
xldv20pmThlFeCodeViolations = _Xldv20pmThlFeCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 21),
    _Xldv20pmThlFeCodeViolations_Type()
)
xldv20pmThlFeCodeViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeCodeViolations.setStatus("mandatory")


class _Xldv20pmThlFeCodeViolationsCP_Type(Integer32):
    """Custom type xldv20pmThlFeCodeViolationsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlFeCodeViolationsCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeCodeViolationsCP_Object = MibTableColumn
xldv20pmThlFeCodeViolationsCP = _Xldv20pmThlFeCodeViolationsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 22),
    _Xldv20pmThlFeCodeViolationsCP_Type()
)
xldv20pmThlFeCodeViolationsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeCodeViolationsCP.setStatus("mandatory")


class _Xldv20pmThlFeCodeViolationsPLCP_Type(Integer32):
    """Custom type xldv20pmThlFeCodeViolationsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlFeCodeViolationsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeCodeViolationsPLCP_Object = MibTableColumn
xldv20pmThlFeCodeViolationsPLCP = _Xldv20pmThlFeCodeViolationsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 23),
    _Xldv20pmThlFeCodeViolationsPLCP_Type()
)
xldv20pmThlFeCodeViolationsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeCodeViolationsPLCP.setStatus("mandatory")


class _Xldv20pmThlFeErroredSeconds_Type(Integer32):
    """Custom type xldv20pmThlFeErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeErroredSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlFeErroredSeconds_Object = MibTableColumn
xldv20pmThlFeErroredSeconds = _Xldv20pmThlFeErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 24),
    _Xldv20pmThlFeErroredSeconds_Type()
)
xldv20pmThlFeErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeErroredSeconds.setStatus("mandatory")


class _Xldv20pmThlFeErroredSecondsCP_Type(Integer32):
    """Custom type xldv20pmThlFeErroredSecondsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeErroredSecondsCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeErroredSecondsCP_Object = MibTableColumn
xldv20pmThlFeErroredSecondsCP = _Xldv20pmThlFeErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 25),
    _Xldv20pmThlFeErroredSecondsCP_Type()
)
xldv20pmThlFeErroredSecondsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeErroredSecondsCP.setStatus("mandatory")


class _Xldv20pmThlFeErroredSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlFeErroredSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeErroredSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeErroredSecondsPLCP_Object = MibTableColumn
xldv20pmThlFeErroredSecondsPLCP = _Xldv20pmThlFeErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 26),
    _Xldv20pmThlFeErroredSecondsPLCP_Type()
)
xldv20pmThlFeErroredSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeErroredSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlFeSas_Type(Integer32):
    """Custom type xldv20pmThlFeSas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeSas_Type.__name__ = "Integer32"
_Xldv20pmThlFeSas_Object = MibTableColumn
xldv20pmThlFeSas = _Xldv20pmThlFeSas_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 27),
    _Xldv20pmThlFeSas_Type()
)
xldv20pmThlFeSas.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeSas.setStatus("mandatory")


class _Xldv20pmThlFeSeverelyErroredSeconds_Type(Integer32):
    """Custom type xldv20pmThlFeSeverelyErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeSeverelyErroredSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlFeSeverelyErroredSeconds_Object = MibTableColumn
xldv20pmThlFeSeverelyErroredSeconds = _Xldv20pmThlFeSeverelyErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 28),
    _Xldv20pmThlFeSeverelyErroredSeconds_Type()
)
xldv20pmThlFeSeverelyErroredSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeSeverelyErroredSeconds.setStatus("mandatory")


class _Xldv20pmThlFeSeverelyErroredSecondsCP_Type(Integer32):
    """Custom type xldv20pmThlFeSeverelyErroredSecondsCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeSeverelyErroredSecondsCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeSeverelyErroredSecondsCP_Object = MibTableColumn
xldv20pmThlFeSeverelyErroredSecondsCP = _Xldv20pmThlFeSeverelyErroredSecondsCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 29),
    _Xldv20pmThlFeSeverelyErroredSecondsCP_Type()
)
xldv20pmThlFeSeverelyErroredSecondsCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeSeverelyErroredSecondsCP.setStatus("mandatory")


class _Xldv20pmThlFeSeverelyErroredSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlFeSeverelyErroredSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeSeverelyErroredSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeSeverelyErroredSecondsPLCP_Object = MibTableColumn
xldv20pmThlFeSeverelyErroredSecondsPLCP = _Xldv20pmThlFeSeverelyErroredSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 30),
    _Xldv20pmThlFeSeverelyErroredSecondsPLCP_Type()
)
xldv20pmThlFeSeverelyErroredSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeSeverelyErroredSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlFeUnavailableSeconds_Type(Integer32):
    """Custom type xldv20pmThlFeUnavailableSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeUnavailableSeconds_Type.__name__ = "Integer32"
_Xldv20pmThlFeUnavailableSeconds_Object = MibTableColumn
xldv20pmThlFeUnavailableSeconds = _Xldv20pmThlFeUnavailableSeconds_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 31),
    _Xldv20pmThlFeUnavailableSeconds_Type()
)
xldv20pmThlFeUnavailableSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeUnavailableSeconds.setStatus("mandatory")


class _Xldv20pmThlFeUnavailableSecondsPLCP_Type(Integer32):
    """Custom type xldv20pmThlFeUnavailableSecondsPLCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_Xldv20pmThlFeUnavailableSecondsPLCP_Type.__name__ = "Integer32"
_Xldv20pmThlFeUnavailableSecondsPLCP_Object = MibTableColumn
xldv20pmThlFeUnavailableSecondsPLCP = _Xldv20pmThlFeUnavailableSecondsPLCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 32),
    _Xldv20pmThlFeUnavailableSecondsPLCP_Type()
)
xldv20pmThlFeUnavailableSecondsPLCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlFeUnavailableSecondsPLCP.setStatus("mandatory")


class _Xldv20pmThlDiscardedCells_Type(Integer32):
    """Custom type xldv20pmThlDiscardedCells based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlDiscardedCells_Type.__name__ = "Integer32"
_Xldv20pmThlDiscardedCells_Object = MibTableColumn
xldv20pmThlDiscardedCells = _Xldv20pmThlDiscardedCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 33),
    _Xldv20pmThlDiscardedCells_Type()
)
xldv20pmThlDiscardedCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlDiscardedCells.setStatus("mandatory")


class _Xldv20pmThlImaGroupUnavailSecs_Type(Integer32):
    """Custom type xldv20pmThlImaGroupUnavailSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaGroupUnavailSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaGroupUnavailSecs_Object = MibTableColumn
xldv20pmThlImaGroupUnavailSecs = _Xldv20pmThlImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 34),
    _Xldv20pmThlImaGroupUnavailSecs_Type()
)
xldv20pmThlImaGroupUnavailSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaGroupUnavailSecs.setStatus("mandatory")


class _Xldv20pmThlImaGroupNeNumFailures_Type(Integer32):
    """Custom type xldv20pmThlImaGroupNeNumFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaGroupNeNumFailures_Type.__name__ = "Integer32"
_Xldv20pmThlImaGroupNeNumFailures_Object = MibTableColumn
xldv20pmThlImaGroupNeNumFailures = _Xldv20pmThlImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 35),
    _Xldv20pmThlImaGroupNeNumFailures_Type()
)
xldv20pmThlImaGroupNeNumFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaGroupNeNumFailures.setStatus("mandatory")


class _Xldv20pmThlImaLinkImaViolations_Type(Integer32):
    """Custom type xldv20pmThlImaLinkImaViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkImaViolations_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkImaViolations_Object = MibTableColumn
xldv20pmThlImaLinkImaViolations = _Xldv20pmThlImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 36),
    _Xldv20pmThlImaLinkImaViolations_Type()
)
xldv20pmThlImaLinkImaViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkImaViolations.setStatus("mandatory")


class _Xldv20pmThlImaLinkOifAnomalies_Type(Integer32):
    """Custom type xldv20pmThlImaLinkOifAnomalies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkOifAnomalies_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkOifAnomalies_Object = MibTableColumn
xldv20pmThlImaLinkOifAnomalies = _Xldv20pmThlImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 37),
    _Xldv20pmThlImaLinkOifAnomalies_Type()
)
xldv20pmThlImaLinkOifAnomalies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkOifAnomalies.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeSevErroredSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeSevErroredSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeSevErroredSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeSevErroredSecs_Object = MibTableColumn
xldv20pmThlImaLinkNeSevErroredSecs = _Xldv20pmThlImaLinkNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 38),
    _Xldv20pmThlImaLinkNeSevErroredSecs_Type()
)
xldv20pmThlImaLinkNeSevErroredSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeSevErroredSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkFeSevErroredSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkFeSevErroredSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkFeSevErroredSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkFeSevErroredSecs_Object = MibTableColumn
xldv20pmThlImaLinkFeSevErroredSecs = _Xldv20pmThlImaLinkFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 39),
    _Xldv20pmThlImaLinkFeSevErroredSecs_Type()
)
xldv20pmThlImaLinkFeSevErroredSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkFeSevErroredSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeUnavailSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeUnavailSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeUnavailSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeUnavailSecs_Object = MibTableColumn
xldv20pmThlImaLinkNeUnavailSecs = _Xldv20pmThlImaLinkNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 40),
    _Xldv20pmThlImaLinkNeUnavailSecs_Type()
)
xldv20pmThlImaLinkNeUnavailSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeUnavailSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkFeUnavailSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkFeUnavailSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkFeUnavailSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkFeUnavailSecs_Object = MibTableColumn
xldv20pmThlImaLinkFeUnavailSecs = _Xldv20pmThlImaLinkFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 41),
    _Xldv20pmThlImaLinkFeUnavailSecs_Type()
)
xldv20pmThlImaLinkFeUnavailSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkFeUnavailSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeTxUnusableSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeTxUnusableSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeTxUnusableSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeTxUnusableSecs_Object = MibTableColumn
xldv20pmThlImaLinkNeTxUnusableSecs = _Xldv20pmThlImaLinkNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 42),
    _Xldv20pmThlImaLinkNeTxUnusableSecs_Type()
)
xldv20pmThlImaLinkNeTxUnusableSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeTxUnusableSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeRxUnusableSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeRxUnusableSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeRxUnusableSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeRxUnusableSecs_Object = MibTableColumn
xldv20pmThlImaLinkNeRxUnusableSecs = _Xldv20pmThlImaLinkNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 43),
    _Xldv20pmThlImaLinkNeRxUnusableSecs_Type()
)
xldv20pmThlImaLinkNeRxUnusableSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeRxUnusableSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkFeTxUnusableSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkFeTxUnusableSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkFeTxUnusableSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkFeTxUnusableSecs_Object = MibTableColumn
xldv20pmThlImaLinkFeTxUnusableSecs = _Xldv20pmThlImaLinkFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 44),
    _Xldv20pmThlImaLinkFeTxUnusableSecs_Type()
)
xldv20pmThlImaLinkFeTxUnusableSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkFeTxUnusableSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkFeRxUnusableSecs_Type(Integer32):
    """Custom type xldv20pmThlImaLinkFeRxUnusableSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkFeRxUnusableSecs_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkFeRxUnusableSecs_Object = MibTableColumn
xldv20pmThlImaLinkFeRxUnusableSecs = _Xldv20pmThlImaLinkFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 45),
    _Xldv20pmThlImaLinkFeRxUnusableSecs_Type()
)
xldv20pmThlImaLinkFeRxUnusableSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkFeRxUnusableSecs.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeTxNumFailures_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeTxNumFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeTxNumFailures_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeTxNumFailures_Object = MibTableColumn
xldv20pmThlImaLinkNeTxNumFailures = _Xldv20pmThlImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 46),
    _Xldv20pmThlImaLinkNeTxNumFailures_Type()
)
xldv20pmThlImaLinkNeTxNumFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeTxNumFailures.setStatus("mandatory")


class _Xldv20pmThlImaLinkNeRxNumFailures_Type(Integer32):
    """Custom type xldv20pmThlImaLinkNeRxNumFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Xldv20pmThlImaLinkNeRxNumFailures_Type.__name__ = "Integer32"
_Xldv20pmThlImaLinkNeRxNumFailures_Object = MibTableColumn
xldv20pmThlImaLinkNeRxNumFailures = _Xldv20pmThlImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 1, 1, 47),
    _Xldv20pmThlImaLinkNeRxNumFailures_Type()
)
xldv20pmThlImaLinkNeRxNumFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmThlImaLinkNeRxNumFailures.setStatus("mandatory")
_Xldv20pmAtmThresholdLimitTable_Object = MibTable
xldv20pmAtmThresholdLimitTable = _Xldv20pmAtmThresholdLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2)
)
if mibBuilder.loadTexts:
    xldv20pmAtmThresholdLimitTable.setStatus("mandatory")
_Xldv20pmAtmThresholdLimitEntry_Object = MibTableRow
xldv20pmAtmThresholdLimitEntry = _Xldv20pmAtmThresholdLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2, 1)
)
xldv20pmAtmThresholdLimitEntry.setIndexNames(
    (0, "XLDV20PM-MIB", "xldv20pmAtlThresholdLimitIndex"),
)
if mibBuilder.loadTexts:
    xldv20pmAtmThresholdLimitEntry.setStatus("mandatory")


class _Xldv20pmAtlThresholdLimitIndex_Type(Integer32):
    """Custom type xldv20pmAtlThresholdLimitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xldv20pmAtlThresholdLimitIndex_Type.__name__ = "Integer32"
_Xldv20pmAtlThresholdLimitIndex_Object = MibTableColumn
xldv20pmAtlThresholdLimitIndex = _Xldv20pmAtlThresholdLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2, 1, 1),
    _Xldv20pmAtlThresholdLimitIndex_Type()
)
xldv20pmAtlThresholdLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xldv20pmAtlThresholdLimitIndex.setStatus("mandatory")
_Xldv20pmAtlTransmittedUserCells_Type = Unsigned32
_Xldv20pmAtlTransmittedUserCells_Object = MibTableColumn
xldv20pmAtlTransmittedUserCells = _Xldv20pmAtlTransmittedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2, 1, 2),
    _Xldv20pmAtlTransmittedUserCells_Type()
)
xldv20pmAtlTransmittedUserCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAtlTransmittedUserCells.setStatus("mandatory")
_Xldv20pmAtlLostUserCells_Type = Unsigned32
_Xldv20pmAtlLostUserCells_Object = MibTableColumn
xldv20pmAtlLostUserCells = _Xldv20pmAtlLostUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2, 1, 3),
    _Xldv20pmAtlLostUserCells_Type()
)
xldv20pmAtlLostUserCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAtlLostUserCells.setStatus("mandatory")
_Xldv20pmAtlMisinsertedUserCells_Type = Unsigned32
_Xldv20pmAtlMisinsertedUserCells_Object = MibTableColumn
xldv20pmAtlMisinsertedUserCells = _Xldv20pmAtlMisinsertedUserCells_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 4, 2, 1, 4),
    _Xldv20pmAtlMisinsertedUserCells_Type()
)
xldv20pmAtlMisinsertedUserCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xldv20pmAtlMisinsertedUserCells.setStatus("mandatory")
_Xldv20pmTraps_ObjectIdentity = ObjectIdentity
xldv20pmTraps = _Xldv20pmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5)
)
_Xldv20pmTrapVars_ObjectIdentity = ObjectIdentity
xldv20pmTrapVars = _Xldv20pmTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1)
)
_Xldv20pmTvIfIndex_Type = Unsigned16
_Xldv20pmTvIfIndex_Object = MibScalar
xldv20pmTvIfIndex = _Xldv20pmTvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 1),
    _Xldv20pmTvIfIndex_Type()
)
xldv20pmTvIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvIfIndex.setStatus("mandatory")
_Xldv20pmTvPmType_Type = Xldv20pmType
_Xldv20pmTvPmType_Object = MibScalar
xldv20pmTvPmType = _Xldv20pmTvPmType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 2),
    _Xldv20pmTvPmType_Type()
)
xldv20pmTvPmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvPmType.setStatus("mandatory")
_Xldv20pmTvPmCounter_Type = Xldv20pmCounterName
_Xldv20pmTvPmCounter_Object = MibScalar
xldv20pmTvPmCounter = _Xldv20pmTvPmCounter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 3),
    _Xldv20pmTvPmCounter_Type()
)
xldv20pmTvPmCounter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvPmCounter.setStatus("mandatory")
_Xldv20pmTvCurrentCounterValue_Type = Counter32
_Xldv20pmTvCurrentCounterValue_Object = MibScalar
xldv20pmTvCurrentCounterValue = _Xldv20pmTvCurrentCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 4),
    _Xldv20pmTvCurrentCounterValue_Type()
)
xldv20pmTvCurrentCounterValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvCurrentCounterValue.setStatus("mandatory")
_Xldv20pmTvCurrentCounterLimit_Type = Counter32
_Xldv20pmTvCurrentCounterLimit_Object = MibScalar
xldv20pmTvCurrentCounterLimit = _Xldv20pmTvCurrentCounterLimit_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 5),
    _Xldv20pmTvCurrentCounterLimit_Type()
)
xldv20pmTvCurrentCounterLimit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvCurrentCounterLimit.setStatus("mandatory")
_Xldv20pmTvAtmPmCounter_Type = Xldv20pmAtmCounterType
_Xldv20pmTvAtmPmCounter_Object = MibScalar
xldv20pmTvAtmPmCounter = _Xldv20pmTvAtmPmCounter_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 6),
    _Xldv20pmTvAtmPmCounter_Type()
)
xldv20pmTvAtmPmCounter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvAtmPmCounter.setStatus("mandatory")
_Xldv20pmTvAtmObjectIndex_Type = Unsigned16
_Xldv20pmTvAtmObjectIndex_Object = MibScalar
xldv20pmTvAtmObjectIndex = _Xldv20pmTvAtmObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 7),
    _Xldv20pmTvAtmObjectIndex_Type()
)
xldv20pmTvAtmObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvAtmObjectIndex.setStatus("mandatory")
_Xldv20pmTvEndpointType_Type = Xldv20pmEndpointType
_Xldv20pmTvEndpointType_Object = MibScalar
xldv20pmTvEndpointType = _Xldv20pmTvEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 8),
    _Xldv20pmTvEndpointType_Type()
)
xldv20pmTvEndpointType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvEndpointType.setStatus("mandatory")
_Xldv20pmTvIntervalType_Type = Xldv20pmIntervalType
_Xldv20pmTvIntervalType_Object = MibScalar
xldv20pmTvIntervalType = _Xldv20pmTvIntervalType_Object(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 1, 9),
    _Xldv20pmTvIntervalType_Type()
)
xldv20pmTvIntervalType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xldv20pmTvIntervalType.setStatus("mandatory")
_Xldv20pmTrapTypes_ObjectIdentity = ObjectIdentity
xldv20pmTrapTypes = _Xldv20pmTrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 5, 5, 2)
)

# Managed Objects groups


# Notification objects

xldv20pmTrThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 200)
)
xldv20pmTrThresholdCrossingAlert.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvIfIndex"),
        ("XLDV20PM-MIB", "xldv20pmTvPmType"),
        ("XLDV20PM-MIB", "xldv20pmTvPmCounter"),
        ("XLDV20PM-MIB", "xldv20pmTvIntervalType"),
        ("XLDV20PM-MIB", "xldv20pmTvCurrentCounterValue"),
        ("XLDV20PM-MIB", "xldv20pmTvCurrentCounterLimit"))
)
if mibBuilder.loadTexts:
    xldv20pmTrThresholdCrossingAlert.setStatus(
        ""
    )

xldv20pmTrAtmThresholdCrossingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 300)
)
xldv20pmTrAtmThresholdCrossingAlert.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmObjectIndex"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmPmCounter"),
        ("XLDV20PM-MIB", "xldv20pmTvIntervalType"),
        ("XLDV20PM-MIB", "xldv20pmTvCurrentCounterValue"),
        ("XLDV20PM-MIB", "xldv20pmTvCurrentCounterLimit"))
)
if mibBuilder.loadTexts:
    xldv20pmTrAtmThresholdCrossingAlert.setStatus(
        ""
    )

xldv20pmTrAtmObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 302)
)
xldv20pmTrAtmObjectCreation.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmObjectIndex"))
)
if mibBuilder.loadTexts:
    xldv20pmTrAtmObjectCreation.setStatus(
        ""
    )

xldv20pmTrAtmObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 303)
)
xldv20pmTrAtmObjectDeletion.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmObjectIndex"))
)
if mibBuilder.loadTexts:
    xldv20pmTrAtmObjectDeletion.setStatus(
        ""
    )

xldv20pmTrAtmEndpointObjectCreation = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 304)
)
xldv20pmTrAtmEndpointObjectCreation.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmObjectIndex"),
        ("XLDV20PM-MIB", "xldv20pmTvEndpointType"))
)
if mibBuilder.loadTexts:
    xldv20pmTrAtmEndpointObjectCreation.setStatus(
        ""
    )

xldv20pmTrAtmEndpointObjectDeletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 7, 1, 2, 1, 1, 4, 10, 0, 305)
)
xldv20pmTrAtmEndpointObjectDeletion.setObjects(
      *(("XLDV20-MIB", "xldv20TvTimeAndDate"),
        ("XLDV20PM-MIB", "xldv20pmTvAtmObjectIndex"),
        ("XLDV20PM-MIB", "xldv20pmTvEndpointType"))
)
if mibBuilder.loadTexts:
    xldv20pmTrAtmEndpointObjectDeletion.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XLDV20PM-MIB",
    **{"Xldv20pmIntervalType": Xldv20pmIntervalType,
       "Xldv20pmControlReq": Xldv20pmControlReq,
       "Xldv20pmCounterName": Xldv20pmCounterName,
       "Xldv20pmType": Xldv20pmType,
       "Xldv20pmFlowType": Xldv20pmFlowType,
       "Xldv20pmSuspectType": Xldv20pmSuspectType,
       "Xldv20pmConnectionIndexType": Xldv20pmConnectionIndexType,
       "Xldv20pmRoleType": Xldv20pmRoleType,
       "Xldv20pmEndpointType": Xldv20pmEndpointType,
       "Xldv20pmBlockSizeType": Xldv20pmBlockSizeType,
       "Xldv20pmAtmCounterType": Xldv20pmAtmCounterType,
       "xldv20pmTrThresholdCrossingAlert": xldv20pmTrThresholdCrossingAlert,
       "xldv20pmTrAtmThresholdCrossingAlert": xldv20pmTrAtmThresholdCrossingAlert,
       "xldv20pmTrAtmObjectCreation": xldv20pmTrAtmObjectCreation,
       "xldv20pmTrAtmObjectDeletion": xldv20pmTrAtmObjectDeletion,
       "xldv20pmTrAtmEndpointObjectCreation": xldv20pmTrAtmEndpointObjectCreation,
       "xldv20pmTrAtmEndpointObjectDeletion": xldv20pmTrAtmEndpointObjectDeletion,
       "xldv20Pm": xldv20Pm,
       "xldv20pmPerformanceManagementControl": xldv20pmPerformanceManagementControl,
       "xldv20pmControl": xldv20pmControl,
       "xldv20pmCoIfIndex": xldv20pmCoIfIndex,
       "xldv20pmCoNrHistEntriesSize": xldv20pmCoNrHistEntriesSize,
       "xldv20pmCoIntervalType": xldv20pmCoIntervalType,
       "xldv20pmCoControlReq": xldv20pmCoControlReq,
       "xldv20pmCoControlStatus": xldv20pmCoControlStatus,
       "xldv20pmCoRemainingHistoryEntriesSize": xldv20pmCoRemainingHistoryEntriesSize,
       "xldv20pmCoOAMLevel": xldv20pmCoOAMLevel,
       "xldv20pmCoControlReqResult": xldv20pmCoControlReqResult,
       "xldv20pmCoControlTimeStamp": xldv20pmCoControlTimeStamp,
       "xldv20pmAtmControl": xldv20pmAtmControl,
       "xldv20pmAcoIndex": xldv20pmAcoIndex,
       "xldv20pmAcoNrHistEntriesSize": xldv20pmAcoNrHistEntriesSize,
       "xldv20pmAcoIntervalType": xldv20pmAcoIntervalType,
       "xldv20pmAcoControlReq": xldv20pmAcoControlReq,
       "xldv20pmAcoControlStatus": xldv20pmAcoControlStatus,
       "xldv20pmAcoRemainingHistoryEntriesSize": xldv20pmAcoRemainingHistoryEntriesSize,
       "xldv20pmAcoFlowType": xldv20pmAcoFlowType,
       "xldv20pmAcoFlowDirection": xldv20pmAcoFlowDirection,
       "xldv20pmAcoConnectionIndex": xldv20pmAcoConnectionIndex,
       "xldv20pmAcoConnectionIndexType": xldv20pmAcoConnectionIndexType,
       "xldv20pmAcoRole": xldv20pmAcoRole,
       "xldv20pmAcoEndpointType": xldv20pmAcoEndpointType,
       "xldv20pmAcoControlReqResult": xldv20pmAcoControlReqResult,
       "xldv20pmAcoControlTimeStamp": xldv20pmAcoControlTimeStamp,
       "xldv20pmPerformanceMonitoring": xldv20pmPerformanceMonitoring,
       "xldv20pmCommonCurrentTable": xldv20pmCommonCurrentTable,
       "xldv20pmCommonCurrentEntry": xldv20pmCommonCurrentEntry,
       "xldv20pmCcIntervalType": xldv20pmCcIntervalType,
       "xldv20pmCcOAMLevel": xldv20pmCcOAMLevel,
       "xldv20pmCcAdminState": xldv20pmCcAdminState,
       "xldv20pmCcSuspectFlag": xldv20pmCcSuspectFlag,
       "xldv20pmCcHistEntrySize": xldv20pmCcHistEntrySize,
       "xldv20pmCcNrHistEntriesAvailable": xldv20pmCcNrHistEntriesAvailable,
       "xldv20pmCcElapsedTime": xldv20pmCcElapsedTime,
       "xldv20pmCcThresholdLimitIndex": xldv20pmCcThresholdLimitIndex,
       "xldv20pmCcNeErroredSeconds": xldv20pmCcNeErroredSeconds,
       "xldv20pmCcFeErroredSeconds": xldv20pmCcFeErroredSeconds,
       "xldv20pmCcNeSeverelyErroredSeconds": xldv20pmCcNeSeverelyErroredSeconds,
       "xldv20pmCcFeSeverelyErroredSeconds": xldv20pmCcFeSeverelyErroredSeconds,
       "xldv20pmCcNeBackgroundBlockErrors": xldv20pmCcNeBackgroundBlockErrors,
       "xldv20pmCcFeBackgroundBlockErrors": xldv20pmCcFeBackgroundBlockErrors,
       "xldv20pmCcNeUnavailableSeconds": xldv20pmCcNeUnavailableSeconds,
       "xldv20pmCcFeUnavailableSeconds": xldv20pmCcFeUnavailableSeconds,
       "xldv20pmCommonHistoryTable": xldv20pmCommonHistoryTable,
       "xldv20pmCommonHistoryEntry": xldv20pmCommonHistoryEntry,
       "xldv20pmChIntervalType": xldv20pmChIntervalType,
       "xldv20pmChOAMLevel": xldv20pmChOAMLevel,
       "xldv20pmChHistEntryNr": xldv20pmChHistEntryNr,
       "xldv20pmChSuspectFlag": xldv20pmChSuspectFlag,
       "xldv20pmChPeriodEndTime": xldv20pmChPeriodEndTime,
       "xldv20pmChNeErroredSeconds": xldv20pmChNeErroredSeconds,
       "xldv20pmChFeErroredSeconds": xldv20pmChFeErroredSeconds,
       "xldv20pmChNeSeverelyErroredSeconds": xldv20pmChNeSeverelyErroredSeconds,
       "xldv20pmChFeSeverelyErroredSeconds": xldv20pmChFeSeverelyErroredSeconds,
       "xldv20pmChNeBackgroundBlockErrors": xldv20pmChNeBackgroundBlockErrors,
       "xldv20pmChFeBackgroundBlockErrors": xldv20pmChFeBackgroundBlockErrors,
       "xldv20pmChNeUnavailableSeconds": xldv20pmChNeUnavailableSeconds,
       "xldv20pmChFeUnavailableSeconds": xldv20pmChFeUnavailableSeconds,
       "xldv20pmS3CurrentTable": xldv20pmS3CurrentTable,
       "xldv20pmS3CurrentEntry": xldv20pmS3CurrentEntry,
       "xldv20pmS3cIntervalType": xldv20pmS3cIntervalType,
       "xldv20pmS3cOAMLevel": xldv20pmS3cOAMLevel,
       "xldv20pmS3cAdminState": xldv20pmS3cAdminState,
       "xldv20pmS3cSuspectFlag": xldv20pmS3cSuspectFlag,
       "xldv20pmS3cHistEntrySize": xldv20pmS3cHistEntrySize,
       "xldv20pmS3cNrHistEntriesAvailable": xldv20pmS3cNrHistEntriesAvailable,
       "xldv20pmS3cElapsedTime": xldv20pmS3cElapsedTime,
       "xldv20pmS3cThresholdLimitIndex": xldv20pmS3cThresholdLimitIndex,
       "xldv20pmS3cNeErroredSeconds": xldv20pmS3cNeErroredSeconds,
       "xldv20pmS3cFeErroredSeconds": xldv20pmS3cFeErroredSeconds,
       "xldv20pmS3cNeSeverelyErroredSeconds": xldv20pmS3cNeSeverelyErroredSeconds,
       "xldv20pmS3cFeSeverelyErroredSeconds": xldv20pmS3cFeSeverelyErroredSeconds,
       "xldv20pmS3cNeCodeViolations": xldv20pmS3cNeCodeViolations,
       "xldv20pmS3cFeCodeViolations": xldv20pmS3cFeCodeViolations,
       "xldv20pmS3cNeUnavailableSeconds": xldv20pmS3cNeUnavailableSeconds,
       "xldv20pmS3cFeUnavailableSeconds": xldv20pmS3cFeUnavailableSeconds,
       "xldv20pmS3cNeSeverelyErroredFrameSeconds": xldv20pmS3cNeSeverelyErroredFrameSeconds,
       "xldv20pmS3HistoryTable": xldv20pmS3HistoryTable,
       "xldv20pmS3HistoryEntry": xldv20pmS3HistoryEntry,
       "xldv20pmS3hIntervalType": xldv20pmS3hIntervalType,
       "xldv20pmS3hOAMLevel": xldv20pmS3hOAMLevel,
       "xldv20pmS3hHistEntryNr": xldv20pmS3hHistEntryNr,
       "xldv20pmS3hSuspectFlag": xldv20pmS3hSuspectFlag,
       "xldv20pmS3hPeriodEndTime": xldv20pmS3hPeriodEndTime,
       "xldv20pmS3hNeErroredSeconds": xldv20pmS3hNeErroredSeconds,
       "xldv20pmS3hFeErroredSeconds": xldv20pmS3hFeErroredSeconds,
       "xldv20pmS3hNeSeverelyErroredSeconds": xldv20pmS3hNeSeverelyErroredSeconds,
       "xldv20pmS3hFeSeverelyErroredSeconds": xldv20pmS3hFeSeverelyErroredSeconds,
       "xldv20pmS3hNeCodeViolations": xldv20pmS3hNeCodeViolations,
       "xldv20pmS3hFeCodeViolations": xldv20pmS3hFeCodeViolations,
       "xldv20pmS3hNeUnavailableSeconds": xldv20pmS3hNeUnavailableSeconds,
       "xldv20pmS3hFeUnavailableSeconds": xldv20pmS3hFeUnavailableSeconds,
       "xldv20pmS3hNeSeverelyErroredFrameSeconds": xldv20pmS3hNeSeverelyErroredFrameSeconds,
       "xldv20pmD3CurrentTable": xldv20pmD3CurrentTable,
       "xldv20pmD3CurrentEntry": xldv20pmD3CurrentEntry,
       "xldv20pmD3cIntervalType": xldv20pmD3cIntervalType,
       "xldv20pmD3cOAMLevel": xldv20pmD3cOAMLevel,
       "xldv20pmD3cAdminState": xldv20pmD3cAdminState,
       "xldv20pmD3cSuspectFlag": xldv20pmD3cSuspectFlag,
       "xldv20pmD3cHistEntrySize": xldv20pmD3cHistEntrySize,
       "xldv20pmD3cNrHistEntriesAvailable": xldv20pmD3cNrHistEntriesAvailable,
       "xldv20pmD3cElapsedTime": xldv20pmD3cElapsedTime,
       "xldv20pmD3cThresholdLimitIndex": xldv20pmD3cThresholdLimitIndex,
       "xldv20pmD3cNeErroredSecondsCP": xldv20pmD3cNeErroredSecondsCP,
       "xldv20pmD3cFeErroredSecondsCP": xldv20pmD3cFeErroredSecondsCP,
       "xldv20pmD3cNeErroredSecondsPLCP": xldv20pmD3cNeErroredSecondsPLCP,
       "xldv20pmD3cFeErroredSecondsPLCP": xldv20pmD3cFeErroredSecondsPLCP,
       "xldv20pmD3cNeSeverelyErroredSecondsCP": xldv20pmD3cNeSeverelyErroredSecondsCP,
       "xldv20pmD3cFeSeverelyErroredSecondsCP": xldv20pmD3cFeSeverelyErroredSecondsCP,
       "xldv20pmD3cNeSeverelyErroredSecondsPLCP": xldv20pmD3cNeSeverelyErroredSecondsPLCP,
       "xldv20pmD3cFeSeverelyErroredSecondsPLCP": xldv20pmD3cFeSeverelyErroredSecondsPLCP,
       "xldv20pmD3cNeCodeViolationsP": xldv20pmD3cNeCodeViolationsP,
       "xldv20pmD3cNeCodeViolationsCP": xldv20pmD3cNeCodeViolationsCP,
       "xldv20pmD3cFeCodeViolationsCP": xldv20pmD3cFeCodeViolationsCP,
       "xldv20pmD3cNeCodeViolationsPLCP": xldv20pmD3cNeCodeViolationsPLCP,
       "xldv20pmD3cFeCodeViolationsPLCP": xldv20pmD3cFeCodeViolationsPLCP,
       "xldv20pmD3cNeUnavailableSeconds": xldv20pmD3cNeUnavailableSeconds,
       "xldv20pmD3cFeUnavailableSeconds": xldv20pmD3cFeUnavailableSeconds,
       "xldv20pmD3cNeUnavailableSecondsPLCP": xldv20pmD3cNeUnavailableSecondsPLCP,
       "xldv20pmD3cFeUnavailableSecondsPLCP": xldv20pmD3cFeUnavailableSecondsPLCP,
       "xldv20pmD3cNeSas": xldv20pmD3cNeSas,
       "xldv20pmD3cFeSas": xldv20pmD3cFeSas,
       "xldv20pmD3HistoryTable": xldv20pmD3HistoryTable,
       "xldv20pmD3HistoryEntry": xldv20pmD3HistoryEntry,
       "xldv20pmD3hIntervalType": xldv20pmD3hIntervalType,
       "xldv20pmD3hOAMLevel": xldv20pmD3hOAMLevel,
       "xldv20pmD3hHistEntryNr": xldv20pmD3hHistEntryNr,
       "xldv20pmD3hSuspectFlag": xldv20pmD3hSuspectFlag,
       "xldv20pmD3hPeriodEndTime": xldv20pmD3hPeriodEndTime,
       "xldv20pmD3hNeErroredSecondsCP": xldv20pmD3hNeErroredSecondsCP,
       "xldv20pmD3hFeErroredSecondsCP": xldv20pmD3hFeErroredSecondsCP,
       "xldv20pmD3hNeErroredSecondsPLCP": xldv20pmD3hNeErroredSecondsPLCP,
       "xldv20pmD3hFeErroredSecondsPLCP": xldv20pmD3hFeErroredSecondsPLCP,
       "xldv20pmD3hNeSeverelyErroredSecondsCP": xldv20pmD3hNeSeverelyErroredSecondsCP,
       "xldv20pmD3hFeSeverelyErroredSecondsCP": xldv20pmD3hFeSeverelyErroredSecondsCP,
       "xldv20pmD3hNeSeverelyErroredSecondsPLCP": xldv20pmD3hNeSeverelyErroredSecondsPLCP,
       "xldv20pmD3hFeSeverelyErroredSecondsPLCP": xldv20pmD3hFeSeverelyErroredSecondsPLCP,
       "xldv20pmD3hNeCodeViolationsP": xldv20pmD3hNeCodeViolationsP,
       "xldv20pmD3hNeCodeViolationsCP": xldv20pmD3hNeCodeViolationsCP,
       "xldv20pmD3hFeCodeViolationsCP": xldv20pmD3hFeCodeViolationsCP,
       "xldv20pmD3hNeCodeViolationsPLCP": xldv20pmD3hNeCodeViolationsPLCP,
       "xldv20pmD3hFeCodeViolationsPLCP": xldv20pmD3hFeCodeViolationsPLCP,
       "xldv20pmD3hNeUnavailableSeconds": xldv20pmD3hNeUnavailableSeconds,
       "xldv20pmD3hFeUnavailableSeconds": xldv20pmD3hFeUnavailableSeconds,
       "xldv20pmD3hNeUnavailableSecondsPLCP": xldv20pmD3hNeUnavailableSecondsPLCP,
       "xldv20pmD3hFeUnavailableSecondsPLCP": xldv20pmD3hFeUnavailableSecondsPLCP,
       "xldv20pmD3hNeSas": xldv20pmD3hNeSas,
       "xldv20pmD3hFeSas": xldv20pmD3hFeSas,
       "xldv20pmS1CurrentTable": xldv20pmS1CurrentTable,
       "xldv20pmS1CurrentEntry": xldv20pmS1CurrentEntry,
       "xldv20pmS1cIntervalType": xldv20pmS1cIntervalType,
       "xldv20pmS1cOAMLevel": xldv20pmS1cOAMLevel,
       "xldv20pmS1cAdminState": xldv20pmS1cAdminState,
       "xldv20pmS1cSuspectFlag": xldv20pmS1cSuspectFlag,
       "xldv20pmS1cHistEntrySize": xldv20pmS1cHistEntrySize,
       "xldv20pmS1cNrHistEntriesAvailable": xldv20pmS1cNrHistEntriesAvailable,
       "xldv20pmS1cElapsedTime": xldv20pmS1cElapsedTime,
       "xldv20pmS1cThresholdLimitIndex": xldv20pmS1cThresholdLimitIndex,
       "xldv20pmS1cNeErroredSeconds": xldv20pmS1cNeErroredSeconds,
       "xldv20pmS1cFeErroredSeconds": xldv20pmS1cFeErroredSeconds,
       "xldv20pmS1cNeSeverelyErroredSeconds": xldv20pmS1cNeSeverelyErroredSeconds,
       "xldv20pmS1cFeSeverelyErroredSeconds": xldv20pmS1cFeSeverelyErroredSeconds,
       "xldv20pmS1cNeBackgroundBlockErrors": xldv20pmS1cNeBackgroundBlockErrors,
       "xldv20pmS1cFeBackgroundBlockErrors": xldv20pmS1cFeBackgroundBlockErrors,
       "xldv20pmS1cNeUnavailableSeconds": xldv20pmS1cNeUnavailableSeconds,
       "xldv20pmS1cFeUnavailableSeconds": xldv20pmS1cFeUnavailableSeconds,
       "xldv20pmS1cNeOfsSeconds": xldv20pmS1cNeOfsSeconds,
       "xldv20pmS1cNeAisSeconds": xldv20pmS1cNeAisSeconds,
       "xldv20pmS1cNeLosSeconds": xldv20pmS1cNeLosSeconds,
       "xldv20pmS1HistoryTable": xldv20pmS1HistoryTable,
       "xldv20pmS1HistoryEntry": xldv20pmS1HistoryEntry,
       "xldv20pmS1hIntervalType": xldv20pmS1hIntervalType,
       "xldv20pmS1hOAMLevel": xldv20pmS1hOAMLevel,
       "xldv20pmS1hHistEntryNr": xldv20pmS1hHistEntryNr,
       "xldv20pmS1hSuspectFlag": xldv20pmS1hSuspectFlag,
       "xldv20pmS1hPeriodEndTime": xldv20pmS1hPeriodEndTime,
       "xldv20pmS1hNeErroredSeconds": xldv20pmS1hNeErroredSeconds,
       "xldv20pmS1hFeErroredSeconds": xldv20pmS1hFeErroredSeconds,
       "xldv20pmS1hNeSeverelyErroredSeconds": xldv20pmS1hNeSeverelyErroredSeconds,
       "xldv20pmS1hFeSeverelyErroredSeconds": xldv20pmS1hFeSeverelyErroredSeconds,
       "xldv20pmS1hNeBackgroundBlockErrors": xldv20pmS1hNeBackgroundBlockErrors,
       "xldv20pmS1hFeBackgroundBlockErrors": xldv20pmS1hFeBackgroundBlockErrors,
       "xldv20pmS1hNeUnavailableSeconds": xldv20pmS1hNeUnavailableSeconds,
       "xldv20pmS1hFeUnavailableSeconds": xldv20pmS1hFeUnavailableSeconds,
       "xldv20pmS1hNeOfsSeconds": xldv20pmS1hNeOfsSeconds,
       "xldv20pmS1hNeAisSeconds": xldv20pmS1hNeAisSeconds,
       "xldv20pmS1hNeLosSeconds": xldv20pmS1hNeLosSeconds,
       "xldv20pmAtmObjectsTable": xldv20pmAtmObjectsTable,
       "xldv20pmAtmObjectsEntry": xldv20pmAtmObjectsEntry,
       "xldv20pmAoIndex": xldv20pmAoIndex,
       "xldv20pmAoFlowType": xldv20pmAoFlowType,
       "xldv20pmAoAdminState": xldv20pmAoAdminState,
       "xldv20pmAoBlockSize": xldv20pmAoBlockSize,
       "xldv20pmAtmEndpointsTable": xldv20pmAtmEndpointsTable,
       "xldv20pmAtmEndpointsEntry": xldv20pmAtmEndpointsEntry,
       "xldv20pmAeEndpointType": xldv20pmAeEndpointType,
       "xldv20pmAeConnectionIndex": xldv20pmAeConnectionIndex,
       "xldv20pmAeConnectionIndexType": xldv20pmAeConnectionIndexType,
       "xldv20pmAeRole": xldv20pmAeRole,
       "xldv20pmAeFlowDirection": xldv20pmAeFlowDirection,
       "xldv20pmAtmCurrentTable": xldv20pmAtmCurrentTable,
       "xldv20pmAtmCurrentEntry": xldv20pmAtmCurrentEntry,
       "xldv20pmAcIntervalType": xldv20pmAcIntervalType,
       "xldv20pmAcAdminState": xldv20pmAcAdminState,
       "xldv20pmAcSuspectFlag": xldv20pmAcSuspectFlag,
       "xldv20pmAcHistEntrySize": xldv20pmAcHistEntrySize,
       "xldv20pmAcNrHistEntriesAvailable": xldv20pmAcNrHistEntriesAvailable,
       "xldv20pmAcElapsedTime": xldv20pmAcElapsedTime,
       "xldv20pmAcThresholdLimitIndex": xldv20pmAcThresholdLimitIndex,
       "xldv20pmAcTransmittedUserCells": xldv20pmAcTransmittedUserCells,
       "xldv20pmAcLostUserCells": xldv20pmAcLostUserCells,
       "xldv20pmAcMisinsertedUserCells": xldv20pmAcMisinsertedUserCells,
       "xldv20pmAtmHistoryTable": xldv20pmAtmHistoryTable,
       "xldv20pmAtmHistoryEntry": xldv20pmAtmHistoryEntry,
       "xldv20pmAhIntervalType": xldv20pmAhIntervalType,
       "xldv20pmAhHistEntryNr": xldv20pmAhHistEntryNr,
       "xldv20pmAhSuspectFlag": xldv20pmAhSuspectFlag,
       "xldv20pmAhPeriodEndTime": xldv20pmAhPeriodEndTime,
       "xldv20pmAhTransmittedUserCells": xldv20pmAhTransmittedUserCells,
       "xldv20pmAhLostUserCells": xldv20pmAhLostUserCells,
       "xldv20pmAhMisinsertedUserCells": xldv20pmAhMisinsertedUserCells,
       "xldv20pmImaGroupCurrentTable": xldv20pmImaGroupCurrentTable,
       "xldv20pmImaGroupCurrentEntry": xldv20pmImaGroupCurrentEntry,
       "xldv20pmImaGroupCurrentIntervalType": xldv20pmImaGroupCurrentIntervalType,
       "xldv20pmImaGroupCurrentAdminState": xldv20pmImaGroupCurrentAdminState,
       "xldv20pmImaGroupCurrentSuspectFlag": xldv20pmImaGroupCurrentSuspectFlag,
       "xldv20pmImaGroupCurrentHistEntrySize": xldv20pmImaGroupCurrentHistEntrySize,
       "xldv20pmImaGroupCurrentNrHistEntriesAvailable": xldv20pmImaGroupCurrentNrHistEntriesAvailable,
       "xldv20pmImaGroupCurrentElapsedTime": xldv20pmImaGroupCurrentElapsedTime,
       "xldv20pmImaGroupCurrentThresholdLimitIndex": xldv20pmImaGroupCurrentThresholdLimitIndex,
       "xldv20pmImaGroupCurrentUnavailSecs": xldv20pmImaGroupCurrentUnavailSecs,
       "xldv20pmImaGroupCurrentNeNumFailures": xldv20pmImaGroupCurrentNeNumFailures,
       "xldv20pmImaGroupHistoryTable": xldv20pmImaGroupHistoryTable,
       "xldv20pmImaGroupHistoryEntry": xldv20pmImaGroupHistoryEntry,
       "xldv20pmImaGroupHistoryIntervalType": xldv20pmImaGroupHistoryIntervalType,
       "xldv20pmImaGroupHistoryHistEntryNr": xldv20pmImaGroupHistoryHistEntryNr,
       "xldv20pmImaGroupHistorySuspectFlag": xldv20pmImaGroupHistorySuspectFlag,
       "xldv20pmImaGroupHistoryPeriodEndTime": xldv20pmImaGroupHistoryPeriodEndTime,
       "xldv20pmImaGroupHistoryUnavailSecs": xldv20pmImaGroupHistoryUnavailSecs,
       "xldv20pmImaGroupHistoryNeNumFailures": xldv20pmImaGroupHistoryNeNumFailures,
       "xldv20pmImaLinkCurrentTable": xldv20pmImaLinkCurrentTable,
       "xldv20pmImaLinkCurrentEntry": xldv20pmImaLinkCurrentEntry,
       "xldv20pmImaLinkCurrentIntervalType": xldv20pmImaLinkCurrentIntervalType,
       "xldv20pmImaLinkCurrentAdminState": xldv20pmImaLinkCurrentAdminState,
       "xldv20pmImaLinkCurrentSuspectFlag": xldv20pmImaLinkCurrentSuspectFlag,
       "xldv20pmImaLinkCurrentHistEntrySize": xldv20pmImaLinkCurrentHistEntrySize,
       "xldv20pmImaLinkCurrentNrHistEntriesAvailable": xldv20pmImaLinkCurrentNrHistEntriesAvailable,
       "xldv20pmImaLinkCurrentElapsedTime": xldv20pmImaLinkCurrentElapsedTime,
       "xldv20pmImaLinkCurrentThresholdLimitIndex": xldv20pmImaLinkCurrentThresholdLimitIndex,
       "xldv20pmImaLinkCurrentImaViolations": xldv20pmImaLinkCurrentImaViolations,
       "xldv20pmImaLinkCurrentOifAnomalies": xldv20pmImaLinkCurrentOifAnomalies,
       "xldv20pmImaLinkCurrentNeSevErroredSecs": xldv20pmImaLinkCurrentNeSevErroredSecs,
       "xldv20pmImaLinkCurrentFeSevErroredSecs": xldv20pmImaLinkCurrentFeSevErroredSecs,
       "xldv20pmImaLinkCurrentNeUnavailSecs": xldv20pmImaLinkCurrentNeUnavailSecs,
       "xldv20pmImaLinkCurrentFeUnavailSecs": xldv20pmImaLinkCurrentFeUnavailSecs,
       "xldv20pmImaLinkCurrentNeTxUnusableSecs": xldv20pmImaLinkCurrentNeTxUnusableSecs,
       "xldv20pmImaLinkCurrentNeRxUnusableSecs": xldv20pmImaLinkCurrentNeRxUnusableSecs,
       "xldv20pmImaLinkCurrentFeTxUnusableSecs": xldv20pmImaLinkCurrentFeTxUnusableSecs,
       "xldv20pmImaLinkCurrentFeRxUnusableSecs": xldv20pmImaLinkCurrentFeRxUnusableSecs,
       "xldv20pmImaLinkCurrentNeTxNumFailures": xldv20pmImaLinkCurrentNeTxNumFailures,
       "xldv20pmImaLinkCurrentNeRxNumFailures": xldv20pmImaLinkCurrentNeRxNumFailures,
       "xldv20pmImaLinkHistoryTable": xldv20pmImaLinkHistoryTable,
       "xldv20pmImaLinkHistoryEntry": xldv20pmImaLinkHistoryEntry,
       "xldv20pmImaLinkHistoryIntervalType": xldv20pmImaLinkHistoryIntervalType,
       "xldv20pmImaLinkHistoryHistEntryNr": xldv20pmImaLinkHistoryHistEntryNr,
       "xldv20pmImaLinkHistorySuspectFlag": xldv20pmImaLinkHistorySuspectFlag,
       "xldv20pmImaLinkHistoryPeriodEndTime": xldv20pmImaLinkHistoryPeriodEndTime,
       "xldv20pmImaLinkHistoryImaViolations": xldv20pmImaLinkHistoryImaViolations,
       "xldv20pmImaLinkHistoryOifAnomalies": xldv20pmImaLinkHistoryOifAnomalies,
       "xldv20pmImaLinkHistoryNeSevErroredSecs": xldv20pmImaLinkHistoryNeSevErroredSecs,
       "xldv20pmImaLinkHistoryFeSevErroredSecs": xldv20pmImaLinkHistoryFeSevErroredSecs,
       "xldv20pmImaLinkHistoryNeUnavailSecs": xldv20pmImaLinkHistoryNeUnavailSecs,
       "xldv20pmImaLinkHistoryFeUnavailSecs": xldv20pmImaLinkHistoryFeUnavailSecs,
       "xldv20pmImaLinkHistoryNeTxUnusableSecs": xldv20pmImaLinkHistoryNeTxUnusableSecs,
       "xldv20pmImaLinkHistoryNeRxUnusableSecs": xldv20pmImaLinkHistoryNeRxUnusableSecs,
       "xldv20pmImaLinkHistoryFeTxUnusableSecs": xldv20pmImaLinkHistoryFeTxUnusableSecs,
       "xldv20pmImaLinkHistoryFeRxUnusableSecs": xldv20pmImaLinkHistoryFeRxUnusableSecs,
       "xldv20pmImaLinkHistoryNeTxNumFailures": xldv20pmImaLinkHistoryNeTxNumFailures,
       "xldv20pmImaLinkHistoryNeRxNumFailures": xldv20pmImaLinkHistoryNeRxNumFailures,
       "xldv20pmProtocolMonitoring": xldv20pmProtocolMonitoring,
       "xldv20pmTcaPrMCurrentTable": xldv20pmTcaPrMCurrentTable,
       "xldv20pmTcaPrMCurrentEntry": xldv20pmTcaPrMCurrentEntry,
       "xldv20pmTcIntervalType": xldv20pmTcIntervalType,
       "xldv20pmTcAdminState": xldv20pmTcAdminState,
       "xldv20pmTcSuspectFlag": xldv20pmTcSuspectFlag,
       "xldv20pmTcHistEntrySize": xldv20pmTcHistEntrySize,
       "xldv20pmTcNrHistEntriesAvailable": xldv20pmTcNrHistEntriesAvailable,
       "xldv20pmTcElapsedTime": xldv20pmTcElapsedTime,
       "xldv20pmTcThresholdLimitIndex": xldv20pmTcThresholdLimitIndex,
       "xldv20pmTcDiscardedCells": xldv20pmTcDiscardedCells,
       "xldv20pmTcaPrMHistoryTable": xldv20pmTcaPrMHistoryTable,
       "xldv20pmTcaPrMHistoryEntry": xldv20pmTcaPrMHistoryEntry,
       "xldv20pmThIntervalType": xldv20pmThIntervalType,
       "xldv20pmThHistEntryNr": xldv20pmThHistEntryNr,
       "xldv20pmThSuspectFlag": xldv20pmThSuspectFlag,
       "xldv20pmThPeriodEndTime": xldv20pmThPeriodEndTime,
       "xldv20pmThDiscardedCells": xldv20pmThDiscardedCells,
       "xldv20pmThresholding": xldv20pmThresholding,
       "xldv20pmThresholdLimitTable": xldv20pmThresholdLimitTable,
       "xldv20pmThresholdLimitEntry": xldv20pmThresholdLimitEntry,
       "xldv20pmThlThresholdLimitIndex": xldv20pmThlThresholdLimitIndex,
       "xldv20pmThlNeBackgroundBlockErrors": xldv20pmThlNeBackgroundBlockErrors,
       "xldv20pmThlNeCodeViolations": xldv20pmThlNeCodeViolations,
       "xldv20pmThlNeCodeViolationsCP": xldv20pmThlNeCodeViolationsCP,
       "xldv20pmThlNeCodeViolationsP": xldv20pmThlNeCodeViolationsP,
       "xldv20pmThlNeCodeViolationsPLCP": xldv20pmThlNeCodeViolationsPLCP,
       "xldv20pmThlNeErroredSeconds": xldv20pmThlNeErroredSeconds,
       "xldv20pmThlNeErroredSecondsCP": xldv20pmThlNeErroredSecondsCP,
       "xldv20pmThlNeErroredSecondsPLCP": xldv20pmThlNeErroredSecondsPLCP,
       "xldv20pmThlNeSas": xldv20pmThlNeSas,
       "xldv20pmThlNeSeverelyErroredFrameSeconds": xldv20pmThlNeSeverelyErroredFrameSeconds,
       "xldv20pmThlNeSeverelyErroredSeconds": xldv20pmThlNeSeverelyErroredSeconds,
       "xldv20pmThlNeSeverelyErroredSecondsCP": xldv20pmThlNeSeverelyErroredSecondsCP,
       "xldv20pmThlNeSeverelyErroredSecondsPLCP": xldv20pmThlNeSeverelyErroredSecondsPLCP,
       "xldv20pmThlNeUnavailableSeconds": xldv20pmThlNeUnavailableSeconds,
       "xldv20pmThlNeUnavailableSecondsPLCP": xldv20pmThlNeUnavailableSecondsPLCP,
       "xldv20pmThlNeAisSeconds": xldv20pmThlNeAisSeconds,
       "xldv20pmThlNeOfsSeconds": xldv20pmThlNeOfsSeconds,
       "xldv20pmThlNeLosSeconds": xldv20pmThlNeLosSeconds,
       "xldv20pmThlFeBackgroundBlockErrors": xldv20pmThlFeBackgroundBlockErrors,
       "xldv20pmThlFeCodeViolations": xldv20pmThlFeCodeViolations,
       "xldv20pmThlFeCodeViolationsCP": xldv20pmThlFeCodeViolationsCP,
       "xldv20pmThlFeCodeViolationsPLCP": xldv20pmThlFeCodeViolationsPLCP,
       "xldv20pmThlFeErroredSeconds": xldv20pmThlFeErroredSeconds,
       "xldv20pmThlFeErroredSecondsCP": xldv20pmThlFeErroredSecondsCP,
       "xldv20pmThlFeErroredSecondsPLCP": xldv20pmThlFeErroredSecondsPLCP,
       "xldv20pmThlFeSas": xldv20pmThlFeSas,
       "xldv20pmThlFeSeverelyErroredSeconds": xldv20pmThlFeSeverelyErroredSeconds,
       "xldv20pmThlFeSeverelyErroredSecondsCP": xldv20pmThlFeSeverelyErroredSecondsCP,
       "xldv20pmThlFeSeverelyErroredSecondsPLCP": xldv20pmThlFeSeverelyErroredSecondsPLCP,
       "xldv20pmThlFeUnavailableSeconds": xldv20pmThlFeUnavailableSeconds,
       "xldv20pmThlFeUnavailableSecondsPLCP": xldv20pmThlFeUnavailableSecondsPLCP,
       "xldv20pmThlDiscardedCells": xldv20pmThlDiscardedCells,
       "xldv20pmThlImaGroupUnavailSecs": xldv20pmThlImaGroupUnavailSecs,
       "xldv20pmThlImaGroupNeNumFailures": xldv20pmThlImaGroupNeNumFailures,
       "xldv20pmThlImaLinkImaViolations": xldv20pmThlImaLinkImaViolations,
       "xldv20pmThlImaLinkOifAnomalies": xldv20pmThlImaLinkOifAnomalies,
       "xldv20pmThlImaLinkNeSevErroredSecs": xldv20pmThlImaLinkNeSevErroredSecs,
       "xldv20pmThlImaLinkFeSevErroredSecs": xldv20pmThlImaLinkFeSevErroredSecs,
       "xldv20pmThlImaLinkNeUnavailSecs": xldv20pmThlImaLinkNeUnavailSecs,
       "xldv20pmThlImaLinkFeUnavailSecs": xldv20pmThlImaLinkFeUnavailSecs,
       "xldv20pmThlImaLinkNeTxUnusableSecs": xldv20pmThlImaLinkNeTxUnusableSecs,
       "xldv20pmThlImaLinkNeRxUnusableSecs": xldv20pmThlImaLinkNeRxUnusableSecs,
       "xldv20pmThlImaLinkFeTxUnusableSecs": xldv20pmThlImaLinkFeTxUnusableSecs,
       "xldv20pmThlImaLinkFeRxUnusableSecs": xldv20pmThlImaLinkFeRxUnusableSecs,
       "xldv20pmThlImaLinkNeTxNumFailures": xldv20pmThlImaLinkNeTxNumFailures,
       "xldv20pmThlImaLinkNeRxNumFailures": xldv20pmThlImaLinkNeRxNumFailures,
       "xldv20pmAtmThresholdLimitTable": xldv20pmAtmThresholdLimitTable,
       "xldv20pmAtmThresholdLimitEntry": xldv20pmAtmThresholdLimitEntry,
       "xldv20pmAtlThresholdLimitIndex": xldv20pmAtlThresholdLimitIndex,
       "xldv20pmAtlTransmittedUserCells": xldv20pmAtlTransmittedUserCells,
       "xldv20pmAtlLostUserCells": xldv20pmAtlLostUserCells,
       "xldv20pmAtlMisinsertedUserCells": xldv20pmAtlMisinsertedUserCells,
       "xldv20pmTraps": xldv20pmTraps,
       "xldv20pmTrapVars": xldv20pmTrapVars,
       "xldv20pmTvIfIndex": xldv20pmTvIfIndex,
       "xldv20pmTvPmType": xldv20pmTvPmType,
       "xldv20pmTvPmCounter": xldv20pmTvPmCounter,
       "xldv20pmTvCurrentCounterValue": xldv20pmTvCurrentCounterValue,
       "xldv20pmTvCurrentCounterLimit": xldv20pmTvCurrentCounterLimit,
       "xldv20pmTvAtmPmCounter": xldv20pmTvAtmPmCounter,
       "xldv20pmTvAtmObjectIndex": xldv20pmTvAtmObjectIndex,
       "xldv20pmTvEndpointType": xldv20pmTvEndpointType,
       "xldv20pmTvIntervalType": xldv20pmTvIntervalType,
       "xldv20pmTrapTypes": xldv20pmTrapTypes}
)
