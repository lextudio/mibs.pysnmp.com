# SNMP MIB module (AVICI-FABRIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-FABRIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:41 2024
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

(aviciBayIndex,
 aviciSlotIndex) = mibBuilder.importSymbols(
    "AVICI-BAY-MIB",
    "aviciBayIndex",
    "aviciSlotIndex")

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(AviciBayType,
 AviciFabricLinkType,
 AviciModuleName,
 AviciRevisionType,
 AviciSlotType) = mibBuilder.importSymbols(
    "AVICI-TC",
    "AviciBayType",
    "AviciFabricLinkType",
    "AviciModuleName",
    "AviciRevisionType",
    "AviciSlotType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aviciFabricMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8)
)
aviciFabricMIB.setRevisions(
        ("0009-05-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciFabricObjects_ObjectIdentity = ObjectIdentity
aviciFabricObjects = _AviciFabricObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1)
)
_AviciFabricCounters_ObjectIdentity = ObjectIdentity
aviciFabricCounters = _AviciFabricCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1)
)
_AviciFabricCountersTable_Object = MibTable
aviciFabricCountersTable = _AviciFabricCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aviciFabricCountersTable.setStatus("current")
_AviciFabricCountersEntry_Object = MibTableRow
aviciFabricCountersEntry = _AviciFabricCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1)
)
aviciFabricCountersEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricLinkIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricCountersEntry.setStatus("current")
_AviciFabricHiPriPktsInserted_Type = Counter64
_AviciFabricHiPriPktsInserted_Object = MibTableColumn
aviciFabricHiPriPktsInserted = _AviciFabricHiPriPktsInserted_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 1),
    _AviciFabricHiPriPktsInserted_Type()
)
aviciFabricHiPriPktsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricHiPriPktsInserted.setStatus("current")
_AviciFabricLoPriPktsInserted_Type = Counter64
_AviciFabricLoPriPktsInserted_Object = MibTableColumn
aviciFabricLoPriPktsInserted = _AviciFabricLoPriPktsInserted_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 2),
    _AviciFabricLoPriPktsInserted_Type()
)
aviciFabricLoPriPktsInserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLoPriPktsInserted.setStatus("current")
_AviciFabricHiPriPktsForwarded_Type = Counter64
_AviciFabricHiPriPktsForwarded_Object = MibTableColumn
aviciFabricHiPriPktsForwarded = _AviciFabricHiPriPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 3),
    _AviciFabricHiPriPktsForwarded_Type()
)
aviciFabricHiPriPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricHiPriPktsForwarded.setStatus("current")
_AviciFabricLoPriPktsForwarded_Type = Counter64
_AviciFabricLoPriPktsForwarded_Object = MibTableColumn
aviciFabricLoPriPktsForwarded = _AviciFabricLoPriPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 4),
    _AviciFabricLoPriPktsForwarded_Type()
)
aviciFabricLoPriPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLoPriPktsForwarded.setStatus("current")
_AviciFabricHiPriFlitsForwarded_Type = Counter64
_AviciFabricHiPriFlitsForwarded_Object = MibTableColumn
aviciFabricHiPriFlitsForwarded = _AviciFabricHiPriFlitsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 5),
    _AviciFabricHiPriFlitsForwarded_Type()
)
aviciFabricHiPriFlitsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricHiPriFlitsForwarded.setStatus("current")
_AviciFabricLoPriFlitsForwarded_Type = Counter64
_AviciFabricLoPriFlitsForwarded_Object = MibTableColumn
aviciFabricLoPriFlitsForwarded = _AviciFabricLoPriFlitsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 1, 1, 6),
    _AviciFabricLoPriFlitsForwarded_Type()
)
aviciFabricLoPriFlitsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLoPriFlitsForwarded.setStatus("current")
_AviciFabricExtractedCountersTable_Object = MibTable
aviciFabricExtractedCountersTable = _AviciFabricExtractedCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    aviciFabricExtractedCountersTable.setStatus("current")
_AviciFabricExtractedCountersEntry_Object = MibTableRow
aviciFabricExtractedCountersEntry = _AviciFabricExtractedCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1)
)
aviciFabricExtractedCountersEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricLinkIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricExtractedCountersEntry.setStatus("current")
_AviciFabricExtractedHiPriPktsSelf_Type = Counter64
_AviciFabricExtractedHiPriPktsSelf_Object = MibTableColumn
aviciFabricExtractedHiPriPktsSelf = _AviciFabricExtractedHiPriPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 1),
    _AviciFabricExtractedHiPriPktsSelf_Type()
)
aviciFabricExtractedHiPriPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedHiPriPktsSelf.setStatus("current")
_AviciFabricExtractedLoPriPktsSelf_Type = Counter64
_AviciFabricExtractedLoPriPktsSelf_Object = MibTableColumn
aviciFabricExtractedLoPriPktsSelf = _AviciFabricExtractedLoPriPktsSelf_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 2),
    _AviciFabricExtractedLoPriPktsSelf_Type()
)
aviciFabricExtractedLoPriPktsSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedLoPriPktsSelf.setStatus("current")
_AviciFabricExtractedHiPriPkts_Type = Counter64
_AviciFabricExtractedHiPriPkts_Object = MibTableColumn
aviciFabricExtractedHiPriPkts = _AviciFabricExtractedHiPriPkts_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 3),
    _AviciFabricExtractedHiPriPkts_Type()
)
aviciFabricExtractedHiPriPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedHiPriPkts.setStatus("current")
_AviciFabricExtractedLoPriPkts_Type = Counter64
_AviciFabricExtractedLoPriPkts_Object = MibTableColumn
aviciFabricExtractedLoPriPkts = _AviciFabricExtractedLoPriPkts_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 4),
    _AviciFabricExtractedLoPriPkts_Type()
)
aviciFabricExtractedLoPriPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedLoPriPkts.setStatus("current")
_AviciFabricExtractedHiPriFlits_Type = Counter64
_AviciFabricExtractedHiPriFlits_Object = MibTableColumn
aviciFabricExtractedHiPriFlits = _AviciFabricExtractedHiPriFlits_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 5),
    _AviciFabricExtractedHiPriFlits_Type()
)
aviciFabricExtractedHiPriFlits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedHiPriFlits.setStatus("current")
_AviciFabricExtractedLoPriFlits_Type = Counter64
_AviciFabricExtractedLoPriFlits_Object = MibTableColumn
aviciFabricExtractedLoPriFlits = _AviciFabricExtractedLoPriFlits_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 1, 2, 1, 6),
    _AviciFabricExtractedLoPriFlits_Type()
)
aviciFabricExtractedLoPriFlits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricExtractedLoPriFlits.setStatus("current")
_AviciFabricConfig_ObjectIdentity = ObjectIdentity
aviciFabricConfig = _AviciFabricConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2)
)
_AviciFabricLinkTable_Object = MibTable
aviciFabricLinkTable = _AviciFabricLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aviciFabricLinkTable.setStatus("current")
_AviciFabricLinkEntry_Object = MibTableRow
aviciFabricLinkEntry = _AviciFabricLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1)
)
aviciFabricLinkEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricLinkIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricLinkEntry.setStatus("current")
_AviciFabricLinkIndex_Type = AviciFabricLinkType
_AviciFabricLinkIndex_Object = MibTableColumn
aviciFabricLinkIndex = _AviciFabricLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 1),
    _AviciFabricLinkIndex_Type()
)
aviciFabricLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkIndex.setStatus("current")


