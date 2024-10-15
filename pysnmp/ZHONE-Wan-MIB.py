# SNMP MIB module (ZHONE-Wan-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-Wan-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:48 2024
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

(InterfaceIndex,
 ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(zhoneDsx,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneDsx")

(ZhoneAdminString,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString")


# MODULE-IDENTITY

zhoneDs1Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 1)
)
zhoneDs1Mib.setRevisions(
        ("2009-07-23 11:15",
         "2009-05-12 07:38",
         "2008-11-10 08:58",
         "2006-05-12 12:46",
         "2004-02-05 11:47",
         "2004-01-21 15:36",
         "2003-05-15 13:15",
         "2003-02-04 13:12",
         "2001-10-22 10:04",
         "2001-08-22 13:50",
         "2001-08-14 16:24",
         "2001-08-09 10:07",
         "2001-01-18 13:28",
         "2001-01-04 11:19",
         "2000-11-13 11:30",
         "2000-09-21 10:27",
         "2000-09-12 13:59")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneDs1Table_Object = MibTable
zhoneDs1Table = _ZhoneDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2)
)
if mibBuilder.loadTexts:
    zhoneDs1Table.setStatus("current")
_ZhoneDs1Entry_Object = MibTableRow
zhoneDs1Entry = _ZhoneDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1)
)
zhoneDs1Entry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneLineIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1Entry.setStatus("current")
_ZhoneLineIndex_Type = InterfaceIndex
_ZhoneLineIndex_Object = MibTableColumn
zhoneLineIndex = _ZhoneLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 1),
    _ZhoneLineIndex_Type()
)
zhoneLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneLineIndex.setStatus("current")


class _ZhoneTimeElapsed_Type(Integer32):
    """Custom type zhoneTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ZhoneTimeElapsed_Type.__name__ = "Integer32"
_ZhoneTimeElapsed_Object = MibTableColumn
zhoneTimeElapsed = _ZhoneTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 2),
    _ZhoneTimeElapsed_Type()
)
zhoneTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTimeElapsed.setStatus("current")


class _ZhoneValidIntervals_Type(Integer32):
    """Custom type zhoneValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneValidIntervals_Type.__name__ = "Integer32"
_ZhoneValidIntervals_Object = MibTableColumn
zhoneValidIntervals = _ZhoneValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 3),
    _ZhoneValidIntervals_Type()
)
zhoneValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneValidIntervals.setStatus("current")


class _ZhoneLineType_Type(Integer32):
    """Custom type zhoneLineType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("ds1Unframed", 10),
          ("e1", 5),
          ("e1Crc", 6),
          ("e1CrcMf", 8),
          ("e1Mf", 7),
          ("e1Unframed", 9),
          ("esf", 2),
          ("other", 1),
          ("slc96", 4))
    )


_ZhoneLineType_Type.__name__ = "Integer32"
_ZhoneLineType_Object = MibTableColumn
zhoneLineType = _ZhoneLineType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 4),
    _ZhoneLineType_Type()
)
zhoneLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneLineType.setStatus("current")


class _ZhoneLineCoding_Type(Integer32):
    """Custom type zhoneLineCoding based on Integer32"""
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
        *(("ami", 5),
          ("b6zs", 7),
          ("b8zs", 2),
          ("hdb3", 3),
          ("jbzs", 1),
          ("other", 6),
          ("zbtsi", 4))
    )


_ZhoneLineCoding_Type.__name__ = "Integer32"
_ZhoneLineCoding_Object = MibTableColumn
zhoneLineCoding = _ZhoneLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 5),
    _ZhoneLineCoding_Type()
)
zhoneLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneLineCoding.setStatus("current")


class _ZhoneSendCode_Type(Integer32):
    """Custom type zhoneSendCode based on Integer32"""
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
        *(("send1in2Pattern", 10),
          ("send2047Pattern", 9),
          ("send2ToPower11Minus1Pattern", 16),
          ("send2ToPower15Minus1Pattern", 17),
          ("send2ToPower20Minus1Pattern", 18),
          ("send2ToPower23Minus1Pattern", 19),
          ("send2ToPower9Minus1Pattern", 15),
          ("send3in24Pattern", 7),
          ("send511Pattern", 6),
          ("sendInbandCode", 11),
          ("sendInbandCodeOff", 12),
          ("sendLineCode", 2),
          ("sendLineCodeOff", 13),
          ("sendNoCode", 1),
          ("sendOtherTestPattern", 8),
          ("sendPayloadCode", 3),
          ("sendPayloadCodeOff", 14),
          ("sendQRSSPattern", 5),
          ("sendResetCode", 4))
    )


_ZhoneSendCode_Type.__name__ = "Integer32"
_ZhoneSendCode_Object = MibTableColumn
zhoneSendCode = _ZhoneSendCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 6),
    _ZhoneSendCode_Type()
)
zhoneSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSendCode.setStatus("current")
_ZhoneCircuitIdentifier_Type = ZhoneAdminString
_ZhoneCircuitIdentifier_Object = MibTableColumn
zhoneCircuitIdentifier = _ZhoneCircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 7),
    _ZhoneCircuitIdentifier_Type()
)
zhoneCircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCircuitIdentifier.setStatus("current")


class _ZhoneLoopbackConfig_Type(Integer32):
    """Custom type zhoneLoopbackConfig based on Integer32"""
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
        *(("lineLoop", 2),
          ("localLoop", 3),
          ("noLoop", 1),
          ("payloadLoop", 4))
    )


_ZhoneLoopbackConfig_Type.__name__ = "Integer32"
_ZhoneLoopbackConfig_Object = MibTableColumn
zhoneLoopbackConfig = _ZhoneLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 8),
    _ZhoneLoopbackConfig_Type()
)
zhoneLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneLoopbackConfig.setStatus("current")


class _ZhoneLineStatus_Type(Integer32):
    """Custom type zhoneLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_ZhoneLineStatus_Type.__name__ = "Integer32"
_ZhoneLineStatus_Object = MibTableColumn
zhoneLineStatus = _ZhoneLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 9),
    _ZhoneLineStatus_Type()
)
zhoneLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLineStatus.setStatus("current")


class _ZhoneSignalMode_Type(Integer32):
    """Custom type zhoneSignalMode based on Integer32"""
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
        *(("bitOriented", 3),
          ("messageOriented", 4),
          ("none", 1),
          ("other", 5),
          ("robbedBit", 2))
    )


_ZhoneSignalMode_Type.__name__ = "Integer32"
_ZhoneSignalMode_Object = MibTableColumn
zhoneSignalMode = _ZhoneSignalMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 10),
    _ZhoneSignalMode_Type()
)
zhoneSignalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneSignalMode.setStatus("current")


class _ZhoneTransmitClockSource_Type(Integer32):
    """Custom type zhoneTransmitClockSource based on Integer32"""
    defaultValue = 3

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
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("sonetThroughTiming", 4),
          ("throughTiming", 3))
    )


_ZhoneTransmitClockSource_Type.__name__ = "Integer32"
_ZhoneTransmitClockSource_Object = MibTableColumn
zhoneTransmitClockSource = _ZhoneTransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 11),
    _ZhoneTransmitClockSource_Type()
)
zhoneTransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneTransmitClockSource.setStatus("current")


class _ZhoneFdl_Type(Integer32):
    """Custom type zhoneFdl based on Integer32"""
    defaultValue = 4

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
        *(("ansiT1403", 2),
          ("att54016", 3),
          ("fdlNone", 4),
          ("other", 1))
    )


_ZhoneFdl_Type.__name__ = "Integer32"
_ZhoneFdl_Object = MibTableColumn
zhoneFdl = _ZhoneFdl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 12),
    _ZhoneFdl_Type()
)
zhoneFdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneFdl.setStatus("current")


