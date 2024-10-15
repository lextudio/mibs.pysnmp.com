# SNMP MIB module (APPIAN-LPORT-HDLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-LPORT-HDLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:35 2024
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

(AcNodeId,
 AcSlotNumber,
 acLport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcNodeId",
    "AcSlotNumber",
    "acLport")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acLogicalHdlc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4)
)
acLogicalHdlc.setRevisions(
        ("1900-02-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcLogicalHdlcTable_Object = MibTable
acLogicalHdlcTable = _AcLogicalHdlcTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    acLogicalHdlcTable.setStatus("current")
_AcLogicalHdlcEntry_Object = MibTableRow
acLogicalHdlcEntry = _AcLogicalHdlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1)
)
acLogicalHdlcEntry.setIndexNames(
    (0, "APPIAN-LPORT-HDLC-MIB", "acLogicalHdlcNodeId"),
    (0, "APPIAN-LPORT-HDLC-MIB", "acLogicalHdlcSlot"),
    (0, "APPIAN-LPORT-HDLC-MIB", "acLogicalHdlcType"),
    (0, "APPIAN-LPORT-HDLC-MIB", "acLogicalHdlcIndex"),
)
if mibBuilder.loadTexts:
    acLogicalHdlcEntry.setStatus("current")
_AcLogicalHdlcNodeId_Type = AcNodeId
_AcLogicalHdlcNodeId_Object = MibTableColumn
acLogicalHdlcNodeId = _AcLogicalHdlcNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 1),
    _AcLogicalHdlcNodeId_Type()
)
acLogicalHdlcNodeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalHdlcNodeId.setStatus("current")
_AcLogicalHdlcSlot_Type = AcSlotNumber
_AcLogicalHdlcSlot_Object = MibTableColumn
acLogicalHdlcSlot = _AcLogicalHdlcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 2),
    _AcLogicalHdlcSlot_Type()
)
acLogicalHdlcSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalHdlcSlot.setStatus("current")


