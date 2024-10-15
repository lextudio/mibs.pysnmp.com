# SNMP MIB module (UCD-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UCD-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:37 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ucdavis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2021)
)
ucdavis.setRevisions(
        ("2016-06-10 00:00",
         "2014-07-31 00:00",
         "2011-05-14 00:00",
         "2009-01-19 00:00",
         "2006-11-22 00:00",
         "2004-04-07 00:00",
         "2002-09-05 00:00",
         "2001-09-20 00:00",
         "2001-01-17 00:00",
         "1999-12-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



class UCDErrorFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("noError", 0))
    )



class UCDErrorFix(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("runFix", 1))
    )



# MIB Managed Objects in the order of their OIDs

_PrTable_Object = MibTable
prTable = _PrTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2)
)
if mibBuilder.loadTexts:
    prTable.setStatus("current")
_PrEntry_Object = MibTableRow
prEntry = _PrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1)
)
prEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "prIndex"),
)
if mibBuilder.loadTexts:
    prEntry.setStatus("current")


class _PrIndex_Type(Integer32):
    """Custom type prIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrIndex_Type.__name__ = "Integer32"
_PrIndex_Object = MibTableColumn
prIndex = _PrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 1),
    _PrIndex_Type()
)
prIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prIndex.setStatus("current")
_PrNames_Type = DisplayString
_PrNames_Object = MibTableColumn
prNames = _PrNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 2),
    _PrNames_Type()
)
prNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prNames.setStatus("current")
_PrMin_Type = Integer32
_PrMin_Object = MibTableColumn
prMin = _PrMin_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 3),
    _PrMin_Type()
)
prMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMin.setStatus("current")
_PrMax_Type = Integer32
_PrMax_Object = MibTableColumn
prMax = _PrMax_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 4),
    _PrMax_Type()
)
prMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMax.setStatus("current")
_PrCount_Type = Integer32
_PrCount_Object = MibTableColumn
prCount = _PrCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 5),
    _PrCount_Type()
)
prCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prCount.setStatus("current")
_PrErrorFlag_Type = UCDErrorFlag
_PrErrorFlag_Object = MibTableColumn
prErrorFlag = _PrErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 100),
    _PrErrorFlag_Type()
)
prErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrorFlag.setStatus("current")
_PrErrMessage_Type = DisplayString
_PrErrMessage_Object = MibTableColumn
prErrMessage = _PrErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 101),
    _PrErrMessage_Type()
)
prErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrMessage.setStatus("current")
_PrErrFix_Type = UCDErrorFix
_PrErrFix_Object = MibTableColumn
prErrFix = _PrErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 102),
    _PrErrFix_Type()
)
prErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prErrFix.setStatus("current")
_PrErrFixCmd_Type = DisplayString
_PrErrFixCmd_Object = MibTableColumn
prErrFixCmd = _PrErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 2021, 2, 1, 103),
    _PrErrFixCmd_Type()
)
prErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prErrFixCmd.setStatus("current")
_Memory_ObjectIdentity = ObjectIdentity
memory = _Memory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 4)
)
_MemIndex_Type = Integer32
_MemIndex_Object = MibScalar
memIndex = _MemIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 1),
    _MemIndex_Type()
)
memIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memIndex.setStatus("current")
_MemErrorName_Type = DisplayString
_MemErrorName_Object = MibScalar
memErrorName = _MemErrorName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 2),
    _MemErrorName_Type()
)
memErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memErrorName.setStatus("current")
_MemTotalSwap_Type = Integer32
_MemTotalSwap_Object = MibScalar
memTotalSwap = _MemTotalSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 3),
    _MemTotalSwap_Type()
)
memTotalSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwap.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwap.setUnits("kB")
_MemAvailSwap_Type = Integer32
_MemAvailSwap_Object = MibScalar
memAvailSwap = _MemAvailSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 4),
    _MemAvailSwap_Type()
)
memAvailSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwap.setStatus("current")
if mibBuilder.loadTexts:
    memAvailSwap.setUnits("kB")
_MemTotalReal_Type = Integer32
_MemTotalReal_Object = MibScalar
memTotalReal = _MemTotalReal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 5),
    _MemTotalReal_Type()
)
memTotalReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalReal.setStatus("current")
if mibBuilder.loadTexts:
    memTotalReal.setUnits("kB")
_MemAvailReal_Type = Integer32
_MemAvailReal_Object = MibScalar
memAvailReal = _MemAvailReal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 6),
    _MemAvailReal_Type()
)
memAvailReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailReal.setStatus("current")
if mibBuilder.loadTexts:
    memAvailReal.setUnits("kB")
_MemTotalSwapTXT_Type = Integer32
_MemTotalSwapTXT_Object = MibScalar
memTotalSwapTXT = _MemTotalSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 7),
    _MemTotalSwapTXT_Type()
)
memTotalSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwapTXT.setUnits("kB")
_MemAvailSwapTXT_Type = Integer32
_MemAvailSwapTXT_Object = MibScalar
memAvailSwapTXT = _MemAvailSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 8),
    _MemAvailSwapTXT_Type()
)
memAvailSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setStatus("deprecated")
if mibBuilder.loadTexts:
    memAvailSwapTXT.setUnits("kB")
_MemTotalRealTXT_Type = Integer32
_MemTotalRealTXT_Object = MibScalar
memTotalRealTXT = _MemTotalRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 9),
    _MemTotalRealTXT_Type()
)
memTotalRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalRealTXT.setStatus("current")
if mibBuilder.loadTexts:
    memTotalRealTXT.setUnits("kB")
_MemAvailRealTXT_Type = Integer32
_MemAvailRealTXT_Object = MibScalar
memAvailRealTXT = _MemAvailRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 10),
    _MemAvailRealTXT_Type()
)
memAvailRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailRealTXT.setStatus("deprecated")
if mibBuilder.loadTexts:
    memAvailRealTXT.setUnits("kB")
_MemTotalFree_Type = Integer32
_MemTotalFree_Object = MibScalar
memTotalFree = _MemTotalFree_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 11),
    _MemTotalFree_Type()
)
memTotalFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalFree.setStatus("current")
if mibBuilder.loadTexts:
    memTotalFree.setUnits("kB")
_MemMinimumSwap_Type = Integer32
_MemMinimumSwap_Object = MibScalar
memMinimumSwap = _MemMinimumSwap_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 12),
    _MemMinimumSwap_Type()
)
memMinimumSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMinimumSwap.setStatus("current")
if mibBuilder.loadTexts:
    memMinimumSwap.setUnits("kB")
_MemShared_Type = Integer32
_MemShared_Object = MibScalar
memShared = _MemShared_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 13),
    _MemShared_Type()
)
memShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memShared.setStatus("current")
if mibBuilder.loadTexts:
    memShared.setUnits("kB")
_MemBuffer_Type = Integer32
_MemBuffer_Object = MibScalar
memBuffer = _MemBuffer_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 14),
    _MemBuffer_Type()
)
memBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBuffer.setStatus("current")
if mibBuilder.loadTexts:
    memBuffer.setUnits("kB")
_MemCached_Type = Integer32
_MemCached_Object = MibScalar
memCached = _MemCached_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 15),
    _MemCached_Type()
)
memCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCached.setStatus("current")
if mibBuilder.loadTexts:
    memCached.setUnits("kB")
_MemUsedSwapTXT_Type = Integer32
_MemUsedSwapTXT_Object = MibScalar
memUsedSwapTXT = _MemUsedSwapTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 16),
    _MemUsedSwapTXT_Type()
)
memUsedSwapTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsedSwapTXT.setStatus("current")
if mibBuilder.loadTexts:
    memUsedSwapTXT.setUnits("kB")
_MemUsedRealTXT_Type = Integer32
_MemUsedRealTXT_Object = MibScalar
memUsedRealTXT = _MemUsedRealTXT_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 17),
    _MemUsedRealTXT_Type()
)
memUsedRealTXT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUsedRealTXT.setStatus("current")
if mibBuilder.loadTexts:
    memUsedRealTXT.setUnits("kB")
_MemTotalSwapX_Type = CounterBasedGauge64
_MemTotalSwapX_Object = MibScalar
memTotalSwapX = _MemTotalSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 18),
    _MemTotalSwapX_Type()
)
memTotalSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalSwapX.setUnits("kB")
_MemAvailSwapX_Type = CounterBasedGauge64
_MemAvailSwapX_Object = MibScalar
memAvailSwapX = _MemAvailSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 19),
    _MemAvailSwapX_Type()
)
memAvailSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memAvailSwapX.setUnits("kB")
_MemTotalRealX_Type = CounterBasedGauge64
_MemTotalRealX_Object = MibScalar
memTotalRealX = _MemTotalRealX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 20),
    _MemTotalRealX_Type()
)
memTotalRealX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalRealX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalRealX.setUnits("kB")
_MemAvailRealX_Type = CounterBasedGauge64
_MemAvailRealX_Object = MibScalar
memAvailRealX = _MemAvailRealX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 21),
    _MemAvailRealX_Type()
)
memAvailRealX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memAvailRealX.setStatus("current")
if mibBuilder.loadTexts:
    memAvailRealX.setUnits("kB")
_MemTotalFreeX_Type = CounterBasedGauge64
_MemTotalFreeX_Object = MibScalar
memTotalFreeX = _MemTotalFreeX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 22),
    _MemTotalFreeX_Type()
)
memTotalFreeX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memTotalFreeX.setStatus("current")
if mibBuilder.loadTexts:
    memTotalFreeX.setUnits("kB")
_MemMinimumSwapX_Type = CounterBasedGauge64
_MemMinimumSwapX_Object = MibScalar
memMinimumSwapX = _MemMinimumSwapX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 23),
    _MemMinimumSwapX_Type()
)
memMinimumSwapX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memMinimumSwapX.setStatus("current")
if mibBuilder.loadTexts:
    memMinimumSwapX.setUnits("kB")
_MemSharedX_Type = CounterBasedGauge64
_MemSharedX_Object = MibScalar
memSharedX = _MemSharedX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 24),
    _MemSharedX_Type()
)
memSharedX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSharedX.setStatus("current")
if mibBuilder.loadTexts:
    memSharedX.setUnits("kB")
_MemBufferX_Type = CounterBasedGauge64
_MemBufferX_Object = MibScalar
memBufferX = _MemBufferX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 25),
    _MemBufferX_Type()
)
memBufferX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memBufferX.setStatus("current")
if mibBuilder.loadTexts:
    memBufferX.setUnits("kB")
_MemCachedX_Type = CounterBasedGauge64
_MemCachedX_Object = MibScalar
memCachedX = _MemCachedX_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 26),
    _MemCachedX_Type()
)
memCachedX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memCachedX.setStatus("current")
if mibBuilder.loadTexts:
    memCachedX.setUnits("kB")
_MemSwapError_Type = UCDErrorFlag
_MemSwapError_Object = MibScalar
memSwapError = _MemSwapError_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 100),
    _MemSwapError_Type()
)
memSwapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapError.setStatus("current")
_MemSwapErrorMsg_Type = DisplayString
_MemSwapErrorMsg_Object = MibScalar
memSwapErrorMsg = _MemSwapErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 4, 101),
    _MemSwapErrorMsg_Type()
)
memSwapErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memSwapErrorMsg.setStatus("current")
_ExtTable_Object = MibTable
extTable = _ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8)
)
if mibBuilder.loadTexts:
    extTable.setStatus("current")
_ExtEntry_Object = MibTableRow
extEntry = _ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1)
)
extEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "extIndex"),
)
if mibBuilder.loadTexts:
    extEntry.setStatus("current")


class _ExtIndex_Type(Integer32):
    """Custom type extIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtIndex_Type.__name__ = "Integer32"
