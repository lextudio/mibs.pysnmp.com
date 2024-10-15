# SNMP MIB module (CISCO-UNIFIED-COMPUTING-COMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-COMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:09 2024
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

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsAaaConfigState,
 CucsCommAdminState,
 CucsCommChannel,
 CucsCommCipherSuiteMode,
 CucsCommDnsProviderAdminState,
 CucsCommHttpRedirectState,
 CucsCommNtpProviderAdminState,
 CucsCommProtocol,
 CucsCommShellProto,
 CucsCommSmashCLPProto,
 CucsCommSnmpAuth,
 CucsCommSnmpConfigState,
 CucsCommSnmpNotificationType,
 CucsCommSnmpProto,
 CucsCommSnmpV3Privilege,
 CucsCommSnmpVersion,
 CucsCommSshAdminState,
 CucsCommSvcEpFsmCurrentFsm,
 CucsCommSvcEpFsmStageName,
 CucsCommSvcEpFsmTaskFlags,
 CucsCommSvcEpFsmTaskItem,
 CucsCommSyslogAdminState,
 CucsCommSyslogClientEnum,
 CucsCommSyslogFileSize,
 CucsCommSyslogForwardingFacility,
 CucsCommSyslogProto,
 CucsCommSyslogRestrictedSeverity,
 CucsCommSyslogSeverity,
 CucsCommSyslogSourceAudits,
 CucsCommSyslogSourceEvents,
 CucsCommSyslogSourceFaults,
 CucsCommTimeZoneConfigState,
 CucsCommWebProto,
 CucsCommXmlClConnPolicyClientType,
 CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFsmStageStatus,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAaaConfigState",
    "CucsCommAdminState",
    "CucsCommChannel",
    "CucsCommCipherSuiteMode",
    "CucsCommDnsProviderAdminState",
    "CucsCommHttpRedirectState",
    "CucsCommNtpProviderAdminState",
    "CucsCommProtocol",
    "CucsCommShellProto",
    "CucsCommSmashCLPProto",
    "CucsCommSnmpAuth",
    "CucsCommSnmpConfigState",
    "CucsCommSnmpNotificationType",
    "CucsCommSnmpProto",
    "CucsCommSnmpV3Privilege",
    "CucsCommSnmpVersion",
    "CucsCommSshAdminState",
    "CucsCommSvcEpFsmCurrentFsm",
    "CucsCommSvcEpFsmStageName",
    "CucsCommSvcEpFsmTaskFlags",
    "CucsCommSvcEpFsmTaskItem",
    "CucsCommSyslogAdminState",
    "CucsCommSyslogClientEnum",
    "CucsCommSyslogFileSize",
    "CucsCommSyslogForwardingFacility",
    "CucsCommSyslogProto",
    "CucsCommSyslogRestrictedSeverity",
    "CucsCommSyslogSeverity",
    "CucsCommSyslogSourceAudits",
    "CucsCommSyslogSourceEvents",
    "CucsCommSyslogSourceFaults",
    "CucsCommTimeZoneConfigState",
    "CucsCommWebProto",
    "CucsCommXmlClConnPolicyClientType",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFsmStageStatus",
    "CucsPolicyPolicyOwner")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsCommObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsCommCimxmlTable_Object = MibTable
cucsCommCimxmlTable = _CucsCommCimxmlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cucsCommCimxmlTable.setStatus("current")
_CucsCommCimxmlEntry_Object = MibTableRow
cucsCommCimxmlEntry = _CucsCommCimxmlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1)
)
cucsCommCimxmlEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommCimxmlInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommCimxmlEntry.setStatus("current")
_CucsCommCimxmlInstanceId_Type = CucsManagedObjectId
_CucsCommCimxmlInstanceId_Object = MibTableColumn
cucsCommCimxmlInstanceId = _CucsCommCimxmlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 1),
    _CucsCommCimxmlInstanceId_Type()
)
cucsCommCimxmlInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommCimxmlInstanceId.setStatus("current")
_CucsCommCimxmlDn_Type = CucsManagedObjectDn
_CucsCommCimxmlDn_Object = MibTableColumn
cucsCommCimxmlDn = _CucsCommCimxmlDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 2),
    _CucsCommCimxmlDn_Type()
)
cucsCommCimxmlDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlDn.setStatus("current")
_CucsCommCimxmlRn_Type = SnmpAdminString
_CucsCommCimxmlRn_Object = MibTableColumn
cucsCommCimxmlRn = _CucsCommCimxmlRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 3),
    _CucsCommCimxmlRn_Type()
)
cucsCommCimxmlRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlRn.setStatus("current")
_CucsCommCimxmlAdminState_Type = CucsCommAdminState
_CucsCommCimxmlAdminState_Object = MibTableColumn
cucsCommCimxmlAdminState = _CucsCommCimxmlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 4),
    _CucsCommCimxmlAdminState_Type()
)
cucsCommCimxmlAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlAdminState.setStatus("current")
_CucsCommCimxmlDescr_Type = SnmpAdminString
_CucsCommCimxmlDescr_Object = MibTableColumn
cucsCommCimxmlDescr = _CucsCommCimxmlDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 5),
    _CucsCommCimxmlDescr_Type()
)
cucsCommCimxmlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlDescr.setStatus("current")
_CucsCommCimxmlIntId_Type = SnmpAdminString
_CucsCommCimxmlIntId_Object = MibTableColumn
cucsCommCimxmlIntId = _CucsCommCimxmlIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 6),
    _CucsCommCimxmlIntId_Type()
)
cucsCommCimxmlIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlIntId.setStatus("current")
_CucsCommCimxmlName_Type = SnmpAdminString
_CucsCommCimxmlName_Object = MibTableColumn
cucsCommCimxmlName = _CucsCommCimxmlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 7),
    _CucsCommCimxmlName_Type()
)
cucsCommCimxmlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlName.setStatus("current")
_CucsCommCimxmlPort_Type = Gauge32
_CucsCommCimxmlPort_Object = MibTableColumn
cucsCommCimxmlPort = _CucsCommCimxmlPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 8),
    _CucsCommCimxmlPort_Type()
)
cucsCommCimxmlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlPort.setStatus("current")
_CucsCommCimxmlProto_Type = CucsCommWebProto
_CucsCommCimxmlProto_Object = MibTableColumn
cucsCommCimxmlProto = _CucsCommCimxmlProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 9),
    _CucsCommCimxmlProto_Type()
)
cucsCommCimxmlProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlProto.setStatus("current")
_CucsCommCimxmlOperPort_Type = Gauge32
_CucsCommCimxmlOperPort_Object = MibTableColumn
cucsCommCimxmlOperPort = _CucsCommCimxmlOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 10),
    _CucsCommCimxmlOperPort_Type()
)
cucsCommCimxmlOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlOperPort.setStatus("current")
_CucsCommCimxmlPolicyLevel_Type = Gauge32
_CucsCommCimxmlPolicyLevel_Object = MibTableColumn
cucsCommCimxmlPolicyLevel = _CucsCommCimxmlPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 11),
    _CucsCommCimxmlPolicyLevel_Type()
)
cucsCommCimxmlPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlPolicyLevel.setStatus("current")
_CucsCommCimxmlPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommCimxmlPolicyOwner_Object = MibTableColumn
cucsCommCimxmlPolicyOwner = _CucsCommCimxmlPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 1, 1, 12),
    _CucsCommCimxmlPolicyOwner_Type()
)
cucsCommCimxmlPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimxmlPolicyOwner.setStatus("current")
_CucsCommDateTimeTable_Object = MibTable
cucsCommDateTimeTable = _CucsCommDateTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cucsCommDateTimeTable.setStatus("current")
_CucsCommDateTimeEntry_Object = MibTableRow
cucsCommDateTimeEntry = _CucsCommDateTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1)
)
cucsCommDateTimeEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommDateTimeInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommDateTimeEntry.setStatus("current")
_CucsCommDateTimeInstanceId_Type = CucsManagedObjectId
_CucsCommDateTimeInstanceId_Object = MibTableColumn
cucsCommDateTimeInstanceId = _CucsCommDateTimeInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 1),
    _CucsCommDateTimeInstanceId_Type()
)
cucsCommDateTimeInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommDateTimeInstanceId.setStatus("current")
_CucsCommDateTimeDn_Type = CucsManagedObjectDn
_CucsCommDateTimeDn_Object = MibTableColumn
cucsCommDateTimeDn = _CucsCommDateTimeDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 2),
    _CucsCommDateTimeDn_Type()
)
cucsCommDateTimeDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeDn.setStatus("current")
_CucsCommDateTimeRn_Type = SnmpAdminString
_CucsCommDateTimeRn_Object = MibTableColumn
cucsCommDateTimeRn = _CucsCommDateTimeRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 3),
    _CucsCommDateTimeRn_Type()
)
cucsCommDateTimeRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeRn.setStatus("current")
_CucsCommDateTimeAdminState_Type = CucsCommAdminState
_CucsCommDateTimeAdminState_Object = MibTableColumn
cucsCommDateTimeAdminState = _CucsCommDateTimeAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 4),
    _CucsCommDateTimeAdminState_Type()
)
cucsCommDateTimeAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeAdminState.setStatus("current")
_CucsCommDateTimeDate_Type = DateAndTime
_CucsCommDateTimeDate_Object = MibTableColumn
cucsCommDateTimeDate = _CucsCommDateTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 5),
    _CucsCommDateTimeDate_Type()
)
cucsCommDateTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeDate.setStatus("current")
_CucsCommDateTimeDescr_Type = SnmpAdminString
_CucsCommDateTimeDescr_Object = MibTableColumn
cucsCommDateTimeDescr = _CucsCommDateTimeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 6),
    _CucsCommDateTimeDescr_Type()
)
cucsCommDateTimeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeDescr.setStatus("current")
_CucsCommDateTimeIntId_Type = SnmpAdminString
_CucsCommDateTimeIntId_Object = MibTableColumn
cucsCommDateTimeIntId = _CucsCommDateTimeIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 7),
    _CucsCommDateTimeIntId_Type()
)
cucsCommDateTimeIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeIntId.setStatus("current")
_CucsCommDateTimeName_Type = SnmpAdminString
_CucsCommDateTimeName_Object = MibTableColumn
cucsCommDateTimeName = _CucsCommDateTimeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 8),
    _CucsCommDateTimeName_Type()
)
cucsCommDateTimeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeName.setStatus("current")
_CucsCommDateTimePort_Type = Gauge32
_CucsCommDateTimePort_Object = MibTableColumn
cucsCommDateTimePort = _CucsCommDateTimePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 9),
    _CucsCommDateTimePort_Type()
)
cucsCommDateTimePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimePort.setStatus("current")
_CucsCommDateTimeProto_Type = CucsCommProtocol
_CucsCommDateTimeProto_Object = MibTableColumn
cucsCommDateTimeProto = _CucsCommDateTimeProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 10),
    _CucsCommDateTimeProto_Type()
)
cucsCommDateTimeProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeProto.setStatus("current")
_CucsCommDateTimeTimezone_Type = SnmpAdminString
_CucsCommDateTimeTimezone_Object = MibTableColumn
cucsCommDateTimeTimezone = _CucsCommDateTimeTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 11),
    _CucsCommDateTimeTimezone_Type()
)
cucsCommDateTimeTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeTimezone.setStatus("current")
_CucsCommDateTimeConfigState_Type = CucsCommTimeZoneConfigState
_CucsCommDateTimeConfigState_Object = MibTableColumn
cucsCommDateTimeConfigState = _CucsCommDateTimeConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 12),
    _CucsCommDateTimeConfigState_Type()
)
cucsCommDateTimeConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeConfigState.setStatus("current")
_CucsCommDateTimeOperPort_Type = Gauge32
_CucsCommDateTimeOperPort_Object = MibTableColumn
cucsCommDateTimeOperPort = _CucsCommDateTimeOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 13),
    _CucsCommDateTimeOperPort_Type()
)
cucsCommDateTimeOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeOperPort.setStatus("current")
_CucsCommDateTimeOperTimezone_Type = SnmpAdminString
_CucsCommDateTimeOperTimezone_Object = MibTableColumn
cucsCommDateTimeOperTimezone = _CucsCommDateTimeOperTimezone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 14),
    _CucsCommDateTimeOperTimezone_Type()
)
cucsCommDateTimeOperTimezone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimeOperTimezone.setStatus("current")
_CucsCommDateTimePolicyLevel_Type = Gauge32
_CucsCommDateTimePolicyLevel_Object = MibTableColumn
cucsCommDateTimePolicyLevel = _CucsCommDateTimePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 15),
    _CucsCommDateTimePolicyLevel_Type()
)
cucsCommDateTimePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimePolicyLevel.setStatus("current")
_CucsCommDateTimePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommDateTimePolicyOwner_Object = MibTableColumn
cucsCommDateTimePolicyOwner = _CucsCommDateTimePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 2, 1, 16),
    _CucsCommDateTimePolicyOwner_Type()
)
cucsCommDateTimePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDateTimePolicyOwner.setStatus("current")
_CucsCommDnsTable_Object = MibTable
cucsCommDnsTable = _CucsCommDnsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3)
)
if mibBuilder.loadTexts:
    cucsCommDnsTable.setStatus("current")
_CucsCommDnsEntry_Object = MibTableRow
cucsCommDnsEntry = _CucsCommDnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1)
)
cucsCommDnsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommDnsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommDnsEntry.setStatus("current")
_CucsCommDnsInstanceId_Type = CucsManagedObjectId
_CucsCommDnsInstanceId_Object = MibTableColumn
cucsCommDnsInstanceId = _CucsCommDnsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 1),
    _CucsCommDnsInstanceId_Type()
)
cucsCommDnsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommDnsInstanceId.setStatus("current")
_CucsCommDnsDn_Type = CucsManagedObjectDn
_CucsCommDnsDn_Object = MibTableColumn
cucsCommDnsDn = _CucsCommDnsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 2),
    _CucsCommDnsDn_Type()
)
cucsCommDnsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsDn.setStatus("current")
_CucsCommDnsRn_Type = SnmpAdminString
_CucsCommDnsRn_Object = MibTableColumn
cucsCommDnsRn = _CucsCommDnsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 3),
    _CucsCommDnsRn_Type()
)
cucsCommDnsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsRn.setStatus("current")
_CucsCommDnsAdminState_Type = CucsCommAdminState
_CucsCommDnsAdminState_Object = MibTableColumn
cucsCommDnsAdminState = _CucsCommDnsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 4),
    _CucsCommDnsAdminState_Type()
)
cucsCommDnsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsAdminState.setStatus("current")
_CucsCommDnsDescr_Type = SnmpAdminString
_CucsCommDnsDescr_Object = MibTableColumn
cucsCommDnsDescr = _CucsCommDnsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 5),
    _CucsCommDnsDescr_Type()
)
cucsCommDnsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsDescr.setStatus("current")
_CucsCommDnsDomain_Type = SnmpAdminString
_CucsCommDnsDomain_Object = MibTableColumn
cucsCommDnsDomain = _CucsCommDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 6),
    _CucsCommDnsDomain_Type()
)
cucsCommDnsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsDomain.setStatus("current")
_CucsCommDnsIntId_Type = SnmpAdminString
_CucsCommDnsIntId_Object = MibTableColumn
cucsCommDnsIntId = _CucsCommDnsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 7),
    _CucsCommDnsIntId_Type()
)
cucsCommDnsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsIntId.setStatus("current")
_CucsCommDnsName_Type = SnmpAdminString
_CucsCommDnsName_Object = MibTableColumn
cucsCommDnsName = _CucsCommDnsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 8),
    _CucsCommDnsName_Type()
)
cucsCommDnsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsName.setStatus("current")
_CucsCommDnsPort_Type = Gauge32
_CucsCommDnsPort_Object = MibTableColumn
cucsCommDnsPort = _CucsCommDnsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 9),
    _CucsCommDnsPort_Type()
)
cucsCommDnsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsPort.setStatus("current")
_CucsCommDnsProto_Type = CucsCommProtocol
_CucsCommDnsProto_Object = MibTableColumn
cucsCommDnsProto = _CucsCommDnsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 10),
    _CucsCommDnsProto_Type()
)
cucsCommDnsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProto.setStatus("current")
_CucsCommDnsOperPort_Type = Gauge32
_CucsCommDnsOperPort_Object = MibTableColumn
cucsCommDnsOperPort = _CucsCommDnsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 11),
    _CucsCommDnsOperPort_Type()
)
cucsCommDnsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsOperPort.setStatus("current")
_CucsCommDnsPolicyLevel_Type = Gauge32
_CucsCommDnsPolicyLevel_Object = MibTableColumn
cucsCommDnsPolicyLevel = _CucsCommDnsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 12),
    _CucsCommDnsPolicyLevel_Type()
)
cucsCommDnsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsPolicyLevel.setStatus("current")
_CucsCommDnsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommDnsPolicyOwner_Object = MibTableColumn
cucsCommDnsPolicyOwner = _CucsCommDnsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 3, 1, 13),
    _CucsCommDnsPolicyOwner_Type()
)
cucsCommDnsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsPolicyOwner.setStatus("current")
_CucsCommDnsProviderTable_Object = MibTable
cucsCommDnsProviderTable = _CucsCommDnsProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4)
)
if mibBuilder.loadTexts:
    cucsCommDnsProviderTable.setStatus("current")
_CucsCommDnsProviderEntry_Object = MibTableRow
cucsCommDnsProviderEntry = _CucsCommDnsProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1)
)
cucsCommDnsProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommDnsProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommDnsProviderEntry.setStatus("current")
_CucsCommDnsProviderInstanceId_Type = CucsManagedObjectId
_CucsCommDnsProviderInstanceId_Object = MibTableColumn
cucsCommDnsProviderInstanceId = _CucsCommDnsProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 1),
    _CucsCommDnsProviderInstanceId_Type()
)
cucsCommDnsProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommDnsProviderInstanceId.setStatus("current")
_CucsCommDnsProviderDn_Type = CucsManagedObjectDn
_CucsCommDnsProviderDn_Object = MibTableColumn
cucsCommDnsProviderDn = _CucsCommDnsProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 2),
    _CucsCommDnsProviderDn_Type()
)
cucsCommDnsProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderDn.setStatus("current")
_CucsCommDnsProviderRn_Type = SnmpAdminString
_CucsCommDnsProviderRn_Object = MibTableColumn
cucsCommDnsProviderRn = _CucsCommDnsProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 3),
    _CucsCommDnsProviderRn_Type()
)
cucsCommDnsProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderRn.setStatus("current")
_CucsCommDnsProviderAdminState_Type = CucsCommDnsProviderAdminState
_CucsCommDnsProviderAdminState_Object = MibTableColumn
cucsCommDnsProviderAdminState = _CucsCommDnsProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 4),
    _CucsCommDnsProviderAdminState_Type()
)
cucsCommDnsProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderAdminState.setStatus("current")
_CucsCommDnsProviderDescr_Type = SnmpAdminString
_CucsCommDnsProviderDescr_Object = MibTableColumn
cucsCommDnsProviderDescr = _CucsCommDnsProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 5),
    _CucsCommDnsProviderDescr_Type()
)
cucsCommDnsProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderDescr.setStatus("current")
_CucsCommDnsProviderHostname_Type = SnmpAdminString
_CucsCommDnsProviderHostname_Object = MibTableColumn
cucsCommDnsProviderHostname = _CucsCommDnsProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 6),
    _CucsCommDnsProviderHostname_Type()
)
cucsCommDnsProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderHostname.setStatus("current")
_CucsCommDnsProviderName_Type = SnmpAdminString
_CucsCommDnsProviderName_Object = MibTableColumn
cucsCommDnsProviderName = _CucsCommDnsProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 4, 1, 8),
    _CucsCommDnsProviderName_Type()
)
cucsCommDnsProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommDnsProviderName.setStatus("current")
_CucsCommEvtChannelTable_Object = MibTable
cucsCommEvtChannelTable = _CucsCommEvtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5)
)
if mibBuilder.loadTexts:
    cucsCommEvtChannelTable.setStatus("current")
