# SNMP MIB module (INXNMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INXNMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:29 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Dot3_ObjectIdentity = ObjectIdentity
dot3 = _Dot3_ObjectIdentity(
    (1, 3, 6, 1, 3, 3)
)
_Dot3Table_Object = MibTable
dot3Table = _Dot3Table_Object(
    (1, 3, 6, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    dot3Table.setStatus("mandatory")
_Dot3Entry_Object = MibTableRow
dot3Entry = _Dot3Entry_Object(
    (1, 3, 6, 1, 3, 3, 1, 1)
)
dot3Entry.setIndexNames(
    (0, "INXNMM-MIB", "dot3Index"),
)
if mibBuilder.loadTexts:
    dot3Entry.setStatus("mandatory")
_Dot3Index_Type = Integer32
_Dot3Index_Object = MibTableColumn
dot3Index = _Dot3Index_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 1),
    _Dot3Index_Type()
)
dot3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3Index.setStatus("mandatory")


class _Dot3InitializeMAC_Type(Integer32):
    """Custom type dot3InitializeMAC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initialize", 1)
    )


_Dot3InitializeMAC_Type.__name__ = "Integer32"
_Dot3InitializeMAC_Object = MibTableColumn
dot3InitializeMAC = _Dot3InitializeMAC_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 2),
    _Dot3InitializeMAC_Type()
)
dot3InitializeMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3InitializeMAC.setStatus("mandatory")


class _Dot3MACSubLayerStatus_Type(Integer32):
    """Custom type dot3MACSubLayerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enabled", 1)
    )


_Dot3MACSubLayerStatus_Type.__name__ = "Integer32"
_Dot3MACSubLayerStatus_Object = MibTableColumn
dot3MACSubLayerStatus = _Dot3MACSubLayerStatus_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 3),
    _Dot3MACSubLayerStatus_Type()
)
dot3MACSubLayerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MACSubLayerStatus.setStatus("mandatory")


class _Dot3MulticastReceiveEnabled_Type(Integer32):
    """Custom type dot3MulticastReceiveEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_Dot3MulticastReceiveEnabled_Type.__name__ = "Integer32"
_Dot3MulticastReceiveEnabled_Object = MibTableColumn
dot3MulticastReceiveEnabled = _Dot3MulticastReceiveEnabled_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 4),
    _Dot3MulticastReceiveEnabled_Type()
)
dot3MulticastReceiveEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3MulticastReceiveEnabled.setStatus("mandatory")
_Dot3AlignmentErrors_Type = Counter32
_Dot3AlignmentErrors_Object = MibTableColumn
dot3AlignmentErrors = _Dot3AlignmentErrors_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 5),
    _Dot3AlignmentErrors_Type()
)
dot3AlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3AlignmentErrors.setStatus("mandatory")
_Dot3FCSErrors_Type = Counter32
_Dot3FCSErrors_Object = MibTableColumn
dot3FCSErrors = _Dot3FCSErrors_Object(
    (1, 3, 6, 1, 3, 3, 1, 1, 6),
    _Dot3FCSErrors_Type()
)
dot3FCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3FCSErrors.setStatus("mandatory")
_Dot3TxTable_Object = MibTable
dot3TxTable = _Dot3TxTable_Object(
    (1, 3, 6, 1, 3, 3, 2)
)
if mibBuilder.loadTexts:
    dot3TxTable.setStatus("mandatory")
_Dot3TxEntry_Object = MibTableRow
dot3TxEntry = _Dot3TxEntry_Object(
    (1, 3, 6, 1, 3, 3, 2, 1)
)
dot3TxEntry.setIndexNames(
    (0, "INXNMM-MIB", "dot3TxIndex"),
)
if mibBuilder.loadTexts:
    dot3TxEntry.setStatus("mandatory")
_Dot3TxIndex_Type = Integer32
_Dot3TxIndex_Object = MibTableColumn
dot3TxIndex = _Dot3TxIndex_Object(
    (1, 3, 6, 1, 3, 3, 2, 1, 1),
    _Dot3TxIndex_Type()
)
dot3TxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TxIndex.setStatus("mandatory")
_Dot3TxSingleCollisionFrames_Type = Counter32
_Dot3TxSingleCollisionFrames_Object = MibTableColumn
dot3TxSingleCollisionFrames = _Dot3TxSingleCollisionFrames_Object(
    (1, 3, 6, 1, 3, 3, 2, 1, 2),
    _Dot3TxSingleCollisionFrames_Type()
)
dot3TxSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TxSingleCollisionFrames.setStatus("mandatory")
_Dot3TxMultipleCollisionFrames_Type = Counter32
_Dot3TxMultipleCollisionFrames_Object = MibTableColumn
dot3TxMultipleCollisionFrames = _Dot3TxMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 3, 3, 2, 1, 3),
    _Dot3TxMultipleCollisionFrames_Type()
)
dot3TxMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TxMultipleCollisionFrames.setStatus("mandatory")
_Dot3TxSQETestErrors_Type = Counter32
_Dot3TxSQETestErrors_Object = MibTableColumn
dot3TxSQETestErrors = _Dot3TxSQETestErrors_Object(
    (1, 3, 6, 1, 3, 3, 2, 1, 4),
    _Dot3TxSQETestErrors_Type()
)
dot3TxSQETestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3TxSQETestErrors.setStatus("mandatory")
_Dot3XRxTable_Object = MibTable
dot3XRxTable = _Dot3XRxTable_Object(
    (1, 3, 6, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    dot3XRxTable.setStatus("mandatory")
_Dot3XRxEntry_Object = MibTableRow
dot3XRxEntry = _Dot3XRxEntry_Object(
    (1, 3, 6, 1, 3, 3, 3, 1)
)
dot3XRxEntry.setIndexNames(
    (0, "INXNMM-MIB", "dot3XRxIndex"),
)
if mibBuilder.loadTexts:
    dot3XRxEntry.setStatus("mandatory")
_Dot3XRxIndex_Type = Integer32
_Dot3XRxIndex_Object = MibTableColumn
dot3XRxIndex = _Dot3XRxIndex_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 1),
    _Dot3XRxIndex_Type()
)
dot3XRxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxIndex.setStatus("mandatory")
_Dot3XRxFrameTooLongs_Type = Counter32
_Dot3XRxFrameTooLongs_Object = MibTableColumn
dot3XRxFrameTooLongs = _Dot3XRxFrameTooLongs_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 2),
    _Dot3XRxFrameTooLongs_Type()
)
dot3XRxFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxFrameTooLongs.setStatus("mandatory")
_Dot3XRxInRangeLengthErrors_Type = Counter32
_Dot3XRxInRangeLengthErrors_Object = MibTableColumn
dot3XRxInRangeLengthErrors = _Dot3XRxInRangeLengthErrors_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 3),
    _Dot3XRxInRangeLengthErrors_Type()
)
dot3XRxInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxInRangeLengthErrors.setStatus("mandatory")
_Dot3XRxOutOfRangeLengthFields_Type = Counter32
_Dot3XRxOutOfRangeLengthFields_Object = MibTableColumn
dot3XRxOutOfRangeLengthFields = _Dot3XRxOutOfRangeLengthFields_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 4),
    _Dot3XRxOutOfRangeLengthFields_Type()
)
dot3XRxOutOfRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxOutOfRangeLengthFields.setStatus("mandatory")
_Dot3XRxInternalMACReceiveErrors_Type = Counter32
_Dot3XRxInternalMACReceiveErrors_Object = MibTableColumn
dot3XRxInternalMACReceiveErrors = _Dot3XRxInternalMACReceiveErrors_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 5),
    _Dot3XRxInternalMACReceiveErrors_Type()
)
dot3XRxInternalMACReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxInternalMACReceiveErrors.setStatus("mandatory")
_Dot3XRxAutoPartitionStatus_Type = Integer32
_Dot3XRxAutoPartitionStatus_Object = MibTableColumn
dot3XRxAutoPartitionStatus = _Dot3XRxAutoPartitionStatus_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 6),
    _Dot3XRxAutoPartitionStatus_Type()
)
dot3XRxAutoPartitionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3XRxAutoPartitionStatus.setStatus("mandatory")
_Dot3XRxAutoPartitionLog_Type = Counter32
_Dot3XRxAutoPartitionLog_Object = MibTableColumn
dot3XRxAutoPartitionLog = _Dot3XRxAutoPartitionLog_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 7),
    _Dot3XRxAutoPartitionLog_Type()
)
dot3XRxAutoPartitionLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxAutoPartitionLog.setStatus("mandatory")
_Dot3XRxLastSourceAddress_Type = OctetString
_Dot3XRxLastSourceAddress_Object = MibTableColumn
dot3XRxLastSourceAddress = _Dot3XRxLastSourceAddress_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 8),
    _Dot3XRxLastSourceAddress_Type()
)
dot3XRxLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxLastSourceAddress.setStatus("mandatory")
_Dot3XRxSourceAddressLog_Type = Counter32
_Dot3XRxSourceAddressLog_Object = MibTableColumn
dot3XRxSourceAddressLog = _Dot3XRxSourceAddressLog_Object(
    (1, 3, 6, 1, 3, 3, 3, 1, 9),
    _Dot3XRxSourceAddressLog_Type()
)
dot3XRxSourceAddressLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XRxSourceAddressLog.setStatus("mandatory")
_Dot3XTxTable_Object = MibTable
dot3XTxTable = _Dot3XTxTable_Object(
    (1, 3, 6, 1, 3, 3, 4)
)
if mibBuilder.loadTexts:
    dot3XTxTable.setStatus("mandatory")
_Dot3XTxEntry_Object = MibTableRow
dot3XTxEntry = _Dot3XTxEntry_Object(
    (1, 3, 6, 1, 3, 3, 4, 1)
)
dot3XTxEntry.setIndexNames(
    (0, "INXNMM-MIB", "dot3XTxIndex"),
)
if mibBuilder.loadTexts:
    dot3XTxEntry.setStatus("mandatory")
_Dot3XTxIndex_Type = Integer32
_Dot3XTxIndex_Object = MibTableColumn
dot3XTxIndex = _Dot3XTxIndex_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 1),
    _Dot3XTxIndex_Type()
)
dot3XTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxIndex.setStatus("mandatory")


class _Dot3XTxEnabled_Type(Integer32):
    """Custom type dot3XTxEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_Dot3XTxEnabled_Type.__name__ = "Integer32"
_Dot3XTxEnabled_Object = MibTableColumn
dot3XTxEnabled = _Dot3XTxEnabled_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 2),
    _Dot3XTxEnabled_Type()
)
dot3XTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3XTxEnabled.setStatus("mandatory")
_Dot3XTxDeferredTransmissions_Type = Counter32
_Dot3XTxDeferredTransmissions_Object = MibTableColumn
dot3XTxDeferredTransmissions = _Dot3XTxDeferredTransmissions_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 3),
    _Dot3XTxDeferredTransmissions_Type()
)
dot3XTxDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxDeferredTransmissions.setStatus("mandatory")
_Dot3XTxLateCollisions_Type = Counter32
_Dot3XTxLateCollisions_Object = MibTableColumn
dot3XTxLateCollisions = _Dot3XTxLateCollisions_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 4),
    _Dot3XTxLateCollisions_Type()
)
dot3XTxLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxLateCollisions.setStatus("mandatory")
_Dot3XTxExcessiveCollisions_Type = Counter32
_Dot3XTxExcessiveCollisions_Object = MibTableColumn
dot3XTxExcessiveCollisions = _Dot3XTxExcessiveCollisions_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 5),
    _Dot3XTxExcessiveCollisions_Type()
)
dot3XTxExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxExcessiveCollisions.setStatus("mandatory")
_Dot3XTxInternalMACTransmitErrors_Type = Counter32
_Dot3XTxInternalMACTransmitErrors_Object = MibTableColumn
dot3XTxInternalMACTransmitErrors = _Dot3XTxInternalMACTransmitErrors_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 6),
    _Dot3XTxInternalMACTransmitErrors_Type()
)
dot3XTxInternalMACTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxInternalMACTransmitErrors.setStatus("mandatory")
_Dot3XTxCarrierSenseErrors_Type = Counter32
_Dot3XTxCarrierSenseErrors_Object = MibTableColumn
dot3XTxCarrierSenseErrors = _Dot3XTxCarrierSenseErrors_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 7),
    _Dot3XTxCarrierSenseErrors_Type()
)
dot3XTxCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxCarrierSenseErrors.setStatus("mandatory")
_Dot3XTxExcessiveDeferrals_Type = Counter32
_Dot3XTxExcessiveDeferrals_Object = MibTableColumn
dot3XTxExcessiveDeferrals = _Dot3XTxExcessiveDeferrals_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 8),
    _Dot3XTxExcessiveDeferrals_Type()
)
dot3XTxExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxExcessiveDeferrals.setStatus("mandatory")
_Dot3XTxTDR_Type = Gauge32
_Dot3XTxTDR_Object = MibTableColumn
dot3XTxTDR = _Dot3XTxTDR_Object(
    (1, 3, 6, 1, 3, 3, 4, 1, 9),
    _Dot3XTxTDR_Type()
)
dot3XTxTDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3XTxTDR.setStatus("mandatory")
_Dot3CollTable_Object = MibTable
dot3CollTable = _Dot3CollTable_Object(
    (1, 3, 6, 1, 3, 3, 5)
)
if mibBuilder.loadTexts:
    dot3CollTable.setStatus("mandatory")
_Dot3CollEntry_Object = MibTableRow
dot3CollEntry = _Dot3CollEntry_Object(
    (1, 3, 6, 1, 3, 3, 5, 1)
)
dot3CollEntry.setIndexNames(
    (0, "INXNMM-MIB", "dot3CollIndex"),
    (0, "INXNMM-MIB", "dot3CollCount"),
)
if mibBuilder.loadTexts:
    dot3CollEntry.setStatus("mandatory")
_Dot3CollIndex_Type = Integer32
_Dot3CollIndex_Object = MibTableColumn
dot3CollIndex = _Dot3CollIndex_Object(
    (1, 3, 6, 1, 3, 3, 5, 1, 1),
    _Dot3CollIndex_Type()
)
dot3CollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollIndex.setStatus("mandatory")


