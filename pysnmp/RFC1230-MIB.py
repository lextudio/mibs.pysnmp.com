# SNMP MIB module (RFC1230-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1230-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:11 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class OctetTime(Integer32):
    """Custom type OctetTime based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dot4_ObjectIdentity = ObjectIdentity
dot4 = _Dot4_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8)
)
_Dot4Table_Object = MibTable
dot4Table = _Dot4Table_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1)
)
if mibBuilder.loadTexts:
    dot4Table.setStatus("mandatory")
_Dot4Entry_Object = MibTableRow
dot4Entry = _Dot4Entry_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1)
)
dot4Entry.setIndexNames(
    (0, "RFC1230-MIB", "dot4IfIndex"),
)
if mibBuilder.loadTexts:
    dot4Entry.setStatus("mandatory")
_Dot4IfIndex_Type = Integer32
_Dot4IfIndex_Object = MibTableColumn
dot4IfIndex = _Dot4IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 1),
    _Dot4IfIndex_Type()
)
dot4IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4IfIndex.setStatus("mandatory")
_Dot4Options_Type = Integer32
_Dot4Options_Object = MibTableColumn
dot4Options = _Dot4Options_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 2),
    _Dot4Options_Type()
)
dot4Options.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4Options.setStatus("mandatory")


class _Dot4State_Type(Integer32):
    """Custom type dot4State based on Integer32"""
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
        *(("enteringRing", 4),
          ("inRing", 5),
          ("offline", 2),
          ("other", 1),
          ("outOfRing", 3))
    )


_Dot4State_Type.__name__ = "Integer32"
_Dot4State_Object = MibTableColumn
dot4State = _Dot4State_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 3),
    _Dot4State_Type()
)
dot4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4State.setStatus("mandatory")


class _Dot4Commands_Type(Integer32):
    """Custom type dot4Commands based on Integer32"""
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
        *(("enterRing", 2),
          ("exitRing", 3),
          ("initialize", 5),
          ("no-op", 1),
          ("reset", 4))
    )


_Dot4Commands_Type.__name__ = "Integer32"
_Dot4Commands_Object = MibTableColumn
dot4Commands = _Dot4Commands_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 4),
    _Dot4Commands_Type()
)
dot4Commands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4Commands.setStatus("mandatory")


class _Dot4MacAddrLen_Type(Integer32):
    """Custom type dot4MacAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forty-eightBit", 2),
          ("sixteenBit", 1))
    )


