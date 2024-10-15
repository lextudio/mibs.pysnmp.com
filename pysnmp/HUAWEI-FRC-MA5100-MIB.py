# SNMP MIB module (HUAWEI-FRC-MA5100-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-FRC-MA5100-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:50 2024
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

(hwMa5100Mib,
 hwMusaFrameIndex,
 hwMusaSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-MUSA-MA5100-MIB",
    "hwMa5100Mib",
    "hwMusaFrameIndex",
    "hwMusaSlotIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMusaFrcMib_ObjectIdentity = ObjectIdentity
hwMusaFrcMib = _HwMusaFrcMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9)
)
_HwMusaFrcBoardTable_Object = MibTable
hwMusaFrcBoardTable = _HwMusaFrcBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1)
)
if mibBuilder.loadTexts:
    hwMusaFrcBoardTable.setStatus("mandatory")
_HwMusaFrcBoardEntry_Object = MibTableRow
hwMusaFrcBoardEntry = _HwMusaFrcBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1)
)
hwMusaFrcBoardEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaFrcBoardEntry.setStatus("mandatory")


class _HwMusaFrcPvcAlarmEnable_Type(Integer32):
    """Custom type hwMusaFrcPvcAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMusaFrcPvcAlarmEnable_Type.__name__ = "Integer32"
_HwMusaFrcPvcAlarmEnable_Object = MibTableColumn
hwMusaFrcPvcAlarmEnable = _HwMusaFrcPvcAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1, 1),
    _HwMusaFrcPvcAlarmEnable_Type()
)
hwMusaFrcPvcAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPvcAlarmEnable.setStatus("mandatory")
_HwMusaFrcBoardClearStatistic_Type = Integer32
_HwMusaFrcBoardClearStatistic_Object = MibTableColumn
hwMusaFrcBoardClearStatistic = _HwMusaFrcBoardClearStatistic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1, 2),
    _HwMusaFrcBoardClearStatistic_Type()
)
hwMusaFrcBoardClearStatistic.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hwMusaFrcBoardClearStatistic.setStatus("mandatory")


class _HwMusaFrcClockMode_Type(Integer32):
    """Custom type hwMusaFrcClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backplate", 1),
          ("line", 2),
          ("local", 0))
    )


_HwMusaFrcClockMode_Type.__name__ = "Integer32"
_HwMusaFrcClockMode_Object = MibTableColumn
hwMusaFrcClockMode = _HwMusaFrcClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1, 3),
    _HwMusaFrcClockMode_Type()
)
hwMusaFrcClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcClockMode.setStatus("mandatory")


class _HwMusaFrcPhyPortId_Type(Integer32):
    """Custom type hwMusaFrcPhyPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMusaFrcPhyPortId_Type.__name__ = "Integer32"
_HwMusaFrcPhyPortId_Object = MibTableColumn
hwMusaFrcPhyPortId = _HwMusaFrcPhyPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1, 4),
    _HwMusaFrcPhyPortId_Type()
)
hwMusaFrcPhyPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortId.setStatus("mandatory")


class _HwMusaFrcPhyPortType_Type(Integer32):
    """Custom type hwMusaFrcPhyPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 1),
          ("t1", 2),
          ("v35", 3))
    )


_HwMusaFrcPhyPortType_Type.__name__ = "Integer32"
_HwMusaFrcPhyPortType_Object = MibTableColumn
hwMusaFrcPhyPortType = _HwMusaFrcPhyPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 1, 1, 5),
    _HwMusaFrcPhyPortType_Type()
)
hwMusaFrcPhyPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortType.setStatus("mandatory")
_HwMusaFrcPhyPortLineIfTable_Object = MibTable
hwMusaFrcPhyPortLineIfTable = _HwMusaFrcPhyPortLineIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2)
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortLineIfTable.setStatus("mandatory")
_HwMusaFrcPhyPortLineIfEntry_Object = MibTableRow
hwMusaFrcPhyPortLineIfEntry = _HwMusaFrcPhyPortLineIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1)
)
hwMusaFrcPhyPortLineIfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcPhyPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortLineIfEntry.setStatus("mandatory")


class _HwMusaFrcMainClock_Type(Integer32):
    """Custom type hwMusaFrcMainClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backplate", 1),
          ("line", 2),
          ("local", 0))
    )


_HwMusaFrcMainClock_Type.__name__ = "Integer32"
_HwMusaFrcMainClock_Object = MibTableColumn
hwMusaFrcMainClock = _HwMusaFrcMainClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 1),
    _HwMusaFrcMainClock_Type()
)
hwMusaFrcMainClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcMainClock.setStatus("mandatory")


class _HwMusaFrcT1HaulMode_Type(Integer32):
    """Custom type hwMusaFrcT1HaulMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 0))
    )


_HwMusaFrcT1HaulMode_Type.__name__ = "Integer32"
_HwMusaFrcT1HaulMode_Object = MibTableColumn
hwMusaFrcT1HaulMode = _HwMusaFrcT1HaulMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 2),
    _HwMusaFrcT1HaulMode_Type()
)
hwMusaFrcT1HaulMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcT1HaulMode.setStatus("mandatory")


class _HwMusaFrcT1E1Crc_Type(Integer32):
    """Custom type hwMusaFrcT1E1Crc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HwMusaFrcT1E1Crc_Type.__name__ = "Integer32"
_HwMusaFrcT1E1Crc_Object = MibTableColumn
hwMusaFrcT1E1Crc = _HwMusaFrcT1E1Crc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 3),
    _HwMusaFrcT1E1Crc_Type()
)
hwMusaFrcT1E1Crc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcT1E1Crc.setStatus("mandatory")


class _HwMusaFrcT1FrameFormat_Type(Integer32):
    """Custom type hwMusaFrcT1FrameFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1d412mf", 2),
          ("t1d44mf", 1),
          ("t1esf", 0))
    )


_HwMusaFrcT1FrameFormat_Type.__name__ = "Integer32"
_HwMusaFrcT1FrameFormat_Object = MibTableColumn
hwMusaFrcT1FrameFormat = _HwMusaFrcT1FrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 4),
    _HwMusaFrcT1FrameFormat_Type()
)
hwMusaFrcT1FrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcT1FrameFormat.setStatus("mandatory")


class _HwMusaFrcT1LineCode_Type(Integer32):
    """Custom type hwMusaFrcT1LineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 0))
    )


_HwMusaFrcT1LineCode_Type.__name__ = "Integer32"
_HwMusaFrcT1LineCode_Object = MibTableColumn
hwMusaFrcT1LineCode = _HwMusaFrcT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 5),
    _HwMusaFrcT1LineCode_Type()
)
hwMusaFrcT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcT1LineCode.setStatus("mandatory")


class _HwMusaFrcV35ClockMode_Type(Integer32):
    """Custom type hwMusaFrcV35ClockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dceinner", 0),
          ("dceouter", 2),
          ("dceslave", 1),
          ("dteinner", 3),
          ("dteouter", 5),
          ("dteslave", 4))
    )


_HwMusaFrcV35ClockMode_Type.__name__ = "Integer32"
_HwMusaFrcV35ClockMode_Object = MibTableColumn
hwMusaFrcV35ClockMode = _HwMusaFrcV35ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 6),
    _HwMusaFrcV35ClockMode_Type()
)
hwMusaFrcV35ClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcV35ClockMode.setStatus("mandatory")
_HwMusaFrcT1E1TsBitMap_Type = Integer32
_HwMusaFrcT1E1TsBitMap_Object = MibTableColumn
hwMusaFrcT1E1TsBitMap = _HwMusaFrcT1E1TsBitMap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 7),
    _HwMusaFrcT1E1TsBitMap_Type()
)
hwMusaFrcT1E1TsBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcT1E1TsBitMap.setStatus("mandatory")


class _HwMusaFrcClockLoopMode_Type(Integer32):
    """Custom type hwMusaFrcClockLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("payloop", 0),
          ("remoteloop", 1),
          ("single-timeslot", 2))
    )


_HwMusaFrcClockLoopMode_Type.__name__ = "Integer32"
_HwMusaFrcClockLoopMode_Object = MibTableColumn
hwMusaFrcClockLoopMode = _HwMusaFrcClockLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 8),
    _HwMusaFrcClockLoopMode_Type()
)
hwMusaFrcClockLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcClockLoopMode.setStatus("mandatory")


class _HwMusaFrcLoopState_Type(Integer32):
    """Custom type hwMusaFrcLoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loop", 1),
          ("noloop", 0))
    )


_HwMusaFrcLoopState_Type.__name__ = "Integer32"
_HwMusaFrcLoopState_Object = MibTableColumn
hwMusaFrcLoopState = _HwMusaFrcLoopState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 9),
    _HwMusaFrcLoopState_Type()
)
hwMusaFrcLoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLoopState.setStatus("mandatory")


class _HwMusaFrcV35InvertTxClock_Type(Integer32):
    """Custom type hwMusaFrcV35InvertTxClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_HwMusaFrcV35InvertTxClock_Type.__name__ = "Integer32"
_HwMusaFrcV35InvertTxClock_Object = MibTableColumn
hwMusaFrcV35InvertTxClock = _HwMusaFrcV35InvertTxClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 10),
    _HwMusaFrcV35InvertTxClock_Type()
)
hwMusaFrcV35InvertTxClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcV35InvertTxClock.setStatus("mandatory")


class _HwMusaFrcSingleTimeSlotId_Type(Integer32):
    """Custom type hwMusaFrcSingleTimeSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_HwMusaFrcSingleTimeSlotId_Type.__name__ = "Integer32"
