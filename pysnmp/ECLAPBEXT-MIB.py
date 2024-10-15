# SNMP MIB module (ECLAPBEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ECLAPBEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:27 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )





class BandwidthStatus(Integer32):
    """Custom type BandwidthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("rx-usage-high", 3),
          ("tx-and-rx-usage-high", 4),
          ("tx-usage-high", 2),
          ("undefined", 5))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Eicon_ObjectIdentity = ObjectIdentity
eicon = _Eicon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434)
)
_Management_ObjectIdentity = ObjectIdentity
management = _Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2)
)
_Mibv2_ObjectIdentity = ObjectIdentity
mibv2 = _Mibv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2)
)
_Module_ObjectIdentity = ObjectIdentity
module = _Module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4)
)
_Lapbext_ObjectIdentity = ObjectIdentity
lapbext = _Lapbext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1)
)
_LapbCountersTable_Object = MibTable
lapbCountersTable = _LapbCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lapbCountersTable.setStatus("mandatory")
_LapbCountEntry_Object = MibTableRow
lapbCountEntry = _LapbCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1)
)
lapbCountEntry.setIndexNames(
    (0, "ECLAPBEXT-MIB", "lapbCountPortRef"),
)
if mibBuilder.loadTexts:
    lapbCountEntry.setStatus("mandatory")
_LapbCountPortRef_Type = Integer32
_LapbCountPortRef_Object = MibTableColumn
lapbCountPortRef = _LapbCountPortRef_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 1),
    _LapbCountPortRef_Type()
)
lapbCountPortRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountPortRef.setStatus("mandatory")
_LapbCountRetransmis_Type = Counter32
_LapbCountRetransmis_Object = MibTableColumn
lapbCountRetransmis = _LapbCountRetransmis_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 2),
    _LapbCountRetransmis_Type()
)
lapbCountRetransmis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRetransmis.setStatus("mandatory")
_LapbCountSABMTxs_Type = Counter32
_LapbCountSABMTxs_Object = MibTableColumn
lapbCountSABMTxs = _LapbCountSABMTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 3),
    _LapbCountSABMTxs_Type()
)
lapbCountSABMTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountSABMTxs.setStatus("mandatory")
_LapbCountSABMRxs_Type = Counter32
_LapbCountSABMRxs_Object = MibTableColumn
lapbCountSABMRxs = _LapbCountSABMRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 4),
    _LapbCountSABMRxs_Type()
)
lapbCountSABMRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountSABMRxs.setStatus("mandatory")
_LapbCountDISCTxs_Type = Counter32
_LapbCountDISCTxs_Object = MibTableColumn
lapbCountDISCTxs = _LapbCountDISCTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 5),
    _LapbCountDISCTxs_Type()
)
lapbCountDISCTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountDISCTxs.setStatus("mandatory")
_LapbCountDISCRxs_Type = Counter32
_LapbCountDISCRxs_Object = MibTableColumn
lapbCountDISCRxs = _LapbCountDISCRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 6),
    _LapbCountDISCRxs_Type()
)
lapbCountDISCRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountDISCRxs.setStatus("mandatory")
_LapbCountDMsTxs_Type = Counter32
_LapbCountDMsTxs_Object = MibTableColumn
lapbCountDMsTxs = _LapbCountDMsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 7),
    _LapbCountDMsTxs_Type()
)
lapbCountDMsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountDMsTxs.setStatus("mandatory")
_LapbCountDMsRxs_Type = Counter32
_LapbCountDMsRxs_Object = MibTableColumn
lapbCountDMsRxs = _LapbCountDMsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 8),
    _LapbCountDMsRxs_Type()
)
lapbCountDMsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountDMsRxs.setStatus("mandatory")
_LapbCountRNRsTxs_Type = Counter32
_LapbCountRNRsTxs_Object = MibTableColumn
lapbCountRNRsTxs = _LapbCountRNRsTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 9),
    _LapbCountRNRsTxs_Type()
)
lapbCountRNRsTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRNRsTxs.setStatus("mandatory")
_LapbCountRNRsRxs_Type = Counter32
_LapbCountRNRsRxs_Object = MibTableColumn
lapbCountRNRsRxs = _LapbCountRNRsRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 10),
    _LapbCountRNRsRxs_Type()
)
lapbCountRNRsRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRNRsRxs.setStatus("mandatory")
_LapbCountUATxs_Type = Counter32
_LapbCountUATxs_Object = MibTableColumn
lapbCountUATxs = _LapbCountUATxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 11),
    _LapbCountUATxs_Type()
)
lapbCountUATxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountUATxs.setStatus("mandatory")
_LapbCountUARxs_Type = Counter32
_LapbCountUARxs_Object = MibTableColumn
lapbCountUARxs = _LapbCountUARxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 12),
    _LapbCountUARxs_Type()
)
lapbCountUARxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountUARxs.setStatus("mandatory")
_LapbCountRRTxs_Type = Counter32
_LapbCountRRTxs_Object = MibTableColumn
lapbCountRRTxs = _LapbCountRRTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 13),
    _LapbCountRRTxs_Type()
)
lapbCountRRTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRRTxs.setStatus("mandatory")
_LapbCountRRRxs_Type = Counter32
_LapbCountRRRxs_Object = MibTableColumn
lapbCountRRRxs = _LapbCountRRRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 14),
    _LapbCountRRRxs_Type()
)
lapbCountRRRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountRRRxs.setStatus("mandatory")
_LapbCountFRMRTxs_Type = Counter32
_LapbCountFRMRTxs_Object = MibTableColumn
lapbCountFRMRTxs = _LapbCountFRMRTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 15),
    _LapbCountFRMRTxs_Type()
)
lapbCountFRMRTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountFRMRTxs.setStatus("mandatory")
_LapbCountFRMRRxs_Type = Counter32
_LapbCountFRMRRxs_Object = MibTableColumn
lapbCountFRMRRxs = _LapbCountFRMRRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 16),
    _LapbCountFRMRRxs_Type()
)
lapbCountFRMRRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountFRMRRxs.setStatus("mandatory")
_LapbCountBadCRCTxs_Type = Counter32
_LapbCountBadCRCTxs_Object = MibTableColumn
lapbCountBadCRCTxs = _LapbCountBadCRCTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 17),
    _LapbCountBadCRCTxs_Type()
)
lapbCountBadCRCTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountBadCRCTxs.setStatus("mandatory")
_LapbCountBadCRCRxs_Type = Counter32
_LapbCountBadCRCRxs_Object = MibTableColumn
lapbCountBadCRCRxs = _LapbCountBadCRCRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 18),
    _LapbCountBadCRCRxs_Type()
)
lapbCountBadCRCRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountBadCRCRxs.setStatus("mandatory")
_LapbCountAbortTxs_Type = Counter32
_LapbCountAbortTxs_Object = MibTableColumn
lapbCountAbortTxs = _LapbCountAbortTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 19),
    _LapbCountAbortTxs_Type()
)
lapbCountAbortTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountAbortTxs.setStatus("mandatory")
_LapbCountAbortRxs_Type = Counter32
_LapbCountAbortRxs_Object = MibTableColumn
lapbCountAbortRxs = _LapbCountAbortRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 20),
    _LapbCountAbortRxs_Type()
)
lapbCountAbortRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountAbortRxs.setStatus("mandatory")
_LapbCountBadTypeTxs_Type = Counter32
_LapbCountBadTypeTxs_Object = MibTableColumn
lapbCountBadTypeTxs = _LapbCountBadTypeTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 21),
    _LapbCountBadTypeTxs_Type()
)
lapbCountBadTypeTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountBadTypeTxs.setStatus("mandatory")
_LapbCountBadTypeRxs_Type = Counter32
_LapbCountBadTypeRxs_Object = MibTableColumn
lapbCountBadTypeRxs = _LapbCountBadTypeRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 22),
    _LapbCountBadTypeRxs_Type()
)
lapbCountBadTypeRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountBadTypeRxs.setStatus("mandatory")
_LapbCountInfoFrameTxs_Type = Counter32
_LapbCountInfoFrameTxs_Object = MibTableColumn
lapbCountInfoFrameTxs = _LapbCountInfoFrameTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 23),
    _LapbCountInfoFrameTxs_Type()
)
lapbCountInfoFrameTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountInfoFrameTxs.setStatus("mandatory")
_LapbCountInfoFrameRxs_Type = Counter32
_LapbCountInfoFrameRxs_Object = MibTableColumn
lapbCountInfoFrameRxs = _LapbCountInfoFrameRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 24),
    _LapbCountInfoFrameRxs_Type()
)
lapbCountInfoFrameRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountInfoFrameRxs.setStatus("mandatory")
_LapbCountUnderrun_Type = Counter32
_LapbCountUnderrun_Object = MibTableColumn
lapbCountUnderrun = _LapbCountUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 25),
    _LapbCountUnderrun_Type()
)
lapbCountUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountUnderrun.setStatus("mandatory")
_LapbCountOverrun_Type = Counter32
_LapbCountOverrun_Object = MibTableColumn
lapbCountOverrun = _LapbCountOverrun_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 26),
    _LapbCountOverrun_Type()
)
lapbCountOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountOverrun.setStatus("mandatory")
_LapbCountXIDTxs_Type = Counter32
_LapbCountXIDTxs_Object = MibTableColumn
lapbCountXIDTxs = _LapbCountXIDTxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 27),
    _LapbCountXIDTxs_Type()
)
lapbCountXIDTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountXIDTxs.setStatus("mandatory")
_LapbCountXIDRxs_Type = Counter32
_LapbCountXIDRxs_Object = MibTableColumn
lapbCountXIDRxs = _LapbCountXIDRxs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 1, 1, 28),
    _LapbCountXIDRxs_Type()
)
lapbCountXIDRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbCountXIDRxs.setStatus("mandatory")
_LapbBandwidthTable_Object = MibTable
lapbBandwidthTable = _LapbBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lapbBandwidthTable.setStatus("mandatory")
_LapbBandwidthEntry_Object = MibTableRow
lapbBandwidthEntry = _LapbBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1)
)
lapbBandwidthEntry.setIndexNames(
    (0, "ECLAPBEXT-MIB", "lapbBandwidthIndex"),
)
if mibBuilder.loadTexts:
    lapbBandwidthEntry.setStatus("mandatory")


class _LapbBandwidthIndex_Type(Integer32):
    """Custom type lapbBandwidthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_LapbBandwidthIndex_Type.__name__ = "Integer32"
