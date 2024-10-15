# SNMP MIB module (ADTRAN-ATLAS-V35NX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADTRAN-ATLAS-V35NX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:27 2024
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

(adATLASModuleInfoFPStatus,) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-MODULE-MIB",
    "adATLASModuleInfoFPStatus")

(adATLASUnitFPStatus,
 adATLASUnitPortAddress,
 adATLASUnitSlotAddress) = mibBuilder.importSymbols(
    "ADTRAN-ATLAS-UNIT-MIB",
    "adATLASUnitFPStatus",
    "adATLASUnitPortAddress",
    "adATLASUnitSlotAddress")

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

_Adtran_ObjectIdentity = ObjectIdentity
adtran = _Adtran_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664)
)
_AdMgmt_ObjectIdentity = ObjectIdentity
adMgmt = _AdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2)
)
_AdATLASmg_ObjectIdentity = ObjectIdentity
adATLASmg = _AdATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154)
)
_AdGenATLASmg_ObjectIdentity = ObjectIdentity
adGenATLASmg = _AdGenATLASmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1)
)
_AdATLASV35Nxmg_ObjectIdentity = ObjectIdentity
adATLASV35Nxmg = _AdATLASV35Nxmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7)
)
_AdATLASV35NxIfNumber_Type = Integer32
_AdATLASV35NxIfNumber_Object = MibScalar
adATLASV35NxIfNumber = _AdATLASV35NxIfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 1),
    _AdATLASV35NxIfNumber_Type()
)
adATLASV35NxIfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfNumber.setStatus("mandatory")
_AdATLASV35NxIfTable_Object = MibTable
adATLASV35NxIfTable = _AdATLASV35NxIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2)
)
if mibBuilder.loadTexts:
    adATLASV35NxIfTable.setStatus("mandatory")
_AdATLASV35NxIfEntry_Object = MibTableRow
adATLASV35NxIfEntry = _AdATLASV35NxIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1)
)
adATLASV35NxIfEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfIndex"),
)
if mibBuilder.loadTexts:
    adATLASV35NxIfEntry.setStatus("mandatory")
_AdATLASV35NxIfIndex_Type = Integer32
_AdATLASV35NxIfIndex_Object = MibTableColumn
adATLASV35NxIfIndex = _AdATLASV35NxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 1),
    _AdATLASV35NxIfIndex_Type()
)
adATLASV35NxIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfIndex.setStatus("mandatory")
_AdATLASV35NxIfSlotNum_Type = Integer32
_AdATLASV35NxIfSlotNum_Object = MibTableColumn
adATLASV35NxIfSlotNum = _AdATLASV35NxIfSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 2),
    _AdATLASV35NxIfSlotNum_Type()
)
adATLASV35NxIfSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfSlotNum.setStatus("mandatory")
_AdATLASV35NxIfPortNum_Type = Integer32
_AdATLASV35NxIfPortNum_Object = MibTableColumn
adATLASV35NxIfPortNum = _AdATLASV35NxIfPortNum_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 3),
    _AdATLASV35NxIfPortNum_Type()
)
adATLASV35NxIfPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfPortNum.setStatus("mandatory")


class _AdATLASV35NxIfAlarmStatus_Type(Integer32):
    """Custom type adATLASV35NxIfAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AdATLASV35NxIfAlarmStatus_Type.__name__ = "Integer32"
_AdATLASV35NxIfAlarmStatus_Object = MibTableColumn
adATLASV35NxIfAlarmStatus = _AdATLASV35NxIfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 4),
    _AdATLASV35NxIfAlarmStatus_Type()
)
adATLASV35NxIfAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfAlarmStatus.setStatus("mandatory")


class _AdATLASV35NxIfDTEStatus_Type(Integer32):
    """Custom type adATLASV35NxIfDTEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AdATLASV35NxIfDTEStatus_Type.__name__ = "Integer32"
