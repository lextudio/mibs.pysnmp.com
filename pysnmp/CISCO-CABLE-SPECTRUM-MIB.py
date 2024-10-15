# SNMP MIB module (CISCO-CABLE-SPECTRUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-SPECTRUM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableSpectrumMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114)
)
ciscoCableSpectrumMIB.setRevisions(
        ("2011-04-08 00:00",
         "2006-10-10 00:00",
         "2004-09-05 00:00",
         "2004-07-14 00:00",
         "2004-03-02 00:00",
         "2003-06-18 00:00",
         "2002-06-10 00:00",
         "2001-02-01 00:00",
         "2000-08-18 00:00",
         "2000-04-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CCSFrequency(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 85000),
    )



class CCSMeasuredFrequency(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 85000),
    )



class CCSRequestOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("abort", 2),
          ("none", 0),
          ("start", 1))
    )



class CCSRequestOperState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 4),
          ("fftBusy", 8),
          ("fftFailed", 9),
          ("idle", 0),
          ("invalidMac", 6),
          ("noError", 3),
          ("notOnLine", 5),
          ("others", 10),
          ("pending", 1),
          ("running", 2),
          ("timeOut", 7))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCableSpectrumMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableSpectrumMIBObjects = _CiscoCableSpectrumMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1)
)
_CcsFlapObjects_ObjectIdentity = ObjectIdentity
ccsFlapObjects = _CcsFlapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1)
)


class _CcsFlapListMaxSize_Type(Integer32):
    """Custom type ccsFlapListMaxSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_CcsFlapListMaxSize_Type.__name__ = "Integer32"
_CcsFlapListMaxSize_Object = MibScalar
ccsFlapListMaxSize = _CcsFlapListMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 1),
    _CcsFlapListMaxSize_Type()
)
ccsFlapListMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapListMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    ccsFlapListMaxSize.setUnits("modems")


class _CcsFlapListCurrentSize_Type(Gauge32):
    """Custom type ccsFlapListCurrentSize based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CcsFlapListCurrentSize_Type.__name__ = "Gauge32"
_CcsFlapListCurrentSize_Object = MibScalar
ccsFlapListCurrentSize = _CcsFlapListCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 2),
    _CcsFlapListCurrentSize_Type()
)
ccsFlapListCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapListCurrentSize.setStatus("current")
if mibBuilder.loadTexts:
    ccsFlapListCurrentSize.setUnits("modems")


class _CcsFlapAging_Type(Integer32):
    """Custom type ccsFlapAging based on Integer32"""
    defaultValue = 10080

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CcsFlapAging_Type.__name__ = "Integer32"
_CcsFlapAging_Object = MibScalar
ccsFlapAging = _CcsFlapAging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 3),
    _CcsFlapAging_Type()
)
ccsFlapAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapAging.setStatus("current")
if mibBuilder.loadTexts:
    ccsFlapAging.setUnits("minutes")


class _CcsFlapInsertionTime_Type(Integer32):
    """Custom type ccsFlapInsertionTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CcsFlapInsertionTime_Type.__name__ = "Integer32"
_CcsFlapInsertionTime_Object = MibScalar
ccsFlapInsertionTime = _CcsFlapInsertionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 4),
    _CcsFlapInsertionTime_Type()
)
ccsFlapInsertionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapInsertionTime.setStatus("current")
if mibBuilder.loadTexts:
    ccsFlapInsertionTime.setUnits("seconds")
_CcsFlapTable_Object = MibTable
ccsFlapTable = _CcsFlapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ccsFlapTable.setStatus("deprecated")
_CcsFlapEntry_Object = MibTableRow
ccsFlapEntry = _CcsFlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1)
)
ccsFlapEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsFlapMacAddr"),
)
if mibBuilder.loadTexts:
    ccsFlapEntry.setStatus("deprecated")
_CcsFlapMacAddr_Type = MacAddress
_CcsFlapMacAddr_Object = MibTableColumn
ccsFlapMacAddr = _CcsFlapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 1),
    _CcsFlapMacAddr_Type()
)
ccsFlapMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsFlapMacAddr.setStatus("deprecated")
_CcsFlapUpstreamIfIndex_Type = InterfaceIndex
_CcsFlapUpstreamIfIndex_Object = MibTableColumn
ccsFlapUpstreamIfIndex = _CcsFlapUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 2),
    _CcsFlapUpstreamIfIndex_Type()
)
ccsFlapUpstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapUpstreamIfIndex.setStatus("deprecated")
_CcsFlapDownstreamIfIndex_Type = InterfaceIndex
_CcsFlapDownstreamIfIndex_Object = MibTableColumn
ccsFlapDownstreamIfIndex = _CcsFlapDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 3),
    _CcsFlapDownstreamIfIndex_Type()
)
ccsFlapDownstreamIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapDownstreamIfIndex.setStatus("deprecated")
_CcsFlapInsertionFails_Type = Counter32
_CcsFlapInsertionFails_Object = MibTableColumn
ccsFlapInsertionFails = _CcsFlapInsertionFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 4),
    _CcsFlapInsertionFails_Type()
)
ccsFlapInsertionFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapInsertionFails.setStatus("deprecated")
_CcsFlapHits_Type = Counter32
_CcsFlapHits_Object = MibTableColumn
ccsFlapHits = _CcsFlapHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 5),
    _CcsFlapHits_Type()
)
ccsFlapHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapHits.setStatus("deprecated")
_CcsFlapMisses_Type = Counter32
_CcsFlapMisses_Object = MibTableColumn
ccsFlapMisses = _CcsFlapMisses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 6),
    _CcsFlapMisses_Type()
)
ccsFlapMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapMisses.setStatus("deprecated")
_CcsFlapCrcErrors_Type = Counter32
_CcsFlapCrcErrors_Object = MibTableColumn
ccsFlapCrcErrors = _CcsFlapCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 7),
    _CcsFlapCrcErrors_Type()
)
ccsFlapCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapCrcErrors.setStatus("deprecated")
_CcsFlapPowerAdjustments_Type = Counter32
_CcsFlapPowerAdjustments_Object = MibTableColumn
ccsFlapPowerAdjustments = _CcsFlapPowerAdjustments_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 8),
    _CcsFlapPowerAdjustments_Type()
)
ccsFlapPowerAdjustments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapPowerAdjustments.setStatus("deprecated")
_CcsFlapTotal_Type = Counter32
_CcsFlapTotal_Object = MibTableColumn
ccsFlapTotal = _CcsFlapTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 9),
    _CcsFlapTotal_Type()
)
ccsFlapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapTotal.setStatus("deprecated")
_CcsFlapLastFlapTime_Type = DateAndTime
_CcsFlapLastFlapTime_Object = MibTableColumn
ccsFlapLastFlapTime = _CcsFlapLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 10),
    _CcsFlapLastFlapTime_Type()
)
ccsFlapLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapLastFlapTime.setStatus("deprecated")
_CcsFlapCreateTime_Type = DateAndTime
_CcsFlapCreateTime_Object = MibTableColumn
ccsFlapCreateTime = _CcsFlapCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 11),
    _CcsFlapCreateTime_Type()
)
ccsFlapCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapCreateTime.setStatus("deprecated")
_CcsFlapRowStatus_Type = RowStatus
_CcsFlapRowStatus_Object = MibTableColumn
ccsFlapRowStatus = _CcsFlapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 12),
    _CcsFlapRowStatus_Type()
)
ccsFlapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapRowStatus.setStatus("deprecated")
_CcsFlapInsertionFailNum_Type = Unsigned32
_CcsFlapInsertionFailNum_Object = MibTableColumn
ccsFlapInsertionFailNum = _CcsFlapInsertionFailNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 13),
    _CcsFlapInsertionFailNum_Type()
)
ccsFlapInsertionFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapInsertionFailNum.setStatus("deprecated")
_CcsFlapHitNum_Type = Unsigned32
_CcsFlapHitNum_Object = MibTableColumn
ccsFlapHitNum = _CcsFlapHitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 14),
    _CcsFlapHitNum_Type()
)
ccsFlapHitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapHitNum.setStatus("deprecated")
_CcsFlapMissNum_Type = Unsigned32
_CcsFlapMissNum_Object = MibTableColumn
ccsFlapMissNum = _CcsFlapMissNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 15),
    _CcsFlapMissNum_Type()
)
ccsFlapMissNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapMissNum.setStatus("deprecated")
_CcsFlapCrcErrorNum_Type = Unsigned32
_CcsFlapCrcErrorNum_Object = MibTableColumn
ccsFlapCrcErrorNum = _CcsFlapCrcErrorNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 16),
    _CcsFlapCrcErrorNum_Type()
)
ccsFlapCrcErrorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapCrcErrorNum.setStatus("deprecated")
_CcsFlapPowerAdjustmentNum_Type = Unsigned32
_CcsFlapPowerAdjustmentNum_Object = MibTableColumn
ccsFlapPowerAdjustmentNum = _CcsFlapPowerAdjustmentNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 17),
    _CcsFlapPowerAdjustmentNum_Type()
)
ccsFlapPowerAdjustmentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapPowerAdjustmentNum.setStatus("deprecated")
_CcsFlapTotalNum_Type = Unsigned32
_CcsFlapTotalNum_Object = MibTableColumn
ccsFlapTotalNum = _CcsFlapTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 18),
    _CcsFlapTotalNum_Type()
)
ccsFlapTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapTotalNum.setStatus("deprecated")
_CcsFlapResetNow_Type = TruthValue
_CcsFlapResetNow_Object = MibTableColumn
ccsFlapResetNow = _CcsFlapResetNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 19),
    _CcsFlapResetNow_Type()
)
ccsFlapResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapResetNow.setStatus("deprecated")
_CcsFlapLastResetTime_Type = DateAndTime
_CcsFlapLastResetTime_Object = MibTableColumn
ccsFlapLastResetTime = _CcsFlapLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 5, 1, 20),
    _CcsFlapLastResetTime_Type()
)
ccsFlapLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapLastResetTime.setStatus("deprecated")


class _CcsFlapPowerAdjustThreshold_Type(Integer32):
    """Custom type ccsFlapPowerAdjustThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CcsFlapPowerAdjustThreshold_Type.__name__ = "Integer32"
