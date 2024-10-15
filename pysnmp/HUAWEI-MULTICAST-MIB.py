# SNMP MIB module (HUAWEI-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:17 2024
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

(hwL2VlanDescr,
 hwL2VlanIndex) = mibBuilder.importSymbols(
    "HUAWEI-L2VLAN-MIB",
    "hwL2VlanDescr",
    "hwL2VlanIndex")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(Ipv6Address,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6IfIndexOrZero")

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

hwMultiCastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



class VlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class VlanIndexOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class PortFlag(Integer32, TextualConvention):
    status = "current"
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
        *(("dynamic", 1),
          ("none", 0),
          ("static", 2),
          ("staticANDdynamic", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HwIGSPMibObject_ObjectIdentity = ObjectIdentity
hwIGSPMibObject = _HwIGSPMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1)
)
_HwIGSPSystemInfo_ObjectIdentity = ObjectIdentity
hwIGSPSystemInfo = _HwIGSPSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1)
)
_HwIgmpSnoopingEnabled_Type = EnabledStatus
_HwIgmpSnoopingEnabled_Object = MibScalar
hwIgmpSnoopingEnabled = _HwIgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 1),
    _HwIgmpSnoopingEnabled_Type()
)
hwIgmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingEnabled.setStatus("current")


class _HwSsmPolicyAclNum_Type(Integer32):
    """Custom type hwSsmPolicyAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 2999),
    )


_HwSsmPolicyAclNum_Type.__name__ = "Integer32"
_HwSsmPolicyAclNum_Object = MibScalar
hwSsmPolicyAclNum = _HwSsmPolicyAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 2),
    _HwSsmPolicyAclNum_Type()
)
hwSsmPolicyAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSsmPolicyAclNum.setStatus("current")
_HwSendQueryEnabled_Type = EnabledStatus
_HwSendQueryEnabled_Object = MibScalar
hwSendQueryEnabled = _HwSendQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 3),
    _HwSendQueryEnabled_Type()
)
hwSendQueryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSendQueryEnabled.setStatus("current")
_HwSendQuerySourceIpAddr_Type = IpAddress
_HwSendQuerySourceIpAddr_Object = MibScalar
hwSendQuerySourceIpAddr = _HwSendQuerySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 4),
    _HwSendQuerySourceIpAddr_Type()
)
hwSendQuerySourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSendQuerySourceIpAddr.setStatus("current")
_HwSnmpTrapEnable_Type = EnabledStatus
_HwSnmpTrapEnable_Object = MibScalar
hwSnmpTrapEnable = _HwSnmpTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 5),
    _HwSnmpTrapEnable_Type()
)
hwSnmpTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnmpTrapEnable.setStatus("current")


class _HwIgmpSnoopingSuppressionTime_Type(Integer32):
    """Custom type hwIgmpSnoopingSuppressionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwIgmpSnoopingSuppressionTime_Type.__name__ = "Integer32"
_HwIgmpSnoopingSuppressionTime_Object = MibScalar
hwIgmpSnoopingSuppressionTime = _HwIgmpSnoopingSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 6),
    _HwIgmpSnoopingSuppressionTime_Type()
)
hwIgmpSnoopingSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingSuppressionTime.setStatus("current")
_HwIgmpProxyEnabled_Type = EnabledStatus
_HwIgmpProxyEnabled_Object = MibScalar
hwIgmpProxyEnabled = _HwIgmpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 7),
    _HwIgmpProxyEnabled_Type()
)
hwIgmpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpProxyEnabled.setStatus("current")
_HwIgmpSnoopingProxyEnabled_Type = EnabledStatus
_HwIgmpSnoopingProxyEnabled_Object = MibScalar
hwIgmpSnoopingProxyEnabled = _HwIgmpSnoopingProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 1, 8),
    _HwIgmpSnoopingProxyEnabled_Type()
)
hwIgmpSnoopingProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIgmpSnoopingProxyEnabled.setStatus("current")
_HwVlanCfgInfo_ObjectIdentity = ObjectIdentity
hwVlanCfgInfo = _HwVlanCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2)
)
_HwVlanCfgTable_Object = MibTable
hwVlanCfgTable = _HwVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwVlanCfgTable.setStatus("current")
_HwVlanCfgEntry_Object = MibTableRow
hwVlanCfgEntry = _HwVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1)
)
hwVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwVlanIndex"),
)
if mibBuilder.loadTexts:
    hwVlanCfgEntry.setStatus("current")
_HwVlanIndex_Type = VlanIndex
_HwVlanIndex_Object = MibTableColumn
hwVlanIndex = _HwVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 1),
    _HwVlanIndex_Type()
)
hwVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanIndex.setStatus("current")
_HwVlanIgmpSnoopingEnabled_Type = EnabledStatus
_HwVlanIgmpSnoopingEnabled_Object = MibTableColumn
hwVlanIgmpSnoopingEnabled = _HwVlanIgmpSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 2),
    _HwVlanIgmpSnoopingEnabled_Type()
)
hwVlanIgmpSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpSnoopingEnabled.setStatus("current")


class _HwVlanRouterAgingTime_Type(Integer32):
    """Custom type hwVlanRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwVlanRouterAgingTime_Type.__name__ = "Integer32"
_HwVlanRouterAgingTime_Object = MibTableColumn
hwVlanRouterAgingTime = _HwVlanRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 3),
    _HwVlanRouterAgingTime_Type()
)
hwVlanRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanRouterAgingTime.setStatus("current")


class _HwVlanMaxQueryRespTime_Type(Integer32):
    """Custom type hwVlanMaxQueryRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwVlanMaxQueryRespTime_Type.__name__ = "Integer32"
_HwVlanMaxQueryRespTime_Object = MibTableColumn
hwVlanMaxQueryRespTime = _HwVlanMaxQueryRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 4),
    _HwVlanMaxQueryRespTime_Type()
)
hwVlanMaxQueryRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMaxQueryRespTime.setStatus("current")


class _HwVlanLastMemQueryInt_Type(Integer32):
    """Custom type hwVlanLastMemQueryInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwVlanLastMemQueryInt_Type.__name__ = "Integer32"
_HwVlanLastMemQueryInt_Object = MibTableColumn
hwVlanLastMemQueryInt = _HwVlanLastMemQueryInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 5),
    _HwVlanLastMemQueryInt_Type()
)
hwVlanLastMemQueryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanLastMemQueryInt.setStatus("current")


class _HwVlanQueryInt_Type(Integer32):
    """Custom type hwVlanQueryInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwVlanQueryInt_Type.__name__ = "Integer32"
_HwVlanQueryInt_Object = MibTableColumn
hwVlanQueryInt = _HwVlanQueryInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 6),
    _HwVlanQueryInt_Type()
)
hwVlanQueryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanQueryInt.setStatus("current")


class _HwVlanRobustCount_Type(Integer32):
    """Custom type hwVlanRobustCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_HwVlanRobustCount_Type.__name__ = "Integer32"
_HwVlanRobustCount_Object = MibTableColumn
hwVlanRobustCount = _HwVlanRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 7),
    _HwVlanRobustCount_Type()
)
hwVlanRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanRobustCount.setStatus("current")


class _HwVlanCheckRouterAlert_Type(TruthValue):
    """Custom type hwVlanCheckRouterAlert based on TruthValue"""


_HwVlanCheckRouterAlert_Object = MibTableColumn
hwVlanCheckRouterAlert = _HwVlanCheckRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 8),
    _HwVlanCheckRouterAlert_Type()
)
hwVlanCheckRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanCheckRouterAlert.setStatus("current")


class _HwVlanSendRouterAlert_Type(TruthValue):
    """Custom type hwVlanSendRouterAlert based on TruthValue"""


_HwVlanSendRouterAlert_Object = MibTableColumn
hwVlanSendRouterAlert = _HwVlanSendRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 9),
    _HwVlanSendRouterAlert_Type()
)
hwVlanSendRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanSendRouterAlert.setStatus("current")


class _HwVlanIgmpVersion_Type(Integer32):
    """Custom type hwVlanIgmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("igmpV1", 1),
          ("igmpV2", 2),
          ("igmpV3", 3))
    )


_HwVlanIgmpVersion_Type.__name__ = "Integer32"
_HwVlanIgmpVersion_Object = MibTableColumn
hwVlanIgmpVersion = _HwVlanIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 10),
    _HwVlanIgmpVersion_Type()
)
hwVlanIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpVersion.setStatus("current")
_HwVlanPromptLeaveEnable_Type = EnabledStatus
_HwVlanPromptLeaveEnable_Object = MibTableColumn
hwVlanPromptLeaveEnable = _HwVlanPromptLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 11),
    _HwVlanPromptLeaveEnable_Type()
)
hwVlanPromptLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPromptLeaveEnable.setStatus("current")


class _HwVlanPromptLeaveAclNum_Type(Integer32):
    """Custom type hwVlanPromptLeaveAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 3999),
    )


_HwVlanPromptLeaveAclNum_Type.__name__ = "Integer32"
_HwVlanPromptLeaveAclNum_Object = MibTableColumn
hwVlanPromptLeaveAclNum = _HwVlanPromptLeaveAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 12),
    _HwVlanPromptLeaveAclNum_Type()
)
hwVlanPromptLeaveAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanPromptLeaveAclNum.setStatus("current")
_HwVlanDropUnknown_Type = EnabledStatus
_HwVlanDropUnknown_Object = MibTableColumn
hwVlanDropUnknown = _HwVlanDropUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 13),
    _HwVlanDropUnknown_Type()
)
hwVlanDropUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanDropUnknown.setStatus("current")
_HwVlanLimitAction_Type = EnabledStatus
_HwVlanLimitAction_Object = MibTableColumn
hwVlanLimitAction = _HwVlanLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 1, 1, 14),
    _HwVlanLimitAction_Type()
)
hwVlanLimitAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanLimitAction.setStatus("current")
_HwVlanIgmpProxyTable_Object = MibTable
hwVlanIgmpProxyTable = _HwVlanIgmpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwVlanIgmpProxyTable.setStatus("current")
_HwVlanIgmpProxyEntry_Object = MibTableRow
hwVlanIgmpProxyEntry = _HwVlanIgmpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1)
)
hwVlanIgmpProxyEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwVlanIgmpProxyIndex"),
)
if mibBuilder.loadTexts:
    hwVlanIgmpProxyEntry.setStatus("current")
_HwVlanIgmpProxyIndex_Type = VlanIndex
_HwVlanIgmpProxyIndex_Object = MibTableColumn
hwVlanIgmpProxyIndex = _HwVlanIgmpProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 1),
    _HwVlanIgmpProxyIndex_Type()
)
hwVlanIgmpProxyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanIgmpProxyIndex.setStatus("current")


class _HwVlanIgmpProxyEnabled_Type(EnabledStatus):
    """Custom type hwVlanIgmpProxyEnabled based on EnabledStatus"""
    defaultValue = 2


_HwVlanIgmpProxyEnabled_Object = MibTableColumn
hwVlanIgmpProxyEnabled = _HwVlanIgmpProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 2),
    _HwVlanIgmpProxyEnabled_Type()
)
hwVlanIgmpProxyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpProxyEnabled.setStatus("current")


class _HwVlanQueryInterval_Type(Integer32):
    """Custom type hwVlanQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwVlanQueryInterval_Type.__name__ = "Integer32"
_HwVlanQueryInterval_Object = MibTableColumn
hwVlanQueryInterval = _HwVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 3),
    _HwVlanQueryInterval_Type()
)
hwVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanQueryInterval.setStatus("current")


class _HwVlanMaxResponseTime_Type(Integer32):
    """Custom type hwVlanMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwVlanMaxResponseTime_Type.__name__ = "Integer32"
_HwVlanMaxResponseTime_Object = MibTableColumn
hwVlanMaxResponseTime = _HwVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 4),
    _HwVlanMaxResponseTime_Type()
)
hwVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMaxResponseTime.setStatus("current")


class _HwVlanLastMemQueryInterval_Type(Integer32):
    """Custom type hwVlanLastMemQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwVlanLastMemQueryInterval_Type.__name__ = "Integer32"
_HwVlanLastMemQueryInterval_Object = MibTableColumn
hwVlanLastMemQueryInterval = _HwVlanLastMemQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 5),
    _HwVlanLastMemQueryInterval_Type()
)
hwVlanLastMemQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanLastMemQueryInterval.setStatus("current")


class _HwVlanIgmpRouterAgingTime_Type(Integer32):
    """Custom type hwVlanIgmpRouterAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwVlanIgmpRouterAgingTime_Type.__name__ = "Integer32"
_HwVlanIgmpRouterAgingTime_Object = MibTableColumn
hwVlanIgmpRouterAgingTime = _HwVlanIgmpRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 6),
    _HwVlanIgmpRouterAgingTime_Type()
)
hwVlanIgmpRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpRouterAgingTime.setStatus("current")


class _HwVlanMaxIgmpVersion_Type(Integer32):
    """Custom type hwVlanMaxIgmpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwVlanMaxIgmpVersion_Type.__name__ = "Integer32"
_HwVlanMaxIgmpVersion_Object = MibTableColumn
hwVlanMaxIgmpVersion = _HwVlanMaxIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 7),
    _HwVlanMaxIgmpVersion_Type()
)
hwVlanMaxIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMaxIgmpVersion.setStatus("current")


