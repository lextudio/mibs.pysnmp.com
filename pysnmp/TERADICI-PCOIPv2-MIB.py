# SNMP MIB module (TERADICI-PCOIPv2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERADICI-PCOIPv2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:10 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

teraMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25071)
)
teraMibModule.setRevisions(
        ("2012-01-28 10:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TeraProducts_ObjectIdentity = ObjectIdentity
teraProducts = _TeraProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1)
)
_TeraPcoipV2_ObjectIdentity = ObjectIdentity
teraPcoipV2 = _TeraPcoipV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2)
)
_TeraPcoipGenStats_ObjectIdentity = ObjectIdentity
teraPcoipGenStats = _TeraPcoipGenStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1)
)
_PcoipGenStatsTable_Object = MibTable
pcoipGenStatsTable = _PcoipGenStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pcoipGenStatsTable.setStatus("current")
_PcoipGenStatsEntry_Object = MibTableRow
pcoipGenStatsEntry = _PcoipGenStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1)
)
pcoipGenStatsEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipGenStatsSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipGenStatsEntry.setStatus("current")


class _PcoipGenStatsSessionNumber_Type(Integer32):
    """Custom type pcoipGenStatsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipGenStatsSessionNumber_Type.__name__ = "Integer32"
_PcoipGenStatsSessionNumber_Object = MibTableColumn
pcoipGenStatsSessionNumber = _PcoipGenStatsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 1),
    _PcoipGenStatsSessionNumber_Type()
)
pcoipGenStatsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsSessionNumber.setStatus("current")
_PcoipGenStatsPacketsSent_Type = Counter64
_PcoipGenStatsPacketsSent_Object = MibTableColumn
pcoipGenStatsPacketsSent = _PcoipGenStatsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 2),
    _PcoipGenStatsPacketsSent_Type()
)
pcoipGenStatsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsPacketsSent.setStatus("current")
_PcoipGenStatsBytesSent_Type = Counter64
_PcoipGenStatsBytesSent_Object = MibTableColumn
pcoipGenStatsBytesSent = _PcoipGenStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 3),
    _PcoipGenStatsBytesSent_Type()
)
pcoipGenStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsBytesSent.setStatus("current")
_PcoipGenStatsPacketsReceived_Type = Counter64
_PcoipGenStatsPacketsReceived_Object = MibTableColumn
pcoipGenStatsPacketsReceived = _PcoipGenStatsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 4),
    _PcoipGenStatsPacketsReceived_Type()
)
pcoipGenStatsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsPacketsReceived.setStatus("current")
_PcoipGenStatsBytesReceived_Type = Counter64
_PcoipGenStatsBytesReceived_Object = MibTableColumn
pcoipGenStatsBytesReceived = _PcoipGenStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 5),
    _PcoipGenStatsBytesReceived_Type()
)
pcoipGenStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsBytesReceived.setStatus("current")
_PcoipGenStatsTxPacketsLost_Type = Counter64
_PcoipGenStatsTxPacketsLost_Object = MibTableColumn
pcoipGenStatsTxPacketsLost = _PcoipGenStatsTxPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 6),
    _PcoipGenStatsTxPacketsLost_Type()
)
pcoipGenStatsTxPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsTxPacketsLost.setStatus("current")
_PcoipGenStatsSessionDuration_Type = Counter64
_PcoipGenStatsSessionDuration_Object = MibTableColumn
pcoipGenStatsSessionDuration = _PcoipGenStatsSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 1, 1, 1, 7),
    _PcoipGenStatsSessionDuration_Type()
)
pcoipGenStatsSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenStatsSessionDuration.setStatus("current")
_TeraPcoipNetStats_ObjectIdentity = ObjectIdentity
teraPcoipNetStats = _TeraPcoipNetStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2)
)
_PcoipNetStatsTable_Object = MibTable
pcoipNetStatsTable = _PcoipNetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pcoipNetStatsTable.setStatus("current")
_PcoipNetStatsEntry_Object = MibTableRow
pcoipNetStatsEntry = _PcoipNetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1)
)
pcoipNetStatsEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipNetStatsSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipNetStatsEntry.setStatus("current")


class _PcoipNetStatsSessionNumber_Type(Integer32):
    """Custom type pcoipNetStatsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipNetStatsSessionNumber_Type.__name__ = "Integer32"
_PcoipNetStatsSessionNumber_Object = MibTableColumn
pcoipNetStatsSessionNumber = _PcoipNetStatsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 1),
    _PcoipNetStatsSessionNumber_Type()
)
pcoipNetStatsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsSessionNumber.setStatus("current")
_PcoipNetStatsRoundTripLatencyMs_Type = Counter64
_PcoipNetStatsRoundTripLatencyMs_Object = MibTableColumn
pcoipNetStatsRoundTripLatencyMs = _PcoipNetStatsRoundTripLatencyMs_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 2),
    _PcoipNetStatsRoundTripLatencyMs_Type()
)
pcoipNetStatsRoundTripLatencyMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsRoundTripLatencyMs.setStatus("current")
_PcoipNetStatsRXBWkbitPersec_Type = Counter64
_PcoipNetStatsRXBWkbitPersec_Object = MibTableColumn
pcoipNetStatsRXBWkbitPersec = _PcoipNetStatsRXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 3),
    _PcoipNetStatsRXBWkbitPersec_Type()
)
pcoipNetStatsRXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsRXBWkbitPersec.setStatus("current")


