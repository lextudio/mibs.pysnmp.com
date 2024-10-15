# SNMP MIB module (H320ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H320ENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:38 2024
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

(MmTerminalAudioCapability,
 MmTerminalDataCapability,
 MmTerminalLineRateCapability,
 MmTerminalVideoCapability,
 mmH320Root) = mibBuilder.importSymbols(
    "MULTI-MEDIA-MIB-TC",
    "MmTerminalAudioCapability",
    "MmTerminalDataCapability",
    "MmTerminalLineRateCapability",
    "MmTerminalVideoCapability",
    "mmH320Root")

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

h320Entity = ModuleIdentity(
    (0, 0, 8, 341, 1, 2, 1)
)
h320Entity.setRevisions(
        ("1998-12-18 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H320Capability_ObjectIdentity = ObjectIdentity
h320Capability = _H320Capability_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 1)
)
_H320CapsTable_Object = MibTable
h320CapsTable = _H320CapsTable_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h320CapsTable.setStatus("current")
_H320CapsEntry_Object = MibTableRow
h320CapsEntry = _H320CapsEntry_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1)
)
h320CapsEntry.setIndexNames(
    (0, "H320ENTITY-MIB", "terminalIndex"),
)
if mibBuilder.loadTexts:
    h320CapsEntry.setStatus("current")


class _TerminalIndex_Type(Integer32):
    """Custom type terminalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TerminalIndex_Type.__name__ = "Integer32"
_TerminalIndex_Object = MibTableColumn
terminalIndex = _TerminalIndex_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 1),
    _TerminalIndex_Type()
)
terminalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    terminalIndex.setStatus("current")
_H320CapsEntityLineRate_Type = MmTerminalLineRateCapability
_H320CapsEntityLineRate_Object = MibTableColumn
h320CapsEntityLineRate = _H320CapsEntityLineRate_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 2),
    _H320CapsEntityLineRate_Type()
)
h320CapsEntityLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityLineRate.setStatus("current")
_H320CapsEntityVideoFormats_Type = MmTerminalVideoCapability
_H320CapsEntityVideoFormats_Object = MibTableColumn
h320CapsEntityVideoFormats = _H320CapsEntityVideoFormats_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 3),
    _H320CapsEntityVideoFormats_Type()
)
h320CapsEntityVideoFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityVideoFormats.setStatus("current")
_H320CapsEntityMaxVideoRate_Type = Integer32
_H320CapsEntityMaxVideoRate_Object = MibTableColumn
h320CapsEntityMaxVideoRate = _H320CapsEntityMaxVideoRate_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 4),
    _H320CapsEntityMaxVideoRate_Type()
)
h320CapsEntityMaxVideoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityMaxVideoRate.setStatus("current")
_H320CapsEntityAudioTypes_Type = MmTerminalAudioCapability
_H320CapsEntityAudioTypes_Object = MibTableColumn
h320CapsEntityAudioTypes = _H320CapsEntityAudioTypes_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 5),
    _H320CapsEntityAudioTypes_Type()
)
h320CapsEntityAudioTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityAudioTypes.setStatus("current")
_H320CapsEntityDataCaps_Type = MmTerminalDataCapability
_H320CapsEntityDataCaps_Object = MibTableColumn
h320CapsEntityDataCaps = _H320CapsEntityDataCaps_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 6),
    _H320CapsEntityDataCaps_Type()
)
h320CapsEntityDataCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityDataCaps.setStatus("current")
_H320CapsEntityEncryp_Type = Integer32
_H320CapsEntityEncryp_Object = MibTableColumn
h320CapsEntityEncryp = _H320CapsEntityEncryp_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 7),
    _H320CapsEntityEncryp_Type()
)
h320CapsEntityEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntityEncryp.setStatus("current")
_H320CapsEntryRDC_Type = Integer32
_H320CapsEntryRDC_Object = MibTableColumn
h320CapsEntryRDC = _H320CapsEntryRDC_Object(
    (0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 8),
    _H320CapsEntryRDC_Type()
)
h320CapsEntryRDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CapsEntryRDC.setStatus("current")
_H320CallStatus_ObjectIdentity = ObjectIdentity
h320CallStatus = _H320CallStatus_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 2)
)
_H320CallStatusTable_Object = MibTable
h320CallStatusTable = _H320CallStatusTable_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h320CallStatusTable.setStatus("current")
_H320CallStatusEntry_Object = MibTableRow
h320CallStatusEntry = _H320CallStatusEntry_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    h320CallStatusEntry.setStatus("current")


class _H320CallCurrentCallStatus_Type(Integer32):
    """Custom type h320CallCurrentCallStatus based on Integer32"""
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
        *(("connected", 3),
          ("connecting", 2),
          ("disconnected", 5),
          ("disconnecting", 4),
          ("idle", 1))
    )


_H320CallCurrentCallStatus_Type.__name__ = "Integer32"
_H320CallCurrentCallStatus_Object = MibTableColumn
h320CallCurrentCallStatus = _H320CallCurrentCallStatus_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 1),
    _H320CallCurrentCallStatus_Type()
)
h320CallCurrentCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallCurrentCallStatus.setStatus("current")


class _H320CallSiteName_Type(DisplayString):
    """Custom type h320CallSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H320CallSiteName_Type.__name__ = "DisplayString"