_AdATLASV35NxIfDTEStatus_Object = MibTableColumn
adATLASV35NxIfDTEStatus = _AdATLASV35NxIfDTEStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 5),
    _AdATLASV35NxIfDTEStatus_Type()
)
adATLASV35NxIfDTEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfDTEStatus.setStatus("mandatory")
_AdATLASV35NxIfDataRate_Type = Gauge32
_AdATLASV35NxIfDataRate_Object = MibTableColumn
adATLASV35NxIfDataRate = _AdATLASV35NxIfDataRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 6),
    _AdATLASV35NxIfDataRate_Type()
)
adATLASV35NxIfDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfDataRate.setStatus("mandatory")


class _AdATLASV35NxIfPLLFifoStatus_Type(Integer32):
    """Custom type adATLASV35NxIfPLLFifoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AdATLASV35NxIfPLLFifoStatus_Type.__name__ = "Integer32"
_AdATLASV35NxIfPLLFifoStatus_Object = MibTableColumn
adATLASV35NxIfPLLFifoStatus = _AdATLASV35NxIfPLLFifoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 2, 1, 7),
    _AdATLASV35NxIfPLLFifoStatus_Type()
)
adATLASV35NxIfPLLFifoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfPLLFifoStatus.setStatus("mandatory")
_AdATLASV35NxIfInbandStatTable_Object = MibTable
adATLASV35NxIfInbandStatTable = _AdATLASV35NxIfInbandStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3)
)
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatTable.setStatus("mandatory")
_AdATLASV35NxIfInbandStatEntry_Object = MibTableRow
adATLASV35NxIfInbandStatEntry = _AdATLASV35NxIfInbandStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1)
)
adATLASV35NxIfInbandStatEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfInbandStatIndex"),
)
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatEntry.setStatus("mandatory")
_AdATLASV35NxIfInbandStatIndex_Type = Integer32
_AdATLASV35NxIfInbandStatIndex_Object = MibTableColumn
adATLASV35NxIfInbandStatIndex = _AdATLASV35NxIfInbandStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 1),
    _AdATLASV35NxIfInbandStatIndex_Type()
)
adATLASV35NxIfInbandStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatIndex.setStatus("mandatory")
_AdATLASV35NxIfInbandStatRxFrames_Type = Counter32
_AdATLASV35NxIfInbandStatRxFrames_Object = MibTableColumn
adATLASV35NxIfInbandStatRxFrames = _AdATLASV35NxIfInbandStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 2),
    _AdATLASV35NxIfInbandStatRxFrames_Type()
)
adATLASV35NxIfInbandStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatRxFrames.setStatus("mandatory")
_AdATLASV35NxIfInbandStatTxFrames_Type = Counter32
_AdATLASV35NxIfInbandStatTxFrames_Object = MibTableColumn
adATLASV35NxIfInbandStatTxFrames = _AdATLASV35NxIfInbandStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 3),
    _AdATLASV35NxIfInbandStatTxFrames_Type()
)
adATLASV35NxIfInbandStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatTxFrames.setStatus("mandatory")
_AdATLASV35NxIfInbandStatRxBytes_Type = Counter32
_AdATLASV35NxIfInbandStatRxBytes_Object = MibTableColumn
adATLASV35NxIfInbandStatRxBytes = _AdATLASV35NxIfInbandStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 4),
    _AdATLASV35NxIfInbandStatRxBytes_Type()
)
adATLASV35NxIfInbandStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatRxBytes.setStatus("mandatory")
_AdATLASV35NxIfInbandStatTxBytes_Type = Counter32
_AdATLASV35NxIfInbandStatTxBytes_Object = MibTableColumn
adATLASV35NxIfInbandStatTxBytes = _AdATLASV35NxIfInbandStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 5),
    _AdATLASV35NxIfInbandStatTxBytes_Type()
)
adATLASV35NxIfInbandStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatTxBytes.setStatus("mandatory")


class _AdATLASV35NxIfInbandStatReset_Type(Integer32):
    """Custom type adATLASV35NxIfInbandStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetStats", 1)
    )


