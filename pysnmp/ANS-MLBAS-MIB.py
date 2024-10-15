# SNMP MIB module (ANS-MLBAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ANS-MLBAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:59 2024
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

(DateAndTime,
 RowPointer,
 RowStatus,
 mlpmpR115) = mibBuilder.importSymbols(
    "ANS-COMMON-MIB",
    "DateAndTime",
    "RowPointer",
    "RowStatus",
    "mlpmpR115")

(ansBoardPosition,
 ansBoardSubrackIndex,
 ansBoardSystemNodeIndex,
 ansSlotPosition,
 ansSlotSubrackIndex,
 ansSlotSystemNodeIndex) = mibBuilder.importSymbols(
    "ANS-EQUIPMENT-MIB",
    "ansBoardPosition",
    "ansBoardSubrackIndex",
    "ansBoardSystemNodeIndex",
    "ansSlotPosition",
    "ansSlotSubrackIndex",
    "ansSlotSystemNodeIndex")

(ansAccessUserPortIndex,
 ansAccessUserPortPosition,
 ansAccessUserPortSubrack,
 ansAccessUserPortSystemNode) = mibBuilder.importSymbols(
    "ANS-GS-MIB",
    "ansAccessUserPortIndex",
    "ansAccessUserPortPosition",
    "ansAccessUserPortSubrack",
    "ansAccessUserPortSystemNode")

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

_Mlbas_ObjectIdentity = ObjectIdentity
mlbas = _Mlbas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5)
)
_MlbasRadioNode_ObjectIdentity = ObjectIdentity
mlbasRadioNode = _MlbasRadioNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1)
)
_MlbasRadioNodeTable_Object = MibTable
mlbasRadioNodeTable = _MlbasRadioNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1)
)
if mibBuilder.loadTexts:
    mlbasRadioNodeTable.setStatus("mandatory")
_MlbasRadioNodeEntry_Object = MibTableRow
mlbasRadioNodeEntry = _MlbasRadioNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1)
)
mlbasRadioNodeEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    mlbasRadioNodeEntry.setStatus("mandatory")


class _MlbasRnCUId_Type(DisplayString):
    """Custom type mlbasRnCUId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasRnCUId_Type.__name__ = "DisplayString"
_MlbasRnCUId_Object = MibTableColumn
mlbasRnCUId = _MlbasRnCUId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 1),
    _MlbasRnCUId_Type()
)
mlbasRnCUId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUId.setStatus("mandatory")


class _MlbasRnCUSecurity_Type(Integer32):
    """Custom type mlbasRnCUSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MlbasRnCUSecurity_Type.__name__ = "Integer32"
_MlbasRnCUSecurity_Object = MibTableColumn
mlbasRnCUSecurity = _MlbasRnCUSecurity_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 2),
    _MlbasRnCUSecurity_Type()
)
mlbasRnCUSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUSecurity.setStatus("mandatory")


class _MlbasRnCUBerThreshold_Type(Integer32):
    """Custom type mlbasRnCUBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ber3", 3),
          ("ber4", 4),
          ("ber5", 5),
          ("ber6", 6))
    )


_MlbasRnCUBerThreshold_Type.__name__ = "Integer32"
_MlbasRnCUBerThreshold_Object = MibTableColumn
mlbasRnCUBerThreshold = _MlbasRnCUBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 3),
    _MlbasRnCUBerThreshold_Type()
)
mlbasRnCUBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUBerThreshold.setStatus("mandatory")


class _MlbasRnCUBwLimit_Type(Integer32):
    """Custom type mlbasRnCUBwLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MlbasRnCUBwLimit_Type.__name__ = "Integer32"
_MlbasRnCUBwLimit_Object = MibTableColumn
mlbasRnCUBwLimit = _MlbasRnCUBwLimit_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 4),
    _MlbasRnCUBwLimit_Type()
)
mlbasRnCUBwLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUBwLimit.setStatus("mandatory")


class _MlbasRnCULoopMode_Type(Integer32):
    """Custom type mlbasRnCULoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("permanent", 2),
          ("selfTest", 3))
    )


_MlbasRnCULoopMode_Type.__name__ = "Integer32"
_MlbasRnCULoopMode_Object = MibTableColumn
mlbasRnCULoopMode = _MlbasRnCULoopMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 5),
    _MlbasRnCULoopMode_Type()
)
mlbasRnCULoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCULoopMode.setStatus("mandatory")


class _MlbasRnCULoopPoint_Type(Integer32):
    """Custom type mlbasRnCULoopPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modem", 1),
          ("radio", 2))
    )


_MlbasRnCULoopPoint_Type.__name__ = "Integer32"
_MlbasRnCULoopPoint_Object = MibTableColumn
mlbasRnCULoopPoint = _MlbasRnCULoopPoint_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 6),
    _MlbasRnCULoopPoint_Type()
)
mlbasRnCULoopPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCULoopPoint.setStatus("mandatory")


class _MlbasRnCUAlarmLevel_Type(Integer32):
    """Custom type mlbasRnCUAlarmLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allAlarms", 1),
          ("filter", 2),
          ("noAlarms", 3))
    )


_MlbasRnCUAlarmLevel_Type.__name__ = "Integer32"
_MlbasRnCUAlarmLevel_Object = MibTableColumn
mlbasRnCUAlarmLevel = _MlbasRnCUAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 7),
    _MlbasRnCUAlarmLevel_Type()
)
mlbasRnCUAlarmLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUAlarmLevel.setStatus("mandatory")
_MlbasRnCUSignedOnAts_Type = Integer32
_MlbasRnCUSignedOnAts_Object = MibTableColumn
mlbasRnCUSignedOnAts = _MlbasRnCUSignedOnAts_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 8),
    _MlbasRnCUSignedOnAts_Type()
)
mlbasRnCUSignedOnAts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnCUSignedOnAts.setStatus("mandatory")
_MlbasRnCUSignedOffAts_Type = Integer32
_MlbasRnCUSignedOffAts_Object = MibTableColumn
mlbasRnCUSignedOffAts = _MlbasRnCUSignedOffAts_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 9),
    _MlbasRnCUSignedOffAts_Type()
)
mlbasRnCUSignedOffAts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnCUSignedOffAts.setStatus("mandatory")
_MlbasRnCUChBw_Type = Integer32
_MlbasRnCUChBw_Object = MibTableColumn
mlbasRnCUChBw = _MlbasRnCUChBw_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 10),
    _MlbasRnCUChBw_Type()
)
mlbasRnCUChBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnCUChBw.setStatus("mandatory")


class _MlbasRnCUHwIdModem_Type(DisplayString):
    """Custom type mlbasRnCUHwIdModem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(41, 41),
    )


_MlbasRnCUHwIdModem_Type.__name__ = "DisplayString"
_MlbasRnCUHwIdModem_Object = MibTableColumn
mlbasRnCUHwIdModem = _MlbasRnCUHwIdModem_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 11),
    _MlbasRnCUHwIdModem_Type()
)
mlbasRnCUHwIdModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnCUHwIdModem.setStatus("mandatory")


class _MlbasRnCUSwIdModem_Type(DisplayString):
    """Custom type mlbasRnCUSwIdModem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_MlbasRnCUSwIdModem_Type.__name__ = "DisplayString"
_MlbasRnCUSwIdModem_Object = MibTableColumn
mlbasRnCUSwIdModem = _MlbasRnCUSwIdModem_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 12),
    _MlbasRnCUSwIdModem_Type()
)
mlbasRnCUSwIdModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnCUSwIdModem.setStatus("mandatory")
_MlbasRnRUDownFreq_Type = Integer32
_MlbasRnRUDownFreq_Object = MibTableColumn
mlbasRnRUDownFreq = _MlbasRnRUDownFreq_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 13),
    _MlbasRnRUDownFreq_Type()
)
mlbasRnRUDownFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnRUDownFreq.setStatus("mandatory")
_MlbasRnRUUpFreq_Type = Integer32
_MlbasRnRUUpFreq_Object = MibTableColumn
mlbasRnRUUpFreq = _MlbasRnRUUpFreq_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 14),
    _MlbasRnRUUpFreq_Type()
)
mlbasRnRUUpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUUpFreq.setStatus("mandatory")
_MlbasRnRUDownFreqMin_Type = Integer32
_MlbasRnRUDownFreqMin_Object = MibTableColumn
mlbasRnRUDownFreqMin = _MlbasRnRUDownFreqMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 15),
    _MlbasRnRUDownFreqMin_Type()
)
mlbasRnRUDownFreqMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUDownFreqMin.setStatus("mandatory")
_MlbasRnRUDownFreqMax_Type = Integer32
_MlbasRnRUDownFreqMax_Object = MibTableColumn
mlbasRnRUDownFreqMax = _MlbasRnRUDownFreqMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 16),
    _MlbasRnRUDownFreqMax_Type()
)
mlbasRnRUDownFreqMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUDownFreqMax.setStatus("mandatory")
_MlbasRnRUFreqDuplex_Type = Integer32
_MlbasRnRUFreqDuplex_Object = MibTableColumn
mlbasRnRUFreqDuplex = _MlbasRnRUFreqDuplex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 17),
    _MlbasRnRUFreqDuplex_Type()
)
mlbasRnRUFreqDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUFreqDuplex.setStatus("mandatory")
_MlbasRnRUFreqStep_Type = Integer32
_MlbasRnRUFreqStep_Object = MibTableColumn
mlbasRnRUFreqStep = _MlbasRnRUFreqStep_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 18),
    _MlbasRnRUFreqStep_Type()
)
mlbasRnRUFreqStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUFreqStep.setStatus("mandatory")
_MlbasRnRUOutputPower_Type = Integer32
_MlbasRnRUOutputPower_Object = MibTableColumn
mlbasRnRUOutputPower = _MlbasRnRUOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 19),
    _MlbasRnRUOutputPower_Type()
)
mlbasRnRUOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnRUOutputPower.setStatus("mandatory")
_MlbasRnRUOutputPowerMin_Type = Integer32
_MlbasRnRUOutputPowerMin_Object = MibTableColumn
mlbasRnRUOutputPowerMin = _MlbasRnRUOutputPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 20),
    _MlbasRnRUOutputPowerMin_Type()
)
mlbasRnRUOutputPowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUOutputPowerMin.setStatus("mandatory")
_MlbasRnRUOutputPowerMax_Type = Integer32
_MlbasRnRUOutputPowerMax_Object = MibTableColumn
mlbasRnRUOutputPowerMax = _MlbasRnRUOutputPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 21),
    _MlbasRnRUOutputPowerMax_Type()
)
mlbasRnRUOutputPowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUOutputPowerMax.setStatus("mandatory")


class _MlbasRnRUHwIdRadio_Type(DisplayString):
    """Custom type mlbasRnRUHwIdRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(41, 41),
    )


_MlbasRnRUHwIdRadio_Type.__name__ = "DisplayString"
_MlbasRnRUHwIdRadio_Object = MibTableColumn
mlbasRnRUHwIdRadio = _MlbasRnRUHwIdRadio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 22),
    _MlbasRnRUHwIdRadio_Type()
)
mlbasRnRUHwIdRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUHwIdRadio.setStatus("mandatory")


class _MlbasRnRUSwIdRadio_Type(DisplayString):
    """Custom type mlbasRnRUSwIdRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_MlbasRnRUSwIdRadio_Type.__name__ = "DisplayString"
_MlbasRnRUSwIdRadio_Object = MibTableColumn
mlbasRnRUSwIdRadio = _MlbasRnRUSwIdRadio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 23),
    _MlbasRnRUSwIdRadio_Type()
)
mlbasRnRUSwIdRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasRnRUSwIdRadio.setStatus("mandatory")


class _MlbasRnInterfLevel_Type(Integer32):
    """Custom type mlbasRnInterfLevel based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("manual", 4),
          ("medium", 2))
    )


_MlbasRnInterfLevel_Type.__name__ = "Integer32"
_MlbasRnInterfLevel_Object = MibTableColumn
mlbasRnInterfLevel = _MlbasRnInterfLevel_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 24),
    _MlbasRnInterfLevel_Type()
)
mlbasRnInterfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnInterfLevel.setStatus("mandatory")
_MlbasRnRSSIEXP_Type = Integer32
_MlbasRnRSSIEXP_Object = MibTableColumn
mlbasRnRSSIEXP = _MlbasRnRSSIEXP_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 25),
    _MlbasRnRSSIEXP_Type()
)
mlbasRnRSSIEXP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnRSSIEXP.setStatus("mandatory")


class _MlbasRnCUSignOffAts_Type(Integer32):
    """Custom type mlbasRnCUSignOffAts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("signOff", 2))
    )


_MlbasRnCUSignOffAts_Type.__name__ = "Integer32"
_MlbasRnCUSignOffAts_Object = MibTableColumn
mlbasRnCUSignOffAts = _MlbasRnCUSignOffAts_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 26),
    _MlbasRnCUSignOffAts_Type()
)
mlbasRnCUSignOffAts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnCUSignOffAts.setStatus("mandatory")


class _MlbasRnSwitchBoardAction_Type(Integer32):
    """Custom type mlbasRnSwitchBoardAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("switch-board", 2))
    )