_CucsCommEvtChannelEntry_Object = MibTableRow
cucsCommEvtChannelEntry = _CucsCommEvtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1)
)
cucsCommEvtChannelEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommEvtChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommEvtChannelEntry.setStatus("current")
_CucsCommEvtChannelInstanceId_Type = CucsManagedObjectId
_CucsCommEvtChannelInstanceId_Object = MibTableColumn
cucsCommEvtChannelInstanceId = _CucsCommEvtChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 1),
    _CucsCommEvtChannelInstanceId_Type()
)
cucsCommEvtChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommEvtChannelInstanceId.setStatus("current")
_CucsCommEvtChannelDn_Type = CucsManagedObjectDn
_CucsCommEvtChannelDn_Object = MibTableColumn
cucsCommEvtChannelDn = _CucsCommEvtChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 2),
    _CucsCommEvtChannelDn_Type()
)
cucsCommEvtChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelDn.setStatus("current")
_CucsCommEvtChannelRn_Type = SnmpAdminString
_CucsCommEvtChannelRn_Object = MibTableColumn
cucsCommEvtChannelRn = _CucsCommEvtChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 3),
    _CucsCommEvtChannelRn_Type()
)
cucsCommEvtChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelRn.setStatus("current")
_CucsCommEvtChannelChannelState_Type = CucsCommChannel
_CucsCommEvtChannelChannelState_Object = MibTableColumn
cucsCommEvtChannelChannelState = _CucsCommEvtChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 4),
    _CucsCommEvtChannelChannelState_Type()
)
cucsCommEvtChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelChannelState.setStatus("current")
_CucsCommEvtChannelDescr_Type = SnmpAdminString
_CucsCommEvtChannelDescr_Object = MibTableColumn
cucsCommEvtChannelDescr = _CucsCommEvtChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 5),
    _CucsCommEvtChannelDescr_Type()
)
cucsCommEvtChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelDescr.setStatus("current")
_CucsCommEvtChannelIntId_Type = SnmpAdminString
_CucsCommEvtChannelIntId_Object = MibTableColumn
cucsCommEvtChannelIntId = _CucsCommEvtChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 6),
    _CucsCommEvtChannelIntId_Type()
)
cucsCommEvtChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelIntId.setStatus("current")
_CucsCommEvtChannelName_Type = SnmpAdminString
_CucsCommEvtChannelName_Object = MibTableColumn
cucsCommEvtChannelName = _CucsCommEvtChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 7),
    _CucsCommEvtChannelName_Type()
)
cucsCommEvtChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelName.setStatus("current")
_CucsCommEvtChannelPolicyLevel_Type = Gauge32
_CucsCommEvtChannelPolicyLevel_Object = MibTableColumn
cucsCommEvtChannelPolicyLevel = _CucsCommEvtChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 8),
    _CucsCommEvtChannelPolicyLevel_Type()
)
cucsCommEvtChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelPolicyLevel.setStatus("current")
_CucsCommEvtChannelPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommEvtChannelPolicyOwner_Object = MibTableColumn
cucsCommEvtChannelPolicyOwner = _CucsCommEvtChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 5, 1, 9),
    _CucsCommEvtChannelPolicyOwner_Type()
)
cucsCommEvtChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommEvtChannelPolicyOwner.setStatus("current")
_CucsCommHttpTable_Object = MibTable
cucsCommHttpTable = _CucsCommHttpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6)
)
if mibBuilder.loadTexts:
    cucsCommHttpTable.setStatus("current")
_CucsCommHttpEntry_Object = MibTableRow
cucsCommHttpEntry = _CucsCommHttpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1)
)
cucsCommHttpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommHttpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommHttpEntry.setStatus("current")
_CucsCommHttpInstanceId_Type = CucsManagedObjectId
_CucsCommHttpInstanceId_Object = MibTableColumn
cucsCommHttpInstanceId = _CucsCommHttpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 1),
    _CucsCommHttpInstanceId_Type()
)
cucsCommHttpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommHttpInstanceId.setStatus("current")
_CucsCommHttpDn_Type = CucsManagedObjectDn
_CucsCommHttpDn_Object = MibTableColumn
cucsCommHttpDn = _CucsCommHttpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 2),
    _CucsCommHttpDn_Type()
)
cucsCommHttpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpDn.setStatus("current")
_CucsCommHttpRn_Type = SnmpAdminString
_CucsCommHttpRn_Object = MibTableColumn
cucsCommHttpRn = _CucsCommHttpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 3),
    _CucsCommHttpRn_Type()
)
cucsCommHttpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpRn.setStatus("current")
_CucsCommHttpAdminState_Type = CucsCommAdminState
_CucsCommHttpAdminState_Object = MibTableColumn
cucsCommHttpAdminState = _CucsCommHttpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 4),
    _CucsCommHttpAdminState_Type()
)
cucsCommHttpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpAdminState.setStatus("current")
_CucsCommHttpDescr_Type = SnmpAdminString
_CucsCommHttpDescr_Object = MibTableColumn
cucsCommHttpDescr = _CucsCommHttpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 5),
    _CucsCommHttpDescr_Type()
)
cucsCommHttpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpDescr.setStatus("current")
_CucsCommHttpIntId_Type = SnmpAdminString
_CucsCommHttpIntId_Object = MibTableColumn
cucsCommHttpIntId = _CucsCommHttpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 6),
    _CucsCommHttpIntId_Type()
)
cucsCommHttpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpIntId.setStatus("current")
_CucsCommHttpName_Type = SnmpAdminString
_CucsCommHttpName_Object = MibTableColumn
cucsCommHttpName = _CucsCommHttpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 7),
    _CucsCommHttpName_Type()
)
cucsCommHttpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpName.setStatus("current")
_CucsCommHttpPort_Type = Gauge32
_CucsCommHttpPort_Object = MibTableColumn
cucsCommHttpPort = _CucsCommHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 8),
    _CucsCommHttpPort_Type()
)
cucsCommHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpPort.setStatus("current")
_CucsCommHttpProto_Type = CucsCommWebProto
_CucsCommHttpProto_Object = MibTableColumn
cucsCommHttpProto = _CucsCommHttpProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 9),
    _CucsCommHttpProto_Type()
)
cucsCommHttpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpProto.setStatus("current")
_CucsCommHttpRedirectState_Type = CucsCommHttpRedirectState
_CucsCommHttpRedirectState_Object = MibTableColumn
cucsCommHttpRedirectState = _CucsCommHttpRedirectState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 11),
    _CucsCommHttpRedirectState_Type()
)
cucsCommHttpRedirectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpRedirectState.setStatus("current")
_CucsCommHttpOperPort_Type = Gauge32
_CucsCommHttpOperPort_Object = MibTableColumn
cucsCommHttpOperPort = _CucsCommHttpOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 12),
    _CucsCommHttpOperPort_Type()
)
cucsCommHttpOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpOperPort.setStatus("current")
_CucsCommHttpPolicyLevel_Type = Gauge32
_CucsCommHttpPolicyLevel_Object = MibTableColumn
cucsCommHttpPolicyLevel = _CucsCommHttpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 13),
    _CucsCommHttpPolicyLevel_Type()
)
cucsCommHttpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpPolicyLevel.setStatus("current")
_CucsCommHttpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommHttpPolicyOwner_Object = MibTableColumn
cucsCommHttpPolicyOwner = _CucsCommHttpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 6, 1, 14),
    _CucsCommHttpPolicyOwner_Type()
)
cucsCommHttpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpPolicyOwner.setStatus("current")
_CucsCommHttpsTable_Object = MibTable
cucsCommHttpsTable = _CucsCommHttpsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7)
)
if mibBuilder.loadTexts:
    cucsCommHttpsTable.setStatus("current")
_CucsCommHttpsEntry_Object = MibTableRow
cucsCommHttpsEntry = _CucsCommHttpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1)
)
cucsCommHttpsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommHttpsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommHttpsEntry.setStatus("current")
_CucsCommHttpsInstanceId_Type = CucsManagedObjectId
_CucsCommHttpsInstanceId_Object = MibTableColumn
cucsCommHttpsInstanceId = _CucsCommHttpsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 1),
    _CucsCommHttpsInstanceId_Type()
)
cucsCommHttpsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommHttpsInstanceId.setStatus("current")
_CucsCommHttpsDn_Type = CucsManagedObjectDn
_CucsCommHttpsDn_Object = MibTableColumn
cucsCommHttpsDn = _CucsCommHttpsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 2),
    _CucsCommHttpsDn_Type()
)
cucsCommHttpsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsDn.setStatus("current")
_CucsCommHttpsRn_Type = SnmpAdminString
_CucsCommHttpsRn_Object = MibTableColumn
cucsCommHttpsRn = _CucsCommHttpsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 3),
    _CucsCommHttpsRn_Type()
)
cucsCommHttpsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsRn.setStatus("current")
_CucsCommHttpsAdminState_Type = CucsCommAdminState
_CucsCommHttpsAdminState_Object = MibTableColumn
cucsCommHttpsAdminState = _CucsCommHttpsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 4),
    _CucsCommHttpsAdminState_Type()
)
cucsCommHttpsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsAdminState.setStatus("current")
_CucsCommHttpsDescr_Type = SnmpAdminString
_CucsCommHttpsDescr_Object = MibTableColumn
cucsCommHttpsDescr = _CucsCommHttpsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 5),
    _CucsCommHttpsDescr_Type()
)
cucsCommHttpsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsDescr.setStatus("current")
_CucsCommHttpsIntId_Type = SnmpAdminString
_CucsCommHttpsIntId_Object = MibTableColumn
cucsCommHttpsIntId = _CucsCommHttpsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 6),
    _CucsCommHttpsIntId_Type()
)
cucsCommHttpsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsIntId.setStatus("current")
_CucsCommHttpsKeyRing_Type = SnmpAdminString
_CucsCommHttpsKeyRing_Object = MibTableColumn
cucsCommHttpsKeyRing = _CucsCommHttpsKeyRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 7),
    _CucsCommHttpsKeyRing_Type()
)
cucsCommHttpsKeyRing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsKeyRing.setStatus("current")
_CucsCommHttpsName_Type = SnmpAdminString
_CucsCommHttpsName_Object = MibTableColumn
cucsCommHttpsName = _CucsCommHttpsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 8),
    _CucsCommHttpsName_Type()
)
cucsCommHttpsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsName.setStatus("current")
_CucsCommHttpsPort_Type = Gauge32
_CucsCommHttpsPort_Object = MibTableColumn
cucsCommHttpsPort = _CucsCommHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 9),
    _CucsCommHttpsPort_Type()
)
cucsCommHttpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsPort.setStatus("current")
_CucsCommHttpsProto_Type = CucsCommWebProto
_CucsCommHttpsProto_Object = MibTableColumn
cucsCommHttpsProto = _CucsCommHttpsProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 10),
    _CucsCommHttpsProto_Type()
)
cucsCommHttpsProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsProto.setStatus("current")
_CucsCommHttpsCipherSuite_Type = SnmpAdminString
_CucsCommHttpsCipherSuite_Object = MibTableColumn
cucsCommHttpsCipherSuite = _CucsCommHttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 12),
    _CucsCommHttpsCipherSuite_Type()
)
cucsCommHttpsCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsCipherSuite.setStatus("current")
_CucsCommHttpsCipherSuiteMode_Type = CucsCommCipherSuiteMode
_CucsCommHttpsCipherSuiteMode_Object = MibTableColumn
cucsCommHttpsCipherSuiteMode = _CucsCommHttpsCipherSuiteMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 13),
    _CucsCommHttpsCipherSuiteMode_Type()
)
cucsCommHttpsCipherSuiteMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsCipherSuiteMode.setStatus("current")
_CucsCommHttpsOperPort_Type = Gauge32
_CucsCommHttpsOperPort_Object = MibTableColumn
cucsCommHttpsOperPort = _CucsCommHttpsOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 14),
    _CucsCommHttpsOperPort_Type()
)
cucsCommHttpsOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsOperPort.setStatus("current")
_CucsCommHttpsPolicyLevel_Type = Gauge32
_CucsCommHttpsPolicyLevel_Object = MibTableColumn
cucsCommHttpsPolicyLevel = _CucsCommHttpsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 15),
    _CucsCommHttpsPolicyLevel_Type()
)
cucsCommHttpsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsPolicyLevel.setStatus("current")
_CucsCommHttpsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommHttpsPolicyOwner_Object = MibTableColumn
cucsCommHttpsPolicyOwner = _CucsCommHttpsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 7, 1, 16),
    _CucsCommHttpsPolicyOwner_Type()
)
cucsCommHttpsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommHttpsPolicyOwner.setStatus("current")
_CucsCommNtpProviderTable_Object = MibTable
cucsCommNtpProviderTable = _CucsCommNtpProviderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8)
)
if mibBuilder.loadTexts:
    cucsCommNtpProviderTable.setStatus("current")
_CucsCommNtpProviderEntry_Object = MibTableRow
cucsCommNtpProviderEntry = _CucsCommNtpProviderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1)
)
cucsCommNtpProviderEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommNtpProviderInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommNtpProviderEntry.setStatus("current")
_CucsCommNtpProviderInstanceId_Type = CucsManagedObjectId
_CucsCommNtpProviderInstanceId_Object = MibTableColumn
cucsCommNtpProviderInstanceId = _CucsCommNtpProviderInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 1),
    _CucsCommNtpProviderInstanceId_Type()
)
cucsCommNtpProviderInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommNtpProviderInstanceId.setStatus("current")
_CucsCommNtpProviderDn_Type = CucsManagedObjectDn
_CucsCommNtpProviderDn_Object = MibTableColumn
cucsCommNtpProviderDn = _CucsCommNtpProviderDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 2),
    _CucsCommNtpProviderDn_Type()
)
cucsCommNtpProviderDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderDn.setStatus("current")
_CucsCommNtpProviderRn_Type = SnmpAdminString
_CucsCommNtpProviderRn_Object = MibTableColumn
cucsCommNtpProviderRn = _CucsCommNtpProviderRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 3),
    _CucsCommNtpProviderRn_Type()
)
cucsCommNtpProviderRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderRn.setStatus("current")
_CucsCommNtpProviderAdminState_Type = CucsCommNtpProviderAdminState
_CucsCommNtpProviderAdminState_Object = MibTableColumn
cucsCommNtpProviderAdminState = _CucsCommNtpProviderAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 4),
    _CucsCommNtpProviderAdminState_Type()
)
cucsCommNtpProviderAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderAdminState.setStatus("current")
_CucsCommNtpProviderDescr_Type = SnmpAdminString
_CucsCommNtpProviderDescr_Object = MibTableColumn
cucsCommNtpProviderDescr = _CucsCommNtpProviderDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 5),
    _CucsCommNtpProviderDescr_Type()
)
cucsCommNtpProviderDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderDescr.setStatus("current")
_CucsCommNtpProviderHostname_Type = SnmpAdminString
_CucsCommNtpProviderHostname_Object = MibTableColumn
cucsCommNtpProviderHostname = _CucsCommNtpProviderHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 6),
    _CucsCommNtpProviderHostname_Type()
)
cucsCommNtpProviderHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderHostname.setStatus("current")
_CucsCommNtpProviderName_Type = SnmpAdminString
_CucsCommNtpProviderName_Object = MibTableColumn
cucsCommNtpProviderName = _CucsCommNtpProviderName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 8, 1, 8),
    _CucsCommNtpProviderName_Type()
)
cucsCommNtpProviderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommNtpProviderName.setStatus("current")
_CucsCommSmashCLPTable_Object = MibTable
cucsCommSmashCLPTable = _CucsCommSmashCLPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9)
)
if mibBuilder.loadTexts:
    cucsCommSmashCLPTable.setStatus("current")
_CucsCommSmashCLPEntry_Object = MibTableRow
cucsCommSmashCLPEntry = _CucsCommSmashCLPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1)
)
cucsCommSmashCLPEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSmashCLPInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSmashCLPEntry.setStatus("current")
_CucsCommSmashCLPInstanceId_Type = CucsManagedObjectId
_CucsCommSmashCLPInstanceId_Object = MibTableColumn
cucsCommSmashCLPInstanceId = _CucsCommSmashCLPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 1),
    _CucsCommSmashCLPInstanceId_Type()
)
cucsCommSmashCLPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSmashCLPInstanceId.setStatus("current")
_CucsCommSmashCLPDn_Type = CucsManagedObjectDn
_CucsCommSmashCLPDn_Object = MibTableColumn
cucsCommSmashCLPDn = _CucsCommSmashCLPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 2),
    _CucsCommSmashCLPDn_Type()
)
cucsCommSmashCLPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPDn.setStatus("current")
_CucsCommSmashCLPRn_Type = SnmpAdminString
_CucsCommSmashCLPRn_Object = MibTableColumn
cucsCommSmashCLPRn = _CucsCommSmashCLPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 3),
    _CucsCommSmashCLPRn_Type()
)
cucsCommSmashCLPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPRn.setStatus("current")
_CucsCommSmashCLPAdminState_Type = CucsCommAdminState
_CucsCommSmashCLPAdminState_Object = MibTableColumn
cucsCommSmashCLPAdminState = _CucsCommSmashCLPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 4),
    _CucsCommSmashCLPAdminState_Type()
)
cucsCommSmashCLPAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPAdminState.setStatus("current")
_CucsCommSmashCLPDescr_Type = SnmpAdminString
_CucsCommSmashCLPDescr_Object = MibTableColumn
cucsCommSmashCLPDescr = _CucsCommSmashCLPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 5),
    _CucsCommSmashCLPDescr_Type()
)
cucsCommSmashCLPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPDescr.setStatus("current")
_CucsCommSmashCLPIntId_Type = SnmpAdminString
_CucsCommSmashCLPIntId_Object = MibTableColumn
cucsCommSmashCLPIntId = _CucsCommSmashCLPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 6),
    _CucsCommSmashCLPIntId_Type()
)
cucsCommSmashCLPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPIntId.setStatus("current")
_CucsCommSmashCLPName_Type = SnmpAdminString
_CucsCommSmashCLPName_Object = MibTableColumn
cucsCommSmashCLPName = _CucsCommSmashCLPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 7),
    _CucsCommSmashCLPName_Type()
)
cucsCommSmashCLPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPName.setStatus("current")
_CucsCommSmashCLPPort_Type = Gauge32
_CucsCommSmashCLPPort_Object = MibTableColumn
cucsCommSmashCLPPort = _CucsCommSmashCLPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 8),
    _CucsCommSmashCLPPort_Type()
)
cucsCommSmashCLPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPPort.setStatus("current")
_CucsCommSmashCLPProto_Type = CucsCommSmashCLPProto
_CucsCommSmashCLPProto_Object = MibTableColumn
cucsCommSmashCLPProto = _CucsCommSmashCLPProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 9),
    _CucsCommSmashCLPProto_Type()
)
cucsCommSmashCLPProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPProto.setStatus("current")
_CucsCommSmashCLPOperPort_Type = Gauge32
_CucsCommSmashCLPOperPort_Object = MibTableColumn
cucsCommSmashCLPOperPort = _CucsCommSmashCLPOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 10),
    _CucsCommSmashCLPOperPort_Type()
)
cucsCommSmashCLPOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPOperPort.setStatus("current")
_CucsCommSmashCLPPolicyLevel_Type = Gauge32
_CucsCommSmashCLPPolicyLevel_Object = MibTableColumn
cucsCommSmashCLPPolicyLevel = _CucsCommSmashCLPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 11),
    _CucsCommSmashCLPPolicyLevel_Type()
)
cucsCommSmashCLPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPPolicyLevel.setStatus("current")
_CucsCommSmashCLPPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSmashCLPPolicyOwner_Object = MibTableColumn
cucsCommSmashCLPPolicyOwner = _CucsCommSmashCLPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 9, 1, 12),
    _CucsCommSmashCLPPolicyOwner_Type()
)
cucsCommSmashCLPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSmashCLPPolicyOwner.setStatus("current")
_CucsCommSnmpTable_Object = MibTable
cucsCommSnmpTable = _CucsCommSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10)
)
if mibBuilder.loadTexts:
    cucsCommSnmpTable.setStatus("current")
