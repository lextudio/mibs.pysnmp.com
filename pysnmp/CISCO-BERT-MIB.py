# SNMP MIB module (CISCO-BERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BERT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:15 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoBertMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185)
)
ciscoBertMIB.setRevisions(
        ("2002-05-05 00:00",
         "2001-09-09 00:00",
         "2000-12-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BertPatterns(Integer32, TextualConvention):
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
              38)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 2),
          ("allZeros", 1),
          ("altOneZero", 3),
          ("dds1pattern", 33),
          ("dds2pattern", 34),
          ("dds3pattern", 35),
          ("dds4pattern", 36),
          ("dds5pattern", 37),
          ("doubleAltOnesZeros", 4),
          ("inbandLoopBackActivate", 9),
          ("inbandLoopBackDeactivate", 10),
          ("oneIn16", 7),
          ("oneIn4", 5),
          ("oneIn8", 6),
          ("threeIn24", 8),
          ("twoE10MinusOne", 19),
          ("twoE11MinusOne", 20),
          ("twoE15MinusOne", 21),
          ("twoE17MinusOne", 22),
          ("twoE18MinusOne", 23),
          ("twoE20MinusOne", 24),
          ("twoE20MinusOneQRSS", 25),
          ("twoE21MinusOne", 26),
          ("twoE22MinusOne", 27),
          ("twoE23MinusOne", 28),
          ("twoE25MinusOne", 29),
          ("twoE28MinusOne", 30),
          ("twoE29MinusOne", 31),
          ("twoE31MinusOne", 32),
          ("twoE3MinusOne", 11),
          ("twoE4MinusOne", 12),
          ("twoE5MinusOne", 13),
          ("twoE6MinusOne", 14),
          ("twoE7MinusOne", 15),
          ("twoE7MinusOneFT1Loopdown", 17),
          ("twoE7MinusOneFT1Loopup", 16),
          ("twoE9MinusOne", 18),
          ("userPattern", 38))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoBertMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBertMIBObjects = _CiscoBertMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1)
)
_CiscoBertConfig_ObjectIdentity = ObjectIdentity
ciscoBertConfig = _CiscoBertConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1)
)
_CbConfTable_Object = MibTable
cbConfTable = _CbConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cbConfTable.setStatus("current")
_CbConfEntry_Object = MibTableRow
cbConfEntry = _CbConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1)
)
cbConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cbConfEntry.setStatus("current")
_CbTestPattern_Type = BertPatterns
_CbTestPattern_Object = MibTableColumn
cbTestPattern = _CbTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 1),
    _CbTestPattern_Type()
)
cbTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbTestPattern.setStatus("current")


class _CbUserPattern_Type(OctetString):
    """Custom type cbUserPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_CbUserPattern_Type.__name__ = "OctetString"
_CbUserPattern_Object = MibTableColumn
cbUserPattern = _CbUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 2),
    _CbUserPattern_Type()
)
cbUserPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbUserPattern.setStatus("current")


class _CbBertTxPatternInv_Type(Integer32):
    """Custom type cbBertTxPatternInv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("notInverted", 1))
    )


_CbBertTxPatternInv_Type.__name__ = "Integer32"
_CbBertTxPatternInv_Object = MibTableColumn
cbBertTxPatternInv = _CbBertTxPatternInv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 3),
    _CbBertTxPatternInv_Type()
)
cbBertTxPatternInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbBertTxPatternInv.setStatus("current")


class _CbBertRxPatternInv_Type(Integer32):
    """Custom type cbBertRxPatternInv based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("notInverted", 1))
    )


_CbBertRxPatternInv_Type.__name__ = "Integer32"
_CbBertRxPatternInv_Object = MibTableColumn
cbBertRxPatternInv = _CbBertRxPatternInv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 4),
    _CbBertRxPatternInv_Type()
)
cbBertRxPatternInv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbBertRxPatternInv.setStatus("current")


class _CbLoopback_Type(Integer32):
    """Custom type cbLoopback based on Integer32"""
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
        *(("farEndLineLoopback", 1),
          ("farEndPayloadLoopback", 4),
          ("localLoopback", 3),
          ("noLoopback", 6),
          ("remoteLineLoopback", 2),
          ("remotePayloadLoopback", 5))
    )


_CbLoopback_Type.__name__ = "Integer32"
_CbLoopback_Object = MibTableColumn
cbLoopback = _CbLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 5),
    _CbLoopback_Type()
)
cbLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbLoopback.setStatus("current")


class _CbLoopbackCode_Type(Integer32):
    """Custom type cbLoopbackCode based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("latchCSU", 8),
          ("latchDS0Drop", 5),
          ("latchDS0Line", 6),
          ("latchDSU", 9),
          ("latchHL96", 10),
          ("latchOCU", 7),
          ("lineInband", 12),
          ("lineLoopbackESF", 13),
          ("lineLoopbackFEAC", 17),
          ("localLoopback", 14),
          ("noLoopbackCode", 15),
          ("nonLatchCSU", 3),
          ("nonLatchDSU", 4),
          ("nonLatchOCUwith1", 1),
          ("nonLatchOCUwithout1", 2),
          ("payloadLoopbackESF", 16),
          ("smartJackInband", 18),
          ("v54PN127Polynomial", 11))
    )


