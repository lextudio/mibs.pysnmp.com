# SNMP MIB module (INTEL-FREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-FREXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:42 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(mib2ext,) = mibBuilder.importSymbols(
    "INTEL-GEN-MIB",
    "mib2ext")

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



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrEx_ObjectIdentity = ObjectIdentity
frEx = _FrEx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 28)
)
_FrCircuitExt_ObjectIdentity = ObjectIdentity
frCircuitExt = _FrCircuitExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1)
)
_FrCirExtEncTable_Object = MibTable
frCirExtEncTable = _FrCirExtEncTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1)
)
if mibBuilder.loadTexts:
    frCirExtEncTable.setStatus("mandatory")
_FrCirExtEncEntry_Object = MibTableRow
frCirExtEncEntry = _FrCirExtEncEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1)
)
frCirExtEncEntry.setIndexNames(
    (0, "INTEL-FREXT-MIB", "frCirExtEncIfIndex"),
    (0, "INTEL-FREXT-MIB", "frCirExtEncDlci"),
)
if mibBuilder.loadTexts:
    frCirExtEncEntry.setStatus("mandatory")
_FrCirExtEncIfIndex_Type = InterfaceIndex
_FrCirExtEncIfIndex_Object = MibTableColumn
frCirExtEncIfIndex = _FrCirExtEncIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 1),
    _FrCirExtEncIfIndex_Type()
)
frCirExtEncIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncIfIndex.setStatus("mandatory")
_FrCirExtEncDlci_Type = DLCI
_FrCirExtEncDlci_Object = MibTableColumn
frCirExtEncDlci = _FrCirExtEncDlci_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 2),
    _FrCirExtEncDlci_Type()
)
frCirExtEncDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncDlci.setStatus("mandatory")
_FrCirExtEncLogicalIfIndex_Type = InterfaceIndex
_FrCirExtEncLogicalIfIndex_Object = MibTableColumn
frCirExtEncLogicalIfIndex = _FrCirExtEncLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 3),
    _FrCirExtEncLogicalIfIndex_Type()
)
frCirExtEncLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncLogicalIfIndex.setStatus("mandatory")


class _FrCirExtEncEnabled_Type(Integer32):
    """Custom type frCirExtEncEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrCirExtEncEnabled_Type.__name__ = "Integer32"
_FrCirExtEncEnabled_Object = MibTableColumn
frCirExtEncEnabled = _FrCirExtEncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 4),
    _FrCirExtEncEnabled_Type()
)
frCirExtEncEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncEnabled.setStatus("mandatory")


class _FrCirExtEncNegotiated_Type(Integer32):
    """Custom type frCirExtEncNegotiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrCirExtEncNegotiated_Type.__name__ = "Integer32"
_FrCirExtEncNegotiated_Object = MibTableColumn
frCirExtEncNegotiated = _FrCirExtEncNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 5),
    _FrCirExtEncNegotiated_Type()
)
frCirExtEncNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncNegotiated.setStatus("mandatory")
_FrCirExtEncResetRequestsRx_Type = Counter32
_FrCirExtEncResetRequestsRx_Object = MibTableColumn
frCirExtEncResetRequestsRx = _FrCirExtEncResetRequestsRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 6),
    _FrCirExtEncResetRequestsRx_Type()
)
frCirExtEncResetRequestsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncResetRequestsRx.setStatus("mandatory")
_FrCirExtEncResetRequestsTx_Type = Counter32
_FrCirExtEncResetRequestsTx_Object = MibTableColumn
frCirExtEncResetRequestsTx = _FrCirExtEncResetRequestsTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 7),
    _FrCirExtEncResetRequestsTx_Type()
)
frCirExtEncResetRequestsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncResetRequestsTx.setStatus("mandatory")
_FrCirExtEncResetAcksRx_Type = Counter32
_FrCirExtEncResetAcksRx_Object = MibTableColumn
frCirExtEncResetAcksRx = _FrCirExtEncResetAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 8),
    _FrCirExtEncResetAcksRx_Type()
)
frCirExtEncResetAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncResetAcksRx.setStatus("mandatory")
_FrCirExtEncResetAcksTx_Type = Counter32
_FrCirExtEncResetAcksTx_Object = MibTableColumn
frCirExtEncResetAcksTx = _FrCirExtEncResetAcksTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 9),
    _FrCirExtEncResetAcksTx_Type()
)
frCirExtEncResetAcksTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncResetAcksTx.setStatus("mandatory")
_FrCirExtEncRxDiscarded_Type = Counter32
_FrCirExtEncRxDiscarded_Object = MibTableColumn
frCirExtEncRxDiscarded = _FrCirExtEncRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 10),
    _FrCirExtEncRxDiscarded_Type()
)
frCirExtEncRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncRxDiscarded.setStatus("mandatory")
_FrCirExtEncTxDiscarded_Type = Counter32
_FrCirExtEncTxDiscarded_Object = MibTableColumn
frCirExtEncTxDiscarded = _FrCirExtEncTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 11),
    _FrCirExtEncTxDiscarded_Type()
)
frCirExtEncTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncTxDiscarded.setStatus("mandatory")


