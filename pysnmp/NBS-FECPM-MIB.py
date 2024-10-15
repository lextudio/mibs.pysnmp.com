# SNMP MIB module (NBS-FECPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-FECPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:49 2024
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

(InterfaceIndex,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(Unsigned64,
 WritableU64,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "Unsigned64",
    "WritableU64",
    "nbs")

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

nbsFecpmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsFecpmThresholdsGrp_ObjectIdentity = ObjectIdentity
nbsFecpmThresholdsGrp = _NbsFecpmThresholdsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 1)
)
if mibBuilder.loadTexts:
    nbsFecpmThresholdsGrp.setStatus("current")
_NbsFecpmThresholdsTable_Object = MibTable
nbsFecpmThresholdsTable = _NbsFecpmThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1)
)
if mibBuilder.loadTexts:
    nbsFecpmThresholdsTable.setStatus("current")
_NbsFecpmThresholdsEntry_Object = MibTableRow
nbsFecpmThresholdsEntry = _NbsFecpmThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1)
)
nbsFecpmThresholdsEntry.setIndexNames(
    (0, "NBS-FECPM-MIB", "nbsFecpmThresholdsIfIndex"),
    (0, "NBS-FECPM-MIB", "nbsFecpmThresholdsInterval"),
)
if mibBuilder.loadTexts:
    nbsFecpmThresholdsEntry.setStatus("current")
_NbsFecpmThresholdsIfIndex_Type = InterfaceIndex
_NbsFecpmThresholdsIfIndex_Object = MibTableColumn
nbsFecpmThresholdsIfIndex = _NbsFecpmThresholdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 1),
    _NbsFecpmThresholdsIfIndex_Type()
)
nbsFecpmThresholdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsIfIndex.setStatus("current")


class _NbsFecpmThresholdsInterval_Type(Integer32):
    """Custom type nbsFecpmThresholdsInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsFecpmThresholdsInterval_Type.__name__ = "Integer32"
_NbsFecpmThresholdsInterval_Object = MibTableColumn
nbsFecpmThresholdsInterval = _NbsFecpmThresholdsInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 2),
    _NbsFecpmThresholdsInterval_Type()
)
nbsFecpmThresholdsInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsInterval.setStatus("current")
_NbsFecpmThresholdsBitErrCor_Type = WritableU64
_NbsFecpmThresholdsBitErrCor_Object = MibTableColumn
nbsFecpmThresholdsBitErrCor = _NbsFecpmThresholdsBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 10),
    _NbsFecpmThresholdsBitErrCor_Type()
)
nbsFecpmThresholdsBitErrCor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsBitErrCor.setStatus("current")
_NbsFecpmThresholdsByteErrCor_Type = WritableU64
_NbsFecpmThresholdsByteErrCor_Object = MibTableColumn
nbsFecpmThresholdsByteErrCor = _NbsFecpmThresholdsByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 12),
    _NbsFecpmThresholdsByteErrCor_Type()
)
nbsFecpmThresholdsByteErrCor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsByteErrCor.setStatus("current")
_NbsFecpmThresholdsCorBit0to1_Type = WritableU64
_NbsFecpmThresholdsCorBit0to1_Object = MibTableColumn
nbsFecpmThresholdsCorBit0to1 = _NbsFecpmThresholdsCorBit0to1_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 14),
    _NbsFecpmThresholdsCorBit0to1_Type()
)
nbsFecpmThresholdsCorBit0to1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsCorBit0to1.setStatus("current")
_NbsFecpmThresholdsCorBit1to0_Type = WritableU64
_NbsFecpmThresholdsCorBit1to0_Object = MibTableColumn
nbsFecpmThresholdsCorBit1to0 = _NbsFecpmThresholdsCorBit1to0_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 16),
    _NbsFecpmThresholdsCorBit1to0_Type()
)
nbsFecpmThresholdsCorBit1to0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsCorBit1to0.setStatus("current")
_NbsFecpmThresholdsUncorWords_Type = WritableU64
_NbsFecpmThresholdsUncorWords_Object = MibTableColumn
nbsFecpmThresholdsUncorWords = _NbsFecpmThresholdsUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 18),
    _NbsFecpmThresholdsUncorWords_Type()
)
nbsFecpmThresholdsUncorWords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecpmThresholdsUncorWords.setStatus("current")
_NbsFecpmCurrentGrp_ObjectIdentity = ObjectIdentity
nbsFecpmCurrentGrp = _NbsFecpmCurrentGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 2)
)
if mibBuilder.loadTexts:
    nbsFecpmCurrentGrp.setStatus("current")
_NbsFecpmCurrentSysDate_Type = Integer32
_NbsFecpmCurrentSysDate_Object = MibScalar
nbsFecpmCurrentSysDate = _NbsFecpmCurrentSysDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 1),
    _NbsFecpmCurrentSysDate_Type()
)
nbsFecpmCurrentSysDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentSysDate.setStatus("current")
_NbsFecpmCurrentSysTime_Type = Integer32
_NbsFecpmCurrentSysTime_Object = MibScalar
nbsFecpmCurrentSysTime = _NbsFecpmCurrentSysTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 2),
    _NbsFecpmCurrentSysTime_Type()
)
nbsFecpmCurrentSysTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentSysTime.setStatus("current")
_NbsFecpmCurrentTable_Object = MibTable
nbsFecpmCurrentTable = _NbsFecpmCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3)
)
if mibBuilder.loadTexts:
    nbsFecpmCurrentTable.setStatus("current")
_NbsFecpmCurrentEntry_Object = MibTableRow
nbsFecpmCurrentEntry = _NbsFecpmCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1)
)
nbsFecpmCurrentEntry.setIndexNames(
    (0, "NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
    (0, "NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
)
if mibBuilder.loadTexts:
    nbsFecpmCurrentEntry.setStatus("current")
_NbsFecpmCurrentIfIndex_Type = InterfaceIndex
_NbsFecpmCurrentIfIndex_Object = MibTableColumn
nbsFecpmCurrentIfIndex = _NbsFecpmCurrentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 1),
    _NbsFecpmCurrentIfIndex_Type()
)
nbsFecpmCurrentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentIfIndex.setStatus("current")


class _NbsFecpmCurrentInterval_Type(Integer32):
    """Custom type nbsFecpmCurrentInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsFecpmCurrentInterval_Type.__name__ = "Integer32"
