# SNMP MIB module (CISCO-CIDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CIDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:24 2024
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

(CiscoIpProtocol,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoIpProtocol",
    "Unsigned64")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCidsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383)
)
ciscoCidsMIB.setRevisions(
        ("2013-08-08 00:00",
         "2008-06-26 00:00",
         "2006-03-02 00:00",
         "2005-10-10 00:00",
         "2003-12-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CidsHealthStatusColor(Integer32, TextualConvention):
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
        *(("green", 1),
          ("red", 3),
          ("yellow", 2))
    )



class CidsApplicationStatus(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("notResponding", 1),
          ("notRunning", 2),
          ("processingTransaction", 3),
          ("reconfiguring", 4),
          ("running", 5),
          ("starting", 6),
          ("stopping", 7),
          ("unknown", 8),
          ("upgradeInprogress", 9))
    )



class CidsErrorCode(Integer32, TextualConvention):
    status = "current"
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("errAuthenticationTokenExpired", 1),
          ("errConfigCollision", 2),
          ("errEngineBuildFailed", 16),
          ("errInUse", 3),
          ("errInvalidDocument", 4),
          ("errLimitExceeded", 5),
          ("errNotAvailable", 6),
          ("errNotFound", 7),
          ("errNotSupported", 8),
          ("errPermissionDenied", 9),
          ("errSyslog", 10),
          ("errSystemError", 11),
          ("errTransport", 12),
          ("errUnacceptableValue", 13),
          ("errUnclassified", 14),
          ("errWarning", 15))
    )



class CidsTargetValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("high", 4),
          ("low", 2),
          ("medium", 3),
          ("missionCritical", 5),
          ("zeroValue", 1))
    )



class CidsAttackRelevance(Integer32, TextualConvention):
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
        *(("notRelevant", 2),
          ("relevant", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCidsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCidsMIBNotifs = _CiscoCidsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 0)
)
_CiscoCidsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCidsMIBObjects = _CiscoCidsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1)
)
_CidsGeneral_ObjectIdentity = ObjectIdentity
cidsGeneral = _CidsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1)
)
_CidsGeneralEventId_Type = Unsigned64
_CidsGeneralEventId_Object = MibScalar
cidsGeneralEventId = _CidsGeneralEventId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 1),
    _CidsGeneralEventId_Type()
)
cidsGeneralEventId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralEventId.setStatus("current")
_CidsGeneralLocalTime_Type = DateAndTime
_CidsGeneralLocalTime_Object = MibScalar
cidsGeneralLocalTime = _CidsGeneralLocalTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 2),
    _CidsGeneralLocalTime_Type()
)
cidsGeneralLocalTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralLocalTime.setStatus("current")
_CidsGeneralUTCTime_Type = DateAndTime
_CidsGeneralUTCTime_Object = MibScalar
cidsGeneralUTCTime = _CidsGeneralUTCTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 3),
    _CidsGeneralUTCTime_Type()
)
cidsGeneralUTCTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralUTCTime.setStatus("current")
_CidsGeneralOriginatorHostId_Type = SnmpAdminString
_CidsGeneralOriginatorHostId_Object = MibScalar
cidsGeneralOriginatorHostId = _CidsGeneralOriginatorHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 4),
    _CidsGeneralOriginatorHostId_Type()
)
cidsGeneralOriginatorHostId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralOriginatorHostId.setStatus("current")
_CidsGeneralOriginatorAppName_Type = SnmpAdminString
_CidsGeneralOriginatorAppName_Object = MibScalar
cidsGeneralOriginatorAppName = _CidsGeneralOriginatorAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 5),
    _CidsGeneralOriginatorAppName_Type()
)
cidsGeneralOriginatorAppName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralOriginatorAppName.setStatus("current")
_CidsGeneralOriginatorAppId_Type = SnmpAdminString
_CidsGeneralOriginatorAppId_Object = MibScalar
cidsGeneralOriginatorAppId = _CidsGeneralOriginatorAppId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 6),
    _CidsGeneralOriginatorAppId_Type()
)
cidsGeneralOriginatorAppId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsGeneralOriginatorAppId.setStatus("current")


class _CidsNotificationsEnabled_Type(TruthValue):
    """Custom type cidsNotificationsEnabled based on TruthValue"""


_CidsNotificationsEnabled_Object = MibScalar
cidsNotificationsEnabled = _CidsNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 1, 7),
    _CidsNotificationsEnabled_Type()
)
cidsNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cidsNotificationsEnabled.setStatus("current")
_CidsAlert_ObjectIdentity = ObjectIdentity
cidsAlert = _CidsAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2)
)
_CidsAlertSeverity_Type = SnmpAdminString
_CidsAlertSeverity_Object = MibScalar
cidsAlertSeverity = _CidsAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 1),
    _CidsAlertSeverity_Type()
)
cidsAlertSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSeverity.setStatus("current")
_CidsAlertAlarmTraits_Type = Unsigned32
_CidsAlertAlarmTraits_Object = MibScalar
cidsAlertAlarmTraits = _CidsAlertAlarmTraits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 2),
    _CidsAlertAlarmTraits_Type()
)
cidsAlertAlarmTraits.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertAlarmTraits.setStatus("current")


class _CidsAlertSignature_Type(SnmpAdminString):
    """Custom type cidsAlertSignature based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsAlertSignature_Type.__name__ = "SnmpAdminString"
_CidsAlertSignature_Object = MibScalar
cidsAlertSignature = _CidsAlertSignature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 3),
    _CidsAlertSignature_Type()
)
cidsAlertSignature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSignature.setStatus("current")


class _CidsAlertSignatureSigName_Type(SnmpAdminString):
    """Custom type cidsAlertSignatureSigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsAlertSignatureSigName_Type.__name__ = "SnmpAdminString"
_CidsAlertSignatureSigName_Object = MibScalar
cidsAlertSignatureSigName = _CidsAlertSignatureSigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 4),
    _CidsAlertSignatureSigName_Type()
)
cidsAlertSignatureSigName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSignatureSigName.setStatus("current")
_CidsAlertSignatureSigId_Type = Unsigned32
_CidsAlertSignatureSigId_Object = MibScalar
cidsAlertSignatureSigId = _CidsAlertSignatureSigId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 5),
    _CidsAlertSignatureSigId_Type()
)
cidsAlertSignatureSigId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSignatureSigId.setStatus("current")
_CidsAlertSignatureSubSigId_Type = Unsigned32
_CidsAlertSignatureSubSigId_Object = MibScalar
cidsAlertSignatureSubSigId = _CidsAlertSignatureSubSigId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 6),
    _CidsAlertSignatureSubSigId_Type()
)
cidsAlertSignatureSubSigId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSignatureSubSigId.setStatus("current")


class _CidsAlertSignatureVersion_Type(SnmpAdminString):
    """Custom type cidsAlertSignatureVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsAlertSignatureVersion_Type.__name__ = "SnmpAdminString"
_CidsAlertSignatureVersion_Object = MibScalar
cidsAlertSignatureVersion = _CidsAlertSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 7),
    _CidsAlertSignatureVersion_Type()
)
cidsAlertSignatureVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSignatureVersion.setStatus("current")
_CidsAlertSummary_Type = Unsigned32
_CidsAlertSummary_Object = MibScalar
cidsAlertSummary = _CidsAlertSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 8),
    _CidsAlertSummary_Type()
)
cidsAlertSummary.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSummary.setStatus("current")


class _CidsAlertSummaryType_Type(SnmpAdminString):
    """Custom type cidsAlertSummaryType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CidsAlertSummaryType_Type.__name__ = "SnmpAdminString"
_CidsAlertSummaryType_Object = MibScalar
cidsAlertSummaryType = _CidsAlertSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 9),
    _CidsAlertSummaryType_Type()
)
cidsAlertSummaryType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSummaryType.setStatus("current")
_CidsAlertSummaryFinal_Type = TruthValue
_CidsAlertSummaryFinal_Object = MibScalar
cidsAlertSummaryFinal = _CidsAlertSummaryFinal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 10),
    _CidsAlertSummaryFinal_Type()
)
cidsAlertSummaryFinal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSummaryFinal.setStatus("current")
_CidsAlertSummaryInitialAlert_Type = Unsigned64
_CidsAlertSummaryInitialAlert_Object = MibScalar
cidsAlertSummaryInitialAlert = _CidsAlertSummaryInitialAlert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 11),
    _CidsAlertSummaryInitialAlert_Type()
)
cidsAlertSummaryInitialAlert.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertSummaryInitialAlert.setStatus("current")


