# SNMP MIB module (HUAWEI-L2MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:21 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIdOrAny,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrAny")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwL2MultiCastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWPortType(Integer32, TextualConvention):
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
        *(("dot1q", 4),
          ("invalid", 1),
          ("pw", 2),
          ("switchport", 3),
          ("termination", 5))
    )



# MIB Managed Objects in the order of their OIDs

_HwIgspMibObject_ObjectIdentity = ObjectIdentity
hwIgspMibObject = _HwIgspMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1)
)
_HwIgspSystemInfo_ObjectIdentity = ObjectIdentity
hwIgspSystemInfo = _HwIgspSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 1)
)
_HwIgmpSnoopingEnabled_Type = EnabledStatus
_HwIgmpSnoopingEnabled_Object = MibScalar
hwIgmpSnoopingEnabled = _HwIgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 1, 1),
    _HwIgmpSnoopingEnabled_Type()
)
hwIgmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingEnabled.setStatus("current")
_HwSendQueryEnabled_Type = EnabledStatus
_HwSendQueryEnabled_Object = MibScalar
hwSendQueryEnabled = _HwSendQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 1, 2),
    _HwSendQueryEnabled_Type()
)
hwSendQueryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSendQueryEnabled.setStatus("current")
_HwSendQuerySourceIpAddr_Type = IpAddress
_HwSendQuerySourceIpAddr_Object = MibScalar
hwSendQuerySourceIpAddr = _HwSendQuerySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 1, 3),
    _HwSendQuerySourceIpAddr_Type()
)
hwSendQuerySourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSendQuerySourceIpAddr.setStatus("current")


class _HwL2mcCacTrapInterval_Type(Integer32):
    """Custom type hwL2mcCacTrapInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_HwL2mcCacTrapInterval_Type.__name__ = "Integer32"
_HwL2mcCacTrapInterval_Object = MibScalar
hwL2mcCacTrapInterval = _HwL2mcCacTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 1, 4),
    _HwL2mcCacTrapInterval_Type()
)
hwL2mcCacTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2mcCacTrapInterval.setStatus("current")
_HwL2mcCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcCfgInfo = _HwL2mcCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2)
)
_HwL2mcCfgTable_Object = MibTable
hwL2mcCfgTable = _HwL2mcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwL2mcCfgTable.setStatus("current")
_HwL2mcCfgEntry_Object = MibTableRow
hwL2mcCfgEntry = _HwL2mcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1)
)
hwL2mcCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcCfgEntry.setStatus("current")
_HwL2mcVlanIndex_Type = VlanIdOrAny
_HwL2mcVlanIndex_Object = MibTableColumn
hwL2mcVlanIndex = _HwL2mcVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 1),
    _HwL2mcVlanIndex_Type()
)
hwL2mcVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcVlanIndex.setStatus("current")


class _HwL2mcVsiName_Type(DisplayString):
    """Custom type hwL2mcVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcVsiName_Type.__name__ = "DisplayString"
_HwL2mcVsiName_Object = MibTableColumn
hwL2mcVsiName = _HwL2mcVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 2),
    _HwL2mcVsiName_Type()
)
hwL2mcVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcVsiName.setStatus("current")
_HwL2mcEnabled_Type = EnabledStatus
_HwL2mcEnabled_Object = MibTableColumn
hwL2mcEnabled = _HwL2mcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 3),
    _HwL2mcEnabled_Type()
)
hwL2mcEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcEnabled.setStatus("current")


class _HwL2mcRouterAgingTime_Type(Integer32):
    """Custom type hwL2mcRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwL2mcRouterAgingTime_Type.__name__ = "Integer32"
_HwL2mcRouterAgingTime_Object = MibTableColumn
hwL2mcRouterAgingTime = _HwL2mcRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 4),
    _HwL2mcRouterAgingTime_Type()
)
hwL2mcRouterAgingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcRouterAgingTime.setStatus("current")


class _HwL2mcMaxQueryRespTime_Type(Integer32):
    """Custom type hwL2mcMaxQueryRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwL2mcMaxQueryRespTime_Type.__name__ = "Integer32"
_HwL2mcMaxQueryRespTime_Object = MibTableColumn
hwL2mcMaxQueryRespTime = _HwL2mcMaxQueryRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 5),
    _HwL2mcMaxQueryRespTime_Type()
)
hwL2mcMaxQueryRespTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcMaxQueryRespTime.setStatus("current")


class _HwL2mcLastMemQueryInterval_Type(Integer32):
    """Custom type hwL2mcLastMemQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwL2mcLastMemQueryInterval_Type.__name__ = "Integer32"
_HwL2mcLastMemQueryInterval_Object = MibTableColumn
hwL2mcLastMemQueryInterval = _HwL2mcLastMemQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 6),
    _HwL2mcLastMemQueryInterval_Type()
)
hwL2mcLastMemQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcLastMemQueryInterval.setStatus("current")


class _HwL2mcQueryInterval_Type(Integer32):
    """Custom type hwL2mcQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwL2mcQueryInterval_Type.__name__ = "Integer32"
_HwL2mcQueryInterval_Object = MibTableColumn
hwL2mcQueryInterval = _HwL2mcQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 7),
    _HwL2mcQueryInterval_Type()
)
hwL2mcQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcQueryInterval.setStatus("current")


class _HwL2mcRobustCount_Type(Integer32):
    """Custom type hwL2mcRobustCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_HwL2mcRobustCount_Type.__name__ = "Integer32"
_HwL2mcRobustCount_Object = MibTableColumn
hwL2mcRobustCount = _HwL2mcRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 8),
    _HwL2mcRobustCount_Type()
)
hwL2mcRobustCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcRobustCount.setStatus("current")
_HwL2mcCheckRouterAlert_Type = TruthValue
_HwL2mcCheckRouterAlert_Object = MibTableColumn
hwL2mcCheckRouterAlert = _HwL2mcCheckRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 9),
    _HwL2mcCheckRouterAlert_Type()
)
hwL2mcCheckRouterAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcCheckRouterAlert.setStatus("current")
_HwL2mcSendRouterAlert_Type = TruthValue
_HwL2mcSendRouterAlert_Object = MibTableColumn
hwL2mcSendRouterAlert = _HwL2mcSendRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 10),
    _HwL2mcSendRouterAlert_Type()
)
hwL2mcSendRouterAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcSendRouterAlert.setStatus("current")


class _HwL2mcIgmpVersion_Type(Integer32):
    """Custom type hwL2mcIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )


_HwL2mcIgmpVersion_Type.__name__ = "Integer32"
_HwL2mcIgmpVersion_Object = MibTableColumn
hwL2mcIgmpVersion = _HwL2mcIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 11),
    _HwL2mcIgmpVersion_Type()
)
hwL2mcIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcIgmpVersion.setStatus("current")


class _HwL2mcFwdMode_Type(Integer32):
    """Custom type hwL2mcFwdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_HwL2mcFwdMode_Type.__name__ = "Integer32"
_HwL2mcFwdMode_Object = MibTableColumn
hwL2mcFwdMode = _HwL2mcFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 12),
    _HwL2mcFwdMode_Type()
)
hwL2mcFwdMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcFwdMode.setStatus("current")
_HwL2mcPromptLeaveEnable_Type = EnabledStatus
_HwL2mcPromptLeaveEnable_Object = MibTableColumn
hwL2mcPromptLeaveEnable = _HwL2mcPromptLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 13),
    _HwL2mcPromptLeaveEnable_Type()
)
hwL2mcPromptLeaveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcPromptLeaveEnable.setStatus("current")


class _HwL2mcPromptLeaveAclNum_Type(Integer32):
    """Custom type hwL2mcPromptLeaveAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwL2mcPromptLeaveAclNum_Type.__name__ = "Integer32"
_HwL2mcPromptLeaveAclNum_Object = MibTableColumn
hwL2mcPromptLeaveAclNum = _HwL2mcPromptLeaveAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 14),
    _HwL2mcPromptLeaveAclNum_Type()
)
hwL2mcPromptLeaveAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcPromptLeaveAclNum.setStatus("current")
_HwL2mcRouterPortLearningEnable_Type = EnabledStatus
_HwL2mcRouterPortLearningEnable_Object = MibTableColumn
hwL2mcRouterPortLearningEnable = _HwL2mcRouterPortLearningEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 15),
    _HwL2mcRouterPortLearningEnable_Type()
)
hwL2mcRouterPortLearningEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcRouterPortLearningEnable.setStatus("current")
_HwL2mcReportSuppressEnable_Type = EnabledStatus
_HwL2mcReportSuppressEnable_Object = MibTableColumn
hwL2mcReportSuppressEnable = _HwL2mcReportSuppressEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 16),
    _HwL2mcReportSuppressEnable_Type()
)
hwL2mcReportSuppressEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcReportSuppressEnable.setStatus("current")
_HwL2mcIgmpQuerierEnable_Type = EnabledStatus
_HwL2mcIgmpQuerierEnable_Object = MibTableColumn
hwL2mcIgmpQuerierEnable = _HwL2mcIgmpQuerierEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 17),
    _HwL2mcIgmpQuerierEnable_Type()
)
hwL2mcIgmpQuerierEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcIgmpQuerierEnable.setStatus("current")
_HwL2mcIgmpSsmMappingEnable_Type = EnabledStatus
_HwL2mcIgmpSsmMappingEnable_Object = MibTableColumn
hwL2mcIgmpSsmMappingEnable = _HwL2mcIgmpSsmMappingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 18),
    _HwL2mcIgmpSsmMappingEnable_Type()
)
hwL2mcIgmpSsmMappingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcIgmpSsmMappingEnable.setStatus("current")


class _HwL2mcSsmAclNum_Type(Integer32):
    """Custom type hwL2mcSsmAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwL2mcSsmAclNum_Type.__name__ = "Integer32"
_HwL2mcSsmAclNum_Object = MibTableColumn
hwL2mcSsmAclNum = _HwL2mcSsmAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 19),
    _HwL2mcSsmAclNum_Type()
)
hwL2mcSsmAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcSsmAclNum.setStatus("current")
_HwL2mcRowStatus_Type = RowStatus
_HwL2mcRowStatus_Object = MibTableColumn
hwL2mcRowStatus = _HwL2mcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 2, 1, 1, 100),
    _HwL2mcRowStatus_Type()
)
hwL2mcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcRowStatus.setStatus("current")
_HwL2mcStatisticsInfo_ObjectIdentity = ObjectIdentity
hwL2mcStatisticsInfo = _HwL2mcStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3)
)
_HwL2mcStatisticsTable_Object = MibTable
hwL2mcStatisticsTable = _HwL2mcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwL2mcStatisticsTable.setStatus("current")
_HwL2mcStatisticsEntry_Object = MibTableRow
hwL2mcStatisticsEntry = _HwL2mcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1)
)
hwL2mcStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcStatsVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcStatsVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcStatisticsEntry.setStatus("current")
_HwL2mcStatsVlanIndex_Type = VlanIdOrAny
_HwL2mcStatsVlanIndex_Object = MibTableColumn
hwL2mcStatsVlanIndex = _HwL2mcStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 1),
    _HwL2mcStatsVlanIndex_Type()
)
hwL2mcStatsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcStatsVlanIndex.setStatus("current")


class _HwL2mcStatsVsiName_Type(DisplayString):
    """Custom type hwL2mcStatsVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcStatsVsiName_Type.__name__ = "DisplayString"