_LapbBandwidthIndex_Object = MibTableColumn
lapbBandwidthIndex = _LapbBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 1),
    _LapbBandwidthIndex_Type()
)
lapbBandwidthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbBandwidthIndex.setStatus("mandatory")


class _LapbBandwidthHigh_Type(Integer32):
    """Custom type lapbBandwidthHigh based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LapbBandwidthHigh_Type.__name__ = "Integer32"
_LapbBandwidthHigh_Object = MibTableColumn
lapbBandwidthHigh = _LapbBandwidthHigh_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 2),
    _LapbBandwidthHigh_Type()
)
lapbBandwidthHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbBandwidthHigh.setStatus("mandatory")


class _LapbBandwidthLow_Type(Integer32):
    """Custom type lapbBandwidthLow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LapbBandwidthLow_Type.__name__ = "Integer32"
_LapbBandwidthLow_Object = MibTableColumn
lapbBandwidthLow = _LapbBandwidthLow_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 3),
    _LapbBandwidthLow_Type()
)
lapbBandwidthLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbBandwidthLow.setStatus("mandatory")


class _LapbBandwidthSecs_Type(Integer32):
    """Custom type lapbBandwidthSecs based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_LapbBandwidthSecs_Type.__name__ = "Integer32"
_LapbBandwidthSecs_Object = MibTableColumn
lapbBandwidthSecs = _LapbBandwidthSecs_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 4),
    _LapbBandwidthSecs_Type()
)
lapbBandwidthSecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbBandwidthSecs.setStatus("mandatory")


class _LapbBandwidthNumPeriods_Type(Integer32):
    """Custom type lapbBandwidthNumPeriods based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LapbBandwidthNumPeriods_Type.__name__ = "Integer32"