_ExtIndex_Object = MibTableColumn
extIndex = _ExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 1),
    _ExtIndex_Type()
)
extIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extIndex.setStatus("current")
_ExtNames_Type = DisplayString
_ExtNames_Object = MibTableColumn
extNames = _ExtNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 2),
    _ExtNames_Type()
)
extNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extNames.setStatus("current")
_ExtCommand_Type = DisplayString
_ExtCommand_Object = MibTableColumn
extCommand = _ExtCommand_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 3),
    _ExtCommand_Type()
)
extCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extCommand.setStatus("current")
_ExtResult_Type = Integer32
_ExtResult_Object = MibTableColumn
extResult = _ExtResult_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 100),
    _ExtResult_Type()
)
extResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extResult.setStatus("current")
_ExtOutput_Type = DisplayString
_ExtOutput_Object = MibTableColumn
extOutput = _ExtOutput_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 101),
    _ExtOutput_Type()
)
extOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extOutput.setStatus("current")
_ExtErrFix_Type = UCDErrorFix
_ExtErrFix_Object = MibTableColumn
extErrFix = _ExtErrFix_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 102),
    _ExtErrFix_Type()
)
extErrFix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extErrFix.setStatus("current")
_ExtErrFixCmd_Type = DisplayString
_ExtErrFixCmd_Object = MibTableColumn
extErrFixCmd = _ExtErrFixCmd_Object(
    (1, 3, 6, 1, 4, 1, 2021, 8, 1, 103),
    _ExtErrFixCmd_Type()
)
extErrFixCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extErrFixCmd.setStatus("current")
_DskTable_Object = MibTable
dskTable = _DskTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9)
)
if mibBuilder.loadTexts:
    dskTable.setStatus("current")