_MlbasRnSwitchBoardAction_Type.__name__ = "Integer32"
_MlbasRnSwitchBoardAction_Object = MibTableColumn
mlbasRnSwitchBoardAction = _MlbasRnSwitchBoardAction_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 1, 1, 1, 27),
    _MlbasRnSwitchBoardAction_Type()
)
mlbasRnSwitchBoardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasRnSwitchBoardAction.setStatus("mandatory")
_MlbasAccessTerminalSlot_ObjectIdentity = ObjectIdentity
mlbasAccessTerminalSlot = _MlbasAccessTerminalSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2)
)
_MlbasAccessTerminalSlotTable_Object = MibTable
mlbasAccessTerminalSlotTable = _MlbasAccessTerminalSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1)
)
if mibBuilder.loadTexts:
    mlbasAccessTerminalSlotTable.setStatus("mandatory")
_MlbasAccessTerminalSlotEntry_Object = MibTableRow
mlbasAccessTerminalSlotEntry = _MlbasAccessTerminalSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1)
)
mlbasAccessTerminalSlotEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotPosition"),
)
if mibBuilder.loadTexts:
    mlbasAccessTerminalSlotEntry.setStatus("mandatory")


class _MlbasAtSlotTerminalId_Type(DisplayString):
    """Custom type mlbasAtSlotTerminalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasAtSlotTerminalId_Type.__name__ = "DisplayString"
_MlbasAtSlotTerminalId_Object = MibTableColumn
mlbasAtSlotTerminalId = _MlbasAtSlotTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 1),
    _MlbasAtSlotTerminalId_Type()
)
mlbasAtSlotTerminalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtSlotTerminalId.setStatus("mandatory")
_MlbasAtSlotRnPos_Type = Integer32
_MlbasAtSlotRnPos_Object = MibTableColumn
mlbasAtSlotRnPos = _MlbasAtSlotRnPos_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 2),
    _MlbasAtSlotRnPos_Type()
)
mlbasAtSlotRnPos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtSlotRnPos.setStatus("mandatory")


class _MlbasAtSlotLocation_Type(DisplayString):
    """Custom type mlbasAtSlotLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MlbasAtSlotLocation_Type.__name__ = "DisplayString"
_MlbasAtSlotLocation_Object = MibTableColumn
mlbasAtSlotLocation = _MlbasAtSlotLocation_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 3),
    _MlbasAtSlotLocation_Type()
)
mlbasAtSlotLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtSlotLocation.setStatus("mandatory")


class _MlbasAtSlotSignOnAction_Type(Integer32):
    """Custom type mlbasAtSlotSignOnAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_MlbasAtSlotSignOnAction_Type.__name__ = "Integer32"
_MlbasAtSlotSignOnAction_Object = MibTableColumn
mlbasAtSlotSignOnAction = _MlbasAtSlotSignOnAction_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 4),
    _MlbasAtSlotSignOnAction_Type()
)
mlbasAtSlotSignOnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtSlotSignOnAction.setStatus("mandatory")


class _MlbasAtSlotSignOnStatus_Type(Integer32):
    """Custom type mlbasAtSlotSignOnStatus based on Integer32"""
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
        *(("signedOff", 2),
          ("signedOn", 1),
          ("signingOff", 4),
          ("signingOn", 3))
    )


_MlbasAtSlotSignOnStatus_Type.__name__ = "Integer32"
_MlbasAtSlotSignOnStatus_Object = MibTableColumn
mlbasAtSlotSignOnStatus = _MlbasAtSlotSignOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 5),
    _MlbasAtSlotSignOnStatus_Type()
)
mlbasAtSlotSignOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtSlotSignOnStatus.setStatus("mandatory")
_MlbasAtSlotRowStatus_Type = RowStatus
_MlbasAtSlotRowStatus_Object = MibTableColumn
mlbasAtSlotRowStatus = _MlbasAtSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 2, 1, 1, 6),
    _MlbasAtSlotRowStatus_Type()
)
mlbasAtSlotRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtSlotRowStatus.setStatus("mandatory")
_MlbasAccessTerminal_ObjectIdentity = ObjectIdentity
mlbasAccessTerminal = _MlbasAccessTerminal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3)
)
_MlbasAccessTerminalTable_Object = MibTable
mlbasAccessTerminalTable = _MlbasAccessTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1)
)
if mibBuilder.loadTexts:
    mlbasAccessTerminalTable.setStatus("mandatory")
_MlbasAccessTerminalEntry_Object = MibTableRow
mlbasAccessTerminalEntry = _MlbasAccessTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1)
)
mlbasAccessTerminalEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansSlotPosition"),
)
if mibBuilder.loadTexts:
    mlbasAccessTerminalEntry.setStatus("mandatory")


class _MlbasAtCUPerformance_Type(Integer32):
    """Custom type mlbasAtCUPerformance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MlbasAtCUPerformance_Type.__name__ = "Integer32"
_MlbasAtCUPerformance_Object = MibTableColumn
mlbasAtCUPerformance = _MlbasAtCUPerformance_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 1),
    _MlbasAtCUPerformance_Type()
)
mlbasAtCUPerformance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtCUPerformance.setStatus("mandatory")
_MlbasAtCUPerfStart_Type = DateAndTime
_MlbasAtCUPerfStart_Object = MibTableColumn
mlbasAtCUPerfStart = _MlbasAtCUPerfStart_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 2),
    _MlbasAtCUPerfStart_Type()
)
mlbasAtCUPerfStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUPerfStart.setStatus("mandatory")


class _MlbasAtCUAtmLoop_Type(Integer32):
    """Custom type mlbasAtCUAtmLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_MlbasAtCUAtmLoop_Type.__name__ = "Integer32"
_MlbasAtCUAtmLoop_Object = MibTableColumn
mlbasAtCUAtmLoop = _MlbasAtCUAtmLoop_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 3),
    _MlbasAtCUAtmLoop_Type()
)
mlbasAtCUAtmLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtCUAtmLoop.setStatus("mandatory")


class _MlbasAtCUBerThreshold_Type(Integer32):
    """Custom type mlbasAtCUBerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ber3", 3),
          ("ber4", 4),
          ("ber5", 5),
          ("ber6", 6))
    )


_MlbasAtCUBerThreshold_Type.__name__ = "Integer32"
_MlbasAtCUBerThreshold_Object = MibTableColumn
mlbasAtCUBerThreshold = _MlbasAtCUBerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 4),
    _MlbasAtCUBerThreshold_Type()
)
mlbasAtCUBerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasAtCUBerThreshold.setStatus("mandatory")
_MlbasAtCUValid15MinPerf_Type = Integer32
_MlbasAtCUValid15MinPerf_Object = MibTableColumn
mlbasAtCUValid15MinPerf = _MlbasAtCUValid15MinPerf_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 5),
    _MlbasAtCUValid15MinPerf_Type()
)
mlbasAtCUValid15MinPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUValid15MinPerf.setStatus("mandatory")
_MlbasAtCUInvalid15MinPerf_Type = Integer32
_MlbasAtCUInvalid15MinPerf_Object = MibTableColumn
mlbasAtCUInvalid15MinPerf = _MlbasAtCUInvalid15MinPerf_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 6),
    _MlbasAtCUInvalid15MinPerf_Type()
)
mlbasAtCUInvalid15MinPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUInvalid15MinPerf.setStatus("mandatory")
_MlbasAtCUValid24HPerf_Type = Integer32
_MlbasAtCUValid24HPerf_Object = MibTableColumn
mlbasAtCUValid24HPerf = _MlbasAtCUValid24HPerf_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 7),
    _MlbasAtCUValid24HPerf_Type()
)
mlbasAtCUValid24HPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUValid24HPerf.setStatus("mandatory")
_MlbasAtCUInvalid24HPerf_Type = Integer32
_MlbasAtCUInvalid24HPerf_Object = MibTableColumn
mlbasAtCUInvalid24HPerf = _MlbasAtCUInvalid24HPerf_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 8),
    _MlbasAtCUInvalid24HPerf_Type()
)
mlbasAtCUInvalid24HPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUInvalid24HPerf.setStatus("mandatory")


class _MlbasAtCUHwIdModem_Type(DisplayString):
    """Custom type mlbasAtCUHwIdModem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(41, 41),
    )


_MlbasAtCUHwIdModem_Type.__name__ = "DisplayString"
_MlbasAtCUHwIdModem_Object = MibTableColumn
mlbasAtCUHwIdModem = _MlbasAtCUHwIdModem_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 9),
    _MlbasAtCUHwIdModem_Type()
)
mlbasAtCUHwIdModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUHwIdModem.setStatus("mandatory")


class _MlbasAtCUSwIdModem_Type(DisplayString):
    """Custom type mlbasAtCUSwIdModem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_MlbasAtCUSwIdModem_Type.__name__ = "DisplayString"
_MlbasAtCUSwIdModem_Object = MibTableColumn
mlbasAtCUSwIdModem = _MlbasAtCUSwIdModem_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 10),
    _MlbasAtCUSwIdModem_Type()
)
mlbasAtCUSwIdModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtCUSwIdModem.setStatus("mandatory")
_MlbasAtRUDownFreq_Type = Integer32
_MlbasAtRUDownFreq_Object = MibTableColumn
mlbasAtRUDownFreq = _MlbasAtRUDownFreq_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 11),
    _MlbasAtRUDownFreq_Type()
)
mlbasAtRUDownFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtRUDownFreq.setStatus("mandatory")
_MlbasAtRUUpFreq_Type = Integer32
_MlbasAtRUUpFreq_Object = MibTableColumn
mlbasAtRUUpFreq = _MlbasAtRUUpFreq_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 12),
    _MlbasAtRUUpFreq_Type()
)
mlbasAtRUUpFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtRUUpFreq.setStatus("mandatory")
_MlbasAtRUOutputPower_Type = Integer32
_MlbasAtRUOutputPower_Object = MibTableColumn
mlbasAtRUOutputPower = _MlbasAtRUOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 13),
    _MlbasAtRUOutputPower_Type()
)
mlbasAtRUOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtRUOutputPower.setStatus("mandatory")


class _MlbasAtRUHwIdRadio_Type(DisplayString):
    """Custom type mlbasAtRUHwIdRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(41, 41),
    )


_MlbasAtRUHwIdRadio_Type.__name__ = "DisplayString"
_MlbasAtRUHwIdRadio_Object = MibTableColumn
mlbasAtRUHwIdRadio = _MlbasAtRUHwIdRadio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 14),
    _MlbasAtRUHwIdRadio_Type()
)
mlbasAtRUHwIdRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtRUHwIdRadio.setStatus("mandatory")


class _MlbasAtRUSwIdRadio_Type(DisplayString):
    """Custom type mlbasAtRUSwIdRadio based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_MlbasAtRUSwIdRadio_Type.__name__ = "DisplayString"
_MlbasAtRUSwIdRadio_Object = MibTableColumn
mlbasAtRUSwIdRadio = _MlbasAtRUSwIdRadio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 3, 1, 1, 15),
    _MlbasAtRUSwIdRadio_Type()
)
mlbasAtRUSwIdRadio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasAtRUSwIdRadio.setStatus("mandatory")
_MlbasServiceUnit_ObjectIdentity = ObjectIdentity
mlbasServiceUnit = _MlbasServiceUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4)
)
_MlbasServiceUnitTable_Object = MibTable
mlbasServiceUnitTable = _MlbasServiceUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1)
)
if mibBuilder.loadTexts:
    mlbasServiceUnitTable.setStatus("mandatory")
_MlbasServiceUnitEntry_Object = MibTableRow
mlbasServiceUnitEntry = _MlbasServiceUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1)
)
mlbasServiceUnitEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-MLBAS-MIB", "mlbasSuPos"),
)
if mibBuilder.loadTexts:
    mlbasServiceUnitEntry.setStatus("mandatory")
_MlbasSuPos_Type = Integer32
_MlbasSuPos_Object = MibTableColumn
mlbasSuPos = _MlbasSuPos_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 1),
    _MlbasSuPos_Type()
)
mlbasSuPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuPos.setStatus("mandatory")


class _MlbasSuManagedStatus_Type(Integer32):
    """Custom type mlbasSuManagedStatus based on Integer32"""
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
        *(("empty", 2),
          ("managed", 4),
          ("present", 3),
          ("unmanaged", 1))
    )


_MlbasSuManagedStatus_Type.__name__ = "Integer32"
_MlbasSuManagedStatus_Object = MibTableColumn
mlbasSuManagedStatus = _MlbasSuManagedStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 2),
    _MlbasSuManagedStatus_Type()
)
mlbasSuManagedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasSuManagedStatus.setStatus("mandatory")


class _MlbasSuOperState_Type(Integer32):
    """Custom type mlbasSuOperState based on Integer32"""
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


_MlbasSuOperState_Type.__name__ = "Integer32"
_MlbasSuOperState_Object = MibTableColumn
mlbasSuOperState = _MlbasSuOperState_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 3),
    _MlbasSuOperState_Type()
)
mlbasSuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuOperState.setStatus("mandatory")


