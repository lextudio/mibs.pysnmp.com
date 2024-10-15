# SNMP MIB module (NetWare-Server-Trend-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NetWare-Server-Trend-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:09 2024
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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



class NWTime(Integer32):
    """Custom type NWTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class Seconds(Integer32):
    """Custom type Seconds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_NwTrend_ObjectIdentity = ObjectIdentity
nwTrend = _NwTrend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 26)
)
_NwtControl_ObjectIdentity = ObjectIdentity
nwtControl = _NwtControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1)
)
_NwtControlTable_Object = MibTable
nwtControlTable = _NwtControlTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1)
)
if mibBuilder.loadTexts:
    nwtControlTable.setStatus("mandatory")
_NwtControlEntry_Object = MibTableRow
nwtControlEntry = _NwtControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1)
)
nwtControlEntry.setIndexNames(
    (0, "NetWare-Server-Trend-MIB", "nwtControlAttributeClass"),
    (0, "NetWare-Server-Trend-MIB", "nwtControlIndex"),
)
if mibBuilder.loadTexts:
    nwtControlEntry.setStatus("mandatory")


class _NwtControlAttributeClass_Type(Integer32):
    """Custom type nwtControlAttributeClass based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("avgConnections", 2),
          ("avgLoggedInUsers", 1),
          ("diskPctFreeRedirectionArea", 24),
          ("fileReadKBytes", 5),
          ("fileReads", 3),
          ("fileWriteKBytes", 6),
          ("fileWrites", 4),
          ("lslInPackets", 7),
          ("lslOutPackets", 8),
          ("ncpRequests", 9),
          ("noECBCount", 26),
          ("osPktRcvBuffer", 27),
          ("pctAllocatedMemory", 13),
          ("pctCacheBuffers", 11),
          ("pctCacheHitRate", 23),
          ("pctCodeAndDataMemory", 12),
          ("pctCpuUtilization", 10),
          ("pctDirtyPacketReceiveBuffers", 14),
          ("physIfInKBytes", 17),
          ("physIfInPackets", 15),
          ("physIfOutKBytes", 18),
          ("physIfOutPackets", 16),
          ("queueAvgNextJobWaitTime", 21),
          ("queueAvgNumReadyJobs", 19),
          ("queueAvgNumReadyKBytes", 20),
          ("serverProcesses", 25),
          ("volumePctFreeSpace", 22))
    )


_NwtControlAttributeClass_Type.__name__ = "Integer32"
_NwtControlAttributeClass_Object = MibTableColumn
nwtControlAttributeClass = _NwtControlAttributeClass_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 1),
    _NwtControlAttributeClass_Type()
)
nwtControlAttributeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlAttributeClass.setStatus("mandatory")


class _NwtControlIndex_Type(Integer32):
    """Custom type nwtControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwtControlIndex_Type.__name__ = "Integer32"
_NwtControlIndex_Object = MibTableColumn
nwtControlIndex = _NwtControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 2),
    _NwtControlIndex_Type()
)
nwtControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlIndex.setStatus("mandatory")
_NwtControlAttributeInstance_Type = InternationalDisplayString
_NwtControlAttributeInstance_Object = MibTableColumn
nwtControlAttributeInstance = _NwtControlAttributeInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 3),
    _NwtControlAttributeInstance_Type()
)
nwtControlAttributeInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlAttributeInstance.setStatus("mandatory")


class _NwtControlSampleInterval_Type(Integer32):
    """Custom type nwtControlSampleInterval based on Integer32"""
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
        *(("eightHours", 11),
          ("fifteenMinutes", 7),
          ("fifteenSeconds", 3),
          ("fiveMinutes", 6),
          ("fiveSeconds", 1),
          ("fourHours", 10),
          ("oneDay", 12),
          ("oneHour", 9),
          ("oneMinute", 5),
          ("tenSeconds", 2),
          ("thirtyMinutes", 8),
          ("thirtySeconds", 4))
    )


_NwtControlSampleInterval_Type.__name__ = "Integer32"
_NwtControlSampleInterval_Object = MibTableColumn
nwtControlSampleInterval = _NwtControlSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 4),
    _NwtControlSampleInterval_Type()
)
nwtControlSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlSampleInterval.setStatus("mandatory")