class _HwVlanIgmpRobustCount_Type(Integer32):
    """Custom type hwVlanIgmpRobustCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_HwVlanIgmpRobustCount_Type.__name__ = "Integer32"
_HwVlanIgmpRobustCount_Object = MibTableColumn
hwVlanIgmpRobustCount = _HwVlanIgmpRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 8),
    _HwVlanIgmpRobustCount_Type()
)
hwVlanIgmpRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpRobustCount.setStatus("current")


class _HwVlanRequireRouterAlert_Type(TruthValue):
    """Custom type hwVlanRequireRouterAlert based on TruthValue"""
    defaultValue = 1


_HwVlanRequireRouterAlert_Object = MibTableColumn
hwVlanRequireRouterAlert = _HwVlanRequireRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 9),
    _HwVlanRequireRouterAlert_Type()
)
hwVlanRequireRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanRequireRouterAlert.setStatus("current")


class _HwVlanIgmpSendRouterAlert_Type(TruthValue):
    """Custom type hwVlanIgmpSendRouterAlert based on TruthValue"""
    defaultValue = 1


_HwVlanIgmpSendRouterAlert_Object = MibTableColumn
hwVlanIgmpSendRouterAlert = _HwVlanIgmpSendRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 10),
    _HwVlanIgmpSendRouterAlert_Type()
)
hwVlanIgmpSendRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpSendRouterAlert.setStatus("current")


class _HwVlanIgmpPromptLeaveEnable_Type(EnabledStatus):
    """Custom type hwVlanIgmpPromptLeaveEnable based on EnabledStatus"""
    defaultValue = 2


_HwVlanIgmpPromptLeaveEnable_Object = MibTableColumn
hwVlanIgmpPromptLeaveEnable = _HwVlanIgmpPromptLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 2, 1, 11),
    _HwVlanIgmpPromptLeaveEnable_Type()
)
hwVlanIgmpPromptLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIgmpPromptLeaveEnable.setStatus("current")
_HwL2McastVlanCfgTable_Object = MibTable
hwL2McastVlanCfgTable = _HwL2McastVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwL2McastVlanCfgTable.setStatus("current")
_HwL2McastVlanCfgEntry_Object = MibTableRow
hwL2McastVlanCfgEntry = _HwL2McastVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 3, 1)
)
hwL2McastVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwL2McastVlanIndex"),
)
if mibBuilder.loadTexts:
    hwL2McastVlanCfgEntry.setStatus("current")
_HwL2McastVlanIndex_Type = VlanIndex
_HwL2McastVlanIndex_Object = MibTableColumn
hwL2McastVlanIndex = _HwL2McastVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 3, 1, 1),
    _HwL2McastVlanIndex_Type()
)
hwL2McastVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2McastVlanIndex.setStatus("current")


class _HwVlanL2FlowTriggerEnabled_Type(EnabledStatus):
    """Custom type hwVlanL2FlowTriggerEnabled based on EnabledStatus"""
    defaultValue = 2


_HwVlanL2FlowTriggerEnabled_Object = MibTableColumn
hwVlanL2FlowTriggerEnabled = _HwVlanL2FlowTriggerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 3, 1, 2),
    _HwVlanL2FlowTriggerEnabled_Type()
)
hwVlanL2FlowTriggerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanL2FlowTriggerEnabled.setStatus("current")
_HwVlanL2StaticFlow_Type = IpAddress
_HwVlanL2StaticFlow_Object = MibTableColumn
hwVlanL2StaticFlow = _HwVlanL2StaticFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 2, 3, 1, 3),
    _HwVlanL2StaticFlow_Type()
)
hwVlanL2StaticFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanL2StaticFlow.setStatus("current")
_HwStatisticsInfo_ObjectIdentity = ObjectIdentity
hwStatisticsInfo = _HwStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3)
)
_HwSystemStatisticsInfo_ObjectIdentity = ObjectIdentity
hwSystemStatisticsInfo = _HwSystemStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1)
)
_HwSystemRecvVlanUpEventTimes_Type = Counter32
_HwSystemRecvVlanUpEventTimes_Object = MibScalar
hwSystemRecvVlanUpEventTimes = _HwSystemRecvVlanUpEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 1),
    _HwSystemRecvVlanUpEventTimes_Type()
)
hwSystemRecvVlanUpEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvVlanUpEventTimes.setStatus("current")
_HwSystemRecvVlanDownEventTimes_Type = Counter32
_HwSystemRecvVlanDownEventTimes_Object = MibScalar
hwSystemRecvVlanDownEventTimes = _HwSystemRecvVlanDownEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 2),
    _HwSystemRecvVlanDownEventTimes_Type()
)
hwSystemRecvVlanDownEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvVlanDownEventTimes.setStatus("current")
_HwSystemRecvVlanDelEventTimes_Type = Counter32
_HwSystemRecvVlanDelEventTimes_Object = MibScalar
hwSystemRecvVlanDelEventTimes = _HwSystemRecvVlanDelEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 3),
    _HwSystemRecvVlanDelEventTimes_Type()
)
hwSystemRecvVlanDelEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvVlanDelEventTimes.setStatus("current")
_HwSystemRecvPortUpEventTimes_Type = Counter32
_HwSystemRecvPortUpEventTimes_Object = MibScalar
hwSystemRecvPortUpEventTimes = _HwSystemRecvPortUpEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 4),
    _HwSystemRecvPortUpEventTimes_Type()
)
hwSystemRecvPortUpEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvPortUpEventTimes.setStatus("current")
_HwSystemRecvPortDownEventTimes_Type = Counter32
_HwSystemRecvPortDownEventTimes_Object = MibScalar
hwSystemRecvPortDownEventTimes = _HwSystemRecvPortDownEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 5),
    _HwSystemRecvPortDownEventTimes_Type()
)
hwSystemRecvPortDownEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvPortDownEventTimes.setStatus("current")
_HwSystemRecvPortDelEventTimes_Type = Counter32
_HwSystemRecvPortDelEventTimes_Object = MibScalar
hwSystemRecvPortDelEventTimes = _HwSystemRecvPortDelEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 6),
    _HwSystemRecvPortDelEventTimes_Type()
)
hwSystemRecvPortDelEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvPortDelEventTimes.setStatus("current")
_HwSystemRecvPortIncEventTimes_Type = Counter32
_HwSystemRecvPortIncEventTimes_Object = MibScalar
hwSystemRecvPortIncEventTimes = _HwSystemRecvPortIncEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 7),
    _HwSystemRecvPortIncEventTimes_Type()
)
hwSystemRecvPortIncEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvPortIncEventTimes.setStatus("current")
_HwSystemRecvPortExcEventTimes_Type = Counter32
_HwSystemRecvPortExcEventTimes_Object = MibScalar
hwSystemRecvPortExcEventTimes = _HwSystemRecvPortExcEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 8),
    _HwSystemRecvPortExcEventTimes_Type()
)
hwSystemRecvPortExcEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvPortExcEventTimes.setStatus("current")
_HwSystemRecvMSTPBlockEventTimes_Type = Counter32
_HwSystemRecvMSTPBlockEventTimes_Object = MibScalar
hwSystemRecvMSTPBlockEventTimes = _HwSystemRecvMSTPBlockEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 9),
    _HwSystemRecvMSTPBlockEventTimes_Type()
)
hwSystemRecvMSTPBlockEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvMSTPBlockEventTimes.setStatus("current")
_HwSystemRecvMSTPForwardEventTimes_Type = Counter32
_HwSystemRecvMSTPForwardEventTimes_Object = MibScalar
hwSystemRecvMSTPForwardEventTimes = _HwSystemRecvMSTPForwardEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 10),
    _HwSystemRecvMSTPForwardEventTimes_Type()
)
hwSystemRecvMSTPForwardEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvMSTPForwardEventTimes.setStatus("current")
_HwSystemIGMPSysClearStats_Type = TruthValue
_HwSystemIGMPSysClearStats_Object = MibScalar
hwSystemIGMPSysClearStats = _HwSystemIGMPSysClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 11),
    _HwSystemIGMPSysClearStats_Type()
)
hwSystemIGMPSysClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSystemIGMPSysClearStats.setStatus("current")
_HwSystemIGMPPacketClearStats_Type = TruthValue
_HwSystemIGMPPacketClearStats_Object = MibScalar
hwSystemIGMPPacketClearStats = _HwSystemIGMPPacketClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 12),
    _HwSystemIGMPPacketClearStats_Type()
)
hwSystemIGMPPacketClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSystemIGMPPacketClearStats.setStatus("current")
_HwSystemRecvLinkChangeEventTimes_Type = Counter32
_HwSystemRecvLinkChangeEventTimes_Object = MibScalar
hwSystemRecvLinkChangeEventTimes = _HwSystemRecvLinkChangeEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 1, 13),
    _HwSystemRecvLinkChangeEventTimes_Type()
)
hwSystemRecvLinkChangeEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSystemRecvLinkChangeEventTimes.setStatus("current")
_HwVlanStatisticsTable_Object = MibTable
hwVlanStatisticsTable = _HwVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwVlanStatisticsTable.setStatus("current")
_HwVlanStatisticsEntry_Object = MibTableRow
hwVlanStatisticsEntry = _HwVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1)
)
hwVlanStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwVlanStatsVlanIndex"),
)
if mibBuilder.loadTexts:
    hwVlanStatisticsEntry.setStatus("current")
_HwVlanStatsVlanIndex_Type = VlanIndex
_HwVlanStatsVlanIndex_Object = MibTableColumn
hwVlanStatsVlanIndex = _HwVlanStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 1),
    _HwVlanStatsVlanIndex_Type()
)
hwVlanStatsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanStatsVlanIndex.setStatus("current")
_HwVlanRecvIGMPV1ReportNum_Type = Counter32
_HwVlanRecvIGMPV1ReportNum_Object = MibTableColumn
hwVlanRecvIGMPV1ReportNum = _HwVlanRecvIGMPV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 2),
    _HwVlanRecvIGMPV1ReportNum_Type()
)
hwVlanRecvIGMPV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV1ReportNum.setStatus("current")
_HwVlanRecvIGMPV2ReportNum_Type = Counter32
_HwVlanRecvIGMPV2ReportNum_Object = MibTableColumn
hwVlanRecvIGMPV2ReportNum = _HwVlanRecvIGMPV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 3),
    _HwVlanRecvIGMPV2ReportNum_Type()
)
hwVlanRecvIGMPV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV2ReportNum.setStatus("current")
_HwVlanRecvIGMPV3ReportNum_Type = Counter32
_HwVlanRecvIGMPV3ReportNum_Object = MibTableColumn
hwVlanRecvIGMPV3ReportNum = _HwVlanRecvIGMPV3ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 4),
    _HwVlanRecvIGMPV3ReportNum_Type()
)
hwVlanRecvIGMPV3ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV3ReportNum.setStatus("current")
_HwVlanRecvIGMPLeaveNum_Type = Counter32
_HwVlanRecvIGMPLeaveNum_Object = MibTableColumn
hwVlanRecvIGMPLeaveNum = _HwVlanRecvIGMPLeaveNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 5),
    _HwVlanRecvIGMPLeaveNum_Type()
)
hwVlanRecvIGMPLeaveNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPLeaveNum.setStatus("current")
_HwVlanRecvIGMPV1QueryNum_Type = Counter32
_HwVlanRecvIGMPV1QueryNum_Object = MibTableColumn
hwVlanRecvIGMPV1QueryNum = _HwVlanRecvIGMPV1QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 6),
    _HwVlanRecvIGMPV1QueryNum_Type()
)
hwVlanRecvIGMPV1QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV1QueryNum.setStatus("current")
_HwVlanRecvIGMPV2QueryNum_Type = Counter32
_HwVlanRecvIGMPV2QueryNum_Object = MibTableColumn
hwVlanRecvIGMPV2QueryNum = _HwVlanRecvIGMPV2QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 7),
    _HwVlanRecvIGMPV2QueryNum_Type()
)
hwVlanRecvIGMPV2QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV2QueryNum.setStatus("current")
_HwVlanRecvIGMPV3QueryNum_Type = Counter32
_HwVlanRecvIGMPV3QueryNum_Object = MibTableColumn
hwVlanRecvIGMPV3QueryNum = _HwVlanRecvIGMPV3QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 8),
    _HwVlanRecvIGMPV3QueryNum_Type()
)
hwVlanRecvIGMPV3QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIGMPV3QueryNum.setStatus("current")
_HwVlanRecvPimHelloNum_Type = Counter32
_HwVlanRecvPimHelloNum_Object = MibTableColumn
hwVlanRecvPimHelloNum = _HwVlanRecvPimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 9),
    _HwVlanRecvPimHelloNum_Type()
)
hwVlanRecvPimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvPimHelloNum.setStatus("current")
_HwVlanSendQueryNum_Type = Counter32
_HwVlanSendQueryNum_Object = MibTableColumn
hwVlanSendQueryNum = _HwVlanSendQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 10),
    _HwVlanSendQueryNum_Type()
)
hwVlanSendQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSendQueryNum.setStatus("current")
_HwVlanIGMPPacketClearStats_Type = TruthValue
_HwVlanIGMPPacketClearStats_Object = MibTableColumn
hwVlanIGMPPacketClearStats = _HwVlanIGMPPacketClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 11),
    _HwVlanIGMPPacketClearStats_Type()
)
hwVlanIGMPPacketClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanIGMPPacketClearStats.setStatus("current")
_HwVlanSendSourceIPSpecQueryNum_Type = Counter32
_HwVlanSendSourceIPSpecQueryNum_Object = MibTableColumn
hwVlanSendSourceIPSpecQueryNum = _HwVlanSendSourceIPSpecQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 3, 2, 1, 12),
    _HwVlanSendSourceIPSpecQueryNum_Type()
)
hwVlanSendSourceIPSpecQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSendSourceIPSpecQueryNum.setStatus("current")
_HwMCGrpInfo_ObjectIdentity = ObjectIdentity
hwMCGrpInfo = _HwMCGrpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4)
)
_HwIPGrpInfoTable_Object = MibTable
hwIPGrpInfoTable = _HwIPGrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwIPGrpInfoTable.setStatus("current")
_HwIPGrpInfoEntry_Object = MibTableRow
hwIPGrpInfoEntry = _HwIPGrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1)
)
hwIPGrpInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwIPGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwIPGrpPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwIPGrpAddress"),
)
if mibBuilder.loadTexts:
    hwIPGrpInfoEntry.setStatus("current")
_HwIPGrpVlanIndex_Type = VlanIndex
_HwIPGrpVlanIndex_Object = MibTableColumn
hwIPGrpVlanIndex = _HwIPGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 1),
    _HwIPGrpVlanIndex_Type()
)
hwIPGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIPGrpVlanIndex.setStatus("current")
_HwIPGrpPortIfIndex_Type = InterfaceIndex
_HwIPGrpPortIfIndex_Object = MibTableColumn
hwIPGrpPortIfIndex = _HwIPGrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 2),
    _HwIPGrpPortIfIndex_Type()
)
hwIPGrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIPGrpPortIfIndex.setStatus("current")
_HwIPGrpAddress_Type = IpAddress
_HwIPGrpAddress_Object = MibTableColumn
hwIPGrpAddress = _HwIPGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 3),
    _HwIPGrpAddress_Type()
)
hwIPGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIPGrpAddress.setStatus("current")
_HwIPGrpUpTime_Type = Unsigned32
_HwIPGrpUpTime_Object = MibTableColumn
hwIPGrpUpTime = _HwIPGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 4),
    _HwIPGrpUpTime_Type()
)
hwIPGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPGrpUpTime.setStatus("current")
_HwIPHostUpTime_Type = Unsigned32
_HwIPHostUpTime_Object = MibTableColumn
hwIPHostUpTime = _HwIPHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 5),
    _HwIPHostUpTime_Type()
)
hwIPHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPHostUpTime.setStatus("current")
_HwIPHostExpires_Type = Unsigned32
_HwIPHostExpires_Object = MibTableColumn
hwIPHostExpires = _HwIPHostExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 6),
    _HwIPHostExpires_Type()
)
hwIPHostExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPHostExpires.setStatus("current")
_HwIPHostFlags_Type = PortFlag
_HwIPHostFlags_Object = MibTableColumn
hwIPHostFlags = _HwIPHostFlags_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 7),
    _HwIPHostFlags_Type()
)
hwIPHostFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPHostFlags.setStatus("current")
_HwIPRtUPTime_Type = Unsigned32
_HwIPRtUPTime_Object = MibTableColumn
hwIPRtUPTime = _HwIPRtUPTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 8),
    _HwIPRtUPTime_Type()
)
hwIPRtUPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPRtUPTime.setStatus("current")
_HwIPRtExpires_Type = Unsigned32
_HwIPRtExpires_Object = MibTableColumn
hwIPRtExpires = _HwIPRtExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 9),
    _HwIPRtExpires_Type()
)
hwIPRtExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPRtExpires.setStatus("current")
_HwIPRtFlags_Type = PortFlag
_HwIPRtFlags_Object = MibTableColumn
hwIPRtFlags = _HwIPRtFlags_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 1, 1, 10),
    _HwIPRtFlags_Type()
)
hwIPRtFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIPRtFlags.setStatus("current")
_HwMACGrpInfoTable_Object = MibTable
hwMACGrpInfoTable = _HwMACGrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwMACGrpInfoTable.setStatus("current")
_HwMACGrpInfoEntry_Object = MibTableRow
hwMACGrpInfoEntry = _HwMACGrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 2, 1)
)
hwMACGrpInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMACGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMACGrpPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMACGrpAddress"),
)
if mibBuilder.loadTexts:
    hwMACGrpInfoEntry.setStatus("current")
_HwMACGrpVlanIndex_Type = VlanIndex
_HwMACGrpVlanIndex_Object = MibTableColumn
hwMACGrpVlanIndex = _HwMACGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 2, 1, 1),
    _HwMACGrpVlanIndex_Type()
)
hwMACGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACGrpVlanIndex.setStatus("current")
_HwMACGrpPortIfIndex_Type = InterfaceIndex
_HwMACGrpPortIfIndex_Object = MibTableColumn
hwMACGrpPortIfIndex = _HwMACGrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 2, 1, 2),
    _HwMACGrpPortIfIndex_Type()
)
hwMACGrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMACGrpPortIfIndex.setStatus("current")
_HwMACGrpAddress_Type = MacAddress
_HwMACGrpAddress_Object = MibTableColumn
hwMACGrpAddress = _HwMACGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 2, 1, 3),
    _HwMACGrpAddress_Type()
)
hwMACGrpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMACGrpAddress.setStatus("current")
_HwMcastGrpCfgTable_Object = MibTable
hwMcastGrpCfgTable = _HwMcastGrpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hwMcastGrpCfgTable.setStatus("current")
_HwMcastGrpCfgEntry_Object = MibTableRow
hwMcastGrpCfgEntry = _HwMcastGrpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1)
)
hwMcastGrpCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwGrpProfileNameIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwGrpListNameIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwGrpNameIndex"),
)
if mibBuilder.loadTexts:
    hwMcastGrpCfgEntry.setStatus("current")
_HwGrpProfileNameIndex_Type = DisplayString
_HwGrpProfileNameIndex_Object = MibTableColumn
hwGrpProfileNameIndex = _HwGrpProfileNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1, 1),
    _HwGrpProfileNameIndex_Type()
)
hwGrpProfileNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGrpProfileNameIndex.setStatus("current")
_HwGrpListNameIndex_Type = DisplayString
_HwGrpListNameIndex_Object = MibTableColumn
hwGrpListNameIndex = _HwGrpListNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1, 2),
    _HwGrpListNameIndex_Type()
)
hwGrpListNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGrpListNameIndex.setStatus("current")
_HwGrpNameIndex_Type = DisplayString
_HwGrpNameIndex_Object = MibTableColumn
hwGrpNameIndex = _HwGrpNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1, 3),
    _HwGrpNameIndex_Type()
)
hwGrpNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGrpNameIndex.setStatus("current")
_HwGrpIpAddress_Type = IpAddress
_HwGrpIpAddress_Object = MibTableColumn
hwGrpIpAddress = _HwGrpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1, 4),
    _HwGrpIpAddress_Type()
)
hwGrpIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpIpAddress.setStatus("current")
_HwGrpRowStatus_Type = RowStatus
_HwGrpRowStatus_Object = MibTableColumn
hwGrpRowStatus = _HwGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 3, 1, 100),
    _HwGrpRowStatus_Type()
)
hwGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpRowStatus.setStatus("current")
_HwVlanMcastGrpTable_Object = MibTable
hwVlanMcastGrpTable = _HwVlanMcastGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hwVlanMcastGrpTable.setStatus("current")
_HwVlanMcastGrpEntry_Object = MibTableRow
hwVlanMcastGrpEntry = _HwVlanMcastGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 4, 1)
)
hwVlanMcastGrpEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwVlanMcastIndex"),
)
if mibBuilder.loadTexts:
    hwVlanMcastGrpEntry.setStatus("current")
_HwVlanMcastIndex_Type = VlanIndex
_HwVlanMcastIndex_Object = MibTableColumn
hwVlanMcastIndex = _HwVlanMcastIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 4, 1, 1),
    _HwVlanMcastIndex_Type()
)
hwVlanMcastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanMcastIndex.setStatus("current")
_HwVlanMcastProfileName_Type = DisplayString
_HwVlanMcastProfileName_Object = MibTableColumn
hwVlanMcastProfileName = _HwVlanMcastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 4, 1, 2),
    _HwVlanMcastProfileName_Type()
)
hwVlanMcastProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMcastProfileName.setStatus("current")
_HwMcastGrpProfileTable_Object = MibTable
hwMcastGrpProfileTable = _HwMcastGrpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5)
)
if mibBuilder.loadTexts:
    hwMcastGrpProfileTable.setStatus("current")
_HwMcastGrpProfileEntry_Object = MibTableRow
hwMcastGrpProfileEntry = _HwMcastGrpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5, 1)
)
hwMcastGrpProfileEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwVlanMulticastProfileName"),
)
if mibBuilder.loadTexts:
    hwMcastGrpProfileEntry.setStatus("current")
_HwVlanMulticastProfileName_Type = DisplayString
_HwVlanMulticastProfileName_Object = MibTableColumn
hwVlanMulticastProfileName = _HwVlanMulticastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5, 1, 1),
    _HwVlanMulticastProfileName_Type()
)
hwVlanMulticastProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanMulticastProfileName.setStatus("current")


class _HwMulticastProfilePreviewTimes_Type(Integer32):
    """Custom type hwMulticastProfilePreviewTimes based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwMulticastProfilePreviewTimes_Type.__name__ = "Integer32"
_HwMulticastProfilePreviewTimes_Object = MibTableColumn
hwMulticastProfilePreviewTimes = _HwMulticastProfilePreviewTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5, 1, 2),
    _HwMulticastProfilePreviewTimes_Type()
)
hwMulticastProfilePreviewTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastProfilePreviewTimes.setStatus("current")


class _HwMulticastProfilePreviewMinutes_Type(Integer32):
    """Custom type hwMulticastProfilePreviewMinutes based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HwMulticastProfilePreviewMinutes_Type.__name__ = "Integer32"
_HwMulticastProfilePreviewMinutes_Object = MibTableColumn
hwMulticastProfilePreviewMinutes = _HwMulticastProfilePreviewMinutes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5, 1, 3),
    _HwMulticastProfilePreviewMinutes_Type()
)
hwMulticastProfilePreviewMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastProfilePreviewMinutes.setStatus("current")


class _HwMulticastProfilePreviewInterval_Type(Integer32):
    """Custom type hwMulticastProfilePreviewInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_HwMulticastProfilePreviewInterval_Type.__name__ = "Integer32"
_HwMulticastProfilePreviewInterval_Object = MibTableColumn
hwMulticastProfilePreviewInterval = _HwMulticastProfilePreviewInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 5, 1, 4),
    _HwMulticastProfilePreviewInterval_Type()
)
hwMulticastProfilePreviewInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMulticastProfilePreviewInterval.setStatus("current")
_HwExternIpGrpInfoTable_Object = MibTable
hwExternIpGrpInfoTable = _HwExternIpGrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6)
)
if mibBuilder.loadTexts:
    hwExternIpGrpInfoTable.setStatus("current")
_HwExternIpGrpInfoEntry_Object = MibTableRow
hwExternIpGrpInfoEntry = _HwExternIpGrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1)
)
hwExternIpGrpInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwExternIpGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternIpGrpPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternIpGrpAddress"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternIpSourceAddress"),
)
if mibBuilder.loadTexts:
    hwExternIpGrpInfoEntry.setStatus("current")
_HwExternIpGrpVlanIndex_Type = VlanIndex
_HwExternIpGrpVlanIndex_Object = MibTableColumn
hwExternIpGrpVlanIndex = _HwExternIpGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 1),
    _HwExternIpGrpVlanIndex_Type()
)
hwExternIpGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternIpGrpVlanIndex.setStatus("current")
_HwExternIpGrpPortIfIndex_Type = InterfaceIndex
_HwExternIpGrpPortIfIndex_Object = MibTableColumn
hwExternIpGrpPortIfIndex = _HwExternIpGrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 2),
    _HwExternIpGrpPortIfIndex_Type()
)
hwExternIpGrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternIpGrpPortIfIndex.setStatus("current")
_HwExternIpGrpAddress_Type = IpAddress
_HwExternIpGrpAddress_Object = MibTableColumn
hwExternIpGrpAddress = _HwExternIpGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 3),
    _HwExternIpGrpAddress_Type()
)
hwExternIpGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternIpGrpAddress.setStatus("current")
_HwExternIpGrpUpTime_Type = Unsigned32
_HwExternIpGrpUpTime_Object = MibTableColumn
hwExternIpGrpUpTime = _HwExternIpGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 4),
    _HwExternIpGrpUpTime_Type()
)
hwExternIpGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpGrpUpTime.setStatus("current")
_HwExternIpHostUpTime_Type = Unsigned32
_HwExternIpHostUpTime_Object = MibTableColumn
hwExternIpHostUpTime = _HwExternIpHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 5),
    _HwExternIpHostUpTime_Type()
)
hwExternIpHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpHostUpTime.setStatus("current")
_HwExternIpHostExpires_Type = Unsigned32
_HwExternIpHostExpires_Object = MibTableColumn
hwExternIpHostExpires = _HwExternIpHostExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 6),
    _HwExternIpHostExpires_Type()
)
hwExternIpHostExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpHostExpires.setStatus("current")
_HwExternIpHostFlag_Type = PortFlag
_HwExternIpHostFlag_Object = MibTableColumn
hwExternIpHostFlag = _HwExternIpHostFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 7),
    _HwExternIpHostFlag_Type()
)
hwExternIpHostFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpHostFlag.setStatus("current")
_HwExternIpRtUpTime_Type = Unsigned32
_HwExternIpRtUpTime_Object = MibTableColumn
hwExternIpRtUpTime = _HwExternIpRtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 8),
    _HwExternIpRtUpTime_Type()
)
hwExternIpRtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpRtUpTime.setStatus("current")
_HwExternIpRtExpires_Type = Unsigned32
_HwExternIpRtExpires_Object = MibTableColumn
hwExternIpRtExpires = _HwExternIpRtExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 9),
    _HwExternIpRtExpires_Type()
)
hwExternIpRtExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpRtExpires.setStatus("current")
_HwExternIpRtFlag_Type = PortFlag
_HwExternIpRtFlag_Object = MibTableColumn
hwExternIpRtFlag = _HwExternIpRtFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 10),
    _HwExternIpRtFlag_Type()
)
hwExternIpRtFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExternIpRtFlag.setStatus("current")
_HwExternIpSourceAddress_Type = IpAddress
_HwExternIpSourceAddress_Object = MibTableColumn
hwExternIpSourceAddress = _HwExternIpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 4, 6, 1, 11),
    _HwExternIpSourceAddress_Type()
)
hwExternIpSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternIpSourceAddress.setStatus("current")
_HwPortInfo_ObjectIdentity = ObjectIdentity
hwPortInfo = _HwPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5)
)
_HwPortStaticGrpTable_Object = MibTable
hwPortStaticGrpTable = _HwPortStaticGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwPortStaticGrpTable.setStatus("current")
_HwPortStaticGrpEntry_Object = MibTableRow
hwPortStaticGrpEntry = _HwPortStaticGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1, 1)
)
hwPortStaticGrpEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwPortStaticGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwPortStaticGrpIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwPortStaticGrpAddr"),
)
if mibBuilder.loadTexts:
    hwPortStaticGrpEntry.setStatus("current")
_HwPortStaticGrpVlanIndex_Type = VlanIndex
_HwPortStaticGrpVlanIndex_Object = MibTableColumn
hwPortStaticGrpVlanIndex = _HwPortStaticGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1, 1, 1),
    _HwPortStaticGrpVlanIndex_Type()
)
hwPortStaticGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortStaticGrpVlanIndex.setStatus("current")
_HwPortStaticGrpIfIndex_Type = InterfaceIndex
_HwPortStaticGrpIfIndex_Object = MibTableColumn
hwPortStaticGrpIfIndex = _HwPortStaticGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1, 1, 2),
    _HwPortStaticGrpIfIndex_Type()
)
hwPortStaticGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortStaticGrpIfIndex.setStatus("current")
_HwPortStaticGrpAddr_Type = IpAddress
_HwPortStaticGrpAddr_Object = MibTableColumn
hwPortStaticGrpAddr = _HwPortStaticGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1, 1, 3),
    _HwPortStaticGrpAddr_Type()
)
hwPortStaticGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortStaticGrpAddr.setStatus("current")
_HwPortStaticGrpRowStatus_Type = RowStatus
_HwPortStaticGrpRowStatus_Object = MibTableColumn
hwPortStaticGrpRowStatus = _HwPortStaticGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 1, 1, 100),
    _HwPortStaticGrpRowStatus_Type()
)
hwPortStaticGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortStaticGrpRowStatus.setStatus("current")
_HwGrpPolicyCfgTable_Object = MibTable
hwGrpPolicyCfgTable = _HwGrpPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2)
)
if mibBuilder.loadTexts:
    hwGrpPolicyCfgTable.setStatus("current")
_HwGrpPolicyCfgEntry_Object = MibTableRow
hwGrpPolicyCfgEntry = _HwGrpPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2, 1)
)
hwGrpPolicyCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwGrpPolicyVlanIndex"),
)
if mibBuilder.loadTexts:
    hwGrpPolicyCfgEntry.setStatus("current")
_HwGrpPolicyVlanIndex_Type = VlanIndex
_HwGrpPolicyVlanIndex_Object = MibTableColumn
hwGrpPolicyVlanIndex = _HwGrpPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2, 1, 1),
    _HwGrpPolicyVlanIndex_Type()
)
hwGrpPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwGrpPolicyVlanIndex.setStatus("current")
_HwGrpPolicyAclNum_Type = Integer32
_HwGrpPolicyAclNum_Object = MibTableColumn
hwGrpPolicyAclNum = _HwGrpPolicyAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2, 1, 2),
    _HwGrpPolicyAclNum_Type()
)
hwGrpPolicyAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpPolicyAclNum.setStatus("current")


class _HwGrpPolicyIgmpVersion_Type(Integer32):
    """Custom type hwGrpPolicyIgmpVersion based on Integer32"""
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
        *(("igmpV1", 1),
          ("igmpV1V2", 3),
          ("igmpV1V2V3", 5),
          ("igmpV2", 2),
          ("igmpV3", 4))
    )


_HwGrpPolicyIgmpVersion_Type.__name__ = "Integer32"
_HwGrpPolicyIgmpVersion_Object = MibTableColumn
hwGrpPolicyIgmpVersion = _HwGrpPolicyIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2, 1, 3),
    _HwGrpPolicyIgmpVersion_Type()
)
hwGrpPolicyIgmpVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpPolicyIgmpVersion.setStatus("current")
_HwGrpPolicyRowStatus_Type = RowStatus
_HwGrpPolicyRowStatus_Object = MibTableColumn
hwGrpPolicyRowStatus = _HwGrpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 2, 1, 100),
    _HwGrpPolicyRowStatus_Type()
)
hwGrpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpPolicyRowStatus.setStatus("current")
_HwRouterPortInfoTable_Object = MibTable
hwRouterPortInfoTable = _HwRouterPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3)
)
if mibBuilder.loadTexts:
    hwRouterPortInfoTable.setStatus("current")