_HwL2mcStatsVsiName_Object = MibTableColumn
hwL2mcStatsVsiName = _HwL2mcStatsVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 2),
    _HwL2mcStatsVsiName_Type()
)
hwL2mcStatsVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcStatsVsiName.setStatus("current")
_HwL2mcRecvIgmpV1ReportNum_Type = Counter32
_HwL2mcRecvIgmpV1ReportNum_Object = MibTableColumn
hwL2mcRecvIgmpV1ReportNum = _HwL2mcRecvIgmpV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 3),
    _HwL2mcRecvIgmpV1ReportNum_Type()
)
hwL2mcRecvIgmpV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV1ReportNum.setStatus("current")
_HwL2mcRecvIgmpV2ReportNum_Type = Counter32
_HwL2mcRecvIgmpV2ReportNum_Object = MibTableColumn
hwL2mcRecvIgmpV2ReportNum = _HwL2mcRecvIgmpV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 4),
    _HwL2mcRecvIgmpV2ReportNum_Type()
)
hwL2mcRecvIgmpV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV2ReportNum.setStatus("current")
_HwL2mcRecvIgmpV3ReportNum_Type = Counter32
_HwL2mcRecvIgmpV3ReportNum_Object = MibTableColumn
hwL2mcRecvIgmpV3ReportNum = _HwL2mcRecvIgmpV3ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 5),
    _HwL2mcRecvIgmpV3ReportNum_Type()
)
hwL2mcRecvIgmpV3ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV3ReportNum.setStatus("current")
_HwL2mcRecvIgmpLeaveNum_Type = Counter32
_HwL2mcRecvIgmpLeaveNum_Object = MibTableColumn
hwL2mcRecvIgmpLeaveNum = _HwL2mcRecvIgmpLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 6),
    _HwL2mcRecvIgmpLeaveNum_Type()
)
hwL2mcRecvIgmpLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpLeaveNum.setStatus("current")
_HwL2mcRecvIgmpV1QueryNum_Type = Counter32
_HwL2mcRecvIgmpV1QueryNum_Object = MibTableColumn
hwL2mcRecvIgmpV1QueryNum = _HwL2mcRecvIgmpV1QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 7),
    _HwL2mcRecvIgmpV1QueryNum_Type()
)
hwL2mcRecvIgmpV1QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV1QueryNum.setStatus("current")
_HwL2mcRecvIgmpV2QueryNum_Type = Counter32
_HwL2mcRecvIgmpV2QueryNum_Object = MibTableColumn
hwL2mcRecvIgmpV2QueryNum = _HwL2mcRecvIgmpV2QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 8),
    _HwL2mcRecvIgmpV2QueryNum_Type()
)
hwL2mcRecvIgmpV2QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV2QueryNum.setStatus("current")
_HwL2mcRecvIgmpV3QueryNum_Type = Counter32
_HwL2mcRecvIgmpV3QueryNum_Object = MibTableColumn
hwL2mcRecvIgmpV3QueryNum = _HwL2mcRecvIgmpV3QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 9),
    _HwL2mcRecvIgmpV3QueryNum_Type()
)
hwL2mcRecvIgmpV3QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvIgmpV3QueryNum.setStatus("current")
_HwL2mcRecvPimHelloNum_Type = Counter32
_HwL2mcRecvPimHelloNum_Object = MibTableColumn
hwL2mcRecvPimHelloNum = _HwL2mcRecvPimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 10),
    _HwL2mcRecvPimHelloNum_Type()
)
hwL2mcRecvPimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRecvPimHelloNum.setStatus("current")
_HwL2mcSendQueryNum_Type = Counter32
_HwL2mcSendQueryNum_Object = MibTableColumn
hwL2mcSendQueryNum = _HwL2mcSendQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 11),
    _HwL2mcSendQueryNum_Type()
)
hwL2mcSendQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcSendQueryNum.setStatus("current")
_HwL2mcSendQuerySourceNum_Type = Counter32
_HwL2mcSendQuerySourceNum_Object = MibTableColumn
hwL2mcSendQuerySourceNum = _HwL2mcSendQuerySourceNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 12),
    _HwL2mcSendQuerySourceNum_Type()
)
hwL2mcSendQuerySourceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcSendQuerySourceNum.setStatus("current")
_HwL2mcProxyGenQueryNum_Type = Counter32
_HwL2mcProxyGenQueryNum_Object = MibTableColumn
hwL2mcProxyGenQueryNum = _HwL2mcProxyGenQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 13),
    _HwL2mcProxyGenQueryNum_Type()
)
hwL2mcProxyGenQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcProxyGenQueryNum.setStatus("current")
_HwL2mcProxyGroupQueryNum_Type = Counter32
_HwL2mcProxyGroupQueryNum_Object = MibTableColumn
hwL2mcProxyGroupQueryNum = _HwL2mcProxyGroupQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 14),
    _HwL2mcProxyGroupQueryNum_Type()
)
hwL2mcProxyGroupQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcProxyGroupQueryNum.setStatus("current")
_HwL2mcProxyGroupSourceQueryNum_Type = Counter32
_HwL2mcProxyGroupSourceQueryNum_Object = MibTableColumn
hwL2mcProxyGroupSourceQueryNum = _HwL2mcProxyGroupSourceQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 15),
    _HwL2mcProxyGroupSourceQueryNum_Type()
)
hwL2mcProxyGroupSourceQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcProxyGroupSourceQueryNum.setStatus("current")
_HwL2mcIgmpPacketClearStats_Type = TruthValue
_HwL2mcIgmpPacketClearStats_Object = MibTableColumn
hwL2mcIgmpPacketClearStats = _HwL2mcIgmpPacketClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 3, 1, 1, 30),
    _HwL2mcIgmpPacketClearStats_Type()
)
hwL2mcIgmpPacketClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2mcIgmpPacketClearStats.setStatus("current")
_HwL2mcFwdInfo_ObjectIdentity = ObjectIdentity
hwL2mcFwdInfo = _HwL2mcFwdInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4)
)
_HwL2mcFwdTable_Object = MibTable
hwL2mcFwdTable = _HwL2mcFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwL2mcFwdTable.setStatus("current")
_HwL2mcFwdEntry_Object = MibTableRow
hwL2mcFwdEntry = _HwL2mcFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1)
)
hwL2mcFwdEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdSourceAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdVcOrSiteId"),
)
if mibBuilder.loadTexts:
    hwL2mcFwdEntry.setStatus("current")
_HwL2mcFwdVlanIndex_Type = VlanIdOrAny
_HwL2mcFwdVlanIndex_Object = MibTableColumn
hwL2mcFwdVlanIndex = _HwL2mcFwdVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 1),
    _HwL2mcFwdVlanIndex_Type()
)
hwL2mcFwdVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdVlanIndex.setStatus("current")


class _HwL2mcFwdVsiName_Type(DisplayString):
    """Custom type hwL2mcFwdVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcFwdVsiName_Type.__name__ = "DisplayString"
_HwL2mcFwdVsiName_Object = MibTableColumn
hwL2mcFwdVsiName = _HwL2mcFwdVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 2),
    _HwL2mcFwdVsiName_Type()
)
hwL2mcFwdVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdVsiName.setStatus("current")
_HwL2mcFwdGroupAddress_Type = IpAddress
_HwL2mcFwdGroupAddress_Object = MibTableColumn
hwL2mcFwdGroupAddress = _HwL2mcFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 3),
    _HwL2mcFwdGroupAddress_Type()
)
hwL2mcFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdGroupAddress.setStatus("current")
_HwL2mcFwdSourceAddress_Type = IpAddress
_HwL2mcFwdSourceAddress_Object = MibTableColumn
hwL2mcFwdSourceAddress = _HwL2mcFwdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 4),
    _HwL2mcFwdSourceAddress_Type()
)
hwL2mcFwdSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdSourceAddress.setStatus("current")
_HwL2mcFwdPortType_Type = HWPortType
_HwL2mcFwdPortType_Object = MibTableColumn
hwL2mcFwdPortType = _HwL2mcFwdPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 5),
    _HwL2mcFwdPortType_Type()
)
hwL2mcFwdPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdPortType.setStatus("current")
_HwL2mcFwdPortIfIndex_Type = InterfaceIndexOrZero
_HwL2mcFwdPortIfIndex_Object = MibTableColumn
hwL2mcFwdPortIfIndex = _HwL2mcFwdPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 6),
    _HwL2mcFwdPortIfIndex_Type()
)
hwL2mcFwdPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdPortIfIndex.setStatus("current")
_HwL2mcFwdPortPeId_Type = VlanIdOrAny
_HwL2mcFwdPortPeId_Object = MibTableColumn
hwL2mcFwdPortPeId = _HwL2mcFwdPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 7),
    _HwL2mcFwdPortPeId_Type()
)
hwL2mcFwdPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdPortPeId.setStatus("current")
_HwL2mcFwdPortCeId_Type = VlanIdOrAny
_HwL2mcFwdPortCeId_Object = MibTableColumn
hwL2mcFwdPortCeId = _HwL2mcFwdPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 8),
    _HwL2mcFwdPortCeId_Type()
)
hwL2mcFwdPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdPortCeId.setStatus("current")
_HwL2mcFwdPeerAddress_Type = IpAddress
_HwL2mcFwdPeerAddress_Object = MibTableColumn
hwL2mcFwdPeerAddress = _HwL2mcFwdPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 9),
    _HwL2mcFwdPeerAddress_Type()
)
hwL2mcFwdPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdPeerAddress.setStatus("current")


class _HwL2mcFwdVcOrSiteId_Type(Unsigned32):
    """Custom type hwL2mcFwdVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwL2mcFwdVcOrSiteId_Type.__name__ = "Unsigned32"
_HwL2mcFwdVcOrSiteId_Object = MibTableColumn
hwL2mcFwdVcOrSiteId = _HwL2mcFwdVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 10),
    _HwL2mcFwdVcOrSiteId_Type()
)
hwL2mcFwdVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFwdVcOrSiteId.setStatus("current")


class _HwL2mcFwdAddressType_Type(Integer32):
    """Custom type hwL2mcFwdAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2))
    )


_HwL2mcFwdAddressType_Type.__name__ = "Integer32"
_HwL2mcFwdAddressType_Object = MibTableColumn
hwL2mcFwdAddressType = _HwL2mcFwdAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 11),
    _HwL2mcFwdAddressType_Type()
)
hwL2mcFwdAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcFwdAddressType.setStatus("current")


class _HwL2mcFwdHostFlag1_Type(Integer32):
    """Custom type hwL2mcFwdHostFlag1 based on Integer32"""
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
        *(("dynamic", 2),
          ("invalid", 4),
          ("static", 1),
          ("staticDynamic", 3))
    )


_HwL2mcFwdHostFlag1_Type.__name__ = "Integer32"
_HwL2mcFwdHostFlag1_Object = MibTableColumn
hwL2mcFwdHostFlag1 = _HwL2mcFwdHostFlag1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 18),
    _HwL2mcFwdHostFlag1_Type()
)
hwL2mcFwdHostFlag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcFwdHostFlag1.setStatus("current")


class _HwL2mcFwdHostFlag2_Type(Integer32):
    """Custom type hwL2mcFwdHostFlag2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapping", 2),
          ("nonMapping", 1))
    )


_HwL2mcFwdHostFlag2_Type.__name__ = "Integer32"
_HwL2mcFwdHostFlag2_Object = MibTableColumn
hwL2mcFwdHostFlag2 = _HwL2mcFwdHostFlag2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 19),
    _HwL2mcFwdHostFlag2_Type()
)
hwL2mcFwdHostFlag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcFwdHostFlag2.setStatus("current")


class _HwL2mcFwdHostFlag3_Type(Integer32):
    """Custom type hwL2mcFwdHostFlag3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 1),
          ("router", 2))
    )


_HwL2mcFwdHostFlag3_Type.__name__ = "Integer32"
_HwL2mcFwdHostFlag3_Object = MibTableColumn
hwL2mcFwdHostFlag3 = _HwL2mcFwdHostFlag3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 20),
    _HwL2mcFwdHostFlag3_Type()
)
hwL2mcFwdHostFlag3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcFwdHostFlag3.setStatus("current")


class _HwL2mcFwdHostFlag4_Type(Integer32):
    """Custom type hwL2mcFwdHostFlag4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("port", 1),
          ("static", 2))
    )


_HwL2mcFwdHostFlag4_Type.__name__ = "Integer32"
_HwL2mcFwdHostFlag4_Object = MibTableColumn
hwL2mcFwdHostFlag4 = _HwL2mcFwdHostFlag4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 4, 1, 1, 21),
    _HwL2mcFwdHostFlag4_Type()
)
hwL2mcFwdHostFlag4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcFwdHostFlag4.setStatus("current")
_HwL2mcGroupInfo_ObjectIdentity = ObjectIdentity
hwL2mcGroupInfo = _HwL2mcGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5)
)
_HwL2mcGroupInfoTable_Object = MibTable
hwL2mcGroupInfoTable = _HwL2mcGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwL2mcGroupInfoTable.setStatus("current")
_HwL2mcGroupInfoEntry_Object = MibTableRow
hwL2mcGroupInfoEntry = _HwL2mcGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1)
)
hwL2mcGroupInfoEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupSourceAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupVcOrSiteId"),
)
if mibBuilder.loadTexts:
    hwL2mcGroupInfoEntry.setStatus("current")
_HwL2mcGroupVlanIndex_Type = VlanIdOrAny
_HwL2mcGroupVlanIndex_Object = MibTableColumn
hwL2mcGroupVlanIndex = _HwL2mcGroupVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 1),
    _HwL2mcGroupVlanIndex_Type()
)
hwL2mcGroupVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupVlanIndex.setStatus("current")


class _HwL2mcGroupVsiName_Type(DisplayString):
    """Custom type hwL2mcGroupVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcGroupVsiName_Type.__name__ = "DisplayString"
_HwL2mcGroupVsiName_Object = MibTableColumn
hwL2mcGroupVsiName = _HwL2mcGroupVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 2),
    _HwL2mcGroupVsiName_Type()
)
hwL2mcGroupVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupVsiName.setStatus("current")
_HwL2mcGroupGroupAddress_Type = IpAddress
_HwL2mcGroupGroupAddress_Object = MibTableColumn
hwL2mcGroupGroupAddress = _HwL2mcGroupGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 3),
    _HwL2mcGroupGroupAddress_Type()
)
hwL2mcGroupGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupGroupAddress.setStatus("current")
_HwL2mcGroupSourceAddress_Type = IpAddress
_HwL2mcGroupSourceAddress_Object = MibTableColumn
hwL2mcGroupSourceAddress = _HwL2mcGroupSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 4),
    _HwL2mcGroupSourceAddress_Type()
)
hwL2mcGroupSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupSourceAddress.setStatus("current")
_HwL2mcPortType_Type = HWPortType
_HwL2mcPortType_Object = MibTableColumn
hwL2mcPortType = _HwL2mcPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 5),
    _HwL2mcPortType_Type()
)
hwL2mcPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcPortType.setStatus("current")
_HwL2mcGroupPortIfIndex_Type = InterfaceIndexOrZero
_HwL2mcGroupPortIfIndex_Object = MibTableColumn
hwL2mcGroupPortIfIndex = _HwL2mcGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 6),
    _HwL2mcGroupPortIfIndex_Type()
)
hwL2mcGroupPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupPortIfIndex.setStatus("current")
_HwL2mcGroupPortPeId_Type = VlanIdOrAny
_HwL2mcGroupPortPeId_Object = MibTableColumn
hwL2mcGroupPortPeId = _HwL2mcGroupPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 7),
    _HwL2mcGroupPortPeId_Type()
)
hwL2mcGroupPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupPortPeId.setStatus("current")
_HwL2mcGroupPortCeId_Type = VlanIdOrAny
_HwL2mcGroupPortCeId_Object = MibTableColumn
hwL2mcGroupPortCeId = _HwL2mcGroupPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 8),
    _HwL2mcGroupPortCeId_Type()
)
hwL2mcGroupPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupPortCeId.setStatus("current")
_HwL2mcGroupPeerAddress_Type = IpAddress
_HwL2mcGroupPeerAddress_Object = MibTableColumn
hwL2mcGroupPeerAddress = _HwL2mcGroupPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 9),
    _HwL2mcGroupPeerAddress_Type()
)
hwL2mcGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupPeerAddress.setStatus("current")


class _HwL2mcGroupVcOrSiteId_Type(Unsigned32):
    """Custom type hwL2mcGroupVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwL2mcGroupVcOrSiteId_Type.__name__ = "Unsigned32"