class _Dot3CollCount_Type(Integer32):
    """Custom type dot3CollCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Dot3CollCount_Type.__name__ = "Integer32"
_Dot3CollCount_Object = MibTableColumn
dot3CollCount = _Dot3CollCount_Object(
    (1, 3, 6, 1, 3, 3, 5, 1, 2),
    _Dot3CollCount_Type()
)
dot3CollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollCount.setStatus("mandatory")
_Dot3CollFrequency_Type = Counter32
_Dot3CollFrequency_Object = MibTableColumn
dot3CollFrequency = _Dot3CollFrequency_Object(
    (1, 3, 6, 1, 3, 3, 5, 1, 3),
    _Dot3CollFrequency_Type()
)
dot3CollFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3CollFrequency.setStatus("mandatory")
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Interlan_ObjectIdentity = ObjectIdentity
interlan = _Interlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28)
)
_RiProducts_ObjectIdentity = ObjectIdentity
riProducts = _RiProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1)
)
_RiProdLdc_ObjectIdentity = ObjectIdentity
riProdLdc = _RiProdLdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1, 3)
)
_RiPLdcNMM_ObjectIdentity = ObjectIdentity
riPLdcNMM = _RiPLdcNMM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1, 3, 1)
)
_RiTelnet_ObjectIdentity = ObjectIdentity
riTelnet = _RiTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 3)
)
_TnCount_Type = Counter32
_TnCount_Object = MibScalar
tnCount = _TnCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 1),
    _TnCount_Type()
)
tnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnCount.setStatus("mandatory")
_TnTable_Object = MibTable
tnTable = _TnTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2)
)
if mibBuilder.loadTexts:
    tnTable.setStatus("mandatory")
_TnEntry_Object = MibTableRow
tnEntry = _TnEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1)
)
tnEntry.setIndexNames(
    (0, "INXNMM-MIB", "tnLocalIpAddress"),
    (0, "INXNMM-MIB", "tnLocalPort"),
    (0, "INXNMM-MIB", "tnRemoteIpAddress"),
    (0, "INXNMM-MIB", "tnRemotePort"),
)
if mibBuilder.loadTexts:
    tnEntry.setStatus("mandatory")
_TnPort_Type = Integer32
_TnPort_Object = MibTableColumn
tnPort = _TnPort_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 1),
    _TnPort_Type()
)
tnPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnPort.setStatus("mandatory")
_TnLocalIpAddress_Type = IpAddress
_TnLocalIpAddress_Object = MibTableColumn
tnLocalIpAddress = _TnLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 2),
    _TnLocalIpAddress_Type()
)
tnLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLocalIpAddress.setStatus("mandatory")
_TnRemoteIpAddress_Type = IpAddress
_TnRemoteIpAddress_Object = MibTableColumn
tnRemoteIpAddress = _TnRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 3),
    _TnRemoteIpAddress_Type()
)
tnRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRemoteIpAddress.setStatus("mandatory")


class _TnLocalPort_Type(Integer32):
    """Custom type tnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnLocalPort_Type.__name__ = "Integer32"
_TnLocalPort_Object = MibTableColumn
tnLocalPort = _TnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 4),
    _TnLocalPort_Type()
)
tnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLocalPort.setStatus("mandatory")


class _TnRemotePort_Type(Integer32):
    """Custom type tnRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TnRemotePort_Type.__name__ = "Integer32"
_TnRemotePort_Object = MibTableColumn
tnRemotePort = _TnRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 5),
    _TnRemotePort_Type()
)
tnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnRemotePort.setStatus("mandatory")
_TnUpTime_Type = TimeTicks
_TnUpTime_Object = MibTableColumn
tnUpTime = _TnUpTime_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 6),
    _TnUpTime_Type()
)
tnUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUpTime.setStatus("mandatory")
_TnOptionsOn_Type = OctetString
_TnOptionsOn_Object = MibTableColumn
tnOptionsOn = _TnOptionsOn_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 7),
    _TnOptionsOn_Type()
)
tnOptionsOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOptionsOn.setStatus("mandatory")


class _TnState_Type(Integer32):
    """Custom type tnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("serverActive", 1)
    )


_TnState_Type.__name__ = "Integer32"
_TnState_Object = MibTableColumn
tnState = _TnState_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 8),
    _TnState_Type()
)
tnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnState.setStatus("mandatory")
_TnUserId_Type = OctetString
_TnUserId_Object = MibTableColumn
tnUserId = _TnUserId_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 9),
    _TnUserId_Type()
)
tnUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserId.setStatus("mandatory")
_RiLdcNmm_ObjectIdentity = ObjectIdentity
riLdcNmm = _RiLdcNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 10)
)
_RiLdcHardwareRev_Type = DisplayString
_RiLdcHardwareRev_Object = MibScalar
riLdcHardwareRev = _RiLdcHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 1),
    _RiLdcHardwareRev_Type()
)
riLdcHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHardwareRev.setStatus("mandatory")
_RiLdcFirmwareRev_Type = DisplayString
_RiLdcFirmwareRev_Object = MibScalar
riLdcFirmwareRev = _RiLdcFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 2),
    _RiLdcFirmwareRev_Type()
)
riLdcFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcFirmwareRev.setStatus("mandatory")
_RiLdcChassisSoftwareRev_Type = DisplayString
_RiLdcChassisSoftwareRev_Object = MibScalar
riLdcChassisSoftwareRev = _RiLdcChassisSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 3),
    _RiLdcChassisSoftwareRev_Type()
)
riLdcChassisSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcChassisSoftwareRev.setStatus("mandatory")
_RiLdcChassisSerialNumber_Type = DisplayString
_RiLdcChassisSerialNumber_Object = MibScalar
riLdcChassisSerialNumber = _RiLdcChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 4),
    _RiLdcChassisSerialNumber_Type()
)
riLdcChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcChassisSerialNumber.setStatus("mandatory")


class _RiLdcChassisStatus_Type(Integer32):
    """Custom type riLdcChassisStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 7),
          ("enabled", 6),
          ("other", 200),
          ("reset", 1))
    )


_RiLdcChassisStatus_Type.__name__ = "Integer32"
_RiLdcChassisStatus_Object = MibScalar
riLdcChassisStatus = _RiLdcChassisStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 5),
    _RiLdcChassisStatus_Type()
)
riLdcChassisStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcChassisStatus.setStatus("mandatory")
_RiLdcChassisSlotCount_Type = Integer32
_RiLdcChassisSlotCount_Object = MibScalar
riLdcChassisSlotCount = _RiLdcChassisSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 6),
    _RiLdcChassisSlotCount_Type()
)
riLdcChassisSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcChassisSlotCount.setStatus("mandatory")


class _RiLdcNumPowerSupplies_Type(Integer32):
    """Custom type riLdcNumPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RiLdcNumPowerSupplies_Type.__name__ = "Integer32"
_RiLdcNumPowerSupplies_Object = MibScalar
riLdcNumPowerSupplies = _RiLdcNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 7),
    _RiLdcNumPowerSupplies_Type()
)
riLdcNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcNumPowerSupplies.setStatus("mandatory")
_RiLdcNumBusMons_Type = Integer32
_RiLdcNumBusMons_Object = MibScalar
riLdcNumBusMons = _RiLdcNumBusMons_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 8),
    _RiLdcNumBusMons_Type()
)
riLdcNumBusMons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcNumBusMons.setStatus("mandatory")
_RiLdcNumFans_Type = Integer32
_RiLdcNumFans_Object = MibScalar
riLdcNumFans = _RiLdcNumFans_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 9),
    _RiLdcNumFans_Type()
)
riLdcNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcNumFans.setStatus("mandatory")
_RiLdcChassisSlotTable_Object = MibTable
riLdcChassisSlotTable = _RiLdcChassisSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10)
)
if mibBuilder.loadTexts:
    riLdcChassisSlotTable.setStatus("mandatory")
_RiLdcSlotEntry_Object = MibTableRow
riLdcSlotEntry = _RiLdcSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1)
)
riLdcSlotEntry.setIndexNames(
    (0, "INXNMM-MIB", "riLdcSlotIndex"),
)
if mibBuilder.loadTexts:
    riLdcSlotEntry.setStatus("mandatory")
_RiLdcSlotIndex_Type = Integer32
_RiLdcSlotIndex_Object = MibTableColumn
riLdcSlotIndex = _RiLdcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 1),
    _RiLdcSlotIndex_Type()
)
riLdcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotIndex.setStatus("mandatory")
_RiLdcSlotContents_Type = ObjectIdentifier
_RiLdcSlotContents_Object = MibTableColumn
riLdcSlotContents = _RiLdcSlotContents_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 2),
    _RiLdcSlotContents_Type()
)
riLdcSlotContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotContents.setStatus("mandatory")


class _RiLdcSlotAdminStatus_Type(Integer32):
    """Custom type riLdcSlotAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              31,
              34,
              200)
        )
    )
    namedValues = NamedValues(
        *(("booting", 34),
          ("disabled", 7),
          ("empty", 31),
          ("enabled", 6),
          ("other", 200),
          ("reboot", 1))
    )


_RiLdcSlotAdminStatus_Type.__name__ = "Integer32"
_RiLdcSlotAdminStatus_Object = MibTableColumn
riLdcSlotAdminStatus = _RiLdcSlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 3),
    _RiLdcSlotAdminStatus_Type()
)
riLdcSlotAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotAdminStatus.setStatus("mandatory")


class _RiLdcSlotOperStatus_Type(Integer32):
    """Custom type riLdcSlotOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              31,
              34,
              200)
        )
    )
    namedValues = NamedValues(
        *(("booting", 34),
          ("disabled", 7),
          ("empty", 31),
          ("enabled", 6),
          ("other", 200))
    )


_RiLdcSlotOperStatus_Type.__name__ = "Integer32"
_RiLdcSlotOperStatus_Object = MibTableColumn
riLdcSlotOperStatus = _RiLdcSlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 4),
    _RiLdcSlotOperStatus_Type()
)
riLdcSlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotOperStatus.setStatus("mandatory")


class _RiLdcSlotBus_Type(Integer32):
    """Custom type riLdcSlotBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              200)
        )
    )
    namedValues = NamedValues(
        *(("bus-a", 2),
          ("bus-b", 3),
          ("other", 200))
    )


_RiLdcSlotBus_Type.__name__ = "Integer32"
_RiLdcSlotBus_Object = MibTableColumn
riLdcSlotBus = _RiLdcSlotBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 5),
    _RiLdcSlotBus_Type()
)
riLdcSlotBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotBus.setStatus("mandatory")
_RiLdcSlotHwRev_Type = DisplayString
_RiLdcSlotHwRev_Object = MibTableColumn
riLdcSlotHwRev = _RiLdcSlotHwRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 6),
    _RiLdcSlotHwRev_Type()
)
riLdcSlotHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotHwRev.setStatus("mandatory")
_RiLdcSlotFwRev_Type = DisplayString
_RiLdcSlotFwRev_Object = MibTableColumn
riLdcSlotFwRev = _RiLdcSlotFwRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 7),
    _RiLdcSlotFwRev_Type()
)
riLdcSlotFwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotFwRev.setStatus("mandatory")
_RiLdcSlotSwRev_Type = DisplayString
_RiLdcSlotSwRev_Object = MibTableColumn
riLdcSlotSwRev = _RiLdcSlotSwRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 8),
    _RiLdcSlotSwRev_Type()
)
riLdcSlotSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotSwRev.setStatus("mandatory")
_RiLdcSlotSerialNumber_Type = DisplayString
_RiLdcSlotSerialNumber_Object = MibTableColumn
riLdcSlotSerialNumber = _RiLdcSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 9),
    _RiLdcSlotSerialNumber_Type()
)
riLdcSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotSerialNumber.setStatus("mandatory")


class _RiLdcSlotDiagnostic_Type(Integer32):
    """Custom type riLdcSlotDiagnostic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(92,
              93,
              200)
        )
    )
    namedValues = NamedValues(
        *(("fail", 93),
          ("other", 200),
          ("pass", 92))
    )


_RiLdcSlotDiagnostic_Type.__name__ = "Integer32"
_RiLdcSlotDiagnostic_Object = MibTableColumn
riLdcSlotDiagnostic = _RiLdcSlotDiagnostic_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 10),
    _RiLdcSlotDiagnostic_Type()
)
riLdcSlotDiagnostic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotDiagnostic.setStatus("mandatory")
_RiLdcSlotDiagnosticCode_Type = OctetString
_RiLdcSlotDiagnosticCode_Object = MibTableColumn
riLdcSlotDiagnosticCode = _RiLdcSlotDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 11),
    _RiLdcSlotDiagnosticCode_Type()
)
riLdcSlotDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotDiagnosticCode.setStatus("mandatory")
_RiLdcSlotResetTime_Type = TimeTicks
_RiLdcSlotResetTime_Object = MibTableColumn
riLdcSlotResetTime = _RiLdcSlotResetTime_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 12),
    _RiLdcSlotResetTime_Type()
)
riLdcSlotResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotResetTime.setStatus("mandatory")


class _RiLdcSlotTempCondition_Type(Integer32):
    """Custom type riLdcSlotTempCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(60,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("ok", 61),
          ("too-hot", 62),
          ("unknown", 60))
    )


_RiLdcSlotTempCondition_Type.__name__ = "Integer32"
_RiLdcSlotTempCondition_Object = MibTableColumn
riLdcSlotTempCondition = _RiLdcSlotTempCondition_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 13),
    _RiLdcSlotTempCondition_Type()
)
riLdcSlotTempCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotTempCondition.setStatus("mandatory")
_RiLdcSlotConnectivityType_Type = ObjectIdentifier
_RiLdcSlotConnectivityType_Object = MibTableColumn
riLdcSlotConnectivityType = _RiLdcSlotConnectivityType_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 14),
    _RiLdcSlotConnectivityType_Type()
)
riLdcSlotConnectivityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotConnectivityType.setStatus("mandatory")
_RiLdcSlotConnectivityRev_Type = DisplayString
_RiLdcSlotConnectivityRev_Object = MibTableColumn
riLdcSlotConnectivityRev = _RiLdcSlotConnectivityRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 15),
    _RiLdcSlotConnectivityRev_Type()
)
riLdcSlotConnectivityRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotConnectivityRev.setStatus("mandatory")
_RiLdcSlotConnectivitySerialNumber_Type = DisplayString
_RiLdcSlotConnectivitySerialNumber_Object = MibTableColumn
riLdcSlotConnectivitySerialNumber = _RiLdcSlotConnectivitySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 16),
    _RiLdcSlotConnectivitySerialNumber_Type()
)
riLdcSlotConnectivitySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotConnectivitySerialNumber.setStatus("mandatory")


class _RiLdcSlotConnectivityState_Type(Integer32):
    """Custom type riLdcSlotConnectivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              19,
              200)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 10),
          ("enabled", 19),
          ("other", 200))
    )


