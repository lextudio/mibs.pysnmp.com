# SNMP MIB module (LIGO-ATHDRV-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIGO-ATHDRV-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:10 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ligoMgmt,) = mibBuilder.importSymbols(
    "LIGOWAVE-MIB",
    "ligoMgmt")

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

ligoAthDrvStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7)
)
ligoAthDrvStatsMIB.setRevisions(
        ("2008-12-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LigoAthDrvStatsMIBObjects_ObjectIdentity = ObjectIdentity
ligoAthDrvStatsMIBObjects = _LigoAthDrvStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1)
)
_LigoAthStatsTable_Object = MibTable
ligoAthStatsTable = _LigoAthStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ligoAthStatsTable.setStatus("current")
_LigoAthStatsEntry_Object = MibTableRow
ligoAthStatsEntry = _LigoAthStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1)
)
ligoAthStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoAthStatsEntry.setStatus("current")
_LigoAthWatchdogTimeouts_Type = Counter32
_LigoAthWatchdogTimeouts_Object = MibTableColumn
ligoAthWatchdogTimeouts = _LigoAthWatchdogTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 1),
    _LigoAthWatchdogTimeouts_Type()
)
ligoAthWatchdogTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthWatchdogTimeouts.setStatus("current")
_LigoAthHardwareErrorInterrupts_Type = Counter32
_LigoAthHardwareErrorInterrupts_Object = MibTableColumn
ligoAthHardwareErrorInterrupts = _LigoAthHardwareErrorInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 2),
    _LigoAthHardwareErrorInterrupts_Type()
)
ligoAthHardwareErrorInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthHardwareErrorInterrupts.setStatus("current")
_LigoAthBeaconMissInterrupts_Type = Counter32
_LigoAthBeaconMissInterrupts_Object = MibTableColumn
ligoAthBeaconMissInterrupts = _LigoAthBeaconMissInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 3),
    _LigoAthBeaconMissInterrupts_Type()
)
ligoAthBeaconMissInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthBeaconMissInterrupts.setStatus("current")
_LigoAthRecvOverrunInterrupts_Type = Counter32
_LigoAthRecvOverrunInterrupts_Object = MibTableColumn
ligoAthRecvOverrunInterrupts = _LigoAthRecvOverrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 4),
    _LigoAthRecvOverrunInterrupts_Type()
)
ligoAthRecvOverrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRecvOverrunInterrupts.setStatus("current")
_LigoAthRecvEolInterrupts_Type = Counter32
_LigoAthRecvEolInterrupts_Object = MibTableColumn
ligoAthRecvEolInterrupts = _LigoAthRecvEolInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 5),
    _LigoAthRecvEolInterrupts_Type()
)
ligoAthRecvEolInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRecvEolInterrupts.setStatus("current")
_LigoAthTxmitUnderrunInterrupts_Type = Counter32
_LigoAthTxmitUnderrunInterrupts_Object = MibTableColumn
ligoAthTxmitUnderrunInterrupts = _LigoAthTxmitUnderrunInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 6),
    _LigoAthTxmitUnderrunInterrupts_Type()
)
ligoAthTxmitUnderrunInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxmitUnderrunInterrupts.setStatus("current")
_LigoAthTxManagementFrames_Type = Counter32
_LigoAthTxManagementFrames_Object = MibTableColumn
ligoAthTxManagementFrames = _LigoAthTxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 7),
    _LigoAthTxManagementFrames_Type()
)
ligoAthTxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxManagementFrames.setStatus("current")
_LigoAthTxFramesDiscQueueDepth_Type = Counter32
_LigoAthTxFramesDiscQueueDepth_Object = MibTableColumn
ligoAthTxFramesDiscQueueDepth = _LigoAthTxFramesDiscQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 8),
    _LigoAthTxFramesDiscQueueDepth_Type()
)
ligoAthTxFramesDiscQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesDiscQueueDepth.setStatus("current")
_LigoAthTxFramesDiscDeviceGone_Type = Counter32
_LigoAthTxFramesDiscDeviceGone_Object = MibTableColumn
ligoAthTxFramesDiscDeviceGone = _LigoAthTxFramesDiscDeviceGone_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 9),
    _LigoAthTxFramesDiscDeviceGone_Type()
)
ligoAthTxFramesDiscDeviceGone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesDiscDeviceGone.setStatus("current")
_LigoAthTxQueueFull_Type = Counter32
_LigoAthTxQueueFull_Object = MibTableColumn
ligoAthTxQueueFull = _LigoAthTxQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 10),
    _LigoAthTxQueueFull_Type()
)
ligoAthTxQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxQueueFull.setStatus("current")
_LigoAthTxEncapsulationFailed_Type = Counter32
_LigoAthTxEncapsulationFailed_Object = MibTableColumn
ligoAthTxEncapsulationFailed = _LigoAthTxEncapsulationFailed_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 11),
    _LigoAthTxEncapsulationFailed_Type()
)
ligoAthTxEncapsulationFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxEncapsulationFailed.setStatus("current")
_LigoAthTxFailedNoNode_Type = Counter32
_LigoAthTxFailedNoNode_Object = MibTableColumn
ligoAthTxFailedNoNode = _LigoAthTxFailedNoNode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 12),
    _LigoAthTxFailedNoNode_Type()
)
ligoAthTxFailedNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedNoNode.setStatus("current")
_LigoAthTxFailedNoDataTxBuffer_Type = Counter32
_LigoAthTxFailedNoDataTxBuffer_Object = MibTableColumn
ligoAthTxFailedNoDataTxBuffer = _LigoAthTxFailedNoDataTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 13),
    _LigoAthTxFailedNoDataTxBuffer_Type()
)
ligoAthTxFailedNoDataTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedNoDataTxBuffer.setStatus("current")
_LigoAthTxFailedNoMgtTxBuffer_Type = Counter32
_LigoAthTxFailedNoMgtTxBuffer_Object = MibTableColumn
ligoAthTxFailedNoMgtTxBuffer = _LigoAthTxFailedNoMgtTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 14),
    _LigoAthTxFailedNoMgtTxBuffer_Type()
)
ligoAthTxFailedNoMgtTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedNoMgtTxBuffer.setStatus("current")
_LigoAthTxFailedTooManyRetries_Type = Counter32
_LigoAthTxFailedTooManyRetries_Object = MibTableColumn
ligoAthTxFailedTooManyRetries = _LigoAthTxFailedTooManyRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 15),
    _LigoAthTxFailedTooManyRetries_Type()
)
ligoAthTxFailedTooManyRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedTooManyRetries.setStatus("current")
_LigoAthTxFailedFifoUnderrun_Type = Counter32
_LigoAthTxFailedFifoUnderrun_Object = MibTableColumn
ligoAthTxFailedFifoUnderrun = _LigoAthTxFailedFifoUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 16),
    _LigoAthTxFailedFifoUnderrun_Type()
)
ligoAthTxFailedFifoUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedFifoUnderrun.setStatus("current")
_LigoAthTxFailedXmitFiltered_Type = Counter32
_LigoAthTxFailedXmitFiltered_Object = MibTableColumn
ligoAthTxFailedXmitFiltered = _LigoAthTxFailedXmitFiltered_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 17),
    _LigoAthTxFailedXmitFiltered_Type()
)
ligoAthTxFailedXmitFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedXmitFiltered.setStatus("current")
_LigoAthShortOnchipTxRetries_Type = Counter32
_LigoAthShortOnchipTxRetries_Object = MibTableColumn
ligoAthShortOnchipTxRetries = _LigoAthShortOnchipTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 18),
    _LigoAthShortOnchipTxRetries_Type()
)
ligoAthShortOnchipTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthShortOnchipTxRetries.setStatus("current")
_LigoAthLongOnchipTxRetries_Type = Counter32
_LigoAthLongOnchipTxRetries_Object = MibTableColumn
ligoAthLongOnchipTxRetries = _LigoAthLongOnchipTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 19),
    _LigoAthLongOnchipTxRetries_Type()
)
ligoAthLongOnchipTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthLongOnchipTxRetries.setStatus("current")
_LigoAthTxFailedBogusXmitRate_Type = Counter32
_LigoAthTxFailedBogusXmitRate_Object = MibTableColumn
ligoAthTxFailedBogusXmitRate = _LigoAthTxFailedBogusXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 20),
    _LigoAthTxFailedBogusXmitRate_Type()
)
ligoAthTxFailedBogusXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFailedBogusXmitRate.setStatus("current")
_LigoAthTxFramesNoAckMarked_Type = Counter32
_LigoAthTxFramesNoAckMarked_Object = MibTableColumn
ligoAthTxFramesNoAckMarked = _LigoAthTxFramesNoAckMarked_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 21),
    _LigoAthTxFramesNoAckMarked_Type()
)
ligoAthTxFramesNoAckMarked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesNoAckMarked.setStatus("current")
_LigoAthTxFramesRtsEnabled_Type = Counter32
_LigoAthTxFramesRtsEnabled_Object = MibTableColumn
ligoAthTxFramesRtsEnabled = _LigoAthTxFramesRtsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 22),
    _LigoAthTxFramesRtsEnabled_Type()
)
ligoAthTxFramesRtsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesRtsEnabled.setStatus("current")
_LigoAthTxFramesCtsEnabled_Type = Counter32
_LigoAthTxFramesCtsEnabled_Object = MibTableColumn
ligoAthTxFramesCtsEnabled = _LigoAthTxFramesCtsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 23),
    _LigoAthTxFramesCtsEnabled_Type()
)
ligoAthTxFramesCtsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesCtsEnabled.setStatus("current")
_LigoAthTxFramesShortPreamble_Type = Counter32
_LigoAthTxFramesShortPreamble_Object = MibTableColumn
ligoAthTxFramesShortPreamble = _LigoAthTxFramesShortPreamble_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 24),
    _LigoAthTxFramesShortPreamble_Type()
)
ligoAthTxFramesShortPreamble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesShortPreamble.setStatus("current")
_LigoAthTxFramesAlternateRate_Type = Counter32
_LigoAthTxFramesAlternateRate_Object = MibTableColumn
ligoAthTxFramesAlternateRate = _LigoAthTxFramesAlternateRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 25),
    _LigoAthTxFramesAlternateRate_Type()
)
ligoAthTxFramesAlternateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesAlternateRate.setStatus("current")
_LigoAthTxFrames11gProtection_Type = Counter32
_LigoAthTxFrames11gProtection_Object = MibTableColumn
ligoAthTxFrames11gProtection = _LigoAthTxFrames11gProtection_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 26),
    _LigoAthTxFrames11gProtection_Type()
)
ligoAthTxFrames11gProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFrames11gProtection.setStatus("current")
_LigoAthRxFailedDescOverrun_Type = Counter32
_LigoAthRxFailedDescOverrun_Object = MibTableColumn
ligoAthRxFailedDescOverrun = _LigoAthRxFailedDescOverrun_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 27),
    _LigoAthRxFailedDescOverrun_Type()
)
ligoAthRxFailedDescOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedDescOverrun.setStatus("current")
_LigoAthRxFailedBadCrc_Type = Counter32
_LigoAthRxFailedBadCrc_Object = MibTableColumn
ligoAthRxFailedBadCrc = _LigoAthRxFailedBadCrc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 28),
    _LigoAthRxFailedBadCrc_Type()
)
ligoAthRxFailedBadCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedBadCrc.setStatus("current")
_LigoAthRxFailedFifoOverrun_Type = Counter32
_LigoAthRxFailedFifoOverrun_Object = MibTableColumn
ligoAthRxFailedFifoOverrun = _LigoAthRxFailedFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 29),
    _LigoAthRxFailedFifoOverrun_Type()
)
ligoAthRxFailedFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedFifoOverrun.setStatus("current")
_LigoAthRxFailedDecryptErrors_Type = Counter32
_LigoAthRxFailedDecryptErrors_Object = MibTableColumn
ligoAthRxFailedDecryptErrors = _LigoAthRxFailedDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 30),
    _LigoAthRxFailedDecryptErrors_Type()
)
ligoAthRxFailedDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedDecryptErrors.setStatus("current")
_LigoAthRxFailedMicFailure_Type = Counter32
_LigoAthRxFailedMicFailure_Object = MibTableColumn
ligoAthRxFailedMicFailure = _LigoAthRxFailedMicFailure_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 31),
    _LigoAthRxFailedMicFailure_Type()
)
ligoAthRxFailedMicFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedMicFailure.setStatus("current")
_LigoAthRxFailedFrameTooShort_Type = Counter32
_LigoAthRxFailedFrameTooShort_Object = MibTableColumn
ligoAthRxFailedFrameTooShort = _LigoAthRxFailedFrameTooShort_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 32),
    _LigoAthRxFailedFrameTooShort_Type()
)
ligoAthRxFailedFrameTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFailedFrameTooShort.setStatus("current")
_LigoAthRxSetupFailedNoSkbuff_Type = Counter32
_LigoAthRxSetupFailedNoSkbuff_Object = MibTableColumn
ligoAthRxSetupFailedNoSkbuff = _LigoAthRxSetupFailedNoSkbuff_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 33),
    _LigoAthRxSetupFailedNoSkbuff_Type()
)
ligoAthRxSetupFailedNoSkbuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxSetupFailedNoSkbuff.setStatus("current")
_LigoAthRxManagementFrames_Type = Counter32
_LigoAthRxManagementFrames_Object = MibTableColumn
ligoAthRxManagementFrames = _LigoAthRxManagementFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 34),
    _LigoAthRxManagementFrames_Type()
)
ligoAthRxManagementFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxManagementFrames.setStatus("current")
_LigoAthRxControlFrames_Type = Counter32
_LigoAthRxControlFrames_Object = MibTableColumn
ligoAthRxControlFrames = _LigoAthRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 35),
    _LigoAthRxControlFrames_Type()
)
ligoAthRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxControlFrames.setStatus("current")
_LigoAthNoSkbuffForBeacon_Type = Counter32
_LigoAthNoSkbuffForBeacon_Object = MibTableColumn
ligoAthNoSkbuffForBeacon = _LigoAthNoSkbuffForBeacon_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 36),
    _LigoAthNoSkbuffForBeacon_Type()
)
ligoAthNoSkbuffForBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthNoSkbuffForBeacon.setStatus("current")
_LigoAthBeaconsTransmitted_Type = Counter32
_LigoAthBeaconsTransmitted_Object = MibTableColumn
ligoAthBeaconsTransmitted = _LigoAthBeaconsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 37),
    _LigoAthBeaconsTransmitted_Type()
)
ligoAthBeaconsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthBeaconsTransmitted.setStatus("current")
_LigoAthPeriodicCalibrations_Type = Counter32
_LigoAthPeriodicCalibrations_Object = MibTableColumn
ligoAthPeriodicCalibrations = _LigoAthPeriodicCalibrations_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 38),
    _LigoAthPeriodicCalibrations_Type()
)
ligoAthPeriodicCalibrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeriodicCalibrations.setStatus("current")
_LigoAthPeriodicCalibrFailures_Type = Counter32
_LigoAthPeriodicCalibrFailures_Object = MibTableColumn
ligoAthPeriodicCalibrFailures = _LigoAthPeriodicCalibrFailures_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 39),
    _LigoAthPeriodicCalibrFailures_Type()
)
ligoAthPeriodicCalibrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeriodicCalibrFailures.setStatus("current")
_LigoAthRfgainValueChange_Type = Counter32
_LigoAthRfgainValueChange_Object = MibTableColumn
ligoAthRfgainValueChange = _LigoAthRfgainValueChange_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 40),
    _LigoAthRfgainValueChange_Type()
)
ligoAthRfgainValueChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRfgainValueChange.setStatus("current")
_LigoAthRateControlChecks_Type = Counter32
_LigoAthRateControlChecks_Object = MibTableColumn
ligoAthRateControlChecks = _LigoAthRateControlChecks_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 41),
    _LigoAthRateControlChecks_Type()
)
ligoAthRateControlChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRateControlChecks.setStatus("current")
_LigoAthRateCtrlRaisedXmitRate_Type = Counter32
_LigoAthRateCtrlRaisedXmitRate_Object = MibTableColumn
ligoAthRateCtrlRaisedXmitRate = _LigoAthRateCtrlRaisedXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 42),
    _LigoAthRateCtrlRaisedXmitRate_Type()
)
ligoAthRateCtrlRaisedXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRateCtrlRaisedXmitRate.setStatus("current")
_LigoAthRateCtrlDroppedXmitRate_Type = Counter32
_LigoAthRateCtrlDroppedXmitRate_Object = MibTableColumn
ligoAthRateCtrlDroppedXmitRate = _LigoAthRateCtrlDroppedXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 43),
    _LigoAthRateCtrlDroppedXmitRate_Type()
)
ligoAthRateCtrlDroppedXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRateCtrlDroppedXmitRate.setStatus("current")
_LigoAthRssiOfLastAck_Type = Gauge32
_LigoAthRssiOfLastAck_Object = MibTableColumn
ligoAthRssiOfLastAck = _LigoAthRssiOfLastAck_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 44),
    _LigoAthRssiOfLastAck_Type()
)
ligoAthRssiOfLastAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRssiOfLastAck.setStatus("current")
_LigoAthRssiOfLastRcv_Type = Gauge32
_LigoAthRssiOfLastRcv_Object = MibTableColumn
ligoAthRssiOfLastRcv = _LigoAthRssiOfLastRcv_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 1, 1, 45),
    _LigoAthRssiOfLastRcv_Type()
)
ligoAthRssiOfLastRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRssiOfLastRcv.setStatus("current")
_LigoAthPhyErrorsTable_Object = MibTable
ligoAthPhyErrorsTable = _LigoAthPhyErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ligoAthPhyErrorsTable.setStatus("current")
_LigoAthPhyErrorsEntry_Object = MibTableRow
ligoAthPhyErrorsEntry = _LigoAthPhyErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1)
)
ligoAthPhyErrorsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoAthPhyErrorsEntry.setStatus("current")
_LigoAthPhyTransmitUnderrun_Type = Counter32
_LigoAthPhyTransmitUnderrun_Object = MibTableColumn
ligoAthPhyTransmitUnderrun = _LigoAthPhyTransmitUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 1),
    _LigoAthPhyTransmitUnderrun_Type()
)
ligoAthPhyTransmitUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyTransmitUnderrun.setStatus("current")
_LigoAthPhyTimingError_Type = Counter32
_LigoAthPhyTimingError_Object = MibTableColumn
ligoAthPhyTimingError = _LigoAthPhyTimingError_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 2),
    _LigoAthPhyTimingError_Type()
)
ligoAthPhyTimingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyTimingError.setStatus("current")
_LigoAthPhyIllegalParity_Type = Counter32
_LigoAthPhyIllegalParity_Object = MibTableColumn
ligoAthPhyIllegalParity = _LigoAthPhyIllegalParity_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 3),
    _LigoAthPhyIllegalParity_Type()
)
ligoAthPhyIllegalParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyIllegalParity.setStatus("current")
_LigoAthPhyIllegalRate_Type = Counter32
_LigoAthPhyIllegalRate_Object = MibTableColumn
ligoAthPhyIllegalRate = _LigoAthPhyIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 4),
    _LigoAthPhyIllegalRate_Type()
)
ligoAthPhyIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyIllegalRate.setStatus("current")
_LigoAthPhyIllegalLength_Type = Counter32
_LigoAthPhyIllegalLength_Object = MibTableColumn
ligoAthPhyIllegalLength = _LigoAthPhyIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 5),
    _LigoAthPhyIllegalLength_Type()
)
ligoAthPhyIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyIllegalLength.setStatus("current")
_LigoAthPhyRadarDetect_Type = Counter32
_LigoAthPhyRadarDetect_Object = MibTableColumn
ligoAthPhyRadarDetect = _LigoAthPhyRadarDetect_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 6),
    _LigoAthPhyRadarDetect_Type()
)
ligoAthPhyRadarDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyRadarDetect.setStatus("current")
_LigoAthPhyIllegalService_Type = Counter32
_LigoAthPhyIllegalService_Object = MibTableColumn
ligoAthPhyIllegalService = _LigoAthPhyIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 7),
    _LigoAthPhyIllegalService_Type()
)
ligoAthPhyIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyIllegalService.setStatus("current")
_LigoAthPhyTxmitOverrideRecv_Type = Counter32
_LigoAthPhyTxmitOverrideRecv_Object = MibTableColumn
ligoAthPhyTxmitOverrideRecv = _LigoAthPhyTxmitOverrideRecv_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 8),
    _LigoAthPhyTxmitOverrideRecv_Type()
)
ligoAthPhyTxmitOverrideRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyTxmitOverrideRecv.setStatus("current")
_LigoAthPhyOfdmTiming_Type = Counter32
_LigoAthPhyOfdmTiming_Object = MibTableColumn
ligoAthPhyOfdmTiming = _LigoAthPhyOfdmTiming_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 9),
    _LigoAthPhyOfdmTiming_Type()
)
ligoAthPhyOfdmTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmTiming.setStatus("current")
_LigoAthPhyOfdmIllegalParity_Type = Counter32
_LigoAthPhyOfdmIllegalParity_Object = MibTableColumn
ligoAthPhyOfdmIllegalParity = _LigoAthPhyOfdmIllegalParity_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 10),
    _LigoAthPhyOfdmIllegalParity_Type()
)
ligoAthPhyOfdmIllegalParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmIllegalParity.setStatus("current")
_LigoAthPhyOfdmIllegalRate_Type = Counter32
_LigoAthPhyOfdmIllegalRate_Object = MibTableColumn
ligoAthPhyOfdmIllegalRate = _LigoAthPhyOfdmIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 11),
    _LigoAthPhyOfdmIllegalRate_Type()
)
ligoAthPhyOfdmIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmIllegalRate.setStatus("current")
_LigoAthPhyOfdmIllegalLength_Type = Counter32
_LigoAthPhyOfdmIllegalLength_Object = MibTableColumn
ligoAthPhyOfdmIllegalLength = _LigoAthPhyOfdmIllegalLength_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 12),
    _LigoAthPhyOfdmIllegalLength_Type()
)
ligoAthPhyOfdmIllegalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmIllegalLength.setStatus("current")
_LigoAthPhyOfdmPowerDrop_Type = Counter32
_LigoAthPhyOfdmPowerDrop_Object = MibTableColumn
ligoAthPhyOfdmPowerDrop = _LigoAthPhyOfdmPowerDrop_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 13),
    _LigoAthPhyOfdmPowerDrop_Type()
)
ligoAthPhyOfdmPowerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmPowerDrop.setStatus("current")
_LigoAthPhyOfdmIllegalService_Type = Counter32
_LigoAthPhyOfdmIllegalService_Object = MibTableColumn
ligoAthPhyOfdmIllegalService = _LigoAthPhyOfdmIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 14),
    _LigoAthPhyOfdmIllegalService_Type()
)
ligoAthPhyOfdmIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmIllegalService.setStatus("current")
_LigoAthPhyOfdmRestart_Type = Counter32
_LigoAthPhyOfdmRestart_Object = MibTableColumn
ligoAthPhyOfdmRestart = _LigoAthPhyOfdmRestart_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 15),
    _LigoAthPhyOfdmRestart_Type()
)
ligoAthPhyOfdmRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyOfdmRestart.setStatus("current")
_LigoAthPhyCckTiming_Type = Counter32
_LigoAthPhyCckTiming_Object = MibTableColumn
ligoAthPhyCckTiming = _LigoAthPhyCckTiming_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 16),
    _LigoAthPhyCckTiming_Type()
)
ligoAthPhyCckTiming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyCckTiming.setStatus("current")
_LigoAthPhyCckHeaderCrc_Type = Counter32
_LigoAthPhyCckHeaderCrc_Object = MibTableColumn
ligoAthPhyCckHeaderCrc = _LigoAthPhyCckHeaderCrc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 17),
    _LigoAthPhyCckHeaderCrc_Type()
)
ligoAthPhyCckHeaderCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyCckHeaderCrc.setStatus("current")
_LigoAthPhyCckIllegalRate_Type = Counter32
_LigoAthPhyCckIllegalRate_Object = MibTableColumn
ligoAthPhyCckIllegalRate = _LigoAthPhyCckIllegalRate_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 18),
    _LigoAthPhyCckIllegalRate_Type()
)
ligoAthPhyCckIllegalRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyCckIllegalRate.setStatus("current")
_LigoAthPhyCckIllegalService_Type = Counter32
_LigoAthPhyCckIllegalService_Object = MibTableColumn
ligoAthPhyCckIllegalService = _LigoAthPhyCckIllegalService_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 19),
    _LigoAthPhyCckIllegalService_Type()
)
ligoAthPhyCckIllegalService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyCckIllegalService.setStatus("current")
_LigoAthPhyCckRestart_Type = Counter32
_LigoAthPhyCckRestart_Object = MibTableColumn
ligoAthPhyCckRestart = _LigoAthPhyCckRestart_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 2, 1, 20),
    _LigoAthPhyCckRestart_Type()
)
ligoAthPhyCckRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPhyCckRestart.setStatus("current")
_LigoAthAntennaStatsTable_Object = MibTable
ligoAthAntennaStatsTable = _LigoAthAntennaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ligoAthAntennaStatsTable.setStatus("current")
_LigoAthAntennaStatsEntry_Object = MibTableRow
ligoAthAntennaStatsEntry = _LigoAthAntennaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1)
)
ligoAthAntennaStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoAthAntennaStatsEntry.setStatus("current")
_LigoAthSwitchedDefaultRxAntenna_Type = Counter32
_LigoAthSwitchedDefaultRxAntenna_Object = MibTableColumn
ligoAthSwitchedDefaultRxAntenna = _LigoAthSwitchedDefaultRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 1),
    _LigoAthSwitchedDefaultRxAntenna_Type()
)
ligoAthSwitchedDefaultRxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthSwitchedDefaultRxAntenna.setStatus("current")
_LigoAthTxUsedAlternateAntenna_Type = Counter32
_LigoAthTxUsedAlternateAntenna_Object = MibTableColumn
ligoAthTxUsedAlternateAntenna = _LigoAthTxUsedAlternateAntenna_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 2),
    _LigoAthTxUsedAlternateAntenna_Type()
)
ligoAthTxUsedAlternateAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxUsedAlternateAntenna.setStatus("current")
_LigoAthTxFramesAntenna1_Type = Counter32
_LigoAthTxFramesAntenna1_Object = MibTableColumn
ligoAthTxFramesAntenna1 = _LigoAthTxFramesAntenna1_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 3),
    _LigoAthTxFramesAntenna1_Type()
)
ligoAthTxFramesAntenna1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesAntenna1.setStatus("current")
_LigoAthRxFramesAntenna1_Type = Counter32
_LigoAthRxFramesAntenna1_Object = MibTableColumn
ligoAthRxFramesAntenna1 = _LigoAthRxFramesAntenna1_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 4),
    _LigoAthRxFramesAntenna1_Type()
)
ligoAthRxFramesAntenna1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFramesAntenna1.setStatus("current")
_LigoAthTxFramesAntenna2_Type = Counter32
_LigoAthTxFramesAntenna2_Object = MibTableColumn
ligoAthTxFramesAntenna2 = _LigoAthTxFramesAntenna2_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 5),
    _LigoAthTxFramesAntenna2_Type()
)
ligoAthTxFramesAntenna2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesAntenna2.setStatus("current")
_LigoAthRxFramesAntenna2_Type = Counter32
_LigoAthRxFramesAntenna2_Object = MibTableColumn
ligoAthRxFramesAntenna2 = _LigoAthRxFramesAntenna2_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 6),
    _LigoAthRxFramesAntenna2_Type()
)
ligoAthRxFramesAntenna2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFramesAntenna2.setStatus("current")
_LigoAthTxFramesAntenna3_Type = Counter32
_LigoAthTxFramesAntenna3_Object = MibTableColumn
ligoAthTxFramesAntenna3 = _LigoAthTxFramesAntenna3_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 7),
    _LigoAthTxFramesAntenna3_Type()
)
ligoAthTxFramesAntenna3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthTxFramesAntenna3.setStatus("current")
_LigoAthRxFramesAntenna3_Type = Counter32
_LigoAthRxFramesAntenna3_Object = MibTableColumn
ligoAthRxFramesAntenna3 = _LigoAthRxFramesAntenna3_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 3, 1, 8),
    _LigoAthRxFramesAntenna3_Type()
)
ligoAthRxFramesAntenna3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthRxFramesAntenna3.setStatus("current")
_LigoAthDot11StatsTable_Object = MibTable
ligoAthDot11StatsTable = _LigoAthDot11StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ligoAthDot11StatsTable.setStatus("current")
_LigoAthDot11StatsEntry_Object = MibTableRow
ligoAthDot11StatsEntry = _LigoAthDot11StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1)
)
ligoAthDot11StatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ligoAthDot11StatsEntry.setStatus("current")
_LigoAthDot11RxBadVersion_Type = Counter32
_LigoAthDot11RxBadVersion_Object = MibTableColumn
ligoAthDot11RxBadVersion = _LigoAthDot11RxBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 1),
    _LigoAthDot11RxBadVersion_Type()
)
ligoAthDot11RxBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxBadVersion.setStatus("current")
_LigoAthDot11RxTooShort_Type = Counter32
_LigoAthDot11RxTooShort_Object = MibTableColumn
ligoAthDot11RxTooShort = _LigoAthDot11RxTooShort_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 2),
    _LigoAthDot11RxTooShort_Type()
)
ligoAthDot11RxTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTooShort.setStatus("current")
_LigoAthDot11RxWrongBssid_Type = Counter32
_LigoAthDot11RxWrongBssid_Object = MibTableColumn
ligoAthDot11RxWrongBssid = _LigoAthDot11RxWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 3),
    _LigoAthDot11RxWrongBssid_Type()
)
ligoAthDot11RxWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxWrongBssid.setStatus("current")
_LigoAthDot11RxDup_Type = Counter32
_LigoAthDot11RxDup_Object = MibTableColumn
ligoAthDot11RxDup = _LigoAthDot11RxDup_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 4),
    _LigoAthDot11RxDup_Type()
)
ligoAthDot11RxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDup.setStatus("current")
_LigoAthDot11RxWrongDirection_Type = Counter32
_LigoAthDot11RxWrongDirection_Object = MibTableColumn
ligoAthDot11RxWrongDirection = _LigoAthDot11RxWrongDirection_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 5),
    _LigoAthDot11RxWrongDirection_Type()
)
ligoAthDot11RxWrongDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxWrongDirection.setStatus("current")
_LigoAthDot11RxMcastEcho_Type = Counter32
_LigoAthDot11RxMcastEcho_Object = MibTableColumn
ligoAthDot11RxMcastEcho = _LigoAthDot11RxMcastEcho_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 6),
    _LigoAthDot11RxMcastEcho_Type()
)
ligoAthDot11RxMcastEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxMcastEcho.setStatus("current")
_LigoAthDot11RxNotAssoc_Type = Counter32
_LigoAthDot11RxNotAssoc_Object = MibTableColumn
ligoAthDot11RxNotAssoc = _LigoAthDot11RxNotAssoc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 7),
    _LigoAthDot11RxNotAssoc_Type()
)
ligoAthDot11RxNotAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxNotAssoc.setStatus("current")
_LigoAthDot11RxNoPrivacy_Type = Counter32
_LigoAthDot11RxNoPrivacy_Object = MibTableColumn
ligoAthDot11RxNoPrivacy = _LigoAthDot11RxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 8),
    _LigoAthDot11RxNoPrivacy_Type()
)
ligoAthDot11RxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxNoPrivacy.setStatus("current")
_LigoAthDot11RxUnencrypted_Type = Counter32
_LigoAthDot11RxUnencrypted_Object = MibTableColumn
ligoAthDot11RxUnencrypted = _LigoAthDot11RxUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 9),
    _LigoAthDot11RxUnencrypted_Type()
)
ligoAthDot11RxUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxUnencrypted.setStatus("current")
_LigoAthDot11RxWepFail_Type = Counter32
_LigoAthDot11RxWepFail_Object = MibTableColumn
ligoAthDot11RxWepFail = _LigoAthDot11RxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 10),
    _LigoAthDot11RxWepFail_Type()
)
ligoAthDot11RxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxWepFail.setStatus("current")
_LigoAthDot11RxDecapFail_Type = Counter32
_LigoAthDot11RxDecapFail_Object = MibTableColumn
ligoAthDot11RxDecapFail = _LigoAthDot11RxDecapFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 11),
    _LigoAthDot11RxDecapFail_Type()
)
ligoAthDot11RxDecapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDecapFail.setStatus("current")
_LigoAthDot11RxDiscardMgt_Type = Counter32
_LigoAthDot11RxDiscardMgt_Object = MibTableColumn
ligoAthDot11RxDiscardMgt = _LigoAthDot11RxDiscardMgt_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 12),
    _LigoAthDot11RxDiscardMgt_Type()
)
ligoAthDot11RxDiscardMgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDiscardMgt.setStatus("current")
_LigoAthDot11RxDiscardCtrl_Type = Counter32
_LigoAthDot11RxDiscardCtrl_Object = MibTableColumn
ligoAthDot11RxDiscardCtrl = _LigoAthDot11RxDiscardCtrl_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 13),
    _LigoAthDot11RxDiscardCtrl_Type()
)
ligoAthDot11RxDiscardCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDiscardCtrl.setStatus("current")
_LigoAthDot11RxBeaconFrames_Type = Counter32
_LigoAthDot11RxBeaconFrames_Object = MibTableColumn
ligoAthDot11RxBeaconFrames = _LigoAthDot11RxBeaconFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 14),
    _LigoAthDot11RxBeaconFrames_Type()
)
ligoAthDot11RxBeaconFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxBeaconFrames.setStatus("current")
_LigoAthDot11RxRateSetTrunc_Type = Counter32
_LigoAthDot11RxRateSetTrunc_Object = MibTableColumn
ligoAthDot11RxRateSetTrunc = _LigoAthDot11RxRateSetTrunc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 15),
    _LigoAthDot11RxRateSetTrunc_Type()
)
ligoAthDot11RxRateSetTrunc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxRateSetTrunc.setStatus("current")
_LigoAthDot11RxReqElemMissing_Type = Counter32
_LigoAthDot11RxReqElemMissing_Object = MibTableColumn
ligoAthDot11RxReqElemMissing = _LigoAthDot11RxReqElemMissing_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 16),
    _LigoAthDot11RxReqElemMissing_Type()
)
ligoAthDot11RxReqElemMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxReqElemMissing.setStatus("current")
_LigoAthDot11RxElementTooBig_Type = Counter32
_LigoAthDot11RxElementTooBig_Object = MibTableColumn
ligoAthDot11RxElementTooBig = _LigoAthDot11RxElementTooBig_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 17),
    _LigoAthDot11RxElementTooBig_Type()
)
ligoAthDot11RxElementTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxElementTooBig.setStatus("current")
_LigoAthDot11RxElementTooSmall_Type = Counter32
_LigoAthDot11RxElementTooSmall_Object = MibTableColumn
ligoAthDot11RxElementTooSmall = _LigoAthDot11RxElementTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 18),
    _LigoAthDot11RxElementTooSmall_Type()
)
ligoAthDot11RxElementTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxElementTooSmall.setStatus("current")
_LigoAthDot11RxElementUnknown_Type = Counter32
_LigoAthDot11RxElementUnknown_Object = MibTableColumn
ligoAthDot11RxElementUnknown = _LigoAthDot11RxElementUnknown_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 19),
    _LigoAthDot11RxElementUnknown_Type()
)
ligoAthDot11RxElementUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxElementUnknown.setStatus("current")
_LigoAthDot11RxInvalidChannel_Type = Counter32
_LigoAthDot11RxInvalidChannel_Object = MibTableColumn
ligoAthDot11RxInvalidChannel = _LigoAthDot11RxInvalidChannel_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 20),
    _LigoAthDot11RxInvalidChannel_Type()
)
ligoAthDot11RxInvalidChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxInvalidChannel.setStatus("current")
_LigoAthDot11RxChannelMismatch_Type = Counter32
_LigoAthDot11RxChannelMismatch_Object = MibTableColumn
ligoAthDot11RxChannelMismatch = _LigoAthDot11RxChannelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 21),
    _LigoAthDot11RxChannelMismatch_Type()
)
ligoAthDot11RxChannelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxChannelMismatch.setStatus("current")
_LigoAthDot11RxNodesAllocated_Type = Counter32
_LigoAthDot11RxNodesAllocated_Object = MibTableColumn
ligoAthDot11RxNodesAllocated = _LigoAthDot11RxNodesAllocated_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 22),
    _LigoAthDot11RxNodesAllocated_Type()
)
ligoAthDot11RxNodesAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxNodesAllocated.setStatus("current")
_LigoAthDot11RxSsidMismatch_Type = Counter32
_LigoAthDot11RxSsidMismatch_Object = MibTableColumn
ligoAthDot11RxSsidMismatch = _LigoAthDot11RxSsidMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 23),
    _LigoAthDot11RxSsidMismatch_Type()
)
ligoAthDot11RxSsidMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxSsidMismatch.setStatus("current")
_LigoAthDot11RxUnsupportedAuthAlg_Type = Counter32
_LigoAthDot11RxUnsupportedAuthAlg_Object = MibTableColumn
ligoAthDot11RxUnsupportedAuthAlg = _LigoAthDot11RxUnsupportedAuthAlg_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 24),
    _LigoAthDot11RxUnsupportedAuthAlg_Type()
)
ligoAthDot11RxUnsupportedAuthAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxUnsupportedAuthAlg.setStatus("current")
_LigoAthDot11RxAuthFail_Type = Counter32
_LigoAthDot11RxAuthFail_Object = MibTableColumn
ligoAthDot11RxAuthFail = _LigoAthDot11RxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 25),
    _LigoAthDot11RxAuthFail_Type()
)
ligoAthDot11RxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAuthFail.setStatus("current")
_LigoAthDot11RxTkipCtrm_Type = Counter32
_LigoAthDot11RxTkipCtrm_Object = MibTableColumn
ligoAthDot11RxTkipCtrm = _LigoAthDot11RxTkipCtrm_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 26),
    _LigoAthDot11RxTkipCtrm_Type()
)
ligoAthDot11RxTkipCtrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTkipCtrm.setStatus("current")
_LigoAthDot11RxAssocWrongBssid_Type = Counter32
_LigoAthDot11RxAssocWrongBssid_Object = MibTableColumn
ligoAthDot11RxAssocWrongBssid = _LigoAthDot11RxAssocWrongBssid_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 27),
    _LigoAthDot11RxAssocWrongBssid_Type()
)
ligoAthDot11RxAssocWrongBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAssocWrongBssid.setStatus("current")
_LigoAthDot11RxAssocNotAuth_Type = Counter32
_LigoAthDot11RxAssocNotAuth_Object = MibTableColumn
ligoAthDot11RxAssocNotAuth = _LigoAthDot11RxAssocNotAuth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 28),
    _LigoAthDot11RxAssocNotAuth_Type()
)
ligoAthDot11RxAssocNotAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAssocNotAuth.setStatus("current")
_LigoAthDot11RxAssocCapMismatch_Type = Counter32
_LigoAthDot11RxAssocCapMismatch_Object = MibTableColumn
ligoAthDot11RxAssocCapMismatch = _LigoAthDot11RxAssocCapMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 29),
    _LigoAthDot11RxAssocCapMismatch_Type()
)
ligoAthDot11RxAssocCapMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAssocCapMismatch.setStatus("current")
_LigoAthDot11RxAssocNoRateMatch_Type = Counter32
_LigoAthDot11RxAssocNoRateMatch_Object = MibTableColumn
ligoAthDot11RxAssocNoRateMatch = _LigoAthDot11RxAssocNoRateMatch_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 30),
    _LigoAthDot11RxAssocNoRateMatch_Type()
)
ligoAthDot11RxAssocNoRateMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAssocNoRateMatch.setStatus("current")
_LigoAthDot11RxAssocBadWpaIe_Type = Counter32
_LigoAthDot11RxAssocBadWpaIe_Object = MibTableColumn
ligoAthDot11RxAssocBadWpaIe = _LigoAthDot11RxAssocBadWpaIe_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 31),
    _LigoAthDot11RxAssocBadWpaIe_Type()
)
ligoAthDot11RxAssocBadWpaIe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAssocBadWpaIe.setStatus("current")
_LigoAthDot11RxDeauth_Type = Counter32
_LigoAthDot11RxDeauth_Object = MibTableColumn
ligoAthDot11RxDeauth = _LigoAthDot11RxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 32),
    _LigoAthDot11RxDeauth_Type()
)
ligoAthDot11RxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDeauth.setStatus("current")
_LigoAthDot11RxDisassoc_Type = Counter32
_LigoAthDot11RxDisassoc_Object = MibTableColumn
ligoAthDot11RxDisassoc = _LigoAthDot11RxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 33),
    _LigoAthDot11RxDisassoc_Type()
)
ligoAthDot11RxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDisassoc.setStatus("current")
_LigoAthDot11RxUnknownSubtype_Type = Counter32
_LigoAthDot11RxUnknownSubtype_Object = MibTableColumn
ligoAthDot11RxUnknownSubtype = _LigoAthDot11RxUnknownSubtype_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 34),
    _LigoAthDot11RxUnknownSubtype_Type()
)
ligoAthDot11RxUnknownSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxUnknownSubtype.setStatus("current")
_LigoAthDot11RxNoBuffer_Type = Counter32
_LigoAthDot11RxNoBuffer_Object = MibTableColumn
ligoAthDot11RxNoBuffer = _LigoAthDot11RxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 35),
    _LigoAthDot11RxNoBuffer_Type()
)
ligoAthDot11RxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxNoBuffer.setStatus("current")
_LigoAthDot11RxDecryptCrcError_Type = Counter32
_LigoAthDot11RxDecryptCrcError_Object = MibTableColumn
ligoAthDot11RxDecryptCrcError = _LigoAthDot11RxDecryptCrcError_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 36),
    _LigoAthDot11RxDecryptCrcError_Type()
)
ligoAthDot11RxDecryptCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxDecryptCrcError.setStatus("current")
_LigoAthDot11RxMgmtInAhdocDemo_Type = Counter32
_LigoAthDot11RxMgmtInAhdocDemo_Object = MibTableColumn
ligoAthDot11RxMgmtInAhdocDemo = _LigoAthDot11RxMgmtInAhdocDemo_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 37),
    _LigoAthDot11RxMgmtInAhdocDemo_Type()
)
ligoAthDot11RxMgmtInAhdocDemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxMgmtInAhdocDemo.setStatus("current")
_LigoAthDot11RxBadAuthRequest_Type = Counter32
_LigoAthDot11RxBadAuthRequest_Object = MibTableColumn
ligoAthDot11RxBadAuthRequest = _LigoAthDot11RxBadAuthRequest_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 38),
    _LigoAthDot11RxBadAuthRequest_Type()
)
ligoAthDot11RxBadAuthRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxBadAuthRequest.setStatus("current")
_LigoAthDot11RxPortUnauth_Type = Counter32
_LigoAthDot11RxPortUnauth_Object = MibTableColumn
ligoAthDot11RxPortUnauth = _LigoAthDot11RxPortUnauth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 39),
    _LigoAthDot11RxPortUnauth_Type()
)
ligoAthDot11RxPortUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxPortUnauth.setStatus("current")
_LigoAthDot11RxBadKeyId_Type = Counter32
_LigoAthDot11RxBadKeyId_Object = MibTableColumn
ligoAthDot11RxBadKeyId = _LigoAthDot11RxBadKeyId_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 40),
    _LigoAthDot11RxBadKeyId_Type()
)
ligoAthDot11RxBadKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxBadKeyId.setStatus("current")
_LigoAthDot11RxCcmpBadSeqNum_Type = Counter32
_LigoAthDot11RxCcmpBadSeqNum_Object = MibTableColumn
ligoAthDot11RxCcmpBadSeqNum = _LigoAthDot11RxCcmpBadSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 41),
    _LigoAthDot11RxCcmpBadSeqNum_Type()
)
ligoAthDot11RxCcmpBadSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxCcmpBadSeqNum.setStatus("current")
_LigoAthDot11RxCcmpBadFormat_Type = Counter32
_LigoAthDot11RxCcmpBadFormat_Object = MibTableColumn
ligoAthDot11RxCcmpBadFormat = _LigoAthDot11RxCcmpBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 42),
    _LigoAthDot11RxCcmpBadFormat_Type()
)
ligoAthDot11RxCcmpBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxCcmpBadFormat.setStatus("current")
_LigoAthDot11RxCcmpMicCheck_Type = Counter32
_LigoAthDot11RxCcmpMicCheck_Object = MibTableColumn
ligoAthDot11RxCcmpMicCheck = _LigoAthDot11RxCcmpMicCheck_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 43),
    _LigoAthDot11RxCcmpMicCheck_Type()
)
ligoAthDot11RxCcmpMicCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxCcmpMicCheck.setStatus("current")
_LigoAthDot11RxTkipBadSeqNum_Type = Counter32
_LigoAthDot11RxTkipBadSeqNum_Object = MibTableColumn
ligoAthDot11RxTkipBadSeqNum = _LigoAthDot11RxTkipBadSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 44),
    _LigoAthDot11RxTkipBadSeqNum_Type()
)
ligoAthDot11RxTkipBadSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTkipBadSeqNum.setStatus("current")
_LigoAthDot11RxTkipBadFormat_Type = Counter32
_LigoAthDot11RxTkipBadFormat_Object = MibTableColumn
ligoAthDot11RxTkipBadFormat = _LigoAthDot11RxTkipBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 45),
    _LigoAthDot11RxTkipBadFormat_Type()
)
ligoAthDot11RxTkipBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTkipBadFormat.setStatus("current")
_LigoAthDot11RxTkipMicCheck_Type = Counter32
_LigoAthDot11RxTkipMicCheck_Object = MibTableColumn
ligoAthDot11RxTkipMicCheck = _LigoAthDot11RxTkipMicCheck_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 46),
    _LigoAthDot11RxTkipMicCheck_Type()
)
ligoAthDot11RxTkipMicCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTkipMicCheck.setStatus("current")
_LigoAthDot11RxTkipIcvCheck_Type = Counter32
_LigoAthDot11RxTkipIcvCheck_Object = MibTableColumn
ligoAthDot11RxTkipIcvCheck = _LigoAthDot11RxTkipIcvCheck_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 47),
    _LigoAthDot11RxTkipIcvCheck_Type()
)
ligoAthDot11RxTkipIcvCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxTkipIcvCheck.setStatus("current")
_LigoAthDot11RxBadCipherKeyType_Type = Counter32
_LigoAthDot11RxBadCipherKeyType_Object = MibTableColumn
ligoAthDot11RxBadCipherKeyType = _LigoAthDot11RxBadCipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 48),
    _LigoAthDot11RxBadCipherKeyType_Type()
)
ligoAthDot11RxBadCipherKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxBadCipherKeyType.setStatus("current")
_LigoAthDot11RxCipherKeyNotSet_Type = Counter32
_LigoAthDot11RxCipherKeyNotSet_Object = MibTableColumn
ligoAthDot11RxCipherKeyNotSet = _LigoAthDot11RxCipherKeyNotSet_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 49),
    _LigoAthDot11RxCipherKeyNotSet_Type()
)
ligoAthDot11RxCipherKeyNotSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxCipherKeyNotSet.setStatus("current")
_LigoAthDot11RxAclPolicy_Type = Counter32
_LigoAthDot11RxAclPolicy_Object = MibTableColumn
ligoAthDot11RxAclPolicy = _LigoAthDot11RxAclPolicy_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 50),
    _LigoAthDot11RxAclPolicy_Type()
)
ligoAthDot11RxAclPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxAclPolicy.setStatus("current")
_LigoAthDot11RxFastFrames_Type = Counter32
_LigoAthDot11RxFastFrames_Object = MibTableColumn
ligoAthDot11RxFastFrames = _LigoAthDot11RxFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 51),
    _LigoAthDot11RxFastFrames_Type()
)
ligoAthDot11RxFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxFastFrames.setStatus("current")
_LigoAthDot11RxFfBadTunnelHdr_Type = Counter32
_LigoAthDot11RxFfBadTunnelHdr_Object = MibTableColumn
ligoAthDot11RxFfBadTunnelHdr = _LigoAthDot11RxFfBadTunnelHdr_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 52),
    _LigoAthDot11RxFfBadTunnelHdr_Type()
)
ligoAthDot11RxFfBadTunnelHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11RxFfBadTunnelHdr.setStatus("current")
_LigoAthDot11TxNoBuffer_Type = Counter32
_LigoAthDot11TxNoBuffer_Object = MibTableColumn
ligoAthDot11TxNoBuffer = _LigoAthDot11TxNoBuffer_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 53),
    _LigoAthDot11TxNoBuffer_Type()
)
ligoAthDot11TxNoBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxNoBuffer.setStatus("current")
_LigoAthDot11TxNoNode_Type = Counter32
_LigoAthDot11TxNoNode_Object = MibTableColumn
ligoAthDot11TxNoNode = _LigoAthDot11TxNoNode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 54),
    _LigoAthDot11TxNoNode_Type()
)
ligoAthDot11TxNoNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxNoNode.setStatus("current")
_LigoAthDot11TxBadMgtFrames_Type = Counter32
_LigoAthDot11TxBadMgtFrames_Object = MibTableColumn
ligoAthDot11TxBadMgtFrames = _LigoAthDot11TxBadMgtFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 55),
    _LigoAthDot11TxBadMgtFrames_Type()
)
ligoAthDot11TxBadMgtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxBadMgtFrames.setStatus("current")
_LigoAthDot11TxBadCipherKeyType_Type = Counter32
_LigoAthDot11TxBadCipherKeyType_Object = MibTableColumn
ligoAthDot11TxBadCipherKeyType = _LigoAthDot11TxBadCipherKeyType_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 56),
    _LigoAthDot11TxBadCipherKeyType_Type()
)
ligoAthDot11TxBadCipherKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxBadCipherKeyType.setStatus("current")
_LigoAthDot11TxNoDefKey_Type = Counter32
_LigoAthDot11TxNoDefKey_Object = MibTableColumn
ligoAthDot11TxNoDefKey = _LigoAthDot11TxNoDefKey_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 57),
    _LigoAthDot11TxNoDefKey_Type()
)
ligoAthDot11TxNoDefKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxNoDefKey.setStatus("current")
_LigoAthDot11TxNoCryptoHeadroom_Type = Counter32
_LigoAthDot11TxNoCryptoHeadroom_Object = MibTableColumn
ligoAthDot11TxNoCryptoHeadroom = _LigoAthDot11TxNoCryptoHeadroom_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 58),
    _LigoAthDot11TxNoCryptoHeadroom_Type()
)
ligoAthDot11TxNoCryptoHeadroom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxNoCryptoHeadroom.setStatus("current")
_LigoAthDot11TxGoodFastFrames_Type = Counter32
_LigoAthDot11TxGoodFastFrames_Object = MibTableColumn
ligoAthDot11TxGoodFastFrames = _LigoAthDot11TxGoodFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 59),
    _LigoAthDot11TxGoodFastFrames_Type()
)
ligoAthDot11TxGoodFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxGoodFastFrames.setStatus("current")
_LigoAthDot11TxBadFastFrames_Type = Counter32
_LigoAthDot11TxBadFastFrames_Object = MibTableColumn
ligoAthDot11TxBadFastFrames = _LigoAthDot11TxBadFastFrames_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 60),
    _LigoAthDot11TxBadFastFrames_Type()
)
ligoAthDot11TxBadFastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11TxBadFastFrames.setStatus("current")
_LigoAthDot11ActiveScans_Type = Counter32
_LigoAthDot11ActiveScans_Object = MibTableColumn
ligoAthDot11ActiveScans = _LigoAthDot11ActiveScans_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 61),
    _LigoAthDot11ActiveScans_Type()
)
ligoAthDot11ActiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11ActiveScans.setStatus("current")
_LigoAthDot11PassiveScans_Type = Counter32
_LigoAthDot11PassiveScans_Object = MibTableColumn
ligoAthDot11PassiveScans = _LigoAthDot11PassiveScans_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 62),
    _LigoAthDot11PassiveScans_Type()
)
ligoAthDot11PassiveScans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11PassiveScans.setStatus("current")
_LigoAthDot11NodesTimeout_Type = Counter32
_LigoAthDot11NodesTimeout_Object = MibTableColumn
ligoAthDot11NodesTimeout = _LigoAthDot11NodesTimeout_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 63),
    _LigoAthDot11NodesTimeout_Type()
)
ligoAthDot11NodesTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11NodesTimeout.setStatus("current")
_LigoAthDot11CryptoCipherMalloc_Type = Counter32
_LigoAthDot11CryptoCipherMalloc_Object = MibTableColumn
ligoAthDot11CryptoCipherMalloc = _LigoAthDot11CryptoCipherMalloc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 64),
    _LigoAthDot11CryptoCipherMalloc_Type()
)
ligoAthDot11CryptoCipherMalloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoCipherMalloc.setStatus("current")
_LigoAthDot11CryptoSwTkip_Type = Counter32
_LigoAthDot11CryptoSwTkip_Object = MibTableColumn
ligoAthDot11CryptoSwTkip = _LigoAthDot11CryptoSwTkip_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 65),
    _LigoAthDot11CryptoSwTkip_Type()
)
ligoAthDot11CryptoSwTkip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoSwTkip.setStatus("current")
_LigoAthDot11CryptoTkipSwMicEnc_Type = Counter32
_LigoAthDot11CryptoTkipSwMicEnc_Object = MibTableColumn
ligoAthDot11CryptoTkipSwMicEnc = _LigoAthDot11CryptoTkipSwMicEnc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 66),
    _LigoAthDot11CryptoTkipSwMicEnc_Type()
)
ligoAthDot11CryptoTkipSwMicEnc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoTkipSwMicEnc.setStatus("current")
_LigoAthDot11CryptoTkipSwMicDec_Type = Counter32
_LigoAthDot11CryptoTkipSwMicDec_Object = MibTableColumn
ligoAthDot11CryptoTkipSwMicDec = _LigoAthDot11CryptoTkipSwMicDec_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 67),
    _LigoAthDot11CryptoTkipSwMicDec_Type()
)
ligoAthDot11CryptoTkipSwMicDec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoTkipSwMicDec.setStatus("current")
_LigoAthDot11CryptoTkipCtrm_Type = Counter32
_LigoAthDot11CryptoTkipCtrm_Object = MibTableColumn
ligoAthDot11CryptoTkipCtrm = _LigoAthDot11CryptoTkipCtrm_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 68),
    _LigoAthDot11CryptoTkipCtrm_Type()
)
ligoAthDot11CryptoTkipCtrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoTkipCtrm.setStatus("current")
_LigoAthDot11CryptoSwCcmp_Type = Counter32
_LigoAthDot11CryptoSwCcmp_Object = MibTableColumn
ligoAthDot11CryptoSwCcmp = _LigoAthDot11CryptoSwCcmp_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 69),
    _LigoAthDot11CryptoSwCcmp_Type()
)
ligoAthDot11CryptoSwCcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoSwCcmp.setStatus("current")
_LigoAthDot11CryptoSwWep_Type = Counter32
_LigoAthDot11CryptoSwWep_Object = MibTableColumn
ligoAthDot11CryptoSwWep = _LigoAthDot11CryptoSwWep_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 70),
    _LigoAthDot11CryptoSwWep_Type()
)
ligoAthDot11CryptoSwWep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoSwWep.setStatus("current")
_LigoAthDot11CryptoCipherRej_Type = Counter32
_LigoAthDot11CryptoCipherRej_Object = MibTableColumn
ligoAthDot11CryptoCipherRej = _LigoAthDot11CryptoCipherRej_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 71),
    _LigoAthDot11CryptoCipherRej_Type()
)
ligoAthDot11CryptoCipherRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoCipherRej.setStatus("current")
_LigoAthDot11CryptoNoKey_Type = Counter32
_LigoAthDot11CryptoNoKey_Object = MibTableColumn
ligoAthDot11CryptoNoKey = _LigoAthDot11CryptoNoKey_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 72),
    _LigoAthDot11CryptoNoKey_Type()
)
ligoAthDot11CryptoNoKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoNoKey.setStatus("current")
_LigoAthDot11CryptoDelKey_Type = Counter32
_LigoAthDot11CryptoDelKey_Object = MibTableColumn
ligoAthDot11CryptoDelKey = _LigoAthDot11CryptoDelKey_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 73),
    _LigoAthDot11CryptoDelKey_Type()
)
ligoAthDot11CryptoDelKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoDelKey.setStatus("current")
_LigoAthDot11CryptoBadCipher_Type = Counter32
_LigoAthDot11CryptoBadCipher_Object = MibTableColumn
ligoAthDot11CryptoBadCipher = _LigoAthDot11CryptoBadCipher_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 74),
    _LigoAthDot11CryptoBadCipher_Type()
)
ligoAthDot11CryptoBadCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoBadCipher.setStatus("current")
_LigoAthDot11CryptoNoCipher_Type = Counter32
_LigoAthDot11CryptoNoCipher_Object = MibTableColumn
ligoAthDot11CryptoNoCipher = _LigoAthDot11CryptoNoCipher_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 75),
    _LigoAthDot11CryptoNoCipher_Type()
)
ligoAthDot11CryptoNoCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoNoCipher.setStatus("current")
_LigoAthDot11CryptoAttachFail_Type = Counter32
_LigoAthDot11CryptoAttachFail_Object = MibTableColumn
ligoAthDot11CryptoAttachFail = _LigoAthDot11CryptoAttachFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 76),
    _LigoAthDot11CryptoAttachFail_Type()
)
ligoAthDot11CryptoAttachFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoAttachFail.setStatus("current")
_LigoAthDot11CryptoSwFallback_Type = Counter32
_LigoAthDot11CryptoSwFallback_Object = MibTableColumn
ligoAthDot11CryptoSwFallback = _LigoAthDot11CryptoSwFallback_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 77),
    _LigoAthDot11CryptoSwFallback_Type()
)
ligoAthDot11CryptoSwFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoSwFallback.setStatus("current")
_LigoAthDot11CryptoKeyFail_Type = Counter32
_LigoAthDot11CryptoKeyFail_Object = MibTableColumn
ligoAthDot11CryptoKeyFail = _LigoAthDot11CryptoKeyFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 78),
    _LigoAthDot11CryptoKeyFail_Type()
)
ligoAthDot11CryptoKeyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11CryptoKeyFail.setStatus("current")
_LigoAthDot11SnoopMcastPass_Type = Counter32
_LigoAthDot11SnoopMcastPass_Object = MibTableColumn
ligoAthDot11SnoopMcastPass = _LigoAthDot11SnoopMcastPass_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 79),
    _LigoAthDot11SnoopMcastPass_Type()
)
ligoAthDot11SnoopMcastPass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11SnoopMcastPass.setStatus("current")
_LigoAthDot11SnoopMcastDrop_Type = Counter32
_LigoAthDot11SnoopMcastDrop_Object = MibTableColumn
ligoAthDot11SnoopMcastDrop = _LigoAthDot11SnoopMcastDrop_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 4, 1, 80),
    _LigoAthDot11SnoopMcastDrop_Type()
)
ligoAthDot11SnoopMcastDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthDot11SnoopMcastDrop.setStatus("current")
_LigoAthPeerStatsTable_Object = MibTable
ligoAthPeerStatsTable = _LigoAthPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5)
)
if mibBuilder.loadTexts:
    ligoAthPeerStatsTable.setStatus("current")
