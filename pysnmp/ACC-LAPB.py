# SNMP MIB module (ACC-LAPB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-LAPB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:30 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccLapb_ObjectIdentity = ObjectIdentity
accLapb = _AccLapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7)
)
_AccLapbNum_Type = Integer32
_AccLapbNum_Object = MibScalar
accLapbNum = _AccLapbNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 1),
    _AccLapbNum_Type()
)
accLapbNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbNum.setStatus("mandatory")
_AccLapbParmTable_Object = MibTable
accLapbParmTable = _AccLapbParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    accLapbParmTable.setStatus("mandatory")
_AccLapbParmEntry_Object = MibTableRow
accLapbParmEntry = _AccLapbParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1)
)
accLapbParmEntry.setIndexNames(
    (0, "ACC-LAPB", "accLapbIndex"),
)
if mibBuilder.loadTexts:
    accLapbParmEntry.setStatus("mandatory")
_AccLapbIndex_Type = Integer32
_AccLapbIndex_Object = MibTableColumn
accLapbIndex = _AccLapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 1),
    _AccLapbIndex_Type()
)
accLapbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbIndex.setStatus("mandatory")


class _AccLapbType_Type(Integer32):
    """Custom type accLapbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 0))
    )


_AccLapbType_Type.__name__ = "Integer32"
_AccLapbType_Object = MibTableColumn
accLapbType = _AccLapbType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 2),
    _AccLapbType_Type()
)
accLapbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbType.setStatus("mandatory")


class _AccLapbT1Timer_Type(Integer32):
    """Custom type accLapbT1Timer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_AccLapbT1Timer_Type.__name__ = "Integer32"
_AccLapbT1Timer_Object = MibTableColumn
accLapbT1Timer = _AccLapbT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 3),
    _AccLapbT1Timer_Type()
)
accLapbT1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbT1Timer.setStatus("mandatory")


class _AccLapbN2Count_Type(Integer32):
    """Custom type accLapbN2Count based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_AccLapbN2Count_Type.__name__ = "Integer32"
_AccLapbN2Count_Object = MibTableColumn
accLapbN2Count = _AccLapbN2Count_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 4),
    _AccLapbN2Count_Type()
)
accLapbN2Count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbN2Count.setStatus("mandatory")


class _AccLapbFrameWindow_Type(Integer32):
    """Custom type accLapbFrameWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccLapbFrameWindow_Type.__name__ = "Integer32"
_AccLapbFrameWindow_Object = MibTableColumn
accLapbFrameWindow = _AccLapbFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 5),
    _AccLapbFrameWindow_Type()
)
accLapbFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbFrameWindow.setStatus("mandatory")


class _AccLapbFlags_Type(Integer32):
    """Custom type accLapbFlags based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccLapbFlags_Type.__name__ = "Integer32"
_AccLapbFlags_Object = MibTableColumn
accLapbFlags = _AccLapbFlags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 6),
    _AccLapbFlags_Type()
)
accLapbFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbFlags.setStatus("mandatory")


class _AccHdlcRrPolling_Type(Integer32):
    """Custom type accHdlcRrPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_AccHdlcRrPolling_Type.__name__ = "Integer32"
_AccHdlcRrPolling_Object = MibTableColumn
accHdlcRrPolling = _AccHdlcRrPolling_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 7),
    _AccHdlcRrPolling_Type()
)
accHdlcRrPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcRrPolling.setStatus("mandatory")


class _AccHdlcFCS_Type(Integer32):
    """Custom type accHdlcFCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccitt-16", 1),
          ("ccitt-32", 2))
    )


_AccHdlcFCS_Type.__name__ = "Integer32"
_AccHdlcFCS_Object = MibTableColumn
accHdlcFCS = _AccHdlcFCS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 8),
    _AccHdlcFCS_Type()
)
accHdlcFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcFCS.setStatus("mandatory")


class _AccHdlcCoding_Type(Integer32):
    """Custom type accHdlcCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 0),
          ("nrzi", 1))
    )


_AccHdlcCoding_Type.__name__ = "Integer32"
_AccHdlcCoding_Object = MibTableColumn
accHdlcCoding = _AccHdlcCoding_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 9),
    _AccHdlcCoding_Type()
)
accHdlcCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcCoding.setStatus("mandatory")


class _AccHdlcDuplex_Type(Integer32):
    """Custom type accHdlcDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("half", 1))
    )


_AccHdlcDuplex_Type.__name__ = "Integer32"
_AccHdlcDuplex_Object = MibTableColumn
accHdlcDuplex = _AccHdlcDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 10),
    _AccHdlcDuplex_Type()
)
accHdlcDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcDuplex.setStatus("mandatory")


class _AccHdlcIdleFill_Type(Integer32):
    """Custom type accHdlcIdleFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flags", 1),
          ("ones", 2))
    )


