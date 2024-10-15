# SNMP MIB module (TOKENRING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOKENRING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:33 2024
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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

dot5 = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot5Table_Object = MibTable
dot5Table = _Dot5Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1)
)
if mibBuilder.loadTexts:
    dot5Table.setStatus("current")
_Dot5Entry_Object = MibTableRow
dot5Entry = _Dot5Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1)
)
dot5Entry.setIndexNames(
    (0, "TOKENRING-MIB", "dot5IfIndex"),
)
if mibBuilder.loadTexts:
    dot5Entry.setStatus("current")
_Dot5IfIndex_Type = Integer32
_Dot5IfIndex_Object = MibTableColumn
dot5IfIndex = _Dot5IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 1),
    _Dot5IfIndex_Type()
)
dot5IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5IfIndex.setStatus("current")


class _Dot5Commands_Type(Integer32):
    """Custom type dot5Commands based on Integer32"""
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
        *(("close", 4),
          ("noop", 1),
          ("open", 2),
          ("reset", 3))
    )


_Dot5Commands_Type.__name__ = "Integer32"
_Dot5Commands_Object = MibTableColumn
dot5Commands = _Dot5Commands_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 2),
    _Dot5Commands_Type()
)
dot5Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5Commands.setStatus("current")


class _Dot5RingStatus_Type(Integer32):
    """Custom type dot5RingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262143),
    )


_Dot5RingStatus_Type.__name__ = "Integer32"
_Dot5RingStatus_Object = MibTableColumn
dot5RingStatus = _Dot5RingStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 3),
    _Dot5RingStatus_Type()
)
dot5RingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingStatus.setStatus("current")


class _Dot5RingState_Type(Integer32):
    """Custom type dot5RingState based on Integer32"""
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
        *(("closed", 2),
          ("closing", 4),
          ("openFailure", 5),
          ("opened", 1),
          ("opening", 3),
          ("ringFailure", 6))
    )


_Dot5RingState_Type.__name__ = "Integer32"
_Dot5RingState_Object = MibTableColumn
dot5RingState = _Dot5RingState_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 4),
    _Dot5RingState_Type()
)
dot5RingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingState.setStatus("current")


class _Dot5RingOpenStatus_Type(Integer32):
    """Custom type dot5RingOpenStatus based on Integer32"""
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
        *(("badParam", 2),
          ("beaconing", 7),
          ("duplicateMAC", 8),
          ("insertionTimeout", 5),
          ("lobeFailed", 3),
          ("noOpen", 1),
          ("open", 11),
          ("removeReceived", 10),
          ("requestFailed", 9),
          ("ringFailed", 6),
          ("signalLoss", 4))
    )


_Dot5RingOpenStatus_Type.__name__ = "Integer32"
_Dot5RingOpenStatus_Object = MibTableColumn
dot5RingOpenStatus = _Dot5RingOpenStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 5),
    _Dot5RingOpenStatus_Type()
)
dot5RingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5RingOpenStatus.setStatus("current")


class _Dot5RingSpeed_Type(Integer32):
    """Custom type dot5RingSpeed based on Integer32"""
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
        *(("fourMegabit", 3),
          ("oneMegabit", 2),
          ("sixteenMegabit", 4),
          ("unknown", 1))
    )


_Dot5RingSpeed_Type.__name__ = "Integer32"
_Dot5RingSpeed_Object = MibTableColumn
dot5RingSpeed = _Dot5RingSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 6),
    _Dot5RingSpeed_Type()
)
dot5RingSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5RingSpeed.setStatus("current")
_Dot5UpStream_Type = MacAddress
_Dot5UpStream_Object = MibTableColumn
dot5UpStream = _Dot5UpStream_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 7),
    _Dot5UpStream_Type()
)
dot5UpStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5UpStream.setStatus("current")


class _Dot5ActMonParticipate_Type(Integer32):
    """Custom type dot5ActMonParticipate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_Dot5ActMonParticipate_Type.__name__ = "Integer32"