_CcsFlapPowerAdjustThreshold_Object = MibScalar
ccsFlapPowerAdjustThreshold = _CcsFlapPowerAdjustThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 6),
    _CcsFlapPowerAdjustThreshold_Type()
)
ccsFlapPowerAdjustThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapPowerAdjustThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccsFlapPowerAdjustThreshold.setUnits("db")


class _CcsFlapMissThreshold_Type(Unsigned32):
    """Custom type ccsFlapMissThreshold based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CcsFlapMissThreshold_Type.__name__ = "Unsigned32"
_CcsFlapMissThreshold_Object = MibScalar
ccsFlapMissThreshold = _CcsFlapMissThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 7),
    _CcsFlapMissThreshold_Type()
)
ccsFlapMissThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapMissThreshold.setStatus("deprecated")
_CcsFlapResetAll_Type = TruthValue
_CcsFlapResetAll_Object = MibScalar
ccsFlapResetAll = _CcsFlapResetAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 8),
    _CcsFlapResetAll_Type()
)
ccsFlapResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapResetAll.setStatus("deprecated")
_CcsFlapClearAll_Type = TruthValue
_CcsFlapClearAll_Object = MibScalar
ccsFlapClearAll = _CcsFlapClearAll_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 9),
    _CcsFlapClearAll_Type()
)
ccsFlapClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsFlapClearAll.setStatus("deprecated")
_CcsFlapLastClearTime_Type = DateAndTime
_CcsFlapLastClearTime_Object = MibScalar
ccsFlapLastClearTime = _CcsFlapLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 10),
    _CcsFlapLastClearTime_Type()
)
ccsFlapLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsFlapLastClearTime.setStatus("deprecated")
_CcsCmFlapTable_Object = MibTable
ccsCmFlapTable = _CcsCmFlapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11)
)
if mibBuilder.loadTexts:
    ccsCmFlapTable.setStatus("current")
_CcsCmFlapEntry_Object = MibTableRow
ccsCmFlapEntry = _CcsCmFlapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1)
)
ccsCmFlapEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapDownstreamIfIndex"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapUpstreamIfIndex"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapMacAddr"),
)
if mibBuilder.loadTexts:
    ccsCmFlapEntry.setStatus("current")
_CcsCmFlapDownstreamIfIndex_Type = InterfaceIndex
_CcsCmFlapDownstreamIfIndex_Object = MibTableColumn
ccsCmFlapDownstreamIfIndex = _CcsCmFlapDownstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 1),
    _CcsCmFlapDownstreamIfIndex_Type()
)
ccsCmFlapDownstreamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsCmFlapDownstreamIfIndex.setStatus("current")
_CcsCmFlapUpstreamIfIndex_Type = InterfaceIndex
_CcsCmFlapUpstreamIfIndex_Object = MibTableColumn
ccsCmFlapUpstreamIfIndex = _CcsCmFlapUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 2),
    _CcsCmFlapUpstreamIfIndex_Type()
)
ccsCmFlapUpstreamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsCmFlapUpstreamIfIndex.setStatus("current")
_CcsCmFlapMacAddr_Type = MacAddress
_CcsCmFlapMacAddr_Object = MibTableColumn
ccsCmFlapMacAddr = _CcsCmFlapMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 3),
    _CcsCmFlapMacAddr_Type()
)
ccsCmFlapMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsCmFlapMacAddr.setStatus("current")
_CcsCmFlapLastFlapTime_Type = DateAndTime
_CcsCmFlapLastFlapTime_Object = MibTableColumn
ccsCmFlapLastFlapTime = _CcsCmFlapLastFlapTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 4),
    _CcsCmFlapLastFlapTime_Type()
)
ccsCmFlapLastFlapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapLastFlapTime.setStatus("current")
_CcsCmFlapCreateTime_Type = DateAndTime
_CcsCmFlapCreateTime_Object = MibTableColumn
ccsCmFlapCreateTime = _CcsCmFlapCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 5),
    _CcsCmFlapCreateTime_Type()
)
ccsCmFlapCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapCreateTime.setStatus("current")
_CcsCmFlapInsertionFailNum_Type = Unsigned32
_CcsCmFlapInsertionFailNum_Object = MibTableColumn
ccsCmFlapInsertionFailNum = _CcsCmFlapInsertionFailNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 6),
    _CcsCmFlapInsertionFailNum_Type()
)
ccsCmFlapInsertionFailNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapInsertionFailNum.setStatus("current")
_CcsCmFlapHitNum_Type = Unsigned32
_CcsCmFlapHitNum_Object = MibTableColumn
ccsCmFlapHitNum = _CcsCmFlapHitNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 7),
    _CcsCmFlapHitNum_Type()
)
ccsCmFlapHitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapHitNum.setStatus("current")
_CcsCmFlapMissNum_Type = Unsigned32
_CcsCmFlapMissNum_Object = MibTableColumn
ccsCmFlapMissNum = _CcsCmFlapMissNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 8),
    _CcsCmFlapMissNum_Type()
)
ccsCmFlapMissNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapMissNum.setStatus("current")
_CcsCmFlapCrcErrorNum_Type = Unsigned32
_CcsCmFlapCrcErrorNum_Object = MibTableColumn
ccsCmFlapCrcErrorNum = _CcsCmFlapCrcErrorNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 9),
    _CcsCmFlapCrcErrorNum_Type()
)
ccsCmFlapCrcErrorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapCrcErrorNum.setStatus("current")
_CcsCmFlapPowerAdjustmentNum_Type = Unsigned32
_CcsCmFlapPowerAdjustmentNum_Object = MibTableColumn
ccsCmFlapPowerAdjustmentNum = _CcsCmFlapPowerAdjustmentNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 10),
    _CcsCmFlapPowerAdjustmentNum_Type()
)
ccsCmFlapPowerAdjustmentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapPowerAdjustmentNum.setStatus("current")
_CcsCmFlapTotalNum_Type = Unsigned32
_CcsCmFlapTotalNum_Object = MibTableColumn
ccsCmFlapTotalNum = _CcsCmFlapTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 11),
    _CcsCmFlapTotalNum_Type()
)
ccsCmFlapTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapTotalNum.setStatus("current")
_CcsCmFlapResetNow_Type = TruthValue
_CcsCmFlapResetNow_Object = MibTableColumn
ccsCmFlapResetNow = _CcsCmFlapResetNow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 12),
    _CcsCmFlapResetNow_Type()
)
ccsCmFlapResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsCmFlapResetNow.setStatus("current")
_CcsCmFlapLastResetTime_Type = DateAndTime
_CcsCmFlapLastResetTime_Object = MibTableColumn
ccsCmFlapLastResetTime = _CcsCmFlapLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 13),
    _CcsCmFlapLastResetTime_Type()
)
ccsCmFlapLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsCmFlapLastResetTime.setStatus("current")
_CcsCmFlapRowStatus_Type = RowStatus
_CcsCmFlapRowStatus_Object = MibTableColumn
ccsCmFlapRowStatus = _CcsCmFlapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 1, 11, 1, 14),
    _CcsCmFlapRowStatus_Type()
)
ccsCmFlapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsCmFlapRowStatus.setStatus("current")
_CcsSpectrumObjects_ObjectIdentity = ObjectIdentity
ccsSpectrumObjects = _CcsSpectrumObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2)
)
_CcsSpectrumRequestTable_Object = MibTable
ccsSpectrumRequestTable = _CcsSpectrumRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccsSpectrumRequestTable.setStatus("current")
_CcsSpectrumRequestEntry_Object = MibTableRow
ccsSpectrumRequestEntry = _CcsSpectrumRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1)
)
ccsSpectrumRequestEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestIndex"),
)
if mibBuilder.loadTexts:
    ccsSpectrumRequestEntry.setStatus("current")


class _CcsSpectrumRequestIndex_Type(Integer32):
    """Custom type ccsSpectrumRequestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcsSpectrumRequestIndex_Type.__name__ = "Integer32"
