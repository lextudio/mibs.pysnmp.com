# SNMP MIB module (CISCO-MGX82XX-DSX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MGX82XX-DSX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:31 2024
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

(dsx1Line,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "dsx1Line")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoMgx82xxDsx1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 58)
)
ciscoMgx82xxDsx1MIB.setRevisions(
        ("2003-03-31 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx1CnfGrp_ObjectIdentity = ObjectIdentity
dsx1CnfGrp = _Dsx1CnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1)
)
_Dsx1CnfGrpTable_Object = MibTable
dsx1CnfGrpTable = _Dsx1CnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1CnfGrpTable.setStatus("current")
_Dsx1CnfGrpEntry_Object = MibTableRow
dsx1CnfGrpEntry = _Dsx1CnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1)
)
dsx1CnfGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX1-MIB", "lineNum"),
)
if mibBuilder.loadTexts:
    dsx1CnfGrpEntry.setStatus("current")


class _LineNum_Type(Integer32):
    """Custom type lineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LineNum_Type.__name__ = "Integer32"
_LineNum_Object = MibTableColumn
lineNum = _LineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 1),
    _LineNum_Type()
)
lineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineNum.setStatus("current")


class _LineConnectorType_Type(Integer32):
    """Custom type lineConnectorType based on Integer32"""
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
        *(("bnc", 2),
          ("db15", 1),
          ("rj48", 3),
          ("smb", 5),
          ("unused", 4))
    )


_LineConnectorType_Type.__name__ = "Integer32"
_LineConnectorType_Object = MibTableColumn
lineConnectorType = _LineConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 2),
    _LineConnectorType_Type()
)
lineConnectorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineConnectorType.setStatus("current")


class _LineEnable_Type(Integer32):
    """Custom type lineEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("modify", 3))
    )


_LineEnable_Type.__name__ = "Integer32"
_LineEnable_Object = MibTableColumn
lineEnable = _LineEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 3),
    _LineEnable_Type()
)
lineEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineEnable.setStatus("current")


class _LineType_Type(Integer32):
    """Custom type lineType based on Integer32"""
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
        *(("dsx1D4", 2),
          ("dsx1E1", 3),
          ("dsx1E1CRC", 4),
          ("dsx1E1CRC-MF", 6),
          ("dsx1E1MF", 5),
          ("dsx1E1Q50", 8),
          ("dsx1E1Q50CRC", 9),
          ("dsx1E1clearchannel", 7),
          ("dsx1ESF", 1))
    )


_LineType_Type.__name__ = "Integer32"
_LineType_Object = MibTableColumn
lineType = _LineType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 4),
    _LineType_Type()
)
lineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineType.setStatus("current")


class _LineCoding_Type(Integer32):
    """Custom type lineCoding based on Integer32"""
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
        *(("dsx1AMI", 4),
          ("dsx1B8ZS", 2),
          ("dsx1HDB3", 3),
          ("dsx1JBZS", 1),
          ("unused", 5))
    )


_LineCoding_Type.__name__ = "Integer32"
_LineCoding_Object = MibTableColumn
lineCoding = _LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 5),
    _LineCoding_Type()
)
lineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineCoding.setStatus("current")


class _LineLength_Type(Integer32):
    """Custom type lineLength based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("lineLength-120-Ohm", 9),
          ("lineLength-75-Ohm", 8),
          ("lineLength0To110Feet", 1),
          ("lineLength0To131Feet", 10),
          ("lineLength110To220Feet", 2),
          ("lineLength131To262Feet", 11),
          ("lineLength220To330Feet", 3),
          ("lineLength262To393Feet", 12),
          ("lineLength330To440Feet", 4),
          ("lineLength393To524Feet", 13),
          ("lineLength440To550Feet", 5),
          ("lineLength524To655Feet", 14),
          ("lineLength550To660Feet", 6),
          ("lineLength655FeetPlus", 15),
          ("lineLength660FeetPlus", 7),
          ("notRequired", 16))
    )


_LineLength_Type.__name__ = "Integer32"
_LineLength_Object = MibTableColumn
lineLength = _LineLength_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 6),
    _LineLength_Type()
)
lineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineLength.setStatus("current")


class _LineXmtClockSource_Type(Integer32):
    """Custom type lineXmtClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )


_LineXmtClockSource_Type.__name__ = "Integer32"
_LineXmtClockSource_Object = MibTableColumn
lineXmtClockSource = _LineXmtClockSource_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 7),
    _LineXmtClockSource_Type()
)
lineXmtClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineXmtClockSource.setStatus("current")


class _LineLoopbackCommand_Type(Integer32):
    """Custom type lineLoopbackCommand based on Integer32"""
    defaultValue = 1

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
        *(("dsx1LocalLoop", 3),
          ("dsx1NoLoop", 1),
          ("dsx1PayloadLoop", 4),
          ("dsx1RemoteLoop", 2))
    )


_LineLoopbackCommand_Type.__name__ = "Integer32"
_LineLoopbackCommand_Object = MibTableColumn
lineLoopbackCommand = _LineLoopbackCommand_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 8),
    _LineLoopbackCommand_Type()
)
lineLoopbackCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineLoopbackCommand.setStatus("current")


