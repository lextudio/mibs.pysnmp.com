# SNMP MIB module (CISCO-LWAPP-DOT11-CCX-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-CCX-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:20 2024
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

(ciscoLwappDot11ClientCcxMIBObjects,
 cldcClientMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "ciscoLwappDot11ClientCcxMIBObjects",
    "cldcClientMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoMilliSeconds,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoMilliSeconds")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11CcxClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3)
)
ciscoLwappDot11CcxClientMIB.setRevisions(
        ("2006-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CcxEventLogResponseStatus(Integer32, TextualConvention):
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
        *(("ccx-event-log-incapable", 3),
          ("ccx-event-log-refused", 2),
          ("ccx-event-log-successful", 1))
    )



class CcxEventLogDialogToken(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11CcxClientMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11CcxClientMIBObjects = _CiscoLwappDot11CcxClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0)
)
_CiscoClientCcxEventLogRequest_ObjectIdentity = ObjectIdentity
ciscoClientCcxEventLogRequest = _CiscoClientCcxEventLogRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 1)
)
_CldccEventLogsRequestTable_Object = MibTable
cldccEventLogsRequestTable = _CldccEventLogsRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 1, 1)
)
if mibBuilder.loadTexts:
    cldccEventLogsRequestTable.setStatus("current")
_CldccEventLogsRequestEntry_Object = MibTableRow
cldccEventLogsRequestEntry = _CldccEventLogsRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 1, 1, 1)
)
cldccEventLogsRequestEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccEventLogsRequestEntry.setStatus("current")


class _CldccEventLogsRequestLogType_Type(Bits):
    """Custom type cldccEventLogsRequestLogType based on Bits"""
    namedValues = NamedValues(
        *(("roaming", 0),
          ("rsna", 1),
          ("syslog", 2))
    )

_CldccEventLogsRequestLogType_Type.__name__ = "Bits"
_CldccEventLogsRequestLogType_Object = MibTableColumn
cldccEventLogsRequestLogType = _CldccEventLogsRequestLogType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 1, 1, 1, 1),
    _CldccEventLogsRequestLogType_Type()
)
cldccEventLogsRequestLogType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccEventLogsRequestLogType.setStatus("current")
_CldccEventLogsRequestRowStatus_Type = RowStatus
_CldccEventLogsRequestRowStatus_Object = MibTableColumn
cldccEventLogsRequestRowStatus = _CldccEventLogsRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 1, 1, 1, 2),
    _CldccEventLogsRequestRowStatus_Type()
)
cldccEventLogsRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccEventLogsRequestRowStatus.setStatus("current")
_CiscoClientCcxEventLogResponse_ObjectIdentity = ObjectIdentity
ciscoClientCcxEventLogResponse = _CiscoClientCcxEventLogResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2)
)
_CldccSysLogsTable_Object = MibTable
cldccSysLogsTable = _CldccSysLogsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 1)
)
if mibBuilder.loadTexts:
    cldccSysLogsTable.setStatus("current")
_CldccSysLogsEntry_Object = MibTableRow
cldccSysLogsEntry = _CldccSysLogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 1, 1)
)
cldccSysLogsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CCX-CLIENT-MIB", "cldccSysLogsIndex"),
)
if mibBuilder.loadTexts:
    cldccSysLogsEntry.setStatus("current")
_CldccSysLogsIndex_Type = Unsigned32
_CldccSysLogsIndex_Object = MibTableColumn
cldccSysLogsIndex = _CldccSysLogsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 1, 1, 1),
    _CldccSysLogsIndex_Type()
)
cldccSysLogsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccSysLogsIndex.setStatus("current")
_CldccSysLogsTimeStamp_Type = TimeStamp
_CldccSysLogsTimeStamp_Object = MibTableColumn
cldccSysLogsTimeStamp = _CldccSysLogsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 1, 1, 3),
    _CldccSysLogsTimeStamp_Type()
)
cldccSysLogsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccSysLogsTimeStamp.setStatus("current")


