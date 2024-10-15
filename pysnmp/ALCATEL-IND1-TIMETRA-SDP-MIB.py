# SNMP MIB module (ALCATEL-IND1-TIMETRA-SDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-SDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:23 2024
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

(tmnxCardSlotNum,
 tmnxChassisIndex,
 tmnxMDASlotNum) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-CHASSIS-MIB",
    "tmnxCardSlotNum",
    "tmnxChassisIndex",
    "tmnxMDASlotNum")

(TFilterID,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-FILTER-MIB",
    "TFilterID")

(timetraSRMIBModules,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules")

(BridgeId,
 ConfigStatus,
 L2RouteOrigin,
 L2ptProtocols,
 LspIdList,
 MvplsPruneState,
 PWTemplateId,
 SdpBFHundredthsOfPercent,
 SdpBindBandwidth,
 SdpBindTlsBpduTranslation,
 SdpBindVcType,
 SdpId,
 ServObjDesc,
 ServObjName,
 StpExceptionCondition,
 StpPortRole,
 StpProtocol,
 TStpPortState,
 TdmOptionsCasTrunkFraming,
 TdmOptionsSigPkts,
 TlsLimitMacMove,
 TlsLimitMacMoveLevel,
 VpnId,
 custId,
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
 svcTlsStpDesignatedRoot,
 svcVpnId,
 tlsDhcpPacketProblem,
 tmnxCustomerBridgeId,
 tmnxCustomerRootBridgeId,
 tmnxOldSdpBindTlsStpPortState,
 tmnxOtherBridgeId,
 tmnxServConformance,
 tmnxServNotifications,
 tmnxServObjs,
 tmnxSvcObjs,
 tstpTraps) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    "BridgeId",
    "ConfigStatus",
    "L2RouteOrigin",
    "L2ptProtocols",
    "LspIdList",
    "MvplsPruneState",
    "PWTemplateId",
    "SdpBFHundredthsOfPercent",
    "SdpBindBandwidth",
    "SdpBindTlsBpduTranslation",
    "SdpBindVcType",
    "SdpId",
    "ServObjDesc",
    "ServObjName",
    "StpExceptionCondition",
    "StpPortRole",
    "StpProtocol",
    "TStpPortState",
    "TdmOptionsCasTrunkFraming",
    "TdmOptionsSigPkts",
    "TlsLimitMacMove",
    "TlsLimitMacMoveLevel",
    "VpnId",
    "custId",
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
    "svcTlsStpDesignatedRoot",
    "svcVpnId",
    "tlsDhcpPacketProblem",
    "tmnxCustomerBridgeId",
    "tmnxCustomerRootBridgeId",
    "tmnxOldSdpBindTlsStpPortState",
    "tmnxOtherBridgeId",
    "tmnxServConformance",
    "tmnxServNotifications",
    "tmnxServObjs",
    "tmnxSvcObjs",
    "tstpTraps")

(SdpBindId,
 ServiceAdminStatus,
 TItemDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxCustId,
 TmnxEnabledDisabled,
 TmnxIgmpVersion,
 TmnxOperState,
 TmnxServId,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrMplsLspID) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "SdpBindId",
    "ServiceAdminStatus",
    "TItemDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxCustId",
    "TmnxEnabledDisabled",
    "TmnxIgmpVersion",
    "TmnxOperState",
    "TmnxServId",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrMplsLspID")

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

timetraServicesSdpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 56)
)
timetraServicesSdpMIBModule.setRevisions(
        ("1907-10-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSdpConformance_ObjectIdentity = ObjectIdentity
tmnxSdpConformance = _TmnxSdpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4)
)
_TmnxSdpCompliances_ObjectIdentity = ObjectIdentity
tmnxSdpCompliances = _TmnxSdpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1)
)
_TmnxSdpGroups_ObjectIdentity = ObjectIdentity
tmnxSdpGroups = _TmnxSdpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2)
)
_SvcTlsBgpADPWTempBindTblLC_Type = TimeStamp
_SvcTlsBgpADPWTempBindTblLC_Object = MibScalar
svcTlsBgpADPWTempBindTblLC = _SvcTlsBgpADPWTempBindTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 32),
    _SvcTlsBgpADPWTempBindTblLC_Type()
)
svcTlsBgpADPWTempBindTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindTblLC.setStatus("current")
_SvcTlsBgpADPWTempBindTable_Object = MibTable
svcTlsBgpADPWTempBindTable = _SvcTlsBgpADPWTempBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33)
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindTable.setStatus("current")
_SvcTlsBgpADPWTempBindEntry_Object = MibTableRow
svcTlsBgpADPWTempBindEntry = _SvcTlsBgpADPWTempBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1)
)
svcTlsBgpADPWTempBindEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindEntry.setStatus("current")
_SvcTlsBgpADPWTempBindRowStatus_Type = RowStatus
_SvcTlsBgpADPWTempBindRowStatus_Object = MibTableColumn
svcTlsBgpADPWTempBindRowStatus = _SvcTlsBgpADPWTempBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 1),
    _SvcTlsBgpADPWTempBindRowStatus_Type()
)
svcTlsBgpADPWTempBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRowStatus.setStatus("current")
_SvcTlsBgpADPWTempBindLastChngd_Type = TimeStamp
_SvcTlsBgpADPWTempBindLastChngd_Object = MibTableColumn
svcTlsBgpADPWTempBindLastChngd = _SvcTlsBgpADPWTempBindLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 2),
    _SvcTlsBgpADPWTempBindLastChngd_Type()
)
svcTlsBgpADPWTempBindLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindLastChngd.setStatus("current")
_SvcTlsBgpADPWTempBindSHG_Type = TNamedItemOrEmpty
_SvcTlsBgpADPWTempBindSHG_Object = MibTableColumn
svcTlsBgpADPWTempBindSHG = _SvcTlsBgpADPWTempBindSHG_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 33, 1, 3),
    _SvcTlsBgpADPWTempBindSHG_Type()
)
svcTlsBgpADPWTempBindSHG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindSHG.setStatus("current")
_SvcTlsBgpADPWTempBindRTTblLC_Type = TimeStamp
_SvcTlsBgpADPWTempBindRTTblLC_Object = MibScalar
svcTlsBgpADPWTempBindRTTblLC = _SvcTlsBgpADPWTempBindRTTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 34),
    _SvcTlsBgpADPWTempBindRTTblLC_Type()
)
svcTlsBgpADPWTempBindRTTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTTblLC.setStatus("current")
_SvcTlsBgpADPWTempBindRTTable_Object = MibTable
svcTlsBgpADPWTempBindRTTable = _SvcTlsBgpADPWTempBindRTTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35)
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTTable.setStatus("current")
_SvcTlsBgpADPWTempBindRTEntry_Object = MibTableRow
svcTlsBgpADPWTempBindRTEntry = _SvcTlsBgpADPWTempBindRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1)
)
svcTlsBgpADPWTempBindRTEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateId"),
    (1, "ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRT"),
)
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTEntry.setStatus("current")
_SvcTlsBgpADPWTempBindRT_Type = TNamedItem
_SvcTlsBgpADPWTempBindRT_Object = MibTableColumn
svcTlsBgpADPWTempBindRT = _SvcTlsBgpADPWTempBindRT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1, 1),
    _SvcTlsBgpADPWTempBindRT_Type()
)
svcTlsBgpADPWTempBindRT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRT.setStatus("current")
_SvcTlsBgpADPWTempBindRTRowStat_Type = RowStatus
_SvcTlsBgpADPWTempBindRTRowStat_Object = MibTableColumn
svcTlsBgpADPWTempBindRTRowStat = _SvcTlsBgpADPWTempBindRTRowStat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 35, 1, 2),
    _SvcTlsBgpADPWTempBindRTRowStat_Type()
)
svcTlsBgpADPWTempBindRTRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    svcTlsBgpADPWTempBindRTRowStat.setStatus("current")
_SvcL2RteTableLastChanged_Type = TimeStamp
_SvcL2RteTableLastChanged_Object = MibScalar
svcL2RteTableLastChanged = _SvcL2RteTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 38),
    _SvcL2RteTableLastChanged_Type()
)
svcL2RteTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteTableLastChanged.setStatus("current")
_SvcL2RteTable_Object = MibTable
svcL2RteTable = _SvcL2RteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39)
)
if mibBuilder.loadTexts:
    svcL2RteTable.setStatus("current")
_SvcL2RteEntry_Object = MibTableRow
svcL2RteEntry = _SvcL2RteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1)
)
svcL2RteEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteVsiPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteRouteDistinguisher"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteNextHopType"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteNextHop"),
)
if mibBuilder.loadTexts:
    svcL2RteEntry.setStatus("current")
_SvcL2RteVsiPrefix_Type = Unsigned32
_SvcL2RteVsiPrefix_Object = MibTableColumn
svcL2RteVsiPrefix = _SvcL2RteVsiPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 1),
    _SvcL2RteVsiPrefix_Type()
)
svcL2RteVsiPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteVsiPrefix.setStatus("current")
_SvcL2RteRouteDistinguisher_Type = TmnxVPNRouteDistinguisher
_SvcL2RteRouteDistinguisher_Object = MibTableColumn
svcL2RteRouteDistinguisher = _SvcL2RteRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 2),
    _SvcL2RteRouteDistinguisher_Type()
)
svcL2RteRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteRouteDistinguisher.setStatus("current")
_SvcL2RteNextHopType_Type = InetAddressType
_SvcL2RteNextHopType_Object = MibTableColumn
svcL2RteNextHopType = _SvcL2RteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 3),
    _SvcL2RteNextHopType_Type()
)
svcL2RteNextHopType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteNextHopType.setStatus("current")
_SvcL2RteNextHop_Type = InetAddress
_SvcL2RteNextHop_Object = MibTableColumn
svcL2RteNextHop = _SvcL2RteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 4),
    _SvcL2RteNextHop_Type()
)
svcL2RteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    svcL2RteNextHop.setStatus("current")
_SvcL2RteSdpBindId_Type = SdpBindId
_SvcL2RteSdpBindId_Object = MibTableColumn
svcL2RteSdpBindId = _SvcL2RteSdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 5),
    _SvcL2RteSdpBindId_Type()
)
svcL2RteSdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RteSdpBindId.setStatus("current")
_SvcL2RtePwTemplateId_Type = PWTemplateId
_SvcL2RtePwTemplateId_Object = MibTableColumn
svcL2RtePwTemplateId = _SvcL2RtePwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 2, 39, 1, 6),
    _SvcL2RtePwTemplateId_Type()
)
svcL2RtePwTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svcL2RtePwTemplateId.setStatus("current")
_TmnxSdpObjs_ObjectIdentity = ObjectIdentity
tmnxSdpObjs = _TmnxSdpObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4)
)
_SdpNumEntries_Type = Integer32
_SdpNumEntries_Object = MibScalar
sdpNumEntries = _SdpNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 1),
    _SdpNumEntries_Type()
)
sdpNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNumEntries.setStatus("current")
_SdpNextFreeId_Type = SdpId
_SdpNextFreeId_Object = MibScalar
sdpNextFreeId = _SdpNextFreeId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 2),
    _SdpNextFreeId_Type()
)
sdpNextFreeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpNextFreeId.setStatus("current")
_SdpInfoTable_Object = MibTable
sdpInfoTable = _SdpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3)
)
if mibBuilder.loadTexts:
    sdpInfoTable.setStatus("current")
_SdpInfoEntry_Object = MibTableRow
sdpInfoEntry = _SdpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1)
)
sdpInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
)
if mibBuilder.loadTexts:
    sdpInfoEntry.setStatus("current")
_SdpId_Type = SdpId
_SdpId_Object = MibTableColumn
sdpId = _SdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 1),
    _SdpId_Type()
)
sdpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpId.setStatus("current")
_SdpRowStatus_Type = RowStatus
_SdpRowStatus_Object = MibTableColumn
sdpRowStatus = _SdpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 2),
    _SdpRowStatus_Type()
)
sdpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpRowStatus.setStatus("current")


class _SdpDelivery_Type(Integer32):
    """Custom type sdpDelivery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gre", 1),
          ("mpls", 2))
    )


_SdpDelivery_Type.__name__ = "Integer32"
_SdpDelivery_Object = MibTableColumn
sdpDelivery = _SdpDelivery_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 3),
    _SdpDelivery_Type()
)
sdpDelivery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDelivery.setStatus("current")
_SdpFarEndIpAddress_Type = IpAddress
_SdpFarEndIpAddress_Object = MibTableColumn
sdpFarEndIpAddress = _SdpFarEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 4),
    _SdpFarEndIpAddress_Type()
)
sdpFarEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFarEndIpAddress.setStatus("current")
_SdpLspList_Type = LspIdList
_SdpLspList_Object = MibTableColumn
sdpLspList = _SdpLspList_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 5),
    _SdpLspList_Type()
)
sdpLspList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLspList.setStatus("current")
_SdpDescription_Type = ServObjDesc
_SdpDescription_Object = MibTableColumn
sdpDescription = _SdpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 6),
    _SdpDescription_Type()
)
sdpDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpDescription.setStatus("current")


class _SdpLabelSignaling_Type(Integer32):
    """Custom type sdpLabelSignaling based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tldp", 2))
    )


_SdpLabelSignaling_Type.__name__ = "Integer32"
_SdpLabelSignaling_Object = MibTableColumn
sdpLabelSignaling = _SdpLabelSignaling_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 7),
    _SdpLabelSignaling_Type()
)
sdpLabelSignaling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLabelSignaling.setStatus("current")


class _SdpAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpAdminStatus based on ServiceAdminStatus"""


_SdpAdminStatus_Object = MibTableColumn
sdpAdminStatus = _SdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 8),
    _SdpAdminStatus_Type()
)
sdpAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminStatus.setStatus("current")


class _SdpOperStatus_Type(Integer32):
    """Custom type sdpOperStatus based on Integer32"""
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
        *(("down", 6),
          ("invalidEgressInterface", 4),
          ("notAlive", 2),
          ("notReady", 3),
          ("transportTunnelDown", 5),
          ("up", 1))
    )


_SdpOperStatus_Type.__name__ = "Integer32"
_SdpOperStatus_Object = MibTableColumn
sdpOperStatus = _SdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 9),
    _SdpOperStatus_Type()
)
sdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperStatus.setStatus("current")


class _SdpAdminPathMtu_Type(Integer32):
    """Custom type sdpAdminPathMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(576, 9194),
    )


_SdpAdminPathMtu_Type.__name__ = "Integer32"
_SdpAdminPathMtu_Object = MibTableColumn
sdpAdminPathMtu = _SdpAdminPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 10),
    _SdpAdminPathMtu_Type()
)
sdpAdminPathMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdminPathMtu.setStatus("current")
_SdpOperPathMtu_Type = Integer32
_SdpOperPathMtu_Object = MibTableColumn
sdpOperPathMtu = _SdpOperPathMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 11),
    _SdpOperPathMtu_Type()
)
sdpOperPathMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperPathMtu.setStatus("current")


class _SdpKeepAliveAdminStatus_Type(Integer32):
    """Custom type sdpKeepAliveAdminStatus based on Integer32"""
    defaultValue = 2

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


_SdpKeepAliveAdminStatus_Type.__name__ = "Integer32"
_SdpKeepAliveAdminStatus_Object = MibTableColumn
sdpKeepAliveAdminStatus = _SdpKeepAliveAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 12),
    _SdpKeepAliveAdminStatus_Type()
)
sdpKeepAliveAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveAdminStatus.setStatus("current")


class _SdpKeepAliveOperStatus_Type(Integer32):
    """Custom type sdpKeepAliveOperStatus based on Integer32"""
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
        *(("alive", 1),
          ("disabled", 5),
          ("noResponse", 2),
          ("responderIdError", 4),
          ("senderIdInvalid", 3))
    )


_SdpKeepAliveOperStatus_Type.__name__ = "Integer32"
_SdpKeepAliveOperStatus_Object = MibTableColumn
sdpKeepAliveOperStatus = _SdpKeepAliveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 13),
    _SdpKeepAliveOperStatus_Type()
)
sdpKeepAliveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveOperStatus.setStatus("current")


class _SdpKeepAliveHelloTime_Type(Integer32):
    """Custom type sdpKeepAliveHelloTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SdpKeepAliveHelloTime_Type.__name__ = "Integer32"
_SdpKeepAliveHelloTime_Object = MibTableColumn
sdpKeepAliveHelloTime = _SdpKeepAliveHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 14),
    _SdpKeepAliveHelloTime_Type()
)
sdpKeepAliveHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloTime.setStatus("current")


class _SdpKeepAliveMaxDropCount_Type(Integer32):
    """Custom type sdpKeepAliveMaxDropCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SdpKeepAliveMaxDropCount_Type.__name__ = "Integer32"
_SdpKeepAliveMaxDropCount_Object = MibTableColumn
sdpKeepAliveMaxDropCount = _SdpKeepAliveMaxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 15),
    _SdpKeepAliveMaxDropCount_Type()
)
sdpKeepAliveMaxDropCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveMaxDropCount.setStatus("current")


class _SdpKeepAliveHoldDownTime_Type(Integer32):
    """Custom type sdpKeepAliveHoldDownTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_SdpKeepAliveHoldDownTime_Type.__name__ = "Integer32"
_SdpKeepAliveHoldDownTime_Object = MibTableColumn
sdpKeepAliveHoldDownTime = _SdpKeepAliveHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 16),
    _SdpKeepAliveHoldDownTime_Type()
)
sdpKeepAliveHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHoldDownTime.setStatus("current")
_SdpLastMgmtChange_Type = TimeStamp
_SdpLastMgmtChange_Object = MibTableColumn
sdpLastMgmtChange = _SdpLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 17),
    _SdpLastMgmtChange_Type()
)
sdpLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastMgmtChange.setStatus("current")


class _SdpKeepAliveHelloMessageLength_Type(Integer32):
    """Custom type sdpKeepAliveHelloMessageLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(40, 9198),
    )


_SdpKeepAliveHelloMessageLength_Type.__name__ = "Integer32"
_SdpKeepAliveHelloMessageLength_Object = MibTableColumn
sdpKeepAliveHelloMessageLength = _SdpKeepAliveHelloMessageLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 18),
    _SdpKeepAliveHelloMessageLength_Type()
)
sdpKeepAliveHelloMessageLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloMessageLength.setStatus("current")
_SdpKeepAliveNumHelloRequestMessages_Type = Unsigned32
_SdpKeepAliveNumHelloRequestMessages_Object = MibTableColumn
sdpKeepAliveNumHelloRequestMessages = _SdpKeepAliveNumHelloRequestMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 19),
    _SdpKeepAliveNumHelloRequestMessages_Type()
)
sdpKeepAliveNumHelloRequestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloRequestMessages.setStatus("current")
_SdpKeepAliveNumHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumHelloResponseMessages = _SdpKeepAliveNumHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 20),
    _SdpKeepAliveNumHelloResponseMessages_Type()
)
sdpKeepAliveNumHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumHelloResponseMessages.setStatus("current")
_SdpKeepAliveNumLateHelloResponseMessages_Type = Unsigned32
_SdpKeepAliveNumLateHelloResponseMessages_Object = MibTableColumn
sdpKeepAliveNumLateHelloResponseMessages = _SdpKeepAliveNumLateHelloResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 21),
    _SdpKeepAliveNumLateHelloResponseMessages_Type()
)
sdpKeepAliveNumLateHelloResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpKeepAliveNumLateHelloResponseMessages.setStatus("current")


class _SdpKeepAliveHelloRequestTimeout_Type(Integer32):
    """Custom type sdpKeepAliveHelloRequestTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SdpKeepAliveHelloRequestTimeout_Type.__name__ = "Integer32"
_SdpKeepAliveHelloRequestTimeout_Object = MibTableColumn
sdpKeepAliveHelloRequestTimeout = _SdpKeepAliveHelloRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 22),
    _SdpKeepAliveHelloRequestTimeout_Type()
)
sdpKeepAliveHelloRequestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpKeepAliveHelloRequestTimeout.setStatus("current")


class _SdpLdpEnabled_Type(TruthValue):
    """Custom type sdpLdpEnabled based on TruthValue"""


_SdpLdpEnabled_Object = MibTableColumn
sdpLdpEnabled = _SdpLdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 23),
    _SdpLdpEnabled_Type()
)
sdpLdpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpLdpEnabled.setStatus("current")


class _SdpVlanVcEtype_Type(Unsigned32):
    """Custom type sdpVlanVcEtype based on Unsigned32"""
    defaultHexValue = 33024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpVlanVcEtype_Type.__name__ = "Unsigned32"
_SdpVlanVcEtype_Object = MibTableColumn
sdpVlanVcEtype = _SdpVlanVcEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 24),
    _SdpVlanVcEtype_Type()
)
sdpVlanVcEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpVlanVcEtype.setStatus("current")


class _SdpAdvertisedVllMtuOverride_Type(TruthValue):
    """Custom type sdpAdvertisedVllMtuOverride based on TruthValue"""


_SdpAdvertisedVllMtuOverride_Object = MibTableColumn
sdpAdvertisedVllMtuOverride = _SdpAdvertisedVllMtuOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 25),
    _SdpAdvertisedVllMtuOverride_Type()
)
sdpAdvertisedVllMtuOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAdvertisedVllMtuOverride.setStatus("current")


class _SdpOperFlags_Type(Bits):
    """Custom type sdpOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("invalidEgressInterface", 4),
          ("keepaliveFailure", 3),
          ("noSystemIpAddress", 5),
          ("sdpAdminDown", 0),
          ("signalingSessionDown", 1),
          ("transportTunnelDown", 2),
          ("transportTunnelUnstable", 6))
    )

_SdpOperFlags_Type.__name__ = "Bits"
_SdpOperFlags_Object = MibTableColumn
sdpOperFlags = _SdpOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 26),
    _SdpOperFlags_Type()
)
sdpOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperFlags.setStatus("current")
_SdpLastStatusChange_Type = TimeStamp
_SdpLastStatusChange_Object = MibTableColumn
sdpLastStatusChange = _SdpLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 27),
    _SdpLastStatusChange_Type()
)
sdpLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpLastStatusChange.setStatus("current")
_SdpMvplsMgmtService_Type = TmnxServId
_SdpMvplsMgmtService_Object = MibTableColumn
sdpMvplsMgmtService = _SdpMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 28),
    _SdpMvplsMgmtService_Type()
)
sdpMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtService.setStatus("current")
_SdpMvplsMgmtSdpBndId_Type = SdpBindId
_SdpMvplsMgmtSdpBndId_Object = MibTableColumn
sdpMvplsMgmtSdpBndId = _SdpMvplsMgmtSdpBndId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 29),
    _SdpMvplsMgmtSdpBndId_Type()
)
sdpMvplsMgmtSdpBndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpMvplsMgmtSdpBndId.setStatus("current")


class _SdpCollectAcctStats_Type(TruthValue):
    """Custom type sdpCollectAcctStats based on TruthValue"""


_SdpCollectAcctStats_Object = MibTableColumn
sdpCollectAcctStats = _SdpCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 30),
    _SdpCollectAcctStats_Type()
)
sdpCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpCollectAcctStats.setStatus("current")


class _SdpAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_SdpAccountingPolicyId_Object = MibTableColumn
sdpAccountingPolicyId = _SdpAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 31),
    _SdpAccountingPolicyId_Type()
)
sdpAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpAccountingPolicyId.setStatus("current")


class _SdpClassFwdingEnabled_Type(TruthValue):
    """Custom type sdpClassFwdingEnabled based on TruthValue"""


