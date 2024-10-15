# SNMP MIB module (SOURCE-ROUTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SOURCE-ROUTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:16 2024
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

(dot1dBridge,
 dot1dSr) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBridge",
    "dot1dSr")

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

_Dot1dSrPortTable_Object = MibTable
dot1dSrPortTable = _Dot1dSrPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1)
)
if mibBuilder.loadTexts:
    dot1dSrPortTable.setStatus("mandatory")
_Dot1dSrPortEntry_Object = MibTableRow
dot1dSrPortEntry = _Dot1dSrPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1)
)
dot1dSrPortEntry.setIndexNames(
    (0, "SOURCE-ROUTING-MIB", "dot1dSrPort"),
)
if mibBuilder.loadTexts:
    dot1dSrPortEntry.setStatus("mandatory")


class _Dot1dSrPort_Type(Integer32):
    """Custom type dot1dSrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dSrPort_Type.__name__ = "Integer32"
_Dot1dSrPort_Object = MibTableColumn
dot1dSrPort = _Dot1dSrPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 1),
    _Dot1dSrPort_Type()
)
dot1dSrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPort.setStatus("mandatory")
_Dot1dSrPortHopCount_Type = Integer32
_Dot1dSrPortHopCount_Object = MibTableColumn
dot1dSrPortHopCount = _Dot1dSrPortHopCount_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 2),
    _Dot1dSrPortHopCount_Type()
)
dot1dSrPortHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortHopCount.setStatus("mandatory")
_Dot1dSrPortLocalSegment_Type = Integer32
_Dot1dSrPortLocalSegment_Object = MibTableColumn
dot1dSrPortLocalSegment = _Dot1dSrPortLocalSegment_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 3),
    _Dot1dSrPortLocalSegment_Type()
)
dot1dSrPortLocalSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortLocalSegment.setStatus("mandatory")
_Dot1dSrPortBridgeNum_Type = Integer32
_Dot1dSrPortBridgeNum_Object = MibTableColumn
dot1dSrPortBridgeNum = _Dot1dSrPortBridgeNum_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 4),
    _Dot1dSrPortBridgeNum_Type()
)
dot1dSrPortBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortBridgeNum.setStatus("mandatory")
_Dot1dSrPortTargetSegment_Type = Integer32
_Dot1dSrPortTargetSegment_Object = MibTableColumn
dot1dSrPortTargetSegment = _Dot1dSrPortTargetSegment_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 5),
    _Dot1dSrPortTargetSegment_Type()
)
dot1dSrPortTargetSegment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortTargetSegment.setStatus("mandatory")
_Dot1dSrPortLargestFrame_Type = Integer32
_Dot1dSrPortLargestFrame_Object = MibTableColumn
dot1dSrPortLargestFrame = _Dot1dSrPortLargestFrame_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 6),
    _Dot1dSrPortLargestFrame_Type()
)
dot1dSrPortLargestFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortLargestFrame.setStatus("mandatory")


class _Dot1dSrPortSTESpanMode_Type(Integer32):
    """Custom type dot1dSrPortSTESpanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-span", 1),
          ("disabled", 2),
          ("forced", 3))
    )