class _CldccSysLogsBuffer_Type(OctetString):
    """Custom type cldccSysLogsBuffer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_CldccSysLogsBuffer_Type.__name__ = "OctetString"
_CldccSysLogsBuffer_Object = MibTableColumn
cldccSysLogsBuffer = _CldccSysLogsBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 1, 1, 4),
    _CldccSysLogsBuffer_Type()
)
cldccSysLogsBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccSysLogsBuffer.setStatus("current")
_CldccRoamingLogsTable_Object = MibTable
cldccRoamingLogsTable = _CldccRoamingLogsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2)
)
if mibBuilder.loadTexts:
    cldccRoamingLogsTable.setStatus("current")
_CldccRoamingLogsEntry_Object = MibTableRow
cldccRoamingLogsEntry = _CldccRoamingLogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1)
)
cldccRoamingLogsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CCX-CLIENT-MIB", "cldccRoamingLogsIndex"),
)
if mibBuilder.loadTexts:
    cldccRoamingLogsEntry.setStatus("current")
_CldccRoamingLogsIndex_Type = Unsigned32
_CldccRoamingLogsIndex_Object = MibTableColumn
cldccRoamingLogsIndex = _CldccRoamingLogsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 1),
    _CldccRoamingLogsIndex_Type()
)
cldccRoamingLogsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsIndex.setStatus("current")
_CldccRoamingLogsTimeStamp_Type = TimeStamp
_CldccRoamingLogsTimeStamp_Object = MibTableColumn
cldccRoamingLogsTimeStamp = _CldccRoamingLogsTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 2),
    _CldccRoamingLogsTimeStamp_Type()
)
cldccRoamingLogsTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsTimeStamp.setStatus("current")
_CldccRoamingLogsTargetSSID_Type = MacAddress
_CldccRoamingLogsTargetSSID_Object = MibTableColumn
cldccRoamingLogsTargetSSID = _CldccRoamingLogsTargetSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 3),
    _CldccRoamingLogsTargetSSID_Type()
)
cldccRoamingLogsTargetSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsTargetSSID.setStatus("current")
_CldccRoamingLogsSourceSSID_Type = MacAddress
_CldccRoamingLogsSourceSSID_Object = MibTableColumn
cldccRoamingLogsSourceSSID = _CldccRoamingLogsSourceSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 4),
    _CldccRoamingLogsSourceSSID_Type()
)
cldccRoamingLogsSourceSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsSourceSSID.setStatus("current")
_CldccRoamingLogsTransitionTime_Type = CiscoMilliSeconds
_CldccRoamingLogsTransitionTime_Object = MibTableColumn
cldccRoamingLogsTransitionTime = _CldccRoamingLogsTransitionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 5),
    _CldccRoamingLogsTransitionTime_Type()
)
cldccRoamingLogsTransitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsTransitionTime.setStatus("current")


class _CldccRoamingLogsTransitionReason_Type(Integer32):
    """Custom type cldccRoamingLogsTransitionReason based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("disassociated-or-deauthenticated", 9),
          ("excessive-interference", 16),
          ("failed-8021x-4way-handshake", 11),
          ("failed-8021x-eap-auth", 10),
          ("first-association-to-wlan", 5),
          ("inf-directed-roam", 4),
          ("insufficient-capacity", 3),
          ("many-broadcast-deauth", 18),
          ("many-broadcast-disassociations", 17),
          ("many-data-mic-failures", 13),
          ("many-mgt-mic-failures", 14),
          ("many-replay-counters", 12),
          ("max-retransmissions-excedded", 15),
          ("normal-roam-better-ap", 8),
          ("normal-roam-load-bal", 2),
          ("normal-roam-poor-link", 1),
          ("roaming-from-cellular", 6),
          ("roaming-to-cellular", 7))
    )


_CldccRoamingLogsTransitionReason_Type.__name__ = "Integer32"
_CldccRoamingLogsTransitionReason_Object = MibTableColumn
cldccRoamingLogsTransitionReason = _CldccRoamingLogsTransitionReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 6),
    _CldccRoamingLogsTransitionReason_Type()
)
cldccRoamingLogsTransitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsTransitionReason.setStatus("current")


class _CldccRoamingLogsTransitionResult_Type(Integer32):
    """Custom type cldccRoamingLogsTransitionResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 51),
    )


_CldccRoamingLogsTransitionResult_Type.__name__ = "Integer32"
_CldccRoamingLogsTransitionResult_Object = MibTableColumn
cldccRoamingLogsTransitionResult = _CldccRoamingLogsTransitionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 2, 1, 7),
    _CldccRoamingLogsTransitionResult_Type()
)
cldccRoamingLogsTransitionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsTransitionResult.setStatus("current")
_CldccRsnaDataTable_Object = MibTable
cldccRsnaDataTable = _CldccRsnaDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3)
)
if mibBuilder.loadTexts:
    cldccRsnaDataTable.setStatus("current")
_CldccRsnaDataEntry_Object = MibTableRow
cldccRsnaDataEntry = _CldccRsnaDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1)
)
cldccRsnaDataEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
    (0, "CISCO-LWAPP-DOT11-CCX-CLIENT-MIB", "cldccRsnaDataIndex"),
)
if mibBuilder.loadTexts:
    cldccRsnaDataEntry.setStatus("current")
_CldccRsnaDataIndex_Type = Unsigned32
_CldccRsnaDataIndex_Object = MibTableColumn
cldccRsnaDataIndex = _CldccRsnaDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 1),
    _CldccRsnaDataIndex_Type()
)
cldccRsnaDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldccRsnaDataIndex.setStatus("current")
_CldccRsnaDataTimeStamp_Type = TimeStamp
_CldccRsnaDataTimeStamp_Object = MibTableColumn
cldccRsnaDataTimeStamp = _CldccRsnaDataTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 2),
    _CldccRsnaDataTimeStamp_Type()
)
cldccRsnaDataTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataTimeStamp.setStatus("current")
_CldccRsnaDataVersion_Type = Unsigned32
_CldccRsnaDataVersion_Object = MibTableColumn
cldccRsnaDataVersion = _CldccRsnaDataVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 3),
    _CldccRsnaDataVersion_Type()
)
cldccRsnaDataVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataVersion.setStatus("current")
_CldccRsnaDataTargetSSID_Type = MacAddress
_CldccRsnaDataTargetSSID_Object = MibTableColumn
cldccRsnaDataTargetSSID = _CldccRsnaDataTargetSSID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 4),
    _CldccRsnaDataTargetSSID_Type()
)
cldccRsnaDataTargetSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataTargetSSID.setStatus("current")


class _CldccRsnaDataAuthType_Type(Integer32):
    """Custom type cldccRsnaDataAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ccx-dot1x-eap-fast", 1),
          ("ccx-dot1x-eap-md5", 6),
          ("ccx-dot1x-eap-sim", 7),
          ("ccx-dot1x-eap-tls", 2),
          ("ccx-dot1x-eap-ttls", 3),
          ("ccx-dot1x-leap", 0),
          ("ccx-dot1x-peap-v0", 4),
          ("ccx-dot1x-peap-v1", 5),
          ("ccx-dot1x-psk", 8),
          ("ccx-dot1x-unknown", 255))
    )