_SdpClassFwdingEnabled_Object = MibTableColumn
sdpClassFwdingEnabled = _SdpClassFwdingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 32),
    _SdpClassFwdingEnabled_Type()
)
sdpClassFwdingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingEnabled.setStatus("current")


class _SdpClassFwdingDefaultLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingDefaultLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingDefaultLsp_Object = MibTableColumn
sdpClassFwdingDefaultLsp = _SdpClassFwdingDefaultLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 33),
    _SdpClassFwdingDefaultLsp_Type()
)
sdpClassFwdingDefaultLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingDefaultLsp.setStatus("current")


class _SdpClassFwdingMcLsp_Type(TmnxVRtrMplsLspID):
    """Custom type sdpClassFwdingMcLsp based on TmnxVRtrMplsLspID"""
    defaultValue = 0


_SdpClassFwdingMcLsp_Object = MibTableColumn
sdpClassFwdingMcLsp = _SdpClassFwdingMcLsp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 34),
    _SdpClassFwdingMcLsp_Type()
)
sdpClassFwdingMcLsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpClassFwdingMcLsp.setStatus("current")


class _SdpMetric_Type(Unsigned32):
    """Custom type sdpMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SdpMetric_Type.__name__ = "Unsigned32"
_SdpMetric_Object = MibTableColumn
sdpMetric = _SdpMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 35),
    _SdpMetric_Type()
)
sdpMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpMetric.setStatus("current")
_SdpAutoSdp_Type = TruthValue
_SdpAutoSdp_Object = MibTableColumn
sdpAutoSdp = _SdpAutoSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 36),
    _SdpAutoSdp_Type()
)
sdpAutoSdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoSdp.setStatus("current")
_SdpSnmpAllowed_Type = TruthValue
_SdpSnmpAllowed_Object = MibTableColumn
sdpSnmpAllowed = _SdpSnmpAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 37),
    _SdpSnmpAllowed_Type()
)
sdpSnmpAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpSnmpAllowed.setStatus("current")


class _SdpPBBEtype_Type(Unsigned32):
    """Custom type sdpPBBEtype based on Unsigned32"""
    defaultHexValue = 35047

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_SdpPBBEtype_Type.__name__ = "Unsigned32"
_SdpPBBEtype_Object = MibTableColumn
sdpPBBEtype = _SdpPBBEtype_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 38),
    _SdpPBBEtype_Type()
)
sdpPBBEtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpPBBEtype.setStatus("current")


class _SdpBandwidthBookingFactor_Type(Unsigned32):
    """Custom type sdpBandwidthBookingFactor based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SdpBandwidthBookingFactor_Type.__name__ = "Unsigned32"
_SdpBandwidthBookingFactor_Object = MibTableColumn
sdpBandwidthBookingFactor = _SdpBandwidthBookingFactor_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 39),
    _SdpBandwidthBookingFactor_Type()
)
sdpBandwidthBookingFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBandwidthBookingFactor.setStatus("current")
_SdpOperBandwidth_Type = Unsigned32
_SdpOperBandwidth_Object = MibTableColumn
sdpOperBandwidth = _SdpOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 40),
    _SdpOperBandwidth_Type()
)
sdpOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpOperBandwidth.setUnits("kilo-bits per second")
_SdpAvailableBandwidth_Type = Unsigned32
_SdpAvailableBandwidth_Object = MibTableColumn
sdpAvailableBandwidth = _SdpAvailableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 41),
    _SdpAvailableBandwidth_Type()
)
sdpAvailableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpAvailableBandwidth.setUnits("kilo-bits per second")
_SdpMaxBookableBandwidth_Type = Unsigned32
_SdpMaxBookableBandwidth_Object = MibTableColumn
sdpMaxBookableBandwidth = _SdpMaxBookableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 42),
    _SdpMaxBookableBandwidth_Type()
)
sdpMaxBookableBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpMaxBookableBandwidth.setUnits("kilo-bits per second")
_SdpBookedBandwidth_Type = Unsigned32
_SdpBookedBandwidth_Object = MibTableColumn
sdpBookedBandwidth = _SdpBookedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 43),
    _SdpBookedBandwidth_Type()
)
sdpBookedBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBookedBandwidth.setUnits("kilo-bits per second")
_SdpCreationOrigin_Type = L2RouteOrigin
_SdpCreationOrigin_Object = MibTableColumn
sdpCreationOrigin = _SdpCreationOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 3, 1, 44),
    _SdpCreationOrigin_Type()
)
sdpCreationOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpCreationOrigin.setStatus("current")
_SdpBindTable_Object = MibTable
sdpBindTable = _SdpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4)
)
if mibBuilder.loadTexts:
    sdpBindTable.setStatus("current")
_SdpBindEntry_Object = MibTableRow
sdpBindEntry = _SdpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1)
)
sdpBindEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindEntry.setStatus("current")
_SdpBindId_Type = SdpBindId
_SdpBindId_Object = MibTableColumn
sdpBindId = _SdpBindId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 1),
    _SdpBindId_Type()
)
sdpBindId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindId.setStatus("current")
_SdpBindRowStatus_Type = RowStatus
_SdpBindRowStatus_Object = MibTableColumn
sdpBindRowStatus = _SdpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 2),
    _SdpBindRowStatus_Type()
)
sdpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindRowStatus.setStatus("current")


class _SdpBindAdminIngressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2048, 18431),
    )


_SdpBindAdminIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminIngressLabel_Object = MibTableColumn
sdpBindAdminIngressLabel = _SdpBindAdminIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 3),
    _SdpBindAdminIngressLabel_Type()
)
sdpBindAdminIngressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminIngressLabel.setStatus("current")


class _SdpBindAdminEgressLabel_Type(Unsigned32):
    """Custom type sdpBindAdminEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 1048575),
    )


_SdpBindAdminEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindAdminEgressLabel_Object = MibTableColumn
sdpBindAdminEgressLabel = _SdpBindAdminEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 4),
    _SdpBindAdminEgressLabel_Type()
)
sdpBindAdminEgressLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminEgressLabel.setStatus("current")


class _SdpBindOperIngressLabel_Type(Unsigned32):
    """Custom type sdpBindOperIngressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperIngressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperIngressLabel_Object = MibTableColumn
sdpBindOperIngressLabel = _SdpBindOperIngressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 5),
    _SdpBindOperIngressLabel_Type()
)
sdpBindOperIngressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperIngressLabel.setStatus("current")


class _SdpBindOperEgressLabel_Type(Unsigned32):
    """Custom type sdpBindOperEgressLabel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1048575),
    )


_SdpBindOperEgressLabel_Type.__name__ = "Unsigned32"
_SdpBindOperEgressLabel_Object = MibTableColumn
sdpBindOperEgressLabel = _SdpBindOperEgressLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 6),
    _SdpBindOperEgressLabel_Type()
)
sdpBindOperEgressLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperEgressLabel.setStatus("current")


class _SdpBindAdminStatus_Type(ServiceAdminStatus):
    """Custom type sdpBindAdminStatus based on ServiceAdminStatus"""


_SdpBindAdminStatus_Object = MibTableColumn
sdpBindAdminStatus = _SdpBindAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 7),
    _SdpBindAdminStatus_Type()
)
sdpBindAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminStatus.setStatus("current")


class _SdpBindOperStatus_Type(Integer32):
    """Custom type sdpBindOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("down", 5),
          ("noEgressLabel", 2),
          ("noIngressLabel", 3),
          ("noLabels", 4),
          ("sapDown", 10),
          ("sdpDown", 9),
          ("sdpNotReady", 8),
          ("sdpPathMtuTooSmall", 7),
          ("svcMtuMismatch", 6),
          ("up", 1))
    )


_SdpBindOperStatus_Type.__name__ = "Integer32"
_SdpBindOperStatus_Object = MibTableColumn
sdpBindOperStatus = _SdpBindOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 8),
    _SdpBindOperStatus_Type()
)
sdpBindOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperStatus.setStatus("current")
_SdpBindLastMgmtChange_Type = TimeStamp
_SdpBindLastMgmtChange_Object = MibTableColumn
sdpBindLastMgmtChange = _SdpBindLastMgmtChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 9),
    _SdpBindLastMgmtChange_Type()
)
sdpBindLastMgmtChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastMgmtChange.setStatus("current")


class _SdpBindType_Type(Integer32):
    """Custom type sdpBindType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 2),
          ("spoke", 1))
    )


_SdpBindType_Type.__name__ = "Integer32"
_SdpBindType_Object = MibTableColumn
sdpBindType = _SdpBindType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 10),
    _SdpBindType_Type()
)
sdpBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindType.setStatus("current")


class _SdpBindIngressMacFilterId_Type(TFilterID):
    """Custom type sdpBindIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressMacFilterId_Object = MibTableColumn
sdpBindIngressMacFilterId = _SdpBindIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 11),
    _SdpBindIngressMacFilterId_Type()
)
sdpBindIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressMacFilterId.setStatus("current")


class _SdpBindIngressIpFilterId_Type(TFilterID):
    """Custom type sdpBindIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressIpFilterId_Object = MibTableColumn
sdpBindIngressIpFilterId = _SdpBindIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 12),
    _SdpBindIngressIpFilterId_Type()
)
sdpBindIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpFilterId.setStatus("current")


class _SdpBindEgressMacFilterId_Type(TFilterID):
    """Custom type sdpBindEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressMacFilterId_Object = MibTableColumn
sdpBindEgressMacFilterId = _SdpBindEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 13),
    _SdpBindEgressMacFilterId_Type()
)
sdpBindEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressMacFilterId.setStatus("current")


class _SdpBindEgressIpFilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpFilterId_Object = MibTableColumn
sdpBindEgressIpFilterId = _SdpBindEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 14),
    _SdpBindEgressIpFilterId_Type()
)
sdpBindEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpFilterId.setStatus("current")
_SdpBindVpnId_Type = VpnId
_SdpBindVpnId_Object = MibTableColumn
sdpBindVpnId = _SdpBindVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 15),
    _SdpBindVpnId_Type()
)
sdpBindVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindVpnId.setStatus("current")
_SdpBindCustId_Type = TmnxCustId
_SdpBindCustId_Object = MibTableColumn
sdpBindCustId = _SdpBindCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 16),
    _SdpBindCustId_Type()
)
sdpBindCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCustId.setStatus("current")
_SdpBindVcType_Type = SdpBindVcType
_SdpBindVcType_Object = MibTableColumn
sdpBindVcType = _SdpBindVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 17),
    _SdpBindVcType_Type()
)
sdpBindVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVcType.setStatus("current")


class _SdpBindVlanVcTag_Type(Unsigned32):
    """Custom type sdpBindVlanVcTag based on Unsigned32"""
    defaultHexValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SdpBindVlanVcTag_Type.__name__ = "Unsigned32"
_SdpBindVlanVcTag_Object = MibTableColumn
sdpBindVlanVcTag = _SdpBindVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 18),
    _SdpBindVlanVcTag_Type()
)
sdpBindVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindVlanVcTag.setStatus("current")
_SdpBindSplitHorizonGrp_Type = ServObjName
_SdpBindSplitHorizonGrp_Object = MibTableColumn
sdpBindSplitHorizonGrp = _SdpBindSplitHorizonGrp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 19),
    _SdpBindSplitHorizonGrp_Type()
)
sdpBindSplitHorizonGrp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindSplitHorizonGrp.setStatus("current")


class _SdpBindOperFlags_Type(Bits):
    """Custom type sdpBindOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("iesIfAdminDown", 10),
          ("insufficientBandwidth", 14),
          ("labelsExhausted", 12),
          ("meshSdpDown", 16),
          ("noEgressVcLabel", 6),
          ("noIngressVcLabel", 5),
          ("pwPeerFaultStatusBits", 15),
          ("relearnLimitExceeded", 9),
          ("releasedIngressVcLabel", 11),
          ("sapOperDown", 2),
          ("sdpBindAdminDown", 0),
          ("sdpOperDown", 3),
          ("sdpPathMtuTooSmall", 4),
          ("svcAdminDown", 1),
          ("svcMtuMismatch", 7),
          ("svcParamMismatch", 13),
          ("vcTypeMismatch", 8))
    )

_SdpBindOperFlags_Type.__name__ = "Bits"
_SdpBindOperFlags_Object = MibTableColumn
sdpBindOperFlags = _SdpBindOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 20),
    _SdpBindOperFlags_Type()
)
sdpBindOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperFlags.setStatus("current")
_SdpBindLastStatusChange_Type = TimeStamp
_SdpBindLastStatusChange_Object = MibTableColumn
sdpBindLastStatusChange = _SdpBindLastStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 21),
    _SdpBindLastStatusChange_Type()
)
sdpBindLastStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindLastStatusChange.setStatus("current")
_SdpBindIesIfIndex_Type = InterfaceIndexOrZero
_SdpBindIesIfIndex_Object = MibTableColumn
sdpBindIesIfIndex = _SdpBindIesIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 22),
    _SdpBindIesIfIndex_Type()
)
sdpBindIesIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIesIfIndex.setStatus("current")
_SdpBindMacPinning_Type = TmnxEnabledDisabled
_SdpBindMacPinning_Object = MibTableColumn
sdpBindMacPinning = _SdpBindMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 23),
    _SdpBindMacPinning_Type()
)
sdpBindMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindMacPinning.setStatus("current")


class _SdpBindIngressIpv6FilterId_Type(TFilterID):
    """Custom type sdpBindIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SdpBindIngressIpv6FilterId_Object = MibTableColumn
sdpBindIngressIpv6FilterId = _SdpBindIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 24),
    _SdpBindIngressIpv6FilterId_Type()
)
sdpBindIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIngressIpv6FilterId.setStatus("current")


class _SdpBindEgressIpv6FilterId_Type(TFilterID):
    """Custom type sdpBindEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_SdpBindEgressIpv6FilterId_Object = MibTableColumn
sdpBindEgressIpv6FilterId = _SdpBindEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 25),
    _SdpBindEgressIpv6FilterId_Type()
)
sdpBindEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEgressIpv6FilterId.setStatus("current")


class _SdpBindCollectAcctStats_Type(TruthValue):
    """Custom type sdpBindCollectAcctStats based on TruthValue"""


_SdpBindCollectAcctStats_Object = MibTableColumn
sdpBindCollectAcctStats = _SdpBindCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 26),
    _SdpBindCollectAcctStats_Type()
)
sdpBindCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindCollectAcctStats.setStatus("current")


class _SdpBindAccountingPolicyId_Type(Unsigned32):
    """Custom type sdpBindAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_SdpBindAccountingPolicyId_Object = MibTableColumn
sdpBindAccountingPolicyId = _SdpBindAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 27),
    _SdpBindAccountingPolicyId_Type()
)
sdpBindAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAccountingPolicyId.setStatus("current")


class _SdpBindPwPeerStatusBits_Type(Bits):
    """Custom type sdpBindPwPeerStatusBits based on Bits"""
    namedValues = NamedValues(
        *(("lacEgresssFault", 2),
          ("lacIngressFault", 1),
          ("psnEgressFault", 4),
          ("psnIngressFault", 3),
          ("pwFwdingStandby", 5),
          ("pwNotForwarding", 0))
    )

_SdpBindPwPeerStatusBits_Type.__name__ = "Bits"
_SdpBindPwPeerStatusBits_Object = MibTableColumn
sdpBindPwPeerStatusBits = _SdpBindPwPeerStatusBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 28),
    _SdpBindPwPeerStatusBits_Type()
)
sdpBindPwPeerStatusBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwPeerStatusBits.setStatus("current")


class _SdpBindPeerVccvCvBits_Type(Bits):
    """Custom type sdpBindPeerVccvCvBits based on Bits"""
    namedValues = NamedValues(
        *(("bfdFaultDetection", 2),
          ("bfdFaultDetectionAndSignalling", 3),
          ("icmpPing", 0),
          ("lspPing", 1))
    )

_SdpBindPeerVccvCvBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCvBits_Object = MibTableColumn
sdpBindPeerVccvCvBits = _SdpBindPeerVccvCvBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 29),
    _SdpBindPeerVccvCvBits_Type()
)
sdpBindPeerVccvCvBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCvBits.setStatus("current")


class _SdpBindPeerVccvCcBits_Type(Bits):
    """Custom type sdpBindPeerVccvCcBits based on Bits"""
    namedValues = NamedValues(
        *(("mplsPwDemultiplexorLabel", 2),
          ("mplsRouterAlertLabel", 1),
          ("pwe3ControlWord", 0))
    )

_SdpBindPeerVccvCcBits_Type.__name__ = "Bits"
_SdpBindPeerVccvCcBits_Object = MibTableColumn
sdpBindPeerVccvCcBits = _SdpBindPeerVccvCcBits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 30),
    _SdpBindPeerVccvCcBits_Type()
)
sdpBindPeerVccvCcBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPeerVccvCcBits.setStatus("current")
_SdpBindControlWordBit_Type = TruthValue
_SdpBindControlWordBit_Object = MibTableColumn
sdpBindControlWordBit = _SdpBindControlWordBit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 31),
    _SdpBindControlWordBit_Type()
)
sdpBindControlWordBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindControlWordBit.setStatus("current")
_SdpBindOperControlWord_Type = TruthValue
_SdpBindOperControlWord_Object = MibTableColumn
sdpBindOperControlWord = _SdpBindOperControlWord_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 32),
    _SdpBindOperControlWord_Type()
)
sdpBindOperControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperControlWord.setStatus("current")
_SdpBindEndPoint_Type = ServObjName
_SdpBindEndPoint_Object = MibTableColumn
sdpBindEndPoint = _SdpBindEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 33),
    _SdpBindEndPoint_Type()
)
sdpBindEndPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPoint.setStatus("current")


class _SdpBindEndPointPrecedence_Type(Unsigned32):
    """Custom type sdpBindEndPointPrecedence based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_SdpBindEndPointPrecedence_Type.__name__ = "Unsigned32"
_SdpBindEndPointPrecedence_Object = MibTableColumn
sdpBindEndPointPrecedence = _SdpBindEndPointPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 34),
    _SdpBindEndPointPrecedence_Type()
)
sdpBindEndPointPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindEndPointPrecedence.setStatus("current")


class _SdpBindIsICB_Type(TruthValue):
    """Custom type sdpBindIsICB based on TruthValue"""


_SdpBindIsICB_Object = MibTableColumn
sdpBindIsICB = _SdpBindIsICB_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 35),
    _SdpBindIsICB_Type()
)
sdpBindIsICB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindIsICB.setStatus("current")
_SdpBindPwFaultInetAddressType_Type = InetAddressType
_SdpBindPwFaultInetAddressType_Object = MibTableColumn
sdpBindPwFaultInetAddressType = _SdpBindPwFaultInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 36),
    _SdpBindPwFaultInetAddressType_Type()
)
sdpBindPwFaultInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddressType.setStatus("current")


class _SdpBindPwFaultInetAddress_Type(InetAddress):
    """Custom type sdpBindPwFaultInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_SdpBindPwFaultInetAddress_Type.__name__ = "InetAddress"
_SdpBindPwFaultInetAddress_Object = MibTableColumn
sdpBindPwFaultInetAddress = _SdpBindPwFaultInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 37),
    _SdpBindPwFaultInetAddress_Type()
)
sdpBindPwFaultInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindPwFaultInetAddress.setStatus("current")
_SdpBindClassFwdingOperState_Type = TmnxOperState
_SdpBindClassFwdingOperState_Object = MibTableColumn
sdpBindClassFwdingOperState = _SdpBindClassFwdingOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 38),
    _SdpBindClassFwdingOperState_Type()
)
sdpBindClassFwdingOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindClassFwdingOperState.setStatus("current")


class _SdpBindForceVlanVcForwarding_Type(TruthValue):
    """Custom type sdpBindForceVlanVcForwarding based on TruthValue"""


_SdpBindForceVlanVcForwarding_Object = MibTableColumn
sdpBindForceVlanVcForwarding = _SdpBindForceVlanVcForwarding_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 39),
    _SdpBindForceVlanVcForwarding_Type()
)
sdpBindForceVlanVcForwarding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindForceVlanVcForwarding.setStatus("current")


class _SdpBindAdminBandwidth_Type(SdpBindBandwidth):
    """Custom type sdpBindAdminBandwidth based on SdpBindBandwidth"""
    defaultValue = 0


_SdpBindAdminBandwidth_Object = MibTableColumn
sdpBindAdminBandwidth = _SdpBindAdminBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 40),
    _SdpBindAdminBandwidth_Type()
)
sdpBindAdminBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindAdminBandwidth.setUnits("kilo-bits per second")
_SdpBindOperBandwidth_Type = SdpBindBandwidth
_SdpBindOperBandwidth_Object = MibTableColumn
sdpBindOperBandwidth = _SdpBindOperBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 4, 1, 41),
    _SdpBindOperBandwidth_Type()
)
sdpBindOperBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindOperBandwidth.setUnits("kilo-bits per second")
_SdpBindBaseStatsTable_Object = MibTable
sdpBindBaseStatsTable = _SdpBindBaseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5)
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsTable.setStatus("current")
_SdpBindBaseStatsEntry_Object = MibTableRow
sdpBindBaseStatsEntry = _SdpBindBaseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1)
)
sdpBindBaseStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindBaseStatsEntry.setStatus("current")
_SdpBindBaseStatsIngressForwardedPackets_Type = Counter64
_SdpBindBaseStatsIngressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressForwardedPackets = _SdpBindBaseStatsIngressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 1),
    _SdpBindBaseStatsIngressForwardedPackets_Type()
)
sdpBindBaseStatsIngressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressForwardedPackets.setStatus("current")
_SdpBindBaseStatsIngressDroppedPackets_Type = Counter64
_SdpBindBaseStatsIngressDroppedPackets_Object = MibTableColumn
sdpBindBaseStatsIngressDroppedPackets = _SdpBindBaseStatsIngressDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 2),
    _SdpBindBaseStatsIngressDroppedPackets_Type()
)
sdpBindBaseStatsIngressDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngressDroppedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedPackets_Type = Counter64
_SdpBindBaseStatsEgressForwardedPackets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedPackets = _SdpBindBaseStatsEgressForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 3),
    _SdpBindBaseStatsEgressForwardedPackets_Type()
)
sdpBindBaseStatsEgressForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedPackets.setStatus("current")
_SdpBindBaseStatsEgressForwardedOctets_Type = Counter64
_SdpBindBaseStatsEgressForwardedOctets_Object = MibTableColumn
sdpBindBaseStatsEgressForwardedOctets = _SdpBindBaseStatsEgressForwardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 4),
    _SdpBindBaseStatsEgressForwardedOctets_Type()
)
sdpBindBaseStatsEgressForwardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsEgressForwardedOctets.setStatus("current")
_SdpBindBaseStatsCustId_Type = TmnxCustId
_SdpBindBaseStatsCustId_Object = MibTableColumn
sdpBindBaseStatsCustId = _SdpBindBaseStatsCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 5),
    _SdpBindBaseStatsCustId_Type()
)
sdpBindBaseStatsCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsCustId.setStatus("current")
_SdpBindBaseStatsIngFwdOctets_Type = Counter64
_SdpBindBaseStatsIngFwdOctets_Object = MibTableColumn
sdpBindBaseStatsIngFwdOctets = _SdpBindBaseStatsIngFwdOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 6),
    _SdpBindBaseStatsIngFwdOctets_Type()
)
sdpBindBaseStatsIngFwdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngFwdOctets.setStatus("current")
_SdpBindBaseStatsIngDropOctets_Type = Counter64
_SdpBindBaseStatsIngDropOctets_Object = MibTableColumn
sdpBindBaseStatsIngDropOctets = _SdpBindBaseStatsIngDropOctets_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 5, 1, 7),
    _SdpBindBaseStatsIngDropOctets_Type()
)
sdpBindBaseStatsIngDropOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindBaseStatsIngDropOctets.setStatus("current")
_SdpBindTlsTable_Object = MibTable
sdpBindTlsTable = _SdpBindTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    sdpBindTlsTable.setStatus("current")
_SdpBindTlsEntry_Object = MibTableRow
sdpBindTlsEntry = _SdpBindTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1)
)
sdpBindTlsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsEntry.setStatus("current")