_AdATLASV35NxIfInbandStatReset_Type.__name__ = "Integer32"
_AdATLASV35NxIfInbandStatReset_Object = MibTableColumn
adATLASV35NxIfInbandStatReset = _AdATLASV35NxIfInbandStatReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 3, 1, 6),
    _AdATLASV35NxIfInbandStatReset_Type()
)
adATLASV35NxIfInbandStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASV35NxIfInbandStatReset.setStatus("mandatory")
_AdATLASV35NxTstTable_Object = MibTable
adATLASV35NxTstTable = _AdATLASV35NxTstTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4)
)
if mibBuilder.loadTexts:
    adATLASV35NxTstTable.setStatus("mandatory")
_AdATLASV35NxTstEntry_Object = MibTableRow
adATLASV35NxTstEntry = _AdATLASV35NxTstEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1)
)
adATLASV35NxTstEntry.setIndexNames(
    (0, "ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxTstIndex"),
)
if mibBuilder.loadTexts:
    adATLASV35NxTstEntry.setStatus("mandatory")
_AdATLASV35NxTstIndex_Type = Integer32
_AdATLASV35NxTstIndex_Object = MibTableColumn
adATLASV35NxTstIndex = _AdATLASV35NxTstIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 1),
    _AdATLASV35NxTstIndex_Type()
)
adATLASV35NxTstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxTstIndex.setStatus("mandatory")


class _AdATLASV35NxTstLoopbk_Type(Integer32):
    """Custom type adATLASV35NxTstLoopbk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLpBk", 2),
          ("noLpBk", 1),
          ("remoteLpBk", 3))
    )


_AdATLASV35NxTstLoopbk_Type.__name__ = "Integer32"
_AdATLASV35NxTstLoopbk_Object = MibTableColumn
adATLASV35NxTstLoopbk = _AdATLASV35NxTstLoopbk_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 2),
    _AdATLASV35NxTstLoopbk_Type()
)
adATLASV35NxTstLoopbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASV35NxTstLoopbk.setStatus("mandatory")


class _AdATLASV35NxTstLoopbkStatus_Type(Integer32):
    """Custom type adATLASV35NxTstLoopbkStatus based on Integer32"""
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
        *(("inactive", 1),
          ("loopbkActive", 7),
          ("loopedFromRmt", 6),
          ("loopingDownRmt", 4),
          ("loopingUpRmt", 2),
          ("rmtLoopFailed", 5),
          ("rmtLooped", 3))
    )


_AdATLASV35NxTstLoopbkStatus_Type.__name__ = "Integer32"
_AdATLASV35NxTstLoopbkStatus_Object = MibTableColumn
adATLASV35NxTstLoopbkStatus = _AdATLASV35NxTstLoopbkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 3),
    _AdATLASV35NxTstLoopbkStatus_Type()
)
adATLASV35NxTstLoopbkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxTstLoopbkStatus.setStatus("mandatory")


class _AdATLASV35NxTst511Pattern_Type(Integer32):
    """Custom type adATLASV35NxTst511Pattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AdATLASV35NxTst511Pattern_Type.__name__ = "Integer32"
_AdATLASV35NxTst511Pattern_Object = MibTableColumn
adATLASV35NxTst511Pattern = _AdATLASV35NxTst511Pattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 4),
    _AdATLASV35NxTst511Pattern_Type()
)
adATLASV35NxTst511Pattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASV35NxTst511Pattern.setStatus("mandatory")


class _AdATLASV35NxTstPatternSync_Type(Integer32):
    """Custom type adATLASV35NxTstPatternSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSync", 2),
          ("synced", 1))
    )


_AdATLASV35NxTstPatternSync_Type.__name__ = "Integer32"
_AdATLASV35NxTstPatternSync_Object = MibTableColumn
adATLASV35NxTstPatternSync = _AdATLASV35NxTstPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 5),
    _AdATLASV35NxTstPatternSync_Type()
)
adATLASV35NxTstPatternSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxTstPatternSync.setStatus("mandatory")


class _AdATLASV35NxTstPatternSyncLost_Type(Integer32):
    """Custom type adATLASV35NxTstPatternSyncLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syncLost", 1),
          ("syncNotLost", 2))
    )