class _FrCirExtEncReceiverState_Type(Integer32):
    """Custom type frCirExtEncReceiverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_FrCirExtEncReceiverState_Type.__name__ = "Integer32"
_FrCirExtEncReceiverState_Object = MibTableColumn
frCirExtEncReceiverState = _FrCirExtEncReceiverState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 1, 1, 12),
    _FrCirExtEncReceiverState_Type()
)
frCirExtEncReceiverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtEncReceiverState.setStatus("mandatory")
_FrCirExtCompTable_Object = MibTable
frCirExtCompTable = _FrCirExtCompTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2)
)
if mibBuilder.loadTexts:
    frCirExtCompTable.setStatus("mandatory")
_FrCirExtCompEntry_Object = MibTableRow
frCirExtCompEntry = _FrCirExtCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1)
)
frCirExtCompEntry.setIndexNames(
    (0, "INTEL-FREXT-MIB", "frCirExtCompIfIndex"),
    (0, "INTEL-FREXT-MIB", "frCirExtCompDlci"),
)
if mibBuilder.loadTexts:
    frCirExtCompEntry.setStatus("mandatory")
_FrCirExtCompIfIndex_Type = InterfaceIndex
_FrCirExtCompIfIndex_Object = MibTableColumn
frCirExtCompIfIndex = _FrCirExtCompIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 1),
    _FrCirExtCompIfIndex_Type()
)
frCirExtCompIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompIfIndex.setStatus("mandatory")
_FrCirExtCompDlci_Type = DLCI
_FrCirExtCompDlci_Object = MibTableColumn
frCirExtCompDlci = _FrCirExtCompDlci_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 2),
    _FrCirExtCompDlci_Type()
)
frCirExtCompDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDlci.setStatus("mandatory")
_FrCirExtCompLogicalIfIndex_Type = InterfaceIndex
_FrCirExtCompLogicalIfIndex_Object = MibTableColumn
frCirExtCompLogicalIfIndex = _FrCirExtCompLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 3),
    _FrCirExtCompLogicalIfIndex_Type()
)
frCirExtCompLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompLogicalIfIndex.setStatus("mandatory")


class _FrCirExtCompEnabled_Type(Integer32):
    """Custom type frCirExtCompEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrCirExtCompEnabled_Type.__name__ = "Integer32"
_FrCirExtCompEnabled_Object = MibTableColumn
frCirExtCompEnabled = _FrCirExtCompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 4),
    _FrCirExtCompEnabled_Type()
)
frCirExtCompEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEnabled.setStatus("mandatory")