_HwRouterPortInfoEntry_Object = MibTableRow
hwRouterPortInfoEntry = _HwRouterPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1)
)
hwRouterPortInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwRouterPortVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwRouterPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwRouterPortInfoEntry.setStatus("current")
_HwRouterPortVlanIndex_Type = VlanIndex
_HwRouterPortVlanIndex_Object = MibTableColumn
hwRouterPortVlanIndex = _HwRouterPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1, 1),
    _HwRouterPortVlanIndex_Type()
)
hwRouterPortVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouterPortVlanIndex.setStatus("current")
_HwRouterPortIfIndex_Type = InterfaceIndex
_HwRouterPortIfIndex_Object = MibTableColumn
hwRouterPortIfIndex = _HwRouterPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1, 2),
    _HwRouterPortIfIndex_Type()
)
hwRouterPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouterPortIfIndex.setStatus("current")
_HwRouterPortUpTime_Type = Unsigned32
_HwRouterPortUpTime_Object = MibTableColumn
hwRouterPortUpTime = _HwRouterPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1, 3),
    _HwRouterPortUpTime_Type()
)
hwRouterPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouterPortUpTime.setStatus("current")
_HwRouterPortExpires_Type = Unsigned32
_HwRouterPortExpires_Object = MibTableColumn
hwRouterPortExpires = _HwRouterPortExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1, 4),
    _HwRouterPortExpires_Type()
)
hwRouterPortExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouterPortExpires.setStatus("current")
_HwRouterPortFlags_Type = PortFlag
_HwRouterPortFlags_Object = MibTableColumn
hwRouterPortFlags = _HwRouterPortFlags_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 3, 1, 5),
    _HwRouterPortFlags_Type()
)
hwRouterPortFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouterPortFlags.setStatus("current")
_HwRouterPortCfgTable_Object = MibTable
hwRouterPortCfgTable = _HwRouterPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 4)
)
if mibBuilder.loadTexts:
    hwRouterPortCfgTable.setStatus("current")
_HwRouterPortCfgEntry_Object = MibTableRow
hwRouterPortCfgEntry = _HwRouterPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 4, 1)
)
hwRouterPortCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwRouterPortCfgVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwRouterPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwRouterPortCfgEntry.setStatus("current")
_HwRouterPortCfgVlanIndex_Type = VlanIndex
_HwRouterPortCfgVlanIndex_Object = MibTableColumn
hwRouterPortCfgVlanIndex = _HwRouterPortCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 4, 1, 1),
    _HwRouterPortCfgVlanIndex_Type()
)
hwRouterPortCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouterPortCfgVlanIndex.setStatus("current")
_HwRouterPortCfgIfIndex_Type = InterfaceIndex
_HwRouterPortCfgIfIndex_Object = MibTableColumn
hwRouterPortCfgIfIndex = _HwRouterPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 4, 1, 2),
    _HwRouterPortCfgIfIndex_Type()
)
hwRouterPortCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRouterPortCfgIfIndex.setStatus("current")
_HwRouterPortCfgRowStatus_Type = RowStatus
_HwRouterPortCfgRowStatus_Object = MibTableColumn
hwRouterPortCfgRowStatus = _HwRouterPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 4, 1, 100),
    _HwRouterPortCfgRowStatus_Type()
)
hwRouterPortCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRouterPortCfgRowStatus.setStatus("current")
_HwPortLimitTable_Object = MibTable
hwPortLimitTable = _HwPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 5)
)
if mibBuilder.loadTexts:
    hwPortLimitTable.setStatus("current")
_HwPortLimitEntry_Object = MibTableRow
hwPortLimitEntry = _HwPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 5, 1)
)
hwPortLimitEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwPortLimitIfIndex"),
)
if mibBuilder.loadTexts:
    hwPortLimitEntry.setStatus("current")
_HwPortLimitIfIndex_Type = InterfaceIndex
_HwPortLimitIfIndex_Object = MibTableColumn
hwPortLimitIfIndex = _HwPortLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 5, 1, 1),
    _HwPortLimitIfIndex_Type()
)
hwPortLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortLimitIfIndex.setStatus("current")
_HwPortLimitNumber_Type = Integer32
_HwPortLimitNumber_Object = MibTableColumn
hwPortLimitNumber = _HwPortLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 5, 1, 2),
    _HwPortLimitNumber_Type()
)
hwPortLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitNumber.setStatus("current")
_HwPortLimitRowStatus_Type = RowStatus
_HwPortLimitRowStatus_Object = MibTableColumn
hwPortLimitRowStatus = _HwPortLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 5, 1, 100),
    _HwPortLimitRowStatus_Type()
)
hwPortLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortLimitRowStatus.setStatus("current")
_HwPortGroupPolicyTable_Object = MibTable
hwPortGroupPolicyTable = _HwPortGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6)
)
if mibBuilder.loadTexts:
    hwPortGroupPolicyTable.setStatus("current")
_HwPortGroupPolicyEntry_Object = MibTableRow
hwPortGroupPolicyEntry = _HwPortGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1)
)
hwPortGroupPolicyEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwPortGroupPolicyIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwPortGroupPolicyVlanIndex"),
)
if mibBuilder.loadTexts:
    hwPortGroupPolicyEntry.setStatus("current")
_HwPortGroupPolicyIfIndex_Type = InterfaceIndex
_HwPortGroupPolicyIfIndex_Object = MibTableColumn
hwPortGroupPolicyIfIndex = _HwPortGroupPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1, 1),
    _HwPortGroupPolicyIfIndex_Type()
)
hwPortGroupPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyIfIndex.setStatus("current")


class _HwPortGroupPolicyAclNumber_Type(Integer32):
    """Custom type hwPortGroupPolicyAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 3999),
    )


_HwPortGroupPolicyAclNumber_Type.__name__ = "Integer32"
_HwPortGroupPolicyAclNumber_Object = MibTableColumn
hwPortGroupPolicyAclNumber = _HwPortGroupPolicyAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1, 2),
    _HwPortGroupPolicyAclNumber_Type()
)
hwPortGroupPolicyAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyAclNumber.setStatus("current")
_HwPortGroupPolicyVlanIndex_Type = VlanIndex
_HwPortGroupPolicyVlanIndex_Object = MibTableColumn
hwPortGroupPolicyVlanIndex = _HwPortGroupPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1, 3),
    _HwPortGroupPolicyVlanIndex_Type()
)
hwPortGroupPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortGroupPolicyVlanIndex.setStatus("current")


class _HwPortGroupPolicyVersion_Type(Integer32):
    """Custom type hwPortGroupPolicyVersion based on Integer32"""
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
        *(("igmpV1", 1),
          ("igmpV1V2", 3),
          ("igmpV1V2V3", 5),
          ("igmpV2", 2),
          ("igmpV3", 4))
    )


_HwPortGroupPolicyVersion_Type.__name__ = "Integer32"
_HwPortGroupPolicyVersion_Object = MibTableColumn
hwPortGroupPolicyVersion = _HwPortGroupPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1, 4),
    _HwPortGroupPolicyVersion_Type()
)
hwPortGroupPolicyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyVersion.setStatus("current")
_HwPortGroupPolicyRowStatus_Type = RowStatus
_HwPortGroupPolicyRowStatus_Object = MibTableColumn
hwPortGroupPolicyRowStatus = _HwPortGroupPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 6, 1, 51),
    _HwPortGroupPolicyRowStatus_Type()
)
hwPortGroupPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortGroupPolicyRowStatus.setStatus("current")
_HwExternPortStaticGrpTable_Object = MibTable
hwExternPortStaticGrpTable = _HwExternPortStaticGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7)
)
if mibBuilder.loadTexts:
    hwExternPortStaticGrpTable.setStatus("current")
_HwExternPortStaticGrpEntry_Object = MibTableRow
hwExternPortStaticGrpEntry = _HwExternPortStaticGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1)
)
hwExternPortStaticGrpEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwExternPortStaticGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternPortStaticGrpIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternPortStaticGroupAddr"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternPortStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    hwExternPortStaticGrpEntry.setStatus("current")
_HwExternPortStaticGrpVlanIndex_Type = VlanIndex
_HwExternPortStaticGrpVlanIndex_Object = MibTableColumn
hwExternPortStaticGrpVlanIndex = _HwExternPortStaticGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1, 1),
    _HwExternPortStaticGrpVlanIndex_Type()
)
hwExternPortStaticGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternPortStaticGrpVlanIndex.setStatus("current")
_HwExternPortStaticGrpIfIndex_Type = InterfaceIndex
_HwExternPortStaticGrpIfIndex_Object = MibTableColumn
hwExternPortStaticGrpIfIndex = _HwExternPortStaticGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1, 2),
    _HwExternPortStaticGrpIfIndex_Type()
)
hwExternPortStaticGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternPortStaticGrpIfIndex.setStatus("current")
_HwExternPortStaticGroupAddr_Type = IpAddress
_HwExternPortStaticGroupAddr_Object = MibTableColumn
hwExternPortStaticGroupAddr = _HwExternPortStaticGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1, 3),
    _HwExternPortStaticGroupAddr_Type()
)
hwExternPortStaticGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternPortStaticGroupAddr.setStatus("current")
_HwExternPortStaticSourceAddr_Type = IpAddress
_HwExternPortStaticSourceAddr_Object = MibTableColumn
hwExternPortStaticSourceAddr = _HwExternPortStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1, 4),
    _HwExternPortStaticSourceAddr_Type()
)
hwExternPortStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternPortStaticSourceAddr.setStatus("current")
_HwExternPortStaticGrpRowStatus_Type = RowStatus
_HwExternPortStaticGrpRowStatus_Object = MibTableColumn
hwExternPortStaticGrpRowStatus = _HwExternPortStaticGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 7, 1, 51),
    _HwExternPortStaticGrpRowStatus_Type()
)
hwExternPortStaticGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwExternPortStaticGrpRowStatus.setStatus("current")
_HwPortVlanLimitTable_Object = MibTable
hwPortVlanLimitTable = _HwPortVlanLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8)
)
if mibBuilder.loadTexts:
    hwPortVlanLimitTable.setStatus("current")
_HwPortVlanLimitEntry_Object = MibTableRow
hwPortVlanLimitEntry = _HwPortVlanLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8, 1)
)
hwPortVlanLimitEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwPortVlanLimitIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwPortVlanLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    hwPortVlanLimitEntry.setStatus("current")
_HwPortVlanLimitIfIndex_Type = InterfaceIndex
_HwPortVlanLimitIfIndex_Object = MibTableColumn
hwPortVlanLimitIfIndex = _HwPortVlanLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8, 1, 1),
    _HwPortVlanLimitIfIndex_Type()
)
hwPortVlanLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortVlanLimitIfIndex.setStatus("current")
_HwPortVlanLimitNumber_Type = Integer32
_HwPortVlanLimitNumber_Object = MibTableColumn
hwPortVlanLimitNumber = _HwPortVlanLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8, 1, 2),
    _HwPortVlanLimitNumber_Type()
)
hwPortVlanLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortVlanLimitNumber.setStatus("current")
_HwPortVlanLimitVlanIndex_Type = VlanIndex
_HwPortVlanLimitVlanIndex_Object = MibTableColumn
hwPortVlanLimitVlanIndex = _HwPortVlanLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8, 1, 3),
    _HwPortVlanLimitVlanIndex_Type()
)
hwPortVlanLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortVlanLimitVlanIndex.setStatus("current")
_HwPortVlanLimitRowStatus_Type = RowStatus
_HwPortVlanLimitRowStatus_Object = MibTableColumn
hwPortVlanLimitRowStatus = _HwPortVlanLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 1, 5, 8, 1, 51),
    _HwPortVlanLimitRowStatus_Type()
)
hwPortVlanLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortVlanLimitRowStatus.setStatus("current")
_HwMldSnpgMibObject_ObjectIdentity = ObjectIdentity
hwMldSnpgMibObject = _HwMldSnpgMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2)
)
_HwMldSnpgSystemInfo_ObjectIdentity = ObjectIdentity
hwMldSnpgSystemInfo = _HwMldSnpgSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 1)
)
_HwMldSnoopingEnabled_Type = EnabledStatus
_HwMldSnoopingEnabled_Object = MibScalar
hwMldSnoopingEnabled = _HwMldSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 1, 1),
    _HwMldSnoopingEnabled_Type()
)
hwMldSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSnoopingEnabled.setStatus("current")
_HwMldSendQueryEnabled_Type = EnabledStatus
_HwMldSendQueryEnabled_Object = MibScalar
hwMldSendQueryEnabled = _HwMldSendQueryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 1, 2),
    _HwMldSendQueryEnabled_Type()
)
hwMldSendQueryEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSendQueryEnabled.setStatus("current")
_HwMldSendQuerySourceIpAddr_Type = Ipv6Address
_HwMldSendQuerySourceIpAddr_Object = MibScalar
hwMldSendQuerySourceIpAddr = _HwMldSendQuerySourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 1, 3),
    _HwMldSendQuerySourceIpAddr_Type()
)
hwMldSendQuerySourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSendQuerySourceIpAddr.setStatus("current")


class _HwMldSnoopingSuppressionTime_Type(Integer32):
    """Custom type hwMldSnoopingSuppressionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HwMldSnoopingSuppressionTime_Type.__name__ = "Integer32"
_HwMldSnoopingSuppressionTime_Object = MibScalar
hwMldSnoopingSuppressionTime = _HwMldSnoopingSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 1, 4),
    _HwMldSnoopingSuppressionTime_Type()
)
hwMldSnoopingSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSnoopingSuppressionTime.setStatus("current")
_HwMldVlanCfgInfo_ObjectIdentity = ObjectIdentity
hwMldVlanCfgInfo = _HwMldVlanCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2)
)
_HwMldVlanCfgTable_Object = MibTable
hwMldVlanCfgTable = _HwMldVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwMldVlanCfgTable.setStatus("current")
_HwMldVlanCfgEntry_Object = MibTableRow
hwMldVlanCfgEntry = _HwMldVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1)
)
hwMldVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMldVlanCfgEntry.setStatus("current")
_HwMldVlanIndex_Type = VlanIndex
_HwMldVlanIndex_Object = MibTableColumn
hwMldVlanIndex = _HwMldVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 1),
    _HwMldVlanIndex_Type()
)
hwMldVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldVlanIndex.setStatus("current")
_HwVlanMldSnoopingEnabled_Type = EnabledStatus
_HwVlanMldSnoopingEnabled_Object = MibTableColumn
hwVlanMldSnoopingEnabled = _HwVlanMldSnoopingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 2),
    _HwVlanMldSnoopingEnabled_Type()
)
hwVlanMldSnoopingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMldSnoopingEnabled.setStatus("current")


class _HwMldVlanRouterAgingTime_Type(Integer32):
    """Custom type hwMldVlanRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwMldVlanRouterAgingTime_Type.__name__ = "Integer32"
_HwMldVlanRouterAgingTime_Object = MibTableColumn
hwMldVlanRouterAgingTime = _HwMldVlanRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 3),
    _HwMldVlanRouterAgingTime_Type()
)
hwMldVlanRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanRouterAgingTime.setStatus("current")


class _HwMldVlanMaxQueryRespTime_Type(Integer32):
    """Custom type hwMldVlanMaxQueryRespTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_HwMldVlanMaxQueryRespTime_Type.__name__ = "Integer32"
_HwMldVlanMaxQueryRespTime_Object = MibTableColumn
hwMldVlanMaxQueryRespTime = _HwMldVlanMaxQueryRespTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 4),
    _HwMldVlanMaxQueryRespTime_Type()
)
hwMldVlanMaxQueryRespTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanMaxQueryRespTime.setStatus("current")


class _HwMldVlanLastListenerQueryInt_Type(Integer32):
    """Custom type hwMldVlanLastListenerQueryInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwMldVlanLastListenerQueryInt_Type.__name__ = "Integer32"
_HwMldVlanLastListenerQueryInt_Object = MibTableColumn
hwMldVlanLastListenerQueryInt = _HwMldVlanLastListenerQueryInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 5),
    _HwMldVlanLastListenerQueryInt_Type()
)
hwMldVlanLastListenerQueryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanLastListenerQueryInt.setStatus("current")


class _HwMldVlanQueryInt_Type(Integer32):
    """Custom type hwMldVlanQueryInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMldVlanQueryInt_Type.__name__ = "Integer32"
_HwMldVlanQueryInt_Object = MibTableColumn
hwMldVlanQueryInt = _HwMldVlanQueryInt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 6),
    _HwMldVlanQueryInt_Type()
)
hwMldVlanQueryInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanQueryInt.setStatus("current")


class _HwMldVlanRobustCount_Type(Integer32):
    """Custom type hwMldVlanRobustCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 5),
    )


_HwMldVlanRobustCount_Type.__name__ = "Integer32"
_HwMldVlanRobustCount_Object = MibTableColumn
hwMldVlanRobustCount = _HwMldVlanRobustCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 7),
    _HwMldVlanRobustCount_Type()
)
hwMldVlanRobustCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanRobustCount.setStatus("current")


class _HwMldVlanCheckRouterAlert_Type(TruthValue):
    """Custom type hwMldVlanCheckRouterAlert based on TruthValue"""


_HwMldVlanCheckRouterAlert_Object = MibTableColumn
hwMldVlanCheckRouterAlert = _HwMldVlanCheckRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 8),
    _HwMldVlanCheckRouterAlert_Type()
)
hwMldVlanCheckRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanCheckRouterAlert.setStatus("current")


class _HwMldVlanSendRouterAlert_Type(TruthValue):
    """Custom type hwMldVlanSendRouterAlert based on TruthValue"""


_HwMldVlanSendRouterAlert_Object = MibTableColumn
hwMldVlanSendRouterAlert = _HwMldVlanSendRouterAlert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 9),
    _HwMldVlanSendRouterAlert_Type()
)
hwMldVlanSendRouterAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanSendRouterAlert.setStatus("current")


class _HwVlanMldVersion_Type(Integer32):
    """Custom type hwVlanMldVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mldV1", 1),
          ("mldV2", 2))
    )


_HwVlanMldVersion_Type.__name__ = "Integer32"
_HwVlanMldVersion_Object = MibTableColumn
hwVlanMldVersion = _HwVlanMldVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 10),
    _HwVlanMldVersion_Type()
)
hwVlanMldVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMldVersion.setStatus("current")
_HwMldVlanPromptLeaveEnable_Type = EnabledStatus
_HwMldVlanPromptLeaveEnable_Object = MibTableColumn
hwMldVlanPromptLeaveEnable = _HwMldVlanPromptLeaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 11),
    _HwMldVlanPromptLeaveEnable_Type()
)
hwMldVlanPromptLeaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanPromptLeaveEnable.setStatus("current")