_RiLdcSlotConnectivityState_Type.__name__ = "Integer32"
_RiLdcSlotConnectivityState_Object = MibTableColumn
riLdcSlotConnectivityState = _RiLdcSlotConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 17),
    _RiLdcSlotConnectivityState_Type()
)
riLdcSlotConnectivityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotConnectivityState.setStatus("mandatory")


class _RiLdcSlotConnectivityBus_Type(Integer32):
    """Custom type riLdcSlotConnectivityBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              200)
        )
    )
    namedValues = NamedValues(
        *(("bus-a", 8),
          ("bus-b", 9),
          ("other", 200))
    )


_RiLdcSlotConnectivityBus_Type.__name__ = "Integer32"
_RiLdcSlotConnectivityBus_Object = MibTableColumn
riLdcSlotConnectivityBus = _RiLdcSlotConnectivityBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 18),
    _RiLdcSlotConnectivityBus_Type()
)
riLdcSlotConnectivityBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotConnectivityBus.setStatus("mandatory")


class _RiLdcSlotConnectivityMedia_Type(Integer32):
    """Custom type riLdcSlotConnectivityMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              17,
              18,
              33,
              34,
              49,
              81,
              82,
              200)
        )
    )
    namedValues = NamedValues(
        *(("backbone-fiber", 13),
          ("backbone-thick", 11),
          ("backbone-thin", 12),
          ("bridge-v35", 81),
          ("bridge-x21", 82),
          ("bt-10-rj45", 34),
          ("bt-10-telco", 33),
          ("foirl-fiber", 49),
          ("nts-rj45", 18),
          ("nts-telco", 17),
          ("other", 200))
    )


_RiLdcSlotConnectivityMedia_Type.__name__ = "Integer32"
_RiLdcSlotConnectivityMedia_Object = MibTableColumn
riLdcSlotConnectivityMedia = _RiLdcSlotConnectivityMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 19),
    _RiLdcSlotConnectivityMedia_Type()
)
riLdcSlotConnectivityMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotConnectivityMedia.setStatus("mandatory")


class _RiLdcSlotSonicBus_Type(Integer32):
    """Custom type riLdcSlotSonicBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              16,
              200)
        )
    )
    namedValues = NamedValues(
        *(("bus-a", 15),
          ("bus-b", 16),
          ("other", 200))
    )


_RiLdcSlotSonicBus_Type.__name__ = "Integer32"
_RiLdcSlotSonicBus_Object = MibTableColumn
riLdcSlotSonicBus = _RiLdcSlotSonicBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 20),
    _RiLdcSlotSonicBus_Type()
)
riLdcSlotSonicBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotSonicBus.setStatus("mandatory")


class _RiLdcSlotModuleType_Type(Integer32):
    """Custom type riLdcSlotModuleType based on Integer32"""
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
              31,
              200)
        )
    )
    namedValues = NamedValues(
        *(("empty", 31),
          ("inx-10bt", 3),
          ("inx-cmm", 4),
          ("inx-foirl", 6),
          ("inx-lbr", 7),
          ("inx-nmm", 1),
          ("inx-nts", 2),
          ("inx-rbr", 5),
          ("other", 200))
    )


_RiLdcSlotModuleType_Type.__name__ = "Integer32"
_RiLdcSlotModuleType_Object = MibTableColumn
riLdcSlotModuleType = _RiLdcSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 21),
    _RiLdcSlotModuleType_Type()
)
riLdcSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcSlotModuleType.setStatus("mandatory")


class _RiLdcSlotStandbyNMM_Type(Integer32):
    """Custom type riLdcSlotStandbyNMM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              200)
        )
    )
    namedValues = NamedValues(
        *(("non-standby-NMM", 4),
          ("other", 200),
          ("standby-NMM", 3))
    )


_RiLdcSlotStandbyNMM_Type.__name__ = "Integer32"
_RiLdcSlotStandbyNMM_Object = MibTableColumn
riLdcSlotStandbyNMM = _RiLdcSlotStandbyNMM_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 10, 1, 22),
    _RiLdcSlotStandbyNMM_Type()
)
riLdcSlotStandbyNMM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcSlotStandbyNMM.setStatus("mandatory")
_RiLdcPowerSupplyTable_Object = MibTable
riLdcPowerSupplyTable = _RiLdcPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 11)
)
if mibBuilder.loadTexts:
    riLdcPowerSupplyTable.setStatus("mandatory")
_RiLdcPSEntry_Object = MibTableRow
riLdcPSEntry = _RiLdcPSEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 11, 1)
)
riLdcPSEntry.setIndexNames(
    (0, "INXNMM-MIB", "riLdcPSIndex"),
)
if mibBuilder.loadTexts:
    riLdcPSEntry.setStatus("mandatory")
_RiLdcPSIndex_Type = Integer32
_RiLdcPSIndex_Object = MibTableColumn
riLdcPSIndex = _RiLdcPSIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 11, 1, 1),
    _RiLdcPSIndex_Type()
)
riLdcPSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcPSIndex.setStatus("mandatory")


class _RiLdcPSActualStatus_Type(Integer32):
    """Custom type riLdcPSActualStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(71,
              72,
              200)
        )
    )
    namedValues = NamedValues(
        *(("active", 72),
          ("off", 71),
          ("other", 200))
    )


_RiLdcPSActualStatus_Type.__name__ = "Integer32"
_RiLdcPSActualStatus_Object = MibTableColumn
riLdcPSActualStatus = _RiLdcPSActualStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 11, 1, 3),
    _RiLdcPSActualStatus_Type()
)
riLdcPSActualStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcPSActualStatus.setStatus("mandatory")
_RiLdcBusMonTable_Object = MibTable
riLdcBusMonTable = _RiLdcBusMonTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12)
)
if mibBuilder.loadTexts:
    riLdcBusMonTable.setStatus("mandatory")
_RiLdcBusMonEntry_Object = MibTableRow
riLdcBusMonEntry = _RiLdcBusMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1)
)
riLdcBusMonEntry.setIndexNames(
    (0, "INXNMM-MIB", "riLdcBusMonIndex"),
)
if mibBuilder.loadTexts:
    riLdcBusMonEntry.setStatus("mandatory")
_RiLdcBusMonIndex_Type = Integer32
_RiLdcBusMonIndex_Object = MibTableColumn
riLdcBusMonIndex = _RiLdcBusMonIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 1),
    _RiLdcBusMonIndex_Type()
)
riLdcBusMonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonIndex.setStatus("mandatory")


class _RiLdcBusMonBus_Type(Integer32):
    """Custom type riLdcBusMonBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("bus-a", 15),
          ("bus-b", 16))
    )


_RiLdcBusMonBus_Type.__name__ = "Integer32"
_RiLdcBusMonBus_Object = MibTableColumn
riLdcBusMonBus = _RiLdcBusMonBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 2),
    _RiLdcBusMonBus_Type()
)
riLdcBusMonBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonBus.setStatus("mandatory")
_RiLdcBusMonFramesReceivedOK_Type = Counter32
_RiLdcBusMonFramesReceivedOK_Object = MibTableColumn
riLdcBusMonFramesReceivedOK = _RiLdcBusMonFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 3),
    _RiLdcBusMonFramesReceivedOK_Type()
)
riLdcBusMonFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonFramesReceivedOK.setStatus("mandatory")
_RiLdcBusMonFramesReceivedOKRate_Type = Gauge32
_RiLdcBusMonFramesReceivedOKRate_Object = MibTableColumn
riLdcBusMonFramesReceivedOKRate = _RiLdcBusMonFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 4),
    _RiLdcBusMonFramesReceivedOKRate_Type()
)
riLdcBusMonFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonFramesReceivedOKRate.setStatus("mandatory")
_RiLdcBusMonOctetsReceivedOK_Type = Counter32
_RiLdcBusMonOctetsReceivedOK_Object = MibTableColumn
riLdcBusMonOctetsReceivedOK = _RiLdcBusMonOctetsReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 5),
    _RiLdcBusMonOctetsReceivedOK_Type()
)
riLdcBusMonOctetsReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonOctetsReceivedOK.setStatus("mandatory")
_RiLdcBusMonOctetsReceivedOKRate_Type = Gauge32
_RiLdcBusMonOctetsReceivedOKRate_Object = MibTableColumn
riLdcBusMonOctetsReceivedOKRate = _RiLdcBusMonOctetsReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 6),
    _RiLdcBusMonOctetsReceivedOKRate_Type()
)
riLdcBusMonOctetsReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonOctetsReceivedOKRate.setStatus("mandatory")
_RiLdcBusMonMCastFramesReceivedOK_Type = Counter32
_RiLdcBusMonMCastFramesReceivedOK_Object = MibTableColumn
riLdcBusMonMCastFramesReceivedOK = _RiLdcBusMonMCastFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 7),
    _RiLdcBusMonMCastFramesReceivedOK_Type()
)
riLdcBusMonMCastFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonMCastFramesReceivedOK.setStatus("mandatory")
_RiLdcBusMonMCastFramesReceivedOKRate_Type = Gauge32
_RiLdcBusMonMCastFramesReceivedOKRate_Object = MibTableColumn
riLdcBusMonMCastFramesReceivedOKRate = _RiLdcBusMonMCastFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 8),
    _RiLdcBusMonMCastFramesReceivedOKRate_Type()
)
riLdcBusMonMCastFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonMCastFramesReceivedOKRate.setStatus("mandatory")
_RiLdcBusMonBCastFramesReceivedOK_Type = Counter32
_RiLdcBusMonBCastFramesReceivedOK_Object = MibTableColumn
riLdcBusMonBCastFramesReceivedOK = _RiLdcBusMonBCastFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 9),
    _RiLdcBusMonBCastFramesReceivedOK_Type()
)
riLdcBusMonBCastFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonBCastFramesReceivedOK.setStatus("mandatory")
_RiLdcBusMonBCastFramesReceivedOKRate_Type = Gauge32
_RiLdcBusMonBCastFramesReceivedOKRate_Object = MibTableColumn
riLdcBusMonBCastFramesReceivedOKRate = _RiLdcBusMonBCastFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 10),
    _RiLdcBusMonBCastFramesReceivedOKRate_Type()
)
riLdcBusMonBCastFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonBCastFramesReceivedOKRate.setStatus("mandatory")
_RiLdcBusMonCollisions_Type = Counter32
_RiLdcBusMonCollisions_Object = MibTableColumn
riLdcBusMonCollisions = _RiLdcBusMonCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 11),
    _RiLdcBusMonCollisions_Type()
)
riLdcBusMonCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonCollisions.setStatus("mandatory")
_RiLdcBusMonCollisionsRate_Type = Gauge32
_RiLdcBusMonCollisionsRate_Object = MibTableColumn
riLdcBusMonCollisionsRate = _RiLdcBusMonCollisionsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 12),
    _RiLdcBusMonCollisionsRate_Type()
)
riLdcBusMonCollisionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonCollisionsRate.setStatus("mandatory")
_RiLdcBusMonLateCollisions_Type = Counter32
_RiLdcBusMonLateCollisions_Object = MibTableColumn
riLdcBusMonLateCollisions = _RiLdcBusMonLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 13),
    _RiLdcBusMonLateCollisions_Type()
)
riLdcBusMonLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonLateCollisions.setStatus("mandatory")
_RiLdcBusMonLateCollisionsRate_Type = Gauge32
_RiLdcBusMonLateCollisionsRate_Object = MibTableColumn
riLdcBusMonLateCollisionsRate = _RiLdcBusMonLateCollisionsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 14),
    _RiLdcBusMonLateCollisionsRate_Type()
)
riLdcBusMonLateCollisionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonLateCollisionsRate.setStatus("mandatory")
_RiLdcBusMonCRCErrors_Type = Counter32
_RiLdcBusMonCRCErrors_Object = MibTableColumn
riLdcBusMonCRCErrors = _RiLdcBusMonCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 15),
    _RiLdcBusMonCRCErrors_Type()
)
riLdcBusMonCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonCRCErrors.setStatus("mandatory")
_RiLdcBusMonCRCErrorsRate_Type = Gauge32
_RiLdcBusMonCRCErrorsRate_Object = MibTableColumn
riLdcBusMonCRCErrorsRate = _RiLdcBusMonCRCErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 16),
    _RiLdcBusMonCRCErrorsRate_Type()
)
riLdcBusMonCRCErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonCRCErrorsRate.setStatus("mandatory")
_RiLdcBusMonPygmies_Type = Counter32
_RiLdcBusMonPygmies_Object = MibTableColumn
riLdcBusMonPygmies = _RiLdcBusMonPygmies_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 17),
    _RiLdcBusMonPygmies_Type()
)
riLdcBusMonPygmies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonPygmies.setStatus("mandatory")
_RiLdcBusMonPygmiesRate_Type = Gauge32
_RiLdcBusMonPygmiesRate_Object = MibTableColumn
riLdcBusMonPygmiesRate = _RiLdcBusMonPygmiesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 18),
    _RiLdcBusMonPygmiesRate_Type()
)
riLdcBusMonPygmiesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonPygmiesRate.setStatus("mandatory")
_RiLdcBusMonShortFrames_Type = Counter32
_RiLdcBusMonShortFrames_Object = MibTableColumn
riLdcBusMonShortFrames = _RiLdcBusMonShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 19),
    _RiLdcBusMonShortFrames_Type()
)
riLdcBusMonShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonShortFrames.setStatus("mandatory")
_RiLdcBusMonShortFramesRate_Type = Gauge32
_RiLdcBusMonShortFramesRate_Object = MibTableColumn
riLdcBusMonShortFramesRate = _RiLdcBusMonShortFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 20),
    _RiLdcBusMonShortFramesRate_Type()
)
riLdcBusMonShortFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonShortFramesRate.setStatus("mandatory")
_RiLdcBusMonInRangeLengthErrors_Type = Counter32
_RiLdcBusMonInRangeLengthErrors_Object = MibTableColumn
riLdcBusMonInRangeLengthErrors = _RiLdcBusMonInRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 21),
    _RiLdcBusMonInRangeLengthErrors_Type()
)
riLdcBusMonInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonInRangeLengthErrors.setStatus("mandatory")
_RiLdcBusMonInRangeLengthErrorsRate_Type = Gauge32
_RiLdcBusMonInRangeLengthErrorsRate_Object = MibTableColumn
riLdcBusMonInRangeLengthErrorsRate = _RiLdcBusMonInRangeLengthErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 22),
    _RiLdcBusMonInRangeLengthErrorsRate_Type()
)
riLdcBusMonInRangeLengthErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonInRangeLengthErrorsRate.setStatus("mandatory")
_RiLdcBusMonOutOfRangeLengthErrors_Type = Counter32
_RiLdcBusMonOutOfRangeLengthErrors_Object = MibTableColumn
riLdcBusMonOutOfRangeLengthErrors = _RiLdcBusMonOutOfRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 23),
    _RiLdcBusMonOutOfRangeLengthErrors_Type()
)
riLdcBusMonOutOfRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonOutOfRangeLengthErrors.setStatus("mandatory")
_RiLdcBusMonOutOfRangeLengthErrorsRate_Type = Gauge32
_RiLdcBusMonOutOfRangeLengthErrorsRate_Object = MibTableColumn
riLdcBusMonOutOfRangeLengthErrorsRate = _RiLdcBusMonOutOfRangeLengthErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 24),
    _RiLdcBusMonOutOfRangeLengthErrorsRate_Type()
)
riLdcBusMonOutOfRangeLengthErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonOutOfRangeLengthErrorsRate.setStatus("mandatory")
_RiLdcBusMonFramesTooLong_Type = Counter32
_RiLdcBusMonFramesTooLong_Object = MibTableColumn
riLdcBusMonFramesTooLong = _RiLdcBusMonFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 25),
    _RiLdcBusMonFramesTooLong_Type()
)
riLdcBusMonFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonFramesTooLong.setStatus("mandatory")
_RiLdcBusMonFramesTooLongRate_Type = Gauge32
_RiLdcBusMonFramesTooLongRate_Object = MibTableColumn
riLdcBusMonFramesTooLongRate = _RiLdcBusMonFramesTooLongRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 26),
    _RiLdcBusMonFramesTooLongRate_Type()
)
riLdcBusMonFramesTooLongRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonFramesTooLongRate.setStatus("mandatory")
_RiLdcBusMonAlignmentErrors_Type = Counter32
_RiLdcBusMonAlignmentErrors_Object = MibTableColumn
riLdcBusMonAlignmentErrors = _RiLdcBusMonAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 27),
    _RiLdcBusMonAlignmentErrors_Type()
)
riLdcBusMonAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonAlignmentErrors.setStatus("mandatory")
_RiLdcBusMonAlignmentErrorsRate_Type = Gauge32
_RiLdcBusMonAlignmentErrorsRate_Object = MibTableColumn
riLdcBusMonAlignmentErrorsRate = _RiLdcBusMonAlignmentErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 28),
    _RiLdcBusMonAlignmentErrorsRate_Type()
)
riLdcBusMonAlignmentErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonAlignmentErrorsRate.setStatus("mandatory")
_RiLdcBusMonMissedPackets_Type = Counter32
_RiLdcBusMonMissedPackets_Object = MibTableColumn
riLdcBusMonMissedPackets = _RiLdcBusMonMissedPackets_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 29),
    _RiLdcBusMonMissedPackets_Type()
)
riLdcBusMonMissedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonMissedPackets.setStatus("mandatory")
_RiLdcBusMonMissedPacketsRate_Type = Gauge32
_RiLdcBusMonMissedPacketsRate_Object = MibTableColumn
riLdcBusMonMissedPacketsRate = _RiLdcBusMonMissedPacketsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 30),
    _RiLdcBusMonMissedPacketsRate_Type()
)
riLdcBusMonMissedPacketsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonMissedPacketsRate.setStatus("mandatory")
_RiLdcBusMonErrorFrames_Type = Counter32
_RiLdcBusMonErrorFrames_Object = MibTableColumn
riLdcBusMonErrorFrames = _RiLdcBusMonErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 31),
    _RiLdcBusMonErrorFrames_Type()
)
riLdcBusMonErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonErrorFrames.setStatus("mandatory")
_RiLdcBusMonErrorFramesRate_Type = Gauge32
_RiLdcBusMonErrorFramesRate_Object = MibTableColumn
riLdcBusMonErrorFramesRate = _RiLdcBusMonErrorFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 32),
    _RiLdcBusMonErrorFramesRate_Type()
)
riLdcBusMonErrorFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonErrorFramesRate.setStatus("mandatory")
_RiLdcBusMonUtilPeak_Type = Gauge32
_RiLdcBusMonUtilPeak_Object = MibTableColumn
riLdcBusMonUtilPeak = _RiLdcBusMonUtilPeak_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 33),
    _RiLdcBusMonUtilPeak_Type()
)
riLdcBusMonUtilPeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcBusMonUtilPeak.setStatus("mandatory")
_RiLdcBusMonUtilPeakTime_Type = TimeTicks
_RiLdcBusMonUtilPeakTime_Object = MibTableColumn
riLdcBusMonUtilPeakTime = _RiLdcBusMonUtilPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 34),
    _RiLdcBusMonUtilPeakTime_Type()
)
riLdcBusMonUtilPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonUtilPeakTime.setStatus("mandatory")
_RiLdcBusMonUtilCurrent_Type = Gauge32
_RiLdcBusMonUtilCurrent_Object = MibTableColumn
riLdcBusMonUtilCurrent = _RiLdcBusMonUtilCurrent_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 12, 1, 35),
    _RiLdcBusMonUtilCurrent_Type()
)
riLdcBusMonUtilCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcBusMonUtilCurrent.setStatus("mandatory")
_RiLdcFanTable_Object = MibTable
riLdcFanTable = _RiLdcFanTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 13)
)
if mibBuilder.loadTexts:
    riLdcFanTable.setStatus("mandatory")