class _PcoipNetStatsRXBWPeakkbitPersec_Type(Integer32):
    """Custom type pcoipNetStatsRXBWPeakkbitPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PcoipNetStatsRXBWPeakkbitPersec_Type.__name__ = "Integer32"
_PcoipNetStatsRXBWPeakkbitPersec_Object = MibTableColumn
pcoipNetStatsRXBWPeakkbitPersec = _PcoipNetStatsRXBWPeakkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 4),
    _PcoipNetStatsRXBWPeakkbitPersec_Type()
)
pcoipNetStatsRXBWPeakkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsRXBWPeakkbitPersec.setStatus("current")


class _PcoipNetStatsRXPacketLossPercent_Type(Integer32):
    """Custom type pcoipNetStatsRXPacketLossPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PcoipNetStatsRXPacketLossPercent_Type.__name__ = "Integer32"
_PcoipNetStatsRXPacketLossPercent_Object = MibTableColumn
pcoipNetStatsRXPacketLossPercent = _PcoipNetStatsRXPacketLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 5),
    _PcoipNetStatsRXPacketLossPercent_Type()
)
pcoipNetStatsRXPacketLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsRXPacketLossPercent.setStatus("current")
_PcoipNetStatsTXBWkbitPersec_Type = Counter64
_PcoipNetStatsTXBWkbitPersec_Object = MibTableColumn
pcoipNetStatsTXBWkbitPersec = _PcoipNetStatsTXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 6),
    _PcoipNetStatsTXBWkbitPersec_Type()
)
pcoipNetStatsTXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsTXBWkbitPersec.setStatus("current")


class _PcoipNetStatsTXBWActiveLimitkbitPersec_Type(Integer32):
    """Custom type pcoipNetStatsTXBWActiveLimitkbitPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PcoipNetStatsTXBWActiveLimitkbitPersec_Type.__name__ = "Integer32"
_PcoipNetStatsTXBWActiveLimitkbitPersec_Object = MibTableColumn
pcoipNetStatsTXBWActiveLimitkbitPersec = _PcoipNetStatsTXBWActiveLimitkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 7),
    _PcoipNetStatsTXBWActiveLimitkbitPersec_Type()
)
pcoipNetStatsTXBWActiveLimitkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsTXBWActiveLimitkbitPersec.setStatus("current")


class _PcoipNetStatsTXBWLimitkbitPersec_Type(Integer32):
    """Custom type pcoipNetStatsTXBWLimitkbitPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PcoipNetStatsTXBWLimitkbitPersec_Type.__name__ = "Integer32"
_PcoipNetStatsTXBWLimitkbitPersec_Object = MibTableColumn
pcoipNetStatsTXBWLimitkbitPersec = _PcoipNetStatsTXBWLimitkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 8),
    _PcoipNetStatsTXBWLimitkbitPersec_Type()
)
pcoipNetStatsTXBWLimitkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsTXBWLimitkbitPersec.setStatus("current")


class _PcoipNetStatsTXPacketLossPercent_Type(Integer32):
    """Custom type pcoipNetStatsTXPacketLossPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PcoipNetStatsTXPacketLossPercent_Type.__name__ = "Integer32"
_PcoipNetStatsTXPacketLossPercent_Object = MibTableColumn
pcoipNetStatsTXPacketLossPercent = _PcoipNetStatsTXPacketLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 2, 1, 1, 9),
    _PcoipNetStatsTXPacketLossPercent_Type()
)
pcoipNetStatsTXPacketLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipNetStatsTXPacketLossPercent.setStatus("current")
_TeraPcoipAudioStats_ObjectIdentity = ObjectIdentity
teraPcoipAudioStats = _TeraPcoipAudioStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3)
)
_PcoipAudioStatsTable_Object = MibTable
pcoipAudioStatsTable = _PcoipAudioStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pcoipAudioStatsTable.setStatus("current")
_PcoipAudioStatsEntry_Object = MibTableRow
pcoipAudioStatsEntry = _PcoipAudioStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1)
)
pcoipAudioStatsEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipAudioStatsSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipAudioStatsEntry.setStatus("current")


class _PcoipAudioStatsSessionNumber_Type(Integer32):
    """Custom type pcoipAudioStatsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipAudioStatsSessionNumber_Type.__name__ = "Integer32"
_PcoipAudioStatsSessionNumber_Object = MibTableColumn
pcoipAudioStatsSessionNumber = _PcoipAudioStatsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 1),
    _PcoipAudioStatsSessionNumber_Type()
)
pcoipAudioStatsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsSessionNumber.setStatus("current")
_PcoipAudioStatsBytesReceived_Type = Counter64
_PcoipAudioStatsBytesReceived_Object = MibTableColumn
pcoipAudioStatsBytesReceived = _PcoipAudioStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 2),
    _PcoipAudioStatsBytesReceived_Type()
)
pcoipAudioStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsBytesReceived.setStatus("current")
_PcoipAudioStatsBytesSent_Type = Counter64
_PcoipAudioStatsBytesSent_Object = MibTableColumn
pcoipAudioStatsBytesSent = _PcoipAudioStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 3),
    _PcoipAudioStatsBytesSent_Type()
)
pcoipAudioStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsBytesSent.setStatus("current")
_PcoipAudioStatsRXBWkbitPersec_Type = Counter64
_PcoipAudioStatsRXBWkbitPersec_Object = MibTableColumn
pcoipAudioStatsRXBWkbitPersec = _PcoipAudioStatsRXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 4),
    _PcoipAudioStatsRXBWkbitPersec_Type()
)
pcoipAudioStatsRXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsRXBWkbitPersec.setStatus("current")
_PcoipAudioStatsTXBWkbitPersec_Type = Counter64
_PcoipAudioStatsTXBWkbitPersec_Object = MibTableColumn
pcoipAudioStatsTXBWkbitPersec = _PcoipAudioStatsTXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 5),
    _PcoipAudioStatsTXBWkbitPersec_Type()
)
pcoipAudioStatsTXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsTXBWkbitPersec.setStatus("current")