_LapbBandwidthNumPeriods_Object = MibTableColumn
lapbBandwidthNumPeriods = _LapbBandwidthNumPeriods_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 5),
    _LapbBandwidthNumPeriods_Type()
)
lapbBandwidthNumPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbBandwidthNumPeriods.setStatus("mandatory")


class _LapbBandwidthTrapState_Type(Integer32):
    """Custom type lapbBandwidthTrapState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LapbBandwidthTrapState_Type.__name__ = "Integer32"
_LapbBandwidthTrapState_Object = MibTableColumn
lapbBandwidthTrapState = _LapbBandwidthTrapState_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 6),
    _LapbBandwidthTrapState_Type()
)
lapbBandwidthTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbBandwidthTrapState.setStatus("mandatory")
_LapbBandwidthTrapStatus_Type = BandwidthStatus
_LapbBandwidthTrapStatus_Object = MibTableColumn
lapbBandwidthTrapStatus = _LapbBandwidthTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 7),
    _LapbBandwidthTrapStatus_Type()
)
lapbBandwidthTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbBandwidthTrapStatus.setStatus("mandatory")


class _LapbBandwidthRxInUse_Type(Integer32):
    """Custom type lapbBandwidthRxInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LapbBandwidthRxInUse_Type.__name__ = "Integer32"