class _LineSendCode_Type(Integer32):
    """Custom type lineSendCode based on Integer32"""
    defaultValue = 1

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
        *(("dsx1SendLineCode", 2),
          ("dsx1SendNoCode", 1),
          ("dsx1SendPayloadCode", 3),
          ("dsx1SendResetCode", 4))
    )


_LineSendCode_Type.__name__ = "Integer32"
_LineSendCode_Object = MibTableColumn
lineSendCode = _LineSendCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 9),
    _LineSendCode_Type()
)
lineSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSendCode.setStatus("current")


class _LineUsedTimeslotsBitMap_Type(Integer32):
    """Custom type lineUsedTimeslotsBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LineUsedTimeslotsBitMap_Type.__name__ = "Integer32"
_LineUsedTimeslotsBitMap_Object = MibTableColumn
lineUsedTimeslotsBitMap = _LineUsedTimeslotsBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 10),
    _LineUsedTimeslotsBitMap_Type()
)
lineUsedTimeslotsBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUsedTimeslotsBitMap.setStatus("current")


class _LineLoopbackCodeDetection_Type(Integer32):
    """Custom type lineLoopbackCodeDetection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("codeDetectDisabled", 1),
          ("codeDetectEnabled", 2))
    )


_LineLoopbackCodeDetection_Type.__name__ = "Integer32"
_LineLoopbackCodeDetection_Object = MibTableColumn
lineLoopbackCodeDetection = _LineLoopbackCodeDetection_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 11),
    _LineLoopbackCodeDetection_Type()
)
lineLoopbackCodeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineLoopbackCodeDetection.setStatus("current")


class _LineBERTEnable_Type(Integer32):
    """Custom type lineBERTEnable based on Integer32"""
    defaultValue = 1

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


_LineBERTEnable_Type.__name__ = "Integer32"
_LineBERTEnable_Object = MibTableColumn
lineBERTEnable = _LineBERTEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 12),
    _LineBERTEnable_Type()
)
lineBERTEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBERTEnable.setStatus("current")


class _LineBERTPattern_Type(Integer32):
    """Custom type lineBERTPattern based on Integer32"""
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 2),
          ("allZeros", 1),
          ("alternateONeZero", 3),
          ("doubleOneZero", 4),
          ("fifteenBit", 9),
          ("twentyBit", 10),
          ("twentyBitQRSS", 11),
          ("twentythreeBit", 12),
          ("userFourWords", 8),
          ("userOneWords", 5),
          ("userThreeWords", 7),
          ("userTwoWords", 6))
    )


_LineBERTPattern_Type.__name__ = "Integer32"
_LineBERTPattern_Object = MibTableColumn
lineBERTPattern = _LineBERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 13),
    _LineBERTPattern_Type()
)
lineBERTPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBERTPattern.setStatus("current")


class _LineBERTResult_Type(Integer32):
    """Custom type lineBERTResult based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_LineBERTResult_Type.__name__ = "Integer32"
_LineBERTResult_Object = MibTableColumn
lineBERTResult = _LineBERTResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 14),
    _LineBERTResult_Type()
)
lineBERTResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineBERTResult.setStatus("current")


class _BERTResultClrButton_Type(Integer32):
    """Custom type bERTResultClrButton based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_BERTResultClrButton_Type.__name__ = "Integer32"
_BERTResultClrButton_Object = MibTableColumn
bERTResultClrButton = _BERTResultClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 1, 1, 15),
    _BERTResultClrButton_Type()
)
bERTResultClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bERTResultClrButton.setStatus("current")


class _LineNumofValidEntries_Type(Integer32):
    """Custom type lineNumofValidEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_LineNumofValidEntries_Type.__name__ = "Integer32"
_LineNumofValidEntries_Object = MibScalar
lineNumofValidEntries = _LineNumofValidEntries_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 1, 2),
    _LineNumofValidEntries_Type()
)
lineNumofValidEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineNumofValidEntries.setStatus("current")
_Dsx1AlmCnfGrp_ObjectIdentity = ObjectIdentity
dsx1AlmCnfGrp = _Dsx1AlmCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2)
)
_Dsx1AlmCnfGrpTable_Object = MibTable
dsx1AlmCnfGrpTable = _Dsx1AlmCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dsx1AlmCnfGrpTable.setStatus("current")
_Dsx1AlmCnfGrpEntry_Object = MibTableRow
dsx1AlmCnfGrpEntry = _Dsx1AlmCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1)
)
dsx1AlmCnfGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX1-MIB", "almCnfLineNum"),
)
if mibBuilder.loadTexts:
    dsx1AlmCnfGrpEntry.setStatus("current")


class _AlmCnfLineNum_Type(Integer32):
    """Custom type almCnfLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlmCnfLineNum_Type.__name__ = "Integer32"
_AlmCnfLineNum_Object = MibTableColumn
almCnfLineNum = _AlmCnfLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 1),
    _AlmCnfLineNum_Type()
)
almCnfLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almCnfLineNum.setStatus("current")


class _RedSeverity_Type(Integer32):
    """Custom type redSeverity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_RedSeverity_Type.__name__ = "Integer32"
_RedSeverity_Object = MibTableColumn
redSeverity = _RedSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 2),
    _RedSeverity_Type()
)
redSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redSeverity.setStatus("current")


class _RAISeverity_Type(Integer32):
    """Custom type rAISeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("major", 2),
          ("minor", 1))
    )