_AdATLASV35NxTstPatternSyncLost_Type.__name__ = "Integer32"
_AdATLASV35NxTstPatternSyncLost_Object = MibTableColumn
adATLASV35NxTstPatternSyncLost = _AdATLASV35NxTstPatternSyncLost_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 6),
    _AdATLASV35NxTstPatternSyncLost_Type()
)
adATLASV35NxTstPatternSyncLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxTstPatternSyncLost.setStatus("mandatory")
_AdATLASV35NxTstPatternESs_Type = Counter32
_AdATLASV35NxTstPatternESs_Object = MibTableColumn
adATLASV35NxTstPatternESs = _AdATLASV35NxTstPatternESs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 7),
    _AdATLASV35NxTstPatternESs_Type()
)
adATLASV35NxTstPatternESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adATLASV35NxTstPatternESs.setStatus("mandatory")


class _AdATLASV35NxTstInjectErrs_Type(Integer32):
    """Custom type adATLASV35NxTstInjectErrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("injectError", 1)
    )


_AdATLASV35NxTstInjectErrs_Type.__name__ = "Integer32"
_AdATLASV35NxTstInjectErrs_Object = MibTableColumn
adATLASV35NxTstInjectErrs = _AdATLASV35NxTstInjectErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 8),
    _AdATLASV35NxTstInjectErrs_Type()
)
adATLASV35NxTstInjectErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASV35NxTstInjectErrs.setStatus("mandatory")


class _AdATLASV35NxTstClearRslts_Type(Integer32):
    """Custom type adATLASV35NxTstClearRslts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearResults", 1)
    )


_AdATLASV35NxTstClearRslts_Type.__name__ = "Integer32"
_AdATLASV35NxTstClearRslts_Object = MibTableColumn
adATLASV35NxTstClearRslts = _AdATLASV35NxTstClearRslts_Object(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 1, 7, 4, 1, 9),
    _AdATLASV35NxTstClearRslts_Type()
)
adATLASV35NxTstClearRslts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adATLASV35NxTstClearRslts.setStatus("mandatory")

# Managed Objects groups


# Notification objects

adATLASV35NxSlipAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400700)
)
adATLASV35NxSlipAlarmActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxSlipAlarmActive.setStatus(
        ""
    )

adATLASV35NxSlipAlarmInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400701)
)
adATLASV35NxSlipAlarmInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxSlipAlarmInActive.setStatus(
        ""
    )

adATLASV35NxPLLAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400702)
)
adATLASV35NxPLLAlarmActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxPLLAlarmActive.setStatus(
        ""
    )

adATLASV35NxPLLAlarmInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400703)
)
adATLASV35NxPLLAlarmInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxPLLAlarmInActive.setStatus(
        ""
    )

adATLASV35NxZeroAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400704)
)
adATLASV35NxZeroAlarmActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxZeroAlarmActive.setStatus(
        ""
    )

adATLASV35NxZeroAlarmInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400705)
)
adATLASV35NxZeroAlarmInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxZeroAlarmInActive.setStatus(
        ""
    )

adATLASV35NxExtClkAlarmActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400706)
)
adATLASV35NxExtClkAlarmActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxExtClkAlarmActive.setStatus(
        ""
    )

adATLASV35NxExtClkAlarmInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400707)
)
adATLASV35NxExtClkAlarmInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfAlarmStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxExtClkAlarmInActive.setStatus(
        ""
    )

adATLASV35NxRTSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400708)
)
adATLASV35NxRTSActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRTSActive.setStatus(
        ""
    )