_H320CallSiteName_Object = MibTableColumn
h320CallSiteName = _H320CallSiteName_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 2),
    _H320CallSiteName_Type()
)
h320CallSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallSiteName.setStatus("current")
_H320CallLineRate_Type = MmTerminalLineRateCapability
_H320CallLineRate_Object = MibTableColumn
h320CallLineRate = _H320CallLineRate_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 3),
    _H320CallLineRate_Type()
)
h320CallLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallLineRate.setStatus("current")
_H320CallVideoInFormat_Type = MmTerminalVideoCapability
_H320CallVideoInFormat_Object = MibTableColumn
h320CallVideoInFormat = _H320CallVideoInFormat_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 4),
    _H320CallVideoInFormat_Type()
)
h320CallVideoInFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallVideoInFormat.setStatus("current")
_H320CallVideoOutFormat_Type = MmTerminalVideoCapability
_H320CallVideoOutFormat_Object = MibTableColumn
h320CallVideoOutFormat = _H320CallVideoOutFormat_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 5),
    _H320CallVideoOutFormat_Type()
)
h320CallVideoOutFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallVideoOutFormat.setStatus("current")
_H320CallAudioInFormat_Type = MmTerminalAudioCapability
_H320CallAudioInFormat_Object = MibTableColumn
h320CallAudioInFormat = _H320CallAudioInFormat_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 6),
    _H320CallAudioInFormat_Type()
)
h320CallAudioInFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallAudioInFormat.setStatus("current")
_H320CallAudioOutFormat_Type = MmTerminalAudioCapability
_H320CallAudioOutFormat_Object = MibTableColumn
h320CallAudioOutFormat = _H320CallAudioOutFormat_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 7),
    _H320CallAudioOutFormat_Type()
)
h320CallAudioOutFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallAudioOutFormat.setStatus("current")
_H320CallData_Type = MmTerminalDataCapability
_H320CallData_Object = MibTableColumn
h320CallData = _H320CallData_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 8),
    _H320CallData_Type()
)
h320CallData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallData.setStatus("current")


class _H320CallEncryp_Type(Integer32):
    """Custom type h320CallEncryp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h233", 2),
          ("other", 1))
    )


_H320CallEncryp_Type.__name__ = "Integer32"
_H320CallEncryp_Object = MibTableColumn
h320CallEncryp = _H320CallEncryp_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 9),
    _H320CallEncryp_Type()
)
h320CallEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallEncryp.setStatus("current")


class _H320CallRDC_Type(Integer32):
    """Custom type h320CallRDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h281FECC", 2),
          ("other", 1))
    )


