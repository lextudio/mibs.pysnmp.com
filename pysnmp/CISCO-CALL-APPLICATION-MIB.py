# SNMP MIB module (CISCO-CALL-APPLICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-APPLICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:45 2024
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

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoCallApplicationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146)
)
ciscoCallApplicationMIB.setRevisions(
        ("2003-05-13 00:01",
         "1999-09-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class URLStringOrNull(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class ServerNameString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCallApplicationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCallApplicationMIBObjects = _CiscoCallApplicationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1)
)
_CcapConf_ObjectIdentity = ObjectIdentity
ccapConf = _CcapConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1)
)
_CcapApplicationTable_Object = MibTable
ccapApplicationTable = _CcapApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ccapApplicationTable.setStatus("current")
_CcapApplicationEntry_Object = MibTableRow
ccapApplicationEntry = _CcapApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1)
)
ccapApplicationEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppName"),
)
if mibBuilder.loadTexts:
    ccapApplicationEntry.setStatus("current")


class _CcapAppName_Type(SnmpAdminString):
    """Custom type ccapAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CcapAppName_Type.__name__ = "SnmpAdminString"
_CcapAppName_Object = MibTableColumn
ccapAppName = _CcapAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 1),
    _CcapAppName_Type()
)
ccapAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppName.setStatus("current")
_CcapAppLocation_Type = URLStringOrNull
_CcapAppLocation_Object = MibTableColumn
ccapAppLocation = _CcapAppLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 2),
    _CcapAppLocation_Type()
)
ccapAppLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccapAppLocation.setStatus("current")


class _CcapAppLoadState_Type(Integer32):
    """Custom type ccapAppLoadState based on Integer32"""
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
        *(("builtIn", 1),
          ("loadFailed", 4),
          ("loaded", 3),
          ("loading", 2))
    )


_CcapAppLoadState_Type.__name__ = "Integer32"
_CcapAppLoadState_Object = MibTableColumn
ccapAppLoadState = _CcapAppLoadState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 3),
    _CcapAppLoadState_Type()
)
ccapAppLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppLoadState.setStatus("current")


class _CcapAppLoadFailReason_Type(Integer32):
    """Custom type ccapAppLoadFailReason based on Integer32"""
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
        *(("badSignature", 6),
          ("noPermission", 5),
          ("noSpace", 7),
          ("none", 1),
          ("notFound", 3),
          ("other", 2),
          ("timedOut", 4))
    )


_CcapAppLoadFailReason_Type.__name__ = "Integer32"
_CcapAppLoadFailReason_Object = MibTableColumn
ccapAppLoadFailReason = _CcapAppLoadFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 4),
    _CcapAppLoadFailReason_Type()
)
ccapAppLoadFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppLoadFailReason.setStatus("current")
_CcapAppDescr_Type = SnmpAdminString
_CcapAppDescr_Object = MibTableColumn
ccapAppDescr = _CcapAppDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 5),
    _CcapAppDescr_Type()
)
ccapAppDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccapAppDescr.setStatus("current")


class _CcapAppCallType_Type(OctetString):
    """Custom type ccapAppCallType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_CcapAppCallType_Type.__name__ = "OctetString"
_CcapAppCallType_Object = MibTableColumn
ccapAppCallType = _CcapAppCallType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 6),
    _CcapAppCallType_Type()
)
ccapAppCallType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccapAppCallType.setStatus("current")
_CcapAppRowStatus_Type = RowStatus
_CcapAppRowStatus_Object = MibTableColumn
ccapAppRowStatus = _CcapAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 7),
    _CcapAppRowStatus_Type()
)
ccapAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccapAppRowStatus.setStatus("current")
_CcapAppActiveInstances_Type = Gauge32
_CcapAppActiveInstances_Object = MibTableColumn
ccapAppActiveInstances = _CcapAppActiveInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 8),
    _CcapAppActiveInstances_Type()
)
ccapAppActiveInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppActiveInstances.setStatus("current")
_CcapAppEventLogging_Type = TruthValue
_CcapAppEventLogging_Object = MibTableColumn
ccapAppEventLogging = _CcapAppEventLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 9),
    _CcapAppEventLogging_Type()
)
ccapAppEventLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppEventLogging.setStatus("current")
_CcapAppPSTNInCallNowConn_Type = Gauge32
_CcapAppPSTNInCallNowConn_Object = MibTableColumn
ccapAppPSTNInCallNowConn = _CcapAppPSTNInCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 10),
    _CcapAppPSTNInCallNowConn_Type()
)
ccapAppPSTNInCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppPSTNInCallNowConn.setStatus("current")
_CcapAppPSTNOutCallNowConn_Type = Gauge32
_CcapAppPSTNOutCallNowConn_Object = MibTableColumn
ccapAppPSTNOutCallNowConn = _CcapAppPSTNOutCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 11),
    _CcapAppPSTNOutCallNowConn_Type()
)
ccapAppPSTNOutCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppPSTNOutCallNowConn.setStatus("current")
_CcapAppIPInCallNowConn_Type = Gauge32
_CcapAppIPInCallNowConn_Object = MibTableColumn
ccapAppIPInCallNowConn = _CcapAppIPInCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 12),
    _CcapAppIPInCallNowConn_Type()
)
ccapAppIPInCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIPInCallNowConn.setStatus("current")
_CcapAppIPOutCallNowConn_Type = Gauge32
_CcapAppIPOutCallNowConn_Object = MibTableColumn
ccapAppIPOutCallNowConn = _CcapAppIPOutCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 13),
    _CcapAppIPOutCallNowConn_Type()
)
ccapAppIPOutCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIPOutCallNowConn.setStatus("current")
_CcapAppPlaceCallInProgress_Type = Gauge32
_CcapAppPlaceCallInProgress_Object = MibTableColumn
ccapAppPlaceCallInProgress = _CcapAppPlaceCallInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 14),
    _CcapAppPlaceCallInProgress_Type()
)
ccapAppPlaceCallInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppPlaceCallInProgress.setStatus("current")
_CcapAppHandoffInProgress_Type = Gauge32
_CcapAppHandoffInProgress_Object = MibTableColumn
ccapAppHandoffInProgress = _CcapAppHandoffInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 15),
    _CcapAppHandoffInProgress_Type()
)
ccapAppHandoffInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppHandoffInProgress.setStatus("current")
_CcapAppPromptPlayActive_Type = Gauge32
_CcapAppPromptPlayActive_Object = MibTableColumn
ccapAppPromptPlayActive = _CcapAppPromptPlayActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 16),
    _CcapAppPromptPlayActive_Type()
)
ccapAppPromptPlayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppPromptPlayActive.setStatus("current")
_CcapAppRecordingActive_Type = Gauge32
_CcapAppRecordingActive_Object = MibTableColumn
ccapAppRecordingActive = _CcapAppRecordingActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 17),
    _CcapAppRecordingActive_Type()
)
ccapAppRecordingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppRecordingActive.setStatus("current")
_CcapAppTTSActive_Type = Gauge32
_CcapAppTTSActive_Object = MibTableColumn
ccapAppTTSActive = _CcapAppTTSActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 1, 1, 1, 18),
    _CcapAppTTSActive_Type()
)
ccapAppTTSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTTSActive.setStatus("current")
_CcapAppTypeHisStat_ObjectIdentity = ObjectIdentity
ccapAppTypeHisStat = _CcapAppTypeHisStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2)
)
_CcapAppTypeHistoryTable_Object = MibTable
ccapAppTypeHistoryTable = _CcapAppTypeHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ccapAppTypeHistoryTable.setStatus("current")
_CcapAppTypeHistoryEntry_Object = MibTableRow
ccapAppTypeHistoryEntry = _CcapAppTypeHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1)
)
ccapAppTypeHistoryEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppName"),
)
if mibBuilder.loadTexts:
    ccapAppTypeHistoryEntry.setStatus("current")
_CcapAppTypeHisEvtLogging_Type = TruthValue
_CcapAppTypeHisEvtLogging_Object = MibTableColumn
ccapAppTypeHisEvtLogging = _CcapAppTypeHisEvtLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 1),
    _CcapAppTypeHisEvtLogging_Type()
)
ccapAppTypeHisEvtLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisEvtLogging.setStatus("current")
_CcapAppTypeHisLastResetTime_Type = TimeStamp
_CcapAppTypeHisLastResetTime_Object = MibTableColumn
ccapAppTypeHisLastResetTime = _CcapAppTypeHisLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 2),
    _CcapAppTypeHisLastResetTime_Type()
)
ccapAppTypeHisLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisLastResetTime.setStatus("current")
_CcapAppTypeHisPSTNInCallSetupInd_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallSetupInd_Object = MibTableColumn
ccapAppTypeHisPSTNInCallSetupInd = _CcapAppTypeHisPSTNInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 3),
    _CcapAppTypeHisPSTNInCallSetupInd_Type()
)
ccapAppTypeHisPSTNInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallSetupInd.setStatus("current")
_CcapAppTypeHisPSTNInCallTotConn_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallTotConn_Object = MibTableColumn
ccapAppTypeHisPSTNInCallTotConn = _CcapAppTypeHisPSTNInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 4),
    _CcapAppTypeHisPSTNInCallTotConn_Type()
)
ccapAppTypeHisPSTNInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallTotConn.setStatus("current")
_CcapAppTypeHisPSTNInCallHandedOut_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallHandedOut_Object = MibTableColumn
ccapAppTypeHisPSTNInCallHandedOut = _CcapAppTypeHisPSTNInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 5),
    _CcapAppTypeHisPSTNInCallHandedOut_Type()
)
ccapAppTypeHisPSTNInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallHandedOut.setStatus("current")
_CcapAppTypeHisPSTNInCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallHandOutRet_Object = MibTableColumn
ccapAppTypeHisPSTNInCallHandOutRet = _CcapAppTypeHisPSTNInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 6),
    _CcapAppTypeHisPSTNInCallHandOutRet_Type()
)
ccapAppTypeHisPSTNInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallHandOutRet.setStatus("current")
_CcapAppTypeHisPSTNInCallInHandoff_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallInHandoff_Object = MibTableColumn
ccapAppTypeHisPSTNInCallInHandoff = _CcapAppTypeHisPSTNInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 7),
    _CcapAppTypeHisPSTNInCallInHandoff_Type()
)
ccapAppTypeHisPSTNInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallInHandoff.setStatus("current")
_CcapAppTypeHisPSTNInCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallInHandoffRet_Object = MibTableColumn
ccapAppTypeHisPSTNInCallInHandoffRet = _CcapAppTypeHisPSTNInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 8),
    _CcapAppTypeHisPSTNInCallInHandoffRet_Type()
)
ccapAppTypeHisPSTNInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallInHandoffRet.setStatus("current")
_CcapAppTypeHisPSTNInCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallDiscNormal_Object = MibTableColumn
ccapAppTypeHisPSTNInCallDiscNormal = _CcapAppTypeHisPSTNInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 9),
    _CcapAppTypeHisPSTNInCallDiscNormal_Type()
)
ccapAppTypeHisPSTNInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallDiscNormal.setStatus("current")
_CcapAppTypeHisPSTNInCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallDiscUsrErr_Object = MibTableColumn
ccapAppTypeHisPSTNInCallDiscUsrErr = _CcapAppTypeHisPSTNInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 10),
    _CcapAppTypeHisPSTNInCallDiscUsrErr_Type()
)
ccapAppTypeHisPSTNInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallDiscUsrErr.setStatus("current")
_CcapAppTypeHisPSTNInCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNInCallDiscSysErr_Object = MibTableColumn
ccapAppTypeHisPSTNInCallDiscSysErr = _CcapAppTypeHisPSTNInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 11),
    _CcapAppTypeHisPSTNInCallDiscSysErr_Type()
)
ccapAppTypeHisPSTNInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNInCallDiscSysErr.setStatus("current")
_CcapAppTypeHisPSTNOutCallSetupReq_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallSetupReq_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallSetupReq = _CcapAppTypeHisPSTNOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 12),
    _CcapAppTypeHisPSTNOutCallSetupReq_Type()
)
ccapAppTypeHisPSTNOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallSetupReq.setStatus("current")
_CcapAppTypeHisPSTNOutCallTotConn_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallTotConn_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallTotConn = _CcapAppTypeHisPSTNOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 13),
    _CcapAppTypeHisPSTNOutCallTotConn_Type()
)
ccapAppTypeHisPSTNOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallTotConn.setStatus("current")
_CcapAppTypeHisPSTNOutCallHandedOut_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallHandedOut_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallHandedOut = _CcapAppTypeHisPSTNOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 14),
    _CcapAppTypeHisPSTNOutCallHandedOut_Type()
)
ccapAppTypeHisPSTNOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallHandedOut.setStatus("current")
_CcapAppTypeHisPSTNOutCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallHandOutRet_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallHandOutRet = _CcapAppTypeHisPSTNOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 15),
    _CcapAppTypeHisPSTNOutCallHandOutRet_Type()
)
ccapAppTypeHisPSTNOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallHandOutRet.setStatus("current")
_CcapAppTypeHisPSTNOutCallInHandoff_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallInHandoff_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallInHandoff = _CcapAppTypeHisPSTNOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 16),
    _CcapAppTypeHisPSTNOutCallInHandoff_Type()
)
ccapAppTypeHisPSTNOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallInHandoff.setStatus("current")
_CcapAppTypeHisPSTNOutCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallInHandoffRet_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallInHandoffRet = _CcapAppTypeHisPSTNOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 17),
    _CcapAppTypeHisPSTNOutCallInHandoffRet_Type()
)
ccapAppTypeHisPSTNOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallInHandoffRet.setStatus("current")
_CcapAppTypeHisPSTNOutCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallDiscNormal_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallDiscNormal = _CcapAppTypeHisPSTNOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 18),
    _CcapAppTypeHisPSTNOutCallDiscNormal_Type()
)
ccapAppTypeHisPSTNOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallDiscNormal.setStatus("current")
_CcapAppTypeHisPSTNOutCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallDiscUsrErr_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallDiscUsrErr = _CcapAppTypeHisPSTNOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 19),
    _CcapAppTypeHisPSTNOutCallDiscUsrErr_Type()
)
ccapAppTypeHisPSTNOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallDiscUsrErr.setStatus("current")
_CcapAppTypeHisPSTNOutCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppTypeHisPSTNOutCallDiscSysErr_Object = MibTableColumn
ccapAppTypeHisPSTNOutCallDiscSysErr = _CcapAppTypeHisPSTNOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 20),
    _CcapAppTypeHisPSTNOutCallDiscSysErr_Type()
)
ccapAppTypeHisPSTNOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPSTNOutCallDiscSysErr.setStatus("current")
_CcapAppTypeHisIPInCallSetupInd_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallSetupInd_Object = MibTableColumn
ccapAppTypeHisIPInCallSetupInd = _CcapAppTypeHisIPInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 21),
    _CcapAppTypeHisIPInCallSetupInd_Type()
)
ccapAppTypeHisIPInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallSetupInd.setStatus("current")
_CcapAppTypeHisIPInCallTotConn_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallTotConn_Object = MibTableColumn
ccapAppTypeHisIPInCallTotConn = _CcapAppTypeHisIPInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 22),
    _CcapAppTypeHisIPInCallTotConn_Type()
)
ccapAppTypeHisIPInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallTotConn.setStatus("current")
_CcapAppTypeHisIPInCallHandedOut_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallHandedOut_Object = MibTableColumn
ccapAppTypeHisIPInCallHandedOut = _CcapAppTypeHisIPInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 23),
    _CcapAppTypeHisIPInCallHandedOut_Type()
)
ccapAppTypeHisIPInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallHandedOut.setStatus("current")
_CcapAppTypeHisIPInCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallHandOutRet_Object = MibTableColumn
ccapAppTypeHisIPInCallHandOutRet = _CcapAppTypeHisIPInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 24),
    _CcapAppTypeHisIPInCallHandOutRet_Type()
)
ccapAppTypeHisIPInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallHandOutRet.setStatus("current")
_CcapAppTypeHisIPInCallInHandoff_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallInHandoff_Object = MibTableColumn
ccapAppTypeHisIPInCallInHandoff = _CcapAppTypeHisIPInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 25),
    _CcapAppTypeHisIPInCallInHandoff_Type()
)
ccapAppTypeHisIPInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallInHandoff.setStatus("current")
_CcapAppTypeHisIPInCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallInHandoffRet_Object = MibTableColumn
ccapAppTypeHisIPInCallInHandoffRet = _CcapAppTypeHisIPInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 26),
    _CcapAppTypeHisIPInCallInHandoffRet_Type()
)
ccapAppTypeHisIPInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallInHandoffRet.setStatus("current")
_CcapAppTypeHisIPInCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallDiscNormal_Object = MibTableColumn
ccapAppTypeHisIPInCallDiscNormal = _CcapAppTypeHisIPInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 27),
    _CcapAppTypeHisIPInCallDiscNormal_Type()
)
ccapAppTypeHisIPInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallDiscNormal.setStatus("current")
_CcapAppTypeHisIPInCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallDiscUsrErr_Object = MibTableColumn
ccapAppTypeHisIPInCallDiscUsrErr = _CcapAppTypeHisIPInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 28),
    _CcapAppTypeHisIPInCallDiscUsrErr_Type()
)
ccapAppTypeHisIPInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallDiscUsrErr.setStatus("current")
_CcapAppTypeHisIPInCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppTypeHisIPInCallDiscSysErr_Object = MibTableColumn
ccapAppTypeHisIPInCallDiscSysErr = _CcapAppTypeHisIPInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 29),
    _CcapAppTypeHisIPInCallDiscSysErr_Type()
)
ccapAppTypeHisIPInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPInCallDiscSysErr.setStatus("current")
_CcapAppTypeHisIPOutCallSetupReq_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallSetupReq_Object = MibTableColumn
ccapAppTypeHisIPOutCallSetupReq = _CcapAppTypeHisIPOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 30),
    _CcapAppTypeHisIPOutCallSetupReq_Type()
)
ccapAppTypeHisIPOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallSetupReq.setStatus("current")
_CcapAppTypeHisIPOutCallTotConn_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallTotConn_Object = MibTableColumn
ccapAppTypeHisIPOutCallTotConn = _CcapAppTypeHisIPOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 31),
    _CcapAppTypeHisIPOutCallTotConn_Type()
)
ccapAppTypeHisIPOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallTotConn.setStatus("current")
_CcapAppTypeHisIPOutCallHandedOut_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallHandedOut_Object = MibTableColumn
ccapAppTypeHisIPOutCallHandedOut = _CcapAppTypeHisIPOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 32),
    _CcapAppTypeHisIPOutCallHandedOut_Type()
)
ccapAppTypeHisIPOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallHandedOut.setStatus("current")
_CcapAppTypeHisIPOutCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallHandOutRet_Object = MibTableColumn
ccapAppTypeHisIPOutCallHandOutRet = _CcapAppTypeHisIPOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 33),
    _CcapAppTypeHisIPOutCallHandOutRet_Type()
)
ccapAppTypeHisIPOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallHandOutRet.setStatus("current")
_CcapAppTypeHisIPOutCallInHandoff_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallInHandoff_Object = MibTableColumn
ccapAppTypeHisIPOutCallInHandoff = _CcapAppTypeHisIPOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 34),
    _CcapAppTypeHisIPOutCallInHandoff_Type()
)
ccapAppTypeHisIPOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallInHandoff.setStatus("current")
_CcapAppTypeHisIPOutCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallInHandoffRet_Object = MibTableColumn
ccapAppTypeHisIPOutCallInHandoffRet = _CcapAppTypeHisIPOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 35),
    _CcapAppTypeHisIPOutCallInHandoffRet_Type()
)
ccapAppTypeHisIPOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallInHandoffRet.setStatus("current")
_CcapAppTypeHisIPOutCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallDiscNormal_Object = MibTableColumn
ccapAppTypeHisIPOutCallDiscNormal = _CcapAppTypeHisIPOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 36),
    _CcapAppTypeHisIPOutCallDiscNormal_Type()
)
ccapAppTypeHisIPOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallDiscNormal.setStatus("current")
_CcapAppTypeHisIPOutCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallDiscUsrErr_Object = MibTableColumn
ccapAppTypeHisIPOutCallDiscUsrErr = _CcapAppTypeHisIPOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 37),
    _CcapAppTypeHisIPOutCallDiscUsrErr_Type()
)
ccapAppTypeHisIPOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallDiscUsrErr.setStatus("current")
_CcapAppTypeHisIPOutCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppTypeHisIPOutCallDiscSysErr_Object = MibTableColumn
ccapAppTypeHisIPOutCallDiscSysErr = _CcapAppTypeHisIPOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 38),
    _CcapAppTypeHisIPOutCallDiscSysErr_Type()
)
ccapAppTypeHisIPOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisIPOutCallDiscSysErr.setStatus("current")
_CcapAppTypeHisPlaceCallAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisPlaceCallAttempts_Object = MibTableColumn
ccapAppTypeHisPlaceCallAttempts = _CcapAppTypeHisPlaceCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 39),
    _CcapAppTypeHisPlaceCallAttempts_Type()
)
ccapAppTypeHisPlaceCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPlaceCallAttempts.setStatus("current")
_CcapAppTypeHisPlaceCallSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisPlaceCallSuccess_Object = MibTableColumn
ccapAppTypeHisPlaceCallSuccess = _CcapAppTypeHisPlaceCallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 40),
    _CcapAppTypeHisPlaceCallSuccess_Type()
)
ccapAppTypeHisPlaceCallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPlaceCallSuccess.setStatus("current")
_CcapAppTypeHisPlaceCallFailure_Type = ZeroBasedCounter32
_CcapAppTypeHisPlaceCallFailure_Object = MibTableColumn
ccapAppTypeHisPlaceCallFailure = _CcapAppTypeHisPlaceCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 41),
    _CcapAppTypeHisPlaceCallFailure_Type()
)
ccapAppTypeHisPlaceCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPlaceCallFailure.setStatus("current")
_CcapAppTypeHisInHandoffCallback_Type = ZeroBasedCounter32
_CcapAppTypeHisInHandoffCallback_Object = MibTableColumn
ccapAppTypeHisInHandoffCallback = _CcapAppTypeHisInHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 42),
    _CcapAppTypeHisInHandoffCallback_Type()
)
ccapAppTypeHisInHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisInHandoffCallback.setStatus("current")
_CcapAppTypeHisInHandoffCallbackRet_Type = ZeroBasedCounter32
_CcapAppTypeHisInHandoffCallbackRet_Object = MibTableColumn
ccapAppTypeHisInHandoffCallbackRet = _CcapAppTypeHisInHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 43),
    _CcapAppTypeHisInHandoffCallbackRet_Type()
)
ccapAppTypeHisInHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisInHandoffCallbackRet.setStatus("current")
_CcapAppTypeHisInHandoffNoCallback_Type = ZeroBasedCounter32
_CcapAppTypeHisInHandoffNoCallback_Object = MibTableColumn
ccapAppTypeHisInHandoffNoCallback = _CcapAppTypeHisInHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 44),
    _CcapAppTypeHisInHandoffNoCallback_Type()
)
ccapAppTypeHisInHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisInHandoffNoCallback.setStatus("current")
_CcapAppTypeHisOutHandoffCallback_Type = ZeroBasedCounter32
_CcapAppTypeHisOutHandoffCallback_Object = MibTableColumn
ccapAppTypeHisOutHandoffCallback = _CcapAppTypeHisOutHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 45),
    _CcapAppTypeHisOutHandoffCallback_Type()
)
ccapAppTypeHisOutHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisOutHandoffCallback.setStatus("current")
_CcapAppTypeHisOutHandoffCallbackRet_Type = ZeroBasedCounter32
_CcapAppTypeHisOutHandoffCallbackRet_Object = MibTableColumn
ccapAppTypeHisOutHandoffCallbackRet = _CcapAppTypeHisOutHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 46),
    _CcapAppTypeHisOutHandoffCallbackRet_Type()
)
ccapAppTypeHisOutHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisOutHandoffCallbackRet.setStatus("current")
_CcapAppTypeHisOutHandoffNoCallback_Type = ZeroBasedCounter32
_CcapAppTypeHisOutHandoffNoCallback_Object = MibTableColumn
ccapAppTypeHisOutHandoffNoCallback = _CcapAppTypeHisOutHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 47),
    _CcapAppTypeHisOutHandoffNoCallback_Type()
)
ccapAppTypeHisOutHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisOutHandoffNoCallback.setStatus("current")
_CcapAppTypeHisOutHandofffailures_Type = ZeroBasedCounter32
_CcapAppTypeHisOutHandofffailures_Object = MibTableColumn
ccapAppTypeHisOutHandofffailures = _CcapAppTypeHisOutHandofffailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 48),
    _CcapAppTypeHisOutHandofffailures_Type()
)
ccapAppTypeHisOutHandofffailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisOutHandofffailures.setStatus("current")
_CcapAppTypeHisDocumentReadAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentReadAttempts_Object = MibTableColumn
ccapAppTypeHisDocumentReadAttempts = _CcapAppTypeHisDocumentReadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 49),
    _CcapAppTypeHisDocumentReadAttempts_Type()
)
ccapAppTypeHisDocumentReadAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentReadAttempts.setStatus("current")
_CcapAppTypeHisDocumentReadSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentReadSuccess_Object = MibTableColumn
ccapAppTypeHisDocumentReadSuccess = _CcapAppTypeHisDocumentReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 50),
    _CcapAppTypeHisDocumentReadSuccess_Type()
)
ccapAppTypeHisDocumentReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentReadSuccess.setStatus("current")
_CcapAppTypeHisDocumentReadFailures_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentReadFailures_Object = MibTableColumn
ccapAppTypeHisDocumentReadFailures = _CcapAppTypeHisDocumentReadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 51),
    _CcapAppTypeHisDocumentReadFailures_Type()
)
ccapAppTypeHisDocumentReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentReadFailures.setStatus("current")
_CcapAppTypeHisDocumentParseErrors_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentParseErrors_Object = MibTableColumn
ccapAppTypeHisDocumentParseErrors = _CcapAppTypeHisDocumentParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 52),
    _CcapAppTypeHisDocumentParseErrors_Type()
)
ccapAppTypeHisDocumentParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentParseErrors.setStatus("current")
_CcapAppTypeHisDocumentWriteAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentWriteAttempts_Object = MibTableColumn
ccapAppTypeHisDocumentWriteAttempts = _CcapAppTypeHisDocumentWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 53),
    _CcapAppTypeHisDocumentWriteAttempts_Type()
)
ccapAppTypeHisDocumentWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentWriteAttempts.setStatus("current")
_CcapAppTypeHisDocumentWriteSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentWriteSuccess_Object = MibTableColumn
ccapAppTypeHisDocumentWriteSuccess = _CcapAppTypeHisDocumentWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 54),
    _CcapAppTypeHisDocumentWriteSuccess_Type()
)
ccapAppTypeHisDocumentWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentWriteSuccess.setStatus("current")
_CcapAppTypeHisDocumentWriteFailures_Type = ZeroBasedCounter32
_CcapAppTypeHisDocumentWriteFailures_Object = MibTableColumn
ccapAppTypeHisDocumentWriteFailures = _CcapAppTypeHisDocumentWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 55),
    _CcapAppTypeHisDocumentWriteFailures_Type()
)
ccapAppTypeHisDocumentWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDocumentWriteFailures.setStatus("current")
_CcapAppTypeHisDTMFAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFAttempts_Object = MibTableColumn
ccapAppTypeHisDTMFAttempts = _CcapAppTypeHisDTMFAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 56),
    _CcapAppTypeHisDTMFAttempts_Type()
)
ccapAppTypeHisDTMFAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFAttempts.setStatus("current")
_CcapAppTypeHisDTMFAborted_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFAborted_Object = MibTableColumn
ccapAppTypeHisDTMFAborted = _CcapAppTypeHisDTMFAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 57),
    _CcapAppTypeHisDTMFAborted_Type()
)
ccapAppTypeHisDTMFAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFAborted.setStatus("current")
_CcapAppTypeHisDTMFNoMatch_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFNoMatch_Object = MibTableColumn
ccapAppTypeHisDTMFNoMatch = _CcapAppTypeHisDTMFNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 58),
    _CcapAppTypeHisDTMFNoMatch_Type()
)
ccapAppTypeHisDTMFNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFNoMatch.setStatus("current")
_CcapAppTypeHisDTMFNoInput_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFNoInput_Object = MibTableColumn
ccapAppTypeHisDTMFNoInput = _CcapAppTypeHisDTMFNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 59),
    _CcapAppTypeHisDTMFNoInput_Type()
)
ccapAppTypeHisDTMFNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFNoInput.setStatus("current")
_CcapAppTypeHisDTMFMatch_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFMatch_Object = MibTableColumn
ccapAppTypeHisDTMFMatch = _CcapAppTypeHisDTMFMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 60),
    _CcapAppTypeHisDTMFMatch_Type()
)
ccapAppTypeHisDTMFMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFMatch.setStatus("current")
_CcapAppTypeHisDTMFLongPound_Type = ZeroBasedCounter32
_CcapAppTypeHisDTMFLongPound_Object = MibTableColumn
ccapAppTypeHisDTMFLongPound = _CcapAppTypeHisDTMFLongPound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 61),
    _CcapAppTypeHisDTMFLongPound_Type()
)
ccapAppTypeHisDTMFLongPound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisDTMFLongPound.setStatus("current")
_CcapAppTypeHisASRAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisASRAttempts_Object = MibTableColumn
ccapAppTypeHisASRAttempts = _CcapAppTypeHisASRAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 62),
    _CcapAppTypeHisASRAttempts_Type()
)
ccapAppTypeHisASRAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASRAttempts.setStatus("current")
_CcapAppTypeHisASRAborted_Type = ZeroBasedCounter32
_CcapAppTypeHisASRAborted_Object = MibTableColumn
ccapAppTypeHisASRAborted = _CcapAppTypeHisASRAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 63),
    _CcapAppTypeHisASRAborted_Type()
)
ccapAppTypeHisASRAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASRAborted.setStatus("current")
_CcapAppTypeHisASRNoMatch_Type = ZeroBasedCounter32
_CcapAppTypeHisASRNoMatch_Object = MibTableColumn
ccapAppTypeHisASRNoMatch = _CcapAppTypeHisASRNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 64),
    _CcapAppTypeHisASRNoMatch_Type()
)
ccapAppTypeHisASRNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASRNoMatch.setStatus("current")
_CcapAppTypeHisASRNoInput_Type = ZeroBasedCounter32
_CcapAppTypeHisASRNoInput_Object = MibTableColumn
ccapAppTypeHisASRNoInput = _CcapAppTypeHisASRNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 65),
    _CcapAppTypeHisASRNoInput_Type()
)
ccapAppTypeHisASRNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASRNoInput.setStatus("current")
_CcapAppTypeHisASRMatch_Type = ZeroBasedCounter32
_CcapAppTypeHisASRMatch_Object = MibTableColumn
ccapAppTypeHisASRMatch = _CcapAppTypeHisASRMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 66),
    _CcapAppTypeHisASRMatch_Type()
)
ccapAppTypeHisASRMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASRMatch.setStatus("current")
_CcapAppTypeHisAAAAuthenticateFailure_Type = ZeroBasedCounter32
_CcapAppTypeHisAAAAuthenticateFailure_Object = MibTableColumn
ccapAppTypeHisAAAAuthenticateFailure = _CcapAppTypeHisAAAAuthenticateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 67),
    _CcapAppTypeHisAAAAuthenticateFailure_Type()
)
ccapAppTypeHisAAAAuthenticateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisAAAAuthenticateFailure.setStatus("current")
_CcapAppTypeHisAAAAuthenticateSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisAAAAuthenticateSuccess_Object = MibTableColumn
ccapAppTypeHisAAAAuthenticateSuccess = _CcapAppTypeHisAAAAuthenticateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 68),
    _CcapAppTypeHisAAAAuthenticateSuccess_Type()
)
ccapAppTypeHisAAAAuthenticateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisAAAAuthenticateSuccess.setStatus("current")
_CcapAppTypeHisAAAAuthorizeFailure_Type = ZeroBasedCounter32
_CcapAppTypeHisAAAAuthorizeFailure_Object = MibTableColumn
ccapAppTypeHisAAAAuthorizeFailure = _CcapAppTypeHisAAAAuthorizeFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 69),
    _CcapAppTypeHisAAAAuthorizeFailure_Type()
)
ccapAppTypeHisAAAAuthorizeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisAAAAuthorizeFailure.setStatus("current")
_CcapAppTypeHisAAAAuthorizeSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisAAAAuthorizeSuccess_Object = MibTableColumn
ccapAppTypeHisAAAAuthorizeSuccess = _CcapAppTypeHisAAAAuthorizeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 70),
    _CcapAppTypeHisAAAAuthorizeSuccess_Type()
)
ccapAppTypeHisAAAAuthorizeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisAAAAuthorizeSuccess.setStatus("current")
_CcapAppTypeHisASNLSubscriptionsSent_Type = ZeroBasedCounter32
_CcapAppTypeHisASNLSubscriptionsSent_Object = MibTableColumn
ccapAppTypeHisASNLSubscriptionsSent = _CcapAppTypeHisASNLSubscriptionsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 71),
    _CcapAppTypeHisASNLSubscriptionsSent_Type()
)
ccapAppTypeHisASNLSubscriptionsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASNLSubscriptionsSent.setStatus("current")
_CcapAppTypeHisASNLSubscriptionsSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisASNLSubscriptionsSuccess_Object = MibTableColumn
ccapAppTypeHisASNLSubscriptionsSuccess = _CcapAppTypeHisASNLSubscriptionsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 72),
    _CcapAppTypeHisASNLSubscriptionsSuccess_Type()
)
ccapAppTypeHisASNLSubscriptionsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASNLSubscriptionsSuccess.setStatus("current")
_CcapAppTypeHisASNLSubscriptionsFailed_Type = ZeroBasedCounter32
_CcapAppTypeHisASNLSubscriptionsFailed_Object = MibTableColumn
ccapAppTypeHisASNLSubscriptionsFailed = _CcapAppTypeHisASNLSubscriptionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 73),
    _CcapAppTypeHisASNLSubscriptionsFailed_Type()
)
ccapAppTypeHisASNLSubscriptionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASNLSubscriptionsFailed.setStatus("current")
_CcapAppTypeHisASNLNotifReceived_Type = ZeroBasedCounter32
_CcapAppTypeHisASNLNotifReceived_Object = MibTableColumn
ccapAppTypeHisASNLNotifReceived = _CcapAppTypeHisASNLNotifReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 74),
    _CcapAppTypeHisASNLNotifReceived_Type()
)
ccapAppTypeHisASNLNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisASNLNotifReceived.setStatus("current")
_CcapAppTypeHisPromptPlayAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisPromptPlayAttempts_Object = MibTableColumn
ccapAppTypeHisPromptPlayAttempts = _CcapAppTypeHisPromptPlayAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 75),
    _CcapAppTypeHisPromptPlayAttempts_Type()
)
ccapAppTypeHisPromptPlayAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPromptPlayAttempts.setStatus("current")
_CcapAppTypeHisPromptPlaySuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisPromptPlaySuccess_Object = MibTableColumn
ccapAppTypeHisPromptPlaySuccess = _CcapAppTypeHisPromptPlaySuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 76),
    _CcapAppTypeHisPromptPlaySuccess_Type()
)
ccapAppTypeHisPromptPlaySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPromptPlaySuccess.setStatus("current")
_CcapAppTypeHisPromptPlayFailed_Type = ZeroBasedCounter32
_CcapAppTypeHisPromptPlayFailed_Object = MibTableColumn
ccapAppTypeHisPromptPlayFailed = _CcapAppTypeHisPromptPlayFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 77),
    _CcapAppTypeHisPromptPlayFailed_Type()
)
ccapAppTypeHisPromptPlayFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPromptPlayFailed.setStatus("current")
_CcapAppTypeHisPromptPlayDuration_Type = ZeroBasedCounter32
_CcapAppTypeHisPromptPlayDuration_Object = MibTableColumn
ccapAppTypeHisPromptPlayDuration = _CcapAppTypeHisPromptPlayDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 78),
    _CcapAppTypeHisPromptPlayDuration_Type()
)
ccapAppTypeHisPromptPlayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisPromptPlayDuration.setStatus("current")
_CcapAppTypeHisRecordingAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisRecordingAttempts_Object = MibTableColumn
ccapAppTypeHisRecordingAttempts = _CcapAppTypeHisRecordingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 79),
    _CcapAppTypeHisRecordingAttempts_Type()
)
ccapAppTypeHisRecordingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisRecordingAttempts.setStatus("current")
_CcapAppTypeHisRecordingSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisRecordingSuccess_Object = MibTableColumn
ccapAppTypeHisRecordingSuccess = _CcapAppTypeHisRecordingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 80),
    _CcapAppTypeHisRecordingSuccess_Type()
)
ccapAppTypeHisRecordingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisRecordingSuccess.setStatus("current")
_CcapAppTypeHisRecordingFailed_Type = ZeroBasedCounter32
_CcapAppTypeHisRecordingFailed_Object = MibTableColumn
ccapAppTypeHisRecordingFailed = _CcapAppTypeHisRecordingFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 81),
    _CcapAppTypeHisRecordingFailed_Type()
)
ccapAppTypeHisRecordingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisRecordingFailed.setStatus("current")
_CcapAppTypeHisRecordingDuration_Type = ZeroBasedCounter32
_CcapAppTypeHisRecordingDuration_Object = MibTableColumn
ccapAppTypeHisRecordingDuration = _CcapAppTypeHisRecordingDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 82),
    _CcapAppTypeHisRecordingDuration_Type()
)
ccapAppTypeHisRecordingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisRecordingDuration.setStatus("current")
_CcapAppTypeHisTTSAttempts_Type = ZeroBasedCounter32
_CcapAppTypeHisTTSAttempts_Object = MibTableColumn
ccapAppTypeHisTTSAttempts = _CcapAppTypeHisTTSAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 83),
    _CcapAppTypeHisTTSAttempts_Type()
)
ccapAppTypeHisTTSAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisTTSAttempts.setStatus("current")
_CcapAppTypeHisTTSSuccess_Type = ZeroBasedCounter32
_CcapAppTypeHisTTSSuccess_Object = MibTableColumn
ccapAppTypeHisTTSSuccess = _CcapAppTypeHisTTSSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 84),
    _CcapAppTypeHisTTSSuccess_Type()
)
ccapAppTypeHisTTSSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisTTSSuccess.setStatus("current")
_CcapAppTypeHisTTSFailed_Type = ZeroBasedCounter32
_CcapAppTypeHisTTSFailed_Object = MibTableColumn
ccapAppTypeHisTTSFailed = _CcapAppTypeHisTTSFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 2, 2, 1, 85),
    _CcapAppTypeHisTTSFailed_Type()
)
ccapAppTypeHisTTSFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppTypeHisTTSFailed.setStatus("current")
_CcapAppInstHisStat_ObjectIdentity = ObjectIdentity
ccapAppInstHisStat = _CcapAppInstHisStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3)
)
_CcapAppInstanceHistoryTable_Object = MibTable
ccapAppInstanceHistoryTable = _CcapAppInstanceHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ccapAppInstanceHistoryTable.setStatus("current")
_CcapAppInstanceHistoryEntry_Object = MibTableRow
ccapAppInstanceHistoryEntry = _CcapAppInstanceHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1)
)
ccapAppInstanceHistoryEntry.setIndexNames(
    (0, "CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIndex"),
)
if mibBuilder.loadTexts:
    ccapAppInstanceHistoryEntry.setStatus("current")