_RAISeverity_Type.__name__ = "Integer32"
_RAISeverity_Object = MibTableColumn
rAISeverity = _RAISeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 3),
    _RAISeverity_Type()
)
rAISeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rAISeverity.setStatus("current")


class _NEAlarmUpCount_Type(Integer32):
    """Custom type nEAlarmUpCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NEAlarmUpCount_Type.__name__ = "Integer32"
_NEAlarmUpCount_Object = MibTableColumn
nEAlarmUpCount = _NEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 4),
    _NEAlarmUpCount_Type()
)
nEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nEAlarmUpCount.setStatus("current")


class _NEAlarmDownCount_Type(Integer32):
    """Custom type nEAlarmDownCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NEAlarmDownCount_Type.__name__ = "Integer32"
_NEAlarmDownCount_Object = MibTableColumn
nEAlarmDownCount = _NEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 5),
    _NEAlarmDownCount_Type()
)
nEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nEAlarmDownCount.setStatus("current")


class _NEAlarmThreshold_Type(Integer32):
    """Custom type nEAlarmThreshold based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NEAlarmThreshold_Type.__name__ = "Integer32"
_NEAlarmThreshold_Object = MibTableColumn
nEAlarmThreshold = _NEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 6),
    _NEAlarmThreshold_Type()
)
nEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nEAlarmThreshold.setStatus("current")


class _FEAlarmUpCount_Type(Integer32):
    """Custom type fEAlarmUpCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FEAlarmUpCount_Type.__name__ = "Integer32"
_FEAlarmUpCount_Object = MibTableColumn
fEAlarmUpCount = _FEAlarmUpCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 7),
    _FEAlarmUpCount_Type()
)
fEAlarmUpCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fEAlarmUpCount.setStatus("current")


class _FEAlarmDownCount_Type(Integer32):
    """Custom type fEAlarmDownCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FEAlarmDownCount_Type.__name__ = "Integer32"
_FEAlarmDownCount_Object = MibTableColumn
fEAlarmDownCount = _FEAlarmDownCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 8),
    _FEAlarmDownCount_Type()
)
fEAlarmDownCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fEAlarmDownCount.setStatus("current")


class _FEAlarmThreshold_Type(Integer32):
    """Custom type fEAlarmThreshold based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FEAlarmThreshold_Type.__name__ = "Integer32"
_FEAlarmThreshold_Object = MibTableColumn
fEAlarmThreshold = _FEAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 9),
    _FEAlarmThreshold_Type()
)
fEAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fEAlarmThreshold.setStatus("current")


class _StatisticalAlarmSeverity_Type(Integer32):
    """Custom type statisticalAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 3),
          ("major", 2),
          ("minor", 1))
    )


_StatisticalAlarmSeverity_Type.__name__ = "Integer32"
_StatisticalAlarmSeverity_Object = MibTableColumn
statisticalAlarmSeverity = _StatisticalAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 10),
    _StatisticalAlarmSeverity_Type()
)
statisticalAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statisticalAlarmSeverity.setStatus("current")


class _LCV15MinThreshold_Type(Integer32):
    """Custom type lCV15MinThreshold based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LCV15MinThreshold_Type.__name__ = "Integer32"
_LCV15MinThreshold_Object = MibTableColumn
lCV15MinThreshold = _LCV15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 11),
    _LCV15MinThreshold_Type()
)
lCV15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lCV15MinThreshold.setStatus("current")


class _LCV24HrThreshold_Type(Integer32):
    """Custom type lCV24HrThreshold based on Integer32"""
    defaultValue = 134

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LCV24HrThreshold_Type.__name__ = "Integer32"
_LCV24HrThreshold_Object = MibTableColumn
lCV24HrThreshold = _LCV24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 12),
    _LCV24HrThreshold_Type()
)
lCV24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lCV24HrThreshold.setStatus("current")


class _LES15MinThreshold_Type(Integer32):
    """Custom type lES15MinThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LES15MinThreshold_Type.__name__ = "Integer32"
_LES15MinThreshold_Object = MibTableColumn
lES15MinThreshold = _LES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 13),
    _LES15MinThreshold_Type()
)
lES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lES15MinThreshold.setStatus("current")


class _LES24HrThreshold_Type(Integer32):
    """Custom type lES24HrThreshold based on Integer32"""
    defaultValue = 121

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LES24HrThreshold_Type.__name__ = "Integer32"
_LES24HrThreshold_Object = MibTableColumn
lES24HrThreshold = _LES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 14),
    _LES24HrThreshold_Type()
)
lES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lES24HrThreshold.setStatus("current")


class _LSES15MinThreshold_Type(Integer32):
    """Custom type lSES15MinThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LSES15MinThreshold_Type.__name__ = "Integer32"
_LSES15MinThreshold_Object = MibTableColumn
lSES15MinThreshold = _LSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 15),
    _LSES15MinThreshold_Type()
)
lSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSES15MinThreshold.setStatus("current")