class _MlbasSuHwId_Type(DisplayString):
    """Custom type mlbasSuHwId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(35, 35),
    )


_MlbasSuHwId_Type.__name__ = "DisplayString"
_MlbasSuHwId_Object = MibTableColumn
mlbasSuHwId = _MlbasSuHwId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 4),
    _MlbasSuHwId_Type()
)
mlbasSuHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuHwId.setStatus("mandatory")


class _MlbasSuType_Type(Integer32):
    """Custom type mlbasSuType based on Integer32"""
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
        *(("any", 1),
          ("atm", 5),
          ("ds1", 4),
          ("e1", 3),
          ("ethernet", 2),
          ("unknown", 6))
    )


_MlbasSuType_Type.__name__ = "Integer32"
_MlbasSuType_Object = MibTableColumn
mlbasSuType = _MlbasSuType_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 5),
    _MlbasSuType_Type()
)
mlbasSuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mlbasSuType.setStatus("mandatory")
_MlbasSuPciId_Type = Integer32
_MlbasSuPciId_Object = MibTableColumn
mlbasSuPciId = _MlbasSuPciId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 6),
    _MlbasSuPciId_Type()
)
mlbasSuPciId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuPciId.setStatus("mandatory")
_MlbasSuPciVendor_Type = Integer32
_MlbasSuPciVendor_Object = MibTableColumn
mlbasSuPciVendor = _MlbasSuPciVendor_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 7),
    _MlbasSuPciVendor_Type()
)
mlbasSuPciVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuPciVendor.setStatus("mandatory")
_MlbasSuPortStartIndex_Type = Integer32
_MlbasSuPortStartIndex_Object = MibTableColumn
mlbasSuPortStartIndex = _MlbasSuPortStartIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 8),
    _MlbasSuPortStartIndex_Type()
)
mlbasSuPortStartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuPortStartIndex.setStatus("mandatory")
_MlbasSuNumOfPorts_Type = Integer32
_MlbasSuNumOfPorts_Object = MibTableColumn
mlbasSuNumOfPorts = _MlbasSuNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 4, 1, 1, 9),
    _MlbasSuNumOfPorts_Type()
)
mlbasSuNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSuNumOfPorts.setStatus("mandatory")
_MlbasDownLinkPerf15min_ObjectIdentity = ObjectIdentity
mlbasDownLinkPerf15min = _MlbasDownLinkPerf15min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5)
)
_MlbasDownLinkPerf15minTable_Object = MibTable
mlbasDownLinkPerf15minTable = _MlbasDownLinkPerf15minTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1)
)
if mibBuilder.loadTexts:
    mlbasDownLinkPerf15minTable.setStatus("mandatory")
_MlbasDownLinkPerf15minEntry_Object = MibTableRow
mlbasDownLinkPerf15minEntry = _MlbasDownLinkPerf15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1)
)
mlbasDownLinkPerf15minEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-MLBAS-MIB", "mlbasDL15PeriodIndex"),
)
if mibBuilder.loadTexts:
    mlbasDownLinkPerf15minEntry.setStatus("mandatory")
_MlbasDL15PeriodIndex_Type = Integer32
_MlbasDL15PeriodIndex_Object = MibTableColumn
mlbasDL15PeriodIndex = _MlbasDL15PeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 1),
    _MlbasDL15PeriodIndex_Type()
)
mlbasDL15PeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PeriodIndex.setStatus("mandatory")
_MlbasDL15UpdateTime_Type = DateAndTime
_MlbasDL15UpdateTime_Object = MibTableColumn
mlbasDL15UpdateTime = _MlbasDL15UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 2),
    _MlbasDL15UpdateTime_Type()
)
mlbasDL15UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15UpdateTime.setStatus("mandatory")
_MlbasDL15PerfCellErrRatio_Type = Integer32
_MlbasDL15PerfCellErrRatio_Object = MibTableColumn
mlbasDL15PerfCellErrRatio = _MlbasDL15PerfCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 3),
    _MlbasDL15PerfCellErrRatio_Type()
)
mlbasDL15PerfCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfCellErrRatio.setStatus("mandatory")
_MlbasDL15PerfCellLossRatio_Type = Integer32
_MlbasDL15PerfCellLossRatio_Object = MibTableColumn
mlbasDL15PerfCellLossRatio = _MlbasDL15PerfCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 4),
    _MlbasDL15PerfCellLossRatio_Type()
)
mlbasDL15PerfCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfCellLossRatio.setStatus("mandatory")
_MlbasDL15PerfUbrDiscCell_Type = Integer32
_MlbasDL15PerfUbrDiscCell_Object = MibTableColumn
mlbasDL15PerfUbrDiscCell = _MlbasDL15PerfUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 5),
    _MlbasDL15PerfUbrDiscCell_Type()
)
mlbasDL15PerfUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfUbrDiscCell.setStatus("mandatory")
_MlbasDL15PerfCbrDiscCell_Type = Integer32
_MlbasDL15PerfCbrDiscCell_Object = MibTableColumn
mlbasDL15PerfCbrDiscCell = _MlbasDL15PerfCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 6),
    _MlbasDL15PerfCbrDiscCell_Type()
)
mlbasDL15PerfCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfCbrDiscCell.setStatus("mandatory")
_MlbasDL15PerfAvailTime_Type = Integer32
_MlbasDL15PerfAvailTime_Object = MibTableColumn
mlbasDL15PerfAvailTime = _MlbasDL15PerfAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 7),
    _MlbasDL15PerfAvailTime_Type()
)
mlbasDL15PerfAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfAvailTime.setStatus("mandatory")
_MlbasDL15PerfUnavailTime_Type = Integer32
_MlbasDL15PerfUnavailTime_Object = MibTableColumn
mlbasDL15PerfUnavailTime = _MlbasDL15PerfUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 8),
    _MlbasDL15PerfUnavailTime_Type()
)
mlbasDL15PerfUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfUnavailTime.setStatus("mandatory")
_MlbasDL15PerfErroredSecRatio_Type = Integer32
_MlbasDL15PerfErroredSecRatio_Object = MibTableColumn
mlbasDL15PerfErroredSecRatio = _MlbasDL15PerfErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 9),
    _MlbasDL15PerfErroredSecRatio_Type()
)
mlbasDL15PerfErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfErroredSecRatio.setStatus("mandatory")
_MlbasDL15PerfSevErroredSecRatio_Type = Integer32
_MlbasDL15PerfSevErroredSecRatio_Object = MibTableColumn
mlbasDL15PerfSevErroredSecRatio = _MlbasDL15PerfSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 10),
    _MlbasDL15PerfSevErroredSecRatio_Type()
)
mlbasDL15PerfSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfSevErroredSecRatio.setStatus("mandatory")
_MlbasDL15PerfBgBlockErrRatio_Type = Integer32
_MlbasDL15PerfBgBlockErrRatio_Object = MibTableColumn
mlbasDL15PerfBgBlockErrRatio = _MlbasDL15PerfBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 11),
    _MlbasDL15PerfBgBlockErrRatio_Type()
)
mlbasDL15PerfBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfBgBlockErrRatio.setStatus("mandatory")
_MlbasDL15PerfMinInPower_Type = Integer32
_MlbasDL15PerfMinInPower_Object = MibTableColumn
mlbasDL15PerfMinInPower = _MlbasDL15PerfMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 12),
    _MlbasDL15PerfMinInPower_Type()
)
mlbasDL15PerfMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfMinInPower.setStatus("mandatory")
_MlbasDL15PerfMaxInPower_Type = Integer32
_MlbasDL15PerfMaxInPower_Object = MibTableColumn
mlbasDL15PerfMaxInPower = _MlbasDL15PerfMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 13),
    _MlbasDL15PerfMaxInPower_Type()
)
mlbasDL15PerfMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfMaxInPower.setStatus("mandatory")
_MlbasDL15PerfAverageInPower_Type = Integer32
_MlbasDL15PerfAverageInPower_Object = MibTableColumn
mlbasDL15PerfAverageInPower = _MlbasDL15PerfAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 14),
    _MlbasDL15PerfAverageInPower_Type()
)
mlbasDL15PerfAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfAverageInPower.setStatus("mandatory")
_MlbasDL15PerfMinOutPower_Type = Integer32
_MlbasDL15PerfMinOutPower_Object = MibTableColumn
mlbasDL15PerfMinOutPower = _MlbasDL15PerfMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 15),
    _MlbasDL15PerfMinOutPower_Type()
)
mlbasDL15PerfMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfMinOutPower.setStatus("mandatory")
_MlbasDL15PerfMaxOutPower_Type = Integer32
_MlbasDL15PerfMaxOutPower_Object = MibTableColumn
mlbasDL15PerfMaxOutPower = _MlbasDL15PerfMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 16),
    _MlbasDL15PerfMaxOutPower_Type()
)
mlbasDL15PerfMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfMaxOutPower.setStatus("mandatory")
_MlbasDL15PerfAverageOutPower_Type = Integer32
_MlbasDL15PerfAverageOutPower_Object = MibTableColumn
mlbasDL15PerfAverageOutPower = _MlbasDL15PerfAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 17),
    _MlbasDL15PerfAverageOutPower_Type()
)
mlbasDL15PerfAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfAverageOutPower.setStatus("mandatory")


class _MlbasDL15PerfTerminalId_Type(DisplayString):
    """Custom type mlbasDL15PerfTerminalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasDL15PerfTerminalId_Type.__name__ = "DisplayString"
_MlbasDL15PerfTerminalId_Object = MibTableColumn
mlbasDL15PerfTerminalId = _MlbasDL15PerfTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 5, 1, 1, 18),
    _MlbasDL15PerfTerminalId_Type()
)
mlbasDL15PerfTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15PerfTerminalId.setStatus("mandatory")
_MlbasUpLinkPerf15min_ObjectIdentity = ObjectIdentity
mlbasUpLinkPerf15min = _MlbasUpLinkPerf15min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6)
)
_MlbasUpLinkPerf15minTable_Object = MibTable
mlbasUpLinkPerf15minTable = _MlbasUpLinkPerf15minTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1)
)
if mibBuilder.loadTexts:
    mlbasUpLinkPerf15minTable.setStatus("mandatory")
_MlbasUpLinkPerf15minEntry_Object = MibTableRow
mlbasUpLinkPerf15minEntry = _MlbasUpLinkPerf15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1)
)
mlbasUpLinkPerf15minEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-MLBAS-MIB", "mlbasUL15PeriodIndex"),
)
if mibBuilder.loadTexts:
    mlbasUpLinkPerf15minEntry.setStatus("mandatory")
