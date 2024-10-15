# SNMP MIB module (TIARA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:44 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(tiaraIpIfIndex,) = mibBuilder.importSymbols(
    "TIARA-IP-MIB",
    "tiaraIpIfIndex")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17)
)
tiaraQosMib.setRevisions(
        ("1900-02-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TiaraRedConfigTable_Object = MibTable
tiaraRedConfigTable = _TiaraRedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1)
)
if mibBuilder.loadTexts:
    tiaraRedConfigTable.setStatus("current")
_TiaraRedConfigEntry_Object = MibTableRow
tiaraRedConfigEntry = _TiaraRedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1)
)
tiaraRedConfigEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
)
if mibBuilder.loadTexts:
    tiaraRedConfigEntry.setStatus("current")
_RedTxMaxThreshold_Type = Integer32
_RedTxMaxThreshold_Object = MibTableColumn
redTxMaxThreshold = _RedTxMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 1),
    _RedTxMaxThreshold_Type()
)
redTxMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redTxMaxThreshold.setStatus("current")
_RedTxMinThreshold_Type = Integer32
_RedTxMinThreshold_Object = MibTableColumn
redTxMinThreshold = _RedTxMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 2),
    _RedTxMinThreshold_Type()
)
redTxMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redTxMinThreshold.setStatus("current")