_CucsCommSnmpEntry_Object = MibTableRow
cucsCommSnmpEntry = _CucsCommSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1)
)
cucsCommSnmpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSnmpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSnmpEntry.setStatus("current")
_CucsCommSnmpInstanceId_Type = CucsManagedObjectId
_CucsCommSnmpInstanceId_Object = MibTableColumn
cucsCommSnmpInstanceId = _CucsCommSnmpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 1),
    _CucsCommSnmpInstanceId_Type()
)
cucsCommSnmpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSnmpInstanceId.setStatus("current")
_CucsCommSnmpDn_Type = CucsManagedObjectDn
_CucsCommSnmpDn_Object = MibTableColumn
cucsCommSnmpDn = _CucsCommSnmpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 2),
    _CucsCommSnmpDn_Type()
)
cucsCommSnmpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpDn.setStatus("current")
_CucsCommSnmpRn_Type = SnmpAdminString
_CucsCommSnmpRn_Object = MibTableColumn
cucsCommSnmpRn = _CucsCommSnmpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 3),
    _CucsCommSnmpRn_Type()
)
cucsCommSnmpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpRn.setStatus("current")
_CucsCommSnmpAdminState_Type = CucsCommAdminState
_CucsCommSnmpAdminState_Object = MibTableColumn
cucsCommSnmpAdminState = _CucsCommSnmpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 4),
    _CucsCommSnmpAdminState_Type()
)
cucsCommSnmpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpAdminState.setStatus("current")
_CucsCommSnmpCommunity_Type = SnmpAdminString
_CucsCommSnmpCommunity_Object = MibTableColumn
cucsCommSnmpCommunity = _CucsCommSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 5),
    _CucsCommSnmpCommunity_Type()
)
cucsCommSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpCommunity.setStatus("current")
_CucsCommSnmpDescr_Type = SnmpAdminString
_CucsCommSnmpDescr_Object = MibTableColumn
cucsCommSnmpDescr = _CucsCommSnmpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 6),
    _CucsCommSnmpDescr_Type()
)
cucsCommSnmpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpDescr.setStatus("current")
_CucsCommSnmpIntId_Type = SnmpAdminString
_CucsCommSnmpIntId_Object = MibTableColumn
cucsCommSnmpIntId = _CucsCommSnmpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 7),
    _CucsCommSnmpIntId_Type()
)
cucsCommSnmpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpIntId.setStatus("current")
_CucsCommSnmpName_Type = SnmpAdminString
_CucsCommSnmpName_Object = MibTableColumn
cucsCommSnmpName = _CucsCommSnmpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 8),
    _CucsCommSnmpName_Type()
)
cucsCommSnmpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpName.setStatus("current")
_CucsCommSnmpPort_Type = Gauge32
_CucsCommSnmpPort_Object = MibTableColumn
cucsCommSnmpPort = _CucsCommSnmpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 9),
    _CucsCommSnmpPort_Type()
)
cucsCommSnmpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpPort.setStatus("current")
_CucsCommSnmpProto_Type = CucsCommSnmpProto
_CucsCommSnmpProto_Object = MibTableColumn
cucsCommSnmpProto = _CucsCommSnmpProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 10),
    _CucsCommSnmpProto_Type()
)
cucsCommSnmpProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpProto.setStatus("current")
_CucsCommSnmpSysContact_Type = SnmpAdminString
_CucsCommSnmpSysContact_Object = MibTableColumn
cucsCommSnmpSysContact = _CucsCommSnmpSysContact_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 11),
    _CucsCommSnmpSysContact_Type()
)
cucsCommSnmpSysContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpSysContact.setStatus("current")
_CucsCommSnmpSysLocation_Type = SnmpAdminString
_CucsCommSnmpSysLocation_Object = MibTableColumn
cucsCommSnmpSysLocation = _CucsCommSnmpSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 12),
    _CucsCommSnmpSysLocation_Type()
)
cucsCommSnmpSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpSysLocation.setStatus("current")
_CucsCommSnmpConfigState_Type = CucsCommSnmpConfigState
_CucsCommSnmpConfigState_Object = MibTableColumn
cucsCommSnmpConfigState = _CucsCommSnmpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 13),
    _CucsCommSnmpConfigState_Type()
)
cucsCommSnmpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpConfigState.setStatus("current")
_CucsCommSnmpOperPort_Type = Gauge32
_CucsCommSnmpOperPort_Object = MibTableColumn
cucsCommSnmpOperPort = _CucsCommSnmpOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 14),
    _CucsCommSnmpOperPort_Type()
)
cucsCommSnmpOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpOperPort.setStatus("current")
_CucsCommSnmpPolicyLevel_Type = Gauge32
_CucsCommSnmpPolicyLevel_Object = MibTableColumn
cucsCommSnmpPolicyLevel = _CucsCommSnmpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 15),
    _CucsCommSnmpPolicyLevel_Type()
)
cucsCommSnmpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpPolicyLevel.setStatus("current")
_CucsCommSnmpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSnmpPolicyOwner_Object = MibTableColumn
cucsCommSnmpPolicyOwner = _CucsCommSnmpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 16),
    _CucsCommSnmpPolicyOwner_Type()
)
cucsCommSnmpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpPolicyOwner.setStatus("current")
_CucsCommSnmpIsSetSnmpSecure_Type = TruthValue
_CucsCommSnmpIsSetSnmpSecure_Object = MibTableColumn
cucsCommSnmpIsSetSnmpSecure = _CucsCommSnmpIsSetSnmpSecure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 17),
    _CucsCommSnmpIsSetSnmpSecure_Type()
)
cucsCommSnmpIsSetSnmpSecure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpIsSetSnmpSecure.setStatus("current")
_CucsCommSnmpSnmpOperState_Type = CucsCommAdminState
_CucsCommSnmpSnmpOperState_Object = MibTableColumn
cucsCommSnmpSnmpOperState = _CucsCommSnmpSnmpOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 10, 1, 18),
    _CucsCommSnmpSnmpOperState_Type()
)
cucsCommSnmpSnmpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpSnmpOperState.setStatus("current")
_CucsCommSnmpTrapTable_Object = MibTable
cucsCommSnmpTrapTable = _CucsCommSnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11)
)
if mibBuilder.loadTexts:
    cucsCommSnmpTrapTable.setStatus("current")
_CucsCommSnmpTrapEntry_Object = MibTableRow
cucsCommSnmpTrapEntry = _CucsCommSnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1)
)
cucsCommSnmpTrapEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSnmpTrapInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSnmpTrapEntry.setStatus("current")
_CucsCommSnmpTrapInstanceId_Type = CucsManagedObjectId
_CucsCommSnmpTrapInstanceId_Object = MibTableColumn
cucsCommSnmpTrapInstanceId = _CucsCommSnmpTrapInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 1),
    _CucsCommSnmpTrapInstanceId_Type()
)
cucsCommSnmpTrapInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapInstanceId.setStatus("current")
_CucsCommSnmpTrapDn_Type = CucsManagedObjectDn
_CucsCommSnmpTrapDn_Object = MibTableColumn
cucsCommSnmpTrapDn = _CucsCommSnmpTrapDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 2),
    _CucsCommSnmpTrapDn_Type()
)
cucsCommSnmpTrapDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapDn.setStatus("current")
_CucsCommSnmpTrapRn_Type = SnmpAdminString
_CucsCommSnmpTrapRn_Object = MibTableColumn
cucsCommSnmpTrapRn = _CucsCommSnmpTrapRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 3),
    _CucsCommSnmpTrapRn_Type()
)
cucsCommSnmpTrapRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapRn.setStatus("current")
_CucsCommSnmpTrapCommunity_Type = SnmpAdminString
_CucsCommSnmpTrapCommunity_Object = MibTableColumn
cucsCommSnmpTrapCommunity = _CucsCommSnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 4),
    _CucsCommSnmpTrapCommunity_Type()
)
cucsCommSnmpTrapCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapCommunity.setStatus("current")
_CucsCommSnmpTrapHostname_Type = SnmpAdminString
_CucsCommSnmpTrapHostname_Object = MibTableColumn
cucsCommSnmpTrapHostname = _CucsCommSnmpTrapHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 5),
    _CucsCommSnmpTrapHostname_Type()
)
cucsCommSnmpTrapHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapHostname.setStatus("current")
_CucsCommSnmpTrapPort_Type = Gauge32
_CucsCommSnmpTrapPort_Object = MibTableColumn
cucsCommSnmpTrapPort = _CucsCommSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 6),
    _CucsCommSnmpTrapPort_Type()
)
cucsCommSnmpTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapPort.setStatus("current")
_CucsCommSnmpTrapV3Privilege_Type = CucsCommSnmpV3Privilege
_CucsCommSnmpTrapV3Privilege_Object = MibTableColumn
cucsCommSnmpTrapV3Privilege = _CucsCommSnmpTrapV3Privilege_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 7),
    _CucsCommSnmpTrapV3Privilege_Type()
)
cucsCommSnmpTrapV3Privilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapV3Privilege.setStatus("current")
_CucsCommSnmpTrapVersion_Type = CucsCommSnmpVersion
_CucsCommSnmpTrapVersion_Object = MibTableColumn
cucsCommSnmpTrapVersion = _CucsCommSnmpTrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 8),
    _CucsCommSnmpTrapVersion_Type()
)
cucsCommSnmpTrapVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapVersion.setStatus("current")
_CucsCommSnmpTrapNotificationType_Type = CucsCommSnmpNotificationType
_CucsCommSnmpTrapNotificationType_Object = MibTableColumn
cucsCommSnmpTrapNotificationType = _CucsCommSnmpTrapNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 11, 1, 9),
    _CucsCommSnmpTrapNotificationType_Type()
)
cucsCommSnmpTrapNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpTrapNotificationType.setStatus("current")
_CucsCommSnmpUserTable_Object = MibTable
cucsCommSnmpUserTable = _CucsCommSnmpUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12)
)
if mibBuilder.loadTexts:
    cucsCommSnmpUserTable.setStatus("current")
_CucsCommSnmpUserEntry_Object = MibTableRow
cucsCommSnmpUserEntry = _CucsCommSnmpUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1)
)
cucsCommSnmpUserEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSnmpUserInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSnmpUserEntry.setStatus("current")
_CucsCommSnmpUserInstanceId_Type = CucsManagedObjectId
_CucsCommSnmpUserInstanceId_Object = MibTableColumn
cucsCommSnmpUserInstanceId = _CucsCommSnmpUserInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 1),
    _CucsCommSnmpUserInstanceId_Type()
)
cucsCommSnmpUserInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSnmpUserInstanceId.setStatus("current")
_CucsCommSnmpUserDn_Type = CucsManagedObjectDn
_CucsCommSnmpUserDn_Object = MibTableColumn
cucsCommSnmpUserDn = _CucsCommSnmpUserDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 2),
    _CucsCommSnmpUserDn_Type()
)
cucsCommSnmpUserDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserDn.setStatus("current")
_CucsCommSnmpUserRn_Type = SnmpAdminString
_CucsCommSnmpUserRn_Object = MibTableColumn
cucsCommSnmpUserRn = _CucsCommSnmpUserRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 3),
    _CucsCommSnmpUserRn_Type()
)
cucsCommSnmpUserRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserRn.setStatus("current")
_CucsCommSnmpUserAuth_Type = CucsCommSnmpAuth
_CucsCommSnmpUserAuth_Object = MibTableColumn
cucsCommSnmpUserAuth = _CucsCommSnmpUserAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 4),
    _CucsCommSnmpUserAuth_Type()
)
cucsCommSnmpUserAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserAuth.setStatus("current")
_CucsCommSnmpUserDescr_Type = SnmpAdminString
_CucsCommSnmpUserDescr_Object = MibTableColumn
cucsCommSnmpUserDescr = _CucsCommSnmpUserDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 5),
    _CucsCommSnmpUserDescr_Type()
)
cucsCommSnmpUserDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserDescr.setStatus("current")
_CucsCommSnmpUserName_Type = SnmpAdminString
_CucsCommSnmpUserName_Object = MibTableColumn
cucsCommSnmpUserName = _CucsCommSnmpUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 7),
    _CucsCommSnmpUserName_Type()
)
cucsCommSnmpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserName.setStatus("current")
_CucsCommSnmpUserPrivPwdSet_Type = TruthValue
_CucsCommSnmpUserPrivPwdSet_Object = MibTableColumn
cucsCommSnmpUserPrivPwdSet = _CucsCommSnmpUserPrivPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 8),
    _CucsCommSnmpUserPrivPwdSet_Type()
)
cucsCommSnmpUserPrivPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserPrivPwdSet.setStatus("current")
_CucsCommSnmpUserPrivpwd_Type = SnmpAdminString
_CucsCommSnmpUserPrivpwd_Object = MibTableColumn
cucsCommSnmpUserPrivpwd = _CucsCommSnmpUserPrivpwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 9),
    _CucsCommSnmpUserPrivpwd_Type()
)
cucsCommSnmpUserPrivpwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserPrivpwd.setStatus("current")
_CucsCommSnmpUserPwd_Type = SnmpAdminString
_CucsCommSnmpUserPwd_Object = MibTableColumn
cucsCommSnmpUserPwd = _CucsCommSnmpUserPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 10),
    _CucsCommSnmpUserPwd_Type()
)
cucsCommSnmpUserPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserPwd.setStatus("current")
_CucsCommSnmpUserPwdSet_Type = TruthValue
_CucsCommSnmpUserPwdSet_Object = MibTableColumn
cucsCommSnmpUserPwdSet = _CucsCommSnmpUserPwdSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 11),
    _CucsCommSnmpUserPwdSet_Type()
)
cucsCommSnmpUserPwdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserPwdSet.setStatus("current")
_CucsCommSnmpUserUseAes_Type = TruthValue
_CucsCommSnmpUserUseAes_Object = MibTableColumn
cucsCommSnmpUserUseAes = _CucsCommSnmpUserUseAes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 12),
    _CucsCommSnmpUserUseAes_Type()
)
cucsCommSnmpUserUseAes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserUseAes.setStatus("current")
_CucsCommSnmpUserConfigState_Type = CucsAaaConfigState
_CucsCommSnmpUserConfigState_Object = MibTableColumn
cucsCommSnmpUserConfigState = _CucsCommSnmpUserConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 13),
    _CucsCommSnmpUserConfigState_Type()
)
cucsCommSnmpUserConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserConfigState.setStatus("current")
_CucsCommSnmpUserConfigStatusMessage_Type = SnmpAdminString
_CucsCommSnmpUserConfigStatusMessage_Object = MibTableColumn
cucsCommSnmpUserConfigStatusMessage = _CucsCommSnmpUserConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 12, 1, 14),
    _CucsCommSnmpUserConfigStatusMessage_Type()
)
cucsCommSnmpUserConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSnmpUserConfigStatusMessage.setStatus("current")
_CucsCommSshTable_Object = MibTable
cucsCommSshTable = _CucsCommSshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13)
)
if mibBuilder.loadTexts:
    cucsCommSshTable.setStatus("current")
_CucsCommSshEntry_Object = MibTableRow
cucsCommSshEntry = _CucsCommSshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1)
)
cucsCommSshEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSshInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSshEntry.setStatus("current")
_CucsCommSshInstanceId_Type = CucsManagedObjectId
_CucsCommSshInstanceId_Object = MibTableColumn
cucsCommSshInstanceId = _CucsCommSshInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 1),
    _CucsCommSshInstanceId_Type()
)
cucsCommSshInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSshInstanceId.setStatus("current")
_CucsCommSshDn_Type = CucsManagedObjectDn
_CucsCommSshDn_Object = MibTableColumn
cucsCommSshDn = _CucsCommSshDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 2),
    _CucsCommSshDn_Type()
)
cucsCommSshDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshDn.setStatus("current")
_CucsCommSshRn_Type = SnmpAdminString
_CucsCommSshRn_Object = MibTableColumn
cucsCommSshRn = _CucsCommSshRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 3),
    _CucsCommSshRn_Type()
)
cucsCommSshRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshRn.setStatus("current")
_CucsCommSshAdminState_Type = CucsCommSshAdminState
_CucsCommSshAdminState_Object = MibTableColumn
cucsCommSshAdminState = _CucsCommSshAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 4),
    _CucsCommSshAdminState_Type()
)
cucsCommSshAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshAdminState.setStatus("current")
_CucsCommSshDescr_Type = SnmpAdminString
_CucsCommSshDescr_Object = MibTableColumn
cucsCommSshDescr = _CucsCommSshDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 5),
    _CucsCommSshDescr_Type()
)
cucsCommSshDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshDescr.setStatus("current")
_CucsCommSshIntId_Type = SnmpAdminString
_CucsCommSshIntId_Object = MibTableColumn
cucsCommSshIntId = _CucsCommSshIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 6),
    _CucsCommSshIntId_Type()
)
cucsCommSshIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshIntId.setStatus("current")
_CucsCommSshName_Type = SnmpAdminString
_CucsCommSshName_Object = MibTableColumn
cucsCommSshName = _CucsCommSshName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 7),
    _CucsCommSshName_Type()
)
cucsCommSshName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshName.setStatus("current")
_CucsCommSshPort_Type = Gauge32
_CucsCommSshPort_Object = MibTableColumn
cucsCommSshPort = _CucsCommSshPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 8),
    _CucsCommSshPort_Type()
)
cucsCommSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshPort.setStatus("current")
_CucsCommSshProto_Type = CucsCommShellProto
_CucsCommSshProto_Object = MibTableColumn
cucsCommSshProto = _CucsCommSshProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 9),
    _CucsCommSshProto_Type()
)
cucsCommSshProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshProto.setStatus("current")
_CucsCommSshOperPort_Type = Gauge32
_CucsCommSshOperPort_Object = MibTableColumn
cucsCommSshOperPort = _CucsCommSshOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 10),
    _CucsCommSshOperPort_Type()
)
cucsCommSshOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshOperPort.setStatus("current")
_CucsCommSshPolicyLevel_Type = Gauge32
_CucsCommSshPolicyLevel_Object = MibTableColumn
cucsCommSshPolicyLevel = _CucsCommSshPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 11),
    _CucsCommSshPolicyLevel_Type()
)
cucsCommSshPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshPolicyLevel.setStatus("current")
_CucsCommSshPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSshPolicyOwner_Object = MibTableColumn
cucsCommSshPolicyOwner = _CucsCommSshPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 13, 1, 12),
    _CucsCommSshPolicyOwner_Type()
)
cucsCommSshPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSshPolicyOwner.setStatus("current")
_CucsCommSvcEpTable_Object = MibTable
cucsCommSvcEpTable = _CucsCommSvcEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14)
)
if mibBuilder.loadTexts:
    cucsCommSvcEpTable.setStatus("current")