class _CcapAppInstHisIndex_Type(Unsigned32):
    """Custom type ccapAppInstHisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcapAppInstHisIndex_Type.__name__ = "Unsigned32"
_CcapAppInstHisIndex_Object = MibTableColumn
ccapAppInstHisIndex = _CcapAppInstHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 1),
    _CcapAppInstHisIndex_Type()
)
ccapAppInstHisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppInstHisIndex.setStatus("current")
_CcapAppInstHisSessionID_Type = Unsigned32
_CcapAppInstHisSessionID_Object = MibTableColumn
ccapAppInstHisSessionID = _CcapAppInstHisSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 2),
    _CcapAppInstHisSessionID_Type()
)
ccapAppInstHisSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisSessionID.setStatus("current")


class _CcapAppInstHisAppName_Type(OctetString):
    """Custom type ccapAppInstHisAppName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcapAppInstHisAppName_Type.__name__ = "OctetString"
_CcapAppInstHisAppName_Object = MibTableColumn
ccapAppInstHisAppName = _CcapAppInstHisAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 3),
    _CcapAppInstHisAppName_Type()
)
ccapAppInstHisAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisAppName.setStatus("current")
_CcapAppInstHisPSTNInCallSetupInd_Type = Unsigned32
_CcapAppInstHisPSTNInCallSetupInd_Object = MibTableColumn
ccapAppInstHisPSTNInCallSetupInd = _CcapAppInstHisPSTNInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 4),
    _CcapAppInstHisPSTNInCallSetupInd_Type()
)
ccapAppInstHisPSTNInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallSetupInd.setStatus("current")
_CcapAppInstHisPSTNInCallTotConn_Type = Unsigned32
_CcapAppInstHisPSTNInCallTotConn_Object = MibTableColumn
ccapAppInstHisPSTNInCallTotConn = _CcapAppInstHisPSTNInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 5),
    _CcapAppInstHisPSTNInCallTotConn_Type()
)
ccapAppInstHisPSTNInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallTotConn.setStatus("current")
_CcapAppInstHisPSTNInCallHandedOut_Type = Unsigned32
_CcapAppInstHisPSTNInCallHandedOut_Object = MibTableColumn
ccapAppInstHisPSTNInCallHandedOut = _CcapAppInstHisPSTNInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 6),
    _CcapAppInstHisPSTNInCallHandedOut_Type()
)
ccapAppInstHisPSTNInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallHandedOut.setStatus("current")
_CcapAppInstHisPSTNInCallHandOutRet_Type = Unsigned32
_CcapAppInstHisPSTNInCallHandOutRet_Object = MibTableColumn
ccapAppInstHisPSTNInCallHandOutRet = _CcapAppInstHisPSTNInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 7),
    _CcapAppInstHisPSTNInCallHandOutRet_Type()
)
ccapAppInstHisPSTNInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallHandOutRet.setStatus("current")
_CcapAppInstHisPSTNInCallInHandoff_Type = Unsigned32
_CcapAppInstHisPSTNInCallInHandoff_Object = MibTableColumn
ccapAppInstHisPSTNInCallInHandoff = _CcapAppInstHisPSTNInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 8),
    _CcapAppInstHisPSTNInCallInHandoff_Type()
)
ccapAppInstHisPSTNInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallInHandoff.setStatus("current")
_CcapAppInstHisPSTNInCallInHandoffRet_Type = Unsigned32
_CcapAppInstHisPSTNInCallInHandoffRet_Object = MibTableColumn
ccapAppInstHisPSTNInCallInHandoffRet = _CcapAppInstHisPSTNInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 9),
    _CcapAppInstHisPSTNInCallInHandoffRet_Type()
)
ccapAppInstHisPSTNInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallInHandoffRet.setStatus("current")
_CcapAppInstHisPSTNInCallDiscNormal_Type = Unsigned32
_CcapAppInstHisPSTNInCallDiscNormal_Object = MibTableColumn
ccapAppInstHisPSTNInCallDiscNormal = _CcapAppInstHisPSTNInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 10),
    _CcapAppInstHisPSTNInCallDiscNormal_Type()
)
ccapAppInstHisPSTNInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallDiscNormal.setStatus("current")
_CcapAppInstHisPSTNInCallDiscUsrErr_Type = Unsigned32
_CcapAppInstHisPSTNInCallDiscUsrErr_Object = MibTableColumn
ccapAppInstHisPSTNInCallDiscUsrErr = _CcapAppInstHisPSTNInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 11),
    _CcapAppInstHisPSTNInCallDiscUsrErr_Type()
)
ccapAppInstHisPSTNInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallDiscUsrErr.setStatus("current")
_CcapAppInstHisPSTNInCallDiscSysErr_Type = Unsigned32
_CcapAppInstHisPSTNInCallDiscSysErr_Object = MibTableColumn
ccapAppInstHisPSTNInCallDiscSysErr = _CcapAppInstHisPSTNInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 12),
    _CcapAppInstHisPSTNInCallDiscSysErr_Type()
)
ccapAppInstHisPSTNInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNInCallDiscSysErr.setStatus("current")
_CcapAppInstHisPSTNOutCallSetupReq_Type = Unsigned32
_CcapAppInstHisPSTNOutCallSetupReq_Object = MibTableColumn
ccapAppInstHisPSTNOutCallSetupReq = _CcapAppInstHisPSTNOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 13),
    _CcapAppInstHisPSTNOutCallSetupReq_Type()
)
ccapAppInstHisPSTNOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallSetupReq.setStatus("current")
_CcapAppInstHisPSTNOutCallTotConn_Type = Unsigned32
_CcapAppInstHisPSTNOutCallTotConn_Object = MibTableColumn
ccapAppInstHisPSTNOutCallTotConn = _CcapAppInstHisPSTNOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 14),
    _CcapAppInstHisPSTNOutCallTotConn_Type()
)
ccapAppInstHisPSTNOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallTotConn.setStatus("current")
_CcapAppInstHisPSTNOutCallHandedOut_Type = Unsigned32
_CcapAppInstHisPSTNOutCallHandedOut_Object = MibTableColumn
ccapAppInstHisPSTNOutCallHandedOut = _CcapAppInstHisPSTNOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 15),
    _CcapAppInstHisPSTNOutCallHandedOut_Type()
)
ccapAppInstHisPSTNOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallHandedOut.setStatus("current")
_CcapAppInstHisPSTNOutCallHandOutRet_Type = Unsigned32
_CcapAppInstHisPSTNOutCallHandOutRet_Object = MibTableColumn
ccapAppInstHisPSTNOutCallHandOutRet = _CcapAppInstHisPSTNOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 16),
    _CcapAppInstHisPSTNOutCallHandOutRet_Type()
)
ccapAppInstHisPSTNOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallHandOutRet.setStatus("current")
_CcapAppInstHisPSTNOutCallInHandoff_Type = Unsigned32
_CcapAppInstHisPSTNOutCallInHandoff_Object = MibTableColumn
ccapAppInstHisPSTNOutCallInHandoff = _CcapAppInstHisPSTNOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 17),
    _CcapAppInstHisPSTNOutCallInHandoff_Type()
)
ccapAppInstHisPSTNOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallInHandoff.setStatus("current")
_CcapAppInstHisPSTNOutCallInHandoffRet_Type = Unsigned32
_CcapAppInstHisPSTNOutCallInHandoffRet_Object = MibTableColumn
ccapAppInstHisPSTNOutCallInHandoffRet = _CcapAppInstHisPSTNOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 18),
    _CcapAppInstHisPSTNOutCallInHandoffRet_Type()
)
ccapAppInstHisPSTNOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallInHandoffRet.setStatus("current")
_CcapAppInstHisPSTNOutCallDiscNormal_Type = Unsigned32
_CcapAppInstHisPSTNOutCallDiscNormal_Object = MibTableColumn
ccapAppInstHisPSTNOutCallDiscNormal = _CcapAppInstHisPSTNOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 19),
    _CcapAppInstHisPSTNOutCallDiscNormal_Type()
)
ccapAppInstHisPSTNOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallDiscNormal.setStatus("current")
_CcapAppInstHisPSTNOutCallDiscUsrErr_Type = Unsigned32
_CcapAppInstHisPSTNOutCallDiscUsrErr_Object = MibTableColumn
ccapAppInstHisPSTNOutCallDiscUsrErr = _CcapAppInstHisPSTNOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 20),
    _CcapAppInstHisPSTNOutCallDiscUsrErr_Type()
)
ccapAppInstHisPSTNOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallDiscUsrErr.setStatus("current")
_CcapAppInstHisPSTNOutCallDiscSysErr_Type = Unsigned32
_CcapAppInstHisPSTNOutCallDiscSysErr_Object = MibTableColumn
ccapAppInstHisPSTNOutCallDiscSysErr = _CcapAppInstHisPSTNOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 21),
    _CcapAppInstHisPSTNOutCallDiscSysErr_Type()
)
ccapAppInstHisPSTNOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPSTNOutCallDiscSysErr.setStatus("current")
_CcapAppInstHisIPInCallSetupInd_Type = Unsigned32
_CcapAppInstHisIPInCallSetupInd_Object = MibTableColumn
ccapAppInstHisIPInCallSetupInd = _CcapAppInstHisIPInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 22),
    _CcapAppInstHisIPInCallSetupInd_Type()
)
ccapAppInstHisIPInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallSetupInd.setStatus("current")
_CcapAppInstHisIPInCallTotConn_Type = Unsigned32
_CcapAppInstHisIPInCallTotConn_Object = MibTableColumn
ccapAppInstHisIPInCallTotConn = _CcapAppInstHisIPInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 23),
    _CcapAppInstHisIPInCallTotConn_Type()
)
ccapAppInstHisIPInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallTotConn.setStatus("current")
_CcapAppInstHisIPInCallHandedOut_Type = Unsigned32
_CcapAppInstHisIPInCallHandedOut_Object = MibTableColumn
ccapAppInstHisIPInCallHandedOut = _CcapAppInstHisIPInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 24),
    _CcapAppInstHisIPInCallHandedOut_Type()
)
ccapAppInstHisIPInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallHandedOut.setStatus("current")
_CcapAppInstHisIPInCallHandOutRet_Type = Unsigned32
_CcapAppInstHisIPInCallHandOutRet_Object = MibTableColumn
ccapAppInstHisIPInCallHandOutRet = _CcapAppInstHisIPInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 25),
    _CcapAppInstHisIPInCallHandOutRet_Type()
)
ccapAppInstHisIPInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallHandOutRet.setStatus("current")
_CcapAppInstHisIPInCallInHandoff_Type = Unsigned32
_CcapAppInstHisIPInCallInHandoff_Object = MibTableColumn
ccapAppInstHisIPInCallInHandoff = _CcapAppInstHisIPInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 26),
    _CcapAppInstHisIPInCallInHandoff_Type()
)
ccapAppInstHisIPInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallInHandoff.setStatus("current")
_CcapAppInstHisIPInCallInHandoffRet_Type = Unsigned32
_CcapAppInstHisIPInCallInHandoffRet_Object = MibTableColumn
ccapAppInstHisIPInCallInHandoffRet = _CcapAppInstHisIPInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 27),
    _CcapAppInstHisIPInCallInHandoffRet_Type()
)
ccapAppInstHisIPInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallInHandoffRet.setStatus("current")
_CcapAppInstHisIPInCallDiscNormal_Type = Unsigned32
_CcapAppInstHisIPInCallDiscNormal_Object = MibTableColumn
ccapAppInstHisIPInCallDiscNormal = _CcapAppInstHisIPInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 28),
    _CcapAppInstHisIPInCallDiscNormal_Type()
)
ccapAppInstHisIPInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallDiscNormal.setStatus("current")
_CcapAppInstHisIPInCallDiscUsrErr_Type = Unsigned32
_CcapAppInstHisIPInCallDiscUsrErr_Object = MibTableColumn
ccapAppInstHisIPInCallDiscUsrErr = _CcapAppInstHisIPInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 29),
    _CcapAppInstHisIPInCallDiscUsrErr_Type()
)
ccapAppInstHisIPInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallDiscUsrErr.setStatus("current")
_CcapAppInstHisIPInCallDiscSysErr_Type = Unsigned32
_CcapAppInstHisIPInCallDiscSysErr_Object = MibTableColumn
ccapAppInstHisIPInCallDiscSysErr = _CcapAppInstHisIPInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 30),
    _CcapAppInstHisIPInCallDiscSysErr_Type()
)
ccapAppInstHisIPInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPInCallDiscSysErr.setStatus("current")
_CcapAppInstHisIPOutCallSetupReq_Type = Unsigned32
_CcapAppInstHisIPOutCallSetupReq_Object = MibTableColumn
ccapAppInstHisIPOutCallSetupReq = _CcapAppInstHisIPOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 31),
    _CcapAppInstHisIPOutCallSetupReq_Type()
)
ccapAppInstHisIPOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallSetupReq.setStatus("current")
_CcapAppInstHisIPOutCallTotConn_Type = Unsigned32
_CcapAppInstHisIPOutCallTotConn_Object = MibTableColumn
ccapAppInstHisIPOutCallTotConn = _CcapAppInstHisIPOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 32),
    _CcapAppInstHisIPOutCallTotConn_Type()
)
ccapAppInstHisIPOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallTotConn.setStatus("current")
_CcapAppInstHisIPOutCallHandedOut_Type = Unsigned32
_CcapAppInstHisIPOutCallHandedOut_Object = MibTableColumn
ccapAppInstHisIPOutCallHandedOut = _CcapAppInstHisIPOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 33),
    _CcapAppInstHisIPOutCallHandedOut_Type()
)
ccapAppInstHisIPOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallHandedOut.setStatus("current")
_CcapAppInstHisIPOutCallHandOutRet_Type = Unsigned32
_CcapAppInstHisIPOutCallHandOutRet_Object = MibTableColumn
ccapAppInstHisIPOutCallHandOutRet = _CcapAppInstHisIPOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 34),
    _CcapAppInstHisIPOutCallHandOutRet_Type()
)
ccapAppInstHisIPOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallHandOutRet.setStatus("current")
_CcapAppInstHisIPOutCallInHandoff_Type = Unsigned32
_CcapAppInstHisIPOutCallInHandoff_Object = MibTableColumn
ccapAppInstHisIPOutCallInHandoff = _CcapAppInstHisIPOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 35),
    _CcapAppInstHisIPOutCallInHandoff_Type()
)
ccapAppInstHisIPOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallInHandoff.setStatus("current")
_CcapAppInstHisIPOutCallInHandoffRet_Type = Unsigned32
_CcapAppInstHisIPOutCallInHandoffRet_Object = MibTableColumn
ccapAppInstHisIPOutCallInHandoffRet = _CcapAppInstHisIPOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 36),
    _CcapAppInstHisIPOutCallInHandoffRet_Type()
)
ccapAppInstHisIPOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallInHandoffRet.setStatus("current")
_CcapAppInstHisIPOutCallDiscNormal_Type = Unsigned32
_CcapAppInstHisIPOutCallDiscNormal_Object = MibTableColumn
ccapAppInstHisIPOutCallDiscNormal = _CcapAppInstHisIPOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 37),
    _CcapAppInstHisIPOutCallDiscNormal_Type()
)
ccapAppInstHisIPOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallDiscNormal.setStatus("current")
_CcapAppInstHisIPOutCallDiscUsrErr_Type = Unsigned32
_CcapAppInstHisIPOutCallDiscUsrErr_Object = MibTableColumn
ccapAppInstHisIPOutCallDiscUsrErr = _CcapAppInstHisIPOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 38),
    _CcapAppInstHisIPOutCallDiscUsrErr_Type()
)
ccapAppInstHisIPOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallDiscUsrErr.setStatus("current")
_CcapAppInstHisIPOutCallDiscSysErr_Type = Unsigned32
_CcapAppInstHisIPOutCallDiscSysErr_Object = MibTableColumn
ccapAppInstHisIPOutCallDiscSysErr = _CcapAppInstHisIPOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 39),
    _CcapAppInstHisIPOutCallDiscSysErr_Type()
)
ccapAppInstHisIPOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisIPOutCallDiscSysErr.setStatus("current")
_CcapAppInstHisPlaceCallAttempts_Type = Unsigned32
_CcapAppInstHisPlaceCallAttempts_Object = MibTableColumn
ccapAppInstHisPlaceCallAttempts = _CcapAppInstHisPlaceCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 40),
    _CcapAppInstHisPlaceCallAttempts_Type()
)
ccapAppInstHisPlaceCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPlaceCallAttempts.setStatus("current")
_CcapAppInstHisPlaceCallSuccess_Type = Unsigned32
_CcapAppInstHisPlaceCallSuccess_Object = MibTableColumn
ccapAppInstHisPlaceCallSuccess = _CcapAppInstHisPlaceCallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 41),
    _CcapAppInstHisPlaceCallSuccess_Type()
)
ccapAppInstHisPlaceCallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPlaceCallSuccess.setStatus("current")
_CcapAppInstHisPlaceCallFailure_Type = Unsigned32
_CcapAppInstHisPlaceCallFailure_Object = MibTableColumn
ccapAppInstHisPlaceCallFailure = _CcapAppInstHisPlaceCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 42),
    _CcapAppInstHisPlaceCallFailure_Type()
)
ccapAppInstHisPlaceCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPlaceCallFailure.setStatus("current")
_CcapAppInstHisInHandoffCallback_Type = Unsigned32
_CcapAppInstHisInHandoffCallback_Object = MibTableColumn
ccapAppInstHisInHandoffCallback = _CcapAppInstHisInHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 43),
    _CcapAppInstHisInHandoffCallback_Type()
)
ccapAppInstHisInHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisInHandoffCallback.setStatus("current")
_CcapAppInstHisInHandoffCallbackRet_Type = Unsigned32
_CcapAppInstHisInHandoffCallbackRet_Object = MibTableColumn
ccapAppInstHisInHandoffCallbackRet = _CcapAppInstHisInHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 44),
    _CcapAppInstHisInHandoffCallbackRet_Type()
)
ccapAppInstHisInHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisInHandoffCallbackRet.setStatus("current")
_CcapAppInstHisInHandoffNoCallback_Type = Unsigned32
_CcapAppInstHisInHandoffNoCallback_Object = MibTableColumn
ccapAppInstHisInHandoffNoCallback = _CcapAppInstHisInHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 45),
    _CcapAppInstHisInHandoffNoCallback_Type()
)
ccapAppInstHisInHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisInHandoffNoCallback.setStatus("current")
_CcapAppInstHisOutHandoffCallback_Type = Unsigned32
_CcapAppInstHisOutHandoffCallback_Object = MibTableColumn
ccapAppInstHisOutHandoffCallback = _CcapAppInstHisOutHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 46),
    _CcapAppInstHisOutHandoffCallback_Type()
)
ccapAppInstHisOutHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisOutHandoffCallback.setStatus("current")
_CcapAppInstHisOutHandoffCallbackRet_Type = Unsigned32
_CcapAppInstHisOutHandoffCallbackRet_Object = MibTableColumn
ccapAppInstHisOutHandoffCallbackRet = _CcapAppInstHisOutHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 47),
    _CcapAppInstHisOutHandoffCallbackRet_Type()
)
ccapAppInstHisOutHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisOutHandoffCallbackRet.setStatus("current")
_CcapAppInstHisOutHandoffNoCallback_Type = Unsigned32
_CcapAppInstHisOutHandoffNoCallback_Object = MibTableColumn
ccapAppInstHisOutHandoffNoCallback = _CcapAppInstHisOutHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 48),
    _CcapAppInstHisOutHandoffNoCallback_Type()
)
ccapAppInstHisOutHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisOutHandoffNoCallback.setStatus("current")
_CcapAppInstHisOutHandofffailures_Type = Unsigned32
_CcapAppInstHisOutHandofffailures_Object = MibTableColumn
ccapAppInstHisOutHandofffailures = _CcapAppInstHisOutHandofffailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 49),
    _CcapAppInstHisOutHandofffailures_Type()
)
ccapAppInstHisOutHandofffailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisOutHandofffailures.setStatus("current")
_CcapAppInstHisDocumentReadAttempts_Type = Unsigned32
_CcapAppInstHisDocumentReadAttempts_Object = MibTableColumn
ccapAppInstHisDocumentReadAttempts = _CcapAppInstHisDocumentReadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 50),
    _CcapAppInstHisDocumentReadAttempts_Type()
)
ccapAppInstHisDocumentReadAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentReadAttempts.setStatus("current")
_CcapAppInstHisDocumentReadSuccess_Type = Unsigned32
_CcapAppInstHisDocumentReadSuccess_Object = MibTableColumn
ccapAppInstHisDocumentReadSuccess = _CcapAppInstHisDocumentReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 51),
    _CcapAppInstHisDocumentReadSuccess_Type()
)
ccapAppInstHisDocumentReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentReadSuccess.setStatus("current")
_CcapAppInstHisDocumentReadFailures_Type = Unsigned32
_CcapAppInstHisDocumentReadFailures_Object = MibTableColumn
ccapAppInstHisDocumentReadFailures = _CcapAppInstHisDocumentReadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 52),
    _CcapAppInstHisDocumentReadFailures_Type()
)
ccapAppInstHisDocumentReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentReadFailures.setStatus("current")
_CcapAppInstHisDocumentParseErrors_Type = Unsigned32
_CcapAppInstHisDocumentParseErrors_Object = MibTableColumn
ccapAppInstHisDocumentParseErrors = _CcapAppInstHisDocumentParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 53),
    _CcapAppInstHisDocumentParseErrors_Type()
)
ccapAppInstHisDocumentParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentParseErrors.setStatus("current")
_CcapAppInstHisDocumentWriteAttempts_Type = Unsigned32
_CcapAppInstHisDocumentWriteAttempts_Object = MibTableColumn
ccapAppInstHisDocumentWriteAttempts = _CcapAppInstHisDocumentWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 54),
    _CcapAppInstHisDocumentWriteAttempts_Type()
)
ccapAppInstHisDocumentWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentWriteAttempts.setStatus("current")
_CcapAppInstHisDocumentWriteSuccess_Type = Unsigned32
_CcapAppInstHisDocumentWriteSuccess_Object = MibTableColumn
ccapAppInstHisDocumentWriteSuccess = _CcapAppInstHisDocumentWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 55),
    _CcapAppInstHisDocumentWriteSuccess_Type()
)
ccapAppInstHisDocumentWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentWriteSuccess.setStatus("current")
_CcapAppInstHisDocumentWriteFailures_Type = Unsigned32
_CcapAppInstHisDocumentWriteFailures_Object = MibTableColumn
ccapAppInstHisDocumentWriteFailures = _CcapAppInstHisDocumentWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 56),
    _CcapAppInstHisDocumentWriteFailures_Type()
)
ccapAppInstHisDocumentWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDocumentWriteFailures.setStatus("current")
_CcapAppInstHisDTMFAttempts_Type = Unsigned32
_CcapAppInstHisDTMFAttempts_Object = MibTableColumn
ccapAppInstHisDTMFAttempts = _CcapAppInstHisDTMFAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 57),
    _CcapAppInstHisDTMFAttempts_Type()
)
ccapAppInstHisDTMFAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFAttempts.setStatus("current")
_CcapAppInstHisDTMFAborted_Type = Unsigned32
_CcapAppInstHisDTMFAborted_Object = MibTableColumn
ccapAppInstHisDTMFAborted = _CcapAppInstHisDTMFAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 58),
    _CcapAppInstHisDTMFAborted_Type()
)
ccapAppInstHisDTMFAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFAborted.setStatus("current")
_CcapAppInstHisDTMFNoMatch_Type = Unsigned32
_CcapAppInstHisDTMFNoMatch_Object = MibTableColumn
ccapAppInstHisDTMFNoMatch = _CcapAppInstHisDTMFNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 59),
    _CcapAppInstHisDTMFNoMatch_Type()
)
ccapAppInstHisDTMFNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFNoMatch.setStatus("current")
_CcapAppInstHisDTMFNoInput_Type = Unsigned32
_CcapAppInstHisDTMFNoInput_Object = MibTableColumn
ccapAppInstHisDTMFNoInput = _CcapAppInstHisDTMFNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 60),
    _CcapAppInstHisDTMFNoInput_Type()
)
ccapAppInstHisDTMFNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFNoInput.setStatus("current")
_CcapAppInstHisDTMFMatch_Type = Unsigned32
_CcapAppInstHisDTMFMatch_Object = MibTableColumn
ccapAppInstHisDTMFMatch = _CcapAppInstHisDTMFMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 61),
    _CcapAppInstHisDTMFMatch_Type()
)
ccapAppInstHisDTMFMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFMatch.setStatus("current")
_CcapAppInstHisDTMFLongPound_Type = Unsigned32
_CcapAppInstHisDTMFLongPound_Object = MibTableColumn
ccapAppInstHisDTMFLongPound = _CcapAppInstHisDTMFLongPound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 62),
    _CcapAppInstHisDTMFLongPound_Type()
)
ccapAppInstHisDTMFLongPound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisDTMFLongPound.setStatus("current")
_CcapAppInstHisASRAttempts_Type = Unsigned32
_CcapAppInstHisASRAttempts_Object = MibTableColumn
ccapAppInstHisASRAttempts = _CcapAppInstHisASRAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 63),
    _CcapAppInstHisASRAttempts_Type()
)
ccapAppInstHisASRAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASRAttempts.setStatus("current")
_CcapAppInstHisASRAborted_Type = Unsigned32
_CcapAppInstHisASRAborted_Object = MibTableColumn
ccapAppInstHisASRAborted = _CcapAppInstHisASRAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 64),
    _CcapAppInstHisASRAborted_Type()
)
ccapAppInstHisASRAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASRAborted.setStatus("current")
_CcapAppInstHisASRNoMatch_Type = Unsigned32
_CcapAppInstHisASRNoMatch_Object = MibTableColumn
ccapAppInstHisASRNoMatch = _CcapAppInstHisASRNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 65),
    _CcapAppInstHisASRNoMatch_Type()
)
ccapAppInstHisASRNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASRNoMatch.setStatus("current")
_CcapAppInstHisASRNoInput_Type = Unsigned32
_CcapAppInstHisASRNoInput_Object = MibTableColumn
ccapAppInstHisASRNoInput = _CcapAppInstHisASRNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 66),
    _CcapAppInstHisASRNoInput_Type()
)
ccapAppInstHisASRNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASRNoInput.setStatus("current")
_CcapAppInstHisASRMatch_Type = Unsigned32
_CcapAppInstHisASRMatch_Object = MibTableColumn
ccapAppInstHisASRMatch = _CcapAppInstHisASRMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 67),
    _CcapAppInstHisASRMatch_Type()
)
ccapAppInstHisASRMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASRMatch.setStatus("current")
_CcapAppInstHisAAAAuthenticateFailure_Type = Unsigned32
_CcapAppInstHisAAAAuthenticateFailure_Object = MibTableColumn
ccapAppInstHisAAAAuthenticateFailure = _CcapAppInstHisAAAAuthenticateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 68),
    _CcapAppInstHisAAAAuthenticateFailure_Type()
)
ccapAppInstHisAAAAuthenticateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisAAAAuthenticateFailure.setStatus("current")
_CcapAppInstHisAAAAuthenticateSuccess_Type = Unsigned32
_CcapAppInstHisAAAAuthenticateSuccess_Object = MibTableColumn
ccapAppInstHisAAAAuthenticateSuccess = _CcapAppInstHisAAAAuthenticateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 69),
    _CcapAppInstHisAAAAuthenticateSuccess_Type()
)
ccapAppInstHisAAAAuthenticateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisAAAAuthenticateSuccess.setStatus("current")
_CcapAppInstHisAAAAuthorizeFailure_Type = Unsigned32
_CcapAppInstHisAAAAuthorizeFailure_Object = MibTableColumn
ccapAppInstHisAAAAuthorizeFailure = _CcapAppInstHisAAAAuthorizeFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 70),
    _CcapAppInstHisAAAAuthorizeFailure_Type()
)
ccapAppInstHisAAAAuthorizeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisAAAAuthorizeFailure.setStatus("current")
_CcapAppInstHisAAAAuthorizeSuccess_Type = Unsigned32
_CcapAppInstHisAAAAuthorizeSuccess_Object = MibTableColumn
ccapAppInstHisAAAAuthorizeSuccess = _CcapAppInstHisAAAAuthorizeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 71),
    _CcapAppInstHisAAAAuthorizeSuccess_Type()
)
ccapAppInstHisAAAAuthorizeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisAAAAuthorizeSuccess.setStatus("current")
_CcapAppInstHisASNLSubscriptionsSent_Type = Unsigned32
_CcapAppInstHisASNLSubscriptionsSent_Object = MibTableColumn
ccapAppInstHisASNLSubscriptionsSent = _CcapAppInstHisASNLSubscriptionsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 72),
    _CcapAppInstHisASNLSubscriptionsSent_Type()
)
ccapAppInstHisASNLSubscriptionsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASNLSubscriptionsSent.setStatus("current")
_CcapAppInstHisASNLSubscriptionsSuccess_Type = Unsigned32
_CcapAppInstHisASNLSubscriptionsSuccess_Object = MibTableColumn
ccapAppInstHisASNLSubscriptionsSuccess = _CcapAppInstHisASNLSubscriptionsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 73),
    _CcapAppInstHisASNLSubscriptionsSuccess_Type()
)
ccapAppInstHisASNLSubscriptionsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASNLSubscriptionsSuccess.setStatus("current")
_CcapAppInstHisASNLSubscriptionsFailed_Type = Unsigned32
_CcapAppInstHisASNLSubscriptionsFailed_Object = MibTableColumn
ccapAppInstHisASNLSubscriptionsFailed = _CcapAppInstHisASNLSubscriptionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 74),
    _CcapAppInstHisASNLSubscriptionsFailed_Type()
)
ccapAppInstHisASNLSubscriptionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASNLSubscriptionsFailed.setStatus("current")
_CcapAppInstHisASNLNotifReceived_Type = Unsigned32
_CcapAppInstHisASNLNotifReceived_Object = MibTableColumn
ccapAppInstHisASNLNotifReceived = _CcapAppInstHisASNLNotifReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 75),
    _CcapAppInstHisASNLNotifReceived_Type()
)
ccapAppInstHisASNLNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisASNLNotifReceived.setStatus("current")
_CcapAppInstHisPromptPlayAttempts_Type = Unsigned32
_CcapAppInstHisPromptPlayAttempts_Object = MibTableColumn
ccapAppInstHisPromptPlayAttempts = _CcapAppInstHisPromptPlayAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 76),
    _CcapAppInstHisPromptPlayAttempts_Type()
)
ccapAppInstHisPromptPlayAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPromptPlayAttempts.setStatus("current")
_CcapAppInstHisPromptPlaySuccess_Type = Unsigned32
_CcapAppInstHisPromptPlaySuccess_Object = MibTableColumn
ccapAppInstHisPromptPlaySuccess = _CcapAppInstHisPromptPlaySuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 77),
    _CcapAppInstHisPromptPlaySuccess_Type()
)
ccapAppInstHisPromptPlaySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPromptPlaySuccess.setStatus("current")
_CcapAppInstHisPromptPlayFailed_Type = Unsigned32
_CcapAppInstHisPromptPlayFailed_Object = MibTableColumn
ccapAppInstHisPromptPlayFailed = _CcapAppInstHisPromptPlayFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 78),
    _CcapAppInstHisPromptPlayFailed_Type()
)
ccapAppInstHisPromptPlayFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPromptPlayFailed.setStatus("current")
_CcapAppInstHisPromptPlayDuration_Type = Unsigned32
_CcapAppInstHisPromptPlayDuration_Object = MibTableColumn
ccapAppInstHisPromptPlayDuration = _CcapAppInstHisPromptPlayDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 79),
    _CcapAppInstHisPromptPlayDuration_Type()
)
ccapAppInstHisPromptPlayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisPromptPlayDuration.setStatus("current")
_CcapAppInstHisRecordingAttempts_Type = Unsigned32
_CcapAppInstHisRecordingAttempts_Object = MibTableColumn
ccapAppInstHisRecordingAttempts = _CcapAppInstHisRecordingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 80),
    _CcapAppInstHisRecordingAttempts_Type()
)
ccapAppInstHisRecordingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisRecordingAttempts.setStatus("current")
_CcapAppInstHisRecordingSuccess_Type = Unsigned32
_CcapAppInstHisRecordingSuccess_Object = MibTableColumn
ccapAppInstHisRecordingSuccess = _CcapAppInstHisRecordingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 81),
    _CcapAppInstHisRecordingSuccess_Type()
)
ccapAppInstHisRecordingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisRecordingSuccess.setStatus("current")
_CcapAppInstHisRecordingFailed_Type = Unsigned32
_CcapAppInstHisRecordingFailed_Object = MibTableColumn
ccapAppInstHisRecordingFailed = _CcapAppInstHisRecordingFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 82),
    _CcapAppInstHisRecordingFailed_Type()
)
ccapAppInstHisRecordingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisRecordingFailed.setStatus("current")
_CcapAppInstHisRecordingDuration_Type = Unsigned32
_CcapAppInstHisRecordingDuration_Object = MibTableColumn
ccapAppInstHisRecordingDuration = _CcapAppInstHisRecordingDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 83),
    _CcapAppInstHisRecordingDuration_Type()
)
ccapAppInstHisRecordingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisRecordingDuration.setStatus("current")
_CcapAppInstHisTTSAttempts_Type = Unsigned32
_CcapAppInstHisTTSAttempts_Object = MibTableColumn
ccapAppInstHisTTSAttempts = _CcapAppInstHisTTSAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 84),
    _CcapAppInstHisTTSAttempts_Type()
)
ccapAppInstHisTTSAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisTTSAttempts.setStatus("current")
_CcapAppInstHisTTSSuccess_Type = Unsigned32
_CcapAppInstHisTTSSuccess_Object = MibTableColumn
ccapAppInstHisTTSSuccess = _CcapAppInstHisTTSSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 85),
    _CcapAppInstHisTTSSuccess_Type()
)
ccapAppInstHisTTSSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisTTSSuccess.setStatus("current")
_CcapAppInstHisTTSFailed_Type = Unsigned32
_CcapAppInstHisTTSFailed_Object = MibTableColumn
ccapAppInstHisTTSFailed = _CcapAppInstHisTTSFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 86),
    _CcapAppInstHisTTSFailed_Type()
)
ccapAppInstHisTTSFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHisTTSFailed.setStatus("current")
_CcapAppInstHistEvtLogging_Type = TruthValue
_CcapAppInstHistEvtLogging_Object = MibTableColumn
ccapAppInstHistEvtLogging = _CcapAppInstHistEvtLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 3, 3, 1, 87),
    _CcapAppInstHistEvtLogging_Type()
)
ccapAppInstHistEvtLogging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppInstHistEvtLogging.setStatus("current")
_CcapAppGblActStat_ObjectIdentity = ObjectIdentity
ccapAppGblActStat = _CcapAppGblActStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4)
)
_CcapAppGblActCurrentInstances_Type = Gauge32
_CcapAppGblActCurrentInstances_Object = MibScalar
ccapAppGblActCurrentInstances = _CcapAppGblActCurrentInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 1),
    _CcapAppGblActCurrentInstances_Type()
)
ccapAppGblActCurrentInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActCurrentInstances.setStatus("current")
_CcapAppGblActPSTNInCallNowConn_Type = Gauge32
_CcapAppGblActPSTNInCallNowConn_Object = MibScalar
ccapAppGblActPSTNInCallNowConn = _CcapAppGblActPSTNInCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 2),
    _CcapAppGblActPSTNInCallNowConn_Type()
)
ccapAppGblActPSTNInCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActPSTNInCallNowConn.setStatus("current")
_CcapAppGblActPSTNOutCallNowConn_Type = Gauge32
_CcapAppGblActPSTNOutCallNowConn_Object = MibScalar
ccapAppGblActPSTNOutCallNowConn = _CcapAppGblActPSTNOutCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 3),
    _CcapAppGblActPSTNOutCallNowConn_Type()
)
ccapAppGblActPSTNOutCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActPSTNOutCallNowConn.setStatus("current")
_CcapAppGblActIPInCallNowConn_Type = Gauge32
_CcapAppGblActIPInCallNowConn_Object = MibScalar
ccapAppGblActIPInCallNowConn = _CcapAppGblActIPInCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 4),
    _CcapAppGblActIPInCallNowConn_Type()
)
ccapAppGblActIPInCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActIPInCallNowConn.setStatus("current")
_CcapAppGblActIPOutCallNowConn_Type = Gauge32
_CcapAppGblActIPOutCallNowConn_Object = MibScalar
ccapAppGblActIPOutCallNowConn = _CcapAppGblActIPOutCallNowConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 5),
    _CcapAppGblActIPOutCallNowConn_Type()
)
ccapAppGblActIPOutCallNowConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActIPOutCallNowConn.setStatus("current")
_CcapAppGblActPlaceCallInProgress_Type = Gauge32
_CcapAppGblActPlaceCallInProgress_Object = MibScalar
ccapAppGblActPlaceCallInProgress = _CcapAppGblActPlaceCallInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 6),
    _CcapAppGblActPlaceCallInProgress_Type()
)
ccapAppGblActPlaceCallInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActPlaceCallInProgress.setStatus("current")
_CcapAppGblActHandoffInProgress_Type = Gauge32
_CcapAppGblActHandoffInProgress_Object = MibScalar
ccapAppGblActHandoffInProgress = _CcapAppGblActHandoffInProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 7),
    _CcapAppGblActHandoffInProgress_Type()
)
ccapAppGblActHandoffInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActHandoffInProgress.setStatus("current")
_CcapAppGblActPromptPlayActive_Type = Gauge32
_CcapAppGblActPromptPlayActive_Object = MibScalar
ccapAppGblActPromptPlayActive = _CcapAppGblActPromptPlayActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 8),
    _CcapAppGblActPromptPlayActive_Type()
)
ccapAppGblActPromptPlayActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActPromptPlayActive.setStatus("current")
_CcapAppGblActRecordingActive_Type = Gauge32
_CcapAppGblActRecordingActive_Object = MibScalar
ccapAppGblActRecordingActive = _CcapAppGblActRecordingActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 9),
    _CcapAppGblActRecordingActive_Type()
)
ccapAppGblActRecordingActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActRecordingActive.setStatus("current")
_CcapAppGblActTTSActive_Type = Gauge32
_CcapAppGblActTTSActive_Object = MibScalar
ccapAppGblActTTSActive = _CcapAppGblActTTSActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 10),
    _CcapAppGblActTTSActive_Type()
)
ccapAppGblActTTSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblActTTSActive.setStatus("current")


