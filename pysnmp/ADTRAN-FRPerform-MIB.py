# SNMP MIB module (ADTRAN-FRPerform-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-FRPerform-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:32 2024
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

(adMgmt,
 adProdPhysAddress,
 adProducts,
 adtran) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adMgmt",
    "adProdPhysAddress",
    "adProducts",
    "adtran")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdPerform_ObjectIdentity = ObjectIdentity
adPerform = _AdPerform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4)
)
_AdFRPerformmg_ObjectIdentity = ObjectIdentity
adFRPerformmg = _AdFRPerformmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1)
)
_AdFRPerformHistoryControl_ObjectIdentity = ObjectIdentity
adFRPerformHistoryControl = _AdFRPerformHistoryControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 1)
)


class _AdFRPerformHistoryIntLength_Type(Integer32):
    """Custom type adFRPerformHistoryIntLength based on Integer32"""
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
        *(("min10", 2),
          ("min15", 3),
          ("min20", 4),
          ("min30", 5),
          ("min5", 1))
    )


_AdFRPerformHistoryIntLength_Type.__name__ = "Integer32"
_AdFRPerformHistoryIntLength_Object = MibScalar
adFRPerformHistoryIntLength = _AdFRPerformHistoryIntLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 1, 1),
    _AdFRPerformHistoryIntLength_Type()
)
adFRPerformHistoryIntLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adFRPerformHistoryIntLength.setStatus("mandatory")


class _AdFRPerformCurrentIntTimeRemaining_Type(Integer32):
    """Custom type adFRPerformCurrentIntTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_AdFRPerformCurrentIntTimeRemaining_Type.__name__ = "Integer32"
_AdFRPerformCurrentIntTimeRemaining_Object = MibScalar
adFRPerformCurrentIntTimeRemaining = _AdFRPerformCurrentIntTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 1, 2),
    _AdFRPerformCurrentIntTimeRemaining_Type()
)
adFRPerformCurrentIntTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCurrentIntTimeRemaining.setStatus("mandatory")
_AdFRPerformCompletedInts_Type = Integer32
_AdFRPerformCompletedInts_Object = MibScalar
adFRPerformCompletedInts = _AdFRPerformCompletedInts_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 1, 3),
    _AdFRPerformCompletedInts_Type()
)
adFRPerformCompletedInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCompletedInts.setStatus("mandatory")
_AdFRPerformCompletedDays_Type = Integer32
_AdFRPerformCompletedDays_Object = MibScalar
adFRPerformCompletedDays = _AdFRPerformCompletedDays_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 1, 4),
    _AdFRPerformCompletedDays_Type()
)
adFRPerformCompletedDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCompletedDays.setStatus("mandatory")
_AdFRPerformCurrentPvcStatus_ObjectIdentity = ObjectIdentity
adFRPerformCurrentPvcStatus = _AdFRPerformCurrentPvcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2)
)
_AdFRPerformCurrentPvcStatusTable_Object = MibTable
adFRPerformCurrentPvcStatusTable = _AdFRPerformCurrentPvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcStatusTable.setStatus("mandatory")
_AdFRPerformCurrentPvcStatusEntry_Object = MibTableRow
adFRPerformCurrentPvcStatusEntry = _AdFRPerformCurrentPvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1, 1)
)
adFRPerformCurrentPvcStatusEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformCurrentPvcIfIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformCurrentPvcStatusIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcStatusEntry.setStatus("mandatory")
_AdFRPerformCurrentPvcIfIndex_Type = Integer32
_AdFRPerformCurrentPvcIfIndex_Object = MibTableColumn
adFRPerformCurrentPvcIfIndex = _AdFRPerformCurrentPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1, 1, 1),
    _AdFRPerformCurrentPvcIfIndex_Type()
)
adFRPerformCurrentPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcIfIndex.setStatus("mandatory")
_AdFRPerformCurrentPvcStatusIndex_Type = Integer32
_AdFRPerformCurrentPvcStatusIndex_Object = MibTableColumn
adFRPerformCurrentPvcStatusIndex = _AdFRPerformCurrentPvcStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1, 1, 2),
    _AdFRPerformCurrentPvcStatusIndex_Type()
)
adFRPerformCurrentPvcStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcStatusIndex.setStatus("mandatory")


class _AdFRPerformCurrentPvcState_Type(Integer32):
    """Custom type adFRPerformCurrentPvcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("unknown", 3))
    )


_AdFRPerformCurrentPvcState_Type.__name__ = "Integer32"
_AdFRPerformCurrentPvcState_Object = MibTableColumn
adFRPerformCurrentPvcState = _AdFRPerformCurrentPvcState_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1, 1, 3),
    _AdFRPerformCurrentPvcState_Type()
)
adFRPerformCurrentPvcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcState.setStatus("mandatory")


