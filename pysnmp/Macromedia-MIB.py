# SNMP MIB module (Macromedia-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Macromedia-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:34 2024
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

_Allaire_ObjectIdentity = ObjectIdentity
allaire = _Allaire_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1)
)
_Coldfusion_ObjectIdentity = ObjectIdentity
coldfusion = _Coldfusion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1)
)


class _CfOSName_Type(DisplayString):
    """Custom type cfOSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfOSName_Type.__name__ = "DisplayString"
_CfOSName_Object = MibScalar
cfOSName = _CfOSName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 1),
    _CfOSName_Type()
)
cfOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfOSName.setStatus("mandatory")


class _CfOSVersion_Type(DisplayString):
    """Custom type cfOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfOSVersion_Type.__name__ = "DisplayString"
_CfOSVersion_Object = MibScalar
cfOSVersion = _CfOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 2),
    _CfOSVersion_Type()
)
cfOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfOSVersion.setStatus("mandatory")


class _CfOSBuildNumber_Type(DisplayString):
    """Custom type cfOSBuildNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfOSBuildNumber_Type.__name__ = "DisplayString"
_CfOSBuildNumber_Object = MibScalar
cfOSBuildNumber = _CfOSBuildNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 3),
    _CfOSBuildNumber_Type()
)
cfOSBuildNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfOSBuildNumber.setStatus("mandatory")


class _CfOSAdditionalInfo_Type(DisplayString):
    """Custom type cfOSAdditionalInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfOSAdditionalInfo_Type.__name__ = "DisplayString"
_CfOSAdditionalInfo_Object = MibScalar
cfOSAdditionalInfo = _CfOSAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 4),
    _CfOSAdditionalInfo_Type()
)
cfOSAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfOSAdditionalInfo.setStatus("mandatory")


class _CfProductName_Type(DisplayString):
    """Custom type cfProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfProductName_Type.__name__ = "DisplayString"
_CfProductName_Object = MibScalar
cfProductName = _CfProductName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 5),
    _CfProductName_Type()
)
cfProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfProductName.setStatus("mandatory")


class _CfProductLevel_Type(DisplayString):
    """Custom type cfProductLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfProductLevel_Type.__name__ = "DisplayString"
_CfProductLevel_Object = MibScalar
cfProductLevel = _CfProductLevel_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 6),
    _CfProductLevel_Type()
)
cfProductLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfProductLevel.setStatus("mandatory")


class _CfProductVersion_Type(DisplayString):
    """Custom type cfProductVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfProductVersion_Type.__name__ = "DisplayString"
_CfProductVersion_Object = MibScalar
cfProductVersion = _CfProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 7),
    _CfProductVersion_Type()
)
cfProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfProductVersion.setStatus("mandatory")


class _CfPerformanceMonitorOn_Type(Integer32):
    """Custom type cfPerformanceMonitorOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfPerformanceMonitorOn_Type.__name__ = "Integer32"
_CfPerformanceMonitorOn_Object = MibScalar
cfPerformanceMonitorOn = _CfPerformanceMonitorOn_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 8),
    _CfPerformanceMonitorOn_Type()
)
cfPerformanceMonitorOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPerformanceMonitorOn.setStatus("mandatory")
_CfPageHits_Type = Integer32
_CfPageHits_Object = MibScalar
cfPageHits = _CfPageHits_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 9),
    _CfPageHits_Type()
)
cfPageHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfPageHits.setStatus("mandatory")
_CfRequestsQueued_Type = Integer32
_CfRequestsQueued_Object = MibScalar
cfRequestsQueued = _CfRequestsQueued_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 10),
    _CfRequestsQueued_Type()
)
cfRequestsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfRequestsQueued.setStatus("mandatory")
_CfDatabaseHits_Type = Integer32
_CfDatabaseHits_Object = MibScalar
cfDatabaseHits = _CfDatabaseHits_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 11),
    _CfDatabaseHits_Type()
)
cfDatabaseHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfDatabaseHits.setStatus("mandatory")
_CfRequestsRunning_Type = Integer32
_CfRequestsRunning_Object = MibScalar
cfRequestsRunning = _CfRequestsRunning_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 12),
    _CfRequestsRunning_Type()
)
cfRequestsRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfRequestsRunning.setStatus("mandatory")
_CfReqestsTimedOut_Type = Integer32
_CfReqestsTimedOut_Object = MibScalar
cfReqestsTimedOut = _CfReqestsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 13),
    _CfReqestsTimedOut_Type()
)
cfReqestsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfReqestsTimedOut.setStatus("mandatory")
_CfBytesIn_Type = Integer32
_CfBytesIn_Object = MibScalar
cfBytesIn = _CfBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 14),
    _CfBytesIn_Type()
)
cfBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfBytesIn.setStatus("mandatory")
_CfBytesOut_Type = Integer32
_CfBytesOut_Object = MibScalar
cfBytesOut = _CfBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 15),
    _CfBytesOut_Type()
)
cfBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfBytesOut.setStatus("mandatory")
_CfAvgQueueTimes_Type = Integer32
_CfAvgQueueTimes_Object = MibScalar
cfAvgQueueTimes = _CfAvgQueueTimes_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 16),
    _CfAvgQueueTimes_Type()
)
cfAvgQueueTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAvgQueueTimes.setStatus("mandatory")
_CfAvgRequestTime_Type = Integer32
_CfAvgRequestTime_Object = MibScalar
cfAvgRequestTime = _CfAvgRequestTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 17),
    _CfAvgRequestTime_Type()
)
cfAvgRequestTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAvgRequestTime.setStatus("mandatory")
_CfAvgDBTime_Type = Integer32
_CfAvgDBTime_Object = MibScalar
cfAvgDBTime = _CfAvgDBTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 18),
    _CfAvgDBTime_Type()
)
cfAvgDBTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfAvgDBTime.setStatus("mandatory")
_CfCachePops_Type = Integer32
_CfCachePops_Object = MibScalar
cfCachePops = _CfCachePops_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 19),
    _CfCachePops_Type()
)
cfCachePops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfCachePops.setStatus("mandatory")
_CfMaxRequests_Type = Integer32
_CfMaxRequests_Object = MibScalar
cfMaxRequests = _CfMaxRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 20),
    _CfMaxRequests_Type()
)
cfMaxRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMaxRequests.setStatus("mandatory")


class _CfLimitTime_Type(Integer32):
    """Custom type cfLimitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfLimitTime_Type.__name__ = "Integer32"
_CfLimitTime_Object = MibScalar
cfLimitTime = _CfLimitTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 21),
    _CfLimitTime_Type()
)
cfLimitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfLimitTime.setStatus("mandatory")
_CfMaxSeconds_Type = Integer32
_CfMaxSeconds_Object = MibScalar
cfMaxSeconds = _CfMaxSeconds_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 22),
    _CfMaxSeconds_Type()
)
cfMaxSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMaxSeconds.setStatus("mandatory")


class _CfTrustCache_Type(Integer32):
    """Custom type cfTrustCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfTrustCache_Type.__name__ = "Integer32"