class _LSES24HrThreshold_Type(Integer32):
    """Custom type lSES24HrThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LSES24HrThreshold_Type.__name__ = "Integer32"
_LSES24HrThreshold_Object = MibTableColumn
lSES24HrThreshold = _LSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 16),
    _LSES24HrThreshold_Type()
)
lSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lSES24HrThreshold.setStatus("current")


class _CRC15MinThreshold_Type(Integer32):
    """Custom type cRC15MinThreshold based on Integer32"""
    defaultValue = 14

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRC15MinThreshold_Type.__name__ = "Integer32"
_CRC15MinThreshold_Object = MibTableColumn
cRC15MinThreshold = _CRC15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 17),
    _CRC15MinThreshold_Type()
)
cRC15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRC15MinThreshold.setStatus("current")


class _CRC24HrThreshold_Type(Integer32):
    """Custom type cRC24HrThreshold based on Integer32"""
    defaultValue = 134

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRC24HrThreshold_Type.__name__ = "Integer32"
_CRC24HrThreshold_Object = MibTableColumn
cRC24HrThreshold = _CRC24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 18),
    _CRC24HrThreshold_Type()
)
cRC24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRC24HrThreshold.setStatus("current")


class _CRCES15MinThreshold_Type(Integer32):
    """Custom type cRCES15MinThreshold based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRCES15MinThreshold_Type.__name__ = "Integer32"
_CRCES15MinThreshold_Object = MibTableColumn
cRCES15MinThreshold = _CRCES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 19),
    _CRCES15MinThreshold_Type()
)
cRCES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRCES15MinThreshold.setStatus("current")


class _CRCES24HrThreshold_Type(Integer32):
    """Custom type cRCES24HrThreshold based on Integer32"""
    defaultValue = 121

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRCES24HrThreshold_Type.__name__ = "Integer32"
_CRCES24HrThreshold_Object = MibTableColumn
cRCES24HrThreshold = _CRCES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 20),
    _CRCES24HrThreshold_Type()
)
cRCES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRCES24HrThreshold.setStatus("current")


class _CRCSES15MinThreshold_Type(Integer32):
    """Custom type cRCSES15MinThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRCSES15MinThreshold_Type.__name__ = "Integer32"
_CRCSES15MinThreshold_Object = MibTableColumn
cRCSES15MinThreshold = _CRCSES15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 21),
    _CRCSES15MinThreshold_Type()
)
cRCSES15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRCSES15MinThreshold.setStatus("current")


class _CRCSES24HrThreshold_Type(Integer32):
    """Custom type cRCSES24HrThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CRCSES24HrThreshold_Type.__name__ = "Integer32"
_CRCSES24HrThreshold_Object = MibTableColumn
cRCSES24HrThreshold = _CRCSES24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 22),
    _CRCSES24HrThreshold_Type()
)
cRCSES24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRCSES24HrThreshold.setStatus("current")


class _SEFS15MinThreshold_Type(Integer32):
    """Custom type sEFS15MinThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SEFS15MinThreshold_Type.__name__ = "Integer32"
_SEFS15MinThreshold_Object = MibTableColumn
sEFS15MinThreshold = _SEFS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 23),
    _SEFS15MinThreshold_Type()
)
sEFS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sEFS15MinThreshold.setStatus("current")


class _SEFS24HrThreshold_Type(Integer32):
    """Custom type sEFS24HrThreshold based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SEFS24HrThreshold_Type.__name__ = "Integer32"
_SEFS24HrThreshold_Object = MibTableColumn
sEFS24HrThreshold = _SEFS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 24),
    _SEFS24HrThreshold_Type()
)
sEFS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sEFS24HrThreshold.setStatus("current")


class _AISS15MinThreshold_Type(Integer32):
    """Custom type aISS15MinThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AISS15MinThreshold_Type.__name__ = "Integer32"
_AISS15MinThreshold_Object = MibTableColumn
aISS15MinThreshold = _AISS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 25),
    _AISS15MinThreshold_Type()
)
aISS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aISS15MinThreshold.setStatus("current")


class _AISS24HrThreshold_Type(Integer32):
    """Custom type aISS24HrThreshold based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AISS24HrThreshold_Type.__name__ = "Integer32"
_AISS24HrThreshold_Object = MibTableColumn
aISS24HrThreshold = _AISS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 26),
    _AISS24HrThreshold_Type()
)
aISS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aISS24HrThreshold.setStatus("current")


class _UAS15MinThreshold_Type(Integer32):
    """Custom type uAS15MinThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UAS15MinThreshold_Type.__name__ = "Integer32"
_UAS15MinThreshold_Object = MibTableColumn
uAS15MinThreshold = _UAS15MinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 27),
    _UAS15MinThreshold_Type()
)
uAS15MinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uAS15MinThreshold.setStatus("current")


class _UAS24HrThreshold_Type(Integer32):
    """Custom type uAS24HrThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UAS24HrThreshold_Type.__name__ = "Integer32"
_UAS24HrThreshold_Object = MibTableColumn
uAS24HrThreshold = _UAS24HrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 2, 1, 1, 28),
    _UAS24HrThreshold_Type()
)
uAS24HrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uAS24HrThreshold.setStatus("current")
_Dsx1AlmGrp_ObjectIdentity = ObjectIdentity
dsx1AlmGrp = _Dsx1AlmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3)
)
_Dsx1AlmGrpTable_Object = MibTable
dsx1AlmGrpTable = _Dsx1AlmGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dsx1AlmGrpTable.setStatus("current")
_Dsx1AlmGrpEntry_Object = MibTableRow
dsx1AlmGrpEntry = _Dsx1AlmGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1)
)
dsx1AlmGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX1-MIB", "almLineNum"),
)
if mibBuilder.loadTexts:
    dsx1AlmGrpEntry.setStatus("current")