_Dot1dSrPortSTESpanMode_Type.__name__ = "Integer32"
_Dot1dSrPortSTESpanMode_Object = MibTableColumn
dot1dSrPortSTESpanMode = _Dot1dSrPortSTESpanMode_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 7),
    _Dot1dSrPortSTESpanMode_Type()
)
dot1dSrPortSTESpanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrPortSTESpanMode.setStatus("mandatory")
_Dot1dSrPortSpecInFrames_Type = Counter32
_Dot1dSrPortSpecInFrames_Object = MibTableColumn
dot1dSrPortSpecInFrames = _Dot1dSrPortSpecInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 8),
    _Dot1dSrPortSpecInFrames_Type()
)
dot1dSrPortSpecInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSpecInFrames.setStatus("mandatory")
_Dot1dSrPortSpecOutFrames_Type = Counter32
_Dot1dSrPortSpecOutFrames_Object = MibTableColumn
dot1dSrPortSpecOutFrames = _Dot1dSrPortSpecOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 9),
    _Dot1dSrPortSpecOutFrames_Type()
)
dot1dSrPortSpecOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSpecOutFrames.setStatus("mandatory")
_Dot1dSrPortApeInFrames_Type = Counter32
_Dot1dSrPortApeInFrames_Object = MibTableColumn
dot1dSrPortApeInFrames = _Dot1dSrPortApeInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 10),
    _Dot1dSrPortApeInFrames_Type()
)
dot1dSrPortApeInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortApeInFrames.setStatus("mandatory")
_Dot1dSrPortApeOutFrames_Type = Counter32
_Dot1dSrPortApeOutFrames_Object = MibTableColumn
dot1dSrPortApeOutFrames = _Dot1dSrPortApeOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 11),
    _Dot1dSrPortApeOutFrames_Type()
)
dot1dSrPortApeOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortApeOutFrames.setStatus("mandatory")
_Dot1dSrPortSteInFrames_Type = Counter32
_Dot1dSrPortSteInFrames_Object = MibTableColumn
dot1dSrPortSteInFrames = _Dot1dSrPortSteInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 12),
    _Dot1dSrPortSteInFrames_Type()
)
dot1dSrPortSteInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSteInFrames.setStatus("mandatory")
_Dot1dSrPortSteOutFrames_Type = Counter32
_Dot1dSrPortSteOutFrames_Object = MibTableColumn
dot1dSrPortSteOutFrames = _Dot1dSrPortSteOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 13),
    _Dot1dSrPortSteOutFrames_Type()
)
dot1dSrPortSteOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSteOutFrames.setStatus("mandatory")
_Dot1dSrPortSegmentMismatchDiscards_Type = Counter32
_Dot1dSrPortSegmentMismatchDiscards_Object = MibTableColumn
dot1dSrPortSegmentMismatchDiscards = _Dot1dSrPortSegmentMismatchDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 14),
    _Dot1dSrPortSegmentMismatchDiscards_Type()
)
dot1dSrPortSegmentMismatchDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortSegmentMismatchDiscards.setStatus("mandatory")
_Dot1dSrPortDuplicateSegmentDiscards_Type = Counter32
_Dot1dSrPortDuplicateSegmentDiscards_Object = MibTableColumn
dot1dSrPortDuplicateSegmentDiscards = _Dot1dSrPortDuplicateSegmentDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 15),
    _Dot1dSrPortDuplicateSegmentDiscards_Type()
)
dot1dSrPortDuplicateSegmentDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortDuplicateSegmentDiscards.setStatus("mandatory")
_Dot1dSrPortHopCountExceededDiscards_Type = Counter32
_Dot1dSrPortHopCountExceededDiscards_Object = MibTableColumn
dot1dSrPortHopCountExceededDiscards = _Dot1dSrPortHopCountExceededDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 16),
    _Dot1dSrPortHopCountExceededDiscards_Type()
)
dot1dSrPortHopCountExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortHopCountExceededDiscards.setStatus("mandatory")
_Dot1dSrPortDupLanIdOrTreeErrors_Type = Counter32
_Dot1dSrPortDupLanIdOrTreeErrors_Object = MibTableColumn
dot1dSrPortDupLanIdOrTreeErrors = _Dot1dSrPortDupLanIdOrTreeErrors_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 17),
    _Dot1dSrPortDupLanIdOrTreeErrors_Type()
)
dot1dSrPortDupLanIdOrTreeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortDupLanIdOrTreeErrors.setStatus("mandatory")
_Dot1dSrPortLanIdMismatches_Type = Counter32
_Dot1dSrPortLanIdMismatches_Object = MibTableColumn
dot1dSrPortLanIdMismatches = _Dot1dSrPortLanIdMismatches_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 1, 1, 18),
    _Dot1dSrPortLanIdMismatches_Type()
)
dot1dSrPortLanIdMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dSrPortLanIdMismatches.setStatus("mandatory")


class _Dot1dSrBridgeLfMode_Type(Integer32):
    """Custom type dot1dSrBridgeLfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode3", 1),
          ("mode6", 2))
    )


_Dot1dSrBridgeLfMode_Type.__name__ = "Integer32"
_Dot1dSrBridgeLfMode_Object = MibScalar
dot1dSrBridgeLfMode = _Dot1dSrBridgeLfMode_Object(
    (1, 3, 6, 1, 2, 1, 17, 3, 2),
    _Dot1dSrBridgeLfMode_Type()
)
dot1dSrBridgeLfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dSrBridgeLfMode.setStatus("mandatory")
_Dot1dPortPair_ObjectIdentity = ObjectIdentity
dot1dPortPair = _Dot1dPortPair_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 10)
)
_Dot1dPortPairTableSize_Type = Gauge32
_Dot1dPortPairTableSize_Object = MibScalar
dot1dPortPairTableSize = _Dot1dPortPairTableSize_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 1),
    _Dot1dPortPairTableSize_Type()
)
dot1dPortPairTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1dPortPairTableSize.setStatus("mandatory")
_Dot1dPortPairTable_Object = MibTable
dot1dPortPairTable = _Dot1dPortPairTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2)
)
if mibBuilder.loadTexts:
    dot1dPortPairTable.setStatus("mandatory")
_Dot1dPortPairEntry_Object = MibTableRow
dot1dPortPairEntry = _Dot1dPortPairEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2, 1)
)
dot1dPortPairEntry.setIndexNames(
    (0, "SOURCE-ROUTING-MIB", "dot1dPortPairLowPort"),
    (0, "SOURCE-ROUTING-MIB", "dot1dPortPairHighPort"),
)
if mibBuilder.loadTexts:
    dot1dPortPairEntry.setStatus("mandatory")


class _Dot1dPortPairLowPort_Type(Integer32):
    """Custom type dot1dPortPairLowPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dPortPairLowPort_Type.__name__ = "Integer32"