_CfTrustCache_Object = MibScalar
cfTrustCache = _CfTrustCache_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 23),
    _CfTrustCache_Type()
)
cfTrustCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTrustCache.setStatus("mandatory")
_CfTemplateCacheSize_Type = Integer32
_CfTemplateCacheSize_Object = MibScalar
cfTemplateCacheSize = _CfTemplateCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 24),
    _CfTemplateCacheSize_Type()
)
cfTemplateCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfTemplateCacheSize.setStatus("mandatory")


class _CfRunningRDS_Type(Integer32):
    """Custom type cfRunningRDS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfRunningRDS_Type.__name__ = "Integer32"
_CfRunningRDS_Object = MibScalar
cfRunningRDS = _CfRunningRDS_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 25),
    _CfRunningRDS_Type()
)
cfRunningRDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfRunningRDS.setStatus("mandatory")


class _CfDebuggingOn_Type(Integer32):
    """Custom type cfDebuggingOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfDebuggingOn_Type.__name__ = "Integer32"
_CfDebuggingOn_Object = MibScalar
cfDebuggingOn = _CfDebuggingOn_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 26),
    _CfDebuggingOn_Type()
)
cfDebuggingOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfDebuggingOn.setStatus("mandatory")


class _CfEnforceStrictAttributeValidation_Type(Integer32):
    """Custom type cfEnforceStrictAttributeValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_CfEnforceStrictAttributeValidation_Type.__name__ = "Integer32"
_CfEnforceStrictAttributeValidation_Object = MibScalar
cfEnforceStrictAttributeValidation = _CfEnforceStrictAttributeValidation_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 27),
    _CfEnforceStrictAttributeValidation_Type()
)
cfEnforceStrictAttributeValidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfEnforceStrictAttributeValidation.setStatus("mandatory")
_CfRestartThreshold_Type = Integer32
_CfRestartThreshold_Object = MibScalar
cfRestartThreshold = _CfRestartThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 28),
    _CfRestartThreshold_Type()
)
cfRestartThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfRestartThreshold.setStatus("mandatory")
_CfMaxCachedQueries_Type = Integer32
_CfMaxCachedQueries_Object = MibScalar
cfMaxCachedQueries = _CfMaxCachedQueries_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 29),
    _CfMaxCachedQueries_Type()
)
cfMaxCachedQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMaxCachedQueries.setStatus("mandatory")


class _CfMailServerName_Type(DisplayString):
    """Custom type cfMailServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CfMailServerName_Type.__name__ = "DisplayString"
_CfMailServerName_Object = MibScalar
cfMailServerName = _CfMailServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 30),
    _CfMailServerName_Type()
)
cfMailServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMailServerName.setStatus("mandatory")
_CfMailServerPortNumber_Type = Integer32
_CfMailServerPortNumber_Object = MibScalar
cfMailServerPortNumber = _CfMailServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 31),
    _CfMailServerPortNumber_Type()
)
cfMailServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMailServerPortNumber.setStatus("mandatory")
_CfMailServerConnectTimeout_Type = Integer32
_CfMailServerConnectTimeout_Object = MibScalar
cfMailServerConnectTimeout = _CfMailServerConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 1, 32),
    _CfMailServerConnectTimeout_Type()
)
cfMailServerConnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfMailServerConnectTimeout.setStatus("mandatory")
_Jrun_ObjectIdentity = ObjectIdentity
jrun = _Jrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2)
)


class _JOSName_Type(DisplayString):
    """Custom type jOSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JOSName_Type.__name__ = "DisplayString"
_JOSName_Object = MibScalar
jOSName = _JOSName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 1),
    _JOSName_Type()
)
jOSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jOSName.setStatus("mandatory")


class _JOSVersion_Type(DisplayString):
    """Custom type jOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JOSVersion_Type.__name__ = "DisplayString"
_JOSVersion_Object = MibScalar
jOSVersion = _JOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 2),
    _JOSVersion_Type()
)
jOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jOSVersion.setStatus("mandatory")


class _JMachineArchitecture_Type(DisplayString):
    """Custom type jMachineArchitecture based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JMachineArchitecture_Type.__name__ = "DisplayString"
_JMachineArchitecture_Object = MibScalar
jMachineArchitecture = _JMachineArchitecture_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 3),
    _JMachineArchitecture_Type()
)
jMachineArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jMachineArchitecture.setStatus("mandatory")


class _JJDKVendor_Type(DisplayString):
    """Custom type jJDKVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JJDKVendor_Type.__name__ = "DisplayString"
_JJDKVendor_Object = MibScalar
jJDKVendor = _JJDKVendor_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 4),
    _JJDKVendor_Type()
)
jJDKVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJDKVendor.setStatus("mandatory")


class _JJDKVersion_Type(DisplayString):
    """Custom type jJDKVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JJDKVersion_Type.__name__ = "DisplayString"
_JJDKVersion_Object = MibScalar
jJDKVersion = _JJDKVersion_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 5),
    _JJDKVersion_Type()
)
jJDKVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJDKVersion.setStatus("mandatory")


class _JJRunVersion_Type(DisplayString):
    """Custom type jJRunVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JJRunVersion_Type.__name__ = "DisplayString"