_RiLdcFanEntry_Object = MibTableRow
riLdcFanEntry = _RiLdcFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 13, 1)
)
riLdcFanEntry.setIndexNames(
    (0, "INXNMM-MIB", "riLdcFanIndex"),
)
if mibBuilder.loadTexts:
    riLdcFanEntry.setStatus("mandatory")
_RiLdcFanIndex_Type = Integer32
_RiLdcFanIndex_Object = MibTableColumn
riLdcFanIndex = _RiLdcFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 13, 1, 1),
    _RiLdcFanIndex_Type()
)
riLdcFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcFanIndex.setStatus("mandatory")


class _RiLdcFanStatus_Type(Integer32):
    """Custom type riLdcFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(81,
              82,
              200)
        )
    )
    namedValues = NamedValues(
        *(("off", 81),
          ("on", 82),
          ("other", 200))
    )


_RiLdcFanStatus_Type.__name__ = "Integer32"
_RiLdcFanStatus_Object = MibTableColumn
riLdcFanStatus = _RiLdcFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 13, 1, 2),
    _RiLdcFanStatus_Type()
)
riLdcFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcFanStatus.setStatus("mandatory")
_RiHotFail_ObjectIdentity = ObjectIdentity
riHotFail = _RiHotFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 10, 14)
)
_RiLdcHfAPrimaryAui_Type = Integer32
_RiLdcHfAPrimaryAui_Object = MibScalar
riLdcHfAPrimaryAui = _RiLdcHfAPrimaryAui_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 1),
    _RiLdcHfAPrimaryAui_Type()
)
riLdcHfAPrimaryAui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfAPrimaryAui.setStatus("mandatory")


class _RiLdcHfAPrimaryMedia_Type(Integer32):
    """Custom type riLdcHfAPrimaryMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backbone-fiber", 13),
          ("backbone-thick", 11),
          ("backbone-thin", 12))
    )


_RiLdcHfAPrimaryMedia_Type.__name__ = "Integer32"
_RiLdcHfAPrimaryMedia_Object = MibScalar
riLdcHfAPrimaryMedia = _RiLdcHfAPrimaryMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 2),
    _RiLdcHfAPrimaryMedia_Type()
)
riLdcHfAPrimaryMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfAPrimaryMedia.setStatus("mandatory")
_RiLdcHfBPrimaryAui_Type = Integer32
_RiLdcHfBPrimaryAui_Object = MibScalar
riLdcHfBPrimaryAui = _RiLdcHfBPrimaryAui_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 3),
    _RiLdcHfBPrimaryAui_Type()
)
riLdcHfBPrimaryAui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfBPrimaryAui.setStatus("mandatory")


class _RiLdcHfBPrimaryMedia_Type(Integer32):
    """Custom type riLdcHfBPrimaryMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backbone-fiber", 13),
          ("backbone-thick", 11),
          ("backbone-thin", 12))
    )


_RiLdcHfBPrimaryMedia_Type.__name__ = "Integer32"
_RiLdcHfBPrimaryMedia_Object = MibScalar
riLdcHfBPrimaryMedia = _RiLdcHfBPrimaryMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 4),
    _RiLdcHfBPrimaryMedia_Type()
)
riLdcHfBPrimaryMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfBPrimaryMedia.setStatus("mandatory")
_RiLdcHfABackupAui_Type = Integer32
_RiLdcHfABackupAui_Object = MibScalar
riLdcHfABackupAui = _RiLdcHfABackupAui_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 5),
    _RiLdcHfABackupAui_Type()
)
riLdcHfABackupAui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfABackupAui.setStatus("mandatory")


class _RiLdcHfABackupMedia_Type(Integer32):
    """Custom type riLdcHfABackupMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backbone-fiber", 13),
          ("backbone-thick", 11),
          ("backbone-thin", 12))
    )


_RiLdcHfABackupMedia_Type.__name__ = "Integer32"
_RiLdcHfABackupMedia_Object = MibScalar
riLdcHfABackupMedia = _RiLdcHfABackupMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 6),
    _RiLdcHfABackupMedia_Type()
)
riLdcHfABackupMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfABackupMedia.setStatus("mandatory")
_RiLdcHfBBackupAui_Type = Integer32
_RiLdcHfBBackupAui_Object = MibScalar
riLdcHfBBackupAui = _RiLdcHfBBackupAui_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 7),
    _RiLdcHfBBackupAui_Type()
)
riLdcHfBBackupAui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfBBackupAui.setStatus("mandatory")


class _RiLdcHfBBackupMedia_Type(Integer32):
    """Custom type riLdcHfBBackupMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("backbone-fiber", 13),
          ("backbone-thick", 11),
          ("backbone-thin", 12))
    )


_RiLdcHfBBackupMedia_Type.__name__ = "Integer32"
_RiLdcHfBBackupMedia_Object = MibScalar
riLdcHfBBackupMedia = _RiLdcHfBBackupMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 8),
    _RiLdcHfBBackupMedia_Type()
)
riLdcHfBBackupMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfBBackupMedia.setStatus("mandatory")


class _RiLdcHfIntState_Type(Integer32):
    """Custom type riLdcHfIntState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dis-A-B-conflict", 5),
          ("dis-no-A-config", 3),
          ("dis-no-B-config", 4),
          ("dis-no-backbone", 7),
          ("dis-zero-frequency", 6),
          ("disabled", 2),
          ("enabled", 1))
    )


_RiLdcHfIntState_Type.__name__ = "Integer32"
_RiLdcHfIntState_Object = MibScalar
riLdcHfIntState = _RiLdcHfIntState_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 9),
    _RiLdcHfIntState_Type()
)
riLdcHfIntState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfIntState.setStatus("mandatory")


class _RiLdcHfIntPollFreq_Type(Integer32):
    """Custom type riLdcHfIntPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RiLdcHfIntPollFreq_Type.__name__ = "Integer32"
_RiLdcHfIntPollFreq_Object = MibScalar
riLdcHfIntPollFreq = _RiLdcHfIntPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 10),
    _RiLdcHfIntPollFreq_Type()
)
riLdcHfIntPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfIntPollFreq.setStatus("mandatory")


class _RiLdcHfIntRetries_Type(Integer32):
    """Custom type riLdcHfIntRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RiLdcHfIntRetries_Type.__name__ = "Integer32"
_RiLdcHfIntRetries_Object = MibScalar
riLdcHfIntRetries = _RiLdcHfIntRetries_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 11),
    _RiLdcHfIntRetries_Type()
)
riLdcHfIntRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfIntRetries.setStatus("mandatory")


class _RiLdcHfExtState_Type(Integer32):
    """Custom type riLdcHfExtState based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dis-A-B-conflict", 5),
          ("dis-no-A-config", 3),
          ("dis-no-B-config", 4),
          ("dis-no-backbone", 7),
          ("dis-wrong-ext-bus", 9),
          ("dis-zero-frequency", 6),
          ("dis-zero-p1-addr", 8),
          ("disabled", 2),
          ("enabled", 1))
    )


_RiLdcHfExtState_Type.__name__ = "Integer32"
_RiLdcHfExtState_Object = MibScalar
riLdcHfExtState = _RiLdcHfExtState_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 12),
    _RiLdcHfExtState_Type()
)
riLdcHfExtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtState.setStatus("mandatory")
_RiLdcHfExtPing1_Type = IpAddress
_RiLdcHfExtPing1_Object = MibScalar
riLdcHfExtPing1 = _RiLdcHfExtPing1_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 13),
    _RiLdcHfExtPing1_Type()
)
riLdcHfExtPing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtPing1.setStatus("mandatory")
_RiLdcHfExtPing2_Type = IpAddress
_RiLdcHfExtPing2_Object = MibScalar
riLdcHfExtPing2 = _RiLdcHfExtPing2_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 14),
    _RiLdcHfExtPing2_Type()
)
riLdcHfExtPing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtPing2.setStatus("mandatory")


class _RiLdcHfExtPollFreq_Type(Integer32):
    """Custom type riLdcHfExtPollFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RiLdcHfExtPollFreq_Type.__name__ = "Integer32"
_RiLdcHfExtPollFreq_Object = MibScalar
riLdcHfExtPollFreq = _RiLdcHfExtPollFreq_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 15),
    _RiLdcHfExtPollFreq_Type()
)
riLdcHfExtPollFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtPollFreq.setStatus("mandatory")