_HwMusaFrcSingleTimeSlotId_Object = MibTableColumn
hwMusaFrcSingleTimeSlotId = _HwMusaFrcSingleTimeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 2, 1, 11),
    _HwMusaFrcSingleTimeSlotId_Type()
)
hwMusaFrcSingleTimeSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcSingleTimeSlotId.setStatus("mandatory")
_HwMusaFrcPhyPortAlarmTable_Object = MibTable
hwMusaFrcPhyPortAlarmTable = _HwMusaFrcPhyPortAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3)
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortAlarmTable.setStatus("mandatory")
_HwMusaFrcPhyPortAlarmEntry_Object = MibTableRow
hwMusaFrcPhyPortAlarmEntry = _HwMusaFrcPhyPortAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1)
)
hwMusaFrcPhyPortAlarmEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcPhyPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyPortAlarmEntry.setStatus("mandatory")


class _HwMusaFrcAlarmSw_Type(Integer32):
    """Custom type hwMusaFrcAlarmSw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMusaFrcAlarmSw_Type.__name__ = "Integer32"
_HwMusaFrcAlarmSw_Object = MibTableColumn
hwMusaFrcAlarmSw = _HwMusaFrcAlarmSw_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 1),
    _HwMusaFrcAlarmSw_Type()
)
hwMusaFrcAlarmSw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcAlarmSw.setStatus("mandatory")


class _HwMusaFrcRACTS_Type(Integer32):
    """Custom type hwMusaFrcRACTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmdown", 1),
          ("noalarmup", 0))
    )


_HwMusaFrcRACTS_Type.__name__ = "Integer32"
_HwMusaFrcRACTS_Object = MibTableColumn
hwMusaFrcRACTS = _HwMusaFrcRACTS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 2),
    _HwMusaFrcRACTS_Type()
)
hwMusaFrcRACTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcRACTS.setStatus("mandatory")


class _HwMusaFrcLFADSR_Type(Integer32):
    """Custom type hwMusaFrcLFADSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmdown", 1),
          ("noalarmup", 0))
    )


_HwMusaFrcLFADSR_Type.__name__ = "Integer32"
_HwMusaFrcLFADSR_Object = MibTableColumn
hwMusaFrcLFADSR = _HwMusaFrcLFADSR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 3),
    _HwMusaFrcLFADSR_Type()
)
hwMusaFrcLFADSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcLFADSR.setStatus("mandatory")


class _HwMusaFrcLOSPLL_Type(Integer32):
    """Custom type hwMusaFrcLOSPLL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmdown", 1),
          ("noalarmup", 0))
    )


_HwMusaFrcLOSPLL_Type.__name__ = "Integer32"
_HwMusaFrcLOSPLL_Object = MibTableColumn
hwMusaFrcLOSPLL = _HwMusaFrcLOSPLL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 4),
    _HwMusaFrcLOSPLL_Type()
)
hwMusaFrcLOSPLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcLOSPLL.setStatus("mandatory")


class _HwMusaFrcAISDCD_Type(Integer32):
    """Custom type hwMusaFrcAISDCD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmdown", 1),
          ("noalarmup", 0))
    )


_HwMusaFrcAISDCD_Type.__name__ = "Integer32"
_HwMusaFrcAISDCD_Object = MibTableColumn
hwMusaFrcAISDCD = _HwMusaFrcAISDCD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 5),
    _HwMusaFrcAISDCD_Type()
)
hwMusaFrcAISDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAISDCD.setStatus("mandatory")
_HwMusaFrcAlarmCount_Type = Integer32
_HwMusaFrcAlarmCount_Object = MibTableColumn
hwMusaFrcAlarmCount = _HwMusaFrcAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 6),
    _HwMusaFrcAlarmCount_Type()
)
hwMusaFrcAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAlarmCount.setStatus("mandatory")


class _HwMusaFrcDTR_Type(Integer32):
    """Custom type hwMusaFrcDTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 0))
    )


_HwMusaFrcDTR_Type.__name__ = "Integer32"
_HwMusaFrcDTR_Object = MibTableColumn
hwMusaFrcDTR = _HwMusaFrcDTR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 7),
    _HwMusaFrcDTR_Type()
)
hwMusaFrcDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcDTR.setStatus("mandatory")


class _HwMusaFrcRTS_Type(Integer32):
    """Custom type hwMusaFrcRTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 0))
    )


_HwMusaFrcRTS_Type.__name__ = "Integer32"
_HwMusaFrcRTS_Object = MibTableColumn
hwMusaFrcRTS = _HwMusaFrcRTS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 8),
    _HwMusaFrcRTS_Type()
)
hwMusaFrcRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcRTS.setStatus("mandatory")


class _HwMusaFrcSCOL_Type(Integer32):
    """Custom type hwMusaFrcSCOL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("noalarm", 0))
    )


_HwMusaFrcSCOL_Type.__name__ = "Integer32"
_HwMusaFrcSCOL_Object = MibTableColumn
hwMusaFrcSCOL = _HwMusaFrcSCOL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 3, 1, 9),
    _HwMusaFrcSCOL_Type()
)
hwMusaFrcSCOL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSCOL.setStatus("mandatory")
_HwMusaFrcLogicPortTable_Object = MibTable
hwMusaFrcLogicPortTable = _HwMusaFrcLogicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4)
)
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortTable.setStatus("mandatory")
_HwMusaFrcLogicPortEntry_Object = MibTableRow
hwMusaFrcLogicPortEntry = _HwMusaFrcLogicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1)
)
hwMusaFrcLogicPortEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogicPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortEntry.setStatus("mandatory")


class _HwMusaFrcLogicPortId_Type(Integer32):
    """Custom type hwMusaFrcLogicPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMusaFrcLogicPortId_Type.__name__ = "Integer32"
_HwMusaFrcLogicPortId_Object = MibTableColumn
hwMusaFrcLogicPortId = _HwMusaFrcLogicPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 1),
    _HwMusaFrcLogicPortId_Type()
)
hwMusaFrcLogicPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortId.setStatus("mandatory")


class _HwMusaFrcPhyPort_Type(Integer32):
    """Custom type hwMusaFrcPhyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwMusaFrcPhyPort_Type.__name__ = "Integer32"
_HwMusaFrcPhyPort_Object = MibTableColumn
hwMusaFrcPhyPort = _HwMusaFrcPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 2),
    _HwMusaFrcPhyPort_Type()
)
hwMusaFrcPhyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPhyPort.setStatus("mandatory")
_HwMusaFrcE1T1TsBitMapV35NValue_Type = Integer32
_HwMusaFrcE1T1TsBitMapV35NValue_Object = MibTableColumn
hwMusaFrcE1T1TsBitMapV35NValue = _HwMusaFrcE1T1TsBitMapV35NValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 3),
    _HwMusaFrcE1T1TsBitMapV35NValue_Type()
)
hwMusaFrcE1T1TsBitMapV35NValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcE1T1TsBitMapV35NValue.setStatus("mandatory")


class _HwMusaFrcDlciType_Type(Integer32):
    """Custom type hwMusaFrcDlciType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwMusaFrcDlciType_Type.__name__ = "Integer32"
_HwMusaFrcDlciType_Object = MibTableColumn
hwMusaFrcDlciType = _HwMusaFrcDlciType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 4),
    _HwMusaFrcDlciType_Type()
)
hwMusaFrcDlciType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDlciType.setStatus("mandatory")
_HwMusaFrcFreeBandwidth_Type = Integer32
_HwMusaFrcFreeBandwidth_Object = MibTableColumn
hwMusaFrcFreeBandwidth = _HwMusaFrcFreeBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 5),
    _HwMusaFrcFreeBandwidth_Type()
)
hwMusaFrcFreeBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcFreeBandwidth.setStatus("mandatory")


class _HwMusaFrcServiceFlag_Type(Integer32):
    """Custom type hwMusaFrcServiceFlag based on Integer32"""
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
        *(("frIwf", 4),
          ("hdlc", 2),
          ("network11", 0),
          ("networkN1", 3),
          ("service", 1))
    )


_HwMusaFrcServiceFlag_Type.__name__ = "Integer32"
_HwMusaFrcServiceFlag_Object = MibTableColumn
hwMusaFrcServiceFlag = _HwMusaFrcServiceFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 6),
    _HwMusaFrcServiceFlag_Type()
)
hwMusaFrcServiceFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcServiceFlag.setStatus("mandatory")


class _HwMusaFrcPortActivate_Type(Integer32):
    """Custom type hwMusaFrcPortActivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("block", 0),
          ("unblock", 1))
    )


_HwMusaFrcPortActivate_Type.__name__ = "Integer32"
_HwMusaFrcPortActivate_Object = MibTableColumn
hwMusaFrcPortActivate = _HwMusaFrcPortActivate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 7),
    _HwMusaFrcPortActivate_Type()
)
hwMusaFrcPortActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPortActivate.setStatus("mandatory")