_JJRunVersion_Object = MibScalar
jJRunVersion = _JJRunVersion_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 6),
    _JJRunVersion_Type()
)
jJRunVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJRunVersion.setStatus("mandatory")
_JFreeMomory_Type = Integer32
_JFreeMomory_Object = MibScalar
jFreeMomory = _JFreeMomory_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 7),
    _JFreeMomory_Type()
)
jFreeMomory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jFreeMomory.setStatus("mandatory")
_JTotalMomory_Type = Integer32
_JTotalMomory_Object = MibScalar
jTotalMomory = _JTotalMomory_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 8),
    _JTotalMomory_Type()
)
jTotalMomory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jTotalMomory.setStatus("mandatory")
_JSessions_Type = Integer32
_JSessions_Object = MibScalar
jSessions = _JSessions_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 9),
    _JSessions_Type()
)
jSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jSessions.setStatus("mandatory")
_JSessionsInMemory_Type = Integer32
_JSessionsInMemory_Object = MibScalar
jSessionsInMemory = _JSessionsInMemory_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 10),
    _JSessionsInMemory_Type()
)
jSessionsInMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jSessionsInMemory.setStatus("mandatory")
_JJcpBytesIn_Type = Integer32
_JJcpBytesIn_Object = MibScalar
jJcpBytesIn = _JJcpBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 11),
    _JJcpBytesIn_Type()
)
jJcpBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpBytesIn.setStatus("mandatory")
_JJcpBytesOut_Type = Integer32
_JJcpBytesOut_Object = MibScalar
jJcpBytesOut = _JJcpBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 12),
    _JJcpBytesOut_Type()
)
jJcpBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpBytesOut.setStatus("mandatory")
_JJcpHandledRequests_Type = Integer32
_JJcpHandledRequests_Object = MibScalar
jJcpHandledRequests = _JJcpHandledRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 13),
    _JJcpHandledRequests_Type()
)
jJcpHandledRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpHandledRequests.setStatus("mandatory")
_JJcpDelayRequests_Type = Integer32
_JJcpDelayRequests_Object = MibScalar
jJcpDelayRequests = _JJcpDelayRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 14),
    _JJcpDelayRequests_Type()
)
jJcpDelayRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpDelayRequests.setStatus("mandatory")
_JJcpDroppedRequests_Type = Integer32
_JJcpDroppedRequests_Object = MibScalar
jJcpDroppedRequests = _JJcpDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 15),
    _JJcpDroppedRequests_Type()
)
jJcpDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpDroppedRequests.setStatus("mandatory")
_JJcpHandledMs_Type = Integer32
_JJcpHandledMs_Object = MibScalar
jJcpHandledMs = _JJcpHandledMs_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 16),
    _JJcpHandledMs_Type()
)
jJcpHandledMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpHandledMs.setStatus("mandatory")
_JJcpDelayMs_Type = Integer32
_JJcpDelayMs_Object = MibScalar
jJcpDelayMs = _JJcpDelayMs_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 17),
    _JJcpDelayMs_Type()
)
jJcpDelayMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpDelayMs.setStatus("mandatory")
_JJcpTotalThreads_Type = Integer32
_JJcpTotalThreads_Object = MibScalar
jJcpTotalThreads = _JJcpTotalThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 18),
    _JJcpTotalThreads_Type()
)
jJcpTotalThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpTotalThreads.setStatus("mandatory")
_JJcpListenThreads_Type = Integer32
_JJcpListenThreads_Object = MibScalar
jJcpListenThreads = _JJcpListenThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 19),
    _JJcpListenThreads_Type()
)
jJcpListenThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpListenThreads.setStatus("mandatory")
_JJcpBusyThreads_Type = Integer32
_JJcpBusyThreads_Object = MibScalar
jJcpBusyThreads = _JJcpBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 20),
    _JJcpBusyThreads_Type()
)
jJcpBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpBusyThreads.setStatus("mandatory")
_JJcpDelayThreads_Type = Integer32
_JJcpDelayThreads_Object = MibScalar
jJcpDelayThreads = _JJcpDelayThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 21),
    _JJcpDelayThreads_Type()
)
jJcpDelayThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpDelayThreads.setStatus("mandatory")
_JJcpIdleThreads_Type = Integer32
_JJcpIdleThreads_Object = MibScalar
jJcpIdleThreads = _JJcpIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 22),
    _JJcpIdleThreads_Type()
)
jJcpIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jJcpIdleThreads.setStatus("mandatory")
_JWebBytesIn_Type = Integer32
_JWebBytesIn_Object = MibScalar
jWebBytesIn = _JWebBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 23),
    _JWebBytesIn_Type()
)
jWebBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebBytesIn.setStatus("mandatory")
_JWebBytesOut_Type = Integer32
_JWebBytesOut_Object = MibScalar
jWebBytesOut = _JWebBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 24),
    _JWebBytesOut_Type()
)
jWebBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebBytesOut.setStatus("mandatory")
_JWebHandledRequests_Type = Integer32
_JWebHandledRequests_Object = MibScalar
jWebHandledRequests = _JWebHandledRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 25),
    _JWebHandledRequests_Type()
)
jWebHandledRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebHandledRequests.setStatus("mandatory")
_JWebDelayRequests_Type = Integer32
_JWebDelayRequests_Object = MibScalar
jWebDelayRequests = _JWebDelayRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 26),
    _JWebDelayRequests_Type()
)
jWebDelayRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebDelayRequests.setStatus("mandatory")
_JWebDroppedRequests_Type = Integer32
_JWebDroppedRequests_Object = MibScalar
jWebDroppedRequests = _JWebDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 27),
    _JWebDroppedRequests_Type()
)
jWebDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebDroppedRequests.setStatus("mandatory")
_JWebHandledMs_Type = Integer32
_JWebHandledMs_Object = MibScalar
jWebHandledMs = _JWebHandledMs_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 28),
    _JWebHandledMs_Type()
)
jWebHandledMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebHandledMs.setStatus("mandatory")
_JWebDelayMs_Type = Integer32
_JWebDelayMs_Object = MibScalar
jWebDelayMs = _JWebDelayMs_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 29),
    _JWebDelayMs_Type()
)
jWebDelayMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebDelayMs.setStatus("mandatory")
_JWebTotalThreads_Type = Integer32
_JWebTotalThreads_Object = MibScalar
jWebTotalThreads = _JWebTotalThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 30),
    _JWebTotalThreads_Type()
)
jWebTotalThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebTotalThreads.setStatus("mandatory")
_JWebListenThreads_Type = Integer32
_JWebListenThreads_Object = MibScalar
jWebListenThreads = _JWebListenThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 31),
    _JWebListenThreads_Type()
)
jWebListenThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebListenThreads.setStatus("mandatory")
_JWebBusyThreads_Type = Integer32
_JWebBusyThreads_Object = MibScalar
jWebBusyThreads = _JWebBusyThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 32),
    _JWebBusyThreads_Type()
)
jWebBusyThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebBusyThreads.setStatus("mandatory")
_JWebDelayThreads_Type = Integer32
_JWebDelayThreads_Object = MibScalar
jWebDelayThreads = _JWebDelayThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 33),
    _JWebDelayThreads_Type()
)
jWebDelayThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebDelayThreads.setStatus("mandatory")
_JWebIdleThreads_Type = Integer32
_JWebIdleThreads_Object = MibScalar
jWebIdleThreads = _JWebIdleThreads_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 2, 34),
    _JWebIdleThreads_Type()
)
jWebIdleThreads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jWebIdleThreads.setStatus("mandatory")
_JrunServers_ObjectIdentity = ObjectIdentity
jrunServers = _JrunServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3)
)
_JrunServerTable_Object = MibTable
jrunServerTable = _JrunServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jrunServerTable.setStatus("mandatory")
_JrunServerEntry_Object = MibTableRow
jrunServerEntry = _JrunServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1)
)
jrunServerEntry.setIndexNames(
    (0, "Macromedia-MIB", "jrunServerOrdinal"),
)
if mibBuilder.loadTexts:
    jrunServerEntry.setStatus("mandatory")