_CucsCommSvcEpEntry_Object = MibTableRow
cucsCommSvcEpEntry = _CucsCommSvcEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1)
)
cucsCommSvcEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSvcEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSvcEpEntry.setStatus("current")
_CucsCommSvcEpInstanceId_Type = CucsManagedObjectId
_CucsCommSvcEpInstanceId_Object = MibTableColumn
cucsCommSvcEpInstanceId = _CucsCommSvcEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 1),
    _CucsCommSvcEpInstanceId_Type()
)
cucsCommSvcEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSvcEpInstanceId.setStatus("current")
_CucsCommSvcEpDn_Type = CucsManagedObjectDn
_CucsCommSvcEpDn_Object = MibTableColumn
cucsCommSvcEpDn = _CucsCommSvcEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 2),
    _CucsCommSvcEpDn_Type()
)
cucsCommSvcEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpDn.setStatus("current")
_CucsCommSvcEpRn_Type = SnmpAdminString
_CucsCommSvcEpRn_Object = MibTableColumn
cucsCommSvcEpRn = _CucsCommSvcEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 3),
    _CucsCommSvcEpRn_Type()
)
cucsCommSvcEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpRn.setStatus("current")
_CucsCommSvcEpDescr_Type = SnmpAdminString
_CucsCommSvcEpDescr_Object = MibTableColumn
cucsCommSvcEpDescr = _CucsCommSvcEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 4),
    _CucsCommSvcEpDescr_Type()
)
cucsCommSvcEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpDescr.setStatus("current")
_CucsCommSvcEpFsmDescr_Type = SnmpAdminString
_CucsCommSvcEpFsmDescr_Object = MibTableColumn
cucsCommSvcEpFsmDescr = _CucsCommSvcEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 5),
    _CucsCommSvcEpFsmDescr_Type()
)
cucsCommSvcEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmDescr.setStatus("current")
_CucsCommSvcEpFsmFlags_Type = SnmpAdminString
_CucsCommSvcEpFsmFlags_Object = MibTableColumn
cucsCommSvcEpFsmFlags = _CucsCommSvcEpFsmFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 6),
    _CucsCommSvcEpFsmFlags_Type()
)
cucsCommSvcEpFsmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmFlags.setStatus("current")
_CucsCommSvcEpFsmPrev_Type = SnmpAdminString
_CucsCommSvcEpFsmPrev_Object = MibTableColumn
cucsCommSvcEpFsmPrev = _CucsCommSvcEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 7),
    _CucsCommSvcEpFsmPrev_Type()
)
cucsCommSvcEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmPrev.setStatus("current")
_CucsCommSvcEpFsmProgr_Type = Gauge32
_CucsCommSvcEpFsmProgr_Object = MibTableColumn
cucsCommSvcEpFsmProgr = _CucsCommSvcEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 8),
    _CucsCommSvcEpFsmProgr_Type()
)
cucsCommSvcEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmProgr.setStatus("current")
_CucsCommSvcEpFsmRmtInvErrCode_Type = Gauge32
_CucsCommSvcEpFsmRmtInvErrCode_Object = MibTableColumn
cucsCommSvcEpFsmRmtInvErrCode = _CucsCommSvcEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 9),
    _CucsCommSvcEpFsmRmtInvErrCode_Type()
)
cucsCommSvcEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtInvErrCode.setStatus("current")
_CucsCommSvcEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsCommSvcEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsCommSvcEpFsmRmtInvErrDescr = _CucsCommSvcEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 10),
    _CucsCommSvcEpFsmRmtInvErrDescr_Type()
)
cucsCommSvcEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtInvErrDescr.setStatus("current")
_CucsCommSvcEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsCommSvcEpFsmRmtInvRslt_Object = MibTableColumn
cucsCommSvcEpFsmRmtInvRslt = _CucsCommSvcEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 11),
    _CucsCommSvcEpFsmRmtInvRslt_Type()
)
cucsCommSvcEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtInvRslt.setStatus("current")
_CucsCommSvcEpFsmStageDescr_Type = SnmpAdminString
_CucsCommSvcEpFsmStageDescr_Object = MibTableColumn
cucsCommSvcEpFsmStageDescr = _CucsCommSvcEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 12),
    _CucsCommSvcEpFsmStageDescr_Type()
)
cucsCommSvcEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageDescr.setStatus("current")
_CucsCommSvcEpFsmStamp_Type = DateAndTime
_CucsCommSvcEpFsmStamp_Object = MibTableColumn
cucsCommSvcEpFsmStamp = _CucsCommSvcEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 13),
    _CucsCommSvcEpFsmStamp_Type()
)
cucsCommSvcEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStamp.setStatus("current")
_CucsCommSvcEpFsmStatus_Type = SnmpAdminString
_CucsCommSvcEpFsmStatus_Object = MibTableColumn
cucsCommSvcEpFsmStatus = _CucsCommSvcEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 14),
    _CucsCommSvcEpFsmStatus_Type()
)
cucsCommSvcEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStatus.setStatus("current")
_CucsCommSvcEpFsmTry_Type = Gauge32
_CucsCommSvcEpFsmTry_Object = MibTableColumn
cucsCommSvcEpFsmTry = _CucsCommSvcEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 15),
    _CucsCommSvcEpFsmTry_Type()
)
cucsCommSvcEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTry.setStatus("current")
_CucsCommSvcEpIntId_Type = SnmpAdminString
_CucsCommSvcEpIntId_Object = MibTableColumn
cucsCommSvcEpIntId = _CucsCommSvcEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 16),
    _CucsCommSvcEpIntId_Type()
)
cucsCommSvcEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpIntId.setStatus("current")
_CucsCommSvcEpName_Type = SnmpAdminString
_CucsCommSvcEpName_Object = MibTableColumn
cucsCommSvcEpName = _CucsCommSvcEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 17),
    _CucsCommSvcEpName_Type()
)
cucsCommSvcEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpName.setStatus("current")
_CucsCommSvcEpConfigState_Type = CucsAaaConfigState
_CucsCommSvcEpConfigState_Object = MibTableColumn
cucsCommSvcEpConfigState = _CucsCommSvcEpConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 18),
    _CucsCommSvcEpConfigState_Type()
)
cucsCommSvcEpConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpConfigState.setStatus("current")
_CucsCommSvcEpConfigStatusMessage_Type = SnmpAdminString
_CucsCommSvcEpConfigStatusMessage_Object = MibTableColumn
cucsCommSvcEpConfigStatusMessage = _CucsCommSvcEpConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 19),
    _CucsCommSvcEpConfigStatusMessage_Type()
)
cucsCommSvcEpConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpConfigStatusMessage.setStatus("current")
_CucsCommSvcEpPolicyLevel_Type = Gauge32
_CucsCommSvcEpPolicyLevel_Object = MibTableColumn
cucsCommSvcEpPolicyLevel = _CucsCommSvcEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 20),
    _CucsCommSvcEpPolicyLevel_Type()
)
cucsCommSvcEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpPolicyLevel.setStatus("current")
_CucsCommSvcEpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSvcEpPolicyOwner_Object = MibTableColumn
cucsCommSvcEpPolicyOwner = _CucsCommSvcEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 14, 1, 21),
    _CucsCommSvcEpPolicyOwner_Type()
)
cucsCommSvcEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpPolicyOwner.setStatus("current")
_CucsCommSvcEpFsmTaskTable_Object = MibTable
cucsCommSvcEpFsmTaskTable = _CucsCommSvcEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15)
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskTable.setStatus("current")
_CucsCommSvcEpFsmTaskEntry_Object = MibTableRow
cucsCommSvcEpFsmTaskEntry = _CucsCommSvcEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1)
)
cucsCommSvcEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSvcEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskEntry.setStatus("current")
_CucsCommSvcEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsCommSvcEpFsmTaskInstanceId_Object = MibTableColumn
cucsCommSvcEpFsmTaskInstanceId = _CucsCommSvcEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 1),
    _CucsCommSvcEpFsmTaskInstanceId_Type()
)
cucsCommSvcEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskInstanceId.setStatus("current")
_CucsCommSvcEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsCommSvcEpFsmTaskDn_Object = MibTableColumn
cucsCommSvcEpFsmTaskDn = _CucsCommSvcEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 2),
    _CucsCommSvcEpFsmTaskDn_Type()
)
cucsCommSvcEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskDn.setStatus("current")
_CucsCommSvcEpFsmTaskRn_Type = SnmpAdminString
_CucsCommSvcEpFsmTaskRn_Object = MibTableColumn
cucsCommSvcEpFsmTaskRn = _CucsCommSvcEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 3),
    _CucsCommSvcEpFsmTaskRn_Type()
)
cucsCommSvcEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskRn.setStatus("current")
_CucsCommSvcEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsCommSvcEpFsmTaskCompletion_Object = MibTableColumn
cucsCommSvcEpFsmTaskCompletion = _CucsCommSvcEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 4),
    _CucsCommSvcEpFsmTaskCompletion_Type()
)
cucsCommSvcEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskCompletion.setStatus("current")
_CucsCommSvcEpFsmTaskFlags_Type = CucsCommSvcEpFsmTaskFlags
_CucsCommSvcEpFsmTaskFlags_Object = MibTableColumn
cucsCommSvcEpFsmTaskFlags = _CucsCommSvcEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 5),
    _CucsCommSvcEpFsmTaskFlags_Type()
)
cucsCommSvcEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskFlags.setStatus("current")
_CucsCommSvcEpFsmTaskItem_Type = CucsCommSvcEpFsmTaskItem
_CucsCommSvcEpFsmTaskItem_Object = MibTableColumn
cucsCommSvcEpFsmTaskItem = _CucsCommSvcEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 6),
    _CucsCommSvcEpFsmTaskItem_Type()
)
cucsCommSvcEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskItem.setStatus("current")
_CucsCommSvcEpFsmTaskSeqId_Type = Gauge32
_CucsCommSvcEpFsmTaskSeqId_Object = MibTableColumn
cucsCommSvcEpFsmTaskSeqId = _CucsCommSvcEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 15, 1, 7),
    _CucsCommSvcEpFsmTaskSeqId_Type()
)
cucsCommSvcEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTaskSeqId.setStatus("current")
_CucsCommSyslogTable_Object = MibTable
cucsCommSyslogTable = _CucsCommSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16)
)
if mibBuilder.loadTexts:
    cucsCommSyslogTable.setStatus("current")
_CucsCommSyslogEntry_Object = MibTableRow
cucsCommSyslogEntry = _CucsCommSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1)
)
cucsCommSyslogEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogEntry.setStatus("current")
_CucsCommSyslogInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogInstanceId_Object = MibTableColumn
cucsCommSyslogInstanceId = _CucsCommSyslogInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 1),
    _CucsCommSyslogInstanceId_Type()
)
cucsCommSyslogInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogInstanceId.setStatus("current")
_CucsCommSyslogDn_Type = CucsManagedObjectDn
_CucsCommSyslogDn_Object = MibTableColumn
cucsCommSyslogDn = _CucsCommSyslogDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 2),
    _CucsCommSyslogDn_Type()
)
cucsCommSyslogDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogDn.setStatus("current")
_CucsCommSyslogRn_Type = SnmpAdminString
_CucsCommSyslogRn_Object = MibTableColumn
cucsCommSyslogRn = _CucsCommSyslogRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 3),
    _CucsCommSyslogRn_Type()
)
cucsCommSyslogRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogRn.setStatus("current")
_CucsCommSyslogAdminState_Type = CucsCommAdminState
_CucsCommSyslogAdminState_Object = MibTableColumn
cucsCommSyslogAdminState = _CucsCommSyslogAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 4),
    _CucsCommSyslogAdminState_Type()
)
cucsCommSyslogAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogAdminState.setStatus("current")
_CucsCommSyslogDescr_Type = SnmpAdminString
_CucsCommSyslogDescr_Object = MibTableColumn
cucsCommSyslogDescr = _CucsCommSyslogDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 5),
    _CucsCommSyslogDescr_Type()
)
cucsCommSyslogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogDescr.setStatus("current")
_CucsCommSyslogIntId_Type = SnmpAdminString
_CucsCommSyslogIntId_Object = MibTableColumn
cucsCommSyslogIntId = _CucsCommSyslogIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 6),
    _CucsCommSyslogIntId_Type()
)
cucsCommSyslogIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogIntId.setStatus("current")
_CucsCommSyslogName_Type = SnmpAdminString
_CucsCommSyslogName_Object = MibTableColumn
cucsCommSyslogName = _CucsCommSyslogName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 7),
    _CucsCommSyslogName_Type()
)
cucsCommSyslogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogName.setStatus("current")
_CucsCommSyslogPort_Type = Gauge32
_CucsCommSyslogPort_Object = MibTableColumn
cucsCommSyslogPort = _CucsCommSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 8),
    _CucsCommSyslogPort_Type()
)
cucsCommSyslogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogPort.setStatus("current")
_CucsCommSyslogProto_Type = CucsCommSyslogProto
_CucsCommSyslogProto_Object = MibTableColumn
cucsCommSyslogProto = _CucsCommSyslogProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 9),
    _CucsCommSyslogProto_Type()
)
cucsCommSyslogProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogProto.setStatus("current")
_CucsCommSyslogSeverity_Type = CucsCommSyslogSeverity
_CucsCommSyslogSeverity_Object = MibTableColumn
cucsCommSyslogSeverity = _CucsCommSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 10),
    _CucsCommSyslogSeverity_Type()
)
cucsCommSyslogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSeverity.setStatus("current")
_CucsCommSyslogOperPort_Type = Gauge32
_CucsCommSyslogOperPort_Object = MibTableColumn
cucsCommSyslogOperPort = _CucsCommSyslogOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 11),
    _CucsCommSyslogOperPort_Type()
)
cucsCommSyslogOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogOperPort.setStatus("current")
_CucsCommSyslogPolicyLevel_Type = Gauge32
_CucsCommSyslogPolicyLevel_Object = MibTableColumn
cucsCommSyslogPolicyLevel = _CucsCommSyslogPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 12),
    _CucsCommSyslogPolicyLevel_Type()
)
cucsCommSyslogPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogPolicyLevel.setStatus("current")
_CucsCommSyslogPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSyslogPolicyOwner_Object = MibTableColumn
cucsCommSyslogPolicyOwner = _CucsCommSyslogPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 16, 1, 13),
    _CucsCommSyslogPolicyOwner_Type()
)
cucsCommSyslogPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogPolicyOwner.setStatus("current")
_CucsCommSyslogClientTable_Object = MibTable
cucsCommSyslogClientTable = _CucsCommSyslogClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17)
)
if mibBuilder.loadTexts:
    cucsCommSyslogClientTable.setStatus("current")
_CucsCommSyslogClientEntry_Object = MibTableRow
cucsCommSyslogClientEntry = _CucsCommSyslogClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1)
)
cucsCommSyslogClientEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogClientInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogClientEntry.setStatus("current")
_CucsCommSyslogClientInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogClientInstanceId_Object = MibTableColumn
cucsCommSyslogClientInstanceId = _CucsCommSyslogClientInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 1),
    _CucsCommSyslogClientInstanceId_Type()
)
cucsCommSyslogClientInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogClientInstanceId.setStatus("current")
_CucsCommSyslogClientDn_Type = CucsManagedObjectDn
_CucsCommSyslogClientDn_Object = MibTableColumn
cucsCommSyslogClientDn = _CucsCommSyslogClientDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 2),
    _CucsCommSyslogClientDn_Type()
)
cucsCommSyslogClientDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientDn.setStatus("current")
_CucsCommSyslogClientRn_Type = SnmpAdminString
_CucsCommSyslogClientRn_Object = MibTableColumn
cucsCommSyslogClientRn = _CucsCommSyslogClientRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 3),
    _CucsCommSyslogClientRn_Type()
)
cucsCommSyslogClientRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientRn.setStatus("current")
_CucsCommSyslogClientAdminState_Type = CucsCommSyslogAdminState
_CucsCommSyslogClientAdminState_Object = MibTableColumn
cucsCommSyslogClientAdminState = _CucsCommSyslogClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 4),
    _CucsCommSyslogClientAdminState_Type()
)
cucsCommSyslogClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientAdminState.setStatus("current")
_CucsCommSyslogClientForwardingFacility_Type = CucsCommSyslogForwardingFacility
_CucsCommSyslogClientForwardingFacility_Object = MibTableColumn
cucsCommSyslogClientForwardingFacility = _CucsCommSyslogClientForwardingFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 5),
    _CucsCommSyslogClientForwardingFacility_Type()
)
cucsCommSyslogClientForwardingFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientForwardingFacility.setStatus("current")
_CucsCommSyslogClientHostname_Type = SnmpAdminString
_CucsCommSyslogClientHostname_Object = MibTableColumn
cucsCommSyslogClientHostname = _CucsCommSyslogClientHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 6),
    _CucsCommSyslogClientHostname_Type()
)
cucsCommSyslogClientHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientHostname.setStatus("current")
_CucsCommSyslogClientName_Type = CucsCommSyslogClientEnum
_CucsCommSyslogClientName_Object = MibTableColumn
cucsCommSyslogClientName = _CucsCommSyslogClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 7),
    _CucsCommSyslogClientName_Type()
)
cucsCommSyslogClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientName.setStatus("current")
_CucsCommSyslogClientSeverity_Type = CucsCommSyslogSeverity
_CucsCommSyslogClientSeverity_Object = MibTableColumn
cucsCommSyslogClientSeverity = _CucsCommSyslogClientSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 17, 1, 8),
    _CucsCommSyslogClientSeverity_Type()
)
cucsCommSyslogClientSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogClientSeverity.setStatus("current")
_CucsCommSyslogConsoleTable_Object = MibTable
cucsCommSyslogConsoleTable = _CucsCommSyslogConsoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18)
)
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleTable.setStatus("current")
_CucsCommSyslogConsoleEntry_Object = MibTableRow
cucsCommSyslogConsoleEntry = _CucsCommSyslogConsoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1)
)
cucsCommSyslogConsoleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogConsoleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleEntry.setStatus("current")
_CucsCommSyslogConsoleInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogConsoleInstanceId_Object = MibTableColumn
cucsCommSyslogConsoleInstanceId = _CucsCommSyslogConsoleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 1),
    _CucsCommSyslogConsoleInstanceId_Type()
)
cucsCommSyslogConsoleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleInstanceId.setStatus("current")
_CucsCommSyslogConsoleDn_Type = CucsManagedObjectDn
_CucsCommSyslogConsoleDn_Object = MibTableColumn
cucsCommSyslogConsoleDn = _CucsCommSyslogConsoleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 2),
    _CucsCommSyslogConsoleDn_Type()
)
cucsCommSyslogConsoleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleDn.setStatus("current")
_CucsCommSyslogConsoleRn_Type = SnmpAdminString
_CucsCommSyslogConsoleRn_Object = MibTableColumn
cucsCommSyslogConsoleRn = _CucsCommSyslogConsoleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 3),
    _CucsCommSyslogConsoleRn_Type()
)
cucsCommSyslogConsoleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleRn.setStatus("current")
_CucsCommSyslogConsoleAdminState_Type = CucsCommSyslogAdminState
_CucsCommSyslogConsoleAdminState_Object = MibTableColumn
cucsCommSyslogConsoleAdminState = _CucsCommSyslogConsoleAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 4),
    _CucsCommSyslogConsoleAdminState_Type()
)
cucsCommSyslogConsoleAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleAdminState.setStatus("current")
_CucsCommSyslogConsoleDescr_Type = SnmpAdminString
_CucsCommSyslogConsoleDescr_Object = MibTableColumn
cucsCommSyslogConsoleDescr = _CucsCommSyslogConsoleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 5),
    _CucsCommSyslogConsoleDescr_Type()
)
cucsCommSyslogConsoleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleDescr.setStatus("current")
_CucsCommSyslogConsoleName_Type = SnmpAdminString
_CucsCommSyslogConsoleName_Object = MibTableColumn
cucsCommSyslogConsoleName = _CucsCommSyslogConsoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 7),
    _CucsCommSyslogConsoleName_Type()
)
cucsCommSyslogConsoleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleName.setStatus("current")
_CucsCommSyslogConsoleSeverity_Type = CucsCommSyslogRestrictedSeverity
_CucsCommSyslogConsoleSeverity_Object = MibTableColumn
cucsCommSyslogConsoleSeverity = _CucsCommSyslogConsoleSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 18, 1, 8),
    _CucsCommSyslogConsoleSeverity_Type()
)
cucsCommSyslogConsoleSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogConsoleSeverity.setStatus("current")
_CucsCommSyslogFileTable_Object = MibTable
cucsCommSyslogFileTable = _CucsCommSyslogFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19)
)
if mibBuilder.loadTexts:
    cucsCommSyslogFileTable.setStatus("current")
_CucsCommSyslogFileEntry_Object = MibTableRow
cucsCommSyslogFileEntry = _CucsCommSyslogFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1)
)
cucsCommSyslogFileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogFileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogFileEntry.setStatus("current")
_CucsCommSyslogFileInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogFileInstanceId_Object = MibTableColumn
cucsCommSyslogFileInstanceId = _CucsCommSyslogFileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 1),
    _CucsCommSyslogFileInstanceId_Type()
)
cucsCommSyslogFileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogFileInstanceId.setStatus("current")
_CucsCommSyslogFileDn_Type = CucsManagedObjectDn
_CucsCommSyslogFileDn_Object = MibTableColumn
cucsCommSyslogFileDn = _CucsCommSyslogFileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 2),
    _CucsCommSyslogFileDn_Type()
)
cucsCommSyslogFileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileDn.setStatus("current")
_CucsCommSyslogFileRn_Type = SnmpAdminString
_CucsCommSyslogFileRn_Object = MibTableColumn
cucsCommSyslogFileRn = _CucsCommSyslogFileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 3),
    _CucsCommSyslogFileRn_Type()
)
cucsCommSyslogFileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileRn.setStatus("current")
_CucsCommSyslogFileAdminState_Type = CucsCommSyslogAdminState
_CucsCommSyslogFileAdminState_Object = MibTableColumn
cucsCommSyslogFileAdminState = _CucsCommSyslogFileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 4),
    _CucsCommSyslogFileAdminState_Type()
)
cucsCommSyslogFileAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileAdminState.setStatus("current")
_CucsCommSyslogFileDescr_Type = SnmpAdminString
_CucsCommSyslogFileDescr_Object = MibTableColumn
cucsCommSyslogFileDescr = _CucsCommSyslogFileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 5),
    _CucsCommSyslogFileDescr_Type()
)
cucsCommSyslogFileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileDescr.setStatus("current")
_CucsCommSyslogFileName_Type = SnmpAdminString
_CucsCommSyslogFileName_Object = MibTableColumn
cucsCommSyslogFileName = _CucsCommSyslogFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 7),
    _CucsCommSyslogFileName_Type()
)
cucsCommSyslogFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileName.setStatus("current")
_CucsCommSyslogFileSeverity_Type = CucsCommSyslogSeverity
_CucsCommSyslogFileSeverity_Object = MibTableColumn
cucsCommSyslogFileSeverity = _CucsCommSyslogFileSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 8),
    _CucsCommSyslogFileSeverity_Type()
)
cucsCommSyslogFileSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileSeverity.setStatus("current")
_CucsCommSyslogFileSize_Type = CucsCommSyslogFileSize
_CucsCommSyslogFileSize_Object = MibTableColumn
cucsCommSyslogFileSize = _CucsCommSyslogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 19, 1, 9),
    _CucsCommSyslogFileSize_Type()
)
cucsCommSyslogFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogFileSize.setStatus("current")
_CucsCommSyslogMonitorTable_Object = MibTable
cucsCommSyslogMonitorTable = _CucsCommSyslogMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20)
)
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorTable.setStatus("current")
_CucsCommSyslogMonitorEntry_Object = MibTableRow
cucsCommSyslogMonitorEntry = _CucsCommSyslogMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1)
)
cucsCommSyslogMonitorEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogMonitorInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorEntry.setStatus("current")
_CucsCommSyslogMonitorInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogMonitorInstanceId_Object = MibTableColumn
cucsCommSyslogMonitorInstanceId = _CucsCommSyslogMonitorInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 1),
    _CucsCommSyslogMonitorInstanceId_Type()
)
cucsCommSyslogMonitorInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorInstanceId.setStatus("current")
_CucsCommSyslogMonitorDn_Type = CucsManagedObjectDn
_CucsCommSyslogMonitorDn_Object = MibTableColumn
cucsCommSyslogMonitorDn = _CucsCommSyslogMonitorDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 2),
    _CucsCommSyslogMonitorDn_Type()
)
cucsCommSyslogMonitorDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorDn.setStatus("current")
_CucsCommSyslogMonitorRn_Type = SnmpAdminString
_CucsCommSyslogMonitorRn_Object = MibTableColumn
cucsCommSyslogMonitorRn = _CucsCommSyslogMonitorRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 3),
    _CucsCommSyslogMonitorRn_Type()
)
cucsCommSyslogMonitorRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorRn.setStatus("current")
_CucsCommSyslogMonitorAdminState_Type = CucsCommSyslogAdminState
_CucsCommSyslogMonitorAdminState_Object = MibTableColumn
cucsCommSyslogMonitorAdminState = _CucsCommSyslogMonitorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 4),
    _CucsCommSyslogMonitorAdminState_Type()
)
cucsCommSyslogMonitorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorAdminState.setStatus("current")
_CucsCommSyslogMonitorDescr_Type = SnmpAdminString
_CucsCommSyslogMonitorDescr_Object = MibTableColumn
cucsCommSyslogMonitorDescr = _CucsCommSyslogMonitorDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 5),
    _CucsCommSyslogMonitorDescr_Type()
)
cucsCommSyslogMonitorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorDescr.setStatus("current")
_CucsCommSyslogMonitorName_Type = SnmpAdminString
_CucsCommSyslogMonitorName_Object = MibTableColumn
cucsCommSyslogMonitorName = _CucsCommSyslogMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 7),
    _CucsCommSyslogMonitorName_Type()
)
cucsCommSyslogMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorName.setStatus("current")
_CucsCommSyslogMonitorSeverity_Type = CucsCommSyslogSeverity
_CucsCommSyslogMonitorSeverity_Object = MibTableColumn
cucsCommSyslogMonitorSeverity = _CucsCommSyslogMonitorSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 20, 1, 8),
    _CucsCommSyslogMonitorSeverity_Type()
)
cucsCommSyslogMonitorSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogMonitorSeverity.setStatus("current")
_CucsCommTelnetTable_Object = MibTable
cucsCommTelnetTable = _CucsCommTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21)
)
if mibBuilder.loadTexts:
    cucsCommTelnetTable.setStatus("current")