class _AviciFabricLinkDescr_Type(DisplayString):
    """Custom type aviciFabricLinkDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_AviciFabricLinkDescr_Type.__name__ = "DisplayString"
_AviciFabricLinkDescr_Object = MibTableColumn
aviciFabricLinkDescr = _AviciFabricLinkDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 2),
    _AviciFabricLinkDescr_Type()
)
aviciFabricLinkDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkDescr.setStatus("current")


class _AviciFabricLinkAdminStatus_Type(Integer32):
    """Custom type aviciFabricLinkAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AviciFabricLinkAdminStatus_Type.__name__ = "Integer32"
_AviciFabricLinkAdminStatus_Object = MibTableColumn
aviciFabricLinkAdminStatus = _AviciFabricLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 3),
    _AviciFabricLinkAdminStatus_Type()
)
aviciFabricLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciFabricLinkAdminStatus.setStatus("current")


class _AviciFabricLinkOperStatus_Type(Integer32):
    """Custom type aviciFabricLinkOperStatus based on Integer32"""
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
        *(("admin-down", 3),
          ("down", 2),
          ("failed", 4),
          ("up", 1))
    )


_AviciFabricLinkOperStatus_Type.__name__ = "Integer32"
_AviciFabricLinkOperStatus_Object = MibTableColumn
aviciFabricLinkOperStatus = _AviciFabricLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 4),
    _AviciFabricLinkOperStatus_Type()
)
aviciFabricLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkOperStatus.setStatus("current")
_AviciFabricLinkSpeed_Type = Unsigned32
_AviciFabricLinkSpeed_Object = MibTableColumn
aviciFabricLinkSpeed = _AviciFabricLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 5),
    _AviciFabricLinkSpeed_Type()
)
aviciFabricLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkSpeed.setStatus("current")
_AviciFabricLinkCRCErrors_Type = Counter32
_AviciFabricLinkCRCErrors_Object = MibTableColumn
aviciFabricLinkCRCErrors = _AviciFabricLinkCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 6),
    _AviciFabricLinkCRCErrors_Type()
)
aviciFabricLinkCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkCRCErrors.setStatus("current")
_AviciFabricLinkDownTransitions_Type = Counter32
_AviciFabricLinkDownTransitions_Object = MibTableColumn
aviciFabricLinkDownTransitions = _AviciFabricLinkDownTransitions_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 7),
    _AviciFabricLinkDownTransitions_Type()
)
aviciFabricLinkDownTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkDownTransitions.setStatus("current")
_AviciFabricLinkLastChange_Type = TimeTicks
_AviciFabricLinkLastChange_Object = MibTableColumn
aviciFabricLinkLastChange = _AviciFabricLinkLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 1, 1, 8),
    _AviciFabricLinkLastChange_Type()
)
aviciFabricLinkLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLinkLastChange.setStatus("current")
_AviciFabricChannelTable_Object = MibTable
aviciFabricChannelTable = _AviciFabricChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    aviciFabricChannelTable.setStatus("current")
_AviciFabricChannelEntry_Object = MibTableRow
aviciFabricChannelEntry = _AviciFabricChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1)
)
aviciFabricChannelEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricChannelIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricChannelEntry.setStatus("current")


