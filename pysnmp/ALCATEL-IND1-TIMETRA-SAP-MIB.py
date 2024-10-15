# SNMP MIB module (ALCATEL-IND1-TIMETRA-SAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-SAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:14 2024
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

(TFilterID,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-FILTER-MIB",
    "TFilterID")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(TAdaptationRule,
 TBurstPercentOrDefault,
 TBurstSize,
 tSchedulerPolicyName,
 tVirtualSchedulerName) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-QOS-MIB",
    "TAdaptationRule",
    "TBurstPercentOrDefault",
    "TBurstSize",
    "tSchedulerPolicyName",
    "tVirtualSchedulerName")

(BridgeId,
 CemSapEcid,
 CemSapReportAlarm,
 ConfigStatus,
 L2ptProtocols,
 MstiInstanceIdOrZero,
 MvplsPruneState,
 ServObjDesc,
 ServObjName,
 ServType,
 StpExceptionCondition,
 StpPortRole,
 StpProtocol,
 TQosQueueAttribute,
 TSapEgrQueueId,
 TSapIngQueueId,
 TStpPortState,
 TVirtSchedAttribute,
 TdmOptionsCasTrunkFraming,
 TlsLimitMacMove,
 TlsLimitMacMoveLevel,
 VpnId,
 custId,
 hostConnectivityChAddr,
 hostConnectivityCiAddr,
 hostConnectivityCiAddrType,
 protectedMacForNotify,
 staticHostDynamicMacConflict,
 staticHostDynamicMacIpAddress,
 svcDhcpClientLease,
 svcDhcpCoAError,
 svcDhcpLseStateNewChAddr,
 svcDhcpLseStateNewCiAddr,
 svcDhcpLseStateOldChAddr,
 svcDhcpLseStateOldCiAddr,
 svcDhcpLseStatePopulateError,
 svcDhcpPacketProblem,
 svcDhcpProxyError,
 svcDhcpSubAuthError,
 svcId,
 svcTlsMacMoveMaxRate,
 svcVpnId,
 tlsDHCPClientLease,
 tlsDhcpLseStateNewChAddr,
 tlsDhcpLseStateNewCiAddr,
 tlsDhcpLseStateOldChAddr,
 tlsDhcpLseStateOldCiAddr,
 tlsDhcpPacketProblem,
 tlsMstiInstanceId,
 tmnxCustomerBridgeId,
 tmnxCustomerRootBridgeId,
 tmnxOtherBridgeId,
 tmnxServConformance,
 tmnxServNotifications,
 tmnxServObjs,
 tstpTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    "BridgeId",
    "CemSapEcid",
    "CemSapReportAlarm",
    "ConfigStatus",
    "L2ptProtocols",
    "MstiInstanceIdOrZero",
    "MvplsPruneState",
    "ServObjDesc",
    "ServObjName",
    "ServType",
    "StpExceptionCondition",
    "StpPortRole",
    "StpProtocol",
    "TQosQueueAttribute",
    "TSapEgrQueueId",
    "TSapIngQueueId",
    "TStpPortState",
    "TVirtSchedAttribute",
    "TdmOptionsCasTrunkFraming",
    "TlsLimitMacMove",
    "TlsLimitMacMoveLevel",
    "VpnId",
    "custId",
    "hostConnectivityChAddr",
    "hostConnectivityCiAddr",
    "hostConnectivityCiAddrType",
    "protectedMacForNotify",
    "staticHostDynamicMacConflict",
    "staticHostDynamicMacIpAddress",
    "svcDhcpClientLease",
    "svcDhcpCoAError",
    "svcDhcpLseStateNewChAddr",
    "svcDhcpLseStateNewCiAddr",
    "svcDhcpLseStateOldChAddr",
    "svcDhcpLseStateOldCiAddr",
    "svcDhcpLseStatePopulateError",
    "svcDhcpPacketProblem",
    "svcDhcpProxyError",
    "svcDhcpSubAuthError",
    "svcId",
    "svcTlsMacMoveMaxRate",
    "svcVpnId",
    "tlsDHCPClientLease",
    "tlsDhcpLseStateNewChAddr",
    "tlsDhcpLseStateNewCiAddr",
    "tlsDhcpLseStateOldChAddr",
    "tlsDhcpLseStateOldCiAddr",
    "tlsDhcpPacketProblem",
    "tlsMstiInstanceId",
    "tmnxCustomerBridgeId",
    "tmnxCustomerRootBridgeId",
    "tmnxOtherBridgeId",
    "tmnxServConformance",
    "tmnxServNotifications",
    "tmnxServObjs",
    "tstpTraps")

(ServiceAdminStatus,
 TCIRRate,
 TCpmProtPolicyID,
 TEgressQueueId,
 TIngressQueueId,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPIRRate,
 TPolicyStatementNameOrEmpty,
 TPortSchedulerPIR,
 TSapEgressPolicyID,
 TSapIngressPolicyID,
 TmnxActionType,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxEncapVal,
 TmnxIgmpVersion,
 TmnxOperState,
 TmnxPortID,
 TmnxServId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "ServiceAdminStatus",
    "TCIRRate",
    "TCpmProtPolicyID",
    "TEgressQueueId",
    "TIngressQueueId",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPIRRate",
    "TPolicyStatementNameOrEmpty",
    "TPortSchedulerPIR",
    "TSapEgressPolicyID",
    "TSapIngressPolicyID",
    "TmnxActionType",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxEncapVal",
    "TmnxIgmpVersion",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId")

(AtmTrafficDescrParamIndex,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmTrafficDescrParamIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

timetraSvcSapMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 55)
)
timetraSvcSapMIBModule.setRevisions(
        ("1907-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSapConformance_ObjectIdentity = ObjectIdentity
tmnxSapConformance = _TmnxSapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3)
)
_TmnxSapCompliances_ObjectIdentity = ObjectIdentity
tmnxSapCompliances = _TmnxSapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 1)
)
_TmnxSapGroups_ObjectIdentity = ObjectIdentity
tmnxSapGroups = _TmnxSapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2)
)
_TmnxSapObjs_ObjectIdentity = ObjectIdentity
tmnxSapObjs = _TmnxSapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3)
)
_SapNumEntries_Type = Integer32
_SapNumEntries_Object = MibScalar
sapNumEntries = _SapNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 1),
    _SapNumEntries_Type()
)
sapNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapNumEntries.setStatus("current")
_SapBaseInfoTable_Object = MibTable
sapBaseInfoTable = _SapBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    sapBaseInfoTable.setStatus("current")
_SapBaseInfoEntry_Object = MibTableRow
sapBaseInfoEntry = _SapBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1)
)
sapBaseInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapBaseInfoEntry.setStatus("current")
_SapPortId_Type = TmnxPortID
_SapPortId_Object = MibTableColumn
sapPortId = _SapPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 1),
    _SapPortId_Type()
)
sapPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortId.setStatus("current")
_SapEncapValue_Type = TmnxEncapVal
_SapEncapValue_Object = MibTableColumn
sapEncapValue = _SapEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 2),
    _SapEncapValue_Type()
)
sapEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEncapValue.setStatus("current")
_SapRowStatus_Type = RowStatus
_SapRowStatus_Object = MibTableColumn
sapRowStatus = _SapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 3),
    _SapRowStatus_Type()
)
sapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapRowStatus.setStatus("current")
_SapType_Type = ServType
_SapType_Object = MibTableColumn
sapType = _SapType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 4),
    _SapType_Type()
)
sapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapType.setStatus("current")
_SapDescription_Type = ServObjDesc
_SapDescription_Object = MibTableColumn
sapDescription = _SapDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 5),
    _SapDescription_Type()
)
sapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapDescription.setStatus("current")


class _SapAdminStatus_Type(ServiceAdminStatus):
    """Custom type sapAdminStatus based on ServiceAdminStatus"""


_SapAdminStatus_Object = MibTableColumn
sapAdminStatus = _SapAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 6),
    _SapAdminStatus_Type()
)
sapAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapAdminStatus.setStatus("current")


class _SapOperStatus_Type(Integer32):
    """Custom type sapOperStatus based on Integer32"""
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
        *(("down", 2),
          ("egressQosMismatch", 4),
          ("iesIfAdminDown", 7),
          ("ingressQosMismatch", 3),
          ("portMtuTooSmall", 5),
          ("svcAdminDown", 6),
          ("up", 1))
    )


_SapOperStatus_Type.__name__ = "Integer32"
_SapOperStatus_Object = MibTableColumn
sapOperStatus = _SapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 7),
    _SapOperStatus_Type()
)
sapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapOperStatus.setStatus("current")


class _SapIngressQosPolicyId_Type(TSapIngressPolicyID):
    """Custom type sapIngressQosPolicyId based on TSapIngressPolicyID"""
    defaultValue = 1


_SapIngressQosPolicyId_Object = MibTableColumn
sapIngressQosPolicyId = _SapIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 8),
    _SapIngressQosPolicyId_Type()
)
sapIngressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressQosPolicyId.setStatus("current")


class _SapIngressMacFilterId_Type(TFilterID):
    """Custom type sapIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_SapIngressMacFilterId_Object = MibTableColumn
sapIngressMacFilterId = _SapIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 9),
    _SapIngressMacFilterId_Type()
)
sapIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressMacFilterId.setStatus("current")


class _SapIngressIpFilterId_Type(TFilterID):
    """Custom type sapIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_SapIngressIpFilterId_Object = MibTableColumn
sapIngressIpFilterId = _SapIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 10),
    _SapIngressIpFilterId_Type()
)
sapIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressIpFilterId.setStatus("current")


class _SapEgressQosPolicyId_Type(TSapEgressPolicyID):
    """Custom type sapEgressQosPolicyId based on TSapEgressPolicyID"""
    defaultValue = 1


_SapEgressQosPolicyId_Object = MibTableColumn
sapEgressQosPolicyId = _SapEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 11),
    _SapEgressQosPolicyId_Type()
)
sapEgressQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressQosPolicyId.setStatus("current")


class _SapEgressMacFilterId_Type(TFilterID):
    """Custom type sapEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_SapEgressMacFilterId_Object = MibTableColumn
sapEgressMacFilterId = _SapEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 12),
    _SapEgressMacFilterId_Type()
)
sapEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressMacFilterId.setStatus("current")


class _SapEgressIpFilterId_Type(TFilterID):
    """Custom type sapEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_SapEgressIpFilterId_Object = MibTableColumn
sapEgressIpFilterId = _SapEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 13),
    _SapEgressIpFilterId_Type()
)
sapEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressIpFilterId.setStatus("current")


class _SapMirrorStatus_Type(Integer32):
    """Custom type sapMirrorStatus based on Integer32"""
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
        *(("disabled", 4),
          ("egress", 2),
          ("ingress", 1),
          ("ingressAndEgress", 3))
    )


_SapMirrorStatus_Type.__name__ = "Integer32"
_SapMirrorStatus_Object = MibTableColumn
sapMirrorStatus = _SapMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 14),
    _SapMirrorStatus_Type()
)
sapMirrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapMirrorStatus.setStatus("current")
_SapIesIfIndex_Type = InterfaceIndexOrZero
_SapIesIfIndex_Object = MibTableColumn
sapIesIfIndex = _SapIesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 15),
    _SapIesIfIndex_Type()
)
sapIesIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIesIfIndex.setStatus("current")
_SapLastMgmtChange_Type = TimeStamp
_SapLastMgmtChange_Object = MibTableColumn
sapLastMgmtChange = _SapLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 16),
    _SapLastMgmtChange_Type()
)
sapLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapLastMgmtChange.setStatus("current")


class _SapCollectAcctStats_Type(TruthValue):
    """Custom type sapCollectAcctStats based on TruthValue"""


_SapCollectAcctStats_Object = MibTableColumn
sapCollectAcctStats = _SapCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 17),
    _SapCollectAcctStats_Type()
)
sapCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapCollectAcctStats.setStatus("current")


class _SapAccountingPolicyId_Type(Unsigned32):
    """Custom type sapAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_SapAccountingPolicyId_Object = MibTableColumn
sapAccountingPolicyId = _SapAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 18),
    _SapAccountingPolicyId_Type()
)
sapAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapAccountingPolicyId.setStatus("current")
_SapVpnId_Type = VpnId
_SapVpnId_Object = MibTableColumn
sapVpnId = _SapVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 19),
    _SapVpnId_Type()
)
sapVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapVpnId.setStatus("current")
_SapCustId_Type = TmnxCustId
_SapCustId_Object = MibTableColumn
sapCustId = _SapCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 20),
    _SapCustId_Type()
)
sapCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCustId.setStatus("current")
_SapCustMultSvcSite_Type = ServObjName
_SapCustMultSvcSite_Object = MibTableColumn
sapCustMultSvcSite = _SapCustMultSvcSite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 21),
    _SapCustMultSvcSite_Type()
)
sapCustMultSvcSite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapCustMultSvcSite.setStatus("current")
_SapIngressQosSchedulerPolicy_Type = ServObjName
_SapIngressQosSchedulerPolicy_Object = MibTableColumn
sapIngressQosSchedulerPolicy = _SapIngressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 22),
    _SapIngressQosSchedulerPolicy_Type()
)
sapIngressQosSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressQosSchedulerPolicy.setStatus("current")
_SapEgressQosSchedulerPolicy_Type = ServObjName
_SapEgressQosSchedulerPolicy_Object = MibTableColumn
sapEgressQosSchedulerPolicy = _SapEgressQosSchedulerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 23),
    _SapEgressQosSchedulerPolicy_Type()
)
sapEgressQosSchedulerPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressQosSchedulerPolicy.setStatus("current")
_SapSplitHorizonGrp_Type = ServObjName
_SapSplitHorizonGrp_Object = MibTableColumn
sapSplitHorizonGrp = _SapSplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 24),
    _SapSplitHorizonGrp_Type()
)
sapSplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSplitHorizonGrp.setStatus("current")
_SapIngressSharedQueuePolicy_Type = ServObjName
_SapIngressSharedQueuePolicy_Object = MibTableColumn
sapIngressSharedQueuePolicy = _SapIngressSharedQueuePolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 25),
    _SapIngressSharedQueuePolicy_Type()
)
sapIngressSharedQueuePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressSharedQueuePolicy.setStatus("current")


class _SapIngressMatchQinQDot1PBits_Type(Integer32):
    """Custom type sapIngressMatchQinQDot1PBits based on Integer32"""
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
        *(("bottom", 3),
          ("default", 1),
          ("top", 2))
    )


_SapIngressMatchQinQDot1PBits_Type.__name__ = "Integer32"
_SapIngressMatchQinQDot1PBits_Object = MibTableColumn
sapIngressMatchQinQDot1PBits = _SapIngressMatchQinQDot1PBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 26),
    _SapIngressMatchQinQDot1PBits_Type()
)
sapIngressMatchQinQDot1PBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressMatchQinQDot1PBits.setStatus("current")


class _SapOperFlags_Type(Bits):
    """Custom type sapOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("egressNamedPoolMismatch", 19),
          ("egressQosMismatch", 7),
          ("iesIfAdminDown", 2),
          ("ingressNamedPoolMismatch", 18),
          ("ingressQosMismatch", 6),
          ("ipMirrorNoMacAddr", 20),
          ("l2OperDown", 5),
          ("portMtuTooSmall", 4),
          ("portOperDown", 3),
          ("recProtSrcMac", 9),
          ("relearnLimitExceeded", 8),
          ("sapAdminDown", 0),
          ("sapCemNoEcidOrMacAddr", 15),
          ("sapEpipeNoRingNode", 21),
          ("sapIpipeNoCeIpAddr", 11),
          ("sapParamMismatch", 14),
          ("sapStandbyForMcRing", 16),
          ("sapSvcMtuTooSmall", 17),
          ("sapTodMssResourceUnavail", 13),
          ("sapTodResourceUnavail", 12),
          ("subIfAdminDown", 10),
          ("svcAdminDown", 1))
    )

_SapOperFlags_Type.__name__ = "Bits"
_SapOperFlags_Object = MibTableColumn
sapOperFlags = _SapOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 27),
    _SapOperFlags_Type()
)
sapOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapOperFlags.setStatus("current")
_SapLastStatusChange_Type = TimeStamp
_SapLastStatusChange_Object = MibTableColumn
sapLastStatusChange = _SapLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 28),
    _SapLastStatusChange_Type()
)
sapLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapLastStatusChange.setStatus("current")


class _SapAntiSpoofing_Type(Integer32):
    """Custom type sapAntiSpoofing based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("nextHopIpAndMacAddr", 4),
          ("sourceIpAddr", 1),
          ("sourceIpAndMacAddr", 3),
          ("sourceMacAddr", 2))
    )


_SapAntiSpoofing_Type.__name__ = "Integer32"
_SapAntiSpoofing_Object = MibTableColumn
sapAntiSpoofing = _SapAntiSpoofing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 29),
    _SapAntiSpoofing_Type()
)
sapAntiSpoofing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapAntiSpoofing.setStatus("current")


class _SapIngressIpv6FilterId_Type(TFilterID):
    """Custom type sapIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SapIngressIpv6FilterId_Object = MibTableColumn
sapIngressIpv6FilterId = _SapIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 30),
    _SapIngressIpv6FilterId_Type()
)
sapIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressIpv6FilterId.setStatus("current")


class _SapEgressIpv6FilterId_Type(TFilterID):
    """Custom type sapEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SapEgressIpv6FilterId_Object = MibTableColumn
sapEgressIpv6FilterId = _SapEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 31),
    _SapEgressIpv6FilterId_Type()
)
sapEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressIpv6FilterId.setStatus("current")


class _SapTodSuite_Type(TNamedItemOrEmpty):
    """Custom type sapTodSuite based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_SapTodSuite_Object = MibTableColumn
sapTodSuite = _SapTodSuite_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 32),
    _SapTodSuite_Type()
)
sapTodSuite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapTodSuite.setStatus("current")


class _SapIngUseMultipointShared_Type(TruthValue):
    """Custom type sapIngUseMultipointShared based on TruthValue"""


_SapIngUseMultipointShared_Object = MibTableColumn
sapIngUseMultipointShared = _SapIngUseMultipointShared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 33),
    _SapIngUseMultipointShared_Type()
)
sapIngUseMultipointShared.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngUseMultipointShared.setStatus("current")


class _SapEgressQinQMarkTopOnly_Type(TruthValue):
    """Custom type sapEgressQinQMarkTopOnly based on TruthValue"""


_SapEgressQinQMarkTopOnly_Object = MibTableColumn
sapEgressQinQMarkTopOnly = _SapEgressQinQMarkTopOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 34),
    _SapEgressQinQMarkTopOnly_Type()
)
sapEgressQinQMarkTopOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressQinQMarkTopOnly.setStatus("current")


class _SapEgressAggRateLimit_Type(TPortSchedulerPIR):
    """Custom type sapEgressAggRateLimit based on TPortSchedulerPIR"""
    defaultValue = -1


_SapEgressAggRateLimit_Object = MibTableColumn
sapEgressAggRateLimit = _SapEgressAggRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 35),
    _SapEgressAggRateLimit_Type()
)
sapEgressAggRateLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressAggRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    sapEgressAggRateLimit.setUnits("kbps")
_SapEndPoint_Type = ServObjName
_SapEndPoint_Object = MibTableColumn
sapEndPoint = _SapEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 36),
    _SapEndPoint_Type()
)
sapEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEndPoint.setStatus("current")


class _SapIngressVlanTranslation_Type(Integer32):
    """Custom type sapIngressVlanTranslation based on Integer32"""
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
        *(("copyOuter", 3),
          ("none", 1),
          ("vlanId", 2))
    )


_SapIngressVlanTranslation_Type.__name__ = "Integer32"
_SapIngressVlanTranslation_Object = MibTableColumn
sapIngressVlanTranslation = _SapIngressVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 37),
    _SapIngressVlanTranslation_Type()
)
sapIngressVlanTranslation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressVlanTranslation.setStatus("current")


class _SapIngressVlanTranslationId_Type(Integer32):
    """Custom type sapIngressVlanTranslationId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 4094),
    )


_SapIngressVlanTranslationId_Type.__name__ = "Integer32"
_SapIngressVlanTranslationId_Object = MibTableColumn
sapIngressVlanTranslationId = _SapIngressVlanTranslationId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 38),
    _SapIngressVlanTranslationId_Type()
)
sapIngressVlanTranslationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngressVlanTranslationId.setStatus("current")


class _SapSubType_Type(Integer32):
    """Custom type sapSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("capture", 1),
          ("managed", 2),
          ("regular", 0))
    )


_SapSubType_Type.__name__ = "Integer32"
_SapSubType_Object = MibTableColumn
sapSubType = _SapSubType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 39),
    _SapSubType_Type()
)
sapSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubType.setStatus("current")
_SapCpmProtPolicyId_Type = TCpmProtPolicyID
_SapCpmProtPolicyId_Object = MibTableColumn
sapCpmProtPolicyId = _SapCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 40),
    _SapCpmProtPolicyId_Type()
)
sapCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapCpmProtPolicyId.setStatus("current")


class _SapCpmProtMonitorMac_Type(TruthValue):
    """Custom type sapCpmProtMonitorMac based on TruthValue"""


_SapCpmProtMonitorMac_Object = MibTableColumn
sapCpmProtMonitorMac = _SapCpmProtMonitorMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 41),
    _SapCpmProtMonitorMac_Type()
)
sapCpmProtMonitorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapCpmProtMonitorMac.setStatus("current")


class _SapEgressFrameBasedAccounting_Type(TruthValue):
    """Custom type sapEgressFrameBasedAccounting based on TruthValue"""


_SapEgressFrameBasedAccounting_Object = MibTableColumn
sapEgressFrameBasedAccounting = _SapEgressFrameBasedAccounting_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 2, 1, 42),
    _SapEgressFrameBasedAccounting_Type()
)
sapEgressFrameBasedAccounting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgressFrameBasedAccounting.setStatus("current")
_SapTlsInfoTable_Object = MibTable
sapTlsInfoTable = _SapTlsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3)
)
if mibBuilder.loadTexts:
    sapTlsInfoTable.setStatus("current")
_SapTlsInfoEntry_Object = MibTableRow
sapTlsInfoEntry = _SapTlsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1)
)
sapTlsInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapTlsInfoEntry.setStatus("current")


class _SapTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type sapTlsStpAdminStatus based on TmnxEnabledDisabled"""


_SapTlsStpAdminStatus_Object = MibTableColumn
sapTlsStpAdminStatus = _SapTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 1),
    _SapTlsStpAdminStatus_Type()
)
sapTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpAdminStatus.setStatus("current")


class _SapTlsStpPriority_Type(Integer32):
    """Custom type sapTlsStpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SapTlsStpPriority_Type.__name__ = "Integer32"
_SapTlsStpPriority_Object = MibTableColumn
sapTlsStpPriority = _SapTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 2),
    _SapTlsStpPriority_Type()
)
sapTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpPriority.setStatus("current")


class _SapTlsStpPortNum_Type(Integer32):
    """Custom type sapTlsStpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SapTlsStpPortNum_Type.__name__ = "Integer32"
_SapTlsStpPortNum_Object = MibTableColumn
sapTlsStpPortNum = _SapTlsStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 3),
    _SapTlsStpPortNum_Type()
)
sapTlsStpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpPortNum.setStatus("current")


class _SapTlsStpPathCost_Type(Integer32):
    """Custom type sapTlsStpPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SapTlsStpPathCost_Type.__name__ = "Integer32"
_SapTlsStpPathCost_Object = MibTableColumn
sapTlsStpPathCost = _SapTlsStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 4),
    _SapTlsStpPathCost_Type()
)
sapTlsStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpPathCost.setStatus("current")


class _SapTlsStpRapidStart_Type(TmnxEnabledDisabled):
    """Custom type sapTlsStpRapidStart based on TmnxEnabledDisabled"""


_SapTlsStpRapidStart_Object = MibTableColumn
sapTlsStpRapidStart = _SapTlsStpRapidStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 5),
    _SapTlsStpRapidStart_Type()
)
sapTlsStpRapidStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpRapidStart.setStatus("current")


class _SapTlsStpBpduEncap_Type(Integer32):
    """Custom type sapTlsStpBpduEncap based on Integer32"""
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
        *(("dot1d", 2),
          ("dynamic", 1),
          ("pvst", 3))
    )


_SapTlsStpBpduEncap_Type.__name__ = "Integer32"
_SapTlsStpBpduEncap_Object = MibTableColumn
sapTlsStpBpduEncap = _SapTlsStpBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 6),
    _SapTlsStpBpduEncap_Type()
)
sapTlsStpBpduEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpBpduEncap.setStatus("current")
_SapTlsStpPortState_Type = TStpPortState
_SapTlsStpPortState_Object = MibTableColumn
sapTlsStpPortState = _SapTlsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 7),
    _SapTlsStpPortState_Type()
)
sapTlsStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpPortState.setStatus("current")
_SapTlsStpDesignatedBridge_Type = BridgeId
_SapTlsStpDesignatedBridge_Object = MibTableColumn
sapTlsStpDesignatedBridge = _SapTlsStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 8),
    _SapTlsStpDesignatedBridge_Type()
)
sapTlsStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpDesignatedBridge.setStatus("current")
_SapTlsStpDesignatedPort_Type = Integer32
_SapTlsStpDesignatedPort_Object = MibTableColumn
sapTlsStpDesignatedPort = _SapTlsStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 9),
    _SapTlsStpDesignatedPort_Type()
)
sapTlsStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpDesignatedPort.setStatus("current")
_SapTlsStpForwardTransitions_Type = Gauge32
_SapTlsStpForwardTransitions_Object = MibTableColumn
sapTlsStpForwardTransitions = _SapTlsStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 10),
    _SapTlsStpForwardTransitions_Type()
)
sapTlsStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpForwardTransitions.setStatus("current")
_SapTlsStpInConfigBpdus_Type = Gauge32
_SapTlsStpInConfigBpdus_Object = MibTableColumn
sapTlsStpInConfigBpdus = _SapTlsStpInConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 11),
    _SapTlsStpInConfigBpdus_Type()
)
sapTlsStpInConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInConfigBpdus.setStatus("current")
_SapTlsStpInTcnBpdus_Type = Gauge32
_SapTlsStpInTcnBpdus_Object = MibTableColumn
sapTlsStpInTcnBpdus = _SapTlsStpInTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 12),
    _SapTlsStpInTcnBpdus_Type()
)
sapTlsStpInTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInTcnBpdus.setStatus("current")
_SapTlsStpInBadBpdus_Type = Gauge32
_SapTlsStpInBadBpdus_Object = MibTableColumn
sapTlsStpInBadBpdus = _SapTlsStpInBadBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 13),
    _SapTlsStpInBadBpdus_Type()
)
sapTlsStpInBadBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInBadBpdus.setStatus("current")
_SapTlsStpOutConfigBpdus_Type = Gauge32
_SapTlsStpOutConfigBpdus_Object = MibTableColumn
sapTlsStpOutConfigBpdus = _SapTlsStpOutConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 14),
    _SapTlsStpOutConfigBpdus_Type()
)
sapTlsStpOutConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOutConfigBpdus.setStatus("current")
_SapTlsStpOutTcnBpdus_Type = Gauge32
_SapTlsStpOutTcnBpdus_Object = MibTableColumn
sapTlsStpOutTcnBpdus = _SapTlsStpOutTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 15),
    _SapTlsStpOutTcnBpdus_Type()
)
sapTlsStpOutTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOutTcnBpdus.setStatus("current")


class _SapTlsStpOperBpduEncap_Type(Integer32):
    """Custom type sapTlsStpOperBpduEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 2),
          ("dynamic", 1),
          ("pvst", 3))
    )


_SapTlsStpOperBpduEncap_Type.__name__ = "Integer32"
_SapTlsStpOperBpduEncap_Object = MibTableColumn
sapTlsStpOperBpduEncap = _SapTlsStpOperBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 16),
    _SapTlsStpOperBpduEncap_Type()
)
sapTlsStpOperBpduEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOperBpduEncap.setStatus("current")
_SapTlsVpnId_Type = VpnId
_SapTlsVpnId_Object = MibTableColumn
sapTlsVpnId = _SapTlsVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 17),
    _SapTlsVpnId_Type()
)
sapTlsVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsVpnId.setStatus("current")
_SapTlsCustId_Type = TmnxCustId
_SapTlsCustId_Object = MibTableColumn
sapTlsCustId = _SapTlsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 18),
    _SapTlsCustId_Type()
)
sapTlsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsCustId.setStatus("current")


class _SapTlsMacAddressLimit_Type(Integer32):
    """Custom type sapTlsMacAddressLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196607),
    )


_SapTlsMacAddressLimit_Type.__name__ = "Integer32"
_SapTlsMacAddressLimit_Object = MibTableColumn
sapTlsMacAddressLimit = _SapTlsMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 19),
    _SapTlsMacAddressLimit_Type()
)
sapTlsMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMacAddressLimit.setStatus("current")
_SapTlsNumMacAddresses_Type = Integer32
_SapTlsNumMacAddresses_Object = MibTableColumn
sapTlsNumMacAddresses = _SapTlsNumMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 20),
    _SapTlsNumMacAddresses_Type()
)
sapTlsNumMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsNumMacAddresses.setStatus("current")
_SapTlsNumStaticMacAddresses_Type = Integer32
_SapTlsNumStaticMacAddresses_Object = MibTableColumn
sapTlsNumStaticMacAddresses = _SapTlsNumStaticMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 21),
    _SapTlsNumStaticMacAddresses_Type()
)
sapTlsNumStaticMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsNumStaticMacAddresses.setStatus("current")


class _SapTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type sapTlsMacLearning based on TmnxEnabledDisabled"""


_SapTlsMacLearning_Object = MibTableColumn
sapTlsMacLearning = _SapTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 22),
    _SapTlsMacLearning_Type()
)
sapTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMacLearning.setStatus("current")


class _SapTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type sapTlsMacAgeing based on TmnxEnabledDisabled"""


_SapTlsMacAgeing_Object = MibTableColumn
sapTlsMacAgeing = _SapTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 23),
    _SapTlsMacAgeing_Type()
)
sapTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMacAgeing.setStatus("current")
_SapTlsStpOperEdge_Type = TruthValue
_SapTlsStpOperEdge_Object = MibTableColumn
sapTlsStpOperEdge = _SapTlsStpOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 24),
    _SapTlsStpOperEdge_Type()
)
sapTlsStpOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOperEdge.setStatus("current")


class _SapTlsStpAdminPointToPoint_Type(Integer32):
    """Custom type sapTlsStpAdminPointToPoint based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("forceFalse", 1),
          ("forceTrue", 0))
    )


_SapTlsStpAdminPointToPoint_Type.__name__ = "Integer32"
_SapTlsStpAdminPointToPoint_Object = MibTableColumn
sapTlsStpAdminPointToPoint = _SapTlsStpAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 25),
    _SapTlsStpAdminPointToPoint_Type()
)
sapTlsStpAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpAdminPointToPoint.setStatus("current")
_SapTlsStpPortRole_Type = StpPortRole
_SapTlsStpPortRole_Object = MibTableColumn
sapTlsStpPortRole = _SapTlsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 26),
    _SapTlsStpPortRole_Type()
)
sapTlsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpPortRole.setStatus("current")


class _SapTlsStpAutoEdge_Type(TmnxEnabledDisabled):
    """Custom type sapTlsStpAutoEdge based on TmnxEnabledDisabled"""


_SapTlsStpAutoEdge_Object = MibTableColumn
sapTlsStpAutoEdge = _SapTlsStpAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 27),
    _SapTlsStpAutoEdge_Type()
)
sapTlsStpAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpAutoEdge.setStatus("current")
_SapTlsStpOperProtocol_Type = StpProtocol
_SapTlsStpOperProtocol_Object = MibTableColumn
sapTlsStpOperProtocol = _SapTlsStpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 28),
    _SapTlsStpOperProtocol_Type()
)
sapTlsStpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOperProtocol.setStatus("current")
_SapTlsStpInRstBpdus_Type = Gauge32
_SapTlsStpInRstBpdus_Object = MibTableColumn
sapTlsStpInRstBpdus = _SapTlsStpInRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 29),
    _SapTlsStpInRstBpdus_Type()
)
sapTlsStpInRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInRstBpdus.setStatus("current")
_SapTlsStpOutRstBpdus_Type = Gauge32
_SapTlsStpOutRstBpdus_Object = MibTableColumn
sapTlsStpOutRstBpdus = _SapTlsStpOutRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 30),
    _SapTlsStpOutRstBpdus_Type()
)
sapTlsStpOutRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOutRstBpdus.setStatus("current")


class _SapTlsLimitMacMove_Type(TlsLimitMacMove):
    """Custom type sapTlsLimitMacMove based on TlsLimitMacMove"""


_SapTlsLimitMacMove_Object = MibTableColumn
sapTlsLimitMacMove = _SapTlsLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 31),
    _SapTlsLimitMacMove_Type()
)
sapTlsLimitMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsLimitMacMove.setStatus("current")


class _SapTlsDhcpSnooping_Type(TmnxEnabledDisabled):
    """Custom type sapTlsDhcpSnooping based on TmnxEnabledDisabled"""


_SapTlsDhcpSnooping_Object = MibTableColumn
sapTlsDhcpSnooping = _SapTlsDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 32),
    _SapTlsDhcpSnooping_Type()
)
sapTlsDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpSnooping.setStatus("obsolete")
_SapTlsMacPinning_Type = TmnxEnabledDisabled
_SapTlsMacPinning_Object = MibTableColumn
sapTlsMacPinning = _SapTlsMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 33),
    _SapTlsMacPinning_Type()
)
sapTlsMacPinning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMacPinning.setStatus("current")


class _SapTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type sapTlsDiscardUnknownSource based on TmnxEnabledDisabled"""


_SapTlsDiscardUnknownSource_Object = MibTableColumn
sapTlsDiscardUnknownSource = _SapTlsDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 34),
    _SapTlsDiscardUnknownSource_Type()
)
sapTlsDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDiscardUnknownSource.setStatus("current")
_SapTlsMvplsPruneState_Type = MvplsPruneState
_SapTlsMvplsPruneState_Object = MibTableColumn
sapTlsMvplsPruneState = _SapTlsMvplsPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 35),
    _SapTlsMvplsPruneState_Type()
)
sapTlsMvplsPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMvplsPruneState.setStatus("current")
_SapTlsMvplsMgmtService_Type = TmnxServId
_SapTlsMvplsMgmtService_Object = MibTableColumn
sapTlsMvplsMgmtService = _SapTlsMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 36),
    _SapTlsMvplsMgmtService_Type()
)
sapTlsMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMvplsMgmtService.setStatus("current")
_SapTlsMvplsMgmtPortId_Type = TmnxPortID
_SapTlsMvplsMgmtPortId_Object = MibTableColumn
sapTlsMvplsMgmtPortId = _SapTlsMvplsMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 37),
    _SapTlsMvplsMgmtPortId_Type()
)
sapTlsMvplsMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMvplsMgmtPortId.setStatus("current")
_SapTlsMvplsMgmtEncapValue_Type = TmnxEncapVal
_SapTlsMvplsMgmtEncapValue_Object = MibTableColumn
sapTlsMvplsMgmtEncapValue = _SapTlsMvplsMgmtEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 38),
    _SapTlsMvplsMgmtEncapValue_Type()
)
sapTlsMvplsMgmtEncapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMvplsMgmtEncapValue.setStatus("current")


class _SapTlsArpReplyAgent_Type(Integer32):
    """Custom type sapTlsArpReplyAgent based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWithSubscrIdent", 3))
    )


_SapTlsArpReplyAgent_Type.__name__ = "Integer32"
_SapTlsArpReplyAgent_Object = MibTableColumn
sapTlsArpReplyAgent = _SapTlsArpReplyAgent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 39),
    _SapTlsArpReplyAgent_Type()
)
sapTlsArpReplyAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsArpReplyAgent.setStatus("current")
_SapTlsStpException_Type = StpExceptionCondition
_SapTlsStpException_Object = MibTableColumn
sapTlsStpException = _SapTlsStpException_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 40),
    _SapTlsStpException_Type()
)
sapTlsStpException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpException.setStatus("current")


class _SapTlsAuthenticationPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type sapTlsAuthenticationPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_SapTlsAuthenticationPolicy_Object = MibTableColumn
sapTlsAuthenticationPolicy = _SapTlsAuthenticationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 41),
    _SapTlsAuthenticationPolicy_Type()
)
sapTlsAuthenticationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsAuthenticationPolicy.setStatus("current")


class _SapTlsL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type sapTlsL2ptTermination based on TmnxEnabledDisabled"""


_SapTlsL2ptTermination_Object = MibTableColumn
sapTlsL2ptTermination = _SapTlsL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 42),
    _SapTlsL2ptTermination_Type()
)
sapTlsL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsL2ptTermination.setStatus("current")


class _SapTlsBpduTranslation_Type(Integer32):
    """Custom type sapTlsBpduTranslation based on Integer32"""
    defaultValue = 2

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
        *(("auto", 1),
          ("disabled", 2),
          ("pvst", 3),
          ("stp", 4))
    )


_SapTlsBpduTranslation_Type.__name__ = "Integer32"
_SapTlsBpduTranslation_Object = MibTableColumn
sapTlsBpduTranslation = _SapTlsBpduTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 43),
    _SapTlsBpduTranslation_Type()
)
sapTlsBpduTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsBpduTranslation.setStatus("current")


class _SapTlsStpRootGuard_Type(TruthValue):
    """Custom type sapTlsStpRootGuard based on TruthValue"""


_SapTlsStpRootGuard_Object = MibTableColumn
sapTlsStpRootGuard = _SapTlsStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 44),
    _SapTlsStpRootGuard_Type()
)
sapTlsStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsStpRootGuard.setStatus("current")
_SapTlsStpInsideRegion_Type = TruthValue
_SapTlsStpInsideRegion_Object = MibTableColumn
sapTlsStpInsideRegion = _SapTlsStpInsideRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 45),
    _SapTlsStpInsideRegion_Type()
)
sapTlsStpInsideRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInsideRegion.setStatus("current")
_SapTlsEgressMcastGroup_Type = TNamedItemOrEmpty
_SapTlsEgressMcastGroup_Object = MibTableColumn
sapTlsEgressMcastGroup = _SapTlsEgressMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 46),
    _SapTlsEgressMcastGroup_Type()
)
sapTlsEgressMcastGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsEgressMcastGroup.setStatus("current")
_SapTlsStpInMstBpdus_Type = Gauge32
_SapTlsStpInMstBpdus_Object = MibTableColumn
sapTlsStpInMstBpdus = _SapTlsStpInMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 47),
    _SapTlsStpInMstBpdus_Type()
)
sapTlsStpInMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpInMstBpdus.setStatus("current")
_SapTlsStpOutMstBpdus_Type = Gauge32
_SapTlsStpOutMstBpdus_Object = MibTableColumn
sapTlsStpOutMstBpdus = _SapTlsStpOutMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 48),
    _SapTlsStpOutMstBpdus_Type()
)
sapTlsStpOutMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpOutMstBpdus.setStatus("current")


class _SapTlsRestProtSrcMac_Type(TruthValue):
    """Custom type sapTlsRestProtSrcMac based on TruthValue"""


_SapTlsRestProtSrcMac_Object = MibTableColumn
sapTlsRestProtSrcMac = _SapTlsRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 49),
    _SapTlsRestProtSrcMac_Type()
)
sapTlsRestProtSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsRestProtSrcMac.setStatus("current")


class _SapTlsRestUnprotDstMac_Type(TruthValue):
    """Custom type sapTlsRestUnprotDstMac based on TruthValue"""


_SapTlsRestUnprotDstMac_Object = MibTableColumn
sapTlsRestUnprotDstMac = _SapTlsRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 50),
    _SapTlsRestUnprotDstMac_Type()
)
sapTlsRestUnprotDstMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsRestUnprotDstMac.setStatus("current")
_SapTlsStpRxdDesigBridge_Type = BridgeId
_SapTlsStpRxdDesigBridge_Object = MibTableColumn
sapTlsStpRxdDesigBridge = _SapTlsStpRxdDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 51),
    _SapTlsStpRxdDesigBridge_Type()
)
sapTlsStpRxdDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpRxdDesigBridge.setStatus("current")
_SapTlsStpRootGuardViolation_Type = TruthValue
_SapTlsStpRootGuardViolation_Object = MibTableColumn
sapTlsStpRootGuardViolation = _SapTlsStpRootGuardViolation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 52),
    _SapTlsStpRootGuardViolation_Type()
)
sapTlsStpRootGuardViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsStpRootGuardViolation.setStatus("current")


class _SapTlsShcvAction_Type(Integer32):
    """Custom type sapTlsShcvAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("remove", 2))
    )


_SapTlsShcvAction_Type.__name__ = "Integer32"
_SapTlsShcvAction_Object = MibTableColumn
sapTlsShcvAction = _SapTlsShcvAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 53),
    _SapTlsShcvAction_Type()
)
sapTlsShcvAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsShcvAction.setStatus("current")
_SapTlsShcvSrcIp_Type = IpAddress
_SapTlsShcvSrcIp_Object = MibTableColumn
sapTlsShcvSrcIp = _SapTlsShcvSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 54),
    _SapTlsShcvSrcIp_Type()
)
sapTlsShcvSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsShcvSrcIp.setStatus("current")
_SapTlsShcvSrcMac_Type = MacAddress
_SapTlsShcvSrcMac_Object = MibTableColumn
sapTlsShcvSrcMac = _SapTlsShcvSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 55),
    _SapTlsShcvSrcMac_Type()
)
sapTlsShcvSrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsShcvSrcMac.setStatus("current")


class _SapTlsShcvInterval_Type(Unsigned32):
    """Custom type sapTlsShcvInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_SapTlsShcvInterval_Type.__name__ = "Unsigned32"
_SapTlsShcvInterval_Object = MibTableColumn
sapTlsShcvInterval = _SapTlsShcvInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 56),
    _SapTlsShcvInterval_Type()
)
sapTlsShcvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsShcvInterval.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsShcvInterval.setUnits("minutes")
_SapTlsMvplsMgmtMsti_Type = MstiInstanceIdOrZero
_SapTlsMvplsMgmtMsti_Object = MibTableColumn
sapTlsMvplsMgmtMsti = _SapTlsMvplsMgmtMsti_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 57),
    _SapTlsMvplsMgmtMsti_Type()
)
sapTlsMvplsMgmtMsti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMvplsMgmtMsti.setStatus("current")
_SapTlsMacMoveNextUpTime_Type = Unsigned32
_SapTlsMacMoveNextUpTime_Object = MibTableColumn
sapTlsMacMoveNextUpTime = _SapTlsMacMoveNextUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 58),
    _SapTlsMacMoveNextUpTime_Type()
)
sapTlsMacMoveNextUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMacMoveNextUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsMacMoveNextUpTime.setUnits("seconds")
_SapTlsMacMoveRateExcdLeft_Type = Unsigned32
_SapTlsMacMoveRateExcdLeft_Object = MibTableColumn
sapTlsMacMoveRateExcdLeft = _SapTlsMacMoveRateExcdLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 59),
    _SapTlsMacMoveRateExcdLeft_Type()
)
sapTlsMacMoveRateExcdLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMacMoveRateExcdLeft.setStatus("current")


class _SapTlsRestProtSrcMacAction_Type(Integer32):
    """Custom type sapTlsRestProtSrcMacAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-only", 2),
          ("disable", 1))
    )


_SapTlsRestProtSrcMacAction_Type.__name__ = "Integer32"
_SapTlsRestProtSrcMacAction_Object = MibTableColumn
sapTlsRestProtSrcMacAction = _SapTlsRestProtSrcMacAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 60),
    _SapTlsRestProtSrcMacAction_Type()
)
sapTlsRestProtSrcMacAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsRestProtSrcMacAction.setStatus("current")


class _SapTlsL2ptForceBoundary_Type(TruthValue):
    """Custom type sapTlsL2ptForceBoundary based on TruthValue"""


_SapTlsL2ptForceBoundary_Object = MibTableColumn
sapTlsL2ptForceBoundary = _SapTlsL2ptForceBoundary_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 61),
    _SapTlsL2ptForceBoundary_Type()
)
sapTlsL2ptForceBoundary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsL2ptForceBoundary.setStatus("current")


class _SapTlsLimitMacMoveLevel_Type(TlsLimitMacMoveLevel):
    """Custom type sapTlsLimitMacMoveLevel based on TlsLimitMacMoveLevel"""


_SapTlsLimitMacMoveLevel_Object = MibTableColumn
sapTlsLimitMacMoveLevel = _SapTlsLimitMacMoveLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 62),
    _SapTlsLimitMacMoveLevel_Type()
)
sapTlsLimitMacMoveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsLimitMacMoveLevel.setStatus("current")


class _SapTlsBpduTransOper_Type(Integer32):
    """Custom type sapTlsBpduTransOper based on Integer32"""
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
        *(("disabled", 2),
          ("pvst", 3),
          ("stp", 4),
          ("undefined", 1))
    )


_SapTlsBpduTransOper_Type.__name__ = "Integer32"
_SapTlsBpduTransOper_Object = MibTableColumn
sapTlsBpduTransOper = _SapTlsBpduTransOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 63),
    _SapTlsBpduTransOper_Type()
)
sapTlsBpduTransOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsBpduTransOper.setStatus("current")
_SapTlsDefMsapPolicy_Type = TPolicyStatementNameOrEmpty
_SapTlsDefMsapPolicy_Object = MibTableColumn
sapTlsDefMsapPolicy = _SapTlsDefMsapPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 64),
    _SapTlsDefMsapPolicy_Type()
)
sapTlsDefMsapPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDefMsapPolicy.setStatus("current")


class _SapTlsL2ptProtocols_Type(L2ptProtocols):
    """Custom type sapTlsL2ptProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_SapTlsL2ptProtocols_Object = MibTableColumn
sapTlsL2ptProtocols = _SapTlsL2ptProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 65),
    _SapTlsL2ptProtocols_Type()
)
sapTlsL2ptProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsL2ptProtocols.setStatus("current")


class _SapTlsL2ptForceProtocols_Type(L2ptProtocols):
    """Custom type sapTlsL2ptForceProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_SapTlsL2ptForceProtocols_Object = MibTableColumn
sapTlsL2ptForceProtocols = _SapTlsL2ptForceProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 66),
    _SapTlsL2ptForceProtocols_Type()
)
sapTlsL2ptForceProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsL2ptForceProtocols.setStatus("current")


class _SapTlsPppoeMsapTrigger_Type(TruthValue):
    """Custom type sapTlsPppoeMsapTrigger based on TruthValue"""


_SapTlsPppoeMsapTrigger_Object = MibTableColumn
sapTlsPppoeMsapTrigger = _SapTlsPppoeMsapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 67),
    _SapTlsPppoeMsapTrigger_Type()
)
sapTlsPppoeMsapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsPppoeMsapTrigger.setStatus("current")


class _SapTlsDhcpMsapTrigger_Type(TruthValue):
    """Custom type sapTlsDhcpMsapTrigger based on TruthValue"""


_SapTlsDhcpMsapTrigger_Object = MibTableColumn
sapTlsDhcpMsapTrigger = _SapTlsDhcpMsapTrigger_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 68),
    _SapTlsDhcpMsapTrigger_Type()
)
sapTlsDhcpMsapTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpMsapTrigger.setStatus("current")


class _SapTlsMrpJoinTime_Type(Unsigned32):
    """Custom type sapTlsMrpJoinTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SapTlsMrpJoinTime_Type.__name__ = "Unsigned32"
_SapTlsMrpJoinTime_Object = MibTableColumn
sapTlsMrpJoinTime = _SapTlsMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 69),
    _SapTlsMrpJoinTime_Type()
)
sapTlsMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMrpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsMrpJoinTime.setUnits("deci-seconds")


class _SapTlsMrpLeaveTime_Type(Unsigned32):
    """Custom type sapTlsMrpLeaveTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_SapTlsMrpLeaveTime_Type.__name__ = "Unsigned32"
_SapTlsMrpLeaveTime_Object = MibTableColumn
sapTlsMrpLeaveTime = _SapTlsMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 70),
    _SapTlsMrpLeaveTime_Type()
)
sapTlsMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMrpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsMrpLeaveTime.setUnits("deci-seconds")


class _SapTlsMrpLeaveAllTime_Type(Unsigned32):
    """Custom type sapTlsMrpLeaveAllTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_SapTlsMrpLeaveAllTime_Type.__name__ = "Unsigned32"
_SapTlsMrpLeaveAllTime_Object = MibTableColumn
sapTlsMrpLeaveAllTime = _SapTlsMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 71),
    _SapTlsMrpLeaveAllTime_Type()
)
sapTlsMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMrpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsMrpLeaveAllTime.setUnits("deci-seconds")


class _SapTlsMrpPeriodicTime_Type(Unsigned32):
    """Custom type sapTlsMrpPeriodicTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SapTlsMrpPeriodicTime_Type.__name__ = "Unsigned32"
_SapTlsMrpPeriodicTime_Object = MibTableColumn
sapTlsMrpPeriodicTime = _SapTlsMrpPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 72),
    _SapTlsMrpPeriodicTime_Type()
)
sapTlsMrpPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMrpPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsMrpPeriodicTime.setUnits("deci-seconds")


class _SapTlsMrpPeriodicEnabled_Type(TruthValue):
    """Custom type sapTlsMrpPeriodicEnabled based on TruthValue"""


_SapTlsMrpPeriodicEnabled_Object = MibTableColumn
sapTlsMrpPeriodicEnabled = _SapTlsMrpPeriodicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 3, 1, 73),
    _SapTlsMrpPeriodicEnabled_Type()
)
sapTlsMrpPeriodicEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMrpPeriodicEnabled.setStatus("current")
_SapAtmInfoTable_Object = MibTable
sapAtmInfoTable = _SapAtmInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4)
)
if mibBuilder.loadTexts:
    sapAtmInfoTable.setStatus("current")
_SapAtmInfoEntry_Object = MibTableRow
sapAtmInfoEntry = _SapAtmInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1)
)
sapAtmInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapAtmInfoEntry.setStatus("current")


class _SapAtmEncapsulation_Type(Integer32):
    """Custom type sapAtmEncapsulation based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("llcSnapBridgedProtocol8023", 11),
          ("llcSnapRoutedProtocol", 7),
          ("multiprotocolFrameRelaySscs", 8),
          ("unknown", 10),
          ("vcMultiplexBridgedProtocol8023", 2),
          ("vcMultiplexRoutedProtocol", 1))
    )


_SapAtmEncapsulation_Type.__name__ = "Integer32"
_SapAtmEncapsulation_Object = MibTableColumn
sapAtmEncapsulation = _SapAtmEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 1),
    _SapAtmEncapsulation_Type()
)
sapAtmEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmEncapsulation.setStatus("current")


class _SapAtmIngressTrafficDescIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type sapAtmIngressTrafficDescIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1

    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SapAtmIngressTrafficDescIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_SapAtmIngressTrafficDescIndex_Object = MibTableColumn
sapAtmIngressTrafficDescIndex = _SapAtmIngressTrafficDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 2),
    _SapAtmIngressTrafficDescIndex_Type()
)
sapAtmIngressTrafficDescIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmIngressTrafficDescIndex.setStatus("current")


class _SapAtmEgressTrafficDescIndex_Type(AtmTrafficDescrParamIndex):
    """Custom type sapAtmEgressTrafficDescIndex based on AtmTrafficDescrParamIndex"""
    defaultValue = 1

    subtypeSpec = AtmTrafficDescrParamIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SapAtmEgressTrafficDescIndex_Type.__name__ = "AtmTrafficDescrParamIndex"
_SapAtmEgressTrafficDescIndex_Object = MibTableColumn
sapAtmEgressTrafficDescIndex = _SapAtmEgressTrafficDescIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 3),
    _SapAtmEgressTrafficDescIndex_Type()
)
sapAtmEgressTrafficDescIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmEgressTrafficDescIndex.setStatus("current")


class _SapAtmOamAlarmCellHandling_Type(ServiceAdminStatus):
    """Custom type sapAtmOamAlarmCellHandling based on ServiceAdminStatus"""


_SapAtmOamAlarmCellHandling_Object = MibTableColumn
sapAtmOamAlarmCellHandling = _SapAtmOamAlarmCellHandling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 4),
    _SapAtmOamAlarmCellHandling_Type()
)
sapAtmOamAlarmCellHandling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmOamAlarmCellHandling.setStatus("current")


class _SapAtmOamTerminate_Type(ServiceAdminStatus):
    """Custom type sapAtmOamTerminate based on ServiceAdminStatus"""


_SapAtmOamTerminate_Object = MibTableColumn
sapAtmOamTerminate = _SapAtmOamTerminate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 5),
    _SapAtmOamTerminate_Type()
)
sapAtmOamTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmOamTerminate.setStatus("current")


class _SapAtmOamPeriodicLoopback_Type(ServiceAdminStatus):
    """Custom type sapAtmOamPeriodicLoopback based on ServiceAdminStatus"""


_SapAtmOamPeriodicLoopback_Object = MibTableColumn
sapAtmOamPeriodicLoopback = _SapAtmOamPeriodicLoopback_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 4, 1, 6),
    _SapAtmOamPeriodicLoopback_Type()
)
sapAtmOamPeriodicLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapAtmOamPeriodicLoopback.setStatus("current")
_SapBaseStatsTable_Object = MibTable
sapBaseStatsTable = _SapBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6)
)
if mibBuilder.loadTexts:
    sapBaseStatsTable.setStatus("current")
_SapBaseStatsEntry_Object = MibTableRow
sapBaseStatsEntry = _SapBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1)
)
sapBaseStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapBaseStatsEntry.setStatus("current")
_SapBaseStatsIngressPchipDroppedPackets_Type = Counter64
_SapBaseStatsIngressPchipDroppedPackets_Object = MibTableColumn
sapBaseStatsIngressPchipDroppedPackets = _SapBaseStatsIngressPchipDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 1),
    _SapBaseStatsIngressPchipDroppedPackets_Type()
)
sapBaseStatsIngressPchipDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipDroppedPackets.setStatus("current")
_SapBaseStatsIngressPchipDroppedOctets_Type = Counter64
_SapBaseStatsIngressPchipDroppedOctets_Object = MibTableColumn
sapBaseStatsIngressPchipDroppedOctets = _SapBaseStatsIngressPchipDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 2),
    _SapBaseStatsIngressPchipDroppedOctets_Type()
)
sapBaseStatsIngressPchipDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipDroppedOctets.setStatus("current")
_SapBaseStatsIngressPchipOfferedHiPrioPackets_Type = Counter64
_SapBaseStatsIngressPchipOfferedHiPrioPackets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedHiPrioPackets = _SapBaseStatsIngressPchipOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 3),
    _SapBaseStatsIngressPchipOfferedHiPrioPackets_Type()
)
sapBaseStatsIngressPchipOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedHiPrioPackets.setStatus("current")
_SapBaseStatsIngressPchipOfferedHiPrioOctets_Type = Counter64
_SapBaseStatsIngressPchipOfferedHiPrioOctets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedHiPrioOctets = _SapBaseStatsIngressPchipOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 4),
    _SapBaseStatsIngressPchipOfferedHiPrioOctets_Type()
)
sapBaseStatsIngressPchipOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedHiPrioOctets.setStatus("current")
_SapBaseStatsIngressPchipOfferedLoPrioPackets_Type = Counter64
_SapBaseStatsIngressPchipOfferedLoPrioPackets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedLoPrioPackets = _SapBaseStatsIngressPchipOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 5),
    _SapBaseStatsIngressPchipOfferedLoPrioPackets_Type()
)
sapBaseStatsIngressPchipOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedLoPrioPackets.setStatus("current")
_SapBaseStatsIngressPchipOfferedLoPrioOctets_Type = Counter64
_SapBaseStatsIngressPchipOfferedLoPrioOctets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedLoPrioOctets = _SapBaseStatsIngressPchipOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 6),
    _SapBaseStatsIngressPchipOfferedLoPrioOctets_Type()
)
sapBaseStatsIngressPchipOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedLoPrioOctets.setStatus("current")
_SapBaseStatsIngressQchipDroppedHiPrioPackets_Type = Counter64
_SapBaseStatsIngressQchipDroppedHiPrioPackets_Object = MibTableColumn
sapBaseStatsIngressQchipDroppedHiPrioPackets = _SapBaseStatsIngressQchipDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 7),
    _SapBaseStatsIngressQchipDroppedHiPrioPackets_Type()
)
sapBaseStatsIngressQchipDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipDroppedHiPrioPackets.setStatus("current")
_SapBaseStatsIngressQchipDroppedHiPrioOctets_Type = Counter64
_SapBaseStatsIngressQchipDroppedHiPrioOctets_Object = MibTableColumn
sapBaseStatsIngressQchipDroppedHiPrioOctets = _SapBaseStatsIngressQchipDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 8),
    _SapBaseStatsIngressQchipDroppedHiPrioOctets_Type()
)
sapBaseStatsIngressQchipDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipDroppedHiPrioOctets.setStatus("current")
_SapBaseStatsIngressQchipDroppedLoPrioPackets_Type = Counter64
_SapBaseStatsIngressQchipDroppedLoPrioPackets_Object = MibTableColumn
sapBaseStatsIngressQchipDroppedLoPrioPackets = _SapBaseStatsIngressQchipDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 9),
    _SapBaseStatsIngressQchipDroppedLoPrioPackets_Type()
)
sapBaseStatsIngressQchipDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipDroppedLoPrioPackets.setStatus("current")
_SapBaseStatsIngressQchipDroppedLoPrioOctets_Type = Counter64
_SapBaseStatsIngressQchipDroppedLoPrioOctets_Object = MibTableColumn
sapBaseStatsIngressQchipDroppedLoPrioOctets = _SapBaseStatsIngressQchipDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 10),
    _SapBaseStatsIngressQchipDroppedLoPrioOctets_Type()
)
sapBaseStatsIngressQchipDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipDroppedLoPrioOctets.setStatus("current")
_SapBaseStatsIngressQchipForwardedInProfPackets_Type = Counter64
_SapBaseStatsIngressQchipForwardedInProfPackets_Object = MibTableColumn
sapBaseStatsIngressQchipForwardedInProfPackets = _SapBaseStatsIngressQchipForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 11),
    _SapBaseStatsIngressQchipForwardedInProfPackets_Type()
)
sapBaseStatsIngressQchipForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipForwardedInProfPackets.setStatus("current")
_SapBaseStatsIngressQchipForwardedInProfOctets_Type = Counter64
_SapBaseStatsIngressQchipForwardedInProfOctets_Object = MibTableColumn
sapBaseStatsIngressQchipForwardedInProfOctets = _SapBaseStatsIngressQchipForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 12),
    _SapBaseStatsIngressQchipForwardedInProfOctets_Type()
)
sapBaseStatsIngressQchipForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipForwardedInProfOctets.setStatus("current")
_SapBaseStatsIngressQchipForwardedOutProfPackets_Type = Counter64
_SapBaseStatsIngressQchipForwardedOutProfPackets_Object = MibTableColumn
sapBaseStatsIngressQchipForwardedOutProfPackets = _SapBaseStatsIngressQchipForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 13),
    _SapBaseStatsIngressQchipForwardedOutProfPackets_Type()
)
sapBaseStatsIngressQchipForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipForwardedOutProfPackets.setStatus("current")
_SapBaseStatsIngressQchipForwardedOutProfOctets_Type = Counter64
_SapBaseStatsIngressQchipForwardedOutProfOctets_Object = MibTableColumn
sapBaseStatsIngressQchipForwardedOutProfOctets = _SapBaseStatsIngressQchipForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 14),
    _SapBaseStatsIngressQchipForwardedOutProfOctets_Type()
)
sapBaseStatsIngressQchipForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressQchipForwardedOutProfOctets.setStatus("current")
_SapBaseStatsEgressQchipDroppedInProfPackets_Type = Counter64
_SapBaseStatsEgressQchipDroppedInProfPackets_Object = MibTableColumn
sapBaseStatsEgressQchipDroppedInProfPackets = _SapBaseStatsEgressQchipDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 15),
    _SapBaseStatsEgressQchipDroppedInProfPackets_Type()
)
sapBaseStatsEgressQchipDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipDroppedInProfPackets.setStatus("current")
_SapBaseStatsEgressQchipDroppedInProfOctets_Type = Counter64
_SapBaseStatsEgressQchipDroppedInProfOctets_Object = MibTableColumn
sapBaseStatsEgressQchipDroppedInProfOctets = _SapBaseStatsEgressQchipDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 16),
    _SapBaseStatsEgressQchipDroppedInProfOctets_Type()
)
sapBaseStatsEgressQchipDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipDroppedInProfOctets.setStatus("current")
_SapBaseStatsEgressQchipDroppedOutProfPackets_Type = Counter64
_SapBaseStatsEgressQchipDroppedOutProfPackets_Object = MibTableColumn
sapBaseStatsEgressQchipDroppedOutProfPackets = _SapBaseStatsEgressQchipDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 17),
    _SapBaseStatsEgressQchipDroppedOutProfPackets_Type()
)
sapBaseStatsEgressQchipDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipDroppedOutProfPackets.setStatus("current")
_SapBaseStatsEgressQchipDroppedOutProfOctets_Type = Counter64
_SapBaseStatsEgressQchipDroppedOutProfOctets_Object = MibTableColumn
sapBaseStatsEgressQchipDroppedOutProfOctets = _SapBaseStatsEgressQchipDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 18),
    _SapBaseStatsEgressQchipDroppedOutProfOctets_Type()
)
sapBaseStatsEgressQchipDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipDroppedOutProfOctets.setStatus("current")
_SapBaseStatsEgressQchipForwardedInProfPackets_Type = Counter64
_SapBaseStatsEgressQchipForwardedInProfPackets_Object = MibTableColumn
sapBaseStatsEgressQchipForwardedInProfPackets = _SapBaseStatsEgressQchipForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 19),
    _SapBaseStatsEgressQchipForwardedInProfPackets_Type()
)
sapBaseStatsEgressQchipForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipForwardedInProfPackets.setStatus("current")
_SapBaseStatsEgressQchipForwardedInProfOctets_Type = Counter64
_SapBaseStatsEgressQchipForwardedInProfOctets_Object = MibTableColumn
sapBaseStatsEgressQchipForwardedInProfOctets = _SapBaseStatsEgressQchipForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 20),
    _SapBaseStatsEgressQchipForwardedInProfOctets_Type()
)
sapBaseStatsEgressQchipForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipForwardedInProfOctets.setStatus("current")
_SapBaseStatsEgressQchipForwardedOutProfPackets_Type = Counter64
_SapBaseStatsEgressQchipForwardedOutProfPackets_Object = MibTableColumn
sapBaseStatsEgressQchipForwardedOutProfPackets = _SapBaseStatsEgressQchipForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 21),
    _SapBaseStatsEgressQchipForwardedOutProfPackets_Type()
)
sapBaseStatsEgressQchipForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipForwardedOutProfPackets.setStatus("current")
_SapBaseStatsEgressQchipForwardedOutProfOctets_Type = Counter64
_SapBaseStatsEgressQchipForwardedOutProfOctets_Object = MibTableColumn
sapBaseStatsEgressQchipForwardedOutProfOctets = _SapBaseStatsEgressQchipForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 22),
    _SapBaseStatsEgressQchipForwardedOutProfOctets_Type()
)
sapBaseStatsEgressQchipForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsEgressQchipForwardedOutProfOctets.setStatus("current")
_SapBaseStatsCustId_Type = TmnxCustId
_SapBaseStatsCustId_Object = MibTableColumn
sapBaseStatsCustId = _SapBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 23),
    _SapBaseStatsCustId_Type()
)
sapBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsCustId.setStatus("current")
_SapBaseStatsIngressPchipOfferedUncoloredPackets_Type = Counter64
_SapBaseStatsIngressPchipOfferedUncoloredPackets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedUncoloredPackets = _SapBaseStatsIngressPchipOfferedUncoloredPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 24),
    _SapBaseStatsIngressPchipOfferedUncoloredPackets_Type()
)
sapBaseStatsIngressPchipOfferedUncoloredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedUncoloredPackets.setStatus("current")
_SapBaseStatsIngressPchipOfferedUncoloredOctets_Type = Counter64
_SapBaseStatsIngressPchipOfferedUncoloredOctets_Object = MibTableColumn
sapBaseStatsIngressPchipOfferedUncoloredOctets = _SapBaseStatsIngressPchipOfferedUncoloredOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 25),
    _SapBaseStatsIngressPchipOfferedUncoloredOctets_Type()
)
sapBaseStatsIngressPchipOfferedUncoloredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsIngressPchipOfferedUncoloredOctets.setStatus("current")
_SapBaseStatsAuthenticationPktsDiscarded_Type = Counter32
_SapBaseStatsAuthenticationPktsDiscarded_Object = MibTableColumn
sapBaseStatsAuthenticationPktsDiscarded = _SapBaseStatsAuthenticationPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 26),
    _SapBaseStatsAuthenticationPktsDiscarded_Type()
)
sapBaseStatsAuthenticationPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsAuthenticationPktsDiscarded.setStatus("current")
_SapBaseStatsAuthenticationPktsSuccess_Type = Counter32
_SapBaseStatsAuthenticationPktsSuccess_Object = MibTableColumn
sapBaseStatsAuthenticationPktsSuccess = _SapBaseStatsAuthenticationPktsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 27),
    _SapBaseStatsAuthenticationPktsSuccess_Type()
)
sapBaseStatsAuthenticationPktsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsAuthenticationPktsSuccess.setStatus("current")
_SapBaseStatsLastClearedTime_Type = TimeStamp
_SapBaseStatsLastClearedTime_Object = MibTableColumn
sapBaseStatsLastClearedTime = _SapBaseStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 6, 1, 28),
    _SapBaseStatsLastClearedTime_Type()
)
sapBaseStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapBaseStatsLastClearedTime.setStatus("current")
_SapIngQosQueueStatsTable_Object = MibTable
sapIngQosQueueStatsTable = _SapIngQosQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7)
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsTable.setStatus("current")
_SapIngQosQueueStatsEntry_Object = MibTableRow
sapIngQosQueueStatsEntry = _SapIngQosQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1)
)
sapIngQosQueueStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueId"),
)
if mibBuilder.loadTexts:
    sapIngQosQueueStatsEntry.setStatus("current")
_SapIngQosQueueId_Type = TSapIngQueueId
_SapIngQosQueueId_Object = MibTableColumn
sapIngQosQueueId = _SapIngQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 1),
    _SapIngQosQueueId_Type()
)
sapIngQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueId.setStatus("current")
_SapIngQosQueueStatsOfferedHiPrioPackets_Type = Counter64
_SapIngQosQueueStatsOfferedHiPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsOfferedHiPrioPackets = _SapIngQosQueueStatsOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 2),
    _SapIngQosQueueStatsOfferedHiPrioPackets_Type()
)
sapIngQosQueueStatsOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedHiPrioPackets.setStatus("current")
_SapIngQosQueueStatsDroppedHiPrioPackets_Type = Counter64
_SapIngQosQueueStatsDroppedHiPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsDroppedHiPrioPackets = _SapIngQosQueueStatsDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 3),
    _SapIngQosQueueStatsDroppedHiPrioPackets_Type()
)
sapIngQosQueueStatsDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedHiPrioPackets.setStatus("current")
_SapIngQosQueueStatsOfferedLoPrioPackets_Type = Counter64
_SapIngQosQueueStatsOfferedLoPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsOfferedLoPrioPackets = _SapIngQosQueueStatsOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 4),
    _SapIngQosQueueStatsOfferedLoPrioPackets_Type()
)
sapIngQosQueueStatsOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedLoPrioPackets.setStatus("current")
_SapIngQosQueueStatsDroppedLoPrioPackets_Type = Counter64
_SapIngQosQueueStatsDroppedLoPrioPackets_Object = MibTableColumn
sapIngQosQueueStatsDroppedLoPrioPackets = _SapIngQosQueueStatsDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 5),
    _SapIngQosQueueStatsDroppedLoPrioPackets_Type()
)
sapIngQosQueueStatsDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedLoPrioPackets.setStatus("current")
_SapIngQosQueueStatsOfferedHiPrioOctets_Type = Counter64
_SapIngQosQueueStatsOfferedHiPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsOfferedHiPrioOctets = _SapIngQosQueueStatsOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 6),
    _SapIngQosQueueStatsOfferedHiPrioOctets_Type()
)
sapIngQosQueueStatsOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedHiPrioOctets.setStatus("current")
_SapIngQosQueueStatsDroppedHiPrioOctets_Type = Counter64
_SapIngQosQueueStatsDroppedHiPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsDroppedHiPrioOctets = _SapIngQosQueueStatsDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 7),
    _SapIngQosQueueStatsDroppedHiPrioOctets_Type()
)
sapIngQosQueueStatsDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedHiPrioOctets.setStatus("current")
_SapIngQosQueueStatsOfferedLoPrioOctets_Type = Counter64
_SapIngQosQueueStatsOfferedLoPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsOfferedLoPrioOctets = _SapIngQosQueueStatsOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 8),
    _SapIngQosQueueStatsOfferedLoPrioOctets_Type()
)
sapIngQosQueueStatsOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsOfferedLoPrioOctets.setStatus("current")
_SapIngQosQueueStatsDroppedLoPrioOctets_Type = Counter64
_SapIngQosQueueStatsDroppedLoPrioOctets_Object = MibTableColumn
sapIngQosQueueStatsDroppedLoPrioOctets = _SapIngQosQueueStatsDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 9),
    _SapIngQosQueueStatsDroppedLoPrioOctets_Type()
)
sapIngQosQueueStatsDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsDroppedLoPrioOctets.setStatus("current")
_SapIngQosQueueStatsForwardedInProfPackets_Type = Counter64
_SapIngQosQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapIngQosQueueStatsForwardedInProfPackets = _SapIngQosQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 10),
    _SapIngQosQueueStatsForwardedInProfPackets_Type()
)
sapIngQosQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedInProfPackets.setStatus("current")
_SapIngQosQueueStatsForwardedOutProfPackets_Type = Counter64
_SapIngQosQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapIngQosQueueStatsForwardedOutProfPackets = _SapIngQosQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 11),
    _SapIngQosQueueStatsForwardedOutProfPackets_Type()
)
sapIngQosQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedOutProfPackets.setStatus("current")
_SapIngQosQueueStatsForwardedInProfOctets_Type = Counter64
_SapIngQosQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapIngQosQueueStatsForwardedInProfOctets = _SapIngQosQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 12),
    _SapIngQosQueueStatsForwardedInProfOctets_Type()
)
sapIngQosQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedInProfOctets.setStatus("current")
_SapIngQosQueueStatsForwardedOutProfOctets_Type = Counter64
_SapIngQosQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapIngQosQueueStatsForwardedOutProfOctets = _SapIngQosQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 13),
    _SapIngQosQueueStatsForwardedOutProfOctets_Type()
)
sapIngQosQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsForwardedOutProfOctets.setStatus("current")
_SapIngQosCustId_Type = TmnxCustId
_SapIngQosCustId_Object = MibTableColumn
sapIngQosCustId = _SapIngQosCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 14),
    _SapIngQosCustId_Type()
)
sapIngQosCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosCustId.setStatus("current")
_SapIngQosQueueStatsUncoloredPacketsOffered_Type = Counter64
_SapIngQosQueueStatsUncoloredPacketsOffered_Object = MibTableColumn
sapIngQosQueueStatsUncoloredPacketsOffered = _SapIngQosQueueStatsUncoloredPacketsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 15),
    _SapIngQosQueueStatsUncoloredPacketsOffered_Type()
)
sapIngQosQueueStatsUncoloredPacketsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsUncoloredPacketsOffered.setStatus("current")
_SapIngQosQueueStatsUncoloredOctetsOffered_Type = Counter64
_SapIngQosQueueStatsUncoloredOctetsOffered_Object = MibTableColumn
sapIngQosQueueStatsUncoloredOctetsOffered = _SapIngQosQueueStatsUncoloredOctetsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 7, 1, 16),
    _SapIngQosQueueStatsUncoloredOctetsOffered_Type()
)
sapIngQosQueueStatsUncoloredOctetsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQueueStatsUncoloredOctetsOffered.setStatus("current")
_SapEgrQosQueueStatsTable_Object = MibTable
sapEgrQosQueueStatsTable = _SapEgrQosQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8)
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsTable.setStatus("current")
_SapEgrQosQueueStatsEntry_Object = MibTableRow
sapEgrQosQueueStatsEntry = _SapEgrQosQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1)
)
sapEgrQosQueueStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueId"),
)
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsEntry.setStatus("current")
_SapEgrQosQueueId_Type = TSapEgrQueueId
_SapEgrQosQueueId_Object = MibTableColumn
sapEgrQosQueueId = _SapEgrQosQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 1),
    _SapEgrQosQueueId_Type()
)
sapEgrQosQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueId.setStatus("current")
_SapEgrQosQueueStatsForwardedInProfPackets_Type = Counter64
_SapEgrQosQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedInProfPackets = _SapEgrQosQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 2),
    _SapEgrQosQueueStatsForwardedInProfPackets_Type()
)
sapEgrQosQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedInProfPackets.setStatus("current")
_SapEgrQosQueueStatsDroppedInProfPackets_Type = Counter64
_SapEgrQosQueueStatsDroppedInProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedInProfPackets = _SapEgrQosQueueStatsDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 3),
    _SapEgrQosQueueStatsDroppedInProfPackets_Type()
)
sapEgrQosQueueStatsDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedInProfPackets.setStatus("current")
_SapEgrQosQueueStatsForwardedOutProfPackets_Type = Counter64
_SapEgrQosQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedOutProfPackets = _SapEgrQosQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 4),
    _SapEgrQosQueueStatsForwardedOutProfPackets_Type()
)
sapEgrQosQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedOutProfPackets.setStatus("current")
_SapEgrQosQueueStatsDroppedOutProfPackets_Type = Counter64
_SapEgrQosQueueStatsDroppedOutProfPackets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedOutProfPackets = _SapEgrQosQueueStatsDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 5),
    _SapEgrQosQueueStatsDroppedOutProfPackets_Type()
)
sapEgrQosQueueStatsDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedOutProfPackets.setStatus("current")
_SapEgrQosQueueStatsForwardedInProfOctets_Type = Counter64
_SapEgrQosQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedInProfOctets = _SapEgrQosQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 6),
    _SapEgrQosQueueStatsForwardedInProfOctets_Type()
)
sapEgrQosQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedInProfOctets.setStatus("current")
_SapEgrQosQueueStatsDroppedInProfOctets_Type = Counter64
_SapEgrQosQueueStatsDroppedInProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedInProfOctets = _SapEgrQosQueueStatsDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 7),
    _SapEgrQosQueueStatsDroppedInProfOctets_Type()
)
sapEgrQosQueueStatsDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedInProfOctets.setStatus("current")
_SapEgrQosQueueStatsForwardedOutProfOctets_Type = Counter64
_SapEgrQosQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsForwardedOutProfOctets = _SapEgrQosQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 8),
    _SapEgrQosQueueStatsForwardedOutProfOctets_Type()
)
sapEgrQosQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsForwardedOutProfOctets.setStatus("current")
_SapEgrQosQueueStatsDroppedOutProfOctets_Type = Counter64
_SapEgrQosQueueStatsDroppedOutProfOctets_Object = MibTableColumn
sapEgrQosQueueStatsDroppedOutProfOctets = _SapEgrQosQueueStatsDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 9),
    _SapEgrQosQueueStatsDroppedOutProfOctets_Type()
)
sapEgrQosQueueStatsDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQueueStatsDroppedOutProfOctets.setStatus("current")
_SapEgrQosCustId_Type = TmnxCustId
_SapEgrQosCustId_Object = MibTableColumn
sapEgrQosCustId = _SapEgrQosCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 8, 1, 10),
    _SapEgrQosCustId_Type()
)
sapEgrQosCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosCustId.setStatus("current")
_SapIngQosSchedStatsTable_Object = MibTable
sapIngQosSchedStatsTable = _SapIngQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9)
)
if mibBuilder.loadTexts:
    sapIngQosSchedStatsTable.setStatus("current")
_SapIngQosSchedStatsEntry_Object = MibTableRow
sapIngQosSchedStatsEntry = _SapIngQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9, 1)
)
sapIngQosSchedStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSchedName"),
)
if mibBuilder.loadTexts:
    sapIngQosSchedStatsEntry.setStatus("current")
_SapIngQosSchedName_Type = TNamedItem
_SapIngQosSchedName_Object = MibTableColumn
sapIngQosSchedName = _SapIngQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9, 1, 1),
    _SapIngQosSchedName_Type()
)
sapIngQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIngQosSchedName.setStatus("current")
_SapIngQosSchedStatsForwardedPackets_Type = Counter64
_SapIngQosSchedStatsForwardedPackets_Object = MibTableColumn
sapIngQosSchedStatsForwardedPackets = _SapIngQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9, 1, 2),
    _SapIngQosSchedStatsForwardedPackets_Type()
)
sapIngQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedStatsForwardedPackets.setStatus("current")
_SapIngQosSchedStatsForwardedOctets_Type = Counter64
_SapIngQosSchedStatsForwardedOctets_Object = MibTableColumn
sapIngQosSchedStatsForwardedOctets = _SapIngQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9, 1, 3),
    _SapIngQosSchedStatsForwardedOctets_Type()
)
sapIngQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedStatsForwardedOctets.setStatus("current")
_SapIngQosSchedCustId_Type = TmnxCustId
_SapIngQosSchedCustId_Object = MibTableColumn
sapIngQosSchedCustId = _SapIngQosSchedCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 9, 1, 4),
    _SapIngQosSchedCustId_Type()
)
sapIngQosSchedCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSchedCustId.setStatus("current")
_SapEgrQosSchedStatsTable_Object = MibTable
sapEgrQosSchedStatsTable = _SapEgrQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10)
)
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsTable.setStatus("current")
_SapEgrQosSchedStatsEntry_Object = MibTableRow
sapEgrQosSchedStatsEntry = _SapEgrQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10, 1)
)
sapEgrQosSchedStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSchedName"),
)
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsEntry.setStatus("current")
_SapEgrQosSchedName_Type = TNamedItem
_SapEgrQosSchedName_Object = MibTableColumn
sapEgrQosSchedName = _SapEgrQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10, 1, 1),
    _SapEgrQosSchedName_Type()
)
sapEgrQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgrQosSchedName.setStatus("current")
_SapEgrQosSchedStatsForwardedPackets_Type = Counter64
_SapEgrQosSchedStatsForwardedPackets_Object = MibTableColumn
sapEgrQosSchedStatsForwardedPackets = _SapEgrQosSchedStatsForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10, 1, 2),
    _SapEgrQosSchedStatsForwardedPackets_Type()
)
sapEgrQosSchedStatsForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsForwardedPackets.setStatus("current")
_SapEgrQosSchedStatsForwardedOctets_Type = Counter64
_SapEgrQosSchedStatsForwardedOctets_Object = MibTableColumn
sapEgrQosSchedStatsForwardedOctets = _SapEgrQosSchedStatsForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10, 1, 3),
    _SapEgrQosSchedStatsForwardedOctets_Type()
)
sapEgrQosSchedStatsForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedStatsForwardedOctets.setStatus("current")
_SapEgrQosSchedCustId_Type = TmnxCustId
_SapEgrQosSchedCustId_Object = MibTableColumn
sapEgrQosSchedCustId = _SapEgrQosSchedCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 10, 1, 4),
    _SapEgrQosSchedCustId_Type()
)
sapEgrQosSchedCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSchedCustId.setStatus("current")
_SapTlsManagedVlanListTable_Object = MibTable
sapTlsManagedVlanListTable = _SapTlsManagedVlanListTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 11)
)
if mibBuilder.loadTexts:
    sapTlsManagedVlanListTable.setStatus("current")
_SapTlsManagedVlanListEntry_Object = MibTableRow
sapTlsManagedVlanListEntry = _SapTlsManagedVlanListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 11, 1)
)
sapTlsManagedVlanListEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMinVlanTag"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMaxVlanTag"),
)
if mibBuilder.loadTexts:
    sapTlsManagedVlanListEntry.setStatus("current")


class _SapTlsMvplsMinVlanTag_Type(Unsigned32):
    """Custom type sapTlsMvplsMinVlanTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SapTlsMvplsMinVlanTag_Type.__name__ = "Unsigned32"
_SapTlsMvplsMinVlanTag_Object = MibTableColumn
sapTlsMvplsMinVlanTag = _SapTlsMvplsMinVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 11, 1, 1),
    _SapTlsMvplsMinVlanTag_Type()
)
sapTlsMvplsMinVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapTlsMvplsMinVlanTag.setStatus("current")


class _SapTlsMvplsMaxVlanTag_Type(Unsigned32):
    """Custom type sapTlsMvplsMaxVlanTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SapTlsMvplsMaxVlanTag_Type.__name__ = "Unsigned32"
_SapTlsMvplsMaxVlanTag_Object = MibTableColumn
sapTlsMvplsMaxVlanTag = _SapTlsMvplsMaxVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 11, 1, 2),
    _SapTlsMvplsMaxVlanTag_Type()
)
sapTlsMvplsMaxVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapTlsMvplsMaxVlanTag.setStatus("current")
_SapTlsMvplsRowStatus_Type = RowStatus
_SapTlsMvplsRowStatus_Object = MibTableColumn
sapTlsMvplsRowStatus = _SapTlsMvplsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 11, 1, 3),
    _SapTlsMvplsRowStatus_Type()
)
sapTlsMvplsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapTlsMvplsRowStatus.setStatus("current")
_SapAntiSpoofTable_Object = MibTable
sapAntiSpoofTable = _SapAntiSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 12)
)
if mibBuilder.loadTexts:
    sapAntiSpoofTable.setStatus("current")
_SapAntiSpoofEntry_Object = MibTableRow
sapAntiSpoofEntry = _SapAntiSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 12, 1)
)
sapAntiSpoofEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAntiSpoofIpAddress"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAntiSpoofMacAddress"),
)
if mibBuilder.loadTexts:
    sapAntiSpoofEntry.setStatus("current")
_SapAntiSpoofIpAddress_Type = IpAddress
_SapAntiSpoofIpAddress_Object = MibTableColumn
sapAntiSpoofIpAddress = _SapAntiSpoofIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 12, 1, 1),
    _SapAntiSpoofIpAddress_Type()
)
sapAntiSpoofIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapAntiSpoofIpAddress.setStatus("current")
_SapAntiSpoofMacAddress_Type = MacAddress
_SapAntiSpoofMacAddress_Object = MibTableColumn
sapAntiSpoofMacAddress = _SapAntiSpoofMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 12, 1, 2),
    _SapAntiSpoofMacAddress_Type()
)
sapAntiSpoofMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapAntiSpoofMacAddress.setStatus("current")
_SapStaticHostTable_Object = MibTable
sapStaticHostTable = _SapStaticHostTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13)
)
if mibBuilder.loadTexts:
    sapStaticHostTable.setStatus("current")
_SapStaticHostEntry_Object = MibTableRow
sapStaticHostEntry = _SapStaticHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1)
)
sapStaticHostEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostIpAddress"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostMacAddress"),
)
if mibBuilder.loadTexts:
    sapStaticHostEntry.setStatus("current")
_SapStaticHostRowStatus_Type = RowStatus
_SapStaticHostRowStatus_Object = MibTableColumn
sapStaticHostRowStatus = _SapStaticHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 1),
    _SapStaticHostRowStatus_Type()
)
sapStaticHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostRowStatus.setStatus("current")
_SapStaticHostIpAddress_Type = IpAddress
_SapStaticHostIpAddress_Object = MibTableColumn
sapStaticHostIpAddress = _SapStaticHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 2),
    _SapStaticHostIpAddress_Type()
)
sapStaticHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapStaticHostIpAddress.setStatus("current")
_SapStaticHostMacAddress_Type = MacAddress
_SapStaticHostMacAddress_Object = MibTableColumn
sapStaticHostMacAddress = _SapStaticHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 3),
    _SapStaticHostMacAddress_Type()
)
sapStaticHostMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapStaticHostMacAddress.setStatus("current")


class _SapStaticHostSubscrIdent_Type(DisplayString):
    """Custom type sapStaticHostSubscrIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapStaticHostSubscrIdent_Type.__name__ = "DisplayString"
_SapStaticHostSubscrIdent_Object = MibTableColumn
sapStaticHostSubscrIdent = _SapStaticHostSubscrIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 4),
    _SapStaticHostSubscrIdent_Type()
)
sapStaticHostSubscrIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostSubscrIdent.setStatus("current")
_SapStaticHostSubProfile_Type = ServObjName
_SapStaticHostSubProfile_Object = MibTableColumn
sapStaticHostSubProfile = _SapStaticHostSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 5),
    _SapStaticHostSubProfile_Type()
)
sapStaticHostSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostSubProfile.setStatus("current")
_SapStaticHostSlaProfile_Type = ServObjName
_SapStaticHostSlaProfile_Object = MibTableColumn
sapStaticHostSlaProfile = _SapStaticHostSlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 6),
    _SapStaticHostSlaProfile_Type()
)
sapStaticHostSlaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostSlaProfile.setStatus("current")


class _SapStaticHostShcvOperState_Type(Integer32):
    """Custom type sapStaticHostShcvOperState based on Integer32"""
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
        *(("disabled", 1),
          ("down", 3),
          ("undefined", 2),
          ("up", 4))
    )


_SapStaticHostShcvOperState_Type.__name__ = "Integer32"
_SapStaticHostShcvOperState_Object = MibTableColumn
sapStaticHostShcvOperState = _SapStaticHostShcvOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 7),
    _SapStaticHostShcvOperState_Type()
)
sapStaticHostShcvOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostShcvOperState.setStatus("current")
_SapStaticHostShcvChecks_Type = Unsigned32
_SapStaticHostShcvChecks_Object = MibTableColumn
sapStaticHostShcvChecks = _SapStaticHostShcvChecks_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 8),
    _SapStaticHostShcvChecks_Type()
)
sapStaticHostShcvChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostShcvChecks.setStatus("current")
_SapStaticHostShcvReplies_Type = Unsigned32
_SapStaticHostShcvReplies_Object = MibTableColumn
sapStaticHostShcvReplies = _SapStaticHostShcvReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 9),
    _SapStaticHostShcvReplies_Type()
)
sapStaticHostShcvReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostShcvReplies.setStatus("current")
_SapStaticHostShcvReplyTime_Type = TimeStamp
_SapStaticHostShcvReplyTime_Object = MibTableColumn
sapStaticHostShcvReplyTime = _SapStaticHostShcvReplyTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 10),
    _SapStaticHostShcvReplyTime_Type()
)
sapStaticHostShcvReplyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostShcvReplyTime.setStatus("current")
_SapStaticHostDynMacAddress_Type = MacAddress
_SapStaticHostDynMacAddress_Object = MibTableColumn
sapStaticHostDynMacAddress = _SapStaticHostDynMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 11),
    _SapStaticHostDynMacAddress_Type()
)
sapStaticHostDynMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostDynMacAddress.setStatus("current")
_SapStaticHostRetailerSvcId_Type = TmnxServId
_SapStaticHostRetailerSvcId_Object = MibTableColumn
sapStaticHostRetailerSvcId = _SapStaticHostRetailerSvcId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 12),
    _SapStaticHostRetailerSvcId_Type()
)
sapStaticHostRetailerSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostRetailerSvcId.setStatus("current")
_SapStaticHostRetailerIf_Type = InterfaceIndexOrZero
_SapStaticHostRetailerIf_Object = MibTableColumn
sapStaticHostRetailerIf = _SapStaticHostRetailerIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 13),
    _SapStaticHostRetailerIf_Type()
)
sapStaticHostRetailerIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostRetailerIf.setStatus("current")
_SapStaticHostFwdingState_Type = TmnxOperState
_SapStaticHostFwdingState_Object = MibTableColumn
sapStaticHostFwdingState = _SapStaticHostFwdingState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 14),
    _SapStaticHostFwdingState_Type()
)
sapStaticHostFwdingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapStaticHostFwdingState.setStatus("current")


class _SapStaticHostAncpString_Type(DisplayString):
    """Custom type sapStaticHostAncpString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SapStaticHostAncpString_Type.__name__ = "DisplayString"
_SapStaticHostAncpString_Object = MibTableColumn
sapStaticHostAncpString = _SapStaticHostAncpString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 15),
    _SapStaticHostAncpString_Type()
)
sapStaticHostAncpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostAncpString.setStatus("current")


class _SapStaticHostSubIdIsSapId_Type(TruthValue):
    """Custom type sapStaticHostSubIdIsSapId based on TruthValue"""


_SapStaticHostSubIdIsSapId_Object = MibTableColumn
sapStaticHostSubIdIsSapId = _SapStaticHostSubIdIsSapId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 16),
    _SapStaticHostSubIdIsSapId_Type()
)
sapStaticHostSubIdIsSapId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostSubIdIsSapId.setStatus("current")
_SapStaticHostAppProfile_Type = ServObjName
_SapStaticHostAppProfile_Object = MibTableColumn
sapStaticHostAppProfile = _SapStaticHostAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 17),
    _SapStaticHostAppProfile_Type()
)
sapStaticHostAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostAppProfile.setStatus("current")


class _SapStaticHostIntermediateDestId_Type(DisplayString):
    """Custom type sapStaticHostIntermediateDestId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapStaticHostIntermediateDestId_Type.__name__ = "DisplayString"
_SapStaticHostIntermediateDestId_Object = MibTableColumn
sapStaticHostIntermediateDestId = _SapStaticHostIntermediateDestId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 13, 1, 18),
    _SapStaticHostIntermediateDestId_Type()
)
sapStaticHostIntermediateDestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapStaticHostIntermediateDestId.setStatus("current")
_SapTlsDhcpInfoTable_Object = MibTable
sapTlsDhcpInfoTable = _SapTlsDhcpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14)
)
if mibBuilder.loadTexts:
    sapTlsDhcpInfoTable.setStatus("current")
_SapTlsDhcpInfoEntry_Object = MibTableRow
sapTlsDhcpInfoEntry = _SapTlsDhcpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1)
)
sapTlsDhcpInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapTlsDhcpInfoEntry.setStatus("current")


class _SapTlsDhcpAdminState_Type(TmnxEnabledDisabled):
    """Custom type sapTlsDhcpAdminState based on TmnxEnabledDisabled"""


_SapTlsDhcpAdminState_Object = MibTableColumn
sapTlsDhcpAdminState = _SapTlsDhcpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 1),
    _SapTlsDhcpAdminState_Type()
)
sapTlsDhcpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpAdminState.setStatus("current")


class _SapTlsDhcpDescription_Type(ServObjDesc):
    """Custom type sapTlsDhcpDescription based on ServObjDesc"""
    defaultHexValue = ""


_SapTlsDhcpDescription_Object = MibTableColumn
sapTlsDhcpDescription = _SapTlsDhcpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 2),
    _SapTlsDhcpDescription_Type()
)
sapTlsDhcpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpDescription.setStatus("current")


class _SapTlsDhcpSnoop_Type(TmnxEnabledDisabled):
    """Custom type sapTlsDhcpSnoop based on TmnxEnabledDisabled"""


_SapTlsDhcpSnoop_Object = MibTableColumn
sapTlsDhcpSnoop = _SapTlsDhcpSnoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 3),
    _SapTlsDhcpSnoop_Type()
)
sapTlsDhcpSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpSnoop.setStatus("current")


class _SapTlsDhcpLeasePopulate_Type(Unsigned32):
    """Custom type sapTlsDhcpLeasePopulate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SapTlsDhcpLeasePopulate_Type.__name__ = "Unsigned32"
_SapTlsDhcpLeasePopulate_Object = MibTableColumn
sapTlsDhcpLeasePopulate = _SapTlsDhcpLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 4),
    _SapTlsDhcpLeasePopulate_Type()
)
sapTlsDhcpLeasePopulate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpLeasePopulate.setStatus("current")


class _SapTlsDhcpOperLeasePopulate_Type(Unsigned32):
    """Custom type sapTlsDhcpOperLeasePopulate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SapTlsDhcpOperLeasePopulate_Type.__name__ = "Unsigned32"
_SapTlsDhcpOperLeasePopulate_Object = MibTableColumn
sapTlsDhcpOperLeasePopulate = _SapTlsDhcpOperLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 5),
    _SapTlsDhcpOperLeasePopulate_Type()
)
sapTlsDhcpOperLeasePopulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpOperLeasePopulate.setStatus("current")


class _SapTlsDhcpInfoAction_Type(Integer32):
    """Custom type sapTlsDhcpInfoAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_SapTlsDhcpInfoAction_Type.__name__ = "Integer32"
_SapTlsDhcpInfoAction_Object = MibTableColumn
sapTlsDhcpInfoAction = _SapTlsDhcpInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 6),
    _SapTlsDhcpInfoAction_Type()
)
sapTlsDhcpInfoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpInfoAction.setStatus("current")


class _SapTlsDhcpCircuitId_Type(Integer32):
    """Custom type sapTlsDhcpCircuitId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asciiTuple", 1),
          ("none", 0),
          ("vlanAsciiTuple", 2))
    )


_SapTlsDhcpCircuitId_Type.__name__ = "Integer32"
_SapTlsDhcpCircuitId_Object = MibTableColumn
sapTlsDhcpCircuitId = _SapTlsDhcpCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 7),
    _SapTlsDhcpCircuitId_Type()
)
sapTlsDhcpCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpCircuitId.setStatus("current")


class _SapTlsDhcpRemoteId_Type(Integer32):
    """Custom type sapTlsDhcpRemoteId based on Integer32"""
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
        *(("mac", 2),
          ("none", 1),
          ("remote-id", 3))
    )


_SapTlsDhcpRemoteId_Type.__name__ = "Integer32"
_SapTlsDhcpRemoteId_Object = MibTableColumn
sapTlsDhcpRemoteId = _SapTlsDhcpRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 8),
    _SapTlsDhcpRemoteId_Type()
)
sapTlsDhcpRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpRemoteId.setStatus("current")


class _SapTlsDhcpRemoteIdString_Type(DisplayString):
    """Custom type sapTlsDhcpRemoteIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapTlsDhcpRemoteIdString_Type.__name__ = "DisplayString"
_SapTlsDhcpRemoteIdString_Object = MibTableColumn
sapTlsDhcpRemoteIdString = _SapTlsDhcpRemoteIdString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 9),
    _SapTlsDhcpRemoteIdString_Type()
)
sapTlsDhcpRemoteIdString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpRemoteIdString.setStatus("current")


class _SapTlsDhcpProxyAdminState_Type(TmnxEnabledDisabled):
    """Custom type sapTlsDhcpProxyAdminState based on TmnxEnabledDisabled"""


_SapTlsDhcpProxyAdminState_Object = MibTableColumn
sapTlsDhcpProxyAdminState = _SapTlsDhcpProxyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 10),
    _SapTlsDhcpProxyAdminState_Type()
)
sapTlsDhcpProxyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpProxyAdminState.setStatus("current")


class _SapTlsDhcpProxyServerAddr_Type(IpAddress):
    """Custom type sapTlsDhcpProxyServerAddr based on IpAddress"""
    defaultHexValue = "00000000"


_SapTlsDhcpProxyServerAddr_Object = MibTableColumn
sapTlsDhcpProxyServerAddr = _SapTlsDhcpProxyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 11),
    _SapTlsDhcpProxyServerAddr_Type()
)
sapTlsDhcpProxyServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpProxyServerAddr.setStatus("current")


class _SapTlsDhcpProxyLeaseTime_Type(Unsigned32):
    """Custom type sapTlsDhcpProxyLeaseTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
    )


_SapTlsDhcpProxyLeaseTime_Type.__name__ = "Unsigned32"
_SapTlsDhcpProxyLeaseTime_Object = MibTableColumn
sapTlsDhcpProxyLeaseTime = _SapTlsDhcpProxyLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 12),
    _SapTlsDhcpProxyLeaseTime_Type()
)
sapTlsDhcpProxyLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpProxyLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    sapTlsDhcpProxyLeaseTime.setUnits("seconds")


class _SapTlsDhcpProxyLTRadiusOverride_Type(TruthValue):
    """Custom type sapTlsDhcpProxyLTRadiusOverride based on TruthValue"""


_SapTlsDhcpProxyLTRadiusOverride_Object = MibTableColumn
sapTlsDhcpProxyLTRadiusOverride = _SapTlsDhcpProxyLTRadiusOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 13),
    _SapTlsDhcpProxyLTRadiusOverride_Type()
)
sapTlsDhcpProxyLTRadiusOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpProxyLTRadiusOverride.setStatus("current")


class _SapTlsDhcpVendorIncludeOptions_Type(Bits):
    """Custom type sapTlsDhcpVendorIncludeOptions based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("clientMac", 1),
          ("sapId", 3),
          ("serviceId", 2),
          ("systemId", 0))
    )

_SapTlsDhcpVendorIncludeOptions_Type.__name__ = "Bits"
_SapTlsDhcpVendorIncludeOptions_Object = MibTableColumn
sapTlsDhcpVendorIncludeOptions = _SapTlsDhcpVendorIncludeOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 14),
    _SapTlsDhcpVendorIncludeOptions_Type()
)
sapTlsDhcpVendorIncludeOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpVendorIncludeOptions.setStatus("current")


class _SapTlsDhcpVendorOptionString_Type(DisplayString):
    """Custom type sapTlsDhcpVendorOptionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapTlsDhcpVendorOptionString_Type.__name__ = "DisplayString"
_SapTlsDhcpVendorOptionString_Object = MibTableColumn
sapTlsDhcpVendorOptionString = _SapTlsDhcpVendorOptionString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 14, 1, 15),
    _SapTlsDhcpVendorOptionString_Type()
)
sapTlsDhcpVendorOptionString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsDhcpVendorOptionString.setStatus("current")
_SapTlsDhcpStatsTable_Object = MibTable
sapTlsDhcpStatsTable = _SapTlsDhcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15)
)
if mibBuilder.loadTexts:
    sapTlsDhcpStatsTable.setStatus("current")
_SapTlsDhcpStatsEntry_Object = MibTableRow
sapTlsDhcpStatsEntry = _SapTlsDhcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1)
)
sapTlsDhcpStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapTlsDhcpStatsEntry.setStatus("current")
_SapTlsDhcpStatsClntSnoopdPckts_Type = Counter32
_SapTlsDhcpStatsClntSnoopdPckts_Object = MibTableColumn
sapTlsDhcpStatsClntSnoopdPckts = _SapTlsDhcpStatsClntSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 1),
    _SapTlsDhcpStatsClntSnoopdPckts_Type()
)
sapTlsDhcpStatsClntSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsClntSnoopdPckts.setStatus("current")
_SapTlsDhcpStatsSrvrSnoopdPckts_Type = Counter32
_SapTlsDhcpStatsSrvrSnoopdPckts_Object = MibTableColumn
sapTlsDhcpStatsSrvrSnoopdPckts = _SapTlsDhcpStatsSrvrSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 2),
    _SapTlsDhcpStatsSrvrSnoopdPckts_Type()
)
sapTlsDhcpStatsSrvrSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsSrvrSnoopdPckts.setStatus("current")
_SapTlsDhcpStatsClntForwdPckts_Type = Counter32
_SapTlsDhcpStatsClntForwdPckts_Object = MibTableColumn
sapTlsDhcpStatsClntForwdPckts = _SapTlsDhcpStatsClntForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 3),
    _SapTlsDhcpStatsClntForwdPckts_Type()
)
sapTlsDhcpStatsClntForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsClntForwdPckts.setStatus("current")
_SapTlsDhcpStatsSrvrForwdPckts_Type = Counter32
_SapTlsDhcpStatsSrvrForwdPckts_Object = MibTableColumn
sapTlsDhcpStatsSrvrForwdPckts = _SapTlsDhcpStatsSrvrForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 4),
    _SapTlsDhcpStatsSrvrForwdPckts_Type()
)
sapTlsDhcpStatsSrvrForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsSrvrForwdPckts.setStatus("current")
_SapTlsDhcpStatsClntDropdPckts_Type = Counter32
_SapTlsDhcpStatsClntDropdPckts_Object = MibTableColumn
sapTlsDhcpStatsClntDropdPckts = _SapTlsDhcpStatsClntDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 5),
    _SapTlsDhcpStatsClntDropdPckts_Type()
)
sapTlsDhcpStatsClntDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsClntDropdPckts.setStatus("current")
_SapTlsDhcpStatsSrvrDropdPckts_Type = Counter32
_SapTlsDhcpStatsSrvrDropdPckts_Object = MibTableColumn
sapTlsDhcpStatsSrvrDropdPckts = _SapTlsDhcpStatsSrvrDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 6),
    _SapTlsDhcpStatsSrvrDropdPckts_Type()
)
sapTlsDhcpStatsSrvrDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsSrvrDropdPckts.setStatus("current")
_SapTlsDhcpStatsClntProxRadPckts_Type = Counter32
_SapTlsDhcpStatsClntProxRadPckts_Object = MibTableColumn
sapTlsDhcpStatsClntProxRadPckts = _SapTlsDhcpStatsClntProxRadPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 7),
    _SapTlsDhcpStatsClntProxRadPckts_Type()
)
sapTlsDhcpStatsClntProxRadPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsClntProxRadPckts.setStatus("current")
_SapTlsDhcpStatsClntProxLSPckts_Type = Counter32
_SapTlsDhcpStatsClntProxLSPckts_Object = MibTableColumn
sapTlsDhcpStatsClntProxLSPckts = _SapTlsDhcpStatsClntProxLSPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 8),
    _SapTlsDhcpStatsClntProxLSPckts_Type()
)
sapTlsDhcpStatsClntProxLSPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsClntProxLSPckts.setStatus("current")
_SapTlsDhcpStatsGenReleasePckts_Type = Counter32
_SapTlsDhcpStatsGenReleasePckts_Object = MibTableColumn
sapTlsDhcpStatsGenReleasePckts = _SapTlsDhcpStatsGenReleasePckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 9),
    _SapTlsDhcpStatsGenReleasePckts_Type()
)
sapTlsDhcpStatsGenReleasePckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsGenReleasePckts.setStatus("current")
_SapTlsDhcpStatsGenForceRenPckts_Type = Counter32
_SapTlsDhcpStatsGenForceRenPckts_Object = MibTableColumn
sapTlsDhcpStatsGenForceRenPckts = _SapTlsDhcpStatsGenForceRenPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 15, 1, 10),
    _SapTlsDhcpStatsGenForceRenPckts_Type()
)
sapTlsDhcpStatsGenForceRenPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpStatsGenForceRenPckts.setStatus("current")
_SapTlsDhcpLeaseStateTable_Object = MibTable
sapTlsDhcpLeaseStateTable = _SapTlsDhcpLeaseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16)
)
if mibBuilder.loadTexts:
    sapTlsDhcpLeaseStateTable.setStatus("obsolete")
_SapTlsDhcpLeaseStateEntry_Object = MibTableRow
sapTlsDhcpLeaseStateEntry = _SapTlsDhcpLeaseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1)
)
sapTlsDhcpLeaseStateEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLseStateCiAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLseStateChAddr"),
)
if mibBuilder.loadTexts:
    sapTlsDhcpLeaseStateEntry.setStatus("obsolete")
_SapTlsDhcpLseStateCiAddr_Type = IpAddress
_SapTlsDhcpLseStateCiAddr_Object = MibTableColumn
sapTlsDhcpLseStateCiAddr = _SapTlsDhcpLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1, 1),
    _SapTlsDhcpLseStateCiAddr_Type()
)
sapTlsDhcpLseStateCiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapTlsDhcpLseStateCiAddr.setStatus("obsolete")
_SapTlsDhcpLseStateChAddr_Type = MacAddress
_SapTlsDhcpLseStateChAddr_Object = MibTableColumn
sapTlsDhcpLseStateChAddr = _SapTlsDhcpLseStateChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1, 2),
    _SapTlsDhcpLseStateChAddr_Type()
)
sapTlsDhcpLseStateChAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapTlsDhcpLseStateChAddr.setStatus("obsolete")
_SapTlsDhcpLseStateRemainLseTime_Type = Unsigned32
_SapTlsDhcpLseStateRemainLseTime_Object = MibTableColumn
sapTlsDhcpLseStateRemainLseTime = _SapTlsDhcpLseStateRemainLseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1, 3),
    _SapTlsDhcpLseStateRemainLseTime_Type()
)
sapTlsDhcpLseStateRemainLseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpLseStateRemainLseTime.setStatus("obsolete")
_SapTlsDhcpLseStateOption82_Type = OctetString
_SapTlsDhcpLseStateOption82_Object = MibTableColumn
sapTlsDhcpLseStateOption82 = _SapTlsDhcpLseStateOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1, 4),
    _SapTlsDhcpLseStateOption82_Type()
)
sapTlsDhcpLseStateOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpLseStateOption82.setStatus("obsolete")
_SapTlsDhcpLseStatePersistKey_Type = Unsigned32
_SapTlsDhcpLseStatePersistKey_Object = MibTableColumn
sapTlsDhcpLseStatePersistKey = _SapTlsDhcpLseStatePersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 16, 1, 5),
    _SapTlsDhcpLseStatePersistKey_Type()
)
sapTlsDhcpLseStatePersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsDhcpLseStatePersistKey.setStatus("obsolete")
_SapPortIdIngQosSchedStatsTable_Object = MibTable
sapPortIdIngQosSchedStatsTable = _SapPortIdIngQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17)
)
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedStatsTable.setStatus("current")
_SapPortIdIngQosSchedStatsEntry_Object = MibTableRow
sapPortIdIngQosSchedStatsEntry = _SapPortIdIngQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1)
)
sapPortIdIngQosSchedStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngQosSchedName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngPortId"),
)
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedStatsEntry.setStatus("current")
_SapPortIdIngQosSchedName_Type = TNamedItem
_SapPortIdIngQosSchedName_Object = MibTableColumn
sapPortIdIngQosSchedName = _SapPortIdIngQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1, 1),
    _SapPortIdIngQosSchedName_Type()
)
sapPortIdIngQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedName.setStatus("current")
_SapPortIdIngPortId_Type = TmnxPortID
_SapPortIdIngPortId_Object = MibTableColumn
sapPortIdIngPortId = _SapPortIdIngPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1, 2),
    _SapPortIdIngPortId_Type()
)
sapPortIdIngPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapPortIdIngPortId.setStatus("current")
_SapPortIdIngQosSchedFwdPkts_Type = Counter64
_SapPortIdIngQosSchedFwdPkts_Object = MibTableColumn
sapPortIdIngQosSchedFwdPkts = _SapPortIdIngQosSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1, 3),
    _SapPortIdIngQosSchedFwdPkts_Type()
)
sapPortIdIngQosSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedFwdPkts.setStatus("current")
_SapPortIdIngQosSchedFwdOctets_Type = Counter64
_SapPortIdIngQosSchedFwdOctets_Object = MibTableColumn
sapPortIdIngQosSchedFwdOctets = _SapPortIdIngQosSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1, 4),
    _SapPortIdIngQosSchedFwdOctets_Type()
)
sapPortIdIngQosSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedFwdOctets.setStatus("current")
_SapPortIdIngQosSchedCustId_Type = TmnxCustId
_SapPortIdIngQosSchedCustId_Object = MibTableColumn
sapPortIdIngQosSchedCustId = _SapPortIdIngQosSchedCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 17, 1, 5),
    _SapPortIdIngQosSchedCustId_Type()
)
sapPortIdIngQosSchedCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdIngQosSchedCustId.setStatus("current")
_SapPortIdEgrQosSchedStatsTable_Object = MibTable
sapPortIdEgrQosSchedStatsTable = _SapPortIdEgrQosSchedStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18)
)
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedStatsTable.setStatus("current")
_SapPortIdEgrQosSchedStatsEntry_Object = MibTableRow
sapPortIdEgrQosSchedStatsEntry = _SapPortIdEgrQosSchedStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1)
)
sapPortIdEgrQosSchedStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrQosSchedName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrPortId"),
)
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedStatsEntry.setStatus("current")
_SapPortIdEgrQosSchedName_Type = TNamedItem
_SapPortIdEgrQosSchedName_Object = MibTableColumn
sapPortIdEgrQosSchedName = _SapPortIdEgrQosSchedName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1, 1),
    _SapPortIdEgrQosSchedName_Type()
)
sapPortIdEgrQosSchedName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedName.setStatus("current")
_SapPortIdEgrPortId_Type = TmnxPortID
_SapPortIdEgrPortId_Object = MibTableColumn
sapPortIdEgrPortId = _SapPortIdEgrPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1, 2),
    _SapPortIdEgrPortId_Type()
)
sapPortIdEgrPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapPortIdEgrPortId.setStatus("current")
_SapPortIdEgrQosSchedFwdPkts_Type = Counter64
_SapPortIdEgrQosSchedFwdPkts_Object = MibTableColumn
sapPortIdEgrQosSchedFwdPkts = _SapPortIdEgrQosSchedFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1, 3),
    _SapPortIdEgrQosSchedFwdPkts_Type()
)
sapPortIdEgrQosSchedFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedFwdPkts.setStatus("current")
_SapPortIdEgrQosSchedFwdOctets_Type = Counter64
_SapPortIdEgrQosSchedFwdOctets_Object = MibTableColumn
sapPortIdEgrQosSchedFwdOctets = _SapPortIdEgrQosSchedFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1, 4),
    _SapPortIdEgrQosSchedFwdOctets_Type()
)
sapPortIdEgrQosSchedFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedFwdOctets.setStatus("current")
_SapPortIdEgrQosSchedCustId_Type = TmnxCustId
_SapPortIdEgrQosSchedCustId_Object = MibTableColumn
sapPortIdEgrQosSchedCustId = _SapPortIdEgrQosSchedCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 18, 1, 5),
    _SapPortIdEgrQosSchedCustId_Type()
)
sapPortIdEgrQosSchedCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapPortIdEgrQosSchedCustId.setStatus("current")
_SapIngQosQueueInfoTable_Object = MibTable
sapIngQosQueueInfoTable = _SapIngQosQueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19)
)
if mibBuilder.loadTexts:
    sapIngQosQueueInfoTable.setStatus("current")
_SapIngQosQueueInfoEntry_Object = MibTableRow
sapIngQosQueueInfoEntry = _SapIngQosQueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1)
)
sapIngQosQueueInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQId"),
)
if mibBuilder.loadTexts:
    sapIngQosQueueInfoEntry.setStatus("current")
_SapIngQosQId_Type = TIngressQueueId
_SapIngQosQId_Object = MibTableColumn
sapIngQosQId = _SapIngQosQId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 1),
    _SapIngQosQId_Type()
)
sapIngQosQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIngQosQId.setStatus("current")
_SapIngQosQRowStatus_Type = RowStatus
_SapIngQosQRowStatus_Object = MibTableColumn
sapIngQosQRowStatus = _SapIngQosQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 2),
    _SapIngQosQRowStatus_Type()
)
sapIngQosQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQRowStatus.setStatus("current")
_SapIngQosQLastMgmtChange_Type = TimeStamp
_SapIngQosQLastMgmtChange_Object = MibTableColumn
sapIngQosQLastMgmtChange = _SapIngQosQLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 3),
    _SapIngQosQLastMgmtChange_Type()
)
sapIngQosQLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosQLastMgmtChange.setStatus("current")
_SapIngQosQOverrideFlags_Type = TQosQueueAttribute
_SapIngQosQOverrideFlags_Object = MibTableColumn
sapIngQosQOverrideFlags = _SapIngQosQOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 4),
    _SapIngQosQOverrideFlags_Type()
)
sapIngQosQOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQOverrideFlags.setStatus("current")


class _SapIngQosQCBS_Type(TBurstSize):
    """Custom type sapIngQosQCBS based on TBurstSize"""
    defaultValue = -1


_SapIngQosQCBS_Object = MibTableColumn
sapIngQosQCBS = _SapIngQosQCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 5),
    _SapIngQosQCBS_Type()
)
sapIngQosQCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQCBS.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosQCBS.setUnits("kilo bytes")


class _SapIngQosQMBS_Type(TBurstSize):
    """Custom type sapIngQosQMBS based on TBurstSize"""
    defaultValue = -1


_SapIngQosQMBS_Object = MibTableColumn
sapIngQosQMBS = _SapIngQosQMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 6),
    _SapIngQosQMBS_Type()
)
sapIngQosQMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQMBS.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosQMBS.setUnits("kilo bytes")


class _SapIngQosQHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type sapIngQosQHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_SapIngQosQHiPrioOnly_Object = MibTableColumn
sapIngQosQHiPrioOnly = _SapIngQosQHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 7),
    _SapIngQosQHiPrioOnly_Type()
)
sapIngQosQHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosQHiPrioOnly.setUnits("percent")


class _SapIngQosQCIRAdaptation_Type(TAdaptationRule):
    """Custom type sapIngQosQCIRAdaptation based on TAdaptationRule"""


_SapIngQosQCIRAdaptation_Object = MibTableColumn
sapIngQosQCIRAdaptation = _SapIngQosQCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 8),
    _SapIngQosQCIRAdaptation_Type()
)
sapIngQosQCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQCIRAdaptation.setStatus("current")


class _SapIngQosQPIRAdaptation_Type(TAdaptationRule):
    """Custom type sapIngQosQPIRAdaptation based on TAdaptationRule"""


_SapIngQosQPIRAdaptation_Object = MibTableColumn
sapIngQosQPIRAdaptation = _SapIngQosQPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 9),
    _SapIngQosQPIRAdaptation_Type()
)
sapIngQosQPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQPIRAdaptation.setStatus("current")


class _SapIngQosQAdminPIR_Type(TPIRRate):
    """Custom type sapIngQosQAdminPIR based on TPIRRate"""
    defaultValue = -1


_SapIngQosQAdminPIR_Object = MibTableColumn
sapIngQosQAdminPIR = _SapIngQosQAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 10),
    _SapIngQosQAdminPIR_Type()
)
sapIngQosQAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosQAdminPIR.setUnits("kilo bits per second")


class _SapIngQosQAdminCIR_Type(TCIRRate):
    """Custom type sapIngQosQAdminCIR based on TCIRRate"""
    defaultValue = -1


_SapIngQosQAdminCIR_Object = MibTableColumn
sapIngQosQAdminCIR = _SapIngQosQAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 19, 1, 11),
    _SapIngQosQAdminCIR_Type()
)
sapIngQosQAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosQAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosQAdminCIR.setUnits("kilo bits per second")
_SapEgrQosQueueInfoTable_Object = MibTable
sapEgrQosQueueInfoTable = _SapEgrQosQueueInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20)
)
if mibBuilder.loadTexts:
    sapEgrQosQueueInfoTable.setStatus("current")
_SapEgrQosQueueInfoEntry_Object = MibTableRow
sapEgrQosQueueInfoEntry = _SapEgrQosQueueInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1)
)
sapEgrQosQueueInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQId"),
)
if mibBuilder.loadTexts:
    sapEgrQosQueueInfoEntry.setStatus("current")
_SapEgrQosQId_Type = TEgressQueueId
_SapEgrQosQId_Object = MibTableColumn
sapEgrQosQId = _SapEgrQosQId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 1),
    _SapEgrQosQId_Type()
)
sapEgrQosQId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgrQosQId.setStatus("current")
_SapEgrQosQRowStatus_Type = RowStatus
_SapEgrQosQRowStatus_Object = MibTableColumn
sapEgrQosQRowStatus = _SapEgrQosQRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 2),
    _SapEgrQosQRowStatus_Type()
)
sapEgrQosQRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQRowStatus.setStatus("current")
_SapEgrQosQLastMgmtChange_Type = TimeStamp
_SapEgrQosQLastMgmtChange_Object = MibTableColumn
sapEgrQosQLastMgmtChange = _SapEgrQosQLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 3),
    _SapEgrQosQLastMgmtChange_Type()
)
sapEgrQosQLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosQLastMgmtChange.setStatus("current")
_SapEgrQosQOverrideFlags_Type = TQosQueueAttribute
_SapEgrQosQOverrideFlags_Object = MibTableColumn
sapEgrQosQOverrideFlags = _SapEgrQosQOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 4),
    _SapEgrQosQOverrideFlags_Type()
)
sapEgrQosQOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQOverrideFlags.setStatus("current")


class _SapEgrQosQCBS_Type(TBurstSize):
    """Custom type sapEgrQosQCBS based on TBurstSize"""
    defaultValue = -1


_SapEgrQosQCBS_Object = MibTableColumn
sapEgrQosQCBS = _SapEgrQosQCBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 5),
    _SapEgrQosQCBS_Type()
)
sapEgrQosQCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQCBS.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosQCBS.setUnits("kilo bytes")


class _SapEgrQosQMBS_Type(TBurstSize):
    """Custom type sapEgrQosQMBS based on TBurstSize"""
    defaultValue = -1


_SapEgrQosQMBS_Object = MibTableColumn
sapEgrQosQMBS = _SapEgrQosQMBS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 6),
    _SapEgrQosQMBS_Type()
)
sapEgrQosQMBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQMBS.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosQMBS.setUnits("kilo bytes")


class _SapEgrQosQHiPrioOnly_Type(TBurstPercentOrDefault):
    """Custom type sapEgrQosQHiPrioOnly based on TBurstPercentOrDefault"""
    defaultValue = -1


_SapEgrQosQHiPrioOnly_Object = MibTableColumn
sapEgrQosQHiPrioOnly = _SapEgrQosQHiPrioOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 7),
    _SapEgrQosQHiPrioOnly_Type()
)
sapEgrQosQHiPrioOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQHiPrioOnly.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosQHiPrioOnly.setUnits("percent")


class _SapEgrQosQCIRAdaptation_Type(TAdaptationRule):
    """Custom type sapEgrQosQCIRAdaptation based on TAdaptationRule"""


_SapEgrQosQCIRAdaptation_Object = MibTableColumn
sapEgrQosQCIRAdaptation = _SapEgrQosQCIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 8),
    _SapEgrQosQCIRAdaptation_Type()
)
sapEgrQosQCIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQCIRAdaptation.setStatus("current")


class _SapEgrQosQPIRAdaptation_Type(TAdaptationRule):
    """Custom type sapEgrQosQPIRAdaptation based on TAdaptationRule"""


_SapEgrQosQPIRAdaptation_Object = MibTableColumn
sapEgrQosQPIRAdaptation = _SapEgrQosQPIRAdaptation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 9),
    _SapEgrQosQPIRAdaptation_Type()
)
sapEgrQosQPIRAdaptation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQPIRAdaptation.setStatus("current")


class _SapEgrQosQAdminPIR_Type(TPIRRate):
    """Custom type sapEgrQosQAdminPIR based on TPIRRate"""
    defaultValue = -1


_SapEgrQosQAdminPIR_Object = MibTableColumn
sapEgrQosQAdminPIR = _SapEgrQosQAdminPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 10),
    _SapEgrQosQAdminPIR_Type()
)
sapEgrQosQAdminPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQAdminPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosQAdminPIR.setUnits("kilo bits per second")


class _SapEgrQosQAdminCIR_Type(TCIRRate):
    """Custom type sapEgrQosQAdminCIR based on TCIRRate"""
    defaultValue = -1


_SapEgrQosQAdminCIR_Object = MibTableColumn
sapEgrQosQAdminCIR = _SapEgrQosQAdminCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 11),
    _SapEgrQosQAdminCIR_Type()
)
sapEgrQosQAdminCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQAdminCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosQAdminCIR.setUnits("kilo bits per second")


class _SapEgrQosQAvgOverhead_Type(Unsigned32):
    """Custom type sapEgrQosQAvgOverhead based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SapEgrQosQAvgOverhead_Type.__name__ = "Unsigned32"
_SapEgrQosQAvgOverhead_Object = MibTableColumn
sapEgrQosQAvgOverhead = _SapEgrQosQAvgOverhead_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 20, 1, 12),
    _SapEgrQosQAvgOverhead_Type()
)
sapEgrQosQAvgOverhead.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosQAvgOverhead.setStatus("current")
_SapIngQosSchedInfoTable_Object = MibTable
sapIngQosSchedInfoTable = _SapIngQosSchedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21)
)
if mibBuilder.loadTexts:
    sapIngQosSchedInfoTable.setStatus("current")
_SapIngQosSchedInfoEntry_Object = MibTableRow
sapIngQosSchedInfoEntry = _SapIngQosSchedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1)
)
sapIngQosSchedInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSName"),
)
if mibBuilder.loadTexts:
    sapIngQosSchedInfoEntry.setStatus("current")
_SapIngQosSName_Type = TNamedItem
_SapIngQosSName_Object = MibTableColumn
sapIngQosSName = _SapIngQosSName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 1),
    _SapIngQosSName_Type()
)
sapIngQosSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIngQosSName.setStatus("current")
_SapIngQosSRowStatus_Type = RowStatus
_SapIngQosSRowStatus_Object = MibTableColumn
sapIngQosSRowStatus = _SapIngQosSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 2),
    _SapIngQosSRowStatus_Type()
)
sapIngQosSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosSRowStatus.setStatus("current")
_SapIngQosSLastMgmtChange_Type = TimeStamp
_SapIngQosSLastMgmtChange_Object = MibTableColumn
sapIngQosSLastMgmtChange = _SapIngQosSLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 3),
    _SapIngQosSLastMgmtChange_Type()
)
sapIngQosSLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngQosSLastMgmtChange.setStatus("current")
_SapIngQosSOverrideFlags_Type = TVirtSchedAttribute
_SapIngQosSOverrideFlags_Object = MibTableColumn
sapIngQosSOverrideFlags = _SapIngQosSOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 4),
    _SapIngQosSOverrideFlags_Type()
)
sapIngQosSOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosSOverrideFlags.setStatus("current")


class _SapIngQosSPIR_Type(TPIRRate):
    """Custom type sapIngQosSPIR based on TPIRRate"""
    defaultValue = -1


_SapIngQosSPIR_Object = MibTableColumn
sapIngQosSPIR = _SapIngQosSPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 5),
    _SapIngQosSPIR_Type()
)
sapIngQosSPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosSPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosSPIR.setUnits("kilo bits per second")


class _SapIngQosSCIR_Type(TCIRRate):
    """Custom type sapIngQosSCIR based on TCIRRate"""
    defaultValue = -1


_SapIngQosSCIR_Object = MibTableColumn
sapIngQosSCIR = _SapIngQosSCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 6),
    _SapIngQosSCIR_Type()
)
sapIngQosSCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosSCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapIngQosSCIR.setUnits("kilo bits per second")


class _SapIngQosSSummedCIR_Type(TruthValue):
    """Custom type sapIngQosSSummedCIR based on TruthValue"""


_SapIngQosSSummedCIR_Object = MibTableColumn
sapIngQosSSummedCIR = _SapIngQosSSummedCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 21, 1, 7),
    _SapIngQosSSummedCIR_Type()
)
sapIngQosSSummedCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapIngQosSSummedCIR.setStatus("current")
_SapEgrQosSchedInfoTable_Object = MibTable
sapEgrQosSchedInfoTable = _SapEgrQosSchedInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22)
)
if mibBuilder.loadTexts:
    sapEgrQosSchedInfoTable.setStatus("current")
_SapEgrQosSchedInfoEntry_Object = MibTableRow
sapEgrQosSchedInfoEntry = _SapEgrQosSchedInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1)
)
sapEgrQosSchedInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSName"),
)
if mibBuilder.loadTexts:
    sapEgrQosSchedInfoEntry.setStatus("current")
_SapEgrQosSName_Type = TNamedItem
_SapEgrQosSName_Object = MibTableColumn
sapEgrQosSName = _SapEgrQosSName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 1),
    _SapEgrQosSName_Type()
)
sapEgrQosSName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgrQosSName.setStatus("current")
_SapEgrQosSRowStatus_Type = RowStatus
_SapEgrQosSRowStatus_Object = MibTableColumn
sapEgrQosSRowStatus = _SapEgrQosSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 2),
    _SapEgrQosSRowStatus_Type()
)
sapEgrQosSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosSRowStatus.setStatus("current")
_SapEgrQosSLastMgmtChange_Type = TimeStamp
_SapEgrQosSLastMgmtChange_Object = MibTableColumn
sapEgrQosSLastMgmtChange = _SapEgrQosSLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 3),
    _SapEgrQosSLastMgmtChange_Type()
)
sapEgrQosSLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrQosSLastMgmtChange.setStatus("current")
_SapEgrQosSOverrideFlags_Type = TVirtSchedAttribute
_SapEgrQosSOverrideFlags_Object = MibTableColumn
sapEgrQosSOverrideFlags = _SapEgrQosSOverrideFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 4),
    _SapEgrQosSOverrideFlags_Type()
)
sapEgrQosSOverrideFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosSOverrideFlags.setStatus("current")


class _SapEgrQosSPIR_Type(TPIRRate):
    """Custom type sapEgrQosSPIR based on TPIRRate"""
    defaultValue = -1


_SapEgrQosSPIR_Object = MibTableColumn
sapEgrQosSPIR = _SapEgrQosSPIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 5),
    _SapEgrQosSPIR_Type()
)
sapEgrQosSPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosSPIR.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosSPIR.setUnits("kilo bits per second")


class _SapEgrQosSCIR_Type(TCIRRate):
    """Custom type sapEgrQosSCIR based on TCIRRate"""
    defaultValue = -1


_SapEgrQosSCIR_Object = MibTableColumn
sapEgrQosSCIR = _SapEgrQosSCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 6),
    _SapEgrQosSCIR_Type()
)
sapEgrQosSCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosSCIR.setStatus("current")
if mibBuilder.loadTexts:
    sapEgrQosSCIR.setUnits("kilo bits per second")


class _SapEgrQosSSummedCIR_Type(TruthValue):
    """Custom type sapEgrQosSSummedCIR based on TruthValue"""


_SapEgrQosSSummedCIR_Object = MibTableColumn
sapEgrQosSSummedCIR = _SapEgrQosSSummedCIR_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 22, 1, 7),
    _SapEgrQosSSummedCIR_Type()
)
sapEgrQosSSummedCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEgrQosSSummedCIR.setStatus("current")
_SapSubMgmtInfoTable_Object = MibTable
sapSubMgmtInfoTable = _SapSubMgmtInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23)
)
if mibBuilder.loadTexts:
    sapSubMgmtInfoTable.setStatus("current")
_SapSubMgmtInfoEntry_Object = MibTableRow
sapSubMgmtInfoEntry = _SapSubMgmtInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1)
)
sapSubMgmtInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapSubMgmtInfoEntry.setStatus("current")


class _SapSubMgmtAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type sapSubMgmtAdminStatus based on TmnxEnabledDisabled"""


_SapSubMgmtAdminStatus_Object = MibTableColumn
sapSubMgmtAdminStatus = _SapSubMgmtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 1),
    _SapSubMgmtAdminStatus_Type()
)
sapSubMgmtAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtAdminStatus.setStatus("current")
_SapSubMgmtDefSubProfile_Type = ServObjName
_SapSubMgmtDefSubProfile_Object = MibTableColumn
sapSubMgmtDefSubProfile = _SapSubMgmtDefSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 2),
    _SapSubMgmtDefSubProfile_Type()
)
sapSubMgmtDefSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtDefSubProfile.setStatus("current")
_SapSubMgmtDefSlaProfile_Type = ServObjName
_SapSubMgmtDefSlaProfile_Object = MibTableColumn
sapSubMgmtDefSlaProfile = _SapSubMgmtDefSlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 3),
    _SapSubMgmtDefSlaProfile_Type()
)
sapSubMgmtDefSlaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtDefSlaProfile.setStatus("current")
_SapSubMgmtSubIdentPolicy_Type = ServObjName
_SapSubMgmtSubIdentPolicy_Object = MibTableColumn
sapSubMgmtSubIdentPolicy = _SapSubMgmtSubIdentPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 4),
    _SapSubMgmtSubIdentPolicy_Type()
)
sapSubMgmtSubIdentPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtSubIdentPolicy.setStatus("current")


class _SapSubMgmtSubscriberLimit_Type(Unsigned32):
    """Custom type sapSubMgmtSubscriberLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_SapSubMgmtSubscriberLimit_Type.__name__ = "Unsigned32"
_SapSubMgmtSubscriberLimit_Object = MibTableColumn
sapSubMgmtSubscriberLimit = _SapSubMgmtSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 5),
    _SapSubMgmtSubscriberLimit_Type()
)
sapSubMgmtSubscriberLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtSubscriberLimit.setStatus("current")


class _SapSubMgmtProfiledTrafficOnly_Type(TruthValue):
    """Custom type sapSubMgmtProfiledTrafficOnly based on TruthValue"""


_SapSubMgmtProfiledTrafficOnly_Object = MibTableColumn
sapSubMgmtProfiledTrafficOnly = _SapSubMgmtProfiledTrafficOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 6),
    _SapSubMgmtProfiledTrafficOnly_Type()
)
sapSubMgmtProfiledTrafficOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtProfiledTrafficOnly.setStatus("current")


class _SapSubMgmtNonSubTrafficSubIdent_Type(DisplayString):
    """Custom type sapSubMgmtNonSubTrafficSubIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapSubMgmtNonSubTrafficSubIdent_Type.__name__ = "DisplayString"
_SapSubMgmtNonSubTrafficSubIdent_Object = MibTableColumn
sapSubMgmtNonSubTrafficSubIdent = _SapSubMgmtNonSubTrafficSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 7),
    _SapSubMgmtNonSubTrafficSubIdent_Type()
)
sapSubMgmtNonSubTrafficSubIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtNonSubTrafficSubIdent.setStatus("current")
_SapSubMgmtNonSubTrafficSubProf_Type = ServObjName
_SapSubMgmtNonSubTrafficSubProf_Object = MibTableColumn
sapSubMgmtNonSubTrafficSubProf = _SapSubMgmtNonSubTrafficSubProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 8),
    _SapSubMgmtNonSubTrafficSubProf_Type()
)
sapSubMgmtNonSubTrafficSubProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtNonSubTrafficSubProf.setStatus("current")
_SapSubMgmtNonSubTrafficSlaProf_Type = ServObjName
_SapSubMgmtNonSubTrafficSlaProf_Object = MibTableColumn
sapSubMgmtNonSubTrafficSlaProf = _SapSubMgmtNonSubTrafficSlaProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 9),
    _SapSubMgmtNonSubTrafficSlaProf_Type()
)
sapSubMgmtNonSubTrafficSlaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtNonSubTrafficSlaProf.setStatus("current")


class _SapSubMgmtMacDaHashing_Type(TruthValue):
    """Custom type sapSubMgmtMacDaHashing based on TruthValue"""


_SapSubMgmtMacDaHashing_Object = MibTableColumn
sapSubMgmtMacDaHashing = _SapSubMgmtMacDaHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 10),
    _SapSubMgmtMacDaHashing_Type()
)
sapSubMgmtMacDaHashing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtMacDaHashing.setStatus("current")


class _SapSubMgmtDefSubIdent_Type(Integer32):
    """Custom type sapSubMgmtDefSubIdent based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useSapId", 1),
          ("useString", 2))
    )


_SapSubMgmtDefSubIdent_Type.__name__ = "Integer32"
_SapSubMgmtDefSubIdent_Object = MibTableColumn
sapSubMgmtDefSubIdent = _SapSubMgmtDefSubIdent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 11),
    _SapSubMgmtDefSubIdent_Type()
)
sapSubMgmtDefSubIdent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtDefSubIdent.setStatus("current")


class _SapSubMgmtDefSubIdentString_Type(DisplayString):
    """Custom type sapSubMgmtDefSubIdentString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SapSubMgmtDefSubIdentString_Type.__name__ = "DisplayString"
_SapSubMgmtDefSubIdentString_Object = MibTableColumn
sapSubMgmtDefSubIdentString = _SapSubMgmtDefSubIdentString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 12),
    _SapSubMgmtDefSubIdentString_Type()
)
sapSubMgmtDefSubIdentString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtDefSubIdentString.setStatus("current")
_SapSubMgmtDefAppProfile_Type = ServObjName
_SapSubMgmtDefAppProfile_Object = MibTableColumn
sapSubMgmtDefAppProfile = _SapSubMgmtDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 13),
    _SapSubMgmtDefAppProfile_Type()
)
sapSubMgmtDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtDefAppProfile.setStatus("current")
_SapSubMgmtNonSubTrafficAppProf_Type = ServObjName
_SapSubMgmtNonSubTrafficAppProf_Object = MibTableColumn
sapSubMgmtNonSubTrafficAppProf = _SapSubMgmtNonSubTrafficAppProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 23, 1, 14),
    _SapSubMgmtNonSubTrafficAppProf_Type()
)
sapSubMgmtNonSubTrafficAppProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapSubMgmtNonSubTrafficAppProf.setStatus("current")
_SapTlsMstiTable_Object = MibTable
sapTlsMstiTable = _SapTlsMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24)
)
if mibBuilder.loadTexts:
    sapTlsMstiTable.setStatus("current")
_SapTlsMstiEntry_Object = MibTableRow
sapTlsMstiEntry = _SapTlsMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1)
)
sapTlsMstiEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsMstiInstanceId"),
)
if mibBuilder.loadTexts:
    sapTlsMstiEntry.setStatus("current")


class _SapTlsMstiPriority_Type(Integer32):
    """Custom type sapTlsMstiPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SapTlsMstiPriority_Type.__name__ = "Integer32"
_SapTlsMstiPriority_Object = MibTableColumn
sapTlsMstiPriority = _SapTlsMstiPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 1),
    _SapTlsMstiPriority_Type()
)
sapTlsMstiPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMstiPriority.setStatus("current")


class _SapTlsMstiPathCost_Type(Integer32):
    """Custom type sapTlsMstiPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SapTlsMstiPathCost_Type.__name__ = "Integer32"
_SapTlsMstiPathCost_Object = MibTableColumn
sapTlsMstiPathCost = _SapTlsMstiPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 2),
    _SapTlsMstiPathCost_Type()
)
sapTlsMstiPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapTlsMstiPathCost.setStatus("current")
_SapTlsMstiLastMgmtChange_Type = TimeStamp
_SapTlsMstiLastMgmtChange_Object = MibTableColumn
sapTlsMstiLastMgmtChange = _SapTlsMstiLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 3),
    _SapTlsMstiLastMgmtChange_Type()
)
sapTlsMstiLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMstiLastMgmtChange.setStatus("current")
_SapTlsMstiPortRole_Type = StpPortRole
_SapTlsMstiPortRole_Object = MibTableColumn
sapTlsMstiPortRole = _SapTlsMstiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 4),
    _SapTlsMstiPortRole_Type()
)
sapTlsMstiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMstiPortRole.setStatus("current")
_SapTlsMstiPortState_Type = TStpPortState
_SapTlsMstiPortState_Object = MibTableColumn
sapTlsMstiPortState = _SapTlsMstiPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 5),
    _SapTlsMstiPortState_Type()
)
sapTlsMstiPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMstiPortState.setStatus("current")
_SapTlsMstiDesignatedBridge_Type = BridgeId
_SapTlsMstiDesignatedBridge_Object = MibTableColumn
sapTlsMstiDesignatedBridge = _SapTlsMstiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 6),
    _SapTlsMstiDesignatedBridge_Type()
)
sapTlsMstiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMstiDesignatedBridge.setStatus("current")
_SapTlsMstiDesignatedPort_Type = Integer32
_SapTlsMstiDesignatedPort_Object = MibTableColumn
sapTlsMstiDesignatedPort = _SapTlsMstiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 24, 1, 7),
    _SapTlsMstiDesignatedPort_Type()
)
sapTlsMstiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMstiDesignatedPort.setStatus("current")
_SapIpipeInfoTable_Object = MibTable
sapIpipeInfoTable = _SapIpipeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25)
)
if mibBuilder.loadTexts:
    sapIpipeInfoTable.setStatus("current")
_SapIpipeInfoEntry_Object = MibTableRow
sapIpipeInfoEntry = _SapIpipeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1)
)
sapIpipeInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapIpipeInfoEntry.setStatus("current")
_SapIpipeCeInetAddressType_Type = InetAddressType
_SapIpipeCeInetAddressType_Object = MibTableColumn
sapIpipeCeInetAddressType = _SapIpipeCeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 1),
    _SapIpipeCeInetAddressType_Type()
)
sapIpipeCeInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIpipeCeInetAddressType.setStatus("current")


class _SapIpipeCeInetAddress_Type(InetAddress):
    """Custom type sapIpipeCeInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SapIpipeCeInetAddress_Type.__name__ = "InetAddress"
_SapIpipeCeInetAddress_Object = MibTableColumn
sapIpipeCeInetAddress = _SapIpipeCeInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 2),
    _SapIpipeCeInetAddress_Type()
)
sapIpipeCeInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIpipeCeInetAddress.setStatus("current")


class _SapIpipeMacRefreshInterval_Type(Unsigned32):
    """Custom type sapIpipeMacRefreshInterval based on Unsigned32"""
    defaultValue = 14400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SapIpipeMacRefreshInterval_Type.__name__ = "Unsigned32"
_SapIpipeMacRefreshInterval_Object = MibTableColumn
sapIpipeMacRefreshInterval = _SapIpipeMacRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 3),
    _SapIpipeMacRefreshInterval_Type()
)
sapIpipeMacRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIpipeMacRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    sapIpipeMacRefreshInterval.setUnits("seconds")
_SapIpipeMacAddress_Type = MacAddress
_SapIpipeMacAddress_Object = MibTableColumn
sapIpipeMacAddress = _SapIpipeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 4),
    _SapIpipeMacAddress_Type()
)
sapIpipeMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapIpipeMacAddress.setStatus("current")
_SapIpipeArpedMacAddress_Type = MacAddress
_SapIpipeArpedMacAddress_Object = MibTableColumn
sapIpipeArpedMacAddress = _SapIpipeArpedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 5),
    _SapIpipeArpedMacAddress_Type()
)
sapIpipeArpedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIpipeArpedMacAddress.setStatus("current")


class _SapIpipeArpedMacAddressTimeout_Type(Unsigned32):
    """Custom type sapIpipeArpedMacAddressTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SapIpipeArpedMacAddressTimeout_Type.__name__ = "Unsigned32"
_SapIpipeArpedMacAddressTimeout_Object = MibTableColumn
sapIpipeArpedMacAddressTimeout = _SapIpipeArpedMacAddressTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 25, 1, 6),
    _SapIpipeArpedMacAddressTimeout_Type()
)
sapIpipeArpedMacAddressTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIpipeArpedMacAddressTimeout.setStatus("current")
_SapTodMonitorTable_Object = MibTable
sapTodMonitorTable = _SapTodMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26)
)
if mibBuilder.loadTexts:
    sapTodMonitorTable.setStatus("current")
_SapTodMonitorEntry_Object = MibTableRow
sapTodMonitorEntry = _SapTodMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1)
)
sapTodMonitorEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapTodMonitorEntry.setStatus("current")
_SapCurrentIngressIpFilterId_Type = TFilterID
_SapCurrentIngressIpFilterId_Object = MibTableColumn
sapCurrentIngressIpFilterId = _SapCurrentIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 1),
    _SapCurrentIngressIpFilterId_Type()
)
sapCurrentIngressIpFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentIngressIpFilterId.setStatus("current")
_SapCurrentIngressIpv6FilterId_Type = TFilterID
_SapCurrentIngressIpv6FilterId_Object = MibTableColumn
sapCurrentIngressIpv6FilterId = _SapCurrentIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 2),
    _SapCurrentIngressIpv6FilterId_Type()
)
sapCurrentIngressIpv6FilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentIngressIpv6FilterId.setStatus("current")
_SapCurrentIngressMacFilterId_Type = TFilterID
_SapCurrentIngressMacFilterId_Object = MibTableColumn
sapCurrentIngressMacFilterId = _SapCurrentIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 3),
    _SapCurrentIngressMacFilterId_Type()
)
sapCurrentIngressMacFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentIngressMacFilterId.setStatus("current")
_SapCurrentIngressQosPolicyId_Type = TSapIngressPolicyID
_SapCurrentIngressQosPolicyId_Object = MibTableColumn
sapCurrentIngressQosPolicyId = _SapCurrentIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 4),
    _SapCurrentIngressQosPolicyId_Type()
)
sapCurrentIngressQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentIngressQosPolicyId.setStatus("current")
_SapCurrentIngressQosSchedPlcy_Type = ServObjName
_SapCurrentIngressQosSchedPlcy_Object = MibTableColumn
sapCurrentIngressQosSchedPlcy = _SapCurrentIngressQosSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 5),
    _SapCurrentIngressQosSchedPlcy_Type()
)
sapCurrentIngressQosSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentIngressQosSchedPlcy.setStatus("current")
_SapCurrentEgressIpFilterId_Type = TFilterID
_SapCurrentEgressIpFilterId_Object = MibTableColumn
sapCurrentEgressIpFilterId = _SapCurrentEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 6),
    _SapCurrentEgressIpFilterId_Type()
)
sapCurrentEgressIpFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentEgressIpFilterId.setStatus("current")
_SapCurrentEgressIpv6FilterId_Type = TFilterID
_SapCurrentEgressIpv6FilterId_Object = MibTableColumn
sapCurrentEgressIpv6FilterId = _SapCurrentEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 7),
    _SapCurrentEgressIpv6FilterId_Type()
)
sapCurrentEgressIpv6FilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentEgressIpv6FilterId.setStatus("current")
_SapCurrentEgressMacFilterId_Type = TFilterID
_SapCurrentEgressMacFilterId_Object = MibTableColumn
sapCurrentEgressMacFilterId = _SapCurrentEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 8),
    _SapCurrentEgressMacFilterId_Type()
)
sapCurrentEgressMacFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentEgressMacFilterId.setStatus("current")
_SapCurrentEgressQosPolicyId_Type = TSapEgressPolicyID
_SapCurrentEgressQosPolicyId_Object = MibTableColumn
sapCurrentEgressQosPolicyId = _SapCurrentEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 9),
    _SapCurrentEgressQosPolicyId_Type()
)
sapCurrentEgressQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentEgressQosPolicyId.setStatus("current")
_SapCurrentEgressQosSchedPlcy_Type = ServObjName
_SapCurrentEgressQosSchedPlcy_Object = MibTableColumn
sapCurrentEgressQosSchedPlcy = _SapCurrentEgressQosSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 10),
    _SapCurrentEgressQosSchedPlcy_Type()
)
sapCurrentEgressQosSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCurrentEgressQosSchedPlcy.setStatus("current")
_SapIntendedIngressIpFilterId_Type = TFilterID
_SapIntendedIngressIpFilterId_Object = MibTableColumn
sapIntendedIngressIpFilterId = _SapIntendedIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 11),
    _SapIntendedIngressIpFilterId_Type()
)
sapIntendedIngressIpFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedIngressIpFilterId.setStatus("current")
_SapIntendedIngressIpv6FilterId_Type = TFilterID
_SapIntendedIngressIpv6FilterId_Object = MibTableColumn
sapIntendedIngressIpv6FilterId = _SapIntendedIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 12),
    _SapIntendedIngressIpv6FilterId_Type()
)
sapIntendedIngressIpv6FilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedIngressIpv6FilterId.setStatus("current")
_SapIntendedIngressMacFilterId_Type = TFilterID
_SapIntendedIngressMacFilterId_Object = MibTableColumn
sapIntendedIngressMacFilterId = _SapIntendedIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 13),
    _SapIntendedIngressMacFilterId_Type()
)
sapIntendedIngressMacFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedIngressMacFilterId.setStatus("current")
_SapIntendedIngressQosPolicyId_Type = TSapIngressPolicyID
_SapIntendedIngressQosPolicyId_Object = MibTableColumn
sapIntendedIngressQosPolicyId = _SapIntendedIngressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 14),
    _SapIntendedIngressQosPolicyId_Type()
)
sapIntendedIngressQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedIngressQosPolicyId.setStatus("current")
_SapIntendedIngressQosSchedPlcy_Type = ServObjName
_SapIntendedIngressQosSchedPlcy_Object = MibTableColumn
sapIntendedIngressQosSchedPlcy = _SapIntendedIngressQosSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 15),
    _SapIntendedIngressQosSchedPlcy_Type()
)
sapIntendedIngressQosSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedIngressQosSchedPlcy.setStatus("current")
_SapIntendedEgressIpFilterId_Type = TFilterID
_SapIntendedEgressIpFilterId_Object = MibTableColumn
sapIntendedEgressIpFilterId = _SapIntendedEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 16),
    _SapIntendedEgressIpFilterId_Type()
)
sapIntendedEgressIpFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedEgressIpFilterId.setStatus("current")
_SapIntendedEgressIpv6FilterId_Type = TFilterID
_SapIntendedEgressIpv6FilterId_Object = MibTableColumn
sapIntendedEgressIpv6FilterId = _SapIntendedEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 17),
    _SapIntendedEgressIpv6FilterId_Type()
)
sapIntendedEgressIpv6FilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedEgressIpv6FilterId.setStatus("current")
_SapIntendedEgressMacFilterId_Type = TFilterID
_SapIntendedEgressMacFilterId_Object = MibTableColumn
sapIntendedEgressMacFilterId = _SapIntendedEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 18),
    _SapIntendedEgressMacFilterId_Type()
)
sapIntendedEgressMacFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedEgressMacFilterId.setStatus("current")
_SapIntendedEgressQosPolicyId_Type = TSapEgressPolicyID
_SapIntendedEgressQosPolicyId_Object = MibTableColumn
sapIntendedEgressQosPolicyId = _SapIntendedEgressQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 19),
    _SapIntendedEgressQosPolicyId_Type()
)
sapIntendedEgressQosPolicyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedEgressQosPolicyId.setStatus("current")
_SapIntendedEgressQosSchedPlcy_Type = ServObjName
_SapIntendedEgressQosSchedPlcy_Object = MibTableColumn
sapIntendedEgressQosSchedPlcy = _SapIntendedEgressQosSchedPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 26, 1, 20),
    _SapIntendedEgressQosSchedPlcy_Type()
)
sapIntendedEgressQosSchedPlcy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIntendedEgressQosSchedPlcy.setStatus("current")
_SapIngrQosPlcyStatsTable_Object = MibTable
sapIngrQosPlcyStatsTable = _SapIngrQosPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27)
)
if mibBuilder.loadTexts:
    sapIngrQosPlcyStatsTable.setStatus("current")
_SapIngrQosPlcyStatsEntry_Object = MibTableRow
sapIngrQosPlcyStatsEntry = _SapIngrQosPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1)
)
sapIngrQosPlcyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyId"),
)
if mibBuilder.loadTexts:
    sapIngrQosPlcyStatsEntry.setStatus("current")
_SapIgQosPlcyId_Type = TSapIngressPolicyID
_SapIgQosPlcyId_Object = MibTableColumn
sapIgQosPlcyId = _SapIgQosPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 1),
    _SapIgQosPlcyId_Type()
)
sapIgQosPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgQosPlcyId.setStatus("current")
_SapIgQosPlcyDroppedHiPrioPackets_Type = Counter64
_SapIgQosPlcyDroppedHiPrioPackets_Object = MibTableColumn
sapIgQosPlcyDroppedHiPrioPackets = _SapIgQosPlcyDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 2),
    _SapIgQosPlcyDroppedHiPrioPackets_Type()
)
sapIgQosPlcyDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyDroppedHiPrioPackets.setStatus("current")
_SapIgQosPlcyDroppedHiPrioOctets_Type = Counter64
_SapIgQosPlcyDroppedHiPrioOctets_Object = MibTableColumn
sapIgQosPlcyDroppedHiPrioOctets = _SapIgQosPlcyDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 3),
    _SapIgQosPlcyDroppedHiPrioOctets_Type()
)
sapIgQosPlcyDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyDroppedHiPrioOctets.setStatus("current")
_SapIgQosPlcyDroppedLoPrioPackets_Type = Counter64
_SapIgQosPlcyDroppedLoPrioPackets_Object = MibTableColumn
sapIgQosPlcyDroppedLoPrioPackets = _SapIgQosPlcyDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 4),
    _SapIgQosPlcyDroppedLoPrioPackets_Type()
)
sapIgQosPlcyDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyDroppedLoPrioPackets.setStatus("current")
_SapIgQosPlcyDroppedLoPrioOctets_Type = Counter64
_SapIgQosPlcyDroppedLoPrioOctets_Object = MibTableColumn
sapIgQosPlcyDroppedLoPrioOctets = _SapIgQosPlcyDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 5),
    _SapIgQosPlcyDroppedLoPrioOctets_Type()
)
sapIgQosPlcyDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyDroppedLoPrioOctets.setStatus("current")
_SapIgQosPlcyForwardedInProfPackets_Type = Counter64
_SapIgQosPlcyForwardedInProfPackets_Object = MibTableColumn
sapIgQosPlcyForwardedInProfPackets = _SapIgQosPlcyForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 6),
    _SapIgQosPlcyForwardedInProfPackets_Type()
)
sapIgQosPlcyForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyForwardedInProfPackets.setStatus("current")
_SapIgQosPlcyForwardedInProfOctets_Type = Counter64
_SapIgQosPlcyForwardedInProfOctets_Object = MibTableColumn
sapIgQosPlcyForwardedInProfOctets = _SapIgQosPlcyForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 7),
    _SapIgQosPlcyForwardedInProfOctets_Type()
)
sapIgQosPlcyForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyForwardedInProfOctets.setStatus("current")
_SapIgQosPlcyForwardedOutProfPackets_Type = Counter64
_SapIgQosPlcyForwardedOutProfPackets_Object = MibTableColumn
sapIgQosPlcyForwardedOutProfPackets = _SapIgQosPlcyForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 8),
    _SapIgQosPlcyForwardedOutProfPackets_Type()
)
sapIgQosPlcyForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyForwardedOutProfPackets.setStatus("current")
_SapIgQosPlcyForwardedOutProfOctets_Type = Counter64
_SapIgQosPlcyForwardedOutProfOctets_Object = MibTableColumn
sapIgQosPlcyForwardedOutProfOctets = _SapIgQosPlcyForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 27, 1, 9),
    _SapIgQosPlcyForwardedOutProfOctets_Type()
)
sapIgQosPlcyForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyForwardedOutProfOctets.setStatus("current")
_SapEgrQosPlcyStatsTable_Object = MibTable
sapEgrQosPlcyStatsTable = _SapEgrQosPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28)
)
if mibBuilder.loadTexts:
    sapEgrQosPlcyStatsTable.setStatus("current")
_SapEgrQosPlcyStatsEntry_Object = MibTableRow
sapEgrQosPlcyStatsEntry = _SapEgrQosPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1)
)
sapEgrQosPlcyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyId"),
)
if mibBuilder.loadTexts:
    sapEgrQosPlcyStatsEntry.setStatus("current")
_SapEgQosPlcyId_Type = TSapEgressPolicyID
_SapEgQosPlcyId_Object = MibTableColumn
sapEgQosPlcyId = _SapEgQosPlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 1),
    _SapEgQosPlcyId_Type()
)
sapEgQosPlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgQosPlcyId.setStatus("current")
_SapEgQosPlcyDroppedInProfPackets_Type = Counter64
_SapEgQosPlcyDroppedInProfPackets_Object = MibTableColumn
sapEgQosPlcyDroppedInProfPackets = _SapEgQosPlcyDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 2),
    _SapEgQosPlcyDroppedInProfPackets_Type()
)
sapEgQosPlcyDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyDroppedInProfPackets.setStatus("current")
_SapEgQosPlcyDroppedInProfOctets_Type = Counter64
_SapEgQosPlcyDroppedInProfOctets_Object = MibTableColumn
sapEgQosPlcyDroppedInProfOctets = _SapEgQosPlcyDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 3),
    _SapEgQosPlcyDroppedInProfOctets_Type()
)
sapEgQosPlcyDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyDroppedInProfOctets.setStatus("current")
_SapEgQosPlcyDroppedOutProfPackets_Type = Counter64
_SapEgQosPlcyDroppedOutProfPackets_Object = MibTableColumn
sapEgQosPlcyDroppedOutProfPackets = _SapEgQosPlcyDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 4),
    _SapEgQosPlcyDroppedOutProfPackets_Type()
)
sapEgQosPlcyDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyDroppedOutProfPackets.setStatus("current")
_SapEgQosPlcyDroppedOutProfOctets_Type = Counter64
_SapEgQosPlcyDroppedOutProfOctets_Object = MibTableColumn
sapEgQosPlcyDroppedOutProfOctets = _SapEgQosPlcyDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 5),
    _SapEgQosPlcyDroppedOutProfOctets_Type()
)
sapEgQosPlcyDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyDroppedOutProfOctets.setStatus("current")
_SapEgQosPlcyForwardedInProfPackets_Type = Counter64
_SapEgQosPlcyForwardedInProfPackets_Object = MibTableColumn
sapEgQosPlcyForwardedInProfPackets = _SapEgQosPlcyForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 6),
    _SapEgQosPlcyForwardedInProfPackets_Type()
)
sapEgQosPlcyForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyForwardedInProfPackets.setStatus("current")
_SapEgQosPlcyForwardedInProfOctets_Type = Counter64
_SapEgQosPlcyForwardedInProfOctets_Object = MibTableColumn
sapEgQosPlcyForwardedInProfOctets = _SapEgQosPlcyForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 7),
    _SapEgQosPlcyForwardedInProfOctets_Type()
)
sapEgQosPlcyForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyForwardedInProfOctets.setStatus("current")
_SapEgQosPlcyForwardedOutProfPackets_Type = Counter64
_SapEgQosPlcyForwardedOutProfPackets_Object = MibTableColumn
sapEgQosPlcyForwardedOutProfPackets = _SapEgQosPlcyForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 8),
    _SapEgQosPlcyForwardedOutProfPackets_Type()
)
sapEgQosPlcyForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyForwardedOutProfPackets.setStatus("current")
_SapEgQosPlcyForwardedOutProfOctets_Type = Counter64
_SapEgQosPlcyForwardedOutProfOctets_Object = MibTableColumn
sapEgQosPlcyForwardedOutProfOctets = _SapEgQosPlcyForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 28, 1, 9),
    _SapEgQosPlcyForwardedOutProfOctets_Type()
)
sapEgQosPlcyForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyForwardedOutProfOctets.setStatus("current")
_SapIngQosPlcyQueueStatsTable_Object = MibTable
sapIngQosPlcyQueueStatsTable = _SapIngQosPlcyQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29)
)
if mibBuilder.loadTexts:
    sapIngQosPlcyQueueStatsTable.setStatus("current")
_SapIngQosPlcyQueueStatsEntry_Object = MibTableRow
sapIngQosPlcyQueueStatsEntry = _SapIngQosPlcyQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1)
)
sapIngQosPlcyQueueStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueuePlcyId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueId"),
)
if mibBuilder.loadTexts:
    sapIngQosPlcyQueueStatsEntry.setStatus("current")
_SapIgQosPlcyQueuePlcyId_Type = TSapIngressPolicyID
_SapIgQosPlcyQueuePlcyId_Object = MibTableColumn
sapIgQosPlcyQueuePlcyId = _SapIgQosPlcyQueuePlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 1),
    _SapIgQosPlcyQueuePlcyId_Type()
)
sapIgQosPlcyQueuePlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueuePlcyId.setStatus("current")
_SapIgQosPlcyQueueId_Type = TSapIngQueueId
_SapIgQosPlcyQueueId_Object = MibTableColumn
sapIgQosPlcyQueueId = _SapIgQosPlcyQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 2),
    _SapIgQosPlcyQueueId_Type()
)
sapIgQosPlcyQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueId.setStatus("current")
_SapIgQosPlcyQueueStatsOfferedHiPrioPackets_Type = Counter64
_SapIgQosPlcyQueueStatsOfferedHiPrioPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsOfferedHiPrioPackets = _SapIgQosPlcyQueueStatsOfferedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 3),
    _SapIgQosPlcyQueueStatsOfferedHiPrioPackets_Type()
)
sapIgQosPlcyQueueStatsOfferedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsOfferedHiPrioPackets.setStatus("current")
_SapIgQosPlcyQueueStatsDroppedHiPrioPackets_Type = Counter64
_SapIgQosPlcyQueueStatsDroppedHiPrioPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsDroppedHiPrioPackets = _SapIgQosPlcyQueueStatsDroppedHiPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 4),
    _SapIgQosPlcyQueueStatsDroppedHiPrioPackets_Type()
)
sapIgQosPlcyQueueStatsDroppedHiPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsDroppedHiPrioPackets.setStatus("current")
_SapIgQosPlcyQueueStatsOfferedLoPrioPackets_Type = Counter64
_SapIgQosPlcyQueueStatsOfferedLoPrioPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsOfferedLoPrioPackets = _SapIgQosPlcyQueueStatsOfferedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 5),
    _SapIgQosPlcyQueueStatsOfferedLoPrioPackets_Type()
)
sapIgQosPlcyQueueStatsOfferedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsOfferedLoPrioPackets.setStatus("current")
_SapIgQosPlcyQueueStatsDroppedLoPrioPackets_Type = Counter64
_SapIgQosPlcyQueueStatsDroppedLoPrioPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsDroppedLoPrioPackets = _SapIgQosPlcyQueueStatsDroppedLoPrioPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 6),
    _SapIgQosPlcyQueueStatsDroppedLoPrioPackets_Type()
)
sapIgQosPlcyQueueStatsDroppedLoPrioPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsDroppedLoPrioPackets.setStatus("current")
_SapIgQosPlcyQueueStatsOfferedHiPrioOctets_Type = Counter64
_SapIgQosPlcyQueueStatsOfferedHiPrioOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsOfferedHiPrioOctets = _SapIgQosPlcyQueueStatsOfferedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 7),
    _SapIgQosPlcyQueueStatsOfferedHiPrioOctets_Type()
)
sapIgQosPlcyQueueStatsOfferedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsOfferedHiPrioOctets.setStatus("current")
_SapIgQosPlcyQueueStatsDroppedHiPrioOctets_Type = Counter64
_SapIgQosPlcyQueueStatsDroppedHiPrioOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsDroppedHiPrioOctets = _SapIgQosPlcyQueueStatsDroppedHiPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 8),
    _SapIgQosPlcyQueueStatsDroppedHiPrioOctets_Type()
)
sapIgQosPlcyQueueStatsDroppedHiPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsDroppedHiPrioOctets.setStatus("current")
_SapIgQosPlcyQueueStatsOfferedLoPrioOctets_Type = Counter64
_SapIgQosPlcyQueueStatsOfferedLoPrioOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsOfferedLoPrioOctets = _SapIgQosPlcyQueueStatsOfferedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 9),
    _SapIgQosPlcyQueueStatsOfferedLoPrioOctets_Type()
)
sapIgQosPlcyQueueStatsOfferedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsOfferedLoPrioOctets.setStatus("current")
_SapIgQosPlcyQueueStatsDroppedLoPrioOctets_Type = Counter64
_SapIgQosPlcyQueueStatsDroppedLoPrioOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsDroppedLoPrioOctets = _SapIgQosPlcyQueueStatsDroppedLoPrioOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 10),
    _SapIgQosPlcyQueueStatsDroppedLoPrioOctets_Type()
)
sapIgQosPlcyQueueStatsDroppedLoPrioOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsDroppedLoPrioOctets.setStatus("current")
_SapIgQosPlcyQueueStatsForwardedInProfPackets_Type = Counter64
_SapIgQosPlcyQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsForwardedInProfPackets = _SapIgQosPlcyQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 11),
    _SapIgQosPlcyQueueStatsForwardedInProfPackets_Type()
)
sapIgQosPlcyQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsForwardedInProfPackets.setStatus("current")
_SapIgQosPlcyQueueStatsForwardedOutProfPackets_Type = Counter64
_SapIgQosPlcyQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapIgQosPlcyQueueStatsForwardedOutProfPackets = _SapIgQosPlcyQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 12),
    _SapIgQosPlcyQueueStatsForwardedOutProfPackets_Type()
)
sapIgQosPlcyQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsForwardedOutProfPackets.setStatus("current")
_SapIgQosPlcyQueueStatsForwardedInProfOctets_Type = Counter64
_SapIgQosPlcyQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsForwardedInProfOctets = _SapIgQosPlcyQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 13),
    _SapIgQosPlcyQueueStatsForwardedInProfOctets_Type()
)
sapIgQosPlcyQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsForwardedInProfOctets.setStatus("current")
_SapIgQosPlcyQueueStatsForwardedOutProfOctets_Type = Counter64
_SapIgQosPlcyQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapIgQosPlcyQueueStatsForwardedOutProfOctets = _SapIgQosPlcyQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 14),
    _SapIgQosPlcyQueueStatsForwardedOutProfOctets_Type()
)
sapIgQosPlcyQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsForwardedOutProfOctets.setStatus("current")
_SapIgQosPlcyQueueCustId_Type = TmnxCustId
_SapIgQosPlcyQueueCustId_Object = MibTableColumn
sapIgQosPlcyQueueCustId = _SapIgQosPlcyQueueCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 15),
    _SapIgQosPlcyQueueCustId_Type()
)
sapIgQosPlcyQueueCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueCustId.setStatus("current")
_SapIgQosPlcyQueueStatsUncoloredPacketsOffered_Type = Counter64
_SapIgQosPlcyQueueStatsUncoloredPacketsOffered_Object = MibTableColumn
sapIgQosPlcyQueueStatsUncoloredPacketsOffered = _SapIgQosPlcyQueueStatsUncoloredPacketsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 16),
    _SapIgQosPlcyQueueStatsUncoloredPacketsOffered_Type()
)
sapIgQosPlcyQueueStatsUncoloredPacketsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsUncoloredPacketsOffered.setStatus("current")
_SapIgQosPlcyQueueStatsUncoloredOctetsOffered_Type = Counter64
_SapIgQosPlcyQueueStatsUncoloredOctetsOffered_Object = MibTableColumn
sapIgQosPlcyQueueStatsUncoloredOctetsOffered = _SapIgQosPlcyQueueStatsUncoloredOctetsOffered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 29, 1, 17),
    _SapIgQosPlcyQueueStatsUncoloredOctetsOffered_Type()
)
sapIgQosPlcyQueueStatsUncoloredOctetsOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIgQosPlcyQueueStatsUncoloredOctetsOffered.setStatus("current")
_SapEgrQosPlcyQueueStatsTable_Object = MibTable
sapEgrQosPlcyQueueStatsTable = _SapEgrQosPlcyQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30)
)
if mibBuilder.loadTexts:
    sapEgrQosPlcyQueueStatsTable.setStatus("current")
_SapEgrQosPlcyQueueStatsEntry_Object = MibTableRow
sapEgrQosPlcyQueueStatsEntry = _SapEgrQosPlcyQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1)
)
sapEgrQosPlcyQueueStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueuePlcyId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueId"),
)
if mibBuilder.loadTexts:
    sapEgrQosPlcyQueueStatsEntry.setStatus("current")
_SapEgQosPlcyQueuePlcyId_Type = TSapEgressPolicyID
_SapEgQosPlcyQueuePlcyId_Object = MibTableColumn
sapEgQosPlcyQueuePlcyId = _SapEgQosPlcyQueuePlcyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 1),
    _SapEgQosPlcyQueuePlcyId_Type()
)
sapEgQosPlcyQueuePlcyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueuePlcyId.setStatus("current")
_SapEgQosPlcyQueueId_Type = TSapEgrQueueId
_SapEgQosPlcyQueueId_Object = MibTableColumn
sapEgQosPlcyQueueId = _SapEgQosPlcyQueueId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 2),
    _SapEgQosPlcyQueueId_Type()
)
sapEgQosPlcyQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueId.setStatus("current")
_SapEgQosPlcyQueueStatsForwardedInProfPackets_Type = Counter64
_SapEgQosPlcyQueueStatsForwardedInProfPackets_Object = MibTableColumn
sapEgQosPlcyQueueStatsForwardedInProfPackets = _SapEgQosPlcyQueueStatsForwardedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 3),
    _SapEgQosPlcyQueueStatsForwardedInProfPackets_Type()
)
sapEgQosPlcyQueueStatsForwardedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsForwardedInProfPackets.setStatus("current")
_SapEgQosPlcyQueueStatsDroppedInProfPackets_Type = Counter64
_SapEgQosPlcyQueueStatsDroppedInProfPackets_Object = MibTableColumn
sapEgQosPlcyQueueStatsDroppedInProfPackets = _SapEgQosPlcyQueueStatsDroppedInProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 4),
    _SapEgQosPlcyQueueStatsDroppedInProfPackets_Type()
)
sapEgQosPlcyQueueStatsDroppedInProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsDroppedInProfPackets.setStatus("current")
_SapEgQosPlcyQueueStatsForwardedOutProfPackets_Type = Counter64
_SapEgQosPlcyQueueStatsForwardedOutProfPackets_Object = MibTableColumn
sapEgQosPlcyQueueStatsForwardedOutProfPackets = _SapEgQosPlcyQueueStatsForwardedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 5),
    _SapEgQosPlcyQueueStatsForwardedOutProfPackets_Type()
)
sapEgQosPlcyQueueStatsForwardedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsForwardedOutProfPackets.setStatus("current")
_SapEgQosPlcyQueueStatsDroppedOutProfPackets_Type = Counter64
_SapEgQosPlcyQueueStatsDroppedOutProfPackets_Object = MibTableColumn
sapEgQosPlcyQueueStatsDroppedOutProfPackets = _SapEgQosPlcyQueueStatsDroppedOutProfPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 6),
    _SapEgQosPlcyQueueStatsDroppedOutProfPackets_Type()
)
sapEgQosPlcyQueueStatsDroppedOutProfPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsDroppedOutProfPackets.setStatus("current")
_SapEgQosPlcyQueueStatsForwardedInProfOctets_Type = Counter64
_SapEgQosPlcyQueueStatsForwardedInProfOctets_Object = MibTableColumn
sapEgQosPlcyQueueStatsForwardedInProfOctets = _SapEgQosPlcyQueueStatsForwardedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 7),
    _SapEgQosPlcyQueueStatsForwardedInProfOctets_Type()
)
sapEgQosPlcyQueueStatsForwardedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsForwardedInProfOctets.setStatus("current")
_SapEgQosPlcyQueueStatsDroppedInProfOctets_Type = Counter64
_SapEgQosPlcyQueueStatsDroppedInProfOctets_Object = MibTableColumn
sapEgQosPlcyQueueStatsDroppedInProfOctets = _SapEgQosPlcyQueueStatsDroppedInProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 8),
    _SapEgQosPlcyQueueStatsDroppedInProfOctets_Type()
)
sapEgQosPlcyQueueStatsDroppedInProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsDroppedInProfOctets.setStatus("current")
_SapEgQosPlcyQueueStatsForwardedOutProfOctets_Type = Counter64
_SapEgQosPlcyQueueStatsForwardedOutProfOctets_Object = MibTableColumn
sapEgQosPlcyQueueStatsForwardedOutProfOctets = _SapEgQosPlcyQueueStatsForwardedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 9),
    _SapEgQosPlcyQueueStatsForwardedOutProfOctets_Type()
)
sapEgQosPlcyQueueStatsForwardedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsForwardedOutProfOctets.setStatus("current")
_SapEgQosPlcyQueueStatsDroppedOutProfOctets_Type = Counter64
_SapEgQosPlcyQueueStatsDroppedOutProfOctets_Object = MibTableColumn
sapEgQosPlcyQueueStatsDroppedOutProfOctets = _SapEgQosPlcyQueueStatsDroppedOutProfOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 10),
    _SapEgQosPlcyQueueStatsDroppedOutProfOctets_Type()
)
sapEgQosPlcyQueueStatsDroppedOutProfOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueStatsDroppedOutProfOctets.setStatus("current")
_SapEgQosPlcyQueueCustId_Type = TmnxCustId
_SapEgQosPlcyQueueCustId_Object = MibTableColumn
sapEgQosPlcyQueueCustId = _SapEgQosPlcyQueueCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 30, 1, 11),
    _SapEgQosPlcyQueueCustId_Type()
)
sapEgQosPlcyQueueCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgQosPlcyQueueCustId.setStatus("current")
_SapDhcpInfoTable_Object = MibTable
sapDhcpInfoTable = _SapDhcpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 31)
)
if mibBuilder.loadTexts:
    sapDhcpInfoTable.setStatus("current")
_SapDhcpInfoEntry_Object = MibTableRow
sapDhcpInfoEntry = _SapDhcpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 31, 1)
)
sapDhcpInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapDhcpInfoEntry.setStatus("current")
_SapDhcpOperLeasePopulate_Type = Unsigned32
_SapDhcpOperLeasePopulate_Object = MibTableColumn
sapDhcpOperLeasePopulate = _SapDhcpOperLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 31, 1, 1),
    _SapDhcpOperLeasePopulate_Type()
)
sapDhcpOperLeasePopulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapDhcpOperLeasePopulate.setStatus("current")
_SapIngSchedPlcyStatsTable_Object = MibTable
sapIngSchedPlcyStatsTable = _SapIngSchedPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 32)
)
if mibBuilder.loadTexts:
    sapIngSchedPlcyStatsTable.setStatus("current")
_SapIngSchedPlcyStatsEntry_Object = MibTableRow
sapIngSchedPlcyStatsEntry = _SapIngSchedPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 32, 1)
)
sapIngSchedPlcyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSchedName"),
)
if mibBuilder.loadTexts:
    sapIngSchedPlcyStatsEntry.setStatus("current")
_SapIngSchedPlcyStatsFwdPkt_Type = Counter64
_SapIngSchedPlcyStatsFwdPkt_Object = MibTableColumn
sapIngSchedPlcyStatsFwdPkt = _SapIngSchedPlcyStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 32, 1, 1),
    _SapIngSchedPlcyStatsFwdPkt_Type()
)
sapIngSchedPlcyStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngSchedPlcyStatsFwdPkt.setStatus("current")
_SapIngSchedPlcyStatsFwdOct_Type = Counter64
_SapIngSchedPlcyStatsFwdOct_Object = MibTableColumn
sapIngSchedPlcyStatsFwdOct = _SapIngSchedPlcyStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 32, 1, 2),
    _SapIngSchedPlcyStatsFwdOct_Type()
)
sapIngSchedPlcyStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngSchedPlcyStatsFwdOct.setStatus("current")
_SapEgrSchedPlcyStatsTable_Object = MibTable
sapEgrSchedPlcyStatsTable = _SapEgrSchedPlcyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 33)
)
if mibBuilder.loadTexts:
    sapEgrSchedPlcyStatsTable.setStatus("current")
_SapEgrSchedPlcyStatsEntry_Object = MibTableRow
sapEgrSchedPlcyStatsEntry = _SapEgrSchedPlcyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 33, 1)
)
sapEgrSchedPlcyStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (1, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSchedName"),
)
if mibBuilder.loadTexts:
    sapEgrSchedPlcyStatsEntry.setStatus("current")
_SapEgrSchedPlcyStatsFwdPkt_Type = Counter64
_SapEgrSchedPlcyStatsFwdPkt_Object = MibTableColumn
sapEgrSchedPlcyStatsFwdPkt = _SapEgrSchedPlcyStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 33, 1, 1),
    _SapEgrSchedPlcyStatsFwdPkt_Type()
)
sapEgrSchedPlcyStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrSchedPlcyStatsFwdPkt.setStatus("current")
_SapEgrSchedPlcyStatsFwdOct_Type = Counter64
_SapEgrSchedPlcyStatsFwdOct_Object = MibTableColumn
sapEgrSchedPlcyStatsFwdOct = _SapEgrSchedPlcyStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 33, 1, 2),
    _SapEgrSchedPlcyStatsFwdOct_Type()
)
sapEgrSchedPlcyStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrSchedPlcyStatsFwdOct.setStatus("current")
_SapIngSchedPlcyPortStatsTable_Object = MibTable
sapIngSchedPlcyPortStatsTable = _SapIngSchedPlcyPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 34)
)
if mibBuilder.loadTexts:
    sapIngSchedPlcyPortStatsTable.setStatus("current")
_SapIngSchedPlcyPortStatsEntry_Object = MibTableRow
sapIngSchedPlcyPortStatsEntry = _SapIngSchedPlcyPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 34, 1)
)
sapIngSchedPlcyPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngPortId"),
)
if mibBuilder.loadTexts:
    sapIngSchedPlcyPortStatsEntry.setStatus("current")
_SapIngSchedPlcyPortStatsPort_Type = TmnxPortID
_SapIngSchedPlcyPortStatsPort_Object = MibTableColumn
sapIngSchedPlcyPortStatsPort = _SapIngSchedPlcyPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 34, 1, 1),
    _SapIngSchedPlcyPortStatsPort_Type()
)
sapIngSchedPlcyPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngSchedPlcyPortStatsPort.setStatus("current")
_SapIngSchedPlcyPortStatsFwdPkt_Type = Counter64
_SapIngSchedPlcyPortStatsFwdPkt_Object = MibTableColumn
sapIngSchedPlcyPortStatsFwdPkt = _SapIngSchedPlcyPortStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 34, 1, 2),
    _SapIngSchedPlcyPortStatsFwdPkt_Type()
)
sapIngSchedPlcyPortStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngSchedPlcyPortStatsFwdPkt.setStatus("current")
_SapIngSchedPlcyPortStatsFwdOct_Type = Counter64
_SapIngSchedPlcyPortStatsFwdOct_Object = MibTableColumn
sapIngSchedPlcyPortStatsFwdOct = _SapIngSchedPlcyPortStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 34, 1, 3),
    _SapIngSchedPlcyPortStatsFwdOct_Type()
)
sapIngSchedPlcyPortStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapIngSchedPlcyPortStatsFwdOct.setStatus("current")
_SapEgrSchedPlcyPortStatsTable_Object = MibTable
sapEgrSchedPlcyPortStatsTable = _SapEgrSchedPlcyPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 35)
)
if mibBuilder.loadTexts:
    sapEgrSchedPlcyPortStatsTable.setStatus("current")
_SapEgrSchedPlcyPortStatsEntry_Object = MibTableRow
sapEgrSchedPlcyPortStatsEntry = _SapEgrSchedPlcyPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 35, 1)
)
sapEgrSchedPlcyPortStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tSchedulerPolicyName"),
    (0, "ALCATEL-IND1-TIMETRA-QOS-MIB", "tVirtualSchedulerName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrPortId"),
)
if mibBuilder.loadTexts:
    sapEgrSchedPlcyPortStatsEntry.setStatus("current")
_SapEgrSchedPlcyPortStatsPort_Type = TmnxPortID
_SapEgrSchedPlcyPortStatsPort_Object = MibTableColumn
sapEgrSchedPlcyPortStatsPort = _SapEgrSchedPlcyPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 35, 1, 1),
    _SapEgrSchedPlcyPortStatsPort_Type()
)
sapEgrSchedPlcyPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrSchedPlcyPortStatsPort.setStatus("current")
_SapEgrSchedPlcyPortStatsFwdPkt_Type = Counter64
_SapEgrSchedPlcyPortStatsFwdPkt_Object = MibTableColumn
sapEgrSchedPlcyPortStatsFwdPkt = _SapEgrSchedPlcyPortStatsFwdPkt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 35, 1, 2),
    _SapEgrSchedPlcyPortStatsFwdPkt_Type()
)
sapEgrSchedPlcyPortStatsFwdPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrSchedPlcyPortStatsFwdPkt.setStatus("current")
_SapEgrSchedPlcyPortStatsFwdOct_Type = Counter64
_SapEgrSchedPlcyPortStatsFwdOct_Object = MibTableColumn
sapEgrSchedPlcyPortStatsFwdOct = _SapEgrSchedPlcyPortStatsFwdOct_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 35, 1, 3),
    _SapEgrSchedPlcyPortStatsFwdOct_Type()
)
sapEgrSchedPlcyPortStatsFwdOct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEgrSchedPlcyPortStatsFwdOct.setStatus("current")
_SapCemInfoTable_Object = MibTable
sapCemInfoTable = _SapCemInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40)
)
if mibBuilder.loadTexts:
    sapCemInfoTable.setStatus("current")
_SapCemInfoEntry_Object = MibTableRow
sapCemInfoEntry = _SapCemInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1)
)
sapCemInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapCemInfoEntry.setStatus("current")
_SapCemLastMgmtChange_Type = TimeStamp
_SapCemLastMgmtChange_Object = MibTableColumn
sapCemLastMgmtChange = _SapCemLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 1),
    _SapCemLastMgmtChange_Type()
)
sapCemLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemLastMgmtChange.setStatus("current")


class _SapCemEndpointType_Type(Integer32):
    """Custom type sapCemEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nxDS0", 5),
          ("nxDS0WithCas", 6),
          ("unstructuredE1", 1),
          ("unstructuredE3", 3),
          ("unstructuredT1", 2),
          ("unstructuredT3", 4))
    )


_SapCemEndpointType_Type.__name__ = "Integer32"
_SapCemEndpointType_Object = MibTableColumn
sapCemEndpointType = _SapCemEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 2),
    _SapCemEndpointType_Type()
)
sapCemEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemEndpointType.setStatus("current")


class _SapCemBitrate_Type(Unsigned32):
    """Custom type sapCemBitrate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 699),
    )


_SapCemBitrate_Type.__name__ = "Unsigned32"
_SapCemBitrate_Object = MibTableColumn
sapCemBitrate = _SapCemBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 3),
    _SapCemBitrate_Type()
)
sapCemBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemBitrate.setStatus("current")
if mibBuilder.loadTexts:
    sapCemBitrate.setUnits("64 Kbits/s")
_SapCemCasTrunkFraming_Type = TdmOptionsCasTrunkFraming
_SapCemCasTrunkFraming_Object = MibTableColumn
sapCemCasTrunkFraming = _SapCemCasTrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 4),
    _SapCemCasTrunkFraming_Type()
)
sapCemCasTrunkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemCasTrunkFraming.setStatus("current")


class _SapCemPayloadSize_Type(Unsigned32):
    """Custom type sapCemPayloadSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 2048),
    )


_SapCemPayloadSize_Type.__name__ = "Unsigned32"
_SapCemPayloadSize_Object = MibTableColumn
sapCemPayloadSize = _SapCemPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 5),
    _SapCemPayloadSize_Type()
)
sapCemPayloadSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    sapCemPayloadSize.setUnits("bytes")


class _SapCemJitterBuffer_Type(Unsigned32):
    """Custom type sapCemJitterBuffer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 250),
    )


_SapCemJitterBuffer_Type.__name__ = "Unsigned32"
_SapCemJitterBuffer_Object = MibTableColumn
sapCemJitterBuffer = _SapCemJitterBuffer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 6),
    _SapCemJitterBuffer_Type()
)
sapCemJitterBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemJitterBuffer.setStatus("current")
if mibBuilder.loadTexts:
    sapCemJitterBuffer.setUnits("milliseconds")


class _SapCemUseRtpHeader_Type(TruthValue):
    """Custom type sapCemUseRtpHeader based on TruthValue"""


_SapCemUseRtpHeader_Object = MibTableColumn
sapCemUseRtpHeader = _SapCemUseRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 7),
    _SapCemUseRtpHeader_Type()
)
sapCemUseRtpHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemUseRtpHeader.setStatus("current")
_SapCemDifferential_Type = TruthValue
_SapCemDifferential_Object = MibTableColumn
sapCemDifferential = _SapCemDifferential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 8),
    _SapCemDifferential_Type()
)
sapCemDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemDifferential.setStatus("current")
_SapCemTimestampFreq_Type = Unsigned32
_SapCemTimestampFreq_Object = MibTableColumn
sapCemTimestampFreq = _SapCemTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 9),
    _SapCemTimestampFreq_Type()
)
sapCemTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    sapCemTimestampFreq.setUnits("8 KHz")


class _SapCemReportAlarm_Type(CemSapReportAlarm):
    """Custom type sapCemReportAlarm based on CemSapReportAlarm"""
    defaultBinValue = "011111"


_SapCemReportAlarm_Object = MibTableColumn
sapCemReportAlarm = _SapCemReportAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 10),
    _SapCemReportAlarm_Type()
)
sapCemReportAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemReportAlarm.setStatus("current")
_SapCemReportAlarmStatus_Type = CemSapReportAlarm
_SapCemReportAlarmStatus_Object = MibTableColumn
sapCemReportAlarmStatus = _SapCemReportAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 11),
    _SapCemReportAlarmStatus_Type()
)
sapCemReportAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemReportAlarmStatus.setStatus("current")


class _SapCemLocalEcid_Type(CemSapEcid):
    """Custom type sapCemLocalEcid based on CemSapEcid"""
    defaultValue = 0


_SapCemLocalEcid_Object = MibTableColumn
sapCemLocalEcid = _SapCemLocalEcid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 12),
    _SapCemLocalEcid_Type()
)
sapCemLocalEcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemLocalEcid.setStatus("current")


class _SapCemRemoteMacAddr_Type(MacAddress):
    """Custom type sapCemRemoteMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_SapCemRemoteMacAddr_Object = MibTableColumn
sapCemRemoteMacAddr = _SapCemRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 13),
    _SapCemRemoteMacAddr_Type()
)
sapCemRemoteMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemRemoteMacAddr.setStatus("current")


class _SapCemRemoteEcid_Type(CemSapEcid):
    """Custom type sapCemRemoteEcid based on CemSapEcid"""
    defaultValue = 0


_SapCemRemoteEcid_Object = MibTableColumn
sapCemRemoteEcid = _SapCemRemoteEcid_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 40, 1, 14),
    _SapCemRemoteEcid_Type()
)
sapCemRemoteEcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sapCemRemoteEcid.setStatus("current")
_SapCemStatsTable_Object = MibTable
sapCemStatsTable = _SapCemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41)
)
if mibBuilder.loadTexts:
    sapCemStatsTable.setStatus("current")
_SapCemStatsEntry_Object = MibTableRow
sapCemStatsEntry = _SapCemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1)
)
sapCemStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapCemStatsEntry.setStatus("current")
_SapCemStatsIngressForwardedPkts_Type = Counter32
_SapCemStatsIngressForwardedPkts_Object = MibTableColumn
sapCemStatsIngressForwardedPkts = _SapCemStatsIngressForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 1),
    _SapCemStatsIngressForwardedPkts_Type()
)
sapCemStatsIngressForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsIngressForwardedPkts.setStatus("current")
_SapCemStatsIngressDroppedPkts_Type = Counter32
_SapCemStatsIngressDroppedPkts_Object = MibTableColumn
sapCemStatsIngressDroppedPkts = _SapCemStatsIngressDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 2),
    _SapCemStatsIngressDroppedPkts_Type()
)
sapCemStatsIngressDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsIngressDroppedPkts.setStatus("current")
_SapCemStatsEgressForwardedPkts_Type = Counter32
_SapCemStatsEgressForwardedPkts_Object = MibTableColumn
sapCemStatsEgressForwardedPkts = _SapCemStatsEgressForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 3),
    _SapCemStatsEgressForwardedPkts_Type()
)
sapCemStatsEgressForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressForwardedPkts.setStatus("current")
_SapCemStatsEgressDroppedPkts_Type = Counter32
_SapCemStatsEgressDroppedPkts_Object = MibTableColumn
sapCemStatsEgressDroppedPkts = _SapCemStatsEgressDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 4),
    _SapCemStatsEgressDroppedPkts_Type()
)
sapCemStatsEgressDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressDroppedPkts.setStatus("current")
_SapCemStatsEgressMissingPkts_Type = Counter32
_SapCemStatsEgressMissingPkts_Object = MibTableColumn
sapCemStatsEgressMissingPkts = _SapCemStatsEgressMissingPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 5),
    _SapCemStatsEgressMissingPkts_Type()
)
sapCemStatsEgressMissingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressMissingPkts.setStatus("current")
_SapCemStatsEgressPktsReOrder_Type = Counter32
_SapCemStatsEgressPktsReOrder_Object = MibTableColumn
sapCemStatsEgressPktsReOrder = _SapCemStatsEgressPktsReOrder_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 6),
    _SapCemStatsEgressPktsReOrder_Type()
)
sapCemStatsEgressPktsReOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressPktsReOrder.setStatus("current")
_SapCemStatsEgressJtrBfrUnderruns_Type = Counter32
_SapCemStatsEgressJtrBfrUnderruns_Object = MibTableColumn
sapCemStatsEgressJtrBfrUnderruns = _SapCemStatsEgressJtrBfrUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 7),
    _SapCemStatsEgressJtrBfrUnderruns_Type()
)
sapCemStatsEgressJtrBfrUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressJtrBfrUnderruns.setStatus("current")
_SapCemStatsEgressJtrBfrOverruns_Type = Counter32
_SapCemStatsEgressJtrBfrOverruns_Object = MibTableColumn
sapCemStatsEgressJtrBfrOverruns = _SapCemStatsEgressJtrBfrOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 8),
    _SapCemStatsEgressJtrBfrOverruns_Type()
)
sapCemStatsEgressJtrBfrOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressJtrBfrOverruns.setStatus("current")
_SapCemStatsEgressMisOrderDropped_Type = Counter32
_SapCemStatsEgressMisOrderDropped_Object = MibTableColumn
sapCemStatsEgressMisOrderDropped = _SapCemStatsEgressMisOrderDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 9),
    _SapCemStatsEgressMisOrderDropped_Type()
)
sapCemStatsEgressMisOrderDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressMisOrderDropped.setStatus("current")
_SapCemStatsEgressMalformedPkts_Type = Counter32
_SapCemStatsEgressMalformedPkts_Object = MibTableColumn
sapCemStatsEgressMalformedPkts = _SapCemStatsEgressMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 10),
    _SapCemStatsEgressMalformedPkts_Type()
)
sapCemStatsEgressMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressMalformedPkts.setStatus("current")
_SapCemStatsEgressLBitDropped_Type = Counter32
_SapCemStatsEgressLBitDropped_Object = MibTableColumn
sapCemStatsEgressLBitDropped = _SapCemStatsEgressLBitDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 11),
    _SapCemStatsEgressLBitDropped_Type()
)
sapCemStatsEgressLBitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressLBitDropped.setStatus("current")
_SapCemStatsEgressMultipleDropped_Type = Counter32
_SapCemStatsEgressMultipleDropped_Object = MibTableColumn
sapCemStatsEgressMultipleDropped = _SapCemStatsEgressMultipleDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 12),
    _SapCemStatsEgressMultipleDropped_Type()
)
sapCemStatsEgressMultipleDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressMultipleDropped.setStatus("current")
_SapCemStatsEgressESs_Type = Counter32
_SapCemStatsEgressESs_Object = MibTableColumn
sapCemStatsEgressESs = _SapCemStatsEgressESs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 13),
    _SapCemStatsEgressESs_Type()
)
sapCemStatsEgressESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressESs.setStatus("current")
_SapCemStatsEgressSESs_Type = Counter32
_SapCemStatsEgressSESs_Object = MibTableColumn
sapCemStatsEgressSESs = _SapCemStatsEgressSESs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 14),
    _SapCemStatsEgressSESs_Type()
)
sapCemStatsEgressSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressSESs.setStatus("current")
_SapCemStatsEgressUASs_Type = Counter32
_SapCemStatsEgressUASs_Object = MibTableColumn
sapCemStatsEgressUASs = _SapCemStatsEgressUASs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 15),
    _SapCemStatsEgressUASs_Type()
)
sapCemStatsEgressUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressUASs.setStatus("current")
_SapCemStatsEgressFailureCounts_Type = Counter32
_SapCemStatsEgressFailureCounts_Object = MibTableColumn
sapCemStatsEgressFailureCounts = _SapCemStatsEgressFailureCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 16),
    _SapCemStatsEgressFailureCounts_Type()
)
sapCemStatsEgressFailureCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressFailureCounts.setStatus("current")
_SapCemStatsEgressUnderrunCounts_Type = Counter32
_SapCemStatsEgressUnderrunCounts_Object = MibTableColumn
sapCemStatsEgressUnderrunCounts = _SapCemStatsEgressUnderrunCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 17),
    _SapCemStatsEgressUnderrunCounts_Type()
)
sapCemStatsEgressUnderrunCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressUnderrunCounts.setStatus("current")
_SapCemStatsEgressOverrunCounts_Type = Counter32
_SapCemStatsEgressOverrunCounts_Object = MibTableColumn
sapCemStatsEgressOverrunCounts = _SapCemStatsEgressOverrunCounts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 41, 1, 18),
    _SapCemStatsEgressOverrunCounts_Type()
)
sapCemStatsEgressOverrunCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapCemStatsEgressOverrunCounts.setStatus("current")
_SapTlsL2ptStatsTable_Object = MibTable
sapTlsL2ptStatsTable = _SapTlsL2ptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42)
)
if mibBuilder.loadTexts:
    sapTlsL2ptStatsTable.setStatus("current")
_SapTlsL2ptStatsEntry_Object = MibTableRow
sapTlsL2ptStatsEntry = _SapTlsL2ptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1)
)
sapTlsL2ptStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapTlsL2ptStatsEntry.setStatus("current")
_SapTlsL2ptStatsLastClearedTime_Type = TimeStamp
_SapTlsL2ptStatsLastClearedTime_Object = MibTableColumn
sapTlsL2ptStatsLastClearedTime = _SapTlsL2ptStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 1),
    _SapTlsL2ptStatsLastClearedTime_Type()
)
sapTlsL2ptStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsLastClearedTime.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx = _SapTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 2),
    _SapTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx = _SapTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 3),
    _SapTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpRstBpdusRx = _SapTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 4),
    _SapTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpRstBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpRstBpdusTx = _SapTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 5),
    _SapTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpRstBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx = _SapTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 6),
    _SapTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx = _SapTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 7),
    _SapTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx = _SapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 8),
    _SapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx = _SapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 9),
    _SapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx = _SapTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 10),
    _SapTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx = _SapTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 11),
    _SapTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx = _SapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 12),
    _SapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx = _SapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 13),
    _SapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setStatus("current")
_SapTlsL2ptStatsStpConfigBpdusRx_Type = Counter32
_SapTlsL2ptStatsStpConfigBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsStpConfigBpdusRx = _SapTlsL2ptStatsStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 14),
    _SapTlsL2ptStatsStpConfigBpdusRx_Type()
)
sapTlsL2ptStatsStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpConfigBpdusRx.setStatus("current")
_SapTlsL2ptStatsStpConfigBpdusTx_Type = Counter32
_SapTlsL2ptStatsStpConfigBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsStpConfigBpdusTx = _SapTlsL2ptStatsStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 15),
    _SapTlsL2ptStatsStpConfigBpdusTx_Type()
)
sapTlsL2ptStatsStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpConfigBpdusTx.setStatus("current")
_SapTlsL2ptStatsStpRstBpdusRx_Type = Counter32
_SapTlsL2ptStatsStpRstBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsStpRstBpdusRx = _SapTlsL2ptStatsStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 16),
    _SapTlsL2ptStatsStpRstBpdusRx_Type()
)
sapTlsL2ptStatsStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpRstBpdusRx.setStatus("current")
_SapTlsL2ptStatsStpRstBpdusTx_Type = Counter32
_SapTlsL2ptStatsStpRstBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsStpRstBpdusTx = _SapTlsL2ptStatsStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 17),
    _SapTlsL2ptStatsStpRstBpdusTx_Type()
)
sapTlsL2ptStatsStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpRstBpdusTx.setStatus("current")
_SapTlsL2ptStatsStpTcnBpdusRx_Type = Counter32
_SapTlsL2ptStatsStpTcnBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsStpTcnBpdusRx = _SapTlsL2ptStatsStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 18),
    _SapTlsL2ptStatsStpTcnBpdusRx_Type()
)
sapTlsL2ptStatsStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpTcnBpdusRx.setStatus("current")
_SapTlsL2ptStatsStpTcnBpdusTx_Type = Counter32
_SapTlsL2ptStatsStpTcnBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsStpTcnBpdusTx = _SapTlsL2ptStatsStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 19),
    _SapTlsL2ptStatsStpTcnBpdusTx_Type()
)
sapTlsL2ptStatsStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsStpTcnBpdusTx.setStatus("current")
_SapTlsL2ptStatsPvstConfigBpdusRx_Type = Counter32
_SapTlsL2ptStatsPvstConfigBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsPvstConfigBpdusRx = _SapTlsL2ptStatsPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 20),
    _SapTlsL2ptStatsPvstConfigBpdusRx_Type()
)
sapTlsL2ptStatsPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstConfigBpdusRx.setStatus("current")
_SapTlsL2ptStatsPvstConfigBpdusTx_Type = Counter32
_SapTlsL2ptStatsPvstConfigBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsPvstConfigBpdusTx = _SapTlsL2ptStatsPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 21),
    _SapTlsL2ptStatsPvstConfigBpdusTx_Type()
)
sapTlsL2ptStatsPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstConfigBpdusTx.setStatus("current")
_SapTlsL2ptStatsPvstRstBpdusRx_Type = Counter32
_SapTlsL2ptStatsPvstRstBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsPvstRstBpdusRx = _SapTlsL2ptStatsPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 22),
    _SapTlsL2ptStatsPvstRstBpdusRx_Type()
)
sapTlsL2ptStatsPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstRstBpdusRx.setStatus("current")
_SapTlsL2ptStatsPvstRstBpdusTx_Type = Counter32
_SapTlsL2ptStatsPvstRstBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsPvstRstBpdusTx = _SapTlsL2ptStatsPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 23),
    _SapTlsL2ptStatsPvstRstBpdusTx_Type()
)
sapTlsL2ptStatsPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstRstBpdusTx.setStatus("current")
_SapTlsL2ptStatsPvstTcnBpdusRx_Type = Counter32
_SapTlsL2ptStatsPvstTcnBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsPvstTcnBpdusRx = _SapTlsL2ptStatsPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 24),
    _SapTlsL2ptStatsPvstTcnBpdusRx_Type()
)
sapTlsL2ptStatsPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstTcnBpdusRx.setStatus("current")
_SapTlsL2ptStatsPvstTcnBpdusTx_Type = Counter32
_SapTlsL2ptStatsPvstTcnBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsPvstTcnBpdusTx = _SapTlsL2ptStatsPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 25),
    _SapTlsL2ptStatsPvstTcnBpdusTx_Type()
)
sapTlsL2ptStatsPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPvstTcnBpdusTx.setStatus("current")
_SapTlsL2ptStatsOtherBpdusRx_Type = Counter32
_SapTlsL2ptStatsOtherBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsOtherBpdusRx = _SapTlsL2ptStatsOtherBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 26),
    _SapTlsL2ptStatsOtherBpdusRx_Type()
)
sapTlsL2ptStatsOtherBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherBpdusRx.setStatus("current")
_SapTlsL2ptStatsOtherBpdusTx_Type = Counter32
_SapTlsL2ptStatsOtherBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsOtherBpdusTx = _SapTlsL2ptStatsOtherBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 27),
    _SapTlsL2ptStatsOtherBpdusTx_Type()
)
sapTlsL2ptStatsOtherBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherBpdusTx.setStatus("current")
_SapTlsL2ptStatsOtherL2ptBpdusRx_Type = Counter32
_SapTlsL2ptStatsOtherL2ptBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsOtherL2ptBpdusRx = _SapTlsL2ptStatsOtherL2ptBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 28),
    _SapTlsL2ptStatsOtherL2ptBpdusRx_Type()
)
sapTlsL2ptStatsOtherL2ptBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherL2ptBpdusRx.setStatus("current")
_SapTlsL2ptStatsOtherL2ptBpdusTx_Type = Counter32
_SapTlsL2ptStatsOtherL2ptBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsOtherL2ptBpdusTx = _SapTlsL2ptStatsOtherL2ptBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 29),
    _SapTlsL2ptStatsOtherL2ptBpdusTx_Type()
)
sapTlsL2ptStatsOtherL2ptBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherL2ptBpdusTx.setStatus("current")
_SapTlsL2ptStatsOtherInvalidBpdusRx_Type = Counter32
_SapTlsL2ptStatsOtherInvalidBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsOtherInvalidBpdusRx = _SapTlsL2ptStatsOtherInvalidBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 30),
    _SapTlsL2ptStatsOtherInvalidBpdusRx_Type()
)
sapTlsL2ptStatsOtherInvalidBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherInvalidBpdusRx.setStatus("current")
_SapTlsL2ptStatsOtherInvalidBpdusTx_Type = Counter32
_SapTlsL2ptStatsOtherInvalidBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsOtherInvalidBpdusTx = _SapTlsL2ptStatsOtherInvalidBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 31),
    _SapTlsL2ptStatsOtherInvalidBpdusTx_Type()
)
sapTlsL2ptStatsOtherInvalidBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsOtherInvalidBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapCdpBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapCdpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapCdpBpdusRx = _SapTlsL2ptStatsL2ptEncapCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 32),
    _SapTlsL2ptStatsL2ptEncapCdpBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapCdpBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapCdpBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapCdpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapCdpBpdusTx = _SapTlsL2ptStatsL2ptEncapCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 33),
    _SapTlsL2ptStatsL2ptEncapCdpBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapCdpBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapVtpBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapVtpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapVtpBpdusRx = _SapTlsL2ptStatsL2ptEncapVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 34),
    _SapTlsL2ptStatsL2ptEncapVtpBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapVtpBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapVtpBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapVtpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapVtpBpdusTx = _SapTlsL2ptStatsL2ptEncapVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 35),
    _SapTlsL2ptStatsL2ptEncapVtpBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapVtpBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapDtpBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapDtpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapDtpBpdusRx = _SapTlsL2ptStatsL2ptEncapDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 36),
    _SapTlsL2ptStatsL2ptEncapDtpBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapDtpBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapDtpBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapDtpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapDtpBpdusTx = _SapTlsL2ptStatsL2ptEncapDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 37),
    _SapTlsL2ptStatsL2ptEncapDtpBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapDtpBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPagpBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPagpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPagpBpdusRx = _SapTlsL2ptStatsL2ptEncapPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 38),
    _SapTlsL2ptStatsL2ptEncapPagpBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPagpBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapPagpBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapPagpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapPagpBpdusTx = _SapTlsL2ptStatsL2ptEncapPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 39),
    _SapTlsL2ptStatsL2ptEncapPagpBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapPagpBpdusTx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapUdldBpdusRx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapUdldBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapUdldBpdusRx = _SapTlsL2ptStatsL2ptEncapUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 40),
    _SapTlsL2ptStatsL2ptEncapUdldBpdusRx_Type()
)
sapTlsL2ptStatsL2ptEncapUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapUdldBpdusRx.setStatus("current")
_SapTlsL2ptStatsL2ptEncapUdldBpdusTx_Type = Counter32
_SapTlsL2ptStatsL2ptEncapUdldBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsL2ptEncapUdldBpdusTx = _SapTlsL2ptStatsL2ptEncapUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 41),
    _SapTlsL2ptStatsL2ptEncapUdldBpdusTx_Type()
)
sapTlsL2ptStatsL2ptEncapUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsL2ptEncapUdldBpdusTx.setStatus("current")
_SapTlsL2ptStatsCdpBpdusRx_Type = Counter32
_SapTlsL2ptStatsCdpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsCdpBpdusRx = _SapTlsL2ptStatsCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 42),
    _SapTlsL2ptStatsCdpBpdusRx_Type()
)
sapTlsL2ptStatsCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsCdpBpdusRx.setStatus("current")
_SapTlsL2ptStatsCdpBpdusTx_Type = Counter32
_SapTlsL2ptStatsCdpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsCdpBpdusTx = _SapTlsL2ptStatsCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 43),
    _SapTlsL2ptStatsCdpBpdusTx_Type()
)
sapTlsL2ptStatsCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsCdpBpdusTx.setStatus("current")
_SapTlsL2ptStatsVtpBpdusRx_Type = Counter32
_SapTlsL2ptStatsVtpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsVtpBpdusRx = _SapTlsL2ptStatsVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 44),
    _SapTlsL2ptStatsVtpBpdusRx_Type()
)
sapTlsL2ptStatsVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsVtpBpdusRx.setStatus("current")
_SapTlsL2ptStatsVtpBpdusTx_Type = Counter32
_SapTlsL2ptStatsVtpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsVtpBpdusTx = _SapTlsL2ptStatsVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 45),
    _SapTlsL2ptStatsVtpBpdusTx_Type()
)
sapTlsL2ptStatsVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsVtpBpdusTx.setStatus("current")
_SapTlsL2ptStatsDtpBpdusRx_Type = Counter32
_SapTlsL2ptStatsDtpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsDtpBpdusRx = _SapTlsL2ptStatsDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 46),
    _SapTlsL2ptStatsDtpBpdusRx_Type()
)
sapTlsL2ptStatsDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsDtpBpdusRx.setStatus("current")
_SapTlsL2ptStatsDtpBpdusTx_Type = Counter32
_SapTlsL2ptStatsDtpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsDtpBpdusTx = _SapTlsL2ptStatsDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 47),
    _SapTlsL2ptStatsDtpBpdusTx_Type()
)
sapTlsL2ptStatsDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsDtpBpdusTx.setStatus("current")
_SapTlsL2ptStatsPagpBpdusRx_Type = Counter32
_SapTlsL2ptStatsPagpBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsPagpBpdusRx = _SapTlsL2ptStatsPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 48),
    _SapTlsL2ptStatsPagpBpdusRx_Type()
)
sapTlsL2ptStatsPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPagpBpdusRx.setStatus("current")
_SapTlsL2ptStatsPagpBpdusTx_Type = Counter32
_SapTlsL2ptStatsPagpBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsPagpBpdusTx = _SapTlsL2ptStatsPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 49),
    _SapTlsL2ptStatsPagpBpdusTx_Type()
)
sapTlsL2ptStatsPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsPagpBpdusTx.setStatus("current")
_SapTlsL2ptStatsUdldBpdusRx_Type = Counter32
_SapTlsL2ptStatsUdldBpdusRx_Object = MibTableColumn
sapTlsL2ptStatsUdldBpdusRx = _SapTlsL2ptStatsUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 50),
    _SapTlsL2ptStatsUdldBpdusRx_Type()
)
sapTlsL2ptStatsUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsUdldBpdusRx.setStatus("current")
_SapTlsL2ptStatsUdldBpdusTx_Type = Counter32
_SapTlsL2ptStatsUdldBpdusTx_Object = MibTableColumn
sapTlsL2ptStatsUdldBpdusTx = _SapTlsL2ptStatsUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 42, 1, 51),
    _SapTlsL2ptStatsUdldBpdusTx_Type()
)
sapTlsL2ptStatsUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsL2ptStatsUdldBpdusTx.setStatus("current")
_SapEthernetInfoTable_Object = MibTable
sapEthernetInfoTable = _SapEthernetInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 43)
)
if mibBuilder.loadTexts:
    sapEthernetInfoTable.setStatus("current")
_SapEthernetInfoEntry_Object = MibTableRow
sapEthernetInfoEntry = _SapEthernetInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 43, 1)
)
sapEthernetInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    sapEthernetInfoEntry.setStatus("current")


class _SapEthernetLLFAdminStatus_Type(ServiceAdminStatus):
    """Custom type sapEthernetLLFAdminStatus based on ServiceAdminStatus"""


_SapEthernetLLFAdminStatus_Object = MibTableColumn
sapEthernetLLFAdminStatus = _SapEthernetLLFAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 43, 1, 1),
    _SapEthernetLLFAdminStatus_Type()
)
sapEthernetLLFAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sapEthernetLLFAdminStatus.setStatus("current")


class _SapEthernetLLFOperStatus_Type(Integer32):
    """Custom type sapEthernetLLFOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("fault", 1))
    )


_SapEthernetLLFOperStatus_Type.__name__ = "Integer32"
_SapEthernetLLFOperStatus_Object = MibTableColumn
sapEthernetLLFOperStatus = _SapEthernetLLFOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 43, 1, 2),
    _SapEthernetLLFOperStatus_Type()
)
sapEthernetLLFOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapEthernetLLFOperStatus.setStatus("current")
_MsapPlcyTable_Object = MibTable
msapPlcyTable = _MsapPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44)
)
if mibBuilder.loadTexts:
    msapPlcyTable.setStatus("current")
_MsapPlcyEntry_Object = MibTableRow
msapPlcyEntry = _MsapPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1)
)
msapPlcyEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyName"),
)
if mibBuilder.loadTexts:
    msapPlcyEntry.setStatus("current")
_MsapPlcyName_Type = TNamedItem
_MsapPlcyName_Object = MibTableColumn
msapPlcyName = _MsapPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 1),
    _MsapPlcyName_Type()
)
msapPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msapPlcyName.setStatus("current")
_MsapPlcyRowStatus_Type = RowStatus
_MsapPlcyRowStatus_Object = MibTableColumn
msapPlcyRowStatus = _MsapPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 2),
    _MsapPlcyRowStatus_Type()
)
msapPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcyRowStatus.setStatus("current")
_MsapPlcyLastChanged_Type = TimeStamp
_MsapPlcyLastChanged_Object = MibTableColumn
msapPlcyLastChanged = _MsapPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 3),
    _MsapPlcyLastChanged_Type()
)
msapPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapPlcyLastChanged.setStatus("current")
_MsapPlcyDescription_Type = TItemDescription
_MsapPlcyDescription_Object = MibTableColumn
msapPlcyDescription = _MsapPlcyDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 4),
    _MsapPlcyDescription_Type()
)
msapPlcyDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcyDescription.setStatus("current")


class _MsapPlcyCpmProtPolicyId_Type(TCpmProtPolicyID):
    """Custom type msapPlcyCpmProtPolicyId based on TCpmProtPolicyID"""
    defaultValue = 1


_MsapPlcyCpmProtPolicyId_Object = MibTableColumn
msapPlcyCpmProtPolicyId = _MsapPlcyCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 5),
    _MsapPlcyCpmProtPolicyId_Type()
)
msapPlcyCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcyCpmProtPolicyId.setStatus("current")


class _MsapPlcyCpmProtMonitorMac_Type(TruthValue):
    """Custom type msapPlcyCpmProtMonitorMac based on TruthValue"""


_MsapPlcyCpmProtMonitorMac_Object = MibTableColumn
msapPlcyCpmProtMonitorMac = _MsapPlcyCpmProtMonitorMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 6),
    _MsapPlcyCpmProtMonitorMac_Type()
)
msapPlcyCpmProtMonitorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcyCpmProtMonitorMac.setStatus("current")


class _MsapPlcySubMgmtDefSubId_Type(Integer32):
    """Custom type msapPlcySubMgmtDefSubId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useSapId", 1),
          ("useString", 2))
    )


_MsapPlcySubMgmtDefSubId_Type.__name__ = "Integer32"
_MsapPlcySubMgmtDefSubId_Object = MibTableColumn
msapPlcySubMgmtDefSubId = _MsapPlcySubMgmtDefSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 7),
    _MsapPlcySubMgmtDefSubId_Type()
)
msapPlcySubMgmtDefSubId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtDefSubId.setStatus("current")
_MsapPlcySubMgmtDefSubIdStr_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtDefSubIdStr_Object = MibTableColumn
msapPlcySubMgmtDefSubIdStr = _MsapPlcySubMgmtDefSubIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 8),
    _MsapPlcySubMgmtDefSubIdStr_Type()
)
msapPlcySubMgmtDefSubIdStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtDefSubIdStr.setStatus("current")
_MsapPlcySubMgmtDefSubProfile_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtDefSubProfile_Object = MibTableColumn
msapPlcySubMgmtDefSubProfile = _MsapPlcySubMgmtDefSubProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 9),
    _MsapPlcySubMgmtDefSubProfile_Type()
)
msapPlcySubMgmtDefSubProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtDefSubProfile.setStatus("current")
_MsapPlcySubMgmtDefSlaProfile_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtDefSlaProfile_Object = MibTableColumn
msapPlcySubMgmtDefSlaProfile = _MsapPlcySubMgmtDefSlaProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 10),
    _MsapPlcySubMgmtDefSlaProfile_Type()
)
msapPlcySubMgmtDefSlaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtDefSlaProfile.setStatus("current")
_MsapPlcySubMgmtDefAppProfile_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtDefAppProfile_Object = MibTableColumn
msapPlcySubMgmtDefAppProfile = _MsapPlcySubMgmtDefAppProfile_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 11),
    _MsapPlcySubMgmtDefAppProfile_Type()
)
msapPlcySubMgmtDefAppProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtDefAppProfile.setStatus("current")
_MsapPlcySubMgmtSubIdPlcy_Type = TPolicyStatementNameOrEmpty
_MsapPlcySubMgmtSubIdPlcy_Object = MibTableColumn
msapPlcySubMgmtSubIdPlcy = _MsapPlcySubMgmtSubIdPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 12),
    _MsapPlcySubMgmtSubIdPlcy_Type()
)
msapPlcySubMgmtSubIdPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtSubIdPlcy.setStatus("current")


class _MsapPlcySubMgmtSubscriberLimit_Type(Unsigned32):
    """Custom type msapPlcySubMgmtSubscriberLimit based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_MsapPlcySubMgmtSubscriberLimit_Type.__name__ = "Unsigned32"
_MsapPlcySubMgmtSubscriberLimit_Object = MibTableColumn
msapPlcySubMgmtSubscriberLimit = _MsapPlcySubMgmtSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 13),
    _MsapPlcySubMgmtSubscriberLimit_Type()
)
msapPlcySubMgmtSubscriberLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtSubscriberLimit.setStatus("current")


class _MsapPlcySubMgmtProfiledTrafOnly_Type(TruthValue):
    """Custom type msapPlcySubMgmtProfiledTrafOnly based on TruthValue"""


_MsapPlcySubMgmtProfiledTrafOnly_Object = MibTableColumn
msapPlcySubMgmtProfiledTrafOnly = _MsapPlcySubMgmtProfiledTrafOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 14),
    _MsapPlcySubMgmtProfiledTrafOnly_Type()
)
msapPlcySubMgmtProfiledTrafOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtProfiledTrafOnly.setStatus("current")
_MsapPlcySubMgmtNonSubTrafSubId_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtNonSubTrafSubId_Object = MibTableColumn
msapPlcySubMgmtNonSubTrafSubId = _MsapPlcySubMgmtNonSubTrafSubId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 15),
    _MsapPlcySubMgmtNonSubTrafSubId_Type()
)
msapPlcySubMgmtNonSubTrafSubId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtNonSubTrafSubId.setStatus("current")
_MsapPlcySubMgmtNonSubTrafSubProf_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtNonSubTrafSubProf_Object = MibTableColumn
msapPlcySubMgmtNonSubTrafSubProf = _MsapPlcySubMgmtNonSubTrafSubProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 16),
    _MsapPlcySubMgmtNonSubTrafSubProf_Type()
)
msapPlcySubMgmtNonSubTrafSubProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtNonSubTrafSubProf.setStatus("current")
_MsapPlcySubMgmtNonSubTrafSlaProf_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtNonSubTrafSlaProf_Object = MibTableColumn
msapPlcySubMgmtNonSubTrafSlaProf = _MsapPlcySubMgmtNonSubTrafSlaProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 17),
    _MsapPlcySubMgmtNonSubTrafSlaProf_Type()
)
msapPlcySubMgmtNonSubTrafSlaProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtNonSubTrafSlaProf.setStatus("current")
_MsapPlcySubMgmtNonSubTrafAppProf_Type = TNamedItemOrEmpty
_MsapPlcySubMgmtNonSubTrafAppProf_Object = MibTableColumn
msapPlcySubMgmtNonSubTrafAppProf = _MsapPlcySubMgmtNonSubTrafAppProf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 18),
    _MsapPlcySubMgmtNonSubTrafAppProf_Type()
)
msapPlcySubMgmtNonSubTrafAppProf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapPlcySubMgmtNonSubTrafAppProf.setStatus("current")
_MsapPlcyAssociatedMsaps_Type = Counter32
_MsapPlcyAssociatedMsaps_Object = MibTableColumn
msapPlcyAssociatedMsaps = _MsapPlcyAssociatedMsaps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 44, 1, 19),
    _MsapPlcyAssociatedMsaps_Type()
)
msapPlcyAssociatedMsaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapPlcyAssociatedMsaps.setStatus("current")
_MsapTlsPlcyTable_Object = MibTable
msapTlsPlcyTable = _MsapTlsPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45)
)
if mibBuilder.loadTexts:
    msapTlsPlcyTable.setStatus("current")
_MsapTlsPlcyEntry_Object = MibTableRow
msapTlsPlcyEntry = _MsapTlsPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1)
)
if mibBuilder.loadTexts:
    msapTlsPlcyEntry.setStatus("current")
_MsapTlsPlcyLastChanged_Type = TimeStamp
_MsapTlsPlcyLastChanged_Object = MibTableColumn
msapTlsPlcyLastChanged = _MsapTlsPlcyLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 1),
    _MsapTlsPlcyLastChanged_Type()
)
msapTlsPlcyLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapTlsPlcyLastChanged.setStatus("current")
_MsapTlsPlcySplitHorizonGrp_Type = TNamedItemOrEmpty
_MsapTlsPlcySplitHorizonGrp_Object = MibTableColumn
msapTlsPlcySplitHorizonGrp = _MsapTlsPlcySplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 2),
    _MsapTlsPlcySplitHorizonGrp_Type()
)
msapTlsPlcySplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcySplitHorizonGrp.setStatus("current")


class _MsapTlsPlcyArpReplyAgent_Type(Integer32):
    """Custom type msapTlsPlcyArpReplyAgent based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWithSubscrIdent", 3))
    )


_MsapTlsPlcyArpReplyAgent_Type.__name__ = "Integer32"
_MsapTlsPlcyArpReplyAgent_Object = MibTableColumn
msapTlsPlcyArpReplyAgent = _MsapTlsPlcyArpReplyAgent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 3),
    _MsapTlsPlcyArpReplyAgent_Type()
)
msapTlsPlcyArpReplyAgent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyArpReplyAgent.setStatus("current")


class _MsapTlsPlcySubMgmtMacDaHashing_Type(TruthValue):
    """Custom type msapTlsPlcySubMgmtMacDaHashing based on TruthValue"""


_MsapTlsPlcySubMgmtMacDaHashing_Object = MibTableColumn
msapTlsPlcySubMgmtMacDaHashing = _MsapTlsPlcySubMgmtMacDaHashing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 4),
    _MsapTlsPlcySubMgmtMacDaHashing_Type()
)
msapTlsPlcySubMgmtMacDaHashing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcySubMgmtMacDaHashing.setStatus("current")


class _MsapTlsPlcyDhcpLeasePopulate_Type(Unsigned32):
    """Custom type msapTlsPlcyDhcpLeasePopulate based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_MsapTlsPlcyDhcpLeasePopulate_Type.__name__ = "Unsigned32"
_MsapTlsPlcyDhcpLeasePopulate_Object = MibTableColumn
msapTlsPlcyDhcpLeasePopulate = _MsapTlsPlcyDhcpLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 5),
    _MsapTlsPlcyDhcpLeasePopulate_Type()
)
msapTlsPlcyDhcpLeasePopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpLeasePopulate.setStatus("current")


class _MsapTlsPlcyDhcpPrxyAdminState_Type(TmnxEnabledDisabled):
    """Custom type msapTlsPlcyDhcpPrxyAdminState based on TmnxEnabledDisabled"""


_MsapTlsPlcyDhcpPrxyAdminState_Object = MibTableColumn
msapTlsPlcyDhcpPrxyAdminState = _MsapTlsPlcyDhcpPrxyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 6),
    _MsapTlsPlcyDhcpPrxyAdminState_Type()
)
msapTlsPlcyDhcpPrxyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyAdminState.setStatus("current")


class _MsapTlsPlcyDhcpPrxyServAddrType_Type(InetAddressType):
    """Custom type msapTlsPlcyDhcpPrxyServAddrType based on InetAddressType"""


_MsapTlsPlcyDhcpPrxyServAddrType_Object = MibTableColumn
msapTlsPlcyDhcpPrxyServAddrType = _MsapTlsPlcyDhcpPrxyServAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 7),
    _MsapTlsPlcyDhcpPrxyServAddrType_Type()
)
msapTlsPlcyDhcpPrxyServAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyServAddrType.setStatus("current")


class _MsapTlsPlcyDhcpPrxyServAddr_Type(InetAddress):
    """Custom type msapTlsPlcyDhcpPrxyServAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_MsapTlsPlcyDhcpPrxyServAddr_Type.__name__ = "InetAddress"
_MsapTlsPlcyDhcpPrxyServAddr_Object = MibTableColumn
msapTlsPlcyDhcpPrxyServAddr = _MsapTlsPlcyDhcpPrxyServAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 8),
    _MsapTlsPlcyDhcpPrxyServAddr_Type()
)
msapTlsPlcyDhcpPrxyServAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyServAddr.setStatus("current")


class _MsapTlsPlcyDhcpPrxyLeaseTime_Type(Unsigned32):
    """Custom type msapTlsPlcyDhcpPrxyLeaseTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
    )


_MsapTlsPlcyDhcpPrxyLeaseTime_Type.__name__ = "Unsigned32"
_MsapTlsPlcyDhcpPrxyLeaseTime_Object = MibTableColumn
msapTlsPlcyDhcpPrxyLeaseTime = _MsapTlsPlcyDhcpPrxyLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 9),
    _MsapTlsPlcyDhcpPrxyLeaseTime_Type()
)
msapTlsPlcyDhcpPrxyLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyLeaseTime.setUnits("seconds")


class _MsapTlsPlcyDhcpPrxyLTRadOverride_Type(TruthValue):
    """Custom type msapTlsPlcyDhcpPrxyLTRadOverride based on TruthValue"""


_MsapTlsPlcyDhcpPrxyLTRadOverride_Object = MibTableColumn
msapTlsPlcyDhcpPrxyLTRadOverride = _MsapTlsPlcyDhcpPrxyLTRadOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 10),
    _MsapTlsPlcyDhcpPrxyLTRadOverride_Type()
)
msapTlsPlcyDhcpPrxyLTRadOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpPrxyLTRadOverride.setStatus("current")


class _MsapTlsPlcyDhcpInfoAction_Type(Integer32):
    """Custom type msapTlsPlcyDhcpInfoAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_MsapTlsPlcyDhcpInfoAction_Type.__name__ = "Integer32"
_MsapTlsPlcyDhcpInfoAction_Object = MibTableColumn
msapTlsPlcyDhcpInfoAction = _MsapTlsPlcyDhcpInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 11),
    _MsapTlsPlcyDhcpInfoAction_Type()
)
msapTlsPlcyDhcpInfoAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpInfoAction.setStatus("current")


class _MsapTlsPlcyDhcpCircuitId_Type(Integer32):
    """Custom type msapTlsPlcyDhcpCircuitId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asciiTuple", 1),
          ("none", 0),
          ("vlanAsciiTuple", 2))
    )


_MsapTlsPlcyDhcpCircuitId_Type.__name__ = "Integer32"
_MsapTlsPlcyDhcpCircuitId_Object = MibTableColumn
msapTlsPlcyDhcpCircuitId = _MsapTlsPlcyDhcpCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 12),
    _MsapTlsPlcyDhcpCircuitId_Type()
)
msapTlsPlcyDhcpCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpCircuitId.setStatus("current")


class _MsapTlsPlcyDhcpRemoteId_Type(Integer32):
    """Custom type msapTlsPlcyDhcpRemoteId based on Integer32"""
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
        *(("mac", 2),
          ("none", 1),
          ("remote-id", 3))
    )


_MsapTlsPlcyDhcpRemoteId_Type.__name__ = "Integer32"
_MsapTlsPlcyDhcpRemoteId_Object = MibTableColumn
msapTlsPlcyDhcpRemoteId = _MsapTlsPlcyDhcpRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 13),
    _MsapTlsPlcyDhcpRemoteId_Type()
)
msapTlsPlcyDhcpRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpRemoteId.setStatus("current")
_MsapTlsPlcyDhcpRemoteIdString_Type = TNamedItemOrEmpty
_MsapTlsPlcyDhcpRemoteIdString_Object = MibTableColumn
msapTlsPlcyDhcpRemoteIdString = _MsapTlsPlcyDhcpRemoteIdString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 14),
    _MsapTlsPlcyDhcpRemoteIdString_Type()
)
msapTlsPlcyDhcpRemoteIdString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpRemoteIdString.setStatus("current")


class _MsapTlsPlcyDhcpVendorInclOpts_Type(Bits):
    """Custom type msapTlsPlcyDhcpVendorInclOpts based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("clientMac", 1),
          ("sapId", 3),
          ("serviceId", 2),
          ("systemId", 0))
    )

_MsapTlsPlcyDhcpVendorInclOpts_Type.__name__ = "Bits"
_MsapTlsPlcyDhcpVendorInclOpts_Object = MibTableColumn
msapTlsPlcyDhcpVendorInclOpts = _MsapTlsPlcyDhcpVendorInclOpts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 15),
    _MsapTlsPlcyDhcpVendorInclOpts_Type()
)
msapTlsPlcyDhcpVendorInclOpts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpVendorInclOpts.setStatus("current")
_MsapTlsPlcyDhcpVendorOptStr_Type = TNamedItemOrEmpty
_MsapTlsPlcyDhcpVendorOptStr_Object = MibTableColumn
msapTlsPlcyDhcpVendorOptStr = _MsapTlsPlcyDhcpVendorOptStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 16),
    _MsapTlsPlcyDhcpVendorOptStr_Type()
)
msapTlsPlcyDhcpVendorOptStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyDhcpVendorOptStr.setStatus("current")
_MsapTlsPlcyEgressMcastGroup_Type = TNamedItemOrEmpty
_MsapTlsPlcyEgressMcastGroup_Object = MibTableColumn
msapTlsPlcyEgressMcastGroup = _MsapTlsPlcyEgressMcastGroup_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 17),
    _MsapTlsPlcyEgressMcastGroup_Type()
)
msapTlsPlcyEgressMcastGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyEgressMcastGroup.setStatus("current")
_MsapTlsPlcyIgmpSnpgImportPlcy_Type = TPolicyStatementNameOrEmpty
_MsapTlsPlcyIgmpSnpgImportPlcy_Object = MibTableColumn
msapTlsPlcyIgmpSnpgImportPlcy = _MsapTlsPlcyIgmpSnpgImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 18),
    _MsapTlsPlcyIgmpSnpgImportPlcy_Type()
)
msapTlsPlcyIgmpSnpgImportPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgImportPlcy.setStatus("current")


class _MsapTlsPlcyIgmpSnpgFastLeave_Type(TmnxEnabledDisabled):
    """Custom type msapTlsPlcyIgmpSnpgFastLeave based on TmnxEnabledDisabled"""


_MsapTlsPlcyIgmpSnpgFastLeave_Object = MibTableColumn
msapTlsPlcyIgmpSnpgFastLeave = _MsapTlsPlcyIgmpSnpgFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 19),
    _MsapTlsPlcyIgmpSnpgFastLeave_Type()
)
msapTlsPlcyIgmpSnpgFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgFastLeave.setStatus("current")


class _MsapTlsPlcyIgmpSnpgSendQueries_Type(TmnxEnabledDisabled):
    """Custom type msapTlsPlcyIgmpSnpgSendQueries based on TmnxEnabledDisabled"""


_MsapTlsPlcyIgmpSnpgSendQueries_Object = MibTableColumn
msapTlsPlcyIgmpSnpgSendQueries = _MsapTlsPlcyIgmpSnpgSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 20),
    _MsapTlsPlcyIgmpSnpgSendQueries_Type()
)
msapTlsPlcyIgmpSnpgSendQueries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgSendQueries.setStatus("current")


class _MsapTlsPlcyIgmpSnpgGenQueryIntv_Type(Unsigned32):
    """Custom type msapTlsPlcyIgmpSnpgGenQueryIntv based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_MsapTlsPlcyIgmpSnpgGenQueryIntv_Type.__name__ = "Unsigned32"
_MsapTlsPlcyIgmpSnpgGenQueryIntv_Object = MibTableColumn
msapTlsPlcyIgmpSnpgGenQueryIntv = _MsapTlsPlcyIgmpSnpgGenQueryIntv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 21),
    _MsapTlsPlcyIgmpSnpgGenQueryIntv_Type()
)
msapTlsPlcyIgmpSnpgGenQueryIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgGenQueryIntv.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgGenQueryIntv.setUnits("seconds")


class _MsapTlsPlcyIgmpSnpgQueryRespIntv_Type(Unsigned32):
    """Custom type msapTlsPlcyIgmpSnpgQueryRespIntv based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_MsapTlsPlcyIgmpSnpgQueryRespIntv_Type.__name__ = "Unsigned32"
_MsapTlsPlcyIgmpSnpgQueryRespIntv_Object = MibTableColumn
msapTlsPlcyIgmpSnpgQueryRespIntv = _MsapTlsPlcyIgmpSnpgQueryRespIntv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 22),
    _MsapTlsPlcyIgmpSnpgQueryRespIntv_Type()
)
msapTlsPlcyIgmpSnpgQueryRespIntv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgQueryRespIntv.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgQueryRespIntv.setUnits("seconds")


class _MsapTlsPlcyIgmpSnpgRobustCount_Type(Unsigned32):
    """Custom type msapTlsPlcyIgmpSnpgRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_MsapTlsPlcyIgmpSnpgRobustCount_Type.__name__ = "Unsigned32"
_MsapTlsPlcyIgmpSnpgRobustCount_Object = MibTableColumn
msapTlsPlcyIgmpSnpgRobustCount = _MsapTlsPlcyIgmpSnpgRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 23),
    _MsapTlsPlcyIgmpSnpgRobustCount_Type()
)
msapTlsPlcyIgmpSnpgRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgRobustCount.setStatus("current")


class _MsapTlsPlcyIgmpSnpgLastMembIntvl_Type(Unsigned32):
    """Custom type msapTlsPlcyIgmpSnpgLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_MsapTlsPlcyIgmpSnpgLastMembIntvl_Type.__name__ = "Unsigned32"
_MsapTlsPlcyIgmpSnpgLastMembIntvl_Object = MibTableColumn
msapTlsPlcyIgmpSnpgLastMembIntvl = _MsapTlsPlcyIgmpSnpgLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 24),
    _MsapTlsPlcyIgmpSnpgLastMembIntvl_Type()
)
msapTlsPlcyIgmpSnpgLastMembIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgLastMembIntvl.setUnits("deci-seconds")


class _MsapTlsPlcyIgmpSnpgMaxNbrGrps_Type(Unsigned32):
    """Custom type msapTlsPlcyIgmpSnpgMaxNbrGrps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MsapTlsPlcyIgmpSnpgMaxNbrGrps_Type.__name__ = "Unsigned32"
_MsapTlsPlcyIgmpSnpgMaxNbrGrps_Object = MibTableColumn
msapTlsPlcyIgmpSnpgMaxNbrGrps = _MsapTlsPlcyIgmpSnpgMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 25),
    _MsapTlsPlcyIgmpSnpgMaxNbrGrps_Type()
)
msapTlsPlcyIgmpSnpgMaxNbrGrps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMaxNbrGrps.setStatus("current")


class _MsapTlsPlcyIgmpSnpgMvrFromVplsId_Type(TmnxServId):
    """Custom type msapTlsPlcyIgmpSnpgMvrFromVplsId based on TmnxServId"""
    defaultValue = 0


_MsapTlsPlcyIgmpSnpgMvrFromVplsId_Object = MibTableColumn
msapTlsPlcyIgmpSnpgMvrFromVplsId = _MsapTlsPlcyIgmpSnpgMvrFromVplsId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 26),
    _MsapTlsPlcyIgmpSnpgMvrFromVplsId_Type()
)
msapTlsPlcyIgmpSnpgMvrFromVplsId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMvrFromVplsId.setStatus("current")


class _MsapTlsPlcyIgmpSnpgVersion_Type(TmnxIgmpVersion):
    """Custom type msapTlsPlcyIgmpSnpgVersion based on TmnxIgmpVersion"""


_MsapTlsPlcyIgmpSnpgVersion_Object = MibTableColumn
msapTlsPlcyIgmpSnpgVersion = _MsapTlsPlcyIgmpSnpgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 27),
    _MsapTlsPlcyIgmpSnpgVersion_Type()
)
msapTlsPlcyIgmpSnpgVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgVersion.setStatus("current")
_MsapTlsPlcyIgmpSnpgMcacPlcyName_Type = TPolicyStatementNameOrEmpty
_MsapTlsPlcyIgmpSnpgMcacPlcyName_Object = MibTableColumn
msapTlsPlcyIgmpSnpgMcacPlcyName = _MsapTlsPlcyIgmpSnpgMcacPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 28),
    _MsapTlsPlcyIgmpSnpgMcacPlcyName_Type()
)
msapTlsPlcyIgmpSnpgMcacPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMcacPlcyName.setStatus("current")


class _MsapTlsPlcyIgmpSnpgMcacUncnstBW_Type(Integer32):
    """Custom type msapTlsPlcyIgmpSnpgMcacUncnstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MsapTlsPlcyIgmpSnpgMcacUncnstBW_Type.__name__ = "Integer32"
_MsapTlsPlcyIgmpSnpgMcacUncnstBW_Object = MibTableColumn
msapTlsPlcyIgmpSnpgMcacUncnstBW = _MsapTlsPlcyIgmpSnpgMcacUncnstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 29),
    _MsapTlsPlcyIgmpSnpgMcacUncnstBW_Type()
)
msapTlsPlcyIgmpSnpgMcacUncnstBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMcacUncnstBW.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMcacUncnstBW.setUnits("kbps")


class _MsapTlsPlcyIgmpSnpgMcacPrRsvMnBW_Type(Integer32):
    """Custom type msapTlsPlcyIgmpSnpgMcacPrRsvMnBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_MsapTlsPlcyIgmpSnpgMcacPrRsvMnBW_Type.__name__ = "Integer32"
_MsapTlsPlcyIgmpSnpgMcacPrRsvMnBW_Object = MibTableColumn
msapTlsPlcyIgmpSnpgMcacPrRsvMnBW = _MsapTlsPlcyIgmpSnpgMcacPrRsvMnBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 45, 1, 30),
    _MsapTlsPlcyIgmpSnpgMcacPrRsvMnBW_Type()
)
msapTlsPlcyIgmpSnpgMcacPrRsvMnBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMcacPrRsvMnBW.setStatus("current")
if mibBuilder.loadTexts:
    msapTlsPlcyIgmpSnpgMcacPrRsvMnBW.setUnits("kbps")
_MsapIgmpSnpgMcacLevelTable_Object = MibTable
msapIgmpSnpgMcacLevelTable = _MsapIgmpSnpgMcacLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46)
)
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelTable.setStatus("current")
_MsapIgmpSnpgMcacLevelEntry_Object = MibTableRow
msapIgmpSnpgMcacLevelEntry = _MsapIgmpSnpgMcacLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46, 1)
)
msapIgmpSnpgMcacLevelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLevelId"),
)
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelEntry.setStatus("current")


class _MsapIgmpSnpgMcacLevelId_Type(Unsigned32):
    """Custom type msapIgmpSnpgMcacLevelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MsapIgmpSnpgMcacLevelId_Type.__name__ = "Unsigned32"
_MsapIgmpSnpgMcacLevelId_Object = MibTableColumn
msapIgmpSnpgMcacLevelId = _MsapIgmpSnpgMcacLevelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46, 1, 1),
    _MsapIgmpSnpgMcacLevelId_Type()
)
msapIgmpSnpgMcacLevelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelId.setStatus("current")
_MsapIgmpSnpgMcacLevelRowStatus_Type = RowStatus
_MsapIgmpSnpgMcacLevelRowStatus_Object = MibTableColumn
msapIgmpSnpgMcacLevelRowStatus = _MsapIgmpSnpgMcacLevelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46, 1, 2),
    _MsapIgmpSnpgMcacLevelRowStatus_Type()
)
msapIgmpSnpgMcacLevelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelRowStatus.setStatus("current")
_MsapIgmpSnpgMcacLevelLastChanged_Type = TimeStamp
_MsapIgmpSnpgMcacLevelLastChanged_Object = MibTableColumn
msapIgmpSnpgMcacLevelLastChanged = _MsapIgmpSnpgMcacLevelLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46, 1, 3),
    _MsapIgmpSnpgMcacLevelLastChanged_Type()
)
msapIgmpSnpgMcacLevelLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelLastChanged.setStatus("current")


class _MsapIgmpSnpgMcacLevelBW_Type(Unsigned32):
    """Custom type msapIgmpSnpgMcacLevelBW based on Unsigned32"""
    defaultValue = 1


_MsapIgmpSnpgMcacLevelBW_Object = MibTableColumn
msapIgmpSnpgMcacLevelBW = _MsapIgmpSnpgMcacLevelBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 46, 1, 4),
    _MsapIgmpSnpgMcacLevelBW_Type()
)
msapIgmpSnpgMcacLevelBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelBW.setStatus("current")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLevelBW.setUnits("kbps")
_MsapIgmpSnpgMcacLagTable_Object = MibTable
msapIgmpSnpgMcacLagTable = _MsapIgmpSnpgMcacLagTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47)
)
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagTable.setStatus("current")
_MsapIgmpSnpgMcacLagEntry_Object = MibTableRow
msapIgmpSnpgMcacLagEntry = _MsapIgmpSnpgMcacLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47, 1)
)
msapIgmpSnpgMcacLagEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyName"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLagPortsDown"),
)
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagEntry.setStatus("current")


class _MsapIgmpSnpgMcacLagPortsDown_Type(Unsigned32):
    """Custom type msapIgmpSnpgMcacLagPortsDown based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MsapIgmpSnpgMcacLagPortsDown_Type.__name__ = "Unsigned32"
_MsapIgmpSnpgMcacLagPortsDown_Object = MibTableColumn
msapIgmpSnpgMcacLagPortsDown = _MsapIgmpSnpgMcacLagPortsDown_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47, 1, 1),
    _MsapIgmpSnpgMcacLagPortsDown_Type()
)
msapIgmpSnpgMcacLagPortsDown.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagPortsDown.setStatus("current")
_MsapIgmpSnpgMcacLagRowStatus_Type = RowStatus
_MsapIgmpSnpgMcacLagRowStatus_Object = MibTableColumn
msapIgmpSnpgMcacLagRowStatus = _MsapIgmpSnpgMcacLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47, 1, 2),
    _MsapIgmpSnpgMcacLagRowStatus_Type()
)
msapIgmpSnpgMcacLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagRowStatus.setStatus("current")
_MsapIgmpSnpgMcacLagLastChanged_Type = TimeStamp
_MsapIgmpSnpgMcacLagLastChanged_Object = MibTableColumn
msapIgmpSnpgMcacLagLastChanged = _MsapIgmpSnpgMcacLagLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47, 1, 3),
    _MsapIgmpSnpgMcacLagLastChanged_Type()
)
msapIgmpSnpgMcacLagLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagLastChanged.setStatus("current")


class _MsapIgmpSnpgMcacLagLevel_Type(Unsigned32):
    """Custom type msapIgmpSnpgMcacLagLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_MsapIgmpSnpgMcacLagLevel_Type.__name__ = "Unsigned32"
_MsapIgmpSnpgMcacLagLevel_Object = MibTableColumn
msapIgmpSnpgMcacLagLevel = _MsapIgmpSnpgMcacLagLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 47, 1, 4),
    _MsapIgmpSnpgMcacLagLevel_Type()
)
msapIgmpSnpgMcacLagLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagLevel.setStatus("current")
_MsapInfoTable_Object = MibTable
msapInfoTable = _MsapInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48)
)
if mibBuilder.loadTexts:
    msapInfoTable.setStatus("current")
_MsapInfoEntry_Object = MibTableRow
msapInfoEntry = _MsapInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48, 1)
)
msapInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
)
if mibBuilder.loadTexts:
    msapInfoEntry.setStatus("current")
_MsapInfoCreationSapPortEncapVal_Type = TmnxEncapVal
_MsapInfoCreationSapPortEncapVal_Object = MibTableColumn
msapInfoCreationSapPortEncapVal = _MsapInfoCreationSapPortEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48, 1, 1),
    _MsapInfoCreationSapPortEncapVal_Type()
)
msapInfoCreationSapPortEncapVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapInfoCreationSapPortEncapVal.setStatus("current")
_MsapInfoCreationPlcyName_Type = TNamedItem
_MsapInfoCreationPlcyName_Object = MibTableColumn
msapInfoCreationPlcyName = _MsapInfoCreationPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48, 1, 2),
    _MsapInfoCreationPlcyName_Type()
)
msapInfoCreationPlcyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapInfoCreationPlcyName.setStatus("current")


class _MsapInfoReEvalPolicy_Type(TmnxActionType):
    """Custom type msapInfoReEvalPolicy based on TmnxActionType"""


_MsapInfoReEvalPolicy_Object = MibTableColumn
msapInfoReEvalPolicy = _MsapInfoReEvalPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48, 1, 3),
    _MsapInfoReEvalPolicy_Type()
)
msapInfoReEvalPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msapInfoReEvalPolicy.setStatus("current")
_MsapInfoLastChanged_Type = TimeStamp
_MsapInfoLastChanged_Object = MibTableColumn
msapInfoLastChanged = _MsapInfoLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 48, 1, 4),
    _MsapInfoLastChanged_Type()
)
msapInfoLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapInfoLastChanged.setStatus("current")
_MsapCaptureSapStatsTable_Object = MibTable
msapCaptureSapStatsTable = _MsapCaptureSapStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49)
)
if mibBuilder.loadTexts:
    msapCaptureSapStatsTable.setStatus("current")
_MsapCaptureSapStatsEntry_Object = MibTableRow
msapCaptureSapStatsEntry = _MsapCaptureSapStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49, 1)
)
msapCaptureSapStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "msapCaptureSapStatsTriggerType"),
)
if mibBuilder.loadTexts:
    msapCaptureSapStatsEntry.setStatus("current")


class _MsapCaptureSapStatsTriggerType_Type(Integer32):
    """Custom type msapCaptureSapStatsTriggerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("pppoe", 2))
    )


_MsapCaptureSapStatsTriggerType_Type.__name__ = "Integer32"
_MsapCaptureSapStatsTriggerType_Object = MibTableColumn
msapCaptureSapStatsTriggerType = _MsapCaptureSapStatsTriggerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49, 1, 1),
    _MsapCaptureSapStatsTriggerType_Type()
)
msapCaptureSapStatsTriggerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msapCaptureSapStatsTriggerType.setStatus("current")
_MsapCaptureSapStatsPktsRecvd_Type = Counter32
_MsapCaptureSapStatsPktsRecvd_Object = MibTableColumn
msapCaptureSapStatsPktsRecvd = _MsapCaptureSapStatsPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49, 1, 2),
    _MsapCaptureSapStatsPktsRecvd_Type()
)
msapCaptureSapStatsPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapCaptureSapStatsPktsRecvd.setStatus("current")
_MsapCaptureSapStatsPktsRedirect_Type = Counter32
_MsapCaptureSapStatsPktsRedirect_Object = MibTableColumn
msapCaptureSapStatsPktsRedirect = _MsapCaptureSapStatsPktsRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49, 1, 3),
    _MsapCaptureSapStatsPktsRedirect_Type()
)
msapCaptureSapStatsPktsRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapCaptureSapStatsPktsRedirect.setStatus("current")
_MsapCaptureSapStatsPktsDropped_Type = Counter32
_MsapCaptureSapStatsPktsDropped_Object = MibTableColumn
msapCaptureSapStatsPktsDropped = _MsapCaptureSapStatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 49, 1, 4),
    _MsapCaptureSapStatsPktsDropped_Type()
)
msapCaptureSapStatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapCaptureSapStatsPktsDropped.setStatus("current")
_SapTlsMrpTable_Object = MibTable
sapTlsMrpTable = _SapTlsMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50)
)
if mibBuilder.loadTexts:
    sapTlsMrpTable.setStatus("current")
_SapTlsMrpEntry_Object = MibTableRow
sapTlsMrpEntry = _SapTlsMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1)
)
if mibBuilder.loadTexts:
    sapTlsMrpEntry.setStatus("current")
_SapTlsMrpRxPdus_Type = Counter32
_SapTlsMrpRxPdus_Object = MibTableColumn
sapTlsMrpRxPdus = _SapTlsMrpRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 1),
    _SapTlsMrpRxPdus_Type()
)
sapTlsMrpRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxPdus.setStatus("current")
_SapTlsMrpDroppedPdus_Type = Counter32
_SapTlsMrpDroppedPdus_Object = MibTableColumn
sapTlsMrpDroppedPdus = _SapTlsMrpDroppedPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 2),
    _SapTlsMrpDroppedPdus_Type()
)
sapTlsMrpDroppedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpDroppedPdus.setStatus("current")
_SapTlsMrpTxPdus_Type = Counter32
_SapTlsMrpTxPdus_Object = MibTableColumn
sapTlsMrpTxPdus = _SapTlsMrpTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 3),
    _SapTlsMrpTxPdus_Type()
)
sapTlsMrpTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxPdus.setStatus("current")
_SapTlsMrpRxNewEvent_Type = Counter32
_SapTlsMrpRxNewEvent_Object = MibTableColumn
sapTlsMrpRxNewEvent = _SapTlsMrpRxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 4),
    _SapTlsMrpRxNewEvent_Type()
)
sapTlsMrpRxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxNewEvent.setStatus("current")
_SapTlsMrpRxJoinInEvent_Type = Counter32
_SapTlsMrpRxJoinInEvent_Object = MibTableColumn
sapTlsMrpRxJoinInEvent = _SapTlsMrpRxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 5),
    _SapTlsMrpRxJoinInEvent_Type()
)
sapTlsMrpRxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxJoinInEvent.setStatus("current")
_SapTlsMrpRxInEvent_Type = Counter32
_SapTlsMrpRxInEvent_Object = MibTableColumn
sapTlsMrpRxInEvent = _SapTlsMrpRxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 6),
    _SapTlsMrpRxInEvent_Type()
)
sapTlsMrpRxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxInEvent.setStatus("current")
_SapTlsMrpRxJoinEmptyEvent_Type = Counter32
_SapTlsMrpRxJoinEmptyEvent_Object = MibTableColumn
sapTlsMrpRxJoinEmptyEvent = _SapTlsMrpRxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 7),
    _SapTlsMrpRxJoinEmptyEvent_Type()
)
sapTlsMrpRxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxJoinEmptyEvent.setStatus("current")
_SapTlsMrpRxEmptyEvent_Type = Counter32
_SapTlsMrpRxEmptyEvent_Object = MibTableColumn
sapTlsMrpRxEmptyEvent = _SapTlsMrpRxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 8),
    _SapTlsMrpRxEmptyEvent_Type()
)
sapTlsMrpRxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxEmptyEvent.setStatus("current")
_SapTlsMrpRxLeaveEvent_Type = Counter32
_SapTlsMrpRxLeaveEvent_Object = MibTableColumn
sapTlsMrpRxLeaveEvent = _SapTlsMrpRxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 9),
    _SapTlsMrpRxLeaveEvent_Type()
)
sapTlsMrpRxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpRxLeaveEvent.setStatus("current")
_SapTlsMrpTxNewEvent_Type = Counter32
_SapTlsMrpTxNewEvent_Object = MibTableColumn
sapTlsMrpTxNewEvent = _SapTlsMrpTxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 10),
    _SapTlsMrpTxNewEvent_Type()
)
sapTlsMrpTxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxNewEvent.setStatus("current")
_SapTlsMrpTxJoinInEvent_Type = Counter32
_SapTlsMrpTxJoinInEvent_Object = MibTableColumn
sapTlsMrpTxJoinInEvent = _SapTlsMrpTxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 11),
    _SapTlsMrpTxJoinInEvent_Type()
)
sapTlsMrpTxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxJoinInEvent.setStatus("current")
_SapTlsMrpTxInEvent_Type = Counter32
_SapTlsMrpTxInEvent_Object = MibTableColumn
sapTlsMrpTxInEvent = _SapTlsMrpTxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 12),
    _SapTlsMrpTxInEvent_Type()
)
sapTlsMrpTxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxInEvent.setStatus("current")
_SapTlsMrpTxJoinEmptyEvent_Type = Counter32
_SapTlsMrpTxJoinEmptyEvent_Object = MibTableColumn
sapTlsMrpTxJoinEmptyEvent = _SapTlsMrpTxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 13),
    _SapTlsMrpTxJoinEmptyEvent_Type()
)
sapTlsMrpTxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxJoinEmptyEvent.setStatus("current")
_SapTlsMrpTxEmptyEvent_Type = Counter32
_SapTlsMrpTxEmptyEvent_Object = MibTableColumn
sapTlsMrpTxEmptyEvent = _SapTlsMrpTxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 14),
    _SapTlsMrpTxEmptyEvent_Type()
)
sapTlsMrpTxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxEmptyEvent.setStatus("current")
_SapTlsMrpTxLeaveEvent_Type = Counter32
_SapTlsMrpTxLeaveEvent_Object = MibTableColumn
sapTlsMrpTxLeaveEvent = _SapTlsMrpTxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 50, 1, 15),
    _SapTlsMrpTxLeaveEvent_Type()
)
sapTlsMrpTxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMrpTxLeaveEvent.setStatus("current")
_SapTlsMmrpTable_Object = MibTable
sapTlsMmrpTable = _SapTlsMmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 51)
)
if mibBuilder.loadTexts:
    sapTlsMmrpTable.setStatus("current")
_SapTlsMmrpEntry_Object = MibTableRow
sapTlsMmrpEntry = _SapTlsMmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 51, 1)
)
sapTlsMmrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
    (0, "ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMmrpMacAddr"),
)
if mibBuilder.loadTexts:
    sapTlsMmrpEntry.setStatus("current")
_SapTlsMmrpMacAddr_Type = MacAddress
_SapTlsMmrpMacAddr_Object = MibTableColumn
sapTlsMmrpMacAddr = _SapTlsMmrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 51, 1, 1),
    _SapTlsMmrpMacAddr_Type()
)
sapTlsMmrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sapTlsMmrpMacAddr.setStatus("current")
_SapTlsMmrpDeclared_Type = TruthValue
_SapTlsMmrpDeclared_Object = MibTableColumn
sapTlsMmrpDeclared = _SapTlsMmrpDeclared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 51, 1, 2),
    _SapTlsMmrpDeclared_Type()
)
sapTlsMmrpDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMmrpDeclared.setStatus("current")
_SapTlsMmrpRegistered_Type = TruthValue
_SapTlsMmrpRegistered_Object = MibTableColumn
sapTlsMmrpRegistered = _SapTlsMmrpRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 51, 1, 3),
    _SapTlsMmrpRegistered_Type()
)
sapTlsMmrpRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sapTlsMmrpRegistered.setStatus("current")
_MsapPlcyTblLastChgd_Type = TimeStamp
_MsapPlcyTblLastChgd_Object = MibScalar
msapPlcyTblLastChgd = _MsapPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 59),
    _MsapPlcyTblLastChgd_Type()
)
msapPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapPlcyTblLastChgd.setStatus("current")
_MsapTlsPlcyTblLastChgd_Type = TimeStamp
_MsapTlsPlcyTblLastChgd_Object = MibScalar
msapTlsPlcyTblLastChgd = _MsapTlsPlcyTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 60),
    _MsapTlsPlcyTblLastChgd_Type()
)
msapTlsPlcyTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapTlsPlcyTblLastChgd.setStatus("current")
_MsapIgmpSnpgMcacLvlTblLastChgd_Type = TimeStamp
_MsapIgmpSnpgMcacLvlTblLastChgd_Object = MibScalar
msapIgmpSnpgMcacLvlTblLastChgd = _MsapIgmpSnpgMcacLvlTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 61),
    _MsapIgmpSnpgMcacLvlTblLastChgd_Type()
)
msapIgmpSnpgMcacLvlTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLvlTblLastChgd.setStatus("current")
_MsapIgmpSnpgMcacLagTblLastChgd_Type = TimeStamp
_MsapIgmpSnpgMcacLagTblLastChgd_Object = MibScalar
msapIgmpSnpgMcacLagTblLastChgd = _MsapIgmpSnpgMcacLagTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 62),
    _MsapIgmpSnpgMcacLagTblLastChgd_Type()
)
msapIgmpSnpgMcacLagTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapIgmpSnpgMcacLagTblLastChgd.setStatus("current")
_MsapInfoTblLastChgd_Type = TimeStamp
_MsapInfoTblLastChgd_Object = MibScalar
msapInfoTblLastChgd = _MsapInfoTblLastChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 63),
    _MsapInfoTblLastChgd_Type()
)
msapInfoTblLastChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msapInfoTblLastChgd.setStatus("current")
_TmnxSapNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSapNotifyObjs = _TmnxSapNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 100)
)
_SapNotifyPortId_Type = TmnxPortID
_SapNotifyPortId_Object = MibScalar
sapNotifyPortId = _SapNotifyPortId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 100, 1),
    _SapNotifyPortId_Type()
)
sapNotifyPortId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sapNotifyPortId.setStatus("current")
_MsapStatus_Type = ConfigStatus
_MsapStatus_Object = MibScalar
msapStatus = _MsapStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 100, 2),
    _MsapStatus_Type()
)
msapStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    msapStatus.setStatus("current")
_SvcManagedSapCreationError_Type = DisplayString
_SvcManagedSapCreationError_Object = MibScalar
svcManagedSapCreationError = _SvcManagedSapCreationError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 3, 100, 3),
    _SvcManagedSapCreationError_Type()
)
svcManagedSapCreationError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    svcManagedSapCreationError.setStatus("current")
_SapTrapsPrefix_ObjectIdentity = ObjectIdentity
sapTrapsPrefix = _SapTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3)
)
_SapTraps_ObjectIdentity = ObjectIdentity
sapTraps = _SapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0)
)
msapPlcyEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-SAP-MIB",
     "msapTlsPlcyEntry")
)
msapTlsPlcyEntry.setIndexNames(*msapPlcyEntry.getIndexNames())
sapTlsInfoEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-SAP-MIB",
     "sapTlsMrpEntry")
)
sapTlsMrpEntry.setIndexNames(*sapTlsInfoEntry.getIndexNames())

# Managed Objects groups

tmnxSapV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 100)
)
tmnxSapV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapNumEntries"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapType"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDescription"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressVlanTranslationId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapMirrorStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIesIfIndex"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCollectAcctStats"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAccountingPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCustMultSvcSite"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressQosSchedulerPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressQosSchedulerPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSplitHorizonGrp"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressSharedQueuePolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressMatchQinQDot1PBits"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapOperFlags"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapLastStatusChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAntiSpoofing"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTodSuite"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngUseMultipointShared"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressQinQMarkTopOnly"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressAggRateLimit"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEndPoint"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressVlanTranslation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubType"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCpmProtPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCpmProtMonitorMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressFrameBasedAccounting"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEthernetLLFAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEthernetLLFOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAntiSpoofIpAddress"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAntiSpoofMacAddress"))
)
if mibBuilder.loadTexts:
    tmnxSapV6v0Group.setStatus("current")

tmnxSapTlsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 101)
)
tmnxSapTlsV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpPriority"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpPortNum"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpPathCost"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpRapidStart"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpBpduEncap"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpDesignatedBridge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpDesignatedPort"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpForwardTransitions"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInBadBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOutConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOutTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOperBpduEncap"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacAddressLimit"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsNumMacAddresses"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsNumStaticMacAddresses"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacLearning"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacAgeing"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOperEdge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpAdminPointToPoint"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpPortRole"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpAutoEdge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOperProtocol"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOutRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsLimitMacMove"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacPinning"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDiscardUnknownSource"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsPruneState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMgmtService"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMgmtPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMgmtEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsArpReplyAgent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpException"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsAuthenticationPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptTermination"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsBpduTranslation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpRootGuard"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInsideRegion"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsEgressMcastGroup"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpInMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOutMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsRestProtSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsRestProtSrcMacAction"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsRestUnprotDstMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpRxdDesigBridge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpRootGuardViolation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsShcvAction"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsShcvSrcIp"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsShcvSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsShcvInterval"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMvplsMgmtMsti"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacMoveNextUpTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacMoveRateExcdLeft"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptForceBoundary"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsLimitMacMoveLevel"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsBpduTransOper"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDefMsapPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptProtocols"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptForceProtocols"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpMsapTrigger"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpProxyLeaseTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpRemoteId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpJoinTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpLeaveTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpLeaveAllTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpPeriodicTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpPeriodicEnabled"))
)
if mibBuilder.loadTexts:
    tmnxSapTlsV6v0Group.setStatus("current")

tmnxSapAtmV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 102)
)
tmnxSapAtmV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmEncapsulation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmIngressTrafficDescIndex"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmEgressTrafficDescIndex"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmOamAlarmCellHandling"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmOamTerminate"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAtmOamPeriodicLoopback"))
)
if mibBuilder.loadTexts:
    tmnxSapAtmV6v0Group.setStatus("current")

tmnxSapBaseV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 103)
)
tmnxSapBaseV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipDroppedPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipDroppedOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipDroppedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipDroppedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipDroppedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipDroppedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressQchipForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipDroppedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipDroppedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipDroppedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipDroppedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsEgressQchipForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedUncoloredPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsIngressPchipOfferedUncoloredOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsAuthenticationPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsAuthenticationPktsSuccess"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapBaseStatsLastClearedTime"))
)
if mibBuilder.loadTexts:
    tmnxSapBaseV6v0Group.setStatus("current")

tmnxSapQosV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 104)
)
tmnxSapQosV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsOfferedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsDroppedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsOfferedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsDroppedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsOfferedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsDroppedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsOfferedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsDroppedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsUncoloredPacketsOffered"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQueueStatsUncoloredOctetsOffered"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsDroppedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsDroppedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsDroppedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQueueStatsDroppedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSchedStatsForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSchedStatsForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSchedCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSchedStatsForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSchedStatsForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSchedCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQCBS"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQMBS"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQPIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosQAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQCBS"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQMBS"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQHiPrioOnly"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQCIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQPIRAdaptation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQAdminPIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQAdminCIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosQAvgOverhead"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSPIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSCIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngQosSSummedCIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSOverrideFlags"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSPIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSCIR"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrQosSSummedCIR"))
)
if mibBuilder.loadTexts:
    tmnxSapQosV6v0Group.setStatus("current")

tmnxSapStaticHostV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 105)
)
tmnxSapStaticHostV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostSubscrIdent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostSubProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostSlaProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostShcvOperState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostShcvChecks"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostShcvReplies"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostShcvReplyTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostDynMacAddress"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostRetailerSvcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostRetailerIf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostFwdingState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostAncpString"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostSubIdIsSapId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostIntermediateDestId"))
)
if mibBuilder.loadTexts:
    tmnxSapStaticHostV6v0Group.setStatus("current")

tmnxSapDhcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 106)
)
tmnxSapDhcpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpAdminState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpDescription"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpSnoop"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpOperLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpInfoAction"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpCircuitId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpRemoteIdString"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpProxyAdminState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpProxyServerAddr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpProxyLTRadiusOverride"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpVendorIncludeOptions"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpVendorOptionString"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsClntSnoopdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsSrvrSnoopdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsClntForwdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsSrvrForwdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsClntDropdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsSrvrDropdPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsClntProxRadPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsClntProxLSPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsGenReleasePckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpStatsGenForceRenPckts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDhcpOperLeasePopulate"))
)
if mibBuilder.loadTexts:
    tmnxSapDhcpV6v0Group.setStatus("current")

tmnxSapPortIdV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 107)
)
tmnxSapPortIdV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngQosSchedFwdPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngQosSchedFwdOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdIngQosSchedCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrQosSchedFwdPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrQosSchedFwdOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortIdEgrQosSchedCustId"))
)
if mibBuilder.loadTexts:
    tmnxSapPortIdV6v0Group.setStatus("current")

tmnxSapSubMgmtV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 108)
)
tmnxSapSubMgmtV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtDefSubProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtDefSlaProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtSubIdentPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtSubscriberLimit"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtProfiledTrafficOnly"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtNonSubTrafficSubIdent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtNonSubTrafficSubProf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtNonSubTrafficSlaProf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtMacDaHashing"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtDefSubIdent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtDefSubIdentString"))
)
if mibBuilder.loadTexts:
    tmnxSapSubMgmtV6v0Group.setStatus("current")

tmnxSapMstiV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 109)
)
tmnxSapMstiV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiPriority"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiPathCost"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiPortRole"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiPortState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiDesignatedBridge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMstiDesignatedPort"))
)
if mibBuilder.loadTexts:
    tmnxSapMstiV6v0Group.setStatus("current")

tmnxSapIppipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 110)
)
tmnxSapIppipeV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeCeInetAddress"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeCeInetAddressType"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeMacRefreshInterval"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeMacAddress"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeArpedMacAddress"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIpipeArpedMacAddressTimeout"))
)
if mibBuilder.loadTexts:
    tmnxSapIppipeV6v0Group.setStatus("current")

tmnxSapPolicyV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 111)
)
tmnxSapPolicyV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentIngressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentIngressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentIngressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentIngressQosSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentEgressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentEgressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentEgressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentEgressQosSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedIngressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedIngressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedIngressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedIngressQosSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedEgressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedEgressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedEgressQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedEgressQosSchedPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyDroppedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyDroppedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyDroppedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyDroppedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyDroppedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyDroppedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyDroppedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyDroppedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsOfferedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsDroppedHiPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsOfferedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsDroppedLoPrioPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsOfferedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsDroppedHiPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsOfferedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsDroppedLoPrioOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsUncoloredPacketsOffered"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIgQosPlcyQueueStatsUncoloredOctetsOffered"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsForwardedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsDroppedInProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsForwardedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsDroppedOutProfPackets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsForwardedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsDroppedInProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsForwardedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueStatsDroppedOutProfOctets"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgQosPlcyQueueCustId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngSchedPlcyStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngSchedPlcyStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrSchedPlcyStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrSchedPlcyStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrSchedPlcyPortStatsPort"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngSchedPlcyPortStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngSchedPlcyPortStatsFwdOct"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngSchedPlcyPortStatsPort"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrSchedPlcyPortStatsFwdPkt"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgrSchedPlcyPortStatsFwdOct"))
)
if mibBuilder.loadTexts:
    tmnxSapPolicyV6v0Group.setStatus("current")

tmnxSapCemV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 112)
)
tmnxSapCemV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemEndpointType"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemBitrate"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemCasTrunkFraming"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemPayloadSize"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemJitterBuffer"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemUseRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemDifferential"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemReportAlarm"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemReportAlarmStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemLocalEcid"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemRemoteMacAddr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemRemoteEcid"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsIngressForwardedPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsIngressDroppedPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressForwardedPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressDroppedPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressMissingPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressPktsReOrder"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressJtrBfrUnderruns"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressJtrBfrOverruns"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressMisOrderDropped"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressMalformedPkts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressLBitDropped"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressMultipleDropped"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressESs"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressSESs"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressUASs"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressFailureCounts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressUnderrunCounts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemStatsEgressOverrunCounts"))
)
if mibBuilder.loadTexts:
    tmnxSapCemV6v0Group.setStatus("current")

tmnxSapL2ptV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 113)
)
tmnxSapL2ptV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsLastClearedTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsStpTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPvstTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherL2ptBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherL2ptBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherInvalidBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsOtherInvalidBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapCdpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapCdpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapVtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapVtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapDtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapDtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPagpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapPagpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapUdldBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsL2ptEncapUdldBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsCdpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsCdpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsVtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsVtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsDtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsDtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPagpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsPagpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsUdldBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsL2ptStatsUdldBpdusTx"))
)
if mibBuilder.loadTexts:
    tmnxSapL2ptV6v0Group.setStatus("current")

tmnxSapMsapV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 114)
)
tmnxSapMsapV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyDescription"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyCpmProtPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyCpmProtMonitorMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtDefSubId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtDefSubIdStr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtDefSubProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtDefSlaProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtSubIdPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtSubscriberLimit"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtProfiledTrafOnly"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtNonSubTrafSubId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtNonSubTrafSubProf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtNonSubTrafSlaProf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyAssociatedMsaps"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcySplitHorizonGrp"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyArpReplyAgent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcySubMgmtMacDaHashing"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpPrxyAdminState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpPrxyServAddr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpPrxyServAddrType"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpPrxyLTRadOverride"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpInfoAction"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpCircuitId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpRemoteId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpRemoteIdString"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpVendorInclOpts"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpVendorOptStr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyDhcpPrxyLeaseTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyEgressMcastGroup"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgImportPlcy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgFastLeave"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgSendQueries"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgGenQueryIntv"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgQueryRespIntv"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgRobustCount"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgLastMembIntvl"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgMaxNbrGrps"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgMvrFromVplsId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgVersion"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgMcacPlcyName"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgMcacPrRsvMnBW"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyIgmpSnpgMcacUncnstBW"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLevelRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLevelLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLevelBW"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLagRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLagLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLagLevel"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapInfoCreationSapPortEncapVal"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapInfoCreationPlcyName"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapInfoReEvalPolicy"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapInfoLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapCaptureSapStatsPktsRecvd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapCaptureSapStatsPktsRedirect"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapCaptureSapStatsPktsDropped"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcyTblLastChgd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapTlsPlcyTblLastChgd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLvlTblLastChgd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapIgmpSnpgMcacLagTblLastChgd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapInfoTblLastChgd"))
)
if mibBuilder.loadTexts:
    tmnxSapMsapV6v0Group.setStatus("current")

tmnxSapMrpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 115)
)
tmnxSapMrpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxPdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpDroppedPdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxPdus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxNewEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxJoinInEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxInEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxJoinEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpRxLeaveEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxNewEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxJoinInEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxInEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxJoinEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMrpTxLeaveEvent"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMmrpDeclared"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMmrpRegistered"))
)
if mibBuilder.loadTexts:
    tmnxSapMrpV6v0Group.setStatus("current")

tmnxTlsMsapPppoeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 117)
)
tmnxTlsMsapPppoeV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsPppoeMsapTrigger")
)
if mibBuilder.loadTexts:
    tmnxTlsMsapPppoeV6v0Group.setStatus("current")

tmnxSapIpV6FilterV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 118)
)
tmnxSapIpV6FilterV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIngressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEgressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentIngressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCurrentEgressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedIngressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapIntendedEgressIpv6FilterId"))
)
if mibBuilder.loadTexts:
    tmnxSapIpV6FilterV6v0Group.setStatus("current")

tmnxSapBsxV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 119)
)
tmnxSapBsxV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostAppProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtDefAppProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapSubMgmtNonSubTrafficAppProf"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtDefAppProfile"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapPlcySubMgmtNonSubTrafAppProf"))
)
if mibBuilder.loadTexts:
    tmnxSapBsxV6v0Group.setStatus("current")

tmnxSapNotificationObjV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 200)
)
tmnxSapNotificationObjV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "svcManagedSapCreationError"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapStatus"))
)
if mibBuilder.loadTexts:
    tmnxSapNotificationObjV6v0Group.setStatus("current")

tmnxSapObsoletedV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 300)
)
tmnxSapObsoletedV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpSnooping"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLseStateRemainLseTime"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLseStateOption82"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDhcpLseStatePersistKey"))
)
if mibBuilder.loadTexts:
    tmnxSapObsoletedV6v0Group.setStatus("current")


# Notification objects

sapCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 1)
)
sapCreated.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    sapCreated.setStatus(
        "obsolete"
    )

sapDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 2)
)
sapDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    sapDeleted.setStatus(
        "obsolete"
    )

sapStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 3)
)
sapStatusChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapOperFlags"))
)
if mibBuilder.loadTexts:
    sapStatusChanged.setStatus(
        "current"
    )

sapTlsMacAddrLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 4)
)
sapTlsMacAddrLimitAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    sapTlsMacAddrLimitAlarmRaised.setStatus(
        "current"
    )

sapTlsMacAddrLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 5)
)
sapTlsMacAddrLimitAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    sapTlsMacAddrLimitAlarmCleared.setStatus(
        "current"
    )

sapTlsDHCPLseStEntriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 6)
)
sapTlsDHCPLseStEntriesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDHCPClientLease"))
)
if mibBuilder.loadTexts:
    sapTlsDHCPLseStEntriesExceeded.setStatus(
        "obsolete"
    )

sapTlsDHCPLeaseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 7)
)
sapTlsDHCPLeaseStateOverride.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpLseStateOldChAddr"))
)
if mibBuilder.loadTexts:
    sapTlsDHCPLeaseStateOverride.setStatus(
        "obsolete"
    )

sapTlsDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 8)
)
sapTlsDHCPSuspiciousPcktRcvd.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sapTlsDHCPSuspiciousPcktRcvd.setStatus(
        "obsolete"
    )

sapDHCPLeaseEntriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 9)
)
sapDHCPLeaseEntriesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    sapDHCPLeaseEntriesExceeded.setStatus(
        "current"
    )

sapDHCPLseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 10)
)
sapDHCPLseStateOverride.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"))
)
if mibBuilder.loadTexts:
    sapDHCPLseStateOverride.setStatus(
        "current"
    )

sapDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 11)
)
sapDHCPSuspiciousPcktRcvd.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sapDHCPSuspiciousPcktRcvd.setStatus(
        "current"
    )

sapDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 12)
)
sapDHCPLseStatePopulateErr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    sapDHCPLseStatePopulateErr.setStatus(
        "current"
    )

hostConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 13)
)
hostConnectivityLost.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityChAddr"))
)
if mibBuilder.loadTexts:
    hostConnectivityLost.setStatus(
        "current"
    )

hostConnectivityRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 14)
)
hostConnectivityRestored.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddrType"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "hostConnectivityChAddr"))
)
if mibBuilder.loadTexts:
    hostConnectivityRestored.setStatus(
        "current"
    )

sapReceivedProtSrcMac = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 15)
)
sapReceivedProtSrcMac.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "protectedMacForNotify"))
)
if mibBuilder.loadTexts:
    sapReceivedProtSrcMac.setStatus(
        "current"
    )

sapStaticHostDynMacConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 16)
)
sapStaticHostDynMacConflict.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "staticHostDynamicMacIpAddress"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "staticHostDynamicMacConflict"))
)
if mibBuilder.loadTexts:
    sapStaticHostDynMacConflict.setStatus(
        "current"
    )

sapTlsMacMoveExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 17)
)
sapTlsMacMoveExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacMoveRateExcdLeft"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacMoveNextUpTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"))
)
if mibBuilder.loadTexts:
    sapTlsMacMoveExceeded.setStatus(
        "current"
    )

sapDHCPProxyServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 18)
)
sapDHCPProxyServerError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpProxyError"))
)
if mibBuilder.loadTexts:
    sapDHCPProxyServerError.setStatus(
        "current"
    )

sapDHCPCoAError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 19)
)
sapDHCPCoAError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpCoAError"))
)
if mibBuilder.loadTexts:
    sapDHCPCoAError.setStatus(
        "obsolete"
    )

sapDHCPSubAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 20)
)
sapDHCPSubAuthError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpSubAuthError"))
)
if mibBuilder.loadTexts:
    sapDHCPSubAuthError.setStatus(
        "obsolete"
    )

sapPortStateChangeProcessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 21)
)
sapPortStateChangeProcessed.setObjects(
    ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapNotifyPortId")
)
if mibBuilder.loadTexts:
    sapPortStateChangeProcessed.setStatus(
        "current"
    )

sapDHCPLseStateMobilityError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 22)
)
sapDHCPLseStateMobilityError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    sapDHCPLseStateMobilityError.setStatus(
        "current"
    )

sapCemPacketDefectAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 23)
)
sapCemPacketDefectAlarm.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemReportAlarmStatus"))
)
if mibBuilder.loadTexts:
    sapCemPacketDefectAlarm.setStatus(
        "current"
    )

sapCemPacketDefectAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 24)
)
sapCemPacketDefectAlarmClear.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemReportAlarmStatus"))
)
if mibBuilder.loadTexts:
    sapCemPacketDefectAlarmClear.setStatus(
        "current"
    )

msapStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 25)
)
msapStateChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapStatus"))
)
if mibBuilder.loadTexts:
    msapStateChanged.setStatus(
        "current"
    )

msapCreationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 3, 0, 26)
)
msapCreationFailure.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "svcManagedSapCreationError"))
)
if mibBuilder.loadTexts:
    msapCreationFailure.setStatus(
        "current"
    )

topologyChangeSapMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 1)
)
topologyChangeSapMajorState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    topologyChangeSapMajorState.setStatus(
        "current"
    )

newRootSap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 2)
)
newRootSap.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    newRootSap.setStatus(
        "current"
    )

topologyChangeSapState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 5)
)
topologyChangeSapState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    topologyChangeSapState.setStatus(
        "current"
    )

receivedTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 6)
)
receivedTCN.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    receivedTCN.setStatus(
        "current"
    )

higherPriorityBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 9)
)
higherPriorityBridge.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"))
)
if mibBuilder.loadTexts:
    higherPriorityBridge.setStatus(
        "current"
    )

bridgedTLS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 10)
)
bridgedTLS.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"))
)
if mibBuilder.loadTexts:
    bridgedTLS.setStatus(
        "obsolete"
    )

sapEncapPVST = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 11)
)
sapEncapPVST.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    sapEncapPVST.setStatus(
        "current"
    )

sapEncapDot1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 12)
)
sapEncapDot1d.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    sapEncapDot1d.setStatus(
        "current"
    )

sapReceiveOwnBpdu = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 13)
)
sapReceiveOwnBpdu.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    sapReceiveOwnBpdu.setStatus(
        "obsolete"
    )

sapActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 30)
)
sapActiveProtocolChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpOperProtocol"))
)
if mibBuilder.loadTexts:
    sapActiveProtocolChange.setStatus(
        "current"
    )

tmnxStpRootGuardViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 35)
)
tmnxStpRootGuardViolation.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpRootGuardViolation"))
)
if mibBuilder.loadTexts:
    tmnxStpRootGuardViolation.setStatus(
        "current"
    )

tmnxSapStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 37)
)
tmnxSapStpExcepCondStateChng.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsStpException"))
)
if mibBuilder.loadTexts:
    tmnxSapStpExcepCondStateChng.setStatus(
        "current"
    )


# Notifications groups

tmnxSapNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 400)
)
tmnxSapNotifyGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStatusChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacAddrLimitAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacAddrLimitAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPLeaseEntriesExceeded"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPLseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPLseStatePopulateErr"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "hostConnectivityLost"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "hostConnectivityRestored"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapReceivedProtSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapStaticHostDynMacConflict"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsMacMoveExceeded"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPProxyServerError"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortStateChangeProcessed"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPLseStateMobilityError"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapStateChanged"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "msapCreationFailure"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "topologyChangeSapMajorState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "newRootSap"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "topologyChangeSapState"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "receivedTCN"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "higherPriorityBridge"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapPVST"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapDot1d"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapActiveProtocolChange"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "tmnxStpRootGuardViolation"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "tmnxSapStpExcepCondStateChng"))
)
if mibBuilder.loadTexts:
    tmnxSapNotifyGroup.setStatus(
        "current"
    )

tmnxSapCemNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 401)
)
tmnxSapCemNotificationV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemPacketDefectAlarm"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCemPacketDefectAlarmClear"))
)
if mibBuilder.loadTexts:
    tmnxSapCemNotificationV6v0Group.setStatus(
        "current"
    )

tmnxSapObsoletedNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 2, 402)
)
tmnxSapObsoletedNotifyGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapCreated"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDeleted"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDHCPLseStEntriesExceeded"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDHCPLeaseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapTlsDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPCoAError"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapDHCPSubAuthError"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "bridgedTLS"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapReceiveOwnBpdu"))
)
if mibBuilder.loadTexts:
    tmnxSapObsoletedNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSap7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 1, 100)
)
if mibBuilder.loadTexts:
    tmnxSap7450V6v0Compliance.setStatus(
        "current"
    )

tmnxSap7750V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 1, 101)
)
if mibBuilder.loadTexts:
    tmnxSap7750V6v0Compliance.setStatus(
        "current"
    )

tmnxSap7710V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 3, 1, 102)
)
if mibBuilder.loadTexts:
    tmnxSap7710V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-SAP-MIB",
    **{"timetraSvcSapMIBModule": timetraSvcSapMIBModule,
       "tmnxSapConformance": tmnxSapConformance,
       "tmnxSapCompliances": tmnxSapCompliances,
       "tmnxSap7450V6v0Compliance": tmnxSap7450V6v0Compliance,
       "tmnxSap7750V6v0Compliance": tmnxSap7750V6v0Compliance,
       "tmnxSap7710V6v0Compliance": tmnxSap7710V6v0Compliance,
       "tmnxSapGroups": tmnxSapGroups,
       "tmnxSapV6v0Group": tmnxSapV6v0Group,
       "tmnxSapTlsV6v0Group": tmnxSapTlsV6v0Group,
       "tmnxSapAtmV6v0Group": tmnxSapAtmV6v0Group,
       "tmnxSapBaseV6v0Group": tmnxSapBaseV6v0Group,
       "tmnxSapQosV6v0Group": tmnxSapQosV6v0Group,
       "tmnxSapStaticHostV6v0Group": tmnxSapStaticHostV6v0Group,
       "tmnxSapDhcpV6v0Group": tmnxSapDhcpV6v0Group,
       "tmnxSapPortIdV6v0Group": tmnxSapPortIdV6v0Group,
       "tmnxSapSubMgmtV6v0Group": tmnxSapSubMgmtV6v0Group,
       "tmnxSapMstiV6v0Group": tmnxSapMstiV6v0Group,
       "tmnxSapIppipeV6v0Group": tmnxSapIppipeV6v0Group,
       "tmnxSapPolicyV6v0Group": tmnxSapPolicyV6v0Group,
       "tmnxSapCemV6v0Group": tmnxSapCemV6v0Group,
       "tmnxSapL2ptV6v0Group": tmnxSapL2ptV6v0Group,
       "tmnxSapMsapV6v0Group": tmnxSapMsapV6v0Group,
       "tmnxSapMrpV6v0Group": tmnxSapMrpV6v0Group,
       "tmnxTlsMsapPppoeV6v0Group": tmnxTlsMsapPppoeV6v0Group,
       "tmnxSapIpV6FilterV6v0Group": tmnxSapIpV6FilterV6v0Group,
       "tmnxSapBsxV6v0Group": tmnxSapBsxV6v0Group,
       "tmnxSapNotificationObjV6v0Group": tmnxSapNotificationObjV6v0Group,
       "tmnxSapObsoletedV6v0Group": tmnxSapObsoletedV6v0Group,
       "tmnxSapNotifyGroup": tmnxSapNotifyGroup,
       "tmnxSapCemNotificationV6v0Group": tmnxSapCemNotificationV6v0Group,
       "tmnxSapObsoletedNotifyGroup": tmnxSapObsoletedNotifyGroup,
       "tmnxSapObjs": tmnxSapObjs,
       "sapNumEntries": sapNumEntries,
       "sapBaseInfoTable": sapBaseInfoTable,
       "sapBaseInfoEntry": sapBaseInfoEntry,
       "sapPortId": sapPortId,
       "sapEncapValue": sapEncapValue,
       "sapRowStatus": sapRowStatus,
       "sapType": sapType,
       "sapDescription": sapDescription,
       "sapAdminStatus": sapAdminStatus,
       "sapOperStatus": sapOperStatus,
       "sapIngressQosPolicyId": sapIngressQosPolicyId,
       "sapIngressMacFilterId": sapIngressMacFilterId,
       "sapIngressIpFilterId": sapIngressIpFilterId,
       "sapEgressQosPolicyId": sapEgressQosPolicyId,
       "sapEgressMacFilterId": sapEgressMacFilterId,
       "sapEgressIpFilterId": sapEgressIpFilterId,
       "sapMirrorStatus": sapMirrorStatus,
       "sapIesIfIndex": sapIesIfIndex,
       "sapLastMgmtChange": sapLastMgmtChange,
       "sapCollectAcctStats": sapCollectAcctStats,
       "sapAccountingPolicyId": sapAccountingPolicyId,
       "sapVpnId": sapVpnId,
       "sapCustId": sapCustId,
       "sapCustMultSvcSite": sapCustMultSvcSite,
       "sapIngressQosSchedulerPolicy": sapIngressQosSchedulerPolicy,
       "sapEgressQosSchedulerPolicy": sapEgressQosSchedulerPolicy,
       "sapSplitHorizonGrp": sapSplitHorizonGrp,
       "sapIngressSharedQueuePolicy": sapIngressSharedQueuePolicy,
       "sapIngressMatchQinQDot1PBits": sapIngressMatchQinQDot1PBits,
       "sapOperFlags": sapOperFlags,
       "sapLastStatusChange": sapLastStatusChange,
       "sapAntiSpoofing": sapAntiSpoofing,
       "sapIngressIpv6FilterId": sapIngressIpv6FilterId,
       "sapEgressIpv6FilterId": sapEgressIpv6FilterId,
       "sapTodSuite": sapTodSuite,
       "sapIngUseMultipointShared": sapIngUseMultipointShared,
       "sapEgressQinQMarkTopOnly": sapEgressQinQMarkTopOnly,
       "sapEgressAggRateLimit": sapEgressAggRateLimit,
       "sapEndPoint": sapEndPoint,
       "sapIngressVlanTranslation": sapIngressVlanTranslation,
       "sapIngressVlanTranslationId": sapIngressVlanTranslationId,
       "sapSubType": sapSubType,
       "sapCpmProtPolicyId": sapCpmProtPolicyId,
       "sapCpmProtMonitorMac": sapCpmProtMonitorMac,
       "sapEgressFrameBasedAccounting": sapEgressFrameBasedAccounting,
       "sapTlsInfoTable": sapTlsInfoTable,
       "sapTlsInfoEntry": sapTlsInfoEntry,
       "sapTlsStpAdminStatus": sapTlsStpAdminStatus,
       "sapTlsStpPriority": sapTlsStpPriority,
       "sapTlsStpPortNum": sapTlsStpPortNum,
       "sapTlsStpPathCost": sapTlsStpPathCost,
       "sapTlsStpRapidStart": sapTlsStpRapidStart,
       "sapTlsStpBpduEncap": sapTlsStpBpduEncap,
       "sapTlsStpPortState": sapTlsStpPortState,
       "sapTlsStpDesignatedBridge": sapTlsStpDesignatedBridge,
       "sapTlsStpDesignatedPort": sapTlsStpDesignatedPort,
       "sapTlsStpForwardTransitions": sapTlsStpForwardTransitions,
       "sapTlsStpInConfigBpdus": sapTlsStpInConfigBpdus,
       "sapTlsStpInTcnBpdus": sapTlsStpInTcnBpdus,
       "sapTlsStpInBadBpdus": sapTlsStpInBadBpdus,
       "sapTlsStpOutConfigBpdus": sapTlsStpOutConfigBpdus,
       "sapTlsStpOutTcnBpdus": sapTlsStpOutTcnBpdus,
       "sapTlsStpOperBpduEncap": sapTlsStpOperBpduEncap,
       "sapTlsVpnId": sapTlsVpnId,
       "sapTlsCustId": sapTlsCustId,
       "sapTlsMacAddressLimit": sapTlsMacAddressLimit,
       "sapTlsNumMacAddresses": sapTlsNumMacAddresses,
       "sapTlsNumStaticMacAddresses": sapTlsNumStaticMacAddresses,
       "sapTlsMacLearning": sapTlsMacLearning,
       "sapTlsMacAgeing": sapTlsMacAgeing,
       "sapTlsStpOperEdge": sapTlsStpOperEdge,
       "sapTlsStpAdminPointToPoint": sapTlsStpAdminPointToPoint,
       "sapTlsStpPortRole": sapTlsStpPortRole,
       "sapTlsStpAutoEdge": sapTlsStpAutoEdge,
       "sapTlsStpOperProtocol": sapTlsStpOperProtocol,
       "sapTlsStpInRstBpdus": sapTlsStpInRstBpdus,
       "sapTlsStpOutRstBpdus": sapTlsStpOutRstBpdus,
       "sapTlsLimitMacMove": sapTlsLimitMacMove,
       "sapTlsDhcpSnooping": sapTlsDhcpSnooping,
       "sapTlsMacPinning": sapTlsMacPinning,
       "sapTlsDiscardUnknownSource": sapTlsDiscardUnknownSource,
       "sapTlsMvplsPruneState": sapTlsMvplsPruneState,
       "sapTlsMvplsMgmtService": sapTlsMvplsMgmtService,
       "sapTlsMvplsMgmtPortId": sapTlsMvplsMgmtPortId,
       "sapTlsMvplsMgmtEncapValue": sapTlsMvplsMgmtEncapValue,
       "sapTlsArpReplyAgent": sapTlsArpReplyAgent,
       "sapTlsStpException": sapTlsStpException,
       "sapTlsAuthenticationPolicy": sapTlsAuthenticationPolicy,
       "sapTlsL2ptTermination": sapTlsL2ptTermination,
       "sapTlsBpduTranslation": sapTlsBpduTranslation,
       "sapTlsStpRootGuard": sapTlsStpRootGuard,
       "sapTlsStpInsideRegion": sapTlsStpInsideRegion,
       "sapTlsEgressMcastGroup": sapTlsEgressMcastGroup,
       "sapTlsStpInMstBpdus": sapTlsStpInMstBpdus,
       "sapTlsStpOutMstBpdus": sapTlsStpOutMstBpdus,
       "sapTlsRestProtSrcMac": sapTlsRestProtSrcMac,
       "sapTlsRestUnprotDstMac": sapTlsRestUnprotDstMac,
       "sapTlsStpRxdDesigBridge": sapTlsStpRxdDesigBridge,
       "sapTlsStpRootGuardViolation": sapTlsStpRootGuardViolation,
       "sapTlsShcvAction": sapTlsShcvAction,
       "sapTlsShcvSrcIp": sapTlsShcvSrcIp,
       "sapTlsShcvSrcMac": sapTlsShcvSrcMac,
       "sapTlsShcvInterval": sapTlsShcvInterval,
       "sapTlsMvplsMgmtMsti": sapTlsMvplsMgmtMsti,
       "sapTlsMacMoveNextUpTime": sapTlsMacMoveNextUpTime,
       "sapTlsMacMoveRateExcdLeft": sapTlsMacMoveRateExcdLeft,
       "sapTlsRestProtSrcMacAction": sapTlsRestProtSrcMacAction,
       "sapTlsL2ptForceBoundary": sapTlsL2ptForceBoundary,
       "sapTlsLimitMacMoveLevel": sapTlsLimitMacMoveLevel,
       "sapTlsBpduTransOper": sapTlsBpduTransOper,
       "sapTlsDefMsapPolicy": sapTlsDefMsapPolicy,
       "sapTlsL2ptProtocols": sapTlsL2ptProtocols,
       "sapTlsL2ptForceProtocols": sapTlsL2ptForceProtocols,
       "sapTlsPppoeMsapTrigger": sapTlsPppoeMsapTrigger,
       "sapTlsDhcpMsapTrigger": sapTlsDhcpMsapTrigger,
       "sapTlsMrpJoinTime": sapTlsMrpJoinTime,
       "sapTlsMrpLeaveTime": sapTlsMrpLeaveTime,
       "sapTlsMrpLeaveAllTime": sapTlsMrpLeaveAllTime,
       "sapTlsMrpPeriodicTime": sapTlsMrpPeriodicTime,
       "sapTlsMrpPeriodicEnabled": sapTlsMrpPeriodicEnabled,
       "sapAtmInfoTable": sapAtmInfoTable,
       "sapAtmInfoEntry": sapAtmInfoEntry,
       "sapAtmEncapsulation": sapAtmEncapsulation,
       "sapAtmIngressTrafficDescIndex": sapAtmIngressTrafficDescIndex,
       "sapAtmEgressTrafficDescIndex": sapAtmEgressTrafficDescIndex,
       "sapAtmOamAlarmCellHandling": sapAtmOamAlarmCellHandling,
       "sapAtmOamTerminate": sapAtmOamTerminate,
       "sapAtmOamPeriodicLoopback": sapAtmOamPeriodicLoopback,
       "sapBaseStatsTable": sapBaseStatsTable,
       "sapBaseStatsEntry": sapBaseStatsEntry,
       "sapBaseStatsIngressPchipDroppedPackets": sapBaseStatsIngressPchipDroppedPackets,
       "sapBaseStatsIngressPchipDroppedOctets": sapBaseStatsIngressPchipDroppedOctets,
       "sapBaseStatsIngressPchipOfferedHiPrioPackets": sapBaseStatsIngressPchipOfferedHiPrioPackets,
       "sapBaseStatsIngressPchipOfferedHiPrioOctets": sapBaseStatsIngressPchipOfferedHiPrioOctets,
       "sapBaseStatsIngressPchipOfferedLoPrioPackets": sapBaseStatsIngressPchipOfferedLoPrioPackets,
       "sapBaseStatsIngressPchipOfferedLoPrioOctets": sapBaseStatsIngressPchipOfferedLoPrioOctets,
       "sapBaseStatsIngressQchipDroppedHiPrioPackets": sapBaseStatsIngressQchipDroppedHiPrioPackets,
       "sapBaseStatsIngressQchipDroppedHiPrioOctets": sapBaseStatsIngressQchipDroppedHiPrioOctets,
       "sapBaseStatsIngressQchipDroppedLoPrioPackets": sapBaseStatsIngressQchipDroppedLoPrioPackets,
       "sapBaseStatsIngressQchipDroppedLoPrioOctets": sapBaseStatsIngressQchipDroppedLoPrioOctets,
       "sapBaseStatsIngressQchipForwardedInProfPackets": sapBaseStatsIngressQchipForwardedInProfPackets,
       "sapBaseStatsIngressQchipForwardedInProfOctets": sapBaseStatsIngressQchipForwardedInProfOctets,
       "sapBaseStatsIngressQchipForwardedOutProfPackets": sapBaseStatsIngressQchipForwardedOutProfPackets,
       "sapBaseStatsIngressQchipForwardedOutProfOctets": sapBaseStatsIngressQchipForwardedOutProfOctets,
       "sapBaseStatsEgressQchipDroppedInProfPackets": sapBaseStatsEgressQchipDroppedInProfPackets,
       "sapBaseStatsEgressQchipDroppedInProfOctets": sapBaseStatsEgressQchipDroppedInProfOctets,
       "sapBaseStatsEgressQchipDroppedOutProfPackets": sapBaseStatsEgressQchipDroppedOutProfPackets,
       "sapBaseStatsEgressQchipDroppedOutProfOctets": sapBaseStatsEgressQchipDroppedOutProfOctets,
       "sapBaseStatsEgressQchipForwardedInProfPackets": sapBaseStatsEgressQchipForwardedInProfPackets,
       "sapBaseStatsEgressQchipForwardedInProfOctets": sapBaseStatsEgressQchipForwardedInProfOctets,
       "sapBaseStatsEgressQchipForwardedOutProfPackets": sapBaseStatsEgressQchipForwardedOutProfPackets,
       "sapBaseStatsEgressQchipForwardedOutProfOctets": sapBaseStatsEgressQchipForwardedOutProfOctets,
       "sapBaseStatsCustId": sapBaseStatsCustId,
       "sapBaseStatsIngressPchipOfferedUncoloredPackets": sapBaseStatsIngressPchipOfferedUncoloredPackets,
       "sapBaseStatsIngressPchipOfferedUncoloredOctets": sapBaseStatsIngressPchipOfferedUncoloredOctets,
       "sapBaseStatsAuthenticationPktsDiscarded": sapBaseStatsAuthenticationPktsDiscarded,
       "sapBaseStatsAuthenticationPktsSuccess": sapBaseStatsAuthenticationPktsSuccess,
       "sapBaseStatsLastClearedTime": sapBaseStatsLastClearedTime,
       "sapIngQosQueueStatsTable": sapIngQosQueueStatsTable,
       "sapIngQosQueueStatsEntry": sapIngQosQueueStatsEntry,
       "sapIngQosQueueId": sapIngQosQueueId,
       "sapIngQosQueueStatsOfferedHiPrioPackets": sapIngQosQueueStatsOfferedHiPrioPackets,
       "sapIngQosQueueStatsDroppedHiPrioPackets": sapIngQosQueueStatsDroppedHiPrioPackets,
       "sapIngQosQueueStatsOfferedLoPrioPackets": sapIngQosQueueStatsOfferedLoPrioPackets,
       "sapIngQosQueueStatsDroppedLoPrioPackets": sapIngQosQueueStatsDroppedLoPrioPackets,
       "sapIngQosQueueStatsOfferedHiPrioOctets": sapIngQosQueueStatsOfferedHiPrioOctets,
       "sapIngQosQueueStatsDroppedHiPrioOctets": sapIngQosQueueStatsDroppedHiPrioOctets,
       "sapIngQosQueueStatsOfferedLoPrioOctets": sapIngQosQueueStatsOfferedLoPrioOctets,
       "sapIngQosQueueStatsDroppedLoPrioOctets": sapIngQosQueueStatsDroppedLoPrioOctets,
       "sapIngQosQueueStatsForwardedInProfPackets": sapIngQosQueueStatsForwardedInProfPackets,
       "sapIngQosQueueStatsForwardedOutProfPackets": sapIngQosQueueStatsForwardedOutProfPackets,
       "sapIngQosQueueStatsForwardedInProfOctets": sapIngQosQueueStatsForwardedInProfOctets,
       "sapIngQosQueueStatsForwardedOutProfOctets": sapIngQosQueueStatsForwardedOutProfOctets,
       "sapIngQosCustId": sapIngQosCustId,
       "sapIngQosQueueStatsUncoloredPacketsOffered": sapIngQosQueueStatsUncoloredPacketsOffered,
       "sapIngQosQueueStatsUncoloredOctetsOffered": sapIngQosQueueStatsUncoloredOctetsOffered,
       "sapEgrQosQueueStatsTable": sapEgrQosQueueStatsTable,
       "sapEgrQosQueueStatsEntry": sapEgrQosQueueStatsEntry,
       "sapEgrQosQueueId": sapEgrQosQueueId,
       "sapEgrQosQueueStatsForwardedInProfPackets": sapEgrQosQueueStatsForwardedInProfPackets,
       "sapEgrQosQueueStatsDroppedInProfPackets": sapEgrQosQueueStatsDroppedInProfPackets,
       "sapEgrQosQueueStatsForwardedOutProfPackets": sapEgrQosQueueStatsForwardedOutProfPackets,
       "sapEgrQosQueueStatsDroppedOutProfPackets": sapEgrQosQueueStatsDroppedOutProfPackets,
       "sapEgrQosQueueStatsForwardedInProfOctets": sapEgrQosQueueStatsForwardedInProfOctets,
       "sapEgrQosQueueStatsDroppedInProfOctets": sapEgrQosQueueStatsDroppedInProfOctets,
       "sapEgrQosQueueStatsForwardedOutProfOctets": sapEgrQosQueueStatsForwardedOutProfOctets,
       "sapEgrQosQueueStatsDroppedOutProfOctets": sapEgrQosQueueStatsDroppedOutProfOctets,
       "sapEgrQosCustId": sapEgrQosCustId,
       "sapIngQosSchedStatsTable": sapIngQosSchedStatsTable,
       "sapIngQosSchedStatsEntry": sapIngQosSchedStatsEntry,
       "sapIngQosSchedName": sapIngQosSchedName,
       "sapIngQosSchedStatsForwardedPackets": sapIngQosSchedStatsForwardedPackets,
       "sapIngQosSchedStatsForwardedOctets": sapIngQosSchedStatsForwardedOctets,
       "sapIngQosSchedCustId": sapIngQosSchedCustId,
       "sapEgrQosSchedStatsTable": sapEgrQosSchedStatsTable,
       "sapEgrQosSchedStatsEntry": sapEgrQosSchedStatsEntry,
       "sapEgrQosSchedName": sapEgrQosSchedName,
       "sapEgrQosSchedStatsForwardedPackets": sapEgrQosSchedStatsForwardedPackets,
       "sapEgrQosSchedStatsForwardedOctets": sapEgrQosSchedStatsForwardedOctets,
       "sapEgrQosSchedCustId": sapEgrQosSchedCustId,
       "sapTlsManagedVlanListTable": sapTlsManagedVlanListTable,
       "sapTlsManagedVlanListEntry": sapTlsManagedVlanListEntry,
       "sapTlsMvplsMinVlanTag": sapTlsMvplsMinVlanTag,
       "sapTlsMvplsMaxVlanTag": sapTlsMvplsMaxVlanTag,
       "sapTlsMvplsRowStatus": sapTlsMvplsRowStatus,
       "sapAntiSpoofTable": sapAntiSpoofTable,
       "sapAntiSpoofEntry": sapAntiSpoofEntry,
       "sapAntiSpoofIpAddress": sapAntiSpoofIpAddress,
       "sapAntiSpoofMacAddress": sapAntiSpoofMacAddress,
       "sapStaticHostTable": sapStaticHostTable,
       "sapStaticHostEntry": sapStaticHostEntry,
       "sapStaticHostRowStatus": sapStaticHostRowStatus,
       "sapStaticHostIpAddress": sapStaticHostIpAddress,
       "sapStaticHostMacAddress": sapStaticHostMacAddress,
       "sapStaticHostSubscrIdent": sapStaticHostSubscrIdent,
       "sapStaticHostSubProfile": sapStaticHostSubProfile,
       "sapStaticHostSlaProfile": sapStaticHostSlaProfile,
       "sapStaticHostShcvOperState": sapStaticHostShcvOperState,
       "sapStaticHostShcvChecks": sapStaticHostShcvChecks,
       "sapStaticHostShcvReplies": sapStaticHostShcvReplies,
       "sapStaticHostShcvReplyTime": sapStaticHostShcvReplyTime,
       "sapStaticHostDynMacAddress": sapStaticHostDynMacAddress,
       "sapStaticHostRetailerSvcId": sapStaticHostRetailerSvcId,
       "sapStaticHostRetailerIf": sapStaticHostRetailerIf,
       "sapStaticHostFwdingState": sapStaticHostFwdingState,
       "sapStaticHostAncpString": sapStaticHostAncpString,
       "sapStaticHostSubIdIsSapId": sapStaticHostSubIdIsSapId,
       "sapStaticHostAppProfile": sapStaticHostAppProfile,
       "sapStaticHostIntermediateDestId": sapStaticHostIntermediateDestId,
       "sapTlsDhcpInfoTable": sapTlsDhcpInfoTable,
       "sapTlsDhcpInfoEntry": sapTlsDhcpInfoEntry,
       "sapTlsDhcpAdminState": sapTlsDhcpAdminState,
       "sapTlsDhcpDescription": sapTlsDhcpDescription,
       "sapTlsDhcpSnoop": sapTlsDhcpSnoop,
       "sapTlsDhcpLeasePopulate": sapTlsDhcpLeasePopulate,
       "sapTlsDhcpOperLeasePopulate": sapTlsDhcpOperLeasePopulate,
       "sapTlsDhcpInfoAction": sapTlsDhcpInfoAction,
       "sapTlsDhcpCircuitId": sapTlsDhcpCircuitId,
       "sapTlsDhcpRemoteId": sapTlsDhcpRemoteId,
       "sapTlsDhcpRemoteIdString": sapTlsDhcpRemoteIdString,
       "sapTlsDhcpProxyAdminState": sapTlsDhcpProxyAdminState,
       "sapTlsDhcpProxyServerAddr": sapTlsDhcpProxyServerAddr,
       "sapTlsDhcpProxyLeaseTime": sapTlsDhcpProxyLeaseTime,
       "sapTlsDhcpProxyLTRadiusOverride": sapTlsDhcpProxyLTRadiusOverride,
       "sapTlsDhcpVendorIncludeOptions": sapTlsDhcpVendorIncludeOptions,
       "sapTlsDhcpVendorOptionString": sapTlsDhcpVendorOptionString,
       "sapTlsDhcpStatsTable": sapTlsDhcpStatsTable,
       "sapTlsDhcpStatsEntry": sapTlsDhcpStatsEntry,
       "sapTlsDhcpStatsClntSnoopdPckts": sapTlsDhcpStatsClntSnoopdPckts,
       "sapTlsDhcpStatsSrvrSnoopdPckts": sapTlsDhcpStatsSrvrSnoopdPckts,
       "sapTlsDhcpStatsClntForwdPckts": sapTlsDhcpStatsClntForwdPckts,
       "sapTlsDhcpStatsSrvrForwdPckts": sapTlsDhcpStatsSrvrForwdPckts,
       "sapTlsDhcpStatsClntDropdPckts": sapTlsDhcpStatsClntDropdPckts,
       "sapTlsDhcpStatsSrvrDropdPckts": sapTlsDhcpStatsSrvrDropdPckts,
       "sapTlsDhcpStatsClntProxRadPckts": sapTlsDhcpStatsClntProxRadPckts,
       "sapTlsDhcpStatsClntProxLSPckts": sapTlsDhcpStatsClntProxLSPckts,
       "sapTlsDhcpStatsGenReleasePckts": sapTlsDhcpStatsGenReleasePckts,
       "sapTlsDhcpStatsGenForceRenPckts": sapTlsDhcpStatsGenForceRenPckts,
       "sapTlsDhcpLeaseStateTable": sapTlsDhcpLeaseStateTable,
       "sapTlsDhcpLeaseStateEntry": sapTlsDhcpLeaseStateEntry,
       "sapTlsDhcpLseStateCiAddr": sapTlsDhcpLseStateCiAddr,
       "sapTlsDhcpLseStateChAddr": sapTlsDhcpLseStateChAddr,
       "sapTlsDhcpLseStateRemainLseTime": sapTlsDhcpLseStateRemainLseTime,
       "sapTlsDhcpLseStateOption82": sapTlsDhcpLseStateOption82,
       "sapTlsDhcpLseStatePersistKey": sapTlsDhcpLseStatePersistKey,
       "sapPortIdIngQosSchedStatsTable": sapPortIdIngQosSchedStatsTable,
       "sapPortIdIngQosSchedStatsEntry": sapPortIdIngQosSchedStatsEntry,
       "sapPortIdIngQosSchedName": sapPortIdIngQosSchedName,
       "sapPortIdIngPortId": sapPortIdIngPortId,
       "sapPortIdIngQosSchedFwdPkts": sapPortIdIngQosSchedFwdPkts,
       "sapPortIdIngQosSchedFwdOctets": sapPortIdIngQosSchedFwdOctets,
       "sapPortIdIngQosSchedCustId": sapPortIdIngQosSchedCustId,
       "sapPortIdEgrQosSchedStatsTable": sapPortIdEgrQosSchedStatsTable,
       "sapPortIdEgrQosSchedStatsEntry": sapPortIdEgrQosSchedStatsEntry,
       "sapPortIdEgrQosSchedName": sapPortIdEgrQosSchedName,
       "sapPortIdEgrPortId": sapPortIdEgrPortId,
       "sapPortIdEgrQosSchedFwdPkts": sapPortIdEgrQosSchedFwdPkts,
       "sapPortIdEgrQosSchedFwdOctets": sapPortIdEgrQosSchedFwdOctets,
       "sapPortIdEgrQosSchedCustId": sapPortIdEgrQosSchedCustId,
       "sapIngQosQueueInfoTable": sapIngQosQueueInfoTable,
       "sapIngQosQueueInfoEntry": sapIngQosQueueInfoEntry,
       "sapIngQosQId": sapIngQosQId,
       "sapIngQosQRowStatus": sapIngQosQRowStatus,
       "sapIngQosQLastMgmtChange": sapIngQosQLastMgmtChange,
       "sapIngQosQOverrideFlags": sapIngQosQOverrideFlags,
       "sapIngQosQCBS": sapIngQosQCBS,
       "sapIngQosQMBS": sapIngQosQMBS,
       "sapIngQosQHiPrioOnly": sapIngQosQHiPrioOnly,
       "sapIngQosQCIRAdaptation": sapIngQosQCIRAdaptation,
       "sapIngQosQPIRAdaptation": sapIngQosQPIRAdaptation,
       "sapIngQosQAdminPIR": sapIngQosQAdminPIR,
       "sapIngQosQAdminCIR": sapIngQosQAdminCIR,
       "sapEgrQosQueueInfoTable": sapEgrQosQueueInfoTable,
       "sapEgrQosQueueInfoEntry": sapEgrQosQueueInfoEntry,
       "sapEgrQosQId": sapEgrQosQId,
       "sapEgrQosQRowStatus": sapEgrQosQRowStatus,
       "sapEgrQosQLastMgmtChange": sapEgrQosQLastMgmtChange,
       "sapEgrQosQOverrideFlags": sapEgrQosQOverrideFlags,
       "sapEgrQosQCBS": sapEgrQosQCBS,
       "sapEgrQosQMBS": sapEgrQosQMBS,
       "sapEgrQosQHiPrioOnly": sapEgrQosQHiPrioOnly,
       "sapEgrQosQCIRAdaptation": sapEgrQosQCIRAdaptation,
       "sapEgrQosQPIRAdaptation": sapEgrQosQPIRAdaptation,
       "sapEgrQosQAdminPIR": sapEgrQosQAdminPIR,
       "sapEgrQosQAdminCIR": sapEgrQosQAdminCIR,
       "sapEgrQosQAvgOverhead": sapEgrQosQAvgOverhead,
       "sapIngQosSchedInfoTable": sapIngQosSchedInfoTable,
       "sapIngQosSchedInfoEntry": sapIngQosSchedInfoEntry,
       "sapIngQosSName": sapIngQosSName,
       "sapIngQosSRowStatus": sapIngQosSRowStatus,
       "sapIngQosSLastMgmtChange": sapIngQosSLastMgmtChange,
       "sapIngQosSOverrideFlags": sapIngQosSOverrideFlags,
       "sapIngQosSPIR": sapIngQosSPIR,
       "sapIngQosSCIR": sapIngQosSCIR,
       "sapIngQosSSummedCIR": sapIngQosSSummedCIR,
       "sapEgrQosSchedInfoTable": sapEgrQosSchedInfoTable,
       "sapEgrQosSchedInfoEntry": sapEgrQosSchedInfoEntry,
       "sapEgrQosSName": sapEgrQosSName,
       "sapEgrQosSRowStatus": sapEgrQosSRowStatus,
       "sapEgrQosSLastMgmtChange": sapEgrQosSLastMgmtChange,
       "sapEgrQosSOverrideFlags": sapEgrQosSOverrideFlags,
       "sapEgrQosSPIR": sapEgrQosSPIR,
       "sapEgrQosSCIR": sapEgrQosSCIR,
       "sapEgrQosSSummedCIR": sapEgrQosSSummedCIR,
       "sapSubMgmtInfoTable": sapSubMgmtInfoTable,
       "sapSubMgmtInfoEntry": sapSubMgmtInfoEntry,
       "sapSubMgmtAdminStatus": sapSubMgmtAdminStatus,
       "sapSubMgmtDefSubProfile": sapSubMgmtDefSubProfile,
       "sapSubMgmtDefSlaProfile": sapSubMgmtDefSlaProfile,
       "sapSubMgmtSubIdentPolicy": sapSubMgmtSubIdentPolicy,
       "sapSubMgmtSubscriberLimit": sapSubMgmtSubscriberLimit,
       "sapSubMgmtProfiledTrafficOnly": sapSubMgmtProfiledTrafficOnly,
       "sapSubMgmtNonSubTrafficSubIdent": sapSubMgmtNonSubTrafficSubIdent,
       "sapSubMgmtNonSubTrafficSubProf": sapSubMgmtNonSubTrafficSubProf,
       "sapSubMgmtNonSubTrafficSlaProf": sapSubMgmtNonSubTrafficSlaProf,
       "sapSubMgmtMacDaHashing": sapSubMgmtMacDaHashing,
       "sapSubMgmtDefSubIdent": sapSubMgmtDefSubIdent,
       "sapSubMgmtDefSubIdentString": sapSubMgmtDefSubIdentString,
       "sapSubMgmtDefAppProfile": sapSubMgmtDefAppProfile,
       "sapSubMgmtNonSubTrafficAppProf": sapSubMgmtNonSubTrafficAppProf,
       "sapTlsMstiTable": sapTlsMstiTable,
       "sapTlsMstiEntry": sapTlsMstiEntry,
       "sapTlsMstiPriority": sapTlsMstiPriority,
       "sapTlsMstiPathCost": sapTlsMstiPathCost,
       "sapTlsMstiLastMgmtChange": sapTlsMstiLastMgmtChange,
       "sapTlsMstiPortRole": sapTlsMstiPortRole,
       "sapTlsMstiPortState": sapTlsMstiPortState,
       "sapTlsMstiDesignatedBridge": sapTlsMstiDesignatedBridge,
       "sapTlsMstiDesignatedPort": sapTlsMstiDesignatedPort,
       "sapIpipeInfoTable": sapIpipeInfoTable,
       "sapIpipeInfoEntry": sapIpipeInfoEntry,
       "sapIpipeCeInetAddressType": sapIpipeCeInetAddressType,
       "sapIpipeCeInetAddress": sapIpipeCeInetAddress,
       "sapIpipeMacRefreshInterval": sapIpipeMacRefreshInterval,
       "sapIpipeMacAddress": sapIpipeMacAddress,
       "sapIpipeArpedMacAddress": sapIpipeArpedMacAddress,
       "sapIpipeArpedMacAddressTimeout": sapIpipeArpedMacAddressTimeout,
       "sapTodMonitorTable": sapTodMonitorTable,
       "sapTodMonitorEntry": sapTodMonitorEntry,
       "sapCurrentIngressIpFilterId": sapCurrentIngressIpFilterId,
       "sapCurrentIngressIpv6FilterId": sapCurrentIngressIpv6FilterId,
       "sapCurrentIngressMacFilterId": sapCurrentIngressMacFilterId,
       "sapCurrentIngressQosPolicyId": sapCurrentIngressQosPolicyId,
       "sapCurrentIngressQosSchedPlcy": sapCurrentIngressQosSchedPlcy,
       "sapCurrentEgressIpFilterId": sapCurrentEgressIpFilterId,
       "sapCurrentEgressIpv6FilterId": sapCurrentEgressIpv6FilterId,
       "sapCurrentEgressMacFilterId": sapCurrentEgressMacFilterId,
       "sapCurrentEgressQosPolicyId": sapCurrentEgressQosPolicyId,
       "sapCurrentEgressQosSchedPlcy": sapCurrentEgressQosSchedPlcy,
       "sapIntendedIngressIpFilterId": sapIntendedIngressIpFilterId,
       "sapIntendedIngressIpv6FilterId": sapIntendedIngressIpv6FilterId,
       "sapIntendedIngressMacFilterId": sapIntendedIngressMacFilterId,
       "sapIntendedIngressQosPolicyId": sapIntendedIngressQosPolicyId,
       "sapIntendedIngressQosSchedPlcy": sapIntendedIngressQosSchedPlcy,
       "sapIntendedEgressIpFilterId": sapIntendedEgressIpFilterId,
       "sapIntendedEgressIpv6FilterId": sapIntendedEgressIpv6FilterId,
       "sapIntendedEgressMacFilterId": sapIntendedEgressMacFilterId,
       "sapIntendedEgressQosPolicyId": sapIntendedEgressQosPolicyId,
       "sapIntendedEgressQosSchedPlcy": sapIntendedEgressQosSchedPlcy,
       "sapIngrQosPlcyStatsTable": sapIngrQosPlcyStatsTable,
       "sapIngrQosPlcyStatsEntry": sapIngrQosPlcyStatsEntry,
       "sapIgQosPlcyId": sapIgQosPlcyId,
       "sapIgQosPlcyDroppedHiPrioPackets": sapIgQosPlcyDroppedHiPrioPackets,
       "sapIgQosPlcyDroppedHiPrioOctets": sapIgQosPlcyDroppedHiPrioOctets,
       "sapIgQosPlcyDroppedLoPrioPackets": sapIgQosPlcyDroppedLoPrioPackets,
       "sapIgQosPlcyDroppedLoPrioOctets": sapIgQosPlcyDroppedLoPrioOctets,
       "sapIgQosPlcyForwardedInProfPackets": sapIgQosPlcyForwardedInProfPackets,
       "sapIgQosPlcyForwardedInProfOctets": sapIgQosPlcyForwardedInProfOctets,
       "sapIgQosPlcyForwardedOutProfPackets": sapIgQosPlcyForwardedOutProfPackets,
       "sapIgQosPlcyForwardedOutProfOctets": sapIgQosPlcyForwardedOutProfOctets,
       "sapEgrQosPlcyStatsTable": sapEgrQosPlcyStatsTable,
       "sapEgrQosPlcyStatsEntry": sapEgrQosPlcyStatsEntry,
       "sapEgQosPlcyId": sapEgQosPlcyId,
       "sapEgQosPlcyDroppedInProfPackets": sapEgQosPlcyDroppedInProfPackets,
       "sapEgQosPlcyDroppedInProfOctets": sapEgQosPlcyDroppedInProfOctets,
       "sapEgQosPlcyDroppedOutProfPackets": sapEgQosPlcyDroppedOutProfPackets,
       "sapEgQosPlcyDroppedOutProfOctets": sapEgQosPlcyDroppedOutProfOctets,
       "sapEgQosPlcyForwardedInProfPackets": sapEgQosPlcyForwardedInProfPackets,
       "sapEgQosPlcyForwardedInProfOctets": sapEgQosPlcyForwardedInProfOctets,
       "sapEgQosPlcyForwardedOutProfPackets": sapEgQosPlcyForwardedOutProfPackets,
       "sapEgQosPlcyForwardedOutProfOctets": sapEgQosPlcyForwardedOutProfOctets,
       "sapIngQosPlcyQueueStatsTable": sapIngQosPlcyQueueStatsTable,
       "sapIngQosPlcyQueueStatsEntry": sapIngQosPlcyQueueStatsEntry,
       "sapIgQosPlcyQueuePlcyId": sapIgQosPlcyQueuePlcyId,
       "sapIgQosPlcyQueueId": sapIgQosPlcyQueueId,
       "sapIgQosPlcyQueueStatsOfferedHiPrioPackets": sapIgQosPlcyQueueStatsOfferedHiPrioPackets,
       "sapIgQosPlcyQueueStatsDroppedHiPrioPackets": sapIgQosPlcyQueueStatsDroppedHiPrioPackets,
       "sapIgQosPlcyQueueStatsOfferedLoPrioPackets": sapIgQosPlcyQueueStatsOfferedLoPrioPackets,
       "sapIgQosPlcyQueueStatsDroppedLoPrioPackets": sapIgQosPlcyQueueStatsDroppedLoPrioPackets,
       "sapIgQosPlcyQueueStatsOfferedHiPrioOctets": sapIgQosPlcyQueueStatsOfferedHiPrioOctets,
       "sapIgQosPlcyQueueStatsDroppedHiPrioOctets": sapIgQosPlcyQueueStatsDroppedHiPrioOctets,
       "sapIgQosPlcyQueueStatsOfferedLoPrioOctets": sapIgQosPlcyQueueStatsOfferedLoPrioOctets,
       "sapIgQosPlcyQueueStatsDroppedLoPrioOctets": sapIgQosPlcyQueueStatsDroppedLoPrioOctets,
       "sapIgQosPlcyQueueStatsForwardedInProfPackets": sapIgQosPlcyQueueStatsForwardedInProfPackets,
       "sapIgQosPlcyQueueStatsForwardedOutProfPackets": sapIgQosPlcyQueueStatsForwardedOutProfPackets,
       "sapIgQosPlcyQueueStatsForwardedInProfOctets": sapIgQosPlcyQueueStatsForwardedInProfOctets,
       "sapIgQosPlcyQueueStatsForwardedOutProfOctets": sapIgQosPlcyQueueStatsForwardedOutProfOctets,
       "sapIgQosPlcyQueueCustId": sapIgQosPlcyQueueCustId,
       "sapIgQosPlcyQueueStatsUncoloredPacketsOffered": sapIgQosPlcyQueueStatsUncoloredPacketsOffered,
       "sapIgQosPlcyQueueStatsUncoloredOctetsOffered": sapIgQosPlcyQueueStatsUncoloredOctetsOffered,
       "sapEgrQosPlcyQueueStatsTable": sapEgrQosPlcyQueueStatsTable,
       "sapEgrQosPlcyQueueStatsEntry": sapEgrQosPlcyQueueStatsEntry,
       "sapEgQosPlcyQueuePlcyId": sapEgQosPlcyQueuePlcyId,
       "sapEgQosPlcyQueueId": sapEgQosPlcyQueueId,
       "sapEgQosPlcyQueueStatsForwardedInProfPackets": sapEgQosPlcyQueueStatsForwardedInProfPackets,
       "sapEgQosPlcyQueueStatsDroppedInProfPackets": sapEgQosPlcyQueueStatsDroppedInProfPackets,
       "sapEgQosPlcyQueueStatsForwardedOutProfPackets": sapEgQosPlcyQueueStatsForwardedOutProfPackets,
       "sapEgQosPlcyQueueStatsDroppedOutProfPackets": sapEgQosPlcyQueueStatsDroppedOutProfPackets,
       "sapEgQosPlcyQueueStatsForwardedInProfOctets": sapEgQosPlcyQueueStatsForwardedInProfOctets,
       "sapEgQosPlcyQueueStatsDroppedInProfOctets": sapEgQosPlcyQueueStatsDroppedInProfOctets,
       "sapEgQosPlcyQueueStatsForwardedOutProfOctets": sapEgQosPlcyQueueStatsForwardedOutProfOctets,
       "sapEgQosPlcyQueueStatsDroppedOutProfOctets": sapEgQosPlcyQueueStatsDroppedOutProfOctets,
       "sapEgQosPlcyQueueCustId": sapEgQosPlcyQueueCustId,
       "sapDhcpInfoTable": sapDhcpInfoTable,
       "sapDhcpInfoEntry": sapDhcpInfoEntry,
       "sapDhcpOperLeasePopulate": sapDhcpOperLeasePopulate,
       "sapIngSchedPlcyStatsTable": sapIngSchedPlcyStatsTable,
       "sapIngSchedPlcyStatsEntry": sapIngSchedPlcyStatsEntry,
       "sapIngSchedPlcyStatsFwdPkt": sapIngSchedPlcyStatsFwdPkt,
       "sapIngSchedPlcyStatsFwdOct": sapIngSchedPlcyStatsFwdOct,
       "sapEgrSchedPlcyStatsTable": sapEgrSchedPlcyStatsTable,
       "sapEgrSchedPlcyStatsEntry": sapEgrSchedPlcyStatsEntry,
       "sapEgrSchedPlcyStatsFwdPkt": sapEgrSchedPlcyStatsFwdPkt,
       "sapEgrSchedPlcyStatsFwdOct": sapEgrSchedPlcyStatsFwdOct,
       "sapIngSchedPlcyPortStatsTable": sapIngSchedPlcyPortStatsTable,
       "sapIngSchedPlcyPortStatsEntry": sapIngSchedPlcyPortStatsEntry,
       "sapIngSchedPlcyPortStatsPort": sapIngSchedPlcyPortStatsPort,
       "sapIngSchedPlcyPortStatsFwdPkt": sapIngSchedPlcyPortStatsFwdPkt,
       "sapIngSchedPlcyPortStatsFwdOct": sapIngSchedPlcyPortStatsFwdOct,
       "sapEgrSchedPlcyPortStatsTable": sapEgrSchedPlcyPortStatsTable,
       "sapEgrSchedPlcyPortStatsEntry": sapEgrSchedPlcyPortStatsEntry,
       "sapEgrSchedPlcyPortStatsPort": sapEgrSchedPlcyPortStatsPort,
       "sapEgrSchedPlcyPortStatsFwdPkt": sapEgrSchedPlcyPortStatsFwdPkt,
       "sapEgrSchedPlcyPortStatsFwdOct": sapEgrSchedPlcyPortStatsFwdOct,
       "sapCemInfoTable": sapCemInfoTable,
       "sapCemInfoEntry": sapCemInfoEntry,
       "sapCemLastMgmtChange": sapCemLastMgmtChange,
       "sapCemEndpointType": sapCemEndpointType,
       "sapCemBitrate": sapCemBitrate,
       "sapCemCasTrunkFraming": sapCemCasTrunkFraming,
       "sapCemPayloadSize": sapCemPayloadSize,
       "sapCemJitterBuffer": sapCemJitterBuffer,
       "sapCemUseRtpHeader": sapCemUseRtpHeader,
       "sapCemDifferential": sapCemDifferential,
       "sapCemTimestampFreq": sapCemTimestampFreq,
       "sapCemReportAlarm": sapCemReportAlarm,
       "sapCemReportAlarmStatus": sapCemReportAlarmStatus,
       "sapCemLocalEcid": sapCemLocalEcid,
       "sapCemRemoteMacAddr": sapCemRemoteMacAddr,
       "sapCemRemoteEcid": sapCemRemoteEcid,
       "sapCemStatsTable": sapCemStatsTable,
       "sapCemStatsEntry": sapCemStatsEntry,
       "sapCemStatsIngressForwardedPkts": sapCemStatsIngressForwardedPkts,
       "sapCemStatsIngressDroppedPkts": sapCemStatsIngressDroppedPkts,
       "sapCemStatsEgressForwardedPkts": sapCemStatsEgressForwardedPkts,
       "sapCemStatsEgressDroppedPkts": sapCemStatsEgressDroppedPkts,
       "sapCemStatsEgressMissingPkts": sapCemStatsEgressMissingPkts,
       "sapCemStatsEgressPktsReOrder": sapCemStatsEgressPktsReOrder,
       "sapCemStatsEgressJtrBfrUnderruns": sapCemStatsEgressJtrBfrUnderruns,
       "sapCemStatsEgressJtrBfrOverruns": sapCemStatsEgressJtrBfrOverruns,
       "sapCemStatsEgressMisOrderDropped": sapCemStatsEgressMisOrderDropped,
       "sapCemStatsEgressMalformedPkts": sapCemStatsEgressMalformedPkts,
       "sapCemStatsEgressLBitDropped": sapCemStatsEgressLBitDropped,
       "sapCemStatsEgressMultipleDropped": sapCemStatsEgressMultipleDropped,
       "sapCemStatsEgressESs": sapCemStatsEgressESs,
       "sapCemStatsEgressSESs": sapCemStatsEgressSESs,
       "sapCemStatsEgressUASs": sapCemStatsEgressUASs,
       "sapCemStatsEgressFailureCounts": sapCemStatsEgressFailureCounts,
       "sapCemStatsEgressUnderrunCounts": sapCemStatsEgressUnderrunCounts,
       "sapCemStatsEgressOverrunCounts": sapCemStatsEgressOverrunCounts,
       "sapTlsL2ptStatsTable": sapTlsL2ptStatsTable,
       "sapTlsL2ptStatsEntry": sapTlsL2ptStatsEntry,
       "sapTlsL2ptStatsLastClearedTime": sapTlsL2ptStatsLastClearedTime,
       "sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx": sapTlsL2ptStatsL2ptEncapStpConfigBpdusRx,
       "sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx": sapTlsL2ptStatsL2ptEncapStpConfigBpdusTx,
       "sapTlsL2ptStatsL2ptEncapStpRstBpdusRx": sapTlsL2ptStatsL2ptEncapStpRstBpdusRx,
       "sapTlsL2ptStatsL2ptEncapStpRstBpdusTx": sapTlsL2ptStatsL2ptEncapStpRstBpdusTx,
       "sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx": sapTlsL2ptStatsL2ptEncapStpTcnBpdusRx,
       "sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx": sapTlsL2ptStatsL2ptEncapStpTcnBpdusTx,
       "sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx": sapTlsL2ptStatsL2ptEncapPvstConfigBpdusRx,
       "sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx": sapTlsL2ptStatsL2ptEncapPvstConfigBpdusTx,
       "sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx": sapTlsL2ptStatsL2ptEncapPvstRstBpdusRx,
       "sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx": sapTlsL2ptStatsL2ptEncapPvstRstBpdusTx,
       "sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx": sapTlsL2ptStatsL2ptEncapPvstTcnBpdusRx,
       "sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx": sapTlsL2ptStatsL2ptEncapPvstTcnBpdusTx,
       "sapTlsL2ptStatsStpConfigBpdusRx": sapTlsL2ptStatsStpConfigBpdusRx,
       "sapTlsL2ptStatsStpConfigBpdusTx": sapTlsL2ptStatsStpConfigBpdusTx,
       "sapTlsL2ptStatsStpRstBpdusRx": sapTlsL2ptStatsStpRstBpdusRx,
       "sapTlsL2ptStatsStpRstBpdusTx": sapTlsL2ptStatsStpRstBpdusTx,
       "sapTlsL2ptStatsStpTcnBpdusRx": sapTlsL2ptStatsStpTcnBpdusRx,
       "sapTlsL2ptStatsStpTcnBpdusTx": sapTlsL2ptStatsStpTcnBpdusTx,
       "sapTlsL2ptStatsPvstConfigBpdusRx": sapTlsL2ptStatsPvstConfigBpdusRx,
       "sapTlsL2ptStatsPvstConfigBpdusTx": sapTlsL2ptStatsPvstConfigBpdusTx,
       "sapTlsL2ptStatsPvstRstBpdusRx": sapTlsL2ptStatsPvstRstBpdusRx,
       "sapTlsL2ptStatsPvstRstBpdusTx": sapTlsL2ptStatsPvstRstBpdusTx,
       "sapTlsL2ptStatsPvstTcnBpdusRx": sapTlsL2ptStatsPvstTcnBpdusRx,
       "sapTlsL2ptStatsPvstTcnBpdusTx": sapTlsL2ptStatsPvstTcnBpdusTx,
       "sapTlsL2ptStatsOtherBpdusRx": sapTlsL2ptStatsOtherBpdusRx,
       "sapTlsL2ptStatsOtherBpdusTx": sapTlsL2ptStatsOtherBpdusTx,
       "sapTlsL2ptStatsOtherL2ptBpdusRx": sapTlsL2ptStatsOtherL2ptBpdusRx,
       "sapTlsL2ptStatsOtherL2ptBpdusTx": sapTlsL2ptStatsOtherL2ptBpdusTx,
       "sapTlsL2ptStatsOtherInvalidBpdusRx": sapTlsL2ptStatsOtherInvalidBpdusRx,
       "sapTlsL2ptStatsOtherInvalidBpdusTx": sapTlsL2ptStatsOtherInvalidBpdusTx,
       "sapTlsL2ptStatsL2ptEncapCdpBpdusRx": sapTlsL2ptStatsL2ptEncapCdpBpdusRx,
       "sapTlsL2ptStatsL2ptEncapCdpBpdusTx": sapTlsL2ptStatsL2ptEncapCdpBpdusTx,
       "sapTlsL2ptStatsL2ptEncapVtpBpdusRx": sapTlsL2ptStatsL2ptEncapVtpBpdusRx,
       "sapTlsL2ptStatsL2ptEncapVtpBpdusTx": sapTlsL2ptStatsL2ptEncapVtpBpdusTx,
       "sapTlsL2ptStatsL2ptEncapDtpBpdusRx": sapTlsL2ptStatsL2ptEncapDtpBpdusRx,
       "sapTlsL2ptStatsL2ptEncapDtpBpdusTx": sapTlsL2ptStatsL2ptEncapDtpBpdusTx,
       "sapTlsL2ptStatsL2ptEncapPagpBpdusRx": sapTlsL2ptStatsL2ptEncapPagpBpdusRx,
       "sapTlsL2ptStatsL2ptEncapPagpBpdusTx": sapTlsL2ptStatsL2ptEncapPagpBpdusTx,
       "sapTlsL2ptStatsL2ptEncapUdldBpdusRx": sapTlsL2ptStatsL2ptEncapUdldBpdusRx,
       "sapTlsL2ptStatsL2ptEncapUdldBpdusTx": sapTlsL2ptStatsL2ptEncapUdldBpdusTx,
       "sapTlsL2ptStatsCdpBpdusRx": sapTlsL2ptStatsCdpBpdusRx,
       "sapTlsL2ptStatsCdpBpdusTx": sapTlsL2ptStatsCdpBpdusTx,
       "sapTlsL2ptStatsVtpBpdusRx": sapTlsL2ptStatsVtpBpdusRx,
       "sapTlsL2ptStatsVtpBpdusTx": sapTlsL2ptStatsVtpBpdusTx,
       "sapTlsL2ptStatsDtpBpdusRx": sapTlsL2ptStatsDtpBpdusRx,
       "sapTlsL2ptStatsDtpBpdusTx": sapTlsL2ptStatsDtpBpdusTx,
       "sapTlsL2ptStatsPagpBpdusRx": sapTlsL2ptStatsPagpBpdusRx,
       "sapTlsL2ptStatsPagpBpdusTx": sapTlsL2ptStatsPagpBpdusTx,
       "sapTlsL2ptStatsUdldBpdusRx": sapTlsL2ptStatsUdldBpdusRx,
       "sapTlsL2ptStatsUdldBpdusTx": sapTlsL2ptStatsUdldBpdusTx,
       "sapEthernetInfoTable": sapEthernetInfoTable,
       "sapEthernetInfoEntry": sapEthernetInfoEntry,
       "sapEthernetLLFAdminStatus": sapEthernetLLFAdminStatus,
       "sapEthernetLLFOperStatus": sapEthernetLLFOperStatus,
       "msapPlcyTable": msapPlcyTable,
       "msapPlcyEntry": msapPlcyEntry,
       "msapPlcyName": msapPlcyName,
       "msapPlcyRowStatus": msapPlcyRowStatus,
       "msapPlcyLastChanged": msapPlcyLastChanged,
       "msapPlcyDescription": msapPlcyDescription,
       "msapPlcyCpmProtPolicyId": msapPlcyCpmProtPolicyId,
       "msapPlcyCpmProtMonitorMac": msapPlcyCpmProtMonitorMac,
       "msapPlcySubMgmtDefSubId": msapPlcySubMgmtDefSubId,
       "msapPlcySubMgmtDefSubIdStr": msapPlcySubMgmtDefSubIdStr,
       "msapPlcySubMgmtDefSubProfile": msapPlcySubMgmtDefSubProfile,
       "msapPlcySubMgmtDefSlaProfile": msapPlcySubMgmtDefSlaProfile,
       "msapPlcySubMgmtDefAppProfile": msapPlcySubMgmtDefAppProfile,
       "msapPlcySubMgmtSubIdPlcy": msapPlcySubMgmtSubIdPlcy,
       "msapPlcySubMgmtSubscriberLimit": msapPlcySubMgmtSubscriberLimit,
       "msapPlcySubMgmtProfiledTrafOnly": msapPlcySubMgmtProfiledTrafOnly,
       "msapPlcySubMgmtNonSubTrafSubId": msapPlcySubMgmtNonSubTrafSubId,
       "msapPlcySubMgmtNonSubTrafSubProf": msapPlcySubMgmtNonSubTrafSubProf,
       "msapPlcySubMgmtNonSubTrafSlaProf": msapPlcySubMgmtNonSubTrafSlaProf,
       "msapPlcySubMgmtNonSubTrafAppProf": msapPlcySubMgmtNonSubTrafAppProf,
       "msapPlcyAssociatedMsaps": msapPlcyAssociatedMsaps,
       "msapTlsPlcyTable": msapTlsPlcyTable,
       "msapTlsPlcyEntry": msapTlsPlcyEntry,
       "msapTlsPlcyLastChanged": msapTlsPlcyLastChanged,
       "msapTlsPlcySplitHorizonGrp": msapTlsPlcySplitHorizonGrp,
       "msapTlsPlcyArpReplyAgent": msapTlsPlcyArpReplyAgent,
       "msapTlsPlcySubMgmtMacDaHashing": msapTlsPlcySubMgmtMacDaHashing,
       "msapTlsPlcyDhcpLeasePopulate": msapTlsPlcyDhcpLeasePopulate,
       "msapTlsPlcyDhcpPrxyAdminState": msapTlsPlcyDhcpPrxyAdminState,
       "msapTlsPlcyDhcpPrxyServAddrType": msapTlsPlcyDhcpPrxyServAddrType,
       "msapTlsPlcyDhcpPrxyServAddr": msapTlsPlcyDhcpPrxyServAddr,
       "msapTlsPlcyDhcpPrxyLeaseTime": msapTlsPlcyDhcpPrxyLeaseTime,
       "msapTlsPlcyDhcpPrxyLTRadOverride": msapTlsPlcyDhcpPrxyLTRadOverride,
       "msapTlsPlcyDhcpInfoAction": msapTlsPlcyDhcpInfoAction,
       "msapTlsPlcyDhcpCircuitId": msapTlsPlcyDhcpCircuitId,
       "msapTlsPlcyDhcpRemoteId": msapTlsPlcyDhcpRemoteId,
       "msapTlsPlcyDhcpRemoteIdString": msapTlsPlcyDhcpRemoteIdString,
       "msapTlsPlcyDhcpVendorInclOpts": msapTlsPlcyDhcpVendorInclOpts,
       "msapTlsPlcyDhcpVendorOptStr": msapTlsPlcyDhcpVendorOptStr,
       "msapTlsPlcyEgressMcastGroup": msapTlsPlcyEgressMcastGroup,
       "msapTlsPlcyIgmpSnpgImportPlcy": msapTlsPlcyIgmpSnpgImportPlcy,
       "msapTlsPlcyIgmpSnpgFastLeave": msapTlsPlcyIgmpSnpgFastLeave,
       "msapTlsPlcyIgmpSnpgSendQueries": msapTlsPlcyIgmpSnpgSendQueries,
       "msapTlsPlcyIgmpSnpgGenQueryIntv": msapTlsPlcyIgmpSnpgGenQueryIntv,
       "msapTlsPlcyIgmpSnpgQueryRespIntv": msapTlsPlcyIgmpSnpgQueryRespIntv,
       "msapTlsPlcyIgmpSnpgRobustCount": msapTlsPlcyIgmpSnpgRobustCount,
       "msapTlsPlcyIgmpSnpgLastMembIntvl": msapTlsPlcyIgmpSnpgLastMembIntvl,
       "msapTlsPlcyIgmpSnpgMaxNbrGrps": msapTlsPlcyIgmpSnpgMaxNbrGrps,
       "msapTlsPlcyIgmpSnpgMvrFromVplsId": msapTlsPlcyIgmpSnpgMvrFromVplsId,
       "msapTlsPlcyIgmpSnpgVersion": msapTlsPlcyIgmpSnpgVersion,
       "msapTlsPlcyIgmpSnpgMcacPlcyName": msapTlsPlcyIgmpSnpgMcacPlcyName,
       "msapTlsPlcyIgmpSnpgMcacUncnstBW": msapTlsPlcyIgmpSnpgMcacUncnstBW,
       "msapTlsPlcyIgmpSnpgMcacPrRsvMnBW": msapTlsPlcyIgmpSnpgMcacPrRsvMnBW,
       "msapIgmpSnpgMcacLevelTable": msapIgmpSnpgMcacLevelTable,
       "msapIgmpSnpgMcacLevelEntry": msapIgmpSnpgMcacLevelEntry,
       "msapIgmpSnpgMcacLevelId": msapIgmpSnpgMcacLevelId,
       "msapIgmpSnpgMcacLevelRowStatus": msapIgmpSnpgMcacLevelRowStatus,
       "msapIgmpSnpgMcacLevelLastChanged": msapIgmpSnpgMcacLevelLastChanged,
       "msapIgmpSnpgMcacLevelBW": msapIgmpSnpgMcacLevelBW,
       "msapIgmpSnpgMcacLagTable": msapIgmpSnpgMcacLagTable,
       "msapIgmpSnpgMcacLagEntry": msapIgmpSnpgMcacLagEntry,
       "msapIgmpSnpgMcacLagPortsDown": msapIgmpSnpgMcacLagPortsDown,
       "msapIgmpSnpgMcacLagRowStatus": msapIgmpSnpgMcacLagRowStatus,
       "msapIgmpSnpgMcacLagLastChanged": msapIgmpSnpgMcacLagLastChanged,
       "msapIgmpSnpgMcacLagLevel": msapIgmpSnpgMcacLagLevel,
       "msapInfoTable": msapInfoTable,
       "msapInfoEntry": msapInfoEntry,
       "msapInfoCreationSapPortEncapVal": msapInfoCreationSapPortEncapVal,
       "msapInfoCreationPlcyName": msapInfoCreationPlcyName,
       "msapInfoReEvalPolicy": msapInfoReEvalPolicy,
       "msapInfoLastChanged": msapInfoLastChanged,
       "msapCaptureSapStatsTable": msapCaptureSapStatsTable,
       "msapCaptureSapStatsEntry": msapCaptureSapStatsEntry,
       "msapCaptureSapStatsTriggerType": msapCaptureSapStatsTriggerType,
       "msapCaptureSapStatsPktsRecvd": msapCaptureSapStatsPktsRecvd,
       "msapCaptureSapStatsPktsRedirect": msapCaptureSapStatsPktsRedirect,
       "msapCaptureSapStatsPktsDropped": msapCaptureSapStatsPktsDropped,
       "sapTlsMrpTable": sapTlsMrpTable,
       "sapTlsMrpEntry": sapTlsMrpEntry,
       "sapTlsMrpRxPdus": sapTlsMrpRxPdus,
       "sapTlsMrpDroppedPdus": sapTlsMrpDroppedPdus,
       "sapTlsMrpTxPdus": sapTlsMrpTxPdus,
       "sapTlsMrpRxNewEvent": sapTlsMrpRxNewEvent,
       "sapTlsMrpRxJoinInEvent": sapTlsMrpRxJoinInEvent,
       "sapTlsMrpRxInEvent": sapTlsMrpRxInEvent,
       "sapTlsMrpRxJoinEmptyEvent": sapTlsMrpRxJoinEmptyEvent,
       "sapTlsMrpRxEmptyEvent": sapTlsMrpRxEmptyEvent,
       "sapTlsMrpRxLeaveEvent": sapTlsMrpRxLeaveEvent,
       "sapTlsMrpTxNewEvent": sapTlsMrpTxNewEvent,
       "sapTlsMrpTxJoinInEvent": sapTlsMrpTxJoinInEvent,
       "sapTlsMrpTxInEvent": sapTlsMrpTxInEvent,
       "sapTlsMrpTxJoinEmptyEvent": sapTlsMrpTxJoinEmptyEvent,
       "sapTlsMrpTxEmptyEvent": sapTlsMrpTxEmptyEvent,
       "sapTlsMrpTxLeaveEvent": sapTlsMrpTxLeaveEvent,
       "sapTlsMmrpTable": sapTlsMmrpTable,
       "sapTlsMmrpEntry": sapTlsMmrpEntry,
       "sapTlsMmrpMacAddr": sapTlsMmrpMacAddr,
       "sapTlsMmrpDeclared": sapTlsMmrpDeclared,
       "sapTlsMmrpRegistered": sapTlsMmrpRegistered,
       "msapPlcyTblLastChgd": msapPlcyTblLastChgd,
       "msapTlsPlcyTblLastChgd": msapTlsPlcyTblLastChgd,
       "msapIgmpSnpgMcacLvlTblLastChgd": msapIgmpSnpgMcacLvlTblLastChgd,
       "msapIgmpSnpgMcacLagTblLastChgd": msapIgmpSnpgMcacLagTblLastChgd,
       "msapInfoTblLastChgd": msapInfoTblLastChgd,
       "tmnxSapNotifyObjs": tmnxSapNotifyObjs,
       "sapNotifyPortId": sapNotifyPortId,
       "msapStatus": msapStatus,
       "svcManagedSapCreationError": svcManagedSapCreationError,
       "sapTrapsPrefix": sapTrapsPrefix,
       "sapTraps": sapTraps,
       "sapCreated": sapCreated,
       "sapDeleted": sapDeleted,
       "sapStatusChanged": sapStatusChanged,
       "sapTlsMacAddrLimitAlarmRaised": sapTlsMacAddrLimitAlarmRaised,
       "sapTlsMacAddrLimitAlarmCleared": sapTlsMacAddrLimitAlarmCleared,
       "sapTlsDHCPLseStEntriesExceeded": sapTlsDHCPLseStEntriesExceeded,
       "sapTlsDHCPLeaseStateOverride": sapTlsDHCPLeaseStateOverride,
       "sapTlsDHCPSuspiciousPcktRcvd": sapTlsDHCPSuspiciousPcktRcvd,
       "sapDHCPLeaseEntriesExceeded": sapDHCPLeaseEntriesExceeded,
       "sapDHCPLseStateOverride": sapDHCPLseStateOverride,
       "sapDHCPSuspiciousPcktRcvd": sapDHCPSuspiciousPcktRcvd,
       "sapDHCPLseStatePopulateErr": sapDHCPLseStatePopulateErr,
       "hostConnectivityLost": hostConnectivityLost,
       "hostConnectivityRestored": hostConnectivityRestored,
       "sapReceivedProtSrcMac": sapReceivedProtSrcMac,
       "sapStaticHostDynMacConflict": sapStaticHostDynMacConflict,
       "sapTlsMacMoveExceeded": sapTlsMacMoveExceeded,
       "sapDHCPProxyServerError": sapDHCPProxyServerError,
       "sapDHCPCoAError": sapDHCPCoAError,
       "sapDHCPSubAuthError": sapDHCPSubAuthError,
       "sapPortStateChangeProcessed": sapPortStateChangeProcessed,
       "sapDHCPLseStateMobilityError": sapDHCPLseStateMobilityError,
       "sapCemPacketDefectAlarm": sapCemPacketDefectAlarm,
       "sapCemPacketDefectAlarmClear": sapCemPacketDefectAlarmClear,
       "msapStateChanged": msapStateChanged,
       "msapCreationFailure": msapCreationFailure,
       "topologyChangeSapMajorState": topologyChangeSapMajorState,
       "newRootSap": newRootSap,
       "topologyChangeSapState": topologyChangeSapState,
       "receivedTCN": receivedTCN,
       "higherPriorityBridge": higherPriorityBridge,
       "bridgedTLS": bridgedTLS,
       "sapEncapPVST": sapEncapPVST,
       "sapEncapDot1d": sapEncapDot1d,
       "sapReceiveOwnBpdu": sapReceiveOwnBpdu,
       "sapActiveProtocolChange": sapActiveProtocolChange,
       "tmnxStpRootGuardViolation": tmnxStpRootGuardViolation,
       "tmnxSapStpExcepCondStateChng": tmnxSapStpExcepCondStateChng}
)
