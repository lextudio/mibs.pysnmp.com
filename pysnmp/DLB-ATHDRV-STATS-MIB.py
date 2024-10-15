# SNMP MIB module (DLB-ATHDRV-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLB-ATHDRV-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:34 2024
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

(dlbMgmt,) = mibBuilder.importSymbols(
    "DELIBERANT-MIB",
    "dlbMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

dlbAthDrvStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7)
)
dlbAthDrvStatsMIB.setRevisions(
        ("2008-12-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DlbAthDrvStatsMIBObjects_ObjectIdentity = ObjectIdentity
dlbAthDrvStatsMIBObjects = _DlbAthDrvStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1)
)
_DlbAthStatsTable_Object = MibTable
dlbAthStatsTable = _DlbAthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    dlbAthStatsTable.setStatus("current")
_DlbAthStatsEntry_Object = MibTableRow
dlbAthStatsEntry = _DlbAthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1)
)
dlbAthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbAthStatsEntry.setStatus("current")
_DlbAthWatchdogTimeouts_Type = Counter32
_DlbAthWatchdogTimeouts_Object = MibTableColumn
dlbAthWatchdogTimeouts = _DlbAthWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 1),
    _DlbAthWatchdogTimeouts_Type()
)
dlbAthWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthWatchdogTimeouts.setStatus("current")
_DlbAthHardwareErrorInterrupts_Type = Counter32
_DlbAthHardwareErrorInterrupts_Object = MibTableColumn
dlbAthHardwareErrorInterrupts = _DlbAthHardwareErrorInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 2),
    _DlbAthHardwareErrorInterrupts_Type()
)
dlbAthHardwareErrorInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthHardwareErrorInterrupts.setStatus("current")
_DlbAthBeaconMissInterrupts_Type = Counter32
_DlbAthBeaconMissInterrupts_Object = MibTableColumn
dlbAthBeaconMissInterrupts = _DlbAthBeaconMissInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 3),
    _DlbAthBeaconMissInterrupts_Type()
)
dlbAthBeaconMissInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthBeaconMissInterrupts.setStatus("current")
_DlbAthRecvOverrunInterrupts_Type = Counter32
_DlbAthRecvOverrunInterrupts_Object = MibTableColumn
dlbAthRecvOverrunInterrupts = _DlbAthRecvOverrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 4),
    _DlbAthRecvOverrunInterrupts_Type()
)
dlbAthRecvOverrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRecvOverrunInterrupts.setStatus("current")
_DlbAthRecvEolInterrupts_Type = Counter32
_DlbAthRecvEolInterrupts_Object = MibTableColumn
dlbAthRecvEolInterrupts = _DlbAthRecvEolInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 5),
    _DlbAthRecvEolInterrupts_Type()
)
dlbAthRecvEolInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRecvEolInterrupts.setStatus("current")
_DlbAthTxmitUnderrunInterrupts_Type = Counter32
_DlbAthTxmitUnderrunInterrupts_Object = MibTableColumn
dlbAthTxmitUnderrunInterrupts = _DlbAthTxmitUnderrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 6),
    _DlbAthTxmitUnderrunInterrupts_Type()
)
dlbAthTxmitUnderrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxmitUnderrunInterrupts.setStatus("current")
_DlbAthTxManagementFrames_Type = Counter32
_DlbAthTxManagementFrames_Object = MibTableColumn
dlbAthTxManagementFrames = _DlbAthTxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 7),
    _DlbAthTxManagementFrames_Type()
)
dlbAthTxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxManagementFrames.setStatus("current")
_DlbAthTxFramesDiscQueueDepth_Type = Counter32
_DlbAthTxFramesDiscQueueDepth_Object = MibTableColumn
dlbAthTxFramesDiscQueueDepth = _DlbAthTxFramesDiscQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 8),
    _DlbAthTxFramesDiscQueueDepth_Type()
)
dlbAthTxFramesDiscQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesDiscQueueDepth.setStatus("current")
_DlbAthTxFramesDiscDeviceGone_Type = Counter32
_DlbAthTxFramesDiscDeviceGone_Object = MibTableColumn
dlbAthTxFramesDiscDeviceGone = _DlbAthTxFramesDiscDeviceGone_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 9),
    _DlbAthTxFramesDiscDeviceGone_Type()
)
dlbAthTxFramesDiscDeviceGone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesDiscDeviceGone.setStatus("current")
_DlbAthTxQueueFull_Type = Counter32
_DlbAthTxQueueFull_Object = MibTableColumn
dlbAthTxQueueFull = _DlbAthTxQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 10),
    _DlbAthTxQueueFull_Type()
)
dlbAthTxQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxQueueFull.setStatus("current")
_DlbAthTxEncapsulationFailed_Type = Counter32
_DlbAthTxEncapsulationFailed_Object = MibTableColumn
dlbAthTxEncapsulationFailed = _DlbAthTxEncapsulationFailed_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 11),
    _DlbAthTxEncapsulationFailed_Type()
)
dlbAthTxEncapsulationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxEncapsulationFailed.setStatus("current")
_DlbAthTxFailedNoNode_Type = Counter32
_DlbAthTxFailedNoNode_Object = MibTableColumn
dlbAthTxFailedNoNode = _DlbAthTxFailedNoNode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 12),
    _DlbAthTxFailedNoNode_Type()
)
dlbAthTxFailedNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedNoNode.setStatus("current")
_DlbAthTxFailedNoDataTxBuffer_Type = Counter32
_DlbAthTxFailedNoDataTxBuffer_Object = MibTableColumn
dlbAthTxFailedNoDataTxBuffer = _DlbAthTxFailedNoDataTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 13),
    _DlbAthTxFailedNoDataTxBuffer_Type()
)
dlbAthTxFailedNoDataTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedNoDataTxBuffer.setStatus("current")
_DlbAthTxFailedNoMgtTxBuffer_Type = Counter32
_DlbAthTxFailedNoMgtTxBuffer_Object = MibTableColumn
dlbAthTxFailedNoMgtTxBuffer = _DlbAthTxFailedNoMgtTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 14),
    _DlbAthTxFailedNoMgtTxBuffer_Type()
)
dlbAthTxFailedNoMgtTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedNoMgtTxBuffer.setStatus("current")
_DlbAthTxFailedTooManyRetries_Type = Counter32
_DlbAthTxFailedTooManyRetries_Object = MibTableColumn
dlbAthTxFailedTooManyRetries = _DlbAthTxFailedTooManyRetries_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 15),
    _DlbAthTxFailedTooManyRetries_Type()
)
dlbAthTxFailedTooManyRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedTooManyRetries.setStatus("current")
_DlbAthTxFailedFifoUnderrun_Type = Counter32
_DlbAthTxFailedFifoUnderrun_Object = MibTableColumn
dlbAthTxFailedFifoUnderrun = _DlbAthTxFailedFifoUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 16),
    _DlbAthTxFailedFifoUnderrun_Type()
)
dlbAthTxFailedFifoUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedFifoUnderrun.setStatus("current")
_DlbAthTxFailedXmitFiltered_Type = Counter32
_DlbAthTxFailedXmitFiltered_Object = MibTableColumn
dlbAthTxFailedXmitFiltered = _DlbAthTxFailedXmitFiltered_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 17),
    _DlbAthTxFailedXmitFiltered_Type()
)
dlbAthTxFailedXmitFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedXmitFiltered.setStatus("current")
_DlbAthShortOnchipTxRetries_Type = Counter32
_DlbAthShortOnchipTxRetries_Object = MibTableColumn
dlbAthShortOnchipTxRetries = _DlbAthShortOnchipTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 18),
    _DlbAthShortOnchipTxRetries_Type()
)
dlbAthShortOnchipTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthShortOnchipTxRetries.setStatus("current")
_DlbAthLongOnchipTxRetries_Type = Counter32
_DlbAthLongOnchipTxRetries_Object = MibTableColumn
dlbAthLongOnchipTxRetries = _DlbAthLongOnchipTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 19),
    _DlbAthLongOnchipTxRetries_Type()
)
dlbAthLongOnchipTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthLongOnchipTxRetries.setStatus("current")
_DlbAthTxFailedBogusXmitRate_Type = Counter32
_DlbAthTxFailedBogusXmitRate_Object = MibTableColumn
dlbAthTxFailedBogusXmitRate = _DlbAthTxFailedBogusXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 20),
    _DlbAthTxFailedBogusXmitRate_Type()
)
dlbAthTxFailedBogusXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFailedBogusXmitRate.setStatus("current")
_DlbAthTxFramesNoAckMarked_Type = Counter32
_DlbAthTxFramesNoAckMarked_Object = MibTableColumn
dlbAthTxFramesNoAckMarked = _DlbAthTxFramesNoAckMarked_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 21),
    _DlbAthTxFramesNoAckMarked_Type()
)
dlbAthTxFramesNoAckMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesNoAckMarked.setStatus("current")
_DlbAthTxFramesRtsEnabled_Type = Counter32
_DlbAthTxFramesRtsEnabled_Object = MibTableColumn
dlbAthTxFramesRtsEnabled = _DlbAthTxFramesRtsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 22),
    _DlbAthTxFramesRtsEnabled_Type()
)
dlbAthTxFramesRtsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesRtsEnabled.setStatus("current")
_DlbAthTxFramesCtsEnabled_Type = Counter32
_DlbAthTxFramesCtsEnabled_Object = MibTableColumn
dlbAthTxFramesCtsEnabled = _DlbAthTxFramesCtsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 23),
    _DlbAthTxFramesCtsEnabled_Type()
)
dlbAthTxFramesCtsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesCtsEnabled.setStatus("current")
_DlbAthTxFramesShortPreamble_Type = Counter32
_DlbAthTxFramesShortPreamble_Object = MibTableColumn
dlbAthTxFramesShortPreamble = _DlbAthTxFramesShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 24),
    _DlbAthTxFramesShortPreamble_Type()
)
dlbAthTxFramesShortPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesShortPreamble.setStatus("current")
_DlbAthTxFramesAlternateRate_Type = Counter32
_DlbAthTxFramesAlternateRate_Object = MibTableColumn
dlbAthTxFramesAlternateRate = _DlbAthTxFramesAlternateRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 25),
    _DlbAthTxFramesAlternateRate_Type()
)
dlbAthTxFramesAlternateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesAlternateRate.setStatus("current")
_DlbAthTxFrames11gProtection_Type = Counter32
_DlbAthTxFrames11gProtection_Object = MibTableColumn
dlbAthTxFrames11gProtection = _DlbAthTxFrames11gProtection_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 26),
    _DlbAthTxFrames11gProtection_Type()
)
dlbAthTxFrames11gProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFrames11gProtection.setStatus("current")
_DlbAthRxFailedDescOverrun_Type = Counter32
_DlbAthRxFailedDescOverrun_Object = MibTableColumn
dlbAthRxFailedDescOverrun = _DlbAthRxFailedDescOverrun_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 27),
    _DlbAthRxFailedDescOverrun_Type()
)
dlbAthRxFailedDescOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedDescOverrun.setStatus("current")
_DlbAthRxFailedBadCrc_Type = Counter32
_DlbAthRxFailedBadCrc_Object = MibTableColumn
dlbAthRxFailedBadCrc = _DlbAthRxFailedBadCrc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 28),
    _DlbAthRxFailedBadCrc_Type()
)
dlbAthRxFailedBadCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedBadCrc.setStatus("current")
_DlbAthRxFailedFifoOverrun_Type = Counter32
_DlbAthRxFailedFifoOverrun_Object = MibTableColumn
dlbAthRxFailedFifoOverrun = _DlbAthRxFailedFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 29),
    _DlbAthRxFailedFifoOverrun_Type()
)
dlbAthRxFailedFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedFifoOverrun.setStatus("current")
_DlbAthRxFailedDecryptErrors_Type = Counter32
_DlbAthRxFailedDecryptErrors_Object = MibTableColumn
dlbAthRxFailedDecryptErrors = _DlbAthRxFailedDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 30),
    _DlbAthRxFailedDecryptErrors_Type()
)
dlbAthRxFailedDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedDecryptErrors.setStatus("current")
_DlbAthRxFailedMicFailure_Type = Counter32
_DlbAthRxFailedMicFailure_Object = MibTableColumn
dlbAthRxFailedMicFailure = _DlbAthRxFailedMicFailure_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 31),
    _DlbAthRxFailedMicFailure_Type()
)
dlbAthRxFailedMicFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedMicFailure.setStatus("current")
_DlbAthRxFailedFrameTooShort_Type = Counter32
_DlbAthRxFailedFrameTooShort_Object = MibTableColumn
dlbAthRxFailedFrameTooShort = _DlbAthRxFailedFrameTooShort_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 32),
    _DlbAthRxFailedFrameTooShort_Type()
)
dlbAthRxFailedFrameTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFailedFrameTooShort.setStatus("current")
_DlbAthRxSetupFailedNoSkbuff_Type = Counter32
_DlbAthRxSetupFailedNoSkbuff_Object = MibTableColumn
dlbAthRxSetupFailedNoSkbuff = _DlbAthRxSetupFailedNoSkbuff_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 33),
    _DlbAthRxSetupFailedNoSkbuff_Type()
)
dlbAthRxSetupFailedNoSkbuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxSetupFailedNoSkbuff.setStatus("current")
_DlbAthRxManagementFrames_Type = Counter32
_DlbAthRxManagementFrames_Object = MibTableColumn
dlbAthRxManagementFrames = _DlbAthRxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 34),
    _DlbAthRxManagementFrames_Type()
)
dlbAthRxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxManagementFrames.setStatus("current")
_DlbAthRxControlFrames_Type = Counter32
_DlbAthRxControlFrames_Object = MibTableColumn
dlbAthRxControlFrames = _DlbAthRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 35),
    _DlbAthRxControlFrames_Type()
)
dlbAthRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxControlFrames.setStatus("current")
_DlbAthNoSkbuffForBeacon_Type = Counter32
_DlbAthNoSkbuffForBeacon_Object = MibTableColumn
dlbAthNoSkbuffForBeacon = _DlbAthNoSkbuffForBeacon_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 36),
    _DlbAthNoSkbuffForBeacon_Type()
)
dlbAthNoSkbuffForBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthNoSkbuffForBeacon.setStatus("current")
_DlbAthBeaconsTransmitted_Type = Counter32
_DlbAthBeaconsTransmitted_Object = MibTableColumn
dlbAthBeaconsTransmitted = _DlbAthBeaconsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 37),
    _DlbAthBeaconsTransmitted_Type()
)
dlbAthBeaconsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthBeaconsTransmitted.setStatus("current")
_DlbAthPeriodicCalibrations_Type = Counter32
_DlbAthPeriodicCalibrations_Object = MibTableColumn
dlbAthPeriodicCalibrations = _DlbAthPeriodicCalibrations_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 38),
    _DlbAthPeriodicCalibrations_Type()
)
dlbAthPeriodicCalibrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeriodicCalibrations.setStatus("current")
_DlbAthPeriodicCalibrFailures_Type = Counter32
_DlbAthPeriodicCalibrFailures_Object = MibTableColumn
dlbAthPeriodicCalibrFailures = _DlbAthPeriodicCalibrFailures_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 39),
    _DlbAthPeriodicCalibrFailures_Type()
)
dlbAthPeriodicCalibrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeriodicCalibrFailures.setStatus("current")
_DlbAthRfgainValueChange_Type = Counter32
_DlbAthRfgainValueChange_Object = MibTableColumn
dlbAthRfgainValueChange = _DlbAthRfgainValueChange_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 40),
    _DlbAthRfgainValueChange_Type()
)
dlbAthRfgainValueChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRfgainValueChange.setStatus("current")
_DlbAthRateControlChecks_Type = Counter32
_DlbAthRateControlChecks_Object = MibTableColumn
dlbAthRateControlChecks = _DlbAthRateControlChecks_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 41),
    _DlbAthRateControlChecks_Type()
)
dlbAthRateControlChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRateControlChecks.setStatus("current")
_DlbAthRateCtrlRaisedXmitRate_Type = Counter32
_DlbAthRateCtrlRaisedXmitRate_Object = MibTableColumn
dlbAthRateCtrlRaisedXmitRate = _DlbAthRateCtrlRaisedXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 42),
    _DlbAthRateCtrlRaisedXmitRate_Type()
)
dlbAthRateCtrlRaisedXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRateCtrlRaisedXmitRate.setStatus("current")
_DlbAthRateCtrlDroppedXmitRate_Type = Counter32
_DlbAthRateCtrlDroppedXmitRate_Object = MibTableColumn
dlbAthRateCtrlDroppedXmitRate = _DlbAthRateCtrlDroppedXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 43),
    _DlbAthRateCtrlDroppedXmitRate_Type()
)
dlbAthRateCtrlDroppedXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRateCtrlDroppedXmitRate.setStatus("current")
_DlbAthRssiOfLastAck_Type = Gauge32
_DlbAthRssiOfLastAck_Object = MibTableColumn
dlbAthRssiOfLastAck = _DlbAthRssiOfLastAck_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 44),
    _DlbAthRssiOfLastAck_Type()
)
dlbAthRssiOfLastAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRssiOfLastAck.setStatus("current")
_DlbAthRssiOfLastRcv_Type = Gauge32
_DlbAthRssiOfLastRcv_Object = MibTableColumn
dlbAthRssiOfLastRcv = _DlbAthRssiOfLastRcv_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 1, 1, 45),
    _DlbAthRssiOfLastRcv_Type()
)
dlbAthRssiOfLastRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRssiOfLastRcv.setStatus("current")
_DlbAthPhyErrorsTable_Object = MibTable
dlbAthPhyErrorsTable = _DlbAthPhyErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    dlbAthPhyErrorsTable.setStatus("current")
_DlbAthPhyErrorsEntry_Object = MibTableRow
dlbAthPhyErrorsEntry = _DlbAthPhyErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1)
)
dlbAthPhyErrorsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbAthPhyErrorsEntry.setStatus("current")
_DlbAthPhyTransmitUnderrun_Type = Counter32
_DlbAthPhyTransmitUnderrun_Object = MibTableColumn
dlbAthPhyTransmitUnderrun = _DlbAthPhyTransmitUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 1),
    _DlbAthPhyTransmitUnderrun_Type()
)
dlbAthPhyTransmitUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyTransmitUnderrun.setStatus("current")
_DlbAthPhyTimingError_Type = Counter32
_DlbAthPhyTimingError_Object = MibTableColumn
dlbAthPhyTimingError = _DlbAthPhyTimingError_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 2),
    _DlbAthPhyTimingError_Type()
)
dlbAthPhyTimingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyTimingError.setStatus("current")
_DlbAthPhyIllegalParity_Type = Counter32
_DlbAthPhyIllegalParity_Object = MibTableColumn
dlbAthPhyIllegalParity = _DlbAthPhyIllegalParity_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 3),
    _DlbAthPhyIllegalParity_Type()
)
dlbAthPhyIllegalParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyIllegalParity.setStatus("current")
_DlbAthPhyIllegalRate_Type = Counter32
_DlbAthPhyIllegalRate_Object = MibTableColumn
dlbAthPhyIllegalRate = _DlbAthPhyIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 4),
    _DlbAthPhyIllegalRate_Type()
)
dlbAthPhyIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyIllegalRate.setStatus("current")
_DlbAthPhyIllegalLength_Type = Counter32
_DlbAthPhyIllegalLength_Object = MibTableColumn
dlbAthPhyIllegalLength = _DlbAthPhyIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 5),
    _DlbAthPhyIllegalLength_Type()
)
dlbAthPhyIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyIllegalLength.setStatus("current")
_DlbAthPhyRadarDetect_Type = Counter32
_DlbAthPhyRadarDetect_Object = MibTableColumn
dlbAthPhyRadarDetect = _DlbAthPhyRadarDetect_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 6),
    _DlbAthPhyRadarDetect_Type()
)
dlbAthPhyRadarDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyRadarDetect.setStatus("current")
_DlbAthPhyIllegalService_Type = Counter32
_DlbAthPhyIllegalService_Object = MibTableColumn
dlbAthPhyIllegalService = _DlbAthPhyIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 7),
    _DlbAthPhyIllegalService_Type()
)
dlbAthPhyIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyIllegalService.setStatus("current")
_DlbAthPhyTxmitOverrideRecv_Type = Counter32
_DlbAthPhyTxmitOverrideRecv_Object = MibTableColumn
dlbAthPhyTxmitOverrideRecv = _DlbAthPhyTxmitOverrideRecv_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 8),
    _DlbAthPhyTxmitOverrideRecv_Type()
)
dlbAthPhyTxmitOverrideRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyTxmitOverrideRecv.setStatus("current")
_DlbAthPhyOfdmTiming_Type = Counter32
_DlbAthPhyOfdmTiming_Object = MibTableColumn
dlbAthPhyOfdmTiming = _DlbAthPhyOfdmTiming_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 9),
    _DlbAthPhyOfdmTiming_Type()
)
dlbAthPhyOfdmTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmTiming.setStatus("current")
_DlbAthPhyOfdmIllegalParity_Type = Counter32
_DlbAthPhyOfdmIllegalParity_Object = MibTableColumn
dlbAthPhyOfdmIllegalParity = _DlbAthPhyOfdmIllegalParity_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 10),
    _DlbAthPhyOfdmIllegalParity_Type()
)
dlbAthPhyOfdmIllegalParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmIllegalParity.setStatus("current")
_DlbAthPhyOfdmIllegalRate_Type = Counter32
_DlbAthPhyOfdmIllegalRate_Object = MibTableColumn
dlbAthPhyOfdmIllegalRate = _DlbAthPhyOfdmIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 11),
    _DlbAthPhyOfdmIllegalRate_Type()
)
dlbAthPhyOfdmIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmIllegalRate.setStatus("current")
_DlbAthPhyOfdmIllegalLength_Type = Counter32
_DlbAthPhyOfdmIllegalLength_Object = MibTableColumn
dlbAthPhyOfdmIllegalLength = _DlbAthPhyOfdmIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 12),
    _DlbAthPhyOfdmIllegalLength_Type()
)
dlbAthPhyOfdmIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmIllegalLength.setStatus("current")
_DlbAthPhyOfdmPowerDrop_Type = Counter32
_DlbAthPhyOfdmPowerDrop_Object = MibTableColumn
dlbAthPhyOfdmPowerDrop = _DlbAthPhyOfdmPowerDrop_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 13),
    _DlbAthPhyOfdmPowerDrop_Type()
)
dlbAthPhyOfdmPowerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmPowerDrop.setStatus("current")
_DlbAthPhyOfdmIllegalService_Type = Counter32
_DlbAthPhyOfdmIllegalService_Object = MibTableColumn
dlbAthPhyOfdmIllegalService = _DlbAthPhyOfdmIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 14),
    _DlbAthPhyOfdmIllegalService_Type()
)
dlbAthPhyOfdmIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmIllegalService.setStatus("current")
_DlbAthPhyOfdmRestart_Type = Counter32
_DlbAthPhyOfdmRestart_Object = MibTableColumn
dlbAthPhyOfdmRestart = _DlbAthPhyOfdmRestart_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 15),
    _DlbAthPhyOfdmRestart_Type()
)
dlbAthPhyOfdmRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyOfdmRestart.setStatus("current")
_DlbAthPhyCckTiming_Type = Counter32
_DlbAthPhyCckTiming_Object = MibTableColumn
dlbAthPhyCckTiming = _DlbAthPhyCckTiming_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 16),
    _DlbAthPhyCckTiming_Type()
)
dlbAthPhyCckTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyCckTiming.setStatus("current")
_DlbAthPhyCckHeaderCrc_Type = Counter32
_DlbAthPhyCckHeaderCrc_Object = MibTableColumn
dlbAthPhyCckHeaderCrc = _DlbAthPhyCckHeaderCrc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 17),
    _DlbAthPhyCckHeaderCrc_Type()
)
dlbAthPhyCckHeaderCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyCckHeaderCrc.setStatus("current")
_DlbAthPhyCckIllegalRate_Type = Counter32
_DlbAthPhyCckIllegalRate_Object = MibTableColumn
dlbAthPhyCckIllegalRate = _DlbAthPhyCckIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 18),
    _DlbAthPhyCckIllegalRate_Type()
)
dlbAthPhyCckIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyCckIllegalRate.setStatus("current")
_DlbAthPhyCckIllegalService_Type = Counter32
_DlbAthPhyCckIllegalService_Object = MibTableColumn
dlbAthPhyCckIllegalService = _DlbAthPhyCckIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 19),
    _DlbAthPhyCckIllegalService_Type()
)
dlbAthPhyCckIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyCckIllegalService.setStatus("current")
_DlbAthPhyCckRestart_Type = Counter32
_DlbAthPhyCckRestart_Object = MibTableColumn
dlbAthPhyCckRestart = _DlbAthPhyCckRestart_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 2, 1, 20),
    _DlbAthPhyCckRestart_Type()
)
dlbAthPhyCckRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPhyCckRestart.setStatus("current")
_DlbAthAntennaStatsTable_Object = MibTable
dlbAthAntennaStatsTable = _DlbAthAntennaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    dlbAthAntennaStatsTable.setStatus("current")
_DlbAthAntennaStatsEntry_Object = MibTableRow
dlbAthAntennaStatsEntry = _DlbAthAntennaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1)
)
dlbAthAntennaStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbAthAntennaStatsEntry.setStatus("current")
_DlbAthSwitchedDefaultRxAntenna_Type = Counter32
_DlbAthSwitchedDefaultRxAntenna_Object = MibTableColumn
dlbAthSwitchedDefaultRxAntenna = _DlbAthSwitchedDefaultRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 1),
    _DlbAthSwitchedDefaultRxAntenna_Type()
)
dlbAthSwitchedDefaultRxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthSwitchedDefaultRxAntenna.setStatus("current")
_DlbAthTxUsedAlternateAntenna_Type = Counter32
_DlbAthTxUsedAlternateAntenna_Object = MibTableColumn
dlbAthTxUsedAlternateAntenna = _DlbAthTxUsedAlternateAntenna_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 2),
    _DlbAthTxUsedAlternateAntenna_Type()
)
dlbAthTxUsedAlternateAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxUsedAlternateAntenna.setStatus("current")
_DlbAthTxFramesAntenna1_Type = Counter32
_DlbAthTxFramesAntenna1_Object = MibTableColumn
dlbAthTxFramesAntenna1 = _DlbAthTxFramesAntenna1_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 3),
    _DlbAthTxFramesAntenna1_Type()
)
dlbAthTxFramesAntenna1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesAntenna1.setStatus("current")
_DlbAthRxFramesAntenna1_Type = Counter32
_DlbAthRxFramesAntenna1_Object = MibTableColumn
dlbAthRxFramesAntenna1 = _DlbAthRxFramesAntenna1_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 4),
    _DlbAthRxFramesAntenna1_Type()
)
dlbAthRxFramesAntenna1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFramesAntenna1.setStatus("current")
_DlbAthTxFramesAntenna2_Type = Counter32
_DlbAthTxFramesAntenna2_Object = MibTableColumn
dlbAthTxFramesAntenna2 = _DlbAthTxFramesAntenna2_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 5),
    _DlbAthTxFramesAntenna2_Type()
)
dlbAthTxFramesAntenna2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesAntenna2.setStatus("current")
_DlbAthRxFramesAntenna2_Type = Counter32
_DlbAthRxFramesAntenna2_Object = MibTableColumn
dlbAthRxFramesAntenna2 = _DlbAthRxFramesAntenna2_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 6),
    _DlbAthRxFramesAntenna2_Type()
)
dlbAthRxFramesAntenna2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFramesAntenna2.setStatus("current")
_DlbAthTxFramesAntenna3_Type = Counter32
_DlbAthTxFramesAntenna3_Object = MibTableColumn
dlbAthTxFramesAntenna3 = _DlbAthTxFramesAntenna3_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 7),
    _DlbAthTxFramesAntenna3_Type()
)
dlbAthTxFramesAntenna3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthTxFramesAntenna3.setStatus("current")
_DlbAthRxFramesAntenna3_Type = Counter32
_DlbAthRxFramesAntenna3_Object = MibTableColumn
dlbAthRxFramesAntenna3 = _DlbAthRxFramesAntenna3_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 3, 1, 8),
    _DlbAthRxFramesAntenna3_Type()
)
dlbAthRxFramesAntenna3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthRxFramesAntenna3.setStatus("current")
_DlbAthDot11StatsTable_Object = MibTable
dlbAthDot11StatsTable = _DlbAthDot11StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4)
)
if mibBuilder.loadTexts:
    dlbAthDot11StatsTable.setStatus("current")