_CldccRsnaDataAuthType_Type.__name__ = "Integer32"
_CldccRsnaDataAuthType_Object = MibTableColumn
cldccRsnaDataAuthType = _CldccRsnaDataAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 5),
    _CldccRsnaDataAuthType_Type()
)
cldccRsnaDataAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataAuthType.setStatus("current")


class _CldccRsnaDataResult_Type(Integer32):
    """Custom type cldccRsnaDataResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CldccRsnaDataResult_Type.__name__ = "Integer32"
_CldccRsnaDataResult_Object = MibTableColumn
cldccRsnaDataResult = _CldccRsnaDataResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 6),
    _CldccRsnaDataResult_Type()
)
cldccRsnaDataResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataResult.setStatus("current")


class _CldccRsnaDataElemMultiCastOuis_Type(OctetString):
    """Custom type cldccRsnaDataElemMultiCastOuis based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CldccRsnaDataElemMultiCastOuis_Type.__name__ = "OctetString"
_CldccRsnaDataElemMultiCastOuis_Object = MibTableColumn
cldccRsnaDataElemMultiCastOuis = _CldccRsnaDataElemMultiCastOuis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 7),
    _CldccRsnaDataElemMultiCastOuis_Type()
)
cldccRsnaDataElemMultiCastOuis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataElemMultiCastOuis.setStatus("current")


class _CldccRsnaDataElemUnicastCastOuis_Type(OctetString):
    """Custom type cldccRsnaDataElemUnicastCastOuis based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CldccRsnaDataElemUnicastCastOuis_Type.__name__ = "OctetString"
_CldccRsnaDataElemUnicastCastOuis_Object = MibTableColumn
cldccRsnaDataElemUnicastCastOuis = _CldccRsnaDataElemUnicastCastOuis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 8),
    _CldccRsnaDataElemUnicastCastOuis_Type()
)
cldccRsnaDataElemUnicastCastOuis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataElemUnicastCastOuis.setStatus("current")


class _CldccRsnaDataElemAuthOuis_Type(OctetString):
    """Custom type cldccRsnaDataElemAuthOuis based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CldccRsnaDataElemAuthOuis_Type.__name__ = "OctetString"
_CldccRsnaDataElemAuthOuis_Object = MibTableColumn
cldccRsnaDataElemAuthOuis = _CldccRsnaDataElemAuthOuis_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 9),
    _CldccRsnaDataElemAuthOuis_Type()
)
cldccRsnaDataElemAuthOuis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataElemAuthOuis.setStatus("current")
_CldccRsnaDataElemCapabilities_Type = Unsigned32
_CldccRsnaDataElemCapabilities_Object = MibTableColumn
cldccRsnaDataElemCapabilities = _CldccRsnaDataElemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 2, 3, 1, 10),
    _CldccRsnaDataElemCapabilities_Type()
)
cldccRsnaDataElemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaDataElemCapabilities.setStatus("current")
_CiscoClientCcxEventLogStatus_ObjectIdentity = ObjectIdentity
ciscoClientCcxEventLogStatus = _CiscoClientCcxEventLogStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3)
)
_CldccEventLogStatusTable_Object = MibTable
cldccEventLogStatusTable = _CldccEventLogStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3, 1)
)
if mibBuilder.loadTexts:
    cldccEventLogStatusTable.setStatus("current")