_LapbBandwidthRxInUse_Object = MibTableColumn
lapbBandwidthRxInUse = _LapbBandwidthRxInUse_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 8),
    _LapbBandwidthRxInUse_Type()
)
lapbBandwidthRxInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbBandwidthRxInUse.setStatus("mandatory")


class _LapbBandwidthTxInUse_Type(Integer32):
    """Custom type lapbBandwidthTxInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LapbBandwidthTxInUse_Type.__name__ = "Integer32"
_LapbBandwidthTxInUse_Object = MibTableColumn
lapbBandwidthTxInUse = _LapbBandwidthTxInUse_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 2, 1, 9),
    _LapbBandwidthTxInUse_Type()
)
lapbBandwidthTxInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbBandwidthTxInUse.setStatus("mandatory")
_LapbOperTable_Object = MibTable
lapbOperTable = _LapbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3)
)
if mibBuilder.loadTexts:
    lapbOperTable.setStatus("mandatory")
_LapbOperEntry_Object = MibTableRow
lapbOperEntry = _LapbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1)
)
lapbOperEntry.setIndexNames(
    (0, "ECLAPBEXT-MIB", "lapbOperIndex"),
)
if mibBuilder.loadTexts:
    lapbOperEntry.setStatus("mandatory")
_LapbOperIndex_Type = IfIndexType
_LapbOperIndex_Object = MibTableColumn
lapbOperIndex = _LapbOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 1),
    _LapbOperIndex_Type()
)
lapbOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperIndex.setStatus("mandatory")


class _LapbOperStationType_Type(Integer32):
    """Custom type lapbOperStationType based on Integer32"""
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
          ("dte", 1),
          ("dxe", 3))
    )


_LapbOperStationType_Type.__name__ = "Integer32"
_LapbOperStationType_Object = MibTableColumn
lapbOperStationType = _LapbOperStationType_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 2),
    _LapbOperStationType_Type()
)
lapbOperStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperStationType.setStatus("mandatory")


class _LapbOperControlField_Type(Integer32):
    """Custom type lapbOperControlField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_LapbOperControlField_Type.__name__ = "Integer32"