class _SdpBindTlsStpAdminStatus_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsStpAdminStatus based on TmnxEnabledDisabled"""


_SdpBindTlsStpAdminStatus_Object = MibTableColumn
sdpBindTlsStpAdminStatus = _SdpBindTlsStpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 1),
    _SdpBindTlsStpAdminStatus_Type()
)
sdpBindTlsStpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAdminStatus.setStatus("current")


class _SdpBindTlsStpPriority_Type(Integer32):
    """Custom type sdpBindTlsStpPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdpBindTlsStpPriority_Type.__name__ = "Integer32"
_SdpBindTlsStpPriority_Object = MibTableColumn
sdpBindTlsStpPriority = _SdpBindTlsStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 2),
    _SdpBindTlsStpPriority_Type()
)
sdpBindTlsStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPriority.setStatus("current")


class _SdpBindTlsStpPortNum_Type(Integer32):
    """Custom type sdpBindTlsStpPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SdpBindTlsStpPortNum_Type.__name__ = "Integer32"
_SdpBindTlsStpPortNum_Object = MibTableColumn
sdpBindTlsStpPortNum = _SdpBindTlsStpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 3),
    _SdpBindTlsStpPortNum_Type()
)
sdpBindTlsStpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortNum.setStatus("current")


class _SdpBindTlsStpPathCost_Type(Integer32):
    """Custom type sdpBindTlsStpPathCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SdpBindTlsStpPathCost_Type.__name__ = "Integer32"
_SdpBindTlsStpPathCost_Object = MibTableColumn
sdpBindTlsStpPathCost = _SdpBindTlsStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 4),
    _SdpBindTlsStpPathCost_Type()
)
sdpBindTlsStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpPathCost.setStatus("current")


class _SdpBindTlsStpRapidStart_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsStpRapidStart based on TmnxEnabledDisabled"""


_SdpBindTlsStpRapidStart_Object = MibTableColumn
sdpBindTlsStpRapidStart = _SdpBindTlsStpRapidStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 5),
    _SdpBindTlsStpRapidStart_Type()
)
sdpBindTlsStpRapidStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpRapidStart.setStatus("current")


class _SdpBindTlsStpBpduEncap_Type(Integer32):
    """Custom type sdpBindTlsStpBpduEncap based on Integer32"""
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


_SdpBindTlsStpBpduEncap_Type.__name__ = "Integer32"
_SdpBindTlsStpBpduEncap_Object = MibTableColumn
sdpBindTlsStpBpduEncap = _SdpBindTlsStpBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 6),
    _SdpBindTlsStpBpduEncap_Type()
)
sdpBindTlsStpBpduEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpBpduEncap.setStatus("current")
_SdpBindTlsStpPortState_Type = TStpPortState
_SdpBindTlsStpPortState_Object = MibTableColumn
sdpBindTlsStpPortState = _SdpBindTlsStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 7),
    _SdpBindTlsStpPortState_Type()
)
sdpBindTlsStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortState.setStatus("current")
_SdpBindTlsStpDesignatedBridge_Type = BridgeId
_SdpBindTlsStpDesignatedBridge_Object = MibTableColumn
sdpBindTlsStpDesignatedBridge = _SdpBindTlsStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 8),
    _SdpBindTlsStpDesignatedBridge_Type()
)
sdpBindTlsStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpDesignatedBridge.setStatus("current")
_SdpBindTlsStpDesignatedPort_Type = Integer32
_SdpBindTlsStpDesignatedPort_Object = MibTableColumn
sdpBindTlsStpDesignatedPort = _SdpBindTlsStpDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 9),
    _SdpBindTlsStpDesignatedPort_Type()
)
sdpBindTlsStpDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpDesignatedPort.setStatus("current")
_SdpBindTlsStpForwardTransitions_Type = Gauge32
_SdpBindTlsStpForwardTransitions_Object = MibTableColumn
sdpBindTlsStpForwardTransitions = _SdpBindTlsStpForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 10),
    _SdpBindTlsStpForwardTransitions_Type()
)
sdpBindTlsStpForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpForwardTransitions.setStatus("current")
_SdpBindTlsStpInConfigBpdus_Type = Gauge32
_SdpBindTlsStpInConfigBpdus_Object = MibTableColumn
sdpBindTlsStpInConfigBpdus = _SdpBindTlsStpInConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 11),
    _SdpBindTlsStpInConfigBpdus_Type()
)
sdpBindTlsStpInConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInConfigBpdus.setStatus("current")
_SdpBindTlsStpInTcnBpdus_Type = Gauge32
_SdpBindTlsStpInTcnBpdus_Object = MibTableColumn
sdpBindTlsStpInTcnBpdus = _SdpBindTlsStpInTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 12),
    _SdpBindTlsStpInTcnBpdus_Type()
)
sdpBindTlsStpInTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInTcnBpdus.setStatus("current")
_SdpBindTlsStpInBadBpdus_Type = Gauge32
_SdpBindTlsStpInBadBpdus_Object = MibTableColumn
sdpBindTlsStpInBadBpdus = _SdpBindTlsStpInBadBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 13),
    _SdpBindTlsStpInBadBpdus_Type()
)
sdpBindTlsStpInBadBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInBadBpdus.setStatus("current")
_SdpBindTlsStpOutConfigBpdus_Type = Gauge32
_SdpBindTlsStpOutConfigBpdus_Object = MibTableColumn
sdpBindTlsStpOutConfigBpdus = _SdpBindTlsStpOutConfigBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 14),
    _SdpBindTlsStpOutConfigBpdus_Type()
)
sdpBindTlsStpOutConfigBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutConfigBpdus.setStatus("current")
_SdpBindTlsStpOutTcnBpdus_Type = Gauge32
_SdpBindTlsStpOutTcnBpdus_Object = MibTableColumn
sdpBindTlsStpOutTcnBpdus = _SdpBindTlsStpOutTcnBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 15),
    _SdpBindTlsStpOutTcnBpdus_Type()
)
sdpBindTlsStpOutTcnBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutTcnBpdus.setStatus("current")


class _SdpBindTlsStpOperBpduEncap_Type(Integer32):
    """Custom type sdpBindTlsStpOperBpduEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d", 2),
          ("pvst", 3))
    )


_SdpBindTlsStpOperBpduEncap_Type.__name__ = "Integer32"
_SdpBindTlsStpOperBpduEncap_Object = MibTableColumn
sdpBindTlsStpOperBpduEncap = _SdpBindTlsStpOperBpduEncap_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 16),
    _SdpBindTlsStpOperBpduEncap_Type()
)
sdpBindTlsStpOperBpduEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperBpduEncap.setStatus("current")
_SdpBindTlsStpVpnId_Type = VpnId
_SdpBindTlsStpVpnId_Object = MibTableColumn
sdpBindTlsStpVpnId = _SdpBindTlsStpVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 17),
    _SdpBindTlsStpVpnId_Type()
)
sdpBindTlsStpVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpVpnId.setStatus("current")
_SdpBindTlsStpCustId_Type = TmnxCustId
_SdpBindTlsStpCustId_Object = MibTableColumn
sdpBindTlsStpCustId = _SdpBindTlsStpCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 18),
    _SdpBindTlsStpCustId_Type()
)
sdpBindTlsStpCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpCustId.setStatus("current")


class _SdpBindTlsMacAddressLimit_Type(Integer32):
    """Custom type sdpBindTlsMacAddressLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196607),
    )


_SdpBindTlsMacAddressLimit_Type.__name__ = "Integer32"
_SdpBindTlsMacAddressLimit_Object = MibTableColumn
sdpBindTlsMacAddressLimit = _SdpBindTlsMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 19),
    _SdpBindTlsMacAddressLimit_Type()
)
sdpBindTlsMacAddressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAddressLimit.setStatus("current")
_SdpBindTlsNumMacAddresses_Type = Integer32
_SdpBindTlsNumMacAddresses_Object = MibTableColumn
sdpBindTlsNumMacAddresses = _SdpBindTlsNumMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 20),
    _SdpBindTlsNumMacAddresses_Type()
)
sdpBindTlsNumMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumMacAddresses.setStatus("current")
_SdpBindTlsNumStaticMacAddresses_Type = Integer32
_SdpBindTlsNumStaticMacAddresses_Object = MibTableColumn
sdpBindTlsNumStaticMacAddresses = _SdpBindTlsNumStaticMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 21),
    _SdpBindTlsNumStaticMacAddresses_Type()
)
sdpBindTlsNumStaticMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsNumStaticMacAddresses.setStatus("current")


class _SdpBindTlsMacLearning_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacLearning based on TmnxEnabledDisabled"""


_SdpBindTlsMacLearning_Object = MibTableColumn
sdpBindTlsMacLearning = _SdpBindTlsMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 22),
    _SdpBindTlsMacLearning_Type()
)
sdpBindTlsMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacLearning.setStatus("current")


class _SdpBindTlsMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsMacAgeing based on TmnxEnabledDisabled"""


_SdpBindTlsMacAgeing_Object = MibTableColumn
sdpBindTlsMacAgeing = _SdpBindTlsMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 23),
    _SdpBindTlsMacAgeing_Type()
)
sdpBindTlsMacAgeing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMacAgeing.setStatus("current")
_SdpBindTlsStpOperEdge_Type = TruthValue
_SdpBindTlsStpOperEdge_Object = MibTableColumn
sdpBindTlsStpOperEdge = _SdpBindTlsStpOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 24),
    _SdpBindTlsStpOperEdge_Type()
)
sdpBindTlsStpOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperEdge.setStatus("current")


class _SdpBindTlsStpAdminPointToPoint_Type(Integer32):
    """Custom type sdpBindTlsStpAdminPointToPoint based on Integer32"""
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


_SdpBindTlsStpAdminPointToPoint_Type.__name__ = "Integer32"
_SdpBindTlsStpAdminPointToPoint_Object = MibTableColumn
sdpBindTlsStpAdminPointToPoint = _SdpBindTlsStpAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 25),
    _SdpBindTlsStpAdminPointToPoint_Type()
)
sdpBindTlsStpAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAdminPointToPoint.setStatus("current")
_SdpBindTlsStpPortRole_Type = StpPortRole
_SdpBindTlsStpPortRole_Object = MibTableColumn
sdpBindTlsStpPortRole = _SdpBindTlsStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 26),
    _SdpBindTlsStpPortRole_Type()
)
sdpBindTlsStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpPortRole.setStatus("current")


class _SdpBindTlsStpAutoEdge_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsStpAutoEdge based on TmnxEnabledDisabled"""


_SdpBindTlsStpAutoEdge_Object = MibTableColumn
sdpBindTlsStpAutoEdge = _SdpBindTlsStpAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 27),
    _SdpBindTlsStpAutoEdge_Type()
)
sdpBindTlsStpAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpAutoEdge.setStatus("current")
_SdpBindTlsStpOperProtocol_Type = StpProtocol
_SdpBindTlsStpOperProtocol_Object = MibTableColumn
sdpBindTlsStpOperProtocol = _SdpBindTlsStpOperProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 28),
    _SdpBindTlsStpOperProtocol_Type()
)
sdpBindTlsStpOperProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOperProtocol.setStatus("current")
_SdpBindTlsStpInRstBpdus_Type = Gauge32
_SdpBindTlsStpInRstBpdus_Object = MibTableColumn
sdpBindTlsStpInRstBpdus = _SdpBindTlsStpInRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 29),
    _SdpBindTlsStpInRstBpdus_Type()
)
sdpBindTlsStpInRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInRstBpdus.setStatus("current")
_SdpBindTlsStpOutRstBpdus_Type = Gauge32
_SdpBindTlsStpOutRstBpdus_Object = MibTableColumn
sdpBindTlsStpOutRstBpdus = _SdpBindTlsStpOutRstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 30),
    _SdpBindTlsStpOutRstBpdus_Type()
)
sdpBindTlsStpOutRstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutRstBpdus.setStatus("current")


class _SdpBindTlsLimitMacMove_Type(TlsLimitMacMove):
    """Custom type sdpBindTlsLimitMacMove based on TlsLimitMacMove"""


_SdpBindTlsLimitMacMove_Object = MibTableColumn
sdpBindTlsLimitMacMove = _SdpBindTlsLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 31),
    _SdpBindTlsLimitMacMove_Type()
)
sdpBindTlsLimitMacMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsLimitMacMove.setStatus("current")


class _SdpBindTlsDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsDiscardUnknownSource based on TmnxEnabledDisabled"""


_SdpBindTlsDiscardUnknownSource_Object = MibTableColumn
sdpBindTlsDiscardUnknownSource = _SdpBindTlsDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 32),
    _SdpBindTlsDiscardUnknownSource_Type()
)
sdpBindTlsDiscardUnknownSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsDiscardUnknownSource.setStatus("current")
_SdpBindTlsMvplsPruneState_Type = MvplsPruneState
_SdpBindTlsMvplsPruneState_Object = MibTableColumn
sdpBindTlsMvplsPruneState = _SdpBindTlsMvplsPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 33),
    _SdpBindTlsMvplsPruneState_Type()
)
sdpBindTlsMvplsPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsPruneState.setStatus("current")
_SdpBindTlsMvplsMgmtService_Type = TmnxServId
_SdpBindTlsMvplsMgmtService_Object = MibTableColumn
sdpBindTlsMvplsMgmtService = _SdpBindTlsMvplsMgmtService_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 34),
    _SdpBindTlsMvplsMgmtService_Type()
)
sdpBindTlsMvplsMgmtService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsMgmtService.setStatus("current")
_SdpBindTlsMvplsMgmtSdpBndId_Type = SdpBindId
_SdpBindTlsMvplsMgmtSdpBndId_Object = MibTableColumn
sdpBindTlsMvplsMgmtSdpBndId = _SdpBindTlsMvplsMgmtSdpBndId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 35),
    _SdpBindTlsMvplsMgmtSdpBndId_Type()
)
sdpBindTlsMvplsMgmtSdpBndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMvplsMgmtSdpBndId.setStatus("current")
_SdpBindTlsStpException_Type = StpExceptionCondition
_SdpBindTlsStpException_Object = MibTableColumn
sdpBindTlsStpException = _SdpBindTlsStpException_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 36),
    _SdpBindTlsStpException_Type()
)
sdpBindTlsStpException.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpException.setStatus("current")


class _SdpBindTlsL2ptTermination_Type(TmnxEnabledDisabled):
    """Custom type sdpBindTlsL2ptTermination based on TmnxEnabledDisabled"""


_SdpBindTlsL2ptTermination_Object = MibTableColumn
sdpBindTlsL2ptTermination = _SdpBindTlsL2ptTermination_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 37),
    _SdpBindTlsL2ptTermination_Type()
)
sdpBindTlsL2ptTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptTermination.setStatus("current")


class _SdpBindTlsBpduTranslation_Type(SdpBindTlsBpduTranslation):
    """Custom type sdpBindTlsBpduTranslation based on SdpBindTlsBpduTranslation"""


_SdpBindTlsBpduTranslation_Object = MibTableColumn
sdpBindTlsBpduTranslation = _SdpBindTlsBpduTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 38),
    _SdpBindTlsBpduTranslation_Type()
)
sdpBindTlsBpduTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsBpduTranslation.setStatus("current")


class _SdpBindTlsStpRootGuard_Type(TruthValue):
    """Custom type sdpBindTlsStpRootGuard based on TruthValue"""


_SdpBindTlsStpRootGuard_Object = MibTableColumn
sdpBindTlsStpRootGuard = _SdpBindTlsStpRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 39),
    _SdpBindTlsStpRootGuard_Type()
)
sdpBindTlsStpRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsStpRootGuard.setStatus("current")
_SdpBindTlsStpInMstBpdus_Type = Gauge32
_SdpBindTlsStpInMstBpdus_Object = MibTableColumn
sdpBindTlsStpInMstBpdus = _SdpBindTlsStpInMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 40),
    _SdpBindTlsStpInMstBpdus_Type()
)
sdpBindTlsStpInMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpInMstBpdus.setStatus("current")
_SdpBindTlsStpOutMstBpdus_Type = Gauge32
_SdpBindTlsStpOutMstBpdus_Object = MibTableColumn
sdpBindTlsStpOutMstBpdus = _SdpBindTlsStpOutMstBpdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 41),
    _SdpBindTlsStpOutMstBpdus_Type()
)
sdpBindTlsStpOutMstBpdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpOutMstBpdus.setStatus("current")
_SdpBindTlsStpRxdDesigBridge_Type = BridgeId
_SdpBindTlsStpRxdDesigBridge_Object = MibTableColumn
sdpBindTlsStpRxdDesigBridge = _SdpBindTlsStpRxdDesigBridge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 42),
    _SdpBindTlsStpRxdDesigBridge_Type()
)
sdpBindTlsStpRxdDesigBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsStpRxdDesigBridge.setStatus("current")
_SdpBindTlsMacMoveNextUpTime_Type = Unsigned32
_SdpBindTlsMacMoveNextUpTime_Object = MibTableColumn
sdpBindTlsMacMoveNextUpTime = _SdpBindTlsMacMoveNextUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 43),
    _SdpBindTlsMacMoveNextUpTime_Type()
)
sdpBindTlsMacMoveNextUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveNextUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveNextUpTime.setUnits("seconds")
_SdpBindTlsMacMoveRateExcdLeft_Type = Unsigned32
_SdpBindTlsMacMoveRateExcdLeft_Object = MibTableColumn
sdpBindTlsMacMoveRateExcdLeft = _SdpBindTlsMacMoveRateExcdLeft_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 44),
    _SdpBindTlsMacMoveRateExcdLeft_Type()
)
sdpBindTlsMacMoveRateExcdLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveRateExcdLeft.setStatus("current")


class _SdpBindTlsLimitMacMoveLevel_Type(TlsLimitMacMoveLevel):
    """Custom type sdpBindTlsLimitMacMoveLevel based on TlsLimitMacMoveLevel"""


_SdpBindTlsLimitMacMoveLevel_Object = MibTableColumn
sdpBindTlsLimitMacMoveLevel = _SdpBindTlsLimitMacMoveLevel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 45),
    _SdpBindTlsLimitMacMoveLevel_Type()
)
sdpBindTlsLimitMacMoveLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsLimitMacMoveLevel.setStatus("current")


class _SdpBindTlsBpduTransOper_Type(Integer32):
    """Custom type sdpBindTlsBpduTransOper based on Integer32"""
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


_SdpBindTlsBpduTransOper_Type.__name__ = "Integer32"
_SdpBindTlsBpduTransOper_Object = MibTableColumn
sdpBindTlsBpduTransOper = _SdpBindTlsBpduTransOper_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 46),
    _SdpBindTlsBpduTransOper_Type()
)
sdpBindTlsBpduTransOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsBpduTransOper.setStatus("current")


class _SdpBindTlsL2ptProtocols_Type(L2ptProtocols):
    """Custom type sdpBindTlsL2ptProtocols based on L2ptProtocols"""
    defaultBinValue = "1"


_SdpBindTlsL2ptProtocols_Object = MibTableColumn
sdpBindTlsL2ptProtocols = _SdpBindTlsL2ptProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 47),
    _SdpBindTlsL2ptProtocols_Type()
)
sdpBindTlsL2ptProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptProtocols.setStatus("current")


class _SdpBindTlsIgnoreStandbySig_Type(TruthValue):
    """Custom type sdpBindTlsIgnoreStandbySig based on TruthValue"""


_SdpBindTlsIgnoreStandbySig_Object = MibTableColumn
sdpBindTlsIgnoreStandbySig = _SdpBindTlsIgnoreStandbySig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 48),
    _SdpBindTlsIgnoreStandbySig_Type()
)
sdpBindTlsIgnoreStandbySig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsIgnoreStandbySig.setStatus("current")


class _SdpBindTlsBlockOnMeshFail_Type(TruthValue):
    """Custom type sdpBindTlsBlockOnMeshFail based on TruthValue"""


_SdpBindTlsBlockOnMeshFail_Object = MibTableColumn
sdpBindTlsBlockOnMeshFail = _SdpBindTlsBlockOnMeshFail_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 6, 1, 49),
    _SdpBindTlsBlockOnMeshFail_Type()
)
sdpBindTlsBlockOnMeshFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsBlockOnMeshFail.setStatus("current")
_SdpBindMeshTlsTable_Object = MibTable
sdpBindMeshTlsTable = _SdpBindMeshTlsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7)
)
if mibBuilder.loadTexts:
    sdpBindMeshTlsTable.setStatus("current")
_SdpBindMeshTlsEntry_Object = MibTableRow
sdpBindMeshTlsEntry = _SdpBindMeshTlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1)
)
sdpBindMeshTlsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindMeshTlsEntry.setStatus("current")
_SdpBindMeshTlsPortState_Type = TStpPortState
_SdpBindMeshTlsPortState_Object = MibTableColumn
sdpBindMeshTlsPortState = _SdpBindMeshTlsPortState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 1),
    _SdpBindMeshTlsPortState_Type()
)
sdpBindMeshTlsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsPortState.setStatus("current")


class _SdpBindMeshTlsHoldDownTimer_Type(Integer32):
    """Custom type sdpBindMeshTlsHoldDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("not-active", 1))
    )


_SdpBindMeshTlsHoldDownTimer_Type.__name__ = "Integer32"
_SdpBindMeshTlsHoldDownTimer_Object = MibTableColumn
sdpBindMeshTlsHoldDownTimer = _SdpBindMeshTlsHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 2),
    _SdpBindMeshTlsHoldDownTimer_Type()
)
sdpBindMeshTlsHoldDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsHoldDownTimer.setStatus("current")


class _SdpBindMeshTlsTransitionState_Type(Integer32):
    """Custom type sdpBindMeshTlsTransitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("agreement-received", 3),
          ("not-applicable", 1),
          ("waiting-for-agreement", 2))
    )


_SdpBindMeshTlsTransitionState_Type.__name__ = "Integer32"
_SdpBindMeshTlsTransitionState_Object = MibTableColumn
sdpBindMeshTlsTransitionState = _SdpBindMeshTlsTransitionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 3),
    _SdpBindMeshTlsTransitionState_Type()
)
sdpBindMeshTlsTransitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsTransitionState.setStatus("current")
_SdpBindMeshTlsNotInMstRegion_Type = TruthValue
_SdpBindMeshTlsNotInMstRegion_Object = MibTableColumn
sdpBindMeshTlsNotInMstRegion = _SdpBindMeshTlsNotInMstRegion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 7, 1, 4),
    _SdpBindMeshTlsNotInMstRegion_Type()
)
sdpBindMeshTlsNotInMstRegion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindMeshTlsNotInMstRegion.setStatus("current")
_SdpBindApipeTable_Object = MibTable
sdpBindApipeTable = _SdpBindApipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8)
)
if mibBuilder.loadTexts:
    sdpBindApipeTable.setStatus("current")
_SdpBindApipeEntry_Object = MibTableRow
sdpBindApipeEntry = _SdpBindApipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1)
)
sdpBindApipeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindApipeEntry.setStatus("current")


class _SdpBindApipeAdminConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeAdminConcatCellCount based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdpBindApipeAdminConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeAdminConcatCellCount_Object = MibTableColumn
sdpBindApipeAdminConcatCellCount = _SdpBindApipeAdminConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 1),
    _SdpBindApipeAdminConcatCellCount_Type()
)
sdpBindApipeAdminConcatCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeAdminConcatCellCount.setStatus("current")


class _SdpBindApipeSigConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeSigConcatCellCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_SdpBindApipeSigConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeSigConcatCellCount_Object = MibTableColumn
sdpBindApipeSigConcatCellCount = _SdpBindApipeSigConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 2),
    _SdpBindApipeSigConcatCellCount_Type()
)
sdpBindApipeSigConcatCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindApipeSigConcatCellCount.setStatus("current")


class _SdpBindApipeOperConcatCellCount_Type(Integer32):
    """Custom type sdpBindApipeOperConcatCellCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdpBindApipeOperConcatCellCount_Type.__name__ = "Integer32"
