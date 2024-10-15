# SNMP MIB module (WF-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WF-HTTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:47 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfHttpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfHttpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfHttp_ObjectIdentity = ObjectIdentity
wfHttp = _WfHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1)
)
_WfHttpSrv_ObjectIdentity = ObjectIdentity
wfHttpSrv = _WfHttpSrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1)
)


class _WfHttpSrvDelete_Type(Integer32):
    """Custom type wfHttpSrvDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfHttpSrvDelete_Type.__name__ = "Integer32"
_WfHttpSrvDelete_Object = MibScalar
wfHttpSrvDelete = _WfHttpSrvDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 1),
    _WfHttpSrvDelete_Type()
)
wfHttpSrvDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvDelete.setStatus("mandatory")


class _WfHttpSrvDisable_Type(Integer32):
    """Custom type wfHttpSrvDisable based on Integer32"""
    defaultValue = 1

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


_WfHttpSrvDisable_Type.__name__ = "Integer32"
_WfHttpSrvDisable_Object = MibScalar
wfHttpSrvDisable = _WfHttpSrvDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 2),
    _WfHttpSrvDisable_Type()
)
wfHttpSrvDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvDisable.setStatus("mandatory")


class _WfHttpSrvState_Type(Integer32):
    """Custom type wfHttpSrvState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfHttpSrvState_Type.__name__ = "Integer32"
_WfHttpSrvState_Object = MibScalar
wfHttpSrvState = _WfHttpSrvState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 3),
    _WfHttpSrvState_Type()
)
wfHttpSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSrvState.setStatus("mandatory")


class _WfHttpSrvPort_Type(Integer32):
    """Custom type wfHttpSrvPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_WfHttpSrvPort_Type.__name__ = "Integer32"
_WfHttpSrvPort_Object = MibScalar
wfHttpSrvPort = _WfHttpSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 4),
    _WfHttpSrvPort_Type()
)
wfHttpSrvPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvPort.setStatus("mandatory")


class _WfHttpSrvMaxCacheCount_Type(Integer32):
    """Custom type wfHttpSrvMaxCacheCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_WfHttpSrvMaxCacheCount_Type.__name__ = "Integer32"
_WfHttpSrvMaxCacheCount_Object = MibScalar
wfHttpSrvMaxCacheCount = _WfHttpSrvMaxCacheCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 5),
    _WfHttpSrvMaxCacheCount_Type()
)
wfHttpSrvMaxCacheCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvMaxCacheCount.setStatus("mandatory")


class _WfHttpSrvMaxCacheAge_Type(Integer32):
    """Custom type wfHttpSrvMaxCacheAge based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfHttpSrvMaxCacheAge_Type.__name__ = "Integer32"
_WfHttpSrvMaxCacheAge_Object = MibScalar
wfHttpSrvMaxCacheAge = _WfHttpSrvMaxCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 6),
    _WfHttpSrvMaxCacheAge_Type()
)
wfHttpSrvMaxCacheAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvMaxCacheAge.setStatus("mandatory")


class _WfHttpSrvAuthType_Type(Integer32):
    """Custom type wfHttpSrvAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("digest", 2))
    )


_WfHttpSrvAuthType_Type.__name__ = "Integer32"
_WfHttpSrvAuthType_Object = MibScalar
wfHttpSrvAuthType = _WfHttpSrvAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 7),
    _WfHttpSrvAuthType_Type()
)
wfHttpSrvAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvAuthType.setStatus("mandatory")
_WfHttpSrvHostName_Type = DisplayString
_WfHttpSrvHostName_Object = MibScalar
wfHttpSrvHostName = _WfHttpSrvHostName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 8),
    _WfHttpSrvHostName_Type()
)
wfHttpSrvHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvHostName.setStatus("mandatory")


class _WfHttpSrvHelpBaseUrl_Type(DisplayString):
    """Custom type wfHttpSrvHelpBaseUrl based on DisplayString"""
    defaultValue = OctetString("http://support.baynetworks.com/library/tpubs/")