_DlbAthDot11StatsEntry_Object = MibTableRow
dlbAthDot11StatsEntry = _DlbAthDot11StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1)
)
dlbAthDot11StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlbAthDot11StatsEntry.setStatus("current")
_DlbAthDot11RxBadVersion_Type = Counter32
_DlbAthDot11RxBadVersion_Object = MibTableColumn
dlbAthDot11RxBadVersion = _DlbAthDot11RxBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 1),
    _DlbAthDot11RxBadVersion_Type()
)
dlbAthDot11RxBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxBadVersion.setStatus("current")
_DlbAthDot11RxTooShort_Type = Counter32
_DlbAthDot11RxTooShort_Object = MibTableColumn
dlbAthDot11RxTooShort = _DlbAthDot11RxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 2),
    _DlbAthDot11RxTooShort_Type()
)
dlbAthDot11RxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTooShort.setStatus("current")
_DlbAthDot11RxWrongBssid_Type = Counter32
_DlbAthDot11RxWrongBssid_Object = MibTableColumn
dlbAthDot11RxWrongBssid = _DlbAthDot11RxWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 3),
    _DlbAthDot11RxWrongBssid_Type()
)
dlbAthDot11RxWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxWrongBssid.setStatus("current")
_DlbAthDot11RxDup_Type = Counter32
_DlbAthDot11RxDup_Object = MibTableColumn
dlbAthDot11RxDup = _DlbAthDot11RxDup_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 4),
    _DlbAthDot11RxDup_Type()
)
dlbAthDot11RxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDup.setStatus("current")
_DlbAthDot11RxWrongDirection_Type = Counter32
_DlbAthDot11RxWrongDirection_Object = MibTableColumn
dlbAthDot11RxWrongDirection = _DlbAthDot11RxWrongDirection_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 5),
    _DlbAthDot11RxWrongDirection_Type()
)
dlbAthDot11RxWrongDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxWrongDirection.setStatus("current")
_DlbAthDot11RxMcastEcho_Type = Counter32
_DlbAthDot11RxMcastEcho_Object = MibTableColumn
dlbAthDot11RxMcastEcho = _DlbAthDot11RxMcastEcho_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 6),
    _DlbAthDot11RxMcastEcho_Type()
)
dlbAthDot11RxMcastEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxMcastEcho.setStatus("current")
_DlbAthDot11RxNotAssoc_Type = Counter32
_DlbAthDot11RxNotAssoc_Object = MibTableColumn
dlbAthDot11RxNotAssoc = _DlbAthDot11RxNotAssoc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 7),
    _DlbAthDot11RxNotAssoc_Type()
)
dlbAthDot11RxNotAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxNotAssoc.setStatus("current")
_DlbAthDot11RxNoPrivacy_Type = Counter32
_DlbAthDot11RxNoPrivacy_Object = MibTableColumn
dlbAthDot11RxNoPrivacy = _DlbAthDot11RxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 8),
    _DlbAthDot11RxNoPrivacy_Type()
)
dlbAthDot11RxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxNoPrivacy.setStatus("current")
_DlbAthDot11RxUnencrypted_Type = Counter32
_DlbAthDot11RxUnencrypted_Object = MibTableColumn
dlbAthDot11RxUnencrypted = _DlbAthDot11RxUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 9),
    _DlbAthDot11RxUnencrypted_Type()
)
dlbAthDot11RxUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxUnencrypted.setStatus("current")
_DlbAthDot11RxWepFail_Type = Counter32
_DlbAthDot11RxWepFail_Object = MibTableColumn
dlbAthDot11RxWepFail = _DlbAthDot11RxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 10),
    _DlbAthDot11RxWepFail_Type()
)
dlbAthDot11RxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxWepFail.setStatus("current")
_DlbAthDot11RxDecapFail_Type = Counter32
_DlbAthDot11RxDecapFail_Object = MibTableColumn
dlbAthDot11RxDecapFail = _DlbAthDot11RxDecapFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 11),
    _DlbAthDot11RxDecapFail_Type()
)
dlbAthDot11RxDecapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDecapFail.setStatus("current")
_DlbAthDot11RxDiscardMgt_Type = Counter32
_DlbAthDot11RxDiscardMgt_Object = MibTableColumn
dlbAthDot11RxDiscardMgt = _DlbAthDot11RxDiscardMgt_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 12),
    _DlbAthDot11RxDiscardMgt_Type()
)
dlbAthDot11RxDiscardMgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDiscardMgt.setStatus("current")
_DlbAthDot11RxDiscardCtrl_Type = Counter32
_DlbAthDot11RxDiscardCtrl_Object = MibTableColumn
dlbAthDot11RxDiscardCtrl = _DlbAthDot11RxDiscardCtrl_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 13),
    _DlbAthDot11RxDiscardCtrl_Type()
)
dlbAthDot11RxDiscardCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDiscardCtrl.setStatus("current")
_DlbAthDot11RxBeaconFrames_Type = Counter32
_DlbAthDot11RxBeaconFrames_Object = MibTableColumn
dlbAthDot11RxBeaconFrames = _DlbAthDot11RxBeaconFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 14),
    _DlbAthDot11RxBeaconFrames_Type()
)
dlbAthDot11RxBeaconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxBeaconFrames.setStatus("current")
_DlbAthDot11RxRateSetTrunc_Type = Counter32
_DlbAthDot11RxRateSetTrunc_Object = MibTableColumn
dlbAthDot11RxRateSetTrunc = _DlbAthDot11RxRateSetTrunc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 15),
    _DlbAthDot11RxRateSetTrunc_Type()
)
dlbAthDot11RxRateSetTrunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxRateSetTrunc.setStatus("current")
_DlbAthDot11RxReqElemMissing_Type = Counter32
_DlbAthDot11RxReqElemMissing_Object = MibTableColumn
dlbAthDot11RxReqElemMissing = _DlbAthDot11RxReqElemMissing_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 16),
    _DlbAthDot11RxReqElemMissing_Type()
)
dlbAthDot11RxReqElemMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxReqElemMissing.setStatus("current")
_DlbAthDot11RxElementTooBig_Type = Counter32
_DlbAthDot11RxElementTooBig_Object = MibTableColumn
dlbAthDot11RxElementTooBig = _DlbAthDot11RxElementTooBig_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 17),
    _DlbAthDot11RxElementTooBig_Type()
)
dlbAthDot11RxElementTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxElementTooBig.setStatus("current")
_DlbAthDot11RxElementTooSmall_Type = Counter32
_DlbAthDot11RxElementTooSmall_Object = MibTableColumn
dlbAthDot11RxElementTooSmall = _DlbAthDot11RxElementTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 18),
    _DlbAthDot11RxElementTooSmall_Type()
)
dlbAthDot11RxElementTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxElementTooSmall.setStatus("current")
_DlbAthDot11RxElementUnknown_Type = Counter32
_DlbAthDot11RxElementUnknown_Object = MibTableColumn
dlbAthDot11RxElementUnknown = _DlbAthDot11RxElementUnknown_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 19),
    _DlbAthDot11RxElementUnknown_Type()
)
dlbAthDot11RxElementUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxElementUnknown.setStatus("current")
_DlbAthDot11RxInvalidChannel_Type = Counter32
_DlbAthDot11RxInvalidChannel_Object = MibTableColumn
dlbAthDot11RxInvalidChannel = _DlbAthDot11RxInvalidChannel_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 20),
    _DlbAthDot11RxInvalidChannel_Type()
)
dlbAthDot11RxInvalidChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxInvalidChannel.setStatus("current")
_DlbAthDot11RxChannelMismatch_Type = Counter32
_DlbAthDot11RxChannelMismatch_Object = MibTableColumn
dlbAthDot11RxChannelMismatch = _DlbAthDot11RxChannelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 21),
    _DlbAthDot11RxChannelMismatch_Type()
)
dlbAthDot11RxChannelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxChannelMismatch.setStatus("current")
_DlbAthDot11RxNodesAllocated_Type = Counter32
_DlbAthDot11RxNodesAllocated_Object = MibTableColumn
dlbAthDot11RxNodesAllocated = _DlbAthDot11RxNodesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 22),
    _DlbAthDot11RxNodesAllocated_Type()
)
dlbAthDot11RxNodesAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxNodesAllocated.setStatus("current")
_DlbAthDot11RxSsidMismatch_Type = Counter32
_DlbAthDot11RxSsidMismatch_Object = MibTableColumn
dlbAthDot11RxSsidMismatch = _DlbAthDot11RxSsidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 23),
    _DlbAthDot11RxSsidMismatch_Type()
)
dlbAthDot11RxSsidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxSsidMismatch.setStatus("current")
_DlbAthDot11RxUnsupportedAuthAlg_Type = Counter32
_DlbAthDot11RxUnsupportedAuthAlg_Object = MibTableColumn
dlbAthDot11RxUnsupportedAuthAlg = _DlbAthDot11RxUnsupportedAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 24),
    _DlbAthDot11RxUnsupportedAuthAlg_Type()
)
dlbAthDot11RxUnsupportedAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxUnsupportedAuthAlg.setStatus("current")
_DlbAthDot11RxAuthFail_Type = Counter32
_DlbAthDot11RxAuthFail_Object = MibTableColumn
dlbAthDot11RxAuthFail = _DlbAthDot11RxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 25),
    _DlbAthDot11RxAuthFail_Type()
)
dlbAthDot11RxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAuthFail.setStatus("current")
_DlbAthDot11RxTkipCtrm_Type = Counter32
_DlbAthDot11RxTkipCtrm_Object = MibTableColumn
dlbAthDot11RxTkipCtrm = _DlbAthDot11RxTkipCtrm_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 26),
    _DlbAthDot11RxTkipCtrm_Type()
)
dlbAthDot11RxTkipCtrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTkipCtrm.setStatus("current")
_DlbAthDot11RxAssocWrongBssid_Type = Counter32
_DlbAthDot11RxAssocWrongBssid_Object = MibTableColumn
dlbAthDot11RxAssocWrongBssid = _DlbAthDot11RxAssocWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 27),
    _DlbAthDot11RxAssocWrongBssid_Type()
)
dlbAthDot11RxAssocWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAssocWrongBssid.setStatus("current")
_DlbAthDot11RxAssocNotAuth_Type = Counter32
_DlbAthDot11RxAssocNotAuth_Object = MibTableColumn
dlbAthDot11RxAssocNotAuth = _DlbAthDot11RxAssocNotAuth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 28),
    _DlbAthDot11RxAssocNotAuth_Type()
)
dlbAthDot11RxAssocNotAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAssocNotAuth.setStatus("current")
_DlbAthDot11RxAssocCapMismatch_Type = Counter32
_DlbAthDot11RxAssocCapMismatch_Object = MibTableColumn
dlbAthDot11RxAssocCapMismatch = _DlbAthDot11RxAssocCapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 29),
    _DlbAthDot11RxAssocCapMismatch_Type()
)
dlbAthDot11RxAssocCapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAssocCapMismatch.setStatus("current")
_DlbAthDot11RxAssocNoRateMatch_Type = Counter32
_DlbAthDot11RxAssocNoRateMatch_Object = MibTableColumn
dlbAthDot11RxAssocNoRateMatch = _DlbAthDot11RxAssocNoRateMatch_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 30),
    _DlbAthDot11RxAssocNoRateMatch_Type()
)
dlbAthDot11RxAssocNoRateMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAssocNoRateMatch.setStatus("current")
_DlbAthDot11RxAssocBadWpaIe_Type = Counter32
_DlbAthDot11RxAssocBadWpaIe_Object = MibTableColumn
dlbAthDot11RxAssocBadWpaIe = _DlbAthDot11RxAssocBadWpaIe_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 31),
    _DlbAthDot11RxAssocBadWpaIe_Type()
)
dlbAthDot11RxAssocBadWpaIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAssocBadWpaIe.setStatus("current")
_DlbAthDot11RxDeauth_Type = Counter32
_DlbAthDot11RxDeauth_Object = MibTableColumn
dlbAthDot11RxDeauth = _DlbAthDot11RxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 32),
    _DlbAthDot11RxDeauth_Type()
)
dlbAthDot11RxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDeauth.setStatus("current")
_DlbAthDot11RxDisassoc_Type = Counter32
_DlbAthDot11RxDisassoc_Object = MibTableColumn
dlbAthDot11RxDisassoc = _DlbAthDot11RxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 33),
    _DlbAthDot11RxDisassoc_Type()
)
dlbAthDot11RxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDisassoc.setStatus("current")
_DlbAthDot11RxUnknownSubtype_Type = Counter32
_DlbAthDot11RxUnknownSubtype_Object = MibTableColumn
dlbAthDot11RxUnknownSubtype = _DlbAthDot11RxUnknownSubtype_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 34),
    _DlbAthDot11RxUnknownSubtype_Type()
)
dlbAthDot11RxUnknownSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxUnknownSubtype.setStatus("current")
_DlbAthDot11RxNoBuffer_Type = Counter32
_DlbAthDot11RxNoBuffer_Object = MibTableColumn
dlbAthDot11RxNoBuffer = _DlbAthDot11RxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 35),
    _DlbAthDot11RxNoBuffer_Type()
)
dlbAthDot11RxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxNoBuffer.setStatus("current")
_DlbAthDot11RxDecryptCrcError_Type = Counter32
_DlbAthDot11RxDecryptCrcError_Object = MibTableColumn
dlbAthDot11RxDecryptCrcError = _DlbAthDot11RxDecryptCrcError_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 36),
    _DlbAthDot11RxDecryptCrcError_Type()
)
dlbAthDot11RxDecryptCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxDecryptCrcError.setStatus("current")
_DlbAthDot11RxMgmtInAhdocDemo_Type = Counter32
_DlbAthDot11RxMgmtInAhdocDemo_Object = MibTableColumn
dlbAthDot11RxMgmtInAhdocDemo = _DlbAthDot11RxMgmtInAhdocDemo_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 37),
    _DlbAthDot11RxMgmtInAhdocDemo_Type()
)
dlbAthDot11RxMgmtInAhdocDemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxMgmtInAhdocDemo.setStatus("current")
_DlbAthDot11RxBadAuthRequest_Type = Counter32
_DlbAthDot11RxBadAuthRequest_Object = MibTableColumn
dlbAthDot11RxBadAuthRequest = _DlbAthDot11RxBadAuthRequest_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 38),
    _DlbAthDot11RxBadAuthRequest_Type()
)
dlbAthDot11RxBadAuthRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxBadAuthRequest.setStatus("current")
_DlbAthDot11RxPortUnauth_Type = Counter32
_DlbAthDot11RxPortUnauth_Object = MibTableColumn
dlbAthDot11RxPortUnauth = _DlbAthDot11RxPortUnauth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 39),
    _DlbAthDot11RxPortUnauth_Type()
)
dlbAthDot11RxPortUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxPortUnauth.setStatus("current")
_DlbAthDot11RxBadKeyId_Type = Counter32
_DlbAthDot11RxBadKeyId_Object = MibTableColumn
dlbAthDot11RxBadKeyId = _DlbAthDot11RxBadKeyId_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 40),
    _DlbAthDot11RxBadKeyId_Type()
)
dlbAthDot11RxBadKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxBadKeyId.setStatus("current")
_DlbAthDot11RxCcmpBadSeqNum_Type = Counter32
_DlbAthDot11RxCcmpBadSeqNum_Object = MibTableColumn
dlbAthDot11RxCcmpBadSeqNum = _DlbAthDot11RxCcmpBadSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 41),
    _DlbAthDot11RxCcmpBadSeqNum_Type()
)
dlbAthDot11RxCcmpBadSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxCcmpBadSeqNum.setStatus("current")
_DlbAthDot11RxCcmpBadFormat_Type = Counter32
_DlbAthDot11RxCcmpBadFormat_Object = MibTableColumn
dlbAthDot11RxCcmpBadFormat = _DlbAthDot11RxCcmpBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 42),
    _DlbAthDot11RxCcmpBadFormat_Type()
)
dlbAthDot11RxCcmpBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxCcmpBadFormat.setStatus("current")
_DlbAthDot11RxCcmpMicCheck_Type = Counter32
_DlbAthDot11RxCcmpMicCheck_Object = MibTableColumn
dlbAthDot11RxCcmpMicCheck = _DlbAthDot11RxCcmpMicCheck_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 43),
    _DlbAthDot11RxCcmpMicCheck_Type()
)
dlbAthDot11RxCcmpMicCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxCcmpMicCheck.setStatus("current")
_DlbAthDot11RxTkipBadSeqNum_Type = Counter32
_DlbAthDot11RxTkipBadSeqNum_Object = MibTableColumn
dlbAthDot11RxTkipBadSeqNum = _DlbAthDot11RxTkipBadSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 44),
    _DlbAthDot11RxTkipBadSeqNum_Type()
)
dlbAthDot11RxTkipBadSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTkipBadSeqNum.setStatus("current")
_DlbAthDot11RxTkipBadFormat_Type = Counter32
_DlbAthDot11RxTkipBadFormat_Object = MibTableColumn
dlbAthDot11RxTkipBadFormat = _DlbAthDot11RxTkipBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 45),
    _DlbAthDot11RxTkipBadFormat_Type()
)
dlbAthDot11RxTkipBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTkipBadFormat.setStatus("current")
_DlbAthDot11RxTkipMicCheck_Type = Counter32
_DlbAthDot11RxTkipMicCheck_Object = MibTableColumn
dlbAthDot11RxTkipMicCheck = _DlbAthDot11RxTkipMicCheck_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 46),
    _DlbAthDot11RxTkipMicCheck_Type()
)
dlbAthDot11RxTkipMicCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTkipMicCheck.setStatus("current")
_DlbAthDot11RxTkipIcvCheck_Type = Counter32
_DlbAthDot11RxTkipIcvCheck_Object = MibTableColumn
dlbAthDot11RxTkipIcvCheck = _DlbAthDot11RxTkipIcvCheck_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 47),
    _DlbAthDot11RxTkipIcvCheck_Type()
)
dlbAthDot11RxTkipIcvCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxTkipIcvCheck.setStatus("current")
_DlbAthDot11RxBadCipherKeyType_Type = Counter32
_DlbAthDot11RxBadCipherKeyType_Object = MibTableColumn
dlbAthDot11RxBadCipherKeyType = _DlbAthDot11RxBadCipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 48),
    _DlbAthDot11RxBadCipherKeyType_Type()
)
dlbAthDot11RxBadCipherKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxBadCipherKeyType.setStatus("current")
_DlbAthDot11RxCipherKeyNotSet_Type = Counter32
_DlbAthDot11RxCipherKeyNotSet_Object = MibTableColumn
dlbAthDot11RxCipherKeyNotSet = _DlbAthDot11RxCipherKeyNotSet_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 49),
    _DlbAthDot11RxCipherKeyNotSet_Type()
)
dlbAthDot11RxCipherKeyNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxCipherKeyNotSet.setStatus("current")
_DlbAthDot11RxAclPolicy_Type = Counter32
_DlbAthDot11RxAclPolicy_Object = MibTableColumn
dlbAthDot11RxAclPolicy = _DlbAthDot11RxAclPolicy_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 50),
    _DlbAthDot11RxAclPolicy_Type()
)
dlbAthDot11RxAclPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxAclPolicy.setStatus("current")
_DlbAthDot11RxFastFrames_Type = Counter32
_DlbAthDot11RxFastFrames_Object = MibTableColumn
dlbAthDot11RxFastFrames = _DlbAthDot11RxFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 51),
    _DlbAthDot11RxFastFrames_Type()
)
dlbAthDot11RxFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxFastFrames.setStatus("current")
_DlbAthDot11RxFfBadTunnelHdr_Type = Counter32
_DlbAthDot11RxFfBadTunnelHdr_Object = MibTableColumn
dlbAthDot11RxFfBadTunnelHdr = _DlbAthDot11RxFfBadTunnelHdr_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 52),
    _DlbAthDot11RxFfBadTunnelHdr_Type()
)
dlbAthDot11RxFfBadTunnelHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11RxFfBadTunnelHdr.setStatus("current")
_DlbAthDot11TxNoBuffer_Type = Counter32
_DlbAthDot11TxNoBuffer_Object = MibTableColumn
dlbAthDot11TxNoBuffer = _DlbAthDot11TxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 53),
    _DlbAthDot11TxNoBuffer_Type()
)
dlbAthDot11TxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxNoBuffer.setStatus("current")
_DlbAthDot11TxNoNode_Type = Counter32
_DlbAthDot11TxNoNode_Object = MibTableColumn
dlbAthDot11TxNoNode = _DlbAthDot11TxNoNode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 54),
    _DlbAthDot11TxNoNode_Type()
)
dlbAthDot11TxNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxNoNode.setStatus("current")
_DlbAthDot11TxBadMgtFrames_Type = Counter32
_DlbAthDot11TxBadMgtFrames_Object = MibTableColumn
dlbAthDot11TxBadMgtFrames = _DlbAthDot11TxBadMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 55),
    _DlbAthDot11TxBadMgtFrames_Type()
)
dlbAthDot11TxBadMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxBadMgtFrames.setStatus("current")
_DlbAthDot11TxBadCipherKeyType_Type = Counter32
_DlbAthDot11TxBadCipherKeyType_Object = MibTableColumn
dlbAthDot11TxBadCipherKeyType = _DlbAthDot11TxBadCipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 56),
    _DlbAthDot11TxBadCipherKeyType_Type()
)
dlbAthDot11TxBadCipherKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxBadCipherKeyType.setStatus("current")
_DlbAthDot11TxNoDefKey_Type = Counter32
_DlbAthDot11TxNoDefKey_Object = MibTableColumn
dlbAthDot11TxNoDefKey = _DlbAthDot11TxNoDefKey_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 57),
    _DlbAthDot11TxNoDefKey_Type()
)
dlbAthDot11TxNoDefKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxNoDefKey.setStatus("current")
_DlbAthDot11TxNoCryptoHeadroom_Type = Counter32
_DlbAthDot11TxNoCryptoHeadroom_Object = MibTableColumn
dlbAthDot11TxNoCryptoHeadroom = _DlbAthDot11TxNoCryptoHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 58),
    _DlbAthDot11TxNoCryptoHeadroom_Type()
)
dlbAthDot11TxNoCryptoHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxNoCryptoHeadroom.setStatus("current")
_DlbAthDot11TxGoodFastFrames_Type = Counter32
_DlbAthDot11TxGoodFastFrames_Object = MibTableColumn
dlbAthDot11TxGoodFastFrames = _DlbAthDot11TxGoodFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 59),
    _DlbAthDot11TxGoodFastFrames_Type()
)
dlbAthDot11TxGoodFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxGoodFastFrames.setStatus("current")
_DlbAthDot11TxBadFastFrames_Type = Counter32
_DlbAthDot11TxBadFastFrames_Object = MibTableColumn
dlbAthDot11TxBadFastFrames = _DlbAthDot11TxBadFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 60),
    _DlbAthDot11TxBadFastFrames_Type()
)
dlbAthDot11TxBadFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11TxBadFastFrames.setStatus("current")
_DlbAthDot11ActiveScans_Type = Counter32
_DlbAthDot11ActiveScans_Object = MibTableColumn
dlbAthDot11ActiveScans = _DlbAthDot11ActiveScans_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 61),
    _DlbAthDot11ActiveScans_Type()
)
dlbAthDot11ActiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11ActiveScans.setStatus("current")
_DlbAthDot11PassiveScans_Type = Counter32
_DlbAthDot11PassiveScans_Object = MibTableColumn
dlbAthDot11PassiveScans = _DlbAthDot11PassiveScans_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 62),
    _DlbAthDot11PassiveScans_Type()
)
dlbAthDot11PassiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11PassiveScans.setStatus("current")
_DlbAthDot11NodesTimeout_Type = Counter32
_DlbAthDot11NodesTimeout_Object = MibTableColumn
dlbAthDot11NodesTimeout = _DlbAthDot11NodesTimeout_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 63),
    _DlbAthDot11NodesTimeout_Type()
)
dlbAthDot11NodesTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11NodesTimeout.setStatus("current")
_DlbAthDot11CryptoCipherMalloc_Type = Counter32
_DlbAthDot11CryptoCipherMalloc_Object = MibTableColumn
dlbAthDot11CryptoCipherMalloc = _DlbAthDot11CryptoCipherMalloc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 64),
    _DlbAthDot11CryptoCipherMalloc_Type()
)
dlbAthDot11CryptoCipherMalloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoCipherMalloc.setStatus("current")
_DlbAthDot11CryptoSwTkip_Type = Counter32
_DlbAthDot11CryptoSwTkip_Object = MibTableColumn
dlbAthDot11CryptoSwTkip = _DlbAthDot11CryptoSwTkip_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 65),
    _DlbAthDot11CryptoSwTkip_Type()
)
dlbAthDot11CryptoSwTkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoSwTkip.setStatus("current")
_DlbAthDot11CryptoTkipSwMicEnc_Type = Counter32
_DlbAthDot11CryptoTkipSwMicEnc_Object = MibTableColumn
dlbAthDot11CryptoTkipSwMicEnc = _DlbAthDot11CryptoTkipSwMicEnc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 66),
    _DlbAthDot11CryptoTkipSwMicEnc_Type()
)
dlbAthDot11CryptoTkipSwMicEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoTkipSwMicEnc.setStatus("current")
_DlbAthDot11CryptoTkipSwMicDec_Type = Counter32
_DlbAthDot11CryptoTkipSwMicDec_Object = MibTableColumn
dlbAthDot11CryptoTkipSwMicDec = _DlbAthDot11CryptoTkipSwMicDec_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 67),
    _DlbAthDot11CryptoTkipSwMicDec_Type()
)
dlbAthDot11CryptoTkipSwMicDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoTkipSwMicDec.setStatus("current")
_DlbAthDot11CryptoTkipCtrm_Type = Counter32
_DlbAthDot11CryptoTkipCtrm_Object = MibTableColumn
dlbAthDot11CryptoTkipCtrm = _DlbAthDot11CryptoTkipCtrm_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 68),
    _DlbAthDot11CryptoTkipCtrm_Type()
)
dlbAthDot11CryptoTkipCtrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoTkipCtrm.setStatus("current")
_DlbAthDot11CryptoSwCcmp_Type = Counter32
_DlbAthDot11CryptoSwCcmp_Object = MibTableColumn
dlbAthDot11CryptoSwCcmp = _DlbAthDot11CryptoSwCcmp_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 69),
    _DlbAthDot11CryptoSwCcmp_Type()
)
dlbAthDot11CryptoSwCcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoSwCcmp.setStatus("current")
_DlbAthDot11CryptoSwWep_Type = Counter32
_DlbAthDot11CryptoSwWep_Object = MibTableColumn
dlbAthDot11CryptoSwWep = _DlbAthDot11CryptoSwWep_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 70),
    _DlbAthDot11CryptoSwWep_Type()
)
dlbAthDot11CryptoSwWep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoSwWep.setStatus("current")
_DlbAthDot11CryptoCipherRej_Type = Counter32
_DlbAthDot11CryptoCipherRej_Object = MibTableColumn
dlbAthDot11CryptoCipherRej = _DlbAthDot11CryptoCipherRej_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 71),
    _DlbAthDot11CryptoCipherRej_Type()
)
dlbAthDot11CryptoCipherRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoCipherRej.setStatus("current")
_DlbAthDot11CryptoNoKey_Type = Counter32
_DlbAthDot11CryptoNoKey_Object = MibTableColumn
dlbAthDot11CryptoNoKey = _DlbAthDot11CryptoNoKey_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 72),
    _DlbAthDot11CryptoNoKey_Type()
)
dlbAthDot11CryptoNoKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoNoKey.setStatus("current")
_DlbAthDot11CryptoDelKey_Type = Counter32
_DlbAthDot11CryptoDelKey_Object = MibTableColumn
dlbAthDot11CryptoDelKey = _DlbAthDot11CryptoDelKey_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 73),
    _DlbAthDot11CryptoDelKey_Type()
)
dlbAthDot11CryptoDelKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoDelKey.setStatus("current")
_DlbAthDot11CryptoBadCipher_Type = Counter32
_DlbAthDot11CryptoBadCipher_Object = MibTableColumn
dlbAthDot11CryptoBadCipher = _DlbAthDot11CryptoBadCipher_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 74),
    _DlbAthDot11CryptoBadCipher_Type()
)
dlbAthDot11CryptoBadCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoBadCipher.setStatus("current")
_DlbAthDot11CryptoNoCipher_Type = Counter32
_DlbAthDot11CryptoNoCipher_Object = MibTableColumn
dlbAthDot11CryptoNoCipher = _DlbAthDot11CryptoNoCipher_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 75),
    _DlbAthDot11CryptoNoCipher_Type()
)
dlbAthDot11CryptoNoCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoNoCipher.setStatus("current")
_DlbAthDot11CryptoAttachFail_Type = Counter32
_DlbAthDot11CryptoAttachFail_Object = MibTableColumn
dlbAthDot11CryptoAttachFail = _DlbAthDot11CryptoAttachFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 76),
    _DlbAthDot11CryptoAttachFail_Type()
)
dlbAthDot11CryptoAttachFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoAttachFail.setStatus("current")
_DlbAthDot11CryptoSwFallback_Type = Counter32
_DlbAthDot11CryptoSwFallback_Object = MibTableColumn
dlbAthDot11CryptoSwFallback = _DlbAthDot11CryptoSwFallback_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 77),
    _DlbAthDot11CryptoSwFallback_Type()
)
dlbAthDot11CryptoSwFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoSwFallback.setStatus("current")
_DlbAthDot11CryptoKeyFail_Type = Counter32
_DlbAthDot11CryptoKeyFail_Object = MibTableColumn
dlbAthDot11CryptoKeyFail = _DlbAthDot11CryptoKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 78),
    _DlbAthDot11CryptoKeyFail_Type()
)
dlbAthDot11CryptoKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11CryptoKeyFail.setStatus("current")
_DlbAthDot11SnoopMcastPass_Type = Counter32
_DlbAthDot11SnoopMcastPass_Object = MibTableColumn
dlbAthDot11SnoopMcastPass = _DlbAthDot11SnoopMcastPass_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 79),
    _DlbAthDot11SnoopMcastPass_Type()
)
dlbAthDot11SnoopMcastPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11SnoopMcastPass.setStatus("current")
_DlbAthDot11SnoopMcastDrop_Type = Counter32
_DlbAthDot11SnoopMcastDrop_Object = MibTableColumn
dlbAthDot11SnoopMcastDrop = _DlbAthDot11SnoopMcastDrop_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 4, 1, 80),
    _DlbAthDot11SnoopMcastDrop_Type()
)
dlbAthDot11SnoopMcastDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthDot11SnoopMcastDrop.setStatus("current")
_DlbAthPeerStatsTable_Object = MibTable
dlbAthPeerStatsTable = _DlbAthPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5)
)
if mibBuilder.loadTexts:
    dlbAthPeerStatsTable.setStatus("current")