class _CidsAlertInterfaceGroup_Type(Integer32):
    """Custom type cidsAlertInterfaceGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CidsAlertInterfaceGroup_Type.__name__ = "Integer32"
_CidsAlertInterfaceGroup_Object = MibScalar
cidsAlertInterfaceGroup = _CidsAlertInterfaceGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 12),
    _CidsAlertInterfaceGroup_Type()
)
cidsAlertInterfaceGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertInterfaceGroup.setStatus("deprecated")


class _CidsAlertVlan_Type(Unsigned32):
    """Custom type cidsAlertVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CidsAlertVlan_Type.__name__ = "Unsigned32"
_CidsAlertVlan_Object = MibScalar
cidsAlertVlan = _CidsAlertVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 13),
    _CidsAlertVlan_Type()
)
cidsAlertVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertVlan.setStatus("current")
_CidsAlertVictimContext_Type = SnmpAdminString
_CidsAlertVictimContext_Object = MibScalar
cidsAlertVictimContext = _CidsAlertVictimContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 14),
    _CidsAlertVictimContext_Type()
)
cidsAlertVictimContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertVictimContext.setStatus("current")
_CidsAlertAttackerContext_Type = SnmpAdminString
_CidsAlertAttackerContext_Object = MibScalar
cidsAlertAttackerContext = _CidsAlertAttackerContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 15),
    _CidsAlertAttackerContext_Type()
)
cidsAlertAttackerContext.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertAttackerContext.setStatus("current")
_CidsAlertAttackerAddress_Type = SnmpAdminString
_CidsAlertAttackerAddress_Object = MibScalar
cidsAlertAttackerAddress = _CidsAlertAttackerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 16),
    _CidsAlertAttackerAddress_Type()
)
cidsAlertAttackerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertAttackerAddress.setStatus("current")
_CidsAlertVictimAddress_Type = SnmpAdminString
_CidsAlertVictimAddress_Object = MibScalar
cidsAlertVictimAddress = _CidsAlertVictimAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 17),
    _CidsAlertVictimAddress_Type()
)
cidsAlertVictimAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertVictimAddress.setStatus("current")
_CidsAlertIpLoggingActivated_Type = TruthValue
_CidsAlertIpLoggingActivated_Object = MibScalar
cidsAlertIpLoggingActivated = _CidsAlertIpLoggingActivated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 18),
    _CidsAlertIpLoggingActivated_Type()
)
cidsAlertIpLoggingActivated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertIpLoggingActivated.setStatus("current")
_CidsAlertTcpResetSent_Type = TruthValue
_CidsAlertTcpResetSent_Object = MibScalar
cidsAlertTcpResetSent = _CidsAlertTcpResetSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 19),
    _CidsAlertTcpResetSent_Type()
)
cidsAlertTcpResetSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertTcpResetSent.setStatus("current")
_CidsAlertShunRequested_Type = TruthValue
_CidsAlertShunRequested_Object = MibScalar
cidsAlertShunRequested = _CidsAlertShunRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 20),
    _CidsAlertShunRequested_Type()
)
cidsAlertShunRequested.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertShunRequested.setStatus("current")
_CidsAlertDetails_Type = SnmpAdminString
_CidsAlertDetails_Object = MibScalar
cidsAlertDetails = _CidsAlertDetails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 21),
    _CidsAlertDetails_Type()
)
cidsAlertDetails.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDetails.setStatus("current")
_CidsAlertIpLogId_Type = SnmpAdminString
_CidsAlertIpLogId_Object = MibScalar
cidsAlertIpLogId = _CidsAlertIpLogId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 22),
    _CidsAlertIpLogId_Type()
)
cidsAlertIpLogId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertIpLogId.setStatus("current")
_CidsThreatResponseStatus_Type = SnmpAdminString
_CidsThreatResponseStatus_Object = MibScalar
cidsThreatResponseStatus = _CidsThreatResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 23),
    _CidsThreatResponseStatus_Type()
)
cidsThreatResponseStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsThreatResponseStatus.setStatus("current")