class _NwtControlSampleType_Type(Integer32):
    """Custom type nwtControlSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("averageValue", 3),
          ("deltaValue", 2))
    )


_NwtControlSampleType_Type.__name__ = "Integer32"
_NwtControlSampleType_Object = MibTableColumn
nwtControlSampleType = _NwtControlSampleType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 5),
    _NwtControlSampleType_Type()
)
nwtControlSampleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlSampleType.setStatus("mandatory")
_NwtControlSampleInvalidValue_Type = Integer32
_NwtControlSampleInvalidValue_Object = MibTableColumn
nwtControlSampleInvalidValue = _NwtControlSampleInvalidValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 6),
    _NwtControlSampleInvalidValue_Type()
)
nwtControlSampleInvalidValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlSampleInvalidValue.setStatus("mandatory")
_NwtControlLastSampleValue_Type = Integer32
_NwtControlLastSampleValue_Object = MibTableColumn
nwtControlLastSampleValue = _NwtControlLastSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 7),
    _NwtControlLastSampleValue_Type()
)
nwtControlLastSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlLastSampleValue.setStatus("mandatory")
_NwtControlReferenceTimeStamp_Type = NWTime
_NwtControlReferenceTimeStamp_Object = MibTableColumn
nwtControlReferenceTimeStamp = _NwtControlReferenceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 8),
    _NwtControlReferenceTimeStamp_Type()
)
nwtControlReferenceTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlReferenceTimeStamp.setStatus("mandatory")


class _NwtControlThresholdState_Type(Integer32):
    """Custom type nwtControlThresholdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NwtControlThresholdState_Type.__name__ = "Integer32"
_NwtControlThresholdState_Object = MibTableColumn
nwtControlThresholdState = _NwtControlThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 9),
    _NwtControlThresholdState_Type()
)
nwtControlThresholdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlThresholdState.setStatus("mandatory")


class _NwtControlThresholdType_Type(Integer32):
    """Custom type nwtControlThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1))
    )


_NwtControlThresholdType_Type.__name__ = "Integer32"
_NwtControlThresholdType_Object = MibTableColumn
nwtControlThresholdType = _NwtControlThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 10),
    _NwtControlThresholdType_Type()
)
nwtControlThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlThresholdType.setStatus("mandatory")
_NwtControlRisingThreshold_Type = Integer32
_NwtControlRisingThreshold_Object = MibTableColumn
nwtControlRisingThreshold = _NwtControlRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 11),
    _NwtControlRisingThreshold_Type()
)
nwtControlRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlRisingThreshold.setStatus("mandatory")
_NwtControlFallingThreshold_Type = Integer32
_NwtControlFallingThreshold_Object = MibTableColumn
nwtControlFallingThreshold = _NwtControlFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 12),
    _NwtControlFallingThreshold_Type()
)
nwtControlFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlFallingThreshold.setStatus("mandatory")


class _NwtControlHistoryState_Type(Integer32):
    """Custom type nwtControlHistoryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_NwtControlHistoryState_Type.__name__ = "Integer32"
_NwtControlHistoryState_Object = MibTableColumn
nwtControlHistoryState = _NwtControlHistoryState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 13),
    _NwtControlHistoryState_Type()
)
nwtControlHistoryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlHistoryState.setStatus("mandatory")


class _NwtControlHistoryLastSampleIndex_Type(Integer32):
    """Custom type nwtControlHistoryLastSampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NwtControlHistoryLastSampleIndex_Type.__name__ = "Integer32"
_NwtControlHistoryLastSampleIndex_Object = MibTableColumn
nwtControlHistoryLastSampleIndex = _NwtControlHistoryLastSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 14),
    _NwtControlHistoryLastSampleIndex_Type()
)
nwtControlHistoryLastSampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlHistoryLastSampleIndex.setStatus("mandatory")


class _NwtControlHistoryBucketsRequested_Type(Integer32):
    """Custom type nwtControlHistoryBucketsRequested based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NwtControlHistoryBucketsRequested_Type.__name__ = "Integer32"
