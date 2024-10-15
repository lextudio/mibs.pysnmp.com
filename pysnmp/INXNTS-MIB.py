# SNMP MIB module (INXNTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INXNTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:30 2024
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
    (0, "INXNTS-MIB", "dot3Index"),
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
    (0, "INXNTS-MIB", "dot3TxIndex"),
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
    (0, "INXNTS-MIB", "dot3XRxIndex"),
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


class _Dot3XRxAutoPartitionStatus_Type(Integer32):
    """Custom type dot3XRxAutoPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("notpartitioned", 2)
    )


_Dot3XRxAutoPartitionStatus_Type.__name__ = "Integer32"
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
    (0, "INXNTS-MIB", "dot3XTxIndex"),
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
    (0, "INXNTS-MIB", "dot3CollIndex"),
    (0, "INXNTS-MIB", "dot3CollCount"),
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
_RiProdNts_ObjectIdentity = ObjectIdentity
riProdNts = _RiProdNts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1, 2)
)
_RiProdLdc_ObjectIdentity = ObjectIdentity
riProdLdc = _RiProdLdc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1, 3)
)
_RiLdcNts_ObjectIdentity = ObjectIdentity
riLdcNts = _RiLdcNts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 1, 3, 4)
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
    (0, "INXNTS-MIB", "tnLocalIpAddress"),
    (0, "INXNTS-MIB", "tnLocalPort"),
    (0, "INXNTS-MIB", "tnRemoteIpAddress"),
    (0, "INXNTS-MIB", "tnRemotePort"),
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
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client", 3),
          ("serverActive", 1))
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
_TnUserId_Type = DisplayString
_TnUserId_Object = MibTableColumn
tnUserId = _TnUserId_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 9),
    _TnUserId_Type()
)
tnUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnUserId.setStatus("mandatory")
_TnOctetsReceived_Type = Counter32
_TnOctetsReceived_Object = MibTableColumn
tnOctetsReceived = _TnOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 10),
    _TnOctetsReceived_Type()
)
tnOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOctetsReceived.setStatus("mandatory")
_TnOctetsSent_Type = Counter32
_TnOctetsSent_Object = MibTableColumn
tnOctetsSent = _TnOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 11),
    _TnOctetsSent_Type()
)
tnOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnOctetsSent.setStatus("mandatory")
_TnNextType_Type = Integer32
_TnNextType_Object = MibTableColumn
tnNextType = _TnNextType_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 12),
    _TnNextType_Type()
)
tnNextType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNextType.setStatus("mandatory")
_TnNextName_Type = ObjectIdentifier
_TnNextName_Object = MibTableColumn
tnNextName = _TnNextName_Object(
    (1, 3, 6, 1, 4, 1, 28, 3, 2, 1, 13),
    _TnNextName_Type()
)
tnNextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnNextName.setStatus("mandatory")
_RiTs_ObjectIdentity = ObjectIdentity
riTs = _RiTs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 4)
)
_RiTsPortCount_Type = Integer32
_RiTsPortCount_Object = MibScalar
riTsPortCount = _RiTsPortCount_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 1),
    _RiTsPortCount_Type()
)
riTsPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortCount.setStatus("mandatory")
_RiTsSignOn_Type = DisplayString
_RiTsSignOn_Object = MibScalar
riTsSignOn = _RiTsSignOn_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 3),
    _RiTsSignOn_Type()
)
riTsSignOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsSignOn.setStatus("mandatory")
_RiTsPrompt_Type = DisplayString
_RiTsPrompt_Object = MibScalar
riTsPrompt = _RiTsPrompt_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 4),
    _RiTsPrompt_Type()
)
riTsPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPrompt.setStatus("mandatory")
_RiTsAdminPW_Type = DisplayString
_RiTsAdminPW_Object = MibScalar
riTsAdminPW = _RiTsAdminPW_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 5),
    _RiTsAdminPW_Type()
)
riTsAdminPW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsAdminPW.setStatus("mandatory")
_RiTsDomainName_Type = DisplayString
_RiTsDomainName_Object = MibScalar
riTsDomainName = _RiTsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 7),
    _RiTsDomainName_Type()
)
riTsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsDomainName.setStatus("mandatory")
_RiTsUpTimeNodeName_Type = DisplayString
_RiTsUpTimeNodeName_Object = MibScalar
riTsUpTimeNodeName = _RiTsUpTimeNodeName_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 8),
    _RiTsUpTimeNodeName_Type()
)
riTsUpTimeNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsUpTimeNodeName.setStatus("mandatory")


class _RiTsNumBuffers_Type(Integer32):
    """Custom type riTsNumBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_RiTsNumBuffers_Type.__name__ = "Integer32"