class _ZhoneInvalidIntervals_Type(Integer32):
    """Custom type zhoneInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneInvalidIntervals_Object = MibTableColumn
zhoneInvalidIntervals = _ZhoneInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 13),
    _ZhoneInvalidIntervals_Type()
)
zhoneInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneInvalidIntervals.setStatus("current")


class _ZhoneDsxLineLength_Type(Integer32):
    """Custom type zhoneDsxLineLength based on Integer32"""
    defaultValue = 1

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
        *(("dsx0", 1),
          ("dsx133", 2),
          ("dsx266", 3),
          ("dsx399", 4),
          ("dsx533", 5),
          ("dsx655", 6))
    )


_ZhoneDsxLineLength_Type.__name__ = "Integer32"
_ZhoneDsxLineLength_Object = MibTableColumn
zhoneDsxLineLength = _ZhoneDsxLineLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 14),
    _ZhoneDsxLineLength_Type()
)
zhoneDsxLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDsxLineLength.setStatus("current")
_ZhoneLineStatusLastChange_Type = TimeStamp
_ZhoneLineStatusLastChange_Object = MibTableColumn
zhoneLineStatusLastChange = _ZhoneLineStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 15),
    _ZhoneLineStatusLastChange_Type()
)
zhoneLineStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLineStatusLastChange.setStatus("current")


class _ZhoneLineStatusChangeTrapEnable_Type(Integer32):
    """Custom type zhoneLineStatusChangeTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneLineStatusChangeTrapEnable_Type.__name__ = "Integer32"
_ZhoneLineStatusChangeTrapEnable_Object = MibTableColumn
zhoneLineStatusChangeTrapEnable = _ZhoneLineStatusChangeTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 16),
    _ZhoneLineStatusChangeTrapEnable_Type()
)
zhoneLineStatusChangeTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneLineStatusChangeTrapEnable.setStatus("current")


class _ZhoneLoopbackStatus_Type(Integer32):
    """Custom type zhoneLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_ZhoneLoopbackStatus_Type.__name__ = "Integer32"
_ZhoneLoopbackStatus_Object = MibTableColumn
zhoneLoopbackStatus = _ZhoneLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 17),
    _ZhoneLoopbackStatus_Type()
)
zhoneLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLoopbackStatus.setStatus("current")


class _ZhoneDs1ChannelNumber_Type(Integer32):
    """Custom type zhoneDs1ChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_ZhoneDs1ChannelNumber_Type.__name__ = "Integer32"
_ZhoneDs1ChannelNumber_Object = MibTableColumn
zhoneDs1ChannelNumber = _ZhoneDs1ChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 18),
    _ZhoneDs1ChannelNumber_Type()
)
zhoneDs1ChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDs1ChannelNumber.setStatus("current")


class _ZhoneChannelization_Type(Integer32):
    """Custom type zhoneChannelization based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledDs0", 2),
          ("enabledDs1", 3))
    )


_ZhoneChannelization_Type.__name__ = "Integer32"
_ZhoneChannelization_Object = MibTableColumn
zhoneChannelization = _ZhoneChannelization_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 19),
    _ZhoneChannelization_Type()
)
zhoneChannelization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneChannelization.setStatus("current")


class _ZhoneDs1Mode_Type(Integer32):
    """Custom type zhoneDs1Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("csu", 3),
          ("dsx", 2),
          ("other", 1))
    )


_ZhoneDs1Mode_Type.__name__ = "Integer32"
_ZhoneDs1Mode_Object = MibTableColumn
zhoneDs1Mode = _ZhoneDs1Mode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 20),
    _ZhoneDs1Mode_Type()
)
zhoneDs1Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1Mode.setStatus("current")


class _ZhoneCsuLineLength_Type(Integer32):
    """Custom type zhoneCsuLineLength based on Integer32"""
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
        *(("csu00", 1),
          ("csu150", 3),
          ("csu225", 4),
          ("csu75", 2))
    )


_ZhoneCsuLineLength_Type.__name__ = "Integer32"
_ZhoneCsuLineLength_Object = MibTableColumn
zhoneCsuLineLength = _ZhoneCsuLineLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 21),
    _ZhoneCsuLineLength_Type()
)
zhoneCsuLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCsuLineLength.setStatus("current")


class _ZhoneClockSourceEligibility_Type(Integer32):
    """Custom type zhoneClockSourceEligibility based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 2),
          ("notEligible", 1))
    )


_ZhoneClockSourceEligibility_Type.__name__ = "Integer32"
_ZhoneClockSourceEligibility_Object = MibTableColumn
zhoneClockSourceEligibility = _ZhoneClockSourceEligibility_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 22),
    _ZhoneClockSourceEligibility_Type()
)
zhoneClockSourceEligibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneClockSourceEligibility.setStatus("current")


class _ZhoneCellScramble_Type(TruthValue):
    """Custom type zhoneCellScramble based on TruthValue"""


_ZhoneCellScramble_Object = MibTableColumn
zhoneCellScramble = _ZhoneCellScramble_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 23),
    _ZhoneCellScramble_Type()
)
zhoneCellScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCellScramble.setStatus("current")
_ZhoneCosetPolynomial_Type = TruthValue
_ZhoneCosetPolynomial_Object = MibTableColumn
zhoneCosetPolynomial = _ZhoneCosetPolynomial_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 24),
    _ZhoneCosetPolynomial_Type()
)
zhoneCosetPolynomial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneCosetPolynomial.setStatus("current")


class _ZhoneDs1ProtocolEmulation_Type(Integer32):
    """Custom type zhoneDs1ProtocolEmulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpe", 2),
          ("network", 1))
    )


_ZhoneDs1ProtocolEmulation_Type.__name__ = "Integer32"
_ZhoneDs1ProtocolEmulation_Object = MibTableColumn
zhoneDs1ProtocolEmulation = _ZhoneDs1ProtocolEmulation_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 25),
    _ZhoneDs1ProtocolEmulation_Type()
)
zhoneDs1ProtocolEmulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1ProtocolEmulation.setStatus("current")


class _ZhoneDs1SignalType_Type(Integer32):
    """Custom type zhoneDs1SignalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("groundStart", 2),
          ("loopStart", 1))
    )


_ZhoneDs1SignalType_Type.__name__ = "Integer32"
_ZhoneDs1SignalType_Object = MibTableColumn
zhoneDs1SignalType = _ZhoneDs1SignalType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 26),
    _ZhoneDs1SignalType_Type()
)
zhoneDs1SignalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1SignalType.setStatus("current")


class _ZhoneDs1GroupIndex_Type(Integer32):
    """Custom type zhoneDs1GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneDs1GroupIndex_Type.__name__ = "Integer32"
_ZhoneDs1GroupIndex_Object = MibTableColumn
zhoneDs1GroupIndex = _ZhoneDs1GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 27),
    _ZhoneDs1GroupIndex_Type()
)
zhoneDs1GroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1GroupIndex.setStatus("current")