class _RiLdcHfExtResponseTmo_Type(Integer32):
    """Custom type riLdcHfExtResponseTmo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RiLdcHfExtResponseTmo_Type.__name__ = "Integer32"
_RiLdcHfExtResponseTmo_Object = MibScalar
riLdcHfExtResponseTmo = _RiLdcHfExtResponseTmo_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 16),
    _RiLdcHfExtResponseTmo_Type()
)
riLdcHfExtResponseTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtResponseTmo.setStatus("mandatory")


class _RiLdcHfExtRetries_Type(Integer32):
    """Custom type riLdcHfExtRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RiLdcHfExtRetries_Type.__name__ = "Integer32"
_RiLdcHfExtRetries_Object = MibScalar
riLdcHfExtRetries = _RiLdcHfExtRetries_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 17),
    _RiLdcHfExtRetries_Type()
)
riLdcHfExtRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfExtRetries.setStatus("mandatory")


class _RiLdcHfHysteresis_Type(Integer32):
    """Custom type riLdcHfHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_RiLdcHfHysteresis_Type.__name__ = "Integer32"
_RiLdcHfHysteresis_Object = MibScalar
riLdcHfHysteresis = _RiLdcHfHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 18),
    _RiLdcHfHysteresis_Type()
)
riLdcHfHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riLdcHfHysteresis.setStatus("mandatory")
_RiLdcHfTable_Object = MibTable
riLdcHfTable = _RiLdcHfTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19)
)
if mibBuilder.loadTexts:
    riLdcHfTable.setStatus("mandatory")
_RiLdcHfEntry_Object = MibTableRow
riLdcHfEntry = _RiLdcHfEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1)
)
riLdcHfEntry.setIndexNames(
    (0, "INXNMM-MIB", "riLdcHfIndex"),
)
if mibBuilder.loadTexts:
    riLdcHfEntry.setStatus("mandatory")


class _RiLdcHfIndex_Type(Integer32):
    """Custom type riLdcHfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RiLdcHfIndex_Type.__name__ = "Integer32"
_RiLdcHfIndex_Object = MibTableColumn
riLdcHfIndex = _RiLdcHfIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 1),
    _RiLdcHfIndex_Type()
)
riLdcHfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfIndex.setStatus("mandatory")


class _RiLdcHfPrimBkupState_Type(Integer32):
    """Custom type riLdcHfPrimBkupState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              200)
        )
    )
    namedValues = NamedValues(
        *(("not-in-use", 200),
          ("using-bkup-config", 2),
          ("using-prim-config", 1))
    )


_RiLdcHfPrimBkupState_Type.__name__ = "Integer32"
_RiLdcHfPrimBkupState_Object = MibTableColumn
riLdcHfPrimBkupState = _RiLdcHfPrimBkupState_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 2),
    _RiLdcHfPrimBkupState_Type()
)
riLdcHfPrimBkupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfPrimBkupState.setStatus("mandatory")
_RiLdcHfLastFailover_Type = TimeTicks
_RiLdcHfLastFailover_Object = MibTableColumn
riLdcHfLastFailover = _RiLdcHfLastFailover_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 3),
    _RiLdcHfLastFailover_Type()
)
riLdcHfLastFailover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfLastFailover.setStatus("mandatory")
_RiLdcHfIntFailovers_Type = Counter32
_RiLdcHfIntFailovers_Object = MibTableColumn
riLdcHfIntFailovers = _RiLdcHfIntFailovers_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 4),
    _RiLdcHfIntFailovers_Type()
)
riLdcHfIntFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfIntFailovers.setStatus("mandatory")
_RiLdcHfExtFailovers_Type = Counter32
_RiLdcHfExtFailovers_Object = MibTableColumn
riLdcHfExtFailovers = _RiLdcHfExtFailovers_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 5),
    _RiLdcHfExtFailovers_Type()
)
riLdcHfExtFailovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfExtFailovers.setStatus("mandatory")


class _RiLdcHfPrimReason_Type(Integer32):
    """Custom type riLdcHfPrimReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autopartitioned", 3),
          ("bus-clock-failure", 4),
          ("config-change", 7),
          ("external-ping-failure", 6),
          ("internal-tx-failure", 5),
          ("nofailover", 1))
    )


_RiLdcHfPrimReason_Type.__name__ = "Integer32"
_RiLdcHfPrimReason_Object = MibTableColumn
riLdcHfPrimReason = _RiLdcHfPrimReason_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 6),
    _RiLdcHfPrimReason_Type()
)
riLdcHfPrimReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfPrimReason.setStatus("mandatory")


class _RiLdcHfBkupReason_Type(Integer32):
    """Custom type riLdcHfBkupReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autopartitioned", 3),
          ("bus-clock-failure", 4),
          ("config-change", 7),
          ("external-ping-failure", 6),
          ("internal-tx-failure", 5),
          ("nofailover", 1))
    )


_RiLdcHfBkupReason_Type.__name__ = "Integer32"
_RiLdcHfBkupReason_Object = MibTableColumn
riLdcHfBkupReason = _RiLdcHfBkupReason_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 7),
    _RiLdcHfBkupReason_Type()
)
riLdcHfBkupReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBkupReason.setStatus("mandatory")


class _RiLdcHfIntTxStatus_Type(Integer32):
    """Custom type riLdcHfIntTxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              200)
        )
    )
    namedValues = NamedValues(
        *(("excess-collisions", 3),
          ("internal-bus-OK", 1),
          ("lost-crs", 2),
          ("not-in-use", 200),
          ("other-tx-error", 4))
    )


_RiLdcHfIntTxStatus_Type.__name__ = "Integer32"
_RiLdcHfIntTxStatus_Object = MibTableColumn
riLdcHfIntTxStatus = _RiLdcHfIntTxStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 8),
    _RiLdcHfIntTxStatus_Type()
)
riLdcHfIntTxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfIntTxStatus.setStatus("mandatory")
_RiLdcHfIntTxFailures_Type = Counter32
_RiLdcHfIntTxFailures_Object = MibTableColumn
riLdcHfIntTxFailures = _RiLdcHfIntTxFailures_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 9),
    _RiLdcHfIntTxFailures_Type()
)
riLdcHfIntTxFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfIntTxFailures.setStatus("mandatory")


class _RiLdcHfAutopartState_Type(Integer32):
    """Custom type riLdcHfAutopartState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              200)
        )
    )
    namedValues = NamedValues(
        *(("aui-OK", 1),
          ("aui-autopartitioned", 2),
          ("not-configured", 200))
    )


_RiLdcHfAutopartState_Type.__name__ = "Integer32"
_RiLdcHfAutopartState_Object = MibTableColumn
riLdcHfAutopartState = _RiLdcHfAutopartState_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 10),
    _RiLdcHfAutopartState_Type()
)
riLdcHfAutopartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfAutopartState.setStatus("mandatory")
_RiLdcHfBusAutopartitions_Type = Counter32
_RiLdcHfBusAutopartitions_Object = MibTableColumn
riLdcHfBusAutopartitions = _RiLdcHfBusAutopartitions_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 11),
    _RiLdcHfBusAutopartitions_Type()
)
riLdcHfBusAutopartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBusAutopartitions.setStatus("mandatory")


class _RiLdcHfBusClockStatus_Type(Integer32):
    """Custom type riLdcHfBusClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bus-clock-failed", 2),
          ("bus-clock-ok", 1))
    )


_RiLdcHfBusClockStatus_Type.__name__ = "Integer32"
_RiLdcHfBusClockStatus_Object = MibTableColumn
riLdcHfBusClockStatus = _RiLdcHfBusClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 12),
    _RiLdcHfBusClockStatus_Type()
)
riLdcHfBusClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBusClockStatus.setStatus("mandatory")
_RiLdcHfBusClockFailures_Type = Counter32
_RiLdcHfBusClockFailures_Object = MibTableColumn
riLdcHfBusClockFailures = _RiLdcHfBusClockFailures_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 13),
    _RiLdcHfBusClockFailures_Type()
)
riLdcHfBusClockFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBusClockFailures.setStatus("mandatory")


class _RiLdcHfBusConfigStatus_Type(Integer32):
    """Custom type riLdcHfBusConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config-ok", 1),
          ("no-backbones-enabled", 3),
          ("two-backbones-enabled", 2))
    )


_RiLdcHfBusConfigStatus_Type.__name__ = "Integer32"
_RiLdcHfBusConfigStatus_Object = MibTableColumn
riLdcHfBusConfigStatus = _RiLdcHfBusConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 14),
    _RiLdcHfBusConfigStatus_Type()
)
riLdcHfBusConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBusConfigStatus.setStatus("mandatory")
_RiLdcHfBusConfigChanges_Type = Counter32
_RiLdcHfBusConfigChanges_Object = MibTableColumn
riLdcHfBusConfigChanges = _RiLdcHfBusConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 15),
    _RiLdcHfBusConfigChanges_Type()
)
riLdcHfBusConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfBusConfigChanges.setStatus("mandatory")


class _RiLdcHfExtPing1Status_Type(Integer32):
    """Custom type riLdcHfExtPing1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              200)
        )
    )
    namedValues = NamedValues(
        *(("external-bus-OK", 1),
          ("host-unreachable", 2),
          ("not-configured", 200))
    )


_RiLdcHfExtPing1Status_Type.__name__ = "Integer32"
_RiLdcHfExtPing1Status_Object = MibTableColumn
riLdcHfExtPing1Status = _RiLdcHfExtPing1Status_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 16),
    _RiLdcHfExtPing1Status_Type()
)
riLdcHfExtPing1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfExtPing1Status.setStatus("mandatory")
_RiLdcHfExtPing1Failures_Type = Counter32
_RiLdcHfExtPing1Failures_Object = MibTableColumn
riLdcHfExtPing1Failures = _RiLdcHfExtPing1Failures_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 17),
    _RiLdcHfExtPing1Failures_Type()
)
riLdcHfExtPing1Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfExtPing1Failures.setStatus("mandatory")


class _RiLdcHfExtPing2Status_Type(Integer32):
    """Custom type riLdcHfExtPing2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              200)
        )
    )
    namedValues = NamedValues(
        *(("external-bus-OK", 1),
          ("host-unreachable", 2),
          ("not-configured", 200))
    )


_RiLdcHfExtPing2Status_Type.__name__ = "Integer32"
_RiLdcHfExtPing2Status_Object = MibTableColumn
riLdcHfExtPing2Status = _RiLdcHfExtPing2Status_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 18),
    _RiLdcHfExtPing2Status_Type()
)
riLdcHfExtPing2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfExtPing2Status.setStatus("mandatory")
_RiLdcHfExtPing2Failures_Type = Counter32
_RiLdcHfExtPing2Failures_Object = MibTableColumn
riLdcHfExtPing2Failures = _RiLdcHfExtPing2Failures_Object(
    (1, 3, 6, 1, 4, 1, 28, 10, 14, 19, 1, 19),
    _RiLdcHfExtPing2Failures_Type()
)
riLdcHfExtPing2Failures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riLdcHfExtPing2Failures.setStatus("mandatory")
_RiPort_ObjectIdentity = ObjectIdentity
riPort = _RiPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 13)
)
_RiPortTable_Object = MibTable
riPortTable = _RiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1)
)
if mibBuilder.loadTexts:
    riPortTable.setStatus("mandatory")
_RiPortEntry_Object = MibTableRow
riPortEntry = _RiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1)
)
riPortEntry.setIndexNames(
    (0, "INXNMM-MIB", "riPortSlotNumber"),
    (0, "INXNMM-MIB", "riPortPortNumber"),
)
if mibBuilder.loadTexts:
    riPortEntry.setStatus("mandatory")
_RiPortSlotNumber_Type = Integer32
_RiPortSlotNumber_Object = MibTableColumn
riPortSlotNumber = _RiPortSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 1),
    _RiPortSlotNumber_Type()
)
riPortSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortSlotNumber.setStatus("mandatory")


class _RiPortPortNumber_Type(Integer32):
    """Custom type riPortPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_RiPortPortNumber_Type.__name__ = "Integer32"
_RiPortPortNumber_Object = MibTableColumn
riPortPortNumber = _RiPortPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 2),
    _RiPortPortNumber_Type()
)
riPortPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortPortNumber.setStatus("mandatory")