class _HwMusaFrcLogicPortOperate_Type(Integer32):
    """Custom type hwMusaFrcLogicPortOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaFrcLogicPortOperate_Type.__name__ = "Integer32"
_HwMusaFrcLogicPortOperate_Object = MibTableColumn
hwMusaFrcLogicPortOperate = _HwMusaFrcLogicPortOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 4, 1, 8),
    _HwMusaFrcLogicPortOperate_Type()
)
hwMusaFrcLogicPortOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortOperate.setStatus("mandatory")
_HwMusaFrcLogPortSigTable_Object = MibTable
hwMusaFrcLogPortSigTable = _HwMusaFrcLogPortSigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5)
)
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigTable.setStatus("mandatory")
_HwMusaFrcLogPortSigEntry_Object = MibTableRow
hwMusaFrcLogPortSigEntry = _HwMusaFrcLogPortSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1)
)
hwMusaFrcLogPortSigEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogPortSigSide"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogicPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigEntry.setStatus("mandatory")


class _HwMusaFrcLogPortSigSide_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("atmside", 1),
          ("frside", 0))
    )


_HwMusaFrcLogPortSigSide_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigSide_Object = MibTableColumn
hwMusaFrcLogPortSigSide = _HwMusaFrcLogPortSigSide_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 1),
    _HwMusaFrcLogPortSigSide_Type()
)
hwMusaFrcLogPortSigSide.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigSide.setStatus("mandatory")


class _HwMusaFrcLogPortSigProtocalType_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigProtocalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ansit167d", 1),
          ("cisiolmi", 2),
          ("q933a", 0))
    )


_HwMusaFrcLogPortSigProtocalType_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigProtocalType_Object = MibTableColumn
hwMusaFrcLogPortSigProtocalType = _HwMusaFrcLogPortSigProtocalType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 2),
    _HwMusaFrcLogPortSigProtocalType_Type()
)
hwMusaFrcLogPortSigProtocalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigProtocalType.setStatus("mandatory")


class _HwMusaFrcLogPortSigPortType_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bid", 3),
          ("net", 2),
          ("user", 1))
    )


_HwMusaFrcLogPortSigPortType_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigPortType_Object = MibTableColumn
hwMusaFrcLogPortSigPortType = _HwMusaFrcLogPortSigPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 3),
    _HwMusaFrcLogPortSigPortType_Type()
)
hwMusaFrcLogPortSigPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigPortType.setStatus("mandatory")


class _HwMusaFrcLogPortSigN391_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigN391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMusaFrcLogPortSigN391_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigN391_Object = MibTableColumn
hwMusaFrcLogPortSigN391 = _HwMusaFrcLogPortSigN391_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 4),
    _HwMusaFrcLogPortSigN391_Type()
)
hwMusaFrcLogPortSigN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigN391.setStatus("mandatory")


class _HwMusaFrcLogPortSigUserN392_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigUserN392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMusaFrcLogPortSigUserN392_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigUserN392_Object = MibTableColumn
hwMusaFrcLogPortSigUserN392 = _HwMusaFrcLogPortSigUserN392_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 5),
    _HwMusaFrcLogPortSigUserN392_Type()
)
hwMusaFrcLogPortSigUserN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigUserN392.setStatus("mandatory")


class _HwMusaFrcLogPortSigUserN393_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigUserN393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMusaFrcLogPortSigUserN393_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigUserN393_Object = MibTableColumn
hwMusaFrcLogPortSigUserN393 = _HwMusaFrcLogPortSigUserN393_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 6),
    _HwMusaFrcLogPortSigUserN393_Type()
)
hwMusaFrcLogPortSigUserN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigUserN393.setStatus("mandatory")


class _HwMusaFrcLogPortSigNetN392_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigNetN392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMusaFrcLogPortSigNetN392_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigNetN392_Object = MibTableColumn
hwMusaFrcLogPortSigNetN392 = _HwMusaFrcLogPortSigNetN392_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 7),
    _HwMusaFrcLogPortSigNetN392_Type()
)
hwMusaFrcLogPortSigNetN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigNetN392.setStatus("mandatory")


class _HwMusaFrcLogPortSigNetN393_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigNetN393 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMusaFrcLogPortSigNetN393_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigNetN393_Object = MibTableColumn
hwMusaFrcLogPortSigNetN393 = _HwMusaFrcLogPortSigNetN393_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 8),
    _HwMusaFrcLogPortSigNetN393_Type()
)
hwMusaFrcLogPortSigNetN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigNetN393.setStatus("mandatory")


class _HwMusaFrcLogPortSigT391_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigT391 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_HwMusaFrcLogPortSigT391_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigT391_Object = MibTableColumn
hwMusaFrcLogPortSigT391 = _HwMusaFrcLogPortSigT391_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 9),
    _HwMusaFrcLogPortSigT391_Type()
)
hwMusaFrcLogPortSigT391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigT391.setStatus("mandatory")


class _HwMusaFrcLogPortSigT392_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigT392 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 255),
    )


_HwMusaFrcLogPortSigT392_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigT392_Object = MibTableColumn
hwMusaFrcLogPortSigT392 = _HwMusaFrcLogPortSigT392_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 10),
    _HwMusaFrcLogPortSigT392_Type()
)
hwMusaFrcLogPortSigT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigT392.setStatus("mandatory")


class _HwMusaFrcLogPortSigOper_Type(Integer32):
    """Custom type hwMusaFrcLogPortSigOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaFrcLogPortSigOper_Type.__name__ = "Integer32"
_HwMusaFrcLogPortSigOper_Object = MibTableColumn
hwMusaFrcLogPortSigOper = _HwMusaFrcLogPortSigOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 5, 1, 11),
    _HwMusaFrcLogPortSigOper_Type()
)
hwMusaFrcLogPortSigOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogPortSigOper.setStatus("mandatory")
_HwMusaFrcIwfTable_Object = MibTable
hwMusaFrcIwfTable = _HwMusaFrcIwfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6)
)
if mibBuilder.loadTexts:
    hwMusaFrcIwfTable.setStatus("mandatory")
_HwMusaFrcIwfEntry_Object = MibTableRow
hwMusaFrcIwfEntry = _HwMusaFrcIwfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1)
)
hwMusaFrcIwfEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcIwfCcid"),
)
if mibBuilder.loadTexts:
    hwMusaFrcIwfEntry.setStatus("mandatory")


class _HwMusaFrcIwfCcid_Type(Integer32):
    """Custom type hwMusaFrcIwfCcid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_HwMusaFrcIwfCcid_Type.__name__ = "Integer32"
_HwMusaFrcIwfCcid_Object = MibTableColumn
hwMusaFrcIwfCcid = _HwMusaFrcIwfCcid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 1),
    _HwMusaFrcIwfCcid_Type()
)
hwMusaFrcIwfCcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMusaFrcIwfCcid.setStatus("mandatory")


class _HwMusaFrcConnectMode_Type(Integer32):
    """Custom type hwMusaFrcConnectMode based on Integer32"""
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
        *(("frIwf", 4),
          ("hdlc", 2),
          ("network11", 0),
          ("networkN1", 3),
          ("service", 1))
    )


_HwMusaFrcConnectMode_Type.__name__ = "Integer32"
_HwMusaFrcConnectMode_Object = MibTableColumn
hwMusaFrcConnectMode = _HwMusaFrcConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 2),
    _HwMusaFrcConnectMode_Type()
)
hwMusaFrcConnectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcConnectMode.setStatus("mandatory")


class _HwMusaFrcLogicPort_Type(Integer32):
    """Custom type hwMusaFrcLogicPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 494),
    )


_HwMusaFrcLogicPort_Type.__name__ = "Integer32"
_HwMusaFrcLogicPort_Object = MibTableColumn
hwMusaFrcLogicPort = _HwMusaFrcLogicPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 3),
    _HwMusaFrcLogicPort_Type()
)
hwMusaFrcLogicPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcLogicPort.setStatus("mandatory")
_HwMusaFrcDlci_Type = Integer32
_HwMusaFrcDlci_Object = MibTableColumn
hwMusaFrcDlci = _HwMusaFrcDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 4),
    _HwMusaFrcDlci_Type()
)
hwMusaFrcDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDlci.setStatus("mandatory")


class _HwMusaFrcAtmVcc_Type(Integer32):
    """Custom type hwMusaFrcAtmVcc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 494),
    )


_HwMusaFrcAtmVcc_Type.__name__ = "Integer32"
_HwMusaFrcAtmVcc_Object = MibTableColumn
hwMusaFrcAtmVcc = _HwMusaFrcAtmVcc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 5),
    _HwMusaFrcAtmVcc_Type()
)
hwMusaFrcAtmVcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcAtmVcc.setStatus("mandatory")
_HwMusaFrcAtmDlci_Type = Integer32
_HwMusaFrcAtmDlci_Object = MibTableColumn
hwMusaFrcAtmDlci = _HwMusaFrcAtmDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 6),
    _HwMusaFrcAtmDlci_Type()
)
hwMusaFrcAtmDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcAtmDlci.setStatus("mandatory")


class _HwMusaFrcEfci_Type(Integer32):
    """Custom type hwMusaFrcEfci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("efcn", 0),
          ("valure0", 1))
    )


_HwMusaFrcEfci_Type.__name__ = "Integer32"
_HwMusaFrcEfci_Object = MibTableColumn
hwMusaFrcEfci = _HwMusaFrcEfci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 7),
    _HwMusaFrcEfci_Type()
)
hwMusaFrcEfci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcEfci.setStatus("mandatory")


class _HwMusaFrcDe_Type(Integer32):
    """Custom type hwMusaFrcDe based on Integer32"""
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
        *(("netdeClpFrsscs", 0),
          ("netdeFrsscs", 1),
          ("srvde0", 3),
          ("srvde1", 4),
          ("srvdeClp", 2))
    )


_HwMusaFrcDe_Type.__name__ = "Integer32"
_HwMusaFrcDe_Object = MibTableColumn
hwMusaFrcDe = _HwMusaFrcDe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 8),
    _HwMusaFrcDe_Type()
)
hwMusaFrcDe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDe.setStatus("mandatory")


class _HwMusaFrcClp_Type(Integer32):
    """Custom type hwMusaFrcClp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clp0", 1),
          ("clp1", 2),
          ("clpDe", 0))
    )


_HwMusaFrcClp_Type.__name__ = "Integer32"
_HwMusaFrcClp_Object = MibTableColumn
hwMusaFrcClp = _HwMusaFrcClp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 9),
    _HwMusaFrcClp_Type()
)
hwMusaFrcClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcClp.setStatus("mandatory")


class _HwMusaFrcCir_Type(Integer32):
    """Custom type hwMusaFrcCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HwMusaFrcCir_Type.__name__ = "Integer32"
_HwMusaFrcCir_Object = MibTableColumn
hwMusaFrcCir = _HwMusaFrcCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 10),
    _HwMusaFrcCir_Type()
)
hwMusaFrcCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcCir.setStatus("mandatory")


class _HwMusaFrcEir_Type(Integer32):
    """Custom type hwMusaFrcEir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1984),
    )


_HwMusaFrcEir_Type.__name__ = "Integer32"
_HwMusaFrcEir_Object = MibTableColumn
hwMusaFrcEir = _HwMusaFrcEir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 11),
    _HwMusaFrcEir_Type()
)
hwMusaFrcEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcEir.setStatus("mandatory")


class _HwMusaFrcServiceMode_Type(Integer32):
    """Custom type hwMusaFrcServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMusaFrcServiceMode_Type.__name__ = "Integer32"