class _ZhoneDs1LinePower_Type(Integer32):
    """Custom type zhoneDs1LinePower based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ZhoneDs1LinePower_Type.__name__ = "Integer32"
_ZhoneDs1LinePower_Object = MibTableColumn
zhoneDs1LinePower = _ZhoneDs1LinePower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 28),
    _ZhoneDs1LinePower_Type()
)
zhoneDs1LinePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1LinePower.setStatus("current")


class _ZhoneDs1TimeslotAssignment_Type(Bits):
    """Custom type zhoneDs1TimeslotAssignment based on Bits"""
    namedValues = NamedValues(
        *(("ts0", 0),
          ("ts1", 1),
          ("ts10", 10),
          ("ts11", 11),
          ("ts12", 12),
          ("ts13", 13),
          ("ts14", 14),
          ("ts15", 15),
          ("ts16", 16),
          ("ts17", 17),
          ("ts18", 18),
          ("ts19", 19),
          ("ts2", 2),
          ("ts20", 20),
          ("ts21", 21),
          ("ts22", 22),
          ("ts23", 23),
          ("ts24", 24),
          ("ts25", 25),
          ("ts26", 26),
          ("ts27", 27),
          ("ts28", 28),
          ("ts29", 29),
          ("ts3", 3),
          ("ts30", 30),
          ("ts31", 31),
          ("ts4", 4),
          ("ts5", 5),
          ("ts6", 6),
          ("ts7", 7),
          ("ts8", 8),
          ("ts9", 9))
    )

_ZhoneDs1TimeslotAssignment_Type.__name__ = "Bits"
_ZhoneDs1TimeslotAssignment_Object = MibTableColumn
zhoneDs1TimeslotAssignment = _ZhoneDs1TimeslotAssignment_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 29),
    _ZhoneDs1TimeslotAssignment_Type()
)
zhoneDs1TimeslotAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1TimeslotAssignment.setStatus("current")


class _ZhoneDs1TxClockRecovery_Type(Integer32):
    """Custom type zhoneDs1TxClockRecovery based on Integer32"""
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
        *(("adaptive", 2),
          ("differential", 3),
          ("none", 1))
    )


_ZhoneDs1TxClockRecovery_Type.__name__ = "Integer32"
_ZhoneDs1TxClockRecovery_Object = MibTableColumn
zhoneDs1TxClockRecovery = _ZhoneDs1TxClockRecovery_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 30),
    _ZhoneDs1TxClockRecovery_Type()
)
zhoneDs1TxClockRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1TxClockRecovery.setStatus("obsolete")


class _ZhoneDs1TxClockAdaptiveQuality_Type(Integer32):
    """Custom type zhoneDs1TxClockAdaptiveQuality based on Integer32"""
    defaultValue = 2

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
        *(("stratum1", 1),
          ("stratum3", 2),
          ("stratum3e", 3),
          ("stratum4", 4))
    )


_ZhoneDs1TxClockAdaptiveQuality_Type.__name__ = "Integer32"
_ZhoneDs1TxClockAdaptiveQuality_Object = MibTableColumn
zhoneDs1TxClockAdaptiveQuality = _ZhoneDs1TxClockAdaptiveQuality_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 2, 1, 31),
    _ZhoneDs1TxClockAdaptiveQuality_Type()
)
zhoneDs1TxClockAdaptiveQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneDs1TxClockAdaptiveQuality.setStatus("current")
_ZhoneDs1CurrentTable_Object = MibTable
zhoneDs1CurrentTable = _ZhoneDs1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3)
)
if mibBuilder.loadTexts:
    zhoneDs1CurrentTable.setStatus("current")
_ZhoneDs1CurrentEntry_Object = MibTableRow
zhoneDs1CurrentEntry = _ZhoneDs1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1)
)
zhoneDs1CurrentEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneCurrentIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1CurrentEntry.setStatus("current")
_ZhoneCurrentIndex_Type = InterfaceIndex
_ZhoneCurrentIndex_Object = MibTableColumn
zhoneCurrentIndex = _ZhoneCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 1),
    _ZhoneCurrentIndex_Type()
)
zhoneCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneCurrentIndex.setStatus("current")
_ZhoneCurrentESs_Type = PerfCurrentCount
_ZhoneCurrentESs_Object = MibTableColumn
zhoneCurrentESs = _ZhoneCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 2),
    _ZhoneCurrentESs_Type()
)
zhoneCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentESs.setStatus("current")
_ZhoneCurrentSESs_Type = PerfCurrentCount
_ZhoneCurrentSESs_Object = MibTableColumn
zhoneCurrentSESs = _ZhoneCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 3),
    _ZhoneCurrentSESs_Type()
)
zhoneCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentSESs.setStatus("current")
_ZhoneCurrentSEFSs_Type = PerfCurrentCount
_ZhoneCurrentSEFSs_Object = MibTableColumn
zhoneCurrentSEFSs = _ZhoneCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 4),
    _ZhoneCurrentSEFSs_Type()
)
zhoneCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentSEFSs.setStatus("current")
_ZhoneCurrentUASs_Type = PerfCurrentCount
_ZhoneCurrentUASs_Object = MibTableColumn
zhoneCurrentUASs = _ZhoneCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 5),
    _ZhoneCurrentUASs_Type()
)
zhoneCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentUASs.setStatus("current")
_ZhoneCurrentCSSs_Type = PerfCurrentCount
_ZhoneCurrentCSSs_Object = MibTableColumn
zhoneCurrentCSSs = _ZhoneCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 6),
    _ZhoneCurrentCSSs_Type()
)
zhoneCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentCSSs.setStatus("current")
_ZhoneCurrentPCVs_Type = PerfCurrentCount
_ZhoneCurrentPCVs_Object = MibTableColumn
zhoneCurrentPCVs = _ZhoneCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 7),
    _ZhoneCurrentPCVs_Type()
)
zhoneCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentPCVs.setStatus("current")
_ZhoneCurrentLESs_Type = PerfCurrentCount
_ZhoneCurrentLESs_Object = MibTableColumn
zhoneCurrentLESs = _ZhoneCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 8),
    _ZhoneCurrentLESs_Type()
)
zhoneCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentLESs.setStatus("current")
_ZhoneCurrentBESs_Type = PerfCurrentCount
_ZhoneCurrentBESs_Object = MibTableColumn
zhoneCurrentBESs = _ZhoneCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 9),
    _ZhoneCurrentBESs_Type()
)
zhoneCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentBESs.setStatus("current")
_ZhoneCurrentDMs_Type = PerfCurrentCount
_ZhoneCurrentDMs_Object = MibTableColumn
zhoneCurrentDMs = _ZhoneCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 10),
    _ZhoneCurrentDMs_Type()
)
zhoneCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentDMs.setStatus("current")
_ZhoneCurrentLCVs_Type = PerfCurrentCount
_ZhoneCurrentLCVs_Object = MibTableColumn
zhoneCurrentLCVs = _ZhoneCurrentLCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 3, 1, 11),
    _ZhoneCurrentLCVs_Type()
)
zhoneCurrentLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneCurrentLCVs.setStatus("current")
_ZhoneDs1IntervalTable_Object = MibTable
zhoneDs1IntervalTable = _ZhoneDs1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4)
)
if mibBuilder.loadTexts:
    zhoneDs1IntervalTable.setStatus("current")
_ZhoneDs1IntervalEntry_Object = MibTableRow
zhoneDs1IntervalEntry = _ZhoneDs1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1)
)
zhoneDs1IntervalEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneIntervalIndex"),
    (0, "ZHONE-Wan-MIB", "zhoneIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneDs1IntervalEntry.setStatus("current")
_ZhoneIntervalIndex_Type = InterfaceIndex
_ZhoneIntervalIndex_Object = MibTableColumn
zhoneIntervalIndex = _ZhoneIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 1),
    _ZhoneIntervalIndex_Type()
)
zhoneIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneIntervalIndex.setStatus("current")


class _ZhoneIntervalNumber_Type(Integer32):
    """Custom type zhoneIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZhoneIntervalNumber_Type.__name__ = "Integer32"