_WfHttpSrvHelpBaseUrl_Object = MibScalar
wfHttpSrvHelpBaseUrl = _WfHttpSrvHelpBaseUrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 1, 9),
    _WfHttpSrvHelpBaseUrl_Type()
)
wfHttpSrvHelpBaseUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfHttpSrvHelpBaseUrl.setStatus("mandatory")
_WfHttpStatistics_ObjectIdentity = ObjectIdentity
wfHttpStatistics = _WfHttpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2)
)
_WfHttpSummary_ObjectIdentity = ObjectIdentity
wfHttpSummary = _WfHttpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1)
)
_WfHttpSummaryRequests_Type = Counter32
_WfHttpSummaryRequests_Object = MibScalar
wfHttpSummaryRequests = _WfHttpSummaryRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 1),
    _WfHttpSummaryRequests_Type()
)
wfHttpSummaryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryRequests.setStatus("mandatory")
_WfHttpSummaryRequestErrors_Type = Counter32
_WfHttpSummaryRequestErrors_Object = MibScalar
wfHttpSummaryRequestErrors = _WfHttpSummaryRequestErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 2),
    _WfHttpSummaryRequestErrors_Type()
)
wfHttpSummaryRequestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryRequestErrors.setStatus("mandatory")
_WfHttpSummaryRequestDiscards_Type = Counter32
_WfHttpSummaryRequestDiscards_Object = MibScalar
wfHttpSummaryRequestDiscards = _WfHttpSummaryRequestDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 3),
    _WfHttpSummaryRequestDiscards_Type()
)
wfHttpSummaryRequestDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryRequestDiscards.setStatus("mandatory")
_WfHttpSummaryResponses_Type = Counter32
_WfHttpSummaryResponses_Object = MibScalar
wfHttpSummaryResponses = _WfHttpSummaryResponses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 4),
    _WfHttpSummaryResponses_Type()
)
wfHttpSummaryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryResponses.setStatus("mandatory")
_WfHttpSummaryResponseErrors_Type = Counter32
_WfHttpSummaryResponseErrors_Object = MibScalar
wfHttpSummaryResponseErrors = _WfHttpSummaryResponseErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 5),
    _WfHttpSummaryResponseErrors_Type()
)
wfHttpSummaryResponseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryResponseErrors.setStatus("mandatory")
_WfHttpSummaryResponseDiscards_Type = Counter32
_WfHttpSummaryResponseDiscards_Object = MibScalar
wfHttpSummaryResponseDiscards = _WfHttpSummaryResponseDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 6),
    _WfHttpSummaryResponseDiscards_Type()
)
wfHttpSummaryResponseDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryResponseDiscards.setStatus("mandatory")
_WfHttpSummaryInUnknowns_Type = Counter32
_WfHttpSummaryInUnknowns_Object = MibScalar
wfHttpSummaryInUnknowns = _WfHttpSummaryInUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 7),
    _WfHttpSummaryInUnknowns_Type()
)
wfHttpSummaryInUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryInUnknowns.setStatus("mandatory")
_WfHttpSummaryInBytes_Type = Counter32
_WfHttpSummaryInBytes_Object = MibScalar
wfHttpSummaryInBytes = _WfHttpSummaryInBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 8),
    _WfHttpSummaryInBytes_Type()
)
wfHttpSummaryInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryInBytes.setStatus("mandatory")
_WfHttpSummaryOutBytes_Type = Counter32
_WfHttpSummaryOutBytes_Object = MibScalar
wfHttpSummaryOutBytes = _WfHttpSummaryOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 9),
    _WfHttpSummaryOutBytes_Type()
)
wfHttpSummaryOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryOutBytes.setStatus("mandatory")
_WfHttpSummaryTimeOuts_Type = Counter32
_WfHttpSummaryTimeOuts_Object = MibScalar
wfHttpSummaryTimeOuts = _WfHttpSummaryTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 10),
    _WfHttpSummaryTimeOuts_Type()
)
wfHttpSummaryTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryTimeOuts.setStatus("mandatory")
_WfHttpSummaryStartTime_Type = TimeTicks
_WfHttpSummaryStartTime_Object = MibScalar
wfHttpSummaryStartTime = _WfHttpSummaryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 1, 11),
    _WfHttpSummaryStartTime_Type()
)
wfHttpSummaryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpSummaryStartTime.setStatus("mandatory")
_WfHttpRequestTable_Object = MibTable
wfHttpRequestTable = _WfHttpRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfHttpRequestTable.setStatus("mandatory")
_WfHttpRequestEntry_Object = MibTableRow
wfHttpRequestEntry = _WfHttpRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1)
)
wfHttpRequestEntry.setIndexNames(
    (0, "WF-HTTP-MIB", "wfHttpRequestMethodIndex"),
)
if mibBuilder.loadTexts:
    wfHttpRequestEntry.setStatus("mandatory")