_SdpBindApipeOperConcatCellCount_Object = MibTableColumn
sdpBindApipeOperConcatCellCount = _SdpBindApipeOperConcatCellCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 3),
    _SdpBindApipeOperConcatCellCount_Type()
)
sdpBindApipeOperConcatCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindApipeOperConcatCellCount.setStatus("current")


class _SdpBindApipeConcatMaxDelay_Type(Integer32):
    """Custom type sdpBindApipeConcatMaxDelay based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SdpBindApipeConcatMaxDelay_Type.__name__ = "Integer32"
_SdpBindApipeConcatMaxDelay_Object = MibTableColumn
sdpBindApipeConcatMaxDelay = _SdpBindApipeConcatMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 4),
    _SdpBindApipeConcatMaxDelay_Type()
)
sdpBindApipeConcatMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindApipeConcatMaxDelay.setUnits("hundreds of microseconds")


class _SdpBindApipeConcatCellClp_Type(TruthValue):
    """Custom type sdpBindApipeConcatCellClp based on TruthValue"""


_SdpBindApipeConcatCellClp_Object = MibTableColumn
sdpBindApipeConcatCellClp = _SdpBindApipeConcatCellClp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 5),
    _SdpBindApipeConcatCellClp_Type()
)
sdpBindApipeConcatCellClp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatCellClp.setStatus("current")


class _SdpBindApipeConcatCellAal5Fr_Type(TruthValue):
    """Custom type sdpBindApipeConcatCellAal5Fr based on TruthValue"""


_SdpBindApipeConcatCellAal5Fr_Object = MibTableColumn
sdpBindApipeConcatCellAal5Fr = _SdpBindApipeConcatCellAal5Fr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 8, 1, 6),
    _SdpBindApipeConcatCellAal5Fr_Type()
)
sdpBindApipeConcatCellAal5Fr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindApipeConcatCellAal5Fr.setStatus("current")
_SdpBindDhcpInfoTable_Object = MibTable
sdpBindDhcpInfoTable = _SdpBindDhcpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9)
)
if mibBuilder.loadTexts:
    sdpBindDhcpInfoTable.setStatus("current")
_SdpBindDhcpInfoEntry_Object = MibTableRow
sdpBindDhcpInfoEntry = _SdpBindDhcpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1)
)
sdpBindDhcpInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindDhcpInfoEntry.setStatus("current")


class _SdpBindDhcpDescription_Type(ServObjDesc):
    """Custom type sdpBindDhcpDescription based on ServObjDesc"""
    defaultHexValue = ""


_SdpBindDhcpDescription_Object = MibTableColumn
sdpBindDhcpDescription = _SdpBindDhcpDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1, 1),
    _SdpBindDhcpDescription_Type()
)
sdpBindDhcpDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcpDescription.setStatus("current")


class _SdpBindDhcpSnoop_Type(TmnxEnabledDisabled):
    """Custom type sdpBindDhcpSnoop based on TmnxEnabledDisabled"""


_SdpBindDhcpSnoop_Object = MibTableColumn
sdpBindDhcpSnoop = _SdpBindDhcpSnoop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 9, 1, 2),
    _SdpBindDhcpSnoop_Type()
)
sdpBindDhcpSnoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindDhcpSnoop.setStatus("current")
_SdpBindDhcpStatsTable_Object = MibTable
sdpBindDhcpStatsTable = _SdpBindDhcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10)
)
if mibBuilder.loadTexts:
    sdpBindDhcpStatsTable.setStatus("current")
_SdpBindDhcpStatsEntry_Object = MibTableRow
sdpBindDhcpStatsEntry = _SdpBindDhcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1)
)
sdpBindDhcpStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindDhcpStatsEntry.setStatus("current")
_SdpBindDhcpStatsClntSnoopdPckts_Type = Counter32
_SdpBindDhcpStatsClntSnoopdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntSnoopdPckts = _SdpBindDhcpStatsClntSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 1),
    _SdpBindDhcpStatsClntSnoopdPckts_Type()
)
sdpBindDhcpStatsClntSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntSnoopdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrSnoopdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrSnoopdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrSnoopdPckts = _SdpBindDhcpStatsSrvrSnoopdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 2),
    _SdpBindDhcpStatsSrvrSnoopdPckts_Type()
)
sdpBindDhcpStatsSrvrSnoopdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrSnoopdPckts.setStatus("current")
_SdpBindDhcpStatsClntForwdPckts_Type = Counter32
_SdpBindDhcpStatsClntForwdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntForwdPckts = _SdpBindDhcpStatsClntForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 3),
    _SdpBindDhcpStatsClntForwdPckts_Type()
)
sdpBindDhcpStatsClntForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntForwdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrForwdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrForwdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrForwdPckts = _SdpBindDhcpStatsSrvrForwdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 4),
    _SdpBindDhcpStatsSrvrForwdPckts_Type()
)
sdpBindDhcpStatsSrvrForwdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrForwdPckts.setStatus("current")
_SdpBindDhcpStatsClntDropdPckts_Type = Counter32
_SdpBindDhcpStatsClntDropdPckts_Object = MibTableColumn
sdpBindDhcpStatsClntDropdPckts = _SdpBindDhcpStatsClntDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 5),
    _SdpBindDhcpStatsClntDropdPckts_Type()
)
sdpBindDhcpStatsClntDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntDropdPckts.setStatus("current")
_SdpBindDhcpStatsSrvrDropdPckts_Type = Counter32
_SdpBindDhcpStatsSrvrDropdPckts_Object = MibTableColumn
sdpBindDhcpStatsSrvrDropdPckts = _SdpBindDhcpStatsSrvrDropdPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 6),
    _SdpBindDhcpStatsSrvrDropdPckts_Type()
)
sdpBindDhcpStatsSrvrDropdPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsSrvrDropdPckts.setStatus("current")
_SdpBindDhcpStatsClntProxRadPckts_Type = Counter32
_SdpBindDhcpStatsClntProxRadPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxRadPckts = _SdpBindDhcpStatsClntProxRadPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 7),
    _SdpBindDhcpStatsClntProxRadPckts_Type()
)
sdpBindDhcpStatsClntProxRadPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxRadPckts.setStatus("current")
_SdpBindDhcpStatsClntProxLSPckts_Type = Counter32
_SdpBindDhcpStatsClntProxLSPckts_Object = MibTableColumn
sdpBindDhcpStatsClntProxLSPckts = _SdpBindDhcpStatsClntProxLSPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 8),
    _SdpBindDhcpStatsClntProxLSPckts_Type()
)
sdpBindDhcpStatsClntProxLSPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsClntProxLSPckts.setStatus("current")
_SdpBindDhcpStatsGenReleasePckts_Type = Counter32
_SdpBindDhcpStatsGenReleasePckts_Object = MibTableColumn
sdpBindDhcpStatsGenReleasePckts = _SdpBindDhcpStatsGenReleasePckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 9),
    _SdpBindDhcpStatsGenReleasePckts_Type()
)
sdpBindDhcpStatsGenReleasePckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsGenReleasePckts.setStatus("current")
_SdpBindDhcpStatsGenForceRenPckts_Type = Counter32
_SdpBindDhcpStatsGenForceRenPckts_Object = MibTableColumn
sdpBindDhcpStatsGenForceRenPckts = _SdpBindDhcpStatsGenForceRenPckts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 10, 1, 10),
    _SdpBindDhcpStatsGenForceRenPckts_Type()
)
sdpBindDhcpStatsGenForceRenPckts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindDhcpStatsGenForceRenPckts.setStatus("current")
_SdpBindIpipeTable_Object = MibTable
sdpBindIpipeTable = _SdpBindIpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11)
)
if mibBuilder.loadTexts:
    sdpBindIpipeTable.setStatus("current")
_SdpBindIpipeEntry_Object = MibTableRow
sdpBindIpipeEntry = _SdpBindIpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1)
)
sdpBindIpipeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindIpipeEntry.setStatus("current")
_SdpBindIpipeCeInetAddressType_Type = InetAddressType
_SdpBindIpipeCeInetAddressType_Object = MibTableColumn
sdpBindIpipeCeInetAddressType = _SdpBindIpipeCeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 1),
    _SdpBindIpipeCeInetAddressType_Type()
)
sdpBindIpipeCeInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindIpipeCeInetAddressType.setStatus("current")


class _SdpBindIpipeCeInetAddress_Type(InetAddress):
    """Custom type sdpBindIpipeCeInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_SdpBindIpipeCeInetAddress_Type.__name__ = "InetAddress"
_SdpBindIpipeCeInetAddress_Object = MibTableColumn
sdpBindIpipeCeInetAddress = _SdpBindIpipeCeInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 11, 1, 2),
    _SdpBindIpipeCeInetAddress_Type()
)
sdpBindIpipeCeInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindIpipeCeInetAddress.setStatus("current")
_SdpFCMappingTable_Object = MibTable
sdpFCMappingTable = _SdpFCMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12)
)
if mibBuilder.loadTexts:
    sdpFCMappingTable.setStatus("current")
_SdpFCMappingEntry_Object = MibTableRow
sdpFCMappingEntry = _SdpFCMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1)
)
sdpFCMappingEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpFCMappingFCName"),
)
if mibBuilder.loadTexts:
    sdpFCMappingEntry.setStatus("current")
_SdpFCMappingFCName_Type = TNamedItem
_SdpFCMappingFCName_Object = MibTableColumn
sdpFCMappingFCName = _SdpFCMappingFCName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 1),
    _SdpFCMappingFCName_Type()
)
sdpFCMappingFCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpFCMappingFCName.setStatus("current")
_SdpFCMappingRowStatus_Type = RowStatus
_SdpFCMappingRowStatus_Object = MibTableColumn
sdpFCMappingRowStatus = _SdpFCMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 2),
    _SdpFCMappingRowStatus_Type()
)
sdpFCMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingRowStatus.setStatus("current")
_SdpFCMappingLspId_Type = TmnxVRtrMplsLspID
_SdpFCMappingLspId_Object = MibTableColumn
sdpFCMappingLspId = _SdpFCMappingLspId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 12, 1, 3),
    _SdpFCMappingLspId_Type()
)
sdpFCMappingLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpFCMappingLspId.setStatus("current")
_SdpBindTlsMfibAllowedMdaTable_Object = MibTable
sdpBindTlsMfibAllowedMdaTable = _SdpBindTlsMfibAllowedMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13)
)
if mibBuilder.loadTexts:
    sdpBindTlsMfibAllowedMdaTable.setStatus("current")
_SdpBindTlsMfibAllowedMdaEntry_Object = MibTableRow
sdpBindTlsMfibAllowedMdaEntry = _SdpBindTlsMfibAllowedMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13, 1)
)
sdpBindTlsMfibAllowedMdaEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMfibAllowedMdaEntry.setStatus("current")
_SdpBindTlsMfibMdaRowStatus_Type = RowStatus
_SdpBindTlsMfibMdaRowStatus_Object = MibTableColumn
sdpBindTlsMfibMdaRowStatus = _SdpBindTlsMfibMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 13, 1, 1),
    _SdpBindTlsMfibMdaRowStatus_Type()
)
sdpBindTlsMfibMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sdpBindTlsMfibMdaRowStatus.setStatus("current")
_SdpBindCpipeTable_Object = MibTable
sdpBindCpipeTable = _SdpBindCpipeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15)
)
if mibBuilder.loadTexts:
    sdpBindCpipeTable.setStatus("current")
_SdpBindCpipeEntry_Object = MibTableRow
sdpBindCpipeEntry = _SdpBindCpipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1)
)
sdpBindCpipeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindCpipeEntry.setStatus("current")
_SdpBindCpipeLocalPayloadSize_Type = Unsigned32
_SdpBindCpipeLocalPayloadSize_Object = MibTableColumn
sdpBindCpipeLocalPayloadSize = _SdpBindCpipeLocalPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 1),
    _SdpBindCpipeLocalPayloadSize_Type()
)
sdpBindCpipeLocalPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalPayloadSize.setUnits("bytes")
_SdpBindCpipePeerPayloadSize_Type = Unsigned32
_SdpBindCpipePeerPayloadSize_Object = MibTableColumn
sdpBindCpipePeerPayloadSize = _SdpBindCpipePeerPayloadSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 2),
    _SdpBindCpipePeerPayloadSize_Type()
)
sdpBindCpipePeerPayloadSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerPayloadSize.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerPayloadSize.setUnits("bytes")
_SdpBindCpipeLocalBitrate_Type = Unsigned32
_SdpBindCpipeLocalBitrate_Object = MibTableColumn
sdpBindCpipeLocalBitrate = _SdpBindCpipeLocalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 3),
    _SdpBindCpipeLocalBitrate_Type()
)
sdpBindCpipeLocalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalBitrate.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalBitrate.setUnits("64 Kbits/s")
_SdpBindCpipePeerBitrate_Type = Unsigned32
_SdpBindCpipePeerBitrate_Object = MibTableColumn
sdpBindCpipePeerBitrate = _SdpBindCpipePeerBitrate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 4),
    _SdpBindCpipePeerBitrate_Type()
)
sdpBindCpipePeerBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerBitrate.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerBitrate.setUnits("64 Kbits/s")
_SdpBindCpipeLocalSigPkts_Type = TdmOptionsSigPkts
_SdpBindCpipeLocalSigPkts_Object = MibTableColumn
sdpBindCpipeLocalSigPkts = _SdpBindCpipeLocalSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 5),
    _SdpBindCpipeLocalSigPkts_Type()
)
sdpBindCpipeLocalSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalSigPkts.setStatus("current")
_SdpBindCpipePeerSigPkts_Type = TdmOptionsSigPkts
_SdpBindCpipePeerSigPkts_Object = MibTableColumn
sdpBindCpipePeerSigPkts = _SdpBindCpipePeerSigPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 6),
    _SdpBindCpipePeerSigPkts_Type()
)
sdpBindCpipePeerSigPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerSigPkts.setStatus("current")
_SdpBindCpipeLocalCasTrunkFraming_Type = TdmOptionsCasTrunkFraming
_SdpBindCpipeLocalCasTrunkFraming_Object = MibTableColumn
sdpBindCpipeLocalCasTrunkFraming = _SdpBindCpipeLocalCasTrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 7),
    _SdpBindCpipeLocalCasTrunkFraming_Type()
)
sdpBindCpipeLocalCasTrunkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalCasTrunkFraming.setStatus("current")
_SdpBindCpipePeerCasTrunkFraming_Type = TdmOptionsCasTrunkFraming
_SdpBindCpipePeerCasTrunkFraming_Object = MibTableColumn
sdpBindCpipePeerCasTrunkFraming = _SdpBindCpipePeerCasTrunkFraming_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 8),
    _SdpBindCpipePeerCasTrunkFraming_Type()
)
sdpBindCpipePeerCasTrunkFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerCasTrunkFraming.setStatus("current")
_SdpBindCpipeLocalUseRtpHeader_Type = TruthValue
_SdpBindCpipeLocalUseRtpHeader_Object = MibTableColumn
sdpBindCpipeLocalUseRtpHeader = _SdpBindCpipeLocalUseRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 9),
    _SdpBindCpipeLocalUseRtpHeader_Type()
)
sdpBindCpipeLocalUseRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalUseRtpHeader.setStatus("current")
_SdpBindCpipePeerUseRtpHeader_Type = TruthValue
_SdpBindCpipePeerUseRtpHeader_Object = MibTableColumn
sdpBindCpipePeerUseRtpHeader = _SdpBindCpipePeerUseRtpHeader_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 10),
    _SdpBindCpipePeerUseRtpHeader_Type()
)
sdpBindCpipePeerUseRtpHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerUseRtpHeader.setStatus("current")
_SdpBindCpipeLocalDifferential_Type = TruthValue
_SdpBindCpipeLocalDifferential_Object = MibTableColumn
sdpBindCpipeLocalDifferential = _SdpBindCpipeLocalDifferential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 11),
    _SdpBindCpipeLocalDifferential_Type()
)
sdpBindCpipeLocalDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalDifferential.setStatus("current")
_SdpBindCpipePeerDifferential_Type = TruthValue
_SdpBindCpipePeerDifferential_Object = MibTableColumn
sdpBindCpipePeerDifferential = _SdpBindCpipePeerDifferential_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 12),
    _SdpBindCpipePeerDifferential_Type()
)
sdpBindCpipePeerDifferential.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerDifferential.setStatus("current")
_SdpBindCpipeLocalTimestampFreq_Type = Unsigned32
_SdpBindCpipeLocalTimestampFreq_Object = MibTableColumn
sdpBindCpipeLocalTimestampFreq = _SdpBindCpipeLocalTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 13),
    _SdpBindCpipeLocalTimestampFreq_Type()
)
sdpBindCpipeLocalTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipeLocalTimestampFreq.setUnits("8 KHz")
_SdpBindCpipePeerTimestampFreq_Type = Unsigned32
_SdpBindCpipePeerTimestampFreq_Object = MibTableColumn
sdpBindCpipePeerTimestampFreq = _SdpBindCpipePeerTimestampFreq_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 15, 1, 14),
    _SdpBindCpipePeerTimestampFreq_Type()
)
sdpBindCpipePeerTimestampFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindCpipePeerTimestampFreq.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindCpipePeerTimestampFreq.setUnits("8 KHz")
_SdpBindTlsL2ptStatsTable_Object = MibTable
sdpBindTlsL2ptStatsTable = _SdpBindTlsL2ptStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16)
)
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsTable.setStatus("current")
_SdpBindTlsL2ptStatsEntry_Object = MibTableRow
sdpBindTlsL2ptStatsEntry = _SdpBindTlsL2ptStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1)
)
sdpBindTlsL2ptStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsEntry.setStatus("current")
_SdpBindTlsL2ptStatsLastClearedTime_Type = TimeStamp
_SdpBindTlsL2ptStatsLastClearedTime_Object = MibTableColumn
sdpBindTlsL2ptStatsLastClearedTime = _SdpBindTlsL2ptStatsLastClearedTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 1),
    _SdpBindTlsL2ptStatsLastClearedTime_Type()
)
sdpBindTlsL2ptStatsLastClearedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsLastClearedTime.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 2),
    _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 3),
    _SdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 4),
    _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 5),
    _SdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 6),
    _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 7),
    _SdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 8),
    _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 9),
    _SdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 10),
    _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 11),
    _SdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 12),
    _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 13),
    _SdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpConfigBpdusRx = _SdpBindTlsL2ptStatsStpConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 14),
    _SdpBindTlsL2ptStatsStpConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpConfigBpdusTx = _SdpBindTlsL2ptStatsStpConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 15),
    _SdpBindTlsL2ptStatsStpConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpRstBpdusRx = _SdpBindTlsL2ptStatsStpRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 16),
    _SdpBindTlsL2ptStatsStpRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpRstBpdusTx = _SdpBindTlsL2ptStatsStpRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 17),
    _SdpBindTlsL2ptStatsStpRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsStpTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsStpTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpTcnBpdusRx = _SdpBindTlsL2ptStatsStpTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 18),
    _SdpBindTlsL2ptStatsStpTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsStpTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsStpTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsStpTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsStpTcnBpdusTx = _SdpBindTlsL2ptStatsStpTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 19),
    _SdpBindTlsL2ptStatsStpTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsStpTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsStpTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstConfigBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstConfigBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstConfigBpdusRx = _SdpBindTlsL2ptStatsPvstConfigBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 20),
    _SdpBindTlsL2ptStatsPvstConfigBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstConfigBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstConfigBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstConfigBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstConfigBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstConfigBpdusTx = _SdpBindTlsL2ptStatsPvstConfigBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 21),
    _SdpBindTlsL2ptStatsPvstConfigBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstConfigBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstConfigBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstRstBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstRstBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstRstBpdusRx = _SdpBindTlsL2ptStatsPvstRstBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 22),
    _SdpBindTlsL2ptStatsPvstRstBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstRstBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstRstBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstRstBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstRstBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstRstBpdusTx = _SdpBindTlsL2ptStatsPvstRstBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 23),
    _SdpBindTlsL2ptStatsPvstRstBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstRstBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstRstBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPvstTcnBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPvstTcnBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstTcnBpdusRx = _SdpBindTlsL2ptStatsPvstTcnBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 24),
    _SdpBindTlsL2ptStatsPvstTcnBpdusRx_Type()
)
sdpBindTlsL2ptStatsPvstTcnBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstTcnBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPvstTcnBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPvstTcnBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPvstTcnBpdusTx = _SdpBindTlsL2ptStatsPvstTcnBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 25),
    _SdpBindTlsL2ptStatsPvstTcnBpdusTx_Type()
)
sdpBindTlsL2ptStatsPvstTcnBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPvstTcnBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherBpdusRx = _SdpBindTlsL2ptStatsOtherBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 26),
    _SdpBindTlsL2ptStatsOtherBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherBpdusTx = _SdpBindTlsL2ptStatsOtherBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 27),
    _SdpBindTlsL2ptStatsOtherBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherL2ptBpdusRx = _SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 28),
    _SdpBindTlsL2ptStatsOtherL2ptBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherL2ptBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherL2ptBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherL2ptBpdusTx = _SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 29),
    _SdpBindTlsL2ptStatsOtherL2ptBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherL2ptBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherL2ptBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherInvalidBpdusRx = _SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 30),
    _SdpBindTlsL2ptStatsOtherInvalidBpdusRx_Type()
)
sdpBindTlsL2ptStatsOtherInvalidBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherInvalidBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsOtherInvalidBpdusTx = _SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 31),
    _SdpBindTlsL2ptStatsOtherInvalidBpdusTx_Type()
)
sdpBindTlsL2ptStatsOtherInvalidBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsOtherInvalidBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 32),
    _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 33),
    _SdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 34),
    _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 35),
    _SdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 36),
    _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 37),
    _SdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 38),
    _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 39),
    _SdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx = _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 40),
    _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx = _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 41),
    _SdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx_Type()
)
sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsCdpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsCdpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsCdpBpdusRx = _SdpBindTlsL2ptStatsCdpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 42),
    _SdpBindTlsL2ptStatsCdpBpdusRx_Type()
)
sdpBindTlsL2ptStatsCdpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsCdpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsCdpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsCdpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsCdpBpdusTx = _SdpBindTlsL2ptStatsCdpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 43),
    _SdpBindTlsL2ptStatsCdpBpdusTx_Type()
)
sdpBindTlsL2ptStatsCdpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsCdpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsVtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsVtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsVtpBpdusRx = _SdpBindTlsL2ptStatsVtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 44),
    _SdpBindTlsL2ptStatsVtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsVtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsVtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsVtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsVtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsVtpBpdusTx = _SdpBindTlsL2ptStatsVtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 45),
    _SdpBindTlsL2ptStatsVtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsVtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsVtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsDtpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsDtpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsDtpBpdusRx = _SdpBindTlsL2ptStatsDtpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 46),
    _SdpBindTlsL2ptStatsDtpBpdusRx_Type()
)
sdpBindTlsL2ptStatsDtpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsDtpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsDtpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsDtpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsDtpBpdusTx = _SdpBindTlsL2ptStatsDtpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 47),
    _SdpBindTlsL2ptStatsDtpBpdusTx_Type()
)
sdpBindTlsL2ptStatsDtpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsDtpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsPagpBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsPagpBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsPagpBpdusRx = _SdpBindTlsL2ptStatsPagpBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 48),
    _SdpBindTlsL2ptStatsPagpBpdusRx_Type()
)
sdpBindTlsL2ptStatsPagpBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPagpBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsPagpBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsPagpBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsPagpBpdusTx = _SdpBindTlsL2ptStatsPagpBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 49),
    _SdpBindTlsL2ptStatsPagpBpdusTx_Type()
)
sdpBindTlsL2ptStatsPagpBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsPagpBpdusTx.setStatus("current")
_SdpBindTlsL2ptStatsUdldBpdusRx_Type = Counter32
_SdpBindTlsL2ptStatsUdldBpdusRx_Object = MibTableColumn
sdpBindTlsL2ptStatsUdldBpdusRx = _SdpBindTlsL2ptStatsUdldBpdusRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 50),
    _SdpBindTlsL2ptStatsUdldBpdusRx_Type()
)
sdpBindTlsL2ptStatsUdldBpdusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsUdldBpdusRx.setStatus("current")
_SdpBindTlsL2ptStatsUdldBpdusTx_Type = Counter32
_SdpBindTlsL2ptStatsUdldBpdusTx_Object = MibTableColumn
sdpBindTlsL2ptStatsUdldBpdusTx = _SdpBindTlsL2ptStatsUdldBpdusTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 16, 1, 51),
    _SdpBindTlsL2ptStatsUdldBpdusTx_Type()
)
sdpBindTlsL2ptStatsUdldBpdusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsL2ptStatsUdldBpdusTx.setStatus("current")
_PwTemplateTableLastChanged_Type = TimeStamp
_PwTemplateTableLastChanged_Object = MibScalar
pwTemplateTableLastChanged = _PwTemplateTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 17),
    _PwTemplateTableLastChanged_Type()
)
pwTemplateTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateTableLastChanged.setStatus("current")
_PwTemplateTable_Object = MibTable
pwTemplateTable = _PwTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18)
)
if mibBuilder.loadTexts:
    pwTemplateTable.setStatus("current")