class _HwMldVlanPromptLeaveAclNum_Type(Integer32):
    """Custom type hwMldVlanPromptLeaveAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 3999),
    )


_HwMldVlanPromptLeaveAclNum_Type.__name__ = "Integer32"
_HwMldVlanPromptLeaveAclNum_Object = MibTableColumn
hwMldVlanPromptLeaveAclNum = _HwMldVlanPromptLeaveAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 12),
    _HwMldVlanPromptLeaveAclNum_Type()
)
hwMldVlanPromptLeaveAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanPromptLeaveAclNum.setStatus("current")
_HwMldVlanDropUnknown_Type = EnabledStatus
_HwMldVlanDropUnknown_Object = MibTableColumn
hwMldVlanDropUnknown = _HwMldVlanDropUnknown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 2, 1, 1, 13),
    _HwMldVlanDropUnknown_Type()
)
hwMldVlanDropUnknown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldVlanDropUnknown.setStatus("current")
_HwMldStatisticsInfo_ObjectIdentity = ObjectIdentity
hwMldStatisticsInfo = _HwMldStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3)
)
_HwMldSystemStatisticsInfo_ObjectIdentity = ObjectIdentity
hwMldSystemStatisticsInfo = _HwMldSystemStatisticsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1)
)
_HwMldSystemRecvVlanUpEventTimes_Type = Counter32
_HwMldSystemRecvVlanUpEventTimes_Object = MibScalar
hwMldSystemRecvVlanUpEventTimes = _HwMldSystemRecvVlanUpEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 1),
    _HwMldSystemRecvVlanUpEventTimes_Type()
)
hwMldSystemRecvVlanUpEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvVlanUpEventTimes.setStatus("current")
_HwMldSystemRecvVlanDownEventTimes_Type = Counter32
_HwMldSystemRecvVlanDownEventTimes_Object = MibScalar
hwMldSystemRecvVlanDownEventTimes = _HwMldSystemRecvVlanDownEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 2),
    _HwMldSystemRecvVlanDownEventTimes_Type()
)
hwMldSystemRecvVlanDownEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvVlanDownEventTimes.setStatus("current")
_HwMldSystemRecvVlanDelEventTimes_Type = Counter32
_HwMldSystemRecvVlanDelEventTimes_Object = MibScalar
hwMldSystemRecvVlanDelEventTimes = _HwMldSystemRecvVlanDelEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 3),
    _HwMldSystemRecvVlanDelEventTimes_Type()
)
hwMldSystemRecvVlanDelEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvVlanDelEventTimes.setStatus("current")
_HwMldSystemRecvPortUpEventTimes_Type = Counter32
_HwMldSystemRecvPortUpEventTimes_Object = MibScalar
hwMldSystemRecvPortUpEventTimes = _HwMldSystemRecvPortUpEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 4),
    _HwMldSystemRecvPortUpEventTimes_Type()
)
hwMldSystemRecvPortUpEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvPortUpEventTimes.setStatus("current")
_HwMldSystemRecvPortDownEventTimes_Type = Counter32
_HwMldSystemRecvPortDownEventTimes_Object = MibScalar
hwMldSystemRecvPortDownEventTimes = _HwMldSystemRecvPortDownEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 5),
    _HwMldSystemRecvPortDownEventTimes_Type()
)
hwMldSystemRecvPortDownEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvPortDownEventTimes.setStatus("current")
_HwMldSystemRecvPortDelEventTimes_Type = Counter32
_HwMldSystemRecvPortDelEventTimes_Object = MibScalar
hwMldSystemRecvPortDelEventTimes = _HwMldSystemRecvPortDelEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 6),
    _HwMldSystemRecvPortDelEventTimes_Type()
)
hwMldSystemRecvPortDelEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvPortDelEventTimes.setStatus("current")
_HwMldSystemRecvPortIncEventTimes_Type = Counter32
_HwMldSystemRecvPortIncEventTimes_Object = MibScalar
hwMldSystemRecvPortIncEventTimes = _HwMldSystemRecvPortIncEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 7),
    _HwMldSystemRecvPortIncEventTimes_Type()
)
hwMldSystemRecvPortIncEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvPortIncEventTimes.setStatus("current")
_HwMldSystemRecvPortExcEventTimes_Type = Counter32
_HwMldSystemRecvPortExcEventTimes_Object = MibScalar
hwMldSystemRecvPortExcEventTimes = _HwMldSystemRecvPortExcEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 8),
    _HwMldSystemRecvPortExcEventTimes_Type()
)
hwMldSystemRecvPortExcEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvPortExcEventTimes.setStatus("current")
_HwMldSystemRecvMstpBlockEventTimes_Type = Counter32
_HwMldSystemRecvMstpBlockEventTimes_Object = MibScalar
hwMldSystemRecvMstpBlockEventTimes = _HwMldSystemRecvMstpBlockEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 9),
    _HwMldSystemRecvMstpBlockEventTimes_Type()
)
hwMldSystemRecvMstpBlockEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvMstpBlockEventTimes.setStatus("current")
_HwMldSystemRecvMstpForwardEventTimes_Type = Counter32
_HwMldSystemRecvMstpForwardEventTimes_Object = MibScalar
hwMldSystemRecvMstpForwardEventTimes = _HwMldSystemRecvMstpForwardEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 10),
    _HwMldSystemRecvMstpForwardEventTimes_Type()
)
hwMldSystemRecvMstpForwardEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvMstpForwardEventTimes.setStatus("current")
_HwMldSystemSysClearStats_Type = TruthValue
_HwMldSystemSysClearStats_Object = MibScalar
hwMldSystemSysClearStats = _HwMldSystemSysClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 11),
    _HwMldSystemSysClearStats_Type()
)
hwMldSystemSysClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSystemSysClearStats.setStatus("current")
_HwMldSystemPacketClearStats_Type = TruthValue
_HwMldSystemPacketClearStats_Object = MibScalar
hwMldSystemPacketClearStats = _HwMldSystemPacketClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 12),
    _HwMldSystemPacketClearStats_Type()
)
hwMldSystemPacketClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMldSystemPacketClearStats.setStatus("current")
_HwMldSystemRecvLinkChangeEventTimes_Type = Counter32
_HwMldSystemRecvLinkChangeEventTimes_Object = MibScalar
hwMldSystemRecvLinkChangeEventTimes = _HwMldSystemRecvLinkChangeEventTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 1, 13),
    _HwMldSystemRecvLinkChangeEventTimes_Type()
)
hwMldSystemRecvLinkChangeEventTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldSystemRecvLinkChangeEventTimes.setStatus("current")
_HwMldVlanStatisticsTable_Object = MibTable
hwMldVlanStatisticsTable = _HwMldVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hwMldVlanStatisticsTable.setStatus("current")
_HwMldVlanStatisticsEntry_Object = MibTableRow
hwMldVlanStatisticsEntry = _HwMldVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1)
)
hwMldVlanStatisticsEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldVlanStatsVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMldVlanStatisticsEntry.setStatus("current")
_HwMldVlanStatsVlanIndex_Type = VlanIndex
_HwMldVlanStatsVlanIndex_Object = MibTableColumn
hwMldVlanStatsVlanIndex = _HwMldVlanStatsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 1),
    _HwMldVlanStatsVlanIndex_Type()
)
hwMldVlanStatsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldVlanStatsVlanIndex.setStatus("current")
_HwVlanRecvMldV1ReportNum_Type = Counter32
_HwVlanRecvMldV1ReportNum_Object = MibTableColumn
hwVlanRecvMldV1ReportNum = _HwVlanRecvMldV1ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 2),
    _HwVlanRecvMldV1ReportNum_Type()
)
hwVlanRecvMldV1ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvMldV1ReportNum.setStatus("current")
_HwVlanRecvMldV2ReportNum_Type = Counter32
_HwVlanRecvMldV2ReportNum_Object = MibTableColumn
hwVlanRecvMldV2ReportNum = _HwVlanRecvMldV2ReportNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 3),
    _HwVlanRecvMldV2ReportNum_Type()
)
hwVlanRecvMldV2ReportNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvMldV2ReportNum.setStatus("current")
_HwVlanRecvMldDoneNum_Type = Counter32
_HwVlanRecvMldDoneNum_Object = MibTableColumn
hwVlanRecvMldDoneNum = _HwVlanRecvMldDoneNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 4),
    _HwVlanRecvMldDoneNum_Type()
)
hwVlanRecvMldDoneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvMldDoneNum.setStatus("current")
_HwVlanRecvMldV1QueryNum_Type = Counter32
_HwVlanRecvMldV1QueryNum_Object = MibTableColumn
hwVlanRecvMldV1QueryNum = _HwVlanRecvMldV1QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 5),
    _HwVlanRecvMldV1QueryNum_Type()
)
hwVlanRecvMldV1QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvMldV1QueryNum.setStatus("current")
_HwVlanRecvMldV2QueryNum_Type = Counter32
_HwVlanRecvMldV2QueryNum_Object = MibTableColumn
hwVlanRecvMldV2QueryNum = _HwVlanRecvMldV2QueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 6),
    _HwVlanRecvMldV2QueryNum_Type()
)
hwVlanRecvMldV2QueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvMldV2QueryNum.setStatus("current")
_HwVlanRecvIpv6PimHelloNum_Type = Counter32
_HwVlanRecvIpv6PimHelloNum_Object = MibTableColumn
hwVlanRecvIpv6PimHelloNum = _HwVlanRecvIpv6PimHelloNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 7),
    _HwVlanRecvIpv6PimHelloNum_Type()
)
hwVlanRecvIpv6PimHelloNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanRecvIpv6PimHelloNum.setStatus("current")
_HwVlanSendMldQueryNum_Type = Counter32
_HwVlanSendMldQueryNum_Object = MibTableColumn
hwVlanSendMldQueryNum = _HwVlanSendMldQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 8),
    _HwVlanSendMldQueryNum_Type()
)
hwVlanSendMldQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSendMldQueryNum.setStatus("current")
_HwVlanMldPacketClearStats_Type = TruthValue
_HwVlanMldPacketClearStats_Object = MibTableColumn
hwVlanMldPacketClearStats = _HwVlanMldPacketClearStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 9),
    _HwVlanMldPacketClearStats_Type()
)
hwVlanMldPacketClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMldPacketClearStats.setStatus("current")
_HwVlanSendSourceIpSpecMldQueryNum_Type = Counter32
_HwVlanSendSourceIpSpecMldQueryNum_Object = MibTableColumn
hwVlanSendSourceIpSpecMldQueryNum = _HwVlanSendSourceIpSpecMldQueryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 3, 2, 1, 10),
    _HwVlanSendSourceIpSpecMldQueryNum_Type()
)
hwVlanSendSourceIpSpecMldQueryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVlanSendSourceIpSpecMldQueryNum.setStatus("current")
_HwMldMCGrpInfo_ObjectIdentity = ObjectIdentity
hwMldMCGrpInfo = _HwMldMCGrpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4)
)
_HwMldIpGrpInfoTable_Object = MibTable
hwMldIpGrpInfoTable = _HwMldIpGrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hwMldIpGrpInfoTable.setStatus("current")
_HwMldIpGrpInfoEntry_Object = MibTableRow
hwMldIpGrpInfoEntry = _HwMldIpGrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1)
)
hwMldIpGrpInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldIpGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldIpGrpPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldIpGrpAddress"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldIpSourceAddress"),
)
if mibBuilder.loadTexts:
    hwMldIpGrpInfoEntry.setStatus("current")
_HwMldIpGrpVlanIndex_Type = VlanIndex
_HwMldIpGrpVlanIndex_Object = MibTableColumn
hwMldIpGrpVlanIndex = _HwMldIpGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 1),
    _HwMldIpGrpVlanIndex_Type()
)
hwMldIpGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldIpGrpVlanIndex.setStatus("current")
_HwMldIpGrpPortIfIndex_Type = InterfaceIndex
_HwMldIpGrpPortIfIndex_Object = MibTableColumn
hwMldIpGrpPortIfIndex = _HwMldIpGrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 2),
    _HwMldIpGrpPortIfIndex_Type()
)
hwMldIpGrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldIpGrpPortIfIndex.setStatus("current")
_HwMldIpGrpAddress_Type = Ipv6Address
_HwMldIpGrpAddress_Object = MibTableColumn
hwMldIpGrpAddress = _HwMldIpGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 3),
    _HwMldIpGrpAddress_Type()
)
hwMldIpGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldIpGrpAddress.setStatus("current")
_HwMldIpGrpUpTime_Type = Unsigned32
_HwMldIpGrpUpTime_Object = MibTableColumn
hwMldIpGrpUpTime = _HwMldIpGrpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 4),
    _HwMldIpGrpUpTime_Type()
)
hwMldIpGrpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpGrpUpTime.setStatus("current")
_HwMldIpHostUpTime_Type = Unsigned32
_HwMldIpHostUpTime_Object = MibTableColumn
hwMldIpHostUpTime = _HwMldIpHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 5),
    _HwMldIpHostUpTime_Type()
)
hwMldIpHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpHostUpTime.setStatus("current")
_HwMldIpHostExpires_Type = Unsigned32
_HwMldIpHostExpires_Object = MibTableColumn
hwMldIpHostExpires = _HwMldIpHostExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 6),
    _HwMldIpHostExpires_Type()
)
hwMldIpHostExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpHostExpires.setStatus("current")
_HwMldIpHostFlag_Type = PortFlag
_HwMldIpHostFlag_Object = MibTableColumn
hwMldIpHostFlag = _HwMldIpHostFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 7),
    _HwMldIpHostFlag_Type()
)
hwMldIpHostFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpHostFlag.setStatus("current")
_HwMldIpRtUpTime_Type = Unsigned32
_HwMldIpRtUpTime_Object = MibTableColumn
hwMldIpRtUpTime = _HwMldIpRtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 8),
    _HwMldIpRtUpTime_Type()
)
hwMldIpRtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpRtUpTime.setStatus("current")
_HwMldIpRtExpires_Type = Unsigned32
_HwMldIpRtExpires_Object = MibTableColumn
hwMldIpRtExpires = _HwMldIpRtExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 9),
    _HwMldIpRtExpires_Type()
)
hwMldIpRtExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpRtExpires.setStatus("current")
_HwMldIpRtFlag_Type = PortFlag
_HwMldIpRtFlag_Object = MibTableColumn
hwMldIpRtFlag = _HwMldIpRtFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 10),
    _HwMldIpRtFlag_Type()
)
hwMldIpRtFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldIpRtFlag.setStatus("current")
_HwMldIpSourceAddress_Type = Ipv6Address
_HwMldIpSourceAddress_Object = MibTableColumn
hwMldIpSourceAddress = _HwMldIpSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 4, 1, 1, 11),
    _HwMldIpSourceAddress_Type()
)
hwMldIpSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldIpSourceAddress.setStatus("current")
_HwMldPortInfo_ObjectIdentity = ObjectIdentity
hwMldPortInfo = _HwMldPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5)
)
_HwMldPortStaticGrpTable_Object = MibTable
hwMldPortStaticGrpTable = _HwMldPortStaticGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1)
)
if mibBuilder.loadTexts:
    hwMldPortStaticGrpTable.setStatus("current")
_HwMldPortStaticGrpEntry_Object = MibTableRow
hwMldPortStaticGrpEntry = _HwMldPortStaticGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1)
)
hwMldPortStaticGrpEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortStaticGrpVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortStaticGrpIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortStaticGrpAddr"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortStaticSourceAddr"),
)
if mibBuilder.loadTexts:
    hwMldPortStaticGrpEntry.setStatus("current")
_HwMldPortStaticGrpVlanIndex_Type = VlanIndex
_HwMldPortStaticGrpVlanIndex_Object = MibTableColumn
hwMldPortStaticGrpVlanIndex = _HwMldPortStaticGrpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1, 1),
    _HwMldPortStaticGrpVlanIndex_Type()
)
hwMldPortStaticGrpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortStaticGrpVlanIndex.setStatus("current")
_HwMldPortStaticGrpIfIndex_Type = InterfaceIndex
_HwMldPortStaticGrpIfIndex_Object = MibTableColumn
hwMldPortStaticGrpIfIndex = _HwMldPortStaticGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1, 2),
    _HwMldPortStaticGrpIfIndex_Type()
)
hwMldPortStaticGrpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortStaticGrpIfIndex.setStatus("current")
_HwMldPortStaticGrpAddr_Type = Ipv6Address
_HwMldPortStaticGrpAddr_Object = MibTableColumn
hwMldPortStaticGrpAddr = _HwMldPortStaticGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1, 3),
    _HwMldPortStaticGrpAddr_Type()
)
hwMldPortStaticGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortStaticGrpAddr.setStatus("current")
_HwMldPortStaticSourceAddr_Type = Ipv6Address
_HwMldPortStaticSourceAddr_Object = MibTableColumn
hwMldPortStaticSourceAddr = _HwMldPortStaticSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1, 4),
    _HwMldPortStaticSourceAddr_Type()
)
hwMldPortStaticSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortStaticSourceAddr.setStatus("current")
_HwMldPortStaticGrpRowStatus_Type = RowStatus
_HwMldPortStaticGrpRowStatus_Object = MibTableColumn
hwMldPortStaticGrpRowStatus = _HwMldPortStaticGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 1, 1, 51),
    _HwMldPortStaticGrpRowStatus_Type()
)
hwMldPortStaticGrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortStaticGrpRowStatus.setStatus("current")
_HwMldGrpPolicyCfgTable_Object = MibTable
hwMldGrpPolicyCfgTable = _HwMldGrpPolicyCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2)
)
if mibBuilder.loadTexts:
    hwMldGrpPolicyCfgTable.setStatus("current")
_HwMldGrpPolicyCfgEntry_Object = MibTableRow
hwMldGrpPolicyCfgEntry = _HwMldGrpPolicyCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2, 1)
)
hwMldGrpPolicyCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldGrpPolicyVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMldGrpPolicyCfgEntry.setStatus("current")
_HwMldGrpPolicyVlanIndex_Type = VlanIndex
_HwMldGrpPolicyVlanIndex_Object = MibTableColumn
hwMldGrpPolicyVlanIndex = _HwMldGrpPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2, 1, 1),
    _HwMldGrpPolicyVlanIndex_Type()
)
hwMldGrpPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldGrpPolicyVlanIndex.setStatus("current")


class _HwMldGrpPolicyAclNum_Type(Integer32):
    """Custom type hwMldGrpPolicyAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 3999),
    )


_HwMldGrpPolicyAclNum_Type.__name__ = "Integer32"
_HwMldGrpPolicyAclNum_Object = MibTableColumn
hwMldGrpPolicyAclNum = _HwMldGrpPolicyAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2, 1, 2),
    _HwMldGrpPolicyAclNum_Type()
)
hwMldGrpPolicyAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldGrpPolicyAclNum.setStatus("current")


class _HwGrpPolicyMldVersion_Type(Integer32):
    """Custom type hwGrpPolicyMldVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mldV1", 1),
          ("mldV1V2", 3),
          ("mldV2", 2))
    )


_HwGrpPolicyMldVersion_Type.__name__ = "Integer32"
_HwGrpPolicyMldVersion_Object = MibTableColumn
hwGrpPolicyMldVersion = _HwGrpPolicyMldVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2, 1, 3),
    _HwGrpPolicyMldVersion_Type()
)
hwGrpPolicyMldVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGrpPolicyMldVersion.setStatus("current")
_HwMldGrpPolicyRowStatus_Type = RowStatus
_HwMldGrpPolicyRowStatus_Object = MibTableColumn
hwMldGrpPolicyRowStatus = _HwMldGrpPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 2, 1, 51),
    _HwMldGrpPolicyRowStatus_Type()
)
hwMldGrpPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldGrpPolicyRowStatus.setStatus("current")
_HwMldRouterPortInfoTable_Object = MibTable
hwMldRouterPortInfoTable = _HwMldRouterPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3)
)
if mibBuilder.loadTexts:
    hwMldRouterPortInfoTable.setStatus("current")
_HwMldRouterPortInfoEntry_Object = MibTableRow
hwMldRouterPortInfoEntry = _HwMldRouterPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1)
)
hwMldRouterPortInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldRouterPortVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldRouterPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwMldRouterPortInfoEntry.setStatus("current")
_HwMldRouterPortVlanIndex_Type = VlanIndex
_HwMldRouterPortVlanIndex_Object = MibTableColumn
hwMldRouterPortVlanIndex = _HwMldRouterPortVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1, 1),
    _HwMldRouterPortVlanIndex_Type()
)
hwMldRouterPortVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldRouterPortVlanIndex.setStatus("current")
_HwMldRouterPortIfIndex_Type = InterfaceIndex
_HwMldRouterPortIfIndex_Object = MibTableColumn
hwMldRouterPortIfIndex = _HwMldRouterPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1, 2),
    _HwMldRouterPortIfIndex_Type()
)
hwMldRouterPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldRouterPortIfIndex.setStatus("current")
_HwMldRouterPortUpTime_Type = Unsigned32
_HwMldRouterPortUpTime_Object = MibTableColumn
hwMldRouterPortUpTime = _HwMldRouterPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1, 3),
    _HwMldRouterPortUpTime_Type()
)
hwMldRouterPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldRouterPortUpTime.setStatus("current")
_HwMldRouterPortExpires_Type = Unsigned32
_HwMldRouterPortExpires_Object = MibTableColumn
hwMldRouterPortExpires = _HwMldRouterPortExpires_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1, 4),
    _HwMldRouterPortExpires_Type()
)
hwMldRouterPortExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldRouterPortExpires.setStatus("current")
_HwMldRouterPortFlag_Type = PortFlag
_HwMldRouterPortFlag_Object = MibTableColumn
hwMldRouterPortFlag = _HwMldRouterPortFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 3, 1, 5),
    _HwMldRouterPortFlag_Type()
)
hwMldRouterPortFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMldRouterPortFlag.setStatus("current")
_HwMldRouterPortCfgTable_Object = MibTable
hwMldRouterPortCfgTable = _HwMldRouterPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 4)
)
if mibBuilder.loadTexts:
    hwMldRouterPortCfgTable.setStatus("current")
_HwMldRouterPortCfgEntry_Object = MibTableRow
hwMldRouterPortCfgEntry = _HwMldRouterPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 4, 1)
)
hwMldRouterPortCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldRouterPortCfgVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldRouterPortCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwMldRouterPortCfgEntry.setStatus("current")
_HwMldRouterPortCfgVlanIndex_Type = VlanIndex
_HwMldRouterPortCfgVlanIndex_Object = MibTableColumn
hwMldRouterPortCfgVlanIndex = _HwMldRouterPortCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 4, 1, 1),
    _HwMldRouterPortCfgVlanIndex_Type()
)
hwMldRouterPortCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldRouterPortCfgVlanIndex.setStatus("current")
_HwMldRouterPortCfgIfIndex_Type = InterfaceIndex
_HwMldRouterPortCfgIfIndex_Object = MibTableColumn
hwMldRouterPortCfgIfIndex = _HwMldRouterPortCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 4, 1, 2),
    _HwMldRouterPortCfgIfIndex_Type()
)
hwMldRouterPortCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldRouterPortCfgIfIndex.setStatus("current")
_HwMldRouterPortCfgRowStatus_Type = RowStatus
_HwMldRouterPortCfgRowStatus_Object = MibTableColumn
hwMldRouterPortCfgRowStatus = _HwMldRouterPortCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 4, 1, 51),
    _HwMldRouterPortCfgRowStatus_Type()
)
hwMldRouterPortCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldRouterPortCfgRowStatus.setStatus("current")
_HwMldPortLimitTable_Object = MibTable
hwMldPortLimitTable = _HwMldPortLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5)
)
if mibBuilder.loadTexts:
    hwMldPortLimitTable.setStatus("current")
_HwMldPortLimitEntry_Object = MibTableRow
hwMldPortLimitEntry = _HwMldPortLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5, 1)
)
hwMldPortLimitEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortLimitIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortLimitVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMldPortLimitEntry.setStatus("current")
_HwMldPortLimitIfIndex_Type = InterfaceIndex
_HwMldPortLimitIfIndex_Object = MibTableColumn
hwMldPortLimitIfIndex = _HwMldPortLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5, 1, 1),
    _HwMldPortLimitIfIndex_Type()
)
hwMldPortLimitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortLimitIfIndex.setStatus("current")


class _HwMldPortLimitNumber_Type(Integer32):
    """Custom type hwMldPortLimitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMldPortLimitNumber_Type.__name__ = "Integer32"
_HwMldPortLimitNumber_Object = MibTableColumn
hwMldPortLimitNumber = _HwMldPortLimitNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5, 1, 2),
    _HwMldPortLimitNumber_Type()
)
hwMldPortLimitNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortLimitNumber.setStatus("current")
_HwMldPortLimitVlanIndex_Type = VlanIndex
_HwMldPortLimitVlanIndex_Object = MibTableColumn
hwMldPortLimitVlanIndex = _HwMldPortLimitVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5, 1, 3),
    _HwMldPortLimitVlanIndex_Type()
)
hwMldPortLimitVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortLimitVlanIndex.setStatus("current")
_HwMldPortLimitRowStatus_Type = RowStatus
_HwMldPortLimitRowStatus_Object = MibTableColumn
hwMldPortLimitRowStatus = _HwMldPortLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 5, 1, 51),
    _HwMldPortLimitRowStatus_Type()
)
hwMldPortLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortLimitRowStatus.setStatus("current")
_HwMldPortGroupPolicyTable_Object = MibTable
hwMldPortGroupPolicyTable = _HwMldPortGroupPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6)
)
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyTable.setStatus("current")
_HwMldPortGroupPolicyEntry_Object = MibTableRow
hwMldPortGroupPolicyEntry = _HwMldPortGroupPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1)
)
hwMldPortGroupPolicyEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortGroupPolicyIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMldPortGroupPolicyVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyEntry.setStatus("current")
_HwMldPortGroupPolicyIfIndex_Type = InterfaceIndex
_HwMldPortGroupPolicyIfIndex_Object = MibTableColumn
hwMldPortGroupPolicyIfIndex = _HwMldPortGroupPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1, 1),
    _HwMldPortGroupPolicyIfIndex_Type()
)
hwMldPortGroupPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyIfIndex.setStatus("current")


class _HwMldPortGroupPolicyAclNumber_Type(Integer32):
    """Custom type hwMldPortGroupPolicyAclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(2000, 3999),
    )


_HwMldPortGroupPolicyAclNumber_Type.__name__ = "Integer32"
_HwMldPortGroupPolicyAclNumber_Object = MibTableColumn
hwMldPortGroupPolicyAclNumber = _HwMldPortGroupPolicyAclNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1, 2),
    _HwMldPortGroupPolicyAclNumber_Type()
)
hwMldPortGroupPolicyAclNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyAclNumber.setStatus("current")
_HwMldPortGroupPolicyVlanIndex_Type = VlanIndex
_HwMldPortGroupPolicyVlanIndex_Object = MibTableColumn
hwMldPortGroupPolicyVlanIndex = _HwMldPortGroupPolicyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1, 3),
    _HwMldPortGroupPolicyVlanIndex_Type()
)
hwMldPortGroupPolicyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyVlanIndex.setStatus("current")


class _HwMldPortGroupPolicyVersion_Type(Integer32):
    """Custom type hwMldPortGroupPolicyVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mldV1", 1),
          ("mldV2", 2))
    )


