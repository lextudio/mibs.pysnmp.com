# SNMP MIB module (DDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:29 2024
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

(gdc,) = mibBuilder.importSymbols(
    "GDCCMN-MIB",
    "gdc")

(SCinstance,) = mibBuilder.importSymbols(
    "GDCMACRO-MIB",
    "SCinstance")

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

_Dsu_ObjectIdentity = ObjectIdentity
dsu = _Dsu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8)
)
_Dds_ObjectIdentity = ObjectIdentity
dds = _Dds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 498, 8, 1)
)


class _DdsMIBversion_Type(DisplayString):
    """Custom type ddsMIBversion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_DdsMIBversion_Type.__name__ = "DisplayString"
_DdsMIBversion_Object = MibScalar
ddsMIBversion = _DdsMIBversion_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 1),
    _DdsMIBversion_Type()
)
ddsMIBversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsMIBversion.setStatus("mandatory")
_DdsLineCfgTable_Object = MibTable
ddsLineCfgTable = _DdsLineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2)
)
if mibBuilder.loadTexts:
    ddsLineCfgTable.setStatus("mandatory")
_DdsLineCfgEntry_Object = MibTableRow
ddsLineCfgEntry = _DdsLineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1)
)
ddsLineCfgEntry.setIndexNames(
    (0, "DDS-MIB", "ddsLineCfgIndex"),
)
if mibBuilder.loadTexts:
    ddsLineCfgEntry.setStatus("mandatory")
_DdsLineCfgIndex_Type = SCinstance
_DdsLineCfgIndex_Object = MibTableColumn
ddsLineCfgIndex = _DdsLineCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 1),
    _DdsLineCfgIndex_Type()
)
ddsLineCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsLineCfgIndex.setStatus("mandatory")


class _DdsLineType_Type(Integer32):
    """Custom type ddsLineType based on Integer32"""
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
        *(("auto", 4),
          ("clearChannel", 3),
          ("dds1", 1),
          ("ddsSc", 2))
    )


_DdsLineType_Type.__name__ = "Integer32"
_DdsLineType_Object = MibTableColumn
ddsLineType = _DdsLineType_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 2),
    _DdsLineType_Type()
)
ddsLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsLineType.setStatus("mandatory")


class _DdsAutoDataRateDetect_Type(Integer32):
    """Custom type ddsAutoDataRateDetect based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("async19200", 7),
          ("async2400", 1),
          ("async4800", 3),
          ("async9600", 5),
          ("autoAsync", 11),
          ("autoSync", 12),
          ("sync19200", 8),
          ("sync2400", 2),
          ("sync4800", 4),
          ("sync56000", 9),
          ("sync64000", 10),
          ("sync9600", 6))
    )


_DdsAutoDataRateDetect_Type.__name__ = "Integer32"
_DdsAutoDataRateDetect_Object = MibTableColumn
ddsAutoDataRateDetect = _DdsAutoDataRateDetect_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 3),
    _DdsAutoDataRateDetect_Type()
)
ddsAutoDataRateDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsAutoDataRateDetect.setStatus("mandatory")


class _DdsDataRate_Type(Integer32):
    """Custom type ddsDataRate based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("async19200", 7),
          ("async2400", 1),
          ("async4800", 3),
          ("async9600", 5),
          ("autoAsync", 11),
          ("autoSync", 12),
          ("sync19200", 8),
          ("sync2400", 2),
          ("sync4800", 4),
          ("sync56000", 9),
          ("sync64000", 10),
          ("sync9600", 6))
    )


_DdsDataRate_Type.__name__ = "Integer32"
_DdsDataRate_Object = MibTableColumn
ddsDataRate = _DdsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 4),
    _DdsDataRate_Type()
)
ddsDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDataRate.setStatus("mandatory")


class _DdsTxClockSource_Type(Integer32):
    """Custom type ddsTxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 3),
          ("internal", 2),
          ("receive", 1))
    )


_DdsTxClockSource_Type.__name__ = "Integer32"
_DdsTxClockSource_Object = MibTableColumn
ddsTxClockSource = _DdsTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 5),
    _DdsTxClockSource_Type()
)
ddsTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsTxClockSource.setStatus("mandatory")