class _FrCirExtCompNegotiated_Type(Integer32):
    """Custom type frCirExtCompNegotiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FrCirExtCompNegotiated_Type.__name__ = "Integer32"
_FrCirExtCompNegotiated_Object = MibTableColumn
frCirExtCompNegotiated = _FrCirExtCompNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 5),
    _FrCirExtCompNegotiated_Type()
)
frCirExtCompNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompNegotiated.setStatus("mandatory")
_FrCirExtCompDecoderBytesIn_Type = Counter32
_FrCirExtCompDecoderBytesIn_Object = MibTableColumn
frCirExtCompDecoderBytesIn = _FrCirExtCompDecoderBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 6),
    _FrCirExtCompDecoderBytesIn_Type()
)
frCirExtCompDecoderBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderBytesIn.setStatus("mandatory")
_FrCirExtCompDecoderDecompBytesOut_Type = Counter32
_FrCirExtCompDecoderDecompBytesOut_Object = MibTableColumn
frCirExtCompDecoderDecompBytesOut = _FrCirExtCompDecoderDecompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 7),
    _FrCirExtCompDecoderDecompBytesOut_Type()
)
frCirExtCompDecoderDecompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderDecompBytesOut.setStatus("mandatory")
_FrCirExtCompDecoderUncompBytesOut_Type = Counter32
_FrCirExtCompDecoderUncompBytesOut_Object = MibTableColumn
frCirExtCompDecoderUncompBytesOut = _FrCirExtCompDecoderUncompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 8),
    _FrCirExtCompDecoderUncompBytesOut_Type()
)
frCirExtCompDecoderUncompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderUncompBytesOut.setStatus("mandatory")
_FrCirExtCompDecoderCompPacketsIn_Type = Counter32
_FrCirExtCompDecoderCompPacketsIn_Object = MibTableColumn
frCirExtCompDecoderCompPacketsIn = _FrCirExtCompDecoderCompPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 9),
    _FrCirExtCompDecoderCompPacketsIn_Type()
)
frCirExtCompDecoderCompPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderCompPacketsIn.setStatus("mandatory")
_FrCirExtCompDecoderUncompPacketsIn_Type = Counter32
_FrCirExtCompDecoderUncompPacketsIn_Object = MibTableColumn
frCirExtCompDecoderUncompPacketsIn = _FrCirExtCompDecoderUncompPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 10),
    _FrCirExtCompDecoderUncompPacketsIn_Type()
)
frCirExtCompDecoderUncompPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderUncompPacketsIn.setStatus("mandatory")
_FrCirExtCompDecoderDecompQueueLength_Type = Counter32
_FrCirExtCompDecoderDecompQueueLength_Object = MibTableColumn
frCirExtCompDecoderDecompQueueLength = _FrCirExtCompDecoderDecompQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 11),
    _FrCirExtCompDecoderDecompQueueLength_Type()
)
frCirExtCompDecoderDecompQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderDecompQueueLength.setStatus("mandatory")
_FrCirExtCompDecoderCompressionRatio_Type = Counter32
_FrCirExtCompDecoderCompressionRatio_Object = MibTableColumn
frCirExtCompDecoderCompressionRatio = _FrCirExtCompDecoderCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 12),
    _FrCirExtCompDecoderCompressionRatio_Type()
)
frCirExtCompDecoderCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderCompressionRatio.setStatus("mandatory")
_FrCirExtCompDecoderResetRequestTx_Type = Counter32
_FrCirExtCompDecoderResetRequestTx_Object = MibTableColumn
frCirExtCompDecoderResetRequestTx = _FrCirExtCompDecoderResetRequestTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 13),
    _FrCirExtCompDecoderResetRequestTx_Type()
)
frCirExtCompDecoderResetRequestTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderResetRequestTx.setStatus("mandatory")
_FrCirExtCompDecoderResetAcksRx_Type = Counter32
_FrCirExtCompDecoderResetAcksRx_Object = MibTableColumn
frCirExtCompDecoderResetAcksRx = _FrCirExtCompDecoderResetAcksRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 14),
    _FrCirExtCompDecoderResetAcksRx_Type()
)
frCirExtCompDecoderResetAcksRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderResetAcksRx.setStatus("mandatory")
_FrCirExtCompDecoderRxDiscarded_Type = Counter32
_FrCirExtCompDecoderRxDiscarded_Object = MibTableColumn
frCirExtCompDecoderRxDiscarded = _FrCirExtCompDecoderRxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 15),
    _FrCirExtCompDecoderRxDiscarded_Type()
)
frCirExtCompDecoderRxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderRxDiscarded.setStatus("mandatory")


class _FrCirExtCompDecoderState_Type(Integer32):
    """Custom type frCirExtCompDecoderState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("ok", 1))
    )