class _PcoipAudioStatsTXBWLimitkbitPersec_Type(Integer32):
    """Custom type pcoipAudioStatsTXBWLimitkbitPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PcoipAudioStatsTXBWLimitkbitPersec_Type.__name__ = "Integer32"
_PcoipAudioStatsTXBWLimitkbitPersec_Object = MibTableColumn
pcoipAudioStatsTXBWLimitkbitPersec = _PcoipAudioStatsTXBWLimitkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 3, 1, 1, 6),
    _PcoipAudioStatsTXBWLimitkbitPersec_Type()
)
pcoipAudioStatsTXBWLimitkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipAudioStatsTXBWLimitkbitPersec.setStatus("current")
_TeraPcoipImagingStats_ObjectIdentity = ObjectIdentity
teraPcoipImagingStats = _TeraPcoipImagingStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4)
)
_PcoipImagingStatsTable_Object = MibTable
pcoipImagingStatsTable = _PcoipImagingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    pcoipImagingStatsTable.setStatus("current")
_PcoipImagingStatsEntry_Object = MibTableRow
pcoipImagingStatsEntry = _PcoipImagingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1)
)
pcoipImagingStatsEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipImagingStatsSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipImagingStatsEntry.setStatus("current")


class _PcoipImagingStatsSessionNumber_Type(Integer32):
    """Custom type pcoipImagingStatsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipImagingStatsSessionNumber_Type.__name__ = "Integer32"
_PcoipImagingStatsSessionNumber_Object = MibTableColumn
pcoipImagingStatsSessionNumber = _PcoipImagingStatsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 1),
    _PcoipImagingStatsSessionNumber_Type()
)
pcoipImagingStatsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsSessionNumber.setStatus("current")
_PcoipImagingStatsBytesReceived_Type = Counter64
_PcoipImagingStatsBytesReceived_Object = MibTableColumn
pcoipImagingStatsBytesReceived = _PcoipImagingStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 2),
    _PcoipImagingStatsBytesReceived_Type()
)
pcoipImagingStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsBytesReceived.setStatus("current")
_PcoipImagingStatsBytesSent_Type = Counter64
_PcoipImagingStatsBytesSent_Object = MibTableColumn
pcoipImagingStatsBytesSent = _PcoipImagingStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 3),
    _PcoipImagingStatsBytesSent_Type()
)
pcoipImagingStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsBytesSent.setStatus("current")
_PcoipImagingStatsRXBWkbitPersec_Type = Counter64
_PcoipImagingStatsRXBWkbitPersec_Object = MibTableColumn
pcoipImagingStatsRXBWkbitPersec = _PcoipImagingStatsRXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 4),
    _PcoipImagingStatsRXBWkbitPersec_Type()
)
pcoipImagingStatsRXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsRXBWkbitPersec.setStatus("current")
_PcoipImagingStatsTXBWkbitPersec_Type = Counter64
_PcoipImagingStatsTXBWkbitPersec_Object = MibTableColumn
pcoipImagingStatsTXBWkbitPersec = _PcoipImagingStatsTXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 5),
    _PcoipImagingStatsTXBWkbitPersec_Type()
)
pcoipImagingStatsTXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsTXBWkbitPersec.setStatus("current")


class _PcoipImagingStatsEncodedFramesPersec_Type(Integer32):
    """Custom type pcoipImagingStatsEncodedFramesPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_PcoipImagingStatsEncodedFramesPersec_Type.__name__ = "Integer32"
_PcoipImagingStatsEncodedFramesPersec_Object = MibTableColumn
pcoipImagingStatsEncodedFramesPersec = _PcoipImagingStatsEncodedFramesPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 6),
    _PcoipImagingStatsEncodedFramesPersec_Type()
)
pcoipImagingStatsEncodedFramesPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsEncodedFramesPersec.setStatus("current")


class _PcoipImagingStatsActiveMinimumQuality_Type(Integer32):
    """Custom type pcoipImagingStatsActiveMinimumQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PcoipImagingStatsActiveMinimumQuality_Type.__name__ = "Integer32"
_PcoipImagingStatsActiveMinimumQuality_Object = MibTableColumn
pcoipImagingStatsActiveMinimumQuality = _PcoipImagingStatsActiveMinimumQuality_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 7),
    _PcoipImagingStatsActiveMinimumQuality_Type()
)
pcoipImagingStatsActiveMinimumQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsActiveMinimumQuality.setStatus("current")


class _PcoipImagingStatsDecoderCapabilitykbitPersec_Type(Integer32):
    """Custom type pcoipImagingStatsDecoderCapabilitykbitPersec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_PcoipImagingStatsDecoderCapabilitykbitPersec_Type.__name__ = "Integer32"
_PcoipImagingStatsDecoderCapabilitykbitPersec_Object = MibTableColumn
pcoipImagingStatsDecoderCapabilitykbitPersec = _PcoipImagingStatsDecoderCapabilitykbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 8),
    _PcoipImagingStatsDecoderCapabilitykbitPersec_Type()
)
pcoipImagingStatsDecoderCapabilitykbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsDecoderCapabilitykbitPersec.setStatus("current")


class _PcoipImagingStatsPipelineProcRate_Type(Integer32):
    """Custom type pcoipImagingStatsPipelineProcRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_PcoipImagingStatsPipelineProcRate_Type.__name__ = "Integer32"
