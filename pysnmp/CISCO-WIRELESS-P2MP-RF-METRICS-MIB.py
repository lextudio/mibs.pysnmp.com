# SNMP MIB module (CISCO-WIRELESS-P2MP-RF-METRICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-P2MP-RF-METRICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:40 2024
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

(CwrCollectionAction,
 CwrCollectionStatus,
 CwrFixedPointPrecision,
 CwrFixedPointScale,
 CwrFixedPointValue,
 CwrThreshLimitType,
 CwrUpdateTime,
 P2mpRadioSignalAttribute,
 P2mpSnapshotAttribute) = mibBuilder.importSymbols(
    "CISCO-WIRELESS-TC-MIB",
    "CwrCollectionAction",
    "CwrCollectionStatus",
    "CwrFixedPointPrecision",
    "CwrFixedPointScale",
    "CwrFixedPointValue",
    "CwrThreshLimitType",
    "CwrUpdateTime",
    "P2mpRadioSignalAttribute",
    "P2mpSnapshotAttribute")

(OwnerString,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString",
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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessRfMetricsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_P2mpRadioHistoryGroup_ObjectIdentity = ObjectIdentity
p2mpRadioHistoryGroup = _P2mpRadioHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1)
)
_P2mpHistCtrlTable_Object = MibTable
p2mpHistCtrlTable = _P2mpHistCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpHistCtrlTable.setStatus("current")
_P2mpHistCtrlEntry_Object = MibTableRow
p2mpHistCtrlEntry = _P2mpHistCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1)
)
p2mpHistCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"),
)
if mibBuilder.loadTexts:
    p2mpHistCtrlEntry.setStatus("current")
_P2mpHistSuMacAddress_Type = MacAddress
_P2mpHistSuMacAddress_Object = MibTableColumn
p2mpHistSuMacAddress = _P2mpHistSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 1),
    _P2mpHistSuMacAddress_Type()
)
p2mpHistSuMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHistSuMacAddress.setStatus("current")
_P2mpHistClass_Type = P2mpRadioSignalAttribute
_P2mpHistClass_Object = MibTableColumn
p2mpHistClass = _P2mpHistClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 2),
    _P2mpHistClass_Type()
)
p2mpHistClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHistClass.setStatus("current")


class _P2mpHistSize_Type(Integer32):
    """Custom type p2mpHistSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coarse", 2),
          ("fine", 1))
    )


_P2mpHistSize_Type.__name__ = "Integer32"
_P2mpHistSize_Object = MibTableColumn
p2mpHistSize = _P2mpHistSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 3),
    _P2mpHistSize_Type()
)
p2mpHistSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpHistSize.setStatus("current")
_P2mpHistSumScale_Type = CwrFixedPointScale
_P2mpHistSumScale_Object = MibTableColumn
p2mpHistSumScale = _P2mpHistSumScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 4),
    _P2mpHistSumScale_Type()
)
p2mpHistSumScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistSumScale.setStatus("current")
_P2mpHistSumPrecision_Type = CwrFixedPointPrecision
_P2mpHistSumPrecision_Object = MibTableColumn
p2mpHistSumPrecision = _P2mpHistSumPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 5),
    _P2mpHistSumPrecision_Type()
)
p2mpHistSumPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistSumPrecision.setStatus("current")


class _P2mpStartBinValue_Type(Integer32):
    """Custom type p2mpStartBinValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_P2mpStartBinValue_Type.__name__ = "Integer32"
_P2mpStartBinValue_Object = MibTableColumn
p2mpStartBinValue = _P2mpStartBinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 6),
    _P2mpStartBinValue_Type()
)
p2mpStartBinValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpStartBinValue.setStatus("current")