_CucsCommTelnetEntry_Object = MibTableRow
cucsCommTelnetEntry = _CucsCommTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1)
)
cucsCommTelnetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommTelnetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommTelnetEntry.setStatus("current")
_CucsCommTelnetInstanceId_Type = CucsManagedObjectId
_CucsCommTelnetInstanceId_Object = MibTableColumn
cucsCommTelnetInstanceId = _CucsCommTelnetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 1),
    _CucsCommTelnetInstanceId_Type()
)
cucsCommTelnetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommTelnetInstanceId.setStatus("current")
_CucsCommTelnetDn_Type = CucsManagedObjectDn
_CucsCommTelnetDn_Object = MibTableColumn
cucsCommTelnetDn = _CucsCommTelnetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 2),
    _CucsCommTelnetDn_Type()
)
cucsCommTelnetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetDn.setStatus("current")
_CucsCommTelnetRn_Type = SnmpAdminString
_CucsCommTelnetRn_Object = MibTableColumn
cucsCommTelnetRn = _CucsCommTelnetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 3),
    _CucsCommTelnetRn_Type()
)
cucsCommTelnetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetRn.setStatus("current")
_CucsCommTelnetAdminState_Type = CucsCommAdminState
_CucsCommTelnetAdminState_Object = MibTableColumn
cucsCommTelnetAdminState = _CucsCommTelnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 4),
    _CucsCommTelnetAdminState_Type()
)
cucsCommTelnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetAdminState.setStatus("current")
_CucsCommTelnetDescr_Type = SnmpAdminString
_CucsCommTelnetDescr_Object = MibTableColumn
cucsCommTelnetDescr = _CucsCommTelnetDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 5),
    _CucsCommTelnetDescr_Type()
)
cucsCommTelnetDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetDescr.setStatus("current")
_CucsCommTelnetIntId_Type = SnmpAdminString
_CucsCommTelnetIntId_Object = MibTableColumn
cucsCommTelnetIntId = _CucsCommTelnetIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 6),
    _CucsCommTelnetIntId_Type()
)
cucsCommTelnetIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetIntId.setStatus("current")
_CucsCommTelnetName_Type = SnmpAdminString
_CucsCommTelnetName_Object = MibTableColumn
cucsCommTelnetName = _CucsCommTelnetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 7),
    _CucsCommTelnetName_Type()
)
cucsCommTelnetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetName.setStatus("current")
_CucsCommTelnetPort_Type = Gauge32
_CucsCommTelnetPort_Object = MibTableColumn
cucsCommTelnetPort = _CucsCommTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 8),
    _CucsCommTelnetPort_Type()
)
cucsCommTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetPort.setStatus("current")
_CucsCommTelnetProto_Type = CucsCommShellProto
_CucsCommTelnetProto_Object = MibTableColumn
cucsCommTelnetProto = _CucsCommTelnetProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 9),
    _CucsCommTelnetProto_Type()
)
cucsCommTelnetProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetProto.setStatus("current")
_CucsCommTelnetOperPort_Type = Gauge32
_CucsCommTelnetOperPort_Object = MibTableColumn
cucsCommTelnetOperPort = _CucsCommTelnetOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 10),
    _CucsCommTelnetOperPort_Type()
)
cucsCommTelnetOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetOperPort.setStatus("current")
_CucsCommTelnetPolicyLevel_Type = Gauge32
_CucsCommTelnetPolicyLevel_Object = MibTableColumn
cucsCommTelnetPolicyLevel = _CucsCommTelnetPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 11),
    _CucsCommTelnetPolicyLevel_Type()
)
cucsCommTelnetPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetPolicyLevel.setStatus("current")
_CucsCommTelnetPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommTelnetPolicyOwner_Object = MibTableColumn
cucsCommTelnetPolicyOwner = _CucsCommTelnetPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 21, 1, 12),
    _CucsCommTelnetPolicyOwner_Type()
)
cucsCommTelnetPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommTelnetPolicyOwner.setStatus("current")
_CucsCommWebChannelTable_Object = MibTable
cucsCommWebChannelTable = _CucsCommWebChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22)
)
if mibBuilder.loadTexts:
    cucsCommWebChannelTable.setStatus("current")
_CucsCommWebChannelEntry_Object = MibTableRow
cucsCommWebChannelEntry = _CucsCommWebChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1)
)
cucsCommWebChannelEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommWebChannelInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommWebChannelEntry.setStatus("current")
_CucsCommWebChannelInstanceId_Type = CucsManagedObjectId
_CucsCommWebChannelInstanceId_Object = MibTableColumn
cucsCommWebChannelInstanceId = _CucsCommWebChannelInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 1),
    _CucsCommWebChannelInstanceId_Type()
)
cucsCommWebChannelInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommWebChannelInstanceId.setStatus("current")
_CucsCommWebChannelDn_Type = CucsManagedObjectDn
_CucsCommWebChannelDn_Object = MibTableColumn
cucsCommWebChannelDn = _CucsCommWebChannelDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 2),
    _CucsCommWebChannelDn_Type()
)
cucsCommWebChannelDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelDn.setStatus("current")
_CucsCommWebChannelRn_Type = SnmpAdminString
_CucsCommWebChannelRn_Object = MibTableColumn
cucsCommWebChannelRn = _CucsCommWebChannelRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 3),
    _CucsCommWebChannelRn_Type()
)
cucsCommWebChannelRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelRn.setStatus("current")
_CucsCommWebChannelChannelState_Type = CucsCommChannel
_CucsCommWebChannelChannelState_Object = MibTableColumn
cucsCommWebChannelChannelState = _CucsCommWebChannelChannelState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 4),
    _CucsCommWebChannelChannelState_Type()
)
cucsCommWebChannelChannelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelChannelState.setStatus("current")
_CucsCommWebChannelDescr_Type = SnmpAdminString
_CucsCommWebChannelDescr_Object = MibTableColumn
cucsCommWebChannelDescr = _CucsCommWebChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 5),
    _CucsCommWebChannelDescr_Type()
)
cucsCommWebChannelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelDescr.setStatus("current")
_CucsCommWebChannelIntId_Type = SnmpAdminString
_CucsCommWebChannelIntId_Object = MibTableColumn
cucsCommWebChannelIntId = _CucsCommWebChannelIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 6),
    _CucsCommWebChannelIntId_Type()
)
cucsCommWebChannelIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelIntId.setStatus("current")
_CucsCommWebChannelName_Type = SnmpAdminString
_CucsCommWebChannelName_Object = MibTableColumn
cucsCommWebChannelName = _CucsCommWebChannelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 7),
    _CucsCommWebChannelName_Type()
)
cucsCommWebChannelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelName.setStatus("current")
_CucsCommWebChannelPolicyLevel_Type = Gauge32
_CucsCommWebChannelPolicyLevel_Object = MibTableColumn
cucsCommWebChannelPolicyLevel = _CucsCommWebChannelPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 8),
    _CucsCommWebChannelPolicyLevel_Type()
)
cucsCommWebChannelPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelPolicyLevel.setStatus("current")
_CucsCommWebChannelPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommWebChannelPolicyOwner_Object = MibTableColumn
cucsCommWebChannelPolicyOwner = _CucsCommWebChannelPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 22, 1, 9),
    _CucsCommWebChannelPolicyOwner_Type()
)
cucsCommWebChannelPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebChannelPolicyOwner.setStatus("current")
_CucsCommWsmanTable_Object = MibTable
cucsCommWsmanTable = _CucsCommWsmanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23)
)
if mibBuilder.loadTexts:
    cucsCommWsmanTable.setStatus("current")
_CucsCommWsmanEntry_Object = MibTableRow
cucsCommWsmanEntry = _CucsCommWsmanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1)
)
cucsCommWsmanEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommWsmanInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommWsmanEntry.setStatus("current")
_CucsCommWsmanInstanceId_Type = CucsManagedObjectId
_CucsCommWsmanInstanceId_Object = MibTableColumn
cucsCommWsmanInstanceId = _CucsCommWsmanInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 1),
    _CucsCommWsmanInstanceId_Type()
)
cucsCommWsmanInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommWsmanInstanceId.setStatus("current")
_CucsCommWsmanDn_Type = CucsManagedObjectDn
_CucsCommWsmanDn_Object = MibTableColumn
cucsCommWsmanDn = _CucsCommWsmanDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 2),
    _CucsCommWsmanDn_Type()
)
cucsCommWsmanDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanDn.setStatus("current")
_CucsCommWsmanRn_Type = SnmpAdminString
_CucsCommWsmanRn_Object = MibTableColumn
cucsCommWsmanRn = _CucsCommWsmanRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 3),
    _CucsCommWsmanRn_Type()
)
cucsCommWsmanRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanRn.setStatus("current")
_CucsCommWsmanAdminState_Type = CucsCommAdminState
_CucsCommWsmanAdminState_Object = MibTableColumn
cucsCommWsmanAdminState = _CucsCommWsmanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 4),
    _CucsCommWsmanAdminState_Type()
)
cucsCommWsmanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanAdminState.setStatus("current")
_CucsCommWsmanDescr_Type = SnmpAdminString
_CucsCommWsmanDescr_Object = MibTableColumn
cucsCommWsmanDescr = _CucsCommWsmanDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 5),
    _CucsCommWsmanDescr_Type()
)
cucsCommWsmanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanDescr.setStatus("current")
_CucsCommWsmanIntId_Type = SnmpAdminString
_CucsCommWsmanIntId_Object = MibTableColumn
cucsCommWsmanIntId = _CucsCommWsmanIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 6),
    _CucsCommWsmanIntId_Type()
)
cucsCommWsmanIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanIntId.setStatus("current")
_CucsCommWsmanName_Type = SnmpAdminString
_CucsCommWsmanName_Object = MibTableColumn
cucsCommWsmanName = _CucsCommWsmanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 7),
    _CucsCommWsmanName_Type()
)
cucsCommWsmanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanName.setStatus("current")
_CucsCommWsmanPort_Type = Gauge32
_CucsCommWsmanPort_Object = MibTableColumn
cucsCommWsmanPort = _CucsCommWsmanPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 8),
    _CucsCommWsmanPort_Type()
)
cucsCommWsmanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanPort.setStatus("current")
_CucsCommWsmanProto_Type = CucsCommWebProto
_CucsCommWsmanProto_Object = MibTableColumn
cucsCommWsmanProto = _CucsCommWsmanProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 9),
    _CucsCommWsmanProto_Type()
)
cucsCommWsmanProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanProto.setStatus("current")
_CucsCommWsmanOperPort_Type = Gauge32
_CucsCommWsmanOperPort_Object = MibTableColumn
cucsCommWsmanOperPort = _CucsCommWsmanOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 10),
    _CucsCommWsmanOperPort_Type()
)
cucsCommWsmanOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanOperPort.setStatus("current")
_CucsCommWsmanPolicyLevel_Type = Gauge32
_CucsCommWsmanPolicyLevel_Object = MibTableColumn
cucsCommWsmanPolicyLevel = _CucsCommWsmanPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 11),
    _CucsCommWsmanPolicyLevel_Type()
)
cucsCommWsmanPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanPolicyLevel.setStatus("current")
_CucsCommWsmanPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommWsmanPolicyOwner_Object = MibTableColumn
cucsCommWsmanPolicyOwner = _CucsCommWsmanPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 23, 1, 12),
    _CucsCommWsmanPolicyOwner_Type()
)
cucsCommWsmanPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWsmanPolicyOwner.setStatus("current")
_CucsCommXmlClConnPolicyTable_Object = MibTable
cucsCommXmlClConnPolicyTable = _CucsCommXmlClConnPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24)
)
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyTable.setStatus("current")
_CucsCommXmlClConnPolicyEntry_Object = MibTableRow
cucsCommXmlClConnPolicyEntry = _CucsCommXmlClConnPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1)
)
cucsCommXmlClConnPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommXmlClConnPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyEntry.setStatus("current")
_CucsCommXmlClConnPolicyInstanceId_Type = CucsManagedObjectId
_CucsCommXmlClConnPolicyInstanceId_Object = MibTableColumn
cucsCommXmlClConnPolicyInstanceId = _CucsCommXmlClConnPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 1),
    _CucsCommXmlClConnPolicyInstanceId_Type()
)
cucsCommXmlClConnPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyInstanceId.setStatus("current")
_CucsCommXmlClConnPolicyDn_Type = CucsManagedObjectDn
_CucsCommXmlClConnPolicyDn_Object = MibTableColumn
cucsCommXmlClConnPolicyDn = _CucsCommXmlClConnPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 2),
    _CucsCommXmlClConnPolicyDn_Type()
)
cucsCommXmlClConnPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyDn.setStatus("current")
_CucsCommXmlClConnPolicyRn_Type = SnmpAdminString
_CucsCommXmlClConnPolicyRn_Object = MibTableColumn
cucsCommXmlClConnPolicyRn = _CucsCommXmlClConnPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 3),
    _CucsCommXmlClConnPolicyRn_Type()
)
cucsCommXmlClConnPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyRn.setStatus("current")
_CucsCommXmlClConnPolicyAdminState_Type = CucsCommAdminState
_CucsCommXmlClConnPolicyAdminState_Object = MibTableColumn
cucsCommXmlClConnPolicyAdminState = _CucsCommXmlClConnPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 4),
    _CucsCommXmlClConnPolicyAdminState_Type()
)
cucsCommXmlClConnPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyAdminState.setStatus("current")
_CucsCommXmlClConnPolicyClientType_Type = CucsCommXmlClConnPolicyClientType
_CucsCommXmlClConnPolicyClientType_Object = MibTableColumn
cucsCommXmlClConnPolicyClientType = _CucsCommXmlClConnPolicyClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 5),
    _CucsCommXmlClConnPolicyClientType_Type()
)
cucsCommXmlClConnPolicyClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyClientType.setStatus("current")
_CucsCommXmlClConnPolicyDescr_Type = SnmpAdminString
_CucsCommXmlClConnPolicyDescr_Object = MibTableColumn
cucsCommXmlClConnPolicyDescr = _CucsCommXmlClConnPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 6),
    _CucsCommXmlClConnPolicyDescr_Type()
)
cucsCommXmlClConnPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyDescr.setStatus("current")
_CucsCommXmlClConnPolicyIntId_Type = SnmpAdminString
_CucsCommXmlClConnPolicyIntId_Object = MibTableColumn
cucsCommXmlClConnPolicyIntId = _CucsCommXmlClConnPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 7),
    _CucsCommXmlClConnPolicyIntId_Type()
)
cucsCommXmlClConnPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyIntId.setStatus("current")
_CucsCommXmlClConnPolicyName_Type = SnmpAdminString
_CucsCommXmlClConnPolicyName_Object = MibTableColumn
cucsCommXmlClConnPolicyName = _CucsCommXmlClConnPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 8),
    _CucsCommXmlClConnPolicyName_Type()
)
cucsCommXmlClConnPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyName.setStatus("current")
_CucsCommXmlClConnPolicyPort_Type = Gauge32
_CucsCommXmlClConnPolicyPort_Object = MibTableColumn
cucsCommXmlClConnPolicyPort = _CucsCommXmlClConnPolicyPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 9),
    _CucsCommXmlClConnPolicyPort_Type()
)
cucsCommXmlClConnPolicyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyPort.setStatus("current")
_CucsCommXmlClConnPolicyProto_Type = CucsCommWebProto
_CucsCommXmlClConnPolicyProto_Object = MibTableColumn
cucsCommXmlClConnPolicyProto = _CucsCommXmlClConnPolicyProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 10),
    _CucsCommXmlClConnPolicyProto_Type()
)
cucsCommXmlClConnPolicyProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyProto.setStatus("current")
_CucsCommXmlClConnPolicyOperPort_Type = Gauge32
_CucsCommXmlClConnPolicyOperPort_Object = MibTableColumn
cucsCommXmlClConnPolicyOperPort = _CucsCommXmlClConnPolicyOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 11),
    _CucsCommXmlClConnPolicyOperPort_Type()
)
cucsCommXmlClConnPolicyOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyOperPort.setStatus("current")
_CucsCommXmlClConnPolicyPolicyLevel_Type = Gauge32
_CucsCommXmlClConnPolicyPolicyLevel_Object = MibTableColumn
cucsCommXmlClConnPolicyPolicyLevel = _CucsCommXmlClConnPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 12),
    _CucsCommXmlClConnPolicyPolicyLevel_Type()
)
cucsCommXmlClConnPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyPolicyLevel.setStatus("current")
_CucsCommXmlClConnPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommXmlClConnPolicyPolicyOwner_Object = MibTableColumn
cucsCommXmlClConnPolicyPolicyOwner = _CucsCommXmlClConnPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 24, 1, 13),
    _CucsCommXmlClConnPolicyPolicyOwner_Type()
)
cucsCommXmlClConnPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommXmlClConnPolicyPolicyOwner.setStatus("current")
_CucsCommShellSvcLimitsTable_Object = MibTable
cucsCommShellSvcLimitsTable = _CucsCommShellSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25)
)
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsTable.setStatus("current")
_CucsCommShellSvcLimitsEntry_Object = MibTableRow
cucsCommShellSvcLimitsEntry = _CucsCommShellSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1)
)
cucsCommShellSvcLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommShellSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsEntry.setStatus("current")
_CucsCommShellSvcLimitsInstanceId_Type = CucsManagedObjectId
_CucsCommShellSvcLimitsInstanceId_Object = MibTableColumn
cucsCommShellSvcLimitsInstanceId = _CucsCommShellSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 1),
    _CucsCommShellSvcLimitsInstanceId_Type()
)
cucsCommShellSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsInstanceId.setStatus("current")
_CucsCommShellSvcLimitsDn_Type = CucsManagedObjectDn
_CucsCommShellSvcLimitsDn_Object = MibTableColumn
cucsCommShellSvcLimitsDn = _CucsCommShellSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 2),
    _CucsCommShellSvcLimitsDn_Type()
)
cucsCommShellSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsDn.setStatus("current")
_CucsCommShellSvcLimitsRn_Type = SnmpAdminString
_CucsCommShellSvcLimitsRn_Object = MibTableColumn
cucsCommShellSvcLimitsRn = _CucsCommShellSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 3),
    _CucsCommShellSvcLimitsRn_Type()
)
cucsCommShellSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsRn.setStatus("current")
_CucsCommShellSvcLimitsDescr_Type = SnmpAdminString
_CucsCommShellSvcLimitsDescr_Object = MibTableColumn
cucsCommShellSvcLimitsDescr = _CucsCommShellSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 4),
    _CucsCommShellSvcLimitsDescr_Type()
)
cucsCommShellSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsDescr.setStatus("current")
_CucsCommShellSvcLimitsIntId_Type = SnmpAdminString
_CucsCommShellSvcLimitsIntId_Object = MibTableColumn
cucsCommShellSvcLimitsIntId = _CucsCommShellSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 5),
    _CucsCommShellSvcLimitsIntId_Type()
)
cucsCommShellSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsIntId.setStatus("current")
_CucsCommShellSvcLimitsName_Type = SnmpAdminString
_CucsCommShellSvcLimitsName_Object = MibTableColumn
cucsCommShellSvcLimitsName = _CucsCommShellSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 6),
    _CucsCommShellSvcLimitsName_Type()
)
cucsCommShellSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsName.setStatus("current")
_CucsCommShellSvcLimitsSessionsPerUser_Type = Gauge32
_CucsCommShellSvcLimitsSessionsPerUser_Object = MibTableColumn
cucsCommShellSvcLimitsSessionsPerUser = _CucsCommShellSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 7),
    _CucsCommShellSvcLimitsSessionsPerUser_Type()
)
cucsCommShellSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsSessionsPerUser.setStatus("current")
_CucsCommShellSvcLimitsTotalSessions_Type = Gauge32
_CucsCommShellSvcLimitsTotalSessions_Object = MibTableColumn
cucsCommShellSvcLimitsTotalSessions = _CucsCommShellSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 8),
    _CucsCommShellSvcLimitsTotalSessions_Type()
)
cucsCommShellSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsTotalSessions.setStatus("current")
_CucsCommShellSvcLimitsPolicyLevel_Type = Gauge32
_CucsCommShellSvcLimitsPolicyLevel_Object = MibTableColumn
cucsCommShellSvcLimitsPolicyLevel = _CucsCommShellSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 9),
    _CucsCommShellSvcLimitsPolicyLevel_Type()
)
cucsCommShellSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsPolicyLevel.setStatus("current")
_CucsCommShellSvcLimitsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommShellSvcLimitsPolicyOwner_Object = MibTableColumn
cucsCommShellSvcLimitsPolicyOwner = _CucsCommShellSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 25, 1, 10),
    _CucsCommShellSvcLimitsPolicyOwner_Type()
)
cucsCommShellSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommShellSvcLimitsPolicyOwner.setStatus("current")
_CucsCommSyslogSourceTable_Object = MibTable
cucsCommSyslogSourceTable = _CucsCommSyslogSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26)
)
if mibBuilder.loadTexts:
    cucsCommSyslogSourceTable.setStatus("current")