class _AcLogicalHdlcType_Type(Integer32):
    """Custom type acLogicalHdlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcc", 3),
          ("ds1", 1),
          ("ds3", 2))
    )


_AcLogicalHdlcType_Type.__name__ = "Integer32"
_AcLogicalHdlcType_Object = MibTableColumn
acLogicalHdlcType = _AcLogicalHdlcType_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 3),
    _AcLogicalHdlcType_Type()
)
acLogicalHdlcType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalHdlcType.setStatus("current")
_AcLogicalHdlcIndex_Type = Integer32
_AcLogicalHdlcIndex_Object = MibTableColumn
acLogicalHdlcIndex = _AcLogicalHdlcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 4),
    _AcLogicalHdlcIndex_Type()
)
acLogicalHdlcIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    acLogicalHdlcIndex.setStatus("current")
_AcLogicalHdlcStatsReset_Type = TruthValue
_AcLogicalHdlcStatsReset_Object = MibTableColumn
acLogicalHdlcStatsReset = _AcLogicalHdlcStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 5),
    _AcLogicalHdlcStatsReset_Type()
)
acLogicalHdlcStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acLogicalHdlcStatsReset.setStatus("current")
_AcLogicalHdlcRxFifoOverrun_Type = Counter64
_AcLogicalHdlcRxFifoOverrun_Object = MibTableColumn
acLogicalHdlcRxFifoOverrun = _AcLogicalHdlcRxFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 6),
    _AcLogicalHdlcRxFifoOverrun_Type()
)
acLogicalHdlcRxFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxFifoOverrun.setStatus("current")
_AcLogicalHdlcRxMaxPktLenViolation_Type = Counter64
_AcLogicalHdlcRxMaxPktLenViolation_Object = MibTableColumn
acLogicalHdlcRxMaxPktLenViolation = _AcLogicalHdlcRxMaxPktLenViolation_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 7),
    _AcLogicalHdlcRxMaxPktLenViolation_Type()
)
acLogicalHdlcRxMaxPktLenViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxMaxPktLenViolation.setStatus("current")
_AcLogicalHdlcRxFCSError_Type = Counter64
_AcLogicalHdlcRxFCSError_Object = MibTableColumn
acLogicalHdlcRxFCSError = _AcLogicalHdlcRxFCSError_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 8),
    _AcLogicalHdlcRxFCSError_Type()
)
acLogicalHdlcRxFCSError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxFCSError.setStatus("current")
_AcLogicalHdlcRxNonOctetAligned_Type = Counter64
_AcLogicalHdlcRxNonOctetAligned_Object = MibTableColumn
acLogicalHdlcRxNonOctetAligned = _AcLogicalHdlcRxNonOctetAligned_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 9),
    _AcLogicalHdlcRxNonOctetAligned_Type()
)
acLogicalHdlcRxNonOctetAligned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxNonOctetAligned.setStatus("current")
_AcLogicalHdlcRxHdlcPktAbort_Type = Counter64
_AcLogicalHdlcRxHdlcPktAbort_Object = MibTableColumn
acLogicalHdlcRxHdlcPktAbort = _AcLogicalHdlcRxHdlcPktAbort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 10),
    _AcLogicalHdlcRxHdlcPktAbort_Type()
)
acLogicalHdlcRxHdlcPktAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxHdlcPktAbort.setStatus("current")
_AcLogicalHdlcRxBufferStarvation_Type = Counter64
_AcLogicalHdlcRxBufferStarvation_Object = MibTableColumn
acLogicalHdlcRxBufferStarvation = _AcLogicalHdlcRxBufferStarvation_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 11),
    _AcLogicalHdlcRxBufferStarvation_Type()
)
acLogicalHdlcRxBufferStarvation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxBufferStarvation.setStatus("current")
_AcLogicalHdlcTxFifoUnderrun_Type = Counter64
_AcLogicalHdlcTxFifoUnderrun_Object = MibTableColumn
acLogicalHdlcTxFifoUnderrun = _AcLogicalHdlcTxFifoUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 12),
    _AcLogicalHdlcTxFifoUnderrun_Type()
)
acLogicalHdlcTxFifoUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcTxFifoUnderrun.setStatus("current")
_AcLogicalHdlcRxBundleDiscardDupSeq_Type = Counter64
_AcLogicalHdlcRxBundleDiscardDupSeq_Object = MibTableColumn
acLogicalHdlcRxBundleDiscardDupSeq = _AcLogicalHdlcRxBundleDiscardDupSeq_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 13),
    _AcLogicalHdlcRxBundleDiscardDupSeq_Type()
)
acLogicalHdlcRxBundleDiscardDupSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxBundleDiscardDupSeq.setStatus("current")
_AcLogicalHdlcRxBundleDiscardMissSeq_Type = Counter64
_AcLogicalHdlcRxBundleDiscardMissSeq_Object = MibTableColumn
acLogicalHdlcRxBundleDiscardMissSeq = _AcLogicalHdlcRxBundleDiscardMissSeq_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 14),
    _AcLogicalHdlcRxBundleDiscardMissSeq_Type()
)
acLogicalHdlcRxBundleDiscardMissSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxBundleDiscardMissSeq.setStatus("current")
_AcLogicalHdlcRxBundleDiscardQDepth_Type = Counter64
_AcLogicalHdlcRxBundleDiscardQDepth_Object = MibTableColumn
acLogicalHdlcRxBundleDiscardQDepth = _AcLogicalHdlcRxBundleDiscardQDepth_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 15),
    _AcLogicalHdlcRxBundleDiscardQDepth_Type()
)
acLogicalHdlcRxBundleDiscardQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcRxBundleDiscardQDepth.setStatus("current")
_AcLogicalHdlcIngressRxFrames_Type = Counter64
_AcLogicalHdlcIngressRxFrames_Object = MibTableColumn
acLogicalHdlcIngressRxFrames = _AcLogicalHdlcIngressRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 16),
    _AcLogicalHdlcIngressRxFrames_Type()
)
acLogicalHdlcIngressRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcIngressRxFrames.setStatus("current")
_AcLogicalHdlcEgressTxFrames_Type = Counter64
_AcLogicalHdlcEgressTxFrames_Object = MibTableColumn
acLogicalHdlcEgressTxFrames = _AcLogicalHdlcEgressTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 4, 4, 1, 1, 17),
    _AcLogicalHdlcEgressTxFrames_Type()
)
acLogicalHdlcEgressTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acLogicalHdlcEgressTxFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-LPORT-HDLC-MIB",
    **{"acLogicalHdlc": acLogicalHdlc,
       "acLogicalHdlcTable": acLogicalHdlcTable,
       "acLogicalHdlcEntry": acLogicalHdlcEntry,
       "acLogicalHdlcNodeId": acLogicalHdlcNodeId,
       "acLogicalHdlcSlot": acLogicalHdlcSlot,
       "acLogicalHdlcType": acLogicalHdlcType,
       "acLogicalHdlcIndex": acLogicalHdlcIndex,
       "acLogicalHdlcStatsReset": acLogicalHdlcStatsReset,
       "acLogicalHdlcRxFifoOverrun": acLogicalHdlcRxFifoOverrun,
       "acLogicalHdlcRxMaxPktLenViolation": acLogicalHdlcRxMaxPktLenViolation,
       "acLogicalHdlcRxFCSError": acLogicalHdlcRxFCSError,
       "acLogicalHdlcRxNonOctetAligned": acLogicalHdlcRxNonOctetAligned,
       "acLogicalHdlcRxHdlcPktAbort": acLogicalHdlcRxHdlcPktAbort,
       "acLogicalHdlcRxBufferStarvation": acLogicalHdlcRxBufferStarvation,
       "acLogicalHdlcTxFifoUnderrun": acLogicalHdlcTxFifoUnderrun,
       "acLogicalHdlcRxBundleDiscardDupSeq": acLogicalHdlcRxBundleDiscardDupSeq,
       "acLogicalHdlcRxBundleDiscardMissSeq": acLogicalHdlcRxBundleDiscardMissSeq,
       "acLogicalHdlcRxBundleDiscardQDepth": acLogicalHdlcRxBundleDiscardQDepth,
       "acLogicalHdlcIngressRxFrames": acLogicalHdlcIngressRxFrames,
       "acLogicalHdlcEgressTxFrames": acLogicalHdlcEgressTxFrames}
)