class _RedTxWqBiasFactor_Type(Integer32):
    """Custom type redTxWqBiasFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_RedTxWqBiasFactor_Type.__name__ = "Integer32"
_RedTxWqBiasFactor_Object = MibTableColumn
redTxWqBiasFactor = _RedTxWqBiasFactor_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 3),
    _RedTxWqBiasFactor_Type()
)
redTxWqBiasFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redTxWqBiasFactor.setStatus("current")
_RedTxEnable_Type = TruthValue
_RedTxEnable_Object = MibTableColumn
redTxEnable = _RedTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 1, 1, 4),
    _RedTxEnable_Type()
)
redTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redTxEnable.setStatus("current")
_TiaraRedStatTable_Object = MibTable
tiaraRedStatTable = _TiaraRedStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2)
)
if mibBuilder.loadTexts:
    tiaraRedStatTable.setStatus("current")
_TiaraRedStatEntry_Object = MibTableRow
tiaraRedStatEntry = _TiaraRedStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1)
)
tiaraRedStatEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
)
if mibBuilder.loadTexts:
    tiaraRedStatEntry.setStatus("current")
_RedTxLoanedCount_Type = Counter32
_RedTxLoanedCount_Object = MibTableColumn
redTxLoanedCount = _RedTxLoanedCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 1),
    _RedTxLoanedCount_Type()
)
redTxLoanedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxLoanedCount.setStatus("current")
_RedTxMaxLoanedCount_Type = Counter32
_RedTxMaxLoanedCount_Object = MibTableColumn
redTxMaxLoanedCount = _RedTxMaxLoanedCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 2),
    _RedTxMaxLoanedCount_Type()
)
redTxMaxLoanedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMaxLoanedCount.setStatus("current")
_RedTxAvgQueueSize_Type = Counter32
_RedTxAvgQueueSize_Object = MibTableColumn
redTxAvgQueueSize = _RedTxAvgQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 3),
    _RedTxAvgQueueSize_Type()
)
redTxAvgQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxAvgQueueSize.setStatus("current")
_RedTxMaxAvgQueueSize_Type = Counter32
_RedTxMaxAvgQueueSize_Object = MibTableColumn
redTxMaxAvgQueueSize = _RedTxMaxAvgQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 4),
    _RedTxMaxAvgQueueSize_Type()
)
redTxMaxAvgQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMaxAvgQueueSize.setStatus("current")
_RedTxDropRate_Type = Counter32
_RedTxDropRate_Object = MibTableColumn
redTxDropRate = _RedTxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 5),
    _RedTxDropRate_Type()
)
redTxDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxDropRate.setStatus("current")
_RedTxMinThresholdSuccess_Type = Counter32
_RedTxMinThresholdSuccess_Object = MibTableColumn
redTxMinThresholdSuccess = _RedTxMinThresholdSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 6),
    _RedTxMinThresholdSuccess_Type()
)
redTxMinThresholdSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMinThresholdSuccess.setStatus("current")
_RedTxMaxThresholdFailure_Type = Counter32
_RedTxMaxThresholdFailure_Object = MibTableColumn
redTxMaxThresholdFailure = _RedTxMaxThresholdFailure_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 7),
    _RedTxMaxThresholdFailure_Type()
)
redTxMaxThresholdFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMaxThresholdFailure.setStatus("current")
_RedTxMinMaxRangeSuccess_Type = Counter32
_RedTxMinMaxRangeSuccess_Object = MibTableColumn
redTxMinMaxRangeSuccess = _RedTxMinMaxRangeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 8),
    _RedTxMinMaxRangeSuccess_Type()
)
redTxMinMaxRangeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMinMaxRangeSuccess.setStatus("current")
_RedTxMinMaxRangeFailure_Type = Counter32
_RedTxMinMaxRangeFailure_Object = MibTableColumn
redTxMinMaxRangeFailure = _RedTxMinMaxRangeFailure_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 9),
    _RedTxMinMaxRangeFailure_Type()
)
redTxMinMaxRangeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxMinMaxRangeFailure.setStatus("current")
_RedTxControlSuccess_Type = Counter32
_RedTxControlSuccess_Object = MibTableColumn
redTxControlSuccess = _RedTxControlSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 2, 1, 10),
    _RedTxControlSuccess_Type()
)
redTxControlSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redTxControlSuccess.setStatus("current")
_TiaraCbqConfigTable_Object = MibTable
tiaraCbqConfigTable = _TiaraCbqConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3)
)
if mibBuilder.loadTexts:
    tiaraCbqConfigTable.setStatus("current")
_TiaraCbqConfigEntry_Object = MibTableRow
tiaraCbqConfigEntry = _TiaraCbqConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1)
)
tiaraCbqConfigEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
    (0, "TIARA-QOS-MIB", "cbqClassIndex"),
)
if mibBuilder.loadTexts:
    tiaraCbqConfigEntry.setStatus("current")
_CbqClassIndex_Type = Integer32
_CbqClassIndex_Object = MibTableColumn
cbqClassIndex = _CbqClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 1),
    _CbqClassIndex_Type()
)
cbqClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassIndex.setStatus("current")
_CbqClassName_Type = DisplayString
_CbqClassName_Object = MibTableColumn
cbqClassName = _CbqClassName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 2),
    _CbqClassName_Type()
)
cbqClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassName.setStatus("current")
_CbqClassParentName_Type = DisplayString
_CbqClassParentName_Object = MibTableColumn
cbqClassParentName = _CbqClassParentName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 3),
    _CbqClassParentName_Type()
)
cbqClassParentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassParentName.setStatus("current")
_CbqClassBandwidth_Type = Integer32
_CbqClassBandwidth_Object = MibTableColumn
cbqClassBandwidth = _CbqClassBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 4),
    _CbqClassBandwidth_Type()
)
cbqClassBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassBandwidth.setStatus("current")
_CbqClassBurstTolerance_Type = Integer32
_CbqClassBurstTolerance_Object = MibTableColumn
cbqClassBurstTolerance = _CbqClassBurstTolerance_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 5),
    _CbqClassBurstTolerance_Type()
)
cbqClassBurstTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassBurstTolerance.setStatus("current")


class _CbqClassKeyType_Type(Integer32):
    """Custom type cbqClassKeyType based on Integer32"""
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
        *(("cbqClassifyDestIp", 3),
          ("cbqClassifyDestPort", 5),
          ("cbqClassifyProtocolType", 6),
          ("cbqClassifySrcIp", 2),
          ("cbqClassifySrcPort", 4),
          ("cbqClassifyTypeNotSet", 1),
          ("cbqClassifyVlanId", 7))
    )


_CbqClassKeyType_Type.__name__ = "Integer32"
_CbqClassKeyType_Object = MibTableColumn
cbqClassKeyType = _CbqClassKeyType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 6),
    _CbqClassKeyType_Type()
)
cbqClassKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyType.setStatus("current")
_CbqClassIsDefault_Type = TruthValue
_CbqClassIsDefault_Object = MibTableColumn
cbqClassIsDefault = _CbqClassIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 7),
    _CbqClassIsDefault_Type()
)
cbqClassIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassIsDefault.setStatus("current")
_CbqClassAverageBandwidth_Type = Integer32
_CbqClassAverageBandwidth_Object = MibTableColumn
cbqClassAverageBandwidth = _CbqClassAverageBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 3, 1, 8),
    _CbqClassAverageBandwidth_Type()
)
cbqClassAverageBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassAverageBandwidth.setStatus("current")
_TiaraCbqClassKeyTable_Object = MibTable
tiaraCbqClassKeyTable = _TiaraCbqClassKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4)
)
if mibBuilder.loadTexts:
    tiaraCbqClassKeyTable.setStatus("current")
_TiaraCbqClassKeyTableEntry_Object = MibTableRow
tiaraCbqClassKeyTableEntry = _TiaraCbqClassKeyTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1)
)
tiaraCbqClassKeyTableEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
    (0, "TIARA-QOS-MIB", "cbqClassIndex"),
    (0, "TIARA-QOS-MIB", "cbqClassKeyIndex"),
)
if mibBuilder.loadTexts:
    tiaraCbqClassKeyTableEntry.setStatus("current")
_CbqClassKeyIndex_Type = Integer32
_CbqClassKeyIndex_Object = MibTableColumn
cbqClassKeyIndex = _CbqClassKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 1),
    _CbqClassKeyIndex_Type()
)
cbqClassKeyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyIndex.setStatus("current")
_CbqKeyClassName_Type = DisplayString
_CbqKeyClassName_Object = MibTableColumn
cbqKeyClassName = _CbqKeyClassName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 2),
    _CbqKeyClassName_Type()
)
cbqKeyClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqKeyClassName.setStatus("current")
_CbqClassKeyVlanId_Type = Integer32
_CbqClassKeyVlanId_Object = MibTableColumn
cbqClassKeyVlanId = _CbqClassKeyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 3),
    _CbqClassKeyVlanId_Type()
)
cbqClassKeyVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyVlanId.setStatus("current")
_CbqClassKeyIpAddress_Type = IpAddress
_CbqClassKeyIpAddress_Object = MibTableColumn
cbqClassKeyIpAddress = _CbqClassKeyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 4),
    _CbqClassKeyIpAddress_Type()
)
cbqClassKeyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyIpAddress.setStatus("current")
_CbqClassKeyIpNetMask_Type = IpAddress
_CbqClassKeyIpNetMask_Object = MibTableColumn
cbqClassKeyIpNetMask = _CbqClassKeyIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 5),
    _CbqClassKeyIpNetMask_Type()
)
cbqClassKeyIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyIpNetMask.setStatus("current")
_CbqClassKeyPort_Type = Integer32
_CbqClassKeyPort_Object = MibTableColumn
cbqClassKeyPort = _CbqClassKeyPort_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 6),
    _CbqClassKeyPort_Type()
)
cbqClassKeyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyPort.setStatus("current")
_CbqClassKeyProtocolType_Type = Integer32
_CbqClassKeyProtocolType_Object = MibTableColumn
cbqClassKeyProtocolType = _CbqClassKeyProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 4, 1, 7),
    _CbqClassKeyProtocolType_Type()
)
cbqClassKeyProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassKeyProtocolType.setStatus("current")
_TiaraCbqStatsTable_Object = MibTable
tiaraCbqStatsTable = _TiaraCbqStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5)
)
if mibBuilder.loadTexts:
    tiaraCbqStatsTable.setStatus("current")
_TiaraCbqStatsEntry_Object = MibTableRow
tiaraCbqStatsEntry = _TiaraCbqStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1)
)
tiaraCbqStatsEntry.setIndexNames(
    (0, "TIARA-IP-MIB", "tiaraIpIfIndex"),
    (0, "TIARA-QOS-MIB", "cbqClassIndex"),
)
if mibBuilder.loadTexts:
    tiaraCbqStatsEntry.setStatus("current")
_CbqStatsClassName_Type = DisplayString
_CbqStatsClassName_Object = MibTableColumn
cbqStatsClassName = _CbqStatsClassName_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 1),
    _CbqStatsClassName_Type()
)
cbqStatsClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqStatsClassName.setStatus("current")
_CbqClassPacketsForwarded_Type = Counter32
_CbqClassPacketsForwarded_Object = MibTableColumn
cbqClassPacketsForwarded = _CbqClassPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 2),
    _CbqClassPacketsForwarded_Type()
)
cbqClassPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassPacketsForwarded.setStatus("current")
_CbqClassBytesForwarded_Type = Counter32
_CbqClassBytesForwarded_Object = MibTableColumn
cbqClassBytesForwarded = _CbqClassBytesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 3),
    _CbqClassBytesForwarded_Type()
)
cbqClassBytesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassBytesForwarded.setStatus("current")
_CbqClassPacketsDropped_Type = Counter32
_CbqClassPacketsDropped_Object = MibTableColumn
cbqClassPacketsDropped = _CbqClassPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 4),
    _CbqClassPacketsDropped_Type()
)
cbqClassPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassPacketsDropped.setStatus("current")
_CbqClassBytesDropped_Type = Counter32
_CbqClassBytesDropped_Object = MibTableColumn
cbqClassBytesDropped = _CbqClassBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 5),
    _CbqClassBytesDropped_Type()
)
cbqClassBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassBytesDropped.setStatus("current")
_CbqClassBurstExceedCount_Type = Counter32
_CbqClassBurstExceedCount_Object = MibTableColumn
cbqClassBurstExceedCount = _CbqClassBurstExceedCount_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 17, 5, 1, 6),
    _CbqClassBurstExceedCount_Type()
)
cbqClassBurstExceedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cbqClassBurstExceedCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-QOS-MIB",
    **{"tiaraQosMib": tiaraQosMib,
       "tiaraRedConfigTable": tiaraRedConfigTable,
       "tiaraRedConfigEntry": tiaraRedConfigEntry,
       "redTxMaxThreshold": redTxMaxThreshold,
       "redTxMinThreshold": redTxMinThreshold,
       "redTxWqBiasFactor": redTxWqBiasFactor,
       "redTxEnable": redTxEnable,
       "tiaraRedStatTable": tiaraRedStatTable,
       "tiaraRedStatEntry": tiaraRedStatEntry,
       "redTxLoanedCount": redTxLoanedCount,
       "redTxMaxLoanedCount": redTxMaxLoanedCount,
       "redTxAvgQueueSize": redTxAvgQueueSize,
       "redTxMaxAvgQueueSize": redTxMaxAvgQueueSize,
       "redTxDropRate": redTxDropRate,
       "redTxMinThresholdSuccess": redTxMinThresholdSuccess,
       "redTxMaxThresholdFailure": redTxMaxThresholdFailure,
       "redTxMinMaxRangeSuccess": redTxMinMaxRangeSuccess,
       "redTxMinMaxRangeFailure": redTxMinMaxRangeFailure,
       "redTxControlSuccess": redTxControlSuccess,
       "tiaraCbqConfigTable": tiaraCbqConfigTable,
       "tiaraCbqConfigEntry": tiaraCbqConfigEntry,
       "cbqClassIndex": cbqClassIndex,
       "cbqClassName": cbqClassName,
       "cbqClassParentName": cbqClassParentName,
       "cbqClassBandwidth": cbqClassBandwidth,
       "cbqClassBurstTolerance": cbqClassBurstTolerance,
       "cbqClassKeyType": cbqClassKeyType,
       "cbqClassIsDefault": cbqClassIsDefault,
       "cbqClassAverageBandwidth": cbqClassAverageBandwidth,
       "tiaraCbqClassKeyTable": tiaraCbqClassKeyTable,
       "tiaraCbqClassKeyTableEntry": tiaraCbqClassKeyTableEntry,
       "cbqClassKeyIndex": cbqClassKeyIndex,
       "cbqKeyClassName": cbqKeyClassName,
       "cbqClassKeyVlanId": cbqClassKeyVlanId,
       "cbqClassKeyIpAddress": cbqClassKeyIpAddress,
       "cbqClassKeyIpNetMask": cbqClassKeyIpNetMask,
       "cbqClassKeyPort": cbqClassKeyPort,
       "cbqClassKeyProtocolType": cbqClassKeyProtocolType,
       "tiaraCbqStatsTable": tiaraCbqStatsTable,
       "tiaraCbqStatsEntry": tiaraCbqStatsEntry,
       "cbqStatsClassName": cbqStatsClassName,
       "cbqClassPacketsForwarded": cbqClassPacketsForwarded,
       "cbqClassBytesForwarded": cbqClassBytesForwarded,
       "cbqClassPacketsDropped": cbqClassPacketsDropped,
       "cbqClassBytesDropped": cbqClassBytesDropped,
       "cbqClassBurstExceedCount": cbqClassBurstExceedCount}
)