_PwTemplateEntry_Object = MibTableRow
pwTemplateEntry = _PwTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1)
)
pwTemplateEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateId"),
)
if mibBuilder.loadTexts:
    pwTemplateEntry.setStatus("current")
_PwTemplateId_Type = PWTemplateId
_PwTemplateId_Object = MibTableColumn
pwTemplateId = _PwTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 1),
    _PwTemplateId_Type()
)
pwTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateId.setStatus("current")
_PwTemplateRowStatus_Type = RowStatus
_PwTemplateRowStatus_Object = MibTableColumn
pwTemplateRowStatus = _PwTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 2),
    _PwTemplateRowStatus_Type()
)
pwTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateRowStatus.setStatus("current")
_PwTemplateLastChanged_Type = TimeStamp
_PwTemplateLastChanged_Object = MibTableColumn
pwTemplateLastChanged = _PwTemplateLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 3),
    _PwTemplateLastChanged_Type()
)
pwTemplateLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateLastChanged.setStatus("current")


class _PwTemplateUseProvisionedSdp_Type(TruthValue):
    """Custom type pwTemplateUseProvisionedSdp based on TruthValue"""


_PwTemplateUseProvisionedSdp_Object = MibTableColumn
pwTemplateUseProvisionedSdp = _PwTemplateUseProvisionedSdp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 4),
    _PwTemplateUseProvisionedSdp_Type()
)
pwTemplateUseProvisionedSdp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateUseProvisionedSdp.setStatus("current")


class _PwTemplateVcType_Type(SdpBindVcType):
    """Custom type pwTemplateVcType based on SdpBindVcType"""


_PwTemplateVcType_Object = MibTableColumn
pwTemplateVcType = _PwTemplateVcType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 5),
    _PwTemplateVcType_Type()
)
pwTemplateVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateVcType.setStatus("current")


class _PwTemplateAccountingPolicyId_Type(Unsigned32):
    """Custom type pwTemplateAccountingPolicyId based on Unsigned32"""
    defaultValue = 0


_PwTemplateAccountingPolicyId_Object = MibTableColumn
pwTemplateAccountingPolicyId = _PwTemplateAccountingPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 6),
    _PwTemplateAccountingPolicyId_Type()
)
pwTemplateAccountingPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateAccountingPolicyId.setStatus("current")


class _PwTemplateCollectAcctStats_Type(TruthValue):
    """Custom type pwTemplateCollectAcctStats based on TruthValue"""


_PwTemplateCollectAcctStats_Object = MibTableColumn
pwTemplateCollectAcctStats = _PwTemplateCollectAcctStats_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 7),
    _PwTemplateCollectAcctStats_Type()
)
pwTemplateCollectAcctStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateCollectAcctStats.setStatus("current")


class _PwTemplateMacLearning_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacLearning based on TmnxEnabledDisabled"""


_PwTemplateMacLearning_Object = MibTableColumn
pwTemplateMacLearning = _PwTemplateMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 8),
    _PwTemplateMacLearning_Type()
)
pwTemplateMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacLearning.setStatus("current")


class _PwTemplateMacAgeing_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacAgeing based on TmnxEnabledDisabled"""


_PwTemplateMacAgeing_Object = MibTableColumn
pwTemplateMacAgeing = _PwTemplateMacAgeing_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 9),
    _PwTemplateMacAgeing_Type()
)
pwTemplateMacAgeing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacAgeing.setStatus("current")


class _PwTemplateDiscardUnknownSource_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateDiscardUnknownSource based on TmnxEnabledDisabled"""


_PwTemplateDiscardUnknownSource_Object = MibTableColumn
pwTemplateDiscardUnknownSource = _PwTemplateDiscardUnknownSource_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 10),
    _PwTemplateDiscardUnknownSource_Type()
)
pwTemplateDiscardUnknownSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateDiscardUnknownSource.setStatus("current")


class _PwTemplateLimitMacMove_Type(TlsLimitMacMove):
    """Custom type pwTemplateLimitMacMove based on TlsLimitMacMove"""


_PwTemplateLimitMacMove_Object = MibTableColumn
pwTemplateLimitMacMove = _PwTemplateLimitMacMove_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 11),
    _PwTemplateLimitMacMove_Type()
)
pwTemplateLimitMacMove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateLimitMacMove.setStatus("current")


class _PwTemplateMacPinning_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateMacPinning based on TmnxEnabledDisabled"""


_PwTemplateMacPinning_Object = MibTableColumn
pwTemplateMacPinning = _PwTemplateMacPinning_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 12),
    _PwTemplateMacPinning_Type()
)
pwTemplateMacPinning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacPinning.setStatus("current")


class _PwTemplateVlanVcTag_Type(Unsigned32):
    """Custom type pwTemplateVlanVcTag based on Unsigned32"""
    defaultHexValue = 4095

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_PwTemplateVlanVcTag_Type.__name__ = "Unsigned32"
_PwTemplateVlanVcTag_Object = MibTableColumn
pwTemplateVlanVcTag = _PwTemplateVlanVcTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 13),
    _PwTemplateVlanVcTag_Type()
)
pwTemplateVlanVcTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateVlanVcTag.setStatus("current")


class _PwTemplateMacAddressLimit_Type(Unsigned32):
    """Custom type pwTemplateMacAddressLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 196607),
    )


_PwTemplateMacAddressLimit_Type.__name__ = "Unsigned32"
_PwTemplateMacAddressLimit_Object = MibTableColumn
pwTemplateMacAddressLimit = _PwTemplateMacAddressLimit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 14),
    _PwTemplateMacAddressLimit_Type()
)
pwTemplateMacAddressLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMacAddressLimit.setStatus("current")
_PwTemplateShgName_Type = TNamedItemOrEmpty
_PwTemplateShgName_Object = MibTableColumn
pwTemplateShgName = _PwTemplateShgName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 15),
    _PwTemplateShgName_Type()
)
pwTemplateShgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgName.setStatus("current")
_PwTemplateShgDescription_Type = TItemDescription
_PwTemplateShgDescription_Object = MibTableColumn
pwTemplateShgDescription = _PwTemplateShgDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 16),
    _PwTemplateShgDescription_Type()
)
pwTemplateShgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgDescription.setStatus("current")


class _PwTemplateShgRestProtSrcMac_Type(TruthValue):
    """Custom type pwTemplateShgRestProtSrcMac based on TruthValue"""


_PwTemplateShgRestProtSrcMac_Object = MibTableColumn
pwTemplateShgRestProtSrcMac = _PwTemplateShgRestProtSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 17),
    _PwTemplateShgRestProtSrcMac_Type()
)
pwTemplateShgRestProtSrcMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgRestProtSrcMac.setStatus("current")


class _PwTemplateShgRestUnprotDstMac_Type(TruthValue):
    """Custom type pwTemplateShgRestUnprotDstMac based on TruthValue"""


_PwTemplateShgRestUnprotDstMac_Object = MibTableColumn
pwTemplateShgRestUnprotDstMac = _PwTemplateShgRestUnprotDstMac_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 18),
    _PwTemplateShgRestUnprotDstMac_Type()
)
pwTemplateShgRestUnprotDstMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateShgRestUnprotDstMac.setStatus("current")


class _PwTemplateEgressMacFilterId_Type(TFilterID):
    """Custom type pwTemplateEgressMacFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressMacFilterId_Object = MibTableColumn
pwTemplateEgressMacFilterId = _PwTemplateEgressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 19),
    _PwTemplateEgressMacFilterId_Type()
)
pwTemplateEgressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressMacFilterId.setStatus("current")


class _PwTemplateEgressIpFilterId_Type(TFilterID):
    """Custom type pwTemplateEgressIpFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressIpFilterId_Object = MibTableColumn
pwTemplateEgressIpFilterId = _PwTemplateEgressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 20),
    _PwTemplateEgressIpFilterId_Type()
)
pwTemplateEgressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpFilterId.setStatus("current")


class _PwTemplateEgressIpv6FilterId_Type(TFilterID):
    """Custom type pwTemplateEgressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateEgressIpv6FilterId_Object = MibTableColumn
pwTemplateEgressIpv6FilterId = _PwTemplateEgressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 21),
    _PwTemplateEgressIpv6FilterId_Type()
)
pwTemplateEgressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateEgressIpv6FilterId.setStatus("current")


class _PwTemplateIngressMacFilterId_Type(TFilterID):
    """Custom type pwTemplateIngressMacFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressMacFilterId_Object = MibTableColumn
pwTemplateIngressMacFilterId = _PwTemplateIngressMacFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 22),
    _PwTemplateIngressMacFilterId_Type()
)
pwTemplateIngressMacFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressMacFilterId.setStatus("current")


class _PwTemplateIngressIpFilterId_Type(TFilterID):
    """Custom type pwTemplateIngressIpFilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressIpFilterId_Object = MibTableColumn
pwTemplateIngressIpFilterId = _PwTemplateIngressIpFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 23),
    _PwTemplateIngressIpFilterId_Type()
)
pwTemplateIngressIpFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpFilterId.setStatus("current")


class _PwTemplateIngressIpv6FilterId_Type(TFilterID):
    """Custom type pwTemplateIngressIpv6FilterId based on TFilterID"""
    defaultValue = 0


_PwTemplateIngressIpv6FilterId_Object = MibTableColumn
pwTemplateIngressIpv6FilterId = _PwTemplateIngressIpv6FilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 24),
    _PwTemplateIngressIpv6FilterId_Type()
)
pwTemplateIngressIpv6FilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIngressIpv6FilterId.setStatus("current")


class _PwTemplateIgmpFastLeave_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpFastLeave based on TmnxEnabledDisabled"""


_PwTemplateIgmpFastLeave_Object = MibTableColumn
pwTemplateIgmpFastLeave = _PwTemplateIgmpFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 25),
    _PwTemplateIgmpFastLeave_Type()
)
pwTemplateIgmpFastLeave.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpFastLeave.setStatus("current")
_PwTemplateIgmpImportPlcy_Type = TNamedItemOrEmpty
_PwTemplateIgmpImportPlcy_Object = MibTableColumn
pwTemplateIgmpImportPlcy = _PwTemplateIgmpImportPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 26),
    _PwTemplateIgmpImportPlcy_Type()
)
pwTemplateIgmpImportPlcy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpImportPlcy.setStatus("current")


class _PwTemplateIgmpLastMembIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpLastMembIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_PwTemplateIgmpLastMembIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpLastMembIntvl_Object = MibTableColumn
pwTemplateIgmpLastMembIntvl = _PwTemplateIgmpLastMembIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 27),
    _PwTemplateIgmpLastMembIntvl_Type()
)
pwTemplateIgmpLastMembIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpLastMembIntvl.setUnits("deci-seconds")


class _PwTemplateIgmpMaxNbrGrps_Type(Unsigned32):
    """Custom type pwTemplateIgmpMaxNbrGrps based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_PwTemplateIgmpMaxNbrGrps_Type.__name__ = "Unsigned32"
_PwTemplateIgmpMaxNbrGrps_Object = MibTableColumn
pwTemplateIgmpMaxNbrGrps = _PwTemplateIgmpMaxNbrGrps_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 28),
    _PwTemplateIgmpMaxNbrGrps_Type()
)
pwTemplateIgmpMaxNbrGrps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMaxNbrGrps.setStatus("current")


class _PwTemplateIgmpGenQueryIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpGenQueryIntvl based on Unsigned32"""
    defaultValue = 125

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_PwTemplateIgmpGenQueryIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpGenQueryIntvl_Object = MibTableColumn
pwTemplateIgmpGenQueryIntvl = _PwTemplateIgmpGenQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 29),
    _PwTemplateIgmpGenQueryIntvl_Type()
)
pwTemplateIgmpGenQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpGenQueryIntvl.setUnits("seconds")


class _PwTemplateIgmpQueryRespIntvl_Type(Unsigned32):
    """Custom type pwTemplateIgmpQueryRespIntvl based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_PwTemplateIgmpQueryRespIntvl_Type.__name__ = "Unsigned32"
_PwTemplateIgmpQueryRespIntvl_Object = MibTableColumn
pwTemplateIgmpQueryRespIntvl = _PwTemplateIgmpQueryRespIntvl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 30),
    _PwTemplateIgmpQueryRespIntvl_Type()
)
pwTemplateIgmpQueryRespIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpQueryRespIntvl.setUnits("seconds")


class _PwTemplateIgmpRobustCount_Type(Unsigned32):
    """Custom type pwTemplateIgmpRobustCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
    )


_PwTemplateIgmpRobustCount_Type.__name__ = "Unsigned32"
_PwTemplateIgmpRobustCount_Object = MibTableColumn
pwTemplateIgmpRobustCount = _PwTemplateIgmpRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 31),
    _PwTemplateIgmpRobustCount_Type()
)
pwTemplateIgmpRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpRobustCount.setStatus("current")


class _PwTemplateIgmpSendQueries_Type(TmnxEnabledDisabled):
    """Custom type pwTemplateIgmpSendQueries based on TmnxEnabledDisabled"""


_PwTemplateIgmpSendQueries_Object = MibTableColumn
pwTemplateIgmpSendQueries = _PwTemplateIgmpSendQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 32),
    _PwTemplateIgmpSendQueries_Type()
)
pwTemplateIgmpSendQueries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSendQueries.setStatus("current")
_PwTemplateIgmpMcacPolicyName_Type = TPolicyStatementNameOrEmpty
_PwTemplateIgmpMcacPolicyName_Object = MibTableColumn
pwTemplateIgmpMcacPolicyName = _PwTemplateIgmpMcacPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 33),
    _PwTemplateIgmpMcacPolicyName_Type()
)
pwTemplateIgmpMcacPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPolicyName.setStatus("current")


class _PwTemplateIgmpMcacUnconstBW_Type(Integer32):
    """Custom type pwTemplateIgmpMcacUnconstBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_PwTemplateIgmpMcacUnconstBW_Type.__name__ = "Integer32"
_PwTemplateIgmpMcacUnconstBW_Object = MibTableColumn
pwTemplateIgmpMcacUnconstBW = _PwTemplateIgmpMcacUnconstBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 34),
    _PwTemplateIgmpMcacUnconstBW_Type()
)
pwTemplateIgmpMcacUnconstBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacUnconstBW.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacUnconstBW.setUnits("kbps")


class _PwTemplateIgmpMcacPrRsvMndBW_Type(Integer32):
    """Custom type pwTemplateIgmpMcacPrRsvMndBW based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_PwTemplateIgmpMcacPrRsvMndBW_Type.__name__ = "Integer32"
_PwTemplateIgmpMcacPrRsvMndBW_Object = MibTableColumn
pwTemplateIgmpMcacPrRsvMndBW = _PwTemplateIgmpMcacPrRsvMndBW_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 35),
    _PwTemplateIgmpMcacPrRsvMndBW_Type()
)
pwTemplateIgmpMcacPrRsvMndBW.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPrRsvMndBW.setStatus("current")
if mibBuilder.loadTexts:
    pwTemplateIgmpMcacPrRsvMndBW.setUnits("kbps")


class _PwTemplateIgmpVersion_Type(TmnxIgmpVersion):
    """Custom type pwTemplateIgmpVersion based on TmnxIgmpVersion"""


_PwTemplateIgmpVersion_Object = MibTableColumn
pwTemplateIgmpVersion = _PwTemplateIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 18, 1, 36),
    _PwTemplateIgmpVersion_Type()
)
pwTemplateIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpVersion.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTblLC_Type = TimeStamp
_PwTemplateIgmpSnpgGrpSrcTblLC_Object = MibScalar
pwTemplateIgmpSnpgGrpSrcTblLC = _PwTemplateIgmpSnpgGrpSrcTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 19),
    _PwTemplateIgmpSnpgGrpSrcTblLC_Type()
)
pwTemplateIgmpSnpgGrpSrcTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTblLC.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcTable_Object = MibTable
pwTemplateIgmpSnpgGrpSrcTable = _PwTemplateIgmpSnpgGrpSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20)
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcTable.setStatus("current")
_PwTemplateIgmpSnpgGrpSrcEntry_Object = MibTableRow
pwTemplateIgmpSnpgGrpSrcEntry = _PwTemplateIgmpSnpgGrpSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1)
)
pwTemplateIgmpSnpgGrpSrcEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpAddr"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgSrcAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgSrcAddr"),
)
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpSrcEntry.setStatus("current")
_PwTemplateIgmpSnpgGrpAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgGrpAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddrType = _PwTemplateIgmpSnpgGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 1),
    _PwTemplateIgmpSnpgGrpAddrType_Type()
)
pwTemplateIgmpSnpgGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddrType.setStatus("current")


class _PwTemplateIgmpSnpgGrpAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgGrpAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgGrpAddr_Object = MibTableColumn
pwTemplateIgmpSnpgGrpAddr = _PwTemplateIgmpSnpgGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 2),
    _PwTemplateIgmpSnpgGrpAddr_Type()
)
pwTemplateIgmpSnpgGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgGrpAddr.setStatus("current")
_PwTemplateIgmpSnpgSrcAddrType_Type = InetAddressType
_PwTemplateIgmpSnpgSrcAddrType_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddrType = _PwTemplateIgmpSnpgSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 3),
    _PwTemplateIgmpSnpgSrcAddrType_Type()
)
pwTemplateIgmpSnpgSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddrType.setStatus("current")


class _PwTemplateIgmpSnpgSrcAddr_Type(InetAddress):
    """Custom type pwTemplateIgmpSnpgSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_PwTemplateIgmpSnpgSrcAddr_Type.__name__ = "InetAddress"
_PwTemplateIgmpSnpgSrcAddr_Object = MibTableColumn
pwTemplateIgmpSnpgSrcAddr = _PwTemplateIgmpSnpgSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 4),
    _PwTemplateIgmpSnpgSrcAddr_Type()
)
pwTemplateIgmpSnpgSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgSrcAddr.setStatus("current")
_PwTemplateIgmpSnpgRowStatus_Type = RowStatus
_PwTemplateIgmpSnpgRowStatus_Object = MibTableColumn
pwTemplateIgmpSnpgRowStatus = _PwTemplateIgmpSnpgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 5),
    _PwTemplateIgmpSnpgRowStatus_Type()
)
pwTemplateIgmpSnpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgRowStatus.setStatus("current")
_PwTemplateIgmpSnpgLastChngd_Type = TimeStamp
_PwTemplateIgmpSnpgLastChngd_Object = MibTableColumn
pwTemplateIgmpSnpgLastChngd = _PwTemplateIgmpSnpgLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 20, 1, 6),
    _PwTemplateIgmpSnpgLastChngd_Type()
)
pwTemplateIgmpSnpgLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateIgmpSnpgLastChngd.setStatus("current")
_PwTemplateMfibAllowedMdaTblLC_Type = TimeStamp
_PwTemplateMfibAllowedMdaTblLC_Object = MibScalar
pwTemplateMfibAllowedMdaTblLC = _PwTemplateMfibAllowedMdaTblLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 21),
    _PwTemplateMfibAllowedMdaTblLC_Type()
)
pwTemplateMfibAllowedMdaTblLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaTblLC.setStatus("current")
_PwTemplateMfibAllowedMdaTable_Object = MibTable
pwTemplateMfibAllowedMdaTable = _PwTemplateMfibAllowedMdaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22)
)
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaTable.setStatus("current")
_PwTemplateMfibAllowedMdaEntry_Object = MibTableRow
pwTemplateMfibAllowedMdaEntry = _PwTemplateMfibAllowedMdaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22, 1)
)
pwTemplateMfibAllowedMdaEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateId"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxCardSlotNum"),
    (0, "ALCATEL-IND1-TIMETRA-CHASSIS-MIB", "tmnxMDASlotNum"),
)
if mibBuilder.loadTexts:
    pwTemplateMfibAllowedMdaEntry.setStatus("current")
_PwTemplateMfibMdaRowStatus_Type = RowStatus
_PwTemplateMfibMdaRowStatus_Object = MibTableColumn
pwTemplateMfibMdaRowStatus = _PwTemplateMfibMdaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 22, 1, 1),
    _PwTemplateMfibMdaRowStatus_Type()
)
pwTemplateMfibMdaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pwTemplateMfibMdaRowStatus.setStatus("current")
_SdpBindTlsMrpTableLastChanged_Type = TimeStamp
_SdpBindTlsMrpTableLastChanged_Object = MibScalar
sdpBindTlsMrpTableLastChanged = _SdpBindTlsMrpTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 23),
    _SdpBindTlsMrpTableLastChanged_Type()
)
sdpBindTlsMrpTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTableLastChanged.setStatus("current")
_SdpBindTlsMrpTable_Object = MibTable
sdpBindTlsMrpTable = _SdpBindTlsMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24)
)
if mibBuilder.loadTexts:
    sdpBindTlsMrpTable.setStatus("current")