_HwMusaFrcServiceMode_Object = MibTableColumn
hwMusaFrcServiceMode = _HwMusaFrcServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 12),
    _HwMusaFrcServiceMode_Type()
)
hwMusaFrcServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcServiceMode.setStatus("mandatory")


class _HwMusaFrcOperate_Type(Integer32):
    """Custom type hwMusaFrcOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("del", 1))
    )


_HwMusaFrcOperate_Type.__name__ = "Integer32"
_HwMusaFrcOperate_Object = MibTableColumn
hwMusaFrcOperate = _HwMusaFrcOperate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 6, 1, 13),
    _HwMusaFrcOperate_Type()
)
hwMusaFrcOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcOperate.setStatus("mandatory")
_HwMusaFrcLogicPortStatisTable_Object = MibTable
hwMusaFrcLogicPortStatisTable = _HwMusaFrcLogicPortStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7)
)
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortStatisTable.setStatus("mandatory")
_HwMusaFrcLogicPortStatisEntry_Object = MibTableRow
hwMusaFrcLogicPortStatisEntry = _HwMusaFrcLogicPortStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1)
)
hwMusaFrcLogicPortStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogicPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortStatisEntry.setStatus("mandatory")


class _HwMusaFrcLogicPortActive_Type(Integer32):
    """Custom type hwMusaFrcLogicPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_HwMusaFrcLogicPortActive_Type.__name__ = "Integer32"
_HwMusaFrcLogicPortActive_Object = MibTableColumn
hwMusaFrcLogicPortActive = _HwMusaFrcLogicPortActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 1),
    _HwMusaFrcLogicPortActive_Type()
)
hwMusaFrcLogicPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcLogicPortActive.setStatus("mandatory")


class _HwMusaFrcCongestState_Type(Integer32):
    """Custom type hwMusaFrcCongestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("serious", 2),
          ("yes", 1))
    )


_HwMusaFrcCongestState_Type.__name__ = "Integer32"
_HwMusaFrcCongestState_Object = MibTableColumn
hwMusaFrcCongestState = _HwMusaFrcCongestState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 2),
    _HwMusaFrcCongestState_Type()
)
hwMusaFrcCongestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcCongestState.setStatus("mandatory")
_HwMusaFrcInFrameCount_Type = Counter32
_HwMusaFrcInFrameCount_Object = MibTableColumn
hwMusaFrcInFrameCount = _HwMusaFrcInFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 3),
    _HwMusaFrcInFrameCount_Type()
)
hwMusaFrcInFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcInFrameCount.setStatus("mandatory")
_HwMusaFrcInByteCount_Type = Counter32
_HwMusaFrcInByteCount_Object = MibTableColumn
hwMusaFrcInByteCount = _HwMusaFrcInByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 4),
    _HwMusaFrcInByteCount_Type()
)
hwMusaFrcInByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcInByteCount.setStatus("mandatory")
_HwMusaFrcInLossParkageC_Type = Counter32
_HwMusaFrcInLossParkageC_Object = MibTableColumn
hwMusaFrcInLossParkageC = _HwMusaFrcInLossParkageC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 5),
    _HwMusaFrcInLossParkageC_Type()
)
hwMusaFrcInLossParkageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcInLossParkageC.setStatus("mandatory")
_HwMusaFrcOutFrameCount_Type = Counter32
_HwMusaFrcOutFrameCount_Object = MibTableColumn
hwMusaFrcOutFrameCount = _HwMusaFrcOutFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 6),
    _HwMusaFrcOutFrameCount_Type()
)
hwMusaFrcOutFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcOutFrameCount.setStatus("mandatory")
_HwMusaFrcOutByteCount_Type = Counter32
_HwMusaFrcOutByteCount_Object = MibTableColumn
hwMusaFrcOutByteCount = _HwMusaFrcOutByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 7),
    _HwMusaFrcOutByteCount_Type()
)
hwMusaFrcOutByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcOutByteCount.setStatus("mandatory")
_HwMusaFrcOutLossParkageC_Type = Counter32
_HwMusaFrcOutLossParkageC_Object = MibTableColumn
hwMusaFrcOutLossParkageC = _HwMusaFrcOutLossParkageC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 7, 1, 8),
    _HwMusaFrcOutLossParkageC_Type()
)
hwMusaFrcOutLossParkageC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcOutLossParkageC.setStatus("mandatory")
_HwMusaFrcAtmPortStatisTable_Object = MibTable
hwMusaFrcAtmPortStatisTable = _HwMusaFrcAtmPortStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8)
)
if mibBuilder.loadTexts:
    hwMusaFrcAtmPortStatisTable.setStatus("mandatory")
_HwMusaFrcAtmPortStatisEntry_Object = MibTableRow
hwMusaFrcAtmPortStatisEntry = _HwMusaFrcAtmPortStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1)
)
hwMusaFrcAtmPortStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcAtmVcc"),
)
if mibBuilder.loadTexts:
    hwMusaFrcAtmPortStatisEntry.setStatus("mandatory")


class _HwMusaFrcAtmPortActive_Type(Integer32):
    """Custom type hwMusaFrcAtmPortActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_HwMusaFrcAtmPortActive_Type.__name__ = "Integer32"
_HwMusaFrcAtmPortActive_Object = MibTableColumn
hwMusaFrcAtmPortActive = _HwMusaFrcAtmPortActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 1),
    _HwMusaFrcAtmPortActive_Type()
)
hwMusaFrcAtmPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmPortActive.setStatus("mandatory")


class _HwMusaFrcAtmCongestState_Type(Integer32):
    """Custom type hwMusaFrcAtmCongestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("serious", 2),
          ("yes", 1))
    )


_HwMusaFrcAtmCongestState_Type.__name__ = "Integer32"
_HwMusaFrcAtmCongestState_Object = MibTableColumn
hwMusaFrcAtmCongestState = _HwMusaFrcAtmCongestState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 2),
    _HwMusaFrcAtmCongestState_Type()
)
hwMusaFrcAtmCongestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmCongestState.setStatus("mandatory")
_HwMusaFrcAtmInFrames_Type = Counter32
_HwMusaFrcAtmInFrames_Object = MibTableColumn
hwMusaFrcAtmInFrames = _HwMusaFrcAtmInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 3),
    _HwMusaFrcAtmInFrames_Type()
)
hwMusaFrcAtmInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmInFrames.setStatus("mandatory")
_HwMusaFrcAtmInBytes_Type = Counter32
_HwMusaFrcAtmInBytes_Object = MibTableColumn
hwMusaFrcAtmInBytes = _HwMusaFrcAtmInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 4),
    _HwMusaFrcAtmInBytes_Type()
)
hwMusaFrcAtmInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmInBytes.setStatus("mandatory")
_HwMusaFrcAtmInDiscards_Type = Counter32
_HwMusaFrcAtmInDiscards_Object = MibTableColumn
hwMusaFrcAtmInDiscards = _HwMusaFrcAtmInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 5),
    _HwMusaFrcAtmInDiscards_Type()
)
hwMusaFrcAtmInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmInDiscards.setStatus("mandatory")
_HwMusaFrcAtmOutFrames_Type = Counter32
_HwMusaFrcAtmOutFrames_Object = MibTableColumn
hwMusaFrcAtmOutFrames = _HwMusaFrcAtmOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 6),
    _HwMusaFrcAtmOutFrames_Type()
)
hwMusaFrcAtmOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmOutFrames.setStatus("mandatory")
_HwMusaFrcAtmOutBytes_Type = Counter32
_HwMusaFrcAtmOutBytes_Object = MibTableColumn
hwMusaFrcAtmOutBytes = _HwMusaFrcAtmOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 7),
    _HwMusaFrcAtmOutBytes_Type()
)
hwMusaFrcAtmOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmOutBytes.setStatus("mandatory")
_HwMusaFrcAtmOutDiscards_Type = Counter32
_HwMusaFrcAtmOutDiscards_Object = MibTableColumn
hwMusaFrcAtmOutDiscards = _HwMusaFrcAtmOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 8, 1, 8),
    _HwMusaFrcAtmOutDiscards_Type()
)
hwMusaFrcAtmOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcAtmOutDiscards.setStatus("mandatory")
_HwMusaFrcSigPortStatisTable_Object = MibTable
hwMusaFrcSigPortStatisTable = _HwMusaFrcSigPortStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9)
)
if mibBuilder.loadTexts:
    hwMusaFrcSigPortStatisTable.setStatus("mandatory")
_HwMusaFrcSigPortStatisEntry_Object = MibTableRow
hwMusaFrcSigPortStatisEntry = _HwMusaFrcSigPortStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1)
)
hwMusaFrcSigPortStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogPortSigSide"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcLogicPortId"),
)
if mibBuilder.loadTexts:
    hwMusaFrcSigPortStatisEntry.setStatus("mandatory")


class _HwMusaFrcSigType_Type(Integer32):
    """Custom type hwMusaFrcSigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidside", 3),
          ("networkside", 2),
          ("userside", 1))
    )


_HwMusaFrcSigType_Type.__name__ = "Integer32"
_HwMusaFrcSigType_Object = MibTableColumn
hwMusaFrcSigType = _HwMusaFrcSigType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 1),
    _HwMusaFrcSigType_Type()
)
hwMusaFrcSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcSigType.setStatus("mandatory")


