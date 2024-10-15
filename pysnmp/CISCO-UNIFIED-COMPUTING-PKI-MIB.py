# SNMP MIB module (CISCO-UNIFIED-COMPUTING-PKI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-PKI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:08 2024
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
 CucsConditionRemoteInvRslt,
 CucsFsmCompletion,
 CucsFsmFlags,
 CucsFsmFsmStageStatus,
 CucsPkiCertStatus,
 CucsPkiEpFsmCurrentFsm,
 CucsPkiEpFsmStageName,
 CucsPkiEpFsmTaskItem,
 CucsPkiKeyringState,
 CucsPkiModulus,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsAaaConfigState",
    "CucsConditionRemoteInvRslt",
    "CucsFsmCompletion",
    "CucsFsmFlags",
    "CucsFsmFsmStageStatus",
    "CucsPkiCertStatus",
    "CucsPkiEpFsmCurrentFsm",
    "CucsPkiEpFsmStageName",
    "CucsPkiEpFsmTaskItem",
    "CucsPkiKeyringState",
    "CucsPkiModulus",
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

cucsPkiObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsPkiCertReqTable_Object = MibTable
cucsPkiCertReqTable = _CucsPkiCertReqTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1)
)
if mibBuilder.loadTexts:
    cucsPkiCertReqTable.setStatus("current")
_CucsPkiCertReqEntry_Object = MibTableRow
cucsPkiCertReqEntry = _CucsPkiCertReqEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1)
)
cucsPkiCertReqEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiCertReqInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiCertReqEntry.setStatus("current")
_CucsPkiCertReqInstanceId_Type = CucsManagedObjectId
_CucsPkiCertReqInstanceId_Object = MibTableColumn
cucsPkiCertReqInstanceId = _CucsPkiCertReqInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 1),
    _CucsPkiCertReqInstanceId_Type()
)
cucsPkiCertReqInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiCertReqInstanceId.setStatus("current")
_CucsPkiCertReqDn_Type = CucsManagedObjectDn
_CucsPkiCertReqDn_Object = MibTableColumn
cucsPkiCertReqDn = _CucsPkiCertReqDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 2),
    _CucsPkiCertReqDn_Type()
)
cucsPkiCertReqDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqDn.setStatus("current")
_CucsPkiCertReqRn_Type = SnmpAdminString
_CucsPkiCertReqRn_Object = MibTableColumn
cucsPkiCertReqRn = _CucsPkiCertReqRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 3),
    _CucsPkiCertReqRn_Type()
)
cucsPkiCertReqRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqRn.setStatus("current")
_CucsPkiCertReqIp_Type = InetAddressIPv4
_CucsPkiCertReqIp_Object = MibTableColumn
cucsPkiCertReqIp = _CucsPkiCertReqIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 4),
    _CucsPkiCertReqIp_Type()
)
cucsPkiCertReqIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIp.setStatus("current")
_CucsPkiCertReqPwd_Type = SnmpAdminString
_CucsPkiCertReqPwd_Object = MibTableColumn
cucsPkiCertReqPwd = _CucsPkiCertReqPwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 5),
    _CucsPkiCertReqPwd_Type()
)
cucsPkiCertReqPwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqPwd.setStatus("current")
_CucsPkiCertReqReq_Type = SnmpAdminString
_CucsPkiCertReqReq_Object = MibTableColumn
cucsPkiCertReqReq = _CucsPkiCertReqReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 6),
    _CucsPkiCertReqReq_Type()
)
cucsPkiCertReqReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqReq.setStatus("current")
_CucsPkiCertReqSubjName_Type = SnmpAdminString
_CucsPkiCertReqSubjName_Object = MibTableColumn
cucsPkiCertReqSubjName = _CucsPkiCertReqSubjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 7),
    _CucsPkiCertReqSubjName_Type()
)
cucsPkiCertReqSubjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqSubjName.setStatus("current")
_CucsPkiCertReqCountry_Type = SnmpAdminString
_CucsPkiCertReqCountry_Object = MibTableColumn
cucsPkiCertReqCountry = _CucsPkiCertReqCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 8),
    _CucsPkiCertReqCountry_Type()
)
cucsPkiCertReqCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqCountry.setStatus("current")
_CucsPkiCertReqDns_Type = SnmpAdminString
_CucsPkiCertReqDns_Object = MibTableColumn
cucsPkiCertReqDns = _CucsPkiCertReqDns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 9),
    _CucsPkiCertReqDns_Type()
)
cucsPkiCertReqDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqDns.setStatus("current")
_CucsPkiCertReqEmail_Type = SnmpAdminString
_CucsPkiCertReqEmail_Object = MibTableColumn
cucsPkiCertReqEmail = _CucsPkiCertReqEmail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 10),
    _CucsPkiCertReqEmail_Type()
)
cucsPkiCertReqEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqEmail.setStatus("current")
_CucsPkiCertReqLocality_Type = SnmpAdminString
_CucsPkiCertReqLocality_Object = MibTableColumn
cucsPkiCertReqLocality = _CucsPkiCertReqLocality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 11),
    _CucsPkiCertReqLocality_Type()
)
cucsPkiCertReqLocality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqLocality.setStatus("current")
_CucsPkiCertReqOrgName_Type = SnmpAdminString
_CucsPkiCertReqOrgName_Object = MibTableColumn
cucsPkiCertReqOrgName = _CucsPkiCertReqOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 12),
    _CucsPkiCertReqOrgName_Type()
)
cucsPkiCertReqOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqOrgName.setStatus("current")
_CucsPkiCertReqOrgUnitName_Type = SnmpAdminString
_CucsPkiCertReqOrgUnitName_Object = MibTableColumn
cucsPkiCertReqOrgUnitName = _CucsPkiCertReqOrgUnitName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 13),
    _CucsPkiCertReqOrgUnitName_Type()
)
cucsPkiCertReqOrgUnitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqOrgUnitName.setStatus("current")
_CucsPkiCertReqState_Type = SnmpAdminString
_CucsPkiCertReqState_Object = MibTableColumn
cucsPkiCertReqState = _CucsPkiCertReqState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 14),
    _CucsPkiCertReqState_Type()
)
cucsPkiCertReqState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqState.setStatus("current")
_CucsPkiCertReqIpA_Type = InetAddressIPv4
_CucsPkiCertReqIpA_Object = MibTableColumn
cucsPkiCertReqIpA = _CucsPkiCertReqIpA_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 15),
    _CucsPkiCertReqIpA_Type()
)
cucsPkiCertReqIpA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIpA.setStatus("current")
_CucsPkiCertReqIpB_Type = InetAddressIPv4
_CucsPkiCertReqIpB_Object = MibTableColumn
cucsPkiCertReqIpB = _CucsPkiCertReqIpB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 16),
    _CucsPkiCertReqIpB_Type()
)
cucsPkiCertReqIpB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIpB.setStatus("current")
_CucsPkiCertReqIpv6_Type = InetAddressIPv6
_CucsPkiCertReqIpv6_Object = MibTableColumn
cucsPkiCertReqIpv6 = _CucsPkiCertReqIpv6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 17),
    _CucsPkiCertReqIpv6_Type()
)
cucsPkiCertReqIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIpv6.setStatus("current")
_CucsPkiCertReqIpv6A_Type = InetAddressIPv6
_CucsPkiCertReqIpv6A_Object = MibTableColumn
cucsPkiCertReqIpv6A = _CucsPkiCertReqIpv6A_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 18),
    _CucsPkiCertReqIpv6A_Type()
)
cucsPkiCertReqIpv6A.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIpv6A.setStatus("current")
_CucsPkiCertReqIpv6B_Type = InetAddressIPv6
_CucsPkiCertReqIpv6B_Object = MibTableColumn
cucsPkiCertReqIpv6B = _CucsPkiCertReqIpv6B_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 1, 1, 19),
    _CucsPkiCertReqIpv6B_Type()
)
cucsPkiCertReqIpv6B.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiCertReqIpv6B.setStatus("current")
_CucsPkiEpTable_Object = MibTable
cucsPkiEpTable = _CucsPkiEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2)
)
if mibBuilder.loadTexts:
    cucsPkiEpTable.setStatus("current")