_H320CallRDC_Type.__name__ = "Integer32"
_H320CallRDC_Object = MibTableColumn
h320CallRDC = _H320CallRDC_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 10),
    _H320CallRDC_Type()
)
h320CallRDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallRDC.setStatus("current")


class _H221CallStatusHangUpDirection_Type(Integer32):
    """Custom type h221CallStatusHangUpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("farEnd", 3),
          ("nearEndSystem", 2),
          ("nearEndUser", 1))
    )


_H221CallStatusHangUpDirection_Type.__name__ = "Integer32"
_H221CallStatusHangUpDirection_Object = MibTableColumn
h221CallStatusHangUpDirection = _H221CallStatusHangUpDirection_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 11),
    _H221CallStatusHangUpDirection_Type()
)
h221CallStatusHangUpDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221CallStatusHangUpDirection.setStatus("current")


class _H221CallStatusQ850Cause_Type(Integer32):
    """Custom type h221CallStatusQ850Cause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H221CallStatusQ850Cause_Type.__name__ = "Integer32"
_H221CallStatusQ850Cause_Object = MibTableColumn
h221CallStatusQ850Cause = _H221CallStatusQ850Cause_Object(
    (0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 12),
    _H221CallStatusQ850Cause_Type()
)
h221CallStatusQ850Cause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221CallStatusQ850Cause.setStatus("current")
_H320H221Stats_ObjectIdentity = ObjectIdentity
h320H221Stats = _H320H221Stats_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 3)
)
_H221ChannelStatsTable_Object = MibTable
h221ChannelStatsTable = _H221ChannelStatsTable_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h221ChannelStatsTable.setStatus("current")
_H221ChannelStatsEntry_Object = MibTableRow
h221ChannelStatsEntry = _H221ChannelStatsEntry_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h221ChannelStatsEntry.setStatus("current")


class _NumberofConnections_Type(Integer32):
    """Custom type numberofConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NumberofConnections_Type.__name__ = "Integer32"
_NumberofConnections_Object = MibTableColumn
numberofConnections = _NumberofConnections_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 1),
    _NumberofConnections_Type()
)
numberofConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberofConnections.setStatus("current")
_H221StatsInVideoFrames_Type = Counter32
_H221StatsInVideoFrames_Object = MibTableColumn
h221StatsInVideoFrames = _H221StatsInVideoFrames_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 2),
    _H221StatsInVideoFrames_Type()
)
h221StatsInVideoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInVideoFrames.setStatus("current")
_H221StatsInVideoFramesCorrectableErrs_Type = Counter32
_H221StatsInVideoFramesCorrectableErrs_Object = MibTableColumn
h221StatsInVideoFramesCorrectableErrs = _H221StatsInVideoFramesCorrectableErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 3),
    _H221StatsInVideoFramesCorrectableErrs_Type()
)
h221StatsInVideoFramesCorrectableErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInVideoFramesCorrectableErrs.setStatus("current")
_H221StatsInVideoFramesUncorrectableErrs_Type = Counter32
_H221StatsInVideoFramesUncorrectableErrs_Object = MibTableColumn
h221StatsInVideoFramesUncorrectableErrs = _H221StatsInVideoFramesUncorrectableErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 4),
    _H221StatsInVideoFramesUncorrectableErrs_Type()
)
h221StatsInVideoFramesUncorrectableErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInVideoFramesUncorrectableErrs.setStatus("current")
_H221StatsOutVCU_Type = Counter32
_H221StatsOutVCU_Object = MibTableColumn
h221StatsOutVCU = _H221StatsOutVCU_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 5),
    _H221StatsOutVCU_Type()
)
h221StatsOutVCU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsOutVCU.setStatus("current")
_H221ConnectionStatsTable_Object = MibTable
h221ConnectionStatsTable = _H221ConnectionStatsTable_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h221ConnectionStatsTable.setStatus("current")
_H221ConnectionStatsEntry_Object = MibTableRow
h221ConnectionStatsEntry = _H221ConnectionStatsEntry_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1)
)
h221ConnectionStatsEntry.setIndexNames(
    (0, "H320ENTITY-MIB", "terminalIndex"),
    (0, "H320ENTITY-MIB", "connectionIndex"),
)
if mibBuilder.loadTexts:
    h221ConnectionStatsEntry.setStatus("current")


class _ConnectionIndex_Type(Integer32):
    """Custom type connectionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConnectionIndex_Type.__name__ = "Integer32"