_CucsCommSyslogSourceEntry_Object = MibTableRow
cucsCommSyslogSourceEntry = _CucsCommSyslogSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1)
)
cucsCommSyslogSourceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSyslogSourceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSyslogSourceEntry.setStatus("current")
_CucsCommSyslogSourceInstanceId_Type = CucsManagedObjectId
_CucsCommSyslogSourceInstanceId_Object = MibTableColumn
cucsCommSyslogSourceInstanceId = _CucsCommSyslogSourceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 1),
    _CucsCommSyslogSourceInstanceId_Type()
)
cucsCommSyslogSourceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceInstanceId.setStatus("current")
_CucsCommSyslogSourceDn_Type = CucsManagedObjectDn
_CucsCommSyslogSourceDn_Object = MibTableColumn
cucsCommSyslogSourceDn = _CucsCommSyslogSourceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 2),
    _CucsCommSyslogSourceDn_Type()
)
cucsCommSyslogSourceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceDn.setStatus("current")
_CucsCommSyslogSourceRn_Type = SnmpAdminString
_CucsCommSyslogSourceRn_Object = MibTableColumn
cucsCommSyslogSourceRn = _CucsCommSyslogSourceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 3),
    _CucsCommSyslogSourceRn_Type()
)
cucsCommSyslogSourceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceRn.setStatus("current")
_CucsCommSyslogSourceAudits_Type = CucsCommSyslogSourceAudits
_CucsCommSyslogSourceAudits_Object = MibTableColumn
cucsCommSyslogSourceAudits = _CucsCommSyslogSourceAudits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 4),
    _CucsCommSyslogSourceAudits_Type()
)
cucsCommSyslogSourceAudits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceAudits.setStatus("current")
_CucsCommSyslogSourceDescr_Type = SnmpAdminString
_CucsCommSyslogSourceDescr_Object = MibTableColumn
cucsCommSyslogSourceDescr = _CucsCommSyslogSourceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 5),
    _CucsCommSyslogSourceDescr_Type()
)
cucsCommSyslogSourceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceDescr.setStatus("current")
_CucsCommSyslogSourceEvents_Type = CucsCommSyslogSourceEvents
_CucsCommSyslogSourceEvents_Object = MibTableColumn
cucsCommSyslogSourceEvents = _CucsCommSyslogSourceEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 6),
    _CucsCommSyslogSourceEvents_Type()
)
cucsCommSyslogSourceEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceEvents.setStatus("current")
_CucsCommSyslogSourceFaults_Type = CucsCommSyslogSourceFaults
_CucsCommSyslogSourceFaults_Object = MibTableColumn
cucsCommSyslogSourceFaults = _CucsCommSyslogSourceFaults_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 7),
    _CucsCommSyslogSourceFaults_Type()
)
cucsCommSyslogSourceFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceFaults.setStatus("current")
_CucsCommSyslogSourceName_Type = SnmpAdminString
_CucsCommSyslogSourceName_Object = MibTableColumn
cucsCommSyslogSourceName = _CucsCommSyslogSourceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 26, 1, 9),
    _CucsCommSyslogSourceName_Type()
)
cucsCommSyslogSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSyslogSourceName.setStatus("current")
_CucsCommWebSvcLimitsTable_Object = MibTable
cucsCommWebSvcLimitsTable = _CucsCommWebSvcLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27)
)
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsTable.setStatus("current")
_CucsCommWebSvcLimitsEntry_Object = MibTableRow
cucsCommWebSvcLimitsEntry = _CucsCommWebSvcLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1)
)
cucsCommWebSvcLimitsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommWebSvcLimitsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsEntry.setStatus("current")
_CucsCommWebSvcLimitsInstanceId_Type = CucsManagedObjectId
_CucsCommWebSvcLimitsInstanceId_Object = MibTableColumn
cucsCommWebSvcLimitsInstanceId = _CucsCommWebSvcLimitsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 1),
    _CucsCommWebSvcLimitsInstanceId_Type()
)
cucsCommWebSvcLimitsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsInstanceId.setStatus("current")
_CucsCommWebSvcLimitsDn_Type = CucsManagedObjectDn
_CucsCommWebSvcLimitsDn_Object = MibTableColumn
cucsCommWebSvcLimitsDn = _CucsCommWebSvcLimitsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 2),
    _CucsCommWebSvcLimitsDn_Type()
)
cucsCommWebSvcLimitsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsDn.setStatus("current")
_CucsCommWebSvcLimitsRn_Type = SnmpAdminString
_CucsCommWebSvcLimitsRn_Object = MibTableColumn
cucsCommWebSvcLimitsRn = _CucsCommWebSvcLimitsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 3),
    _CucsCommWebSvcLimitsRn_Type()
)
cucsCommWebSvcLimitsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsRn.setStatus("current")
_CucsCommWebSvcLimitsDescr_Type = SnmpAdminString
_CucsCommWebSvcLimitsDescr_Object = MibTableColumn
cucsCommWebSvcLimitsDescr = _CucsCommWebSvcLimitsDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 4),
    _CucsCommWebSvcLimitsDescr_Type()
)
cucsCommWebSvcLimitsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsDescr.setStatus("current")
_CucsCommWebSvcLimitsIntId_Type = SnmpAdminString
_CucsCommWebSvcLimitsIntId_Object = MibTableColumn
cucsCommWebSvcLimitsIntId = _CucsCommWebSvcLimitsIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 5),
    _CucsCommWebSvcLimitsIntId_Type()
)
cucsCommWebSvcLimitsIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsIntId.setStatus("current")
_CucsCommWebSvcLimitsName_Type = SnmpAdminString
_CucsCommWebSvcLimitsName_Object = MibTableColumn
cucsCommWebSvcLimitsName = _CucsCommWebSvcLimitsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 6),
    _CucsCommWebSvcLimitsName_Type()
)
cucsCommWebSvcLimitsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsName.setStatus("current")
_CucsCommWebSvcLimitsSessionsPerUser_Type = Gauge32
_CucsCommWebSvcLimitsSessionsPerUser_Object = MibTableColumn
cucsCommWebSvcLimitsSessionsPerUser = _CucsCommWebSvcLimitsSessionsPerUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 7),
    _CucsCommWebSvcLimitsSessionsPerUser_Type()
)
cucsCommWebSvcLimitsSessionsPerUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsSessionsPerUser.setStatus("current")
_CucsCommWebSvcLimitsTotalSessions_Type = Gauge32
_CucsCommWebSvcLimitsTotalSessions_Object = MibTableColumn
cucsCommWebSvcLimitsTotalSessions = _CucsCommWebSvcLimitsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 8),
    _CucsCommWebSvcLimitsTotalSessions_Type()
)
cucsCommWebSvcLimitsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsTotalSessions.setStatus("current")
_CucsCommWebSvcLimitsPolicyLevel_Type = Gauge32
_CucsCommWebSvcLimitsPolicyLevel_Object = MibTableColumn
cucsCommWebSvcLimitsPolicyLevel = _CucsCommWebSvcLimitsPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 9),
    _CucsCommWebSvcLimitsPolicyLevel_Type()
)
cucsCommWebSvcLimitsPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsPolicyLevel.setStatus("current")
_CucsCommWebSvcLimitsPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommWebSvcLimitsPolicyOwner_Object = MibTableColumn
cucsCommWebSvcLimitsPolicyOwner = _CucsCommWebSvcLimitsPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 27, 1, 10),
    _CucsCommWebSvcLimitsPolicyOwner_Type()
)
cucsCommWebSvcLimitsPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommWebSvcLimitsPolicyOwner.setStatus("current")
_CucsCommSvcEpFsmTable_Object = MibTable
cucsCommSvcEpFsmTable = _CucsCommSvcEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28)
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmTable.setStatus("current")
_CucsCommSvcEpFsmEntry_Object = MibTableRow
cucsCommSvcEpFsmEntry = _CucsCommSvcEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1)
)
cucsCommSvcEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSvcEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmEntry.setStatus("current")
_CucsCommSvcEpFsmInstanceId_Type = CucsManagedObjectId
_CucsCommSvcEpFsmInstanceId_Object = MibTableColumn
cucsCommSvcEpFsmInstanceId = _CucsCommSvcEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 1),
    _CucsCommSvcEpFsmInstanceId_Type()
)
cucsCommSvcEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmInstanceId.setStatus("current")
_CucsCommSvcEpFsmDn_Type = CucsManagedObjectDn
_CucsCommSvcEpFsmDn_Object = MibTableColumn
cucsCommSvcEpFsmDn = _CucsCommSvcEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 2),
    _CucsCommSvcEpFsmDn_Type()
)
cucsCommSvcEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmDn.setStatus("current")
_CucsCommSvcEpFsmRn_Type = SnmpAdminString
_CucsCommSvcEpFsmRn_Object = MibTableColumn
cucsCommSvcEpFsmRn = _CucsCommSvcEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 3),
    _CucsCommSvcEpFsmRn_Type()
)
cucsCommSvcEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRn.setStatus("current")
_CucsCommSvcEpFsmCompletionTime_Type = DateAndTime
_CucsCommSvcEpFsmCompletionTime_Object = MibTableColumn
cucsCommSvcEpFsmCompletionTime = _CucsCommSvcEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 4),
    _CucsCommSvcEpFsmCompletionTime_Type()
)
cucsCommSvcEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmCompletionTime.setStatus("current")
_CucsCommSvcEpFsmCurrentFsm_Type = CucsCommSvcEpFsmCurrentFsm
_CucsCommSvcEpFsmCurrentFsm_Object = MibTableColumn
cucsCommSvcEpFsmCurrentFsm = _CucsCommSvcEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 5),
    _CucsCommSvcEpFsmCurrentFsm_Type()
)
cucsCommSvcEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmCurrentFsm.setStatus("current")
_CucsCommSvcEpFsmDescrData_Type = SnmpAdminString
_CucsCommSvcEpFsmDescrData_Object = MibTableColumn
cucsCommSvcEpFsmDescrData = _CucsCommSvcEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 6),
    _CucsCommSvcEpFsmDescrData_Type()
)
cucsCommSvcEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmDescrData.setStatus("current")
_CucsCommSvcEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsCommSvcEpFsmFsmStatus_Object = MibTableColumn
cucsCommSvcEpFsmFsmStatus = _CucsCommSvcEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 7),
    _CucsCommSvcEpFsmFsmStatus_Type()
)
cucsCommSvcEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmFsmStatus.setStatus("current")
_CucsCommSvcEpFsmProgress_Type = Gauge32
_CucsCommSvcEpFsmProgress_Object = MibTableColumn
cucsCommSvcEpFsmProgress = _CucsCommSvcEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 8),
    _CucsCommSvcEpFsmProgress_Type()
)
cucsCommSvcEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmProgress.setStatus("current")
_CucsCommSvcEpFsmRmtErrCode_Type = Gauge32
_CucsCommSvcEpFsmRmtErrCode_Object = MibTableColumn
cucsCommSvcEpFsmRmtErrCode = _CucsCommSvcEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 9),
    _CucsCommSvcEpFsmRmtErrCode_Type()
)
cucsCommSvcEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtErrCode.setStatus("current")
_CucsCommSvcEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsCommSvcEpFsmRmtErrDescr_Object = MibTableColumn
cucsCommSvcEpFsmRmtErrDescr = _CucsCommSvcEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 10),
    _CucsCommSvcEpFsmRmtErrDescr_Type()
)
cucsCommSvcEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtErrDescr.setStatus("current")
_CucsCommSvcEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsCommSvcEpFsmRmtRslt_Object = MibTableColumn
cucsCommSvcEpFsmRmtRslt = _CucsCommSvcEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 28, 1, 11),
    _CucsCommSvcEpFsmRmtRslt_Type()
)
cucsCommSvcEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmRmtRslt.setStatus("current")
_CucsCommSvcEpFsmStageTable_Object = MibTable
cucsCommSvcEpFsmStageTable = _CucsCommSvcEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29)
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageTable.setStatus("current")
_CucsCommSvcEpFsmStageEntry_Object = MibTableRow
cucsCommSvcEpFsmStageEntry = _CucsCommSvcEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1)
)
cucsCommSvcEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSvcEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageEntry.setStatus("current")
_CucsCommSvcEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsCommSvcEpFsmStageInstanceId_Object = MibTableColumn
cucsCommSvcEpFsmStageInstanceId = _CucsCommSvcEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 1),
    _CucsCommSvcEpFsmStageInstanceId_Type()
)
cucsCommSvcEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageInstanceId.setStatus("current")
_CucsCommSvcEpFsmStageDn_Type = CucsManagedObjectDn
_CucsCommSvcEpFsmStageDn_Object = MibTableColumn
cucsCommSvcEpFsmStageDn = _CucsCommSvcEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 2),
    _CucsCommSvcEpFsmStageDn_Type()
)
cucsCommSvcEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageDn.setStatus("current")
_CucsCommSvcEpFsmStageRn_Type = SnmpAdminString
_CucsCommSvcEpFsmStageRn_Object = MibTableColumn
cucsCommSvcEpFsmStageRn = _CucsCommSvcEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 3),
    _CucsCommSvcEpFsmStageRn_Type()
)
cucsCommSvcEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageRn.setStatus("current")
_CucsCommSvcEpFsmStageDescrData_Type = SnmpAdminString
_CucsCommSvcEpFsmStageDescrData_Object = MibTableColumn
cucsCommSvcEpFsmStageDescrData = _CucsCommSvcEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 4),
    _CucsCommSvcEpFsmStageDescrData_Type()
)
cucsCommSvcEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageDescrData.setStatus("current")
_CucsCommSvcEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsCommSvcEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsCommSvcEpFsmStageLastUpdateTime = _CucsCommSvcEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 5),
    _CucsCommSvcEpFsmStageLastUpdateTime_Type()
)
cucsCommSvcEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageLastUpdateTime.setStatus("current")
_CucsCommSvcEpFsmStageName_Type = CucsCommSvcEpFsmStageName
_CucsCommSvcEpFsmStageName_Object = MibTableColumn
cucsCommSvcEpFsmStageName = _CucsCommSvcEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 6),
    _CucsCommSvcEpFsmStageName_Type()
)
cucsCommSvcEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageName.setStatus("current")
_CucsCommSvcEpFsmStageOrder_Type = Gauge32
_CucsCommSvcEpFsmStageOrder_Object = MibTableColumn
cucsCommSvcEpFsmStageOrder = _CucsCommSvcEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 7),
    _CucsCommSvcEpFsmStageOrder_Type()
)
cucsCommSvcEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageOrder.setStatus("current")
_CucsCommSvcEpFsmStageRetry_Type = Gauge32
_CucsCommSvcEpFsmStageRetry_Object = MibTableColumn
cucsCommSvcEpFsmStageRetry = _CucsCommSvcEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 8),
    _CucsCommSvcEpFsmStageRetry_Type()
)
cucsCommSvcEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageRetry.setStatus("current")
_CucsCommSvcEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsCommSvcEpFsmStageStageStatus_Object = MibTableColumn
cucsCommSvcEpFsmStageStageStatus = _CucsCommSvcEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 29, 1, 9),
    _CucsCommSvcEpFsmStageStageStatus_Type()
)
cucsCommSvcEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcEpFsmStageStageStatus.setStatus("current")
_CucsCommCimcWebServiceTable_Object = MibTable
cucsCommCimcWebServiceTable = _CucsCommCimcWebServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30)
)
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceTable.setStatus("current")
_CucsCommCimcWebServiceEntry_Object = MibTableRow
cucsCommCimcWebServiceEntry = _CucsCommCimcWebServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1)
)
cucsCommCimcWebServiceEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommCimcWebServiceInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceEntry.setStatus("current")
_CucsCommCimcWebServiceInstanceId_Type = CucsManagedObjectId
_CucsCommCimcWebServiceInstanceId_Object = MibTableColumn
cucsCommCimcWebServiceInstanceId = _CucsCommCimcWebServiceInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 1),
    _CucsCommCimcWebServiceInstanceId_Type()
)
cucsCommCimcWebServiceInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceInstanceId.setStatus("current")
_CucsCommCimcWebServiceDn_Type = CucsManagedObjectDn
_CucsCommCimcWebServiceDn_Object = MibTableColumn
cucsCommCimcWebServiceDn = _CucsCommCimcWebServiceDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 2),
    _CucsCommCimcWebServiceDn_Type()
)
cucsCommCimcWebServiceDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceDn.setStatus("current")
_CucsCommCimcWebServiceRn_Type = SnmpAdminString
_CucsCommCimcWebServiceRn_Object = MibTableColumn
cucsCommCimcWebServiceRn = _CucsCommCimcWebServiceRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 3),
    _CucsCommCimcWebServiceRn_Type()
)
cucsCommCimcWebServiceRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceRn.setStatus("current")
_CucsCommCimcWebServiceAdminState_Type = CucsCommAdminState
_CucsCommCimcWebServiceAdminState_Object = MibTableColumn
cucsCommCimcWebServiceAdminState = _CucsCommCimcWebServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 4),
    _CucsCommCimcWebServiceAdminState_Type()
)
cucsCommCimcWebServiceAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceAdminState.setStatus("current")
_CucsCommCimcWebServiceDescr_Type = SnmpAdminString
_CucsCommCimcWebServiceDescr_Object = MibTableColumn
cucsCommCimcWebServiceDescr = _CucsCommCimcWebServiceDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 5),
    _CucsCommCimcWebServiceDescr_Type()
)
cucsCommCimcWebServiceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceDescr.setStatus("current")
_CucsCommCimcWebServiceIntId_Type = SnmpAdminString
_CucsCommCimcWebServiceIntId_Object = MibTableColumn
cucsCommCimcWebServiceIntId = _CucsCommCimcWebServiceIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 6),
    _CucsCommCimcWebServiceIntId_Type()
)
cucsCommCimcWebServiceIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceIntId.setStatus("current")
_CucsCommCimcWebServiceName_Type = SnmpAdminString
_CucsCommCimcWebServiceName_Object = MibTableColumn
cucsCommCimcWebServiceName = _CucsCommCimcWebServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 7),
    _CucsCommCimcWebServiceName_Type()
)
cucsCommCimcWebServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceName.setStatus("current")
_CucsCommCimcWebServiceOperPort_Type = Gauge32
_CucsCommCimcWebServiceOperPort_Object = MibTableColumn
cucsCommCimcWebServiceOperPort = _CucsCommCimcWebServiceOperPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 8),
    _CucsCommCimcWebServiceOperPort_Type()
)
cucsCommCimcWebServiceOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceOperPort.setStatus("current")
_CucsCommCimcWebServicePolicyLevel_Type = Gauge32
_CucsCommCimcWebServicePolicyLevel_Object = MibTableColumn
cucsCommCimcWebServicePolicyLevel = _CucsCommCimcWebServicePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 9),
    _CucsCommCimcWebServicePolicyLevel_Type()
)
cucsCommCimcWebServicePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServicePolicyLevel.setStatus("current")
_CucsCommCimcWebServicePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommCimcWebServicePolicyOwner_Object = MibTableColumn
cucsCommCimcWebServicePolicyOwner = _CucsCommCimcWebServicePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 10),
    _CucsCommCimcWebServicePolicyOwner_Type()
)
cucsCommCimcWebServicePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServicePolicyOwner.setStatus("current")
_CucsCommCimcWebServicePort_Type = Gauge32
_CucsCommCimcWebServicePort_Object = MibTableColumn
cucsCommCimcWebServicePort = _CucsCommCimcWebServicePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 11),
    _CucsCommCimcWebServicePort_Type()
)
cucsCommCimcWebServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServicePort.setStatus("current")
_CucsCommCimcWebServiceProto_Type = CucsCommWebProto
_CucsCommCimcWebServiceProto_Object = MibTableColumn
cucsCommCimcWebServiceProto = _CucsCommCimcWebServiceProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 30, 1, 12),
    _CucsCommCimcWebServiceProto_Type()
)
cucsCommCimcWebServiceProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommCimcWebServiceProto.setStatus("current")
_CucsCommLocaleTable_Object = MibTable
cucsCommLocaleTable = _CucsCommLocaleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31)
)
if mibBuilder.loadTexts:
    cucsCommLocaleTable.setStatus("current")