class _WfHttpRequestMethodIndex_Type(Integer32):
    """Custom type wfHttpRequestMethodIndex based on Integer32"""
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
        *(("delete", 7),
          ("get", 1),
          ("head", 2),
          ("options", 5),
          ("post", 4),
          ("put", 6),
          ("trace", 3))
    )


_WfHttpRequestMethodIndex_Type.__name__ = "Integer32"
_WfHttpRequestMethodIndex_Object = MibTableColumn
wfHttpRequestMethodIndex = _WfHttpRequestMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 1),
    _WfHttpRequestMethodIndex_Type()
)
wfHttpRequestMethodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpRequestMethodIndex.setStatus("mandatory")
_WfHttpRequestInCount_Type = Counter32
_WfHttpRequestInCount_Object = MibTableColumn
wfHttpRequestInCount = _WfHttpRequestInCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 2),
    _WfHttpRequestInCount_Type()
)
wfHttpRequestInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpRequestInCount.setStatus("mandatory")
_WfHttpRequestInLastTime_Type = TimeTicks
_WfHttpRequestInLastTime_Object = MibTableColumn
wfHttpRequestInLastTime = _WfHttpRequestInLastTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 3),
    _WfHttpRequestInLastTime_Type()
)
wfHttpRequestInLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpRequestInLastTime.setStatus("mandatory")
_WfHttpRequestOutCount_Type = Counter32
_WfHttpRequestOutCount_Object = MibTableColumn
wfHttpRequestOutCount = _WfHttpRequestOutCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 4),
    _WfHttpRequestOutCount_Type()
)
wfHttpRequestOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpRequestOutCount.setStatus("mandatory")
_WfHttpRequestOutLastTime_Type = TimeTicks
_WfHttpRequestOutLastTime_Object = MibTableColumn
wfHttpRequestOutLastTime = _WfHttpRequestOutLastTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 2, 1, 5),
    _WfHttpRequestOutLastTime_Type()
)
wfHttpRequestOutLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpRequestOutLastTime.setStatus("mandatory")
_WfHttpResponseTable_Object = MibTable
wfHttpResponseTable = _WfHttpResponseTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wfHttpResponseTable.setStatus("mandatory")
_WfHttpResponseEntry_Object = MibTableRow
wfHttpResponseEntry = _WfHttpResponseEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1)
)
wfHttpResponseEntry.setIndexNames(
    (0, "WF-HTTP-MIB", "wfHttpResponseStatusIndex"),
)
if mibBuilder.loadTexts:
    wfHttpResponseEntry.setStatus("mandatory")