_HwMldPortGroupPolicyVersion_Type.__name__ = "Integer32"
_HwMldPortGroupPolicyVersion_Object = MibTableColumn
hwMldPortGroupPolicyVersion = _HwMldPortGroupPolicyVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1, 4),
    _HwMldPortGroupPolicyVersion_Type()
)
hwMldPortGroupPolicyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyVersion.setStatus("current")
_HwMldPortGroupPolicyRowStatus_Type = RowStatus
_HwMldPortGroupPolicyRowStatus_Object = MibTableColumn
hwMldPortGroupPolicyRowStatus = _HwMldPortGroupPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 2, 5, 6, 1, 51),
    _HwMldPortGroupPolicyRowStatus_Type()
)
hwMldPortGroupPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyRowStatus.setStatus("current")
_HwMVlanMibObject_ObjectIdentity = ObjectIdentity
hwMVlanMibObject = _HwMVlanMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3)
)
_HwMVlanSystemInfo_ObjectIdentity = ObjectIdentity
hwMVlanSystemInfo = _HwMVlanSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 1)
)
_HwMVlanEnabled_Type = EnabledStatus
_HwMVlanEnabled_Object = MibScalar
hwMVlanEnabled = _HwMVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 1, 1),
    _HwMVlanEnabled_Type()
)
hwMVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMVlanEnabled.setStatus("current")
_HwMVlanVlanCfgInfo_ObjectIdentity = ObjectIdentity
hwMVlanVlanCfgInfo = _HwMVlanVlanCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2)
)
_HwMVlanEnableTable_Object = MibTable
hwMVlanEnableTable = _HwMVlanEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwMVlanEnableTable.setStatus("current")
_HwMVlanEnableEntry_Object = MibTableRow
hwMVlanEnableEntry = _HwMVlanEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 1, 1)
)
hwMVlanEnableEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMVlanEnableEntry.setStatus("current")
_HwMVlanIndex_Type = VlanIndex
_HwMVlanIndex_Object = MibTableColumn
hwMVlanIndex = _HwMVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 1, 1, 1),
    _HwMVlanIndex_Type()
)
hwMVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanIndex.setStatus("current")
_HwMVlanStatus_Type = RowStatus
_HwMVlanStatus_Object = MibTableColumn
hwMVlanStatus = _HwMVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 1, 1, 100),
    _HwMVlanStatus_Type()
)
hwMVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMVlanStatus.setStatus("current")
_HwMVlanUserVlanTable_Object = MibTable
hwMVlanUserVlanTable = _HwMVlanUserVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 2)
)
if mibBuilder.loadTexts:
    hwMVlanUserVlanTable.setStatus("current")
_HwMVlanUserVlanEntry_Object = MibTableRow
hwMVlanUserVlanEntry = _HwMVlanUserVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 2, 1)
)
hwMVlanUserVlanEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwUserVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMVlanUserVlanEntry.setStatus("current")
_HwUserVlanIndex_Type = VlanIndex
_HwUserVlanIndex_Object = MibTableColumn
hwUserVlanIndex = _HwUserVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 2, 1, 1),
    _HwUserVlanIndex_Type()
)
hwUserVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUserVlanIndex.setStatus("current")
_HwUserVlanCfgRowStatus_Type = RowStatus
_HwUserVlanCfgRowStatus_Object = MibTableColumn
hwUserVlanCfgRowStatus = _HwUserVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 2, 1, 100),
    _HwUserVlanCfgRowStatus_Type()
)
hwUserVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwUserVlanCfgRowStatus.setStatus("current")
_HwUserVlanTable_Object = MibTable
hwUserVlanTable = _HwUserVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 3)
)
if mibBuilder.loadTexts:
    hwUserVlanTable.setStatus("current")
_HwUserVlanEntry_Object = MibTableRow
hwUserVlanEntry = _HwUserVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 3, 1)
)
hwUserVlanEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwUserVlanIndex"),
)
if mibBuilder.loadTexts:
    hwUserVlanEntry.setStatus("current")
_HwUserVlanFlowTriggerEnable_Type = EnabledStatus
_HwUserVlanFlowTriggerEnable_Object = MibTableColumn
hwUserVlanFlowTriggerEnable = _HwUserVlanFlowTriggerEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 3, 1, 1),
    _HwUserVlanFlowTriggerEnable_Type()
)
hwUserVlanFlowTriggerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserVlanFlowTriggerEnable.setStatus("current")
_HwMcSourceDenyTable_Object = MibTable
hwMcSourceDenyTable = _HwMcSourceDenyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 4)
)
if mibBuilder.loadTexts:
    hwMcSourceDenyTable.setStatus("current")
_HwMcSourceDenyEntry_Object = MibTableRow
hwMcSourceDenyEntry = _HwMcSourceDenyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 4, 1)
)
hwMcSourceDenyEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcSourceDenyVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMcSourceDenyIfIndex"),
)
if mibBuilder.loadTexts:
    hwMcSourceDenyEntry.setStatus("current")
_HwMcSourceDenyVlanIndex_Type = VlanIndex
_HwMcSourceDenyVlanIndex_Object = MibTableColumn
hwMcSourceDenyVlanIndex = _HwMcSourceDenyVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 4, 1, 1),
    _HwMcSourceDenyVlanIndex_Type()
)
hwMcSourceDenyVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcSourceDenyVlanIndex.setStatus("current")
_HwMcSourceDenyIfIndex_Type = InterfaceIndex
_HwMcSourceDenyIfIndex_Object = MibTableColumn
hwMcSourceDenyIfIndex = _HwMcSourceDenyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 4, 1, 2),
    _HwMcSourceDenyIfIndex_Type()
)
hwMcSourceDenyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcSourceDenyIfIndex.setStatus("current")
_HwMcSourceDenyRowStatus_Type = RowStatus
_HwMcSourceDenyRowStatus_Object = MibTableColumn
hwMcSourceDenyRowStatus = _HwMcSourceDenyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 2, 4, 1, 51),
    _HwMcSourceDenyRowStatus_Type()
)
hwMcSourceDenyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcSourceDenyRowStatus.setStatus("current")
_HwMVlanGrpInfo_ObjectIdentity = ObjectIdentity
hwMVlanGrpInfo = _HwMVlanGrpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3)
)
_HwMVlanGrpInfoTable_Object = MibTable
hwMVlanGrpInfoTable = _HwMVlanGrpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hwMVlanGrpInfoTable.setStatus("current")
_HwMVlanGrpInfoEntry_Object = MibTableRow
hwMVlanGrpInfoEntry = _HwMVlanGrpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 1, 1)
)
hwMVlanGrpInfoEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanGrpAddress"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanGrpPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanGrpUserVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMVlanGrpInfoEntry.setStatus("current")
_HwMVlanGrpAddress_Type = IpAddress
_HwMVlanGrpAddress_Object = MibTableColumn
hwMVlanGrpAddress = _HwMVlanGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 1, 1, 1),
    _HwMVlanGrpAddress_Type()
)
hwMVlanGrpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMVlanGrpAddress.setStatus("current")
_HwMVlanGrpPortIfIndex_Type = InterfaceIndex
_HwMVlanGrpPortIfIndex_Object = MibTableColumn
hwMVlanGrpPortIfIndex = _HwMVlanGrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 1, 1, 2),
    _HwMVlanGrpPortIfIndex_Type()
)
hwMVlanGrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanGrpPortIfIndex.setStatus("current")
_HwMVlanGrpUserVlanIndex_Type = VlanIndex
_HwMVlanGrpUserVlanIndex_Object = MibTableColumn
hwMVlanGrpUserVlanIndex = _HwMVlanGrpUserVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 1, 1, 3),
    _HwMVlanGrpUserVlanIndex_Type()
)
hwMVlanGrpUserVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanGrpUserVlanIndex.setStatus("current")
_HwMVlanStaticFlowTable_Object = MibTable
hwMVlanStaticFlowTable = _HwMVlanStaticFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 2)
)
if mibBuilder.loadTexts:
    hwMVlanStaticFlowTable.setStatus("current")
_HwMVlanStaticFlowEntry_Object = MibTableRow
hwMVlanStaticFlowEntry = _HwMVlanStaticFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 2, 1)
)
hwMVlanStaticFlowEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanStaticFlowGrpAddress"),
)
if mibBuilder.loadTexts:
    hwMVlanStaticFlowEntry.setStatus("current")
_HwMVlanStaticFlowGrpAddress_Type = IpAddress
_HwMVlanStaticFlowGrpAddress_Object = MibTableColumn
hwMVlanStaticFlowGrpAddress = _HwMVlanStaticFlowGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 2, 1, 1),
    _HwMVlanStaticFlowGrpAddress_Type()
)
hwMVlanStaticFlowGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanStaticFlowGrpAddress.setStatus("current")
_HwMVlanStaticFlowRowStatus_Type = RowStatus
_HwMVlanStaticFlowRowStatus_Object = MibTableColumn
hwMVlanStaticFlowRowStatus = _HwMVlanStaticFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 2, 1, 2),
    _HwMVlanStaticFlowRowStatus_Type()
)
hwMVlanStaticFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMVlanStaticFlowRowStatus.setStatus("current")
_HwMVlanIpv6StaticFlowTable_Object = MibTable
hwMVlanIpv6StaticFlowTable = _HwMVlanIpv6StaticFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 3)
)
if mibBuilder.loadTexts:
    hwMVlanIpv6StaticFlowTable.setStatus("current")
_HwMVlanIpv6StaticFlowEntry_Object = MibTableRow
hwMVlanIpv6StaticFlowEntry = _HwMVlanIpv6StaticFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 3, 1)
)
hwMVlanIpv6StaticFlowEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanStaticFlowIpv6GrpAddress"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanStaticFlowIpv6SourceAddress"),
)
if mibBuilder.loadTexts:
    hwMVlanIpv6StaticFlowEntry.setStatus("current")
_HwMVlanStaticFlowIpv6GrpAddress_Type = Ipv6Address
_HwMVlanStaticFlowIpv6GrpAddress_Object = MibTableColumn
hwMVlanStaticFlowIpv6GrpAddress = _HwMVlanStaticFlowIpv6GrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 3, 1, 1),
    _HwMVlanStaticFlowIpv6GrpAddress_Type()
)
hwMVlanStaticFlowIpv6GrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanStaticFlowIpv6GrpAddress.setStatus("current")
_HwMVlanStaticFlowIpv6SourceAddress_Type = Ipv6Address
_HwMVlanStaticFlowIpv6SourceAddress_Object = MibTableColumn
hwMVlanStaticFlowIpv6SourceAddress = _HwMVlanStaticFlowIpv6SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 3, 1, 2),
    _HwMVlanStaticFlowIpv6SourceAddress_Type()
)
hwMVlanStaticFlowIpv6SourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMVlanStaticFlowIpv6SourceAddress.setStatus("current")
_HwMVlanIpv6StaticFlowRowStatus_Type = RowStatus
_HwMVlanIpv6StaticFlowRowStatus_Object = MibTableColumn
hwMVlanIpv6StaticFlowRowStatus = _HwMVlanIpv6StaticFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 3, 1, 51),
    _HwMVlanIpv6StaticFlowRowStatus_Type()
)
hwMVlanIpv6StaticFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMVlanIpv6StaticFlowRowStatus.setStatus("current")
_HwExternMVlanStaticFlowTable_Object = MibTable
hwExternMVlanStaticFlowTable = _HwExternMVlanStaticFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 4)
)
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowTable.setStatus("current")
_HwExternMVlanStaticFlowEntry_Object = MibTableRow
hwExternMVlanStaticFlowEntry = _HwExternMVlanStaticFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 4, 1)
)
hwExternMVlanStaticFlowEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternMVlanStaticFlowGrpAddress"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternMVlanStaticFlowSourceAddress"),
)
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowEntry.setStatus("current")
_HwExternMVlanStaticFlowGrpAddress_Type = IpAddress
_HwExternMVlanStaticFlowGrpAddress_Object = MibTableColumn
hwExternMVlanStaticFlowGrpAddress = _HwExternMVlanStaticFlowGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 4, 1, 1),
    _HwExternMVlanStaticFlowGrpAddress_Type()
)
hwExternMVlanStaticFlowGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowGrpAddress.setStatus("current")
_HwExternMVlanStaticFlowSourceAddress_Type = IpAddress
_HwExternMVlanStaticFlowSourceAddress_Object = MibTableColumn
hwExternMVlanStaticFlowSourceAddress = _HwExternMVlanStaticFlowSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 4, 1, 2),
    _HwExternMVlanStaticFlowSourceAddress_Type()
)
hwExternMVlanStaticFlowSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowSourceAddress.setStatus("current")
_HwExternMVlanStaticFlowRowStatus_Type = RowStatus
_HwExternMVlanStaticFlowRowStatus_Object = MibTableColumn
hwExternMVlanStaticFlowRowStatus = _HwExternMVlanStaticFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 3, 3, 4, 1, 51),
    _HwExternMVlanStaticFlowRowStatus_Type()
)
hwExternMVlanStaticFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowRowStatus.setStatus("current")
_HwMultiCastCommonObject_ObjectIdentity = ObjectIdentity
hwMultiCastCommonObject = _HwMultiCastCommonObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 4)
)
_HwMCSystemInfo_ObjectIdentity = ObjectIdentity
hwMCSystemInfo = _HwMCSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 4, 1)
)
_HwEthTrunkLoadBalancingEnabled_Type = EnabledStatus
_HwEthTrunkLoadBalancingEnabled_Object = MibScalar
hwEthTrunkLoadBalancingEnabled = _HwEthTrunkLoadBalancingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 4, 1, 1),
    _HwEthTrunkLoadBalancingEnabled_Type()
)
hwEthTrunkLoadBalancingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEthTrunkLoadBalancingEnabled.setStatus("current")
_HwL2CacTrapObject_ObjectIdentity = ObjectIdentity
hwL2CacTrapObject = _HwL2CacTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5)
)
_HwL2mcCacCount_Type = Integer32
_HwL2mcCacCount_Object = MibScalar
hwL2mcCacCount = _HwL2mcCacCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 1),
    _HwL2mcCacCount_Type()
)
hwL2mcCacCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacCount.setStatus("current")
_HwL2mcCacBandwidth_Type = Unsigned32
_HwL2mcCacBandwidth_Object = MibScalar
hwL2mcCacBandwidth = _HwL2mcCacBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 2),
    _HwL2mcCacBandwidth_Type()
)
hwL2mcCacBandwidth.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacBandwidth.setStatus("current")
_HwL2mcCacGroupAddress_Type = IpAddress
_HwL2mcCacGroupAddress_Object = MibScalar
hwL2mcCacGroupAddress = _HwL2mcCacGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 3),
    _HwL2mcCacGroupAddress_Type()
)
hwL2mcCacGroupAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacGroupAddress.setStatus("current")
_HwL2mcCacChannelName_Type = DisplayString
_HwL2mcCacChannelName_Object = MibScalar
hwL2mcCacChannelName = _HwL2mcCacChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 4),
    _HwL2mcCacChannelName_Type()
)
hwL2mcCacChannelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacChannelName.setStatus("current")
_HwL2mcCacVlanIndex_Type = Integer32
_HwL2mcCacVlanIndex_Object = MibScalar
hwL2mcCacVlanIndex = _HwL2mcCacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 5),
    _HwL2mcCacVlanIndex_Type()
)
hwL2mcCacVlanIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacVlanIndex.setStatus("current")
_HwL2mcCacVsiName_Type = DisplayString
_HwL2mcCacVsiName_Object = MibScalar
hwL2mcCacVsiName = _HwL2mcCacVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 6),
    _HwL2mcCacVsiName_Type()
)
hwL2mcCacVsiName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacVsiName.setStatus("current")
_HwL2mcCacIfIndex_Type = InterfaceIndex
_HwL2mcCacIfIndex_Object = MibScalar
hwL2mcCacIfIndex = _HwL2mcCacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 7),
    _HwL2mcCacIfIndex_Type()
)
hwL2mcCacIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacIfIndex.setStatus("current")
_HwL2mcCacPwId_Type = Unsigned32
_HwL2mcCacPwId_Object = MibScalar
hwL2mcCacPwId = _HwL2mcCacPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 8),
    _HwL2mcCacPwId_Type()
)
hwL2mcCacPwId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacPwId.setStatus("current")
_HwL2mcCacRemoteIpAddress_Type = IpAddress
_HwL2mcCacRemoteIpAddress_Object = MibScalar
hwL2mcCacRemoteIpAddress = _HwL2mcCacRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 9),
    _HwL2mcCacRemoteIpAddress_Type()
)
hwL2mcCacRemoteIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacRemoteIpAddress.setStatus("current")
_HwL2mcCacRemoteSiteId_Type = Integer32
_HwL2mcCacRemoteSiteId_Object = MibScalar
hwL2mcCacRemoteSiteId = _HwL2mcCacRemoteSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 5, 10),
    _HwL2mcCacRemoteSiteId_Type()
)
hwL2mcCacRemoteSiteId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2mcCacRemoteSiteId.setStatus("current")
_HwBtvMibObject_ObjectIdentity = ObjectIdentity
hwBtvMibObject = _HwBtvMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6)
)
_HwBtvSystemInfo_ObjectIdentity = ObjectIdentity
hwBtvSystemInfo = _HwBtvSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 1)
)
_HwBtvEnabled_Type = EnabledStatus
_HwBtvEnabled_Object = MibScalar
hwBtvEnabled = _HwBtvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 1, 1),
    _HwBtvEnabled_Type()
)
hwBtvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBtvEnabled.setStatus("current")
_HwBtvCfgInfo_ObjectIdentity = ObjectIdentity
hwBtvCfgInfo = _HwBtvCfgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2)
)
_HwMcastGroupTable_Object = MibTable
hwMcastGroupTable = _HwMcastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hwMcastGroupTable.setStatus("current")
_HwMcastGroupEntry_Object = MibTableRow
hwMcastGroupEntry = _HwMcastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1)
)
hwMcastGroupEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastGroupIndex"),
)
if mibBuilder.loadTexts:
    hwMcastGroupEntry.setStatus("current")


class _HwMcastGroupIndex_Type(Integer32):
    """Custom type hwMcastGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMcastGroupIndex_Type.__name__ = "Integer32"
_HwMcastGroupIndex_Object = MibTableColumn
hwMcastGroupIndex = _HwMcastGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1, 1),
    _HwMcastGroupIndex_Type()
)
hwMcastGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcastGroupIndex.setStatus("current")
_HwMcastGroupName_Type = DisplayString
_HwMcastGroupName_Object = MibTableColumn
hwMcastGroupName = _HwMcastGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1, 2),
    _HwMcastGroupName_Type()
)
hwMcastGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastGroupName.setStatus("current")
_HwMcastGroupAddress_Type = IpAddress
_HwMcastGroupAddress_Object = MibTableColumn
hwMcastGroupAddress = _HwMcastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1, 3),
    _HwMcastGroupAddress_Type()
)
hwMcastGroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastGroupAddress.setStatus("current")
_HwMcastGroupRowStatus_Type = RowStatus
_HwMcastGroupRowStatus_Object = MibTableColumn
hwMcastGroupRowStatus = _HwMcastGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1, 4),
    _HwMcastGroupRowStatus_Type()
)
hwMcastGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastGroupRowStatus.setStatus("current")
_HwMcastSourceAddress_Type = IpAddress
_HwMcastSourceAddress_Object = MibTableColumn
hwMcastSourceAddress = _HwMcastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 1, 1, 5),
    _HwMcastSourceAddress_Type()
)
hwMcastSourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastSourceAddress.setStatus("current")
_HwMcastListTable_Object = MibTable
hwMcastListTable = _HwMcastListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwMcastListTable.setStatus("current")
_HwMcastListEntry_Object = MibTableRow
hwMcastListEntry = _HwMcastListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 2, 1)
)
hwMcastListEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastListIndex"),
)
if mibBuilder.loadTexts:
    hwMcastListEntry.setStatus("current")


class _HwMcastListIndex_Type(Integer32):
    """Custom type hwMcastListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwMcastListIndex_Type.__name__ = "Integer32"
_HwMcastListIndex_Object = MibTableColumn
hwMcastListIndex = _HwMcastListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 2, 1, 1),
    _HwMcastListIndex_Type()
)
hwMcastListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcastListIndex.setStatus("current")
_HwMcastListName_Type = DisplayString
_HwMcastListName_Object = MibTableColumn
hwMcastListName = _HwMcastListName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 2, 1, 2),
    _HwMcastListName_Type()
)
hwMcastListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastListName.setStatus("current")
_HwMcastListRowStatus_Type = RowStatus
_HwMcastListRowStatus_Object = MibTableColumn
hwMcastListRowStatus = _HwMcastListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 2, 1, 3),
    _HwMcastListRowStatus_Type()
)
hwMcastListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastListRowStatus.setStatus("current")
_HwMcastProfileTable_Object = MibTable
hwMcastProfileTable = _HwMcastProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 3)
)
if mibBuilder.loadTexts:
    hwMcastProfileTable.setStatus("current")
_HwMcastProfileEntry_Object = MibTableRow
hwMcastProfileEntry = _HwMcastProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 3, 1)
)
hwMcastProfileEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastProfileIndex"),
)
if mibBuilder.loadTexts:
    hwMcastProfileEntry.setStatus("current")