class _AviciFabricChannelIndex_Type(Integer32):
    """Custom type aviciFabricChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AviciFabricChannelIndex_Type.__name__ = "Integer32"
_AviciFabricChannelIndex_Object = MibTableColumn
aviciFabricChannelIndex = _AviciFabricChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1, 1),
    _AviciFabricChannelIndex_Type()
)
aviciFabricChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricChannelIndex.setStatus("current")
_AviciFabricChannelHiPriScrubEvents_Type = Counter32
_AviciFabricChannelHiPriScrubEvents_Object = MibTableColumn
aviciFabricChannelHiPriScrubEvents = _AviciFabricChannelHiPriScrubEvents_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1, 2),
    _AviciFabricChannelHiPriScrubEvents_Type()
)
aviciFabricChannelHiPriScrubEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricChannelHiPriScrubEvents.setStatus("current")
_AviciFabricChannelLoPriScrubEvents_Type = Counter32
_AviciFabricChannelLoPriScrubEvents_Object = MibTableColumn
aviciFabricChannelLoPriScrubEvents = _AviciFabricChannelLoPriScrubEvents_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1, 3),
    _AviciFabricChannelLoPriScrubEvents_Type()
)
aviciFabricChannelLoPriScrubEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricChannelLoPriScrubEvents.setStatus("current")
_AviciFabricChannelHiPriLastScrubTime_Type = TimeTicks
_AviciFabricChannelHiPriLastScrubTime_Object = MibTableColumn
aviciFabricChannelHiPriLastScrubTime = _AviciFabricChannelHiPriLastScrubTime_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1, 4),
    _AviciFabricChannelHiPriLastScrubTime_Type()
)
aviciFabricChannelHiPriLastScrubTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricChannelHiPriLastScrubTime.setStatus("current")
_AviciFabricChannelLoPriLastScrubTime_Type = TimeTicks
_AviciFabricChannelLoPriLastScrubTime_Object = MibTableColumn
aviciFabricChannelLoPriLastScrubTime = _AviciFabricChannelLoPriLastScrubTime_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 2, 2, 1, 5),
    _AviciFabricChannelLoPriLastScrubTime_Type()
)
aviciFabricChannelLoPriLastScrubTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricChannelLoPriLastScrubTime.setStatus("current")
_AviciFabricRouting_ObjectIdentity = ObjectIdentity
aviciFabricRouting = _AviciFabricRouting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3)
)
_AviciFabricLsaTable_Object = MibTable
aviciFabricLsaTable = _AviciFabricLsaTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aviciFabricLsaTable.setStatus("current")
_AviciFabricLsaEntry_Object = MibTableRow
aviciFabricLsaEntry = _AviciFabricLsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1)
)
aviciFabricLsaEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricLsaOriginBay"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricLsaOriginSlot"),
)
if mibBuilder.loadTexts:
    aviciFabricLsaEntry.setStatus("current")
_AviciFabricLsaOriginBay_Type = AviciBayType
_AviciFabricLsaOriginBay_Object = MibTableColumn
aviciFabricLsaOriginBay = _AviciFabricLsaOriginBay_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 1),
    _AviciFabricLsaOriginBay_Type()
)
aviciFabricLsaOriginBay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviciFabricLsaOriginBay.setStatus("current")
_AviciFabricLsaOriginSlot_Type = AviciSlotType
_AviciFabricLsaOriginSlot_Object = MibTableColumn
aviciFabricLsaOriginSlot = _AviciFabricLsaOriginSlot_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 2),
    _AviciFabricLsaOriginSlot_Type()
)
aviciFabricLsaOriginSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviciFabricLsaOriginSlot.setStatus("current")
_AviciFabricLsaSequenceNum_Type = Unsigned32
_AviciFabricLsaSequenceNum_Object = MibTableColumn
aviciFabricLsaSequenceNum = _AviciFabricLsaSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 3),
    _AviciFabricLsaSequenceNum_Type()
)
aviciFabricLsaSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaSequenceNum.setStatus("current")
_AviciFabricLsaCreationTime_Type = DisplayString
_AviciFabricLsaCreationTime_Object = MibTableColumn
aviciFabricLsaCreationTime = _AviciFabricLsaCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 4),
    _AviciFabricLsaCreationTime_Type()
)
aviciFabricLsaCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaCreationTime.setStatus("current")
_AviciFabricLsaModuleReachable_Type = TruthValue
_AviciFabricLsaModuleReachable_Object = MibTableColumn
aviciFabricLsaModuleReachable = _AviciFabricLsaModuleReachable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 5),
    _AviciFabricLsaModuleReachable_Type()
)
aviciFabricLsaModuleReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModuleReachable.setStatus("current")


class _AviciFabricLsaChannels_Type(DisplayString):
    """Custom type aviciFabricLsaChannels based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AviciFabricLsaChannels_Type.__name__ = "DisplayString"