class _DdsZeroEncodingCfg_Type(Integer32):
    """Custom type ddsZeroEncodingCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DdsZeroEncodingCfg_Type.__name__ = "Integer32"
_DdsZeroEncodingCfg_Object = MibTableColumn
ddsZeroEncodingCfg = _DdsZeroEncodingCfg_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 6),
    _DdsZeroEncodingCfg_Type()
)
ddsZeroEncodingCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsZeroEncodingCfg.setStatus("mandatory")


class _DdsDefaultConfig_Type(Integer32):
    """Custom type ddsDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaultCfg", 2),
          ("noChange", 1))
    )


_DdsDefaultConfig_Type.__name__ = "Integer32"
_DdsDefaultConfig_Object = MibTableColumn
ddsDefaultConfig = _DdsDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 2, 1, 7),
    _DdsDefaultConfig_Type()
)
ddsDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDefaultConfig.setStatus("mandatory")
_DdsDteCfgTable_Object = MibTable
ddsDteCfgTable = _DdsDteCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3)
)
if mibBuilder.loadTexts:
    ddsDteCfgTable.setStatus("mandatory")
_DdsDteCfgEntry_Object = MibTableRow
ddsDteCfgEntry = _DdsDteCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1)
)
ddsDteCfgEntry.setIndexNames(
    (0, "DDS-MIB", "ddsDteCfgIndex"),
)
if mibBuilder.loadTexts:
    ddsDteCfgEntry.setStatus("mandatory")
_DdsDteCfgIndex_Type = SCinstance
_DdsDteCfgIndex_Object = MibTableColumn
ddsDteCfgIndex = _DdsDteCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 1),
    _DdsDteCfgIndex_Type()
)
ddsDteCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsDteCfgIndex.setStatus("mandatory")


class _DdsDteExtBuffClk_Type(Integer32):
    """Custom type ddsDteExtBuffClk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_DdsDteExtBuffClk_Type.__name__ = "Integer32"
_DdsDteExtBuffClk_Object = MibTableColumn
ddsDteExtBuffClk = _DdsDteExtBuffClk_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 2),
    _DdsDteExtBuffClk_Type()
)
ddsDteExtBuffClk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteExtBuffClk.setStatus("mandatory")


class _DdsDteCfgTxCarrier_Type(Integer32):
    """Custom type ddsDteCfgTxCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_DdsDteCfgTxCarrier_Type.__name__ = "Integer32"
_DdsDteCfgTxCarrier_Object = MibTableColumn
ddsDteCfgTxCarrier = _DdsDteCfgTxCarrier_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 3),
    _DdsDteCfgTxCarrier_Type()
)
ddsDteCfgTxCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgTxCarrier.setStatus("mandatory")


class _DdsDteCfgRxCarrier_Type(Integer32):
    """Custom type ddsDteCfgRxCarrier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 1),
          ("switched", 2))
    )


_DdsDteCfgRxCarrier_Type.__name__ = "Integer32"
_DdsDteCfgRxCarrier_Object = MibTableColumn
ddsDteCfgRxCarrier = _DdsDteCfgRxCarrier_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 4),
    _DdsDteCfgRxCarrier_Type()
)
ddsDteCfgRxCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgRxCarrier.setStatus("mandatory")


class _DdsDteCfgCtsDelay_Type(Integer32):
    """Custom type ddsDteCfgCtsDelay based on Integer32"""
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
        *(("cts0mSec", 3),
          ("cts30mSec", 4),
          ("cts60mSec", 5),
          ("cts90mSec", 6),
          ("ctsFixed3Char", 2),
          ("ctsOn", 1))
    )


_DdsDteCfgCtsDelay_Type.__name__ = "Integer32"
_DdsDteCfgCtsDelay_Object = MibTableColumn
ddsDteCfgCtsDelay = _DdsDteCfgCtsDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 5),
    _DdsDteCfgCtsDelay_Type()
)
ddsDteCfgCtsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgCtsDelay.setStatus("mandatory")


class _DdsDteCfgLocalDSR_Type(Integer32):
    """Custom type ddsDteCfgLocalDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("followsDTR", 1),
          ("forcedOn", 2))
    )