_CcsSpectrumRequestIndex_Object = MibTableColumn
ccsSpectrumRequestIndex = _CcsSpectrumRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 1),
    _CcsSpectrumRequestIndex_Type()
)
ccsSpectrumRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsSpectrumRequestIndex.setStatus("current")
_CcsSpectrumRequestIfIndex_Type = InterfaceIndexOrZero
_CcsSpectrumRequestIfIndex_Object = MibTableColumn
ccsSpectrumRequestIfIndex = _CcsSpectrumRequestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 2),
    _CcsSpectrumRequestIfIndex_Type()
)
ccsSpectrumRequestIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestIfIndex.setStatus("current")


class _CcsSpectrumRequestMacAddr_Type(MacAddress):
    """Custom type ccsSpectrumRequestMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_CcsSpectrumRequestMacAddr_Object = MibTableColumn
ccsSpectrumRequestMacAddr = _CcsSpectrumRequestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 3),
    _CcsSpectrumRequestMacAddr_Type()
)
ccsSpectrumRequestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestMacAddr.setStatus("current")


class _CcsSpectrumRequestLowFreq_Type(CCSFrequency):
    """Custom type ccsSpectrumRequestLowFreq based on CCSFrequency"""
    defaultValue = 5000


_CcsSpectrumRequestLowFreq_Object = MibTableColumn
ccsSpectrumRequestLowFreq = _CcsSpectrumRequestLowFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 4),
    _CcsSpectrumRequestLowFreq_Type()
)
ccsSpectrumRequestLowFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestLowFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpectrumRequestLowFreq.setUnits("KHz")


class _CcsSpectrumRequestUpperFreq_Type(CCSFrequency):
    """Custom type ccsSpectrumRequestUpperFreq based on CCSFrequency"""
    defaultValue = 42000


_CcsSpectrumRequestUpperFreq_Object = MibTableColumn
ccsSpectrumRequestUpperFreq = _CcsSpectrumRequestUpperFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 5),
    _CcsSpectrumRequestUpperFreq_Type()
)
ccsSpectrumRequestUpperFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestUpperFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpectrumRequestUpperFreq.setUnits("KHz")


class _CcsSpectrumRequestResolution_Type(Integer32):
    """Custom type ccsSpectrumRequestResolution based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 37000),
    )


_CcsSpectrumRequestResolution_Type.__name__ = "Integer32"
_CcsSpectrumRequestResolution_Object = MibTableColumn
ccsSpectrumRequestResolution = _CcsSpectrumRequestResolution_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 6),
    _CcsSpectrumRequestResolution_Type()
)
ccsSpectrumRequestResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestResolution.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpectrumRequestResolution.setUnits("KHz")


class _CcsSpectrumRequestOperation_Type(CCSRequestOperation):
    """Custom type ccsSpectrumRequestOperation based on CCSRequestOperation"""


_CcsSpectrumRequestOperation_Object = MibTableColumn
ccsSpectrumRequestOperation = _CcsSpectrumRequestOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 7),
    _CcsSpectrumRequestOperation_Type()
)
ccsSpectrumRequestOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestOperation.setStatus("current")
_CcsSpectrumRequestOperState_Type = CCSRequestOperState
_CcsSpectrumRequestOperState_Object = MibTableColumn
ccsSpectrumRequestOperState = _CcsSpectrumRequestOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 8),
    _CcsSpectrumRequestOperState_Type()
)
ccsSpectrumRequestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSpectrumRequestOperState.setStatus("current")
_CcsSpectrumRequestStartTime_Type = TimeStamp
_CcsSpectrumRequestStartTime_Object = MibTableColumn
ccsSpectrumRequestStartTime = _CcsSpectrumRequestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 9),
    _CcsSpectrumRequestStartTime_Type()
)
ccsSpectrumRequestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSpectrumRequestStartTime.setStatus("current")
_CcsSpectrumRequestStoppedTime_Type = TimeStamp
_CcsSpectrumRequestStoppedTime_Object = MibTableColumn
ccsSpectrumRequestStoppedTime = _CcsSpectrumRequestStoppedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 10),
    _CcsSpectrumRequestStoppedTime_Type()
)
ccsSpectrumRequestStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSpectrumRequestStoppedTime.setStatus("current")
_CcsSpectrumRequestStatus_Type = RowStatus
_CcsSpectrumRequestStatus_Object = MibTableColumn
ccsSpectrumRequestStatus = _CcsSpectrumRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 1, 1, 11),
    _CcsSpectrumRequestStatus_Type()
)
ccsSpectrumRequestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpectrumRequestStatus.setStatus("current")
_CcsSpectrumDataTable_Object = MibTable
ccsSpectrumDataTable = _CcsSpectrumDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccsSpectrumDataTable.setStatus("current")
_CcsSpectrumDataEntry_Object = MibTableRow
ccsSpectrumDataEntry = _CcsSpectrumDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 2, 1)
)
ccsSpectrumDataEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestIndex"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumDataFreq"),
)
if mibBuilder.loadTexts:
    ccsSpectrumDataEntry.setStatus("current")
_CcsSpectrumDataFreq_Type = CCSMeasuredFrequency
_CcsSpectrumDataFreq_Object = MibTableColumn
ccsSpectrumDataFreq = _CcsSpectrumDataFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 2, 1, 1),
    _CcsSpectrumDataFreq_Type()
)
ccsSpectrumDataFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSpectrumDataFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpectrumDataFreq.setUnits("KHz")


class _CcsSpectrumDataPower_Type(Integer32):
    """Custom type ccsSpectrumDataPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 50),
    )


_CcsSpectrumDataPower_Type.__name__ = "Integer32"
_CcsSpectrumDataPower_Object = MibTableColumn
ccsSpectrumDataPower = _CcsSpectrumDataPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 2, 1, 2),
    _CcsSpectrumDataPower_Type()
)
ccsSpectrumDataPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSpectrumDataPower.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpectrumDataPower.setUnits("dBmV")
_CcsSNRRequestTable_Object = MibTable
ccsSNRRequestTable = _CcsSNRRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ccsSNRRequestTable.setStatus("current")
_CcsSNRRequestEntry_Object = MibTableRow
ccsSNRRequestEntry = _CcsSNRRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1)
)
ccsSNRRequestEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestIndex"),
)
if mibBuilder.loadTexts:
    ccsSNRRequestEntry.setStatus("current")


class _CcsSNRRequestIndex_Type(Integer32):
    """Custom type ccsSNRRequestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcsSNRRequestIndex_Type.__name__ = "Integer32"
_CcsSNRRequestIndex_Object = MibTableColumn
ccsSNRRequestIndex = _CcsSNRRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 1),
    _CcsSNRRequestIndex_Type()
)
ccsSNRRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsSNRRequestIndex.setStatus("current")
_CcsSNRRequestMacAddr_Type = MacAddress
_CcsSNRRequestMacAddr_Object = MibTableColumn
ccsSNRRequestMacAddr = _CcsSNRRequestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 2),
    _CcsSNRRequestMacAddr_Type()
)
ccsSNRRequestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSNRRequestMacAddr.setStatus("current")