class _RiPortState_Type(Integer32):
    """Custom type riPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              41,
              200)
        )
    )
    namedValues = NamedValues(
        *(("auto-partitioned", 3),
          ("disabled", 5),
          ("empty", 41),
          ("enabled", 4),
          ("other", 200))
    )


_RiPortState_Type.__name__ = "Integer32"
_RiPortState_Object = MibTableColumn
riPortState = _RiPortState_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 3),
    _RiPortState_Type()
)
riPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riPortState.setStatus("mandatory")
_RiPortFramesReceivedOK_Type = Counter32
_RiPortFramesReceivedOK_Object = MibTableColumn
riPortFramesReceivedOK = _RiPortFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 4),
    _RiPortFramesReceivedOK_Type()
)
riPortFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortFramesReceivedOK.setStatus("mandatory")
_RiPortFramesReceivedOKRate_Type = Gauge32
_RiPortFramesReceivedOKRate_Object = MibTableColumn
riPortFramesReceivedOKRate = _RiPortFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 5),
    _RiPortFramesReceivedOKRate_Type()
)
riPortFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortFramesReceivedOKRate.setStatus("mandatory")
_RiPortOctetsReceivedOK_Type = Counter32
_RiPortOctetsReceivedOK_Object = MibTableColumn
riPortOctetsReceivedOK = _RiPortOctetsReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 6),
    _RiPortOctetsReceivedOK_Type()
)
riPortOctetsReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortOctetsReceivedOK.setStatus("mandatory")
_RiPortOctetsReceivedOKRate_Type = Gauge32
_RiPortOctetsReceivedOKRate_Object = MibTableColumn
riPortOctetsReceivedOKRate = _RiPortOctetsReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 7),
    _RiPortOctetsReceivedOKRate_Type()
)
riPortOctetsReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortOctetsReceivedOKRate.setStatus("mandatory")
_RiPortMulticastFramesReceivedOK_Type = Counter32
_RiPortMulticastFramesReceivedOK_Object = MibTableColumn
riPortMulticastFramesReceivedOK = _RiPortMulticastFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 8),
    _RiPortMulticastFramesReceivedOK_Type()
)
riPortMulticastFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortMulticastFramesReceivedOK.setStatus("mandatory")
_RiPortMulticastFramesReceivedOKRate_Type = Gauge32
_RiPortMulticastFramesReceivedOKRate_Object = MibTableColumn
riPortMulticastFramesReceivedOKRate = _RiPortMulticastFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 9),
    _RiPortMulticastFramesReceivedOKRate_Type()
)
riPortMulticastFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortMulticastFramesReceivedOKRate.setStatus("mandatory")
_RiPortBroadcastFramesReceivedOK_Type = Counter32
_RiPortBroadcastFramesReceivedOK_Object = MibTableColumn
riPortBroadcastFramesReceivedOK = _RiPortBroadcastFramesReceivedOK_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 10),
    _RiPortBroadcastFramesReceivedOK_Type()
)
riPortBroadcastFramesReceivedOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortBroadcastFramesReceivedOK.setStatus("mandatory")
_RiPortBroadcastFramesReceivedOKRate_Type = Gauge32
_RiPortBroadcastFramesReceivedOKRate_Object = MibTableColumn
riPortBroadcastFramesReceivedOKRate = _RiPortBroadcastFramesReceivedOKRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 11),
    _RiPortBroadcastFramesReceivedOKRate_Type()
)
riPortBroadcastFramesReceivedOKRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortBroadcastFramesReceivedOKRate.setStatus("mandatory")
_RiPortCollisions_Type = Counter32
_RiPortCollisions_Object = MibTableColumn
riPortCollisions = _RiPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 12),
    _RiPortCollisions_Type()
)
riPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortCollisions.setStatus("mandatory")
_RiPortCollisionsRate_Type = Gauge32
_RiPortCollisionsRate_Object = MibTableColumn
riPortCollisionsRate = _RiPortCollisionsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 13),
    _RiPortCollisionsRate_Type()
)
riPortCollisionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortCollisionsRate.setStatus("mandatory")
_RiPortCRCErrors_Type = Counter32
_RiPortCRCErrors_Object = MibTableColumn
riPortCRCErrors = _RiPortCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 14),
    _RiPortCRCErrors_Type()
)
riPortCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortCRCErrors.setStatus("mandatory")
_RiPortCRCErrorsRate_Type = Gauge32
_RiPortCRCErrorsRate_Object = MibTableColumn
riPortCRCErrorsRate = _RiPortCRCErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 15),
    _RiPortCRCErrorsRate_Type()
)
riPortCRCErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortCRCErrorsRate.setStatus("mandatory")
_RiPortShortFrames_Type = Counter32
_RiPortShortFrames_Object = MibTableColumn
riPortShortFrames = _RiPortShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 16),
    _RiPortShortFrames_Type()
)
riPortShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortShortFrames.setStatus("mandatory")
_RiPortShortFramesRate_Type = Gauge32
_RiPortShortFramesRate_Object = MibTableColumn
riPortShortFramesRate = _RiPortShortFramesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 17),
    _RiPortShortFramesRate_Type()
)
riPortShortFramesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortShortFramesRate.setStatus("mandatory")
_RiPortInRangeLengthErrors_Type = Counter32
_RiPortInRangeLengthErrors_Object = MibTableColumn
riPortInRangeLengthErrors = _RiPortInRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 18),
    _RiPortInRangeLengthErrors_Type()
)
riPortInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortInRangeLengthErrors.setStatus("mandatory")
_RiPortInRangeLengthErrorsRate_Type = Gauge32
_RiPortInRangeLengthErrorsRate_Object = MibTableColumn
riPortInRangeLengthErrorsRate = _RiPortInRangeLengthErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 19),
    _RiPortInRangeLengthErrorsRate_Type()
)
riPortInRangeLengthErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortInRangeLengthErrorsRate.setStatus("mandatory")
_RiPortOutOfRangeLengthErrors_Type = Counter32
_RiPortOutOfRangeLengthErrors_Object = MibTableColumn
riPortOutOfRangeLengthErrors = _RiPortOutOfRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 20),
    _RiPortOutOfRangeLengthErrors_Type()
)
riPortOutOfRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortOutOfRangeLengthErrors.setStatus("mandatory")
_RiPortOutOfRangeLengthErrorsRate_Type = Gauge32
_RiPortOutOfRangeLengthErrorsRate_Object = MibTableColumn
riPortOutOfRangeLengthErrorsRate = _RiPortOutOfRangeLengthErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 21),
    _RiPortOutOfRangeLengthErrorsRate_Type()
)
riPortOutOfRangeLengthErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortOutOfRangeLengthErrorsRate.setStatus("mandatory")
_RiPortFramesTooLong_Type = Counter32
_RiPortFramesTooLong_Object = MibTableColumn
riPortFramesTooLong = _RiPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 22),
    _RiPortFramesTooLong_Type()
)
riPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortFramesTooLong.setStatus("mandatory")
_RiPortFramesTooLongRate_Type = Gauge32
_RiPortFramesTooLongRate_Object = MibTableColumn
riPortFramesTooLongRate = _RiPortFramesTooLongRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 23),
    _RiPortFramesTooLongRate_Type()
)
riPortFramesTooLongRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortFramesTooLongRate.setStatus("mandatory")
_RiPortAlignmentErrors_Type = Counter32
_RiPortAlignmentErrors_Object = MibTableColumn
riPortAlignmentErrors = _RiPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 24),
    _RiPortAlignmentErrors_Type()
)
riPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortAlignmentErrors.setStatus("mandatory")
_RiPortAlignmentErrorsRate_Type = Gauge32
_RiPortAlignmentErrorsRate_Object = MibTableColumn
riPortAlignmentErrorsRate = _RiPortAlignmentErrorsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 25),
    _RiPortAlignmentErrorsRate_Type()
)
riPortAlignmentErrorsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortAlignmentErrorsRate.setStatus("mandatory")
_RiPortAutoPartitions_Type = Counter32
_RiPortAutoPartitions_Object = MibTableColumn
riPortAutoPartitions = _RiPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 26),
    _RiPortAutoPartitions_Type()
)
riPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortAutoPartitions.setStatus("mandatory")
_RiPortAutoPartitionsRate_Type = Gauge32
_RiPortAutoPartitionsRate_Object = MibTableColumn
riPortAutoPartitionsRate = _RiPortAutoPartitionsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 27),
    _RiPortAutoPartitionsRate_Type()
)
riPortAutoPartitionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortAutoPartitionsRate.setStatus("mandatory")
_RiPortTransmitClockViolations_Type = Counter32
_RiPortTransmitClockViolations_Object = MibTableColumn
riPortTransmitClockViolations = _RiPortTransmitClockViolations_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 28),
    _RiPortTransmitClockViolations_Type()
)
riPortTransmitClockViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortTransmitClockViolations.setStatus("mandatory")
_RiPortTransmitClockViolationsRate_Type = Gauge32
_RiPortTransmitClockViolationsRate_Object = MibTableColumn
riPortTransmitClockViolationsRate = _RiPortTransmitClockViolationsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 29),
    _RiPortTransmitClockViolationsRate_Type()
)
riPortTransmitClockViolationsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortTransmitClockViolationsRate.setStatus("mandatory")
_RiPortLastSourceAddress_Type = OctetString
_RiPortLastSourceAddress_Object = MibTableColumn
riPortLastSourceAddress = _RiPortLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 30),
    _RiPortLastSourceAddress_Type()
)
riPortLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLastSourceAddress.setStatus("mandatory")
_RiPortSourceAddressChanges_Type = Counter32
_RiPortSourceAddressChanges_Object = MibTableColumn
riPortSourceAddressChanges = _RiPortSourceAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 31),
    _RiPortSourceAddressChanges_Type()
)
riPortSourceAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortSourceAddressChanges.setStatus("mandatory")
_RiPortSourceAddressChangesRate_Type = Gauge32
_RiPortSourceAddressChangesRate_Object = MibTableColumn
riPortSourceAddressChangesRate = _RiPortSourceAddressChangesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 32),
    _RiPortSourceAddressChangesRate_Type()
)
riPortSourceAddressChangesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortSourceAddressChangesRate.setStatus("mandatory")
_RiPortLinkIntegrityChanges_Type = Counter32
_RiPortLinkIntegrityChanges_Object = MibTableColumn
riPortLinkIntegrityChanges = _RiPortLinkIntegrityChanges_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 33),
    _RiPortLinkIntegrityChanges_Type()
)
riPortLinkIntegrityChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLinkIntegrityChanges.setStatus("mandatory")
_RiPortLinkIntegrityChangesRate_Type = Gauge32
_RiPortLinkIntegrityChangesRate_Object = MibTableColumn
riPortLinkIntegrityChangesRate = _RiPortLinkIntegrityChangesRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 34),
    _RiPortLinkIntegrityChangesRate_Type()
)
riPortLinkIntegrityChangesRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLinkIntegrityChangesRate.setStatus("mandatory")
_RiPortLateCollisions_Type = Counter32
_RiPortLateCollisions_Object = MibTableColumn
riPortLateCollisions = _RiPortLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 35),
    _RiPortLateCollisions_Type()
)
riPortLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLateCollisions.setStatus("mandatory")
_RiPortLateCollisionsRate_Type = Gauge32
_RiPortLateCollisionsRate_Object = MibTableColumn
riPortLateCollisionsRate = _RiPortLateCollisionsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 36),
    _RiPortLateCollisionsRate_Type()
)
riPortLateCollisionsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLateCollisionsRate.setStatus("mandatory")
_RiPortMauJabberLockups_Type = Counter32
_RiPortMauJabberLockups_Object = MibTableColumn
riPortMauJabberLockups = _RiPortMauJabberLockups_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 37),
    _RiPortMauJabberLockups_Type()
)
riPortMauJabberLockups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortMauJabberLockups.setStatus("mandatory")
_RiPortMauJabberpLockupsRate_Type = Gauge32
_RiPortMauJabberpLockupsRate_Object = MibScalar
riPortMauJabberpLockupsRate = _RiPortMauJabberpLockupsRate_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 38),
    _RiPortMauJabberpLockupsRate_Type()
)
riPortMauJabberpLockupsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortMauJabberpLockupsRate.setStatus("mandatory")


class _RiPortLinkStatus_Type(Integer32):
    """Custom type riPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              200)
        )
    )
    namedValues = NamedValues(
        *(("link-status-led-off", 2),
          ("link-status-led-on", 1),
          ("other", 200))
    )


_RiPortLinkStatus_Type.__name__ = "Integer32"
_RiPortLinkStatus_Object = MibTableColumn
riPortLinkStatus = _RiPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 13, 1, 1, 39),
    _RiPortLinkStatus_Type()
)
riPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riPortLinkStatus.setStatus("mandatory")
_RiBoot_ObjectIdentity = ObjectIdentity
riBoot = _RiBoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 16)
)
_RiNumBoots_Type = Integer32
_RiNumBoots_Object = MibScalar
riNumBoots = _RiNumBoots_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 1),
    _RiNumBoots_Type()
)
riNumBoots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riNumBoots.setStatus("mandatory")


class _RiBootServiceOffered_Type(Integer32):
    """Custom type riBootServiceOffered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_RiBootServiceOffered_Type.__name__ = "Integer32"
_RiBootServiceOffered_Object = MibScalar
riBootServiceOffered = _RiBootServiceOffered_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 2),
    _RiBootServiceOffered_Type()
)
riBootServiceOffered.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riBootServiceOffered.setStatus("mandatory")
_RiBootTable_Object = MibTable
riBootTable = _RiBootTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3)
)
if mibBuilder.loadTexts:
    riBootTable.setStatus("mandatory")
_RiBootEntry_Object = MibTableRow
riBootEntry = _RiBootEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1)
)
riBootEntry.setIndexNames(
    (0, "INXNMM-MIB", "riBootIndex"),
)
if mibBuilder.loadTexts:
    riBootEntry.setStatus("mandatory")


class _RiBootIndex_Type(Integer32):
    """Custom type riBootIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RiBootIndex_Type.__name__ = "Integer32"
_RiBootIndex_Object = MibTableColumn
riBootIndex = _RiBootIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1, 1),
    _RiBootIndex_Type()
)
riBootIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riBootIndex.setStatus("mandatory")
_RiBootFileName_Type = OctetString
_RiBootFileName_Object = MibTableColumn
riBootFileName = _RiBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1, 3),
    _RiBootFileName_Type()
)
riBootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riBootFileName.setStatus("mandatory")
_RiBootIPAddress_Type = IpAddress
_RiBootIPAddress_Object = MibTableColumn
riBootIPAddress = _RiBootIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1, 6),
    _RiBootIPAddress_Type()
)
riBootIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riBootIPAddress.setStatus("mandatory")
_RiBootVersion_Type = Integer32
_RiBootVersion_Object = MibTableColumn
riBootVersion = _RiBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1, 7),
    _RiBootVersion_Type()
)
riBootVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riBootVersion.setStatus("mandatory")
_RiBootGateway_Type = IpAddress
_RiBootGateway_Object = MibTableColumn
riBootGateway = _RiBootGateway_Object(
    (1, 3, 6, 1, 4, 1, 28, 16, 3, 1, 8),
    _RiBootGateway_Type()
)
riBootGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riBootGateway.setStatus("mandatory")
_RiThresh_ObjectIdentity = ObjectIdentity
riThresh = _RiThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 17)
)
_RiThCount_Type = Gauge32
_RiThCount_Object = MibScalar
riThCount = _RiThCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 1),
    _RiThCount_Type()
)
riThCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riThCount.setStatus("mandatory")
_RiThMaxCount_Type = Integer32
_RiThMaxCount_Object = MibScalar
riThMaxCount = _RiThMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 2),
    _RiThMaxCount_Type()
)
riThMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riThMaxCount.setStatus("mandatory")
_RiThUniqueIndex_Type = Integer32
_RiThUniqueIndex_Object = MibScalar
riThUniqueIndex = _RiThUniqueIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 3),
    _RiThUniqueIndex_Type()
)
riThUniqueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThUniqueIndex.setStatus("mandatory")
_RiThInterval_Type = Integer32
_RiThInterval_Object = MibScalar
riThInterval = _RiThInterval_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 4),
    _RiThInterval_Type()
)
riThInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThInterval.setStatus("mandatory")
_RiThTable_Object = MibTable
riThTable = _RiThTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5)
)
if mibBuilder.loadTexts:
    riThTable.setStatus("mandatory")
