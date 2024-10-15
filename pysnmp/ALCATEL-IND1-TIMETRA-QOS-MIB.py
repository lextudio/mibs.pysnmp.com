# SNMP MIB module (ALCATEL-IND1-TIMETRA-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:13 2024
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

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(Dot1PPriority,
 IpAddressPrefixLength,
 ServiceAccessPoint,
 TCIRRate,
 TDSCPName,
 TDSCPNameOrEmpty,
 TDSCPValue,
 TEgressQueueId,
 TFCName,
 TFCNameOrEmpty,
 TFrameType,
 TIngressQueueId,
 TIpProtocol,
 TItemDescription,
 TLspExpValue,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPIRRateOrZero,
 TPolicyID,
 TPortSchedulerCIR,
 TPortSchedulerPIR,
 TQueueId,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TTcpUdpPort,
 TTcpUdpPortOperator,
 TWeight,
 TmnxEnabledDisabled) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "ServiceAccessPoint",
    "TCIRRate",
    "TDSCPName",
    "TDSCPNameOrEmpty",
    "TDSCPValue",
    "TEgressQueueId",
    "TFCName",
    "TFCNameOrEmpty",
    "TFrameType",
    "TIngressQueueId",
    "TIpProtocol",
    "TItemDescription",
    "TLspExpValue",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPIRRateOrZero",
    "TPolicyID",
    "TPortSchedulerCIR",
    "TPortSchedulerPIR",
    "TQueueId",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TTcpUdpPort",
    "TTcpUdpPortOperator",
    "TWeight",
    "TmnxEnabledDisabled")

(AtmServiceCategory,
 AtmTrafficDescrParamIndex) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmServiceCategory",
    "AtmTrafficDescrParamIndex")

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


# MODULE-IDENTITY

timetraQosMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 16)
)
timetraQosMIBModule.setRevisions(
        ("1908-01-01 00:00",
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



class TNetworkPolicyID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TItemScope(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclusive", 1),
          ("template", 2))
    )



class TItemMatch(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("off", 1),
          ("true", 3))
    )



class TPriority(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 1))
    )



class TPriorityOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("high", 2),
          ("low", 1))
    )



class TProfile(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )



class TDEProfile(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("de", 3),
          ("in", 1),
          ("out", 2))
    )



class TProfileOrNone(Integer32, TextualConvention):
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
        *(("in", 1),
          ("none", 0),
          ("out", 2))
    )



class TAdaptationRule(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closest", 3),
          ("max", 1),
          ("min", 2))
    )



class TRemarkType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("none", 1),
          ("precedence", 3))
    )



class TPrecValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TPrecValueOrNone(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )



class TBurstSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 131072),
    )



class TBurstPercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TBurstHundredthsOfPercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )



class TBurstPercentOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 100),
    )



class TRatePercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TPIRRatePercent(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TLevel(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class TLevelOrDefault(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class TQueueMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("priority", 1),
          ("profile", 2))
    )



class TEntryIndicator(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class TEntryId(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )



class TMatchCriteria(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("none", 3))
    )



class TAtmTdpDescrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clp0And1pcr", 0),
          ("clp0And1pcrPlusClp0And1scr", 1),
          ("clp0And1pcrPlusClp0scr", 2),
          ("clp0And1pcrPlusClp0scrTag", 3))
    )



class TDEValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
)
if mibBuilder.loadTexts:
    tSapIngressEntry.setStatus("current")


class _TSapIngressIndex_Type(TSapIngressPolicyID):
    """Custom type tSapIngressIndex based on TSapIngressPolicyID"""
    subtypeSpec = TSapIngressPolicyID.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueue"),
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
    tSapIngressQueueMBS.setStatus("current")


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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCP"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pValue"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCName"),
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
_TSapIngressFCQueue_Type = TIngressQueueId
_TSapIngressFCQueue_Object = MibTableColumn
tSapIngressFCQueue = _TSapIngressFCQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 3),
    _TSapIngressFCQueue_Type()
)
tSapIngressFCQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCQueue.setStatus("current")
_TSapIngressFCMCastQueue_Type = TIngressQueueId
_TSapIngressFCMCastQueue_Object = MibTableColumn
tSapIngressFCMCastQueue = _TSapIngressFCMCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 4),
    _TSapIngressFCMCastQueue_Type()
)
tSapIngressFCMCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCMCastQueue.setStatus("current")
_TSapIngressFCBCastQueue_Type = TIngressQueueId
_TSapIngressFCBCastQueue_Object = MibTableColumn
tSapIngressFCBCastQueue = _TSapIngressFCBCastQueue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 3, 7, 1, 5),
    _TSapIngressFCBCastQueue_Type()
)
tSapIngressFCBCastQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tSapIngressFCBCastQueue.setStatus("current")
_TSapIngressFCUnknownQueue_Type = TIngressQueueId
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecValue"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueIndex"),
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
    tSapEgressQueueMBS.setStatus("current")


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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCName"),
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
_TSapEgressFCQueue_Type = TEgressQueueId
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
)
if mibBuilder.loadTexts:
    tNetworkPolicyEntry.setStatus("current")