_ConnectionIndex_Object = MibTableColumn
connectionIndex = _ConnectionIndex_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 1),
    _ConnectionIndex_Type()
)
connectionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    connectionIndex.setStatus("current")
_H221StatsInFrames_Type = Counter32
_H221StatsInFrames_Object = MibTableColumn
h221StatsInFrames = _H221StatsInFrames_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 2),
    _H221StatsInFrames_Type()
)
h221StatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInFrames.setStatus("current")
_H221StatsOutFrames_Type = Counter32
_H221StatsOutFrames_Object = MibTableColumn
h221StatsOutFrames = _H221StatsOutFrames_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 3),
    _H221StatsOutFrames_Type()
)
h221StatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsOutFrames.setStatus("current")
_H221StatsInFrameErrs_Type = Counter32
_H221StatsInFrameErrs_Object = MibTableColumn
h221StatsInFrameErrs = _H221StatsInFrameErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 4),
    _H221StatsInFrameErrs_Type()
)
h221StatsInFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInFrameErrs.setStatus("current")
_H221StatsFrameAlignmentErrs_Type = Counter32
_H221StatsFrameAlignmentErrs_Object = MibTableColumn
h221StatsFrameAlignmentErrs = _H221StatsFrameAlignmentErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 5),
    _H221StatsFrameAlignmentErrs_Type()
)
h221StatsFrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsFrameAlignmentErrs.setStatus("current")
_H221StatsMultiFrameAlignmentErrs_Type = Counter32
_H221StatsMultiFrameAlignmentErrs_Object = MibTableColumn
h221StatsMultiFrameAlignmentErrs = _H221StatsMultiFrameAlignmentErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 6),
    _H221StatsMultiFrameAlignmentErrs_Type()
)
h221StatsMultiFrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsMultiFrameAlignmentErrs.setStatus("current")