_DskEntry_Object = MibTableRow
dskEntry = _DskEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1)
)
dskEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "dskIndex"),
)
if mibBuilder.loadTexts:
    dskEntry.setStatus("current")


class _DskIndex_Type(Integer32):
    """Custom type dskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DskIndex_Type.__name__ = "Integer32"
_DskIndex_Object = MibTableColumn
dskIndex = _DskIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 1),
    _DskIndex_Type()
)
dskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskIndex.setStatus("current")
_DskPath_Type = DisplayString
_DskPath_Object = MibTableColumn
dskPath = _DskPath_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 2),
    _DskPath_Type()
)
dskPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPath.setStatus("current")
_DskDevice_Type = DisplayString
_DskDevice_Object = MibTableColumn
dskDevice = _DskDevice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 3),
    _DskDevice_Type()
)
dskDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskDevice.setStatus("current")
_DskMinimum_Type = Integer32
_DskMinimum_Object = MibTableColumn
dskMinimum = _DskMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 4),
    _DskMinimum_Type()
)
dskMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinimum.setStatus("current")
_DskMinPercent_Type = Integer32
_DskMinPercent_Object = MibTableColumn
dskMinPercent = _DskMinPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 5),
    _DskMinPercent_Type()
)
dskMinPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskMinPercent.setStatus("current")
_DskTotal_Type = Integer32
_DskTotal_Object = MibTableColumn
dskTotal = _DskTotal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 6),
    _DskTotal_Type()
)
dskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotal.setStatus("current")
_DskAvail_Type = Integer32
_DskAvail_Object = MibTableColumn
dskAvail = _DskAvail_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 7),
    _DskAvail_Type()
)
dskAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvail.setStatus("current")
_DskUsed_Type = Integer32
_DskUsed_Object = MibTableColumn
dskUsed = _DskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 8),
    _DskUsed_Type()
)
dskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsed.setStatus("current")
_DskPercent_Type = Integer32
_DskPercent_Object = MibTableColumn
dskPercent = _DskPercent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 9),
    _DskPercent_Type()
)
dskPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercent.setStatus("current")
_DskPercentNode_Type = Integer32
_DskPercentNode_Object = MibTableColumn
dskPercentNode = _DskPercentNode_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 10),
    _DskPercentNode_Type()
)
dskPercentNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskPercentNode.setStatus("current")
_DskTotalLow_Type = Unsigned32
_DskTotalLow_Object = MibTableColumn
dskTotalLow = _DskTotalLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 11),
    _DskTotalLow_Type()
)
dskTotalLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotalLow.setStatus("current")
_DskTotalHigh_Type = Unsigned32
_DskTotalHigh_Object = MibTableColumn
dskTotalHigh = _DskTotalHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 12),
    _DskTotalHigh_Type()
)
dskTotalHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskTotalHigh.setStatus("current")
_DskAvailLow_Type = Unsigned32
_DskAvailLow_Object = MibTableColumn
dskAvailLow = _DskAvailLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 13),
    _DskAvailLow_Type()
)
dskAvailLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvailLow.setStatus("current")
_DskAvailHigh_Type = Unsigned32
_DskAvailHigh_Object = MibTableColumn
dskAvailHigh = _DskAvailHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 14),
    _DskAvailHigh_Type()
)
dskAvailHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskAvailHigh.setStatus("current")
_DskUsedLow_Type = Unsigned32
_DskUsedLow_Object = MibTableColumn
dskUsedLow = _DskUsedLow_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 15),
    _DskUsedLow_Type()
)
dskUsedLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsedLow.setStatus("current")
_DskUsedHigh_Type = Unsigned32
_DskUsedHigh_Object = MibTableColumn
dskUsedHigh = _DskUsedHigh_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 16),
    _DskUsedHigh_Type()
)
dskUsedHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskUsedHigh.setStatus("current")
_DskErrorFlag_Type = UCDErrorFlag
_DskErrorFlag_Object = MibTableColumn
dskErrorFlag = _DskErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 100),
    _DskErrorFlag_Type()
)
dskErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorFlag.setStatus("current")
_DskErrorMsg_Type = DisplayString
_DskErrorMsg_Object = MibTableColumn
dskErrorMsg = _DskErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 9, 1, 101),
    _DskErrorMsg_Type()
)
dskErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dskErrorMsg.setStatus("current")
_LaTable_Object = MibTable
laTable = _LaTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10)
)
if mibBuilder.loadTexts:
    laTable.setStatus("current")
_LaEntry_Object = MibTableRow
laEntry = _LaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1)
)
laEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "laIndex"),
)
if mibBuilder.loadTexts:
    laEntry.setStatus("current")


class _LaIndex_Type(Integer32):
    """Custom type laIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_LaIndex_Type.__name__ = "Integer32"