class _CcsSNRRequestSNR_Type(Integer32):
    """Custom type ccsSNRRequestSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CcsSNRRequestSNR_Type.__name__ = "Integer32"
_CcsSNRRequestSNR_Object = MibTableColumn
ccsSNRRequestSNR = _CcsSNRRequestSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 3),
    _CcsSNRRequestSNR_Type()
)
ccsSNRRequestSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSNRRequestSNR.setStatus("current")
if mibBuilder.loadTexts:
    ccsSNRRequestSNR.setUnits("dB")


class _CcsSNRRequestOperation_Type(CCSRequestOperation):
    """Custom type ccsSNRRequestOperation based on CCSRequestOperation"""


_CcsSNRRequestOperation_Object = MibTableColumn
ccsSNRRequestOperation = _CcsSNRRequestOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 4),
    _CcsSNRRequestOperation_Type()
)
ccsSNRRequestOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSNRRequestOperation.setStatus("current")
_CcsSNRRequestOperState_Type = CCSRequestOperState
_CcsSNRRequestOperState_Object = MibTableColumn
ccsSNRRequestOperState = _CcsSNRRequestOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 5),
    _CcsSNRRequestOperState_Type()
)
ccsSNRRequestOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSNRRequestOperState.setStatus("current")
_CcsSNRRequestStartTime_Type = TimeStamp
_CcsSNRRequestStartTime_Object = MibTableColumn
ccsSNRRequestStartTime = _CcsSNRRequestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 6),
    _CcsSNRRequestStartTime_Type()
)
ccsSNRRequestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSNRRequestStartTime.setStatus("current")
_CcsSNRRequestStoppedTime_Type = TimeStamp
_CcsSNRRequestStoppedTime_Object = MibTableColumn
ccsSNRRequestStoppedTime = _CcsSNRRequestStoppedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 7),
    _CcsSNRRequestStoppedTime_Type()
)
ccsSNRRequestStoppedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsSNRRequestStoppedTime.setStatus("current")
_CcsSNRRequestStatus_Type = RowStatus
_CcsSNRRequestStatus_Object = MibTableColumn
ccsSNRRequestStatus = _CcsSNRRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 3, 1, 8),
    _CcsSNRRequestStatus_Type()
)
ccsSNRRequestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSNRRequestStatus.setStatus("current")
_CcsUpInSpecGroupTable_Object = MibTable
ccsUpInSpecGroupTable = _CcsUpInSpecGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ccsUpInSpecGroupTable.setStatus("current")
_CcsUpInSpecGroupEntry_Object = MibTableRow
ccsUpInSpecGroupEntry = _CcsUpInSpecGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4, 1)
)
ccsUpInSpecGroupEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupNumber"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupUpstreamIfIndex"),
)
if mibBuilder.loadTexts:
    ccsUpInSpecGroupEntry.setStatus("current")


class _CcsSpecGroupNumber_Type(Unsigned32):
    """Custom type ccsSpecGroupNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcsSpecGroupNumber_Type.__name__ = "Unsigned32"
_CcsSpecGroupNumber_Object = MibTableColumn
ccsSpecGroupNumber = _CcsSpecGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4, 1, 1),
    _CcsSpecGroupNumber_Type()
)
ccsSpecGroupNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsSpecGroupNumber.setStatus("current")
_CcsSpecGroupUpstreamIfIndex_Type = InterfaceIndex
_CcsSpecGroupUpstreamIfIndex_Object = MibTableColumn
ccsSpecGroupUpstreamIfIndex = _CcsSpecGroupUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4, 1, 2),
    _CcsSpecGroupUpstreamIfIndex_Type()
)
ccsSpecGroupUpstreamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsSpecGroupUpstreamIfIndex.setStatus("current")
_CcsSpecGroupUpstreamStorage_Type = StorageType
_CcsSpecGroupUpstreamStorage_Object = MibTableColumn
ccsSpecGroupUpstreamStorage = _CcsSpecGroupUpstreamStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4, 1, 3),
    _CcsSpecGroupUpstreamStorage_Type()
)
ccsSpecGroupUpstreamStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupUpstreamStorage.setStatus("current")
_CcsSpecGroupUpstreamRowStatus_Type = RowStatus
_CcsSpecGroupUpstreamRowStatus_Object = MibTableColumn
ccsSpecGroupUpstreamRowStatus = _CcsSpecGroupUpstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 4, 1, 4),
    _CcsSpecGroupUpstreamRowStatus_Type()
)
ccsSpecGroupUpstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupUpstreamRowStatus.setStatus("current")
_CcsUpInFiberNodeTable_Object = MibTable
ccsUpInFiberNodeTable = _CcsUpInFiberNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ccsUpInFiberNodeTable.setStatus("current")
_CcsUpInFiberNodeEntry_Object = MibTableRow
ccsUpInFiberNodeEntry = _CcsUpInFiberNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5, 1)
)
ccsUpInFiberNodeEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsFiberNodeNumber"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsFiberNodeUpstreamIfIndex"),
)
if mibBuilder.loadTexts:
    ccsUpInFiberNodeEntry.setStatus("current")


class _CcsFiberNodeNumber_Type(Unsigned32):
    """Custom type ccsFiberNodeNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcsFiberNodeNumber_Type.__name__ = "Unsigned32"
_CcsFiberNodeNumber_Object = MibTableColumn
ccsFiberNodeNumber = _CcsFiberNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5, 1, 1),
    _CcsFiberNodeNumber_Type()
)
ccsFiberNodeNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsFiberNodeNumber.setStatus("current")
_CcsFiberNodeUpstreamIfIndex_Type = InterfaceIndex
_CcsFiberNodeUpstreamIfIndex_Object = MibTableColumn
ccsFiberNodeUpstreamIfIndex = _CcsFiberNodeUpstreamIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5, 1, 2),
    _CcsFiberNodeUpstreamIfIndex_Type()
)
ccsFiberNodeUpstreamIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsFiberNodeUpstreamIfIndex.setStatus("current")
_CcsFiberNodeUpstreamStorage_Type = StorageType
_CcsFiberNodeUpstreamStorage_Object = MibTableColumn
ccsFiberNodeUpstreamStorage = _CcsFiberNodeUpstreamStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5, 1, 3),
    _CcsFiberNodeUpstreamStorage_Type()
)
ccsFiberNodeUpstreamStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsFiberNodeUpstreamStorage.setStatus("current")
_CcsFiberNodeUpstreamRowStatus_Type = RowStatus
_CcsFiberNodeUpstreamRowStatus_Object = MibTableColumn
ccsFiberNodeUpstreamRowStatus = _CcsFiberNodeUpstreamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 2, 5, 1, 4),
    _CcsFiberNodeUpstreamRowStatus_Type()
)
ccsFiberNodeUpstreamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsFiberNodeUpstreamRowStatus.setStatus("current")
_CcsConfigObjects_ObjectIdentity = ObjectIdentity
ccsConfigObjects = _CcsConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3)
)
_CcsUpSpecMgmtTable_Object = MibTable
ccsUpSpecMgmtTable = _CcsUpSpecMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtTable.setStatus("current")
_CcsUpSpecMgmtEntry_Object = MibTableRow
ccsUpSpecMgmtEntry = _CcsUpSpecMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1)
)
ccsUpSpecMgmtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtEntry.setStatus("current")


class _CcsUpSpecMgmtHopPriority_Type(Integer32):
    """Custom type ccsUpSpecMgmtHopPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("channelFrqMod", 4),
          ("channelModFrq", 5),
          ("frqChannelMod", 1),
          ("frqModChannel", 0),
          ("modChannelFrq", 3),
          ("modFrqChannel", 2))
    )


_CcsUpSpecMgmtHopPriority_Type.__name__ = "Integer32"
_CcsUpSpecMgmtHopPriority_Object = MibTableColumn
ccsUpSpecMgmtHopPriority = _CcsUpSpecMgmtHopPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 1),
    _CcsUpSpecMgmtHopPriority_Type()
)
ccsUpSpecMgmtHopPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtHopPriority.setStatus("current")


class _CcsUpSpecMgmtSnrThres1_Type(Integer32):
    """Custom type ccsUpSpecMgmtSnrThres1 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 35),
    )


_CcsUpSpecMgmtSnrThres1_Type.__name__ = "Integer32"
_CcsUpSpecMgmtSnrThres1_Object = MibTableColumn
ccsUpSpecMgmtSnrThres1 = _CcsUpSpecMgmtSnrThres1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 2),
    _CcsUpSpecMgmtSnrThres1_Type()
)
ccsUpSpecMgmtSnrThres1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrThres1.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrThres1.setUnits("dB")


class _CcsUpSpecMgmtSnrThres2_Type(Integer32):
    """Custom type ccsUpSpecMgmtSnrThres2 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 35),
    )


_CcsUpSpecMgmtSnrThres2_Type.__name__ = "Integer32"
_CcsUpSpecMgmtSnrThres2_Object = MibTableColumn
ccsUpSpecMgmtSnrThres2 = _CcsUpSpecMgmtSnrThres2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 3),
    _CcsUpSpecMgmtSnrThres2_Type()
)
ccsUpSpecMgmtSnrThres2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrThres2.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrThres2.setUnits("dB")


class _CcsUpSpecMgmtFecCorrectThres1_Type(Integer32):
    """Custom type ccsUpSpecMgmtFecCorrectThres1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )


_CcsUpSpecMgmtFecCorrectThres1_Type.__name__ = "Integer32"
_CcsUpSpecMgmtFecCorrectThres1_Object = MibTableColumn
ccsUpSpecMgmtFecCorrectThres1 = _CcsUpSpecMgmtFecCorrectThres1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 4),
    _CcsUpSpecMgmtFecCorrectThres1_Type()
)
ccsUpSpecMgmtFecCorrectThres1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFecCorrectThres1.setStatus("current")


class _CcsUpSpecMgmtFecCorrectThres2_Type(Integer32):
    """Custom type ccsUpSpecMgmtFecCorrectThres2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CcsUpSpecMgmtFecCorrectThres2_Type.__name__ = "Integer32"