_FrCirExtCompDecoderState_Type.__name__ = "Integer32"
_FrCirExtCompDecoderState_Object = MibTableColumn
frCirExtCompDecoderState = _FrCirExtCompDecoderState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 16),
    _FrCirExtCompDecoderState_Type()
)
frCirExtCompDecoderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompDecoderState.setStatus("mandatory")
_FrCirExtCompEncoderBytesIn_Type = Counter32
_FrCirExtCompEncoderBytesIn_Object = MibTableColumn
frCirExtCompEncoderBytesIn = _FrCirExtCompEncoderBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 17),
    _FrCirExtCompEncoderBytesIn_Type()
)
frCirExtCompEncoderBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderBytesIn.setStatus("mandatory")
_FrCirExtCompEncoderCompBytesOut_Type = Counter32
_FrCirExtCompEncoderCompBytesOut_Object = MibTableColumn
frCirExtCompEncoderCompBytesOut = _FrCirExtCompEncoderCompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 18),
    _FrCirExtCompEncoderCompBytesOut_Type()
)
frCirExtCompEncoderCompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderCompBytesOut.setStatus("mandatory")
_FrCirExtCompEncoderUncompBytesOut_Type = Counter32
_FrCirExtCompEncoderUncompBytesOut_Object = MibTableColumn
frCirExtCompEncoderUncompBytesOut = _FrCirExtCompEncoderUncompBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 19),
    _FrCirExtCompEncoderUncompBytesOut_Type()
)
frCirExtCompEncoderUncompBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderUncompBytesOut.setStatus("mandatory")
_FrCirExtCompEncoderCompPacketsOut_Type = Counter32
_FrCirExtCompEncoderCompPacketsOut_Object = MibTableColumn
frCirExtCompEncoderCompPacketsOut = _FrCirExtCompEncoderCompPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 20),
    _FrCirExtCompEncoderCompPacketsOut_Type()
)
frCirExtCompEncoderCompPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderCompPacketsOut.setStatus("mandatory")
_FrCirExtCompEncoderUncompPacketsOut_Type = Counter32
_FrCirExtCompEncoderUncompPacketsOut_Object = MibTableColumn
frCirExtCompEncoderUncompPacketsOut = _FrCirExtCompEncoderUncompPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 21),
    _FrCirExtCompEncoderUncompPacketsOut_Type()
)
frCirExtCompEncoderUncompPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderUncompPacketsOut.setStatus("mandatory")
_FrCirExtCompEncoderCompQueueLength_Type = Counter32
_FrCirExtCompEncoderCompQueueLength_Object = MibTableColumn
frCirExtCompEncoderCompQueueLength = _FrCirExtCompEncoderCompQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 22),
    _FrCirExtCompEncoderCompQueueLength_Type()
)
frCirExtCompEncoderCompQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderCompQueueLength.setStatus("mandatory")
_FrCirExtCompEncoderCompressionRation_Type = Counter32
_FrCirExtCompEncoderCompressionRation_Object = MibTableColumn
frCirExtCompEncoderCompressionRation = _FrCirExtCompEncoderCompressionRation_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 23),
    _FrCirExtCompEncoderCompressionRation_Type()
)
frCirExtCompEncoderCompressionRation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderCompressionRation.setStatus("mandatory")
_FrCirExtCompEncoderResetRequestRx_Type = Counter32
_FrCirExtCompEncoderResetRequestRx_Object = MibTableColumn
frCirExtCompEncoderResetRequestRx = _FrCirExtCompEncoderResetRequestRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 24),
    _FrCirExtCompEncoderResetRequestRx_Type()
)
frCirExtCompEncoderResetRequestRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderResetRequestRx.setStatus("mandatory")
_FrCirExtCompEncoderResetAckTx_Type = Counter32
_FrCirExtCompEncoderResetAckTx_Object = MibTableColumn
frCirExtCompEncoderResetAckTx = _FrCirExtCompEncoderResetAckTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 25),
    _FrCirExtCompEncoderResetAckTx_Type()
)
frCirExtCompEncoderResetAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderResetAckTx.setStatus("mandatory")
_FrCirExtCompEncoderTxDiscarded_Type = Counter32
_FrCirExtCompEncoderTxDiscarded_Object = MibTableColumn
frCirExtCompEncoderTxDiscarded = _FrCirExtCompEncoderTxDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 28, 1, 2, 1, 26),
    _FrCirExtCompEncoderTxDiscarded_Type()
)
frCirExtCompEncoderTxDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCirExtCompEncoderTxDiscarded.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-FREXT-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "frEx": frEx,
       "frCircuitExt": frCircuitExt,
       "frCirExtEncTable": frCirExtEncTable,
       "frCirExtEncEntry": frCirExtEncEntry,
       "frCirExtEncIfIndex": frCirExtEncIfIndex,
       "frCirExtEncDlci": frCirExtEncDlci,
       "frCirExtEncLogicalIfIndex": frCirExtEncLogicalIfIndex,
       "frCirExtEncEnabled": frCirExtEncEnabled,
       "frCirExtEncNegotiated": frCirExtEncNegotiated,
       "frCirExtEncResetRequestsRx": frCirExtEncResetRequestsRx,
       "frCirExtEncResetRequestsTx": frCirExtEncResetRequestsTx,
       "frCirExtEncResetAcksRx": frCirExtEncResetAcksRx,
       "frCirExtEncResetAcksTx": frCirExtEncResetAcksTx,
       "frCirExtEncRxDiscarded": frCirExtEncRxDiscarded,
       "frCirExtEncTxDiscarded": frCirExtEncTxDiscarded,
       "frCirExtEncReceiverState": frCirExtEncReceiverState,
       "frCirExtCompTable": frCirExtCompTable,
       "frCirExtCompEntry": frCirExtCompEntry,
       "frCirExtCompIfIndex": frCirExtCompIfIndex,
       "frCirExtCompDlci": frCirExtCompDlci,
       "frCirExtCompLogicalIfIndex": frCirExtCompLogicalIfIndex,
       "frCirExtCompEnabled": frCirExtCompEnabled,
       "frCirExtCompNegotiated": frCirExtCompNegotiated,
       "frCirExtCompDecoderBytesIn": frCirExtCompDecoderBytesIn,
       "frCirExtCompDecoderDecompBytesOut": frCirExtCompDecoderDecompBytesOut,
       "frCirExtCompDecoderUncompBytesOut": frCirExtCompDecoderUncompBytesOut,
       "frCirExtCompDecoderCompPacketsIn": frCirExtCompDecoderCompPacketsIn,
       "frCirExtCompDecoderUncompPacketsIn": frCirExtCompDecoderUncompPacketsIn,
       "frCirExtCompDecoderDecompQueueLength": frCirExtCompDecoderDecompQueueLength,
       "frCirExtCompDecoderCompressionRatio": frCirExtCompDecoderCompressionRatio,
       "frCirExtCompDecoderResetRequestTx": frCirExtCompDecoderResetRequestTx,
       "frCirExtCompDecoderResetAcksRx": frCirExtCompDecoderResetAcksRx,
       "frCirExtCompDecoderRxDiscarded": frCirExtCompDecoderRxDiscarded,
       "frCirExtCompDecoderState": frCirExtCompDecoderState,
       "frCirExtCompEncoderBytesIn": frCirExtCompEncoderBytesIn,
       "frCirExtCompEncoderCompBytesOut": frCirExtCompEncoderCompBytesOut,
       "frCirExtCompEncoderUncompBytesOut": frCirExtCompEncoderUncompBytesOut,
       "frCirExtCompEncoderCompPacketsOut": frCirExtCompEncoderCompPacketsOut,
       "frCirExtCompEncoderUncompPacketsOut": frCirExtCompEncoderUncompPacketsOut,
       "frCirExtCompEncoderCompQueueLength": frCirExtCompEncoderCompQueueLength,
       "frCirExtCompEncoderCompressionRation": frCirExtCompEncoderCompressionRation,
       "frCirExtCompEncoderResetRequestRx": frCirExtCompEncoderResetRequestRx,
       "frCirExtCompEncoderResetAckTx": frCirExtCompEncoderResetAckTx,
       "frCirExtCompEncoderTxDiscarded": frCirExtCompEncoderTxDiscarded}
)