_HwL2mcGroupVcOrSiteId_Object = MibTableColumn
hwL2mcGroupVcOrSiteId = _HwL2mcGroupVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 10),
    _HwL2mcGroupVcOrSiteId_Type()
)
hwL2mcGroupVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcGroupVcOrSiteId.setStatus("current")
_HwL2mcSourceUpTime_Type = Counter32
_HwL2mcSourceUpTime_Object = MibTableColumn
hwL2mcSourceUpTime = _HwL2mcSourceUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 14),
    _HwL2mcSourceUpTime_Type()
)
hwL2mcSourceUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcSourceUpTime.setStatus("current")
_HwL2mcSourceExpires_Type = Counter32
_HwL2mcSourceExpires_Object = MibTableColumn
hwL2mcSourceExpires = _HwL2mcSourceExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 15),
    _HwL2mcSourceExpires_Type()
)
hwL2mcSourceExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcSourceExpires.setStatus("current")
_HwL2mcGroupUpTime_Type = Counter32
_HwL2mcGroupUpTime_Object = MibTableColumn
hwL2mcGroupUpTime = _HwL2mcGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 16),
    _HwL2mcGroupUpTime_Type()
)
hwL2mcGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupUpTime.setStatus("current")
_HwL2mcGroupExpires_Type = Counter32
_HwL2mcGroupExpires_Object = MibTableColumn
hwL2mcGroupExpires = _HwL2mcGroupExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 17),
    _HwL2mcGroupExpires_Type()
)
hwL2mcGroupExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupExpires.setStatus("current")


class _HwL2mcGroupFilterFlag_Type(Integer32):
    """Custom type hwL2mcGroupFilterFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1),
          ("invalid", 3))
    )


_HwL2mcGroupFilterFlag_Type.__name__ = "Integer32"
_HwL2mcGroupFilterFlag_Object = MibTableColumn
hwL2mcGroupFilterFlag = _HwL2mcGroupFilterFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 18),
    _HwL2mcGroupFilterFlag_Type()
)
hwL2mcGroupFilterFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupFilterFlag.setStatus("current")


class _HwL2mcGroupHostFlag1_Type(Integer32):
    """Custom type hwL2mcGroupHostFlag1 based on Integer32"""
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
        *(("dynamic", 2),
          ("invalid", 4),
          ("static", 1),
          ("staticDynamic", 3))
    )


_HwL2mcGroupHostFlag1_Type.__name__ = "Integer32"
_HwL2mcGroupHostFlag1_Object = MibTableColumn
hwL2mcGroupHostFlag1 = _HwL2mcGroupHostFlag1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 19),
    _HwL2mcGroupHostFlag1_Type()
)
hwL2mcGroupHostFlag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupHostFlag1.setStatus("current")


class _HwL2mcGroupHostFlag2_Type(Integer32):
    """Custom type hwL2mcGroupHostFlag2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapping", 2),
          ("nonMapping", 1))
    )


_HwL2mcGroupHostFlag2_Type.__name__ = "Integer32"
_HwL2mcGroupHostFlag2_Object = MibTableColumn
hwL2mcGroupHostFlag2 = _HwL2mcGroupHostFlag2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 20),
    _HwL2mcGroupHostFlag2_Type()
)
hwL2mcGroupHostFlag2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupHostFlag2.setStatus("current")
_HwL2mcGroupRowStatus_Type = RowStatus
_HwL2mcGroupRowStatus_Object = MibTableColumn
hwL2mcGroupRowStatus = _HwL2mcGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 5, 1, 1, 100),
    _HwL2mcGroupRowStatus_Type()
)
hwL2mcGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcGroupRowStatus.setStatus("current")
_HwL2mcGroupCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcGroupCfgInfo = _HwL2mcGroupCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6)
)
_HwL2mcGroupCfgTable_Object = MibTable
hwL2mcGroupCfgTable = _HwL2mcGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hwL2mcGroupCfgTable.setStatus("current")
_HwL2mcGroupCfgEntry_Object = MibTableRow
hwL2mcGroupCfgEntry = _HwL2mcGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1)
)
hwL2mcGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgVcOrSiteId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupCfgSourceAddress"),
)
if mibBuilder.loadTexts:
    hwL2mcGroupCfgEntry.setStatus("current")
_HwGroupCfgPortType_Type = HWPortType
_HwGroupCfgPortType_Object = MibTableColumn
hwGroupCfgPortType = _HwGroupCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 1),
    _HwGroupCfgPortType_Type()
)
hwGroupCfgPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgPortType.setStatus("current")
_HwGroupCfgPortIfIndex_Type = InterfaceIndexOrZero
_HwGroupCfgPortIfIndex_Object = MibTableColumn
hwGroupCfgPortIfIndex = _HwGroupCfgPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 2),
    _HwGroupCfgPortIfIndex_Type()
)
hwGroupCfgPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgPortIfIndex.setStatus("current")
_HwGroupCfgPortPeId_Type = VlanIdOrAny
_HwGroupCfgPortPeId_Object = MibTableColumn
hwGroupCfgPortPeId = _HwGroupCfgPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 3),
    _HwGroupCfgPortPeId_Type()
)
hwGroupCfgPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgPortPeId.setStatus("current")
_HwGroupCfgPortCeId_Type = VlanIdOrAny
_HwGroupCfgPortCeId_Object = MibTableColumn
hwGroupCfgPortCeId = _HwGroupCfgPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 4),
    _HwGroupCfgPortCeId_Type()
)
hwGroupCfgPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgPortCeId.setStatus("current")
_HwGroupCfgPeerAddress_Type = IpAddress
_HwGroupCfgPeerAddress_Object = MibTableColumn
hwGroupCfgPeerAddress = _HwGroupCfgPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 5),
    _HwGroupCfgPeerAddress_Type()
)
hwGroupCfgPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgPeerAddress.setStatus("current")


class _HwGroupCfgVcOrSiteId_Type(Unsigned32):
    """Custom type hwGroupCfgVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwGroupCfgVcOrSiteId_Type.__name__ = "Unsigned32"
_HwGroupCfgVcOrSiteId_Object = MibTableColumn
hwGroupCfgVcOrSiteId = _HwGroupCfgVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 6),
    _HwGroupCfgVcOrSiteId_Type()
)
hwGroupCfgVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgVcOrSiteId.setStatus("current")
_HwGroupCfgVlanIndex_Type = VlanIdOrAny
_HwGroupCfgVlanIndex_Object = MibTableColumn
hwGroupCfgVlanIndex = _HwGroupCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 7),
    _HwGroupCfgVlanIndex_Type()
)
hwGroupCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgVlanIndex.setStatus("current")


class _HwGroupCfgVsiName_Type(DisplayString):
    """Custom type hwGroupCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwGroupCfgVsiName_Type.__name__ = "DisplayString"
_HwGroupCfgVsiName_Object = MibTableColumn
hwGroupCfgVsiName = _HwGroupCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 8),
    _HwGroupCfgVsiName_Type()
)
hwGroupCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgVsiName.setStatus("current")
_HwGroupCfgGroupAddress_Type = IpAddress
_HwGroupCfgGroupAddress_Object = MibTableColumn
hwGroupCfgGroupAddress = _HwGroupCfgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 9),
    _HwGroupCfgGroupAddress_Type()
)
hwGroupCfgGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgGroupAddress.setStatus("current")
_HwGroupCfgSourceAddress_Type = IpAddress
_HwGroupCfgSourceAddress_Object = MibTableColumn
hwGroupCfgSourceAddress = _HwGroupCfgSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 10),
    _HwGroupCfgSourceAddress_Type()
)
hwGroupCfgSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupCfgSourceAddress.setStatus("current")
_HwGroupCfgRowStatus_Type = RowStatus
_HwGroupCfgRowStatus_Object = MibTableColumn
hwGroupCfgRowStatus = _HwGroupCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 6, 1, 1, 100),
    _HwGroupCfgRowStatus_Type()
)
hwGroupCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGroupCfgRowStatus.setStatus("current")
_HwL2mcSsmSourceInfo_ObjectIdentity = ObjectIdentity
hwL2mcSsmSourceInfo = _HwL2mcSsmSourceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7)
)
_HwL2mcSsmSourceTable_Object = MibTable
hwL2mcSsmSourceTable = _HwL2mcSsmSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwL2mcSsmSourceTable.setStatus("current")
_HwL2mcSsmSourceEntry_Object = MibTableRow
hwL2mcSsmSourceEntry = _HwL2mcSsmSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1)
)
hwL2mcSsmSourceEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmSourceVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmSourceVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmGroupLen"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmSourceAddress"),
)
if mibBuilder.loadTexts:
    hwL2mcSsmSourceEntry.setStatus("current")
_HwL2mcSsmSourceVlanIndex_Type = VlanIdOrAny
_HwL2mcSsmSourceVlanIndex_Object = MibTableColumn
hwL2mcSsmSourceVlanIndex = _HwL2mcSsmSourceVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 1),
    _HwL2mcSsmSourceVlanIndex_Type()
)
hwL2mcSsmSourceVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcSsmSourceVlanIndex.setStatus("current")


class _HwL2mcSsmSourceVsiName_Type(DisplayString):
    """Custom type hwL2mcSsmSourceVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcSsmSourceVsiName_Type.__name__ = "DisplayString"
_HwL2mcSsmSourceVsiName_Object = MibTableColumn
hwL2mcSsmSourceVsiName = _HwL2mcSsmSourceVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 2),
    _HwL2mcSsmSourceVsiName_Type()
)
hwL2mcSsmSourceVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcSsmSourceVsiName.setStatus("current")
_HwL2mcSsmGroupAddress_Type = IpAddress
_HwL2mcSsmGroupAddress_Object = MibTableColumn
hwL2mcSsmGroupAddress = _HwL2mcSsmGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 3),
    _HwL2mcSsmGroupAddress_Type()
)
hwL2mcSsmGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcSsmGroupAddress.setStatus("current")


class _HwL2mcSsmGroupLen_Type(Integer32):
    """Custom type hwL2mcSsmGroupLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_HwL2mcSsmGroupLen_Type.__name__ = "Integer32"
_HwL2mcSsmGroupLen_Object = MibTableColumn
hwL2mcSsmGroupLen = _HwL2mcSsmGroupLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 4),
    _HwL2mcSsmGroupLen_Type()
)
hwL2mcSsmGroupLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcSsmGroupLen.setStatus("current")
_HwL2mcSsmSourceAddress_Type = IpAddress
_HwL2mcSsmSourceAddress_Object = MibTableColumn
hwL2mcSsmSourceAddress = _HwL2mcSsmSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 5),
    _HwL2mcSsmSourceAddress_Type()
)
hwL2mcSsmSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcSsmSourceAddress.setStatus("current")
_HwL2mcSsmSourceRowStatus_Type = RowStatus
_HwL2mcSsmSourceRowStatus_Object = MibTableColumn
hwL2mcSsmSourceRowStatus = _HwL2mcSsmSourceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 7, 1, 1, 100),
    _HwL2mcSsmSourceRowStatus_Type()
)
hwL2mcSsmSourceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcSsmSourceRowStatus.setStatus("current")
_HwL2mcPortGroupPolicyCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcPortGroupPolicyCfgInfo = _HwL2mcPortGroupPolicyCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8)
)
_HwL2mcPortGroupPolicyCfgTable_Object = MibTable
hwL2mcPortGroupPolicyCfgTable = _HwL2mcPortGroupPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1)
)
if mibBuilder.loadTexts:
    hwL2mcPortGroupPolicyCfgTable.setStatus("current")
_HwL2mcPortGroupPolicyCfgEntry_Object = MibTableRow
hwL2mcPortGroupPolicyCfgEntry = _HwL2mcPortGroupPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1)
)
hwL2mcPortGroupPolicyCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyVcOrSiteId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcPortGroupPolicyCfgEntry.setStatus("current")
_HwPortGroupPolicyPortType_Type = HWPortType
_HwPortGroupPolicyPortType_Object = MibTableColumn
hwPortGroupPolicyPortType = _HwPortGroupPolicyPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 1),
    _HwPortGroupPolicyPortType_Type()
)
hwPortGroupPolicyPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyPortType.setStatus("current")
_HwPortGroupPolicyPortIfIndex_Type = InterfaceIndexOrZero
_HwPortGroupPolicyPortIfIndex_Object = MibTableColumn
hwPortGroupPolicyPortIfIndex = _HwPortGroupPolicyPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 2),
    _HwPortGroupPolicyPortIfIndex_Type()
)
hwPortGroupPolicyPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyPortIfIndex.setStatus("current")
_HwPortGroupPolicyPortPeId_Type = VlanIdOrAny
_HwPortGroupPolicyPortPeId_Object = MibTableColumn
hwPortGroupPolicyPortPeId = _HwPortGroupPolicyPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 3),
    _HwPortGroupPolicyPortPeId_Type()
)
hwPortGroupPolicyPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyPortPeId.setStatus("current")
_HwPortGroupPolicyPortCeId_Type = VlanIdOrAny
_HwPortGroupPolicyPortCeId_Object = MibTableColumn
hwPortGroupPolicyPortCeId = _HwPortGroupPolicyPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 4),
    _HwPortGroupPolicyPortCeId_Type()
)
hwPortGroupPolicyPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyPortCeId.setStatus("current")
_HwPortGroupPolicyPeerAddress_Type = IpAddress
_HwPortGroupPolicyPeerAddress_Object = MibTableColumn
hwPortGroupPolicyPeerAddress = _HwPortGroupPolicyPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 5),
    _HwPortGroupPolicyPeerAddress_Type()
)
hwPortGroupPolicyPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyPeerAddress.setStatus("current")