_JrunServerOrdinal_Type = Integer32
_JrunServerOrdinal_Object = MibTableColumn
jrunServerOrdinal = _JrunServerOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 1),
    _JrunServerOrdinal_Type()
)
jrunServerOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jrunServerOrdinal.setStatus("mandatory")


class _JrunServerName_Type(DisplayString):
    """Custom type jrunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JrunServerName_Type.__name__ = "DisplayString"
_JrunServerName_Object = MibTableColumn
jrunServerName = _JrunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 2),
    _JrunServerName_Type()
)
jrunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jrunServerName.setStatus("mandatory")


class _JrunServerState_Type(Integer32):
    """Custom type jrunServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 0))
    )


_JrunServerState_Type.__name__ = "Integer32"
_JrunServerState_Object = MibTableColumn
jrunServerState = _JrunServerState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 3, 1, 1, 3),
    _JrunServerState_Type()
)
jrunServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jrunServerState.setStatus("mandatory")
_JrunJDBCs_ObjectIdentity = ObjectIdentity
jrunJDBCs = _JrunJDBCs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4)
)
_JrunJDBCTable_Object = MibTable
jrunJDBCTable = _JrunJDBCTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jrunJDBCTable.setStatus("mandatory")
_JrunJDBCEntry_Object = MibTableRow
jrunJDBCEntry = _JrunJDBCEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1)
)
jrunJDBCEntry.setIndexNames(
    (0, "Macromedia-MIB", "jdbcOrdinal"),
)
if mibBuilder.loadTexts:
    jrunJDBCEntry.setStatus("mandatory")
_JdbcOrdinal_Type = Integer32
_JdbcOrdinal_Object = MibTableColumn
jdbcOrdinal = _JdbcOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 1),
    _JdbcOrdinal_Type()
)
jdbcOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdbcOrdinal.setStatus("mandatory")


class _JdbcJRunServerName_Type(DisplayString):
    """Custom type jdbcJRunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JdbcJRunServerName_Type.__name__ = "DisplayString"
_JdbcJRunServerName_Object = MibTableColumn
jdbcJRunServerName = _JdbcJRunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 2),
    _JdbcJRunServerName_Type()
)
jdbcJRunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdbcJRunServerName.setStatus("mandatory")


class _JdbcName_Type(DisplayString):
    """Custom type jdbcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JdbcName_Type.__name__ = "DisplayString"
_JdbcName_Object = MibTableColumn
jdbcName = _JdbcName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 3),
    _JdbcName_Type()
)
jdbcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdbcName.setStatus("mandatory")


class _JdbcState_Type(Integer32):
    """Custom type jdbcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 0))
    )


_JdbcState_Type.__name__ = "Integer32"
_JdbcState_Object = MibTableColumn
jdbcState = _JdbcState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 4, 1, 1, 4),
    _JdbcState_Type()
)
jdbcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jdbcState.setStatus("mandatory")
_JrunWebApps_ObjectIdentity = ObjectIdentity
jrunWebApps = _JrunWebApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5)
)
_JrunWebAppTable_Object = MibTable
jrunWebAppTable = _JrunWebAppTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jrunWebAppTable.setStatus("mandatory")
_JrunWebAppEntry_Object = MibTableRow
jrunWebAppEntry = _JrunWebAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1)
)
jrunWebAppEntry.setIndexNames(
    (0, "Macromedia-MIB", "webAppOrdinal"),
)
if mibBuilder.loadTexts:
    jrunWebAppEntry.setStatus("mandatory")
_WebAppOrdinal_Type = Integer32
_WebAppOrdinal_Object = MibTableColumn
webAppOrdinal = _WebAppOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 1),
    _WebAppOrdinal_Type()
)
webAppOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAppOrdinal.setStatus("mandatory")


class _WebAppJRunServerName_Type(DisplayString):
    """Custom type webAppJRunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WebAppJRunServerName_Type.__name__ = "DisplayString"
_WebAppJRunServerName_Object = MibTableColumn
webAppJRunServerName = _WebAppJRunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 2),
    _WebAppJRunServerName_Type()
)
webAppJRunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAppJRunServerName.setStatus("mandatory")


class _WebAppName_Type(DisplayString):
    """Custom type webAppName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_WebAppName_Type.__name__ = "DisplayString"
_WebAppName_Object = MibTableColumn
webAppName = _WebAppName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 5, 1, 1, 3),
    _WebAppName_Type()
)
webAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAppName.setStatus("mandatory")
_JrunEJBs_ObjectIdentity = ObjectIdentity
jrunEJBs = _JrunEJBs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6)
)
_JrunEjbTable_Object = MibTable
jrunEjbTable = _JrunEjbTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6, 1)
)
if mibBuilder.loadTexts:
    jrunEjbTable.setStatus("mandatory")
_JrunEjbEntry_Object = MibTableRow
jrunEjbEntry = _JrunEjbEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1)
)
jrunEjbEntry.setIndexNames(
    (0, "Macromedia-MIB", "ejbOrdinal"),
)
if mibBuilder.loadTexts:
    jrunEjbEntry.setStatus("mandatory")
_EjbOrdinal_Type = Integer32
_EjbOrdinal_Object = MibTableColumn
ejbOrdinal = _EjbOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 1),
    _EjbOrdinal_Type()
)
ejbOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ejbOrdinal.setStatus("mandatory")


class _EjbJRunServerName_Type(DisplayString):
    """Custom type ejbJRunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EjbJRunServerName_Type.__name__ = "DisplayString"
_EjbJRunServerName_Object = MibTableColumn
ejbJRunServerName = _EjbJRunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 2),
    _EjbJRunServerName_Type()
)
ejbJRunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ejbJRunServerName.setStatus("mandatory")


class _EjbName_Type(DisplayString):
    """Custom type ejbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EjbName_Type.__name__ = "DisplayString"
_EjbName_Object = MibTableColumn
ejbName = _EjbName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 6, 1, 1, 3),
    _EjbName_Type()
)
ejbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ejbName.setStatus("mandatory")
_Probes_ObjectIdentity = ObjectIdentity
probes = _Probes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7)
)
_ProbeTable_Object = MibTable
probeTable = _ProbeTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7, 1)
)
if mibBuilder.loadTexts:
    probeTable.setStatus("mandatory")
_ProbeEntry_Object = MibTableRow
probeEntry = _ProbeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1)
)
probeEntry.setIndexNames(
    (0, "Macromedia-MIB", "probeOrdinalNumber"),
)
if mibBuilder.loadTexts:
    probeEntry.setStatus("mandatory")
_ProbeOrdinalNumber_Type = Integer32
_ProbeOrdinalNumber_Object = MibTableColumn
probeOrdinalNumber = _ProbeOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 1),
    _ProbeOrdinalNumber_Type()
)
probeOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeOrdinalNumber.setStatus("mandatory")


class _ProbeName_Type(DisplayString):
    """Custom type probeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ProbeName_Type.__name__ = "DisplayString"