_CbLoopbackCode_Type.__name__ = "Integer32"
_CbLoopbackCode_Object = MibTableColumn
cbLoopbackCode = _CbLoopbackCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 6),
    _CbLoopbackCode_Type()
)
cbLoopbackCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbLoopbackCode.setStatus("current")


class _CbSingleBitErrorInsert_Type(Integer32):
    """Custom type cbSingleBitErrorInsert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertError", 2),
          ("noError", 1))
    )


_CbSingleBitErrorInsert_Type.__name__ = "Integer32"
_CbSingleBitErrorInsert_Object = MibTableColumn
cbSingleBitErrorInsert = _CbSingleBitErrorInsert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 7),
    _CbSingleBitErrorInsert_Type()
)
cbSingleBitErrorInsert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbSingleBitErrorInsert.setStatus("current")


class _CbErrorInsertionRate_Type(Integer32):
    """Custom type cbErrorInsertionRate based on Integer32"""
    defaultValue = 1

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
        *(("noError", 1),
          ("oneInHundred", 3),
          ("oneInHundredThousand", 6),
          ("oneInMillion", 7),
          ("oneInTen", 2),
          ("oneInTenMillion", 8),
          ("oneInTenThousand", 5),
          ("oneInThousand", 4))
    )


_CbErrorInsertionRate_Type.__name__ = "Integer32"
_CbErrorInsertionRate_Object = MibTableColumn
cbErrorInsertionRate = _CbErrorInsertionRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 8),
    _CbErrorInsertionRate_Type()
)
cbErrorInsertionRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbErrorInsertionRate.setStatus("current")


class _CbDuration_Type(Integer32):
    """Custom type cbDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CbDuration_Type.__name__ = "Integer32"
_CbDuration_Object = MibTableColumn
cbDuration = _CbDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 9),
    _CbDuration_Type()
)
cbDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbDuration.setStatus("current")
if mibBuilder.loadTexts:
    cbDuration.setUnits("seconds")


class _CbOperStatus_Type(Integer32):
    """Custom type cbOperStatus based on Integer32"""
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
        *(("bertFailed", 6),
          ("clockOutOfSync", 5),
          ("inLoopback", 4),
          ("inSync", 2),
          ("outOfSync", 3),
          ("success", 1))
    )


_CbOperStatus_Type.__name__ = "Integer32"
_CbOperStatus_Object = MibTableColumn
cbOperStatus = _CbOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 10),
    _CbOperStatus_Type()
)
cbOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbOperStatus.setStatus("current")


class _CbFailedReason_Type(Integer32):
    """Custom type cbFailedReason based on Integer32"""
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
        *(("aborted", 1),
          ("interfaceStateChange", 3),
          ("loopbackFailed", 2),
          ("processorModuleStateChange", 4),
          ("unknown", 5))
    )


_CbFailedReason_Type.__name__ = "Integer32"
_CbFailedReason_Object = MibTableColumn
cbFailedReason = _CbFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 11),
    _CbFailedReason_Type()
)
cbFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbFailedReason.setStatus("current")
_CbStartDateAndTime_Type = DateAndTime
_CbStartDateAndTime_Object = MibTableColumn
cbStartDateAndTime = _CbStartDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 12),
    _CbStartDateAndTime_Type()
)
cbStartDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbStartDateAndTime.setStatus("current")