class _HwPortGroupPolicyVcOrSiteId_Type(Unsigned32):
    """Custom type hwPortGroupPolicyVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwPortGroupPolicyVcOrSiteId_Type.__name__ = "Unsigned32"
_HwPortGroupPolicyVcOrSiteId_Object = MibTableColumn
hwPortGroupPolicyVcOrSiteId = _HwPortGroupPolicyVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 6),
    _HwPortGroupPolicyVcOrSiteId_Type()
)
hwPortGroupPolicyVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyVcOrSiteId.setStatus("current")
_HwPortGroupPolicyVlanIndex_Type = VlanIdOrAny
_HwPortGroupPolicyVlanIndex_Object = MibTableColumn
hwPortGroupPolicyVlanIndex = _HwPortGroupPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 7),
    _HwPortGroupPolicyVlanIndex_Type()
)
hwPortGroupPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyVlanIndex.setStatus("current")


class _HwPortGroupPolicyVsiName_Type(DisplayString):
    """Custom type hwPortGroupPolicyVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPortGroupPolicyVsiName_Type.__name__ = "DisplayString"
_HwPortGroupPolicyVsiName_Object = MibTableColumn
hwPortGroupPolicyVsiName = _HwPortGroupPolicyVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 8),
    _HwPortGroupPolicyVsiName_Type()
)
hwPortGroupPolicyVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyVsiName.setStatus("current")


class _HwPortGroupPolicyAclNum_Type(Integer32):
    """Custom type hwPortGroupPolicyAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwPortGroupPolicyAclNum_Type.__name__ = "Integer32"
_HwPortGroupPolicyAclNum_Object = MibTableColumn
hwPortGroupPolicyAclNum = _HwPortGroupPolicyAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 9),
    _HwPortGroupPolicyAclNum_Type()
)
hwPortGroupPolicyAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyAclNum.setStatus("current")


class _HwPortGroupPolicyIgmpVersion_Type(Integer32):
    """Custom type hwPortGroupPolicyIgmpVersion based on Integer32"""
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("versionAll", 0))
    )


_HwPortGroupPolicyIgmpVersion_Type.__name__ = "Integer32"
_HwPortGroupPolicyIgmpVersion_Object = MibTableColumn
hwPortGroupPolicyIgmpVersion = _HwPortGroupPolicyIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 10),
    _HwPortGroupPolicyIgmpVersion_Type()
)
hwPortGroupPolicyIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyIgmpVersion.setStatus("current")
_HwPortGroupPolicyRowStatus_Type = RowStatus
_HwPortGroupPolicyRowStatus_Object = MibTableColumn
hwPortGroupPolicyRowStatus = _HwPortGroupPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 8, 1, 1, 100),
    _HwPortGroupPolicyRowStatus_Type()
)
hwPortGroupPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyRowStatus.setStatus("current")
_HwL2mcChnlCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcChnlCfgInfo = _HwL2mcChnlCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9)
)
_HwL2mcChnlCfgTable_Object = MibTable
hwL2mcChnlCfgTable = _HwL2mcChnlCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hwL2mcChnlCfgTable.setStatus("current")
_HwL2mcChnlCfgEntry_Object = MibTableRow
hwL2mcChnlCfgEntry = _HwL2mcChnlCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1)
)
hwL2mcChnlCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlCfgVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlCfgChnlName"),
)
if mibBuilder.loadTexts:
    hwL2mcChnlCfgEntry.setStatus("current")
_HwChnlCfgVlanIndex_Type = VlanIdOrAny
_HwChnlCfgVlanIndex_Object = MibTableColumn
hwChnlCfgVlanIndex = _HwChnlCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1, 1),
    _HwChnlCfgVlanIndex_Type()
)
hwChnlCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlCfgVlanIndex.setStatus("current")


class _HwChnlCfgVsiName_Type(DisplayString):
    """Custom type hwChnlCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwChnlCfgVsiName_Type.__name__ = "DisplayString"
_HwChnlCfgVsiName_Object = MibTableColumn
hwChnlCfgVsiName = _HwChnlCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1, 2),
    _HwChnlCfgVsiName_Type()
)
hwChnlCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlCfgVsiName.setStatus("current")


class _HwChnlCfgChnlName_Type(DisplayString):
    """Custom type hwChnlCfgChnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwChnlCfgChnlName_Type.__name__ = "DisplayString"
_HwChnlCfgChnlName_Object = MibTableColumn
hwChnlCfgChnlName = _HwChnlCfgChnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1, 3),
    _HwChnlCfgChnlName_Type()
)
hwChnlCfgChnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlCfgChnlName.setStatus("current")


class _HwChnlCfgChnlType_Type(Integer32):
    """Custom type hwChnlCfgChnlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asm", 2),
          ("ssm", 1))
    )


_HwChnlCfgChnlType_Type.__name__ = "Integer32"
_HwChnlCfgChnlType_Object = MibTableColumn
hwChnlCfgChnlType = _HwChnlCfgChnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1, 9),
    _HwChnlCfgChnlType_Type()
)
hwChnlCfgChnlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlCfgChnlType.setStatus("current")
_HwChnlCfgRowStatus_Type = RowStatus
_HwChnlCfgRowStatus_Object = MibTableColumn
hwChnlCfgRowStatus = _HwChnlCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 9, 1, 1, 100),
    _HwChnlCfgRowStatus_Type()
)
hwChnlCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlCfgRowStatus.setStatus("current")
_HwL2mcLimitInfo_ObjectIdentity = ObjectIdentity
hwL2mcLimitInfo = _HwL2mcLimitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10)
)
_HwL2mcLimitTable_Object = MibTable
hwL2mcLimitTable = _HwL2mcLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1)
)
if mibBuilder.loadTexts:
    hwL2mcLimitTable.setStatus("current")
_HwL2mcLimitEntry_Object = MibTableRow
hwL2mcLimitEntry = _HwL2mcLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1)
)
hwL2mcLimitEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitChnlName"),
)
if mibBuilder.loadTexts:
    hwL2mcLimitEntry.setStatus("current")
_HwL2mcLimitVlanIndex_Type = VlanIdOrAny
_HwL2mcLimitVlanIndex_Object = MibTableColumn
hwL2mcLimitVlanIndex = _HwL2mcLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 1),
    _HwL2mcLimitVlanIndex_Type()
)
hwL2mcLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcLimitVlanIndex.setStatus("current")


class _HwL2mcLimitVsiName_Type(DisplayString):
    """Custom type hwL2mcLimitVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcLimitVsiName_Type.__name__ = "DisplayString"
_HwL2mcLimitVsiName_Object = MibTableColumn
hwL2mcLimitVsiName = _HwL2mcLimitVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 2),
    _HwL2mcLimitVsiName_Type()
)
hwL2mcLimitVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcLimitVsiName.setStatus("current")


class _HwL2mcLimitChnlName_Type(DisplayString):
    """Custom type hwL2mcLimitChnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcLimitChnlName_Type.__name__ = "DisplayString"
_HwL2mcLimitChnlName_Object = MibTableColumn
hwL2mcLimitChnlName = _HwL2mcLimitChnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 3),
    _HwL2mcLimitChnlName_Type()
)
hwL2mcLimitChnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcLimitChnlName.setStatus("current")


class _HwL2mcLimitMaxEntry_Type(Integer32):
    """Custom type hwL2mcLimitMaxEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_HwL2mcLimitMaxEntry_Type.__name__ = "Integer32"
_HwL2mcLimitMaxEntry_Object = MibTableColumn
hwL2mcLimitMaxEntry = _HwL2mcLimitMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 4),
    _HwL2mcLimitMaxEntry_Type()
)
hwL2mcLimitMaxEntry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcLimitMaxEntry.setStatus("current")
_HwL2mcLimitEntryCnt_Type = Counter32
_HwL2mcLimitEntryCnt_Object = MibTableColumn
hwL2mcLimitEntryCnt = _HwL2mcLimitEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 5),
    _HwL2mcLimitEntryCnt_Type()
)
hwL2mcLimitEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcLimitEntryCnt.setStatus("current")


class _HwL2mcLimitMaxBandWidth_Type(Integer32):
    """Custom type hwL2mcLimitMaxBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194304),
    )


_HwL2mcLimitMaxBandWidth_Type.__name__ = "Integer32"
_HwL2mcLimitMaxBandWidth_Object = MibTableColumn
hwL2mcLimitMaxBandWidth = _HwL2mcLimitMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 6),
    _HwL2mcLimitMaxBandWidth_Type()
)
hwL2mcLimitMaxBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcLimitMaxBandWidth.setStatus("current")
_HwL2mcLimitBandWidth_Type = Counter32
_HwL2mcLimitBandWidth_Object = MibTableColumn
hwL2mcLimitBandWidth = _HwL2mcLimitBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 7),
    _HwL2mcLimitBandWidth_Type()
)
hwL2mcLimitBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcLimitBandWidth.setStatus("current")


class _HwL2mcLimitAcl_Type(Integer32):
    """Custom type hwL2mcLimitAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwL2mcLimitAcl_Type.__name__ = "Integer32"
_HwL2mcLimitAcl_Object = MibTableColumn
hwL2mcLimitAcl = _HwL2mcLimitAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 8),
    _HwL2mcLimitAcl_Type()
)
hwL2mcLimitAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcLimitAcl.setStatus("current")
_HwL2mcLimitCfgRowStatus_Type = RowStatus
_HwL2mcLimitCfgRowStatus_Object = MibTableColumn
hwL2mcLimitCfgRowStatus = _HwL2mcLimitCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 10, 1, 1, 100),
    _HwL2mcLimitCfgRowStatus_Type()
)
hwL2mcLimitCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcLimitCfgRowStatus.setStatus("current")
_HwL2mcPortLimitInfo_ObjectIdentity = ObjectIdentity
hwL2mcPortLimitInfo = _HwL2mcPortLimitInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11)
)
_HwL2mcPortLimitTable_Object = MibTable
hwL2mcPortLimitTable = _HwL2mcPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hwL2mcPortLimitTable.setStatus("current")
_HwL2mcPortLimitEntry_Object = MibTableRow
hwL2mcPortLimitEntry = _HwL2mcPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1)
)
hwL2mcPortLimitEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitVcOrSiteId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwPortLimitChnlName"),
)
if mibBuilder.loadTexts:
    hwL2mcPortLimitEntry.setStatus("current")
_HwPortLimitVlanIndex_Type = VlanIdOrAny
_HwPortLimitVlanIndex_Object = MibTableColumn
hwPortLimitVlanIndex = _HwPortLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 1),
    _HwPortLimitVlanIndex_Type()
)
hwPortLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitVlanIndex.setStatus("current")


class _HwPortLimitVsiName_Type(DisplayString):
    """Custom type hwPortLimitVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPortLimitVsiName_Type.__name__ = "DisplayString"
_HwPortLimitVsiName_Object = MibTableColumn
hwPortLimitVsiName = _HwPortLimitVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 2),
    _HwPortLimitVsiName_Type()
)
hwPortLimitVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitVsiName.setStatus("current")
_HwPortLimitPortType_Type = HWPortType
_HwPortLimitPortType_Object = MibTableColumn
hwPortLimitPortType = _HwPortLimitPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 3),
    _HwPortLimitPortType_Type()
)
hwPortLimitPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitPortType.setStatus("current")
_HwPortLimitIfIndex_Type = InterfaceIndexOrZero
_HwPortLimitIfIndex_Object = MibTableColumn
hwPortLimitIfIndex = _HwPortLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 4),
    _HwPortLimitIfIndex_Type()
)
hwPortLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitIfIndex.setStatus("current")
_HwPortLimitPeId_Type = VlanIdOrAny
_HwPortLimitPeId_Object = MibTableColumn
hwPortLimitPeId = _HwPortLimitPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 5),
    _HwPortLimitPeId_Type()
)
hwPortLimitPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitPeId.setStatus("current")
_HwPortLimitCeId_Type = VlanIdOrAny
_HwPortLimitCeId_Object = MibTableColumn
hwPortLimitCeId = _HwPortLimitCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 6),
    _HwPortLimitCeId_Type()
)
hwPortLimitCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitCeId.setStatus("current")
_HwPortLimitPeerAddress_Type = IpAddress
_HwPortLimitPeerAddress_Object = MibTableColumn
hwPortLimitPeerAddress = _HwPortLimitPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 7),
    _HwPortLimitPeerAddress_Type()
)
hwPortLimitPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitPeerAddress.setStatus("current")