class _CidsThreatResponseSeverity_Type(Integer32):
    """Custom type cidsThreatResponseSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CidsThreatResponseSeverity_Type.__name__ = "Integer32"
_CidsThreatResponseSeverity_Object = MibScalar
cidsThreatResponseSeverity = _CidsThreatResponseSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 24),
    _CidsThreatResponseSeverity_Type()
)
cidsThreatResponseSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsThreatResponseSeverity.setStatus("current")
_CidsAlertEventRiskRating_Type = Unsigned32
_CidsAlertEventRiskRating_Object = MibScalar
cidsAlertEventRiskRating = _CidsAlertEventRiskRating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 25),
    _CidsAlertEventRiskRating_Type()
)
cidsAlertEventRiskRating.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertEventRiskRating.setStatus("current")
_CidsAlertIfIndex_Type = InterfaceIndex
_CidsAlertIfIndex_Object = MibScalar
cidsAlertIfIndex = _CidsAlertIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 26),
    _CidsAlertIfIndex_Type()
)
cidsAlertIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertIfIndex.setStatus("current")
_CidsAlertProtocol_Type = CiscoIpProtocol
_CidsAlertProtocol_Object = MibScalar
cidsAlertProtocol = _CidsAlertProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 27),
    _CidsAlertProtocol_Type()
)
cidsAlertProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertProtocol.setStatus("current")
_CidsAlertDeniedAttacker_Type = TruthValue
_CidsAlertDeniedAttacker_Object = MibScalar
cidsAlertDeniedAttacker = _CidsAlertDeniedAttacker_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 28),
    _CidsAlertDeniedAttacker_Type()
)
cidsAlertDeniedAttacker.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDeniedAttacker.setStatus("current")
_CidsAlertDeniedFlow_Type = TruthValue
_CidsAlertDeniedFlow_Object = MibScalar
cidsAlertDeniedFlow = _CidsAlertDeniedFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 29),
    _CidsAlertDeniedFlow_Type()
)
cidsAlertDeniedFlow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDeniedFlow.setStatus("current")
_CidsAlertDenyPacketReqNotPerf_Type = TruthValue
_CidsAlertDenyPacketReqNotPerf_Object = MibScalar
cidsAlertDenyPacketReqNotPerf = _CidsAlertDenyPacketReqNotPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 30),
    _CidsAlertDenyPacketReqNotPerf_Type()
)
cidsAlertDenyPacketReqNotPerf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyPacketReqNotPerf.setStatus("current")
_CidsAlertDenyFlowReqNotPerf_Type = TruthValue
_CidsAlertDenyFlowReqNotPerf_Object = MibScalar
cidsAlertDenyFlowReqNotPerf = _CidsAlertDenyFlowReqNotPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 31),
    _CidsAlertDenyFlowReqNotPerf_Type()
)
cidsAlertDenyFlowReqNotPerf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyFlowReqNotPerf.setStatus("current")
_CidsAlertDenyAttackerReqNotPerf_Type = TruthValue
_CidsAlertDenyAttackerReqNotPerf_Object = MibScalar
cidsAlertDenyAttackerReqNotPerf = _CidsAlertDenyAttackerReqNotPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 32),
    _CidsAlertDenyAttackerReqNotPerf_Type()
)
cidsAlertDenyAttackerReqNotPerf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyAttackerReqNotPerf.setStatus("current")
_CidsAlertBlockConnectionReq_Type = TruthValue
_CidsAlertBlockConnectionReq_Object = MibScalar
cidsAlertBlockConnectionReq = _CidsAlertBlockConnectionReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 33),
    _CidsAlertBlockConnectionReq_Type()
)
cidsAlertBlockConnectionReq.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertBlockConnectionReq.setStatus("current")
_CidsAlertLogAttackerPacketsAct_Type = TruthValue
_CidsAlertLogAttackerPacketsAct_Object = MibScalar
cidsAlertLogAttackerPacketsAct = _CidsAlertLogAttackerPacketsAct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 34),
    _CidsAlertLogAttackerPacketsAct_Type()
)
cidsAlertLogAttackerPacketsAct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertLogAttackerPacketsAct.setStatus("current")
_CidsAlertLogVictimPacketsAct_Type = TruthValue
_CidsAlertLogVictimPacketsAct_Object = MibScalar
cidsAlertLogVictimPacketsAct = _CidsAlertLogVictimPacketsAct_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 35),
    _CidsAlertLogVictimPacketsAct_Type()
)
cidsAlertLogVictimPacketsAct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertLogVictimPacketsAct.setStatus("current")
_CidsAlertLogPairPacketsActivated_Type = TruthValue
_CidsAlertLogPairPacketsActivated_Object = MibScalar
cidsAlertLogPairPacketsActivated = _CidsAlertLogPairPacketsActivated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 36),
    _CidsAlertLogPairPacketsActivated_Type()
)
cidsAlertLogPairPacketsActivated.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertLogPairPacketsActivated.setStatus("current")
_CidsAlertRateLimitRequested_Type = TruthValue
_CidsAlertRateLimitRequested_Object = MibScalar
cidsAlertRateLimitRequested = _CidsAlertRateLimitRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 37),
    _CidsAlertRateLimitRequested_Type()
)
cidsAlertRateLimitRequested.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertRateLimitRequested.setStatus("current")
_CidsAlertDeniedAttackVictimPair_Type = TruthValue
_CidsAlertDeniedAttackVictimPair_Object = MibScalar
cidsAlertDeniedAttackVictimPair = _CidsAlertDeniedAttackVictimPair_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 38),
    _CidsAlertDeniedAttackVictimPair_Type()
)
cidsAlertDeniedAttackVictimPair.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDeniedAttackVictimPair.setStatus("current")
_CidsAlertDeniedAttackSericePair_Type = TruthValue
_CidsAlertDeniedAttackSericePair_Object = MibScalar
cidsAlertDeniedAttackSericePair = _CidsAlertDeniedAttackSericePair_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 39),
    _CidsAlertDeniedAttackSericePair_Type()
)
cidsAlertDeniedAttackSericePair.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDeniedAttackSericePair.setStatus("current")
_CidsAlertDenyAttackVicReqNotPerf_Type = TruthValue
_CidsAlertDenyAttackVicReqNotPerf_Object = MibScalar
cidsAlertDenyAttackVicReqNotPerf = _CidsAlertDenyAttackVicReqNotPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 40),
    _CidsAlertDenyAttackVicReqNotPerf_Type()
)
cidsAlertDenyAttackVicReqNotPerf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyAttackVicReqNotPerf.setStatus("current")
_CidsAlertDenyAttackSerReqNotPerf_Type = TruthValue
_CidsAlertDenyAttackSerReqNotPerf_Object = MibScalar
cidsAlertDenyAttackSerReqNotPerf = _CidsAlertDenyAttackSerReqNotPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 41),
    _CidsAlertDenyAttackSerReqNotPerf_Type()
)
cidsAlertDenyAttackSerReqNotPerf.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyAttackSerReqNotPerf.setStatus("current")
_CidsAlertThreatValueRating_Type = Unsigned32
_CidsAlertThreatValueRating_Object = MibScalar
cidsAlertThreatValueRating = _CidsAlertThreatValueRating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 42),
    _CidsAlertThreatValueRating_Type()
)
cidsAlertThreatValueRating.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertThreatValueRating.setStatus("current")
_CidsAlertRiskRatingTargetValue_Type = CidsTargetValue
_CidsAlertRiskRatingTargetValue_Object = MibScalar
cidsAlertRiskRatingTargetValue = _CidsAlertRiskRatingTargetValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 43),
    _CidsAlertRiskRatingTargetValue_Type()
)
cidsAlertRiskRatingTargetValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertRiskRatingTargetValue.setStatus("current")
_CidsAlertRiskRatingRelevance_Type = CidsAttackRelevance
_CidsAlertRiskRatingRelevance_Object = MibScalar
cidsAlertRiskRatingRelevance = _CidsAlertRiskRatingRelevance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 44),
    _CidsAlertRiskRatingRelevance_Type()
)
cidsAlertRiskRatingRelevance.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertRiskRatingRelevance.setStatus("current")
_CidsAlertRiskRatingWatchList_Type = Unsigned32
_CidsAlertRiskRatingWatchList_Object = MibScalar
cidsAlertRiskRatingWatchList = _CidsAlertRiskRatingWatchList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 45),
    _CidsAlertRiskRatingWatchList_Type()
)
cidsAlertRiskRatingWatchList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertRiskRatingWatchList.setStatus("current")
_CidsAlertDenyPacket_Type = TruthValue
_CidsAlertDenyPacket_Object = MibScalar
cidsAlertDenyPacket = _CidsAlertDenyPacket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 46),
    _CidsAlertDenyPacket_Type()
)
cidsAlertDenyPacket.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertDenyPacket.setStatus("current")
_CidsAlertBlockHost_Type = TruthValue
_CidsAlertBlockHost_Object = MibScalar
cidsAlertBlockHost = _CidsAlertBlockHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 47),
    _CidsAlertBlockHost_Type()
)
cidsAlertBlockHost.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertBlockHost.setStatus("current")
_CidsAlertTcpOneWayResetSent_Type = TruthValue
_CidsAlertTcpOneWayResetSent_Object = MibScalar
cidsAlertTcpOneWayResetSent = _CidsAlertTcpOneWayResetSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 48),
    _CidsAlertTcpOneWayResetSent_Type()
)
cidsAlertTcpOneWayResetSent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertTcpOneWayResetSent.setStatus("current")


class _CidsAlertVirtualSensor_Type(SnmpAdminString):
    """Custom type cidsAlertVirtualSensor based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsAlertVirtualSensor_Type.__name__ = "SnmpAdminString"
_CidsAlertVirtualSensor_Object = MibScalar
cidsAlertVirtualSensor = _CidsAlertVirtualSensor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 2, 49),
    _CidsAlertVirtualSensor_Type()
)
cidsAlertVirtualSensor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsAlertVirtualSensor.setStatus("current")
_CidsError_ObjectIdentity = ObjectIdentity
cidsError = _CidsError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 3)
)
_CidsErrorSeverity_Type = SnmpAdminString
_CidsErrorSeverity_Object = MibScalar
cidsErrorSeverity = _CidsErrorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 3, 1),
    _CidsErrorSeverity_Type()
)
cidsErrorSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsErrorSeverity.setStatus("current")
_CidsErrorName_Type = CidsErrorCode
_CidsErrorName_Object = MibScalar
cidsErrorName = _CidsErrorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 3, 2),
    _CidsErrorName_Type()
)
cidsErrorName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsErrorName.setStatus("current")
_CidsErrorMessage_Type = SnmpAdminString
_CidsErrorMessage_Object = MibScalar
cidsErrorMessage = _CidsErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 3, 3),
    _CidsErrorMessage_Type()
)
cidsErrorMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsErrorMessage.setStatus("current")
_CidsHealth_ObjectIdentity = ObjectIdentity
cidsHealth = _CidsHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4)
)


class _CidsHealthPacketLoss_Type(Integer32):
    """Custom type cidsHealthPacketLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CidsHealthPacketLoss_Type.__name__ = "Integer32"
_CidsHealthPacketLoss_Object = MibScalar
cidsHealthPacketLoss = _CidsHealthPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 1),
    _CidsHealthPacketLoss_Type()
)
cidsHealthPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthPacketLoss.setStatus("current")
if mibBuilder.loadTexts:
    cidsHealthPacketLoss.setUnits("percent")


class _CidsHealthPacketDenialRate_Type(Integer32):
    """Custom type cidsHealthPacketDenialRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CidsHealthPacketDenialRate_Type.__name__ = "Integer32"
_CidsHealthPacketDenialRate_Object = MibScalar
cidsHealthPacketDenialRate = _CidsHealthPacketDenialRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 2),
    _CidsHealthPacketDenialRate_Type()
)
cidsHealthPacketDenialRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthPacketDenialRate.setStatus("current")
if mibBuilder.loadTexts:
    cidsHealthPacketDenialRate.setUnits("percent")