class _HwMcastProfileIndex_Type(Integer32):
    """Custom type hwMcastProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwMcastProfileIndex_Type.__name__ = "Integer32"
_HwMcastProfileIndex_Object = MibTableColumn
hwMcastProfileIndex = _HwMcastProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 3, 1, 1),
    _HwMcastProfileIndex_Type()
)
hwMcastProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcastProfileIndex.setStatus("current")
_HwMcastProfileName_Type = DisplayString
_HwMcastProfileName_Object = MibTableColumn
hwMcastProfileName = _HwMcastProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 3, 1, 2),
    _HwMcastProfileName_Type()
)
hwMcastProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastProfileName.setStatus("current")
_HwMcastProfileRowStatus_Type = RowStatus
_HwMcastProfileRowStatus_Object = MibTableColumn
hwMcastProfileRowStatus = _HwMcastProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 3, 1, 3),
    _HwMcastProfileRowStatus_Type()
)
hwMcastProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastProfileRowStatus.setStatus("current")
_HwMcastProfileCfgTable_Object = MibTable
hwMcastProfileCfgTable = _HwMcastProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4)
)
if mibBuilder.loadTexts:
    hwMcastProfileCfgTable.setStatus("current")
_HwMcastProfileCfgEntry_Object = MibTableRow
hwMcastProfileCfgEntry = _HwMcastProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4, 1)
)
hwMcastProfileCfgEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastProfileIndex"),
)
if mibBuilder.loadTexts:
    hwMcastProfileCfgEntry.setStatus("current")
_HwMcastProfileCfgPreviewTimes_Type = Integer32
_HwMcastProfileCfgPreviewTimes_Object = MibTableColumn
hwMcastProfileCfgPreviewTimes = _HwMcastProfileCfgPreviewTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4, 1, 1),
    _HwMcastProfileCfgPreviewTimes_Type()
)
hwMcastProfileCfgPreviewTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMcastProfileCfgPreviewTimes.setStatus("current")
_HwMcastProfileCfgPreviewMinute_Type = Integer32
_HwMcastProfileCfgPreviewMinute_Object = MibTableColumn
hwMcastProfileCfgPreviewMinute = _HwMcastProfileCfgPreviewMinute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4, 1, 2),
    _HwMcastProfileCfgPreviewMinute_Type()
)
hwMcastProfileCfgPreviewMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMcastProfileCfgPreviewMinute.setStatus("current")
_HwMcastProfileCfgPreviewInterval_Type = Integer32
_HwMcastProfileCfgPreviewInterval_Object = MibTableColumn
hwMcastProfileCfgPreviewInterval = _HwMcastProfileCfgPreviewInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4, 1, 3),
    _HwMcastProfileCfgPreviewInterval_Type()
)
hwMcastProfileCfgPreviewInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMcastProfileCfgPreviewInterval.setStatus("current")
_HwMcastProfileCfgMaxNumProgram_Type = Integer32
_HwMcastProfileCfgMaxNumProgram_Object = MibTableColumn
hwMcastProfileCfgMaxNumProgram = _HwMcastProfileCfgMaxNumProgram_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 4, 1, 4),
    _HwMcastProfileCfgMaxNumProgram_Type()
)
hwMcastProfileCfgMaxNumProgram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMcastProfileCfgMaxNumProgram.setStatus("current")
_HwMcastListReferTable_Object = MibTable
hwMcastListReferTable = _HwMcastListReferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 5)
)
if mibBuilder.loadTexts:
    hwMcastListReferTable.setStatus("current")
_HwMcastListReferEntry_Object = MibTableRow
hwMcastListReferEntry = _HwMcastListReferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 5, 1)
)
hwMcastListReferEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastListIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastGroupIndex"),
)
if mibBuilder.loadTexts:
    hwMcastListReferEntry.setStatus("current")
_HwMcastListReferRowStatus_Type = RowStatus
_HwMcastListReferRowStatus_Object = MibTableColumn
hwMcastListReferRowStatus = _HwMcastListReferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 5, 1, 5),
    _HwMcastListReferRowStatus_Type()
)
hwMcastListReferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastListReferRowStatus.setStatus("current")
_HwMcastProfileReferTable_Object = MibTable
hwMcastProfileReferTable = _HwMcastProfileReferTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 6)
)
if mibBuilder.loadTexts:
    hwMcastProfileReferTable.setStatus("current")
_HwMcastProfileReferEntry_Object = MibTableRow
hwMcastProfileReferEntry = _HwMcastProfileReferEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 6, 1)
)
hwMcastProfileReferEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastProfileIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastListIndex"),
)
if mibBuilder.loadTexts:
    hwMcastProfileReferEntry.setStatus("current")
_HwMcastPreviewStatus_Type = EnabledStatus
_HwMcastPreviewStatus_Object = MibTableColumn
hwMcastPreviewStatus = _HwMcastPreviewStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 6, 1, 1),
    _HwMcastPreviewStatus_Type()
)
hwMcastPreviewStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastPreviewStatus.setStatus("current")
_HwMcastProfileReferRowStatus_Type = RowStatus
_HwMcastProfileReferRowStatus_Object = MibTableColumn
hwMcastProfileReferRowStatus = _HwMcastProfileReferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 6, 1, 5),
    _HwMcastProfileReferRowStatus_Type()
)
hwMcastProfileReferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastProfileReferRowStatus.setStatus("current")
_HwVlanApplyProfileTable_Object = MibTable
hwVlanApplyProfileTable = _HwVlanApplyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 7)
)
if mibBuilder.loadTexts:
    hwVlanApplyProfileTable.setStatus("current")
_HwVlanApplyProfileEntry_Object = MibTableRow
hwVlanApplyProfileEntry = _HwVlanApplyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 7, 1)
)
hwVlanApplyProfileEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwUserVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastProfileIndex"),
)
if mibBuilder.loadTexts:
    hwVlanApplyProfileEntry.setStatus("current")
_HwVlanApplyProfileRowStatus_Type = RowStatus
_HwVlanApplyProfileRowStatus_Object = MibTableColumn
hwVlanApplyProfileRowStatus = _HwVlanApplyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 7, 1, 5),
    _HwVlanApplyProfileRowStatus_Type()
)
hwVlanApplyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVlanApplyProfileRowStatus.setStatus("current")
_HwMcastIpv6GroupTable_Object = MibTable
hwMcastIpv6GroupTable = _HwMcastIpv6GroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8)
)
if mibBuilder.loadTexts:
    hwMcastIpv6GroupTable.setStatus("current")
_HwMcastIpv6GroupEntry_Object = MibTableRow
hwMcastIpv6GroupEntry = _HwMcastIpv6GroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1)
)
hwMcastIpv6GroupEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastIpv6GroupIndex"),
)
if mibBuilder.loadTexts:
    hwMcastIpv6GroupEntry.setStatus("current")


class _HwMcastIpv6GroupIndex_Type(Integer32):
    """Custom type hwMcastIpv6GroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwMcastIpv6GroupIndex_Type.__name__ = "Integer32"
_HwMcastIpv6GroupIndex_Object = MibTableColumn
hwMcastIpv6GroupIndex = _HwMcastIpv6GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1, 1),
    _HwMcastIpv6GroupIndex_Type()
)
hwMcastIpv6GroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMcastIpv6GroupIndex.setStatus("current")
_HwMcastIpv6GroupName_Type = DisplayString
_HwMcastIpv6GroupName_Object = MibTableColumn
hwMcastIpv6GroupName = _HwMcastIpv6GroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1, 2),
    _HwMcastIpv6GroupName_Type()
)
hwMcastIpv6GroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastIpv6GroupName.setStatus("current")
_HwMcastIpv6GroupAddress_Type = Ipv6Address
_HwMcastIpv6GroupAddress_Object = MibTableColumn
hwMcastIpv6GroupAddress = _HwMcastIpv6GroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1, 3),
    _HwMcastIpv6GroupAddress_Type()
)
hwMcastIpv6GroupAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastIpv6GroupAddress.setStatus("current")
_HwMcastIpv6SourceAddress_Type = Ipv6Address
_HwMcastIpv6SourceAddress_Object = MibTableColumn
hwMcastIpv6SourceAddress = _HwMcastIpv6SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1, 4),
    _HwMcastIpv6SourceAddress_Type()
)
hwMcastIpv6SourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastIpv6SourceAddress.setStatus("current")
_HwMcastIpv6GroupRowStatus_Type = RowStatus
_HwMcastIpv6GroupRowStatus_Object = MibTableColumn
hwMcastIpv6GroupRowStatus = _HwMcastIpv6GroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 8, 1, 51),
    _HwMcastIpv6GroupRowStatus_Type()
)
hwMcastIpv6GroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMcastIpv6GroupRowStatus.setStatus("current")
_HwExternVlanApplyProfileTable_Object = MibTable
hwExternVlanApplyProfileTable = _HwExternVlanApplyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 9)
)
if mibBuilder.loadTexts:
    hwExternVlanApplyProfileTable.setStatus("current")
_HwExternVlanApplyProfileEntry_Object = MibTableRow
hwExternVlanApplyProfileEntry = _HwExternVlanApplyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 9, 1)
)
hwExternVlanApplyProfileEntry.setIndexNames(
    (0, "HUAWEI-MULTICAST-MIB", "hwUserVlanIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwMcastProfileIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternPortIfIndex"),
    (0, "HUAWEI-MULTICAST-MIB", "hwExternSourceMacAddress"),
)
if mibBuilder.loadTexts:
    hwExternVlanApplyProfileEntry.setStatus("current")
_HwExternPortIfIndex_Type = InterfaceIndex
_HwExternPortIfIndex_Object = MibTableColumn
hwExternPortIfIndex = _HwExternPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 9, 1, 1),
    _HwExternPortIfIndex_Type()
)
hwExternPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternPortIfIndex.setStatus("current")
_HwExternSourceMacAddress_Type = MacAddress
_HwExternSourceMacAddress_Object = MibTableColumn
hwExternSourceMacAddress = _HwExternSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 9, 1, 2),
    _HwExternSourceMacAddress_Type()
)
hwExternSourceMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwExternSourceMacAddress.setStatus("current")
_HwExternVlanApplyProfileRowStatus_Type = RowStatus
_HwExternVlanApplyProfileRowStatus_Object = MibTableColumn
hwExternVlanApplyProfileRowStatus = _HwExternVlanApplyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 6, 2, 9, 1, 51),
    _HwExternVlanApplyProfileRowStatus_Type()
)
hwExternVlanApplyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwExternVlanApplyProfileRowStatus.setStatus("current")
_HwMcastAlarmObject_ObjectIdentity = ObjectIdentity
hwMcastAlarmObject = _HwMcastAlarmObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99)
)
_HwMCMibConformance_ObjectIdentity = ObjectIdentity
hwMCMibConformance = _HwMCMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100)
)
_HwMCMibCompliances_ObjectIdentity = ObjectIdentity
hwMCMibCompliances = _HwMCMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 1)
)
_HwMCMibGroups_ObjectIdentity = ObjectIdentity
hwMCMibGroups = _HwMCMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2)
)

# Managed Objects groups

hwIGSPSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 1)
)
hwIGSPSystemInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwIgmpSnoopingEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwSsmPolicyAclNum"),
        ("HUAWEI-MULTICAST-MIB", "hwSendQueryEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwSendQuerySourceIpAddr"),
        ("HUAWEI-MULTICAST-MIB", "hwSnmpTrapEnable"),
        ("HUAWEI-MULTICAST-MIB", "hwIgmpSnoopingSuppressionTime"),
        ("HUAWEI-MULTICAST-MIB", "hwIgmpProxyEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwIgmpSnoopingProxyEnabled"))
)
if mibBuilder.loadTexts:
    hwIGSPSystemInfoGroup.setStatus("current")

hwVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 2)
)
hwVlanCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanIgmpSnoopingEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRouterAgingTime"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanMaxQueryRespTime"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanLastMemQueryInt"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanQueryInt"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRobustCount"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanCheckRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanSendRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIgmpVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanPromptLeaveEnable"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanPromptLeaveAclNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanDropUnknown"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanLimitAction"))
)
if mibBuilder.loadTexts:
    hwVlanCfgGroup.setStatus("current")

hwSystemStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 3)
)
hwSystemStatisticsGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwSystemRecvVlanUpEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvVlanDownEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvVlanDelEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvPortUpEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvPortDownEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvPortDelEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvPortIncEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvPortExcEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvMSTPBlockEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvMSTPForwardEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemIGMPSysClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemIGMPPacketClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwSystemRecvLinkChangeEventTimes"))
)
if mibBuilder.loadTexts:
    hwSystemStatisticsGroup.setStatus("current")

hwVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 4)
)
hwVlanStatisticsGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV1ReportNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV2ReportNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV3ReportNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPLeaveNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV1QueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV2QueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIGMPV3QueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvPimHelloNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanSendQueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIGMPPacketClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanSendSourceIPSpecQueryNum"))
)
if mibBuilder.loadTexts:
    hwVlanStatisticsGroup.setStatus("current")

hwIPGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 5)
)
hwIPGrpInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwIPGrpUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwIPHostUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwIPHostExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwIPHostFlags"),
        ("HUAWEI-MULTICAST-MIB", "hwIPRtUPTime"),
        ("HUAWEI-MULTICAST-MIB", "hwIPRtExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwIPRtFlags"))
)
if mibBuilder.loadTexts:
    hwIPGrpInfoGroup.setStatus("current")

hwMACGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 6)
)
hwMACGrpInfoGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMACGrpAddress")
)
if mibBuilder.loadTexts:
    hwMACGrpInfoGroup.setStatus("current")

hwPortStaticGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 7)
)
hwPortStaticGrpGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwPortStaticGrpRowStatus")
)
if mibBuilder.loadTexts:
    hwPortStaticGrpGroup.setStatus("current")

hwGrpPolicyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 8)
)
hwGrpPolicyCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwGrpPolicyAclNum"),
        ("HUAWEI-MULTICAST-MIB", "hwGrpPolicyIgmpVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwGrpPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwGrpPolicyCfgGroup.setStatus("current")

hwRouterPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 9)
)
hwRouterPortInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwRouterPortUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwRouterPortExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwRouterPortFlags"))
)
if mibBuilder.loadTexts:
    hwRouterPortInfoGroup.setStatus("current")

hwRouterPortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 10)
)
hwRouterPortCfgGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwRouterPortCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwRouterPortCfgGroup.setStatus("current")

hwPortLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 11)
)
hwPortLimitGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwPortLimitNumber"),
        ("HUAWEI-MULTICAST-MIB", "hwPortLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwPortLimitGroup.setStatus("current")

hwMVlanSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 13)
)
hwMVlanSystemGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMVlanEnabled")
)
if mibBuilder.loadTexts:
    hwMVlanSystemGroup.setStatus("current")

hwMVlanEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 14)
)
hwMVlanEnableGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMVlanStatus")
)
if mibBuilder.loadTexts:
    hwMVlanEnableGroup.setStatus("current")

hwMVlanUserVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 15)
)
hwMVlanUserVlanGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwUserVlanCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwMVlanUserVlanGroup.setStatus("current")

hwMVlanGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 16)
)
hwMVlanGrpInfoGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMVlanGrpAddress")
)
if mibBuilder.loadTexts:
    hwMVlanGrpInfoGroup.setStatus("current")

hwMCastSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 18)
)
hwMCastSystemGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwEthTrunkLoadBalancingEnabled")
)
if mibBuilder.loadTexts:
    hwMCastSystemGroup.setStatus("current")

hwL2CacTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 19)
)
hwL2CacTrapGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPwId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteSiteId"))
)
if mibBuilder.loadTexts:
    hwL2CacTrapGroup.setStatus("current")

hwVlanIgmpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 20)
)
hwVlanIgmpProxyGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanIgmpProxyEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanQueryInterval"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanMaxResponseTime"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanLastMemQueryInterval"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIgmpRouterAgingTime"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanMaxIgmpVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIgmpRobustCount"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRequireRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIgmpSendRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanIgmpPromptLeaveEnable"))
)
if mibBuilder.loadTexts:
    hwVlanIgmpProxyGroup.setStatus("current")

hwL2McastVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 21)
)
hwL2McastVlanCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanL2FlowTriggerEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanL2StaticFlow"))
)
if mibBuilder.loadTexts:
    hwL2McastVlanCfgGroup.setStatus("current")

hwGrpMcastCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 22)
)
hwGrpMcastCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwGrpIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwGrpRowStatus"))
)
if mibBuilder.loadTexts:
    hwGrpMcastCfgGroup.setStatus("current")

hwVlanMcastGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 23)
)
hwVlanMcastGrpGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwVlanMcastProfileName")
)
if mibBuilder.loadTexts:
    hwVlanMcastGrpGroup.setStatus("current")

hwGrpMcastProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 24)
)
hwGrpMcastProfileGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMulticastProfilePreviewTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMulticastProfilePreviewMinutes"),
        ("HUAWEI-MULTICAST-MIB", "hwMulticastProfilePreviewInterval"))
)
if mibBuilder.loadTexts:
    hwGrpMcastProfileGroup.setStatus("current")

hwUserVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 25)
)
hwUserVlanGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwUserVlanFlowTriggerEnable")
)
if mibBuilder.loadTexts:
    hwUserVlanGroup.setStatus("current")

hwMVlanStaticFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 26)
)
hwMVlanStaticFlowGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMVlanStaticFlowRowStatus")
)
if mibBuilder.loadTexts:
    hwMVlanStaticFlowGroup.setStatus("current")

hwBtvSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 27)
)
hwBtvSystemGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwBtvEnabled")
)
if mibBuilder.loadTexts:
    hwBtvSystemGroup.setStatus("current")

hwMcastGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 28)
)
hwMcastGroupGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastGroupName"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastGroupAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastGroupRowStatus"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastSourceAddress"))
)
if mibBuilder.loadTexts:
    hwMcastGroupGroup.setStatus("current")

hwMcastListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 29)
)
hwMcastListGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastListName"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastListRowStatus"))
)
if mibBuilder.loadTexts:
    hwMcastListGroup.setStatus("current")

hwMcastProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 30)
)
hwMcastProfileGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastProfileName"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwMcastProfileGroup.setStatus("current")

hwMcastProfileCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 31)
)
hwMcastProfileCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastProfileCfgPreviewTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastProfileCfgPreviewMinute"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastProfileCfgPreviewInterval"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastProfileCfgMaxNumProgram"))
)
if mibBuilder.loadTexts:
    hwMcastProfileCfgGroup.setStatus("current")

hwMcastListReferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 32)
)
hwMcastListReferGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMcastListReferRowStatus")
)
if mibBuilder.loadTexts:
    hwMcastListReferGroup.setStatus("current")

hwMcastProfileReferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 33)
)
hwMcastProfileReferGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastPreviewStatus"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastProfileReferRowStatus"))
)
if mibBuilder.loadTexts:
    hwMcastProfileReferGroup.setStatus("current")

hwVlanApplyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 34)
)
hwVlanApplyProfileGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwVlanApplyProfileRowStatus")
)
if mibBuilder.loadTexts:
    hwVlanApplyProfileGroup.setStatus("current")

hwPortGroupPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 35)
)
hwPortGroupPolicyGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwPortGroupPolicyAclNumber"),
        ("HUAWEI-MULTICAST-MIB", "hwPortGroupPolicyVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwPortGroupPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwPortGroupPolicyGroup.setStatus("current")

hwMldSnpgSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 36)
)
hwMldSnpgSystemInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldSnoopingEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSendQueryEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSendQuerySourceIpAddr"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSnoopingSuppressionTime"))
)
if mibBuilder.loadTexts:
    hwMldSnpgSystemInfoGroup.setStatus("current")

hwMldVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 37)
)
hwMldVlanCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanMldSnoopingEnabled"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanRouterAgingTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanMaxQueryRespTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanLastListenerQueryInt"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanQueryInt"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanRobustCount"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanCheckRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanSendRouterAlert"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanMldVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanPromptLeaveEnable"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanPromptLeaveAclNum"),
        ("HUAWEI-MULTICAST-MIB", "hwMldVlanDropUnknown"))
)
if mibBuilder.loadTexts:
    hwMldVlanCfgGroup.setStatus("current")

hwMldSystemStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 38)
)
hwMldSystemStatisticsGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvVlanUpEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvVlanDownEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvVlanDelEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvPortUpEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvPortDownEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvPortDelEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvPortIncEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvPortExcEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvMstpBlockEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvMstpForwardEventTimes"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemSysClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemPacketClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwMldSystemRecvLinkChangeEventTimes"))
)
if mibBuilder.loadTexts:
    hwMldSystemStatisticsGroup.setStatus("current")

hwMldVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 39)
)
hwMldVlanStatisticsGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwVlanRecvMldV1ReportNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvMldV2ReportNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvMldDoneNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvMldV1QueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvMldV2QueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanRecvIpv6PimHelloNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanSendMldQueryNum"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanMldPacketClearStats"),
        ("HUAWEI-MULTICAST-MIB", "hwVlanSendSourceIpSpecMldQueryNum"))
)
if mibBuilder.loadTexts:
    hwMldVlanStatisticsGroup.setStatus("current")

hwMldIpGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 40)
)
hwMldIpGrpInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldIpGrpUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpHostUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpHostExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpHostFlag"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpRtUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpRtExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwMldIpRtFlag"))
)
if mibBuilder.loadTexts:
    hwMldIpGrpInfoGroup.setStatus("current")

hwMldPortStaticGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 41)
)
hwMldPortStaticGrpGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMldPortStaticGrpRowStatus")
)
if mibBuilder.loadTexts:
    hwMldPortStaticGrpGroup.setStatus("current")

hwMldGrpPolicyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 42)
)
hwMldGrpPolicyCfgGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldGrpPolicyAclNum"),
        ("HUAWEI-MULTICAST-MIB", "hwGrpPolicyMldVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwMldGrpPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwMldGrpPolicyCfgGroup.setStatus("current")

hwMldRouterPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 43)
)
hwMldRouterPortInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldRouterPortUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwMldRouterPortExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwMldRouterPortFlag"))
)
if mibBuilder.loadTexts:
    hwMldRouterPortInfoGroup.setStatus("current")

hwMldRouterPortCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 44)
)
hwMldRouterPortCfgGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMldRouterPortCfgRowStatus")
)
if mibBuilder.loadTexts:
    hwMldRouterPortCfgGroup.setStatus("current")

hwMldPortLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 45)
)
hwMldPortLimitGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldPortLimitNumber"),
        ("HUAWEI-MULTICAST-MIB", "hwMldPortLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwMldPortLimitGroup.setStatus("current")

hwMldPortGroupPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 46)
)
hwMldPortGroupPolicyGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMldPortGroupPolicyAclNumber"),
        ("HUAWEI-MULTICAST-MIB", "hwMldPortGroupPolicyVersion"),
        ("HUAWEI-MULTICAST-MIB", "hwMldPortGroupPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwMldPortGroupPolicyGroup.setStatus("current")

hwMcSourceDenyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 47)
)
hwMcSourceDenyGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMcSourceDenyRowStatus")
)
if mibBuilder.loadTexts:
    hwMcSourceDenyGroup.setStatus("current")

hwMVlanIpv6StaticFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 48)
)
hwMVlanIpv6StaticFlowGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwMVlanIpv6StaticFlowRowStatus")
)
if mibBuilder.loadTexts:
    hwMVlanIpv6StaticFlowGroup.setStatus("current")

hwMcastIpv6GroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 49)
)
hwMcastIpv6GroupGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwMcastIpv6GroupName"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastIpv6GroupAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastIpv6GroupRowStatus"),
        ("HUAWEI-MULTICAST-MIB", "hwMcastIpv6SourceAddress"))
)
if mibBuilder.loadTexts:
    hwMcastIpv6GroupGroup.setStatus("current")

hwExternIpGrpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 50)
)
hwExternIpGrpInfoGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwExternIpGrpUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpHostUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpHostExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpHostFlag"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpRtUpTime"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpRtExpires"),
        ("HUAWEI-MULTICAST-MIB", "hwExternIpRtFlag"))
)
if mibBuilder.loadTexts:
    hwExternIpGrpInfoGroup.setStatus("current")

hwExternPortStaticGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 51)
)
hwExternPortStaticGrpGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwExternPortStaticGrpRowStatus")
)
if mibBuilder.loadTexts:
    hwExternPortStaticGrpGroup.setStatus("current")

hwPortVlanLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 52)
)
hwPortVlanLimitGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwPortVlanLimitNumber"),
        ("HUAWEI-MULTICAST-MIB", "hwPortVlanLimitRowStatus"))
)
if mibBuilder.loadTexts:
    hwPortVlanLimitGroup.setStatus("current")

hwExternMVlanStaticFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 53)
)
hwExternMVlanStaticFlowGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwExternMVlanStaticFlowRowStatus")
)
if mibBuilder.loadTexts:
    hwExternMVlanStaticFlowGroup.setStatus("current")

hwExternVlanApplyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 54)
)
hwExternVlanApplyProfileGroup.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwExternVlanApplyProfileRowStatus")
)
if mibBuilder.loadTexts:
    hwExternVlanApplyProfileGroup.setStatus("current")


# Notification objects

hwCfgRefreshFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 1)
)
hwCfgRefreshFailAlarm.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr")
)
if mibBuilder.loadTexts:
    hwCfgRefreshFailAlarm.setStatus(
        "current"
    )

hwMCastTableLoadAbnormalNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 2)
)
if mibBuilder.loadTexts:
    hwMCastTableLoadAbnormalNotify.setStatus(
        "current"
    )

hwMCastTableLoadAbnormalResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 3)
)
if mibBuilder.loadTexts:
    hwMCastTableLoadAbnormalResume.setStatus(
        "current"
    )

hwMCastVlanFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 4)
)
hwMCastVlanFailAlarm.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr")
)
if mibBuilder.loadTexts:
    hwMCastVlanFailAlarm.setStatus(
        "current"
    )

hwMCastVlanOkNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 5)
)
hwMCastVlanOkNotify.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr")
)
if mibBuilder.loadTexts:
    hwMCastVlanOkNotify.setStatus(
        "current"
    )

hwMCastApsSwitchAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 6)
)
hwMCastApsSwitchAlarm.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr")
)
if mibBuilder.loadTexts:
    hwMCastApsSwitchAlarm.setStatus(
        "current"
    )

hwMCastApsIdleNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 7)
)
hwMCastApsIdleNotify.setObjects(
    ("HUAWEI-L2VLAN-MIB", "hwL2VlanDescr")
)
if mibBuilder.loadTexts:
    hwMCastApsIdleNotify.setStatus(
        "current"
    )

hwL2mcCacGlobalCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 8)
)
hwL2mcCacGlobalCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacGlobalCountExceed.setStatus(
        "current"
    )

hwL2mcCacGlobalBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 9)
)
hwL2mcCacGlobalBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacGlobalBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacGlobalChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 10)
)
hwL2mcCacGlobalChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacGlobalChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacGlobalChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 11)
)
hwL2mcCacGlobalChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacGlobalChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacVlanCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 12)
)
hwL2mcCacVlanCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVlanCountExceed.setStatus(
        "current"
    )

hwL2mcCacVlanBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 13)
)
hwL2mcCacVlanBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVlanBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacVlanChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 14)
)
hwL2mcCacVlanChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVlanChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacVlanChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 15)
)
hwL2mcCacVlanChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVlanChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacVsiCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 16)
)
hwL2mcCacVsiCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVsiCountExceed.setStatus(
        "current"
    )

hwL2mcCacVsiBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 17)
)
hwL2mcCacVsiBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVsiBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacVsiChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 18)
)
hwL2mcCacVsiChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVsiChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacVsiChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 19)
)
hwL2mcCacVsiChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVsiChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacPortCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 20)
)
hwL2mcCacPortCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortCountExceed.setStatus(
        "current"
    )

hwL2mcCacPortBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 21)
)
hwL2mcCacPortBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacPortChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 22)
)
hwL2mcCacPortChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacPortChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 23)
)
hwL2mcCacPortChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacPortVlanCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 24)
)
hwL2mcCacPortVlanCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortVlanCountExceed.setStatus(
        "current"
    )

hwL2mcCacPortVlanBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 25)
)
hwL2mcCacPortVlanBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortVlanBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacPortVlanChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 26)
)
hwL2mcCacPortVlanChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortVlanChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacPortVlanChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 27)
)
hwL2mcCacPortVlanChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacPortVlanChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacSubIfCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 28)
)
hwL2mcCacSubIfCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacSubIfCountExceed.setStatus(
        "current"
    )

hwL2mcCacSubIfBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 29)
)
hwL2mcCacSubIfBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacSubIfBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacSubIfChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 30)
)
hwL2mcCacSubIfChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacSubIfChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacSubIfChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 31)
)
hwL2mcCacSubIfChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacIfIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacSubIfChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacLdpPwCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 32)
)
hwL2mcCacLdpPwCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacPwId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacLdpPwCountExceed.setStatus(
        "current"
    )

hwL2mcCacLdpPwBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 33)
)
hwL2mcCacLdpPwBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacPwId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacLdpPwBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacLdpPwChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 34)
)
hwL2mcCacLdpPwChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPwId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacLdpPwChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacLdpPwChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 35)
)
hwL2mcCacLdpPwChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPwId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteIpAddress"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacLdpPwChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacBgpPwCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 36)
)
hwL2mcCacBgpPwCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteSiteId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacBgpPwCountExceed.setStatus(
        "current"
    )

hwL2mcCacBgpPwBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 37)
)
hwL2mcCacBgpPwBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteSiteId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacBgpPwBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacBgpPwChannelCountExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 38)
)
hwL2mcCacBgpPwChannelCountExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteSiteId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacCount"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacBgpPwChannelCountExceed.setStatus(
        "current"
    )

hwL2mcCacBgpPwChannelBandwidthExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 39)
)
hwL2mcCacBgpPwChannelBandwidthExceed.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacChannelName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacRemoteSiteId"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBandwidth"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacBgpPwChannelBandwidthExceed.setStatus(
        "current"
    )

hwL2mcCacVlanUnspecifiedChannelDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 40)
)
hwL2mcCacVlanUnspecifiedChannelDeny.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanIndex"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVlanUnspecifiedChannelDeny.setStatus(
        "current"
    )

hwL2mcCacVsiUnspecifiedChannelDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 41)
)
hwL2mcCacVsiUnspecifiedChannelDeny.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiName"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress"))
)
if mibBuilder.loadTexts:
    hwL2mcCacVsiUnspecifiedChannelDeny.setStatus(
        "current"
    )

hwL2mcCacGlobalUnspecifiedChannelDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 99, 42)
)
hwL2mcCacGlobalUnspecifiedChannelDeny.setObjects(
    ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGroupAddress")
)
if mibBuilder.loadTexts:
    hwL2mcCacGlobalUnspecifiedChannelDeny.setStatus(
        "current"
    )


# Notifications groups

hwMcastAlarmGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 2, 99)
)
hwMcastAlarmGroup.setObjects(
      *(("HUAWEI-MULTICAST-MIB", "hwCfgRefreshFailAlarm"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastTableLoadAbnormalNotify"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastTableLoadAbnormalResume"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastVlanFailAlarm"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastVlanOkNotify"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastApsSwitchAlarm"),
        ("HUAWEI-MULTICAST-MIB", "hwMCastApsIdleNotify"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGlobalCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGlobalBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGlobalChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGlobalChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortVlanCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortVlanBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortVlanChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacPortVlanChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacSubIfCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacSubIfBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacSubIfChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacSubIfChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacLdpPwCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacLdpPwBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacLdpPwChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacLdpPwChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBgpPwCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBgpPwBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBgpPwChannelCountExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacBgpPwChannelBandwidthExceed"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVlanUnspecifiedChannelDeny"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacVsiUnspecifiedChannelDeny"),
        ("HUAWEI-MULTICAST-MIB", "hwL2mcCacGlobalUnspecifiedChannelDeny"))
)
if mibBuilder.loadTexts:
    hwMcastAlarmGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIGSPMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 44, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwIGSPMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MULTICAST-MIB",
    **{"EnabledStatus": EnabledStatus,
       "VlanIndex": VlanIndex,
       "VlanIndexOrZero": VlanIndexOrZero,
       "PortFlag": PortFlag,
       "hwMultiCastMIB": hwMultiCastMIB,
       "hwIGSPMibObject": hwIGSPMibObject,
       "hwIGSPSystemInfo": hwIGSPSystemInfo,
       "hwIgmpSnoopingEnabled": hwIgmpSnoopingEnabled,
       "hwSsmPolicyAclNum": hwSsmPolicyAclNum,
       "hwSendQueryEnabled": hwSendQueryEnabled,
       "hwSendQuerySourceIpAddr": hwSendQuerySourceIpAddr,
       "hwSnmpTrapEnable": hwSnmpTrapEnable,
       "hwIgmpSnoopingSuppressionTime": hwIgmpSnoopingSuppressionTime,
       "hwIgmpProxyEnabled": hwIgmpProxyEnabled,
       "hwIgmpSnoopingProxyEnabled": hwIgmpSnoopingProxyEnabled,
       "hwVlanCfgInfo": hwVlanCfgInfo,
       "hwVlanCfgTable": hwVlanCfgTable,
       "hwVlanCfgEntry": hwVlanCfgEntry,
       "hwVlanIndex": hwVlanIndex,
       "hwVlanIgmpSnoopingEnabled": hwVlanIgmpSnoopingEnabled,
       "hwVlanRouterAgingTime": hwVlanRouterAgingTime,
       "hwVlanMaxQueryRespTime": hwVlanMaxQueryRespTime,
       "hwVlanLastMemQueryInt": hwVlanLastMemQueryInt,
       "hwVlanQueryInt": hwVlanQueryInt,
       "hwVlanRobustCount": hwVlanRobustCount,
       "hwVlanCheckRouterAlert": hwVlanCheckRouterAlert,
       "hwVlanSendRouterAlert": hwVlanSendRouterAlert,
       "hwVlanIgmpVersion": hwVlanIgmpVersion,
       "hwVlanPromptLeaveEnable": hwVlanPromptLeaveEnable,
       "hwVlanPromptLeaveAclNum": hwVlanPromptLeaveAclNum,
       "hwVlanDropUnknown": hwVlanDropUnknown,
       "hwVlanLimitAction": hwVlanLimitAction,
       "hwVlanIgmpProxyTable": hwVlanIgmpProxyTable,
       "hwVlanIgmpProxyEntry": hwVlanIgmpProxyEntry,
       "hwVlanIgmpProxyIndex": hwVlanIgmpProxyIndex,
       "hwVlanIgmpProxyEnabled": hwVlanIgmpProxyEnabled,
       "hwVlanQueryInterval": hwVlanQueryInterval,
       "hwVlanMaxResponseTime": hwVlanMaxResponseTime,
       "hwVlanLastMemQueryInterval": hwVlanLastMemQueryInterval,
       "hwVlanIgmpRouterAgingTime": hwVlanIgmpRouterAgingTime,
       "hwVlanMaxIgmpVersion": hwVlanMaxIgmpVersion,
       "hwVlanIgmpRobustCount": hwVlanIgmpRobustCount,
       "hwVlanRequireRouterAlert": hwVlanRequireRouterAlert,
       "hwVlanIgmpSendRouterAlert": hwVlanIgmpSendRouterAlert,
       "hwVlanIgmpPromptLeaveEnable": hwVlanIgmpPromptLeaveEnable,
       "hwL2McastVlanCfgTable": hwL2McastVlanCfgTable,
       "hwL2McastVlanCfgEntry": hwL2McastVlanCfgEntry,
       "hwL2McastVlanIndex": hwL2McastVlanIndex,
       "hwVlanL2FlowTriggerEnabled": hwVlanL2FlowTriggerEnabled,
       "hwVlanL2StaticFlow": hwVlanL2StaticFlow,
       "hwStatisticsInfo": hwStatisticsInfo,
       "hwSystemStatisticsInfo": hwSystemStatisticsInfo,
       "hwSystemRecvVlanUpEventTimes": hwSystemRecvVlanUpEventTimes,
       "hwSystemRecvVlanDownEventTimes": hwSystemRecvVlanDownEventTimes,
       "hwSystemRecvVlanDelEventTimes": hwSystemRecvVlanDelEventTimes,
       "hwSystemRecvPortUpEventTimes": hwSystemRecvPortUpEventTimes,
       "hwSystemRecvPortDownEventTimes": hwSystemRecvPortDownEventTimes,
       "hwSystemRecvPortDelEventTimes": hwSystemRecvPortDelEventTimes,
       "hwSystemRecvPortIncEventTimes": hwSystemRecvPortIncEventTimes,
       "hwSystemRecvPortExcEventTimes": hwSystemRecvPortExcEventTimes,
       "hwSystemRecvMSTPBlockEventTimes": hwSystemRecvMSTPBlockEventTimes,
       "hwSystemRecvMSTPForwardEventTimes": hwSystemRecvMSTPForwardEventTimes,
       "hwSystemIGMPSysClearStats": hwSystemIGMPSysClearStats,
       "hwSystemIGMPPacketClearStats": hwSystemIGMPPacketClearStats,
       "hwSystemRecvLinkChangeEventTimes": hwSystemRecvLinkChangeEventTimes,
       "hwVlanStatisticsTable": hwVlanStatisticsTable,
       "hwVlanStatisticsEntry": hwVlanStatisticsEntry,
       "hwVlanStatsVlanIndex": hwVlanStatsVlanIndex,
       "hwVlanRecvIGMPV1ReportNum": hwVlanRecvIGMPV1ReportNum,
       "hwVlanRecvIGMPV2ReportNum": hwVlanRecvIGMPV2ReportNum,
       "hwVlanRecvIGMPV3ReportNum": hwVlanRecvIGMPV3ReportNum,
       "hwVlanRecvIGMPLeaveNum": hwVlanRecvIGMPLeaveNum,
       "hwVlanRecvIGMPV1QueryNum": hwVlanRecvIGMPV1QueryNum,
       "hwVlanRecvIGMPV2QueryNum": hwVlanRecvIGMPV2QueryNum,
       "hwVlanRecvIGMPV3QueryNum": hwVlanRecvIGMPV3QueryNum,
       "hwVlanRecvPimHelloNum": hwVlanRecvPimHelloNum,
       "hwVlanSendQueryNum": hwVlanSendQueryNum,
       "hwVlanIGMPPacketClearStats": hwVlanIGMPPacketClearStats,
       "hwVlanSendSourceIPSpecQueryNum": hwVlanSendSourceIPSpecQueryNum,
       "hwMCGrpInfo": hwMCGrpInfo,
       "hwIPGrpInfoTable": hwIPGrpInfoTable,
       "hwIPGrpInfoEntry": hwIPGrpInfoEntry,
       "hwIPGrpVlanIndex": hwIPGrpVlanIndex,
       "hwIPGrpPortIfIndex": hwIPGrpPortIfIndex,
       "hwIPGrpAddress": hwIPGrpAddress,
       "hwIPGrpUpTime": hwIPGrpUpTime,
       "hwIPHostUpTime": hwIPHostUpTime,
       "hwIPHostExpires": hwIPHostExpires,
       "hwIPHostFlags": hwIPHostFlags,
       "hwIPRtUPTime": hwIPRtUPTime,
       "hwIPRtExpires": hwIPRtExpires,
       "hwIPRtFlags": hwIPRtFlags,
       "hwMACGrpInfoTable": hwMACGrpInfoTable,
       "hwMACGrpInfoEntry": hwMACGrpInfoEntry,
       "hwMACGrpVlanIndex": hwMACGrpVlanIndex,
       "hwMACGrpPortIfIndex": hwMACGrpPortIfIndex,
       "hwMACGrpAddress": hwMACGrpAddress,
       "hwMcastGrpCfgTable": hwMcastGrpCfgTable,
       "hwMcastGrpCfgEntry": hwMcastGrpCfgEntry,
       "hwGrpProfileNameIndex": hwGrpProfileNameIndex,
       "hwGrpListNameIndex": hwGrpListNameIndex,
       "hwGrpNameIndex": hwGrpNameIndex,
       "hwGrpIpAddress": hwGrpIpAddress,
       "hwGrpRowStatus": hwGrpRowStatus,
       "hwVlanMcastGrpTable": hwVlanMcastGrpTable,
       "hwVlanMcastGrpEntry": hwVlanMcastGrpEntry,
       "hwVlanMcastIndex": hwVlanMcastIndex,
       "hwVlanMcastProfileName": hwVlanMcastProfileName,
       "hwMcastGrpProfileTable": hwMcastGrpProfileTable,
       "hwMcastGrpProfileEntry": hwMcastGrpProfileEntry,
       "hwVlanMulticastProfileName": hwVlanMulticastProfileName,
       "hwMulticastProfilePreviewTimes": hwMulticastProfilePreviewTimes,
       "hwMulticastProfilePreviewMinutes": hwMulticastProfilePreviewMinutes,
       "hwMulticastProfilePreviewInterval": hwMulticastProfilePreviewInterval,
       "hwExternIpGrpInfoTable": hwExternIpGrpInfoTable,
       "hwExternIpGrpInfoEntry": hwExternIpGrpInfoEntry,
       "hwExternIpGrpVlanIndex": hwExternIpGrpVlanIndex,
       "hwExternIpGrpPortIfIndex": hwExternIpGrpPortIfIndex,
       "hwExternIpGrpAddress": hwExternIpGrpAddress,
       "hwExternIpGrpUpTime": hwExternIpGrpUpTime,
       "hwExternIpHostUpTime": hwExternIpHostUpTime,
       "hwExternIpHostExpires": hwExternIpHostExpires,
       "hwExternIpHostFlag": hwExternIpHostFlag,
       "hwExternIpRtUpTime": hwExternIpRtUpTime,
       "hwExternIpRtExpires": hwExternIpRtExpires,
       "hwExternIpRtFlag": hwExternIpRtFlag,
       "hwExternIpSourceAddress": hwExternIpSourceAddress,
       "hwPortInfo": hwPortInfo,
       "hwPortStaticGrpTable": hwPortStaticGrpTable,
       "hwPortStaticGrpEntry": hwPortStaticGrpEntry,
       "hwPortStaticGrpVlanIndex": hwPortStaticGrpVlanIndex,
       "hwPortStaticGrpIfIndex": hwPortStaticGrpIfIndex,
       "hwPortStaticGrpAddr": hwPortStaticGrpAddr,
       "hwPortStaticGrpRowStatus": hwPortStaticGrpRowStatus,
       "hwGrpPolicyCfgTable": hwGrpPolicyCfgTable,
       "hwGrpPolicyCfgEntry": hwGrpPolicyCfgEntry,
       "hwGrpPolicyVlanIndex": hwGrpPolicyVlanIndex,
       "hwGrpPolicyAclNum": hwGrpPolicyAclNum,
       "hwGrpPolicyIgmpVersion": hwGrpPolicyIgmpVersion,
       "hwGrpPolicyRowStatus": hwGrpPolicyRowStatus,
       "hwRouterPortInfoTable": hwRouterPortInfoTable,
       "hwRouterPortInfoEntry": hwRouterPortInfoEntry,
       "hwRouterPortVlanIndex": hwRouterPortVlanIndex,
       "hwRouterPortIfIndex": hwRouterPortIfIndex,
       "hwRouterPortUpTime": hwRouterPortUpTime,
       "hwRouterPortExpires": hwRouterPortExpires,
       "hwRouterPortFlags": hwRouterPortFlags,
       "hwRouterPortCfgTable": hwRouterPortCfgTable,
       "hwRouterPortCfgEntry": hwRouterPortCfgEntry,
       "hwRouterPortCfgVlanIndex": hwRouterPortCfgVlanIndex,
       "hwRouterPortCfgIfIndex": hwRouterPortCfgIfIndex,
       "hwRouterPortCfgRowStatus": hwRouterPortCfgRowStatus,
       "hwPortLimitTable": hwPortLimitTable,
       "hwPortLimitEntry": hwPortLimitEntry,
       "hwPortLimitIfIndex": hwPortLimitIfIndex,
       "hwPortLimitNumber": hwPortLimitNumber,
       "hwPortLimitRowStatus": hwPortLimitRowStatus,
       "hwPortGroupPolicyTable": hwPortGroupPolicyTable,
       "hwPortGroupPolicyEntry": hwPortGroupPolicyEntry,
       "hwPortGroupPolicyIfIndex": hwPortGroupPolicyIfIndex,
       "hwPortGroupPolicyAclNumber": hwPortGroupPolicyAclNumber,
       "hwPortGroupPolicyVlanIndex": hwPortGroupPolicyVlanIndex,
       "hwPortGroupPolicyVersion": hwPortGroupPolicyVersion,
       "hwPortGroupPolicyRowStatus": hwPortGroupPolicyRowStatus,
       "hwExternPortStaticGrpTable": hwExternPortStaticGrpTable,
       "hwExternPortStaticGrpEntry": hwExternPortStaticGrpEntry,
       "hwExternPortStaticGrpVlanIndex": hwExternPortStaticGrpVlanIndex,
       "hwExternPortStaticGrpIfIndex": hwExternPortStaticGrpIfIndex,
       "hwExternPortStaticGroupAddr": hwExternPortStaticGroupAddr,
       "hwExternPortStaticSourceAddr": hwExternPortStaticSourceAddr,
       "hwExternPortStaticGrpRowStatus": hwExternPortStaticGrpRowStatus,
       "hwPortVlanLimitTable": hwPortVlanLimitTable,
       "hwPortVlanLimitEntry": hwPortVlanLimitEntry,
       "hwPortVlanLimitIfIndex": hwPortVlanLimitIfIndex,
       "hwPortVlanLimitNumber": hwPortVlanLimitNumber,
       "hwPortVlanLimitVlanIndex": hwPortVlanLimitVlanIndex,
       "hwPortVlanLimitRowStatus": hwPortVlanLimitRowStatus,
       "hwMldSnpgMibObject": hwMldSnpgMibObject,
       "hwMldSnpgSystemInfo": hwMldSnpgSystemInfo,
       "hwMldSnoopingEnabled": hwMldSnoopingEnabled,
       "hwMldSendQueryEnabled": hwMldSendQueryEnabled,
       "hwMldSendQuerySourceIpAddr": hwMldSendQuerySourceIpAddr,
       "hwMldSnoopingSuppressionTime": hwMldSnoopingSuppressionTime,
       "hwMldVlanCfgInfo": hwMldVlanCfgInfo,
       "hwMldVlanCfgTable": hwMldVlanCfgTable,
       "hwMldVlanCfgEntry": hwMldVlanCfgEntry,
       "hwMldVlanIndex": hwMldVlanIndex,
       "hwVlanMldSnoopingEnabled": hwVlanMldSnoopingEnabled,
       "hwMldVlanRouterAgingTime": hwMldVlanRouterAgingTime,
       "hwMldVlanMaxQueryRespTime": hwMldVlanMaxQueryRespTime,
       "hwMldVlanLastListenerQueryInt": hwMldVlanLastListenerQueryInt,
       "hwMldVlanQueryInt": hwMldVlanQueryInt,
       "hwMldVlanRobustCount": hwMldVlanRobustCount,
       "hwMldVlanCheckRouterAlert": hwMldVlanCheckRouterAlert,
       "hwMldVlanSendRouterAlert": hwMldVlanSendRouterAlert,
       "hwVlanMldVersion": hwVlanMldVersion,
       "hwMldVlanPromptLeaveEnable": hwMldVlanPromptLeaveEnable,
       "hwMldVlanPromptLeaveAclNum": hwMldVlanPromptLeaveAclNum,
       "hwMldVlanDropUnknown": hwMldVlanDropUnknown,
       "hwMldStatisticsInfo": hwMldStatisticsInfo,
       "hwMldSystemStatisticsInfo": hwMldSystemStatisticsInfo,
       "hwMldSystemRecvVlanUpEventTimes": hwMldSystemRecvVlanUpEventTimes,
       "hwMldSystemRecvVlanDownEventTimes": hwMldSystemRecvVlanDownEventTimes,
       "hwMldSystemRecvVlanDelEventTimes": hwMldSystemRecvVlanDelEventTimes,
       "hwMldSystemRecvPortUpEventTimes": hwMldSystemRecvPortUpEventTimes,
       "hwMldSystemRecvPortDownEventTimes": hwMldSystemRecvPortDownEventTimes,
       "hwMldSystemRecvPortDelEventTimes": hwMldSystemRecvPortDelEventTimes,
       "hwMldSystemRecvPortIncEventTimes": hwMldSystemRecvPortIncEventTimes,
       "hwMldSystemRecvPortExcEventTimes": hwMldSystemRecvPortExcEventTimes,
       "hwMldSystemRecvMstpBlockEventTimes": hwMldSystemRecvMstpBlockEventTimes,
       "hwMldSystemRecvMstpForwardEventTimes": hwMldSystemRecvMstpForwardEventTimes,
       "hwMldSystemSysClearStats": hwMldSystemSysClearStats,
       "hwMldSystemPacketClearStats": hwMldSystemPacketClearStats,
       "hwMldSystemRecvLinkChangeEventTimes": hwMldSystemRecvLinkChangeEventTimes,
       "hwMldVlanStatisticsTable": hwMldVlanStatisticsTable,
       "hwMldVlanStatisticsEntry": hwMldVlanStatisticsEntry,
       "hwMldVlanStatsVlanIndex": hwMldVlanStatsVlanIndex,
       "hwVlanRecvMldV1ReportNum": hwVlanRecvMldV1ReportNum,
       "hwVlanRecvMldV2ReportNum": hwVlanRecvMldV2ReportNum,
       "hwVlanRecvMldDoneNum": hwVlanRecvMldDoneNum,
       "hwVlanRecvMldV1QueryNum": hwVlanRecvMldV1QueryNum,
       "hwVlanRecvMldV2QueryNum": hwVlanRecvMldV2QueryNum,
       "hwVlanRecvIpv6PimHelloNum": hwVlanRecvIpv6PimHelloNum,
       "hwVlanSendMldQueryNum": hwVlanSendMldQueryNum,
       "hwVlanMldPacketClearStats": hwVlanMldPacketClearStats,
       "hwVlanSendSourceIpSpecMldQueryNum": hwVlanSendSourceIpSpecMldQueryNum,
       "hwMldMCGrpInfo": hwMldMCGrpInfo,
       "hwMldIpGrpInfoTable": hwMldIpGrpInfoTable,
       "hwMldIpGrpInfoEntry": hwMldIpGrpInfoEntry,
       "hwMldIpGrpVlanIndex": hwMldIpGrpVlanIndex,
       "hwMldIpGrpPortIfIndex": hwMldIpGrpPortIfIndex,
       "hwMldIpGrpAddress": hwMldIpGrpAddress,
       "hwMldIpGrpUpTime": hwMldIpGrpUpTime,
       "hwMldIpHostUpTime": hwMldIpHostUpTime,
       "hwMldIpHostExpires": hwMldIpHostExpires,
       "hwMldIpHostFlag": hwMldIpHostFlag,
       "hwMldIpRtUpTime": hwMldIpRtUpTime,
       "hwMldIpRtExpires": hwMldIpRtExpires,
       "hwMldIpRtFlag": hwMldIpRtFlag,
       "hwMldIpSourceAddress": hwMldIpSourceAddress,
       "hwMldPortInfo": hwMldPortInfo,
       "hwMldPortStaticGrpTable": hwMldPortStaticGrpTable,
       "hwMldPortStaticGrpEntry": hwMldPortStaticGrpEntry,
       "hwMldPortStaticGrpVlanIndex": hwMldPortStaticGrpVlanIndex,
       "hwMldPortStaticGrpIfIndex": hwMldPortStaticGrpIfIndex,
       "hwMldPortStaticGrpAddr": hwMldPortStaticGrpAddr,
       "hwMldPortStaticSourceAddr": hwMldPortStaticSourceAddr,
       "hwMldPortStaticGrpRowStatus": hwMldPortStaticGrpRowStatus,
       "hwMldGrpPolicyCfgTable": hwMldGrpPolicyCfgTable,
       "hwMldGrpPolicyCfgEntry": hwMldGrpPolicyCfgEntry,
       "hwMldGrpPolicyVlanIndex": hwMldGrpPolicyVlanIndex,
       "hwMldGrpPolicyAclNum": hwMldGrpPolicyAclNum,
       "hwGrpPolicyMldVersion": hwGrpPolicyMldVersion,
       "hwMldGrpPolicyRowStatus": hwMldGrpPolicyRowStatus,
       "hwMldRouterPortInfoTable": hwMldRouterPortInfoTable,
       "hwMldRouterPortInfoEntry": hwMldRouterPortInfoEntry,
       "hwMldRouterPortVlanIndex": hwMldRouterPortVlanIndex,
       "hwMldRouterPortIfIndex": hwMldRouterPortIfIndex,
       "hwMldRouterPortUpTime": hwMldRouterPortUpTime,
       "hwMldRouterPortExpires": hwMldRouterPortExpires,
       "hwMldRouterPortFlag": hwMldRouterPortFlag,
       "hwMldRouterPortCfgTable": hwMldRouterPortCfgTable,
       "hwMldRouterPortCfgEntry": hwMldRouterPortCfgEntry,
       "hwMldRouterPortCfgVlanIndex": hwMldRouterPortCfgVlanIndex,
       "hwMldRouterPortCfgIfIndex": hwMldRouterPortCfgIfIndex,
       "hwMldRouterPortCfgRowStatus": hwMldRouterPortCfgRowStatus,
       "hwMldPortLimitTable": hwMldPortLimitTable,
       "hwMldPortLimitEntry": hwMldPortLimitEntry,
       "hwMldPortLimitIfIndex": hwMldPortLimitIfIndex,
       "hwMldPortLimitNumber": hwMldPortLimitNumber,
       "hwMldPortLimitVlanIndex": hwMldPortLimitVlanIndex,
       "hwMldPortLimitRowStatus": hwMldPortLimitRowStatus,
       "hwMldPortGroupPolicyTable": hwMldPortGroupPolicyTable,
       "hwMldPortGroupPolicyEntry": hwMldPortGroupPolicyEntry,
       "hwMldPortGroupPolicyIfIndex": hwMldPortGroupPolicyIfIndex,
       "hwMldPortGroupPolicyAclNumber": hwMldPortGroupPolicyAclNumber,
       "hwMldPortGroupPolicyVlanIndex": hwMldPortGroupPolicyVlanIndex,
       "hwMldPortGroupPolicyVersion": hwMldPortGroupPolicyVersion,
       "hwMldPortGroupPolicyRowStatus": hwMldPortGroupPolicyRowStatus,
       "hwMVlanMibObject": hwMVlanMibObject,
       "hwMVlanSystemInfo": hwMVlanSystemInfo,
       "hwMVlanEnabled": hwMVlanEnabled,
       "hwMVlanVlanCfgInfo": hwMVlanVlanCfgInfo,
       "hwMVlanEnableTable": hwMVlanEnableTable,
       "hwMVlanEnableEntry": hwMVlanEnableEntry,
       "hwMVlanIndex": hwMVlanIndex,
       "hwMVlanStatus": hwMVlanStatus,
       "hwMVlanUserVlanTable": hwMVlanUserVlanTable,
       "hwMVlanUserVlanEntry": hwMVlanUserVlanEntry,
       "hwUserVlanIndex": hwUserVlanIndex,
       "hwUserVlanCfgRowStatus": hwUserVlanCfgRowStatus,
       "hwUserVlanTable": hwUserVlanTable,
       "hwUserVlanEntry": hwUserVlanEntry,
       "hwUserVlanFlowTriggerEnable": hwUserVlanFlowTriggerEnable,
       "hwMcSourceDenyTable": hwMcSourceDenyTable,
       "hwMcSourceDenyEntry": hwMcSourceDenyEntry,
       "hwMcSourceDenyVlanIndex": hwMcSourceDenyVlanIndex,
       "hwMcSourceDenyIfIndex": hwMcSourceDenyIfIndex,
       "hwMcSourceDenyRowStatus": hwMcSourceDenyRowStatus,
       "hwMVlanGrpInfo": hwMVlanGrpInfo,
       "hwMVlanGrpInfoTable": hwMVlanGrpInfoTable,
       "hwMVlanGrpInfoEntry": hwMVlanGrpInfoEntry,
       "hwMVlanGrpAddress": hwMVlanGrpAddress,
       "hwMVlanGrpPortIfIndex": hwMVlanGrpPortIfIndex,
       "hwMVlanGrpUserVlanIndex": hwMVlanGrpUserVlanIndex,
       "hwMVlanStaticFlowTable": hwMVlanStaticFlowTable,
       "hwMVlanStaticFlowEntry": hwMVlanStaticFlowEntry,
       "hwMVlanStaticFlowGrpAddress": hwMVlanStaticFlowGrpAddress,
       "hwMVlanStaticFlowRowStatus": hwMVlanStaticFlowRowStatus,
       "hwMVlanIpv6StaticFlowTable": hwMVlanIpv6StaticFlowTable,
       "hwMVlanIpv6StaticFlowEntry": hwMVlanIpv6StaticFlowEntry,
       "hwMVlanStaticFlowIpv6GrpAddress": hwMVlanStaticFlowIpv6GrpAddress,
       "hwMVlanStaticFlowIpv6SourceAddress": hwMVlanStaticFlowIpv6SourceAddress,
       "hwMVlanIpv6StaticFlowRowStatus": hwMVlanIpv6StaticFlowRowStatus,
       "hwExternMVlanStaticFlowTable": hwExternMVlanStaticFlowTable,
       "hwExternMVlanStaticFlowEntry": hwExternMVlanStaticFlowEntry,
       "hwExternMVlanStaticFlowGrpAddress": hwExternMVlanStaticFlowGrpAddress,
       "hwExternMVlanStaticFlowSourceAddress": hwExternMVlanStaticFlowSourceAddress,
       "hwExternMVlanStaticFlowRowStatus": hwExternMVlanStaticFlowRowStatus,
       "hwMultiCastCommonObject": hwMultiCastCommonObject,
       "hwMCSystemInfo": hwMCSystemInfo,
       "hwEthTrunkLoadBalancingEnabled": hwEthTrunkLoadBalancingEnabled,
       "hwL2CacTrapObject": hwL2CacTrapObject,
       "hwL2mcCacCount": hwL2mcCacCount,
       "hwL2mcCacBandwidth": hwL2mcCacBandwidth,
       "hwL2mcCacGroupAddress": hwL2mcCacGroupAddress,
       "hwL2mcCacChannelName": hwL2mcCacChannelName,
       "hwL2mcCacVlanIndex": hwL2mcCacVlanIndex,
       "hwL2mcCacVsiName": hwL2mcCacVsiName,
       "hwL2mcCacIfIndex": hwL2mcCacIfIndex,
       "hwL2mcCacPwId": hwL2mcCacPwId,
       "hwL2mcCacRemoteIpAddress": hwL2mcCacRemoteIpAddress,
       "hwL2mcCacRemoteSiteId": hwL2mcCacRemoteSiteId,
       "hwBtvMibObject": hwBtvMibObject,
       "hwBtvSystemInfo": hwBtvSystemInfo,
       "hwBtvEnabled": hwBtvEnabled,
       "hwBtvCfgInfo": hwBtvCfgInfo,
       "hwMcastGroupTable": hwMcastGroupTable,
       "hwMcastGroupEntry": hwMcastGroupEntry,
       "hwMcastGroupIndex": hwMcastGroupIndex,
       "hwMcastGroupName": hwMcastGroupName,
       "hwMcastGroupAddress": hwMcastGroupAddress,
       "hwMcastGroupRowStatus": hwMcastGroupRowStatus,
       "hwMcastSourceAddress": hwMcastSourceAddress,
       "hwMcastListTable": hwMcastListTable,
       "hwMcastListEntry": hwMcastListEntry,
       "hwMcastListIndex": hwMcastListIndex,
       "hwMcastListName": hwMcastListName,
       "hwMcastListRowStatus": hwMcastListRowStatus,
       "hwMcastProfileTable": hwMcastProfileTable,
       "hwMcastProfileEntry": hwMcastProfileEntry,
       "hwMcastProfileIndex": hwMcastProfileIndex,
       "hwMcastProfileName": hwMcastProfileName,
       "hwMcastProfileRowStatus": hwMcastProfileRowStatus,
       "hwMcastProfileCfgTable": hwMcastProfileCfgTable,
       "hwMcastProfileCfgEntry": hwMcastProfileCfgEntry,
       "hwMcastProfileCfgPreviewTimes": hwMcastProfileCfgPreviewTimes,
       "hwMcastProfileCfgPreviewMinute": hwMcastProfileCfgPreviewMinute,
       "hwMcastProfileCfgPreviewInterval": hwMcastProfileCfgPreviewInterval,
       "hwMcastProfileCfgMaxNumProgram": hwMcastProfileCfgMaxNumProgram,
       "hwMcastListReferTable": hwMcastListReferTable,
       "hwMcastListReferEntry": hwMcastListReferEntry,
       "hwMcastListReferRowStatus": hwMcastListReferRowStatus,
       "hwMcastProfileReferTable": hwMcastProfileReferTable,
       "hwMcastProfileReferEntry": hwMcastProfileReferEntry,
       "hwMcastPreviewStatus": hwMcastPreviewStatus,
       "hwMcastProfileReferRowStatus": hwMcastProfileReferRowStatus,
       "hwVlanApplyProfileTable": hwVlanApplyProfileTable,
       "hwVlanApplyProfileEntry": hwVlanApplyProfileEntry,
       "hwVlanApplyProfileRowStatus": hwVlanApplyProfileRowStatus,
       "hwMcastIpv6GroupTable": hwMcastIpv6GroupTable,
       "hwMcastIpv6GroupEntry": hwMcastIpv6GroupEntry,
       "hwMcastIpv6GroupIndex": hwMcastIpv6GroupIndex,
       "hwMcastIpv6GroupName": hwMcastIpv6GroupName,
       "hwMcastIpv6GroupAddress": hwMcastIpv6GroupAddress,
       "hwMcastIpv6SourceAddress": hwMcastIpv6SourceAddress,
       "hwMcastIpv6GroupRowStatus": hwMcastIpv6GroupRowStatus,
       "hwExternVlanApplyProfileTable": hwExternVlanApplyProfileTable,
       "hwExternVlanApplyProfileEntry": hwExternVlanApplyProfileEntry,
       "hwExternPortIfIndex": hwExternPortIfIndex,
       "hwExternSourceMacAddress": hwExternSourceMacAddress,
       "hwExternVlanApplyProfileRowStatus": hwExternVlanApplyProfileRowStatus,
       "hwMcastAlarmObject": hwMcastAlarmObject,
       "hwCfgRefreshFailAlarm": hwCfgRefreshFailAlarm,
       "hwMCastTableLoadAbnormalNotify": hwMCastTableLoadAbnormalNotify,
       "hwMCastTableLoadAbnormalResume": hwMCastTableLoadAbnormalResume,
       "hwMCastVlanFailAlarm": hwMCastVlanFailAlarm,
       "hwMCastVlanOkNotify": hwMCastVlanOkNotify,
       "hwMCastApsSwitchAlarm": hwMCastApsSwitchAlarm,
       "hwMCastApsIdleNotify": hwMCastApsIdleNotify,
       "hwL2mcCacGlobalCountExceed": hwL2mcCacGlobalCountExceed,
       "hwL2mcCacGlobalBandwidthExceed": hwL2mcCacGlobalBandwidthExceed,
       "hwL2mcCacGlobalChannelCountExceed": hwL2mcCacGlobalChannelCountExceed,
       "hwL2mcCacGlobalChannelBandwidthExceed": hwL2mcCacGlobalChannelBandwidthExceed,
       "hwL2mcCacVlanCountExceed": hwL2mcCacVlanCountExceed,
       "hwL2mcCacVlanBandwidthExceed": hwL2mcCacVlanBandwidthExceed,
       "hwL2mcCacVlanChannelCountExceed": hwL2mcCacVlanChannelCountExceed,
       "hwL2mcCacVlanChannelBandwidthExceed": hwL2mcCacVlanChannelBandwidthExceed,
       "hwL2mcCacVsiCountExceed": hwL2mcCacVsiCountExceed,
       "hwL2mcCacVsiBandwidthExceed": hwL2mcCacVsiBandwidthExceed,
       "hwL2mcCacVsiChannelCountExceed": hwL2mcCacVsiChannelCountExceed,
       "hwL2mcCacVsiChannelBandwidthExceed": hwL2mcCacVsiChannelBandwidthExceed,
       "hwL2mcCacPortCountExceed": hwL2mcCacPortCountExceed,
       "hwL2mcCacPortBandwidthExceed": hwL2mcCacPortBandwidthExceed,
       "hwL2mcCacPortChannelCountExceed": hwL2mcCacPortChannelCountExceed,
       "hwL2mcCacPortChannelBandwidthExceed": hwL2mcCacPortChannelBandwidthExceed,
       "hwL2mcCacPortVlanCountExceed": hwL2mcCacPortVlanCountExceed,
       "hwL2mcCacPortVlanBandwidthExceed": hwL2mcCacPortVlanBandwidthExceed,
       "hwL2mcCacPortVlanChannelCountExceed": hwL2mcCacPortVlanChannelCountExceed,
       "hwL2mcCacPortVlanChannelBandwidthExceed": hwL2mcCacPortVlanChannelBandwidthExceed,
       "hwL2mcCacSubIfCountExceed": hwL2mcCacSubIfCountExceed,
       "hwL2mcCacSubIfBandwidthExceed": hwL2mcCacSubIfBandwidthExceed,
       "hwL2mcCacSubIfChannelCountExceed": hwL2mcCacSubIfChannelCountExceed,
       "hwL2mcCacSubIfChannelBandwidthExceed": hwL2mcCacSubIfChannelBandwidthExceed,
       "hwL2mcCacLdpPwCountExceed": hwL2mcCacLdpPwCountExceed,
       "hwL2mcCacLdpPwBandwidthExceed": hwL2mcCacLdpPwBandwidthExceed,
       "hwL2mcCacLdpPwChannelCountExceed": hwL2mcCacLdpPwChannelCountExceed,
       "hwL2mcCacLdpPwChannelBandwidthExceed": hwL2mcCacLdpPwChannelBandwidthExceed,
       "hwL2mcCacBgpPwCountExceed": hwL2mcCacBgpPwCountExceed,
       "hwL2mcCacBgpPwBandwidthExceed": hwL2mcCacBgpPwBandwidthExceed,
       "hwL2mcCacBgpPwChannelCountExceed": hwL2mcCacBgpPwChannelCountExceed,
       "hwL2mcCacBgpPwChannelBandwidthExceed": hwL2mcCacBgpPwChannelBandwidthExceed,
       "hwL2mcCacVlanUnspecifiedChannelDeny": hwL2mcCacVlanUnspecifiedChannelDeny,
       "hwL2mcCacVsiUnspecifiedChannelDeny": hwL2mcCacVsiUnspecifiedChannelDeny,
       "hwL2mcCacGlobalUnspecifiedChannelDeny": hwL2mcCacGlobalUnspecifiedChannelDeny,
       "hwMCMibConformance": hwMCMibConformance,
       "hwMCMibCompliances": hwMCMibCompliances,
       "hwIGSPMibCompliance": hwIGSPMibCompliance,
       "hwMCMibGroups": hwMCMibGroups,
       "hwIGSPSystemInfoGroup": hwIGSPSystemInfoGroup,
       "hwVlanCfgGroup": hwVlanCfgGroup,
       "hwSystemStatisticsGroup": hwSystemStatisticsGroup,
       "hwVlanStatisticsGroup": hwVlanStatisticsGroup,
       "hwIPGrpInfoGroup": hwIPGrpInfoGroup,
       "hwMACGrpInfoGroup": hwMACGrpInfoGroup,
       "hwPortStaticGrpGroup": hwPortStaticGrpGroup,
       "hwGrpPolicyCfgGroup": hwGrpPolicyCfgGroup,
       "hwRouterPortInfoGroup": hwRouterPortInfoGroup,
       "hwRouterPortCfgGroup": hwRouterPortCfgGroup,
       "hwPortLimitGroup": hwPortLimitGroup,
       "hwMVlanSystemGroup": hwMVlanSystemGroup,
       "hwMVlanEnableGroup": hwMVlanEnableGroup,
       "hwMVlanUserVlanGroup": hwMVlanUserVlanGroup,
       "hwMVlanGrpInfoGroup": hwMVlanGrpInfoGroup,
       "hwMCastSystemGroup": hwMCastSystemGroup,
       "hwL2CacTrapGroup": hwL2CacTrapGroup,
       "hwVlanIgmpProxyGroup": hwVlanIgmpProxyGroup,
       "hwL2McastVlanCfgGroup": hwL2McastVlanCfgGroup,
       "hwGrpMcastCfgGroup": hwGrpMcastCfgGroup,
       "hwVlanMcastGrpGroup": hwVlanMcastGrpGroup,
       "hwGrpMcastProfileGroup": hwGrpMcastProfileGroup,
       "hwUserVlanGroup": hwUserVlanGroup,
       "hwMVlanStaticFlowGroup": hwMVlanStaticFlowGroup,
       "hwBtvSystemGroup": hwBtvSystemGroup,
       "hwMcastGroupGroup": hwMcastGroupGroup,
       "hwMcastListGroup": hwMcastListGroup,
       "hwMcastProfileGroup": hwMcastProfileGroup,
       "hwMcastProfileCfgGroup": hwMcastProfileCfgGroup,
       "hwMcastListReferGroup": hwMcastListReferGroup,
       "hwMcastProfileReferGroup": hwMcastProfileReferGroup,
       "hwVlanApplyProfileGroup": hwVlanApplyProfileGroup,
       "hwPortGroupPolicyGroup": hwPortGroupPolicyGroup,
       "hwMldSnpgSystemInfoGroup": hwMldSnpgSystemInfoGroup,
       "hwMldVlanCfgGroup": hwMldVlanCfgGroup,
       "hwMldSystemStatisticsGroup": hwMldSystemStatisticsGroup,
       "hwMldVlanStatisticsGroup": hwMldVlanStatisticsGroup,
       "hwMldIpGrpInfoGroup": hwMldIpGrpInfoGroup,
       "hwMldPortStaticGrpGroup": hwMldPortStaticGrpGroup,
       "hwMldGrpPolicyCfgGroup": hwMldGrpPolicyCfgGroup,
       "hwMldRouterPortInfoGroup": hwMldRouterPortInfoGroup,
       "hwMldRouterPortCfgGroup": hwMldRouterPortCfgGroup,
       "hwMldPortLimitGroup": hwMldPortLimitGroup,
       "hwMldPortGroupPolicyGroup": hwMldPortGroupPolicyGroup,
       "hwMcSourceDenyGroup": hwMcSourceDenyGroup,
       "hwMVlanIpv6StaticFlowGroup": hwMVlanIpv6StaticFlowGroup,
       "hwMcastIpv6GroupGroup": hwMcastIpv6GroupGroup,
       "hwExternIpGrpInfoGroup": hwExternIpGrpInfoGroup,
       "hwExternPortStaticGrpGroup": hwExternPortStaticGrpGroup,
       "hwPortVlanLimitGroup": hwPortVlanLimitGroup,
       "hwExternMVlanStaticFlowGroup": hwExternMVlanStaticFlowGroup,
       "hwExternVlanApplyProfileGroup": hwExternVlanApplyProfileGroup,
       "hwMcastAlarmGroup": hwMcastAlarmGroup}
)