_LapbOperControlField_Object = MibTableColumn
lapbOperControlField = _LapbOperControlField_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 3),
    _LapbOperControlField_Type()
)
lapbOperControlField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperControlField.setStatus("mandatory")
_LapbOperTransmitN1FrameSize_Type = PositiveInteger
_LapbOperTransmitN1FrameSize_Object = MibTableColumn
lapbOperTransmitN1FrameSize = _LapbOperTransmitN1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 4),
    _LapbOperTransmitN1FrameSize_Type()
)
lapbOperTransmitN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperTransmitN1FrameSize.setStatus("mandatory")
_LapbOperReceiveN1FrameSize_Type = PositiveInteger
_LapbOperReceiveN1FrameSize_Object = MibTableColumn
lapbOperReceiveN1FrameSize = _LapbOperReceiveN1FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 5),
    _LapbOperReceiveN1FrameSize_Type()
)
lapbOperReceiveN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperReceiveN1FrameSize.setStatus("mandatory")


class _LapbOperTransmitKWindowSize_Type(Integer32):
    """Custom type lapbOperTransmitKWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbOperTransmitKWindowSize_Type.__name__ = "Integer32"
_LapbOperTransmitKWindowSize_Object = MibTableColumn
lapbOperTransmitKWindowSize = _LapbOperTransmitKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 6),
    _LapbOperTransmitKWindowSize_Type()
)
lapbOperTransmitKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperTransmitKWindowSize.setStatus("mandatory")


class _LapbOperReceiveKWindowSize_Type(Integer32):
    """Custom type lapbOperReceiveKWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbOperReceiveKWindowSize_Type.__name__ = "Integer32"
_LapbOperReceiveKWindowSize_Object = MibTableColumn
lapbOperReceiveKWindowSize = _LapbOperReceiveKWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 7),
    _LapbOperReceiveKWindowSize_Type()
)
lapbOperReceiveKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperReceiveKWindowSize.setStatus("mandatory")


class _LapbOperN2RxmitCount_Type(Integer32):
    """Custom type lapbOperN2RxmitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LapbOperN2RxmitCount_Type.__name__ = "Integer32"
_LapbOperN2RxmitCount_Object = MibTableColumn
lapbOperN2RxmitCount = _LapbOperN2RxmitCount_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 8),
    _LapbOperN2RxmitCount_Type()
)
lapbOperN2RxmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperN2RxmitCount.setStatus("mandatory")
_LapbOperT1AckTimer_Type = PositiveInteger
_LapbOperT1AckTimer_Object = MibTableColumn
lapbOperT1AckTimer = _LapbOperT1AckTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 9),
    _LapbOperT1AckTimer_Type()
)
lapbOperT1AckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT1AckTimer.setStatus("mandatory")
_LapbOperT2AckDelayTimer_Type = PositiveInteger
_LapbOperT2AckDelayTimer_Object = MibTableColumn
lapbOperT2AckDelayTimer = _LapbOperT2AckDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 10),
    _LapbOperT2AckDelayTimer_Type()
)
lapbOperT2AckDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT2AckDelayTimer.setStatus("mandatory")
_LapbOperT3DisconnectTimer_Type = PositiveInteger
_LapbOperT3DisconnectTimer_Object = MibTableColumn
lapbOperT3DisconnectTimer = _LapbOperT3DisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 11),
    _LapbOperT3DisconnectTimer_Type()
)
lapbOperT3DisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT3DisconnectTimer.setStatus("mandatory")
_LapbOperT4IdleTimer_Type = PositiveInteger
_LapbOperT4IdleTimer_Object = MibTableColumn
lapbOperT4IdleTimer = _LapbOperT4IdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 12),
    _LapbOperT4IdleTimer_Type()
)
lapbOperT4IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbOperT4IdleTimer.setStatus("mandatory")
_LapbOperPortId_Type = ObjectIdentifier
_LapbOperPortId_Object = MibTableColumn
lapbOperPortId = _LapbOperPortId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 13),
    _LapbOperPortId_Type()
)
lapbOperPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperPortId.setStatus("mandatory")
_LapbOperProtocolVersionId_Type = ObjectIdentifier
_LapbOperProtocolVersionId_Object = MibTableColumn
lapbOperProtocolVersionId = _LapbOperProtocolVersionId_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 3, 1, 14),
    _LapbOperProtocolVersionId_Type()
)
lapbOperProtocolVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperProtocolVersionId.setStatus("mandatory")
_LapbFlowTable_Object = MibTable
lapbFlowTable = _LapbFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    lapbFlowTable.setStatus("mandatory")
_LapbFlowEntry_Object = MibTableRow
lapbFlowEntry = _LapbFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1)
)
lapbFlowEntry.setIndexNames(
    (0, "ECLAPBEXT-MIB", "lapbFlowIfIndex"),
)
if mibBuilder.loadTexts:
    lapbFlowEntry.setStatus("mandatory")
_LapbFlowIfIndex_Type = IfIndexType
_LapbFlowIfIndex_Object = MibTableColumn
lapbFlowIfIndex = _LapbFlowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 1),
    _LapbFlowIfIndex_Type()
)
lapbFlowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowIfIndex.setStatus("mandatory")
_LapbFlowStateChanges_Type = Counter32
_LapbFlowStateChanges_Object = MibTableColumn
lapbFlowStateChanges = _LapbFlowStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 2),
    _LapbFlowStateChanges_Type()
)
lapbFlowStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowStateChanges.setStatus("mandatory")


class _LapbFlowChangeReason_Type(Integer32):
    """Custom type lapbFlowChangeReason based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmEntered", 2),
          ("abmReset", 4),
          ("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("frmrSent", 11),
          ("n2Timeout", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_LapbFlowChangeReason_Type.__name__ = "Integer32"
_LapbFlowChangeReason_Object = MibTableColumn
lapbFlowChangeReason = _LapbFlowChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 3),
    _LapbFlowChangeReason_Type()
)
lapbFlowChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowChangeReason.setStatus("mandatory")