_CidsHealthAlarmsGenerated_Type = Counter32
_CidsHealthAlarmsGenerated_Object = MibScalar
cidsHealthAlarmsGenerated = _CidsHealthAlarmsGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 3),
    _CidsHealthAlarmsGenerated_Type()
)
cidsHealthAlarmsGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthAlarmsGenerated.setStatus("current")
_CidsHealthFragmentsInFRU_Type = Gauge32
_CidsHealthFragmentsInFRU_Object = MibScalar
cidsHealthFragmentsInFRU = _CidsHealthFragmentsInFRU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 4),
    _CidsHealthFragmentsInFRU_Type()
)
cidsHealthFragmentsInFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthFragmentsInFRU.setStatus("current")
_CidsHealthDatagramsInFRU_Type = Gauge32
_CidsHealthDatagramsInFRU_Object = MibScalar
cidsHealthDatagramsInFRU = _CidsHealthDatagramsInFRU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 5),
    _CidsHealthDatagramsInFRU_Type()
)
cidsHealthDatagramsInFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthDatagramsInFRU.setStatus("current")
_CidsHealthTcpEmbryonicStreams_Type = Gauge32
_CidsHealthTcpEmbryonicStreams_Object = MibScalar
cidsHealthTcpEmbryonicStreams = _CidsHealthTcpEmbryonicStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 6),
    _CidsHealthTcpEmbryonicStreams_Type()
)
cidsHealthTcpEmbryonicStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthTcpEmbryonicStreams.setStatus("current")
_CidsHealthTCPEstablishedStreams_Type = Gauge32
_CidsHealthTCPEstablishedStreams_Object = MibScalar
cidsHealthTCPEstablishedStreams = _CidsHealthTCPEstablishedStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 7),
    _CidsHealthTCPEstablishedStreams_Type()
)
cidsHealthTCPEstablishedStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthTCPEstablishedStreams.setStatus("current")
_CidsHealthTcpClosingStreams_Type = Gauge32
_CidsHealthTcpClosingStreams_Object = MibScalar
cidsHealthTcpClosingStreams = _CidsHealthTcpClosingStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 8),
    _CidsHealthTcpClosingStreams_Type()
)
cidsHealthTcpClosingStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthTcpClosingStreams.setStatus("current")
_CidsHealthTcpStreams_Type = Gauge32
_CidsHealthTcpStreams_Object = MibScalar
cidsHealthTcpStreams = _CidsHealthTcpStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 9),
    _CidsHealthTcpStreams_Type()
)
cidsHealthTcpStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthTcpStreams.setStatus("current")
_CidsHealthActiveNodes_Type = Gauge32
_CidsHealthActiveNodes_Object = MibScalar
cidsHealthActiveNodes = _CidsHealthActiveNodes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 10),
    _CidsHealthActiveNodes_Type()
)
cidsHealthActiveNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthActiveNodes.setStatus("current")
_CidsHealthTcpDualIpAndPorts_Type = Gauge32
_CidsHealthTcpDualIpAndPorts_Object = MibScalar
cidsHealthTcpDualIpAndPorts = _CidsHealthTcpDualIpAndPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 11),
    _CidsHealthTcpDualIpAndPorts_Type()
)
cidsHealthTcpDualIpAndPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthTcpDualIpAndPorts.setStatus("current")
_CidsHealthUdpDualIpAndPorts_Type = Gauge32
_CidsHealthUdpDualIpAndPorts_Object = MibScalar
cidsHealthUdpDualIpAndPorts = _CidsHealthUdpDualIpAndPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 12),
    _CidsHealthUdpDualIpAndPorts_Type()
)
cidsHealthUdpDualIpAndPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthUdpDualIpAndPorts.setStatus("current")
_CidsHealthIpDualIp_Type = Gauge32
_CidsHealthIpDualIp_Object = MibScalar
cidsHealthIpDualIp = _CidsHealthIpDualIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 13),
    _CidsHealthIpDualIp_Type()
)
cidsHealthIpDualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthIpDualIp.setStatus("current")


class _CidsHealthIsSensorMemoryCritical_Type(Unsigned32):
    """Custom type cidsHealthIsSensorMemoryCritical based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CidsHealthIsSensorMemoryCritical_Type.__name__ = "Unsigned32"
_CidsHealthIsSensorMemoryCritical_Object = MibScalar
cidsHealthIsSensorMemoryCritical = _CidsHealthIsSensorMemoryCritical_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 14),
    _CidsHealthIsSensorMemoryCritical_Type()
)
cidsHealthIsSensorMemoryCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthIsSensorMemoryCritical.setStatus("current")
_CidsHealthIsSensorActive_Type = TruthValue
_CidsHealthIsSensorActive_Object = MibScalar
cidsHealthIsSensorActive = _CidsHealthIsSensorActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 15),
    _CidsHealthIsSensorActive_Type()
)
cidsHealthIsSensorActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthIsSensorActive.setStatus("current")
_CidsHealthCommandAndControlPort_Type = SnmpAdminString
_CidsHealthCommandAndControlPort_Object = MibScalar
cidsHealthCommandAndControlPort = _CidsHealthCommandAndControlPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 16),
    _CidsHealthCommandAndControlPort_Type()
)
cidsHealthCommandAndControlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthCommandAndControlPort.setStatus("current")
_CidsHealthSensorStatsResetTime_Type = TimeTicks
_CidsHealthSensorStatsResetTime_Object = MibScalar
cidsHealthSensorStatsResetTime = _CidsHealthSensorStatsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 17),
    _CidsHealthSensorStatsResetTime_Type()
)
cidsHealthSensorStatsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSensorStatsResetTime.setStatus("current")
_CidsHealthSecMonAvailability_Type = TruthValue
_CidsHealthSecMonAvailability_Object = MibScalar
cidsHealthSecMonAvailability = _CidsHealthSecMonAvailability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 18),
    _CidsHealthSecMonAvailability_Type()
)
cidsHealthSecMonAvailability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonAvailability.setStatus("current")
_CidsHealthSecMonOverallHealth_Type = CidsHealthStatusColor
_CidsHealthSecMonOverallHealth_Object = MibScalar
cidsHealthSecMonOverallHealth = _CidsHealthSecMonOverallHealth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 19),
    _CidsHealthSecMonOverallHealth_Type()
)
cidsHealthSecMonOverallHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonOverallHealth.setStatus("current")


class _CidsHealthSecMonSoftwareVersion_Type(DisplayString):
    """Custom type cidsHealthSecMonSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CidsHealthSecMonSoftwareVersion_Type.__name__ = "DisplayString"
_CidsHealthSecMonSoftwareVersion_Object = MibScalar
cidsHealthSecMonSoftwareVersion = _CidsHealthSecMonSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 20),
    _CidsHealthSecMonSoftwareVersion_Type()
)
cidsHealthSecMonSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonSoftwareVersion.setStatus("current")


class _CidsHealthSecMonSignatureVersion_Type(DisplayString):
    """Custom type cidsHealthSecMonSignatureVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CidsHealthSecMonSignatureVersion_Type.__name__ = "DisplayString"
_CidsHealthSecMonSignatureVersion_Object = MibScalar
cidsHealthSecMonSignatureVersion = _CidsHealthSecMonSignatureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 21),
    _CidsHealthSecMonSignatureVersion_Type()
)
cidsHealthSecMonSignatureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonSignatureVersion.setStatus("current")


class _CidsHealthSecMonLicenseStatus_Type(DisplayString):
    """Custom type cidsHealthSecMonLicenseStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CidsHealthSecMonLicenseStatus_Type.__name__ = "DisplayString"