class _AlmLineNum_Type(Integer32):
    """Custom type almLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlmLineNum_Type.__name__ = "Integer32"
_AlmLineNum_Object = MibTableColumn
almLineNum = _AlmLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 1),
    _AlmLineNum_Type()
)
almLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almLineNum.setStatus("current")


class _LineAlarmState_Type(Integer32):
    """Custom type lineAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LineAlarmState_Type.__name__ = "Integer32"
_LineAlarmState_Object = MibTableColumn
lineAlarmState = _LineAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 2),
    _LineAlarmState_Type()
)
lineAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAlarmState.setStatus("current")


class _LineStatisticalAlarmState_Type(Integer32):
    """Custom type lineStatisticalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LineStatisticalAlarmState_Type.__name__ = "Integer32"
_LineStatisticalAlarmState_Object = MibTableColumn
lineStatisticalAlarmState = _LineStatisticalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 3),
    _LineStatisticalAlarmState_Type()
)
lineStatisticalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineStatisticalAlarmState.setStatus("current")
_LCVCurrent_Type = Counter32
_LCVCurrent_Object = MibTableColumn
lCVCurrent = _LCVCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 4),
    _LCVCurrent_Type()
)
lCVCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCVCurrent.setStatus("current")
_LCV15MinBucket_Type = Counter32
_LCV15MinBucket_Object = MibTableColumn
lCV15MinBucket = _LCV15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 5),
    _LCV15MinBucket_Type()
)
lCV15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCV15MinBucket.setStatus("current")
_LCV24HrBucket_Type = Counter32
_LCV24HrBucket_Object = MibTableColumn
lCV24HrBucket = _LCV24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 6),
    _LCV24HrBucket_Type()
)
lCV24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCV24HrBucket.setStatus("current")
_LESCurrent_Type = Counter32
_LESCurrent_Object = MibTableColumn
lESCurrent = _LESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 7),
    _LESCurrent_Type()
)
lESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lESCurrent.setStatus("current")
_LES15MinBucket_Type = Counter32
_LES15MinBucket_Object = MibTableColumn
lES15MinBucket = _LES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 8),
    _LES15MinBucket_Type()
)
lES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lES15MinBucket.setStatus("current")
_LES24HrBucket_Type = Counter32
_LES24HrBucket_Object = MibTableColumn
lES24HrBucket = _LES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 9),
    _LES24HrBucket_Type()
)
lES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lES24HrBucket.setStatus("current")
_LSESCurrent_Type = Counter32
_LSESCurrent_Object = MibTableColumn
lSESCurrent = _LSESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 10),
    _LSESCurrent_Type()
)
lSESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSESCurrent.setStatus("current")
_LSES15MinBucket_Type = Counter32
_LSES15MinBucket_Object = MibTableColumn
lSES15MinBucket = _LSES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 11),
    _LSES15MinBucket_Type()
)
lSES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSES15MinBucket.setStatus("current")
_LSES24HrBucket_Type = Counter32
_LSES24HrBucket_Object = MibTableColumn
lSES24HrBucket = _LSES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 12),
    _LSES24HrBucket_Type()
)
lSES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSES24HrBucket.setStatus("current")
_CRCCurrent_Type = Counter32
_CRCCurrent_Object = MibTableColumn
cRCCurrent = _CRCCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 13),
    _CRCCurrent_Type()
)
cRCCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCCurrent.setStatus("current")
_CRC15MinBucket_Type = Counter32
_CRC15MinBucket_Object = MibTableColumn
cRC15MinBucket = _CRC15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 14),
    _CRC15MinBucket_Type()
)
cRC15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRC15MinBucket.setStatus("current")
_CRC24HrBucket_Type = Counter32
_CRC24HrBucket_Object = MibTableColumn
cRC24HrBucket = _CRC24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 15),
    _CRC24HrBucket_Type()
)
cRC24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRC24HrBucket.setStatus("current")
_CRCESCurrent_Type = Counter32
_CRCESCurrent_Object = MibTableColumn
cRCESCurrent = _CRCESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 16),
    _CRCESCurrent_Type()
)
cRCESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCESCurrent.setStatus("current")
_CRCES15MinBucket_Type = Counter32
_CRCES15MinBucket_Object = MibTableColumn
cRCES15MinBucket = _CRCES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 17),
    _CRCES15MinBucket_Type()
)
cRCES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCES15MinBucket.setStatus("current")
_CRCES24HrBucket_Type = Counter32
_CRCES24HrBucket_Object = MibTableColumn
cRCES24HrBucket = _CRCES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 18),
    _CRCES24HrBucket_Type()
)
cRCES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCES24HrBucket.setStatus("current")
_CRCSESCurrent_Type = Counter32
_CRCSESCurrent_Object = MibTableColumn
cRCSESCurrent = _CRCSESCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 19),
    _CRCSESCurrent_Type()
)
cRCSESCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCSESCurrent.setStatus("current")
_CRCSES15MinBucket_Type = Counter32
_CRCSES15MinBucket_Object = MibTableColumn
cRCSES15MinBucket = _CRCSES15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 20),
    _CRCSES15MinBucket_Type()
)
cRCSES15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCSES15MinBucket.setStatus("current")
_CRCSES24HrBucket_Type = Counter32
_CRCSES24HrBucket_Object = MibTableColumn
cRCSES24HrBucket = _CRCSES24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 21),
    _CRCSES24HrBucket_Type()
)
cRCSES24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCSES24HrBucket.setStatus("current")
_SEFSCurrent_Type = Counter32
_SEFSCurrent_Object = MibTableColumn
sEFSCurrent = _SEFSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 22),
    _SEFSCurrent_Type()
)
sEFSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sEFSCurrent.setStatus("current")
_SEFS15MinBucket_Type = Counter32
_SEFS15MinBucket_Object = MibTableColumn
sEFS15MinBucket = _SEFS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 23),
    _SEFS15MinBucket_Type()
)
sEFS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sEFS15MinBucket.setStatus("current")
_SEFS24HrBucket_Type = Counter32
_SEFS24HrBucket_Object = MibTableColumn
sEFS24HrBucket = _SEFS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 24),
    _SEFS24HrBucket_Type()
)
sEFS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sEFS24HrBucket.setStatus("current")
_AISSCurrent_Type = Counter32
_AISSCurrent_Object = MibTableColumn
aISSCurrent = _AISSCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 25),
    _AISSCurrent_Type()
)
aISSCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aISSCurrent.setStatus("current")
_AISS15MinBucket_Type = Counter32
_AISS15MinBucket_Object = MibTableColumn
aISS15MinBucket = _AISS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 26),
    _AISS15MinBucket_Type()
)
aISS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aISS15MinBucket.setStatus("current")
_AISS24HrBucket_Type = Counter32
_AISS24HrBucket_Object = MibTableColumn
aISS24HrBucket = _AISS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 27),
    _AISS24HrBucket_Type()
)
aISS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aISS24HrBucket.setStatus("current")
_UASCurrent_Type = Counter32
_UASCurrent_Object = MibTableColumn
uASCurrent = _UASCurrent_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 28),
    _UASCurrent_Type()
)
uASCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uASCurrent.setStatus("current")
_UAS15MinBucket_Type = Counter32
_UAS15MinBucket_Object = MibTableColumn
uAS15MinBucket = _UAS15MinBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 29),
    _UAS15MinBucket_Type()
)
uAS15MinBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uAS15MinBucket.setStatus("current")
_UAS24HrBucket_Type = Counter32
_UAS24HrBucket_Object = MibTableColumn
uAS24HrBucket = _UAS24HrBucket_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 30),
    _UAS24HrBucket_Type()
)
uAS24HrBucket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uAS24HrBucket.setStatus("current")


class _PercentEFS_Type(Integer32):
    """Custom type percentEFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PercentEFS_Type.__name__ = "Integer32"