_PcoipImagingStatsPipelineProcRate_Object = MibTableColumn
pcoipImagingStatsPipelineProcRate = _PcoipImagingStatsPipelineProcRate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 4, 1, 1, 9),
    _PcoipImagingStatsPipelineProcRate_Type()
)
pcoipImagingStatsPipelineProcRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingStatsPipelineProcRate.setStatus("current")
_TeraPcoipUSBStats_ObjectIdentity = ObjectIdentity
teraPcoipUSBStats = _TeraPcoipUSBStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5)
)
_PcoipUSBStatsTable_Object = MibTable
pcoipUSBStatsTable = _PcoipUSBStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pcoipUSBStatsTable.setStatus("current")
_PcoipUSBStatsEntry_Object = MibTableRow
pcoipUSBStatsEntry = _PcoipUSBStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1)
)
pcoipUSBStatsEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipUSBStatsSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipUSBStatsEntry.setStatus("current")


class _PcoipUSBStatsSessionNumber_Type(Integer32):
    """Custom type pcoipUSBStatsSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipUSBStatsSessionNumber_Type.__name__ = "Integer32"
_PcoipUSBStatsSessionNumber_Object = MibTableColumn
pcoipUSBStatsSessionNumber = _PcoipUSBStatsSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1, 1),
    _PcoipUSBStatsSessionNumber_Type()
)
pcoipUSBStatsSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBStatsSessionNumber.setStatus("current")
_PcoipUSBStatsBytesReceived_Type = Counter64
_PcoipUSBStatsBytesReceived_Object = MibTableColumn
pcoipUSBStatsBytesReceived = _PcoipUSBStatsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1, 2),
    _PcoipUSBStatsBytesReceived_Type()
)
pcoipUSBStatsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBStatsBytesReceived.setStatus("current")
_PcoipUSBStatsBytesSent_Type = Counter64
_PcoipUSBStatsBytesSent_Object = MibTableColumn
pcoipUSBStatsBytesSent = _PcoipUSBStatsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1, 3),
    _PcoipUSBStatsBytesSent_Type()
)
pcoipUSBStatsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBStatsBytesSent.setStatus("current")
_PcoipUSBStatsRXBWkbitPersec_Type = Counter64
_PcoipUSBStatsRXBWkbitPersec_Object = MibTableColumn
pcoipUSBStatsRXBWkbitPersec = _PcoipUSBStatsRXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1, 4),
    _PcoipUSBStatsRXBWkbitPersec_Type()
)
pcoipUSBStatsRXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBStatsRXBWkbitPersec.setStatus("current")
_PcoipUSBStatsTXBWkbitPersec_Type = Counter64
_PcoipUSBStatsTXBWkbitPersec_Object = MibTableColumn
pcoipUSBStatsTXBWkbitPersec = _PcoipUSBStatsTXBWkbitPersec_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 5, 1, 1, 5),
    _PcoipUSBStatsTXBWkbitPersec_Type()
)
pcoipUSBStatsTXBWkbitPersec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBStatsTXBWkbitPersec.setStatus("current")
_TeraPcoipGenDevices_ObjectIdentity = ObjectIdentity
teraPcoipGenDevices = _TeraPcoipGenDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6)
)
_PcoipGenDevicesTable_Object = MibTable
pcoipGenDevicesTable = _PcoipGenDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pcoipGenDevicesTable.setStatus("current")
_PcoipGenDevicesEntry_Object = MibTableRow
pcoipGenDevicesEntry = _PcoipGenDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1)
)
pcoipGenDevicesEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipGenDevicesSessionNumber"),
)
if mibBuilder.loadTexts:
    pcoipGenDevicesEntry.setStatus("current")


class _PcoipGenDevicesSessionNumber_Type(Integer32):
    """Custom type pcoipGenDevicesSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipGenDevicesSessionNumber_Type.__name__ = "Integer32"
