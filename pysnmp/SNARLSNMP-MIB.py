# SNMP MIB module (SNARLSNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SNARLSNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:55:48 2024
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
 Opaque,
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
    "Opaque",
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

snarlsnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15553)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TruthValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )



class Comparative(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bigger", 1),
          ("equal", 0),
          ("smaller", -1))
    )



class AgeComparative(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bigger", 1),
          ("equal", 0),
          ("smaller", -1))
    )



class Float(Opaque, TextualConvention):
    status = "current"
    subtypeSpec = Opaque.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )



# MIB Managed Objects in the order of their OIDs

_Snarl_ObjectIdentity = ObjectIdentity
snarl = _Snarl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15553, 1)
)
_SnarlGlobalInfo_ObjectIdentity = ObjectIdentity
snarlGlobalInfo = _SnarlGlobalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15553, 1, 1)
)
_SnarlTotalTaskCount_Type = Integer32
_SnarlTotalTaskCount_Object = MibScalar
snarlTotalTaskCount = _SnarlTotalTaskCount_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 1, 1),
    _SnarlTotalTaskCount_Type()
)
snarlTotalTaskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snarlTotalTaskCount.setStatus("current")
_SnarlTotalTransfers_Type = Integer32
_SnarlTotalTransfers_Object = MibScalar
snarlTotalTransfers = _SnarlTotalTransfers_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 1, 2),
    _SnarlTotalTransfers_Type()
)
snarlTotalTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snarlTotalTransfers.setStatus("current")
_SnarlTotalTransferVolume_Type = Integer32
_SnarlTotalTransferVolume_Object = MibScalar
snarlTotalTransferVolume = _SnarlTotalTransferVolume_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 1, 3),
    _SnarlTotalTransferVolume_Type()
)
snarlTotalTransferVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snarlTotalTransferVolume.setStatus("current")
_SiteTable_Object = MibTable
siteTable = _SiteTable_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2)
)
if mibBuilder.loadTexts:
    siteTable.setStatus("current")
_SiteEntry_Object = MibTableRow
siteEntry = _SiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1)
)
siteEntry.setIndexNames(
    (0, "SNARLSNMP-MIB", "siteIndex"),
)
if mibBuilder.loadTexts:
    siteEntry.setStatus("current")