class _CcapAppGblStatsLogging_Type(Integer32):
    """Custom type ccapAppGblStatsLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppGblStatsLogging_Type.__name__ = "Integer32"
_CcapAppGblStatsLogging_Object = MibScalar
ccapAppGblStatsLogging = _CcapAppGblStatsLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 11),
    _CcapAppGblStatsLogging_Type()
)
ccapAppGblStatsLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppGblStatsLogging.setStatus("current")


class _CcapAppGblEventLogging_Type(Integer32):
    """Custom type ccapAppGblEventLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppGblEventLogging_Type.__name__ = "Integer32"
_CcapAppGblEventLogging_Object = MibScalar
ccapAppGblEventLogging = _CcapAppGblEventLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 12),
    _CcapAppGblEventLogging_Type()
)
ccapAppGblEventLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppGblEventLogging.setStatus("current")


class _CcapAppGblEvtLogflush_Type(Integer32):
    """Custom type ccapAppGblEvtLogflush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ftp", 1)
    )


_CcapAppGblEvtLogflush_Type.__name__ = "Integer32"
_CcapAppGblEvtLogflush_Object = MibScalar
ccapAppGblEvtLogflush = _CcapAppGblEvtLogflush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 13),
    _CcapAppGblEvtLogflush_Type()
)
ccapAppGblEvtLogflush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppGblEvtLogflush.setStatus("current")


class _CcapAppGblStatsClear_Type(Integer32):
    """Custom type ccapAppGblStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_CcapAppGblStatsClear_Type.__name__ = "Integer32"
