# SNMP MIB module (APTIS-FRAME-RELAY-DTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APTIS-FRAME-RELAY-DTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:05 2024
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

(aptis_generic,) = mibBuilder.importSymbols(
    "APTIS-MIB",
    "aptis-generic")

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



class Index(Integer32):
    """Custom type Index based on Integer32"""




class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AptisFrameRelay_ObjectIdentity = ObjectIdentity
aptisFrameRelay = _AptisFrameRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6)
)
_AptisDlcmiTable_Object = MibTable
aptisDlcmiTable = _AptisDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1)
)
if mibBuilder.loadTexts:
    aptisDlcmiTable.setStatus("mandatory")
_AptisDlcmiEntry_Object = MibTableRow
aptisDlcmiEntry = _AptisDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1)
)
aptisDlcmiEntry.setIndexNames(
    (0, "APTIS-FRAME-RELAY-DTE-MIB", "aptisDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    aptisDlcmiEntry.setStatus("mandatory")
_AptisDlcmiIfIndex_Type = Index
_AptisDlcmiIfIndex_Object = MibTableColumn
aptisDlcmiIfIndex = _AptisDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 1),
    _AptisDlcmiIfIndex_Type()
)
aptisDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiIfIndex.setStatus("mandatory")
_AptisDlcmiXmtFramesDropped_Type = Counter32
_AptisDlcmiXmtFramesDropped_Object = MibTableColumn
aptisDlcmiXmtFramesDropped = _AptisDlcmiXmtFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 2),
    _AptisDlcmiXmtFramesDropped_Type()
)
aptisDlcmiXmtFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiXmtFramesDropped.setStatus("mandatory")
_AptisDlcmiXmtOctetsDropped_Type = Counter32
_AptisDlcmiXmtOctetsDropped_Object = MibTableColumn
aptisDlcmiXmtOctetsDropped = _AptisDlcmiXmtOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 3),
    _AptisDlcmiXmtOctetsDropped_Type()
)
aptisDlcmiXmtOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiXmtOctetsDropped.setStatus("mandatory")
_AptisDlcmiRcvFramesDropped_Type = Counter32
_AptisDlcmiRcvFramesDropped_Object = MibTableColumn
aptisDlcmiRcvFramesDropped = _AptisDlcmiRcvFramesDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 4),
    _AptisDlcmiRcvFramesDropped_Type()
)
aptisDlcmiRcvFramesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvFramesDropped.setStatus("mandatory")
_AptisDlcmiRcvOctetsDropped_Type = Counter32
_AptisDlcmiRcvOctetsDropped_Object = MibTableColumn
aptisDlcmiRcvOctetsDropped = _AptisDlcmiRcvOctetsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 5),
    _AptisDlcmiRcvOctetsDropped_Type()
)
aptisDlcmiRcvOctetsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvOctetsDropped.setStatus("mandatory")
_AptisDlcmiRcvInvFrames_Type = Counter32
_AptisDlcmiRcvInvFrames_Object = MibTableColumn
aptisDlcmiRcvInvFrames = _AptisDlcmiRcvInvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 6),
    _AptisDlcmiRcvInvFrames_Type()
)
aptisDlcmiRcvInvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvInvFrames.setStatus("mandatory")
_AptisDlcmiRcvShortFrames_Type = Counter32
_AptisDlcmiRcvShortFrames_Object = MibTableColumn
aptisDlcmiRcvShortFrames = _AptisDlcmiRcvShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 7),
    _AptisDlcmiRcvShortFrames_Type()
)
aptisDlcmiRcvShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvShortFrames.setStatus("mandatory")
_AptisDlcmiRcvLongFrames_Type = Counter32
_AptisDlcmiRcvLongFrames_Object = MibTableColumn
aptisDlcmiRcvLongFrames = _AptisDlcmiRcvLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 8),
    _AptisDlcmiRcvLongFrames_Type()
)
aptisDlcmiRcvLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvLongFrames.setStatus("mandatory")
_AptisDlcmiRcvInvalidDLCI_Type = Counter32
_AptisDlcmiRcvInvalidDLCI_Object = MibTableColumn
aptisDlcmiRcvInvalidDLCI = _AptisDlcmiRcvInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 9),
    _AptisDlcmiRcvInvalidDLCI_Type()
)
aptisDlcmiRcvInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvInvalidDLCI.setStatus("mandatory")
_AptisDlcmiRcvUnknownDLCI_Type = Counter32
_AptisDlcmiRcvUnknownDLCI_Object = MibTableColumn
aptisDlcmiRcvUnknownDLCI = _AptisDlcmiRcvUnknownDLCI_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 10),
    _AptisDlcmiRcvUnknownDLCI_Type()
)
aptisDlcmiRcvUnknownDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvUnknownDLCI.setStatus("mandatory")
_AptisDlcmiRcvUnknownErrs_Type = Counter32
_AptisDlcmiRcvUnknownErrs_Object = MibTableColumn
aptisDlcmiRcvUnknownErrs = _AptisDlcmiRcvUnknownErrs_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 11),
    _AptisDlcmiRcvUnknownErrs_Type()
)
aptisDlcmiRcvUnknownErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiRcvUnknownErrs.setStatus("mandatory")
_AptisDlcmiLMIStatusEnquiries_Type = Counter32
_AptisDlcmiLMIStatusEnquiries_Object = MibTableColumn
aptisDlcmiLMIStatusEnquiries = _AptisDlcmiLMIStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 12),
    _AptisDlcmiLMIStatusEnquiries_Type()
)
aptisDlcmiLMIStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLMIStatusEnquiries.setStatus("mandatory")
_AptisDlcmiLMIFullStatusEnquiries_Type = Counter32
_AptisDlcmiLMIFullStatusEnquiries_Object = MibTableColumn
aptisDlcmiLMIFullStatusEnquiries = _AptisDlcmiLMIFullStatusEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 13),
    _AptisDlcmiLMIFullStatusEnquiries_Type()
)
aptisDlcmiLMIFullStatusEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLMIFullStatusEnquiries.setStatus("mandatory")
_AptisDlcmiLMIStatusResponses_Type = Counter32
_AptisDlcmiLMIStatusResponses_Object = MibTableColumn
aptisDlcmiLMIStatusResponses = _AptisDlcmiLMIStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 14),
    _AptisDlcmiLMIStatusResponses_Type()
)
aptisDlcmiLMIStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLMIStatusResponses.setStatus("mandatory")
_AptisDlcmiLMIFullStatusResponses_Type = Counter32
_AptisDlcmiLMIFullStatusResponses_Object = MibTableColumn
aptisDlcmiLMIFullStatusResponses = _AptisDlcmiLMIFullStatusResponses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 15),
    _AptisDlcmiLMIFullStatusResponses_Type()
)
aptisDlcmiLMIFullStatusResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLMIFullStatusResponses.setStatus("mandatory")
_AptisDlcmiLMIUpdates_Type = Counter32
_AptisDlcmiLMIUpdates_Object = MibTableColumn
aptisDlcmiLMIUpdates = _AptisDlcmiLMIUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 16),
    _AptisDlcmiLMIUpdates_Type()
)
aptisDlcmiLMIUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLMIUpdates.setStatus("mandatory")
_AptisDlcmiUnknownLMIMessagesRcvd_Type = Counter32
_AptisDlcmiUnknownLMIMessagesRcvd_Object = MibTableColumn
aptisDlcmiUnknownLMIMessagesRcvd = _AptisDlcmiUnknownLMIMessagesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 17),
    _AptisDlcmiUnknownLMIMessagesRcvd_Type()
)
aptisDlcmiUnknownLMIMessagesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiUnknownLMIMessagesRcvd.setStatus("mandatory")
_AptisDlcmiBadLMIMessagesRcvd_Type = Counter32
_AptisDlcmiBadLMIMessagesRcvd_Object = MibTableColumn
aptisDlcmiBadLMIMessagesRcvd = _AptisDlcmiBadLMIMessagesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 18),
    _AptisDlcmiBadLMIMessagesRcvd_Type()
)
aptisDlcmiBadLMIMessagesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiBadLMIMessagesRcvd.setStatus("mandatory")
_AptisDlcmiLostLMISequences_Type = Counter32
_AptisDlcmiLostLMISequences_Object = MibTableColumn
aptisDlcmiLostLMISequences = _AptisDlcmiLostLMISequences_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 19),
    _AptisDlcmiLostLMISequences_Type()
)
aptisDlcmiLostLMISequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiLostLMISequences.setStatus("mandatory")
_AptisDlcmiMissingLMIResponses_Type = Counter32
_AptisDlcmiMissingLMIResponses_Object = MibTableColumn
aptisDlcmiMissingLMIResponses = _AptisDlcmiMissingLMIResponses_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 20),
    _AptisDlcmiMissingLMIResponses_Type()
)
aptisDlcmiMissingLMIResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiMissingLMIResponses.setStatus("mandatory")
_AptisDlcmiUpTime_Type = TimeTicks
_AptisDlcmiUpTime_Object = MibTableColumn
aptisDlcmiUpTime = _AptisDlcmiUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 1, 1, 21),
    _AptisDlcmiUpTime_Type()
)
aptisDlcmiUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisDlcmiUpTime.setStatus("mandatory")
_AptisCircuitTable_Object = MibTable
aptisCircuitTable = _AptisCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2)
)
if mibBuilder.loadTexts:
    aptisCircuitTable.setStatus("mandatory")
