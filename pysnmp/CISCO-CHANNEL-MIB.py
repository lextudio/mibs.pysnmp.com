# SNMP MIB module (CISCO-CHANNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CHANNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:24 2024
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

channel = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20)
)
channel.setRevisions(
        ("1998-01-06 00:00",
         "1998-08-14 00:00",
         "1997-03-26 00:00",
         "1996-06-13 00:00",
         "1995-09-25 00:00",
         "1994-11-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CipCard_ObjectIdentity = ObjectIdentity
cipCard = _CipCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1)
)
_CipCardTable_Object = MibTable
cipCardTable = _CipCardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1)
)
if mibBuilder.loadTexts:
    cipCardTable.setStatus("current")
_CipCardEntry_Object = MibTableRow
cipCardEntry = _CipCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1)
)
cipCardEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
)
if mibBuilder.loadTexts:
    cipCardEntry.setStatus("current")


class _CipCardEntryIndex_Type(Integer32):
    """Custom type cipCardEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipCardEntryIndex_Type.__name__ = "Integer32"
_CipCardEntryIndex_Object = MibTableColumn
cipCardEntryIndex = _CipCardEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 1),
    _CipCardEntryIndex_Type()
)
cipCardEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardEntryIndex.setStatus("current")


class _CipCardEntryName_Type(DisplayString):
    """Custom type cipCardEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CipCardEntryName_Type.__name__ = "DisplayString"
_CipCardEntryName_Object = MibTableColumn
cipCardEntryName = _CipCardEntryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 2),
    _CipCardEntryName_Type()
)
cipCardEntryName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cipCardEntryName.setStatus("current")
_CipCardEntryTotalMemory_Type = Integer32
_CipCardEntryTotalMemory_Object = MibTableColumn
cipCardEntryTotalMemory = _CipCardEntryTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 3),
    _CipCardEntryTotalMemory_Type()
)
cipCardEntryTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryTotalMemory.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryTotalMemory.setUnits("kilo bytes")
_CipCardEntryFreeMemory_Type = Integer32
_CipCardEntryFreeMemory_Object = MibTableColumn
cipCardEntryFreeMemory = _CipCardEntryFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 4),
    _CipCardEntryFreeMemory_Type()
)
cipCardEntryFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryFreeMemory.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryFreeMemory.setUnits("kilo bytes")


class _CipCardEntryCpuUtilization_Type(Integer32):
    """Custom type cipCardEntryCpuUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryCpuUtilization_Type.__name__ = "Integer32"
_CipCardEntryCpuUtilization_Object = MibTableColumn
cipCardEntryCpuUtilization = _CipCardEntryCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 5),
    _CipCardEntryCpuUtilization_Type()
)
cipCardEntryCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryCpuUtilization.setStatus("current")
_CipCardEntryTimeSinceLastReset_Type = Counter32
_CipCardEntryTimeSinceLastReset_Object = MibTableColumn
cipCardEntryTimeSinceLastReset = _CipCardEntryTimeSinceLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 6),
    _CipCardEntryTimeSinceLastReset_Type()
)
cipCardEntryTimeSinceLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryTimeSinceLastReset.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryTimeSinceLastReset.setUnits("seconds")
_CipCardEntryMajorSwRevisionNr_Type = Integer32
_CipCardEntryMajorSwRevisionNr_Object = MibTableColumn
cipCardEntryMajorSwRevisionNr = _CipCardEntryMajorSwRevisionNr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 7),
    _CipCardEntryMajorSwRevisionNr_Type()
)
cipCardEntryMajorSwRevisionNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryMajorSwRevisionNr.setStatus("current")
_CipCardEntryMinorSwRevisionNr_Type = Integer32
_CipCardEntryMinorSwRevisionNr_Object = MibTableColumn
cipCardEntryMinorSwRevisionNr = _CipCardEntryMinorSwRevisionNr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 8),
    _CipCardEntryMinorSwRevisionNr_Type()
)
cipCardEntryMinorSwRevisionNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryMinorSwRevisionNr.setStatus("current")
_CipCardEntryMajorHwRevisionNr_Type = Integer32
_CipCardEntryMajorHwRevisionNr_Object = MibTableColumn
cipCardEntryMajorHwRevisionNr = _CipCardEntryMajorHwRevisionNr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 9),
    _CipCardEntryMajorHwRevisionNr_Type()
)
cipCardEntryMajorHwRevisionNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryMajorHwRevisionNr.setStatus("current")
_CipCardEntryMinorHwRevisionNr_Type = Integer32
_CipCardEntryMinorHwRevisionNr_Object = MibTableColumn
cipCardEntryMinorHwRevisionNr = _CipCardEntryMinorHwRevisionNr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 10),
    _CipCardEntryMinorHwRevisionNr_Type()
)
cipCardEntryMinorHwRevisionNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryMinorHwRevisionNr.setStatus("current")


class _CipCardEntryCpuLoad1m_Type(Integer32):
    """Custom type cipCardEntryCpuLoad1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryCpuLoad1m_Type.__name__ = "Integer32"
_CipCardEntryCpuLoad1m_Object = MibTableColumn
cipCardEntryCpuLoad1m = _CipCardEntryCpuLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 11),
    _CipCardEntryCpuLoad1m_Type()
)
cipCardEntryCpuLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad1m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad1m.setUnits("percent")


class _CipCardEntryCpuLoad5m_Type(Integer32):
    """Custom type cipCardEntryCpuLoad5m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryCpuLoad5m_Type.__name__ = "Integer32"
_CipCardEntryCpuLoad5m_Object = MibTableColumn
cipCardEntryCpuLoad5m = _CipCardEntryCpuLoad5m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 12),
    _CipCardEntryCpuLoad5m_Type()
)
cipCardEntryCpuLoad5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad5m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad5m.setUnits("percent")


class _CipCardEntryCpuLoad60m_Type(Integer32):
    """Custom type cipCardEntryCpuLoad60m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryCpuLoad60m_Type.__name__ = "Integer32"