class _P2mpEndBinValue_Type(Integer32):
    """Custom type p2mpEndBinValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_P2mpEndBinValue_Type.__name__ = "Integer32"
_P2mpEndBinValue_Object = MibTableColumn
p2mpEndBinValue = _P2mpEndBinValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 7),
    _P2mpEndBinValue_Type()
)
p2mpEndBinValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpEndBinValue.setStatus("current")
_P2mpCollDuration_Type = CwrUpdateTime
_P2mpCollDuration_Object = MibTableColumn
p2mpCollDuration = _P2mpCollDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 8),
    _P2mpCollDuration_Type()
)
p2mpCollDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpCollDuration.setStatus("current")
if mibBuilder.loadTexts:
    p2mpCollDuration.setUnits("seconds")
_P2mpUpdateRate_Type = CwrUpdateTime
_P2mpUpdateRate_Object = MibTableColumn
p2mpUpdateRate = _P2mpUpdateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 9),
    _P2mpUpdateRate_Type()
)
p2mpUpdateRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpUpdateRate.setStatus("current")
if mibBuilder.loadTexts:
    p2mpUpdateRate.setUnits("seconds")
_P2mpPeriodicSum_Type = TruthValue
_P2mpPeriodicSum_Object = MibTableColumn
p2mpPeriodicSum = _P2mpPeriodicSum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 10),
    _P2mpPeriodicSum_Type()
)
p2mpPeriodicSum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpPeriodicSum.setStatus("current")
_P2mpHistOwner_Type = OwnerString
_P2mpHistOwner_Object = MibTableColumn
p2mpHistOwner = _P2mpHistOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 11),
    _P2mpHistOwner_Type()
)
p2mpHistOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpHistOwner.setStatus("current")
_P2mpHistAction_Type = CwrCollectionAction
_P2mpHistAction_Object = MibTableColumn
p2mpHistAction = _P2mpHistAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 12),
    _P2mpHistAction_Type()
)
p2mpHistAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpHistAction.setStatus("current")
_P2mpHistStatus_Type = CwrCollectionStatus
_P2mpHistStatus_Object = MibTableColumn
p2mpHistStatus = _P2mpHistStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 13),
    _P2mpHistStatus_Type()
)
p2mpHistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistStatus.setStatus("current")
_P2mpHistRowStatus_Type = RowStatus
_P2mpHistRowStatus_Object = MibTableColumn
p2mpHistRowStatus = _P2mpHistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 1, 1, 14),
    _P2mpHistRowStatus_Type()
)
p2mpHistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpHistRowStatus.setStatus("current")
_P2mpHistSummaryTable_Object = MibTable
p2mpHistSummaryTable = _P2mpHistSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2)
)
if mibBuilder.loadTexts:
    p2mpHistSummaryTable.setStatus("current")
_P2mpHistSummaryEntry_Object = MibTableRow
p2mpHistSummaryEntry = _P2mpHistSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1)
)
p2mpHistSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"),
)
if mibBuilder.loadTexts:
    p2mpHistSummaryEntry.setStatus("current")
_P2mpHistUpdateTime_Type = CwrUpdateTime
_P2mpHistUpdateTime_Object = MibTableColumn
p2mpHistUpdateTime = _P2mpHistUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 1),
    _P2mpHistUpdateTime_Type()
)
p2mpHistUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpHistUpdateTime.setUnits("seconds")
_P2mpHistMin_Type = CwrFixedPointValue
_P2mpHistMin_Object = MibTableColumn
p2mpHistMin = _P2mpHistMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 2),
    _P2mpHistMin_Type()
)
p2mpHistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistMin.setStatus("current")
_P2mpHistMax_Type = CwrFixedPointValue
_P2mpHistMax_Object = MibTableColumn
p2mpHistMax = _P2mpHistMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 3),
    _P2mpHistMax_Type()
)
p2mpHistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistMax.setStatus("current")
_P2mpHistMean_Type = CwrFixedPointValue
_P2mpHistMean_Object = MibTableColumn
p2mpHistMean = _P2mpHistMean_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 2, 1, 4),
    _P2mpHistMean_Type()
)
p2mpHistMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpHistMean.setStatus("current")
_P2mpHistDataTable_Object = MibTable
p2mpHistDataTable = _P2mpHistDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3)
)
if mibBuilder.loadTexts:
    p2mpHistDataTable.setStatus("current")
_P2mpHistDataEntry_Object = MibTableRow
p2mpHistDataEntry = _P2mpHistDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1)
)
p2mpHistDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistClass"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistBinIndex"),
)
if mibBuilder.loadTexts:
    p2mpHistDataEntry.setStatus("current")


class _P2mpHistBinIndex_Type(Integer32):
    """Custom type p2mpHistBinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_P2mpHistBinIndex_Type.__name__ = "Integer32"
_P2mpHistBinIndex_Object = MibTableColumn
p2mpHistBinIndex = _P2mpHistBinIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1, 1),
    _P2mpHistBinIndex_Type()
)
p2mpHistBinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpHistBinIndex.setStatus("current")