_ProbeName_Object = MibTableColumn
probeName = _ProbeName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 2),
    _ProbeName_Type()
)
probeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeName.setStatus("mandatory")


class _ProbeState_Type(Integer32):
    """Custom type probeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 0),
          ("suspended", 2))
    )


_ProbeState_Type.__name__ = "Integer32"
_ProbeState_Object = MibTableColumn
probeState = _ProbeState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 7, 1, 1, 3),
    _ProbeState_Type()
)
probeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    probeState.setStatus("mandatory")
_HaaManagement_ObjectIdentity = ObjectIdentity
haaManagement = _HaaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8)
)
_HaaServerTable_Object = MibTable
haaServerTable = _HaaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1)
)
if mibBuilder.loadTexts:
    haaServerTable.setStatus("mandatory")
_HserverEntry_Object = MibTableRow
hserverEntry = _HserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1)
)
hserverEntry.setIndexNames(
    (0, "Macromedia-MIB", "hServerOrdinalNumber"),
)
if mibBuilder.loadTexts:
    hserverEntry.setStatus("mandatory")
_HServerOrdinalNumber_Type = Integer32
_HServerOrdinalNumber_Object = MibTableColumn
hServerOrdinalNumber = _HServerOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 1),
    _HServerOrdinalNumber_Type()
)
hServerOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerOrdinalNumber.setStatus("mandatory")


class _HServerName_Type(DisplayString):
    """Custom type hServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HServerName_Type.__name__ = "DisplayString"
_HServerName_Object = MibTableColumn
hServerName = _HServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 2),
    _HServerName_Type()
)
hServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerName.setStatus("mandatory")


class _HServerIP_Type(DisplayString):
    """Custom type hServerIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HServerIP_Type.__name__ = "DisplayString"
_HServerIP_Object = MibTableColumn
hServerIP = _HServerIP_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 3),
    _HServerIP_Type()
)
hServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerIP.setStatus("mandatory")


class _HServerState_Type(Integer32):
    """Custom type hServerState based on Integer32"""
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
        *(("available", 0),
          ("busy", 2),
          ("restricted", 3),
          ("unavailable", 1))
    )


_HServerState_Type.__name__ = "Integer32"
_HServerState_Object = MibTableColumn
hServerState = _HServerState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 4),
    _HServerState_Type()
)
hServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerState.setStatus("mandatory")


class _HServerMode_Type(Integer32):
    """Custom type hServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_HServerMode_Type.__name__ = "Integer32"
_HServerMode_Object = MibTableColumn
hServerMode = _HServerMode_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 5),
    _HServerMode_Type()
)
hServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerMode.setStatus("mandatory")


class _HServerLoad_Type(Integer32):
    """Custom type hServerLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HServerLoad_Type.__name__ = "Integer32"
_HServerLoad_Object = MibTableColumn
hServerLoad = _HServerLoad_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 6),
    _HServerLoad_Type()
)
hServerLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerLoad.setStatus("mandatory")


class _HServerLoadBalanceProduct_Type(Integer32):
    """Custom type hServerLoadBalanceProduct based on Integer32"""
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
        *(("brightTiger", 1),
          ("ciscoLocalDirector", 2),
          ("none", 0),
          ("other", 3))
    )


_HServerLoadBalanceProduct_Type.__name__ = "Integer32"
_HServerLoadBalanceProduct_Object = MibTableColumn
hServerLoadBalanceProduct = _HServerLoadBalanceProduct_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 7),
    _HServerLoadBalanceProduct_Type()
)
hServerLoadBalanceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerLoadBalanceProduct.setStatus("mandatory")


class _HServerLoadThreshold_Type(Integer32):
    """Custom type hServerLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HServerLoadThreshold_Type.__name__ = "Integer32"
_HServerLoadThreshold_Object = MibTableColumn
hServerLoadThreshold = _HServerLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 8),
    _HServerLoadThreshold_Type()
)
hServerLoadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerLoadThreshold.setStatus("mandatory")


class _HServerLoadType_Type(Integer32):
    """Custom type hServerLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("coldFusion", 0),
          ("jrun", 1))
    )


_HServerLoadType_Type.__name__ = "Integer32"
_HServerLoadType_Object = MibTableColumn
hServerLoadType = _HServerLoadType_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 8, 1, 1, 9),
    _HServerLoadType_Type()
)
hServerLoadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hServerLoadType.setStatus("mandatory")
_ServerManagement_ObjectIdentity = ObjectIdentity
serverManagement = _ServerManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9)
)
_ServerTable_Object = MibTable
serverTable = _ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1)
)
if mibBuilder.loadTexts:
    serverTable.setStatus("mandatory")
_ServerEntry_Object = MibTableRow
serverEntry = _ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1)
)
serverEntry.setIndexNames(
    (0, "Macromedia-MIB", "serverOrdinalNumber"),
)
if mibBuilder.loadTexts:
    serverEntry.setStatus("mandatory")
_ServerOrdinalNumber_Type = Integer32
_ServerOrdinalNumber_Object = MibTableColumn
serverOrdinalNumber = _ServerOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 1),
    _ServerOrdinalNumber_Type()
)
serverOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverOrdinalNumber.setStatus("mandatory")


class _ServerName_Type(DisplayString):
    """Custom type serverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ServerName_Type.__name__ = "DisplayString"
_ServerName_Object = MibTableColumn
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 2),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("mandatory")


class _ServerIP_Type(DisplayString):
    """Custom type serverIP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ServerIP_Type.__name__ = "DisplayString"
_ServerIP_Object = MibTableColumn
serverIP = _ServerIP_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 3),
    _ServerIP_Type()
)
serverIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverIP.setStatus("mandatory")


class _ServerState_Type(Integer32):
    """Custom type serverState based on Integer32"""
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
        *(("available", 0),
          ("busy", 2),
          ("restricted", 3),
          ("unavailable", 1))
    )


_ServerState_Type.__name__ = "Integer32"
_ServerState_Object = MibTableColumn
serverState = _ServerState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 4),
    _ServerState_Type()
)
serverState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverState.setStatus("mandatory")


class _ServerMode_Type(Integer32):
    """Custom type serverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_ServerMode_Type.__name__ = "Integer32"