_RiTsNumBuffers_Object = MibScalar
riTsNumBuffers = _RiTsNumBuffers_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 9),
    _RiTsNumBuffers_Type()
)
riTsNumBuffers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsNumBuffers.setStatus("mandatory")


class _RiTsReadBufferSize_Type(Integer32):
    """Custom type riTsReadBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 512),
    )


_RiTsReadBufferSize_Type.__name__ = "Integer32"
_RiTsReadBufferSize_Object = MibScalar
riTsReadBufferSize = _RiTsReadBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 10),
    _RiTsReadBufferSize_Type()
)
riTsReadBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsReadBufferSize.setStatus("mandatory")


class _RiTsWriteBufferSize_Type(Integer32):
    """Custom type riTsWriteBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(48, 128),
    )


_RiTsWriteBufferSize_Type.__name__ = "Integer32"
_RiTsWriteBufferSize_Object = MibScalar
riTsWriteBufferSize = _RiTsWriteBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 11),
    _RiTsWriteBufferSize_Type()
)
riTsWriteBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsWriteBufferSize.setStatus("mandatory")


class _RiTsTcpWindowSize_Type(Integer32):
    """Custom type riTsTcpWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1024),
    )


_RiTsTcpWindowSize_Type.__name__ = "Integer32"
_RiTsTcpWindowSize_Object = MibScalar
riTsTcpWindowSize = _RiTsTcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 12),
    _RiTsTcpWindowSize_Type()
)
riTsTcpWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsTcpWindowSize.setStatus("mandatory")


class _RiTsTcpMaxSeg_Type(Integer32):
    """Custom type riTsTcpMaxSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 512),
    )


_RiTsTcpMaxSeg_Type.__name__ = "Integer32"
_RiTsTcpMaxSeg_Object = MibScalar
riTsTcpMaxSeg = _RiTsTcpMaxSeg_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 13),
    _RiTsTcpMaxSeg_Type()
)
riTsTcpMaxSeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsTcpMaxSeg.setStatus("mandatory")


class _RiTsBreakChar_Type(Integer32):
    """Custom type riTsBreakChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RiTsBreakChar_Type.__name__ = "Integer32"
_RiTsBreakChar_Object = MibScalar
riTsBreakChar = _RiTsBreakChar_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 14),
    _RiTsBreakChar_Type()
)
riTsBreakChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsBreakChar.setStatus("mandatory")
_RiTsFarMemoryFree_Type = Integer32
_RiTsFarMemoryFree_Object = MibScalar
riTsFarMemoryFree = _RiTsFarMemoryFree_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 22),
    _RiTsFarMemoryFree_Type()
)
riTsFarMemoryFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsFarMemoryFree.setStatus("mandatory")
_RiTsFarMemoryLowest_Type = Integer32
_RiTsFarMemoryLowest_Object = MibScalar
riTsFarMemoryLowest = _RiTsFarMemoryLowest_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 24),
    _RiTsFarMemoryLowest_Type()
)
riTsFarMemoryLowest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsFarMemoryLowest.setStatus("mandatory")


class _RiTsTcpAckTimer_Type(Integer32):
    """Custom type riTsTcpAckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 300),
    )


_RiTsTcpAckTimer_Type.__name__ = "Integer32"
_RiTsTcpAckTimer_Object = MibScalar
riTsTcpAckTimer = _RiTsTcpAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 25),
    _RiTsTcpAckTimer_Type()
)
riTsTcpAckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsTcpAckTimer.setStatus("mandatory")
_RiTsPortTable_Object = MibTable
riTsPortTable = _RiTsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28)
)
if mibBuilder.loadTexts:
    riTsPortTable.setStatus("mandatory")