class _P2mpValue_Type(Integer32):
    """Custom type p2mpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_P2mpValue_Type.__name__ = "Integer32"
_P2mpValue_Object = MibTableColumn
p2mpValue = _P2mpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 1, 3, 1, 2),
    _P2mpValue_Type()
)
p2mpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpValue.setStatus("current")
_P2mpRadioTimelineGroup_ObjectIdentity = ObjectIdentity
p2mpRadioTimelineGroup = _P2mpRadioTimelineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2)
)
_P2mpTlCtrlTable_Object = MibTable
p2mpTlCtrlTable = _P2mpTlCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1)
)
if mibBuilder.loadTexts:
    p2mpTlCtrlTable.setStatus("current")
_P2mpTlCtrlEntry_Object = MibTableRow
p2mpTlCtrlEntry = _P2mpTlCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1)
)
p2mpTlCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"),
)
if mibBuilder.loadTexts:
    p2mpTlCtrlEntry.setStatus("current")
_P2mpTlSuMacAddress_Type = MacAddress
_P2mpTlSuMacAddress_Object = MibTableColumn
p2mpTlSuMacAddress = _P2mpTlSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 1),
    _P2mpTlSuMacAddress_Type()
)
p2mpTlSuMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpTlSuMacAddress.setStatus("current")
_P2mpTlClass_Type = P2mpRadioSignalAttribute
_P2mpTlClass_Object = MibTableColumn
p2mpTlClass = _P2mpTlClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 2),
    _P2mpTlClass_Type()
)
p2mpTlClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpTlClass.setStatus("current")
_P2mpTlThreshAttribute_Type = P2mpRadioSignalAttribute
_P2mpTlThreshAttribute_Object = MibTableColumn
p2mpTlThreshAttribute = _P2mpTlThreshAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 3),
    _P2mpTlThreshAttribute_Type()
)
p2mpTlThreshAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlThreshAttribute.setStatus("current")
_P2mpTlThreshType_Type = CwrThreshLimitType
_P2mpTlThreshType_Object = MibTableColumn
p2mpTlThreshType = _P2mpTlThreshType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 4),
    _P2mpTlThreshType_Type()
)
p2mpTlThreshType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlThreshType.setStatus("current")


class _P2mpTlNumDataValues_Type(Integer32):
    """Custom type p2mpTlNumDataValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpTlNumDataValues_Type.__name__ = "Integer32"
_P2mpTlNumDataValues_Object = MibTableColumn
p2mpTlNumDataValues = _P2mpTlNumDataValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 5),
    _P2mpTlNumDataValues_Type()
)
p2mpTlNumDataValues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlNumDataValues.setStatus("current")
if mibBuilder.loadTexts:
    p2mpTlNumDataValues.setUnits("number of data values")
_P2mpTlDataScale_Type = CwrFixedPointScale
_P2mpTlDataScale_Object = MibTableColumn
p2mpTlDataScale = _P2mpTlDataScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 6),
    _P2mpTlDataScale_Type()
)
p2mpTlDataScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlDataScale.setStatus("current")
_P2mpTlDataPrecision_Type = CwrFixedPointPrecision
_P2mpTlDataPrecision_Object = MibTableColumn
p2mpTlDataPrecision = _P2mpTlDataPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 7),
    _P2mpTlDataPrecision_Type()
)
p2mpTlDataPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlDataPrecision.setStatus("current")


class _P2mpTlSamplePeriod_Type(Integer32):
    """Custom type p2mpTlSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_P2mpTlSamplePeriod_Type.__name__ = "Integer32"
_P2mpTlSamplePeriod_Object = MibTableColumn
p2mpTlSamplePeriod = _P2mpTlSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 8),
    _P2mpTlSamplePeriod_Type()
)
p2mpTlSamplePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlSamplePeriod.setStatus("current")
if mibBuilder.loadTexts:
    p2mpTlSamplePeriod.setUnits("milliseconds")
_P2mpTlAction_Type = CwrCollectionAction
_P2mpTlAction_Object = MibTableColumn
p2mpTlAction = _P2mpTlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 9),
    _P2mpTlAction_Type()
)
p2mpTlAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlAction.setStatus("current")


class _P2mpTlPostTrigBufMgmt_Type(Integer32):
    """Custom type p2mpTlPostTrigBufMgmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("postTrigger", 2),
          ("preTrigger", 1))
    )


_P2mpTlPostTrigBufMgmt_Type.__name__ = "Integer32"
_P2mpTlPostTrigBufMgmt_Object = MibTableColumn
p2mpTlPostTrigBufMgmt = _P2mpTlPostTrigBufMgmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 10),
    _P2mpTlPostTrigBufMgmt_Type()
)
p2mpTlPostTrigBufMgmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlPostTrigBufMgmt.setStatus("current")
_P2mpTlOwner_Type = OwnerString
_P2mpTlOwner_Object = MibTableColumn
p2mpTlOwner = _P2mpTlOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 11),
    _P2mpTlOwner_Type()
)
p2mpTlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlOwner.setStatus("current")
_P2mpTlStatus_Type = CwrCollectionStatus
_P2mpTlStatus_Object = MibTableColumn
p2mpTlStatus = _P2mpTlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 12),
    _P2mpTlStatus_Type()
)
p2mpTlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlStatus.setStatus("current")
_P2mpTlRowStatus_Type = RowStatus
_P2mpTlRowStatus_Object = MibTableColumn
p2mpTlRowStatus = _P2mpTlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 1, 1, 13),
    _P2mpTlRowStatus_Type()
)
p2mpTlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpTlRowStatus.setStatus("current")
_P2mpTlSummaryTable_Object = MibTable
p2mpTlSummaryTable = _P2mpTlSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2)
)
if mibBuilder.loadTexts:
    p2mpTlSummaryTable.setStatus("current")
_P2mpTlSummaryEntry_Object = MibTableRow
p2mpTlSummaryEntry = _P2mpTlSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1)
)
p2mpTlSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"),
)
if mibBuilder.loadTexts:
    p2mpTlSummaryEntry.setStatus("current")