_CldccEventLogStatusEntry_Object = MibTableRow
cldccEventLogStatusEntry = _CldccEventLogStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3, 1, 1)
)
cldccEventLogStatusEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccEventLogStatusEntry.setStatus("current")
_CldccRoamingLogsResponseStatus_Type = CcxEventLogResponseStatus
_CldccRoamingLogsResponseStatus_Object = MibTableColumn
cldccRoamingLogsResponseStatus = _CldccRoamingLogsResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3, 1, 1, 1),
    _CldccRoamingLogsResponseStatus_Type()
)
cldccRoamingLogsResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRoamingLogsResponseStatus.setStatus("current")
_CldccRsnaLogsResponseStatus_Type = CcxEventLogResponseStatus
_CldccRsnaLogsResponseStatus_Object = MibTableColumn
cldccRsnaLogsResponseStatus = _CldccRsnaLogsResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3, 1, 1, 2),
    _CldccRsnaLogsResponseStatus_Type()
)
cldccRsnaLogsResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccRsnaLogsResponseStatus.setStatus("current")
_CldccSysLogsResponseStatus_Type = CcxEventLogResponseStatus
_CldccSysLogsResponseStatus_Object = MibTableColumn
cldccSysLogsResponseStatus = _CldccSysLogsResponseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 3, 1, 1, 3),
    _CldccSysLogsResponseStatus_Type()
)
cldccSysLogsResponseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccSysLogsResponseStatus.setStatus("current")
_CiscoClientCcxStatsRequest_ObjectIdentity = ObjectIdentity
ciscoClientCcxStatsRequest = _CiscoClientCcxStatsRequest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4)
)
_CldccStatsReqTable_Object = MibTable
cldccStatsReqTable = _CldccStatsReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1)
)
if mibBuilder.loadTexts:
    cldccStatsReqTable.setStatus("current")
_CldccStatsReqEntry_Object = MibTableRow
cldccStatsReqEntry = _CldccStatsReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1, 1)
)
cldccStatsReqEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccStatsReqEntry.setStatus("current")


class _CldccStatsReqStatus_Type(Integer32):
    """Custom type cldccStatsReqStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("incapable", 0),
          ("inprogress", 5),
          ("invalid-state", 2),
          ("refused", 1),
          ("success", 4))
    )


_CldccStatsReqStatus_Type.__name__ = "Integer32"
_CldccStatsReqStatus_Object = MibTableColumn
cldccStatsReqStatus = _CldccStatsReqStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1, 1, 1),
    _CldccStatsReqStatus_Type()
)
cldccStatsReqStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccStatsReqStatus.setStatus("current")


class _CldccStatsReqGroupId_Type(Integer32):
    """Custom type cldccStatsReqGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dot11-meas", 0),
          ("security-meas", 1))
    )


_CldccStatsReqGroupId_Type.__name__ = "Integer32"
_CldccStatsReqGroupId_Object = MibTableColumn
cldccStatsReqGroupId = _CldccStatsReqGroupId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1, 1, 2),
    _CldccStatsReqGroupId_Type()
)
cldccStatsReqGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccStatsReqGroupId.setStatus("current")
_CldccStatsReqDuration_Type = CiscoMilliSeconds
_CldccStatsReqDuration_Object = MibTableColumn
cldccStatsReqDuration = _CldccStatsReqDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1, 1, 3),
    _CldccStatsReqDuration_Type()
)
cldccStatsReqDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldccStatsReqDuration.setStatus("current")
_CldccStatsReqRowStatus_Type = RowStatus
_CldccStatsReqRowStatus_Object = MibTableColumn
cldccStatsReqRowStatus = _CldccStatsReqRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 4, 1, 1, 4),
    _CldccStatsReqRowStatus_Type()
)
cldccStatsReqRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cldccStatsReqRowStatus.setStatus("current")
_CiscoClientCcxStatsResponse_ObjectIdentity = ObjectIdentity
ciscoClientCcxStatsResponse = _CiscoClientCcxStatsResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5)
)
_CldccStatsDot11RespTable_Object = MibTable
cldccStatsDot11RespTable = _CldccStatsDot11RespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1)
)
if mibBuilder.loadTexts:
    cldccStatsDot11RespTable.setStatus("current")