class _WfHttpResponseStatusIndex_Type(Integer32):
    """Custom type wfHttpResponseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(200,
              201,
              202,
              204,
              301,
              302,
              304,
              400,
              401,
              403,
              404,
              500,
              501,
              502,
              503)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 202),
          ("bad-gateway", 502),
          ("bad-request", 400),
          ("created", 201),
          ("forbidden", 403),
          ("internal-server-error", 500),
          ("moved-permanently", 301),
          ("moved-temporarily", 302),
          ("no-content", 204),
          ("not-found", 404),
          ("not-implemented", 501),
          ("not-modified", 304),
          ("ok", 200),
          ("service-unavailable", 503),
          ("unauthorized", 401))
    )


_WfHttpResponseStatusIndex_Type.__name__ = "Integer32"
_WfHttpResponseStatusIndex_Object = MibTableColumn
wfHttpResponseStatusIndex = _WfHttpResponseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 1),
    _WfHttpResponseStatusIndex_Type()
)
wfHttpResponseStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpResponseStatusIndex.setStatus("mandatory")
_WfHttpResponseInCount_Type = Counter32
_WfHttpResponseInCount_Object = MibTableColumn
wfHttpResponseInCount = _WfHttpResponseInCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 2),
    _WfHttpResponseInCount_Type()
)
wfHttpResponseInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpResponseInCount.setStatus("mandatory")
_WfHttpResponseInLastTime_Type = TimeTicks
_WfHttpResponseInLastTime_Object = MibTableColumn
wfHttpResponseInLastTime = _WfHttpResponseInLastTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 3),
    _WfHttpResponseInLastTime_Type()
)
wfHttpResponseInLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpResponseInLastTime.setStatus("mandatory")
_WfHttpResponseOutCount_Type = Counter32
_WfHttpResponseOutCount_Object = MibTableColumn
wfHttpResponseOutCount = _WfHttpResponseOutCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 4),
    _WfHttpResponseOutCount_Type()
)
wfHttpResponseOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpResponseOutCount.setStatus("mandatory")
_WfHttpResponseOutLastTime_Type = TimeTicks
_WfHttpResponseOutLastTime_Object = MibTableColumn
wfHttpResponseOutLastTime = _WfHttpResponseOutLastTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 22, 1, 2, 3, 1, 5),
    _WfHttpResponseOutLastTime_Type()
)
wfHttpResponseOutLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfHttpResponseOutLastTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WF-HTTP-MIB",
    **{"wfHttp": wfHttp,
       "wfHttpSrv": wfHttpSrv,
       "wfHttpSrvDelete": wfHttpSrvDelete,
       "wfHttpSrvDisable": wfHttpSrvDisable,
       "wfHttpSrvState": wfHttpSrvState,
       "wfHttpSrvPort": wfHttpSrvPort,
       "wfHttpSrvMaxCacheCount": wfHttpSrvMaxCacheCount,
       "wfHttpSrvMaxCacheAge": wfHttpSrvMaxCacheAge,
       "wfHttpSrvAuthType": wfHttpSrvAuthType,
       "wfHttpSrvHostName": wfHttpSrvHostName,
       "wfHttpSrvHelpBaseUrl": wfHttpSrvHelpBaseUrl,
       "wfHttpStatistics": wfHttpStatistics,
       "wfHttpSummary": wfHttpSummary,
       "wfHttpSummaryRequests": wfHttpSummaryRequests,
       "wfHttpSummaryRequestErrors": wfHttpSummaryRequestErrors,
       "wfHttpSummaryRequestDiscards": wfHttpSummaryRequestDiscards,
       "wfHttpSummaryResponses": wfHttpSummaryResponses,
       "wfHttpSummaryResponseErrors": wfHttpSummaryResponseErrors,
       "wfHttpSummaryResponseDiscards": wfHttpSummaryResponseDiscards,
       "wfHttpSummaryInUnknowns": wfHttpSummaryInUnknowns,
       "wfHttpSummaryInBytes": wfHttpSummaryInBytes,
       "wfHttpSummaryOutBytes": wfHttpSummaryOutBytes,
       "wfHttpSummaryTimeOuts": wfHttpSummaryTimeOuts,
       "wfHttpSummaryStartTime": wfHttpSummaryStartTime,
       "wfHttpRequestTable": wfHttpRequestTable,
       "wfHttpRequestEntry": wfHttpRequestEntry,
       "wfHttpRequestMethodIndex": wfHttpRequestMethodIndex,
       "wfHttpRequestInCount": wfHttpRequestInCount,
       "wfHttpRequestInLastTime": wfHttpRequestInLastTime,
       "wfHttpRequestOutCount": wfHttpRequestOutCount,
       "wfHttpRequestOutLastTime": wfHttpRequestOutLastTime,
       "wfHttpResponseTable": wfHttpResponseTable,
       "wfHttpResponseEntry": wfHttpResponseEntry,
       "wfHttpResponseStatusIndex": wfHttpResponseStatusIndex,
       "wfHttpResponseInCount": wfHttpResponseInCount,
       "wfHttpResponseInLastTime": wfHttpResponseInLastTime,
       "wfHttpResponseOutCount": wfHttpResponseOutCount,
       "wfHttpResponseOutLastTime": wfHttpResponseOutLastTime}
)