_AviciFabricLsaChannels_Object = MibTableColumn
aviciFabricLsaChannels = _AviciFabricLsaChannels_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 6),
    _AviciFabricLsaChannels_Type()
)
aviciFabricLsaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaChannels.setStatus("current")
_AviciFabricLsaModulePlusX_Type = AviciModuleName
_AviciFabricLsaModulePlusX_Object = MibTableColumn
aviciFabricLsaModulePlusX = _AviciFabricLsaModulePlusX_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 7),
    _AviciFabricLsaModulePlusX_Type()
)
aviciFabricLsaModulePlusX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModulePlusX.setStatus("current")
_AviciFabricLsaModuleMinusX_Type = AviciModuleName
_AviciFabricLsaModuleMinusX_Object = MibTableColumn
aviciFabricLsaModuleMinusX = _AviciFabricLsaModuleMinusX_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 8),
    _AviciFabricLsaModuleMinusX_Type()
)
aviciFabricLsaModuleMinusX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModuleMinusX.setStatus("current")
_AviciFabricLsaModulePlusY_Type = AviciModuleName
_AviciFabricLsaModulePlusY_Object = MibTableColumn
aviciFabricLsaModulePlusY = _AviciFabricLsaModulePlusY_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 9),
    _AviciFabricLsaModulePlusY_Type()
)
aviciFabricLsaModulePlusY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModulePlusY.setStatus("current")
_AviciFabricLsaModuleMinusY_Type = AviciModuleName
_AviciFabricLsaModuleMinusY_Object = MibTableColumn
aviciFabricLsaModuleMinusY = _AviciFabricLsaModuleMinusY_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 10),
    _AviciFabricLsaModuleMinusY_Type()
)
aviciFabricLsaModuleMinusY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModuleMinusY.setStatus("current")
_AviciFabricLsaModulePlusZ_Type = AviciModuleName
_AviciFabricLsaModulePlusZ_Object = MibTableColumn
aviciFabricLsaModulePlusZ = _AviciFabricLsaModulePlusZ_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 11),
    _AviciFabricLsaModulePlusZ_Type()
)
aviciFabricLsaModulePlusZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModulePlusZ.setStatus("current")
_AviciFabricLsaModuleMinusZ_Type = AviciModuleName
_AviciFabricLsaModuleMinusZ_Object = MibTableColumn
aviciFabricLsaModuleMinusZ = _AviciFabricLsaModuleMinusZ_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 1, 1, 12),
    _AviciFabricLsaModuleMinusZ_Type()
)
aviciFabricLsaModuleMinusZ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaModuleMinusZ.setStatus("current")
_AviciFabricLsaSummaryTable_Object = MibTable
aviciFabricLsaSummaryTable = _AviciFabricLsaSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    aviciFabricLsaSummaryTable.setStatus("current")
_AviciFabricLsaSummaryEntry_Object = MibTableRow
aviciFabricLsaSummaryEntry = _AviciFabricLsaSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 2, 1)
)
aviciFabricLsaSummaryEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricLsaSummaryEntry.setStatus("current")
_AviciFabricLsaSummaryChecksum_Type = Unsigned32
_AviciFabricLsaSummaryChecksum_Object = MibTableColumn
aviciFabricLsaSummaryChecksum = _AviciFabricLsaSummaryChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 2, 1, 1),
    _AviciFabricLsaSummaryChecksum_Type()
)
aviciFabricLsaSummaryChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricLsaSummaryChecksum.setStatus("current")
_AviciFabricPathTable_Object = MibTable
aviciFabricPathTable = _AviciFabricPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    aviciFabricPathTable.setStatus("current")
_AviciFabricPathEntry_Object = MibTableRow
aviciFabricPathEntry = _AviciFabricPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3, 1)
)
aviciFabricPathEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricPathDestinationBay"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricPathDestinationSlot"),
    (0, "AVICI-FABRIC-MIB", "aviciFabricPathIndex"),
)
if mibBuilder.loadTexts:
    aviciFabricPathEntry.setStatus("current")