_NbsFecpmCurrentInterval_Object = MibTableColumn
nbsFecpmCurrentInterval = _NbsFecpmCurrentInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 2),
    _NbsFecpmCurrentInterval_Type()
)
nbsFecpmCurrentInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentInterval.setStatus("current")
_NbsFecpmCurrentDate_Type = Integer32
_NbsFecpmCurrentDate_Object = MibTableColumn
nbsFecpmCurrentDate = _NbsFecpmCurrentDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 5),
    _NbsFecpmCurrentDate_Type()
)
nbsFecpmCurrentDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentDate.setStatus("current")
_NbsFecpmCurrentTime_Type = Integer32
_NbsFecpmCurrentTime_Object = MibTableColumn
nbsFecpmCurrentTime = _NbsFecpmCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 6),
    _NbsFecpmCurrentTime_Type()
)
nbsFecpmCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentTime.setStatus("current")
_NbsFecpmCurrentBitErrCor_Type = Unsigned64
_NbsFecpmCurrentBitErrCor_Object = MibTableColumn
nbsFecpmCurrentBitErrCor = _NbsFecpmCurrentBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 10),
    _NbsFecpmCurrentBitErrCor_Type()
)
nbsFecpmCurrentBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentBitErrCor.setStatus("current")
_NbsFecpmCurrentByteErrCor_Type = Unsigned64
_NbsFecpmCurrentByteErrCor_Object = MibTableColumn
nbsFecpmCurrentByteErrCor = _NbsFecpmCurrentByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 12),
    _NbsFecpmCurrentByteErrCor_Type()
)
nbsFecpmCurrentByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentByteErrCor.setStatus("current")
_NbsFecpmCurrentCorBit0to1_Type = Unsigned64
_NbsFecpmCurrentCorBit0to1_Object = MibTableColumn
nbsFecpmCurrentCorBit0to1 = _NbsFecpmCurrentCorBit0to1_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 14),
    _NbsFecpmCurrentCorBit0to1_Type()
)
nbsFecpmCurrentCorBit0to1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentCorBit0to1.setStatus("current")
_NbsFecpmCurrentCorBit1to0_Type = Unsigned64
_NbsFecpmCurrentCorBit1to0_Object = MibTableColumn
nbsFecpmCurrentCorBit1to0 = _NbsFecpmCurrentCorBit1to0_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 16),
    _NbsFecpmCurrentCorBit1to0_Type()
)
nbsFecpmCurrentCorBit1to0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentCorBit1to0.setStatus("current")
_NbsFecpmCurrentUncorWords_Type = Unsigned64
_NbsFecpmCurrentUncorWords_Object = MibTableColumn
nbsFecpmCurrentUncorWords = _NbsFecpmCurrentUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 18),
    _NbsFecpmCurrentUncorWords_Type()
)
nbsFecpmCurrentUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmCurrentUncorWords.setStatus("current")
_NbsFecpmHistoricGrp_ObjectIdentity = ObjectIdentity
nbsFecpmHistoricGrp = _NbsFecpmHistoricGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 3)
)
if mibBuilder.loadTexts:
    nbsFecpmHistoricGrp.setStatus("current")