_DlbAthPeerStatsEntry_Object = MibTableRow
dlbAthPeerStatsEntry = _DlbAthPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1)
)
dlbAthPeerStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DLB-ATHDRV-STATS-MIB", "dlbAthPeerIndex"),
)
if mibBuilder.loadTexts:
    dlbAthPeerStatsEntry.setStatus("current")
_DlbAthPeerIndex_Type = Integer32
_DlbAthPeerIndex_Object = MibTableColumn
dlbAthPeerIndex = _DlbAthPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 1),
    _DlbAthPeerIndex_Type()
)
dlbAthPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlbAthPeerIndex.setStatus("current")
_DlbAthPeerMacAddr_Type = MacAddress
_DlbAthPeerMacAddr_Object = MibTableColumn
dlbAthPeerMacAddr = _DlbAthPeerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 2),
    _DlbAthPeerMacAddr_Type()
)
dlbAthPeerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerMacAddr.setStatus("current")
_DlbAthPeerRxData_Type = Counter32
_DlbAthPeerRxData_Object = MibTableColumn
dlbAthPeerRxData = _DlbAthPeerRxData_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 3),
    _DlbAthPeerRxData_Type()
)
dlbAthPeerRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxData.setStatus("current")
_DlbAthPeerRxMgmt_Type = Counter32
_DlbAthPeerRxMgmt_Object = MibTableColumn
dlbAthPeerRxMgmt = _DlbAthPeerRxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 4),
    _DlbAthPeerRxMgmt_Type()
)
dlbAthPeerRxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxMgmt.setStatus("current")
_DlbAthPeerRxCtrl_Type = Counter32
_DlbAthPeerRxCtrl_Object = MibTableColumn
dlbAthPeerRxCtrl = _DlbAthPeerRxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 5),
    _DlbAthPeerRxCtrl_Type()
)
dlbAthPeerRxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxCtrl.setStatus("current")
_DlbAthPeerRxBeacons_Type = Counter64
_DlbAthPeerRxBeacons_Object = MibTableColumn
dlbAthPeerRxBeacons = _DlbAthPeerRxBeacons_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 6),
    _DlbAthPeerRxBeacons_Type()
)
dlbAthPeerRxBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxBeacons.setStatus("current")
_DlbAthPeerRxProbeResponse_Type = Counter32
_DlbAthPeerRxProbeResponse_Object = MibTableColumn
dlbAthPeerRxProbeResponse = _DlbAthPeerRxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 7),
    _DlbAthPeerRxProbeResponse_Type()
)
dlbAthPeerRxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxProbeResponse.setStatus("current")
_DlbAthPeerRxUcast_Type = Counter32
_DlbAthPeerRxUcast_Object = MibTableColumn
dlbAthPeerRxUcast = _DlbAthPeerRxUcast_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 8),
    _DlbAthPeerRxUcast_Type()
)
dlbAthPeerRxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxUcast.setStatus("current")
_DlbAthPeerRxMcast_Type = Counter32
_DlbAthPeerRxMcast_Object = MibTableColumn
dlbAthPeerRxMcast = _DlbAthPeerRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 9),
    _DlbAthPeerRxMcast_Type()
)
dlbAthPeerRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxMcast.setStatus("current")
_DlbAthPeerRxBytes_Type = Counter64
_DlbAthPeerRxBytes_Object = MibTableColumn
dlbAthPeerRxBytes = _DlbAthPeerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 10),
    _DlbAthPeerRxBytes_Type()
)
dlbAthPeerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxBytes.setStatus("current")
_DlbAthPeerRxDup_Type = Counter32
_DlbAthPeerRxDup_Object = MibTableColumn
dlbAthPeerRxDup = _DlbAthPeerRxDup_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 11),
    _DlbAthPeerRxDup_Type()
)
dlbAthPeerRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDup.setStatus("current")
_DlbAthPeerRxNoPrivacy_Type = Counter32
_DlbAthPeerRxNoPrivacy_Object = MibTableColumn
dlbAthPeerRxNoPrivacy = _DlbAthPeerRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 12),
    _DlbAthPeerRxNoPrivacy_Type()
)
dlbAthPeerRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxNoPrivacy.setStatus("current")
_DlbAthPeerRxWepFail_Type = Counter32
_DlbAthPeerRxWepFail_Object = MibTableColumn
dlbAthPeerRxWepFail = _DlbAthPeerRxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 13),
    _DlbAthPeerRxWepFail_Type()
)
dlbAthPeerRxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxWepFail.setStatus("current")
_DlbAthPeerRxDemicFail_Type = Counter32
_DlbAthPeerRxDemicFail_Object = MibTableColumn
dlbAthPeerRxDemicFail = _DlbAthPeerRxDemicFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 14),
    _DlbAthPeerRxDemicFail_Type()
)
dlbAthPeerRxDemicFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDemicFail.setStatus("current")
_DlbAthPeerRxDecapFail_Type = Counter32
_DlbAthPeerRxDecapFail_Object = MibTableColumn
dlbAthPeerRxDecapFail = _DlbAthPeerRxDecapFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 15),
    _DlbAthPeerRxDecapFail_Type()
)
dlbAthPeerRxDecapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDecapFail.setStatus("current")
_DlbAthPeerRxDefragFail_Type = Counter32
_DlbAthPeerRxDefragFail_Object = MibTableColumn
dlbAthPeerRxDefragFail = _DlbAthPeerRxDefragFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 16),
    _DlbAthPeerRxDefragFail_Type()
)
dlbAthPeerRxDefragFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDefragFail.setStatus("current")
_DlbAthPeerRxDissasoc_Type = Counter32
_DlbAthPeerRxDissasoc_Object = MibTableColumn
dlbAthPeerRxDissasoc = _DlbAthPeerRxDissasoc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 17),
    _DlbAthPeerRxDissasoc_Type()
)
dlbAthPeerRxDissasoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDissasoc.setStatus("current")
_DlbAthPeerRxDeauth_Type = Counter32
_DlbAthPeerRxDeauth_Object = MibTableColumn
dlbAthPeerRxDeauth = _DlbAthPeerRxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 18),
    _DlbAthPeerRxDeauth_Type()
)
dlbAthPeerRxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDeauth.setStatus("current")
_DlbAthPeerRxDecryptCrc_Type = Counter32
_DlbAthPeerRxDecryptCrc_Object = MibTableColumn
dlbAthPeerRxDecryptCrc = _DlbAthPeerRxDecryptCrc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 19),
    _DlbAthPeerRxDecryptCrc_Type()
)
dlbAthPeerRxDecryptCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxDecryptCrc.setStatus("current")
_DlbAthPeerRxUnauth_Type = Counter32
_DlbAthPeerRxUnauth_Object = MibTableColumn
dlbAthPeerRxUnauth = _DlbAthPeerRxUnauth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 20),
    _DlbAthPeerRxUnauth_Type()
)
dlbAthPeerRxUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxUnauth.setStatus("current")
_DlbAthPeerRxUnencrypted_Type = Counter32
_DlbAthPeerRxUnencrypted_Object = MibTableColumn
dlbAthPeerRxUnencrypted = _DlbAthPeerRxUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 21),
    _DlbAthPeerRxUnencrypted_Type()
)
dlbAthPeerRxUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerRxUnencrypted.setStatus("current")
_DlbAthPeerTxData_Type = Counter32
_DlbAthPeerTxData_Object = MibTableColumn
dlbAthPeerTxData = _DlbAthPeerTxData_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 22),
    _DlbAthPeerTxData_Type()
)
dlbAthPeerTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxData.setStatus("current")
_DlbAthPeerTxMgmt_Type = Counter32
_DlbAthPeerTxMgmt_Object = MibTableColumn
dlbAthPeerTxMgmt = _DlbAthPeerTxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 23),
    _DlbAthPeerTxMgmt_Type()
)
dlbAthPeerTxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxMgmt.setStatus("current")
_DlbAthPeerTxProbeReq_Type = Counter32
_DlbAthPeerTxProbeReq_Object = MibTableColumn
dlbAthPeerTxProbeReq = _DlbAthPeerTxProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 24),
    _DlbAthPeerTxProbeReq_Type()
)
dlbAthPeerTxProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxProbeReq.setStatus("current")
_DlbAthPeerTxUcast_Type = Counter32
_DlbAthPeerTxUcast_Object = MibTableColumn
dlbAthPeerTxUcast = _DlbAthPeerTxUcast_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 25),
    _DlbAthPeerTxUcast_Type()
)
dlbAthPeerTxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxUcast.setStatus("current")
_DlbAthPeerTxMcast_Type = Counter32
_DlbAthPeerTxMcast_Object = MibTableColumn
dlbAthPeerTxMcast = _DlbAthPeerTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 26),
    _DlbAthPeerTxMcast_Type()
)
dlbAthPeerTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxMcast.setStatus("current")
_DlbAthPeerTxBytes_Type = Counter64
_DlbAthPeerTxBytes_Object = MibTableColumn
dlbAthPeerTxBytes = _DlbAthPeerTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 27),
    _DlbAthPeerTxBytes_Type()
)
dlbAthPeerTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxBytes.setStatus("current")
_DlbAthPeerTxNoVlanTag_Type = Counter32
_DlbAthPeerTxNoVlanTag_Object = MibTableColumn
dlbAthPeerTxNoVlanTag = _DlbAthPeerTxNoVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 28),
    _DlbAthPeerTxNoVlanTag_Type()
)
dlbAthPeerTxNoVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxNoVlanTag.setStatus("current")
_DlbAthPeerTxVlanMismatch_Type = Counter32
_DlbAthPeerTxVlanMismatch_Object = MibTableColumn
dlbAthPeerTxVlanMismatch = _DlbAthPeerTxVlanMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 29),
    _DlbAthPeerTxVlanMismatch_Type()
)
dlbAthPeerTxVlanMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxVlanMismatch.setStatus("current")
_DlbAthPeerTxUapsd_Type = Counter32
_DlbAthPeerTxUapsd_Object = MibTableColumn
dlbAthPeerTxUapsd = _DlbAthPeerTxUapsd_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 30),
    _DlbAthPeerTxUapsd_Type()
)
dlbAthPeerTxUapsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxUapsd.setStatus("current")
_DlbAthPeerUapsdTriggers_Type = Counter32
_DlbAthPeerUapsdTriggers_Object = MibTableColumn
dlbAthPeerUapsdTriggers = _DlbAthPeerUapsdTriggers_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 31),
    _DlbAthPeerUapsdTriggers_Type()
)
dlbAthPeerUapsdTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerUapsdTriggers.setStatus("current")
_DlbAthPeerTxEospLost_Type = Counter32
_DlbAthPeerTxEospLost_Object = MibTableColumn
dlbAthPeerTxEospLost = _DlbAthPeerTxEospLost_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 32),
    _DlbAthPeerTxEospLost_Type()
)
dlbAthPeerTxEospLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxEospLost.setStatus("current")
_DlbAthPeerTxAssoc_Type = Counter32
_DlbAthPeerTxAssoc_Object = MibTableColumn
dlbAthPeerTxAssoc = _DlbAthPeerTxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 33),
    _DlbAthPeerTxAssoc_Type()
)
dlbAthPeerTxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxAssoc.setStatus("current")
_DlbAthPeerTxAssocFail_Type = Counter32
_DlbAthPeerTxAssocFail_Object = MibTableColumn
dlbAthPeerTxAssocFail = _DlbAthPeerTxAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 34),
    _DlbAthPeerTxAssocFail_Type()
)
dlbAthPeerTxAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxAssocFail.setStatus("current")
_DlbAthPeerTxAuth_Type = Counter32
_DlbAthPeerTxAuth_Object = MibTableColumn
dlbAthPeerTxAuth = _DlbAthPeerTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 35),
    _DlbAthPeerTxAuth_Type()
)
dlbAthPeerTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxAuth.setStatus("current")
_DlbAthPeerTxAuthFail_Type = Counter32
_DlbAthPeerTxAuthFail_Object = MibTableColumn
dlbAthPeerTxAuthFail = _DlbAthPeerTxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 36),
    _DlbAthPeerTxAuthFail_Type()
)
dlbAthPeerTxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxAuthFail.setStatus("current")
_DlbAthPeerTxDeauth_Type = Counter32
_DlbAthPeerTxDeauth_Object = MibTableColumn
dlbAthPeerTxDeauth = _DlbAthPeerTxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 37),
    _DlbAthPeerTxDeauth_Type()
)
dlbAthPeerTxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxDeauth.setStatus("current")
_DlbAthPeerTxDeauthCode_Type = Counter32
_DlbAthPeerTxDeauthCode_Object = MibTableColumn
dlbAthPeerTxDeauthCode = _DlbAthPeerTxDeauthCode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 38),
    _DlbAthPeerTxDeauthCode_Type()
)
dlbAthPeerTxDeauthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxDeauthCode.setStatus("current")
_DlbAthPeerTxDisassoc_Type = Counter32
_DlbAthPeerTxDisassoc_Object = MibTableColumn
dlbAthPeerTxDisassoc = _DlbAthPeerTxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 39),
    _DlbAthPeerTxDisassoc_Type()
)
dlbAthPeerTxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxDisassoc.setStatus("current")
_DlbAthPeerTxDisassocCode_Type = Counter32
_DlbAthPeerTxDisassocCode_Object = MibTableColumn
dlbAthPeerTxDisassocCode = _DlbAthPeerTxDisassocCode_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 40),
    _DlbAthPeerTxDisassocCode_Type()
)
dlbAthPeerTxDisassocCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerTxDisassocCode.setStatus("current")
_DlbAthPeerPsqDrops_Type = Counter32
_DlbAthPeerPsqDrops_Object = MibTableColumn
dlbAthPeerPsqDrops = _DlbAthPeerPsqDrops_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 41),
    _DlbAthPeerPsqDrops_Type()
)
dlbAthPeerPsqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerPsqDrops.setStatus("current")
_DlbAthPeerMcastSnoop_Type = Counter32
_DlbAthPeerMcastSnoop_Object = MibTableColumn
dlbAthPeerMcastSnoop = _DlbAthPeerMcastSnoop_Object(
    (1, 3, 6, 1, 4, 1, 32761, 3, 7, 1, 5, 1, 42),
    _DlbAthPeerMcastSnoop_Type()
)
dlbAthPeerMcastSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlbAthPeerMcastSnoop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLB-ATHDRV-STATS-MIB",
    **{"dlbAthDrvStatsMIB": dlbAthDrvStatsMIB,
       "dlbAthDrvStatsMIBObjects": dlbAthDrvStatsMIBObjects,
       "dlbAthStatsTable": dlbAthStatsTable,
       "dlbAthStatsEntry": dlbAthStatsEntry,
       "dlbAthWatchdogTimeouts": dlbAthWatchdogTimeouts,
       "dlbAthHardwareErrorInterrupts": dlbAthHardwareErrorInterrupts,
       "dlbAthBeaconMissInterrupts": dlbAthBeaconMissInterrupts,
       "dlbAthRecvOverrunInterrupts": dlbAthRecvOverrunInterrupts,
       "dlbAthRecvEolInterrupts": dlbAthRecvEolInterrupts,
       "dlbAthTxmitUnderrunInterrupts": dlbAthTxmitUnderrunInterrupts,
       "dlbAthTxManagementFrames": dlbAthTxManagementFrames,
       "dlbAthTxFramesDiscQueueDepth": dlbAthTxFramesDiscQueueDepth,
       "dlbAthTxFramesDiscDeviceGone": dlbAthTxFramesDiscDeviceGone,
       "dlbAthTxQueueFull": dlbAthTxQueueFull,
       "dlbAthTxEncapsulationFailed": dlbAthTxEncapsulationFailed,
       "dlbAthTxFailedNoNode": dlbAthTxFailedNoNode,
       "dlbAthTxFailedNoDataTxBuffer": dlbAthTxFailedNoDataTxBuffer,
       "dlbAthTxFailedNoMgtTxBuffer": dlbAthTxFailedNoMgtTxBuffer,
       "dlbAthTxFailedTooManyRetries": dlbAthTxFailedTooManyRetries,
       "dlbAthTxFailedFifoUnderrun": dlbAthTxFailedFifoUnderrun,
       "dlbAthTxFailedXmitFiltered": dlbAthTxFailedXmitFiltered,
       "dlbAthShortOnchipTxRetries": dlbAthShortOnchipTxRetries,
       "dlbAthLongOnchipTxRetries": dlbAthLongOnchipTxRetries,
       "dlbAthTxFailedBogusXmitRate": dlbAthTxFailedBogusXmitRate,
       "dlbAthTxFramesNoAckMarked": dlbAthTxFramesNoAckMarked,
       "dlbAthTxFramesRtsEnabled": dlbAthTxFramesRtsEnabled,
       "dlbAthTxFramesCtsEnabled": dlbAthTxFramesCtsEnabled,
       "dlbAthTxFramesShortPreamble": dlbAthTxFramesShortPreamble,
       "dlbAthTxFramesAlternateRate": dlbAthTxFramesAlternateRate,
       "dlbAthTxFrames11gProtection": dlbAthTxFrames11gProtection,
       "dlbAthRxFailedDescOverrun": dlbAthRxFailedDescOverrun,
       "dlbAthRxFailedBadCrc": dlbAthRxFailedBadCrc,
       "dlbAthRxFailedFifoOverrun": dlbAthRxFailedFifoOverrun,
       "dlbAthRxFailedDecryptErrors": dlbAthRxFailedDecryptErrors,
       "dlbAthRxFailedMicFailure": dlbAthRxFailedMicFailure,
       "dlbAthRxFailedFrameTooShort": dlbAthRxFailedFrameTooShort,
       "dlbAthRxSetupFailedNoSkbuff": dlbAthRxSetupFailedNoSkbuff,
       "dlbAthRxManagementFrames": dlbAthRxManagementFrames,
       "dlbAthRxControlFrames": dlbAthRxControlFrames,
       "dlbAthNoSkbuffForBeacon": dlbAthNoSkbuffForBeacon,
       "dlbAthBeaconsTransmitted": dlbAthBeaconsTransmitted,
       "dlbAthPeriodicCalibrations": dlbAthPeriodicCalibrations,
       "dlbAthPeriodicCalibrFailures": dlbAthPeriodicCalibrFailures,
       "dlbAthRfgainValueChange": dlbAthRfgainValueChange,
       "dlbAthRateControlChecks": dlbAthRateControlChecks,
       "dlbAthRateCtrlRaisedXmitRate": dlbAthRateCtrlRaisedXmitRate,
       "dlbAthRateCtrlDroppedXmitRate": dlbAthRateCtrlDroppedXmitRate,
       "dlbAthRssiOfLastAck": dlbAthRssiOfLastAck,
       "dlbAthRssiOfLastRcv": dlbAthRssiOfLastRcv,
       "dlbAthPhyErrorsTable": dlbAthPhyErrorsTable,
       "dlbAthPhyErrorsEntry": dlbAthPhyErrorsEntry,
       "dlbAthPhyTransmitUnderrun": dlbAthPhyTransmitUnderrun,
       "dlbAthPhyTimingError": dlbAthPhyTimingError,
       "dlbAthPhyIllegalParity": dlbAthPhyIllegalParity,
       "dlbAthPhyIllegalRate": dlbAthPhyIllegalRate,
       "dlbAthPhyIllegalLength": dlbAthPhyIllegalLength,
       "dlbAthPhyRadarDetect": dlbAthPhyRadarDetect,
       "dlbAthPhyIllegalService": dlbAthPhyIllegalService,
       "dlbAthPhyTxmitOverrideRecv": dlbAthPhyTxmitOverrideRecv,
       "dlbAthPhyOfdmTiming": dlbAthPhyOfdmTiming,
       "dlbAthPhyOfdmIllegalParity": dlbAthPhyOfdmIllegalParity,
       "dlbAthPhyOfdmIllegalRate": dlbAthPhyOfdmIllegalRate,
       "dlbAthPhyOfdmIllegalLength": dlbAthPhyOfdmIllegalLength,
       "dlbAthPhyOfdmPowerDrop": dlbAthPhyOfdmPowerDrop,
       "dlbAthPhyOfdmIllegalService": dlbAthPhyOfdmIllegalService,
       "dlbAthPhyOfdmRestart": dlbAthPhyOfdmRestart,
       "dlbAthPhyCckTiming": dlbAthPhyCckTiming,
       "dlbAthPhyCckHeaderCrc": dlbAthPhyCckHeaderCrc,
       "dlbAthPhyCckIllegalRate": dlbAthPhyCckIllegalRate,
       "dlbAthPhyCckIllegalService": dlbAthPhyCckIllegalService,
       "dlbAthPhyCckRestart": dlbAthPhyCckRestart,
       "dlbAthAntennaStatsTable": dlbAthAntennaStatsTable,
       "dlbAthAntennaStatsEntry": dlbAthAntennaStatsEntry,
       "dlbAthSwitchedDefaultRxAntenna": dlbAthSwitchedDefaultRxAntenna,
       "dlbAthTxUsedAlternateAntenna": dlbAthTxUsedAlternateAntenna,
       "dlbAthTxFramesAntenna1": dlbAthTxFramesAntenna1,
       "dlbAthRxFramesAntenna1": dlbAthRxFramesAntenna1,
       "dlbAthTxFramesAntenna2": dlbAthTxFramesAntenna2,
       "dlbAthRxFramesAntenna2": dlbAthRxFramesAntenna2,
       "dlbAthTxFramesAntenna3": dlbAthTxFramesAntenna3,
       "dlbAthRxFramesAntenna3": dlbAthRxFramesAntenna3,
       "dlbAthDot11StatsTable": dlbAthDot11StatsTable,
       "dlbAthDot11StatsEntry": dlbAthDot11StatsEntry,
       "dlbAthDot11RxBadVersion": dlbAthDot11RxBadVersion,
       "dlbAthDot11RxTooShort": dlbAthDot11RxTooShort,
       "dlbAthDot11RxWrongBssid": dlbAthDot11RxWrongBssid,
       "dlbAthDot11RxDup": dlbAthDot11RxDup,
       "dlbAthDot11RxWrongDirection": dlbAthDot11RxWrongDirection,
       "dlbAthDot11RxMcastEcho": dlbAthDot11RxMcastEcho,
       "dlbAthDot11RxNotAssoc": dlbAthDot11RxNotAssoc,
       "dlbAthDot11RxNoPrivacy": dlbAthDot11RxNoPrivacy,
       "dlbAthDot11RxUnencrypted": dlbAthDot11RxUnencrypted,
       "dlbAthDot11RxWepFail": dlbAthDot11RxWepFail,
       "dlbAthDot11RxDecapFail": dlbAthDot11RxDecapFail,
       "dlbAthDot11RxDiscardMgt": dlbAthDot11RxDiscardMgt,
       "dlbAthDot11RxDiscardCtrl": dlbAthDot11RxDiscardCtrl,
       "dlbAthDot11RxBeaconFrames": dlbAthDot11RxBeaconFrames,
       "dlbAthDot11RxRateSetTrunc": dlbAthDot11RxRateSetTrunc,
       "dlbAthDot11RxReqElemMissing": dlbAthDot11RxReqElemMissing,
       "dlbAthDot11RxElementTooBig": dlbAthDot11RxElementTooBig,
       "dlbAthDot11RxElementTooSmall": dlbAthDot11RxElementTooSmall,
       "dlbAthDot11RxElementUnknown": dlbAthDot11RxElementUnknown,
       "dlbAthDot11RxInvalidChannel": dlbAthDot11RxInvalidChannel,
       "dlbAthDot11RxChannelMismatch": dlbAthDot11RxChannelMismatch,
       "dlbAthDot11RxNodesAllocated": dlbAthDot11RxNodesAllocated,
       "dlbAthDot11RxSsidMismatch": dlbAthDot11RxSsidMismatch,
       "dlbAthDot11RxUnsupportedAuthAlg": dlbAthDot11RxUnsupportedAuthAlg,
       "dlbAthDot11RxAuthFail": dlbAthDot11RxAuthFail,
       "dlbAthDot11RxTkipCtrm": dlbAthDot11RxTkipCtrm,
       "dlbAthDot11RxAssocWrongBssid": dlbAthDot11RxAssocWrongBssid,
       "dlbAthDot11RxAssocNotAuth": dlbAthDot11RxAssocNotAuth,
       "dlbAthDot11RxAssocCapMismatch": dlbAthDot11RxAssocCapMismatch,
       "dlbAthDot11RxAssocNoRateMatch": dlbAthDot11RxAssocNoRateMatch,
       "dlbAthDot11RxAssocBadWpaIe": dlbAthDot11RxAssocBadWpaIe,
       "dlbAthDot11RxDeauth": dlbAthDot11RxDeauth,
       "dlbAthDot11RxDisassoc": dlbAthDot11RxDisassoc,
       "dlbAthDot11RxUnknownSubtype": dlbAthDot11RxUnknownSubtype,
       "dlbAthDot11RxNoBuffer": dlbAthDot11RxNoBuffer,
       "dlbAthDot11RxDecryptCrcError": dlbAthDot11RxDecryptCrcError,
       "dlbAthDot11RxMgmtInAhdocDemo": dlbAthDot11RxMgmtInAhdocDemo,
       "dlbAthDot11RxBadAuthRequest": dlbAthDot11RxBadAuthRequest,
       "dlbAthDot11RxPortUnauth": dlbAthDot11RxPortUnauth,
       "dlbAthDot11RxBadKeyId": dlbAthDot11RxBadKeyId,
       "dlbAthDot11RxCcmpBadSeqNum": dlbAthDot11RxCcmpBadSeqNum,
       "dlbAthDot11RxCcmpBadFormat": dlbAthDot11RxCcmpBadFormat,
       "dlbAthDot11RxCcmpMicCheck": dlbAthDot11RxCcmpMicCheck,
       "dlbAthDot11RxTkipBadSeqNum": dlbAthDot11RxTkipBadSeqNum,
       "dlbAthDot11RxTkipBadFormat": dlbAthDot11RxTkipBadFormat,
       "dlbAthDot11RxTkipMicCheck": dlbAthDot11RxTkipMicCheck,
       "dlbAthDot11RxTkipIcvCheck": dlbAthDot11RxTkipIcvCheck,
       "dlbAthDot11RxBadCipherKeyType": dlbAthDot11RxBadCipherKeyType,
       "dlbAthDot11RxCipherKeyNotSet": dlbAthDot11RxCipherKeyNotSet,
       "dlbAthDot11RxAclPolicy": dlbAthDot11RxAclPolicy,
       "dlbAthDot11RxFastFrames": dlbAthDot11RxFastFrames,
       "dlbAthDot11RxFfBadTunnelHdr": dlbAthDot11RxFfBadTunnelHdr,
       "dlbAthDot11TxNoBuffer": dlbAthDot11TxNoBuffer,
       "dlbAthDot11TxNoNode": dlbAthDot11TxNoNode,
       "dlbAthDot11TxBadMgtFrames": dlbAthDot11TxBadMgtFrames,
       "dlbAthDot11TxBadCipherKeyType": dlbAthDot11TxBadCipherKeyType,
       "dlbAthDot11TxNoDefKey": dlbAthDot11TxNoDefKey,
       "dlbAthDot11TxNoCryptoHeadroom": dlbAthDot11TxNoCryptoHeadroom,
       "dlbAthDot11TxGoodFastFrames": dlbAthDot11TxGoodFastFrames,
       "dlbAthDot11TxBadFastFrames": dlbAthDot11TxBadFastFrames,
       "dlbAthDot11ActiveScans": dlbAthDot11ActiveScans,
       "dlbAthDot11PassiveScans": dlbAthDot11PassiveScans,
       "dlbAthDot11NodesTimeout": dlbAthDot11NodesTimeout,
       "dlbAthDot11CryptoCipherMalloc": dlbAthDot11CryptoCipherMalloc,
       "dlbAthDot11CryptoSwTkip": dlbAthDot11CryptoSwTkip,
       "dlbAthDot11CryptoTkipSwMicEnc": dlbAthDot11CryptoTkipSwMicEnc,
       "dlbAthDot11CryptoTkipSwMicDec": dlbAthDot11CryptoTkipSwMicDec,
       "dlbAthDot11CryptoTkipCtrm": dlbAthDot11CryptoTkipCtrm,
       "dlbAthDot11CryptoSwCcmp": dlbAthDot11CryptoSwCcmp,
       "dlbAthDot11CryptoSwWep": dlbAthDot11CryptoSwWep,
       "dlbAthDot11CryptoCipherRej": dlbAthDot11CryptoCipherRej,
       "dlbAthDot11CryptoNoKey": dlbAthDot11CryptoNoKey,
       "dlbAthDot11CryptoDelKey": dlbAthDot11CryptoDelKey,
       "dlbAthDot11CryptoBadCipher": dlbAthDot11CryptoBadCipher,
       "dlbAthDot11CryptoNoCipher": dlbAthDot11CryptoNoCipher,
       "dlbAthDot11CryptoAttachFail": dlbAthDot11CryptoAttachFail,
       "dlbAthDot11CryptoSwFallback": dlbAthDot11CryptoSwFallback,
       "dlbAthDot11CryptoKeyFail": dlbAthDot11CryptoKeyFail,
       "dlbAthDot11SnoopMcastPass": dlbAthDot11SnoopMcastPass,
       "dlbAthDot11SnoopMcastDrop": dlbAthDot11SnoopMcastDrop,
       "dlbAthPeerStatsTable": dlbAthPeerStatsTable,
       "dlbAthPeerStatsEntry": dlbAthPeerStatsEntry,
       "dlbAthPeerIndex": dlbAthPeerIndex,
       "dlbAthPeerMacAddr": dlbAthPeerMacAddr,
       "dlbAthPeerRxData": dlbAthPeerRxData,
       "dlbAthPeerRxMgmt": dlbAthPeerRxMgmt,
       "dlbAthPeerRxCtrl": dlbAthPeerRxCtrl,
       "dlbAthPeerRxBeacons": dlbAthPeerRxBeacons,
       "dlbAthPeerRxProbeResponse": dlbAthPeerRxProbeResponse,
       "dlbAthPeerRxUcast": dlbAthPeerRxUcast,
       "dlbAthPeerRxMcast": dlbAthPeerRxMcast,
       "dlbAthPeerRxBytes": dlbAthPeerRxBytes,
       "dlbAthPeerRxDup": dlbAthPeerRxDup,
       "dlbAthPeerRxNoPrivacy": dlbAthPeerRxNoPrivacy,
       "dlbAthPeerRxWepFail": dlbAthPeerRxWepFail,
       "dlbAthPeerRxDemicFail": dlbAthPeerRxDemicFail,
       "dlbAthPeerRxDecapFail": dlbAthPeerRxDecapFail,
       "dlbAthPeerRxDefragFail": dlbAthPeerRxDefragFail,
       "dlbAthPeerRxDissasoc": dlbAthPeerRxDissasoc,
       "dlbAthPeerRxDeauth": dlbAthPeerRxDeauth,
       "dlbAthPeerRxDecryptCrc": dlbAthPeerRxDecryptCrc,
       "dlbAthPeerRxUnauth": dlbAthPeerRxUnauth,
       "dlbAthPeerRxUnencrypted": dlbAthPeerRxUnencrypted,
       "dlbAthPeerTxData": dlbAthPeerTxData,
       "dlbAthPeerTxMgmt": dlbAthPeerTxMgmt,
       "dlbAthPeerTxProbeReq": dlbAthPeerTxProbeReq,
       "dlbAthPeerTxUcast": dlbAthPeerTxUcast,
       "dlbAthPeerTxMcast": dlbAthPeerTxMcast,
       "dlbAthPeerTxBytes": dlbAthPeerTxBytes,
       "dlbAthPeerTxNoVlanTag": dlbAthPeerTxNoVlanTag,
       "dlbAthPeerTxVlanMismatch": dlbAthPeerTxVlanMismatch,
       "dlbAthPeerTxUapsd": dlbAthPeerTxUapsd,
       "dlbAthPeerUapsdTriggers": dlbAthPeerUapsdTriggers,
       "dlbAthPeerTxEospLost": dlbAthPeerTxEospLost,
       "dlbAthPeerTxAssoc": dlbAthPeerTxAssoc,
       "dlbAthPeerTxAssocFail": dlbAthPeerTxAssocFail,
       "dlbAthPeerTxAuth": dlbAthPeerTxAuth,
       "dlbAthPeerTxAuthFail": dlbAthPeerTxAuthFail,
       "dlbAthPeerTxDeauth": dlbAthPeerTxDeauth,
       "dlbAthPeerTxDeauthCode": dlbAthPeerTxDeauthCode,
       "dlbAthPeerTxDisassoc": dlbAthPeerTxDisassoc,
       "dlbAthPeerTxDisassocCode": dlbAthPeerTxDisassocCode,
       "dlbAthPeerPsqDrops": dlbAthPeerPsqDrops,
       "dlbAthPeerMcastSnoop": dlbAthPeerMcastSnoop}
)