_RiTsPortEntry_Object = MibTableRow
riTsPortEntry = _RiTsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1)
)
riTsPortEntry.setIndexNames(
    (0, "INXNTS-MIB", "riTsPortIndex"),
)
if mibBuilder.loadTexts:
    riTsPortEntry.setStatus("mandatory")


class _RiTsPortIndex_Type(Integer32):
    """Custom type riTsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RiTsPortIndex_Type.__name__ = "Integer32"
_RiTsPortIndex_Object = MibTableColumn
riTsPortIndex = _RiTsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 1),
    _RiTsPortIndex_Type()
)
riTsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortIndex.setStatus("mandatory")


class _RiTsPortFirstType_Type(Integer32):
    """Custom type riTsPortFirstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 5),
          ("none", 1),
          ("telnet", 4))
    )


_RiTsPortFirstType_Type.__name__ = "Integer32"
_RiTsPortFirstType_Object = MibTableColumn
riTsPortFirstType = _RiTsPortFirstType_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 2),
    _RiTsPortFirstType_Type()
)
riTsPortFirstType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortFirstType.setStatus("mandatory")


class _RiTsPortActiveType_Type(Integer32):
    """Custom type riTsPortActiveType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dummy", 5),
          ("none", 1),
          ("telnet", 4))
    )


_RiTsPortActiveType_Type.__name__ = "Integer32"
_RiTsPortActiveType_Object = MibTableColumn
riTsPortActiveType = _RiTsPortActiveType_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 4),
    _RiTsPortActiveType_Type()
)
riTsPortActiveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortActiveType.setStatus("mandatory")
_RiTsPortNumSessions_Type = Gauge32
_RiTsPortNumSessions_Object = MibTableColumn
riTsPortNumSessions = _RiTsPortNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 6),
    _RiTsPortNumSessions_Type()
)
riTsPortNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortNumSessions.setStatus("mandatory")


class _RiTsPortBaudIn_Type(Integer32):
    """Custom type riTsPortBaudIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(110,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("br-110", 110),
          ("br-1200", 1200),
          ("br-19200", 19200),
          ("br-2400", 2400),
          ("br-300", 300),
          ("br-38400", 38400),
          ("br-4800", 4800),
          ("br-600", 600),
          ("br-9600", 9600))
    )


_RiTsPortBaudIn_Type.__name__ = "Integer32"
_RiTsPortBaudIn_Object = MibTableColumn
riTsPortBaudIn = _RiTsPortBaudIn_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 7),
    _RiTsPortBaudIn_Type()
)
riTsPortBaudIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortBaudIn.setStatus("mandatory")


class _RiTsPortBaudOut_Type(Integer32):
    """Custom type riTsPortBaudOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(110,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("br-110", 110),
          ("br-1200", 1200),
          ("br-19200", 19200),
          ("br-2400", 2400),
          ("br-300", 300),
          ("br-38400", 38400),
          ("br-4800", 4800),
          ("br-600", 600),
          ("br-9600", 9600))
    )


_RiTsPortBaudOut_Type.__name__ = "Integer32"
_RiTsPortBaudOut_Object = MibTableColumn
riTsPortBaudOut = _RiTsPortBaudOut_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 8),
    _RiTsPortBaudOut_Type()
)
riTsPortBaudOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortBaudOut.setStatus("mandatory")


class _RiTsPortParity_Type(Integer32):
    """Custom type riTsPortParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_RiTsPortParity_Type.__name__ = "Integer32"
_RiTsPortParity_Object = MibTableColumn
riTsPortParity = _RiTsPortParity_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 9),
    _RiTsPortParity_Type()
)
riTsPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortParity.setStatus("mandatory")


class _RiTsPortDataBits_Type(Integer32):
    """Custom type riTsPortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_RiTsPortDataBits_Type.__name__ = "Integer32"
_RiTsPortDataBits_Object = MibTableColumn
riTsPortDataBits = _RiTsPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 11),
    _RiTsPortDataBits_Type()
)
riTsPortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortDataBits.setStatus("mandatory")


class _RiTsPortModemControl_Type(Integer32):
    """Custom type riTsPortModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 3),
          ("none", 1))
    )


_RiTsPortModemControl_Type.__name__ = "Integer32"
_RiTsPortModemControl_Object = MibTableColumn
riTsPortModemControl = _RiTsPortModemControl_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 14),
    _RiTsPortModemControl_Type()
)
riTsPortModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortModemControl.setStatus("mandatory")