_TNetworkPolicyIndex_Type = TNetworkPolicyID
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


class _TNetworkPolicyIngressDefaultActionProfile_Type(TProfile):
    """Custom type tNetworkPolicyIngressDefaultActionProfile based on TProfile"""


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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCP"),
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


class _TNetworkIngressDSCPFC_Type(TFCNameOrEmpty):
    """Custom type tNetworkIngressDSCPFC based on TFCNameOrEmpty"""
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pValue"),
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


class _TNetworkIngressDot1pFC_Type(TFCNameOrEmpty):
    """Custom type tNetworkIngressDot1pFC based on TFCNameOrEmpty"""
    defaultHexValue = ""


_TNetworkIngressDot1pFC_Object = MibTableColumn
tNetworkIngressDot1pFC = _TNetworkIngressDot1pFC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 5, 3, 1, 3),
    _TNetworkIngressDot1pFC_Type()
)
tNetworkIngressDot1pFC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tNetworkIngressDot1pFC.setStatus("current")
_TNetworkIngressDot1pProfile_Type = TDEProfile
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXP"),
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


class _TNetworkIngressLSPEXPFC_Type(TFCNameOrEmpty):
    """Custom type tNetworkIngressLSPEXPFC based on TFCNameOrEmpty"""
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIndex"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueue"),
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
    defaultValue = 0


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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicy"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueId"),
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