_AccHdlcIdleFill_Type.__name__ = "Integer32"
_AccHdlcIdleFill_Object = MibTableColumn
accHdlcIdleFill = _AccHdlcIdleFill_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 11),
    _AccHdlcIdleFill_Type()
)
accHdlcIdleFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcIdleFill.setStatus("mandatory")
_AccLapbStatTable_Object = MibTable
accLapbStatTable = _AccLapbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    accLapbStatTable.setStatus("mandatory")
_AccLapbStatEntry_Object = MibTableRow
accLapbStatEntry = _AccLapbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1)
)
accLapbStatEntry.setIndexNames(
    (0, "ACC-LAPB", "accLapbStatIndex"),
)
if mibBuilder.loadTexts:
    accLapbStatEntry.setStatus("mandatory")
_AccLapbStatIndex_Type = Integer32
_AccLapbStatIndex_Object = MibTableColumn
accLapbStatIndex = _AccLapbStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 1),
    _AccLapbStatIndex_Type()
)
accLapbStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatIndex.setStatus("mandatory")
_AccLapbStatBadFCSIns_Type = Counter32
_AccLapbStatBadFCSIns_Object = MibTableColumn
accLapbStatBadFCSIns = _AccLapbStatBadFCSIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 2),
    _AccLapbStatBadFCSIns_Type()
)
accLapbStatBadFCSIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatBadFCSIns.setStatus("mandatory")
_AccLapbStatFRMRIns_Type = Counter32
_AccLapbStatFRMRIns_Object = MibTableColumn
accLapbStatFRMRIns = _AccLapbStatFRMRIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 3),
    _AccLapbStatFRMRIns_Type()
)
accLapbStatFRMRIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatFRMRIns.setStatus("mandatory")
_AccLapbStatT1Timeouts_Type = Counter32
_AccLapbStatT1Timeouts_Object = MibTableColumn
accLapbStatT1Timeouts = _AccLapbStatT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 4),
    _AccLapbStatT1Timeouts_Type()
)
accLapbStatT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatT1Timeouts.setStatus("mandatory")
_AccLapbStatREJIns_Type = Counter32
_AccLapbStatREJIns_Object = MibTableColumn
accLapbStatREJIns = _AccLapbStatREJIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 5),
    _AccLapbStatREJIns_Type()
)
accLapbStatREJIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatREJIns.setStatus("mandatory")
_AccLapbStatREJOuts_Type = Counter32
_AccLapbStatREJOuts_Object = MibTableColumn
accLapbStatREJOuts = _AccLapbStatREJOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 6),
    _AccLapbStatREJOuts_Type()
)
accLapbStatREJOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatREJOuts.setStatus("mandatory")
_AccLapbStatShortIns_Type = Counter32
_AccLapbStatShortIns_Object = MibTableColumn
accLapbStatShortIns = _AccLapbStatShortIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 7),
    _AccLapbStatShortIns_Type()
)
accLapbStatShortIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatShortIns.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-LAPB",
    **{"accLapb": accLapb,
       "accLapbNum": accLapbNum,
       "accLapbParmTable": accLapbParmTable,
       "accLapbParmEntry": accLapbParmEntry,
       "accLapbIndex": accLapbIndex,
       "accLapbType": accLapbType,
       "accLapbT1Timer": accLapbT1Timer,
       "accLapbN2Count": accLapbN2Count,
       "accLapbFrameWindow": accLapbFrameWindow,
       "accLapbFlags": accLapbFlags,
       "accHdlcRrPolling": accHdlcRrPolling,
       "accHdlcFCS": accHdlcFCS,
       "accHdlcCoding": accHdlcCoding,
       "accHdlcDuplex": accHdlcDuplex,
       "accHdlcIdleFill": accHdlcIdleFill,
       "accLapbStatTable": accLapbStatTable,
       "accLapbStatEntry": accLapbStatEntry,
       "accLapbStatIndex": accLapbStatIndex,
       "accLapbStatBadFCSIns": accLapbStatBadFCSIns,
       "accLapbStatFRMRIns": accLapbStatFRMRIns,
       "accLapbStatT1Timeouts": accLapbStatT1Timeouts,
       "accLapbStatREJIns": accLapbStatREJIns,
       "accLapbStatREJOuts": accLapbStatREJOuts,
       "accLapbStatShortIns": accLapbStatShortIns}
)