_P2mpTlUpdateTime_Type = CwrUpdateTime
_P2mpTlUpdateTime_Object = MibTableColumn
p2mpTlUpdateTime = _P2mpTlUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 1),
    _P2mpTlUpdateTime_Type()
)
p2mpTlUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlUpdateTime.setStatus("current")
if mibBuilder.loadTexts:
    p2mpTlUpdateTime.setUnits("seconds")


class _P2mpTlNumValues_Type(Integer32):
    """Custom type p2mpTlNumValues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_P2mpTlNumValues_Type.__name__ = "Integer32"
_P2mpTlNumValues_Object = MibTableColumn
p2mpTlNumValues = _P2mpTlNumValues_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 2),
    _P2mpTlNumValues_Type()
)
p2mpTlNumValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlNumValues.setStatus("current")


class _P2mpTlTriggerLoc_Type(Integer32):
    """Custom type p2mpTlTriggerLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_P2mpTlTriggerLoc_Type.__name__ = "Integer32"
_P2mpTlTriggerLoc_Object = MibTableColumn
p2mpTlTriggerLoc = _P2mpTlTriggerLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 2, 1, 3),
    _P2mpTlTriggerLoc_Type()
)
p2mpTlTriggerLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlTriggerLoc.setStatus("current")
_P2mpTlDataTable_Object = MibTable
p2mpTlDataTable = _P2mpTlDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3)
)
if mibBuilder.loadTexts:
    p2mpTlDataTable.setStatus("current")
_P2mpTlDataEntry_Object = MibTableRow
p2mpTlDataEntry = _P2mpTlDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1)
)
p2mpTlDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSuMacAddress"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlClass"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlValueIndex"),
)
if mibBuilder.loadTexts:
    p2mpTlDataEntry.setStatus("current")


class _P2mpTlValueIndex_Type(Integer32):
    """Custom type p2mpTlValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpTlValueIndex_Type.__name__ = "Integer32"
_P2mpTlValueIndex_Object = MibTableColumn
p2mpTlValueIndex = _P2mpTlValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1, 1),
    _P2mpTlValueIndex_Type()
)
p2mpTlValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpTlValueIndex.setStatus("current")
_P2mpTlValue_Type = CwrFixedPointValue
_P2mpTlValue_Object = MibTableColumn
p2mpTlValue = _P2mpTlValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 2, 3, 1, 2),
    _P2mpTlValue_Type()
)
p2mpTlValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpTlValue.setStatus("current")
_P2mpRadioThresholdGroup_ObjectIdentity = ObjectIdentity
p2mpRadioThresholdGroup = _P2mpRadioThresholdGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3)
)
_P2mpThresholdTable_Object = MibTable
p2mpThresholdTable = _P2mpThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1)
)
if mibBuilder.loadTexts:
    p2mpThresholdTable.setStatus("current")
_P2mpThresholdEntry_Object = MibTableRow
p2mpThresholdEntry = _P2mpThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1)
)
p2mpThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshSuMacAddr"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshAttribute"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshType"),
)
if mibBuilder.loadTexts:
    p2mpThresholdEntry.setStatus("current")
_P2mpThreshSuMacAddr_Type = MacAddress
_P2mpThreshSuMacAddr_Object = MibTableColumn
p2mpThreshSuMacAddr = _P2mpThreshSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 1),
    _P2mpThreshSuMacAddr_Type()
)
p2mpThreshSuMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpThreshSuMacAddr.setStatus("current")
_P2mpThreshAttribute_Type = P2mpRadioSignalAttribute
_P2mpThreshAttribute_Object = MibTableColumn
p2mpThreshAttribute = _P2mpThreshAttribute_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 2),
    _P2mpThreshAttribute_Type()
)
p2mpThreshAttribute.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpThreshAttribute.setStatus("current")
_P2mpThreshType_Type = CwrThreshLimitType
_P2mpThreshType_Object = MibTableColumn
p2mpThreshType = _P2mpThreshType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 3),
    _P2mpThreshType_Type()
)
p2mpThreshType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpThreshType.setStatus("current")


class _P2mpThreshValue_Type(Integer32):
    """Custom type p2mpThreshValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_P2mpThreshValue_Type.__name__ = "Integer32"