_SdpBindTlsMrpEntry_Object = MibTableRow
sdpBindTlsMrpEntry = _SdpBindTlsMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1)
)
sdpBindTlsMrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMrpEntry.setStatus("current")
_SdpBindTlsMrpLastChngd_Type = TimeStamp
_SdpBindTlsMrpLastChngd_Object = MibTableColumn
sdpBindTlsMrpLastChngd = _SdpBindTlsMrpLastChngd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 1),
    _SdpBindTlsMrpLastChngd_Type()
)
sdpBindTlsMrpLastChngd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLastChngd.setStatus("current")


class _SdpBindTlsMrpJoinTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpJoinTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SdpBindTlsMrpJoinTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpJoinTime_Object = MibTableColumn
sdpBindTlsMrpJoinTime = _SdpBindTlsMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 2),
    _SdpBindTlsMrpJoinTime_Type()
)
sdpBindTlsMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpJoinTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpJoinTime.setUnits("deci-seconds")


class _SdpBindTlsMrpLeaveTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpLeaveTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 60),
    )


_SdpBindTlsMrpLeaveTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpLeaveTime_Object = MibTableColumn
sdpBindTlsMrpLeaveTime = _SdpBindTlsMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 3),
    _SdpBindTlsMrpLeaveTime_Type()
)
sdpBindTlsMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveTime.setUnits("deci-seconds")


class _SdpBindTlsMrpLeaveAllTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpLeaveAllTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_SdpBindTlsMrpLeaveAllTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpLeaveAllTime_Object = MibTableColumn
sdpBindTlsMrpLeaveAllTime = _SdpBindTlsMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 4),
    _SdpBindTlsMrpLeaveAllTime_Type()
)
sdpBindTlsMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveAllTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpLeaveAllTime.setUnits("deci-seconds")