class _TSharedQueuePIR_Type(TRatePercent):
    """Custom type tSharedQueuePIR based on TRatePercent"""
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicy"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCName"),
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
        ValueRangeConstraint(9, 16),
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
        ValueRangeConstraint(17, 24),
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
        ValueRangeConstraint(25, 32),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopePolicy"),
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
    (1, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerTier"),
    (1, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
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


class _TVirtualSchedulerPIR_Type(TPIRRate):
    """Custom type tVirtualSchedulerPIR based on TPIRRate"""
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


class _TVirtualSchedulerCIR_Type(TCIRRate):
    """Custom type tVirtualSchedulerCIR based on TCIRRate"""
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
    (1, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyName"),
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


class _TPortSchedulerPlcyMaxRate_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyMaxRate based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl1PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl1PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl2PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl2PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl3PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl3PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl4PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl4PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl5PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl5PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl6PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl6PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl7PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl7PIR based on TPortSchedulerPIR"""
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


class _TPortSchedulerPlcyLvl8PIR_Type(TPortSchedulerPIR):
    """Custom type tPortSchedulerPlcyLvl8PIR based on TPortSchedulerPIR"""
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpIndex"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyName"),
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
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolName"),
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


_TQ1NamedPoolReservedCbs_Object = MibTableColumn
tQ1NamedPoolReservedCbs = _TQ1NamedPoolReservedCbs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 16, 22, 2, 1, 9),
    _TQ1NamedPoolReservedCbs_Type()
)
tQ1NamedPoolReservedCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tQ1NamedPoolReservedCbs.setStatus("current")
_TQosNotifyPrefix_ObjectIdentity = ObjectIdentity
tQosNotifyPrefix = _TQosNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 16)
)
_TQosNotifications_ObjectIdentity = ObjectIdentity
tQosNotifications = _TQosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 16, 0)
)

# Managed Objects groups

tmnxQosGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 1)
)
tmnxQosGlobalGroup.setObjects(
    ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQosDomainLastChanged")
)
if mibBuilder.loadTexts:
    tmnxQosGlobalGroup.setStatus("current")

tmnxQosDSCPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 2)
)
tmnxQosDSCPGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPNameRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPNameStorageType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPNameDscpValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPNameLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tDSCPNameTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosDSCPGroup.setStatus("current")

tmnxQosFCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 3)
)
tmnxQosFCGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCStorageType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCNameLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tFCNameTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosFCGroup.setStatus("current")

tmnxQosSlopeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 7)
)
tmnxQosSlopeGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeHiAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeHiStartAverage"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeHiMaxAverage"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeHiMaxProbability"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeLoAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeLoStartAverage"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeLoMaxAverage"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeLoMaxProbability"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeTimeAvgFactor"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopeLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSlopePolicyTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSlopeGroup.setStatus("current")

tmnxQosSchedulerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 8)
)
tmnxQosSchedulerGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerSummedCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSchedulerGroup.setStatus("obsolete")

tQosObsoleteObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 10)
)
tQosObsoleteObjectsGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueOperPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueOperCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueOperPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueOperCIR"))
)
if mibBuilder.loadTexts:
    tQosObsoleteObjectsGroup.setStatus("current")

tmnxQosSapEgressR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 12)
)
tmnxQosSapEgressR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressR2r1Group.setStatus("obsolete")

tmnxQosNetworkR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 13)
)
tmnxQosNetworkR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkR2r1Group.setStatus("obsolete")

tmnxQosAtmTdpV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 15)
)
tmnxQosAtmTdpV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpSir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpPir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpMbs"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpMir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpShaping"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpServCat"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpDescrType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpCdvt"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpPolicing"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpIndexNext"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpsMaxSupported"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpsCurrentlyConfigured"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosAtmTdpV3v0Group.setStatus("obsolete")

tmnxQosSapIpv6FilterR4r0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 16)
)
tmnxQosSapIpv6FilterR4r0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaActionPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourceIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaNextHeader"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaSourcePortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDestPortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaDSCP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPv6CriteriaTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIpv6FilterR4r0Group.setStatus("current")

tmnxQosQueueV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 18)
)
tmnxQosQueueV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePoolName"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueuePIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueIsMultipoint"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCMCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCBCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSharedQueueFCUnknownQueue"))
)
if mibBuilder.loadTexts:
    tmnxQosQueueV4v0Group.setStatus("current")

tmnxQosSapIngressV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 19)
)
tmnxQosSapIngressV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV4v0Group.setStatus("obsolete")

tmnxQosSchedulerV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 20)
)
tmnxQosSchedulerV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerSummedCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerUsePortParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPortLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPortWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerPortCIRWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyMaxRate"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl1PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl1CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl2PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl2CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl3PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl3CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl4PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl4CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl5PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl5CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl6PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl6CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl7PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl7CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl8PIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyLvl8CIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tPortSchedulerPlcyOrphanCIRWght"))
)
if mibBuilder.loadTexts:
    tmnxQosSchedulerV5v0Group.setStatus("current")

tmnxQosSapEgressV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 21)
)
tmnxQosSapEgressV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueUsePortParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortAvgOverhead"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV5v0Group.setStatus("obsolete")

tmnxQosNetworkV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 22)
)
tmnxQosNetworkV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueUsePortParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortCIRWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortAvgOverhead"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV5v0Group.setStatus("obsolete")

tmnxQosAtmTdpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 24)
)
tmnxQosAtmTdpV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpSir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpPir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpMbs"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpMir"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpShaping"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpServCat"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpDescrType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpCdvt"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpPolicing"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpCLPTagging"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpIndexNext"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpsMaxSupported"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpsCurrentlyConfigured"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tAtmTdpTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosAtmTdpV5v0Group.setStatus("current")

tmnxQosSapIngressV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 25)
)
tmnxQosSapIngressV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDefaultFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDefaultFCPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMatchCriteria"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueMode"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueuePoolName"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressQueuePoliced"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDSCPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressDot1pTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaActionPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourceIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestIpMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaProtocol"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaSourcePortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue1"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortValue2"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDestPortOperator"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaDSCP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaFragment"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressIPCriteriaTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaActionPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaFrameType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSrcMacMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacAddr"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDstMacMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDot1PMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaEthernetType"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaDSAPMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAP"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSSAPMask"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapPid"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaSnapOui"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressMacCriteriaTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCMCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCBCastQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCUnknownQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCInProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCOutProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecFCPriority"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressPrecTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapIngressFCDE1OutOfProfile"))
)
if mibBuilder.loadTexts:
    tmnxQosSapIngressV6v0Group.setStatus("current")

tmnxQosSapEgressV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 26)
)
tmnxQosSapEgressV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCQueue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDot1PInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDot1POutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCForceDEValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDEMark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCInProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCOutProfDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCInProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCOutProfPrec"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueueUsePortParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortCIRWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePortAvgOverhead"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressQueuePoolName"))
)
if mibBuilder.loadTexts:
    tmnxQosSapEgressV6v0Group.setStatus("current")

tmnxQosNetworkV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 27)
)
tmnxQosNetworkV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyScope"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressDefaultActionProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyEgressRemark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyIngressLerUseDscp"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDSCPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressDot1pTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkIngressLSPEXPTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDSCPOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLspExpOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pInProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDot1pOutProfile"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCForceDEValue"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCDEMark"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkEgressFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePoolName"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRLevel"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueExpedite"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePIR"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueMBS"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueUsePortParent"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortCIRLvl"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortCIRWght"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePortAvgOverhead"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueuePIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFC"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCMCast"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNetworkQueueFCTableLastChanged"))
)
if mibBuilder.loadTexts:
    tmnxQosNetworkV6v0Group.setStatus("current")

tmnxQosFrameBasedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 28)
)
tmnxQosFrameBasedV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyFrameBasedAccnt")
)
if mibBuilder.loadTexts:
    tmnxQosFrameBasedV6v0Group.setStatus("current")

tmnxQosObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 29)
)
tmnxQosObsoletedV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tSapEgressFCDot1PValue")
)
if mibBuilder.loadTexts:
    tmnxQosObsoletedV6v0Group.setStatus("current")

tmnxQosNamedPoolPolicyV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 2, 30)
)
tmnxQosNamedPoolPolicyV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1DefaultWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1MdaWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tNamedPoolPolicyQ1PortWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolRowStatus"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolLastChanged"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolDescription"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolNetworkAllocWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolAccessAllocWeight"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolSlopePolicy"),
        ("ALCATEL-IND1-TIMETRA-QOS-MIB", "tQ1NamedPoolReservedCbs"))
)
if mibBuilder.loadTexts:
    tmnxQosNamedPoolPolicyV6v0Group.setStatus("current")


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
        "current"
    )

tmnxQos7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 16, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxQos7750V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-QOS-MIB",
    **{"TNetworkPolicyID": TNetworkPolicyID,
       "TItemScope": TItemScope,
       "TItemMatch": TItemMatch,
       "TPriority": TPriority,
       "TPriorityOrDefault": TPriorityOrDefault,
       "TProfile": TProfile,
       "TDEProfile": TDEProfile,
       "TProfileOrNone": TProfileOrNone,
       "TAdaptationRule": TAdaptationRule,
       "TRemarkType": TRemarkType,
       "TPrecValue": TPrecValue,
       "TPrecValueOrNone": TPrecValueOrNone,
       "TBurstSize": TBurstSize,
       "TBurstPercent": TBurstPercent,
       "TBurstHundredthsOfPercent": TBurstHundredthsOfPercent,
       "TBurstPercentOrDefault": TBurstPercentOrDefault,
       "TRatePercent": TRatePercent,
       "TPIRRatePercent": TPIRRatePercent,
       "TLevel": TLevel,
       "TLevelOrDefault": TLevelOrDefault,
       "TQueueMode": TQueueMode,
       "TEntryIndicator": TEntryIndicator,
       "TEntryId": TEntryId,
       "TMatchCriteria": TMatchCriteria,
       "TAtmTdpDescrType": TAtmTdpDescrType,
       "TDEValue": TDEValue,
       "timetraQosMIBModule": timetraQosMIBModule,
       "tmnxQosConformance": tmnxQosConformance,
       "tmnxQosCompliances": tmnxQosCompliances,
       "tmnxQos7450V4v0Compliance": tmnxQos7450V4v0Compliance,
       "tmnxQos7750V4v0Compliance": tmnxQos7750V4v0Compliance,
       "tmnxQos7450V5v0Compliance": tmnxQos7450V5v0Compliance,
       "tmnxQos7750V5v0Compliance": tmnxQos7750V5v0Compliance,
       "tmnxQos7450V6v0Compliance": tmnxQos7450V6v0Compliance,
       "tmnxQos7750V6v0Compliance": tmnxQos7750V6v0Compliance,
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
       "tmnxQosAtmTdpV5v0Group": tmnxQosAtmTdpV5v0Group,
       "tmnxQosSapIngressV6v0Group": tmnxQosSapIngressV6v0Group,
       "tmnxQosSapEgressV6v0Group": tmnxQosSapEgressV6v0Group,
       "tmnxQosNetworkV6v0Group": tmnxQosNetworkV6v0Group,
       "tmnxQosFrameBasedV6v0Group": tmnxQosFrameBasedV6v0Group,
       "tmnxQosObsoletedV6v0Group": tmnxQosObsoletedV6v0Group,
       "tmnxQosNamedPoolPolicyV6v0Group": tmnxQosNamedPoolPolicyV6v0Group,
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
       "tSapIngressDSCPTable": tSapIngressDSCPTable,
       "tSapIngressDSCPEntry": tSapIngressDSCPEntry,
       "tSapIngressDSCP": tSapIngressDSCP,
       "tSapIngressDSCPRowStatus": tSapIngressDSCPRowStatus,
       "tSapIngressDSCPFC": tSapIngressDSCPFC,
       "tSapIngressDSCPPriority": tSapIngressDSCPPriority,
       "tSapIngressDSCPLastChanged": tSapIngressDSCPLastChanged,
       "tSapIngressDot1pTable": tSapIngressDot1pTable,
       "tSapIngressDot1pEntry": tSapIngressDot1pEntry,
       "tSapIngressDot1pValue": tSapIngressDot1pValue,
       "tSapIngressDot1pRowStatus": tSapIngressDot1pRowStatus,
       "tSapIngressDot1pFC": tSapIngressDot1pFC,
       "tSapIngressDot1pPriority": tSapIngressDot1pPriority,
       "tSapIngressDot1pLastChanged": tSapIngressDot1pLastChanged,
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
       "tSapIngressFCDE1OutOfProfile": tSapIngressFCDE1OutOfProfile,
       "tSapIngressPrecTable": tSapIngressPrecTable,
       "tSapIngressPrecEntry": tSapIngressPrecEntry,
       "tSapIngressPrecValue": tSapIngressPrecValue,
       "tSapIngressPrecRowStatus": tSapIngressPrecRowStatus,
       "tSapIngressPrecFC": tSapIngressPrecFC,
       "tSapIngressPrecFCPriority": tSapIngressPrecFCPriority,
       "tSapIngressPrecLastChanged": tSapIngressPrecLastChanged,
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
       "tSapEgressObjects": tSapEgressObjects,
       "tSapEgressTable": tSapEgressTable,
       "tSapEgressEntry": tSapEgressEntry,
       "tSapEgressIndex": tSapEgressIndex,
       "tSapEgressRowStatus": tSapEgressRowStatus,
       "tSapEgressScope": tSapEgressScope,
       "tSapEgressDescription": tSapEgressDescription,
       "tSapEgressLastChanged": tSapEgressLastChanged,
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
       "tSapEgressFCTable": tSapEgressFCTable,
       "tSapEgressFCEntry": tSapEgressFCEntry,
       "tSapEgressFCName": tSapEgressFCName,
       "tSapEgressFCRowStatus": tSapEgressFCRowStatus,
       "tSapEgressFCQueue": tSapEgressFCQueue,
       "tSapEgressFCDot1PValue": tSapEgressFCDot1PValue,
       "tSapEgressFCLastChanged": tSapEgressFCLastChanged,
       "tSapEgressFCDot1PInProfile": tSapEgressFCDot1PInProfile,
       "tSapEgressFCDot1POutProfile": tSapEgressFCDot1POutProfile,
       "tSapEgressFCForceDEValue": tSapEgressFCForceDEValue,
       "tSapEgressFCDEMark": tSapEgressFCDEMark,
       "tSapEgressFCInProfDscp": tSapEgressFCInProfDscp,
       "tSapEgressFCOutProfDscp": tSapEgressFCOutProfDscp,
       "tSapEgressFCInProfPrec": tSapEgressFCInProfPrec,
       "tSapEgressFCOutProfPrec": tSapEgressFCOutProfPrec,
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
       "tNetworkQueueObjects": tNetworkQueueObjects,
       "tNetworkQueuePolicyTable": tNetworkQueuePolicyTable,
       "tNetworkQueuePolicyEntry": tNetworkQueuePolicyEntry,
       "tNetworkQueuePolicy": tNetworkQueuePolicy,
       "tNetworkQueuePolicyRowStatus": tNetworkQueuePolicyRowStatus,
       "tNetworkQueuePolicyDescription": tNetworkQueuePolicyDescription,
       "tNetworkQueuePolicyLastChanged": tNetworkQueuePolicyLastChanged,
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
       "tQosTimeStampObjects": tQosTimeStampObjects,
       "tQosDomainLastChanged": tQosDomainLastChanged,
       "tDSCPNameTableLastChanged": tDSCPNameTableLastChanged,
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
       "tNamedPoolPolicyTableLastChanged": tNamedPoolPolicyTableLastChanged,
       "tQ1NamedPoolTableLastChanged": tQ1NamedPoolTableLastChanged,
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
       "tQosNotifyPrefix": tQosNotifyPrefix,
       "tQosNotifications": tQosNotifications}
)