_NbsFecpmHistoricTable_Object = MibTable
nbsFecpmHistoricTable = _NbsFecpmHistoricTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3)
)
if mibBuilder.loadTexts:
    nbsFecpmHistoricTable.setStatus("current")
_NbsFecpmHistoricEntry_Object = MibTableRow
nbsFecpmHistoricEntry = _NbsFecpmHistoricEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1)
)
nbsFecpmHistoricEntry.setIndexNames(
    (0, "NBS-FECPM-MIB", "nbsFecpmHistoricIfIndex"),
    (0, "NBS-FECPM-MIB", "nbsFecpmHistoricInterval"),
    (0, "NBS-FECPM-MIB", "nbsFecpmHistoricSample"),
)
if mibBuilder.loadTexts:
    nbsFecpmHistoricEntry.setStatus("current")
_NbsFecpmHistoricIfIndex_Type = InterfaceIndex
_NbsFecpmHistoricIfIndex_Object = MibTableColumn
nbsFecpmHistoricIfIndex = _NbsFecpmHistoricIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 1),
    _NbsFecpmHistoricIfIndex_Type()
)
nbsFecpmHistoricIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricIfIndex.setStatus("current")


class _NbsFecpmHistoricInterval_Type(Integer32):
    """Custom type nbsFecpmHistoricInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quarterHour", 1),
          ("twentyfourHour", 2))
    )


_NbsFecpmHistoricInterval_Type.__name__ = "Integer32"
_NbsFecpmHistoricInterval_Object = MibTableColumn
nbsFecpmHistoricInterval = _NbsFecpmHistoricInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 2),
    _NbsFecpmHistoricInterval_Type()
)
nbsFecpmHistoricInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsFecpmHistoricInterval.setStatus("current")
_NbsFecpmHistoricSample_Type = Integer32
_NbsFecpmHistoricSample_Object = MibTableColumn
nbsFecpmHistoricSample = _NbsFecpmHistoricSample_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 4),
    _NbsFecpmHistoricSample_Type()
)
nbsFecpmHistoricSample.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsFecpmHistoricSample.setStatus("current")
_NbsFecpmHistoricDate_Type = Integer32
_NbsFecpmHistoricDate_Object = MibTableColumn
nbsFecpmHistoricDate = _NbsFecpmHistoricDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 5),
    _NbsFecpmHistoricDate_Type()
)
nbsFecpmHistoricDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricDate.setStatus("current")
_NbsFecpmHistoricTime_Type = Integer32
_NbsFecpmHistoricTime_Object = MibTableColumn
nbsFecpmHistoricTime = _NbsFecpmHistoricTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 6),
    _NbsFecpmHistoricTime_Type()
)
nbsFecpmHistoricTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricTime.setStatus("current")
_NbsFecpmHistoricBitErrCor_Type = Unsigned64
_NbsFecpmHistoricBitErrCor_Object = MibTableColumn
nbsFecpmHistoricBitErrCor = _NbsFecpmHistoricBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 10),
    _NbsFecpmHistoricBitErrCor_Type()
)
nbsFecpmHistoricBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricBitErrCor.setStatus("current")
_NbsFecpmHistoricByteErrCor_Type = Unsigned64
_NbsFecpmHistoricByteErrCor_Object = MibTableColumn
nbsFecpmHistoricByteErrCor = _NbsFecpmHistoricByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 12),
    _NbsFecpmHistoricByteErrCor_Type()
)
nbsFecpmHistoricByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricByteErrCor.setStatus("current")
_NbsFecpmHistoricCorBit0to1_Type = Unsigned64
_NbsFecpmHistoricCorBit0to1_Object = MibTableColumn
nbsFecpmHistoricCorBit0to1 = _NbsFecpmHistoricCorBit0to1_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 14),
    _NbsFecpmHistoricCorBit0to1_Type()
)
nbsFecpmHistoricCorBit0to1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricCorBit0to1.setStatus("current")
_NbsFecpmHistoricCorBit1to0_Type = Unsigned64
_NbsFecpmHistoricCorBit1to0_Object = MibTableColumn
nbsFecpmHistoricCorBit1to0 = _NbsFecpmHistoricCorBit1to0_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 16),
    _NbsFecpmHistoricCorBit1to0_Type()
)
nbsFecpmHistoricCorBit1to0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricCorBit1to0.setStatus("current")
_NbsFecpmHistoricUncorWords_Type = Unsigned64
_NbsFecpmHistoricUncorWords_Object = MibTableColumn
nbsFecpmHistoricUncorWords = _NbsFecpmHistoricUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 18),
    _NbsFecpmHistoricUncorWords_Type()
)
nbsFecpmHistoricUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmHistoricUncorWords.setStatus("current")
_NbsFecpmRunningGrp_ObjectIdentity = ObjectIdentity
nbsFecpmRunningGrp = _NbsFecpmRunningGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 4)
)
if mibBuilder.loadTexts:
    nbsFecpmRunningGrp.setStatus("current")
_NbsFecpmRunningTable_Object = MibTable
nbsFecpmRunningTable = _NbsFecpmRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3)
)
if mibBuilder.loadTexts:
    nbsFecpmRunningTable.setStatus("current")
_NbsFecpmRunningEntry_Object = MibTableRow
nbsFecpmRunningEntry = _NbsFecpmRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1)
)
nbsFecpmRunningEntry.setIndexNames(
    (0, "NBS-FECPM-MIB", "nbsFecpmRunningIfIndex"),
)
if mibBuilder.loadTexts:
    nbsFecpmRunningEntry.setStatus("current")
_NbsFecpmRunningIfIndex_Type = InterfaceIndex
_NbsFecpmRunningIfIndex_Object = MibTableColumn
nbsFecpmRunningIfIndex = _NbsFecpmRunningIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 1),
    _NbsFecpmRunningIfIndex_Type()
)
nbsFecpmRunningIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningIfIndex.setStatus("current")
_NbsFecpmRunningDate_Type = Integer32
_NbsFecpmRunningDate_Object = MibTableColumn
nbsFecpmRunningDate = _NbsFecpmRunningDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 5),
    _NbsFecpmRunningDate_Type()
)
nbsFecpmRunningDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningDate.setStatus("current")
_NbsFecpmRunningTime_Type = Integer32
_NbsFecpmRunningTime_Object = MibTableColumn
nbsFecpmRunningTime = _NbsFecpmRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 6),
    _NbsFecpmRunningTime_Type()
)
nbsFecpmRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningTime.setStatus("current")
_NbsFecpmRunningBitErrCor_Type = Counter64
_NbsFecpmRunningBitErrCor_Object = MibTableColumn
nbsFecpmRunningBitErrCor = _NbsFecpmRunningBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 10),
    _NbsFecpmRunningBitErrCor_Type()
)
nbsFecpmRunningBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningBitErrCor.setStatus("current")
_NbsFecpmRunningByteErrCor_Type = Counter64
_NbsFecpmRunningByteErrCor_Object = MibTableColumn
nbsFecpmRunningByteErrCor = _NbsFecpmRunningByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 12),
    _NbsFecpmRunningByteErrCor_Type()
)
nbsFecpmRunningByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningByteErrCor.setStatus("current")
_NbsFecpmRunningCorBit0to1_Type = Counter64
_NbsFecpmRunningCorBit0to1_Object = MibTableColumn
nbsFecpmRunningCorBit0to1 = _NbsFecpmRunningCorBit0to1_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 14),
    _NbsFecpmRunningCorBit0to1_Type()
)
nbsFecpmRunningCorBit0to1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningCorBit0to1.setStatus("current")
_NbsFecpmRunningCorBit1to0_Type = Counter64
_NbsFecpmRunningCorBit1to0_Object = MibTableColumn
nbsFecpmRunningCorBit1to0 = _NbsFecpmRunningCorBit1to0_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 16),
    _NbsFecpmRunningCorBit1to0_Type()
)
nbsFecpmRunningCorBit1to0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningCorBit1to0.setStatus("current")
_NbsFecpmRunningUncorWords_Type = Counter64
_NbsFecpmRunningUncorWords_Object = MibTableColumn
nbsFecpmRunningUncorWords = _NbsFecpmRunningUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 18),
    _NbsFecpmRunningUncorWords_Type()
)
nbsFecpmRunningUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecpmRunningUncorWords.setStatus("current")
_NbsFecStatsGrp_ObjectIdentity = ObjectIdentity
nbsFecStatsGrp = _NbsFecStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 90)
)
if mibBuilder.loadTexts:
    nbsFecStatsGrp.setStatus("current")
_NbsFecStatsTable_Object = MibTable
nbsFecStatsTable = _NbsFecStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3)
)
if mibBuilder.loadTexts:
    nbsFecStatsTable.setStatus("current")
_NbsFecStatsEntry_Object = MibTableRow
nbsFecStatsEntry = _NbsFecStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1)
)
nbsFecStatsEntry.setIndexNames(
    (0, "NBS-FECPM-MIB", "nbsFecStatsIfIndex"),
)
if mibBuilder.loadTexts:
    nbsFecStatsEntry.setStatus("current")
_NbsFecStatsIfIndex_Type = InterfaceIndex
_NbsFecStatsIfIndex_Object = MibTableColumn
nbsFecStatsIfIndex = _NbsFecStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 1),
    _NbsFecStatsIfIndex_Type()
)
nbsFecStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsIfIndex.setStatus("current")
_NbsFecStatsDate_Type = Integer32
_NbsFecStatsDate_Object = MibTableColumn
nbsFecStatsDate = _NbsFecStatsDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 5),
    _NbsFecStatsDate_Type()
)
nbsFecStatsDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsDate.setStatus("current")
_NbsFecStatsTime_Type = Integer32
_NbsFecStatsTime_Object = MibTableColumn
nbsFecStatsTime = _NbsFecStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 6),
    _NbsFecStatsTime_Type()
)
nbsFecStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsTime.setStatus("current")
_NbsFecStatsSpan_Type = Integer32
_NbsFecStatsSpan_Object = MibTableColumn
nbsFecStatsSpan = _NbsFecStatsSpan_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 7),
    _NbsFecStatsSpan_Type()
)
nbsFecStatsSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsSpan.setStatus("current")


class _NbsFecStatsState_Type(Integer32):
    """Custom type nbsFecStatsState based on Integer32"""
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
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1),
          ("stopped", 4))
    )


_NbsFecStatsState_Type.__name__ = "Integer32"
_NbsFecStatsState_Object = MibTableColumn
nbsFecStatsState = _NbsFecStatsState_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 8),
    _NbsFecStatsState_Type()
)
nbsFecStatsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsFecStatsState.setStatus("current")
_NbsFecStatsBitErrCor_Type = Counter64
_NbsFecStatsBitErrCor_Object = MibTableColumn
nbsFecStatsBitErrCor = _NbsFecStatsBitErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 10),
    _NbsFecStatsBitErrCor_Type()
)
nbsFecStatsBitErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsBitErrCor.setStatus("current")
_NbsFecStatsByteErrCor_Type = Counter64
_NbsFecStatsByteErrCor_Object = MibTableColumn
nbsFecStatsByteErrCor = _NbsFecStatsByteErrCor_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 12),
    _NbsFecStatsByteErrCor_Type()
)
nbsFecStatsByteErrCor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsByteErrCor.setStatus("current")
_NbsFecStatsCorBit0to1_Type = Counter64
_NbsFecStatsCorBit0to1_Object = MibTableColumn
nbsFecStatsCorBit0to1 = _NbsFecStatsCorBit0to1_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 14),
    _NbsFecStatsCorBit0to1_Type()
)
nbsFecStatsCorBit0to1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsCorBit0to1.setStatus("current")
_NbsFecStatsCorBit1to0_Type = Counter64
_NbsFecStatsCorBit1to0_Object = MibTableColumn
nbsFecStatsCorBit1to0 = _NbsFecStatsCorBit1to0_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 16),
    _NbsFecStatsCorBit1to0_Type()
)
nbsFecStatsCorBit1to0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsCorBit1to0.setStatus("current")
_NbsFecStatsUncorWords_Type = Counter64
_NbsFecStatsUncorWords_Object = MibTableColumn
nbsFecStatsUncorWords = _NbsFecStatsUncorWords_Object(
    (1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 18),
    _NbsFecStatsUncorWords_Type()
)
nbsFecStatsUncorWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsFecStatsUncorWords.setStatus("current")
_NbsFecpmEventsGrp_ObjectIdentity = ObjectIdentity
nbsFecpmEventsGrp = _NbsFecpmEventsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 100)
)
if mibBuilder.loadTexts:
    nbsFecpmEventsGrp.setStatus("current")
_NbsFecpmTraps_ObjectIdentity = ObjectIdentity
nbsFecpmTraps = _NbsFecpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0)
)
if mibBuilder.loadTexts:
    nbsFecpmTraps.setStatus("current")

# Managed Objects groups


# Notification objects

nbsFecpmTrapsBitErrCor = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 10)
)
nbsFecpmTrapsBitErrCor.setObjects(
      *(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentBitErrCor"))
)
if mibBuilder.loadTexts:
    nbsFecpmTrapsBitErrCor.setStatus(
        "current"
    )

nbsFecpmTrapsByteErrCor = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 12)
)
nbsFecpmTrapsByteErrCor.setObjects(
      *(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentByteErrCor"))
)
if mibBuilder.loadTexts:
    nbsFecpmTrapsByteErrCor.setStatus(
        "current"
    )

nbsFecpmTrapsCorBit0to1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 14)
)
nbsFecpmTrapsCorBit0to1.setObjects(
      *(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit0to1"))
)
if mibBuilder.loadTexts:
    nbsFecpmTrapsCorBit0to1.setStatus(
        "current"
    )

nbsFecpmTrapsCorBit1to0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 16)
)
nbsFecpmTrapsCorBit1to0.setObjects(
      *(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit1to0"))
)
if mibBuilder.loadTexts:
    nbsFecpmTrapsCorBit1to0.setStatus(
        "current"
    )

nbsFecpmTrapsUncorWords = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 18)
)
nbsFecpmTrapsUncorWords.setObjects(
      *(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"),
        ("NBS-FECPM-MIB", "nbsFecpmCurrentUncorWords"))
)
if mibBuilder.loadTexts:
    nbsFecpmTrapsUncorWords.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-FECPM-MIB",
    **{"nbsFecpmMib": nbsFecpmMib,
       "nbsFecpmThresholdsGrp": nbsFecpmThresholdsGrp,
       "nbsFecpmThresholdsTable": nbsFecpmThresholdsTable,
       "nbsFecpmThresholdsEntry": nbsFecpmThresholdsEntry,
       "nbsFecpmThresholdsIfIndex": nbsFecpmThresholdsIfIndex,
       "nbsFecpmThresholdsInterval": nbsFecpmThresholdsInterval,
       "nbsFecpmThresholdsBitErrCor": nbsFecpmThresholdsBitErrCor,
       "nbsFecpmThresholdsByteErrCor": nbsFecpmThresholdsByteErrCor,
       "nbsFecpmThresholdsCorBit0to1": nbsFecpmThresholdsCorBit0to1,
       "nbsFecpmThresholdsCorBit1to0": nbsFecpmThresholdsCorBit1to0,
       "nbsFecpmThresholdsUncorWords": nbsFecpmThresholdsUncorWords,
       "nbsFecpmCurrentGrp": nbsFecpmCurrentGrp,
       "nbsFecpmCurrentSysDate": nbsFecpmCurrentSysDate,
       "nbsFecpmCurrentSysTime": nbsFecpmCurrentSysTime,
       "nbsFecpmCurrentTable": nbsFecpmCurrentTable,
       "nbsFecpmCurrentEntry": nbsFecpmCurrentEntry,
       "nbsFecpmCurrentIfIndex": nbsFecpmCurrentIfIndex,
       "nbsFecpmCurrentInterval": nbsFecpmCurrentInterval,
       "nbsFecpmCurrentDate": nbsFecpmCurrentDate,
       "nbsFecpmCurrentTime": nbsFecpmCurrentTime,
       "nbsFecpmCurrentBitErrCor": nbsFecpmCurrentBitErrCor,
       "nbsFecpmCurrentByteErrCor": nbsFecpmCurrentByteErrCor,
       "nbsFecpmCurrentCorBit0to1": nbsFecpmCurrentCorBit0to1,
       "nbsFecpmCurrentCorBit1to0": nbsFecpmCurrentCorBit1to0,
       "nbsFecpmCurrentUncorWords": nbsFecpmCurrentUncorWords,
       "nbsFecpmHistoricGrp": nbsFecpmHistoricGrp,
       "nbsFecpmHistoricTable": nbsFecpmHistoricTable,
       "nbsFecpmHistoricEntry": nbsFecpmHistoricEntry,
       "nbsFecpmHistoricIfIndex": nbsFecpmHistoricIfIndex,
       "nbsFecpmHistoricInterval": nbsFecpmHistoricInterval,
       "nbsFecpmHistoricSample": nbsFecpmHistoricSample,
       "nbsFecpmHistoricDate": nbsFecpmHistoricDate,
       "nbsFecpmHistoricTime": nbsFecpmHistoricTime,
       "nbsFecpmHistoricBitErrCor": nbsFecpmHistoricBitErrCor,
       "nbsFecpmHistoricByteErrCor": nbsFecpmHistoricByteErrCor,
       "nbsFecpmHistoricCorBit0to1": nbsFecpmHistoricCorBit0to1,
       "nbsFecpmHistoricCorBit1to0": nbsFecpmHistoricCorBit1to0,
       "nbsFecpmHistoricUncorWords": nbsFecpmHistoricUncorWords,
       "nbsFecpmRunningGrp": nbsFecpmRunningGrp,
       "nbsFecpmRunningTable": nbsFecpmRunningTable,
       "nbsFecpmRunningEntry": nbsFecpmRunningEntry,
       "nbsFecpmRunningIfIndex": nbsFecpmRunningIfIndex,
       "nbsFecpmRunningDate": nbsFecpmRunningDate,
       "nbsFecpmRunningTime": nbsFecpmRunningTime,
       "nbsFecpmRunningBitErrCor": nbsFecpmRunningBitErrCor,
       "nbsFecpmRunningByteErrCor": nbsFecpmRunningByteErrCor,
       "nbsFecpmRunningCorBit0to1": nbsFecpmRunningCorBit0to1,
       "nbsFecpmRunningCorBit1to0": nbsFecpmRunningCorBit1to0,
       "nbsFecpmRunningUncorWords": nbsFecpmRunningUncorWords,
       "nbsFecStatsGrp": nbsFecStatsGrp,
       "nbsFecStatsTable": nbsFecStatsTable,
       "nbsFecStatsEntry": nbsFecStatsEntry,
       "nbsFecStatsIfIndex": nbsFecStatsIfIndex,
       "nbsFecStatsDate": nbsFecStatsDate,
       "nbsFecStatsTime": nbsFecStatsTime,
       "nbsFecStatsSpan": nbsFecStatsSpan,
       "nbsFecStatsState": nbsFecStatsState,
       "nbsFecStatsBitErrCor": nbsFecStatsBitErrCor,
       "nbsFecStatsByteErrCor": nbsFecStatsByteErrCor,
       "nbsFecStatsCorBit0to1": nbsFecStatsCorBit0to1,
       "nbsFecStatsCorBit1to0": nbsFecStatsCorBit1to0,
       "nbsFecStatsUncorWords": nbsFecStatsUncorWords,
       "nbsFecpmEventsGrp": nbsFecpmEventsGrp,
       "nbsFecpmTraps": nbsFecpmTraps,
       "nbsFecpmTrapsBitErrCor": nbsFecpmTrapsBitErrCor,
       "nbsFecpmTrapsByteErrCor": nbsFecpmTrapsByteErrCor,
       "nbsFecpmTrapsCorBit0to1": nbsFecpmTrapsCorBit0to1,
       "nbsFecpmTrapsCorBit1to0": nbsFecpmTrapsCorBit1to0,
       "nbsFecpmTrapsUncorWords": nbsFecpmTrapsUncorWords}
)