_P2mpThreshValue_Object = MibTableColumn
p2mpThreshValue = _P2mpThreshValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 4),
    _P2mpThreshValue_Type()
)
p2mpThreshValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpThreshValue.setStatus("current")
_P2mpThreshHysteresisTime_Type = TimeInterval
_P2mpThreshHysteresisTime_Object = MibTableColumn
p2mpThreshHysteresisTime = _P2mpThreshHysteresisTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 5),
    _P2mpThreshHysteresisTime_Type()
)
p2mpThreshHysteresisTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpThreshHysteresisTime.setStatus("current")
_P2mpThreshLimitTime_Type = TimeInterval
_P2mpThreshLimitTime_Object = MibTableColumn
p2mpThreshLimitTime = _P2mpThreshLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 6),
    _P2mpThreshLimitTime_Type()
)
p2mpThreshLimitTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpThreshLimitTime.setStatus("current")
_P2mpThreshRowStatus_Type = RowStatus
_P2mpThreshRowStatus_Object = MibTableColumn
p2mpThreshRowStatus = _P2mpThreshRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 1, 1, 7),
    _P2mpThreshRowStatus_Type()
)
p2mpThreshRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpThreshRowStatus.setStatus("current")
_P2mpRfMetricsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
p2mpRfMetricsMIBNotificationPrefix = _P2mpRfMetricsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2)
)
_P2mpRfMetricsMIBNotification_ObjectIdentity = ObjectIdentity
p2mpRfMetricsMIBNotification = _P2mpRfMetricsMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2, 0)
)
_P2mpRadioSnapshotGroup_ObjectIdentity = ObjectIdentity
p2mpRadioSnapshotGroup = _P2mpRadioSnapshotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4)
)
_P2mpSnapshotCtrlTable_Object = MibTable
p2mpSnapshotCtrlTable = _P2mpSnapshotCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1)
)
if mibBuilder.loadTexts:
    p2mpSnapshotCtrlTable.setStatus("current")
_P2mpSnapshotCtrlEntry_Object = MibTableRow
p2mpSnapshotCtrlEntry = _P2mpSnapshotCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1)
)
p2mpSnapshotCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"),
)
if mibBuilder.loadTexts:
    p2mpSnapshotCtrlEntry.setStatus("current")


class _P2mpSnapshotDspNum_Type(Integer32):
    """Custom type p2mpSnapshotDspNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_P2mpSnapshotDspNum_Type.__name__ = "Integer32"
_P2mpSnapshotDspNum_Object = MibTableColumn
p2mpSnapshotDspNum = _P2mpSnapshotDspNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 1),
    _P2mpSnapshotDspNum_Type()
)
p2mpSnapshotDspNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSnapshotDspNum.setStatus("current")
_P2mpSnapshotType_Type = P2mpSnapshotAttribute
_P2mpSnapshotType_Object = MibTableColumn
p2mpSnapshotType = _P2mpSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 2),
    _P2mpSnapshotType_Type()
)
p2mpSnapshotType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpSnapshotType.setStatus("current")
_P2mpSnapshotDataScale_Type = CwrFixedPointScale
_P2mpSnapshotDataScale_Object = MibTableColumn
p2mpSnapshotDataScale = _P2mpSnapshotDataScale_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 3),
    _P2mpSnapshotDataScale_Type()
)
p2mpSnapshotDataScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapshotDataScale.setStatus("current")
_P2mpSnapshotDataPrecision_Type = CwrFixedPointPrecision
_P2mpSnapshotDataPrecision_Object = MibTableColumn
p2mpSnapshotDataPrecision = _P2mpSnapshotDataPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 4),
    _P2mpSnapshotDataPrecision_Type()
)
p2mpSnapshotDataPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapshotDataPrecision.setStatus("current")
_P2mpSnapshotOwner_Type = OwnerString
_P2mpSnapshotOwner_Object = MibTableColumn
p2mpSnapshotOwner = _P2mpSnapshotOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 5),
    _P2mpSnapshotOwner_Type()
)
p2mpSnapshotOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpSnapshotOwner.setStatus("current")
_P2mpSnapshotAction_Type = CwrCollectionAction
_P2mpSnapshotAction_Object = MibTableColumn
p2mpSnapshotAction = _P2mpSnapshotAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 6),
    _P2mpSnapshotAction_Type()
)
p2mpSnapshotAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpSnapshotAction.setStatus("current")
_P2mpSnapshotStatus_Type = CwrCollectionStatus
_P2mpSnapshotStatus_Object = MibTableColumn
p2mpSnapshotStatus = _P2mpSnapshotStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 7),
    _P2mpSnapshotStatus_Type()
)
p2mpSnapshotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapshotStatus.setStatus("current")
_P2mpSnapshotRowStatus_Type = RowStatus
_P2mpSnapshotRowStatus_Object = MibTableColumn
p2mpSnapshotRowStatus = _P2mpSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 1, 1, 8),
    _P2mpSnapshotRowStatus_Type()
)
p2mpSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    p2mpSnapshotRowStatus.setStatus("current")
_P2mpSnapSummaryTable_Object = MibTable
p2mpSnapSummaryTable = _P2mpSnapSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2)
)
if mibBuilder.loadTexts:
    p2mpSnapSummaryTable.setStatus("current")
_P2mpSnapSummaryEntry_Object = MibTableRow
p2mpSnapSummaryEntry = _P2mpSnapSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1)
)
p2mpSnapSummaryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"),
)
if mibBuilder.loadTexts:
    p2mpSnapSummaryEntry.setStatus("current")


class _P2mpSnapAttr1Id_Type(Integer32):
    """Custom type p2mpSnapAttr1Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpSnapAttr1Id_Type.__name__ = "Integer32"