_Dot4MacAddrLen_Type.__name__ = "Integer32"
_Dot4MacAddrLen_Object = MibTableColumn
dot4MacAddrLen = _Dot4MacAddrLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 5),
    _Dot4MacAddrLen_Type()
)
dot4MacAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4MacAddrLen.setStatus("mandatory")
_Dot4NextStation_Type = MacAddress
_Dot4NextStation_Object = MibTableColumn
dot4NextStation = _Dot4NextStation_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 6),
    _Dot4NextStation_Type()
)
dot4NextStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4NextStation.setStatus("mandatory")
_Dot4PreviousStation_Type = MacAddress
_Dot4PreviousStation_Object = MibTableColumn
dot4PreviousStation = _Dot4PreviousStation_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 7),
    _Dot4PreviousStation_Type()
)
dot4PreviousStation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4PreviousStation.setStatus("mandatory")
_Dot4SlotTime_Type = OctetTime
_Dot4SlotTime_Object = MibTableColumn
dot4SlotTime = _Dot4SlotTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 8),
    _Dot4SlotTime_Type()
)
dot4SlotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4SlotTime.setStatus("mandatory")
_Dot4LastTokenRotTime_Type = OctetTime
_Dot4LastTokenRotTime_Object = MibTableColumn
dot4LastTokenRotTime = _Dot4LastTokenRotTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 9),
    _Dot4LastTokenRotTime_Type()
)
dot4LastTokenRotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4LastTokenRotTime.setStatus("mandatory")
_Dot4HiPriTokenHoldTime_Type = OctetTime
_Dot4HiPriTokenHoldTime_Object = MibTableColumn
dot4HiPriTokenHoldTime = _Dot4HiPriTokenHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 10),
    _Dot4HiPriTokenHoldTime_Type()
)
dot4HiPriTokenHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4HiPriTokenHoldTime.setStatus("mandatory")
_Dot4TargetRotTimeClass4_Type = OctetTime
_Dot4TargetRotTimeClass4_Object = MibTableColumn
dot4TargetRotTimeClass4 = _Dot4TargetRotTimeClass4_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 11),
    _Dot4TargetRotTimeClass4_Type()
)
dot4TargetRotTimeClass4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4TargetRotTimeClass4.setStatus("mandatory")
_Dot4TargetRotTimeClass2_Type = OctetTime
_Dot4TargetRotTimeClass2_Object = MibTableColumn
dot4TargetRotTimeClass2 = _Dot4TargetRotTimeClass2_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 12),
    _Dot4TargetRotTimeClass2_Type()
)
dot4TargetRotTimeClass2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4TargetRotTimeClass2.setStatus("mandatory")
_Dot4TargetRotTimeClass0_Type = OctetTime
_Dot4TargetRotTimeClass0_Object = MibTableColumn
dot4TargetRotTimeClass0 = _Dot4TargetRotTimeClass0_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 13),
    _Dot4TargetRotTimeClass0_Type()
)
dot4TargetRotTimeClass0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4TargetRotTimeClass0.setStatus("mandatory")
_Dot4TargetRotTimeRingMaint_Type = OctetTime
_Dot4TargetRotTimeRingMaint_Object = MibTableColumn
dot4TargetRotTimeRingMaint = _Dot4TargetRotTimeRingMaint_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 14),
    _Dot4TargetRotTimeRingMaint_Type()
)
dot4TargetRotTimeRingMaint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4TargetRotTimeRingMaint.setStatus("mandatory")
_Dot4RingMaintTimerInitValue_Type = OctetTime
_Dot4RingMaintTimerInitValue_Object = MibTableColumn
dot4RingMaintTimerInitValue = _Dot4RingMaintTimerInitValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 15),
    _Dot4RingMaintTimerInitValue_Type()
)
dot4RingMaintTimerInitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4RingMaintTimerInitValue.setStatus("mandatory")


class _Dot4MaxInterSolicitCount_Type(Integer32):
    """Custom type dot4MaxInterSolicitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Dot4MaxInterSolicitCount_Type.__name__ = "Integer32"
_Dot4MaxInterSolicitCount_Object = MibTableColumn
dot4MaxInterSolicitCount = _Dot4MaxInterSolicitCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 16),
    _Dot4MaxInterSolicitCount_Type()
)
dot4MaxInterSolicitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4MaxInterSolicitCount.setStatus("mandatory")


class _Dot4MaxRetries_Type(Integer32):
    """Custom type dot4MaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot4MaxRetries_Type.__name__ = "Integer32"
_Dot4MaxRetries_Object = MibTableColumn
dot4MaxRetries = _Dot4MaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 17),
    _Dot4MaxRetries_Type()
)
dot4MaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4MaxRetries.setStatus("mandatory")
_Dot4MinPostSilencePreambLen_Type = Integer32
_Dot4MinPostSilencePreambLen_Object = MibTableColumn
dot4MinPostSilencePreambLen = _Dot4MinPostSilencePreambLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 18),
    _Dot4MinPostSilencePreambLen_Type()
)
dot4MinPostSilencePreambLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4MinPostSilencePreambLen.setStatus("mandatory")