_RiThEntry_Object = MibTableRow
riThEntry = _RiThEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1)
)
riThEntry.setIndexNames(
    (0, "INXNMM-MIB", "riThIndex"),
)
if mibBuilder.loadTexts:
    riThEntry.setStatus("mandatory")
_RiThIndex_Type = Integer32
_RiThIndex_Object = MibTableColumn
riThIndex = _RiThIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 1),
    _RiThIndex_Type()
)
riThIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riThIndex.setStatus("mandatory")


class _RiThStatus_Type(Integer32):
    """Custom type riThStatus based on Integer32"""
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
        *(("armed", 3),
          ("delete", 1),
          ("safety", 4),
          ("unset", 2))
    )


_RiThStatus_Type.__name__ = "Integer32"
_RiThStatus_Object = MibTableColumn
riThStatus = _RiThStatus_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 2),
    _RiThStatus_Type()
)
riThStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThStatus.setStatus("mandatory")
_RiThObject_Type = ObjectIdentifier
_RiThObject_Object = MibTableColumn
riThObject = _RiThObject_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 3),
    _RiThObject_Type()
)
riThObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThObject.setStatus("mandatory")
_RiThThreshold_Type = Integer32
_RiThThreshold_Object = MibTableColumn
riThThreshold = _RiThThreshold_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 4),
    _RiThThreshold_Type()
)
riThThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThThreshold.setStatus("mandatory")
_RiThHysteresis_Type = Integer32
_RiThHysteresis_Object = MibTableColumn
riThHysteresis = _RiThHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 5),
    _RiThHysteresis_Type()
)
riThHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThHysteresis.setStatus("mandatory")


class _RiThDirection_Type(Integer32):
    """Custom type riThDirection based on Integer32"""
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


_RiThDirection_Type.__name__ = "Integer32"
_RiThDirection_Object = MibTableColumn
riThDirection = _RiThDirection_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 6),
    _RiThDirection_Type()
)
riThDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThDirection.setStatus("mandatory")
_RiThTriggeredCount_Type = Counter32
_RiThTriggeredCount_Object = MibTableColumn
riThTriggeredCount = _RiThTriggeredCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 7),
    _RiThTriggeredCount_Type()
)
riThTriggeredCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riThTriggeredCount.setStatus("mandatory")
_RiThCommunity_Type = OctetString
_RiThCommunity_Object = MibTableColumn
riThCommunity = _RiThCommunity_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 8),
    _RiThCommunity_Type()
)
riThCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThCommunity.setStatus("mandatory")
_RiThPhysDestination_Type = OctetString
_RiThPhysDestination_Object = MibTableColumn
riThPhysDestination = _RiThPhysDestination_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 9),
    _RiThPhysDestination_Type()
)
riThPhysDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThPhysDestination.setStatus("mandatory")
_RiThIPDestination_Type = IpAddress
_RiThIPDestination_Object = MibTableColumn
riThIPDestination = _RiThIPDestination_Object(
    (1, 3, 6, 1, 4, 1, 28, 17, 5, 1, 10),
    _RiThIPDestination_Type()
)
riThIPDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riThIPDestination.setStatus("mandatory")
_RiSystem_ObjectIdentity = ObjectIdentity
riSystem = _RiSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 18)
)
_RiSystemHardwareRev_Type = DisplayString
_RiSystemHardwareRev_Object = MibScalar
riSystemHardwareRev = _RiSystemHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 1),
    _RiSystemHardwareRev_Type()
)
riSystemHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemHardwareRev.setStatus("mandatory")
_RiSystemFirmwareRev_Type = DisplayString
_RiSystemFirmwareRev_Object = MibScalar
riSystemFirmwareRev = _RiSystemFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 2),
    _RiSystemFirmwareRev_Type()
)
riSystemFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemFirmwareRev.setStatus("mandatory")
_RiSystemSoftwareRev_Type = DisplayString
_RiSystemSoftwareRev_Object = MibScalar
riSystemSoftwareRev = _RiSystemSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 3),
    _RiSystemSoftwareRev_Type()
)
riSystemSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemSoftwareRev.setStatus("mandatory")
_RiSystemSerialNumber_Type = DisplayString
_RiSystemSerialNumber_Object = MibScalar
riSystemSerialNumber = _RiSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 4),
    _RiSystemSerialNumber_Type()
)
riSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemSerialNumber.setStatus("mandatory")