_CucsPkiEpEntry_Object = MibTableRow
cucsPkiEpEntry = _CucsPkiEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1)
)
cucsPkiEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiEpEntry.setStatus("current")
_CucsPkiEpInstanceId_Type = CucsManagedObjectId
_CucsPkiEpInstanceId_Object = MibTableColumn
cucsPkiEpInstanceId = _CucsPkiEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 1),
    _CucsPkiEpInstanceId_Type()
)
cucsPkiEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiEpInstanceId.setStatus("current")
_CucsPkiEpDn_Type = CucsManagedObjectDn
_CucsPkiEpDn_Object = MibTableColumn
cucsPkiEpDn = _CucsPkiEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 2),
    _CucsPkiEpDn_Type()
)
cucsPkiEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpDn.setStatus("current")
_CucsPkiEpRn_Type = SnmpAdminString
_CucsPkiEpRn_Object = MibTableColumn
cucsPkiEpRn = _CucsPkiEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 3),
    _CucsPkiEpRn_Type()
)
cucsPkiEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpRn.setStatus("current")
_CucsPkiEpDescr_Type = SnmpAdminString
_CucsPkiEpDescr_Object = MibTableColumn
cucsPkiEpDescr = _CucsPkiEpDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 4),
    _CucsPkiEpDescr_Type()
)
cucsPkiEpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpDescr.setStatus("current")
_CucsPkiEpFsmDescr_Type = SnmpAdminString
_CucsPkiEpFsmDescr_Object = MibTableColumn
cucsPkiEpFsmDescr = _CucsPkiEpFsmDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 5),
    _CucsPkiEpFsmDescr_Type()
)
cucsPkiEpFsmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmDescr.setStatus("current")
_CucsPkiEpFsmPrev_Type = SnmpAdminString
_CucsPkiEpFsmPrev_Object = MibTableColumn
cucsPkiEpFsmPrev = _CucsPkiEpFsmPrev_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 6),
    _CucsPkiEpFsmPrev_Type()
)
cucsPkiEpFsmPrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmPrev.setStatus("current")
_CucsPkiEpFsmProgr_Type = Gauge32
_CucsPkiEpFsmProgr_Object = MibTableColumn
cucsPkiEpFsmProgr = _CucsPkiEpFsmProgr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 7),
    _CucsPkiEpFsmProgr_Type()
)
cucsPkiEpFsmProgr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmProgr.setStatus("current")
_CucsPkiEpFsmRmtInvErrCode_Type = Gauge32
_CucsPkiEpFsmRmtInvErrCode_Object = MibTableColumn
cucsPkiEpFsmRmtInvErrCode = _CucsPkiEpFsmRmtInvErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 8),
    _CucsPkiEpFsmRmtInvErrCode_Type()
)
cucsPkiEpFsmRmtInvErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtInvErrCode.setStatus("current")
_CucsPkiEpFsmRmtInvErrDescr_Type = SnmpAdminString
_CucsPkiEpFsmRmtInvErrDescr_Object = MibTableColumn
cucsPkiEpFsmRmtInvErrDescr = _CucsPkiEpFsmRmtInvErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 9),
    _CucsPkiEpFsmRmtInvErrDescr_Type()
)
cucsPkiEpFsmRmtInvErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtInvErrDescr.setStatus("current")
_CucsPkiEpFsmRmtInvRslt_Type = CucsConditionRemoteInvRslt
_CucsPkiEpFsmRmtInvRslt_Object = MibTableColumn
cucsPkiEpFsmRmtInvRslt = _CucsPkiEpFsmRmtInvRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 10),
    _CucsPkiEpFsmRmtInvRslt_Type()
)
cucsPkiEpFsmRmtInvRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtInvRslt.setStatus("current")
_CucsPkiEpFsmStageDescr_Type = SnmpAdminString
_CucsPkiEpFsmStageDescr_Object = MibTableColumn
cucsPkiEpFsmStageDescr = _CucsPkiEpFsmStageDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 11),
    _CucsPkiEpFsmStageDescr_Type()
)
cucsPkiEpFsmStageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageDescr.setStatus("current")
_CucsPkiEpFsmStamp_Type = DateAndTime
_CucsPkiEpFsmStamp_Object = MibTableColumn
cucsPkiEpFsmStamp = _CucsPkiEpFsmStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 12),
    _CucsPkiEpFsmStamp_Type()
)
cucsPkiEpFsmStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStamp.setStatus("current")
_CucsPkiEpFsmStatus_Type = SnmpAdminString
_CucsPkiEpFsmStatus_Object = MibTableColumn
cucsPkiEpFsmStatus = _CucsPkiEpFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 13),
    _CucsPkiEpFsmStatus_Type()
)
cucsPkiEpFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStatus.setStatus("current")
_CucsPkiEpFsmTry_Type = Gauge32
_CucsPkiEpFsmTry_Object = MibTableColumn
cucsPkiEpFsmTry = _CucsPkiEpFsmTry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 14),
    _CucsPkiEpFsmTry_Type()
)
cucsPkiEpFsmTry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTry.setStatus("current")
_CucsPkiEpIntId_Type = SnmpAdminString
_CucsPkiEpIntId_Object = MibTableColumn
cucsPkiEpIntId = _CucsPkiEpIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 15),
    _CucsPkiEpIntId_Type()
)
cucsPkiEpIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpIntId.setStatus("current")
_CucsPkiEpName_Type = SnmpAdminString
_CucsPkiEpName_Object = MibTableColumn
cucsPkiEpName = _CucsPkiEpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 16),
    _CucsPkiEpName_Type()
)
cucsPkiEpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpName.setStatus("current")
_CucsPkiEpPolicyLevel_Type = Gauge32
_CucsPkiEpPolicyLevel_Object = MibTableColumn
cucsPkiEpPolicyLevel = _CucsPkiEpPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 17),
    _CucsPkiEpPolicyLevel_Type()
)
cucsPkiEpPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpPolicyLevel.setStatus("current")
_CucsPkiEpPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPkiEpPolicyOwner_Object = MibTableColumn
cucsPkiEpPolicyOwner = _CucsPkiEpPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 2, 1, 18),
    _CucsPkiEpPolicyOwner_Type()
)
cucsPkiEpPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpPolicyOwner.setStatus("current")
_CucsPkiEpFsmTaskTable_Object = MibTable
cucsPkiEpFsmTaskTable = _CucsPkiEpFsmTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3)
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskTable.setStatus("current")
_CucsPkiEpFsmTaskEntry_Object = MibTableRow
cucsPkiEpFsmTaskEntry = _CucsPkiEpFsmTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1)
)
cucsPkiEpFsmTaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmTaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskEntry.setStatus("current")
_CucsPkiEpFsmTaskInstanceId_Type = CucsManagedObjectId
_CucsPkiEpFsmTaskInstanceId_Object = MibTableColumn
cucsPkiEpFsmTaskInstanceId = _CucsPkiEpFsmTaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 1),
    _CucsPkiEpFsmTaskInstanceId_Type()
)
cucsPkiEpFsmTaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskInstanceId.setStatus("current")
_CucsPkiEpFsmTaskDn_Type = CucsManagedObjectDn
_CucsPkiEpFsmTaskDn_Object = MibTableColumn
cucsPkiEpFsmTaskDn = _CucsPkiEpFsmTaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 2),
    _CucsPkiEpFsmTaskDn_Type()
)
cucsPkiEpFsmTaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskDn.setStatus("current")
_CucsPkiEpFsmTaskRn_Type = SnmpAdminString
_CucsPkiEpFsmTaskRn_Object = MibTableColumn
cucsPkiEpFsmTaskRn = _CucsPkiEpFsmTaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 3),
    _CucsPkiEpFsmTaskRn_Type()
)
cucsPkiEpFsmTaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskRn.setStatus("current")
_CucsPkiEpFsmTaskCompletion_Type = CucsFsmCompletion
_CucsPkiEpFsmTaskCompletion_Object = MibTableColumn
cucsPkiEpFsmTaskCompletion = _CucsPkiEpFsmTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 4),
    _CucsPkiEpFsmTaskCompletion_Type()
)
cucsPkiEpFsmTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskCompletion.setStatus("current")
_CucsPkiEpFsmTaskFlags_Type = CucsFsmFlags
_CucsPkiEpFsmTaskFlags_Object = MibTableColumn
cucsPkiEpFsmTaskFlags = _CucsPkiEpFsmTaskFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 5),
    _CucsPkiEpFsmTaskFlags_Type()
)
cucsPkiEpFsmTaskFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskFlags.setStatus("current")
_CucsPkiEpFsmTaskItem_Type = CucsPkiEpFsmTaskItem
_CucsPkiEpFsmTaskItem_Object = MibTableColumn
cucsPkiEpFsmTaskItem = _CucsPkiEpFsmTaskItem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 6),
    _CucsPkiEpFsmTaskItem_Type()
)
cucsPkiEpFsmTaskItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskItem.setStatus("current")
_CucsPkiEpFsmTaskSeqId_Type = Gauge32
_CucsPkiEpFsmTaskSeqId_Object = MibTableColumn
cucsPkiEpFsmTaskSeqId = _CucsPkiEpFsmTaskSeqId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 3, 1, 7),
    _CucsPkiEpFsmTaskSeqId_Type()
)
cucsPkiEpFsmTaskSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmTaskSeqId.setStatus("current")
_CucsPkiKeyRingTable_Object = MibTable
cucsPkiKeyRingTable = _CucsPkiKeyRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4)
)
if mibBuilder.loadTexts:
    cucsPkiKeyRingTable.setStatus("current")