class _HwPortLimitVcOrSiteId_Type(Unsigned32):
    """Custom type hwPortLimitVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwPortLimitVcOrSiteId_Type.__name__ = "Unsigned32"
_HwPortLimitVcOrSiteId_Object = MibTableColumn
hwPortLimitVcOrSiteId = _HwPortLimitVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 8),
    _HwPortLimitVcOrSiteId_Type()
)
hwPortLimitVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitVcOrSiteId.setStatus("current")


class _HwPortLimitChnlName_Type(DisplayString):
    """Custom type hwPortLimitChnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwPortLimitChnlName_Type.__name__ = "DisplayString"
_HwPortLimitChnlName_Object = MibTableColumn
hwPortLimitChnlName = _HwPortLimitChnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 9),
    _HwPortLimitChnlName_Type()
)
hwPortLimitChnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitChnlName.setStatus("current")


class _HwPortLimitAcl_Type(Integer32):
    """Custom type hwPortLimitAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwPortLimitAcl_Type.__name__ = "Integer32"
_HwPortLimitAcl_Object = MibTableColumn
hwPortLimitAcl = _HwPortLimitAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 10),
    _HwPortLimitAcl_Type()
)
hwPortLimitAcl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitAcl.setStatus("current")


class _HwPortLimitMaxEntry_Type(Integer32):
    """Custom type hwPortLimitMaxEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_HwPortLimitMaxEntry_Type.__name__ = "Integer32"
_HwPortLimitMaxEntry_Object = MibTableColumn
hwPortLimitMaxEntry = _HwPortLimitMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 11),
    _HwPortLimitMaxEntry_Type()
)
hwPortLimitMaxEntry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitMaxEntry.setStatus("current")
_HwPortLimitEntryCnt_Type = Counter32
_HwPortLimitEntryCnt_Object = MibTableColumn
hwPortLimitEntryCnt = _HwPortLimitEntryCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 12),
    _HwPortLimitEntryCnt_Type()
)
hwPortLimitEntryCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortLimitEntryCnt.setStatus("current")


class _HwPortLimitMaxBandWidth_Type(Integer32):
    """Custom type hwPortLimitMaxBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4194304),
    )


_HwPortLimitMaxBandWidth_Type.__name__ = "Integer32"
_HwPortLimitMaxBandWidth_Object = MibTableColumn
hwPortLimitMaxBandWidth = _HwPortLimitMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 13),
    _HwPortLimitMaxBandWidth_Type()
)
hwPortLimitMaxBandWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitMaxBandWidth.setStatus("current")
_HwPortLimitBandWidth_Type = Counter32
_HwPortLimitBandWidth_Object = MibTableColumn
hwPortLimitBandWidth = _HwPortLimitBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 14),
    _HwPortLimitBandWidth_Type()
)
hwPortLimitBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortLimitBandWidth.setStatus("current")
_HwPortLimitCfgRowStatus_Type = RowStatus
_HwPortLimitCfgRowStatus_Object = MibTableColumn
hwPortLimitCfgRowStatus = _HwPortLimitCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 11, 1, 1, 100),
    _HwPortLimitCfgRowStatus_Type()
)
hwPortLimitCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitCfgRowStatus.setStatus("current")
_HwL2mcFastChnlCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcFastChnlCfgInfo = _HwL2mcFastChnlCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12)
)
_HwL2mcFastChnlCfgTable_Object = MibTable
hwL2mcFastChnlCfgTable = _HwL2mcFastChnlCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1)
)
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgTable.setStatus("current")
_HwL2mcFastChnlCfgEntry_Object = MibTableRow
hwL2mcFastChnlCfgEntry = _HwL2mcFastChnlCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1)
)
hwL2mcFastChnlCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgGroupLen"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgSourceAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgSourceLen"),
)
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgEntry.setStatus("current")
_HwL2mcFastChnlCfgVlanIndex_Type = VlanIdOrAny
_HwL2mcFastChnlCfgVlanIndex_Object = MibTableColumn
hwL2mcFastChnlCfgVlanIndex = _HwL2mcFastChnlCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 1),
    _HwL2mcFastChnlCfgVlanIndex_Type()
)
hwL2mcFastChnlCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgVlanIndex.setStatus("current")


class _HwL2mcFastChnlCfgVsiName_Type(DisplayString):
    """Custom type hwL2mcFastChnlCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcFastChnlCfgVsiName_Type.__name__ = "DisplayString"
_HwL2mcFastChnlCfgVsiName_Object = MibTableColumn
hwL2mcFastChnlCfgVsiName = _HwL2mcFastChnlCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 2),
    _HwL2mcFastChnlCfgVsiName_Type()
)
hwL2mcFastChnlCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgVsiName.setStatus("current")
_HwL2mcFastChnlCfgGroupAddress_Type = IpAddress
_HwL2mcFastChnlCfgGroupAddress_Object = MibTableColumn
hwL2mcFastChnlCfgGroupAddress = _HwL2mcFastChnlCfgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 3),
    _HwL2mcFastChnlCfgGroupAddress_Type()
)
hwL2mcFastChnlCfgGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgGroupAddress.setStatus("current")


class _HwL2mcFastChnlCfgGroupLen_Type(Integer32):
    """Custom type hwL2mcFastChnlCfgGroupLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_HwL2mcFastChnlCfgGroupLen_Type.__name__ = "Integer32"
_HwL2mcFastChnlCfgGroupLen_Object = MibTableColumn
hwL2mcFastChnlCfgGroupLen = _HwL2mcFastChnlCfgGroupLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 4),
    _HwL2mcFastChnlCfgGroupLen_Type()
)
hwL2mcFastChnlCfgGroupLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgGroupLen.setStatus("current")
_HwL2mcFastChnlCfgSourceAddress_Type = IpAddress
_HwL2mcFastChnlCfgSourceAddress_Object = MibTableColumn
hwL2mcFastChnlCfgSourceAddress = _HwL2mcFastChnlCfgSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 5),
    _HwL2mcFastChnlCfgSourceAddress_Type()
)
hwL2mcFastChnlCfgSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgSourceAddress.setStatus("current")


class _HwL2mcFastChnlCfgSourceLen_Type(Integer32):
    """Custom type hwL2mcFastChnlCfgSourceLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 32),
    )


_HwL2mcFastChnlCfgSourceLen_Type.__name__ = "Integer32"
_HwL2mcFastChnlCfgSourceLen_Object = MibTableColumn
hwL2mcFastChnlCfgSourceLen = _HwL2mcFastChnlCfgSourceLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 6),
    _HwL2mcFastChnlCfgSourceLen_Type()
)
hwL2mcFastChnlCfgSourceLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgSourceLen.setStatus("current")
_HwL2mcFastChnlCfgRowStatus_Type = RowStatus
_HwL2mcFastChnlCfgRowStatus_Object = MibTableColumn
hwL2mcFastChnlCfgRowStatus = _HwL2mcFastChnlCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 12, 1, 1, 100),
    _HwL2mcFastChnlCfgRowStatus_Type()
)
hwL2mcFastChnlCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgRowStatus.setStatus("current")
_HwL2mcRouterPortInfo_ObjectIdentity = ObjectIdentity
hwL2mcRouterPortInfo = _HwL2mcRouterPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13)
)
_HwL2mcRouterPortInfoTable_Object = MibTable
hwL2mcRouterPortInfoTable = _HwL2mcRouterPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortInfoTable.setStatus("current")
_HwL2mcRouterPortInfoEntry_Object = MibTableRow
hwL2mcRouterPortInfoEntry = _HwL2mcRouterPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1)
)
hwL2mcRouterPortInfoEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortVcOrSiteId"),
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortInfoEntry.setStatus("current")
_HwL2mcRouterPortVlanIndex_Type = VlanIdOrAny
_HwL2mcRouterPortVlanIndex_Object = MibTableColumn
hwL2mcRouterPortVlanIndex = _HwL2mcRouterPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 1),
    _HwL2mcRouterPortVlanIndex_Type()
)
hwL2mcRouterPortVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortVlanIndex.setStatus("current")


class _HwL2mcRouterPortVsiName_Type(DisplayString):
    """Custom type hwL2mcRouterPortVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcRouterPortVsiName_Type.__name__ = "DisplayString"
_HwL2mcRouterPortVsiName_Object = MibTableColumn
hwL2mcRouterPortVsiName = _HwL2mcRouterPortVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 2),
    _HwL2mcRouterPortVsiName_Type()
)
hwL2mcRouterPortVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortVsiName.setStatus("current")
_HwL2mcRouterPortType_Type = HWPortType
_HwL2mcRouterPortType_Object = MibTableColumn
hwL2mcRouterPortType = _HwL2mcRouterPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 3),
    _HwL2mcRouterPortType_Type()
)
hwL2mcRouterPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortType.setStatus("current")
_HwL2mcRouterPortIfIndex_Type = InterfaceIndexOrZero
_HwL2mcRouterPortIfIndex_Object = MibTableColumn
hwL2mcRouterPortIfIndex = _HwL2mcRouterPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 4),
    _HwL2mcRouterPortIfIndex_Type()
)
hwL2mcRouterPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortIfIndex.setStatus("current")
_HwL2mcRouterPortPeId_Type = VlanIdOrAny
_HwL2mcRouterPortPeId_Object = MibTableColumn
hwL2mcRouterPortPeId = _HwL2mcRouterPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 5),
    _HwL2mcRouterPortPeId_Type()
)
hwL2mcRouterPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortPeId.setStatus("current")
_HwL2mcRouterPortCeId_Type = VlanIdOrAny
_HwL2mcRouterPortCeId_Object = MibTableColumn
hwL2mcRouterPortCeId = _HwL2mcRouterPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 6),
    _HwL2mcRouterPortCeId_Type()
)
hwL2mcRouterPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCeId.setStatus("current")
_HwL2mcRouterPortPeerAddress_Type = IpAddress
_HwL2mcRouterPortPeerAddress_Object = MibTableColumn
hwL2mcRouterPortPeerAddress = _HwL2mcRouterPortPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 7),
    _HwL2mcRouterPortPeerAddress_Type()
)
hwL2mcRouterPortPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortPeerAddress.setStatus("current")


class _HwL2mcRouterPortVcOrSiteId_Type(Unsigned32):
    """Custom type hwL2mcRouterPortVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwL2mcRouterPortVcOrSiteId_Type.__name__ = "Unsigned32"
_HwL2mcRouterPortVcOrSiteId_Object = MibTableColumn
hwL2mcRouterPortVcOrSiteId = _HwL2mcRouterPortVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 8),
    _HwL2mcRouterPortVcOrSiteId_Type()
)
hwL2mcRouterPortVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortVcOrSiteId.setStatus("current")
_HwL2mcRouterPortGroupUpTime_Type = Counter32
_HwL2mcRouterPortGroupUpTime_Object = MibTableColumn
hwL2mcRouterPortGroupUpTime = _HwL2mcRouterPortGroupUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 16),
    _HwL2mcRouterPortGroupUpTime_Type()
)
hwL2mcRouterPortGroupUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRouterPortGroupUpTime.setStatus("current")
_HwL2mcRouterPortGroupExpires_Type = Counter32
_HwL2mcRouterPortGroupExpires_Object = MibTableColumn
hwL2mcRouterPortGroupExpires = _HwL2mcRouterPortGroupExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 17),
    _HwL2mcRouterPortGroupExpires_Type()
)
hwL2mcRouterPortGroupExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRouterPortGroupExpires.setStatus("current")


class _HwL2mcRouterPortGroupHostFlag1_Type(Integer32):
    """Custom type hwL2mcRouterPortGroupHostFlag1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1),
          ("staticDynamic", 3))
    )


_HwL2mcRouterPortGroupHostFlag1_Type.__name__ = "Integer32"
_HwL2mcRouterPortGroupHostFlag1_Object = MibTableColumn
hwL2mcRouterPortGroupHostFlag1 = _HwL2mcRouterPortGroupHostFlag1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 13, 1, 1, 19),
    _HwL2mcRouterPortGroupHostFlag1_Type()
)
hwL2mcRouterPortGroupHostFlag1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2mcRouterPortGroupHostFlag1.setStatus("current")
_HwL2mcRouterPortCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcRouterPortCfgInfo = _HwL2mcRouterPortCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14)
)
_HwL2mcRouterPortCfgTable_Object = MibTable
hwL2mcRouterPortCfgTable = _HwL2mcRouterPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1)
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgTable.setStatus("current")
_HwL2mcRouterPortCfgEntry_Object = MibTableRow
hwL2mcRouterPortCfgEntry = _HwL2mcRouterPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1)
)
hwL2mcRouterPortCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgPortType"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgPortIfIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgPortPeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgPortCeId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgPeerAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgVcOrSiteId"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgEntry.setStatus("current")
_HwL2mcRouterPortCfgPortType_Type = HWPortType
_HwL2mcRouterPortCfgPortType_Object = MibTableColumn
hwL2mcRouterPortCfgPortType = _HwL2mcRouterPortCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 1),
    _HwL2mcRouterPortCfgPortType_Type()
)
hwL2mcRouterPortCfgPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgPortType.setStatus("current")
_HwL2mcRouterPortCfgPortIfIndex_Type = InterfaceIndexOrZero
_HwL2mcRouterPortCfgPortIfIndex_Object = MibTableColumn
hwL2mcRouterPortCfgPortIfIndex = _HwL2mcRouterPortCfgPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 2),
    _HwL2mcRouterPortCfgPortIfIndex_Type()
)
hwL2mcRouterPortCfgPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgPortIfIndex.setStatus("current")
_HwL2mcRouterPortCfgPortPeId_Type = VlanIdOrAny
_HwL2mcRouterPortCfgPortPeId_Object = MibTableColumn
hwL2mcRouterPortCfgPortPeId = _HwL2mcRouterPortCfgPortPeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 3),
    _HwL2mcRouterPortCfgPortPeId_Type()
)
hwL2mcRouterPortCfgPortPeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgPortPeId.setStatus("current")
_HwL2mcRouterPortCfgPortCeId_Type = VlanIdOrAny
_HwL2mcRouterPortCfgPortCeId_Object = MibTableColumn
hwL2mcRouterPortCfgPortCeId = _HwL2mcRouterPortCfgPortCeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 4),
    _HwL2mcRouterPortCfgPortCeId_Type()
)
hwL2mcRouterPortCfgPortCeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgPortCeId.setStatus("current")
_HwL2mcRouterPortCfgPeerAddress_Type = IpAddress
_HwL2mcRouterPortCfgPeerAddress_Object = MibTableColumn
hwL2mcRouterPortCfgPeerAddress = _HwL2mcRouterPortCfgPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 5),
    _HwL2mcRouterPortCfgPeerAddress_Type()
)
hwL2mcRouterPortCfgPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgPeerAddress.setStatus("current")


class _HwL2mcRouterPortCfgVcOrSiteId_Type(Unsigned32):
    """Custom type hwL2mcRouterPortCfgVcOrSiteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HwL2mcRouterPortCfgVcOrSiteId_Type.__name__ = "Unsigned32"