class _RiSystemReset_Type(Integer32):
    """Custom type riSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("resetupdate", 3))
    )


_RiSystemReset_Type.__name__ = "Integer32"
_RiSystemReset_Object = MibScalar
riSystemReset = _RiSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 5),
    _RiSystemReset_Type()
)
riSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riSystemReset.setStatus("mandatory")
_RiSystemTicksPerSecond_Type = Integer32
_RiSystemTicksPerSecond_Object = MibScalar
riSystemTicksPerSecond = _RiSystemTicksPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 12),
    _RiSystemTicksPerSecond_Type()
)
riSystemTicksPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemTicksPerSecond.setStatus("mandatory")
_RiSystemRateInterval_Type = Integer32
_RiSystemRateInterval_Object = MibScalar
riSystemRateInterval = _RiSystemRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 13),
    _RiSystemRateInterval_Type()
)
riSystemRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riSystemRateInterval.setStatus("mandatory")
_RiSystemNVRamWriteCount_Type = Counter32
_RiSystemNVRamWriteCount_Object = MibScalar
riSystemNVRamWriteCount = _RiSystemNVRamWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 18, 15),
    _RiSystemNVRamWriteCount_Type()
)
riSystemNVRamWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riSystemNVRamWriteCount.setStatus("mandatory")
_RiTsRates_ObjectIdentity = ObjectIdentity
riTsRates = _RiTsRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 22)
)
_RiRateTxSingleCollisionFrames_Type = Gauge32
_RiRateTxSingleCollisionFrames_Object = MibScalar
riRateTxSingleCollisionFrames = _RiRateTxSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 1),
    _RiRateTxSingleCollisionFrames_Type()
)
riRateTxSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxSingleCollisionFrames.setStatus("mandatory")
_RiRateTxMultipleCollisionFrames_Type = Gauge32
_RiRateTxMultipleCollisionFrames_Object = MibScalar
riRateTxMultipleCollisionFrames = _RiRateTxMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 2),
    _RiRateTxMultipleCollisionFrames_Type()
)
riRateTxMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxMultipleCollisionFrames.setStatus("mandatory")
_RiRateTxDeferredTransmissions_Type = Gauge32
_RiRateTxDeferredTransmissions_Object = MibScalar
riRateTxDeferredTransmissions = _RiRateTxDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 3),
    _RiRateTxDeferredTransmissions_Type()
)
riRateTxDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxDeferredTransmissions.setStatus("mandatory")
_RiRateTxLateCollisions_Type = Gauge32
_RiRateTxLateCollisions_Object = MibScalar
riRateTxLateCollisions = _RiRateTxLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 4),
    _RiRateTxLateCollisions_Type()
)
riRateTxLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxLateCollisions.setStatus("mandatory")
_RiRateTxInternalMACTransmitErrors_Type = Gauge32
_RiRateTxInternalMACTransmitErrors_Object = MibScalar
riRateTxInternalMACTransmitErrors = _RiRateTxInternalMACTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 5),
    _RiRateTxInternalMACTransmitErrors_Type()
)
riRateTxInternalMACTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxInternalMACTransmitErrors.setStatus("mandatory")
_RiRateTxCarrierSenseErrors_Type = Gauge32
_RiRateTxCarrierSenseErrors_Object = MibScalar
riRateTxCarrierSenseErrors = _RiRateTxCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 6),
    _RiRateTxCarrierSenseErrors_Type()
)
riRateTxCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxCarrierSenseErrors.setStatus("mandatory")
_RiRateTxExcessiveDeferrals_Type = Gauge32
_RiRateTxExcessiveDeferrals_Object = MibScalar
riRateTxExcessiveDeferrals = _RiRateTxExcessiveDeferrals_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 7),
    _RiRateTxExcessiveDeferrals_Type()
)
riRateTxExcessiveDeferrals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateTxExcessiveDeferrals.setStatus("mandatory")
_RiRateRxInternalMACReceiveErrors_Type = Gauge32
_RiRateRxInternalMACReceiveErrors_Object = MibScalar
riRateRxInternalMACReceiveErrors = _RiRateRxInternalMACReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 8),
    _RiRateRxInternalMACReceiveErrors_Type()
)
riRateRxInternalMACReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxInternalMACReceiveErrors.setStatus("mandatory")
_RiRateRxFCSErrors_Type = Gauge32
_RiRateRxFCSErrors_Object = MibScalar
riRateRxFCSErrors = _RiRateRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 9),
    _RiRateRxFCSErrors_Type()
)
riRateRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxFCSErrors.setStatus("mandatory")
_RiRateRxAlignmentErrors_Type = Gauge32
_RiRateRxAlignmentErrors_Object = MibScalar
riRateRxAlignmentErrors = _RiRateRxAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 10),
    _RiRateRxAlignmentErrors_Type()
)
riRateRxAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxAlignmentErrors.setStatus("mandatory")
_RiRateRxInRangeLengthErrors_Type = Gauge32
_RiRateRxInRangeLengthErrors_Object = MibScalar
riRateRxInRangeLengthErrors = _RiRateRxInRangeLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 11),
    _RiRateRxInRangeLengthErrors_Type()
)
riRateRxInRangeLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxInRangeLengthErrors.setStatus("mandatory")
_RiRateRxOutofRangeLengthFields_Type = Gauge32
_RiRateRxOutofRangeLengthFields_Object = MibScalar
riRateRxOutofRangeLengthFields = _RiRateRxOutofRangeLengthFields_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 12),
    _RiRateRxOutofRangeLengthFields_Type()
)
riRateRxOutofRangeLengthFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxOutofRangeLengthFields.setStatus("mandatory")
_RiRateRxFrameTooLongs_Type = Gauge32
_RiRateRxFrameTooLongs_Object = MibScalar
riRateRxFrameTooLongs = _RiRateRxFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 28, 22, 13),
    _RiRateRxFrameTooLongs_Type()
)
riRateRxFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riRateRxFrameTooLongs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INXNMM-MIB",
    **{"internet": internet,
       "experimental": experimental,
       "dot3": dot3,
       "dot3Table": dot3Table,
       "dot3Entry": dot3Entry,
       "dot3Index": dot3Index,
       "dot3InitializeMAC": dot3InitializeMAC,
       "dot3MACSubLayerStatus": dot3MACSubLayerStatus,
       "dot3MulticastReceiveEnabled": dot3MulticastReceiveEnabled,
       "dot3AlignmentErrors": dot3AlignmentErrors,
       "dot3FCSErrors": dot3FCSErrors,
       "dot3TxTable": dot3TxTable,
       "dot3TxEntry": dot3TxEntry,
       "dot3TxIndex": dot3TxIndex,
       "dot3TxSingleCollisionFrames": dot3TxSingleCollisionFrames,
       "dot3TxMultipleCollisionFrames": dot3TxMultipleCollisionFrames,
       "dot3TxSQETestErrors": dot3TxSQETestErrors,
       "dot3XRxTable": dot3XRxTable,
       "dot3XRxEntry": dot3XRxEntry,
       "dot3XRxIndex": dot3XRxIndex,
       "dot3XRxFrameTooLongs": dot3XRxFrameTooLongs,
       "dot3XRxInRangeLengthErrors": dot3XRxInRangeLengthErrors,
       "dot3XRxOutOfRangeLengthFields": dot3XRxOutOfRangeLengthFields,
       "dot3XRxInternalMACReceiveErrors": dot3XRxInternalMACReceiveErrors,
       "dot3XRxAutoPartitionStatus": dot3XRxAutoPartitionStatus,
       "dot3XRxAutoPartitionLog": dot3XRxAutoPartitionLog,
       "dot3XRxLastSourceAddress": dot3XRxLastSourceAddress,
       "dot3XRxSourceAddressLog": dot3XRxSourceAddressLog,
       "dot3XTxTable": dot3XTxTable,
       "dot3XTxEntry": dot3XTxEntry,
       "dot3XTxIndex": dot3XTxIndex,
       "dot3XTxEnabled": dot3XTxEnabled,
       "dot3XTxDeferredTransmissions": dot3XTxDeferredTransmissions,
       "dot3XTxLateCollisions": dot3XTxLateCollisions,
       "dot3XTxExcessiveCollisions": dot3XTxExcessiveCollisions,
       "dot3XTxInternalMACTransmitErrors": dot3XTxInternalMACTransmitErrors,
       "dot3XTxCarrierSenseErrors": dot3XTxCarrierSenseErrors,
       "dot3XTxExcessiveDeferrals": dot3XTxExcessiveDeferrals,
       "dot3XTxTDR": dot3XTxTDR,
       "dot3CollTable": dot3CollTable,
       "dot3CollEntry": dot3CollEntry,
       "dot3CollIndex": dot3CollIndex,
       "dot3CollCount": dot3CollCount,
       "dot3CollFrequency": dot3CollFrequency,
       "private": private,
       "enterprises": enterprises,
       "interlan": interlan,
       "riProducts": riProducts,
       "riProdLdc": riProdLdc,
       "riPLdcNMM": riPLdcNMM,
       "riTelnet": riTelnet,
       "tnCount": tnCount,
       "tnTable": tnTable,
       "tnEntry": tnEntry,
       "tnPort": tnPort,
       "tnLocalIpAddress": tnLocalIpAddress,
       "tnRemoteIpAddress": tnRemoteIpAddress,
       "tnLocalPort": tnLocalPort,
       "tnRemotePort": tnRemotePort,
       "tnUpTime": tnUpTime,
       "tnOptionsOn": tnOptionsOn,
       "tnState": tnState,
       "tnUserId": tnUserId,
       "riLdcNmm": riLdcNmm,
       "riLdcHardwareRev": riLdcHardwareRev,
       "riLdcFirmwareRev": riLdcFirmwareRev,
       "riLdcChassisSoftwareRev": riLdcChassisSoftwareRev,
       "riLdcChassisSerialNumber": riLdcChassisSerialNumber,
       "riLdcChassisStatus": riLdcChassisStatus,
       "riLdcChassisSlotCount": riLdcChassisSlotCount,
       "riLdcNumPowerSupplies": riLdcNumPowerSupplies,
       "riLdcNumBusMons": riLdcNumBusMons,
       "riLdcNumFans": riLdcNumFans,
       "riLdcChassisSlotTable": riLdcChassisSlotTable,
       "riLdcSlotEntry": riLdcSlotEntry,
       "riLdcSlotIndex": riLdcSlotIndex,
       "riLdcSlotContents": riLdcSlotContents,
       "riLdcSlotAdminStatus": riLdcSlotAdminStatus,
       "riLdcSlotOperStatus": riLdcSlotOperStatus,
       "riLdcSlotBus": riLdcSlotBus,
       "riLdcSlotHwRev": riLdcSlotHwRev,
       "riLdcSlotFwRev": riLdcSlotFwRev,
       "riLdcSlotSwRev": riLdcSlotSwRev,
       "riLdcSlotSerialNumber": riLdcSlotSerialNumber,
       "riLdcSlotDiagnostic": riLdcSlotDiagnostic,
       "riLdcSlotDiagnosticCode": riLdcSlotDiagnosticCode,
       "riLdcSlotResetTime": riLdcSlotResetTime,
       "riLdcSlotTempCondition": riLdcSlotTempCondition,
       "riLdcSlotConnectivityType": riLdcSlotConnectivityType,
       "riLdcSlotConnectivityRev": riLdcSlotConnectivityRev,
       "riLdcSlotConnectivitySerialNumber": riLdcSlotConnectivitySerialNumber,
       "riLdcSlotConnectivityState": riLdcSlotConnectivityState,
       "riLdcSlotConnectivityBus": riLdcSlotConnectivityBus,
       "riLdcSlotConnectivityMedia": riLdcSlotConnectivityMedia,
       "riLdcSlotSonicBus": riLdcSlotSonicBus,
       "riLdcSlotModuleType": riLdcSlotModuleType,
       "riLdcSlotStandbyNMM": riLdcSlotStandbyNMM,
       "riLdcPowerSupplyTable": riLdcPowerSupplyTable,
       "riLdcPSEntry": riLdcPSEntry,
       "riLdcPSIndex": riLdcPSIndex,
       "riLdcPSActualStatus": riLdcPSActualStatus,
       "riLdcBusMonTable": riLdcBusMonTable,
       "riLdcBusMonEntry": riLdcBusMonEntry,
       "riLdcBusMonIndex": riLdcBusMonIndex,
       "riLdcBusMonBus": riLdcBusMonBus,
       "riLdcBusMonFramesReceivedOK": riLdcBusMonFramesReceivedOK,
       "riLdcBusMonFramesReceivedOKRate": riLdcBusMonFramesReceivedOKRate,
       "riLdcBusMonOctetsReceivedOK": riLdcBusMonOctetsReceivedOK,
       "riLdcBusMonOctetsReceivedOKRate": riLdcBusMonOctetsReceivedOKRate,
       "riLdcBusMonMCastFramesReceivedOK": riLdcBusMonMCastFramesReceivedOK,
       "riLdcBusMonMCastFramesReceivedOKRate": riLdcBusMonMCastFramesReceivedOKRate,
       "riLdcBusMonBCastFramesReceivedOK": riLdcBusMonBCastFramesReceivedOK,
       "riLdcBusMonBCastFramesReceivedOKRate": riLdcBusMonBCastFramesReceivedOKRate,
       "riLdcBusMonCollisions": riLdcBusMonCollisions,
       "riLdcBusMonCollisionsRate": riLdcBusMonCollisionsRate,
       "riLdcBusMonLateCollisions": riLdcBusMonLateCollisions,
       "riLdcBusMonLateCollisionsRate": riLdcBusMonLateCollisionsRate,
       "riLdcBusMonCRCErrors": riLdcBusMonCRCErrors,
       "riLdcBusMonCRCErrorsRate": riLdcBusMonCRCErrorsRate,
       "riLdcBusMonPygmies": riLdcBusMonPygmies,
       "riLdcBusMonPygmiesRate": riLdcBusMonPygmiesRate,
       "riLdcBusMonShortFrames": riLdcBusMonShortFrames,
       "riLdcBusMonShortFramesRate": riLdcBusMonShortFramesRate,
       "riLdcBusMonInRangeLengthErrors": riLdcBusMonInRangeLengthErrors,
       "riLdcBusMonInRangeLengthErrorsRate": riLdcBusMonInRangeLengthErrorsRate,
       "riLdcBusMonOutOfRangeLengthErrors": riLdcBusMonOutOfRangeLengthErrors,
       "riLdcBusMonOutOfRangeLengthErrorsRate": riLdcBusMonOutOfRangeLengthErrorsRate,
       "riLdcBusMonFramesTooLong": riLdcBusMonFramesTooLong,
       "riLdcBusMonFramesTooLongRate": riLdcBusMonFramesTooLongRate,
       "riLdcBusMonAlignmentErrors": riLdcBusMonAlignmentErrors,
       "riLdcBusMonAlignmentErrorsRate": riLdcBusMonAlignmentErrorsRate,
       "riLdcBusMonMissedPackets": riLdcBusMonMissedPackets,
       "riLdcBusMonMissedPacketsRate": riLdcBusMonMissedPacketsRate,
       "riLdcBusMonErrorFrames": riLdcBusMonErrorFrames,
       "riLdcBusMonErrorFramesRate": riLdcBusMonErrorFramesRate,
       "riLdcBusMonUtilPeak": riLdcBusMonUtilPeak,
       "riLdcBusMonUtilPeakTime": riLdcBusMonUtilPeakTime,
       "riLdcBusMonUtilCurrent": riLdcBusMonUtilCurrent,
       "riLdcFanTable": riLdcFanTable,
       "riLdcFanEntry": riLdcFanEntry,
       "riLdcFanIndex": riLdcFanIndex,
       "riLdcFanStatus": riLdcFanStatus,
       "riHotFail": riHotFail,
       "riLdcHfAPrimaryAui": riLdcHfAPrimaryAui,
       "riLdcHfAPrimaryMedia": riLdcHfAPrimaryMedia,
       "riLdcHfBPrimaryAui": riLdcHfBPrimaryAui,
       "riLdcHfBPrimaryMedia": riLdcHfBPrimaryMedia,
       "riLdcHfABackupAui": riLdcHfABackupAui,
       "riLdcHfABackupMedia": riLdcHfABackupMedia,
       "riLdcHfBBackupAui": riLdcHfBBackupAui,
       "riLdcHfBBackupMedia": riLdcHfBBackupMedia,
       "riLdcHfIntState": riLdcHfIntState,
       "riLdcHfIntPollFreq": riLdcHfIntPollFreq,
       "riLdcHfIntRetries": riLdcHfIntRetries,
       "riLdcHfExtState": riLdcHfExtState,
       "riLdcHfExtPing1": riLdcHfExtPing1,
       "riLdcHfExtPing2": riLdcHfExtPing2,
       "riLdcHfExtPollFreq": riLdcHfExtPollFreq,
       "riLdcHfExtResponseTmo": riLdcHfExtResponseTmo,
       "riLdcHfExtRetries": riLdcHfExtRetries,
       "riLdcHfHysteresis": riLdcHfHysteresis,
       "riLdcHfTable": riLdcHfTable,
       "riLdcHfEntry": riLdcHfEntry,
       "riLdcHfIndex": riLdcHfIndex,
       "riLdcHfPrimBkupState": riLdcHfPrimBkupState,
       "riLdcHfLastFailover": riLdcHfLastFailover,
       "riLdcHfIntFailovers": riLdcHfIntFailovers,
       "riLdcHfExtFailovers": riLdcHfExtFailovers,
       "riLdcHfPrimReason": riLdcHfPrimReason,
       "riLdcHfBkupReason": riLdcHfBkupReason,
       "riLdcHfIntTxStatus": riLdcHfIntTxStatus,
       "riLdcHfIntTxFailures": riLdcHfIntTxFailures,
       "riLdcHfAutopartState": riLdcHfAutopartState,
       "riLdcHfBusAutopartitions": riLdcHfBusAutopartitions,
       "riLdcHfBusClockStatus": riLdcHfBusClockStatus,
       "riLdcHfBusClockFailures": riLdcHfBusClockFailures,
       "riLdcHfBusConfigStatus": riLdcHfBusConfigStatus,
       "riLdcHfBusConfigChanges": riLdcHfBusConfigChanges,
       "riLdcHfExtPing1Status": riLdcHfExtPing1Status,
       "riLdcHfExtPing1Failures": riLdcHfExtPing1Failures,
       "riLdcHfExtPing2Status": riLdcHfExtPing2Status,
       "riLdcHfExtPing2Failures": riLdcHfExtPing2Failures,
       "riPort": riPort,
       "riPortTable": riPortTable,
       "riPortEntry": riPortEntry,
       "riPortSlotNumber": riPortSlotNumber,
       "riPortPortNumber": riPortPortNumber,
       "riPortState": riPortState,
       "riPortFramesReceivedOK": riPortFramesReceivedOK,
       "riPortFramesReceivedOKRate": riPortFramesReceivedOKRate,
       "riPortOctetsReceivedOK": riPortOctetsReceivedOK,
       "riPortOctetsReceivedOKRate": riPortOctetsReceivedOKRate,
       "riPortMulticastFramesReceivedOK": riPortMulticastFramesReceivedOK,
       "riPortMulticastFramesReceivedOKRate": riPortMulticastFramesReceivedOKRate,
       "riPortBroadcastFramesReceivedOK": riPortBroadcastFramesReceivedOK,
       "riPortBroadcastFramesReceivedOKRate": riPortBroadcastFramesReceivedOKRate,
       "riPortCollisions": riPortCollisions,
       "riPortCollisionsRate": riPortCollisionsRate,
       "riPortCRCErrors": riPortCRCErrors,
       "riPortCRCErrorsRate": riPortCRCErrorsRate,
       "riPortShortFrames": riPortShortFrames,
       "riPortShortFramesRate": riPortShortFramesRate,
       "riPortInRangeLengthErrors": riPortInRangeLengthErrors,
       "riPortInRangeLengthErrorsRate": riPortInRangeLengthErrorsRate,
       "riPortOutOfRangeLengthErrors": riPortOutOfRangeLengthErrors,
       "riPortOutOfRangeLengthErrorsRate": riPortOutOfRangeLengthErrorsRate,
       "riPortFramesTooLong": riPortFramesTooLong,
       "riPortFramesTooLongRate": riPortFramesTooLongRate,
       "riPortAlignmentErrors": riPortAlignmentErrors,
       "riPortAlignmentErrorsRate": riPortAlignmentErrorsRate,
       "riPortAutoPartitions": riPortAutoPartitions,
       "riPortAutoPartitionsRate": riPortAutoPartitionsRate,
       "riPortTransmitClockViolations": riPortTransmitClockViolations,
       "riPortTransmitClockViolationsRate": riPortTransmitClockViolationsRate,
       "riPortLastSourceAddress": riPortLastSourceAddress,
       "riPortSourceAddressChanges": riPortSourceAddressChanges,
       "riPortSourceAddressChangesRate": riPortSourceAddressChangesRate,
       "riPortLinkIntegrityChanges": riPortLinkIntegrityChanges,
       "riPortLinkIntegrityChangesRate": riPortLinkIntegrityChangesRate,
       "riPortLateCollisions": riPortLateCollisions,
       "riPortLateCollisionsRate": riPortLateCollisionsRate,
       "riPortMauJabberLockups": riPortMauJabberLockups,
       "riPortMauJabberpLockupsRate": riPortMauJabberpLockupsRate,
       "riPortLinkStatus": riPortLinkStatus,
       "riBoot": riBoot,
       "riNumBoots": riNumBoots,
       "riBootServiceOffered": riBootServiceOffered,
       "riBootTable": riBootTable,
       "riBootEntry": riBootEntry,
       "riBootIndex": riBootIndex,
       "riBootFileName": riBootFileName,
       "riBootIPAddress": riBootIPAddress,
       "riBootVersion": riBootVersion,
       "riBootGateway": riBootGateway,
       "riThresh": riThresh,
       "riThCount": riThCount,
       "riThMaxCount": riThMaxCount,
       "riThUniqueIndex": riThUniqueIndex,
       "riThInterval": riThInterval,
       "riThTable": riThTable,
       "riThEntry": riThEntry,
       "riThIndex": riThIndex,
       "riThStatus": riThStatus,
       "riThObject": riThObject,
       "riThThreshold": riThThreshold,
       "riThHysteresis": riThHysteresis,
       "riThDirection": riThDirection,
       "riThTriggeredCount": riThTriggeredCount,
       "riThCommunity": riThCommunity,
       "riThPhysDestination": riThPhysDestination,
       "riThIPDestination": riThIPDestination,
       "riSystem": riSystem,
       "riSystemHardwareRev": riSystemHardwareRev,
       "riSystemFirmwareRev": riSystemFirmwareRev,
       "riSystemSoftwareRev": riSystemSoftwareRev,
       "riSystemSerialNumber": riSystemSerialNumber,
       "riSystemReset": riSystemReset,
       "riSystemTicksPerSecond": riSystemTicksPerSecond,
       "riSystemRateInterval": riSystemRateInterval,
       "riSystemNVRamWriteCount": riSystemNVRamWriteCount,
       "riTsRates": riTsRates,
       "riRateTxSingleCollisionFrames": riRateTxSingleCollisionFrames,
       "riRateTxMultipleCollisionFrames": riRateTxMultipleCollisionFrames,
       "riRateTxDeferredTransmissions": riRateTxDeferredTransmissions,
       "riRateTxLateCollisions": riRateTxLateCollisions,
       "riRateTxInternalMACTransmitErrors": riRateTxInternalMACTransmitErrors,
       "riRateTxCarrierSenseErrors": riRateTxCarrierSenseErrors,
       "riRateTxExcessiveDeferrals": riRateTxExcessiveDeferrals,
       "riRateRxInternalMACReceiveErrors": riRateRxInternalMACReceiveErrors,
       "riRateRxFCSErrors": riRateRxFCSErrors,
       "riRateRxAlignmentErrors": riRateRxAlignmentErrors,
       "riRateRxInRangeLengthErrors": riRateRxInRangeLengthErrors,
       "riRateRxOutofRangeLengthFields": riRateRxOutofRangeLengthFields,
       "riRateRxFrameTooLongs": riRateRxFrameTooLongs}
)