_LaIndex_Object = MibTableColumn
laIndex = _LaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 1),
    _LaIndex_Type()
)
laIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laIndex.setStatus("current")
_LaNames_Type = DisplayString
_LaNames_Object = MibTableColumn
laNames = _LaNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 2),
    _LaNames_Type()
)
laNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laNames.setStatus("current")
_LaLoad_Type = DisplayString
_LaLoad_Object = MibTableColumn
laLoad = _LaLoad_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 3),
    _LaLoad_Type()
)
laLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoad.setStatus("current")
_LaConfig_Type = DisplayString
_LaConfig_Object = MibTableColumn
laConfig = _LaConfig_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 4),
    _LaConfig_Type()
)
laConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    laConfig.setStatus("current")
_LaLoadInt_Type = Integer32
_LaLoadInt_Object = MibTableColumn
laLoadInt = _LaLoadInt_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 5),
    _LaLoadInt_Type()
)
laLoadInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoadInt.setStatus("current")
_LaLoadFloat_Type = Float
_LaLoadFloat_Object = MibTableColumn
laLoadFloat = _LaLoadFloat_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 6),
    _LaLoadFloat_Type()
)
laLoadFloat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laLoadFloat.setStatus("current")
_LaErrorFlag_Type = UCDErrorFlag
_LaErrorFlag_Object = MibTableColumn
laErrorFlag = _LaErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 100),
    _LaErrorFlag_Type()
)
laErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laErrorFlag.setStatus("current")
_LaErrMessage_Type = DisplayString
_LaErrMessage_Object = MibTableColumn
laErrMessage = _LaErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 10, 1, 101),
    _LaErrMessage_Type()
)
laErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laErrMessage.setStatus("current")
_SystemStats_ObjectIdentity = ObjectIdentity
systemStats = _SystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 11)
)
_SsIndex_Type = Integer32
_SsIndex_Object = MibScalar
ssIndex = _SsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 1),
    _SsIndex_Type()
)
ssIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIndex.setStatus("current")
_SsErrorName_Type = DisplayString
_SsErrorName_Object = MibScalar
ssErrorName = _SsErrorName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 2),
    _SsErrorName_Type()
)
ssErrorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssErrorName.setStatus("current")
_SsSwapIn_Type = Integer32
_SsSwapIn_Object = MibScalar
ssSwapIn = _SsSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 3),
    _SsSwapIn_Type()
)
ssSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapIn.setStatus("current")
if mibBuilder.loadTexts:
    ssSwapIn.setUnits("kB")
_SsSwapOut_Type = Integer32
_SsSwapOut_Object = MibScalar
ssSwapOut = _SsSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 4),
    _SsSwapOut_Type()
)
ssSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSwapOut.setStatus("current")
if mibBuilder.loadTexts:
    ssSwapOut.setUnits("kB")
_SsIOSent_Type = Integer32
_SsIOSent_Object = MibScalar
ssIOSent = _SsIOSent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 5),
    _SsIOSent_Type()
)
ssIOSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssIOSent.setUnits("blocks/s")
_SsIOReceive_Type = Integer32
_SsIOReceive_Object = MibScalar
ssIOReceive = _SsIOReceive_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 6),
    _SsIOReceive_Type()
)
ssIOReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIOReceive.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssIOReceive.setUnits("blocks/s")
_SsSysInterrupts_Type = Integer32
_SsSysInterrupts_Object = MibScalar
ssSysInterrupts = _SsSysInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 7),
    _SsSysInterrupts_Type()
)
ssSysInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysInterrupts.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssSysInterrupts.setUnits("interrupts/s")
_SsSysContext_Type = Integer32
_SsSysContext_Object = MibScalar
ssSysContext = _SsSysContext_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 8),
    _SsSysContext_Type()
)
ssSysContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssSysContext.setStatus("deprecated")
if mibBuilder.loadTexts:
    ssSysContext.setUnits("switches/s")