_CucsCommLocaleEntry_Object = MibTableRow
cucsCommLocaleEntry = _CucsCommLocaleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1)
)
cucsCommLocaleEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommLocaleInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommLocaleEntry.setStatus("current")
_CucsCommLocaleInstanceId_Type = CucsManagedObjectId
_CucsCommLocaleInstanceId_Object = MibTableColumn
cucsCommLocaleInstanceId = _CucsCommLocaleInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1, 1),
    _CucsCommLocaleInstanceId_Type()
)
cucsCommLocaleInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommLocaleInstanceId.setStatus("current")
_CucsCommLocaleDn_Type = CucsManagedObjectDn
_CucsCommLocaleDn_Object = MibTableColumn
cucsCommLocaleDn = _CucsCommLocaleDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1, 2),
    _CucsCommLocaleDn_Type()
)
cucsCommLocaleDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommLocaleDn.setStatus("current")
_CucsCommLocaleRn_Type = SnmpAdminString
_CucsCommLocaleRn_Object = MibTableColumn
cucsCommLocaleRn = _CucsCommLocaleRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1, 3),
    _CucsCommLocaleRn_Type()
)
cucsCommLocaleRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommLocaleRn.setStatus("current")
_CucsCommLocaleDescr_Type = SnmpAdminString
_CucsCommLocaleDescr_Object = MibTableColumn
cucsCommLocaleDescr = _CucsCommLocaleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1, 4),
    _CucsCommLocaleDescr_Type()
)
cucsCommLocaleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommLocaleDescr.setStatus("current")
_CucsCommLocaleName_Type = SnmpAdminString
_CucsCommLocaleName_Object = MibTableColumn
cucsCommLocaleName = _CucsCommLocaleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 31, 1, 5),
    _CucsCommLocaleName_Type()
)
cucsCommLocaleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommLocaleName.setStatus("current")
_CucsCommSvcPolicyTable_Object = MibTable
cucsCommSvcPolicyTable = _CucsCommSvcPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32)
)
if mibBuilder.loadTexts:
    cucsCommSvcPolicyTable.setStatus("current")