_LigoAthPeerStatsEntry_Object = MibTableRow
ligoAthPeerStatsEntry = _LigoAthPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1)
)
ligoAthPeerStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LIGO-ATHDRV-STATS-MIB", "ligoAthPeerIndex"),
)
if mibBuilder.loadTexts:
    ligoAthPeerStatsEntry.setStatus("current")
_LigoAthPeerIndex_Type = Integer32
_LigoAthPeerIndex_Object = MibTableColumn
ligoAthPeerIndex = _LigoAthPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 1),
    _LigoAthPeerIndex_Type()
)
ligoAthPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ligoAthPeerIndex.setStatus("current")
_LigoAthPeerMacAddr_Type = MacAddress
_LigoAthPeerMacAddr_Object = MibTableColumn
ligoAthPeerMacAddr = _LigoAthPeerMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 2),
    _LigoAthPeerMacAddr_Type()
)
ligoAthPeerMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerMacAddr.setStatus("current")
_LigoAthPeerRxData_Type = Counter32
_LigoAthPeerRxData_Object = MibTableColumn
ligoAthPeerRxData = _LigoAthPeerRxData_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 3),
    _LigoAthPeerRxData_Type()
)
ligoAthPeerRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxData.setStatus("current")
_LigoAthPeerRxMgmt_Type = Counter32
_LigoAthPeerRxMgmt_Object = MibTableColumn
ligoAthPeerRxMgmt = _LigoAthPeerRxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 4),
    _LigoAthPeerRxMgmt_Type()
)
ligoAthPeerRxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxMgmt.setStatus("current")
_LigoAthPeerRxCtrl_Type = Counter32
_LigoAthPeerRxCtrl_Object = MibTableColumn
ligoAthPeerRxCtrl = _LigoAthPeerRxCtrl_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 5),
    _LigoAthPeerRxCtrl_Type()
)
ligoAthPeerRxCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxCtrl.setStatus("current")
_LigoAthPeerRxBeacons_Type = Counter64
_LigoAthPeerRxBeacons_Object = MibTableColumn
ligoAthPeerRxBeacons = _LigoAthPeerRxBeacons_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 6),
    _LigoAthPeerRxBeacons_Type()
)
ligoAthPeerRxBeacons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxBeacons.setStatus("current")
_LigoAthPeerRxProbeResponse_Type = Counter32
_LigoAthPeerRxProbeResponse_Object = MibTableColumn
ligoAthPeerRxProbeResponse = _LigoAthPeerRxProbeResponse_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 7),
    _LigoAthPeerRxProbeResponse_Type()
)
ligoAthPeerRxProbeResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxProbeResponse.setStatus("current")
_LigoAthPeerRxUcast_Type = Counter32
_LigoAthPeerRxUcast_Object = MibTableColumn
ligoAthPeerRxUcast = _LigoAthPeerRxUcast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 8),
    _LigoAthPeerRxUcast_Type()
)
ligoAthPeerRxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxUcast.setStatus("current")
_LigoAthPeerRxMcast_Type = Counter32
_LigoAthPeerRxMcast_Object = MibTableColumn
ligoAthPeerRxMcast = _LigoAthPeerRxMcast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 9),
    _LigoAthPeerRxMcast_Type()
)
ligoAthPeerRxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxMcast.setStatus("current")
_LigoAthPeerRxBytes_Type = Counter64
_LigoAthPeerRxBytes_Object = MibTableColumn
ligoAthPeerRxBytes = _LigoAthPeerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 10),
    _LigoAthPeerRxBytes_Type()
)
ligoAthPeerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxBytes.setStatus("current")
_LigoAthPeerRxDup_Type = Counter32
_LigoAthPeerRxDup_Object = MibTableColumn
ligoAthPeerRxDup = _LigoAthPeerRxDup_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 11),
    _LigoAthPeerRxDup_Type()
)
ligoAthPeerRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDup.setStatus("current")
_LigoAthPeerRxNoPrivacy_Type = Counter32
_LigoAthPeerRxNoPrivacy_Object = MibTableColumn
ligoAthPeerRxNoPrivacy = _LigoAthPeerRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 12),
    _LigoAthPeerRxNoPrivacy_Type()
)
ligoAthPeerRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxNoPrivacy.setStatus("current")
_LigoAthPeerRxWepFail_Type = Counter32
_LigoAthPeerRxWepFail_Object = MibTableColumn
ligoAthPeerRxWepFail = _LigoAthPeerRxWepFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 13),
    _LigoAthPeerRxWepFail_Type()
)
ligoAthPeerRxWepFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxWepFail.setStatus("current")
_LigoAthPeerRxDemicFail_Type = Counter32
_LigoAthPeerRxDemicFail_Object = MibTableColumn
ligoAthPeerRxDemicFail = _LigoAthPeerRxDemicFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 14),
    _LigoAthPeerRxDemicFail_Type()
)
ligoAthPeerRxDemicFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDemicFail.setStatus("current")
_LigoAthPeerRxDecapFail_Type = Counter32
_LigoAthPeerRxDecapFail_Object = MibTableColumn
ligoAthPeerRxDecapFail = _LigoAthPeerRxDecapFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 15),
    _LigoAthPeerRxDecapFail_Type()
)
ligoAthPeerRxDecapFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDecapFail.setStatus("current")
_LigoAthPeerRxDefragFail_Type = Counter32
_LigoAthPeerRxDefragFail_Object = MibTableColumn
ligoAthPeerRxDefragFail = _LigoAthPeerRxDefragFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 16),
    _LigoAthPeerRxDefragFail_Type()
)
ligoAthPeerRxDefragFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDefragFail.setStatus("current")
_LigoAthPeerRxDissasoc_Type = Counter32
_LigoAthPeerRxDissasoc_Object = MibTableColumn
ligoAthPeerRxDissasoc = _LigoAthPeerRxDissasoc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 17),
    _LigoAthPeerRxDissasoc_Type()
)
ligoAthPeerRxDissasoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDissasoc.setStatus("current")
_LigoAthPeerRxDeauth_Type = Counter32
_LigoAthPeerRxDeauth_Object = MibTableColumn
ligoAthPeerRxDeauth = _LigoAthPeerRxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 18),
    _LigoAthPeerRxDeauth_Type()
)
ligoAthPeerRxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDeauth.setStatus("current")
_LigoAthPeerRxDecryptCrc_Type = Counter32
_LigoAthPeerRxDecryptCrc_Object = MibTableColumn
ligoAthPeerRxDecryptCrc = _LigoAthPeerRxDecryptCrc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 19),
    _LigoAthPeerRxDecryptCrc_Type()
)
ligoAthPeerRxDecryptCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxDecryptCrc.setStatus("current")
_LigoAthPeerRxUnauth_Type = Counter32
_LigoAthPeerRxUnauth_Object = MibTableColumn
ligoAthPeerRxUnauth = _LigoAthPeerRxUnauth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 20),
    _LigoAthPeerRxUnauth_Type()
)
ligoAthPeerRxUnauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxUnauth.setStatus("current")
_LigoAthPeerRxUnencrypted_Type = Counter32
_LigoAthPeerRxUnencrypted_Object = MibTableColumn
ligoAthPeerRxUnencrypted = _LigoAthPeerRxUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 21),
    _LigoAthPeerRxUnencrypted_Type()
)
ligoAthPeerRxUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerRxUnencrypted.setStatus("current")
_LigoAthPeerTxData_Type = Counter32
_LigoAthPeerTxData_Object = MibTableColumn
ligoAthPeerTxData = _LigoAthPeerTxData_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 22),
    _LigoAthPeerTxData_Type()
)
ligoAthPeerTxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxData.setStatus("current")
_LigoAthPeerTxMgmt_Type = Counter32
_LigoAthPeerTxMgmt_Object = MibTableColumn
ligoAthPeerTxMgmt = _LigoAthPeerTxMgmt_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 23),
    _LigoAthPeerTxMgmt_Type()
)
ligoAthPeerTxMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxMgmt.setStatus("current")
_LigoAthPeerTxProbeReq_Type = Counter32
_LigoAthPeerTxProbeReq_Object = MibTableColumn
ligoAthPeerTxProbeReq = _LigoAthPeerTxProbeReq_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 24),
    _LigoAthPeerTxProbeReq_Type()
)
ligoAthPeerTxProbeReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxProbeReq.setStatus("current")
_LigoAthPeerTxUcast_Type = Counter32
_LigoAthPeerTxUcast_Object = MibTableColumn
ligoAthPeerTxUcast = _LigoAthPeerTxUcast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 25),
    _LigoAthPeerTxUcast_Type()
)
ligoAthPeerTxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxUcast.setStatus("current")
_LigoAthPeerTxMcast_Type = Counter32
_LigoAthPeerTxMcast_Object = MibTableColumn
ligoAthPeerTxMcast = _LigoAthPeerTxMcast_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 26),
    _LigoAthPeerTxMcast_Type()
)
ligoAthPeerTxMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxMcast.setStatus("current")
_LigoAthPeerTxBytes_Type = Counter64
_LigoAthPeerTxBytes_Object = MibTableColumn
ligoAthPeerTxBytes = _LigoAthPeerTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 27),
    _LigoAthPeerTxBytes_Type()
)
ligoAthPeerTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxBytes.setStatus("current")
_LigoAthPeerTxNoVlanTag_Type = Counter32
_LigoAthPeerTxNoVlanTag_Object = MibTableColumn
ligoAthPeerTxNoVlanTag = _LigoAthPeerTxNoVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 28),
    _LigoAthPeerTxNoVlanTag_Type()
)
ligoAthPeerTxNoVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxNoVlanTag.setStatus("current")
_LigoAthPeerTxVlanMismatch_Type = Counter32
_LigoAthPeerTxVlanMismatch_Object = MibTableColumn
ligoAthPeerTxVlanMismatch = _LigoAthPeerTxVlanMismatch_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 29),
    _LigoAthPeerTxVlanMismatch_Type()
)
ligoAthPeerTxVlanMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxVlanMismatch.setStatus("current")
_LigoAthPeerTxUapsd_Type = Counter32
_LigoAthPeerTxUapsd_Object = MibTableColumn
ligoAthPeerTxUapsd = _LigoAthPeerTxUapsd_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 30),
    _LigoAthPeerTxUapsd_Type()
)
ligoAthPeerTxUapsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxUapsd.setStatus("current")
_LigoAthPeerUapsdTriggers_Type = Counter32
_LigoAthPeerUapsdTriggers_Object = MibTableColumn
ligoAthPeerUapsdTriggers = _LigoAthPeerUapsdTriggers_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 31),
    _LigoAthPeerUapsdTriggers_Type()
)
ligoAthPeerUapsdTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerUapsdTriggers.setStatus("current")
_LigoAthPeerTxEospLost_Type = Counter32
_LigoAthPeerTxEospLost_Object = MibTableColumn
ligoAthPeerTxEospLost = _LigoAthPeerTxEospLost_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 32),
    _LigoAthPeerTxEospLost_Type()
)
ligoAthPeerTxEospLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxEospLost.setStatus("current")
_LigoAthPeerTxAssoc_Type = Counter32
_LigoAthPeerTxAssoc_Object = MibTableColumn
ligoAthPeerTxAssoc = _LigoAthPeerTxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 33),
    _LigoAthPeerTxAssoc_Type()
)
ligoAthPeerTxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxAssoc.setStatus("current")
_LigoAthPeerTxAssocFail_Type = Counter32
_LigoAthPeerTxAssocFail_Object = MibTableColumn
ligoAthPeerTxAssocFail = _LigoAthPeerTxAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 34),
    _LigoAthPeerTxAssocFail_Type()
)
ligoAthPeerTxAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxAssocFail.setStatus("current")
_LigoAthPeerTxAuth_Type = Counter32
_LigoAthPeerTxAuth_Object = MibTableColumn
ligoAthPeerTxAuth = _LigoAthPeerTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 35),
    _LigoAthPeerTxAuth_Type()
)
ligoAthPeerTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxAuth.setStatus("current")
_LigoAthPeerTxAuthFail_Type = Counter32
_LigoAthPeerTxAuthFail_Object = MibTableColumn
ligoAthPeerTxAuthFail = _LigoAthPeerTxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 36),
    _LigoAthPeerTxAuthFail_Type()
)
ligoAthPeerTxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxAuthFail.setStatus("current")
_LigoAthPeerTxDeauth_Type = Counter32
_LigoAthPeerTxDeauth_Object = MibTableColumn
ligoAthPeerTxDeauth = _LigoAthPeerTxDeauth_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 37),
    _LigoAthPeerTxDeauth_Type()
)
ligoAthPeerTxDeauth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxDeauth.setStatus("current")
_LigoAthPeerTxDeauthCode_Type = Counter32
_LigoAthPeerTxDeauthCode_Object = MibTableColumn
ligoAthPeerTxDeauthCode = _LigoAthPeerTxDeauthCode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 38),
    _LigoAthPeerTxDeauthCode_Type()
)
ligoAthPeerTxDeauthCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxDeauthCode.setStatus("current")
_LigoAthPeerTxDisassoc_Type = Counter32
_LigoAthPeerTxDisassoc_Object = MibTableColumn
ligoAthPeerTxDisassoc = _LigoAthPeerTxDisassoc_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 39),
    _LigoAthPeerTxDisassoc_Type()
)
ligoAthPeerTxDisassoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxDisassoc.setStatus("current")
_LigoAthPeerTxDisassocCode_Type = Counter32
_LigoAthPeerTxDisassocCode_Object = MibTableColumn
ligoAthPeerTxDisassocCode = _LigoAthPeerTxDisassocCode_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 40),
    _LigoAthPeerTxDisassocCode_Type()
)
ligoAthPeerTxDisassocCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerTxDisassocCode.setStatus("current")
_LigoAthPeerPsqDrops_Type = Counter32
_LigoAthPeerPsqDrops_Object = MibTableColumn
ligoAthPeerPsqDrops = _LigoAthPeerPsqDrops_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 41),
    _LigoAthPeerPsqDrops_Type()
)
ligoAthPeerPsqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerPsqDrops.setStatus("current")
_LigoAthPeerMcastSnoop_Type = Counter32
_LigoAthPeerMcastSnoop_Object = MibTableColumn
ligoAthPeerMcastSnoop = _LigoAthPeerMcastSnoop_Object(
    (1, 3, 6, 1, 4, 1, 32750, 3, 7, 1, 5, 1, 42),
    _LigoAthPeerMcastSnoop_Type()
)
ligoAthPeerMcastSnoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ligoAthPeerMcastSnoop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIGO-ATHDRV-STATS-MIB",
    **{"ligoAthDrvStatsMIB": ligoAthDrvStatsMIB,
       "ligoAthDrvStatsMIBObjects": ligoAthDrvStatsMIBObjects,
       "ligoAthStatsTable": ligoAthStatsTable,
       "ligoAthStatsEntry": ligoAthStatsEntry,
       "ligoAthWatchdogTimeouts": ligoAthWatchdogTimeouts,
       "ligoAthHardwareErrorInterrupts": ligoAthHardwareErrorInterrupts,
       "ligoAthBeaconMissInterrupts": ligoAthBeaconMissInterrupts,
       "ligoAthRecvOverrunInterrupts": ligoAthRecvOverrunInterrupts,
       "ligoAthRecvEolInterrupts": ligoAthRecvEolInterrupts,
       "ligoAthTxmitUnderrunInterrupts": ligoAthTxmitUnderrunInterrupts,
       "ligoAthTxManagementFrames": ligoAthTxManagementFrames,
       "ligoAthTxFramesDiscQueueDepth": ligoAthTxFramesDiscQueueDepth,
       "ligoAthTxFramesDiscDeviceGone": ligoAthTxFramesDiscDeviceGone,
       "ligoAthTxQueueFull": ligoAthTxQueueFull,
       "ligoAthTxEncapsulationFailed": ligoAthTxEncapsulationFailed,
       "ligoAthTxFailedNoNode": ligoAthTxFailedNoNode,
       "ligoAthTxFailedNoDataTxBuffer": ligoAthTxFailedNoDataTxBuffer,
       "ligoAthTxFailedNoMgtTxBuffer": ligoAthTxFailedNoMgtTxBuffer,
       "ligoAthTxFailedTooManyRetries": ligoAthTxFailedTooManyRetries,
       "ligoAthTxFailedFifoUnderrun": ligoAthTxFailedFifoUnderrun,
       "ligoAthTxFailedXmitFiltered": ligoAthTxFailedXmitFiltered,
       "ligoAthShortOnchipTxRetries": ligoAthShortOnchipTxRetries,
       "ligoAthLongOnchipTxRetries": ligoAthLongOnchipTxRetries,
       "ligoAthTxFailedBogusXmitRate": ligoAthTxFailedBogusXmitRate,
       "ligoAthTxFramesNoAckMarked": ligoAthTxFramesNoAckMarked,
       "ligoAthTxFramesRtsEnabled": ligoAthTxFramesRtsEnabled,
       "ligoAthTxFramesCtsEnabled": ligoAthTxFramesCtsEnabled,
       "ligoAthTxFramesShortPreamble": ligoAthTxFramesShortPreamble,
       "ligoAthTxFramesAlternateRate": ligoAthTxFramesAlternateRate,
       "ligoAthTxFrames11gProtection": ligoAthTxFrames11gProtection,
       "ligoAthRxFailedDescOverrun": ligoAthRxFailedDescOverrun,
       "ligoAthRxFailedBadCrc": ligoAthRxFailedBadCrc,
       "ligoAthRxFailedFifoOverrun": ligoAthRxFailedFifoOverrun,
       "ligoAthRxFailedDecryptErrors": ligoAthRxFailedDecryptErrors,
       "ligoAthRxFailedMicFailure": ligoAthRxFailedMicFailure,
       "ligoAthRxFailedFrameTooShort": ligoAthRxFailedFrameTooShort,
       "ligoAthRxSetupFailedNoSkbuff": ligoAthRxSetupFailedNoSkbuff,
       "ligoAthRxManagementFrames": ligoAthRxManagementFrames,
       "ligoAthRxControlFrames": ligoAthRxControlFrames,
       "ligoAthNoSkbuffForBeacon": ligoAthNoSkbuffForBeacon,
       "ligoAthBeaconsTransmitted": ligoAthBeaconsTransmitted,
       "ligoAthPeriodicCalibrations": ligoAthPeriodicCalibrations,
       "ligoAthPeriodicCalibrFailures": ligoAthPeriodicCalibrFailures,
       "ligoAthRfgainValueChange": ligoAthRfgainValueChange,
       "ligoAthRateControlChecks": ligoAthRateControlChecks,
       "ligoAthRateCtrlRaisedXmitRate": ligoAthRateCtrlRaisedXmitRate,
       "ligoAthRateCtrlDroppedXmitRate": ligoAthRateCtrlDroppedXmitRate,
       "ligoAthRssiOfLastAck": ligoAthRssiOfLastAck,
       "ligoAthRssiOfLastRcv": ligoAthRssiOfLastRcv,
       "ligoAthPhyErrorsTable": ligoAthPhyErrorsTable,
       "ligoAthPhyErrorsEntry": ligoAthPhyErrorsEntry,
       "ligoAthPhyTransmitUnderrun": ligoAthPhyTransmitUnderrun,
       "ligoAthPhyTimingError": ligoAthPhyTimingError,
       "ligoAthPhyIllegalParity": ligoAthPhyIllegalParity,
       "ligoAthPhyIllegalRate": ligoAthPhyIllegalRate,
       "ligoAthPhyIllegalLength": ligoAthPhyIllegalLength,
       "ligoAthPhyRadarDetect": ligoAthPhyRadarDetect,
       "ligoAthPhyIllegalService": ligoAthPhyIllegalService,
       "ligoAthPhyTxmitOverrideRecv": ligoAthPhyTxmitOverrideRecv,
       "ligoAthPhyOfdmTiming": ligoAthPhyOfdmTiming,
       "ligoAthPhyOfdmIllegalParity": ligoAthPhyOfdmIllegalParity,
       "ligoAthPhyOfdmIllegalRate": ligoAthPhyOfdmIllegalRate,
       "ligoAthPhyOfdmIllegalLength": ligoAthPhyOfdmIllegalLength,
       "ligoAthPhyOfdmPowerDrop": ligoAthPhyOfdmPowerDrop,
       "ligoAthPhyOfdmIllegalService": ligoAthPhyOfdmIllegalService,
       "ligoAthPhyOfdmRestart": ligoAthPhyOfdmRestart,
       "ligoAthPhyCckTiming": ligoAthPhyCckTiming,
       "ligoAthPhyCckHeaderCrc": ligoAthPhyCckHeaderCrc,
       "ligoAthPhyCckIllegalRate": ligoAthPhyCckIllegalRate,
       "ligoAthPhyCckIllegalService": ligoAthPhyCckIllegalService,
       "ligoAthPhyCckRestart": ligoAthPhyCckRestart,
       "ligoAthAntennaStatsTable": ligoAthAntennaStatsTable,
       "ligoAthAntennaStatsEntry": ligoAthAntennaStatsEntry,
       "ligoAthSwitchedDefaultRxAntenna": ligoAthSwitchedDefaultRxAntenna,
       "ligoAthTxUsedAlternateAntenna": ligoAthTxUsedAlternateAntenna,
       "ligoAthTxFramesAntenna1": ligoAthTxFramesAntenna1,
       "ligoAthRxFramesAntenna1": ligoAthRxFramesAntenna1,
       "ligoAthTxFramesAntenna2": ligoAthTxFramesAntenna2,
       "ligoAthRxFramesAntenna2": ligoAthRxFramesAntenna2,
       "ligoAthTxFramesAntenna3": ligoAthTxFramesAntenna3,
       "ligoAthRxFramesAntenna3": ligoAthRxFramesAntenna3,
       "ligoAthDot11StatsTable": ligoAthDot11StatsTable,
       "ligoAthDot11StatsEntry": ligoAthDot11StatsEntry,
       "ligoAthDot11RxBadVersion": ligoAthDot11RxBadVersion,
       "ligoAthDot11RxTooShort": ligoAthDot11RxTooShort,
       "ligoAthDot11RxWrongBssid": ligoAthDot11RxWrongBssid,
       "ligoAthDot11RxDup": ligoAthDot11RxDup,
       "ligoAthDot11RxWrongDirection": ligoAthDot11RxWrongDirection,
       "ligoAthDot11RxMcastEcho": ligoAthDot11RxMcastEcho,
       "ligoAthDot11RxNotAssoc": ligoAthDot11RxNotAssoc,
       "ligoAthDot11RxNoPrivacy": ligoAthDot11RxNoPrivacy,
       "ligoAthDot11RxUnencrypted": ligoAthDot11RxUnencrypted,
       "ligoAthDot11RxWepFail": ligoAthDot11RxWepFail,
       "ligoAthDot11RxDecapFail": ligoAthDot11RxDecapFail,
       "ligoAthDot11RxDiscardMgt": ligoAthDot11RxDiscardMgt,
       "ligoAthDot11RxDiscardCtrl": ligoAthDot11RxDiscardCtrl,
       "ligoAthDot11RxBeaconFrames": ligoAthDot11RxBeaconFrames,
       "ligoAthDot11RxRateSetTrunc": ligoAthDot11RxRateSetTrunc,
       "ligoAthDot11RxReqElemMissing": ligoAthDot11RxReqElemMissing,
       "ligoAthDot11RxElementTooBig": ligoAthDot11RxElementTooBig,
       "ligoAthDot11RxElementTooSmall": ligoAthDot11RxElementTooSmall,
       "ligoAthDot11RxElementUnknown": ligoAthDot11RxElementUnknown,
       "ligoAthDot11RxInvalidChannel": ligoAthDot11RxInvalidChannel,
       "ligoAthDot11RxChannelMismatch": ligoAthDot11RxChannelMismatch,
       "ligoAthDot11RxNodesAllocated": ligoAthDot11RxNodesAllocated,
       "ligoAthDot11RxSsidMismatch": ligoAthDot11RxSsidMismatch,
       "ligoAthDot11RxUnsupportedAuthAlg": ligoAthDot11RxUnsupportedAuthAlg,
       "ligoAthDot11RxAuthFail": ligoAthDot11RxAuthFail,
       "ligoAthDot11RxTkipCtrm": ligoAthDot11RxTkipCtrm,
       "ligoAthDot11RxAssocWrongBssid": ligoAthDot11RxAssocWrongBssid,
       "ligoAthDot11RxAssocNotAuth": ligoAthDot11RxAssocNotAuth,
       "ligoAthDot11RxAssocCapMismatch": ligoAthDot11RxAssocCapMismatch,
       "ligoAthDot11RxAssocNoRateMatch": ligoAthDot11RxAssocNoRateMatch,
       "ligoAthDot11RxAssocBadWpaIe": ligoAthDot11RxAssocBadWpaIe,
       "ligoAthDot11RxDeauth": ligoAthDot11RxDeauth,
       "ligoAthDot11RxDisassoc": ligoAthDot11RxDisassoc,
       "ligoAthDot11RxUnknownSubtype": ligoAthDot11RxUnknownSubtype,
       "ligoAthDot11RxNoBuffer": ligoAthDot11RxNoBuffer,
       "ligoAthDot11RxDecryptCrcError": ligoAthDot11RxDecryptCrcError,
       "ligoAthDot11RxMgmtInAhdocDemo": ligoAthDot11RxMgmtInAhdocDemo,
       "ligoAthDot11RxBadAuthRequest": ligoAthDot11RxBadAuthRequest,
       "ligoAthDot11RxPortUnauth": ligoAthDot11RxPortUnauth,
       "ligoAthDot11RxBadKeyId": ligoAthDot11RxBadKeyId,
       "ligoAthDot11RxCcmpBadSeqNum": ligoAthDot11RxCcmpBadSeqNum,
       "ligoAthDot11RxCcmpBadFormat": ligoAthDot11RxCcmpBadFormat,
       "ligoAthDot11RxCcmpMicCheck": ligoAthDot11RxCcmpMicCheck,
       "ligoAthDot11RxTkipBadSeqNum": ligoAthDot11RxTkipBadSeqNum,
       "ligoAthDot11RxTkipBadFormat": ligoAthDot11RxTkipBadFormat,
       "ligoAthDot11RxTkipMicCheck": ligoAthDot11RxTkipMicCheck,
       "ligoAthDot11RxTkipIcvCheck": ligoAthDot11RxTkipIcvCheck,
       "ligoAthDot11RxBadCipherKeyType": ligoAthDot11RxBadCipherKeyType,
       "ligoAthDot11RxCipherKeyNotSet": ligoAthDot11RxCipherKeyNotSet,
       "ligoAthDot11RxAclPolicy": ligoAthDot11RxAclPolicy,
       "ligoAthDot11RxFastFrames": ligoAthDot11RxFastFrames,
       "ligoAthDot11RxFfBadTunnelHdr": ligoAthDot11RxFfBadTunnelHdr,
       "ligoAthDot11TxNoBuffer": ligoAthDot11TxNoBuffer,
       "ligoAthDot11TxNoNode": ligoAthDot11TxNoNode,
       "ligoAthDot11TxBadMgtFrames": ligoAthDot11TxBadMgtFrames,
       "ligoAthDot11TxBadCipherKeyType": ligoAthDot11TxBadCipherKeyType,
       "ligoAthDot11TxNoDefKey": ligoAthDot11TxNoDefKey,
       "ligoAthDot11TxNoCryptoHeadroom": ligoAthDot11TxNoCryptoHeadroom,
       "ligoAthDot11TxGoodFastFrames": ligoAthDot11TxGoodFastFrames,
       "ligoAthDot11TxBadFastFrames": ligoAthDot11TxBadFastFrames,
       "ligoAthDot11ActiveScans": ligoAthDot11ActiveScans,
       "ligoAthDot11PassiveScans": ligoAthDot11PassiveScans,
       "ligoAthDot11NodesTimeout": ligoAthDot11NodesTimeout,
       "ligoAthDot11CryptoCipherMalloc": ligoAthDot11CryptoCipherMalloc,
       "ligoAthDot11CryptoSwTkip": ligoAthDot11CryptoSwTkip,
       "ligoAthDot11CryptoTkipSwMicEnc": ligoAthDot11CryptoTkipSwMicEnc,
       "ligoAthDot11CryptoTkipSwMicDec": ligoAthDot11CryptoTkipSwMicDec,
       "ligoAthDot11CryptoTkipCtrm": ligoAthDot11CryptoTkipCtrm,
       "ligoAthDot11CryptoSwCcmp": ligoAthDot11CryptoSwCcmp,
       "ligoAthDot11CryptoSwWep": ligoAthDot11CryptoSwWep,
       "ligoAthDot11CryptoCipherRej": ligoAthDot11CryptoCipherRej,
       "ligoAthDot11CryptoNoKey": ligoAthDot11CryptoNoKey,
       "ligoAthDot11CryptoDelKey": ligoAthDot11CryptoDelKey,
       "ligoAthDot11CryptoBadCipher": ligoAthDot11CryptoBadCipher,
       "ligoAthDot11CryptoNoCipher": ligoAthDot11CryptoNoCipher,
       "ligoAthDot11CryptoAttachFail": ligoAthDot11CryptoAttachFail,
       "ligoAthDot11CryptoSwFallback": ligoAthDot11CryptoSwFallback,
       "ligoAthDot11CryptoKeyFail": ligoAthDot11CryptoKeyFail,
       "ligoAthDot11SnoopMcastPass": ligoAthDot11SnoopMcastPass,
       "ligoAthDot11SnoopMcastDrop": ligoAthDot11SnoopMcastDrop,
       "ligoAthPeerStatsTable": ligoAthPeerStatsTable,
       "ligoAthPeerStatsEntry": ligoAthPeerStatsEntry,
       "ligoAthPeerIndex": ligoAthPeerIndex,
       "ligoAthPeerMacAddr": ligoAthPeerMacAddr,
       "ligoAthPeerRxData": ligoAthPeerRxData,
       "ligoAthPeerRxMgmt": ligoAthPeerRxMgmt,
       "ligoAthPeerRxCtrl": ligoAthPeerRxCtrl,
       "ligoAthPeerRxBeacons": ligoAthPeerRxBeacons,
       "ligoAthPeerRxProbeResponse": ligoAthPeerRxProbeResponse,
       "ligoAthPeerRxUcast": ligoAthPeerRxUcast,
       "ligoAthPeerRxMcast": ligoAthPeerRxMcast,
       "ligoAthPeerRxBytes": ligoAthPeerRxBytes,
       "ligoAthPeerRxDup": ligoAthPeerRxDup,
       "ligoAthPeerRxNoPrivacy": ligoAthPeerRxNoPrivacy,
       "ligoAthPeerRxWepFail": ligoAthPeerRxWepFail,
       "ligoAthPeerRxDemicFail": ligoAthPeerRxDemicFail,
       "ligoAthPeerRxDecapFail": ligoAthPeerRxDecapFail,
       "ligoAthPeerRxDefragFail": ligoAthPeerRxDefragFail,
       "ligoAthPeerRxDissasoc": ligoAthPeerRxDissasoc,
       "ligoAthPeerRxDeauth": ligoAthPeerRxDeauth,
       "ligoAthPeerRxDecryptCrc": ligoAthPeerRxDecryptCrc,
       "ligoAthPeerRxUnauth": ligoAthPeerRxUnauth,
       "ligoAthPeerRxUnencrypted": ligoAthPeerRxUnencrypted,
       "ligoAthPeerTxData": ligoAthPeerTxData,
       "ligoAthPeerTxMgmt": ligoAthPeerTxMgmt,
       "ligoAthPeerTxProbeReq": ligoAthPeerTxProbeReq,
       "ligoAthPeerTxUcast": ligoAthPeerTxUcast,
       "ligoAthPeerTxMcast": ligoAthPeerTxMcast,
       "ligoAthPeerTxBytes": ligoAthPeerTxBytes,
       "ligoAthPeerTxNoVlanTag": ligoAthPeerTxNoVlanTag,
       "ligoAthPeerTxVlanMismatch": ligoAthPeerTxVlanMismatch,
       "ligoAthPeerTxUapsd": ligoAthPeerTxUapsd,
       "ligoAthPeerUapsdTriggers": ligoAthPeerUapsdTriggers,
       "ligoAthPeerTxEospLost": ligoAthPeerTxEospLost,
       "ligoAthPeerTxAssoc": ligoAthPeerTxAssoc,
       "ligoAthPeerTxAssocFail": ligoAthPeerTxAssocFail,
       "ligoAthPeerTxAuth": ligoAthPeerTxAuth,
       "ligoAthPeerTxAuthFail": ligoAthPeerTxAuthFail,
       "ligoAthPeerTxDeauth": ligoAthPeerTxDeauth,
       "ligoAthPeerTxDeauthCode": ligoAthPeerTxDeauthCode,
       "ligoAthPeerTxDisassoc": ligoAthPeerTxDisassoc,
       "ligoAthPeerTxDisassocCode": ligoAthPeerTxDisassocCode,
       "ligoAthPeerPsqDrops": ligoAthPeerPsqDrops,
       "ligoAthPeerMcastSnoop": ligoAthPeerMcastSnoop}
)