_CipCardEntryCpuLoad60m_Object = MibTableColumn
cipCardEntryCpuLoad60m = _CipCardEntryCpuLoad60m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 13),
    _CipCardEntryCpuLoad60m_Type()
)
cipCardEntryCpuLoad60m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad60m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryCpuLoad60m.setUnits("percent")


class _CipCardEntryDmaLoad1m_Type(Integer32):
    """Custom type cipCardEntryDmaLoad1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryDmaLoad1m_Type.__name__ = "Integer32"
_CipCardEntryDmaLoad1m_Object = MibTableColumn
cipCardEntryDmaLoad1m = _CipCardEntryDmaLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 14),
    _CipCardEntryDmaLoad1m_Type()
)
cipCardEntryDmaLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad1m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad1m.setUnits("percent")


class _CipCardEntryDmaLoad5m_Type(Integer32):
    """Custom type cipCardEntryDmaLoad5m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryDmaLoad5m_Type.__name__ = "Integer32"
_CipCardEntryDmaLoad5m_Object = MibTableColumn
cipCardEntryDmaLoad5m = _CipCardEntryDmaLoad5m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 15),
    _CipCardEntryDmaLoad5m_Type()
)
cipCardEntryDmaLoad5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad5m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad5m.setUnits("percent")


class _CipCardEntryDmaLoad60m_Type(Integer32):
    """Custom type cipCardEntryDmaLoad60m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardEntryDmaLoad60m_Type.__name__ = "Integer32"
_CipCardEntryDmaLoad60m_Object = MibTableColumn
cipCardEntryDmaLoad60m = _CipCardEntryDmaLoad60m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 1, 1, 16),
    _CipCardEntryDmaLoad60m_Type()
)
cipCardEntryDmaLoad60m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad60m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardEntryDmaLoad60m.setUnits("percent")
_CipCardDaughterBoardTable_Object = MibTable
cipCardDaughterBoardTable = _CipCardDaughterBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2)
)
if mibBuilder.loadTexts:
    cipCardDaughterBoardTable.setStatus("current")
_CipCardDaughterBoardEntry_Object = MibTableRow
cipCardDaughterBoardEntry = _CipCardDaughterBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1)
)
cipCardDaughterBoardEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
)
if mibBuilder.loadTexts:
    cipCardDaughterBoardEntry.setStatus("current")


class _CipCardDtrBrdIndex_Type(Integer32):
    """Custom type cipCardDtrBrdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipCardDtrBrdIndex_Type.__name__ = "Integer32"
_CipCardDtrBrdIndex_Object = MibTableColumn
cipCardDtrBrdIndex = _CipCardDtrBrdIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 1),
    _CipCardDtrBrdIndex_Type()
)
cipCardDtrBrdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardDtrBrdIndex.setStatus("current")


class _CipCardDtrBrdType_Type(Integer32):
    """Custom type cipCardDtrBrdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busAndTag", 2),
          ("escon", 1))
    )


_CipCardDtrBrdType_Type.__name__ = "Integer32"
_CipCardDtrBrdType_Object = MibTableColumn
cipCardDtrBrdType = _CipCardDtrBrdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 2),
    _CipCardDtrBrdType_Type()
)
cipCardDtrBrdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdType.setStatus("current")
_CipCardDtrBrdStatus_Type = TruthValue
_CipCardDtrBrdStatus_Object = MibTableColumn
cipCardDtrBrdStatus = _CipCardDtrBrdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 3),
    _CipCardDtrBrdStatus_Type()
)
cipCardDtrBrdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdStatus.setStatus("current")
_CipCardDtrBrdSignal_Type = TruthValue
_CipCardDtrBrdSignal_Object = MibTableColumn
cipCardDtrBrdSignal = _CipCardDtrBrdSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 4),
    _CipCardDtrBrdSignal_Type()
)
cipCardDtrBrdSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdSignal.setStatus("current")
_CipCardDtrBrdOnline_Type = TruthValue
_CipCardDtrBrdOnline_Object = MibTableColumn
cipCardDtrBrdOnline = _CipCardDtrBrdOnline_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 5),
    _CipCardDtrBrdOnline_Type()
)
cipCardDtrBrdOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdOnline.setStatus("current")
_ImplicitIncidents_Type = Counter32
_ImplicitIncidents_Object = MibTableColumn
implicitIncidents = _ImplicitIncidents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 6),
    _ImplicitIncidents_Type()
)
implicitIncidents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    implicitIncidents.setStatus("current")
_CodeViolationErrors_Type = Counter32
_CodeViolationErrors_Object = MibTableColumn
codeViolationErrors = _CodeViolationErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 7),
    _CodeViolationErrors_Type()
)
codeViolationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    codeViolationErrors.setStatus("current")
_LinkFailureSignalOrSyncLoss_Type = Counter32
_LinkFailureSignalOrSyncLoss_Object = MibTableColumn
linkFailureSignalOrSyncLoss = _LinkFailureSignalOrSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 8),
    _LinkFailureSignalOrSyncLoss_Type()
)
linkFailureSignalOrSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFailureSignalOrSyncLoss.setStatus("current")
_LinkFailureNOSs_Type = Counter32
_LinkFailureNOSs_Object = MibTableColumn
linkFailureNOSs = _LinkFailureNOSs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 9),
    _LinkFailureNOSs_Type()
)
linkFailureNOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFailureNOSs.setStatus("current")
_LinkFailureSequenceTimeouts_Type = Counter32
_LinkFailureSequenceTimeouts_Object = MibTableColumn
linkFailureSequenceTimeouts = _LinkFailureSequenceTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 10),
    _LinkFailureSequenceTimeouts_Type()
)
linkFailureSequenceTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFailureSequenceTimeouts.setStatus("current")
_LinkFailureInvalidSequences_Type = Counter32
_LinkFailureInvalidSequences_Object = MibTableColumn
linkFailureInvalidSequences = _LinkFailureInvalidSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 11),
    _LinkFailureInvalidSequences_Type()
)
linkFailureInvalidSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkFailureInvalidSequences.setStatus("current")


class _LinkIncidentTrapCause_Type(Integer32):
    """Custom type linkIncidentTrapCause based on Integer32"""
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
        *(("liBERthreshold", 4),
          ("liImplicitIncidents", 3),
          ("liInvalidSequences", 8),
          ("liNotOperationalSequence", 6),
          ("liOther", 1),
          ("liSequenceTimeouts", 7),
          ("liSignalOrSyncLoss", 5),
          ("liStatus", 2))
    )


_LinkIncidentTrapCause_Type.__name__ = "Integer32"
_LinkIncidentTrapCause_Object = MibTableColumn
linkIncidentTrapCause = _LinkIncidentTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 12),
    _LinkIncidentTrapCause_Type()
)
linkIncidentTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkIncidentTrapCause.setStatus("current")
_CipCardDtrBrdLastStat_Type = TimeTicks
_CipCardDtrBrdLastStat_Object = MibTableColumn
cipCardDtrBrdLastStat = _CipCardDtrBrdLastStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 13),
    _CipCardDtrBrdLastStat_Type()
)
cipCardDtrBrdLastStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdLastStat.setStatus("current")
_CipCardDtrBrdNextStat_Type = TimeTicks
_CipCardDtrBrdNextStat_Object = MibTableColumn
cipCardDtrBrdNextStat = _CipCardDtrBrdNextStat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 14),
    _CipCardDtrBrdNextStat_Type()
)
cipCardDtrBrdNextStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdNextStat.setStatus("current")


class _CipCardDtrBrdChannelLoad1m_Type(Integer32):
    """Custom type cipCardDtrBrdChannelLoad1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardDtrBrdChannelLoad1m_Type.__name__ = "Integer32"