class _HwMusaFrcSigPortSide_Type(Integer32):
    """Custom type hwMusaFrcSigPortSide based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("atm", 1),
          ("fr", 0))
    )


_HwMusaFrcSigPortSide_Type.__name__ = "Integer32"
_HwMusaFrcSigPortSide_Object = MibTableColumn
hwMusaFrcSigPortSide = _HwMusaFrcSigPortSide_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 2),
    _HwMusaFrcSigPortSide_Type()
)
hwMusaFrcSigPortSide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcSigPortSide.setStatus("mandatory")
_HwMusaFrcUserLinkC_Type = Counter32
_HwMusaFrcUserLinkC_Object = MibTableColumn
hwMusaFrcUserLinkC = _HwMusaFrcUserLinkC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 3),
    _HwMusaFrcUserLinkC_Type()
)
hwMusaFrcUserLinkC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUserLinkC.setStatus("mandatory")
_HwMusaFrcUserProtocalC_Type = Counter32
_HwMusaFrcUserProtocalC_Object = MibTableColumn
hwMusaFrcUserProtocalC = _HwMusaFrcUserProtocalC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 4),
    _HwMusaFrcUserProtocalC_Type()
)
hwMusaFrcUserProtocalC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUserProtocalC.setStatus("mandatory")
_HwMusaFrcUserDeactC_Type = Counter32
_HwMusaFrcUserDeactC_Object = MibTableColumn
hwMusaFrcUserDeactC = _HwMusaFrcUserDeactC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 5),
    _HwMusaFrcUserDeactC_Type()
)
hwMusaFrcUserDeactC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUserDeactC.setStatus("mandatory")
_HwMusaFrcNetworkLinkC_Type = Counter32
_HwMusaFrcNetworkLinkC_Object = MibTableColumn
hwMusaFrcNetworkLinkC = _HwMusaFrcNetworkLinkC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 6),
    _HwMusaFrcNetworkLinkC_Type()
)
hwMusaFrcNetworkLinkC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcNetworkLinkC.setStatus("mandatory")
_HwMusaFrcNetworkProtocalC_Type = Counter32
_HwMusaFrcNetworkProtocalC_Object = MibTableColumn
hwMusaFrcNetworkProtocalC = _HwMusaFrcNetworkProtocalC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 7),
    _HwMusaFrcNetworkProtocalC_Type()
)
hwMusaFrcNetworkProtocalC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcNetworkProtocalC.setStatus("mandatory")
_HwMusaFrcNetworkDeactC_Type = Counter32
_HwMusaFrcNetworkDeactC_Object = MibTableColumn
hwMusaFrcNetworkDeactC = _HwMusaFrcNetworkDeactC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 8),
    _HwMusaFrcNetworkDeactC_Type()
)
hwMusaFrcNetworkDeactC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcNetworkDeactC.setStatus("mandatory")
_HwMusaFrcSendFrameC_Type = Counter32
_HwMusaFrcSendFrameC_Object = MibTableColumn
hwMusaFrcSendFrameC = _HwMusaFrcSendFrameC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 9),
    _HwMusaFrcSendFrameC_Type()
)
hwMusaFrcSendFrameC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcSendFrameC.setStatus("mandatory")
_HwMusaFrcRecvFrameC_Type = Counter32
_HwMusaFrcRecvFrameC_Object = MibTableColumn
hwMusaFrcRecvFrameC = _HwMusaFrcRecvFrameC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 9, 1, 10),
    _HwMusaFrcRecvFrameC_Type()
)
hwMusaFrcRecvFrameC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcRecvFrameC.setStatus("mandatory")
_HwMusaFrcIwfStatisTable_Object = MibTable
hwMusaFrcIwfStatisTable = _HwMusaFrcIwfStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10)
)
if mibBuilder.loadTexts:
    hwMusaFrcIwfStatisTable.setStatus("mandatory")
_HwMusaFrcIwfStatisEntry_Object = MibTableRow
hwMusaFrcIwfStatisEntry = _HwMusaFrcIwfStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1)
)
hwMusaFrcIwfStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaFrcIwfCcid"),
)
if mibBuilder.loadTexts:
    hwMusaFrcIwfStatisEntry.setStatus("mandatory")


class _HwMusaFrcPvcType_Type(Integer32):
    """Custom type hwMusaFrcPvcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("networkiwf", 0),
          ("ppp", 3),
          ("serviceiwf", 1))
    )


_HwMusaFrcPvcType_Type.__name__ = "Integer32"
_HwMusaFrcPvcType_Object = MibTableColumn
hwMusaFrcPvcType = _HwMusaFrcPvcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 1),
    _HwMusaFrcPvcType_Type()
)
hwMusaFrcPvcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPvcType.setStatus("mandatory")
_HwMusaFrcPortId_Type = Integer32
_HwMusaFrcPortId_Object = MibTableColumn
hwMusaFrcPortId = _HwMusaFrcPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 2),
    _HwMusaFrcPortId_Type()
)
hwMusaFrcPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPortId.setStatus("mandatory")
_HwMusaFrcPortDlci_Type = Integer32
_HwMusaFrcPortDlci_Object = MibTableColumn
hwMusaFrcPortDlci = _HwMusaFrcPortDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 3),
    _HwMusaFrcPortDlci_Type()
)
hwMusaFrcPortDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcPortDlci.setStatus("mandatory")
_HwMusaFrcUpInFrames_Type = Counter32
_HwMusaFrcUpInFrames_Object = MibTableColumn
hwMusaFrcUpInFrames = _HwMusaFrcUpInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 4),
    _HwMusaFrcUpInFrames_Type()
)
hwMusaFrcUpInFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpInFrames.setStatus("mandatory")
_HwMusaFrcUpInBytes_Type = Counter32
_HwMusaFrcUpInBytes_Object = MibTableColumn
hwMusaFrcUpInBytes = _HwMusaFrcUpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 5),
    _HwMusaFrcUpInBytes_Type()
)
hwMusaFrcUpInBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpInBytes.setStatus("mandatory")
_HwMusaFrcUpInDiscards_Type = Counter32
_HwMusaFrcUpInDiscards_Object = MibTableColumn
hwMusaFrcUpInDiscards = _HwMusaFrcUpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 6),
    _HwMusaFrcUpInDiscards_Type()
)
hwMusaFrcUpInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpInDiscards.setStatus("mandatory")
_HwMusaFrcUpOutFrames_Type = Counter32
_HwMusaFrcUpOutFrames_Object = MibTableColumn
hwMusaFrcUpOutFrames = _HwMusaFrcUpOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 7),
    _HwMusaFrcUpOutFrames_Type()
)
hwMusaFrcUpOutFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpOutFrames.setStatus("mandatory")
_HwMusaFrcUpOutBytes_Type = Counter32
_HwMusaFrcUpOutBytes_Object = MibTableColumn
hwMusaFrcUpOutBytes = _HwMusaFrcUpOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 8),
    _HwMusaFrcUpOutBytes_Type()
)
hwMusaFrcUpOutBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpOutBytes.setStatus("mandatory")
_HwMusaFrcUpOutDiscards_Type = Counter32
_HwMusaFrcUpOutDiscards_Object = MibTableColumn
hwMusaFrcUpOutDiscards = _HwMusaFrcUpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 9),
    _HwMusaFrcUpOutDiscards_Type()
)
hwMusaFrcUpOutDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcUpOutDiscards.setStatus("mandatory")
_HwMusaFrcAtmPort_Type = Integer32
_HwMusaFrcAtmPort_Object = MibTableColumn
hwMusaFrcAtmPort = _HwMusaFrcAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 10),
    _HwMusaFrcAtmPort_Type()
)
hwMusaFrcAtmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcAtmPort.setStatus("mandatory")
_HwMusaFrcAtmPortDlci_Type = Integer32
_HwMusaFrcAtmPortDlci_Object = MibTableColumn
hwMusaFrcAtmPortDlci = _HwMusaFrcAtmPortDlci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 11),
    _HwMusaFrcAtmPortDlci_Type()
)
hwMusaFrcAtmPortDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcAtmPortDlci.setStatus("mandatory")
_HwMusaFrcDownInFrames_Type = Counter32
_HwMusaFrcDownInFrames_Object = MibTableColumn
hwMusaFrcDownInFrames = _HwMusaFrcDownInFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 12),
    _HwMusaFrcDownInFrames_Type()
)
hwMusaFrcDownInFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownInFrames.setStatus("mandatory")
_HwMusaFrcDownInBytes_Type = Counter32
_HwMusaFrcDownInBytes_Object = MibTableColumn
hwMusaFrcDownInBytes = _HwMusaFrcDownInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 13),
    _HwMusaFrcDownInBytes_Type()
)
hwMusaFrcDownInBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownInBytes.setStatus("mandatory")
_HwMusaFrcDownInDiscards_Type = Counter32
_HwMusaFrcDownInDiscards_Object = MibTableColumn
hwMusaFrcDownInDiscards = _HwMusaFrcDownInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 14),
    _HwMusaFrcDownInDiscards_Type()
)
hwMusaFrcDownInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownInDiscards.setStatus("mandatory")
_HwMusaFrcDownOutFrames_Type = Counter32
_HwMusaFrcDownOutFrames_Object = MibTableColumn
hwMusaFrcDownOutFrames = _HwMusaFrcDownOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 15),
    _HwMusaFrcDownOutFrames_Type()
)
hwMusaFrcDownOutFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownOutFrames.setStatus("mandatory")
_HwMusaFrcDownOutBytes_Type = Counter32
_HwMusaFrcDownOutBytes_Object = MibTableColumn
hwMusaFrcDownOutBytes = _HwMusaFrcDownOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 16),
    _HwMusaFrcDownOutBytes_Type()
)
hwMusaFrcDownOutBytes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownOutBytes.setStatus("mandatory")
_HwMusaFrcDownOutDiscards_Type = Counter32
_HwMusaFrcDownOutDiscards_Object = MibTableColumn
hwMusaFrcDownOutDiscards = _HwMusaFrcDownOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 17),
    _HwMusaFrcDownOutDiscards_Type()
)
hwMusaFrcDownOutDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcDownOutDiscards.setStatus("mandatory")
_HwMusaFrcIwfActive_Type = Integer32
_HwMusaFrcIwfActive_Object = MibTableColumn
hwMusaFrcIwfActive = _HwMusaFrcIwfActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 10, 1, 18),
    _HwMusaFrcIwfActive_Type()
)
hwMusaFrcIwfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMusaFrcIwfActive.setStatus("mandatory")
_HwMusaFrcPhyStatisGroup_ObjectIdentity = ObjectIdentity
hwMusaFrcPhyStatisGroup = _HwMusaFrcPhyStatisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11)
)
_HwMusaFrcPhyMCCStatisTable_Object = MibTable
hwMusaFrcPhyMCCStatisTable = _HwMusaFrcPhyMCCStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1)
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyMCCStatisTable.setStatus("mandatory")
_HwMusaFrcPhyMCCStatisEntry_Object = MibTableRow
hwMusaFrcPhyMCCStatisEntry = _HwMusaFrcPhyMCCStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1)
)
hwMusaFrcPhyMCCStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
    (0, "HUAWEI-FRC-MA5100-MIB", "hwMusaMccType"),
)
if mibBuilder.loadTexts:
    hwMusaFrcPhyMCCStatisEntry.setStatus("mandatory")