class _AviciFabricPathIndex_Type(Integer32):
    """Custom type aviciFabricPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_AviciFabricPathIndex_Type.__name__ = "Integer32"
_AviciFabricPathIndex_Object = MibTableColumn
aviciFabricPathIndex = _AviciFabricPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3, 1, 1),
    _AviciFabricPathIndex_Type()
)
aviciFabricPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricPathIndex.setStatus("current")
_AviciFabricPathDestinationBay_Type = AviciBayType
_AviciFabricPathDestinationBay_Object = MibTableColumn
aviciFabricPathDestinationBay = _AviciFabricPathDestinationBay_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3, 1, 2),
    _AviciFabricPathDestinationBay_Type()
)
aviciFabricPathDestinationBay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviciFabricPathDestinationBay.setStatus("current")
_AviciFabricPathDestinationSlot_Type = AviciSlotType
_AviciFabricPathDestinationSlot_Object = MibTableColumn
aviciFabricPathDestinationSlot = _AviciFabricPathDestinationSlot_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3, 1, 3),
    _AviciFabricPathDestinationSlot_Type()
)
aviciFabricPathDestinationSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aviciFabricPathDestinationSlot.setStatus("current")


class _AviciFabricPathVector_Type(DisplayString):
    """Custom type aviciFabricPathVector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 185),
    )