_CipCardDtrBrdChannelLoad1m_Object = MibTableColumn
cipCardDtrBrdChannelLoad1m = _CipCardDtrBrdChannelLoad1m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 15),
    _CipCardDtrBrdChannelLoad1m_Type()
)
cipCardDtrBrdChannelLoad1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad1m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad1m.setUnits("percent")


class _CipCardDtrBrdChannelLoad5m_Type(Integer32):
    """Custom type cipCardDtrBrdChannelLoad5m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardDtrBrdChannelLoad5m_Type.__name__ = "Integer32"
_CipCardDtrBrdChannelLoad5m_Object = MibTableColumn
cipCardDtrBrdChannelLoad5m = _CipCardDtrBrdChannelLoad5m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 16),
    _CipCardDtrBrdChannelLoad5m_Type()
)
cipCardDtrBrdChannelLoad5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad5m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad5m.setUnits("percent")


class _CipCardDtrBrdChannelLoad60m_Type(Integer32):
    """Custom type cipCardDtrBrdChannelLoad60m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CipCardDtrBrdChannelLoad60m_Type.__name__ = "Integer32"
_CipCardDtrBrdChannelLoad60m_Object = MibTableColumn
cipCardDtrBrdChannelLoad60m = _CipCardDtrBrdChannelLoad60m_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 2, 1, 17),
    _CipCardDtrBrdChannelLoad60m_Type()
)
cipCardDtrBrdChannelLoad60m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad60m.setStatus("current")
if mibBuilder.loadTexts:
    cipCardDtrBrdChannelLoad60m.setUnits("percent")
_CipCardSubChannelTable_Object = MibTable
cipCardSubChannelTable = _CipCardSubChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3)
)
if mibBuilder.loadTexts:
    cipCardSubChannelTable.setStatus("current")
_CipCardSubChannelEntry_Object = MibTableRow
cipCardSubChannelEntry = _CipCardSubChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1)
)
cipCardSubChannelEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardSubChannelEntry.setStatus("current")


class _CipCardSubChannelIndex_Type(Integer32):
    """Custom type cipCardSubChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipCardSubChannelIndex_Type.__name__ = "Integer32"
_CipCardSubChannelIndex_Object = MibTableColumn
cipCardSubChannelIndex = _CipCardSubChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 1),
    _CipCardSubChannelIndex_Type()
)
cipCardSubChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelIndex.setStatus("current")
_CipCardSubChannelConnections_Type = Counter32
_CipCardSubChannelConnections_Object = MibTableColumn
cipCardSubChannelConnections = _CipCardSubChannelConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 2),
    _CipCardSubChannelConnections_Type()
)
cipCardSubChannelConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelConnections.setStatus("current")
_CipCardSubChannelCancels_Type = Counter32
_CipCardSubChannelCancels_Object = MibTableColumn
cipCardSubChannelCancels = _CipCardSubChannelCancels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 3),
    _CipCardSubChannelCancels_Type()
)
cipCardSubChannelCancels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelCancels.setStatus("current")
_CipCardSubChannelSelectiveResets_Type = Counter32
_CipCardSubChannelSelectiveResets_Object = MibTableColumn
cipCardSubChannelSelectiveResets = _CipCardSubChannelSelectiveResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 4),
    _CipCardSubChannelSelectiveResets_Type()
)
cipCardSubChannelSelectiveResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelSelectiveResets.setStatus("current")
_CipCardSubChannelSystemResets_Type = Counter32
_CipCardSubChannelSystemResets_Object = MibTableColumn
cipCardSubChannelSystemResets = _CipCardSubChannelSystemResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 5),
    _CipCardSubChannelSystemResets_Type()
)
cipCardSubChannelSystemResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelSystemResets.setStatus("current")
_CipCardSubChannelDeviceErrors_Type = Counter32
_CipCardSubChannelDeviceErrors_Object = MibTableColumn
cipCardSubChannelDeviceErrors = _CipCardSubChannelDeviceErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 6),
    _CipCardSubChannelDeviceErrors_Type()
)
cipCardSubChannelDeviceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelDeviceErrors.setStatus("current")
_CipCardSubChannelWriteBlocksDropped_Type = Counter32
_CipCardSubChannelWriteBlocksDropped_Object = MibTableColumn
cipCardSubChannelWriteBlocksDropped = _CipCardSubChannelWriteBlocksDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 7),
    _CipCardSubChannelWriteBlocksDropped_Type()
)
cipCardSubChannelWriteBlocksDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelWriteBlocksDropped.setStatus("current")


class _CipCardSubChannelLastSenseData_Type(OctetString):
    """Custom type cipCardSubChannelLastSenseData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CipCardSubChannelLastSenseData_Type.__name__ = "OctetString"