class _LapbFlowCurrentMode_Type(Integer32):
    """Custom type lapbFlowCurrentMode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("bothStationsBusy", 10),
          ("disconnectRequest", 4),
          ("disconnected", 1),
          ("error", 16),
          ("frameReject", 3),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("other", 17),
          ("rejFrameSent", 6),
          ("rejFrameSentRemoteBusy", 14),
          ("remoteStationBusy", 9),
          ("stationBusy", 8),
          ("waitingAckBothBusy", 13),
          ("waitingAckRemoteBusy", 12),
          ("waitingAckStationBusy", 11),
          ("waitingAcknowledgement", 7),
          ("xidFrameSent", 15))
    )


_LapbFlowCurrentMode_Type.__name__ = "Integer32"
_LapbFlowCurrentMode_Object = MibTableColumn
lapbFlowCurrentMode = _LapbFlowCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 4),
    _LapbFlowCurrentMode_Type()
)
lapbFlowCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowCurrentMode.setStatus("mandatory")
_LapbFlowBusyDefers_Type = Counter32
_LapbFlowBusyDefers_Object = MibTableColumn
lapbFlowBusyDefers = _LapbFlowBusyDefers_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 5),
    _LapbFlowBusyDefers_Type()
)
lapbFlowBusyDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowBusyDefers.setStatus("mandatory")
_LapbFlowRejOutPkts_Type = Counter32
_LapbFlowRejOutPkts_Object = MibTableColumn
lapbFlowRejOutPkts = _LapbFlowRejOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 6),
    _LapbFlowRejOutPkts_Type()
)
lapbFlowRejOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowRejOutPkts.setStatus("mandatory")
_LapbFlowRejInPkts_Type = Counter32
_LapbFlowRejInPkts_Object = MibTableColumn
lapbFlowRejInPkts = _LapbFlowRejInPkts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 7),
    _LapbFlowRejInPkts_Type()
)
lapbFlowRejInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowRejInPkts.setStatus("mandatory")
_LapbFlowT1Timeouts_Type = Counter32
_LapbFlowT1Timeouts_Object = MibTableColumn
lapbFlowT1Timeouts = _LapbFlowT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 8),
    _LapbFlowT1Timeouts_Type()
)
lapbFlowT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowT1Timeouts.setStatus("mandatory")


class _LapbFlowFrmrSent_Type(OctetString):
    """Custom type lapbFlowFrmrSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LapbFlowFrmrSent_Type.__name__ = "OctetString"