_SsCpuUser_Type = Integer32
_SsCpuUser_Object = MibScalar
ssCpuUser = _SsCpuUser_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 9),
    _SsCpuUser_Type()
)
ssCpuUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuUser.setStatus("deprecated")
_SsCpuSystem_Type = Integer32
_SsCpuSystem_Object = MibScalar
ssCpuSystem = _SsCpuSystem_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 10),
    _SsCpuSystem_Type()
)
ssCpuSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuSystem.setStatus("deprecated")
_SsCpuIdle_Type = Integer32
_SsCpuIdle_Object = MibScalar
ssCpuIdle = _SsCpuIdle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 11),
    _SsCpuIdle_Type()
)
ssCpuIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuIdle.setStatus("deprecated")
_SsCpuRawUser_Type = Counter32
_SsCpuRawUser_Object = MibScalar
ssCpuRawUser = _SsCpuRawUser_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 50),
    _SsCpuRawUser_Type()
)
ssCpuRawUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawUser.setStatus("current")
_SsCpuRawNice_Type = Counter32
_SsCpuRawNice_Object = MibScalar
ssCpuRawNice = _SsCpuRawNice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 51),
    _SsCpuRawNice_Type()
)
ssCpuRawNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawNice.setStatus("current")
_SsCpuRawSystem_Type = Counter32
_SsCpuRawSystem_Object = MibScalar
ssCpuRawSystem = _SsCpuRawSystem_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 52),
    _SsCpuRawSystem_Type()
)
ssCpuRawSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSystem.setStatus("current")
_SsCpuRawIdle_Type = Counter32
_SsCpuRawIdle_Object = MibScalar
ssCpuRawIdle = _SsCpuRawIdle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 53),
    _SsCpuRawIdle_Type()
)
ssCpuRawIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawIdle.setStatus("current")
_SsCpuRawWait_Type = Counter32
_SsCpuRawWait_Object = MibScalar
ssCpuRawWait = _SsCpuRawWait_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 54),
    _SsCpuRawWait_Type()
)
ssCpuRawWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawWait.setStatus("current")
_SsCpuRawKernel_Type = Counter32
_SsCpuRawKernel_Object = MibScalar
ssCpuRawKernel = _SsCpuRawKernel_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 55),
    _SsCpuRawKernel_Type()
)
ssCpuRawKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawKernel.setStatus("current")
_SsCpuRawInterrupt_Type = Counter32
_SsCpuRawInterrupt_Object = MibScalar
ssCpuRawInterrupt = _SsCpuRawInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 56),
    _SsCpuRawInterrupt_Type()
)
ssCpuRawInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawInterrupt.setStatus("current")
_SsIORawSent_Type = Counter32
_SsIORawSent_Object = MibScalar
ssIORawSent = _SsIORawSent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 57),
    _SsIORawSent_Type()
)
ssIORawSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawSent.setStatus("current")
_SsIORawReceived_Type = Counter32
_SsIORawReceived_Object = MibScalar
ssIORawReceived = _SsIORawReceived_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 58),
    _SsIORawReceived_Type()
)
ssIORawReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssIORawReceived.setStatus("current")
_SsRawInterrupts_Type = Counter32
_SsRawInterrupts_Object = MibScalar
ssRawInterrupts = _SsRawInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 59),
    _SsRawInterrupts_Type()
)
ssRawInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawInterrupts.setStatus("current")
_SsRawContexts_Type = Counter32
_SsRawContexts_Object = MibScalar
ssRawContexts = _SsRawContexts_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 60),
    _SsRawContexts_Type()
)
ssRawContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawContexts.setStatus("current")
_SsCpuRawSoftIRQ_Type = Counter32
_SsCpuRawSoftIRQ_Object = MibScalar
ssCpuRawSoftIRQ = _SsCpuRawSoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 61),
    _SsCpuRawSoftIRQ_Type()
)
ssCpuRawSoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSoftIRQ.setStatus("current")
_SsRawSwapIn_Type = Counter32
_SsRawSwapIn_Object = MibScalar
ssRawSwapIn = _SsRawSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 62),
    _SsRawSwapIn_Type()
)
ssRawSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawSwapIn.setStatus("current")
_SsRawSwapOut_Type = Counter32
_SsRawSwapOut_Object = MibScalar
ssRawSwapOut = _SsRawSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 63),
    _SsRawSwapOut_Type()
)
ssRawSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssRawSwapOut.setStatus("current")
_SsCpuRawSteal_Type = Counter32
_SsCpuRawSteal_Object = MibScalar
ssCpuRawSteal = _SsCpuRawSteal_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 64),
    _SsCpuRawSteal_Type()
)
ssCpuRawSteal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawSteal.setStatus("current")
_SsCpuRawGuest_Type = Counter32
_SsCpuRawGuest_Object = MibScalar
ssCpuRawGuest = _SsCpuRawGuest_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 65),
    _SsCpuRawGuest_Type()
)
ssCpuRawGuest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawGuest.setStatus("current")
_SsCpuRawGuestNice_Type = Counter32
_SsCpuRawGuestNice_Object = MibScalar
ssCpuRawGuestNice = _SsCpuRawGuestNice_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 66),
    _SsCpuRawGuestNice_Type()
)
ssCpuRawGuestNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuRawGuestNice.setStatus("current")
_SsCpuNumCpus_Type = Integer32
_SsCpuNumCpus_Object = MibScalar
ssCpuNumCpus = _SsCpuNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 2021, 11, 67),
    _SsCpuNumCpus_Type()
)
ssCpuNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssCpuNumCpus.setStatus("current")
_UcdInternal_ObjectIdentity = ObjectIdentity
ucdInternal = _UcdInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 12)
)
_UcdExperimental_ObjectIdentity = ObjectIdentity
ucdExperimental = _UcdExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 13)
)
_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("current")
_FileEntry_Object = MibTableRow
fileEntry = _FileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1)
)
fileEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "fileIndex"),
)
if mibBuilder.loadTexts:
    fileEntry.setStatus("current")


class _FileIndex_Type(Integer32):
    """Custom type fileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FileIndex_Type.__name__ = "Integer32"
_FileIndex_Object = MibTableColumn
fileIndex = _FileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 1),
    _FileIndex_Type()
)
fileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileIndex.setStatus("current")
_FileName_Type = DisplayString
_FileName_Object = MibTableColumn
fileName = _FileName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 2),
    _FileName_Type()
)
fileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileName.setStatus("current")
_FileSize_Type = Integer32
_FileSize_Object = MibTableColumn
fileSize = _FileSize_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 3),
    _FileSize_Type()
)
fileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileSize.setUnits("kB")
_FileMax_Type = Integer32
_FileMax_Object = MibTableColumn
fileMax = _FileMax_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 4),
    _FileMax_Type()
)
fileMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileMax.setStatus("current")
if mibBuilder.loadTexts:
    fileMax.setUnits("kB")
_FileErrorFlag_Type = UCDErrorFlag
_FileErrorFlag_Object = MibTableColumn
fileErrorFlag = _FileErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 100),
    _FileErrorFlag_Type()
)
fileErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileErrorFlag.setStatus("current")
_FileErrorMsg_Type = DisplayString
_FileErrorMsg_Object = MibTableColumn
fileErrorMsg = _FileErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 2021, 15, 1, 101),
    _FileErrorMsg_Type()
)
fileErrorMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileErrorMsg.setStatus("current")
_LogMatch_ObjectIdentity = ObjectIdentity
logMatch = _LogMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 16)
)
_LogMatchMaxEntries_Type = Integer32
_LogMatchMaxEntries_Object = MibScalar
logMatchMaxEntries = _LogMatchMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 1),
    _LogMatchMaxEntries_Type()
)
logMatchMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchMaxEntries.setStatus("current")
_LogMatchTable_Object = MibTable
logMatchTable = _LogMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2)
)
if mibBuilder.loadTexts:
    logMatchTable.setStatus("current")
_LogMatchEntry_Object = MibTableRow
logMatchEntry = _LogMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1)
)
logMatchEntry.setIndexNames(
    (0, "UCD-SNMP-MIB", "logMatchIndex"),
)
if mibBuilder.loadTexts:
    logMatchEntry.setStatus("current")


class _LogMatchIndex_Type(Integer32):
    """Custom type logMatchIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LogMatchIndex_Type.__name__ = "Integer32"