_CucsCommSvcPolicyEntry_Object = MibTableRow
cucsCommSvcPolicyEntry = _CucsCommSvcPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1)
)
cucsCommSvcPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-COMM-MIB", "cucsCommSvcPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsCommSvcPolicyEntry.setStatus("current")
_CucsCommSvcPolicyInstanceId_Type = CucsManagedObjectId
_CucsCommSvcPolicyInstanceId_Object = MibTableColumn
cucsCommSvcPolicyInstanceId = _CucsCommSvcPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 1),
    _CucsCommSvcPolicyInstanceId_Type()
)
cucsCommSvcPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyInstanceId.setStatus("current")
_CucsCommSvcPolicyDn_Type = CucsManagedObjectDn
_CucsCommSvcPolicyDn_Object = MibTableColumn
cucsCommSvcPolicyDn = _CucsCommSvcPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 2),
    _CucsCommSvcPolicyDn_Type()
)
cucsCommSvcPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyDn.setStatus("current")
_CucsCommSvcPolicyRn_Type = SnmpAdminString
_CucsCommSvcPolicyRn_Object = MibTableColumn
cucsCommSvcPolicyRn = _CucsCommSvcPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 3),
    _CucsCommSvcPolicyRn_Type()
)
cucsCommSvcPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyRn.setStatus("current")
_CucsCommSvcPolicyDescr_Type = SnmpAdminString
_CucsCommSvcPolicyDescr_Object = MibTableColumn
cucsCommSvcPolicyDescr = _CucsCommSvcPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 4),
    _CucsCommSvcPolicyDescr_Type()
)
cucsCommSvcPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyDescr.setStatus("current")
_CucsCommSvcPolicyIntId_Type = SnmpAdminString
_CucsCommSvcPolicyIntId_Object = MibTableColumn
cucsCommSvcPolicyIntId = _CucsCommSvcPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 5),
    _CucsCommSvcPolicyIntId_Type()
)
cucsCommSvcPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyIntId.setStatus("current")
_CucsCommSvcPolicyName_Type = SnmpAdminString
_CucsCommSvcPolicyName_Object = MibTableColumn
cucsCommSvcPolicyName = _CucsCommSvcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 6),
    _CucsCommSvcPolicyName_Type()
)
cucsCommSvcPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyName.setStatus("current")
_CucsCommSvcPolicyPolicyLevel_Type = Gauge32
_CucsCommSvcPolicyPolicyLevel_Object = MibTableColumn
cucsCommSvcPolicyPolicyLevel = _CucsCommSvcPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 7),
    _CucsCommSvcPolicyPolicyLevel_Type()
)
cucsCommSvcPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyPolicyLevel.setStatus("current")
_CucsCommSvcPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsCommSvcPolicyPolicyOwner_Object = MibTableColumn
cucsCommSvcPolicyPolicyOwner = _CucsCommSvcPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 8, 32, 1, 8),
    _CucsCommSvcPolicyPolicyOwner_Type()
)
cucsCommSvcPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsCommSvcPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-COMM-MIB",
    **{"cucsCommObjects": cucsCommObjects,
       "cucsCommCimxmlTable": cucsCommCimxmlTable,
       "cucsCommCimxmlEntry": cucsCommCimxmlEntry,
       "cucsCommCimxmlInstanceId": cucsCommCimxmlInstanceId,
       "cucsCommCimxmlDn": cucsCommCimxmlDn,
       "cucsCommCimxmlRn": cucsCommCimxmlRn,
       "cucsCommCimxmlAdminState": cucsCommCimxmlAdminState,
       "cucsCommCimxmlDescr": cucsCommCimxmlDescr,
       "cucsCommCimxmlIntId": cucsCommCimxmlIntId,
       "cucsCommCimxmlName": cucsCommCimxmlName,
       "cucsCommCimxmlPort": cucsCommCimxmlPort,
       "cucsCommCimxmlProto": cucsCommCimxmlProto,
       "cucsCommCimxmlOperPort": cucsCommCimxmlOperPort,
       "cucsCommCimxmlPolicyLevel": cucsCommCimxmlPolicyLevel,
       "cucsCommCimxmlPolicyOwner": cucsCommCimxmlPolicyOwner,
       "cucsCommDateTimeTable": cucsCommDateTimeTable,
       "cucsCommDateTimeEntry": cucsCommDateTimeEntry,
       "cucsCommDateTimeInstanceId": cucsCommDateTimeInstanceId,
       "cucsCommDateTimeDn": cucsCommDateTimeDn,
       "cucsCommDateTimeRn": cucsCommDateTimeRn,
       "cucsCommDateTimeAdminState": cucsCommDateTimeAdminState,
       "cucsCommDateTimeDate": cucsCommDateTimeDate,
       "cucsCommDateTimeDescr": cucsCommDateTimeDescr,
       "cucsCommDateTimeIntId": cucsCommDateTimeIntId,
       "cucsCommDateTimeName": cucsCommDateTimeName,
       "cucsCommDateTimePort": cucsCommDateTimePort,
       "cucsCommDateTimeProto": cucsCommDateTimeProto,
       "cucsCommDateTimeTimezone": cucsCommDateTimeTimezone,
       "cucsCommDateTimeConfigState": cucsCommDateTimeConfigState,
       "cucsCommDateTimeOperPort": cucsCommDateTimeOperPort,
       "cucsCommDateTimeOperTimezone": cucsCommDateTimeOperTimezone,
       "cucsCommDateTimePolicyLevel": cucsCommDateTimePolicyLevel,
       "cucsCommDateTimePolicyOwner": cucsCommDateTimePolicyOwner,
       "cucsCommDnsTable": cucsCommDnsTable,
       "cucsCommDnsEntry": cucsCommDnsEntry,
       "cucsCommDnsInstanceId": cucsCommDnsInstanceId,
       "cucsCommDnsDn": cucsCommDnsDn,
       "cucsCommDnsRn": cucsCommDnsRn,
       "cucsCommDnsAdminState": cucsCommDnsAdminState,
       "cucsCommDnsDescr": cucsCommDnsDescr,
       "cucsCommDnsDomain": cucsCommDnsDomain,
       "cucsCommDnsIntId": cucsCommDnsIntId,
       "cucsCommDnsName": cucsCommDnsName,
       "cucsCommDnsPort": cucsCommDnsPort,
       "cucsCommDnsProto": cucsCommDnsProto,
       "cucsCommDnsOperPort": cucsCommDnsOperPort,
       "cucsCommDnsPolicyLevel": cucsCommDnsPolicyLevel,
       "cucsCommDnsPolicyOwner": cucsCommDnsPolicyOwner,
       "cucsCommDnsProviderTable": cucsCommDnsProviderTable,
       "cucsCommDnsProviderEntry": cucsCommDnsProviderEntry,
       "cucsCommDnsProviderInstanceId": cucsCommDnsProviderInstanceId,
       "cucsCommDnsProviderDn": cucsCommDnsProviderDn,
       "cucsCommDnsProviderRn": cucsCommDnsProviderRn,
       "cucsCommDnsProviderAdminState": cucsCommDnsProviderAdminState,
       "cucsCommDnsProviderDescr": cucsCommDnsProviderDescr,
       "cucsCommDnsProviderHostname": cucsCommDnsProviderHostname,
       "cucsCommDnsProviderName": cucsCommDnsProviderName,
       "cucsCommEvtChannelTable": cucsCommEvtChannelTable,
       "cucsCommEvtChannelEntry": cucsCommEvtChannelEntry,
       "cucsCommEvtChannelInstanceId": cucsCommEvtChannelInstanceId,
       "cucsCommEvtChannelDn": cucsCommEvtChannelDn,
       "cucsCommEvtChannelRn": cucsCommEvtChannelRn,
       "cucsCommEvtChannelChannelState": cucsCommEvtChannelChannelState,
       "cucsCommEvtChannelDescr": cucsCommEvtChannelDescr,
       "cucsCommEvtChannelIntId": cucsCommEvtChannelIntId,
       "cucsCommEvtChannelName": cucsCommEvtChannelName,
       "cucsCommEvtChannelPolicyLevel": cucsCommEvtChannelPolicyLevel,
       "cucsCommEvtChannelPolicyOwner": cucsCommEvtChannelPolicyOwner,
       "cucsCommHttpTable": cucsCommHttpTable,
       "cucsCommHttpEntry": cucsCommHttpEntry,
       "cucsCommHttpInstanceId": cucsCommHttpInstanceId,
       "cucsCommHttpDn": cucsCommHttpDn,
       "cucsCommHttpRn": cucsCommHttpRn,
       "cucsCommHttpAdminState": cucsCommHttpAdminState,
       "cucsCommHttpDescr": cucsCommHttpDescr,
       "cucsCommHttpIntId": cucsCommHttpIntId,
       "cucsCommHttpName": cucsCommHttpName,
       "cucsCommHttpPort": cucsCommHttpPort,
       "cucsCommHttpProto": cucsCommHttpProto,
       "cucsCommHttpRedirectState": cucsCommHttpRedirectState,
       "cucsCommHttpOperPort": cucsCommHttpOperPort,
       "cucsCommHttpPolicyLevel": cucsCommHttpPolicyLevel,
       "cucsCommHttpPolicyOwner": cucsCommHttpPolicyOwner,
       "cucsCommHttpsTable": cucsCommHttpsTable,
       "cucsCommHttpsEntry": cucsCommHttpsEntry,
       "cucsCommHttpsInstanceId": cucsCommHttpsInstanceId,
       "cucsCommHttpsDn": cucsCommHttpsDn,
       "cucsCommHttpsRn": cucsCommHttpsRn,
       "cucsCommHttpsAdminState": cucsCommHttpsAdminState,
       "cucsCommHttpsDescr": cucsCommHttpsDescr,
       "cucsCommHttpsIntId": cucsCommHttpsIntId,
       "cucsCommHttpsKeyRing": cucsCommHttpsKeyRing,
       "cucsCommHttpsName": cucsCommHttpsName,
       "cucsCommHttpsPort": cucsCommHttpsPort,
       "cucsCommHttpsProto": cucsCommHttpsProto,
       "cucsCommHttpsCipherSuite": cucsCommHttpsCipherSuite,
       "cucsCommHttpsCipherSuiteMode": cucsCommHttpsCipherSuiteMode,
       "cucsCommHttpsOperPort": cucsCommHttpsOperPort,
       "cucsCommHttpsPolicyLevel": cucsCommHttpsPolicyLevel,
       "cucsCommHttpsPolicyOwner": cucsCommHttpsPolicyOwner,
       "cucsCommNtpProviderTable": cucsCommNtpProviderTable,
       "cucsCommNtpProviderEntry": cucsCommNtpProviderEntry,
       "cucsCommNtpProviderInstanceId": cucsCommNtpProviderInstanceId,
       "cucsCommNtpProviderDn": cucsCommNtpProviderDn,
       "cucsCommNtpProviderRn": cucsCommNtpProviderRn,
       "cucsCommNtpProviderAdminState": cucsCommNtpProviderAdminState,
       "cucsCommNtpProviderDescr": cucsCommNtpProviderDescr,
       "cucsCommNtpProviderHostname": cucsCommNtpProviderHostname,
       "cucsCommNtpProviderName": cucsCommNtpProviderName,
       "cucsCommSmashCLPTable": cucsCommSmashCLPTable,
       "cucsCommSmashCLPEntry": cucsCommSmashCLPEntry,
       "cucsCommSmashCLPInstanceId": cucsCommSmashCLPInstanceId,
       "cucsCommSmashCLPDn": cucsCommSmashCLPDn,
       "cucsCommSmashCLPRn": cucsCommSmashCLPRn,
       "cucsCommSmashCLPAdminState": cucsCommSmashCLPAdminState,
       "cucsCommSmashCLPDescr": cucsCommSmashCLPDescr,
       "cucsCommSmashCLPIntId": cucsCommSmashCLPIntId,
       "cucsCommSmashCLPName": cucsCommSmashCLPName,
       "cucsCommSmashCLPPort": cucsCommSmashCLPPort,
       "cucsCommSmashCLPProto": cucsCommSmashCLPProto,
       "cucsCommSmashCLPOperPort": cucsCommSmashCLPOperPort,
       "cucsCommSmashCLPPolicyLevel": cucsCommSmashCLPPolicyLevel,
       "cucsCommSmashCLPPolicyOwner": cucsCommSmashCLPPolicyOwner,
       "cucsCommSnmpTable": cucsCommSnmpTable,
       "cucsCommSnmpEntry": cucsCommSnmpEntry,
       "cucsCommSnmpInstanceId": cucsCommSnmpInstanceId,
       "cucsCommSnmpDn": cucsCommSnmpDn,
       "cucsCommSnmpRn": cucsCommSnmpRn,
       "cucsCommSnmpAdminState": cucsCommSnmpAdminState,
       "cucsCommSnmpCommunity": cucsCommSnmpCommunity,
       "cucsCommSnmpDescr": cucsCommSnmpDescr,
       "cucsCommSnmpIntId": cucsCommSnmpIntId,
       "cucsCommSnmpName": cucsCommSnmpName,
       "cucsCommSnmpPort": cucsCommSnmpPort,
       "cucsCommSnmpProto": cucsCommSnmpProto,
       "cucsCommSnmpSysContact": cucsCommSnmpSysContact,
       "cucsCommSnmpSysLocation": cucsCommSnmpSysLocation,
       "cucsCommSnmpConfigState": cucsCommSnmpConfigState,
       "cucsCommSnmpOperPort": cucsCommSnmpOperPort,
       "cucsCommSnmpPolicyLevel": cucsCommSnmpPolicyLevel,
       "cucsCommSnmpPolicyOwner": cucsCommSnmpPolicyOwner,
       "cucsCommSnmpIsSetSnmpSecure": cucsCommSnmpIsSetSnmpSecure,
       "cucsCommSnmpSnmpOperState": cucsCommSnmpSnmpOperState,
       "cucsCommSnmpTrapTable": cucsCommSnmpTrapTable,
       "cucsCommSnmpTrapEntry": cucsCommSnmpTrapEntry,
       "cucsCommSnmpTrapInstanceId": cucsCommSnmpTrapInstanceId,
       "cucsCommSnmpTrapDn": cucsCommSnmpTrapDn,
       "cucsCommSnmpTrapRn": cucsCommSnmpTrapRn,
       "cucsCommSnmpTrapCommunity": cucsCommSnmpTrapCommunity,
       "cucsCommSnmpTrapHostname": cucsCommSnmpTrapHostname,
       "cucsCommSnmpTrapPort": cucsCommSnmpTrapPort,
       "cucsCommSnmpTrapV3Privilege": cucsCommSnmpTrapV3Privilege,
       "cucsCommSnmpTrapVersion": cucsCommSnmpTrapVersion,
       "cucsCommSnmpTrapNotificationType": cucsCommSnmpTrapNotificationType,
       "cucsCommSnmpUserTable": cucsCommSnmpUserTable,
       "cucsCommSnmpUserEntry": cucsCommSnmpUserEntry,
       "cucsCommSnmpUserInstanceId": cucsCommSnmpUserInstanceId,
       "cucsCommSnmpUserDn": cucsCommSnmpUserDn,
       "cucsCommSnmpUserRn": cucsCommSnmpUserRn,
       "cucsCommSnmpUserAuth": cucsCommSnmpUserAuth,
       "cucsCommSnmpUserDescr": cucsCommSnmpUserDescr,
       "cucsCommSnmpUserName": cucsCommSnmpUserName,
       "cucsCommSnmpUserPrivPwdSet": cucsCommSnmpUserPrivPwdSet,
       "cucsCommSnmpUserPrivpwd": cucsCommSnmpUserPrivpwd,
       "cucsCommSnmpUserPwd": cucsCommSnmpUserPwd,
       "cucsCommSnmpUserPwdSet": cucsCommSnmpUserPwdSet,
       "cucsCommSnmpUserUseAes": cucsCommSnmpUserUseAes,
       "cucsCommSnmpUserConfigState": cucsCommSnmpUserConfigState,
       "cucsCommSnmpUserConfigStatusMessage": cucsCommSnmpUserConfigStatusMessage,
       "cucsCommSshTable": cucsCommSshTable,
       "cucsCommSshEntry": cucsCommSshEntry,
       "cucsCommSshInstanceId": cucsCommSshInstanceId,
       "cucsCommSshDn": cucsCommSshDn,
       "cucsCommSshRn": cucsCommSshRn,
       "cucsCommSshAdminState": cucsCommSshAdminState,
       "cucsCommSshDescr": cucsCommSshDescr,
       "cucsCommSshIntId": cucsCommSshIntId,
       "cucsCommSshName": cucsCommSshName,
       "cucsCommSshPort": cucsCommSshPort,
       "cucsCommSshProto": cucsCommSshProto,
       "cucsCommSshOperPort": cucsCommSshOperPort,
       "cucsCommSshPolicyLevel": cucsCommSshPolicyLevel,
       "cucsCommSshPolicyOwner": cucsCommSshPolicyOwner,
       "cucsCommSvcEpTable": cucsCommSvcEpTable,
       "cucsCommSvcEpEntry": cucsCommSvcEpEntry,
       "cucsCommSvcEpInstanceId": cucsCommSvcEpInstanceId,
       "cucsCommSvcEpDn": cucsCommSvcEpDn,
       "cucsCommSvcEpRn": cucsCommSvcEpRn,
       "cucsCommSvcEpDescr": cucsCommSvcEpDescr,
       "cucsCommSvcEpFsmDescr": cucsCommSvcEpFsmDescr,
       "cucsCommSvcEpFsmFlags": cucsCommSvcEpFsmFlags,
       "cucsCommSvcEpFsmPrev": cucsCommSvcEpFsmPrev,
       "cucsCommSvcEpFsmProgr": cucsCommSvcEpFsmProgr,
       "cucsCommSvcEpFsmRmtInvErrCode": cucsCommSvcEpFsmRmtInvErrCode,
       "cucsCommSvcEpFsmRmtInvErrDescr": cucsCommSvcEpFsmRmtInvErrDescr,
       "cucsCommSvcEpFsmRmtInvRslt": cucsCommSvcEpFsmRmtInvRslt,
       "cucsCommSvcEpFsmStageDescr": cucsCommSvcEpFsmStageDescr,
       "cucsCommSvcEpFsmStamp": cucsCommSvcEpFsmStamp,
       "cucsCommSvcEpFsmStatus": cucsCommSvcEpFsmStatus,
       "cucsCommSvcEpFsmTry": cucsCommSvcEpFsmTry,
       "cucsCommSvcEpIntId": cucsCommSvcEpIntId,
       "cucsCommSvcEpName": cucsCommSvcEpName,
       "cucsCommSvcEpConfigState": cucsCommSvcEpConfigState,
       "cucsCommSvcEpConfigStatusMessage": cucsCommSvcEpConfigStatusMessage,
       "cucsCommSvcEpPolicyLevel": cucsCommSvcEpPolicyLevel,
       "cucsCommSvcEpPolicyOwner": cucsCommSvcEpPolicyOwner,
       "cucsCommSvcEpFsmTaskTable": cucsCommSvcEpFsmTaskTable,
       "cucsCommSvcEpFsmTaskEntry": cucsCommSvcEpFsmTaskEntry,
       "cucsCommSvcEpFsmTaskInstanceId": cucsCommSvcEpFsmTaskInstanceId,
       "cucsCommSvcEpFsmTaskDn": cucsCommSvcEpFsmTaskDn,
       "cucsCommSvcEpFsmTaskRn": cucsCommSvcEpFsmTaskRn,
       "cucsCommSvcEpFsmTaskCompletion": cucsCommSvcEpFsmTaskCompletion,
       "cucsCommSvcEpFsmTaskFlags": cucsCommSvcEpFsmTaskFlags,
       "cucsCommSvcEpFsmTaskItem": cucsCommSvcEpFsmTaskItem,
       "cucsCommSvcEpFsmTaskSeqId": cucsCommSvcEpFsmTaskSeqId,
       "cucsCommSyslogTable": cucsCommSyslogTable,
       "cucsCommSyslogEntry": cucsCommSyslogEntry,
       "cucsCommSyslogInstanceId": cucsCommSyslogInstanceId,
       "cucsCommSyslogDn": cucsCommSyslogDn,
       "cucsCommSyslogRn": cucsCommSyslogRn,
       "cucsCommSyslogAdminState": cucsCommSyslogAdminState,
       "cucsCommSyslogDescr": cucsCommSyslogDescr,
       "cucsCommSyslogIntId": cucsCommSyslogIntId,
       "cucsCommSyslogName": cucsCommSyslogName,
       "cucsCommSyslogPort": cucsCommSyslogPort,
       "cucsCommSyslogProto": cucsCommSyslogProto,
       "cucsCommSyslogSeverity": cucsCommSyslogSeverity,
       "cucsCommSyslogOperPort": cucsCommSyslogOperPort,
       "cucsCommSyslogPolicyLevel": cucsCommSyslogPolicyLevel,
       "cucsCommSyslogPolicyOwner": cucsCommSyslogPolicyOwner,
       "cucsCommSyslogClientTable": cucsCommSyslogClientTable,
       "cucsCommSyslogClientEntry": cucsCommSyslogClientEntry,
       "cucsCommSyslogClientInstanceId": cucsCommSyslogClientInstanceId,
       "cucsCommSyslogClientDn": cucsCommSyslogClientDn,
       "cucsCommSyslogClientRn": cucsCommSyslogClientRn,
       "cucsCommSyslogClientAdminState": cucsCommSyslogClientAdminState,
       "cucsCommSyslogClientForwardingFacility": cucsCommSyslogClientForwardingFacility,
       "cucsCommSyslogClientHostname": cucsCommSyslogClientHostname,
       "cucsCommSyslogClientName": cucsCommSyslogClientName,
       "cucsCommSyslogClientSeverity": cucsCommSyslogClientSeverity,
       "cucsCommSyslogConsoleTable": cucsCommSyslogConsoleTable,
       "cucsCommSyslogConsoleEntry": cucsCommSyslogConsoleEntry,
       "cucsCommSyslogConsoleInstanceId": cucsCommSyslogConsoleInstanceId,
       "cucsCommSyslogConsoleDn": cucsCommSyslogConsoleDn,
       "cucsCommSyslogConsoleRn": cucsCommSyslogConsoleRn,
       "cucsCommSyslogConsoleAdminState": cucsCommSyslogConsoleAdminState,
       "cucsCommSyslogConsoleDescr": cucsCommSyslogConsoleDescr,
       "cucsCommSyslogConsoleName": cucsCommSyslogConsoleName,
       "cucsCommSyslogConsoleSeverity": cucsCommSyslogConsoleSeverity,
       "cucsCommSyslogFileTable": cucsCommSyslogFileTable,
       "cucsCommSyslogFileEntry": cucsCommSyslogFileEntry,
       "cucsCommSyslogFileInstanceId": cucsCommSyslogFileInstanceId,
       "cucsCommSyslogFileDn": cucsCommSyslogFileDn,
       "cucsCommSyslogFileRn": cucsCommSyslogFileRn,
       "cucsCommSyslogFileAdminState": cucsCommSyslogFileAdminState,
       "cucsCommSyslogFileDescr": cucsCommSyslogFileDescr,
       "cucsCommSyslogFileName": cucsCommSyslogFileName,
       "cucsCommSyslogFileSeverity": cucsCommSyslogFileSeverity,
       "cucsCommSyslogFileSize": cucsCommSyslogFileSize,
       "cucsCommSyslogMonitorTable": cucsCommSyslogMonitorTable,
       "cucsCommSyslogMonitorEntry": cucsCommSyslogMonitorEntry,
       "cucsCommSyslogMonitorInstanceId": cucsCommSyslogMonitorInstanceId,
       "cucsCommSyslogMonitorDn": cucsCommSyslogMonitorDn,
       "cucsCommSyslogMonitorRn": cucsCommSyslogMonitorRn,
       "cucsCommSyslogMonitorAdminState": cucsCommSyslogMonitorAdminState,
       "cucsCommSyslogMonitorDescr": cucsCommSyslogMonitorDescr,
       "cucsCommSyslogMonitorName": cucsCommSyslogMonitorName,
       "cucsCommSyslogMonitorSeverity": cucsCommSyslogMonitorSeverity,
       "cucsCommTelnetTable": cucsCommTelnetTable,
       "cucsCommTelnetEntry": cucsCommTelnetEntry,
       "cucsCommTelnetInstanceId": cucsCommTelnetInstanceId,
       "cucsCommTelnetDn": cucsCommTelnetDn,
       "cucsCommTelnetRn": cucsCommTelnetRn,
       "cucsCommTelnetAdminState": cucsCommTelnetAdminState,
       "cucsCommTelnetDescr": cucsCommTelnetDescr,
       "cucsCommTelnetIntId": cucsCommTelnetIntId,
       "cucsCommTelnetName": cucsCommTelnetName,
       "cucsCommTelnetPort": cucsCommTelnetPort,
       "cucsCommTelnetProto": cucsCommTelnetProto,
       "cucsCommTelnetOperPort": cucsCommTelnetOperPort,
       "cucsCommTelnetPolicyLevel": cucsCommTelnetPolicyLevel,
       "cucsCommTelnetPolicyOwner": cucsCommTelnetPolicyOwner,
       "cucsCommWebChannelTable": cucsCommWebChannelTable,
       "cucsCommWebChannelEntry": cucsCommWebChannelEntry,
       "cucsCommWebChannelInstanceId": cucsCommWebChannelInstanceId,
       "cucsCommWebChannelDn": cucsCommWebChannelDn,
       "cucsCommWebChannelRn": cucsCommWebChannelRn,
       "cucsCommWebChannelChannelState": cucsCommWebChannelChannelState,
       "cucsCommWebChannelDescr": cucsCommWebChannelDescr,
       "cucsCommWebChannelIntId": cucsCommWebChannelIntId,
       "cucsCommWebChannelName": cucsCommWebChannelName,
       "cucsCommWebChannelPolicyLevel": cucsCommWebChannelPolicyLevel,
       "cucsCommWebChannelPolicyOwner": cucsCommWebChannelPolicyOwner,
       "cucsCommWsmanTable": cucsCommWsmanTable,
       "cucsCommWsmanEntry": cucsCommWsmanEntry,
       "cucsCommWsmanInstanceId": cucsCommWsmanInstanceId,
       "cucsCommWsmanDn": cucsCommWsmanDn,
       "cucsCommWsmanRn": cucsCommWsmanRn,
       "cucsCommWsmanAdminState": cucsCommWsmanAdminState,
       "cucsCommWsmanDescr": cucsCommWsmanDescr,
       "cucsCommWsmanIntId": cucsCommWsmanIntId,
       "cucsCommWsmanName": cucsCommWsmanName,
       "cucsCommWsmanPort": cucsCommWsmanPort,
       "cucsCommWsmanProto": cucsCommWsmanProto,
       "cucsCommWsmanOperPort": cucsCommWsmanOperPort,
       "cucsCommWsmanPolicyLevel": cucsCommWsmanPolicyLevel,
       "cucsCommWsmanPolicyOwner": cucsCommWsmanPolicyOwner,
       "cucsCommXmlClConnPolicyTable": cucsCommXmlClConnPolicyTable,
       "cucsCommXmlClConnPolicyEntry": cucsCommXmlClConnPolicyEntry,
       "cucsCommXmlClConnPolicyInstanceId": cucsCommXmlClConnPolicyInstanceId,
       "cucsCommXmlClConnPolicyDn": cucsCommXmlClConnPolicyDn,
       "cucsCommXmlClConnPolicyRn": cucsCommXmlClConnPolicyRn,
       "cucsCommXmlClConnPolicyAdminState": cucsCommXmlClConnPolicyAdminState,
       "cucsCommXmlClConnPolicyClientType": cucsCommXmlClConnPolicyClientType,
       "cucsCommXmlClConnPolicyDescr": cucsCommXmlClConnPolicyDescr,
       "cucsCommXmlClConnPolicyIntId": cucsCommXmlClConnPolicyIntId,
       "cucsCommXmlClConnPolicyName": cucsCommXmlClConnPolicyName,
       "cucsCommXmlClConnPolicyPort": cucsCommXmlClConnPolicyPort,
       "cucsCommXmlClConnPolicyProto": cucsCommXmlClConnPolicyProto,
       "cucsCommXmlClConnPolicyOperPort": cucsCommXmlClConnPolicyOperPort,
       "cucsCommXmlClConnPolicyPolicyLevel": cucsCommXmlClConnPolicyPolicyLevel,
       "cucsCommXmlClConnPolicyPolicyOwner": cucsCommXmlClConnPolicyPolicyOwner,
       "cucsCommShellSvcLimitsTable": cucsCommShellSvcLimitsTable,
       "cucsCommShellSvcLimitsEntry": cucsCommShellSvcLimitsEntry,
       "cucsCommShellSvcLimitsInstanceId": cucsCommShellSvcLimitsInstanceId,
       "cucsCommShellSvcLimitsDn": cucsCommShellSvcLimitsDn,
       "cucsCommShellSvcLimitsRn": cucsCommShellSvcLimitsRn,
       "cucsCommShellSvcLimitsDescr": cucsCommShellSvcLimitsDescr,
       "cucsCommShellSvcLimitsIntId": cucsCommShellSvcLimitsIntId,
       "cucsCommShellSvcLimitsName": cucsCommShellSvcLimitsName,
       "cucsCommShellSvcLimitsSessionsPerUser": cucsCommShellSvcLimitsSessionsPerUser,
       "cucsCommShellSvcLimitsTotalSessions": cucsCommShellSvcLimitsTotalSessions,
       "cucsCommShellSvcLimitsPolicyLevel": cucsCommShellSvcLimitsPolicyLevel,
       "cucsCommShellSvcLimitsPolicyOwner": cucsCommShellSvcLimitsPolicyOwner,
       "cucsCommSyslogSourceTable": cucsCommSyslogSourceTable,
       "cucsCommSyslogSourceEntry": cucsCommSyslogSourceEntry,
       "cucsCommSyslogSourceInstanceId": cucsCommSyslogSourceInstanceId,
       "cucsCommSyslogSourceDn": cucsCommSyslogSourceDn,
       "cucsCommSyslogSourceRn": cucsCommSyslogSourceRn,
       "cucsCommSyslogSourceAudits": cucsCommSyslogSourceAudits,
       "cucsCommSyslogSourceDescr": cucsCommSyslogSourceDescr,
       "cucsCommSyslogSourceEvents": cucsCommSyslogSourceEvents,
       "cucsCommSyslogSourceFaults": cucsCommSyslogSourceFaults,
       "cucsCommSyslogSourceName": cucsCommSyslogSourceName,
       "cucsCommWebSvcLimitsTable": cucsCommWebSvcLimitsTable,
       "cucsCommWebSvcLimitsEntry": cucsCommWebSvcLimitsEntry,
       "cucsCommWebSvcLimitsInstanceId": cucsCommWebSvcLimitsInstanceId,
       "cucsCommWebSvcLimitsDn": cucsCommWebSvcLimitsDn,
       "cucsCommWebSvcLimitsRn": cucsCommWebSvcLimitsRn,
       "cucsCommWebSvcLimitsDescr": cucsCommWebSvcLimitsDescr,
       "cucsCommWebSvcLimitsIntId": cucsCommWebSvcLimitsIntId,
       "cucsCommWebSvcLimitsName": cucsCommWebSvcLimitsName,
       "cucsCommWebSvcLimitsSessionsPerUser": cucsCommWebSvcLimitsSessionsPerUser,
       "cucsCommWebSvcLimitsTotalSessions": cucsCommWebSvcLimitsTotalSessions,
       "cucsCommWebSvcLimitsPolicyLevel": cucsCommWebSvcLimitsPolicyLevel,
       "cucsCommWebSvcLimitsPolicyOwner": cucsCommWebSvcLimitsPolicyOwner,
       "cucsCommSvcEpFsmTable": cucsCommSvcEpFsmTable,
       "cucsCommSvcEpFsmEntry": cucsCommSvcEpFsmEntry,
       "cucsCommSvcEpFsmInstanceId": cucsCommSvcEpFsmInstanceId,
       "cucsCommSvcEpFsmDn": cucsCommSvcEpFsmDn,
       "cucsCommSvcEpFsmRn": cucsCommSvcEpFsmRn,
       "cucsCommSvcEpFsmCompletionTime": cucsCommSvcEpFsmCompletionTime,
       "cucsCommSvcEpFsmCurrentFsm": cucsCommSvcEpFsmCurrentFsm,
       "cucsCommSvcEpFsmDescrData": cucsCommSvcEpFsmDescrData,
       "cucsCommSvcEpFsmFsmStatus": cucsCommSvcEpFsmFsmStatus,
       "cucsCommSvcEpFsmProgress": cucsCommSvcEpFsmProgress,
       "cucsCommSvcEpFsmRmtErrCode": cucsCommSvcEpFsmRmtErrCode,
       "cucsCommSvcEpFsmRmtErrDescr": cucsCommSvcEpFsmRmtErrDescr,
       "cucsCommSvcEpFsmRmtRslt": cucsCommSvcEpFsmRmtRslt,
       "cucsCommSvcEpFsmStageTable": cucsCommSvcEpFsmStageTable,
       "cucsCommSvcEpFsmStageEntry": cucsCommSvcEpFsmStageEntry,
       "cucsCommSvcEpFsmStageInstanceId": cucsCommSvcEpFsmStageInstanceId,
       "cucsCommSvcEpFsmStageDn": cucsCommSvcEpFsmStageDn,
       "cucsCommSvcEpFsmStageRn": cucsCommSvcEpFsmStageRn,
       "cucsCommSvcEpFsmStageDescrData": cucsCommSvcEpFsmStageDescrData,
       "cucsCommSvcEpFsmStageLastUpdateTime": cucsCommSvcEpFsmStageLastUpdateTime,
       "cucsCommSvcEpFsmStageName": cucsCommSvcEpFsmStageName,
       "cucsCommSvcEpFsmStageOrder": cucsCommSvcEpFsmStageOrder,
       "cucsCommSvcEpFsmStageRetry": cucsCommSvcEpFsmStageRetry,
       "cucsCommSvcEpFsmStageStageStatus": cucsCommSvcEpFsmStageStageStatus,
       "cucsCommCimcWebServiceTable": cucsCommCimcWebServiceTable,
       "cucsCommCimcWebServiceEntry": cucsCommCimcWebServiceEntry,
       "cucsCommCimcWebServiceInstanceId": cucsCommCimcWebServiceInstanceId,
       "cucsCommCimcWebServiceDn": cucsCommCimcWebServiceDn,
       "cucsCommCimcWebServiceRn": cucsCommCimcWebServiceRn,
       "cucsCommCimcWebServiceAdminState": cucsCommCimcWebServiceAdminState,
       "cucsCommCimcWebServiceDescr": cucsCommCimcWebServiceDescr,
       "cucsCommCimcWebServiceIntId": cucsCommCimcWebServiceIntId,
       "cucsCommCimcWebServiceName": cucsCommCimcWebServiceName,
       "cucsCommCimcWebServiceOperPort": cucsCommCimcWebServiceOperPort,
       "cucsCommCimcWebServicePolicyLevel": cucsCommCimcWebServicePolicyLevel,
       "cucsCommCimcWebServicePolicyOwner": cucsCommCimcWebServicePolicyOwner,
       "cucsCommCimcWebServicePort": cucsCommCimcWebServicePort,
       "cucsCommCimcWebServiceProto": cucsCommCimcWebServiceProto,
       "cucsCommLocaleTable": cucsCommLocaleTable,
       "cucsCommLocaleEntry": cucsCommLocaleEntry,
       "cucsCommLocaleInstanceId": cucsCommLocaleInstanceId,
       "cucsCommLocaleDn": cucsCommLocaleDn,
       "cucsCommLocaleRn": cucsCommLocaleRn,
       "cucsCommLocaleDescr": cucsCommLocaleDescr,
       "cucsCommLocaleName": cucsCommLocaleName,
       "cucsCommSvcPolicyTable": cucsCommSvcPolicyTable,
       "cucsCommSvcPolicyEntry": cucsCommSvcPolicyEntry,
       "cucsCommSvcPolicyInstanceId": cucsCommSvcPolicyInstanceId,
       "cucsCommSvcPolicyDn": cucsCommSvcPolicyDn,
       "cucsCommSvcPolicyRn": cucsCommSvcPolicyRn,
       "cucsCommSvcPolicyDescr": cucsCommSvcPolicyDescr,
       "cucsCommSvcPolicyIntId": cucsCommSvcPolicyIntId,
       "cucsCommSvcPolicyName": cucsCommSvcPolicyName,
       "cucsCommSvcPolicyPolicyLevel": cucsCommSvcPolicyPolicyLevel,
       "cucsCommSvcPolicyPolicyOwner": cucsCommSvcPolicyPolicyOwner}
)