_Dot5ActMonParticipate_Object = MibTableColumn
dot5ActMonParticipate = _Dot5ActMonParticipate_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 8),
    _Dot5ActMonParticipate_Type()
)
dot5ActMonParticipate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5ActMonParticipate.setStatus("current")
_Dot5Functional_Type = MacAddress
_Dot5Functional_Object = MibTableColumn
dot5Functional = _Dot5Functional_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 9),
    _Dot5Functional_Type()
)
dot5Functional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot5Functional.setStatus("current")
_Dot5LastBeaconSent_Type = TimeStamp
_Dot5LastBeaconSent_Object = MibTableColumn
dot5LastBeaconSent = _Dot5LastBeaconSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 1, 1, 10),
    _Dot5LastBeaconSent_Type()
)
dot5LastBeaconSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5LastBeaconSent.setStatus("current")
_Dot5StatsTable_Object = MibTable
dot5StatsTable = _Dot5StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2)
)
if mibBuilder.loadTexts:
    dot5StatsTable.setStatus("current")
_Dot5StatsEntry_Object = MibTableRow
dot5StatsEntry = _Dot5StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1)
)
dot5StatsEntry.setIndexNames(
    (0, "TOKENRING-MIB", "dot5StatsIfIndex"),
)
if mibBuilder.loadTexts:
    dot5StatsEntry.setStatus("current")