_LogMatchIndex_Object = MibTableColumn
logMatchIndex = _LogMatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 1),
    _LogMatchIndex_Type()
)
logMatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchIndex.setStatus("current")
_LogMatchName_Type = DisplayString
_LogMatchName_Object = MibTableColumn
logMatchName = _LogMatchName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 2),
    _LogMatchName_Type()
)
logMatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchName.setStatus("current")
_LogMatchFilename_Type = DisplayString
_LogMatchFilename_Object = MibTableColumn
logMatchFilename = _LogMatchFilename_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 3),
    _LogMatchFilename_Type()
)
logMatchFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchFilename.setStatus("current")
_LogMatchRegEx_Type = DisplayString
_LogMatchRegEx_Object = MibTableColumn
logMatchRegEx = _LogMatchRegEx_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 4),
    _LogMatchRegEx_Type()
)
logMatchRegEx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchRegEx.setStatus("current")
_LogMatchGlobalCounter_Type = Counter32
_LogMatchGlobalCounter_Object = MibTableColumn
logMatchGlobalCounter = _LogMatchGlobalCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 5),
    _LogMatchGlobalCounter_Type()
)
logMatchGlobalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchGlobalCounter.setStatus("current")
_LogMatchGlobalCount_Type = Integer32
_LogMatchGlobalCount_Object = MibTableColumn
logMatchGlobalCount = _LogMatchGlobalCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 6),
    _LogMatchGlobalCount_Type()
)
logMatchGlobalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchGlobalCount.setStatus("current")
_LogMatchCurrentCounter_Type = Counter32
_LogMatchCurrentCounter_Object = MibTableColumn
logMatchCurrentCounter = _LogMatchCurrentCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 7),
    _LogMatchCurrentCounter_Type()
)
logMatchCurrentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCurrentCounter.setStatus("current")
_LogMatchCurrentCount_Type = Integer32
_LogMatchCurrentCount_Object = MibTableColumn
logMatchCurrentCount = _LogMatchCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 8),
    _LogMatchCurrentCount_Type()
)
logMatchCurrentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCurrentCount.setStatus("current")
_LogMatchCounter_Type = Counter32
_LogMatchCounter_Object = MibTableColumn
logMatchCounter = _LogMatchCounter_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 9),
    _LogMatchCounter_Type()
)
logMatchCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCounter.setStatus("current")
_LogMatchCount_Type = Integer32
_LogMatchCount_Object = MibTableColumn
logMatchCount = _LogMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 10),
    _LogMatchCount_Type()
)
logMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCount.setStatus("current")
_LogMatchCycle_Type = Integer32
_LogMatchCycle_Object = MibTableColumn
logMatchCycle = _LogMatchCycle_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 11),
    _LogMatchCycle_Type()
)
logMatchCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchCycle.setStatus("current")
_LogMatchErrorFlag_Type = UCDErrorFlag
_LogMatchErrorFlag_Object = MibTableColumn
logMatchErrorFlag = _LogMatchErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 100),
    _LogMatchErrorFlag_Type()
)
logMatchErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchErrorFlag.setStatus("current")
_LogMatchRegExCompilation_Type = DisplayString
_LogMatchRegExCompilation_Object = MibTableColumn
logMatchRegExCompilation = _LogMatchRegExCompilation_Object(
    (1, 3, 6, 1, 4, 1, 2021, 16, 2, 1, 101),
    _LogMatchRegExCompilation_Type()
)
logMatchRegExCompilation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logMatchRegExCompilation.setStatus("current")
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 100)
)
_VersionIndex_Type = Integer32
_VersionIndex_Object = MibScalar
versionIndex = _VersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 1),
    _VersionIndex_Type()
)
versionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionIndex.setStatus("current")
_VersionTag_Type = DisplayString
_VersionTag_Object = MibScalar
versionTag = _VersionTag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 2),
    _VersionTag_Type()
)
versionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionTag.setStatus("current")
_VersionDate_Type = DisplayString
_VersionDate_Object = MibScalar
versionDate = _VersionDate_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 3),
    _VersionDate_Type()
)
versionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionDate.setStatus("current")
_VersionCDate_Type = DisplayString
_VersionCDate_Object = MibScalar
versionCDate = _VersionCDate_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 4),
    _VersionCDate_Type()
)
versionCDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionCDate.setStatus("current")
_VersionIdent_Type = DisplayString
_VersionIdent_Object = MibScalar
versionIdent = _VersionIdent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 5),
    _VersionIdent_Type()
)
versionIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionIdent.setStatus("current")
_VersionConfigureOptions_Type = DisplayString
_VersionConfigureOptions_Object = MibScalar
versionConfigureOptions = _VersionConfigureOptions_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 6),
    _VersionConfigureOptions_Type()
)
versionConfigureOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionConfigureOptions.setStatus("current")
_VersionClearCache_Type = Integer32
_VersionClearCache_Object = MibScalar
versionClearCache = _VersionClearCache_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 10),
    _VersionClearCache_Type()
)
versionClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionClearCache.setStatus("current")
_VersionUpdateConfig_Type = Integer32
_VersionUpdateConfig_Object = MibScalar
versionUpdateConfig = _VersionUpdateConfig_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 11),
    _VersionUpdateConfig_Type()
)
versionUpdateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionUpdateConfig.setStatus("current")
_VersionRestartAgent_Type = Integer32
_VersionRestartAgent_Object = MibScalar
versionRestartAgent = _VersionRestartAgent_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 12),
    _VersionRestartAgent_Type()
)
versionRestartAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionRestartAgent.setStatus("current")
_VersionSavePersistentData_Type = Integer32
_VersionSavePersistentData_Object = MibScalar
versionSavePersistentData = _VersionSavePersistentData_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 13),
    _VersionSavePersistentData_Type()
)
versionSavePersistentData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionSavePersistentData.setStatus("current")
_VersionDoDebugging_Type = Integer32
_VersionDoDebugging_Object = MibScalar
versionDoDebugging = _VersionDoDebugging_Object(
    (1, 3, 6, 1, 4, 1, 2021, 100, 20),
    _VersionDoDebugging_Type()
)
versionDoDebugging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    versionDoDebugging.setStatus("current")
_Snmperrs_ObjectIdentity = ObjectIdentity
snmperrs = _Snmperrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 101)
)
_SnmperrIndex_Type = Integer32
_SnmperrIndex_Object = MibScalar
snmperrIndex = _SnmperrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 1),
    _SnmperrIndex_Type()
)
snmperrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrIndex.setStatus("current")
_SnmperrNames_Type = DisplayString
_SnmperrNames_Object = MibScalar
snmperrNames = _SnmperrNames_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 2),
    _SnmperrNames_Type()
)
snmperrNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrNames.setStatus("current")
_SnmperrErrorFlag_Type = UCDErrorFlag
_SnmperrErrorFlag_Object = MibScalar
snmperrErrorFlag = _SnmperrErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 100),
    _SnmperrErrorFlag_Type()
)
snmperrErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrErrorFlag.setStatus("current")
_SnmperrErrMessage_Type = DisplayString
_SnmperrErrMessage_Object = MibScalar
snmperrErrMessage = _SnmperrErrMessage_Object(
    (1, 3, 6, 1, 4, 1, 2021, 101, 101),
    _SnmperrErrMessage_Type()
)
snmperrErrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmperrErrMessage.setStatus("current")
_MrTable_Object = MibTable
mrTable = _MrTable_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102)
)
if mibBuilder.loadTexts:
    mrTable.setStatus("current")