class _RiTsPortFlowControlIn_Type(Integer32):
    """Custom type riTsPortFlowControlIn based on Integer32"""
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
        *(("handx", 4),
          ("hardware", 3),
          ("none", 1),
          ("xonxoff", 2))
    )


_RiTsPortFlowControlIn_Type.__name__ = "Integer32"
_RiTsPortFlowControlIn_Object = MibTableColumn
riTsPortFlowControlIn = _RiTsPortFlowControlIn_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 15),
    _RiTsPortFlowControlIn_Type()
)
riTsPortFlowControlIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortFlowControlIn.setStatus("mandatory")


class _RiTsPortFlowControlOut_Type(Integer32):
    """Custom type riTsPortFlowControlOut based on Integer32"""
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
        *(("handx", 4),
          ("hardware", 3),
          ("none", 1),
          ("xonxoff", 2))
    )


_RiTsPortFlowControlOut_Type.__name__ = "Integer32"
_RiTsPortFlowControlOut_Object = MibTableColumn
riTsPortFlowControlOut = _RiTsPortFlowControlOut_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 16),
    _RiTsPortFlowControlOut_Type()
)
riTsPortFlowControlOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortFlowControlOut.setStatus("mandatory")


class _RiTsPortRing_Type(Integer32):
    """Custom type riTsPortRing based on Integer32"""
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


_RiTsPortRing_Type.__name__ = "Integer32"
_RiTsPortRing_Object = MibTableColumn
riTsPortRing = _RiTsPortRing_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 17),
    _RiTsPortRing_Type()
)
riTsPortRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortRing.setStatus("mandatory")
_RiTsPortPassword_Type = OctetString
_RiTsPortPassword_Object = MibTableColumn
riTsPortPassword = _RiTsPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 18),
    _RiTsPortPassword_Type()
)
riTsPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortPassword.setStatus("mandatory")


class _RiTsPortAbortOut_Type(Integer32):
    """Custom type riTsPortAbortOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiTsPortAbortOut_Type.__name__ = "Integer32"
_RiTsPortAbortOut_Object = MibTableColumn
riTsPortAbortOut = _RiTsPortAbortOut_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 19),
    _RiTsPortAbortOut_Type()
)
riTsPortAbortOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortAbortOut.setStatus("mandatory")


class _RiTsPortIntProc_Type(Integer32):
    """Custom type riTsPortIntProc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiTsPortIntProc_Type.__name__ = "Integer32"
_RiTsPortIntProc_Object = MibTableColumn
riTsPortIntProc = _RiTsPortIntProc_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 20),
    _RiTsPortIntProc_Type()
)
riTsPortIntProc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortIntProc.setStatus("mandatory")


class _RiTsPortInactiveTimeOut_Type(Integer32):
    """Custom type riTsPortInactiveTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiTsPortInactiveTimeOut_Type.__name__ = "Integer32"
_RiTsPortInactiveTimeOut_Object = MibTableColumn
riTsPortInactiveTimeOut = _RiTsPortInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 21),
    _RiTsPortInactiveTimeOut_Type()
)
riTsPortInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortInactiveTimeOut.setStatus("mandatory")


class _RiTsPortInactiveTimer_Type(Integer32):
    """Custom type riTsPortInactiveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RiTsPortInactiveTimer_Type.__name__ = "Integer32"
_RiTsPortInactiveTimer_Object = MibTableColumn
riTsPortInactiveTimer = _RiTsPortInactiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 22),
    _RiTsPortInactiveTimer_Type()
)
riTsPortInactiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortInactiveTimer.setStatus("mandatory")


class _RiTsPortMachineInterface_Type(Integer32):
    """Custom type riTsPortMachineInterface based on Integer32"""
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


_RiTsPortMachineInterface_Type.__name__ = "Integer32"
_RiTsPortMachineInterface_Object = MibTableColumn
riTsPortMachineInterface = _RiTsPortMachineInterface_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 23),
    _RiTsPortMachineInterface_Type()
)
riTsPortMachineInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortMachineInterface.setStatus("mandatory")