_PcoipGenDevicesSessionNumber_Object = MibTableColumn
pcoipGenDevicesSessionNumber = _PcoipGenDevicesSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 1),
    _PcoipGenDevicesSessionNumber_Type()
)
pcoipGenDevicesSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesSessionNumber.setStatus("current")
_PcoipGenDevicesName_Type = OctetString
_PcoipGenDevicesName_Object = MibTableColumn
pcoipGenDevicesName = _PcoipGenDevicesName_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 2),
    _PcoipGenDevicesName_Type()
)
pcoipGenDevicesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesName.setStatus("current")
_PcoipGenDevicesDescription_Type = OctetString
_PcoipGenDevicesDescription_Object = MibTableColumn
pcoipGenDevicesDescription = _PcoipGenDevicesDescription_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 3),
    _PcoipGenDevicesDescription_Type()
)
pcoipGenDevicesDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesDescription.setStatus("current")
_PcoipGenDevicesGenericTag_Type = OctetString
_PcoipGenDevicesGenericTag_Object = MibTableColumn
pcoipGenDevicesGenericTag = _PcoipGenDevicesGenericTag_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 4),
    _PcoipGenDevicesGenericTag_Type()
)
pcoipGenDevicesGenericTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesGenericTag.setStatus("current")
_PcoipGenDevicesPartNumber_Type = OctetString
_PcoipGenDevicesPartNumber_Object = MibTableColumn
pcoipGenDevicesPartNumber = _PcoipGenDevicesPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 5),
    _PcoipGenDevicesPartNumber_Type()
)
pcoipGenDevicesPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesPartNumber.setStatus("current")
_PcoipGenDevicesFwPartNumber_Type = OctetString
_PcoipGenDevicesFwPartNumber_Object = MibScalar
pcoipGenDevicesFwPartNumber = _PcoipGenDevicesFwPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 6),
    _PcoipGenDevicesFwPartNumber_Type()
)
pcoipGenDevicesFwPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesFwPartNumber.setStatus("current")
_PcoipGenDevicesSerialNumber_Type = OctetString
_PcoipGenDevicesSerialNumber_Object = MibTableColumn
pcoipGenDevicesSerialNumber = _PcoipGenDevicesSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 7),
    _PcoipGenDevicesSerialNumber_Type()
)
pcoipGenDevicesSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesSerialNumber.setStatus("current")
_PcoipGenDevicesHardwareVersion_Type = OctetString
_PcoipGenDevicesHardwareVersion_Object = MibTableColumn
pcoipGenDevicesHardwareVersion = _PcoipGenDevicesHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 8),
    _PcoipGenDevicesHardwareVersion_Type()
)
pcoipGenDevicesHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesHardwareVersion.setStatus("current")
_PcoipGenDevicesFirmwareVersion_Type = OctetString
_PcoipGenDevicesFirmwareVersion_Object = MibTableColumn
pcoipGenDevicesFirmwareVersion = _PcoipGenDevicesFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 9),
    _PcoipGenDevicesFirmwareVersion_Type()
)
pcoipGenDevicesFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesFirmwareVersion.setStatus("current")
_PcoipGenDevicesUniqueID_Type = OctetString
_PcoipGenDevicesUniqueID_Object = MibTableColumn
pcoipGenDevicesUniqueID = _PcoipGenDevicesUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 10),
    _PcoipGenDevicesUniqueID_Type()
)
pcoipGenDevicesUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesUniqueID.setStatus("current")
_PcoipGenDevicesMAC_Type = OctetString
_PcoipGenDevicesMAC_Object = MibTableColumn
pcoipGenDevicesMAC = _PcoipGenDevicesMAC_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 11),
    _PcoipGenDevicesMAC_Type()
)
pcoipGenDevicesMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesMAC.setStatus("current")
_PcoipGenDevicesUptime_Type = Counter64
_PcoipGenDevicesUptime_Object = MibTableColumn
pcoipGenDevicesUptime = _PcoipGenDevicesUptime_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 6, 1, 1, 12),
    _PcoipGenDevicesUptime_Type()
)
pcoipGenDevicesUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipGenDevicesUptime.setStatus("current")
_TeraPcoipImagingDevices_ObjectIdentity = ObjectIdentity
teraPcoipImagingDevices = _TeraPcoipImagingDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7)
)
_PcoipImagingDevicesTable_Object = MibTable
pcoipImagingDevicesTable = _PcoipImagingDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    pcoipImagingDevicesTable.setStatus("current")
_PcoipImagingDevicesEntry_Object = MibTableRow
pcoipImagingDevicesEntry = _PcoipImagingDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1)
)
pcoipImagingDevicesEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipImagingDevicesIndex"),
)
if mibBuilder.loadTexts:
    pcoipImagingDevicesEntry.setStatus("current")


class _PcoipImagingDevicesIndex_Type(Integer32):
    """Custom type pcoipImagingDevicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PcoipImagingDevicesIndex_Type.__name__ = "Integer32"
_PcoipImagingDevicesIndex_Object = MibTableColumn
pcoipImagingDevicesIndex = _PcoipImagingDevicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 1),
    _PcoipImagingDevicesIndex_Type()
)
pcoipImagingDevicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesIndex.setStatus("current")


class _PcoipImagingDevicesSessionNumber_Type(Integer32):
    """Custom type pcoipImagingDevicesSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipImagingDevicesSessionNumber_Type.__name__ = "Integer32"
_PcoipImagingDevicesSessionNumber_Object = MibTableColumn
pcoipImagingDevicesSessionNumber = _PcoipImagingDevicesSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 2),
    _PcoipImagingDevicesSessionNumber_Type()
)
pcoipImagingDevicesSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesSessionNumber.setStatus("current")


class _PcoipImagingDevicesDisplayWidth_Type(Integer32):
    """Custom type pcoipImagingDevicesDisplayWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PcoipImagingDevicesDisplayWidth_Type.__name__ = "Integer32"
_PcoipImagingDevicesDisplayWidth_Object = MibTableColumn
pcoipImagingDevicesDisplayWidth = _PcoipImagingDevicesDisplayWidth_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 3),
    _PcoipImagingDevicesDisplayWidth_Type()
)
pcoipImagingDevicesDisplayWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDisplayWidth.setStatus("current")


class _PcoipImagingDevicesDisplayHeight_Type(Integer32):
    """Custom type pcoipImagingDevicesDisplayHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_PcoipImagingDevicesDisplayHeight_Type.__name__ = "Integer32"
_PcoipImagingDevicesDisplayHeight_Object = MibTableColumn
pcoipImagingDevicesDisplayHeight = _PcoipImagingDevicesDisplayHeight_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 4),
    _PcoipImagingDevicesDisplayHeight_Type()
)
pcoipImagingDevicesDisplayHeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDisplayHeight.setStatus("current")


class _PcoipImagingDevicesDisplayRefreshRate_Type(Integer32):
    """Custom type pcoipImagingDevicesDisplayRefreshRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PcoipImagingDevicesDisplayRefreshRate_Type.__name__ = "Integer32"
_PcoipImagingDevicesDisplayRefreshRate_Object = MibTableColumn
pcoipImagingDevicesDisplayRefreshRate = _PcoipImagingDevicesDisplayRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 5),
    _PcoipImagingDevicesDisplayRefreshRate_Type()
)
pcoipImagingDevicesDisplayRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDisplayRefreshRate.setStatus("current")


class _PcoipImagingDevicesDisplayChangeRate_Type(Integer32):
    """Custom type pcoipImagingDevicesDisplayChangeRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PcoipImagingDevicesDisplayChangeRate_Type.__name__ = "Integer32"
_PcoipImagingDevicesDisplayChangeRate_Object = MibTableColumn
pcoipImagingDevicesDisplayChangeRate = _PcoipImagingDevicesDisplayChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 6),
    _PcoipImagingDevicesDisplayChangeRate_Type()
)
pcoipImagingDevicesDisplayChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDisplayChangeRate.setStatus("current")