_MlbasUL15PeriodIndex_Type = Integer32
_MlbasUL15PeriodIndex_Object = MibTableColumn
mlbasUL15PeriodIndex = _MlbasUL15PeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 1),
    _MlbasUL15PeriodIndex_Type()
)
mlbasUL15PeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PeriodIndex.setStatus("mandatory")
_MlbasUL15UpdateTime_Type = DateAndTime
_MlbasUL15UpdateTime_Object = MibTableColumn
mlbasUL15UpdateTime = _MlbasUL15UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 2),
    _MlbasUL15UpdateTime_Type()
)
mlbasUL15UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15UpdateTime.setStatus("mandatory")
_MlbasUL15PerfCellErrRatio_Type = Integer32
_MlbasUL15PerfCellErrRatio_Object = MibTableColumn
mlbasUL15PerfCellErrRatio = _MlbasUL15PerfCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 3),
    _MlbasUL15PerfCellErrRatio_Type()
)
mlbasUL15PerfCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfCellErrRatio.setStatus("mandatory")
_MlbasUL15PerfCellLossRatio_Type = Integer32
_MlbasUL15PerfCellLossRatio_Object = MibTableColumn
mlbasUL15PerfCellLossRatio = _MlbasUL15PerfCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 4),
    _MlbasUL15PerfCellLossRatio_Type()
)
mlbasUL15PerfCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfCellLossRatio.setStatus("mandatory")
_MlbasUL15PerfUbrDiscCell_Type = Integer32
_MlbasUL15PerfUbrDiscCell_Object = MibTableColumn
mlbasUL15PerfUbrDiscCell = _MlbasUL15PerfUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 5),
    _MlbasUL15PerfUbrDiscCell_Type()
)
mlbasUL15PerfUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfUbrDiscCell.setStatus("mandatory")
_MlbasUL15PerfCbrDiscCell_Type = Integer32
_MlbasUL15PerfCbrDiscCell_Object = MibTableColumn
mlbasUL15PerfCbrDiscCell = _MlbasUL15PerfCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 6),
    _MlbasUL15PerfCbrDiscCell_Type()
)
mlbasUL15PerfCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfCbrDiscCell.setStatus("mandatory")
_MlbasUL15PerfAvailTime_Type = Integer32
_MlbasUL15PerfAvailTime_Object = MibTableColumn
mlbasUL15PerfAvailTime = _MlbasUL15PerfAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 7),
    _MlbasUL15PerfAvailTime_Type()
)
mlbasUL15PerfAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfAvailTime.setStatus("mandatory")
_MlbasUL15PerfUnavailTime_Type = Integer32
_MlbasUL15PerfUnavailTime_Object = MibTableColumn
mlbasUL15PerfUnavailTime = _MlbasUL15PerfUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 8),
    _MlbasUL15PerfUnavailTime_Type()
)
mlbasUL15PerfUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfUnavailTime.setStatus("mandatory")
_MlbasUL15PerfErroredSecRatio_Type = Integer32
_MlbasUL15PerfErroredSecRatio_Object = MibTableColumn
mlbasUL15PerfErroredSecRatio = _MlbasUL15PerfErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 9),
    _MlbasUL15PerfErroredSecRatio_Type()
)
mlbasUL15PerfErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfErroredSecRatio.setStatus("mandatory")
_MlbasUL15PerfSevErroredSecRatio_Type = Integer32
_MlbasUL15PerfSevErroredSecRatio_Object = MibTableColumn
mlbasUL15PerfSevErroredSecRatio = _MlbasUL15PerfSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 10),
    _MlbasUL15PerfSevErroredSecRatio_Type()
)
mlbasUL15PerfSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfSevErroredSecRatio.setStatus("mandatory")
_MlbasUL15PerfBgBlockErrRatio_Type = Integer32
_MlbasUL15PerfBgBlockErrRatio_Object = MibTableColumn
mlbasUL15PerfBgBlockErrRatio = _MlbasUL15PerfBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 11),
    _MlbasUL15PerfBgBlockErrRatio_Type()
)
mlbasUL15PerfBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfBgBlockErrRatio.setStatus("mandatory")
_MlbasUL15PerfMinInPower_Type = Integer32
_MlbasUL15PerfMinInPower_Object = MibTableColumn
mlbasUL15PerfMinInPower = _MlbasUL15PerfMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 12),
    _MlbasUL15PerfMinInPower_Type()
)
mlbasUL15PerfMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfMinInPower.setStatus("mandatory")
_MlbasUL15PerfMaxInPower_Type = Integer32
_MlbasUL15PerfMaxInPower_Object = MibTableColumn
mlbasUL15PerfMaxInPower = _MlbasUL15PerfMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 13),
    _MlbasUL15PerfMaxInPower_Type()
)
mlbasUL15PerfMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfMaxInPower.setStatus("mandatory")
_MlbasUL15PerfAverageInPower_Type = Integer32
_MlbasUL15PerfAverageInPower_Object = MibTableColumn
mlbasUL15PerfAverageInPower = _MlbasUL15PerfAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 14),
    _MlbasUL15PerfAverageInPower_Type()
)
mlbasUL15PerfAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfAverageInPower.setStatus("mandatory")
_MlbasUL15PerfMinOutPower_Type = Integer32
_MlbasUL15PerfMinOutPower_Object = MibTableColumn
mlbasUL15PerfMinOutPower = _MlbasUL15PerfMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 15),
    _MlbasUL15PerfMinOutPower_Type()
)
mlbasUL15PerfMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfMinOutPower.setStatus("mandatory")
_MlbasUL15PerfMaxOutPower_Type = Integer32
_MlbasUL15PerfMaxOutPower_Object = MibTableColumn
mlbasUL15PerfMaxOutPower = _MlbasUL15PerfMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 16),
    _MlbasUL15PerfMaxOutPower_Type()
)
mlbasUL15PerfMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfMaxOutPower.setStatus("mandatory")
_MlbasUL15PerfAverageOutPower_Type = Integer32
_MlbasUL15PerfAverageOutPower_Object = MibTableColumn
mlbasUL15PerfAverageOutPower = _MlbasUL15PerfAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 17),
    _MlbasUL15PerfAverageOutPower_Type()
)
mlbasUL15PerfAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfAverageOutPower.setStatus("mandatory")


class _MlbasUL15PerfTerminalId_Type(DisplayString):
    """Custom type mlbasUL15PerfTerminalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasUL15PerfTerminalId_Type.__name__ = "DisplayString"
_MlbasUL15PerfTerminalId_Object = MibTableColumn
mlbasUL15PerfTerminalId = _MlbasUL15PerfTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 6, 1, 1, 18),
    _MlbasUL15PerfTerminalId_Type()
)
mlbasUL15PerfTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15PerfTerminalId.setStatus("mandatory")
_MlbasDownLinkPerf24hour_ObjectIdentity = ObjectIdentity
mlbasDownLinkPerf24hour = _MlbasDownLinkPerf24hour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7)
)
_MlbasDownLinkPerf24hourTable_Object = MibTable
mlbasDownLinkPerf24hourTable = _MlbasDownLinkPerf24hourTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mlbasDownLinkPerf24hourTable.setStatus("mandatory")
_MlbasDownLinkPerf24hourEntry_Object = MibTableRow
mlbasDownLinkPerf24hourEntry = _MlbasDownLinkPerf24hourEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1)
)
mlbasDownLinkPerf24hourEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-MLBAS-MIB", "mlbasDL24PeriodIndex"),
)
if mibBuilder.loadTexts:
    mlbasDownLinkPerf24hourEntry.setStatus("mandatory")
_MlbasDL24PeriodIndex_Type = Integer32
_MlbasDL24PeriodIndex_Object = MibTableColumn
mlbasDL24PeriodIndex = _MlbasDL24PeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 1),
    _MlbasDL24PeriodIndex_Type()
)
mlbasDL24PeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PeriodIndex.setStatus("mandatory")
_MlbasDL24UpdateTime_Type = DateAndTime
_MlbasDL24UpdateTime_Object = MibTableColumn
mlbasDL24UpdateTime = _MlbasDL24UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 2),
    _MlbasDL24UpdateTime_Type()
)
mlbasDL24UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24UpdateTime.setStatus("mandatory")
_MlbasDL24PerfCellErrRatio_Type = Integer32
_MlbasDL24PerfCellErrRatio_Object = MibTableColumn
mlbasDL24PerfCellErrRatio = _MlbasDL24PerfCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 3),
    _MlbasDL24PerfCellErrRatio_Type()
)
mlbasDL24PerfCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfCellErrRatio.setStatus("mandatory")
_MlbasDL24PerfCellLossRatio_Type = Integer32
_MlbasDL24PerfCellLossRatio_Object = MibTableColumn
mlbasDL24PerfCellLossRatio = _MlbasDL24PerfCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 4),
    _MlbasDL24PerfCellLossRatio_Type()
)
mlbasDL24PerfCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfCellLossRatio.setStatus("mandatory")
_MlbasDL24PerfUbrDiscCell_Type = Integer32
_MlbasDL24PerfUbrDiscCell_Object = MibTableColumn
mlbasDL24PerfUbrDiscCell = _MlbasDL24PerfUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 5),
    _MlbasDL24PerfUbrDiscCell_Type()
)
mlbasDL24PerfUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfUbrDiscCell.setStatus("mandatory")
_MlbasDL24PerfCbrDiscCell_Type = Integer32
_MlbasDL24PerfCbrDiscCell_Object = MibTableColumn
mlbasDL24PerfCbrDiscCell = _MlbasDL24PerfCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 6),
    _MlbasDL24PerfCbrDiscCell_Type()
)
mlbasDL24PerfCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfCbrDiscCell.setStatus("mandatory")
_MlbasDL24PerfAvailTime_Type = Integer32
_MlbasDL24PerfAvailTime_Object = MibTableColumn
mlbasDL24PerfAvailTime = _MlbasDL24PerfAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 7),
    _MlbasDL24PerfAvailTime_Type()
)
mlbasDL24PerfAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfAvailTime.setStatus("mandatory")
_MlbasDL24PerfUnavailTime_Type = Integer32
_MlbasDL24PerfUnavailTime_Object = MibTableColumn
mlbasDL24PerfUnavailTime = _MlbasDL24PerfUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 8),
    _MlbasDL24PerfUnavailTime_Type()
)
mlbasDL24PerfUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfUnavailTime.setStatus("mandatory")
_MlbasDL24PerfErroredSecRatio_Type = Integer32
_MlbasDL24PerfErroredSecRatio_Object = MibTableColumn
mlbasDL24PerfErroredSecRatio = _MlbasDL24PerfErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 9),
    _MlbasDL24PerfErroredSecRatio_Type()
)
mlbasDL24PerfErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfErroredSecRatio.setStatus("mandatory")
_MlbasDL24PerfSevErroredSecRatio_Type = Integer32
_MlbasDL24PerfSevErroredSecRatio_Object = MibTableColumn
mlbasDL24PerfSevErroredSecRatio = _MlbasDL24PerfSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 10),
    _MlbasDL24PerfSevErroredSecRatio_Type()
)
mlbasDL24PerfSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfSevErroredSecRatio.setStatus("mandatory")
_MlbasDL24PerfBgBlockErrRatio_Type = Integer32
_MlbasDL24PerfBgBlockErrRatio_Object = MibTableColumn
mlbasDL24PerfBgBlockErrRatio = _MlbasDL24PerfBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 11),
    _MlbasDL24PerfBgBlockErrRatio_Type()
)
mlbasDL24PerfBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfBgBlockErrRatio.setStatus("mandatory")
_MlbasDL24PerfMinInPower_Type = Integer32
_MlbasDL24PerfMinInPower_Object = MibTableColumn
mlbasDL24PerfMinInPower = _MlbasDL24PerfMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 12),
    _MlbasDL24PerfMinInPower_Type()
)
mlbasDL24PerfMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfMinInPower.setStatus("mandatory")
_MlbasDL24PerfMaxInPower_Type = Integer32
_MlbasDL24PerfMaxInPower_Object = MibTableColumn
mlbasDL24PerfMaxInPower = _MlbasDL24PerfMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 13),
    _MlbasDL24PerfMaxInPower_Type()
)
mlbasDL24PerfMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfMaxInPower.setStatus("mandatory")
_MlbasDL24PerfAverageInPower_Type = Integer32
_MlbasDL24PerfAverageInPower_Object = MibTableColumn
mlbasDL24PerfAverageInPower = _MlbasDL24PerfAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 14),
    _MlbasDL24PerfAverageInPower_Type()
)
mlbasDL24PerfAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfAverageInPower.setStatus("mandatory")
_MlbasDL24PerfMinOutPower_Type = Integer32
_MlbasDL24PerfMinOutPower_Object = MibTableColumn
mlbasDL24PerfMinOutPower = _MlbasDL24PerfMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 15),
    _MlbasDL24PerfMinOutPower_Type()
)
mlbasDL24PerfMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfMinOutPower.setStatus("mandatory")
_MlbasDL24PerfMaxOutPower_Type = Integer32
_MlbasDL24PerfMaxOutPower_Object = MibTableColumn
mlbasDL24PerfMaxOutPower = _MlbasDL24PerfMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 16),
    _MlbasDL24PerfMaxOutPower_Type()
)
mlbasDL24PerfMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfMaxOutPower.setStatus("mandatory")
_MlbasDL24PerfAverageOutPower_Type = Integer32
_MlbasDL24PerfAverageOutPower_Object = MibTableColumn
mlbasDL24PerfAverageOutPower = _MlbasDL24PerfAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 17),
    _MlbasDL24PerfAverageOutPower_Type()
)
mlbasDL24PerfAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfAverageOutPower.setStatus("mandatory")


class _MlbasDL24PerfTerminalId_Type(DisplayString):
    """Custom type mlbasDL24PerfTerminalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasDL24PerfTerminalId_Type.__name__ = "DisplayString"
_MlbasDL24PerfTerminalId_Object = MibTableColumn
mlbasDL24PerfTerminalId = _MlbasDL24PerfTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 7, 1, 1, 18),
    _MlbasDL24PerfTerminalId_Type()
)
mlbasDL24PerfTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24PerfTerminalId.setStatus("mandatory")
_MlbasUpLinkPerf24hour_ObjectIdentity = ObjectIdentity
mlbasUpLinkPerf24hour = _MlbasUpLinkPerf24hour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8)
)
_MlbasUpLinkPerf24hourTable_Object = MibTable
mlbasUpLinkPerf24hourTable = _MlbasUpLinkPerf24hourTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1)
)
if mibBuilder.loadTexts:
    mlbasUpLinkPerf24hourTable.setStatus("mandatory")
_MlbasUpLinkPerf24hourEntry_Object = MibTableRow
mlbasUpLinkPerf24hourEntry = _MlbasUpLinkPerf24hourEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1)
)
mlbasUpLinkPerf24hourEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
    (0, "ANS-MLBAS-MIB", "mlbasUL24PeriodIndex"),
)
if mibBuilder.loadTexts:
    mlbasUpLinkPerf24hourEntry.setStatus("mandatory")