_Dot5StatsIfIndex_Type = Integer32
_Dot5StatsIfIndex_Object = MibTableColumn
dot5StatsIfIndex = _Dot5StatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 1),
    _Dot5StatsIfIndex_Type()
)
dot5StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsIfIndex.setStatus("current")
_Dot5StatsLineErrors_Type = Counter32
_Dot5StatsLineErrors_Object = MibTableColumn
dot5StatsLineErrors = _Dot5StatsLineErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 2),
    _Dot5StatsLineErrors_Type()
)
dot5StatsLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLineErrors.setStatus("current")
_Dot5StatsBurstErrors_Type = Counter32
_Dot5StatsBurstErrors_Object = MibTableColumn
dot5StatsBurstErrors = _Dot5StatsBurstErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 3),
    _Dot5StatsBurstErrors_Type()
)
dot5StatsBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsBurstErrors.setStatus("current")
_Dot5StatsACErrors_Type = Counter32
_Dot5StatsACErrors_Object = MibTableColumn
dot5StatsACErrors = _Dot5StatsACErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 4),
    _Dot5StatsACErrors_Type()
)
dot5StatsACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsACErrors.setStatus("current")
_Dot5StatsAbortTransErrors_Type = Counter32
_Dot5StatsAbortTransErrors_Object = MibTableColumn
dot5StatsAbortTransErrors = _Dot5StatsAbortTransErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 5),
    _Dot5StatsAbortTransErrors_Type()
)
dot5StatsAbortTransErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsAbortTransErrors.setStatus("current")
_Dot5StatsInternalErrors_Type = Counter32
_Dot5StatsInternalErrors_Object = MibTableColumn
dot5StatsInternalErrors = _Dot5StatsInternalErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 6),
    _Dot5StatsInternalErrors_Type()
)
dot5StatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsInternalErrors.setStatus("current")
_Dot5StatsLostFrameErrors_Type = Counter32
_Dot5StatsLostFrameErrors_Object = MibTableColumn
dot5StatsLostFrameErrors = _Dot5StatsLostFrameErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 7),
    _Dot5StatsLostFrameErrors_Type()
)
dot5StatsLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLostFrameErrors.setStatus("current")
_Dot5StatsReceiveCongestions_Type = Counter32
_Dot5StatsReceiveCongestions_Object = MibTableColumn
dot5StatsReceiveCongestions = _Dot5StatsReceiveCongestions_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 8),
    _Dot5StatsReceiveCongestions_Type()
)
dot5StatsReceiveCongestions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsReceiveCongestions.setStatus("current")
_Dot5StatsFrameCopiedErrors_Type = Counter32
_Dot5StatsFrameCopiedErrors_Object = MibTableColumn
dot5StatsFrameCopiedErrors = _Dot5StatsFrameCopiedErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 9),
    _Dot5StatsFrameCopiedErrors_Type()
)
dot5StatsFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsFrameCopiedErrors.setStatus("current")
_Dot5StatsTokenErrors_Type = Counter32
_Dot5StatsTokenErrors_Object = MibTableColumn
dot5StatsTokenErrors = _Dot5StatsTokenErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 10),
    _Dot5StatsTokenErrors_Type()
)
dot5StatsTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsTokenErrors.setStatus("current")
_Dot5StatsSoftErrors_Type = Counter32
_Dot5StatsSoftErrors_Object = MibTableColumn
dot5StatsSoftErrors = _Dot5StatsSoftErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 11),
    _Dot5StatsSoftErrors_Type()
)
dot5StatsSoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSoftErrors.setStatus("current")
_Dot5StatsHardErrors_Type = Counter32
_Dot5StatsHardErrors_Object = MibTableColumn
dot5StatsHardErrors = _Dot5StatsHardErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 12),
    _Dot5StatsHardErrors_Type()
)
dot5StatsHardErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsHardErrors.setStatus("current")
_Dot5StatsSignalLoss_Type = Counter32
_Dot5StatsSignalLoss_Object = MibTableColumn
dot5StatsSignalLoss = _Dot5StatsSignalLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 13),
    _Dot5StatsSignalLoss_Type()
)
dot5StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSignalLoss.setStatus("current")
_Dot5StatsTransmitBeacons_Type = Counter32
_Dot5StatsTransmitBeacons_Object = MibTableColumn
dot5StatsTransmitBeacons = _Dot5StatsTransmitBeacons_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 14),
    _Dot5StatsTransmitBeacons_Type()
)
dot5StatsTransmitBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsTransmitBeacons.setStatus("current")
_Dot5StatsRecoverys_Type = Counter32
_Dot5StatsRecoverys_Object = MibTableColumn
dot5StatsRecoverys = _Dot5StatsRecoverys_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 15),
    _Dot5StatsRecoverys_Type()
)
dot5StatsRecoverys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsRecoverys.setStatus("current")
_Dot5StatsLobeWires_Type = Counter32
_Dot5StatsLobeWires_Object = MibTableColumn
dot5StatsLobeWires = _Dot5StatsLobeWires_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 16),
    _Dot5StatsLobeWires_Type()
)
dot5StatsLobeWires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsLobeWires.setStatus("current")
_Dot5StatsRemoves_Type = Counter32
_Dot5StatsRemoves_Object = MibTableColumn
dot5StatsRemoves = _Dot5StatsRemoves_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 17),
    _Dot5StatsRemoves_Type()
)
dot5StatsRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsRemoves.setStatus("current")
_Dot5StatsSingles_Type = Counter32
_Dot5StatsSingles_Object = MibTableColumn
dot5StatsSingles = _Dot5StatsSingles_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 18),
    _Dot5StatsSingles_Type()
)
dot5StatsSingles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsSingles.setStatus("current")
_Dot5StatsFreqErrors_Type = Counter32
_Dot5StatsFreqErrors_Object = MibTableColumn
dot5StatsFreqErrors = _Dot5StatsFreqErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 2, 1, 19),
    _Dot5StatsFreqErrors_Type()
)
dot5StatsFreqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5StatsFreqErrors.setStatus("current")
_Dot5Tests_ObjectIdentity = ObjectIdentity
dot5Tests = _Dot5Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 3)
)
_Dot5TestInsertFunc_ObjectIdentity = ObjectIdentity
dot5TestInsertFunc = _Dot5TestInsertFunc_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 3, 1)
)
if mibBuilder.loadTexts:
    dot5TestInsertFunc.setStatus("current")
_Dot5TestFullDuplexLoopBack_ObjectIdentity = ObjectIdentity
dot5TestFullDuplexLoopBack = _Dot5TestFullDuplexLoopBack_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 3, 2)
)
if mibBuilder.loadTexts:
    dot5TestFullDuplexLoopBack.setStatus("current")