class _H221StatsErrorPerformance_Type(Gauge32):
    """Custom type h221StatsErrorPerformance based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_H221StatsErrorPerformance_Type.__name__ = "Gauge32"
_H221StatsErrorPerformance_Object = MibTableColumn
h221StatsErrorPerformance = _H221StatsErrorPerformance_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 7),
    _H221StatsErrorPerformance_Type()
)
h221StatsErrorPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsErrorPerformance.setStatus("current")
_H221StatsBASErrs_Type = Counter32
_H221StatsBASErrs_Object = MibTableColumn
h221StatsBASErrs = _H221StatsBASErrs_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 8),
    _H221StatsBASErrs_Type()
)
h221StatsBASErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsBASErrs.setStatus("current")
_H221StatsCRC4Err_Type = Counter32
_H221StatsCRC4Err_Object = MibTableColumn
h221StatsCRC4Err = _H221StatsCRC4Err_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 9),
    _H221StatsCRC4Err_Type()
)
h221StatsCRC4Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsCRC4Err.setStatus("current")
_H221StatsInEBit_Type = Counter32
_H221StatsInEBit_Object = MibTableColumn
h221StatsInEBit = _H221StatsInEBit_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 10),
    _H221StatsInEBit_Type()
)
h221StatsInEBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInEBit.setStatus("current")
_H221StatsInopportuneBAS_Type = Counter32
_H221StatsInopportuneBAS_Object = MibTableColumn
h221StatsInopportuneBAS = _H221StatsInopportuneBAS_Object(
    (0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 11),
    _H221StatsInopportuneBAS_Type()
)
h221StatsInopportuneBAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221StatsInopportuneBAS.setStatus("current")
_H320EntityMIBConfs_ObjectIdentity = ObjectIdentity
h320EntityMIBConfs = _H320EntityMIBConfs_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 4)
)
_H320EntityMIBGroups_ObjectIdentity = ObjectIdentity
h320EntityMIBGroups = _H320EntityMIBGroups_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 4, 1)
)
_H320EntityMIBCompl_ObjectIdentity = ObjectIdentity
h320EntityMIBCompl = _H320EntityMIBCompl_ObjectIdentity(
    (0, 0, 8, 341, 1, 2, 1, 4, 2)
)
h320CapsEntry.registerAugmentions(
    ("H320ENTITY-MIB",
     "h320CallStatusEntry")
)
h320CallStatusEntry.setIndexNames(*h320CapsEntry.getIndexNames())
h320CapsEntry.registerAugmentions(
    ("H320ENTITY-MIB",
     "h221ChannelStatsEntry")
)
h221ChannelStatsEntry.setIndexNames(*h320CapsEntry.getIndexNames())

# Managed Objects groups

h320CapsGroups = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 1, 4, 1, 1)
)
h320CapsGroups.setObjects(
      *(("H320ENTITY-MIB", "h320CapsEntityLineRate"),
        ("H320ENTITY-MIB", "h320CapsEntityVideoFormats"),
        ("H320ENTITY-MIB", "h320CapsEntityMaxVideoRate"),
        ("H320ENTITY-MIB", "h320CapsEntityAudioTypes"),
        ("H320ENTITY-MIB", "h320CapsEntityDataCaps"),
        ("H320ENTITY-MIB", "h320CapsEntityEncryp"),
        ("H320ENTITY-MIB", "h320CapsEntryRDC"),
        ("H320ENTITY-MIB", "h221CallStatusHangUpDirection"),
        ("H320ENTITY-MIB", "h221CallStatusQ850Cause"))
)
if mibBuilder.loadTexts:
    h320CapsGroups.setStatus("current")

h320CallStatusGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 1, 4, 1, 2)
)
h320CallStatusGroup.setObjects(
      *(("H320ENTITY-MIB", "h320CallCurrentCallStatus"),
        ("H320ENTITY-MIB", "h320CallSiteName"),
        ("H320ENTITY-MIB", "h320CallLineRate"),
        ("H320ENTITY-MIB", "h320CallVideoInFormat"),
        ("H320ENTITY-MIB", "h320CallVideoOutFormat"),
        ("H320ENTITY-MIB", "h320CallAudioInFormat"),
        ("H320ENTITY-MIB", "h320CallAudioOutFormat"),
        ("H320ENTITY-MIB", "h320CallData"),
        ("H320ENTITY-MIB", "h320CallEncryp"),
        ("H320ENTITY-MIB", "h320CallRDC"))
)
if mibBuilder.loadTexts:
    h320CallStatusGroup.setStatus("current")

h320H221StatsGroup = ObjectGroup(
    (0, 0, 8, 341, 1, 2, 1, 4, 1, 3)
)
h320H221StatsGroup.setObjects(
      *(("H320ENTITY-MIB", "numberofConnections"),
        ("H320ENTITY-MIB", "h221StatsInFrames"),
        ("H320ENTITY-MIB", "h221StatsOutFrames"),
        ("H320ENTITY-MIB", "h221StatsInFrameErrs"),
        ("H320ENTITY-MIB", "h221StatsFrameAlignmentErrs"),
        ("H320ENTITY-MIB", "h221StatsMultiFrameAlignmentErrs"),
        ("H320ENTITY-MIB", "h221StatsErrorPerformance"),
        ("H320ENTITY-MIB", "h221StatsBASErrs"),
        ("H320ENTITY-MIB", "h221StatsInVideoFrames"),
        ("H320ENTITY-MIB", "h221StatsInVideoFramesCorrectableErrs"),
        ("H320ENTITY-MIB", "h221StatsInVideoFramesUncorrectableErrs"),
        ("H320ENTITY-MIB", "h221StatsOutVCU"),
        ("H320ENTITY-MIB", "h221StatsCRC4Err"),
        ("H320ENTITY-MIB", "h221StatsInEBit"),
        ("H320ENTITY-MIB", "h221StatsInopportuneBAS"))
)
if mibBuilder.loadTexts:
    h320H221StatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

h221StatsCompliance = ModuleCompliance(
    (0, 0, 8, 341, 1, 2, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h221StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H320ENTITY-MIB",
    **{"h320Entity": h320Entity,
       "h320Capability": h320Capability,
       "h320CapsTable": h320CapsTable,
       "h320CapsEntry": h320CapsEntry,
       "terminalIndex": terminalIndex,
       "h320CapsEntityLineRate": h320CapsEntityLineRate,
       "h320CapsEntityVideoFormats": h320CapsEntityVideoFormats,
       "h320CapsEntityMaxVideoRate": h320CapsEntityMaxVideoRate,
       "h320CapsEntityAudioTypes": h320CapsEntityAudioTypes,
       "h320CapsEntityDataCaps": h320CapsEntityDataCaps,
       "h320CapsEntityEncryp": h320CapsEntityEncryp,
       "h320CapsEntryRDC": h320CapsEntryRDC,
       "h320CallStatus": h320CallStatus,
       "h320CallStatusTable": h320CallStatusTable,
       "h320CallStatusEntry": h320CallStatusEntry,
       "h320CallCurrentCallStatus": h320CallCurrentCallStatus,
       "h320CallSiteName": h320CallSiteName,
       "h320CallLineRate": h320CallLineRate,
       "h320CallVideoInFormat": h320CallVideoInFormat,
       "h320CallVideoOutFormat": h320CallVideoOutFormat,
       "h320CallAudioInFormat": h320CallAudioInFormat,
       "h320CallAudioOutFormat": h320CallAudioOutFormat,
       "h320CallData": h320CallData,
       "h320CallEncryp": h320CallEncryp,
       "h320CallRDC": h320CallRDC,
       "h221CallStatusHangUpDirection": h221CallStatusHangUpDirection,
       "h221CallStatusQ850Cause": h221CallStatusQ850Cause,
       "h320H221Stats": h320H221Stats,
       "h221ChannelStatsTable": h221ChannelStatsTable,
       "h221ChannelStatsEntry": h221ChannelStatsEntry,
       "numberofConnections": numberofConnections,
       "h221StatsInVideoFrames": h221StatsInVideoFrames,
       "h221StatsInVideoFramesCorrectableErrs": h221StatsInVideoFramesCorrectableErrs,
       "h221StatsInVideoFramesUncorrectableErrs": h221StatsInVideoFramesUncorrectableErrs,
       "h221StatsOutVCU": h221StatsOutVCU,
       "h221ConnectionStatsTable": h221ConnectionStatsTable,
       "h221ConnectionStatsEntry": h221ConnectionStatsEntry,
       "connectionIndex": connectionIndex,
       "h221StatsInFrames": h221StatsInFrames,
       "h221StatsOutFrames": h221StatsOutFrames,
       "h221StatsInFrameErrs": h221StatsInFrameErrs,
       "h221StatsFrameAlignmentErrs": h221StatsFrameAlignmentErrs,
       "h221StatsMultiFrameAlignmentErrs": h221StatsMultiFrameAlignmentErrs,
       "h221StatsErrorPerformance": h221StatsErrorPerformance,
       "h221StatsBASErrs": h221StatsBASErrs,
       "h221StatsCRC4Err": h221StatsCRC4Err,
       "h221StatsInEBit": h221StatsInEBit,
       "h221StatsInopportuneBAS": h221StatsInopportuneBAS,
       "h320EntityMIBConfs": h320EntityMIBConfs,
       "h320EntityMIBGroups": h320EntityMIBGroups,
       "h320CapsGroups": h320CapsGroups,
       "h320CallStatusGroup": h320CallStatusGroup,
       "h320H221StatsGroup": h320H221StatsGroup,
       "h320EntityMIBCompl": h320EntityMIBCompl,
       "h221StatsCompliance": h221StatsCompliance}
)