_CipCardSubChannelLastSenseData_Object = MibTableColumn
cipCardSubChannelLastSenseData = _CipCardSubChannelLastSenseData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 8),
    _CipCardSubChannelLastSenseData_Type()
)
cipCardSubChannelLastSenseData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelLastSenseData.setStatus("current")
_CipCardSubChannelLastSenseDataTime_Type = TimeStamp
_CipCardSubChannelLastSenseDataTime_Object = MibTableColumn
cipCardSubChannelLastSenseDataTime = _CipCardSubChannelLastSenseDataTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 9),
    _CipCardSubChannelLastSenseDataTime_Type()
)
cipCardSubChannelLastSenseDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelLastSenseDataTime.setStatus("current")
_CipCardSubChannelCuBusies_Type = Counter32
_CipCardSubChannelCuBusies_Object = MibTableColumn
cipCardSubChannelCuBusies = _CipCardSubChannelCuBusies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 10),
    _CipCardSubChannelCuBusies_Type()
)
cipCardSubChannelCuBusies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelCuBusies.setStatus("current")
_CipCardSubChannelCmdRetries_Type = Counter32
_CipCardSubChannelCmdRetries_Object = MibTableColumn
cipCardSubChannelCmdRetries = _CipCardSubChannelCmdRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 11),
    _CipCardSubChannelCmdRetries_Type()
)
cipCardSubChannelCmdRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelCmdRetries.setStatus("current")
_CipCardSubChannelResetEvent_Type = TruthValue
_CipCardSubChannelResetEvent_Object = MibTableColumn
cipCardSubChannelResetEvent = _CipCardSubChannelResetEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 12),
    _CipCardSubChannelResetEvent_Type()
)
cipCardSubChannelResetEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelResetEvent.setStatus("current")
_CipCardSubChannelShortBusy_Type = TruthValue
_CipCardSubChannelShortBusy_Object = MibTableColumn
cipCardSubChannelShortBusy = _CipCardSubChannelShortBusy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 13),
    _CipCardSubChannelShortBusy_Type()
)
cipCardSubChannelShortBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelShortBusy.setStatus("current")
_CipCardSubChannelCMDRetry_Type = TruthValue
_CipCardSubChannelCMDRetry_Object = MibTableColumn
cipCardSubChannelCMDRetry = _CipCardSubChannelCMDRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 14),
    _CipCardSubChannelCMDRetry_Type()
)
cipCardSubChannelCMDRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelCMDRetry.setStatus("current")
_CipCardSubChannelBufferWait_Type = TruthValue
_CipCardSubChannelBufferWait_Object = MibTableColumn
cipCardSubChannelBufferWait = _CipCardSubChannelBufferWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 15),
    _CipCardSubChannelBufferWait_Type()
)
cipCardSubChannelBufferWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelBufferWait.setStatus("current")
_CipCardSubChannelStatPending_Type = TruthValue
_CipCardSubChannelStatPending_Object = MibTableColumn
cipCardSubChannelStatPending = _CipCardSubChannelStatPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 16),
    _CipCardSubChannelStatPending_Type()
)
cipCardSubChannelStatPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelStatPending.setStatus("current")
_CipCardSubChannelSuspend_Type = TruthValue
_CipCardSubChannelSuspend_Object = MibTableColumn
cipCardSubChannelSuspend = _CipCardSubChannelSuspend_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 17),
    _CipCardSubChannelSuspend_Type()
)
cipCardSubChannelSuspend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelSuspend.setStatus("current")
_CipCardSubChannelFBLWait_Type = TruthValue
_CipCardSubChannelFBLWait_Object = MibTableColumn
cipCardSubChannelFBLWait = _CipCardSubChannelFBLWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 3, 1, 18),
    _CipCardSubChannelFBLWait_Type()
)
cipCardSubChannelFBLWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardSubChannelFBLWait.setStatus("current")
_CipCardClaw_ObjectIdentity = ObjectIdentity
cipCardClaw = _CipCardClaw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4)
)
_CipCardClawTable_Object = MibTable
cipCardClawTable = _CipCardClawTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cipCardClawTable.setStatus("current")
_CipCardClawEntry_Object = MibTableRow
cipCardClawEntry = _CipCardClawEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1)
)
cipCardClawEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"),
)
if mibBuilder.loadTexts:
    cipCardClawEntry.setStatus("current")


class _CipCardClawIndex_Type(Integer32):
    """Custom type cipCardClawIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CipCardClawIndex_Type.__name__ = "Integer32"
_CipCardClawIndex_Object = MibTableColumn
cipCardClawIndex = _CipCardClawIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1, 1),
    _CipCardClawIndex_Type()
)
cipCardClawIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawIndex.setStatus("current")
_CipCardClawConnected_Type = TruthValue
_CipCardClawConnected_Object = MibTableColumn
cipCardClawConnected = _CipCardClawConnected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 1, 1, 2),
    _CipCardClawConnected_Type()
)
cipCardClawConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawConnected.setStatus("current")
_CipCardClawConfigTable_Object = MibTable
cipCardClawConfigTable = _CipCardClawConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cipCardClawConfigTable.setStatus("current")
_CipCardClawConfigEntry_Object = MibTableRow
cipCardClawConfigEntry = _CipCardClawConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1)
)
cipCardClawConfigEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"),
)
if mibBuilder.loadTexts:
    cipCardClawConfigEntry.setStatus("current")


class _CipCardClawConfigPath_Type(OctetString):
    """Custom type cipCardClawConfigPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CipCardClawConfigPath_Type.__name__ = "OctetString"