_CcapAppGblStatsClear_Object = MibScalar
ccapAppGblStatsClear = _CcapAppGblStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 14),
    _CcapAppGblStatsClear_Type()
)
ccapAppGblStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppGblStatsClear.setStatus("current")
_CcapAppGblLastResetTime_Type = TimeStamp
_CcapAppGblLastResetTime_Object = MibScalar
ccapAppGblLastResetTime = _CcapAppGblLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 4, 15),
    _CcapAppGblLastResetTime_Type()
)
ccapAppGblLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblLastResetTime.setStatus("current")
_CcapAppGblHisStat_ObjectIdentity = ObjectIdentity
ccapAppGblHisStat = _CcapAppGblHisStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5)
)
_CcapAppGblHisTotalInstances_Type = ZeroBasedCounter32
_CcapAppGblHisTotalInstances_Object = MibScalar
ccapAppGblHisTotalInstances = _CcapAppGblHisTotalInstances_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 1),
    _CcapAppGblHisTotalInstances_Type()
)
ccapAppGblHisTotalInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisTotalInstances.setStatus("current")
_CcapAppGblHisLastReset_Type = TimeStamp
_CcapAppGblHisLastReset_Object = MibScalar
ccapAppGblHisLastReset = _CcapAppGblHisLastReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 2),
    _CcapAppGblHisLastReset_Type()
)
ccapAppGblHisLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisLastReset.setStatus("current")
_CcapAppGblHisPSTNInCallSetupInd_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallSetupInd_Object = MibScalar
ccapAppGblHisPSTNInCallSetupInd = _CcapAppGblHisPSTNInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 3),
    _CcapAppGblHisPSTNInCallSetupInd_Type()
)
ccapAppGblHisPSTNInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallSetupInd.setStatus("current")
_CcapAppGblHisPSTNInCallTotConn_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallTotConn_Object = MibScalar
ccapAppGblHisPSTNInCallTotConn = _CcapAppGblHisPSTNInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 4),
    _CcapAppGblHisPSTNInCallTotConn_Type()
)
ccapAppGblHisPSTNInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallTotConn.setStatus("current")
_CcapAppGblHisPSTNInCallHandedOut_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallHandedOut_Object = MibScalar
ccapAppGblHisPSTNInCallHandedOut = _CcapAppGblHisPSTNInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 5),
    _CcapAppGblHisPSTNInCallHandedOut_Type()
)
ccapAppGblHisPSTNInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallHandedOut.setStatus("current")
_CcapAppGblHisPSTNInCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallHandOutRet_Object = MibScalar
ccapAppGblHisPSTNInCallHandOutRet = _CcapAppGblHisPSTNInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 6),
    _CcapAppGblHisPSTNInCallHandOutRet_Type()
)
ccapAppGblHisPSTNInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallHandOutRet.setStatus("current")
_CcapAppGblHisPSTNInCallInHandoff_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallInHandoff_Object = MibScalar
ccapAppGblHisPSTNInCallInHandoff = _CcapAppGblHisPSTNInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 7),
    _CcapAppGblHisPSTNInCallInHandoff_Type()
)
ccapAppGblHisPSTNInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallInHandoff.setStatus("current")
_CcapAppGblHisPSTNInCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallInHandoffRet_Object = MibScalar
ccapAppGblHisPSTNInCallInHandoffRet = _CcapAppGblHisPSTNInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 8),
    _CcapAppGblHisPSTNInCallInHandoffRet_Type()
)
ccapAppGblHisPSTNInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallInHandoffRet.setStatus("current")
_CcapAppGblHisPSTNInCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallDiscNormal_Object = MibScalar
ccapAppGblHisPSTNInCallDiscNormal = _CcapAppGblHisPSTNInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 9),
    _CcapAppGblHisPSTNInCallDiscNormal_Type()
)
ccapAppGblHisPSTNInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallDiscNormal.setStatus("current")
_CcapAppGblHisPSTNInCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallDiscUsrErr_Object = MibScalar
ccapAppGblHisPSTNInCallDiscUsrErr = _CcapAppGblHisPSTNInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 10),
    _CcapAppGblHisPSTNInCallDiscUsrErr_Type()
)
ccapAppGblHisPSTNInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallDiscUsrErr.setStatus("current")
_CcapAppGblHisPSTNInCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNInCallDiscSysErr_Object = MibScalar
ccapAppGblHisPSTNInCallDiscSysErr = _CcapAppGblHisPSTNInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 11),
    _CcapAppGblHisPSTNInCallDiscSysErr_Type()
)
ccapAppGblHisPSTNInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNInCallDiscSysErr.setStatus("current")
_CcapAppGblHisPSTNOutCallSetupReq_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallSetupReq_Object = MibScalar
ccapAppGblHisPSTNOutCallSetupReq = _CcapAppGblHisPSTNOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 12),
    _CcapAppGblHisPSTNOutCallSetupReq_Type()
)
ccapAppGblHisPSTNOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallSetupReq.setStatus("current")
_CcapAppGblHisPSTNOutCallTotConn_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallTotConn_Object = MibScalar
ccapAppGblHisPSTNOutCallTotConn = _CcapAppGblHisPSTNOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 13),
    _CcapAppGblHisPSTNOutCallTotConn_Type()
)
ccapAppGblHisPSTNOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallTotConn.setStatus("current")
_CcapAppGblHisPSTNOutCallHandedOut_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallHandedOut_Object = MibScalar
ccapAppGblHisPSTNOutCallHandedOut = _CcapAppGblHisPSTNOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 14),
    _CcapAppGblHisPSTNOutCallHandedOut_Type()
)
ccapAppGblHisPSTNOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallHandedOut.setStatus("current")
_CcapAppGblHisPSTNOutCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallHandOutRet_Object = MibScalar
ccapAppGblHisPSTNOutCallHandOutRet = _CcapAppGblHisPSTNOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 15),
    _CcapAppGblHisPSTNOutCallHandOutRet_Type()
)
ccapAppGblHisPSTNOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallHandOutRet.setStatus("current")
_CcapAppGblHisPSTNOutCallInHandoff_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallInHandoff_Object = MibScalar
ccapAppGblHisPSTNOutCallInHandoff = _CcapAppGblHisPSTNOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 16),
    _CcapAppGblHisPSTNOutCallInHandoff_Type()
)
ccapAppGblHisPSTNOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallInHandoff.setStatus("current")
_CcapAppGblHisPSTNOutCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallInHandoffRet_Object = MibScalar
ccapAppGblHisPSTNOutCallInHandoffRet = _CcapAppGblHisPSTNOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 17),
    _CcapAppGblHisPSTNOutCallInHandoffRet_Type()
)
ccapAppGblHisPSTNOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallInHandoffRet.setStatus("current")
_CcapAppGblHisPSTNOutCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallDiscNormal_Object = MibScalar
ccapAppGblHisPSTNOutCallDiscNormal = _CcapAppGblHisPSTNOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 18),
    _CcapAppGblHisPSTNOutCallDiscNormal_Type()
)
ccapAppGblHisPSTNOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallDiscNormal.setStatus("current")
_CcapAppGblHisPSTNOutCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallDiscUsrErr_Object = MibScalar
ccapAppGblHisPSTNOutCallDiscUsrErr = _CcapAppGblHisPSTNOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 19),
    _CcapAppGblHisPSTNOutCallDiscUsrErr_Type()
)
ccapAppGblHisPSTNOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallDiscUsrErr.setStatus("current")
_CcapAppGblHisPSTNOutCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppGblHisPSTNOutCallDiscSysErr_Object = MibScalar
ccapAppGblHisPSTNOutCallDiscSysErr = _CcapAppGblHisPSTNOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 20),
    _CcapAppGblHisPSTNOutCallDiscSysErr_Type()
)
ccapAppGblHisPSTNOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPSTNOutCallDiscSysErr.setStatus("current")
_CcapAppGblHisIPInCallSetupInd_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallSetupInd_Object = MibScalar
ccapAppGblHisIPInCallSetupInd = _CcapAppGblHisIPInCallSetupInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 21),
    _CcapAppGblHisIPInCallSetupInd_Type()
)
ccapAppGblHisIPInCallSetupInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallSetupInd.setStatus("current")
_CcapAppGblHisIPInCallTotConn_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallTotConn_Object = MibScalar
ccapAppGblHisIPInCallTotConn = _CcapAppGblHisIPInCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 22),
    _CcapAppGblHisIPInCallTotConn_Type()
)
ccapAppGblHisIPInCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallTotConn.setStatus("current")
_CcapAppGblHisIPInCallHandedOut_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallHandedOut_Object = MibScalar
ccapAppGblHisIPInCallHandedOut = _CcapAppGblHisIPInCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 23),
    _CcapAppGblHisIPInCallHandedOut_Type()
)
ccapAppGblHisIPInCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallHandedOut.setStatus("current")
_CcapAppGblHisIPInCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallHandOutRet_Object = MibScalar
ccapAppGblHisIPInCallHandOutRet = _CcapAppGblHisIPInCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 24),
    _CcapAppGblHisIPInCallHandOutRet_Type()
)
ccapAppGblHisIPInCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallHandOutRet.setStatus("current")
_CcapAppGblHisIPInCallInHandoff_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallInHandoff_Object = MibScalar
ccapAppGblHisIPInCallInHandoff = _CcapAppGblHisIPInCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 25),
    _CcapAppGblHisIPInCallInHandoff_Type()
)
ccapAppGblHisIPInCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallInHandoff.setStatus("current")
_CcapAppGblHisIPInCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallInHandoffRet_Object = MibScalar
ccapAppGblHisIPInCallInHandoffRet = _CcapAppGblHisIPInCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 26),
    _CcapAppGblHisIPInCallInHandoffRet_Type()
)
ccapAppGblHisIPInCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallInHandoffRet.setStatus("current")
_CcapAppGblHisIPInCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallDiscNormal_Object = MibScalar
ccapAppGblHisIPInCallDiscNormal = _CcapAppGblHisIPInCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 27),
    _CcapAppGblHisIPInCallDiscNormal_Type()
)
ccapAppGblHisIPInCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallDiscNormal.setStatus("current")
_CcapAppGblHisIPInCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallDiscUsrErr_Object = MibScalar
ccapAppGblHisIPInCallDiscUsrErr = _CcapAppGblHisIPInCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 28),
    _CcapAppGblHisIPInCallDiscUsrErr_Type()
)
ccapAppGblHisIPInCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallDiscUsrErr.setStatus("current")
_CcapAppGblHisIPInCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppGblHisIPInCallDiscSysErr_Object = MibScalar
ccapAppGblHisIPInCallDiscSysErr = _CcapAppGblHisIPInCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 29),
    _CcapAppGblHisIPInCallDiscSysErr_Type()
)
ccapAppGblHisIPInCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPInCallDiscSysErr.setStatus("current")
_CcapAppGblHisIPOutCallSetupReq_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallSetupReq_Object = MibScalar
ccapAppGblHisIPOutCallSetupReq = _CcapAppGblHisIPOutCallSetupReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 30),
    _CcapAppGblHisIPOutCallSetupReq_Type()
)
ccapAppGblHisIPOutCallSetupReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallSetupReq.setStatus("current")
_CcapAppGblHisIPOutCallTotConn_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallTotConn_Object = MibScalar
ccapAppGblHisIPOutCallTotConn = _CcapAppGblHisIPOutCallTotConn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 31),
    _CcapAppGblHisIPOutCallTotConn_Type()
)
ccapAppGblHisIPOutCallTotConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallTotConn.setStatus("current")
_CcapAppGblHisIPOutCallHandedOut_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallHandedOut_Object = MibScalar
ccapAppGblHisIPOutCallHandedOut = _CcapAppGblHisIPOutCallHandedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 32),
    _CcapAppGblHisIPOutCallHandedOut_Type()
)
ccapAppGblHisIPOutCallHandedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallHandedOut.setStatus("current")
_CcapAppGblHisIPOutCallHandOutRet_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallHandOutRet_Object = MibScalar
ccapAppGblHisIPOutCallHandOutRet = _CcapAppGblHisIPOutCallHandOutRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 33),
    _CcapAppGblHisIPOutCallHandOutRet_Type()
)
ccapAppGblHisIPOutCallHandOutRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallHandOutRet.setStatus("current")
_CcapAppGblHisIPOutCallInHandoff_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallInHandoff_Object = MibScalar
ccapAppGblHisIPOutCallInHandoff = _CcapAppGblHisIPOutCallInHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 34),
    _CcapAppGblHisIPOutCallInHandoff_Type()
)
ccapAppGblHisIPOutCallInHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallInHandoff.setStatus("current")
_CcapAppGblHisIPOutCallInHandoffRet_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallInHandoffRet_Object = MibScalar
ccapAppGblHisIPOutCallInHandoffRet = _CcapAppGblHisIPOutCallInHandoffRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 35),
    _CcapAppGblHisIPOutCallInHandoffRet_Type()
)
ccapAppGblHisIPOutCallInHandoffRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallInHandoffRet.setStatus("current")
_CcapAppGblHisIPOutCallDiscNormal_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallDiscNormal_Object = MibScalar
ccapAppGblHisIPOutCallDiscNormal = _CcapAppGblHisIPOutCallDiscNormal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 36),
    _CcapAppGblHisIPOutCallDiscNormal_Type()
)
ccapAppGblHisIPOutCallDiscNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallDiscNormal.setStatus("current")
_CcapAppGblHisIPOutCallDiscUsrErr_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallDiscUsrErr_Object = MibScalar
ccapAppGblHisIPOutCallDiscUsrErr = _CcapAppGblHisIPOutCallDiscUsrErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 37),
    _CcapAppGblHisIPOutCallDiscUsrErr_Type()
)
ccapAppGblHisIPOutCallDiscUsrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallDiscUsrErr.setStatus("current")
_CcapAppGblHisIPOutCallDiscSysErr_Type = ZeroBasedCounter32
_CcapAppGblHisIPOutCallDiscSysErr_Object = MibScalar
ccapAppGblHisIPOutCallDiscSysErr = _CcapAppGblHisIPOutCallDiscSysErr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 38),
    _CcapAppGblHisIPOutCallDiscSysErr_Type()
)
ccapAppGblHisIPOutCallDiscSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisIPOutCallDiscSysErr.setStatus("current")
_CcapAppGblHisPlaceCallAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisPlaceCallAttempts_Object = MibScalar
ccapAppGblHisPlaceCallAttempts = _CcapAppGblHisPlaceCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 39),
    _CcapAppGblHisPlaceCallAttempts_Type()
)
ccapAppGblHisPlaceCallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPlaceCallAttempts.setStatus("current")
_CcapAppGblHisPlaceCallSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisPlaceCallSuccess_Object = MibScalar
ccapAppGblHisPlaceCallSuccess = _CcapAppGblHisPlaceCallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 40),
    _CcapAppGblHisPlaceCallSuccess_Type()
)
ccapAppGblHisPlaceCallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPlaceCallSuccess.setStatus("current")
_CcapAppGblHisPlaceCallFailure_Type = ZeroBasedCounter32
_CcapAppGblHisPlaceCallFailure_Object = MibScalar
ccapAppGblHisPlaceCallFailure = _CcapAppGblHisPlaceCallFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 41),
    _CcapAppGblHisPlaceCallFailure_Type()
)
ccapAppGblHisPlaceCallFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPlaceCallFailure.setStatus("current")
_CcapAppGblHisInHandoffCallback_Type = ZeroBasedCounter32
_CcapAppGblHisInHandoffCallback_Object = MibScalar
ccapAppGblHisInHandoffCallback = _CcapAppGblHisInHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 42),
    _CcapAppGblHisInHandoffCallback_Type()
)
ccapAppGblHisInHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisInHandoffCallback.setStatus("current")
_CcapAppGblHisInHandoffCallbackRet_Type = ZeroBasedCounter32
_CcapAppGblHisInHandoffCallbackRet_Object = MibScalar
ccapAppGblHisInHandoffCallbackRet = _CcapAppGblHisInHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 43),
    _CcapAppGblHisInHandoffCallbackRet_Type()
)
ccapAppGblHisInHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisInHandoffCallbackRet.setStatus("current")
_CcapAppGblHisInHandoffNoCallback_Type = ZeroBasedCounter32
_CcapAppGblHisInHandoffNoCallback_Object = MibScalar
ccapAppGblHisInHandoffNoCallback = _CcapAppGblHisInHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 44),
    _CcapAppGblHisInHandoffNoCallback_Type()
)
ccapAppGblHisInHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisInHandoffNoCallback.setStatus("current")
_CcapAppGblHisOutHandoffCallback_Type = ZeroBasedCounter32
_CcapAppGblHisOutHandoffCallback_Object = MibScalar
ccapAppGblHisOutHandoffCallback = _CcapAppGblHisOutHandoffCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 45),
    _CcapAppGblHisOutHandoffCallback_Type()
)
ccapAppGblHisOutHandoffCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisOutHandoffCallback.setStatus("current")
_CcapAppGblHisOutHandoffCallbackRet_Type = ZeroBasedCounter32
_CcapAppGblHisOutHandoffCallbackRet_Object = MibScalar
ccapAppGblHisOutHandoffCallbackRet = _CcapAppGblHisOutHandoffCallbackRet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 46),
    _CcapAppGblHisOutHandoffCallbackRet_Type()
)
ccapAppGblHisOutHandoffCallbackRet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisOutHandoffCallbackRet.setStatus("current")
_CcapAppGblHisOutHandoffNoCallback_Type = ZeroBasedCounter32
_CcapAppGblHisOutHandoffNoCallback_Object = MibScalar
ccapAppGblHisOutHandoffNoCallback = _CcapAppGblHisOutHandoffNoCallback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 47),
    _CcapAppGblHisOutHandoffNoCallback_Type()
)
ccapAppGblHisOutHandoffNoCallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisOutHandoffNoCallback.setStatus("current")
_CcapAppGblHisOutHandofffailures_Type = ZeroBasedCounter32
_CcapAppGblHisOutHandofffailures_Object = MibScalar
ccapAppGblHisOutHandofffailures = _CcapAppGblHisOutHandofffailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 48),
    _CcapAppGblHisOutHandofffailures_Type()
)
ccapAppGblHisOutHandofffailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisOutHandofffailures.setStatus("current")
_CcapAppGblHisDocumentReadAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentReadAttempts_Object = MibScalar
ccapAppGblHisDocumentReadAttempts = _CcapAppGblHisDocumentReadAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 49),
    _CcapAppGblHisDocumentReadAttempts_Type()
)
ccapAppGblHisDocumentReadAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentReadAttempts.setStatus("current")
_CcapAppGblHisDocumentReadSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentReadSuccess_Object = MibScalar
ccapAppGblHisDocumentReadSuccess = _CcapAppGblHisDocumentReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 50),
    _CcapAppGblHisDocumentReadSuccess_Type()
)
ccapAppGblHisDocumentReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentReadSuccess.setStatus("current")
_CcapAppGblHisDocumentReadFailures_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentReadFailures_Object = MibScalar
ccapAppGblHisDocumentReadFailures = _CcapAppGblHisDocumentReadFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 51),
    _CcapAppGblHisDocumentReadFailures_Type()
)
ccapAppGblHisDocumentReadFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentReadFailures.setStatus("current")
_CcapAppGblHisDocumentParseErrors_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentParseErrors_Object = MibScalar
ccapAppGblHisDocumentParseErrors = _CcapAppGblHisDocumentParseErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 52),
    _CcapAppGblHisDocumentParseErrors_Type()
)
ccapAppGblHisDocumentParseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentParseErrors.setStatus("current")
_CcapAppGblHisDocumentWriteAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentWriteAttempts_Object = MibScalar
ccapAppGblHisDocumentWriteAttempts = _CcapAppGblHisDocumentWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 53),
    _CcapAppGblHisDocumentWriteAttempts_Type()
)
ccapAppGblHisDocumentWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentWriteAttempts.setStatus("current")
_CcapAppGblHisDocumentWriteSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentWriteSuccess_Object = MibScalar
ccapAppGblHisDocumentWriteSuccess = _CcapAppGblHisDocumentWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 54),
    _CcapAppGblHisDocumentWriteSuccess_Type()
)
ccapAppGblHisDocumentWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentWriteSuccess.setStatus("current")
_CcapAppGblHisDocumentWriteFailures_Type = ZeroBasedCounter32
_CcapAppGblHisDocumentWriteFailures_Object = MibScalar
ccapAppGblHisDocumentWriteFailures = _CcapAppGblHisDocumentWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 55),
    _CcapAppGblHisDocumentWriteFailures_Type()
)
ccapAppGblHisDocumentWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDocumentWriteFailures.setStatus("current")
_CcapAppGblHisDTMFAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFAttempts_Object = MibScalar
ccapAppGblHisDTMFAttempts = _CcapAppGblHisDTMFAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 56),
    _CcapAppGblHisDTMFAttempts_Type()
)
ccapAppGblHisDTMFAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFAttempts.setStatus("current")
_CcapAppGblHisDTMFAborted_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFAborted_Object = MibScalar
ccapAppGblHisDTMFAborted = _CcapAppGblHisDTMFAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 57),
    _CcapAppGblHisDTMFAborted_Type()
)
ccapAppGblHisDTMFAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFAborted.setStatus("current")
_CcapAppGblHisDTMFNoMatch_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFNoMatch_Object = MibScalar
ccapAppGblHisDTMFNoMatch = _CcapAppGblHisDTMFNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 58),
    _CcapAppGblHisDTMFNoMatch_Type()
)
ccapAppGblHisDTMFNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFNoMatch.setStatus("current")
_CcapAppGblHisDTMFNoInput_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFNoInput_Object = MibScalar
ccapAppGblHisDTMFNoInput = _CcapAppGblHisDTMFNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 59),
    _CcapAppGblHisDTMFNoInput_Type()
)
ccapAppGblHisDTMFNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFNoInput.setStatus("current")
_CcapAppGblHisDTMFMatch_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFMatch_Object = MibScalar
ccapAppGblHisDTMFMatch = _CcapAppGblHisDTMFMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 60),
    _CcapAppGblHisDTMFMatch_Type()
)
ccapAppGblHisDTMFMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFMatch.setStatus("current")
_CcapAppGblHisDTMFLongPound_Type = ZeroBasedCounter32
_CcapAppGblHisDTMFLongPound_Object = MibScalar
ccapAppGblHisDTMFLongPound = _CcapAppGblHisDTMFLongPound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 61),
    _CcapAppGblHisDTMFLongPound_Type()
)
ccapAppGblHisDTMFLongPound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisDTMFLongPound.setStatus("current")
_CcapAppGblHisASRAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisASRAttempts_Object = MibScalar
ccapAppGblHisASRAttempts = _CcapAppGblHisASRAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 62),
    _CcapAppGblHisASRAttempts_Type()
)
ccapAppGblHisASRAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASRAttempts.setStatus("current")
_CcapAppGblHisASRAborted_Type = ZeroBasedCounter32
_CcapAppGblHisASRAborted_Object = MibScalar
ccapAppGblHisASRAborted = _CcapAppGblHisASRAborted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 63),
    _CcapAppGblHisASRAborted_Type()
)
ccapAppGblHisASRAborted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASRAborted.setStatus("current")
_CcapAppGblHisASRNoMatch_Type = ZeroBasedCounter32
_CcapAppGblHisASRNoMatch_Object = MibScalar
ccapAppGblHisASRNoMatch = _CcapAppGblHisASRNoMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 64),
    _CcapAppGblHisASRNoMatch_Type()
)
ccapAppGblHisASRNoMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASRNoMatch.setStatus("current")
_CcapAppGblHisASRNoInput_Type = ZeroBasedCounter32
_CcapAppGblHisASRNoInput_Object = MibScalar
ccapAppGblHisASRNoInput = _CcapAppGblHisASRNoInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 65),
    _CcapAppGblHisASRNoInput_Type()
)
ccapAppGblHisASRNoInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASRNoInput.setStatus("current")
_CcapAppGblHisASRMatch_Type = ZeroBasedCounter32
_CcapAppGblHisASRMatch_Object = MibScalar
ccapAppGblHisASRMatch = _CcapAppGblHisASRMatch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 66),
    _CcapAppGblHisASRMatch_Type()
)
ccapAppGblHisASRMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASRMatch.setStatus("current")
_CcapAppGblHisAAAAuthenticateFailure_Type = ZeroBasedCounter32
_CcapAppGblHisAAAAuthenticateFailure_Object = MibScalar
ccapAppGblHisAAAAuthenticateFailure = _CcapAppGblHisAAAAuthenticateFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 67),
    _CcapAppGblHisAAAAuthenticateFailure_Type()
)
ccapAppGblHisAAAAuthenticateFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisAAAAuthenticateFailure.setStatus("current")
_CcapAppGblHisAAAAuthenticateSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisAAAAuthenticateSuccess_Object = MibScalar
ccapAppGblHisAAAAuthenticateSuccess = _CcapAppGblHisAAAAuthenticateSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 68),
    _CcapAppGblHisAAAAuthenticateSuccess_Type()
)
ccapAppGblHisAAAAuthenticateSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisAAAAuthenticateSuccess.setStatus("current")
_CcapAppGblHisAAAAuthorizeFailure_Type = ZeroBasedCounter32
_CcapAppGblHisAAAAuthorizeFailure_Object = MibScalar
ccapAppGblHisAAAAuthorizeFailure = _CcapAppGblHisAAAAuthorizeFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 69),
    _CcapAppGblHisAAAAuthorizeFailure_Type()
)
ccapAppGblHisAAAAuthorizeFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisAAAAuthorizeFailure.setStatus("current")
_CcapAppGblHisAAAAuthorizeSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisAAAAuthorizeSuccess_Object = MibScalar
ccapAppGblHisAAAAuthorizeSuccess = _CcapAppGblHisAAAAuthorizeSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 70),
    _CcapAppGblHisAAAAuthorizeSuccess_Type()
)
ccapAppGblHisAAAAuthorizeSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisAAAAuthorizeSuccess.setStatus("current")
_CcapAppGblHisASNLSubscriptionsSent_Type = ZeroBasedCounter32
_CcapAppGblHisASNLSubscriptionsSent_Object = MibScalar
ccapAppGblHisASNLSubscriptionsSent = _CcapAppGblHisASNLSubscriptionsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 71),
    _CcapAppGblHisASNLSubscriptionsSent_Type()
)
ccapAppGblHisASNLSubscriptionsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASNLSubscriptionsSent.setStatus("current")
_CcapAppGblHisASNLSubscriptionsSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisASNLSubscriptionsSuccess_Object = MibScalar
ccapAppGblHisASNLSubscriptionsSuccess = _CcapAppGblHisASNLSubscriptionsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 72),
    _CcapAppGblHisASNLSubscriptionsSuccess_Type()
)
ccapAppGblHisASNLSubscriptionsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASNLSubscriptionsSuccess.setStatus("current")
_CcapAppGblHisASNLSubscriptionsFailed_Type = ZeroBasedCounter32
_CcapAppGblHisASNLSubscriptionsFailed_Object = MibScalar
ccapAppGblHisASNLSubscriptionsFailed = _CcapAppGblHisASNLSubscriptionsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 73),
    _CcapAppGblHisASNLSubscriptionsFailed_Type()
)
ccapAppGblHisASNLSubscriptionsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASNLSubscriptionsFailed.setStatus("current")
_CcapAppGblHisASNLNotifReceived_Type = ZeroBasedCounter32
_CcapAppGblHisASNLNotifReceived_Object = MibScalar
ccapAppGblHisASNLNotifReceived = _CcapAppGblHisASNLNotifReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 74),
    _CcapAppGblHisASNLNotifReceived_Type()
)
ccapAppGblHisASNLNotifReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisASNLNotifReceived.setStatus("current")
_CcapAppGblHisPromptPlayAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisPromptPlayAttempts_Object = MibScalar
ccapAppGblHisPromptPlayAttempts = _CcapAppGblHisPromptPlayAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 75),
    _CcapAppGblHisPromptPlayAttempts_Type()
)
ccapAppGblHisPromptPlayAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPromptPlayAttempts.setStatus("current")
_CcapAppGblHisPromptPlaySuccess_Type = ZeroBasedCounter32
_CcapAppGblHisPromptPlaySuccess_Object = MibScalar
ccapAppGblHisPromptPlaySuccess = _CcapAppGblHisPromptPlaySuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 76),
    _CcapAppGblHisPromptPlaySuccess_Type()
)
ccapAppGblHisPromptPlaySuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPromptPlaySuccess.setStatus("current")
_CcapAppGblHisPromptPlayFailed_Type = ZeroBasedCounter32
_CcapAppGblHisPromptPlayFailed_Object = MibScalar
ccapAppGblHisPromptPlayFailed = _CcapAppGblHisPromptPlayFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 77),
    _CcapAppGblHisPromptPlayFailed_Type()
)
ccapAppGblHisPromptPlayFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPromptPlayFailed.setStatus("current")
_CcapAppGblHisPromptPlayDuration_Type = ZeroBasedCounter32
_CcapAppGblHisPromptPlayDuration_Object = MibScalar
ccapAppGblHisPromptPlayDuration = _CcapAppGblHisPromptPlayDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 78),
    _CcapAppGblHisPromptPlayDuration_Type()
)
ccapAppGblHisPromptPlayDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisPromptPlayDuration.setStatus("current")
_CcapAppGblHisRecordingAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisRecordingAttempts_Object = MibScalar
ccapAppGblHisRecordingAttempts = _CcapAppGblHisRecordingAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 79),
    _CcapAppGblHisRecordingAttempts_Type()
)
ccapAppGblHisRecordingAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisRecordingAttempts.setStatus("current")
_CcapAppGblHisRecordingSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisRecordingSuccess_Object = MibScalar
ccapAppGblHisRecordingSuccess = _CcapAppGblHisRecordingSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 80),
    _CcapAppGblHisRecordingSuccess_Type()
)
ccapAppGblHisRecordingSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisRecordingSuccess.setStatus("current")
_CcapAppGblHisRecordingFailed_Type = ZeroBasedCounter32
_CcapAppGblHisRecordingFailed_Object = MibScalar
ccapAppGblHisRecordingFailed = _CcapAppGblHisRecordingFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 81),
    _CcapAppGblHisRecordingFailed_Type()
)
ccapAppGblHisRecordingFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisRecordingFailed.setStatus("current")
_CcapAppGblHisRecordingDuration_Type = ZeroBasedCounter32
_CcapAppGblHisRecordingDuration_Object = MibScalar
ccapAppGblHisRecordingDuration = _CcapAppGblHisRecordingDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 82),
    _CcapAppGblHisRecordingDuration_Type()
)
ccapAppGblHisRecordingDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisRecordingDuration.setStatus("current")
_CcapAppGblHisTTSAttempts_Type = ZeroBasedCounter32
_CcapAppGblHisTTSAttempts_Object = MibScalar
ccapAppGblHisTTSAttempts = _CcapAppGblHisTTSAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 83),
    _CcapAppGblHisTTSAttempts_Type()
)
ccapAppGblHisTTSAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisTTSAttempts.setStatus("current")
_CcapAppGblHisTTSSuccess_Type = ZeroBasedCounter32
_CcapAppGblHisTTSSuccess_Object = MibScalar
ccapAppGblHisTTSSuccess = _CcapAppGblHisTTSSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 84),
    _CcapAppGblHisTTSSuccess_Type()
)
ccapAppGblHisTTSSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisTTSSuccess.setStatus("current")
_CcapAppGblHisTTSFailed_Type = ZeroBasedCounter32
_CcapAppGblHisTTSFailed_Object = MibScalar
ccapAppGblHisTTSFailed = _CcapAppGblHisTTSFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 5, 85),
    _CcapAppGblHisTTSFailed_Type()
)
ccapAppGblHisTTSFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppGblHisTTSFailed.setStatus("current")
_CcapAppIntf_ObjectIdentity = ObjectIdentity
ccapAppIntf = _CcapAppIntf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6)
)