_NwtControlHistoryBucketsRequested_Object = MibTableColumn
nwtControlHistoryBucketsRequested = _NwtControlHistoryBucketsRequested_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 15),
    _NwtControlHistoryBucketsRequested_Type()
)
nwtControlHistoryBucketsRequested.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nwtControlHistoryBucketsRequested.setStatus("mandatory")


class _NwtControlHistoryBucketsGranted_Type(Integer32):
    """Custom type nwtControlHistoryBucketsGranted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NwtControlHistoryBucketsGranted_Type.__name__ = "Integer32"
_NwtControlHistoryBucketsGranted_Object = MibTableColumn
nwtControlHistoryBucketsGranted = _NwtControlHistoryBucketsGranted_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 16),
    _NwtControlHistoryBucketsGranted_Type()
)
nwtControlHistoryBucketsGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlHistoryBucketsGranted.setStatus("mandatory")


class _NwtControlStatus_Type(Integer32):
    """Custom type nwtControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NwtControlStatus_Type.__name__ = "Integer32"
_NwtControlStatus_Object = MibTableColumn
nwtControlStatus = _NwtControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 1, 1, 17),
    _NwtControlStatus_Type()
)
nwtControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtControlStatus.setStatus("mandatory")
_NwtHistoryTable_Object = MibTable
nwtHistoryTable = _NwtHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2)
)
if mibBuilder.loadTexts:
    nwtHistoryTable.setStatus("mandatory")
_NwtHistoryEntry_Object = MibTableRow
nwtHistoryEntry = _NwtHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1)
)
nwtHistoryEntry.setIndexNames(
    (0, "NetWare-Server-Trend-MIB", "nwtHistoryControlIndex"),
    (0, "NetWare-Server-Trend-MIB", "nwtHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    nwtHistoryEntry.setStatus("mandatory")


class _NwtHistoryControlIndex_Type(Integer32):
    """Custom type nwtHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwtHistoryControlIndex_Type.__name__ = "Integer32"
_NwtHistoryControlIndex_Object = MibTableColumn
nwtHistoryControlIndex = _NwtHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 1),
    _NwtHistoryControlIndex_Type()
)
nwtHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtHistoryControlIndex.setStatus("mandatory")


class _NwtHistorySampleIndex_Type(Integer32):
    """Custom type nwtHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NwtHistorySampleIndex_Type.__name__ = "Integer32"
_NwtHistorySampleIndex_Object = MibTableColumn
nwtHistorySampleIndex = _NwtHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 2),
    _NwtHistorySampleIndex_Type()
)
nwtHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtHistorySampleIndex.setStatus("mandatory")
_NwtHistorySampleValue_Type = Integer32
_NwtHistorySampleValue_Object = MibTableColumn
nwtHistorySampleValue = _NwtHistorySampleValue_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 1, 2, 1, 3),
    _NwtHistorySampleValue_Type()
)
nwtHistorySampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nwtHistorySampleValue.setStatus("mandatory")
_NwtTrapInfo_ObjectIdentity = ObjectIdentity
nwtTrapInfo = _NwtTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2)
)


class _NwtServerName_Type(InternationalDisplayString):
    """Custom type nwtServerName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_NwtServerName_Type.__name__ = "InternationalDisplayString"
_NwtServerName_Object = MibScalar
nwtServerName = _NwtServerName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 1),
    _NwtServerName_Type()
)
nwtServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtServerName.setStatus("mandatory")
_NwtTrapTime_Type = NWTime
_NwtTrapTime_Object = MibScalar
nwtTrapTime = _NwtTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 2),
    _NwtTrapTime_Type()
)
nwtTrapTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtTrapTime.setStatus("mandatory")
_NwtThreshold_Type = Integer32
_NwtThreshold_Object = MibScalar
nwtThreshold = _NwtThreshold_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 3),
    _NwtThreshold_Type()
)
nwtThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtThreshold.setStatus("mandatory")
_NwtInterval_Type = Seconds
_NwtInterval_Object = MibScalar
nwtInterval = _NwtInterval_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 4),
    _NwtInterval_Type()
)
nwtInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtInterval.setStatus("mandatory")


class _NwtInterfaceName_Type(InternationalDisplayString):
    """Custom type nwtInterfaceName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwtInterfaceName_Type.__name__ = "InternationalDisplayString"