_ZhoneIntervalNumber_Object = MibTableColumn
zhoneIntervalNumber = _ZhoneIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 2),
    _ZhoneIntervalNumber_Type()
)
zhoneIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalNumber.setStatus("current")
_ZhoneIntervalESs_Type = PerfIntervalCount
_ZhoneIntervalESs_Object = MibTableColumn
zhoneIntervalESs = _ZhoneIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 3),
    _ZhoneIntervalESs_Type()
)
zhoneIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalESs.setStatus("current")
_ZhoneIntervalSESs_Type = PerfIntervalCount
_ZhoneIntervalSESs_Object = MibTableColumn
zhoneIntervalSESs = _ZhoneIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 4),
    _ZhoneIntervalSESs_Type()
)
zhoneIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalSESs.setStatus("current")
_ZhoneIntervalSEFSs_Type = PerfIntervalCount
_ZhoneIntervalSEFSs_Object = MibTableColumn
zhoneIntervalSEFSs = _ZhoneIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 5),
    _ZhoneIntervalSEFSs_Type()
)
zhoneIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalSEFSs.setStatus("current")
_ZhoneIntervalUASs_Type = PerfIntervalCount
_ZhoneIntervalUASs_Object = MibTableColumn
zhoneIntervalUASs = _ZhoneIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 6),
    _ZhoneIntervalUASs_Type()
)
zhoneIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalUASs.setStatus("current")
_ZhoneIntervalCSSs_Type = PerfIntervalCount
_ZhoneIntervalCSSs_Object = MibTableColumn
zhoneIntervalCSSs = _ZhoneIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 7),
    _ZhoneIntervalCSSs_Type()
)
zhoneIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalCSSs.setStatus("current")
_ZhoneIntervalPCVs_Type = PerfIntervalCount
_ZhoneIntervalPCVs_Object = MibTableColumn
zhoneIntervalPCVs = _ZhoneIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 8),
    _ZhoneIntervalPCVs_Type()
)
zhoneIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalPCVs.setStatus("current")
_ZhoneIntervalLESs_Type = PerfIntervalCount
_ZhoneIntervalLESs_Object = MibTableColumn
zhoneIntervalLESs = _ZhoneIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 9),
    _ZhoneIntervalLESs_Type()
)
zhoneIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalLESs.setStatus("current")
_ZhoneIntervalBESs_Type = PerfIntervalCount
_ZhoneIntervalBESs_Object = MibTableColumn
zhoneIntervalBESs = _ZhoneIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 10),
    _ZhoneIntervalBESs_Type()
)
zhoneIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalBESs.setStatus("current")
_ZhoneIntervalDMs_Type = PerfIntervalCount
_ZhoneIntervalDMs_Object = MibTableColumn
zhoneIntervalDMs = _ZhoneIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 11),
    _ZhoneIntervalDMs_Type()
)
zhoneIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalDMs.setStatus("current")
_ZhoneIntervalLCVs_Type = PerfIntervalCount
_ZhoneIntervalLCVs_Object = MibTableColumn
zhoneIntervalLCVs = _ZhoneIntervalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 12),
    _ZhoneIntervalLCVs_Type()
)
zhoneIntervalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalLCVs.setStatus("current")
_ZhoneIntervalValidData_Type = TruthValue
_ZhoneIntervalValidData_Object = MibTableColumn
zhoneIntervalValidData = _ZhoneIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 4, 1, 13),
    _ZhoneIntervalValidData_Type()
)
zhoneIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneIntervalValidData.setStatus("current")
_ZhoneDs1TotalTable_Object = MibTable
zhoneDs1TotalTable = _ZhoneDs1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5)
)
if mibBuilder.loadTexts:
    zhoneDs1TotalTable.setStatus("current")
_ZhoneDs1TotalEntry_Object = MibTableRow
zhoneDs1TotalEntry = _ZhoneDs1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1)
)
zhoneDs1TotalEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneTotalIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1TotalEntry.setStatus("current")
_ZhoneTotalIndex_Type = InterfaceIndex
_ZhoneTotalIndex_Object = MibTableColumn
zhoneTotalIndex = _ZhoneTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 1),
    _ZhoneTotalIndex_Type()
)
zhoneTotalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneTotalIndex.setStatus("current")
_ZhoneTotalESs_Type = PerfTotalCount
_ZhoneTotalESs_Object = MibTableColumn
zhoneTotalESs = _ZhoneTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 2),
    _ZhoneTotalESs_Type()
)
zhoneTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalESs.setStatus("current")
_ZhoneTotalSESs_Type = PerfTotalCount
_ZhoneTotalSESs_Object = MibTableColumn
zhoneTotalSESs = _ZhoneTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 3),
    _ZhoneTotalSESs_Type()
)
zhoneTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalSESs.setStatus("current")
_ZhoneTotalSEFSs_Type = PerfTotalCount
_ZhoneTotalSEFSs_Object = MibTableColumn
zhoneTotalSEFSs = _ZhoneTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 4),
    _ZhoneTotalSEFSs_Type()
)
zhoneTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalSEFSs.setStatus("current")
_ZhoneTotalUASs_Type = PerfTotalCount
_ZhoneTotalUASs_Object = MibTableColumn
zhoneTotalUASs = _ZhoneTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 5),
    _ZhoneTotalUASs_Type()
)
zhoneTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalUASs.setStatus("current")
_ZhoneTotalCSSs_Type = PerfTotalCount
_ZhoneTotalCSSs_Object = MibTableColumn
zhoneTotalCSSs = _ZhoneTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 6),
    _ZhoneTotalCSSs_Type()
)
zhoneTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalCSSs.setStatus("current")
_ZhoneTotalPCVs_Type = PerfTotalCount
_ZhoneTotalPCVs_Object = MibTableColumn
zhoneTotalPCVs = _ZhoneTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 7),
    _ZhoneTotalPCVs_Type()
)
zhoneTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalPCVs.setStatus("current")
_ZhoneTotalLESs_Type = PerfTotalCount
_ZhoneTotalLESs_Object = MibTableColumn
zhoneTotalLESs = _ZhoneTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 8),
    _ZhoneTotalLESs_Type()
)
zhoneTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalLESs.setStatus("current")
_ZhoneTotalBESs_Type = PerfTotalCount
_ZhoneTotalBESs_Object = MibTableColumn
zhoneTotalBESs = _ZhoneTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 9),
    _ZhoneTotalBESs_Type()
)
zhoneTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalBESs.setStatus("current")
_ZhoneTotalDMs_Type = PerfTotalCount
_ZhoneTotalDMs_Object = MibTableColumn
zhoneTotalDMs = _ZhoneTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 10),
    _ZhoneTotalDMs_Type()
)
zhoneTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalDMs.setStatus("current")
_ZhoneTotalLCVs_Type = PerfTotalCount
_ZhoneTotalLCVs_Object = MibTableColumn
zhoneTotalLCVs = _ZhoneTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 5, 1, 11),
    _ZhoneTotalLCVs_Type()
)
zhoneTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneTotalLCVs.setStatus("current")
_ZhoneDs1FarEndCurrentTable_Object = MibTable
zhoneDs1FarEndCurrentTable = _ZhoneDs1FarEndCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6)
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndCurrentTable.setStatus("current")
_ZhoneDs1FarEndCurrentEntry_Object = MibTableRow
zhoneDs1FarEndCurrentEntry = _ZhoneDs1FarEndCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1)
)
zhoneDs1FarEndCurrentEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneFarEndCurrentIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndCurrentEntry.setStatus("current")
_ZhoneFarEndCurrentIndex_Type = InterfaceIndex
_ZhoneFarEndCurrentIndex_Object = MibTableColumn
zhoneFarEndCurrentIndex = _ZhoneFarEndCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 1),
    _ZhoneFarEndCurrentIndex_Type()
)
zhoneFarEndCurrentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentIndex.setStatus("current")


class _ZhoneFarEndTimeElapsed_Type(Integer32):
    """Custom type zhoneFarEndTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ZhoneFarEndTimeElapsed_Type.__name__ = "Integer32"
_ZhoneFarEndTimeElapsed_Object = MibTableColumn
zhoneFarEndTimeElapsed = _ZhoneFarEndTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 2),
    _ZhoneFarEndTimeElapsed_Type()
)
zhoneFarEndTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTimeElapsed.setStatus("current")


class _ZhoneFarEndValidIntervals_Type(Integer32):
    """Custom type zhoneFarEndValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneFarEndValidIntervals_Type.__name__ = "Integer32"
