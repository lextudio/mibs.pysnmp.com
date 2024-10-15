# SNMP MIB module (CXPCM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXPCM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:45 2024
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

(SapIndex,
 cxPCM) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "SapIndex",
    "cxPCM")

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



class ChannelIndex(Integer32):
    """Custom type ChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PcmSapTable_Object = MibTable
pcmSapTable = _PcmSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40)
)
if mibBuilder.loadTexts:
    pcmSapTable.setStatus("mandatory")
_PcmSapEntry_Object = MibTableRow
pcmSapEntry = _PcmSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1)
)
pcmSapEntry.setIndexNames(
    (0, "CXPCM-MIB", "pcmSapLinkNumber"),
    (0, "CXPCM-MIB", "pcmSapChannelNumber"),
)
if mibBuilder.loadTexts:
    pcmSapEntry.setStatus("mandatory")
_PcmSapLinkNumber_Type = SapIndex
_PcmSapLinkNumber_Object = MibTableColumn
pcmSapLinkNumber = _PcmSapLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 1),
    _PcmSapLinkNumber_Type()
)
pcmSapLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapLinkNumber.setStatus("mandatory")
_PcmSapChannelNumber_Type = ChannelIndex
_PcmSapChannelNumber_Object = MibTableColumn
pcmSapChannelNumber = _PcmSapChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 2),
    _PcmSapChannelNumber_Type()
)
pcmSapChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapChannelNumber.setStatus("mandatory")


class _PcmSapChannelState_Type(Integer32):
    """Custom type pcmSapChannelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_PcmSapChannelState_Type.__name__ = "Integer32"
_PcmSapChannelState_Object = MibTableColumn
pcmSapChannelState = _PcmSapChannelState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 40),
    _PcmSapChannelState_Type()
)
pcmSapChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapChannelState.setStatus("mandatory")
_PcmSapRxPacket_Type = Counter32
_PcmSapRxPacket_Object = MibTableColumn
pcmSapRxPacket = _PcmSapRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 60),
    _PcmSapRxPacket_Type()
)
pcmSapRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapRxPacket.setStatus("mandatory")
_PcmSapTxPacket_Type = Counter32
_PcmSapTxPacket_Object = MibTableColumn
pcmSapTxPacket = _PcmSapTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 61),
    _PcmSapTxPacket_Type()
)
pcmSapTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapTxPacket.setStatus("mandatory")
_PcmSapTxDesync_Type = Counter32
_PcmSapTxDesync_Object = MibTableColumn
pcmSapTxDesync = _PcmSapTxDesync_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 62),
    _PcmSapTxDesync_Type()
)
pcmSapTxDesync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapTxDesync.setStatus("mandatory")
_PcmSapTxNotReady_Type = Counter32
_PcmSapTxNotReady_Object = MibTableColumn
pcmSapTxNotReady = _PcmSapTxNotReady_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 63),
    _PcmSapTxNotReady_Type()
)
pcmSapTxNotReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapTxNotReady.setStatus("mandatory")
_PcmSapRxBusy_Type = Counter32
_PcmSapRxBusy_Object = MibTableColumn
pcmSapRxBusy = _PcmSapRxBusy_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 64),
    _PcmSapRxBusy_Type()
)
pcmSapRxBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapRxBusy.setStatus("mandatory")
_PcmSapTxUnderrun_Type = Counter32
_PcmSapTxUnderrun_Object = MibTableColumn
pcmSapTxUnderrun = _PcmSapTxUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 40, 1, 65),
    _PcmSapTxUnderrun_Type()
)
pcmSapTxUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmSapTxUnderrun.setStatus("mandatory")
_PcmDebugTable_Object = MibTable
pcmDebugTable = _PcmDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 60)
)
if mibBuilder.loadTexts:
    pcmDebugTable.setStatus("mandatory")
_PcmDebugEntry_Object = MibTableRow
pcmDebugEntry = _PcmDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 60, 1)
)
pcmDebugEntry.setIndexNames(
    (0, "CXPCM-MIB", "pcmDebugLinkNumber"),
)
if mibBuilder.loadTexts:
    pcmDebugEntry.setStatus("mandatory")
_PcmDebugLinkNumber_Type = SapIndex
_PcmDebugLinkNumber_Object = MibTableColumn
pcmDebugLinkNumber = _PcmDebugLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 60, 1, 1),
    _PcmDebugLinkNumber_Type()
)
pcmDebugLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcmDebugLinkNumber.setStatus("mandatory")
_PcmDebugLoopInfo_Type = Integer32
_PcmDebugLoopInfo_Object = MibTableColumn
pcmDebugLoopInfo = _PcmDebugLoopInfo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 63, 60, 1, 80),
    _PcmDebugLoopInfo_Type()
)
pcmDebugLoopInfo.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pcmDebugLoopInfo.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXPCM-MIB",
    **{"ChannelIndex": ChannelIndex,
       "pcmSapTable": pcmSapTable,
       "pcmSapEntry": pcmSapEntry,
       "pcmSapLinkNumber": pcmSapLinkNumber,
       "pcmSapChannelNumber": pcmSapChannelNumber,
       "pcmSapChannelState": pcmSapChannelState,
       "pcmSapRxPacket": pcmSapRxPacket,
       "pcmSapTxPacket": pcmSapTxPacket,
       "pcmSapTxDesync": pcmSapTxDesync,
       "pcmSapTxNotReady": pcmSapTxNotReady,
       "pcmSapRxBusy": pcmSapRxBusy,
       "pcmSapTxUnderrun": pcmSapTxUnderrun,
       "pcmDebugTable": pcmDebugTable,
       "pcmDebugEntry": pcmDebugEntry,
       "pcmDebugLinkNumber": pcmDebugLinkNumber,
       "pcmDebugLoopInfo": pcmDebugLoopInfo}
)