adATLASV35NxRTSInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400709)
)
adATLASV35NxRTSInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRTSInActive.setStatus(
        ""
    )

adATLASV35NxCTSActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400710)
)
adATLASV35NxCTSActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxCTSActive.setStatus(
        ""
    )

adATLASV35NxCTSInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400711)
)
adATLASV35NxCTSInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxCTSInActive.setStatus(
        ""
    )

adATLASV35NxDTRActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400712)
)
adATLASV35NxDTRActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDTRActive.setStatus(
        ""
    )

adATLASV35NxDTRInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400713)
)
adATLASV35NxDTRInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDTRInActive.setStatus(
        ""
    )

adATLASV35NxDSRActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400714)
)
adATLASV35NxDSRActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDSRActive.setStatus(
        ""
    )

adATLASV35NxDSRInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400715)
)
adATLASV35NxDSRInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDSRInActive.setStatus(
        ""
    )

adATLASV35NxDCDActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400716)
)
adATLASV35NxDCDActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDCDActive.setStatus(
        ""
    )

adATLASV35NxDCDInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400717)
)
adATLASV35NxDCDInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxDCDInActive.setStatus(
        ""
    )

adATLASV35NxRIActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400718)
)
adATLASV35NxRIActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRIActive.setStatus(
        ""
    )

adATLASV35NxRIInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400719)
)
adATLASV35NxRIInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRIInActive.setStatus(
        ""
    )

adATLASV35NxTDActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400720)
)
adATLASV35NxTDActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxTDActive.setStatus(
        ""
    )

adATLASV35NxTDInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400721)
)
adATLASV35NxTDInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxTDInActive.setStatus(
        ""
    )

adATLASV35NxRDActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400722)
)
adATLASV35NxRDActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRDActive.setStatus(
        ""
    )

adATLASV35NxRDInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400723)
)
adATLASV35NxRDInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxRDInActive.setStatus(
        ""
    )

adATLASV35NxECActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400724)
)
adATLASV35NxECActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxECActive.setStatus(
        ""
    )