_P2mpSnapAttr1Id_Object = MibTableColumn
p2mpSnapAttr1Id = _P2mpSnapAttr1Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 2),
    _P2mpSnapAttr1Id_Type()
)
p2mpSnapAttr1Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr1Id.setStatus("current")


class _P2mpSnapAttr1Size_Type(Integer32):
    """Custom type p2mpSnapAttr1Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_P2mpSnapAttr1Size_Type.__name__ = "Integer32"
_P2mpSnapAttr1Size_Object = MibTableColumn
p2mpSnapAttr1Size = _P2mpSnapAttr1Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 3),
    _P2mpSnapAttr1Size_Type()
)
p2mpSnapAttr1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr1Size.setStatus("current")


class _P2mpSnapAttr2Id_Type(Integer32):
    """Custom type p2mpSnapAttr2Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpSnapAttr2Id_Type.__name__ = "Integer32"
_P2mpSnapAttr2Id_Object = MibTableColumn
p2mpSnapAttr2Id = _P2mpSnapAttr2Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 4),
    _P2mpSnapAttr2Id_Type()
)
p2mpSnapAttr2Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr2Id.setStatus("current")


class _P2mpSnapAttr2Size_Type(Integer32):
    """Custom type p2mpSnapAttr2Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_P2mpSnapAttr2Size_Type.__name__ = "Integer32"
_P2mpSnapAttr2Size_Object = MibTableColumn
p2mpSnapAttr2Size = _P2mpSnapAttr2Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 5),
    _P2mpSnapAttr2Size_Type()
)
p2mpSnapAttr2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr2Size.setStatus("current")


class _P2mpSnapAttr3Id_Type(Integer32):
    """Custom type p2mpSnapAttr3Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpSnapAttr3Id_Type.__name__ = "Integer32"
_P2mpSnapAttr3Id_Object = MibTableColumn
p2mpSnapAttr3Id = _P2mpSnapAttr3Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 6),
    _P2mpSnapAttr3Id_Type()
)
p2mpSnapAttr3Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr3Id.setStatus("current")


class _P2mpSnapAttr3Size_Type(Integer32):
    """Custom type p2mpSnapAttr3Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_P2mpSnapAttr3Size_Type.__name__ = "Integer32"
_P2mpSnapAttr3Size_Object = MibTableColumn
p2mpSnapAttr3Size = _P2mpSnapAttr3Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 7),
    _P2mpSnapAttr3Size_Type()
)
p2mpSnapAttr3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr3Size.setStatus("current")


class _P2mpSnapAttr4Id_Type(Integer32):
    """Custom type p2mpSnapAttr4Id based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_P2mpSnapAttr4Id_Type.__name__ = "Integer32"
_P2mpSnapAttr4Id_Object = MibTableColumn
p2mpSnapAttr4Id = _P2mpSnapAttr4Id_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 8),
    _P2mpSnapAttr4Id_Type()
)
p2mpSnapAttr4Id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr4Id.setStatus("current")


class _P2mpSnapAttr4Size_Type(Integer32):
    """Custom type p2mpSnapAttr4Size based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_P2mpSnapAttr4Size_Type.__name__ = "Integer32"
_P2mpSnapAttr4Size_Object = MibTableColumn
p2mpSnapAttr4Size = _P2mpSnapAttr4Size_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 2, 1, 9),
    _P2mpSnapAttr4Size_Type()
)
p2mpSnapAttr4Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpSnapAttr4Size.setStatus("current")
_P2mpSnapDataTable_Object = MibTable
p2mpSnapDataTable = _P2mpSnapDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3)
)
if mibBuilder.loadTexts:
    p2mpSnapDataTable.setStatus("current")
_P2mpSnapDataEntry_Object = MibTableRow
p2mpSnapDataEntry = _P2mpSnapDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1)
)
p2mpSnapDataEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDspNum"),
    (0, "CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapValueIndex"),
)
if mibBuilder.loadTexts:
    p2mpSnapDataEntry.setStatus("current")


class _P2mpSnapValueIndex_Type(Integer32):
    """Custom type p2mpSnapValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_P2mpSnapValueIndex_Type.__name__ = "Integer32"
_P2mpSnapValueIndex_Object = MibTableColumn
p2mpSnapValueIndex = _P2mpSnapValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 1),
    _P2mpSnapValueIndex_Type()
)
p2mpSnapValueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    p2mpSnapValueIndex.setStatus("current")
_P2mpRealPart_Type = CwrFixedPointValue
_P2mpRealPart_Object = MibTableColumn
p2mpRealPart = _P2mpRealPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 2),
    _P2mpRealPart_Type()
)
p2mpRealPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpRealPart.setStatus("current")
_P2mpImaginaryPart_Type = CwrFixedPointValue
_P2mpImaginaryPart_Object = MibTableColumn
p2mpImaginaryPart = _P2mpImaginaryPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 4, 3, 1, 3),
    _P2mpImaginaryPart_Type()
)
p2mpImaginaryPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    p2mpImaginaryPart.setStatus("current")
_P2mpRadioRfConformance_ObjectIdentity = ObjectIdentity
p2mpRadioRfConformance = _P2mpRadioRfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5)
)
_P2mpRadioRfCompliances_ObjectIdentity = ObjectIdentity
p2mpRadioRfCompliances = _P2mpRadioRfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 1)
)
_P2mpRadioRfGroups_ObjectIdentity = ObjectIdentity
p2mpRadioRfGroups = _P2mpRadioRfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2)
)