_ServerMode_Object = MibTableColumn
serverMode = _ServerMode_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 5),
    _ServerMode_Type()
)
serverMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverMode.setStatus("mandatory")


class _ServerLoad_Type(Integer32):
    """Custom type serverLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ServerLoad_Type.__name__ = "Integer32"
_ServerLoad_Object = MibTableColumn
serverLoad = _ServerLoad_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 6),
    _ServerLoad_Type()
)
serverLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLoad.setStatus("mandatory")


class _ServerLoadBalanceProduct_Type(Integer32):
    """Custom type serverLoadBalanceProduct based on Integer32"""
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
        *(("brightTiger", 1),
          ("ciscoLocalDirector", 2),
          ("none", 0),
          ("other", 3))
    )


_ServerLoadBalanceProduct_Type.__name__ = "Integer32"
_ServerLoadBalanceProduct_Object = MibTableColumn
serverLoadBalanceProduct = _ServerLoadBalanceProduct_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 7),
    _ServerLoadBalanceProduct_Type()
)
serverLoadBalanceProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLoadBalanceProduct.setStatus("mandatory")


class _ServerLoadThreshold_Type(Integer32):
    """Custom type serverLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ServerLoadThreshold_Type.__name__ = "Integer32"
_ServerLoadThreshold_Object = MibTableColumn
serverLoadThreshold = _ServerLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 8),
    _ServerLoadThreshold_Type()
)
serverLoadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLoadThreshold.setStatus("mandatory")


class _ServerLoadType_Type(Integer32):
    """Custom type serverLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("coldFusion", 0),
          ("jrun", 1))
    )


_ServerLoadType_Type.__name__ = "Integer32"
_ServerLoadType_Object = MibTableColumn
serverLoadType = _ServerLoadType_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 9),
    _ServerLoadType_Type()
)
serverLoadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverLoadType.setStatus("mandatory")


class _ServerCluster_Type(DisplayString):
    """Custom type serverCluster based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ServerCluster_Type.__name__ = "DisplayString"
_ServerCluster_Object = MibTableColumn
serverCluster = _ServerCluster_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 10),
    _ServerCluster_Type()
)
serverCluster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverCluster.setStatus("mandatory")


class _ServerAdminAgent_Type(DisplayString):
    """Custom type serverAdminAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ServerAdminAgent_Type.__name__ = "DisplayString"
_ServerAdminAgent_Object = MibTableColumn
serverAdminAgent = _ServerAdminAgent_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 11),
    _ServerAdminAgent_Type()
)
serverAdminAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverAdminAgent.setStatus("mandatory")


class _ServerSessionAwareness_Type(Integer32):
    """Custom type serverSessionAwareness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ServerSessionAwareness_Type.__name__ = "Integer32"
_ServerSessionAwareness_Object = MibTableColumn
serverSessionAwareness = _ServerSessionAwareness_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 12),
    _ServerSessionAwareness_Type()
)
serverSessionAwareness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverSessionAwareness.setStatus("mandatory")


class _ServerGradualLoadThreshold_Type(Integer32):
    """Custom type serverGradualLoadThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ServerGradualLoadThreshold_Type.__name__ = "Integer32"
_ServerGradualLoadThreshold_Object = MibTableColumn
serverGradualLoadThreshold = _ServerGradualLoadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 13),
    _ServerGradualLoadThreshold_Type()
)
serverGradualLoadThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverGradualLoadThreshold.setStatus("mandatory")


class _ServerGradualRedirectState_Type(Integer32):
    """Custom type serverGradualRedirectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_ServerGradualRedirectState_Type.__name__ = "Integer32"
_ServerGradualRedirectState_Object = MibTableColumn
serverGradualRedirectState = _ServerGradualRedirectState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 9, 1, 1, 14),
    _ServerGradualRedirectState_Type()
)
serverGradualRedirectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverGradualRedirectState.setStatus("mandatory")
_ClusterManagement_ObjectIdentity = ObjectIdentity
clusterManagement = _ClusterManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10)
)
_ClusterTable_Object = MibTable
clusterTable = _ClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10, 1)
)
if mibBuilder.loadTexts:
    clusterTable.setStatus("mandatory")
_ClusterEntry_Object = MibTableRow
clusterEntry = _ClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1)
)
clusterEntry.setIndexNames(
    (0, "Macromedia-MIB", "clusterOrdinalNumber"),
)
if mibBuilder.loadTexts:
    clusterEntry.setStatus("mandatory")
_ClusterOrdinalNumber_Type = Integer32
_ClusterOrdinalNumber_Object = MibTableColumn
clusterOrdinalNumber = _ClusterOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 1),
    _ClusterOrdinalNumber_Type()
)
clusterOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterOrdinalNumber.setStatus("mandatory")


class _ClusterName_Type(DisplayString):
    """Custom type clusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClusterName_Type.__name__ = "DisplayString"
_ClusterName_Object = MibTableColumn
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 2),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("mandatory")


class _ClusterAdminAgent_Type(DisplayString):
    """Custom type clusterAdminAgent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClusterAdminAgent_Type.__name__ = "DisplayString"
_ClusterAdminAgent_Object = MibTableColumn
clusterAdminAgent = _ClusterAdminAgent_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 10, 1, 1, 3),
    _ClusterAdminAgent_Type()
)
clusterAdminAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterAdminAgent.setStatus("mandatory")
_ClusterMembership_ObjectIdentity = ObjectIdentity
clusterMembership = _ClusterMembership_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11)
)
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11, 1)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("mandatory")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "Macromedia-MIB", "mClusterOrdinalNumber"),
    (0, "Macromedia-MIB", "mServerOrdinalNumber"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("mandatory")
_MClusterOrdinalNumber_Type = Integer32
_MClusterOrdinalNumber_Object = MibTableColumn
mClusterOrdinalNumber = _MClusterOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 1),
    _MClusterOrdinalNumber_Type()
)
mClusterOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mClusterOrdinalNumber.setStatus("mandatory")
_MServerOrdinalNumber_Type = Integer32
_MServerOrdinalNumber_Object = MibTableColumn
mServerOrdinalNumber = _MServerOrdinalNumber_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 2),
    _MServerOrdinalNumber_Type()
)
mServerOrdinalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mServerOrdinalNumber.setStatus("mandatory")


class _MServerName_Type(DisplayString):
    """Custom type mServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MServerName_Type.__name__ = "DisplayString"
_MServerName_Object = MibTableColumn
mServerName = _MServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 11, 1, 1, 3),
    _MServerName_Type()
)
mServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mServerName.setStatus("mandatory")
_TrapRecord_ObjectIdentity = ObjectIdentity
trapRecord = _TrapRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12)
)


class _TrapProbeName_Type(DisplayString):
    """Custom type trapProbeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapProbeName_Type.__name__ = "DisplayString"