_MrEntry_Object = MibTableRow
mrEntry = _MrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1)
)
mrEntry.setIndexNames(
    (1, "UCD-SNMP-MIB", "mrIndex"),
)
if mibBuilder.loadTexts:
    mrEntry.setStatus("current")
_MrIndex_Type = ObjectIdentifier
_MrIndex_Object = MibTableColumn
mrIndex = _MrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1, 1),
    _MrIndex_Type()
)
mrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrIndex.setStatus("current")
_MrModuleName_Type = DisplayString
_MrModuleName_Object = MibTableColumn
mrModuleName = _MrModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2021, 102, 1, 2),
    _MrModuleName_Type()
)
mrModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrModuleName.setStatus("current")
_UcdSnmpAgent_ObjectIdentity = ObjectIdentity
ucdSnmpAgent = _UcdSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250)
)
_Hpux9_ObjectIdentity = ObjectIdentity
hpux9 = _Hpux9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 1)
)
_Sunos4_ObjectIdentity = ObjectIdentity
sunos4 = _Sunos4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 2)
)
_Solaris_ObjectIdentity = ObjectIdentity
solaris = _Solaris_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 3)
)
_Osf_ObjectIdentity = ObjectIdentity
osf = _Osf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 4)
)
_Ultrix_ObjectIdentity = ObjectIdentity
ultrix = _Ultrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 5)
)
_Hpux10_ObjectIdentity = ObjectIdentity
hpux10 = _Hpux10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 6)
)
_Netbsd1_ObjectIdentity = ObjectIdentity
netbsd1 = _Netbsd1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 7)
)
_Freebsd_ObjectIdentity = ObjectIdentity
freebsd = _Freebsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 8)
)
_Irix_ObjectIdentity = ObjectIdentity
irix = _Irix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 9)
)
_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 10)
)
_Bsdi_ObjectIdentity = ObjectIdentity
bsdi = _Bsdi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 11)
)
_Openbsd_ObjectIdentity = ObjectIdentity
openbsd = _Openbsd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 12)
)
_Win32_ObjectIdentity = ObjectIdentity
win32 = _Win32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 13)
)
_Hpux11_ObjectIdentity = ObjectIdentity
hpux11 = _Hpux11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 14)
)
_Aix_ObjectIdentity = ObjectIdentity
aix = _Aix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 15)
)
_Macosx_ObjectIdentity = ObjectIdentity
macosx = _Macosx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 16)
)
_Dragonfly_ObjectIdentity = ObjectIdentity
dragonfly = _Dragonfly_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 17)
)
_Unknown_ObjectIdentity = ObjectIdentity
unknown = _Unknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 250, 255)
)
_UcdTraps_ObjectIdentity = ObjectIdentity
ucdTraps = _UcdTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2021, 251)
)

# Managed Objects groups


# Notification objects

ucdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2021, 251, 1)
)
if mibBuilder.loadTexts:
    ucdStart.setStatus(
        "current"
    )

ucdShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2021, 251, 2)
)
if mibBuilder.loadTexts:
    ucdShutdown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UCD-SNMP-MIB",
    **{"Float": Float,
       "UCDErrorFlag": UCDErrorFlag,
       "UCDErrorFix": UCDErrorFix,
       "ucdavis": ucdavis,
       "prTable": prTable,
       "prEntry": prEntry,
       "prIndex": prIndex,
       "prNames": prNames,
       "prMin": prMin,
       "prMax": prMax,
       "prCount": prCount,
       "prErrorFlag": prErrorFlag,
       "prErrMessage": prErrMessage,
       "prErrFix": prErrFix,
       "prErrFixCmd": prErrFixCmd,
       "memory": memory,
       "memIndex": memIndex,
       "memErrorName": memErrorName,
       "memTotalSwap": memTotalSwap,
       "memAvailSwap": memAvailSwap,
       "memTotalReal": memTotalReal,
       "memAvailReal": memAvailReal,
       "memTotalSwapTXT": memTotalSwapTXT,
       "memAvailSwapTXT": memAvailSwapTXT,
       "memTotalRealTXT": memTotalRealTXT,
       "memAvailRealTXT": memAvailRealTXT,
       "memTotalFree": memTotalFree,
       "memMinimumSwap": memMinimumSwap,
       "memShared": memShared,
       "memBuffer": memBuffer,
       "memCached": memCached,
       "memUsedSwapTXT": memUsedSwapTXT,
       "memUsedRealTXT": memUsedRealTXT,
       "memTotalSwapX": memTotalSwapX,
       "memAvailSwapX": memAvailSwapX,
       "memTotalRealX": memTotalRealX,
       "memAvailRealX": memAvailRealX,
       "memTotalFreeX": memTotalFreeX,
       "memMinimumSwapX": memMinimumSwapX,
       "memSharedX": memSharedX,
       "memBufferX": memBufferX,
       "memCachedX": memCachedX,
       "memSwapError": memSwapError,
       "memSwapErrorMsg": memSwapErrorMsg,
       "extTable": extTable,
       "extEntry": extEntry,
       "extIndex": extIndex,
       "extNames": extNames,
       "extCommand": extCommand,
       "extResult": extResult,
       "extOutput": extOutput,
       "extErrFix": extErrFix,
       "extErrFixCmd": extErrFixCmd,
       "dskTable": dskTable,
       "dskEntry": dskEntry,
       "dskIndex": dskIndex,
       "dskPath": dskPath,
       "dskDevice": dskDevice,
       "dskMinimum": dskMinimum,
       "dskMinPercent": dskMinPercent,
       "dskTotal": dskTotal,
       "dskAvail": dskAvail,
       "dskUsed": dskUsed,
       "dskPercent": dskPercent,
       "dskPercentNode": dskPercentNode,
       "dskTotalLow": dskTotalLow,
       "dskTotalHigh": dskTotalHigh,
       "dskAvailLow": dskAvailLow,
       "dskAvailHigh": dskAvailHigh,
       "dskUsedLow": dskUsedLow,
       "dskUsedHigh": dskUsedHigh,
       "dskErrorFlag": dskErrorFlag,
       "dskErrorMsg": dskErrorMsg,
       "laTable": laTable,
       "laEntry": laEntry,
       "laIndex": laIndex,
       "laNames": laNames,
       "laLoad": laLoad,
       "laConfig": laConfig,
       "laLoadInt": laLoadInt,
       "laLoadFloat": laLoadFloat,
       "laErrorFlag": laErrorFlag,
       "laErrMessage": laErrMessage,
       "systemStats": systemStats,
       "ssIndex": ssIndex,
       "ssErrorName": ssErrorName,
       "ssSwapIn": ssSwapIn,
       "ssSwapOut": ssSwapOut,
       "ssIOSent": ssIOSent,
       "ssIOReceive": ssIOReceive,
       "ssSysInterrupts": ssSysInterrupts,
       "ssSysContext": ssSysContext,
       "ssCpuUser": ssCpuUser,
       "ssCpuSystem": ssCpuSystem,
       "ssCpuIdle": ssCpuIdle,
       "ssCpuRawUser": ssCpuRawUser,
       "ssCpuRawNice": ssCpuRawNice,
       "ssCpuRawSystem": ssCpuRawSystem,
       "ssCpuRawIdle": ssCpuRawIdle,
       "ssCpuRawWait": ssCpuRawWait,
       "ssCpuRawKernel": ssCpuRawKernel,
       "ssCpuRawInterrupt": ssCpuRawInterrupt,
       "ssIORawSent": ssIORawSent,
       "ssIORawReceived": ssIORawReceived,
       "ssRawInterrupts": ssRawInterrupts,
       "ssRawContexts": ssRawContexts,
       "ssCpuRawSoftIRQ": ssCpuRawSoftIRQ,
       "ssRawSwapIn": ssRawSwapIn,
       "ssRawSwapOut": ssRawSwapOut,
       "ssCpuRawSteal": ssCpuRawSteal,
       "ssCpuRawGuest": ssCpuRawGuest,
       "ssCpuRawGuestNice": ssCpuRawGuestNice,
       "ssCpuNumCpus": ssCpuNumCpus,
       "ucdInternal": ucdInternal,
       "ucdExperimental": ucdExperimental,
       "fileTable": fileTable,
       "fileEntry": fileEntry,
       "fileIndex": fileIndex,
       "fileName": fileName,
       "fileSize": fileSize,
       "fileMax": fileMax,
       "fileErrorFlag": fileErrorFlag,
       "fileErrorMsg": fileErrorMsg,
       "logMatch": logMatch,
       "logMatchMaxEntries": logMatchMaxEntries,
       "logMatchTable": logMatchTable,
       "logMatchEntry": logMatchEntry,
       "logMatchIndex": logMatchIndex,
       "logMatchName": logMatchName,
       "logMatchFilename": logMatchFilename,
       "logMatchRegEx": logMatchRegEx,
       "logMatchGlobalCounter": logMatchGlobalCounter,
       "logMatchGlobalCount": logMatchGlobalCount,
       "logMatchCurrentCounter": logMatchCurrentCounter,
       "logMatchCurrentCount": logMatchCurrentCount,
       "logMatchCounter": logMatchCounter,
       "logMatchCount": logMatchCount,
       "logMatchCycle": logMatchCycle,
       "logMatchErrorFlag": logMatchErrorFlag,
       "logMatchRegExCompilation": logMatchRegExCompilation,
       "version": version,
       "versionIndex": versionIndex,
       "versionTag": versionTag,
       "versionDate": versionDate,
       "versionCDate": versionCDate,
       "versionIdent": versionIdent,
       "versionConfigureOptions": versionConfigureOptions,
       "versionClearCache": versionClearCache,
       "versionUpdateConfig": versionUpdateConfig,
       "versionRestartAgent": versionRestartAgent,
       "versionSavePersistentData": versionSavePersistentData,
       "versionDoDebugging": versionDoDebugging,
       "snmperrs": snmperrs,
       "snmperrIndex": snmperrIndex,
       "snmperrNames": snmperrNames,
       "snmperrErrorFlag": snmperrErrorFlag,
       "snmperrErrMessage": snmperrErrMessage,
       "mrTable": mrTable,
       "mrEntry": mrEntry,
       "mrIndex": mrIndex,
       "mrModuleName": mrModuleName,
       "ucdSnmpAgent": ucdSnmpAgent,
       "hpux9": hpux9,
       "sunos4": sunos4,
       "solaris": solaris,
       "osf": osf,
       "ultrix": ultrix,
       "hpux10": hpux10,
       "netbsd1": netbsd1,
       "freebsd": freebsd,
       "irix": irix,
       "linux": linux,
       "bsdi": bsdi,
       "openbsd": openbsd,
       "win32": win32,
       "hpux11": hpux11,
       "aix": aix,
       "macosx": macosx,
       "dragonfly": dragonfly,
       "unknown": unknown,
       "ucdTraps": ucdTraps,
       "ucdStart": ucdStart,
       "ucdShutdown": ucdShutdown}
)