# Managed Objects groups

p2mpComplianceHistogramGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 1)
)
p2mpComplianceHistogramGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSize"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSumScale"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistSumPrecision"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpStartBinValue"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpEndBinValue"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpUpdateRate"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpCollDuration"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpPeriodicSum"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistOwner"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistAction"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistRowStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistUpdateTime"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMin"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMax"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpHistMean"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpValue"))
)
if mibBuilder.loadTexts:
    p2mpComplianceHistogramGroup.setStatus("current")

p2mpComplianceThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 2)
)
p2mpComplianceThresholdGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshValue"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshHysteresisTime"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshLimitTime"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshRowStatus"))
)
if mibBuilder.loadTexts:
    p2mpComplianceThresholdGroup.setStatus("current")

p2mpComplianceTimelineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 3)
)
p2mpComplianceTimelineGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlThreshAttribute"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlThreshType"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlNumDataValues"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlDataScale"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlDataPrecision"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlSamplePeriod"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlAction"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlPostTrigBufMgmt"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlOwner"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlRowStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlUpdateTime"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlNumValues"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlTriggerLoc"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpTlValue"))
)
if mibBuilder.loadTexts:
    p2mpComplianceTimelineGroup.setStatus("current")

p2mpComplianceSnapshotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 2, 4)
)
p2mpComplianceSnapshotGroup.setObjects(
      *(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotType"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDataScale"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotDataPrecision"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotOwner"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotAction"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapshotRowStatus"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr1Id"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr1Size"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr2Id"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr2Size"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr3Id"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr3Size"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr4Id"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpSnapAttr4Size"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpRealPart"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpImaginaryPart"))
)
if mibBuilder.loadTexts:
    p2mpComplianceSnapshotGroup.setStatus("current")


# Notification objects