class _HwMusaMccType_Type(Integer32):
    """Custom type hwMusaMccType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcc1", 1),
          ("mcc2", 2))
    )


_HwMusaMccType_Type.__name__ = "Integer32"
_HwMusaMccType_Object = MibTableColumn
hwMusaMccType = _HwMusaMccType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 1),
    _HwMusaMccType_Type()
)
hwMusaMccType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaMccType.setStatus("mandatory")
_HwMusaFrcMccTxSucc_Type = Counter32
_HwMusaFrcMccTxSucc_Object = MibTableColumn
hwMusaFrcMccTxSucc = _HwMusaFrcMccTxSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 2),
    _HwMusaFrcMccTxSucc_Type()
)
hwMusaFrcMccTxSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxSucc.setStatus("mandatory")
_HwMusaFrcMccRxSucc_Type = Counter32
_HwMusaFrcMccRxSucc_Object = MibTableColumn
hwMusaFrcMccRxSucc = _HwMusaFrcMccRxSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 3),
    _HwMusaFrcMccRxSucc_Type()
)
hwMusaFrcMccRxSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxSucc.setStatus("mandatory")
_HwMusaFrcMccRxQOV_Type = Counter32
_HwMusaFrcMccRxQOV_Object = MibTableColumn
hwMusaFrcMccRxQOV = _HwMusaFrcMccRxQOV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 4),
    _HwMusaFrcMccRxQOV_Type()
)
hwMusaFrcMccRxQOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxQOV.setStatus("mandatory")
_HwMusaFrcMccRxMRF_Type = Counter32
_HwMusaFrcMccRxMRF_Object = MibTableColumn
hwMusaFrcMccRxMRF = _HwMusaFrcMccRxMRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 5),
    _HwMusaFrcMccRxMRF_Type()
)
hwMusaFrcMccRxMRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxMRF.setStatus("mandatory")
_HwMusaFrcMccRxLRF_Type = Counter32
_HwMusaFrcMccRxLRF_Object = MibTableColumn
hwMusaFrcMccRxLRF = _HwMusaFrcMccRxLRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 6),
    _HwMusaFrcMccRxLRF_Type()
)
hwMusaFrcMccRxLRF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxLRF.setStatus("mandatory")
_HwMusaFrcMccRxIDL_Type = Counter32
_HwMusaFrcMccRxIDL_Object = MibTableColumn
hwMusaFrcMccRxIDL = _HwMusaFrcMccRxIDL_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 7),
    _HwMusaFrcMccRxIDL_Type()
)
hwMusaFrcMccRxIDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxIDL.setStatus("mandatory")
_HwMusaFrcMccRxBSY_Type = Counter32
_HwMusaFrcMccRxBSY_Object = MibTableColumn
hwMusaFrcMccRxBSY = _HwMusaFrcMccRxBSY_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 8),
    _HwMusaFrcMccRxBSY_Type()
)
hwMusaFrcMccRxBSY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxBSY.setStatus("mandatory")
_HwMusaFrcMccRxLG_Type = Counter32
_HwMusaFrcMccRxLG_Object = MibTableColumn
hwMusaFrcMccRxLG = _HwMusaFrcMccRxLG_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 9),
    _HwMusaFrcMccRxLG_Type()
)
hwMusaFrcMccRxLG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxLG.setStatus("mandatory")
_HwMusaFrcMccRxNO_Type = Counter32
_HwMusaFrcMccRxNO_Object = MibTableColumn
hwMusaFrcMccRxNO = _HwMusaFrcMccRxNO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 10),
    _HwMusaFrcMccRxNO_Type()
)
hwMusaFrcMccRxNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxNO.setStatus("mandatory")
_HwMusaFrcMccRxAB_Type = Counter32
_HwMusaFrcMccRxAB_Object = MibTableColumn
hwMusaFrcMccRxAB = _HwMusaFrcMccRxAB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 11),
    _HwMusaFrcMccRxAB_Type()
)
hwMusaFrcMccRxAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxAB.setStatus("mandatory")
_HwMusaFrcMccRxCR_Type = Counter32
_HwMusaFrcMccRxCR_Object = MibTableColumn
hwMusaFrcMccRxCR = _HwMusaFrcMccRxCR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 12),
    _HwMusaFrcMccRxCR_Type()
)
hwMusaFrcMccRxCR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxCR.setStatus("mandatory")
_HwMusaFrcMccTxRxNID_Type = Counter32
_HwMusaFrcMccTxRxNID_Object = MibTableColumn
hwMusaFrcMccTxRxNID = _HwMusaFrcMccTxRxNID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 13),
    _HwMusaFrcMccTxRxNID_Type()
)
hwMusaFrcMccTxRxNID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxRxNID.setStatus("mandatory")
_HwMusaFrcMccTxQOV_Type = Counter32
_HwMusaFrcMccTxQOV_Object = MibTableColumn
hwMusaFrcMccTxQOV = _HwMusaFrcMccTxQOV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 14),
    _HwMusaFrcMccTxQOV_Type()
)
hwMusaFrcMccTxQOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxQOV.setStatus("mandatory")
_HwMusaFrcMccTxGUN_Type = Counter32
_HwMusaFrcMccTxGUN_Object = MibTableColumn
hwMusaFrcMccTxGUN = _HwMusaFrcMccTxGUN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 15),
    _HwMusaFrcMccTxGUN_Type()
)
hwMusaFrcMccTxGUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxGUN.setStatus("mandatory")
_HwMusaFrcMccTxGOV_Type = Counter32
_HwMusaFrcMccTxGOV_Object = MibTableColumn
hwMusaFrcMccTxGOV = _HwMusaFrcMccTxGOV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 16),
    _HwMusaFrcMccTxGOV_Type()
)
hwMusaFrcMccTxGOV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxGOV.setStatus("mandatory")
_HwMusaFrcMccTxUN_Type = Counter32
_HwMusaFrcMccTxUN_Object = MibTableColumn
hwMusaFrcMccTxUN = _HwMusaFrcMccTxUN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 17),
    _HwMusaFrcMccTxUN_Type()
)
hwMusaFrcMccTxUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxUN.setStatus("mandatory")
_HwMusaFrcMccTxNoBD_Type = Counter32
_HwMusaFrcMccTxNoBD_Object = MibTableColumn
hwMusaFrcMccTxNoBD = _HwMusaFrcMccTxNoBD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 18),
    _HwMusaFrcMccTxNoBD_Type()
)
hwMusaFrcMccTxNoBD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccTxNoBD.setStatus("mandatory")
_HwMusaFrcMccRxNoBuff_Type = Counter32
_HwMusaFrcMccRxNoBuff_Object = MibTableColumn
hwMusaFrcMccRxNoBuff = _HwMusaFrcMccRxNoBuff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 1, 1, 19),
    _HwMusaFrcMccRxNoBuff_Type()
)
hwMusaFrcMccRxNoBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcMccRxNoBuff.setStatus("mandatory")
_HwMusaFrcPhySARStatisTable_Object = MibTable
hwMusaFrcPhySARStatisTable = _HwMusaFrcPhySARStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2)
)
if mibBuilder.loadTexts:
    hwMusaFrcPhySARStatisTable.setStatus("mandatory")
_HwMusaFrcPhySARStatisEntry_Object = MibTableRow
hwMusaFrcPhySARStatisEntry = _HwMusaFrcPhySARStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1)
)
hwMusaFrcPhySARStatisEntry.setIndexNames(
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaFrameIndex"),
    (0, "HUAWEI-MUSA-MA5100-MIB", "hwMusaSlotIndex"),
)
if mibBuilder.loadTexts:
    hwMusaFrcPhySARStatisEntry.setStatus("mandatory")
_HwMusaFrcSarSendSucc_Type = Counter32
_HwMusaFrcSarSendSucc_Object = MibTableColumn
hwMusaFrcSarSendSucc = _HwMusaFrcSarSendSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 1),
    _HwMusaFrcSarSendSucc_Type()
)
hwMusaFrcSarSendSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarSendSucc.setStatus("mandatory")
_HwMusaFrcSarRecvSucc_Type = Counter32
_HwMusaFrcSarRecvSucc_Object = MibTableColumn
hwMusaFrcSarRecvSucc = _HwMusaFrcSarRecvSucc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 2),
    _HwMusaFrcSarRecvSucc_Type()
)
hwMusaFrcSarRecvSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRecvSucc.setStatus("mandatory")
_HwMusaFrcSarRxErrBSY_Type = Counter32
_HwMusaFrcSarRxErrBSY_Object = MibTableColumn
hwMusaFrcSarRxErrBSY = _HwMusaFrcSarRxErrBSY_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 3),
    _HwMusaFrcSarRxErrBSY_Type()
)
hwMusaFrcSarRxErrBSY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrBSY.setStatus("mandatory")
_HwMusaFrcSarRxErrTBNR_Type = Counter32
_HwMusaFrcSarRxErrTBNR_Object = MibTableColumn
hwMusaFrcSarRxErrTBNR = _HwMusaFrcSarRxErrTBNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 4),
    _HwMusaFrcSarRxErrTBNR_Type()
)
hwMusaFrcSarRxErrTBNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrTBNR.setStatus("mandatory")
_HwMusaFrcSarRxErrGRLI_Type = Counter32
_HwMusaFrcSarRxErrGRLI_Object = MibTableColumn
hwMusaFrcSarRxErrGRLI = _HwMusaFrcSarRxErrGRLI_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 5),
    _HwMusaFrcSarRxErrGRLI_Type()
)
hwMusaFrcSarRxErrGRLI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrGRLI.setStatus("mandatory")
_HwMusaFrcSarRxErrGBPB_Type = Counter32
_HwMusaFrcSarRxErrGBPB_Object = MibTableColumn
hwMusaFrcSarRxErrGBPB = _HwMusaFrcSarRxErrGBPB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 6),
    _HwMusaFrcSarRxErrGBPB_Type()
)
hwMusaFrcSarRxErrGBPB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrGBPB.setStatus("mandatory")
_HwMusaFrcSarRxErrINTO_Type = Counter32
_HwMusaFrcSarRxErrINTO_Object = MibTableColumn
hwMusaFrcSarRxErrINTO = _HwMusaFrcSarRxErrINTO_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 7),
    _HwMusaFrcSarRxErrINTO_Type()
)
hwMusaFrcSarRxErrINTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrINTO.setStatus("mandatory")
_HwMusaFrcSarRxErrABRT_Type = Counter32
_HwMusaFrcSarRxErrABRT_Object = MibTableColumn
hwMusaFrcSarRxErrABRT = _HwMusaFrcSarRxErrABRT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 8),
    _HwMusaFrcSarRxErrABRT_Type()
)
hwMusaFrcSarRxErrABRT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrABRT.setStatus("mandatory")
_HwMusaFrcSarRxErrLNE_Type = Counter32
_HwMusaFrcSarRxErrLNE_Object = MibTableColumn
hwMusaFrcSarRxErrLNE = _HwMusaFrcSarRxErrLNE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 9),
    _HwMusaFrcSarRxErrLNE_Type()
)
hwMusaFrcSarRxErrLNE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrLNE.setStatus("mandatory")
_HwMusaFrcSarRxErrCRE_Type = Counter32
_HwMusaFrcSarRxErrCRE_Object = MibTableColumn
hwMusaFrcSarRxErrCRE = _HwMusaFrcSarRxErrCRE_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 10),
    _HwMusaFrcSarRxErrCRE_Type()
)
hwMusaFrcSarRxErrCRE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrCRE.setStatus("mandatory")
_HwMusaFrcSarRxErrCLP_Type = Counter32
_HwMusaFrcSarRxErrCLP_Object = MibTableColumn
hwMusaFrcSarRxErrCLP = _HwMusaFrcSarRxErrCLP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 11),
    _HwMusaFrcSarRxErrCLP_Type()
)
hwMusaFrcSarRxErrCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrCLP.setStatus("mandatory")
_HwMusaFrcSarRxErrCNG_Type = Counter32
_HwMusaFrcSarRxErrCNG_Object = MibTableColumn
hwMusaFrcSarRxErrCNG = _HwMusaFrcSarRxErrCNG_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 12),
    _HwMusaFrcSarRxErrCNG_Type()
)
hwMusaFrcSarRxErrCNG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrCNG.setStatus("mandatory")
_HwMusaFrcSarRxErrCPUU_Type = Counter32
_HwMusaFrcSarRxErrCPUU_Object = MibTableColumn
hwMusaFrcSarRxErrCPUU = _HwMusaFrcSarRxErrCPUU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 13),
    _HwMusaFrcSarRxErrCPUU_Type()
)
hwMusaFrcSarRxErrCPUU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrCPUU.setStatus("mandatory")
_HwMusaFrcSarRxErrRedLine_Type = Counter32
_HwMusaFrcSarRxErrRedLine_Object = MibTableColumn
hwMusaFrcSarRxErrRedLine = _HwMusaFrcSarRxErrRedLine_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 14),
    _HwMusaFrcSarRxErrRedLine_Type()
)
hwMusaFrcSarRxErrRedLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrRedLine.setStatus("mandatory")
_HwMusaFrcSarRxErrNoBuff_Type = Counter32
_HwMusaFrcSarRxErrNoBuff_Object = MibTableColumn
hwMusaFrcSarRxErrNoBuff = _HwMusaFrcSarRxErrNoBuff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 15),
    _HwMusaFrcSarRxErrNoBuff_Type()
)
hwMusaFrcSarRxErrNoBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarRxErrNoBuff.setStatus("mandatory")
_HwMusaFrcSarTxErrTIRU_Type = Counter32
_HwMusaFrcSarTxErrTIRU_Object = MibTableColumn
hwMusaFrcSarTxErrTIRU = _HwMusaFrcSarTxErrTIRU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 16),
    _HwMusaFrcSarTxErrTIRU_Type()
)
hwMusaFrcSarTxErrTIRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarTxErrTIRU.setStatus("mandatory")
_HwMusaFrcSarTxErrNoBD_Type = Counter32
_HwMusaFrcSarTxErrNoBD_Object = MibTableColumn
hwMusaFrcSarTxErrNoBD = _HwMusaFrcSarTxErrNoBD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 6, 5, 9, 11, 2, 1, 17),
    _HwMusaFrcSarTxErrNoBD_Type()
)
hwMusaFrcSarTxErrNoBD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMusaFrcSarTxErrNoBD.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-FRC-MA5100-MIB",
    **{"hwMusaFrcMib": hwMusaFrcMib,
       "hwMusaFrcBoardTable": hwMusaFrcBoardTable,
       "hwMusaFrcBoardEntry": hwMusaFrcBoardEntry,
       "hwMusaFrcPvcAlarmEnable": hwMusaFrcPvcAlarmEnable,
       "hwMusaFrcBoardClearStatistic": hwMusaFrcBoardClearStatistic,
       "hwMusaFrcClockMode": hwMusaFrcClockMode,
       "hwMusaFrcPhyPortId": hwMusaFrcPhyPortId,
       "hwMusaFrcPhyPortType": hwMusaFrcPhyPortType,
       "hwMusaFrcPhyPortLineIfTable": hwMusaFrcPhyPortLineIfTable,
       "hwMusaFrcPhyPortLineIfEntry": hwMusaFrcPhyPortLineIfEntry,
       "hwMusaFrcMainClock": hwMusaFrcMainClock,
       "hwMusaFrcT1HaulMode": hwMusaFrcT1HaulMode,
       "hwMusaFrcT1E1Crc": hwMusaFrcT1E1Crc,
       "hwMusaFrcT1FrameFormat": hwMusaFrcT1FrameFormat,
       "hwMusaFrcT1LineCode": hwMusaFrcT1LineCode,
       "hwMusaFrcV35ClockMode": hwMusaFrcV35ClockMode,
       "hwMusaFrcT1E1TsBitMap": hwMusaFrcT1E1TsBitMap,
       "hwMusaFrcClockLoopMode": hwMusaFrcClockLoopMode,
       "hwMusaFrcLoopState": hwMusaFrcLoopState,
       "hwMusaFrcV35InvertTxClock": hwMusaFrcV35InvertTxClock,
       "hwMusaFrcSingleTimeSlotId": hwMusaFrcSingleTimeSlotId,
       "hwMusaFrcPhyPortAlarmTable": hwMusaFrcPhyPortAlarmTable,
       "hwMusaFrcPhyPortAlarmEntry": hwMusaFrcPhyPortAlarmEntry,
       "hwMusaFrcAlarmSw": hwMusaFrcAlarmSw,
       "hwMusaFrcRACTS": hwMusaFrcRACTS,
       "hwMusaFrcLFADSR": hwMusaFrcLFADSR,
       "hwMusaFrcLOSPLL": hwMusaFrcLOSPLL,
       "hwMusaFrcAISDCD": hwMusaFrcAISDCD,
       "hwMusaFrcAlarmCount": hwMusaFrcAlarmCount,
       "hwMusaFrcDTR": hwMusaFrcDTR,
       "hwMusaFrcRTS": hwMusaFrcRTS,
       "hwMusaFrcSCOL": hwMusaFrcSCOL,
       "hwMusaFrcLogicPortTable": hwMusaFrcLogicPortTable,
       "hwMusaFrcLogicPortEntry": hwMusaFrcLogicPortEntry,
       "hwMusaFrcLogicPortId": hwMusaFrcLogicPortId,
       "hwMusaFrcPhyPort": hwMusaFrcPhyPort,
       "hwMusaFrcE1T1TsBitMapV35NValue": hwMusaFrcE1T1TsBitMapV35NValue,
       "hwMusaFrcDlciType": hwMusaFrcDlciType,
       "hwMusaFrcFreeBandwidth": hwMusaFrcFreeBandwidth,
       "hwMusaFrcServiceFlag": hwMusaFrcServiceFlag,
       "hwMusaFrcPortActivate": hwMusaFrcPortActivate,
       "hwMusaFrcLogicPortOperate": hwMusaFrcLogicPortOperate,
       "hwMusaFrcLogPortSigTable": hwMusaFrcLogPortSigTable,
       "hwMusaFrcLogPortSigEntry": hwMusaFrcLogPortSigEntry,
       "hwMusaFrcLogPortSigSide": hwMusaFrcLogPortSigSide,
       "hwMusaFrcLogPortSigProtocalType": hwMusaFrcLogPortSigProtocalType,
       "hwMusaFrcLogPortSigPortType": hwMusaFrcLogPortSigPortType,
       "hwMusaFrcLogPortSigN391": hwMusaFrcLogPortSigN391,
       "hwMusaFrcLogPortSigUserN392": hwMusaFrcLogPortSigUserN392,
       "hwMusaFrcLogPortSigUserN393": hwMusaFrcLogPortSigUserN393,
       "hwMusaFrcLogPortSigNetN392": hwMusaFrcLogPortSigNetN392,
       "hwMusaFrcLogPortSigNetN393": hwMusaFrcLogPortSigNetN393,
       "hwMusaFrcLogPortSigT391": hwMusaFrcLogPortSigT391,
       "hwMusaFrcLogPortSigT392": hwMusaFrcLogPortSigT392,
       "hwMusaFrcLogPortSigOper": hwMusaFrcLogPortSigOper,
       "hwMusaFrcIwfTable": hwMusaFrcIwfTable,
       "hwMusaFrcIwfEntry": hwMusaFrcIwfEntry,
       "hwMusaFrcIwfCcid": hwMusaFrcIwfCcid,
       "hwMusaFrcConnectMode": hwMusaFrcConnectMode,
       "hwMusaFrcLogicPort": hwMusaFrcLogicPort,
       "hwMusaFrcDlci": hwMusaFrcDlci,
       "hwMusaFrcAtmVcc": hwMusaFrcAtmVcc,
       "hwMusaFrcAtmDlci": hwMusaFrcAtmDlci,
       "hwMusaFrcEfci": hwMusaFrcEfci,
       "hwMusaFrcDe": hwMusaFrcDe,
       "hwMusaFrcClp": hwMusaFrcClp,
       "hwMusaFrcCir": hwMusaFrcCir,
       "hwMusaFrcEir": hwMusaFrcEir,
       "hwMusaFrcServiceMode": hwMusaFrcServiceMode,
       "hwMusaFrcOperate": hwMusaFrcOperate,
       "hwMusaFrcLogicPortStatisTable": hwMusaFrcLogicPortStatisTable,
       "hwMusaFrcLogicPortStatisEntry": hwMusaFrcLogicPortStatisEntry,
       "hwMusaFrcLogicPortActive": hwMusaFrcLogicPortActive,
       "hwMusaFrcCongestState": hwMusaFrcCongestState,
       "hwMusaFrcInFrameCount": hwMusaFrcInFrameCount,
       "hwMusaFrcInByteCount": hwMusaFrcInByteCount,
       "hwMusaFrcInLossParkageC": hwMusaFrcInLossParkageC,
       "hwMusaFrcOutFrameCount": hwMusaFrcOutFrameCount,
       "hwMusaFrcOutByteCount": hwMusaFrcOutByteCount,
       "hwMusaFrcOutLossParkageC": hwMusaFrcOutLossParkageC,
       "hwMusaFrcAtmPortStatisTable": hwMusaFrcAtmPortStatisTable,
       "hwMusaFrcAtmPortStatisEntry": hwMusaFrcAtmPortStatisEntry,
       "hwMusaFrcAtmPortActive": hwMusaFrcAtmPortActive,
       "hwMusaFrcAtmCongestState": hwMusaFrcAtmCongestState,
       "hwMusaFrcAtmInFrames": hwMusaFrcAtmInFrames,
       "hwMusaFrcAtmInBytes": hwMusaFrcAtmInBytes,
       "hwMusaFrcAtmInDiscards": hwMusaFrcAtmInDiscards,
       "hwMusaFrcAtmOutFrames": hwMusaFrcAtmOutFrames,
       "hwMusaFrcAtmOutBytes": hwMusaFrcAtmOutBytes,
       "hwMusaFrcAtmOutDiscards": hwMusaFrcAtmOutDiscards,
       "hwMusaFrcSigPortStatisTable": hwMusaFrcSigPortStatisTable,
       "hwMusaFrcSigPortStatisEntry": hwMusaFrcSigPortStatisEntry,
       "hwMusaFrcSigType": hwMusaFrcSigType,
       "hwMusaFrcSigPortSide": hwMusaFrcSigPortSide,
       "hwMusaFrcUserLinkC": hwMusaFrcUserLinkC,
       "hwMusaFrcUserProtocalC": hwMusaFrcUserProtocalC,
       "hwMusaFrcUserDeactC": hwMusaFrcUserDeactC,
       "hwMusaFrcNetworkLinkC": hwMusaFrcNetworkLinkC,
       "hwMusaFrcNetworkProtocalC": hwMusaFrcNetworkProtocalC,
       "hwMusaFrcNetworkDeactC": hwMusaFrcNetworkDeactC,
       "hwMusaFrcSendFrameC": hwMusaFrcSendFrameC,
       "hwMusaFrcRecvFrameC": hwMusaFrcRecvFrameC,
       "hwMusaFrcIwfStatisTable": hwMusaFrcIwfStatisTable,
       "hwMusaFrcIwfStatisEntry": hwMusaFrcIwfStatisEntry,
       "hwMusaFrcPvcType": hwMusaFrcPvcType,
       "hwMusaFrcPortId": hwMusaFrcPortId,
       "hwMusaFrcPortDlci": hwMusaFrcPortDlci,
       "hwMusaFrcUpInFrames": hwMusaFrcUpInFrames,
       "hwMusaFrcUpInBytes": hwMusaFrcUpInBytes,
       "hwMusaFrcUpInDiscards": hwMusaFrcUpInDiscards,
       "hwMusaFrcUpOutFrames": hwMusaFrcUpOutFrames,
       "hwMusaFrcUpOutBytes": hwMusaFrcUpOutBytes,
       "hwMusaFrcUpOutDiscards": hwMusaFrcUpOutDiscards,
       "hwMusaFrcAtmPort": hwMusaFrcAtmPort,
       "hwMusaFrcAtmPortDlci": hwMusaFrcAtmPortDlci,
       "hwMusaFrcDownInFrames": hwMusaFrcDownInFrames,
       "hwMusaFrcDownInBytes": hwMusaFrcDownInBytes,
       "hwMusaFrcDownInDiscards": hwMusaFrcDownInDiscards,
       "hwMusaFrcDownOutFrames": hwMusaFrcDownOutFrames,
       "hwMusaFrcDownOutBytes": hwMusaFrcDownOutBytes,
       "hwMusaFrcDownOutDiscards": hwMusaFrcDownOutDiscards,
       "hwMusaFrcIwfActive": hwMusaFrcIwfActive,
       "hwMusaFrcPhyStatisGroup": hwMusaFrcPhyStatisGroup,
       "hwMusaFrcPhyMCCStatisTable": hwMusaFrcPhyMCCStatisTable,
       "hwMusaFrcPhyMCCStatisEntry": hwMusaFrcPhyMCCStatisEntry,
       "hwMusaMccType": hwMusaMccType,
       "hwMusaFrcMccTxSucc": hwMusaFrcMccTxSucc,
       "hwMusaFrcMccRxSucc": hwMusaFrcMccRxSucc,
       "hwMusaFrcMccRxQOV": hwMusaFrcMccRxQOV,
       "hwMusaFrcMccRxMRF": hwMusaFrcMccRxMRF,
       "hwMusaFrcMccRxLRF": hwMusaFrcMccRxLRF,
       "hwMusaFrcMccRxIDL": hwMusaFrcMccRxIDL,
       "hwMusaFrcMccRxBSY": hwMusaFrcMccRxBSY,
       "hwMusaFrcMccRxLG": hwMusaFrcMccRxLG,
       "hwMusaFrcMccRxNO": hwMusaFrcMccRxNO,
       "hwMusaFrcMccRxAB": hwMusaFrcMccRxAB,
       "hwMusaFrcMccRxCR": hwMusaFrcMccRxCR,
       "hwMusaFrcMccTxRxNID": hwMusaFrcMccTxRxNID,
       "hwMusaFrcMccTxQOV": hwMusaFrcMccTxQOV,
       "hwMusaFrcMccTxGUN": hwMusaFrcMccTxGUN,
       "hwMusaFrcMccTxGOV": hwMusaFrcMccTxGOV,
       "hwMusaFrcMccTxUN": hwMusaFrcMccTxUN,
       "hwMusaFrcMccTxNoBD": hwMusaFrcMccTxNoBD,
       "hwMusaFrcMccRxNoBuff": hwMusaFrcMccRxNoBuff,
       "hwMusaFrcPhySARStatisTable": hwMusaFrcPhySARStatisTable,
       "hwMusaFrcPhySARStatisEntry": hwMusaFrcPhySARStatisEntry,
       "hwMusaFrcSarSendSucc": hwMusaFrcSarSendSucc,
       "hwMusaFrcSarRecvSucc": hwMusaFrcSarRecvSucc,
       "hwMusaFrcSarRxErrBSY": hwMusaFrcSarRxErrBSY,
       "hwMusaFrcSarRxErrTBNR": hwMusaFrcSarRxErrTBNR,
       "hwMusaFrcSarRxErrGRLI": hwMusaFrcSarRxErrGRLI,
       "hwMusaFrcSarRxErrGBPB": hwMusaFrcSarRxErrGBPB,
       "hwMusaFrcSarRxErrINTO": hwMusaFrcSarRxErrINTO,
       "hwMusaFrcSarRxErrABRT": hwMusaFrcSarRxErrABRT,
       "hwMusaFrcSarRxErrLNE": hwMusaFrcSarRxErrLNE,
       "hwMusaFrcSarRxErrCRE": hwMusaFrcSarRxErrCRE,
       "hwMusaFrcSarRxErrCLP": hwMusaFrcSarRxErrCLP,
       "hwMusaFrcSarRxErrCNG": hwMusaFrcSarRxErrCNG,
       "hwMusaFrcSarRxErrCPUU": hwMusaFrcSarRxErrCPUU,
       "hwMusaFrcSarRxErrRedLine": hwMusaFrcSarRxErrRedLine,
       "hwMusaFrcSarRxErrNoBuff": hwMusaFrcSarRxErrNoBuff,
       "hwMusaFrcSarTxErrTIRU": hwMusaFrcSarTxErrTIRU,
       "hwMusaFrcSarTxErrNoBD": hwMusaFrcSarTxErrNoBD}
)