_LapbFlowFrmrSent_Object = MibTableColumn
lapbFlowFrmrSent = _LapbFlowFrmrSent_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 9),
    _LapbFlowFrmrSent_Type()
)
lapbFlowFrmrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowFrmrSent.setStatus("mandatory")


class _LapbFlowFrmrReceived_Type(OctetString):
    """Custom type lapbFlowFrmrReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LapbFlowFrmrReceived_Type.__name__ = "OctetString"
_LapbFlowFrmrReceived_Object = MibTableColumn
lapbFlowFrmrReceived = _LapbFlowFrmrReceived_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 10),
    _LapbFlowFrmrReceived_Type()
)
lapbFlowFrmrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowFrmrReceived.setStatus("mandatory")


class _LapbFlowXidReceived_Type(OctetString):
    """Custom type lapbFlowXidReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8206),
    )


_LapbFlowXidReceived_Type.__name__ = "OctetString"
_LapbFlowXidReceived_Object = MibTableColumn
lapbFlowXidReceived = _LapbFlowXidReceived_Object(
    (1, 3, 6, 1, 4, 1, 434, 2, 2, 4, 1, 4, 1, 11),
    _LapbFlowXidReceived_Type()
)
lapbFlowXidReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowXidReceived.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lapbTrapBandwidthShortage = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 411)
)
lapbTrapBandwidthShortage.setObjects(
      *(("ECLAPBEXT-MIB", "lapbBandwidthIndex"),
        ("ECLAPBEXT-MIB", "lapbBandwidthRxInUse"),
        ("ECLAPBEXT-MIB", "lapbBandwidthTxInUse"),
        ("ECLAPBEXT-MIB", "lapbBandwidthTrapStatus"))
)
if mibBuilder.loadTexts:
    lapbTrapBandwidthShortage.setStatus(
        ""
    )

lapbTrapBandwidthClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 434, 0, 412)
)
lapbTrapBandwidthClear.setObjects(
      *(("ECLAPBEXT-MIB", "lapbBandwidthIndex"),
        ("ECLAPBEXT-MIB", "lapbBandwidthRxInUse"),
        ("ECLAPBEXT-MIB", "lapbBandwidthTxInUse"),
        ("ECLAPBEXT-MIB", "lapbBandwidthTrapStatus"))
)
if mibBuilder.loadTexts:
    lapbTrapBandwidthClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ECLAPBEXT-MIB",
    **{"PositiveInteger": PositiveInteger,
       "IfIndexType": IfIndexType,
       "BandwidthStatus": BandwidthStatus,
       "eicon": eicon,
       "lapbTrapBandwidthShortage": lapbTrapBandwidthShortage,
       "lapbTrapBandwidthClear": lapbTrapBandwidthClear,
       "management": management,
       "mibv2": mibv2,
       "module": module,
       "lapbext": lapbext,
       "lapbCountersTable": lapbCountersTable,
       "lapbCountEntry": lapbCountEntry,
       "lapbCountPortRef": lapbCountPortRef,
       "lapbCountRetransmis": lapbCountRetransmis,
       "lapbCountSABMTxs": lapbCountSABMTxs,
       "lapbCountSABMRxs": lapbCountSABMRxs,
       "lapbCountDISCTxs": lapbCountDISCTxs,
       "lapbCountDISCRxs": lapbCountDISCRxs,
       "lapbCountDMsTxs": lapbCountDMsTxs,
       "lapbCountDMsRxs": lapbCountDMsRxs,
       "lapbCountRNRsTxs": lapbCountRNRsTxs,
       "lapbCountRNRsRxs": lapbCountRNRsRxs,
       "lapbCountUATxs": lapbCountUATxs,
       "lapbCountUARxs": lapbCountUARxs,
       "lapbCountRRTxs": lapbCountRRTxs,
       "lapbCountRRRxs": lapbCountRRRxs,
       "lapbCountFRMRTxs": lapbCountFRMRTxs,
       "lapbCountFRMRRxs": lapbCountFRMRRxs,
       "lapbCountBadCRCTxs": lapbCountBadCRCTxs,
       "lapbCountBadCRCRxs": lapbCountBadCRCRxs,
       "lapbCountAbortTxs": lapbCountAbortTxs,
       "lapbCountAbortRxs": lapbCountAbortRxs,
       "lapbCountBadTypeTxs": lapbCountBadTypeTxs,
       "lapbCountBadTypeRxs": lapbCountBadTypeRxs,
       "lapbCountInfoFrameTxs": lapbCountInfoFrameTxs,
       "lapbCountInfoFrameRxs": lapbCountInfoFrameRxs,
       "lapbCountUnderrun": lapbCountUnderrun,
       "lapbCountOverrun": lapbCountOverrun,
       "lapbCountXIDTxs": lapbCountXIDTxs,
       "lapbCountXIDRxs": lapbCountXIDRxs,
       "lapbBandwidthTable": lapbBandwidthTable,
       "lapbBandwidthEntry": lapbBandwidthEntry,
       "lapbBandwidthIndex": lapbBandwidthIndex,
       "lapbBandwidthHigh": lapbBandwidthHigh,
       "lapbBandwidthLow": lapbBandwidthLow,
       "lapbBandwidthSecs": lapbBandwidthSecs,
       "lapbBandwidthNumPeriods": lapbBandwidthNumPeriods,
       "lapbBandwidthTrapState": lapbBandwidthTrapState,
       "lapbBandwidthTrapStatus": lapbBandwidthTrapStatus,
       "lapbBandwidthRxInUse": lapbBandwidthRxInUse,
       "lapbBandwidthTxInUse": lapbBandwidthTxInUse,
       "lapbOperTable": lapbOperTable,
       "lapbOperEntry": lapbOperEntry,
       "lapbOperIndex": lapbOperIndex,
       "lapbOperStationType": lapbOperStationType,
       "lapbOperControlField": lapbOperControlField,
       "lapbOperTransmitN1FrameSize": lapbOperTransmitN1FrameSize,
       "lapbOperReceiveN1FrameSize": lapbOperReceiveN1FrameSize,
       "lapbOperTransmitKWindowSize": lapbOperTransmitKWindowSize,
       "lapbOperReceiveKWindowSize": lapbOperReceiveKWindowSize,
       "lapbOperN2RxmitCount": lapbOperN2RxmitCount,
       "lapbOperT1AckTimer": lapbOperT1AckTimer,
       "lapbOperT2AckDelayTimer": lapbOperT2AckDelayTimer,
       "lapbOperT3DisconnectTimer": lapbOperT3DisconnectTimer,
       "lapbOperT4IdleTimer": lapbOperT4IdleTimer,
       "lapbOperPortId": lapbOperPortId,
       "lapbOperProtocolVersionId": lapbOperProtocolVersionId,
       "lapbFlowTable": lapbFlowTable,
       "lapbFlowEntry": lapbFlowEntry,
       "lapbFlowIfIndex": lapbFlowIfIndex,
       "lapbFlowStateChanges": lapbFlowStateChanges,
       "lapbFlowChangeReason": lapbFlowChangeReason,
       "lapbFlowCurrentMode": lapbFlowCurrentMode,
       "lapbFlowBusyDefers": lapbFlowBusyDefers,
       "lapbFlowRejOutPkts": lapbFlowRejOutPkts,
       "lapbFlowRejInPkts": lapbFlowRejInPkts,
       "lapbFlowT1Timeouts": lapbFlowT1Timeouts,
       "lapbFlowFrmrSent": lapbFlowFrmrSent,
       "lapbFlowFrmrReceived": lapbFlowFrmrReceived,
       "lapbFlowXidReceived": lapbFlowXidReceived}
)