_PercentEFS_Object = MibTableColumn
percentEFS = _PercentEFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 31),
    _PercentEFS_Type()
)
percentEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentEFS.setStatus("current")


class _AlarmClrButton_Type(Integer32):
    """Custom type alarmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_AlarmClrButton_Type.__name__ = "Integer32"
_AlarmClrButton_Object = MibTableColumn
alarmClrButton = _AlarmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 1, 1, 32),
    _AlarmClrButton_Type()
)
alarmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmClrButton.setStatus("current")
_Dsx1CntGrp_ObjectIdentity = ObjectIdentity
dsx1CntGrp = _Dsx1CntGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4)
)
_Dsx1CntGrpTable_Object = MibTable
dsx1CntGrpTable = _Dsx1CntGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dsx1CntGrpTable.setStatus("current")
_Dsx1CntGrpEntry_Object = MibTableRow
dsx1CntGrpEntry = _Dsx1CntGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1)
)
dsx1CntGrpEntry.setIndexNames(
    (0, "CISCO-MGX82XX-DSX1-MIB", "cntLineNum"),
)
if mibBuilder.loadTexts:
    dsx1CntGrpEntry.setStatus("current")


class _CntLineNum_Type(Integer32):
    """Custom type cntLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CntLineNum_Type.__name__ = "Integer32"
_CntLineNum_Object = MibTableColumn
cntLineNum = _CntLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 1),
    _CntLineNum_Type()
)
cntLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cntLineNum.setStatus("current")
_RcvLOSCount_Type = Counter32
_RcvLOSCount_Object = MibTableColumn
rcvLOSCount = _RcvLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 2),
    _RcvLOSCount_Type()
)
rcvLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvLOSCount.setStatus("current")
_RcvOOFCount_Type = Counter32
_RcvOOFCount_Object = MibTableColumn
rcvOOFCount = _RcvOOFCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 3),
    _RcvOOFCount_Type()
)
rcvOOFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvOOFCount.setStatus("current")
_RcvRAICount_Type = Counter32
_RcvRAICount_Object = MibTableColumn
rcvRAICount = _RcvRAICount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 4),
    _RcvRAICount_Type()
)
rcvRAICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvRAICount.setStatus("current")
_RcvFECount_Type = Counter32
_RcvFECount_Object = MibTableColumn
rcvFECount = _RcvFECount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 5),
    _RcvFECount_Type()
)
rcvFECount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFECount.setStatus("current")