_AviciFabricPathVector_Type.__name__ = "DisplayString"
_AviciFabricPathVector_Object = MibTableColumn
aviciFabricPathVector = _AviciFabricPathVector_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 1, 3, 3, 1, 4),
    _AviciFabricPathVector_Type()
)
aviciFabricPathVector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricPathVector.setStatus("current")
_AviciFabricGroup_ObjectIdentity = ObjectIdentity
aviciFabricGroup = _AviciFabricGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 2)
)
_AviciFabricHardwareVersion_Type = AviciRevisionType
_AviciFabricHardwareVersion_Object = MibScalar
aviciFabricHardwareVersion = _AviciFabricHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 2, 1),
    _AviciFabricHardwareVersion_Type()
)
aviciFabricHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricHardwareVersion.setStatus("current")
_AviciFabricRoutingProtocolVersion_Type = AviciRevisionType
_AviciFabricRoutingProtocolVersion_Object = MibScalar
aviciFabricRoutingProtocolVersion = _AviciFabricRoutingProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 2, 2),
    _AviciFabricRoutingProtocolVersion_Type()
)
aviciFabricRoutingProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciFabricRoutingProtocolVersion.setStatus("current")
_AviciFabricMIBConformance_ObjectIdentity = ObjectIdentity
aviciFabricMIBConformance = _AviciFabricMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3)
)
_AviciFabricMIBCompliances_ObjectIdentity = ObjectIdentity
aviciFabricMIBCompliances = _AviciFabricMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 1)
)
_AviciFabricMIBGroups_ObjectIdentity = ObjectIdentity
aviciFabricMIBGroups = _AviciFabricMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 2)
)

# Managed Objects groups

aviciFabricCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 2, 1)
)
aviciFabricCountersGroup.setObjects(
      *(("AVICI-FABRIC-MIB", "aviciFabricHiPriPktsInserted"),
        ("AVICI-FABRIC-MIB", "aviciFabricLoPriPktsInserted"),
        ("AVICI-FABRIC-MIB", "aviciFabricHiPriPktsForwarded"),
        ("AVICI-FABRIC-MIB", "aviciFabricLoPriPktsForwarded"),
        ("AVICI-FABRIC-MIB", "aviciFabricHiPriFlitsForwarded"),
        ("AVICI-FABRIC-MIB", "aviciFabricLoPriFlitsForwarded"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedHiPriPktsSelf"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedLoPriPktsSelf"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedHiPriPkts"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedLoPriPkts"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedHiPriFlits"),
        ("AVICI-FABRIC-MIB", "aviciFabricExtractedLoPriFlits"))
)
if mibBuilder.loadTexts:
    aviciFabricCountersGroup.setStatus("current")

aviciFabricGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 2, 2)
)
aviciFabricGeneralGroup.setObjects(
      *(("AVICI-FABRIC-MIB", "aviciFabricLinkIndex"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkDescr"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkAdminStatus"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkOperStatus"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkSpeed"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkCRCErrors"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkDownTransitions"),
        ("AVICI-FABRIC-MIB", "aviciFabricLinkLastChange"),
        ("AVICI-FABRIC-MIB", "aviciFabricChannelIndex"),
        ("AVICI-FABRIC-MIB", "aviciFabricChannelHiPriScrubEvents"),
        ("AVICI-FABRIC-MIB", "aviciFabricChannelLoPriScrubEvents"),
        ("AVICI-FABRIC-MIB", "aviciFabricChannelHiPriLastScrubTime"),
        ("AVICI-FABRIC-MIB", "aviciFabricChannelLoPriLastScrubTime"))
)
if mibBuilder.loadTexts:
    aviciFabricGeneralGroup.setStatus("current")

aviciFabricRoutingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 2, 3)
)
aviciFabricRoutingGroup.setObjects(
      *(("AVICI-FABRIC-MIB", "aviciFabricLsaSequenceNum"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaCreationTime"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModuleReachable"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaChannels"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModulePlusX"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModuleMinusX"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModulePlusY"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModuleMinusY"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModulePlusZ"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaModuleMinusZ"),
        ("AVICI-FABRIC-MIB", "aviciFabricLsaSummaryChecksum"),
        ("AVICI-FABRIC-MIB", "aviciFabricPathIndex"),
        ("AVICI-FABRIC-MIB", "aviciFabricPathVector"))
)
if mibBuilder.loadTexts:
    aviciFabricRoutingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aviciFabricMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 8, 3, 1, 1)
)
if mibBuilder.loadTexts:
    aviciFabricMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-FABRIC-MIB",
    **{"aviciFabricMIB": aviciFabricMIB,
       "aviciFabricObjects": aviciFabricObjects,
       "aviciFabricCounters": aviciFabricCounters,
       "aviciFabricCountersTable": aviciFabricCountersTable,
       "aviciFabricCountersEntry": aviciFabricCountersEntry,
       "aviciFabricHiPriPktsInserted": aviciFabricHiPriPktsInserted,
       "aviciFabricLoPriPktsInserted": aviciFabricLoPriPktsInserted,
       "aviciFabricHiPriPktsForwarded": aviciFabricHiPriPktsForwarded,
       "aviciFabricLoPriPktsForwarded": aviciFabricLoPriPktsForwarded,
       "aviciFabricHiPriFlitsForwarded": aviciFabricHiPriFlitsForwarded,
       "aviciFabricLoPriFlitsForwarded": aviciFabricLoPriFlitsForwarded,
       "aviciFabricExtractedCountersTable": aviciFabricExtractedCountersTable,
       "aviciFabricExtractedCountersEntry": aviciFabricExtractedCountersEntry,
       "aviciFabricExtractedHiPriPktsSelf": aviciFabricExtractedHiPriPktsSelf,
       "aviciFabricExtractedLoPriPktsSelf": aviciFabricExtractedLoPriPktsSelf,
       "aviciFabricExtractedHiPriPkts": aviciFabricExtractedHiPriPkts,
       "aviciFabricExtractedLoPriPkts": aviciFabricExtractedLoPriPkts,
       "aviciFabricExtractedHiPriFlits": aviciFabricExtractedHiPriFlits,
       "aviciFabricExtractedLoPriFlits": aviciFabricExtractedLoPriFlits,
       "aviciFabricConfig": aviciFabricConfig,
       "aviciFabricLinkTable": aviciFabricLinkTable,
       "aviciFabricLinkEntry": aviciFabricLinkEntry,
       "aviciFabricLinkIndex": aviciFabricLinkIndex,
       "aviciFabricLinkDescr": aviciFabricLinkDescr,
       "aviciFabricLinkAdminStatus": aviciFabricLinkAdminStatus,
       "aviciFabricLinkOperStatus": aviciFabricLinkOperStatus,
       "aviciFabricLinkSpeed": aviciFabricLinkSpeed,
       "aviciFabricLinkCRCErrors": aviciFabricLinkCRCErrors,
       "aviciFabricLinkDownTransitions": aviciFabricLinkDownTransitions,
       "aviciFabricLinkLastChange": aviciFabricLinkLastChange,
       "aviciFabricChannelTable": aviciFabricChannelTable,
       "aviciFabricChannelEntry": aviciFabricChannelEntry,
       "aviciFabricChannelIndex": aviciFabricChannelIndex,
       "aviciFabricChannelHiPriScrubEvents": aviciFabricChannelHiPriScrubEvents,
       "aviciFabricChannelLoPriScrubEvents": aviciFabricChannelLoPriScrubEvents,
       "aviciFabricChannelHiPriLastScrubTime": aviciFabricChannelHiPriLastScrubTime,
       "aviciFabricChannelLoPriLastScrubTime": aviciFabricChannelLoPriLastScrubTime,
       "aviciFabricRouting": aviciFabricRouting,
       "aviciFabricLsaTable": aviciFabricLsaTable,
       "aviciFabricLsaEntry": aviciFabricLsaEntry,
       "aviciFabricLsaOriginBay": aviciFabricLsaOriginBay,
       "aviciFabricLsaOriginSlot": aviciFabricLsaOriginSlot,
       "aviciFabricLsaSequenceNum": aviciFabricLsaSequenceNum,
       "aviciFabricLsaCreationTime": aviciFabricLsaCreationTime,
       "aviciFabricLsaModuleReachable": aviciFabricLsaModuleReachable,
       "aviciFabricLsaChannels": aviciFabricLsaChannels,
       "aviciFabricLsaModulePlusX": aviciFabricLsaModulePlusX,
       "aviciFabricLsaModuleMinusX": aviciFabricLsaModuleMinusX,
       "aviciFabricLsaModulePlusY": aviciFabricLsaModulePlusY,
       "aviciFabricLsaModuleMinusY": aviciFabricLsaModuleMinusY,
       "aviciFabricLsaModulePlusZ": aviciFabricLsaModulePlusZ,
       "aviciFabricLsaModuleMinusZ": aviciFabricLsaModuleMinusZ,
       "aviciFabricLsaSummaryTable": aviciFabricLsaSummaryTable,
       "aviciFabricLsaSummaryEntry": aviciFabricLsaSummaryEntry,
       "aviciFabricLsaSummaryChecksum": aviciFabricLsaSummaryChecksum,
       "aviciFabricPathTable": aviciFabricPathTable,
       "aviciFabricPathEntry": aviciFabricPathEntry,
       "aviciFabricPathIndex": aviciFabricPathIndex,
       "aviciFabricPathDestinationBay": aviciFabricPathDestinationBay,
       "aviciFabricPathDestinationSlot": aviciFabricPathDestinationSlot,
       "aviciFabricPathVector": aviciFabricPathVector,
       "aviciFabricGroup": aviciFabricGroup,
       "aviciFabricHardwareVersion": aviciFabricHardwareVersion,
       "aviciFabricRoutingProtocolVersion": aviciFabricRoutingProtocolVersion,
       "aviciFabricMIBConformance": aviciFabricMIBConformance,
       "aviciFabricMIBCompliances": aviciFabricMIBCompliances,
       "aviciFabricMIBCompliance": aviciFabricMIBCompliance,
       "aviciFabricMIBGroups": aviciFabricMIBGroups,
       "aviciFabricCountersGroup": aviciFabricCountersGroup,
       "aviciFabricGeneralGroup": aviciFabricGeneralGroup,
       "aviciFabricRoutingGroup": aviciFabricRoutingGroup}
)
