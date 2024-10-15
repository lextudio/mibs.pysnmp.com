# SNMP MIB module (TIMETRA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:02:01 2024
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

(AtmServiceCategory,
 AtmTrafficDescrParamIndex,
 AtmVcIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex",
    "AtmVcIdentifier")

(InetAddress,
 InetAddressIPv6,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxMcMlpppClassIndex,) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxMcMlpppClassIndex")

(Dot1PPriority,
 IpAddressPrefixLength,
 QTagFullRange,
 QTagFullRangeOrNone,
 ServiceAccessPoint,
 TAdaptationRule,
 TAdvCfgRate,
 TAtmTdpDescrType,
 TBWRateType,
 TBurstHundredthsOfPercent,
 TBurstLimit,
 TBurstPercent,
 TBurstPercentOrDefault,
 TBurstSize,
 TBurstSizeBytes,
 TCIRRate,
 TClassBurstLimit,
 TDEProfile,
 TDEProfileOrDei,
 TDEValue,
 TDSCPName,
 TDSCPNameOrEmpty,
 TDSCPValue,
 TEgrPolicerId,
 TEgrPolicerIdOrNone,
 TEgressHsmdaCounterIdOrZero,
 TEgressHsmdaPerPacketOffset,
 TEgressHsmdaQueueId,
 TEgressQPerPacketOffset,
 TEgressQueueId,
 TEntryId,
 TFCName,
 TFCNameOrEmpty,
 TFrameType,
 THPolCIRRate,
 THPolPIRRate,
 THPolVirtualScheCIRRate,
 THPolVirtualSchePIRRate,
 THSMDABurstSizeBytes,
 THSMDAQueueBurstLimit,
 THsmdaCIRKRate,
 THsmdaPIRKRate,
 THsmdaPIRMRate,
 THsmdaPolicyIncludeQueues,
 THsmdaPolicyScheduleClass,
 THsmdaSchedulerPolicyGroupId,
 THsmdaWeight,
 THsmdaWeightClass,
 THsmdaWrrWeight,
 TIngPolicerId,
 TIngPolicerIdOrNone,
 TIngressHsmdaCounterIdOrZero,
 TIngressHsmdaPerPacketOffset,
 TIngressHsmdaQueueId,
 TIngressQueueId,
 TIpProtocol,
 TItemDescription,
 TItemMatch,
 TItemScope,
 TLNamedItemOrEmpty,
 TLevel,
 TLevelOrDefault,
 TLspExpValue,
 TMacFilterType,
 TMatchCriteria,
 TMaxDecRate,
 TMcFrQoSProfileId,
 TMlpppQoSProfileId,
 TNamedItem,
 TNamedItemOrEmpty,
 TNetworkPolicyID,
 TNonZeroWeight,
 TPIRRate,
 TPIRRatePercent,
 TPerPacketOffset,
 TPlcrBurstSizeBytes,
 TPolicerRateType,
 TPolicerWeight,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TPortSchedulerPIRRate,
 TPrecValue,
 TPrecValueOrNone,
 TPriority,
 TPriorityOrDefault,
 TProfile,
 TProfileOrDei,
 TProfileOrNone,
 TProfileUseDEOrNone,
 TQueueId,
 TQueueMode,
 TRatePercent,
 TRateType,
 TRemarkType,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TWeight,
 TmnxEgrPolicerStatMode,
 TmnxEnabledDisabled,
 TmnxIngPolicerStatMode,
 TmnxSlopeMap) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "QTagFullRange",
    "QTagFullRangeOrNone",
    "ServiceAccessPoint",
    "TAdaptationRule",
    "TAdvCfgRate",
    "TAtmTdpDescrType",
    "TBWRateType",
    "TBurstHundredthsOfPercent",
    "TBurstLimit",
    "TBurstPercent",
    "TBurstPercentOrDefault",
    "TBurstSize",
    "TBurstSizeBytes",
    "TCIRRate",
    "TClassBurstLimit",
    "TDEProfile",
    "TDEProfileOrDei",
    "TDEValue",
    "TDSCPName",
    "TDSCPNameOrEmpty",
    "TDSCPValue",
    "TEgrPolicerId",
    "TEgrPolicerIdOrNone",
    "TEgressHsmdaCounterIdOrZero",
    "TEgressHsmdaPerPacketOffset",
    "TEgressHsmdaQueueId",
    "TEgressQPerPacketOffset",
    "TEgressQueueId",
    "TEntryId",
    "TFCName",
    "TFCNameOrEmpty",
    "TFrameType",
    "THPolCIRRate",
    "THPolPIRRate",
    "THPolVirtualScheCIRRate",
    "THPolVirtualSchePIRRate",
    "THSMDABurstSizeBytes",
    "THSMDAQueueBurstLimit",
    "THsmdaCIRKRate",
    "THsmdaPIRKRate",
    "THsmdaPIRMRate",
    "THsmdaPolicyIncludeQueues",
    "THsmdaPolicyScheduleClass",
    "THsmdaSchedulerPolicyGroupId",
    "THsmdaWeight",
    "THsmdaWeightClass",
    "THsmdaWrrWeight",
    "TIngPolicerId",
    "TIngPolicerIdOrNone",
    "TIngressHsmdaCounterIdOrZero",
    "TIngressHsmdaPerPacketOffset",
    "TIngressHsmdaQueueId",
    "TIngressQueueId",
    "TIpProtocol",
    "TItemDescription",
    "TItemMatch",
    "TItemScope",
    "TLNamedItemOrEmpty",
    "TLevel",
    "TLevelOrDefault",
    "TLspExpValue",
    "TMacFilterType",
    "TMatchCriteria",
    "TMaxDecRate",
    "TMcFrQoSProfileId",
    "TMlpppQoSProfileId",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TNetworkPolicyID",
    "TNonZeroWeight",
    "TPIRRate",
    "TPIRRatePercent",
    "TPerPacketOffset",
    "TPlcrBurstSizeBytes",
    "TPolicerRateType",
    "TPolicerWeight",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TPortSchedulerPIRRate",
    "TPrecValue",
    "TPrecValueOrNone",
    "TPriority",
    "TPriorityOrDefault",
    "TProfile",
    "TProfileOrDei",
    "TProfileOrNone",
    "TProfileUseDEOrNone",
    "TQueueId",
    "TQueueMode",
    "TRatePercent",
    "TRateType",
    "TRemarkType",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TWeight",
    "TmnxEgrPolicerStatMode",
    "TmnxEnabledDisabled",
    "TmnxIngPolicerStatMode",
    "TmnxSlopeMap")


# MODULE-IDENTITY

timetraQosMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 16)
)
timetraQosMIBModule.setRevisions(
        ("1909-02-28 00:00",
         "1908-07-01 00:00",
         "1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "2003-01-20 00:00",
         "2001-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxMcFrClassIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



# MIB Managed Objects in the order of their OIDs

_TmnxQosConformance_ObjectIdentity = ObjectIdentity
tmnxQosConformance = _TmnxQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16)
)
_TmnxQosCompliances_ObjectIdentity = ObjectIdentity
tmnxQosCompliances = _TmnxQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1)
)
_TmnxQosGroups_ObjectIdentity = ObjectIdentity
tmnxQosGroups = _TmnxQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2)
)
_TQosObjects_ObjectIdentity = ObjectIdentity
tQosObjects = _TQosObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16)
)
_TDSCPObjects_ObjectIdentity = ObjectIdentity
tDSCPObjects = _TDSCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1)
)
_TDSCPNameTable_Object = MibTable
tDSCPNameTable = _TDSCPNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    tDSCPNameTable.setStatus("current")
_TDSCPNameEntry_Object = MibTableRow
tDSCPNameEntry = _TDSCPNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1)
)
tDSCPNameEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tDSCPName"),
)
if mibBuilder.loadTexts:
    tDSCPNameEntry.setStatus("current")
_TDSCPName_Type = TDSCPName
_TDSCPName_Object = MibTableColumn
tDSCPName = _TDSCPName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1, 1),
    _TDSCPName_Type()
)
tDSCPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tDSCPName.setStatus("current")
_TDSCPNameRowStatus_Type = RowStatus
_TDSCPNameRowStatus_Object = MibTableColumn
tDSCPNameRowStatus = _TDSCPNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1, 2),
    _TDSCPNameRowStatus_Type()
)
tDSCPNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDSCPNameRowStatus.setStatus("current")


class _TDSCPNameStorageType_Type(StorageType):
    """Custom type tDSCPNameStorageType based on StorageType"""


_TDSCPNameStorageType_Object = MibTableColumn
tDSCPNameStorageType = _TDSCPNameStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1, 3),
    _TDSCPNameStorageType_Type()
)
tDSCPNameStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDSCPNameStorageType.setStatus("current")


class _TDSCPNameDscpValue_Type(TDSCPValue):
    """Custom type tDSCPNameDscpValue based on TDSCPValue"""
    defaultValue = 0


_TDSCPNameDscpValue_Object = MibTableColumn
tDSCPNameDscpValue = _TDSCPNameDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1, 4),
    _TDSCPNameDscpValue_Type()
)
tDSCPNameDscpValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tDSCPNameDscpValue.setStatus("current")
_TDSCPNameLastChanged_Type = TimeStamp
_TDSCPNameLastChanged_Object = MibTableColumn
tDSCPNameLastChanged = _TDSCPNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 1, 1, 1, 5),
    _TDSCPNameLastChanged_Type()
)
tDSCPNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDSCPNameLastChanged.setStatus("current")
_TFCObjects_ObjectIdentity = ObjectIdentity
tFCObjects = _TFCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2)
)
_TFCNameTable_Object = MibTable
tFCNameTable = _TFCNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1)
)
if mibBuilder.loadTexts:
    tFCNameTable.setStatus("current")
_TFCNameEntry_Object = MibTableRow
tFCNameEntry = _TFCNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1)
)
tFCNameEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tFCName"),
)
if mibBuilder.loadTexts:
    tFCNameEntry.setStatus("current")
_TFCName_Type = TFCName
_TFCName_Object = MibTableColumn
tFCName = _TFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1, 1),
    _TFCName_Type()
)
tFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tFCName.setStatus("current")
_TFCRowStatus_Type = RowStatus
_TFCRowStatus_Object = MibTableColumn
tFCRowStatus = _TFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1, 2),
    _TFCRowStatus_Type()
)
tFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFCRowStatus.setStatus("current")


class _TFCStorageType_Type(StorageType):
    """Custom type tFCStorageType based on StorageType"""


_TFCStorageType_Object = MibTableColumn
tFCStorageType = _TFCStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1, 3),
    _TFCStorageType_Type()
)
tFCStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFCStorageType.setStatus("current")


class _TFCValue_Type(Integer32):
    """Custom type tFCValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TFCValue_Type.__name__ = "Integer32"
_TFCValue_Object = MibTableColumn
tFCValue = _TFCValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1, 4),
    _TFCValue_Type()
)
tFCValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tFCValue.setStatus("current")
_TFCNameLastChanged_Type = TimeStamp
_TFCNameLastChanged_Object = MibTableColumn
tFCNameLastChanged = _TFCNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 2, 1, 1, 5),
    _TFCNameLastChanged_Type()
)
tFCNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFCNameLastChanged.setStatus("current")
_TSapIngressObjects_ObjectIdentity = ObjectIdentity
tSapIngressObjects = _TSapIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3)
)
_TSapIngressTable_Object = MibTable
tSapIngressTable = _TSapIngressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    tSapIngressTable.setStatus("current")
_TSapIngressEntry_Object = MibTableRow
tSapIngressEntry = _TSapIngressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1)
)
tSapIngressEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
)
if mibBuilder.loadTexts:
    tSapIngressEntry.setStatus("current")


class _TSapIngressIndex_Type(TSapIngressPolicyID):
    """Custom type tSapIngressIndex based on TSapIngressPolicyID"""
    subtypeSpec = TSapIngressPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
    )


_TSapIngressIndex_Type.__name__ = "TSapIngressPolicyID"
_TSapIngressIndex_Object = MibTableColumn
tSapIngressIndex = _TSapIngressIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 1),
    _TSapIngressIndex_Type()
)
tSapIngressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressIndex.setStatus("current")
_TSapIngressRowStatus_Type = RowStatus
_TSapIngressRowStatus_Object = MibTableColumn
tSapIngressRowStatus = _TSapIngressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 2),
    _TSapIngressRowStatus_Type()
)
tSapIngressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressRowStatus.setStatus("current")


class _TSapIngressScope_Type(TItemScope):
    """Custom type tSapIngressScope based on TItemScope"""


_TSapIngressScope_Object = MibTableColumn
tSapIngressScope = _TSapIngressScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 3),
    _TSapIngressScope_Type()
)
tSapIngressScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressScope.setStatus("current")


class _TSapIngressDescription_Type(TItemDescription):
    """Custom type tSapIngressDescription based on TItemDescription"""
    defaultHexValue = ""


_TSapIngressDescription_Object = MibTableColumn
tSapIngressDescription = _TSapIngressDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 4),
    _TSapIngressDescription_Type()
)
tSapIngressDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDescription.setStatus("current")


class _TSapIngressDefaultFC_Type(TNamedItem):
    """Custom type tSapIngressDefaultFC based on TNamedItem"""
    defaultHexValue = "be"


_TSapIngressDefaultFC_Object = MibTableColumn
tSapIngressDefaultFC = _TSapIngressDefaultFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 5),
    _TSapIngressDefaultFC_Type()
)
tSapIngressDefaultFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDefaultFC.setStatus("current")


class _TSapIngressDefaultFCPriority_Type(TPriority):
    """Custom type tSapIngressDefaultFCPriority based on TPriority"""


_TSapIngressDefaultFCPriority_Object = MibTableColumn
tSapIngressDefaultFCPriority = _TSapIngressDefaultFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 6),
    _TSapIngressDefaultFCPriority_Type()
)
tSapIngressDefaultFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDefaultFCPriority.setStatus("current")
_TSapIngressMatchCriteria_Type = TMatchCriteria
_TSapIngressMatchCriteria_Object = MibTableColumn
tSapIngressMatchCriteria = _TSapIngressMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 7),
    _TSapIngressMatchCriteria_Type()
)
tSapIngressMatchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMatchCriteria.setStatus("current")
_TSapIngressLastChanged_Type = TimeStamp
_TSapIngressLastChanged_Object = MibTableColumn
tSapIngressLastChanged = _TSapIngressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 8),
    _TSapIngressLastChanged_Type()
)
tSapIngressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressLastChanged.setStatus("current")


class _TSapIngressHsmdaPacketOffset_Type(TIngressHsmdaPerPacketOffset):
    """Custom type tSapIngressHsmdaPacketOffset based on TIngressHsmdaPerPacketOffset"""
    defaultValue = 0


_TSapIngressHsmdaPacketOffset_Object = MibTableColumn
tSapIngressHsmdaPacketOffset = _TSapIngressHsmdaPacketOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 9),
    _TSapIngressHsmdaPacketOffset_Type()
)
tSapIngressHsmdaPacketOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaPacketOffset.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapIngressHsmdaPacketOffset.setUnits("bytes")


class _TSapIngressDefFCHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressDefFCHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressDefFCHsmdaCntrOvr_Object = MibTableColumn
tSapIngressDefFCHsmdaCntrOvr = _TSapIngressDefFCHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 10),
    _TSapIngressDefFCHsmdaCntrOvr_Type()
)
tSapIngressDefFCHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDefFCHsmdaCntrOvr.setStatus("obsolete")


class _TSapIngressMacCritType_Type(TMacFilterType):
    """Custom type tSapIngressMacCritType based on TMacFilterType"""


_TSapIngressMacCritType_Object = MibTableColumn
tSapIngressMacCritType = _TSapIngressMacCritType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 11),
    _TSapIngressMacCritType_Type()
)
tSapIngressMacCritType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCritType.setStatus("current")


class _TSapIngressPolicyName_Type(TLNamedItemOrEmpty):
    """Custom type tSapIngressPolicyName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressPolicyName_Object = MibTableColumn
tSapIngressPolicyName = _TSapIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 1, 1, 12),
    _TSapIngressPolicyName_Type()
)
tSapIngressPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressPolicyName.setStatus("current")
_TSapIngressQueueTable_Object = MibTable
tSapIngressQueueTable = _TSapIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2)
)
if mibBuilder.loadTexts:
    tSapIngressQueueTable.setStatus("current")
_TSapIngressQueueEntry_Object = MibTableRow
tSapIngressQueueEntry = _TSapIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1)
)
tSapIngressQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressQueue"),
)
if mibBuilder.loadTexts:
    tSapIngressQueueEntry.setStatus("current")


class _TSapIngressQueue_Type(TIngressQueueId):
    """Custom type tSapIngressQueue based on TIngressQueueId"""
    subtypeSpec = TIngressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TSapIngressQueue_Type.__name__ = "TIngressQueueId"
_TSapIngressQueue_Object = MibTableColumn
tSapIngressQueue = _TSapIngressQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 1),
    _TSapIngressQueue_Type()
)
tSapIngressQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressQueue.setStatus("current")
_TSapIngressQueueRowStatus_Type = RowStatus
_TSapIngressQueueRowStatus_Object = MibTableColumn
tSapIngressQueueRowStatus = _TSapIngressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 2),
    _TSapIngressQueueRowStatus_Type()
)
tSapIngressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueRowStatus.setStatus("current")


class _TSapIngressQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressQueueParent_Object = MibTableColumn
tSapIngressQueueParent = _TSapIngressQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 3),
    _TSapIngressQueueParent_Type()
)
tSapIngressQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueParent.setStatus("current")


class _TSapIngressQueueLevel_Type(TLevel):
    """Custom type tSapIngressQueueLevel based on TLevel"""
    defaultValue = 1


_TSapIngressQueueLevel_Object = MibTableColumn
tSapIngressQueueLevel = _TSapIngressQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 4),
    _TSapIngressQueueLevel_Type()
)
tSapIngressQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueLevel.setStatus("current")


class _TSapIngressQueueWeight_Type(TWeight):
    """Custom type tSapIngressQueueWeight based on TWeight"""
    defaultValue = 1


_TSapIngressQueueWeight_Object = MibTableColumn
tSapIngressQueueWeight = _TSapIngressQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 5),
    _TSapIngressQueueWeight_Type()
)
tSapIngressQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueWeight.setStatus("current")


class _TSapIngressQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tSapIngressQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TSapIngressQueueCIRLevel_Object = MibTableColumn
tSapIngressQueueCIRLevel = _TSapIngressQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 6),
    _TSapIngressQueueCIRLevel_Type()
)
tSapIngressQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueCIRLevel.setStatus("current")


class _TSapIngressQueueCIRWeight_Type(TWeight):
    """Custom type tSapIngressQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TSapIngressQueueCIRWeight_Object = MibTableColumn
tSapIngressQueueCIRWeight = _TSapIngressQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 7),
    _TSapIngressQueueCIRWeight_Type()
)
tSapIngressQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueCIRWeight.setStatus("current")


class _TSapIngressQueueMCast_Type(TruthValue):
    """Custom type tSapIngressQueueMCast based on TruthValue"""


_TSapIngressQueueMCast_Object = MibTableColumn
tSapIngressQueueMCast = _TSapIngressQueueMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 8),
    _TSapIngressQueueMCast_Type()
)
tSapIngressQueueMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueMCast.setStatus("current")


class _TSapIngressQueueExpedite_Type(Integer32):
    """Custom type tSapIngressQueueExpedite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-expedited", 2),
          ("expedited", 1),
          ("non-expedited", 3))
    )


_TSapIngressQueueExpedite_Type.__name__ = "Integer32"
_TSapIngressQueueExpedite_Object = MibTableColumn
tSapIngressQueueExpedite = _TSapIngressQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 9),
    _TSapIngressQueueExpedite_Type()
)
tSapIngressQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueExpedite.setStatus("current")


class _TSapIngressQueueCBS_Type(TBurstSize):
    """Custom type tSapIngressQueueCBS based on TBurstSize"""
    defaultValue = -1


_TSapIngressQueueCBS_Object = MibTableColumn
tSapIngressQueueCBS = _TSapIngressQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 10),
    _TSapIngressQueueCBS_Type()
)
tSapIngressQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueCBS.setStatus("current")


class _TSapIngressQueueMBS_Type(TBurstSize):
    """Custom type tSapIngressQueueMBS based on TBurstSize"""
    defaultValue = -1


_TSapIngressQueueMBS_Object = MibTableColumn
tSapIngressQueueMBS = _TSapIngressQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 11),
    _TSapIngressQueueMBS_Type()
)
tSapIngressQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueMBS.setStatus("obsolete")


class _TSapIngressQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tSapIngressQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TSapIngressQueueHiPrioOnly_Object = MibTableColumn
tSapIngressQueueHiPrioOnly = _TSapIngressQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 12),
    _TSapIngressQueueHiPrioOnly_Type()
)
tSapIngressQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueHiPrioOnly.setStatus("current")


class _TSapIngressQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngressQueuePIRAdaptation based on TAdaptationRule"""


_TSapIngressQueuePIRAdaptation_Object = MibTableColumn
tSapIngressQueuePIRAdaptation = _TSapIngressQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 13),
    _TSapIngressQueuePIRAdaptation_Type()
)
tSapIngressQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueuePIRAdaptation.setStatus("current")


class _TSapIngressQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngressQueueCIRAdaptation based on TAdaptationRule"""


_TSapIngressQueueCIRAdaptation_Object = MibTableColumn
tSapIngressQueueCIRAdaptation = _TSapIngressQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 14),
    _TSapIngressQueueCIRAdaptation_Type()
)
tSapIngressQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueCIRAdaptation.setStatus("current")


class _TSapIngressQueueAdminPIR_Type(TPIRRate):
    """Custom type tSapIngressQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TSapIngressQueueAdminPIR_Object = MibTableColumn
tSapIngressQueueAdminPIR = _TSapIngressQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 15),
    _TSapIngressQueueAdminPIR_Type()
)
tSapIngressQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminPIR.setUnits("kbps")


class _TSapIngressQueueAdminCIR_Type(TCIRRate):
    """Custom type tSapIngressQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TSapIngressQueueAdminCIR_Object = MibTableColumn
tSapIngressQueueAdminCIR = _TSapIngressQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 16),
    _TSapIngressQueueAdminCIR_Type()
)
tSapIngressQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminCIR.setUnits("kbps")
_TSapIngressQueueOperPIR_Type = TPIRRate
_TSapIngressQueueOperPIR_Object = MibTableColumn
tSapIngressQueueOperPIR = _TSapIngressQueueOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 17),
    _TSapIngressQueueOperPIR_Type()
)
tSapIngressQueueOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQueueOperPIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapIngressQueueOperPIR.setUnits("kbps")
_TSapIngressQueueOperCIR_Type = TCIRRate
_TSapIngressQueueOperCIR_Object = MibTableColumn
tSapIngressQueueOperCIR = _TSapIngressQueueOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 18),
    _TSapIngressQueueOperCIR_Type()
)
tSapIngressQueueOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQueueOperCIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapIngressQueueOperCIR.setUnits("kbps")
_TSapIngressQueueLastChanged_Type = TimeStamp
_TSapIngressQueueLastChanged_Object = MibTableColumn
tSapIngressQueueLastChanged = _TSapIngressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 19),
    _TSapIngressQueueLastChanged_Type()
)
tSapIngressQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQueueLastChanged.setStatus("current")


class _TSapIngressQueuePoliced_Type(TruthValue):
    """Custom type tSapIngressQueuePoliced based on TruthValue"""


_TSapIngressQueuePoliced_Object = MibTableColumn
tSapIngressQueuePoliced = _TSapIngressQueuePoliced_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 20),
    _TSapIngressQueuePoliced_Type()
)
tSapIngressQueuePoliced.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueuePoliced.setStatus("current")


class _TSapIngressQueueMode_Type(TQueueMode):
    """Custom type tSapIngressQueueMode based on TQueueMode"""


_TSapIngressQueueMode_Object = MibTableColumn
tSapIngressQueueMode = _TSapIngressQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 21),
    _TSapIngressQueueMode_Type()
)
tSapIngressQueueMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueMode.setStatus("current")


class _TSapIngressQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressQueuePoolName_Object = MibTableColumn
tSapIngressQueuePoolName = _TSapIngressQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 22),
    _TSapIngressQueuePoolName_Type()
)
tSapIngressQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueuePoolName.setStatus("current")


class _TSapIngressQueueMBSBytes_Type(TBurstSizeBytes):
    """Custom type tSapIngressQueueMBSBytes based on TBurstSizeBytes"""
    defaultValue = -1


_TSapIngressQueueMBSBytes_Object = MibTableColumn
tSapIngressQueueMBSBytes = _TSapIngressQueueMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 23),
    _TSapIngressQueueMBSBytes_Type()
)
tSapIngressQueueMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueMBSBytes.setUnits("bytes")


class _TSapIngressQueueBurstLimit_Type(TBurstLimit):
    """Custom type tSapIngressQueueBurstLimit based on TBurstLimit"""
    defaultValue = -1


_TSapIngressQueueBurstLimit_Object = MibTableColumn
tSapIngressQueueBurstLimit = _TSapIngressQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 24),
    _TSapIngressQueueBurstLimit_Type()
)
tSapIngressQueueBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueBurstLimit.setUnits("bytes")


class _TSapIngressQueueAdminPIRPercent_Type(Unsigned32):
    """Custom type tSapIngressQueueAdminPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapIngressQueueAdminPIRPercent_Type.__name__ = "Unsigned32"
_TSapIngressQueueAdminPIRPercent_Object = MibTableColumn
tSapIngressQueueAdminPIRPercent = _TSapIngressQueueAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 25),
    _TSapIngressQueueAdminPIRPercent_Type()
)
tSapIngressQueueAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminPIRPercent.setUnits("hundredths of a percent")


class _TSapIngressQueueAdminCIRPercent_Type(Unsigned32):
    """Custom type tSapIngressQueueAdminCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TSapIngressQueueAdminCIRPercent_Type.__name__ = "Unsigned32"
_TSapIngressQueueAdminCIRPercent_Object = MibTableColumn
tSapIngressQueueAdminCIRPercent = _TSapIngressQueueAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 26),
    _TSapIngressQueueAdminCIRPercent_Type()
)
tSapIngressQueueAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngressQueueAdminCIRPercent.setUnits("hundredths of a percent")


class _TSapIngressQueueRateType_Type(TBWRateType):
    """Custom type tSapIngressQueueRateType based on TBWRateType"""


_TSapIngressQueueRateType_Object = MibTableColumn
tSapIngressQueueRateType = _TSapIngressQueueRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 27),
    _TSapIngressQueueRateType_Type()
)
tSapIngressQueueRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueRateType.setStatus("current")


class _TSapIngressQueueAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressQueueAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressQueueAdvCfgPolicy_Object = MibTableColumn
tSapIngressQueueAdvCfgPolicy = _TSapIngressQueueAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 2, 1, 28),
    _TSapIngressQueueAdvCfgPolicy_Type()
)
tSapIngressQueueAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressQueueAdvCfgPolicy.setStatus("current")
_TSapIngressDSCPTable_Object = MibTable
tSapIngressDSCPTable = _TSapIngressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3)
)
if mibBuilder.loadTexts:
    tSapIngressDSCPTable.setStatus("current")
_TSapIngressDSCPEntry_Object = MibTableRow
tSapIngressDSCPEntry = _TSapIngressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1)
)
tSapIngressDSCPEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressDSCP"),
)
if mibBuilder.loadTexts:
    tSapIngressDSCPEntry.setStatus("current")
_TSapIngressDSCP_Type = TDSCPName
_TSapIngressDSCP_Object = MibTableColumn
tSapIngressDSCP = _TSapIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 1),
    _TSapIngressDSCP_Type()
)
tSapIngressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressDSCP.setStatus("current")
_TSapIngressDSCPRowStatus_Type = RowStatus
_TSapIngressDSCPRowStatus_Object = MibTableColumn
tSapIngressDSCPRowStatus = _TSapIngressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 2),
    _TSapIngressDSCPRowStatus_Type()
)
tSapIngressDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDSCPRowStatus.setStatus("current")


class _TSapIngressDSCPFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressDSCPFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressDSCPFC_Object = MibTableColumn
tSapIngressDSCPFC = _TSapIngressDSCPFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 3),
    _TSapIngressDSCPFC_Type()
)
tSapIngressDSCPFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDSCPFC.setStatus("current")


class _TSapIngressDSCPPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressDSCPPriority based on TPriorityOrDefault"""


_TSapIngressDSCPPriority_Object = MibTableColumn
tSapIngressDSCPPriority = _TSapIngressDSCPPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 4),
    _TSapIngressDSCPPriority_Type()
)
tSapIngressDSCPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDSCPPriority.setStatus("current")
_TSapIngressDSCPLastChanged_Type = TimeStamp
_TSapIngressDSCPLastChanged_Object = MibTableColumn
tSapIngressDSCPLastChanged = _TSapIngressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 5),
    _TSapIngressDSCPLastChanged_Type()
)
tSapIngressDSCPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressDSCPLastChanged.setStatus("current")


class _TSapIngressDSCPHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressDSCPHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressDSCPHsmdaCntrOvr_Object = MibTableColumn
tSapIngressDSCPHsmdaCntrOvr = _TSapIngressDSCPHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 3, 1, 6),
    _TSapIngressDSCPHsmdaCntrOvr_Type()
)
tSapIngressDSCPHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDSCPHsmdaCntrOvr.setStatus("obsolete")
_TSapIngressDot1pTable_Object = MibTable
tSapIngressDot1pTable = _TSapIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4)
)
if mibBuilder.loadTexts:
    tSapIngressDot1pTable.setStatus("current")
_TSapIngressDot1pEntry_Object = MibTableRow
tSapIngressDot1pEntry = _TSapIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1)
)
tSapIngressDot1pEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressDot1pValue"),
)
if mibBuilder.loadTexts:
    tSapIngressDot1pEntry.setStatus("current")


class _TSapIngressDot1pValue_Type(Dot1PPriority):
    """Custom type tSapIngressDot1pValue based on Dot1PPriority"""
    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapIngressDot1pValue_Type.__name__ = "Dot1PPriority"
_TSapIngressDot1pValue_Object = MibTableColumn
tSapIngressDot1pValue = _TSapIngressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 1),
    _TSapIngressDot1pValue_Type()
)
tSapIngressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressDot1pValue.setStatus("current")
_TSapIngressDot1pRowStatus_Type = RowStatus
_TSapIngressDot1pRowStatus_Object = MibTableColumn
tSapIngressDot1pRowStatus = _TSapIngressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 2),
    _TSapIngressDot1pRowStatus_Type()
)
tSapIngressDot1pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDot1pRowStatus.setStatus("current")


class _TSapIngressDot1pFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressDot1pFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressDot1pFC_Object = MibTableColumn
tSapIngressDot1pFC = _TSapIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 3),
    _TSapIngressDot1pFC_Type()
)
tSapIngressDot1pFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDot1pFC.setStatus("current")


class _TSapIngressDot1pPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressDot1pPriority based on TPriorityOrDefault"""


_TSapIngressDot1pPriority_Object = MibTableColumn
tSapIngressDot1pPriority = _TSapIngressDot1pPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 4),
    _TSapIngressDot1pPriority_Type()
)
tSapIngressDot1pPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDot1pPriority.setStatus("current")
_TSapIngressDot1pLastChanged_Type = TimeStamp
_TSapIngressDot1pLastChanged_Object = MibTableColumn
tSapIngressDot1pLastChanged = _TSapIngressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 5),
    _TSapIngressDot1pLastChanged_Type()
)
tSapIngressDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressDot1pLastChanged.setStatus("current")


class _TSapIngressDot1pHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressDot1pHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressDot1pHsmdaCntrOvr_Object = MibTableColumn
tSapIngressDot1pHsmdaCntrOvr = _TSapIngressDot1pHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 4, 1, 6),
    _TSapIngressDot1pHsmdaCntrOvr_Type()
)
tSapIngressDot1pHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressDot1pHsmdaCntrOvr.setStatus("obsolete")
_TSapIngressIPCriteriaTable_Object = MibTable
tSapIngressIPCriteriaTable = _TSapIngressIPCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5)
)
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaTable.setStatus("current")
_TSapIngressIPCriteriaEntry_Object = MibTableRow
tSapIngressIPCriteriaEntry = _TSapIngressIPCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1)
)
tSapIngressIPCriteriaEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressIPCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaEntry.setStatus("current")
_TSapIngressIPCriteriaIndex_Type = TEntryId
_TSapIngressIPCriteriaIndex_Object = MibTableColumn
tSapIngressIPCriteriaIndex = _TSapIngressIPCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 1),
    _TSapIngressIPCriteriaIndex_Type()
)
tSapIngressIPCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaIndex.setStatus("current")
_TSapIngressIPCriteriaRowStatus_Type = RowStatus
_TSapIngressIPCriteriaRowStatus_Object = MibTableColumn
tSapIngressIPCriteriaRowStatus = _TSapIngressIPCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 2),
    _TSapIngressIPCriteriaRowStatus_Type()
)
tSapIngressIPCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaRowStatus.setStatus("current")


class _TSapIngressIPCriteriaDescription_Type(TItemDescription):
    """Custom type tSapIngressIPCriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TSapIngressIPCriteriaDescription_Object = MibTableColumn
tSapIngressIPCriteriaDescription = _TSapIngressIPCriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 3),
    _TSapIngressIPCriteriaDescription_Type()
)
tSapIngressIPCriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDescription.setStatus("current")


class _TSapIngressIPCriteriaActionFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressIPCriteriaActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressIPCriteriaActionFC_Object = MibTableColumn
tSapIngressIPCriteriaActionFC = _TSapIngressIPCriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 4),
    _TSapIngressIPCriteriaActionFC_Type()
)
tSapIngressIPCriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaActionFC.setStatus("current")


class _TSapIngressIPCriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressIPCriteriaActionPriority based on TPriorityOrDefault"""


_TSapIngressIPCriteriaActionPriority_Object = MibTableColumn
tSapIngressIPCriteriaActionPriority = _TSapIngressIPCriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 5),
    _TSapIngressIPCriteriaActionPriority_Type()
)
tSapIngressIPCriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaActionPriority.setStatus("current")


class _TSapIngressIPCriteriaSourceIpAddr_Type(IpAddress):
    """Custom type tSapIngressIPCriteriaSourceIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TSapIngressIPCriteriaSourceIpAddr_Object = MibTableColumn
tSapIngressIPCriteriaSourceIpAddr = _TSapIngressIPCriteriaSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 6),
    _TSapIngressIPCriteriaSourceIpAddr_Type()
)
tSapIngressIPCriteriaSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaSourceIpAddr.setStatus("current")


class _TSapIngressIPCriteriaSourceIpMask_Type(IpAddressPrefixLength):
    """Custom type tSapIngressIPCriteriaSourceIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TSapIngressIPCriteriaSourceIpMask_Object = MibTableColumn
tSapIngressIPCriteriaSourceIpMask = _TSapIngressIPCriteriaSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 7),
    _TSapIngressIPCriteriaSourceIpMask_Type()
)
tSapIngressIPCriteriaSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaSourceIpMask.setStatus("current")


class _TSapIngressIPCriteriaDestIpAddr_Type(IpAddress):
    """Custom type tSapIngressIPCriteriaDestIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_TSapIngressIPCriteriaDestIpAddr_Object = MibTableColumn
tSapIngressIPCriteriaDestIpAddr = _TSapIngressIPCriteriaDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 8),
    _TSapIngressIPCriteriaDestIpAddr_Type()
)
tSapIngressIPCriteriaDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDestIpAddr.setStatus("current")


class _TSapIngressIPCriteriaDestIpMask_Type(IpAddressPrefixLength):
    """Custom type tSapIngressIPCriteriaDestIpMask based on IpAddressPrefixLength"""
    defaultValue = 0


_TSapIngressIPCriteriaDestIpMask_Object = MibTableColumn
tSapIngressIPCriteriaDestIpMask = _TSapIngressIPCriteriaDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 9),
    _TSapIngressIPCriteriaDestIpMask_Type()
)
tSapIngressIPCriteriaDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDestIpMask.setStatus("current")


class _TSapIngressIPCriteriaProtocol_Type(TIpProtocol):
    """Custom type tSapIngressIPCriteriaProtocol based on TIpProtocol"""
    defaultValue = -1


_TSapIngressIPCriteriaProtocol_Object = MibTableColumn
tSapIngressIPCriteriaProtocol = _TSapIngressIPCriteriaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 10),
    _TSapIngressIPCriteriaProtocol_Type()
)
tSapIngressIPCriteriaProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaProtocol.setStatus("current")


class _TSapIngressIPCriteriaSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tSapIngressIPCriteriaSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPCriteriaSourcePortValue1_Object = MibTableColumn
tSapIngressIPCriteriaSourcePortValue1 = _TSapIngressIPCriteriaSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 11),
    _TSapIngressIPCriteriaSourcePortValue1_Type()
)
tSapIngressIPCriteriaSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaSourcePortValue1.setStatus("current")


class _TSapIngressIPCriteriaSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tSapIngressIPCriteriaSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPCriteriaSourcePortValue2_Object = MibTableColumn
tSapIngressIPCriteriaSourcePortValue2 = _TSapIngressIPCriteriaSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 12),
    _TSapIngressIPCriteriaSourcePortValue2_Type()
)
tSapIngressIPCriteriaSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaSourcePortValue2.setStatus("current")


class _TSapIngressIPCriteriaSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapIngressIPCriteriaSourcePortOperator based on TTcpUdpPortOperator"""


_TSapIngressIPCriteriaSourcePortOperator_Object = MibTableColumn
tSapIngressIPCriteriaSourcePortOperator = _TSapIngressIPCriteriaSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 13),
    _TSapIngressIPCriteriaSourcePortOperator_Type()
)
tSapIngressIPCriteriaSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaSourcePortOperator.setStatus("current")


class _TSapIngressIPCriteriaDestPortValue1_Type(TTcpUdpPort):
    """Custom type tSapIngressIPCriteriaDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPCriteriaDestPortValue1_Object = MibTableColumn
tSapIngressIPCriteriaDestPortValue1 = _TSapIngressIPCriteriaDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 14),
    _TSapIngressIPCriteriaDestPortValue1_Type()
)
tSapIngressIPCriteriaDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDestPortValue1.setStatus("current")


class _TSapIngressIPCriteriaDestPortValue2_Type(TTcpUdpPort):
    """Custom type tSapIngressIPCriteriaDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPCriteriaDestPortValue2_Object = MibTableColumn
tSapIngressIPCriteriaDestPortValue2 = _TSapIngressIPCriteriaDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 15),
    _TSapIngressIPCriteriaDestPortValue2_Type()
)
tSapIngressIPCriteriaDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDestPortValue2.setStatus("current")


class _TSapIngressIPCriteriaDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapIngressIPCriteriaDestPortOperator based on TTcpUdpPortOperator"""


_TSapIngressIPCriteriaDestPortOperator_Object = MibTableColumn
tSapIngressIPCriteriaDestPortOperator = _TSapIngressIPCriteriaDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 16),
    _TSapIngressIPCriteriaDestPortOperator_Type()
)
tSapIngressIPCriteriaDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDestPortOperator.setStatus("current")


class _TSapIngressIPCriteriaDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tSapIngressIPCriteriaDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TSapIngressIPCriteriaDSCP_Object = MibTableColumn
tSapIngressIPCriteriaDSCP = _TSapIngressIPCriteriaDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 17),
    _TSapIngressIPCriteriaDSCP_Type()
)
tSapIngressIPCriteriaDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaDSCP.setStatus("current")


class _TSapIngressIPCriteriaFragment_Type(TItemMatch):
    """Custom type tSapIngressIPCriteriaFragment based on TItemMatch"""


_TSapIngressIPCriteriaFragment_Object = MibTableColumn
tSapIngressIPCriteriaFragment = _TSapIngressIPCriteriaFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 19),
    _TSapIngressIPCriteriaFragment_Type()
)
tSapIngressIPCriteriaFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaFragment.setStatus("current")
_TSapIngressIPCriteriaLastChanged_Type = TimeStamp
_TSapIngressIPCriteriaLastChanged_Object = MibTableColumn
tSapIngressIPCriteriaLastChanged = _TSapIngressIPCriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 20),
    _TSapIngressIPCriteriaLastChanged_Type()
)
tSapIngressIPCriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaLastChanged.setStatus("current")


class _TSapIngressIPCritHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressIPCritHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressIPCritHsmdaCntrOvr_Object = MibTableColumn
tSapIngressIPCritHsmdaCntrOvr = _TSapIngressIPCritHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 21),
    _TSapIngressIPCritHsmdaCntrOvr_Type()
)
tSapIngressIPCritHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCritHsmdaCntrOvr.setStatus("obsolete")


class _TSapIngressIPCriteriaIpPrecValue_Type(Dot1PPriority):
    """Custom type tSapIngressIPCriteriaIpPrecValue based on Dot1PPriority"""
    defaultValue = -1


_TSapIngressIPCriteriaIpPrecValue_Object = MibTableColumn
tSapIngressIPCriteriaIpPrecValue = _TSapIngressIPCriteriaIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 31),
    _TSapIngressIPCriteriaIpPrecValue_Type()
)
tSapIngressIPCriteriaIpPrecValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaIpPrecValue.setStatus("current")


class _TSapIngressIPCriteriaIpPrecMask_Type(Dot1PPriority):
    """Custom type tSapIngressIPCriteriaIpPrecMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapIngressIPCriteriaIpPrecMask_Type.__name__ = "Dot1PPriority"
_TSapIngressIPCriteriaIpPrecMask_Object = MibTableColumn
tSapIngressIPCriteriaIpPrecMask = _TSapIngressIPCriteriaIpPrecMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 5, 1, 32),
    _TSapIngressIPCriteriaIpPrecMask_Type()
)
tSapIngressIPCriteriaIpPrecMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaIpPrecMask.setStatus("current")
_TSapIngressMacCriteriaTable_Object = MibTable
tSapIngressMacCriteriaTable = _TSapIngressMacCriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6)
)
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaTable.setStatus("current")
_TSapIngressMacCriteriaEntry_Object = MibTableRow
tSapIngressMacCriteriaEntry = _TSapIngressMacCriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1)
)
tSapIngressMacCriteriaEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressMacCriteriaIndex"),
)
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaEntry.setStatus("current")
_TSapIngressMacCriteriaIndex_Type = TEntryId
_TSapIngressMacCriteriaIndex_Object = MibTableColumn
tSapIngressMacCriteriaIndex = _TSapIngressMacCriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 1),
    _TSapIngressMacCriteriaIndex_Type()
)
tSapIngressMacCriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaIndex.setStatus("current")
_TSapIngressMacCriteriaRowStatus_Type = RowStatus
_TSapIngressMacCriteriaRowStatus_Object = MibTableColumn
tSapIngressMacCriteriaRowStatus = _TSapIngressMacCriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 2),
    _TSapIngressMacCriteriaRowStatus_Type()
)
tSapIngressMacCriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaRowStatus.setStatus("current")


class _TSapIngressMacCriteriaDescription_Type(TItemDescription):
    """Custom type tSapIngressMacCriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TSapIngressMacCriteriaDescription_Object = MibTableColumn
tSapIngressMacCriteriaDescription = _TSapIngressMacCriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 3),
    _TSapIngressMacCriteriaDescription_Type()
)
tSapIngressMacCriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDescription.setStatus("current")
_TSapIngressMacCriteriaActionFC_Type = TNamedItemOrEmpty
_TSapIngressMacCriteriaActionFC_Object = MibTableColumn
tSapIngressMacCriteriaActionFC = _TSapIngressMacCriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 4),
    _TSapIngressMacCriteriaActionFC_Type()
)
tSapIngressMacCriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaActionFC.setStatus("current")


class _TSapIngressMacCriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressMacCriteriaActionPriority based on TPriorityOrDefault"""


_TSapIngressMacCriteriaActionPriority_Object = MibTableColumn
tSapIngressMacCriteriaActionPriority = _TSapIngressMacCriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 5),
    _TSapIngressMacCriteriaActionPriority_Type()
)
tSapIngressMacCriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaActionPriority.setStatus("current")


class _TSapIngressMacCriteriaFrameType_Type(TFrameType):
    """Custom type tSapIngressMacCriteriaFrameType based on TFrameType"""


_TSapIngressMacCriteriaFrameType_Object = MibTableColumn
tSapIngressMacCriteriaFrameType = _TSapIngressMacCriteriaFrameType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 6),
    _TSapIngressMacCriteriaFrameType_Type()
)
tSapIngressMacCriteriaFrameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaFrameType.setStatus("current")


class _TSapIngressMacCriteriaSrcMacAddr_Type(MacAddress):
    """Custom type tSapIngressMacCriteriaSrcMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TSapIngressMacCriteriaSrcMacAddr_Object = MibTableColumn
tSapIngressMacCriteriaSrcMacAddr = _TSapIngressMacCriteriaSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 8),
    _TSapIngressMacCriteriaSrcMacAddr_Type()
)
tSapIngressMacCriteriaSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSrcMacAddr.setStatus("current")


class _TSapIngressMacCriteriaSrcMacMask_Type(MacAddress):
    """Custom type tSapIngressMacCriteriaSrcMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TSapIngressMacCriteriaSrcMacMask_Object = MibTableColumn
tSapIngressMacCriteriaSrcMacMask = _TSapIngressMacCriteriaSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 9),
    _TSapIngressMacCriteriaSrcMacMask_Type()
)
tSapIngressMacCriteriaSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSrcMacMask.setStatus("current")


class _TSapIngressMacCriteriaDstMacAddr_Type(MacAddress):
    """Custom type tSapIngressMacCriteriaDstMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_TSapIngressMacCriteriaDstMacAddr_Object = MibTableColumn
tSapIngressMacCriteriaDstMacAddr = _TSapIngressMacCriteriaDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 10),
    _TSapIngressMacCriteriaDstMacAddr_Type()
)
tSapIngressMacCriteriaDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDstMacAddr.setStatus("current")


class _TSapIngressMacCriteriaDstMacMask_Type(MacAddress):
    """Custom type tSapIngressMacCriteriaDstMacMask based on MacAddress"""
    defaultHexValue = "000000000000"


_TSapIngressMacCriteriaDstMacMask_Object = MibTableColumn
tSapIngressMacCriteriaDstMacMask = _TSapIngressMacCriteriaDstMacMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 11),
    _TSapIngressMacCriteriaDstMacMask_Type()
)
tSapIngressMacCriteriaDstMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDstMacMask.setStatus("current")


class _TSapIngressMacCriteriaDot1PValue_Type(Dot1PPriority):
    """Custom type tSapIngressMacCriteriaDot1PValue based on Dot1PPriority"""
    defaultValue = -1


_TSapIngressMacCriteriaDot1PValue_Object = MibTableColumn
tSapIngressMacCriteriaDot1PValue = _TSapIngressMacCriteriaDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 12),
    _TSapIngressMacCriteriaDot1PValue_Type()
)
tSapIngressMacCriteriaDot1PValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDot1PValue.setStatus("current")


class _TSapIngressMacCriteriaDot1PMask_Type(Dot1PPriority):
    """Custom type tSapIngressMacCriteriaDot1PMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapIngressMacCriteriaDot1PMask_Type.__name__ = "Dot1PPriority"
_TSapIngressMacCriteriaDot1PMask_Object = MibTableColumn
tSapIngressMacCriteriaDot1PMask = _TSapIngressMacCriteriaDot1PMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 13),
    _TSapIngressMacCriteriaDot1PMask_Type()
)
tSapIngressMacCriteriaDot1PMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDot1PMask.setStatus("current")


class _TSapIngressMacCriteriaEthernetType_Type(Integer32):
    """Custom type tSapIngressMacCriteriaEthernetType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(1536, 65535),
    )


_TSapIngressMacCriteriaEthernetType_Type.__name__ = "Integer32"
_TSapIngressMacCriteriaEthernetType_Object = MibTableColumn
tSapIngressMacCriteriaEthernetType = _TSapIngressMacCriteriaEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 14),
    _TSapIngressMacCriteriaEthernetType_Type()
)
tSapIngressMacCriteriaEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaEthernetType.setStatus("current")


class _TSapIngressMacCriteriaDSAP_Type(ServiceAccessPoint):
    """Custom type tSapIngressMacCriteriaDSAP based on ServiceAccessPoint"""
    defaultValue = -1


_TSapIngressMacCriteriaDSAP_Object = MibTableColumn
tSapIngressMacCriteriaDSAP = _TSapIngressMacCriteriaDSAP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 15),
    _TSapIngressMacCriteriaDSAP_Type()
)
tSapIngressMacCriteriaDSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDSAP.setStatus("current")


class _TSapIngressMacCriteriaDSAPMask_Type(ServiceAccessPoint):
    """Custom type tSapIngressMacCriteriaDSAPMask based on ServiceAccessPoint"""
    defaultValue = -1


_TSapIngressMacCriteriaDSAPMask_Object = MibTableColumn
tSapIngressMacCriteriaDSAPMask = _TSapIngressMacCriteriaDSAPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 16),
    _TSapIngressMacCriteriaDSAPMask_Type()
)
tSapIngressMacCriteriaDSAPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaDSAPMask.setStatus("current")


class _TSapIngressMacCriteriaSSAP_Type(ServiceAccessPoint):
    """Custom type tSapIngressMacCriteriaSSAP based on ServiceAccessPoint"""
    defaultValue = -1


_TSapIngressMacCriteriaSSAP_Object = MibTableColumn
tSapIngressMacCriteriaSSAP = _TSapIngressMacCriteriaSSAP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 17),
    _TSapIngressMacCriteriaSSAP_Type()
)
tSapIngressMacCriteriaSSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSSAP.setStatus("current")


class _TSapIngressMacCriteriaSSAPMask_Type(ServiceAccessPoint):
    """Custom type tSapIngressMacCriteriaSSAPMask based on ServiceAccessPoint"""
    defaultValue = -1


_TSapIngressMacCriteriaSSAPMask_Object = MibTableColumn
tSapIngressMacCriteriaSSAPMask = _TSapIngressMacCriteriaSSAPMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 18),
    _TSapIngressMacCriteriaSSAPMask_Type()
)
tSapIngressMacCriteriaSSAPMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSSAPMask.setStatus("current")


class _TSapIngressMacCriteriaSnapPid_Type(Integer32):
    """Custom type tSapIngressMacCriteriaSnapPid based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_TSapIngressMacCriteriaSnapPid_Type.__name__ = "Integer32"
_TSapIngressMacCriteriaSnapPid_Object = MibTableColumn
tSapIngressMacCriteriaSnapPid = _TSapIngressMacCriteriaSnapPid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 19),
    _TSapIngressMacCriteriaSnapPid_Type()
)
tSapIngressMacCriteriaSnapPid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSnapPid.setStatus("current")


class _TSapIngressMacCriteriaSnapOui_Type(Integer32):
    """Custom type tSapIngressMacCriteriaSnapOui based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nonZero", 3),
          ("off", 1),
          ("zero", 2))
    )


_TSapIngressMacCriteriaSnapOui_Type.__name__ = "Integer32"
_TSapIngressMacCriteriaSnapOui_Object = MibTableColumn
tSapIngressMacCriteriaSnapOui = _TSapIngressMacCriteriaSnapOui_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 20),
    _TSapIngressMacCriteriaSnapOui_Type()
)
tSapIngressMacCriteriaSnapOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaSnapOui.setStatus("current")
_TSapIngressMacCriteriaLastChanged_Type = TimeStamp
_TSapIngressMacCriteriaLastChanged_Object = MibTableColumn
tSapIngressMacCriteriaLastChanged = _TSapIngressMacCriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 21),
    _TSapIngressMacCriteriaLastChanged_Type()
)
tSapIngressMacCriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaLastChanged.setStatus("current")


class _TSapIngressMacCriteriaAtmVci_Type(AtmVcIdentifier):
    """Custom type tSapIngressMacCriteriaAtmVci based on AtmVcIdentifier"""
    defaultValue = 0


_TSapIngressMacCriteriaAtmVci_Object = MibTableColumn
tSapIngressMacCriteriaAtmVci = _TSapIngressMacCriteriaAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 22),
    _TSapIngressMacCriteriaAtmVci_Type()
)
tSapIngressMacCriteriaAtmVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaAtmVci.setStatus("current")


class _TSapIngressMacCritInnerTagValue_Type(QTagFullRangeOrNone):
    """Custom type tSapIngressMacCritInnerTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TSapIngressMacCritInnerTagValue_Object = MibTableColumn
tSapIngressMacCritInnerTagValue = _TSapIngressMacCritInnerTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 23),
    _TSapIngressMacCritInnerTagValue_Type()
)
tSapIngressMacCritInnerTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCritInnerTagValue.setStatus("current")


class _TSapIngressMacCritInnerTagMask_Type(QTagFullRange):
    """Custom type tSapIngressMacCritInnerTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TSapIngressMacCritInnerTagMask_Type.__name__ = "QTagFullRange"
_TSapIngressMacCritInnerTagMask_Object = MibTableColumn
tSapIngressMacCritInnerTagMask = _TSapIngressMacCritInnerTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 24),
    _TSapIngressMacCritInnerTagMask_Type()
)
tSapIngressMacCritInnerTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCritInnerTagMask.setStatus("current")


class _TSapIngressMacCritOuterTagValue_Type(QTagFullRangeOrNone):
    """Custom type tSapIngressMacCritOuterTagValue based on QTagFullRangeOrNone"""
    defaultValue = -1


_TSapIngressMacCritOuterTagValue_Object = MibTableColumn
tSapIngressMacCritOuterTagValue = _TSapIngressMacCritOuterTagValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 25),
    _TSapIngressMacCritOuterTagValue_Type()
)
tSapIngressMacCritOuterTagValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCritOuterTagValue.setStatus("current")


class _TSapIngressMacCritOuterTagMask_Type(QTagFullRange):
    """Custom type tSapIngressMacCritOuterTagMask based on QTagFullRange"""
    defaultValue = 4095

    subtypeSpec = QTagFullRange.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_TSapIngressMacCritOuterTagMask_Type.__name__ = "QTagFullRange"
_TSapIngressMacCritOuterTagMask_Object = MibTableColumn
tSapIngressMacCritOuterTagMask = _TSapIngressMacCritOuterTagMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 6, 1, 26),
    _TSapIngressMacCritOuterTagMask_Type()
)
tSapIngressMacCritOuterTagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressMacCritOuterTagMask.setStatus("current")
_TSapIngressFCTable_Object = MibTable
tSapIngressFCTable = _TSapIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7)
)
if mibBuilder.loadTexts:
    tSapIngressFCTable.setStatus("current")
_TSapIngressFCEntry_Object = MibTableRow
tSapIngressFCEntry = _TSapIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1)
)
tSapIngressFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressFCName"),
)
if mibBuilder.loadTexts:
    tSapIngressFCEntry.setStatus("current")
_TSapIngressFCName_Type = TNamedItem
_TSapIngressFCName_Object = MibTableColumn
tSapIngressFCName = _TSapIngressFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 1),
    _TSapIngressFCName_Type()
)
tSapIngressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressFCName.setStatus("current")
_TSapIngressFCRowStatus_Type = RowStatus
_TSapIngressFCRowStatus_Object = MibTableColumn
tSapIngressFCRowStatus = _TSapIngressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 2),
    _TSapIngressFCRowStatus_Type()
)
tSapIngressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCRowStatus.setStatus("current")


class _TSapIngressFCQueue_Type(TIngressQueueId):
    """Custom type tSapIngressFCQueue based on TIngressQueueId"""
    defaultValue = 0


_TSapIngressFCQueue_Object = MibTableColumn
tSapIngressFCQueue = _TSapIngressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 3),
    _TSapIngressFCQueue_Type()
)
tSapIngressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQueue.setStatus("current")


class _TSapIngressFCMCastQueue_Type(TIngressQueueId):
    """Custom type tSapIngressFCMCastQueue based on TIngressQueueId"""
    defaultValue = 0


_TSapIngressFCMCastQueue_Object = MibTableColumn
tSapIngressFCMCastQueue = _TSapIngressFCMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 4),
    _TSapIngressFCMCastQueue_Type()
)
tSapIngressFCMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMCastQueue.setStatus("current")


class _TSapIngressFCBCastQueue_Type(TIngressQueueId):
    """Custom type tSapIngressFCBCastQueue based on TIngressQueueId"""
    defaultValue = 0


_TSapIngressFCBCastQueue_Object = MibTableColumn
tSapIngressFCBCastQueue = _TSapIngressFCBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 5),
    _TSapIngressFCBCastQueue_Type()
)
tSapIngressFCBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCBCastQueue.setStatus("current")


class _TSapIngressFCUnknownQueue_Type(TIngressQueueId):
    """Custom type tSapIngressFCUnknownQueue based on TIngressQueueId"""
    defaultValue = 0


_TSapIngressFCUnknownQueue_Object = MibTableColumn
tSapIngressFCUnknownQueue = _TSapIngressFCUnknownQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 6),
    _TSapIngressFCUnknownQueue_Type()
)
tSapIngressFCUnknownQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCUnknownQueue.setStatus("current")
_TSapIngressFCLastChanged_Type = TimeStamp
_TSapIngressFCLastChanged_Object = MibTableColumn
tSapIngressFCLastChanged = _TSapIngressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 7),
    _TSapIngressFCLastChanged_Type()
)
tSapIngressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressFCLastChanged.setStatus("current")


class _TSapIngressFCInProfRemark_Type(TRemarkType):
    """Custom type tSapIngressFCInProfRemark based on TRemarkType"""


_TSapIngressFCInProfRemark_Object = MibTableColumn
tSapIngressFCInProfRemark = _TSapIngressFCInProfRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 8),
    _TSapIngressFCInProfRemark_Type()
)
tSapIngressFCInProfRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCInProfRemark.setStatus("current")


class _TSapIngressFCInProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCInProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCInProfDscp_Object = MibTableColumn
tSapIngressFCInProfDscp = _TSapIngressFCInProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 9),
    _TSapIngressFCInProfDscp_Type()
)
tSapIngressFCInProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCInProfDscp.setStatus("current")


class _TSapIngressFCInProfPrec_Type(TPrecValueOrNone):
    """Custom type tSapIngressFCInProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TSapIngressFCInProfPrec_Object = MibTableColumn
tSapIngressFCInProfPrec = _TSapIngressFCInProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 10),
    _TSapIngressFCInProfPrec_Type()
)
tSapIngressFCInProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCInProfPrec.setStatus("current")


class _TSapIngressFCOutProfRemark_Type(TRemarkType):
    """Custom type tSapIngressFCOutProfRemark based on TRemarkType"""


_TSapIngressFCOutProfRemark_Object = MibTableColumn
tSapIngressFCOutProfRemark = _TSapIngressFCOutProfRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 11),
    _TSapIngressFCOutProfRemark_Type()
)
tSapIngressFCOutProfRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCOutProfRemark.setStatus("current")


class _TSapIngressFCOutProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCOutProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCOutProfDscp_Object = MibTableColumn
tSapIngressFCOutProfDscp = _TSapIngressFCOutProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 12),
    _TSapIngressFCOutProfDscp_Type()
)
tSapIngressFCOutProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCOutProfDscp.setStatus("current")


class _TSapIngressFCOutProfPrec_Type(TPrecValueOrNone):
    """Custom type tSapIngressFCOutProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TSapIngressFCOutProfPrec_Object = MibTableColumn
tSapIngressFCOutProfPrec = _TSapIngressFCOutProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 13),
    _TSapIngressFCOutProfPrec_Type()
)
tSapIngressFCOutProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCOutProfPrec.setStatus("current")


class _TSapIngressFCProfile_Type(TProfileOrNone):
    """Custom type tSapIngressFCProfile based on TProfileOrNone"""


_TSapIngressFCProfile_Object = MibTableColumn
tSapIngressFCProfile = _TSapIngressFCProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 14),
    _TSapIngressFCProfile_Type()
)
tSapIngressFCProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCProfile.setStatus("current")


class _TSapIngressFCHsmdaQueue_Type(TIngressHsmdaQueueId):
    """Custom type tSapIngressFCHsmdaQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TSapIngressFCHsmdaQueue_Object = MibTableColumn
tSapIngressFCHsmdaQueue = _TSapIngressFCHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 15),
    _TSapIngressFCHsmdaQueue_Type()
)
tSapIngressFCHsmdaQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCHsmdaQueue.setStatus("obsolete")


class _TSapIngressFCHsmdaMCastQueue_Type(TIngressHsmdaQueueId):
    """Custom type tSapIngressFCHsmdaMCastQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TSapIngressFCHsmdaMCastQueue_Object = MibTableColumn
tSapIngressFCHsmdaMCastQueue = _TSapIngressFCHsmdaMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 16),
    _TSapIngressFCHsmdaMCastQueue_Type()
)
tSapIngressFCHsmdaMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCHsmdaMCastQueue.setStatus("obsolete")


class _TSapIngressFCHsmdaBCastQueue_Type(TIngressHsmdaQueueId):
    """Custom type tSapIngressFCHsmdaBCastQueue based on TIngressHsmdaQueueId"""
    defaultValue = 0


_TSapIngressFCHsmdaBCastQueue_Object = MibTableColumn
tSapIngressFCHsmdaBCastQueue = _TSapIngressFCHsmdaBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 17),
    _TSapIngressFCHsmdaBCastQueue_Type()
)
tSapIngressFCHsmdaBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCHsmdaBCastQueue.setStatus("obsolete")


class _TSapIngressFCDE1OutOfProfile_Type(TruthValue):
    """Custom type tSapIngressFCDE1OutOfProfile based on TruthValue"""


_TSapIngressFCDE1OutOfProfile_Object = MibTableColumn
tSapIngressFCDE1OutOfProfile = _TSapIngressFCDE1OutOfProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 18),
    _TSapIngressFCDE1OutOfProfile_Type()
)
tSapIngressFCDE1OutOfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCDE1OutOfProfile.setStatus("current")


class _TSapIngressFCQGrp_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCQGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCQGrp_Object = MibTableColumn
tSapIngressFCQGrp = _TSapIngressFCQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 19),
    _TSapIngressFCQGrp_Type()
)
tSapIngressFCQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQGrp.setStatus("current")


class _TSapIngressFCQGrpMCast_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCQGrpMCast based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCQGrpMCast_Object = MibTableColumn
tSapIngressFCQGrpMCast = _TSapIngressFCQGrpMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 20),
    _TSapIngressFCQGrpMCast_Type()
)
tSapIngressFCQGrpMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQGrpMCast.setStatus("current")


class _TSapIngressFCQGrpBCast_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCQGrpBCast based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCQGrpBCast_Object = MibTableColumn
tSapIngressFCQGrpBCast = _TSapIngressFCQGrpBCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 21),
    _TSapIngressFCQGrpBCast_Type()
)
tSapIngressFCQGrpBCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQGrpBCast.setStatus("current")


class _TSapIngressFCQGrpUnknown_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressFCQGrpUnknown based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressFCQGrpUnknown_Object = MibTableColumn
tSapIngressFCQGrpUnknown = _TSapIngressFCQGrpUnknown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 22),
    _TSapIngressFCQGrpUnknown_Type()
)
tSapIngressFCQGrpUnknown.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQGrpUnknown.setStatus("current")


class _TSapIngressFCPolicer_Type(TIngPolicerIdOrNone):
    """Custom type tSapIngressFCPolicer based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TSapIngressFCPolicer_Object = MibTableColumn
tSapIngressFCPolicer = _TSapIngressFCPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 23),
    _TSapIngressFCPolicer_Type()
)
tSapIngressFCPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCPolicer.setStatus("current")


class _TSapIngressFCMCastPolicer_Type(TIngPolicerIdOrNone):
    """Custom type tSapIngressFCMCastPolicer based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TSapIngressFCMCastPolicer_Object = MibTableColumn
tSapIngressFCMCastPolicer = _TSapIngressFCMCastPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 24),
    _TSapIngressFCMCastPolicer_Type()
)
tSapIngressFCMCastPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMCastPolicer.setStatus("current")


class _TSapIngressFCBCastPolicer_Type(TIngPolicerIdOrNone):
    """Custom type tSapIngressFCBCastPolicer based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TSapIngressFCBCastPolicer_Object = MibTableColumn
tSapIngressFCBCastPolicer = _TSapIngressFCBCastPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 25),
    _TSapIngressFCBCastPolicer_Type()
)
tSapIngressFCBCastPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCBCastPolicer.setStatus("current")


class _TSapIngressFCUnknownPolicer_Type(TIngPolicerIdOrNone):
    """Custom type tSapIngressFCUnknownPolicer based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TSapIngressFCUnknownPolicer_Object = MibTableColumn
tSapIngressFCUnknownPolicer = _TSapIngressFCUnknownPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 26),
    _TSapIngressFCUnknownPolicer_Type()
)
tSapIngressFCUnknownPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCUnknownPolicer.setStatus("current")


class _TSapIngressFCPlcrFPQGrp_Type(TruthValue):
    """Custom type tSapIngressFCPlcrFPQGrp based on TruthValue"""


_TSapIngressFCPlcrFPQGrp_Object = MibTableColumn
tSapIngressFCPlcrFPQGrp = _TSapIngressFCPlcrFPQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 27),
    _TSapIngressFCPlcrFPQGrp_Type()
)
tSapIngressFCPlcrFPQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCPlcrFPQGrp.setStatus("current")


class _TSapIngressFCMCastPlcrFPQGrp_Type(TruthValue):
    """Custom type tSapIngressFCMCastPlcrFPQGrp based on TruthValue"""


_TSapIngressFCMCastPlcrFPQGrp_Object = MibTableColumn
tSapIngressFCMCastPlcrFPQGrp = _TSapIngressFCMCastPlcrFPQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 28),
    _TSapIngressFCMCastPlcrFPQGrp_Type()
)
tSapIngressFCMCastPlcrFPQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMCastPlcrFPQGrp.setStatus("current")


class _TSapIngressFCBCastPlcrFPQGrp_Type(TruthValue):
    """Custom type tSapIngressFCBCastPlcrFPQGrp based on TruthValue"""


_TSapIngressFCBCastPlcrFPQGrp_Object = MibTableColumn
tSapIngressFCBCastPlcrFPQGrp = _TSapIngressFCBCastPlcrFPQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 29),
    _TSapIngressFCBCastPlcrFPQGrp_Type()
)
tSapIngressFCBCastPlcrFPQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCBCastPlcrFPQGrp.setStatus("current")


class _TSapIngressFCUnknownPlcrFPQGrp_Type(TruthValue):
    """Custom type tSapIngressFCUnknownPlcrFPQGrp based on TruthValue"""


_TSapIngressFCUnknownPlcrFPQGrp_Object = MibTableColumn
tSapIngressFCUnknownPlcrFPQGrp = _TSapIngressFCUnknownPlcrFPQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 30),
    _TSapIngressFCUnknownPlcrFPQGrp_Type()
)
tSapIngressFCUnknownPlcrFPQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCUnknownPlcrFPQGrp.setStatus("current")
_TSapIngressPrecTable_Object = MibTable
tSapIngressPrecTable = _TSapIngressPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8)
)
if mibBuilder.loadTexts:
    tSapIngressPrecTable.setStatus("current")
_TSapIngressPrecEntry_Object = MibTableRow
tSapIngressPrecEntry = _TSapIngressPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1)
)
tSapIngressPrecEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressPrecValue"),
)
if mibBuilder.loadTexts:
    tSapIngressPrecEntry.setStatus("current")
_TSapIngressPrecValue_Type = TPrecValue
_TSapIngressPrecValue_Object = MibTableColumn
tSapIngressPrecValue = _TSapIngressPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 1),
    _TSapIngressPrecValue_Type()
)
tSapIngressPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressPrecValue.setStatus("current")
_TSapIngressPrecRowStatus_Type = RowStatus
_TSapIngressPrecRowStatus_Object = MibTableColumn
tSapIngressPrecRowStatus = _TSapIngressPrecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 2),
    _TSapIngressPrecRowStatus_Type()
)
tSapIngressPrecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressPrecRowStatus.setStatus("current")


class _TSapIngressPrecFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressPrecFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressPrecFC_Object = MibTableColumn
tSapIngressPrecFC = _TSapIngressPrecFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 3),
    _TSapIngressPrecFC_Type()
)
tSapIngressPrecFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressPrecFC.setStatus("current")


class _TSapIngressPrecFCPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressPrecFCPriority based on TPriorityOrDefault"""


_TSapIngressPrecFCPriority_Object = MibTableColumn
tSapIngressPrecFCPriority = _TSapIngressPrecFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 4),
    _TSapIngressPrecFCPriority_Type()
)
tSapIngressPrecFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressPrecFCPriority.setStatus("current")
_TSapIngressPrecLastChanged_Type = TimeStamp
_TSapIngressPrecLastChanged_Object = MibTableColumn
tSapIngressPrecLastChanged = _TSapIngressPrecLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 5),
    _TSapIngressPrecLastChanged_Type()
)
tSapIngressPrecLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressPrecLastChanged.setStatus("current")


class _TSapIngressPrecHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressPrecHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressPrecHsmdaCntrOvr_Object = MibTableColumn
tSapIngressPrecHsmdaCntrOvr = _TSapIngressPrecHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 8, 1, 6),
    _TSapIngressPrecHsmdaCntrOvr_Type()
)
tSapIngressPrecHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressPrecHsmdaCntrOvr.setStatus("obsolete")
_TSapIngressIPv6CriteriaTable_Object = MibTable
tSapIngressIPv6CriteriaTable = _TSapIngressIPv6CriteriaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9)
)
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaTable.setStatus("current")
_TSapIngressIPv6CriteriaEntry_Object = MibTableRow
tSapIngressIPv6CriteriaEntry = _TSapIngressIPv6CriteriaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1)
)
tSapIngressIPv6CriteriaEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaIndex"),
)
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaEntry.setStatus("current")
_TSapIngressIPv6CriteriaIndex_Type = TEntryId
_TSapIngressIPv6CriteriaIndex_Object = MibTableColumn
tSapIngressIPv6CriteriaIndex = _TSapIngressIPv6CriteriaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 1),
    _TSapIngressIPv6CriteriaIndex_Type()
)
tSapIngressIPv6CriteriaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaIndex.setStatus("current")
_TSapIngressIPv6CriteriaRowStatus_Type = RowStatus
_TSapIngressIPv6CriteriaRowStatus_Object = MibTableColumn
tSapIngressIPv6CriteriaRowStatus = _TSapIngressIPv6CriteriaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 2),
    _TSapIngressIPv6CriteriaRowStatus_Type()
)
tSapIngressIPv6CriteriaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaRowStatus.setStatus("current")


class _TSapIngressIPv6CriteriaDescription_Type(TItemDescription):
    """Custom type tSapIngressIPv6CriteriaDescription based on TItemDescription"""
    defaultHexValue = ""


_TSapIngressIPv6CriteriaDescription_Object = MibTableColumn
tSapIngressIPv6CriteriaDescription = _TSapIngressIPv6CriteriaDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 3),
    _TSapIngressIPv6CriteriaDescription_Type()
)
tSapIngressIPv6CriteriaDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDescription.setStatus("current")


class _TSapIngressIPv6CriteriaActionFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressIPv6CriteriaActionFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressIPv6CriteriaActionFC_Object = MibTableColumn
tSapIngressIPv6CriteriaActionFC = _TSapIngressIPv6CriteriaActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 4),
    _TSapIngressIPv6CriteriaActionFC_Type()
)
tSapIngressIPv6CriteriaActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaActionFC.setStatus("current")


class _TSapIngressIPv6CriteriaActionPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressIPv6CriteriaActionPriority based on TPriorityOrDefault"""


_TSapIngressIPv6CriteriaActionPriority_Object = MibTableColumn
tSapIngressIPv6CriteriaActionPriority = _TSapIngressIPv6CriteriaActionPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 5),
    _TSapIngressIPv6CriteriaActionPriority_Type()
)
tSapIngressIPv6CriteriaActionPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaActionPriority.setStatus("current")


class _TSapIngressIPv6CriteriaSourceIpAddr_Type(InetAddressIPv6):
    """Custom type tSapIngressIPv6CriteriaSourceIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TSapIngressIPv6CriteriaSourceIpAddr_Object = MibTableColumn
tSapIngressIPv6CriteriaSourceIpAddr = _TSapIngressIPv6CriteriaSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 6),
    _TSapIngressIPv6CriteriaSourceIpAddr_Type()
)
tSapIngressIPv6CriteriaSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaSourceIpAddr.setStatus("current")


class _TSapIngressIPv6CriteriaSourceIpMask_Type(InetAddressPrefixLength):
    """Custom type tSapIngressIPv6CriteriaSourceIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TSapIngressIPv6CriteriaSourceIpMask_Type.__name__ = "InetAddressPrefixLength"
_TSapIngressIPv6CriteriaSourceIpMask_Object = MibTableColumn
tSapIngressIPv6CriteriaSourceIpMask = _TSapIngressIPv6CriteriaSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 7),
    _TSapIngressIPv6CriteriaSourceIpMask_Type()
)
tSapIngressIPv6CriteriaSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaSourceIpMask.setStatus("current")


class _TSapIngressIPv6CriteriaDestIpAddr_Type(InetAddressIPv6):
    """Custom type tSapIngressIPv6CriteriaDestIpAddr based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_TSapIngressIPv6CriteriaDestIpAddr_Object = MibTableColumn
tSapIngressIPv6CriteriaDestIpAddr = _TSapIngressIPv6CriteriaDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 8),
    _TSapIngressIPv6CriteriaDestIpAddr_Type()
)
tSapIngressIPv6CriteriaDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDestIpAddr.setStatus("current")


class _TSapIngressIPv6CriteriaDestIpMask_Type(InetAddressPrefixLength):
    """Custom type tSapIngressIPv6CriteriaDestIpMask based on InetAddressPrefixLength"""
    defaultValue = 0

    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TSapIngressIPv6CriteriaDestIpMask_Type.__name__ = "InetAddressPrefixLength"
_TSapIngressIPv6CriteriaDestIpMask_Object = MibTableColumn
tSapIngressIPv6CriteriaDestIpMask = _TSapIngressIPv6CriteriaDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 9),
    _TSapIngressIPv6CriteriaDestIpMask_Type()
)
tSapIngressIPv6CriteriaDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDestIpMask.setStatus("current")


class _TSapIngressIPv6CriteriaNextHeader_Type(TIpProtocol):
    """Custom type tSapIngressIPv6CriteriaNextHeader based on TIpProtocol"""
    defaultValue = -1


_TSapIngressIPv6CriteriaNextHeader_Object = MibTableColumn
tSapIngressIPv6CriteriaNextHeader = _TSapIngressIPv6CriteriaNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 10),
    _TSapIngressIPv6CriteriaNextHeader_Type()
)
tSapIngressIPv6CriteriaNextHeader.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaNextHeader.setStatus("current")


class _TSapIngressIPv6CriteriaSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tSapIngressIPv6CriteriaSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPv6CriteriaSourcePortValue1_Object = MibTableColumn
tSapIngressIPv6CriteriaSourcePortValue1 = _TSapIngressIPv6CriteriaSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 11),
    _TSapIngressIPv6CriteriaSourcePortValue1_Type()
)
tSapIngressIPv6CriteriaSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaSourcePortValue1.setStatus("current")


class _TSapIngressIPv6CriteriaSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tSapIngressIPv6CriteriaSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPv6CriteriaSourcePortValue2_Object = MibTableColumn
tSapIngressIPv6CriteriaSourcePortValue2 = _TSapIngressIPv6CriteriaSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 12),
    _TSapIngressIPv6CriteriaSourcePortValue2_Type()
)
tSapIngressIPv6CriteriaSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaSourcePortValue2.setStatus("current")


class _TSapIngressIPv6CriteriaSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapIngressIPv6CriteriaSourcePortOperator based on TTcpUdpPortOperator"""


_TSapIngressIPv6CriteriaSourcePortOperator_Object = MibTableColumn
tSapIngressIPv6CriteriaSourcePortOperator = _TSapIngressIPv6CriteriaSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 13),
    _TSapIngressIPv6CriteriaSourcePortOperator_Type()
)
tSapIngressIPv6CriteriaSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaSourcePortOperator.setStatus("current")


class _TSapIngressIPv6CriteriaDestPortValue1_Type(TTcpUdpPort):
    """Custom type tSapIngressIPv6CriteriaDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPv6CriteriaDestPortValue1_Object = MibTableColumn
tSapIngressIPv6CriteriaDestPortValue1 = _TSapIngressIPv6CriteriaDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 14),
    _TSapIngressIPv6CriteriaDestPortValue1_Type()
)
tSapIngressIPv6CriteriaDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDestPortValue1.setStatus("current")


class _TSapIngressIPv6CriteriaDestPortValue2_Type(TTcpUdpPort):
    """Custom type tSapIngressIPv6CriteriaDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapIngressIPv6CriteriaDestPortValue2_Object = MibTableColumn
tSapIngressIPv6CriteriaDestPortValue2 = _TSapIngressIPv6CriteriaDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 15),
    _TSapIngressIPv6CriteriaDestPortValue2_Type()
)
tSapIngressIPv6CriteriaDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDestPortValue2.setStatus("current")


class _TSapIngressIPv6CriteriaDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapIngressIPv6CriteriaDestPortOperator based on TTcpUdpPortOperator"""


_TSapIngressIPv6CriteriaDestPortOperator_Object = MibTableColumn
tSapIngressIPv6CriteriaDestPortOperator = _TSapIngressIPv6CriteriaDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 16),
    _TSapIngressIPv6CriteriaDestPortOperator_Type()
)
tSapIngressIPv6CriteriaDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDestPortOperator.setStatus("current")


class _TSapIngressIPv6CriteriaDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tSapIngressIPv6CriteriaDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TSapIngressIPv6CriteriaDSCP_Object = MibTableColumn
tSapIngressIPv6CriteriaDSCP = _TSapIngressIPv6CriteriaDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 17),
    _TSapIngressIPv6CriteriaDSCP_Type()
)
tSapIngressIPv6CriteriaDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaDSCP.setStatus("current")
_TSapIngressIPv6CriteriaLastChanged_Type = TimeStamp
_TSapIngressIPv6CriteriaLastChanged_Object = MibTableColumn
tSapIngressIPv6CriteriaLastChanged = _TSapIngressIPv6CriteriaLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 20),
    _TSapIngressIPv6CriteriaLastChanged_Type()
)
tSapIngressIPv6CriteriaLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaLastChanged.setStatus("current")


class _TSapIngressIPv6CriteriaIpPrecValue_Type(Dot1PPriority):
    """Custom type tSapIngressIPv6CriteriaIpPrecValue based on Dot1PPriority"""
    defaultValue = -1


_TSapIngressIPv6CriteriaIpPrecValue_Object = MibTableColumn
tSapIngressIPv6CriteriaIpPrecValue = _TSapIngressIPv6CriteriaIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 31),
    _TSapIngressIPv6CriteriaIpPrecValue_Type()
)
tSapIngressIPv6CriteriaIpPrecValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaIpPrecValue.setStatus("current")


class _TSapIngressIPv6CriteriaIpPrecMask_Type(Dot1PPriority):
    """Custom type tSapIngressIPv6CriteriaIpPrecMask based on Dot1PPriority"""
    defaultValue = 0

    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapIngressIPv6CriteriaIpPrecMask_Type.__name__ = "Dot1PPriority"
_TSapIngressIPv6CriteriaIpPrecMask_Object = MibTableColumn
tSapIngressIPv6CriteriaIpPrecMask = _TSapIngressIPv6CriteriaIpPrecMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 9, 1, 32),
    _TSapIngressIPv6CriteriaIpPrecMask_Type()
)
tSapIngressIPv6CriteriaIpPrecMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaIpPrecMask.setStatus("current")
_TSapIngressHsmdaQueueTable_Object = MibTable
tSapIngressHsmdaQueueTable = _TSapIngressHsmdaQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10)
)
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueTable.setStatus("obsolete")
_TSapIngressHsmdaQueueEntry_Object = MibTableRow
tSapIngressHsmdaQueueEntry = _TSapIngressHsmdaQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1)
)
tSapIngressHsmdaQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressHsmdaQueue"),
)
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueEntry.setStatus("obsolete")


class _TSapIngressHsmdaQueue_Type(TIngressHsmdaQueueId):
    """Custom type tSapIngressHsmdaQueue based on TIngressHsmdaQueueId"""
    subtypeSpec = TIngressHsmdaQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSapIngressHsmdaQueue_Type.__name__ = "TIngressHsmdaQueueId"
_TSapIngressHsmdaQueue_Object = MibTableColumn
tSapIngressHsmdaQueue = _TSapIngressHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 1),
    _TSapIngressHsmdaQueue_Type()
)
tSapIngressHsmdaQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueue.setStatus("obsolete")
_TSapIngressHsmdaQueueRowStatus_Type = RowStatus
_TSapIngressHsmdaQueueRowStatus_Object = MibTableColumn
tSapIngressHsmdaQueueRowStatus = _TSapIngressHsmdaQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 2),
    _TSapIngressHsmdaQueueRowStatus_Type()
)
tSapIngressHsmdaQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueRowStatus.setStatus("obsolete")
_TSapIngressHsmdaQueueLastChanged_Type = TimeStamp
_TSapIngressHsmdaQueueLastChanged_Object = MibTableColumn
tSapIngressHsmdaQueueLastChanged = _TSapIngressHsmdaQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 3),
    _TSapIngressHsmdaQueueLastChanged_Type()
)
tSapIngressHsmdaQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueLastChanged.setStatus("obsolete")


class _TSapIngressHsmdaQueueCIRAdaptn_Type(TAdaptationRule):
    """Custom type tSapIngressHsmdaQueueCIRAdaptn based on TAdaptationRule"""


_TSapIngressHsmdaQueueCIRAdaptn_Object = MibTableColumn
tSapIngressHsmdaQueueCIRAdaptn = _TSapIngressHsmdaQueueCIRAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 4),
    _TSapIngressHsmdaQueueCIRAdaptn_Type()
)
tSapIngressHsmdaQueueCIRAdaptn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueCIRAdaptn.setStatus("obsolete")


class _TSapIngressHsmdaQueuePIRAdaptn_Type(TAdaptationRule):
    """Custom type tSapIngressHsmdaQueuePIRAdaptn based on TAdaptationRule"""


_TSapIngressHsmdaQueuePIRAdaptn_Object = MibTableColumn
tSapIngressHsmdaQueuePIRAdaptn = _TSapIngressHsmdaQueuePIRAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 5),
    _TSapIngressHsmdaQueuePIRAdaptn_Type()
)
tSapIngressHsmdaQueuePIRAdaptn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueuePIRAdaptn.setStatus("obsolete")


class _TSapIngressHsmdaQueueAdminPIR_Type(THsmdaPIRKRate):
    """Custom type tSapIngressHsmdaQueueAdminPIR based on THsmdaPIRKRate"""
    defaultValue = -1


_TSapIngressHsmdaQueueAdminPIR_Object = MibTableColumn
tSapIngressHsmdaQueueAdminPIR = _TSapIngressHsmdaQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 6),
    _TSapIngressHsmdaQueueAdminPIR_Type()
)
tSapIngressHsmdaQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueAdminPIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueAdminPIR.setUnits("kbps")


class _TSapIngressHsmdaQueueAdminCIR_Type(THsmdaCIRKRate):
    """Custom type tSapIngressHsmdaQueueAdminCIR based on THsmdaCIRKRate"""
    defaultValue = 0


_TSapIngressHsmdaQueueAdminCIR_Object = MibTableColumn
tSapIngressHsmdaQueueAdminCIR = _TSapIngressHsmdaQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 7),
    _TSapIngressHsmdaQueueAdminCIR_Type()
)
tSapIngressHsmdaQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueAdminCIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueAdminCIR.setUnits("kbps")


class _TSapIngressHsmdaQueueSlopePolicy_Type(TNamedItem):
    """Custom type tSapIngressHsmdaQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TSapIngressHsmdaQueueSlopePolicy_Object = MibTableColumn
tSapIngressHsmdaQueueSlopePolicy = _TSapIngressHsmdaQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 8),
    _TSapIngressHsmdaQueueSlopePolicy_Type()
)
tSapIngressHsmdaQueueSlopePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueueSlopePolicy.setStatus("obsolete")


class _TSapIngressHsmdaQueuePoliced_Type(TruthValue):
    """Custom type tSapIngressHsmdaQueuePoliced based on TruthValue"""


_TSapIngressHsmdaQueuePoliced_Object = MibTableColumn
tSapIngressHsmdaQueuePoliced = _TSapIngressHsmdaQueuePoliced_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 10, 1, 9),
    _TSapIngressHsmdaQueuePoliced_Type()
)
tSapIngressHsmdaQueuePoliced.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressHsmdaQueuePoliced.setStatus("obsolete")
_TSapIngressLspExpTable_Object = MibTable
tSapIngressLspExpTable = _TSapIngressLspExpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11)
)
if mibBuilder.loadTexts:
    tSapIngressLspExpTable.setStatus("current")
_TSapIngressLspExpEntry_Object = MibTableRow
tSapIngressLspExpEntry = _TSapIngressLspExpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1)
)
tSapIngressLspExpEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngressLspExpValue"),
)
if mibBuilder.loadTexts:
    tSapIngressLspExpEntry.setStatus("current")


class _TSapIngressLspExpValue_Type(TLspExpValue):
    """Custom type tSapIngressLspExpValue based on TLspExpValue"""
    subtypeSpec = TLspExpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapIngressLspExpValue_Type.__name__ = "TLspExpValue"
_TSapIngressLspExpValue_Object = MibTableColumn
tSapIngressLspExpValue = _TSapIngressLspExpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 1),
    _TSapIngressLspExpValue_Type()
)
tSapIngressLspExpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngressLspExpValue.setStatus("current")
_TSapIngressLspExpRowStatus_Type = RowStatus
_TSapIngressLspExpRowStatus_Object = MibTableColumn
tSapIngressLspExpRowStatus = _TSapIngressLspExpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 2),
    _TSapIngressLspExpRowStatus_Type()
)
tSapIngressLspExpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressLspExpRowStatus.setStatus("current")
_TSapIngressLspExpLastChanged_Type = TimeStamp
_TSapIngressLspExpLastChanged_Object = MibTableColumn
tSapIngressLspExpLastChanged = _TSapIngressLspExpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 3),
    _TSapIngressLspExpLastChanged_Type()
)
tSapIngressLspExpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressLspExpLastChanged.setStatus("current")


class _TSapIngressLspExpFC_Type(TNamedItemOrEmpty):
    """Custom type tSapIngressLspExpFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngressLspExpFC_Object = MibTableColumn
tSapIngressLspExpFC = _TSapIngressLspExpFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 4),
    _TSapIngressLspExpFC_Type()
)
tSapIngressLspExpFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressLspExpFC.setStatus("current")


class _TSapIngressLspExpFCPriority_Type(TPriorityOrDefault):
    """Custom type tSapIngressLspExpFCPriority based on TPriorityOrDefault"""


_TSapIngressLspExpFCPriority_Object = MibTableColumn
tSapIngressLspExpFCPriority = _TSapIngressLspExpFCPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 5),
    _TSapIngressLspExpFCPriority_Type()
)
tSapIngressLspExpFCPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressLspExpFCPriority.setStatus("current")


class _TSapIngressLspExpHsmdaCntrOvr_Type(TIngressHsmdaCounterIdOrZero):
    """Custom type tSapIngressLspExpHsmdaCntrOvr based on TIngressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapIngressLspExpHsmdaCntrOvr_Object = MibTableColumn
tSapIngressLspExpHsmdaCntrOvr = _TSapIngressLspExpHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 11, 1, 6),
    _TSapIngressLspExpHsmdaCntrOvr_Type()
)
tSapIngressLspExpHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressLspExpHsmdaCntrOvr.setStatus("obsolete")
_TSapIngPolicerTable_Object = MibTable
tSapIngPolicerTable = _TSapIngPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12)
)
if mibBuilder.loadTexts:
    tSapIngPolicerTable.setStatus("current")
_TSapIngPolicerEntry_Object = MibTableRow
tSapIngPolicerEntry = _TSapIngPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1)
)
tSapIngPolicerEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapIngPolicerId"),
)
if mibBuilder.loadTexts:
    tSapIngPolicerEntry.setStatus("current")
_TSapIngPolicerId_Type = TIngPolicerId
_TSapIngPolicerId_Object = MibTableColumn
tSapIngPolicerId = _TSapIngPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 1),
    _TSapIngPolicerId_Type()
)
tSapIngPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapIngPolicerId.setStatus("current")
_TSapIngPolicerRowStatus_Type = RowStatus
_TSapIngPolicerRowStatus_Object = MibTableColumn
tSapIngPolicerRowStatus = _TSapIngPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 2),
    _TSapIngPolicerRowStatus_Type()
)
tSapIngPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerRowStatus.setStatus("current")
_TSapIngPolicerLastChanged_Type = TimeStamp
_TSapIngPolicerLastChanged_Object = MibTableColumn
tSapIngPolicerLastChanged = _TSapIngPolicerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 3),
    _TSapIngPolicerLastChanged_Type()
)
tSapIngPolicerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicerLastChanged.setStatus("current")


class _TSapIngPolicerDescr_Type(TItemDescription):
    """Custom type tSapIngPolicerDescr based on TItemDescription"""
    defaultHexValue = ""


_TSapIngPolicerDescr_Object = MibTableColumn
tSapIngPolicerDescr = _TSapIngPolicerDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 4),
    _TSapIngPolicerDescr_Type()
)
tSapIngPolicerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerDescr.setStatus("current")


class _TSapIngPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngPolicerPIRAdaptation based on TAdaptationRule"""


_TSapIngPolicerPIRAdaptation_Object = MibTableColumn
tSapIngPolicerPIRAdaptation = _TSapIngPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 5),
    _TSapIngPolicerPIRAdaptation_Type()
)
tSapIngPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerPIRAdaptation.setStatus("current")


class _TSapIngPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapIngPolicerCIRAdaptation based on TAdaptationRule"""


_TSapIngPolicerCIRAdaptation_Object = MibTableColumn
tSapIngPolicerCIRAdaptation = _TSapIngPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 6),
    _TSapIngPolicerCIRAdaptation_Type()
)
tSapIngPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerCIRAdaptation.setStatus("current")


class _TSapIngPolicerParent_Type(TNamedItemOrEmpty):
    """Custom type tSapIngPolicerParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngPolicerParent_Object = MibTableColumn
tSapIngPolicerParent = _TSapIngPolicerParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 7),
    _TSapIngPolicerParent_Type()
)
tSapIngPolicerParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerParent.setStatus("current")


class _TSapIngPolicerLevel_Type(TLevel):
    """Custom type tSapIngPolicerLevel based on TLevel"""
    defaultValue = 1


_TSapIngPolicerLevel_Object = MibTableColumn
tSapIngPolicerLevel = _TSapIngPolicerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 8),
    _TSapIngPolicerLevel_Type()
)
tSapIngPolicerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerLevel.setStatus("current")


class _TSapIngPolicerWeight_Type(TPolicerWeight):
    """Custom type tSapIngPolicerWeight based on TPolicerWeight"""
    defaultValue = 1


_TSapIngPolicerWeight_Object = MibTableColumn
tSapIngPolicerWeight = _TSapIngPolicerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 9),
    _TSapIngPolicerWeight_Type()
)
tSapIngPolicerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerWeight.setStatus("current")


class _TSapIngPolicerAdminPIR_Type(THPolPIRRate):
    """Custom type tSapIngPolicerAdminPIR based on THPolPIRRate"""
    defaultValue = -1


_TSapIngPolicerAdminPIR_Object = MibTableColumn
tSapIngPolicerAdminPIR = _TSapIngPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 10),
    _TSapIngPolicerAdminPIR_Type()
)
tSapIngPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminPIR.setUnits("kbps")


class _TSapIngPolicerAdminCIR_Type(THPolCIRRate):
    """Custom type tSapIngPolicerAdminCIR based on THPolCIRRate"""
    defaultValue = 0


_TSapIngPolicerAdminCIR_Object = MibTableColumn
tSapIngPolicerAdminCIR = _TSapIngPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 11),
    _TSapIngPolicerAdminCIR_Type()
)
tSapIngPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminCIR.setUnits("kbps")


class _TSapIngPolicerStatMode_Type(TmnxIngPolicerStatMode):
    """Custom type tSapIngPolicerStatMode based on TmnxIngPolicerStatMode"""


_TSapIngPolicerStatMode_Object = MibTableColumn
tSapIngPolicerStatMode = _TSapIngPolicerStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 12),
    _TSapIngPolicerStatMode_Type()
)
tSapIngPolicerStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerStatMode.setStatus("current")


class _TSapIngPolicerMBS_Type(TPlcrBurstSizeBytes):
    """Custom type tSapIngPolicerMBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TSapIngPolicerMBS_Object = MibTableColumn
tSapIngPolicerMBS = _TSapIngPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 13),
    _TSapIngPolicerMBS_Type()
)
tSapIngPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerMBS.setUnits("bytes")


class _TSapIngPolicerHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tSapIngPolicerHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TSapIngPolicerHiPrioOnly_Object = MibTableColumn
tSapIngPolicerHiPrioOnly = _TSapIngPolicerHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 14),
    _TSapIngPolicerHiPrioOnly_Type()
)
tSapIngPolicerHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerHiPrioOnly.setUnits("percent")


class _TSapIngPolicerCBS_Type(TPlcrBurstSizeBytes):
    """Custom type tSapIngPolicerCBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TSapIngPolicerCBS_Object = MibTableColumn
tSapIngPolicerCBS = _TSapIngPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 15),
    _TSapIngPolicerCBS_Type()
)
tSapIngPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerCBS.setUnits("bytes")


class _TSapIngPolicerPktOffset_Type(TPerPacketOffset):
    """Custom type tSapIngPolicerPktOffset based on TPerPacketOffset"""
    defaultValue = 0


_TSapIngPolicerPktOffset_Object = MibTableColumn
tSapIngPolicerPktOffset = _TSapIngPolicerPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 16),
    _TSapIngPolicerPktOffset_Type()
)
tSapIngPolicerPktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerPktOffset.setStatus("current")


class _TSapIngPolicerAdminPIRPercent_Type(Unsigned32):
    """Custom type tSapIngPolicerAdminPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapIngPolicerAdminPIRPercent_Type.__name__ = "Unsigned32"
_TSapIngPolicerAdminPIRPercent_Object = MibTableColumn
tSapIngPolicerAdminPIRPercent = _TSapIngPolicerAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 17),
    _TSapIngPolicerAdminPIRPercent_Type()
)
tSapIngPolicerAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminPIRPercent.setUnits("hundredths of a percent")


class _TSapIngPolicerAdminCIRPercent_Type(Unsigned32):
    """Custom type tSapIngPolicerAdminCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TSapIngPolicerAdminCIRPercent_Type.__name__ = "Unsigned32"
_TSapIngPolicerAdminCIRPercent_Object = MibTableColumn
tSapIngPolicerAdminCIRPercent = _TSapIngPolicerAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 18),
    _TSapIngPolicerAdminCIRPercent_Type()
)
tSapIngPolicerAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerAdminCIRPercent.setUnits("hundredths of a percent")


class _TSapIngPolicerRateType_Type(TPolicerRateType):
    """Custom type tSapIngPolicerRateType based on TPolicerRateType"""


_TSapIngPolicerRateType_Object = MibTableColumn
tSapIngPolicerRateType = _TSapIngPolicerRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 19),
    _TSapIngPolicerRateType_Type()
)
tSapIngPolicerRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerRateType.setStatus("current")


class _TSapIngPolicerSlopeStartDepth_Type(Unsigned32):
    """Custom type tSapIngPolicerSlopeStartDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapIngPolicerSlopeStartDepth_Type.__name__ = "Unsigned32"
_TSapIngPolicerSlopeStartDepth_Object = MibTableColumn
tSapIngPolicerSlopeStartDepth = _TSapIngPolicerSlopeStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 20),
    _TSapIngPolicerSlopeStartDepth_Type()
)
tSapIngPolicerSlopeStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeStartDepth.setUnits("hundredths of a percent")


class _TSapIngPolicerSlopeMaxDepth_Type(Unsigned32):
    """Custom type tSapIngPolicerSlopeMaxDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapIngPolicerSlopeMaxDepth_Type.__name__ = "Unsigned32"
_TSapIngPolicerSlopeMaxDepth_Object = MibTableColumn
tSapIngPolicerSlopeMaxDepth = _TSapIngPolicerSlopeMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 21),
    _TSapIngPolicerSlopeMaxDepth_Type()
)
tSapIngPolicerSlopeMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeMaxDepth.setUnits("hundredths of a percent")


class _TSapIngPolicerSlopeMaxProb_Type(Unsigned32):
    """Custom type tSapIngPolicerSlopeMaxProb based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapIngPolicerSlopeMaxProb_Type.__name__ = "Unsigned32"
_TSapIngPolicerSlopeMaxProb_Object = MibTableColumn
tSapIngPolicerSlopeMaxProb = _TSapIngPolicerSlopeMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 22),
    _TSapIngPolicerSlopeMaxProb_Type()
)
tSapIngPolicerSlopeMaxProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeMaxProb.setStatus("current")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeMaxProb.setUnits("hundredths of a percent")


class _TSapIngPolicerSlopeMap_Type(TmnxSlopeMap):
    """Custom type tSapIngPolicerSlopeMap based on TmnxSlopeMap"""


_TSapIngPolicerSlopeMap_Object = MibTableColumn
tSapIngPolicerSlopeMap = _TSapIngPolicerSlopeMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 23),
    _TSapIngPolicerSlopeMap_Type()
)
tSapIngPolicerSlopeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerSlopeMap.setStatus("current")


class _TSapIngPolicerAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tSapIngPolicerAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapIngPolicerAdvCfgPolicy_Object = MibTableColumn
tSapIngPolicerAdvCfgPolicy = _TSapIngPolicerAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 24),
    _TSapIngPolicerAdvCfgPolicy_Type()
)
tSapIngPolicerAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerAdvCfgPolicy.setStatus("current")


class _TSapIngPolicerProfileCapped_Type(TruthValue):
    """Custom type tSapIngPolicerProfileCapped based on TruthValue"""


_TSapIngPolicerProfileCapped_Object = MibTableColumn
tSapIngPolicerProfileCapped = _TSapIngPolicerProfileCapped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 12, 1, 25),
    _TSapIngPolicerProfileCapped_Type()
)
tSapIngPolicerProfileCapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngPolicerProfileCapped.setStatus("current")
_TSapIngPolicyNameTable_Object = MibTable
tSapIngPolicyNameTable = _TSapIngPolicyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 13)
)
if mibBuilder.loadTexts:
    tSapIngPolicyNameTable.setStatus("current")
_TSapIngPolicyNameEntry_Object = MibTableRow
tSapIngPolicyNameEntry = _TSapIngPolicyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 13, 1)
)
tSapIngPolicyNameEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapIngressPolicyName"),
)
if mibBuilder.loadTexts:
    tSapIngPolicyNameEntry.setStatus("current")
_TSapIngPolicyNameId_Type = TSapIngressPolicyID
_TSapIngPolicyNameId_Object = MibTableColumn
tSapIngPolicyNameId = _TSapIngPolicyNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 13, 1, 1),
    _TSapIngPolicyNameId_Type()
)
tSapIngPolicyNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicyNameId.setStatus("current")
_TSapIngPolicyNameRowStatus_Type = RowStatus
_TSapIngPolicyNameRowStatus_Object = MibTableColumn
tSapIngPolicyNameRowStatus = _TSapIngPolicyNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 13, 1, 2),
    _TSapIngPolicyNameRowStatus_Type()
)
tSapIngPolicyNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicyNameRowStatus.setStatus("current")
_TSapIngPolicyNameLastChanged_Type = TimeStamp
_TSapIngPolicyNameLastChanged_Object = MibTableColumn
tSapIngPolicyNameLastChanged = _TSapIngPolicyNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 13, 1, 3),
    _TSapIngPolicyNameLastChanged_Type()
)
tSapIngPolicyNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicyNameLastChanged.setStatus("current")
_TSapEgressObjects_ObjectIdentity = ObjectIdentity
tSapEgressObjects = _TSapEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4)
)
_TSapEgressTable_Object = MibTable
tSapEgressTable = _TSapEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    tSapEgressTable.setStatus("current")
_TSapEgressEntry_Object = MibTableRow
tSapEgressEntry = _TSapEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1)
)
tSapEgressEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
)
if mibBuilder.loadTexts:
    tSapEgressEntry.setStatus("current")
_TSapEgressIndex_Type = TSapEgressPolicyID
_TSapEgressIndex_Object = MibTableColumn
tSapEgressIndex = _TSapEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 1),
    _TSapEgressIndex_Type()
)
tSapEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressIndex.setStatus("current")
_TSapEgressRowStatus_Type = RowStatus
_TSapEgressRowStatus_Object = MibTableColumn
tSapEgressRowStatus = _TSapEgressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 2),
    _TSapEgressRowStatus_Type()
)
tSapEgressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressRowStatus.setStatus("current")


class _TSapEgressScope_Type(TItemScope):
    """Custom type tSapEgressScope based on TItemScope"""


_TSapEgressScope_Object = MibTableColumn
tSapEgressScope = _TSapEgressScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 3),
    _TSapEgressScope_Type()
)
tSapEgressScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressScope.setStatus("current")


class _TSapEgressDescription_Type(TItemDescription):
    """Custom type tSapEgressDescription based on TItemDescription"""
    defaultHexValue = ""


_TSapEgressDescription_Object = MibTableColumn
tSapEgressDescription = _TSapEgressDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 4),
    _TSapEgressDescription_Type()
)
tSapEgressDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDescription.setStatus("current")
_TSapEgressLastChanged_Type = TimeStamp
_TSapEgressLastChanged_Object = MibTableColumn
tSapEgressLastChanged = _TSapEgressLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 5),
    _TSapEgressLastChanged_Type()
)
tSapEgressLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressLastChanged.setStatus("current")


class _TSapEgressHsmdaPacketOffset_Type(TEgressHsmdaPerPacketOffset):
    """Custom type tSapEgressHsmdaPacketOffset based on TEgressHsmdaPerPacketOffset"""
    defaultValue = 0


_TSapEgressHsmdaPacketOffset_Object = MibTableColumn
tSapEgressHsmdaPacketOffset = _TSapEgressHsmdaPacketOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 6),
    _TSapEgressHsmdaPacketOffset_Type()
)
tSapEgressHsmdaPacketOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaPacketOffset.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressHsmdaPacketOffset.setUnits("bytes")
_TSapEgressMatchCriteria_Type = TMatchCriteria
_TSapEgressMatchCriteria_Object = MibTableColumn
tSapEgressMatchCriteria = _TSapEgressMatchCriteria_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 7),
    _TSapEgressMatchCriteria_Type()
)
tSapEgressMatchCriteria.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressMatchCriteria.setStatus("current")
_TSapEgressHsmdaWrrPolicy_Type = TNamedItemOrEmpty
_TSapEgressHsmdaWrrPolicy_Object = MibTableColumn
tSapEgressHsmdaWrrPolicy = _TSapEgressHsmdaWrrPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 8),
    _TSapEgressHsmdaWrrPolicy_Type()
)
tSapEgressHsmdaWrrPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaWrrPolicy.setStatus("current")


class _TSapEgressHsmdaLowBrstMaxCls_Type(Unsigned32):
    """Custom type tSapEgressHsmdaLowBrstMaxCls based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSapEgressHsmdaLowBrstMaxCls_Type.__name__ = "Unsigned32"
_TSapEgressHsmdaLowBrstMaxCls_Object = MibTableColumn
tSapEgressHsmdaLowBrstMaxCls = _TSapEgressHsmdaLowBrstMaxCls_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 9),
    _TSapEgressHsmdaLowBrstMaxCls_Type()
)
tSapEgressHsmdaLowBrstMaxCls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaLowBrstMaxCls.setStatus("current")


class _TSapEgressPolicyName_Type(TLNamedItemOrEmpty):
    """Custom type tSapEgressPolicyName based on TLNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressPolicyName_Object = MibTableColumn
tSapEgressPolicyName = _TSapEgressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 10),
    _TSapEgressPolicyName_Type()
)
tSapEgressPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressPolicyName.setStatus("current")


class _TSapEgressEthernetCtag_Type(TruthValue):
    """Custom type tSapEgressEthernetCtag based on TruthValue"""


_TSapEgressEthernetCtag_Object = MibTableColumn
tSapEgressEthernetCtag = _TSapEgressEthernetCtag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 1, 1, 11),
    _TSapEgressEthernetCtag_Type()
)
tSapEgressEthernetCtag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressEthernetCtag.setStatus("current")
_TSapEgressQueueTable_Object = MibTable
tSapEgressQueueTable = _TSapEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2)
)
if mibBuilder.loadTexts:
    tSapEgressQueueTable.setStatus("current")
_TSapEgressQueueEntry_Object = MibTableRow
tSapEgressQueueEntry = _TSapEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1)
)
tSapEgressQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressQueueIndex"),
)
if mibBuilder.loadTexts:
    tSapEgressQueueEntry.setStatus("current")


class _TSapEgressQueueIndex_Type(TEgressQueueId):
    """Custom type tSapEgressQueueIndex based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSapEgressQueueIndex_Type.__name__ = "TEgressQueueId"
_TSapEgressQueueIndex_Object = MibTableColumn
tSapEgressQueueIndex = _TSapEgressQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 1),
    _TSapEgressQueueIndex_Type()
)
tSapEgressQueueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressQueueIndex.setStatus("current")
_TSapEgressQueueRowStatus_Type = RowStatus
_TSapEgressQueueRowStatus_Object = MibTableColumn
tSapEgressQueueRowStatus = _TSapEgressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 2),
    _TSapEgressQueueRowStatus_Type()
)
tSapEgressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueRowStatus.setStatus("current")


class _TSapEgressQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressQueueParent_Object = MibTableColumn
tSapEgressQueueParent = _TSapEgressQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 3),
    _TSapEgressQueueParent_Type()
)
tSapEgressQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueParent.setStatus("current")


class _TSapEgressQueueLevel_Type(TLevel):
    """Custom type tSapEgressQueueLevel based on TLevel"""
    defaultValue = 1


_TSapEgressQueueLevel_Object = MibTableColumn
tSapEgressQueueLevel = _TSapEgressQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 4),
    _TSapEgressQueueLevel_Type()
)
tSapEgressQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueLevel.setStatus("current")


class _TSapEgressQueueWeight_Type(TWeight):
    """Custom type tSapEgressQueueWeight based on TWeight"""
    defaultValue = 1


_TSapEgressQueueWeight_Object = MibTableColumn
tSapEgressQueueWeight = _TSapEgressQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 5),
    _TSapEgressQueueWeight_Type()
)
tSapEgressQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueWeight.setStatus("current")


class _TSapEgressQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tSapEgressQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TSapEgressQueueCIRLevel_Object = MibTableColumn
tSapEgressQueueCIRLevel = _TSapEgressQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 6),
    _TSapEgressQueueCIRLevel_Type()
)
tSapEgressQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueCIRLevel.setStatus("current")


class _TSapEgressQueueCIRWeight_Type(TWeight):
    """Custom type tSapEgressQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TSapEgressQueueCIRWeight_Object = MibTableColumn
tSapEgressQueueCIRWeight = _TSapEgressQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 7),
    _TSapEgressQueueCIRWeight_Type()
)
tSapEgressQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueCIRWeight.setStatus("current")


class _TSapEgressQueueExpedite_Type(Integer32):
    """Custom type tSapEgressQueueExpedite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-expedited", 2),
          ("expedited", 1),
          ("non-expedited", 3))
    )


_TSapEgressQueueExpedite_Type.__name__ = "Integer32"
_TSapEgressQueueExpedite_Object = MibTableColumn
tSapEgressQueueExpedite = _TSapEgressQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 8),
    _TSapEgressQueueExpedite_Type()
)
tSapEgressQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueExpedite.setStatus("current")


class _TSapEgressQueueCBS_Type(TBurstSize):
    """Custom type tSapEgressQueueCBS based on TBurstSize"""
    defaultValue = -1


_TSapEgressQueueCBS_Object = MibTableColumn
tSapEgressQueueCBS = _TSapEgressQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 9),
    _TSapEgressQueueCBS_Type()
)
tSapEgressQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueCBS.setStatus("current")


class _TSapEgressQueueMBS_Type(TBurstSize):
    """Custom type tSapEgressQueueMBS based on TBurstSize"""
    defaultValue = -1


_TSapEgressQueueMBS_Object = MibTableColumn
tSapEgressQueueMBS = _TSapEgressQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 10),
    _TSapEgressQueueMBS_Type()
)
tSapEgressQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueMBS.setStatus("obsolete")


class _TSapEgressQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tSapEgressQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TSapEgressQueueHiPrioOnly_Object = MibTableColumn
tSapEgressQueueHiPrioOnly = _TSapEgressQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 11),
    _TSapEgressQueueHiPrioOnly_Type()
)
tSapEgressQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueHiPrioOnly.setStatus("current")


class _TSapEgressQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapEgressQueuePIRAdaptation based on TAdaptationRule"""


_TSapEgressQueuePIRAdaptation_Object = MibTableColumn
tSapEgressQueuePIRAdaptation = _TSapEgressQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 12),
    _TSapEgressQueuePIRAdaptation_Type()
)
tSapEgressQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePIRAdaptation.setStatus("current")


class _TSapEgressQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapEgressQueueCIRAdaptation based on TAdaptationRule"""


_TSapEgressQueueCIRAdaptation_Object = MibTableColumn
tSapEgressQueueCIRAdaptation = _TSapEgressQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 13),
    _TSapEgressQueueCIRAdaptation_Type()
)
tSapEgressQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueCIRAdaptation.setStatus("current")


class _TSapEgressQueueAdminPIR_Type(TPIRRate):
    """Custom type tSapEgressQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TSapEgressQueueAdminPIR_Object = MibTableColumn
tSapEgressQueueAdminPIR = _TSapEgressQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 14),
    _TSapEgressQueueAdminPIR_Type()
)
tSapEgressQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminPIR.setUnits("kbps")


class _TSapEgressQueueAdminCIR_Type(TCIRRate):
    """Custom type tSapEgressQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TSapEgressQueueAdminCIR_Object = MibTableColumn
tSapEgressQueueAdminCIR = _TSapEgressQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 15),
    _TSapEgressQueueAdminCIR_Type()
)
tSapEgressQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminCIR.setUnits("kbps")
_TSapEgressQueueOperPIR_Type = TPIRRate
_TSapEgressQueueOperPIR_Object = MibTableColumn
tSapEgressQueueOperPIR = _TSapEgressQueueOperPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 16),
    _TSapEgressQueueOperPIR_Type()
)
tSapEgressQueueOperPIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressQueueOperPIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapEgressQueueOperPIR.setUnits("kbps")
_TSapEgressQueueOperCIR_Type = TCIRRate
_TSapEgressQueueOperCIR_Object = MibTableColumn
tSapEgressQueueOperCIR = _TSapEgressQueueOperCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 17),
    _TSapEgressQueueOperCIR_Type()
)
tSapEgressQueueOperCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressQueueOperCIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapEgressQueueOperCIR.setUnits("kbps")
_TSapEgressQueueLastChanged_Type = TimeStamp
_TSapEgressQueueLastChanged_Object = MibTableColumn
tSapEgressQueueLastChanged = _TSapEgressQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 18),
    _TSapEgressQueueLastChanged_Type()
)
tSapEgressQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressQueueLastChanged.setStatus("current")


class _TSapEgressQueueUsePortParent_Type(TruthValue):
    """Custom type tSapEgressQueueUsePortParent based on TruthValue"""


_TSapEgressQueueUsePortParent_Object = MibTableColumn
tSapEgressQueueUsePortParent = _TSapEgressQueueUsePortParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 19),
    _TSapEgressQueueUsePortParent_Type()
)
tSapEgressQueueUsePortParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueUsePortParent.setStatus("current")


class _TSapEgressQueuePortLvl_Type(TLevel):
    """Custom type tSapEgressQueuePortLvl based on TLevel"""
    defaultValue = 1


_TSapEgressQueuePortLvl_Object = MibTableColumn
tSapEgressQueuePortLvl = _TSapEgressQueuePortLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 20),
    _TSapEgressQueuePortLvl_Type()
)
tSapEgressQueuePortLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePortLvl.setStatus("current")


class _TSapEgressQueuePortWght_Type(TWeight):
    """Custom type tSapEgressQueuePortWght based on TWeight"""
    defaultValue = 1


_TSapEgressQueuePortWght_Object = MibTableColumn
tSapEgressQueuePortWght = _TSapEgressQueuePortWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 21),
    _TSapEgressQueuePortWght_Type()
)
tSapEgressQueuePortWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePortWght.setStatus("current")


class _TSapEgressQueuePortCIRLvl_Type(TLevelOrDefault):
    """Custom type tSapEgressQueuePortCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TSapEgressQueuePortCIRLvl_Object = MibTableColumn
tSapEgressQueuePortCIRLvl = _TSapEgressQueuePortCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 22),
    _TSapEgressQueuePortCIRLvl_Type()
)
tSapEgressQueuePortCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePortCIRLvl.setStatus("current")


class _TSapEgressQueuePortCIRWght_Type(TWeight):
    """Custom type tSapEgressQueuePortCIRWght based on TWeight"""
    defaultValue = 0


_TSapEgressQueuePortCIRWght_Object = MibTableColumn
tSapEgressQueuePortCIRWght = _TSapEgressQueuePortCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 23),
    _TSapEgressQueuePortCIRWght_Type()
)
tSapEgressQueuePortCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePortCIRWght.setStatus("current")


class _TSapEgressQueuePortAvgOverhead_Type(Unsigned32):
    """Custom type tSapEgressQueuePortAvgOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TSapEgressQueuePortAvgOverhead_Type.__name__ = "Unsigned32"
_TSapEgressQueuePortAvgOverhead_Object = MibTableColumn
tSapEgressQueuePortAvgOverhead = _TSapEgressQueuePortAvgOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 24),
    _TSapEgressQueuePortAvgOverhead_Type()
)
tSapEgressQueuePortAvgOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePortAvgOverhead.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueuePortAvgOverhead.setUnits("Hundredths of a percent")


class _TSapEgressQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressQueuePoolName_Object = MibTableColumn
tSapEgressQueuePoolName = _TSapEgressQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 25),
    _TSapEgressQueuePoolName_Type()
)
tSapEgressQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePoolName.setStatus("current")


class _TSapEgressQueueXPWredQ_Type(TruthValue):
    """Custom type tSapEgressQueueXPWredQ based on TruthValue"""


_TSapEgressQueueXPWredQ_Object = MibTableColumn
tSapEgressQueueXPWredQ = _TSapEgressQueueXPWredQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 26),
    _TSapEgressQueueXPWredQ_Type()
)
tSapEgressQueueXPWredQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueXPWredQ.setStatus("current")


class _TSapEgressQueueXPWredQSlope_Type(TNamedItem):
    """Custom type tSapEgressQueueXPWredQSlope based on TNamedItem"""
    defaultValue = OctetString("default")


_TSapEgressQueueXPWredQSlope_Object = MibTableColumn
tSapEgressQueueXPWredQSlope = _TSapEgressQueueXPWredQSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 27),
    _TSapEgressQueueXPWredQSlope_Type()
)
tSapEgressQueueXPWredQSlope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueXPWredQSlope.setStatus("current")


class _TSapEgressQueueMBSBytes_Type(TBurstSizeBytes):
    """Custom type tSapEgressQueueMBSBytes based on TBurstSizeBytes"""
    defaultValue = -1


_TSapEgressQueueMBSBytes_Object = MibTableColumn
tSapEgressQueueMBSBytes = _TSapEgressQueueMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 28),
    _TSapEgressQueueMBSBytes_Type()
)
tSapEgressQueueMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueMBSBytes.setUnits("bytes")


class _TSapEgressQueueBurstLimit_Type(TBurstLimit):
    """Custom type tSapEgressQueueBurstLimit based on TBurstLimit"""
    defaultValue = -1


_TSapEgressQueueBurstLimit_Object = MibTableColumn
tSapEgressQueueBurstLimit = _TSapEgressQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 29),
    _TSapEgressQueueBurstLimit_Type()
)
tSapEgressQueueBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueBurstLimit.setUnits("bytes")


class _TSapEgressQueuePktOffset_Type(TEgressQPerPacketOffset):
    """Custom type tSapEgressQueuePktOffset based on TEgressQPerPacketOffset"""
    defaultValue = 0


_TSapEgressQueuePktOffset_Object = MibTableColumn
tSapEgressQueuePktOffset = _TSapEgressQueuePktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 30),
    _TSapEgressQueuePktOffset_Type()
)
tSapEgressQueuePktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueuePktOffset.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueuePktOffset.setUnits("bytes")


class _TSapEgressQueueAdminPIRPercent_Type(Unsigned32):
    """Custom type tSapEgressQueueAdminPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapEgressQueueAdminPIRPercent_Type.__name__ = "Unsigned32"
_TSapEgressQueueAdminPIRPercent_Object = MibTableColumn
tSapEgressQueueAdminPIRPercent = _TSapEgressQueueAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 31),
    _TSapEgressQueueAdminPIRPercent_Type()
)
tSapEgressQueueAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminPIRPercent.setUnits("hundredths of a percent")


class _TSapEgressQueueAdminCIRPercent_Type(Unsigned32):
    """Custom type tSapEgressQueueAdminCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TSapEgressQueueAdminCIRPercent_Type.__name__ = "Unsigned32"
_TSapEgressQueueAdminCIRPercent_Object = MibTableColumn
tSapEgressQueueAdminCIRPercent = _TSapEgressQueueAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 32),
    _TSapEgressQueueAdminCIRPercent_Type()
)
tSapEgressQueueAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressQueueAdminCIRPercent.setUnits("hundredths of a percent")


class _TSapEgressQueueRateType_Type(TBWRateType):
    """Custom type tSapEgressQueueRateType based on TBWRateType"""


_TSapEgressQueueRateType_Object = MibTableColumn
tSapEgressQueueRateType = _TSapEgressQueueRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 33),
    _TSapEgressQueueRateType_Type()
)
tSapEgressQueueRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueRateType.setStatus("current")


class _TSapEgressQueueAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressQueueAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressQueueAdvCfgPolicy_Object = MibTableColumn
tSapEgressQueueAdvCfgPolicy = _TSapEgressQueueAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 2, 1, 34),
    _TSapEgressQueueAdvCfgPolicy_Type()
)
tSapEgressQueueAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressQueueAdvCfgPolicy.setStatus("current")
_TSapEgressFCTable_Object = MibTable
tSapEgressFCTable = _TSapEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3)
)
if mibBuilder.loadTexts:
    tSapEgressFCTable.setStatus("current")
_TSapEgressFCEntry_Object = MibTableRow
tSapEgressFCEntry = _TSapEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1)
)
tSapEgressFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressFCName"),
)
if mibBuilder.loadTexts:
    tSapEgressFCEntry.setStatus("current")
_TSapEgressFCName_Type = TFCName
_TSapEgressFCName_Object = MibTableColumn
tSapEgressFCName = _TSapEgressFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 1),
    _TSapEgressFCName_Type()
)
tSapEgressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressFCName.setStatus("current")
_TSapEgressFCRowStatus_Type = RowStatus
_TSapEgressFCRowStatus_Object = MibTableColumn
tSapEgressFCRowStatus = _TSapEgressFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 2),
    _TSapEgressFCRowStatus_Type()
)
tSapEgressFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCRowStatus.setStatus("current")


class _TSapEgressFCQueue_Type(TEgressQueueId):
    """Custom type tSapEgressFCQueue based on TEgressQueueId"""
    defaultValue = 0


_TSapEgressFCQueue_Object = MibTableColumn
tSapEgressFCQueue = _TSapEgressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 3),
    _TSapEgressFCQueue_Type()
)
tSapEgressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCQueue.setStatus("current")


class _TSapEgressFCDot1PValue_Type(Dot1PPriority):
    """Custom type tSapEgressFCDot1PValue based on Dot1PPriority"""
    defaultValue = -1


_TSapEgressFCDot1PValue_Object = MibTableColumn
tSapEgressFCDot1PValue = _TSapEgressFCDot1PValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 4),
    _TSapEgressFCDot1PValue_Type()
)
tSapEgressFCDot1PValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCDot1PValue.setStatus("obsolete")
_TSapEgressFCLastChanged_Type = TimeStamp
_TSapEgressFCLastChanged_Object = MibTableColumn
tSapEgressFCLastChanged = _TSapEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 5),
    _TSapEgressFCLastChanged_Type()
)
tSapEgressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressFCLastChanged.setStatus("current")


class _TSapEgressFCHsmdaQueue_Type(TEgressHsmdaQueueId):
    """Custom type tSapEgressFCHsmdaQueue based on TEgressHsmdaQueueId"""
    defaultValue = 0


_TSapEgressFCHsmdaQueue_Object = MibTableColumn
tSapEgressFCHsmdaQueue = _TSapEgressFCHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 6),
    _TSapEgressFCHsmdaQueue_Type()
)
tSapEgressFCHsmdaQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCHsmdaQueue.setStatus("current")


class _TSapEgressFCDot1PHsmdaProfile_Type(TruthValue):
    """Custom type tSapEgressFCDot1PHsmdaProfile based on TruthValue"""


_TSapEgressFCDot1PHsmdaProfile_Object = MibTableColumn
tSapEgressFCDot1PHsmdaProfile = _TSapEgressFCDot1PHsmdaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 7),
    _TSapEgressFCDot1PHsmdaProfile_Type()
)
tSapEgressFCDot1PHsmdaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCDot1PHsmdaProfile.setStatus("obsolete")


class _TSapEgressFCDot1PInProfile_Type(Dot1PPriority):
    """Custom type tSapEgressFCDot1PInProfile based on Dot1PPriority"""
    defaultValue = -1


_TSapEgressFCDot1PInProfile_Object = MibTableColumn
tSapEgressFCDot1PInProfile = _TSapEgressFCDot1PInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 8),
    _TSapEgressFCDot1PInProfile_Type()
)
tSapEgressFCDot1PInProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCDot1PInProfile.setStatus("current")


class _TSapEgressFCDot1POutProfile_Type(Dot1PPriority):
    """Custom type tSapEgressFCDot1POutProfile based on Dot1PPriority"""
    defaultValue = -1


_TSapEgressFCDot1POutProfile_Object = MibTableColumn
tSapEgressFCDot1POutProfile = _TSapEgressFCDot1POutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 9),
    _TSapEgressFCDot1POutProfile_Type()
)
tSapEgressFCDot1POutProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCDot1POutProfile.setStatus("current")


class _TSapEgressFCForceDEValue_Type(TDEValue):
    """Custom type tSapEgressFCForceDEValue based on TDEValue"""
    defaultValue = -1


_TSapEgressFCForceDEValue_Object = MibTableColumn
tSapEgressFCForceDEValue = _TSapEgressFCForceDEValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 10),
    _TSapEgressFCForceDEValue_Type()
)
tSapEgressFCForceDEValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCForceDEValue.setStatus("current")


class _TSapEgressFCDEMark_Type(TruthValue):
    """Custom type tSapEgressFCDEMark based on TruthValue"""


_TSapEgressFCDEMark_Object = MibTableColumn
tSapEgressFCDEMark = _TSapEgressFCDEMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 11),
    _TSapEgressFCDEMark_Type()
)
tSapEgressFCDEMark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCDEMark.setStatus("current")


class _TSapEgressFCInProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressFCInProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressFCInProfDscp_Object = MibTableColumn
tSapEgressFCInProfDscp = _TSapEgressFCInProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 12),
    _TSapEgressFCInProfDscp_Type()
)
tSapEgressFCInProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCInProfDscp.setStatus("current")


class _TSapEgressFCOutProfDscp_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressFCOutProfDscp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressFCOutProfDscp_Object = MibTableColumn
tSapEgressFCOutProfDscp = _TSapEgressFCOutProfDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 13),
    _TSapEgressFCOutProfDscp_Type()
)
tSapEgressFCOutProfDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCOutProfDscp.setStatus("current")


class _TSapEgressFCInProfPrec_Type(TPrecValueOrNone):
    """Custom type tSapEgressFCInProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TSapEgressFCInProfPrec_Object = MibTableColumn
tSapEgressFCInProfPrec = _TSapEgressFCInProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 14),
    _TSapEgressFCInProfPrec_Type()
)
tSapEgressFCInProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCInProfPrec.setStatus("current")


class _TSapEgressFCOutProfPrec_Type(TPrecValueOrNone):
    """Custom type tSapEgressFCOutProfPrec based on TPrecValueOrNone"""
    defaultValue = -1


_TSapEgressFCOutProfPrec_Object = MibTableColumn
tSapEgressFCOutProfPrec = _TSapEgressFCOutProfPrec_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 15),
    _TSapEgressFCOutProfPrec_Type()
)
tSapEgressFCOutProfPrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCOutProfPrec.setStatus("current")


class _TSapEgressFCQGrp_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressFCQGrp based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressFCQGrp_Object = MibTableColumn
tSapEgressFCQGrp = _TSapEgressFCQGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 16),
    _TSapEgressFCQGrp_Type()
)
tSapEgressFCQGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCQGrp.setStatus("current")


class _TSapEgressFCPolicer_Type(TEgrPolicerIdOrNone):
    """Custom type tSapEgressFCPolicer based on TEgrPolicerIdOrNone"""
    defaultValue = 0


_TSapEgressFCPolicer_Object = MibTableColumn
tSapEgressFCPolicer = _TSapEgressFCPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 17),
    _TSapEgressFCPolicer_Type()
)
tSapEgressFCPolicer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCPolicer.setStatus("current")


class _TSapEgressFCQGrpFC_Type(TFCNameOrEmpty):
    """Custom type tSapEgressFCQGrpFC based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TSapEgressFCQGrpFC_Object = MibTableColumn
tSapEgressFCQGrpFC = _TSapEgressFCQGrpFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 3, 1, 18),
    _TSapEgressFCQGrpFC_Type()
)
tSapEgressFCQGrpFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressFCQGrpFC.setStatus("current")
_TSapEgressHsmdaQueueTable_Object = MibTable
tSapEgressHsmdaQueueTable = _TSapEgressHsmdaQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4)
)
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueTable.setStatus("current")
_TSapEgressHsmdaQueueEntry_Object = MibTableRow
tSapEgressHsmdaQueueEntry = _TSapEgressHsmdaQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1)
)
tSapEgressHsmdaQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressHsmdaQueue"),
)
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueEntry.setStatus("current")


class _TSapEgressHsmdaQueue_Type(TEgressHsmdaQueueId):
    """Custom type tSapEgressHsmdaQueue based on TEgressHsmdaQueueId"""
    subtypeSpec = TEgressHsmdaQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSapEgressHsmdaQueue_Type.__name__ = "TEgressHsmdaQueueId"
_TSapEgressHsmdaQueue_Object = MibTableColumn
tSapEgressHsmdaQueue = _TSapEgressHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 1),
    _TSapEgressHsmdaQueue_Type()
)
tSapEgressHsmdaQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueue.setStatus("current")
_TSapEgressHsmdaQueueRowStatus_Type = RowStatus
_TSapEgressHsmdaQueueRowStatus_Object = MibTableColumn
tSapEgressHsmdaQueueRowStatus = _TSapEgressHsmdaQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 2),
    _TSapEgressHsmdaQueueRowStatus_Type()
)
tSapEgressHsmdaQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueRowStatus.setStatus("current")


class _TSapEgressHsmdaQueueCIRAdaptn_Type(TAdaptationRule):
    """Custom type tSapEgressHsmdaQueueCIRAdaptn based on TAdaptationRule"""


_TSapEgressHsmdaQueueCIRAdaptn_Object = MibTableColumn
tSapEgressHsmdaQueueCIRAdaptn = _TSapEgressHsmdaQueueCIRAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 3),
    _TSapEgressHsmdaQueueCIRAdaptn_Type()
)
tSapEgressHsmdaQueueCIRAdaptn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueCIRAdaptn.setStatus("obsolete")


class _TSapEgressHsmdaQueuePIRAdaptn_Type(TAdaptationRule):
    """Custom type tSapEgressHsmdaQueuePIRAdaptn based on TAdaptationRule"""


_TSapEgressHsmdaQueuePIRAdaptn_Object = MibTableColumn
tSapEgressHsmdaQueuePIRAdaptn = _TSapEgressHsmdaQueuePIRAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 4),
    _TSapEgressHsmdaQueuePIRAdaptn_Type()
)
tSapEgressHsmdaQueuePIRAdaptn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueuePIRAdaptn.setStatus("current")


class _TSapEgressHsmdaQueueAdminPIR_Type(THsmdaPIRKRate):
    """Custom type tSapEgressHsmdaQueueAdminPIR based on THsmdaPIRKRate"""
    defaultValue = -1


_TSapEgressHsmdaQueueAdminPIR_Object = MibTableColumn
tSapEgressHsmdaQueueAdminPIR = _TSapEgressHsmdaQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 5),
    _TSapEgressHsmdaQueueAdminPIR_Type()
)
tSapEgressHsmdaQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueAdminPIR.setUnits("kbps")


class _TSapEgressHsmdaQueueAdminCIR_Type(THsmdaCIRKRate):
    """Custom type tSapEgressHsmdaQueueAdminCIR based on THsmdaCIRKRate"""
    defaultValue = 0


_TSapEgressHsmdaQueueAdminCIR_Object = MibTableColumn
tSapEgressHsmdaQueueAdminCIR = _TSapEgressHsmdaQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 6),
    _TSapEgressHsmdaQueueAdminCIR_Type()
)
tSapEgressHsmdaQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueAdminCIR.setStatus("obsolete")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueAdminCIR.setUnits("kbps")


class _TSapEgressHsmdaQueueSlopePolicy_Type(TNamedItem):
    """Custom type tSapEgressHsmdaQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TSapEgressHsmdaQueueSlopePolicy_Object = MibTableColumn
tSapEgressHsmdaQueueSlopePolicy = _TSapEgressHsmdaQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 7),
    _TSapEgressHsmdaQueueSlopePolicy_Type()
)
tSapEgressHsmdaQueueSlopePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueSlopePolicy.setStatus("current")
_TSapEgressHsmdaQueueLastChanged_Type = TimeStamp
_TSapEgressHsmdaQueueLastChanged_Object = MibTableColumn
tSapEgressHsmdaQueueLastChanged = _TSapEgressHsmdaQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 8),
    _TSapEgressHsmdaQueueLastChanged_Type()
)
tSapEgressHsmdaQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueLastChanged.setStatus("current")


class _TSapEgressHsmdaQueueWrrWeight_Type(THsmdaWrrWeight):
    """Custom type tSapEgressHsmdaQueueWrrWeight based on THsmdaWrrWeight"""
    defaultValue = 1


_TSapEgressHsmdaQueueWrrWeight_Object = MibTableColumn
tSapEgressHsmdaQueueWrrWeight = _TSapEgressHsmdaQueueWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 9),
    _TSapEgressHsmdaQueueWrrWeight_Type()
)
tSapEgressHsmdaQueueWrrWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueWrrWeight.setStatus("current")


class _TSapEgressHsmdaQueueMBS_Type(THSMDABurstSizeBytes):
    """Custom type tSapEgressHsmdaQueueMBS based on THSMDABurstSizeBytes"""
    defaultValue = -1


_TSapEgressHsmdaQueueMBS_Object = MibTableColumn
tSapEgressHsmdaQueueMBS = _TSapEgressHsmdaQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 10),
    _TSapEgressHsmdaQueueMBS_Type()
)
tSapEgressHsmdaQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueMBS.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueMBS.setUnits("bytes")


class _TSapEgressHsmdaQueueBurstLimit_Type(THSMDAQueueBurstLimit):
    """Custom type tSapEgressHsmdaQueueBurstLimit based on THSMDAQueueBurstLimit"""
    defaultValue = -1


_TSapEgressHsmdaQueueBurstLimit_Object = MibTableColumn
tSapEgressHsmdaQueueBurstLimit = _TSapEgressHsmdaQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 4, 1, 11),
    _TSapEgressHsmdaQueueBurstLimit_Type()
)
tSapEgressHsmdaQueueBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgressHsmdaQueueBurstLimit.setUnits("bytes")
_TSapEgressDSCPTable_Object = MibTable
tSapEgressDSCPTable = _TSapEgressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5)
)
if mibBuilder.loadTexts:
    tSapEgressDSCPTable.setStatus("current")
_TSapEgressDSCPEntry_Object = MibTableRow
tSapEgressDSCPEntry = _TSapEgressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1)
)
tSapEgressDSCPEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressDSCP"),
)
if mibBuilder.loadTexts:
    tSapEgressDSCPEntry.setStatus("current")
_TSapEgressDSCP_Type = TDSCPName
_TSapEgressDSCP_Object = MibTableColumn
tSapEgressDSCP = _TSapEgressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 1),
    _TSapEgressDSCP_Type()
)
tSapEgressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressDSCP.setStatus("current")
_TSapEgressDSCPRowStatus_Type = RowStatus
_TSapEgressDSCPRowStatus_Object = MibTableColumn
tSapEgressDSCPRowStatus = _TSapEgressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 2),
    _TSapEgressDSCPRowStatus_Type()
)
tSapEgressDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDSCPRowStatus.setStatus("current")
_TSapEgressDSCPLastChanged_Type = TimeStamp
_TSapEgressDSCPLastChanged_Object = MibTableColumn
tSapEgressDSCPLastChanged = _TSapEgressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 3),
    _TSapEgressDSCPLastChanged_Type()
)
tSapEgressDSCPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressDSCPLastChanged.setStatus("current")


class _TSapEgressDSCPHsmdaCntrOverride_Type(TEgressHsmdaCounterIdOrZero):
    """Custom type tSapEgressDSCPHsmdaCntrOverride based on TEgressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapEgressDSCPHsmdaCntrOverride_Object = MibTableColumn
tSapEgressDSCPHsmdaCntrOverride = _TSapEgressDSCPHsmdaCntrOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 4),
    _TSapEgressDSCPHsmdaCntrOverride_Type()
)
tSapEgressDSCPHsmdaCntrOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDSCPHsmdaCntrOverride.setStatus("current")


class _TSapEgressDSCPfc_Type(TFCNameOrEmpty):
    """Custom type tSapEgressDSCPfc based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TSapEgressDSCPfc_Object = MibTableColumn
tSapEgressDSCPfc = _TSapEgressDSCPfc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 5),
    _TSapEgressDSCPfc_Type()
)
tSapEgressDSCPfc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDSCPfc.setStatus("current")


class _TSapEgressDSCPprofile_Type(TProfileOrNone):
    """Custom type tSapEgressDSCPprofile based on TProfileOrNone"""


_TSapEgressDSCPprofile_Object = MibTableColumn
tSapEgressDSCPprofile = _TSapEgressDSCPprofile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 5, 1, 6),
    _TSapEgressDSCPprofile_Type()
)
tSapEgressDSCPprofile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDSCPprofile.setStatus("current")
_TSapEgressPrecTable_Object = MibTable
tSapEgressPrecTable = _TSapEgressPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6)
)
if mibBuilder.loadTexts:
    tSapEgressPrecTable.setStatus("current")
_TSapEgressPrecEntry_Object = MibTableRow
tSapEgressPrecEntry = _TSapEgressPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1)
)
tSapEgressPrecEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressPrecValue"),
)
if mibBuilder.loadTexts:
    tSapEgressPrecEntry.setStatus("current")
_TSapEgressPrecValue_Type = TPrecValue
_TSapEgressPrecValue_Object = MibTableColumn
tSapEgressPrecValue = _TSapEgressPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 1),
    _TSapEgressPrecValue_Type()
)
tSapEgressPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressPrecValue.setStatus("current")
_TSapEgressPrecRowStatus_Type = RowStatus
_TSapEgressPrecRowStatus_Object = MibTableColumn
tSapEgressPrecRowStatus = _TSapEgressPrecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 2),
    _TSapEgressPrecRowStatus_Type()
)
tSapEgressPrecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressPrecRowStatus.setStatus("current")
_TSapEgressPrecLastChanged_Type = TimeStamp
_TSapEgressPrecLastChanged_Object = MibTableColumn
tSapEgressPrecLastChanged = _TSapEgressPrecLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 3),
    _TSapEgressPrecLastChanged_Type()
)
tSapEgressPrecLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressPrecLastChanged.setStatus("current")


class _TSapEgressPrecHsmdaCntrOverride_Type(TEgressHsmdaCounterIdOrZero):
    """Custom type tSapEgressPrecHsmdaCntrOverride based on TEgressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapEgressPrecHsmdaCntrOverride_Object = MibTableColumn
tSapEgressPrecHsmdaCntrOverride = _TSapEgressPrecHsmdaCntrOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 4),
    _TSapEgressPrecHsmdaCntrOverride_Type()
)
tSapEgressPrecHsmdaCntrOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressPrecHsmdaCntrOverride.setStatus("current")


class _TSapEgressPrecFC_Type(TFCNameOrEmpty):
    """Custom type tSapEgressPrecFC based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TSapEgressPrecFC_Object = MibTableColumn
tSapEgressPrecFC = _TSapEgressPrecFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 5),
    _TSapEgressPrecFC_Type()
)
tSapEgressPrecFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressPrecFC.setStatus("current")


class _TSapEgressPrecProfile_Type(TProfileOrNone):
    """Custom type tSapEgressPrecProfile based on TProfileOrNone"""


_TSapEgressPrecProfile_Object = MibTableColumn
tSapEgressPrecProfile = _TSapEgressPrecProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 6, 1, 6),
    _TSapEgressPrecProfile_Type()
)
tSapEgressPrecProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressPrecProfile.setStatus("current")
_TSapEgrIPCritTable_Object = MibTable
tSapEgrIPCritTable = _TSapEgrIPCritTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7)
)
if mibBuilder.loadTexts:
    tSapEgrIPCritTable.setStatus("current")
_TSapEgrIPCritEntry_Object = MibTableRow
tSapEgrIPCritEntry = _TSapEgrIPCritEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1)
)
tSapEgrIPCritEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgrIPCritAddrType"),
    (0, "TIMETRA-QOS-MIB", "tSapEgrIPCritIndex"),
)
if mibBuilder.loadTexts:
    tSapEgrIPCritEntry.setStatus("current")


class _TSapEgrIPCritAddrType_Type(InetAddressType):
    """Custom type tSapEgrIPCritAddrType based on InetAddressType"""


_TSapEgrIPCritAddrType_Object = MibTableColumn
tSapEgrIPCritAddrType = _TSapEgrIPCritAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 1),
    _TSapEgrIPCritAddrType_Type()
)
tSapEgrIPCritAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgrIPCritAddrType.setStatus("current")
_TSapEgrIPCritIndex_Type = Unsigned32
_TSapEgrIPCritIndex_Object = MibTableColumn
tSapEgrIPCritIndex = _TSapEgrIPCritIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 2),
    _TSapEgrIPCritIndex_Type()
)
tSapEgrIPCritIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgrIPCritIndex.setStatus("current")
_TSapEgrIPCritRowStatus_Type = RowStatus
_TSapEgrIPCritRowStatus_Object = MibTableColumn
tSapEgrIPCritRowStatus = _TSapEgrIPCritRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 3),
    _TSapEgrIPCritRowStatus_Type()
)
tSapEgrIPCritRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritRowStatus.setStatus("current")
_TSapEgrIPCritLastChanged_Type = TimeStamp
_TSapEgrIPCritLastChanged_Object = MibTableColumn
tSapEgrIPCritLastChanged = _TSapEgrIPCritLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 4),
    _TSapEgrIPCritLastChanged_Type()
)
tSapEgrIPCritLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrIPCritLastChanged.setStatus("current")
_TSapEgrIPCritDescription_Type = TItemDescription
_TSapEgrIPCritDescription_Object = MibTableColumn
tSapEgrIPCritDescription = _TSapEgrIPCritDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 5),
    _TSapEgrIPCritDescription_Type()
)
tSapEgrIPCritDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDescription.setStatus("current")


class _TSapEgrIPCritActionHsmdaCntrOvr_Type(TEgressHsmdaCounterIdOrZero):
    """Custom type tSapEgrIPCritActionHsmdaCntrOvr based on TEgressHsmdaCounterIdOrZero"""
    defaultValue = 0


_TSapEgrIPCritActionHsmdaCntrOvr_Object = MibTableColumn
tSapEgrIPCritActionHsmdaCntrOvr = _TSapEgrIPCritActionHsmdaCntrOvr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 6),
    _TSapEgrIPCritActionHsmdaCntrOvr_Type()
)
tSapEgrIPCritActionHsmdaCntrOvr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritActionHsmdaCntrOvr.setStatus("current")


class _TSapEgrIPCritSourceIpAddrType_Type(InetAddressType):
    """Custom type tSapEgrIPCritSourceIpAddrType based on InetAddressType"""


_TSapEgrIPCritSourceIpAddrType_Object = MibTableColumn
tSapEgrIPCritSourceIpAddrType = _TSapEgrIPCritSourceIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 7),
    _TSapEgrIPCritSourceIpAddrType_Type()
)
tSapEgrIPCritSourceIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourceIpAddrType.setStatus("current")


class _TSapEgrIPCritSourceIpAddr_Type(InetAddress):
    """Custom type tSapEgrIPCritSourceIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TSapEgrIPCritSourceIpAddr_Type.__name__ = "InetAddress"
_TSapEgrIPCritSourceIpAddr_Object = MibTableColumn
tSapEgrIPCritSourceIpAddr = _TSapEgrIPCritSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 8),
    _TSapEgrIPCritSourceIpAddr_Type()
)
tSapEgrIPCritSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourceIpAddr.setStatus("current")


class _TSapEgrIPCritSourceIpMask_Type(InetAddressPrefixLength):
    """Custom type tSapEgrIPCritSourceIpMask based on InetAddressPrefixLength"""
    defaultValue = 0


_TSapEgrIPCritSourceIpMask_Object = MibTableColumn
tSapEgrIPCritSourceIpMask = _TSapEgrIPCritSourceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 9),
    _TSapEgrIPCritSourceIpMask_Type()
)
tSapEgrIPCritSourceIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourceIpMask.setStatus("current")


class _TSapEgrIPCritDestIpAddrType_Type(InetAddressType):
    """Custom type tSapEgrIPCritDestIpAddrType based on InetAddressType"""


_TSapEgrIPCritDestIpAddrType_Object = MibTableColumn
tSapEgrIPCritDestIpAddrType = _TSapEgrIPCritDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 10),
    _TSapEgrIPCritDestIpAddrType_Type()
)
tSapEgrIPCritDestIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestIpAddrType.setStatus("current")


class _TSapEgrIPCritDestIpAddr_Type(InetAddress):
    """Custom type tSapEgrIPCritDestIpAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TSapEgrIPCritDestIpAddr_Type.__name__ = "InetAddress"
_TSapEgrIPCritDestIpAddr_Object = MibTableColumn
tSapEgrIPCritDestIpAddr = _TSapEgrIPCritDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 11),
    _TSapEgrIPCritDestIpAddr_Type()
)
tSapEgrIPCritDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestIpAddr.setStatus("current")


class _TSapEgrIPCritDestIpMask_Type(InetAddressPrefixLength):
    """Custom type tSapEgrIPCritDestIpMask based on InetAddressPrefixLength"""
    defaultValue = 0


_TSapEgrIPCritDestIpMask_Object = MibTableColumn
tSapEgrIPCritDestIpMask = _TSapEgrIPCritDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 12),
    _TSapEgrIPCritDestIpMask_Type()
)
tSapEgrIPCritDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestIpMask.setStatus("current")


class _TSapEgrIPCritProtocol_Type(TIpProtocol):
    """Custom type tSapEgrIPCritProtocol based on TIpProtocol"""
    defaultValue = -1


_TSapEgrIPCritProtocol_Object = MibTableColumn
tSapEgrIPCritProtocol = _TSapEgrIPCritProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 13),
    _TSapEgrIPCritProtocol_Type()
)
tSapEgrIPCritProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritProtocol.setStatus("current")


class _TSapEgrIPCritSourcePortValue1_Type(TTcpUdpPort):
    """Custom type tSapEgrIPCritSourcePortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapEgrIPCritSourcePortValue1_Object = MibTableColumn
tSapEgrIPCritSourcePortValue1 = _TSapEgrIPCritSourcePortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 14),
    _TSapEgrIPCritSourcePortValue1_Type()
)
tSapEgrIPCritSourcePortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourcePortValue1.setStatus("current")


class _TSapEgrIPCritSourcePortValue2_Type(TTcpUdpPort):
    """Custom type tSapEgrIPCritSourcePortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapEgrIPCritSourcePortValue2_Object = MibTableColumn
tSapEgrIPCritSourcePortValue2 = _TSapEgrIPCritSourcePortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 15),
    _TSapEgrIPCritSourcePortValue2_Type()
)
tSapEgrIPCritSourcePortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourcePortValue2.setStatus("current")


class _TSapEgrIPCritSourcePortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapEgrIPCritSourcePortOperator based on TTcpUdpPortOperator"""


_TSapEgrIPCritSourcePortOperator_Object = MibTableColumn
tSapEgrIPCritSourcePortOperator = _TSapEgrIPCritSourcePortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 16),
    _TSapEgrIPCritSourcePortOperator_Type()
)
tSapEgrIPCritSourcePortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritSourcePortOperator.setStatus("current")


class _TSapEgrIPCritDestPortValue1_Type(TTcpUdpPort):
    """Custom type tSapEgrIPCritDestPortValue1 based on TTcpUdpPort"""
    defaultValue = 0


_TSapEgrIPCritDestPortValue1_Object = MibTableColumn
tSapEgrIPCritDestPortValue1 = _TSapEgrIPCritDestPortValue1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 17),
    _TSapEgrIPCritDestPortValue1_Type()
)
tSapEgrIPCritDestPortValue1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestPortValue1.setStatus("current")


class _TSapEgrIPCritDestPortValue2_Type(TTcpUdpPort):
    """Custom type tSapEgrIPCritDestPortValue2 based on TTcpUdpPort"""
    defaultValue = 0


_TSapEgrIPCritDestPortValue2_Object = MibTableColumn
tSapEgrIPCritDestPortValue2 = _TSapEgrIPCritDestPortValue2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 18),
    _TSapEgrIPCritDestPortValue2_Type()
)
tSapEgrIPCritDestPortValue2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestPortValue2.setStatus("current")


class _TSapEgrIPCritDestPortOperator_Type(TTcpUdpPortOperator):
    """Custom type tSapEgrIPCritDestPortOperator based on TTcpUdpPortOperator"""


_TSapEgrIPCritDestPortOperator_Object = MibTableColumn
tSapEgrIPCritDestPortOperator = _TSapEgrIPCritDestPortOperator_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 19),
    _TSapEgrIPCritDestPortOperator_Type()
)
tSapEgrIPCritDestPortOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDestPortOperator.setStatus("current")


class _TSapEgrIPCritDSCP_Type(TDSCPNameOrEmpty):
    """Custom type tSapEgrIPCritDSCP based on TDSCPNameOrEmpty"""
    defaultHexValue = ""


_TSapEgrIPCritDSCP_Object = MibTableColumn
tSapEgrIPCritDSCP = _TSapEgrIPCritDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 20),
    _TSapEgrIPCritDSCP_Type()
)
tSapEgrIPCritDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritDSCP.setStatus("current")


class _TSapEgrIPCritFragment_Type(TItemMatch):
    """Custom type tSapEgrIPCritFragment based on TItemMatch"""


_TSapEgrIPCritFragment_Object = MibTableColumn
tSapEgrIPCritFragment = _TSapEgrIPCritFragment_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 21),
    _TSapEgrIPCritFragment_Type()
)
tSapEgrIPCritFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritFragment.setStatus("current")


class _TSapEgrIPCritActionFC_Type(TFCNameOrEmpty):
    """Custom type tSapEgrIPCritActionFC based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TSapEgrIPCritActionFC_Object = MibTableColumn
tSapEgrIPCritActionFC = _TSapEgrIPCritActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 22),
    _TSapEgrIPCritActionFC_Type()
)
tSapEgrIPCritActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritActionFC.setStatus("current")


class _TSapEgrIPCritActionProfile_Type(TProfileOrNone):
    """Custom type tSapEgrIPCritActionProfile based on TProfileOrNone"""


_TSapEgrIPCritActionProfile_Object = MibTableColumn
tSapEgrIPCritActionProfile = _TSapEgrIPCritActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 7, 1, 23),
    _TSapEgrIPCritActionProfile_Type()
)
tSapEgrIPCritActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrIPCritActionProfile.setStatus("current")
_TSapEgrPolicerTable_Object = MibTable
tSapEgrPolicerTable = _TSapEgrPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8)
)
if mibBuilder.loadTexts:
    tSapEgrPolicerTable.setStatus("current")
_TSapEgrPolicerEntry_Object = MibTableRow
tSapEgrPolicerEntry = _TSapEgrPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1)
)
tSapEgrPolicerEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgrPolicerId"),
)
if mibBuilder.loadTexts:
    tSapEgrPolicerEntry.setStatus("current")
_TSapEgrPolicerId_Type = TEgrPolicerId
_TSapEgrPolicerId_Object = MibTableColumn
tSapEgrPolicerId = _TSapEgrPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 1),
    _TSapEgrPolicerId_Type()
)
tSapEgrPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgrPolicerId.setStatus("current")
_TSapEgrPolicerRowStatus_Type = RowStatus
_TSapEgrPolicerRowStatus_Object = MibTableColumn
tSapEgrPolicerRowStatus = _TSapEgrPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 2),
    _TSapEgrPolicerRowStatus_Type()
)
tSapEgrPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerRowStatus.setStatus("current")
_TSapEgrPolicerLastChanged_Type = TimeStamp
_TSapEgrPolicerLastChanged_Object = MibTableColumn
tSapEgrPolicerLastChanged = _TSapEgrPolicerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 3),
    _TSapEgrPolicerLastChanged_Type()
)
tSapEgrPolicerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicerLastChanged.setStatus("current")


class _TSapEgrPolicerDescr_Type(TItemDescription):
    """Custom type tSapEgrPolicerDescr based on TItemDescription"""
    defaultHexValue = ""


_TSapEgrPolicerDescr_Object = MibTableColumn
tSapEgrPolicerDescr = _TSapEgrPolicerDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 4),
    _TSapEgrPolicerDescr_Type()
)
tSapEgrPolicerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerDescr.setStatus("current")


class _TSapEgrPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapEgrPolicerPIRAdaptation based on TAdaptationRule"""


_TSapEgrPolicerPIRAdaptation_Object = MibTableColumn
tSapEgrPolicerPIRAdaptation = _TSapEgrPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 5),
    _TSapEgrPolicerPIRAdaptation_Type()
)
tSapEgrPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerPIRAdaptation.setStatus("current")


class _TSapEgrPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tSapEgrPolicerCIRAdaptation based on TAdaptationRule"""


_TSapEgrPolicerCIRAdaptation_Object = MibTableColumn
tSapEgrPolicerCIRAdaptation = _TSapEgrPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 6),
    _TSapEgrPolicerCIRAdaptation_Type()
)
tSapEgrPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerCIRAdaptation.setStatus("current")


class _TSapEgrPolicerParent_Type(TNamedItemOrEmpty):
    """Custom type tSapEgrPolicerParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgrPolicerParent_Object = MibTableColumn
tSapEgrPolicerParent = _TSapEgrPolicerParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 7),
    _TSapEgrPolicerParent_Type()
)
tSapEgrPolicerParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerParent.setStatus("current")


class _TSapEgrPolicerLevel_Type(TLevel):
    """Custom type tSapEgrPolicerLevel based on TLevel"""
    defaultValue = 1


_TSapEgrPolicerLevel_Object = MibTableColumn
tSapEgrPolicerLevel = _TSapEgrPolicerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 8),
    _TSapEgrPolicerLevel_Type()
)
tSapEgrPolicerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerLevel.setStatus("current")


class _TSapEgrPolicerWeight_Type(TPolicerWeight):
    """Custom type tSapEgrPolicerWeight based on TPolicerWeight"""
    defaultValue = 1


_TSapEgrPolicerWeight_Object = MibTableColumn
tSapEgrPolicerWeight = _TSapEgrPolicerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 9),
    _TSapEgrPolicerWeight_Type()
)
tSapEgrPolicerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerWeight.setStatus("current")


class _TSapEgrPolicerAdminPIR_Type(THPolPIRRate):
    """Custom type tSapEgrPolicerAdminPIR based on THPolPIRRate"""
    defaultValue = -1


_TSapEgrPolicerAdminPIR_Object = MibTableColumn
tSapEgrPolicerAdminPIR = _TSapEgrPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 10),
    _TSapEgrPolicerAdminPIR_Type()
)
tSapEgrPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminPIR.setUnits("kbps")


class _TSapEgrPolicerAdminCIR_Type(THPolCIRRate):
    """Custom type tSapEgrPolicerAdminCIR based on THPolCIRRate"""
    defaultValue = 0


_TSapEgrPolicerAdminCIR_Object = MibTableColumn
tSapEgrPolicerAdminCIR = _TSapEgrPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 11),
    _TSapEgrPolicerAdminCIR_Type()
)
tSapEgrPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminCIR.setUnits("kbps")


class _TSapEgrPolicerStatMode_Type(TmnxEgrPolicerStatMode):
    """Custom type tSapEgrPolicerStatMode based on TmnxEgrPolicerStatMode"""


_TSapEgrPolicerStatMode_Object = MibTableColumn
tSapEgrPolicerStatMode = _TSapEgrPolicerStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 12),
    _TSapEgrPolicerStatMode_Type()
)
tSapEgrPolicerStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerStatMode.setStatus("current")


class _TSapEgrPolicerMBS_Type(TPlcrBurstSizeBytes):
    """Custom type tSapEgrPolicerMBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TSapEgrPolicerMBS_Object = MibTableColumn
tSapEgrPolicerMBS = _TSapEgrPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 13),
    _TSapEgrPolicerMBS_Type()
)
tSapEgrPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerMBS.setUnits("bytes")


class _TSapEgrPolicerHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tSapEgrPolicerHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TSapEgrPolicerHiPrioOnly_Object = MibTableColumn
tSapEgrPolicerHiPrioOnly = _TSapEgrPolicerHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 14),
    _TSapEgrPolicerHiPrioOnly_Type()
)
tSapEgrPolicerHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerHiPrioOnly.setUnits("percent")


class _TSapEgrPolicerCBS_Type(TPlcrBurstSizeBytes):
    """Custom type tSapEgrPolicerCBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TSapEgrPolicerCBS_Object = MibTableColumn
tSapEgrPolicerCBS = _TSapEgrPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 15),
    _TSapEgrPolicerCBS_Type()
)
tSapEgrPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerCBS.setUnits("bytes")


class _TSapEgrPolicerPktOffset_Type(TPerPacketOffset):
    """Custom type tSapEgrPolicerPktOffset based on TPerPacketOffset"""
    defaultValue = 0


_TSapEgrPolicerPktOffset_Object = MibTableColumn
tSapEgrPolicerPktOffset = _TSapEgrPolicerPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 16),
    _TSapEgrPolicerPktOffset_Type()
)
tSapEgrPolicerPktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerPktOffset.setStatus("current")


class _TSapEgrPolicerAdminPIRPercent_Type(Unsigned32):
    """Custom type tSapEgrPolicerAdminPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapEgrPolicerAdminPIRPercent_Type.__name__ = "Unsigned32"
_TSapEgrPolicerAdminPIRPercent_Object = MibTableColumn
tSapEgrPolicerAdminPIRPercent = _TSapEgrPolicerAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 17),
    _TSapEgrPolicerAdminPIRPercent_Type()
)
tSapEgrPolicerAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminPIRPercent.setUnits("hundredths of a percent")


class _TSapEgrPolicerAdminCIRPercent_Type(Unsigned32):
    """Custom type tSapEgrPolicerAdminCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TSapEgrPolicerAdminCIRPercent_Type.__name__ = "Unsigned32"
_TSapEgrPolicerAdminCIRPercent_Object = MibTableColumn
tSapEgrPolicerAdminCIRPercent = _TSapEgrPolicerAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 18),
    _TSapEgrPolicerAdminCIRPercent_Type()
)
tSapEgrPolicerAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdminCIRPercent.setUnits("hundredths of a percent")


class _TSapEgrPolicerRateType_Type(TPolicerRateType):
    """Custom type tSapEgrPolicerRateType based on TPolicerRateType"""


_TSapEgrPolicerRateType_Object = MibTableColumn
tSapEgrPolicerRateType = _TSapEgrPolicerRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 19),
    _TSapEgrPolicerRateType_Type()
)
tSapEgrPolicerRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerRateType.setStatus("current")


class _TSapEgrPolicerSlopeStartDepth_Type(Unsigned32):
    """Custom type tSapEgrPolicerSlopeStartDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapEgrPolicerSlopeStartDepth_Type.__name__ = "Unsigned32"
_TSapEgrPolicerSlopeStartDepth_Object = MibTableColumn
tSapEgrPolicerSlopeStartDepth = _TSapEgrPolicerSlopeStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 20),
    _TSapEgrPolicerSlopeStartDepth_Type()
)
tSapEgrPolicerSlopeStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeStartDepth.setUnits("hundredths of a percent")


class _TSapEgrPolicerSlopeMaxDepth_Type(Unsigned32):
    """Custom type tSapEgrPolicerSlopeMaxDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapEgrPolicerSlopeMaxDepth_Type.__name__ = "Unsigned32"
_TSapEgrPolicerSlopeMaxDepth_Object = MibTableColumn
tSapEgrPolicerSlopeMaxDepth = _TSapEgrPolicerSlopeMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 21),
    _TSapEgrPolicerSlopeMaxDepth_Type()
)
tSapEgrPolicerSlopeMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeMaxDepth.setUnits("hundredths of a percent")


class _TSapEgrPolicerSlopeMaxProb_Type(Unsigned32):
    """Custom type tSapEgrPolicerSlopeMaxProb based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TSapEgrPolicerSlopeMaxProb_Type.__name__ = "Unsigned32"
_TSapEgrPolicerSlopeMaxProb_Object = MibTableColumn
tSapEgrPolicerSlopeMaxProb = _TSapEgrPolicerSlopeMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 22),
    _TSapEgrPolicerSlopeMaxProb_Type()
)
tSapEgrPolicerSlopeMaxProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeMaxProb.setStatus("current")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeMaxProb.setUnits("hundredths of a percent")


class _TSapEgrPolicerSlopeMap_Type(TmnxSlopeMap):
    """Custom type tSapEgrPolicerSlopeMap based on TmnxSlopeMap"""


_TSapEgrPolicerSlopeMap_Object = MibTableColumn
tSapEgrPolicerSlopeMap = _TSapEgrPolicerSlopeMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 23),
    _TSapEgrPolicerSlopeMap_Type()
)
tSapEgrPolicerSlopeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerSlopeMap.setStatus("current")


class _TSapEgrPolicerAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tSapEgrPolicerAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgrPolicerAdvCfgPolicy_Object = MibTableColumn
tSapEgrPolicerAdvCfgPolicy = _TSapEgrPolicerAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 24),
    _TSapEgrPolicerAdvCfgPolicy_Type()
)
tSapEgrPolicerAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerAdvCfgPolicy.setStatus("current")


class _TSapEgrPolicerProfileCapped_Type(TruthValue):
    """Custom type tSapEgrPolicerProfileCapped based on TruthValue"""


_TSapEgrPolicerProfileCapped_Object = MibTableColumn
tSapEgrPolicerProfileCapped = _TSapEgrPolicerProfileCapped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 8, 1, 25),
    _TSapEgrPolicerProfileCapped_Type()
)
tSapEgrPolicerProfileCapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgrPolicerProfileCapped.setStatus("current")
_TSapEgrPolicyNameTable_Object = MibTable
tSapEgrPolicyNameTable = _TSapEgrPolicyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 9)
)
if mibBuilder.loadTexts:
    tSapEgrPolicyNameTable.setStatus("current")
_TSapEgrPolicyNameEntry_Object = MibTableRow
tSapEgrPolicyNameEntry = _TSapEgrPolicyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 9, 1)
)
tSapEgrPolicyNameEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressPolicyName"),
)
if mibBuilder.loadTexts:
    tSapEgrPolicyNameEntry.setStatus("current")
_TSapEgrPolicyNameId_Type = TSapEgressPolicyID
_TSapEgrPolicyNameId_Object = MibTableColumn
tSapEgrPolicyNameId = _TSapEgrPolicyNameId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 9, 1, 1),
    _TSapEgrPolicyNameId_Type()
)
tSapEgrPolicyNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicyNameId.setStatus("current")
_TSapEgrPolicyNameRowStatus_Type = RowStatus
_TSapEgrPolicyNameRowStatus_Object = MibTableColumn
tSapEgrPolicyNameRowStatus = _TSapEgrPolicyNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 9, 1, 2),
    _TSapEgrPolicyNameRowStatus_Type()
)
tSapEgrPolicyNameRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicyNameRowStatus.setStatus("current")
_TSapEgrPolicyNameLastChanged_Type = TimeStamp
_TSapEgrPolicyNameLastChanged_Object = MibTableColumn
tSapEgrPolicyNameLastChanged = _TSapEgrPolicyNameLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 9, 1, 3),
    _TSapEgrPolicyNameLastChanged_Type()
)
tSapEgrPolicyNameLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicyNameLastChanged.setStatus("current")
_TSapEgressDot1pTable_Object = MibTable
tSapEgressDot1pTable = _TSapEgressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10)
)
if mibBuilder.loadTexts:
    tSapEgressDot1pTable.setStatus("current")
_TSapEgressDot1pEntry_Object = MibTableRow
tSapEgressDot1pEntry = _TSapEgressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1)
)
tSapEgressDot1pEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "TIMETRA-QOS-MIB", "tSapEgressDot1pValue"),
)
if mibBuilder.loadTexts:
    tSapEgressDot1pEntry.setStatus("current")


class _TSapEgressDot1pValue_Type(Dot1PPriority):
    """Custom type tSapEgressDot1pValue based on Dot1PPriority"""
    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TSapEgressDot1pValue_Type.__name__ = "Dot1PPriority"
_TSapEgressDot1pValue_Object = MibTableColumn
tSapEgressDot1pValue = _TSapEgressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1, 1),
    _TSapEgressDot1pValue_Type()
)
tSapEgressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSapEgressDot1pValue.setStatus("current")
_TSapEgressDot1pRowStatus_Type = RowStatus
_TSapEgressDot1pRowStatus_Object = MibTableColumn
tSapEgressDot1pRowStatus = _TSapEgressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1, 2),
    _TSapEgressDot1pRowStatus_Type()
)
tSapEgressDot1pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDot1pRowStatus.setStatus("current")
_TSapEgressDot1pLastChanged_Type = TimeStamp
_TSapEgressDot1pLastChanged_Object = MibTableColumn
tSapEgressDot1pLastChanged = _TSapEgressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1, 3),
    _TSapEgressDot1pLastChanged_Type()
)
tSapEgressDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressDot1pLastChanged.setStatus("current")


class _TSapEgressDot1pFC_Type(TNamedItemOrEmpty):
    """Custom type tSapEgressDot1pFC based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSapEgressDot1pFC_Object = MibTableColumn
tSapEgressDot1pFC = _TSapEgressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1, 4),
    _TSapEgressDot1pFC_Type()
)
tSapEgressDot1pFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDot1pFC.setStatus("current")


class _TSapEgressDot1pProfile_Type(TProfileUseDEOrNone):
    """Custom type tSapEgressDot1pProfile based on TProfileUseDEOrNone"""


_TSapEgressDot1pProfile_Object = MibTableColumn
tSapEgressDot1pProfile = _TSapEgressDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 4, 10, 1, 5),
    _TSapEgressDot1pProfile_Type()
)
tSapEgressDot1pProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapEgressDot1pProfile.setStatus("current")
_TNetworkObjects_ObjectIdentity = ObjectIdentity
tNetworkObjects = _TNetworkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5)
)
_TNetworkPolicyTable_Object = MibTable
tNetworkPolicyTable = _TNetworkPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1)
)
if mibBuilder.loadTexts:
    tNetworkPolicyTable.setStatus("current")
_TNetworkPolicyEntry_Object = MibTableRow
tNetworkPolicyEntry = _TNetworkPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1)
)
tNetworkPolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    tNetworkPolicyEntry.setStatus("current")


class _TNetworkPolicyIndex_Type(TNetworkPolicyID):
    """Custom type tNetworkPolicyIndex based on TNetworkPolicyID"""
    subtypeSpec = TNetworkPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
        ValueRangeConstraint(65536, 65536),
        ValueRangeConstraint(65537, 65537),
    )


_TNetworkPolicyIndex_Type.__name__ = "TNetworkPolicyID"
_TNetworkPolicyIndex_Object = MibTableColumn
tNetworkPolicyIndex = _TNetworkPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 1),
    _TNetworkPolicyIndex_Type()
)
tNetworkPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkPolicyIndex.setStatus("current")
_TNetworkPolicyRowStatus_Type = RowStatus
_TNetworkPolicyRowStatus_Object = MibTableColumn
tNetworkPolicyRowStatus = _TNetworkPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 2),
    _TNetworkPolicyRowStatus_Type()
)
tNetworkPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyRowStatus.setStatus("current")


class _TNetworkPolicyScope_Type(TItemScope):
    """Custom type tNetworkPolicyScope based on TItemScope"""


_TNetworkPolicyScope_Object = MibTableColumn
tNetworkPolicyScope = _TNetworkPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 5),
    _TNetworkPolicyScope_Type()
)
tNetworkPolicyScope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyScope.setStatus("current")


class _TNetworkPolicyDescription_Type(TItemDescription):
    """Custom type tNetworkPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TNetworkPolicyDescription_Object = MibTableColumn
tNetworkPolicyDescription = _TNetworkPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 6),
    _TNetworkPolicyDescription_Type()
)
tNetworkPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyDescription.setStatus("current")


class _TNetworkPolicyIngressDefaultActionFC_Type(TFCName):
    """Custom type tNetworkPolicyIngressDefaultActionFC based on TFCName"""
    defaultHexValue = "be"


_TNetworkPolicyIngressDefaultActionFC_Object = MibTableColumn
tNetworkPolicyIngressDefaultActionFC = _TNetworkPolicyIngressDefaultActionFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 7),
    _TNetworkPolicyIngressDefaultActionFC_Type()
)
tNetworkPolicyIngressDefaultActionFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyIngressDefaultActionFC.setStatus("current")


class _TNetworkPolicyIngressDefaultActionProfile_Type(TProfileOrDei):
    """Custom type tNetworkPolicyIngressDefaultActionProfile based on TProfileOrDei"""


_TNetworkPolicyIngressDefaultActionProfile_Object = MibTableColumn
tNetworkPolicyIngressDefaultActionProfile = _TNetworkPolicyIngressDefaultActionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 8),
    _TNetworkPolicyIngressDefaultActionProfile_Type()
)
tNetworkPolicyIngressDefaultActionProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyIngressDefaultActionProfile.setStatus("current")


class _TNetworkPolicyEgressRemark_Type(TruthValue):
    """Custom type tNetworkPolicyEgressRemark based on TruthValue"""


_TNetworkPolicyEgressRemark_Object = MibTableColumn
tNetworkPolicyEgressRemark = _TNetworkPolicyEgressRemark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 9),
    _TNetworkPolicyEgressRemark_Type()
)
tNetworkPolicyEgressRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyEgressRemark.setStatus("current")
_TNetworkPolicyLastChanged_Type = TimeStamp
_TNetworkPolicyLastChanged_Object = MibTableColumn
tNetworkPolicyLastChanged = _TNetworkPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 10),
    _TNetworkPolicyLastChanged_Type()
)
tNetworkPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkPolicyLastChanged.setStatus("current")


class _TNetworkPolicyIngressLerUseDscp_Type(TruthValue):
    """Custom type tNetworkPolicyIngressLerUseDscp based on TruthValue"""


_TNetworkPolicyIngressLerUseDscp_Object = MibTableColumn
tNetworkPolicyIngressLerUseDscp = _TNetworkPolicyIngressLerUseDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 11),
    _TNetworkPolicyIngressLerUseDscp_Type()
)
tNetworkPolicyIngressLerUseDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyIngressLerUseDscp.setStatus("current")


class _TNetworkPolicyEgressRemarkDscp_Type(TruthValue):
    """Custom type tNetworkPolicyEgressRemarkDscp based on TruthValue"""


_TNetworkPolicyEgressRemarkDscp_Object = MibTableColumn
tNetworkPolicyEgressRemarkDscp = _TNetworkPolicyEgressRemarkDscp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 1, 1, 12),
    _TNetworkPolicyEgressRemarkDscp_Type()
)
tNetworkPolicyEgressRemarkDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkPolicyEgressRemarkDscp.setStatus("current")
_TNetworkIngressDSCPTable_Object = MibTable
tNetworkIngressDSCPTable = _TNetworkIngressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2)
)
if mibBuilder.loadTexts:
    tNetworkIngressDSCPTable.setStatus("current")
_TNetworkIngressDSCPEntry_Object = MibTableRow
tNetworkIngressDSCPEntry = _TNetworkIngressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1)
)
tNetworkIngressDSCPEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkIngressDSCP"),
)
if mibBuilder.loadTexts:
    tNetworkIngressDSCPEntry.setStatus("current")
_TNetworkIngressDSCP_Type = TDSCPName
_TNetworkIngressDSCP_Object = MibTableColumn
tNetworkIngressDSCP = _TNetworkIngressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1, 1),
    _TNetworkIngressDSCP_Type()
)
tNetworkIngressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressDSCP.setStatus("current")
_TNetworkIngressDSCPRowStatus_Type = RowStatus
_TNetworkIngressDSCPRowStatus_Object = MibTableColumn
tNetworkIngressDSCPRowStatus = _TNetworkIngressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1, 2),
    _TNetworkIngressDSCPRowStatus_Type()
)
tNetworkIngressDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDSCPRowStatus.setStatus("current")


class _TNetworkIngressDSCPFC_Type(TFCName):
    """Custom type tNetworkIngressDSCPFC based on TFCName"""
    defaultHexValue = ""


_TNetworkIngressDSCPFC_Object = MibTableColumn
tNetworkIngressDSCPFC = _TNetworkIngressDSCPFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1, 3),
    _TNetworkIngressDSCPFC_Type()
)
tNetworkIngressDSCPFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDSCPFC.setStatus("current")
_TNetworkIngressDSCPProfile_Type = TProfile
_TNetworkIngressDSCPProfile_Object = MibTableColumn
tNetworkIngressDSCPProfile = _TNetworkIngressDSCPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1, 4),
    _TNetworkIngressDSCPProfile_Type()
)
tNetworkIngressDSCPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDSCPProfile.setStatus("current")
_TNetworkIngressDSCPLastChanged_Type = TimeStamp
_TNetworkIngressDSCPLastChanged_Object = MibTableColumn
tNetworkIngressDSCPLastChanged = _TNetworkIngressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 2, 1, 5),
    _TNetworkIngressDSCPLastChanged_Type()
)
tNetworkIngressDSCPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressDSCPLastChanged.setStatus("current")
_TNetworkIngressDot1pTable_Object = MibTable
tNetworkIngressDot1pTable = _TNetworkIngressDot1pTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3)
)
if mibBuilder.loadTexts:
    tNetworkIngressDot1pTable.setStatus("current")
_TNetworkIngressDot1pEntry_Object = MibTableRow
tNetworkIngressDot1pEntry = _TNetworkIngressDot1pEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1)
)
tNetworkIngressDot1pEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkIngressDot1pValue"),
)
if mibBuilder.loadTexts:
    tNetworkIngressDot1pEntry.setStatus("current")


class _TNetworkIngressDot1pValue_Type(Dot1PPriority):
    """Custom type tNetworkIngressDot1pValue based on Dot1PPriority"""
    subtypeSpec = Dot1PPriority.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TNetworkIngressDot1pValue_Type.__name__ = "Dot1PPriority"
_TNetworkIngressDot1pValue_Object = MibTableColumn
tNetworkIngressDot1pValue = _TNetworkIngressDot1pValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 1),
    _TNetworkIngressDot1pValue_Type()
)
tNetworkIngressDot1pValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pValue.setStatus("current")
_TNetworkIngressDot1pRowStatus_Type = RowStatus
_TNetworkIngressDot1pRowStatus_Object = MibTableColumn
tNetworkIngressDot1pRowStatus = _TNetworkIngressDot1pRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 2),
    _TNetworkIngressDot1pRowStatus_Type()
)
tNetworkIngressDot1pRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pRowStatus.setStatus("current")


class _TNetworkIngressDot1pFC_Type(TFCName):
    """Custom type tNetworkIngressDot1pFC based on TFCName"""
    defaultHexValue = ""


_TNetworkIngressDot1pFC_Object = MibTableColumn
tNetworkIngressDot1pFC = _TNetworkIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 3),
    _TNetworkIngressDot1pFC_Type()
)
tNetworkIngressDot1pFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pFC.setStatus("current")
_TNetworkIngressDot1pProfile_Type = TDEProfileOrDei
_TNetworkIngressDot1pProfile_Object = MibTableColumn
tNetworkIngressDot1pProfile = _TNetworkIngressDot1pProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 4),
    _TNetworkIngressDot1pProfile_Type()
)
tNetworkIngressDot1pProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pProfile.setStatus("current")
_TNetworkIngressDot1pLastChanged_Type = TimeStamp
_TNetworkIngressDot1pLastChanged_Object = MibTableColumn
tNetworkIngressDot1pLastChanged = _TNetworkIngressDot1pLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 5),
    _TNetworkIngressDot1pLastChanged_Type()
)
tNetworkIngressDot1pLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pLastChanged.setStatus("current")
_TNetworkIngressLSPEXPTable_Object = MibTable
tNetworkIngressLSPEXPTable = _TNetworkIngressLSPEXPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4)
)
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPTable.setStatus("current")
_TNetworkIngressLSPEXPEntry_Object = MibTableRow
tNetworkIngressLSPEXPEntry = _TNetworkIngressLSPEXPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1)
)
tNetworkIngressLSPEXPEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkIngressLSPEXP"),
)
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPEntry.setStatus("current")


class _TNetworkIngressLSPEXP_Type(TLspExpValue):
    """Custom type tNetworkIngressLSPEXP based on TLspExpValue"""
    subtypeSpec = TLspExpValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TNetworkIngressLSPEXP_Type.__name__ = "TLspExpValue"
_TNetworkIngressLSPEXP_Object = MibTableColumn
tNetworkIngressLSPEXP = _TNetworkIngressLSPEXP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1, 1),
    _TNetworkIngressLSPEXP_Type()
)
tNetworkIngressLSPEXP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXP.setStatus("current")
_TNetworkIngressLSPEXPRowStatus_Type = RowStatus
_TNetworkIngressLSPEXPRowStatus_Object = MibTableColumn
tNetworkIngressLSPEXPRowStatus = _TNetworkIngressLSPEXPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1, 2),
    _TNetworkIngressLSPEXPRowStatus_Type()
)
tNetworkIngressLSPEXPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPRowStatus.setStatus("current")


class _TNetworkIngressLSPEXPFC_Type(TFCName):
    """Custom type tNetworkIngressLSPEXPFC based on TFCName"""
    defaultHexValue = ""


_TNetworkIngressLSPEXPFC_Object = MibTableColumn
tNetworkIngressLSPEXPFC = _TNetworkIngressLSPEXPFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1, 3),
    _TNetworkIngressLSPEXPFC_Type()
)
tNetworkIngressLSPEXPFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPFC.setStatus("current")
_TNetworkIngressLSPEXPProfile_Type = TProfile
_TNetworkIngressLSPEXPProfile_Object = MibTableColumn
tNetworkIngressLSPEXPProfile = _TNetworkIngressLSPEXPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1, 4),
    _TNetworkIngressLSPEXPProfile_Type()
)
tNetworkIngressLSPEXPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPProfile.setStatus("current")
_TNetworkIngressLSPEXPLastChanged_Type = TimeStamp
_TNetworkIngressLSPEXPLastChanged_Object = MibTableColumn
tNetworkIngressLSPEXPLastChanged = _TNetworkIngressLSPEXPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 4, 1, 5),
    _TNetworkIngressLSPEXPLastChanged_Type()
)
tNetworkIngressLSPEXPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPLastChanged.setStatus("current")
_TNetworkEgressFCTable_Object = MibTable
tNetworkEgressFCTable = _TNetworkEgressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7)
)
if mibBuilder.loadTexts:
    tNetworkEgressFCTable.setStatus("current")
_TNetworkEgressFCEntry_Object = MibTableRow
tNetworkEgressFCEntry = _TNetworkEgressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1)
)
tNetworkEgressFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkEgressFCName"),
)
if mibBuilder.loadTexts:
    tNetworkEgressFCEntry.setStatus("current")
_TNetworkEgressFCName_Type = TFCName
_TNetworkEgressFCName_Object = MibTableColumn
tNetworkEgressFCName = _TNetworkEgressFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 1),
    _TNetworkEgressFCName_Type()
)
tNetworkEgressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkEgressFCName.setStatus("current")
_TNetworkEgressFCDSCPInProfile_Type = TDSCPNameOrEmpty
_TNetworkEgressFCDSCPInProfile_Object = MibTableColumn
tNetworkEgressFCDSCPInProfile = _TNetworkEgressFCDSCPInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 2),
    _TNetworkEgressFCDSCPInProfile_Type()
)
tNetworkEgressFCDSCPInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDSCPInProfile.setStatus("current")
_TNetworkEgressFCDSCPOutProfile_Type = TDSCPNameOrEmpty
_TNetworkEgressFCDSCPOutProfile_Object = MibTableColumn
tNetworkEgressFCDSCPOutProfile = _TNetworkEgressFCDSCPOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 3),
    _TNetworkEgressFCDSCPOutProfile_Type()
)
tNetworkEgressFCDSCPOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDSCPOutProfile.setStatus("current")
_TNetworkEgressFCLspExpInProfile_Type = TLspExpValue
_TNetworkEgressFCLspExpInProfile_Object = MibTableColumn
tNetworkEgressFCLspExpInProfile = _TNetworkEgressFCLspExpInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 4),
    _TNetworkEgressFCLspExpInProfile_Type()
)
tNetworkEgressFCLspExpInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCLspExpInProfile.setStatus("current")
_TNetworkEgressFCLspExpOutProfile_Type = TLspExpValue
_TNetworkEgressFCLspExpOutProfile_Object = MibTableColumn
tNetworkEgressFCLspExpOutProfile = _TNetworkEgressFCLspExpOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 5),
    _TNetworkEgressFCLspExpOutProfile_Type()
)
tNetworkEgressFCLspExpOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCLspExpOutProfile.setStatus("current")
_TNetworkEgressFCDot1pInProfile_Type = Dot1PPriority
_TNetworkEgressFCDot1pInProfile_Object = MibTableColumn
tNetworkEgressFCDot1pInProfile = _TNetworkEgressFCDot1pInProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 6),
    _TNetworkEgressFCDot1pInProfile_Type()
)
tNetworkEgressFCDot1pInProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDot1pInProfile.setStatus("current")
_TNetworkEgressFCDot1pOutProfile_Type = Dot1PPriority
_TNetworkEgressFCDot1pOutProfile_Object = MibTableColumn
tNetworkEgressFCDot1pOutProfile = _TNetworkEgressFCDot1pOutProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 7),
    _TNetworkEgressFCDot1pOutProfile_Type()
)
tNetworkEgressFCDot1pOutProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDot1pOutProfile.setStatus("current")
_TNetworkEgressFCLastChanged_Type = TimeStamp
_TNetworkEgressFCLastChanged_Object = MibTableColumn
tNetworkEgressFCLastChanged = _TNetworkEgressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 8),
    _TNetworkEgressFCLastChanged_Type()
)
tNetworkEgressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgressFCLastChanged.setStatus("current")


class _TNetworkEgressFCForceDEValue_Type(TDEValue):
    """Custom type tNetworkEgressFCForceDEValue based on TDEValue"""
    defaultValue = -1


_TNetworkEgressFCForceDEValue_Object = MibTableColumn
tNetworkEgressFCForceDEValue = _TNetworkEgressFCForceDEValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 9),
    _TNetworkEgressFCForceDEValue_Type()
)
tNetworkEgressFCForceDEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCForceDEValue.setStatus("current")


class _TNetworkEgressFCDEMark_Type(TruthValue):
    """Custom type tNetworkEgressFCDEMark based on TruthValue"""


_TNetworkEgressFCDEMark_Object = MibTableColumn
tNetworkEgressFCDEMark = _TNetworkEgressFCDEMark_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 10),
    _TNetworkEgressFCDEMark_Type()
)
tNetworkEgressFCDEMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCDEMark.setStatus("current")


class _TNetworkEgressFCQGrpQueue_Type(TEgressQueueId):
    """Custom type tNetworkEgressFCQGrpQueue based on TEgressQueueId"""
    defaultValue = 0


_TNetworkEgressFCQGrpQueue_Object = MibTableColumn
tNetworkEgressFCQGrpQueue = _TNetworkEgressFCQGrpQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 11),
    _TNetworkEgressFCQGrpQueue_Type()
)
tNetworkEgressFCQGrpQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCQGrpQueue.setStatus("current")


class _TNetworkEgressFCQGrpPolicer_Type(TEgrPolicerIdOrNone):
    """Custom type tNetworkEgressFCQGrpPolicer based on TEgrPolicerIdOrNone"""
    defaultValue = 0


_TNetworkEgressFCQGrpPolicer_Object = MibTableColumn
tNetworkEgressFCQGrpPolicer = _TNetworkEgressFCQGrpPolicer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 7, 1, 12),
    _TNetworkEgressFCQGrpPolicer_Type()
)
tNetworkEgressFCQGrpPolicer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgressFCQGrpPolicer.setStatus("current")
_TNetworkIngressFCTable_Object = MibTable
tNetworkIngressFCTable = _TNetworkIngressFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8)
)
if mibBuilder.loadTexts:
    tNetworkIngressFCTable.setStatus("current")
_TNetworkIngressFCEntry_Object = MibTableRow
tNetworkIngressFCEntry = _TNetworkIngressFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8, 1)
)
tNetworkIngressFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkIngressFCName"),
)
if mibBuilder.loadTexts:
    tNetworkIngressFCEntry.setStatus("current")
_TNetworkIngressFCName_Type = TFCName
_TNetworkIngressFCName_Object = MibTableColumn
tNetworkIngressFCName = _TNetworkIngressFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8, 1, 1),
    _TNetworkIngressFCName_Type()
)
tNetworkIngressFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkIngressFCName.setStatus("current")
_TNetworkIngressFCLastChanged_Type = TimeStamp
_TNetworkIngressFCLastChanged_Object = MibTableColumn
tNetworkIngressFCLastChanged = _TNetworkIngressFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8, 1, 2),
    _TNetworkIngressFCLastChanged_Type()
)
tNetworkIngressFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressFCLastChanged.setStatus("current")


class _TNetworkIngressFCMultiCastPlcr_Type(TIngPolicerIdOrNone):
    """Custom type tNetworkIngressFCMultiCastPlcr based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TNetworkIngressFCMultiCastPlcr_Object = MibTableColumn
tNetworkIngressFCMultiCastPlcr = _TNetworkIngressFCMultiCastPlcr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8, 1, 3),
    _TNetworkIngressFCMultiCastPlcr_Type()
)
tNetworkIngressFCMultiCastPlcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkIngressFCMultiCastPlcr.setStatus("current")


class _TNetworkIngressFCUniCastPlcr_Type(TIngPolicerIdOrNone):
    """Custom type tNetworkIngressFCUniCastPlcr based on TIngPolicerIdOrNone"""
    defaultValue = 0


_TNetworkIngressFCUniCastPlcr_Object = MibTableColumn
tNetworkIngressFCUniCastPlcr = _TNetworkIngressFCUniCastPlcr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 8, 1, 4),
    _TNetworkIngressFCUniCastPlcr_Type()
)
tNetworkIngressFCUniCastPlcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkIngressFCUniCastPlcr.setStatus("current")
_TNetworkEgressDSCPTable_Object = MibTable
tNetworkEgressDSCPTable = _TNetworkEgressDSCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9)
)
if mibBuilder.loadTexts:
    tNetworkEgressDSCPTable.setStatus("current")
_TNetworkEgressDSCPEntry_Object = MibTableRow
tNetworkEgressDSCPEntry = _TNetworkEgressDSCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1)
)
tNetworkEgressDSCPEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkEgressDSCP"),
)
if mibBuilder.loadTexts:
    tNetworkEgressDSCPEntry.setStatus("current")
_TNetworkEgressDSCP_Type = TDSCPName
_TNetworkEgressDSCP_Object = MibTableColumn
tNetworkEgressDSCP = _TNetworkEgressDSCP_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1, 1),
    _TNetworkEgressDSCP_Type()
)
tNetworkEgressDSCP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkEgressDSCP.setStatus("current")
_TNetworkEgressDSCPRowStatus_Type = RowStatus
_TNetworkEgressDSCPRowStatus_Object = MibTableColumn
tNetworkEgressDSCPRowStatus = _TNetworkEgressDSCPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1, 2),
    _TNetworkEgressDSCPRowStatus_Type()
)
tNetworkEgressDSCPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressDSCPRowStatus.setStatus("current")
_TNetworkEgressDSCPLastChanged_Type = TimeStamp
_TNetworkEgressDSCPLastChanged_Object = MibTableColumn
tNetworkEgressDSCPLastChanged = _TNetworkEgressDSCPLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1, 3),
    _TNetworkEgressDSCPLastChanged_Type()
)
tNetworkEgressDSCPLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgressDSCPLastChanged.setStatus("current")


class _TNetworkEgressDSCPFC_Type(TFCName):
    """Custom type tNetworkEgressDSCPFC based on TFCName"""
    defaultHexValue = ""


_TNetworkEgressDSCPFC_Object = MibTableColumn
tNetworkEgressDSCPFC = _TNetworkEgressDSCPFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1, 4),
    _TNetworkEgressDSCPFC_Type()
)
tNetworkEgressDSCPFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressDSCPFC.setStatus("current")
_TNetworkEgressDSCPProfile_Type = TProfile
_TNetworkEgressDSCPProfile_Object = MibTableColumn
tNetworkEgressDSCPProfile = _TNetworkEgressDSCPProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 9, 1, 5),
    _TNetworkEgressDSCPProfile_Type()
)
tNetworkEgressDSCPProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressDSCPProfile.setStatus("current")
_TNetworkEgressPrecTable_Object = MibTable
tNetworkEgressPrecTable = _TNetworkEgressPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10)
)
if mibBuilder.loadTexts:
    tNetworkEgressPrecTable.setStatus("current")
_TNetworkEgressPrecEntry_Object = MibTableRow
tNetworkEgressPrecEntry = _TNetworkEgressPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1)
)
tNetworkEgressPrecEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "TIMETRA-QOS-MIB", "tNetworkEgressPrecValue"),
)
if mibBuilder.loadTexts:
    tNetworkEgressPrecEntry.setStatus("current")
_TNetworkEgressPrecValue_Type = TPrecValue
_TNetworkEgressPrecValue_Object = MibTableColumn
tNetworkEgressPrecValue = _TNetworkEgressPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1, 1),
    _TNetworkEgressPrecValue_Type()
)
tNetworkEgressPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkEgressPrecValue.setStatus("current")
_TNetworkEgressPrecRowStatus_Type = RowStatus
_TNetworkEgressPrecRowStatus_Object = MibTableColumn
tNetworkEgressPrecRowStatus = _TNetworkEgressPrecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1, 2),
    _TNetworkEgressPrecRowStatus_Type()
)
tNetworkEgressPrecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressPrecRowStatus.setStatus("current")
_TNetworkEgressPrecLastChanged_Type = TimeStamp
_TNetworkEgressPrecLastChanged_Object = MibTableColumn
tNetworkEgressPrecLastChanged = _TNetworkEgressPrecLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1, 3),
    _TNetworkEgressPrecLastChanged_Type()
)
tNetworkEgressPrecLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgressPrecLastChanged.setStatus("current")


class _TNetworkEgressPrecFC_Type(TFCName):
    """Custom type tNetworkEgressPrecFC based on TFCName"""
    defaultHexValue = ""


_TNetworkEgressPrecFC_Object = MibTableColumn
tNetworkEgressPrecFC = _TNetworkEgressPrecFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1, 4),
    _TNetworkEgressPrecFC_Type()
)
tNetworkEgressPrecFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressPrecFC.setStatus("current")
_TNetworkEgressPrecProfile_Type = TProfile
_TNetworkEgressPrecProfile_Object = MibTableColumn
tNetworkEgressPrecProfile = _TNetworkEgressPrecProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 10, 1, 5),
    _TNetworkEgressPrecProfile_Type()
)
tNetworkEgressPrecProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkEgressPrecProfile.setStatus("current")
_TNetworkQueueObjects_ObjectIdentity = ObjectIdentity
tNetworkQueueObjects = _TNetworkQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6)
)
_TNetworkQueuePolicyTable_Object = MibTable
tNetworkQueuePolicyTable = _TNetworkQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1)
)
if mibBuilder.loadTexts:
    tNetworkQueuePolicyTable.setStatus("current")
_TNetworkQueuePolicyEntry_Object = MibTableRow
tNetworkQueuePolicyEntry = _TNetworkQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1)
)
tNetworkQueuePolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
)
if mibBuilder.loadTexts:
    tNetworkQueuePolicyEntry.setStatus("current")
_TNetworkQueuePolicy_Type = TNamedItem
_TNetworkQueuePolicy_Object = MibTableColumn
tNetworkQueuePolicy = _TNetworkQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 1),
    _TNetworkQueuePolicy_Type()
)
tNetworkQueuePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkQueuePolicy.setStatus("current")
_TNetworkQueuePolicyRowStatus_Type = RowStatus
_TNetworkQueuePolicyRowStatus_Object = MibTableColumn
tNetworkQueuePolicyRowStatus = _TNetworkQueuePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 2),
    _TNetworkQueuePolicyRowStatus_Type()
)
tNetworkQueuePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyRowStatus.setStatus("current")


class _TNetworkQueuePolicyDescription_Type(TItemDescription):
    """Custom type tNetworkQueuePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TNetworkQueuePolicyDescription_Object = MibTableColumn
tNetworkQueuePolicyDescription = _TNetworkQueuePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 3),
    _TNetworkQueuePolicyDescription_Type()
)
tNetworkQueuePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyDescription.setStatus("current")
_TNetworkQueuePolicyLastChanged_Type = TimeStamp
_TNetworkQueuePolicyLastChanged_Object = MibTableColumn
tNetworkQueuePolicyLastChanged = _TNetworkQueuePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 8),
    _TNetworkQueuePolicyLastChanged_Type()
)
tNetworkQueuePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyLastChanged.setStatus("current")
_TNetworkQueuePolicyEHWrrPlcy_Type = TNamedItemOrEmpty
_TNetworkQueuePolicyEHWrrPlcy_Object = MibTableColumn
tNetworkQueuePolicyEHWrrPlcy = _TNetworkQueuePolicyEHWrrPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 9),
    _TNetworkQueuePolicyEHWrrPlcy_Type()
)
tNetworkQueuePolicyEHWrrPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyEHWrrPlcy.setStatus("current")


class _TNetworkQueuePolicyEHPktBOffst_Type(TPerPacketOffset):
    """Custom type tNetworkQueuePolicyEHPktBOffst based on TPerPacketOffset"""
    defaultValue = 0


_TNetworkQueuePolicyEHPktBOffst_Object = MibTableColumn
tNetworkQueuePolicyEHPktBOffst = _TNetworkQueuePolicyEHPktBOffst_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 1, 1, 10),
    _TNetworkQueuePolicyEHPktBOffst_Type()
)
tNetworkQueuePolicyEHPktBOffst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyEHPktBOffst.setStatus("current")
_TNetworkQueueTable_Object = MibTable
tNetworkQueueTable = _TNetworkQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2)
)
if mibBuilder.loadTexts:
    tNetworkQueueTable.setStatus("current")
_TNetworkQueueEntry_Object = MibTableRow
tNetworkQueueEntry = _TNetworkQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1)
)
tNetworkQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
    (0, "TIMETRA-QOS-MIB", "tNetworkQueue"),
)
if mibBuilder.loadTexts:
    tNetworkQueueEntry.setStatus("current")


class _TNetworkQueue_Type(TQueueId):
    """Custom type tNetworkQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TNetworkQueue_Type.__name__ = "TQueueId"
_TNetworkQueue_Object = MibTableColumn
tNetworkQueue = _TNetworkQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 1),
    _TNetworkQueue_Type()
)
tNetworkQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkQueue.setStatus("current")
_TNetworkQueueRowStatus_Type = RowStatus
_TNetworkQueueRowStatus_Object = MibTableColumn
tNetworkQueueRowStatus = _TNetworkQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 2),
    _TNetworkQueueRowStatus_Type()
)
tNetworkQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueRowStatus.setStatus("current")


class _TNetworkQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tNetworkQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TNetworkQueuePoolName_Object = MibTableColumn
tNetworkQueuePoolName = _TNetworkQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 3),
    _TNetworkQueuePoolName_Type()
)
tNetworkQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePoolName.setStatus("current")


class _TNetworkQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tNetworkQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TNetworkQueueParent_Object = MibTableColumn
tNetworkQueueParent = _TNetworkQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 4),
    _TNetworkQueueParent_Type()
)
tNetworkQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueParent.setStatus("current")


class _TNetworkQueueLevel_Type(TLevel):
    """Custom type tNetworkQueueLevel based on TLevel"""
    defaultValue = 1


_TNetworkQueueLevel_Object = MibTableColumn
tNetworkQueueLevel = _TNetworkQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 5),
    _TNetworkQueueLevel_Type()
)
tNetworkQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueLevel.setStatus("current")


class _TNetworkQueueWeight_Type(TWeight):
    """Custom type tNetworkQueueWeight based on TWeight"""
    defaultValue = 1


_TNetworkQueueWeight_Object = MibTableColumn
tNetworkQueueWeight = _TNetworkQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 6),
    _TNetworkQueueWeight_Type()
)
tNetworkQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueWeight.setStatus("current")


class _TNetworkQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tNetworkQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TNetworkQueueCIRLevel_Object = MibTableColumn
tNetworkQueueCIRLevel = _TNetworkQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 7),
    _TNetworkQueueCIRLevel_Type()
)
tNetworkQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueCIRLevel.setStatus("current")


class _TNetworkQueueCIRWeight_Type(TWeight):
    """Custom type tNetworkQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TNetworkQueueCIRWeight_Object = MibTableColumn
tNetworkQueueCIRWeight = _TNetworkQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 8),
    _TNetworkQueueCIRWeight_Type()
)
tNetworkQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueCIRWeight.setStatus("current")


class _TNetworkQueueMCast_Type(TruthValue):
    """Custom type tNetworkQueueMCast based on TruthValue"""


_TNetworkQueueMCast_Object = MibTableColumn
tNetworkQueueMCast = _TNetworkQueueMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 9),
    _TNetworkQueueMCast_Type()
)
tNetworkQueueMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueMCast.setStatus("current")


class _TNetworkQueueExpedite_Type(Integer32):
    """Custom type tNetworkQueueExpedite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-expedited", 2),
          ("expedited", 1),
          ("non-expedited", 3))
    )


_TNetworkQueueExpedite_Type.__name__ = "Integer32"
_TNetworkQueueExpedite_Object = MibTableColumn
tNetworkQueueExpedite = _TNetworkQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 10),
    _TNetworkQueueExpedite_Type()
)
tNetworkQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueExpedite.setStatus("current")


class _TNetworkQueueCIR_Type(TRatePercent):
    """Custom type tNetworkQueueCIR based on TRatePercent"""
    defaultValue = 0


_TNetworkQueueCIR_Object = MibTableColumn
tNetworkQueueCIR = _TNetworkQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 11),
    _TNetworkQueueCIR_Type()
)
tNetworkQueueCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueCIR.setStatus("current")


class _TNetworkQueuePIR_Type(TPIRRatePercent):
    """Custom type tNetworkQueuePIR based on TPIRRatePercent"""
    defaultValue = 100


_TNetworkQueuePIR_Object = MibTableColumn
tNetworkQueuePIR = _TNetworkQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 12),
    _TNetworkQueuePIR_Type()
)
tNetworkQueuePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePIR.setStatus("current")


class _TNetworkQueueCBS_Type(TBurstHundredthsOfPercent):
    """Custom type tNetworkQueueCBS based on TBurstHundredthsOfPercent"""
    defaultValue = 100


_TNetworkQueueCBS_Object = MibTableColumn
tNetworkQueueCBS = _TNetworkQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 13),
    _TNetworkQueueCBS_Type()
)
tNetworkQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkQueueCBS.setUnits("Hundredths of a percent")


class _TNetworkQueueMBS_Type(TBurstHundredthsOfPercent):
    """Custom type tNetworkQueueMBS based on TBurstHundredthsOfPercent"""
    defaultValue = 10000


_TNetworkQueueMBS_Object = MibTableColumn
tNetworkQueueMBS = _TNetworkQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 14),
    _TNetworkQueueMBS_Type()
)
tNetworkQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueMBS.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkQueueMBS.setUnits("Hundredths of a percent")


class _TNetworkQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tNetworkQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TNetworkQueueHiPrioOnly_Object = MibTableColumn
tNetworkQueueHiPrioOnly = _TNetworkQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 15),
    _TNetworkQueueHiPrioOnly_Type()
)
tNetworkQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueHiPrioOnly.setStatus("current")
_TNetworkQueueLastChanged_Type = TimeStamp
_TNetworkQueueLastChanged_Object = MibTableColumn
tNetworkQueueLastChanged = _TNetworkQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 16),
    _TNetworkQueueLastChanged_Type()
)
tNetworkQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueueLastChanged.setStatus("current")


class _TNetworkQueueUsePortParent_Type(TruthValue):
    """Custom type tNetworkQueueUsePortParent based on TruthValue"""


_TNetworkQueueUsePortParent_Object = MibTableColumn
tNetworkQueueUsePortParent = _TNetworkQueueUsePortParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 17),
    _TNetworkQueueUsePortParent_Type()
)
tNetworkQueueUsePortParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueUsePortParent.setStatus("current")


class _TNetworkQueuePortLvl_Type(TLevel):
    """Custom type tNetworkQueuePortLvl based on TLevel"""
    defaultValue = 1


_TNetworkQueuePortLvl_Object = MibTableColumn
tNetworkQueuePortLvl = _TNetworkQueuePortLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 18),
    _TNetworkQueuePortLvl_Type()
)
tNetworkQueuePortLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePortLvl.setStatus("current")


class _TNetworkQueuePortWght_Type(TWeight):
    """Custom type tNetworkQueuePortWght based on TWeight"""
    defaultValue = 1


_TNetworkQueuePortWght_Object = MibTableColumn
tNetworkQueuePortWght = _TNetworkQueuePortWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 19),
    _TNetworkQueuePortWght_Type()
)
tNetworkQueuePortWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePortWght.setStatus("current")


class _TNetworkQueuePortCIRLvl_Type(TLevelOrDefault):
    """Custom type tNetworkQueuePortCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TNetworkQueuePortCIRLvl_Object = MibTableColumn
tNetworkQueuePortCIRLvl = _TNetworkQueuePortCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 20),
    _TNetworkQueuePortCIRLvl_Type()
)
tNetworkQueuePortCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePortCIRLvl.setStatus("current")


class _TNetworkQueuePortCIRWght_Type(TWeight):
    """Custom type tNetworkQueuePortCIRWght based on TWeight"""
    defaultValue = 0


_TNetworkQueuePortCIRWght_Object = MibTableColumn
tNetworkQueuePortCIRWght = _TNetworkQueuePortCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 21),
    _TNetworkQueuePortCIRWght_Type()
)
tNetworkQueuePortCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePortCIRWght.setStatus("current")


class _TNetworkQueuePortAvgOverhead_Type(Unsigned32):
    """Custom type tNetworkQueuePortAvgOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TNetworkQueuePortAvgOverhead_Type.__name__ = "Unsigned32"
_TNetworkQueuePortAvgOverhead_Object = MibTableColumn
tNetworkQueuePortAvgOverhead = _TNetworkQueuePortAvgOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 22),
    _TNetworkQueuePortAvgOverhead_Type()
)
tNetworkQueuePortAvgOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePortAvgOverhead.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkQueuePortAvgOverhead.setUnits("Hundredths of a percent")


class _TNetworkQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tNetworkQueueCIRAdaptation based on TAdaptationRule"""


_TNetworkQueueCIRAdaptation_Object = MibTableColumn
tNetworkQueueCIRAdaptation = _TNetworkQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 23),
    _TNetworkQueueCIRAdaptation_Type()
)
tNetworkQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueCIRAdaptation.setStatus("current")


class _TNetworkQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tNetworkQueuePIRAdaptation based on TAdaptationRule"""


_TNetworkQueuePIRAdaptation_Object = MibTableColumn
tNetworkQueuePIRAdaptation = _TNetworkQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 2, 1, 24),
    _TNetworkQueuePIRAdaptation_Type()
)
tNetworkQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueuePIRAdaptation.setStatus("current")
_TNetworkQueueFCTable_Object = MibTable
tNetworkQueueFCTable = _TNetworkQueueFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3)
)
if mibBuilder.loadTexts:
    tNetworkQueueFCTable.setStatus("current")
_TNetworkQueueFCEntry_Object = MibTableRow
tNetworkQueueFCEntry = _TNetworkQueueFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1)
)
tNetworkQueueFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
    (0, "TIMETRA-QOS-MIB", "tNetworkQueueFCName"),
)
if mibBuilder.loadTexts:
    tNetworkQueueFCEntry.setStatus("current")
_TNetworkQueueFCName_Type = TFCName
_TNetworkQueueFCName_Object = MibTableColumn
tNetworkQueueFCName = _TNetworkQueueFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 1),
    _TNetworkQueueFCName_Type()
)
tNetworkQueueFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkQueueFCName.setStatus("current")
_TNetworkQueueFCRowStatus_Type = RowStatus
_TNetworkQueueFCRowStatus_Object = MibTableColumn
tNetworkQueueFCRowStatus = _TNetworkQueueFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 2),
    _TNetworkQueueFCRowStatus_Type()
)
tNetworkQueueFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueFCRowStatus.setStatus("current")


class _TNetworkQueueFC_Type(TQueueId):
    """Custom type tNetworkQueueFC based on TQueueId"""
    defaultValue = 1

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TNetworkQueueFC_Type.__name__ = "TQueueId"
_TNetworkQueueFC_Object = MibTableColumn
tNetworkQueueFC = _TNetworkQueueFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 3),
    _TNetworkQueueFC_Type()
)
tNetworkQueueFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueFC.setStatus("current")


class _TNetworkQueueFCMCast_Type(TQueueId):
    """Custom type tNetworkQueueFCMCast based on TQueueId"""
    defaultValue = 9

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TNetworkQueueFCMCast_Type.__name__ = "TQueueId"
_TNetworkQueueFCMCast_Object = MibTableColumn
tNetworkQueueFCMCast = _TNetworkQueueFCMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 4),
    _TNetworkQueueFCMCast_Type()
)
tNetworkQueueFCMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueFCMCast.setStatus("current")
_TNetworkQueueFCLastChanged_Type = TimeStamp
_TNetworkQueueFCLastChanged_Object = MibTableColumn
tNetworkQueueFCLastChanged = _TNetworkQueueFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 7),
    _TNetworkQueueFCLastChanged_Type()
)
tNetworkQueueFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueueFCLastChanged.setStatus("current")


class _TNetworkQueueFCEgrHsmdaQueue_Type(TQueueId):
    """Custom type tNetworkQueueFCEgrHsmdaQueue based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TNetworkQueueFCEgrHsmdaQueue_Type.__name__ = "TQueueId"
_TNetworkQueueFCEgrHsmdaQueue_Object = MibTableColumn
tNetworkQueueFCEgrHsmdaQueue = _TNetworkQueueFCEgrHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 3, 1, 8),
    _TNetworkQueueFCEgrHsmdaQueue_Type()
)
tNetworkQueueFCEgrHsmdaQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkQueueFCEgrHsmdaQueue.setStatus("current")
_TNetworkEgrHsmdaQueueTable_Object = MibTable
tNetworkEgrHsmdaQueueTable = _TNetworkEgrHsmdaQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4)
)
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueTable.setStatus("current")
_TNetworkEgrHsmdaQueueEntry_Object = MibTableRow
tNetworkEgrHsmdaQueueEntry = _TNetworkEgrHsmdaQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1)
)
tNetworkEgrHsmdaQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
    (0, "TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueue"),
)
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueEntry.setStatus("current")


class _TNetworkEgrHsmdaQueue_Type(TEgressHsmdaQueueId):
    """Custom type tNetworkEgrHsmdaQueue based on TEgressHsmdaQueueId"""
    subtypeSpec = TEgressHsmdaQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TNetworkEgrHsmdaQueue_Type.__name__ = "TEgressHsmdaQueueId"
_TNetworkEgrHsmdaQueue_Object = MibTableColumn
tNetworkEgrHsmdaQueue = _TNetworkEgrHsmdaQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 1),
    _TNetworkEgrHsmdaQueue_Type()
)
tNetworkEgrHsmdaQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueue.setStatus("current")


class _TNetworkEgrHsmdaQueuePIRPercent_Type(Unsigned32):
    """Custom type tNetworkEgrHsmdaQueuePIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TNetworkEgrHsmdaQueuePIRPercent_Type.__name__ = "Unsigned32"
_TNetworkEgrHsmdaQueuePIRPercent_Object = MibTableColumn
tNetworkEgrHsmdaQueuePIRPercent = _TNetworkEgrHsmdaQueuePIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 2),
    _TNetworkEgrHsmdaQueuePIRPercent_Type()
)
tNetworkEgrHsmdaQueuePIRPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueuePIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueuePIRPercent.setUnits("hundredths of a percent")


class _TNetworkEgrHsmdaQueuePIRAdaptn_Type(TAdaptationRule):
    """Custom type tNetworkEgrHsmdaQueuePIRAdaptn based on TAdaptationRule"""


_TNetworkEgrHsmdaQueuePIRAdaptn_Object = MibTableColumn
tNetworkEgrHsmdaQueuePIRAdaptn = _TNetworkEgrHsmdaQueuePIRAdaptn_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 3),
    _TNetworkEgrHsmdaQueuePIRAdaptn_Type()
)
tNetworkEgrHsmdaQueuePIRAdaptn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueuePIRAdaptn.setStatus("current")


class _TNetworkEgrHsmdaQueueWrrWeight_Type(THsmdaWrrWeight):
    """Custom type tNetworkEgrHsmdaQueueWrrWeight based on THsmdaWrrWeight"""
    defaultValue = 1


_TNetworkEgrHsmdaQueueWrrWeight_Object = MibTableColumn
tNetworkEgrHsmdaQueueWrrWeight = _TNetworkEgrHsmdaQueueWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 4),
    _TNetworkEgrHsmdaQueueWrrWeight_Type()
)
tNetworkEgrHsmdaQueueWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueWrrWeight.setStatus("current")


class _TNetworkEgrHsmdaQueueMBS_Type(THSMDABurstSizeBytes):
    """Custom type tNetworkEgrHsmdaQueueMBS based on THSMDABurstSizeBytes"""
    defaultValue = -1


_TNetworkEgrHsmdaQueueMBS_Object = MibTableColumn
tNetworkEgrHsmdaQueueMBS = _TNetworkEgrHsmdaQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 5),
    _TNetworkEgrHsmdaQueueMBS_Type()
)
tNetworkEgrHsmdaQueueMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueMBS.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueMBS.setUnits("bytes")


class _TNetworkEgrHsmdaQueueSlopePolicy_Type(TNamedItem):
    """Custom type tNetworkEgrHsmdaQueueSlopePolicy based on TNamedItem"""
    defaultValue = OctetString("default")


_TNetworkEgrHsmdaQueueSlopePolicy_Object = MibTableColumn
tNetworkEgrHsmdaQueueSlopePolicy = _TNetworkEgrHsmdaQueueSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 6),
    _TNetworkEgrHsmdaQueueSlopePolicy_Type()
)
tNetworkEgrHsmdaQueueSlopePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueSlopePolicy.setStatus("current")
_TNetworkEgrHsmdaQueueLastChanged_Type = TimeStamp
_TNetworkEgrHsmdaQueueLastChanged_Object = MibTableColumn
tNetworkEgrHsmdaQueueLastChanged = _TNetworkEgrHsmdaQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 7),
    _TNetworkEgrHsmdaQueueLastChanged_Type()
)
tNetworkEgrHsmdaQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueLastChanged.setStatus("current")


class _TNetworkEgrHsmdaQueueBurstLimit_Type(THSMDAQueueBurstLimit):
    """Custom type tNetworkEgrHsmdaQueueBurstLimit based on THSMDAQueueBurstLimit"""
    defaultValue = -1


_TNetworkEgrHsmdaQueueBurstLimit_Object = MibTableColumn
tNetworkEgrHsmdaQueueBurstLimit = _TNetworkEgrHsmdaQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 6, 4, 1, 8),
    _TNetworkEgrHsmdaQueueBurstLimit_Type()
)
tNetworkEgrHsmdaQueueBurstLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueBurstLimit.setUnits("bytes")
_TSharedQueueObjects_ObjectIdentity = ObjectIdentity
tSharedQueueObjects = _TSharedQueueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7)
)
_TSharedQueuePolicyTable_Object = MibTable
tSharedQueuePolicyTable = _TSharedQueuePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1)
)
if mibBuilder.loadTexts:
    tSharedQueuePolicyTable.setStatus("current")
_TSharedQueuePolicyEntry_Object = MibTableRow
tSharedQueuePolicyEntry = _TSharedQueuePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1, 1)
)
tSharedQueuePolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
)
if mibBuilder.loadTexts:
    tSharedQueuePolicyEntry.setStatus("current")
_TSharedQueuePolicy_Type = TNamedItem
_TSharedQueuePolicy_Object = MibTableColumn
tSharedQueuePolicy = _TSharedQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1, 1, 1),
    _TSharedQueuePolicy_Type()
)
tSharedQueuePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSharedQueuePolicy.setStatus("current")
_TSharedQueuePolicyRowStatus_Type = RowStatus
_TSharedQueuePolicyRowStatus_Object = MibTableColumn
tSharedQueuePolicyRowStatus = _TSharedQueuePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1, 1, 2),
    _TSharedQueuePolicyRowStatus_Type()
)
tSharedQueuePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueuePolicyRowStatus.setStatus("current")
_TSharedQueuePolicyLastChanged_Type = TimeStamp
_TSharedQueuePolicyLastChanged_Object = MibTableColumn
tSharedQueuePolicyLastChanged = _TSharedQueuePolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1, 1, 3),
    _TSharedQueuePolicyLastChanged_Type()
)
tSharedQueuePolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueuePolicyLastChanged.setStatus("current")


class _TSharedQueuePolicyDescription_Type(TItemDescription):
    """Custom type tSharedQueuePolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TSharedQueuePolicyDescription_Object = MibTableColumn
tSharedQueuePolicyDescription = _TSharedQueuePolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 1, 1, 4),
    _TSharedQueuePolicyDescription_Type()
)
tSharedQueuePolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueuePolicyDescription.setStatus("current")
_TSharedQueueTable_Object = MibTable
tSharedQueueTable = _TSharedQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2)
)
if mibBuilder.loadTexts:
    tSharedQueueTable.setStatus("current")
_TSharedQueueEntry_Object = MibTableRow
tSharedQueueEntry = _TSharedQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1)
)
tSharedQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
    (0, "TIMETRA-QOS-MIB", "tSharedQueueId"),
)
if mibBuilder.loadTexts:
    tSharedQueueEntry.setStatus("current")


class _TSharedQueueId_Type(TQueueId):
    """Custom type tSharedQueueId based on TQueueId"""
    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TSharedQueueId_Type.__name__ = "TQueueId"
_TSharedQueueId_Object = MibTableColumn
tSharedQueueId = _TSharedQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 1),
    _TSharedQueueId_Type()
)
tSharedQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSharedQueueId.setStatus("current")
_TSharedQueueRowStatus_Type = RowStatus
_TSharedQueueRowStatus_Object = MibTableColumn
tSharedQueueRowStatus = _TSharedQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 2),
    _TSharedQueueRowStatus_Type()
)
tSharedQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueRowStatus.setStatus("current")
_TSharedQueueLastChanged_Type = TimeStamp
_TSharedQueueLastChanged_Object = MibTableColumn
tSharedQueueLastChanged = _TSharedQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 3),
    _TSharedQueueLastChanged_Type()
)
tSharedQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueueLastChanged.setStatus("current")


class _TSharedQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tSharedQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSharedQueuePoolName_Object = MibTableColumn
tSharedQueuePoolName = _TSharedQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 4),
    _TSharedQueuePoolName_Type()
)
tSharedQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueuePoolName.setStatus("current")


class _TSharedQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tSharedQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TSharedQueueParent_Object = MibTableColumn
tSharedQueueParent = _TSharedQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 5),
    _TSharedQueueParent_Type()
)
tSharedQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueParent.setStatus("current")


class _TSharedQueueLevel_Type(TLevel):
    """Custom type tSharedQueueLevel based on TLevel"""
    defaultValue = 1


_TSharedQueueLevel_Object = MibTableColumn
tSharedQueueLevel = _TSharedQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 6),
    _TSharedQueueLevel_Type()
)
tSharedQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueLevel.setStatus("current")


class _TSharedQueueWeight_Type(TWeight):
    """Custom type tSharedQueueWeight based on TWeight"""
    defaultValue = 1


_TSharedQueueWeight_Object = MibTableColumn
tSharedQueueWeight = _TSharedQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 7),
    _TSharedQueueWeight_Type()
)
tSharedQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueWeight.setStatus("current")


class _TSharedQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tSharedQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TSharedQueueCIRLevel_Object = MibTableColumn
tSharedQueueCIRLevel = _TSharedQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 8),
    _TSharedQueueCIRLevel_Type()
)
tSharedQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueCIRLevel.setStatus("current")


class _TSharedQueueCIRWeight_Type(TWeight):
    """Custom type tSharedQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TSharedQueueCIRWeight_Object = MibTableColumn
tSharedQueueCIRWeight = _TSharedQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 9),
    _TSharedQueueCIRWeight_Type()
)
tSharedQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueCIRWeight.setStatus("current")


class _TSharedQueueExpedite_Type(Integer32):
    """Custom type tSharedQueueExpedite based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-expedited", 2),
          ("expedited", 1),
          ("non-expedited", 3))
    )


_TSharedQueueExpedite_Type.__name__ = "Integer32"
_TSharedQueueExpedite_Object = MibTableColumn
tSharedQueueExpedite = _TSharedQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 10),
    _TSharedQueueExpedite_Type()
)
tSharedQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueExpedite.setStatus("current")


class _TSharedQueueCIR_Type(TRatePercent):
    """Custom type tSharedQueueCIR based on TRatePercent"""
    defaultValue = 0


_TSharedQueueCIR_Object = MibTableColumn
tSharedQueueCIR = _TSharedQueueCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 11),
    _TSharedQueueCIR_Type()
)
tSharedQueueCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueCIR.setStatus("current")


class _TSharedQueuePIR_Type(TPIRRatePercent):
    """Custom type tSharedQueuePIR based on TPIRRatePercent"""
    defaultValue = 100


_TSharedQueuePIR_Object = MibTableColumn
tSharedQueuePIR = _TSharedQueuePIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 12),
    _TSharedQueuePIR_Type()
)
tSharedQueuePIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueuePIR.setStatus("current")


class _TSharedQueueCBS_Type(TBurstPercent):
    """Custom type tSharedQueueCBS based on TBurstPercent"""
    defaultValue = 0


_TSharedQueueCBS_Object = MibTableColumn
tSharedQueueCBS = _TSharedQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 13),
    _TSharedQueueCBS_Type()
)
tSharedQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueCBS.setStatus("current")


class _TSharedQueueMBS_Type(TBurstPercent):
    """Custom type tSharedQueueMBS based on TBurstPercent"""
    defaultValue = 100


_TSharedQueueMBS_Object = MibTableColumn
tSharedQueueMBS = _TSharedQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 14),
    _TSharedQueueMBS_Type()
)
tSharedQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueMBS.setStatus("current")


class _TSharedQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tSharedQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TSharedQueueHiPrioOnly_Object = MibTableColumn
tSharedQueueHiPrioOnly = _TSharedQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 15),
    _TSharedQueueHiPrioOnly_Type()
)
tSharedQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueHiPrioOnly.setStatus("current")


class _TSharedQueueIsMultipoint_Type(TruthValue):
    """Custom type tSharedQueueIsMultipoint based on TruthValue"""


_TSharedQueueIsMultipoint_Object = MibTableColumn
tSharedQueueIsMultipoint = _TSharedQueueIsMultipoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 2, 1, 16),
    _TSharedQueueIsMultipoint_Type()
)
tSharedQueueIsMultipoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueIsMultipoint.setStatus("current")
_TSharedQueueFCTable_Object = MibTable
tSharedQueueFCTable = _TSharedQueueFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3)
)
if mibBuilder.loadTexts:
    tSharedQueueFCTable.setStatus("current")
_TSharedQueueFCEntry_Object = MibTableRow
tSharedQueueFCEntry = _TSharedQueueFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1)
)
tSharedQueueFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
    (0, "TIMETRA-QOS-MIB", "tSharedQueueFCName"),
)
if mibBuilder.loadTexts:
    tSharedQueueFCEntry.setStatus("current")
_TSharedQueueFCName_Type = TFCName
_TSharedQueueFCName_Object = MibTableColumn
tSharedQueueFCName = _TSharedQueueFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 1),
    _TSharedQueueFCName_Type()
)
tSharedQueueFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSharedQueueFCName.setStatus("current")
_TSharedQueueFCRowStatus_Type = RowStatus
_TSharedQueueFCRowStatus_Object = MibTableColumn
tSharedQueueFCRowStatus = _TSharedQueueFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 2),
    _TSharedQueueFCRowStatus_Type()
)
tSharedQueueFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueFCRowStatus.setStatus("current")
_TSharedQueueFCLastChanged_Type = TimeStamp
_TSharedQueueFCLastChanged_Object = MibTableColumn
tSharedQueueFCLastChanged = _TSharedQueueFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 3),
    _TSharedQueueFCLastChanged_Type()
)
tSharedQueueFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueueFCLastChanged.setStatus("current")


class _TSharedQueueFCQueue_Type(TQueueId):
    """Custom type tSharedQueueFCQueue based on TQueueId"""
    defaultValue = 1

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TSharedQueueFCQueue_Type.__name__ = "TQueueId"
_TSharedQueueFCQueue_Object = MibTableColumn
tSharedQueueFCQueue = _TSharedQueueFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 4),
    _TSharedQueueFCQueue_Type()
)
tSharedQueueFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueFCQueue.setStatus("current")


class _TSharedQueueFCMCastQueue_Type(TQueueId):
    """Custom type tSharedQueueFCMCastQueue based on TQueueId"""
    defaultValue = 9

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 32),
    )


_TSharedQueueFCMCastQueue_Type.__name__ = "TQueueId"
_TSharedQueueFCMCastQueue_Object = MibTableColumn
tSharedQueueFCMCastQueue = _TSharedQueueFCMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 5),
    _TSharedQueueFCMCastQueue_Type()
)
tSharedQueueFCMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueFCMCastQueue.setStatus("current")


class _TSharedQueueFCBCastQueue_Type(TQueueId):
    """Custom type tSharedQueueFCBCastQueue based on TQueueId"""
    defaultValue = 17

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 32),
    )


_TSharedQueueFCBCastQueue_Type.__name__ = "TQueueId"
_TSharedQueueFCBCastQueue_Object = MibTableColumn
tSharedQueueFCBCastQueue = _TSharedQueueFCBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 6),
    _TSharedQueueFCBCastQueue_Type()
)
tSharedQueueFCBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueFCBCastQueue.setStatus("current")


class _TSharedQueueFCUnknownQueue_Type(TQueueId):
    """Custom type tSharedQueueFCUnknownQueue based on TQueueId"""
    defaultValue = 25

    subtypeSpec = TQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9, 32),
    )


_TSharedQueueFCUnknownQueue_Type.__name__ = "TQueueId"
_TSharedQueueFCUnknownQueue_Object = MibTableColumn
tSharedQueueFCUnknownQueue = _TSharedQueueFCUnknownQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 3, 1, 7),
    _TSharedQueueFCUnknownQueue_Type()
)
tSharedQueueFCUnknownQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSharedQueueFCUnknownQueue.setStatus("current")
_TQosIngQGroupTable_Object = MibTable
tQosIngQGroupTable = _TQosIngQGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4)
)
if mibBuilder.loadTexts:
    tQosIngQGroupTable.setStatus("current")
_TQosIngQGroupEntry_Object = MibTableRow
tQosIngQGroupEntry = _TQosIngQGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4, 1)
)
tQosIngQGroupEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosIngQGroupName"),
)
if mibBuilder.loadTexts:
    tQosIngQGroupEntry.setStatus("current")
_TQosIngQGroupName_Type = TNamedItem
_TQosIngQGroupName_Object = MibTableColumn
tQosIngQGroupName = _TQosIngQGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4, 1, 1),
    _TQosIngQGroupName_Type()
)
tQosIngQGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosIngQGroupName.setStatus("current")
_TQosIngQGroupRowStatus_Type = RowStatus
_TQosIngQGroupRowStatus_Object = MibTableColumn
tQosIngQGroupRowStatus = _TQosIngQGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4, 1, 2),
    _TQosIngQGroupRowStatus_Type()
)
tQosIngQGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQGroupRowStatus.setStatus("current")
_TQosIngQGroupLastChanged_Type = TimeStamp
_TQosIngQGroupLastChanged_Object = MibTableColumn
tQosIngQGroupLastChanged = _TQosIngQGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4, 1, 3),
    _TQosIngQGroupLastChanged_Type()
)
tQosIngQGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngQGroupLastChanged.setStatus("current")


class _TQosIngQGroupDescr_Type(TItemDescription):
    """Custom type tQosIngQGroupDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosIngQGroupDescr_Object = MibTableColumn
tQosIngQGroupDescr = _TQosIngQGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 4, 1, 4),
    _TQosIngQGroupDescr_Type()
)
tQosIngQGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQGroupDescr.setStatus("current")
_TQosIngQueueTable_Object = MibTable
tQosIngQueueTable = _TQosIngQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5)
)
if mibBuilder.loadTexts:
    tQosIngQueueTable.setStatus("current")
_TQosIngQueueEntry_Object = MibTableRow
tQosIngQueueEntry = _TQosIngQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1)
)
tQosIngQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosIngQGroupName"),
    (0, "TIMETRA-QOS-MIB", "tQosIngQueue"),
)
if mibBuilder.loadTexts:
    tQosIngQueueEntry.setStatus("current")


class _TQosIngQueue_Type(TIngressQueueId):
    """Custom type tQosIngQueue based on TIngressQueueId"""
    subtypeSpec = TIngressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TQosIngQueue_Type.__name__ = "TIngressQueueId"
_TQosIngQueue_Object = MibTableColumn
tQosIngQueue = _TQosIngQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 1),
    _TQosIngQueue_Type()
)
tQosIngQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosIngQueue.setStatus("current")
_TQosIngQueueRowStatus_Type = RowStatus
_TQosIngQueueRowStatus_Object = MibTableColumn
tQosIngQueueRowStatus = _TQosIngQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 2),
    _TQosIngQueueRowStatus_Type()
)
tQosIngQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueRowStatus.setStatus("current")


class _TQosIngQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tQosIngQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosIngQueueParent_Object = MibTableColumn
tQosIngQueueParent = _TQosIngQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 3),
    _TQosIngQueueParent_Type()
)
tQosIngQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueParent.setStatus("current")


class _TQosIngQueueLevel_Type(TLevel):
    """Custom type tQosIngQueueLevel based on TLevel"""
    defaultValue = 1


_TQosIngQueueLevel_Object = MibTableColumn
tQosIngQueueLevel = _TQosIngQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 4),
    _TQosIngQueueLevel_Type()
)
tQosIngQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueLevel.setStatus("current")


class _TQosIngQueueWeight_Type(TWeight):
    """Custom type tQosIngQueueWeight based on TWeight"""
    defaultValue = 1


_TQosIngQueueWeight_Object = MibTableColumn
tQosIngQueueWeight = _TQosIngQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 5),
    _TQosIngQueueWeight_Type()
)
tQosIngQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueWeight.setStatus("current")


class _TQosIngQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tQosIngQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TQosIngQueueCIRLevel_Object = MibTableColumn
tQosIngQueueCIRLevel = _TQosIngQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 6),
    _TQosIngQueueCIRLevel_Type()
)
tQosIngQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueCIRLevel.setStatus("current")


class _TQosIngQueueCIRWeight_Type(TWeight):
    """Custom type tQosIngQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TQosIngQueueCIRWeight_Object = MibTableColumn
tQosIngQueueCIRWeight = _TQosIngQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 7),
    _TQosIngQueueCIRWeight_Type()
)
tQosIngQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueCIRWeight.setStatus("current")


class _TQosIngQueueMCast_Type(TruthValue):
    """Custom type tQosIngQueueMCast based on TruthValue"""


_TQosIngQueueMCast_Object = MibTableColumn
tQosIngQueueMCast = _TQosIngQueueMCast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 8),
    _TQosIngQueueMCast_Type()
)
tQosIngQueueMCast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueMCast.setStatus("current")


class _TQosIngQueueExpedite_Type(Integer32):
    """Custom type tQosIngQueueExpedite based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 3),
          ("expedited", 1))
    )


_TQosIngQueueExpedite_Type.__name__ = "Integer32"
_TQosIngQueueExpedite_Object = MibTableColumn
tQosIngQueueExpedite = _TQosIngQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 9),
    _TQosIngQueueExpedite_Type()
)
tQosIngQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueExpedite.setStatus("current")


class _TQosIngQueueCBS_Type(TBurstSize):
    """Custom type tQosIngQueueCBS based on TBurstSize"""
    defaultValue = -1


_TQosIngQueueCBS_Object = MibTableColumn
tQosIngQueueCBS = _TQosIngQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 10),
    _TQosIngQueueCBS_Type()
)
tQosIngQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngQueueCBS.setUnits("kilo-bytes")


class _TQosIngQueueMBS_Type(TBurstSize):
    """Custom type tQosIngQueueMBS based on TBurstSize"""
    defaultValue = -1


_TQosIngQueueMBS_Object = MibTableColumn
tQosIngQueueMBS = _TQosIngQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 11),
    _TQosIngQueueMBS_Type()
)
tQosIngQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueMBS.setStatus("obsolete")
if mibBuilder.loadTexts:
    tQosIngQueueMBS.setUnits("kilo-bytes")


class _TQosIngQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tQosIngQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TQosIngQueueHiPrioOnly_Object = MibTableColumn
tQosIngQueueHiPrioOnly = _TQosIngQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 12),
    _TQosIngQueueHiPrioOnly_Type()
)
tQosIngQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueHiPrioOnly.setStatus("current")


class _TQosIngQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosIngQueuePIRAdaptation based on TAdaptationRule"""


_TQosIngQueuePIRAdaptation_Object = MibTableColumn
tQosIngQueuePIRAdaptation = _TQosIngQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 13),
    _TQosIngQueuePIRAdaptation_Type()
)
tQosIngQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueuePIRAdaptation.setStatus("current")


class _TQosIngQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosIngQueueCIRAdaptation based on TAdaptationRule"""


_TQosIngQueueCIRAdaptation_Object = MibTableColumn
tQosIngQueueCIRAdaptation = _TQosIngQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 14),
    _TQosIngQueueCIRAdaptation_Type()
)
tQosIngQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueCIRAdaptation.setStatus("current")


class _TQosIngQueueAdminPIR_Type(TPIRRate):
    """Custom type tQosIngQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TQosIngQueueAdminPIR_Object = MibTableColumn
tQosIngQueueAdminPIR = _TQosIngQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 15),
    _TQosIngQueueAdminPIR_Type()
)
tQosIngQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngQueueAdminPIR.setUnits("kbps")


class _TQosIngQueueAdminCIR_Type(TCIRRate):
    """Custom type tQosIngQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TQosIngQueueAdminCIR_Object = MibTableColumn
tQosIngQueueAdminCIR = _TQosIngQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 16),
    _TQosIngQueueAdminCIR_Type()
)
tQosIngQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngQueueAdminCIR.setUnits("kbps")
_TQosIngQueueLastChanged_Type = TimeStamp
_TQosIngQueueLastChanged_Object = MibTableColumn
tQosIngQueueLastChanged = _TQosIngQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 17),
    _TQosIngQueueLastChanged_Type()
)
tQosIngQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngQueueLastChanged.setStatus("current")


class _TQosIngQueuePoliced_Type(TruthValue):
    """Custom type tQosIngQueuePoliced based on TruthValue"""


_TQosIngQueuePoliced_Object = MibTableColumn
tQosIngQueuePoliced = _TQosIngQueuePoliced_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 18),
    _TQosIngQueuePoliced_Type()
)
tQosIngQueuePoliced.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueuePoliced.setStatus("current")


class _TQosIngQueueMode_Type(TQueueMode):
    """Custom type tQosIngQueueMode based on TQueueMode"""


_TQosIngQueueMode_Object = MibTableColumn
tQosIngQueueMode = _TQosIngQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 19),
    _TQosIngQueueMode_Type()
)
tQosIngQueueMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueMode.setStatus("current")


class _TQosIngQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tQosIngQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosIngQueuePoolName_Object = MibTableColumn
tQosIngQueuePoolName = _TQosIngQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 20),
    _TQosIngQueuePoolName_Type()
)
tQosIngQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueuePoolName.setStatus("current")


class _TQosIngQueueMBSBytes_Type(TBurstSizeBytes):
    """Custom type tQosIngQueueMBSBytes based on TBurstSizeBytes"""
    defaultValue = -1


_TQosIngQueueMBSBytes_Object = MibTableColumn
tQosIngQueueMBSBytes = _TQosIngQueueMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 21),
    _TQosIngQueueMBSBytes_Type()
)
tQosIngQueueMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngQueueMBSBytes.setUnits("bytes")


class _TQosIngQueueBurstLimit_Type(TBurstLimit):
    """Custom type tQosIngQueueBurstLimit based on TBurstLimit"""
    defaultValue = -1


_TQosIngQueueBurstLimit_Object = MibTableColumn
tQosIngQueueBurstLimit = _TQosIngQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 22),
    _TQosIngQueueBurstLimit_Type()
)
tQosIngQueueBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngQueueBurstLimit.setUnits("bytes")


class _TQosIngQueueAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tQosIngQueueAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosIngQueueAdvCfgPolicy_Object = MibTableColumn
tQosIngQueueAdvCfgPolicy = _TQosIngQueueAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 5, 1, 23),
    _TQosIngQueueAdvCfgPolicy_Type()
)
tQosIngQueueAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngQueueAdvCfgPolicy.setStatus("current")
_TQosEgrQGroupTable_Object = MibTable
tQosEgrQGroupTable = _TQosEgrQGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6)
)
if mibBuilder.loadTexts:
    tQosEgrQGroupTable.setStatus("current")
_TQosEgrQGroupEntry_Object = MibTableRow
tQosEgrQGroupEntry = _TQosEgrQGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6, 1)
)
tQosEgrQGroupEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosEgrQGroupName"),
)
if mibBuilder.loadTexts:
    tQosEgrQGroupEntry.setStatus("current")
_TQosEgrQGroupName_Type = TNamedItem
_TQosEgrQGroupName_Object = MibTableColumn
tQosEgrQGroupName = _TQosEgrQGroupName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6, 1, 1),
    _TQosEgrQGroupName_Type()
)
tQosEgrQGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosEgrQGroupName.setStatus("current")
_TQosEgrQGroupRowStatus_Type = RowStatus
_TQosEgrQGroupRowStatus_Object = MibTableColumn
tQosEgrQGroupRowStatus = _TQosEgrQGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6, 1, 2),
    _TQosEgrQGroupRowStatus_Type()
)
tQosEgrQGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQGroupRowStatus.setStatus("current")
_TQosEgrQGroupLastChanged_Type = TimeStamp
_TQosEgrQGroupLastChanged_Object = MibTableColumn
tQosEgrQGroupLastChanged = _TQosEgrQGroupLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6, 1, 3),
    _TQosEgrQGroupLastChanged_Type()
)
tQosEgrQGroupLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQGroupLastChanged.setStatus("current")


class _TQosEgrQGroupDescr_Type(TItemDescription):
    """Custom type tQosEgrQGroupDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosEgrQGroupDescr_Object = MibTableColumn
tQosEgrQGroupDescr = _TQosEgrQGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 6, 1, 4),
    _TQosEgrQGroupDescr_Type()
)
tQosEgrQGroupDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQGroupDescr.setStatus("current")
_TQosEgrQueueTable_Object = MibTable
tQosEgrQueueTable = _TQosEgrQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7)
)
if mibBuilder.loadTexts:
    tQosEgrQueueTable.setStatus("current")
_TQosEgrQueueEntry_Object = MibTableRow
tQosEgrQueueEntry = _TQosEgrQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1)
)
tQosEgrQueueEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosEgrQGroupName"),
    (0, "TIMETRA-QOS-MIB", "tQosEgrQueue"),
)
if mibBuilder.loadTexts:
    tQosEgrQueueEntry.setStatus("current")


class _TQosEgrQueue_Type(TEgressQueueId):
    """Custom type tQosEgrQueue based on TEgressQueueId"""
    subtypeSpec = TEgressQueueId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TQosEgrQueue_Type.__name__ = "TEgressQueueId"
_TQosEgrQueue_Object = MibTableColumn
tQosEgrQueue = _TQosEgrQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 1),
    _TQosEgrQueue_Type()
)
tQosEgrQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosEgrQueue.setStatus("current")
_TQosEgrQueueRowStatus_Type = RowStatus
_TQosEgrQueueRowStatus_Object = MibTableColumn
tQosEgrQueueRowStatus = _TQosEgrQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 2),
    _TQosEgrQueueRowStatus_Type()
)
tQosEgrQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueRowStatus.setStatus("current")


class _TQosEgrQueueParent_Type(TNamedItemOrEmpty):
    """Custom type tQosEgrQueueParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosEgrQueueParent_Object = MibTableColumn
tQosEgrQueueParent = _TQosEgrQueueParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 3),
    _TQosEgrQueueParent_Type()
)
tQosEgrQueueParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueParent.setStatus("current")


class _TQosEgrQueueLevel_Type(TLevel):
    """Custom type tQosEgrQueueLevel based on TLevel"""
    defaultValue = 1


_TQosEgrQueueLevel_Object = MibTableColumn
tQosEgrQueueLevel = _TQosEgrQueueLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 4),
    _TQosEgrQueueLevel_Type()
)
tQosEgrQueueLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueLevel.setStatus("current")


class _TQosEgrQueueWeight_Type(TWeight):
    """Custom type tQosEgrQueueWeight based on TWeight"""
    defaultValue = 1


_TQosEgrQueueWeight_Object = MibTableColumn
tQosEgrQueueWeight = _TQosEgrQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 5),
    _TQosEgrQueueWeight_Type()
)
tQosEgrQueueWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueWeight.setStatus("current")


class _TQosEgrQueueCIRLevel_Type(TLevelOrDefault):
    """Custom type tQosEgrQueueCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TQosEgrQueueCIRLevel_Object = MibTableColumn
tQosEgrQueueCIRLevel = _TQosEgrQueueCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 6),
    _TQosEgrQueueCIRLevel_Type()
)
tQosEgrQueueCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueCIRLevel.setStatus("current")


class _TQosEgrQueueCIRWeight_Type(TWeight):
    """Custom type tQosEgrQueueCIRWeight based on TWeight"""
    defaultValue = 1


_TQosEgrQueueCIRWeight_Object = MibTableColumn
tQosEgrQueueCIRWeight = _TQosEgrQueueCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 7),
    _TQosEgrQueueCIRWeight_Type()
)
tQosEgrQueueCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueCIRWeight.setStatus("current")


class _TQosEgrQueueExpedite_Type(Integer32):
    """Custom type tQosEgrQueueExpedite based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bestEffort", 3),
          ("expedited", 1))
    )


_TQosEgrQueueExpedite_Type.__name__ = "Integer32"
_TQosEgrQueueExpedite_Object = MibTableColumn
tQosEgrQueueExpedite = _TQosEgrQueueExpedite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 8),
    _TQosEgrQueueExpedite_Type()
)
tQosEgrQueueExpedite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueExpedite.setStatus("current")


class _TQosEgrQueueCBS_Type(TBurstSize):
    """Custom type tQosEgrQueueCBS based on TBurstSize"""
    defaultValue = -1


_TQosEgrQueueCBS_Object = MibTableColumn
tQosEgrQueueCBS = _TQosEgrQueueCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 9),
    _TQosEgrQueueCBS_Type()
)
tQosEgrQueueCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueCBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueCBS.setUnits("kilo-bytes")


class _TQosEgrQueueMBS_Type(TBurstSize):
    """Custom type tQosEgrQueueMBS based on TBurstSize"""
    defaultValue = -1


_TQosEgrQueueMBS_Object = MibTableColumn
tQosEgrQueueMBS = _TQosEgrQueueMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 10),
    _TQosEgrQueueMBS_Type()
)
tQosEgrQueueMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueMBS.setStatus("obsolete")
if mibBuilder.loadTexts:
    tQosEgrQueueMBS.setUnits("kilo-bytes")


class _TQosEgrQueueHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tQosEgrQueueHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TQosEgrQueueHiPrioOnly_Object = MibTableColumn
tQosEgrQueueHiPrioOnly = _TQosEgrQueueHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 11),
    _TQosEgrQueueHiPrioOnly_Type()
)
tQosEgrQueueHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueHiPrioOnly.setStatus("current")


class _TQosEgrQueuePIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosEgrQueuePIRAdaptation based on TAdaptationRule"""


_TQosEgrQueuePIRAdaptation_Object = MibTableColumn
tQosEgrQueuePIRAdaptation = _TQosEgrQueuePIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 12),
    _TQosEgrQueuePIRAdaptation_Type()
)
tQosEgrQueuePIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePIRAdaptation.setStatus("current")


class _TQosEgrQueueCIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosEgrQueueCIRAdaptation based on TAdaptationRule"""


_TQosEgrQueueCIRAdaptation_Object = MibTableColumn
tQosEgrQueueCIRAdaptation = _TQosEgrQueueCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 13),
    _TQosEgrQueueCIRAdaptation_Type()
)
tQosEgrQueueCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueCIRAdaptation.setStatus("current")


class _TQosEgrQueueAdminPIR_Type(TPIRRate):
    """Custom type tQosEgrQueueAdminPIR based on TPIRRate"""
    defaultValue = -1


_TQosEgrQueueAdminPIR_Object = MibTableColumn
tQosEgrQueueAdminPIR = _TQosEgrQueueAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 14),
    _TQosEgrQueueAdminPIR_Type()
)
tQosEgrQueueAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminPIR.setUnits("kbps")


class _TQosEgrQueueAdminCIR_Type(TCIRRate):
    """Custom type tQosEgrQueueAdminCIR based on TCIRRate"""
    defaultValue = 0


_TQosEgrQueueAdminCIR_Object = MibTableColumn
tQosEgrQueueAdminCIR = _TQosEgrQueueAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 15),
    _TQosEgrQueueAdminCIR_Type()
)
tQosEgrQueueAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminCIR.setUnits("kbps")
_TQosEgrQueueLastChanged_Type = TimeStamp
_TQosEgrQueueLastChanged_Object = MibTableColumn
tQosEgrQueueLastChanged = _TQosEgrQueueLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 18),
    _TQosEgrQueueLastChanged_Type()
)
tQosEgrQueueLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQueueLastChanged.setStatus("current")


class _TQosEgrQueueUsePortParent_Type(TruthValue):
    """Custom type tQosEgrQueueUsePortParent based on TruthValue"""


_TQosEgrQueueUsePortParent_Object = MibTableColumn
tQosEgrQueueUsePortParent = _TQosEgrQueueUsePortParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 19),
    _TQosEgrQueueUsePortParent_Type()
)
tQosEgrQueueUsePortParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueUsePortParent.setStatus("current")


class _TQosEgrQueuePortLvl_Type(TLevel):
    """Custom type tQosEgrQueuePortLvl based on TLevel"""
    defaultValue = 1


_TQosEgrQueuePortLvl_Object = MibTableColumn
tQosEgrQueuePortLvl = _TQosEgrQueuePortLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 20),
    _TQosEgrQueuePortLvl_Type()
)
tQosEgrQueuePortLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePortLvl.setStatus("current")


class _TQosEgrQueuePortWght_Type(TWeight):
    """Custom type tQosEgrQueuePortWght based on TWeight"""
    defaultValue = 1


_TQosEgrQueuePortWght_Object = MibTableColumn
tQosEgrQueuePortWght = _TQosEgrQueuePortWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 21),
    _TQosEgrQueuePortWght_Type()
)
tQosEgrQueuePortWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePortWght.setStatus("current")


class _TQosEgrQueuePortCIRLvl_Type(TLevelOrDefault):
    """Custom type tQosEgrQueuePortCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TQosEgrQueuePortCIRLvl_Object = MibTableColumn
tQosEgrQueuePortCIRLvl = _TQosEgrQueuePortCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 22),
    _TQosEgrQueuePortCIRLvl_Type()
)
tQosEgrQueuePortCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePortCIRLvl.setStatus("current")


class _TQosEgrQueuePortCIRWght_Type(TWeight):
    """Custom type tQosEgrQueuePortCIRWght based on TWeight"""
    defaultValue = 0


_TQosEgrQueuePortCIRWght_Object = MibTableColumn
tQosEgrQueuePortCIRWght = _TQosEgrQueuePortCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 23),
    _TQosEgrQueuePortCIRWght_Type()
)
tQosEgrQueuePortCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePortCIRWght.setStatus("current")


class _TQosEgrQueuePoolName_Type(TNamedItemOrEmpty):
    """Custom type tQosEgrQueuePoolName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosEgrQueuePoolName_Object = MibTableColumn
tQosEgrQueuePoolName = _TQosEgrQueuePoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 24),
    _TQosEgrQueuePoolName_Type()
)
tQosEgrQueuePoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePoolName.setStatus("current")


class _TQosEgrQueueXPWredQ_Type(TruthValue):
    """Custom type tQosEgrQueueXPWredQ based on TruthValue"""


_TQosEgrQueueXPWredQ_Object = MibTableColumn
tQosEgrQueueXPWredQ = _TQosEgrQueueXPWredQ_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 25),
    _TQosEgrQueueXPWredQ_Type()
)
tQosEgrQueueXPWredQ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueXPWredQ.setStatus("current")


class _TQosEgrQueueXPWredQSlope_Type(TNamedItem):
    """Custom type tQosEgrQueueXPWredQSlope based on TNamedItem"""
    defaultValue = OctetString("default")


_TQosEgrQueueXPWredQSlope_Object = MibTableColumn
tQosEgrQueueXPWredQSlope = _TQosEgrQueueXPWredQSlope_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 26),
    _TQosEgrQueueXPWredQSlope_Type()
)
tQosEgrQueueXPWredQSlope.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueXPWredQSlope.setStatus("current")


class _TQosEgrQueueMBSBytes_Type(TBurstSizeBytes):
    """Custom type tQosEgrQueueMBSBytes based on TBurstSizeBytes"""
    defaultValue = -1


_TQosEgrQueueMBSBytes_Object = MibTableColumn
tQosEgrQueueMBSBytes = _TQosEgrQueueMBSBytes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 27),
    _TQosEgrQueueMBSBytes_Type()
)
tQosEgrQueueMBSBytes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueMBSBytes.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueMBSBytes.setUnits("bytes")


class _TQosEgrQueueAdminPIRPercent_Type(Unsigned32):
    """Custom type tQosEgrQueueAdminPIRPercent based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosEgrQueueAdminPIRPercent_Type.__name__ = "Unsigned32"
_TQosEgrQueueAdminPIRPercent_Object = MibTableColumn
tQosEgrQueueAdminPIRPercent = _TQosEgrQueueAdminPIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 28),
    _TQosEgrQueueAdminPIRPercent_Type()
)
tQosEgrQueueAdminPIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminPIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminPIRPercent.setUnits("hundredths of a percent")


class _TQosEgrQueueAdminCIRPercent_Type(Unsigned32):
    """Custom type tQosEgrQueueAdminCIRPercent based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TQosEgrQueueAdminCIRPercent_Type.__name__ = "Unsigned32"
_TQosEgrQueueAdminCIRPercent_Object = MibTableColumn
tQosEgrQueueAdminCIRPercent = _TQosEgrQueueAdminCIRPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 29),
    _TQosEgrQueueAdminCIRPercent_Type()
)
tQosEgrQueueAdminCIRPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminCIRPercent.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueAdminCIRPercent.setUnits("hundredths of a percent")


class _TQosEgrQueueRateType_Type(TRateType):
    """Custom type tQosEgrQueueRateType based on TRateType"""


_TQosEgrQueueRateType_Object = MibTableColumn
tQosEgrQueueRateType = _TQosEgrQueueRateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 30),
    _TQosEgrQueueRateType_Type()
)
tQosEgrQueueRateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueRateType.setStatus("current")


class _TQosEgrQueueBurstLimit_Type(TBurstLimit):
    """Custom type tQosEgrQueueBurstLimit based on TBurstLimit"""
    defaultValue = -1


_TQosEgrQueueBurstLimit_Object = MibTableColumn
tQosEgrQueueBurstLimit = _TQosEgrQueueBurstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 31),
    _TQosEgrQueueBurstLimit_Type()
)
tQosEgrQueueBurstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueBurstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrQueueBurstLimit.setUnits("bytes")


class _TQosEgrQueueAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tQosEgrQueueAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosEgrQueueAdvCfgPolicy_Object = MibTableColumn
tQosEgrQueueAdvCfgPolicy = _TQosEgrQueueAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 32),
    _TQosEgrQueueAdvCfgPolicy_Type()
)
tQosEgrQueueAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueueAdvCfgPolicy.setStatus("current")


class _TQosEgrQueuePktOffset_Type(TPerPacketOffset):
    """Custom type tQosEgrQueuePktOffset based on TPerPacketOffset"""
    defaultValue = 0


_TQosEgrQueuePktOffset_Object = MibTableColumn
tQosEgrQueuePktOffset = _TQosEgrQueuePktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 7, 1, 33),
    _TQosEgrQueuePktOffset_Type()
)
tQosEgrQueuePktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQueuePktOffset.setStatus("current")
_TQosEgrQGroupFCTable_Object = MibTable
tQosEgrQGroupFCTable = _TQosEgrQGroupFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8)
)
if mibBuilder.loadTexts:
    tQosEgrQGroupFCTable.setStatus("current")
_TQosEgrQGroupFCEntry_Object = MibTableRow
tQosEgrQGroupFCEntry = _TQosEgrQGroupFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8, 1)
)
tQosEgrQGroupFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosEgrQGroupName"),
    (0, "TIMETRA-QOS-MIB", "tQosEgrQGroupFCName"),
)
if mibBuilder.loadTexts:
    tQosEgrQGroupFCEntry.setStatus("current")
_TQosEgrQGroupFCName_Type = TFCName
_TQosEgrQGroupFCName_Object = MibTableColumn
tQosEgrQGroupFCName = _TQosEgrQGroupFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8, 1, 1),
    _TQosEgrQGroupFCName_Type()
)
tQosEgrQGroupFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosEgrQGroupFCName.setStatus("current")
_TQosEgrQGroupFCRowStatus_Type = RowStatus
_TQosEgrQGroupFCRowStatus_Object = MibTableColumn
tQosEgrQGroupFCRowStatus = _TQosEgrQGroupFCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8, 1, 2),
    _TQosEgrQGroupFCRowStatus_Type()
)
tQosEgrQGroupFCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQGroupFCRowStatus.setStatus("current")
_TQosEgrQGroupFCLastChanged_Type = TimeStamp
_TQosEgrQGroupFCLastChanged_Object = MibTableColumn
tQosEgrQGroupFCLastChanged = _TQosEgrQGroupFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8, 1, 3),
    _TQosEgrQGroupFCLastChanged_Type()
)
tQosEgrQGroupFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQGroupFCLastChanged.setStatus("current")


class _TQosEgrQGroupFCQueue_Type(TEgressQueueId):
    """Custom type tQosEgrQGroupFCQueue based on TEgressQueueId"""
    defaultValue = 0


_TQosEgrQGroupFCQueue_Object = MibTableColumn
tQosEgrQGroupFCQueue = _TQosEgrQGroupFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 7, 8, 1, 4),
    _TQosEgrQGroupFCQueue_Type()
)
tQosEgrQGroupFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrQGroupFCQueue.setStatus("current")
_TSlopeObjects_ObjectIdentity = ObjectIdentity
tSlopeObjects = _TSlopeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10)
)
_TSlopePolicyTable_Object = MibTable
tSlopePolicyTable = _TSlopePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1)
)
if mibBuilder.loadTexts:
    tSlopePolicyTable.setStatus("current")
_TSlopePolicyEntry_Object = MibTableRow
tSlopePolicyEntry = _TSlopePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1)
)
tSlopePolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSlopePolicy"),
)
if mibBuilder.loadTexts:
    tSlopePolicyEntry.setStatus("current")
_TSlopePolicy_Type = TNamedItem
_TSlopePolicy_Object = MibTableColumn
tSlopePolicy = _TSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 1),
    _TSlopePolicy_Type()
)
tSlopePolicy.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSlopePolicy.setStatus("current")
_TSlopeRowStatus_Type = RowStatus
_TSlopeRowStatus_Object = MibTableColumn
tSlopeRowStatus = _TSlopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 2),
    _TSlopeRowStatus_Type()
)
tSlopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeRowStatus.setStatus("current")


class _TSlopeDescription_Type(TItemDescription):
    """Custom type tSlopeDescription based on TItemDescription"""
    defaultHexValue = ""


_TSlopeDescription_Object = MibTableColumn
tSlopeDescription = _TSlopeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 3),
    _TSlopeDescription_Type()
)
tSlopeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeDescription.setStatus("current")


class _TSlopeHiAdminStatus_Type(Integer32):
    """Custom type tSlopeHiAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TSlopeHiAdminStatus_Type.__name__ = "Integer32"
_TSlopeHiAdminStatus_Object = MibTableColumn
tSlopeHiAdminStatus = _TSlopeHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 4),
    _TSlopeHiAdminStatus_Type()
)
tSlopeHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiAdminStatus.setStatus("current")


class _TSlopeHiStartAverage_Type(Unsigned32):
    """Custom type tSlopeHiStartAverage based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeHiStartAverage_Type.__name__ = "Unsigned32"
_TSlopeHiStartAverage_Object = MibTableColumn
tSlopeHiStartAverage = _TSlopeHiStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 5),
    _TSlopeHiStartAverage_Type()
)
tSlopeHiStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiStartAverage.setStatus("current")


class _TSlopeHiMaxAverage_Type(Unsigned32):
    """Custom type tSlopeHiMaxAverage based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeHiMaxAverage_Type.__name__ = "Unsigned32"
_TSlopeHiMaxAverage_Object = MibTableColumn
tSlopeHiMaxAverage = _TSlopeHiMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 6),
    _TSlopeHiMaxAverage_Type()
)
tSlopeHiMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiMaxAverage.setStatus("current")


class _TSlopeHiMaxProbability_Type(Unsigned32):
    """Custom type tSlopeHiMaxProbability based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeHiMaxProbability_Type.__name__ = "Unsigned32"
_TSlopeHiMaxProbability_Object = MibTableColumn
tSlopeHiMaxProbability = _TSlopeHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 7),
    _TSlopeHiMaxProbability_Type()
)
tSlopeHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeHiMaxProbability.setStatus("current")


class _TSlopeLoAdminStatus_Type(Integer32):
    """Custom type tSlopeLoAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_TSlopeLoAdminStatus_Type.__name__ = "Integer32"
_TSlopeLoAdminStatus_Object = MibTableColumn
tSlopeLoAdminStatus = _TSlopeLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 8),
    _TSlopeLoAdminStatus_Type()
)
tSlopeLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoAdminStatus.setStatus("current")


class _TSlopeLoStartAverage_Type(Unsigned32):
    """Custom type tSlopeLoStartAverage based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeLoStartAverage_Type.__name__ = "Unsigned32"
_TSlopeLoStartAverage_Object = MibTableColumn
tSlopeLoStartAverage = _TSlopeLoStartAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 9),
    _TSlopeLoStartAverage_Type()
)
tSlopeLoStartAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoStartAverage.setStatus("current")


class _TSlopeLoMaxAverage_Type(Unsigned32):
    """Custom type tSlopeLoMaxAverage based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeLoMaxAverage_Type.__name__ = "Unsigned32"
_TSlopeLoMaxAverage_Object = MibTableColumn
tSlopeLoMaxAverage = _TSlopeLoMaxAverage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 10),
    _TSlopeLoMaxAverage_Type()
)
tSlopeLoMaxAverage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoMaxAverage.setStatus("current")


class _TSlopeLoMaxProbability_Type(Unsigned32):
    """Custom type tSlopeLoMaxProbability based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TSlopeLoMaxProbability_Type.__name__ = "Unsigned32"
_TSlopeLoMaxProbability_Object = MibTableColumn
tSlopeLoMaxProbability = _TSlopeLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 11),
    _TSlopeLoMaxProbability_Type()
)
tSlopeLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeLoMaxProbability.setStatus("current")


class _TSlopeTimeAvgFactor_Type(Unsigned32):
    """Custom type tSlopeTimeAvgFactor based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TSlopeTimeAvgFactor_Type.__name__ = "Unsigned32"
_TSlopeTimeAvgFactor_Object = MibTableColumn
tSlopeTimeAvgFactor = _TSlopeTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 12),
    _TSlopeTimeAvgFactor_Type()
)
tSlopeTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSlopeTimeAvgFactor.setStatus("current")
_TSlopeLastChanged_Type = TimeStamp
_TSlopeLastChanged_Object = MibTableColumn
tSlopeLastChanged = _TSlopeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 1, 1, 13),
    _TSlopeLastChanged_Type()
)
tSlopeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSlopeLastChanged.setStatus("current")
_THsmdaSlopePolicyTable_Object = MibTable
tHsmdaSlopePolicyTable = _THsmdaSlopePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2)
)
if mibBuilder.loadTexts:
    tHsmdaSlopePolicyTable.setStatus("current")
_THsmdaSlopePolicyEntry_Object = MibTableRow
tHsmdaSlopePolicyEntry = _THsmdaSlopePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1)
)
tHsmdaSlopePolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tHsmdaSlopePolicyName"),
)
if mibBuilder.loadTexts:
    tHsmdaSlopePolicyEntry.setStatus("current")
_THsmdaSlopePolicyName_Type = TNamedItem
_THsmdaSlopePolicyName_Object = MibTableColumn
tHsmdaSlopePolicyName = _THsmdaSlopePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 1),
    _THsmdaSlopePolicyName_Type()
)
tHsmdaSlopePolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tHsmdaSlopePolicyName.setStatus("current")
_THsmdaSlopePolicyRowStatus_Type = RowStatus
_THsmdaSlopePolicyRowStatus_Object = MibTableColumn
tHsmdaSlopePolicyRowStatus = _THsmdaSlopePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 2),
    _THsmdaSlopePolicyRowStatus_Type()
)
tHsmdaSlopePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopePolicyRowStatus.setStatus("current")
_THsmdaSlopeLastChanged_Type = TimeStamp
_THsmdaSlopeLastChanged_Object = MibTableColumn
tHsmdaSlopeLastChanged = _THsmdaSlopeLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 3),
    _THsmdaSlopeLastChanged_Type()
)
tHsmdaSlopeLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaSlopeLastChanged.setStatus("current")
_THsmdaSlopeDescription_Type = TItemDescription
_THsmdaSlopeDescription_Object = MibTableColumn
tHsmdaSlopeDescription = _THsmdaSlopeDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 4),
    _THsmdaSlopeDescription_Type()
)
tHsmdaSlopeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeDescription.setStatus("current")


class _THsmdaSlopeQueueMbs_Type(Unsigned32):
    """Custom type tHsmdaSlopeQueueMbs based on Unsigned32"""
    defaultValue = 16800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500000),
    )


_THsmdaSlopeQueueMbs_Type.__name__ = "Unsigned32"
_THsmdaSlopeQueueMbs_Object = MibTableColumn
tHsmdaSlopeQueueMbs = _THsmdaSlopeQueueMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 5),
    _THsmdaSlopeQueueMbs_Type()
)
tHsmdaSlopeQueueMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeQueueMbs.setStatus("obsolete")
if mibBuilder.loadTexts:
    tHsmdaSlopeQueueMbs.setUnits("bytes")


class _THsmdaSlopeHiAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tHsmdaSlopeHiAdminStatus based on TmnxEnabledDisabled"""


_THsmdaSlopeHiAdminStatus_Object = MibTableColumn
tHsmdaSlopeHiAdminStatus = _THsmdaSlopeHiAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 6),
    _THsmdaSlopeHiAdminStatus_Type()
)
tHsmdaSlopeHiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiAdminStatus.setStatus("current")


class _THsmdaSlopeHiStartDepth_Type(Unsigned32):
    """Custom type tHsmdaSlopeHiStartDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeHiStartDepth_Type.__name__ = "Unsigned32"
_THsmdaSlopeHiStartDepth_Object = MibTableColumn
tHsmdaSlopeHiStartDepth = _THsmdaSlopeHiStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 7),
    _THsmdaSlopeHiStartDepth_Type()
)
tHsmdaSlopeHiStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiStartDepth.setUnits("hundredths of a percent")


class _THsmdaSlopeHiMaxDepth_Type(Unsigned32):
    """Custom type tHsmdaSlopeHiMaxDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeHiMaxDepth_Type.__name__ = "Unsigned32"
_THsmdaSlopeHiMaxDepth_Object = MibTableColumn
tHsmdaSlopeHiMaxDepth = _THsmdaSlopeHiMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 8),
    _THsmdaSlopeHiMaxDepth_Type()
)
tHsmdaSlopeHiMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiMaxDepth.setUnits("hundredths of a percent")


class _THsmdaSlopeHiMaxProbability_Type(Unsigned32):
    """Custom type tHsmdaSlopeHiMaxProbability based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeHiMaxProbability_Type.__name__ = "Unsigned32"
_THsmdaSlopeHiMaxProbability_Object = MibTableColumn
tHsmdaSlopeHiMaxProbability = _THsmdaSlopeHiMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 9),
    _THsmdaSlopeHiMaxProbability_Type()
)
tHsmdaSlopeHiMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiMaxProbability.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeHiMaxProbability.setUnits("hundredths of a percent")


class _THsmdaSlopeLoAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type tHsmdaSlopeLoAdminStatus based on TmnxEnabledDisabled"""


_THsmdaSlopeLoAdminStatus_Object = MibTableColumn
tHsmdaSlopeLoAdminStatus = _THsmdaSlopeLoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 10),
    _THsmdaSlopeLoAdminStatus_Type()
)
tHsmdaSlopeLoAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoAdminStatus.setStatus("current")


class _THsmdaSlopeLoStartDepth_Type(Unsigned32):
    """Custom type tHsmdaSlopeLoStartDepth based on Unsigned32"""
    defaultValue = 9000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeLoStartDepth_Type.__name__ = "Unsigned32"
_THsmdaSlopeLoStartDepth_Object = MibTableColumn
tHsmdaSlopeLoStartDepth = _THsmdaSlopeLoStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 11),
    _THsmdaSlopeLoStartDepth_Type()
)
tHsmdaSlopeLoStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoStartDepth.setUnits("hundredths of a percent")


class _THsmdaSlopeLoMaxDepth_Type(Unsigned32):
    """Custom type tHsmdaSlopeLoMaxDepth based on Unsigned32"""
    defaultValue = 9000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeLoMaxDepth_Type.__name__ = "Unsigned32"
_THsmdaSlopeLoMaxDepth_Object = MibTableColumn
tHsmdaSlopeLoMaxDepth = _THsmdaSlopeLoMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 12),
    _THsmdaSlopeLoMaxDepth_Type()
)
tHsmdaSlopeLoMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoMaxDepth.setUnits("hundredths of a percent")


class _THsmdaSlopeLoMaxProbability_Type(Unsigned32):
    """Custom type tHsmdaSlopeLoMaxProbability based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaSlopeLoMaxProbability_Type.__name__ = "Unsigned32"
_THsmdaSlopeLoMaxProbability_Object = MibTableColumn
tHsmdaSlopeLoMaxProbability = _THsmdaSlopeLoMaxProbability_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 10, 2, 1, 13),
    _THsmdaSlopeLoMaxProbability_Type()
)
tHsmdaSlopeLoMaxProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoMaxProbability.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSlopeLoMaxProbability.setUnits("hundredths of a percent")
_TSchedulerObjects_ObjectIdentity = ObjectIdentity
tSchedulerObjects = _TSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12)
)
_TSchedulerPolicyTable_Object = MibTable
tSchedulerPolicyTable = _TSchedulerPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1)
)
if mibBuilder.loadTexts:
    tSchedulerPolicyTable.setStatus("current")
_TSchedulerPolicyEntry_Object = MibTableRow
tSchedulerPolicyEntry = _TSchedulerPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1)
)
tSchedulerPolicyEntry.setIndexNames(
    (1, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
)
if mibBuilder.loadTexts:
    tSchedulerPolicyEntry.setStatus("current")
_TSchedulerPolicyName_Type = TNamedItem
_TSchedulerPolicyName_Object = MibTableColumn
tSchedulerPolicyName = _TSchedulerPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1, 1),
    _TSchedulerPolicyName_Type()
)
tSchedulerPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tSchedulerPolicyName.setStatus("current")
_TSchedulerPolicyRowStatus_Type = RowStatus
_TSchedulerPolicyRowStatus_Object = MibTableColumn
tSchedulerPolicyRowStatus = _TSchedulerPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1, 2),
    _TSchedulerPolicyRowStatus_Type()
)
tSchedulerPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSchedulerPolicyRowStatus.setStatus("current")


class _TSchedulerPolicyDescription_Type(TItemDescription):
    """Custom type tSchedulerPolicyDescription based on TItemDescription"""
    defaultHexValue = ""


_TSchedulerPolicyDescription_Object = MibTableColumn
tSchedulerPolicyDescription = _TSchedulerPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1, 3),
    _TSchedulerPolicyDescription_Type()
)
tSchedulerPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSchedulerPolicyDescription.setStatus("current")
_TSchedulerPolicyLastChanged_Type = TimeStamp
_TSchedulerPolicyLastChanged_Object = MibTableColumn
tSchedulerPolicyLastChanged = _TSchedulerPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1, 4),
    _TSchedulerPolicyLastChanged_Type()
)
tSchedulerPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSchedulerPolicyLastChanged.setStatus("current")


class _TSchedulerPolicyFrameBasedAccnt_Type(TruthValue):
    """Custom type tSchedulerPolicyFrameBasedAccnt based on TruthValue"""


_TSchedulerPolicyFrameBasedAccnt_Object = MibTableColumn
tSchedulerPolicyFrameBasedAccnt = _TSchedulerPolicyFrameBasedAccnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 1, 1, 5),
    _TSchedulerPolicyFrameBasedAccnt_Type()
)
tSchedulerPolicyFrameBasedAccnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSchedulerPolicyFrameBasedAccnt.setStatus("current")
_TVirtualSchedulerTable_Object = MibTable
tVirtualSchedulerTable = _TVirtualSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2)
)
if mibBuilder.loadTexts:
    tVirtualSchedulerTable.setStatus("current")
_TVirtualSchedulerEntry_Object = MibTableRow
tVirtualSchedulerEntry = _TVirtualSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1)
)
tVirtualSchedulerEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "TIMETRA-QOS-MIB", "tVirtualSchedulerTier"),
    (1, "TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
)
if mibBuilder.loadTexts:
    tVirtualSchedulerEntry.setStatus("current")


class _TVirtualSchedulerTier_Type(Integer32):
    """Custom type tVirtualSchedulerTier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TVirtualSchedulerTier_Type.__name__ = "Integer32"
_TVirtualSchedulerTier_Object = MibTableColumn
tVirtualSchedulerTier = _TVirtualSchedulerTier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 1),
    _TVirtualSchedulerTier_Type()
)
tVirtualSchedulerTier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVirtualSchedulerTier.setStatus("current")
_TVirtualSchedulerName_Type = TNamedItem
_TVirtualSchedulerName_Object = MibTableColumn
tVirtualSchedulerName = _TVirtualSchedulerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 2),
    _TVirtualSchedulerName_Type()
)
tVirtualSchedulerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tVirtualSchedulerName.setStatus("current")
_TVirtualSchedulerRowStatus_Type = RowStatus
_TVirtualSchedulerRowStatus_Object = MibTableColumn
tVirtualSchedulerRowStatus = _TVirtualSchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 3),
    _TVirtualSchedulerRowStatus_Type()
)
tVirtualSchedulerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerRowStatus.setStatus("current")


class _TVirtualSchedulerDescription_Type(TItemDescription):
    """Custom type tVirtualSchedulerDescription based on TItemDescription"""
    defaultHexValue = ""


_TVirtualSchedulerDescription_Object = MibTableColumn
tVirtualSchedulerDescription = _TVirtualSchedulerDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 4),
    _TVirtualSchedulerDescription_Type()
)
tVirtualSchedulerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerDescription.setStatus("current")


class _TVirtualSchedulerParent_Type(TNamedItemOrEmpty):
    """Custom type tVirtualSchedulerParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TVirtualSchedulerParent_Object = MibTableColumn
tVirtualSchedulerParent = _TVirtualSchedulerParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 5),
    _TVirtualSchedulerParent_Type()
)
tVirtualSchedulerParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerParent.setStatus("current")


class _TVirtualSchedulerLevel_Type(TLevel):
    """Custom type tVirtualSchedulerLevel based on TLevel"""
    defaultValue = 1


_TVirtualSchedulerLevel_Object = MibTableColumn
tVirtualSchedulerLevel = _TVirtualSchedulerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 6),
    _TVirtualSchedulerLevel_Type()
)
tVirtualSchedulerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerLevel.setStatus("current")


class _TVirtualSchedulerWeight_Type(TWeight):
    """Custom type tVirtualSchedulerWeight based on TWeight"""
    defaultValue = 1


_TVirtualSchedulerWeight_Object = MibTableColumn
tVirtualSchedulerWeight = _TVirtualSchedulerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 7),
    _TVirtualSchedulerWeight_Type()
)
tVirtualSchedulerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerWeight.setStatus("current")


class _TVirtualSchedulerCIRLevel_Type(TLevelOrDefault):
    """Custom type tVirtualSchedulerCIRLevel based on TLevelOrDefault"""
    defaultValue = 0


_TVirtualSchedulerCIRLevel_Object = MibTableColumn
tVirtualSchedulerCIRLevel = _TVirtualSchedulerCIRLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 8),
    _TVirtualSchedulerCIRLevel_Type()
)
tVirtualSchedulerCIRLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerCIRLevel.setStatus("current")


class _TVirtualSchedulerCIRWeight_Type(TWeight):
    """Custom type tVirtualSchedulerCIRWeight based on TWeight"""
    defaultValue = 1


_TVirtualSchedulerCIRWeight_Object = MibTableColumn
tVirtualSchedulerCIRWeight = _TVirtualSchedulerCIRWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 9),
    _TVirtualSchedulerCIRWeight_Type()
)
tVirtualSchedulerCIRWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerCIRWeight.setStatus("current")


class _TVirtualSchedulerPIR_Type(THPolVirtualSchePIRRate):
    """Custom type tVirtualSchedulerPIR based on THPolVirtualSchePIRRate"""
    defaultValue = -1


_TVirtualSchedulerPIR_Object = MibTableColumn
tVirtualSchedulerPIR = _TVirtualSchedulerPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 10),
    _TVirtualSchedulerPIR_Type()
)
tVirtualSchedulerPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerPIR.setStatus("current")
if mibBuilder.loadTexts:
    tVirtualSchedulerPIR.setUnits("kbps")


class _TVirtualSchedulerCIR_Type(THPolVirtualScheCIRRate):
    """Custom type tVirtualSchedulerCIR based on THPolVirtualScheCIRRate"""
    defaultValue = 0


_TVirtualSchedulerCIR_Object = MibTableColumn
tVirtualSchedulerCIR = _TVirtualSchedulerCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 11),
    _TVirtualSchedulerCIR_Type()
)
tVirtualSchedulerCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerCIR.setStatus("current")
if mibBuilder.loadTexts:
    tVirtualSchedulerCIR.setUnits("kbps")


class _TVirtualSchedulerSummedCIR_Type(TruthValue):
    """Custom type tVirtualSchedulerSummedCIR based on TruthValue"""


_TVirtualSchedulerSummedCIR_Object = MibTableColumn
tVirtualSchedulerSummedCIR = _TVirtualSchedulerSummedCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 12),
    _TVirtualSchedulerSummedCIR_Type()
)
tVirtualSchedulerSummedCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerSummedCIR.setStatus("current")
_TVirtualSchedulerLastChanged_Type = TimeStamp
_TVirtualSchedulerLastChanged_Object = MibTableColumn
tVirtualSchedulerLastChanged = _TVirtualSchedulerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 13),
    _TVirtualSchedulerLastChanged_Type()
)
tVirtualSchedulerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVirtualSchedulerLastChanged.setStatus("current")


class _TVirtualSchedulerUsePortParent_Type(TruthValue):
    """Custom type tVirtualSchedulerUsePortParent based on TruthValue"""


_TVirtualSchedulerUsePortParent_Object = MibTableColumn
tVirtualSchedulerUsePortParent = _TVirtualSchedulerUsePortParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 14),
    _TVirtualSchedulerUsePortParent_Type()
)
tVirtualSchedulerUsePortParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerUsePortParent.setStatus("current")


class _TVirtualSchedulerPortLvl_Type(TLevel):
    """Custom type tVirtualSchedulerPortLvl based on TLevel"""
    defaultValue = 1


_TVirtualSchedulerPortLvl_Object = MibTableColumn
tVirtualSchedulerPortLvl = _TVirtualSchedulerPortLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 15),
    _TVirtualSchedulerPortLvl_Type()
)
tVirtualSchedulerPortLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerPortLvl.setStatus("current")


class _TVirtualSchedulerPortWght_Type(TWeight):
    """Custom type tVirtualSchedulerPortWght based on TWeight"""
    defaultValue = 1


_TVirtualSchedulerPortWght_Object = MibTableColumn
tVirtualSchedulerPortWght = _TVirtualSchedulerPortWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 16),
    _TVirtualSchedulerPortWght_Type()
)
tVirtualSchedulerPortWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerPortWght.setStatus("current")


class _TVirtualSchedulerPortCIRLvl_Type(TLevelOrDefault):
    """Custom type tVirtualSchedulerPortCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TVirtualSchedulerPortCIRLvl_Object = MibTableColumn
tVirtualSchedulerPortCIRLvl = _TVirtualSchedulerPortCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 17),
    _TVirtualSchedulerPortCIRLvl_Type()
)
tVirtualSchedulerPortCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerPortCIRLvl.setStatus("current")


class _TVirtualSchedulerPortCIRWght_Type(TWeight):
    """Custom type tVirtualSchedulerPortCIRWght based on TWeight"""
    defaultValue = 0


_TVirtualSchedulerPortCIRWght_Object = MibTableColumn
tVirtualSchedulerPortCIRWght = _TVirtualSchedulerPortCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 2, 1, 18),
    _TVirtualSchedulerPortCIRWght_Type()
)
tVirtualSchedulerPortCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tVirtualSchedulerPortCIRWght.setStatus("current")
_TPortSchedulerPlcyTable_Object = MibTable
tPortSchedulerPlcyTable = _TPortSchedulerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3)
)
if mibBuilder.loadTexts:
    tPortSchedulerPlcyTable.setStatus("current")
_TPortSchedulerPlcyEntry_Object = MibTableRow
tPortSchedulerPlcyEntry = _TPortSchedulerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1)
)
tPortSchedulerPlcyEntry.setIndexNames(
    (1, "TIMETRA-QOS-MIB", "tPortSchedulerPlcyName"),
)
if mibBuilder.loadTexts:
    tPortSchedulerPlcyEntry.setStatus("current")
_TPortSchedulerPlcyName_Type = TNamedItem
_TPortSchedulerPlcyName_Object = MibTableColumn
tPortSchedulerPlcyName = _TPortSchedulerPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 1),
    _TPortSchedulerPlcyName_Type()
)
tPortSchedulerPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyName.setStatus("current")
_TPortSchedulerPlcyRowStatus_Type = RowStatus
_TPortSchedulerPlcyRowStatus_Object = MibTableColumn
tPortSchedulerPlcyRowStatus = _TPortSchedulerPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 2),
    _TPortSchedulerPlcyRowStatus_Type()
)
tPortSchedulerPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyRowStatus.setStatus("current")
_TPortSchedulerPlcyDescription_Type = TItemDescription
_TPortSchedulerPlcyDescription_Object = MibTableColumn
tPortSchedulerPlcyDescription = _TPortSchedulerPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 3),
    _TPortSchedulerPlcyDescription_Type()
)
tPortSchedulerPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyDescription.setStatus("current")
_TPortSchedulerPlcyLastChanged_Type = TimeStamp
_TPortSchedulerPlcyLastChanged_Object = MibTableColumn
tPortSchedulerPlcyLastChanged = _TPortSchedulerPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 4),
    _TPortSchedulerPlcyLastChanged_Type()
)
tPortSchedulerPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLastChanged.setStatus("current")


class _TPortSchedulerPlcyMaxRate_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyMaxRate based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyMaxRate_Object = MibTableColumn
tPortSchedulerPlcyMaxRate = _TPortSchedulerPlcyMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 5),
    _TPortSchedulerPlcyMaxRate_Type()
)
tPortSchedulerPlcyMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyMaxRate.setUnits("kbps")


class _TPortSchedulerPlcyLvl1PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl1PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl1PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl1PIR = _TPortSchedulerPlcyLvl1PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 6),
    _TPortSchedulerPlcyLvl1PIR_Type()
)
tPortSchedulerPlcyLvl1PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl1PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl1PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl1CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl1CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl1CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl1CIR = _TPortSchedulerPlcyLvl1CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 7),
    _TPortSchedulerPlcyLvl1CIR_Type()
)
tPortSchedulerPlcyLvl1CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl1CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl1CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl2PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl2PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl2PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl2PIR = _TPortSchedulerPlcyLvl2PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 8),
    _TPortSchedulerPlcyLvl2PIR_Type()
)
tPortSchedulerPlcyLvl2PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl2PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl2PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl2CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl2CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl2CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl2CIR = _TPortSchedulerPlcyLvl2CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 9),
    _TPortSchedulerPlcyLvl2CIR_Type()
)
tPortSchedulerPlcyLvl2CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl2CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl2CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl3PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl3PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl3PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl3PIR = _TPortSchedulerPlcyLvl3PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 10),
    _TPortSchedulerPlcyLvl3PIR_Type()
)
tPortSchedulerPlcyLvl3PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl3PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl3PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl3CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl3CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl3CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl3CIR = _TPortSchedulerPlcyLvl3CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 11),
    _TPortSchedulerPlcyLvl3CIR_Type()
)
tPortSchedulerPlcyLvl3CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl3CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl3CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl4PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl4PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl4PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl4PIR = _TPortSchedulerPlcyLvl4PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 12),
    _TPortSchedulerPlcyLvl4PIR_Type()
)
tPortSchedulerPlcyLvl4PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl4PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl4PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl4CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl4CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl4CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl4CIR = _TPortSchedulerPlcyLvl4CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 13),
    _TPortSchedulerPlcyLvl4CIR_Type()
)
tPortSchedulerPlcyLvl4CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl4CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl4CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl5PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl5PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl5PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl5PIR = _TPortSchedulerPlcyLvl5PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 14),
    _TPortSchedulerPlcyLvl5PIR_Type()
)
tPortSchedulerPlcyLvl5PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl5PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl5PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl5CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl5CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl5CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl5CIR = _TPortSchedulerPlcyLvl5CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 15),
    _TPortSchedulerPlcyLvl5CIR_Type()
)
tPortSchedulerPlcyLvl5CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl5CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl5CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl6PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl6PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl6PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl6PIR = _TPortSchedulerPlcyLvl6PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 16),
    _TPortSchedulerPlcyLvl6PIR_Type()
)
tPortSchedulerPlcyLvl6PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl6PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl6PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl6CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl6CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl6CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl6CIR = _TPortSchedulerPlcyLvl6CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 17),
    _TPortSchedulerPlcyLvl6CIR_Type()
)
tPortSchedulerPlcyLvl6CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl6CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl6CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl7PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl7PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl7PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl7PIR = _TPortSchedulerPlcyLvl7PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 18),
    _TPortSchedulerPlcyLvl7PIR_Type()
)
tPortSchedulerPlcyLvl7PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl7PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl7PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl7CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl7CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl7CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl7CIR = _TPortSchedulerPlcyLvl7CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 19),
    _TPortSchedulerPlcyLvl7CIR_Type()
)
tPortSchedulerPlcyLvl7CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl7CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl7CIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl8PIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchedulerPlcyLvl8PIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchedulerPlcyLvl8PIR_Object = MibTableColumn
tPortSchedulerPlcyLvl8PIR = _TPortSchedulerPlcyLvl8PIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 20),
    _TPortSchedulerPlcyLvl8PIR_Type()
)
tPortSchedulerPlcyLvl8PIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl8PIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl8PIR.setUnits("kbps")


class _TPortSchedulerPlcyLvl8CIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchedulerPlcyLvl8CIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchedulerPlcyLvl8CIR_Object = MibTableColumn
tPortSchedulerPlcyLvl8CIR = _TPortSchedulerPlcyLvl8CIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 21),
    _TPortSchedulerPlcyLvl8CIR_Type()
)
tPortSchedulerPlcyLvl8CIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl8CIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyLvl8CIR.setUnits("kbps")


class _TPortSchedulerPlcyOrphanLvl_Type(TLevel):
    """Custom type tPortSchedulerPlcyOrphanLvl based on TLevel"""
    defaultValue = 1


_TPortSchedulerPlcyOrphanLvl_Object = MibTableColumn
tPortSchedulerPlcyOrphanLvl = _TPortSchedulerPlcyOrphanLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 22),
    _TPortSchedulerPlcyOrphanLvl_Type()
)
tPortSchedulerPlcyOrphanLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyOrphanLvl.setStatus("current")


class _TPortSchedulerPlcyOrphanWeight_Type(TWeight):
    """Custom type tPortSchedulerPlcyOrphanWeight based on TWeight"""
    defaultValue = 0


_TPortSchedulerPlcyOrphanWeight_Object = MibTableColumn
tPortSchedulerPlcyOrphanWeight = _TPortSchedulerPlcyOrphanWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 23),
    _TPortSchedulerPlcyOrphanWeight_Type()
)
tPortSchedulerPlcyOrphanWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyOrphanWeight.setStatus("current")


class _TPortSchedulerPlcyOrphanCIRLvl_Type(TLevelOrDefault):
    """Custom type tPortSchedulerPlcyOrphanCIRLvl based on TLevelOrDefault"""
    defaultValue = 0


_TPortSchedulerPlcyOrphanCIRLvl_Object = MibTableColumn
tPortSchedulerPlcyOrphanCIRLvl = _TPortSchedulerPlcyOrphanCIRLvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 24),
    _TPortSchedulerPlcyOrphanCIRLvl_Type()
)
tPortSchedulerPlcyOrphanCIRLvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyOrphanCIRLvl.setStatus("current")


class _TPortSchedulerPlcyOrphanCIRWght_Type(TWeight):
    """Custom type tPortSchedulerPlcyOrphanCIRWght based on TWeight"""
    defaultValue = 0


_TPortSchedulerPlcyOrphanCIRWght_Object = MibTableColumn
tPortSchedulerPlcyOrphanCIRWght = _TPortSchedulerPlcyOrphanCIRWght_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 3, 1, 25),
    _TPortSchedulerPlcyOrphanCIRWght_Type()
)
tPortSchedulerPlcyOrphanCIRWght.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchedulerPlcyOrphanCIRWght.setStatus("current")
_THsmdaSchedulerPlcyTable_Object = MibTable
tHsmdaSchedulerPlcyTable = _THsmdaSchedulerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4)
)
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyTable.setStatus("current")
_THsmdaSchedulerPlcyEntry_Object = MibTableRow
tHsmdaSchedulerPlcyEntry = _THsmdaSchedulerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1)
)
tHsmdaSchedulerPlcyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyName"),
)
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyEntry.setStatus("current")
_THsmdaSchedulerPlcyName_Type = TNamedItem
_THsmdaSchedulerPlcyName_Object = MibTableColumn
tHsmdaSchedulerPlcyName = _THsmdaSchedulerPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 1),
    _THsmdaSchedulerPlcyName_Type()
)
tHsmdaSchedulerPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyName.setStatus("current")
_THsmdaSchedulerPlcyRowStatus_Type = RowStatus
_THsmdaSchedulerPlcyRowStatus_Object = MibTableColumn
tHsmdaSchedulerPlcyRowStatus = _THsmdaSchedulerPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 2),
    _THsmdaSchedulerPlcyRowStatus_Type()
)
tHsmdaSchedulerPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyRowStatus.setStatus("current")
_THsmdaSchedulerPlcyDescription_Type = TItemDescription
_THsmdaSchedulerPlcyDescription_Object = MibTableColumn
tHsmdaSchedulerPlcyDescription = _THsmdaSchedulerPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 3),
    _THsmdaSchedulerPlcyDescription_Type()
)
tHsmdaSchedulerPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyDescription.setStatus("current")


class _THsmdaSchedulerPlcyMaxRate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyMaxRate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyMaxRate_Object = MibTableColumn
tHsmdaSchedulerPlcyMaxRate = _THsmdaSchedulerPlcyMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 4),
    _THsmdaSchedulerPlcyMaxRate_Type()
)
tHsmdaSchedulerPlcyMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyMaxRate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl1Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl1Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl1Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl1Rate = _THsmdaSchedulerPlcyLvl1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 5),
    _THsmdaSchedulerPlcyLvl1Rate_Type()
)
tHsmdaSchedulerPlcyLvl1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl1GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl1GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl1GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl1GrpId = _THsmdaSchedulerPlcyLvl1GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 6),
    _THsmdaSchedulerPlcyLvl1GrpId_Type()
)
tHsmdaSchedulerPlcyLvl1GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl1WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl1WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl1WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl1WgtInGrp = _THsmdaSchedulerPlcyLvl1WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 7),
    _THsmdaSchedulerPlcyLvl1WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl1WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl2Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl2Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl2Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl2Rate = _THsmdaSchedulerPlcyLvl2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 8),
    _THsmdaSchedulerPlcyLvl2Rate_Type()
)
tHsmdaSchedulerPlcyLvl2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl2GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl2GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl2GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl2GrpId = _THsmdaSchedulerPlcyLvl2GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 9),
    _THsmdaSchedulerPlcyLvl2GrpId_Type()
)
tHsmdaSchedulerPlcyLvl2GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl2WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl2WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl2WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl2WgtInGrp = _THsmdaSchedulerPlcyLvl2WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 10),
    _THsmdaSchedulerPlcyLvl2WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl2WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl3Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl3Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl3Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl3Rate = _THsmdaSchedulerPlcyLvl3Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 11),
    _THsmdaSchedulerPlcyLvl3Rate_Type()
)
tHsmdaSchedulerPlcyLvl3Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl3GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl3GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl3GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl3GrpId = _THsmdaSchedulerPlcyLvl3GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 12),
    _THsmdaSchedulerPlcyLvl3GrpId_Type()
)
tHsmdaSchedulerPlcyLvl3GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl3WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl3WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl3WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl3WgtInGrp = _THsmdaSchedulerPlcyLvl3WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 13),
    _THsmdaSchedulerPlcyLvl3WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl3WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl4Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl4Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl4Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl4Rate = _THsmdaSchedulerPlcyLvl4Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 14),
    _THsmdaSchedulerPlcyLvl4Rate_Type()
)
tHsmdaSchedulerPlcyLvl4Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl4GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl4GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl4GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl4GrpId = _THsmdaSchedulerPlcyLvl4GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 15),
    _THsmdaSchedulerPlcyLvl4GrpId_Type()
)
tHsmdaSchedulerPlcyLvl4GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl4WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl4WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl4WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl4WgtInGrp = _THsmdaSchedulerPlcyLvl4WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 16),
    _THsmdaSchedulerPlcyLvl4WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl4WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl5Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl5Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl5Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl5Rate = _THsmdaSchedulerPlcyLvl5Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 17),
    _THsmdaSchedulerPlcyLvl5Rate_Type()
)
tHsmdaSchedulerPlcyLvl5Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl5GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl5GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl5GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl5GrpId = _THsmdaSchedulerPlcyLvl5GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 18),
    _THsmdaSchedulerPlcyLvl5GrpId_Type()
)
tHsmdaSchedulerPlcyLvl5GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl5WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl5WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl5WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl5WgtInGrp = _THsmdaSchedulerPlcyLvl5WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 19),
    _THsmdaSchedulerPlcyLvl5WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl5WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl6Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl6Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl6Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl6Rate = _THsmdaSchedulerPlcyLvl6Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 20),
    _THsmdaSchedulerPlcyLvl6Rate_Type()
)
tHsmdaSchedulerPlcyLvl6Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl6GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl6GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl6GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl6GrpId = _THsmdaSchedulerPlcyLvl6GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 21),
    _THsmdaSchedulerPlcyLvl6GrpId_Type()
)
tHsmdaSchedulerPlcyLvl6GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl6WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl6WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl6WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl6WgtInGrp = _THsmdaSchedulerPlcyLvl6WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 22),
    _THsmdaSchedulerPlcyLvl6WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl6WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl7Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl7Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl7Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl7Rate = _THsmdaSchedulerPlcyLvl7Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 23),
    _THsmdaSchedulerPlcyLvl7Rate_Type()
)
tHsmdaSchedulerPlcyLvl7Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl7GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl7GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl7GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl7GrpId = _THsmdaSchedulerPlcyLvl7GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 24),
    _THsmdaSchedulerPlcyLvl7GrpId_Type()
)
tHsmdaSchedulerPlcyLvl7GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl7WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl7WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl7WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl7WgtInGrp = _THsmdaSchedulerPlcyLvl7WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 25),
    _THsmdaSchedulerPlcyLvl7WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl7WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7WgtInGrp.setStatus("current")


class _THsmdaSchedulerPlcyLvl8Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyLvl8Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl8Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl8Rate = _THsmdaSchedulerPlcyLvl8Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 26),
    _THsmdaSchedulerPlcyLvl8Rate_Type()
)
tHsmdaSchedulerPlcyLvl8Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyLvl8GrpId_Type(THsmdaSchedulerPolicyGroupId):
    """Custom type tHsmdaSchedulerPlcyLvl8GrpId based on THsmdaSchedulerPolicyGroupId"""
    defaultValue = 0


_THsmdaSchedulerPlcyLvl8GrpId_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl8GrpId = _THsmdaSchedulerPlcyLvl8GrpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 27),
    _THsmdaSchedulerPlcyLvl8GrpId_Type()
)
tHsmdaSchedulerPlcyLvl8GrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8GrpId.setStatus("current")


class _THsmdaSchedulerPlcyLvl8WgtInGrp_Type(THsmdaWeight):
    """Custom type tHsmdaSchedulerPlcyLvl8WgtInGrp based on THsmdaWeight"""
    defaultValue = 1


_THsmdaSchedulerPlcyLvl8WgtInGrp_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl8WgtInGrp = _THsmdaSchedulerPlcyLvl8WgtInGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 28),
    _THsmdaSchedulerPlcyLvl8WgtInGrp_Type()
)
tHsmdaSchedulerPlcyLvl8WgtInGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8WgtInGrp.setStatus("current")
_THsmdaSchedulerPlcyLastChanged_Type = TimeStamp
_THsmdaSchedulerPlcyLastChanged_Object = MibTableColumn
tHsmdaSchedulerPlcyLastChanged = _THsmdaSchedulerPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 29),
    _THsmdaSchedulerPlcyLastChanged_Type()
)
tHsmdaSchedulerPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLastChanged.setStatus("current")


class _THsmdaSchedulerPlcyGrp1Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyGrp1Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyGrp1Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyGrp1Rate = _THsmdaSchedulerPlcyGrp1Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 30),
    _THsmdaSchedulerPlcyGrp1Rate_Type()
)
tHsmdaSchedulerPlcyGrp1Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp1Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp1Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyGrp2Rate_Type(THsmdaPIRMRate):
    """Custom type tHsmdaSchedulerPlcyGrp2Rate based on THsmdaPIRMRate"""
    defaultValue = -1


_THsmdaSchedulerPlcyGrp2Rate_Object = MibTableColumn
tHsmdaSchedulerPlcyGrp2Rate = _THsmdaSchedulerPlcyGrp2Rate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 31),
    _THsmdaSchedulerPlcyGrp2Rate_Type()
)
tHsmdaSchedulerPlcyGrp2Rate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp2Rate.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp2Rate.setUnits("Mbps")


class _THsmdaSchedulerPlcyBrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyBrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyBrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyBrstLimit = _THsmdaSchedulerPlcyBrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 32),
    _THsmdaSchedulerPlcyBrstLimit_Type()
)
tHsmdaSchedulerPlcyBrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyBrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyBrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyGrp1BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyGrp1BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyGrp1BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyGrp1BrstLimit = _THsmdaSchedulerPlcyGrp1BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 33),
    _THsmdaSchedulerPlcyGrp1BrstLimit_Type()
)
tHsmdaSchedulerPlcyGrp1BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp1BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp1BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyGrp2BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyGrp2BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyGrp2BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyGrp2BrstLimit = _THsmdaSchedulerPlcyGrp2BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 34),
    _THsmdaSchedulerPlcyGrp2BrstLimit_Type()
)
tHsmdaSchedulerPlcyGrp2BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp2BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyGrp2BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl1BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl1BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl1BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl1BrstLimit = _THsmdaSchedulerPlcyLvl1BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 35),
    _THsmdaSchedulerPlcyLvl1BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl1BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl1BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl2BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl2BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl2BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl2BrstLimit = _THsmdaSchedulerPlcyLvl2BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 36),
    _THsmdaSchedulerPlcyLvl2BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl2BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl2BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl3BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl3BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl3BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl3BrstLimit = _THsmdaSchedulerPlcyLvl3BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 37),
    _THsmdaSchedulerPlcyLvl3BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl3BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl3BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl4BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl4BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl4BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl4BrstLimit = _THsmdaSchedulerPlcyLvl4BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 38),
    _THsmdaSchedulerPlcyLvl4BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl4BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl4BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl5BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl5BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl5BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl5BrstLimit = _THsmdaSchedulerPlcyLvl5BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 39),
    _THsmdaSchedulerPlcyLvl5BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl5BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl5BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl6BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl6BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl6BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl6BrstLimit = _THsmdaSchedulerPlcyLvl6BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 40),
    _THsmdaSchedulerPlcyLvl6BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl6BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl6BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl7BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl7BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl7BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl7BrstLimit = _THsmdaSchedulerPlcyLvl7BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 41),
    _THsmdaSchedulerPlcyLvl7BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl7BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl7BrstLimit.setUnits("bytes")


class _THsmdaSchedulerPlcyLvl8BrstLimit_Type(TClassBurstLimit):
    """Custom type tHsmdaSchedulerPlcyLvl8BrstLimit based on TClassBurstLimit"""
    defaultValue = -1


_THsmdaSchedulerPlcyLvl8BrstLimit_Object = MibTableColumn
tHsmdaSchedulerPlcyLvl8BrstLimit = _THsmdaSchedulerPlcyLvl8BrstLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 4, 1, 42),
    _THsmdaSchedulerPlcyLvl8BrstLimit_Type()
)
tHsmdaSchedulerPlcyLvl8BrstLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8BrstLimit.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaSchedulerPlcyLvl8BrstLimit.setUnits("bytes")
_TPortSchPlcyGrpTable_Object = MibTable
tPortSchPlcyGrpTable = _TPortSchPlcyGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5)
)
if mibBuilder.loadTexts:
    tPortSchPlcyGrpTable.setStatus("current")
_TPortSchPlcyGrpEntry_Object = MibTableRow
tPortSchPlcyGrpEntry = _TPortSchPlcyGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1)
)
tPortSchPlcyGrpEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tPortSchedulerPlcyName"),
    (0, "TIMETRA-QOS-MIB", "tPortSchPlcyGrpName"),
)
if mibBuilder.loadTexts:
    tPortSchPlcyGrpEntry.setStatus("current")
_TPortSchPlcyGrpName_Type = TNamedItem
_TPortSchPlcyGrpName_Object = MibTableColumn
tPortSchPlcyGrpName = _TPortSchPlcyGrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1, 1),
    _TPortSchPlcyGrpName_Type()
)
tPortSchPlcyGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpName.setStatus("current")
_TPortSchPlcyGrpRowStatus_Type = RowStatus
_TPortSchPlcyGrpRowStatus_Object = MibTableColumn
tPortSchPlcyGrpRowStatus = _TPortSchPlcyGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1, 2),
    _TPortSchPlcyGrpRowStatus_Type()
)
tPortSchPlcyGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpRowStatus.setStatus("current")
_TPortSchPlcyGrpLastChanged_Type = TimeStamp
_TPortSchPlcyGrpLastChanged_Object = MibTableColumn
tPortSchPlcyGrpLastChanged = _TPortSchPlcyGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1, 3),
    _TPortSchPlcyGrpLastChanged_Type()
)
tPortSchPlcyGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpLastChanged.setStatus("current")


class _TPortSchPlcyGrpAdminPIR_Type(TPortSchedulerPIRRate):
    """Custom type tPortSchPlcyGrpAdminPIR based on TPortSchedulerPIRRate"""
    defaultValue = -1


_TPortSchPlcyGrpAdminPIR_Object = MibTableColumn
tPortSchPlcyGrpAdminPIR = _TPortSchPlcyGrpAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1, 4),
    _TPortSchPlcyGrpAdminPIR_Type()
)
tPortSchPlcyGrpAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpAdminPIR.setUnits("kbps")


class _TPortSchPlcyGrpAdminCIR_Type(TPortSchedulerCIR):
    """Custom type tPortSchPlcyGrpAdminCIR based on TPortSchedulerCIR"""
    defaultValue = -1


_TPortSchPlcyGrpAdminCIR_Object = MibTableColumn
tPortSchPlcyGrpAdminCIR = _TPortSchPlcyGrpAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 5, 1, 5),
    _TPortSchPlcyGrpAdminCIR_Type()
)
tPortSchPlcyGrpAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpAdminCIR.setUnits("kbps")
_TPortSchPlcyLvlGrpTable_Object = MibTable
tPortSchPlcyLvlGrpTable = _TPortSchPlcyLvlGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6)
)
if mibBuilder.loadTexts:
    tPortSchPlcyLvlGrpTable.setStatus("current")
_TPortSchPlcyLvlGrpEntry_Object = MibTableRow
tPortSchPlcyLvlGrpEntry = _TPortSchPlcyLvlGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1)
)
if mibBuilder.loadTexts:
    tPortSchPlcyLvlGrpEntry.setStatus("current")
_TPortSchPlcyLvlGrpLastChanged_Type = TimeStamp
_TPortSchPlcyLvlGrpLastChanged_Object = MibTableColumn
tPortSchPlcyLvlGrpLastChanged = _TPortSchPlcyLvlGrpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 1),
    _TPortSchPlcyLvlGrpLastChanged_Type()
)
tPortSchPlcyLvlGrpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortSchPlcyLvlGrpLastChanged.setStatus("current")


class _TPortSchPlcyLvl1GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl1GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl1GrpName_Object = MibTableColumn
tPortSchPlcyLvl1GrpName = _TPortSchPlcyLvl1GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 2),
    _TPortSchPlcyLvl1GrpName_Type()
)
tPortSchPlcyLvl1GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl1GrpName.setStatus("current")


class _TPortSchPlcyLvl2GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl2GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl2GrpName_Object = MibTableColumn
tPortSchPlcyLvl2GrpName = _TPortSchPlcyLvl2GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 3),
    _TPortSchPlcyLvl2GrpName_Type()
)
tPortSchPlcyLvl2GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl2GrpName.setStatus("current")


class _TPortSchPlcyLvl3GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl3GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl3GrpName_Object = MibTableColumn
tPortSchPlcyLvl3GrpName = _TPortSchPlcyLvl3GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 4),
    _TPortSchPlcyLvl3GrpName_Type()
)
tPortSchPlcyLvl3GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl3GrpName.setStatus("current")


class _TPortSchPlcyLvl4GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl4GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl4GrpName_Object = MibTableColumn
tPortSchPlcyLvl4GrpName = _TPortSchPlcyLvl4GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 5),
    _TPortSchPlcyLvl4GrpName_Type()
)
tPortSchPlcyLvl4GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl4GrpName.setStatus("current")


class _TPortSchPlcyLvl5GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl5GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl5GrpName_Object = MibTableColumn
tPortSchPlcyLvl5GrpName = _TPortSchPlcyLvl5GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 6),
    _TPortSchPlcyLvl5GrpName_Type()
)
tPortSchPlcyLvl5GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl5GrpName.setStatus("current")


class _TPortSchPlcyLvl6GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl6GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl6GrpName_Object = MibTableColumn
tPortSchPlcyLvl6GrpName = _TPortSchPlcyLvl6GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 7),
    _TPortSchPlcyLvl6GrpName_Type()
)
tPortSchPlcyLvl6GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl6GrpName.setStatus("current")


class _TPortSchPlcyLvl7GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl7GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl7GrpName_Object = MibTableColumn
tPortSchPlcyLvl7GrpName = _TPortSchPlcyLvl7GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 8),
    _TPortSchPlcyLvl7GrpName_Type()
)
tPortSchPlcyLvl7GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl7GrpName.setStatus("current")


class _TPortSchPlcyLvl8GrpName_Type(TNamedItemOrEmpty):
    """Custom type tPortSchPlcyLvl8GrpName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TPortSchPlcyLvl8GrpName_Object = MibTableColumn
tPortSchPlcyLvl8GrpName = _TPortSchPlcyLvl8GrpName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 9),
    _TPortSchPlcyLvl8GrpName_Type()
)
tPortSchPlcyLvl8GrpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl8GrpName.setStatus("current")


class _TPortSchPlcyLvl1GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl1GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl1GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl1GrpWeight = _TPortSchPlcyLvl1GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 10),
    _TPortSchPlcyLvl1GrpWeight_Type()
)
tPortSchPlcyLvl1GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl1GrpWeight.setStatus("current")


class _TPortSchPlcyLvl2GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl2GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl2GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl2GrpWeight = _TPortSchPlcyLvl2GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 11),
    _TPortSchPlcyLvl2GrpWeight_Type()
)
tPortSchPlcyLvl2GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl2GrpWeight.setStatus("current")


class _TPortSchPlcyLvl3GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl3GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl3GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl3GrpWeight = _TPortSchPlcyLvl3GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 12),
    _TPortSchPlcyLvl3GrpWeight_Type()
)
tPortSchPlcyLvl3GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl3GrpWeight.setStatus("current")


class _TPortSchPlcyLvl4GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl4GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl4GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl4GrpWeight = _TPortSchPlcyLvl4GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 13),
    _TPortSchPlcyLvl4GrpWeight_Type()
)
tPortSchPlcyLvl4GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl4GrpWeight.setStatus("current")


class _TPortSchPlcyLvl5GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl5GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl5GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl5GrpWeight = _TPortSchPlcyLvl5GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 14),
    _TPortSchPlcyLvl5GrpWeight_Type()
)
tPortSchPlcyLvl5GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl5GrpWeight.setStatus("current")


class _TPortSchPlcyLvl6GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl6GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl6GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl6GrpWeight = _TPortSchPlcyLvl6GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 15),
    _TPortSchPlcyLvl6GrpWeight_Type()
)
tPortSchPlcyLvl6GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl6GrpWeight.setStatus("current")


class _TPortSchPlcyLvl7GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl7GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl7GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl7GrpWeight = _TPortSchPlcyLvl7GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 16),
    _TPortSchPlcyLvl7GrpWeight_Type()
)
tPortSchPlcyLvl7GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl7GrpWeight.setStatus("current")


class _TPortSchPlcyLvl8GrpWeight_Type(TNonZeroWeight):
    """Custom type tPortSchPlcyLvl8GrpWeight based on TNonZeroWeight"""
    defaultValue = 1


_TPortSchPlcyLvl8GrpWeight_Object = MibTableColumn
tPortSchPlcyLvl8GrpWeight = _TPortSchPlcyLvl8GrpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 12, 6, 1, 17),
    _TPortSchPlcyLvl8GrpWeight_Type()
)
tPortSchPlcyLvl8GrpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tPortSchPlcyLvl8GrpWeight.setStatus("current")
_TQosTimeStampObjects_ObjectIdentity = ObjectIdentity
tQosTimeStampObjects = _TQosTimeStampObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20)
)
_TQosDomainLastChanged_Type = TimeStamp
_TQosDomainLastChanged_Object = MibScalar
tQosDomainLastChanged = _TQosDomainLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 1),
    _TQosDomainLastChanged_Type()
)
tQosDomainLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosDomainLastChanged.setStatus("current")
_TDSCPNameTableLastChanged_Type = TimeStamp
_TDSCPNameTableLastChanged_Object = MibScalar
tDSCPNameTableLastChanged = _TDSCPNameTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 5),
    _TDSCPNameTableLastChanged_Type()
)
tDSCPNameTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tDSCPNameTableLastChanged.setStatus("current")
_TQosIngQGroupTableLastChanged_Type = TimeStamp
_TQosIngQGroupTableLastChanged_Object = MibScalar
tQosIngQGroupTableLastChanged = _TQosIngQGroupTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 6),
    _TQosIngQGroupTableLastChanged_Type()
)
tQosIngQGroupTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngQGroupTableLastChanged.setStatus("current")
_TQosIngQTableLastChanged_Type = TimeStamp
_TQosIngQTableLastChanged_Object = MibScalar
tQosIngQTableLastChanged = _TQosIngQTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 7),
    _TQosIngQTableLastChanged_Type()
)
tQosIngQTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngQTableLastChanged.setStatus("current")
_TQosEgrQGroupTableLastChanged_Type = TimeStamp
_TQosEgrQGroupTableLastChanged_Object = MibScalar
tQosEgrQGroupTableLastChanged = _TQosEgrQGroupTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 8),
    _TQosEgrQGroupTableLastChanged_Type()
)
tQosEgrQGroupTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQGroupTableLastChanged.setStatus("current")
_TQosEgrQTableLastChanged_Type = TimeStamp
_TQosEgrQTableLastChanged_Object = MibScalar
tQosEgrQTableLastChanged = _TQosEgrQTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 9),
    _TQosEgrQTableLastChanged_Type()
)
tQosEgrQTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQTableLastChanged.setStatus("current")
_TFCNameTableLastChanged_Type = TimeStamp
_TFCNameTableLastChanged_Object = MibScalar
tFCNameTableLastChanged = _TFCNameTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 10),
    _TFCNameTableLastChanged_Type()
)
tFCNameTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tFCNameTableLastChanged.setStatus("current")
_TSapIngressTableLastChanged_Type = TimeStamp
_TSapIngressTableLastChanged_Object = MibScalar
tSapIngressTableLastChanged = _TSapIngressTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 20),
    _TSapIngressTableLastChanged_Type()
)
tSapIngressTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressTableLastChanged.setStatus("current")
_TSapIngressQueueTableLastChanged_Type = TimeStamp
_TSapIngressQueueTableLastChanged_Object = MibScalar
tSapIngressQueueTableLastChanged = _TSapIngressQueueTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 21),
    _TSapIngressQueueTableLastChanged_Type()
)
tSapIngressQueueTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressQueueTableLastChanged.setStatus("current")
_TSapIngressDSCPTableLastChanged_Type = TimeStamp
_TSapIngressDSCPTableLastChanged_Object = MibScalar
tSapIngressDSCPTableLastChanged = _TSapIngressDSCPTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 22),
    _TSapIngressDSCPTableLastChanged_Type()
)
tSapIngressDSCPTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressDSCPTableLastChanged.setStatus("current")
_TSapIngressDot1pTableLastChanged_Type = TimeStamp
_TSapIngressDot1pTableLastChanged_Object = MibScalar
tSapIngressDot1pTableLastChanged = _TSapIngressDot1pTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 23),
    _TSapIngressDot1pTableLastChanged_Type()
)
tSapIngressDot1pTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressDot1pTableLastChanged.setStatus("current")
_TSapIngressIPCriteriaTableLastChanged_Type = TimeStamp
_TSapIngressIPCriteriaTableLastChanged_Object = MibScalar
tSapIngressIPCriteriaTableLastChanged = _TSapIngressIPCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 24),
    _TSapIngressIPCriteriaTableLastChanged_Type()
)
tSapIngressIPCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressIPCriteriaTableLastChanged.setStatus("current")
_TSapIngressMacCriteriaTableLastChanged_Type = TimeStamp
_TSapIngressMacCriteriaTableLastChanged_Object = MibScalar
tSapIngressMacCriteriaTableLastChanged = _TSapIngressMacCriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 25),
    _TSapIngressMacCriteriaTableLastChanged_Type()
)
tSapIngressMacCriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressMacCriteriaTableLastChanged.setStatus("current")
_TSapIngressFCTableLastChanged_Type = TimeStamp
_TSapIngressFCTableLastChanged_Object = MibScalar
tSapIngressFCTableLastChanged = _TSapIngressFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 26),
    _TSapIngressFCTableLastChanged_Type()
)
tSapIngressFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressFCTableLastChanged.setStatus("current")
_TSapIngressPrecTableLastChanged_Type = TimeStamp
_TSapIngressPrecTableLastChanged_Object = MibScalar
tSapIngressPrecTableLastChanged = _TSapIngressPrecTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 27),
    _TSapIngressPrecTableLastChanged_Type()
)
tSapIngressPrecTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressPrecTableLastChanged.setStatus("current")
_TSapEgressTableLastChanged_Type = TimeStamp
_TSapEgressTableLastChanged_Object = MibScalar
tSapEgressTableLastChanged = _TSapEgressTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 30),
    _TSapEgressTableLastChanged_Type()
)
tSapEgressTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressTableLastChanged.setStatus("current")
_TSapEgressQueueTableLastChanged_Type = TimeStamp
_TSapEgressQueueTableLastChanged_Object = MibScalar
tSapEgressQueueTableLastChanged = _TSapEgressQueueTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 31),
    _TSapEgressQueueTableLastChanged_Type()
)
tSapEgressQueueTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressQueueTableLastChanged.setStatus("current")
_TSapEgressFCTableLastChanged_Type = TimeStamp
_TSapEgressFCTableLastChanged_Object = MibScalar
tSapEgressFCTableLastChanged = _TSapEgressFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 32),
    _TSapEgressFCTableLastChanged_Type()
)
tSapEgressFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressFCTableLastChanged.setStatus("current")
_TNetworkPolicyTableLastChanged_Type = TimeStamp
_TNetworkPolicyTableLastChanged_Object = MibScalar
tNetworkPolicyTableLastChanged = _TNetworkPolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 40),
    _TNetworkPolicyTableLastChanged_Type()
)
tNetworkPolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkPolicyTableLastChanged.setStatus("current")
_TNetworkIngressDSCPTableLastChanged_Type = TimeStamp
_TNetworkIngressDSCPTableLastChanged_Object = MibScalar
tNetworkIngressDSCPTableLastChanged = _TNetworkIngressDSCPTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 41),
    _TNetworkIngressDSCPTableLastChanged_Type()
)
tNetworkIngressDSCPTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressDSCPTableLastChanged.setStatus("current")
_TNetworkIngressLSPEXPTableLastChanged_Type = TimeStamp
_TNetworkIngressLSPEXPTableLastChanged_Object = MibScalar
tNetworkIngressLSPEXPTableLastChanged = _TNetworkIngressLSPEXPTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 42),
    _TNetworkIngressLSPEXPTableLastChanged_Type()
)
tNetworkIngressLSPEXPTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressLSPEXPTableLastChanged.setStatus("current")
_TNetworkEgressFCTableLastChanged_Type = TimeStamp
_TNetworkEgressFCTableLastChanged_Object = MibScalar
tNetworkEgressFCTableLastChanged = _TNetworkEgressFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 43),
    _TNetworkEgressFCTableLastChanged_Type()
)
tNetworkEgressFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgressFCTableLastChanged.setStatus("current")
_TNetworkIngressDot1pTableLastChanged_Type = TimeStamp
_TNetworkIngressDot1pTableLastChanged_Object = MibScalar
tNetworkIngressDot1pTableLastChanged = _TNetworkIngressDot1pTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 44),
    _TNetworkIngressDot1pTableLastChanged_Type()
)
tNetworkIngressDot1pTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pTableLastChanged.setStatus("current")
_TNetworkQueuePolicyTableLastChanged_Type = TimeStamp
_TNetworkQueuePolicyTableLastChanged_Object = MibScalar
tNetworkQueuePolicyTableLastChanged = _TNetworkQueuePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 50),
    _TNetworkQueuePolicyTableLastChanged_Type()
)
tNetworkQueuePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueuePolicyTableLastChanged.setStatus("current")
_TNetworkQueueTableLastChanged_Type = TimeStamp
_TNetworkQueueTableLastChanged_Object = MibScalar
tNetworkQueueTableLastChanged = _TNetworkQueueTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 51),
    _TNetworkQueueTableLastChanged_Type()
)
tNetworkQueueTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueueTableLastChanged.setStatus("current")
_TNetworkQueueFCTableLastChanged_Type = TimeStamp
_TNetworkQueueFCTableLastChanged_Object = MibScalar
tNetworkQueueFCTableLastChanged = _TNetworkQueueFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 52),
    _TNetworkQueueFCTableLastChanged_Type()
)
tNetworkQueueFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkQueueFCTableLastChanged.setStatus("current")
_TSlopePolicyTableLastChanged_Type = TimeStamp
_TSlopePolicyTableLastChanged_Object = MibScalar
tSlopePolicyTableLastChanged = _TSlopePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 55),
    _TSlopePolicyTableLastChanged_Type()
)
tSlopePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSlopePolicyTableLastChanged.setStatus("current")
_TSchedulerPolicyTableLastChanged_Type = TimeStamp
_TSchedulerPolicyTableLastChanged_Object = MibScalar
tSchedulerPolicyTableLastChanged = _TSchedulerPolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 60),
    _TSchedulerPolicyTableLastChanged_Type()
)
tSchedulerPolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSchedulerPolicyTableLastChanged.setStatus("current")
_TVirtualSchedulerTableLastChanged_Type = TimeStamp
_TVirtualSchedulerTableLastChanged_Object = MibScalar
tVirtualSchedulerTableLastChanged = _TVirtualSchedulerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 61),
    _TVirtualSchedulerTableLastChanged_Type()
)
tVirtualSchedulerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tVirtualSchedulerTableLastChanged.setStatus("current")
_TAtmTdpTableLastChanged_Type = TimeStamp
_TAtmTdpTableLastChanged_Object = MibScalar
tAtmTdpTableLastChanged = _TAtmTdpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 62),
    _TAtmTdpTableLastChanged_Type()
)
tAtmTdpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTdpTableLastChanged.setStatus("current")
_TSharedQueuePolicyTableLastChanged_Type = TimeStamp
_TSharedQueuePolicyTableLastChanged_Object = MibScalar
tSharedQueuePolicyTableLastChanged = _TSharedQueuePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 63),
    _TSharedQueuePolicyTableLastChanged_Type()
)
tSharedQueuePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueuePolicyTableLastChanged.setStatus("current")
_TSharedQueueTableLastChanged_Type = TimeStamp
_TSharedQueueTableLastChanged_Object = MibScalar
tSharedQueueTableLastChanged = _TSharedQueueTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 64),
    _TSharedQueueTableLastChanged_Type()
)
tSharedQueueTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueueTableLastChanged.setStatus("current")
_TSharedQueueFCTableLastChanged_Type = TimeStamp
_TSharedQueueFCTableLastChanged_Object = MibScalar
tSharedQueueFCTableLastChanged = _TSharedQueueFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 65),
    _TSharedQueueFCTableLastChanged_Type()
)
tSharedQueueFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSharedQueueFCTableLastChanged.setStatus("current")
_TSapIngressIPv6CriteriaTableLastChanged_Type = TimeStamp
_TSapIngressIPv6CriteriaTableLastChanged_Object = MibScalar
tSapIngressIPv6CriteriaTableLastChanged = _TSapIngressIPv6CriteriaTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 66),
    _TSapIngressIPv6CriteriaTableLastChanged_Type()
)
tSapIngressIPv6CriteriaTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressIPv6CriteriaTableLastChanged.setStatus("current")
_TSapIngrHsmdaQueueTblLastChngd_Type = TimeStamp
_TSapIngrHsmdaQueueTblLastChngd_Object = MibScalar
tSapIngrHsmdaQueueTblLastChngd = _TSapIngrHsmdaQueueTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 67),
    _TSapIngrHsmdaQueueTblLastChngd_Type()
)
tSapIngrHsmdaQueueTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngrHsmdaQueueTblLastChngd.setStatus("obsolete")
_TSapEgrHsmdaQueueTblLastChngd_Type = TimeStamp
_TSapEgrHsmdaQueueTblLastChngd_Object = MibScalar
tSapEgrHsmdaQueueTblLastChngd = _TSapEgrHsmdaQueueTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 68),
    _TSapEgrHsmdaQueueTblLastChngd_Type()
)
tSapEgrHsmdaQueueTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrHsmdaQueueTblLastChngd.setStatus("current")
_THsmdaSchedPlcyTblLastChngd_Type = TimeStamp
_THsmdaSchedPlcyTblLastChngd_Object = MibScalar
tHsmdaSchedPlcyTblLastChngd = _THsmdaSchedPlcyTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 69),
    _THsmdaSchedPlcyTblLastChngd_Type()
)
tHsmdaSchedPlcyTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaSchedPlcyTblLastChngd.setStatus("current")
_THsmdaSchedPlcyGrpTblLastChngd_Type = TimeStamp
_THsmdaSchedPlcyGrpTblLastChngd_Object = MibScalar
tHsmdaSchedPlcyGrpTblLastChngd = _THsmdaSchedPlcyGrpTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 70),
    _THsmdaSchedPlcyGrpTblLastChngd_Type()
)
tHsmdaSchedPlcyGrpTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaSchedPlcyGrpTblLastChngd.setStatus("current")
_THsmdaPoolPlcyTblLastChngd_Type = TimeStamp
_THsmdaPoolPlcyTblLastChngd_Object = MibScalar
tHsmdaPoolPlcyTblLastChngd = _THsmdaPoolPlcyTblLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 71),
    _THsmdaPoolPlcyTblLastChngd_Type()
)
tHsmdaPoolPlcyTblLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaPoolPlcyTblLastChngd.setStatus("current")
_THsmdaSlopePolicyTableLastChanged_Type = TimeStamp
_THsmdaSlopePolicyTableLastChanged_Object = MibScalar
tHsmdaSlopePolicyTableLastChanged = _THsmdaSlopePolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 72),
    _THsmdaSlopePolicyTableLastChanged_Type()
)
tHsmdaSlopePolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaSlopePolicyTableLastChanged.setStatus("current")
_TNamedPoolPolicyTableLastChanged_Type = TimeStamp
_TNamedPoolPolicyTableLastChanged_Object = MibScalar
tNamedPoolPolicyTableLastChanged = _TNamedPoolPolicyTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 73),
    _TNamedPoolPolicyTableLastChanged_Type()
)
tNamedPoolPolicyTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNamedPoolPolicyTableLastChanged.setStatus("current")
_TQ1NamedPoolTableLastChanged_Type = TimeStamp
_TQ1NamedPoolTableLastChanged_Object = MibScalar
tQ1NamedPoolTableLastChanged = _TQ1NamedPoolTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 74),
    _TQ1NamedPoolTableLastChanged_Type()
)
tQ1NamedPoolTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQ1NamedPoolTableLastChanged.setStatus("current")
_TMcMlpppIngrProfTableLastChanged_Type = TimeStamp
_TMcMlpppIngrProfTableLastChanged_Object = MibScalar
tMcMlpppIngrProfTableLastChanged = _TMcMlpppIngrProfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 75),
    _TMcMlpppIngrProfTableLastChanged_Type()
)
tMcMlpppIngrProfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppIngrProfTableLastChanged.setStatus("current")
_TMcMlpppIngrClassTableLastChanged_Type = TimeStamp
_TMcMlpppIngrClassTableLastChanged_Object = MibScalar
tMcMlpppIngrClassTableLastChanged = _TMcMlpppIngrClassTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 76),
    _TMcMlpppIngrClassTableLastChanged_Type()
)
tMcMlpppIngrClassTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppIngrClassTableLastChanged.setStatus("current")
_TMcMlpppEgrProfTableLastChanged_Type = TimeStamp
_TMcMlpppEgrProfTableLastChanged_Object = MibScalar
tMcMlpppEgrProfTableLastChanged = _TMcMlpppEgrProfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 77),
    _TMcMlpppEgrProfTableLastChanged_Type()
)
tMcMlpppEgrProfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrProfTableLastChanged.setStatus("current")
_TMcMlpppEgrClassTableLastChanged_Type = TimeStamp
_TMcMlpppEgrClassTableLastChanged_Object = MibScalar
tMcMlpppEgrClassTableLastChanged = _TMcMlpppEgrClassTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 78),
    _TMcMlpppEgrClassTableLastChanged_Type()
)
tMcMlpppEgrClassTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassTableLastChanged.setStatus("current")
_TMcMlpppEgrFCTableLastChanged_Type = TimeStamp
_TMcMlpppEgrFCTableLastChanged_Object = MibScalar
tMcMlpppEgrFCTableLastChanged = _TMcMlpppEgrFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 79),
    _TMcMlpppEgrFCTableLastChanged_Type()
)
tMcMlpppEgrFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrFCTableLastChanged.setStatus("current")
_TMcFrIngrProfTableLastChanged_Type = TimeStamp
_TMcFrIngrProfTableLastChanged_Object = MibScalar
tMcFrIngrProfTableLastChanged = _TMcFrIngrProfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 80),
    _TMcFrIngrProfTableLastChanged_Type()
)
tMcFrIngrProfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrIngrProfTableLastChanged.setStatus("current")
_TMcFrIngrClassTableLastChanged_Type = TimeStamp
_TMcFrIngrClassTableLastChanged_Object = MibScalar
tMcFrIngrClassTableLastChanged = _TMcFrIngrClassTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 81),
    _TMcFrIngrClassTableLastChanged_Type()
)
tMcFrIngrClassTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrIngrClassTableLastChanged.setStatus("current")
_TMcFrEgrProfTableLastChanged_Type = TimeStamp
_TMcFrEgrProfTableLastChanged_Object = MibScalar
tMcFrEgrProfTableLastChanged = _TMcFrEgrProfTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 82),
    _TMcFrEgrProfTableLastChanged_Type()
)
tMcFrEgrProfTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrEgrProfTableLastChanged.setStatus("current")
_TMcFrEgrClassTableLastChanged_Type = TimeStamp
_TMcFrEgrClassTableLastChanged_Object = MibScalar
tMcFrEgrClassTableLastChanged = _TMcFrEgrClassTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 83),
    _TMcFrEgrClassTableLastChanged_Type()
)
tMcFrEgrClassTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrEgrClassTableLastChanged.setStatus("current")
_TSapIngressLspExpTableLastChange_Type = TimeStamp
_TSapIngressLspExpTableLastChange_Object = MibScalar
tSapIngressLspExpTableLastChange = _TSapIngressLspExpTableLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 84),
    _TSapIngressLspExpTableLastChange_Type()
)
tSapIngressLspExpTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngressLspExpTableLastChange.setStatus("current")
_TSapIngPolicerTableLastChanged_Type = TimeStamp
_TSapIngPolicerTableLastChanged_Object = MibScalar
tSapIngPolicerTableLastChanged = _TSapIngPolicerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 85),
    _TSapIngPolicerTableLastChanged_Type()
)
tSapIngPolicerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicerTableLastChanged.setStatus("current")
_TSapEgrPolicerTableLastChanged_Type = TimeStamp
_TSapEgrPolicerTableLastChanged_Object = MibScalar
tSapEgrPolicerTableLastChanged = _TSapEgrPolicerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 86),
    _TSapEgrPolicerTableLastChanged_Type()
)
tSapEgrPolicerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicerTableLastChanged.setStatus("current")
_TQosPolicerCtrlPolTblLastChgd_Type = TimeStamp
_TQosPolicerCtrlPolTblLastChgd_Object = MibScalar
tQosPolicerCtrlPolTblLastChgd = _TQosPolicerCtrlPolTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 87),
    _TQosPolicerCtrlPolTblLastChgd_Type()
)
tQosPolicerCtrlPolTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolTblLastChgd.setStatus("current")
_TQosPolicerLevelTblLastChgd_Type = TimeStamp
_TQosPolicerLevelTblLastChgd_Object = MibScalar
tQosPolicerLevelTblLastChgd = _TQosPolicerLevelTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 88),
    _TQosPolicerLevelTblLastChgd_Type()
)
tQosPolicerLevelTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerLevelTblLastChgd.setStatus("current")
_TQosPolicerArbiterTblLastChgd_Type = TimeStamp
_TQosPolicerArbiterTblLastChgd_Object = MibScalar
tQosPolicerArbiterTblLastChgd = _TQosPolicerArbiterTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 89),
    _TQosPolicerArbiterTblLastChgd_Type()
)
tQosPolicerArbiterTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerArbiterTblLastChgd.setStatus("current")
_TQosEgrQGroupFCTableLastChanged_Type = TimeStamp
_TQosEgrQGroupFCTableLastChanged_Object = MibScalar
tQosEgrQGroupFCTableLastChanged = _TQosEgrQGroupFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 90),
    _TQosEgrQGroupFCTableLastChanged_Type()
)
tQosEgrQGroupFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrQGroupFCTableLastChanged.setStatus("current")
_TPortSchPlcyGrpTblLastChgd_Type = TimeStamp
_TPortSchPlcyGrpTblLastChgd_Object = MibScalar
tPortSchPlcyGrpTblLastChgd = _TPortSchPlcyGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 91),
    _TPortSchPlcyGrpTblLastChgd_Type()
)
tPortSchPlcyGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortSchPlcyGrpTblLastChgd.setStatus("current")
_TPortSchPlcyLvlGrpTblLastChgd_Type = TimeStamp
_TPortSchPlcyLvlGrpTblLastChgd_Object = MibScalar
tPortSchPlcyLvlGrpTblLastChgd = _TPortSchPlcyLvlGrpTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 92),
    _TPortSchPlcyLvlGrpTblLastChgd_Type()
)
tPortSchPlcyLvlGrpTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tPortSchPlcyLvlGrpTblLastChgd.setStatus("current")
_THsmdaWrrPolicyTblLastChgd_Type = TimeStamp
_THsmdaWrrPolicyTblLastChgd_Object = MibScalar
tHsmdaWrrPolicyTblLastChgd = _THsmdaWrrPolicyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 93),
    _THsmdaWrrPolicyTblLastChgd_Type()
)
tHsmdaWrrPolicyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyTblLastChgd.setStatus("current")
_TNetworkEgrHsmdaQueueTblLastChgd_Type = TimeStamp
_TNetworkEgrHsmdaQueueTblLastChgd_Object = MibScalar
tNetworkEgrHsmdaQueueTblLastChgd = _TNetworkEgrHsmdaQueueTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 94),
    _TNetworkEgrHsmdaQueueTblLastChgd_Type()
)
tNetworkEgrHsmdaQueueTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgrHsmdaQueueTblLastChgd.setStatus("current")
_TSapIngPolicyNameTableLastChgd_Type = TimeStamp
_TSapIngPolicyNameTableLastChgd_Object = MibScalar
tSapIngPolicyNameTableLastChgd = _TSapIngPolicyNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 95),
    _TSapIngPolicyNameTableLastChgd_Type()
)
tSapIngPolicyNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapIngPolicyNameTableLastChgd.setStatus("current")
_TSapEgrPolicyNameTableLastChgd_Type = TimeStamp
_TSapEgrPolicyNameTableLastChgd_Object = MibScalar
tSapEgrPolicyNameTableLastChgd = _TSapEgrPolicyNameTableLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 96),
    _TSapEgrPolicyNameTableLastChgd_Type()
)
tSapEgrPolicyNameTableLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgrPolicyNameTableLastChgd.setStatus("current")
_TQosIngPolicerTableLastChanged_Type = TimeStamp
_TQosIngPolicerTableLastChanged_Object = MibScalar
tQosIngPolicerTableLastChanged = _TQosIngPolicerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 97),
    _TQosIngPolicerTableLastChanged_Type()
)
tQosIngPolicerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngPolicerTableLastChanged.setStatus("current")
_TQosEgrPolicerTableLastChanged_Type = TimeStamp
_TQosEgrPolicerTableLastChanged_Object = MibScalar
tQosEgrPolicerTableLastChanged = _TQosEgrPolicerTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 98),
    _TQosEgrPolicerTableLastChanged_Type()
)
tQosEgrPolicerTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrPolicerTableLastChanged.setStatus("current")
_TSapEgressDot1pTableLastChanged_Type = TimeStamp
_TSapEgressDot1pTableLastChanged_Object = MibScalar
tSapEgressDot1pTableLastChanged = _TSapEgressDot1pTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 99),
    _TSapEgressDot1pTableLastChanged_Type()
)
tSapEgressDot1pTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSapEgressDot1pTableLastChanged.setStatus("current")
_TAdvCfgPolicyTblLastChgd_Type = TimeStamp
_TAdvCfgPolicyTblLastChgd_Object = MibScalar
tAdvCfgPolicyTblLastChgd = _TAdvCfgPolicyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 100),
    _TAdvCfgPolicyTblLastChgd_Type()
)
tAdvCfgPolicyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAdvCfgPolicyTblLastChgd.setStatus("current")
_TNetworkIngressFCTableLstChanged_Type = TimeStamp
_TNetworkIngressFCTableLstChanged_Object = MibScalar
tNetworkIngressFCTableLstChanged = _TNetworkIngressFCTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 101),
    _TNetworkIngressFCTableLstChanged_Type()
)
tNetworkIngressFCTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkIngressFCTableLstChanged.setStatus("current")
_TNetworkEgrDSCPTableLastChanged_Type = TimeStamp
_TNetworkEgrDSCPTableLastChanged_Object = MibScalar
tNetworkEgrDSCPTableLastChanged = _TNetworkEgrDSCPTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 102),
    _TNetworkEgrDSCPTableLastChanged_Type()
)
tNetworkEgrDSCPTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgrDSCPTableLastChanged.setStatus("current")
_TNetworkEgrPrecTableLastChanged_Type = TimeStamp
_TNetworkEgrPrecTableLastChanged_Object = MibScalar
tNetworkEgrPrecTableLastChanged = _TNetworkEgrPrecTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 20, 103),
    _TNetworkEgrPrecTableLastChanged_Type()
)
tNetworkEgrPrecTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNetworkEgrPrecTableLastChanged.setStatus("current")
_TAtmTdpObjects_ObjectIdentity = ObjectIdentity
tAtmTdpObjects = _TAtmTdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21)
)
_TAtmTdpTable_Object = MibTable
tAtmTdpTable = _TAtmTdpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1)
)
if mibBuilder.loadTexts:
    tAtmTdpTable.setStatus("current")
_TAtmTdpEntry_Object = MibTableRow
tAtmTdpEntry = _TAtmTdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1)
)
tAtmTdpEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tAtmTdpIndex"),
)
if mibBuilder.loadTexts:
    tAtmTdpEntry.setStatus("current")


class _TAtmTdpIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type tAtmTdpIndex based on AtmTrafficDescrParamIndex"""
    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TAtmTdpIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_TAtmTdpIndex_Object = MibTableColumn
tAtmTdpIndex = _TAtmTdpIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 1),
    _TAtmTdpIndex_Type()
)
tAtmTdpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAtmTdpIndex.setStatus("current")


class _TAtmTdpSir_Type(Unsigned32):
    """Custom type tAtmTdpSir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TAtmTdpSir_Type.__name__ = "Unsigned32"
_TAtmTdpSir_Object = MibTableColumn
tAtmTdpSir = _TAtmTdpSir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 2),
    _TAtmTdpSir_Type()
)
tAtmTdpSir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpSir.setStatus("current")


class _TAtmTdpPir_Type(Unsigned32):
    """Custom type tAtmTdpPir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TAtmTdpPir_Type.__name__ = "Unsigned32"
_TAtmTdpPir_Object = MibTableColumn
tAtmTdpPir = _TAtmTdpPir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 3),
    _TAtmTdpPir_Type()
)
tAtmTdpPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpPir.setStatus("current")


class _TAtmTdpMbs_Type(Unsigned32):
    """Custom type tAtmTdpMbs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TAtmTdpMbs_Type.__name__ = "Unsigned32"
_TAtmTdpMbs_Object = MibTableColumn
tAtmTdpMbs = _TAtmTdpMbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 4),
    _TAtmTdpMbs_Type()
)
tAtmTdpMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpMbs.setStatus("current")


class _TAtmTdpMir_Type(Unsigned32):
    """Custom type tAtmTdpMir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TAtmTdpMir_Type.__name__ = "Unsigned32"
_TAtmTdpMir_Object = MibTableColumn
tAtmTdpMir = _TAtmTdpMir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 5),
    _TAtmTdpMir_Type()
)
tAtmTdpMir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpMir.setStatus("current")


class _TAtmTdpShaping_Type(Integer32):
    """Custom type tAtmTdpShaping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TAtmTdpShaping_Type.__name__ = "Integer32"
_TAtmTdpShaping_Object = MibTableColumn
tAtmTdpShaping = _TAtmTdpShaping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 6),
    _TAtmTdpShaping_Type()
)
tAtmTdpShaping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpShaping.setStatus("current")


class _TAtmTdpServCat_Type(AtmServiceCategory):
    """Custom type tAtmTdpServCat based on AtmServiceCategory"""


_TAtmTdpServCat_Object = MibTableColumn
tAtmTdpServCat = _TAtmTdpServCat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 7),
    _TAtmTdpServCat_Type()
)
tAtmTdpServCat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpServCat.setStatus("current")
_TAtmTdpDescription_Type = TItemDescription
_TAtmTdpDescription_Object = MibTableColumn
tAtmTdpDescription = _TAtmTdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 8),
    _TAtmTdpDescription_Type()
)
tAtmTdpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpDescription.setStatus("current")
_TAtmTdpLastChanged_Type = TimeStamp
_TAtmTdpLastChanged_Object = MibTableColumn
tAtmTdpLastChanged = _TAtmTdpLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 9),
    _TAtmTdpLastChanged_Type()
)
tAtmTdpLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTdpLastChanged.setStatus("current")
_TAtmTdpRowStatus_Type = RowStatus
_TAtmTdpRowStatus_Object = MibTableColumn
tAtmTdpRowStatus = _TAtmTdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 10),
    _TAtmTdpRowStatus_Type()
)
tAtmTdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpRowStatus.setStatus("current")
_TAtmTdpDescrType_Type = TAtmTdpDescrType
_TAtmTdpDescrType_Object = MibTableColumn
tAtmTdpDescrType = _TAtmTdpDescrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 11),
    _TAtmTdpDescrType_Type()
)
tAtmTdpDescrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpDescrType.setStatus("current")


class _TAtmTdpCdvt_Type(Unsigned32):
    """Custom type tAtmTdpCdvt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_TAtmTdpCdvt_Type.__name__ = "Unsigned32"
_TAtmTdpCdvt_Object = MibTableColumn
tAtmTdpCdvt = _TAtmTdpCdvt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 12),
    _TAtmTdpCdvt_Type()
)
tAtmTdpCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpCdvt.setStatus("current")


class _TAtmTdpPolicing_Type(Integer32):
    """Custom type tAtmTdpPolicing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TAtmTdpPolicing_Type.__name__ = "Integer32"
_TAtmTdpPolicing_Object = MibTableColumn
tAtmTdpPolicing = _TAtmTdpPolicing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 13),
    _TAtmTdpPolicing_Type()
)
tAtmTdpPolicing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpPolicing.setStatus("current")


class _TAtmTdpCLPTagging_Type(Integer32):
    """Custom type tAtmTdpCLPTagging based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TAtmTdpCLPTagging_Type.__name__ = "Integer32"
_TAtmTdpCLPTagging_Object = MibTableColumn
tAtmTdpCLPTagging = _TAtmTdpCLPTagging_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 14),
    _TAtmTdpCLPTagging_Type()
)
tAtmTdpCLPTagging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpCLPTagging.setStatus("current")


class _TAtmTdpWeight_Type(Integer32):
    """Custom type tAtmTdpWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TAtmTdpWeight_Type.__name__ = "Integer32"
_TAtmTdpWeight_Object = MibTableColumn
tAtmTdpWeight = _TAtmTdpWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 1, 1, 15),
    _TAtmTdpWeight_Type()
)
tAtmTdpWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAtmTdpWeight.setStatus("current")


class _TAtmTdpIndexNext_Type(Integer32):
    """Custom type tAtmTdpIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TAtmTdpIndexNext_Type.__name__ = "Integer32"
_TAtmTdpIndexNext_Object = MibScalar
tAtmTdpIndexNext = _TAtmTdpIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 2),
    _TAtmTdpIndexNext_Type()
)
tAtmTdpIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTdpIndexNext.setStatus("current")
_TAtmTdpsMaxSupported_Type = Integer32
_TAtmTdpsMaxSupported_Object = MibScalar
tAtmTdpsMaxSupported = _TAtmTdpsMaxSupported_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 3),
    _TAtmTdpsMaxSupported_Type()
)
tAtmTdpsMaxSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTdpsMaxSupported.setStatus("current")
_TAtmTdpsCurrentlyConfigured_Type = Integer32
_TAtmTdpsCurrentlyConfigured_Object = MibScalar
tAtmTdpsCurrentlyConfigured = _TAtmTdpsCurrentlyConfigured_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 21, 4),
    _TAtmTdpsCurrentlyConfigured_Type()
)
tAtmTdpsCurrentlyConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAtmTdpsCurrentlyConfigured.setStatus("current")
_TPoolObjects_ObjectIdentity = ObjectIdentity
tPoolObjects = _TPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22)
)
_TNamedPoolPolicyTable_Object = MibTable
tNamedPoolPolicyTable = _TNamedPoolPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1)
)
if mibBuilder.loadTexts:
    tNamedPoolPolicyTable.setStatus("current")
_TNamedPoolPolicyEntry_Object = MibTableRow
tNamedPoolPolicyEntry = _TNamedPoolPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1)
)
tNamedPoolPolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tNamedPoolPolicyName"),
)
if mibBuilder.loadTexts:
    tNamedPoolPolicyEntry.setStatus("current")
_TNamedPoolPolicyName_Type = TNamedItem
_TNamedPoolPolicyName_Object = MibTableColumn
tNamedPoolPolicyName = _TNamedPoolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 1),
    _TNamedPoolPolicyName_Type()
)
tNamedPoolPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tNamedPoolPolicyName.setStatus("current")
_TNamedPoolPolicyRowStatus_Type = RowStatus
_TNamedPoolPolicyRowStatus_Object = MibTableColumn
tNamedPoolPolicyRowStatus = _TNamedPoolPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 2),
    _TNamedPoolPolicyRowStatus_Type()
)
tNamedPoolPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNamedPoolPolicyRowStatus.setStatus("current")
_TNamedPoolPolicyLastChanged_Type = TimeStamp
_TNamedPoolPolicyLastChanged_Object = MibTableColumn
tNamedPoolPolicyLastChanged = _TNamedPoolPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 3),
    _TNamedPoolPolicyLastChanged_Type()
)
tNamedPoolPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNamedPoolPolicyLastChanged.setStatus("current")
_TNamedPoolPolicyDescription_Type = TItemDescription
_TNamedPoolPolicyDescription_Object = MibTableColumn
tNamedPoolPolicyDescription = _TNamedPoolPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 4),
    _TNamedPoolPolicyDescription_Type()
)
tNamedPoolPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNamedPoolPolicyDescription.setStatus("current")


class _TNamedPoolPolicyQ1DefaultWeight_Type(Unsigned32):
    """Custom type tNamedPoolPolicyQ1DefaultWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TNamedPoolPolicyQ1DefaultWeight_Type.__name__ = "Unsigned32"
_TNamedPoolPolicyQ1DefaultWeight_Object = MibTableColumn
tNamedPoolPolicyQ1DefaultWeight = _TNamedPoolPolicyQ1DefaultWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 5),
    _TNamedPoolPolicyQ1DefaultWeight_Type()
)
tNamedPoolPolicyQ1DefaultWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNamedPoolPolicyQ1DefaultWeight.setStatus("current")


class _TNamedPoolPolicyQ1MdaWeight_Type(Unsigned32):
    """Custom type tNamedPoolPolicyQ1MdaWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TNamedPoolPolicyQ1MdaWeight_Type.__name__ = "Unsigned32"
_TNamedPoolPolicyQ1MdaWeight_Object = MibTableColumn
tNamedPoolPolicyQ1MdaWeight = _TNamedPoolPolicyQ1MdaWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 6),
    _TNamedPoolPolicyQ1MdaWeight_Type()
)
tNamedPoolPolicyQ1MdaWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNamedPoolPolicyQ1MdaWeight.setStatus("current")


class _TNamedPoolPolicyQ1PortWeight_Type(Unsigned32):
    """Custom type tNamedPoolPolicyQ1PortWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TNamedPoolPolicyQ1PortWeight_Type.__name__ = "Unsigned32"
_TNamedPoolPolicyQ1PortWeight_Object = MibTableColumn
tNamedPoolPolicyQ1PortWeight = _TNamedPoolPolicyQ1PortWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 1, 1, 7),
    _TNamedPoolPolicyQ1PortWeight_Type()
)
tNamedPoolPolicyQ1PortWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNamedPoolPolicyQ1PortWeight.setStatus("current")
_TQ1NamedPoolTable_Object = MibTable
tQ1NamedPoolTable = _TQ1NamedPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2)
)
if mibBuilder.loadTexts:
    tQ1NamedPoolTable.setStatus("current")
_TQ1NamedPoolEntry_Object = MibTableRow
tQ1NamedPoolEntry = _TQ1NamedPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1)
)
tQ1NamedPoolEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQ1NamedPoolPolicyName"),
    (0, "TIMETRA-QOS-MIB", "tQ1NamedPoolName"),
)
if mibBuilder.loadTexts:
    tQ1NamedPoolEntry.setStatus("current")
_TQ1NamedPoolPolicyName_Type = TNamedItem
_TQ1NamedPoolPolicyName_Object = MibTableColumn
tQ1NamedPoolPolicyName = _TQ1NamedPoolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 1),
    _TQ1NamedPoolPolicyName_Type()
)
tQ1NamedPoolPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQ1NamedPoolPolicyName.setStatus("current")
_TQ1NamedPoolName_Type = TNamedItem
_TQ1NamedPoolName_Object = MibTableColumn
tQ1NamedPoolName = _TQ1NamedPoolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 2),
    _TQ1NamedPoolName_Type()
)
tQ1NamedPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQ1NamedPoolName.setStatus("current")
_TQ1NamedPoolRowStatus_Type = RowStatus
_TQ1NamedPoolRowStatus_Object = MibTableColumn
tQ1NamedPoolRowStatus = _TQ1NamedPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 3),
    _TQ1NamedPoolRowStatus_Type()
)
tQ1NamedPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolRowStatus.setStatus("current")
_TQ1NamedPoolLastChanged_Type = TimeStamp
_TQ1NamedPoolLastChanged_Object = MibTableColumn
tQ1NamedPoolLastChanged = _TQ1NamedPoolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 4),
    _TQ1NamedPoolLastChanged_Type()
)
tQ1NamedPoolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQ1NamedPoolLastChanged.setStatus("current")
_TQ1NamedPoolDescription_Type = TItemDescription
_TQ1NamedPoolDescription_Object = MibTableColumn
tQ1NamedPoolDescription = _TQ1NamedPoolDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 5),
    _TQ1NamedPoolDescription_Type()
)
tQ1NamedPoolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolDescription.setStatus("current")


class _TQ1NamedPoolNetworkAllocWeight_Type(Unsigned32):
    """Custom type tQ1NamedPoolNetworkAllocWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQ1NamedPoolNetworkAllocWeight_Type.__name__ = "Unsigned32"
_TQ1NamedPoolNetworkAllocWeight_Object = MibTableColumn
tQ1NamedPoolNetworkAllocWeight = _TQ1NamedPoolNetworkAllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 6),
    _TQ1NamedPoolNetworkAllocWeight_Type()
)
tQ1NamedPoolNetworkAllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolNetworkAllocWeight.setStatus("current")


class _TQ1NamedPoolAccessAllocWeight_Type(Unsigned32):
    """Custom type tQ1NamedPoolAccessAllocWeight based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQ1NamedPoolAccessAllocWeight_Type.__name__ = "Unsigned32"
_TQ1NamedPoolAccessAllocWeight_Object = MibTableColumn
tQ1NamedPoolAccessAllocWeight = _TQ1NamedPoolAccessAllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 7),
    _TQ1NamedPoolAccessAllocWeight_Type()
)
tQ1NamedPoolAccessAllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolAccessAllocWeight.setStatus("current")


class _TQ1NamedPoolSlopePolicy_Type(TNamedItemOrEmpty):
    """Custom type tQ1NamedPoolSlopePolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQ1NamedPoolSlopePolicy_Object = MibTableColumn
tQ1NamedPoolSlopePolicy = _TQ1NamedPoolSlopePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 8),
    _TQ1NamedPoolSlopePolicy_Type()
)
tQ1NamedPoolSlopePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolSlopePolicy.setStatus("current")


class _TQ1NamedPoolReservedCbs_Type(Integer32):
    """Custom type tQ1NamedPoolReservedCbs based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQ1NamedPoolReservedCbs_Type.__name__ = "Integer32"
_TQ1NamedPoolReservedCbs_Object = MibTableColumn
tQ1NamedPoolReservedCbs = _TQ1NamedPoolReservedCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 9),
    _TQ1NamedPoolReservedCbs_Type()
)
tQ1NamedPoolReservedCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolReservedCbs.setStatus("current")


class _TQ1NamedPoolResvCbsAmbrAlrmStep_Type(Integer32):
    """Custom type tQ1NamedPoolResvCbsAmbrAlrmStep based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQ1NamedPoolResvCbsAmbrAlrmStep_Type.__name__ = "Integer32"
_TQ1NamedPoolResvCbsAmbrAlrmStep_Object = MibTableColumn
tQ1NamedPoolResvCbsAmbrAlrmStep = _TQ1NamedPoolResvCbsAmbrAlrmStep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 10),
    _TQ1NamedPoolResvCbsAmbrAlrmStep_Type()
)
tQ1NamedPoolResvCbsAmbrAlrmStep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolResvCbsAmbrAlrmStep.setStatus("current")
if mibBuilder.loadTexts:
    tQ1NamedPoolResvCbsAmbrAlrmStep.setUnits("percent")


class _TQ1NamedPoolResvCbsAmbrAlrmMax_Type(Integer32):
    """Custom type tQ1NamedPoolResvCbsAmbrAlrmMax based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TQ1NamedPoolResvCbsAmbrAlrmMax_Type.__name__ = "Integer32"
_TQ1NamedPoolResvCbsAmbrAlrmMax_Object = MibTableColumn
tQ1NamedPoolResvCbsAmbrAlrmMax = _TQ1NamedPoolResvCbsAmbrAlrmMax_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 11),
    _TQ1NamedPoolResvCbsAmbrAlrmMax_Type()
)
tQ1NamedPoolResvCbsAmbrAlrmMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolResvCbsAmbrAlrmMax.setStatus("current")
if mibBuilder.loadTexts:
    tQ1NamedPoolResvCbsAmbrAlrmMax.setUnits("percent")


class _TQ1NamedPoolAmbrAlrmThresh_Type(Integer32):
    """Custom type tQ1NamedPoolAmbrAlrmThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TQ1NamedPoolAmbrAlrmThresh_Type.__name__ = "Integer32"
_TQ1NamedPoolAmbrAlrmThresh_Object = MibTableColumn
tQ1NamedPoolAmbrAlrmThresh = _TQ1NamedPoolAmbrAlrmThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 12),
    _TQ1NamedPoolAmbrAlrmThresh_Type()
)
tQ1NamedPoolAmbrAlrmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolAmbrAlrmThresh.setStatus("current")
if mibBuilder.loadTexts:
    tQ1NamedPoolAmbrAlrmThresh.setUnits("percent")


class _TQ1NamedPoolRedAlrmThresh_Type(Integer32):
    """Custom type tQ1NamedPoolRedAlrmThresh based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TQ1NamedPoolRedAlrmThresh_Type.__name__ = "Integer32"
_TQ1NamedPoolRedAlrmThresh_Object = MibTableColumn
tQ1NamedPoolRedAlrmThresh = _TQ1NamedPoolRedAlrmThresh_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 13),
    _TQ1NamedPoolRedAlrmThresh_Type()
)
tQ1NamedPoolRedAlrmThresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolRedAlrmThresh.setStatus("current")
if mibBuilder.loadTexts:
    tQ1NamedPoolRedAlrmThresh.setUnits("percent")
_THsmdaPoolPolicyTable_Object = MibTable
tHsmdaPoolPolicyTable = _THsmdaPoolPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3)
)
if mibBuilder.loadTexts:
    tHsmdaPoolPolicyTable.setStatus("current")
_THsmdaPoolPolicyEntry_Object = MibTableRow
tHsmdaPoolPolicyEntry = _THsmdaPoolPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1)
)
tHsmdaPoolPolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tHsmdaPoolPolicyName"),
)
if mibBuilder.loadTexts:
    tHsmdaPoolPolicyEntry.setStatus("current")
_THsmdaPoolPolicyName_Type = TNamedItem
_THsmdaPoolPolicyName_Object = MibTableColumn
tHsmdaPoolPolicyName = _THsmdaPoolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 1),
    _THsmdaPoolPolicyName_Type()
)
tHsmdaPoolPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tHsmdaPoolPolicyName.setStatus("current")
_THsmdaPoolPolicyRowStatus_Type = RowStatus
_THsmdaPoolPolicyRowStatus_Object = MibTableColumn
tHsmdaPoolPolicyRowStatus = _THsmdaPoolPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 2),
    _THsmdaPoolPolicyRowStatus_Type()
)
tHsmdaPoolPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolPolicyRowStatus.setStatus("current")
_THsmdaPoolLastChanged_Type = TimeStamp
_THsmdaPoolLastChanged_Object = MibTableColumn
tHsmdaPoolLastChanged = _THsmdaPoolLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 3),
    _THsmdaPoolLastChanged_Type()
)
tHsmdaPoolLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaPoolLastChanged.setStatus("current")
_THsmdaPoolDescription_Type = TItemDescription
_THsmdaPoolDescription_Object = MibTableColumn
tHsmdaPoolDescription = _THsmdaPoolDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 4),
    _THsmdaPoolDescription_Type()
)
tHsmdaPoolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolDescription.setStatus("current")


class _THsmdaPoolSystemReserve_Type(Unsigned32):
    """Custom type tHsmdaPoolSystemReserve based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 3000),
    )


_THsmdaPoolSystemReserve_Type.__name__ = "Unsigned32"
_THsmdaPoolSystemReserve_Object = MibTableColumn
tHsmdaPoolSystemReserve = _THsmdaPoolSystemReserve_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 5),
    _THsmdaPoolSystemReserve_Type()
)
tHsmdaPoolSystemReserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolSystemReserve.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolSystemReserve.setUnits("hundredths of a percent")


class _THsmdaPoolRoot1AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot1AllocWeight based on TWeight"""
    defaultValue = 75

    subtypeSpec = TWeight.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_THsmdaPoolRoot1AllocWeight_Type.__name__ = "TWeight"
_THsmdaPoolRoot1AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot1AllocWeight = _THsmdaPoolRoot1AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 6),
    _THsmdaPoolRoot1AllocWeight_Type()
)
tHsmdaPoolRoot1AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot1AllocWeight.setStatus("current")


class _THsmdaPoolRoot2AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot2AllocWeight based on TWeight"""
    defaultValue = 25


_THsmdaPoolRoot2AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot2AllocWeight = _THsmdaPoolRoot2AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 7),
    _THsmdaPoolRoot2AllocWeight_Type()
)
tHsmdaPoolRoot2AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot2AllocWeight.setStatus("current")


class _THsmdaPoolRoot3AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot3AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot3AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot3AllocWeight = _THsmdaPoolRoot3AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 8),
    _THsmdaPoolRoot3AllocWeight_Type()
)
tHsmdaPoolRoot3AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot3AllocWeight.setStatus("current")


class _THsmdaPoolRoot4AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot4AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot4AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot4AllocWeight = _THsmdaPoolRoot4AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 9),
    _THsmdaPoolRoot4AllocWeight_Type()
)
tHsmdaPoolRoot4AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot4AllocWeight.setStatus("current")


class _THsmdaPoolRoot5AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot5AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot5AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot5AllocWeight = _THsmdaPoolRoot5AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 10),
    _THsmdaPoolRoot5AllocWeight_Type()
)
tHsmdaPoolRoot5AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot5AllocWeight.setStatus("current")


class _THsmdaPoolRoot6AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot6AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot6AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot6AllocWeight = _THsmdaPoolRoot6AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 11),
    _THsmdaPoolRoot6AllocWeight_Type()
)
tHsmdaPoolRoot6AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot6AllocWeight.setStatus("current")


class _THsmdaPoolRoot7AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot7AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot7AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot7AllocWeight = _THsmdaPoolRoot7AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 12),
    _THsmdaPoolRoot7AllocWeight_Type()
)
tHsmdaPoolRoot7AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot7AllocWeight.setStatus("current")


class _THsmdaPoolRoot8AllocWeight_Type(TWeight):
    """Custom type tHsmdaPoolRoot8AllocWeight based on TWeight"""
    defaultValue = 0


_THsmdaPoolRoot8AllocWeight_Object = MibTableColumn
tHsmdaPoolRoot8AllocWeight = _THsmdaPoolRoot8AllocWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 13),
    _THsmdaPoolRoot8AllocWeight_Type()
)
tHsmdaPoolRoot8AllocWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolRoot8AllocWeight.setStatus("current")


class _THsmdaPoolClass1Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass1Parent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass1Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass1Parent_Object = MibTableColumn
tHsmdaPoolClass1Parent = _THsmdaPoolClass1Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 14),
    _THsmdaPoolClass1Parent_Type()
)
tHsmdaPoolClass1Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass1Parent.setStatus("current")


class _THsmdaPoolClass1AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass1AllocPercent based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass1AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass1AllocPercent_Object = MibTableColumn
tHsmdaPoolClass1AllocPercent = _THsmdaPoolClass1AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 15),
    _THsmdaPoolClass1AllocPercent_Type()
)
tHsmdaPoolClass1AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass1AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass1AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass2Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass2Parent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass2Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass2Parent_Object = MibTableColumn
tHsmdaPoolClass2Parent = _THsmdaPoolClass2Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 16),
    _THsmdaPoolClass2Parent_Type()
)
tHsmdaPoolClass2Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass2Parent.setStatus("current")


class _THsmdaPoolClass2AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass2AllocPercent based on Unsigned32"""
    defaultValue = 3500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass2AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass2AllocPercent_Object = MibTableColumn
tHsmdaPoolClass2AllocPercent = _THsmdaPoolClass2AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 17),
    _THsmdaPoolClass2AllocPercent_Type()
)
tHsmdaPoolClass2AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass2AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass2AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass3Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass3Parent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass3Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass3Parent_Object = MibTableColumn
tHsmdaPoolClass3Parent = _THsmdaPoolClass3Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 18),
    _THsmdaPoolClass3Parent_Type()
)
tHsmdaPoolClass3Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass3Parent.setStatus("current")


class _THsmdaPoolClass3AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass3AllocPercent based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass3AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass3AllocPercent_Object = MibTableColumn
tHsmdaPoolClass3AllocPercent = _THsmdaPoolClass3AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 19),
    _THsmdaPoolClass3AllocPercent_Type()
)
tHsmdaPoolClass3AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass3AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass3AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass4Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass4Parent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass4Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass4Parent_Object = MibTableColumn
tHsmdaPoolClass4Parent = _THsmdaPoolClass4Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 20),
    _THsmdaPoolClass4Parent_Type()
)
tHsmdaPoolClass4Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass4Parent.setStatus("current")


class _THsmdaPoolClass4AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass4AllocPercent based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass4AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass4AllocPercent_Object = MibTableColumn
tHsmdaPoolClass4AllocPercent = _THsmdaPoolClass4AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 21),
    _THsmdaPoolClass4AllocPercent_Type()
)
tHsmdaPoolClass4AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass4AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass4AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass5Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass5Parent based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass5Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass5Parent_Object = MibTableColumn
tHsmdaPoolClass5Parent = _THsmdaPoolClass5Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 22),
    _THsmdaPoolClass5Parent_Type()
)
tHsmdaPoolClass5Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass5Parent.setStatus("current")


class _THsmdaPoolClass5AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass5AllocPercent based on Unsigned32"""
    defaultValue = 2000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass5AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass5AllocPercent_Object = MibTableColumn
tHsmdaPoolClass5AllocPercent = _THsmdaPoolClass5AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 23),
    _THsmdaPoolClass5AllocPercent_Type()
)
tHsmdaPoolClass5AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass5AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass5AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass6Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass6Parent based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass6Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass6Parent_Object = MibTableColumn
tHsmdaPoolClass6Parent = _THsmdaPoolClass6Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 24),
    _THsmdaPoolClass6Parent_Type()
)
tHsmdaPoolClass6Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass6Parent.setStatus("current")


class _THsmdaPoolClass6AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass6AllocPercent based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass6AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass6AllocPercent_Object = MibTableColumn
tHsmdaPoolClass6AllocPercent = _THsmdaPoolClass6AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 25),
    _THsmdaPoolClass6AllocPercent_Type()
)
tHsmdaPoolClass6AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass6AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass6AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass7Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass7Parent based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass7Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass7Parent_Object = MibTableColumn
tHsmdaPoolClass7Parent = _THsmdaPoolClass7Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 26),
    _THsmdaPoolClass7Parent_Type()
)
tHsmdaPoolClass7Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass7Parent.setStatus("current")


class _THsmdaPoolClass7AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass7AllocPercent based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass7AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass7AllocPercent_Object = MibTableColumn
tHsmdaPoolClass7AllocPercent = _THsmdaPoolClass7AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 27),
    _THsmdaPoolClass7AllocPercent_Type()
)
tHsmdaPoolClass7AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass7AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass7AllocPercent.setUnits("hundredths of a percent")


class _THsmdaPoolClass8Parent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass8Parent based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_THsmdaPoolClass8Parent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass8Parent_Object = MibTableColumn
tHsmdaPoolClass8Parent = _THsmdaPoolClass8Parent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 28),
    _THsmdaPoolClass8Parent_Type()
)
tHsmdaPoolClass8Parent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass8Parent.setStatus("current")


class _THsmdaPoolClass8AllocPercent_Type(Unsigned32):
    """Custom type tHsmdaPoolClass8AllocPercent based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_THsmdaPoolClass8AllocPercent_Type.__name__ = "Unsigned32"
_THsmdaPoolClass8AllocPercent_Object = MibTableColumn
tHsmdaPoolClass8AllocPercent = _THsmdaPoolClass8AllocPercent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 3, 1, 29),
    _THsmdaPoolClass8AllocPercent_Type()
)
tHsmdaPoolClass8AllocPercent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaPoolClass8AllocPercent.setStatus("current")
if mibBuilder.loadTexts:
    tHsmdaPoolClass8AllocPercent.setUnits("hundredths of a percent")
_TMcMlpppIngressObjects_ObjectIdentity = ObjectIdentity
tMcMlpppIngressObjects = _TMcMlpppIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23)
)
_TMcMlpppIngrProfTable_Object = MibTable
tMcMlpppIngrProfTable = _TMcMlpppIngrProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1)
)
if mibBuilder.loadTexts:
    tMcMlpppIngrProfTable.setStatus("current")
_TMcMlpppIngrProfEntry_Object = MibTableRow
tMcMlpppIngrProfEntry = _TMcMlpppIngrProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1, 1)
)
tMcMlpppIngrProfEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcMlpppIngrProfIndex"),
)
if mibBuilder.loadTexts:
    tMcMlpppIngrProfEntry.setStatus("current")


class _TMcMlpppIngrProfIndex_Type(TMlpppQoSProfileId):
    """Custom type tMcMlpppIngrProfIndex based on TMlpppQoSProfileId"""
    subtypeSpec = TMlpppQoSProfileId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMcMlpppIngrProfIndex_Type.__name__ = "TMlpppQoSProfileId"
_TMcMlpppIngrProfIndex_Object = MibTableColumn
tMcMlpppIngrProfIndex = _TMcMlpppIngrProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1, 1, 1),
    _TMcMlpppIngrProfIndex_Type()
)
tMcMlpppIngrProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcMlpppIngrProfIndex.setStatus("current")


class _TMcMlpppIngrProfDescription_Type(TItemDescription):
    """Custom type tMcMlpppIngrProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TMcMlpppIngrProfDescription_Object = MibTableColumn
tMcMlpppIngrProfDescription = _TMcMlpppIngrProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1, 1, 2),
    _TMcMlpppIngrProfDescription_Type()
)
tMcMlpppIngrProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcMlpppIngrProfDescription.setStatus("current")
_TMcMlpppIngrProfLastChanged_Type = TimeStamp
_TMcMlpppIngrProfLastChanged_Object = MibTableColumn
tMcMlpppIngrProfLastChanged = _TMcMlpppIngrProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1, 1, 3),
    _TMcMlpppIngrProfLastChanged_Type()
)
tMcMlpppIngrProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppIngrProfLastChanged.setStatus("current")
_TMcMlpppIngrProfRowStatus_Type = RowStatus
_TMcMlpppIngrProfRowStatus_Object = MibTableColumn
tMcMlpppIngrProfRowStatus = _TMcMlpppIngrProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 1, 1, 4),
    _TMcMlpppIngrProfRowStatus_Type()
)
tMcMlpppIngrProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcMlpppIngrProfRowStatus.setStatus("current")
_TMcMlpppIngrClassTable_Object = MibTable
tMcMlpppIngrClassTable = _TMcMlpppIngrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 2)
)
if mibBuilder.loadTexts:
    tMcMlpppIngrClassTable.setStatus("current")
_TMcMlpppIngrClassEntry_Object = MibTableRow
tMcMlpppIngrClassEntry = _TMcMlpppIngrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 2, 1)
)
tMcMlpppIngrClassEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcMlpppIngrProfIndex"),
    (0, "TIMETRA-QOS-MIB", "tMcMlpppIngrClassIndex"),
)
if mibBuilder.loadTexts:
    tMcMlpppIngrClassEntry.setStatus("current")
_TMcMlpppIngrClassIndex_Type = TmnxMcMlpppClassIndex
_TMcMlpppIngrClassIndex_Object = MibTableColumn
tMcMlpppIngrClassIndex = _TMcMlpppIngrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 2, 1, 1),
    _TMcMlpppIngrClassIndex_Type()
)
tMcMlpppIngrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcMlpppIngrClassIndex.setStatus("current")


class _TMcMlpppIngrClassReassemblyTmout_Type(Unsigned32):
    """Custom type tMcMlpppIngrClassReassemblyTmout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TMcMlpppIngrClassReassemblyTmout_Type.__name__ = "Unsigned32"
_TMcMlpppIngrClassReassemblyTmout_Object = MibTableColumn
tMcMlpppIngrClassReassemblyTmout = _TMcMlpppIngrClassReassemblyTmout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 2, 1, 2),
    _TMcMlpppIngrClassReassemblyTmout_Type()
)
tMcMlpppIngrClassReassemblyTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcMlpppIngrClassReassemblyTmout.setStatus("current")
_TMcMlpppIngrClassLastChanged_Type = TimeStamp
_TMcMlpppIngrClassLastChanged_Object = MibTableColumn
tMcMlpppIngrClassLastChanged = _TMcMlpppIngrClassLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 23, 2, 1, 3),
    _TMcMlpppIngrClassLastChanged_Type()
)
tMcMlpppIngrClassLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppIngrClassLastChanged.setStatus("current")
_TMcMlpppEgressObjects_ObjectIdentity = ObjectIdentity
tMcMlpppEgressObjects = _TMcMlpppEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24)
)
_TMcMlpppEgrProfTable_Object = MibTable
tMcMlpppEgrProfTable = _TMcMlpppEgrProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1)
)
if mibBuilder.loadTexts:
    tMcMlpppEgrProfTable.setStatus("current")
_TMcMlpppEgrProfEntry_Object = MibTableRow
tMcMlpppEgrProfEntry = _TMcMlpppEgrProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1, 1)
)
tMcMlpppEgrProfEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcMlpppEgrProfIndex"),
)
if mibBuilder.loadTexts:
    tMcMlpppEgrProfEntry.setStatus("current")


class _TMcMlpppEgrProfIndex_Type(TMlpppQoSProfileId):
    """Custom type tMcMlpppEgrProfIndex based on TMlpppQoSProfileId"""
    subtypeSpec = TMlpppQoSProfileId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMcMlpppEgrProfIndex_Type.__name__ = "TMlpppQoSProfileId"
_TMcMlpppEgrProfIndex_Object = MibTableColumn
tMcMlpppEgrProfIndex = _TMcMlpppEgrProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1, 1, 1),
    _TMcMlpppEgrProfIndex_Type()
)
tMcMlpppEgrProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcMlpppEgrProfIndex.setStatus("current")


class _TMcMlpppEgrProfDescription_Type(TItemDescription):
    """Custom type tMcMlpppEgrProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TMcMlpppEgrProfDescription_Object = MibTableColumn
tMcMlpppEgrProfDescription = _TMcMlpppEgrProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1, 1, 2),
    _TMcMlpppEgrProfDescription_Type()
)
tMcMlpppEgrProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcMlpppEgrProfDescription.setStatus("current")
_TMcMlpppEgrProfLastChanged_Type = TimeStamp
_TMcMlpppEgrProfLastChanged_Object = MibTableColumn
tMcMlpppEgrProfLastChanged = _TMcMlpppEgrProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1, 1, 3),
    _TMcMlpppEgrProfLastChanged_Type()
)
tMcMlpppEgrProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrProfLastChanged.setStatus("current")
_TMcMlpppEgrProfRowStatus_Type = RowStatus
_TMcMlpppEgrProfRowStatus_Object = MibTableColumn
tMcMlpppEgrProfRowStatus = _TMcMlpppEgrProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 1, 1, 4),
    _TMcMlpppEgrProfRowStatus_Type()
)
tMcMlpppEgrProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcMlpppEgrProfRowStatus.setStatus("current")
_TMcMlpppEgrClassTable_Object = MibTable
tMcMlpppEgrClassTable = _TMcMlpppEgrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3)
)
if mibBuilder.loadTexts:
    tMcMlpppEgrClassTable.setStatus("current")
_TMcMlpppEgrClassEntry_Object = MibTableRow
tMcMlpppEgrClassEntry = _TMcMlpppEgrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1)
)
tMcMlpppEgrClassEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcMlpppEgrProfIndex"),
    (0, "TIMETRA-QOS-MIB", "tMcMlpppEgrClassIndex"),
)
if mibBuilder.loadTexts:
    tMcMlpppEgrClassEntry.setStatus("current")
_TMcMlpppEgrClassIndex_Type = TmnxMcMlpppClassIndex
_TMcMlpppEgrClassIndex_Object = MibTableColumn
tMcMlpppEgrClassIndex = _TMcMlpppEgrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1, 1),
    _TMcMlpppEgrClassIndex_Type()
)
tMcMlpppEgrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassIndex.setStatus("current")


class _TMcMlpppEgrClassMir_Type(Unsigned32):
    """Custom type tMcMlpppEgrClassMir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TMcMlpppEgrClassMir_Type.__name__ = "Unsigned32"
_TMcMlpppEgrClassMir_Object = MibTableColumn
tMcMlpppEgrClassMir = _TMcMlpppEgrClassMir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1, 2),
    _TMcMlpppEgrClassMir_Type()
)
tMcMlpppEgrClassMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassMir.setStatus("current")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassMir.setUnits("percent")


class _TMcMlpppEgrClassWeight_Type(Unsigned32):
    """Custom type tMcMlpppEgrClassWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TMcMlpppEgrClassWeight_Type.__name__ = "Unsigned32"
_TMcMlpppEgrClassWeight_Object = MibTableColumn
tMcMlpppEgrClassWeight = _TMcMlpppEgrClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1, 3),
    _TMcMlpppEgrClassWeight_Type()
)
tMcMlpppEgrClassWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassWeight.setStatus("current")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassWeight.setUnits("percent")


class _TMcMlpppEgrClassMaxSize_Type(Unsigned32):
    """Custom type tMcMlpppEgrClassMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TMcMlpppEgrClassMaxSize_Type.__name__ = "Unsigned32"
_TMcMlpppEgrClassMaxSize_Object = MibTableColumn
tMcMlpppEgrClassMaxSize = _TMcMlpppEgrClassMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1, 4),
    _TMcMlpppEgrClassMaxSize_Type()
)
tMcMlpppEgrClassMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassMaxSize.setUnits("milliseconds")
_TMcMlpppEgrClassLastChanged_Type = TimeStamp
_TMcMlpppEgrClassLastChanged_Object = MibTableColumn
tMcMlpppEgrClassLastChanged = _TMcMlpppEgrClassLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 3, 1, 5),
    _TMcMlpppEgrClassLastChanged_Type()
)
tMcMlpppEgrClassLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrClassLastChanged.setStatus("current")
_TMcMlpppEgrFCTable_Object = MibTable
tMcMlpppEgrFCTable = _TMcMlpppEgrFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 4)
)
if mibBuilder.loadTexts:
    tMcMlpppEgrFCTable.setStatus("current")
_TMcMlpppEgrFCEntry_Object = MibTableRow
tMcMlpppEgrFCEntry = _TMcMlpppEgrFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 4, 1)
)
tMcMlpppEgrFCEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcMlpppEgrProfIndex"),
    (0, "TIMETRA-QOS-MIB", "tMcMlpppEgrFCName"),
)
if mibBuilder.loadTexts:
    tMcMlpppEgrFCEntry.setStatus("current")
_TMcMlpppEgrFCName_Type = TFCName
_TMcMlpppEgrFCName_Object = MibTableColumn
tMcMlpppEgrFCName = _TMcMlpppEgrFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 4, 1, 1),
    _TMcMlpppEgrFCName_Type()
)
tMcMlpppEgrFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcMlpppEgrFCName.setStatus("current")


class _TMcMlpppEgrFCClass_Type(Unsigned32):
    """Custom type tMcMlpppEgrFCClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TMcMlpppEgrFCClass_Type.__name__ = "Unsigned32"
_TMcMlpppEgrFCClass_Object = MibTableColumn
tMcMlpppEgrFCClass = _TMcMlpppEgrFCClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 4, 1, 2),
    _TMcMlpppEgrFCClass_Type()
)
tMcMlpppEgrFCClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcMlpppEgrFCClass.setStatus("current")
_TMcMlpppEgrFCLastChanged_Type = TimeStamp
_TMcMlpppEgrFCLastChanged_Object = MibTableColumn
tMcMlpppEgrFCLastChanged = _TMcMlpppEgrFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 24, 4, 1, 3),
    _TMcMlpppEgrFCLastChanged_Type()
)
tMcMlpppEgrFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcMlpppEgrFCLastChanged.setStatus("current")
_TMcFrIngressObjects_ObjectIdentity = ObjectIdentity
tMcFrIngressObjects = _TMcFrIngressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25)
)
_TMcFrIngrProfTable_Object = MibTable
tMcFrIngrProfTable = _TMcFrIngrProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1)
)
if mibBuilder.loadTexts:
    tMcFrIngrProfTable.setStatus("current")
_TMcFrIngrProfEntry_Object = MibTableRow
tMcFrIngrProfEntry = _TMcFrIngrProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1, 1)
)
tMcFrIngrProfEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcFrIngrProfIndex"),
)
if mibBuilder.loadTexts:
    tMcFrIngrProfEntry.setStatus("current")


class _TMcFrIngrProfIndex_Type(TMcFrQoSProfileId):
    """Custom type tMcFrIngrProfIndex based on TMcFrQoSProfileId"""
    subtypeSpec = TMcFrQoSProfileId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMcFrIngrProfIndex_Type.__name__ = "TMcFrQoSProfileId"
_TMcFrIngrProfIndex_Object = MibTableColumn
tMcFrIngrProfIndex = _TMcFrIngrProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1, 1, 1),
    _TMcFrIngrProfIndex_Type()
)
tMcFrIngrProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcFrIngrProfIndex.setStatus("current")


class _TMcFrIngrProfDescription_Type(TItemDescription):
    """Custom type tMcFrIngrProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TMcFrIngrProfDescription_Object = MibTableColumn
tMcFrIngrProfDescription = _TMcFrIngrProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1, 1, 2),
    _TMcFrIngrProfDescription_Type()
)
tMcFrIngrProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcFrIngrProfDescription.setStatus("current")
_TMcFrIngrProfLastChanged_Type = TimeStamp
_TMcFrIngrProfLastChanged_Object = MibTableColumn
tMcFrIngrProfLastChanged = _TMcFrIngrProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1, 1, 3),
    _TMcFrIngrProfLastChanged_Type()
)
tMcFrIngrProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrIngrProfLastChanged.setStatus("current")
_TMcFrIngrProfRowStatus_Type = RowStatus
_TMcFrIngrProfRowStatus_Object = MibTableColumn
tMcFrIngrProfRowStatus = _TMcFrIngrProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 1, 1, 4),
    _TMcFrIngrProfRowStatus_Type()
)
tMcFrIngrProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcFrIngrProfRowStatus.setStatus("current")
_TMcFrIngrClassTable_Object = MibTable
tMcFrIngrClassTable = _TMcFrIngrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 2)
)
if mibBuilder.loadTexts:
    tMcFrIngrClassTable.setStatus("current")
_TMcFrIngrClassEntry_Object = MibTableRow
tMcFrIngrClassEntry = _TMcFrIngrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 2, 1)
)
tMcFrIngrClassEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcFrIngrProfIndex"),
    (0, "TIMETRA-QOS-MIB", "tMcFrIngrClassIndex"),
)
if mibBuilder.loadTexts:
    tMcFrIngrClassEntry.setStatus("current")
_TMcFrIngrClassIndex_Type = TmnxMcFrClassIndex
_TMcFrIngrClassIndex_Object = MibTableColumn
tMcFrIngrClassIndex = _TMcFrIngrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 2, 1, 1),
    _TMcFrIngrClassIndex_Type()
)
tMcFrIngrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcFrIngrClassIndex.setStatus("current")


class _TMcFrIngrClassReassemblyTmout_Type(Unsigned32):
    """Custom type tMcFrIngrClassReassemblyTmout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TMcFrIngrClassReassemblyTmout_Type.__name__ = "Unsigned32"
_TMcFrIngrClassReassemblyTmout_Object = MibTableColumn
tMcFrIngrClassReassemblyTmout = _TMcFrIngrClassReassemblyTmout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 2, 1, 2),
    _TMcFrIngrClassReassemblyTmout_Type()
)
tMcFrIngrClassReassemblyTmout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcFrIngrClassReassemblyTmout.setStatus("current")
_TMcFrIngrClassLastChanged_Type = TimeStamp
_TMcFrIngrClassLastChanged_Object = MibTableColumn
tMcFrIngrClassLastChanged = _TMcFrIngrClassLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 25, 2, 1, 3),
    _TMcFrIngrClassLastChanged_Type()
)
tMcFrIngrClassLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrIngrClassLastChanged.setStatus("current")
_TMcFrEgressObjects_ObjectIdentity = ObjectIdentity
tMcFrEgressObjects = _TMcFrEgressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26)
)
_TMcFrEgrProfTable_Object = MibTable
tMcFrEgrProfTable = _TMcFrEgrProfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1)
)
if mibBuilder.loadTexts:
    tMcFrEgrProfTable.setStatus("current")
_TMcFrEgrProfEntry_Object = MibTableRow
tMcFrEgrProfEntry = _TMcFrEgrProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1, 1)
)
tMcFrEgrProfEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcFrEgrProfIndex"),
)
if mibBuilder.loadTexts:
    tMcFrEgrProfEntry.setStatus("current")


class _TMcFrEgrProfIndex_Type(TMcFrQoSProfileId):
    """Custom type tMcFrEgrProfIndex based on TMcFrQoSProfileId"""
    subtypeSpec = TMcFrQoSProfileId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TMcFrEgrProfIndex_Type.__name__ = "TMcFrQoSProfileId"
_TMcFrEgrProfIndex_Object = MibTableColumn
tMcFrEgrProfIndex = _TMcFrEgrProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1, 1, 1),
    _TMcFrEgrProfIndex_Type()
)
tMcFrEgrProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcFrEgrProfIndex.setStatus("current")


class _TMcFrEgrProfDescription_Type(TItemDescription):
    """Custom type tMcFrEgrProfDescription based on TItemDescription"""
    defaultHexValue = ""


_TMcFrEgrProfDescription_Object = MibTableColumn
tMcFrEgrProfDescription = _TMcFrEgrProfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1, 1, 2),
    _TMcFrEgrProfDescription_Type()
)
tMcFrEgrProfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcFrEgrProfDescription.setStatus("current")
_TMcFrEgrProfLastChanged_Type = TimeStamp
_TMcFrEgrProfLastChanged_Object = MibTableColumn
tMcFrEgrProfLastChanged = _TMcFrEgrProfLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1, 1, 3),
    _TMcFrEgrProfLastChanged_Type()
)
tMcFrEgrProfLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrEgrProfLastChanged.setStatus("current")
_TMcFrEgrProfRowStatus_Type = RowStatus
_TMcFrEgrProfRowStatus_Object = MibTableColumn
tMcFrEgrProfRowStatus = _TMcFrEgrProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 1, 1, 4),
    _TMcFrEgrProfRowStatus_Type()
)
tMcFrEgrProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tMcFrEgrProfRowStatus.setStatus("current")
_TMcFrEgrClassTable_Object = MibTable
tMcFrEgrClassTable = _TMcFrEgrClassTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3)
)
if mibBuilder.loadTexts:
    tMcFrEgrClassTable.setStatus("current")
_TMcFrEgrClassEntry_Object = MibTableRow
tMcFrEgrClassEntry = _TMcFrEgrClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1)
)
tMcFrEgrClassEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tMcFrEgrProfIndex"),
    (0, "TIMETRA-QOS-MIB", "tMcFrEgrClassIndex"),
)
if mibBuilder.loadTexts:
    tMcFrEgrClassEntry.setStatus("current")
_TMcFrEgrClassIndex_Type = TmnxMcFrClassIndex
_TMcFrEgrClassIndex_Object = MibTableColumn
tMcFrEgrClassIndex = _TMcFrEgrClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1, 1),
    _TMcFrEgrClassIndex_Type()
)
tMcFrEgrClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tMcFrEgrClassIndex.setStatus("current")


class _TMcFrEgrClassMir_Type(Unsigned32):
    """Custom type tMcFrEgrClassMir based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TMcFrEgrClassMir_Type.__name__ = "Unsigned32"
_TMcFrEgrClassMir_Object = MibTableColumn
tMcFrEgrClassMir = _TMcFrEgrClassMir_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1, 2),
    _TMcFrEgrClassMir_Type()
)
tMcFrEgrClassMir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcFrEgrClassMir.setStatus("current")
if mibBuilder.loadTexts:
    tMcFrEgrClassMir.setUnits("percent")


class _TMcFrEgrClassWeight_Type(Unsigned32):
    """Custom type tMcFrEgrClassWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_TMcFrEgrClassWeight_Type.__name__ = "Unsigned32"
_TMcFrEgrClassWeight_Object = MibTableColumn
tMcFrEgrClassWeight = _TMcFrEgrClassWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1, 3),
    _TMcFrEgrClassWeight_Type()
)
tMcFrEgrClassWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcFrEgrClassWeight.setStatus("current")
if mibBuilder.loadTexts:
    tMcFrEgrClassWeight.setUnits("percent")


class _TMcFrEgrClassMaxSize_Type(Unsigned32):
    """Custom type tMcFrEgrClassMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TMcFrEgrClassMaxSize_Type.__name__ = "Unsigned32"
_TMcFrEgrClassMaxSize_Object = MibTableColumn
tMcFrEgrClassMaxSize = _TMcFrEgrClassMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1, 4),
    _TMcFrEgrClassMaxSize_Type()
)
tMcFrEgrClassMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tMcFrEgrClassMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    tMcFrEgrClassMaxSize.setUnits("milliseconds")
_TMcFrEgrClassLastChanged_Type = TimeStamp
_TMcFrEgrClassLastChanged_Object = MibTableColumn
tMcFrEgrClassLastChanged = _TMcFrEgrClassLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 26, 3, 1, 5),
    _TMcFrEgrClassLastChanged_Type()
)
tMcFrEgrClassLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tMcFrEgrClassLastChanged.setStatus("current")
_TQosPolicerObjects_ObjectIdentity = ObjectIdentity
tQosPolicerObjects = _TQosPolicerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27)
)
_TQosPolicerCtrlPolTable_Object = MibTable
tQosPolicerCtrlPolTable = _TQosPolicerCtrlPolTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1)
)
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolTable.setStatus("current")
_TQosPolicerCtrlPolEntry_Object = MibTableRow
tQosPolicerCtrlPolEntry = _TQosPolicerCtrlPolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1)
)
tQosPolicerCtrlPolEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosPolicerCtrlPolName"),
)
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolEntry.setStatus("current")
_TQosPolicerCtrlPolName_Type = TNamedItem
_TQosPolicerCtrlPolName_Object = MibTableColumn
tQosPolicerCtrlPolName = _TQosPolicerCtrlPolName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 1),
    _TQosPolicerCtrlPolName_Type()
)
tQosPolicerCtrlPolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolName.setStatus("current")
_TQosPolicerCtrlPolRowStatus_Type = RowStatus
_TQosPolicerCtrlPolRowStatus_Object = MibTableColumn
tQosPolicerCtrlPolRowStatus = _TQosPolicerCtrlPolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 2),
    _TQosPolicerCtrlPolRowStatus_Type()
)
tQosPolicerCtrlPolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolRowStatus.setStatus("current")
_TQosPolicerCtrlPolLastChgd_Type = TimeStamp
_TQosPolicerCtrlPolLastChgd_Object = MibTableColumn
tQosPolicerCtrlPolLastChgd = _TQosPolicerCtrlPolLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 3),
    _TQosPolicerCtrlPolLastChgd_Type()
)
tQosPolicerCtrlPolLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolLastChgd.setStatus("current")


class _TQosPolicerCtrlPolDescr_Type(TItemDescription):
    """Custom type tQosPolicerCtrlPolDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosPolicerCtrlPolDescr_Object = MibTableColumn
tQosPolicerCtrlPolDescr = _TQosPolicerCtrlPolDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 4),
    _TQosPolicerCtrlPolDescr_Type()
)
tQosPolicerCtrlPolDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolDescr.setStatus("current")


class _TQosPolicerCtrlPolRootMaxRate_Type(THPolPIRRate):
    """Custom type tQosPolicerCtrlPolRootMaxRate based on THPolPIRRate"""
    defaultValue = -1


_TQosPolicerCtrlPolRootMaxRate_Object = MibTableColumn
tQosPolicerCtrlPolRootMaxRate = _TQosPolicerCtrlPolRootMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 5),
    _TQosPolicerCtrlPolRootMaxRate_Type()
)
tQosPolicerCtrlPolRootMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolRootMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolRootMaxRate.setUnits("kbps")


class _TQosPolicerCtrlPolMinMBSSep_Type(TPlcrBurstSizeBytes):
    """Custom type tQosPolicerCtrlPolMinMBSSep based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosPolicerCtrlPolMinMBSSep_Object = MibTableColumn
tQosPolicerCtrlPolMinMBSSep = _TQosPolicerCtrlPolMinMBSSep_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 6),
    _TQosPolicerCtrlPolMinMBSSep_Type()
)
tQosPolicerCtrlPolMinMBSSep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolMinMBSSep.setStatus("current")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolMinMBSSep.setUnits("bytes")


class _TQosPolicerCtrlPolProfPref_Type(TruthValue):
    """Custom type tQosPolicerCtrlPolProfPref based on TruthValue"""


_TQosPolicerCtrlPolProfPref_Object = MibTableColumn
tQosPolicerCtrlPolProfPref = _TQosPolicerCtrlPolProfPref_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 1, 1, 7),
    _TQosPolicerCtrlPolProfPref_Type()
)
tQosPolicerCtrlPolProfPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerCtrlPolProfPref.setStatus("current")
_TQosPolicerLevelTable_Object = MibTable
tQosPolicerLevelTable = _TQosPolicerLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2)
)
if mibBuilder.loadTexts:
    tQosPolicerLevelTable.setStatus("current")
_TQosPolicerLevelEntry_Object = MibTableRow
tQosPolicerLevelEntry = _TQosPolicerLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2, 1)
)
tQosPolicerLevelEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosPolicerCtrlPolName"),
    (0, "TIMETRA-QOS-MIB", "tQosPolicerLevel"),
)
if mibBuilder.loadTexts:
    tQosPolicerLevelEntry.setStatus("current")
_TQosPolicerLevel_Type = TLevel
_TQosPolicerLevel_Object = MibTableColumn
tQosPolicerLevel = _TQosPolicerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2, 1, 1),
    _TQosPolicerLevel_Type()
)
tQosPolicerLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosPolicerLevel.setStatus("current")
_TQosPolicerLevelLastChgd_Type = TimeStamp
_TQosPolicerLevelLastChgd_Object = MibTableColumn
tQosPolicerLevelLastChgd = _TQosPolicerLevelLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2, 1, 2),
    _TQosPolicerLevelLastChgd_Type()
)
tQosPolicerLevelLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerLevelLastChgd.setStatus("current")


class _TQosPolicerLevelCumMBS_Type(TPlcrBurstSizeBytes):
    """Custom type tQosPolicerLevelCumMBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosPolicerLevelCumMBS_Object = MibTableColumn
tQosPolicerLevelCumMBS = _TQosPolicerLevelCumMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2, 1, 3),
    _TQosPolicerLevelCumMBS_Type()
)
tQosPolicerLevelCumMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerLevelCumMBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosPolicerLevelCumMBS.setUnits("bytes")


class _TQosPolicerLevelFixedMBS_Type(TruthValue):
    """Custom type tQosPolicerLevelFixedMBS based on TruthValue"""


_TQosPolicerLevelFixedMBS_Object = MibTableColumn
tQosPolicerLevelFixedMBS = _TQosPolicerLevelFixedMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 2, 1, 4),
    _TQosPolicerLevelFixedMBS_Type()
)
tQosPolicerLevelFixedMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerLevelFixedMBS.setStatus("current")
_TQosPolicerArbiterTable_Object = MibTable
tQosPolicerArbiterTable = _TQosPolicerArbiterTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3)
)
if mibBuilder.loadTexts:
    tQosPolicerArbiterTable.setStatus("current")
_TQosPolicerArbiterEntry_Object = MibTableRow
tQosPolicerArbiterEntry = _TQosPolicerArbiterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1)
)
tQosPolicerArbiterEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosPolicerCtrlPolName"),
    (0, "TIMETRA-QOS-MIB", "tQosPolicerArbiterTier"),
    (0, "TIMETRA-QOS-MIB", "tQosPolicerArbiterName"),
)
if mibBuilder.loadTexts:
    tQosPolicerArbiterEntry.setStatus("current")


class _TQosPolicerArbiterTier_Type(Integer32):
    """Custom type tQosPolicerArbiterTier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tier1", 1),
          ("tier2", 2))
    )


_TQosPolicerArbiterTier_Type.__name__ = "Integer32"
_TQosPolicerArbiterTier_Object = MibTableColumn
tQosPolicerArbiterTier = _TQosPolicerArbiterTier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 1),
    _TQosPolicerArbiterTier_Type()
)
tQosPolicerArbiterTier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosPolicerArbiterTier.setStatus("current")
_TQosPolicerArbiterName_Type = TNamedItem
_TQosPolicerArbiterName_Object = MibTableColumn
tQosPolicerArbiterName = _TQosPolicerArbiterName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 2),
    _TQosPolicerArbiterName_Type()
)
tQosPolicerArbiterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosPolicerArbiterName.setStatus("current")
_TQosPolicerArbiterRowStatus_Type = RowStatus
_TQosPolicerArbiterRowStatus_Object = MibTableColumn
tQosPolicerArbiterRowStatus = _TQosPolicerArbiterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 3),
    _TQosPolicerArbiterRowStatus_Type()
)
tQosPolicerArbiterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterRowStatus.setStatus("current")
_TQosPolicerArbiterLastChgd_Type = TimeStamp
_TQosPolicerArbiterLastChgd_Object = MibTableColumn
tQosPolicerArbiterLastChgd = _TQosPolicerArbiterLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 4),
    _TQosPolicerArbiterLastChgd_Type()
)
tQosPolicerArbiterLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosPolicerArbiterLastChgd.setStatus("current")


class _TQosPolicerArbiterDescr_Type(TItemDescription):
    """Custom type tQosPolicerArbiterDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosPolicerArbiterDescr_Object = MibTableColumn
tQosPolicerArbiterDescr = _TQosPolicerArbiterDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 5),
    _TQosPolicerArbiterDescr_Type()
)
tQosPolicerArbiterDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterDescr.setStatus("current")


class _TQosPolicerArbiterRate_Type(THPolPIRRate):
    """Custom type tQosPolicerArbiterRate based on THPolPIRRate"""
    defaultValue = -1


_TQosPolicerArbiterRate_Object = MibTableColumn
tQosPolicerArbiterRate = _TQosPolicerArbiterRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 6),
    _TQosPolicerArbiterRate_Type()
)
tQosPolicerArbiterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterRate.setStatus("current")
if mibBuilder.loadTexts:
    tQosPolicerArbiterRate.setUnits("kbps")


class _TQosPolicerArbiterParent_Type(TNamedItemOrEmpty):
    """Custom type tQosPolicerArbiterParent based on TNamedItemOrEmpty"""
    defaultValue = OctetString("root")


_TQosPolicerArbiterParent_Object = MibTableColumn
tQosPolicerArbiterParent = _TQosPolicerArbiterParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 7),
    _TQosPolicerArbiterParent_Type()
)
tQosPolicerArbiterParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterParent.setStatus("current")


class _TQosPolicerArbiterLevel_Type(TLevel):
    """Custom type tQosPolicerArbiterLevel based on TLevel"""
    defaultValue = 1


_TQosPolicerArbiterLevel_Object = MibTableColumn
tQosPolicerArbiterLevel = _TQosPolicerArbiterLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 8),
    _TQosPolicerArbiterLevel_Type()
)
tQosPolicerArbiterLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterLevel.setStatus("current")


class _TQosPolicerArbiterWeight_Type(TPolicerWeight):
    """Custom type tQosPolicerArbiterWeight based on TPolicerWeight"""
    defaultValue = 1


_TQosPolicerArbiterWeight_Object = MibTableColumn
tQosPolicerArbiterWeight = _TQosPolicerArbiterWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 3, 1, 9),
    _TQosPolicerArbiterWeight_Type()
)
tQosPolicerArbiterWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosPolicerArbiterWeight.setStatus("current")
_TQosIngPolicerTable_Object = MibTable
tQosIngPolicerTable = _TQosIngPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4)
)
if mibBuilder.loadTexts:
    tQosIngPolicerTable.setStatus("current")
_TQosIngPolicerEntry_Object = MibTableRow
tQosIngPolicerEntry = _TQosIngPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1)
)
tQosIngPolicerEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosIngQGroupName"),
    (0, "TIMETRA-QOS-MIB", "tQosIngPolicerId"),
)
if mibBuilder.loadTexts:
    tQosIngPolicerEntry.setStatus("current")
_TQosIngPolicerId_Type = TIngPolicerId
_TQosIngPolicerId_Object = MibTableColumn
tQosIngPolicerId = _TQosIngPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 1),
    _TQosIngPolicerId_Type()
)
tQosIngPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosIngPolicerId.setStatus("current")
_TQosIngPolicerRowStatus_Type = RowStatus
_TQosIngPolicerRowStatus_Object = MibTableColumn
tQosIngPolicerRowStatus = _TQosIngPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 2),
    _TQosIngPolicerRowStatus_Type()
)
tQosIngPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerRowStatus.setStatus("current")
_TQosIngPolicerLastChanged_Type = TimeStamp
_TQosIngPolicerLastChanged_Object = MibTableColumn
tQosIngPolicerLastChanged = _TQosIngPolicerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 3),
    _TQosIngPolicerLastChanged_Type()
)
tQosIngPolicerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosIngPolicerLastChanged.setStatus("current")


class _TQosIngPolicerDescr_Type(TItemDescription):
    """Custom type tQosIngPolicerDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosIngPolicerDescr_Object = MibTableColumn
tQosIngPolicerDescr = _TQosIngPolicerDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 4),
    _TQosIngPolicerDescr_Type()
)
tQosIngPolicerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerDescr.setStatus("current")


class _TQosIngPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosIngPolicerPIRAdaptation based on TAdaptationRule"""


_TQosIngPolicerPIRAdaptation_Object = MibTableColumn
tQosIngPolicerPIRAdaptation = _TQosIngPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 5),
    _TQosIngPolicerPIRAdaptation_Type()
)
tQosIngPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerPIRAdaptation.setStatus("current")


class _TQosIngPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosIngPolicerCIRAdaptation based on TAdaptationRule"""


_TQosIngPolicerCIRAdaptation_Object = MibTableColumn
tQosIngPolicerCIRAdaptation = _TQosIngPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 6),
    _TQosIngPolicerCIRAdaptation_Type()
)
tQosIngPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerCIRAdaptation.setStatus("current")


class _TQosIngPolicerParent_Type(TNamedItemOrEmpty):
    """Custom type tQosIngPolicerParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosIngPolicerParent_Object = MibTableColumn
tQosIngPolicerParent = _TQosIngPolicerParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 7),
    _TQosIngPolicerParent_Type()
)
tQosIngPolicerParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerParent.setStatus("current")


class _TQosIngPolicerLevel_Type(TLevel):
    """Custom type tQosIngPolicerLevel based on TLevel"""
    defaultValue = 1


_TQosIngPolicerLevel_Object = MibTableColumn
tQosIngPolicerLevel = _TQosIngPolicerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 8),
    _TQosIngPolicerLevel_Type()
)
tQosIngPolicerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerLevel.setStatus("current")


class _TQosIngPolicerWeight_Type(TPolicerWeight):
    """Custom type tQosIngPolicerWeight based on TPolicerWeight"""
    defaultValue = 1


_TQosIngPolicerWeight_Object = MibTableColumn
tQosIngPolicerWeight = _TQosIngPolicerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 9),
    _TQosIngPolicerWeight_Type()
)
tQosIngPolicerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerWeight.setStatus("current")


class _TQosIngPolicerAdminPIR_Type(THPolPIRRate):
    """Custom type tQosIngPolicerAdminPIR based on THPolPIRRate"""
    defaultValue = -1


_TQosIngPolicerAdminPIR_Object = MibTableColumn
tQosIngPolicerAdminPIR = _TQosIngPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 10),
    _TQosIngPolicerAdminPIR_Type()
)
tQosIngPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerAdminPIR.setUnits("kbps")


class _TQosIngPolicerAdminCIR_Type(THPolCIRRate):
    """Custom type tQosIngPolicerAdminCIR based on THPolCIRRate"""
    defaultValue = 0


_TQosIngPolicerAdminCIR_Object = MibTableColumn
tQosIngPolicerAdminCIR = _TQosIngPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 11),
    _TQosIngPolicerAdminCIR_Type()
)
tQosIngPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerAdminCIR.setUnits("kbps")


class _TQosIngPolicerCBS_Type(TPlcrBurstSizeBytes):
    """Custom type tQosIngPolicerCBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosIngPolicerCBS_Object = MibTableColumn
tQosIngPolicerCBS = _TQosIngPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 12),
    _TQosIngPolicerCBS_Type()
)
tQosIngPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerCBS.setUnits("bytes")


class _TQosIngPolicerMBS_Type(TPlcrBurstSizeBytes):
    """Custom type tQosIngPolicerMBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosIngPolicerMBS_Object = MibTableColumn
tQosIngPolicerMBS = _TQosIngPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 13),
    _TQosIngPolicerMBS_Type()
)
tQosIngPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerMBS.setUnits("bytes")


class _TQosIngPolicerHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tQosIngPolicerHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TQosIngPolicerHiPrioOnly_Object = MibTableColumn
tQosIngPolicerHiPrioOnly = _TQosIngPolicerHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 14),
    _TQosIngPolicerHiPrioOnly_Type()
)
tQosIngPolicerHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerHiPrioOnly.setUnits("percent")


class _TQosIngPolicerPktOffset_Type(TPerPacketOffset):
    """Custom type tQosIngPolicerPktOffset based on TPerPacketOffset"""
    defaultValue = 0


_TQosIngPolicerPktOffset_Object = MibTableColumn
tQosIngPolicerPktOffset = _TQosIngPolicerPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 15),
    _TQosIngPolicerPktOffset_Type()
)
tQosIngPolicerPktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerPktOffset.setStatus("current")


class _TQosIngPolicerProfileCapped_Type(TruthValue):
    """Custom type tQosIngPolicerProfileCapped based on TruthValue"""


_TQosIngPolicerProfileCapped_Object = MibTableColumn
tQosIngPolicerProfileCapped = _TQosIngPolicerProfileCapped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 16),
    _TQosIngPolicerProfileCapped_Type()
)
tQosIngPolicerProfileCapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerProfileCapped.setStatus("current")


class _TQosIngPolicerStatMode_Type(TmnxIngPolicerStatMode):
    """Custom type tQosIngPolicerStatMode based on TmnxIngPolicerStatMode"""


_TQosIngPolicerStatMode_Object = MibTableColumn
tQosIngPolicerStatMode = _TQosIngPolicerStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 17),
    _TQosIngPolicerStatMode_Type()
)
tQosIngPolicerStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerStatMode.setStatus("current")


class _TQosIngPolicerSlopeStartDepth_Type(Unsigned32):
    """Custom type tQosIngPolicerSlopeStartDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosIngPolicerSlopeStartDepth_Type.__name__ = "Unsigned32"
_TQosIngPolicerSlopeStartDepth_Object = MibTableColumn
tQosIngPolicerSlopeStartDepth = _TQosIngPolicerSlopeStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 18),
    _TQosIngPolicerSlopeStartDepth_Type()
)
tQosIngPolicerSlopeStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeStartDepth.setUnits("hundredths of a percent")


class _TQosIngPolicerSlopeMaxDepth_Type(Unsigned32):
    """Custom type tQosIngPolicerSlopeMaxDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosIngPolicerSlopeMaxDepth_Type.__name__ = "Unsigned32"
_TQosIngPolicerSlopeMaxDepth_Object = MibTableColumn
tQosIngPolicerSlopeMaxDepth = _TQosIngPolicerSlopeMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 19),
    _TQosIngPolicerSlopeMaxDepth_Type()
)
tQosIngPolicerSlopeMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeMaxDepth.setUnits("hundredths of a percent")


class _TQosIngPolicerSlopeMaxProb_Type(Unsigned32):
    """Custom type tQosIngPolicerSlopeMaxProb based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosIngPolicerSlopeMaxProb_Type.__name__ = "Unsigned32"
_TQosIngPolicerSlopeMaxProb_Object = MibTableColumn
tQosIngPolicerSlopeMaxProb = _TQosIngPolicerSlopeMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 20),
    _TQosIngPolicerSlopeMaxProb_Type()
)
tQosIngPolicerSlopeMaxProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeMaxProb.setStatus("current")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeMaxProb.setUnits("hundredths of a percent")


class _TQosIngPolicerSlopeMap_Type(TmnxSlopeMap):
    """Custom type tQosIngPolicerSlopeMap based on TmnxSlopeMap"""


_TQosIngPolicerSlopeMap_Object = MibTableColumn
tQosIngPolicerSlopeMap = _TQosIngPolicerSlopeMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 21),
    _TQosIngPolicerSlopeMap_Type()
)
tQosIngPolicerSlopeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerSlopeMap.setStatus("current")


class _TQosIngPolicerAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tQosIngPolicerAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosIngPolicerAdvCfgPolicy_Object = MibTableColumn
tQosIngPolicerAdvCfgPolicy = _TQosIngPolicerAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 4, 1, 22),
    _TQosIngPolicerAdvCfgPolicy_Type()
)
tQosIngPolicerAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosIngPolicerAdvCfgPolicy.setStatus("current")
_TQosEgrPolicerTable_Object = MibTable
tQosEgrPolicerTable = _TQosEgrPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5)
)
if mibBuilder.loadTexts:
    tQosEgrPolicerTable.setStatus("current")
_TQosEgrPolicerEntry_Object = MibTableRow
tQosEgrPolicerEntry = _TQosEgrPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1)
)
tQosEgrPolicerEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tQosEgrQGroupName"),
    (0, "TIMETRA-QOS-MIB", "tQosEgrPolicerId"),
)
if mibBuilder.loadTexts:
    tQosEgrPolicerEntry.setStatus("current")
_TQosEgrPolicerId_Type = TEgrPolicerId
_TQosEgrPolicerId_Object = MibTableColumn
tQosEgrPolicerId = _TQosEgrPolicerId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 1),
    _TQosEgrPolicerId_Type()
)
tQosEgrPolicerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tQosEgrPolicerId.setStatus("current")
_TQosEgrPolicerRowStatus_Type = RowStatus
_TQosEgrPolicerRowStatus_Object = MibTableColumn
tQosEgrPolicerRowStatus = _TQosEgrPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 2),
    _TQosEgrPolicerRowStatus_Type()
)
tQosEgrPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerRowStatus.setStatus("current")
_TQosEgrPolicerLastChanged_Type = TimeStamp
_TQosEgrPolicerLastChanged_Object = MibTableColumn
tQosEgrPolicerLastChanged = _TQosEgrPolicerLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 3),
    _TQosEgrPolicerLastChanged_Type()
)
tQosEgrPolicerLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tQosEgrPolicerLastChanged.setStatus("current")


class _TQosEgrPolicerDescr_Type(TItemDescription):
    """Custom type tQosEgrPolicerDescr based on TItemDescription"""
    defaultHexValue = ""


_TQosEgrPolicerDescr_Object = MibTableColumn
tQosEgrPolicerDescr = _TQosEgrPolicerDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 4),
    _TQosEgrPolicerDescr_Type()
)
tQosEgrPolicerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerDescr.setStatus("current")


class _TQosEgrPolicerPIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosEgrPolicerPIRAdaptation based on TAdaptationRule"""


_TQosEgrPolicerPIRAdaptation_Object = MibTableColumn
tQosEgrPolicerPIRAdaptation = _TQosEgrPolicerPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 5),
    _TQosEgrPolicerPIRAdaptation_Type()
)
tQosEgrPolicerPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerPIRAdaptation.setStatus("current")


class _TQosEgrPolicerCIRAdaptation_Type(TAdaptationRule):
    """Custom type tQosEgrPolicerCIRAdaptation based on TAdaptationRule"""


_TQosEgrPolicerCIRAdaptation_Object = MibTableColumn
tQosEgrPolicerCIRAdaptation = _TQosEgrPolicerCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 6),
    _TQosEgrPolicerCIRAdaptation_Type()
)
tQosEgrPolicerCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerCIRAdaptation.setStatus("current")


class _TQosEgrPolicerParent_Type(TNamedItemOrEmpty):
    """Custom type tQosEgrPolicerParent based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosEgrPolicerParent_Object = MibTableColumn
tQosEgrPolicerParent = _TQosEgrPolicerParent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 7),
    _TQosEgrPolicerParent_Type()
)
tQosEgrPolicerParent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerParent.setStatus("current")


class _TQosEgrPolicerLevel_Type(TLevel):
    """Custom type tQosEgrPolicerLevel based on TLevel"""
    defaultValue = 1


_TQosEgrPolicerLevel_Object = MibTableColumn
tQosEgrPolicerLevel = _TQosEgrPolicerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 8),
    _TQosEgrPolicerLevel_Type()
)
tQosEgrPolicerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerLevel.setStatus("current")


class _TQosEgrPolicerWeight_Type(TPolicerWeight):
    """Custom type tQosEgrPolicerWeight based on TPolicerWeight"""
    defaultValue = 1


_TQosEgrPolicerWeight_Object = MibTableColumn
tQosEgrPolicerWeight = _TQosEgrPolicerWeight_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 9),
    _TQosEgrPolicerWeight_Type()
)
tQosEgrPolicerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerWeight.setStatus("current")


class _TQosEgrPolicerAdminPIR_Type(THPolPIRRate):
    """Custom type tQosEgrPolicerAdminPIR based on THPolPIRRate"""
    defaultValue = -1


_TQosEgrPolicerAdminPIR_Object = MibTableColumn
tQosEgrPolicerAdminPIR = _TQosEgrPolicerAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 10),
    _TQosEgrPolicerAdminPIR_Type()
)
tQosEgrPolicerAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerAdminPIR.setUnits("kbps")


class _TQosEgrPolicerAdminCIR_Type(THPolCIRRate):
    """Custom type tQosEgrPolicerAdminCIR based on THPolCIRRate"""
    defaultValue = 0


_TQosEgrPolicerAdminCIR_Object = MibTableColumn
tQosEgrPolicerAdminCIR = _TQosEgrPolicerAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 11),
    _TQosEgrPolicerAdminCIR_Type()
)
tQosEgrPolicerAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerAdminCIR.setUnits("kbps")


class _TQosEgrPolicerCBS_Type(TPlcrBurstSizeBytes):
    """Custom type tQosEgrPolicerCBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosEgrPolicerCBS_Object = MibTableColumn
tQosEgrPolicerCBS = _TQosEgrPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 12),
    _TQosEgrPolicerCBS_Type()
)
tQosEgrPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerCBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerCBS.setUnits("bytes")


class _TQosEgrPolicerMBS_Type(TPlcrBurstSizeBytes):
    """Custom type tQosEgrPolicerMBS based on TPlcrBurstSizeBytes"""
    defaultValue = -1


_TQosEgrPolicerMBS_Object = MibTableColumn
tQosEgrPolicerMBS = _TQosEgrPolicerMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 13),
    _TQosEgrPolicerMBS_Type()
)
tQosEgrPolicerMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerMBS.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerMBS.setUnits("bytes")


class _TQosEgrPolicerHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type tQosEgrPolicerHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_TQosEgrPolicerHiPrioOnly_Object = MibTableColumn
tQosEgrPolicerHiPrioOnly = _TQosEgrPolicerHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 14),
    _TQosEgrPolicerHiPrioOnly_Type()
)
tQosEgrPolicerHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerHiPrioOnly.setUnits("percent")


class _TQosEgrPolicerPktOffset_Type(TPerPacketOffset):
    """Custom type tQosEgrPolicerPktOffset based on TPerPacketOffset"""
    defaultValue = 0


_TQosEgrPolicerPktOffset_Object = MibTableColumn
tQosEgrPolicerPktOffset = _TQosEgrPolicerPktOffset_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 15),
    _TQosEgrPolicerPktOffset_Type()
)
tQosEgrPolicerPktOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerPktOffset.setStatus("current")


class _TQosEgrPolicerProfileCapped_Type(TruthValue):
    """Custom type tQosEgrPolicerProfileCapped based on TruthValue"""


_TQosEgrPolicerProfileCapped_Object = MibTableColumn
tQosEgrPolicerProfileCapped = _TQosEgrPolicerProfileCapped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 16),
    _TQosEgrPolicerProfileCapped_Type()
)
tQosEgrPolicerProfileCapped.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerProfileCapped.setStatus("current")


class _TQosEgrPolicerStatMode_Type(TmnxEgrPolicerStatMode):
    """Custom type tQosEgrPolicerStatMode based on TmnxEgrPolicerStatMode"""


_TQosEgrPolicerStatMode_Object = MibTableColumn
tQosEgrPolicerStatMode = _TQosEgrPolicerStatMode_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 17),
    _TQosEgrPolicerStatMode_Type()
)
tQosEgrPolicerStatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerStatMode.setStatus("current")


class _TQosEgrPolicerSlopeStartDepth_Type(Unsigned32):
    """Custom type tQosEgrPolicerSlopeStartDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosEgrPolicerSlopeStartDepth_Type.__name__ = "Unsigned32"
_TQosEgrPolicerSlopeStartDepth_Object = MibTableColumn
tQosEgrPolicerSlopeStartDepth = _TQosEgrPolicerSlopeStartDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 18),
    _TQosEgrPolicerSlopeStartDepth_Type()
)
tQosEgrPolicerSlopeStartDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeStartDepth.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeStartDepth.setUnits("hundredths of a percent")


class _TQosEgrPolicerSlopeMaxDepth_Type(Unsigned32):
    """Custom type tQosEgrPolicerSlopeMaxDepth based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosEgrPolicerSlopeMaxDepth_Type.__name__ = "Unsigned32"
_TQosEgrPolicerSlopeMaxDepth_Object = MibTableColumn
tQosEgrPolicerSlopeMaxDepth = _TQosEgrPolicerSlopeMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 20),
    _TQosEgrPolicerSlopeMaxDepth_Type()
)
tQosEgrPolicerSlopeMaxDepth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeMaxDepth.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeMaxDepth.setUnits("hundredths of a percent")


class _TQosEgrPolicerSlopeMaxProb_Type(Unsigned32):
    """Custom type tQosEgrPolicerSlopeMaxProb based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_TQosEgrPolicerSlopeMaxProb_Type.__name__ = "Unsigned32"
_TQosEgrPolicerSlopeMaxProb_Object = MibTableColumn
tQosEgrPolicerSlopeMaxProb = _TQosEgrPolicerSlopeMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 21),
    _TQosEgrPolicerSlopeMaxProb_Type()
)
tQosEgrPolicerSlopeMaxProb.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeMaxProb.setStatus("current")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeMaxProb.setUnits("hundredths of a percent")


class _TQosEgrPolicerSlopeMap_Type(TmnxSlopeMap):
    """Custom type tQosEgrPolicerSlopeMap based on TmnxSlopeMap"""


_TQosEgrPolicerSlopeMap_Object = MibTableColumn
tQosEgrPolicerSlopeMap = _TQosEgrPolicerSlopeMap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 22),
    _TQosEgrPolicerSlopeMap_Type()
)
tQosEgrPolicerSlopeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerSlopeMap.setStatus("current")


class _TQosEgrPolicerAdvCfgPolicy_Type(TNamedItemOrEmpty):
    """Custom type tQosEgrPolicerAdvCfgPolicy based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_TQosEgrPolicerAdvCfgPolicy_Object = MibTableColumn
tQosEgrPolicerAdvCfgPolicy = _TQosEgrPolicerAdvCfgPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 5, 1, 23),
    _TQosEgrPolicerAdvCfgPolicy_Type()
)
tQosEgrPolicerAdvCfgPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQosEgrPolicerAdvCfgPolicy.setStatus("current")
_TAdvCfgPolicyTable_Object = MibTable
tAdvCfgPolicyTable = _TAdvCfgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6)
)
if mibBuilder.loadTexts:
    tAdvCfgPolicyTable.setStatus("current")
_TAdvCfgPolicyEntry_Object = MibTableRow
tAdvCfgPolicyEntry = _TAdvCfgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1)
)
tAdvCfgPolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tAdvCfgPolicyName"),
)
if mibBuilder.loadTexts:
    tAdvCfgPolicyEntry.setStatus("current")
_TAdvCfgPolicyName_Type = TNamedItem
_TAdvCfgPolicyName_Object = MibTableColumn
tAdvCfgPolicyName = _TAdvCfgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 1),
    _TAdvCfgPolicyName_Type()
)
tAdvCfgPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tAdvCfgPolicyName.setStatus("current")
_TAdvCfgPolicyRowStatus_Type = RowStatus
_TAdvCfgPolicyRowStatus_Object = MibTableColumn
tAdvCfgPolicyRowStatus = _TAdvCfgPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 2),
    _TAdvCfgPolicyRowStatus_Type()
)
tAdvCfgPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgPolicyRowStatus.setStatus("current")
_TAdvCfgLastChanged_Type = TimeStamp
_TAdvCfgLastChanged_Object = MibTableColumn
tAdvCfgLastChanged = _TAdvCfgLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 3),
    _TAdvCfgLastChanged_Type()
)
tAdvCfgLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tAdvCfgLastChanged.setStatus("current")


class _TAdvCfgDescription_Type(TItemDescription):
    """Custom type tAdvCfgDescription based on TItemDescription"""
    defaultHexValue = ""


_TAdvCfgDescription_Object = MibTableColumn
tAdvCfgDescription = _TAdvCfgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 4),
    _TAdvCfgDescription_Type()
)
tAdvCfgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgDescription.setStatus("current")


class _TAdvCfgChildAdmnPirPrcnt_Type(Unsigned32):
    """Custom type tAdvCfgChildAdmnPirPrcnt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TAdvCfgChildAdmnPirPrcnt_Type.__name__ = "Unsigned32"
_TAdvCfgChildAdmnPirPrcnt_Object = MibTableColumn
tAdvCfgChildAdmnPirPrcnt = _TAdvCfgChildAdmnPirPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 5),
    _TAdvCfgChildAdmnPirPrcnt_Type()
)
tAdvCfgChildAdmnPirPrcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgChildAdmnPirPrcnt.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgChildAdmnPirPrcnt.setUnits("hundredths of a percent")


class _TAdvCfgChildAdminRate_Type(TAdvCfgRate):
    """Custom type tAdvCfgChildAdminRate based on TAdvCfgRate"""
    defaultValue = 0


_TAdvCfgChildAdminRate_Object = MibTableColumn
tAdvCfgChildAdminRate = _TAdvCfgChildAdminRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 6),
    _TAdvCfgChildAdminRate_Type()
)
tAdvCfgChildAdminRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgChildAdminRate.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgChildAdminRate.setUnits("kbps")


class _TAdvCfgOMGranPirPrcnt_Type(Unsigned32):
    """Custom type tAdvCfgOMGranPirPrcnt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TAdvCfgOMGranPirPrcnt_Type.__name__ = "Unsigned32"
_TAdvCfgOMGranPirPrcnt_Object = MibTableColumn
tAdvCfgOMGranPirPrcnt = _TAdvCfgOMGranPirPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 7),
    _TAdvCfgOMGranPirPrcnt_Type()
)
tAdvCfgOMGranPirPrcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgOMGranPirPrcnt.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgOMGranPirPrcnt.setUnits("hundredths of a percent")


class _TAdvCfgOMGranRate_Type(TAdvCfgRate):
    """Custom type tAdvCfgOMGranRate based on TAdvCfgRate"""
    defaultValue = 0


_TAdvCfgOMGranRate_Object = MibTableColumn
tAdvCfgOMGranRate = _TAdvCfgOMGranRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 8),
    _TAdvCfgOMGranRate_Type()
)
tAdvCfgOMGranRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgOMGranRate.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgOMGranRate.setUnits("kbps")


class _TAdvCfgMaxDecPirPrcnt_Type(Unsigned32):
    """Custom type tAdvCfgMaxDecPirPrcnt based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TAdvCfgMaxDecPirPrcnt_Type.__name__ = "Unsigned32"
_TAdvCfgMaxDecPirPrcnt_Object = MibTableColumn
tAdvCfgMaxDecPirPrcnt = _TAdvCfgMaxDecPirPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 9),
    _TAdvCfgMaxDecPirPrcnt_Type()
)
tAdvCfgMaxDecPirPrcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgMaxDecPirPrcnt.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgMaxDecPirPrcnt.setUnits("hundredths of a percent")


class _TAdvCfgMaxDecRate_Type(TMaxDecRate):
    """Custom type tAdvCfgMaxDecRate based on TMaxDecRate"""
    defaultValue = 0


_TAdvCfgMaxDecRate_Object = MibTableColumn
tAdvCfgMaxDecRate = _TAdvCfgMaxDecRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 10),
    _TAdvCfgMaxDecRate_Type()
)
tAdvCfgMaxDecRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgMaxDecRate.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgMaxDecRate.setUnits("kbps")


class _TAdvCfgHiRateHoldTime_Type(Unsigned32):
    """Custom type tAdvCfgHiRateHoldTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_TAdvCfgHiRateHoldTime_Type.__name__ = "Unsigned32"
_TAdvCfgHiRateHoldTime_Object = MibTableColumn
tAdvCfgHiRateHoldTime = _TAdvCfgHiRateHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 11),
    _TAdvCfgHiRateHoldTime_Type()
)
tAdvCfgHiRateHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgHiRateHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgHiRateHoldTime.setUnits("seconds")


class _TAdvCfgTimeAvgFactor_Type(Unsigned32):
    """Custom type tAdvCfgTimeAvgFactor based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TAdvCfgTimeAvgFactor_Type.__name__ = "Unsigned32"
_TAdvCfgTimeAvgFactor_Object = MibTableColumn
tAdvCfgTimeAvgFactor = _TAdvCfgTimeAvgFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 12),
    _TAdvCfgTimeAvgFactor_Type()
)
tAdvCfgTimeAvgFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgTimeAvgFactor.setStatus("current")


class _TAdvCfgSampleInterval_Type(Unsigned32):
    """Custom type tAdvCfgSampleInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TAdvCfgSampleInterval_Type.__name__ = "Unsigned32"
_TAdvCfgSampleInterval_Object = MibTableColumn
tAdvCfgSampleInterval = _TAdvCfgSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 13),
    _TAdvCfgSampleInterval_Type()
)
tAdvCfgSampleInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgSampleInterval.setStatus("current")


class _TAdvCfgFastStart_Type(TruthValue):
    """Custom type tAdvCfgFastStart based on TruthValue"""


_TAdvCfgFastStart_Object = MibTableColumn
tAdvCfgFastStart = _TAdvCfgFastStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 14),
    _TAdvCfgFastStart_Type()
)
tAdvCfgFastStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgFastStart.setStatus("current")


class _TAdvCfgFastStop_Type(TruthValue):
    """Custom type tAdvCfgFastStop based on TruthValue"""


_TAdvCfgFastStop_Object = MibTableColumn
tAdvCfgFastStop = _TAdvCfgFastStop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 15),
    _TAdvCfgFastStop_Type()
)
tAdvCfgFastStop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgFastStop.setStatus("current")


class _TAdvCfgAbvOffCapPirPrcnt_Type(Unsigned32):
    """Custom type tAdvCfgAbvOffCapPirPrcnt based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TAdvCfgAbvOffCapPirPrcnt_Type.__name__ = "Unsigned32"
_TAdvCfgAbvOffCapPirPrcnt_Object = MibTableColumn
tAdvCfgAbvOffCapPirPrcnt = _TAdvCfgAbvOffCapPirPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 16),
    _TAdvCfgAbvOffCapPirPrcnt_Type()
)
tAdvCfgAbvOffCapPirPrcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgAbvOffCapPirPrcnt.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgAbvOffCapPirPrcnt.setUnits("hundredths of a percent")


class _TAdvCfgAbvOffCapRate_Type(Integer32):
    """Custom type tAdvCfgAbvOffCapRate based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100000000),
    )


_TAdvCfgAbvOffCapRate_Type.__name__ = "Integer32"
_TAdvCfgAbvOffCapRate_Object = MibTableColumn
tAdvCfgAbvOffCapRate = _TAdvCfgAbvOffCapRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 17),
    _TAdvCfgAbvOffCapRate_Type()
)
tAdvCfgAbvOffCapRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgAbvOffCapRate.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgAbvOffCapRate.setUnits("kbps")


class _TAdvCfgBWDGranPirPrcnt_Type(Unsigned32):
    """Custom type tAdvCfgBWDGranPirPrcnt based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_TAdvCfgBWDGranPirPrcnt_Type.__name__ = "Unsigned32"
_TAdvCfgBWDGranPirPrcnt_Object = MibTableColumn
tAdvCfgBWDGranPirPrcnt = _TAdvCfgBWDGranPirPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 18),
    _TAdvCfgBWDGranPirPrcnt_Type()
)
tAdvCfgBWDGranPirPrcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgBWDGranPirPrcnt.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgBWDGranPirPrcnt.setUnits("hundredths of a percent")


class _TAdvCfgBWDGranRate_Type(TAdvCfgRate):
    """Custom type tAdvCfgBWDGranRate based on TAdvCfgRate"""
    defaultValue = 0


_TAdvCfgBWDGranRate_Object = MibTableColumn
tAdvCfgBWDGranRate = _TAdvCfgBWDGranRate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 19),
    _TAdvCfgBWDGranRate_Type()
)
tAdvCfgBWDGranRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgBWDGranRate.setStatus("current")
if mibBuilder.loadTexts:
    tAdvCfgBWDGranRate.setUnits("kbps")


class _TAdvCfgMinOnly_Type(TruthValue):
    """Custom type tAdvCfgMinOnly based on TruthValue"""


_TAdvCfgMinOnly_Object = MibTableColumn
tAdvCfgMinOnly = _TAdvCfgMinOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 20),
    _TAdvCfgMinOnly_Type()
)
tAdvCfgMinOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgMinOnly.setStatus("current")


class _TAdvCfgDecOnly_Type(TruthValue):
    """Custom type tAdvCfgDecOnly based on TruthValue"""


_TAdvCfgDecOnly_Object = MibTableColumn
tAdvCfgDecOnly = _TAdvCfgDecOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 27, 6, 1, 21),
    _TAdvCfgDecOnly_Type()
)
tAdvCfgDecOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tAdvCfgDecOnly.setStatus("current")
_TWrrObjects_ObjectIdentity = ObjectIdentity
tWrrObjects = _TWrrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28)
)
_THsmdaWrrPolicyTable_Object = MibTable
tHsmdaWrrPolicyTable = _THsmdaWrrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1)
)
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyTable.setStatus("current")
_THsmdaWrrPolicyEntry_Object = MibTableRow
tHsmdaWrrPolicyEntry = _THsmdaWrrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1)
)
tHsmdaWrrPolicyEntry.setIndexNames(
    (0, "TIMETRA-QOS-MIB", "tHsmdaWrrPolicyName"),
)
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyEntry.setStatus("current")
_THsmdaWrrPolicyName_Type = TNamedItem
_THsmdaWrrPolicyName_Object = MibTableColumn
tHsmdaWrrPolicyName = _THsmdaWrrPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 1),
    _THsmdaWrrPolicyName_Type()
)
tHsmdaWrrPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyName.setStatus("current")
_THsmdaWrrPolicyRowStatus_Type = RowStatus
_THsmdaWrrPolicyRowStatus_Object = MibTableColumn
tHsmdaWrrPolicyRowStatus = _THsmdaWrrPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 2),
    _THsmdaWrrPolicyRowStatus_Type()
)
tHsmdaWrrPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyRowStatus.setStatus("current")
_THsmdaWrrPolicyLastChanged_Type = TimeStamp
_THsmdaWrrPolicyLastChanged_Object = MibTableColumn
tHsmdaWrrPolicyLastChanged = _THsmdaWrrPolicyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 3),
    _THsmdaWrrPolicyLastChanged_Type()
)
tHsmdaWrrPolicyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyLastChanged.setStatus("current")
_THsmdaWrrPolicyDescription_Type = TItemDescription
_THsmdaWrrPolicyDescription_Object = MibTableColumn
tHsmdaWrrPolicyDescription = _THsmdaWrrPolicyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 4),
    _THsmdaWrrPolicyDescription_Type()
)
tHsmdaWrrPolicyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyDescription.setStatus("current")


class _THsmdaWrrPolicyIncludeQueues_Type(THsmdaPolicyIncludeQueues):
    """Custom type tHsmdaWrrPolicyIncludeQueues based on THsmdaPolicyIncludeQueues"""


_THsmdaWrrPolicyIncludeQueues_Object = MibTableColumn
tHsmdaWrrPolicyIncludeQueues = _THsmdaWrrPolicyIncludeQueues_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 5),
    _THsmdaWrrPolicyIncludeQueues_Type()
)
tHsmdaWrrPolicyIncludeQueues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyIncludeQueues.setStatus("current")


class _THsmdaWrrPolicySchedUsingClass_Type(THsmdaPolicyScheduleClass):
    """Custom type tHsmdaWrrPolicySchedUsingClass based on THsmdaPolicyScheduleClass"""
    defaultValue = 1


_THsmdaWrrPolicySchedUsingClass_Object = MibTableColumn
tHsmdaWrrPolicySchedUsingClass = _THsmdaWrrPolicySchedUsingClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 6),
    _THsmdaWrrPolicySchedUsingClass_Type()
)
tHsmdaWrrPolicySchedUsingClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicySchedUsingClass.setStatus("current")


class _THsmdaWrrPolicyAggWeightAtClass_Type(THsmdaWeightClass):
    """Custom type tHsmdaWrrPolicyAggWeightAtClass based on THsmdaWeightClass"""


_THsmdaWrrPolicyAggWeightAtClass_Object = MibTableColumn
tHsmdaWrrPolicyAggWeightAtClass = _THsmdaWrrPolicyAggWeightAtClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 28, 1, 1, 7),
    _THsmdaWrrPolicyAggWeightAtClass_Type()
)
tHsmdaWrrPolicyAggWeightAtClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tHsmdaWrrPolicyAggWeightAtClass.setStatus("current")
_TQosNotifyPrefix_ObjectIdentity = ObjectIdentity
tQosNotifyPrefix = _TQosNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 16)
)
_TQosNotifications_ObjectIdentity = ObjectIdentity
tQosNotifications = _TQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 16, 0)
)
tPortSchedulerPlcyEntry.registerAugmentions(
    ("TIMETRA-QOS-MIB",
     "tPortSchPlcyLvlGrpEntry")
)
tPortSchPlcyLvlGrpEntry.setIndexNames(*tPortSchedulerPlcyEntry.getIndexNames())

# Managed Objects groups

tmnxQosGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 1)
)
tmnxQosGlobalGroup.setObjects(
    ("TIMETRA-QOS-MIB", "tQosDomainLastChanged")
)
if mibBuilder.loadTexts:
    tmnxQosGlobalGroup.setStatus("current")

tmnxQosDSCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 2)
)
tmnxQosDSCPGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tDSCPNameRowStatus"),
        ("TIMETRA-QOS-MIB", "tDSCPNameStorageType"),
        ("TIMETRA-QOS-MIB", "tDSCPNameDscpValue"),
        ("TIMETRA-QOS-MIB", "tDSCPNameLastChanged"),
        ("TIMETRA-QOS-MIB", "tDSCPNameTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosDSCPGroup.setStatus("current")

tmnxQosFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 3)
)
tmnxQosFCGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tFCStorageType"),
        ("TIMETRA-QOS-MIB", "tFCValue"),
        ("TIMETRA-QOS-MIB", "tFCNameLastChanged"),
        ("TIMETRA-QOS-MIB", "tFCNameTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosFCGroup.setStatus("current")

tmnxQosSlopeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 7)
)
tmnxQosSlopeGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSlopeRowStatus"),
        ("TIMETRA-QOS-MIB", "tSlopeDescription"),
        ("TIMETRA-QOS-MIB", "tSlopeHiAdminStatus"),
        ("TIMETRA-QOS-MIB", "tSlopeHiStartAverage"),
        ("TIMETRA-QOS-MIB", "tSlopeHiMaxAverage"),
        ("TIMETRA-QOS-MIB", "tSlopeHiMaxProbability"),
        ("TIMETRA-QOS-MIB", "tSlopeLoAdminStatus"),
        ("TIMETRA-QOS-MIB", "tSlopeLoStartAverage"),
        ("TIMETRA-QOS-MIB", "tSlopeLoMaxAverage"),
        ("TIMETRA-QOS-MIB", "tSlopeLoMaxProbability"),
        ("TIMETRA-QOS-MIB", "tSlopeTimeAvgFactor"),
        ("TIMETRA-QOS-MIB", "tSlopeLastChanged"),
        ("TIMETRA-QOS-MIB", "tSlopePolicyTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSlopeGroup.setStatus("current")

tmnxQosSchedulerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 8)
)
tmnxQosSchedulerGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSchedulerPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerRowStatus"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerDescription"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerParent"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerSummedCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSchedulerGroup.setStatus("obsolete")

tQosObsoleteObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 10)
)
tQosObsoleteObjectsGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressQueueOperPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueOperCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueOperPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueOperCIR"))
)
if mibBuilder.loadTexts:
    tQosObsoleteObjectsGroup.setStatus("current")

tmnxQosSapEgressR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 12)
)
tmnxQosSapEgressR2r1Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressR2r1Group.setStatus("obsolete")

tmnxQosNetworkR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 13)
)
tmnxQosNetworkR2r1Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkR2r1Group.setStatus("obsolete")

tmnxQosAtmTdpV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 15)
)
tmnxQosAtmTdpV3v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tAtmTdpSir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpPir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpMbs"),
        ("TIMETRA-QOS-MIB", "tAtmTdpMir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpShaping"),
        ("TIMETRA-QOS-MIB", "tAtmTdpServCat"),
        ("TIMETRA-QOS-MIB", "tAtmTdpLastChanged"),
        ("TIMETRA-QOS-MIB", "tAtmTdpDescription"),
        ("TIMETRA-QOS-MIB", "tAtmTdpRowStatus"),
        ("TIMETRA-QOS-MIB", "tAtmTdpDescrType"),
        ("TIMETRA-QOS-MIB", "tAtmTdpCdvt"),
        ("TIMETRA-QOS-MIB", "tAtmTdpPolicing"),
        ("TIMETRA-QOS-MIB", "tAtmTdpIndexNext"),
        ("TIMETRA-QOS-MIB", "tAtmTdpsMaxSupported"),
        ("TIMETRA-QOS-MIB", "tAtmTdpsCurrentlyConfigured"),
        ("TIMETRA-QOS-MIB", "tAtmTdpTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosAtmTdpV3v0Group.setStatus("obsolete")

tmnxQosSapIpv6FilterR4r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 16)
)
tmnxQosSapIpv6FilterR4r0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaNextHeader"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDSCP"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIpv6FilterR4r0Group.setStatus("current")

tmnxQosQueueV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 18)
)
tmnxQosQueueV4v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSharedQueuePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tSharedQueuePolicyDescription"),
        ("TIMETRA-QOS-MIB", "tSharedQueuePolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueuePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSharedQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tSharedQueueParent"),
        ("TIMETRA-QOS-MIB", "tSharedQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSharedQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSharedQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSharedQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSharedQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSharedQueueCIR"),
        ("TIMETRA-QOS-MIB", "tSharedQueuePIR"),
        ("TIMETRA-QOS-MIB", "tSharedQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSharedQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSharedQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSharedQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueueIsMultipoint"),
        ("TIMETRA-QOS-MIB", "tSharedQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCQueue"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSharedQueueFCUnknownQueue"))
)
if mibBuilder.loadTexts:
    tmnxQosQueueV4v0Group.setStatus("current")

tmnxQosSapIngressV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 19)
)
tmnxQosSapIngressV4v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV4v0Group.setStatus("obsolete")

tmnxQosSchedulerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 20)
)
tmnxQosSchedulerV5v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSchedulerPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerRowStatus"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerDescription"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerParent"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerSummedCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerUsePortParent"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortLvl"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortWght"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRWght"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyRowStatus"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyDescription"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyMaxRate"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl1PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl1CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl2PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl2CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl3PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl3CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl4PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl4CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl5PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl5CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl6PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl6CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl7PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl7CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl8PIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl8CIR"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanLvl"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRLvl"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRWght"))
)
if mibBuilder.loadTexts:
    tmnxQosSchedulerV5v0Group.setStatus("current")

tmnxQosSapEgressV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 21)
)
tmnxQosSapEgressV5v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortAvgOverhead"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV5v0Group.setStatus("obsolete")

tmnxQosNetworkV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 22)
)
tmnxQosNetworkV5v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortAvgOverhead"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV5v0Group.setStatus("obsolete")

tmnxQosHsmdaV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 23)
)
tmnxQosHsmdaV6v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyMaxRate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp2Rate"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PHsmdaProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaPacketOffset"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefFCHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolSystemReserve"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot1AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot2AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot3AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot4AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot5AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot6AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot7AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot8AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeQueueMbs"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxProbability"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxProbability"),
        ("TIMETRA-QOS-MIB", "tSapIngrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tSapEgrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyGrpTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCritHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritProtocol"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDSCP"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritFragment"),
        ("TIMETRA-QOS-MIB", "tSapEgressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaPacketOffset"))
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaV6v0Group.setStatus("obsolete")

tmnxQosAtmTdpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 24)
)
tmnxQosAtmTdpV5v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tAtmTdpSir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpPir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpMbs"),
        ("TIMETRA-QOS-MIB", "tAtmTdpMir"),
        ("TIMETRA-QOS-MIB", "tAtmTdpShaping"),
        ("TIMETRA-QOS-MIB", "tAtmTdpServCat"),
        ("TIMETRA-QOS-MIB", "tAtmTdpLastChanged"),
        ("TIMETRA-QOS-MIB", "tAtmTdpDescription"),
        ("TIMETRA-QOS-MIB", "tAtmTdpRowStatus"),
        ("TIMETRA-QOS-MIB", "tAtmTdpDescrType"),
        ("TIMETRA-QOS-MIB", "tAtmTdpCdvt"),
        ("TIMETRA-QOS-MIB", "tAtmTdpPolicing"),
        ("TIMETRA-QOS-MIB", "tAtmTdpCLPTagging"),
        ("TIMETRA-QOS-MIB", "tAtmTdpIndexNext"),
        ("TIMETRA-QOS-MIB", "tAtmTdpsMaxSupported"),
        ("TIMETRA-QOS-MIB", "tAtmTdpsCurrentlyConfigured"),
        ("TIMETRA-QOS-MIB", "tAtmTdpTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosAtmTdpV5v0Group.setStatus("current")

tmnxQosSapIngressV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 25)
)
tmnxQosSapIngressV6v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCDE1OutOfProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV6v0Group.setStatus("obsolete")

tmnxQosSapEgressV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 26)
)
tmnxQosSapEgressV6v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PInProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1POutProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCForceDEValue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDEMark"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortAvgOverhead"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePoolName"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV6v0Group.setStatus("obsolete")

tmnxQosNetworkV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 27)
)
tmnxQosNetworkV6v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCForceDEValue"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDEMark"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortAvgOverhead"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV6v0Group.setStatus("obsolete")

tmnxQosFrameBasedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 28)
)
tmnxQosFrameBasedV6v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tSchedulerPolicyFrameBasedAccnt")
)
if mibBuilder.loadTexts:
    tmnxQosFrameBasedV6v0Group.setStatus("current")

tmnxQosObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 29)
)
tmnxQosObsoletedV6v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue")
)
if mibBuilder.loadTexts:
    tmnxQosObsoletedV6v0Group.setStatus("current")

tmnxQosNamedPoolPolicyV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 30)
)
tmnxQosNamedPoolPolicyV6v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNamedPoolPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1DefaultWeight"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1MdaWeight"),
        ("TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1PortWeight"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolRowStatus"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolLastChanged"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolDescription"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolNetworkAllocWeight"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolAccessAllocWeight"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolReservedCbs"))
)
if mibBuilder.loadTexts:
    tmnxQosNamedPoolPolicyV6v0Group.setStatus("current")

tmnxQosMcMlpppIngrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 31)
)
tmnxQosMcMlpppIngrGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tMcMlpppIngrProfDescription"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrProfLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrProfRowStatus"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrProfTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrClassReassemblyTmout"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrClassLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppIngrClassTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosMcMlpppIngrGroup.setStatus("current")

tmnxQosMcMlpppEgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 32)
)
tmnxQosMcMlpppEgrGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tMcMlpppEgrProfDescription"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrProfLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrProfRowStatus"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrProfTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrClassMir"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrClassWeight"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrClassMaxSize"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrClassLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrClassTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrFCClass"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcMlpppEgrFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosMcMlpppEgrGroup.setStatus("current")

tmnxQosQueueObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 33)
)
tmnxQosQueueObjGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosEgrQGroupDescr"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueLevel"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueMBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueParent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueWeight"),
        ("TIMETRA-QOS-MIB", "tQosIngQTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupDescr"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCBS"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueLevel"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMBS"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMCast"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMode"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueParent"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueWeight"))
)
if mibBuilder.loadTexts:
    tmnxQosQueueObjGroup.setStatus("obsolete")

tQosQGrpFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 34)
)
tQosQGrpFCGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressFCQGrp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQGrpMCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQGrpBCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQGrpUnknown"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCQGrp"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCQGrpQueue"))
)
if mibBuilder.loadTexts:
    tQosQGrpFCGroup.setStatus("current")

tmnxQosNetworkV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 35)
)
tmnxQosNetworkV7v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemarkDscp"),
        ("TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCForceDEValue"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCDEMark"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePortAvgOverhead"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV7v0Group.setStatus("current")

tmnxQosHsmdaV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 36)
)
tmnxQosHsmdaV7v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyMaxRate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp2Rate"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaPacketOffset"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefFCHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolSystemReserve"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot1AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot2AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot3AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot4AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot5AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot6AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot7AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot8AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeQueueMbs"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxProbability"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxProbability"),
        ("TIMETRA-QOS-MIB", "tSapIngrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tSapEgrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyGrpTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCritHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritProtocol"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDSCP"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritFragment"),
        ("TIMETRA-QOS-MIB", "tSapEgressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaPacketOffset"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionFC"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPfc"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPprofile"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecProfile"))
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaV7v0Group.setStatus("obsolete")

tmnxQosSapAtmV7v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 37)
)
tmnxQosSapAtmV7v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaAtmVci")
)
if mibBuilder.loadTexts:
    tmnxQosSapAtmV7v0Group.setStatus("current")

tmnxQosMcFrIngrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 38)
)
tmnxQosMcFrIngrGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tMcFrIngrProfDescription"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrProfLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrProfRowStatus"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrProfTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrClassReassemblyTmout"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrClassLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrIngrClassTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosMcFrIngrGroup.setStatus("current")

tmnxQosMcFrEgrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 39)
)
tmnxQosMcFrEgrGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tMcFrEgrProfDescription"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrProfLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrProfRowStatus"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrProfTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrClassMir"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrClassWeight"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrClassMaxSize"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrClassLastChanged"),
        ("TIMETRA-QOS-MIB", "tMcFrEgrClassTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosMcFrEgrGroup.setStatus("current")

tmnxQosSapEgrQWredGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 40)
)
tmnxQosSapEgrQWredGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressQueueXPWredQ"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueXPWredQSlope"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueXPWredQ"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueXPWredQSlope"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgrQWredGroup.setStatus("current")

tmnxQosSapIngressV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 41)
)
tmnxQosSapIngressV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCDE1OutOfProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpTableLastChange"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV8v0Group.setStatus("obsolete")

tmnxQosPolicerV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 42)
)
tmnxQosPolicerV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolDescr"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolLastChgd"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerPktOffset"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerDescr"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerPIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerParent"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerStatMode"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerCBS"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerMBS"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerPktOffset"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerDescr"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerPIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerParent"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerStatMode"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerCBS"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastPolicer"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastPolicer"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCPolicer"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownPolicer"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterDescr"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterLastChgd"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterLevel"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterParent"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterRate"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tQosPolicerArbiterWeight"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolMinMBSSep"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolRootMaxRate"),
        ("TIMETRA-QOS-MIB", "tQosPolicerLevelCumMBS"),
        ("TIMETRA-QOS-MIB", "tQosPolicerLevelLastChgd"),
        ("TIMETRA-QOS-MIB", "tQosPolicerLevelTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCPolicer"),
        ("TIMETRA-QOS-MIB", "tQosPolicerLevelFixedMBS"))
)
if mibBuilder.loadTexts:
    tmnxQosPolicerV8v0Group.setStatus("current")

tQosQGrpV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 43)
)
tQosQGrpV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosEgrQGroupFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupFCQueue"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMBSBytes"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueMBSBytes"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueMBSBytes"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMBSBytes"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminPIRPercent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminCIRPercent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueRateType"))
)
if mibBuilder.loadTexts:
    tQosQGrpV8v0Group.setStatus("current")

tQosFCQGrpFC8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 44)
)
tQosFCQGrpFC8v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tSapEgressFCQGrpFC")
)
if mibBuilder.loadTexts:
    tQosFCQGrpFC8v0Group.setStatus("current")

tmnxQosSapEgressV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 45)
)
tmnxQosSapEgressV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PInProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDot1POutProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCForceDEValue"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCDEMark"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePortAvgOverhead"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueuePoolName"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV8v0Group.setStatus("current")

tmnxQosQueueObjV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 46)
)
tmnxQosQueueObjV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosEgrQGroupDescr"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrQGroupTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueLevel"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueParent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortCIRWght"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortLvl"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePortWght"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueUsePortParent"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueWeight"),
        ("TIMETRA-QOS-MIB", "tQosIngQTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupDescr"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosIngQGroupTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCBS"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueLevel"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMCast"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMode"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueParent"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tQosIngQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueWeight"))
)
if mibBuilder.loadTexts:
    tmnxQosQueueObjV8v0Group.setStatus("current")

tmnxQosObsoletedV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 47)
)
tmnxQosObsoletedV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueMBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueMBS"))
)
if mibBuilder.loadTexts:
    tmnxQosObsoletedV8v0Group.setStatus("current")

tmnxQosPortSchPlcyGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 48)
)
tmnxQosPortSchPlcyGrpGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tPortSchPlcyLvl1GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl1GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl2GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl2GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl3GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl3GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl4GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl4GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl5GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl5GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl6GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl6GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl7GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl7GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl8GrpName"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvl8GrpWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvlGrpLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyLvlGrpTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyGrpAdminCIR"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyGrpAdminPIR"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyGrpLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyGrpRowStatus"),
        ("TIMETRA-QOS-MIB", "tPortSchPlcyGrpTblLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxQosPortSchPlcyGrpGroup.setStatus("current")

tmnxQosSchedulerV8v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 49)
)
tmnxQosSchedulerV8v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSchedulerPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tSchedulerPolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerRowStatus"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerDescription"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerParent"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRLevel"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIRWeight"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerSummedCIR"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerLastChanged"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerUsePortParent"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortLvl"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortWght"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRLvl"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRWght"),
        ("TIMETRA-QOS-MIB", "tVirtualSchedulerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyRowStatus"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyDescription"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyLastChanged"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyMaxRate"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanLvl"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanWeight"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRLvl"),
        ("TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRWght"))
)
if mibBuilder.loadTexts:
    tmnxQosSchedulerV8v0Group.setStatus("current")

tmnxQosBurstLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 50)
)
tmnxQosBurstLimitGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressQueueBurstLimit"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueBurstLimit"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueBurstLimit"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueBurstLimit"))
)
if mibBuilder.loadTexts:
    tmnxQosBurstLimitGroup.setStatus("current")

tmnxQosMacCritVidFltrV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 51)
)
tmnxQosMacCritVidFltrV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressMacCritInnerTagValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCritInnerTagMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCritOuterTagValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCritOuterTagMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCritType"))
)
if mibBuilder.loadTexts:
    tmnxQosMacCritVidFltrV9v0Group.setStatus("current")

tmnxQosSapEgressV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 52)
)
tmnxQosSapEgressV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressQueuePktOffset"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueRateType"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV9v0Group.setStatus("current")

tmnxQosSapIngressV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 53)
)
tmnxQosSapIngressV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueRateType"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV9v0Group.setStatus("current")

tmnxQosPolicerV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 54)
)
tmnxQosPolicerV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngPolicerAdminCIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerAdminPIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerRateType"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerAdminCIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerAdminPIRPercent"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerRateType"))
)
if mibBuilder.loadTexts:
    tmnxQosPolicerV9v0Group.setStatus("current")

tmnxQosAtmTdpV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 55)
)
tmnxQosAtmTdpV9v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tAtmTdpWeight")
)
if mibBuilder.loadTexts:
    tmnxQosAtmTdpV9v0Group.setStatus("current")

tmnxQosHsmdaV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 56)
)
tmnxQosHsmdaV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyIncludeQueues"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicySchedUsingClass"),
        ("TIMETRA-QOS-MIB", "tHsmdaWrrPolicyAggWeightAtClass"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyEHWrrPlcy"),
        ("TIMETRA-QOS-MIB", "tNetworkQueuePolicyEHPktBOffst"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueuePIRPercent"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueWrrWeight"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueMBS"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaLowBrstMaxCls"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaWrrPolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueWrrWeight"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueMBS"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueBurstLimit"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrHsmdaQueueBurstLimit"))
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaV9v0Group.setStatus("current")

tmnxQosNetworkV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 57)
)
tmnxQosNetworkV9v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tNetworkQueueFCEgrHsmdaQueue")
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV9v0Group.setStatus("current")

tmnxQosNamedPoolV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 58)
)
tmnxQosNamedPoolV9v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tQ1NamedPoolResvCbsAmbrAlrmStep"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolResvCbsAmbrAlrmMax"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolAmbrAlrmThresh"),
        ("TIMETRA-QOS-MIB", "tQ1NamedPoolRedAlrmThresh"))
)
if mibBuilder.loadTexts:
    tmnxQosNamedPoolV9v0Group.setStatus("current")

tmnxQosHsmdaObsoletedV9v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 59)
)
tmnxQosHsmdaObsoletedV9v0Group.setObjects(
    ("TIMETRA-QOS-MIB", "tSapEgressFCDot1PHsmdaProfile")
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaObsoletedV9v0Group.setStatus("current")

tmnxQosPolicyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 60)
)
tmnxQosPolicyV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgrPolicyNameId"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicyNameLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicyNameRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicyNameTableLastChgd"),
        ("TIMETRA-QOS-MIB", "tSapEgressPolicyName"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicyNameId"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicyNameLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicyNameRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicyNameTableLastChgd"),
        ("TIMETRA-QOS-MIB", "tSapIngressPolicyName"))
)
if mibBuilder.loadTexts:
    tmnxQosPolicyV10v0Group.setStatus("current")

tmnxQosQueueGrpPolcrV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 61)
)
tmnxQosQueueGrpPolcrV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosIngPolicerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerDescr"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerPIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerParent"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerLevel"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerWeight"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerCBS"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerMBS"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerPktOffset"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerProfileCapped"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerStatMode"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerRowStatus"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerDescr"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerPIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerParent"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerLevel"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerWeight"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerAdminPIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerAdminCIR"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerCBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerMBS"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerPktOffset"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerProfileCapped"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerStatMode"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCPlcrFPQGrp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastPlcrFPQGrp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastPlcrFPQGrp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownPlcrFPQGrp"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressFCQGrpPolicer"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressFCTableLstChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressFCMultiCastPlcr"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressFCUniCastPlcr"),
        ("TIMETRA-QOS-MIB", "tNetworkIngressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueuePktOffset"),
        ("TIMETRA-QOS-MIB", "tQosPolicerCtrlPolProfPref"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerProfileCapped"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerProfileCapped"))
)
if mibBuilder.loadTexts:
    tmnxQosQueueGrpPolcrV10v0Group.setStatus("current")

tmnxQosEgrReClassifyV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 62)
)
tmnxQosEgrReClassifyV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapEgressEthernetCtag"),
        ("TIMETRA-QOS-MIB", "tSapEgressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tSapEgressDot1pProfile"))
)
if mibBuilder.loadTexts:
    tmnxQosEgrReClassifyV10v0Group.setStatus("current")

tmnxQosPolicerSlopeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 63)
)
tmnxQosPolicerSlopeGroup.setObjects(
      *(("TIMETRA-QOS-MIB", "tQosEgrPolicerSlopeMap"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerSlopeMaxDepth"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerSlopeMaxProb"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerSlopeStartDepth"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerSlopeMap"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerSlopeMaxDepth"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerSlopeMaxProb"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerSlopeStartDepth"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerSlopeMap"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerSlopeMaxDepth"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerSlopeMaxProb"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerSlopeStartDepth"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerSlopeMap"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerSlopeMaxDepth"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerSlopeMaxProb"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerSlopeStartDepth"))
)
if mibBuilder.loadTexts:
    tmnxQosPolicerSlopeGroup.setStatus("current")

tmnxQosAdvConfigV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 64)
)
tmnxQosAdvConfigV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tAdvCfgPolicyTblLastChgd"),
        ("TIMETRA-QOS-MIB", "tAdvCfgPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tAdvCfgLastChanged"),
        ("TIMETRA-QOS-MIB", "tAdvCfgDescription"),
        ("TIMETRA-QOS-MIB", "tAdvCfgChildAdmnPirPrcnt"),
        ("TIMETRA-QOS-MIB", "tAdvCfgChildAdminRate"),
        ("TIMETRA-QOS-MIB", "tAdvCfgOMGranPirPrcnt"),
        ("TIMETRA-QOS-MIB", "tAdvCfgOMGranRate"),
        ("TIMETRA-QOS-MIB", "tAdvCfgMaxDecPirPrcnt"),
        ("TIMETRA-QOS-MIB", "tAdvCfgMaxDecRate"),
        ("TIMETRA-QOS-MIB", "tAdvCfgHiRateHoldTime"),
        ("TIMETRA-QOS-MIB", "tAdvCfgTimeAvgFactor"),
        ("TIMETRA-QOS-MIB", "tAdvCfgSampleInterval"),
        ("TIMETRA-QOS-MIB", "tAdvCfgFastStart"),
        ("TIMETRA-QOS-MIB", "tAdvCfgFastStop"),
        ("TIMETRA-QOS-MIB", "tAdvCfgAbvOffCapPirPrcnt"),
        ("TIMETRA-QOS-MIB", "tAdvCfgAbvOffCapRate"),
        ("TIMETRA-QOS-MIB", "tAdvCfgBWDGranPirPrcnt"),
        ("TIMETRA-QOS-MIB", "tAdvCfgBWDGranRate"),
        ("TIMETRA-QOS-MIB", "tQosEgrPolicerAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tQosIngPolicerAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tQosEgrQueueAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tQosIngQueueAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgrPolicerAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngPolicerAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgressQueueAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdvCfgPolicy"),
        ("TIMETRA-QOS-MIB", "tAdvCfgMinOnly"),
        ("TIMETRA-QOS-MIB", "tAdvCfgDecOnly"))
)
if mibBuilder.loadTexts:
    tmnxQosAdvConfigV10v0Group.setStatus("current")

tmnxQosHsmdaV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 65)
)
tmnxQosHsmdaV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyMaxRate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8GrpId"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8WgtInGrp"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp1Rate"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp2Rate"),
        ("TIMETRA-QOS-MIB", "tSapEgressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolSystemReserve"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot1AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot2AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot3AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot4AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot5AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot6AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot7AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolRoot8AllocWeight"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass1AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass2AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass3AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass4AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass5AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass6AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass7AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8Parent"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolClass8AllocPercent"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyRowStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLastChanged"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeDescription"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeHiMaxProbability"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoAdminStatus"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoStartDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxDepth"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopeLoMaxProbability"),
        ("TIMETRA-QOS-MIB", "tSapEgrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedPlcyGrpTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaPoolPlcyTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tHsmdaSlopePolicyTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecHsmdaCntrOverride"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDescription"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddrType"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritProtocol"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritDSCP"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritFragment"),
        ("TIMETRA-QOS-MIB", "tSapEgressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaPacketOffset"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionFC"),
        ("TIMETRA-QOS-MIB", "tSapEgrIPCritActionProfile"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPfc"),
        ("TIMETRA-QOS-MIB", "tSapEgressDSCPprofile"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapEgressPrecProfile"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyBrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp1BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyGrp2BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl1BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl2BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl3BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl4BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl5BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl6BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl7BrstLimit"),
        ("TIMETRA-QOS-MIB", "tHsmdaSchedulerPlcyLvl8BrstLimit"))
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaV10v0Group.setStatus("current")

tmnxQosNetworkV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 66)
)
tmnxQosNetworkV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tNetworkEgressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressDSCPProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressPrecFC"),
        ("TIMETRA-QOS-MIB", "tNetworkEgressPrecProfile"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tNetworkEgrPrecTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV10v0Group.setStatus("current")

tmnxQosSapIngressV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 68)
)
tmnxQosSapIngressV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoolName"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCDE1OutOfProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpFC"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpFCPriority"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpTableLastChange"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV10v0Group.setStatus("current")

tmnxQosHsmdaObsoletedV10v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 69)
)
tmnxQosHsmdaObsoletedV10v0Group.setObjects(
      *(("TIMETRA-QOS-MIB", "tHsmdaSlopeQueueMbs"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaPacketOffset"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaMCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressFCHsmdaBCastQueue"),
        ("TIMETRA-QOS-MIB", "tSapIngressDefFCHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDot1pHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressPrecHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressDSCPHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressLspExpHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapIngressIPCritHsmdaCntrOvr"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapEgressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngrHsmdaQueueTblLastChngd"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueRowStatus"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueLastChanged"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueCIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePIRAdaptn"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminPIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueAdminCIR"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueueSlopePolicy"),
        ("TIMETRA-QOS-MIB", "tSapIngressHsmdaQueuePoliced"))
)
if mibBuilder.loadTexts:
    tmnxQosHsmdaObsoletedV10v0Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tmnxQos7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxQos7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxQos7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxQos7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxQos7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxQos7450V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxQos7750V6v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 10)
)
if mibBuilder.loadTexts:
    tmnxQos7450V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxQos77x0V6v1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 11)
)
if mibBuilder.loadTexts:
    tmnxQos77x0V6v1Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 12)
)
if mibBuilder.loadTexts:
    tmnxQos7450V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos77x0V7v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 13)
)
if mibBuilder.loadTexts:
    tmnxQos77x0V7v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 14)
)
if mibBuilder.loadTexts:
    tmnxQos7450V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos77x0V8v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 15)
)
if mibBuilder.loadTexts:
    tmnxQos77x0V8v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos77x0V9v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 16)
)
if mibBuilder.loadTexts:
    tmnxQos77x0V9v0Compliance.setStatus(
        "obsolete"
    )

tmnxQos7450V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 17)
)
if mibBuilder.loadTexts:
    tmnxQos7450V10v0Compliance.setStatus(
        "current"
    )

tmnxQos77x0V10v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 18)
)
if mibBuilder.loadTexts:
    tmnxQos77x0V10v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-QOS-MIB",
    **{"TmnxMcFrClassIndex": TmnxMcFrClassIndex,
       "timetraQosMIBModule": timetraQosMIBModule,
       "tmnxQosConformance": tmnxQosConformance,
       "tmnxQosCompliances": tmnxQosCompliances,
       "tmnxQos7450V4v0Compliance": tmnxQos7450V4v0Compliance,
       "tmnxQos7750V4v0Compliance": tmnxQos7750V4v0Compliance,
       "tmnxQos7450V5v0Compliance": tmnxQos7450V5v0Compliance,
       "tmnxQos7750V5v0Compliance": tmnxQos7750V5v0Compliance,
       "tmnxQos7450V6v0Compliance": tmnxQos7450V6v0Compliance,
       "tmnxQos7750V6v0Compliance": tmnxQos7750V6v0Compliance,
       "tmnxQos7450V6v1Compliance": tmnxQos7450V6v1Compliance,
       "tmnxQos77x0V6v1Compliance": tmnxQos77x0V6v1Compliance,
       "tmnxQos7450V7v0Compliance": tmnxQos7450V7v0Compliance,
       "tmnxQos77x0V7v0Compliance": tmnxQos77x0V7v0Compliance,
       "tmnxQos7450V8v0Compliance": tmnxQos7450V8v0Compliance,
       "tmnxQos77x0V8v0Compliance": tmnxQos77x0V8v0Compliance,
       "tmnxQos77x0V9v0Compliance": tmnxQos77x0V9v0Compliance,
       "tmnxQos7450V10v0Compliance": tmnxQos7450V10v0Compliance,
       "tmnxQos77x0V10v0Compliance": tmnxQos77x0V10v0Compliance,
       "tmnxQosGroups": tmnxQosGroups,
       "tmnxQosGlobalGroup": tmnxQosGlobalGroup,
       "tmnxQosDSCPGroup": tmnxQosDSCPGroup,
       "tmnxQosFCGroup": tmnxQosFCGroup,
       "tmnxQosSlopeGroup": tmnxQosSlopeGroup,
       "tmnxQosSchedulerGroup": tmnxQosSchedulerGroup,
       "tQosObsoleteObjectsGroup": tQosObsoleteObjectsGroup,
       "tmnxQosSapEgressR2r1Group": tmnxQosSapEgressR2r1Group,
       "tmnxQosNetworkR2r1Group": tmnxQosNetworkR2r1Group,
       "tmnxQosAtmTdpV3v0Group": tmnxQosAtmTdpV3v0Group,
       "tmnxQosSapIpv6FilterR4r0Group": tmnxQosSapIpv6FilterR4r0Group,
       "tmnxQosQueueV4v0Group": tmnxQosQueueV4v0Group,
       "tmnxQosSapIngressV4v0Group": tmnxQosSapIngressV4v0Group,
       "tmnxQosSchedulerV5v0Group": tmnxQosSchedulerV5v0Group,
       "tmnxQosSapEgressV5v0Group": tmnxQosSapEgressV5v0Group,
       "tmnxQosNetworkV5v0Group": tmnxQosNetworkV5v0Group,
       "tmnxQosHsmdaV6v0Group": tmnxQosHsmdaV6v0Group,
       "tmnxQosAtmTdpV5v0Group": tmnxQosAtmTdpV5v0Group,
       "tmnxQosSapIngressV6v0Group": tmnxQosSapIngressV6v0Group,
       "tmnxQosSapEgressV6v0Group": tmnxQosSapEgressV6v0Group,
       "tmnxQosNetworkV6v0Group": tmnxQosNetworkV6v0Group,
       "tmnxQosFrameBasedV6v0Group": tmnxQosFrameBasedV6v0Group,
       "tmnxQosObsoletedV6v0Group": tmnxQosObsoletedV6v0Group,
       "tmnxQosNamedPoolPolicyV6v0Group": tmnxQosNamedPoolPolicyV6v0Group,
       "tmnxQosMcMlpppIngrGroup": tmnxQosMcMlpppIngrGroup,
       "tmnxQosMcMlpppEgrGroup": tmnxQosMcMlpppEgrGroup,
       "tmnxQosQueueObjGroup": tmnxQosQueueObjGroup,
       "tQosQGrpFCGroup": tQosQGrpFCGroup,
       "tmnxQosNetworkV7v0Group": tmnxQosNetworkV7v0Group,
       "tmnxQosHsmdaV7v0Group": tmnxQosHsmdaV7v0Group,
       "tmnxQosSapAtmV7v0Group": tmnxQosSapAtmV7v0Group,
       "tmnxQosMcFrIngrGroup": tmnxQosMcFrIngrGroup,
       "tmnxQosMcFrEgrGroup": tmnxQosMcFrEgrGroup,
       "tmnxQosSapEgrQWredGroup": tmnxQosSapEgrQWredGroup,
       "tmnxQosSapIngressV8v0Group": tmnxQosSapIngressV8v0Group,
       "tmnxQosPolicerV8v0Group": tmnxQosPolicerV8v0Group,
       "tQosQGrpV8v0Group": tQosQGrpV8v0Group,
       "tQosFCQGrpFC8v0Group": tQosFCQGrpFC8v0Group,
       "tmnxQosSapEgressV8v0Group": tmnxQosSapEgressV8v0Group,
       "tmnxQosQueueObjV8v0Group": tmnxQosQueueObjV8v0Group,
       "tmnxQosObsoletedV8v0Group": tmnxQosObsoletedV8v0Group,
       "tmnxQosPortSchPlcyGrpGroup": tmnxQosPortSchPlcyGrpGroup,
       "tmnxQosSchedulerV8v0Group": tmnxQosSchedulerV8v0Group,
       "tmnxQosBurstLimitGroup": tmnxQosBurstLimitGroup,
       "tmnxQosMacCritVidFltrV9v0Group": tmnxQosMacCritVidFltrV9v0Group,
       "tmnxQosSapEgressV9v0Group": tmnxQosSapEgressV9v0Group,
       "tmnxQosSapIngressV9v0Group": tmnxQosSapIngressV9v0Group,
       "tmnxQosPolicerV9v0Group": tmnxQosPolicerV9v0Group,
       "tmnxQosAtmTdpV9v0Group": tmnxQosAtmTdpV9v0Group,
       "tmnxQosHsmdaV9v0Group": tmnxQosHsmdaV9v0Group,
       "tmnxQosNetworkV9v0Group": tmnxQosNetworkV9v0Group,
       "tmnxQosNamedPoolV9v0Group": tmnxQosNamedPoolV9v0Group,
       "tmnxQosHsmdaObsoletedV9v0Group": tmnxQosHsmdaObsoletedV9v0Group,
       "tmnxQosPolicyV10v0Group": tmnxQosPolicyV10v0Group,
       "tmnxQosQueueGrpPolcrV10v0Group": tmnxQosQueueGrpPolcrV10v0Group,
       "tmnxQosEgrReClassifyV10v0Group": tmnxQosEgrReClassifyV10v0Group,
       "tmnxQosPolicerSlopeGroup": tmnxQosPolicerSlopeGroup,
       "tmnxQosAdvConfigV10v0Group": tmnxQosAdvConfigV10v0Group,
       "tmnxQosHsmdaV10v0Group": tmnxQosHsmdaV10v0Group,
       "tmnxQosNetworkV10v0Group": tmnxQosNetworkV10v0Group,
       "tmnxQosSapIngressV10v0Group": tmnxQosSapIngressV10v0Group,
       "tmnxQosHsmdaObsoletedV10v0Group": tmnxQosHsmdaObsoletedV10v0Group,
       "tQosObjects": tQosObjects,
       "tDSCPObjects": tDSCPObjects,
       "tDSCPNameTable": tDSCPNameTable,
       "tDSCPNameEntry": tDSCPNameEntry,
       "tDSCPName": tDSCPName,
       "tDSCPNameRowStatus": tDSCPNameRowStatus,
       "tDSCPNameStorageType": tDSCPNameStorageType,
       "tDSCPNameDscpValue": tDSCPNameDscpValue,
       "tDSCPNameLastChanged": tDSCPNameLastChanged,
       "tFCObjects": tFCObjects,
       "tFCNameTable": tFCNameTable,
       "tFCNameEntry": tFCNameEntry,
       "tFCName": tFCName,
       "tFCRowStatus": tFCRowStatus,
       "tFCStorageType": tFCStorageType,
       "tFCValue": tFCValue,
       "tFCNameLastChanged": tFCNameLastChanged,
       "tSapIngressObjects": tSapIngressObjects,
       "tSapIngressTable": tSapIngressTable,
       "tSapIngressEntry": tSapIngressEntry,
       "tSapIngressIndex": tSapIngressIndex,
       "tSapIngressRowStatus": tSapIngressRowStatus,
       "tSapIngressScope": tSapIngressScope,
       "tSapIngressDescription": tSapIngressDescription,
       "tSapIngressDefaultFC": tSapIngressDefaultFC,
       "tSapIngressDefaultFCPriority": tSapIngressDefaultFCPriority,
       "tSapIngressMatchCriteria": tSapIngressMatchCriteria,
       "tSapIngressLastChanged": tSapIngressLastChanged,
       "tSapIngressHsmdaPacketOffset": tSapIngressHsmdaPacketOffset,
       "tSapIngressDefFCHsmdaCntrOvr": tSapIngressDefFCHsmdaCntrOvr,
       "tSapIngressMacCritType": tSapIngressMacCritType,
       "tSapIngressPolicyName": tSapIngressPolicyName,
       "tSapIngressQueueTable": tSapIngressQueueTable,
       "tSapIngressQueueEntry": tSapIngressQueueEntry,
       "tSapIngressQueue": tSapIngressQueue,
       "tSapIngressQueueRowStatus": tSapIngressQueueRowStatus,
       "tSapIngressQueueParent": tSapIngressQueueParent,
       "tSapIngressQueueLevel": tSapIngressQueueLevel,
       "tSapIngressQueueWeight": tSapIngressQueueWeight,
       "tSapIngressQueueCIRLevel": tSapIngressQueueCIRLevel,
       "tSapIngressQueueCIRWeight": tSapIngressQueueCIRWeight,
       "tSapIngressQueueMCast": tSapIngressQueueMCast,
       "tSapIngressQueueExpedite": tSapIngressQueueExpedite,
       "tSapIngressQueueCBS": tSapIngressQueueCBS,
       "tSapIngressQueueMBS": tSapIngressQueueMBS,
       "tSapIngressQueueHiPrioOnly": tSapIngressQueueHiPrioOnly,
       "tSapIngressQueuePIRAdaptation": tSapIngressQueuePIRAdaptation,
       "tSapIngressQueueCIRAdaptation": tSapIngressQueueCIRAdaptation,
       "tSapIngressQueueAdminPIR": tSapIngressQueueAdminPIR,
       "tSapIngressQueueAdminCIR": tSapIngressQueueAdminCIR,
       "tSapIngressQueueOperPIR": tSapIngressQueueOperPIR,
       "tSapIngressQueueOperCIR": tSapIngressQueueOperCIR,
       "tSapIngressQueueLastChanged": tSapIngressQueueLastChanged,
       "tSapIngressQueuePoliced": tSapIngressQueuePoliced,
       "tSapIngressQueueMode": tSapIngressQueueMode,
       "tSapIngressQueuePoolName": tSapIngressQueuePoolName,
       "tSapIngressQueueMBSBytes": tSapIngressQueueMBSBytes,
       "tSapIngressQueueBurstLimit": tSapIngressQueueBurstLimit,
       "tSapIngressQueueAdminPIRPercent": tSapIngressQueueAdminPIRPercent,
       "tSapIngressQueueAdminCIRPercent": tSapIngressQueueAdminCIRPercent,
       "tSapIngressQueueRateType": tSapIngressQueueRateType,
       "tSapIngressQueueAdvCfgPolicy": tSapIngressQueueAdvCfgPolicy,
       "tSapIngressDSCPTable": tSapIngressDSCPTable,
       "tSapIngressDSCPEntry": tSapIngressDSCPEntry,
       "tSapIngressDSCP": tSapIngressDSCP,
       "tSapIngressDSCPRowStatus": tSapIngressDSCPRowStatus,
       "tSapIngressDSCPFC": tSapIngressDSCPFC,
       "tSapIngressDSCPPriority": tSapIngressDSCPPriority,
       "tSapIngressDSCPLastChanged": tSapIngressDSCPLastChanged,
       "tSapIngressDSCPHsmdaCntrOvr": tSapIngressDSCPHsmdaCntrOvr,
       "tSapIngressDot1pTable": tSapIngressDot1pTable,
       "tSapIngressDot1pEntry": tSapIngressDot1pEntry,
       "tSapIngressDot1pValue": tSapIngressDot1pValue,
       "tSapIngressDot1pRowStatus": tSapIngressDot1pRowStatus,
       "tSapIngressDot1pFC": tSapIngressDot1pFC,
       "tSapIngressDot1pPriority": tSapIngressDot1pPriority,
       "tSapIngressDot1pLastChanged": tSapIngressDot1pLastChanged,
       "tSapIngressDot1pHsmdaCntrOvr": tSapIngressDot1pHsmdaCntrOvr,
       "tSapIngressIPCriteriaTable": tSapIngressIPCriteriaTable,
       "tSapIngressIPCriteriaEntry": tSapIngressIPCriteriaEntry,
       "tSapIngressIPCriteriaIndex": tSapIngressIPCriteriaIndex,
       "tSapIngressIPCriteriaRowStatus": tSapIngressIPCriteriaRowStatus,
       "tSapIngressIPCriteriaDescription": tSapIngressIPCriteriaDescription,
       "tSapIngressIPCriteriaActionFC": tSapIngressIPCriteriaActionFC,
       "tSapIngressIPCriteriaActionPriority": tSapIngressIPCriteriaActionPriority,
       "tSapIngressIPCriteriaSourceIpAddr": tSapIngressIPCriteriaSourceIpAddr,
       "tSapIngressIPCriteriaSourceIpMask": tSapIngressIPCriteriaSourceIpMask,
       "tSapIngressIPCriteriaDestIpAddr": tSapIngressIPCriteriaDestIpAddr,
       "tSapIngressIPCriteriaDestIpMask": tSapIngressIPCriteriaDestIpMask,
       "tSapIngressIPCriteriaProtocol": tSapIngressIPCriteriaProtocol,
       "tSapIngressIPCriteriaSourcePortValue1": tSapIngressIPCriteriaSourcePortValue1,
       "tSapIngressIPCriteriaSourcePortValue2": tSapIngressIPCriteriaSourcePortValue2,
       "tSapIngressIPCriteriaSourcePortOperator": tSapIngressIPCriteriaSourcePortOperator,
       "tSapIngressIPCriteriaDestPortValue1": tSapIngressIPCriteriaDestPortValue1,
       "tSapIngressIPCriteriaDestPortValue2": tSapIngressIPCriteriaDestPortValue2,
       "tSapIngressIPCriteriaDestPortOperator": tSapIngressIPCriteriaDestPortOperator,
       "tSapIngressIPCriteriaDSCP": tSapIngressIPCriteriaDSCP,
       "tSapIngressIPCriteriaFragment": tSapIngressIPCriteriaFragment,
       "tSapIngressIPCriteriaLastChanged": tSapIngressIPCriteriaLastChanged,
       "tSapIngressIPCritHsmdaCntrOvr": tSapIngressIPCritHsmdaCntrOvr,
       "tSapIngressIPCriteriaIpPrecValue": tSapIngressIPCriteriaIpPrecValue,
       "tSapIngressIPCriteriaIpPrecMask": tSapIngressIPCriteriaIpPrecMask,
       "tSapIngressMacCriteriaTable": tSapIngressMacCriteriaTable,
       "tSapIngressMacCriteriaEntry": tSapIngressMacCriteriaEntry,
       "tSapIngressMacCriteriaIndex": tSapIngressMacCriteriaIndex,
       "tSapIngressMacCriteriaRowStatus": tSapIngressMacCriteriaRowStatus,
       "tSapIngressMacCriteriaDescription": tSapIngressMacCriteriaDescription,
       "tSapIngressMacCriteriaActionFC": tSapIngressMacCriteriaActionFC,
       "tSapIngressMacCriteriaActionPriority": tSapIngressMacCriteriaActionPriority,
       "tSapIngressMacCriteriaFrameType": tSapIngressMacCriteriaFrameType,
       "tSapIngressMacCriteriaSrcMacAddr": tSapIngressMacCriteriaSrcMacAddr,
       "tSapIngressMacCriteriaSrcMacMask": tSapIngressMacCriteriaSrcMacMask,
       "tSapIngressMacCriteriaDstMacAddr": tSapIngressMacCriteriaDstMacAddr,
       "tSapIngressMacCriteriaDstMacMask": tSapIngressMacCriteriaDstMacMask,
       "tSapIngressMacCriteriaDot1PValue": tSapIngressMacCriteriaDot1PValue,
       "tSapIngressMacCriteriaDot1PMask": tSapIngressMacCriteriaDot1PMask,
       "tSapIngressMacCriteriaEthernetType": tSapIngressMacCriteriaEthernetType,
       "tSapIngressMacCriteriaDSAP": tSapIngressMacCriteriaDSAP,
       "tSapIngressMacCriteriaDSAPMask": tSapIngressMacCriteriaDSAPMask,
       "tSapIngressMacCriteriaSSAP": tSapIngressMacCriteriaSSAP,
       "tSapIngressMacCriteriaSSAPMask": tSapIngressMacCriteriaSSAPMask,
       "tSapIngressMacCriteriaSnapPid": tSapIngressMacCriteriaSnapPid,
       "tSapIngressMacCriteriaSnapOui": tSapIngressMacCriteriaSnapOui,
       "tSapIngressMacCriteriaLastChanged": tSapIngressMacCriteriaLastChanged,
       "tSapIngressMacCriteriaAtmVci": tSapIngressMacCriteriaAtmVci,
       "tSapIngressMacCritInnerTagValue": tSapIngressMacCritInnerTagValue,
       "tSapIngressMacCritInnerTagMask": tSapIngressMacCritInnerTagMask,
       "tSapIngressMacCritOuterTagValue": tSapIngressMacCritOuterTagValue,
       "tSapIngressMacCritOuterTagMask": tSapIngressMacCritOuterTagMask,
       "tSapIngressFCTable": tSapIngressFCTable,
       "tSapIngressFCEntry": tSapIngressFCEntry,
       "tSapIngressFCName": tSapIngressFCName,
       "tSapIngressFCRowStatus": tSapIngressFCRowStatus,
       "tSapIngressFCQueue": tSapIngressFCQueue,
       "tSapIngressFCMCastQueue": tSapIngressFCMCastQueue,
       "tSapIngressFCBCastQueue": tSapIngressFCBCastQueue,
       "tSapIngressFCUnknownQueue": tSapIngressFCUnknownQueue,
       "tSapIngressFCLastChanged": tSapIngressFCLastChanged,
       "tSapIngressFCInProfRemark": tSapIngressFCInProfRemark,
       "tSapIngressFCInProfDscp": tSapIngressFCInProfDscp,
       "tSapIngressFCInProfPrec": tSapIngressFCInProfPrec,
       "tSapIngressFCOutProfRemark": tSapIngressFCOutProfRemark,
       "tSapIngressFCOutProfDscp": tSapIngressFCOutProfDscp,
       "tSapIngressFCOutProfPrec": tSapIngressFCOutProfPrec,
       "tSapIngressFCProfile": tSapIngressFCProfile,
       "tSapIngressFCHsmdaQueue": tSapIngressFCHsmdaQueue,
       "tSapIngressFCHsmdaMCastQueue": tSapIngressFCHsmdaMCastQueue,
       "tSapIngressFCHsmdaBCastQueue": tSapIngressFCHsmdaBCastQueue,
       "tSapIngressFCDE1OutOfProfile": tSapIngressFCDE1OutOfProfile,
       "tSapIngressFCQGrp": tSapIngressFCQGrp,
       "tSapIngressFCQGrpMCast": tSapIngressFCQGrpMCast,
       "tSapIngressFCQGrpBCast": tSapIngressFCQGrpBCast,
       "tSapIngressFCQGrpUnknown": tSapIngressFCQGrpUnknown,
       "tSapIngressFCPolicer": tSapIngressFCPolicer,
       "tSapIngressFCMCastPolicer": tSapIngressFCMCastPolicer,
       "tSapIngressFCBCastPolicer": tSapIngressFCBCastPolicer,
       "tSapIngressFCUnknownPolicer": tSapIngressFCUnknownPolicer,
       "tSapIngressFCPlcrFPQGrp": tSapIngressFCPlcrFPQGrp,
       "tSapIngressFCMCastPlcrFPQGrp": tSapIngressFCMCastPlcrFPQGrp,
       "tSapIngressFCBCastPlcrFPQGrp": tSapIngressFCBCastPlcrFPQGrp,
       "tSapIngressFCUnknownPlcrFPQGrp": tSapIngressFCUnknownPlcrFPQGrp,
       "tSapIngressPrecTable": tSapIngressPrecTable,
       "tSapIngressPrecEntry": tSapIngressPrecEntry,
       "tSapIngressPrecValue": tSapIngressPrecValue,
       "tSapIngressPrecRowStatus": tSapIngressPrecRowStatus,
       "tSapIngressPrecFC": tSapIngressPrecFC,
       "tSapIngressPrecFCPriority": tSapIngressPrecFCPriority,
       "tSapIngressPrecLastChanged": tSapIngressPrecLastChanged,
       "tSapIngressPrecHsmdaCntrOvr": tSapIngressPrecHsmdaCntrOvr,
       "tSapIngressIPv6CriteriaTable": tSapIngressIPv6CriteriaTable,
       "tSapIngressIPv6CriteriaEntry": tSapIngressIPv6CriteriaEntry,
       "tSapIngressIPv6CriteriaIndex": tSapIngressIPv6CriteriaIndex,
       "tSapIngressIPv6CriteriaRowStatus": tSapIngressIPv6CriteriaRowStatus,
       "tSapIngressIPv6CriteriaDescription": tSapIngressIPv6CriteriaDescription,
       "tSapIngressIPv6CriteriaActionFC": tSapIngressIPv6CriteriaActionFC,
       "tSapIngressIPv6CriteriaActionPriority": tSapIngressIPv6CriteriaActionPriority,
       "tSapIngressIPv6CriteriaSourceIpAddr": tSapIngressIPv6CriteriaSourceIpAddr,
       "tSapIngressIPv6CriteriaSourceIpMask": tSapIngressIPv6CriteriaSourceIpMask,
       "tSapIngressIPv6CriteriaDestIpAddr": tSapIngressIPv6CriteriaDestIpAddr,
       "tSapIngressIPv6CriteriaDestIpMask": tSapIngressIPv6CriteriaDestIpMask,
       "tSapIngressIPv6CriteriaNextHeader": tSapIngressIPv6CriteriaNextHeader,
       "tSapIngressIPv6CriteriaSourcePortValue1": tSapIngressIPv6CriteriaSourcePortValue1,
       "tSapIngressIPv6CriteriaSourcePortValue2": tSapIngressIPv6CriteriaSourcePortValue2,
       "tSapIngressIPv6CriteriaSourcePortOperator": tSapIngressIPv6CriteriaSourcePortOperator,
       "tSapIngressIPv6CriteriaDestPortValue1": tSapIngressIPv6CriteriaDestPortValue1,
       "tSapIngressIPv6CriteriaDestPortValue2": tSapIngressIPv6CriteriaDestPortValue2,
       "tSapIngressIPv6CriteriaDestPortOperator": tSapIngressIPv6CriteriaDestPortOperator,
       "tSapIngressIPv6CriteriaDSCP": tSapIngressIPv6CriteriaDSCP,
       "tSapIngressIPv6CriteriaLastChanged": tSapIngressIPv6CriteriaLastChanged,
       "tSapIngressIPv6CriteriaIpPrecValue": tSapIngressIPv6CriteriaIpPrecValue,
       "tSapIngressIPv6CriteriaIpPrecMask": tSapIngressIPv6CriteriaIpPrecMask,
       "tSapIngressHsmdaQueueTable": tSapIngressHsmdaQueueTable,
       "tSapIngressHsmdaQueueEntry": tSapIngressHsmdaQueueEntry,
       "tSapIngressHsmdaQueue": tSapIngressHsmdaQueue,
       "tSapIngressHsmdaQueueRowStatus": tSapIngressHsmdaQueueRowStatus,
       "tSapIngressHsmdaQueueLastChanged": tSapIngressHsmdaQueueLastChanged,
       "tSapIngressHsmdaQueueCIRAdaptn": tSapIngressHsmdaQueueCIRAdaptn,
       "tSapIngressHsmdaQueuePIRAdaptn": tSapIngressHsmdaQueuePIRAdaptn,
       "tSapIngressHsmdaQueueAdminPIR": tSapIngressHsmdaQueueAdminPIR,
       "tSapIngressHsmdaQueueAdminCIR": tSapIngressHsmdaQueueAdminCIR,
       "tSapIngressHsmdaQueueSlopePolicy": tSapIngressHsmdaQueueSlopePolicy,
       "tSapIngressHsmdaQueuePoliced": tSapIngressHsmdaQueuePoliced,
       "tSapIngressLspExpTable": tSapIngressLspExpTable,
       "tSapIngressLspExpEntry": tSapIngressLspExpEntry,
       "tSapIngressLspExpValue": tSapIngressLspExpValue,
       "tSapIngressLspExpRowStatus": tSapIngressLspExpRowStatus,
       "tSapIngressLspExpLastChanged": tSapIngressLspExpLastChanged,
       "tSapIngressLspExpFC": tSapIngressLspExpFC,
       "tSapIngressLspExpFCPriority": tSapIngressLspExpFCPriority,
       "tSapIngressLspExpHsmdaCntrOvr": tSapIngressLspExpHsmdaCntrOvr,
       "tSapIngPolicerTable": tSapIngPolicerTable,
       "tSapIngPolicerEntry": tSapIngPolicerEntry,
       "tSapIngPolicerId": tSapIngPolicerId,
       "tSapIngPolicerRowStatus": tSapIngPolicerRowStatus,
       "tSapIngPolicerLastChanged": tSapIngPolicerLastChanged,
       "tSapIngPolicerDescr": tSapIngPolicerDescr,
       "tSapIngPolicerPIRAdaptation": tSapIngPolicerPIRAdaptation,
       "tSapIngPolicerCIRAdaptation": tSapIngPolicerCIRAdaptation,
       "tSapIngPolicerParent": tSapIngPolicerParent,
       "tSapIngPolicerLevel": tSapIngPolicerLevel,
       "tSapIngPolicerWeight": tSapIngPolicerWeight,
       "tSapIngPolicerAdminPIR": tSapIngPolicerAdminPIR,
       "tSapIngPolicerAdminCIR": tSapIngPolicerAdminCIR,
       "tSapIngPolicerStatMode": tSapIngPolicerStatMode,
       "tSapIngPolicerMBS": tSapIngPolicerMBS,
       "tSapIngPolicerHiPrioOnly": tSapIngPolicerHiPrioOnly,
       "tSapIngPolicerCBS": tSapIngPolicerCBS,
       "tSapIngPolicerPktOffset": tSapIngPolicerPktOffset,
       "tSapIngPolicerAdminPIRPercent": tSapIngPolicerAdminPIRPercent,
       "tSapIngPolicerAdminCIRPercent": tSapIngPolicerAdminCIRPercent,
       "tSapIngPolicerRateType": tSapIngPolicerRateType,
       "tSapIngPolicerSlopeStartDepth": tSapIngPolicerSlopeStartDepth,
       "tSapIngPolicerSlopeMaxDepth": tSapIngPolicerSlopeMaxDepth,
       "tSapIngPolicerSlopeMaxProb": tSapIngPolicerSlopeMaxProb,
       "tSapIngPolicerSlopeMap": tSapIngPolicerSlopeMap,
       "tSapIngPolicerAdvCfgPolicy": tSapIngPolicerAdvCfgPolicy,
       "tSapIngPolicerProfileCapped": tSapIngPolicerProfileCapped,
       "tSapIngPolicyNameTable": tSapIngPolicyNameTable,
       "tSapIngPolicyNameEntry": tSapIngPolicyNameEntry,
       "tSapIngPolicyNameId": tSapIngPolicyNameId,
       "tSapIngPolicyNameRowStatus": tSapIngPolicyNameRowStatus,
       "tSapIngPolicyNameLastChanged": tSapIngPolicyNameLastChanged,
       "tSapEgressObjects": tSapEgressObjects,
       "tSapEgressTable": tSapEgressTable,
       "tSapEgressEntry": tSapEgressEntry,
       "tSapEgressIndex": tSapEgressIndex,
       "tSapEgressRowStatus": tSapEgressRowStatus,
       "tSapEgressScope": tSapEgressScope,
       "tSapEgressDescription": tSapEgressDescription,
       "tSapEgressLastChanged": tSapEgressLastChanged,
       "tSapEgressHsmdaPacketOffset": tSapEgressHsmdaPacketOffset,
       "tSapEgressMatchCriteria": tSapEgressMatchCriteria,
       "tSapEgressHsmdaWrrPolicy": tSapEgressHsmdaWrrPolicy,
       "tSapEgressHsmdaLowBrstMaxCls": tSapEgressHsmdaLowBrstMaxCls,
       "tSapEgressPolicyName": tSapEgressPolicyName,
       "tSapEgressEthernetCtag": tSapEgressEthernetCtag,
       "tSapEgressQueueTable": tSapEgressQueueTable,
       "tSapEgressQueueEntry": tSapEgressQueueEntry,
       "tSapEgressQueueIndex": tSapEgressQueueIndex,
       "tSapEgressQueueRowStatus": tSapEgressQueueRowStatus,
       "tSapEgressQueueParent": tSapEgressQueueParent,
       "tSapEgressQueueLevel": tSapEgressQueueLevel,
       "tSapEgressQueueWeight": tSapEgressQueueWeight,
       "tSapEgressQueueCIRLevel": tSapEgressQueueCIRLevel,
       "tSapEgressQueueCIRWeight": tSapEgressQueueCIRWeight,
       "tSapEgressQueueExpedite": tSapEgressQueueExpedite,
       "tSapEgressQueueCBS": tSapEgressQueueCBS,
       "tSapEgressQueueMBS": tSapEgressQueueMBS,
       "tSapEgressQueueHiPrioOnly": tSapEgressQueueHiPrioOnly,
       "tSapEgressQueuePIRAdaptation": tSapEgressQueuePIRAdaptation,
       "tSapEgressQueueCIRAdaptation": tSapEgressQueueCIRAdaptation,
       "tSapEgressQueueAdminPIR": tSapEgressQueueAdminPIR,
       "tSapEgressQueueAdminCIR": tSapEgressQueueAdminCIR,
       "tSapEgressQueueOperPIR": tSapEgressQueueOperPIR,
       "tSapEgressQueueOperCIR": tSapEgressQueueOperCIR,
       "tSapEgressQueueLastChanged": tSapEgressQueueLastChanged,
       "tSapEgressQueueUsePortParent": tSapEgressQueueUsePortParent,
       "tSapEgressQueuePortLvl": tSapEgressQueuePortLvl,
       "tSapEgressQueuePortWght": tSapEgressQueuePortWght,
       "tSapEgressQueuePortCIRLvl": tSapEgressQueuePortCIRLvl,
       "tSapEgressQueuePortCIRWght": tSapEgressQueuePortCIRWght,
       "tSapEgressQueuePortAvgOverhead": tSapEgressQueuePortAvgOverhead,
       "tSapEgressQueuePoolName": tSapEgressQueuePoolName,
       "tSapEgressQueueXPWredQ": tSapEgressQueueXPWredQ,
       "tSapEgressQueueXPWredQSlope": tSapEgressQueueXPWredQSlope,
       "tSapEgressQueueMBSBytes": tSapEgressQueueMBSBytes,
       "tSapEgressQueueBurstLimit": tSapEgressQueueBurstLimit,
       "tSapEgressQueuePktOffset": tSapEgressQueuePktOffset,
       "tSapEgressQueueAdminPIRPercent": tSapEgressQueueAdminPIRPercent,
       "tSapEgressQueueAdminCIRPercent": tSapEgressQueueAdminCIRPercent,
       "tSapEgressQueueRateType": tSapEgressQueueRateType,
       "tSapEgressQueueAdvCfgPolicy": tSapEgressQueueAdvCfgPolicy,
       "tSapEgressFCTable": tSapEgressFCTable,
       "tSapEgressFCEntry": tSapEgressFCEntry,
       "tSapEgressFCName": tSapEgressFCName,
       "tSapEgressFCRowStatus": tSapEgressFCRowStatus,
       "tSapEgressFCQueue": tSapEgressFCQueue,
       "tSapEgressFCDot1PValue": tSapEgressFCDot1PValue,
       "tSapEgressFCLastChanged": tSapEgressFCLastChanged,
       "tSapEgressFCHsmdaQueue": tSapEgressFCHsmdaQueue,
       "tSapEgressFCDot1PHsmdaProfile": tSapEgressFCDot1PHsmdaProfile,
       "tSapEgressFCDot1PInProfile": tSapEgressFCDot1PInProfile,
       "tSapEgressFCDot1POutProfile": tSapEgressFCDot1POutProfile,
       "tSapEgressFCForceDEValue": tSapEgressFCForceDEValue,
       "tSapEgressFCDEMark": tSapEgressFCDEMark,
       "tSapEgressFCInProfDscp": tSapEgressFCInProfDscp,
       "tSapEgressFCOutProfDscp": tSapEgressFCOutProfDscp,
       "tSapEgressFCInProfPrec": tSapEgressFCInProfPrec,
       "tSapEgressFCOutProfPrec": tSapEgressFCOutProfPrec,
       "tSapEgressFCQGrp": tSapEgressFCQGrp,
       "tSapEgressFCPolicer": tSapEgressFCPolicer,
       "tSapEgressFCQGrpFC": tSapEgressFCQGrpFC,
       "tSapEgressHsmdaQueueTable": tSapEgressHsmdaQueueTable,
       "tSapEgressHsmdaQueueEntry": tSapEgressHsmdaQueueEntry,
       "tSapEgressHsmdaQueue": tSapEgressHsmdaQueue,
       "tSapEgressHsmdaQueueRowStatus": tSapEgressHsmdaQueueRowStatus,
       "tSapEgressHsmdaQueueCIRAdaptn": tSapEgressHsmdaQueueCIRAdaptn,
       "tSapEgressHsmdaQueuePIRAdaptn": tSapEgressHsmdaQueuePIRAdaptn,
       "tSapEgressHsmdaQueueAdminPIR": tSapEgressHsmdaQueueAdminPIR,
       "tSapEgressHsmdaQueueAdminCIR": tSapEgressHsmdaQueueAdminCIR,
       "tSapEgressHsmdaQueueSlopePolicy": tSapEgressHsmdaQueueSlopePolicy,
       "tSapEgressHsmdaQueueLastChanged": tSapEgressHsmdaQueueLastChanged,
       "tSapEgressHsmdaQueueWrrWeight": tSapEgressHsmdaQueueWrrWeight,
       "tSapEgressHsmdaQueueMBS": tSapEgressHsmdaQueueMBS,
       "tSapEgressHsmdaQueueBurstLimit": tSapEgressHsmdaQueueBurstLimit,
       "tSapEgressDSCPTable": tSapEgressDSCPTable,
       "tSapEgressDSCPEntry": tSapEgressDSCPEntry,
       "tSapEgressDSCP": tSapEgressDSCP,
       "tSapEgressDSCPRowStatus": tSapEgressDSCPRowStatus,
       "tSapEgressDSCPLastChanged": tSapEgressDSCPLastChanged,
       "tSapEgressDSCPHsmdaCntrOverride": tSapEgressDSCPHsmdaCntrOverride,
       "tSapEgressDSCPfc": tSapEgressDSCPfc,
       "tSapEgressDSCPprofile": tSapEgressDSCPprofile,
       "tSapEgressPrecTable": tSapEgressPrecTable,
       "tSapEgressPrecEntry": tSapEgressPrecEntry,
       "tSapEgressPrecValue": tSapEgressPrecValue,
       "tSapEgressPrecRowStatus": tSapEgressPrecRowStatus,
       "tSapEgressPrecLastChanged": tSapEgressPrecLastChanged,
       "tSapEgressPrecHsmdaCntrOverride": tSapEgressPrecHsmdaCntrOverride,
       "tSapEgressPrecFC": tSapEgressPrecFC,
       "tSapEgressPrecProfile": tSapEgressPrecProfile,
       "tSapEgrIPCritTable": tSapEgrIPCritTable,
       "tSapEgrIPCritEntry": tSapEgrIPCritEntry,
       "tSapEgrIPCritAddrType": tSapEgrIPCritAddrType,
       "tSapEgrIPCritIndex": tSapEgrIPCritIndex,
       "tSapEgrIPCritRowStatus": tSapEgrIPCritRowStatus,
       "tSapEgrIPCritLastChanged": tSapEgrIPCritLastChanged,
       "tSapEgrIPCritDescription": tSapEgrIPCritDescription,
       "tSapEgrIPCritActionHsmdaCntrOvr": tSapEgrIPCritActionHsmdaCntrOvr,
       "tSapEgrIPCritSourceIpAddrType": tSapEgrIPCritSourceIpAddrType,
       "tSapEgrIPCritSourceIpAddr": tSapEgrIPCritSourceIpAddr,
       "tSapEgrIPCritSourceIpMask": tSapEgrIPCritSourceIpMask,
       "tSapEgrIPCritDestIpAddrType": tSapEgrIPCritDestIpAddrType,
       "tSapEgrIPCritDestIpAddr": tSapEgrIPCritDestIpAddr,
       "tSapEgrIPCritDestIpMask": tSapEgrIPCritDestIpMask,
       "tSapEgrIPCritProtocol": tSapEgrIPCritProtocol,
       "tSapEgrIPCritSourcePortValue1": tSapEgrIPCritSourcePortValue1,
       "tSapEgrIPCritSourcePortValue2": tSapEgrIPCritSourcePortValue2,
       "tSapEgrIPCritSourcePortOperator": tSapEgrIPCritSourcePortOperator,
       "tSapEgrIPCritDestPortValue1": tSapEgrIPCritDestPortValue1,
       "tSapEgrIPCritDestPortValue2": tSapEgrIPCritDestPortValue2,
       "tSapEgrIPCritDestPortOperator": tSapEgrIPCritDestPortOperator,
       "tSapEgrIPCritDSCP": tSapEgrIPCritDSCP,
       "tSapEgrIPCritFragment": tSapEgrIPCritFragment,
       "tSapEgrIPCritActionFC": tSapEgrIPCritActionFC,
       "tSapEgrIPCritActionProfile": tSapEgrIPCritActionProfile,
       "tSapEgrPolicerTable": tSapEgrPolicerTable,
       "tSapEgrPolicerEntry": tSapEgrPolicerEntry,
       "tSapEgrPolicerId": tSapEgrPolicerId,
       "tSapEgrPolicerRowStatus": tSapEgrPolicerRowStatus,
       "tSapEgrPolicerLastChanged": tSapEgrPolicerLastChanged,
       "tSapEgrPolicerDescr": tSapEgrPolicerDescr,
       "tSapEgrPolicerPIRAdaptation": tSapEgrPolicerPIRAdaptation,
       "tSapEgrPolicerCIRAdaptation": tSapEgrPolicerCIRAdaptation,
       "tSapEgrPolicerParent": tSapEgrPolicerParent,
       "tSapEgrPolicerLevel": tSapEgrPolicerLevel,
       "tSapEgrPolicerWeight": tSapEgrPolicerWeight,
       "tSapEgrPolicerAdminPIR": tSapEgrPolicerAdminPIR,
       "tSapEgrPolicerAdminCIR": tSapEgrPolicerAdminCIR,
       "tSapEgrPolicerStatMode": tSapEgrPolicerStatMode,
       "tSapEgrPolicerMBS": tSapEgrPolicerMBS,
       "tSapEgrPolicerHiPrioOnly": tSapEgrPolicerHiPrioOnly,
       "tSapEgrPolicerCBS": tSapEgrPolicerCBS,
       "tSapEgrPolicerPktOffset": tSapEgrPolicerPktOffset,
       "tSapEgrPolicerAdminPIRPercent": tSapEgrPolicerAdminPIRPercent,
       "tSapEgrPolicerAdminCIRPercent": tSapEgrPolicerAdminCIRPercent,
       "tSapEgrPolicerRateType": tSapEgrPolicerRateType,
       "tSapEgrPolicerSlopeStartDepth": tSapEgrPolicerSlopeStartDepth,
       "tSapEgrPolicerSlopeMaxDepth": tSapEgrPolicerSlopeMaxDepth,
       "tSapEgrPolicerSlopeMaxProb": tSapEgrPolicerSlopeMaxProb,
       "tSapEgrPolicerSlopeMap": tSapEgrPolicerSlopeMap,
       "tSapEgrPolicerAdvCfgPolicy": tSapEgrPolicerAdvCfgPolicy,
       "tSapEgrPolicerProfileCapped": tSapEgrPolicerProfileCapped,
       "tSapEgrPolicyNameTable": tSapEgrPolicyNameTable,
       "tSapEgrPolicyNameEntry": tSapEgrPolicyNameEntry,
       "tSapEgrPolicyNameId": tSapEgrPolicyNameId,
       "tSapEgrPolicyNameRowStatus": tSapEgrPolicyNameRowStatus,
       "tSapEgrPolicyNameLastChanged": tSapEgrPolicyNameLastChanged,
       "tSapEgressDot1pTable": tSapEgressDot1pTable,
       "tSapEgressDot1pEntry": tSapEgressDot1pEntry,
       "tSapEgressDot1pValue": tSapEgressDot1pValue,
       "tSapEgressDot1pRowStatus": tSapEgressDot1pRowStatus,
       "tSapEgressDot1pLastChanged": tSapEgressDot1pLastChanged,
       "tSapEgressDot1pFC": tSapEgressDot1pFC,
       "tSapEgressDot1pProfile": tSapEgressDot1pProfile,
       "tNetworkObjects": tNetworkObjects,
       "tNetworkPolicyTable": tNetworkPolicyTable,
       "tNetworkPolicyEntry": tNetworkPolicyEntry,
       "tNetworkPolicyIndex": tNetworkPolicyIndex,
       "tNetworkPolicyRowStatus": tNetworkPolicyRowStatus,
       "tNetworkPolicyScope": tNetworkPolicyScope,
       "tNetworkPolicyDescription": tNetworkPolicyDescription,
       "tNetworkPolicyIngressDefaultActionFC": tNetworkPolicyIngressDefaultActionFC,
       "tNetworkPolicyIngressDefaultActionProfile": tNetworkPolicyIngressDefaultActionProfile,
       "tNetworkPolicyEgressRemark": tNetworkPolicyEgressRemark,
       "tNetworkPolicyLastChanged": tNetworkPolicyLastChanged,
       "tNetworkPolicyIngressLerUseDscp": tNetworkPolicyIngressLerUseDscp,
       "tNetworkPolicyEgressRemarkDscp": tNetworkPolicyEgressRemarkDscp,
       "tNetworkIngressDSCPTable": tNetworkIngressDSCPTable,
       "tNetworkIngressDSCPEntry": tNetworkIngressDSCPEntry,
       "tNetworkIngressDSCP": tNetworkIngressDSCP,
       "tNetworkIngressDSCPRowStatus": tNetworkIngressDSCPRowStatus,
       "tNetworkIngressDSCPFC": tNetworkIngressDSCPFC,
       "tNetworkIngressDSCPProfile": tNetworkIngressDSCPProfile,
       "tNetworkIngressDSCPLastChanged": tNetworkIngressDSCPLastChanged,
       "tNetworkIngressDot1pTable": tNetworkIngressDot1pTable,
       "tNetworkIngressDot1pEntry": tNetworkIngressDot1pEntry,
       "tNetworkIngressDot1pValue": tNetworkIngressDot1pValue,
       "tNetworkIngressDot1pRowStatus": tNetworkIngressDot1pRowStatus,
       "tNetworkIngressDot1pFC": tNetworkIngressDot1pFC,
       "tNetworkIngressDot1pProfile": tNetworkIngressDot1pProfile,
       "tNetworkIngressDot1pLastChanged": tNetworkIngressDot1pLastChanged,
       "tNetworkIngressLSPEXPTable": tNetworkIngressLSPEXPTable,
       "tNetworkIngressLSPEXPEntry": tNetworkIngressLSPEXPEntry,
       "tNetworkIngressLSPEXP": tNetworkIngressLSPEXP,
       "tNetworkIngressLSPEXPRowStatus": tNetworkIngressLSPEXPRowStatus,
       "tNetworkIngressLSPEXPFC": tNetworkIngressLSPEXPFC,
       "tNetworkIngressLSPEXPProfile": tNetworkIngressLSPEXPProfile,
       "tNetworkIngressLSPEXPLastChanged": tNetworkIngressLSPEXPLastChanged,
       "tNetworkEgressFCTable": tNetworkEgressFCTable,
       "tNetworkEgressFCEntry": tNetworkEgressFCEntry,
       "tNetworkEgressFCName": tNetworkEgressFCName,
       "tNetworkEgressFCDSCPInProfile": tNetworkEgressFCDSCPInProfile,
       "tNetworkEgressFCDSCPOutProfile": tNetworkEgressFCDSCPOutProfile,
       "tNetworkEgressFCLspExpInProfile": tNetworkEgressFCLspExpInProfile,
       "tNetworkEgressFCLspExpOutProfile": tNetworkEgressFCLspExpOutProfile,
       "tNetworkEgressFCDot1pInProfile": tNetworkEgressFCDot1pInProfile,
       "tNetworkEgressFCDot1pOutProfile": tNetworkEgressFCDot1pOutProfile,
       "tNetworkEgressFCLastChanged": tNetworkEgressFCLastChanged,
       "tNetworkEgressFCForceDEValue": tNetworkEgressFCForceDEValue,
       "tNetworkEgressFCDEMark": tNetworkEgressFCDEMark,
       "tNetworkEgressFCQGrpQueue": tNetworkEgressFCQGrpQueue,
       "tNetworkEgressFCQGrpPolicer": tNetworkEgressFCQGrpPolicer,
       "tNetworkIngressFCTable": tNetworkIngressFCTable,
       "tNetworkIngressFCEntry": tNetworkIngressFCEntry,
       "tNetworkIngressFCName": tNetworkIngressFCName,
       "tNetworkIngressFCLastChanged": tNetworkIngressFCLastChanged,
       "tNetworkIngressFCMultiCastPlcr": tNetworkIngressFCMultiCastPlcr,
       "tNetworkIngressFCUniCastPlcr": tNetworkIngressFCUniCastPlcr,
       "tNetworkEgressDSCPTable": tNetworkEgressDSCPTable,
       "tNetworkEgressDSCPEntry": tNetworkEgressDSCPEntry,
       "tNetworkEgressDSCP": tNetworkEgressDSCP,
       "tNetworkEgressDSCPRowStatus": tNetworkEgressDSCPRowStatus,
       "tNetworkEgressDSCPLastChanged": tNetworkEgressDSCPLastChanged,
       "tNetworkEgressDSCPFC": tNetworkEgressDSCPFC,
       "tNetworkEgressDSCPProfile": tNetworkEgressDSCPProfile,
       "tNetworkEgressPrecTable": tNetworkEgressPrecTable,
       "tNetworkEgressPrecEntry": tNetworkEgressPrecEntry,
       "tNetworkEgressPrecValue": tNetworkEgressPrecValue,
       "tNetworkEgressPrecRowStatus": tNetworkEgressPrecRowStatus,
       "tNetworkEgressPrecLastChanged": tNetworkEgressPrecLastChanged,
       "tNetworkEgressPrecFC": tNetworkEgressPrecFC,
       "tNetworkEgressPrecProfile": tNetworkEgressPrecProfile,
       "tNetworkQueueObjects": tNetworkQueueObjects,
       "tNetworkQueuePolicyTable": tNetworkQueuePolicyTable,
       "tNetworkQueuePolicyEntry": tNetworkQueuePolicyEntry,
       "tNetworkQueuePolicy": tNetworkQueuePolicy,
       "tNetworkQueuePolicyRowStatus": tNetworkQueuePolicyRowStatus,
       "tNetworkQueuePolicyDescription": tNetworkQueuePolicyDescription,
       "tNetworkQueuePolicyLastChanged": tNetworkQueuePolicyLastChanged,
       "tNetworkQueuePolicyEHWrrPlcy": tNetworkQueuePolicyEHWrrPlcy,
       "tNetworkQueuePolicyEHPktBOffst": tNetworkQueuePolicyEHPktBOffst,
       "tNetworkQueueTable": tNetworkQueueTable,
       "tNetworkQueueEntry": tNetworkQueueEntry,
       "tNetworkQueue": tNetworkQueue,
       "tNetworkQueueRowStatus": tNetworkQueueRowStatus,
       "tNetworkQueuePoolName": tNetworkQueuePoolName,
       "tNetworkQueueParent": tNetworkQueueParent,
       "tNetworkQueueLevel": tNetworkQueueLevel,
       "tNetworkQueueWeight": tNetworkQueueWeight,
       "tNetworkQueueCIRLevel": tNetworkQueueCIRLevel,
       "tNetworkQueueCIRWeight": tNetworkQueueCIRWeight,
       "tNetworkQueueMCast": tNetworkQueueMCast,
       "tNetworkQueueExpedite": tNetworkQueueExpedite,
       "tNetworkQueueCIR": tNetworkQueueCIR,
       "tNetworkQueuePIR": tNetworkQueuePIR,
       "tNetworkQueueCBS": tNetworkQueueCBS,
       "tNetworkQueueMBS": tNetworkQueueMBS,
       "tNetworkQueueHiPrioOnly": tNetworkQueueHiPrioOnly,
       "tNetworkQueueLastChanged": tNetworkQueueLastChanged,
       "tNetworkQueueUsePortParent": tNetworkQueueUsePortParent,
       "tNetworkQueuePortLvl": tNetworkQueuePortLvl,
       "tNetworkQueuePortWght": tNetworkQueuePortWght,
       "tNetworkQueuePortCIRLvl": tNetworkQueuePortCIRLvl,
       "tNetworkQueuePortCIRWght": tNetworkQueuePortCIRWght,
       "tNetworkQueuePortAvgOverhead": tNetworkQueuePortAvgOverhead,
       "tNetworkQueueCIRAdaptation": tNetworkQueueCIRAdaptation,
       "tNetworkQueuePIRAdaptation": tNetworkQueuePIRAdaptation,
       "tNetworkQueueFCTable": tNetworkQueueFCTable,
       "tNetworkQueueFCEntry": tNetworkQueueFCEntry,
       "tNetworkQueueFCName": tNetworkQueueFCName,
       "tNetworkQueueFCRowStatus": tNetworkQueueFCRowStatus,
       "tNetworkQueueFC": tNetworkQueueFC,
       "tNetworkQueueFCMCast": tNetworkQueueFCMCast,
       "tNetworkQueueFCLastChanged": tNetworkQueueFCLastChanged,
       "tNetworkQueueFCEgrHsmdaQueue": tNetworkQueueFCEgrHsmdaQueue,
       "tNetworkEgrHsmdaQueueTable": tNetworkEgrHsmdaQueueTable,
       "tNetworkEgrHsmdaQueueEntry": tNetworkEgrHsmdaQueueEntry,
       "tNetworkEgrHsmdaQueue": tNetworkEgrHsmdaQueue,
       "tNetworkEgrHsmdaQueuePIRPercent": tNetworkEgrHsmdaQueuePIRPercent,
       "tNetworkEgrHsmdaQueuePIRAdaptn": tNetworkEgrHsmdaQueuePIRAdaptn,
       "tNetworkEgrHsmdaQueueWrrWeight": tNetworkEgrHsmdaQueueWrrWeight,
       "tNetworkEgrHsmdaQueueMBS": tNetworkEgrHsmdaQueueMBS,
       "tNetworkEgrHsmdaQueueSlopePolicy": tNetworkEgrHsmdaQueueSlopePolicy,
       "tNetworkEgrHsmdaQueueLastChanged": tNetworkEgrHsmdaQueueLastChanged,
       "tNetworkEgrHsmdaQueueBurstLimit": tNetworkEgrHsmdaQueueBurstLimit,
       "tSharedQueueObjects": tSharedQueueObjects,
       "tSharedQueuePolicyTable": tSharedQueuePolicyTable,
       "tSharedQueuePolicyEntry": tSharedQueuePolicyEntry,
       "tSharedQueuePolicy": tSharedQueuePolicy,
       "tSharedQueuePolicyRowStatus": tSharedQueuePolicyRowStatus,
       "tSharedQueuePolicyLastChanged": tSharedQueuePolicyLastChanged,
       "tSharedQueuePolicyDescription": tSharedQueuePolicyDescription,
       "tSharedQueueTable": tSharedQueueTable,
       "tSharedQueueEntry": tSharedQueueEntry,
       "tSharedQueueId": tSharedQueueId,
       "tSharedQueueRowStatus": tSharedQueueRowStatus,
       "tSharedQueueLastChanged": tSharedQueueLastChanged,
       "tSharedQueuePoolName": tSharedQueuePoolName,
       "tSharedQueueParent": tSharedQueueParent,
       "tSharedQueueLevel": tSharedQueueLevel,
       "tSharedQueueWeight": tSharedQueueWeight,
       "tSharedQueueCIRLevel": tSharedQueueCIRLevel,
       "tSharedQueueCIRWeight": tSharedQueueCIRWeight,
       "tSharedQueueExpedite": tSharedQueueExpedite,
       "tSharedQueueCIR": tSharedQueueCIR,
       "tSharedQueuePIR": tSharedQueuePIR,
       "tSharedQueueCBS": tSharedQueueCBS,
       "tSharedQueueMBS": tSharedQueueMBS,
       "tSharedQueueHiPrioOnly": tSharedQueueHiPrioOnly,
       "tSharedQueueIsMultipoint": tSharedQueueIsMultipoint,
       "tSharedQueueFCTable": tSharedQueueFCTable,
       "tSharedQueueFCEntry": tSharedQueueFCEntry,
       "tSharedQueueFCName": tSharedQueueFCName,
       "tSharedQueueFCRowStatus": tSharedQueueFCRowStatus,
       "tSharedQueueFCLastChanged": tSharedQueueFCLastChanged,
       "tSharedQueueFCQueue": tSharedQueueFCQueue,
       "tSharedQueueFCMCastQueue": tSharedQueueFCMCastQueue,
       "tSharedQueueFCBCastQueue": tSharedQueueFCBCastQueue,
       "tSharedQueueFCUnknownQueue": tSharedQueueFCUnknownQueue,
       "tQosIngQGroupTable": tQosIngQGroupTable,
       "tQosIngQGroupEntry": tQosIngQGroupEntry,
       "tQosIngQGroupName": tQosIngQGroupName,
       "tQosIngQGroupRowStatus": tQosIngQGroupRowStatus,
       "tQosIngQGroupLastChanged": tQosIngQGroupLastChanged,
       "tQosIngQGroupDescr": tQosIngQGroupDescr,
       "tQosIngQueueTable": tQosIngQueueTable,
       "tQosIngQueueEntry": tQosIngQueueEntry,
       "tQosIngQueue": tQosIngQueue,
       "tQosIngQueueRowStatus": tQosIngQueueRowStatus,
       "tQosIngQueueParent": tQosIngQueueParent,
       "tQosIngQueueLevel": tQosIngQueueLevel,
       "tQosIngQueueWeight": tQosIngQueueWeight,
       "tQosIngQueueCIRLevel": tQosIngQueueCIRLevel,
       "tQosIngQueueCIRWeight": tQosIngQueueCIRWeight,
       "tQosIngQueueMCast": tQosIngQueueMCast,
       "tQosIngQueueExpedite": tQosIngQueueExpedite,
       "tQosIngQueueCBS": tQosIngQueueCBS,
       "tQosIngQueueMBS": tQosIngQueueMBS,
       "tQosIngQueueHiPrioOnly": tQosIngQueueHiPrioOnly,
       "tQosIngQueuePIRAdaptation": tQosIngQueuePIRAdaptation,
       "tQosIngQueueCIRAdaptation": tQosIngQueueCIRAdaptation,
       "tQosIngQueueAdminPIR": tQosIngQueueAdminPIR,
       "tQosIngQueueAdminCIR": tQosIngQueueAdminCIR,
       "tQosIngQueueLastChanged": tQosIngQueueLastChanged,
       "tQosIngQueuePoliced": tQosIngQueuePoliced,
       "tQosIngQueueMode": tQosIngQueueMode,
       "tQosIngQueuePoolName": tQosIngQueuePoolName,
       "tQosIngQueueMBSBytes": tQosIngQueueMBSBytes,
       "tQosIngQueueBurstLimit": tQosIngQueueBurstLimit,
       "tQosIngQueueAdvCfgPolicy": tQosIngQueueAdvCfgPolicy,
       "tQosEgrQGroupTable": tQosEgrQGroupTable,
       "tQosEgrQGroupEntry": tQosEgrQGroupEntry,
       "tQosEgrQGroupName": tQosEgrQGroupName,
       "tQosEgrQGroupRowStatus": tQosEgrQGroupRowStatus,
       "tQosEgrQGroupLastChanged": tQosEgrQGroupLastChanged,
       "tQosEgrQGroupDescr": tQosEgrQGroupDescr,
       "tQosEgrQueueTable": tQosEgrQueueTable,
       "tQosEgrQueueEntry": tQosEgrQueueEntry,
       "tQosEgrQueue": tQosEgrQueue,
       "tQosEgrQueueRowStatus": tQosEgrQueueRowStatus,
       "tQosEgrQueueParent": tQosEgrQueueParent,
       "tQosEgrQueueLevel": tQosEgrQueueLevel,
       "tQosEgrQueueWeight": tQosEgrQueueWeight,
       "tQosEgrQueueCIRLevel": tQosEgrQueueCIRLevel,
       "tQosEgrQueueCIRWeight": tQosEgrQueueCIRWeight,
       "tQosEgrQueueExpedite": tQosEgrQueueExpedite,
       "tQosEgrQueueCBS": tQosEgrQueueCBS,
       "tQosEgrQueueMBS": tQosEgrQueueMBS,
       "tQosEgrQueueHiPrioOnly": tQosEgrQueueHiPrioOnly,
       "tQosEgrQueuePIRAdaptation": tQosEgrQueuePIRAdaptation,
       "tQosEgrQueueCIRAdaptation": tQosEgrQueueCIRAdaptation,
       "tQosEgrQueueAdminPIR": tQosEgrQueueAdminPIR,
       "tQosEgrQueueAdminCIR": tQosEgrQueueAdminCIR,
       "tQosEgrQueueLastChanged": tQosEgrQueueLastChanged,
       "tQosEgrQueueUsePortParent": tQosEgrQueueUsePortParent,
       "tQosEgrQueuePortLvl": tQosEgrQueuePortLvl,
       "tQosEgrQueuePortWght": tQosEgrQueuePortWght,
       "tQosEgrQueuePortCIRLvl": tQosEgrQueuePortCIRLvl,
       "tQosEgrQueuePortCIRWght": tQosEgrQueuePortCIRWght,
       "tQosEgrQueuePoolName": tQosEgrQueuePoolName,
       "tQosEgrQueueXPWredQ": tQosEgrQueueXPWredQ,
       "tQosEgrQueueXPWredQSlope": tQosEgrQueueXPWredQSlope,
       "tQosEgrQueueMBSBytes": tQosEgrQueueMBSBytes,
       "tQosEgrQueueAdminPIRPercent": tQosEgrQueueAdminPIRPercent,
       "tQosEgrQueueAdminCIRPercent": tQosEgrQueueAdminCIRPercent,
       "tQosEgrQueueRateType": tQosEgrQueueRateType,
       "tQosEgrQueueBurstLimit": tQosEgrQueueBurstLimit,
       "tQosEgrQueueAdvCfgPolicy": tQosEgrQueueAdvCfgPolicy,
       "tQosEgrQueuePktOffset": tQosEgrQueuePktOffset,
       "tQosEgrQGroupFCTable": tQosEgrQGroupFCTable,
       "tQosEgrQGroupFCEntry": tQosEgrQGroupFCEntry,
       "tQosEgrQGroupFCName": tQosEgrQGroupFCName,
       "tQosEgrQGroupFCRowStatus": tQosEgrQGroupFCRowStatus,
       "tQosEgrQGroupFCLastChanged": tQosEgrQGroupFCLastChanged,
       "tQosEgrQGroupFCQueue": tQosEgrQGroupFCQueue,
       "tSlopeObjects": tSlopeObjects,
       "tSlopePolicyTable": tSlopePolicyTable,
       "tSlopePolicyEntry": tSlopePolicyEntry,
       "tSlopePolicy": tSlopePolicy,
       "tSlopeRowStatus": tSlopeRowStatus,
       "tSlopeDescription": tSlopeDescription,
       "tSlopeHiAdminStatus": tSlopeHiAdminStatus,
       "tSlopeHiStartAverage": tSlopeHiStartAverage,
       "tSlopeHiMaxAverage": tSlopeHiMaxAverage,
       "tSlopeHiMaxProbability": tSlopeHiMaxProbability,
       "tSlopeLoAdminStatus": tSlopeLoAdminStatus,
       "tSlopeLoStartAverage": tSlopeLoStartAverage,
       "tSlopeLoMaxAverage": tSlopeLoMaxAverage,
       "tSlopeLoMaxProbability": tSlopeLoMaxProbability,
       "tSlopeTimeAvgFactor": tSlopeTimeAvgFactor,
       "tSlopeLastChanged": tSlopeLastChanged,
       "tHsmdaSlopePolicyTable": tHsmdaSlopePolicyTable,
       "tHsmdaSlopePolicyEntry": tHsmdaSlopePolicyEntry,
       "tHsmdaSlopePolicyName": tHsmdaSlopePolicyName,
       "tHsmdaSlopePolicyRowStatus": tHsmdaSlopePolicyRowStatus,
       "tHsmdaSlopeLastChanged": tHsmdaSlopeLastChanged,
       "tHsmdaSlopeDescription": tHsmdaSlopeDescription,
       "tHsmdaSlopeQueueMbs": tHsmdaSlopeQueueMbs,
       "tHsmdaSlopeHiAdminStatus": tHsmdaSlopeHiAdminStatus,
       "tHsmdaSlopeHiStartDepth": tHsmdaSlopeHiStartDepth,
       "tHsmdaSlopeHiMaxDepth": tHsmdaSlopeHiMaxDepth,
       "tHsmdaSlopeHiMaxProbability": tHsmdaSlopeHiMaxProbability,
       "tHsmdaSlopeLoAdminStatus": tHsmdaSlopeLoAdminStatus,
       "tHsmdaSlopeLoStartDepth": tHsmdaSlopeLoStartDepth,
       "tHsmdaSlopeLoMaxDepth": tHsmdaSlopeLoMaxDepth,
       "tHsmdaSlopeLoMaxProbability": tHsmdaSlopeLoMaxProbability,
       "tSchedulerObjects": tSchedulerObjects,
       "tSchedulerPolicyTable": tSchedulerPolicyTable,
       "tSchedulerPolicyEntry": tSchedulerPolicyEntry,
       "tSchedulerPolicyName": tSchedulerPolicyName,
       "tSchedulerPolicyRowStatus": tSchedulerPolicyRowStatus,
       "tSchedulerPolicyDescription": tSchedulerPolicyDescription,
       "tSchedulerPolicyLastChanged": tSchedulerPolicyLastChanged,
       "tSchedulerPolicyFrameBasedAccnt": tSchedulerPolicyFrameBasedAccnt,
       "tVirtualSchedulerTable": tVirtualSchedulerTable,
       "tVirtualSchedulerEntry": tVirtualSchedulerEntry,
       "tVirtualSchedulerTier": tVirtualSchedulerTier,
       "tVirtualSchedulerName": tVirtualSchedulerName,
       "tVirtualSchedulerRowStatus": tVirtualSchedulerRowStatus,
       "tVirtualSchedulerDescription": tVirtualSchedulerDescription,
       "tVirtualSchedulerParent": tVirtualSchedulerParent,
       "tVirtualSchedulerLevel": tVirtualSchedulerLevel,
       "tVirtualSchedulerWeight": tVirtualSchedulerWeight,
       "tVirtualSchedulerCIRLevel": tVirtualSchedulerCIRLevel,
       "tVirtualSchedulerCIRWeight": tVirtualSchedulerCIRWeight,
       "tVirtualSchedulerPIR": tVirtualSchedulerPIR,
       "tVirtualSchedulerCIR": tVirtualSchedulerCIR,
       "tVirtualSchedulerSummedCIR": tVirtualSchedulerSummedCIR,
       "tVirtualSchedulerLastChanged": tVirtualSchedulerLastChanged,
       "tVirtualSchedulerUsePortParent": tVirtualSchedulerUsePortParent,
       "tVirtualSchedulerPortLvl": tVirtualSchedulerPortLvl,
       "tVirtualSchedulerPortWght": tVirtualSchedulerPortWght,
       "tVirtualSchedulerPortCIRLvl": tVirtualSchedulerPortCIRLvl,
       "tVirtualSchedulerPortCIRWght": tVirtualSchedulerPortCIRWght,
       "tPortSchedulerPlcyTable": tPortSchedulerPlcyTable,
       "tPortSchedulerPlcyEntry": tPortSchedulerPlcyEntry,
       "tPortSchedulerPlcyName": tPortSchedulerPlcyName,
       "tPortSchedulerPlcyRowStatus": tPortSchedulerPlcyRowStatus,
       "tPortSchedulerPlcyDescription": tPortSchedulerPlcyDescription,
       "tPortSchedulerPlcyLastChanged": tPortSchedulerPlcyLastChanged,
       "tPortSchedulerPlcyMaxRate": tPortSchedulerPlcyMaxRate,
       "tPortSchedulerPlcyLvl1PIR": tPortSchedulerPlcyLvl1PIR,
       "tPortSchedulerPlcyLvl1CIR": tPortSchedulerPlcyLvl1CIR,
       "tPortSchedulerPlcyLvl2PIR": tPortSchedulerPlcyLvl2PIR,
       "tPortSchedulerPlcyLvl2CIR": tPortSchedulerPlcyLvl2CIR,
       "tPortSchedulerPlcyLvl3PIR": tPortSchedulerPlcyLvl3PIR,
       "tPortSchedulerPlcyLvl3CIR": tPortSchedulerPlcyLvl3CIR,
       "tPortSchedulerPlcyLvl4PIR": tPortSchedulerPlcyLvl4PIR,
       "tPortSchedulerPlcyLvl4CIR": tPortSchedulerPlcyLvl4CIR,
       "tPortSchedulerPlcyLvl5PIR": tPortSchedulerPlcyLvl5PIR,
       "tPortSchedulerPlcyLvl5CIR": tPortSchedulerPlcyLvl5CIR,
       "tPortSchedulerPlcyLvl6PIR": tPortSchedulerPlcyLvl6PIR,
       "tPortSchedulerPlcyLvl6CIR": tPortSchedulerPlcyLvl6CIR,
       "tPortSchedulerPlcyLvl7PIR": tPortSchedulerPlcyLvl7PIR,
       "tPortSchedulerPlcyLvl7CIR": tPortSchedulerPlcyLvl7CIR,
       "tPortSchedulerPlcyLvl8PIR": tPortSchedulerPlcyLvl8PIR,
       "tPortSchedulerPlcyLvl8CIR": tPortSchedulerPlcyLvl8CIR,
       "tPortSchedulerPlcyOrphanLvl": tPortSchedulerPlcyOrphanLvl,
       "tPortSchedulerPlcyOrphanWeight": tPortSchedulerPlcyOrphanWeight,
       "tPortSchedulerPlcyOrphanCIRLvl": tPortSchedulerPlcyOrphanCIRLvl,
       "tPortSchedulerPlcyOrphanCIRWght": tPortSchedulerPlcyOrphanCIRWght,
       "tHsmdaSchedulerPlcyTable": tHsmdaSchedulerPlcyTable,
       "tHsmdaSchedulerPlcyEntry": tHsmdaSchedulerPlcyEntry,
       "tHsmdaSchedulerPlcyName": tHsmdaSchedulerPlcyName,
       "tHsmdaSchedulerPlcyRowStatus": tHsmdaSchedulerPlcyRowStatus,
       "tHsmdaSchedulerPlcyDescription": tHsmdaSchedulerPlcyDescription,
       "tHsmdaSchedulerPlcyMaxRate": tHsmdaSchedulerPlcyMaxRate,
       "tHsmdaSchedulerPlcyLvl1Rate": tHsmdaSchedulerPlcyLvl1Rate,
       "tHsmdaSchedulerPlcyLvl1GrpId": tHsmdaSchedulerPlcyLvl1GrpId,
       "tHsmdaSchedulerPlcyLvl1WgtInGrp": tHsmdaSchedulerPlcyLvl1WgtInGrp,
       "tHsmdaSchedulerPlcyLvl2Rate": tHsmdaSchedulerPlcyLvl2Rate,
       "tHsmdaSchedulerPlcyLvl2GrpId": tHsmdaSchedulerPlcyLvl2GrpId,
       "tHsmdaSchedulerPlcyLvl2WgtInGrp": tHsmdaSchedulerPlcyLvl2WgtInGrp,
       "tHsmdaSchedulerPlcyLvl3Rate": tHsmdaSchedulerPlcyLvl3Rate,
       "tHsmdaSchedulerPlcyLvl3GrpId": tHsmdaSchedulerPlcyLvl3GrpId,
       "tHsmdaSchedulerPlcyLvl3WgtInGrp": tHsmdaSchedulerPlcyLvl3WgtInGrp,
       "tHsmdaSchedulerPlcyLvl4Rate": tHsmdaSchedulerPlcyLvl4Rate,
       "tHsmdaSchedulerPlcyLvl4GrpId": tHsmdaSchedulerPlcyLvl4GrpId,
       "tHsmdaSchedulerPlcyLvl4WgtInGrp": tHsmdaSchedulerPlcyLvl4WgtInGrp,
       "tHsmdaSchedulerPlcyLvl5Rate": tHsmdaSchedulerPlcyLvl5Rate,
       "tHsmdaSchedulerPlcyLvl5GrpId": tHsmdaSchedulerPlcyLvl5GrpId,
       "tHsmdaSchedulerPlcyLvl5WgtInGrp": tHsmdaSchedulerPlcyLvl5WgtInGrp,
       "tHsmdaSchedulerPlcyLvl6Rate": tHsmdaSchedulerPlcyLvl6Rate,
       "tHsmdaSchedulerPlcyLvl6GrpId": tHsmdaSchedulerPlcyLvl6GrpId,
       "tHsmdaSchedulerPlcyLvl6WgtInGrp": tHsmdaSchedulerPlcyLvl6WgtInGrp,
       "tHsmdaSchedulerPlcyLvl7Rate": tHsmdaSchedulerPlcyLvl7Rate,
       "tHsmdaSchedulerPlcyLvl7GrpId": tHsmdaSchedulerPlcyLvl7GrpId,
       "tHsmdaSchedulerPlcyLvl7WgtInGrp": tHsmdaSchedulerPlcyLvl7WgtInGrp,
       "tHsmdaSchedulerPlcyLvl8Rate": tHsmdaSchedulerPlcyLvl8Rate,
       "tHsmdaSchedulerPlcyLvl8GrpId": tHsmdaSchedulerPlcyLvl8GrpId,
       "tHsmdaSchedulerPlcyLvl8WgtInGrp": tHsmdaSchedulerPlcyLvl8WgtInGrp,
       "tHsmdaSchedulerPlcyLastChanged": tHsmdaSchedulerPlcyLastChanged,
       "tHsmdaSchedulerPlcyGrp1Rate": tHsmdaSchedulerPlcyGrp1Rate,
       "tHsmdaSchedulerPlcyGrp2Rate": tHsmdaSchedulerPlcyGrp2Rate,
       "tHsmdaSchedulerPlcyBrstLimit": tHsmdaSchedulerPlcyBrstLimit,
       "tHsmdaSchedulerPlcyGrp1BrstLimit": tHsmdaSchedulerPlcyGrp1BrstLimit,
       "tHsmdaSchedulerPlcyGrp2BrstLimit": tHsmdaSchedulerPlcyGrp2BrstLimit,
       "tHsmdaSchedulerPlcyLvl1BrstLimit": tHsmdaSchedulerPlcyLvl1BrstLimit,
       "tHsmdaSchedulerPlcyLvl2BrstLimit": tHsmdaSchedulerPlcyLvl2BrstLimit,
       "tHsmdaSchedulerPlcyLvl3BrstLimit": tHsmdaSchedulerPlcyLvl3BrstLimit,
       "tHsmdaSchedulerPlcyLvl4BrstLimit": tHsmdaSchedulerPlcyLvl4BrstLimit,
       "tHsmdaSchedulerPlcyLvl5BrstLimit": tHsmdaSchedulerPlcyLvl5BrstLimit,
       "tHsmdaSchedulerPlcyLvl6BrstLimit": tHsmdaSchedulerPlcyLvl6BrstLimit,
       "tHsmdaSchedulerPlcyLvl7BrstLimit": tHsmdaSchedulerPlcyLvl7BrstLimit,
       "tHsmdaSchedulerPlcyLvl8BrstLimit": tHsmdaSchedulerPlcyLvl8BrstLimit,
       "tPortSchPlcyGrpTable": tPortSchPlcyGrpTable,
       "tPortSchPlcyGrpEntry": tPortSchPlcyGrpEntry,
       "tPortSchPlcyGrpName": tPortSchPlcyGrpName,
       "tPortSchPlcyGrpRowStatus": tPortSchPlcyGrpRowStatus,
       "tPortSchPlcyGrpLastChanged": tPortSchPlcyGrpLastChanged,
       "tPortSchPlcyGrpAdminPIR": tPortSchPlcyGrpAdminPIR,
       "tPortSchPlcyGrpAdminCIR": tPortSchPlcyGrpAdminCIR,
       "tPortSchPlcyLvlGrpTable": tPortSchPlcyLvlGrpTable,
       "tPortSchPlcyLvlGrpEntry": tPortSchPlcyLvlGrpEntry,
       "tPortSchPlcyLvlGrpLastChanged": tPortSchPlcyLvlGrpLastChanged,
       "tPortSchPlcyLvl1GrpName": tPortSchPlcyLvl1GrpName,
       "tPortSchPlcyLvl2GrpName": tPortSchPlcyLvl2GrpName,
       "tPortSchPlcyLvl3GrpName": tPortSchPlcyLvl3GrpName,
       "tPortSchPlcyLvl4GrpName": tPortSchPlcyLvl4GrpName,
       "tPortSchPlcyLvl5GrpName": tPortSchPlcyLvl5GrpName,
       "tPortSchPlcyLvl6GrpName": tPortSchPlcyLvl6GrpName,
       "tPortSchPlcyLvl7GrpName": tPortSchPlcyLvl7GrpName,
       "tPortSchPlcyLvl8GrpName": tPortSchPlcyLvl8GrpName,
       "tPortSchPlcyLvl1GrpWeight": tPortSchPlcyLvl1GrpWeight,
       "tPortSchPlcyLvl2GrpWeight": tPortSchPlcyLvl2GrpWeight,
       "tPortSchPlcyLvl3GrpWeight": tPortSchPlcyLvl3GrpWeight,
       "tPortSchPlcyLvl4GrpWeight": tPortSchPlcyLvl4GrpWeight,
       "tPortSchPlcyLvl5GrpWeight": tPortSchPlcyLvl5GrpWeight,
       "tPortSchPlcyLvl6GrpWeight": tPortSchPlcyLvl6GrpWeight,
       "tPortSchPlcyLvl7GrpWeight": tPortSchPlcyLvl7GrpWeight,
       "tPortSchPlcyLvl8GrpWeight": tPortSchPlcyLvl8GrpWeight,
       "tQosTimeStampObjects": tQosTimeStampObjects,
       "tQosDomainLastChanged": tQosDomainLastChanged,
       "tDSCPNameTableLastChanged": tDSCPNameTableLastChanged,
       "tQosIngQGroupTableLastChanged": tQosIngQGroupTableLastChanged,
       "tQosIngQTableLastChanged": tQosIngQTableLastChanged,
       "tQosEgrQGroupTableLastChanged": tQosEgrQGroupTableLastChanged,
       "tQosEgrQTableLastChanged": tQosEgrQTableLastChanged,
       "tFCNameTableLastChanged": tFCNameTableLastChanged,
       "tSapIngressTableLastChanged": tSapIngressTableLastChanged,
       "tSapIngressQueueTableLastChanged": tSapIngressQueueTableLastChanged,
       "tSapIngressDSCPTableLastChanged": tSapIngressDSCPTableLastChanged,
       "tSapIngressDot1pTableLastChanged": tSapIngressDot1pTableLastChanged,
       "tSapIngressIPCriteriaTableLastChanged": tSapIngressIPCriteriaTableLastChanged,
       "tSapIngressMacCriteriaTableLastChanged": tSapIngressMacCriteriaTableLastChanged,
       "tSapIngressFCTableLastChanged": tSapIngressFCTableLastChanged,
       "tSapIngressPrecTableLastChanged": tSapIngressPrecTableLastChanged,
       "tSapEgressTableLastChanged": tSapEgressTableLastChanged,
       "tSapEgressQueueTableLastChanged": tSapEgressQueueTableLastChanged,
       "tSapEgressFCTableLastChanged": tSapEgressFCTableLastChanged,
       "tNetworkPolicyTableLastChanged": tNetworkPolicyTableLastChanged,
       "tNetworkIngressDSCPTableLastChanged": tNetworkIngressDSCPTableLastChanged,
       "tNetworkIngressLSPEXPTableLastChanged": tNetworkIngressLSPEXPTableLastChanged,
       "tNetworkEgressFCTableLastChanged": tNetworkEgressFCTableLastChanged,
       "tNetworkIngressDot1pTableLastChanged": tNetworkIngressDot1pTableLastChanged,
       "tNetworkQueuePolicyTableLastChanged": tNetworkQueuePolicyTableLastChanged,
       "tNetworkQueueTableLastChanged": tNetworkQueueTableLastChanged,
       "tNetworkQueueFCTableLastChanged": tNetworkQueueFCTableLastChanged,
       "tSlopePolicyTableLastChanged": tSlopePolicyTableLastChanged,
       "tSchedulerPolicyTableLastChanged": tSchedulerPolicyTableLastChanged,
       "tVirtualSchedulerTableLastChanged": tVirtualSchedulerTableLastChanged,
       "tAtmTdpTableLastChanged": tAtmTdpTableLastChanged,
       "tSharedQueuePolicyTableLastChanged": tSharedQueuePolicyTableLastChanged,
       "tSharedQueueTableLastChanged": tSharedQueueTableLastChanged,
       "tSharedQueueFCTableLastChanged": tSharedQueueFCTableLastChanged,
       "tSapIngressIPv6CriteriaTableLastChanged": tSapIngressIPv6CriteriaTableLastChanged,
       "tSapIngrHsmdaQueueTblLastChngd": tSapIngrHsmdaQueueTblLastChngd,
       "tSapEgrHsmdaQueueTblLastChngd": tSapEgrHsmdaQueueTblLastChngd,
       "tHsmdaSchedPlcyTblLastChngd": tHsmdaSchedPlcyTblLastChngd,
       "tHsmdaSchedPlcyGrpTblLastChngd": tHsmdaSchedPlcyGrpTblLastChngd,
       "tHsmdaPoolPlcyTblLastChngd": tHsmdaPoolPlcyTblLastChngd,
       "tHsmdaSlopePolicyTableLastChanged": tHsmdaSlopePolicyTableLastChanged,
       "tNamedPoolPolicyTableLastChanged": tNamedPoolPolicyTableLastChanged,
       "tQ1NamedPoolTableLastChanged": tQ1NamedPoolTableLastChanged,
       "tMcMlpppIngrProfTableLastChanged": tMcMlpppIngrProfTableLastChanged,
       "tMcMlpppIngrClassTableLastChanged": tMcMlpppIngrClassTableLastChanged,
       "tMcMlpppEgrProfTableLastChanged": tMcMlpppEgrProfTableLastChanged,
       "tMcMlpppEgrClassTableLastChanged": tMcMlpppEgrClassTableLastChanged,
       "tMcMlpppEgrFCTableLastChanged": tMcMlpppEgrFCTableLastChanged,
       "tMcFrIngrProfTableLastChanged": tMcFrIngrProfTableLastChanged,
       "tMcFrIngrClassTableLastChanged": tMcFrIngrClassTableLastChanged,
       "tMcFrEgrProfTableLastChanged": tMcFrEgrProfTableLastChanged,
       "tMcFrEgrClassTableLastChanged": tMcFrEgrClassTableLastChanged,
       "tSapIngressLspExpTableLastChange": tSapIngressLspExpTableLastChange,
       "tSapIngPolicerTableLastChanged": tSapIngPolicerTableLastChanged,
       "tSapEgrPolicerTableLastChanged": tSapEgrPolicerTableLastChanged,
       "tQosPolicerCtrlPolTblLastChgd": tQosPolicerCtrlPolTblLastChgd,
       "tQosPolicerLevelTblLastChgd": tQosPolicerLevelTblLastChgd,
       "tQosPolicerArbiterTblLastChgd": tQosPolicerArbiterTblLastChgd,
       "tQosEgrQGroupFCTableLastChanged": tQosEgrQGroupFCTableLastChanged,
       "tPortSchPlcyGrpTblLastChgd": tPortSchPlcyGrpTblLastChgd,
       "tPortSchPlcyLvlGrpTblLastChgd": tPortSchPlcyLvlGrpTblLastChgd,
       "tHsmdaWrrPolicyTblLastChgd": tHsmdaWrrPolicyTblLastChgd,
       "tNetworkEgrHsmdaQueueTblLastChgd": tNetworkEgrHsmdaQueueTblLastChgd,
       "tSapIngPolicyNameTableLastChgd": tSapIngPolicyNameTableLastChgd,
       "tSapEgrPolicyNameTableLastChgd": tSapEgrPolicyNameTableLastChgd,
       "tQosIngPolicerTableLastChanged": tQosIngPolicerTableLastChanged,
       "tQosEgrPolicerTableLastChanged": tQosEgrPolicerTableLastChanged,
       "tSapEgressDot1pTableLastChanged": tSapEgressDot1pTableLastChanged,
       "tAdvCfgPolicyTblLastChgd": tAdvCfgPolicyTblLastChgd,
       "tNetworkIngressFCTableLstChanged": tNetworkIngressFCTableLstChanged,
       "tNetworkEgrDSCPTableLastChanged": tNetworkEgrDSCPTableLastChanged,
       "tNetworkEgrPrecTableLastChanged": tNetworkEgrPrecTableLastChanged,
       "tAtmTdpObjects": tAtmTdpObjects,
       "tAtmTdpTable": tAtmTdpTable,
       "tAtmTdpEntry": tAtmTdpEntry,
       "tAtmTdpIndex": tAtmTdpIndex,
       "tAtmTdpSir": tAtmTdpSir,
       "tAtmTdpPir": tAtmTdpPir,
       "tAtmTdpMbs": tAtmTdpMbs,
       "tAtmTdpMir": tAtmTdpMir,
       "tAtmTdpShaping": tAtmTdpShaping,
       "tAtmTdpServCat": tAtmTdpServCat,
       "tAtmTdpDescription": tAtmTdpDescription,
       "tAtmTdpLastChanged": tAtmTdpLastChanged,
       "tAtmTdpRowStatus": tAtmTdpRowStatus,
       "tAtmTdpDescrType": tAtmTdpDescrType,
       "tAtmTdpCdvt": tAtmTdpCdvt,
       "tAtmTdpPolicing": tAtmTdpPolicing,
       "tAtmTdpCLPTagging": tAtmTdpCLPTagging,
       "tAtmTdpWeight": tAtmTdpWeight,
       "tAtmTdpIndexNext": tAtmTdpIndexNext,
       "tAtmTdpsMaxSupported": tAtmTdpsMaxSupported,
       "tAtmTdpsCurrentlyConfigured": tAtmTdpsCurrentlyConfigured,
       "tPoolObjects": tPoolObjects,
       "tNamedPoolPolicyTable": tNamedPoolPolicyTable,
       "tNamedPoolPolicyEntry": tNamedPoolPolicyEntry,
       "tNamedPoolPolicyName": tNamedPoolPolicyName,
       "tNamedPoolPolicyRowStatus": tNamedPoolPolicyRowStatus,
       "tNamedPoolPolicyLastChanged": tNamedPoolPolicyLastChanged,
       "tNamedPoolPolicyDescription": tNamedPoolPolicyDescription,
       "tNamedPoolPolicyQ1DefaultWeight": tNamedPoolPolicyQ1DefaultWeight,
       "tNamedPoolPolicyQ1MdaWeight": tNamedPoolPolicyQ1MdaWeight,
       "tNamedPoolPolicyQ1PortWeight": tNamedPoolPolicyQ1PortWeight,
       "tQ1NamedPoolTable": tQ1NamedPoolTable,
       "tQ1NamedPoolEntry": tQ1NamedPoolEntry,
       "tQ1NamedPoolPolicyName": tQ1NamedPoolPolicyName,
       "tQ1NamedPoolName": tQ1NamedPoolName,
       "tQ1NamedPoolRowStatus": tQ1NamedPoolRowStatus,
       "tQ1NamedPoolLastChanged": tQ1NamedPoolLastChanged,
       "tQ1NamedPoolDescription": tQ1NamedPoolDescription,
       "tQ1NamedPoolNetworkAllocWeight": tQ1NamedPoolNetworkAllocWeight,
       "tQ1NamedPoolAccessAllocWeight": tQ1NamedPoolAccessAllocWeight,
       "tQ1NamedPoolSlopePolicy": tQ1NamedPoolSlopePolicy,
       "tQ1NamedPoolReservedCbs": tQ1NamedPoolReservedCbs,
       "tQ1NamedPoolResvCbsAmbrAlrmStep": tQ1NamedPoolResvCbsAmbrAlrmStep,
       "tQ1NamedPoolResvCbsAmbrAlrmMax": tQ1NamedPoolResvCbsAmbrAlrmMax,
       "tQ1NamedPoolAmbrAlrmThresh": tQ1NamedPoolAmbrAlrmThresh,
       "tQ1NamedPoolRedAlrmThresh": tQ1NamedPoolRedAlrmThresh,
       "tHsmdaPoolPolicyTable": tHsmdaPoolPolicyTable,
       "tHsmdaPoolPolicyEntry": tHsmdaPoolPolicyEntry,
       "tHsmdaPoolPolicyName": tHsmdaPoolPolicyName,
       "tHsmdaPoolPolicyRowStatus": tHsmdaPoolPolicyRowStatus,
       "tHsmdaPoolLastChanged": tHsmdaPoolLastChanged,
       "tHsmdaPoolDescription": tHsmdaPoolDescription,
       "tHsmdaPoolSystemReserve": tHsmdaPoolSystemReserve,
       "tHsmdaPoolRoot1AllocWeight": tHsmdaPoolRoot1AllocWeight,
       "tHsmdaPoolRoot2AllocWeight": tHsmdaPoolRoot2AllocWeight,
       "tHsmdaPoolRoot3AllocWeight": tHsmdaPoolRoot3AllocWeight,
       "tHsmdaPoolRoot4AllocWeight": tHsmdaPoolRoot4AllocWeight,
       "tHsmdaPoolRoot5AllocWeight": tHsmdaPoolRoot5AllocWeight,
       "tHsmdaPoolRoot6AllocWeight": tHsmdaPoolRoot6AllocWeight,
       "tHsmdaPoolRoot7AllocWeight": tHsmdaPoolRoot7AllocWeight,
       "tHsmdaPoolRoot8AllocWeight": tHsmdaPoolRoot8AllocWeight,
       "tHsmdaPoolClass1Parent": tHsmdaPoolClass1Parent,
       "tHsmdaPoolClass1AllocPercent": tHsmdaPoolClass1AllocPercent,
       "tHsmdaPoolClass2Parent": tHsmdaPoolClass2Parent,
       "tHsmdaPoolClass2AllocPercent": tHsmdaPoolClass2AllocPercent,
       "tHsmdaPoolClass3Parent": tHsmdaPoolClass3Parent,
       "tHsmdaPoolClass3AllocPercent": tHsmdaPoolClass3AllocPercent,
       "tHsmdaPoolClass4Parent": tHsmdaPoolClass4Parent,
       "tHsmdaPoolClass4AllocPercent": tHsmdaPoolClass4AllocPercent,
       "tHsmdaPoolClass5Parent": tHsmdaPoolClass5Parent,
       "tHsmdaPoolClass5AllocPercent": tHsmdaPoolClass5AllocPercent,
       "tHsmdaPoolClass6Parent": tHsmdaPoolClass6Parent,
       "tHsmdaPoolClass6AllocPercent": tHsmdaPoolClass6AllocPercent,
       "tHsmdaPoolClass7Parent": tHsmdaPoolClass7Parent,
       "tHsmdaPoolClass7AllocPercent": tHsmdaPoolClass7AllocPercent,
       "tHsmdaPoolClass8Parent": tHsmdaPoolClass8Parent,
       "tHsmdaPoolClass8AllocPercent": tHsmdaPoolClass8AllocPercent,
       "tMcMlpppIngressObjects": tMcMlpppIngressObjects,
       "tMcMlpppIngrProfTable": tMcMlpppIngrProfTable,
       "tMcMlpppIngrProfEntry": tMcMlpppIngrProfEntry,
       "tMcMlpppIngrProfIndex": tMcMlpppIngrProfIndex,
       "tMcMlpppIngrProfDescription": tMcMlpppIngrProfDescription,
       "tMcMlpppIngrProfLastChanged": tMcMlpppIngrProfLastChanged,
       "tMcMlpppIngrProfRowStatus": tMcMlpppIngrProfRowStatus,
       "tMcMlpppIngrClassTable": tMcMlpppIngrClassTable,
       "tMcMlpppIngrClassEntry": tMcMlpppIngrClassEntry,
       "tMcMlpppIngrClassIndex": tMcMlpppIngrClassIndex,
       "tMcMlpppIngrClassReassemblyTmout": tMcMlpppIngrClassReassemblyTmout,
       "tMcMlpppIngrClassLastChanged": tMcMlpppIngrClassLastChanged,
       "tMcMlpppEgressObjects": tMcMlpppEgressObjects,
       "tMcMlpppEgrProfTable": tMcMlpppEgrProfTable,
       "tMcMlpppEgrProfEntry": tMcMlpppEgrProfEntry,
       "tMcMlpppEgrProfIndex": tMcMlpppEgrProfIndex,
       "tMcMlpppEgrProfDescription": tMcMlpppEgrProfDescription,
       "tMcMlpppEgrProfLastChanged": tMcMlpppEgrProfLastChanged,
       "tMcMlpppEgrProfRowStatus": tMcMlpppEgrProfRowStatus,
       "tMcMlpppEgrClassTable": tMcMlpppEgrClassTable,
       "tMcMlpppEgrClassEntry": tMcMlpppEgrClassEntry,
       "tMcMlpppEgrClassIndex": tMcMlpppEgrClassIndex,
       "tMcMlpppEgrClassMir": tMcMlpppEgrClassMir,
       "tMcMlpppEgrClassWeight": tMcMlpppEgrClassWeight,
       "tMcMlpppEgrClassMaxSize": tMcMlpppEgrClassMaxSize,
       "tMcMlpppEgrClassLastChanged": tMcMlpppEgrClassLastChanged,
       "tMcMlpppEgrFCTable": tMcMlpppEgrFCTable,
       "tMcMlpppEgrFCEntry": tMcMlpppEgrFCEntry,
       "tMcMlpppEgrFCName": tMcMlpppEgrFCName,
       "tMcMlpppEgrFCClass": tMcMlpppEgrFCClass,
       "tMcMlpppEgrFCLastChanged": tMcMlpppEgrFCLastChanged,
       "tMcFrIngressObjects": tMcFrIngressObjects,
       "tMcFrIngrProfTable": tMcFrIngrProfTable,
       "tMcFrIngrProfEntry": tMcFrIngrProfEntry,
       "tMcFrIngrProfIndex": tMcFrIngrProfIndex,
       "tMcFrIngrProfDescription": tMcFrIngrProfDescription,
       "tMcFrIngrProfLastChanged": tMcFrIngrProfLastChanged,
       "tMcFrIngrProfRowStatus": tMcFrIngrProfRowStatus,
       "tMcFrIngrClassTable": tMcFrIngrClassTable,
       "tMcFrIngrClassEntry": tMcFrIngrClassEntry,
       "tMcFrIngrClassIndex": tMcFrIngrClassIndex,
       "tMcFrIngrClassReassemblyTmout": tMcFrIngrClassReassemblyTmout,
       "tMcFrIngrClassLastChanged": tMcFrIngrClassLastChanged,
       "tMcFrEgressObjects": tMcFrEgressObjects,
       "tMcFrEgrProfTable": tMcFrEgrProfTable,
       "tMcFrEgrProfEntry": tMcFrEgrProfEntry,
       "tMcFrEgrProfIndex": tMcFrEgrProfIndex,
       "tMcFrEgrProfDescription": tMcFrEgrProfDescription,
       "tMcFrEgrProfLastChanged": tMcFrEgrProfLastChanged,
       "tMcFrEgrProfRowStatus": tMcFrEgrProfRowStatus,
       "tMcFrEgrClassTable": tMcFrEgrClassTable,
       "tMcFrEgrClassEntry": tMcFrEgrClassEntry,
       "tMcFrEgrClassIndex": tMcFrEgrClassIndex,
       "tMcFrEgrClassMir": tMcFrEgrClassMir,
       "tMcFrEgrClassWeight": tMcFrEgrClassWeight,
       "tMcFrEgrClassMaxSize": tMcFrEgrClassMaxSize,
       "tMcFrEgrClassLastChanged": tMcFrEgrClassLastChanged,
       "tQosPolicerObjects": tQosPolicerObjects,
       "tQosPolicerCtrlPolTable": tQosPolicerCtrlPolTable,
       "tQosPolicerCtrlPolEntry": tQosPolicerCtrlPolEntry,
       "tQosPolicerCtrlPolName": tQosPolicerCtrlPolName,
       "tQosPolicerCtrlPolRowStatus": tQosPolicerCtrlPolRowStatus,
       "tQosPolicerCtrlPolLastChgd": tQosPolicerCtrlPolLastChgd,
       "tQosPolicerCtrlPolDescr": tQosPolicerCtrlPolDescr,
       "tQosPolicerCtrlPolRootMaxRate": tQosPolicerCtrlPolRootMaxRate,
       "tQosPolicerCtrlPolMinMBSSep": tQosPolicerCtrlPolMinMBSSep,
       "tQosPolicerCtrlPolProfPref": tQosPolicerCtrlPolProfPref,
       "tQosPolicerLevelTable": tQosPolicerLevelTable,
       "tQosPolicerLevelEntry": tQosPolicerLevelEntry,
       "tQosPolicerLevel": tQosPolicerLevel,
       "tQosPolicerLevelLastChgd": tQosPolicerLevelLastChgd,
       "tQosPolicerLevelCumMBS": tQosPolicerLevelCumMBS,
       "tQosPolicerLevelFixedMBS": tQosPolicerLevelFixedMBS,
       "tQosPolicerArbiterTable": tQosPolicerArbiterTable,
       "tQosPolicerArbiterEntry": tQosPolicerArbiterEntry,
       "tQosPolicerArbiterTier": tQosPolicerArbiterTier,
       "tQosPolicerArbiterName": tQosPolicerArbiterName,
       "tQosPolicerArbiterRowStatus": tQosPolicerArbiterRowStatus,
       "tQosPolicerArbiterLastChgd": tQosPolicerArbiterLastChgd,
       "tQosPolicerArbiterDescr": tQosPolicerArbiterDescr,
       "tQosPolicerArbiterRate": tQosPolicerArbiterRate,
       "tQosPolicerArbiterParent": tQosPolicerArbiterParent,
       "tQosPolicerArbiterLevel": tQosPolicerArbiterLevel,
       "tQosPolicerArbiterWeight": tQosPolicerArbiterWeight,
       "tQosIngPolicerTable": tQosIngPolicerTable,
       "tQosIngPolicerEntry": tQosIngPolicerEntry,
       "tQosIngPolicerId": tQosIngPolicerId,
       "tQosIngPolicerRowStatus": tQosIngPolicerRowStatus,
       "tQosIngPolicerLastChanged": tQosIngPolicerLastChanged,
       "tQosIngPolicerDescr": tQosIngPolicerDescr,
       "tQosIngPolicerPIRAdaptation": tQosIngPolicerPIRAdaptation,
       "tQosIngPolicerCIRAdaptation": tQosIngPolicerCIRAdaptation,
       "tQosIngPolicerParent": tQosIngPolicerParent,
       "tQosIngPolicerLevel": tQosIngPolicerLevel,
       "tQosIngPolicerWeight": tQosIngPolicerWeight,
       "tQosIngPolicerAdminPIR": tQosIngPolicerAdminPIR,
       "tQosIngPolicerAdminCIR": tQosIngPolicerAdminCIR,
       "tQosIngPolicerCBS": tQosIngPolicerCBS,
       "tQosIngPolicerMBS": tQosIngPolicerMBS,
       "tQosIngPolicerHiPrioOnly": tQosIngPolicerHiPrioOnly,
       "tQosIngPolicerPktOffset": tQosIngPolicerPktOffset,
       "tQosIngPolicerProfileCapped": tQosIngPolicerProfileCapped,
       "tQosIngPolicerStatMode": tQosIngPolicerStatMode,
       "tQosIngPolicerSlopeStartDepth": tQosIngPolicerSlopeStartDepth,
       "tQosIngPolicerSlopeMaxDepth": tQosIngPolicerSlopeMaxDepth,
       "tQosIngPolicerSlopeMaxProb": tQosIngPolicerSlopeMaxProb,
       "tQosIngPolicerSlopeMap": tQosIngPolicerSlopeMap,
       "tQosIngPolicerAdvCfgPolicy": tQosIngPolicerAdvCfgPolicy,
       "tQosEgrPolicerTable": tQosEgrPolicerTable,
       "tQosEgrPolicerEntry": tQosEgrPolicerEntry,
       "tQosEgrPolicerId": tQosEgrPolicerId,
       "tQosEgrPolicerRowStatus": tQosEgrPolicerRowStatus,
       "tQosEgrPolicerLastChanged": tQosEgrPolicerLastChanged,
       "tQosEgrPolicerDescr": tQosEgrPolicerDescr,
       "tQosEgrPolicerPIRAdaptation": tQosEgrPolicerPIRAdaptation,
       "tQosEgrPolicerCIRAdaptation": tQosEgrPolicerCIRAdaptation,
       "tQosEgrPolicerParent": tQosEgrPolicerParent,
       "tQosEgrPolicerLevel": tQosEgrPolicerLevel,
       "tQosEgrPolicerWeight": tQosEgrPolicerWeight,
       "tQosEgrPolicerAdminPIR": tQosEgrPolicerAdminPIR,
       "tQosEgrPolicerAdminCIR": tQosEgrPolicerAdminCIR,
       "tQosEgrPolicerCBS": tQosEgrPolicerCBS,
       "tQosEgrPolicerMBS": tQosEgrPolicerMBS,
       "tQosEgrPolicerHiPrioOnly": tQosEgrPolicerHiPrioOnly,
       "tQosEgrPolicerPktOffset": tQosEgrPolicerPktOffset,
       "tQosEgrPolicerProfileCapped": tQosEgrPolicerProfileCapped,
       "tQosEgrPolicerStatMode": tQosEgrPolicerStatMode,
       "tQosEgrPolicerSlopeStartDepth": tQosEgrPolicerSlopeStartDepth,
       "tQosEgrPolicerSlopeMaxDepth": tQosEgrPolicerSlopeMaxDepth,
       "tQosEgrPolicerSlopeMaxProb": tQosEgrPolicerSlopeMaxProb,
       "tQosEgrPolicerSlopeMap": tQosEgrPolicerSlopeMap,
       "tQosEgrPolicerAdvCfgPolicy": tQosEgrPolicerAdvCfgPolicy,
       "tAdvCfgPolicyTable": tAdvCfgPolicyTable,
       "tAdvCfgPolicyEntry": tAdvCfgPolicyEntry,
       "tAdvCfgPolicyName": tAdvCfgPolicyName,
       "tAdvCfgPolicyRowStatus": tAdvCfgPolicyRowStatus,
       "tAdvCfgLastChanged": tAdvCfgLastChanged,
       "tAdvCfgDescription": tAdvCfgDescription,
       "tAdvCfgChildAdmnPirPrcnt": tAdvCfgChildAdmnPirPrcnt,
       "tAdvCfgChildAdminRate": tAdvCfgChildAdminRate,
       "tAdvCfgOMGranPirPrcnt": tAdvCfgOMGranPirPrcnt,
       "tAdvCfgOMGranRate": tAdvCfgOMGranRate,
       "tAdvCfgMaxDecPirPrcnt": tAdvCfgMaxDecPirPrcnt,
       "tAdvCfgMaxDecRate": tAdvCfgMaxDecRate,
       "tAdvCfgHiRateHoldTime": tAdvCfgHiRateHoldTime,
       "tAdvCfgTimeAvgFactor": tAdvCfgTimeAvgFactor,
       "tAdvCfgSampleInterval": tAdvCfgSampleInterval,
       "tAdvCfgFastStart": tAdvCfgFastStart,
       "tAdvCfgFastStop": tAdvCfgFastStop,
       "tAdvCfgAbvOffCapPirPrcnt": tAdvCfgAbvOffCapPirPrcnt,
       "tAdvCfgAbvOffCapRate": tAdvCfgAbvOffCapRate,
       "tAdvCfgBWDGranPirPrcnt": tAdvCfgBWDGranPirPrcnt,
       "tAdvCfgBWDGranRate": tAdvCfgBWDGranRate,
       "tAdvCfgMinOnly": tAdvCfgMinOnly,
       "tAdvCfgDecOnly": tAdvCfgDecOnly,
       "tWrrObjects": tWrrObjects,
       "tHsmdaWrrPolicyTable": tHsmdaWrrPolicyTable,
       "tHsmdaWrrPolicyEntry": tHsmdaWrrPolicyEntry,
       "tHsmdaWrrPolicyName": tHsmdaWrrPolicyName,
       "tHsmdaWrrPolicyRowStatus": tHsmdaWrrPolicyRowStatus,
       "tHsmdaWrrPolicyLastChanged": tHsmdaWrrPolicyLastChanged,
       "tHsmdaWrrPolicyDescription": tHsmdaWrrPolicyDescription,
       "tHsmdaWrrPolicyIncludeQueues": tHsmdaWrrPolicyIncludeQueues,
       "tHsmdaWrrPolicySchedUsingClass": tHsmdaWrrPolicySchedUsingClass,
       "tHsmdaWrrPolicyAggWeightAtClass": tHsmdaWrrPolicyAggWeightAtClass,
       "tQosNotifyPrefix": tQosNotifyPrefix,
       "tQosNotifications": tQosNotifications}
)