_CidsHealthSecMonLicenseStatus_Object = MibScalar
cidsHealthSecMonLicenseStatus = _CidsHealthSecMonLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 22),
    _CidsHealthSecMonLicenseStatus_Type()
)
cidsHealthSecMonLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonLicenseStatus.setStatus("current")
_CidsHealthSecMonOverallAppColor_Type = CidsHealthStatusColor
_CidsHealthSecMonOverallAppColor_Object = MibScalar
cidsHealthSecMonOverallAppColor = _CidsHealthSecMonOverallAppColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 23),
    _CidsHealthSecMonOverallAppColor_Type()
)
cidsHealthSecMonOverallAppColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsHealthSecMonOverallAppColor.setStatus("current")
_CidsHealthSecMonMainAppStatus_Type = CidsApplicationStatus
_CidsHealthSecMonMainAppStatus_Object = MibScalar
cidsHealthSecMonMainAppStatus = _CidsHealthSecMonMainAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 24),
    _CidsHealthSecMonMainAppStatus_Type()
)
cidsHealthSecMonMainAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonMainAppStatus.setStatus("current")
_CidsHealthSecMonAnalysisEngineStatus_Type = CidsApplicationStatus
_CidsHealthSecMonAnalysisEngineStatus_Object = MibScalar
cidsHealthSecMonAnalysisEngineStatus = _CidsHealthSecMonAnalysisEngineStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 25),
    _CidsHealthSecMonAnalysisEngineStatus_Type()
)
cidsHealthSecMonAnalysisEngineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonAnalysisEngineStatus.setStatus("current")
_CidsHealthSecMonCollaborationAppStatus_Type = CidsApplicationStatus
_CidsHealthSecMonCollaborationAppStatus_Object = MibScalar
cidsHealthSecMonCollaborationAppStatus = _CidsHealthSecMonCollaborationAppStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 26),
    _CidsHealthSecMonCollaborationAppStatus_Type()
)
cidsHealthSecMonCollaborationAppStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonCollaborationAppStatus.setStatus("current")
_CidsHealthSecMonByPassMode_Type = TruthValue
_CidsHealthSecMonByPassMode_Object = MibScalar
cidsHealthSecMonByPassMode = _CidsHealthSecMonByPassMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 27),
    _CidsHealthSecMonByPassMode_Type()
)
cidsHealthSecMonByPassMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsHealthSecMonByPassMode.setStatus("current")


class _CidsHealthSecMonMissedPktPctAndThresh_Type(DisplayString):
    """Custom type cidsHealthSecMonMissedPktPctAndThresh based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CidsHealthSecMonMissedPktPctAndThresh_Type.__name__ = "DisplayString"
_CidsHealthSecMonMissedPktPctAndThresh_Object = MibScalar
cidsHealthSecMonMissedPktPctAndThresh = _CidsHealthSecMonMissedPktPctAndThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 28),
    _CidsHealthSecMonMissedPktPctAndThresh_Type()
)
cidsHealthSecMonMissedPktPctAndThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonMissedPktPctAndThresh.setStatus("current")


class _CidsHealthSecMonAnalysisEngMemPercent_Type(Integer32):
    """Custom type cidsHealthSecMonAnalysisEngMemPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CidsHealthSecMonAnalysisEngMemPercent_Type.__name__ = "Integer32"
_CidsHealthSecMonAnalysisEngMemPercent_Object = MibScalar
cidsHealthSecMonAnalysisEngMemPercent = _CidsHealthSecMonAnalysisEngMemPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 29),
    _CidsHealthSecMonAnalysisEngMemPercent_Type()
)
cidsHealthSecMonAnalysisEngMemPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonAnalysisEngMemPercent.setStatus("current")
if mibBuilder.loadTexts:
    cidsHealthSecMonAnalysisEngMemPercent.setUnits("percent")


class _CidsHealthSecMonSensorLoad_Type(Integer32):
    """Custom type cidsHealthSecMonSensorLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CidsHealthSecMonSensorLoad_Type.__name__ = "Integer32"
_CidsHealthSecMonSensorLoad_Object = MibScalar
cidsHealthSecMonSensorLoad = _CidsHealthSecMonSensorLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 30),
    _CidsHealthSecMonSensorLoad_Type()
)
cidsHealthSecMonSensorLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonSensorLoad.setStatus("current")
_CidsHealthSecMonSensorLoadColor_Type = CidsHealthStatusColor
_CidsHealthSecMonSensorLoadColor_Object = MibScalar
cidsHealthSecMonSensorLoadColor = _CidsHealthSecMonSensorLoadColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 31),
    _CidsHealthSecMonSensorLoadColor_Type()
)
cidsHealthSecMonSensorLoadColor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cidsHealthSecMonSensorLoadColor.setStatus("current")
_CidsHealthSecMonVirtSensorStatusTable_Object = MibTable
cidsHealthSecMonVirtSensorStatusTable = _CidsHealthSecMonVirtSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 32)
)
if mibBuilder.loadTexts:
    cidsHealthSecMonVirtSensorStatusTable.setStatus("current")
_CidsHealthSecMonVirtSensorStatusEntry_Object = MibTableRow
cidsHealthSecMonVirtSensorStatusEntry = _CidsHealthSecMonVirtSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 32, 1)
)
cidsHealthSecMonVirtSensorStatusEntry.setIndexNames(
    (0, "CISCO-CIDS-MIB", "cidsHealthSecMonVirtSensorName"),
)
if mibBuilder.loadTexts:
    cidsHealthSecMonVirtSensorStatusEntry.setStatus("current")


class _CidsHealthSecMonVirtSensorName_Type(DisplayString):
    """Custom type cidsHealthSecMonVirtSensorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsHealthSecMonVirtSensorName_Type.__name__ = "DisplayString"
_CidsHealthSecMonVirtSensorName_Object = MibTableColumn
cidsHealthSecMonVirtSensorName = _CidsHealthSecMonVirtSensorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 32, 1, 1),
    _CidsHealthSecMonVirtSensorName_Type()
)
cidsHealthSecMonVirtSensorName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cidsHealthSecMonVirtSensorName.setStatus("current")
_CidsHealthSecMonVirtSensorStatus_Type = CidsHealthStatusColor
_CidsHealthSecMonVirtSensorStatus_Object = MibTableColumn
cidsHealthSecMonVirtSensorStatus = _CidsHealthSecMonVirtSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 32, 1, 2),
    _CidsHealthSecMonVirtSensorStatus_Type()
)
cidsHealthSecMonVirtSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonVirtSensorStatus.setStatus("current")
_CidsHealthSecMonDataStorageTable_Object = MibTable
cidsHealthSecMonDataStorageTable = _CidsHealthSecMonDataStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 33)
)
if mibBuilder.loadTexts:
    cidsHealthSecMonDataStorageTable.setStatus("current")
_CidsHealthSecMonDataStorageEntry_Object = MibTableRow
cidsHealthSecMonDataStorageEntry = _CidsHealthSecMonDataStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 33, 1)
)
cidsHealthSecMonDataStorageEntry.setIndexNames(
    (0, "CISCO-CIDS-MIB", "cidsHealthSecMonPartitionName"),
)
if mibBuilder.loadTexts:
    cidsHealthSecMonDataStorageEntry.setStatus("current")