class _SdpBindTlsMrpPeriodicTime_Type(Unsigned32):
    """Custom type sdpBindTlsMrpPeriodicTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SdpBindTlsMrpPeriodicTime_Type.__name__ = "Unsigned32"
_SdpBindTlsMrpPeriodicTime_Object = MibTableColumn
sdpBindTlsMrpPeriodicTime = _SdpBindTlsMrpPeriodicTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 5),
    _SdpBindTlsMrpPeriodicTime_Type()
)
sdpBindTlsMrpPeriodicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicTime.setStatus("current")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicTime.setUnits("deci-seconds")


class _SdpBindTlsMrpPeriodicEnabled_Type(TruthValue):
    """Custom type sdpBindTlsMrpPeriodicEnabled based on TruthValue"""


_SdpBindTlsMrpPeriodicEnabled_Object = MibTableColumn
sdpBindTlsMrpPeriodicEnabled = _SdpBindTlsMrpPeriodicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 6),
    _SdpBindTlsMrpPeriodicEnabled_Type()
)
sdpBindTlsMrpPeriodicEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdpBindTlsMrpPeriodicEnabled.setStatus("current")
_SdpBindTlsMrpRxPdus_Type = Counter32
_SdpBindTlsMrpRxPdus_Object = MibTableColumn
sdpBindTlsMrpRxPdus = _SdpBindTlsMrpRxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 7),
    _SdpBindTlsMrpRxPdus_Type()
)
sdpBindTlsMrpRxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxPdus.setStatus("current")
_SdpBindTlsMrpDroppedPdus_Type = Counter32
_SdpBindTlsMrpDroppedPdus_Object = MibTableColumn
sdpBindTlsMrpDroppedPdus = _SdpBindTlsMrpDroppedPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 8),
    _SdpBindTlsMrpDroppedPdus_Type()
)
sdpBindTlsMrpDroppedPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpDroppedPdus.setStatus("current")
_SdpBindTlsMrpTxPdus_Type = Counter32
_SdpBindTlsMrpTxPdus_Object = MibTableColumn
sdpBindTlsMrpTxPdus = _SdpBindTlsMrpTxPdus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 9),
    _SdpBindTlsMrpTxPdus_Type()
)
sdpBindTlsMrpTxPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxPdus.setStatus("current")
_SdpBindTlsMrpRxNewEvent_Type = Counter32
_SdpBindTlsMrpRxNewEvent_Object = MibTableColumn
sdpBindTlsMrpRxNewEvent = _SdpBindTlsMrpRxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 10),
    _SdpBindTlsMrpRxNewEvent_Type()
)
sdpBindTlsMrpRxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxNewEvent.setStatus("current")
_SdpBindTlsMrpRxJoinInEvent_Type = Counter32
_SdpBindTlsMrpRxJoinInEvent_Object = MibTableColumn
sdpBindTlsMrpRxJoinInEvent = _SdpBindTlsMrpRxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 11),
    _SdpBindTlsMrpRxJoinInEvent_Type()
)
sdpBindTlsMrpRxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxJoinInEvent.setStatus("current")
_SdpBindTlsMrpRxInEvent_Type = Counter32
_SdpBindTlsMrpRxInEvent_Object = MibTableColumn
sdpBindTlsMrpRxInEvent = _SdpBindTlsMrpRxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 12),
    _SdpBindTlsMrpRxInEvent_Type()
)
sdpBindTlsMrpRxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxInEvent.setStatus("current")
_SdpBindTlsMrpRxJoinEmptyEvent_Type = Counter32
_SdpBindTlsMrpRxJoinEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpRxJoinEmptyEvent = _SdpBindTlsMrpRxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 13),
    _SdpBindTlsMrpRxJoinEmptyEvent_Type()
)
sdpBindTlsMrpRxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxJoinEmptyEvent.setStatus("current")
_SdpBindTlsMrpRxEmptyEvent_Type = Counter32
_SdpBindTlsMrpRxEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpRxEmptyEvent = _SdpBindTlsMrpRxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 14),
    _SdpBindTlsMrpRxEmptyEvent_Type()
)
sdpBindTlsMrpRxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxEmptyEvent.setStatus("current")
_SdpBindTlsMrpRxLeaveEvent_Type = Counter32
_SdpBindTlsMrpRxLeaveEvent_Object = MibTableColumn
sdpBindTlsMrpRxLeaveEvent = _SdpBindTlsMrpRxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 15),
    _SdpBindTlsMrpRxLeaveEvent_Type()
)
sdpBindTlsMrpRxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpRxLeaveEvent.setStatus("current")
_SdpBindTlsMrpTxNewEvent_Type = Counter32
_SdpBindTlsMrpTxNewEvent_Object = MibTableColumn
sdpBindTlsMrpTxNewEvent = _SdpBindTlsMrpTxNewEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 16),
    _SdpBindTlsMrpTxNewEvent_Type()
)
sdpBindTlsMrpTxNewEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxNewEvent.setStatus("current")
_SdpBindTlsMrpTxJoinInEvent_Type = Counter32
_SdpBindTlsMrpTxJoinInEvent_Object = MibTableColumn
sdpBindTlsMrpTxJoinInEvent = _SdpBindTlsMrpTxJoinInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 17),
    _SdpBindTlsMrpTxJoinInEvent_Type()
)
sdpBindTlsMrpTxJoinInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxJoinInEvent.setStatus("current")
_SdpBindTlsMrpTxInEvent_Type = Counter32
_SdpBindTlsMrpTxInEvent_Object = MibTableColumn
sdpBindTlsMrpTxInEvent = _SdpBindTlsMrpTxInEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 18),
    _SdpBindTlsMrpTxInEvent_Type()
)
sdpBindTlsMrpTxInEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxInEvent.setStatus("current")
_SdpBindTlsMrpTxJoinEmptyEvent_Type = Counter32
_SdpBindTlsMrpTxJoinEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpTxJoinEmptyEvent = _SdpBindTlsMrpTxJoinEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 19),
    _SdpBindTlsMrpTxJoinEmptyEvent_Type()
)
sdpBindTlsMrpTxJoinEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxJoinEmptyEvent.setStatus("current")
_SdpBindTlsMrpTxEmptyEvent_Type = Counter32
_SdpBindTlsMrpTxEmptyEvent_Object = MibTableColumn
sdpBindTlsMrpTxEmptyEvent = _SdpBindTlsMrpTxEmptyEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 20),
    _SdpBindTlsMrpTxEmptyEvent_Type()
)
sdpBindTlsMrpTxEmptyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxEmptyEvent.setStatus("current")
_SdpBindTlsMrpTxLeaveEvent_Type = Counter32
_SdpBindTlsMrpTxLeaveEvent_Object = MibTableColumn
sdpBindTlsMrpTxLeaveEvent = _SdpBindTlsMrpTxLeaveEvent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 24, 1, 21),
    _SdpBindTlsMrpTxLeaveEvent_Type()
)
sdpBindTlsMrpTxLeaveEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMrpTxLeaveEvent.setStatus("current")
_SdpBindTlsMmrpTable_Object = MibTable
sdpBindTlsMmrpTable = _SdpBindTlsMmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25)
)
if mibBuilder.loadTexts:
    sdpBindTlsMmrpTable.setStatus("current")
_SdpBindTlsMmrpEntry_Object = MibTableRow
sdpBindTlsMmrpEntry = _SdpBindTlsMmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1)
)
sdpBindTlsMmrpEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMmrpMacAddr"),
)
if mibBuilder.loadTexts:
    sdpBindTlsMmrpEntry.setStatus("current")
_SdpBindTlsMmrpMacAddr_Type = MacAddress
_SdpBindTlsMmrpMacAddr_Object = MibTableColumn
sdpBindTlsMmrpMacAddr = _SdpBindTlsMmrpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 1),
    _SdpBindTlsMmrpMacAddr_Type()
)
sdpBindTlsMmrpMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpMacAddr.setStatus("current")
_SdpBindTlsMmrpDeclared_Type = TruthValue
_SdpBindTlsMmrpDeclared_Object = MibTableColumn
sdpBindTlsMmrpDeclared = _SdpBindTlsMmrpDeclared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 2),
    _SdpBindTlsMmrpDeclared_Type()
)
sdpBindTlsMmrpDeclared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpDeclared.setStatus("current")
_SdpBindTlsMmrpRegistered_Type = TruthValue
_SdpBindTlsMmrpRegistered_Object = MibTableColumn
sdpBindTlsMmrpRegistered = _SdpBindTlsMmrpRegistered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 25, 1, 3),
    _SdpBindTlsMmrpRegistered_Type()
)
sdpBindTlsMmrpRegistered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpBindTlsMmrpRegistered.setStatus("current")
_SdpAutoBindBgpInfoTableLC_Type = TimeStamp
_SdpAutoBindBgpInfoTableLC_Object = MibScalar
sdpAutoBindBgpInfoTableLC = _SdpAutoBindBgpInfoTableLC_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 26),
    _SdpAutoBindBgpInfoTableLC_Type()
)
sdpAutoBindBgpInfoTableLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTableLC.setStatus("current")
_SdpAutoBindBgpInfoTable_Object = MibTable
sdpAutoBindBgpInfoTable = _SdpAutoBindBgpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27)
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTable.setStatus("current")
_SdpAutoBindBgpInfoEntry_Object = MibTableRow
sdpAutoBindBgpInfoEntry = _SdpAutoBindBgpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1)
)
sdpAutoBindBgpInfoEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
    (0, "ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
)
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoEntry.setStatus("current")
_SdpAutoBindBgpInfoTemplateId_Type = PWTemplateId
_SdpAutoBindBgpInfoTemplateId_Object = MibTableColumn
sdpAutoBindBgpInfoTemplateId = _SdpAutoBindBgpInfoTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 1),
    _SdpAutoBindBgpInfoTemplateId_Type()
)
sdpAutoBindBgpInfoTemplateId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTemplateId.setStatus("current")
_SdpAutoBindBgpInfoAGI_Type = TmnxVPNRouteDistinguisher
_SdpAutoBindBgpInfoAGI_Object = MibTableColumn
sdpAutoBindBgpInfoAGI = _SdpAutoBindBgpInfoAGI_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 2),
    _SdpAutoBindBgpInfoAGI_Type()
)
sdpAutoBindBgpInfoAGI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoAGI.setStatus("current")
_SdpAutoBindBgpInfoSAII_Type = Unsigned32
_SdpAutoBindBgpInfoSAII_Object = MibTableColumn
sdpAutoBindBgpInfoSAII = _SdpAutoBindBgpInfoSAII_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 3),
    _SdpAutoBindBgpInfoSAII_Type()
)
sdpAutoBindBgpInfoSAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoSAII.setStatus("current")
_SdpAutoBindBgpInfoTAII_Type = Unsigned32
_SdpAutoBindBgpInfoTAII_Object = MibTableColumn
sdpAutoBindBgpInfoTAII = _SdpAutoBindBgpInfoTAII_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 27, 1, 4),
    _SdpAutoBindBgpInfoTAII_Type()
)
sdpAutoBindBgpInfoTAII.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdpAutoBindBgpInfoTAII.setStatus("current")
_TmnxSdpNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSdpNotifyObjs = _TmnxSdpNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100)
)
_SdpNotifySdpId_Type = SdpId
_SdpNotifySdpId_Object = MibScalar
sdpNotifySdpId = _SdpNotifySdpId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 1),
    _SdpNotifySdpId_Type()
)
sdpNotifySdpId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    sdpNotifySdpId.setStatus("current")
_DynamicSdpStatus_Type = ConfigStatus
_DynamicSdpStatus_Object = MibScalar
dynamicSdpStatus = _DynamicSdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 2),
    _DynamicSdpStatus_Type()
)
dynamicSdpStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpStatus.setStatus("current")
_DynamicSdpOrigin_Type = L2RouteOrigin
_DynamicSdpOrigin_Object = MibScalar
dynamicSdpOrigin = _DynamicSdpOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 3),
    _DynamicSdpOrigin_Type()
)
dynamicSdpOrigin.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpOrigin.setStatus("current")
_DynamicSdpCreationError_Type = DisplayString
_DynamicSdpCreationError_Object = MibScalar
dynamicSdpCreationError = _DynamicSdpCreationError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 4),
    _DynamicSdpCreationError_Type()
)
dynamicSdpCreationError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpCreationError.setStatus("current")
_DynamicSdpBindCreationError_Type = DisplayString
_DynamicSdpBindCreationError_Object = MibScalar
dynamicSdpBindCreationError = _DynamicSdpBindCreationError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 4, 4, 100, 5),
    _DynamicSdpBindCreationError_Type()
)
dynamicSdpBindCreationError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dynamicSdpBindCreationError.setStatus("current")
_SdpTrapsPrefix_ObjectIdentity = ObjectIdentity
sdpTrapsPrefix = _SdpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4)
)
_SdpTraps_ObjectIdentity = ObjectIdentity
sdpTraps = _SdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0)
)

# Managed Objects groups

tmnxSdpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 100)
)
tmnxSdpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpNumEntries"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpNextFreeId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpDelivery"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpFarEndIpAddress"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpLspList"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpDescription"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpLabelSignaling"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpOperPathMtu"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveHelloTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveMaxDropCount"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveHoldDownTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloRequestMessages"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveNumHelloResponseMessages"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveNumLateHelloResponseMessages"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveHelloRequestTimeout"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpLdpEnabled"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpVlanVcEtype"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAdvertisedVllMtuOverride"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpOperFlags"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpLastStatusChange"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpMvplsMgmtService"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpMvplsMgmtSdpBndId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpCollectAcctStats"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAccountingPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpClassFwdingEnabled"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpClassFwdingDefaultLsp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpClassFwdingMcLsp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpMetric"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoSdp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpSnmpAllowed"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpPBBEtype"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBandwidthBookingFactor"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpOperBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAdminPathMtu"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpKeepAliveHelloMessageLength"))
)
if mibBuilder.loadTexts:
    tmnxSdpV6v0Group.setStatus("current")

tmnxSdpBindV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 101)
)
tmnxSdpBindV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindLastMgmtChange"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindType"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIngressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIngressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindEgressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindEgressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCustId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindVcType"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindVlanVcTag"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindSplitHorizonGrp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperFlags"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindLastStatusChange"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIesIfIndex"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindMacPinning"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIngressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindEgressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCollectAcctStats"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAccountingPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBits"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPeerVccvCvBits"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPeerVccvCcBits"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindControlWordBit"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperControlWord"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindEndPoint"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindEndPointPrecedence"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIsICB"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddressType"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindClassFwdingOperState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindForceVlanVcForwarding"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsIngressForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsIngressDroppedPackets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsEgressForwardedPackets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsEgressForwardedOctets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsCustId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsIngFwdOctets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindBaseStatsIngDropOctets"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminIngressLabel"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminEgressLabel"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperIngressLabel"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperEgressLabel"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddress"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddress"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindV6v0Group.setStatus("current")

tmnxSdpBindTlsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 102)
)
tmnxSdpBindTlsV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPriority"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPortNum"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPathCost"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpRapidStart"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpBpduEncap"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpDesignatedBridge"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpDesignatedPort"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpForwardTransitions"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpInConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpInTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpInBadBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOutConfigBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOutTcnBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOperBpduEncap"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpCustId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacAddressLimit"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsNumMacAddresses"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsNumStaticMacAddresses"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacLearning"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacAgeing"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOperEdge"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpAdminPointToPoint"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPortRole"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpAutoEdge"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOperProtocol"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpInRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOutRstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsLimitMacMove"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsDiscardUnknownSource"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMvplsPruneState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMvplsMgmtService"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMvplsMgmtSdpBndId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpException"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptTermination"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsBpduTranslation"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpRootGuard"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpInMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOutMstBpdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpRxdDesigBridge"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacMoveNextUpTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacMoveRateExcdLeft"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsLimitMacMoveLevel"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsBpduTransOper"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptProtocols"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsIgnoreStandbySig"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsBlockOnMeshFail"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsV6v0Group.setStatus("current")

tmnxSdpBindMeshV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 103)
)
tmnxSdpBindMeshV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindMeshTlsPortState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindMeshTlsNotInMstRegion"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindMeshTlsHoldDownTimer"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindMeshTlsTransitionState"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindMeshV6v0Group.setStatus("current")

tmnxSdpApipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 104)
)
tmnxSdpApipeV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeAdminConcatCellCount"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeSigConcatCellCount"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeOperConcatCellCount"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeConcatMaxDelay"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeConcatCellClp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindApipeConcatCellAal5Fr"))
)
if mibBuilder.loadTexts:
    tmnxSdpApipeV6v0Group.setStatus("current")

tmnxSdpBindDhcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 105)
)
tmnxSdpBindDhcpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpDescription"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpSnoop"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntSnoopdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrSnoopdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntForwdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrForwdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntDropdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsSrvrDropdPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxRadPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsClntProxLSPckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsGenReleasePckts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDhcpStatsGenForceRenPckts"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindDhcpV6v0Group.setStatus("current")

tmnxSdpBindIpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 106)
)
tmnxSdpBindIpipeV6v0Group.setObjects(
    ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindIpipeCeInetAddressType")
)
if mibBuilder.loadTexts:
    tmnxSdpBindIpipeV6v0Group.setStatus("current")

tmnxSdpFCV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 107)
)
tmnxSdpFCV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpFCMappingRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpFCMappingLspId"))
)
if mibBuilder.loadTexts:
    tmnxSdpFCV6v0Group.setStatus("current")

tmnxSdpBindCpipeV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 108)
)
tmnxSdpBindCpipeV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalPayloadSize"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerPayloadSize"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalBitrate"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerBitrate"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalSigPkts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerSigPkts"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalCasTrunkFraming"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerCasTrunkFraming"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalUseRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerUseRtpHeader"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalDifferential"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerDifferential"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipeLocalTimestampFreq"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCpipePeerTimestampFreq"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindCpipeV6v0Group.setStatus("current")

tmnxSdpBindTlsL2ptV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 109)
)
tmnxSdpBindTlsL2ptV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMfibMdaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsLastClearedTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsStpTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstConfigBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstConfigBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstRstBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstRstBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstTcnBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPvstTcnBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherL2ptBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherL2ptBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherInvalidBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsOtherInvalidBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsCdpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsCdpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsVtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsVtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsDtpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsDtpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPagpBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsPagpBpdusTx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsUdldBpdusRx"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsL2ptStatsUdldBpdusTx"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsL2ptV6v0Group.setStatus("current")

tmnxSdpAutoBindV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 112)
)
tmnxSdpAutoBindV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateVcType"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateAccountingPolicyId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateCollectAcctStats"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMacLearning"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMacAgeing"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateDiscardUnknownSource"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateLimitMacMove"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMacPinning"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMacAddressLimit"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateShgName"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateShgDescription"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateShgRestProtSrcMac"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateShgRestUnprotDstMac"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateEgressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateEgressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateEgressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIngressMacFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIngressIpFilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIngressIpv6FilterId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpFastLeave"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpImportPlcy"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpLastMembIntvl"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpMaxNbrGrps"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpGenQueryIntvl"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpQueryRespIntvl"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpRobustCount"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSendQueries"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPolicyName"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpMcacPrRsvMndBW"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpMcacUnconstBW"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpVersion"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgGrpSrcTblLC"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateIgmpSnpgLastChngd"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMfibAllowedMdaTblLC"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateMfibMdaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateUseProvisionedSdp"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateVlanVcTag"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTableLC"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTemplateId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoAGI"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoSAII"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAutoBindBgpInfoTAII"))
)
if mibBuilder.loadTexts:
    tmnxSdpAutoBindV6v0Group.setStatus("current")

tmnxSdpBindTlsMrpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 113)
)
tmnxSdpBindTlsMrpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpLastChngd"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpJoinTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpLeaveAllTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicTime"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpPeriodicEnabled"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxPdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpDroppedPdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxPdus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxNewEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinInEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxInEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxJoinEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpRxLeaveEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxNewEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinInEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxInEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxJoinEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxEmptyEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMrpTxLeaveEvent"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMmrpDeclared"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMmrpRegistered"))
)
if mibBuilder.loadTexts:
    tmnxSdpBindTlsMrpV6v0Group.setStatus("current")

tmnxSdpTlsBgpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 114)
)
tmnxSdpTlsBgpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindTblLC"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRowStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindLastChngd"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindSHG"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRTTblLC"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcTlsBgpADPWTempBindRTRowStat"))
)
if mibBuilder.loadTexts:
    tmnxSdpTlsBgpV6v0Group.setStatus("current")

tmnxSdpL2V6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 115)
)
tmnxSdpL2V6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpCreationOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RtePwTemplateId"))
)
if mibBuilder.loadTexts:
    tmnxSdpL2V6v0Group.setStatus("current")

tmnxSdpNotifyObjsV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 200)
)
tmnxSdpNotifyObjsV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpNotifySdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpMaxBookableBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBookedBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpCreationError"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpBindCreationError"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyObjsV6v0Group.setStatus("current")


# Notification objects

sdpCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 1)
)
sdpCreated.setObjects(
    ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId")
)
if mibBuilder.loadTexts:
    sdpCreated.setStatus(
        "obsolete"
    )

sdpDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 2)
)
sdpDeleted.setObjects(
    ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId")
)
if mibBuilder.loadTexts:
    sdpDeleted.setStatus(
        "obsolete"
    )

sdpStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 3)
)
sdpStatusChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpOperStatus"))
)
if mibBuilder.loadTexts:
    sdpStatusChanged.setStatus(
        "current"
    )

sdpBindCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 4)
)
sdpBindCreated.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpBindCreated.setStatus(
        "obsolete"
    )

sdpBindDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 5)
)
sdpBindDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    sdpBindDeleted.setStatus(
        "obsolete"
    )

sdpBindStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 6)
)
sdpBindStatusChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperFlags"))
)
if mibBuilder.loadTexts:
    sdpBindStatusChanged.setStatus(
        "current"
    )

sdpTlsMacAddrLimitAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 7)
)
sdpTlsMacAddrLimitAlarmRaised.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    sdpTlsMacAddrLimitAlarmRaised.setStatus(
        "current"
    )

sdpTlsMacAddrLimitAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 8)
)
sdpTlsMacAddrLimitAlarmCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    sdpTlsMacAddrLimitAlarmCleared.setStatus(
        "current"
    )

sdpTlsDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 9)
)
sdpTlsDHCPSuspiciousPcktRcvd.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tlsDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sdpTlsDHCPSuspiciousPcktRcvd.setStatus(
        "obsolete"
    )

sdpBindDHCPLeaseEntriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 10)
)
sdpBindDHCPLeaseEntriesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLeaseEntriesExceeded.setStatus(
        "current"
    )

sdpBindDHCPLseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 11)
)
sdpBindDHCPLseStateOverride.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateOldChAddr"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStateOverride.setStatus(
        "current"
    )

sdpBindDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 12)
)
sdpBindDHCPSuspiciousPcktRcvd.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPSuspiciousPcktRcvd.setStatus(
        "current"
    )

sdpBindDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 13)
)
sdpBindDHCPLseStatePopulateErr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStatePopulateErr.setStatus(
        "current"
    )

sdpBindPwPeerStatusBitsChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 14)
)
sdpBindPwPeerStatusBitsChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBits"))
)
if mibBuilder.loadTexts:
    sdpBindPwPeerStatusBitsChanged.setStatus(
        "current"
    )

sdpBindTlsMacMoveExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 15)
)
sdpBindTlsMacMoveExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindOperStatus"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacMoveRateExcdLeft"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacMoveNextUpTime"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsMacMoveMaxRate"))
)
if mibBuilder.loadTexts:
    sdpBindTlsMacMoveExceeded.setStatus(
        "current"
    )

sdpBindPwPeerFaultAddrChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 16)
)
sdpBindPwPeerFaultAddrChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddressType"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwFaultInetAddress"))
)
if mibBuilder.loadTexts:
    sdpBindPwPeerFaultAddrChanged.setStatus(
        "current"
    )

sdpBindDHCPProxyServerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 17)
)
sdpBindDHCPProxyServerError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpProxyError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPProxyServerError.setStatus(
        "current"
    )

sdpBindDHCPCoAError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 18)
)
sdpBindDHCPCoAError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpCoAError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPCoAError.setStatus(
        "obsolete"
    )

sdpBindDHCPSubAuthError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 19)
)
sdpBindDHCPSubAuthError.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpSubAuthError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPSubAuthError.setStatus(
        "obsolete"
    )

sdpBindSdpStateChangeProcessed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 20)
)
sdpBindSdpStateChangeProcessed.setObjects(
    ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpNotifySdpId")
)
if mibBuilder.loadTexts:
    sdpBindSdpStateChangeProcessed.setStatus(
        "current"
    )

sdpBindDHCPLseStateMobilityErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 21)
)
sdpBindDHCPLseStateMobilityErr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcVpnId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    sdpBindDHCPLseStateMobilityErr.setStatus(
        "current"
    )

sdpBandwidthOverbooked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 22)
)
sdpBandwidthOverbooked.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpMaxBookableBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBookedBandwidth"))
)
if mibBuilder.loadTexts:
    sdpBandwidthOverbooked.setStatus(
        "current"
    )

sdpBindInsufficientBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 23)
)
sdpBindInsufficientBandwidth.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpAvailableBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindAdminBandwidth"))
)
if mibBuilder.loadTexts:
    sdpBindInsufficientBandwidth.setStatus(
        "current"
    )

dynamicSdpConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 24)
)
dynamicSdpConfigChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpStatus"))
)
if mibBuilder.loadTexts:
    dynamicSdpConfigChanged.setStatus(
        "current"
    )

dynamicSdpBindConfigChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 25)
)
dynamicSdpBindConfigChanged.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpStatus"))
)
if mibBuilder.loadTexts:
    dynamicSdpBindConfigChanged.setStatus(
        "current"
    )

dynamicSdpCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 26)
)
dynamicSdpCreationFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpCreationError"))
)
if mibBuilder.loadTexts:
    dynamicSdpCreationFailed.setStatus(
        "current"
    )

dynamicSdpBindCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 4, 0, 27)
)
dynamicSdpBindCreationFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "svcL2RteSdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpOrigin"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "pwTemplateLastChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpBindCreationError"))
)
if mibBuilder.loadTexts:
    dynamicSdpBindCreationFailed.setStatus(
        "current"
    )

unacknowledgedTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 8)
)
unacknowledgedTCN.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpId"))
)
if mibBuilder.loadTexts:
    unacknowledgedTCN.setStatus(
        "current"
    )

tmnxSvcTopoChgSdpBindMajorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 14)
)
tmnxSvcTopoChgSdpBindMajorState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"))
)
if mibBuilder.loadTexts:
    tmnxSvcTopoChgSdpBindMajorState.setStatus(
        "current"
    )

tmnxSvcNewRootSdpBind = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 15)
)
tmnxSvcNewRootSdpBind.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcTlsStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    tmnxSvcNewRootSdpBind.setStatus(
        "current"
    )

tmnxSvcTopoChgSdpBindState = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 16)
)
tmnxSvcTopoChgSdpBindState.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpPortState"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOldSdpBindTlsStpPortState"))
)
if mibBuilder.loadTexts:
    tmnxSvcTopoChgSdpBindState.setStatus(
        "current"
    )

tmnxSvcSdpBindRcvdTCN = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 17)
)
tmnxSvcSdpBindRcvdTCN.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindRcvdTCN.setStatus(
        "current"
    )

tmnxSvcSdpBindRcvdHigherBriPrio = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 18)
)
tmnxSvcSdpBindRcvdHigherBriPrio.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerBridgeId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxCustomerRootBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindRcvdHigherBriPrio.setStatus(
        "current"
    )

tmnxSvcSdpBindEncapPVST = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 19)
)
tmnxSvcSdpBindEncapPVST.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindEncapPVST.setStatus(
        "current"
    )

tmnxSvcSdpBindEncapDot1d = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 20)
)
tmnxSvcSdpBindEncapDot1d.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "tmnxOtherBridgeId"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpBindEncapDot1d.setStatus(
        "current"
    )

tmnxSvcSdpActiveProtocolChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 31)
)
tmnxSvcSdpActiveProtocolChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpOperProtocol"))
)
if mibBuilder.loadTexts:
    tmnxSvcSdpActiveProtocolChange.setStatus(
        "current"
    )

tmnxStpMeshNotInMstRegion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 36)
)
tmnxStpMeshNotInMstRegion.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"))
)
if mibBuilder.loadTexts:
    tmnxStpMeshNotInMstRegion.setStatus(
        "current"
    )

tmnxSdpBndStpExcepCondStateChng = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 4, 5, 0, 38)
)
tmnxSdpBndStpExcepCondStateChng.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SERV-MIB", "custId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindId"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsStpException"))
)
if mibBuilder.loadTexts:
    tmnxSdpBndStpExcepCondStateChng.setStatus(
        "current"
    )


# Notifications groups

tmnxSdpNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 400)
)
tmnxSdpNotifyV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "unacknowledgedTCN"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcTopoChgSdpBindMajorState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcNewRootSdpBind"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcTopoChgSdpBindState"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcSdpBindRcvdTCN"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcSdpBindRcvdHigherBriPrio"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcSdpBindEncapPVST"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcSdpBindEncapDot1d"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSvcSdpActiveProtocolChange"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxStpMeshNotInMstRegion"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "tmnxSdpBndStpExcepCondStateChng"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpStatusChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindStatusChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpTlsMacAddrLimitAlarmRaised"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpTlsMacAddrLimitAlarmCleared"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPLeaseEntriesExceeded"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPLseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPLseStatePopulateErr"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwPeerStatusBitsChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindTlsMacMoveExceeded"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindPwPeerFaultAddrChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPProxyServerError"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindSdpStateChangeProcessed"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPLseStateMobilityErr"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBandwidthOverbooked"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindInsufficientBandwidth"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpConfigChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpBindConfigChanged"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpCreationFailed"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "dynamicSdpBindCreationFailed"))
)
if mibBuilder.loadTexts:
    tmnxSdpNotifyV6v0Group.setStatus(
        "current"
    )

tmnxSdpObsoletedNotifyV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 2, 401)
)
tmnxSdpObsoletedNotifyV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpCreated"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpDeleted"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindCreated"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDeleted"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpTlsDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPCoAError"),
        ("ALCATEL-IND1-TIMETRA-SDP-MIB", "sdpBindDHCPSubAuthError"))
)
if mibBuilder.loadTexts:
    tmnxSdpObsoletedNotifyV6v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSdp77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxSdp77x0V6v0Compliance.setStatus(
        "current"
    )

tmnxSdp7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 4, 4, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxSdp7450V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-SDP-MIB",
    **{"timetraServicesSdpMIBModule": timetraServicesSdpMIBModule,
       "tmnxSdpConformance": tmnxSdpConformance,
       "tmnxSdpCompliances": tmnxSdpCompliances,
       "tmnxSdp77x0V6v0Compliance": tmnxSdp77x0V6v0Compliance,
       "tmnxSdp7450V6v0Compliance": tmnxSdp7450V6v0Compliance,
       "tmnxSdpGroups": tmnxSdpGroups,
       "tmnxSdpV6v0Group": tmnxSdpV6v0Group,
       "tmnxSdpBindV6v0Group": tmnxSdpBindV6v0Group,
       "tmnxSdpBindTlsV6v0Group": tmnxSdpBindTlsV6v0Group,
       "tmnxSdpBindMeshV6v0Group": tmnxSdpBindMeshV6v0Group,
       "tmnxSdpApipeV6v0Group": tmnxSdpApipeV6v0Group,
       "tmnxSdpBindDhcpV6v0Group": tmnxSdpBindDhcpV6v0Group,
       "tmnxSdpBindIpipeV6v0Group": tmnxSdpBindIpipeV6v0Group,
       "tmnxSdpFCV6v0Group": tmnxSdpFCV6v0Group,
       "tmnxSdpBindCpipeV6v0Group": tmnxSdpBindCpipeV6v0Group,
       "tmnxSdpBindTlsL2ptV6v0Group": tmnxSdpBindTlsL2ptV6v0Group,
       "tmnxSdpAutoBindV6v0Group": tmnxSdpAutoBindV6v0Group,
       "tmnxSdpBindTlsMrpV6v0Group": tmnxSdpBindTlsMrpV6v0Group,
       "tmnxSdpTlsBgpV6v0Group": tmnxSdpTlsBgpV6v0Group,
       "tmnxSdpL2V6v0Group": tmnxSdpL2V6v0Group,
       "tmnxSdpNotifyObjsV6v0Group": tmnxSdpNotifyObjsV6v0Group,
       "tmnxSdpNotifyV6v0Group": tmnxSdpNotifyV6v0Group,
       "tmnxSdpObsoletedNotifyV6v0Group": tmnxSdpObsoletedNotifyV6v0Group,
       "svcTlsBgpADPWTempBindTblLC": svcTlsBgpADPWTempBindTblLC,
       "svcTlsBgpADPWTempBindTable": svcTlsBgpADPWTempBindTable,
       "svcTlsBgpADPWTempBindEntry": svcTlsBgpADPWTempBindEntry,
       "svcTlsBgpADPWTempBindRowStatus": svcTlsBgpADPWTempBindRowStatus,
       "svcTlsBgpADPWTempBindLastChngd": svcTlsBgpADPWTempBindLastChngd,
       "svcTlsBgpADPWTempBindSHG": svcTlsBgpADPWTempBindSHG,
       "svcTlsBgpADPWTempBindRTTblLC": svcTlsBgpADPWTempBindRTTblLC,
       "svcTlsBgpADPWTempBindRTTable": svcTlsBgpADPWTempBindRTTable,
       "svcTlsBgpADPWTempBindRTEntry": svcTlsBgpADPWTempBindRTEntry,
       "svcTlsBgpADPWTempBindRT": svcTlsBgpADPWTempBindRT,
       "svcTlsBgpADPWTempBindRTRowStat": svcTlsBgpADPWTempBindRTRowStat,
       "svcL2RteTableLastChanged": svcL2RteTableLastChanged,
       "svcL2RteTable": svcL2RteTable,
       "svcL2RteEntry": svcL2RteEntry,
       "svcL2RteVsiPrefix": svcL2RteVsiPrefix,
       "svcL2RteRouteDistinguisher": svcL2RteRouteDistinguisher,
       "svcL2RteNextHopType": svcL2RteNextHopType,
       "svcL2RteNextHop": svcL2RteNextHop,
       "svcL2RteSdpBindId": svcL2RteSdpBindId,
       "svcL2RtePwTemplateId": svcL2RtePwTemplateId,
       "tmnxSdpObjs": tmnxSdpObjs,
       "sdpNumEntries": sdpNumEntries,
       "sdpNextFreeId": sdpNextFreeId,
       "sdpInfoTable": sdpInfoTable,
       "sdpInfoEntry": sdpInfoEntry,
       "sdpId": sdpId,
       "sdpRowStatus": sdpRowStatus,
       "sdpDelivery": sdpDelivery,
       "sdpFarEndIpAddress": sdpFarEndIpAddress,
       "sdpLspList": sdpLspList,
       "sdpDescription": sdpDescription,
       "sdpLabelSignaling": sdpLabelSignaling,
       "sdpAdminStatus": sdpAdminStatus,
       "sdpOperStatus": sdpOperStatus,
       "sdpAdminPathMtu": sdpAdminPathMtu,
       "sdpOperPathMtu": sdpOperPathMtu,
       "sdpKeepAliveAdminStatus": sdpKeepAliveAdminStatus,
       "sdpKeepAliveOperStatus": sdpKeepAliveOperStatus,
       "sdpKeepAliveHelloTime": sdpKeepAliveHelloTime,
       "sdpKeepAliveMaxDropCount": sdpKeepAliveMaxDropCount,
       "sdpKeepAliveHoldDownTime": sdpKeepAliveHoldDownTime,
       "sdpLastMgmtChange": sdpLastMgmtChange,
       "sdpKeepAliveHelloMessageLength": sdpKeepAliveHelloMessageLength,
       "sdpKeepAliveNumHelloRequestMessages": sdpKeepAliveNumHelloRequestMessages,
       "sdpKeepAliveNumHelloResponseMessages": sdpKeepAliveNumHelloResponseMessages,
       "sdpKeepAliveNumLateHelloResponseMessages": sdpKeepAliveNumLateHelloResponseMessages,
       "sdpKeepAliveHelloRequestTimeout": sdpKeepAliveHelloRequestTimeout,
       "sdpLdpEnabled": sdpLdpEnabled,
       "sdpVlanVcEtype": sdpVlanVcEtype,
       "sdpAdvertisedVllMtuOverride": sdpAdvertisedVllMtuOverride,
       "sdpOperFlags": sdpOperFlags,
       "sdpLastStatusChange": sdpLastStatusChange,
       "sdpMvplsMgmtService": sdpMvplsMgmtService,
       "sdpMvplsMgmtSdpBndId": sdpMvplsMgmtSdpBndId,
       "sdpCollectAcctStats": sdpCollectAcctStats,
       "sdpAccountingPolicyId": sdpAccountingPolicyId,
       "sdpClassFwdingEnabled": sdpClassFwdingEnabled,
       "sdpClassFwdingDefaultLsp": sdpClassFwdingDefaultLsp,
       "sdpClassFwdingMcLsp": sdpClassFwdingMcLsp,
       "sdpMetric": sdpMetric,
       "sdpAutoSdp": sdpAutoSdp,
       "sdpSnmpAllowed": sdpSnmpAllowed,
       "sdpPBBEtype": sdpPBBEtype,
       "sdpBandwidthBookingFactor": sdpBandwidthBookingFactor,
       "sdpOperBandwidth": sdpOperBandwidth,
       "sdpAvailableBandwidth": sdpAvailableBandwidth,
       "sdpMaxBookableBandwidth": sdpMaxBookableBandwidth,
       "sdpBookedBandwidth": sdpBookedBandwidth,
       "sdpCreationOrigin": sdpCreationOrigin,
       "sdpBindTable": sdpBindTable,
       "sdpBindEntry": sdpBindEntry,
       "sdpBindId": sdpBindId,
       "sdpBindRowStatus": sdpBindRowStatus,
       "sdpBindAdminIngressLabel": sdpBindAdminIngressLabel,
       "sdpBindAdminEgressLabel": sdpBindAdminEgressLabel,
       "sdpBindOperIngressLabel": sdpBindOperIngressLabel,
       "sdpBindOperEgressLabel": sdpBindOperEgressLabel,
       "sdpBindAdminStatus": sdpBindAdminStatus,
       "sdpBindOperStatus": sdpBindOperStatus,
       "sdpBindLastMgmtChange": sdpBindLastMgmtChange,
       "sdpBindType": sdpBindType,
       "sdpBindIngressMacFilterId": sdpBindIngressMacFilterId,
       "sdpBindIngressIpFilterId": sdpBindIngressIpFilterId,
       "sdpBindEgressMacFilterId": sdpBindEgressMacFilterId,
       "sdpBindEgressIpFilterId": sdpBindEgressIpFilterId,
       "sdpBindVpnId": sdpBindVpnId,
       "sdpBindCustId": sdpBindCustId,
       "sdpBindVcType": sdpBindVcType,
       "sdpBindVlanVcTag": sdpBindVlanVcTag,
       "sdpBindSplitHorizonGrp": sdpBindSplitHorizonGrp,
       "sdpBindOperFlags": sdpBindOperFlags,
       "sdpBindLastStatusChange": sdpBindLastStatusChange,
       "sdpBindIesIfIndex": sdpBindIesIfIndex,
       "sdpBindMacPinning": sdpBindMacPinning,
       "sdpBindIngressIpv6FilterId": sdpBindIngressIpv6FilterId,
       "sdpBindEgressIpv6FilterId": sdpBindEgressIpv6FilterId,
       "sdpBindCollectAcctStats": sdpBindCollectAcctStats,
       "sdpBindAccountingPolicyId": sdpBindAccountingPolicyId,
       "sdpBindPwPeerStatusBits": sdpBindPwPeerStatusBits,
       "sdpBindPeerVccvCvBits": sdpBindPeerVccvCvBits,
       "sdpBindPeerVccvCcBits": sdpBindPeerVccvCcBits,
       "sdpBindControlWordBit": sdpBindControlWordBit,
       "sdpBindOperControlWord": sdpBindOperControlWord,
       "sdpBindEndPoint": sdpBindEndPoint,
       "sdpBindEndPointPrecedence": sdpBindEndPointPrecedence,
       "sdpBindIsICB": sdpBindIsICB,
       "sdpBindPwFaultInetAddressType": sdpBindPwFaultInetAddressType,
       "sdpBindPwFaultInetAddress": sdpBindPwFaultInetAddress,
       "sdpBindClassFwdingOperState": sdpBindClassFwdingOperState,
       "sdpBindForceVlanVcForwarding": sdpBindForceVlanVcForwarding,
       "sdpBindAdminBandwidth": sdpBindAdminBandwidth,
       "sdpBindOperBandwidth": sdpBindOperBandwidth,
       "sdpBindBaseStatsTable": sdpBindBaseStatsTable,
       "sdpBindBaseStatsEntry": sdpBindBaseStatsEntry,
       "sdpBindBaseStatsIngressForwardedPackets": sdpBindBaseStatsIngressForwardedPackets,
       "sdpBindBaseStatsIngressDroppedPackets": sdpBindBaseStatsIngressDroppedPackets,
       "sdpBindBaseStatsEgressForwardedPackets": sdpBindBaseStatsEgressForwardedPackets,
       "sdpBindBaseStatsEgressForwardedOctets": sdpBindBaseStatsEgressForwardedOctets,
       "sdpBindBaseStatsCustId": sdpBindBaseStatsCustId,
       "sdpBindBaseStatsIngFwdOctets": sdpBindBaseStatsIngFwdOctets,
       "sdpBindBaseStatsIngDropOctets": sdpBindBaseStatsIngDropOctets,
       "sdpBindTlsTable": sdpBindTlsTable,
       "sdpBindTlsEntry": sdpBindTlsEntry,
       "sdpBindTlsStpAdminStatus": sdpBindTlsStpAdminStatus,
       "sdpBindTlsStpPriority": sdpBindTlsStpPriority,
       "sdpBindTlsStpPortNum": sdpBindTlsStpPortNum,
       "sdpBindTlsStpPathCost": sdpBindTlsStpPathCost,
       "sdpBindTlsStpRapidStart": sdpBindTlsStpRapidStart,
       "sdpBindTlsStpBpduEncap": sdpBindTlsStpBpduEncap,
       "sdpBindTlsStpPortState": sdpBindTlsStpPortState,
       "sdpBindTlsStpDesignatedBridge": sdpBindTlsStpDesignatedBridge,
       "sdpBindTlsStpDesignatedPort": sdpBindTlsStpDesignatedPort,
       "sdpBindTlsStpForwardTransitions": sdpBindTlsStpForwardTransitions,
       "sdpBindTlsStpInConfigBpdus": sdpBindTlsStpInConfigBpdus,
       "sdpBindTlsStpInTcnBpdus": sdpBindTlsStpInTcnBpdus,
       "sdpBindTlsStpInBadBpdus": sdpBindTlsStpInBadBpdus,
       "sdpBindTlsStpOutConfigBpdus": sdpBindTlsStpOutConfigBpdus,
       "sdpBindTlsStpOutTcnBpdus": sdpBindTlsStpOutTcnBpdus,
       "sdpBindTlsStpOperBpduEncap": sdpBindTlsStpOperBpduEncap,
       "sdpBindTlsStpVpnId": sdpBindTlsStpVpnId,
       "sdpBindTlsStpCustId": sdpBindTlsStpCustId,
       "sdpBindTlsMacAddressLimit": sdpBindTlsMacAddressLimit,
       "sdpBindTlsNumMacAddresses": sdpBindTlsNumMacAddresses,
       "sdpBindTlsNumStaticMacAddresses": sdpBindTlsNumStaticMacAddresses,
       "sdpBindTlsMacLearning": sdpBindTlsMacLearning,
       "sdpBindTlsMacAgeing": sdpBindTlsMacAgeing,
       "sdpBindTlsStpOperEdge": sdpBindTlsStpOperEdge,
       "sdpBindTlsStpAdminPointToPoint": sdpBindTlsStpAdminPointToPoint,
       "sdpBindTlsStpPortRole": sdpBindTlsStpPortRole,
       "sdpBindTlsStpAutoEdge": sdpBindTlsStpAutoEdge,
       "sdpBindTlsStpOperProtocol": sdpBindTlsStpOperProtocol,
       "sdpBindTlsStpInRstBpdus": sdpBindTlsStpInRstBpdus,
       "sdpBindTlsStpOutRstBpdus": sdpBindTlsStpOutRstBpdus,
       "sdpBindTlsLimitMacMove": sdpBindTlsLimitMacMove,
       "sdpBindTlsDiscardUnknownSource": sdpBindTlsDiscardUnknownSource,
       "sdpBindTlsMvplsPruneState": sdpBindTlsMvplsPruneState,
       "sdpBindTlsMvplsMgmtService": sdpBindTlsMvplsMgmtService,
       "sdpBindTlsMvplsMgmtSdpBndId": sdpBindTlsMvplsMgmtSdpBndId,
       "sdpBindTlsStpException": sdpBindTlsStpException,
       "sdpBindTlsL2ptTermination": sdpBindTlsL2ptTermination,
       "sdpBindTlsBpduTranslation": sdpBindTlsBpduTranslation,
       "sdpBindTlsStpRootGuard": sdpBindTlsStpRootGuard,
       "sdpBindTlsStpInMstBpdus": sdpBindTlsStpInMstBpdus,
       "sdpBindTlsStpOutMstBpdus": sdpBindTlsStpOutMstBpdus,
       "sdpBindTlsStpRxdDesigBridge": sdpBindTlsStpRxdDesigBridge,
       "sdpBindTlsMacMoveNextUpTime": sdpBindTlsMacMoveNextUpTime,
       "sdpBindTlsMacMoveRateExcdLeft": sdpBindTlsMacMoveRateExcdLeft,
       "sdpBindTlsLimitMacMoveLevel": sdpBindTlsLimitMacMoveLevel,
       "sdpBindTlsBpduTransOper": sdpBindTlsBpduTransOper,
       "sdpBindTlsL2ptProtocols": sdpBindTlsL2ptProtocols,
       "sdpBindTlsIgnoreStandbySig": sdpBindTlsIgnoreStandbySig,
       "sdpBindTlsBlockOnMeshFail": sdpBindTlsBlockOnMeshFail,
       "sdpBindMeshTlsTable": sdpBindMeshTlsTable,
       "sdpBindMeshTlsEntry": sdpBindMeshTlsEntry,
       "sdpBindMeshTlsPortState": sdpBindMeshTlsPortState,
       "sdpBindMeshTlsHoldDownTimer": sdpBindMeshTlsHoldDownTimer,
       "sdpBindMeshTlsTransitionState": sdpBindMeshTlsTransitionState,
       "sdpBindMeshTlsNotInMstRegion": sdpBindMeshTlsNotInMstRegion,
       "sdpBindApipeTable": sdpBindApipeTable,
       "sdpBindApipeEntry": sdpBindApipeEntry,
       "sdpBindApipeAdminConcatCellCount": sdpBindApipeAdminConcatCellCount,
       "sdpBindApipeSigConcatCellCount": sdpBindApipeSigConcatCellCount,
       "sdpBindApipeOperConcatCellCount": sdpBindApipeOperConcatCellCount,
       "sdpBindApipeConcatMaxDelay": sdpBindApipeConcatMaxDelay,
       "sdpBindApipeConcatCellClp": sdpBindApipeConcatCellClp,
       "sdpBindApipeConcatCellAal5Fr": sdpBindApipeConcatCellAal5Fr,
       "sdpBindDhcpInfoTable": sdpBindDhcpInfoTable,
       "sdpBindDhcpInfoEntry": sdpBindDhcpInfoEntry,
       "sdpBindDhcpDescription": sdpBindDhcpDescription,
       "sdpBindDhcpSnoop": sdpBindDhcpSnoop,
       "sdpBindDhcpStatsTable": sdpBindDhcpStatsTable,
       "sdpBindDhcpStatsEntry": sdpBindDhcpStatsEntry,
       "sdpBindDhcpStatsClntSnoopdPckts": sdpBindDhcpStatsClntSnoopdPckts,
       "sdpBindDhcpStatsSrvrSnoopdPckts": sdpBindDhcpStatsSrvrSnoopdPckts,
       "sdpBindDhcpStatsClntForwdPckts": sdpBindDhcpStatsClntForwdPckts,
       "sdpBindDhcpStatsSrvrForwdPckts": sdpBindDhcpStatsSrvrForwdPckts,
       "sdpBindDhcpStatsClntDropdPckts": sdpBindDhcpStatsClntDropdPckts,
       "sdpBindDhcpStatsSrvrDropdPckts": sdpBindDhcpStatsSrvrDropdPckts,
       "sdpBindDhcpStatsClntProxRadPckts": sdpBindDhcpStatsClntProxRadPckts,
       "sdpBindDhcpStatsClntProxLSPckts": sdpBindDhcpStatsClntProxLSPckts,
       "sdpBindDhcpStatsGenReleasePckts": sdpBindDhcpStatsGenReleasePckts,
       "sdpBindDhcpStatsGenForceRenPckts": sdpBindDhcpStatsGenForceRenPckts,
       "sdpBindIpipeTable": sdpBindIpipeTable,
       "sdpBindIpipeEntry": sdpBindIpipeEntry,
       "sdpBindIpipeCeInetAddressType": sdpBindIpipeCeInetAddressType,
       "sdpBindIpipeCeInetAddress": sdpBindIpipeCeInetAddress,
       "sdpFCMappingTable": sdpFCMappingTable,
       "sdpFCMappingEntry": sdpFCMappingEntry,
       "sdpFCMappingFCName": sdpFCMappingFCName,
       "sdpFCMappingRowStatus": sdpFCMappingRowStatus,
       "sdpFCMappingLspId": sdpFCMappingLspId,
       "sdpBindTlsMfibAllowedMdaTable": sdpBindTlsMfibAllowedMdaTable,
       "sdpBindTlsMfibAllowedMdaEntry": sdpBindTlsMfibAllowedMdaEntry,
       "sdpBindTlsMfibMdaRowStatus": sdpBindTlsMfibMdaRowStatus,
       "sdpBindCpipeTable": sdpBindCpipeTable,
       "sdpBindCpipeEntry": sdpBindCpipeEntry,
       "sdpBindCpipeLocalPayloadSize": sdpBindCpipeLocalPayloadSize,
       "sdpBindCpipePeerPayloadSize": sdpBindCpipePeerPayloadSize,
       "sdpBindCpipeLocalBitrate": sdpBindCpipeLocalBitrate,
       "sdpBindCpipePeerBitrate": sdpBindCpipePeerBitrate,
       "sdpBindCpipeLocalSigPkts": sdpBindCpipeLocalSigPkts,
       "sdpBindCpipePeerSigPkts": sdpBindCpipePeerSigPkts,
       "sdpBindCpipeLocalCasTrunkFraming": sdpBindCpipeLocalCasTrunkFraming,
       "sdpBindCpipePeerCasTrunkFraming": sdpBindCpipePeerCasTrunkFraming,
       "sdpBindCpipeLocalUseRtpHeader": sdpBindCpipeLocalUseRtpHeader,
       "sdpBindCpipePeerUseRtpHeader": sdpBindCpipePeerUseRtpHeader,
       "sdpBindCpipeLocalDifferential": sdpBindCpipeLocalDifferential,
       "sdpBindCpipePeerDifferential": sdpBindCpipePeerDifferential,
       "sdpBindCpipeLocalTimestampFreq": sdpBindCpipeLocalTimestampFreq,
       "sdpBindCpipePeerTimestampFreq": sdpBindCpipePeerTimestampFreq,
       "sdpBindTlsL2ptStatsTable": sdpBindTlsL2ptStatsTable,
       "sdpBindTlsL2ptStatsEntry": sdpBindTlsL2ptStatsEntry,
       "sdpBindTlsL2ptStatsLastClearedTime": sdpBindTlsL2ptStatsLastClearedTime,
       "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpConfigBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpRstBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx": sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx": sdpBindTlsL2ptStatsL2ptEncapStpTcnBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstConfigBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstRstBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPvstTcnBpdusTx,
       "sdpBindTlsL2ptStatsStpConfigBpdusRx": sdpBindTlsL2ptStatsStpConfigBpdusRx,
       "sdpBindTlsL2ptStatsStpConfigBpdusTx": sdpBindTlsL2ptStatsStpConfigBpdusTx,
       "sdpBindTlsL2ptStatsStpRstBpdusRx": sdpBindTlsL2ptStatsStpRstBpdusRx,
       "sdpBindTlsL2ptStatsStpRstBpdusTx": sdpBindTlsL2ptStatsStpRstBpdusTx,
       "sdpBindTlsL2ptStatsStpTcnBpdusRx": sdpBindTlsL2ptStatsStpTcnBpdusRx,
       "sdpBindTlsL2ptStatsStpTcnBpdusTx": sdpBindTlsL2ptStatsStpTcnBpdusTx,
       "sdpBindTlsL2ptStatsPvstConfigBpdusRx": sdpBindTlsL2ptStatsPvstConfigBpdusRx,
       "sdpBindTlsL2ptStatsPvstConfigBpdusTx": sdpBindTlsL2ptStatsPvstConfigBpdusTx,
       "sdpBindTlsL2ptStatsPvstRstBpdusRx": sdpBindTlsL2ptStatsPvstRstBpdusRx,
       "sdpBindTlsL2ptStatsPvstRstBpdusTx": sdpBindTlsL2ptStatsPvstRstBpdusTx,
       "sdpBindTlsL2ptStatsPvstTcnBpdusRx": sdpBindTlsL2ptStatsPvstTcnBpdusRx,
       "sdpBindTlsL2ptStatsPvstTcnBpdusTx": sdpBindTlsL2ptStatsPvstTcnBpdusTx,
       "sdpBindTlsL2ptStatsOtherBpdusRx": sdpBindTlsL2ptStatsOtherBpdusRx,
       "sdpBindTlsL2ptStatsOtherBpdusTx": sdpBindTlsL2ptStatsOtherBpdusTx,
       "sdpBindTlsL2ptStatsOtherL2ptBpdusRx": sdpBindTlsL2ptStatsOtherL2ptBpdusRx,
       "sdpBindTlsL2ptStatsOtherL2ptBpdusTx": sdpBindTlsL2ptStatsOtherL2ptBpdusTx,
       "sdpBindTlsL2ptStatsOtherInvalidBpdusRx": sdpBindTlsL2ptStatsOtherInvalidBpdusRx,
       "sdpBindTlsL2ptStatsOtherInvalidBpdusTx": sdpBindTlsL2ptStatsOtherInvalidBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapCdpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapCdpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapVtpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapVtpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapDtpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapDtpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx": sdpBindTlsL2ptStatsL2ptEncapPagpBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx": sdpBindTlsL2ptStatsL2ptEncapPagpBpdusTx,
       "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx": sdpBindTlsL2ptStatsL2ptEncapUdldBpdusRx,
       "sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx": sdpBindTlsL2ptStatsL2ptEncapUdldBpdusTx,
       "sdpBindTlsL2ptStatsCdpBpdusRx": sdpBindTlsL2ptStatsCdpBpdusRx,
       "sdpBindTlsL2ptStatsCdpBpdusTx": sdpBindTlsL2ptStatsCdpBpdusTx,
       "sdpBindTlsL2ptStatsVtpBpdusRx": sdpBindTlsL2ptStatsVtpBpdusRx,
       "sdpBindTlsL2ptStatsVtpBpdusTx": sdpBindTlsL2ptStatsVtpBpdusTx,
       "sdpBindTlsL2ptStatsDtpBpdusRx": sdpBindTlsL2ptStatsDtpBpdusRx,
       "sdpBindTlsL2ptStatsDtpBpdusTx": sdpBindTlsL2ptStatsDtpBpdusTx,
       "sdpBindTlsL2ptStatsPagpBpdusRx": sdpBindTlsL2ptStatsPagpBpdusRx,
       "sdpBindTlsL2ptStatsPagpBpdusTx": sdpBindTlsL2ptStatsPagpBpdusTx,
       "sdpBindTlsL2ptStatsUdldBpdusRx": sdpBindTlsL2ptStatsUdldBpdusRx,
       "sdpBindTlsL2ptStatsUdldBpdusTx": sdpBindTlsL2ptStatsUdldBpdusTx,
       "pwTemplateTableLastChanged": pwTemplateTableLastChanged,
       "pwTemplateTable": pwTemplateTable,
       "pwTemplateEntry": pwTemplateEntry,
       "pwTemplateId": pwTemplateId,
       "pwTemplateRowStatus": pwTemplateRowStatus,
       "pwTemplateLastChanged": pwTemplateLastChanged,
       "pwTemplateUseProvisionedSdp": pwTemplateUseProvisionedSdp,
       "pwTemplateVcType": pwTemplateVcType,
       "pwTemplateAccountingPolicyId": pwTemplateAccountingPolicyId,
       "pwTemplateCollectAcctStats": pwTemplateCollectAcctStats,
       "pwTemplateMacLearning": pwTemplateMacLearning,
       "pwTemplateMacAgeing": pwTemplateMacAgeing,
       "pwTemplateDiscardUnknownSource": pwTemplateDiscardUnknownSource,
       "pwTemplateLimitMacMove": pwTemplateLimitMacMove,
       "pwTemplateMacPinning": pwTemplateMacPinning,
       "pwTemplateVlanVcTag": pwTemplateVlanVcTag,
       "pwTemplateMacAddressLimit": pwTemplateMacAddressLimit,
       "pwTemplateShgName": pwTemplateShgName,
       "pwTemplateShgDescription": pwTemplateShgDescription,
       "pwTemplateShgRestProtSrcMac": pwTemplateShgRestProtSrcMac,
       "pwTemplateShgRestUnprotDstMac": pwTemplateShgRestUnprotDstMac,
       "pwTemplateEgressMacFilterId": pwTemplateEgressMacFilterId,
       "pwTemplateEgressIpFilterId": pwTemplateEgressIpFilterId,
       "pwTemplateEgressIpv6FilterId": pwTemplateEgressIpv6FilterId,
       "pwTemplateIngressMacFilterId": pwTemplateIngressMacFilterId,
       "pwTemplateIngressIpFilterId": pwTemplateIngressIpFilterId,
       "pwTemplateIngressIpv6FilterId": pwTemplateIngressIpv6FilterId,
       "pwTemplateIgmpFastLeave": pwTemplateIgmpFastLeave,
       "pwTemplateIgmpImportPlcy": pwTemplateIgmpImportPlcy,
       "pwTemplateIgmpLastMembIntvl": pwTemplateIgmpLastMembIntvl,
       "pwTemplateIgmpMaxNbrGrps": pwTemplateIgmpMaxNbrGrps,
       "pwTemplateIgmpGenQueryIntvl": pwTemplateIgmpGenQueryIntvl,
       "pwTemplateIgmpQueryRespIntvl": pwTemplateIgmpQueryRespIntvl,
       "pwTemplateIgmpRobustCount": pwTemplateIgmpRobustCount,
       "pwTemplateIgmpSendQueries": pwTemplateIgmpSendQueries,
       "pwTemplateIgmpMcacPolicyName": pwTemplateIgmpMcacPolicyName,
       "pwTemplateIgmpMcacUnconstBW": pwTemplateIgmpMcacUnconstBW,
       "pwTemplateIgmpMcacPrRsvMndBW": pwTemplateIgmpMcacPrRsvMndBW,
       "pwTemplateIgmpVersion": pwTemplateIgmpVersion,
       "pwTemplateIgmpSnpgGrpSrcTblLC": pwTemplateIgmpSnpgGrpSrcTblLC,
       "pwTemplateIgmpSnpgGrpSrcTable": pwTemplateIgmpSnpgGrpSrcTable,
       "pwTemplateIgmpSnpgGrpSrcEntry": pwTemplateIgmpSnpgGrpSrcEntry,
       "pwTemplateIgmpSnpgGrpAddrType": pwTemplateIgmpSnpgGrpAddrType,
       "pwTemplateIgmpSnpgGrpAddr": pwTemplateIgmpSnpgGrpAddr,
       "pwTemplateIgmpSnpgSrcAddrType": pwTemplateIgmpSnpgSrcAddrType,
       "pwTemplateIgmpSnpgSrcAddr": pwTemplateIgmpSnpgSrcAddr,
       "pwTemplateIgmpSnpgRowStatus": pwTemplateIgmpSnpgRowStatus,
       "pwTemplateIgmpSnpgLastChngd": pwTemplateIgmpSnpgLastChngd,
       "pwTemplateMfibAllowedMdaTblLC": pwTemplateMfibAllowedMdaTblLC,
       "pwTemplateMfibAllowedMdaTable": pwTemplateMfibAllowedMdaTable,
       "pwTemplateMfibAllowedMdaEntry": pwTemplateMfibAllowedMdaEntry,
       "pwTemplateMfibMdaRowStatus": pwTemplateMfibMdaRowStatus,
       "sdpBindTlsMrpTableLastChanged": sdpBindTlsMrpTableLastChanged,
       "sdpBindTlsMrpTable": sdpBindTlsMrpTable,
       "sdpBindTlsMrpEntry": sdpBindTlsMrpEntry,
       "sdpBindTlsMrpLastChngd": sdpBindTlsMrpLastChngd,
       "sdpBindTlsMrpJoinTime": sdpBindTlsMrpJoinTime,
       "sdpBindTlsMrpLeaveTime": sdpBindTlsMrpLeaveTime,
       "sdpBindTlsMrpLeaveAllTime": sdpBindTlsMrpLeaveAllTime,
       "sdpBindTlsMrpPeriodicTime": sdpBindTlsMrpPeriodicTime,
       "sdpBindTlsMrpPeriodicEnabled": sdpBindTlsMrpPeriodicEnabled,
       "sdpBindTlsMrpRxPdus": sdpBindTlsMrpRxPdus,
       "sdpBindTlsMrpDroppedPdus": sdpBindTlsMrpDroppedPdus,
       "sdpBindTlsMrpTxPdus": sdpBindTlsMrpTxPdus,
       "sdpBindTlsMrpRxNewEvent": sdpBindTlsMrpRxNewEvent,
       "sdpBindTlsMrpRxJoinInEvent": sdpBindTlsMrpRxJoinInEvent,
       "sdpBindTlsMrpRxInEvent": sdpBindTlsMrpRxInEvent,
       "sdpBindTlsMrpRxJoinEmptyEvent": sdpBindTlsMrpRxJoinEmptyEvent,
       "sdpBindTlsMrpRxEmptyEvent": sdpBindTlsMrpRxEmptyEvent,
       "sdpBindTlsMrpRxLeaveEvent": sdpBindTlsMrpRxLeaveEvent,
       "sdpBindTlsMrpTxNewEvent": sdpBindTlsMrpTxNewEvent,
       "sdpBindTlsMrpTxJoinInEvent": sdpBindTlsMrpTxJoinInEvent,
       "sdpBindTlsMrpTxInEvent": sdpBindTlsMrpTxInEvent,
       "sdpBindTlsMrpTxJoinEmptyEvent": sdpBindTlsMrpTxJoinEmptyEvent,
       "sdpBindTlsMrpTxEmptyEvent": sdpBindTlsMrpTxEmptyEvent,
       "sdpBindTlsMrpTxLeaveEvent": sdpBindTlsMrpTxLeaveEvent,
       "sdpBindTlsMmrpTable": sdpBindTlsMmrpTable,
       "sdpBindTlsMmrpEntry": sdpBindTlsMmrpEntry,
       "sdpBindTlsMmrpMacAddr": sdpBindTlsMmrpMacAddr,
       "sdpBindTlsMmrpDeclared": sdpBindTlsMmrpDeclared,
       "sdpBindTlsMmrpRegistered": sdpBindTlsMmrpRegistered,
       "sdpAutoBindBgpInfoTableLC": sdpAutoBindBgpInfoTableLC,
       "sdpAutoBindBgpInfoTable": sdpAutoBindBgpInfoTable,
       "sdpAutoBindBgpInfoEntry": sdpAutoBindBgpInfoEntry,
       "sdpAutoBindBgpInfoTemplateId": sdpAutoBindBgpInfoTemplateId,
       "sdpAutoBindBgpInfoAGI": sdpAutoBindBgpInfoAGI,
       "sdpAutoBindBgpInfoSAII": sdpAutoBindBgpInfoSAII,
       "sdpAutoBindBgpInfoTAII": sdpAutoBindBgpInfoTAII,
       "tmnxSdpNotifyObjs": tmnxSdpNotifyObjs,
       "sdpNotifySdpId": sdpNotifySdpId,
       "dynamicSdpStatus": dynamicSdpStatus,
       "dynamicSdpOrigin": dynamicSdpOrigin,
       "dynamicSdpCreationError": dynamicSdpCreationError,
       "dynamicSdpBindCreationError": dynamicSdpBindCreationError,
       "sdpTrapsPrefix": sdpTrapsPrefix,
       "sdpTraps": sdpTraps,
       "sdpCreated": sdpCreated,
       "sdpDeleted": sdpDeleted,
       "sdpStatusChanged": sdpStatusChanged,
       "sdpBindCreated": sdpBindCreated,
       "sdpBindDeleted": sdpBindDeleted,
       "sdpBindStatusChanged": sdpBindStatusChanged,
       "sdpTlsMacAddrLimitAlarmRaised": sdpTlsMacAddrLimitAlarmRaised,
       "sdpTlsMacAddrLimitAlarmCleared": sdpTlsMacAddrLimitAlarmCleared,
       "sdpTlsDHCPSuspiciousPcktRcvd": sdpTlsDHCPSuspiciousPcktRcvd,
       "sdpBindDHCPLeaseEntriesExceeded": sdpBindDHCPLeaseEntriesExceeded,
       "sdpBindDHCPLseStateOverride": sdpBindDHCPLseStateOverride,
       "sdpBindDHCPSuspiciousPcktRcvd": sdpBindDHCPSuspiciousPcktRcvd,
       "sdpBindDHCPLseStatePopulateErr": sdpBindDHCPLseStatePopulateErr,
       "sdpBindPwPeerStatusBitsChanged": sdpBindPwPeerStatusBitsChanged,
       "sdpBindTlsMacMoveExceeded": sdpBindTlsMacMoveExceeded,
       "sdpBindPwPeerFaultAddrChanged": sdpBindPwPeerFaultAddrChanged,
       "sdpBindDHCPProxyServerError": sdpBindDHCPProxyServerError,
       "sdpBindDHCPCoAError": sdpBindDHCPCoAError,
       "sdpBindDHCPSubAuthError": sdpBindDHCPSubAuthError,
       "sdpBindSdpStateChangeProcessed": sdpBindSdpStateChangeProcessed,
       "sdpBindDHCPLseStateMobilityErr": sdpBindDHCPLseStateMobilityErr,
       "sdpBandwidthOverbooked": sdpBandwidthOverbooked,
       "sdpBindInsufficientBandwidth": sdpBindInsufficientBandwidth,
       "dynamicSdpConfigChanged": dynamicSdpConfigChanged,
       "dynamicSdpBindConfigChanged": dynamicSdpBindConfigChanged,
       "dynamicSdpCreationFailed": dynamicSdpCreationFailed,
       "dynamicSdpBindCreationFailed": dynamicSdpBindCreationFailed,
       "unacknowledgedTCN": unacknowledgedTCN,
       "tmnxSvcTopoChgSdpBindMajorState": tmnxSvcTopoChgSdpBindMajorState,
       "tmnxSvcNewRootSdpBind": tmnxSvcNewRootSdpBind,
       "tmnxSvcTopoChgSdpBindState": tmnxSvcTopoChgSdpBindState,
       "tmnxSvcSdpBindRcvdTCN": tmnxSvcSdpBindRcvdTCN,
       "tmnxSvcSdpBindRcvdHigherBriPrio": tmnxSvcSdpBindRcvdHigherBriPrio,
       "tmnxSvcSdpBindEncapPVST": tmnxSvcSdpBindEncapPVST,
       "tmnxSvcSdpBindEncapDot1d": tmnxSvcSdpBindEncapDot1d,
       "tmnxSvcSdpActiveProtocolChange": tmnxSvcSdpActiveProtocolChange,
       "tmnxStpMeshNotInMstRegion": tmnxStpMeshNotInMstRegion,
       "tmnxSdpBndStpExcepCondStateChng": tmnxSdpBndStpExcepCondStateChng}
)