_CldccStatsDot11RespEntry_Object = MibTableRow
cldccStatsDot11RespEntry = _CldccStatsDot11RespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1)
)
cldccStatsDot11RespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccStatsDot11RespEntry.setStatus("current")
_CldccStatsRespTransmittedFragmentCount_Type = Counter32
_CldccStatsRespTransmittedFragmentCount_Object = MibTableColumn
cldccStatsRespTransmittedFragmentCount = _CldccStatsRespTransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 1),
    _CldccStatsRespTransmittedFragmentCount_Type()
)
cldccStatsRespTransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespTransmittedFragmentCount.setStatus("current")
_CldccStatsRespMulticastTransmittedFrameCount_Type = Counter32
_CldccStatsRespMulticastTransmittedFrameCount_Object = MibTableColumn
cldccStatsRespMulticastTransmittedFrameCount = _CldccStatsRespMulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 2),
    _CldccStatsRespMulticastTransmittedFrameCount_Type()
)
cldccStatsRespMulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMulticastTransmittedFrameCount.setStatus("current")
_CldccStatsRespFailedCount_Type = Counter32
_CldccStatsRespFailedCount_Object = MibTableColumn
cldccStatsRespFailedCount = _CldccStatsRespFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 3),
    _CldccStatsRespFailedCount_Type()
)
cldccStatsRespFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespFailedCount.setStatus("current")
_CldccStatsRespRetryCount_Type = Counter32
_CldccStatsRespRetryCount_Object = MibTableColumn
cldccStatsRespRetryCount = _CldccStatsRespRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 4),
    _CldccStatsRespRetryCount_Type()
)
cldccStatsRespRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespRetryCount.setStatus("current")
_CldccStatsRespMultipleRetryCount_Type = Counter32
_CldccStatsRespMultipleRetryCount_Object = MibTableColumn
cldccStatsRespMultipleRetryCount = _CldccStatsRespMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 5),
    _CldccStatsRespMultipleRetryCount_Type()
)
cldccStatsRespMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMultipleRetryCount.setStatus("current")
_CldccStatsRespFrameDuplicateCount_Type = Counter32
_CldccStatsRespFrameDuplicateCount_Object = MibTableColumn
cldccStatsRespFrameDuplicateCount = _CldccStatsRespFrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 6),
    _CldccStatsRespFrameDuplicateCount_Type()
)
cldccStatsRespFrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespFrameDuplicateCount.setStatus("current")
_CldccStatsRespRtsSuccessCount_Type = Counter32
_CldccStatsRespRtsSuccessCount_Object = MibTableColumn
cldccStatsRespRtsSuccessCount = _CldccStatsRespRtsSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 7),
    _CldccStatsRespRtsSuccessCount_Type()
)
cldccStatsRespRtsSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespRtsSuccessCount.setStatus("current")
_CldccStatsRespRtsFailureCount_Type = Counter32
_CldccStatsRespRtsFailureCount_Object = MibTableColumn
cldccStatsRespRtsFailureCount = _CldccStatsRespRtsFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 8),
    _CldccStatsRespRtsFailureCount_Type()
)
cldccStatsRespRtsFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespRtsFailureCount.setStatus("current")
_CldccStatsRespAckFailureCount_Type = Counter32
_CldccStatsRespAckFailureCount_Object = MibTableColumn
cldccStatsRespAckFailureCount = _CldccStatsRespAckFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 9),
    _CldccStatsRespAckFailureCount_Type()
)
cldccStatsRespAckFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespAckFailureCount.setStatus("current")
_CldccStatsRespReceivedFragmentCount_Type = Counter32
_CldccStatsRespReceivedFragmentCount_Object = MibTableColumn
cldccStatsRespReceivedFragmentCount = _CldccStatsRespReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 10),
    _CldccStatsRespReceivedFragmentCount_Type()
)
cldccStatsRespReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespReceivedFragmentCount.setStatus("current")
_CldccStatsRespMulticastReceivedFrameCount_Type = Counter32
_CldccStatsRespMulticastReceivedFrameCount_Object = MibTableColumn
cldccStatsRespMulticastReceivedFrameCount = _CldccStatsRespMulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 11),
    _CldccStatsRespMulticastReceivedFrameCount_Type()
)
cldccStatsRespMulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMulticastReceivedFrameCount.setStatus("current")
_CldccStatsRespFcsErrorCount_Type = Counter32
_CldccStatsRespFcsErrorCount_Object = MibTableColumn
cldccStatsRespFcsErrorCount = _CldccStatsRespFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 12),
    _CldccStatsRespFcsErrorCount_Type()
)
cldccStatsRespFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespFcsErrorCount.setStatus("current")
_CldccStatsRespTransmittedFrameCount_Type = Counter32
_CldccStatsRespTransmittedFrameCount_Object = MibTableColumn
cldccStatsRespTransmittedFrameCount = _CldccStatsRespTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 1, 1, 13),
    _CldccStatsRespTransmittedFrameCount_Type()
)
cldccStatsRespTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespTransmittedFrameCount.setStatus("current")
_CldccStatsSecurityRespTable_Object = MibTable
cldccStatsSecurityRespTable = _CldccStatsSecurityRespTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2)
)
if mibBuilder.loadTexts:
    cldccStatsSecurityRespTable.setStatus("current")