p2mpTrapThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 3, 2, 0, 1)
)
p2mpTrapThresh.setObjects(
      *(("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshValue"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshHysteresisTime"),
        ("CISCO-WIRELESS-P2MP-RF-METRICS-MIB", "p2mpThreshLimitTime"))
)
if mibBuilder.loadTexts:
    p2mpTrapThresh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

p2mpRadioRfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 180, 5, 1, 1)
)
if mibBuilder.loadTexts:
    p2mpRadioRfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-P2MP-RF-METRICS-MIB",
    **{"ciscoWirelessRfMetricsMIB": ciscoWirelessRfMetricsMIB,
       "p2mpRadioHistoryGroup": p2mpRadioHistoryGroup,
       "p2mpHistCtrlTable": p2mpHistCtrlTable,
       "p2mpHistCtrlEntry": p2mpHistCtrlEntry,
       "p2mpHistSuMacAddress": p2mpHistSuMacAddress,
       "p2mpHistClass": p2mpHistClass,
       "p2mpHistSize": p2mpHistSize,
       "p2mpHistSumScale": p2mpHistSumScale,
       "p2mpHistSumPrecision": p2mpHistSumPrecision,
       "p2mpStartBinValue": p2mpStartBinValue,
       "p2mpEndBinValue": p2mpEndBinValue,
       "p2mpCollDuration": p2mpCollDuration,
       "p2mpUpdateRate": p2mpUpdateRate,
       "p2mpPeriodicSum": p2mpPeriodicSum,
       "p2mpHistOwner": p2mpHistOwner,
       "p2mpHistAction": p2mpHistAction,
       "p2mpHistStatus": p2mpHistStatus,
       "p2mpHistRowStatus": p2mpHistRowStatus,
       "p2mpHistSummaryTable": p2mpHistSummaryTable,
       "p2mpHistSummaryEntry": p2mpHistSummaryEntry,
       "p2mpHistUpdateTime": p2mpHistUpdateTime,
       "p2mpHistMin": p2mpHistMin,
       "p2mpHistMax": p2mpHistMax,
       "p2mpHistMean": p2mpHistMean,
       "p2mpHistDataTable": p2mpHistDataTable,
       "p2mpHistDataEntry": p2mpHistDataEntry,
       "p2mpHistBinIndex": p2mpHistBinIndex,
       "p2mpValue": p2mpValue,
       "p2mpRadioTimelineGroup": p2mpRadioTimelineGroup,
       "p2mpTlCtrlTable": p2mpTlCtrlTable,
       "p2mpTlCtrlEntry": p2mpTlCtrlEntry,
       "p2mpTlSuMacAddress": p2mpTlSuMacAddress,
       "p2mpTlClass": p2mpTlClass,
       "p2mpTlThreshAttribute": p2mpTlThreshAttribute,
       "p2mpTlThreshType": p2mpTlThreshType,
       "p2mpTlNumDataValues": p2mpTlNumDataValues,
       "p2mpTlDataScale": p2mpTlDataScale,
       "p2mpTlDataPrecision": p2mpTlDataPrecision,
       "p2mpTlSamplePeriod": p2mpTlSamplePeriod,
       "p2mpTlAction": p2mpTlAction,
       "p2mpTlPostTrigBufMgmt": p2mpTlPostTrigBufMgmt,
       "p2mpTlOwner": p2mpTlOwner,
       "p2mpTlStatus": p2mpTlStatus,
       "p2mpTlRowStatus": p2mpTlRowStatus,
       "p2mpTlSummaryTable": p2mpTlSummaryTable,
       "p2mpTlSummaryEntry": p2mpTlSummaryEntry,
       "p2mpTlUpdateTime": p2mpTlUpdateTime,
       "p2mpTlNumValues": p2mpTlNumValues,
       "p2mpTlTriggerLoc": p2mpTlTriggerLoc,
       "p2mpTlDataTable": p2mpTlDataTable,
       "p2mpTlDataEntry": p2mpTlDataEntry,
       "p2mpTlValueIndex": p2mpTlValueIndex,
       "p2mpTlValue": p2mpTlValue,
       "p2mpRadioThresholdGroup": p2mpRadioThresholdGroup,
       "p2mpThresholdTable": p2mpThresholdTable,
       "p2mpThresholdEntry": p2mpThresholdEntry,
       "p2mpThreshSuMacAddr": p2mpThreshSuMacAddr,
       "p2mpThreshAttribute": p2mpThreshAttribute,
       "p2mpThreshType": p2mpThreshType,
       "p2mpThreshValue": p2mpThreshValue,
       "p2mpThreshHysteresisTime": p2mpThreshHysteresisTime,
       "p2mpThreshLimitTime": p2mpThreshLimitTime,
       "p2mpThreshRowStatus": p2mpThreshRowStatus,
       "p2mpRfMetricsMIBNotificationPrefix": p2mpRfMetricsMIBNotificationPrefix,
       "p2mpRfMetricsMIBNotification": p2mpRfMetricsMIBNotification,
       "p2mpTrapThresh": p2mpTrapThresh,
       "p2mpRadioSnapshotGroup": p2mpRadioSnapshotGroup,
       "p2mpSnapshotCtrlTable": p2mpSnapshotCtrlTable,
       "p2mpSnapshotCtrlEntry": p2mpSnapshotCtrlEntry,
       "p2mpSnapshotDspNum": p2mpSnapshotDspNum,
       "p2mpSnapshotType": p2mpSnapshotType,
       "p2mpSnapshotDataScale": p2mpSnapshotDataScale,
       "p2mpSnapshotDataPrecision": p2mpSnapshotDataPrecision,
       "p2mpSnapshotOwner": p2mpSnapshotOwner,
       "p2mpSnapshotAction": p2mpSnapshotAction,
       "p2mpSnapshotStatus": p2mpSnapshotStatus,
       "p2mpSnapshotRowStatus": p2mpSnapshotRowStatus,
       "p2mpSnapSummaryTable": p2mpSnapSummaryTable,
       "p2mpSnapSummaryEntry": p2mpSnapSummaryEntry,
       "p2mpSnapAttr1Id": p2mpSnapAttr1Id,
       "p2mpSnapAttr1Size": p2mpSnapAttr1Size,
       "p2mpSnapAttr2Id": p2mpSnapAttr2Id,
       "p2mpSnapAttr2Size": p2mpSnapAttr2Size,
       "p2mpSnapAttr3Id": p2mpSnapAttr3Id,
       "p2mpSnapAttr3Size": p2mpSnapAttr3Size,
       "p2mpSnapAttr4Id": p2mpSnapAttr4Id,
       "p2mpSnapAttr4Size": p2mpSnapAttr4Size,
       "p2mpSnapDataTable": p2mpSnapDataTable,
       "p2mpSnapDataEntry": p2mpSnapDataEntry,
       "p2mpSnapValueIndex": p2mpSnapValueIndex,
       "p2mpRealPart": p2mpRealPart,
       "p2mpImaginaryPart": p2mpImaginaryPart,
       "p2mpRadioRfConformance": p2mpRadioRfConformance,
       "p2mpRadioRfCompliances": p2mpRadioRfCompliances,
       "p2mpRadioRfCompliance": p2mpRadioRfCompliance,
       "p2mpRadioRfGroups": p2mpRadioRfGroups,
       "p2mpComplianceHistogramGroup": p2mpComplianceHistogramGroup,
       "p2mpComplianceThresholdGroup": p2mpComplianceThresholdGroup,
       "p2mpComplianceTimelineGroup": p2mpComplianceTimelineGroup,
       "p2mpComplianceSnapshotGroup": p2mpComplianceSnapshotGroup}
)