_DdsDteCfgLocalDSR_Type.__name__ = "Integer32"
_DdsDteCfgLocalDSR_Object = MibTableColumn
ddsDteCfgLocalDSR = _DdsDteCfgLocalDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 6),
    _DdsDteCfgLocalDSR_Type()
)
ddsDteCfgLocalDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgLocalDSR.setStatus("mandatory")


class _DdsDteCfgAnaloopDSR_Type(Integer32):
    """Custom type ddsDteCfgAnaloopDSR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("off", 1))
    )


_DdsDteCfgAnaloopDSR_Type.__name__ = "Integer32"
_DdsDteCfgAnaloopDSR_Object = MibTableColumn
ddsDteCfgAnaloopDSR = _DdsDteCfgAnaloopDSR_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 7),
    _DdsDteCfgAnaloopDSR_Type()
)
ddsDteCfgAnaloopDSR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgAnaloopDSR.setStatus("mandatory")


class _DdsDteCfgAasStatus_Type(Integer32):
    """Custom type ddsDteCfgAasStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DdsDteCfgAasStatus_Type.__name__ = "Integer32"
_DdsDteCfgAasStatus_Object = MibTableColumn
ddsDteCfgAasStatus = _DdsDteCfgAasStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 8),
    _DdsDteCfgAasStatus_Type()
)
ddsDteCfgAasStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgAasStatus.setStatus("mandatory")


class _DdsDteCfgAasTimer_Type(Integer32):
    """Custom type ddsDteCfgAasTimer based on Integer32"""
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
        *(("sec10", 2),
          ("sec30", 3),
          ("sec45", 4),
          ("sec5", 1))
    )


_DdsDteCfgAasTimer_Type.__name__ = "Integer32"
_DdsDteCfgAasTimer_Object = MibTableColumn
ddsDteCfgAasTimer = _DdsDteCfgAasTimer_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 9),
    _DdsDteCfgAasTimer_Type()
)
ddsDteCfgAasTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgAasTimer.setStatus("mandatory")


class _DdsDteCfgCircuitAssurance_Type(Integer32):
    """Custom type ddsDteCfgCircuitAssurance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DdsDteCfgCircuitAssurance_Type.__name__ = "Integer32"
_DdsDteCfgCircuitAssurance_Object = MibTableColumn
ddsDteCfgCircuitAssurance = _DdsDteCfgCircuitAssurance_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 10),
    _DdsDteCfgCircuitAssurance_Type()
)
ddsDteCfgCircuitAssurance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgCircuitAssurance.setStatus("mandatory")


class _DdsDteCfgSystemStatus_Type(Integer32):
    """Custom type ddsDteCfgSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_DdsDteCfgSystemStatus_Type.__name__ = "Integer32"
_DdsDteCfgSystemStatus_Object = MibTableColumn
ddsDteCfgSystemStatus = _DdsDteCfgSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 11),
    _DdsDteCfgSystemStatus_Type()
)
ddsDteCfgSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgSystemStatus.setStatus("mandatory")