_CucsPkiKeyRingEntry_Object = MibTableRow
cucsPkiKeyRingEntry = _CucsPkiKeyRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1)
)
cucsPkiKeyRingEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiKeyRingInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiKeyRingEntry.setStatus("current")
_CucsPkiKeyRingInstanceId_Type = CucsManagedObjectId
_CucsPkiKeyRingInstanceId_Object = MibTableColumn
cucsPkiKeyRingInstanceId = _CucsPkiKeyRingInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 1),
    _CucsPkiKeyRingInstanceId_Type()
)
cucsPkiKeyRingInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiKeyRingInstanceId.setStatus("current")
_CucsPkiKeyRingDn_Type = CucsManagedObjectDn
_CucsPkiKeyRingDn_Object = MibTableColumn
cucsPkiKeyRingDn = _CucsPkiKeyRingDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 2),
    _CucsPkiKeyRingDn_Type()
)
cucsPkiKeyRingDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingDn.setStatus("current")
_CucsPkiKeyRingRn_Type = SnmpAdminString
_CucsPkiKeyRingRn_Object = MibTableColumn
cucsPkiKeyRingRn = _CucsPkiKeyRingRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 3),
    _CucsPkiKeyRingRn_Type()
)
cucsPkiKeyRingRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingRn.setStatus("current")
_CucsPkiKeyRingAdminState_Type = CucsPkiKeyringState
_CucsPkiKeyRingAdminState_Object = MibTableColumn
cucsPkiKeyRingAdminState = _CucsPkiKeyRingAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 4),
    _CucsPkiKeyRingAdminState_Type()
)
cucsPkiKeyRingAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingAdminState.setStatus("current")
_CucsPkiKeyRingCert_Type = SnmpAdminString
_CucsPkiKeyRingCert_Object = MibTableColumn
cucsPkiKeyRingCert = _CucsPkiKeyRingCert_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 5),
    _CucsPkiKeyRingCert_Type()
)
cucsPkiKeyRingCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingCert.setStatus("current")
_CucsPkiKeyRingDescr_Type = SnmpAdminString
_CucsPkiKeyRingDescr_Object = MibTableColumn
cucsPkiKeyRingDescr = _CucsPkiKeyRingDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 6),
    _CucsPkiKeyRingDescr_Type()
)
cucsPkiKeyRingDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingDescr.setStatus("current")
_CucsPkiKeyRingIntId_Type = SnmpAdminString
_CucsPkiKeyRingIntId_Object = MibTableColumn
cucsPkiKeyRingIntId = _CucsPkiKeyRingIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 7),
    _CucsPkiKeyRingIntId_Type()
)
cucsPkiKeyRingIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingIntId.setStatus("current")
_CucsPkiKeyRingKey_Type = SnmpAdminString
_CucsPkiKeyRingKey_Object = MibTableColumn
cucsPkiKeyRingKey = _CucsPkiKeyRingKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 8),
    _CucsPkiKeyRingKey_Type()
)
cucsPkiKeyRingKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingKey.setStatus("current")
_CucsPkiKeyRingModulus_Type = CucsPkiModulus
_CucsPkiKeyRingModulus_Object = MibTableColumn
cucsPkiKeyRingModulus = _CucsPkiKeyRingModulus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 9),
    _CucsPkiKeyRingModulus_Type()
)
cucsPkiKeyRingModulus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingModulus.setStatus("current")
_CucsPkiKeyRingName_Type = SnmpAdminString
_CucsPkiKeyRingName_Object = MibTableColumn
cucsPkiKeyRingName = _CucsPkiKeyRingName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 10),
    _CucsPkiKeyRingName_Type()
)
cucsPkiKeyRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingName.setStatus("current")
_CucsPkiKeyRingRegen_Type = TruthValue
_CucsPkiKeyRingRegen_Object = MibTableColumn
cucsPkiKeyRingRegen = _CucsPkiKeyRingRegen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 11),
    _CucsPkiKeyRingRegen_Type()
)
cucsPkiKeyRingRegen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingRegen.setStatus("current")
_CucsPkiKeyRingTp_Type = SnmpAdminString
_CucsPkiKeyRingTp_Object = MibTableColumn
cucsPkiKeyRingTp = _CucsPkiKeyRingTp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 12),
    _CucsPkiKeyRingTp_Type()
)
cucsPkiKeyRingTp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingTp.setStatus("current")
_CucsPkiKeyRingCertStatus_Type = CucsPkiCertStatus
_CucsPkiKeyRingCertStatus_Object = MibTableColumn
cucsPkiKeyRingCertStatus = _CucsPkiKeyRingCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 13),
    _CucsPkiKeyRingCertStatus_Type()
)
cucsPkiKeyRingCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingCertStatus.setStatus("current")
_CucsPkiKeyRingConfigState_Type = CucsAaaConfigState
_CucsPkiKeyRingConfigState_Object = MibTableColumn
cucsPkiKeyRingConfigState = _CucsPkiKeyRingConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 14),
    _CucsPkiKeyRingConfigState_Type()
)
cucsPkiKeyRingConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingConfigState.setStatus("current")
_CucsPkiKeyRingConfigStatusMessage_Type = SnmpAdminString
_CucsPkiKeyRingConfigStatusMessage_Object = MibTableColumn
cucsPkiKeyRingConfigStatusMessage = _CucsPkiKeyRingConfigStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 15),
    _CucsPkiKeyRingConfigStatusMessage_Type()
)
cucsPkiKeyRingConfigStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingConfigStatusMessage.setStatus("current")
_CucsPkiKeyRingPolicyLevel_Type = Gauge32
_CucsPkiKeyRingPolicyLevel_Object = MibTableColumn
cucsPkiKeyRingPolicyLevel = _CucsPkiKeyRingPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 16),
    _CucsPkiKeyRingPolicyLevel_Type()
)
cucsPkiKeyRingPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingPolicyLevel.setStatus("current")
_CucsPkiKeyRingPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPkiKeyRingPolicyOwner_Object = MibTableColumn
cucsPkiKeyRingPolicyOwner = _CucsPkiKeyRingPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 4, 1, 17),
    _CucsPkiKeyRingPolicyOwner_Type()
)
cucsPkiKeyRingPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiKeyRingPolicyOwner.setStatus("current")
_CucsPkiTPTable_Object = MibTable
cucsPkiTPTable = _CucsPkiTPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5)
)
if mibBuilder.loadTexts:
    cucsPkiTPTable.setStatus("current")