_ZhoneFarEndValidIntervals_Object = MibTableColumn
zhoneFarEndValidIntervals = _ZhoneFarEndValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 3),
    _ZhoneFarEndValidIntervals_Type()
)
zhoneFarEndValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndValidIntervals.setStatus("current")
_ZhoneFarEndCurrentESs_Type = PerfCurrentCount
_ZhoneFarEndCurrentESs_Object = MibTableColumn
zhoneFarEndCurrentESs = _ZhoneFarEndCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 4),
    _ZhoneFarEndCurrentESs_Type()
)
zhoneFarEndCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentESs.setStatus("current")
_ZhoneFarEndCurrentSESs_Type = PerfCurrentCount
_ZhoneFarEndCurrentSESs_Object = MibTableColumn
zhoneFarEndCurrentSESs = _ZhoneFarEndCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 5),
    _ZhoneFarEndCurrentSESs_Type()
)
zhoneFarEndCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentSESs.setStatus("current")
_ZhoneFarEndCurrentSEFSs_Type = PerfCurrentCount
_ZhoneFarEndCurrentSEFSs_Object = MibTableColumn
zhoneFarEndCurrentSEFSs = _ZhoneFarEndCurrentSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 6),
    _ZhoneFarEndCurrentSEFSs_Type()
)
zhoneFarEndCurrentSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentSEFSs.setStatus("current")
_ZhoneFarEndCurrentUASs_Type = PerfCurrentCount
_ZhoneFarEndCurrentUASs_Object = MibTableColumn
zhoneFarEndCurrentUASs = _ZhoneFarEndCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 7),
    _ZhoneFarEndCurrentUASs_Type()
)
zhoneFarEndCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentUASs.setStatus("current")
_ZhoneFarEndCurrentCSSs_Type = PerfCurrentCount
_ZhoneFarEndCurrentCSSs_Object = MibTableColumn
zhoneFarEndCurrentCSSs = _ZhoneFarEndCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 8),
    _ZhoneFarEndCurrentCSSs_Type()
)
zhoneFarEndCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentCSSs.setStatus("current")
_ZhoneFarEndCurrentLESs_Type = PerfCurrentCount
_ZhoneFarEndCurrentLESs_Object = MibTableColumn
zhoneFarEndCurrentLESs = _ZhoneFarEndCurrentLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 9),
    _ZhoneFarEndCurrentLESs_Type()
)
zhoneFarEndCurrentLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentLESs.setStatus("current")
_ZhoneFarEndCurrentPCVs_Type = PerfCurrentCount
_ZhoneFarEndCurrentPCVs_Object = MibTableColumn
zhoneFarEndCurrentPCVs = _ZhoneFarEndCurrentPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 10),
    _ZhoneFarEndCurrentPCVs_Type()
)
zhoneFarEndCurrentPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentPCVs.setStatus("current")
_ZhoneFarEndCurrentBESs_Type = PerfCurrentCount
_ZhoneFarEndCurrentBESs_Object = MibTableColumn
zhoneFarEndCurrentBESs = _ZhoneFarEndCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 11),
    _ZhoneFarEndCurrentBESs_Type()
)
zhoneFarEndCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentBESs.setStatus("current")
_ZhoneFarEndCurrentDMs_Type = PerfCurrentCount
_ZhoneFarEndCurrentDMs_Object = MibTableColumn
zhoneFarEndCurrentDMs = _ZhoneFarEndCurrentDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 12),
    _ZhoneFarEndCurrentDMs_Type()
)
zhoneFarEndCurrentDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndCurrentDMs.setStatus("current")


class _ZhoneFarEndInvalidIntervals_Type(Integer32):
    """Custom type zhoneFarEndInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ZhoneFarEndInvalidIntervals_Type.__name__ = "Integer32"
_ZhoneFarEndInvalidIntervals_Object = MibTableColumn
zhoneFarEndInvalidIntervals = _ZhoneFarEndInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 6, 1, 13),
    _ZhoneFarEndInvalidIntervals_Type()
)
zhoneFarEndInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndInvalidIntervals.setStatus("current")
_ZhoneDs1FarEndIntervalTable_Object = MibTable
zhoneDs1FarEndIntervalTable = _ZhoneDs1FarEndIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7)
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndIntervalTable.setStatus("current")
_ZhoneDs1FarEndIntervalEntry_Object = MibTableRow
zhoneDs1FarEndIntervalEntry = _ZhoneDs1FarEndIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1)
)
zhoneDs1FarEndIntervalEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneFarEndIntervalIndex"),
    (0, "ZHONE-Wan-MIB", "zhoneFarEndIntervalNumber"),
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndIntervalEntry.setStatus("current")
_ZhoneFarEndIntervalIndex_Type = InterfaceIndex
_ZhoneFarEndIntervalIndex_Object = MibTableColumn
zhoneFarEndIntervalIndex = _ZhoneFarEndIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 1),
    _ZhoneFarEndIntervalIndex_Type()
)
zhoneFarEndIntervalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalIndex.setStatus("current")


class _ZhoneFarEndIntervalNumber_Type(Integer32):
    """Custom type zhoneFarEndIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZhoneFarEndIntervalNumber_Type.__name__ = "Integer32"