class _DdsDteCfgTermaloop_Type(Integer32):
    """Custom type ddsDteCfgTermaloop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DdsDteCfgTermaloop_Type.__name__ = "Integer32"
_DdsDteCfgTermaloop_Object = MibTableColumn
ddsDteCfgTermaloop = _DdsDteCfgTermaloop_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 3, 1, 12),
    _DdsDteCfgTermaloop_Type()
)
ddsDteCfgTermaloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteCfgTermaloop.setStatus("mandatory")
_DdsDteAsyncCfgTable_Object = MibTable
ddsDteAsyncCfgTable = _DdsDteAsyncCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4)
)
if mibBuilder.loadTexts:
    ddsDteAsyncCfgTable.setStatus("mandatory")
_DdsDteAsyncCfgEntry_Object = MibTableRow
ddsDteAsyncCfgEntry = _DdsDteAsyncCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1)
)
ddsDteAsyncCfgEntry.setIndexNames(
    (0, "DDS-MIB", "ddsDteAsyncCfgIndex"),
)
if mibBuilder.loadTexts:
    ddsDteAsyncCfgEntry.setStatus("mandatory")
_DdsDteAsyncCfgIndex_Type = SCinstance
_DdsDteAsyncCfgIndex_Object = MibTableColumn
ddsDteAsyncCfgIndex = _DdsDteAsyncCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 1),
    _DdsDteAsyncCfgIndex_Type()
)
ddsDteAsyncCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsDteAsyncCfgIndex.setStatus("mandatory")


class _DdsDteAsyncRateAdapt_Type(Integer32):
    """Custom type ddsDteAsyncRateAdapt based on Integer32"""
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
        *(("from1800to2400LineRate", 4),
          ("halfLineRate", 2),
          ("none", 1),
          ("quarterLineRate", 3))
    )


_DdsDteAsyncRateAdapt_Type.__name__ = "Integer32"
_DdsDteAsyncRateAdapt_Object = MibTableColumn
ddsDteAsyncRateAdapt = _DdsDteAsyncRateAdapt_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 2),
    _DdsDteAsyncRateAdapt_Type()
)
ddsDteAsyncRateAdapt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncRateAdapt.setStatus("mandatory")


class _DdsDteAsyncRxDelay_Type(Integer32):
    """Custom type ddsDteAsyncRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_DdsDteAsyncRxDelay_Type.__name__ = "Integer32"
_DdsDteAsyncRxDelay_Object = MibTableColumn
ddsDteAsyncRxDelay = _DdsDteAsyncRxDelay_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 3),
    _DdsDteAsyncRxDelay_Type()
)
ddsDteAsyncRxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncRxDelay.setStatus("mandatory")


class _DdsDteAsyncTxEOTcfg_Type(Integer32):
    """Custom type ddsDteAsyncTxEOTcfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DdsDteAsyncTxEOTcfg_Type.__name__ = "Integer32"
_DdsDteAsyncTxEOTcfg_Object = MibTableColumn
ddsDteAsyncTxEOTcfg = _DdsDteAsyncTxEOTcfg_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 4),
    _DdsDteAsyncTxEOTcfg_Type()
)
ddsDteAsyncTxEOTcfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncTxEOTcfg.setStatus("mandatory")


class _DdsDteAsyncRxEOTcfg_Type(Integer32):
    """Custom type ddsDteAsyncRxEOTcfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_DdsDteAsyncRxEOTcfg_Type.__name__ = "Integer32"
_DdsDteAsyncRxEOTcfg_Object = MibTableColumn
ddsDteAsyncRxEOTcfg = _DdsDteAsyncRxEOTcfg_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 5),
    _DdsDteAsyncRxEOTcfg_Type()
)
ddsDteAsyncRxEOTcfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncRxEOTcfg.setStatus("mandatory")


class _DdsDteAsyncOverSpeed_Type(Integer32):
    """Custom type ddsDteAsyncOverSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("overSpeed1", 1),
          ("overSpeed2point3", 2))
    )


_DdsDteAsyncOverSpeed_Type.__name__ = "Integer32"
_DdsDteAsyncOverSpeed_Object = MibTableColumn
ddsDteAsyncOverSpeed = _DdsDteAsyncOverSpeed_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 6),
    _DdsDteAsyncOverSpeed_Type()
)
ddsDteAsyncOverSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncOverSpeed.setStatus("mandatory")


class _DdsDteAsyncCharacterSize_Type(Integer32):
    """Custom type ddsDteAsyncCharacterSize based on Integer32"""
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
        *(("bits10", 2),
          ("bits11", 1),
          ("bits8", 4),
          ("bits9", 3))
    )


_DdsDteAsyncCharacterSize_Type.__name__ = "Integer32"
_DdsDteAsyncCharacterSize_Object = MibTableColumn
ddsDteAsyncCharacterSize = _DdsDteAsyncCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 4, 1, 7),
    _DdsDteAsyncCharacterSize_Type()
)
ddsDteAsyncCharacterSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ddsDteAsyncCharacterSize.setStatus("mandatory")
_DdsDteStatusTable_Object = MibTable
ddsDteStatusTable = _DdsDteStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 6)
)
if mibBuilder.loadTexts:
    ddsDteStatusTable.setStatus("mandatory")
_DdsDteStatusEntry_Object = MibTableRow
ddsDteStatusEntry = _DdsDteStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 6, 1)
)
ddsDteStatusEntry.setIndexNames(
    (0, "DDS-MIB", "ddsDteStatusIndex"),
)
if mibBuilder.loadTexts:
    ddsDteStatusEntry.setStatus("mandatory")
_DdsDteStatusIndex_Type = SCinstance
_DdsDteStatusIndex_Object = MibTableColumn
ddsDteStatusIndex = _DdsDteStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 6, 1, 1),
    _DdsDteStatusIndex_Type()
)
ddsDteStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsDteStatusIndex.setStatus("mandatory")


class _DdsDteStatus_Type(OctetString):
    """Custom type ddsDteStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_DdsDteStatus_Type.__name__ = "OctetString"