_CcsUpSpecMgmtFecCorrectThres2_Object = MibTableColumn
ccsUpSpecMgmtFecCorrectThres2 = _CcsUpSpecMgmtFecCorrectThres2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 5),
    _CcsUpSpecMgmtFecCorrectThres2_Type()
)
ccsUpSpecMgmtFecCorrectThres2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFecCorrectThres2.setStatus("deprecated")


class _CcsUpSpecMgmtFecUnCorrectThres1_Type(Integer32):
    """Custom type ccsUpSpecMgmtFecUnCorrectThres1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )


_CcsUpSpecMgmtFecUnCorrectThres1_Type.__name__ = "Integer32"
_CcsUpSpecMgmtFecUnCorrectThres1_Object = MibTableColumn
ccsUpSpecMgmtFecUnCorrectThres1 = _CcsUpSpecMgmtFecUnCorrectThres1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 6),
    _CcsUpSpecMgmtFecUnCorrectThres1_Type()
)
ccsUpSpecMgmtFecUnCorrectThres1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFecUnCorrectThres1.setStatus("current")


class _CcsUpSpecMgmtFecUnCorrectThres2_Type(Integer32):
    """Custom type ccsUpSpecMgmtFecUnCorrectThres2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 30),
    )


_CcsUpSpecMgmtFecUnCorrectThres2_Type.__name__ = "Integer32"
_CcsUpSpecMgmtFecUnCorrectThres2_Object = MibTableColumn
ccsUpSpecMgmtFecUnCorrectThres2 = _CcsUpSpecMgmtFecUnCorrectThres2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 7),
    _CcsUpSpecMgmtFecUnCorrectThres2_Type()
)
ccsUpSpecMgmtFecUnCorrectThres2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFecUnCorrectThres2.setStatus("current")


class _CcsUpSpecMgmtSnrPollPeriod_Type(Integer32):
    """Custom type ccsUpSpecMgmtSnrPollPeriod based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 25000),
    )


_CcsUpSpecMgmtSnrPollPeriod_Type.__name__ = "Integer32"
_CcsUpSpecMgmtSnrPollPeriod_Object = MibTableColumn
ccsUpSpecMgmtSnrPollPeriod = _CcsUpSpecMgmtSnrPollPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 8),
    _CcsUpSpecMgmtSnrPollPeriod_Type()
)
ccsUpSpecMgmtSnrPollPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrPollPeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSnrPollPeriod.setUnits("msec")


class _CcsUpSpecMgmtHopCondition_Type(Integer32):
    """Custom type ccsUpSpecMgmtHopCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("others", 2),
          ("snr", 0),
          ("stationMaintainenceMiss", 1))
    )


_CcsUpSpecMgmtHopCondition_Type.__name__ = "Integer32"
_CcsUpSpecMgmtHopCondition_Object = MibTableColumn
ccsUpSpecMgmtHopCondition = _CcsUpSpecMgmtHopCondition_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 9),
    _CcsUpSpecMgmtHopCondition_Type()
)
ccsUpSpecMgmtHopCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtHopCondition.setStatus("deprecated")


class _CcsUpSpecMgmtFromCenterFreq_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtFromCenterFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 65000),
    )


_CcsUpSpecMgmtFromCenterFreq_Type.__name__ = "Unsigned32"
_CcsUpSpecMgmtFromCenterFreq_Object = MibTableColumn
ccsUpSpecMgmtFromCenterFreq = _CcsUpSpecMgmtFromCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 10),
    _CcsUpSpecMgmtFromCenterFreq_Type()
)
ccsUpSpecMgmtFromCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFromCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFromCenterFreq.setUnits("KHz")


class _CcsUpSpecMgmtToCenterFreq_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtToCenterFreq based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 65000),
    )


_CcsUpSpecMgmtToCenterFreq_Type.__name__ = "Unsigned32"
_CcsUpSpecMgmtToCenterFreq_Object = MibTableColumn
ccsUpSpecMgmtToCenterFreq = _CcsUpSpecMgmtToCenterFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 11),
    _CcsUpSpecMgmtToCenterFreq_Type()
)
ccsUpSpecMgmtToCenterFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtToCenterFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtToCenterFreq.setUnits("KHz")


class _CcsUpSpecMgmtFromBandWidth_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtFromBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(400, 400),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(1600, 1600),
        ValueRangeConstraint(3200, 3200),
        ValueRangeConstraint(6400, 6400),
    )


_CcsUpSpecMgmtFromBandWidth_Type.__name__ = "Unsigned32"
_CcsUpSpecMgmtFromBandWidth_Object = MibTableColumn
ccsUpSpecMgmtFromBandWidth = _CcsUpSpecMgmtFromBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 12),
    _CcsUpSpecMgmtFromBandWidth_Type()
)
ccsUpSpecMgmtFromBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFromBandWidth.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFromBandWidth.setUnits("KHz")


class _CcsUpSpecMgmtToBandWidth_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtToBandWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(400, 400),
        ValueRangeConstraint(800, 800),
        ValueRangeConstraint(1600, 1600),
        ValueRangeConstraint(3200, 3200),
        ValueRangeConstraint(6400, 6400),
    )


_CcsUpSpecMgmtToBandWidth_Type.__name__ = "Unsigned32"
_CcsUpSpecMgmtToBandWidth_Object = MibTableColumn
ccsUpSpecMgmtToBandWidth = _CcsUpSpecMgmtToBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 13),
    _CcsUpSpecMgmtToBandWidth_Type()
)
ccsUpSpecMgmtToBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtToBandWidth.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtToBandWidth.setUnits("KHz")


class _CcsUpSpecMgmtFromModProfile_Type(Integer32):
    """Custom type ccsUpSpecMgmtFromModProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcsUpSpecMgmtFromModProfile_Type.__name__ = "Integer32"
_CcsUpSpecMgmtFromModProfile_Object = MibTableColumn
ccsUpSpecMgmtFromModProfile = _CcsUpSpecMgmtFromModProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 14),
    _CcsUpSpecMgmtFromModProfile_Type()
)
ccsUpSpecMgmtFromModProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtFromModProfile.setStatus("current")


class _CcsUpSpecMgmtToModProfile_Type(Integer32):
    """Custom type ccsUpSpecMgmtToModProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcsUpSpecMgmtToModProfile_Type.__name__ = "Integer32"
_CcsUpSpecMgmtToModProfile_Object = MibTableColumn
ccsUpSpecMgmtToModProfile = _CcsUpSpecMgmtToModProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 15),
    _CcsUpSpecMgmtToModProfile_Type()
)
ccsUpSpecMgmtToModProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtToModProfile.setStatus("current")


class _CcsUpSpecMgmtSNR_Type(Integer32):
    """Custom type ccsUpSpecMgmtSNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CcsUpSpecMgmtSNR_Type.__name__ = "Integer32"
_CcsUpSpecMgmtSNR_Object = MibTableColumn
ccsUpSpecMgmtSNR = _CcsUpSpecMgmtSNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 16),
    _CcsUpSpecMgmtSNR_Type()
)
ccsUpSpecMgmtSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSNR.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSNR.setUnits("dB")
_CcsUpSpecMgmtUpperBoundFreq_Type = CCSFrequency
_CcsUpSpecMgmtUpperBoundFreq_Object = MibTableColumn
ccsUpSpecMgmtUpperBoundFreq = _CcsUpSpecMgmtUpperBoundFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 17),
    _CcsUpSpecMgmtUpperBoundFreq_Type()
)
ccsUpSpecMgmtUpperBoundFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtUpperBoundFreq.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtUpperBoundFreq.setUnits("KHz")


class _CcsUpSpecMgmtCnrThres1_Type(Integer32):
    """Custom type ccsUpSpecMgmtCnrThres1 based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 35),
    )


_CcsUpSpecMgmtCnrThres1_Type.__name__ = "Integer32"
_CcsUpSpecMgmtCnrThres1_Object = MibTableColumn
ccsUpSpecMgmtCnrThres1 = _CcsUpSpecMgmtCnrThres1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 18),
    _CcsUpSpecMgmtCnrThres1_Type()
)
ccsUpSpecMgmtCnrThres1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCnrThres1.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCnrThres1.setUnits("dB")


class _CcsUpSpecMgmtCnrThres2_Type(Integer32):
    """Custom type ccsUpSpecMgmtCnrThres2 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 35),
    )


_CcsUpSpecMgmtCnrThres2_Type.__name__ = "Integer32"
_CcsUpSpecMgmtCnrThres2_Object = MibTableColumn
ccsUpSpecMgmtCnrThres2 = _CcsUpSpecMgmtCnrThres2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 19),
    _CcsUpSpecMgmtCnrThres2_Type()
)
ccsUpSpecMgmtCnrThres2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCnrThres2.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCnrThres2.setUnits("dB")


class _CcsUpSpecMgmtCNR_Type(Integer32):
    """Custom type ccsUpSpecMgmtCNR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CcsUpSpecMgmtCNR_Type.__name__ = "Integer32"