_Dot5ChipSets_ObjectIdentity = ObjectIdentity
dot5ChipSets = _Dot5ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 4)
)
_Dot5ChipSetIBM16_ObjectIdentity = ObjectIdentity
dot5ChipSetIBM16 = _Dot5ChipSetIBM16_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 4, 1)
)
if mibBuilder.loadTexts:
    dot5ChipSetIBM16.setStatus("current")
_Dot5ChipSetTItms380_ObjectIdentity = ObjectIdentity
dot5ChipSetTItms380 = _Dot5ChipSetTItms380_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 4, 2)
)
if mibBuilder.loadTexts:
    dot5ChipSetTItms380.setStatus("current")
_Dot5ChipSetTItms380c16_ObjectIdentity = ObjectIdentity
dot5ChipSetTItms380c16 = _Dot5ChipSetTItms380c16_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 4, 3)
)
if mibBuilder.loadTexts:
    dot5ChipSetTItms380c16.setStatus("current")
_Dot5TimerTable_Object = MibTable
dot5TimerTable = _Dot5TimerTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5)
)
if mibBuilder.loadTexts:
    dot5TimerTable.setStatus("obsolete")
_Dot5TimerEntry_Object = MibTableRow
dot5TimerEntry = _Dot5TimerEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1)
)
dot5TimerEntry.setIndexNames(
    (0, "TOKENRING-MIB", "dot5TimerIfIndex"),
)
if mibBuilder.loadTexts:
    dot5TimerEntry.setStatus("obsolete")
_Dot5TimerIfIndex_Type = Integer32
_Dot5TimerIfIndex_Object = MibTableColumn
dot5TimerIfIndex = _Dot5TimerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 1),
    _Dot5TimerIfIndex_Type()
)
dot5TimerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerIfIndex.setStatus("obsolete")
_Dot5TimerReturnRepeat_Type = Integer32
_Dot5TimerReturnRepeat_Object = MibTableColumn
dot5TimerReturnRepeat = _Dot5TimerReturnRepeat_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 2),
    _Dot5TimerReturnRepeat_Type()
)
dot5TimerReturnRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerReturnRepeat.setStatus("obsolete")
_Dot5TimerHolding_Type = Integer32
_Dot5TimerHolding_Object = MibTableColumn
dot5TimerHolding = _Dot5TimerHolding_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 3),
    _Dot5TimerHolding_Type()
)
dot5TimerHolding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerHolding.setStatus("obsolete")
_Dot5TimerQueuePDU_Type = Integer32
_Dot5TimerQueuePDU_Object = MibTableColumn
dot5TimerQueuePDU = _Dot5TimerQueuePDU_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 4),
    _Dot5TimerQueuePDU_Type()
)
dot5TimerQueuePDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerQueuePDU.setStatus("obsolete")
_Dot5TimerValidTransmit_Type = Integer32
_Dot5TimerValidTransmit_Object = MibTableColumn
dot5TimerValidTransmit = _Dot5TimerValidTransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 5),
    _Dot5TimerValidTransmit_Type()
)
dot5TimerValidTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerValidTransmit.setStatus("obsolete")
_Dot5TimerNoToken_Type = Integer32
_Dot5TimerNoToken_Object = MibTableColumn
dot5TimerNoToken = _Dot5TimerNoToken_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 6),
    _Dot5TimerNoToken_Type()
)
dot5TimerNoToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerNoToken.setStatus("obsolete")
_Dot5TimerActiveMon_Type = Integer32
_Dot5TimerActiveMon_Object = MibTableColumn
dot5TimerActiveMon = _Dot5TimerActiveMon_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 7),
    _Dot5TimerActiveMon_Type()
)
dot5TimerActiveMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerActiveMon.setStatus("obsolete")
_Dot5TimerStandbyMon_Type = Integer32
_Dot5TimerStandbyMon_Object = MibTableColumn
dot5TimerStandbyMon = _Dot5TimerStandbyMon_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 8),
    _Dot5TimerStandbyMon_Type()
)
dot5TimerStandbyMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerStandbyMon.setStatus("obsolete")
_Dot5TimerErrorReport_Type = Integer32
_Dot5TimerErrorReport_Object = MibTableColumn
dot5TimerErrorReport = _Dot5TimerErrorReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 9),
    _Dot5TimerErrorReport_Type()
)
dot5TimerErrorReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerErrorReport.setStatus("obsolete")
_Dot5TimerBeaconTransmit_Type = Integer32
_Dot5TimerBeaconTransmit_Object = MibTableColumn
dot5TimerBeaconTransmit = _Dot5TimerBeaconTransmit_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 10),
    _Dot5TimerBeaconTransmit_Type()
)
dot5TimerBeaconTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerBeaconTransmit.setStatus("obsolete")
_Dot5TimerBeaconReceive_Type = Integer32
_Dot5TimerBeaconReceive_Object = MibTableColumn
dot5TimerBeaconReceive = _Dot5TimerBeaconReceive_Object(
    (1, 3, 6, 1, 2, 1, 10, 9, 5, 1, 11),
    _Dot5TimerBeaconReceive_Type()
)
dot5TimerBeaconReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot5TimerBeaconReceive.setStatus("obsolete")
_Dot5Conformance_ObjectIdentity = ObjectIdentity
dot5Conformance = _Dot5Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 6)
)
_Dot5Groups_ObjectIdentity = ObjectIdentity
dot5Groups = _Dot5Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 6, 1)
)
_Dot5Compliances_ObjectIdentity = ObjectIdentity
dot5Compliances = _Dot5Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 9, 6, 2)
)