_AptisCircuitEntry_Object = MibTableRow
aptisCircuitEntry = _AptisCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1)
)
aptisCircuitEntry.setIndexNames(
    (0, "APTIS-FRAME-RELAY-DTE-MIB", "aptisCircuitIfIndex"),
    (0, "APTIS-FRAME-RELAY-DTE-MIB", "aptisCircuitDlci"),
)
if mibBuilder.loadTexts:
    aptisCircuitEntry.setStatus("mandatory")
_AptisCircuitIfIndex_Type = Index
_AptisCircuitIfIndex_Object = MibTableColumn
aptisCircuitIfIndex = _AptisCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 1),
    _AptisCircuitIfIndex_Type()
)
aptisCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitIfIndex.setStatus("mandatory")
_AptisCircuitDlci_Type = DLCI
_AptisCircuitDlci_Object = MibTableColumn
aptisCircuitDlci = _AptisCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 2),
    _AptisCircuitDlci_Type()
)
aptisCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitDlci.setStatus("mandatory")
_AptisCircuitReceivedRBits_Type = Counter32
_AptisCircuitReceivedRBits_Object = MibTableColumn
aptisCircuitReceivedRBits = _AptisCircuitReceivedRBits_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 3),
    _AptisCircuitReceivedRBits_Type()
)
aptisCircuitReceivedRBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitReceivedRBits.setStatus("mandatory")
_AptisCircuitRateFallbacks_Type = Counter32
_AptisCircuitRateFallbacks_Object = MibTableColumn
aptisCircuitRateFallbacks = _AptisCircuitRateFallbacks_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 4),
    _AptisCircuitRateFallbacks_Type()
)
aptisCircuitRateFallbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitRateFallbacks.setStatus("mandatory")
_AptisCircuitRateFallforwards_Type = Counter32
_AptisCircuitRateFallforwards_Object = MibTableColumn
aptisCircuitRateFallforwards = _AptisCircuitRateFallforwards_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 5),
    _AptisCircuitRateFallforwards_Type()
)
aptisCircuitRateFallforwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitRateFallforwards.setStatus("mandatory")
_AptisCircuitFramesDroppedQueueFull_Type = Counter32
_AptisCircuitFramesDroppedQueueFull_Object = MibTableColumn
aptisCircuitFramesDroppedQueueFull = _AptisCircuitFramesDroppedQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 6),
    _AptisCircuitFramesDroppedQueueFull_Type()
)
aptisCircuitFramesDroppedQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitFramesDroppedQueueFull.setStatus("mandatory")
_AptisCircuitNormalSentOctets_Type = Counter32
_AptisCircuitNormalSentOctets_Object = MibTableColumn
aptisCircuitNormalSentOctets = _AptisCircuitNormalSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 7),
    _AptisCircuitNormalSentOctets_Type()
)
aptisCircuitNormalSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitNormalSentOctets.setStatus("mandatory")
_AptisCircuitExcessSentOctets_Type = Counter32
_AptisCircuitExcessSentOctets_Object = MibTableColumn
aptisCircuitExcessSentOctets = _AptisCircuitExcessSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 8),
    _AptisCircuitExcessSentOctets_Type()
)
aptisCircuitExcessSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitExcessSentOctets.setStatus("mandatory")
_AptisCircuitFramesQueuedBandwidth_Type = Counter32
_AptisCircuitFramesQueuedBandwidth_Object = MibTableColumn
aptisCircuitFramesQueuedBandwidth = _AptisCircuitFramesQueuedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 9),
    _AptisCircuitFramesQueuedBandwidth_Type()
)
aptisCircuitFramesQueuedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitFramesQueuedBandwidth.setStatus("mandatory")
_AptisCircuitOctetsQueuedBandwidth_Type = Counter32
_AptisCircuitOctetsQueuedBandwidth_Object = MibTableColumn
aptisCircuitOctetsQueuedBandwidth = _AptisCircuitOctetsQueuedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 10),
    _AptisCircuitOctetsQueuedBandwidth_Type()
)
aptisCircuitOctetsQueuedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitOctetsQueuedBandwidth.setStatus("mandatory")
_AptisCircuitFramesOnQueue_Type = Integer32
_AptisCircuitFramesOnQueue_Object = MibTableColumn
aptisCircuitFramesOnQueue = _AptisCircuitFramesOnQueue_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 11),
    _AptisCircuitFramesOnQueue_Type()
)
aptisCircuitFramesOnQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitFramesOnQueue.setStatus("mandatory")
_AptisCircuitReceivedUnknownProtocol_Type = Counter32
_AptisCircuitReceivedUnknownProtocol_Object = MibTableColumn
aptisCircuitReceivedUnknownProtocol = _AptisCircuitReceivedUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 12),
    _AptisCircuitReceivedUnknownProtocol_Type()
)
aptisCircuitReceivedUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitReceivedUnknownProtocol.setStatus("mandatory")
_AptisCircuitSentUnknownProtocol_Type = Counter32
_AptisCircuitSentUnknownProtocol_Object = MibTableColumn
aptisCircuitSentUnknownProtocol = _AptisCircuitSentUnknownProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 13),
    _AptisCircuitSentUnknownProtocol_Type()
)
aptisCircuitSentUnknownProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitSentUnknownProtocol.setStatus("mandatory")
_AptisCircuitReceivedUnknownFrame_Type = Counter32
_AptisCircuitReceivedUnknownFrame_Object = MibTableColumn
aptisCircuitReceivedUnknownFrame = _AptisCircuitReceivedUnknownFrame_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 14),
    _AptisCircuitReceivedUnknownFrame_Type()
)
aptisCircuitReceivedUnknownFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitReceivedUnknownFrame.setStatus("mandatory")
_AptisCircuitReceivedUnknownOrg_Type = Counter32
_AptisCircuitReceivedUnknownOrg_Object = MibTableColumn
aptisCircuitReceivedUnknownOrg = _AptisCircuitReceivedUnknownOrg_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 15),
    _AptisCircuitReceivedUnknownOrg_Type()
)
aptisCircuitReceivedUnknownOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitReceivedUnknownOrg.setStatus("mandatory")
_AptisCircuitNormalSentFrames_Type = Counter32
_AptisCircuitNormalSentFrames_Object = MibTableColumn
aptisCircuitNormalSentFrames = _AptisCircuitNormalSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 16),
    _AptisCircuitNormalSentFrames_Type()
)
aptisCircuitNormalSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitNormalSentFrames.setStatus("mandatory")
_AptisCircuitExcessSentFrames_Type = Counter32
_AptisCircuitExcessSentFrames_Object = MibTableColumn
aptisCircuitExcessSentFrames = _AptisCircuitExcessSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 17),
    _AptisCircuitExcessSentFrames_Type()
)
aptisCircuitExcessSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitExcessSentFrames.setStatus("mandatory")
_AptisCircuitOctetsDroppedQueueFull_Type = Counter32
_AptisCircuitOctetsDroppedQueueFull_Object = MibTableColumn
aptisCircuitOctetsDroppedQueueFull = _AptisCircuitOctetsDroppedQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 2637, 2, 6, 2, 1, 18),
    _AptisCircuitOctetsDroppedQueueFull_Type()
)
aptisCircuitOctetsDroppedQueueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aptisCircuitOctetsDroppedQueueFull.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APTIS-FRAME-RELAY-DTE-MIB",
    **{"Index": Index,
       "DLCI": DLCI,
       "aptisFrameRelay": aptisFrameRelay,
       "aptisDlcmiTable": aptisDlcmiTable,
       "aptisDlcmiEntry": aptisDlcmiEntry,
       "aptisDlcmiIfIndex": aptisDlcmiIfIndex,
       "aptisDlcmiXmtFramesDropped": aptisDlcmiXmtFramesDropped,
       "aptisDlcmiXmtOctetsDropped": aptisDlcmiXmtOctetsDropped,
       "aptisDlcmiRcvFramesDropped": aptisDlcmiRcvFramesDropped,
       "aptisDlcmiRcvOctetsDropped": aptisDlcmiRcvOctetsDropped,
       "aptisDlcmiRcvInvFrames": aptisDlcmiRcvInvFrames,
       "aptisDlcmiRcvShortFrames": aptisDlcmiRcvShortFrames,
       "aptisDlcmiRcvLongFrames": aptisDlcmiRcvLongFrames,
       "aptisDlcmiRcvInvalidDLCI": aptisDlcmiRcvInvalidDLCI,
       "aptisDlcmiRcvUnknownDLCI": aptisDlcmiRcvUnknownDLCI,
       "aptisDlcmiRcvUnknownErrs": aptisDlcmiRcvUnknownErrs,
       "aptisDlcmiLMIStatusEnquiries": aptisDlcmiLMIStatusEnquiries,
       "aptisDlcmiLMIFullStatusEnquiries": aptisDlcmiLMIFullStatusEnquiries,
       "aptisDlcmiLMIStatusResponses": aptisDlcmiLMIStatusResponses,
       "aptisDlcmiLMIFullStatusResponses": aptisDlcmiLMIFullStatusResponses,
       "aptisDlcmiLMIUpdates": aptisDlcmiLMIUpdates,
       "aptisDlcmiUnknownLMIMessagesRcvd": aptisDlcmiUnknownLMIMessagesRcvd,
       "aptisDlcmiBadLMIMessagesRcvd": aptisDlcmiBadLMIMessagesRcvd,
       "aptisDlcmiLostLMISequences": aptisDlcmiLostLMISequences,
       "aptisDlcmiMissingLMIResponses": aptisDlcmiMissingLMIResponses,
       "aptisDlcmiUpTime": aptisDlcmiUpTime,
       "aptisCircuitTable": aptisCircuitTable,
       "aptisCircuitEntry": aptisCircuitEntry,
       "aptisCircuitIfIndex": aptisCircuitIfIndex,
       "aptisCircuitDlci": aptisCircuitDlci,
       "aptisCircuitReceivedRBits": aptisCircuitReceivedRBits,
       "aptisCircuitRateFallbacks": aptisCircuitRateFallbacks,
       "aptisCircuitRateFallforwards": aptisCircuitRateFallforwards,
       "aptisCircuitFramesDroppedQueueFull": aptisCircuitFramesDroppedQueueFull,
       "aptisCircuitNormalSentOctets": aptisCircuitNormalSentOctets,
       "aptisCircuitExcessSentOctets": aptisCircuitExcessSentOctets,
       "aptisCircuitFramesQueuedBandwidth": aptisCircuitFramesQueuedBandwidth,
       "aptisCircuitOctetsQueuedBandwidth": aptisCircuitOctetsQueuedBandwidth,
       "aptisCircuitFramesOnQueue": aptisCircuitFramesOnQueue,
       "aptisCircuitReceivedUnknownProtocol": aptisCircuitReceivedUnknownProtocol,
       "aptisCircuitSentUnknownProtocol": aptisCircuitSentUnknownProtocol,
       "aptisCircuitReceivedUnknownFrame": aptisCircuitReceivedUnknownFrame,
       "aptisCircuitReceivedUnknownOrg": aptisCircuitReceivedUnknownOrg,
       "aptisCircuitNormalSentFrames": aptisCircuitNormalSentFrames,
       "aptisCircuitExcessSentFrames": aptisCircuitExcessSentFrames,
       "aptisCircuitOctetsDroppedQueueFull": aptisCircuitOctetsDroppedQueueFull}
)