class _SiteIndex_Type(Integer32):
    """Custom type siteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SiteIndex_Type.__name__ = "Integer32"
_SiteIndex_Object = MibTableColumn
siteIndex = _SiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 1),
    _SiteIndex_Type()
)
siteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteIndex.setStatus("current")
_SiteName_Type = DisplayString
_SiteName_Object = MibTableColumn
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 2),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_SiteID_Type = DisplayString
_SiteID_Object = MibTableColumn
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 3),
    _SiteID_Type()
)
siteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteID.setStatus("current")
_SiteInterval_Type = Integer32
_SiteInterval_Object = MibTableColumn
siteInterval = _SiteInterval_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 4),
    _SiteInterval_Type()
)
siteInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteInterval.setStatus("current")
_SiteURL_Type = DisplayString
_SiteURL_Object = MibTableColumn
siteURL = _SiteURL_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 5),
    _SiteURL_Type()
)
siteURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURL.setStatus("current")
_SiteDynamicURLRegexPattern_Type = DisplayString
_SiteDynamicURLRegexPattern_Object = MibTableColumn
siteDynamicURLRegexPattern = _SiteDynamicURLRegexPattern_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 6),
    _SiteDynamicURLRegexPattern_Type()
)
siteDynamicURLRegexPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDynamicURLRegexPattern.setStatus("current")
_SiteDynmaicURLRegexCompilation_Type = DisplayString
_SiteDynmaicURLRegexCompilation_Object = MibTableColumn
siteDynmaicURLRegexCompilation = _SiteDynmaicURLRegexCompilation_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 7),
    _SiteDynmaicURLRegexCompilation_Type()
)
siteDynmaicURLRegexCompilation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDynmaicURLRegexCompilation.setStatus("current")
_SiteDynmaicURLRegexError_Type = DisplayString
_SiteDynmaicURLRegexError_Object = MibTableColumn
siteDynmaicURLRegexError = _SiteDynmaicURLRegexError_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 8),
    _SiteDynmaicURLRegexError_Type()
)
siteDynmaicURLRegexError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDynmaicURLRegexError.setStatus("current")
_SiteDynamicURL_Type = DisplayString
_SiteDynamicURL_Object = MibTableColumn
siteDynamicURL = _SiteDynamicURL_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 9),
    _SiteDynamicURL_Type()
)
siteDynamicURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDynamicURL.setStatus("current")
_SiteGetDynamicURLFrom_Type = DisplayString
_SiteGetDynamicURLFrom_Object = MibTableColumn
siteGetDynamicURLFrom = _SiteGetDynamicURLFrom_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 10),
    _SiteGetDynamicURLFrom_Type()
)
siteGetDynamicURLFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGetDynamicURLFrom.setStatus("current")
_SiteProxy_Type = DisplayString
_SiteProxy_Object = MibTableColumn
siteProxy = _SiteProxy_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 11),
    _SiteProxy_Type()
)
siteProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteProxy.setStatus("current")
_SiteMultiFormData_Type = DisplayString
_SiteMultiFormData_Object = MibTableColumn
siteMultiFormData = _SiteMultiFormData_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 12),
    _SiteMultiFormData_Type()
)
siteMultiFormData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMultiFormData.setStatus("current")
_SiteFormData_Type = DisplayString
_SiteFormData_Object = MibTableColumn
siteFormData = _SiteFormData_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 13),
    _SiteFormData_Type()
)
siteFormData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFormData.setStatus("current")
_SiteEffectiveURL_Type = DisplayString
_SiteEffectiveURL_Object = MibTableColumn
siteEffectiveURL = _SiteEffectiveURL_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 14),
    _SiteEffectiveURL_Type()
)
siteEffectiveURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteEffectiveURL.setStatus("current")
_SiteURLHTTPCode_Type = Integer32
_SiteURLHTTPCode_Object = MibTableColumn
siteURLHTTPCode = _SiteURLHTTPCode_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 15),
    _SiteURLHTTPCode_Type()
)
siteURLHTTPCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLHTTPCode.setStatus("current")
_SitePerformanceDNS_Type = Integer32
_SitePerformanceDNS_Object = MibTableColumn
sitePerformanceDNS = _SitePerformanceDNS_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 16),
    _SitePerformanceDNS_Type()
)
sitePerformanceDNS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceDNS.setStatus("current")
_SitePerformanceConnect_Type = Integer32
_SitePerformanceConnect_Object = MibTableColumn
sitePerformanceConnect = _SitePerformanceConnect_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 17),
    _SitePerformanceConnect_Type()
)
sitePerformanceConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceConnect.setStatus("current")
_SitePerformanceFirstByte_Type = Integer32
_SitePerformanceFirstByte_Object = MibTableColumn
sitePerformanceFirstByte = _SitePerformanceFirstByte_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 18),
    _SitePerformanceFirstByte_Type()
)
sitePerformanceFirstByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceFirstByte.setStatus("current")
_SitePerformanceTotal_Type = Integer32
_SitePerformanceTotal_Object = MibTableColumn
sitePerformanceTotal = _SitePerformanceTotal_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 19),
    _SitePerformanceTotal_Type()
)
sitePerformanceTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceTotal.setStatus("current")
_SitePerformanceTotalWarningThreshold_Type = Integer32
_SitePerformanceTotalWarningThreshold_Object = MibTableColumn
sitePerformanceTotalWarningThreshold = _SitePerformanceTotalWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 20),
    _SitePerformanceTotalWarningThreshold_Type()
)
sitePerformanceTotalWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceTotalWarningThreshold.setStatus("current")
_SitePerformanceTotalCriticalThreshold_Type = Integer32
_SitePerformanceTotalCriticalThreshold_Object = MibTableColumn
sitePerformanceTotalCriticalThreshold = _SitePerformanceTotalCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 21),
    _SitePerformanceTotalCriticalThreshold_Type()
)
sitePerformanceTotalCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sitePerformanceTotalCriticalThreshold.setStatus("current")
_SiteRegexPattern_Type = DisplayString
_SiteRegexPattern_Object = MibTableColumn
siteRegexPattern = _SiteRegexPattern_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 22),
    _SiteRegexPattern_Type()
)
siteRegexPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteRegexPattern.setStatus("current")
_SiteRegexCompilation_Type = DisplayString
_SiteRegexCompilation_Object = MibTableColumn
siteRegexCompilation = _SiteRegexCompilation_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 23),
    _SiteRegexCompilation_Type()
)
siteRegexCompilation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteRegexCompilation.setStatus("current")
_SiteRegexPatternMatchFlag_Type = TruthValue
_SiteRegexPatternMatchFlag_Object = MibTableColumn
siteRegexPatternMatchFlag = _SiteRegexPatternMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 24),
    _SiteRegexPatternMatchFlag_Type()
)
siteRegexPatternMatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteRegexPatternMatchFlag.setStatus("current")
_SiteRegexPatternAlertOnMatch_Type = TruthValue
_SiteRegexPatternAlertOnMatch_Object = MibTableColumn
siteRegexPatternAlertOnMatch = _SiteRegexPatternAlertOnMatch_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 25),
    _SiteRegexPatternAlertOnMatch_Type()
)
siteRegexPatternAlertOnMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteRegexPatternAlertOnMatch.setStatus("current")
_SiteContentMatchSize_Type = Integer32
_SiteContentMatchSize_Object = MibTableColumn
siteContentMatchSize = _SiteContentMatchSize_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 26),
    _SiteContentMatchSize_Type()
)
siteContentMatchSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteContentMatchSize.setStatus("current")
_SiteContentActualSize_Type = Integer32
_SiteContentActualSize_Object = MibTableColumn
siteContentActualSize = _SiteContentActualSize_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 27),
    _SiteContentActualSize_Type()
)
siteContentActualSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteContentActualSize.setStatus("current")
_SiteContentSizeMatchFlag_Type = Comparative
_SiteContentSizeMatchFlag_Object = MibTableColumn
siteContentSizeMatchFlag = _SiteContentSizeMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 28),
    _SiteContentSizeMatchFlag_Type()
)
siteContentSizeMatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteContentSizeMatchFlag.setStatus("current")
_SiteContentSizeAlertOnMatch_Type = TruthValue
_SiteContentSizeAlertOnMatch_Object = MibTableColumn
siteContentSizeAlertOnMatch = _SiteContentSizeAlertOnMatch_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 29),
    _SiteContentSizeAlertOnMatch_Type()
)
siteContentSizeAlertOnMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteContentSizeAlertOnMatch.setStatus("current")
_SiteURLContentPattern_Type = DisplayString
_SiteURLContentPattern_Object = MibTableColumn
siteURLContentPattern = _SiteURLContentPattern_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 30),
    _SiteURLContentPattern_Type()
)
siteURLContentPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLContentPattern.setStatus("current")
_SiteURLContentPatternMatchFlag_Type = TruthValue
_SiteURLContentPatternMatchFlag_Object = MibTableColumn
siteURLContentPatternMatchFlag = _SiteURLContentPatternMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 31),
    _SiteURLContentPatternMatchFlag_Type()
)
siteURLContentPatternMatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLContentPatternMatchFlag.setStatus("current")
_SiteURLContentPatternAlertOnMatch_Type = TruthValue
_SiteURLContentPatternAlertOnMatch_Object = MibTableColumn
siteURLContentPatternAlertOnMatch = _SiteURLContentPatternAlertOnMatch_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 32),
    _SiteURLContentPatternAlertOnMatch_Type()
)
siteURLContentPatternAlertOnMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLContentPatternAlertOnMatch.setStatus("current")
_SiteURLContentPatternProxy_Type = DisplayString
_SiteURLContentPatternProxy_Object = MibTableColumn
siteURLContentPatternProxy = _SiteURLContentPatternProxy_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 33),
    _SiteURLContentPatternProxy_Type()
)
siteURLContentPatternProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLContentPatternProxy.setStatus("current")
_SiteURLContentPatternHTTPCode_Type = Integer32
_SiteURLContentPatternHTTPCode_Object = MibTableColumn
siteURLContentPatternHTTPCode = _SiteURLContentPatternHTTPCode_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 34),
    _SiteURLContentPatternHTTPCode_Type()
)
siteURLContentPatternHTTPCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLContentPatternHTTPCode.setStatus("current")
_SiteURLSize_Type = DisplayString
_SiteURLSize_Object = MibTableColumn
siteURLSize = _SiteURLSize_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 35),
    _SiteURLSize_Type()
)
siteURLSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLSize.setStatus("current")
_SiteURLSizeMatchFlag_Type = TruthValue
_SiteURLSizeMatchFlag_Object = MibTableColumn
siteURLSizeMatchFlag = _SiteURLSizeMatchFlag_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 36),
    _SiteURLSizeMatchFlag_Type()
)
siteURLSizeMatchFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLSizeMatchFlag.setStatus("current")
_SiteURLSizeAlertOnMatch_Type = TruthValue
_SiteURLSizeAlertOnMatch_Object = MibTableColumn
siteURLSizeAlertOnMatch = _SiteURLSizeAlertOnMatch_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 37),
    _SiteURLSizeAlertOnMatch_Type()
)
siteURLSizeAlertOnMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLSizeAlertOnMatch.setStatus("current")
_SiteURLSizeProxy_Type = DisplayString
_SiteURLSizeProxy_Object = MibTableColumn
siteURLSizeProxy = _SiteURLSizeProxy_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 38),
    _SiteURLSizeProxy_Type()
)
siteURLSizeProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLSizeProxy.setStatus("current")
_SiteURLSizeHTTPCode_Type = Integer32
_SiteURLSizeHTTPCode_Object = MibTableColumn
siteURLSizeHTTPCode = _SiteURLSizeHTTPCode_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 39),
    _SiteURLSizeHTTPCode_Type()
)
siteURLSizeHTTPCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteURLSizeHTTPCode.setStatus("current")
_SiteFetchRegex_Type = DisplayString
_SiteFetchRegex_Object = MibTableColumn
siteFetchRegex = _SiteFetchRegex_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 40),
    _SiteFetchRegex_Type()
)
siteFetchRegex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegex.setStatus("current")
_SiteFetchRegexCompilationError_Type = DisplayString
_SiteFetchRegexCompilationError_Object = MibTableColumn
siteFetchRegexCompilationError = _SiteFetchRegexCompilationError_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 41),
    _SiteFetchRegexCompilationError_Type()
)
siteFetchRegexCompilationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexCompilationError.setStatus("current")
_SiteFetchRegexMatchingError_Type = DisplayString
_SiteFetchRegexMatchingError_Object = MibTableColumn
siteFetchRegexMatchingError = _SiteFetchRegexMatchingError_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 42),
    _SiteFetchRegexMatchingError_Type()
)
siteFetchRegexMatchingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexMatchingError.setStatus("current")
_SiteFetchRegexSubResult0_Type = DisplayString
_SiteFetchRegexSubResult0_Object = MibTableColumn
siteFetchRegexSubResult0 = _SiteFetchRegexSubResult0_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 43),
    _SiteFetchRegexSubResult0_Type()
)
siteFetchRegexSubResult0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult0.setStatus("current")
_SiteFetchRegexSubResult1_Type = DisplayString
_SiteFetchRegexSubResult1_Object = MibTableColumn
siteFetchRegexSubResult1 = _SiteFetchRegexSubResult1_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 44),
    _SiteFetchRegexSubResult1_Type()
)
siteFetchRegexSubResult1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult1.setStatus("current")
_SiteFetchRegexSubResult2_Type = DisplayString
_SiteFetchRegexSubResult2_Object = MibTableColumn
siteFetchRegexSubResult2 = _SiteFetchRegexSubResult2_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 45),
    _SiteFetchRegexSubResult2_Type()
)
siteFetchRegexSubResult2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult2.setStatus("current")
_SiteFetchRegexSubResult3_Type = DisplayString
_SiteFetchRegexSubResult3_Object = MibTableColumn
siteFetchRegexSubResult3 = _SiteFetchRegexSubResult3_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 46),
    _SiteFetchRegexSubResult3_Type()
)
siteFetchRegexSubResult3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult3.setStatus("current")
_SiteFetchRegexSubResult4_Type = DisplayString
_SiteFetchRegexSubResult4_Object = MibTableColumn
siteFetchRegexSubResult4 = _SiteFetchRegexSubResult4_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 47),
    _SiteFetchRegexSubResult4_Type()
)
siteFetchRegexSubResult4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult4.setStatus("current")
_SiteFetchRegexSubResult5_Type = DisplayString
_SiteFetchRegexSubResult5_Object = MibTableColumn
siteFetchRegexSubResult5 = _SiteFetchRegexSubResult5_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 48),
    _SiteFetchRegexSubResult5_Type()
)
siteFetchRegexSubResult5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult5.setStatus("current")
_SiteFetchRegexSubResult6_Type = DisplayString
_SiteFetchRegexSubResult6_Object = MibTableColumn
siteFetchRegexSubResult6 = _SiteFetchRegexSubResult6_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 49),
    _SiteFetchRegexSubResult6_Type()
)
siteFetchRegexSubResult6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult6.setStatus("current")
_SiteFetchRegexSubResult7_Type = DisplayString
_SiteFetchRegexSubResult7_Object = MibTableColumn
siteFetchRegexSubResult7 = _SiteFetchRegexSubResult7_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 50),
    _SiteFetchRegexSubResult7_Type()
)
siteFetchRegexSubResult7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFetchRegexSubResult7.setStatus("current")
_SiteAppendRegexResultFrom_Type = DisplayString
_SiteAppendRegexResultFrom_Object = MibTableColumn
siteAppendRegexResultFrom = _SiteAppendRegexResultFrom_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 51),
    _SiteAppendRegexResultFrom_Type()
)
siteAppendRegexResultFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteAppendRegexResultFrom.setStatus("current")
_SiteAppendRegexResultFromIndex_Type = Integer32
_SiteAppendRegexResultFromIndex_Object = MibTableColumn
siteAppendRegexResultFromIndex = _SiteAppendRegexResultFromIndex_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 52),
    _SiteAppendRegexResultFromIndex_Type()
)
siteAppendRegexResultFromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteAppendRegexResultFromIndex.setStatus("current")
_SiteNumericalRegexSubMatch_Type = Integer32
_SiteNumericalRegexSubMatch_Object = MibTableColumn
siteNumericalRegexSubMatch = _SiteNumericalRegexSubMatch_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 53),
    _SiteNumericalRegexSubMatch_Type()
)
siteNumericalRegexSubMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNumericalRegexSubMatch.setStatus("current")
_SiteNumericalPattern_Type = DisplayString
_SiteNumericalPattern_Object = MibTableColumn
siteNumericalPattern = _SiteNumericalPattern_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 54),
    _SiteNumericalPattern_Type()
)
siteNumericalPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNumericalPattern.setStatus("current")
_SiteNumericalAlertOn_Type = Comparative
_SiteNumericalAlertOn_Object = MibTableColumn
siteNumericalAlertOn = _SiteNumericalAlertOn_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 55),
    _SiteNumericalAlertOn_Type()
)
siteNumericalAlertOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNumericalAlertOn.setStatus("current")
_SiteFileTime_Type = Integer32
_SiteFileTime_Object = MibTableColumn
siteFileTime = _SiteFileTime_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 56),
    _SiteFileTime_Type()
)
siteFileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFileTime.setStatus("current")
_SiteDateAgeRegexConstruct_Type = DisplayString
_SiteDateAgeRegexConstruct_Object = MibTableColumn
siteDateAgeRegexConstruct = _SiteDateAgeRegexConstruct_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 57),
    _SiteDateAgeRegexConstruct_Type()
)
siteDateAgeRegexConstruct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDateAgeRegexConstruct.setStatus("current")
_SiteDateAgePattern_Type = DisplayString
_SiteDateAgePattern_Object = MibTableColumn
siteDateAgePattern = _SiteDateAgePattern_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 58),
    _SiteDateAgePattern_Type()
)
siteDateAgePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDateAgePattern.setStatus("current")
_SiteDateAgeAlertOn_Type = AgeComparative
_SiteDateAgeAlertOn_Object = MibTableColumn
siteDateAgeAlertOn = _SiteDateAgeAlertOn_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 59),
    _SiteDateAgeAlertOn_Type()
)
siteDateAgeAlertOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteDateAgeAlertOn.setStatus("current")
_SiteTaskSuspendStart_Type = DisplayString
_SiteTaskSuspendStart_Object = MibTableColumn
siteTaskSuspendStart = _SiteTaskSuspendStart_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 60),
    _SiteTaskSuspendStart_Type()
)
siteTaskSuspendStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTaskSuspendStart.setStatus("current")
_SiteTaskSuspendEnd_Type = DisplayString
_SiteTaskSuspendEnd_Object = MibTableColumn
siteTaskSuspendEnd = _SiteTaskSuspendEnd_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 61),
    _SiteTaskSuspendEnd_Type()
)
siteTaskSuspendEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTaskSuspendEnd.setStatus("current")
_SiteStatusNormal_Type = TruthValue
_SiteStatusNormal_Object = MibTableColumn
siteStatusNormal = _SiteStatusNormal_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 62),
    _SiteStatusNormal_Type()
)
siteStatusNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteStatusNormal.setStatus("current")
_SiteStatusWarning_Type = TruthValue
_SiteStatusWarning_Object = MibTableColumn
siteStatusWarning = _SiteStatusWarning_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 63),
    _SiteStatusWarning_Type()
)
siteStatusWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteStatusWarning.setStatus("current")
_SiteStatusCritical_Type = TruthValue
_SiteStatusCritical_Object = MibTableColumn
siteStatusCritical = _SiteStatusCritical_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 64),
    _SiteStatusCritical_Type()
)
siteStatusCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteStatusCritical.setStatus("current")
_SiteGroupStatusNormal_Type = TruthValue
_SiteGroupStatusNormal_Object = MibTableColumn
siteGroupStatusNormal = _SiteGroupStatusNormal_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 65),
    _SiteGroupStatusNormal_Type()
)
siteGroupStatusNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupStatusNormal.setStatus("current")
_SiteGroupStatusWarning_Type = TruthValue
_SiteGroupStatusWarning_Object = MibTableColumn
siteGroupStatusWarning = _SiteGroupStatusWarning_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 66),
    _SiteGroupStatusWarning_Type()
)
siteGroupStatusWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupStatusWarning.setStatus("current")
_SiteGroupStatusCritical_Type = TruthValue
_SiteGroupStatusCritical_Object = MibTableColumn
siteGroupStatusCritical = _SiteGroupStatusCritical_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 67),
    _SiteGroupStatusCritical_Type()
)
siteGroupStatusCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteGroupStatusCritical.setStatus("current")
_SiteReliability_Type = Integer32
_SiteReliability_Object = MibTableColumn
siteReliability = _SiteReliability_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 68),
    _SiteReliability_Type()
)
siteReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteReliability.setStatus("current")
_SiteMTBWarnings_Type = TimeTicks
_SiteMTBWarnings_Object = MibTableColumn
siteMTBWarnings = _SiteMTBWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 69),
    _SiteMTBWarnings_Type()
)
siteMTBWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMTBWarnings.setStatus("current")
_SiteMTTRWarnings_Type = TimeTicks
_SiteMTTRWarnings_Object = MibTableColumn
siteMTTRWarnings = _SiteMTTRWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 70),
    _SiteMTTRWarnings_Type()
)
siteMTTRWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMTTRWarnings.setStatus("current")
_SiteAccumulatedWarnings_Type = Integer32
_SiteAccumulatedWarnings_Object = MibTableColumn
siteAccumulatedWarnings = _SiteAccumulatedWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 71),
    _SiteAccumulatedWarnings_Type()
)
siteAccumulatedWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteAccumulatedWarnings.setStatus("current")
_SiteMTBCriticals_Type = TimeTicks
_SiteMTBCriticals_Object = MibTableColumn
siteMTBCriticals = _SiteMTBCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 72),
    _SiteMTBCriticals_Type()
)
siteMTBCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMTBCriticals.setStatus("current")
_SiteMTTRCriticals_Type = TimeTicks
_SiteMTTRCriticals_Object = MibTableColumn
siteMTTRCriticals = _SiteMTTRCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 73),
    _SiteMTTRCriticals_Type()
)
siteMTTRCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteMTTRCriticals.setStatus("current")
_SiteAccumulatedCriticals_Type = Integer32
_SiteAccumulatedCriticals_Object = MibTableColumn
siteAccumulatedCriticals = _SiteAccumulatedCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 74),
    _SiteAccumulatedCriticals_Type()
)
siteAccumulatedCriticals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteAccumulatedCriticals.setStatus("current")
_SiteGroupReliability_Type = Integer32
_SiteGroupReliability_Object = MibTableColumn
siteGroupReliability = _SiteGroupReliability_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 75),
    _SiteGroupReliability_Type()
)
siteGroupReliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupReliability.setStatus("current")
_SiteGroupMTBWarnings_Type = TimeTicks
_SiteGroupMTBWarnings_Object = MibTableColumn
siteGroupMTBWarnings = _SiteGroupMTBWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 76),
    _SiteGroupMTBWarnings_Type()
)
siteGroupMTBWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupMTBWarnings.setStatus("current")
_SiteGroupMTTRWarnings_Type = TimeTicks
_SiteGroupMTTRWarnings_Object = MibTableColumn
siteGroupMTTRWarnings = _SiteGroupMTTRWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 77),
    _SiteGroupMTTRWarnings_Type()
)
siteGroupMTTRWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupMTTRWarnings.setStatus("current")
_SiteGroupAccumulatedWarnings_Type = Integer32
_SiteGroupAccumulatedWarnings_Object = MibTableColumn
siteGroupAccumulatedWarnings = _SiteGroupAccumulatedWarnings_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 78),
    _SiteGroupAccumulatedWarnings_Type()
)
siteGroupAccumulatedWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupAccumulatedWarnings.setStatus("current")
_SiteGroupMTBCriticals_Type = TimeTicks
_SiteGroupMTBCriticals_Object = MibTableColumn
siteGroupMTBCriticals = _SiteGroupMTBCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 79),
    _SiteGroupMTBCriticals_Type()
)
siteGroupMTBCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupMTBCriticals.setStatus("current")
_SiteGroupMTTRCriticals_Type = TimeTicks
_SiteGroupMTTRCriticals_Object = MibTableColumn
siteGroupMTTRCriticals = _SiteGroupMTTRCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 80),
    _SiteGroupMTTRCriticals_Type()
)
siteGroupMTTRCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupMTTRCriticals.setStatus("current")
_SiteGroupAccumulatedCriticals_Type = Integer32
_SiteGroupAccumulatedCriticals_Object = MibTableColumn
siteGroupAccumulatedCriticals = _SiteGroupAccumulatedCriticals_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 81),
    _SiteGroupAccumulatedCriticals_Type()
)
siteGroupAccumulatedCriticals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteGroupAccumulatedCriticals.setStatus("current")
_SiteLastRunRelativeTime_Type = TimeTicks
_SiteLastRunRelativeTime_Object = MibTableColumn
siteLastRunRelativeTime = _SiteLastRunRelativeTime_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 82),
    _SiteLastRunRelativeTime_Type()
)
siteLastRunRelativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteLastRunRelativeTime.setStatus("current")
_SiteLastRunAbsTimeString_Type = DisplayString
_SiteLastRunAbsTimeString_Object = MibTableColumn
siteLastRunAbsTimeString = _SiteLastRunAbsTimeString_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 83),
    _SiteLastRunAbsTimeString_Type()
)
siteLastRunAbsTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteLastRunAbsTimeString.setStatus("current")
_SiteNextRunRelativeTime_Type = TimeTicks
_SiteNextRunRelativeTime_Object = MibTableColumn
siteNextRunRelativeTime = _SiteNextRunRelativeTime_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 84),
    _SiteNextRunRelativeTime_Type()
)
siteNextRunRelativeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNextRunRelativeTime.setStatus("current")
_SiteNextRunAbsTimeString_Type = DisplayString
_SiteNextRunAbsTimeString_Object = MibTableColumn
siteNextRunAbsTimeString = _SiteNextRunAbsTimeString_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 85),
    _SiteNextRunAbsTimeString_Type()
)
siteNextRunAbsTimeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteNextRunAbsTimeString.setStatus("current")
_SiteFirstRun_Type = DisplayString
_SiteFirstRun_Object = MibTableColumn
siteFirstRun = _SiteFirstRun_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 86),
    _SiteFirstRun_Type()
)
siteFirstRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteFirstRun.setStatus("current")
_SiteTotalTransfers_Type = Integer32
_SiteTotalTransfers_Object = MibTableColumn
siteTotalTransfers = _SiteTotalTransfers_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 87),
    _SiteTotalTransfers_Type()
)
siteTotalTransfers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalTransfers.setStatus("current")
_SiteTotalTransferVolume_Type = Integer32
_SiteTotalTransferVolume_Object = MibTableColumn
siteTotalTransferVolume = _SiteTotalTransferVolume_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 2, 1, 88),
    _SiteTotalTransferVolume_Type()
)
siteTotalTransferVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteTotalTransferVolume.setStatus("current")
_GroupStatus_Type = Integer32
_GroupStatus_Object = MibScalar
groupStatus = _GroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 100),
    _GroupStatus_Type()
)
groupStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    groupStatus.setStatus("current")
_ProxyStatus_Type = Integer32
_ProxyStatus_Object = MibScalar
proxyStatus = _ProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 101),
    _ProxyStatus_Type()
)
proxyStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    proxyStatus.setStatus("current")
_SiteStatus_Type = Integer32
_SiteStatus_Object = MibScalar
siteStatus = _SiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 102),
    _SiteStatus_Type()
)
siteStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteStatus.setStatus("current")


class _SubTaskID_Type(Integer32):
    """Custom type subTaskID based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 12),
          ("dateAgeMatch", 9),
          ("general", 1),
          ("heartBeat", 13),
          ("httpCode", 3),
          ("matchRegex", 4),
          ("matchSize", 5),
          ("numericalMatch", 8),
          ("performance", 2),
          ("suspension", 10),
          ("syncRequest", 14),
          ("urlContentMatch", 7),
          ("urlSizeMatch", 6),
          ("warmStart", 11))
    )