class _CbDS0DPCodeIteration_Type(Integer32):
    """Custom type cbDS0DPCodeIteration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CbDS0DPCodeIteration_Type.__name__ = "Integer32"
_CbDS0DPCodeIteration_Object = MibTableColumn
cbDS0DPCodeIteration = _CbDS0DPCodeIteration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 13),
    _CbDS0DPCodeIteration_Type()
)
cbDS0DPCodeIteration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbDS0DPCodeIteration.setStatus("current")
_CbRowStatus_Type = RowStatus
_CbRowStatus_Object = MibTableColumn
cbRowStatus = _CbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 14),
    _CbRowStatus_Type()
)
cbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbRowStatus.setStatus("current")


class _CbDs0BitMap_Type(Bits):
    """Custom type cbDs0BitMap based on Bits"""
    namedValues = NamedValues(
        *(("dsZero1", 0),
          ("dsZero10", 9),
          ("dsZero11", 10),
          ("dsZero12", 11),
          ("dsZero13", 12),
          ("dsZero14", 13),
          ("dsZero15", 14),
          ("dsZero16", 15),
          ("dsZero17", 16),
          ("dsZero18", 17),
          ("dsZero19", 18),
          ("dsZero2", 1),
          ("dsZero20", 19),
          ("dsZero21", 20),
          ("dsZero22", 21),
          ("dsZero23", 22),
          ("dsZero24", 23),
          ("dsZero25", 24),
          ("dsZero26", 25),
          ("dsZero27", 26),
          ("dsZero28", 27),
          ("dsZero29", 28),
          ("dsZero3", 2),
          ("dsZero30", 29),
          ("dsZero31", 30),
          ("dsZero4", 3),
          ("dsZero5", 4),
          ("dsZero6", 5),
          ("dsZero7", 6),
          ("dsZero8", 7),
          ("dsZero9", 8))
    )

_CbDs0BitMap_Type.__name__ = "Bits"
_CbDs0BitMap_Object = MibTableColumn
cbDs0BitMap = _CbDs0BitMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 1, 1, 15),
    _CbDs0BitMap_Type()
)
cbDs0BitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cbDs0BitMap.setStatus("current")
_CbStatsTable_Object = MibTable
cbStatsTable = _CbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cbStatsTable.setStatus("current")
_CbStatsEntry_Object = MibTableRow
cbStatsEntry = _CbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1)
)
cbStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cbStatsEntry.setStatus("current")
_CbTxBitCountLower_Type = Counter32
_CbTxBitCountLower_Object = MibTableColumn
cbTxBitCountLower = _CbTxBitCountLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 1),
    _CbTxBitCountLower_Type()
)
cbTxBitCountLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbTxBitCountLower.setStatus("current")
_CbTxBitCountUpper_Type = Counter32
_CbTxBitCountUpper_Object = MibTableColumn
cbTxBitCountUpper = _CbTxBitCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 2),
    _CbTxBitCountUpper_Type()
)
cbTxBitCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbTxBitCountUpper.setStatus("current")
_CbHCTxBitCounts_Type = Counter64
_CbHCTxBitCounts_Object = MibTableColumn
cbHCTxBitCounts = _CbHCTxBitCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 3),
    _CbHCTxBitCounts_Type()
)
cbHCTxBitCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHCTxBitCounts.setStatus("current")
_CbRxBitCountLower_Type = Counter32
_CbRxBitCountLower_Object = MibTableColumn
cbRxBitCountLower = _CbRxBitCountLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 4),
    _CbRxBitCountLower_Type()
)
cbRxBitCountLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbRxBitCountLower.setStatus("current")
_CbRxBitCountUpper_Type = Counter32
_CbRxBitCountUpper_Object = MibTableColumn
cbRxBitCountUpper = _CbRxBitCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 5),
    _CbRxBitCountUpper_Type()
)
cbRxBitCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbRxBitCountUpper.setStatus("current")
_CbHCRxBitCounts_Type = Counter64
_CbHCRxBitCounts_Object = MibTableColumn
cbHCRxBitCounts = _CbHCRxBitCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 6),
    _CbHCRxBitCounts_Type()
)
cbHCRxBitCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHCRxBitCounts.setStatus("current")
_CbRxBitErrCountLower_Type = Counter32
_CbRxBitErrCountLower_Object = MibTableColumn
cbRxBitErrCountLower = _CbRxBitErrCountLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 7),
    _CbRxBitErrCountLower_Type()
)
cbRxBitErrCountLower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbRxBitErrCountLower.setStatus("current")
_CbRxBitErrCountUpper_Type = Counter32
_CbRxBitErrCountUpper_Object = MibTableColumn
cbRxBitErrCountUpper = _CbRxBitErrCountUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 8),
    _CbRxBitErrCountUpper_Type()
)
cbRxBitErrCountUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbRxBitErrCountUpper.setStatus("current")
_CbHCRxBitErrCounts_Type = Counter64
_CbHCRxBitErrCounts_Object = MibTableColumn
cbHCRxBitErrCounts = _CbHCRxBitErrCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 9),
    _CbHCRxBitErrCounts_Type()
)
cbHCRxBitErrCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbHCRxBitErrCounts.setStatus("current")
_CbSyncLossCounts_Type = Counter32
_CbSyncLossCounts_Object = MibTableColumn
cbSyncLossCounts = _CbSyncLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 10),
    _CbSyncLossCounts_Type()
)
cbSyncLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbSyncLossCounts.setStatus("current")
_CbPatternLossCounts_Type = Counter32
_CbPatternLossCounts_Object = MibTableColumn
cbPatternLossCounts = _CbPatternLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 11),
    _CbPatternLossCounts_Type()
)
cbPatternLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbPatternLossCounts.setStatus("current")
_CbFrameLossCounts_Type = Counter32
_CbFrameLossCounts_Object = MibTableColumn
cbFrameLossCounts = _CbFrameLossCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 12),
    _CbFrameLossCounts_Type()
)
cbFrameLossCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbFrameLossCounts.setStatus("current")
_CbESsCounts_Type = Counter32
_CbESsCounts_Object = MibTableColumn
cbESsCounts = _CbESsCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 13),
    _CbESsCounts_Type()
)
cbESsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbESsCounts.setStatus("current")
_CbSESsCounts_Type = Counter32
_CbSESsCounts_Object = MibTableColumn
cbSESsCounts = _CbSESsCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 14),
    _CbSESsCounts_Type()
)
cbSESsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbSESsCounts.setStatus("current")
_CbEFSsCounts_Type = Counter32
_CbEFSsCounts_Object = MibTableColumn
cbEFSsCounts = _CbEFSsCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 15),
    _CbEFSsCounts_Type()
)
cbEFSsCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbEFSsCounts.setStatus("current")
_CbErrorInjectCounts_Type = Counter32
_CbErrorInjectCounts_Object = MibTableColumn
cbErrorInjectCounts = _CbErrorInjectCounts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 1, 1, 2, 1, 16),
    _CbErrorInjectCounts_Type()
)
cbErrorInjectCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbErrorInjectCounts.setStatus("current")
_CiscoBertMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBertMIBConformance = _CiscoBertMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8)
)
_CiscoBertMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBertMIBCompliances = _CiscoBertMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 1)
)
_CiscoBertMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBertMIBGroups = _CiscoBertMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2)
)

# Managed Objects groups

ciscoBertConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2, 1)
)
ciscoBertConfigGroup.setObjects(
      *(("CISCO-BERT-MIB", "cbTestPattern"),
        ("CISCO-BERT-MIB", "cbUserPattern"),
        ("CISCO-BERT-MIB", "cbBertTxPatternInv"),
        ("CISCO-BERT-MIB", "cbBertRxPatternInv"),
        ("CISCO-BERT-MIB", "cbSingleBitErrorInsert"),
        ("CISCO-BERT-MIB", "cbErrorInsertionRate"),
        ("CISCO-BERT-MIB", "cbDuration"),
        ("CISCO-BERT-MIB", "cbOperStatus"),
        ("CISCO-BERT-MIB", "cbFailedReason"),
        ("CISCO-BERT-MIB", "cbStartDateAndTime"),
        ("CISCO-BERT-MIB", "cbDS0DPCodeIteration"),
        ("CISCO-BERT-MIB", "cbRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoBertConfigGroup.setStatus("current")

ciscoBertLoopbackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2, 2)
)
ciscoBertLoopbackGroup.setObjects(
      *(("CISCO-BERT-MIB", "cbLoopback"),
        ("CISCO-BERT-MIB", "cbLoopbackCode"))
)
if mibBuilder.loadTexts:
    ciscoBertLoopbackGroup.setStatus("current")

ciscoBertStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2, 3)
)
ciscoBertStatsGroup.setObjects(
      *(("CISCO-BERT-MIB", "cbTxBitCountLower"),
        ("CISCO-BERT-MIB", "cbTxBitCountUpper"),
        ("CISCO-BERT-MIB", "cbRxBitCountLower"),
        ("CISCO-BERT-MIB", "cbRxBitCountUpper"),
        ("CISCO-BERT-MIB", "cbRxBitErrCountLower"),
        ("CISCO-BERT-MIB", "cbRxBitErrCountUpper"),
        ("CISCO-BERT-MIB", "cbSyncLossCounts"),
        ("CISCO-BERT-MIB", "cbPatternLossCounts"),
        ("CISCO-BERT-MIB", "cbFrameLossCounts"),
        ("CISCO-BERT-MIB", "cbESsCounts"),
        ("CISCO-BERT-MIB", "cbSESsCounts"),
        ("CISCO-BERT-MIB", "cbEFSsCounts"),
        ("CISCO-BERT-MIB", "cbErrorInjectCounts"))
)
if mibBuilder.loadTexts:
    ciscoBertStatsGroup.setStatus("current")

ciscoBertHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2, 4)
)
ciscoBertHCStatsGroup.setObjects(
      *(("CISCO-BERT-MIB", "cbHCTxBitCounts"),
        ("CISCO-BERT-MIB", "cbHCRxBitCounts"),
        ("CISCO-BERT-MIB", "cbHCRxBitErrCounts"))
)
if mibBuilder.loadTexts:
    ciscoBertHCStatsGroup.setStatus("current")

ciscoBertConfigGroupDs1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 2, 5)
)
ciscoBertConfigGroupDs1.setObjects(
    ("CISCO-BERT-MIB", "cbDs0BitMap")
)
if mibBuilder.loadTexts:
    ciscoBertConfigGroupDs1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoBertMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 185, 8, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBertMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BERT-MIB",
    **{"BertPatterns": BertPatterns,
       "ciscoBertMIB": ciscoBertMIB,
       "ciscoBertMIBObjects": ciscoBertMIBObjects,
       "ciscoBertConfig": ciscoBertConfig,
       "cbConfTable": cbConfTable,
       "cbConfEntry": cbConfEntry,
       "cbTestPattern": cbTestPattern,
       "cbUserPattern": cbUserPattern,
       "cbBertTxPatternInv": cbBertTxPatternInv,
       "cbBertRxPatternInv": cbBertRxPatternInv,
       "cbLoopback": cbLoopback,
       "cbLoopbackCode": cbLoopbackCode,
       "cbSingleBitErrorInsert": cbSingleBitErrorInsert,
       "cbErrorInsertionRate": cbErrorInsertionRate,
       "cbDuration": cbDuration,
       "cbOperStatus": cbOperStatus,
       "cbFailedReason": cbFailedReason,
       "cbStartDateAndTime": cbStartDateAndTime,
       "cbDS0DPCodeIteration": cbDS0DPCodeIteration,
       "cbRowStatus": cbRowStatus,
       "cbDs0BitMap": cbDs0BitMap,
       "cbStatsTable": cbStatsTable,
       "cbStatsEntry": cbStatsEntry,
       "cbTxBitCountLower": cbTxBitCountLower,
       "cbTxBitCountUpper": cbTxBitCountUpper,
       "cbHCTxBitCounts": cbHCTxBitCounts,
       "cbRxBitCountLower": cbRxBitCountLower,
       "cbRxBitCountUpper": cbRxBitCountUpper,
       "cbHCRxBitCounts": cbHCRxBitCounts,
       "cbRxBitErrCountLower": cbRxBitErrCountLower,
       "cbRxBitErrCountUpper": cbRxBitErrCountUpper,
       "cbHCRxBitErrCounts": cbHCRxBitErrCounts,
       "cbSyncLossCounts": cbSyncLossCounts,
       "cbPatternLossCounts": cbPatternLossCounts,
       "cbFrameLossCounts": cbFrameLossCounts,
       "cbESsCounts": cbESsCounts,
       "cbSESsCounts": cbSESsCounts,
       "cbEFSsCounts": cbEFSsCounts,
       "cbErrorInjectCounts": cbErrorInjectCounts,
       "ciscoBertMIBConformance": ciscoBertMIBConformance,
       "ciscoBertMIBCompliances": ciscoBertMIBCompliances,
       "ciscoBertMIBCompliance": ciscoBertMIBCompliance,
       "ciscoBertMIBGroups": ciscoBertMIBGroups,
       "ciscoBertConfigGroup": ciscoBertConfigGroup,
       "ciscoBertLoopbackGroup": ciscoBertLoopbackGroup,
       "ciscoBertStatsGroup": ciscoBertStatsGroup,
       "ciscoBertHCStatsGroup": ciscoBertHCStatsGroup,
       "ciscoBertConfigGroupDs1": ciscoBertConfigGroupDs1}
)