class _PcoipImagingDevicesDisplayProcessRate_Type(Integer32):
    """Custom type pcoipImagingDevicesDisplayProcessRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PcoipImagingDevicesDisplayProcessRate_Type.__name__ = "Integer32"
_PcoipImagingDevicesDisplayProcessRate_Object = MibTableColumn
pcoipImagingDevicesDisplayProcessRate = _PcoipImagingDevicesDisplayProcessRate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 7),
    _PcoipImagingDevicesDisplayProcessRate_Type()
)
pcoipImagingDevicesDisplayProcessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDisplayProcessRate.setStatus("current")
_PcoipImagingDevicesLimitReason_Type = OctetString
_PcoipImagingDevicesLimitReason_Object = MibTableColumn
pcoipImagingDevicesLimitReason = _PcoipImagingDevicesLimitReason_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 8),
    _PcoipImagingDevicesLimitReason_Type()
)
pcoipImagingDevicesLimitReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesLimitReason.setStatus("current")
_PcoipImagingDevicesModel_Type = OctetString
_PcoipImagingDevicesModel_Object = MibTableColumn
pcoipImagingDevicesModel = _PcoipImagingDevicesModel_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 9),
    _PcoipImagingDevicesModel_Type()
)
pcoipImagingDevicesModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesModel.setStatus("current")
_PcoipImagingDevicesStatus_Type = OctetString
_PcoipImagingDevicesStatus_Object = MibTableColumn
pcoipImagingDevicesStatus = _PcoipImagingDevicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 10),
    _PcoipImagingDevicesStatus_Type()
)
pcoipImagingDevicesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesStatus.setStatus("current")
_PcoipImagingDevicesMode_Type = OctetString
_PcoipImagingDevicesMode_Object = MibTableColumn
pcoipImagingDevicesMode = _PcoipImagingDevicesMode_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 11),
    _PcoipImagingDevicesMode_Type()
)
pcoipImagingDevicesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesMode.setStatus("current")
_PcoipImagingDevicesSerial_Type = OctetString
_PcoipImagingDevicesSerial_Object = MibTableColumn
pcoipImagingDevicesSerial = _PcoipImagingDevicesSerial_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 12),
    _PcoipImagingDevicesSerial_Type()
)
pcoipImagingDevicesSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesSerial.setStatus("current")
_PcoipImagingDevicesVID_Type = OctetString
_PcoipImagingDevicesVID_Object = MibTableColumn
pcoipImagingDevicesVID = _PcoipImagingDevicesVID_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 13),
    _PcoipImagingDevicesVID_Type()
)
pcoipImagingDevicesVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesVID.setStatus("current")
_PcoipImagingDevicesPID_Type = OctetString
_PcoipImagingDevicesPID_Object = MibTableColumn
pcoipImagingDevicesPID = _PcoipImagingDevicesPID_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 14),
    _PcoipImagingDevicesPID_Type()
)
pcoipImagingDevicesPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesPID.setStatus("current")
_PcoipImagingDevicesDate_Type = OctetString
_PcoipImagingDevicesDate_Object = MibTableColumn
pcoipImagingDevicesDate = _PcoipImagingDevicesDate_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 7, 1, 1, 15),
    _PcoipImagingDevicesDate_Type()
)
pcoipImagingDevicesDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipImagingDevicesDate.setStatus("current")
_TeraPcoipUSBDevices_ObjectIdentity = ObjectIdentity
teraPcoipUSBDevices = _TeraPcoipUSBDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8)
)
_PcoipUSBDevicesTable_Object = MibTable
pcoipUSBDevicesTable = _PcoipUSBDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pcoipUSBDevicesTable.setStatus("current")
_PcoipUSBDevicesEntry_Object = MibTableRow
pcoipUSBDevicesEntry = _PcoipUSBDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1)
)
pcoipUSBDevicesEntry.setIndexNames(
    (0, "TERADICI-PCOIPv2-MIB", "pcoipUSBDevicesIndex"),
)
if mibBuilder.loadTexts:
    pcoipUSBDevicesEntry.setStatus("current")


class _PcoipUSBDevicesIndex_Type(Integer32):
    """Custom type pcoipUSBDevicesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_PcoipUSBDevicesIndex_Type.__name__ = "Integer32"
_PcoipUSBDevicesIndex_Object = MibTableColumn
pcoipUSBDevicesIndex = _PcoipUSBDevicesIndex_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 1),
    _PcoipUSBDevicesIndex_Type()
)
pcoipUSBDevicesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesIndex.setStatus("current")