class _CcapAppIntfGblStatsLogging_Type(Integer32):
    """Custom type ccapAppIntfGblStatsLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfGblStatsLogging_Type.__name__ = "Integer32"
_CcapAppIntfGblStatsLogging_Object = MibScalar
ccapAppIntfGblStatsLogging = _CcapAppIntfGblStatsLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 1),
    _CcapAppIntfGblStatsLogging_Type()
)
ccapAppIntfGblStatsLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppIntfGblStatsLogging.setStatus("current")


class _CcapAppIntfGblEventLogging_Type(Integer32):
    """Custom type ccapAppIntfGblEventLogging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfGblEventLogging_Type.__name__ = "Integer32"
_CcapAppIntfGblEventLogging_Object = MibScalar
ccapAppIntfGblEventLogging = _CcapAppIntfGblEventLogging_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 2),
    _CcapAppIntfGblEventLogging_Type()
)
ccapAppIntfGblEventLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppIntfGblEventLogging.setStatus("current")


class _CcapAppIntfGblEvtLogFlush_Type(Integer32):
    """Custom type ccapAppIntfGblEvtLogFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ftp", 1)
    )


_CcapAppIntfGblEvtLogFlush_Type.__name__ = "Integer32"
_CcapAppIntfGblEvtLogFlush_Object = MibScalar
ccapAppIntfGblEvtLogFlush = _CcapAppIntfGblEvtLogFlush_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 3),
    _CcapAppIntfGblEvtLogFlush_Type()
)
ccapAppIntfGblEvtLogFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppIntfGblEvtLogFlush.setStatus("current")


class _CcapAppIntfGblStatsClear_Type(Integer32):
    """Custom type ccapAppIntfGblStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("clearEventlog", 2),
          ("clearStats", 1))
    )


_CcapAppIntfGblStatsClear_Type.__name__ = "Integer32"
_CcapAppIntfGblStatsClear_Object = MibScalar
ccapAppIntfGblStatsClear = _CcapAppIntfGblStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 4),
    _CcapAppIntfGblStatsClear_Type()
)
ccapAppIntfGblStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccapAppIntfGblStatsClear.setStatus("current")
_CcapAppIntfGblLastResetTime_Type = TimeStamp
_CcapAppIntfGblLastResetTime_Object = MibScalar
ccapAppIntfGblLastResetTime = _CcapAppIntfGblLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 5),
    _CcapAppIntfGblLastResetTime_Type()
)
ccapAppIntfGblLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfGblLastResetTime.setStatus("current")
_CcapAppIntfHTTPTable_Object = MibTable
ccapAppIntfHTTPTable = _CcapAppIntfHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8)
)
if mibBuilder.loadTexts:
    ccapAppIntfHTTPTable.setStatus("current")
_CcapAppIntfHTTPEntry_Object = MibTableRow
ccapAppIntfHTTPEntry = _CcapAppIntfHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1)
)
ccapAppIntfHTTPEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfHTTPEntry.setStatus("current")
_CcapAppIntfHTTPServer_Type = ServerNameString
_CcapAppIntfHTTPServer_Object = MibTableColumn
ccapAppIntfHTTPServer = _CcapAppIntfHTTPServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 1),
    _CcapAppIntfHTTPServer_Type()
)
ccapAppIntfHTTPServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPServer.setStatus("current")


class _CcapAppIntfHTTPStats_Type(Integer32):
    """Custom type ccapAppIntfHTTPStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfHTTPStats_Type.__name__ = "Integer32"
_CcapAppIntfHTTPStats_Object = MibTableColumn
ccapAppIntfHTTPStats = _CcapAppIntfHTTPStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 2),
    _CcapAppIntfHTTPStats_Type()
)
ccapAppIntfHTTPStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPStats.setStatus("current")


class _CcapAppIntfHTTPEvtLog_Type(Integer32):
    """Custom type ccapAppIntfHTTPEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfHTTPEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfHTTPEvtLog_Object = MibTableColumn
ccapAppIntfHTTPEvtLog = _CcapAppIntfHTTPEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 3),
    _CcapAppIntfHTTPEvtLog_Type()
)
ccapAppIntfHTTPEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPEvtLog.setStatus("current")
_CcapAppIntfHTTPGetRequest_Type = ZeroBasedCounter32
_CcapAppIntfHTTPGetRequest_Object = MibTableColumn
ccapAppIntfHTTPGetRequest = _CcapAppIntfHTTPGetRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 4),
    _CcapAppIntfHTTPGetRequest_Type()
)
ccapAppIntfHTTPGetRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPGetRequest.setStatus("current")
_CcapAppIntfHTTPGetSuccess_Type = ZeroBasedCounter32
_CcapAppIntfHTTPGetSuccess_Object = MibTableColumn
ccapAppIntfHTTPGetSuccess = _CcapAppIntfHTTPGetSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 5),
    _CcapAppIntfHTTPGetSuccess_Type()
)
ccapAppIntfHTTPGetSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPGetSuccess.setStatus("current")
_CcapAppIntfHTTPGetFailure_Type = ZeroBasedCounter32
_CcapAppIntfHTTPGetFailure_Object = MibTableColumn
ccapAppIntfHTTPGetFailure = _CcapAppIntfHTTPGetFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 6),
    _CcapAppIntfHTTPGetFailure_Type()
)
ccapAppIntfHTTPGetFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPGetFailure.setStatus("current")
_CcapAppIntfHTTPPostRequest_Type = ZeroBasedCounter32
_CcapAppIntfHTTPPostRequest_Object = MibTableColumn
ccapAppIntfHTTPPostRequest = _CcapAppIntfHTTPPostRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 7),
    _CcapAppIntfHTTPPostRequest_Type()
)
ccapAppIntfHTTPPostRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPPostRequest.setStatus("current")
_CcapAppIntfHTTPPostSuccess_Type = ZeroBasedCounter32
_CcapAppIntfHTTPPostSuccess_Object = MibTableColumn
ccapAppIntfHTTPPostSuccess = _CcapAppIntfHTTPPostSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 8),
    _CcapAppIntfHTTPPostSuccess_Type()
)
ccapAppIntfHTTPPostSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPPostSuccess.setStatus("current")
_CcapAppIntfHTTPPostFailure_Type = ZeroBasedCounter32
_CcapAppIntfHTTPPostFailure_Object = MibTableColumn
ccapAppIntfHTTPPostFailure = _CcapAppIntfHTTPPostFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 9),
    _CcapAppIntfHTTPPostFailure_Type()
)
ccapAppIntfHTTPPostFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPPostFailure.setStatus("current")
_CcapAppIntfHTTPTxBytes_Type = ZeroBasedCounter32
_CcapAppIntfHTTPTxBytes_Object = MibTableColumn
ccapAppIntfHTTPTxBytes = _CcapAppIntfHTTPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 10),
    _CcapAppIntfHTTPTxBytes_Type()
)
ccapAppIntfHTTPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPTxBytes.setStatus("current")
_CcapAppIntfHTTPRxBytes_Type = ZeroBasedCounter32
_CcapAppIntfHTTPRxBytes_Object = MibTableColumn
ccapAppIntfHTTPRxBytes = _CcapAppIntfHTTPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 11),
    _CcapAppIntfHTTPRxBytes_Type()
)
ccapAppIntfHTTPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPRxBytes.setStatus("current")
_CcapAppIntfHTTPMinXferRate_Type = ZeroBasedCounter32
_CcapAppIntfHTTPMinXferRate_Object = MibTableColumn
ccapAppIntfHTTPMinXferRate = _CcapAppIntfHTTPMinXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 12),
    _CcapAppIntfHTTPMinXferRate_Type()
)
ccapAppIntfHTTPMinXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPMinXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPMinXferRate.setUnits("KBytes/second")
_CcapAppIntfHTTPMaxXferRate_Type = ZeroBasedCounter32
_CcapAppIntfHTTPMaxXferRate_Object = MibTableColumn
ccapAppIntfHTTPMaxXferRate = _CcapAppIntfHTTPMaxXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 13),
    _CcapAppIntfHTTPMaxXferRate_Type()
)
ccapAppIntfHTTPMaxXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPMaxXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPMaxXferRate.setUnits("KBytes/second")
_CcapAppIntfHTTPAvgXferRate_Type = ZeroBasedCounter32
_CcapAppIntfHTTPAvgXferRate_Object = MibTableColumn
ccapAppIntfHTTPAvgXferRate = _CcapAppIntfHTTPAvgXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 14),
    _CcapAppIntfHTTPAvgXferRate_Type()
)
ccapAppIntfHTTPAvgXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPAvgXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPAvgXferRate.setUnits("KBytes/second")
_CcapAppIntfHTTPLastResetTime_Type = TimeStamp
_CcapAppIntfHTTPLastResetTime_Object = MibTableColumn
ccapAppIntfHTTPLastResetTime = _CcapAppIntfHTTPLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 8, 1, 15),
    _CcapAppIntfHTTPLastResetTime_Type()
)
ccapAppIntfHTTPLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfHTTPLastResetTime.setStatus("current")
_CcapAppIntfRTSPTable_Object = MibTable
ccapAppIntfRTSPTable = _CcapAppIntfRTSPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9)
)
if mibBuilder.loadTexts:
    ccapAppIntfRTSPTable.setStatus("current")
_CcapAppIntfRTSPEntry_Object = MibTableRow
ccapAppIntfRTSPEntry = _CcapAppIntfRTSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1)
)
ccapAppIntfRTSPEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfRTSPEntry.setStatus("current")
_CcapAppIntfRTSPServer_Type = ServerNameString
_CcapAppIntfRTSPServer_Object = MibTableColumn
ccapAppIntfRTSPServer = _CcapAppIntfRTSPServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 1),
    _CcapAppIntfRTSPServer_Type()
)
ccapAppIntfRTSPServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPServer.setStatus("current")


class _CcapAppIntfRTSPStats_Type(Integer32):
    """Custom type ccapAppIntfRTSPStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfRTSPStats_Type.__name__ = "Integer32"
_CcapAppIntfRTSPStats_Object = MibTableColumn
ccapAppIntfRTSPStats = _CcapAppIntfRTSPStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 2),
    _CcapAppIntfRTSPStats_Type()
)
ccapAppIntfRTSPStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPStats.setStatus("current")


class _CcapAppIntfRTSPEvtLog_Type(Integer32):
    """Custom type ccapAppIntfRTSPEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfRTSPEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfRTSPEvtLog_Object = MibTableColumn
ccapAppIntfRTSPEvtLog = _CcapAppIntfRTSPEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 3),
    _CcapAppIntfRTSPEvtLog_Type()
)
ccapAppIntfRTSPEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPEvtLog.setStatus("current")
_CcapAppIntfRTSPReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfRTSPReadRequest_Object = MibTableColumn
ccapAppIntfRTSPReadRequest = _CcapAppIntfRTSPReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 4),
    _CcapAppIntfRTSPReadRequest_Type()
)
ccapAppIntfRTSPReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPReadRequest.setStatus("current")
_CcapAppIntfRTSPReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfRTSPReadSuccess_Object = MibTableColumn
ccapAppIntfRTSPReadSuccess = _CcapAppIntfRTSPReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 5),
    _CcapAppIntfRTSPReadSuccess_Type()
)
ccapAppIntfRTSPReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPReadSuccess.setStatus("current")
_CcapAppIntfRTSPReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfRTSPReadFailure_Object = MibTableColumn
ccapAppIntfRTSPReadFailure = _CcapAppIntfRTSPReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 6),
    _CcapAppIntfRTSPReadFailure_Type()
)
ccapAppIntfRTSPReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPReadFailure.setStatus("current")
_CcapAppIntfRTSPWriteRequest_Type = ZeroBasedCounter32
_CcapAppIntfRTSPWriteRequest_Object = MibTableColumn
ccapAppIntfRTSPWriteRequest = _CcapAppIntfRTSPWriteRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 7),
    _CcapAppIntfRTSPWriteRequest_Type()
)
ccapAppIntfRTSPWriteRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPWriteRequest.setStatus("current")
_CcapAppIntfRTSPWriteSuccess_Type = ZeroBasedCounter32
_CcapAppIntfRTSPWriteSuccess_Object = MibTableColumn
ccapAppIntfRTSPWriteSuccess = _CcapAppIntfRTSPWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 8),
    _CcapAppIntfRTSPWriteSuccess_Type()
)
ccapAppIntfRTSPWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPWriteSuccess.setStatus("current")
_CcapAppIntfRTSPWriteFailure_Type = ZeroBasedCounter32
_CcapAppIntfRTSPWriteFailure_Object = MibTableColumn
ccapAppIntfRTSPWriteFailure = _CcapAppIntfRTSPWriteFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 9),
    _CcapAppIntfRTSPWriteFailure_Type()
)
ccapAppIntfRTSPWriteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPWriteFailure.setStatus("current")
_CcapAppIntfRTSPTxBytes_Type = ZeroBasedCounter32
_CcapAppIntfRTSPTxBytes_Object = MibTableColumn
ccapAppIntfRTSPTxBytes = _CcapAppIntfRTSPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 10),
    _CcapAppIntfRTSPTxBytes_Type()
)
ccapAppIntfRTSPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPTxBytes.setStatus("current")
_CcapAppIntfRTSPRxBytes_Type = ZeroBasedCounter32
_CcapAppIntfRTSPRxBytes_Object = MibTableColumn
ccapAppIntfRTSPRxBytes = _CcapAppIntfRTSPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 11),
    _CcapAppIntfRTSPRxBytes_Type()
)
ccapAppIntfRTSPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPRxBytes.setStatus("current")
_CcapAppIntfRTSPMinXferRate_Type = ZeroBasedCounter32
_CcapAppIntfRTSPMinXferRate_Object = MibTableColumn
ccapAppIntfRTSPMinXferRate = _CcapAppIntfRTSPMinXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 12),
    _CcapAppIntfRTSPMinXferRate_Type()
)
ccapAppIntfRTSPMinXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPMinXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPMinXferRate.setUnits("KBytes/second")
_CcapAppIntfRTSPMaxXferRate_Type = ZeroBasedCounter32
_CcapAppIntfRTSPMaxXferRate_Object = MibTableColumn
ccapAppIntfRTSPMaxXferRate = _CcapAppIntfRTSPMaxXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 13),
    _CcapAppIntfRTSPMaxXferRate_Type()
)
ccapAppIntfRTSPMaxXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPMaxXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPMaxXferRate.setUnits("KBytes/second")
_CcapAppIntfRTSPAvgXferRate_Type = ZeroBasedCounter32
_CcapAppIntfRTSPAvgXferRate_Object = MibTableColumn
ccapAppIntfRTSPAvgXferRate = _CcapAppIntfRTSPAvgXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 14),
    _CcapAppIntfRTSPAvgXferRate_Type()
)
ccapAppIntfRTSPAvgXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPAvgXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPAvgXferRate.setUnits("KBytes/second")
_CcapAppIntfRTSPLastResetTime_Type = TimeStamp
_CcapAppIntfRTSPLastResetTime_Object = MibTableColumn
ccapAppIntfRTSPLastResetTime = _CcapAppIntfRTSPLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 9, 1, 15),
    _CcapAppIntfRTSPLastResetTime_Type()
)
ccapAppIntfRTSPLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRTSPLastResetTime.setStatus("current")
_CcapAppIntfTFTPTable_Object = MibTable
ccapAppIntfTFTPTable = _CcapAppIntfTFTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10)
)
if mibBuilder.loadTexts:
    ccapAppIntfTFTPTable.setStatus("current")