_HwL2mcRouterPortCfgVcOrSiteId_Object = MibTableColumn
hwL2mcRouterPortCfgVcOrSiteId = _HwL2mcRouterPortCfgVcOrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 6),
    _HwL2mcRouterPortCfgVcOrSiteId_Type()
)
hwL2mcRouterPortCfgVcOrSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgVcOrSiteId.setStatus("current")
_HwL2mcRouterPortCfgVlanIndex_Type = VlanIdOrAny
_HwL2mcRouterPortCfgVlanIndex_Object = MibTableColumn
hwL2mcRouterPortCfgVlanIndex = _HwL2mcRouterPortCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 7),
    _HwL2mcRouterPortCfgVlanIndex_Type()
)
hwL2mcRouterPortCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgVlanIndex.setStatus("current")


class _HwL2mcRouterPortCfgVsiName_Type(DisplayString):
    """Custom type hwL2mcRouterPortCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwL2mcRouterPortCfgVsiName_Type.__name__ = "DisplayString"
_HwL2mcRouterPortCfgVsiName_Object = MibTableColumn
hwL2mcRouterPortCfgVsiName = _HwL2mcRouterPortCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 8),
    _HwL2mcRouterPortCfgVsiName_Type()
)
hwL2mcRouterPortCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgVsiName.setStatus("current")
_HwL2mcRouterPortCfgRowStatus_Type = RowStatus
_HwL2mcRouterPortCfgRowStatus_Object = MibTableColumn
hwL2mcRouterPortCfgRowStatus = _HwL2mcRouterPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 14, 1, 1, 100),
    _HwL2mcRouterPortCfgRowStatus_Type()
)
hwL2mcRouterPortCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgRowStatus.setStatus("current")
_HwL2mcChnlGroupCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcChnlGroupCfgInfo = _HwL2mcChnlGroupCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15)
)
_HwL2mcChnlGroupCfgTable_Object = MibTable
hwL2mcChnlGroupCfgTable = _HwL2mcChnlGroupCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hwL2mcChnlGroupCfgTable.setStatus("current")
_HwL2mcChnlGroupCfgEntry_Object = MibTableRow
hwL2mcChnlGroupCfgEntry = _HwL2mcChnlGroupCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1)
)
hwL2mcChnlGroupCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgVsiName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlCfgGroupChnlName"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgGroupAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgGroupLen"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgSourceAddress"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgSourceLen"),
)
if mibBuilder.loadTexts:
    hwL2mcChnlGroupCfgEntry.setStatus("current")
_HwChnlGroupCfgVlanIndex_Type = VlanIdOrAny
_HwChnlGroupCfgVlanIndex_Object = MibTableColumn
hwChnlGroupCfgVlanIndex = _HwChnlGroupCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 1),
    _HwChnlGroupCfgVlanIndex_Type()
)
hwChnlGroupCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgVlanIndex.setStatus("current")


class _HwChnlGroupCfgVsiName_Type(DisplayString):
    """Custom type hwChnlGroupCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwChnlGroupCfgVsiName_Type.__name__ = "DisplayString"
_HwChnlGroupCfgVsiName_Object = MibTableColumn
hwChnlGroupCfgVsiName = _HwChnlGroupCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 2),
    _HwChnlGroupCfgVsiName_Type()
)
hwChnlGroupCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgVsiName.setStatus("current")


class _HwChnlCfgGroupChnlName_Type(DisplayString):
    """Custom type hwChnlCfgGroupChnlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwChnlCfgGroupChnlName_Type.__name__ = "DisplayString"
_HwChnlCfgGroupChnlName_Object = MibTableColumn
hwChnlCfgGroupChnlName = _HwChnlCfgGroupChnlName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 3),
    _HwChnlCfgGroupChnlName_Type()
)
hwChnlCfgGroupChnlName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlCfgGroupChnlName.setStatus("current")
_HwChnlGroupCfgGroupAddress_Type = IpAddress
_HwChnlGroupCfgGroupAddress_Object = MibTableColumn
hwChnlGroupCfgGroupAddress = _HwChnlGroupCfgGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 4),
    _HwChnlGroupCfgGroupAddress_Type()
)
hwChnlGroupCfgGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgGroupAddress.setStatus("current")


class _HwChnlGroupCfgGroupLen_Type(Integer32):
    """Custom type hwChnlGroupCfgGroupLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 32),
    )


_HwChnlGroupCfgGroupLen_Type.__name__ = "Integer32"
_HwChnlGroupCfgGroupLen_Object = MibTableColumn
hwChnlGroupCfgGroupLen = _HwChnlGroupCfgGroupLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 5),
    _HwChnlGroupCfgGroupLen_Type()
)
hwChnlGroupCfgGroupLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgGroupLen.setStatus("current")
_HwChnlGroupCfgSourceAddress_Type = IpAddress
_HwChnlGroupCfgSourceAddress_Object = MibTableColumn
hwChnlGroupCfgSourceAddress = _HwChnlGroupCfgSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 6),
    _HwChnlGroupCfgSourceAddress_Type()
)
hwChnlGroupCfgSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgSourceAddress.setStatus("current")


class _HwChnlGroupCfgSourceLen_Type(Integer32):
    """Custom type hwChnlGroupCfgSourceLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(8, 32),
    )


_HwChnlGroupCfgSourceLen_Type.__name__ = "Integer32"
_HwChnlGroupCfgSourceLen_Object = MibTableColumn
hwChnlGroupCfgSourceLen = _HwChnlGroupCfgSourceLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 7),
    _HwChnlGroupCfgSourceLen_Type()
)
hwChnlGroupCfgSourceLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlGroupCfgSourceLen.setStatus("current")


class _HwChnlGroupCfgPerBand_Type(Integer32):
    """Custom type hwChnlGroupCfgPerBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwChnlGroupCfgPerBand_Type.__name__ = "Integer32"
_HwChnlGroupCfgPerBand_Object = MibTableColumn
hwChnlGroupCfgPerBand = _HwChnlGroupCfgPerBand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 9),
    _HwChnlGroupCfgPerBand_Type()
)
hwChnlGroupCfgPerBand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlGroupCfgPerBand.setStatus("current")
_HwChnlGroupCfgRowStatus_Type = RowStatus
_HwChnlGroupCfgRowStatus_Object = MibTableColumn
hwChnlGroupCfgRowStatus = _HwChnlGroupCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 15, 1, 1, 100),
    _HwChnlGroupCfgRowStatus_Type()
)
hwChnlGroupCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlGroupCfgRowStatus.setStatus("current")
_HwL2mcGroupPolicyCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcGroupPolicyCfgInfo = _HwL2mcGroupPolicyCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16)
)
_HwL2mcGroupPolicyCfgTable_Object = MibTable
hwL2mcGroupPolicyCfgTable = _HwL2mcGroupPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1)
)
if mibBuilder.loadTexts:
    hwL2mcGroupPolicyCfgTable.setStatus("current")
_HwL2mcGroupPolicyCfgEntry_Object = MibTableRow
hwL2mcGroupPolicyCfgEntry = _HwL2mcGroupPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1)
)
hwL2mcGroupPolicyCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupPolicyVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwGroupPolicyVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcGroupPolicyCfgEntry.setStatus("current")
_HwGroupPolicyVlanIndex_Type = VlanIdOrAny
_HwGroupPolicyVlanIndex_Object = MibTableColumn
hwGroupPolicyVlanIndex = _HwGroupPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1, 1),
    _HwGroupPolicyVlanIndex_Type()
)
hwGroupPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupPolicyVlanIndex.setStatus("current")


class _HwGroupPolicyVsiName_Type(DisplayString):
    """Custom type hwGroupPolicyVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwGroupPolicyVsiName_Type.__name__ = "DisplayString"
_HwGroupPolicyVsiName_Object = MibTableColumn
hwGroupPolicyVsiName = _HwGroupPolicyVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1, 2),
    _HwGroupPolicyVsiName_Type()
)
hwGroupPolicyVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGroupPolicyVsiName.setStatus("current")


class _HwGroupPolicyAclNum_Type(Integer32):
    """Custom type hwGroupPolicyAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwGroupPolicyAclNum_Type.__name__ = "Integer32"
_HwGroupPolicyAclNum_Object = MibTableColumn
hwGroupPolicyAclNum = _HwGroupPolicyAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1, 3),
    _HwGroupPolicyAclNum_Type()
)
hwGroupPolicyAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGroupPolicyAclNum.setStatus("current")


class _HwGroupPolicyIgmpVersion_Type(Integer32):
    """Custom type hwGroupPolicyIgmpVersion based on Integer32"""
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
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3),
          ("versionAll", 0))
    )


_HwGroupPolicyIgmpVersion_Type.__name__ = "Integer32"
_HwGroupPolicyIgmpVersion_Object = MibTableColumn
hwGroupPolicyIgmpVersion = _HwGroupPolicyIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1, 4),
    _HwGroupPolicyIgmpVersion_Type()
)
hwGroupPolicyIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGroupPolicyIgmpVersion.setStatus("current")
_HwGroupPolicyRowStatus_Type = RowStatus
_HwGroupPolicyRowStatus_Object = MibTableColumn
hwGroupPolicyRowStatus = _HwGroupPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 16, 1, 1, 100),
    _HwGroupPolicyRowStatus_Type()
)
hwGroupPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGroupPolicyRowStatus.setStatus("current")
_HwL2mcChnlDenyCfgInfo_ObjectIdentity = ObjectIdentity
hwL2mcChnlDenyCfgInfo = _HwL2mcChnlDenyCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17)
)
_HwL2mcChnlDenyCfgTable_Object = MibTable
hwL2mcChnlDenyCfgTable = _HwL2mcChnlDenyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1)
)
if mibBuilder.loadTexts:
    hwL2mcChnlDenyCfgTable.setStatus("current")
_HwL2mcChnlDenyCfgEntry_Object = MibTableRow
hwL2mcChnlDenyCfgEntry = _HwL2mcChnlDenyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1, 1)
)
hwL2mcChnlDenyCfgEntry.setIndexNames(
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlDenyCfgVlanIndex"),
    (0, "HUAWEI-L2MULTICAST-MIB", "hwChnlDenyCfgVsiName"),
)
if mibBuilder.loadTexts:
    hwL2mcChnlDenyCfgEntry.setStatus("current")
_HwChnlDenyCfgVlanIndex_Type = VlanIdOrAny
_HwChnlDenyCfgVlanIndex_Object = MibTableColumn
hwChnlDenyCfgVlanIndex = _HwChnlDenyCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1, 1, 1),
    _HwChnlDenyCfgVlanIndex_Type()
)
hwChnlDenyCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlDenyCfgVlanIndex.setStatus("current")


class _HwChnlDenyCfgVsiName_Type(DisplayString):
    """Custom type hwChnlDenyCfgVsiName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwChnlDenyCfgVsiName_Type.__name__ = "DisplayString"
_HwChnlDenyCfgVsiName_Object = MibTableColumn
hwChnlDenyCfgVsiName = _HwChnlDenyCfgVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1, 1, 2),
    _HwChnlDenyCfgVsiName_Type()
)
hwChnlDenyCfgVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwChnlDenyCfgVsiName.setStatus("current")


class _HwChnlDenyCfg_Type(Integer32):
    """Custom type hwChnlDenyCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_HwChnlDenyCfg_Type.__name__ = "Integer32"
_HwChnlDenyCfg_Object = MibTableColumn
hwChnlDenyCfg = _HwChnlDenyCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1, 1, 3),
    _HwChnlDenyCfg_Type()
)
hwChnlDenyCfg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlDenyCfg.setStatus("current")
_HwChnlDenyCfgRowStatus_Type = RowStatus
_HwChnlDenyCfgRowStatus_Object = MibTableColumn
hwChnlDenyCfgRowStatus = _HwChnlDenyCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 1, 17, 1, 1, 100),
    _HwChnlDenyCfgRowStatus_Type()
)
hwChnlDenyCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwChnlDenyCfgRowStatus.setStatus("current")
_HwL2mcMibConformance_ObjectIdentity = ObjectIdentity
hwL2mcMibConformance = _HwL2mcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100)
)
_HwL2mcMibCompliances_ObjectIdentity = ObjectIdentity
hwL2mcMibCompliances = _HwL2mcMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 1)
)
_HwL2mcMibGroups_ObjectIdentity = ObjectIdentity
hwL2mcMibGroups = _HwL2mcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2)
)