_DdsDteStatus_Object = MibTableColumn
ddsDteStatus = _DdsDteStatus_Object(
    (1, 3, 6, 1, 4, 1, 498, 8, 1, 6, 1, 2),
    _DdsDteStatus_Type()
)
ddsDteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ddsDteStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DDS-MIB",
    **{"dsu": dsu,
       "dds": dds,
       "ddsMIBversion": ddsMIBversion,
       "ddsLineCfgTable": ddsLineCfgTable,
       "ddsLineCfgEntry": ddsLineCfgEntry,
       "ddsLineCfgIndex": ddsLineCfgIndex,
       "ddsLineType": ddsLineType,
       "ddsAutoDataRateDetect": ddsAutoDataRateDetect,
       "ddsDataRate": ddsDataRate,
       "ddsTxClockSource": ddsTxClockSource,
       "ddsZeroEncodingCfg": ddsZeroEncodingCfg,
       "ddsDefaultConfig": ddsDefaultConfig,
       "ddsDteCfgTable": ddsDteCfgTable,
       "ddsDteCfgEntry": ddsDteCfgEntry,
       "ddsDteCfgIndex": ddsDteCfgIndex,
       "ddsDteExtBuffClk": ddsDteExtBuffClk,
       "ddsDteCfgTxCarrier": ddsDteCfgTxCarrier,
       "ddsDteCfgRxCarrier": ddsDteCfgRxCarrier,
       "ddsDteCfgCtsDelay": ddsDteCfgCtsDelay,
       "ddsDteCfgLocalDSR": ddsDteCfgLocalDSR,
       "ddsDteCfgAnaloopDSR": ddsDteCfgAnaloopDSR,
       "ddsDteCfgAasStatus": ddsDteCfgAasStatus,
       "ddsDteCfgAasTimer": ddsDteCfgAasTimer,
       "ddsDteCfgCircuitAssurance": ddsDteCfgCircuitAssurance,
       "ddsDteCfgSystemStatus": ddsDteCfgSystemStatus,
       "ddsDteCfgTermaloop": ddsDteCfgTermaloop,
       "ddsDteAsyncCfgTable": ddsDteAsyncCfgTable,
       "ddsDteAsyncCfgEntry": ddsDteAsyncCfgEntry,
       "ddsDteAsyncCfgIndex": ddsDteAsyncCfgIndex,
       "ddsDteAsyncRateAdapt": ddsDteAsyncRateAdapt,
       "ddsDteAsyncRxDelay": ddsDteAsyncRxDelay,
       "ddsDteAsyncTxEOTcfg": ddsDteAsyncTxEOTcfg,
       "ddsDteAsyncRxEOTcfg": ddsDteAsyncRxEOTcfg,
       "ddsDteAsyncOverSpeed": ddsDteAsyncOverSpeed,
       "ddsDteAsyncCharacterSize": ddsDteAsyncCharacterSize,
       "ddsDteStatusTable": ddsDteStatusTable,
       "ddsDteStatusEntry": ddsDteStatusEntry,
       "ddsDteStatusIndex": ddsDteStatusIndex,
       "ddsDteStatus": ddsDteStatus}
)