class _CounterClearButton_Type(Integer32):
    """Custom type counterClearButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_CounterClearButton_Type.__name__ = "Integer32"
_CounterClearButton_Object = MibTableColumn
counterClearButton = _CounterClearButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 4, 1, 1, 6),
    _CounterClearButton_Type()
)
counterClearButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterClearButton.setStatus("current")
_CmDsx1MIBConformance_ObjectIdentity = ObjectIdentity
cmDsx1MIBConformance = _CmDsx1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2)
)
_CmDsx1MIBGroups_ObjectIdentity = ObjectIdentity
cmDsx1MIBGroups = _CmDsx1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1)
)
_CmDsx1MIBCompliances_ObjectIdentity = ObjectIdentity
cmDsx1MIBCompliances = _CmDsx1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 2)
)

# Managed Objects groups

cmDsx1GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1, 1)
)
cmDsx1GeneralGroup.setObjects(
    ("CISCO-MGX82XX-DSX1-MIB", "lineNumofValidEntries")
)
if mibBuilder.loadTexts:
    cmDsx1GeneralGroup.setStatus("current")

cmDsx1ConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1, 2)
)
cmDsx1ConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX1-MIB", "lineNum"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineConnectorType"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineEnable"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineType"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineCoding"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineLength"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineXmtClockSource"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineLoopbackCommand"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineSendCode"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineLoopbackCodeDetection"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineUsedTimeslotsBitMap"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineBERTEnable"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineBERTPattern"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineBERTResult"),
        ("CISCO-MGX82XX-DSX1-MIB", "bERTResultClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx1ConfGroup.setStatus("current")

cmDsx1CountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1, 3)
)
cmDsx1CountGroup.setObjects(
      *(("CISCO-MGX82XX-DSX1-MIB", "cntLineNum"),
        ("CISCO-MGX82XX-DSX1-MIB", "rcvLOSCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "rcvOOFCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "rcvRAICount"),
        ("CISCO-MGX82XX-DSX1-MIB", "rcvFECount"),
        ("CISCO-MGX82XX-DSX1-MIB", "counterClearButton"))
)
if mibBuilder.loadTexts:
    cmDsx1CountGroup.setStatus("current")

cmDsx1AlarmConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1, 4)
)
cmDsx1AlarmConfGroup.setObjects(
      *(("CISCO-MGX82XX-DSX1-MIB", "almCnfLineNum"),
        ("CISCO-MGX82XX-DSX1-MIB", "redSeverity"),
        ("CISCO-MGX82XX-DSX1-MIB", "rAISeverity"),
        ("CISCO-MGX82XX-DSX1-MIB", "nEAlarmUpCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "nEAlarmDownCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "nEAlarmThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "fEAlarmUpCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "fEAlarmDownCount"),
        ("CISCO-MGX82XX-DSX1-MIB", "fEAlarmThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "statisticalAlarmSeverity"),
        ("CISCO-MGX82XX-DSX1-MIB", "lCV15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "lCV24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "lES15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "lES24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "lSES15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "lSES24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRC15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRC24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCES15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCES24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCSES15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCSES24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "sEFS15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "sEFS24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "aISS15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "aISS24HrThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "uAS15MinThreshold"),
        ("CISCO-MGX82XX-DSX1-MIB", "uAS24HrThreshold"))
)
if mibBuilder.loadTexts:
    cmDsx1AlarmConfGroup.setStatus("current")

cmDsx1AlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 1, 5)
)
cmDsx1AlarmGroup.setObjects(
      *(("CISCO-MGX82XX-DSX1-MIB", "almLineNum"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineAlarmState"),
        ("CISCO-MGX82XX-DSX1-MIB", "lineStatisticalAlarmState"),
        ("CISCO-MGX82XX-DSX1-MIB", "lCVCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "lCV15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "lCV24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "lESCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "lES15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "lES24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "lSESCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "lSES15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "lSES24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRC15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRC24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCESCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCES15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCES24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCSESCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCSES15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "cRCSES24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "sEFSCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "sEFS15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "sEFS24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "aISSCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "aISS15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "aISS24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "uASCurrent"),
        ("CISCO-MGX82XX-DSX1-MIB", "uAS15MinBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "uAS24HrBucket"),
        ("CISCO-MGX82XX-DSX1-MIB", "percentEFS"),
        ("CISCO-MGX82XX-DSX1-MIB", "alarmClrButton"))
)
if mibBuilder.loadTexts:
    cmDsx1AlarmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmDsx1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 58, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cmDsx1Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MGX82XX-DSX1-MIB",
    **{"dsx1CnfGrp": dsx1CnfGrp,
       "dsx1CnfGrpTable": dsx1CnfGrpTable,
       "dsx1CnfGrpEntry": dsx1CnfGrpEntry,
       "lineNum": lineNum,
       "lineConnectorType": lineConnectorType,
       "lineEnable": lineEnable,
       "lineType": lineType,
       "lineCoding": lineCoding,
       "lineLength": lineLength,
       "lineXmtClockSource": lineXmtClockSource,
       "lineLoopbackCommand": lineLoopbackCommand,
       "lineSendCode": lineSendCode,
       "lineUsedTimeslotsBitMap": lineUsedTimeslotsBitMap,
       "lineLoopbackCodeDetection": lineLoopbackCodeDetection,
       "lineBERTEnable": lineBERTEnable,
       "lineBERTPattern": lineBERTPattern,
       "lineBERTResult": lineBERTResult,
       "bERTResultClrButton": bERTResultClrButton,
       "lineNumofValidEntries": lineNumofValidEntries,
       "dsx1AlmCnfGrp": dsx1AlmCnfGrp,
       "dsx1AlmCnfGrpTable": dsx1AlmCnfGrpTable,
       "dsx1AlmCnfGrpEntry": dsx1AlmCnfGrpEntry,
       "almCnfLineNum": almCnfLineNum,
       "redSeverity": redSeverity,
       "rAISeverity": rAISeverity,
       "nEAlarmUpCount": nEAlarmUpCount,
       "nEAlarmDownCount": nEAlarmDownCount,
       "nEAlarmThreshold": nEAlarmThreshold,
       "fEAlarmUpCount": fEAlarmUpCount,
       "fEAlarmDownCount": fEAlarmDownCount,
       "fEAlarmThreshold": fEAlarmThreshold,
       "statisticalAlarmSeverity": statisticalAlarmSeverity,
       "lCV15MinThreshold": lCV15MinThreshold,
       "lCV24HrThreshold": lCV24HrThreshold,
       "lES15MinThreshold": lES15MinThreshold,
       "lES24HrThreshold": lES24HrThreshold,
       "lSES15MinThreshold": lSES15MinThreshold,
       "lSES24HrThreshold": lSES24HrThreshold,
       "cRC15MinThreshold": cRC15MinThreshold,
       "cRC24HrThreshold": cRC24HrThreshold,
       "cRCES15MinThreshold": cRCES15MinThreshold,
       "cRCES24HrThreshold": cRCES24HrThreshold,
       "cRCSES15MinThreshold": cRCSES15MinThreshold,
       "cRCSES24HrThreshold": cRCSES24HrThreshold,
       "sEFS15MinThreshold": sEFS15MinThreshold,
       "sEFS24HrThreshold": sEFS24HrThreshold,
       "aISS15MinThreshold": aISS15MinThreshold,
       "aISS24HrThreshold": aISS24HrThreshold,
       "uAS15MinThreshold": uAS15MinThreshold,
       "uAS24HrThreshold": uAS24HrThreshold,
       "dsx1AlmGrp": dsx1AlmGrp,
       "dsx1AlmGrpTable": dsx1AlmGrpTable,
       "dsx1AlmGrpEntry": dsx1AlmGrpEntry,
       "almLineNum": almLineNum,
       "lineAlarmState": lineAlarmState,
       "lineStatisticalAlarmState": lineStatisticalAlarmState,
       "lCVCurrent": lCVCurrent,
       "lCV15MinBucket": lCV15MinBucket,
       "lCV24HrBucket": lCV24HrBucket,
       "lESCurrent": lESCurrent,
       "lES15MinBucket": lES15MinBucket,
       "lES24HrBucket": lES24HrBucket,
       "lSESCurrent": lSESCurrent,
       "lSES15MinBucket": lSES15MinBucket,
       "lSES24HrBucket": lSES24HrBucket,
       "cRCCurrent": cRCCurrent,
       "cRC15MinBucket": cRC15MinBucket,
       "cRC24HrBucket": cRC24HrBucket,
       "cRCESCurrent": cRCESCurrent,
       "cRCES15MinBucket": cRCES15MinBucket,
       "cRCES24HrBucket": cRCES24HrBucket,
       "cRCSESCurrent": cRCSESCurrent,
       "cRCSES15MinBucket": cRCSES15MinBucket,
       "cRCSES24HrBucket": cRCSES24HrBucket,
       "sEFSCurrent": sEFSCurrent,
       "sEFS15MinBucket": sEFS15MinBucket,
       "sEFS24HrBucket": sEFS24HrBucket,
       "aISSCurrent": aISSCurrent,
       "aISS15MinBucket": aISS15MinBucket,
       "aISS24HrBucket": aISS24HrBucket,
       "uASCurrent": uASCurrent,
       "uAS15MinBucket": uAS15MinBucket,
       "uAS24HrBucket": uAS24HrBucket,
       "percentEFS": percentEFS,
       "alarmClrButton": alarmClrButton,
       "dsx1CntGrp": dsx1CntGrp,
       "dsx1CntGrpTable": dsx1CntGrpTable,
       "dsx1CntGrpEntry": dsx1CntGrpEntry,
       "cntLineNum": cntLineNum,
       "rcvLOSCount": rcvLOSCount,
       "rcvOOFCount": rcvOOFCount,
       "rcvRAICount": rcvRAICount,
       "rcvFECount": rcvFECount,
       "counterClearButton": counterClearButton,
       "ciscoMgx82xxDsx1MIB": ciscoMgx82xxDsx1MIB,
       "cmDsx1MIBConformance": cmDsx1MIBConformance,
       "cmDsx1MIBGroups": cmDsx1MIBGroups,
       "cmDsx1GeneralGroup": cmDsx1GeneralGroup,
       "cmDsx1ConfGroup": cmDsx1ConfGroup,
       "cmDsx1CountGroup": cmDsx1CountGroup,
       "cmDsx1AlarmConfGroup": cmDsx1AlarmConfGroup,
       "cmDsx1AlarmGroup": cmDsx1AlarmGroup,
       "cmDsx1MIBCompliances": cmDsx1MIBCompliances,
       "cmDsx1Compliance": cmDsx1Compliance}
)