_Dot1dPortPairLowPort_Object = MibTableColumn
dot1dPortPairLowPort = _Dot1dPortPairLowPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2, 1, 1),
    _Dot1dPortPairLowPort_Type()
)
dot1dPortPairLowPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortPairLowPort.setStatus("mandatory")


class _Dot1dPortPairHighPort_Type(Integer32):
    """Custom type dot1dPortPairHighPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1dPortPairHighPort_Type.__name__ = "Integer32"
_Dot1dPortPairHighPort_Object = MibTableColumn
dot1dPortPairHighPort = _Dot1dPortPairHighPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2, 1, 2),
    _Dot1dPortPairHighPort_Type()
)
dot1dPortPairHighPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortPairHighPort.setStatus("mandatory")
_Dot1dPortPairBridgeNum_Type = Integer32
_Dot1dPortPairBridgeNum_Object = MibTableColumn
dot1dPortPairBridgeNum = _Dot1dPortPairBridgeNum_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2, 1, 3),
    _Dot1dPortPairBridgeNum_Type()
)
dot1dPortPairBridgeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortPairBridgeNum.setStatus("mandatory")


class _Dot1dPortPairBridgeState_Type(Integer32):
    """Custom type dot1dPortPairBridgeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("invalid", 3))
    )


_Dot1dPortPairBridgeState_Type.__name__ = "Integer32"
_Dot1dPortPairBridgeState_Object = MibTableColumn
dot1dPortPairBridgeState = _Dot1dPortPairBridgeState_Object(
    (1, 3, 6, 1, 2, 1, 17, 10, 2, 1, 4),
    _Dot1dPortPairBridgeState_Type()
)
dot1dPortPairBridgeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1dPortPairBridgeState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SOURCE-ROUTING-MIB",
    **{"dot1dSrPortTable": dot1dSrPortTable,
       "dot1dSrPortEntry": dot1dSrPortEntry,
       "dot1dSrPort": dot1dSrPort,
       "dot1dSrPortHopCount": dot1dSrPortHopCount,
       "dot1dSrPortLocalSegment": dot1dSrPortLocalSegment,
       "dot1dSrPortBridgeNum": dot1dSrPortBridgeNum,
       "dot1dSrPortTargetSegment": dot1dSrPortTargetSegment,
       "dot1dSrPortLargestFrame": dot1dSrPortLargestFrame,
       "dot1dSrPortSTESpanMode": dot1dSrPortSTESpanMode,
       "dot1dSrPortSpecInFrames": dot1dSrPortSpecInFrames,
       "dot1dSrPortSpecOutFrames": dot1dSrPortSpecOutFrames,
       "dot1dSrPortApeInFrames": dot1dSrPortApeInFrames,
       "dot1dSrPortApeOutFrames": dot1dSrPortApeOutFrames,
       "dot1dSrPortSteInFrames": dot1dSrPortSteInFrames,
       "dot1dSrPortSteOutFrames": dot1dSrPortSteOutFrames,
       "dot1dSrPortSegmentMismatchDiscards": dot1dSrPortSegmentMismatchDiscards,
       "dot1dSrPortDuplicateSegmentDiscards": dot1dSrPortDuplicateSegmentDiscards,
       "dot1dSrPortHopCountExceededDiscards": dot1dSrPortHopCountExceededDiscards,
       "dot1dSrPortDupLanIdOrTreeErrors": dot1dSrPortDupLanIdOrTreeErrors,
       "dot1dSrPortLanIdMismatches": dot1dSrPortLanIdMismatches,
       "dot1dSrBridgeLfMode": dot1dSrBridgeLfMode,
       "dot1dPortPair": dot1dPortPair,
       "dot1dPortPairTableSize": dot1dPortPairTableSize,
       "dot1dPortPairTable": dot1dPortPairTable,
       "dot1dPortPairEntry": dot1dPortPairEntry,
       "dot1dPortPairLowPort": dot1dPortPairLowPort,
       "dot1dPortPairHighPort": dot1dPortPairHighPort,
       "dot1dPortPairBridgeNum": dot1dPortPairBridgeNum,
       "dot1dPortPairBridgeState": dot1dPortPairBridgeState}
)