class _RiTsPortFunction_Type(Integer32):
    """Custom type riTsPortFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("both", 4),
          ("demandckt", 5),
          ("permckt", 3),
          ("queue", 6),
          ("slave", 1),
          ("terminal", 2))
    )


_RiTsPortFunction_Type.__name__ = "Integer32"
_RiTsPortFunction_Object = MibTableColumn
riTsPortFunction = _RiTsPortFunction_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 25),
    _RiTsPortFunction_Type()
)
riTsPortFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortFunction.setStatus("mandatory")


class _RiTsPortState_Type(Integer32):
    """Custom type riTsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("disabled", 1))
    )


_RiTsPortState_Type.__name__ = "Integer32"
_RiTsPortState_Object = MibTableColumn
riTsPortState = _RiTsPortState_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 26),
    _RiTsPortState_Type()
)
riTsPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortState.setStatus("mandatory")
_RiTsPortOctetsIn_Type = Counter32
_RiTsPortOctetsIn_Object = MibTableColumn
riTsPortOctetsIn = _RiTsPortOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 27),
    _RiTsPortOctetsIn_Type()
)
riTsPortOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortOctetsIn.setStatus("mandatory")
_RiTsPortOctetsOut_Type = Counter32
_RiTsPortOctetsOut_Object = MibTableColumn
riTsPortOctetsOut = _RiTsPortOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 28),
    _RiTsPortOctetsOut_Type()
)
riTsPortOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortOctetsOut.setStatus("mandatory")


class _RiTsPortXONChar_Type(Integer32):
    """Custom type riTsPortXONChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_RiTsPortXONChar_Type.__name__ = "Integer32"
_RiTsPortXONChar_Object = MibTableColumn
riTsPortXONChar = _RiTsPortXONChar_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 30),
    _RiTsPortXONChar_Type()
)
riTsPortXONChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortXONChar.setStatus("mandatory")


class _RiTsPortXOFFChar_Type(Integer32):
    """Custom type riTsPortXOFFChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_RiTsPortXOFFChar_Type.__name__ = "Integer32"
_RiTsPortXOFFChar_Object = MibTableColumn
riTsPortXOFFChar = _RiTsPortXOFFChar_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 31),
    _RiTsPortXOFFChar_Type()
)
riTsPortXOFFChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortXOFFChar.setStatus("mandatory")
_RiTsPortMaxSess_Type = Integer32
_RiTsPortMaxSess_Object = MibTableColumn
riTsPortMaxSess = _RiTsPortMaxSess_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 32),
    _RiTsPortMaxSess_Type()
)
riTsPortMaxSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riTsPortMaxSess.setStatus("mandatory")


class _RiTsPortServerPort_Type(Integer32):
    """Custom type riTsPortServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RiTsPortServerPort_Type.__name__ = "Integer32"
_RiTsPortServerPort_Object = MibTableColumn
riTsPortServerPort = _RiTsPortServerPort_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 33),
    _RiTsPortServerPort_Type()
)
riTsPortServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortServerPort.setStatus("mandatory")


class _RiTsPortTCPMode_Type(Integer32):
    """Custom type riTsPortTCPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nvt7bit", 2),
          ("nvt8bit", 3),
          ("rawsocket", 1))
    )


_RiTsPortTCPMode_Type.__name__ = "Integer32"
_RiTsPortTCPMode_Object = MibTableColumn
riTsPortTCPMode = _RiTsPortTCPMode_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 36),
    _RiTsPortTCPMode_Type()
)
riTsPortTCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortTCPMode.setStatus("mandatory")


class _RiTsPortDefXparent_Type(Integer32):
    """Custom type riTsPortDefXparent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_RiTsPortDefXparent_Type.__name__ = "Integer32"
_RiTsPortDefXparent_Object = MibTableColumn
riTsPortDefXparent = _RiTsPortDefXparent_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 37),
    _RiTsPortDefXparent_Type()
)
riTsPortDefXparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortDefXparent.setStatus("mandatory")


class _RiTsPortDefEcho_Type(Integer32):
    """Custom type riTsPortDefEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_RiTsPortDefEcho_Type.__name__ = "Integer32"