_CldccStatsSecurityRespEntry_Object = MibTableRow
cldccStatsSecurityRespEntry = _CldccStatsSecurityRespEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1)
)
cldccStatsSecurityRespEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cldccStatsSecurityRespEntry.setStatus("current")
_CldccStatsRespSelectedPairwiseCipher_Type = Unsigned32
_CldccStatsRespSelectedPairwiseCipher_Object = MibTableColumn
cldccStatsRespSelectedPairwiseCipher = _CldccStatsRespSelectedPairwiseCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 1),
    _CldccStatsRespSelectedPairwiseCipher_Type()
)
cldccStatsRespSelectedPairwiseCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespSelectedPairwiseCipher.setStatus("current")
_CldccStatsRespTkipIcvErrors_Type = Counter32
_CldccStatsRespTkipIcvErrors_Object = MibTableColumn
cldccStatsRespTkipIcvErrors = _CldccStatsRespTkipIcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 2),
    _CldccStatsRespTkipIcvErrors_Type()
)
cldccStatsRespTkipIcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespTkipIcvErrors.setStatus("current")
_CldccStatsRespTkipLocalMicFailures_Type = Counter32
_CldccStatsRespTkipLocalMicFailures_Object = MibTableColumn
cldccStatsRespTkipLocalMicFailures = _CldccStatsRespTkipLocalMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 3),
    _CldccStatsRespTkipLocalMicFailures_Type()
)
cldccStatsRespTkipLocalMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespTkipLocalMicFailures.setStatus("current")
_CldccStatsRespCcmpReplays_Type = Counter32
_CldccStatsRespCcmpReplays_Object = MibTableColumn
cldccStatsRespCcmpReplays = _CldccStatsRespCcmpReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 4),
    _CldccStatsRespCcmpReplays_Type()
)
cldccStatsRespCcmpReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespCcmpReplays.setStatus("current")
_CldccStatsRespCcmpDecrypErrors_Type = Counter32
_CldccStatsRespCcmpDecrypErrors_Object = MibTableColumn
cldccStatsRespCcmpDecrypErrors = _CldccStatsRespCcmpDecrypErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 5),
    _CldccStatsRespCcmpDecrypErrors_Type()
)
cldccStatsRespCcmpDecrypErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespCcmpDecrypErrors.setStatus("current")
_CldccStatsRespTkipReplays_Type = Counter32
_CldccStatsRespTkipReplays_Object = MibTableColumn
cldccStatsRespTkipReplays = _CldccStatsRespTkipReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 6),
    _CldccStatsRespTkipReplays_Type()
)
cldccStatsRespTkipReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespTkipReplays.setStatus("current")
_CldccStatsRespMgmtStatsTkipIcvErrors_Type = Counter32
_CldccStatsRespMgmtStatsTkipIcvErrors_Object = MibTableColumn
cldccStatsRespMgmtStatsTkipIcvErrors = _CldccStatsRespMgmtStatsTkipIcvErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 7),
    _CldccStatsRespMgmtStatsTkipIcvErrors_Type()
)
cldccStatsRespMgmtStatsTkipIcvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsTkipIcvErrors.setStatus("current")
_CldccStatsRespMgmtStatsTkipLocalMicFailures_Type = Counter32
_CldccStatsRespMgmtStatsTkipLocalMicFailures_Object = MibTableColumn
cldccStatsRespMgmtStatsTkipLocalMicFailures = _CldccStatsRespMgmtStatsTkipLocalMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 8),
    _CldccStatsRespMgmtStatsTkipLocalMicFailures_Type()
)
cldccStatsRespMgmtStatsTkipLocalMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsTkipLocalMicFailures.setStatus("current")
_CldccStatsRespMgmtStatsCcmpReplays_Type = Counter32
_CldccStatsRespMgmtStatsCcmpReplays_Object = MibTableColumn
cldccStatsRespMgmtStatsCcmpReplays = _CldccStatsRespMgmtStatsCcmpReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 9),
    _CldccStatsRespMgmtStatsCcmpReplays_Type()
)
cldccStatsRespMgmtStatsCcmpReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsCcmpReplays.setStatus("current")
_CldccStatsRespMgmtStatsCcmpDecryptErrors_Type = Counter32
_CldccStatsRespMgmtStatsCcmpDecryptErrors_Object = MibTableColumn
cldccStatsRespMgmtStatsCcmpDecryptErrors = _CldccStatsRespMgmtStatsCcmpDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 10),
    _CldccStatsRespMgmtStatsCcmpDecryptErrors_Type()
)
cldccStatsRespMgmtStatsCcmpDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsCcmpDecryptErrors.setStatus("current")
_CldccStatsRespMgmtStatsTkipReplays_Type = Counter32
_CldccStatsRespMgmtStatsTkipReplays_Object = MibTableColumn
cldccStatsRespMgmtStatsTkipReplays = _CldccStatsRespMgmtStatsTkipReplays_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 11),
    _CldccStatsRespMgmtStatsTkipReplays_Type()
)
cldccStatsRespMgmtStatsTkipReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsTkipReplays.setStatus("current")
_CldccStatsRespMgmtStatsTkipMhdrErrors_Type = Counter32
_CldccStatsRespMgmtStatsTkipMhdrErrors_Object = MibTableColumn
cldccStatsRespMgmtStatsTkipMhdrErrors = _CldccStatsRespMgmtStatsTkipMhdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 12),
    _CldccStatsRespMgmtStatsTkipMhdrErrors_Type()
)
cldccStatsRespMgmtStatsTkipMhdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsTkipMhdrErrors.setStatus("current")
_CldccStatsRespMgmtStatsCcmpMhdrErrors_Type = Counter32
_CldccStatsRespMgmtStatsCcmpMhdrErrors_Object = MibTableColumn
cldccStatsRespMgmtStatsCcmpMhdrErrors = _CldccStatsRespMgmtStatsCcmpMhdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 13),
    _CldccStatsRespMgmtStatsCcmpMhdrErrors_Type()
)
cldccStatsRespMgmtStatsCcmpMhdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsCcmpMhdrErrors.setStatus("current")
_CldccStatsRespMgmtStatsBroadcastDisassociateCount_Type = Counter32
_CldccStatsRespMgmtStatsBroadcastDisassociateCount_Object = MibTableColumn
cldccStatsRespMgmtStatsBroadcastDisassociateCount = _CldccStatsRespMgmtStatsBroadcastDisassociateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 14),
    _CldccStatsRespMgmtStatsBroadcastDisassociateCount_Type()
)
cldccStatsRespMgmtStatsBroadcastDisassociateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsBroadcastDisassociateCount.setStatus("current")
_CldccStatsRespMgmtStatsBroadcastDeauthenticateCount_Type = Counter32
_CldccStatsRespMgmtStatsBroadcastDeauthenticateCount_Object = MibTableColumn
cldccStatsRespMgmtStatsBroadcastDeauthenticateCount = _CldccStatsRespMgmtStatsBroadcastDeauthenticateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 15),
    _CldccStatsRespMgmtStatsBroadcastDeauthenticateCount_Type()
)
cldccStatsRespMgmtStatsBroadcastDeauthenticateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsBroadcastDeauthenticateCount.setStatus("current")
_CldccStatsRespMgmtStatsBroadcastActionFrameCount_Type = Counter32
_CldccStatsRespMgmtStatsBroadcastActionFrameCount_Object = MibTableColumn
cldccStatsRespMgmtStatsBroadcastActionFrameCount = _CldccStatsRespMgmtStatsBroadcastActionFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 599, 3, 3, 0, 5, 2, 1, 16),
    _CldccStatsRespMgmtStatsBroadcastActionFrameCount_Type()
)
cldccStatsRespMgmtStatsBroadcastActionFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldccStatsRespMgmtStatsBroadcastActionFrameCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-CCX-CLIENT-MIB",
    **{"CcxEventLogResponseStatus": CcxEventLogResponseStatus,
       "CcxEventLogDialogToken": CcxEventLogDialogToken,
       "ciscoLwappDot11CcxClientMIB": ciscoLwappDot11CcxClientMIB,
       "ciscoLwappDot11CcxClientMIBObjects": ciscoLwappDot11CcxClientMIBObjects,
       "ciscoClientCcxEventLogRequest": ciscoClientCcxEventLogRequest,
       "cldccEventLogsRequestTable": cldccEventLogsRequestTable,
       "cldccEventLogsRequestEntry": cldccEventLogsRequestEntry,
       "cldccEventLogsRequestLogType": cldccEventLogsRequestLogType,
       "cldccEventLogsRequestRowStatus": cldccEventLogsRequestRowStatus,
       "ciscoClientCcxEventLogResponse": ciscoClientCcxEventLogResponse,
       "cldccSysLogsTable": cldccSysLogsTable,
       "cldccSysLogsEntry": cldccSysLogsEntry,
       "cldccSysLogsIndex": cldccSysLogsIndex,
       "cldccSysLogsTimeStamp": cldccSysLogsTimeStamp,
       "cldccSysLogsBuffer": cldccSysLogsBuffer,
       "cldccRoamingLogsTable": cldccRoamingLogsTable,
       "cldccRoamingLogsEntry": cldccRoamingLogsEntry,
       "cldccRoamingLogsIndex": cldccRoamingLogsIndex,
       "cldccRoamingLogsTimeStamp": cldccRoamingLogsTimeStamp,
       "cldccRoamingLogsTargetSSID": cldccRoamingLogsTargetSSID,
       "cldccRoamingLogsSourceSSID": cldccRoamingLogsSourceSSID,
       "cldccRoamingLogsTransitionTime": cldccRoamingLogsTransitionTime,
       "cldccRoamingLogsTransitionReason": cldccRoamingLogsTransitionReason,
       "cldccRoamingLogsTransitionResult": cldccRoamingLogsTransitionResult,
       "cldccRsnaDataTable": cldccRsnaDataTable,
       "cldccRsnaDataEntry": cldccRsnaDataEntry,
       "cldccRsnaDataIndex": cldccRsnaDataIndex,
       "cldccRsnaDataTimeStamp": cldccRsnaDataTimeStamp,
       "cldccRsnaDataVersion": cldccRsnaDataVersion,
       "cldccRsnaDataTargetSSID": cldccRsnaDataTargetSSID,
       "cldccRsnaDataAuthType": cldccRsnaDataAuthType,
       "cldccRsnaDataResult": cldccRsnaDataResult,
       "cldccRsnaDataElemMultiCastOuis": cldccRsnaDataElemMultiCastOuis,
       "cldccRsnaDataElemUnicastCastOuis": cldccRsnaDataElemUnicastCastOuis,
       "cldccRsnaDataElemAuthOuis": cldccRsnaDataElemAuthOuis,
       "cldccRsnaDataElemCapabilities": cldccRsnaDataElemCapabilities,
       "ciscoClientCcxEventLogStatus": ciscoClientCcxEventLogStatus,
       "cldccEventLogStatusTable": cldccEventLogStatusTable,
       "cldccEventLogStatusEntry": cldccEventLogStatusEntry,
       "cldccRoamingLogsResponseStatus": cldccRoamingLogsResponseStatus,
       "cldccRsnaLogsResponseStatus": cldccRsnaLogsResponseStatus,
       "cldccSysLogsResponseStatus": cldccSysLogsResponseStatus,
       "ciscoClientCcxStatsRequest": ciscoClientCcxStatsRequest,
       "cldccStatsReqTable": cldccStatsReqTable,
       "cldccStatsReqEntry": cldccStatsReqEntry,
       "cldccStatsReqStatus": cldccStatsReqStatus,
       "cldccStatsReqGroupId": cldccStatsReqGroupId,
       "cldccStatsReqDuration": cldccStatsReqDuration,
       "cldccStatsReqRowStatus": cldccStatsReqRowStatus,
       "ciscoClientCcxStatsResponse": ciscoClientCcxStatsResponse,
       "cldccStatsDot11RespTable": cldccStatsDot11RespTable,
       "cldccStatsDot11RespEntry": cldccStatsDot11RespEntry,
       "cldccStatsRespTransmittedFragmentCount": cldccStatsRespTransmittedFragmentCount,
       "cldccStatsRespMulticastTransmittedFrameCount": cldccStatsRespMulticastTransmittedFrameCount,
       "cldccStatsRespFailedCount": cldccStatsRespFailedCount,
       "cldccStatsRespRetryCount": cldccStatsRespRetryCount,
       "cldccStatsRespMultipleRetryCount": cldccStatsRespMultipleRetryCount,
       "cldccStatsRespFrameDuplicateCount": cldccStatsRespFrameDuplicateCount,
       "cldccStatsRespRtsSuccessCount": cldccStatsRespRtsSuccessCount,
       "cldccStatsRespRtsFailureCount": cldccStatsRespRtsFailureCount,
       "cldccStatsRespAckFailureCount": cldccStatsRespAckFailureCount,
       "cldccStatsRespReceivedFragmentCount": cldccStatsRespReceivedFragmentCount,
       "cldccStatsRespMulticastReceivedFrameCount": cldccStatsRespMulticastReceivedFrameCount,
       "cldccStatsRespFcsErrorCount": cldccStatsRespFcsErrorCount,
       "cldccStatsRespTransmittedFrameCount": cldccStatsRespTransmittedFrameCount,
       "cldccStatsSecurityRespTable": cldccStatsSecurityRespTable,
       "cldccStatsSecurityRespEntry": cldccStatsSecurityRespEntry,
       "cldccStatsRespSelectedPairwiseCipher": cldccStatsRespSelectedPairwiseCipher,
       "cldccStatsRespTkipIcvErrors": cldccStatsRespTkipIcvErrors,
       "cldccStatsRespTkipLocalMicFailures": cldccStatsRespTkipLocalMicFailures,
       "cldccStatsRespCcmpReplays": cldccStatsRespCcmpReplays,
       "cldccStatsRespCcmpDecrypErrors": cldccStatsRespCcmpDecrypErrors,
       "cldccStatsRespTkipReplays": cldccStatsRespTkipReplays,
       "cldccStatsRespMgmtStatsTkipIcvErrors": cldccStatsRespMgmtStatsTkipIcvErrors,
       "cldccStatsRespMgmtStatsTkipLocalMicFailures": cldccStatsRespMgmtStatsTkipLocalMicFailures,
       "cldccStatsRespMgmtStatsCcmpReplays": cldccStatsRespMgmtStatsCcmpReplays,
       "cldccStatsRespMgmtStatsCcmpDecryptErrors": cldccStatsRespMgmtStatsCcmpDecryptErrors,
       "cldccStatsRespMgmtStatsTkipReplays": cldccStatsRespMgmtStatsTkipReplays,
       "cldccStatsRespMgmtStatsTkipMhdrErrors": cldccStatsRespMgmtStatsTkipMhdrErrors,
       "cldccStatsRespMgmtStatsCcmpMhdrErrors": cldccStatsRespMgmtStatsCcmpMhdrErrors,
       "cldccStatsRespMgmtStatsBroadcastDisassociateCount": cldccStatsRespMgmtStatsBroadcastDisassociateCount,
       "cldccStatsRespMgmtStatsBroadcastDeauthenticateCount": cldccStatsRespMgmtStatsBroadcastDeauthenticateCount,
       "cldccStatsRespMgmtStatsBroadcastActionFrameCount": cldccStatsRespMgmtStatsBroadcastActionFrameCount}
)