_CipCardClawConfigPath_Object = MibTableColumn
cipCardClawConfigPath = _CipCardClawConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 1),
    _CipCardClawConfigPath_Type()
)
cipCardClawConfigPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigPath.setStatus("current")


class _CipCardClawConfigDevice_Type(OctetString):
    """Custom type cipCardClawConfigDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CipCardClawConfigDevice_Type.__name__ = "OctetString"
_CipCardClawConfigDevice_Object = MibTableColumn
cipCardClawConfigDevice = _CipCardClawConfigDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 2),
    _CipCardClawConfigDevice_Type()
)
cipCardClawConfigDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigDevice.setStatus("current")
_CipCardClawConfigIpAddr_Type = IpAddress
_CipCardClawConfigIpAddr_Object = MibTableColumn
cipCardClawConfigIpAddr = _CipCardClawConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 3),
    _CipCardClawConfigIpAddr_Type()
)
cipCardClawConfigIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigIpAddr.setStatus("current")


class _CipCardClawConfigHostName_Type(DisplayString):
    """Custom type cipCardClawConfigHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardClawConfigHostName_Type.__name__ = "DisplayString"
_CipCardClawConfigHostName_Object = MibTableColumn
cipCardClawConfigHostName = _CipCardClawConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 4),
    _CipCardClawConfigHostName_Type()
)
cipCardClawConfigHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigHostName.setStatus("current")


class _CipCardClawConfigRouterName_Type(DisplayString):
    """Custom type cipCardClawConfigRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardClawConfigRouterName_Type.__name__ = "DisplayString"
_CipCardClawConfigRouterName_Object = MibTableColumn
cipCardClawConfigRouterName = _CipCardClawConfigRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 5),
    _CipCardClawConfigRouterName_Type()
)
cipCardClawConfigRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigRouterName.setStatus("current")


class _CipCardClawConfigHostAppl_Type(DisplayString):
    """Custom type cipCardClawConfigHostAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardClawConfigHostAppl_Type.__name__ = "DisplayString"
_CipCardClawConfigHostAppl_Object = MibTableColumn
cipCardClawConfigHostAppl = _CipCardClawConfigHostAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 6),
    _CipCardClawConfigHostAppl_Type()
)
cipCardClawConfigHostAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigHostAppl.setStatus("current")


class _CipCardClawConfigRouterAppl_Type(DisplayString):
    """Custom type cipCardClawConfigRouterAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardClawConfigRouterAppl_Type.__name__ = "DisplayString"
_CipCardClawConfigRouterAppl_Object = MibTableColumn
cipCardClawConfigRouterAppl = _CipCardClawConfigRouterAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 7),
    _CipCardClawConfigRouterAppl_Type()
)
cipCardClawConfigRouterAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigRouterAppl.setStatus("current")
_CipCardClawConfigBroadcastEnable_Type = TruthValue
_CipCardClawConfigBroadcastEnable_Object = MibTableColumn
cipCardClawConfigBroadcastEnable = _CipCardClawConfigBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 8),
    _CipCardClawConfigBroadcastEnable_Type()
)
cipCardClawConfigBroadcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigBroadcastEnable.setStatus("current")
_CipCardClawConfigRowStatus_Type = RowStatus
_CipCardClawConfigRowStatus_Object = MibTableColumn
cipCardClawConfigRowStatus = _CipCardClawConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 2, 1, 9),
    _CipCardClawConfigRowStatus_Type()
)
cipCardClawConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardClawConfigRowStatus.setStatus("current")
_CipCardClawDataXferStatsTable_Object = MibTable
cipCardClawDataXferStatsTable = _CipCardClawDataXferStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsTable.setStatus("current")
_CipCardClawDataXferStatsEntry_Object = MibTableRow
cipCardClawDataXferStatsEntry = _CipCardClawDataXferStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1)
)
cipCardClawDataXferStatsEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardClawIndex"),
)
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsEntry.setStatus("current")
_CipCardClawDataXferStatsBlocksRead_Type = Counter32
_CipCardClawDataXferStatsBlocksRead_Object = MibTableColumn
cipCardClawDataXferStatsBlocksRead = _CipCardClawDataXferStatsBlocksRead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 1),
    _CipCardClawDataXferStatsBlocksRead_Type()
)
cipCardClawDataXferStatsBlocksRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsBlocksRead.setStatus("current")
_CipCardClawDataXferStatsBlocksWritten_Type = Counter32
_CipCardClawDataXferStatsBlocksWritten_Object = MibTableColumn
cipCardClawDataXferStatsBlocksWritten = _CipCardClawDataXferStatsBlocksWritten_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 2),
    _CipCardClawDataXferStatsBlocksWritten_Type()
)
cipCardClawDataXferStatsBlocksWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsBlocksWritten.setStatus("current")
_CipCardClawDataXferStatsBytesRead_Type = Counter32
_CipCardClawDataXferStatsBytesRead_Object = MibTableColumn
cipCardClawDataXferStatsBytesRead = _CipCardClawDataXferStatsBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 3),
    _CipCardClawDataXferStatsBytesRead_Type()
)
cipCardClawDataXferStatsBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsBytesRead.setStatus("current")
_CipCardClawDataXferStatsHCBytesRead_Type = Counter64
_CipCardClawDataXferStatsHCBytesRead_Object = MibTableColumn
cipCardClawDataXferStatsHCBytesRead = _CipCardClawDataXferStatsHCBytesRead_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 4),
    _CipCardClawDataXferStatsHCBytesRead_Type()
)
cipCardClawDataXferStatsHCBytesRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsHCBytesRead.setStatus("current")
_CipCardClawDataXferStatsBytesWritten_Type = Counter32
_CipCardClawDataXferStatsBytesWritten_Object = MibTableColumn
cipCardClawDataXferStatsBytesWritten = _CipCardClawDataXferStatsBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 5),
    _CipCardClawDataXferStatsBytesWritten_Type()
)
cipCardClawDataXferStatsBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsBytesWritten.setStatus("current")
_CipCardClawDataXferStatsHCBytesWritten_Type = Counter64
_CipCardClawDataXferStatsHCBytesWritten_Object = MibTableColumn
cipCardClawDataXferStatsHCBytesWritten = _CipCardClawDataXferStatsHCBytesWritten_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 6),
    _CipCardClawDataXferStatsHCBytesWritten_Type()
)
cipCardClawDataXferStatsHCBytesWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsHCBytesWritten.setStatus("current")
_CipCardClawDataXferStatsReadBlocksDropped_Type = Counter32
_CipCardClawDataXferStatsReadBlocksDropped_Object = MibTableColumn
cipCardClawDataXferStatsReadBlocksDropped = _CipCardClawDataXferStatsReadBlocksDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 7),
    _CipCardClawDataXferStatsReadBlocksDropped_Type()
)
cipCardClawDataXferStatsReadBlocksDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsReadBlocksDropped.setStatus("current")
_CipCardClawDataXferStatsWriteBlocksDropped_Type = Counter32
_CipCardClawDataXferStatsWriteBlocksDropped_Object = MibTableColumn
cipCardClawDataXferStatsWriteBlocksDropped = _CipCardClawDataXferStatsWriteBlocksDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 8),
    _CipCardClawDataXferStatsWriteBlocksDropped_Type()
)
cipCardClawDataXferStatsWriteBlocksDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsWriteBlocksDropped.setStatus("current")
_CipCardClawDataXferStatsBufferGetRetryCount_Type = Counter32
_CipCardClawDataXferStatsBufferGetRetryCount_Object = MibTableColumn
cipCardClawDataXferStatsBufferGetRetryCount = _CipCardClawDataXferStatsBufferGetRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 4, 3, 1, 9),
    _CipCardClawDataXferStatsBufferGetRetryCount_Type()
)
cipCardClawDataXferStatsBufferGetRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardClawDataXferStatsBufferGetRetryCount.setStatus("current")
_CipCardTraps_ObjectIdentity = ObjectIdentity
cipCardTraps = _CipCardTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5)
)
_CipCardApplicationTable_Object = MibTable
cipCardApplicationTable = _CipCardApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6)
)
if mibBuilder.loadTexts:
    cipCardApplicationTable.setStatus("current")
_CipCardApplicationEntry_Object = MibTableRow
cipCardApplicationEntry = _CipCardApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1)
)
cipCardApplicationEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardApplicationNameIndex"),
)
if mibBuilder.loadTexts:
    cipCardApplicationEntry.setStatus("current")


class _CipCardApplicationNameIndex_Type(DisplayString):
    """Custom type cipCardApplicationNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_CipCardApplicationNameIndex_Type.__name__ = "DisplayString"