_RiTsPortDefEcho_Object = MibTableColumn
riTsPortDefEcho = _RiTsPortDefEcho_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 28, 1, 38),
    _RiTsPortDefEcho_Type()
)
riTsPortDefEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsPortDefEcho.setStatus("mandatory")
_RiTsDomainServerAddress_Type = IpAddress
_RiTsDomainServerAddress_Object = MibTableColumn
riTsDomainServerAddress = _RiTsDomainServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 28, 4, 29),
    _RiTsDomainServerAddress_Type()
)
riTsDomainServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    riTsDomainServerAddress.setStatus("mandatory")
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
    (0, "INXNTS-MIB", "riBootIndex"),
)
if mibBuilder.loadTexts:
    riBootEntry.setStatus("mandatory")
_RiBootIndex_Type = Integer32
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
    (0, "INXNTS-MIB", "riThIndex"),
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


class _RiSystemRateInterval_Type(Integer32):
    """Custom type riSystemRateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_RiSystemRateInterval_Type.__name__ = "Integer32"
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
_RiInternext_ObjectIdentity = ObjectIdentity
riInternext = _RiInternext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28, 21)
)
_RiInxSlot_Type = Integer32
_RiInxSlot_Object = MibScalar
riInxSlot = _RiInxSlot_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 1),
    _RiInxSlot_Type()
)
riInxSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlot.setStatus("mandatory")


class _RiInxBus_Type(Integer32):
    """Custom type riInxBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bus-a", 2),
          ("bus-b", 3),
          ("none", 4))
    )


_RiInxBus_Type.__name__ = "Integer32"
_RiInxBus_Object = MibScalar
riInxBus = _RiInxBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 2),
    _RiInxBus_Type()
)
riInxBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxBus.setStatus("mandatory")
_RiInxSlotConnectivityType_Type = ObjectIdentifier
_RiInxSlotConnectivityType_Object = MibScalar
riInxSlotConnectivityType = _RiInxSlotConnectivityType_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 4),
    _RiInxSlotConnectivityType_Type()
)
riInxSlotConnectivityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivityType.setStatus("mandatory")
_RiInxSlotConnectivityRev_Type = DisplayString
_RiInxSlotConnectivityRev_Object = MibScalar
riInxSlotConnectivityRev = _RiInxSlotConnectivityRev_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 5),
    _RiInxSlotConnectivityRev_Type()
)
riInxSlotConnectivityRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivityRev.setStatus("mandatory")
_RiInxSlotConnectivitySerialNumber_Type = DisplayString
_RiInxSlotConnectivitySerialNumber_Object = MibScalar
riInxSlotConnectivitySerialNumber = _RiInxSlotConnectivitySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 6),
    _RiInxSlotConnectivitySerialNumber_Type()
)
riInxSlotConnectivitySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivitySerialNumber.setStatus("mandatory")


class _RiInxSlotConnectivityState_Type(Integer32):
    """Custom type riInxSlotConnectivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("enabled", 2)
    )


_RiInxSlotConnectivityState_Type.__name__ = "Integer32"
_RiInxSlotConnectivityState_Object = MibScalar
riInxSlotConnectivityState = _RiInxSlotConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 7),
    _RiInxSlotConnectivityState_Type()
)
riInxSlotConnectivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivityState.setStatus("mandatory")


class _RiInxSlotConnectivityBus_Type(Integer32):
    """Custom type riInxSlotConnectivityBus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("other", 3)
    )


_RiInxSlotConnectivityBus_Type.__name__ = "Integer32"
_RiInxSlotConnectivityBus_Object = MibScalar
riInxSlotConnectivityBus = _RiInxSlotConnectivityBus_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 8),
    _RiInxSlotConnectivityBus_Type()
)
riInxSlotConnectivityBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivityBus.setStatus("mandatory")