class _PcoipUSBDevicesSessionNumber_Type(Integer32):
    """Custom type pcoipUSBDevicesSessionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_PcoipUSBDevicesSessionNumber_Type.__name__ = "Integer32"
_PcoipUSBDevicesSessionNumber_Object = MibTableColumn
pcoipUSBDevicesSessionNumber = _PcoipUSBDevicesSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 2),
    _PcoipUSBDevicesSessionNumber_Type()
)
pcoipUSBDevicesSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesSessionNumber.setStatus("current")
_PcoipUSBDevicesPort_Type = OctetString
_PcoipUSBDevicesPort_Object = MibTableColumn
pcoipUSBDevicesPort = _PcoipUSBDevicesPort_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 3),
    _PcoipUSBDevicesPort_Type()
)
pcoipUSBDevicesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesPort.setStatus("current")
_PcoipUSBDevicesModel_Type = OctetString
_PcoipUSBDevicesModel_Object = MibTableColumn
pcoipUSBDevicesModel = _PcoipUSBDevicesModel_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 4),
    _PcoipUSBDevicesModel_Type()
)
pcoipUSBDevicesModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesModel.setStatus("current")
_PcoipUSBDevicesStatus_Type = OctetString
_PcoipUSBDevicesStatus_Object = MibTableColumn
pcoipUSBDevicesStatus = _PcoipUSBDevicesStatus_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 5),
    _PcoipUSBDevicesStatus_Type()
)
pcoipUSBDevicesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesStatus.setStatus("current")
_PcoipUSBDevicesDeviceClass_Type = OctetString
_PcoipUSBDevicesDeviceClass_Object = MibTableColumn
pcoipUSBDevicesDeviceClass = _PcoipUSBDevicesDeviceClass_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 6),
    _PcoipUSBDevicesDeviceClass_Type()
)
pcoipUSBDevicesDeviceClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesDeviceClass.setStatus("current")
_PcoipUSBDevicesSubClass_Type = OctetString
_PcoipUSBDevicesSubClass_Object = MibTableColumn
pcoipUSBDevicesSubClass = _PcoipUSBDevicesSubClass_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 7),
    _PcoipUSBDevicesSubClass_Type()
)
pcoipUSBDevicesSubClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesSubClass.setStatus("current")
_PcoipUSBDevicesProtocol_Type = OctetString
_PcoipUSBDevicesProtocol_Object = MibTableColumn
pcoipUSBDevicesProtocol = _PcoipUSBDevicesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 8),
    _PcoipUSBDevicesProtocol_Type()
)
pcoipUSBDevicesProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesProtocol.setStatus("current")
_PcoipUSBDevicesSerial_Type = OctetString
_PcoipUSBDevicesSerial_Object = MibTableColumn
pcoipUSBDevicesSerial = _PcoipUSBDevicesSerial_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 9),
    _PcoipUSBDevicesSerial_Type()
)
pcoipUSBDevicesSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesSerial.setStatus("current")
_PcoipUSBDevicesVID_Type = OctetString
_PcoipUSBDevicesVID_Object = MibTableColumn
pcoipUSBDevicesVID = _PcoipUSBDevicesVID_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 10),
    _PcoipUSBDevicesVID_Type()
)
pcoipUSBDevicesVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesVID.setStatus("current")
_PcoipUSBDevicesPID_Type = OctetString
_PcoipUSBDevicesPID_Object = MibTableColumn
pcoipUSBDevicesPID = _PcoipUSBDevicesPID_Object(
    (1, 3, 6, 1, 4, 1, 25071, 1, 2, 8, 1, 1, 11),
    _PcoipUSBDevicesPID_Type()
)
pcoipUSBDevicesPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcoipUSBDevicesPID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERADICI-PCOIPv2-MIB",
    **{"teraMibModule": teraMibModule,
       "teraProducts": teraProducts,
       "teraPcoipV2": teraPcoipV2,
       "teraPcoipGenStats": teraPcoipGenStats,
       "pcoipGenStatsTable": pcoipGenStatsTable,
       "pcoipGenStatsEntry": pcoipGenStatsEntry,
       "pcoipGenStatsSessionNumber": pcoipGenStatsSessionNumber,
       "pcoipGenStatsPacketsSent": pcoipGenStatsPacketsSent,
       "pcoipGenStatsBytesSent": pcoipGenStatsBytesSent,
       "pcoipGenStatsPacketsReceived": pcoipGenStatsPacketsReceived,
       "pcoipGenStatsBytesReceived": pcoipGenStatsBytesReceived,
       "pcoipGenStatsTxPacketsLost": pcoipGenStatsTxPacketsLost,
       "pcoipGenStatsSessionDuration": pcoipGenStatsSessionDuration,
       "teraPcoipNetStats": teraPcoipNetStats,
       "pcoipNetStatsTable": pcoipNetStatsTable,
       "pcoipNetStatsEntry": pcoipNetStatsEntry,
       "pcoipNetStatsSessionNumber": pcoipNetStatsSessionNumber,
       "pcoipNetStatsRoundTripLatencyMs": pcoipNetStatsRoundTripLatencyMs,
       "pcoipNetStatsRXBWkbitPersec": pcoipNetStatsRXBWkbitPersec,
       "pcoipNetStatsRXBWPeakkbitPersec": pcoipNetStatsRXBWPeakkbitPersec,
       "pcoipNetStatsRXPacketLossPercent": pcoipNetStatsRXPacketLossPercent,
       "pcoipNetStatsTXBWkbitPersec": pcoipNetStatsTXBWkbitPersec,
       "pcoipNetStatsTXBWActiveLimitkbitPersec": pcoipNetStatsTXBWActiveLimitkbitPersec,
       "pcoipNetStatsTXBWLimitkbitPersec": pcoipNetStatsTXBWLimitkbitPersec,
       "pcoipNetStatsTXPacketLossPercent": pcoipNetStatsTXPacketLossPercent,
       "teraPcoipAudioStats": teraPcoipAudioStats,
       "pcoipAudioStatsTable": pcoipAudioStatsTable,
       "pcoipAudioStatsEntry": pcoipAudioStatsEntry,
       "pcoipAudioStatsSessionNumber": pcoipAudioStatsSessionNumber,
       "pcoipAudioStatsBytesReceived": pcoipAudioStatsBytesReceived,
       "pcoipAudioStatsBytesSent": pcoipAudioStatsBytesSent,
       "pcoipAudioStatsRXBWkbitPersec": pcoipAudioStatsRXBWkbitPersec,
       "pcoipAudioStatsTXBWkbitPersec": pcoipAudioStatsTXBWkbitPersec,
       "pcoipAudioStatsTXBWLimitkbitPersec": pcoipAudioStatsTXBWLimitkbitPersec,
       "teraPcoipImagingStats": teraPcoipImagingStats,
       "pcoipImagingStatsTable": pcoipImagingStatsTable,
       "pcoipImagingStatsEntry": pcoipImagingStatsEntry,
       "pcoipImagingStatsSessionNumber": pcoipImagingStatsSessionNumber,
       "pcoipImagingStatsBytesReceived": pcoipImagingStatsBytesReceived,
       "pcoipImagingStatsBytesSent": pcoipImagingStatsBytesSent,
       "pcoipImagingStatsRXBWkbitPersec": pcoipImagingStatsRXBWkbitPersec,
       "pcoipImagingStatsTXBWkbitPersec": pcoipImagingStatsTXBWkbitPersec,
       "pcoipImagingStatsEncodedFramesPersec": pcoipImagingStatsEncodedFramesPersec,
       "pcoipImagingStatsActiveMinimumQuality": pcoipImagingStatsActiveMinimumQuality,
       "pcoipImagingStatsDecoderCapabilitykbitPersec": pcoipImagingStatsDecoderCapabilitykbitPersec,
       "pcoipImagingStatsPipelineProcRate": pcoipImagingStatsPipelineProcRate,
       "teraPcoipUSBStats": teraPcoipUSBStats,
       "pcoipUSBStatsTable": pcoipUSBStatsTable,
       "pcoipUSBStatsEntry": pcoipUSBStatsEntry,
       "pcoipUSBStatsSessionNumber": pcoipUSBStatsSessionNumber,
       "pcoipUSBStatsBytesReceived": pcoipUSBStatsBytesReceived,
       "pcoipUSBStatsBytesSent": pcoipUSBStatsBytesSent,
       "pcoipUSBStatsRXBWkbitPersec": pcoipUSBStatsRXBWkbitPersec,
       "pcoipUSBStatsTXBWkbitPersec": pcoipUSBStatsTXBWkbitPersec,
       "teraPcoipGenDevices": teraPcoipGenDevices,
       "pcoipGenDevicesTable": pcoipGenDevicesTable,
       "pcoipGenDevicesEntry": pcoipGenDevicesEntry,
       "pcoipGenDevicesSessionNumber": pcoipGenDevicesSessionNumber,
       "pcoipGenDevicesName": pcoipGenDevicesName,
       "pcoipGenDevicesDescription": pcoipGenDevicesDescription,
       "pcoipGenDevicesGenericTag": pcoipGenDevicesGenericTag,
       "pcoipGenDevicesPartNumber": pcoipGenDevicesPartNumber,
       "pcoipGenDevicesFwPartNumber": pcoipGenDevicesFwPartNumber,
       "pcoipGenDevicesSerialNumber": pcoipGenDevicesSerialNumber,
       "pcoipGenDevicesHardwareVersion": pcoipGenDevicesHardwareVersion,
       "pcoipGenDevicesFirmwareVersion": pcoipGenDevicesFirmwareVersion,
       "pcoipGenDevicesUniqueID": pcoipGenDevicesUniqueID,
       "pcoipGenDevicesMAC": pcoipGenDevicesMAC,
       "pcoipGenDevicesUptime": pcoipGenDevicesUptime,
       "teraPcoipImagingDevices": teraPcoipImagingDevices,
       "pcoipImagingDevicesTable": pcoipImagingDevicesTable,
       "pcoipImagingDevicesEntry": pcoipImagingDevicesEntry,
       "pcoipImagingDevicesIndex": pcoipImagingDevicesIndex,
       "pcoipImagingDevicesSessionNumber": pcoipImagingDevicesSessionNumber,
       "pcoipImagingDevicesDisplayWidth": pcoipImagingDevicesDisplayWidth,
       "pcoipImagingDevicesDisplayHeight": pcoipImagingDevicesDisplayHeight,
       "pcoipImagingDevicesDisplayRefreshRate": pcoipImagingDevicesDisplayRefreshRate,
       "pcoipImagingDevicesDisplayChangeRate": pcoipImagingDevicesDisplayChangeRate,
       "pcoipImagingDevicesDisplayProcessRate": pcoipImagingDevicesDisplayProcessRate,
       "pcoipImagingDevicesLimitReason": pcoipImagingDevicesLimitReason,
       "pcoipImagingDevicesModel": pcoipImagingDevicesModel,
       "pcoipImagingDevicesStatus": pcoipImagingDevicesStatus,
       "pcoipImagingDevicesMode": pcoipImagingDevicesMode,
       "pcoipImagingDevicesSerial": pcoipImagingDevicesSerial,
       "pcoipImagingDevicesVID": pcoipImagingDevicesVID,
       "pcoipImagingDevicesPID": pcoipImagingDevicesPID,
       "pcoipImagingDevicesDate": pcoipImagingDevicesDate,
       "teraPcoipUSBDevices": teraPcoipUSBDevices,
       "pcoipUSBDevicesTable": pcoipUSBDevicesTable,
       "pcoipUSBDevicesEntry": pcoipUSBDevicesEntry,
       "pcoipUSBDevicesIndex": pcoipUSBDevicesIndex,
       "pcoipUSBDevicesSessionNumber": pcoipUSBDevicesSessionNumber,
       "pcoipUSBDevicesPort": pcoipUSBDevicesPort,
       "pcoipUSBDevicesModel": pcoipUSBDevicesModel,
       "pcoipUSBDevicesStatus": pcoipUSBDevicesStatus,
       "pcoipUSBDevicesDeviceClass": pcoipUSBDevicesDeviceClass,
       "pcoipUSBDevicesSubClass": pcoipUSBDevicesSubClass,
       "pcoipUSBDevicesProtocol": pcoipUSBDevicesProtocol,
       "pcoipUSBDevicesSerial": pcoipUSBDevicesSerial,
       "pcoipUSBDevicesVID": pcoipUSBDevicesVID,
       "pcoipUSBDevicesPID": pcoipUSBDevicesPID}
)