_MlbasUL24PeriodIndex_Type = Integer32
_MlbasUL24PeriodIndex_Object = MibTableColumn
mlbasUL24PeriodIndex = _MlbasUL24PeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 1),
    _MlbasUL24PeriodIndex_Type()
)
mlbasUL24PeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PeriodIndex.setStatus("mandatory")
_MlbasUL24UpdateTime_Type = DateAndTime
_MlbasUL24UpdateTime_Object = MibTableColumn
mlbasUL24UpdateTime = _MlbasUL24UpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 2),
    _MlbasUL24UpdateTime_Type()
)
mlbasUL24UpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24UpdateTime.setStatus("mandatory")
_MlbasUL24PerfCellErrRatio_Type = Integer32
_MlbasUL24PerfCellErrRatio_Object = MibTableColumn
mlbasUL24PerfCellErrRatio = _MlbasUL24PerfCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 3),
    _MlbasUL24PerfCellErrRatio_Type()
)
mlbasUL24PerfCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfCellErrRatio.setStatus("mandatory")
_MlbasUL24PerfCellLossRatio_Type = Integer32
_MlbasUL24PerfCellLossRatio_Object = MibTableColumn
mlbasUL24PerfCellLossRatio = _MlbasUL24PerfCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 4),
    _MlbasUL24PerfCellLossRatio_Type()
)
mlbasUL24PerfCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfCellLossRatio.setStatus("mandatory")
_MlbasUL24PerfUbrDiscCell_Type = Integer32
_MlbasUL24PerfUbrDiscCell_Object = MibTableColumn
mlbasUL24PerfUbrDiscCell = _MlbasUL24PerfUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 5),
    _MlbasUL24PerfUbrDiscCell_Type()
)
mlbasUL24PerfUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfUbrDiscCell.setStatus("mandatory")
_MlbasUL24PerfCbrDiscCell_Type = Integer32
_MlbasUL24PerfCbrDiscCell_Object = MibTableColumn
mlbasUL24PerfCbrDiscCell = _MlbasUL24PerfCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 6),
    _MlbasUL24PerfCbrDiscCell_Type()
)
mlbasUL24PerfCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfCbrDiscCell.setStatus("mandatory")
_MlbasUL24PerfAvailTime_Type = Integer32
_MlbasUL24PerfAvailTime_Object = MibTableColumn
mlbasUL24PerfAvailTime = _MlbasUL24PerfAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 7),
    _MlbasUL24PerfAvailTime_Type()
)
mlbasUL24PerfAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfAvailTime.setStatus("mandatory")
_MlbasUL24PerfUnavailTime_Type = Integer32
_MlbasUL24PerfUnavailTime_Object = MibTableColumn
mlbasUL24PerfUnavailTime = _MlbasUL24PerfUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 8),
    _MlbasUL24PerfUnavailTime_Type()
)
mlbasUL24PerfUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfUnavailTime.setStatus("mandatory")
_MlbasUL24PerfErroredSecRatio_Type = Integer32
_MlbasUL24PerfErroredSecRatio_Object = MibTableColumn
mlbasUL24PerfErroredSecRatio = _MlbasUL24PerfErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 9),
    _MlbasUL24PerfErroredSecRatio_Type()
)
mlbasUL24PerfErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfErroredSecRatio.setStatus("mandatory")
_MlbasUL24PerfSevErroredSecRatio_Type = Integer32
_MlbasUL24PerfSevErroredSecRatio_Object = MibTableColumn
mlbasUL24PerfSevErroredSecRatio = _MlbasUL24PerfSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 10),
    _MlbasUL24PerfSevErroredSecRatio_Type()
)
mlbasUL24PerfSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfSevErroredSecRatio.setStatus("mandatory")
_MlbasUL24PerfBgBlockErrRatio_Type = Integer32
_MlbasUL24PerfBgBlockErrRatio_Object = MibTableColumn
mlbasUL24PerfBgBlockErrRatio = _MlbasUL24PerfBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 11),
    _MlbasUL24PerfBgBlockErrRatio_Type()
)
mlbasUL24PerfBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfBgBlockErrRatio.setStatus("mandatory")
_MlbasUL24PerfMinInPower_Type = Integer32
_MlbasUL24PerfMinInPower_Object = MibTableColumn
mlbasUL24PerfMinInPower = _MlbasUL24PerfMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 12),
    _MlbasUL24PerfMinInPower_Type()
)
mlbasUL24PerfMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfMinInPower.setStatus("mandatory")
_MlbasUL24PerfMaxInPower_Type = Integer32
_MlbasUL24PerfMaxInPower_Object = MibTableColumn
mlbasUL24PerfMaxInPower = _MlbasUL24PerfMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 13),
    _MlbasUL24PerfMaxInPower_Type()
)
mlbasUL24PerfMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfMaxInPower.setStatus("mandatory")
_MlbasUL24PerfAverageInPower_Type = Integer32
_MlbasUL24PerfAverageInPower_Object = MibTableColumn
mlbasUL24PerfAverageInPower = _MlbasUL24PerfAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 14),
    _MlbasUL24PerfAverageInPower_Type()
)
mlbasUL24PerfAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfAverageInPower.setStatus("mandatory")
_MlbasUL24PerfMinOutPower_Type = Integer32
_MlbasUL24PerfMinOutPower_Object = MibTableColumn
mlbasUL24PerfMinOutPower = _MlbasUL24PerfMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 15),
    _MlbasUL24PerfMinOutPower_Type()
)
mlbasUL24PerfMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfMinOutPower.setStatus("mandatory")
_MlbasUL24PerfMaxOutPower_Type = Integer32
_MlbasUL24PerfMaxOutPower_Object = MibTableColumn
mlbasUL24PerfMaxOutPower = _MlbasUL24PerfMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 16),
    _MlbasUL24PerfMaxOutPower_Type()
)
mlbasUL24PerfMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfMaxOutPower.setStatus("mandatory")
_MlbasUL24PerfAverageOutPower_Type = Integer32
_MlbasUL24PerfAverageOutPower_Object = MibTableColumn
mlbasUL24PerfAverageOutPower = _MlbasUL24PerfAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 17),
    _MlbasUL24PerfAverageOutPower_Type()
)
mlbasUL24PerfAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfAverageOutPower.setStatus("mandatory")