_CcapAppIntfTFTPEntry_Object = MibTableRow
ccapAppIntfTFTPEntry = _CcapAppIntfTFTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1)
)
ccapAppIntfTFTPEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfTFTPEntry.setStatus("current")
_CcapAppIntfTFTPServer_Type = ServerNameString
_CcapAppIntfTFTPServer_Object = MibTableColumn
ccapAppIntfTFTPServer = _CcapAppIntfTFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 1),
    _CcapAppIntfTFTPServer_Type()
)
ccapAppIntfTFTPServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPServer.setStatus("current")


class _CcapAppIntfTFTPStats_Type(Integer32):
    """Custom type ccapAppIntfTFTPStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfTFTPStats_Type.__name__ = "Integer32"
_CcapAppIntfTFTPStats_Object = MibTableColumn
ccapAppIntfTFTPStats = _CcapAppIntfTFTPStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 2),
    _CcapAppIntfTFTPStats_Type()
)
ccapAppIntfTFTPStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPStats.setStatus("current")


class _CcapAppIntfTFTPEvtLog_Type(Integer32):
    """Custom type ccapAppIntfTFTPEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfTFTPEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfTFTPEvtLog_Object = MibTableColumn
ccapAppIntfTFTPEvtLog = _CcapAppIntfTFTPEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 3),
    _CcapAppIntfTFTPEvtLog_Type()
)
ccapAppIntfTFTPEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPEvtLog.setStatus("current")
_CcapAppIntfTFTPReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfTFTPReadRequest_Object = MibTableColumn
ccapAppIntfTFTPReadRequest = _CcapAppIntfTFTPReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 4),
    _CcapAppIntfTFTPReadRequest_Type()
)
ccapAppIntfTFTPReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPReadRequest.setStatus("current")
_CcapAppIntfTFTPReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfTFTPReadSuccess_Object = MibTableColumn
ccapAppIntfTFTPReadSuccess = _CcapAppIntfTFTPReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 5),
    _CcapAppIntfTFTPReadSuccess_Type()
)
ccapAppIntfTFTPReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPReadSuccess.setStatus("current")
_CcapAppIntfTFTPReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfTFTPReadFailure_Object = MibTableColumn
ccapAppIntfTFTPReadFailure = _CcapAppIntfTFTPReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 6),
    _CcapAppIntfTFTPReadFailure_Type()
)
ccapAppIntfTFTPReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPReadFailure.setStatus("current")
_CcapAppIntfTFTPWriteRequest_Type = ZeroBasedCounter32
_CcapAppIntfTFTPWriteRequest_Object = MibTableColumn
ccapAppIntfTFTPWriteRequest = _CcapAppIntfTFTPWriteRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 7),
    _CcapAppIntfTFTPWriteRequest_Type()
)
ccapAppIntfTFTPWriteRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPWriteRequest.setStatus("current")
_CcapAppIntfTFTPWriteSuccess_Type = ZeroBasedCounter32
_CcapAppIntfTFTPWriteSuccess_Object = MibTableColumn
ccapAppIntfTFTPWriteSuccess = _CcapAppIntfTFTPWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 8),
    _CcapAppIntfTFTPWriteSuccess_Type()
)
ccapAppIntfTFTPWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPWriteSuccess.setStatus("current")
_CcapAppIntfTFTPWriteFailure_Type = ZeroBasedCounter32
_CcapAppIntfTFTPWriteFailure_Object = MibTableColumn
ccapAppIntfTFTPWriteFailure = _CcapAppIntfTFTPWriteFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 9),
    _CcapAppIntfTFTPWriteFailure_Type()
)
ccapAppIntfTFTPWriteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPWriteFailure.setStatus("current")
_CcapAppIntfTFTPTxBytes_Type = ZeroBasedCounter32
_CcapAppIntfTFTPTxBytes_Object = MibTableColumn
ccapAppIntfTFTPTxBytes = _CcapAppIntfTFTPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 10),
    _CcapAppIntfTFTPTxBytes_Type()
)
ccapAppIntfTFTPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPTxBytes.setStatus("current")
_CcapAppIntfTFTPRxBytes_Type = ZeroBasedCounter32
_CcapAppIntfTFTPRxBytes_Object = MibTableColumn
ccapAppIntfTFTPRxBytes = _CcapAppIntfTFTPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 11),
    _CcapAppIntfTFTPRxBytes_Type()
)
ccapAppIntfTFTPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPRxBytes.setStatus("current")
_CcapAppIntfTFTPMinXferRate_Type = ZeroBasedCounter32
_CcapAppIntfTFTPMinXferRate_Object = MibTableColumn
ccapAppIntfTFTPMinXferRate = _CcapAppIntfTFTPMinXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 12),
    _CcapAppIntfTFTPMinXferRate_Type()
)
ccapAppIntfTFTPMinXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPMinXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPMinXferRate.setUnits("KBytes/second")
_CcapAppIntfTFTPMaxXferRate_Type = ZeroBasedCounter32
_CcapAppIntfTFTPMaxXferRate_Object = MibTableColumn
ccapAppIntfTFTPMaxXferRate = _CcapAppIntfTFTPMaxXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 13),
    _CcapAppIntfTFTPMaxXferRate_Type()
)
ccapAppIntfTFTPMaxXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPMaxXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPMaxXferRate.setUnits("KBytes/second")
_CcapAppIntfTFTPAvgXferRate_Type = ZeroBasedCounter32
_CcapAppIntfTFTPAvgXferRate_Object = MibTableColumn
ccapAppIntfTFTPAvgXferRate = _CcapAppIntfTFTPAvgXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 14),
    _CcapAppIntfTFTPAvgXferRate_Type()
)
ccapAppIntfTFTPAvgXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPAvgXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPAvgXferRate.setUnits("KBytes/second")
_CcapAppIntfTFTPLastResetTime_Type = TimeStamp
_CcapAppIntfTFTPLastResetTime_Object = MibTableColumn
ccapAppIntfTFTPLastResetTime = _CcapAppIntfTFTPLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 10, 1, 15),
    _CcapAppIntfTFTPLastResetTime_Type()
)
ccapAppIntfTFTPLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTFTPLastResetTime.setStatus("current")
_CcapAppIntfFlashReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfFlashReadRequest_Object = MibScalar
ccapAppIntfFlashReadRequest = _CcapAppIntfFlashReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 11),
    _CcapAppIntfFlashReadRequest_Type()
)
ccapAppIntfFlashReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfFlashReadRequest.setStatus("current")
_CcapAppIntfFlashReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfFlashReadSuccess_Object = MibScalar
ccapAppIntfFlashReadSuccess = _CcapAppIntfFlashReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 12),
    _CcapAppIntfFlashReadSuccess_Type()
)
ccapAppIntfFlashReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfFlashReadSuccess.setStatus("current")
_CcapAppIntfFlashReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfFlashReadFailure_Object = MibScalar
ccapAppIntfFlashReadFailure = _CcapAppIntfFlashReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 13),
    _CcapAppIntfFlashReadFailure_Type()
)
ccapAppIntfFlashReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfFlashReadFailure.setStatus("current")
_CcapAppIntfRAMRecordReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordReadRequest_Object = MibScalar
ccapAppIntfRAMRecordReadRequest = _CcapAppIntfRAMRecordReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 14),
    _CcapAppIntfRAMRecordReadRequest_Type()
)
ccapAppIntfRAMRecordReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordReadRequest.setStatus("current")
_CcapAppIntfRAMRecordReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordReadSuccess_Object = MibScalar
ccapAppIntfRAMRecordReadSuccess = _CcapAppIntfRAMRecordReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 15),
    _CcapAppIntfRAMRecordReadSuccess_Type()
)
ccapAppIntfRAMRecordReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordReadSuccess.setStatus("current")
_CcapAppIntfRAMRecordiongReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordiongReadFailure_Object = MibScalar
ccapAppIntfRAMRecordiongReadFailure = _CcapAppIntfRAMRecordiongReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 16),
    _CcapAppIntfRAMRecordiongReadFailure_Type()
)
ccapAppIntfRAMRecordiongReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordiongReadFailure.setStatus("current")
_CcapAppIntfRAMRecordRequest_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordRequest_Object = MibScalar
ccapAppIntfRAMRecordRequest = _CcapAppIntfRAMRecordRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 17),
    _CcapAppIntfRAMRecordRequest_Type()
)
ccapAppIntfRAMRecordRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordRequest.setStatus("current")
_CcapAppIntfRAMRecordSuccess_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordSuccess_Object = MibScalar
ccapAppIntfRAMRecordSuccess = _CcapAppIntfRAMRecordSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 18),
    _CcapAppIntfRAMRecordSuccess_Type()
)
ccapAppIntfRAMRecordSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordSuccess.setStatus("current")
_CcapAppIntfRAMRecordiongFailure_Type = ZeroBasedCounter32
_CcapAppIntfRAMRecordiongFailure_Object = MibScalar
ccapAppIntfRAMRecordiongFailure = _CcapAppIntfRAMRecordiongFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 19),
    _CcapAppIntfRAMRecordiongFailure_Type()
)
ccapAppIntfRAMRecordiongFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordiongFailure.setStatus("current")
_CcapAppIntfSMTPTable_Object = MibTable
ccapAppIntfSMTPTable = _CcapAppIntfSMTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20)
)
if mibBuilder.loadTexts:
    ccapAppIntfSMTPTable.setStatus("current")
_CcapAppIntfSMTPEntry_Object = MibTableRow
ccapAppIntfSMTPEntry = _CcapAppIntfSMTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1)
)
ccapAppIntfSMTPEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfSMTPEntry.setStatus("current")
_CcapAppIntfSMTPServer_Type = ServerNameString
_CcapAppIntfSMTPServer_Object = MibTableColumn
ccapAppIntfSMTPServer = _CcapAppIntfSMTPServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 1),
    _CcapAppIntfSMTPServer_Type()
)
ccapAppIntfSMTPServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPServer.setStatus("current")


class _CcapAppIntfSMTPStats_Type(Integer32):
    """Custom type ccapAppIntfSMTPStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfSMTPStats_Type.__name__ = "Integer32"
_CcapAppIntfSMTPStats_Object = MibTableColumn
ccapAppIntfSMTPStats = _CcapAppIntfSMTPStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 2),
    _CcapAppIntfSMTPStats_Type()
)
ccapAppIntfSMTPStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPStats.setStatus("current")


class _CcapAppIntfSMTPEvtLog_Type(Integer32):
    """Custom type ccapAppIntfSMTPEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfSMTPEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfSMTPEvtLog_Object = MibTableColumn
ccapAppIntfSMTPEvtLog = _CcapAppIntfSMTPEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 3),
    _CcapAppIntfSMTPEvtLog_Type()
)
ccapAppIntfSMTPEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPEvtLog.setStatus("current")
_CcapAppIntfSMTPReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfSMTPReadRequest_Object = MibTableColumn
ccapAppIntfSMTPReadRequest = _CcapAppIntfSMTPReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 4),
    _CcapAppIntfSMTPReadRequest_Type()
)
ccapAppIntfSMTPReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPReadRequest.setStatus("current")
_CcapAppIntfSMTPReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfSMTPReadSuccess_Object = MibTableColumn
ccapAppIntfSMTPReadSuccess = _CcapAppIntfSMTPReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 5),
    _CcapAppIntfSMTPReadSuccess_Type()
)
ccapAppIntfSMTPReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPReadSuccess.setStatus("current")
_CcapAppIntfSMTPReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfSMTPReadFailure_Object = MibTableColumn
ccapAppIntfSMTPReadFailure = _CcapAppIntfSMTPReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 6),
    _CcapAppIntfSMTPReadFailure_Type()
)
ccapAppIntfSMTPReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPReadFailure.setStatus("current")
_CcapAppIntfSMTPWriteRequest_Type = ZeroBasedCounter32
_CcapAppIntfSMTPWriteRequest_Object = MibTableColumn
ccapAppIntfSMTPWriteRequest = _CcapAppIntfSMTPWriteRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 7),
    _CcapAppIntfSMTPWriteRequest_Type()
)
ccapAppIntfSMTPWriteRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPWriteRequest.setStatus("current")
_CcapAppIntfSMTPWriteSuccess_Type = ZeroBasedCounter32
_CcapAppIntfSMTPWriteSuccess_Object = MibTableColumn
ccapAppIntfSMTPWriteSuccess = _CcapAppIntfSMTPWriteSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 8),
    _CcapAppIntfSMTPWriteSuccess_Type()
)
ccapAppIntfSMTPWriteSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPWriteSuccess.setStatus("current")
_CcapAppIntfSMTPWriteFailure_Type = ZeroBasedCounter32
_CcapAppIntfSMTPWriteFailure_Object = MibTableColumn
ccapAppIntfSMTPWriteFailure = _CcapAppIntfSMTPWriteFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 9),
    _CcapAppIntfSMTPWriteFailure_Type()
)
ccapAppIntfSMTPWriteFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPWriteFailure.setStatus("current")
_CcapAppIntfSMTPTxBytes_Type = ZeroBasedCounter32
_CcapAppIntfSMTPTxBytes_Object = MibTableColumn
ccapAppIntfSMTPTxBytes = _CcapAppIntfSMTPTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 10),
    _CcapAppIntfSMTPTxBytes_Type()
)
ccapAppIntfSMTPTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPTxBytes.setStatus("current")
_CcapAppIntfSMTPRxBytes_Type = ZeroBasedCounter32
_CcapAppIntfSMTPRxBytes_Object = MibTableColumn
ccapAppIntfSMTPRxBytes = _CcapAppIntfSMTPRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 11),
    _CcapAppIntfSMTPRxBytes_Type()
)
ccapAppIntfSMTPRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPRxBytes.setStatus("current")
_CcapAppIntfSMTPMinXferRate_Type = ZeroBasedCounter32
_CcapAppIntfSMTPMinXferRate_Object = MibTableColumn
ccapAppIntfSMTPMinXferRate = _CcapAppIntfSMTPMinXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 12),
    _CcapAppIntfSMTPMinXferRate_Type()
)
ccapAppIntfSMTPMinXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPMinXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPMinXferRate.setUnits("KBytes/second")
_CcapAppIntfSMTPMaxXferRate_Type = ZeroBasedCounter32
_CcapAppIntfSMTPMaxXferRate_Object = MibTableColumn
ccapAppIntfSMTPMaxXferRate = _CcapAppIntfSMTPMaxXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 13),
    _CcapAppIntfSMTPMaxXferRate_Type()
)
ccapAppIntfSMTPMaxXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPMaxXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPMaxXferRate.setUnits("KBytes/second")
_CcapAppIntfSMTPAvgXferRate_Type = ZeroBasedCounter32
_CcapAppIntfSMTPAvgXferRate_Object = MibTableColumn
ccapAppIntfSMTPAvgXferRate = _CcapAppIntfSMTPAvgXferRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 14),
    _CcapAppIntfSMTPAvgXferRate_Type()
)
ccapAppIntfSMTPAvgXferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPAvgXferRate.setStatus("current")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPAvgXferRate.setUnits("KBytes/second")
_CcapAppIntfSMTPLastResetTime_Type = TimeStamp
_CcapAppIntfSMTPLastResetTime_Object = MibTableColumn
ccapAppIntfSMTPLastResetTime = _CcapAppIntfSMTPLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 20, 1, 15),
    _CcapAppIntfSMTPLastResetTime_Type()
)
ccapAppIntfSMTPLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfSMTPLastResetTime.setStatus("current")
_CcapAppIntfAAAMethodListTable_Object = MibTable
ccapAppIntfAAAMethodListTable = _CcapAppIntfAAAMethodListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21)
)
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListTable.setStatus("current")
_CcapAppIntfAAAMethodListEntry_Object = MibTableRow
ccapAppIntfAAAMethodListEntry = _CcapAppIntfAAAMethodListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1)
)
ccapAppIntfAAAMethodListEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListEntry.setStatus("current")


class _CcapAppIntfAAAMethodListServer_Type(SnmpAdminString):
    """Custom type ccapAppIntfAAAMethodListServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CcapAppIntfAAAMethodListServer_Type.__name__ = "SnmpAdminString"
_CcapAppIntfAAAMethodListServer_Object = MibTableColumn
ccapAppIntfAAAMethodListServer = _CcapAppIntfAAAMethodListServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 1),
    _CcapAppIntfAAAMethodListServer_Type()
)
ccapAppIntfAAAMethodListServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListServer.setStatus("current")


class _CcapAppIntfAAAMethodListStats_Type(Integer32):
    """Custom type ccapAppIntfAAAMethodListStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfAAAMethodListStats_Type.__name__ = "Integer32"
_CcapAppIntfAAAMethodListStats_Object = MibTableColumn
ccapAppIntfAAAMethodListStats = _CcapAppIntfAAAMethodListStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 2),
    _CcapAppIntfAAAMethodListStats_Type()
)
ccapAppIntfAAAMethodListStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListStats.setStatus("current")


class _CcapAppIntfAAAMethodListEvtLog_Type(Integer32):
    """Custom type ccapAppIntfAAAMethodListEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfAAAMethodListEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfAAAMethodListEvtLog_Object = MibTableColumn
ccapAppIntfAAAMethodListEvtLog = _CcapAppIntfAAAMethodListEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 3),
    _CcapAppIntfAAAMethodListEvtLog_Type()
)
ccapAppIntfAAAMethodListEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListEvtLog.setStatus("current")
_CcapAppIntfAAAMethodListReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfAAAMethodListReadRequest_Object = MibTableColumn
ccapAppIntfAAAMethodListReadRequest = _CcapAppIntfAAAMethodListReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 4),
    _CcapAppIntfAAAMethodListReadRequest_Type()
)
ccapAppIntfAAAMethodListReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListReadRequest.setStatus("current")
_CcapAppIntfAAAMethodListReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfAAAMethodListReadSuccess_Object = MibTableColumn
ccapAppIntfAAAMethodListReadSuccess = _CcapAppIntfAAAMethodListReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 5),
    _CcapAppIntfAAAMethodListReadSuccess_Type()
)
ccapAppIntfAAAMethodListReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListReadSuccess.setStatus("current")
_CcapAppIntfAAAMethodListReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfAAAMethodListReadFailure_Object = MibTableColumn
ccapAppIntfAAAMethodListReadFailure = _CcapAppIntfAAAMethodListReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 6),
    _CcapAppIntfAAAMethodListReadFailure_Type()
)
ccapAppIntfAAAMethodListReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListReadFailure.setStatus("current")
_CcapAppIntfAAAMethodListLastResetTime_Type = TimeStamp
_CcapAppIntfAAAMethodListLastResetTime_Object = MibTableColumn
ccapAppIntfAAAMethodListLastResetTime = _CcapAppIntfAAAMethodListLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 21, 1, 7),
    _CcapAppIntfAAAMethodListLastResetTime_Type()
)
ccapAppIntfAAAMethodListLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListLastResetTime.setStatus("current")
_CcapAppIntfASRTable_Object = MibTable
ccapAppIntfASRTable = _CcapAppIntfASRTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22)
)
if mibBuilder.loadTexts:
    ccapAppIntfASRTable.setStatus("current")
_CcapAppIntfASREntry_Object = MibTableRow
ccapAppIntfASREntry = _CcapAppIntfASREntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1)
)
ccapAppIntfASREntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfASREntry.setStatus("current")
_CcapAppIntfASRServer_Type = ServerNameString
_CcapAppIntfASRServer_Object = MibTableColumn
ccapAppIntfASRServer = _CcapAppIntfASRServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 1),
    _CcapAppIntfASRServer_Type()
)
ccapAppIntfASRServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfASRServer.setStatus("current")


class _CcapAppIntfASRStats_Type(Integer32):
    """Custom type ccapAppIntfASRStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfASRStats_Type.__name__ = "Integer32"
_CcapAppIntfASRStats_Object = MibTableColumn
ccapAppIntfASRStats = _CcapAppIntfASRStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 2),
    _CcapAppIntfASRStats_Type()
)
ccapAppIntfASRStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASRStats.setStatus("current")


class _CcapAppIntfASREvtLog_Type(Integer32):
    """Custom type ccapAppIntfASREvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfASREvtLog_Type.__name__ = "Integer32"
_CcapAppIntfASREvtLog_Object = MibTableColumn
ccapAppIntfASREvtLog = _CcapAppIntfASREvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 3),
    _CcapAppIntfASREvtLog_Type()
)
ccapAppIntfASREvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASREvtLog.setStatus("current")
_CcapAppIntfASRReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfASRReadRequest_Object = MibTableColumn
ccapAppIntfASRReadRequest = _CcapAppIntfASRReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 4),
    _CcapAppIntfASRReadRequest_Type()
)
ccapAppIntfASRReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASRReadRequest.setStatus("current")
_CcapAppIntfASRReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfASRReadSuccess_Object = MibTableColumn
ccapAppIntfASRReadSuccess = _CcapAppIntfASRReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 5),
    _CcapAppIntfASRReadSuccess_Type()
)
ccapAppIntfASRReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASRReadSuccess.setStatus("current")
_CcapAppIntfASRReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfASRReadFailure_Object = MibTableColumn
ccapAppIntfASRReadFailure = _CcapAppIntfASRReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 6),
    _CcapAppIntfASRReadFailure_Type()
)
ccapAppIntfASRReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASRReadFailure.setStatus("current")
_CcapAppIntfASRLastResetTime_Type = TimeStamp
_CcapAppIntfASRLastResetTime_Object = MibTableColumn
ccapAppIntfASRLastResetTime = _CcapAppIntfASRLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 22, 1, 7),
    _CcapAppIntfASRLastResetTime_Type()
)
ccapAppIntfASRLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfASRLastResetTime.setStatus("current")
_CcapAppIntfTTSTable_Object = MibTable
ccapAppIntfTTSTable = _CcapAppIntfTTSTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23)
)
if mibBuilder.loadTexts:
    ccapAppIntfTTSTable.setStatus("current")
_CcapAppIntfTTSEntry_Object = MibTableRow
ccapAppIntfTTSEntry = _CcapAppIntfTTSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1)
)
ccapAppIntfTTSEntry.setIndexNames(
    (1, "CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSServer"),
)
if mibBuilder.loadTexts:
    ccapAppIntfTTSEntry.setStatus("current")
_CcapAppIntfTTSServer_Type = ServerNameString
_CcapAppIntfTTSServer_Object = MibTableColumn
ccapAppIntfTTSServer = _CcapAppIntfTTSServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 1),
    _CcapAppIntfTTSServer_Type()
)
ccapAppIntfTTSServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccapAppIntfTTSServer.setStatus("current")


class _CcapAppIntfTTSStats_Type(Integer32):
    """Custom type ccapAppIntfTTSStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfTTSStats_Type.__name__ = "Integer32"
_CcapAppIntfTTSStats_Object = MibTableColumn
ccapAppIntfTTSStats = _CcapAppIntfTTSStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 2),
    _CcapAppIntfTTSStats_Type()
)
ccapAppIntfTTSStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSStats.setStatus("current")