_SubTaskID_Type.__name__ = "Integer32"
_SubTaskID_Object = MibScalar
subTaskID = _SubTaskID_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 103),
    _SubTaskID_Type()
)
subTaskID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subTaskID.setStatus("current")
_EventTime_Type = Integer32
_EventTime_Object = MibScalar
eventTime = _EventTime_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 104),
    _EventTime_Type()
)
eventTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventTime.setStatus("current")
_SiteTrapMessage_Type = DisplayString
_SiteTrapMessage_Object = MibScalar
siteTrapMessage = _SiteTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 15553, 1, 105),
    _SiteTrapMessage_Type()
)
siteTrapMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteTrapMessage.setStatus("current")

# Managed Objects groups


# Notification objects

snarlsnmpInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 1)
)
snarlsnmpInfo.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpInfo.setStatus(
        ""
    )

snarlsnmpNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 2)
)
snarlsnmpNormal.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpNormal.setStatus(
        ""
    )

snarlsnmpWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 3)
)
snarlsnmpWarning.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpWarning.setStatus(
        ""
    )

snarlsnmpCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 4)
)
snarlsnmpCritical.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpCritical.setStatus(
        ""
    )

snarlsnmpSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 5)
)
snarlsnmpSuspended.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpSuspended.setStatus(
        ""
    )

snarlsnmpResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 6)
)
snarlsnmpResumed.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpResumed.setStatus(
        ""
    )

snarlsnmpGenericInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 7)
)
snarlsnmpGenericInfo.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpGenericInfo.setStatus(
        ""
    )

snarlsnmpStateUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 15553, 0, 8)
)
snarlsnmpStateUnknown.setObjects(
      *(("SNARLSNMP-MIB", "siteIndex"),
        ("SNARLSNMP-MIB", "subTaskID"),
        ("SNARLSNMP-MIB", "siteTrapMessage"),
        ("SNARLSNMP-MIB", "groupStatus"),
        ("SNARLSNMP-MIB", "siteName"),
        ("SNARLSNMP-MIB", "siteID"),
        ("SNARLSNMP-MIB", "siteProxy"),
        ("SNARLSNMP-MIB", "eventTime"),
        ("SNARLSNMP-MIB", "siteStatus"),
        ("SNARLSNMP-MIB", "proxyStatus"))
)
if mibBuilder.loadTexts:
    snarlsnmpStateUnknown.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNARLSNMP-MIB",
    **{"TruthValue": TruthValue,
       "Comparative": Comparative,
       "AgeComparative": AgeComparative,
       "Float": Float,
       "snarlsnmp": snarlsnmp,
       "snarlsnmpInfo": snarlsnmpInfo,
       "snarlsnmpNormal": snarlsnmpNormal,
       "snarlsnmpWarning": snarlsnmpWarning,
       "snarlsnmpCritical": snarlsnmpCritical,
       "snarlsnmpSuspended": snarlsnmpSuspended,
       "snarlsnmpResumed": snarlsnmpResumed,
       "snarlsnmpGenericInfo": snarlsnmpGenericInfo,
       "snarlsnmpStateUnknown": snarlsnmpStateUnknown,
       "snarl": snarl,
       "snarlGlobalInfo": snarlGlobalInfo,
       "snarlTotalTaskCount": snarlTotalTaskCount,
       "snarlTotalTransfers": snarlTotalTransfers,
       "snarlTotalTransferVolume": snarlTotalTransferVolume,
       "siteTable": siteTable,
       "siteEntry": siteEntry,
       "siteIndex": siteIndex,
       "siteName": siteName,
       "siteID": siteID,
       "siteInterval": siteInterval,
       "siteURL": siteURL,
       "siteDynamicURLRegexPattern": siteDynamicURLRegexPattern,
       "siteDynmaicURLRegexCompilation": siteDynmaicURLRegexCompilation,
       "siteDynmaicURLRegexError": siteDynmaicURLRegexError,
       "siteDynamicURL": siteDynamicURL,
       "siteGetDynamicURLFrom": siteGetDynamicURLFrom,
       "siteProxy": siteProxy,
       "siteMultiFormData": siteMultiFormData,
       "siteFormData": siteFormData,
       "siteEffectiveURL": siteEffectiveURL,
       "siteURLHTTPCode": siteURLHTTPCode,
       "sitePerformanceDNS": sitePerformanceDNS,
       "sitePerformanceConnect": sitePerformanceConnect,
       "sitePerformanceFirstByte": sitePerformanceFirstByte,
       "sitePerformanceTotal": sitePerformanceTotal,
       "sitePerformanceTotalWarningThreshold": sitePerformanceTotalWarningThreshold,
       "sitePerformanceTotalCriticalThreshold": sitePerformanceTotalCriticalThreshold,
       "siteRegexPattern": siteRegexPattern,
       "siteRegexCompilation": siteRegexCompilation,
       "siteRegexPatternMatchFlag": siteRegexPatternMatchFlag,
       "siteRegexPatternAlertOnMatch": siteRegexPatternAlertOnMatch,
       "siteContentMatchSize": siteContentMatchSize,
       "siteContentActualSize": siteContentActualSize,
       "siteContentSizeMatchFlag": siteContentSizeMatchFlag,
       "siteContentSizeAlertOnMatch": siteContentSizeAlertOnMatch,
       "siteURLContentPattern": siteURLContentPattern,
       "siteURLContentPatternMatchFlag": siteURLContentPatternMatchFlag,
       "siteURLContentPatternAlertOnMatch": siteURLContentPatternAlertOnMatch,
       "siteURLContentPatternProxy": siteURLContentPatternProxy,
       "siteURLContentPatternHTTPCode": siteURLContentPatternHTTPCode,
       "siteURLSize": siteURLSize,
       "siteURLSizeMatchFlag": siteURLSizeMatchFlag,
       "siteURLSizeAlertOnMatch": siteURLSizeAlertOnMatch,
       "siteURLSizeProxy": siteURLSizeProxy,
       "siteURLSizeHTTPCode": siteURLSizeHTTPCode,
       "siteFetchRegex": siteFetchRegex,
       "siteFetchRegexCompilationError": siteFetchRegexCompilationError,
       "siteFetchRegexMatchingError": siteFetchRegexMatchingError,
       "siteFetchRegexSubResult0": siteFetchRegexSubResult0,
       "siteFetchRegexSubResult1": siteFetchRegexSubResult1,
       "siteFetchRegexSubResult2": siteFetchRegexSubResult2,
       "siteFetchRegexSubResult3": siteFetchRegexSubResult3,
       "siteFetchRegexSubResult4": siteFetchRegexSubResult4,
       "siteFetchRegexSubResult5": siteFetchRegexSubResult5,
       "siteFetchRegexSubResult6": siteFetchRegexSubResult6,
       "siteFetchRegexSubResult7": siteFetchRegexSubResult7,
       "siteAppendRegexResultFrom": siteAppendRegexResultFrom,
       "siteAppendRegexResultFromIndex": siteAppendRegexResultFromIndex,
       "siteNumericalRegexSubMatch": siteNumericalRegexSubMatch,
       "siteNumericalPattern": siteNumericalPattern,
       "siteNumericalAlertOn": siteNumericalAlertOn,
       "siteFileTime": siteFileTime,
       "siteDateAgeRegexConstruct": siteDateAgeRegexConstruct,
       "siteDateAgePattern": siteDateAgePattern,
       "siteDateAgeAlertOn": siteDateAgeAlertOn,
       "siteTaskSuspendStart": siteTaskSuspendStart,
       "siteTaskSuspendEnd": siteTaskSuspendEnd,
       "siteStatusNormal": siteStatusNormal,
       "siteStatusWarning": siteStatusWarning,
       "siteStatusCritical": siteStatusCritical,
       "siteGroupStatusNormal": siteGroupStatusNormal,
       "siteGroupStatusWarning": siteGroupStatusWarning,
       "siteGroupStatusCritical": siteGroupStatusCritical,
       "siteReliability": siteReliability,
       "siteMTBWarnings": siteMTBWarnings,
       "siteMTTRWarnings": siteMTTRWarnings,
       "siteAccumulatedWarnings": siteAccumulatedWarnings,
       "siteMTBCriticals": siteMTBCriticals,
       "siteMTTRCriticals": siteMTTRCriticals,
       "siteAccumulatedCriticals": siteAccumulatedCriticals,
       "siteGroupReliability": siteGroupReliability,
       "siteGroupMTBWarnings": siteGroupMTBWarnings,
       "siteGroupMTTRWarnings": siteGroupMTTRWarnings,
       "siteGroupAccumulatedWarnings": siteGroupAccumulatedWarnings,
       "siteGroupMTBCriticals": siteGroupMTBCriticals,
       "siteGroupMTTRCriticals": siteGroupMTTRCriticals,
       "siteGroupAccumulatedCriticals": siteGroupAccumulatedCriticals,
       "siteLastRunRelativeTime": siteLastRunRelativeTime,
       "siteLastRunAbsTimeString": siteLastRunAbsTimeString,
       "siteNextRunRelativeTime": siteNextRunRelativeTime,
       "siteNextRunAbsTimeString": siteNextRunAbsTimeString,
       "siteFirstRun": siteFirstRun,
       "siteTotalTransfers": siteTotalTransfers,
       "siteTotalTransferVolume": siteTotalTransferVolume,
       "groupStatus": groupStatus,
       "proxyStatus": proxyStatus,
       "siteStatus": siteStatus,
       "subTaskID": subTaskID,
       "eventTime": eventTime,
       "siteTrapMessage": siteTrapMessage}
)