adATLASV35NxECInActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 2, 154, 0, 15400725)
)
adATLASV35NxECInActive.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitSlotAddress"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitPortAddress"),
        ("ADTRAN-ATLAS-MODULE-MIB", "adATLASModuleInfoFPStatus"),
        ("ADTRAN-ATLAS-UNIT-MIB", "adATLASUnitFPStatus"),
        ("ADTRAN-ATLAS-V35NX-MIB", "adATLASV35NxIfDTEStatus"))
)
if mibBuilder.loadTexts:
    adATLASV35NxECInActive.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-ATLAS-V35NX-MIB",
    **{"adtran": adtran,
       "adMgmt": adMgmt,
       "adATLASmg": adATLASmg,
       "adATLASV35NxSlipAlarmActive": adATLASV35NxSlipAlarmActive,
       "adATLASV35NxSlipAlarmInActive": adATLASV35NxSlipAlarmInActive,
       "adATLASV35NxPLLAlarmActive": adATLASV35NxPLLAlarmActive,
       "adATLASV35NxPLLAlarmInActive": adATLASV35NxPLLAlarmInActive,
       "adATLASV35NxZeroAlarmActive": adATLASV35NxZeroAlarmActive,
       "adATLASV35NxZeroAlarmInActive": adATLASV35NxZeroAlarmInActive,
       "adATLASV35NxExtClkAlarmActive": adATLASV35NxExtClkAlarmActive,
       "adATLASV35NxExtClkAlarmInActive": adATLASV35NxExtClkAlarmInActive,
       "adATLASV35NxRTSActive": adATLASV35NxRTSActive,
       "adATLASV35NxRTSInActive": adATLASV35NxRTSInActive,
       "adATLASV35NxCTSActive": adATLASV35NxCTSActive,
       "adATLASV35NxCTSInActive": adATLASV35NxCTSInActive,
       "adATLASV35NxDTRActive": adATLASV35NxDTRActive,
       "adATLASV35NxDTRInActive": adATLASV35NxDTRInActive,
       "adATLASV35NxDSRActive": adATLASV35NxDSRActive,
       "adATLASV35NxDSRInActive": adATLASV35NxDSRInActive,
       "adATLASV35NxDCDActive": adATLASV35NxDCDActive,
       "adATLASV35NxDCDInActive": adATLASV35NxDCDInActive,
       "adATLASV35NxRIActive": adATLASV35NxRIActive,
       "adATLASV35NxRIInActive": adATLASV35NxRIInActive,
       "adATLASV35NxTDActive": adATLASV35NxTDActive,
       "adATLASV35NxTDInActive": adATLASV35NxTDInActive,
       "adATLASV35NxRDActive": adATLASV35NxRDActive,
       "adATLASV35NxRDInActive": adATLASV35NxRDInActive,
       "adATLASV35NxECActive": adATLASV35NxECActive,
       "adATLASV35NxECInActive": adATLASV35NxECInActive,
       "adGenATLASmg": adGenATLASmg,
       "adATLASV35Nxmg": adATLASV35Nxmg,
       "adATLASV35NxIfNumber": adATLASV35NxIfNumber,
       "adATLASV35NxIfTable": adATLASV35NxIfTable,
       "adATLASV35NxIfEntry": adATLASV35NxIfEntry,
       "adATLASV35NxIfIndex": adATLASV35NxIfIndex,
       "adATLASV35NxIfSlotNum": adATLASV35NxIfSlotNum,
       "adATLASV35NxIfPortNum": adATLASV35NxIfPortNum,
       "adATLASV35NxIfAlarmStatus": adATLASV35NxIfAlarmStatus,
       "adATLASV35NxIfDTEStatus": adATLASV35NxIfDTEStatus,
       "adATLASV35NxIfDataRate": adATLASV35NxIfDataRate,
       "adATLASV35NxIfPLLFifoStatus": adATLASV35NxIfPLLFifoStatus,
       "adATLASV35NxIfInbandStatTable": adATLASV35NxIfInbandStatTable,
       "adATLASV35NxIfInbandStatEntry": adATLASV35NxIfInbandStatEntry,
       "adATLASV35NxIfInbandStatIndex": adATLASV35NxIfInbandStatIndex,
       "adATLASV35NxIfInbandStatRxFrames": adATLASV35NxIfInbandStatRxFrames,
       "adATLASV35NxIfInbandStatTxFrames": adATLASV35NxIfInbandStatTxFrames,
       "adATLASV35NxIfInbandStatRxBytes": adATLASV35NxIfInbandStatRxBytes,
       "adATLASV35NxIfInbandStatTxBytes": adATLASV35NxIfInbandStatTxBytes,
       "adATLASV35NxIfInbandStatReset": adATLASV35NxIfInbandStatReset,
       "adATLASV35NxTstTable": adATLASV35NxTstTable,
       "adATLASV35NxTstEntry": adATLASV35NxTstEntry,
       "adATLASV35NxTstIndex": adATLASV35NxTstIndex,
       "adATLASV35NxTstLoopbk": adATLASV35NxTstLoopbk,
       "adATLASV35NxTstLoopbkStatus": adATLASV35NxTstLoopbkStatus,
       "adATLASV35NxTst511Pattern": adATLASV35NxTst511Pattern,
       "adATLASV35NxTstPatternSync": adATLASV35NxTstPatternSync,
       "adATLASV35NxTstPatternSyncLost": adATLASV35NxTstPatternSyncLost,
       "adATLASV35NxTstPatternESs": adATLASV35NxTstPatternESs,
       "adATLASV35NxTstInjectErrs": adATLASV35NxTstInjectErrs,
       "adATLASV35NxTstClearRslts": adATLASV35NxTstClearRslts}
)