_CucsPkiTPEntry_Object = MibTableRow
cucsPkiTPEntry = _CucsPkiTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1)
)
cucsPkiTPEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiTPInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiTPEntry.setStatus("current")
_CucsPkiTPInstanceId_Type = CucsManagedObjectId
_CucsPkiTPInstanceId_Object = MibTableColumn
cucsPkiTPInstanceId = _CucsPkiTPInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 1),
    _CucsPkiTPInstanceId_Type()
)
cucsPkiTPInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiTPInstanceId.setStatus("current")
_CucsPkiTPDn_Type = CucsManagedObjectDn
_CucsPkiTPDn_Object = MibTableColumn
cucsPkiTPDn = _CucsPkiTPDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 2),
    _CucsPkiTPDn_Type()
)
cucsPkiTPDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPDn.setStatus("current")
_CucsPkiTPRn_Type = SnmpAdminString
_CucsPkiTPRn_Object = MibTableColumn
cucsPkiTPRn = _CucsPkiTPRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 3),
    _CucsPkiTPRn_Type()
)
cucsPkiTPRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPRn.setStatus("current")
_CucsPkiTPCertChain_Type = SnmpAdminString
_CucsPkiTPCertChain_Object = MibTableColumn
cucsPkiTPCertChain = _CucsPkiTPCertChain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 4),
    _CucsPkiTPCertChain_Type()
)
cucsPkiTPCertChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPCertChain.setStatus("current")
_CucsPkiTPDescr_Type = SnmpAdminString
_CucsPkiTPDescr_Object = MibTableColumn
cucsPkiTPDescr = _CucsPkiTPDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 5),
    _CucsPkiTPDescr_Type()
)
cucsPkiTPDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPDescr.setStatus("current")
_CucsPkiTPFp_Type = SnmpAdminString
_CucsPkiTPFp_Object = MibTableColumn
cucsPkiTPFp = _CucsPkiTPFp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 6),
    _CucsPkiTPFp_Type()
)
cucsPkiTPFp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPFp.setStatus("current")
_CucsPkiTPIntId_Type = SnmpAdminString
_CucsPkiTPIntId_Object = MibTableColumn
cucsPkiTPIntId = _CucsPkiTPIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 7),
    _CucsPkiTPIntId_Type()
)
cucsPkiTPIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPIntId.setStatus("current")
_CucsPkiTPName_Type = SnmpAdminString
_CucsPkiTPName_Object = MibTableColumn
cucsPkiTPName = _CucsPkiTPName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 8),
    _CucsPkiTPName_Type()
)
cucsPkiTPName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPName.setStatus("current")
_CucsPkiTPNumCerts_Type = Gauge32
_CucsPkiTPNumCerts_Object = MibTableColumn
cucsPkiTPNumCerts = _CucsPkiTPNumCerts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 9),
    _CucsPkiTPNumCerts_Type()
)
cucsPkiTPNumCerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPNumCerts.setStatus("current")
_CucsPkiTPCertStatus_Type = CucsPkiCertStatus
_CucsPkiTPCertStatus_Object = MibTableColumn
cucsPkiTPCertStatus = _CucsPkiTPCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 10),
    _CucsPkiTPCertStatus_Type()
)
cucsPkiTPCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPCertStatus.setStatus("current")
_CucsPkiTPPolicyLevel_Type = Gauge32
_CucsPkiTPPolicyLevel_Object = MibTableColumn
cucsPkiTPPolicyLevel = _CucsPkiTPPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 11),
    _CucsPkiTPPolicyLevel_Type()
)
cucsPkiTPPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPPolicyLevel.setStatus("current")
_CucsPkiTPPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsPkiTPPolicyOwner_Object = MibTableColumn
cucsPkiTPPolicyOwner = _CucsPkiTPPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 5, 1, 12),
    _CucsPkiTPPolicyOwner_Type()
)
cucsPkiTPPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiTPPolicyOwner.setStatus("current")
_CucsPkiEpFsmTable_Object = MibTable
cucsPkiEpFsmTable = _CucsPkiEpFsmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6)
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmTable.setStatus("current")
_CucsPkiEpFsmEntry_Object = MibTableRow
cucsPkiEpFsmEntry = _CucsPkiEpFsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1)
)
cucsPkiEpFsmEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmEntry.setStatus("current")
_CucsPkiEpFsmInstanceId_Type = CucsManagedObjectId
_CucsPkiEpFsmInstanceId_Object = MibTableColumn
cucsPkiEpFsmInstanceId = _CucsPkiEpFsmInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 1),
    _CucsPkiEpFsmInstanceId_Type()
)
cucsPkiEpFsmInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiEpFsmInstanceId.setStatus("current")
_CucsPkiEpFsmDn_Type = CucsManagedObjectDn
_CucsPkiEpFsmDn_Object = MibTableColumn
cucsPkiEpFsmDn = _CucsPkiEpFsmDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 2),
    _CucsPkiEpFsmDn_Type()
)
cucsPkiEpFsmDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmDn.setStatus("current")
_CucsPkiEpFsmRn_Type = SnmpAdminString
_CucsPkiEpFsmRn_Object = MibTableColumn
cucsPkiEpFsmRn = _CucsPkiEpFsmRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 3),
    _CucsPkiEpFsmRn_Type()
)
cucsPkiEpFsmRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRn.setStatus("current")
_CucsPkiEpFsmCompletionTime_Type = DateAndTime
_CucsPkiEpFsmCompletionTime_Object = MibTableColumn
cucsPkiEpFsmCompletionTime = _CucsPkiEpFsmCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 4),
    _CucsPkiEpFsmCompletionTime_Type()
)
cucsPkiEpFsmCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmCompletionTime.setStatus("current")
_CucsPkiEpFsmCurrentFsm_Type = CucsPkiEpFsmCurrentFsm
_CucsPkiEpFsmCurrentFsm_Object = MibTableColumn
cucsPkiEpFsmCurrentFsm = _CucsPkiEpFsmCurrentFsm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 5),
    _CucsPkiEpFsmCurrentFsm_Type()
)
cucsPkiEpFsmCurrentFsm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmCurrentFsm.setStatus("current")
_CucsPkiEpFsmDescrData_Type = SnmpAdminString
_CucsPkiEpFsmDescrData_Object = MibTableColumn
cucsPkiEpFsmDescrData = _CucsPkiEpFsmDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 6),
    _CucsPkiEpFsmDescrData_Type()
)
cucsPkiEpFsmDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmDescrData.setStatus("current")
_CucsPkiEpFsmFsmStatus_Type = CucsFsmFsmStageStatus
_CucsPkiEpFsmFsmStatus_Object = MibTableColumn
cucsPkiEpFsmFsmStatus = _CucsPkiEpFsmFsmStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 7),
    _CucsPkiEpFsmFsmStatus_Type()
)
cucsPkiEpFsmFsmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmFsmStatus.setStatus("current")
_CucsPkiEpFsmProgress_Type = Gauge32
_CucsPkiEpFsmProgress_Object = MibTableColumn
cucsPkiEpFsmProgress = _CucsPkiEpFsmProgress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 8),
    _CucsPkiEpFsmProgress_Type()
)
cucsPkiEpFsmProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmProgress.setStatus("current")
_CucsPkiEpFsmRmtErrCode_Type = Gauge32
_CucsPkiEpFsmRmtErrCode_Object = MibTableColumn
cucsPkiEpFsmRmtErrCode = _CucsPkiEpFsmRmtErrCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 9),
    _CucsPkiEpFsmRmtErrCode_Type()
)
cucsPkiEpFsmRmtErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtErrCode.setStatus("current")
_CucsPkiEpFsmRmtErrDescr_Type = SnmpAdminString
_CucsPkiEpFsmRmtErrDescr_Object = MibTableColumn
cucsPkiEpFsmRmtErrDescr = _CucsPkiEpFsmRmtErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 10),
    _CucsPkiEpFsmRmtErrDescr_Type()
)
cucsPkiEpFsmRmtErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtErrDescr.setStatus("current")
_CucsPkiEpFsmRmtRslt_Type = CucsConditionRemoteInvRslt
_CucsPkiEpFsmRmtRslt_Object = MibTableColumn
cucsPkiEpFsmRmtRslt = _CucsPkiEpFsmRmtRslt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 6, 1, 11),
    _CucsPkiEpFsmRmtRslt_Type()
)
cucsPkiEpFsmRmtRslt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmRmtRslt.setStatus("current")
_CucsPkiEpFsmStageTable_Object = MibTable
cucsPkiEpFsmStageTable = _CucsPkiEpFsmStageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7)
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageTable.setStatus("current")
_CucsPkiEpFsmStageEntry_Object = MibTableRow
cucsPkiEpFsmStageEntry = _CucsPkiEpFsmStageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1)
)
cucsPkiEpFsmStageEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PKI-MIB", "cucsPkiEpFsmStageInstanceId"),
)
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageEntry.setStatus("current")
_CucsPkiEpFsmStageInstanceId_Type = CucsManagedObjectId
_CucsPkiEpFsmStageInstanceId_Object = MibTableColumn
cucsPkiEpFsmStageInstanceId = _CucsPkiEpFsmStageInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 1),
    _CucsPkiEpFsmStageInstanceId_Type()
)
cucsPkiEpFsmStageInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageInstanceId.setStatus("current")
_CucsPkiEpFsmStageDn_Type = CucsManagedObjectDn
_CucsPkiEpFsmStageDn_Object = MibTableColumn
cucsPkiEpFsmStageDn = _CucsPkiEpFsmStageDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 2),
    _CucsPkiEpFsmStageDn_Type()
)
cucsPkiEpFsmStageDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageDn.setStatus("current")
_CucsPkiEpFsmStageRn_Type = SnmpAdminString
_CucsPkiEpFsmStageRn_Object = MibTableColumn
cucsPkiEpFsmStageRn = _CucsPkiEpFsmStageRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 3),
    _CucsPkiEpFsmStageRn_Type()
)
cucsPkiEpFsmStageRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageRn.setStatus("current")
_CucsPkiEpFsmStageDescrData_Type = SnmpAdminString
_CucsPkiEpFsmStageDescrData_Object = MibTableColumn
cucsPkiEpFsmStageDescrData = _CucsPkiEpFsmStageDescrData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 4),
    _CucsPkiEpFsmStageDescrData_Type()
)
cucsPkiEpFsmStageDescrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageDescrData.setStatus("current")
_CucsPkiEpFsmStageLastUpdateTime_Type = DateAndTime
_CucsPkiEpFsmStageLastUpdateTime_Object = MibTableColumn
cucsPkiEpFsmStageLastUpdateTime = _CucsPkiEpFsmStageLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 5),
    _CucsPkiEpFsmStageLastUpdateTime_Type()
)
cucsPkiEpFsmStageLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageLastUpdateTime.setStatus("current")
_CucsPkiEpFsmStageName_Type = CucsPkiEpFsmStageName
_CucsPkiEpFsmStageName_Object = MibTableColumn
cucsPkiEpFsmStageName = _CucsPkiEpFsmStageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 6),
    _CucsPkiEpFsmStageName_Type()
)
cucsPkiEpFsmStageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageName.setStatus("current")
_CucsPkiEpFsmStageOrder_Type = Gauge32
_CucsPkiEpFsmStageOrder_Object = MibTableColumn
cucsPkiEpFsmStageOrder = _CucsPkiEpFsmStageOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 7),
    _CucsPkiEpFsmStageOrder_Type()
)
cucsPkiEpFsmStageOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageOrder.setStatus("current")
_CucsPkiEpFsmStageRetry_Type = Gauge32
_CucsPkiEpFsmStageRetry_Object = MibTableColumn
cucsPkiEpFsmStageRetry = _CucsPkiEpFsmStageRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 8),
    _CucsPkiEpFsmStageRetry_Type()
)
cucsPkiEpFsmStageRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageRetry.setStatus("current")
_CucsPkiEpFsmStageStageStatus_Type = CucsFsmFsmStageStatus
_CucsPkiEpFsmStageStageStatus_Object = MibTableColumn
cucsPkiEpFsmStageStageStatus = _CucsPkiEpFsmStageStageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 37, 7, 1, 9),
    _CucsPkiEpFsmStageStageStatus_Type()
)
cucsPkiEpFsmStageStageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsPkiEpFsmStageStageStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-PKI-MIB",
    **{"cucsPkiObjects": cucsPkiObjects,
       "cucsPkiCertReqTable": cucsPkiCertReqTable,
       "cucsPkiCertReqEntry": cucsPkiCertReqEntry,
       "cucsPkiCertReqInstanceId": cucsPkiCertReqInstanceId,
       "cucsPkiCertReqDn": cucsPkiCertReqDn,
       "cucsPkiCertReqRn": cucsPkiCertReqRn,
       "cucsPkiCertReqIp": cucsPkiCertReqIp,
       "cucsPkiCertReqPwd": cucsPkiCertReqPwd,
       "cucsPkiCertReqReq": cucsPkiCertReqReq,
       "cucsPkiCertReqSubjName": cucsPkiCertReqSubjName,
       "cucsPkiCertReqCountry": cucsPkiCertReqCountry,
       "cucsPkiCertReqDns": cucsPkiCertReqDns,
       "cucsPkiCertReqEmail": cucsPkiCertReqEmail,
       "cucsPkiCertReqLocality": cucsPkiCertReqLocality,
       "cucsPkiCertReqOrgName": cucsPkiCertReqOrgName,
       "cucsPkiCertReqOrgUnitName": cucsPkiCertReqOrgUnitName,
       "cucsPkiCertReqState": cucsPkiCertReqState,
       "cucsPkiCertReqIpA": cucsPkiCertReqIpA,
       "cucsPkiCertReqIpB": cucsPkiCertReqIpB,
       "cucsPkiCertReqIpv6": cucsPkiCertReqIpv6,
       "cucsPkiCertReqIpv6A": cucsPkiCertReqIpv6A,
       "cucsPkiCertReqIpv6B": cucsPkiCertReqIpv6B,
       "cucsPkiEpTable": cucsPkiEpTable,
       "cucsPkiEpEntry": cucsPkiEpEntry,
       "cucsPkiEpInstanceId": cucsPkiEpInstanceId,
       "cucsPkiEpDn": cucsPkiEpDn,
       "cucsPkiEpRn": cucsPkiEpRn,
       "cucsPkiEpDescr": cucsPkiEpDescr,
       "cucsPkiEpFsmDescr": cucsPkiEpFsmDescr,
       "cucsPkiEpFsmPrev": cucsPkiEpFsmPrev,
       "cucsPkiEpFsmProgr": cucsPkiEpFsmProgr,
       "cucsPkiEpFsmRmtInvErrCode": cucsPkiEpFsmRmtInvErrCode,
       "cucsPkiEpFsmRmtInvErrDescr": cucsPkiEpFsmRmtInvErrDescr,
       "cucsPkiEpFsmRmtInvRslt": cucsPkiEpFsmRmtInvRslt,
       "cucsPkiEpFsmStageDescr": cucsPkiEpFsmStageDescr,
       "cucsPkiEpFsmStamp": cucsPkiEpFsmStamp,
       "cucsPkiEpFsmStatus": cucsPkiEpFsmStatus,
       "cucsPkiEpFsmTry": cucsPkiEpFsmTry,
       "cucsPkiEpIntId": cucsPkiEpIntId,
       "cucsPkiEpName": cucsPkiEpName,
       "cucsPkiEpPolicyLevel": cucsPkiEpPolicyLevel,
       "cucsPkiEpPolicyOwner": cucsPkiEpPolicyOwner,
       "cucsPkiEpFsmTaskTable": cucsPkiEpFsmTaskTable,
       "cucsPkiEpFsmTaskEntry": cucsPkiEpFsmTaskEntry,
       "cucsPkiEpFsmTaskInstanceId": cucsPkiEpFsmTaskInstanceId,
       "cucsPkiEpFsmTaskDn": cucsPkiEpFsmTaskDn,
       "cucsPkiEpFsmTaskRn": cucsPkiEpFsmTaskRn,
       "cucsPkiEpFsmTaskCompletion": cucsPkiEpFsmTaskCompletion,
       "cucsPkiEpFsmTaskFlags": cucsPkiEpFsmTaskFlags,
       "cucsPkiEpFsmTaskItem": cucsPkiEpFsmTaskItem,
       "cucsPkiEpFsmTaskSeqId": cucsPkiEpFsmTaskSeqId,
       "cucsPkiKeyRingTable": cucsPkiKeyRingTable,
       "cucsPkiKeyRingEntry": cucsPkiKeyRingEntry,
       "cucsPkiKeyRingInstanceId": cucsPkiKeyRingInstanceId,
       "cucsPkiKeyRingDn": cucsPkiKeyRingDn,
       "cucsPkiKeyRingRn": cucsPkiKeyRingRn,
       "cucsPkiKeyRingAdminState": cucsPkiKeyRingAdminState,
       "cucsPkiKeyRingCert": cucsPkiKeyRingCert,
       "cucsPkiKeyRingDescr": cucsPkiKeyRingDescr,
       "cucsPkiKeyRingIntId": cucsPkiKeyRingIntId,
       "cucsPkiKeyRingKey": cucsPkiKeyRingKey,
       "cucsPkiKeyRingModulus": cucsPkiKeyRingModulus,
       "cucsPkiKeyRingName": cucsPkiKeyRingName,
       "cucsPkiKeyRingRegen": cucsPkiKeyRingRegen,
       "cucsPkiKeyRingTp": cucsPkiKeyRingTp,
       "cucsPkiKeyRingCertStatus": cucsPkiKeyRingCertStatus,
       "cucsPkiKeyRingConfigState": cucsPkiKeyRingConfigState,
       "cucsPkiKeyRingConfigStatusMessage": cucsPkiKeyRingConfigStatusMessage,
       "cucsPkiKeyRingPolicyLevel": cucsPkiKeyRingPolicyLevel,
       "cucsPkiKeyRingPolicyOwner": cucsPkiKeyRingPolicyOwner,
       "cucsPkiTPTable": cucsPkiTPTable,
       "cucsPkiTPEntry": cucsPkiTPEntry,
       "cucsPkiTPInstanceId": cucsPkiTPInstanceId,
       "cucsPkiTPDn": cucsPkiTPDn,
       "cucsPkiTPRn": cucsPkiTPRn,
       "cucsPkiTPCertChain": cucsPkiTPCertChain,
       "cucsPkiTPDescr": cucsPkiTPDescr,
       "cucsPkiTPFp": cucsPkiTPFp,
       "cucsPkiTPIntId": cucsPkiTPIntId,
       "cucsPkiTPName": cucsPkiTPName,
       "cucsPkiTPNumCerts": cucsPkiTPNumCerts,
       "cucsPkiTPCertStatus": cucsPkiTPCertStatus,
       "cucsPkiTPPolicyLevel": cucsPkiTPPolicyLevel,
       "cucsPkiTPPolicyOwner": cucsPkiTPPolicyOwner,
       "cucsPkiEpFsmTable": cucsPkiEpFsmTable,
       "cucsPkiEpFsmEntry": cucsPkiEpFsmEntry,
       "cucsPkiEpFsmInstanceId": cucsPkiEpFsmInstanceId,
       "cucsPkiEpFsmDn": cucsPkiEpFsmDn,
       "cucsPkiEpFsmRn": cucsPkiEpFsmRn,
       "cucsPkiEpFsmCompletionTime": cucsPkiEpFsmCompletionTime,
       "cucsPkiEpFsmCurrentFsm": cucsPkiEpFsmCurrentFsm,
       "cucsPkiEpFsmDescrData": cucsPkiEpFsmDescrData,
       "cucsPkiEpFsmFsmStatus": cucsPkiEpFsmFsmStatus,
       "cucsPkiEpFsmProgress": cucsPkiEpFsmProgress,
       "cucsPkiEpFsmRmtErrCode": cucsPkiEpFsmRmtErrCode,
       "cucsPkiEpFsmRmtErrDescr": cucsPkiEpFsmRmtErrDescr,
       "cucsPkiEpFsmRmtRslt": cucsPkiEpFsmRmtRslt,
       "cucsPkiEpFsmStageTable": cucsPkiEpFsmStageTable,
       "cucsPkiEpFsmStageEntry": cucsPkiEpFsmStageEntry,
       "cucsPkiEpFsmStageInstanceId": cucsPkiEpFsmStageInstanceId,
       "cucsPkiEpFsmStageDn": cucsPkiEpFsmStageDn,
       "cucsPkiEpFsmStageRn": cucsPkiEpFsmStageRn,
       "cucsPkiEpFsmStageDescrData": cucsPkiEpFsmStageDescrData,
       "cucsPkiEpFsmStageLastUpdateTime": cucsPkiEpFsmStageLastUpdateTime,
       "cucsPkiEpFsmStageName": cucsPkiEpFsmStageName,
       "cucsPkiEpFsmStageOrder": cucsPkiEpFsmStageOrder,
       "cucsPkiEpFsmStageRetry": cucsPkiEpFsmStageRetry,
       "cucsPkiEpFsmStageStageStatus": cucsPkiEpFsmStageStageStatus}
)