# Managed Objects groups

dot5StateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 1)
)
dot5StateGroup.setObjects(
      *(("TOKENRING-MIB", "dot5Commands"),
        ("TOKENRING-MIB", "dot5RingStatus"),
        ("TOKENRING-MIB", "dot5RingState"),
        ("TOKENRING-MIB", "dot5RingOpenStatus"),
        ("TOKENRING-MIB", "dot5RingSpeed"),
        ("TOKENRING-MIB", "dot5UpStream"),
        ("TOKENRING-MIB", "dot5ActMonParticipate"),
        ("TOKENRING-MIB", "dot5Functional"),
        ("TOKENRING-MIB", "dot5LastBeaconSent"))
)
if mibBuilder.loadTexts:
    dot5StateGroup.setStatus("current")

dot5StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 9, 6, 1, 2)
)
dot5StatsGroup.setObjects(
      *(("TOKENRING-MIB", "dot5StatsLineErrors"),
        ("TOKENRING-MIB", "dot5StatsBurstErrors"),
        ("TOKENRING-MIB", "dot5StatsACErrors"),
        ("TOKENRING-MIB", "dot5StatsAbortTransErrors"),
        ("TOKENRING-MIB", "dot5StatsInternalErrors"),
        ("TOKENRING-MIB", "dot5StatsLostFrameErrors"),
        ("TOKENRING-MIB", "dot5StatsReceiveCongestions"),
        ("TOKENRING-MIB", "dot5StatsFrameCopiedErrors"),
        ("TOKENRING-MIB", "dot5StatsTokenErrors"),
        ("TOKENRING-MIB", "dot5StatsSoftErrors"),
        ("TOKENRING-MIB", "dot5StatsHardErrors"),
        ("TOKENRING-MIB", "dot5StatsSignalLoss"),
        ("TOKENRING-MIB", "dot5StatsTransmitBeacons"),
        ("TOKENRING-MIB", "dot5StatsRecoverys"),
        ("TOKENRING-MIB", "dot5StatsLobeWires"),
        ("TOKENRING-MIB", "dot5StatsRemoves"),
        ("TOKENRING-MIB", "dot5StatsSingles"),
        ("TOKENRING-MIB", "dot5StatsFreqErrors"))
)
if mibBuilder.loadTexts:
    dot5StatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot5Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 9, 6, 2, 1)
)
if mibBuilder.loadTexts:
    dot5Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOKENRING-MIB",
    **{"dot5": dot5,
       "dot5Table": dot5Table,
       "dot5Entry": dot5Entry,
       "dot5IfIndex": dot5IfIndex,
       "dot5Commands": dot5Commands,
       "dot5RingStatus": dot5RingStatus,
       "dot5RingState": dot5RingState,
       "dot5RingOpenStatus": dot5RingOpenStatus,
       "dot5RingSpeed": dot5RingSpeed,
       "dot5UpStream": dot5UpStream,
       "dot5ActMonParticipate": dot5ActMonParticipate,
       "dot5Functional": dot5Functional,
       "dot5LastBeaconSent": dot5LastBeaconSent,
       "dot5StatsTable": dot5StatsTable,
       "dot5StatsEntry": dot5StatsEntry,
       "dot5StatsIfIndex": dot5StatsIfIndex,
       "dot5StatsLineErrors": dot5StatsLineErrors,
       "dot5StatsBurstErrors": dot5StatsBurstErrors,
       "dot5StatsACErrors": dot5StatsACErrors,
       "dot5StatsAbortTransErrors": dot5StatsAbortTransErrors,
       "dot5StatsInternalErrors": dot5StatsInternalErrors,
       "dot5StatsLostFrameErrors": dot5StatsLostFrameErrors,
       "dot5StatsReceiveCongestions": dot5StatsReceiveCongestions,
       "dot5StatsFrameCopiedErrors": dot5StatsFrameCopiedErrors,
       "dot5StatsTokenErrors": dot5StatsTokenErrors,
       "dot5StatsSoftErrors": dot5StatsSoftErrors,
       "dot5StatsHardErrors": dot5StatsHardErrors,
       "dot5StatsSignalLoss": dot5StatsSignalLoss,
       "dot5StatsTransmitBeacons": dot5StatsTransmitBeacons,
       "dot5StatsRecoverys": dot5StatsRecoverys,
       "dot5StatsLobeWires": dot5StatsLobeWires,
       "dot5StatsRemoves": dot5StatsRemoves,
       "dot5StatsSingles": dot5StatsSingles,
       "dot5StatsFreqErrors": dot5StatsFreqErrors,
       "dot5Tests": dot5Tests,
       "dot5TestInsertFunc": dot5TestInsertFunc,
       "dot5TestFullDuplexLoopBack": dot5TestFullDuplexLoopBack,
       "dot5ChipSets": dot5ChipSets,
       "dot5ChipSetIBM16": dot5ChipSetIBM16,
       "dot5ChipSetTItms380": dot5ChipSetTItms380,
       "dot5ChipSetTItms380c16": dot5ChipSetTItms380c16,
       "dot5TimerTable": dot5TimerTable,
       "dot5TimerEntry": dot5TimerEntry,
       "dot5TimerIfIndex": dot5TimerIfIndex,
       "dot5TimerReturnRepeat": dot5TimerReturnRepeat,
       "dot5TimerHolding": dot5TimerHolding,
       "dot5TimerQueuePDU": dot5TimerQueuePDU,
       "dot5TimerValidTransmit": dot5TimerValidTransmit,
       "dot5TimerNoToken": dot5TimerNoToken,
       "dot5TimerActiveMon": dot5TimerActiveMon,
       "dot5TimerStandbyMon": dot5TimerStandbyMon,
       "dot5TimerErrorReport": dot5TimerErrorReport,
       "dot5TimerBeaconTransmit": dot5TimerBeaconTransmit,
       "dot5TimerBeaconReceive": dot5TimerBeaconReceive,
       "dot5Conformance": dot5Conformance,
       "dot5Groups": dot5Groups,
       "dot5StateGroup": dot5StateGroup,
       "dot5StatsGroup": dot5StatsGroup,
       "dot5Compliances": dot5Compliances,
       "dot5Compliance": dot5Compliance}
)
