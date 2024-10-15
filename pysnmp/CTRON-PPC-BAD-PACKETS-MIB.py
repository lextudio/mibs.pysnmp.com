# SNMP MIB module (CTRON-PPC-BAD-PACKETS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-PPC-BAD-PACKETS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:07 2024
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

(ctFWDebug,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctFWDebug")

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

_CtPPCBadPkts_ObjectIdentity = ObjectIdentity
ctPPCBadPkts = _CtPPCBadPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1)
)
_CtPPCBadPktsTotalTx_Type = Integer32
_CtPPCBadPktsTotalTx_Object = MibScalar
ctPPCBadPktsTotalTx = _CtPPCBadPktsTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 1),
    _CtPPCBadPktsTotalTx_Type()
)
ctPPCBadPktsTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTotalTx.setStatus("mandatory")
_CtPPCBadPktsTotalRx_Type = Integer32
_CtPPCBadPktsTotalRx_Object = MibScalar
ctPPCBadPktsTotalRx = _CtPPCBadPktsTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 2),
    _CtPPCBadPktsTotalRx_Type()
)
ctPPCBadPktsTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTotalRx.setStatus("mandatory")
_CtPPCBadPktsTxTable_Object = MibTable
ctPPCBadPktsTxTable = _CtPPCBadPktsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    ctPPCBadPktsTxTable.setStatus("mandatory")
_CtPPCBadPktsTxEntry_Object = MibTableRow
ctPPCBadPktsTxEntry = _CtPPCBadPktsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1)
)
ctPPCBadPktsTxEntry.setIndexNames(
    (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxIndex"),
)
if mibBuilder.loadTexts:
    ctPPCBadPktsTxEntry.setStatus("mandatory")
_CtPPCBadPktsTxIndex_Type = Integer32
_CtPPCBadPktsTxIndex_Object = MibTableColumn
ctPPCBadPktsTxIndex = _CtPPCBadPktsTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 1),
    _CtPPCBadPktsTxIndex_Type()
)
ctPPCBadPktsTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTxIndex.setStatus("mandatory")
_CtPPCBadPktsTxQueues_Type = Integer32
_CtPPCBadPktsTxQueues_Object = MibTableColumn
ctPPCBadPktsTxQueues = _CtPPCBadPktsTxQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 2),
    _CtPPCBadPktsTxQueues_Type()
)
ctPPCBadPktsTxQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTxQueues.setStatus("mandatory")
_CtPPCBadPktsTxFulls_Type = Integer32
_CtPPCBadPktsTxFulls_Object = MibTableColumn
ctPPCBadPktsTxFulls = _CtPPCBadPktsTxFulls_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 3, 1, 3),
    _CtPPCBadPktsTxFulls_Type()
)
ctPPCBadPktsTxFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTxFulls.setStatus("mandatory")
_CtPPCBadPktsTxQDepthTable_Object = MibTable
ctPPCBadPktsTxQDepthTable = _CtPPCBadPktsTxQDepthTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    ctPPCBadPktsTxQDepthTable.setStatus("mandatory")
_CtPPCBadPktsTxQDepthEntry_Object = MibTableRow
ctPPCBadPktsTxQDepthEntry = _CtPPCBadPktsTxQDepthEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1)
)
ctPPCBadPktsTxQDepthEntry.setIndexNames(
    (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsTxQIndex"),
    (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsQ"),
)
if mibBuilder.loadTexts:
    ctPPCBadPktsTxQDepthEntry.setStatus("mandatory")
_CtPPCBadPktsTxQIndex_Type = Integer32
_CtPPCBadPktsTxQIndex_Object = MibTableColumn
ctPPCBadPktsTxQIndex = _CtPPCBadPktsTxQIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 1),
    _CtPPCBadPktsTxQIndex_Type()
)
ctPPCBadPktsTxQIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTxQIndex.setStatus("mandatory")