class _CidsHealthSecMonPartitionName_Type(DisplayString):
    """Custom type cidsHealthSecMonPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CidsHealthSecMonPartitionName_Type.__name__ = "DisplayString"
_CidsHealthSecMonPartitionName_Object = MibTableColumn
cidsHealthSecMonPartitionName = _CidsHealthSecMonPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 33, 1, 1),
    _CidsHealthSecMonPartitionName_Type()
)
cidsHealthSecMonPartitionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cidsHealthSecMonPartitionName.setStatus("current")
_CidsHealthSecMonTotalPartitionSpace_Type = Unsigned32
_CidsHealthSecMonTotalPartitionSpace_Object = MibTableColumn
cidsHealthSecMonTotalPartitionSpace = _CidsHealthSecMonTotalPartitionSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 33, 1, 2),
    _CidsHealthSecMonTotalPartitionSpace_Type()
)
cidsHealthSecMonTotalPartitionSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonTotalPartitionSpace.setStatus("current")
if mibBuilder.loadTexts:
    cidsHealthSecMonTotalPartitionSpace.setUnits("MB")
_CidsHealthSecMonUtilizedPartitionSpace_Type = Unsigned32
_CidsHealthSecMonUtilizedPartitionSpace_Object = MibTableColumn
cidsHealthSecMonUtilizedPartitionSpace = _CidsHealthSecMonUtilizedPartitionSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 1, 4, 33, 1, 3),
    _CidsHealthSecMonUtilizedPartitionSpace_Type()
)
cidsHealthSecMonUtilizedPartitionSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cidsHealthSecMonUtilizedPartitionSpace.setStatus("current")
if mibBuilder.loadTexts:
    cidsHealthSecMonUtilizedPartitionSpace.setUnits("MB")
_CiscoCidsMIBConform_ObjectIdentity = ObjectIdentity
ciscoCidsMIBConform = _CiscoCidsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2)
)
_CiscoCidsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCidsMIBCompliances = _CiscoCidsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1)
)
_CiscoCidsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCidsMIBGroups = _CiscoCidsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2)
)

# Managed Objects groups

ciscoCidsGeneralObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 1)
)
ciscoCidsGeneralObjectGroup.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppName"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppId"),
        ("CISCO-CIDS-MIB", "cidsNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    ciscoCidsGeneralObjectGroup.setStatus("deprecated")

ciscoCidsAlertObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 2)
)
ciscoCidsAlertObjectGroup.setObjects(
      *(("CISCO-CIDS-MIB", "cidsAlertSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertAlarmTraits"),
        ("CISCO-CIDS-MIB", "cidsAlertSignature"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigName"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSubSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureVersion"),
        ("CISCO-CIDS-MIB", "cidsAlertSummary"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryType"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryFinal"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryInitialAlert"),
        ("CISCO-CIDS-MIB", "cidsAlertInterfaceGroup"),
        ("CISCO-CIDS-MIB", "cidsAlertVlan"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimContext"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerContext"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimAddress"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerAddress"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLoggingActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertTcpResetSent"),
        ("CISCO-CIDS-MIB", "cidsAlertShunRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDetails"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLogId"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseStatus"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertEventRiskRating"))
)
if mibBuilder.loadTexts:
    ciscoCidsAlertObjectGroup.setStatus("deprecated")

ciscoCidsErrorObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 3)
)
ciscoCidsErrorObjectGroup.setObjects(
      *(("CISCO-CIDS-MIB", "cidsErrorSeverity"),
        ("CISCO-CIDS-MIB", "cidsErrorName"),
        ("CISCO-CIDS-MIB", "cidsErrorMessage"))
)
if mibBuilder.loadTexts:
    ciscoCidsErrorObjectGroup.setStatus("current")

ciscoCidsHealthObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 5)
)
ciscoCidsHealthObjectGroup.setObjects(
      *(("CISCO-CIDS-MIB", "cidsHealthPacketLoss"),
        ("CISCO-CIDS-MIB", "cidsHealthPacketDenialRate"),
        ("CISCO-CIDS-MIB", "cidsHealthAlarmsGenerated"),
        ("CISCO-CIDS-MIB", "cidsHealthFragmentsInFRU"),
        ("CISCO-CIDS-MIB", "cidsHealthDatagramsInFRU"),
        ("CISCO-CIDS-MIB", "cidsHealthTcpEmbryonicStreams"),
        ("CISCO-CIDS-MIB", "cidsHealthTCPEstablishedStreams"),
        ("CISCO-CIDS-MIB", "cidsHealthTcpClosingStreams"),
        ("CISCO-CIDS-MIB", "cidsHealthTcpStreams"),
        ("CISCO-CIDS-MIB", "cidsHealthActiveNodes"),
        ("CISCO-CIDS-MIB", "cidsHealthTcpDualIpAndPorts"),
        ("CISCO-CIDS-MIB", "cidsHealthUdpDualIpAndPorts"),
        ("CISCO-CIDS-MIB", "cidsHealthIpDualIp"),
        ("CISCO-CIDS-MIB", "cidsHealthIsSensorMemoryCritical"),
        ("CISCO-CIDS-MIB", "cidsHealthIsSensorActive"),
        ("CISCO-CIDS-MIB", "cidsHealthCommandAndControlPort"),
        ("CISCO-CIDS-MIB", "cidsHealthSensorStatsResetTime"))
)
if mibBuilder.loadTexts:
    ciscoCidsHealthObjectGroup.setStatus("current")

ciscoCidsGeneralObjectGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 6)
)
ciscoCidsGeneralObjectGroupRev1.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsNotificationsEnabled"))
)
if mibBuilder.loadTexts:
    ciscoCidsGeneralObjectGroupRev1.setStatus("current")

ciscoCidsAlertObjectGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 7)
)
ciscoCidsAlertObjectGroupRev1.setObjects(
      *(("CISCO-CIDS-MIB", "cidsAlertSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertAlarmTraits"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigName"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSubSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimAddress"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerAddress"))
)
if mibBuilder.loadTexts:
    ciscoCidsAlertObjectGroupRev1.setStatus("current")

ciscoCidsOptionalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 8)
)
ciscoCidsOptionalObjectGroup.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppName"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignature"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureVersion"),
        ("CISCO-CIDS-MIB", "cidsAlertSummary"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryType"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryFinal"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryInitialAlert"),
        ("CISCO-CIDS-MIB", "cidsAlertInterfaceGroup"),
        ("CISCO-CIDS-MIB", "cidsAlertVlan"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimContext"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerContext"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLoggingActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertTcpResetSent"),
        ("CISCO-CIDS-MIB", "cidsAlertShunRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDetails"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLogId"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseStatus"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertEventRiskRating"),
        ("CISCO-CIDS-MIB", "cidsAlertIfIndex"),
        ("CISCO-CIDS-MIB", "cidsAlertProtocol"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttacker"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedFlow"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyPacketReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyFlowReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackerReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertBlockConnectionReq"),
        ("CISCO-CIDS-MIB", "cidsAlertLogAttackerPacketsAct"),
        ("CISCO-CIDS-MIB", "cidsAlertLogVictimPacketsAct"),
        ("CISCO-CIDS-MIB", "cidsAlertLogPairPacketsActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertRateLimitRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttackVictimPair"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttackSericePair"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackVicReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackSerReqNotPerf"))
)
if mibBuilder.loadTexts:
    ciscoCidsOptionalObjectGroup.setStatus("deprecated")

ciscoCidsOptionalObjectGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 9)
)
ciscoCidsOptionalObjectGroupRev1.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppName"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorAppId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignature"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureVersion"),
        ("CISCO-CIDS-MIB", "cidsAlertSummary"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryType"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryFinal"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryInitialAlert"),
        ("CISCO-CIDS-MIB", "cidsAlertInterfaceGroup"),
        ("CISCO-CIDS-MIB", "cidsAlertVlan"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimContext"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerContext"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLoggingActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertTcpResetSent"),
        ("CISCO-CIDS-MIB", "cidsAlertShunRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDetails"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLogId"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseStatus"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertEventRiskRating"),
        ("CISCO-CIDS-MIB", "cidsAlertIfIndex"),
        ("CISCO-CIDS-MIB", "cidsAlertProtocol"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttacker"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedFlow"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyPacketReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyFlowReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackerReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertBlockConnectionReq"),
        ("CISCO-CIDS-MIB", "cidsAlertLogAttackerPacketsAct"),
        ("CISCO-CIDS-MIB", "cidsAlertLogVictimPacketsAct"),
        ("CISCO-CIDS-MIB", "cidsAlertLogPairPacketsActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertRateLimitRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttackVictimPair"),
        ("CISCO-CIDS-MIB", "cidsAlertDeniedAttackSericePair"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackVicReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertDenyAttackSerReqNotPerf"),
        ("CISCO-CIDS-MIB", "cidsAlertThreatValueRating"),
        ("CISCO-CIDS-MIB", "cidsAlertRiskRatingTargetValue"),
        ("CISCO-CIDS-MIB", "cidsAlertRiskRatingRelevance"),
        ("CISCO-CIDS-MIB", "cidsAlertRiskRatingWatchList"))
)
if mibBuilder.loadTexts:
    ciscoCidsOptionalObjectGroupRev1.setStatus("current")

ciscoCidsOptionalObjectGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 10)
)
ciscoCidsOptionalObjectGroupRev2.setObjects(
      *(("CISCO-CIDS-MIB", "cidsAlertDenyPacket"),
        ("CISCO-CIDS-MIB", "cidsAlertBlockHost"),
        ("CISCO-CIDS-MIB", "cidsAlertTcpOneWayResetSent"))
)
if mibBuilder.loadTexts:
    ciscoCidsOptionalObjectGroupRev2.setStatus("current")

ciscoCidsAlertObjectGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 11)
)
ciscoCidsAlertObjectGroupRev2.setObjects(
      *(("CISCO-CIDS-MIB", "cidsAlertSignature"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureVersion"),
        ("CISCO-CIDS-MIB", "cidsAlertSummary"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryType"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryFinal"),
        ("CISCO-CIDS-MIB", "cidsAlertSummaryInitialAlert"),
        ("CISCO-CIDS-MIB", "cidsAlertVlan"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimContext"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerContext"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLoggingActivated"),
        ("CISCO-CIDS-MIB", "cidsAlertTcpResetSent"),
        ("CISCO-CIDS-MIB", "cidsAlertShunRequested"),
        ("CISCO-CIDS-MIB", "cidsAlertDetails"),
        ("CISCO-CIDS-MIB", "cidsAlertIpLogId"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseStatus"),
        ("CISCO-CIDS-MIB", "cidsThreatResponseSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertEventRiskRating"))
)
if mibBuilder.loadTexts:
    ciscoCidsAlertObjectGroupRev2.setStatus("current")

ciscoCidsHealthObjectGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 12)
)
ciscoCidsHealthObjectGroupRev1.setObjects(
      *(("CISCO-CIDS-MIB", "cidsHealthSecMonAvailability"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallHealth"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSoftwareVersion"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSignatureVersion"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonLicenseStatus"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonMainAppStatus"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonAnalysisEngineStatus"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonByPassMode"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonMissedPktPctAndThresh"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonAnalysisEngMemPercent"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSensorLoad"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonVirtSensorStatus"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonCollaborationAppStatus"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonTotalPartitionSpace"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonUtilizedPartitionSpace"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallAppColor"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSensorLoadColor"))
)
if mibBuilder.loadTexts:
    ciscoCidsHealthObjectGroupRev1.setStatus("current")

ciscoCidsOptionalObjectGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 13)
)
ciscoCidsOptionalObjectGroupRev3.setObjects(
    ("CISCO-CIDS-MIB", "cidsAlertVirtualSensor")
)
if mibBuilder.loadTexts:
    ciscoCidsOptionalObjectGroupRev3.setStatus("current")


# Notification objects

ciscoCidsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 0, 1)
)
ciscoCidsAlert.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsAlertSeverity"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigName"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertSignatureSubSigId"),
        ("CISCO-CIDS-MIB", "cidsAlertAlarmTraits"),
        ("CISCO-CIDS-MIB", "cidsAlertAttackerAddress"),
        ("CISCO-CIDS-MIB", "cidsAlertVictimAddress"))
)
if mibBuilder.loadTexts:
    ciscoCidsAlert.setStatus(
        "current"
    )

ciscoCidsError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 0, 2)
)
ciscoCidsError.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsErrorSeverity"),
        ("CISCO-CIDS-MIB", "cidsErrorName"),
        ("CISCO-CIDS-MIB", "cidsErrorMessage"))
)
if mibBuilder.loadTexts:
    ciscoCidsError.setStatus(
        "current"
    )

ciscoCidsHealthHeartBeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 0, 3)
)
ciscoCidsHealthHeartBeat.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallAppColor"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSensorLoadColor"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallHealth"))
)
if mibBuilder.loadTexts:
    ciscoCidsHealthHeartBeat.setStatus(
        "current"
    )

ciscoCidsHealthMetricChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 0, 4)
)
ciscoCidsHealthMetricChange.setObjects(
      *(("CISCO-CIDS-MIB", "cidsGeneralEventId"),
        ("CISCO-CIDS-MIB", "cidsGeneralOriginatorHostId"),
        ("CISCO-CIDS-MIB", "cidsGeneralLocalTime"),
        ("CISCO-CIDS-MIB", "cidsGeneralUTCTime"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallAppColor"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonSensorLoadColor"),
        ("CISCO-CIDS-MIB", "cidsHealthSecMonOverallHealth"))
)
if mibBuilder.loadTexts:
    ciscoCidsHealthMetricChange.setStatus(
        "current"
    )


# Notifications groups

ciscoCidsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 4)
)
ciscoCidsNotificationsGroup.setObjects(
      *(("CISCO-CIDS-MIB", "ciscoCidsAlert"),
        ("CISCO-CIDS-MIB", "ciscoCidsError"))
)
if mibBuilder.loadTexts:
    ciscoCidsNotificationsGroup.setStatus(
        "current"
    )

ciscoCidsNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 2, 14)
)
ciscoCidsNotificationsGroupRev1.setObjects(
      *(("CISCO-CIDS-MIB", "ciscoCidsHealthHeartBeat"),
        ("CISCO-CIDS-MIB", "ciscoCidsHealthMetricChange"))
)
if mibBuilder.loadTexts:
    ciscoCidsNotificationsGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCidsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCidsMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCidsMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCidsMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCidsMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCidsMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoCidsMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCidsMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoCidsMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 383, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoCidsMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CIDS-MIB",
    **{"CidsHealthStatusColor": CidsHealthStatusColor,
       "CidsApplicationStatus": CidsApplicationStatus,
       "CidsErrorCode": CidsErrorCode,
       "CidsTargetValue": CidsTargetValue,
       "CidsAttackRelevance": CidsAttackRelevance,
       "ciscoCidsMIB": ciscoCidsMIB,
       "ciscoCidsMIBNotifs": ciscoCidsMIBNotifs,
       "ciscoCidsAlert": ciscoCidsAlert,
       "ciscoCidsError": ciscoCidsError,
       "ciscoCidsHealthHeartBeat": ciscoCidsHealthHeartBeat,
       "ciscoCidsHealthMetricChange": ciscoCidsHealthMetricChange,
       "ciscoCidsMIBObjects": ciscoCidsMIBObjects,
       "cidsGeneral": cidsGeneral,
       "cidsGeneralEventId": cidsGeneralEventId,
       "cidsGeneralLocalTime": cidsGeneralLocalTime,
       "cidsGeneralUTCTime": cidsGeneralUTCTime,
       "cidsGeneralOriginatorHostId": cidsGeneralOriginatorHostId,
       "cidsGeneralOriginatorAppName": cidsGeneralOriginatorAppName,
       "cidsGeneralOriginatorAppId": cidsGeneralOriginatorAppId,
       "cidsNotificationsEnabled": cidsNotificationsEnabled,
       "cidsAlert": cidsAlert,
       "cidsAlertSeverity": cidsAlertSeverity,
       "cidsAlertAlarmTraits": cidsAlertAlarmTraits,
       "cidsAlertSignature": cidsAlertSignature,
       "cidsAlertSignatureSigName": cidsAlertSignatureSigName,
       "cidsAlertSignatureSigId": cidsAlertSignatureSigId,
       "cidsAlertSignatureSubSigId": cidsAlertSignatureSubSigId,
       "cidsAlertSignatureVersion": cidsAlertSignatureVersion,
       "cidsAlertSummary": cidsAlertSummary,
       "cidsAlertSummaryType": cidsAlertSummaryType,
       "cidsAlertSummaryFinal": cidsAlertSummaryFinal,
       "cidsAlertSummaryInitialAlert": cidsAlertSummaryInitialAlert,
       "cidsAlertInterfaceGroup": cidsAlertInterfaceGroup,
       "cidsAlertVlan": cidsAlertVlan,
       "cidsAlertVictimContext": cidsAlertVictimContext,
       "cidsAlertAttackerContext": cidsAlertAttackerContext,
       "cidsAlertAttackerAddress": cidsAlertAttackerAddress,
       "cidsAlertVictimAddress": cidsAlertVictimAddress,
       "cidsAlertIpLoggingActivated": cidsAlertIpLoggingActivated,
       "cidsAlertTcpResetSent": cidsAlertTcpResetSent,
       "cidsAlertShunRequested": cidsAlertShunRequested,
       "cidsAlertDetails": cidsAlertDetails,
       "cidsAlertIpLogId": cidsAlertIpLogId,
       "cidsThreatResponseStatus": cidsThreatResponseStatus,
       "cidsThreatResponseSeverity": cidsThreatResponseSeverity,
       "cidsAlertEventRiskRating": cidsAlertEventRiskRating,
       "cidsAlertIfIndex": cidsAlertIfIndex,
       "cidsAlertProtocol": cidsAlertProtocol,
       "cidsAlertDeniedAttacker": cidsAlertDeniedAttacker,
       "cidsAlertDeniedFlow": cidsAlertDeniedFlow,
       "cidsAlertDenyPacketReqNotPerf": cidsAlertDenyPacketReqNotPerf,
       "cidsAlertDenyFlowReqNotPerf": cidsAlertDenyFlowReqNotPerf,
       "cidsAlertDenyAttackerReqNotPerf": cidsAlertDenyAttackerReqNotPerf,
       "cidsAlertBlockConnectionReq": cidsAlertBlockConnectionReq,
       "cidsAlertLogAttackerPacketsAct": cidsAlertLogAttackerPacketsAct,
       "cidsAlertLogVictimPacketsAct": cidsAlertLogVictimPacketsAct,
       "cidsAlertLogPairPacketsActivated": cidsAlertLogPairPacketsActivated,
       "cidsAlertRateLimitRequested": cidsAlertRateLimitRequested,
       "cidsAlertDeniedAttackVictimPair": cidsAlertDeniedAttackVictimPair,
       "cidsAlertDeniedAttackSericePair": cidsAlertDeniedAttackSericePair,
       "cidsAlertDenyAttackVicReqNotPerf": cidsAlertDenyAttackVicReqNotPerf,
       "cidsAlertDenyAttackSerReqNotPerf": cidsAlertDenyAttackSerReqNotPerf,
       "cidsAlertThreatValueRating": cidsAlertThreatValueRating,
       "cidsAlertRiskRatingTargetValue": cidsAlertRiskRatingTargetValue,
       "cidsAlertRiskRatingRelevance": cidsAlertRiskRatingRelevance,
       "cidsAlertRiskRatingWatchList": cidsAlertRiskRatingWatchList,
       "cidsAlertDenyPacket": cidsAlertDenyPacket,
       "cidsAlertBlockHost": cidsAlertBlockHost,
       "cidsAlertTcpOneWayResetSent": cidsAlertTcpOneWayResetSent,
       "cidsAlertVirtualSensor": cidsAlertVirtualSensor,
       "cidsError": cidsError,
       "cidsErrorSeverity": cidsErrorSeverity,
       "cidsErrorName": cidsErrorName,
       "cidsErrorMessage": cidsErrorMessage,
       "cidsHealth": cidsHealth,
       "cidsHealthPacketLoss": cidsHealthPacketLoss,
       "cidsHealthPacketDenialRate": cidsHealthPacketDenialRate,
       "cidsHealthAlarmsGenerated": cidsHealthAlarmsGenerated,
       "cidsHealthFragmentsInFRU": cidsHealthFragmentsInFRU,
       "cidsHealthDatagramsInFRU": cidsHealthDatagramsInFRU,
       "cidsHealthTcpEmbryonicStreams": cidsHealthTcpEmbryonicStreams,
       "cidsHealthTCPEstablishedStreams": cidsHealthTCPEstablishedStreams,
       "cidsHealthTcpClosingStreams": cidsHealthTcpClosingStreams,
       "cidsHealthTcpStreams": cidsHealthTcpStreams,
       "cidsHealthActiveNodes": cidsHealthActiveNodes,
       "cidsHealthTcpDualIpAndPorts": cidsHealthTcpDualIpAndPorts,
       "cidsHealthUdpDualIpAndPorts": cidsHealthUdpDualIpAndPorts,
       "cidsHealthIpDualIp": cidsHealthIpDualIp,
       "cidsHealthIsSensorMemoryCritical": cidsHealthIsSensorMemoryCritical,
       "cidsHealthIsSensorActive": cidsHealthIsSensorActive,
       "cidsHealthCommandAndControlPort": cidsHealthCommandAndControlPort,
       "cidsHealthSensorStatsResetTime": cidsHealthSensorStatsResetTime,
       "cidsHealthSecMonAvailability": cidsHealthSecMonAvailability,
       "cidsHealthSecMonOverallHealth": cidsHealthSecMonOverallHealth,
       "cidsHealthSecMonSoftwareVersion": cidsHealthSecMonSoftwareVersion,
       "cidsHealthSecMonSignatureVersion": cidsHealthSecMonSignatureVersion,
       "cidsHealthSecMonLicenseStatus": cidsHealthSecMonLicenseStatus,
       "cidsHealthSecMonOverallAppColor": cidsHealthSecMonOverallAppColor,
       "cidsHealthSecMonMainAppStatus": cidsHealthSecMonMainAppStatus,
       "cidsHealthSecMonAnalysisEngineStatus": cidsHealthSecMonAnalysisEngineStatus,
       "cidsHealthSecMonCollaborationAppStatus": cidsHealthSecMonCollaborationAppStatus,
       "cidsHealthSecMonByPassMode": cidsHealthSecMonByPassMode,
       "cidsHealthSecMonMissedPktPctAndThresh": cidsHealthSecMonMissedPktPctAndThresh,
       "cidsHealthSecMonAnalysisEngMemPercent": cidsHealthSecMonAnalysisEngMemPercent,
       "cidsHealthSecMonSensorLoad": cidsHealthSecMonSensorLoad,
       "cidsHealthSecMonSensorLoadColor": cidsHealthSecMonSensorLoadColor,
       "cidsHealthSecMonVirtSensorStatusTable": cidsHealthSecMonVirtSensorStatusTable,
       "cidsHealthSecMonVirtSensorStatusEntry": cidsHealthSecMonVirtSensorStatusEntry,
       "cidsHealthSecMonVirtSensorName": cidsHealthSecMonVirtSensorName,
       "cidsHealthSecMonVirtSensorStatus": cidsHealthSecMonVirtSensorStatus,
       "cidsHealthSecMonDataStorageTable": cidsHealthSecMonDataStorageTable,
       "cidsHealthSecMonDataStorageEntry": cidsHealthSecMonDataStorageEntry,
       "cidsHealthSecMonPartitionName": cidsHealthSecMonPartitionName,
       "cidsHealthSecMonTotalPartitionSpace": cidsHealthSecMonTotalPartitionSpace,
       "cidsHealthSecMonUtilizedPartitionSpace": cidsHealthSecMonUtilizedPartitionSpace,
       "ciscoCidsMIBConform": ciscoCidsMIBConform,
       "ciscoCidsMIBCompliances": ciscoCidsMIBCompliances,
       "ciscoCidsMIBCompliance": ciscoCidsMIBCompliance,
       "ciscoCidsMIBComplianceRev1": ciscoCidsMIBComplianceRev1,
       "ciscoCidsMIBComplianceRev2": ciscoCidsMIBComplianceRev2,
       "ciscoCidsMIBComplianceRev3": ciscoCidsMIBComplianceRev3,
       "ciscoCidsMIBComplianceRev4": ciscoCidsMIBComplianceRev4,
       "ciscoCidsMIBGroups": ciscoCidsMIBGroups,
       "ciscoCidsGeneralObjectGroup": ciscoCidsGeneralObjectGroup,
       "ciscoCidsAlertObjectGroup": ciscoCidsAlertObjectGroup,
       "ciscoCidsErrorObjectGroup": ciscoCidsErrorObjectGroup,
       "ciscoCidsNotificationsGroup": ciscoCidsNotificationsGroup,
       "ciscoCidsHealthObjectGroup": ciscoCidsHealthObjectGroup,
       "ciscoCidsGeneralObjectGroupRev1": ciscoCidsGeneralObjectGroupRev1,
       "ciscoCidsAlertObjectGroupRev1": ciscoCidsAlertObjectGroupRev1,
       "ciscoCidsOptionalObjectGroup": ciscoCidsOptionalObjectGroup,
       "ciscoCidsOptionalObjectGroupRev1": ciscoCidsOptionalObjectGroupRev1,
       "ciscoCidsOptionalObjectGroupRev2": ciscoCidsOptionalObjectGroupRev2,
       "ciscoCidsAlertObjectGroupRev2": ciscoCidsAlertObjectGroupRev2,
       "ciscoCidsHealthObjectGroupRev1": ciscoCidsHealthObjectGroupRev1,
       "ciscoCidsOptionalObjectGroupRev3": ciscoCidsOptionalObjectGroupRev3,
       "ciscoCidsNotificationsGroupRev1": ciscoCidsNotificationsGroupRev1}
)