class _CcapAppIntfTTSEvtLog_Type(Integer32):
    """Custom type ccapAppIntfTTSEvtLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_CcapAppIntfTTSEvtLog_Type.__name__ = "Integer32"
_CcapAppIntfTTSEvtLog_Object = MibTableColumn
ccapAppIntfTTSEvtLog = _CcapAppIntfTTSEvtLog_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 3),
    _CcapAppIntfTTSEvtLog_Type()
)
ccapAppIntfTTSEvtLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSEvtLog.setStatus("current")
_CcapAppIntfTTSReadRequest_Type = ZeroBasedCounter32
_CcapAppIntfTTSReadRequest_Object = MibTableColumn
ccapAppIntfTTSReadRequest = _CcapAppIntfTTSReadRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 4),
    _CcapAppIntfTTSReadRequest_Type()
)
ccapAppIntfTTSReadRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSReadRequest.setStatus("current")
_CcapAppIntfTTSReadSuccess_Type = ZeroBasedCounter32
_CcapAppIntfTTSReadSuccess_Object = MibTableColumn
ccapAppIntfTTSReadSuccess = _CcapAppIntfTTSReadSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 5),
    _CcapAppIntfTTSReadSuccess_Type()
)
ccapAppIntfTTSReadSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSReadSuccess.setStatus("current")
_CcapAppIntfTTSReadFailure_Type = ZeroBasedCounter32
_CcapAppIntfTTSReadFailure_Object = MibTableColumn
ccapAppIntfTTSReadFailure = _CcapAppIntfTTSReadFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 6),
    _CcapAppIntfTTSReadFailure_Type()
)
ccapAppIntfTTSReadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSReadFailure.setStatus("current")
_CcapAppIntfTTSLastResetTime_Type = TimeStamp
_CcapAppIntfTTSLastResetTime_Object = MibTableColumn
ccapAppIntfTTSLastResetTime = _CcapAppIntfTTSLastResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 1, 6, 23, 1, 7),
    _CcapAppIntfTTSLastResetTime_Type()
)
ccapAppIntfTTSLastResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccapAppIntfTTSLastResetTime.setStatus("current")
_CiscoCallApplicationMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCallApplicationMIBConformance = _CiscoCallApplicationMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3)
)
_CiscoCallApplicationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCallApplicationMIBCompliances = _CiscoCallApplicationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 1)
)
_CiscoCallApplicationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCallApplicationMIBGroups = _CiscoCallApplicationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2)
)

# Managed Objects groups

ccapGeneralCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 1)
)
ccapGeneralCfgGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppLocation"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppLoadState"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppLoadFailReason"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppDescr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppCallType"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppRowStatus"))
)
if mibBuilder.loadTexts:
    ccapGeneralCfgGroup.setStatus("deprecated")

ccapGeneralCfgGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 2)
)
ccapGeneralCfgGroupRev1.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppLocation"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppLoadState"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppLoadFailReason"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppDescr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppCallType"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppRowStatus"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppActiveInstances"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppEventLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppPSTNInCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppPSTNOutCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIPInCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIPOutCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppPlaceCallInProgress"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppHandoffInProgress"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppPromptPlayActive"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppRecordingActive"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTTSActive"))
)
if mibBuilder.loadTexts:
    ccapGeneralCfgGroupRev1.setStatus("current")

ccapAppTypeHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 3)
)
ccapAppTypeHistoryGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisEvtLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisLastResetTime"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPSTNOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisIPOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPlaceCallAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPlaceCallSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPlaceCallFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisInHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisInHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisInHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisOutHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisOutHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisOutHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisOutHandofffailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentReadAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentReadFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentParseErrors"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentWriteAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDocumentWriteFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisDTMFLongPound"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASRAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASRAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASRNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASRNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASRMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisAAAAuthenticateFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisAAAAuthenticateSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisAAAAuthorizeFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisAAAAuthorizeSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASNLSubscriptionsSent"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASNLSubscriptionsSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASNLSubscriptionsFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisASNLNotifReceived"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPromptPlayAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPromptPlaySuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPromptPlayFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisPromptPlayDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisRecordingAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisRecordingSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisRecordingFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisRecordingDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisTTSAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisTTSSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppTypeHisTTSFailed"))
)
if mibBuilder.loadTexts:
    ccapAppTypeHistoryGroup.setStatus("current")

ccapAppInstanceHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 4)
)
ccapAppInstanceHistoryGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisSessionID"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisAppName"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPSTNOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisIPOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPlaceCallAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPlaceCallSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPlaceCallFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisInHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisInHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisInHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisOutHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisOutHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisOutHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisOutHandofffailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentReadAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentReadFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentParseErrors"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentWriteAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDocumentWriteFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisDTMFLongPound"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASRAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASRAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASRNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASRNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASRMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisAAAAuthenticateFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisAAAAuthenticateSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisAAAAuthorizeFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisAAAAuthorizeSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASNLSubscriptionsSent"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASNLSubscriptionsSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASNLSubscriptionsFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisASNLNotifReceived"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPromptPlayAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPromptPlaySuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPromptPlayFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisPromptPlayDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisRecordingAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisRecordingSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisRecordingFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisRecordingDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisTTSAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisTTSSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHisTTSFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppInstHistEvtLogging"))
)
if mibBuilder.loadTexts:
    ccapAppInstanceHistoryGroup.setStatus("current")

ccapAppGblActGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 5)
)
ccapAppGblActGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActCurrentInstances"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActPSTNInCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActPSTNOutCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActIPInCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActIPOutCallNowConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActPlaceCallInProgress"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActHandoffInProgress"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActPromptPlayActive"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActRecordingActive"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblActTTSActive"))
)
if mibBuilder.loadTexts:
    ccapAppGblActGroup.setStatus("current")

ccapAppGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 6)
)
ccapAppGblCfgGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppGblStatsLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblEventLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblEvtLogflush"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblStatsClear"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppGblCfgGroup.setStatus("current")

ccapAppGblHisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 7)
)
ccapAppGblHisGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisTotalInstances"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisLastReset"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPSTNOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallSetupInd"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPInCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallSetupReq"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallTotConn"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallHandedOut"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallHandOutRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallInHandoff"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallInHandoffRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallDiscNormal"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallDiscUsrErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisIPOutCallDiscSysErr"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPlaceCallAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPlaceCallSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPlaceCallFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisInHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisInHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisInHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisOutHandoffCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisOutHandoffCallbackRet"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisOutHandoffNoCallback"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisOutHandofffailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentReadAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentReadFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentParseErrors"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentWriteAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDocumentWriteFailures"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisDTMFLongPound"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASRAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASRAborted"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASRNoMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASRNoInput"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASRMatch"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisAAAAuthenticateFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisAAAAuthenticateSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisAAAAuthorizeFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisAAAAuthorizeSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASNLSubscriptionsSent"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASNLSubscriptionsSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASNLSubscriptionsFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisASNLNotifReceived"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPromptPlayAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPromptPlaySuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPromptPlayFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisPromptPlayDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisRecordingAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisRecordingSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisRecordingFailed"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisRecordingDuration"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisTTSAttempts"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisTTSSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppGblHisTTSFailed"))
)
if mibBuilder.loadTexts:
    ccapAppGblHisGroup.setStatus("current")

ccapAppIntfGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 8)
)
ccapAppIntfGblCfgGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfGblStatsLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfGblEventLogging"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfGblEvtLogFlush"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfGblStatsClear"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfGblLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfGblCfgGroup.setStatus("current")

ccapAppIntfHTTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 9)
)
ccapAppIntfHTTPGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPGetRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPGetSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPGetFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPPostRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPPostSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPPostFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPTxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPRxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPMinXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPMaxXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPAvgXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfHTTPLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfHTTPGroup.setStatus("current")

ccapAppIntfRTSPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 10)
)
ccapAppIntfRTSPGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPWriteRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPWriteFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPTxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPRxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPMinXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPMaxXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPAvgXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRTSPLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfRTSPGroup.setStatus("current")

ccapAppIntfTFTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 11)
)
ccapAppIntfTFTPGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPWriteRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPWriteFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPTxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPRxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPMinXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPMaxXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPAvgXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTFTPLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfTFTPGroup.setStatus("current")

ccapAppIntfSMTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 12)
)
ccapAppIntfSMTPGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPWriteRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPWriteSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPWriteFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPTxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPRxBytes"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPMinXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPMaxXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPAvgXferRate"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfSMTPLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfSMTPGroup.setStatus("current")

ccapAppIntfAAAMethodListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 13)
)
ccapAppIntfAAAMethodListGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfAAAMethodListLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfAAAMethodListGroup.setStatus("current")

ccapAppIntfASRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 14)
)
ccapAppIntfASRGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASREvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfASRLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfASRGroup.setStatus("current")

ccapAppIntfTTSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 15)
)
ccapAppIntfTTSGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSStats"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSEvtLog"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfTTSLastResetTime"))
)
if mibBuilder.loadTexts:
    ccapAppIntfTTSGroup.setStatus("current")

ccapAppIntfFlashGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 16)
)
ccapAppIntfFlashGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfFlashReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfFlashReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfFlashReadFailure"))
)
if mibBuilder.loadTexts:
    ccapAppIntfFlashGroup.setStatus("current")

ccapAppIntfRAMRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 2, 17)
)
ccapAppIntfRAMRecordGroup.setObjects(
      *(("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordReadRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordReadSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordiongReadFailure"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordRequest"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordSuccess"),
        ("CISCO-CALL-APPLICATION-MIB", "ccapAppIntfRAMRecordiongFailure"))
)
if mibBuilder.loadTexts:
    ccapAppIntfRAMRecordGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCallApplicationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCallApplicationMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCallApplicationMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 146, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCallApplicationMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-APPLICATION-MIB",
    **{"URLStringOrNull": URLStringOrNull,
       "ServerNameString": ServerNameString,
       "ciscoCallApplicationMIB": ciscoCallApplicationMIB,
       "ciscoCallApplicationMIBObjects": ciscoCallApplicationMIBObjects,
       "ccapConf": ccapConf,
       "ccapApplicationTable": ccapApplicationTable,
       "ccapApplicationEntry": ccapApplicationEntry,
       "ccapAppName": ccapAppName,
       "ccapAppLocation": ccapAppLocation,
       "ccapAppLoadState": ccapAppLoadState,
       "ccapAppLoadFailReason": ccapAppLoadFailReason,
       "ccapAppDescr": ccapAppDescr,
       "ccapAppCallType": ccapAppCallType,
       "ccapAppRowStatus": ccapAppRowStatus,
       "ccapAppActiveInstances": ccapAppActiveInstances,
       "ccapAppEventLogging": ccapAppEventLogging,
       "ccapAppPSTNInCallNowConn": ccapAppPSTNInCallNowConn,
       "ccapAppPSTNOutCallNowConn": ccapAppPSTNOutCallNowConn,
       "ccapAppIPInCallNowConn": ccapAppIPInCallNowConn,
       "ccapAppIPOutCallNowConn": ccapAppIPOutCallNowConn,
       "ccapAppPlaceCallInProgress": ccapAppPlaceCallInProgress,
       "ccapAppHandoffInProgress": ccapAppHandoffInProgress,
       "ccapAppPromptPlayActive": ccapAppPromptPlayActive,
       "ccapAppRecordingActive": ccapAppRecordingActive,
       "ccapAppTTSActive": ccapAppTTSActive,
       "ccapAppTypeHisStat": ccapAppTypeHisStat,
       "ccapAppTypeHistoryTable": ccapAppTypeHistoryTable,
       "ccapAppTypeHistoryEntry": ccapAppTypeHistoryEntry,
       "ccapAppTypeHisEvtLogging": ccapAppTypeHisEvtLogging,
       "ccapAppTypeHisLastResetTime": ccapAppTypeHisLastResetTime,
       "ccapAppTypeHisPSTNInCallSetupInd": ccapAppTypeHisPSTNInCallSetupInd,
       "ccapAppTypeHisPSTNInCallTotConn": ccapAppTypeHisPSTNInCallTotConn,
       "ccapAppTypeHisPSTNInCallHandedOut": ccapAppTypeHisPSTNInCallHandedOut,
       "ccapAppTypeHisPSTNInCallHandOutRet": ccapAppTypeHisPSTNInCallHandOutRet,
       "ccapAppTypeHisPSTNInCallInHandoff": ccapAppTypeHisPSTNInCallInHandoff,
       "ccapAppTypeHisPSTNInCallInHandoffRet": ccapAppTypeHisPSTNInCallInHandoffRet,
       "ccapAppTypeHisPSTNInCallDiscNormal": ccapAppTypeHisPSTNInCallDiscNormal,
       "ccapAppTypeHisPSTNInCallDiscUsrErr": ccapAppTypeHisPSTNInCallDiscUsrErr,
       "ccapAppTypeHisPSTNInCallDiscSysErr": ccapAppTypeHisPSTNInCallDiscSysErr,
       "ccapAppTypeHisPSTNOutCallSetupReq": ccapAppTypeHisPSTNOutCallSetupReq,
       "ccapAppTypeHisPSTNOutCallTotConn": ccapAppTypeHisPSTNOutCallTotConn,
       "ccapAppTypeHisPSTNOutCallHandedOut": ccapAppTypeHisPSTNOutCallHandedOut,
       "ccapAppTypeHisPSTNOutCallHandOutRet": ccapAppTypeHisPSTNOutCallHandOutRet,
       "ccapAppTypeHisPSTNOutCallInHandoff": ccapAppTypeHisPSTNOutCallInHandoff,
       "ccapAppTypeHisPSTNOutCallInHandoffRet": ccapAppTypeHisPSTNOutCallInHandoffRet,
       "ccapAppTypeHisPSTNOutCallDiscNormal": ccapAppTypeHisPSTNOutCallDiscNormal,
       "ccapAppTypeHisPSTNOutCallDiscUsrErr": ccapAppTypeHisPSTNOutCallDiscUsrErr,
       "ccapAppTypeHisPSTNOutCallDiscSysErr": ccapAppTypeHisPSTNOutCallDiscSysErr,
       "ccapAppTypeHisIPInCallSetupInd": ccapAppTypeHisIPInCallSetupInd,
       "ccapAppTypeHisIPInCallTotConn": ccapAppTypeHisIPInCallTotConn,
       "ccapAppTypeHisIPInCallHandedOut": ccapAppTypeHisIPInCallHandedOut,
       "ccapAppTypeHisIPInCallHandOutRet": ccapAppTypeHisIPInCallHandOutRet,
       "ccapAppTypeHisIPInCallInHandoff": ccapAppTypeHisIPInCallInHandoff,
       "ccapAppTypeHisIPInCallInHandoffRet": ccapAppTypeHisIPInCallInHandoffRet,
       "ccapAppTypeHisIPInCallDiscNormal": ccapAppTypeHisIPInCallDiscNormal,
       "ccapAppTypeHisIPInCallDiscUsrErr": ccapAppTypeHisIPInCallDiscUsrErr,
       "ccapAppTypeHisIPInCallDiscSysErr": ccapAppTypeHisIPInCallDiscSysErr,
       "ccapAppTypeHisIPOutCallSetupReq": ccapAppTypeHisIPOutCallSetupReq,
       "ccapAppTypeHisIPOutCallTotConn": ccapAppTypeHisIPOutCallTotConn,
       "ccapAppTypeHisIPOutCallHandedOut": ccapAppTypeHisIPOutCallHandedOut,
       "ccapAppTypeHisIPOutCallHandOutRet": ccapAppTypeHisIPOutCallHandOutRet,
       "ccapAppTypeHisIPOutCallInHandoff": ccapAppTypeHisIPOutCallInHandoff,
       "ccapAppTypeHisIPOutCallInHandoffRet": ccapAppTypeHisIPOutCallInHandoffRet,
       "ccapAppTypeHisIPOutCallDiscNormal": ccapAppTypeHisIPOutCallDiscNormal,
       "ccapAppTypeHisIPOutCallDiscUsrErr": ccapAppTypeHisIPOutCallDiscUsrErr,
       "ccapAppTypeHisIPOutCallDiscSysErr": ccapAppTypeHisIPOutCallDiscSysErr,
       "ccapAppTypeHisPlaceCallAttempts": ccapAppTypeHisPlaceCallAttempts,
       "ccapAppTypeHisPlaceCallSuccess": ccapAppTypeHisPlaceCallSuccess,
       "ccapAppTypeHisPlaceCallFailure": ccapAppTypeHisPlaceCallFailure,
       "ccapAppTypeHisInHandoffCallback": ccapAppTypeHisInHandoffCallback,
       "ccapAppTypeHisInHandoffCallbackRet": ccapAppTypeHisInHandoffCallbackRet,
       "ccapAppTypeHisInHandoffNoCallback": ccapAppTypeHisInHandoffNoCallback,
       "ccapAppTypeHisOutHandoffCallback": ccapAppTypeHisOutHandoffCallback,
       "ccapAppTypeHisOutHandoffCallbackRet": ccapAppTypeHisOutHandoffCallbackRet,
       "ccapAppTypeHisOutHandoffNoCallback": ccapAppTypeHisOutHandoffNoCallback,
       "ccapAppTypeHisOutHandofffailures": ccapAppTypeHisOutHandofffailures,
       "ccapAppTypeHisDocumentReadAttempts": ccapAppTypeHisDocumentReadAttempts,
       "ccapAppTypeHisDocumentReadSuccess": ccapAppTypeHisDocumentReadSuccess,
       "ccapAppTypeHisDocumentReadFailures": ccapAppTypeHisDocumentReadFailures,
       "ccapAppTypeHisDocumentParseErrors": ccapAppTypeHisDocumentParseErrors,
       "ccapAppTypeHisDocumentWriteAttempts": ccapAppTypeHisDocumentWriteAttempts,
       "ccapAppTypeHisDocumentWriteSuccess": ccapAppTypeHisDocumentWriteSuccess,
       "ccapAppTypeHisDocumentWriteFailures": ccapAppTypeHisDocumentWriteFailures,
       "ccapAppTypeHisDTMFAttempts": ccapAppTypeHisDTMFAttempts,
       "ccapAppTypeHisDTMFAborted": ccapAppTypeHisDTMFAborted,
       "ccapAppTypeHisDTMFNoMatch": ccapAppTypeHisDTMFNoMatch,
       "ccapAppTypeHisDTMFNoInput": ccapAppTypeHisDTMFNoInput,
       "ccapAppTypeHisDTMFMatch": ccapAppTypeHisDTMFMatch,
       "ccapAppTypeHisDTMFLongPound": ccapAppTypeHisDTMFLongPound,
       "ccapAppTypeHisASRAttempts": ccapAppTypeHisASRAttempts,
       "ccapAppTypeHisASRAborted": ccapAppTypeHisASRAborted,
       "ccapAppTypeHisASRNoMatch": ccapAppTypeHisASRNoMatch,
       "ccapAppTypeHisASRNoInput": ccapAppTypeHisASRNoInput,
       "ccapAppTypeHisASRMatch": ccapAppTypeHisASRMatch,
       "ccapAppTypeHisAAAAuthenticateFailure": ccapAppTypeHisAAAAuthenticateFailure,
       "ccapAppTypeHisAAAAuthenticateSuccess": ccapAppTypeHisAAAAuthenticateSuccess,
       "ccapAppTypeHisAAAAuthorizeFailure": ccapAppTypeHisAAAAuthorizeFailure,
       "ccapAppTypeHisAAAAuthorizeSuccess": ccapAppTypeHisAAAAuthorizeSuccess,
       "ccapAppTypeHisASNLSubscriptionsSent": ccapAppTypeHisASNLSubscriptionsSent,
       "ccapAppTypeHisASNLSubscriptionsSuccess": ccapAppTypeHisASNLSubscriptionsSuccess,
       "ccapAppTypeHisASNLSubscriptionsFailed": ccapAppTypeHisASNLSubscriptionsFailed,
       "ccapAppTypeHisASNLNotifReceived": ccapAppTypeHisASNLNotifReceived,
       "ccapAppTypeHisPromptPlayAttempts": ccapAppTypeHisPromptPlayAttempts,
       "ccapAppTypeHisPromptPlaySuccess": ccapAppTypeHisPromptPlaySuccess,
       "ccapAppTypeHisPromptPlayFailed": ccapAppTypeHisPromptPlayFailed,
       "ccapAppTypeHisPromptPlayDuration": ccapAppTypeHisPromptPlayDuration,
       "ccapAppTypeHisRecordingAttempts": ccapAppTypeHisRecordingAttempts,
       "ccapAppTypeHisRecordingSuccess": ccapAppTypeHisRecordingSuccess,
       "ccapAppTypeHisRecordingFailed": ccapAppTypeHisRecordingFailed,
       "ccapAppTypeHisRecordingDuration": ccapAppTypeHisRecordingDuration,
       "ccapAppTypeHisTTSAttempts": ccapAppTypeHisTTSAttempts,
       "ccapAppTypeHisTTSSuccess": ccapAppTypeHisTTSSuccess,
       "ccapAppTypeHisTTSFailed": ccapAppTypeHisTTSFailed,
       "ccapAppInstHisStat": ccapAppInstHisStat,
       "ccapAppInstanceHistoryTable": ccapAppInstanceHistoryTable,
       "ccapAppInstanceHistoryEntry": ccapAppInstanceHistoryEntry,
       "ccapAppInstHisIndex": ccapAppInstHisIndex,
       "ccapAppInstHisSessionID": ccapAppInstHisSessionID,
       "ccapAppInstHisAppName": ccapAppInstHisAppName,
       "ccapAppInstHisPSTNInCallSetupInd": ccapAppInstHisPSTNInCallSetupInd,
       "ccapAppInstHisPSTNInCallTotConn": ccapAppInstHisPSTNInCallTotConn,
       "ccapAppInstHisPSTNInCallHandedOut": ccapAppInstHisPSTNInCallHandedOut,
       "ccapAppInstHisPSTNInCallHandOutRet": ccapAppInstHisPSTNInCallHandOutRet,
       "ccapAppInstHisPSTNInCallInHandoff": ccapAppInstHisPSTNInCallInHandoff,
       "ccapAppInstHisPSTNInCallInHandoffRet": ccapAppInstHisPSTNInCallInHandoffRet,
       "ccapAppInstHisPSTNInCallDiscNormal": ccapAppInstHisPSTNInCallDiscNormal,
       "ccapAppInstHisPSTNInCallDiscUsrErr": ccapAppInstHisPSTNInCallDiscUsrErr,
       "ccapAppInstHisPSTNInCallDiscSysErr": ccapAppInstHisPSTNInCallDiscSysErr,
       "ccapAppInstHisPSTNOutCallSetupReq": ccapAppInstHisPSTNOutCallSetupReq,
       "ccapAppInstHisPSTNOutCallTotConn": ccapAppInstHisPSTNOutCallTotConn,
       "ccapAppInstHisPSTNOutCallHandedOut": ccapAppInstHisPSTNOutCallHandedOut,
       "ccapAppInstHisPSTNOutCallHandOutRet": ccapAppInstHisPSTNOutCallHandOutRet,
       "ccapAppInstHisPSTNOutCallInHandoff": ccapAppInstHisPSTNOutCallInHandoff,
       "ccapAppInstHisPSTNOutCallInHandoffRet": ccapAppInstHisPSTNOutCallInHandoffRet,
       "ccapAppInstHisPSTNOutCallDiscNormal": ccapAppInstHisPSTNOutCallDiscNormal,
       "ccapAppInstHisPSTNOutCallDiscUsrErr": ccapAppInstHisPSTNOutCallDiscUsrErr,
       "ccapAppInstHisPSTNOutCallDiscSysErr": ccapAppInstHisPSTNOutCallDiscSysErr,
       "ccapAppInstHisIPInCallSetupInd": ccapAppInstHisIPInCallSetupInd,
       "ccapAppInstHisIPInCallTotConn": ccapAppInstHisIPInCallTotConn,
       "ccapAppInstHisIPInCallHandedOut": ccapAppInstHisIPInCallHandedOut,
       "ccapAppInstHisIPInCallHandOutRet": ccapAppInstHisIPInCallHandOutRet,
       "ccapAppInstHisIPInCallInHandoff": ccapAppInstHisIPInCallInHandoff,
       "ccapAppInstHisIPInCallInHandoffRet": ccapAppInstHisIPInCallInHandoffRet,
       "ccapAppInstHisIPInCallDiscNormal": ccapAppInstHisIPInCallDiscNormal,
       "ccapAppInstHisIPInCallDiscUsrErr": ccapAppInstHisIPInCallDiscUsrErr,
       "ccapAppInstHisIPInCallDiscSysErr": ccapAppInstHisIPInCallDiscSysErr,
       "ccapAppInstHisIPOutCallSetupReq": ccapAppInstHisIPOutCallSetupReq,
       "ccapAppInstHisIPOutCallTotConn": ccapAppInstHisIPOutCallTotConn,
       "ccapAppInstHisIPOutCallHandedOut": ccapAppInstHisIPOutCallHandedOut,
       "ccapAppInstHisIPOutCallHandOutRet": ccapAppInstHisIPOutCallHandOutRet,
       "ccapAppInstHisIPOutCallInHandoff": ccapAppInstHisIPOutCallInHandoff,
       "ccapAppInstHisIPOutCallInHandoffRet": ccapAppInstHisIPOutCallInHandoffRet,
       "ccapAppInstHisIPOutCallDiscNormal": ccapAppInstHisIPOutCallDiscNormal,
       "ccapAppInstHisIPOutCallDiscUsrErr": ccapAppInstHisIPOutCallDiscUsrErr,
       "ccapAppInstHisIPOutCallDiscSysErr": ccapAppInstHisIPOutCallDiscSysErr,
       "ccapAppInstHisPlaceCallAttempts": ccapAppInstHisPlaceCallAttempts,
       "ccapAppInstHisPlaceCallSuccess": ccapAppInstHisPlaceCallSuccess,
       "ccapAppInstHisPlaceCallFailure": ccapAppInstHisPlaceCallFailure,
       "ccapAppInstHisInHandoffCallback": ccapAppInstHisInHandoffCallback,
       "ccapAppInstHisInHandoffCallbackRet": ccapAppInstHisInHandoffCallbackRet,
       "ccapAppInstHisInHandoffNoCallback": ccapAppInstHisInHandoffNoCallback,
       "ccapAppInstHisOutHandoffCallback": ccapAppInstHisOutHandoffCallback,
       "ccapAppInstHisOutHandoffCallbackRet": ccapAppInstHisOutHandoffCallbackRet,
       "ccapAppInstHisOutHandoffNoCallback": ccapAppInstHisOutHandoffNoCallback,
       "ccapAppInstHisOutHandofffailures": ccapAppInstHisOutHandofffailures,
       "ccapAppInstHisDocumentReadAttempts": ccapAppInstHisDocumentReadAttempts,
       "ccapAppInstHisDocumentReadSuccess": ccapAppInstHisDocumentReadSuccess,
       "ccapAppInstHisDocumentReadFailures": ccapAppInstHisDocumentReadFailures,
       "ccapAppInstHisDocumentParseErrors": ccapAppInstHisDocumentParseErrors,
       "ccapAppInstHisDocumentWriteAttempts": ccapAppInstHisDocumentWriteAttempts,
       "ccapAppInstHisDocumentWriteSuccess": ccapAppInstHisDocumentWriteSuccess,
       "ccapAppInstHisDocumentWriteFailures": ccapAppInstHisDocumentWriteFailures,
       "ccapAppInstHisDTMFAttempts": ccapAppInstHisDTMFAttempts,
       "ccapAppInstHisDTMFAborted": ccapAppInstHisDTMFAborted,
       "ccapAppInstHisDTMFNoMatch": ccapAppInstHisDTMFNoMatch,
       "ccapAppInstHisDTMFNoInput": ccapAppInstHisDTMFNoInput,
       "ccapAppInstHisDTMFMatch": ccapAppInstHisDTMFMatch,
       "ccapAppInstHisDTMFLongPound": ccapAppInstHisDTMFLongPound,
       "ccapAppInstHisASRAttempts": ccapAppInstHisASRAttempts,
       "ccapAppInstHisASRAborted": ccapAppInstHisASRAborted,
       "ccapAppInstHisASRNoMatch": ccapAppInstHisASRNoMatch,
       "ccapAppInstHisASRNoInput": ccapAppInstHisASRNoInput,
       "ccapAppInstHisASRMatch": ccapAppInstHisASRMatch,
       "ccapAppInstHisAAAAuthenticateFailure": ccapAppInstHisAAAAuthenticateFailure,
       "ccapAppInstHisAAAAuthenticateSuccess": ccapAppInstHisAAAAuthenticateSuccess,
       "ccapAppInstHisAAAAuthorizeFailure": ccapAppInstHisAAAAuthorizeFailure,
       "ccapAppInstHisAAAAuthorizeSuccess": ccapAppInstHisAAAAuthorizeSuccess,
       "ccapAppInstHisASNLSubscriptionsSent": ccapAppInstHisASNLSubscriptionsSent,
       "ccapAppInstHisASNLSubscriptionsSuccess": ccapAppInstHisASNLSubscriptionsSuccess,
       "ccapAppInstHisASNLSubscriptionsFailed": ccapAppInstHisASNLSubscriptionsFailed,
       "ccapAppInstHisASNLNotifReceived": ccapAppInstHisASNLNotifReceived,
       "ccapAppInstHisPromptPlayAttempts": ccapAppInstHisPromptPlayAttempts,
       "ccapAppInstHisPromptPlaySuccess": ccapAppInstHisPromptPlaySuccess,
       "ccapAppInstHisPromptPlayFailed": ccapAppInstHisPromptPlayFailed,
       "ccapAppInstHisPromptPlayDuration": ccapAppInstHisPromptPlayDuration,
       "ccapAppInstHisRecordingAttempts": ccapAppInstHisRecordingAttempts,
       "ccapAppInstHisRecordingSuccess": ccapAppInstHisRecordingSuccess,
       "ccapAppInstHisRecordingFailed": ccapAppInstHisRecordingFailed,
       "ccapAppInstHisRecordingDuration": ccapAppInstHisRecordingDuration,
       "ccapAppInstHisTTSAttempts": ccapAppInstHisTTSAttempts,
       "ccapAppInstHisTTSSuccess": ccapAppInstHisTTSSuccess,
       "ccapAppInstHisTTSFailed": ccapAppInstHisTTSFailed,
       "ccapAppInstHistEvtLogging": ccapAppInstHistEvtLogging,
       "ccapAppGblActStat": ccapAppGblActStat,
       "ccapAppGblActCurrentInstances": ccapAppGblActCurrentInstances,
       "ccapAppGblActPSTNInCallNowConn": ccapAppGblActPSTNInCallNowConn,
       "ccapAppGblActPSTNOutCallNowConn": ccapAppGblActPSTNOutCallNowConn,
       "ccapAppGblActIPInCallNowConn": ccapAppGblActIPInCallNowConn,
       "ccapAppGblActIPOutCallNowConn": ccapAppGblActIPOutCallNowConn,
       "ccapAppGblActPlaceCallInProgress": ccapAppGblActPlaceCallInProgress,
       "ccapAppGblActHandoffInProgress": ccapAppGblActHandoffInProgress,
       "ccapAppGblActPromptPlayActive": ccapAppGblActPromptPlayActive,
       "ccapAppGblActRecordingActive": ccapAppGblActRecordingActive,
       "ccapAppGblActTTSActive": ccapAppGblActTTSActive,
       "ccapAppGblStatsLogging": ccapAppGblStatsLogging,
       "ccapAppGblEventLogging": ccapAppGblEventLogging,
       "ccapAppGblEvtLogflush": ccapAppGblEvtLogflush,
       "ccapAppGblStatsClear": ccapAppGblStatsClear,
       "ccapAppGblLastResetTime": ccapAppGblLastResetTime,
       "ccapAppGblHisStat": ccapAppGblHisStat,
       "ccapAppGblHisTotalInstances": ccapAppGblHisTotalInstances,
       "ccapAppGblHisLastReset": ccapAppGblHisLastReset,
       "ccapAppGblHisPSTNInCallSetupInd": ccapAppGblHisPSTNInCallSetupInd,
       "ccapAppGblHisPSTNInCallTotConn": ccapAppGblHisPSTNInCallTotConn,
       "ccapAppGblHisPSTNInCallHandedOut": ccapAppGblHisPSTNInCallHandedOut,
       "ccapAppGblHisPSTNInCallHandOutRet": ccapAppGblHisPSTNInCallHandOutRet,
       "ccapAppGblHisPSTNInCallInHandoff": ccapAppGblHisPSTNInCallInHandoff,
       "ccapAppGblHisPSTNInCallInHandoffRet": ccapAppGblHisPSTNInCallInHandoffRet,
       "ccapAppGblHisPSTNInCallDiscNormal": ccapAppGblHisPSTNInCallDiscNormal,
       "ccapAppGblHisPSTNInCallDiscUsrErr": ccapAppGblHisPSTNInCallDiscUsrErr,
       "ccapAppGblHisPSTNInCallDiscSysErr": ccapAppGblHisPSTNInCallDiscSysErr,
       "ccapAppGblHisPSTNOutCallSetupReq": ccapAppGblHisPSTNOutCallSetupReq,
       "ccapAppGblHisPSTNOutCallTotConn": ccapAppGblHisPSTNOutCallTotConn,
       "ccapAppGblHisPSTNOutCallHandedOut": ccapAppGblHisPSTNOutCallHandedOut,
       "ccapAppGblHisPSTNOutCallHandOutRet": ccapAppGblHisPSTNOutCallHandOutRet,
       "ccapAppGblHisPSTNOutCallInHandoff": ccapAppGblHisPSTNOutCallInHandoff,
       "ccapAppGblHisPSTNOutCallInHandoffRet": ccapAppGblHisPSTNOutCallInHandoffRet,
       "ccapAppGblHisPSTNOutCallDiscNormal": ccapAppGblHisPSTNOutCallDiscNormal,
       "ccapAppGblHisPSTNOutCallDiscUsrErr": ccapAppGblHisPSTNOutCallDiscUsrErr,
       "ccapAppGblHisPSTNOutCallDiscSysErr": ccapAppGblHisPSTNOutCallDiscSysErr,
       "ccapAppGblHisIPInCallSetupInd": ccapAppGblHisIPInCallSetupInd,
       "ccapAppGblHisIPInCallTotConn": ccapAppGblHisIPInCallTotConn,
       "ccapAppGblHisIPInCallHandedOut": ccapAppGblHisIPInCallHandedOut,
       "ccapAppGblHisIPInCallHandOutRet": ccapAppGblHisIPInCallHandOutRet,
       "ccapAppGblHisIPInCallInHandoff": ccapAppGblHisIPInCallInHandoff,
       "ccapAppGblHisIPInCallInHandoffRet": ccapAppGblHisIPInCallInHandoffRet,
       "ccapAppGblHisIPInCallDiscNormal": ccapAppGblHisIPInCallDiscNormal,
       "ccapAppGblHisIPInCallDiscUsrErr": ccapAppGblHisIPInCallDiscUsrErr,
       "ccapAppGblHisIPInCallDiscSysErr": ccapAppGblHisIPInCallDiscSysErr,
       "ccapAppGblHisIPOutCallSetupReq": ccapAppGblHisIPOutCallSetupReq,
       "ccapAppGblHisIPOutCallTotConn": ccapAppGblHisIPOutCallTotConn,
       "ccapAppGblHisIPOutCallHandedOut": ccapAppGblHisIPOutCallHandedOut,
       "ccapAppGblHisIPOutCallHandOutRet": ccapAppGblHisIPOutCallHandOutRet,
       "ccapAppGblHisIPOutCallInHandoff": ccapAppGblHisIPOutCallInHandoff,
       "ccapAppGblHisIPOutCallInHandoffRet": ccapAppGblHisIPOutCallInHandoffRet,
       "ccapAppGblHisIPOutCallDiscNormal": ccapAppGblHisIPOutCallDiscNormal,
       "ccapAppGblHisIPOutCallDiscUsrErr": ccapAppGblHisIPOutCallDiscUsrErr,
       "ccapAppGblHisIPOutCallDiscSysErr": ccapAppGblHisIPOutCallDiscSysErr,
       "ccapAppGblHisPlaceCallAttempts": ccapAppGblHisPlaceCallAttempts,
       "ccapAppGblHisPlaceCallSuccess": ccapAppGblHisPlaceCallSuccess,
       "ccapAppGblHisPlaceCallFailure": ccapAppGblHisPlaceCallFailure,
       "ccapAppGblHisInHandoffCallback": ccapAppGblHisInHandoffCallback,
       "ccapAppGblHisInHandoffCallbackRet": ccapAppGblHisInHandoffCallbackRet,
       "ccapAppGblHisInHandoffNoCallback": ccapAppGblHisInHandoffNoCallback,
       "ccapAppGblHisOutHandoffCallback": ccapAppGblHisOutHandoffCallback,
       "ccapAppGblHisOutHandoffCallbackRet": ccapAppGblHisOutHandoffCallbackRet,
       "ccapAppGblHisOutHandoffNoCallback": ccapAppGblHisOutHandoffNoCallback,
       "ccapAppGblHisOutHandofffailures": ccapAppGblHisOutHandofffailures,
       "ccapAppGblHisDocumentReadAttempts": ccapAppGblHisDocumentReadAttempts,
       "ccapAppGblHisDocumentReadSuccess": ccapAppGblHisDocumentReadSuccess,
       "ccapAppGblHisDocumentReadFailures": ccapAppGblHisDocumentReadFailures,
       "ccapAppGblHisDocumentParseErrors": ccapAppGblHisDocumentParseErrors,
       "ccapAppGblHisDocumentWriteAttempts": ccapAppGblHisDocumentWriteAttempts,
       "ccapAppGblHisDocumentWriteSuccess": ccapAppGblHisDocumentWriteSuccess,
       "ccapAppGblHisDocumentWriteFailures": ccapAppGblHisDocumentWriteFailures,
       "ccapAppGblHisDTMFAttempts": ccapAppGblHisDTMFAttempts,
       "ccapAppGblHisDTMFAborted": ccapAppGblHisDTMFAborted,
       "ccapAppGblHisDTMFNoMatch": ccapAppGblHisDTMFNoMatch,
       "ccapAppGblHisDTMFNoInput": ccapAppGblHisDTMFNoInput,
       "ccapAppGblHisDTMFMatch": ccapAppGblHisDTMFMatch,
       "ccapAppGblHisDTMFLongPound": ccapAppGblHisDTMFLongPound,
       "ccapAppGblHisASRAttempts": ccapAppGblHisASRAttempts,
       "ccapAppGblHisASRAborted": ccapAppGblHisASRAborted,
       "ccapAppGblHisASRNoMatch": ccapAppGblHisASRNoMatch,
       "ccapAppGblHisASRNoInput": ccapAppGblHisASRNoInput,
       "ccapAppGblHisASRMatch": ccapAppGblHisASRMatch,
       "ccapAppGblHisAAAAuthenticateFailure": ccapAppGblHisAAAAuthenticateFailure,
       "ccapAppGblHisAAAAuthenticateSuccess": ccapAppGblHisAAAAuthenticateSuccess,
       "ccapAppGblHisAAAAuthorizeFailure": ccapAppGblHisAAAAuthorizeFailure,
       "ccapAppGblHisAAAAuthorizeSuccess": ccapAppGblHisAAAAuthorizeSuccess,
       "ccapAppGblHisASNLSubscriptionsSent": ccapAppGblHisASNLSubscriptionsSent,
       "ccapAppGblHisASNLSubscriptionsSuccess": ccapAppGblHisASNLSubscriptionsSuccess,
       "ccapAppGblHisASNLSubscriptionsFailed": ccapAppGblHisASNLSubscriptionsFailed,
       "ccapAppGblHisASNLNotifReceived": ccapAppGblHisASNLNotifReceived,
       "ccapAppGblHisPromptPlayAttempts": ccapAppGblHisPromptPlayAttempts,
       "ccapAppGblHisPromptPlaySuccess": ccapAppGblHisPromptPlaySuccess,
       "ccapAppGblHisPromptPlayFailed": ccapAppGblHisPromptPlayFailed,
       "ccapAppGblHisPromptPlayDuration": ccapAppGblHisPromptPlayDuration,
       "ccapAppGblHisRecordingAttempts": ccapAppGblHisRecordingAttempts,
       "ccapAppGblHisRecordingSuccess": ccapAppGblHisRecordingSuccess,
       "ccapAppGblHisRecordingFailed": ccapAppGblHisRecordingFailed,
       "ccapAppGblHisRecordingDuration": ccapAppGblHisRecordingDuration,
       "ccapAppGblHisTTSAttempts": ccapAppGblHisTTSAttempts,
       "ccapAppGblHisTTSSuccess": ccapAppGblHisTTSSuccess,
       "ccapAppGblHisTTSFailed": ccapAppGblHisTTSFailed,
       "ccapAppIntf": ccapAppIntf,
       "ccapAppIntfGblStatsLogging": ccapAppIntfGblStatsLogging,
       "ccapAppIntfGblEventLogging": ccapAppIntfGblEventLogging,
       "ccapAppIntfGblEvtLogFlush": ccapAppIntfGblEvtLogFlush,
       "ccapAppIntfGblStatsClear": ccapAppIntfGblStatsClear,
       "ccapAppIntfGblLastResetTime": ccapAppIntfGblLastResetTime,
       "ccapAppIntfHTTPTable": ccapAppIntfHTTPTable,
       "ccapAppIntfHTTPEntry": ccapAppIntfHTTPEntry,
       "ccapAppIntfHTTPServer": ccapAppIntfHTTPServer,
       "ccapAppIntfHTTPStats": ccapAppIntfHTTPStats,
       "ccapAppIntfHTTPEvtLog": ccapAppIntfHTTPEvtLog,
       "ccapAppIntfHTTPGetRequest": ccapAppIntfHTTPGetRequest,
       "ccapAppIntfHTTPGetSuccess": ccapAppIntfHTTPGetSuccess,
       "ccapAppIntfHTTPGetFailure": ccapAppIntfHTTPGetFailure,
       "ccapAppIntfHTTPPostRequest": ccapAppIntfHTTPPostRequest,
       "ccapAppIntfHTTPPostSuccess": ccapAppIntfHTTPPostSuccess,
       "ccapAppIntfHTTPPostFailure": ccapAppIntfHTTPPostFailure,
       "ccapAppIntfHTTPTxBytes": ccapAppIntfHTTPTxBytes,
       "ccapAppIntfHTTPRxBytes": ccapAppIntfHTTPRxBytes,
       "ccapAppIntfHTTPMinXferRate": ccapAppIntfHTTPMinXferRate,
       "ccapAppIntfHTTPMaxXferRate": ccapAppIntfHTTPMaxXferRate,
       "ccapAppIntfHTTPAvgXferRate": ccapAppIntfHTTPAvgXferRate,
       "ccapAppIntfHTTPLastResetTime": ccapAppIntfHTTPLastResetTime,
       "ccapAppIntfRTSPTable": ccapAppIntfRTSPTable,
       "ccapAppIntfRTSPEntry": ccapAppIntfRTSPEntry,
       "ccapAppIntfRTSPServer": ccapAppIntfRTSPServer,
       "ccapAppIntfRTSPStats": ccapAppIntfRTSPStats,
       "ccapAppIntfRTSPEvtLog": ccapAppIntfRTSPEvtLog,
       "ccapAppIntfRTSPReadRequest": ccapAppIntfRTSPReadRequest,
       "ccapAppIntfRTSPReadSuccess": ccapAppIntfRTSPReadSuccess,
       "ccapAppIntfRTSPReadFailure": ccapAppIntfRTSPReadFailure,
       "ccapAppIntfRTSPWriteRequest": ccapAppIntfRTSPWriteRequest,
       "ccapAppIntfRTSPWriteSuccess": ccapAppIntfRTSPWriteSuccess,
       "ccapAppIntfRTSPWriteFailure": ccapAppIntfRTSPWriteFailure,
       "ccapAppIntfRTSPTxBytes": ccapAppIntfRTSPTxBytes,
       "ccapAppIntfRTSPRxBytes": ccapAppIntfRTSPRxBytes,
       "ccapAppIntfRTSPMinXferRate": ccapAppIntfRTSPMinXferRate,
       "ccapAppIntfRTSPMaxXferRate": ccapAppIntfRTSPMaxXferRate,
       "ccapAppIntfRTSPAvgXferRate": ccapAppIntfRTSPAvgXferRate,
       "ccapAppIntfRTSPLastResetTime": ccapAppIntfRTSPLastResetTime,
       "ccapAppIntfTFTPTable": ccapAppIntfTFTPTable,
       "ccapAppIntfTFTPEntry": ccapAppIntfTFTPEntry,
       "ccapAppIntfTFTPServer": ccapAppIntfTFTPServer,
       "ccapAppIntfTFTPStats": ccapAppIntfTFTPStats,
       "ccapAppIntfTFTPEvtLog": ccapAppIntfTFTPEvtLog,
       "ccapAppIntfTFTPReadRequest": ccapAppIntfTFTPReadRequest,
       "ccapAppIntfTFTPReadSuccess": ccapAppIntfTFTPReadSuccess,
       "ccapAppIntfTFTPReadFailure": ccapAppIntfTFTPReadFailure,
       "ccapAppIntfTFTPWriteRequest": ccapAppIntfTFTPWriteRequest,
       "ccapAppIntfTFTPWriteSuccess": ccapAppIntfTFTPWriteSuccess,
       "ccapAppIntfTFTPWriteFailure": ccapAppIntfTFTPWriteFailure,
       "ccapAppIntfTFTPTxBytes": ccapAppIntfTFTPTxBytes,
       "ccapAppIntfTFTPRxBytes": ccapAppIntfTFTPRxBytes,
       "ccapAppIntfTFTPMinXferRate": ccapAppIntfTFTPMinXferRate,
       "ccapAppIntfTFTPMaxXferRate": ccapAppIntfTFTPMaxXferRate,
       "ccapAppIntfTFTPAvgXferRate": ccapAppIntfTFTPAvgXferRate,
       "ccapAppIntfTFTPLastResetTime": ccapAppIntfTFTPLastResetTime,
       "ccapAppIntfFlashReadRequest": ccapAppIntfFlashReadRequest,
       "ccapAppIntfFlashReadSuccess": ccapAppIntfFlashReadSuccess,
       "ccapAppIntfFlashReadFailure": ccapAppIntfFlashReadFailure,
       "ccapAppIntfRAMRecordReadRequest": ccapAppIntfRAMRecordReadRequest,
       "ccapAppIntfRAMRecordReadSuccess": ccapAppIntfRAMRecordReadSuccess,
       "ccapAppIntfRAMRecordiongReadFailure": ccapAppIntfRAMRecordiongReadFailure,
       "ccapAppIntfRAMRecordRequest": ccapAppIntfRAMRecordRequest,
       "ccapAppIntfRAMRecordSuccess": ccapAppIntfRAMRecordSuccess,
       "ccapAppIntfRAMRecordiongFailure": ccapAppIntfRAMRecordiongFailure,
       "ccapAppIntfSMTPTable": ccapAppIntfSMTPTable,
       "ccapAppIntfSMTPEntry": ccapAppIntfSMTPEntry,
       "ccapAppIntfSMTPServer": ccapAppIntfSMTPServer,
       "ccapAppIntfSMTPStats": ccapAppIntfSMTPStats,
       "ccapAppIntfSMTPEvtLog": ccapAppIntfSMTPEvtLog,
       "ccapAppIntfSMTPReadRequest": ccapAppIntfSMTPReadRequest,
       "ccapAppIntfSMTPReadSuccess": ccapAppIntfSMTPReadSuccess,
       "ccapAppIntfSMTPReadFailure": ccapAppIntfSMTPReadFailure,
       "ccapAppIntfSMTPWriteRequest": ccapAppIntfSMTPWriteRequest,
       "ccapAppIntfSMTPWriteSuccess": ccapAppIntfSMTPWriteSuccess,
       "ccapAppIntfSMTPWriteFailure": ccapAppIntfSMTPWriteFailure,
       "ccapAppIntfSMTPTxBytes": ccapAppIntfSMTPTxBytes,
       "ccapAppIntfSMTPRxBytes": ccapAppIntfSMTPRxBytes,
       "ccapAppIntfSMTPMinXferRate": ccapAppIntfSMTPMinXferRate,
       "ccapAppIntfSMTPMaxXferRate": ccapAppIntfSMTPMaxXferRate,
       "ccapAppIntfSMTPAvgXferRate": ccapAppIntfSMTPAvgXferRate,
       "ccapAppIntfSMTPLastResetTime": ccapAppIntfSMTPLastResetTime,
       "ccapAppIntfAAAMethodListTable": ccapAppIntfAAAMethodListTable,
       "ccapAppIntfAAAMethodListEntry": ccapAppIntfAAAMethodListEntry,
       "ccapAppIntfAAAMethodListServer": ccapAppIntfAAAMethodListServer,
       "ccapAppIntfAAAMethodListStats": ccapAppIntfAAAMethodListStats,
       "ccapAppIntfAAAMethodListEvtLog": ccapAppIntfAAAMethodListEvtLog,
       "ccapAppIntfAAAMethodListReadRequest": ccapAppIntfAAAMethodListReadRequest,
       "ccapAppIntfAAAMethodListReadSuccess": ccapAppIntfAAAMethodListReadSuccess,
       "ccapAppIntfAAAMethodListReadFailure": ccapAppIntfAAAMethodListReadFailure,
       "ccapAppIntfAAAMethodListLastResetTime": ccapAppIntfAAAMethodListLastResetTime,
       "ccapAppIntfASRTable": ccapAppIntfASRTable,
       "ccapAppIntfASREntry": ccapAppIntfASREntry,
       "ccapAppIntfASRServer": ccapAppIntfASRServer,
       "ccapAppIntfASRStats": ccapAppIntfASRStats,
       "ccapAppIntfASREvtLog": ccapAppIntfASREvtLog,
       "ccapAppIntfASRReadRequest": ccapAppIntfASRReadRequest,
       "ccapAppIntfASRReadSuccess": ccapAppIntfASRReadSuccess,
       "ccapAppIntfASRReadFailure": ccapAppIntfASRReadFailure,
       "ccapAppIntfASRLastResetTime": ccapAppIntfASRLastResetTime,
       "ccapAppIntfTTSTable": ccapAppIntfTTSTable,
       "ccapAppIntfTTSEntry": ccapAppIntfTTSEntry,
       "ccapAppIntfTTSServer": ccapAppIntfTTSServer,
       "ccapAppIntfTTSStats": ccapAppIntfTTSStats,
       "ccapAppIntfTTSEvtLog": ccapAppIntfTTSEvtLog,
       "ccapAppIntfTTSReadRequest": ccapAppIntfTTSReadRequest,
       "ccapAppIntfTTSReadSuccess": ccapAppIntfTTSReadSuccess,
       "ccapAppIntfTTSReadFailure": ccapAppIntfTTSReadFailure,
       "ccapAppIntfTTSLastResetTime": ccapAppIntfTTSLastResetTime,
       "ciscoCallApplicationMIBConformance": ciscoCallApplicationMIBConformance,
       "ciscoCallApplicationMIBCompliances": ciscoCallApplicationMIBCompliances,
       "ciscoCallApplicationMIBCompliance": ciscoCallApplicationMIBCompliance,
       "ciscoCallApplicationMIBComplianceRev1": ciscoCallApplicationMIBComplianceRev1,
       "ciscoCallApplicationMIBGroups": ciscoCallApplicationMIBGroups,
       "ccapGeneralCfgGroup": ccapGeneralCfgGroup,
       "ccapGeneralCfgGroupRev1": ccapGeneralCfgGroupRev1,
       "ccapAppTypeHistoryGroup": ccapAppTypeHistoryGroup,
       "ccapAppInstanceHistoryGroup": ccapAppInstanceHistoryGroup,
       "ccapAppGblActGroup": ccapAppGblActGroup,
       "ccapAppGblCfgGroup": ccapAppGblCfgGroup,
       "ccapAppGblHisGroup": ccapAppGblHisGroup,
       "ccapAppIntfGblCfgGroup": ccapAppIntfGblCfgGroup,
       "ccapAppIntfHTTPGroup": ccapAppIntfHTTPGroup,
       "ccapAppIntfRTSPGroup": ccapAppIntfRTSPGroup,
       "ccapAppIntfTFTPGroup": ccapAppIntfTFTPGroup,
       "ccapAppIntfSMTPGroup": ccapAppIntfSMTPGroup,
       "ccapAppIntfAAAMethodListGroup": ccapAppIntfAAAMethodListGroup,
       "ccapAppIntfASRGroup": ccapAppIntfASRGroup,
       "ccapAppIntfTTSGroup": ccapAppIntfTTSGroup,
       "ccapAppIntfFlashGroup": ccapAppIntfFlashGroup,
       "ccapAppIntfRAMRecordGroup": ccapAppIntfRAMRecordGroup}
)