_CcsUpSpecMgmtCNR_Object = MibTableColumn
ccsUpSpecMgmtCNR = _CcsUpSpecMgmtCNR_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 20),
    _CcsUpSpecMgmtCNR_Type()
)
ccsUpSpecMgmtCNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCNR.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCNR.setUnits("dB")


class _CcsUpSpecMgmtMissedMaintMsgThres_Type(Integer32):
    """Custom type ccsUpSpecMgmtMissedMaintMsgThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcsUpSpecMgmtMissedMaintMsgThres_Type.__name__ = "Integer32"
_CcsUpSpecMgmtMissedMaintMsgThres_Object = MibTableColumn
ccsUpSpecMgmtMissedMaintMsgThres = _CcsUpSpecMgmtMissedMaintMsgThres_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 21),
    _CcsUpSpecMgmtMissedMaintMsgThres_Type()
)
ccsUpSpecMgmtMissedMaintMsgThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtMissedMaintMsgThres.setStatus("current")


class _CcsUpSpecMgmtHopPeriod_Type(Integer32):
    """Custom type ccsUpSpecMgmtHopPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 3600),
    )


_CcsUpSpecMgmtHopPeriod_Type.__name__ = "Integer32"
_CcsUpSpecMgmtHopPeriod_Object = MibTableColumn
ccsUpSpecMgmtHopPeriod = _CcsUpSpecMgmtHopPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 22),
    _CcsUpSpecMgmtHopPeriod_Type()
)
ccsUpSpecMgmtHopPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtHopPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtHopPeriod.setUnits("seconds")


class _CcsUpSpecMgmtCriteria_Type(Bits):
    """Custom type ccsUpSpecMgmtCriteria based on Bits"""
    namedValues = NamedValues(
        *(("cnrAboveThres", 5),
          ("cnrBelowThres", 1),
          ("corrFecAboveThres", 2),
          ("corrFecBelowThres", 6),
          ("noActiveModem", 8),
          ("others", 10),
          ("snrAboveThres", 4),
          ("snrBelowThres", 0),
          ("uncorrFecAboveSecondThres", 9),
          ("uncorrFecAboveThres", 3),
          ("uncorrFecBelowThres", 7))
    )

_CcsUpSpecMgmtCriteria_Type.__name__ = "Bits"
_CcsUpSpecMgmtCriteria_Object = MibTableColumn
ccsUpSpecMgmtCriteria = _CcsUpSpecMgmtCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 23),
    _CcsUpSpecMgmtCriteria_Type()
)
ccsUpSpecMgmtCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtCriteria.setStatus("current")


class _CcsUpSpecMgmtSpecGroup_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtSpecGroup based on Unsigned32"""
    defaultValue = 0


_CcsUpSpecMgmtSpecGroup_Object = MibTableColumn
ccsUpSpecMgmtSpecGroup = _CcsUpSpecMgmtSpecGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 24),
    _CcsUpSpecMgmtSpecGroup_Type()
)
ccsUpSpecMgmtSpecGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSpecGroup.setStatus("current")


class _CcsUpSpecMgmtSharedSpectrum_Type(Unsigned32):
    """Custom type ccsUpSpecMgmtSharedSpectrum based on Unsigned32"""
    defaultValue = 0


_CcsUpSpecMgmtSharedSpectrum_Object = MibTableColumn
ccsUpSpecMgmtSharedSpectrum = _CcsUpSpecMgmtSharedSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 1, 1, 25),
    _CcsUpSpecMgmtSharedSpectrum_Type()
)
ccsUpSpecMgmtSharedSpectrum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccsUpSpecMgmtSharedSpectrum.setStatus("current")
_CcsSpecGroupFreqTable_Object = MibTable
ccsSpecGroupFreqTable = _CcsSpecGroupFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ccsSpecGroupFreqTable.setStatus("current")
_CcsSpecGroupFreqEntry_Object = MibTableRow
ccsSpecGroupFreqEntry = _CcsSpecGroupFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1)
)
ccsSpecGroupFreqEntry.setIndexNames(
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupNumber"),
    (0, "CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupFreqIndex"),
)
if mibBuilder.loadTexts:
    ccsSpecGroupFreqEntry.setStatus("current")


class _CcsSpecGroupFreqIndex_Type(Unsigned32):
    """Custom type ccsSpecGroupFreqIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcsSpecGroupFreqIndex_Type.__name__ = "Unsigned32"
_CcsSpecGroupFreqIndex_Object = MibTableColumn
ccsSpecGroupFreqIndex = _CcsSpecGroupFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 1),
    _CcsSpecGroupFreqIndex_Type()
)
ccsSpecGroupFreqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqIndex.setStatus("current")


class _CcsSpecGroupFreqType_Type(Integer32):
    """Custom type ccsSpecGroupFreqType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandFreq", 2),
          ("centerFreq", 1))
    )


_CcsSpecGroupFreqType_Type.__name__ = "Integer32"
_CcsSpecGroupFreqType_Object = MibTableColumn
ccsSpecGroupFreqType = _CcsSpecGroupFreqType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 2),
    _CcsSpecGroupFreqType_Type()
)
ccsSpecGroupFreqType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqType.setStatus("current")


class _CcsSpecGroupFreqLower_Type(Integer32):
    """Custom type ccsSpecGroupFreqLower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CcsSpecGroupFreqLower_Type.__name__ = "Integer32"
_CcsSpecGroupFreqLower_Object = MibTableColumn
ccsSpecGroupFreqLower = _CcsSpecGroupFreqLower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 3),
    _CcsSpecGroupFreqLower_Type()
)
ccsSpecGroupFreqLower.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqLower.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqLower.setUnits("Hz")