class _RiInxSlotConnectivityMedia_Type(Integer32):
    """Custom type riInxSlotConnectivityMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("other", 3)
    )


_RiInxSlotConnectivityMedia_Type.__name__ = "Integer32"
_RiInxSlotConnectivityMedia_Object = MibScalar
riInxSlotConnectivityMedia = _RiInxSlotConnectivityMedia_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 9),
    _RiInxSlotConnectivityMedia_Type()
)
riInxSlotConnectivityMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxSlotConnectivityMedia.setStatus("mandatory")
_RiInxChassisType_Type = ObjectIdentifier
_RiInxChassisType_Object = MibScalar
riInxChassisType = _RiInxChassisType_Object(
    (1, 3, 6, 1, 4, 1, 28, 21, 10),
    _RiInxChassisType_Type()
)
riInxChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    riInxChassisType.setStatus("mandatory")
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
    "INXNTS-MIB",
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
       "riProdNts": riProdNts,
       "riProdLdc": riProdLdc,
       "riLdcNts": riLdcNts,
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
       "tnOctetsReceived": tnOctetsReceived,
       "tnOctetsSent": tnOctetsSent,
       "tnNextType": tnNextType,
       "tnNextName": tnNextName,
       "riTs": riTs,
       "riTsPortCount": riTsPortCount,
       "riTsSignOn": riTsSignOn,
       "riTsPrompt": riTsPrompt,
       "riTsAdminPW": riTsAdminPW,
       "riTsDomainName": riTsDomainName,
       "riTsUpTimeNodeName": riTsUpTimeNodeName,
       "riTsNumBuffers": riTsNumBuffers,
       "riTsReadBufferSize": riTsReadBufferSize,
       "riTsWriteBufferSize": riTsWriteBufferSize,
       "riTsTcpWindowSize": riTsTcpWindowSize,
       "riTsTcpMaxSeg": riTsTcpMaxSeg,
       "riTsBreakChar": riTsBreakChar,
       "riTsFarMemoryFree": riTsFarMemoryFree,
       "riTsFarMemoryLowest": riTsFarMemoryLowest,
       "riTsTcpAckTimer": riTsTcpAckTimer,
       "riTsPortTable": riTsPortTable,
       "riTsPortEntry": riTsPortEntry,
       "riTsPortIndex": riTsPortIndex,
       "riTsPortFirstType": riTsPortFirstType,
       "riTsPortActiveType": riTsPortActiveType,
       "riTsPortNumSessions": riTsPortNumSessions,
       "riTsPortBaudIn": riTsPortBaudIn,
       "riTsPortBaudOut": riTsPortBaudOut,
       "riTsPortParity": riTsPortParity,
       "riTsPortDataBits": riTsPortDataBits,
       "riTsPortModemControl": riTsPortModemControl,
       "riTsPortFlowControlIn": riTsPortFlowControlIn,
       "riTsPortFlowControlOut": riTsPortFlowControlOut,
       "riTsPortRing": riTsPortRing,
       "riTsPortPassword": riTsPortPassword,
       "riTsPortAbortOut": riTsPortAbortOut,
       "riTsPortIntProc": riTsPortIntProc,
       "riTsPortInactiveTimeOut": riTsPortInactiveTimeOut,
       "riTsPortInactiveTimer": riTsPortInactiveTimer,
       "riTsPortMachineInterface": riTsPortMachineInterface,
       "riTsPortFunction": riTsPortFunction,
       "riTsPortState": riTsPortState,
       "riTsPortOctetsIn": riTsPortOctetsIn,
       "riTsPortOctetsOut": riTsPortOctetsOut,
       "riTsPortXONChar": riTsPortXONChar,
       "riTsPortXOFFChar": riTsPortXOFFChar,
       "riTsPortMaxSess": riTsPortMaxSess,
       "riTsPortServerPort": riTsPortServerPort,
       "riTsPortTCPMode": riTsPortTCPMode,
       "riTsPortDefXparent": riTsPortDefXparent,
       "riTsPortDefEcho": riTsPortDefEcho,
       "riTsDomainServerAddress": riTsDomainServerAddress,
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
       "riInternext": riInternext,
       "riInxSlot": riInxSlot,
       "riInxBus": riInxBus,
       "riInxSlotConnectivityType": riInxSlotConnectivityType,
       "riInxSlotConnectivityRev": riInxSlotConnectivityRev,
       "riInxSlotConnectivitySerialNumber": riInxSlotConnectivitySerialNumber,
       "riInxSlotConnectivityState": riInxSlotConnectivityState,
       "riInxSlotConnectivityBus": riInxSlotConnectivityBus,
       "riInxSlotConnectivityMedia": riInxSlotConnectivityMedia,
       "riInxChassisType": riInxChassisType,
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