class _MlbasUL24PerfTerminalId_Type(DisplayString):
    """Custom type mlbasUL24PerfTerminalId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MlbasUL24PerfTerminalId_Type.__name__ = "DisplayString"
_MlbasUL24PerfTerminalId_Object = MibTableColumn
mlbasUL24PerfTerminalId = _MlbasUL24PerfTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 8, 1, 1, 18),
    _MlbasUL24PerfTerminalId_Type()
)
mlbasUL24PerfTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24PerfTerminalId.setStatus("mandatory")
_MlbasDownLinkLog15min_ObjectIdentity = ObjectIdentity
mlbasDownLinkLog15min = _MlbasDownLinkLog15min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9)
)
_MlbasDownLinkLog15minTable_Object = MibTable
mlbasDownLinkLog15minTable = _MlbasDownLinkLog15minTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1)
)
if mibBuilder.loadTexts:
    mlbasDownLinkLog15minTable.setStatus("mandatory")
_MlbasDownLinkLog15minEntry_Object = MibTableRow
mlbasDownLinkLog15minEntry = _MlbasDownLinkLog15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1)
)
mlbasDownLinkLog15minEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    mlbasDownLinkLog15minEntry.setStatus("mandatory")
_MlbasDL15LogCellErrRatio_Type = Integer32
_MlbasDL15LogCellErrRatio_Object = MibTableColumn
mlbasDL15LogCellErrRatio = _MlbasDL15LogCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 1),
    _MlbasDL15LogCellErrRatio_Type()
)
mlbasDL15LogCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogCellErrRatio.setStatus("mandatory")
_MlbasDL15LogCellLossRatio_Type = Integer32
_MlbasDL15LogCellLossRatio_Object = MibTableColumn
mlbasDL15LogCellLossRatio = _MlbasDL15LogCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 2),
    _MlbasDL15LogCellLossRatio_Type()
)
mlbasDL15LogCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogCellLossRatio.setStatus("mandatory")
_MlbasDL15LogUbrDiscCell_Type = Integer32
_MlbasDL15LogUbrDiscCell_Object = MibTableColumn
mlbasDL15LogUbrDiscCell = _MlbasDL15LogUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 3),
    _MlbasDL15LogUbrDiscCell_Type()
)
mlbasDL15LogUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogUbrDiscCell.setStatus("mandatory")
_MlbasDL15LogCbrDiscCell_Type = Integer32
_MlbasDL15LogCbrDiscCell_Object = MibTableColumn
mlbasDL15LogCbrDiscCell = _MlbasDL15LogCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 4),
    _MlbasDL15LogCbrDiscCell_Type()
)
mlbasDL15LogCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogCbrDiscCell.setStatus("mandatory")
_MlbasDL15LogAvailTime_Type = Integer32
_MlbasDL15LogAvailTime_Object = MibTableColumn
mlbasDL15LogAvailTime = _MlbasDL15LogAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 5),
    _MlbasDL15LogAvailTime_Type()
)
mlbasDL15LogAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogAvailTime.setStatus("mandatory")
_MlbasDL15LogUnavailTime_Type = Integer32
_MlbasDL15LogUnavailTime_Object = MibTableColumn
mlbasDL15LogUnavailTime = _MlbasDL15LogUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 6),
    _MlbasDL15LogUnavailTime_Type()
)
mlbasDL15LogUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogUnavailTime.setStatus("mandatory")
_MlbasDL15LogErroredSecRatio_Type = Integer32
_MlbasDL15LogErroredSecRatio_Object = MibTableColumn
mlbasDL15LogErroredSecRatio = _MlbasDL15LogErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 7),
    _MlbasDL15LogErroredSecRatio_Type()
)
mlbasDL15LogErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogErroredSecRatio.setStatus("mandatory")
_MlbasDL15LogSevErroredSecRatio_Type = Integer32
_MlbasDL15LogSevErroredSecRatio_Object = MibTableColumn
mlbasDL15LogSevErroredSecRatio = _MlbasDL15LogSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 8),
    _MlbasDL15LogSevErroredSecRatio_Type()
)
mlbasDL15LogSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogSevErroredSecRatio.setStatus("mandatory")
_MlbasDL15LogBgBlockErrRatio_Type = Integer32
_MlbasDL15LogBgBlockErrRatio_Object = MibTableColumn
mlbasDL15LogBgBlockErrRatio = _MlbasDL15LogBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 9),
    _MlbasDL15LogBgBlockErrRatio_Type()
)
mlbasDL15LogBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogBgBlockErrRatio.setStatus("mandatory")
_MlbasDL15LogMinInPower_Type = Integer32
_MlbasDL15LogMinInPower_Object = MibTableColumn
mlbasDL15LogMinInPower = _MlbasDL15LogMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 10),
    _MlbasDL15LogMinInPower_Type()
)
mlbasDL15LogMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogMinInPower.setStatus("mandatory")
_MlbasDL15LogMaxInPower_Type = Integer32
_MlbasDL15LogMaxInPower_Object = MibTableColumn
mlbasDL15LogMaxInPower = _MlbasDL15LogMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 11),
    _MlbasDL15LogMaxInPower_Type()
)
mlbasDL15LogMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogMaxInPower.setStatus("mandatory")
_MlbasDL15LogAverageInPower_Type = Integer32
_MlbasDL15LogAverageInPower_Object = MibTableColumn
mlbasDL15LogAverageInPower = _MlbasDL15LogAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 12),
    _MlbasDL15LogAverageInPower_Type()
)
mlbasDL15LogAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogAverageInPower.setStatus("mandatory")
_MlbasDL15LogMinOutPower_Type = Integer32
_MlbasDL15LogMinOutPower_Object = MibTableColumn
mlbasDL15LogMinOutPower = _MlbasDL15LogMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 13),
    _MlbasDL15LogMinOutPower_Type()
)
mlbasDL15LogMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogMinOutPower.setStatus("mandatory")
_MlbasDL15LogMaxOutPower_Type = Integer32
_MlbasDL15LogMaxOutPower_Object = MibTableColumn
mlbasDL15LogMaxOutPower = _MlbasDL15LogMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 14),
    _MlbasDL15LogMaxOutPower_Type()
)
mlbasDL15LogMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogMaxOutPower.setStatus("mandatory")
_MlbasDL15LogAverageOutPower_Type = Integer32
_MlbasDL15LogAverageOutPower_Object = MibTableColumn
mlbasDL15LogAverageOutPower = _MlbasDL15LogAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 9, 1, 1, 15),
    _MlbasDL15LogAverageOutPower_Type()
)
mlbasDL15LogAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL15LogAverageOutPower.setStatus("mandatory")
_MlbasUpLinkLog15min_ObjectIdentity = ObjectIdentity
mlbasUpLinkLog15min = _MlbasUpLinkLog15min_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10)
)
_MlbasUpLinkLog15minTable_Object = MibTable
mlbasUpLinkLog15minTable = _MlbasUpLinkLog15minTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1)
)
if mibBuilder.loadTexts:
    mlbasUpLinkLog15minTable.setStatus("mandatory")
_MlbasUpLinkLog15minEntry_Object = MibTableRow
mlbasUpLinkLog15minEntry = _MlbasUpLinkLog15minEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1)
)
mlbasUpLinkLog15minEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    mlbasUpLinkLog15minEntry.setStatus("mandatory")
_MlbasUL15LogCellErrRatio_Type = Integer32
_MlbasUL15LogCellErrRatio_Object = MibTableColumn
mlbasUL15LogCellErrRatio = _MlbasUL15LogCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 1),
    _MlbasUL15LogCellErrRatio_Type()
)
mlbasUL15LogCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogCellErrRatio.setStatus("mandatory")
_MlbasUL15LogCellLossRatio_Type = Integer32
_MlbasUL15LogCellLossRatio_Object = MibTableColumn
mlbasUL15LogCellLossRatio = _MlbasUL15LogCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 2),
    _MlbasUL15LogCellLossRatio_Type()
)
mlbasUL15LogCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogCellLossRatio.setStatus("mandatory")
_MlbasUL15LogUbrDiscCell_Type = Integer32
_MlbasUL15LogUbrDiscCell_Object = MibTableColumn
mlbasUL15LogUbrDiscCell = _MlbasUL15LogUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 3),
    _MlbasUL15LogUbrDiscCell_Type()
)
mlbasUL15LogUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogUbrDiscCell.setStatus("mandatory")
_MlbasUL15LogCbrDiscCell_Type = Integer32
_MlbasUL15LogCbrDiscCell_Object = MibTableColumn
mlbasUL15LogCbrDiscCell = _MlbasUL15LogCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 4),
    _MlbasUL15LogCbrDiscCell_Type()
)
mlbasUL15LogCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogCbrDiscCell.setStatus("mandatory")
_MlbasUL15LogAvailTime_Type = Integer32
_MlbasUL15LogAvailTime_Object = MibTableColumn
mlbasUL15LogAvailTime = _MlbasUL15LogAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 5),
    _MlbasUL15LogAvailTime_Type()
)
mlbasUL15LogAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogAvailTime.setStatus("mandatory")
_MlbasUL15LogUnavailTime_Type = Integer32
_MlbasUL15LogUnavailTime_Object = MibTableColumn
mlbasUL15LogUnavailTime = _MlbasUL15LogUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 6),
    _MlbasUL15LogUnavailTime_Type()
)
mlbasUL15LogUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogUnavailTime.setStatus("mandatory")
_MlbasUL15LogErroredSecRatio_Type = Integer32
_MlbasUL15LogErroredSecRatio_Object = MibTableColumn
mlbasUL15LogErroredSecRatio = _MlbasUL15LogErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 7),
    _MlbasUL15LogErroredSecRatio_Type()
)
mlbasUL15LogErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogErroredSecRatio.setStatus("mandatory")
_MlbasUL15LogSevErroredSecRatio_Type = Integer32
_MlbasUL15LogSevErroredSecRatio_Object = MibTableColumn
mlbasUL15LogSevErroredSecRatio = _MlbasUL15LogSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 8),
    _MlbasUL15LogSevErroredSecRatio_Type()
)
mlbasUL15LogSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogSevErroredSecRatio.setStatus("mandatory")
_MlbasUL15LogBgBlockErrRatio_Type = Integer32
_MlbasUL15LogBgBlockErrRatio_Object = MibTableColumn
mlbasUL15LogBgBlockErrRatio = _MlbasUL15LogBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 9),
    _MlbasUL15LogBgBlockErrRatio_Type()
)
mlbasUL15LogBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogBgBlockErrRatio.setStatus("mandatory")
_MlbasUL15LogMinInPower_Type = Integer32
_MlbasUL15LogMinInPower_Object = MibTableColumn
mlbasUL15LogMinInPower = _MlbasUL15LogMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 10),
    _MlbasUL15LogMinInPower_Type()
)
mlbasUL15LogMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogMinInPower.setStatus("mandatory")
_MlbasUL15LogMaxInPower_Type = Integer32
_MlbasUL15LogMaxInPower_Object = MibTableColumn
mlbasUL15LogMaxInPower = _MlbasUL15LogMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 11),
    _MlbasUL15LogMaxInPower_Type()
)
mlbasUL15LogMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogMaxInPower.setStatus("mandatory")
_MlbasUL15LogAverageInPower_Type = Integer32
_MlbasUL15LogAverageInPower_Object = MibTableColumn
mlbasUL15LogAverageInPower = _MlbasUL15LogAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 12),
    _MlbasUL15LogAverageInPower_Type()
)
mlbasUL15LogAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogAverageInPower.setStatus("mandatory")
_MlbasUL15LogMinOutPower_Type = Integer32
_MlbasUL15LogMinOutPower_Object = MibTableColumn
mlbasUL15LogMinOutPower = _MlbasUL15LogMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 13),
    _MlbasUL15LogMinOutPower_Type()
)
mlbasUL15LogMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogMinOutPower.setStatus("mandatory")
_MlbasUL15LogMaxOutPower_Type = Integer32
_MlbasUL15LogMaxOutPower_Object = MibTableColumn
mlbasUL15LogMaxOutPower = _MlbasUL15LogMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 14),
    _MlbasUL15LogMaxOutPower_Type()
)
mlbasUL15LogMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogMaxOutPower.setStatus("mandatory")
_MlbasUL15LogAverageOutPower_Type = Integer32
_MlbasUL15LogAverageOutPower_Object = MibTableColumn
mlbasUL15LogAverageOutPower = _MlbasUL15LogAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 10, 1, 1, 15),
    _MlbasUL15LogAverageOutPower_Type()
)
mlbasUL15LogAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL15LogAverageOutPower.setStatus("mandatory")
_MlbasDownLinkLog24hour_ObjectIdentity = ObjectIdentity
mlbasDownLinkLog24hour = _MlbasDownLinkLog24hour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11)
)
_MlbasDownLinkLog24hourTable_Object = MibTable
mlbasDownLinkLog24hourTable = _MlbasDownLinkLog24hourTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1)
)
if mibBuilder.loadTexts:
    mlbasDownLinkLog24hourTable.setStatus("mandatory")
_MlbasDownLinkLog24hourEntry_Object = MibTableRow
mlbasDownLinkLog24hourEntry = _MlbasDownLinkLog24hourEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1)
)
mlbasDownLinkLog24hourEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    mlbasDownLinkLog24hourEntry.setStatus("mandatory")
_MlbasDL24LogCellErrRatio_Type = Integer32
_MlbasDL24LogCellErrRatio_Object = MibTableColumn
mlbasDL24LogCellErrRatio = _MlbasDL24LogCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 1),
    _MlbasDL24LogCellErrRatio_Type()
)
mlbasDL24LogCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogCellErrRatio.setStatus("mandatory")
_MlbasDL24LogCellLossRatio_Type = Integer32
_MlbasDL24LogCellLossRatio_Object = MibTableColumn
mlbasDL24LogCellLossRatio = _MlbasDL24LogCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 2),
    _MlbasDL24LogCellLossRatio_Type()
)
mlbasDL24LogCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogCellLossRatio.setStatus("mandatory")
_MlbasDL24LogUbrDiscCell_Type = Integer32
_MlbasDL24LogUbrDiscCell_Object = MibTableColumn
mlbasDL24LogUbrDiscCell = _MlbasDL24LogUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 3),
    _MlbasDL24LogUbrDiscCell_Type()
)
mlbasDL24LogUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogUbrDiscCell.setStatus("mandatory")
_MlbasDL24LogCbrDiscCell_Type = Integer32
_MlbasDL24LogCbrDiscCell_Object = MibTableColumn
mlbasDL24LogCbrDiscCell = _MlbasDL24LogCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 4),
    _MlbasDL24LogCbrDiscCell_Type()
)
mlbasDL24LogCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogCbrDiscCell.setStatus("mandatory")
_MlbasDL24LogAvailTime_Type = Integer32
_MlbasDL24LogAvailTime_Object = MibTableColumn
mlbasDL24LogAvailTime = _MlbasDL24LogAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 5),
    _MlbasDL24LogAvailTime_Type()
)
mlbasDL24LogAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogAvailTime.setStatus("mandatory")
_MlbasDL24LogUnavailTime_Type = Integer32
_MlbasDL24LogUnavailTime_Object = MibTableColumn
mlbasDL24LogUnavailTime = _MlbasDL24LogUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 6),
    _MlbasDL24LogUnavailTime_Type()
)
mlbasDL24LogUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogUnavailTime.setStatus("mandatory")
_MlbasDL24LogErroredSecRatio_Type = Integer32
_MlbasDL24LogErroredSecRatio_Object = MibTableColumn
mlbasDL24LogErroredSecRatio = _MlbasDL24LogErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 7),
    _MlbasDL24LogErroredSecRatio_Type()
)
mlbasDL24LogErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogErroredSecRatio.setStatus("mandatory")
_MlbasDL24LogSevErroredSecRatio_Type = Integer32
_MlbasDL24LogSevErroredSecRatio_Object = MibTableColumn
mlbasDL24LogSevErroredSecRatio = _MlbasDL24LogSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 8),
    _MlbasDL24LogSevErroredSecRatio_Type()
)
mlbasDL24LogSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogSevErroredSecRatio.setStatus("mandatory")
_MlbasDL24LogBgBlockErrRatio_Type = Integer32
_MlbasDL24LogBgBlockErrRatio_Object = MibTableColumn
mlbasDL24LogBgBlockErrRatio = _MlbasDL24LogBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 9),
    _MlbasDL24LogBgBlockErrRatio_Type()
)
mlbasDL24LogBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogBgBlockErrRatio.setStatus("mandatory")
_MlbasDL24LogMinInPower_Type = Integer32
_MlbasDL24LogMinInPower_Object = MibTableColumn
mlbasDL24LogMinInPower = _MlbasDL24LogMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 10),
    _MlbasDL24LogMinInPower_Type()
)
mlbasDL24LogMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogMinInPower.setStatus("mandatory")
_MlbasDL24LogMaxInPower_Type = Integer32
_MlbasDL24LogMaxInPower_Object = MibTableColumn
mlbasDL24LogMaxInPower = _MlbasDL24LogMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 11),
    _MlbasDL24LogMaxInPower_Type()
)
mlbasDL24LogMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogMaxInPower.setStatus("mandatory")
_MlbasDL24LogAverageInPower_Type = Integer32
_MlbasDL24LogAverageInPower_Object = MibTableColumn
mlbasDL24LogAverageInPower = _MlbasDL24LogAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 12),
    _MlbasDL24LogAverageInPower_Type()
)
mlbasDL24LogAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogAverageInPower.setStatus("mandatory")
_MlbasDL24LogMinOutPower_Type = Integer32
_MlbasDL24LogMinOutPower_Object = MibTableColumn
mlbasDL24LogMinOutPower = _MlbasDL24LogMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 13),
    _MlbasDL24LogMinOutPower_Type()
)
mlbasDL24LogMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogMinOutPower.setStatus("mandatory")
_MlbasDL24LogMaxOutPower_Type = Integer32
_MlbasDL24LogMaxOutPower_Object = MibTableColumn
mlbasDL24LogMaxOutPower = _MlbasDL24LogMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 14),
    _MlbasDL24LogMaxOutPower_Type()
)
mlbasDL24LogMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogMaxOutPower.setStatus("mandatory")
_MlbasDL24LogAverageOutPower_Type = Integer32
_MlbasDL24LogAverageOutPower_Object = MibTableColumn
mlbasDL24LogAverageOutPower = _MlbasDL24LogAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 11, 1, 1, 15),
    _MlbasDL24LogAverageOutPower_Type()
)
mlbasDL24LogAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasDL24LogAverageOutPower.setStatus("mandatory")
_MlbasUpLinkLog24hour_ObjectIdentity = ObjectIdentity
mlbasUpLinkLog24hour = _MlbasUpLinkLog24hour_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12)
)
_MlbasUpLinkLog24hourTable_Object = MibTable
mlbasUpLinkLog24hourTable = _MlbasUpLinkLog24hourTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1)
)
if mibBuilder.loadTexts:
    mlbasUpLinkLog24hourTable.setStatus("mandatory")
_MlbasUpLinkLog24hourEntry_Object = MibTableRow
mlbasUpLinkLog24hourEntry = _MlbasUpLinkLog24hourEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1)
)
mlbasUpLinkLog24hourEntry.setIndexNames(
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSystemNodeIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardSubrackIndex"),
    (0, "ANS-EQUIPMENT-MIB", "ansBoardPosition"),
)
if mibBuilder.loadTexts:
    mlbasUpLinkLog24hourEntry.setStatus("mandatory")
_MlbasUL24LogCellErrRatio_Type = Integer32
_MlbasUL24LogCellErrRatio_Object = MibTableColumn
mlbasUL24LogCellErrRatio = _MlbasUL24LogCellErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 1),
    _MlbasUL24LogCellErrRatio_Type()
)
mlbasUL24LogCellErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogCellErrRatio.setStatus("mandatory")
_MlbasUL24LogCellLossRatio_Type = Integer32
_MlbasUL24LogCellLossRatio_Object = MibTableColumn
mlbasUL24LogCellLossRatio = _MlbasUL24LogCellLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 2),
    _MlbasUL24LogCellLossRatio_Type()
)
mlbasUL24LogCellLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogCellLossRatio.setStatus("mandatory")
_MlbasUL24LogUbrDiscCell_Type = Integer32
_MlbasUL24LogUbrDiscCell_Object = MibTableColumn
mlbasUL24LogUbrDiscCell = _MlbasUL24LogUbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 3),
    _MlbasUL24LogUbrDiscCell_Type()
)
mlbasUL24LogUbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogUbrDiscCell.setStatus("mandatory")
_MlbasUL24LogCbrDiscCell_Type = Integer32
_MlbasUL24LogCbrDiscCell_Object = MibTableColumn
mlbasUL24LogCbrDiscCell = _MlbasUL24LogCbrDiscCell_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 4),
    _MlbasUL24LogCbrDiscCell_Type()
)
mlbasUL24LogCbrDiscCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogCbrDiscCell.setStatus("mandatory")
_MlbasUL24LogAvailTime_Type = Integer32
_MlbasUL24LogAvailTime_Object = MibTableColumn
mlbasUL24LogAvailTime = _MlbasUL24LogAvailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 5),
    _MlbasUL24LogAvailTime_Type()
)
mlbasUL24LogAvailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogAvailTime.setStatus("mandatory")
_MlbasUL24LogUnavailTime_Type = Integer32
_MlbasUL24LogUnavailTime_Object = MibTableColumn
mlbasUL24LogUnavailTime = _MlbasUL24LogUnavailTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 6),
    _MlbasUL24LogUnavailTime_Type()
)
mlbasUL24LogUnavailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogUnavailTime.setStatus("mandatory")
_MlbasUL24LogErroredSecRatio_Type = Integer32
_MlbasUL24LogErroredSecRatio_Object = MibTableColumn
mlbasUL24LogErroredSecRatio = _MlbasUL24LogErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 7),
    _MlbasUL24LogErroredSecRatio_Type()
)
mlbasUL24LogErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogErroredSecRatio.setStatus("mandatory")
_MlbasUL24LogSevErroredSecRatio_Type = Integer32
_MlbasUL24LogSevErroredSecRatio_Object = MibTableColumn
mlbasUL24LogSevErroredSecRatio = _MlbasUL24LogSevErroredSecRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 8),
    _MlbasUL24LogSevErroredSecRatio_Type()
)
mlbasUL24LogSevErroredSecRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogSevErroredSecRatio.setStatus("mandatory")
_MlbasUL24LogBgBlockErrRatio_Type = Integer32
_MlbasUL24LogBgBlockErrRatio_Object = MibTableColumn
mlbasUL24LogBgBlockErrRatio = _MlbasUL24LogBgBlockErrRatio_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 9),
    _MlbasUL24LogBgBlockErrRatio_Type()
)
mlbasUL24LogBgBlockErrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogBgBlockErrRatio.setStatus("mandatory")
_MlbasUL24LogMinInPower_Type = Integer32
_MlbasUL24LogMinInPower_Object = MibTableColumn
mlbasUL24LogMinInPower = _MlbasUL24LogMinInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 10),
    _MlbasUL24LogMinInPower_Type()
)
mlbasUL24LogMinInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogMinInPower.setStatus("mandatory")
_MlbasUL24LogMaxInPower_Type = Integer32
_MlbasUL24LogMaxInPower_Object = MibTableColumn
mlbasUL24LogMaxInPower = _MlbasUL24LogMaxInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 11),
    _MlbasUL24LogMaxInPower_Type()
)
mlbasUL24LogMaxInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogMaxInPower.setStatus("mandatory")
_MlbasUL24LogAverageInPower_Type = Integer32
_MlbasUL24LogAverageInPower_Object = MibTableColumn
mlbasUL24LogAverageInPower = _MlbasUL24LogAverageInPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 12),
    _MlbasUL24LogAverageInPower_Type()
)
mlbasUL24LogAverageInPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogAverageInPower.setStatus("mandatory")
_MlbasUL24LogMinOutPower_Type = Integer32
_MlbasUL24LogMinOutPower_Object = MibTableColumn
mlbasUL24LogMinOutPower = _MlbasUL24LogMinOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 13),
    _MlbasUL24LogMinOutPower_Type()
)
mlbasUL24LogMinOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogMinOutPower.setStatus("mandatory")
_MlbasUL24LogMaxOutPower_Type = Integer32
_MlbasUL24LogMaxOutPower_Object = MibTableColumn
mlbasUL24LogMaxOutPower = _MlbasUL24LogMaxOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 14),
    _MlbasUL24LogMaxOutPower_Type()
)
mlbasUL24LogMaxOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogMaxOutPower.setStatus("mandatory")
_MlbasUL24LogAverageOutPower_Type = Integer32
_MlbasUL24LogAverageOutPower_Object = MibTableColumn
mlbasUL24LogAverageOutPower = _MlbasUL24LogAverageOutPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 12, 1, 1, 15),
    _MlbasUL24LogAverageOutPower_Type()
)
mlbasUL24LogAverageOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasUL24LogAverageOutPower.setStatus("mandatory")
_MlbasServiceUnitPort_ObjectIdentity = ObjectIdentity
mlbasServiceUnitPort = _MlbasServiceUnitPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 13)
)
_MlbasServiceUnitPortTable_Object = MibTable
mlbasServiceUnitPortTable = _MlbasServiceUnitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 13, 1)
)
if mibBuilder.loadTexts:
    mlbasServiceUnitPortTable.setStatus("mandatory")
_MlbasServiceUnitPortEntry_Object = MibTableRow
mlbasServiceUnitPortEntry = _MlbasServiceUnitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 13, 1, 1)
)
mlbasServiceUnitPortEntry.setIndexNames(
    (0, "ANS-GS-MIB", "ansAccessUserPortSystemNode"),
    (0, "ANS-GS-MIB", "ansAccessUserPortSubrack"),
    (0, "ANS-GS-MIB", "ansAccessUserPortPosition"),
    (0, "ANS-GS-MIB", "ansAccessUserPortIndex"),
)
if mibBuilder.loadTexts:
    mlbasServiceUnitPortEntry.setStatus("mandatory")
_MlbasSUPortPosition_Type = Integer32
_MlbasSUPortPosition_Object = MibTableColumn
mlbasSUPortPosition = _MlbasSUPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 13, 1, 1, 1),
    _MlbasSUPortPosition_Type()
)
mlbasSUPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSUPortPosition.setStatus("mandatory")
_MlbasSUPortIndex_Type = Integer32
_MlbasSUPortIndex_Object = MibTableColumn
mlbasSUPortIndex = _MlbasSUPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 96, 115, 5, 13, 1, 1, 2),
    _MlbasSUPortIndex_Type()
)
mlbasSUPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mlbasSUPortIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANS-MLBAS-MIB",
    **{"mlbas": mlbas,
       "mlbasRadioNode": mlbasRadioNode,
       "mlbasRadioNodeTable": mlbasRadioNodeTable,
       "mlbasRadioNodeEntry": mlbasRadioNodeEntry,
       "mlbasRnCUId": mlbasRnCUId,
       "mlbasRnCUSecurity": mlbasRnCUSecurity,
       "mlbasRnCUBerThreshold": mlbasRnCUBerThreshold,
       "mlbasRnCUBwLimit": mlbasRnCUBwLimit,
       "mlbasRnCULoopMode": mlbasRnCULoopMode,
       "mlbasRnCULoopPoint": mlbasRnCULoopPoint,
       "mlbasRnCUAlarmLevel": mlbasRnCUAlarmLevel,
       "mlbasRnCUSignedOnAts": mlbasRnCUSignedOnAts,
       "mlbasRnCUSignedOffAts": mlbasRnCUSignedOffAts,
       "mlbasRnCUChBw": mlbasRnCUChBw,
       "mlbasRnCUHwIdModem": mlbasRnCUHwIdModem,
       "mlbasRnCUSwIdModem": mlbasRnCUSwIdModem,
       "mlbasRnRUDownFreq": mlbasRnRUDownFreq,
       "mlbasRnRUUpFreq": mlbasRnRUUpFreq,
       "mlbasRnRUDownFreqMin": mlbasRnRUDownFreqMin,
       "mlbasRnRUDownFreqMax": mlbasRnRUDownFreqMax,
       "mlbasRnRUFreqDuplex": mlbasRnRUFreqDuplex,
       "mlbasRnRUFreqStep": mlbasRnRUFreqStep,
       "mlbasRnRUOutputPower": mlbasRnRUOutputPower,
       "mlbasRnRUOutputPowerMin": mlbasRnRUOutputPowerMin,
       "mlbasRnRUOutputPowerMax": mlbasRnRUOutputPowerMax,
       "mlbasRnRUHwIdRadio": mlbasRnRUHwIdRadio,
       "mlbasRnRUSwIdRadio": mlbasRnRUSwIdRadio,
       "mlbasRnInterfLevel": mlbasRnInterfLevel,
       "mlbasRnRSSIEXP": mlbasRnRSSIEXP,
       "mlbasRnCUSignOffAts": mlbasRnCUSignOffAts,
       "mlbasRnSwitchBoardAction": mlbasRnSwitchBoardAction,
       "mlbasAccessTerminalSlot": mlbasAccessTerminalSlot,
       "mlbasAccessTerminalSlotTable": mlbasAccessTerminalSlotTable,
       "mlbasAccessTerminalSlotEntry": mlbasAccessTerminalSlotEntry,
       "mlbasAtSlotTerminalId": mlbasAtSlotTerminalId,
       "mlbasAtSlotRnPos": mlbasAtSlotRnPos,
       "mlbasAtSlotLocation": mlbasAtSlotLocation,
       "mlbasAtSlotSignOnAction": mlbasAtSlotSignOnAction,
       "mlbasAtSlotSignOnStatus": mlbasAtSlotSignOnStatus,
       "mlbasAtSlotRowStatus": mlbasAtSlotRowStatus,
       "mlbasAccessTerminal": mlbasAccessTerminal,
       "mlbasAccessTerminalTable": mlbasAccessTerminalTable,
       "mlbasAccessTerminalEntry": mlbasAccessTerminalEntry,
       "mlbasAtCUPerformance": mlbasAtCUPerformance,
       "mlbasAtCUPerfStart": mlbasAtCUPerfStart,
       "mlbasAtCUAtmLoop": mlbasAtCUAtmLoop,
       "mlbasAtCUBerThreshold": mlbasAtCUBerThreshold,
       "mlbasAtCUValid15MinPerf": mlbasAtCUValid15MinPerf,
       "mlbasAtCUInvalid15MinPerf": mlbasAtCUInvalid15MinPerf,
       "mlbasAtCUValid24HPerf": mlbasAtCUValid24HPerf,
       "mlbasAtCUInvalid24HPerf": mlbasAtCUInvalid24HPerf,
       "mlbasAtCUHwIdModem": mlbasAtCUHwIdModem,
       "mlbasAtCUSwIdModem": mlbasAtCUSwIdModem,
       "mlbasAtRUDownFreq": mlbasAtRUDownFreq,
       "mlbasAtRUUpFreq": mlbasAtRUUpFreq,
       "mlbasAtRUOutputPower": mlbasAtRUOutputPower,
       "mlbasAtRUHwIdRadio": mlbasAtRUHwIdRadio,
       "mlbasAtRUSwIdRadio": mlbasAtRUSwIdRadio,
       "mlbasServiceUnit": mlbasServiceUnit,
       "mlbasServiceUnitTable": mlbasServiceUnitTable,
       "mlbasServiceUnitEntry": mlbasServiceUnitEntry,
       "mlbasSuPos": mlbasSuPos,
       "mlbasSuManagedStatus": mlbasSuManagedStatus,
       "mlbasSuOperState": mlbasSuOperState,
       "mlbasSuHwId": mlbasSuHwId,
       "mlbasSuType": mlbasSuType,
       "mlbasSuPciId": mlbasSuPciId,
       "mlbasSuPciVendor": mlbasSuPciVendor,
       "mlbasSuPortStartIndex": mlbasSuPortStartIndex,
       "mlbasSuNumOfPorts": mlbasSuNumOfPorts,
       "mlbasDownLinkPerf15min": mlbasDownLinkPerf15min,
       "mlbasDownLinkPerf15minTable": mlbasDownLinkPerf15minTable,
       "mlbasDownLinkPerf15minEntry": mlbasDownLinkPerf15minEntry,
       "mlbasDL15PeriodIndex": mlbasDL15PeriodIndex,
       "mlbasDL15UpdateTime": mlbasDL15UpdateTime,
       "mlbasDL15PerfCellErrRatio": mlbasDL15PerfCellErrRatio,
       "mlbasDL15PerfCellLossRatio": mlbasDL15PerfCellLossRatio,
       "mlbasDL15PerfUbrDiscCell": mlbasDL15PerfUbrDiscCell,
       "mlbasDL15PerfCbrDiscCell": mlbasDL15PerfCbrDiscCell,
       "mlbasDL15PerfAvailTime": mlbasDL15PerfAvailTime,
       "mlbasDL15PerfUnavailTime": mlbasDL15PerfUnavailTime,
       "mlbasDL15PerfErroredSecRatio": mlbasDL15PerfErroredSecRatio,
       "mlbasDL15PerfSevErroredSecRatio": mlbasDL15PerfSevErroredSecRatio,
       "mlbasDL15PerfBgBlockErrRatio": mlbasDL15PerfBgBlockErrRatio,
       "mlbasDL15PerfMinInPower": mlbasDL15PerfMinInPower,
       "mlbasDL15PerfMaxInPower": mlbasDL15PerfMaxInPower,
       "mlbasDL15PerfAverageInPower": mlbasDL15PerfAverageInPower,
       "mlbasDL15PerfMinOutPower": mlbasDL15PerfMinOutPower,
       "mlbasDL15PerfMaxOutPower": mlbasDL15PerfMaxOutPower,
       "mlbasDL15PerfAverageOutPower": mlbasDL15PerfAverageOutPower,
       "mlbasDL15PerfTerminalId": mlbasDL15PerfTerminalId,
       "mlbasUpLinkPerf15min": mlbasUpLinkPerf15min,
       "mlbasUpLinkPerf15minTable": mlbasUpLinkPerf15minTable,
       "mlbasUpLinkPerf15minEntry": mlbasUpLinkPerf15minEntry,
       "mlbasUL15PeriodIndex": mlbasUL15PeriodIndex,
       "mlbasUL15UpdateTime": mlbasUL15UpdateTime,
       "mlbasUL15PerfCellErrRatio": mlbasUL15PerfCellErrRatio,
       "mlbasUL15PerfCellLossRatio": mlbasUL15PerfCellLossRatio,
       "mlbasUL15PerfUbrDiscCell": mlbasUL15PerfUbrDiscCell,
       "mlbasUL15PerfCbrDiscCell": mlbasUL15PerfCbrDiscCell,
       "mlbasUL15PerfAvailTime": mlbasUL15PerfAvailTime,
       "mlbasUL15PerfUnavailTime": mlbasUL15PerfUnavailTime,
       "mlbasUL15PerfErroredSecRatio": mlbasUL15PerfErroredSecRatio,
       "mlbasUL15PerfSevErroredSecRatio": mlbasUL15PerfSevErroredSecRatio,
       "mlbasUL15PerfBgBlockErrRatio": mlbasUL15PerfBgBlockErrRatio,
       "mlbasUL15PerfMinInPower": mlbasUL15PerfMinInPower,
       "mlbasUL15PerfMaxInPower": mlbasUL15PerfMaxInPower,
       "mlbasUL15PerfAverageInPower": mlbasUL15PerfAverageInPower,
       "mlbasUL15PerfMinOutPower": mlbasUL15PerfMinOutPower,
       "mlbasUL15PerfMaxOutPower": mlbasUL15PerfMaxOutPower,
       "mlbasUL15PerfAverageOutPower": mlbasUL15PerfAverageOutPower,
       "mlbasUL15PerfTerminalId": mlbasUL15PerfTerminalId,
       "mlbasDownLinkPerf24hour": mlbasDownLinkPerf24hour,
       "mlbasDownLinkPerf24hourTable": mlbasDownLinkPerf24hourTable,
       "mlbasDownLinkPerf24hourEntry": mlbasDownLinkPerf24hourEntry,
       "mlbasDL24PeriodIndex": mlbasDL24PeriodIndex,
       "mlbasDL24UpdateTime": mlbasDL24UpdateTime,
       "mlbasDL24PerfCellErrRatio": mlbasDL24PerfCellErrRatio,
       "mlbasDL24PerfCellLossRatio": mlbasDL24PerfCellLossRatio,
       "mlbasDL24PerfUbrDiscCell": mlbasDL24PerfUbrDiscCell,
       "mlbasDL24PerfCbrDiscCell": mlbasDL24PerfCbrDiscCell,
       "mlbasDL24PerfAvailTime": mlbasDL24PerfAvailTime,
       "mlbasDL24PerfUnavailTime": mlbasDL24PerfUnavailTime,
       "mlbasDL24PerfErroredSecRatio": mlbasDL24PerfErroredSecRatio,
       "mlbasDL24PerfSevErroredSecRatio": mlbasDL24PerfSevErroredSecRatio,
       "mlbasDL24PerfBgBlockErrRatio": mlbasDL24PerfBgBlockErrRatio,
       "mlbasDL24PerfMinInPower": mlbasDL24PerfMinInPower,
       "mlbasDL24PerfMaxInPower": mlbasDL24PerfMaxInPower,
       "mlbasDL24PerfAverageInPower": mlbasDL24PerfAverageInPower,
       "mlbasDL24PerfMinOutPower": mlbasDL24PerfMinOutPower,
       "mlbasDL24PerfMaxOutPower": mlbasDL24PerfMaxOutPower,
       "mlbasDL24PerfAverageOutPower": mlbasDL24PerfAverageOutPower,
       "mlbasDL24PerfTerminalId": mlbasDL24PerfTerminalId,
       "mlbasUpLinkPerf24hour": mlbasUpLinkPerf24hour,
       "mlbasUpLinkPerf24hourTable": mlbasUpLinkPerf24hourTable,
       "mlbasUpLinkPerf24hourEntry": mlbasUpLinkPerf24hourEntry,
       "mlbasUL24PeriodIndex": mlbasUL24PeriodIndex,
       "mlbasUL24UpdateTime": mlbasUL24UpdateTime,
       "mlbasUL24PerfCellErrRatio": mlbasUL24PerfCellErrRatio,
       "mlbasUL24PerfCellLossRatio": mlbasUL24PerfCellLossRatio,
       "mlbasUL24PerfUbrDiscCell": mlbasUL24PerfUbrDiscCell,
       "mlbasUL24PerfCbrDiscCell": mlbasUL24PerfCbrDiscCell,
       "mlbasUL24PerfAvailTime": mlbasUL24PerfAvailTime,
       "mlbasUL24PerfUnavailTime": mlbasUL24PerfUnavailTime,
       "mlbasUL24PerfErroredSecRatio": mlbasUL24PerfErroredSecRatio,
       "mlbasUL24PerfSevErroredSecRatio": mlbasUL24PerfSevErroredSecRatio,
       "mlbasUL24PerfBgBlockErrRatio": mlbasUL24PerfBgBlockErrRatio,
       "mlbasUL24PerfMinInPower": mlbasUL24PerfMinInPower,
       "mlbasUL24PerfMaxInPower": mlbasUL24PerfMaxInPower,
       "mlbasUL24PerfAverageInPower": mlbasUL24PerfAverageInPower,
       "mlbasUL24PerfMinOutPower": mlbasUL24PerfMinOutPower,
       "mlbasUL24PerfMaxOutPower": mlbasUL24PerfMaxOutPower,
       "mlbasUL24PerfAverageOutPower": mlbasUL24PerfAverageOutPower,
       "mlbasUL24PerfTerminalId": mlbasUL24PerfTerminalId,
       "mlbasDownLinkLog15min": mlbasDownLinkLog15min,
       "mlbasDownLinkLog15minTable": mlbasDownLinkLog15minTable,
       "mlbasDownLinkLog15minEntry": mlbasDownLinkLog15minEntry,
       "mlbasDL15LogCellErrRatio": mlbasDL15LogCellErrRatio,
       "mlbasDL15LogCellLossRatio": mlbasDL15LogCellLossRatio,
       "mlbasDL15LogUbrDiscCell": mlbasDL15LogUbrDiscCell,
       "mlbasDL15LogCbrDiscCell": mlbasDL15LogCbrDiscCell,
       "mlbasDL15LogAvailTime": mlbasDL15LogAvailTime,
       "mlbasDL15LogUnavailTime": mlbasDL15LogUnavailTime,
       "mlbasDL15LogErroredSecRatio": mlbasDL15LogErroredSecRatio,
       "mlbasDL15LogSevErroredSecRatio": mlbasDL15LogSevErroredSecRatio,
       "mlbasDL15LogBgBlockErrRatio": mlbasDL15LogBgBlockErrRatio,
       "mlbasDL15LogMinInPower": mlbasDL15LogMinInPower,
       "mlbasDL15LogMaxInPower": mlbasDL15LogMaxInPower,
       "mlbasDL15LogAverageInPower": mlbasDL15LogAverageInPower,
       "mlbasDL15LogMinOutPower": mlbasDL15LogMinOutPower,
       "mlbasDL15LogMaxOutPower": mlbasDL15LogMaxOutPower,
       "mlbasDL15LogAverageOutPower": mlbasDL15LogAverageOutPower,
       "mlbasUpLinkLog15min": mlbasUpLinkLog15min,
       "mlbasUpLinkLog15minTable": mlbasUpLinkLog15minTable,
       "mlbasUpLinkLog15minEntry": mlbasUpLinkLog15minEntry,
       "mlbasUL15LogCellErrRatio": mlbasUL15LogCellErrRatio,
       "mlbasUL15LogCellLossRatio": mlbasUL15LogCellLossRatio,
       "mlbasUL15LogUbrDiscCell": mlbasUL15LogUbrDiscCell,
       "mlbasUL15LogCbrDiscCell": mlbasUL15LogCbrDiscCell,
       "mlbasUL15LogAvailTime": mlbasUL15LogAvailTime,
       "mlbasUL15LogUnavailTime": mlbasUL15LogUnavailTime,
       "mlbasUL15LogErroredSecRatio": mlbasUL15LogErroredSecRatio,
       "mlbasUL15LogSevErroredSecRatio": mlbasUL15LogSevErroredSecRatio,
       "mlbasUL15LogBgBlockErrRatio": mlbasUL15LogBgBlockErrRatio,
       "mlbasUL15LogMinInPower": mlbasUL15LogMinInPower,
       "mlbasUL15LogMaxInPower": mlbasUL15LogMaxInPower,
       "mlbasUL15LogAverageInPower": mlbasUL15LogAverageInPower,
       "mlbasUL15LogMinOutPower": mlbasUL15LogMinOutPower,
       "mlbasUL15LogMaxOutPower": mlbasUL15LogMaxOutPower,
       "mlbasUL15LogAverageOutPower": mlbasUL15LogAverageOutPower,
       "mlbasDownLinkLog24hour": mlbasDownLinkLog24hour,
       "mlbasDownLinkLog24hourTable": mlbasDownLinkLog24hourTable,
       "mlbasDownLinkLog24hourEntry": mlbasDownLinkLog24hourEntry,
       "mlbasDL24LogCellErrRatio": mlbasDL24LogCellErrRatio,
       "mlbasDL24LogCellLossRatio": mlbasDL24LogCellLossRatio,
       "mlbasDL24LogUbrDiscCell": mlbasDL24LogUbrDiscCell,
       "mlbasDL24LogCbrDiscCell": mlbasDL24LogCbrDiscCell,
       "mlbasDL24LogAvailTime": mlbasDL24LogAvailTime,
       "mlbasDL24LogUnavailTime": mlbasDL24LogUnavailTime,
       "mlbasDL24LogErroredSecRatio": mlbasDL24LogErroredSecRatio,
       "mlbasDL24LogSevErroredSecRatio": mlbasDL24LogSevErroredSecRatio,
       "mlbasDL24LogBgBlockErrRatio": mlbasDL24LogBgBlockErrRatio,
       "mlbasDL24LogMinInPower": mlbasDL24LogMinInPower,
       "mlbasDL24LogMaxInPower": mlbasDL24LogMaxInPower,
       "mlbasDL24LogAverageInPower": mlbasDL24LogAverageInPower,
       "mlbasDL24LogMinOutPower": mlbasDL24LogMinOutPower,
       "mlbasDL24LogMaxOutPower": mlbasDL24LogMaxOutPower,
       "mlbasDL24LogAverageOutPower": mlbasDL24LogAverageOutPower,
       "mlbasUpLinkLog24hour": mlbasUpLinkLog24hour,
       "mlbasUpLinkLog24hourTable": mlbasUpLinkLog24hourTable,
       "mlbasUpLinkLog24hourEntry": mlbasUpLinkLog24hourEntry,
       "mlbasUL24LogCellErrRatio": mlbasUL24LogCellErrRatio,
       "mlbasUL24LogCellLossRatio": mlbasUL24LogCellLossRatio,
       "mlbasUL24LogUbrDiscCell": mlbasUL24LogUbrDiscCell,
       "mlbasUL24LogCbrDiscCell": mlbasUL24LogCbrDiscCell,
       "mlbasUL24LogAvailTime": mlbasUL24LogAvailTime,
       "mlbasUL24LogUnavailTime": mlbasUL24LogUnavailTime,
       "mlbasUL24LogErroredSecRatio": mlbasUL24LogErroredSecRatio,
       "mlbasUL24LogSevErroredSecRatio": mlbasUL24LogSevErroredSecRatio,
       "mlbasUL24LogBgBlockErrRatio": mlbasUL24LogBgBlockErrRatio,
       "mlbasUL24LogMinInPower": mlbasUL24LogMinInPower,
       "mlbasUL24LogMaxInPower": mlbasUL24LogMaxInPower,
       "mlbasUL24LogAverageInPower": mlbasUL24LogAverageInPower,
       "mlbasUL24LogMinOutPower": mlbasUL24LogMinOutPower,
       "mlbasUL24LogMaxOutPower": mlbasUL24LogMaxOutPower,
       "mlbasUL24LogAverageOutPower": mlbasUL24LogAverageOutPower,
       "mlbasServiceUnitPort": mlbasServiceUnitPort,
       "mlbasServiceUnitPortTable": mlbasServiceUnitPortTable,
       "mlbasServiceUnitPortEntry": mlbasServiceUnitPortEntry,
       "mlbasSUPortPosition": mlbasSUPortPosition,
       "mlbasSUPortIndex": mlbasSUPortIndex}
)