class _Dot4StandardRevision_Type(Integer32):
    """Custom type dot4StandardRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("rev2", 2)
    )


_Dot4StandardRevision_Type.__name__ = "Integer32"
_Dot4StandardRevision_Object = MibTableColumn
dot4StandardRevision = _Dot4StandardRevision_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 1, 1, 19),
    _Dot4StandardRevision_Type()
)
dot4StandardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StandardRevision.setStatus("mandatory")
_Dot4InitTable_Object = MibTable
dot4InitTable = _Dot4InitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2)
)
if mibBuilder.loadTexts:
    dot4InitTable.setStatus("mandatory")
_Dot4InitEntry_Object = MibTableRow
dot4InitEntry = _Dot4InitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1)
)
dot4InitEntry.setIndexNames(
    (0, "RFC1230-MIB", "dot4InitIfIndex"),
)
if mibBuilder.loadTexts:
    dot4InitEntry.setStatus("mandatory")
_Dot4InitIfIndex_Type = Integer32
_Dot4InitIfIndex_Object = MibTableColumn
dot4InitIfIndex = _Dot4InitIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 1),
    _Dot4InitIfIndex_Type()
)
dot4InitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4InitIfIndex.setStatus("mandatory")
_Dot4InitSlotTime_Type = OctetTime
_Dot4InitSlotTime_Object = MibTableColumn
dot4InitSlotTime = _Dot4InitSlotTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 2),
    _Dot4InitSlotTime_Type()
)
dot4InitSlotTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitSlotTime.setStatus("mandatory")


class _Dot4InitMaxInterSolicitCount_Type(Integer32):
    """Custom type dot4InitMaxInterSolicitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 255),
    )


_Dot4InitMaxInterSolicitCount_Type.__name__ = "Integer32"
_Dot4InitMaxInterSolicitCount_Object = MibTableColumn
dot4InitMaxInterSolicitCount = _Dot4InitMaxInterSolicitCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 3),
    _Dot4InitMaxInterSolicitCount_Type()
)
dot4InitMaxInterSolicitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitMaxInterSolicitCount.setStatus("mandatory")


class _Dot4InitMaxRetries_Type(Integer32):
    """Custom type dot4InitMaxRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dot4InitMaxRetries_Type.__name__ = "Integer32"
_Dot4InitMaxRetries_Object = MibTableColumn
dot4InitMaxRetries = _Dot4InitMaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 4),
    _Dot4InitMaxRetries_Type()
)
dot4InitMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitMaxRetries.setStatus("mandatory")
_Dot4InitHiPriTokenHoldTime_Type = OctetTime
_Dot4InitHiPriTokenHoldTime_Object = MibTableColumn
dot4InitHiPriTokenHoldTime = _Dot4InitHiPriTokenHoldTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 5),
    _Dot4InitHiPriTokenHoldTime_Type()
)
dot4InitHiPriTokenHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitHiPriTokenHoldTime.setStatus("mandatory")
_Dot4InitTargetRotTimeClass4_Type = OctetTime
_Dot4InitTargetRotTimeClass4_Object = MibTableColumn
dot4InitTargetRotTimeClass4 = _Dot4InitTargetRotTimeClass4_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 6),
    _Dot4InitTargetRotTimeClass4_Type()
)
dot4InitTargetRotTimeClass4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitTargetRotTimeClass4.setStatus("mandatory")
_Dot4InitTargetRotTimeClass2_Type = OctetTime
_Dot4InitTargetRotTimeClass2_Object = MibTableColumn
dot4InitTargetRotTimeClass2 = _Dot4InitTargetRotTimeClass2_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 7),
    _Dot4InitTargetRotTimeClass2_Type()
)
dot4InitTargetRotTimeClass2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitTargetRotTimeClass2.setStatus("mandatory")
_Dot4InitTargetRotTimeClass0_Type = OctetTime
_Dot4InitTargetRotTimeClass0_Object = MibTableColumn
dot4InitTargetRotTimeClass0 = _Dot4InitTargetRotTimeClass0_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 8),
    _Dot4InitTargetRotTimeClass0_Type()
)
dot4InitTargetRotTimeClass0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitTargetRotTimeClass0.setStatus("mandatory")
_Dot4InitTargetRotTimeRingMaint_Type = OctetTime
_Dot4InitTargetRotTimeRingMaint_Object = MibTableColumn
dot4InitTargetRotTimeRingMaint = _Dot4InitTargetRotTimeRingMaint_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 9),
    _Dot4InitTargetRotTimeRingMaint_Type()
)
dot4InitTargetRotTimeRingMaint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitTargetRotTimeRingMaint.setStatus("mandatory")
_Dot4InitRingMaintTimerInitValue_Type = OctetTime
_Dot4InitRingMaintTimerInitValue_Object = MibTableColumn
dot4InitRingMaintTimerInitValue = _Dot4InitRingMaintTimerInitValue_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 10),
    _Dot4InitRingMaintTimerInitValue_Type()
)
dot4InitRingMaintTimerInitValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitRingMaintTimerInitValue.setStatus("mandatory")
_Dot4InitMinPostSilencePreambLen_Type = Integer32
_Dot4InitMinPostSilencePreambLen_Object = MibTableColumn
dot4InitMinPostSilencePreambLen = _Dot4InitMinPostSilencePreambLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 11),
    _Dot4InitMinPostSilencePreambLen_Type()
)
dot4InitMinPostSilencePreambLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitMinPostSilencePreambLen.setStatus("mandatory")


class _Dot4InitInRingDesired_Type(Integer32):
    """Custom type dot4InitInRingDesired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inRing", 1),
          ("outOfRing", 2))
    )