_TrapProbeName_Object = MibScalar
trapProbeName = _TrapProbeName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 1),
    _TrapProbeName_Type()
)
trapProbeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProbeName.setStatus("mandatory")


class _TrapProbeFailureTime_Type(DisplayString):
    """Custom type trapProbeFailureTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapProbeFailureTime_Type.__name__ = "DisplayString"
_TrapProbeFailureTime_Object = MibScalar
trapProbeFailureTime = _TrapProbeFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 2),
    _TrapProbeFailureTime_Type()
)
trapProbeFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapProbeFailureTime.setStatus("mandatory")


class _TrapServerName_Type(DisplayString):
    """Custom type trapServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapServerName_Type.__name__ = "DisplayString"
_TrapServerName_Object = MibScalar
trapServerName = _TrapServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 3),
    _TrapServerName_Type()
)
trapServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapServerName.setStatus("mandatory")


class _TrapServerState_Type(Integer32):
    """Custom type trapServerState based on Integer32"""
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
        *(("available", 0),
          ("busy", 2),
          ("restricted", 3),
          ("unavailable", 1))
    )


_TrapServerState_Type.__name__ = "Integer32"
_TrapServerState_Object = MibScalar
trapServerState = _TrapServerState_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 4),
    _TrapServerState_Type()
)
trapServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapServerState.setStatus("mandatory")


class _TrapServerAbnormalStateTime_Type(DisplayString):
    """Custom type trapServerAbnormalStateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapServerAbnormalStateTime_Type.__name__ = "DisplayString"
_TrapServerAbnormalStateTime_Object = MibScalar
trapServerAbnormalStateTime = _TrapServerAbnormalStateTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 5),
    _TrapServerAbnormalStateTime_Type()
)
trapServerAbnormalStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapServerAbnormalStateTime.setStatus("mandatory")


class _TrapJRunServerName_Type(DisplayString):
    """Custom type trapJRunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapJRunServerName_Type.__name__ = "DisplayString"
_TrapJRunServerName_Object = MibScalar
trapJRunServerName = _TrapJRunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 6),
    _TrapJRunServerName_Type()
)
trapJRunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapJRunServerName.setStatus("mandatory")


class _TrapJRunServerAbnormalStateTime_Type(DisplayString):
    """Custom type trapJRunServerAbnormalStateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapJRunServerAbnormalStateTime_Type.__name__ = "DisplayString"
_TrapJRunServerAbnormalStateTime_Object = MibScalar
trapJRunServerAbnormalStateTime = _TrapJRunServerAbnormalStateTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 7),
    _TrapJRunServerAbnormalStateTime_Type()
)
trapJRunServerAbnormalStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapJRunServerAbnormalStateTime.setStatus("mandatory")


class _TrapJdbcJRunServerName_Type(DisplayString):
    """Custom type trapJdbcJRunServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapJdbcJRunServerName_Type.__name__ = "DisplayString"
_TrapJdbcJRunServerName_Object = MibScalar
trapJdbcJRunServerName = _TrapJdbcJRunServerName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 8),
    _TrapJdbcJRunServerName_Type()
)
trapJdbcJRunServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapJdbcJRunServerName.setStatus("mandatory")


class _TrapJdbcName_Type(DisplayString):
    """Custom type trapJdbcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapJdbcName_Type.__name__ = "DisplayString"
_TrapJdbcName_Object = MibScalar
trapJdbcName = _TrapJdbcName_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 9),
    _TrapJdbcName_Type()
)
trapJdbcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapJdbcName.setStatus("mandatory")


class _TrapJRunJDBCFailureTime_Type(DisplayString):
    """Custom type trapJRunJDBCFailureTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_TrapJRunJDBCFailureTime_Type.__name__ = "DisplayString"
_TrapJRunJDBCFailureTime_Object = MibScalar
trapJRunJDBCFailureTime = _TrapJRunJDBCFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 7138, 1, 12, 10),
    _TrapJRunJDBCFailureTime_Type()
)
trapJRunJDBCFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapJRunJDBCFailureTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects

probeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7138, 0, 1)
)
probeFailure.setObjects(
    ("Macromedia-MIB", "trapProbeName")
)
if mibBuilder.loadTexts:
    probeFailure.setStatus(
        ""
    )

serverAbnormalState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7138, 0, 2)
)
serverAbnormalState.setObjects(
      *(("Macromedia-MIB", "trapServerName"),
        ("Macromedia-MIB", "trapServerState"))
)
if mibBuilder.loadTexts:
    serverAbnormalState.setStatus(
        ""
    )

jrunServerAbnormalState = NotificationType(
    (1, 3, 6, 1, 4, 1, 7138, 0, 3)
)
jrunServerAbnormalState.setObjects(
    ("Macromedia-MIB", "trapJRunServerName")
)
if mibBuilder.loadTexts:
    jrunServerAbnormalState.setStatus(
        ""
    )

jrunJDBCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 7138, 0, 4)
)
jrunJDBCFailure.setObjects(
      *(("Macromedia-MIB", "trapJdbcJRunServerName"),
        ("Macromedia-MIB", "trapJdbcName"))
)
if mibBuilder.loadTexts:
    jrunJDBCFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Macromedia-MIB",
    **{"allaire": allaire,
       "probeFailure": probeFailure,
       "serverAbnormalState": serverAbnormalState,
       "jrunServerAbnormalState": jrunServerAbnormalState,
       "jrunJDBCFailure": jrunJDBCFailure,
       "software": software,
       "coldfusion": coldfusion,
       "cfOSName": cfOSName,
       "cfOSVersion": cfOSVersion,
       "cfOSBuildNumber": cfOSBuildNumber,
       "cfOSAdditionalInfo": cfOSAdditionalInfo,
       "cfProductName": cfProductName,
       "cfProductLevel": cfProductLevel,
       "cfProductVersion": cfProductVersion,
       "cfPerformanceMonitorOn": cfPerformanceMonitorOn,
       "cfPageHits": cfPageHits,
       "cfRequestsQueued": cfRequestsQueued,
       "cfDatabaseHits": cfDatabaseHits,
       "cfRequestsRunning": cfRequestsRunning,
       "cfReqestsTimedOut": cfReqestsTimedOut,
       "cfBytesIn": cfBytesIn,
       "cfBytesOut": cfBytesOut,
       "cfAvgQueueTimes": cfAvgQueueTimes,
       "cfAvgRequestTime": cfAvgRequestTime,
       "cfAvgDBTime": cfAvgDBTime,
       "cfCachePops": cfCachePops,
       "cfMaxRequests": cfMaxRequests,
       "cfLimitTime": cfLimitTime,
       "cfMaxSeconds": cfMaxSeconds,
       "cfTrustCache": cfTrustCache,
       "cfTemplateCacheSize": cfTemplateCacheSize,
       "cfRunningRDS": cfRunningRDS,
       "cfDebuggingOn": cfDebuggingOn,
       "cfEnforceStrictAttributeValidation": cfEnforceStrictAttributeValidation,
       "cfRestartThreshold": cfRestartThreshold,
       "cfMaxCachedQueries": cfMaxCachedQueries,
       "cfMailServerName": cfMailServerName,
       "cfMailServerPortNumber": cfMailServerPortNumber,
       "cfMailServerConnectTimeout": cfMailServerConnectTimeout,
       "jrun": jrun,
       "jOSName": jOSName,
       "jOSVersion": jOSVersion,
       "jMachineArchitecture": jMachineArchitecture,
       "jJDKVendor": jJDKVendor,
       "jJDKVersion": jJDKVersion,
       "jJRunVersion": jJRunVersion,
       "jFreeMomory": jFreeMomory,
       "jTotalMomory": jTotalMomory,
       "jSessions": jSessions,
       "jSessionsInMemory": jSessionsInMemory,
       "jJcpBytesIn": jJcpBytesIn,
       "jJcpBytesOut": jJcpBytesOut,
       "jJcpHandledRequests": jJcpHandledRequests,
       "jJcpDelayRequests": jJcpDelayRequests,
       "jJcpDroppedRequests": jJcpDroppedRequests,
       "jJcpHandledMs": jJcpHandledMs,
       "jJcpDelayMs": jJcpDelayMs,
       "jJcpTotalThreads": jJcpTotalThreads,
       "jJcpListenThreads": jJcpListenThreads,
       "jJcpBusyThreads": jJcpBusyThreads,
       "jJcpDelayThreads": jJcpDelayThreads,
       "jJcpIdleThreads": jJcpIdleThreads,
       "jWebBytesIn": jWebBytesIn,
       "jWebBytesOut": jWebBytesOut,
       "jWebHandledRequests": jWebHandledRequests,
       "jWebDelayRequests": jWebDelayRequests,
       "jWebDroppedRequests": jWebDroppedRequests,
       "jWebHandledMs": jWebHandledMs,
       "jWebDelayMs": jWebDelayMs,
       "jWebTotalThreads": jWebTotalThreads,
       "jWebListenThreads": jWebListenThreads,
       "jWebBusyThreads": jWebBusyThreads,
       "jWebDelayThreads": jWebDelayThreads,
       "jWebIdleThreads": jWebIdleThreads,
       "jrunServers": jrunServers,
       "jrunServerTable": jrunServerTable,
       "jrunServerEntry": jrunServerEntry,
       "jrunServerOrdinal": jrunServerOrdinal,
       "jrunServerName": jrunServerName,
       "jrunServerState": jrunServerState,
       "jrunJDBCs": jrunJDBCs,
       "jrunJDBCTable": jrunJDBCTable,
       "jrunJDBCEntry": jrunJDBCEntry,
       "jdbcOrdinal": jdbcOrdinal,
       "jdbcJRunServerName": jdbcJRunServerName,
       "jdbcName": jdbcName,
       "jdbcState": jdbcState,
       "jrunWebApps": jrunWebApps,
       "jrunWebAppTable": jrunWebAppTable,
       "jrunWebAppEntry": jrunWebAppEntry,
       "webAppOrdinal": webAppOrdinal,
       "webAppJRunServerName": webAppJRunServerName,
       "webAppName": webAppName,
       "jrunEJBs": jrunEJBs,
       "jrunEjbTable": jrunEjbTable,
       "jrunEjbEntry": jrunEjbEntry,
       "ejbOrdinal": ejbOrdinal,
       "ejbJRunServerName": ejbJRunServerName,
       "ejbName": ejbName,
       "probes": probes,
       "probeTable": probeTable,
       "probeEntry": probeEntry,
       "probeOrdinalNumber": probeOrdinalNumber,
       "probeName": probeName,
       "probeState": probeState,
       "haaManagement": haaManagement,
       "haaServerTable": haaServerTable,
       "hserverEntry": hserverEntry,
       "hServerOrdinalNumber": hServerOrdinalNumber,
       "hServerName": hServerName,
       "hServerIP": hServerIP,
       "hServerState": hServerState,
       "hServerMode": hServerMode,
       "hServerLoad": hServerLoad,
       "hServerLoadBalanceProduct": hServerLoadBalanceProduct,
       "hServerLoadThreshold": hServerLoadThreshold,
       "hServerLoadType": hServerLoadType,
       "serverManagement": serverManagement,
       "serverTable": serverTable,
       "serverEntry": serverEntry,
       "serverOrdinalNumber": serverOrdinalNumber,
       "serverName": serverName,
       "serverIP": serverIP,
       "serverState": serverState,
       "serverMode": serverMode,
       "serverLoad": serverLoad,
       "serverLoadBalanceProduct": serverLoadBalanceProduct,
       "serverLoadThreshold": serverLoadThreshold,
       "serverLoadType": serverLoadType,
       "serverCluster": serverCluster,
       "serverAdminAgent": serverAdminAgent,
       "serverSessionAwareness": serverSessionAwareness,
       "serverGradualLoadThreshold": serverGradualLoadThreshold,
       "serverGradualRedirectState": serverGradualRedirectState,
       "clusterManagement": clusterManagement,
       "clusterTable": clusterTable,
       "clusterEntry": clusterEntry,
       "clusterOrdinalNumber": clusterOrdinalNumber,
       "clusterName": clusterName,
       "clusterAdminAgent": clusterAdminAgent,
       "clusterMembership": clusterMembership,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "mClusterOrdinalNumber": mClusterOrdinalNumber,
       "mServerOrdinalNumber": mServerOrdinalNumber,
       "mServerName": mServerName,
       "trapRecord": trapRecord,
       "trapProbeName": trapProbeName,
       "trapProbeFailureTime": trapProbeFailureTime,
       "trapServerName": trapServerName,
       "trapServerState": trapServerState,
       "trapServerAbnormalStateTime": trapServerAbnormalStateTime,
       "trapJRunServerName": trapJRunServerName,
       "trapJRunServerAbnormalStateTime": trapJRunServerAbnormalStateTime,
       "trapJdbcJRunServerName": trapJdbcJRunServerName,
       "trapJdbcName": trapJdbcName,
       "trapJRunJDBCFailureTime": trapJRunJDBCFailureTime}
)