class _CcsSpecGroupFreqUpper_Type(Integer32):
    """Custom type ccsSpecGroupFreqUpper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CcsSpecGroupFreqUpper_Type.__name__ = "Integer32"
_CcsSpecGroupFreqUpper_Object = MibTableColumn
ccsSpecGroupFreqUpper = _CcsSpecGroupFreqUpper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 4),
    _CcsSpecGroupFreqUpper_Type()
)
ccsSpecGroupFreqUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqUpper.setStatus("current")
if mibBuilder.loadTexts:
    ccsSpecGroupFreqUpper.setUnits("Hz")
_CcsSpecGroupStorage_Type = StorageType
_CcsSpecGroupStorage_Object = MibTableColumn
ccsSpecGroupStorage = _CcsSpecGroupStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 5),
    _CcsSpecGroupStorage_Type()
)
ccsSpecGroupStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupStorage.setStatus("current")
_CcsSpecGroupRowStatus_Type = RowStatus
_CcsSpecGroupRowStatus_Object = MibTableColumn
ccsSpecGroupRowStatus = _CcsSpecGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 1, 3, 2, 1, 6),
    _CcsSpecGroupRowStatus_Type()
)
ccsSpecGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccsSpecGroupRowStatus.setStatus("current")
_CiscoCableSpectrumMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoCableSpectrumMIBNotificationPrefix = _CiscoCableSpectrumMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 2)
)
_CcsMIBNotifications_ObjectIdentity = ObjectIdentity
ccsMIBNotifications = _CcsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 2, 0)
)
_CiscoCableSpectrumMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCableSpectrumMIBConformance = _CiscoCableSpectrumMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3)
)
_CiscoCableSpectrumMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableSpectrumMIBCompliances = _CiscoCableSpectrumMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1)
)
_CiscoCableSpectrumMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableSpectrumMIBGroups = _CiscoCableSpectrumMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2)
)

# Managed Objects groups

ccsFlapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 1)
)
ccsFlapGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListMaxSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListCurrentSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapAging"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapInsertionTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapUpstreamIfIndex"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapDownstreamIfIndex"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapInsertionFails"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapHits"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapMisses"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapCrcErrors"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapPowerAdjustments"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapTotal"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapLastFlapTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapCreateTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapRowStatus"))
)
if mibBuilder.loadTexts:
    ccsFlapGroup.setStatus("deprecated")

ccsSpectrumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 2)
)
ccsSpectrumGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestIfIndex"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestMacAddr"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestUpperFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestLowFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestResolution"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestStartTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestStoppedTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestOperation"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestOperState"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumRequestStatus"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumDataFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpectrumDataPower"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestMacAddr"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestSNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestStartTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestStoppedTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestOperation"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestOperState"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSNRRequestStatus"))
)
if mibBuilder.loadTexts:
    ccsSpectrumGroup.setStatus("current")

ccsUpSpecMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 3)
)
ccsUpSpecMgmtGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPriority"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrPollPeriod"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopCondition"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSNR"))
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtGroup.setStatus("deprecated")

ccsFlapGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 5)
)
ccsFlapGroupRev1.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListMaxSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListCurrentSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapAging"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapInsertionTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapUpstreamIfIndex"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapDownstreamIfIndex"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapLastFlapTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapCreateTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapRowStatus"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapInsertionFailNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapHitNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapMissNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapCrcErrorNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapPowerAdjustmentNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapTotalNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapResetNow"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapLastResetTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapPowerAdjustThreshold"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapMissThreshold"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapResetAll"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapClearAll"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapLastClearTime"))
)
if mibBuilder.loadTexts:
    ccsFlapGroupRev1.setStatus("deprecated")

ccsUpSpecMgmtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 6)
)
ccsUpSpecMgmtGroupRev1.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPriority"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopCondition"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSNR"))
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtGroupRev1.setStatus("deprecated")

ccsFlapGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 7)
)
ccsFlapGroupRev2.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListMaxSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapListCurrentSize"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapAging"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFlapInsertionTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapLastFlapTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapCreateTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapInsertionFailNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapHitNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapMissNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapCrcErrorNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapPowerAdjustmentNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapTotalNum"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapResetNow"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapLastResetTime"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsCmFlapRowStatus"))
)
if mibBuilder.loadTexts:
    ccsFlapGroupRev2.setStatus("current")

ccsUpSpecMgmtGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 8)
)
ccsUpSpecMgmtGroupRev2.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPriority"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopCondition"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtUpperBoundFreq"))
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtGroupRev2.setStatus("deprecated")

ccsUpSpecMgmtGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 10)
)
ccsUpSpecMgmtGroupRev3.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPriority"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtUpperBoundFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtMissedMaintMsgThres"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPeriod"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCriteria"))
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtGroupRev3.setStatus("deprecated")

ccsSpecGroupFreqGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 11)
)
ccsSpecGroupFreqGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupFreqType"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupFreqLower"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupFreqUpper"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupStorage"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ccsSpecGroupFreqGroup.setStatus("current")

ccsUpSpecMgmtGroupRev4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 12)
)
ccsUpSpecMgmtGroupRev4.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPriority"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFecUnCorrectThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtUpperBoundFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCnrThres1"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCnrThres2"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCNR"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtMissedMaintMsgThres"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopPeriod"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCriteria"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSpecGroup"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtSharedSpectrum"))
)
if mibBuilder.loadTexts:
    ccsUpSpecMgmtGroupRev4.setStatus("current")

ccsUpInSpecGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 13)
)
ccsUpInSpecGroupGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupUpstreamStorage"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecGroupUpstreamRowStatus"))
)
if mibBuilder.loadTexts:
    ccsUpInSpecGroupGroup.setStatus("current")

ccsUpInFiberNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 14)
)
ccsUpInFiberNodeGroup.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsFiberNodeUpstreamStorage"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsFiberNodeUpstreamRowStatus"))
)
if mibBuilder.loadTexts:
    ccsUpInFiberNodeGroup.setStatus("current")


# Notification objects

ccsHoppingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 2, 0, 1)
)
ccsHoppingNotification.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtHopCondition"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"))
)
if mibBuilder.loadTexts:
    ccsHoppingNotification.setStatus(
        "deprecated"
    )

ccsSpecMgmtNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 2, 0, 2)
)
ccsSpecMgmtNotification.setObjects(
      *(("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtCriteria"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToCenterFreq"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToBandWidth"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtFromModProfile"),
        ("CISCO-CABLE-SPECTRUM-MIB", "ccsUpSpecMgmtToModProfile"))
)
if mibBuilder.loadTexts:
    ccsSpecMgmtNotification.setStatus(
        "current"
    )


# Notifications groups

ccsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 4)
)
ccsNotificationGroup.setObjects(
    ("CISCO-CABLE-SPECTRUM-MIB", "ccsHoppingNotification")
)
if mibBuilder.loadTexts:
    ccsNotificationGroup.setStatus(
        "deprecated"
    )

ccsNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 2, 9)
)
ccsNotificationGroupRev1.setObjects(
    ("CISCO-CABLE-SPECTRUM-MIB", "ccsSpecMgmtNotification")
)
if mibBuilder.loadTexts:
    ccsNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ccsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ccsCompliance.setStatus(
        "obsolete"
    )

ccsCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ccsCompliance2.setStatus(
        "deprecated"
    )

ccsCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ccsCompliance3.setStatus(
        "deprecated"
    )

ccsCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ccsCompliance4.setStatus(
        "deprecated"
    )

ccsCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ccsCompliance5.setStatus(
        "deprecated"
    )

ccsCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ccsCompliance6.setStatus(
        "deprecated"
    )

ccsCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 114, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ccsCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-SPECTRUM-MIB",
    **{"CCSFrequency": CCSFrequency,
       "CCSMeasuredFrequency": CCSMeasuredFrequency,
       "CCSRequestOperation": CCSRequestOperation,
       "CCSRequestOperState": CCSRequestOperState,
       "ciscoCableSpectrumMIB": ciscoCableSpectrumMIB,
       "ciscoCableSpectrumMIBObjects": ciscoCableSpectrumMIBObjects,
       "ccsFlapObjects": ccsFlapObjects,
       "ccsFlapListMaxSize": ccsFlapListMaxSize,
       "ccsFlapListCurrentSize": ccsFlapListCurrentSize,
       "ccsFlapAging": ccsFlapAging,
       "ccsFlapInsertionTime": ccsFlapInsertionTime,
       "ccsFlapTable": ccsFlapTable,
       "ccsFlapEntry": ccsFlapEntry,
       "ccsFlapMacAddr": ccsFlapMacAddr,
       "ccsFlapUpstreamIfIndex": ccsFlapUpstreamIfIndex,
       "ccsFlapDownstreamIfIndex": ccsFlapDownstreamIfIndex,
       "ccsFlapInsertionFails": ccsFlapInsertionFails,
       "ccsFlapHits": ccsFlapHits,
       "ccsFlapMisses": ccsFlapMisses,
       "ccsFlapCrcErrors": ccsFlapCrcErrors,
       "ccsFlapPowerAdjustments": ccsFlapPowerAdjustments,
       "ccsFlapTotal": ccsFlapTotal,
       "ccsFlapLastFlapTime": ccsFlapLastFlapTime,
       "ccsFlapCreateTime": ccsFlapCreateTime,
       "ccsFlapRowStatus": ccsFlapRowStatus,
       "ccsFlapInsertionFailNum": ccsFlapInsertionFailNum,
       "ccsFlapHitNum": ccsFlapHitNum,
       "ccsFlapMissNum": ccsFlapMissNum,
       "ccsFlapCrcErrorNum": ccsFlapCrcErrorNum,
       "ccsFlapPowerAdjustmentNum": ccsFlapPowerAdjustmentNum,
       "ccsFlapTotalNum": ccsFlapTotalNum,
       "ccsFlapResetNow": ccsFlapResetNow,
       "ccsFlapLastResetTime": ccsFlapLastResetTime,
       "ccsFlapPowerAdjustThreshold": ccsFlapPowerAdjustThreshold,
       "ccsFlapMissThreshold": ccsFlapMissThreshold,
       "ccsFlapResetAll": ccsFlapResetAll,
       "ccsFlapClearAll": ccsFlapClearAll,
       "ccsFlapLastClearTime": ccsFlapLastClearTime,
       "ccsCmFlapTable": ccsCmFlapTable,
       "ccsCmFlapEntry": ccsCmFlapEntry,
       "ccsCmFlapDownstreamIfIndex": ccsCmFlapDownstreamIfIndex,
       "ccsCmFlapUpstreamIfIndex": ccsCmFlapUpstreamIfIndex,
       "ccsCmFlapMacAddr": ccsCmFlapMacAddr,
       "ccsCmFlapLastFlapTime": ccsCmFlapLastFlapTime,
       "ccsCmFlapCreateTime": ccsCmFlapCreateTime,
       "ccsCmFlapInsertionFailNum": ccsCmFlapInsertionFailNum,
       "ccsCmFlapHitNum": ccsCmFlapHitNum,
       "ccsCmFlapMissNum": ccsCmFlapMissNum,
       "ccsCmFlapCrcErrorNum": ccsCmFlapCrcErrorNum,
       "ccsCmFlapPowerAdjustmentNum": ccsCmFlapPowerAdjustmentNum,
       "ccsCmFlapTotalNum": ccsCmFlapTotalNum,
       "ccsCmFlapResetNow": ccsCmFlapResetNow,
       "ccsCmFlapLastResetTime": ccsCmFlapLastResetTime,
       "ccsCmFlapRowStatus": ccsCmFlapRowStatus,
       "ccsSpectrumObjects": ccsSpectrumObjects,
       "ccsSpectrumRequestTable": ccsSpectrumRequestTable,
       "ccsSpectrumRequestEntry": ccsSpectrumRequestEntry,
       "ccsSpectrumRequestIndex": ccsSpectrumRequestIndex,
       "ccsSpectrumRequestIfIndex": ccsSpectrumRequestIfIndex,
       "ccsSpectrumRequestMacAddr": ccsSpectrumRequestMacAddr,
       "ccsSpectrumRequestLowFreq": ccsSpectrumRequestLowFreq,
       "ccsSpectrumRequestUpperFreq": ccsSpectrumRequestUpperFreq,
       "ccsSpectrumRequestResolution": ccsSpectrumRequestResolution,
       "ccsSpectrumRequestOperation": ccsSpectrumRequestOperation,
       "ccsSpectrumRequestOperState": ccsSpectrumRequestOperState,
       "ccsSpectrumRequestStartTime": ccsSpectrumRequestStartTime,
       "ccsSpectrumRequestStoppedTime": ccsSpectrumRequestStoppedTime,
       "ccsSpectrumRequestStatus": ccsSpectrumRequestStatus,
       "ccsSpectrumDataTable": ccsSpectrumDataTable,
       "ccsSpectrumDataEntry": ccsSpectrumDataEntry,
       "ccsSpectrumDataFreq": ccsSpectrumDataFreq,
       "ccsSpectrumDataPower": ccsSpectrumDataPower,
       "ccsSNRRequestTable": ccsSNRRequestTable,
       "ccsSNRRequestEntry": ccsSNRRequestEntry,
       "ccsSNRRequestIndex": ccsSNRRequestIndex,
       "ccsSNRRequestMacAddr": ccsSNRRequestMacAddr,
       "ccsSNRRequestSNR": ccsSNRRequestSNR,
       "ccsSNRRequestOperation": ccsSNRRequestOperation,
       "ccsSNRRequestOperState": ccsSNRRequestOperState,
       "ccsSNRRequestStartTime": ccsSNRRequestStartTime,
       "ccsSNRRequestStoppedTime": ccsSNRRequestStoppedTime,
       "ccsSNRRequestStatus": ccsSNRRequestStatus,
       "ccsUpInSpecGroupTable": ccsUpInSpecGroupTable,
       "ccsUpInSpecGroupEntry": ccsUpInSpecGroupEntry,
       "ccsSpecGroupNumber": ccsSpecGroupNumber,
       "ccsSpecGroupUpstreamIfIndex": ccsSpecGroupUpstreamIfIndex,
       "ccsSpecGroupUpstreamStorage": ccsSpecGroupUpstreamStorage,
       "ccsSpecGroupUpstreamRowStatus": ccsSpecGroupUpstreamRowStatus,
       "ccsUpInFiberNodeTable": ccsUpInFiberNodeTable,
       "ccsUpInFiberNodeEntry": ccsUpInFiberNodeEntry,
       "ccsFiberNodeNumber": ccsFiberNodeNumber,
       "ccsFiberNodeUpstreamIfIndex": ccsFiberNodeUpstreamIfIndex,
       "ccsFiberNodeUpstreamStorage": ccsFiberNodeUpstreamStorage,
       "ccsFiberNodeUpstreamRowStatus": ccsFiberNodeUpstreamRowStatus,
       "ccsConfigObjects": ccsConfigObjects,
       "ccsUpSpecMgmtTable": ccsUpSpecMgmtTable,
       "ccsUpSpecMgmtEntry": ccsUpSpecMgmtEntry,
       "ccsUpSpecMgmtHopPriority": ccsUpSpecMgmtHopPriority,
       "ccsUpSpecMgmtSnrThres1": ccsUpSpecMgmtSnrThres1,
       "ccsUpSpecMgmtSnrThres2": ccsUpSpecMgmtSnrThres2,
       "ccsUpSpecMgmtFecCorrectThres1": ccsUpSpecMgmtFecCorrectThres1,
       "ccsUpSpecMgmtFecCorrectThres2": ccsUpSpecMgmtFecCorrectThres2,
       "ccsUpSpecMgmtFecUnCorrectThres1": ccsUpSpecMgmtFecUnCorrectThres1,
       "ccsUpSpecMgmtFecUnCorrectThres2": ccsUpSpecMgmtFecUnCorrectThres2,
       "ccsUpSpecMgmtSnrPollPeriod": ccsUpSpecMgmtSnrPollPeriod,
       "ccsUpSpecMgmtHopCondition": ccsUpSpecMgmtHopCondition,
       "ccsUpSpecMgmtFromCenterFreq": ccsUpSpecMgmtFromCenterFreq,
       "ccsUpSpecMgmtToCenterFreq": ccsUpSpecMgmtToCenterFreq,
       "ccsUpSpecMgmtFromBandWidth": ccsUpSpecMgmtFromBandWidth,
       "ccsUpSpecMgmtToBandWidth": ccsUpSpecMgmtToBandWidth,
       "ccsUpSpecMgmtFromModProfile": ccsUpSpecMgmtFromModProfile,
       "ccsUpSpecMgmtToModProfile": ccsUpSpecMgmtToModProfile,
       "ccsUpSpecMgmtSNR": ccsUpSpecMgmtSNR,
       "ccsUpSpecMgmtUpperBoundFreq": ccsUpSpecMgmtUpperBoundFreq,
       "ccsUpSpecMgmtCnrThres1": ccsUpSpecMgmtCnrThres1,
       "ccsUpSpecMgmtCnrThres2": ccsUpSpecMgmtCnrThres2,
       "ccsUpSpecMgmtCNR": ccsUpSpecMgmtCNR,
       "ccsUpSpecMgmtMissedMaintMsgThres": ccsUpSpecMgmtMissedMaintMsgThres,
       "ccsUpSpecMgmtHopPeriod": ccsUpSpecMgmtHopPeriod,
       "ccsUpSpecMgmtCriteria": ccsUpSpecMgmtCriteria,
       "ccsUpSpecMgmtSpecGroup": ccsUpSpecMgmtSpecGroup,
       "ccsUpSpecMgmtSharedSpectrum": ccsUpSpecMgmtSharedSpectrum,
       "ccsSpecGroupFreqTable": ccsSpecGroupFreqTable,
       "ccsSpecGroupFreqEntry": ccsSpecGroupFreqEntry,
       "ccsSpecGroupFreqIndex": ccsSpecGroupFreqIndex,
       "ccsSpecGroupFreqType": ccsSpecGroupFreqType,
       "ccsSpecGroupFreqLower": ccsSpecGroupFreqLower,
       "ccsSpecGroupFreqUpper": ccsSpecGroupFreqUpper,
       "ccsSpecGroupStorage": ccsSpecGroupStorage,
       "ccsSpecGroupRowStatus": ccsSpecGroupRowStatus,
       "ciscoCableSpectrumMIBNotificationPrefix": ciscoCableSpectrumMIBNotificationPrefix,
       "ccsMIBNotifications": ccsMIBNotifications,
       "ccsHoppingNotification": ccsHoppingNotification,
       "ccsSpecMgmtNotification": ccsSpecMgmtNotification,
       "ciscoCableSpectrumMIBConformance": ciscoCableSpectrumMIBConformance,
       "ciscoCableSpectrumMIBCompliances": ciscoCableSpectrumMIBCompliances,
       "ccsCompliance": ccsCompliance,
       "ccsCompliance2": ccsCompliance2,
       "ccsCompliance3": ccsCompliance3,
       "ccsCompliance4": ccsCompliance4,
       "ccsCompliance5": ccsCompliance5,
       "ccsCompliance6": ccsCompliance6,
       "ccsCompliance7": ccsCompliance7,
       "ciscoCableSpectrumMIBGroups": ciscoCableSpectrumMIBGroups,
       "ccsFlapGroup": ccsFlapGroup,
       "ccsSpectrumGroup": ccsSpectrumGroup,
       "ccsUpSpecMgmtGroup": ccsUpSpecMgmtGroup,
       "ccsNotificationGroup": ccsNotificationGroup,
       "ccsFlapGroupRev1": ccsFlapGroupRev1,
       "ccsUpSpecMgmtGroupRev1": ccsUpSpecMgmtGroupRev1,
       "ccsFlapGroupRev2": ccsFlapGroupRev2,
       "ccsUpSpecMgmtGroupRev2": ccsUpSpecMgmtGroupRev2,
       "ccsNotificationGroupRev1": ccsNotificationGroupRev1,
       "ccsUpSpecMgmtGroupRev3": ccsUpSpecMgmtGroupRev3,
       "ccsSpecGroupFreqGroup": ccsSpecGroupFreqGroup,
       "ccsUpSpecMgmtGroupRev4": ccsUpSpecMgmtGroupRev4,
       "ccsUpInSpecGroupGroup": ccsUpInSpecGroupGroup,
       "ccsUpInFiberNodeGroup": ccsUpInFiberNodeGroup}
)