_NwtInterfaceName_Object = MibScalar
nwtInterfaceName = _NwtInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 5),
    _NwtInterfaceName_Type()
)
nwtInterfaceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtInterfaceName.setStatus("mandatory")
_NwtQueueName_Type = InternationalDisplayString
_NwtQueueName_Object = MibScalar
nwtQueueName = _NwtQueueName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 6),
    _NwtQueueName_Type()
)
nwtQueueName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtQueueName.setStatus("mandatory")


class _NwtVolumeName_Type(InternationalDisplayString):
    """Custom type nwtVolumeName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwtVolumeName_Type.__name__ = "InternationalDisplayString"
_NwtVolumeName_Object = MibScalar
nwtVolumeName = _NwtVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 7),
    _NwtVolumeName_Type()
)
nwtVolumeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtVolumeName.setStatus("mandatory")


class _NwtDiskName_Type(InternationalDisplayString):
    """Custom type nwtDiskName based on InternationalDisplayString"""
    subtypeSpec = InternationalDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_NwtDiskName_Type.__name__ = "InternationalDisplayString"
_NwtDiskName_Object = MibScalar
nwtDiskName = _NwtDiskName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 8),
    _NwtDiskName_Type()
)
nwtDiskName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtDiskName.setStatus("mandatory")
_NwtCPUDescription_Type = InternationalDisplayString
_NwtCPUDescription_Object = MibScalar
nwtCPUDescription = _NwtCPUDescription_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 2, 9),
    _NwtCPUDescription_Type()
)
nwtCPUDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nwtCPUDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects

nwtThresholdLoggedInUsers = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 1)
)
nwtThresholdLoggedInUsers.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdLoggedInUsers.setStatus(
        ""
    )

nwtThresholdConnections = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 2)
)
nwtThresholdConnections.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdConnections.setStatus(
        ""
    )

nwtThresholdFileReads = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 3)
)
nwtThresholdFileReads.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdFileReads.setStatus(
        ""
    )

nwtThresholdFileWrites = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 4)
)
nwtThresholdFileWrites.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdFileWrites.setStatus(
        ""
    )

nwtThresholdFileReadKBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 5)
)
nwtThresholdFileReadKBytes.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdFileReadKBytes.setStatus(
        ""
    )

nwtThresholdFileWriteKBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 6)
)
nwtThresholdFileWriteKBytes.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdFileWriteKBytes.setStatus(
        ""
    )

nwtThresholdLslInPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 7)
)
nwtThresholdLslInPackets.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdLslInPackets.setStatus(
        ""
    )

nwtThresholdLslOutPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 8)
)
nwtThresholdLslOutPackets.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdLslOutPackets.setStatus(
        ""
    )

nwtThresholdNcpRequests = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 9)
)
nwtThresholdNcpRequests.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdNcpRequests.setStatus(
        ""
    )

nwtThresholdPctCpuUtilization = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 10)
)
nwtThresholdPctCpuUtilization.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtCPUDescription"))
)
if mibBuilder.loadTexts:
    nwtThresholdPctCpuUtilization.setStatus(
        ""
    )

nwtThresholdPctCacheBuffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 11)
)
nwtThresholdPctCacheBuffers.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"))
)
if mibBuilder.loadTexts:
    nwtThresholdPctCacheBuffers.setStatus(
        ""
    )

nwtThresholdCodeAndDataMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 12)
)
nwtThresholdCodeAndDataMemory.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"))
)
if mibBuilder.loadTexts:
    nwtThresholdCodeAndDataMemory.setStatus(
        ""
    )

nwtThresholdAllocatedMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 13)
)
nwtThresholdAllocatedMemory.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"))
)
if mibBuilder.loadTexts:
    nwtThresholdAllocatedMemory.setStatus(
        ""
    )

nwtThresholdPctDirtyCacheBuffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 14)
)
nwtThresholdPctDirtyCacheBuffers.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdPctDirtyCacheBuffers.setStatus(
        ""
    )

nwtThresholdPhysIfInPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 15)
)
nwtThresholdPhysIfInPackets.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdPhysIfInPackets.setStatus(
        ""
    )

nwtThresholdPhysIfOutPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 16)
)
nwtThresholdPhysIfOutPackets.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdPhysIfOutPackets.setStatus(
        ""
    )

nwtThresholdPhysIfInKBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 17)
)
nwtThresholdPhysIfInKBytes.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdPhysIfInKBytes.setStatus(
        ""
    )

nwtThresholdPhysIfOutKBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 18)
)
nwtThresholdPhysIfOutKBytes.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdPhysIfOutKBytes.setStatus(
        ""
    )

nwtThresholdQueueNumReadyJobs = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 19)
)
nwtThresholdQueueNumReadyJobs.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtQueueName"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdQueueNumReadyJobs.setStatus(
        ""
    )

nwtThresholdQueueNumReadyKBytes = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 20)
)
nwtThresholdQueueNumReadyKBytes.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtQueueName"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdQueueNumReadyKBytes.setStatus(
        ""
    )

nwtThresholdQueueNextJobWaitTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 21)
)
nwtThresholdQueueNextJobWaitTime.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtQueueName"))
)
if mibBuilder.loadTexts:
    nwtThresholdQueueNextJobWaitTime.setStatus(
        ""
    )

nwtThresholdVolumePctFreeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 22)
)
nwtThresholdVolumePctFreeSpace.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtVolumeName"))
)
if mibBuilder.loadTexts:
    nwtThresholdVolumePctFreeSpace.setStatus(
        ""
    )

nwtThresholdPctCacheHitRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 23)
)
nwtThresholdPctCacheHitRate.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"))
)
if mibBuilder.loadTexts:
    nwtThresholdPctCacheHitRate.setStatus(
        ""
    )

nwtThresholdDiskPctFreeRedirectionArea = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 24)
)
nwtThresholdDiskPctFreeRedirectionArea.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtDiskName"))
)
if mibBuilder.loadTexts:
    nwtThresholdDiskPctFreeRedirectionArea.setStatus(
        ""
    )

nwtThresholdServerProcesses = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 25)
)
nwtThresholdServerProcesses.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"))
)
if mibBuilder.loadTexts:
    nwtThresholdServerProcesses.setStatus(
        ""
    )

nwtThresholdNoECBCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 26)
)
nwtThresholdNoECBCount.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdNoECBCount.setStatus(
        ""
    )

nwtThresholdOsPktRcvBuffer = NotificationType(
    (1, 3, 6, 1, 4, 1, 23, 2, 26, 0, 27)
)
nwtThresholdOsPktRcvBuffer.setObjects(
      *(("NetWare-Server-Trend-MIB", "nwtServerName"),
        ("NetWare-Server-Trend-MIB", "nwtTrapTime"),
        ("NetWare-Server-Trend-MIB", "nwtThreshold"),
        ("NetWare-Server-Trend-MIB", "nwtInterval"),
        ("NetWare-Server-Trend-MIB", "nwtInterfaceName"))
)
if mibBuilder.loadTexts:
    nwtThresholdOsPktRcvBuffer.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NetWare-Server-Trend-MIB",
    **{"NWTime": NWTime,
       "Seconds": Seconds,
       "novell": novell,
       "mibDoc": mibDoc,
       "nwTrend": nwTrend,
       "nwtThresholdLoggedInUsers": nwtThresholdLoggedInUsers,
       "nwtThresholdConnections": nwtThresholdConnections,
       "nwtThresholdFileReads": nwtThresholdFileReads,
       "nwtThresholdFileWrites": nwtThresholdFileWrites,
       "nwtThresholdFileReadKBytes": nwtThresholdFileReadKBytes,
       "nwtThresholdFileWriteKBytes": nwtThresholdFileWriteKBytes,
       "nwtThresholdLslInPackets": nwtThresholdLslInPackets,
       "nwtThresholdLslOutPackets": nwtThresholdLslOutPackets,
       "nwtThresholdNcpRequests": nwtThresholdNcpRequests,
       "nwtThresholdPctCpuUtilization": nwtThresholdPctCpuUtilization,
       "nwtThresholdPctCacheBuffers": nwtThresholdPctCacheBuffers,
       "nwtThresholdCodeAndDataMemory": nwtThresholdCodeAndDataMemory,
       "nwtThresholdAllocatedMemory": nwtThresholdAllocatedMemory,
       "nwtThresholdPctDirtyCacheBuffers": nwtThresholdPctDirtyCacheBuffers,
       "nwtThresholdPhysIfInPackets": nwtThresholdPhysIfInPackets,
       "nwtThresholdPhysIfOutPackets": nwtThresholdPhysIfOutPackets,
       "nwtThresholdPhysIfInKBytes": nwtThresholdPhysIfInKBytes,
       "nwtThresholdPhysIfOutKBytes": nwtThresholdPhysIfOutKBytes,
       "nwtThresholdQueueNumReadyJobs": nwtThresholdQueueNumReadyJobs,
       "nwtThresholdQueueNumReadyKBytes": nwtThresholdQueueNumReadyKBytes,
       "nwtThresholdQueueNextJobWaitTime": nwtThresholdQueueNextJobWaitTime,
       "nwtThresholdVolumePctFreeSpace": nwtThresholdVolumePctFreeSpace,
       "nwtThresholdPctCacheHitRate": nwtThresholdPctCacheHitRate,
       "nwtThresholdDiskPctFreeRedirectionArea": nwtThresholdDiskPctFreeRedirectionArea,
       "nwtThresholdServerProcesses": nwtThresholdServerProcesses,
       "nwtThresholdNoECBCount": nwtThresholdNoECBCount,
       "nwtThresholdOsPktRcvBuffer": nwtThresholdOsPktRcvBuffer,
       "nwtControl": nwtControl,
       "nwtControlTable": nwtControlTable,
       "nwtControlEntry": nwtControlEntry,
       "nwtControlAttributeClass": nwtControlAttributeClass,
       "nwtControlIndex": nwtControlIndex,
       "nwtControlAttributeInstance": nwtControlAttributeInstance,
       "nwtControlSampleInterval": nwtControlSampleInterval,
       "nwtControlSampleType": nwtControlSampleType,
       "nwtControlSampleInvalidValue": nwtControlSampleInvalidValue,
       "nwtControlLastSampleValue": nwtControlLastSampleValue,
       "nwtControlReferenceTimeStamp": nwtControlReferenceTimeStamp,
       "nwtControlThresholdState": nwtControlThresholdState,
       "nwtControlThresholdType": nwtControlThresholdType,
       "nwtControlRisingThreshold": nwtControlRisingThreshold,
       "nwtControlFallingThreshold": nwtControlFallingThreshold,
       "nwtControlHistoryState": nwtControlHistoryState,
       "nwtControlHistoryLastSampleIndex": nwtControlHistoryLastSampleIndex,
       "nwtControlHistoryBucketsRequested": nwtControlHistoryBucketsRequested,
       "nwtControlHistoryBucketsGranted": nwtControlHistoryBucketsGranted,
       "nwtControlStatus": nwtControlStatus,
       "nwtHistoryTable": nwtHistoryTable,
       "nwtHistoryEntry": nwtHistoryEntry,
       "nwtHistoryControlIndex": nwtHistoryControlIndex,
       "nwtHistorySampleIndex": nwtHistorySampleIndex,
       "nwtHistorySampleValue": nwtHistorySampleValue,
       "nwtTrapInfo": nwtTrapInfo,
       "nwtServerName": nwtServerName,
       "nwtTrapTime": nwtTrapTime,
       "nwtThreshold": nwtThreshold,
       "nwtInterval": nwtInterval,
       "nwtInterfaceName": nwtInterfaceName,
       "nwtQueueName": nwtQueueName,
       "nwtVolumeName": nwtVolumeName,
       "nwtDiskName": nwtDiskName,
       "nwtCPUDescription": nwtCPUDescription}
)