_ZhoneFarEndIntervalNumber_Object = MibTableColumn
zhoneFarEndIntervalNumber = _ZhoneFarEndIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 2),
    _ZhoneFarEndIntervalNumber_Type()
)
zhoneFarEndIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalNumber.setStatus("current")
_ZhoneFarEndIntervalESs_Type = PerfIntervalCount
_ZhoneFarEndIntervalESs_Object = MibTableColumn
zhoneFarEndIntervalESs = _ZhoneFarEndIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 3),
    _ZhoneFarEndIntervalESs_Type()
)
zhoneFarEndIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalESs.setStatus("current")
_ZhoneFarEndIntervalSESs_Type = PerfIntervalCount
_ZhoneFarEndIntervalSESs_Object = MibTableColumn
zhoneFarEndIntervalSESs = _ZhoneFarEndIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 4),
    _ZhoneFarEndIntervalSESs_Type()
)
zhoneFarEndIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalSESs.setStatus("current")
_ZhoneFarEndIntervalSEFSs_Type = PerfIntervalCount
_ZhoneFarEndIntervalSEFSs_Object = MibTableColumn
zhoneFarEndIntervalSEFSs = _ZhoneFarEndIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 5),
    _ZhoneFarEndIntervalSEFSs_Type()
)
zhoneFarEndIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalSEFSs.setStatus("current")
_ZhoneFarEndIntervalUASs_Type = PerfIntervalCount
_ZhoneFarEndIntervalUASs_Object = MibTableColumn
zhoneFarEndIntervalUASs = _ZhoneFarEndIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 6),
    _ZhoneFarEndIntervalUASs_Type()
)
zhoneFarEndIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalUASs.setStatus("current")
_ZhoneFarEndIntervalCSSs_Type = PerfIntervalCount
_ZhoneFarEndIntervalCSSs_Object = MibTableColumn
zhoneFarEndIntervalCSSs = _ZhoneFarEndIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 7),
    _ZhoneFarEndIntervalCSSs_Type()
)
zhoneFarEndIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalCSSs.setStatus("current")
_ZhoneFarEndIntervalLESs_Type = PerfIntervalCount
_ZhoneFarEndIntervalLESs_Object = MibTableColumn
zhoneFarEndIntervalLESs = _ZhoneFarEndIntervalLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 8),
    _ZhoneFarEndIntervalLESs_Type()
)
zhoneFarEndIntervalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalLESs.setStatus("current")
_ZhoneFarEndIntervalPCVs_Type = PerfIntervalCount
_ZhoneFarEndIntervalPCVs_Object = MibTableColumn
zhoneFarEndIntervalPCVs = _ZhoneFarEndIntervalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 9),
    _ZhoneFarEndIntervalPCVs_Type()
)
zhoneFarEndIntervalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalPCVs.setStatus("current")
_ZhoneFarEndIntervalBESs_Type = PerfIntervalCount
_ZhoneFarEndIntervalBESs_Object = MibTableColumn
zhoneFarEndIntervalBESs = _ZhoneFarEndIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 10),
    _ZhoneFarEndIntervalBESs_Type()
)
zhoneFarEndIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalBESs.setStatus("current")
_ZhoneFarEndIntervalDMs_Type = PerfIntervalCount
_ZhoneFarEndIntervalDMs_Object = MibTableColumn
zhoneFarEndIntervalDMs = _ZhoneFarEndIntervalDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 11),
    _ZhoneFarEndIntervalDMs_Type()
)
zhoneFarEndIntervalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalDMs.setStatus("current")
_ZhoneFarEndIntervalValidData_Type = TruthValue
_ZhoneFarEndIntervalValidData_Object = MibTableColumn
zhoneFarEndIntervalValidData = _ZhoneFarEndIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 7, 1, 12),
    _ZhoneFarEndIntervalValidData_Type()
)
zhoneFarEndIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndIntervalValidData.setStatus("current")
_ZhoneDs1FarEndTotalTable_Object = MibTable
zhoneDs1FarEndTotalTable = _ZhoneDs1FarEndTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8)
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndTotalTable.setStatus("current")
_ZhoneDs1FarEndTotalEntry_Object = MibTableRow
zhoneDs1FarEndTotalEntry = _ZhoneDs1FarEndTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1)
)
zhoneDs1FarEndTotalEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneFarEndTotalIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1FarEndTotalEntry.setStatus("current")
_ZhoneFarEndTotalIndex_Type = InterfaceIndex
_ZhoneFarEndTotalIndex_Object = MibTableColumn
zhoneFarEndTotalIndex = _ZhoneFarEndTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 1),
    _ZhoneFarEndTotalIndex_Type()
)
zhoneFarEndTotalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneFarEndTotalIndex.setStatus("current")
_ZhoneFarEndTotalESs_Type = PerfTotalCount
_ZhoneFarEndTotalESs_Object = MibTableColumn
zhoneFarEndTotalESs = _ZhoneFarEndTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 2),
    _ZhoneFarEndTotalESs_Type()
)
zhoneFarEndTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalESs.setStatus("current")
_ZhoneFarEndTotalSESs_Type = PerfTotalCount
_ZhoneFarEndTotalSESs_Object = MibTableColumn
zhoneFarEndTotalSESs = _ZhoneFarEndTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 3),
    _ZhoneFarEndTotalSESs_Type()
)
zhoneFarEndTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalSESs.setStatus("current")
_ZhoneFarEndTotalSEFSs_Type = PerfTotalCount
_ZhoneFarEndTotalSEFSs_Object = MibTableColumn
zhoneFarEndTotalSEFSs = _ZhoneFarEndTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 4),
    _ZhoneFarEndTotalSEFSs_Type()
)
zhoneFarEndTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalSEFSs.setStatus("current")
_ZhoneFarEndTotalUASs_Type = PerfTotalCount
_ZhoneFarEndTotalUASs_Object = MibTableColumn
zhoneFarEndTotalUASs = _ZhoneFarEndTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 5),
    _ZhoneFarEndTotalUASs_Type()
)
zhoneFarEndTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalUASs.setStatus("current")
_ZhoneFarEndTotalCSSs_Type = PerfTotalCount
_ZhoneFarEndTotalCSSs_Object = MibTableColumn
zhoneFarEndTotalCSSs = _ZhoneFarEndTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 6),
    _ZhoneFarEndTotalCSSs_Type()
)
zhoneFarEndTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalCSSs.setStatus("current")
_ZhoneFarEndTotalLESs_Type = PerfTotalCount
_ZhoneFarEndTotalLESs_Object = MibTableColumn
zhoneFarEndTotalLESs = _ZhoneFarEndTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 7),
    _ZhoneFarEndTotalLESs_Type()
)
zhoneFarEndTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalLESs.setStatus("current")
_ZhoneFarEndTotalPCVs_Type = PerfTotalCount
_ZhoneFarEndTotalPCVs_Object = MibTableColumn
zhoneFarEndTotalPCVs = _ZhoneFarEndTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 8),
    _ZhoneFarEndTotalPCVs_Type()
)
zhoneFarEndTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalPCVs.setStatus("current")
_ZhoneFarEndTotalBESs_Type = PerfTotalCount
_ZhoneFarEndTotalBESs_Object = MibTableColumn
zhoneFarEndTotalBESs = _ZhoneFarEndTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 9),
    _ZhoneFarEndTotalBESs_Type()
)
zhoneFarEndTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalBESs.setStatus("current")
_ZhoneFarEndTotalDMs_Type = PerfTotalCount
_ZhoneFarEndTotalDMs_Object = MibTableColumn
zhoneFarEndTotalDMs = _ZhoneFarEndTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 8, 1, 10),
    _ZhoneFarEndTotalDMs_Type()
)
zhoneFarEndTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneFarEndTotalDMs.setStatus("current")
_ZhoneChanMappingTable_Object = MibTable
zhoneChanMappingTable = _ZhoneChanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 9)
)
if mibBuilder.loadTexts:
    zhoneChanMappingTable.setStatus("current")
_ZhoneChanMappingEntry_Object = MibTableRow
zhoneChanMappingEntry = _ZhoneChanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 9, 1)
)
zhoneChanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZHONE-Wan-MIB", "zhoneDs1ChannelNumber"),
)
if mibBuilder.loadTexts:
    zhoneChanMappingEntry.setStatus("current")
_ZhoneChanMappedIfIndex_Type = InterfaceIndex
_ZhoneChanMappedIfIndex_Object = MibTableColumn
zhoneChanMappedIfIndex = _ZhoneChanMappedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 9, 1, 1),
    _ZhoneChanMappedIfIndex_Type()
)
zhoneChanMappedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneChanMappedIfIndex.setStatus("current")
_ZhoneDsxTraps_ObjectIdentity = ObjectIdentity
zhoneDsxTraps = _ZhoneDsxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 10)
)
_ZhoneDsxTrapsV2_ObjectIdentity = ObjectIdentity
zhoneDsxTrapsV2 = _ZhoneDsxTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 10, 0)
)
_ZhoneDs1BertTable_Object = MibTable
zhoneDs1BertTable = _ZhoneDs1BertTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13)
)
if mibBuilder.loadTexts:
    zhoneDs1BertTable.setStatus("current")
_ZhoneDs1BertEntry_Object = MibTableRow
zhoneDs1BertEntry = _ZhoneDs1BertEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1)
)
zhoneDs1BertEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneBertIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1BertEntry.setStatus("current")


class _ZhoneBertIndex_Type(Integer32):
    """Custom type zhoneBertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 21),
    )


_ZhoneBertIndex_Type.__name__ = "Integer32"
_ZhoneBertIndex_Object = MibTableColumn
zhoneBertIndex = _ZhoneBertIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 1),
    _ZhoneBertIndex_Type()
)
zhoneBertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zhoneBertIndex.setStatus("current")
_ZhoneBertInterfaceIndex_Type = InterfaceIndex
_ZhoneBertInterfaceIndex_Object = MibTableColumn
zhoneBertInterfaceIndex = _ZhoneBertInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 2),
    _ZhoneBertInterfaceIndex_Type()
)
zhoneBertInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBertInterfaceIndex.setStatus("current")


class _ZhoneBertRequest_Type(Integer32):
    """Custom type zhoneBertRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("start", 2),
          ("stop", 3))
    )