_CipCardApplicationNameIndex_Object = MibTableColumn
cipCardApplicationNameIndex = _CipCardApplicationNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 1),
    _CipCardApplicationNameIndex_Type()
)
cipCardApplicationNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cipCardApplicationNameIndex.setStatus("current")
_CipCardApplicationRevision_Type = Integer32
_CipCardApplicationRevision_Object = MibTableColumn
cipCardApplicationRevision = _CipCardApplicationRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 2),
    _CipCardApplicationRevision_Type()
)
cipCardApplicationRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardApplicationRevision.setStatus("current")


class _CipCardApplicationCompileInfo_Type(DisplayString):
    """Custom type cipCardApplicationCompileInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CipCardApplicationCompileInfo_Type.__name__ = "DisplayString"
_CipCardApplicationCompileInfo_Object = MibTableColumn
cipCardApplicationCompileInfo = _CipCardApplicationCompileInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 6, 1, 3),
    _CipCardApplicationCompileInfo_Type()
)
cipCardApplicationCompileInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cipCardApplicationCompileInfo.setStatus("current")
_CiscoChannelMibConformance_ObjectIdentity = ObjectIdentity
ciscoChannelMibConformance = _CiscoChannelMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2)
)
_CiscoChannelMibCompliances_ObjectIdentity = ObjectIdentity
ciscoChannelMibCompliances = _CiscoChannelMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1)
)
_CiscoChannelMibGroups_ObjectIdentity = ObjectIdentity
ciscoChannelMibGroups = _CiscoChannelMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2)
)

# Managed Objects groups

ciscoChannelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 1)
)
ciscoChannelGroup.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardEntryName"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryTotalMemory"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryFreeMemory"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryCpuUtilization"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryTimeSinceLastReset"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMajorSwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMinorSwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMajorHwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMinorHwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardApplicationRevision"),
        ("CISCO-CHANNEL-MIB", "cipCardApplicationCompileInfo"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdType"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdOnline"),
        ("CISCO-CHANNEL-MIB", "implicitIncidents"),
        ("CISCO-CHANNEL-MIB", "codeViolationErrors"),
        ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"),
        ("CISCO-CHANNEL-MIB", "linkFailureNOSs"),
        ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"),
        ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"),
        ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelConnections"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCancels"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelSelectiveResets"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelSystemResets"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelDeviceErrors"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelWriteBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseData"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseDataTime"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCuBusies"),
        ("CISCO-CHANNEL-MIB", "cipCardClawIndex"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConnected"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigPath"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigDevice"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigIpAddr"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostName"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterName"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostAppl"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterAppl"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsReadBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsWriteBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBufferGetRetryCount"))
)
if mibBuilder.loadTexts:
    ciscoChannelGroup.setStatus("current")

ciscoChannelGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 2)
)
ciscoChannelGroupRev1.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardEntryName"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryTotalMemory"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryFreeMemory"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryCpuUtilization"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryTimeSinceLastReset"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMajorSwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMinorSwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMajorHwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryMinorHwRevisionNr"),
        ("CISCO-CHANNEL-MIB", "cipCardApplicationRevision"),
        ("CISCO-CHANNEL-MIB", "cipCardApplicationCompileInfo"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdType"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdOnline"),
        ("CISCO-CHANNEL-MIB", "implicitIncidents"),
        ("CISCO-CHANNEL-MIB", "codeViolationErrors"),
        ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"),
        ("CISCO-CHANNEL-MIB", "linkFailureNOSs"),
        ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"),
        ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"),
        ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdLastStat"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdNextStat"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelConnections"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCancels"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelSelectiveResets"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelSystemResets"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelDeviceErrors"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelWriteBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseData"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelLastSenseDataTime"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCuBusies"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCmdRetries"),
        ("CISCO-CHANNEL-MIB", "cipCardClawIndex"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConnected"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigPath"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigDevice"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigIpAddr"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostName"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterName"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigHostAppl"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigRouterAppl"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBlocksWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesRead"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBytesWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsHCBytesWritten"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsReadBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsWriteBlocksDropped"),
        ("CISCO-CHANNEL-MIB", "cipCardClawDataXferStatsBufferGetRetryCount"))
)
if mibBuilder.loadTexts:
    ciscoChannelGroupRev1.setStatus("current")

ciscoChannelGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 3)
)
ciscoChannelGroupRev2.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad1m"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad5m"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryCpuLoad60m"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad1m"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad5m"),
        ("CISCO-CHANNEL-MIB", "cipCardEntryDmaLoad60m"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad1m"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad5m"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdChannelLoad60m"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigBroadcastEnable"),
        ("CISCO-CHANNEL-MIB", "cipCardClawConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoChannelGroupRev2.setStatus("current")

ciscoChannelGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 2, 4)
)
ciscoChannelGroupRev3.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardSubChannelResetEvent"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelShortBusy"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelCMDRetry"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelBufferWait"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelStatPending"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelSuspend"),
        ("CISCO-CHANNEL-MIB", "cipCardSubChannelFBLWait"))
)
if mibBuilder.loadTexts:
    ciscoChannelGroupRev3.setStatus("current")


# Notification objects

cipCardLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5, 1)
)
cipCardLinkFailure.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"),
        ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"),
        ("CISCO-CHANNEL-MIB", "implicitIncidents"),
        ("CISCO-CHANNEL-MIB", "codeViolationErrors"),
        ("CISCO-CHANNEL-MIB", "linkFailureSignalOrSyncLoss"),
        ("CISCO-CHANNEL-MIB", "linkFailureNOSs"),
        ("CISCO-CHANNEL-MIB", "linkFailureSequenceTimeouts"),
        ("CISCO-CHANNEL-MIB", "linkFailureInvalidSequences"))
)
if mibBuilder.loadTexts:
    cipCardLinkFailure.setStatus(
        "deprecated"
    )

cipCardDtrBrdLinkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 1, 5, 2)
)
cipCardDtrBrdLinkFailure.setObjects(
      *(("CISCO-CHANNEL-MIB", "cipCardDtrBrdStatus"),
        ("CISCO-CHANNEL-MIB", "cipCardDtrBrdSignal"),
        ("CISCO-CHANNEL-MIB", "linkIncidentTrapCause"))
)
if mibBuilder.loadTexts:
    cipCardDtrBrdLinkFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoChannelMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoChannelMibCompliance.setStatus(
        "current"
    )

ciscoChannelMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoChannelMibComplianceRev1.setStatus(
        "current"
    )

ciscoChannelMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 20, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoChannelMibComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CHANNEL-MIB",
    **{"channel": channel,
       "cipCard": cipCard,
       "cipCardTable": cipCardTable,
       "cipCardEntry": cipCardEntry,
       "cipCardEntryIndex": cipCardEntryIndex,
       "cipCardEntryName": cipCardEntryName,
       "cipCardEntryTotalMemory": cipCardEntryTotalMemory,
       "cipCardEntryFreeMemory": cipCardEntryFreeMemory,
       "cipCardEntryCpuUtilization": cipCardEntryCpuUtilization,
       "cipCardEntryTimeSinceLastReset": cipCardEntryTimeSinceLastReset,
       "cipCardEntryMajorSwRevisionNr": cipCardEntryMajorSwRevisionNr,
       "cipCardEntryMinorSwRevisionNr": cipCardEntryMinorSwRevisionNr,
       "cipCardEntryMajorHwRevisionNr": cipCardEntryMajorHwRevisionNr,
       "cipCardEntryMinorHwRevisionNr": cipCardEntryMinorHwRevisionNr,
       "cipCardEntryCpuLoad1m": cipCardEntryCpuLoad1m,
       "cipCardEntryCpuLoad5m": cipCardEntryCpuLoad5m,
       "cipCardEntryCpuLoad60m": cipCardEntryCpuLoad60m,
       "cipCardEntryDmaLoad1m": cipCardEntryDmaLoad1m,
       "cipCardEntryDmaLoad5m": cipCardEntryDmaLoad5m,
       "cipCardEntryDmaLoad60m": cipCardEntryDmaLoad60m,
       "cipCardDaughterBoardTable": cipCardDaughterBoardTable,
       "cipCardDaughterBoardEntry": cipCardDaughterBoardEntry,
       "cipCardDtrBrdIndex": cipCardDtrBrdIndex,
       "cipCardDtrBrdType": cipCardDtrBrdType,
       "cipCardDtrBrdStatus": cipCardDtrBrdStatus,
       "cipCardDtrBrdSignal": cipCardDtrBrdSignal,
       "cipCardDtrBrdOnline": cipCardDtrBrdOnline,
       "implicitIncidents": implicitIncidents,
       "codeViolationErrors": codeViolationErrors,
       "linkFailureSignalOrSyncLoss": linkFailureSignalOrSyncLoss,
       "linkFailureNOSs": linkFailureNOSs,
       "linkFailureSequenceTimeouts": linkFailureSequenceTimeouts,
       "linkFailureInvalidSequences": linkFailureInvalidSequences,
       "linkIncidentTrapCause": linkIncidentTrapCause,
       "cipCardDtrBrdLastStat": cipCardDtrBrdLastStat,
       "cipCardDtrBrdNextStat": cipCardDtrBrdNextStat,
       "cipCardDtrBrdChannelLoad1m": cipCardDtrBrdChannelLoad1m,
       "cipCardDtrBrdChannelLoad5m": cipCardDtrBrdChannelLoad5m,
       "cipCardDtrBrdChannelLoad60m": cipCardDtrBrdChannelLoad60m,
       "cipCardSubChannelTable": cipCardSubChannelTable,
       "cipCardSubChannelEntry": cipCardSubChannelEntry,
       "cipCardSubChannelIndex": cipCardSubChannelIndex,
       "cipCardSubChannelConnections": cipCardSubChannelConnections,
       "cipCardSubChannelCancels": cipCardSubChannelCancels,
       "cipCardSubChannelSelectiveResets": cipCardSubChannelSelectiveResets,
       "cipCardSubChannelSystemResets": cipCardSubChannelSystemResets,
       "cipCardSubChannelDeviceErrors": cipCardSubChannelDeviceErrors,
       "cipCardSubChannelWriteBlocksDropped": cipCardSubChannelWriteBlocksDropped,
       "cipCardSubChannelLastSenseData": cipCardSubChannelLastSenseData,
       "cipCardSubChannelLastSenseDataTime": cipCardSubChannelLastSenseDataTime,
       "cipCardSubChannelCuBusies": cipCardSubChannelCuBusies,
       "cipCardSubChannelCmdRetries": cipCardSubChannelCmdRetries,
       "cipCardSubChannelResetEvent": cipCardSubChannelResetEvent,
       "cipCardSubChannelShortBusy": cipCardSubChannelShortBusy,
       "cipCardSubChannelCMDRetry": cipCardSubChannelCMDRetry,
       "cipCardSubChannelBufferWait": cipCardSubChannelBufferWait,
       "cipCardSubChannelStatPending": cipCardSubChannelStatPending,
       "cipCardSubChannelSuspend": cipCardSubChannelSuspend,
       "cipCardSubChannelFBLWait": cipCardSubChannelFBLWait,
       "cipCardClaw": cipCardClaw,
       "cipCardClawTable": cipCardClawTable,
       "cipCardClawEntry": cipCardClawEntry,
       "cipCardClawIndex": cipCardClawIndex,
       "cipCardClawConnected": cipCardClawConnected,
       "cipCardClawConfigTable": cipCardClawConfigTable,
       "cipCardClawConfigEntry": cipCardClawConfigEntry,
       "cipCardClawConfigPath": cipCardClawConfigPath,
       "cipCardClawConfigDevice": cipCardClawConfigDevice,
       "cipCardClawConfigIpAddr": cipCardClawConfigIpAddr,
       "cipCardClawConfigHostName": cipCardClawConfigHostName,
       "cipCardClawConfigRouterName": cipCardClawConfigRouterName,
       "cipCardClawConfigHostAppl": cipCardClawConfigHostAppl,
       "cipCardClawConfigRouterAppl": cipCardClawConfigRouterAppl,
       "cipCardClawConfigBroadcastEnable": cipCardClawConfigBroadcastEnable,
       "cipCardClawConfigRowStatus": cipCardClawConfigRowStatus,
       "cipCardClawDataXferStatsTable": cipCardClawDataXferStatsTable,
       "cipCardClawDataXferStatsEntry": cipCardClawDataXferStatsEntry,
       "cipCardClawDataXferStatsBlocksRead": cipCardClawDataXferStatsBlocksRead,
       "cipCardClawDataXferStatsBlocksWritten": cipCardClawDataXferStatsBlocksWritten,
       "cipCardClawDataXferStatsBytesRead": cipCardClawDataXferStatsBytesRead,
       "cipCardClawDataXferStatsHCBytesRead": cipCardClawDataXferStatsHCBytesRead,
       "cipCardClawDataXferStatsBytesWritten": cipCardClawDataXferStatsBytesWritten,
       "cipCardClawDataXferStatsHCBytesWritten": cipCardClawDataXferStatsHCBytesWritten,
       "cipCardClawDataXferStatsReadBlocksDropped": cipCardClawDataXferStatsReadBlocksDropped,
       "cipCardClawDataXferStatsWriteBlocksDropped": cipCardClawDataXferStatsWriteBlocksDropped,
       "cipCardClawDataXferStatsBufferGetRetryCount": cipCardClawDataXferStatsBufferGetRetryCount,
       "cipCardTraps": cipCardTraps,
       "cipCardLinkFailure": cipCardLinkFailure,
       "cipCardDtrBrdLinkFailure": cipCardDtrBrdLinkFailure,
       "cipCardApplicationTable": cipCardApplicationTable,
       "cipCardApplicationEntry": cipCardApplicationEntry,
       "cipCardApplicationNameIndex": cipCardApplicationNameIndex,
       "cipCardApplicationRevision": cipCardApplicationRevision,
       "cipCardApplicationCompileInfo": cipCardApplicationCompileInfo,
       "ciscoChannelMibConformance": ciscoChannelMibConformance,
       "ciscoChannelMibCompliances": ciscoChannelMibCompliances,
       "ciscoChannelMibCompliance": ciscoChannelMibCompliance,
       "ciscoChannelMibComplianceRev1": ciscoChannelMibComplianceRev1,
       "ciscoChannelMibComplianceRev2": ciscoChannelMibComplianceRev2,
       "ciscoChannelMibGroups": ciscoChannelMibGroups,
       "ciscoChannelGroup": ciscoChannelGroup,
       "ciscoChannelGroupRev1": ciscoChannelGroupRev1,
       "ciscoChannelGroupRev2": ciscoChannelGroupRev2,
       "ciscoChannelGroupRev3": ciscoChannelGroupRev3}
)