class _CtPPCBadPktsQ_Type(Integer32):
    """Custom type ctPPCBadPktsQ based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CtPPCBadPktsQ_Type.__name__ = "Integer32"
_CtPPCBadPktsQ_Object = MibTableColumn
ctPPCBadPktsQ = _CtPPCBadPktsQ_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 2),
    _CtPPCBadPktsQ_Type()
)
ctPPCBadPktsQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsQ.setStatus("mandatory")
_CtPPCBadPktsTxQDepth_Type = Integer32
_CtPPCBadPktsTxQDepth_Object = MibTableColumn
ctPPCBadPktsTxQDepth = _CtPPCBadPktsTxQDepth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 4, 1, 3),
    _CtPPCBadPktsTxQDepth_Type()
)
ctPPCBadPktsTxQDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsTxQDepth.setStatus("mandatory")
_CtPPCBadPktsRxTable_Object = MibTable
ctPPCBadPktsRxTable = _CtPPCBadPktsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    ctPPCBadPktsRxTable.setStatus("mandatory")
_CtPPCBadPktsRxEntry_Object = MibTableRow
ctPPCBadPktsRxEntry = _CtPPCBadPktsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1)
)
ctPPCBadPktsRxEntry.setIndexNames(
    (0, "CTRON-PPC-BAD-PACKETS-MIB", "ctPPCBadPktsRxIndex"),
)
if mibBuilder.loadTexts:
    ctPPCBadPktsRxEntry.setStatus("mandatory")
_CtPPCBadPktsRxIndex_Type = Integer32
_CtPPCBadPktsRxIndex_Object = MibTableColumn
ctPPCBadPktsRxIndex = _CtPPCBadPktsRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 1),
    _CtPPCBadPktsRxIndex_Type()
)
ctPPCBadPktsRxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxIndex.setStatus("mandatory")
_CtPPCBadPktsRxTotalErrors_Type = Integer32
_CtPPCBadPktsRxTotalErrors_Object = MibTableColumn
ctPPCBadPktsRxTotalErrors = _CtPPCBadPktsRxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 2),
    _CtPPCBadPktsRxTotalErrors_Type()
)
ctPPCBadPktsRxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxTotalErrors.setStatus("mandatory")
_CtPPCBadPktsRxDescHigh_Type = Integer32
_CtPPCBadPktsRxDescHigh_Object = MibTableColumn
ctPPCBadPktsRxDescHigh = _CtPPCBadPktsRxDescHigh_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 3),
    _CtPPCBadPktsRxDescHigh_Type()
)
ctPPCBadPktsRxDescHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxDescHigh.setStatus("mandatory")
_CtPPCBadPktsRxDescLow_Type = Integer32
_CtPPCBadPktsRxDescLow_Object = MibTableColumn
ctPPCBadPktsRxDescLow = _CtPPCBadPktsRxDescLow_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 4),
    _CtPPCBadPktsRxDescLow_Type()
)
ctPPCBadPktsRxDescLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxDescLow.setStatus("mandatory")
_CtPPCBadPktsRxDaSa0_Type = Integer32
_CtPPCBadPktsRxDaSa0_Object = MibTableColumn
ctPPCBadPktsRxDaSa0 = _CtPPCBadPktsRxDaSa0_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 5),
    _CtPPCBadPktsRxDaSa0_Type()
)
ctPPCBadPktsRxDaSa0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxDaSa0.setStatus("mandatory")
_CtPPCBadPktsRxDaSa1_Type = Integer32
_CtPPCBadPktsRxDaSa1_Object = MibTableColumn
ctPPCBadPktsRxDaSa1 = _CtPPCBadPktsRxDaSa1_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 6),
    _CtPPCBadPktsRxDaSa1_Type()
)
ctPPCBadPktsRxDaSa1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxDaSa1.setStatus("mandatory")
_CtPPCBadPktsRxDaSa2_Type = Integer32
_CtPPCBadPktsRxDaSa2_Object = MibTableColumn
ctPPCBadPktsRxDaSa2 = _CtPPCBadPktsRxDaSa2_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 7),
    _CtPPCBadPktsRxDaSa2_Type()
)
ctPPCBadPktsRxDaSa2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxDaSa2.setStatus("mandatory")
_CtPPCBadPktsRxData_Type = Integer32
_CtPPCBadPktsRxData_Object = MibTableColumn
ctPPCBadPktsRxData = _CtPPCBadPktsRxData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 29, 1, 5, 1, 8),
    _CtPPCBadPktsRxData_Type()
)
ctPPCBadPktsRxData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPPCBadPktsRxData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-PPC-BAD-PACKETS-MIB",
    **{"ctPPCBadPkts": ctPPCBadPkts,
       "ctPPCBadPktsTotalTx": ctPPCBadPktsTotalTx,
       "ctPPCBadPktsTotalRx": ctPPCBadPktsTotalRx,
       "ctPPCBadPktsTxTable": ctPPCBadPktsTxTable,
       "ctPPCBadPktsTxEntry": ctPPCBadPktsTxEntry,
       "ctPPCBadPktsTxIndex": ctPPCBadPktsTxIndex,
       "ctPPCBadPktsTxQueues": ctPPCBadPktsTxQueues,
       "ctPPCBadPktsTxFulls": ctPPCBadPktsTxFulls,
       "ctPPCBadPktsTxQDepthTable": ctPPCBadPktsTxQDepthTable,
       "ctPPCBadPktsTxQDepthEntry": ctPPCBadPktsTxQDepthEntry,
       "ctPPCBadPktsTxQIndex": ctPPCBadPktsTxQIndex,
       "ctPPCBadPktsQ": ctPPCBadPktsQ,
       "ctPPCBadPktsTxQDepth": ctPPCBadPktsTxQDepth,
       "ctPPCBadPktsRxTable": ctPPCBadPktsRxTable,
       "ctPPCBadPktsRxEntry": ctPPCBadPktsRxEntry,
       "ctPPCBadPktsRxIndex": ctPPCBadPktsRxIndex,
       "ctPPCBadPktsRxTotalErrors": ctPPCBadPktsRxTotalErrors,
       "ctPPCBadPktsRxDescHigh": ctPPCBadPktsRxDescHigh,
       "ctPPCBadPktsRxDescLow": ctPPCBadPktsRxDescLow,
       "ctPPCBadPktsRxDaSa0": ctPPCBadPktsRxDaSa0,
       "ctPPCBadPktsRxDaSa1": ctPPCBadPktsRxDaSa1,
       "ctPPCBadPktsRxDaSa2": ctPPCBadPktsRxDaSa2,
       "ctPPCBadPktsRxData": ctPPCBadPktsRxData}
)