_ZhoneBertRequest_Type.__name__ = "Integer32"
_ZhoneBertRequest_Object = MibTableColumn
zhoneBertRequest = _ZhoneBertRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 3),
    _ZhoneBertRequest_Type()
)
zhoneBertRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBertRequest.setStatus("current")


class _ZhoneBertType_Type(Integer32):
    """Custom type zhoneBertType based on Integer32"""
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
        *(("prbs215", 2),
          ("prbs220", 3),
          ("qrss", 1))
    )


_ZhoneBertType_Type.__name__ = "Integer32"
_ZhoneBertType_Object = MibTableColumn
zhoneBertType = _ZhoneBertType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 4),
    _ZhoneBertType_Type()
)
zhoneBertType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBertType.setStatus("current")


class _ZhoneBertTestDuration_Type(Integer32):
    """Custom type zhoneBertTestDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_ZhoneBertTestDuration_Type.__name__ = "Integer32"
_ZhoneBertTestDuration_Object = MibTableColumn
zhoneBertTestDuration = _ZhoneBertTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 5),
    _ZhoneBertTestDuration_Type()
)
zhoneBertTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBertTestDuration.setStatus("current")


class _ZhoneBertLoopUp_Type(Integer32):
    """Custom type zhoneBertLoopUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 2),
          ("noloop", 1),
          ("payloadloop", 3))
    )


_ZhoneBertLoopUp_Type.__name__ = "Integer32"
_ZhoneBertLoopUp_Object = MibTableColumn
zhoneBertLoopUp = _ZhoneBertLoopUp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 13, 1, 6),
    _ZhoneBertLoopUp_Type()
)
zhoneBertLoopUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneBertLoopUp.setStatus("current")
_ZhoneDs1BertResultsTable_Object = MibTable
zhoneDs1BertResultsTable = _ZhoneDs1BertResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14)
)
if mibBuilder.loadTexts:
    zhoneDs1BertResultsTable.setStatus("current")
_ZhoneDs1BertResultsEntry_Object = MibTableRow
zhoneDs1BertResultsEntry = _ZhoneDs1BertResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1)
)
zhoneDs1BertResultsEntry.setIndexNames(
    (0, "ZHONE-Wan-MIB", "zhoneBertIndex"),
)
if mibBuilder.loadTexts:
    zhoneDs1BertResultsEntry.setStatus("current")


class _ZhoneBertStatus_Type(Integer32):
    """Custom type zhoneBertStatus based on Integer32"""
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
        *(("abortInProgress", 2),
          ("aborted", 5),
          ("complete", 3),
          ("failed", 8),
          ("inProgress", 1),
          ("noResults", 4),
          ("portNotAdminTest", 7),
          ("unsupported", 6))
    )


_ZhoneBertStatus_Type.__name__ = "Integer32"
_ZhoneBertStatus_Object = MibTableColumn
zhoneBertStatus = _ZhoneBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1, 1),
    _ZhoneBertStatus_Type()
)
zhoneBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBertStatus.setStatus("current")


class _ZhoneBertElapsedTime_Type(Integer32):
    """Custom type zhoneBertElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ZhoneBertElapsedTime_Type.__name__ = "Integer32"
_ZhoneBertElapsedTime_Object = MibTableColumn
zhoneBertElapsedTime = _ZhoneBertElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1, 2),
    _ZhoneBertElapsedTime_Type()
)
zhoneBertElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBertElapsedTime.setStatus("current")


class _ZhoneBertErroredSeconds_Type(Integer32):
    """Custom type zhoneBertErroredSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ZhoneBertErroredSeconds_Type.__name__ = "Integer32"
_ZhoneBertErroredSeconds_Object = MibTableColumn
zhoneBertErroredSeconds = _ZhoneBertErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1, 3),
    _ZhoneBertErroredSeconds_Type()
)
zhoneBertErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBertErroredSeconds.setStatus("current")


class _ZhoneBertOutOfSynchSeconds_Type(Integer32):
    """Custom type zhoneBertOutOfSynchSeconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ZhoneBertOutOfSynchSeconds_Type.__name__ = "Integer32"
_ZhoneBertOutOfSynchSeconds_Object = MibTableColumn
zhoneBertOutOfSynchSeconds = _ZhoneBertOutOfSynchSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1, 4),
    _ZhoneBertOutOfSynchSeconds_Type()
)
zhoneBertOutOfSynchSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBertOutOfSynchSeconds.setStatus("current")


class _ZhoneBertErrors_Type(Integer32):
    """Custom type zhoneBertErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneBertErrors_Type.__name__ = "Integer32"
_ZhoneBertErrors_Object = MibTableColumn
zhoneBertErrors = _ZhoneBertErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 14, 1, 5),
    _ZhoneBertErrors_Type()
)
zhoneBertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneBertErrors.setStatus("current")

# Managed Objects groups


# Notification objects

zhoneLineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 2, 10, 0, 1)
)
zhoneLineStatusChange.setObjects(
      *(("ZHONE-Wan-MIB", "zhoneLineStatus"),
        ("ZHONE-Wan-MIB", "zhoneLineStatusLastChange"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    zhoneLineStatusChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-Wan-MIB",
    **{"zhoneDs1Mib": zhoneDs1Mib,
       "zhoneDs1Table": zhoneDs1Table,
       "zhoneDs1Entry": zhoneDs1Entry,
       "zhoneLineIndex": zhoneLineIndex,
       "zhoneTimeElapsed": zhoneTimeElapsed,
       "zhoneValidIntervals": zhoneValidIntervals,
       "zhoneLineType": zhoneLineType,
       "zhoneLineCoding": zhoneLineCoding,
       "zhoneSendCode": zhoneSendCode,
       "zhoneCircuitIdentifier": zhoneCircuitIdentifier,
       "zhoneLoopbackConfig": zhoneLoopbackConfig,
       "zhoneLineStatus": zhoneLineStatus,
       "zhoneSignalMode": zhoneSignalMode,
       "zhoneTransmitClockSource": zhoneTransmitClockSource,
       "zhoneFdl": zhoneFdl,
       "zhoneInvalidIntervals": zhoneInvalidIntervals,
       "zhoneDsxLineLength": zhoneDsxLineLength,
       "zhoneLineStatusLastChange": zhoneLineStatusLastChange,
       "zhoneLineStatusChangeTrapEnable": zhoneLineStatusChangeTrapEnable,
       "zhoneLoopbackStatus": zhoneLoopbackStatus,
       "zhoneDs1ChannelNumber": zhoneDs1ChannelNumber,
       "zhoneChannelization": zhoneChannelization,
       "zhoneDs1Mode": zhoneDs1Mode,
       "zhoneCsuLineLength": zhoneCsuLineLength,
       "zhoneClockSourceEligibility": zhoneClockSourceEligibility,
       "zhoneCellScramble": zhoneCellScramble,
       "zhoneCosetPolynomial": zhoneCosetPolynomial,
       "zhoneDs1ProtocolEmulation": zhoneDs1ProtocolEmulation,
       "zhoneDs1SignalType": zhoneDs1SignalType,
       "zhoneDs1GroupIndex": zhoneDs1GroupIndex,
       "zhoneDs1LinePower": zhoneDs1LinePower,
       "zhoneDs1TimeslotAssignment": zhoneDs1TimeslotAssignment,
       "zhoneDs1TxClockRecovery": zhoneDs1TxClockRecovery,
       "zhoneDs1TxClockAdaptiveQuality": zhoneDs1TxClockAdaptiveQuality,
       "zhoneDs1CurrentTable": zhoneDs1CurrentTable,
       "zhoneDs1CurrentEntry": zhoneDs1CurrentEntry,
       "zhoneCurrentIndex": zhoneCurrentIndex,
       "zhoneCurrentESs": zhoneCurrentESs,
       "zhoneCurrentSESs": zhoneCurrentSESs,
       "zhoneCurrentSEFSs": zhoneCurrentSEFSs,
       "zhoneCurrentUASs": zhoneCurrentUASs,
       "zhoneCurrentCSSs": zhoneCurrentCSSs,
       "zhoneCurrentPCVs": zhoneCurrentPCVs,
       "zhoneCurrentLESs": zhoneCurrentLESs,
       "zhoneCurrentBESs": zhoneCurrentBESs,
       "zhoneCurrentDMs": zhoneCurrentDMs,
       "zhoneCurrentLCVs": zhoneCurrentLCVs,
       "zhoneDs1IntervalTable": zhoneDs1IntervalTable,
       "zhoneDs1IntervalEntry": zhoneDs1IntervalEntry,
       "zhoneIntervalIndex": zhoneIntervalIndex,
       "zhoneIntervalNumber": zhoneIntervalNumber,
       "zhoneIntervalESs": zhoneIntervalESs,
       "zhoneIntervalSESs": zhoneIntervalSESs,
       "zhoneIntervalSEFSs": zhoneIntervalSEFSs,
       "zhoneIntervalUASs": zhoneIntervalUASs,
       "zhoneIntervalCSSs": zhoneIntervalCSSs,
       "zhoneIntervalPCVs": zhoneIntervalPCVs,
       "zhoneIntervalLESs": zhoneIntervalLESs,
       "zhoneIntervalBESs": zhoneIntervalBESs,
       "zhoneIntervalDMs": zhoneIntervalDMs,
       "zhoneIntervalLCVs": zhoneIntervalLCVs,
       "zhoneIntervalValidData": zhoneIntervalValidData,
       "zhoneDs1TotalTable": zhoneDs1TotalTable,
       "zhoneDs1TotalEntry": zhoneDs1TotalEntry,
       "zhoneTotalIndex": zhoneTotalIndex,
       "zhoneTotalESs": zhoneTotalESs,
       "zhoneTotalSESs": zhoneTotalSESs,
       "zhoneTotalSEFSs": zhoneTotalSEFSs,
       "zhoneTotalUASs": zhoneTotalUASs,
       "zhoneTotalCSSs": zhoneTotalCSSs,
       "zhoneTotalPCVs": zhoneTotalPCVs,
       "zhoneTotalLESs": zhoneTotalLESs,
       "zhoneTotalBESs": zhoneTotalBESs,
       "zhoneTotalDMs": zhoneTotalDMs,
       "zhoneTotalLCVs": zhoneTotalLCVs,
       "zhoneDs1FarEndCurrentTable": zhoneDs1FarEndCurrentTable,
       "zhoneDs1FarEndCurrentEntry": zhoneDs1FarEndCurrentEntry,
       "zhoneFarEndCurrentIndex": zhoneFarEndCurrentIndex,
       "zhoneFarEndTimeElapsed": zhoneFarEndTimeElapsed,
       "zhoneFarEndValidIntervals": zhoneFarEndValidIntervals,
       "zhoneFarEndCurrentESs": zhoneFarEndCurrentESs,
       "zhoneFarEndCurrentSESs": zhoneFarEndCurrentSESs,
       "zhoneFarEndCurrentSEFSs": zhoneFarEndCurrentSEFSs,
       "zhoneFarEndCurrentUASs": zhoneFarEndCurrentUASs,
       "zhoneFarEndCurrentCSSs": zhoneFarEndCurrentCSSs,
       "zhoneFarEndCurrentLESs": zhoneFarEndCurrentLESs,
       "zhoneFarEndCurrentPCVs": zhoneFarEndCurrentPCVs,
       "zhoneFarEndCurrentBESs": zhoneFarEndCurrentBESs,
       "zhoneFarEndCurrentDMs": zhoneFarEndCurrentDMs,
       "zhoneFarEndInvalidIntervals": zhoneFarEndInvalidIntervals,
       "zhoneDs1FarEndIntervalTable": zhoneDs1FarEndIntervalTable,
       "zhoneDs1FarEndIntervalEntry": zhoneDs1FarEndIntervalEntry,
       "zhoneFarEndIntervalIndex": zhoneFarEndIntervalIndex,
       "zhoneFarEndIntervalNumber": zhoneFarEndIntervalNumber,
       "zhoneFarEndIntervalESs": zhoneFarEndIntervalESs,
       "zhoneFarEndIntervalSESs": zhoneFarEndIntervalSESs,
       "zhoneFarEndIntervalSEFSs": zhoneFarEndIntervalSEFSs,
       "zhoneFarEndIntervalUASs": zhoneFarEndIntervalUASs,
       "zhoneFarEndIntervalCSSs": zhoneFarEndIntervalCSSs,
       "zhoneFarEndIntervalLESs": zhoneFarEndIntervalLESs,
       "zhoneFarEndIntervalPCVs": zhoneFarEndIntervalPCVs,
       "zhoneFarEndIntervalBESs": zhoneFarEndIntervalBESs,
       "zhoneFarEndIntervalDMs": zhoneFarEndIntervalDMs,
       "zhoneFarEndIntervalValidData": zhoneFarEndIntervalValidData,
       "zhoneDs1FarEndTotalTable": zhoneDs1FarEndTotalTable,
       "zhoneDs1FarEndTotalEntry": zhoneDs1FarEndTotalEntry,
       "zhoneFarEndTotalIndex": zhoneFarEndTotalIndex,
       "zhoneFarEndTotalESs": zhoneFarEndTotalESs,
       "zhoneFarEndTotalSESs": zhoneFarEndTotalSESs,
       "zhoneFarEndTotalSEFSs": zhoneFarEndTotalSEFSs,
       "zhoneFarEndTotalUASs": zhoneFarEndTotalUASs,
       "zhoneFarEndTotalCSSs": zhoneFarEndTotalCSSs,
       "zhoneFarEndTotalLESs": zhoneFarEndTotalLESs,
       "zhoneFarEndTotalPCVs": zhoneFarEndTotalPCVs,
       "zhoneFarEndTotalBESs": zhoneFarEndTotalBESs,
       "zhoneFarEndTotalDMs": zhoneFarEndTotalDMs,
       "zhoneChanMappingTable": zhoneChanMappingTable,
       "zhoneChanMappingEntry": zhoneChanMappingEntry,
       "zhoneChanMappedIfIndex": zhoneChanMappedIfIndex,
       "zhoneDsxTraps": zhoneDsxTraps,
       "zhoneDsxTrapsV2": zhoneDsxTrapsV2,
       "zhoneLineStatusChange": zhoneLineStatusChange,
       "zhoneDs1BertTable": zhoneDs1BertTable,
       "zhoneDs1BertEntry": zhoneDs1BertEntry,
       "zhoneBertIndex": zhoneBertIndex,
       "zhoneBertInterfaceIndex": zhoneBertInterfaceIndex,
       "zhoneBertRequest": zhoneBertRequest,
       "zhoneBertType": zhoneBertType,
       "zhoneBertTestDuration": zhoneBertTestDuration,
       "zhoneBertLoopUp": zhoneBertLoopUp,
       "zhoneDs1BertResultsTable": zhoneDs1BertResultsTable,
       "zhoneDs1BertResultsEntry": zhoneDs1BertResultsEntry,
       "zhoneBertStatus": zhoneBertStatus,
       "zhoneBertElapsedTime": zhoneBertElapsedTime,
       "zhoneBertErroredSeconds": zhoneBertErroredSeconds,
       "zhoneBertOutOfSynchSeconds": zhoneBertOutOfSynchSeconds,
       "zhoneBertErrors": zhoneBertErrors}
)