_Dot4InitInRingDesired_Type.__name__ = "Integer32"
_Dot4InitInRingDesired_Object = MibTableColumn
dot4InitInRingDesired = _Dot4InitInRingDesired_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 2, 1, 12),
    _Dot4InitInRingDesired_Type()
)
dot4InitInRingDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot4InitInRingDesired.setStatus("mandatory")
_Dot4StatsTable_Object = MibTable
dot4StatsTable = _Dot4StatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3)
)
if mibBuilder.loadTexts:
    dot4StatsTable.setStatus("mandatory")
_Dot4StatsEntry_Object = MibTableRow
dot4StatsEntry = _Dot4StatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1)
)
dot4StatsEntry.setIndexNames(
    (0, "RFC1230-MIB", "dot4StatsIfIndex"),
)
if mibBuilder.loadTexts:
    dot4StatsEntry.setStatus("mandatory")
_Dot4StatsIfIndex_Type = Integer32
_Dot4StatsIfIndex_Object = MibTableColumn
dot4StatsIfIndex = _Dot4StatsIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 1),
    _Dot4StatsIfIndex_Type()
)
dot4StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsIfIndex.setStatus("mandatory")
_Dot4StatsTokenPasses_Type = Counter32
_Dot4StatsTokenPasses_Object = MibTableColumn
dot4StatsTokenPasses = _Dot4StatsTokenPasses_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 2),
    _Dot4StatsTokenPasses_Type()
)
dot4StatsTokenPasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsTokenPasses.setStatus("optional")
_Dot4StatsTokenHeards_Type = Counter32
_Dot4StatsTokenHeards_Object = MibTableColumn
dot4StatsTokenHeards = _Dot4StatsTokenHeards_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 3),
    _Dot4StatsTokenHeards_Type()
)
dot4StatsTokenHeards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsTokenHeards.setStatus("optional")
_Dot4StatsNoSuccessors_Type = Counter32
_Dot4StatsNoSuccessors_Object = MibTableColumn
dot4StatsNoSuccessors = _Dot4StatsNoSuccessors_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 4),
    _Dot4StatsNoSuccessors_Type()
)
dot4StatsNoSuccessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsNoSuccessors.setStatus("mandatory")
_Dot4StatsWhoFollows_Type = Counter32
_Dot4StatsWhoFollows_Object = MibTableColumn
dot4StatsWhoFollows = _Dot4StatsWhoFollows_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 5),
    _Dot4StatsWhoFollows_Type()
)
dot4StatsWhoFollows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsWhoFollows.setStatus("mandatory")
_Dot4StatsTokenPassFails_Type = Counter32
_Dot4StatsTokenPassFails_Object = MibTableColumn
dot4StatsTokenPassFails = _Dot4StatsTokenPassFails_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 6),
    _Dot4StatsTokenPassFails_Type()
)
dot4StatsTokenPassFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsTokenPassFails.setStatus("mandatory")
_Dot4StatsNonSilences_Type = Counter32
_Dot4StatsNonSilences_Object = MibTableColumn
dot4StatsNonSilences = _Dot4StatsNonSilences_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 7),
    _Dot4StatsNonSilences_Type()
)
dot4StatsNonSilences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsNonSilences.setStatus("mandatory")
_Dot4StatsFcsErrors_Type = Counter32
_Dot4StatsFcsErrors_Object = MibTableColumn
dot4StatsFcsErrors = _Dot4StatsFcsErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 8),
    _Dot4StatsFcsErrors_Type()
)
dot4StatsFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsFcsErrors.setStatus("mandatory")
_Dot4StatsEbitErrors_Type = Counter32
_Dot4StatsEbitErrors_Object = MibTableColumn
dot4StatsEbitErrors = _Dot4StatsEbitErrors_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 9),
    _Dot4StatsEbitErrors_Type()
)
dot4StatsEbitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsEbitErrors.setStatus("mandatory")
_Dot4StatsFrameFrags_Type = Counter32
_Dot4StatsFrameFrags_Object = MibTableColumn
dot4StatsFrameFrags = _Dot4StatsFrameFrags_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 10),
    _Dot4StatsFrameFrags_Type()
)
dot4StatsFrameFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsFrameFrags.setStatus("mandatory")
_Dot4StatsFrameTooLongs_Type = Counter32
_Dot4StatsFrameTooLongs_Object = MibTableColumn
dot4StatsFrameTooLongs = _Dot4StatsFrameTooLongs_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 11),
    _Dot4StatsFrameTooLongs_Type()
)
dot4StatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsFrameTooLongs.setStatus("mandatory")
_Dot4StatsOverRuns_Type = Counter32
_Dot4StatsOverRuns_Object = MibTableColumn
dot4StatsOverRuns = _Dot4StatsOverRuns_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 12),
    _Dot4StatsOverRuns_Type()
)
dot4StatsOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsOverRuns.setStatus("mandatory")
_Dot4StatsDupAddresses_Type = Counter32
_Dot4StatsDupAddresses_Object = MibTableColumn
dot4StatsDupAddresses = _Dot4StatsDupAddresses_Object(
    (1, 3, 6, 1, 2, 1, 10, 8, 3, 1, 13),
    _Dot4StatsDupAddresses_Type()
)
dot4StatsDupAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot4StatsDupAddresses.setStatus("mandatory")
_Dot4Errors_ObjectIdentity = ObjectIdentity
dot4Errors = _Dot4Errors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 4)
)
_Dot4ModemInitFailed_ObjectIdentity = ObjectIdentity
dot4ModemInitFailed = _Dot4ModemInitFailed_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 4, 1)
)
_Dot4Tests_ObjectIdentity = ObjectIdentity
dot4Tests = _Dot4Tests_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 5)
)
_TestFifoPath_ObjectIdentity = ObjectIdentity
testFifoPath = _TestFifoPath_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 5, 1)
)
_TestExternalLoopback_ObjectIdentity = ObjectIdentity
testExternalLoopback = _TestExternalLoopback_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 5, 2)
)
_Dot4ChipSets_ObjectIdentity = ObjectIdentity
dot4ChipSets = _Dot4ChipSets_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 6)
)
_ChipSetMc68824_ObjectIdentity = ObjectIdentity
chipSetMc68824 = _ChipSetMc68824_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 8, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1230-MIB",
    **{"MacAddress": MacAddress,
       "OctetTime": OctetTime,
       "dot4": dot4,
       "dot4Table": dot4Table,
       "dot4Entry": dot4Entry,
       "dot4IfIndex": dot4IfIndex,
       "dot4Options": dot4Options,
       "dot4State": dot4State,
       "dot4Commands": dot4Commands,
       "dot4MacAddrLen": dot4MacAddrLen,
       "dot4NextStation": dot4NextStation,
       "dot4PreviousStation": dot4PreviousStation,
       "dot4SlotTime": dot4SlotTime,
       "dot4LastTokenRotTime": dot4LastTokenRotTime,
       "dot4HiPriTokenHoldTime": dot4HiPriTokenHoldTime,
       "dot4TargetRotTimeClass4": dot4TargetRotTimeClass4,
       "dot4TargetRotTimeClass2": dot4TargetRotTimeClass2,
       "dot4TargetRotTimeClass0": dot4TargetRotTimeClass0,
       "dot4TargetRotTimeRingMaint": dot4TargetRotTimeRingMaint,
       "dot4RingMaintTimerInitValue": dot4RingMaintTimerInitValue,
       "dot4MaxInterSolicitCount": dot4MaxInterSolicitCount,
       "dot4MaxRetries": dot4MaxRetries,
       "dot4MinPostSilencePreambLen": dot4MinPostSilencePreambLen,
       "dot4StandardRevision": dot4StandardRevision,
       "dot4InitTable": dot4InitTable,
       "dot4InitEntry": dot4InitEntry,
       "dot4InitIfIndex": dot4InitIfIndex,
       "dot4InitSlotTime": dot4InitSlotTime,
       "dot4InitMaxInterSolicitCount": dot4InitMaxInterSolicitCount,
       "dot4InitMaxRetries": dot4InitMaxRetries,
       "dot4InitHiPriTokenHoldTime": dot4InitHiPriTokenHoldTime,
       "dot4InitTargetRotTimeClass4": dot4InitTargetRotTimeClass4,
       "dot4InitTargetRotTimeClass2": dot4InitTargetRotTimeClass2,
       "dot4InitTargetRotTimeClass0": dot4InitTargetRotTimeClass0,
       "dot4InitTargetRotTimeRingMaint": dot4InitTargetRotTimeRingMaint,
       "dot4InitRingMaintTimerInitValue": dot4InitRingMaintTimerInitValue,
       "dot4InitMinPostSilencePreambLen": dot4InitMinPostSilencePreambLen,
       "dot4InitInRingDesired": dot4InitInRingDesired,
       "dot4StatsTable": dot4StatsTable,
       "dot4StatsEntry": dot4StatsEntry,
       "dot4StatsIfIndex": dot4StatsIfIndex,
       "dot4StatsTokenPasses": dot4StatsTokenPasses,
       "dot4StatsTokenHeards": dot4StatsTokenHeards,
       "dot4StatsNoSuccessors": dot4StatsNoSuccessors,
       "dot4StatsWhoFollows": dot4StatsWhoFollows,
       "dot4StatsTokenPassFails": dot4StatsTokenPassFails,
       "dot4StatsNonSilences": dot4StatsNonSilences,
       "dot4StatsFcsErrors": dot4StatsFcsErrors,
       "dot4StatsEbitErrors": dot4StatsEbitErrors,
       "dot4StatsFrameFrags": dot4StatsFrameFrags,
       "dot4StatsFrameTooLongs": dot4StatsFrameTooLongs,
       "dot4StatsOverRuns": dot4StatsOverRuns,
       "dot4StatsDupAddresses": dot4StatsDupAddresses,
       "dot4Errors": dot4Errors,
       "dot4ModemInitFailed": dot4ModemInitFailed,
       "dot4Tests": dot4Tests,
       "testFifoPath": testFifoPath,
       "testExternalLoopback": testExternalLoopback,
       "dot4ChipSets": dot4ChipSets,
       "chipSetMc68824": chipSetMc68824}
)