# Managed Objects groups

hwIgspSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 1)
)
hwIgspSystemInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwIgmpSnoopingEnabled"),
        ("HUAWEI-L2MULTICAST-MIB", "hwSendQueryEnabled"),
        ("HUAWEI-L2MULTICAST-MIB", "hwSendQuerySourceIpAddr"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcCacTrapInterval"))
)
if mibBuilder.loadTexts:
    hwIgspSystemInfoGroup.setStatus("current")

hwL2mcCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 2)
)
hwL2mcCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcEnabled"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterAgingTime"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcMaxQueryRespTime"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLastMemQueryInterval"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcQueryInterval"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRobustCount"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcCheckRouterAlert"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSendRouterAlert"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcIgmpVersion"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdMode"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcPromptLeaveEnable"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcPromptLeaveAclNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortLearningEnable"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcReportSuppressEnable"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcIgmpQuerierEnable"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcIgmpSsmMappingEnable"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmAclNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcCfgInfoGroup.setStatus("current")

hwL2mcStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 3)
)
hwL2mcStatisticsInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV1ReportNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV2ReportNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV3ReportNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpLeaveNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV1QueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV2QueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvIgmpV3QueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRecvPimHelloNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSendQueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSendQuerySourceNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcProxyGenQueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcProxyGroupQueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcProxyGroupSourceQueryNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcIgmpPacketClearStats"))
)
if mibBuilder.loadTexts:
    hwL2mcStatisticsInfoGroup.setStatus("current")

hwL2mcFwdInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 4)
)
hwL2mcFwdInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdAddressType"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdHostFlag1"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdHostFlag2"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdHostFlag3"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFwdHostFlag4"))
)
if mibBuilder.loadTexts:
    hwL2mcFwdInfoGroup.setStatus("current")

hwL2mcGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 5)
)
hwL2mcGroupInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcSourceUpTime"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSourceExpires"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupUpTime"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupExpires"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupFilterFlag"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupHostFlag1"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupHostFlag2"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcGroupInfoGroup.setStatus("current")

hwL2mcGroupCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 6)
)
hwL2mcGroupCfgInfoGroup.setObjects(
    ("HUAWEI-L2MULTICAST-MIB", "hwGroupCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwL2mcGroupCfgInfoGroup.setStatus("current")

hwL2mcSsmSourceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 7)
)
hwL2mcSsmSourceInfoGroup.setObjects(
    ("HUAWEI-L2MULTICAST-MIB", "hwL2mcSsmSourceRowStatus")
)
if mibBuilder.loadTexts:
    hwL2mcSsmSourceInfoGroup.setStatus("current")

hwL2mcPortGroupPolicyCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 8)
)
hwL2mcPortGroupPolicyCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyAclNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyIgmpVersion"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortGroupPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcPortGroupPolicyCfgInfoGroup.setStatus("current")

hwL2mcChnlCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 9)
)
hwL2mcChnlCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwChnlCfgChnlType"),
        ("HUAWEI-L2MULTICAST-MIB", "hwChnlCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcChnlCfgInfoGroup.setStatus("current")

hwL2mcLimitInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 10)
)
hwL2mcLimitInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitMaxEntry"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitEntryCnt"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitMaxBandWidth"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitBandWidth"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitAcl"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcLimitCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcLimitInfoGroup.setStatus("current")

hwL2mcPortLimitInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 11)
)
hwL2mcPortLimitInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwPortLimitAcl"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortLimitMaxEntry"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortLimitEntryCnt"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortLimitMaxBandWidth"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortLimitBandWidth"),
        ("HUAWEI-L2MULTICAST-MIB", "hwPortLimitCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcPortLimitInfoGroup.setStatus("current")

hwL2mcFastChnlCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 12)
)
hwL2mcFastChnlCfgInfoGroup.setObjects(
    ("HUAWEI-L2MULTICAST-MIB", "hwL2mcFastChnlCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwL2mcFastChnlCfgInfoGroup.setStatus("current")

hwL2mcRouterPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 13)
)
hwL2mcRouterPortInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortGroupUpTime"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortGroupExpires"),
        ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortGroupHostFlag1"))
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortInfoGroup.setStatus("current")