class _AdFRPerformCurrentPvcStatistics_Type(Integer32):
    """Custom type adFRPerformCurrentPvcStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("not-available", 2))
    )


_AdFRPerformCurrentPvcStatistics_Type.__name__ = "Integer32"
_AdFRPerformCurrentPvcStatistics_Object = MibTableColumn
adFRPerformCurrentPvcStatistics = _AdFRPerformCurrentPvcStatistics_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 2, 1, 1, 4),
    _AdFRPerformCurrentPvcStatistics_Type()
)
adFRPerformCurrentPvcStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformCurrentPvcStatistics.setStatus("mandatory")
_AdFRPerformIntPvcStatus_ObjectIdentity = ObjectIdentity
adFRPerformIntPvcStatus = _AdFRPerformIntPvcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3)
)
_AdFRPerformIntPvcStatusTable_Object = MibTable
adFRPerformIntPvcStatusTable = _AdFRPerformIntPvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adFRPerformIntPvcStatusTable.setStatus("mandatory")
_AdFRPerformIntPvcStatusEntry_Object = MibTableRow
adFRPerformIntPvcStatusEntry = _AdFRPerformIntPvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1)
)
adFRPerformIntPvcStatusEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPvcIfIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPvcIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPvcSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformIntPvcStatusEntry.setStatus("mandatory")
_AdFRPerformIntPvcIfIndex_Type = Integer32
_AdFRPerformIntPvcIfIndex_Object = MibTableColumn
adFRPerformIntPvcIfIndex = _AdFRPerformIntPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 1),
    _AdFRPerformIntPvcIfIndex_Type()
)
adFRPerformIntPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPvcIfIndex.setStatus("mandatory")
_AdFRPerformIntPvcIndex_Type = Integer32
_AdFRPerformIntPvcIndex_Object = MibTableColumn
adFRPerformIntPvcIndex = _AdFRPerformIntPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 2),
    _AdFRPerformIntPvcIndex_Type()
)
adFRPerformIntPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPvcIndex.setStatus("mandatory")
_AdFRPerformIntPvcSlotIndex_Type = Integer32
_AdFRPerformIntPvcSlotIndex_Object = MibTableColumn
adFRPerformIntPvcSlotIndex = _AdFRPerformIntPvcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 3),
    _AdFRPerformIntPvcSlotIndex_Type()
)
adFRPerformIntPvcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPvcSlotIndex.setStatus("mandatory")
_AdFRPerformIntPVCStateChange_Type = Counter32
_AdFRPerformIntPVCStateChange_Object = MibTableColumn
adFRPerformIntPVCStateChange = _AdFRPerformIntPVCStateChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 4),
    _AdFRPerformIntPVCStateChange_Type()
)
adFRPerformIntPVCStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCStateChange.setStatus("mandatory")
_AdFRPerformIntPVCInactiveTime_Type = Counter32
_AdFRPerformIntPVCInactiveTime_Object = MibTableColumn
adFRPerformIntPVCInactiveTime = _AdFRPerformIntPVCInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 5),
    _AdFRPerformIntPVCInactiveTime_Type()
)
adFRPerformIntPVCInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCInactiveTime.setStatus("mandatory")
_AdFRPerformIntPVCFramesRx_Type = Counter32
_AdFRPerformIntPVCFramesRx_Object = MibTableColumn
adFRPerformIntPVCFramesRx = _AdFRPerformIntPVCFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 6),
    _AdFRPerformIntPVCFramesRx_Type()
)
adFRPerformIntPVCFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCFramesRx.setStatus("mandatory")
_AdFRPerformIntPVCFramesTx_Type = Counter32
_AdFRPerformIntPVCFramesTx_Object = MibTableColumn
adFRPerformIntPVCFramesTx = _AdFRPerformIntPVCFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 7),
    _AdFRPerformIntPVCFramesTx_Type()
)
adFRPerformIntPVCFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCFramesTx.setStatus("mandatory")
_AdFRPerformIntPVCBytesRx_Type = Counter32
_AdFRPerformIntPVCBytesRx_Object = MibTableColumn
adFRPerformIntPVCBytesRx = _AdFRPerformIntPVCBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 8),
    _AdFRPerformIntPVCBytesRx_Type()
)
adFRPerformIntPVCBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBytesRx.setStatus("mandatory")
_AdFRPerformIntPVCBytesTx_Type = Counter32
_AdFRPerformIntPVCBytesTx_Object = MibTableColumn
adFRPerformIntPVCBytesTx = _AdFRPerformIntPVCBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 9),
    _AdFRPerformIntPVCBytesTx_Type()
)
adFRPerformIntPVCBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBytesTx.setStatus("mandatory")
_AdFRPerformIntPVCAvgThruputTx_Type = Gauge32
_AdFRPerformIntPVCAvgThruputTx_Object = MibTableColumn
adFRPerformIntPVCAvgThruputTx = _AdFRPerformIntPVCAvgThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 10),
    _AdFRPerformIntPVCAvgThruputTx_Type()
)
adFRPerformIntPVCAvgThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgThruputTx.setStatus("mandatory")
_AdFRPerformIntPVCAvgThruputRx_Type = Gauge32
_AdFRPerformIntPVCAvgThruputRx_Object = MibTableColumn
adFRPerformIntPVCAvgThruputRx = _AdFRPerformIntPVCAvgThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 11),
    _AdFRPerformIntPVCAvgThruputRx_Type()
)
adFRPerformIntPVCAvgThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgThruputRx.setStatus("mandatory")
_AdFRPerformIntPVCMaxThruputTx_Type = Counter32
_AdFRPerformIntPVCMaxThruputTx_Object = MibTableColumn
adFRPerformIntPVCMaxThruputTx = _AdFRPerformIntPVCMaxThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 12),
    _AdFRPerformIntPVCMaxThruputTx_Type()
)
adFRPerformIntPVCMaxThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxThruputTx.setStatus("mandatory")
_AdFRPerformIntPVCMaxThruputRx_Type = Counter32
_AdFRPerformIntPVCMaxThruputRx_Object = MibTableColumn
adFRPerformIntPVCMaxThruputRx = _AdFRPerformIntPVCMaxThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 13),
    _AdFRPerformIntPVCMaxThruputRx_Type()
)
adFRPerformIntPVCMaxThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxThruputRx.setStatus("mandatory")
_AdFRPerformIntPVCAvgUtilizationTx_Type = Gauge32
_AdFRPerformIntPVCAvgUtilizationTx_Object = MibTableColumn
adFRPerformIntPVCAvgUtilizationTx = _AdFRPerformIntPVCAvgUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 14),
    _AdFRPerformIntPVCAvgUtilizationTx_Type()
)
adFRPerformIntPVCAvgUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgUtilizationTx.setStatus("mandatory")
_AdFRPerformIntPVCAvgUtilizationRx_Type = Gauge32
_AdFRPerformIntPVCAvgUtilizationRx_Object = MibTableColumn
adFRPerformIntPVCAvgUtilizationRx = _AdFRPerformIntPVCAvgUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 15),
    _AdFRPerformIntPVCAvgUtilizationRx_Type()
)
adFRPerformIntPVCAvgUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgUtilizationRx.setStatus("mandatory")
_AdFRPerformIntPVCMaxUtilizationTx_Type = Counter32
_AdFRPerformIntPVCMaxUtilizationTx_Object = MibTableColumn
adFRPerformIntPVCMaxUtilizationTx = _AdFRPerformIntPVCMaxUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 16),
    _AdFRPerformIntPVCMaxUtilizationTx_Type()
)
adFRPerformIntPVCMaxUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxUtilizationTx.setStatus("mandatory")
_AdFRPerformIntPVCMaxUtilizationRx_Type = Counter32
_AdFRPerformIntPVCMaxUtilizationRx_Object = MibTableColumn
adFRPerformIntPVCMaxUtilizationRx = _AdFRPerformIntPVCMaxUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 17),
    _AdFRPerformIntPVCMaxUtilizationRx_Type()
)
adFRPerformIntPVCMaxUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxUtilizationRx.setStatus("mandatory")
_AdFRPerformIntPVCBurstTx_Type = Counter32
_AdFRPerformIntPVCBurstTx_Object = MibTableColumn
adFRPerformIntPVCBurstTx = _AdFRPerformIntPVCBurstTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 18),
    _AdFRPerformIntPVCBurstTx_Type()
)
adFRPerformIntPVCBurstTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBurstTx.setStatus("mandatory")
_AdFRPerformIntPVCBurstRx_Type = Counter32
_AdFRPerformIntPVCBurstRx_Object = MibTableColumn
adFRPerformIntPVCBurstRx = _AdFRPerformIntPVCBurstRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 19),
    _AdFRPerformIntPVCBurstRx_Type()
)
adFRPerformIntPVCBurstRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBurstRx.setStatus("mandatory")
_AdFRPerformIntPVCFecnRx_Type = Counter32
_AdFRPerformIntPVCFecnRx_Object = MibTableColumn
adFRPerformIntPVCFecnRx = _AdFRPerformIntPVCFecnRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 20),
    _AdFRPerformIntPVCFecnRx_Type()
)
adFRPerformIntPVCFecnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCFecnRx.setStatus("mandatory")
_AdFRPerformIntPVCFecnTx_Type = Counter32
_AdFRPerformIntPVCFecnTx_Object = MibTableColumn
adFRPerformIntPVCFecnTx = _AdFRPerformIntPVCFecnTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 21),
    _AdFRPerformIntPVCFecnTx_Type()
)
adFRPerformIntPVCFecnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCFecnTx.setStatus("mandatory")
_AdFRPerformIntPVCBecnRx_Type = Counter32
_AdFRPerformIntPVCBecnRx_Object = MibTableColumn
adFRPerformIntPVCBecnRx = _AdFRPerformIntPVCBecnRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 22),
    _AdFRPerformIntPVCBecnRx_Type()
)
adFRPerformIntPVCBecnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBecnRx.setStatus("mandatory")
_AdFRPerformIntPVCBecnTx_Type = Counter32
_AdFRPerformIntPVCBecnTx_Object = MibTableColumn
adFRPerformIntPVCBecnTx = _AdFRPerformIntPVCBecnTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 23),
    _AdFRPerformIntPVCBecnTx_Type()
)
adFRPerformIntPVCBecnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCBecnTx.setStatus("mandatory")
_AdFRPerformIntPVCDeRx_Type = Counter32
_AdFRPerformIntPVCDeRx_Object = MibTableColumn
adFRPerformIntPVCDeRx = _AdFRPerformIntPVCDeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 24),
    _AdFRPerformIntPVCDeRx_Type()
)
adFRPerformIntPVCDeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCDeRx.setStatus("mandatory")
_AdFRPerformIntPVCDeTx_Type = Counter32
_AdFRPerformIntPVCDeTx_Object = MibTableColumn
adFRPerformIntPVCDeTx = _AdFRPerformIntPVCDeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 25),
    _AdFRPerformIntPVCDeTx_Type()
)
adFRPerformIntPVCDeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCDeTx.setStatus("mandatory")
_AdFRPerformIntPVCCrRx_Type = Counter32
_AdFRPerformIntPVCCrRx_Object = MibTableColumn
adFRPerformIntPVCCrRx = _AdFRPerformIntPVCCrRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 26),
    _AdFRPerformIntPVCCrRx_Type()
)
adFRPerformIntPVCCrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCCrRx.setStatus("mandatory")
_AdFRPerformIntPVCCrTx_Type = Counter32
_AdFRPerformIntPVCCrTx_Object = MibTableColumn
adFRPerformIntPVCCrTx = _AdFRPerformIntPVCCrTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 27),
    _AdFRPerformIntPVCCrTx_Type()
)
adFRPerformIntPVCCrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCCrTx.setStatus("mandatory")
_AdFRPerformIntPVCMinFrameSizeRx_Type = Counter32
_AdFRPerformIntPVCMinFrameSizeRx_Object = MibTableColumn
adFRPerformIntPVCMinFrameSizeRx = _AdFRPerformIntPVCMinFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 28),
    _AdFRPerformIntPVCMinFrameSizeRx_Type()
)
adFRPerformIntPVCMinFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMinFrameSizeRx.setStatus("mandatory")
_AdFRPerformIntPVCMinFrameSizeTx_Type = Counter32
_AdFRPerformIntPVCMinFrameSizeTx_Object = MibTableColumn
adFRPerformIntPVCMinFrameSizeTx = _AdFRPerformIntPVCMinFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 29),
    _AdFRPerformIntPVCMinFrameSizeTx_Type()
)
adFRPerformIntPVCMinFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMinFrameSizeTx.setStatus("mandatory")
_AdFRPerformIntPVCMaxFrameSizeRx_Type = Counter32
_AdFRPerformIntPVCMaxFrameSizeRx_Object = MibTableColumn
adFRPerformIntPVCMaxFrameSizeRx = _AdFRPerformIntPVCMaxFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 30),
    _AdFRPerformIntPVCMaxFrameSizeRx_Type()
)
adFRPerformIntPVCMaxFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxFrameSizeRx.setStatus("mandatory")
_AdFRPerformIntPVCMaxFrameSizeTx_Type = Counter32
_AdFRPerformIntPVCMaxFrameSizeTx_Object = MibTableColumn
adFRPerformIntPVCMaxFrameSizeTx = _AdFRPerformIntPVCMaxFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 31),
    _AdFRPerformIntPVCMaxFrameSizeTx_Type()
)
adFRPerformIntPVCMaxFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxFrameSizeTx.setStatus("mandatory")
_AdFRPerformIntPVCAvgFrameSizeRx_Type = Gauge32
_AdFRPerformIntPVCAvgFrameSizeRx_Object = MibTableColumn
adFRPerformIntPVCAvgFrameSizeRx = _AdFRPerformIntPVCAvgFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 32),
    _AdFRPerformIntPVCAvgFrameSizeRx_Type()
)
adFRPerformIntPVCAvgFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgFrameSizeRx.setStatus("mandatory")
_AdFRPerformIntPVCAvgFrameSizeTx_Type = Gauge32
_AdFRPerformIntPVCAvgFrameSizeTx_Object = MibTableColumn
adFRPerformIntPVCAvgFrameSizeTx = _AdFRPerformIntPVCAvgFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 33),
    _AdFRPerformIntPVCAvgFrameSizeTx_Type()
)
adFRPerformIntPVCAvgFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgFrameSizeTx.setStatus("mandatory")
_AdFRPerformIntPVCLostFrames_Type = Counter32
_AdFRPerformIntPVCLostFrames_Object = MibTableColumn
adFRPerformIntPVCLostFrames = _AdFRPerformIntPVCLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 34),
    _AdFRPerformIntPVCLostFrames_Type()
)
adFRPerformIntPVCLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCLostFrames.setStatus("mandatory")
_AdFRPerformIntPVCRemoteLostFrames_Type = Counter32
_AdFRPerformIntPVCRemoteLostFrames_Object = MibTableColumn
adFRPerformIntPVCRemoteLostFrames = _AdFRPerformIntPVCRemoteLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 35),
    _AdFRPerformIntPVCRemoteLostFrames_Type()
)
adFRPerformIntPVCRemoteLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCRemoteLostFrames.setStatus("mandatory")
_AdFRPerformIntPVCMaxDelay_Type = Gauge32
_AdFRPerformIntPVCMaxDelay_Object = MibTableColumn
adFRPerformIntPVCMaxDelay = _AdFRPerformIntPVCMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 36),
    _AdFRPerformIntPVCMaxDelay_Type()
)
adFRPerformIntPVCMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMaxDelay.setStatus("mandatory")
_AdFRPerformIntPVCMinDelay_Type = Gauge32
_AdFRPerformIntPVCMinDelay_Object = MibTableColumn
adFRPerformIntPVCMinDelay = _AdFRPerformIntPVCMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 37),
    _AdFRPerformIntPVCMinDelay_Type()
)
adFRPerformIntPVCMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCMinDelay.setStatus("mandatory")
_AdFRPerformIntPVCAvgDelay_Type = Gauge32
_AdFRPerformIntPVCAvgDelay_Object = MibTableColumn
adFRPerformIntPVCAvgDelay = _AdFRPerformIntPVCAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 38),
    _AdFRPerformIntPVCAvgDelay_Type()
)
adFRPerformIntPVCAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCAvgDelay.setStatus("mandatory")
_AdFRPerformIntPVCTimeInDBU_Type = Counter32
_AdFRPerformIntPVCTimeInDBU_Object = MibTableColumn
adFRPerformIntPVCTimeInDBU = _AdFRPerformIntPVCTimeInDBU_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 3, 1, 1, 39),
    _AdFRPerformIntPVCTimeInDBU_Type()
)
adFRPerformIntPVCTimeInDBU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPVCTimeInDBU.setStatus("mandatory")
_AdFRPerformIntPortStatus_ObjectIdentity = ObjectIdentity
adFRPerformIntPortStatus = _AdFRPerformIntPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4)
)
_AdFRPerformIntPortStatusTable_Object = MibTable
adFRPerformIntPortStatusTable = _AdFRPerformIntPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adFRPerformIntPortStatusTable.setStatus("mandatory")
_AdFRPerformIntPortStatusEntry_Object = MibTableRow
adFRPerformIntPortStatusEntry = _AdFRPerformIntPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1)
)
adFRPerformIntPortStatusEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntIfIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPortSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformIntPortStatusEntry.setStatus("mandatory")
_AdFRPerformIntIfIndex_Type = Integer32
_AdFRPerformIntIfIndex_Object = MibTableColumn
adFRPerformIntIfIndex = _AdFRPerformIntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 1),
    _AdFRPerformIntIfIndex_Type()
)
adFRPerformIntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntIfIndex.setStatus("mandatory")
_AdFRPerformIntPortSlotIndex_Type = Integer32
_AdFRPerformIntPortSlotIndex_Object = MibTableColumn
adFRPerformIntPortSlotIndex = _AdFRPerformIntPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 2),
    _AdFRPerformIntPortSlotIndex_Type()
)
adFRPerformIntPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortSlotIndex.setStatus("mandatory")
_AdFRPerformIntPortFramesRx_Type = Counter32
_AdFRPerformIntPortFramesRx_Object = MibTableColumn
adFRPerformIntPortFramesRx = _AdFRPerformIntPortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 3),
    _AdFRPerformIntPortFramesRx_Type()
)
adFRPerformIntPortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortFramesRx.setStatus("mandatory")
_AdFRPerformIntPortFramesTx_Type = Counter32
_AdFRPerformIntPortFramesTx_Object = MibTableColumn
adFRPerformIntPortFramesTx = _AdFRPerformIntPortFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 4),
    _AdFRPerformIntPortFramesTx_Type()
)
adFRPerformIntPortFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortFramesTx.setStatus("mandatory")
_AdFRPerformIntPortBytesRx_Type = Counter32
_AdFRPerformIntPortBytesRx_Object = MibTableColumn
adFRPerformIntPortBytesRx = _AdFRPerformIntPortBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 5),
    _AdFRPerformIntPortBytesRx_Type()
)
adFRPerformIntPortBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortBytesRx.setStatus("mandatory")
_AdFRPerformIntPortBytesTx_Type = Counter32
_AdFRPerformIntPortBytesTx_Object = MibTableColumn
adFRPerformIntPortBytesTx = _AdFRPerformIntPortBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 6),
    _AdFRPerformIntPortBytesTx_Type()
)
adFRPerformIntPortBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortBytesTx.setStatus("mandatory")
_AdFRPerformIntPortAvgThruputTx_Type = Gauge32
_AdFRPerformIntPortAvgThruputTx_Object = MibTableColumn
adFRPerformIntPortAvgThruputTx = _AdFRPerformIntPortAvgThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 7),
    _AdFRPerformIntPortAvgThruputTx_Type()
)
adFRPerformIntPortAvgThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortAvgThruputTx.setStatus("mandatory")
_AdFRPerformIntPortAvgThruputRx_Type = Gauge32
_AdFRPerformIntPortAvgThruputRx_Object = MibTableColumn
adFRPerformIntPortAvgThruputRx = _AdFRPerformIntPortAvgThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 8),
    _AdFRPerformIntPortAvgThruputRx_Type()
)
adFRPerformIntPortAvgThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortAvgThruputRx.setStatus("mandatory")
_AdFRPerformIntPortMaxThruputTx_Type = Counter32
_AdFRPerformIntPortMaxThruputTx_Object = MibTableColumn
adFRPerformIntPortMaxThruputTx = _AdFRPerformIntPortMaxThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 9),
    _AdFRPerformIntPortMaxThruputTx_Type()
)
adFRPerformIntPortMaxThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortMaxThruputTx.setStatus("mandatory")
_AdFRPerformIntPortMaxThruputRx_Type = Counter32
_AdFRPerformIntPortMaxThruputRx_Object = MibTableColumn
adFRPerformIntPortMaxThruputRx = _AdFRPerformIntPortMaxThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 10),
    _AdFRPerformIntPortMaxThruputRx_Type()
)
adFRPerformIntPortMaxThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortMaxThruputRx.setStatus("mandatory")
_AdFRPerformIntPortAvgUtilizationTx_Type = Gauge32
_AdFRPerformIntPortAvgUtilizationTx_Object = MibTableColumn
adFRPerformIntPortAvgUtilizationTx = _AdFRPerformIntPortAvgUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 11),
    _AdFRPerformIntPortAvgUtilizationTx_Type()
)
adFRPerformIntPortAvgUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortAvgUtilizationTx.setStatus("mandatory")
_AdFRPerformIntPortAvgUtilizationRx_Type = Gauge32
_AdFRPerformIntPortAvgUtilizationRx_Object = MibTableColumn
adFRPerformIntPortAvgUtilizationRx = _AdFRPerformIntPortAvgUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 12),
    _AdFRPerformIntPortAvgUtilizationRx_Type()
)
adFRPerformIntPortAvgUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortAvgUtilizationRx.setStatus("mandatory")
_AdFRPerformIntPortMaxUtilizationTx_Type = Counter32
_AdFRPerformIntPortMaxUtilizationTx_Object = MibTableColumn
adFRPerformIntPortMaxUtilizationTx = _AdFRPerformIntPortMaxUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 13),
    _AdFRPerformIntPortMaxUtilizationTx_Type()
)
adFRPerformIntPortMaxUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortMaxUtilizationTx.setStatus("mandatory")
_AdFRPerformIntPortMaxUtilizationRx_Type = Counter32
_AdFRPerformIntPortMaxUtilizationRx_Object = MibTableColumn
adFRPerformIntPortMaxUtilizationRx = _AdFRPerformIntPortMaxUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 14),
    _AdFRPerformIntPortMaxUtilizationRx_Type()
)
adFRPerformIntPortMaxUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortMaxUtilizationRx.setStatus("mandatory")
_AdFRPerformIntPortFullStatusRX_Type = Counter32
_AdFRPerformIntPortFullStatusRX_Object = MibTableColumn
adFRPerformIntPortFullStatusRX = _AdFRPerformIntPortFullStatusRX_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 15),
    _AdFRPerformIntPortFullStatusRX_Type()
)
adFRPerformIntPortFullStatusRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortFullStatusRX.setStatus("mandatory")
_AdFRPerformIntPortFullStatusTx_Type = Counter32
_AdFRPerformIntPortFullStatusTx_Object = MibTableColumn
adFRPerformIntPortFullStatusTx = _AdFRPerformIntPortFullStatusTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 16),
    _AdFRPerformIntPortFullStatusTx_Type()
)
adFRPerformIntPortFullStatusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortFullStatusTx.setStatus("mandatory")
_AdFRPerformIntPortLIOnlyRX_Type = Counter32
_AdFRPerformIntPortLIOnlyRX_Object = MibTableColumn
adFRPerformIntPortLIOnlyRX = _AdFRPerformIntPortLIOnlyRX_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 17),
    _AdFRPerformIntPortLIOnlyRX_Type()
)
adFRPerformIntPortLIOnlyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortLIOnlyRX.setStatus("mandatory")
_AdFRPerformIntPortLIOnlyTx_Type = Counter32
_AdFRPerformIntPortLIOnlyTx_Object = MibTableColumn
adFRPerformIntPortLIOnlyTx = _AdFRPerformIntPortLIOnlyTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 18),
    _AdFRPerformIntPortLIOnlyTx_Type()
)
adFRPerformIntPortLIOnlyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortLIOnlyTx.setStatus("mandatory")
_AdFRPerformIntPortAsyncStatusFrame_Type = Counter32
_AdFRPerformIntPortAsyncStatusFrame_Object = MibTableColumn
adFRPerformIntPortAsyncStatusFrame = _AdFRPerformIntPortAsyncStatusFrame_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 4, 1, 1, 19),
    _AdFRPerformIntPortAsyncStatusFrame_Type()
)
adFRPerformIntPortAsyncStatusFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortAsyncStatusFrame.setStatus("mandatory")
_AdFRPerformIntPortError_ObjectIdentity = ObjectIdentity
adFRPerformIntPortError = _AdFRPerformIntPortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5)
)
_AdFRPerformIntPortErrorTable_Object = MibTable
adFRPerformIntPortErrorTable = _AdFRPerformIntPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1)
)
if mibBuilder.loadTexts:
    adFRPerformIntPortErrorTable.setStatus("mandatory")
_AdFRPerformIntPortErrorEntry_Object = MibTableRow
adFRPerformIntPortErrorEntry = _AdFRPerformIntPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1)
)
adFRPerformIntPortErrorEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPortIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntPortErrorSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformIntPortErrorEntry.setStatus("mandatory")
_AdFRPerformIntPortIndex_Type = Integer32
_AdFRPerformIntPortIndex_Object = MibTableColumn
adFRPerformIntPortIndex = _AdFRPerformIntPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 1),
    _AdFRPerformIntPortIndex_Type()
)
adFRPerformIntPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortIndex.setStatus("mandatory")
_AdFRPerformIntPortErrorSlotIndex_Type = Integer32
_AdFRPerformIntPortErrorSlotIndex_Object = MibTableColumn
adFRPerformIntPortErrorSlotIndex = _AdFRPerformIntPortErrorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 2),
    _AdFRPerformIntPortErrorSlotIndex_Type()
)
adFRPerformIntPortErrorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortErrorSlotIndex.setStatus("mandatory")
_AdFRPerformIntPortUnavailableTime_Type = Counter32
_AdFRPerformIntPortUnavailableTime_Object = MibTableColumn
adFRPerformIntPortUnavailableTime = _AdFRPerformIntPortUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 3),
    _AdFRPerformIntPortUnavailableTime_Type()
)
adFRPerformIntPortUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntPortUnavailableTime.setStatus("mandatory")
_AdFRPerformIntCrcErrors_Type = Counter32
_AdFRPerformIntCrcErrors_Object = MibTableColumn
adFRPerformIntCrcErrors = _AdFRPerformIntCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 4),
    _AdFRPerformIntCrcErrors_Type()
)
adFRPerformIntCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntCrcErrors.setStatus("mandatory")
_AdFRPerformIntAbortFrames_Type = Counter32
_AdFRPerformIntAbortFrames_Object = MibTableColumn
adFRPerformIntAbortFrames = _AdFRPerformIntAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 5),
    _AdFRPerformIntAbortFrames_Type()
)
adFRPerformIntAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntAbortFrames.setStatus("mandatory")
_AdFRPerformIntOctectViolations_Type = Counter32
_AdFRPerformIntOctectViolations_Object = MibTableColumn
adFRPerformIntOctectViolations = _AdFRPerformIntOctectViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 6),
    _AdFRPerformIntOctectViolations_Type()
)
adFRPerformIntOctectViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntOctectViolations.setStatus("mandatory")
_AdFRPerformIntDiscardFrames_Type = Counter32
_AdFRPerformIntDiscardFrames_Object = MibTableColumn
adFRPerformIntDiscardFrames = _AdFRPerformIntDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 7),
    _AdFRPerformIntDiscardFrames_Type()
)
adFRPerformIntDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntDiscardFrames.setStatus("mandatory")
_AdFRPerformIntLengthErrors_Type = Counter32
_AdFRPerformIntLengthErrors_Object = MibTableColumn
adFRPerformIntLengthErrors = _AdFRPerformIntLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 8),
    _AdFRPerformIntLengthErrors_Type()
)
adFRPerformIntLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntLengthErrors.setStatus("mandatory")
_AdFRPerformIntEAViolations_Type = Counter32
_AdFRPerformIntEAViolations_Object = MibTableColumn
adFRPerformIntEAViolations = _AdFRPerformIntEAViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 9),
    _AdFRPerformIntEAViolations_Type()
)
adFRPerformIntEAViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntEAViolations.setStatus("mandatory")
_AdFRPerformIntEncapsulationErrors_Type = Counter32
_AdFRPerformIntEncapsulationErrors_Object = MibTableColumn
adFRPerformIntEncapsulationErrors = _AdFRPerformIntEncapsulationErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 10),
    _AdFRPerformIntEncapsulationErrors_Type()
)
adFRPerformIntEncapsulationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntEncapsulationErrors.setStatus("mandatory")
_AdFRPerformIntInactiveDLCI_Type = Counter32
_AdFRPerformIntInactiveDLCI_Object = MibTableColumn
adFRPerformIntInactiveDLCI = _AdFRPerformIntInactiveDLCI_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 11),
    _AdFRPerformIntInactiveDLCI_Type()
)
adFRPerformIntInactiveDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntInactiveDLCI.setStatus("mandatory")
_AdFRPerformIntInvalidDLCI_Type = Counter32
_AdFRPerformIntInvalidDLCI_Object = MibTableColumn
adFRPerformIntInvalidDLCI = _AdFRPerformIntInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 12),
    _AdFRPerformIntInvalidDLCI_Type()
)
adFRPerformIntInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntInvalidDLCI.setStatus("mandatory")
_AdFRPerformIntUnroutable_Type = Counter32
_AdFRPerformIntUnroutable_Object = MibTableColumn
adFRPerformIntUnroutable = _AdFRPerformIntUnroutable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 13),
    _AdFRPerformIntUnroutable_Type()
)
adFRPerformIntUnroutable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntUnroutable.setStatus("mandatory")
_AdFRPerformIntSignalDownTime_Type = Counter32
_AdFRPerformIntSignalDownTime_Object = MibTableColumn
adFRPerformIntSignalDownTime = _AdFRPerformIntSignalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 14),
    _AdFRPerformIntSignalDownTime_Type()
)
adFRPerformIntSignalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntSignalDownTime.setStatus("mandatory")
_AdFRPerformIntSignalErrors_Type = Counter32
_AdFRPerformIntSignalErrors_Object = MibTableColumn
adFRPerformIntSignalErrors = _AdFRPerformIntSignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 15),
    _AdFRPerformIntSignalErrors_Type()
)
adFRPerformIntSignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntSignalErrors.setStatus("mandatory")
_AdFRPerformIntSignalTimeOut_Type = Counter32
_AdFRPerformIntSignalTimeOut_Object = MibTableColumn
adFRPerformIntSignalTimeOut = _AdFRPerformIntSignalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 16),
    _AdFRPerformIntSignalTimeOut_Type()
)
adFRPerformIntSignalTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntSignalTimeOut.setStatus("mandatory")
_AdFRPerformIntSignalStateChange_Type = Counter32
_AdFRPerformIntSignalStateChange_Object = MibTableColumn
adFRPerformIntSignalStateChange = _AdFRPerformIntSignalStateChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 5, 1, 1, 17),
    _AdFRPerformIntSignalStateChange_Type()
)
adFRPerformIntSignalStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntSignalStateChange.setStatus("mandatory")
_AdFRPerformIntHistoryTime_ObjectIdentity = ObjectIdentity
adFRPerformIntHistoryTime = _AdFRPerformIntHistoryTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6)
)
_AdFRPerformIntHistoryTimeTable_Object = MibTable
adFRPerformIntHistoryTimeTable = _AdFRPerformIntHistoryTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6, 1)
)
if mibBuilder.loadTexts:
    adFRPerformIntHistoryTimeTable.setStatus("mandatory")
_AdFRPerformIntHistoryTimeEntry_Object = MibTableRow
adFRPerformIntHistoryTimeEntry = _AdFRPerformIntHistoryTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6, 1, 1)
)
adFRPerformIntHistoryTimeEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformIntHistoryTimeSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformIntHistoryTimeEntry.setStatus("mandatory")
_AdFRPerformIntHistoryTimeSlotIndex_Type = Integer32
_AdFRPerformIntHistoryTimeSlotIndex_Object = MibTableColumn
adFRPerformIntHistoryTimeSlotIndex = _AdFRPerformIntHistoryTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6, 1, 1, 1),
    _AdFRPerformIntHistoryTimeSlotIndex_Type()
)
adFRPerformIntHistoryTimeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntHistoryTimeSlotIndex.setStatus("mandatory")
_AdFRPerformIntHistorySlotTotalTime_Type = Integer32
_AdFRPerformIntHistorySlotTotalTime_Object = MibTableColumn
adFRPerformIntHistorySlotTotalTime = _AdFRPerformIntHistorySlotTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6, 1, 1, 2),
    _AdFRPerformIntHistorySlotTotalTime_Type()
)
adFRPerformIntHistorySlotTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntHistorySlotTotalTime.setStatus("mandatory")
_AdFRPerformIntHistoryTimeStamp_Type = DisplayString
_AdFRPerformIntHistoryTimeStamp_Object = MibTableColumn
adFRPerformIntHistoryTimeStamp = _AdFRPerformIntHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 6, 1, 1, 3),
    _AdFRPerformIntHistoryTimeStamp_Type()
)
adFRPerformIntHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformIntHistoryTimeStamp.setStatus("mandatory")
_AdFRPerformDayPvcStatus_ObjectIdentity = ObjectIdentity
adFRPerformDayPvcStatus = _AdFRPerformDayPvcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7)
)
_AdFRPerformDayPvcStatusTable_Object = MibTable
adFRPerformDayPvcStatusTable = _AdFRPerformDayPvcStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    adFRPerformDayPvcStatusTable.setStatus("mandatory")
_AdFRPerformDayPvcStatusEntry_Object = MibTableRow
adFRPerformDayPvcStatusEntry = _AdFRPerformDayPvcStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1)
)
adFRPerformDayPvcStatusEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPvcIfIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPvcIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPvcSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformDayPvcStatusEntry.setStatus("mandatory")
_AdFRPerformDayPvcIfIndex_Type = Integer32
_AdFRPerformDayPvcIfIndex_Object = MibTableColumn
adFRPerformDayPvcIfIndex = _AdFRPerformDayPvcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 1),
    _AdFRPerformDayPvcIfIndex_Type()
)
adFRPerformDayPvcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPvcIfIndex.setStatus("mandatory")
_AdFRPerformDayPvcIndex_Type = Integer32
_AdFRPerformDayPvcIndex_Object = MibTableColumn
adFRPerformDayPvcIndex = _AdFRPerformDayPvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 2),
    _AdFRPerformDayPvcIndex_Type()
)
adFRPerformDayPvcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPvcIndex.setStatus("mandatory")
_AdFRPerformDayPvcSlotIndex_Type = Integer32
_AdFRPerformDayPvcSlotIndex_Object = MibTableColumn
adFRPerformDayPvcSlotIndex = _AdFRPerformDayPvcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 3),
    _AdFRPerformDayPvcSlotIndex_Type()
)
adFRPerformDayPvcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPvcSlotIndex.setStatus("mandatory")
_AdFRPerformDayPVCStateChange_Type = Counter32
_AdFRPerformDayPVCStateChange_Object = MibTableColumn
adFRPerformDayPVCStateChange = _AdFRPerformDayPVCStateChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 4),
    _AdFRPerformDayPVCStateChange_Type()
)
adFRPerformDayPVCStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCStateChange.setStatus("mandatory")
_AdFRPerformDayPVCInactiveTime_Type = Counter32
_AdFRPerformDayPVCInactiveTime_Object = MibTableColumn
adFRPerformDayPVCInactiveTime = _AdFRPerformDayPVCInactiveTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 5),
    _AdFRPerformDayPVCInactiveTime_Type()
)
adFRPerformDayPVCInactiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCInactiveTime.setStatus("mandatory")
_AdFRPerformDayPVCFramesRx_Type = Counter32
_AdFRPerformDayPVCFramesRx_Object = MibTableColumn
adFRPerformDayPVCFramesRx = _AdFRPerformDayPVCFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 6),
    _AdFRPerformDayPVCFramesRx_Type()
)
adFRPerformDayPVCFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCFramesRx.setStatus("mandatory")
_AdFRPerformDayPVCFramesTx_Type = Counter32
_AdFRPerformDayPVCFramesTx_Object = MibTableColumn
adFRPerformDayPVCFramesTx = _AdFRPerformDayPVCFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 7),
    _AdFRPerformDayPVCFramesTx_Type()
)
adFRPerformDayPVCFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCFramesTx.setStatus("mandatory")
_AdFRPerformDayPVCBytesRx_Type = Counter32
_AdFRPerformDayPVCBytesRx_Object = MibTableColumn
adFRPerformDayPVCBytesRx = _AdFRPerformDayPVCBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 8),
    _AdFRPerformDayPVCBytesRx_Type()
)
adFRPerformDayPVCBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBytesRx.setStatus("mandatory")
_AdFRPerformDayPVCBytesTx_Type = Counter32
_AdFRPerformDayPVCBytesTx_Object = MibTableColumn
adFRPerformDayPVCBytesTx = _AdFRPerformDayPVCBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 9),
    _AdFRPerformDayPVCBytesTx_Type()
)
adFRPerformDayPVCBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBytesTx.setStatus("mandatory")
_AdFRPerformDayPVCAvgThruputTx_Type = Gauge32
_AdFRPerformDayPVCAvgThruputTx_Object = MibTableColumn
adFRPerformDayPVCAvgThruputTx = _AdFRPerformDayPVCAvgThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 10),
    _AdFRPerformDayPVCAvgThruputTx_Type()
)
adFRPerformDayPVCAvgThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgThruputTx.setStatus("mandatory")
_AdFRPerformDayPVCAvgThruputRx_Type = Gauge32
_AdFRPerformDayPVCAvgThruputRx_Object = MibTableColumn
adFRPerformDayPVCAvgThruputRx = _AdFRPerformDayPVCAvgThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 11),
    _AdFRPerformDayPVCAvgThruputRx_Type()
)
adFRPerformDayPVCAvgThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgThruputRx.setStatus("mandatory")
_AdFRPerformDayPVCMaxThruputTx_Type = Counter32
_AdFRPerformDayPVCMaxThruputTx_Object = MibTableColumn
adFRPerformDayPVCMaxThruputTx = _AdFRPerformDayPVCMaxThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 12),
    _AdFRPerformDayPVCMaxThruputTx_Type()
)
adFRPerformDayPVCMaxThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxThruputTx.setStatus("mandatory")
_AdFRPerformDayPVCMaxThruputRx_Type = Counter32
_AdFRPerformDayPVCMaxThruputRx_Object = MibTableColumn
adFRPerformDayPVCMaxThruputRx = _AdFRPerformDayPVCMaxThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 13),
    _AdFRPerformDayPVCMaxThruputRx_Type()
)
adFRPerformDayPVCMaxThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxThruputRx.setStatus("mandatory")
_AdFRPerformDayPVCAvgUtilizationTx_Type = Gauge32
_AdFRPerformDayPVCAvgUtilizationTx_Object = MibTableColumn
adFRPerformDayPVCAvgUtilizationTx = _AdFRPerformDayPVCAvgUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 14),
    _AdFRPerformDayPVCAvgUtilizationTx_Type()
)
adFRPerformDayPVCAvgUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgUtilizationTx.setStatus("mandatory")
_AdFRPerformDayPVCAvgUtilizationRx_Type = Gauge32
_AdFRPerformDayPVCAvgUtilizationRx_Object = MibTableColumn
adFRPerformDayPVCAvgUtilizationRx = _AdFRPerformDayPVCAvgUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 15),
    _AdFRPerformDayPVCAvgUtilizationRx_Type()
)
adFRPerformDayPVCAvgUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgUtilizationRx.setStatus("mandatory")
_AdFRPerformDayPVCMaxUtilizationTx_Type = Counter32
_AdFRPerformDayPVCMaxUtilizationTx_Object = MibTableColumn
adFRPerformDayPVCMaxUtilizationTx = _AdFRPerformDayPVCMaxUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 16),
    _AdFRPerformDayPVCMaxUtilizationTx_Type()
)
adFRPerformDayPVCMaxUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxUtilizationTx.setStatus("mandatory")
_AdFRPerformDayPVCMaxUtilizationRx_Type = Counter32
_AdFRPerformDayPVCMaxUtilizationRx_Object = MibTableColumn
adFRPerformDayPVCMaxUtilizationRx = _AdFRPerformDayPVCMaxUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 17),
    _AdFRPerformDayPVCMaxUtilizationRx_Type()
)
adFRPerformDayPVCMaxUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxUtilizationRx.setStatus("mandatory")
_AdFRPerformDayPVCBurstTx_Type = Counter32
_AdFRPerformDayPVCBurstTx_Object = MibTableColumn
adFRPerformDayPVCBurstTx = _AdFRPerformDayPVCBurstTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 18),
    _AdFRPerformDayPVCBurstTx_Type()
)
adFRPerformDayPVCBurstTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBurstTx.setStatus("mandatory")
_AdFRPerformDayPVCBurstRx_Type = Counter32
_AdFRPerformDayPVCBurstRx_Object = MibTableColumn
adFRPerformDayPVCBurstRx = _AdFRPerformDayPVCBurstRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 19),
    _AdFRPerformDayPVCBurstRx_Type()
)
adFRPerformDayPVCBurstRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBurstRx.setStatus("mandatory")
_AdFRPerformDayPVCFecnRx_Type = Counter32
_AdFRPerformDayPVCFecnRx_Object = MibTableColumn
adFRPerformDayPVCFecnRx = _AdFRPerformDayPVCFecnRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 20),
    _AdFRPerformDayPVCFecnRx_Type()
)
adFRPerformDayPVCFecnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCFecnRx.setStatus("mandatory")
_AdFRPerformDayPVCFecnTx_Type = Counter32
_AdFRPerformDayPVCFecnTx_Object = MibTableColumn
adFRPerformDayPVCFecnTx = _AdFRPerformDayPVCFecnTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 21),
    _AdFRPerformDayPVCFecnTx_Type()
)
adFRPerformDayPVCFecnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCFecnTx.setStatus("mandatory")
_AdFRPerformDayPVCBecnRx_Type = Counter32
_AdFRPerformDayPVCBecnRx_Object = MibTableColumn
adFRPerformDayPVCBecnRx = _AdFRPerformDayPVCBecnRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 22),
    _AdFRPerformDayPVCBecnRx_Type()
)
adFRPerformDayPVCBecnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBecnRx.setStatus("mandatory")
_AdFRPerformDayPVCBecnTx_Type = Counter32
_AdFRPerformDayPVCBecnTx_Object = MibTableColumn
adFRPerformDayPVCBecnTx = _AdFRPerformDayPVCBecnTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 23),
    _AdFRPerformDayPVCBecnTx_Type()
)
adFRPerformDayPVCBecnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCBecnTx.setStatus("mandatory")
_AdFRPerformDayPVCDeRx_Type = Counter32
_AdFRPerformDayPVCDeRx_Object = MibTableColumn
adFRPerformDayPVCDeRx = _AdFRPerformDayPVCDeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 24),
    _AdFRPerformDayPVCDeRx_Type()
)
adFRPerformDayPVCDeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCDeRx.setStatus("mandatory")
_AdFRPerformDayPVCDeTx_Type = Counter32
_AdFRPerformDayPVCDeTx_Object = MibTableColumn
adFRPerformDayPVCDeTx = _AdFRPerformDayPVCDeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 25),
    _AdFRPerformDayPVCDeTx_Type()
)
adFRPerformDayPVCDeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCDeTx.setStatus("mandatory")
_AdFRPerformDayPVCCrRx_Type = Counter32
_AdFRPerformDayPVCCrRx_Object = MibTableColumn
adFRPerformDayPVCCrRx = _AdFRPerformDayPVCCrRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 26),
    _AdFRPerformDayPVCCrRx_Type()
)
adFRPerformDayPVCCrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCCrRx.setStatus("mandatory")
_AdFRPerformDayPVCCrTx_Type = Counter32
_AdFRPerformDayPVCCrTx_Object = MibTableColumn
adFRPerformDayPVCCrTx = _AdFRPerformDayPVCCrTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 27),
    _AdFRPerformDayPVCCrTx_Type()
)
adFRPerformDayPVCCrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCCrTx.setStatus("mandatory")
_AdFRPerformDayPVCMinFrameSizeRx_Type = Counter32
_AdFRPerformDayPVCMinFrameSizeRx_Object = MibTableColumn
adFRPerformDayPVCMinFrameSizeRx = _AdFRPerformDayPVCMinFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 28),
    _AdFRPerformDayPVCMinFrameSizeRx_Type()
)
adFRPerformDayPVCMinFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMinFrameSizeRx.setStatus("mandatory")
_AdFRPerformDayPVCMinFrameSizeTx_Type = Counter32
_AdFRPerformDayPVCMinFrameSizeTx_Object = MibTableColumn
adFRPerformDayPVCMinFrameSizeTx = _AdFRPerformDayPVCMinFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 29),
    _AdFRPerformDayPVCMinFrameSizeTx_Type()
)
adFRPerformDayPVCMinFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMinFrameSizeTx.setStatus("mandatory")
_AdFRPerformDayPVCMaxFrameSizeRx_Type = Counter32
_AdFRPerformDayPVCMaxFrameSizeRx_Object = MibTableColumn
adFRPerformDayPVCMaxFrameSizeRx = _AdFRPerformDayPVCMaxFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 30),
    _AdFRPerformDayPVCMaxFrameSizeRx_Type()
)
adFRPerformDayPVCMaxFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxFrameSizeRx.setStatus("mandatory")
_AdFRPerformDayPVCMaxFrameSizeTx_Type = Counter32
_AdFRPerformDayPVCMaxFrameSizeTx_Object = MibTableColumn
adFRPerformDayPVCMaxFrameSizeTx = _AdFRPerformDayPVCMaxFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 31),
    _AdFRPerformDayPVCMaxFrameSizeTx_Type()
)
adFRPerformDayPVCMaxFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxFrameSizeTx.setStatus("mandatory")
_AdFRPerformDayPVCAvgFrameSizeRx_Type = Gauge32
_AdFRPerformDayPVCAvgFrameSizeRx_Object = MibTableColumn
adFRPerformDayPVCAvgFrameSizeRx = _AdFRPerformDayPVCAvgFrameSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 32),
    _AdFRPerformDayPVCAvgFrameSizeRx_Type()
)
adFRPerformDayPVCAvgFrameSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgFrameSizeRx.setStatus("mandatory")
_AdFRPerformDayPVCAvgFrameSizeTx_Type = Gauge32
_AdFRPerformDayPVCAvgFrameSizeTx_Object = MibTableColumn
adFRPerformDayPVCAvgFrameSizeTx = _AdFRPerformDayPVCAvgFrameSizeTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 33),
    _AdFRPerformDayPVCAvgFrameSizeTx_Type()
)
adFRPerformDayPVCAvgFrameSizeTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgFrameSizeTx.setStatus("mandatory")
_AdFRPerformDayPVCLostFrames_Type = Counter32
_AdFRPerformDayPVCLostFrames_Object = MibTableColumn
adFRPerformDayPVCLostFrames = _AdFRPerformDayPVCLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 34),
    _AdFRPerformDayPVCLostFrames_Type()
)
adFRPerformDayPVCLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCLostFrames.setStatus("mandatory")
_AdFRPerformDayPVCRemoteLostFrames_Type = Counter32
_AdFRPerformDayPVCRemoteLostFrames_Object = MibTableColumn
adFRPerformDayPVCRemoteLostFrames = _AdFRPerformDayPVCRemoteLostFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 35),
    _AdFRPerformDayPVCRemoteLostFrames_Type()
)
adFRPerformDayPVCRemoteLostFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCRemoteLostFrames.setStatus("mandatory")
_AdFRPerformDayPVCMaxDelay_Type = Gauge32
_AdFRPerformDayPVCMaxDelay_Object = MibTableColumn
adFRPerformDayPVCMaxDelay = _AdFRPerformDayPVCMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 36),
    _AdFRPerformDayPVCMaxDelay_Type()
)
adFRPerformDayPVCMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMaxDelay.setStatus("mandatory")
_AdFRPerformDayPVCMinDelay_Type = Gauge32
_AdFRPerformDayPVCMinDelay_Object = MibTableColumn
adFRPerformDayPVCMinDelay = _AdFRPerformDayPVCMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 37),
    _AdFRPerformDayPVCMinDelay_Type()
)
adFRPerformDayPVCMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCMinDelay.setStatus("mandatory")
_AdFRPerformDayPVCAvgDelay_Type = Gauge32
_AdFRPerformDayPVCAvgDelay_Object = MibTableColumn
adFRPerformDayPVCAvgDelay = _AdFRPerformDayPVCAvgDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 38),
    _AdFRPerformDayPVCAvgDelay_Type()
)
adFRPerformDayPVCAvgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCAvgDelay.setStatus("mandatory")
_AdFRPerformDayPVCTimeInDBU_Type = Counter32
_AdFRPerformDayPVCTimeInDBU_Object = MibTableColumn
adFRPerformDayPVCTimeInDBU = _AdFRPerformDayPVCTimeInDBU_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 7, 1, 1, 39),
    _AdFRPerformDayPVCTimeInDBU_Type()
)
adFRPerformDayPVCTimeInDBU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPVCTimeInDBU.setStatus("mandatory")
_AdFRPerformDayPortStatus_ObjectIdentity = ObjectIdentity
adFRPerformDayPortStatus = _AdFRPerformDayPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8)
)
_AdFRPerformDayPortStatusTable_Object = MibTable
adFRPerformDayPortStatusTable = _AdFRPerformDayPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    adFRPerformDayPortStatusTable.setStatus("mandatory")
_AdFRPerformDayPortStatusEntry_Object = MibTableRow
adFRPerformDayPortStatusEntry = _AdFRPerformDayPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1)
)
adFRPerformDayPortStatusEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayIfIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPortSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformDayPortStatusEntry.setStatus("mandatory")
_AdFRPerformDayIfIndex_Type = Integer32
_AdFRPerformDayIfIndex_Object = MibTableColumn
adFRPerformDayIfIndex = _AdFRPerformDayIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 1),
    _AdFRPerformDayIfIndex_Type()
)
adFRPerformDayIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayIfIndex.setStatus("mandatory")
_AdFRPerformDayPortSlotIndex_Type = Integer32
_AdFRPerformDayPortSlotIndex_Object = MibTableColumn
adFRPerformDayPortSlotIndex = _AdFRPerformDayPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 2),
    _AdFRPerformDayPortSlotIndex_Type()
)
adFRPerformDayPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortSlotIndex.setStatus("mandatory")
_AdFRPerformDayPortFramesRx_Type = Counter32
_AdFRPerformDayPortFramesRx_Object = MibTableColumn
adFRPerformDayPortFramesRx = _AdFRPerformDayPortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 3),
    _AdFRPerformDayPortFramesRx_Type()
)
adFRPerformDayPortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortFramesRx.setStatus("mandatory")
_AdFRPerformDayPortFramesTx_Type = Counter32
_AdFRPerformDayPortFramesTx_Object = MibTableColumn
adFRPerformDayPortFramesTx = _AdFRPerformDayPortFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 4),
    _AdFRPerformDayPortFramesTx_Type()
)
adFRPerformDayPortFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortFramesTx.setStatus("mandatory")
_AdFRPerformDayPortBytesRx_Type = Counter32
_AdFRPerformDayPortBytesRx_Object = MibTableColumn
adFRPerformDayPortBytesRx = _AdFRPerformDayPortBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 5),
    _AdFRPerformDayPortBytesRx_Type()
)
adFRPerformDayPortBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortBytesRx.setStatus("mandatory")
_AdFRPerformDayPortBytesTx_Type = Counter32
_AdFRPerformDayPortBytesTx_Object = MibTableColumn
adFRPerformDayPortBytesTx = _AdFRPerformDayPortBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 6),
    _AdFRPerformDayPortBytesTx_Type()
)
adFRPerformDayPortBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortBytesTx.setStatus("mandatory")
_AdFRPerformDayPortAvgThruputTx_Type = Gauge32
_AdFRPerformDayPortAvgThruputTx_Object = MibTableColumn
adFRPerformDayPortAvgThruputTx = _AdFRPerformDayPortAvgThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 7),
    _AdFRPerformDayPortAvgThruputTx_Type()
)
adFRPerformDayPortAvgThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortAvgThruputTx.setStatus("mandatory")
_AdFRPerformDayPortAvgThruputRx_Type = Gauge32
_AdFRPerformDayPortAvgThruputRx_Object = MibTableColumn
adFRPerformDayPortAvgThruputRx = _AdFRPerformDayPortAvgThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 8),
    _AdFRPerformDayPortAvgThruputRx_Type()
)
adFRPerformDayPortAvgThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortAvgThruputRx.setStatus("mandatory")
_AdFRPerformDayPortMaxThruputTx_Type = Counter32
_AdFRPerformDayPortMaxThruputTx_Object = MibTableColumn
adFRPerformDayPortMaxThruputTx = _AdFRPerformDayPortMaxThruputTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 9),
    _AdFRPerformDayPortMaxThruputTx_Type()
)
adFRPerformDayPortMaxThruputTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortMaxThruputTx.setStatus("mandatory")
_AdFRPerformDayPortMaxThruputRx_Type = Counter32
_AdFRPerformDayPortMaxThruputRx_Object = MibTableColumn
adFRPerformDayPortMaxThruputRx = _AdFRPerformDayPortMaxThruputRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 10),
    _AdFRPerformDayPortMaxThruputRx_Type()
)
adFRPerformDayPortMaxThruputRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortMaxThruputRx.setStatus("mandatory")
_AdFRPerformDayPortAvgUtilizationTx_Type = Gauge32
_AdFRPerformDayPortAvgUtilizationTx_Object = MibTableColumn
adFRPerformDayPortAvgUtilizationTx = _AdFRPerformDayPortAvgUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 11),
    _AdFRPerformDayPortAvgUtilizationTx_Type()
)
adFRPerformDayPortAvgUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortAvgUtilizationTx.setStatus("mandatory")
_AdFRPerformDayPortAvgUtilizationRx_Type = Gauge32
_AdFRPerformDayPortAvgUtilizationRx_Object = MibTableColumn
adFRPerformDayPortAvgUtilizationRx = _AdFRPerformDayPortAvgUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 12),
    _AdFRPerformDayPortAvgUtilizationRx_Type()
)
adFRPerformDayPortAvgUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortAvgUtilizationRx.setStatus("mandatory")
_AdFRPerformDayPortMaxUtilizationTx_Type = Counter32
_AdFRPerformDayPortMaxUtilizationTx_Object = MibTableColumn
adFRPerformDayPortMaxUtilizationTx = _AdFRPerformDayPortMaxUtilizationTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 13),
    _AdFRPerformDayPortMaxUtilizationTx_Type()
)
adFRPerformDayPortMaxUtilizationTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortMaxUtilizationTx.setStatus("mandatory")
_AdFRPerformDayPortMaxUtilizationRx_Type = Counter32
_AdFRPerformDayPortMaxUtilizationRx_Object = MibTableColumn
adFRPerformDayPortMaxUtilizationRx = _AdFRPerformDayPortMaxUtilizationRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 14),
    _AdFRPerformDayPortMaxUtilizationRx_Type()
)
adFRPerformDayPortMaxUtilizationRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortMaxUtilizationRx.setStatus("mandatory")
_AdFRPerformDayPortFullStatusRX_Type = Counter32
_AdFRPerformDayPortFullStatusRX_Object = MibTableColumn
adFRPerformDayPortFullStatusRX = _AdFRPerformDayPortFullStatusRX_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 15),
    _AdFRPerformDayPortFullStatusRX_Type()
)
adFRPerformDayPortFullStatusRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortFullStatusRX.setStatus("mandatory")
_AdFRPerformDayPortFullStatusTx_Type = Counter32
_AdFRPerformDayPortFullStatusTx_Object = MibTableColumn
adFRPerformDayPortFullStatusTx = _AdFRPerformDayPortFullStatusTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 16),
    _AdFRPerformDayPortFullStatusTx_Type()
)
adFRPerformDayPortFullStatusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortFullStatusTx.setStatus("mandatory")
_AdFRPerformDayPortLIOnlyRX_Type = Counter32
_AdFRPerformDayPortLIOnlyRX_Object = MibTableColumn
adFRPerformDayPortLIOnlyRX = _AdFRPerformDayPortLIOnlyRX_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 17),
    _AdFRPerformDayPortLIOnlyRX_Type()
)
adFRPerformDayPortLIOnlyRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortLIOnlyRX.setStatus("mandatory")
_AdFRPerformDayPortLIOnlyTx_Type = Counter32
_AdFRPerformDayPortLIOnlyTx_Object = MibTableColumn
adFRPerformDayPortLIOnlyTx = _AdFRPerformDayPortLIOnlyTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 18),
    _AdFRPerformDayPortLIOnlyTx_Type()
)
adFRPerformDayPortLIOnlyTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortLIOnlyTx.setStatus("mandatory")
_AdFRPerformDayPortAsyncStatusFrame_Type = Counter32
_AdFRPerformDayPortAsyncStatusFrame_Object = MibTableColumn
adFRPerformDayPortAsyncStatusFrame = _AdFRPerformDayPortAsyncStatusFrame_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 8, 1, 1, 19),
    _AdFRPerformDayPortAsyncStatusFrame_Type()
)
adFRPerformDayPortAsyncStatusFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortAsyncStatusFrame.setStatus("mandatory")
_AdFRPerformDayPortError_ObjectIdentity = ObjectIdentity
adFRPerformDayPortError = _AdFRPerformDayPortError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9)
)
_AdFRPerformDayPortErrorTable_Object = MibTable
adFRPerformDayPortErrorTable = _AdFRPerformDayPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1)
)
if mibBuilder.loadTexts:
    adFRPerformDayPortErrorTable.setStatus("mandatory")
_AdFRPerformDayPortErrorEntry_Object = MibTableRow
adFRPerformDayPortErrorEntry = _AdFRPerformDayPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1)
)
adFRPerformDayPortErrorEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPortIndex"),
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayPortErrorSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformDayPortErrorEntry.setStatus("mandatory")
_AdFRPerformDayPortIndex_Type = Integer32
_AdFRPerformDayPortIndex_Object = MibTableColumn
adFRPerformDayPortIndex = _AdFRPerformDayPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 1),
    _AdFRPerformDayPortIndex_Type()
)
adFRPerformDayPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortIndex.setStatus("mandatory")
_AdFRPerformDayPortErrorSlotIndex_Type = Integer32
_AdFRPerformDayPortErrorSlotIndex_Object = MibTableColumn
adFRPerformDayPortErrorSlotIndex = _AdFRPerformDayPortErrorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 2),
    _AdFRPerformDayPortErrorSlotIndex_Type()
)
adFRPerformDayPortErrorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortErrorSlotIndex.setStatus("mandatory")
_AdFRPerformDayPortUnavailableTime_Type = Counter32
_AdFRPerformDayPortUnavailableTime_Object = MibTableColumn
adFRPerformDayPortUnavailableTime = _AdFRPerformDayPortUnavailableTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 3),
    _AdFRPerformDayPortUnavailableTime_Type()
)
adFRPerformDayPortUnavailableTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayPortUnavailableTime.setStatus("mandatory")
_AdFRPerformDayCrcErrors_Type = Counter32
_AdFRPerformDayCrcErrors_Object = MibTableColumn
adFRPerformDayCrcErrors = _AdFRPerformDayCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 4),
    _AdFRPerformDayCrcErrors_Type()
)
adFRPerformDayCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayCrcErrors.setStatus("mandatory")
_AdFRPerformDayAbortFrames_Type = Counter32
_AdFRPerformDayAbortFrames_Object = MibTableColumn
adFRPerformDayAbortFrames = _AdFRPerformDayAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 5),
    _AdFRPerformDayAbortFrames_Type()
)
adFRPerformDayAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayAbortFrames.setStatus("mandatory")
_AdFRPerformDayOctectViolations_Type = Counter32
_AdFRPerformDayOctectViolations_Object = MibTableColumn
adFRPerformDayOctectViolations = _AdFRPerformDayOctectViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 6),
    _AdFRPerformDayOctectViolations_Type()
)
adFRPerformDayOctectViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayOctectViolations.setStatus("mandatory")
_AdFRPerformDayDiscardFrames_Type = Counter32
_AdFRPerformDayDiscardFrames_Object = MibTableColumn
adFRPerformDayDiscardFrames = _AdFRPerformDayDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 7),
    _AdFRPerformDayDiscardFrames_Type()
)
adFRPerformDayDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayDiscardFrames.setStatus("mandatory")
_AdFRPerformDayLengthErrors_Type = Counter32
_AdFRPerformDayLengthErrors_Object = MibTableColumn
adFRPerformDayLengthErrors = _AdFRPerformDayLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 8),
    _AdFRPerformDayLengthErrors_Type()
)
adFRPerformDayLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayLengthErrors.setStatus("mandatory")
_AdFRPerformDayEAViolations_Type = Counter32
_AdFRPerformDayEAViolations_Object = MibTableColumn
adFRPerformDayEAViolations = _AdFRPerformDayEAViolations_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 9),
    _AdFRPerformDayEAViolations_Type()
)
adFRPerformDayEAViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayEAViolations.setStatus("mandatory")
_AdFRPerformDayEncapsulationErrors_Type = Counter32
_AdFRPerformDayEncapsulationErrors_Object = MibTableColumn
adFRPerformDayEncapsulationErrors = _AdFRPerformDayEncapsulationErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 10),
    _AdFRPerformDayEncapsulationErrors_Type()
)
adFRPerformDayEncapsulationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayEncapsulationErrors.setStatus("mandatory")
_AdFRPerformDayInactiveDLCI_Type = Counter32
_AdFRPerformDayInactiveDLCI_Object = MibTableColumn
adFRPerformDayInactiveDLCI = _AdFRPerformDayInactiveDLCI_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 11),
    _AdFRPerformDayInactiveDLCI_Type()
)
adFRPerformDayInactiveDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayInactiveDLCI.setStatus("mandatory")
_AdFRPerformDayInvalidDLCI_Type = Counter32
_AdFRPerformDayInvalidDLCI_Object = MibTableColumn
adFRPerformDayInvalidDLCI = _AdFRPerformDayInvalidDLCI_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 12),
    _AdFRPerformDayInvalidDLCI_Type()
)
adFRPerformDayInvalidDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayInvalidDLCI.setStatus("mandatory")
_AdFRPerformDayUnroutable_Type = Counter32
_AdFRPerformDayUnroutable_Object = MibTableColumn
adFRPerformDayUnroutable = _AdFRPerformDayUnroutable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 13),
    _AdFRPerformDayUnroutable_Type()
)
adFRPerformDayUnroutable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayUnroutable.setStatus("mandatory")
_AdFRPerformDaySignalDownTime_Type = Counter32
_AdFRPerformDaySignalDownTime_Object = MibTableColumn
adFRPerformDaySignalDownTime = _AdFRPerformDaySignalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 14),
    _AdFRPerformDaySignalDownTime_Type()
)
adFRPerformDaySignalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDaySignalDownTime.setStatus("mandatory")
_AdFRPerformDaySignalErrors_Type = Counter32
_AdFRPerformDaySignalErrors_Object = MibTableColumn
adFRPerformDaySignalErrors = _AdFRPerformDaySignalErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 15),
    _AdFRPerformDaySignalErrors_Type()
)
adFRPerformDaySignalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDaySignalErrors.setStatus("mandatory")
_AdFRPerformDaySignalTimeOut_Type = Counter32
_AdFRPerformDaySignalTimeOut_Object = MibTableColumn
adFRPerformDaySignalTimeOut = _AdFRPerformDaySignalTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 16),
    _AdFRPerformDaySignalTimeOut_Type()
)
adFRPerformDaySignalTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDaySignalTimeOut.setStatus("mandatory")
_AdFRPerformDaySignalStateChange_Type = Counter32
_AdFRPerformDaySignalStateChange_Object = MibTableColumn
adFRPerformDaySignalStateChange = _AdFRPerformDaySignalStateChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 9, 1, 1, 17),
    _AdFRPerformDaySignalStateChange_Type()
)
adFRPerformDaySignalStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDaySignalStateChange.setStatus("mandatory")
_AdFRPerformDayHistoryTime_ObjectIdentity = ObjectIdentity
adFRPerformDayHistoryTime = _AdFRPerformDayHistoryTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10)
)
_AdFRPerformDayHistoryTimeTable_Object = MibTable
adFRPerformDayHistoryTimeTable = _AdFRPerformDayHistoryTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10, 1)
)
if mibBuilder.loadTexts:
    adFRPerformDayHistoryTimeTable.setStatus("mandatory")
_AdFRPerformDayHistoryTimeEntry_Object = MibTableRow
adFRPerformDayHistoryTimeEntry = _AdFRPerformDayHistoryTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10, 1, 1)
)
adFRPerformDayHistoryTimeEntry.setIndexNames(
    (0, "ADTRAN-FRPerform-MIB", "adFRPerformDayHistoryTimeSlotIndex"),
)
if mibBuilder.loadTexts:
    adFRPerformDayHistoryTimeEntry.setStatus("mandatory")
_AdFRPerformDayHistoryTimeSlotIndex_Type = Integer32
_AdFRPerformDayHistoryTimeSlotIndex_Object = MibTableColumn
adFRPerformDayHistoryTimeSlotIndex = _AdFRPerformDayHistoryTimeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10, 1, 1, 1),
    _AdFRPerformDayHistoryTimeSlotIndex_Type()
)
adFRPerformDayHistoryTimeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayHistoryTimeSlotIndex.setStatus("mandatory")
_AdFRPerformDayHistorySlotTotalTime_Type = Integer32
_AdFRPerformDayHistorySlotTotalTime_Object = MibTableColumn
adFRPerformDayHistorySlotTotalTime = _AdFRPerformDayHistorySlotTotalTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10, 1, 1, 2),
    _AdFRPerformDayHistorySlotTotalTime_Type()
)
adFRPerformDayHistorySlotTotalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayHistorySlotTotalTime.setStatus("mandatory")
_AdFRPerformDayHistoryTimeStamp_Type = DisplayString
_AdFRPerformDayHistoryTimeStamp_Object = MibTableColumn
adFRPerformDayHistoryTimeStamp = _AdFRPerformDayHistoryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 4, 1, 10, 1, 1, 3),
    _AdFRPerformDayHistoryTimeStamp_Type()
)
adFRPerformDayHistoryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adFRPerformDayHistoryTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-FRPerform-MIB",
    **{"adPerform": adPerform,
       "adFRPerformmg": adFRPerformmg,
       "adFRPerformHistoryControl": adFRPerformHistoryControl,
       "adFRPerformHistoryIntLength": adFRPerformHistoryIntLength,
       "adFRPerformCurrentIntTimeRemaining": adFRPerformCurrentIntTimeRemaining,
       "adFRPerformCompletedInts": adFRPerformCompletedInts,
       "adFRPerformCompletedDays": adFRPerformCompletedDays,
       "adFRPerformCurrentPvcStatus": adFRPerformCurrentPvcStatus,
       "adFRPerformCurrentPvcStatusTable": adFRPerformCurrentPvcStatusTable,
       "adFRPerformCurrentPvcStatusEntry": adFRPerformCurrentPvcStatusEntry,
       "adFRPerformCurrentPvcIfIndex": adFRPerformCurrentPvcIfIndex,
       "adFRPerformCurrentPvcStatusIndex": adFRPerformCurrentPvcStatusIndex,
       "adFRPerformCurrentPvcState": adFRPerformCurrentPvcState,
       "adFRPerformCurrentPvcStatistics": adFRPerformCurrentPvcStatistics,
       "adFRPerformIntPvcStatus": adFRPerformIntPvcStatus,
       "adFRPerformIntPvcStatusTable": adFRPerformIntPvcStatusTable,
       "adFRPerformIntPvcStatusEntry": adFRPerformIntPvcStatusEntry,
       "adFRPerformIntPvcIfIndex": adFRPerformIntPvcIfIndex,
       "adFRPerformIntPvcIndex": adFRPerformIntPvcIndex,
       "adFRPerformIntPvcSlotIndex": adFRPerformIntPvcSlotIndex,
       "adFRPerformIntPVCStateChange": adFRPerformIntPVCStateChange,
       "adFRPerformIntPVCInactiveTime": adFRPerformIntPVCInactiveTime,
       "adFRPerformIntPVCFramesRx": adFRPerformIntPVCFramesRx,
       "adFRPerformIntPVCFramesTx": adFRPerformIntPVCFramesTx,
       "adFRPerformIntPVCBytesRx": adFRPerformIntPVCBytesRx,
       "adFRPerformIntPVCBytesTx": adFRPerformIntPVCBytesTx,
       "adFRPerformIntPVCAvgThruputTx": adFRPerformIntPVCAvgThruputTx,
       "adFRPerformIntPVCAvgThruputRx": adFRPerformIntPVCAvgThruputRx,
       "adFRPerformIntPVCMaxThruputTx": adFRPerformIntPVCMaxThruputTx,
       "adFRPerformIntPVCMaxThruputRx": adFRPerformIntPVCMaxThruputRx,
       "adFRPerformIntPVCAvgUtilizationTx": adFRPerformIntPVCAvgUtilizationTx,
       "adFRPerformIntPVCAvgUtilizationRx": adFRPerformIntPVCAvgUtilizationRx,
       "adFRPerformIntPVCMaxUtilizationTx": adFRPerformIntPVCMaxUtilizationTx,
       "adFRPerformIntPVCMaxUtilizationRx": adFRPerformIntPVCMaxUtilizationRx,
       "adFRPerformIntPVCBurstTx": adFRPerformIntPVCBurstTx,
       "adFRPerformIntPVCBurstRx": adFRPerformIntPVCBurstRx,
       "adFRPerformIntPVCFecnRx": adFRPerformIntPVCFecnRx,
       "adFRPerformIntPVCFecnTx": adFRPerformIntPVCFecnTx,
       "adFRPerformIntPVCBecnRx": adFRPerformIntPVCBecnRx,
       "adFRPerformIntPVCBecnTx": adFRPerformIntPVCBecnTx,
       "adFRPerformIntPVCDeRx": adFRPerformIntPVCDeRx,
       "adFRPerformIntPVCDeTx": adFRPerformIntPVCDeTx,
       "adFRPerformIntPVCCrRx": adFRPerformIntPVCCrRx,
       "adFRPerformIntPVCCrTx": adFRPerformIntPVCCrTx,
       "adFRPerformIntPVCMinFrameSizeRx": adFRPerformIntPVCMinFrameSizeRx,
       "adFRPerformIntPVCMinFrameSizeTx": adFRPerformIntPVCMinFrameSizeTx,
       "adFRPerformIntPVCMaxFrameSizeRx": adFRPerformIntPVCMaxFrameSizeRx,
       "adFRPerformIntPVCMaxFrameSizeTx": adFRPerformIntPVCMaxFrameSizeTx,
       "adFRPerformIntPVCAvgFrameSizeRx": adFRPerformIntPVCAvgFrameSizeRx,
       "adFRPerformIntPVCAvgFrameSizeTx": adFRPerformIntPVCAvgFrameSizeTx,
       "adFRPerformIntPVCLostFrames": adFRPerformIntPVCLostFrames,
       "adFRPerformIntPVCRemoteLostFrames": adFRPerformIntPVCRemoteLostFrames,
       "adFRPerformIntPVCMaxDelay": adFRPerformIntPVCMaxDelay,
       "adFRPerformIntPVCMinDelay": adFRPerformIntPVCMinDelay,
       "adFRPerformIntPVCAvgDelay": adFRPerformIntPVCAvgDelay,
       "adFRPerformIntPVCTimeInDBU": adFRPerformIntPVCTimeInDBU,
       "adFRPerformIntPortStatus": adFRPerformIntPortStatus,
       "adFRPerformIntPortStatusTable": adFRPerformIntPortStatusTable,
       "adFRPerformIntPortStatusEntry": adFRPerformIntPortStatusEntry,
       "adFRPerformIntIfIndex": adFRPerformIntIfIndex,
       "adFRPerformIntPortSlotIndex": adFRPerformIntPortSlotIndex,
       "adFRPerformIntPortFramesRx": adFRPerformIntPortFramesRx,
       "adFRPerformIntPortFramesTx": adFRPerformIntPortFramesTx,
       "adFRPerformIntPortBytesRx": adFRPerformIntPortBytesRx,
       "adFRPerformIntPortBytesTx": adFRPerformIntPortBytesTx,
       "adFRPerformIntPortAvgThruputTx": adFRPerformIntPortAvgThruputTx,
       "adFRPerformIntPortAvgThruputRx": adFRPerformIntPortAvgThruputRx,
       "adFRPerformIntPortMaxThruputTx": adFRPerformIntPortMaxThruputTx,
       "adFRPerformIntPortMaxThruputRx": adFRPerformIntPortMaxThruputRx,
       "adFRPerformIntPortAvgUtilizationTx": adFRPerformIntPortAvgUtilizationTx,
       "adFRPerformIntPortAvgUtilizationRx": adFRPerformIntPortAvgUtilizationRx,
       "adFRPerformIntPortMaxUtilizationTx": adFRPerformIntPortMaxUtilizationTx,
       "adFRPerformIntPortMaxUtilizationRx": adFRPerformIntPortMaxUtilizationRx,
       "adFRPerformIntPortFullStatusRX": adFRPerformIntPortFullStatusRX,
       "adFRPerformIntPortFullStatusTx": adFRPerformIntPortFullStatusTx,
       "adFRPerformIntPortLIOnlyRX": adFRPerformIntPortLIOnlyRX,
       "adFRPerformIntPortLIOnlyTx": adFRPerformIntPortLIOnlyTx,
       "adFRPerformIntPortAsyncStatusFrame": adFRPerformIntPortAsyncStatusFrame,
       "adFRPerformIntPortError": adFRPerformIntPortError,
       "adFRPerformIntPortErrorTable": adFRPerformIntPortErrorTable,
       "adFRPerformIntPortErrorEntry": adFRPerformIntPortErrorEntry,
       "adFRPerformIntPortIndex": adFRPerformIntPortIndex,
       "adFRPerformIntPortErrorSlotIndex": adFRPerformIntPortErrorSlotIndex,
       "adFRPerformIntPortUnavailableTime": adFRPerformIntPortUnavailableTime,
       "adFRPerformIntCrcErrors": adFRPerformIntCrcErrors,
       "adFRPerformIntAbortFrames": adFRPerformIntAbortFrames,
       "adFRPerformIntOctectViolations": adFRPerformIntOctectViolations,
       "adFRPerformIntDiscardFrames": adFRPerformIntDiscardFrames,
       "adFRPerformIntLengthErrors": adFRPerformIntLengthErrors,
       "adFRPerformIntEAViolations": adFRPerformIntEAViolations,
       "adFRPerformIntEncapsulationErrors": adFRPerformIntEncapsulationErrors,
       "adFRPerformIntInactiveDLCI": adFRPerformIntInactiveDLCI,
       "adFRPerformIntInvalidDLCI": adFRPerformIntInvalidDLCI,
       "adFRPerformIntUnroutable": adFRPerformIntUnroutable,
       "adFRPerformIntSignalDownTime": adFRPerformIntSignalDownTime,
       "adFRPerformIntSignalErrors": adFRPerformIntSignalErrors,
       "adFRPerformIntSignalTimeOut": adFRPerformIntSignalTimeOut,
       "adFRPerformIntSignalStateChange": adFRPerformIntSignalStateChange,
       "adFRPerformIntHistoryTime": adFRPerformIntHistoryTime,
       "adFRPerformIntHistoryTimeTable": adFRPerformIntHistoryTimeTable,
       "adFRPerformIntHistoryTimeEntry": adFRPerformIntHistoryTimeEntry,
       "adFRPerformIntHistoryTimeSlotIndex": adFRPerformIntHistoryTimeSlotIndex,
       "adFRPerformIntHistorySlotTotalTime": adFRPerformIntHistorySlotTotalTime,
       "adFRPerformIntHistoryTimeStamp": adFRPerformIntHistoryTimeStamp,
       "adFRPerformDayPvcStatus": adFRPerformDayPvcStatus,
       "adFRPerformDayPvcStatusTable": adFRPerformDayPvcStatusTable,
       "adFRPerformDayPvcStatusEntry": adFRPerformDayPvcStatusEntry,
       "adFRPerformDayPvcIfIndex": adFRPerformDayPvcIfIndex,
       "adFRPerformDayPvcIndex": adFRPerformDayPvcIndex,
       "adFRPerformDayPvcSlotIndex": adFRPerformDayPvcSlotIndex,
       "adFRPerformDayPVCStateChange": adFRPerformDayPVCStateChange,
       "adFRPerformDayPVCInactiveTime": adFRPerformDayPVCInactiveTime,
       "adFRPerformDayPVCFramesRx": adFRPerformDayPVCFramesRx,
       "adFRPerformDayPVCFramesTx": adFRPerformDayPVCFramesTx,
       "adFRPerformDayPVCBytesRx": adFRPerformDayPVCBytesRx,
       "adFRPerformDayPVCBytesTx": adFRPerformDayPVCBytesTx,
       "adFRPerformDayPVCAvgThruputTx": adFRPerformDayPVCAvgThruputTx,
       "adFRPerformDayPVCAvgThruputRx": adFRPerformDayPVCAvgThruputRx,
       "adFRPerformDayPVCMaxThruputTx": adFRPerformDayPVCMaxThruputTx,
       "adFRPerformDayPVCMaxThruputRx": adFRPerformDayPVCMaxThruputRx,
       "adFRPerformDayPVCAvgUtilizationTx": adFRPerformDayPVCAvgUtilizationTx,
       "adFRPerformDayPVCAvgUtilizationRx": adFRPerformDayPVCAvgUtilizationRx,
       "adFRPerformDayPVCMaxUtilizationTx": adFRPerformDayPVCMaxUtilizationTx,
       "adFRPerformDayPVCMaxUtilizationRx": adFRPerformDayPVCMaxUtilizationRx,
       "adFRPerformDayPVCBurstTx": adFRPerformDayPVCBurstTx,
       "adFRPerformDayPVCBurstRx": adFRPerformDayPVCBurstRx,
       "adFRPerformDayPVCFecnRx": adFRPerformDayPVCFecnRx,
       "adFRPerformDayPVCFecnTx": adFRPerformDayPVCFecnTx,
       "adFRPerformDayPVCBecnRx": adFRPerformDayPVCBecnRx,
       "adFRPerformDayPVCBecnTx": adFRPerformDayPVCBecnTx,
       "adFRPerformDayPVCDeRx": adFRPerformDayPVCDeRx,
       "adFRPerformDayPVCDeTx": adFRPerformDayPVCDeTx,
       "adFRPerformDayPVCCrRx": adFRPerformDayPVCCrRx,
       "adFRPerformDayPVCCrTx": adFRPerformDayPVCCrTx,
       "adFRPerformDayPVCMinFrameSizeRx": adFRPerformDayPVCMinFrameSizeRx,
       "adFRPerformDayPVCMinFrameSizeTx": adFRPerformDayPVCMinFrameSizeTx,
       "adFRPerformDayPVCMaxFrameSizeRx": adFRPerformDayPVCMaxFrameSizeRx,
       "adFRPerformDayPVCMaxFrameSizeTx": adFRPerformDayPVCMaxFrameSizeTx,
       "adFRPerformDayPVCAvgFrameSizeRx": adFRPerformDayPVCAvgFrameSizeRx,
       "adFRPerformDayPVCAvgFrameSizeTx": adFRPerformDayPVCAvgFrameSizeTx,
       "adFRPerformDayPVCLostFrames": adFRPerformDayPVCLostFrames,
       "adFRPerformDayPVCRemoteLostFrames": adFRPerformDayPVCRemoteLostFrames,
       "adFRPerformDayPVCMaxDelay": adFRPerformDayPVCMaxDelay,
       "adFRPerformDayPVCMinDelay": adFRPerformDayPVCMinDelay,
       "adFRPerformDayPVCAvgDelay": adFRPerformDayPVCAvgDelay,
       "adFRPerformDayPVCTimeInDBU": adFRPerformDayPVCTimeInDBU,
       "adFRPerformDayPortStatus": adFRPerformDayPortStatus,
       "adFRPerformDayPortStatusTable": adFRPerformDayPortStatusTable,
       "adFRPerformDayPortStatusEntry": adFRPerformDayPortStatusEntry,
       "adFRPerformDayIfIndex": adFRPerformDayIfIndex,
       "adFRPerformDayPortSlotIndex": adFRPerformDayPortSlotIndex,
       "adFRPerformDayPortFramesRx": adFRPerformDayPortFramesRx,
       "adFRPerformDayPortFramesTx": adFRPerformDayPortFramesTx,
       "adFRPerformDayPortBytesRx": adFRPerformDayPortBytesRx,
       "adFRPerformDayPortBytesTx": adFRPerformDayPortBytesTx,
       "adFRPerformDayPortAvgThruputTx": adFRPerformDayPortAvgThruputTx,
       "adFRPerformDayPortAvgThruputRx": adFRPerformDayPortAvgThruputRx,
       "adFRPerformDayPortMaxThruputTx": adFRPerformDayPortMaxThruputTx,
       "adFRPerformDayPortMaxThruputRx": adFRPerformDayPortMaxThruputRx,
       "adFRPerformDayPortAvgUtilizationTx": adFRPerformDayPortAvgUtilizationTx,
       "adFRPerformDayPortAvgUtilizationRx": adFRPerformDayPortAvgUtilizationRx,
       "adFRPerformDayPortMaxUtilizationTx": adFRPerformDayPortMaxUtilizationTx,
       "adFRPerformDayPortMaxUtilizationRx": adFRPerformDayPortMaxUtilizationRx,
       "adFRPerformDayPortFullStatusRX": adFRPerformDayPortFullStatusRX,
       "adFRPerformDayPortFullStatusTx": adFRPerformDayPortFullStatusTx,
       "adFRPerformDayPortLIOnlyRX": adFRPerformDayPortLIOnlyRX,
       "adFRPerformDayPortLIOnlyTx": adFRPerformDayPortLIOnlyTx,
       "adFRPerformDayPortAsyncStatusFrame": adFRPerformDayPortAsyncStatusFrame,
       "adFRPerformDayPortError": adFRPerformDayPortError,
       "adFRPerformDayPortErrorTable": adFRPerformDayPortErrorTable,
       "adFRPerformDayPortErrorEntry": adFRPerformDayPortErrorEntry,
       "adFRPerformDayPortIndex": adFRPerformDayPortIndex,
       "adFRPerformDayPortErrorSlotIndex": adFRPerformDayPortErrorSlotIndex,
       "adFRPerformDayPortUnavailableTime": adFRPerformDayPortUnavailableTime,
       "adFRPerformDayCrcErrors": adFRPerformDayCrcErrors,
       "adFRPerformDayAbortFrames": adFRPerformDayAbortFrames,
       "adFRPerformDayOctectViolations": adFRPerformDayOctectViolations,
       "adFRPerformDayDiscardFrames": adFRPerformDayDiscardFrames,
       "adFRPerformDayLengthErrors": adFRPerformDayLengthErrors,
       "adFRPerformDayEAViolations": adFRPerformDayEAViolations,
       "adFRPerformDayEncapsulationErrors": adFRPerformDayEncapsulationErrors,
       "adFRPerformDayInactiveDLCI": adFRPerformDayInactiveDLCI,
       "adFRPerformDayInvalidDLCI": adFRPerformDayInvalidDLCI,
       "adFRPerformDayUnroutable": adFRPerformDayUnroutable,
       "adFRPerformDaySignalDownTime": adFRPerformDaySignalDownTime,
       "adFRPerformDaySignalErrors": adFRPerformDaySignalErrors,
       "adFRPerformDaySignalTimeOut": adFRPerformDaySignalTimeOut,
       "adFRPerformDaySignalStateChange": adFRPerformDaySignalStateChange,
       "adFRPerformDayHistoryTime": adFRPerformDayHistoryTime,
       "adFRPerformDayHistoryTimeTable": adFRPerformDayHistoryTimeTable,
       "adFRPerformDayHistoryTimeEntry": adFRPerformDayHistoryTimeEntry,
       "adFRPerformDayHistoryTimeSlotIndex": adFRPerformDayHistoryTimeSlotIndex,
       "adFRPerformDayHistorySlotTotalTime": adFRPerformDayHistorySlotTotalTime,
       "adFRPerformDayHistoryTimeStamp": adFRPerformDayHistoryTimeStamp}
)