hwL2mcRouterPortCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 14)
)
hwL2mcRouterPortCfgInfoGroup.setObjects(
    ("HUAWEI-L2MULTICAST-MIB", "hwL2mcRouterPortCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwL2mcRouterPortCfgInfoGroup.setStatus("current")

hwL2mcChnlGroupCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 15)
)
hwL2mcChnlGroupCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgPerBand"),
        ("HUAWEI-L2MULTICAST-MIB", "hwChnlGroupCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcChnlGroupCfgInfoGroup.setStatus("current")

hwL2mcGroupPolicyCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 16)
)
hwL2mcGroupPolicyCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwGroupPolicyAclNum"),
        ("HUAWEI-L2MULTICAST-MIB", "hwGroupPolicyIgmpVersion"),
        ("HUAWEI-L2MULTICAST-MIB", "hwGroupPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcGroupPolicyCfgInfoGroup.setStatus("current")

hwL2mcChnlDenyCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 2, 17)
)
hwL2mcChnlDenyCfgInfoGroup.setObjects(
      *(("HUAWEI-L2MULTICAST-MIB", "hwChnlDenyCfg"),
        ("HUAWEI-L2MULTICAST-MIB", "hwChnlDenyCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2mcChnlDenyCfgInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwIgspMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 181, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwIgspMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2MULTICAST-MIB",
    **{"HWPortType": HWPortType,
       "hwL2MultiCastMIB": hwL2MultiCastMIB,
       "hwIgspMibObject": hwIgspMibObject,
       "hwIgspSystemInfo": hwIgspSystemInfo,
       "hwIgmpSnoopingEnabled": hwIgmpSnoopingEnabled,
       "hwSendQueryEnabled": hwSendQueryEnabled,
       "hwSendQuerySourceIpAddr": hwSendQuerySourceIpAddr,
       "hwL2mcCacTrapInterval": hwL2mcCacTrapInterval,
       "hwL2mcCfgInfo": hwL2mcCfgInfo,
       "hwL2mcCfgTable": hwL2mcCfgTable,
       "hwL2mcCfgEntry": hwL2mcCfgEntry,
       "hwL2mcVlanIndex": hwL2mcVlanIndex,
       "hwL2mcVsiName": hwL2mcVsiName,
       "hwL2mcEnabled": hwL2mcEnabled,
       "hwL2mcRouterAgingTime": hwL2mcRouterAgingTime,
       "hwL2mcMaxQueryRespTime": hwL2mcMaxQueryRespTime,
       "hwL2mcLastMemQueryInterval": hwL2mcLastMemQueryInterval,
       "hwL2mcQueryInterval": hwL2mcQueryInterval,
       "hwL2mcRobustCount": hwL2mcRobustCount,
       "hwL2mcCheckRouterAlert": hwL2mcCheckRouterAlert,
       "hwL2mcSendRouterAlert": hwL2mcSendRouterAlert,
       "hwL2mcIgmpVersion": hwL2mcIgmpVersion,
       "hwL2mcFwdMode": hwL2mcFwdMode,
       "hwL2mcPromptLeaveEnable": hwL2mcPromptLeaveEnable,
       "hwL2mcPromptLeaveAclNum": hwL2mcPromptLeaveAclNum,
       "hwL2mcRouterPortLearningEnable": hwL2mcRouterPortLearningEnable,
       "hwL2mcReportSuppressEnable": hwL2mcReportSuppressEnable,
       "hwL2mcIgmpQuerierEnable": hwL2mcIgmpQuerierEnable,
       "hwL2mcIgmpSsmMappingEnable": hwL2mcIgmpSsmMappingEnable,
       "hwL2mcSsmAclNum": hwL2mcSsmAclNum,
       "hwL2mcRowStatus": hwL2mcRowStatus,
       "hwL2mcStatisticsInfo": hwL2mcStatisticsInfo,
       "hwL2mcStatisticsTable": hwL2mcStatisticsTable,
       "hwL2mcStatisticsEntry": hwL2mcStatisticsEntry,
       "hwL2mcStatsVlanIndex": hwL2mcStatsVlanIndex,
       "hwL2mcStatsVsiName": hwL2mcStatsVsiName,
       "hwL2mcRecvIgmpV1ReportNum": hwL2mcRecvIgmpV1ReportNum,
       "hwL2mcRecvIgmpV2ReportNum": hwL2mcRecvIgmpV2ReportNum,
       "hwL2mcRecvIgmpV3ReportNum": hwL2mcRecvIgmpV3ReportNum,
       "hwL2mcRecvIgmpLeaveNum": hwL2mcRecvIgmpLeaveNum,
       "hwL2mcRecvIgmpV1QueryNum": hwL2mcRecvIgmpV1QueryNum,
       "hwL2mcRecvIgmpV2QueryNum": hwL2mcRecvIgmpV2QueryNum,
       "hwL2mcRecvIgmpV3QueryNum": hwL2mcRecvIgmpV3QueryNum,
       "hwL2mcRecvPimHelloNum": hwL2mcRecvPimHelloNum,
       "hwL2mcSendQueryNum": hwL2mcSendQueryNum,
       "hwL2mcSendQuerySourceNum": hwL2mcSendQuerySourceNum,
       "hwL2mcProxyGenQueryNum": hwL2mcProxyGenQueryNum,
       "hwL2mcProxyGroupQueryNum": hwL2mcProxyGroupQueryNum,
       "hwL2mcProxyGroupSourceQueryNum": hwL2mcProxyGroupSourceQueryNum,
       "hwL2mcIgmpPacketClearStats": hwL2mcIgmpPacketClearStats,
       "hwL2mcFwdInfo": hwL2mcFwdInfo,
       "hwL2mcFwdTable": hwL2mcFwdTable,
       "hwL2mcFwdEntry": hwL2mcFwdEntry,
       "hwL2mcFwdVlanIndex": hwL2mcFwdVlanIndex,
       "hwL2mcFwdVsiName": hwL2mcFwdVsiName,
       "hwL2mcFwdGroupAddress": hwL2mcFwdGroupAddress,
       "hwL2mcFwdSourceAddress": hwL2mcFwdSourceAddress,
       "hwL2mcFwdPortType": hwL2mcFwdPortType,
       "hwL2mcFwdPortIfIndex": hwL2mcFwdPortIfIndex,
       "hwL2mcFwdPortPeId": hwL2mcFwdPortPeId,
       "hwL2mcFwdPortCeId": hwL2mcFwdPortCeId,
       "hwL2mcFwdPeerAddress": hwL2mcFwdPeerAddress,
       "hwL2mcFwdVcOrSiteId": hwL2mcFwdVcOrSiteId,
       "hwL2mcFwdAddressType": hwL2mcFwdAddressType,
       "hwL2mcFwdHostFlag1": hwL2mcFwdHostFlag1,
       "hwL2mcFwdHostFlag2": hwL2mcFwdHostFlag2,
       "hwL2mcFwdHostFlag3": hwL2mcFwdHostFlag3,
       "hwL2mcFwdHostFlag4": hwL2mcFwdHostFlag4,
       "hwL2mcGroupInfo": hwL2mcGroupInfo,
       "hwL2mcGroupInfoTable": hwL2mcGroupInfoTable,
       "hwL2mcGroupInfoEntry": hwL2mcGroupInfoEntry,
       "hwL2mcGroupVlanIndex": hwL2mcGroupVlanIndex,
       "hwL2mcGroupVsiName": hwL2mcGroupVsiName,
       "hwL2mcGroupGroupAddress": hwL2mcGroupGroupAddress,
       "hwL2mcGroupSourceAddress": hwL2mcGroupSourceAddress,
       "hwL2mcPortType": hwL2mcPortType,
       "hwL2mcGroupPortIfIndex": hwL2mcGroupPortIfIndex,
       "hwL2mcGroupPortPeId": hwL2mcGroupPortPeId,
       "hwL2mcGroupPortCeId": hwL2mcGroupPortCeId,
       "hwL2mcGroupPeerAddress": hwL2mcGroupPeerAddress,
       "hwL2mcGroupVcOrSiteId": hwL2mcGroupVcOrSiteId,
       "hwL2mcSourceUpTime": hwL2mcSourceUpTime,
       "hwL2mcSourceExpires": hwL2mcSourceExpires,
       "hwL2mcGroupUpTime": hwL2mcGroupUpTime,
       "hwL2mcGroupExpires": hwL2mcGroupExpires,
       "hwL2mcGroupFilterFlag": hwL2mcGroupFilterFlag,
       "hwL2mcGroupHostFlag1": hwL2mcGroupHostFlag1,
       "hwL2mcGroupHostFlag2": hwL2mcGroupHostFlag2,
       "hwL2mcGroupRowStatus": hwL2mcGroupRowStatus,
       "hwL2mcGroupCfgInfo": hwL2mcGroupCfgInfo,
       "hwL2mcGroupCfgTable": hwL2mcGroupCfgTable,
       "hwL2mcGroupCfgEntry": hwL2mcGroupCfgEntry,
       "hwGroupCfgPortType": hwGroupCfgPortType,
       "hwGroupCfgPortIfIndex": hwGroupCfgPortIfIndex,
       "hwGroupCfgPortPeId": hwGroupCfgPortPeId,
       "hwGroupCfgPortCeId": hwGroupCfgPortCeId,
       "hwGroupCfgPeerAddress": hwGroupCfgPeerAddress,
       "hwGroupCfgVcOrSiteId": hwGroupCfgVcOrSiteId,
       "hwGroupCfgVlanIndex": hwGroupCfgVlanIndex,
       "hwGroupCfgVsiName": hwGroupCfgVsiName,
       "hwGroupCfgGroupAddress": hwGroupCfgGroupAddress,
       "hwGroupCfgSourceAddress": hwGroupCfgSourceAddress,
       "hwGroupCfgRowStatus": hwGroupCfgRowStatus,
       "hwL2mcSsmSourceInfo": hwL2mcSsmSourceInfo,
       "hwL2mcSsmSourceTable": hwL2mcSsmSourceTable,
       "hwL2mcSsmSourceEntry": hwL2mcSsmSourceEntry,
       "hwL2mcSsmSourceVlanIndex": hwL2mcSsmSourceVlanIndex,
       "hwL2mcSsmSourceVsiName": hwL2mcSsmSourceVsiName,
       "hwL2mcSsmGroupAddress": hwL2mcSsmGroupAddress,
       "hwL2mcSsmGroupLen": hwL2mcSsmGroupLen,
       "hwL2mcSsmSourceAddress": hwL2mcSsmSourceAddress,
       "hwL2mcSsmSourceRowStatus": hwL2mcSsmSourceRowStatus,
       "hwL2mcPortGroupPolicyCfgInfo": hwL2mcPortGroupPolicyCfgInfo,
       "hwL2mcPortGroupPolicyCfgTable": hwL2mcPortGroupPolicyCfgTable,
       "hwL2mcPortGroupPolicyCfgEntry": hwL2mcPortGroupPolicyCfgEntry,
       "hwPortGroupPolicyPortType": hwPortGroupPolicyPortType,
       "hwPortGroupPolicyPortIfIndex": hwPortGroupPolicyPortIfIndex,
       "hwPortGroupPolicyPortPeId": hwPortGroupPolicyPortPeId,
       "hwPortGroupPolicyPortCeId": hwPortGroupPolicyPortCeId,
       "hwPortGroupPolicyPeerAddress": hwPortGroupPolicyPeerAddress,
       "hwPortGroupPolicyVcOrSiteId": hwPortGroupPolicyVcOrSiteId,
       "hwPortGroupPolicyVlanIndex": hwPortGroupPolicyVlanIndex,
       "hwPortGroupPolicyVsiName": hwPortGroupPolicyVsiName,
       "hwPortGroupPolicyAclNum": hwPortGroupPolicyAclNum,
       "hwPortGroupPolicyIgmpVersion": hwPortGroupPolicyIgmpVersion,
       "hwPortGroupPolicyRowStatus": hwPortGroupPolicyRowStatus,
       "hwL2mcChnlCfgInfo": hwL2mcChnlCfgInfo,
       "hwL2mcChnlCfgTable": hwL2mcChnlCfgTable,
       "hwL2mcChnlCfgEntry": hwL2mcChnlCfgEntry,
       "hwChnlCfgVlanIndex": hwChnlCfgVlanIndex,
       "hwChnlCfgVsiName": hwChnlCfgVsiName,
       "hwChnlCfgChnlName": hwChnlCfgChnlName,
       "hwChnlCfgChnlType": hwChnlCfgChnlType,
       "hwChnlCfgRowStatus": hwChnlCfgRowStatus,
       "hwL2mcLimitInfo": hwL2mcLimitInfo,
       "hwL2mcLimitTable": hwL2mcLimitTable,
       "hwL2mcLimitEntry": hwL2mcLimitEntry,
       "hwL2mcLimitVlanIndex": hwL2mcLimitVlanIndex,
       "hwL2mcLimitVsiName": hwL2mcLimitVsiName,
       "hwL2mcLimitChnlName": hwL2mcLimitChnlName,
       "hwL2mcLimitMaxEntry": hwL2mcLimitMaxEntry,
       "hwL2mcLimitEntryCnt": hwL2mcLimitEntryCnt,
       "hwL2mcLimitMaxBandWidth": hwL2mcLimitMaxBandWidth,
       "hwL2mcLimitBandWidth": hwL2mcLimitBandWidth,
       "hwL2mcLimitAcl": hwL2mcLimitAcl,
       "hwL2mcLimitCfgRowStatus": hwL2mcLimitCfgRowStatus,
       "hwL2mcPortLimitInfo": hwL2mcPortLimitInfo,
       "hwL2mcPortLimitTable": hwL2mcPortLimitTable,
       "hwL2mcPortLimitEntry": hwL2mcPortLimitEntry,
       "hwPortLimitVlanIndex": hwPortLimitVlanIndex,
       "hwPortLimitVsiName": hwPortLimitVsiName,
       "hwPortLimitPortType": hwPortLimitPortType,
       "hwPortLimitIfIndex": hwPortLimitIfIndex,
       "hwPortLimitPeId": hwPortLimitPeId,
       "hwPortLimitCeId": hwPortLimitCeId,
       "hwPortLimitPeerAddress": hwPortLimitPeerAddress,
       "hwPortLimitVcOrSiteId": hwPortLimitVcOrSiteId,
       "hwPortLimitChnlName": hwPortLimitChnlName,
       "hwPortLimitAcl": hwPortLimitAcl,
       "hwPortLimitMaxEntry": hwPortLimitMaxEntry,
       "hwPortLimitEntryCnt": hwPortLimitEntryCnt,
       "hwPortLimitMaxBandWidth": hwPortLimitMaxBandWidth,
       "hwPortLimitBandWidth": hwPortLimitBandWidth,
       "hwPortLimitCfgRowStatus": hwPortLimitCfgRowStatus,
       "hwL2mcFastChnlCfgInfo": hwL2mcFastChnlCfgInfo,
       "hwL2mcFastChnlCfgTable": hwL2mcFastChnlCfgTable,
       "hwL2mcFastChnlCfgEntry": hwL2mcFastChnlCfgEntry,
       "hwL2mcFastChnlCfgVlanIndex": hwL2mcFastChnlCfgVlanIndex,
       "hwL2mcFastChnlCfgVsiName": hwL2mcFastChnlCfgVsiName,
       "hwL2mcFastChnlCfgGroupAddress": hwL2mcFastChnlCfgGroupAddress,
       "hwL2mcFastChnlCfgGroupLen": hwL2mcFastChnlCfgGroupLen,
       "hwL2mcFastChnlCfgSourceAddress": hwL2mcFastChnlCfgSourceAddress,
       "hwL2mcFastChnlCfgSourceLen": hwL2mcFastChnlCfgSourceLen,
       "hwL2mcFastChnlCfgRowStatus": hwL2mcFastChnlCfgRowStatus,
       "hwL2mcRouterPortInfo": hwL2mcRouterPortInfo,
       "hwL2mcRouterPortInfoTable": hwL2mcRouterPortInfoTable,
       "hwL2mcRouterPortInfoEntry": hwL2mcRouterPortInfoEntry,
       "hwL2mcRouterPortVlanIndex": hwL2mcRouterPortVlanIndex,
       "hwL2mcRouterPortVsiName": hwL2mcRouterPortVsiName,
       "hwL2mcRouterPortType": hwL2mcRouterPortType,
       "hwL2mcRouterPortIfIndex": hwL2mcRouterPortIfIndex,
       "hwL2mcRouterPortPeId": hwL2mcRouterPortPeId,
       "hwL2mcRouterPortCeId": hwL2mcRouterPortCeId,
       "hwL2mcRouterPortPeerAddress": hwL2mcRouterPortPeerAddress,
       "hwL2mcRouterPortVcOrSiteId": hwL2mcRouterPortVcOrSiteId,
       "hwL2mcRouterPortGroupUpTime": hwL2mcRouterPortGroupUpTime,
       "hwL2mcRouterPortGroupExpires": hwL2mcRouterPortGroupExpires,
       "hwL2mcRouterPortGroupHostFlag1": hwL2mcRouterPortGroupHostFlag1,
       "hwL2mcRouterPortCfgInfo": hwL2mcRouterPortCfgInfo,
       "hwL2mcRouterPortCfgTable": hwL2mcRouterPortCfgTable,
       "hwL2mcRouterPortCfgEntry": hwL2mcRouterPortCfgEntry,
       "hwL2mcRouterPortCfgPortType": hwL2mcRouterPortCfgPortType,
       "hwL2mcRouterPortCfgPortIfIndex": hwL2mcRouterPortCfgPortIfIndex,
       "hwL2mcRouterPortCfgPortPeId": hwL2mcRouterPortCfgPortPeId,
       "hwL2mcRouterPortCfgPortCeId": hwL2mcRouterPortCfgPortCeId,
       "hwL2mcRouterPortCfgPeerAddress": hwL2mcRouterPortCfgPeerAddress,
       "hwL2mcRouterPortCfgVcOrSiteId": hwL2mcRouterPortCfgVcOrSiteId,
       "hwL2mcRouterPortCfgVlanIndex": hwL2mcRouterPortCfgVlanIndex,
       "hwL2mcRouterPortCfgVsiName": hwL2mcRouterPortCfgVsiName,
       "hwL2mcRouterPortCfgRowStatus": hwL2mcRouterPortCfgRowStatus,
       "hwL2mcChnlGroupCfgInfo": hwL2mcChnlGroupCfgInfo,
       "hwL2mcChnlGroupCfgTable": hwL2mcChnlGroupCfgTable,
       "hwL2mcChnlGroupCfgEntry": hwL2mcChnlGroupCfgEntry,
       "hwChnlGroupCfgVlanIndex": hwChnlGroupCfgVlanIndex,
       "hwChnlGroupCfgVsiName": hwChnlGroupCfgVsiName,
       "hwChnlCfgGroupChnlName": hwChnlCfgGroupChnlName,
       "hwChnlGroupCfgGroupAddress": hwChnlGroupCfgGroupAddress,
       "hwChnlGroupCfgGroupLen": hwChnlGroupCfgGroupLen,
       "hwChnlGroupCfgSourceAddress": hwChnlGroupCfgSourceAddress,
       "hwChnlGroupCfgSourceLen": hwChnlGroupCfgSourceLen,
       "hwChnlGroupCfgPerBand": hwChnlGroupCfgPerBand,
       "hwChnlGroupCfgRowStatus": hwChnlGroupCfgRowStatus,
       "hwL2mcGroupPolicyCfgInfo": hwL2mcGroupPolicyCfgInfo,
       "hwL2mcGroupPolicyCfgTable": hwL2mcGroupPolicyCfgTable,
       "hwL2mcGroupPolicyCfgEntry": hwL2mcGroupPolicyCfgEntry,
       "hwGroupPolicyVlanIndex": hwGroupPolicyVlanIndex,
       "hwGroupPolicyVsiName": hwGroupPolicyVsiName,
       "hwGroupPolicyAclNum": hwGroupPolicyAclNum,
       "hwGroupPolicyIgmpVersion": hwGroupPolicyIgmpVersion,
       "hwGroupPolicyRowStatus": hwGroupPolicyRowStatus,
       "hwL2mcChnlDenyCfgInfo": hwL2mcChnlDenyCfgInfo,
       "hwL2mcChnlDenyCfgTable": hwL2mcChnlDenyCfgTable,
       "hwL2mcChnlDenyCfgEntry": hwL2mcChnlDenyCfgEntry,
       "hwChnlDenyCfgVlanIndex": hwChnlDenyCfgVlanIndex,
       "hwChnlDenyCfgVsiName": hwChnlDenyCfgVsiName,
       "hwChnlDenyCfg": hwChnlDenyCfg,
       "hwChnlDenyCfgRowStatus": hwChnlDenyCfgRowStatus,
       "hwL2mcMibConformance": hwL2mcMibConformance,
       "hwL2mcMibCompliances": hwL2mcMibCompliances,
       "hwIgspMibCompliance": hwIgspMibCompliance,
       "hwL2mcMibGroups": hwL2mcMibGroups,
       "hwIgspSystemInfoGroup": hwIgspSystemInfoGroup,
       "hwL2mcCfgInfoGroup": hwL2mcCfgInfoGroup,
       "hwL2mcStatisticsInfoGroup": hwL2mcStatisticsInfoGroup,
       "hwL2mcFwdInfoGroup": hwL2mcFwdInfoGroup,
       "hwL2mcGroupInfoGroup": hwL2mcGroupInfoGroup,
       "hwL2mcGroupCfgInfoGroup": hwL2mcGroupCfgInfoGroup,
       "hwL2mcSsmSourceInfoGroup": hwL2mcSsmSourceInfoGroup,
       "hwL2mcPortGroupPolicyCfgInfoGroup": hwL2mcPortGroupPolicyCfgInfoGroup,
       "hwL2mcChnlCfgInfoGroup": hwL2mcChnlCfgInfoGroup,
       "hwL2mcLimitInfoGroup": hwL2mcLimitInfoGroup,
       "hwL2mcPortLimitInfoGroup": hwL2mcPortLimitInfoGroup,
       "hwL2mcFastChnlCfgInfoGroup": hwL2mcFastChnlCfgInfoGroup,
       "hwL2mcRouterPortInfoGroup": hwL2mcRouterPortInfoGroup,
       "hwL2mcRouterPortCfgInfoGroup": hwL2mcRouterPortCfgInfoGroup,
       "hwL2mcChnlGroupCfgInfoGroup": hwL2mcChnlGroupCfgInfoGroup,
       "hwL2mcGroupPolicyCfgInfoGroup": hwL2mcGroupPolicyCfgInfoGroup,
       "hwL2mcChnlDenyCfgInfoGroup": hwL2mcChnlDenyCfgInfoGroup}
)
