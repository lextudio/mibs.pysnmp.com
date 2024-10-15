# SNMP MIB module (HUAWEI-LswQos-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LswQos-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:44 2024
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

(lswCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "lswCommon")

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

hwLswQosAclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16)
)
hwLswQosAclMib.setRevisions(
        ("2002-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwMirrorOrMonitorType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("board", 2),
          ("port", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwLswQosMibObject_ObjectIdentity = ObjectIdentity
hwLswQosMibObject = _HwLswQosMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2)
)


class _HwPriorityTrustMode_Type(Integer32):
    """Custom type hwPriorityTrustMode based on Integer32"""
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
        *(("cos", 3),
          ("default", 0),
          ("dscp", 1),
          ("ipprecedence", 2),
          ("localprecedence", 4))
    )


_HwPriorityTrustMode_Type.__name__ = "Integer32"
_HwPriorityTrustMode_Object = MibScalar
hwPriorityTrustMode = _HwPriorityTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 1),
    _HwPriorityTrustMode_Type()
)
hwPriorityTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPriorityTrustMode.setStatus("current")


class _HwPortMonitorBothIfIndex_Type(Integer32):
    """Custom type hwPortMonitorBothIfIndex based on Integer32"""
    defaultValue = 0


_HwPortMonitorBothIfIndex_Object = MibScalar
hwPortMonitorBothIfIndex = _HwPortMonitorBothIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 2),
    _HwPortMonitorBothIfIndex_Type()
)
hwPortMonitorBothIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortMonitorBothIfIndex.setStatus("current")
_HwQueueTable_Object = MibTable
hwQueueTable = _HwQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    hwQueueTable.setStatus("current")
_HwQueueEntry_Object = MibTableRow
hwQueueEntry = _HwQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1)
)
hwQueueEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwQueueIfIndex"),
)
if mibBuilder.loadTexts:
    hwQueueEntry.setStatus("current")
_HwQueueIfIndex_Type = Integer32
_HwQueueIfIndex_Object = MibTableColumn
hwQueueIfIndex = _HwQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 1),
    _HwQueueIfIndex_Type()
)
hwQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwQueueIfIndex.setStatus("current")


class _HwQueueScheduleMode_Type(Integer32):
    """Custom type hwQueueScheduleMode based on Integer32"""
    defaultValue = 1

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
        *(("hq-wrr", 9),
          ("rr", 7),
          ("sc-0", 4),
          ("sc-1", 5),
          ("sc-2", 6),
          ("sp", 1),
          ("wfq", 8),
          ("wrr", 2),
          ("wrr-max-delay", 3))
    )


_HwQueueScheduleMode_Type.__name__ = "Integer32"
_HwQueueScheduleMode_Object = MibTableColumn
hwQueueScheduleMode = _HwQueueScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 2),
    _HwQueueScheduleMode_Type()
)
hwQueueScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueScheduleMode.setStatus("current")
_HwQueueWeight1_Type = Integer32
_HwQueueWeight1_Object = MibTableColumn
hwQueueWeight1 = _HwQueueWeight1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 3),
    _HwQueueWeight1_Type()
)
hwQueueWeight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight1.setStatus("current")
_HwQueueWeight2_Type = Integer32
_HwQueueWeight2_Object = MibTableColumn
hwQueueWeight2 = _HwQueueWeight2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 4),
    _HwQueueWeight2_Type()
)
hwQueueWeight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight2.setStatus("current")
_HwQueueWeight3_Type = Integer32
_HwQueueWeight3_Object = MibTableColumn
hwQueueWeight3 = _HwQueueWeight3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 5),
    _HwQueueWeight3_Type()
)
hwQueueWeight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight3.setStatus("current")
_HwQueueWeight4_Type = Integer32
_HwQueueWeight4_Object = MibTableColumn
hwQueueWeight4 = _HwQueueWeight4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 6),
    _HwQueueWeight4_Type()
)
hwQueueWeight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight4.setStatus("current")


class _HwQueueMaxDelay_Type(Integer32):
    """Custom type hwQueueMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwQueueMaxDelay_Type.__name__ = "Integer32"
_HwQueueMaxDelay_Object = MibTableColumn
hwQueueMaxDelay = _HwQueueMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 7),
    _HwQueueMaxDelay_Type()
)
hwQueueMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueMaxDelay.setStatus("current")
_HwQueueWeight5_Type = Integer32
_HwQueueWeight5_Object = MibTableColumn
hwQueueWeight5 = _HwQueueWeight5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 8),
    _HwQueueWeight5_Type()
)
hwQueueWeight5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight5.setStatus("current")
_HwQueueWeight6_Type = Integer32
_HwQueueWeight6_Object = MibTableColumn
hwQueueWeight6 = _HwQueueWeight6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 9),
    _HwQueueWeight6_Type()
)
hwQueueWeight6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight6.setStatus("current")
_HwQueueWeight7_Type = Integer32
_HwQueueWeight7_Object = MibTableColumn
hwQueueWeight7 = _HwQueueWeight7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 10),
    _HwQueueWeight7_Type()
)
hwQueueWeight7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight7.setStatus("current")
_HwQueueWeight8_Type = Integer32
_HwQueueWeight8_Object = MibTableColumn
hwQueueWeight8 = _HwQueueWeight8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 3, 1, 11),
    _HwQueueWeight8_Type()
)
hwQueueWeight8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwQueueWeight8.setStatus("current")
_HwRateLimitTable_Object = MibTable
hwRateLimitTable = _HwRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4)
)
if mibBuilder.loadTexts:
    hwRateLimitTable.setStatus("current")
_HwRateLimitEntry_Object = MibTableRow
hwRateLimitEntry = _HwRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1)
)
hwRateLimitEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwRateLimitAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRateLimitIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRateLimitVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwRateLimitDirection"),
)
if mibBuilder.loadTexts:
    hwRateLimitEntry.setStatus("current")


class _HwRateLimitAclIndex_Type(Integer32):
    """Custom type hwRateLimitAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwRateLimitAclIndex_Type.__name__ = "Integer32"
_HwRateLimitAclIndex_Object = MibTableColumn
hwRateLimitAclIndex = _HwRateLimitAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 1),
    _HwRateLimitAclIndex_Type()
)
hwRateLimitAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitAclIndex.setStatus("current")
_HwRateLimitIfIndex_Type = Integer32
_HwRateLimitIfIndex_Object = MibTableColumn
hwRateLimitIfIndex = _HwRateLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 2),
    _HwRateLimitIfIndex_Type()
)
hwRateLimitIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitIfIndex.setStatus("current")


class _HwRateLimitVlanID_Type(Integer32):
    """Custom type hwRateLimitVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRateLimitVlanID_Type.__name__ = "Integer32"
_HwRateLimitVlanID_Object = MibTableColumn
hwRateLimitVlanID = _HwRateLimitVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 3),
    _HwRateLimitVlanID_Type()
)
hwRateLimitVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitVlanID.setStatus("current")


class _HwRateLimitDirection_Type(Integer32):
    """Custom type hwRateLimitDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwRateLimitDirection_Type.__name__ = "Integer32"
_HwRateLimitDirection_Object = MibTableColumn
hwRateLimitDirection = _HwRateLimitDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 4),
    _HwRateLimitDirection_Type()
)
hwRateLimitDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitDirection.setStatus("current")


class _HwRateLimitUserAclNum_Type(Integer32):
    """Custom type hwRateLimitUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRateLimitUserAclNum_Type.__name__ = "Integer32"
_HwRateLimitUserAclNum_Object = MibTableColumn
hwRateLimitUserAclNum = _HwRateLimitUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 5),
    _HwRateLimitUserAclNum_Type()
)
hwRateLimitUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitUserAclNum.setStatus("current")


class _HwRateLimitUserAclRule_Type(Integer32):
    """Custom type hwRateLimitUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRateLimitUserAclRule_Type.__name__ = "Integer32"
_HwRateLimitUserAclRule_Object = MibTableColumn
hwRateLimitUserAclRule = _HwRateLimitUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 6),
    _HwRateLimitUserAclRule_Type()
)
hwRateLimitUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitUserAclRule.setStatus("current")


class _HwRateLimitIpAclNum_Type(Integer32):
    """Custom type hwRateLimitIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRateLimitIpAclNum_Type.__name__ = "Integer32"
_HwRateLimitIpAclNum_Object = MibTableColumn
hwRateLimitIpAclNum = _HwRateLimitIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 7),
    _HwRateLimitIpAclNum_Type()
)
hwRateLimitIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitIpAclNum.setStatus("current")


class _HwRateLimitIpAclRule_Type(Integer32):
    """Custom type hwRateLimitIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRateLimitIpAclRule_Type.__name__ = "Integer32"
_HwRateLimitIpAclRule_Object = MibTableColumn
hwRateLimitIpAclRule = _HwRateLimitIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 8),
    _HwRateLimitIpAclRule_Type()
)
hwRateLimitIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitIpAclRule.setStatus("current")


class _HwRateLimitLinkAclNum_Type(Integer32):
    """Custom type hwRateLimitLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRateLimitLinkAclNum_Type.__name__ = "Integer32"
_HwRateLimitLinkAclNum_Object = MibTableColumn
hwRateLimitLinkAclNum = _HwRateLimitLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 9),
    _HwRateLimitLinkAclNum_Type()
)
hwRateLimitLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitLinkAclNum.setStatus("current")


class _HwRateLimitLinkAclRule_Type(Integer32):
    """Custom type hwRateLimitLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRateLimitLinkAclRule_Type.__name__ = "Integer32"
_HwRateLimitLinkAclRule_Object = MibTableColumn
hwRateLimitLinkAclRule = _HwRateLimitLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 10),
    _HwRateLimitLinkAclRule_Type()
)
hwRateLimitLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitLinkAclRule.setStatus("current")
_HwRateLimitTargetRateMbps_Type = Integer32
_HwRateLimitTargetRateMbps_Object = MibTableColumn
hwRateLimitTargetRateMbps = _HwRateLimitTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 11),
    _HwRateLimitTargetRateMbps_Type()
)
hwRateLimitTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitTargetRateMbps.setStatus("current")
_HwRateLimitTargetRateKbps_Type = Integer32
_HwRateLimitTargetRateKbps_Object = MibTableColumn
hwRateLimitTargetRateKbps = _HwRateLimitTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 12),
    _HwRateLimitTargetRateKbps_Type()
)
hwRateLimitTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitTargetRateKbps.setStatus("current")


class _HwRateLimitPeakRate_Type(Integer32):
    """Custom type hwRateLimitPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_HwRateLimitPeakRate_Type.__name__ = "Integer32"
_HwRateLimitPeakRate_Object = MibTableColumn
hwRateLimitPeakRate = _HwRateLimitPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 13),
    _HwRateLimitPeakRate_Type()
)
hwRateLimitPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitPeakRate.setStatus("current")


class _HwRateLimitCIR_Type(Integer32):
    """Custom type hwRateLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HwRateLimitCIR_Type.__name__ = "Integer32"
_HwRateLimitCIR_Object = MibTableColumn
hwRateLimitCIR = _HwRateLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 14),
    _HwRateLimitCIR_Type()
)
hwRateLimitCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitCIR.setStatus("current")


class _HwRateLimitCBS_Type(Integer32):
    """Custom type hwRateLimitCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_HwRateLimitCBS_Type.__name__ = "Integer32"
_HwRateLimitCBS_Object = MibTableColumn
hwRateLimitCBS = _HwRateLimitCBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 15),
    _HwRateLimitCBS_Type()
)
hwRateLimitCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitCBS.setStatus("current")


class _HwRateLimitEBS_Type(Integer32):
    """Custom type hwRateLimitEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_HwRateLimitEBS_Type.__name__ = "Integer32"
_HwRateLimitEBS_Object = MibTableColumn
hwRateLimitEBS = _HwRateLimitEBS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 16),
    _HwRateLimitEBS_Type()
)
hwRateLimitEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitEBS.setStatus("current")


class _HwRateLimitPIR_Type(Integer32):
    """Custom type hwRateLimitPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HwRateLimitPIR_Type.__name__ = "Integer32"
_HwRateLimitPIR_Object = MibTableColumn
hwRateLimitPIR = _HwRateLimitPIR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 17),
    _HwRateLimitPIR_Type()
)
hwRateLimitPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitPIR.setStatus("current")


class _HwRateLimitConformLocalPre_Type(Integer32):
    """Custom type hwRateLimitConformLocalPre based on Integer32"""
    defaultValue = 1


_HwRateLimitConformLocalPre_Object = MibTableColumn
hwRateLimitConformLocalPre = _HwRateLimitConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 18),
    _HwRateLimitConformLocalPre_Type()
)
hwRateLimitConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitConformLocalPre.setStatus("current")


class _HwRateLimitConformActionType_Type(Integer32):
    """Custom type hwRateLimitConformActionType based on Integer32"""
    defaultValue = 1

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
        *(("invalid", 0),
          ("remark-cos", 1),
          ("remark-cos-drop-priority", 3),
          ("remark-drop-priority", 2),
          ("remark-dscp", 5),
          ("remark-policed-service", 4))
    )


_HwRateLimitConformActionType_Type.__name__ = "Integer32"
_HwRateLimitConformActionType_Object = MibTableColumn
hwRateLimitConformActionType = _HwRateLimitConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 19),
    _HwRateLimitConformActionType_Type()
)
hwRateLimitConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitConformActionType.setStatus("current")


class _HwRateLimitExceedActionType_Type(Integer32):
    """Custom type hwRateLimitExceedActionType based on Integer32"""
    defaultValue = 1

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
        *(("drop", 2),
          ("exceed-cos", 4),
          ("forward", 1),
          ("invalid", 0),
          ("remarkdscp", 3))
    )


_HwRateLimitExceedActionType_Type.__name__ = "Integer32"
_HwRateLimitExceedActionType_Object = MibTableColumn
hwRateLimitExceedActionType = _HwRateLimitExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 20),
    _HwRateLimitExceedActionType_Type()
)
hwRateLimitExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitExceedActionType.setStatus("current")


class _HwRateLimitExceedDscp_Type(Integer32):
    """Custom type hwRateLimitExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwRateLimitExceedDscp_Type.__name__ = "Integer32"
_HwRateLimitExceedDscp_Object = MibTableColumn
hwRateLimitExceedDscp = _HwRateLimitExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 21),
    _HwRateLimitExceedDscp_Type()
)
hwRateLimitExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitExceedDscp.setStatus("current")
_HwRateLimitRuntime_Type = TruthValue
_HwRateLimitRuntime_Object = MibTableColumn
hwRateLimitRuntime = _HwRateLimitRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 22),
    _HwRateLimitRuntime_Type()
)
hwRateLimitRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRateLimitRuntime.setStatus("current")
_HwRateLimitRowStatus_Type = RowStatus
_HwRateLimitRowStatus_Object = MibTableColumn
hwRateLimitRowStatus = _HwRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 23),
    _HwRateLimitRowStatus_Type()
)
hwRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitRowStatus.setStatus("current")


class _HwRateLimitExceedCos_Type(Integer32):
    """Custom type hwRateLimitExceedCos based on Integer32"""
    defaultValue = 255


_HwRateLimitExceedCos_Object = MibTableColumn
hwRateLimitExceedCos = _HwRateLimitExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 24),
    _HwRateLimitExceedCos_Type()
)
hwRateLimitExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitExceedCos.setStatus("current")


class _HwRateLimitConformCos_Type(Integer32):
    """Custom type hwRateLimitConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwRateLimitConformCos_Type.__name__ = "Integer32"
_HwRateLimitConformCos_Object = MibTableColumn
hwRateLimitConformCos = _HwRateLimitConformCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 25),
    _HwRateLimitConformCos_Type()
)
hwRateLimitConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitConformCos.setStatus("current")


class _HwRateLimitConformDscp_Type(Integer32):
    """Custom type hwRateLimitConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwRateLimitConformDscp_Type.__name__ = "Integer32"
_HwRateLimitConformDscp_Object = MibTableColumn
hwRateLimitConformDscp = _HwRateLimitConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 26),
    _HwRateLimitConformDscp_Type()
)
hwRateLimitConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitConformDscp.setStatus("current")
_HwRateLimitMeterStatByteCount_Type = Counter64
_HwRateLimitMeterStatByteCount_Object = MibTableColumn
hwRateLimitMeterStatByteCount = _HwRateLimitMeterStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 27),
    _HwRateLimitMeterStatByteCount_Type()
)
hwRateLimitMeterStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRateLimitMeterStatByteCount.setStatus("current")
_HwRateLimitMeterStatByteXCount_Type = Counter64
_HwRateLimitMeterStatByteXCount_Object = MibTableColumn
hwRateLimitMeterStatByteXCount = _HwRateLimitMeterStatByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 28),
    _HwRateLimitMeterStatByteXCount_Type()
)
hwRateLimitMeterStatByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRateLimitMeterStatByteXCount.setStatus("current")


class _HwRateLimitMeterStatState_Type(Integer32):
    """Custom type hwRateLimitMeterStatState based on Integer32"""
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
        *(("notRunning", 5),
          ("reset", 3),
          ("running", 4),
          ("set", 1),
          ("unDo", 2))
    )


_HwRateLimitMeterStatState_Type.__name__ = "Integer32"
_HwRateLimitMeterStatState_Object = MibTableColumn
hwRateLimitMeterStatState = _HwRateLimitMeterStatState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 4, 1, 29),
    _HwRateLimitMeterStatState_Type()
)
hwRateLimitMeterStatState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRateLimitMeterStatState.setStatus("current")
_HwPriorityTable_Object = MibTable
hwPriorityTable = _HwPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5)
)
if mibBuilder.loadTexts:
    hwPriorityTable.setStatus("current")
_HwPriorityEntry_Object = MibTableRow
hwPriorityEntry = _HwPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1)
)
hwPriorityEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwPriorityAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwPriorityIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwPriorityVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwPriorityDirection"),
)
if mibBuilder.loadTexts:
    hwPriorityEntry.setStatus("current")


class _HwPriorityAclIndex_Type(Integer32):
    """Custom type hwPriorityAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwPriorityAclIndex_Type.__name__ = "Integer32"
_HwPriorityAclIndex_Object = MibTableColumn
hwPriorityAclIndex = _HwPriorityAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 1),
    _HwPriorityAclIndex_Type()
)
hwPriorityAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityAclIndex.setStatus("current")
_HwPriorityIfIndex_Type = Integer32
_HwPriorityIfIndex_Object = MibTableColumn
hwPriorityIfIndex = _HwPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 2),
    _HwPriorityIfIndex_Type()
)
hwPriorityIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityIfIndex.setStatus("current")


class _HwPriorityVlanID_Type(Integer32):
    """Custom type hwPriorityVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwPriorityVlanID_Type.__name__ = "Integer32"
_HwPriorityVlanID_Object = MibTableColumn
hwPriorityVlanID = _HwPriorityVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 3),
    _HwPriorityVlanID_Type()
)
hwPriorityVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityVlanID.setStatus("current")


class _HwPriorityDirection_Type(Integer32):
    """Custom type hwPriorityDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwPriorityDirection_Type.__name__ = "Integer32"
_HwPriorityDirection_Object = MibTableColumn
hwPriorityDirection = _HwPriorityDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 4),
    _HwPriorityDirection_Type()
)
hwPriorityDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityDirection.setStatus("current")


class _HwPriorityUserAclNum_Type(Integer32):
    """Custom type hwPriorityUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwPriorityUserAclNum_Type.__name__ = "Integer32"
_HwPriorityUserAclNum_Object = MibTableColumn
hwPriorityUserAclNum = _HwPriorityUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 5),
    _HwPriorityUserAclNum_Type()
)
hwPriorityUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityUserAclNum.setStatus("current")


class _HwPriorityUserAclRule_Type(Integer32):
    """Custom type hwPriorityUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPriorityUserAclRule_Type.__name__ = "Integer32"
_HwPriorityUserAclRule_Object = MibTableColumn
hwPriorityUserAclRule = _HwPriorityUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 6),
    _HwPriorityUserAclRule_Type()
)
hwPriorityUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityUserAclRule.setStatus("current")


class _HwPriorityIpAclNum_Type(Integer32):
    """Custom type hwPriorityIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwPriorityIpAclNum_Type.__name__ = "Integer32"
_HwPriorityIpAclNum_Object = MibTableColumn
hwPriorityIpAclNum = _HwPriorityIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 7),
    _HwPriorityIpAclNum_Type()
)
hwPriorityIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityIpAclNum.setStatus("current")


class _HwPriorityIpAclRule_Type(Integer32):
    """Custom type hwPriorityIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPriorityIpAclRule_Type.__name__ = "Integer32"
_HwPriorityIpAclRule_Object = MibTableColumn
hwPriorityIpAclRule = _HwPriorityIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 8),
    _HwPriorityIpAclRule_Type()
)
hwPriorityIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityIpAclRule.setStatus("current")


class _HwPriorityLinkAclNum_Type(Integer32):
    """Custom type hwPriorityLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwPriorityLinkAclNum_Type.__name__ = "Integer32"
_HwPriorityLinkAclNum_Object = MibTableColumn
hwPriorityLinkAclNum = _HwPriorityLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 9),
    _HwPriorityLinkAclNum_Type()
)
hwPriorityLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityLinkAclNum.setStatus("current")


class _HwPriorityLinkAclRule_Type(Integer32):
    """Custom type hwPriorityLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPriorityLinkAclRule_Type.__name__ = "Integer32"
_HwPriorityLinkAclRule_Object = MibTableColumn
hwPriorityLinkAclRule = _HwPriorityLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 10),
    _HwPriorityLinkAclRule_Type()
)
hwPriorityLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityLinkAclRule.setStatus("current")


class _HwPriorityDscp_Type(Integer32):
    """Custom type hwPriorityDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityDscp_Type.__name__ = "Integer32"
_HwPriorityDscp_Object = MibTableColumn
hwPriorityDscp = _HwPriorityDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 11),
    _HwPriorityDscp_Type()
)
hwPriorityDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityDscp.setStatus("current")


class _HwPriorityIpPre_Type(Integer32):
    """Custom type hwPriorityIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityIpPre_Type.__name__ = "Integer32"
_HwPriorityIpPre_Object = MibTableColumn
hwPriorityIpPre = _HwPriorityIpPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 12),
    _HwPriorityIpPre_Type()
)
hwPriorityIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityIpPre.setStatus("current")


class _HwPriorityIpPreFromCos_Type(TruthValue):
    """Custom type hwPriorityIpPreFromCos based on TruthValue"""
    defaultValue = 2


_HwPriorityIpPreFromCos_Object = MibTableColumn
hwPriorityIpPreFromCos = _HwPriorityIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 13),
    _HwPriorityIpPreFromCos_Type()
)
hwPriorityIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityIpPreFromCos.setStatus("current")


class _HwPriorityCos_Type(Integer32):
    """Custom type hwPriorityCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityCos_Type.__name__ = "Integer32"
_HwPriorityCos_Object = MibTableColumn
hwPriorityCos = _HwPriorityCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 14),
    _HwPriorityCos_Type()
)
hwPriorityCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityCos.setStatus("current")


class _HwPriorityCosFromIpPre_Type(TruthValue):
    """Custom type hwPriorityCosFromIpPre based on TruthValue"""
    defaultValue = 2


_HwPriorityCosFromIpPre_Object = MibTableColumn
hwPriorityCosFromIpPre = _HwPriorityCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 15),
    _HwPriorityCosFromIpPre_Type()
)
hwPriorityCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityCosFromIpPre.setStatus("current")


class _HwPriorityLocalPre_Type(Integer32):
    """Custom type hwPriorityLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityLocalPre_Type.__name__ = "Integer32"
_HwPriorityLocalPre_Object = MibTableColumn
hwPriorityLocalPre = _HwPriorityLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 16),
    _HwPriorityLocalPre_Type()
)
hwPriorityLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityLocalPre.setStatus("current")


class _HwPriorityPolicedServiceType_Type(Integer32):
    """Custom type hwPriorityPolicedServiceType based on Integer32"""
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
        *(("auto", 1),
          ("invalid", 0),
          ("new-dscp", 3),
          ("trust-dscp", 2),
          ("untrusted", 4))
    )


_HwPriorityPolicedServiceType_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceType_Object = MibTableColumn
hwPriorityPolicedServiceType = _HwPriorityPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 17),
    _HwPriorityPolicedServiceType_Type()
)
hwPriorityPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceType.setStatus("current")


class _HwPriorityPolicedServiceDscp_Type(Integer32):
    """Custom type hwPriorityPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityPolicedServiceDscp_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceDscp_Object = MibTableColumn
hwPriorityPolicedServiceDscp = _HwPriorityPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 18),
    _HwPriorityPolicedServiceDscp_Type()
)
hwPriorityPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceDscp.setStatus("current")


class _HwPriorityPolicedServiceExp_Type(Integer32):
    """Custom type hwPriorityPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityPolicedServiceExp_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceExp_Object = MibTableColumn
hwPriorityPolicedServiceExp = _HwPriorityPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 19),
    _HwPriorityPolicedServiceExp_Type()
)
hwPriorityPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceExp.setStatus("current")


class _HwPriorityPolicedServiceCos_Type(Integer32):
    """Custom type hwPriorityPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityPolicedServiceCos_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceCos_Object = MibTableColumn
hwPriorityPolicedServiceCos = _HwPriorityPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 20),
    _HwPriorityPolicedServiceCos_Type()
)
hwPriorityPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceCos.setStatus("current")


class _HwPriorityPolicedServiceLoaclPre_Type(Integer32):
    """Custom type hwPriorityPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceLoaclPre_Object = MibTableColumn
hwPriorityPolicedServiceLoaclPre = _HwPriorityPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 21),
    _HwPriorityPolicedServiceLoaclPre_Type()
)
hwPriorityPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceLoaclPre.setStatus("current")


class _HwPriorityPolicedServiceDropPriority_Type(Integer32):
    """Custom type hwPriorityPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_HwPriorityPolicedServiceDropPriority_Type.__name__ = "Integer32"
_HwPriorityPolicedServiceDropPriority_Object = MibTableColumn
hwPriorityPolicedServiceDropPriority = _HwPriorityPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 22),
    _HwPriorityPolicedServiceDropPriority_Type()
)
hwPriorityPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityPolicedServiceDropPriority.setStatus("current")
_HwPriorityRuntime_Type = TruthValue
_HwPriorityRuntime_Object = MibTableColumn
hwPriorityRuntime = _HwPriorityRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 23),
    _HwPriorityRuntime_Type()
)
hwPriorityRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPriorityRuntime.setStatus("current")
_HwPriorityRowStatus_Type = RowStatus
_HwPriorityRowStatus_Object = MibTableColumn
hwPriorityRowStatus = _HwPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 5, 1, 24),
    _HwPriorityRowStatus_Type()
)
hwPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPriorityRowStatus.setStatus("current")
_HwRedirectTable_Object = MibTable
hwRedirectTable = _HwRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6)
)
if mibBuilder.loadTexts:
    hwRedirectTable.setStatus("current")
_HwRedirectEntry_Object = MibTableRow
hwRedirectEntry = _HwRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1)
)
hwRedirectEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwRedirectAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRedirectIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRedirectVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwRedirectDirection"),
)
if mibBuilder.loadTexts:
    hwRedirectEntry.setStatus("current")


class _HwRedirectAclIndex_Type(Integer32):
    """Custom type hwRedirectAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwRedirectAclIndex_Type.__name__ = "Integer32"
_HwRedirectAclIndex_Object = MibTableColumn
hwRedirectAclIndex = _HwRedirectAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 1),
    _HwRedirectAclIndex_Type()
)
hwRedirectAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectAclIndex.setStatus("current")
_HwRedirectIfIndex_Type = Integer32
_HwRedirectIfIndex_Object = MibTableColumn
hwRedirectIfIndex = _HwRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 2),
    _HwRedirectIfIndex_Type()
)
hwRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectIfIndex.setStatus("current")


class _HwRedirectVlanID_Type(Integer32):
    """Custom type hwRedirectVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRedirectVlanID_Type.__name__ = "Integer32"
_HwRedirectVlanID_Object = MibTableColumn
hwRedirectVlanID = _HwRedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 3),
    _HwRedirectVlanID_Type()
)
hwRedirectVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectVlanID.setStatus("current")


class _HwRedirectDirection_Type(Integer32):
    """Custom type hwRedirectDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwRedirectDirection_Type.__name__ = "Integer32"
_HwRedirectDirection_Object = MibTableColumn
hwRedirectDirection = _HwRedirectDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 4),
    _HwRedirectDirection_Type()
)
hwRedirectDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectDirection.setStatus("current")


class _HwRedirectUserAclNum_Type(Integer32):
    """Custom type hwRedirectUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRedirectUserAclNum_Type.__name__ = "Integer32"
_HwRedirectUserAclNum_Object = MibTableColumn
hwRedirectUserAclNum = _HwRedirectUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 5),
    _HwRedirectUserAclNum_Type()
)
hwRedirectUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectUserAclNum.setStatus("current")


class _HwRedirectUserAclRule_Type(Integer32):
    """Custom type hwRedirectUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRedirectUserAclRule_Type.__name__ = "Integer32"
_HwRedirectUserAclRule_Object = MibTableColumn
hwRedirectUserAclRule = _HwRedirectUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 6),
    _HwRedirectUserAclRule_Type()
)
hwRedirectUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectUserAclRule.setStatus("current")


class _HwRedirectIpAclNum_Type(Integer32):
    """Custom type hwRedirectIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRedirectIpAclNum_Type.__name__ = "Integer32"
_HwRedirectIpAclNum_Object = MibTableColumn
hwRedirectIpAclNum = _HwRedirectIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 7),
    _HwRedirectIpAclNum_Type()
)
hwRedirectIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectIpAclNum.setStatus("current")


class _HwRedirectIpAclRule_Type(Integer32):
    """Custom type hwRedirectIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRedirectIpAclRule_Type.__name__ = "Integer32"
_HwRedirectIpAclRule_Object = MibTableColumn
hwRedirectIpAclRule = _HwRedirectIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 8),
    _HwRedirectIpAclRule_Type()
)
hwRedirectIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectIpAclRule.setStatus("current")


class _HwRedirectLinkAclNum_Type(Integer32):
    """Custom type hwRedirectLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRedirectLinkAclNum_Type.__name__ = "Integer32"
_HwRedirectLinkAclNum_Object = MibTableColumn
hwRedirectLinkAclNum = _HwRedirectLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 9),
    _HwRedirectLinkAclNum_Type()
)
hwRedirectLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectLinkAclNum.setStatus("current")


class _HwRedirectLinkAclRule_Type(Integer32):
    """Custom type hwRedirectLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRedirectLinkAclRule_Type.__name__ = "Integer32"
_HwRedirectLinkAclRule_Object = MibTableColumn
hwRedirectLinkAclRule = _HwRedirectLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 10),
    _HwRedirectLinkAclRule_Type()
)
hwRedirectLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectLinkAclRule.setStatus("current")


class _HwRedirectToCpu_Type(TruthValue):
    """Custom type hwRedirectToCpu based on TruthValue"""
    defaultValue = 2


_HwRedirectToCpu_Object = MibTableColumn
hwRedirectToCpu = _HwRedirectToCpu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 11),
    _HwRedirectToCpu_Type()
)
hwRedirectToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToCpu.setStatus("current")
_HwRedirectToIfIndex_Type = Integer32
_HwRedirectToIfIndex_Object = MibTableColumn
hwRedirectToIfIndex = _HwRedirectToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 12),
    _HwRedirectToIfIndex_Type()
)
hwRedirectToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToIfIndex.setStatus("current")
_HwRedirectToNextHop1_Type = IpAddress
_HwRedirectToNextHop1_Object = MibTableColumn
hwRedirectToNextHop1 = _HwRedirectToNextHop1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 13),
    _HwRedirectToNextHop1_Type()
)
hwRedirectToNextHop1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToNextHop1.setStatus("current")
_HwRedirectToNextHop2_Type = IpAddress
_HwRedirectToNextHop2_Object = MibTableColumn
hwRedirectToNextHop2 = _HwRedirectToNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 14),
    _HwRedirectToNextHop2_Type()
)
hwRedirectToNextHop2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToNextHop2.setStatus("current")
_HwRedirectRuntime_Type = TruthValue
_HwRedirectRuntime_Object = MibTableColumn
hwRedirectRuntime = _HwRedirectRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 15),
    _HwRedirectRuntime_Type()
)
hwRedirectRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRedirectRuntime.setStatus("current")
_HwRedirectRowStatus_Type = RowStatus
_HwRedirectRowStatus_Object = MibTableColumn
hwRedirectRowStatus = _HwRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 16),
    _HwRedirectRowStatus_Type()
)
hwRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectRowStatus.setStatus("current")


class _HwRedirectToSlotNo_Type(Integer32):
    """Custom type hwRedirectToSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwRedirectToSlotNo_Type.__name__ = "Integer32"
_HwRedirectToSlotNo_Object = MibTableColumn
hwRedirectToSlotNo = _HwRedirectToSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 17),
    _HwRedirectToSlotNo_Type()
)
hwRedirectToSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToSlotNo.setStatus("current")


class _HwRedirectRemarkedDSCP_Type(Integer32):
    """Custom type hwRedirectRemarkedDSCP based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HwRedirectRemarkedDSCP_Type.__name__ = "Integer32"
_HwRedirectRemarkedDSCP_Object = MibTableColumn
hwRedirectRemarkedDSCP = _HwRedirectRemarkedDSCP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 18),
    _HwRedirectRemarkedDSCP_Type()
)
hwRedirectRemarkedDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectRemarkedDSCP.setStatus("current")


class _HwRedirectRemarkedPri_Type(Integer32):
    """Custom type hwRedirectRemarkedPri based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwRedirectRemarkedPri_Type.__name__ = "Integer32"
_HwRedirectRemarkedPri_Object = MibTableColumn
hwRedirectRemarkedPri = _HwRedirectRemarkedPri_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 19),
    _HwRedirectRemarkedPri_Type()
)
hwRedirectRemarkedPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectRemarkedPri.setStatus("current")


class _HwRedirectRemarkedTos_Type(Integer32):
    """Custom type hwRedirectRemarkedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HwRedirectRemarkedTos_Type.__name__ = "Integer32"
_HwRedirectRemarkedTos_Object = MibTableColumn
hwRedirectRemarkedTos = _HwRedirectRemarkedTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 20),
    _HwRedirectRemarkedTos_Type()
)
hwRedirectRemarkedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectRemarkedTos.setStatus("current")
_HwRedirectToNextHop3_Type = IpAddress
_HwRedirectToNextHop3_Object = MibTableColumn
hwRedirectToNextHop3 = _HwRedirectToNextHop3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 21),
    _HwRedirectToNextHop3_Type()
)
hwRedirectToNextHop3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToNextHop3.setStatus("current")


class _HwRedirectTargetVlanID_Type(Integer32):
    """Custom type hwRedirectTargetVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRedirectTargetVlanID_Type.__name__ = "Integer32"
_HwRedirectTargetVlanID_Object = MibTableColumn
hwRedirectTargetVlanID = _HwRedirectTargetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 22),
    _HwRedirectTargetVlanID_Type()
)
hwRedirectTargetVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectTargetVlanID.setStatus("current")


class _HwRedirectMode_Type(Integer32):
    """Custom type hwRedirectMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("load-balance", 2),
          ("strict-priority", 1))
    )


_HwRedirectMode_Type.__name__ = "Integer32"
_HwRedirectMode_Object = MibTableColumn
hwRedirectMode = _HwRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 23),
    _HwRedirectMode_Type()
)
hwRedirectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectMode.setStatus("current")


class _HwRedirectToNestedVlanID_Type(Integer32):
    """Custom type hwRedirectToNestedVlanID based on Integer32"""
    defaultValue = 0


_HwRedirectToNestedVlanID_Object = MibTableColumn
hwRedirectToNestedVlanID = _HwRedirectToNestedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 24),
    _HwRedirectToNestedVlanID_Type()
)
hwRedirectToNestedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToNestedVlanID.setStatus("current")


class _HwRedirectToModifiedVlanID_Type(Integer32):
    """Custom type hwRedirectToModifiedVlanID based on Integer32"""
    defaultValue = 0


_HwRedirectToModifiedVlanID_Object = MibTableColumn
hwRedirectToModifiedVlanID = _HwRedirectToModifiedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 6, 1, 25),
    _HwRedirectToModifiedVlanID_Type()
)
hwRedirectToModifiedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedirectToModifiedVlanID.setStatus("current")
_HwStatisticTable_Object = MibTable
hwStatisticTable = _HwStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7)
)
if mibBuilder.loadTexts:
    hwStatisticTable.setStatus("current")
_HwStatisticEntry_Object = MibTableRow
hwStatisticEntry = _HwStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1)
)
hwStatisticEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwStatisticAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwStatisticIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwStatisticVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwStatisticDirection"),
)
if mibBuilder.loadTexts:
    hwStatisticEntry.setStatus("current")


class _HwStatisticAclIndex_Type(Integer32):
    """Custom type hwStatisticAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwStatisticAclIndex_Type.__name__ = "Integer32"
_HwStatisticAclIndex_Object = MibTableColumn
hwStatisticAclIndex = _HwStatisticAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 1),
    _HwStatisticAclIndex_Type()
)
hwStatisticAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticAclIndex.setStatus("current")
_HwStatisticIfIndex_Type = Integer32
_HwStatisticIfIndex_Object = MibTableColumn
hwStatisticIfIndex = _HwStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 2),
    _HwStatisticIfIndex_Type()
)
hwStatisticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticIfIndex.setStatus("current")


class _HwStatisticVlanID_Type(Integer32):
    """Custom type hwStatisticVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwStatisticVlanID_Type.__name__ = "Integer32"
_HwStatisticVlanID_Object = MibTableColumn
hwStatisticVlanID = _HwStatisticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 3),
    _HwStatisticVlanID_Type()
)
hwStatisticVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticVlanID.setStatus("current")


class _HwStatisticDirection_Type(Integer32):
    """Custom type hwStatisticDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwStatisticDirection_Type.__name__ = "Integer32"
_HwStatisticDirection_Object = MibTableColumn
hwStatisticDirection = _HwStatisticDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 4),
    _HwStatisticDirection_Type()
)
hwStatisticDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticDirection.setStatus("current")


class _HwStatisticUserAclNum_Type(Integer32):
    """Custom type hwStatisticUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwStatisticUserAclNum_Type.__name__ = "Integer32"
_HwStatisticUserAclNum_Object = MibTableColumn
hwStatisticUserAclNum = _HwStatisticUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 5),
    _HwStatisticUserAclNum_Type()
)
hwStatisticUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticUserAclNum.setStatus("current")


class _HwStatisticUserAclRule_Type(Integer32):
    """Custom type hwStatisticUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwStatisticUserAclRule_Type.__name__ = "Integer32"
_HwStatisticUserAclRule_Object = MibTableColumn
hwStatisticUserAclRule = _HwStatisticUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 6),
    _HwStatisticUserAclRule_Type()
)
hwStatisticUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticUserAclRule.setStatus("current")


class _HwStatisticIpAclNum_Type(Integer32):
    """Custom type hwStatisticIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwStatisticIpAclNum_Type.__name__ = "Integer32"
_HwStatisticIpAclNum_Object = MibTableColumn
hwStatisticIpAclNum = _HwStatisticIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 7),
    _HwStatisticIpAclNum_Type()
)
hwStatisticIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticIpAclNum.setStatus("current")


class _HwStatisticIpAclRule_Type(Integer32):
    """Custom type hwStatisticIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwStatisticIpAclRule_Type.__name__ = "Integer32"
_HwStatisticIpAclRule_Object = MibTableColumn
hwStatisticIpAclRule = _HwStatisticIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 8),
    _HwStatisticIpAclRule_Type()
)
hwStatisticIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticIpAclRule.setStatus("current")


class _HwStatisticLinkAclNum_Type(Integer32):
    """Custom type hwStatisticLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwStatisticLinkAclNum_Type.__name__ = "Integer32"
_HwStatisticLinkAclNum_Object = MibTableColumn
hwStatisticLinkAclNum = _HwStatisticLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 9),
    _HwStatisticLinkAclNum_Type()
)
hwStatisticLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticLinkAclNum.setStatus("current")


class _HwStatisticLinkAclRule_Type(Integer32):
    """Custom type hwStatisticLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwStatisticLinkAclRule_Type.__name__ = "Integer32"
_HwStatisticLinkAclRule_Object = MibTableColumn
hwStatisticLinkAclRule = _HwStatisticLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 10),
    _HwStatisticLinkAclRule_Type()
)
hwStatisticLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticLinkAclRule.setStatus("current")
_HwStatisticRuntime_Type = TruthValue
_HwStatisticRuntime_Object = MibTableColumn
hwStatisticRuntime = _HwStatisticRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 11),
    _HwStatisticRuntime_Type()
)
hwStatisticRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatisticRuntime.setStatus("current")
_HwStatisticPacketCount_Type = Counter64
_HwStatisticPacketCount_Object = MibTableColumn
hwStatisticPacketCount = _HwStatisticPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 12),
    _HwStatisticPacketCount_Type()
)
hwStatisticPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatisticPacketCount.setStatus("current")
_HwStatisticByteCount_Type = Counter64
_HwStatisticByteCount_Object = MibTableColumn
hwStatisticByteCount = _HwStatisticByteCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 13),
    _HwStatisticByteCount_Type()
)
hwStatisticByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatisticByteCount.setStatus("current")


class _HwStatisticCountClear_Type(Integer32):
    """Custom type hwStatisticCountClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )


_HwStatisticCountClear_Type.__name__ = "Integer32"
_HwStatisticCountClear_Object = MibTableColumn
hwStatisticCountClear = _HwStatisticCountClear_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 14),
    _HwStatisticCountClear_Type()
)
hwStatisticCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStatisticCountClear.setStatus("current")
_HwStatisticRowStatus_Type = RowStatus
_HwStatisticRowStatus_Object = MibTableColumn
hwStatisticRowStatus = _HwStatisticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 15),
    _HwStatisticRowStatus_Type()
)
hwStatisticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStatisticRowStatus.setStatus("current")
_HwStatisticPacketXCount_Type = Counter64
_HwStatisticPacketXCount_Object = MibTableColumn
hwStatisticPacketXCount = _HwStatisticPacketXCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 16),
    _HwStatisticPacketXCount_Type()
)
hwStatisticPacketXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatisticPacketXCount.setStatus("current")
_HwStatisticByteXCount_Type = Counter64
_HwStatisticByteXCount_Object = MibTableColumn
hwStatisticByteXCount = _HwStatisticByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 7, 1, 17),
    _HwStatisticByteXCount_Type()
)
hwStatisticByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStatisticByteXCount.setStatus("current")
_HwMirrorTable_Object = MibTable
hwMirrorTable = _HwMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8)
)
if mibBuilder.loadTexts:
    hwMirrorTable.setStatus("current")
_HwMirrorEntry_Object = MibTableRow
hwMirrorEntry = _HwMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1)
)
hwMirrorEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirrorAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwMirrorIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwMirrorVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwMirrorDirection"),
)
if mibBuilder.loadTexts:
    hwMirrorEntry.setStatus("current")


class _HwMirrorAclIndex_Type(Integer32):
    """Custom type hwMirrorAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwMirrorAclIndex_Type.__name__ = "Integer32"
_HwMirrorAclIndex_Object = MibTableColumn
hwMirrorAclIndex = _HwMirrorAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 1),
    _HwMirrorAclIndex_Type()
)
hwMirrorAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorAclIndex.setStatus("current")
_HwMirrorIfIndex_Type = Integer32
_HwMirrorIfIndex_Object = MibTableColumn
hwMirrorIfIndex = _HwMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 2),
    _HwMirrorIfIndex_Type()
)
hwMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorIfIndex.setStatus("current")


class _HwMirrorVlanID_Type(Integer32):
    """Custom type hwMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMirrorVlanID_Type.__name__ = "Integer32"
_HwMirrorVlanID_Object = MibTableColumn
hwMirrorVlanID = _HwMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 3),
    _HwMirrorVlanID_Type()
)
hwMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorVlanID.setStatus("current")


class _HwMirrorDirection_Type(Integer32):
    """Custom type hwMirrorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwMirrorDirection_Type.__name__ = "Integer32"
_HwMirrorDirection_Object = MibTableColumn
hwMirrorDirection = _HwMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 4),
    _HwMirrorDirection_Type()
)
hwMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorDirection.setStatus("current")


class _HwMirrorUserAclNum_Type(Integer32):
    """Custom type hwMirrorUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwMirrorUserAclNum_Type.__name__ = "Integer32"
_HwMirrorUserAclNum_Object = MibTableColumn
hwMirrorUserAclNum = _HwMirrorUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 5),
    _HwMirrorUserAclNum_Type()
)
hwMirrorUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorUserAclNum.setStatus("current")


class _HwMirrorUserAclRule_Type(Integer32):
    """Custom type hwMirrorUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMirrorUserAclRule_Type.__name__ = "Integer32"
_HwMirrorUserAclRule_Object = MibTableColumn
hwMirrorUserAclRule = _HwMirrorUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 6),
    _HwMirrorUserAclRule_Type()
)
hwMirrorUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorUserAclRule.setStatus("current")


class _HwMirrorIpAclNum_Type(Integer32):
    """Custom type hwMirrorIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwMirrorIpAclNum_Type.__name__ = "Integer32"
_HwMirrorIpAclNum_Object = MibTableColumn
hwMirrorIpAclNum = _HwMirrorIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 7),
    _HwMirrorIpAclNum_Type()
)
hwMirrorIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorIpAclNum.setStatus("current")


class _HwMirrorIpAclRule_Type(Integer32):
    """Custom type hwMirrorIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMirrorIpAclRule_Type.__name__ = "Integer32"
_HwMirrorIpAclRule_Object = MibTableColumn
hwMirrorIpAclRule = _HwMirrorIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 8),
    _HwMirrorIpAclRule_Type()
)
hwMirrorIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorIpAclRule.setStatus("current")


class _HwMirrorLinkAclNum_Type(Integer32):
    """Custom type hwMirrorLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwMirrorLinkAclNum_Type.__name__ = "Integer32"
_HwMirrorLinkAclNum_Object = MibTableColumn
hwMirrorLinkAclNum = _HwMirrorLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 9),
    _HwMirrorLinkAclNum_Type()
)
hwMirrorLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorLinkAclNum.setStatus("current")


class _HwMirrorLinkAclRule_Type(Integer32):
    """Custom type hwMirrorLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMirrorLinkAclRule_Type.__name__ = "Integer32"
_HwMirrorLinkAclRule_Object = MibTableColumn
hwMirrorLinkAclRule = _HwMirrorLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 10),
    _HwMirrorLinkAclRule_Type()
)
hwMirrorLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorLinkAclRule.setStatus("current")
_HwMirrorToIfIndex_Type = Integer32
_HwMirrorToIfIndex_Object = MibTableColumn
hwMirrorToIfIndex = _HwMirrorToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 11),
    _HwMirrorToIfIndex_Type()
)
hwMirrorToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorToIfIndex.setStatus("current")
_HwMirrorToCpu_Type = TruthValue
_HwMirrorToCpu_Object = MibTableColumn
hwMirrorToCpu = _HwMirrorToCpu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 12),
    _HwMirrorToCpu_Type()
)
hwMirrorToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorToCpu.setStatus("current")
_HwMirrorRuntime_Type = TruthValue
_HwMirrorRuntime_Object = MibTableColumn
hwMirrorRuntime = _HwMirrorRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 13),
    _HwMirrorRuntime_Type()
)
hwMirrorRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorRuntime.setStatus("current")
_HwMirrorRowStatus_Type = RowStatus
_HwMirrorRowStatus_Object = MibTableColumn
hwMirrorRowStatus = _HwMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 14),
    _HwMirrorRowStatus_Type()
)
hwMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorRowStatus.setStatus("current")
_HwMirrorToGroup_Type = Integer32
_HwMirrorToGroup_Object = MibTableColumn
hwMirrorToGroup = _HwMirrorToGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 8, 1, 15),
    _HwMirrorToGroup_Type()
)
hwMirrorToGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorToGroup.setStatus("current")
_HwPortMirrorTable_Object = MibTable
hwPortMirrorTable = _HwPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 9)
)
if mibBuilder.loadTexts:
    hwPortMirrorTable.setStatus("current")
_HwPortMirrorEntry_Object = MibTableRow
hwPortMirrorEntry = _HwPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 9, 1)
)
hwPortMirrorEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwPortMirrorIfIndex"),
)
if mibBuilder.loadTexts:
    hwPortMirrorEntry.setStatus("current")
_HwPortMirrorIfIndex_Type = Integer32
_HwPortMirrorIfIndex_Object = MibTableColumn
hwPortMirrorIfIndex = _HwPortMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 9, 1, 1),
    _HwPortMirrorIfIndex_Type()
)
hwPortMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortMirrorIfIndex.setStatus("current")


class _HwPortMirrorDirection_Type(Integer32):
    """Custom type hwPortMirrorDirection based on Integer32"""
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
          ("in", 1),
          ("out", 2))
    )


_HwPortMirrorDirection_Type.__name__ = "Integer32"
_HwPortMirrorDirection_Object = MibTableColumn
hwPortMirrorDirection = _HwPortMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 9, 1, 2),
    _HwPortMirrorDirection_Type()
)
hwPortMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortMirrorDirection.setStatus("current")
_HwPortMirrorRowStatus_Type = RowStatus
_HwPortMirrorRowStatus_Object = MibTableColumn
hwPortMirrorRowStatus = _HwPortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 9, 1, 3),
    _HwPortMirrorRowStatus_Type()
)
hwPortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPortMirrorRowStatus.setStatus("current")
_HwLineRateTable_Object = MibTable
hwLineRateTable = _HwLineRateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10)
)
if mibBuilder.loadTexts:
    hwLineRateTable.setStatus("current")
_HwLineRateEntry_Object = MibTableRow
hwLineRateEntry = _HwLineRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10, 1)
)
hwLineRateEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwLineRateIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwLineRateDirection"),
)
if mibBuilder.loadTexts:
    hwLineRateEntry.setStatus("current")
_HwLineRateIfIndex_Type = Integer32
_HwLineRateIfIndex_Object = MibTableColumn
hwLineRateIfIndex = _HwLineRateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10, 1, 1),
    _HwLineRateIfIndex_Type()
)
hwLineRateIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLineRateIfIndex.setStatus("current")


class _HwLineRateDirection_Type(Integer32):
    """Custom type hwLineRateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_HwLineRateDirection_Type.__name__ = "Integer32"
_HwLineRateDirection_Object = MibTableColumn
hwLineRateDirection = _HwLineRateDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10, 1, 2),
    _HwLineRateDirection_Type()
)
hwLineRateDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLineRateDirection.setStatus("current")
_HwLineRateValue_Type = Integer32
_HwLineRateValue_Object = MibTableColumn
hwLineRateValue = _HwLineRateValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10, 1, 3),
    _HwLineRateValue_Type()
)
hwLineRateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLineRateValue.setStatus("current")
_HwLineRateRowStatus_Type = RowStatus
_HwLineRateRowStatus_Object = MibTableColumn
hwLineRateRowStatus = _HwLineRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 10, 1, 4),
    _HwLineRateRowStatus_Type()
)
hwLineRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwLineRateRowStatus.setStatus("current")
_HwBandwidthTable_Object = MibTable
hwBandwidthTable = _HwBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11)
)
if mibBuilder.loadTexts:
    hwBandwidthTable.setStatus("current")
_HwBandwidthEntry_Object = MibTableRow
hwBandwidthEntry = _HwBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1)
)
hwBandwidthEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwBandwidthAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwBandwidthIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwBandwidthVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwBandwidthDirection"),
)
if mibBuilder.loadTexts:
    hwBandwidthEntry.setStatus("current")


class _HwBandwidthAclIndex_Type(Integer32):
    """Custom type hwBandwidthAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwBandwidthAclIndex_Type.__name__ = "Integer32"
_HwBandwidthAclIndex_Object = MibTableColumn
hwBandwidthAclIndex = _HwBandwidthAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 1),
    _HwBandwidthAclIndex_Type()
)
hwBandwidthAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthAclIndex.setStatus("current")
_HwBandwidthIfIndex_Type = Integer32
_HwBandwidthIfIndex_Object = MibTableColumn
hwBandwidthIfIndex = _HwBandwidthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 2),
    _HwBandwidthIfIndex_Type()
)
hwBandwidthIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthIfIndex.setStatus("current")


class _HwBandwidthVlanID_Type(Integer32):
    """Custom type hwBandwidthVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwBandwidthVlanID_Type.__name__ = "Integer32"
_HwBandwidthVlanID_Object = MibTableColumn
hwBandwidthVlanID = _HwBandwidthVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 3),
    _HwBandwidthVlanID_Type()
)
hwBandwidthVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthVlanID.setStatus("current")


class _HwBandwidthDirection_Type(Integer32):
    """Custom type hwBandwidthDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("output", 2))
    )


_HwBandwidthDirection_Type.__name__ = "Integer32"
_HwBandwidthDirection_Object = MibTableColumn
hwBandwidthDirection = _HwBandwidthDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 4),
    _HwBandwidthDirection_Type()
)
hwBandwidthDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthDirection.setStatus("current")


class _HwBandwidthIpAclNum_Type(Integer32):
    """Custom type hwBandwidthIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwBandwidthIpAclNum_Type.__name__ = "Integer32"
_HwBandwidthIpAclNum_Object = MibTableColumn
hwBandwidthIpAclNum = _HwBandwidthIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 5),
    _HwBandwidthIpAclNum_Type()
)
hwBandwidthIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthIpAclNum.setStatus("current")


class _HwBandwidthIpAclRule_Type(Integer32):
    """Custom type hwBandwidthIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBandwidthIpAclRule_Type.__name__ = "Integer32"
_HwBandwidthIpAclRule_Object = MibTableColumn
hwBandwidthIpAclRule = _HwBandwidthIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 6),
    _HwBandwidthIpAclRule_Type()
)
hwBandwidthIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthIpAclRule.setStatus("current")


class _HwBandwidthLinkAclNum_Type(Integer32):
    """Custom type hwBandwidthLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwBandwidthLinkAclNum_Type.__name__ = "Integer32"
_HwBandwidthLinkAclNum_Object = MibTableColumn
hwBandwidthLinkAclNum = _HwBandwidthLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 7),
    _HwBandwidthLinkAclNum_Type()
)
hwBandwidthLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthLinkAclNum.setStatus("current")


class _HwBandwidthLinkAclRule_Type(Integer32):
    """Custom type hwBandwidthLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwBandwidthLinkAclRule_Type.__name__ = "Integer32"
_HwBandwidthLinkAclRule_Object = MibTableColumn
hwBandwidthLinkAclRule = _HwBandwidthLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 8),
    _HwBandwidthLinkAclRule_Type()
)
hwBandwidthLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBandwidthLinkAclRule.setStatus("current")


class _HwBandwidthMinGuaranteedWidth_Type(Integer32):
    """Custom type hwBandwidthMinGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_HwBandwidthMinGuaranteedWidth_Type.__name__ = "Integer32"
_HwBandwidthMinGuaranteedWidth_Object = MibTableColumn
hwBandwidthMinGuaranteedWidth = _HwBandwidthMinGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 9),
    _HwBandwidthMinGuaranteedWidth_Type()
)
hwBandwidthMinGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBandwidthMinGuaranteedWidth.setStatus("current")


class _HwBandwidthMaxGuaranteedWidth_Type(Integer32):
    """Custom type hwBandwidthMaxGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_HwBandwidthMaxGuaranteedWidth_Type.__name__ = "Integer32"
_HwBandwidthMaxGuaranteedWidth_Object = MibTableColumn
hwBandwidthMaxGuaranteedWidth = _HwBandwidthMaxGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 10),
    _HwBandwidthMaxGuaranteedWidth_Type()
)
hwBandwidthMaxGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBandwidthMaxGuaranteedWidth.setStatus("current")


class _HwBandwidthWeight_Type(Integer32):
    """Custom type hwBandwidthWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBandwidthWeight_Type.__name__ = "Integer32"
_HwBandwidthWeight_Object = MibTableColumn
hwBandwidthWeight = _HwBandwidthWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 11),
    _HwBandwidthWeight_Type()
)
hwBandwidthWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBandwidthWeight.setStatus("current")
_HwBandwidthRuntime_Type = TruthValue
_HwBandwidthRuntime_Object = MibTableColumn
hwBandwidthRuntime = _HwBandwidthRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 12),
    _HwBandwidthRuntime_Type()
)
hwBandwidthRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBandwidthRuntime.setStatus("current")
_HwBandwidthRowStatus_Type = RowStatus
_HwBandwidthRowStatus_Object = MibTableColumn
hwBandwidthRowStatus = _HwBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 11, 1, 13),
    _HwBandwidthRowStatus_Type()
)
hwBandwidthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBandwidthRowStatus.setStatus("current")
_HwRedTable_Object = MibTable
hwRedTable = _HwRedTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12)
)
if mibBuilder.loadTexts:
    hwRedTable.setStatus("current")
_HwRedEntry_Object = MibTableRow
hwRedEntry = _HwRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1)
)
hwRedEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwRedAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRedIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRedVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwRedDirection"),
)
if mibBuilder.loadTexts:
    hwRedEntry.setStatus("current")


class _HwRedAclIndex_Type(Integer32):
    """Custom type hwRedAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwRedAclIndex_Type.__name__ = "Integer32"
_HwRedAclIndex_Object = MibTableColumn
hwRedAclIndex = _HwRedAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 1),
    _HwRedAclIndex_Type()
)
hwRedAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedAclIndex.setStatus("current")
_HwRedIfIndex_Type = Integer32
_HwRedIfIndex_Object = MibTableColumn
hwRedIfIndex = _HwRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 2),
    _HwRedIfIndex_Type()
)
hwRedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedIfIndex.setStatus("current")


class _HwRedVlanID_Type(Integer32):
    """Custom type hwRedVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRedVlanID_Type.__name__ = "Integer32"
_HwRedVlanID_Object = MibTableColumn
hwRedVlanID = _HwRedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 3),
    _HwRedVlanID_Type()
)
hwRedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedVlanID.setStatus("current")


class _HwRedDirection_Type(Integer32):
    """Custom type hwRedDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("output", 2))
    )


_HwRedDirection_Type.__name__ = "Integer32"
_HwRedDirection_Object = MibTableColumn
hwRedDirection = _HwRedDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 4),
    _HwRedDirection_Type()
)
hwRedDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedDirection.setStatus("current")


class _HwRedIpAclNum_Type(Integer32):
    """Custom type hwRedIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRedIpAclNum_Type.__name__ = "Integer32"
_HwRedIpAclNum_Object = MibTableColumn
hwRedIpAclNum = _HwRedIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 5),
    _HwRedIpAclNum_Type()
)
hwRedIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedIpAclNum.setStatus("current")


class _HwRedIpAclRule_Type(Integer32):
    """Custom type hwRedIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRedIpAclRule_Type.__name__ = "Integer32"
_HwRedIpAclRule_Object = MibTableColumn
hwRedIpAclRule = _HwRedIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 6),
    _HwRedIpAclRule_Type()
)
hwRedIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedIpAclRule.setStatus("current")


class _HwRedLinkAclNum_Type(Integer32):
    """Custom type hwRedLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRedLinkAclNum_Type.__name__ = "Integer32"
_HwRedLinkAclNum_Object = MibTableColumn
hwRedLinkAclNum = _HwRedLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 7),
    _HwRedLinkAclNum_Type()
)
hwRedLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedLinkAclNum.setStatus("current")


class _HwRedLinkAclRule_Type(Integer32):
    """Custom type hwRedLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRedLinkAclRule_Type.__name__ = "Integer32"
_HwRedLinkAclRule_Object = MibTableColumn
hwRedLinkAclRule = _HwRedLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 8),
    _HwRedLinkAclRule_Type()
)
hwRedLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRedLinkAclRule.setStatus("current")


class _HwRedStartQueueLen_Type(Integer32):
    """Custom type hwRedStartQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_HwRedStartQueueLen_Type.__name__ = "Integer32"
_HwRedStartQueueLen_Object = MibTableColumn
hwRedStartQueueLen = _HwRedStartQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 9),
    _HwRedStartQueueLen_Type()
)
hwRedStartQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRedStartQueueLen.setStatus("current")


class _HwRedStopQueueLen_Type(Integer32):
    """Custom type hwRedStopQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_HwRedStopQueueLen_Type.__name__ = "Integer32"
_HwRedStopQueueLen_Object = MibTableColumn
hwRedStopQueueLen = _HwRedStopQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 10),
    _HwRedStopQueueLen_Type()
)
hwRedStopQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRedStopQueueLen.setStatus("current")


class _HwRedProbability_Type(Integer32):
    """Custom type hwRedProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwRedProbability_Type.__name__ = "Integer32"
_HwRedProbability_Object = MibTableColumn
hwRedProbability = _HwRedProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 11),
    _HwRedProbability_Type()
)
hwRedProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRedProbability.setStatus("current")
_HwRedRuntime_Type = TruthValue
_HwRedRuntime_Object = MibTableColumn
hwRedRuntime = _HwRedRuntime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 12),
    _HwRedRuntime_Type()
)
hwRedRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRedRuntime.setStatus("current")
_HwRedRowStatus_Type = RowStatus
_HwRedRowStatus_Object = MibTableColumn
hwRedRowStatus = _HwRedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 12, 1, 13),
    _HwRedRowStatus_Type()
)
hwRedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRedRowStatus.setStatus("current")
_HwMirrorGroupTable_Object = MibTable
hwMirrorGroupTable = _HwMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13)
)
if mibBuilder.loadTexts:
    hwMirrorGroupTable.setStatus("current")
_HwMirrorGroupEntry_Object = MibTableRow
hwMirrorGroupEntry = _HwMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1)
)
hwMirrorGroupEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hwMirrorGroupEntry.setStatus("current")


class _HwMirrorGroupID_Type(Integer32):
    """Custom type hwMirrorGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwMirrorGroupID_Type.__name__ = "Integer32"
_HwMirrorGroupID_Object = MibTableColumn
hwMirrorGroupID = _HwMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1, 1),
    _HwMirrorGroupID_Type()
)
hwMirrorGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirrorGroupID.setStatus("current")


class _HwMirrorGroupDirection_Type(Integer32):
    """Custom type hwMirrorGroupDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_HwMirrorGroupDirection_Type.__name__ = "Integer32"
_HwMirrorGroupDirection_Object = MibTableColumn
hwMirrorGroupDirection = _HwMirrorGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1, 2),
    _HwMirrorGroupDirection_Type()
)
hwMirrorGroupDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMirrorGroupDirection.setStatus("current")


class _HwMirrorGroupMirrorIfIndexList_Type(OctetString):
    """Custom type hwMirrorGroupMirrorIfIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_HwMirrorGroupMirrorIfIndexList_Type.__name__ = "OctetString"
_HwMirrorGroupMirrorIfIndexList_Object = MibTableColumn
hwMirrorGroupMirrorIfIndexList = _HwMirrorGroupMirrorIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1, 3),
    _HwMirrorGroupMirrorIfIndexList_Type()
)
hwMirrorGroupMirrorIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMirrorGroupMirrorIfIndexList.setStatus("current")
_HwMirrorGroupMonitorIfIndex_Type = Integer32
_HwMirrorGroupMonitorIfIndex_Object = MibTableColumn
hwMirrorGroupMonitorIfIndex = _HwMirrorGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1, 4),
    _HwMirrorGroupMonitorIfIndex_Type()
)
hwMirrorGroupMonitorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMirrorGroupMonitorIfIndex.setStatus("current")
_HwMirrorGroupRowStatus_Type = RowStatus
_HwMirrorGroupRowStatus_Object = MibTableColumn
hwMirrorGroupRowStatus = _HwMirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 13, 1, 5),
    _HwMirrorGroupRowStatus_Type()
)
hwMirrorGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMirrorGroupRowStatus.setStatus("current")
_HwFlowtempTable_Object = MibTable
hwFlowtempTable = _HwFlowtempTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14)
)
if mibBuilder.loadTexts:
    hwFlowtempTable.setStatus("current")
_HwFlowtempEntry_Object = MibTableRow
hwFlowtempEntry = _HwFlowtempEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1)
)
hwFlowtempEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwFlowtempIndex"),
)
if mibBuilder.loadTexts:
    hwFlowtempEntry.setStatus("current")


class _HwFlowtempIndex_Type(Integer32):
    """Custom type hwFlowtempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user-defined", 2))
    )


_HwFlowtempIndex_Type.__name__ = "Integer32"
_HwFlowtempIndex_Object = MibTableColumn
hwFlowtempIndex = _HwFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 1),
    _HwFlowtempIndex_Type()
)
hwFlowtempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwFlowtempIndex.setStatus("current")
_HwFlowtempIpProtocol_Type = TruthValue
_HwFlowtempIpProtocol_Object = MibTableColumn
hwFlowtempIpProtocol = _HwFlowtempIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 2),
    _HwFlowtempIpProtocol_Type()
)
hwFlowtempIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempIpProtocol.setStatus("current")
_HwFlowtempTcpFlag_Type = TruthValue
_HwFlowtempTcpFlag_Object = MibTableColumn
hwFlowtempTcpFlag = _HwFlowtempTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 3),
    _HwFlowtempTcpFlag_Type()
)
hwFlowtempTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempTcpFlag.setStatus("current")
_HwFlowtempSPort_Type = TruthValue
_HwFlowtempSPort_Object = MibTableColumn
hwFlowtempSPort = _HwFlowtempSPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 4),
    _HwFlowtempSPort_Type()
)
hwFlowtempSPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempSPort.setStatus("current")
_HwFlowtempDPort_Type = TruthValue
_HwFlowtempDPort_Object = MibTableColumn
hwFlowtempDPort = _HwFlowtempDPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 5),
    _HwFlowtempDPort_Type()
)
hwFlowtempDPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDPort.setStatus("current")
_HwFlowtempIcmpType_Type = TruthValue
_HwFlowtempIcmpType_Object = MibTableColumn
hwFlowtempIcmpType = _HwFlowtempIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 6),
    _HwFlowtempIcmpType_Type()
)
hwFlowtempIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempIcmpType.setStatus("current")
_HwFlowtempIcmpCode_Type = TruthValue
_HwFlowtempIcmpCode_Object = MibTableColumn
hwFlowtempIcmpCode = _HwFlowtempIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 7),
    _HwFlowtempIcmpCode_Type()
)
hwFlowtempIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempIcmpCode.setStatus("current")
_HwFlowtempFragment_Type = TruthValue
_HwFlowtempFragment_Object = MibTableColumn
hwFlowtempFragment = _HwFlowtempFragment_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 8),
    _HwFlowtempFragment_Type()
)
hwFlowtempFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempFragment.setStatus("current")
_HwFlowtempDscp_Type = TruthValue
_HwFlowtempDscp_Object = MibTableColumn
hwFlowtempDscp = _HwFlowtempDscp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 9),
    _HwFlowtempDscp_Type()
)
hwFlowtempDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDscp.setStatus("current")
_HwFlowtempIpPre_Type = TruthValue
_HwFlowtempIpPre_Object = MibTableColumn
hwFlowtempIpPre = _HwFlowtempIpPre_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 10),
    _HwFlowtempIpPre_Type()
)
hwFlowtempIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempIpPre.setStatus("current")
_HwFlowtempTos_Type = TruthValue
_HwFlowtempTos_Object = MibTableColumn
hwFlowtempTos = _HwFlowtempTos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 11),
    _HwFlowtempTos_Type()
)
hwFlowtempTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempTos.setStatus("current")
_HwFlowtempSIp_Type = TruthValue
_HwFlowtempSIp_Object = MibTableColumn
hwFlowtempSIp = _HwFlowtempSIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 12),
    _HwFlowtempSIp_Type()
)
hwFlowtempSIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempSIp.setStatus("current")
_HwFlowtempSIpMask_Type = IpAddress
_HwFlowtempSIpMask_Object = MibTableColumn
hwFlowtempSIpMask = _HwFlowtempSIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 13),
    _HwFlowtempSIpMask_Type()
)
hwFlowtempSIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempSIpMask.setStatus("current")
_HwFlowtempDIp_Type = TruthValue
_HwFlowtempDIp_Object = MibTableColumn
hwFlowtempDIp = _HwFlowtempDIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 14),
    _HwFlowtempDIp_Type()
)
hwFlowtempDIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDIp.setStatus("current")
_HwFlowtempDIpMask_Type = IpAddress
_HwFlowtempDIpMask_Object = MibTableColumn
hwFlowtempDIpMask = _HwFlowtempDIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 15),
    _HwFlowtempDIpMask_Type()
)
hwFlowtempDIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDIpMask.setStatus("current")
_HwFlowtempEthProtocol_Type = TruthValue
_HwFlowtempEthProtocol_Object = MibTableColumn
hwFlowtempEthProtocol = _HwFlowtempEthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 16),
    _HwFlowtempEthProtocol_Type()
)
hwFlowtempEthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempEthProtocol.setStatus("current")
_HwFlowtempSMac_Type = TruthValue
_HwFlowtempSMac_Object = MibTableColumn
hwFlowtempSMac = _HwFlowtempSMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 17),
    _HwFlowtempSMac_Type()
)
hwFlowtempSMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempSMac.setStatus("current")
_HwFlowtempSMacMask_Type = MacAddress
_HwFlowtempSMacMask_Object = MibTableColumn
hwFlowtempSMacMask = _HwFlowtempSMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 18),
    _HwFlowtempSMacMask_Type()
)
hwFlowtempSMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempSMacMask.setStatus("current")
_HwFlowtempDMac_Type = TruthValue
_HwFlowtempDMac_Object = MibTableColumn
hwFlowtempDMac = _HwFlowtempDMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 19),
    _HwFlowtempDMac_Type()
)
hwFlowtempDMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDMac.setStatus("current")
_HwFlowtempDMacMask_Type = MacAddress
_HwFlowtempDMacMask_Object = MibTableColumn
hwFlowtempDMacMask = _HwFlowtempDMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 20),
    _HwFlowtempDMacMask_Type()
)
hwFlowtempDMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempDMacMask.setStatus("current")
_HwFlowtempVpn_Type = TruthValue
_HwFlowtempVpn_Object = MibTableColumn
hwFlowtempVpn = _HwFlowtempVpn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 21),
    _HwFlowtempVpn_Type()
)
hwFlowtempVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempVpn.setStatus("current")
_HwFlowtempRowStatus_Type = RowStatus
_HwFlowtempRowStatus_Object = MibTableColumn
hwFlowtempRowStatus = _HwFlowtempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 22),
    _HwFlowtempRowStatus_Type()
)
hwFlowtempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempRowStatus.setStatus("current")
_HwFlowtempVlanId_Type = TruthValue
_HwFlowtempVlanId_Object = MibTableColumn
hwFlowtempVlanId = _HwFlowtempVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 23),
    _HwFlowtempVlanId_Type()
)
hwFlowtempVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempVlanId.setStatus("current")
_HwFlowtempCos_Type = TruthValue
_HwFlowtempCos_Object = MibTableColumn
hwFlowtempCos = _HwFlowtempCos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 14, 1, 24),
    _HwFlowtempCos_Type()
)
hwFlowtempCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempCos.setStatus("current")
_HwFlowtempEnableTable_Object = MibTable
hwFlowtempEnableTable = _HwFlowtempEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 15)
)
if mibBuilder.loadTexts:
    hwFlowtempEnableTable.setStatus("current")
_HwFlowtempEnableEntry_Object = MibTableRow
hwFlowtempEnableEntry = _HwFlowtempEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 15, 1)
)
hwFlowtempEnableEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwFlowtempEnableIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwFlowtempEnableVlanID"),
)
if mibBuilder.loadTexts:
    hwFlowtempEnableEntry.setStatus("current")
_HwFlowtempEnableIfIndex_Type = Integer32
_HwFlowtempEnableIfIndex_Object = MibTableColumn
hwFlowtempEnableIfIndex = _HwFlowtempEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 15, 1, 1),
    _HwFlowtempEnableIfIndex_Type()
)
hwFlowtempEnableIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempEnableIfIndex.setStatus("current")


class _HwFlowtempEnableVlanID_Type(Integer32):
    """Custom type hwFlowtempEnableVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwFlowtempEnableVlanID_Type.__name__ = "Integer32"
_HwFlowtempEnableVlanID_Object = MibTableColumn
hwFlowtempEnableVlanID = _HwFlowtempEnableVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 15, 1, 2),
    _HwFlowtempEnableVlanID_Type()
)
hwFlowtempEnableVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwFlowtempEnableVlanID.setStatus("current")


class _HwFlowtempEnableFlowtempIndex_Type(Integer32):
    """Custom type hwFlowtempEnableFlowtempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user-defined", 2))
    )


_HwFlowtempEnableFlowtempIndex_Type.__name__ = "Integer32"
_HwFlowtempEnableFlowtempIndex_Object = MibTableColumn
hwFlowtempEnableFlowtempIndex = _HwFlowtempEnableFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 15, 1, 3),
    _HwFlowtempEnableFlowtempIndex_Type()
)
hwFlowtempEnableFlowtempIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwFlowtempEnableFlowtempIndex.setStatus("current")
_HwTrafficShapeTable_Object = MibTable
hwTrafficShapeTable = _HwTrafficShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16)
)
if mibBuilder.loadTexts:
    hwTrafficShapeTable.setStatus("current")
_HwTrafficShapeEntry_Object = MibTableRow
hwTrafficShapeEntry = _HwTrafficShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1)
)
hwTrafficShapeEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwTrafficShapeIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwTrafficShapeQueueId"),
)
if mibBuilder.loadTexts:
    hwTrafficShapeEntry.setStatus("current")
_HwTrafficShapeIfIndex_Type = Integer32
_HwTrafficShapeIfIndex_Object = MibTableColumn
hwTrafficShapeIfIndex = _HwTrafficShapeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 1),
    _HwTrafficShapeIfIndex_Type()
)
hwTrafficShapeIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeIfIndex.setStatus("current")


class _HwTrafficShapeQueueId_Type(Integer32):
    """Custom type hwTrafficShapeQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HwTrafficShapeQueueId_Type.__name__ = "Integer32"
_HwTrafficShapeQueueId_Object = MibTableColumn
hwTrafficShapeQueueId = _HwTrafficShapeQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 2),
    _HwTrafficShapeQueueId_Type()
)
hwTrafficShapeQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeQueueId.setStatus("current")
_HwTrafficShapeMaxRate_Type = Integer32
_HwTrafficShapeMaxRate_Object = MibTableColumn
hwTrafficShapeMaxRate = _HwTrafficShapeMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 3),
    _HwTrafficShapeMaxRate_Type()
)
hwTrafficShapeMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeMaxRate.setStatus("current")
_HwTrafficShapeBurstSize_Type = Integer32
_HwTrafficShapeBurstSize_Object = MibTableColumn
hwTrafficShapeBurstSize = _HwTrafficShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 4),
    _HwTrafficShapeBurstSize_Type()
)
hwTrafficShapeBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeBurstSize.setStatus("current")


class _HwTrafficShapeBufferLimit_Type(Integer32):
    """Custom type hwTrafficShapeBufferLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 8000),
    )


_HwTrafficShapeBufferLimit_Type.__name__ = "Integer32"
_HwTrafficShapeBufferLimit_Object = MibTableColumn
hwTrafficShapeBufferLimit = _HwTrafficShapeBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 5),
    _HwTrafficShapeBufferLimit_Type()
)
hwTrafficShapeBufferLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeBufferLimit.setStatus("current")
_HwTrafficShapeRowStatus_Type = RowStatus
_HwTrafficShapeRowStatus_Object = MibTableColumn
hwTrafficShapeRowStatus = _HwTrafficShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 16, 1, 6),
    _HwTrafficShapeRowStatus_Type()
)
hwTrafficShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTrafficShapeRowStatus.setStatus("current")
_HwPortQueueTable_Object = MibTable
hwPortQueueTable = _HwPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17)
)
if mibBuilder.loadTexts:
    hwPortQueueTable.setStatus("current")
_HwPortQueueEntry_Object = MibTableRow
hwPortQueueEntry = _HwPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17, 1)
)
hwPortQueueEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwPortQueueIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwPortQueueQueueID"),
)
if mibBuilder.loadTexts:
    hwPortQueueEntry.setStatus("current")
_HwPortQueueIfIndex_Type = Integer32
_HwPortQueueIfIndex_Object = MibTableColumn
hwPortQueueIfIndex = _HwPortQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17, 1, 1),
    _HwPortQueueIfIndex_Type()
)
hwPortQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortQueueIfIndex.setStatus("current")


class _HwPortQueueQueueID_Type(Integer32):
    """Custom type hwPortQueueQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPortQueueQueueID_Type.__name__ = "Integer32"
_HwPortQueueQueueID_Object = MibTableColumn
hwPortQueueQueueID = _HwPortQueueQueueID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17, 1, 2),
    _HwPortQueueQueueID_Type()
)
hwPortQueueQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortQueueQueueID.setStatus("current")


class _HwPortQueueWrrPriority_Type(Integer32):
    """Custom type hwPortQueueWrrPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr-high-priority", 2),
          ("wrr-low-priority", 3))
    )


_HwPortQueueWrrPriority_Type.__name__ = "Integer32"
_HwPortQueueWrrPriority_Object = MibTableColumn
hwPortQueueWrrPriority = _HwPortQueueWrrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17, 1, 3),
    _HwPortQueueWrrPriority_Type()
)
hwPortQueueWrrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortQueueWrrPriority.setStatus("current")


class _HwPortQueueWeight_Type(Integer32):
    """Custom type hwPortQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HwPortQueueWeight_Type.__name__ = "Integer32"
_HwPortQueueWeight_Object = MibTableColumn
hwPortQueueWeight = _HwPortQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 17, 1, 4),
    _HwPortQueueWeight_Type()
)
hwPortQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortQueueWeight.setStatus("current")
_HwDropModeTable_Object = MibTable
hwDropModeTable = _HwDropModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 18)
)
if mibBuilder.loadTexts:
    hwDropModeTable.setStatus("current")
_HwDropModeEntry_Object = MibTableRow
hwDropModeEntry = _HwDropModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 18, 1)
)
hwDropModeEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDropModeIfIndex"),
)
if mibBuilder.loadTexts:
    hwDropModeEntry.setStatus("current")
_HwDropModeIfIndex_Type = Integer32
_HwDropModeIfIndex_Object = MibTableColumn
hwDropModeIfIndex = _HwDropModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 18, 1, 1),
    _HwDropModeIfIndex_Type()
)
hwDropModeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDropModeIfIndex.setStatus("current")


class _HwDropModeMode_Type(Integer32):
    """Custom type hwDropModeMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("random-detect", 1),
          ("tail-drop", 2))
    )


_HwDropModeMode_Type.__name__ = "Integer32"
_HwDropModeMode_Object = MibTableColumn
hwDropModeMode = _HwDropModeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 18, 1, 2),
    _HwDropModeMode_Type()
)
hwDropModeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDropModeMode.setStatus("current")


class _HwDropModeWredIndex_Type(Integer32):
    """Custom type hwDropModeWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwDropModeWredIndex_Type.__name__ = "Integer32"
_HwDropModeWredIndex_Object = MibTableColumn
hwDropModeWredIndex = _HwDropModeWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 18, 1, 3),
    _HwDropModeWredIndex_Type()
)
hwDropModeWredIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDropModeWredIndex.setStatus("current")
_HwWredTable_Object = MibTable
hwWredTable = _HwWredTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19)
)
if mibBuilder.loadTexts:
    hwWredTable.setStatus("current")
_HwWredEntry_Object = MibTableRow
hwWredEntry = _HwWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1)
)
hwWredEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwWredIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwWredQueueId"),
)
if mibBuilder.loadTexts:
    hwWredEntry.setStatus("current")


class _HwWredIndex_Type(Integer32):
    """Custom type hwWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HwWredIndex_Type.__name__ = "Integer32"
_HwWredIndex_Object = MibTableColumn
hwWredIndex = _HwWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 1),
    _HwWredIndex_Type()
)
hwWredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWredIndex.setStatus("current")


class _HwWredQueueId_Type(Integer32):
    """Custom type hwWredQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwWredQueueId_Type.__name__ = "Integer32"
_HwWredQueueId_Object = MibTableColumn
hwWredQueueId = _HwWredQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 2),
    _HwWredQueueId_Type()
)
hwWredQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWredQueueId.setStatus("current")


class _HwWredGreenMinThreshold_Type(Integer32):
    """Custom type hwWredGreenMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredGreenMinThreshold_Type.__name__ = "Integer32"
_HwWredGreenMinThreshold_Object = MibTableColumn
hwWredGreenMinThreshold = _HwWredGreenMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 3),
    _HwWredGreenMinThreshold_Type()
)
hwWredGreenMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredGreenMinThreshold.setStatus("current")


class _HwWredGreenMaxThreshold_Type(Integer32):
    """Custom type hwWredGreenMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredGreenMaxThreshold_Type.__name__ = "Integer32"
_HwWredGreenMaxThreshold_Object = MibTableColumn
hwWredGreenMaxThreshold = _HwWredGreenMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 4),
    _HwWredGreenMaxThreshold_Type()
)
hwWredGreenMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredGreenMaxThreshold.setStatus("current")


class _HwWredGreenMaxProb_Type(Integer32):
    """Custom type hwWredGreenMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwWredGreenMaxProb_Type.__name__ = "Integer32"
_HwWredGreenMaxProb_Object = MibTableColumn
hwWredGreenMaxProb = _HwWredGreenMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 5),
    _HwWredGreenMaxProb_Type()
)
hwWredGreenMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredGreenMaxProb.setStatus("current")


class _HwWredYellowMinThreshold_Type(Integer32):
    """Custom type hwWredYellowMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredYellowMinThreshold_Type.__name__ = "Integer32"
_HwWredYellowMinThreshold_Object = MibTableColumn
hwWredYellowMinThreshold = _HwWredYellowMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 6),
    _HwWredYellowMinThreshold_Type()
)
hwWredYellowMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredYellowMinThreshold.setStatus("current")


class _HwWredYellowMaxThreshold_Type(Integer32):
    """Custom type hwWredYellowMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredYellowMaxThreshold_Type.__name__ = "Integer32"
_HwWredYellowMaxThreshold_Object = MibTableColumn
hwWredYellowMaxThreshold = _HwWredYellowMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 7),
    _HwWredYellowMaxThreshold_Type()
)
hwWredYellowMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredYellowMaxThreshold.setStatus("current")


class _HwWredYellowMaxProb_Type(Integer32):
    """Custom type hwWredYellowMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwWredYellowMaxProb_Type.__name__ = "Integer32"
_HwWredYellowMaxProb_Object = MibTableColumn
hwWredYellowMaxProb = _HwWredYellowMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 8),
    _HwWredYellowMaxProb_Type()
)
hwWredYellowMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredYellowMaxProb.setStatus("current")


class _HwWredRedMinThreshold_Type(Integer32):
    """Custom type hwWredRedMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredRedMinThreshold_Type.__name__ = "Integer32"
_HwWredRedMinThreshold_Object = MibTableColumn
hwWredRedMinThreshold = _HwWredRedMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 9),
    _HwWredRedMinThreshold_Type()
)
hwWredRedMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredRedMinThreshold.setStatus("current")


class _HwWredRedMaxThreshold_Type(Integer32):
    """Custom type hwWredRedMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwWredRedMaxThreshold_Type.__name__ = "Integer32"
_HwWredRedMaxThreshold_Object = MibTableColumn
hwWredRedMaxThreshold = _HwWredRedMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 10),
    _HwWredRedMaxThreshold_Type()
)
hwWredRedMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredRedMaxThreshold.setStatus("current")


class _HwWredRedMaxProb_Type(Integer32):
    """Custom type hwWredRedMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwWredRedMaxProb_Type.__name__ = "Integer32"
_HwWredRedMaxProb_Object = MibTableColumn
hwWredRedMaxProb = _HwWredRedMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 11),
    _HwWredRedMaxProb_Type()
)
hwWredRedMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredRedMaxProb.setStatus("current")


class _HwWredExponent_Type(Integer32):
    """Custom type hwWredExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HwWredExponent_Type.__name__ = "Integer32"
_HwWredExponent_Object = MibTableColumn
hwWredExponent = _HwWredExponent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 19, 1, 12),
    _HwWredExponent_Type()
)
hwWredExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWredExponent.setStatus("current")
_HwCosToLocalPrecedenceMapTable_Object = MibTable
hwCosToLocalPrecedenceMapTable = _HwCosToLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 20)
)
if mibBuilder.loadTexts:
    hwCosToLocalPrecedenceMapTable.setStatus("current")
_HwCosToLocalPrecedenceMapEntry_Object = MibTableRow
hwCosToLocalPrecedenceMapEntry = _HwCosToLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 20, 1)
)
hwCosToLocalPrecedenceMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwCosToLocalPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hwCosToLocalPrecedenceMapEntry.setStatus("current")


class _HwCosToLocalPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hwCosToLocalPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwCosToLocalPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_HwCosToLocalPrecedenceMapCosIndex_Object = MibTableColumn
hwCosToLocalPrecedenceMapCosIndex = _HwCosToLocalPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 20, 1, 1),
    _HwCosToLocalPrecedenceMapCosIndex_Type()
)
hwCosToLocalPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCosToLocalPrecedenceMapCosIndex.setStatus("current")


class _HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type(Integer32):
    """Custom type hwCosToLocalPrecedenceMapLocalPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type.__name__ = "Integer32"
_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Object = MibTableColumn
hwCosToLocalPrecedenceMapLocalPrecedenceValue = _HwCosToLocalPrecedenceMapLocalPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 20, 1, 2),
    _HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type()
)
hwCosToLocalPrecedenceMapLocalPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCosToLocalPrecedenceMapLocalPrecedenceValue.setStatus("current")
_HwCosToDropPrecedenceMapTable_Object = MibTable
hwCosToDropPrecedenceMapTable = _HwCosToDropPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 21)
)
if mibBuilder.loadTexts:
    hwCosToDropPrecedenceMapTable.setStatus("current")
_HwCosToDropPrecedenceMapEntry_Object = MibTableRow
hwCosToDropPrecedenceMapEntry = _HwCosToDropPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 21, 1)
)
hwCosToDropPrecedenceMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwCosToDropPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hwCosToDropPrecedenceMapEntry.setStatus("current")


class _HwCosToDropPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hwCosToDropPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwCosToDropPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_HwCosToDropPrecedenceMapCosIndex_Object = MibTableColumn
hwCosToDropPrecedenceMapCosIndex = _HwCosToDropPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 21, 1, 1),
    _HwCosToDropPrecedenceMapCosIndex_Type()
)
hwCosToDropPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCosToDropPrecedenceMapCosIndex.setStatus("current")


class _HwCosToDropPrecedenceMapDropPrecedenceValue_Type(Integer32):
    """Custom type hwCosToDropPrecedenceMapDropPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwCosToDropPrecedenceMapDropPrecedenceValue_Type.__name__ = "Integer32"
_HwCosToDropPrecedenceMapDropPrecedenceValue_Object = MibTableColumn
hwCosToDropPrecedenceMapDropPrecedenceValue = _HwCosToDropPrecedenceMapDropPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 21, 1, 2),
    _HwCosToDropPrecedenceMapDropPrecedenceValue_Type()
)
hwCosToDropPrecedenceMapDropPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCosToDropPrecedenceMapDropPrecedenceValue.setStatus("current")
_HwDscpMapTable_Object = MibTable
hwDscpMapTable = _HwDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22)
)
if mibBuilder.loadTexts:
    hwDscpMapTable.setStatus("current")
_HwDscpMapEntry_Object = MibTableRow
hwDscpMapEntry = _HwDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1)
)
hwDscpMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDscpMapConformLevel"),
    (0, "HUAWEI-LswQos-MIB", "hwDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hwDscpMapEntry.setStatus("current")


class _HwDscpMapConformLevel_Type(Integer32):
    """Custom type hwDscpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwDscpMapConformLevel_Type.__name__ = "Integer32"
_HwDscpMapConformLevel_Object = MibTableColumn
hwDscpMapConformLevel = _HwDscpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 1),
    _HwDscpMapConformLevel_Type()
)
hwDscpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDscpMapConformLevel.setStatus("current")


class _HwDscpMapDscpIndex_Type(Integer32):
    """Custom type hwDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpMapDscpIndex_Type.__name__ = "Integer32"
_HwDscpMapDscpIndex_Object = MibTableColumn
hwDscpMapDscpIndex = _HwDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 2),
    _HwDscpMapDscpIndex_Type()
)
hwDscpMapDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDscpMapDscpIndex.setStatus("current")


class _HwDscpMapDscpValue_Type(Integer32):
    """Custom type hwDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpMapDscpValue_Type.__name__ = "Integer32"
_HwDscpMapDscpValue_Object = MibTableColumn
hwDscpMapDscpValue = _HwDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 3),
    _HwDscpMapDscpValue_Type()
)
hwDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpMapDscpValue.setStatus("current")


class _HwDscpMapExpValue_Type(Integer32):
    """Custom type hwDscpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDscpMapExpValue_Type.__name__ = "Integer32"
_HwDscpMapExpValue_Object = MibTableColumn
hwDscpMapExpValue = _HwDscpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 4),
    _HwDscpMapExpValue_Type()
)
hwDscpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpMapExpValue.setStatus("current")


class _HwDscpMapCosValue_Type(Integer32):
    """Custom type hwDscpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDscpMapCosValue_Type.__name__ = "Integer32"
_HwDscpMapCosValue_Object = MibTableColumn
hwDscpMapCosValue = _HwDscpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 5),
    _HwDscpMapCosValue_Type()
)
hwDscpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpMapCosValue.setStatus("current")


class _HwDscpMapLocalPrecedence_Type(Integer32):
    """Custom type hwDscpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDscpMapLocalPrecedence_Type.__name__ = "Integer32"
_HwDscpMapLocalPrecedence_Object = MibTableColumn
hwDscpMapLocalPrecedence = _HwDscpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 6),
    _HwDscpMapLocalPrecedence_Type()
)
hwDscpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpMapLocalPrecedence.setStatus("current")


class _HwDscpMapDropPrecedence_Type(Integer32):
    """Custom type hwDscpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwDscpMapDropPrecedence_Type.__name__ = "Integer32"
_HwDscpMapDropPrecedence_Object = MibTableColumn
hwDscpMapDropPrecedence = _HwDscpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 22, 1, 7),
    _HwDscpMapDropPrecedence_Type()
)
hwDscpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpMapDropPrecedence.setStatus("current")
_HwExpMapTable_Object = MibTable
hwExpMapTable = _HwExpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23)
)
if mibBuilder.loadTexts:
    hwExpMapTable.setStatus("current")
_HwExpMapEntry_Object = MibTableRow
hwExpMapEntry = _HwExpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1)
)
hwExpMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwExpMapConformLevel"),
    (0, "HUAWEI-LswQos-MIB", "hwExpMapExpIndex"),
)
if mibBuilder.loadTexts:
    hwExpMapEntry.setStatus("current")


class _HwExpMapConformLevel_Type(Integer32):
    """Custom type hwExpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwExpMapConformLevel_Type.__name__ = "Integer32"
_HwExpMapConformLevel_Object = MibTableColumn
hwExpMapConformLevel = _HwExpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 1),
    _HwExpMapConformLevel_Type()
)
hwExpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExpMapConformLevel.setStatus("current")


class _HwExpMapExpIndex_Type(Integer32):
    """Custom type hwExpMapExpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwExpMapExpIndex_Type.__name__ = "Integer32"
_HwExpMapExpIndex_Object = MibTableColumn
hwExpMapExpIndex = _HwExpMapExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 2),
    _HwExpMapExpIndex_Type()
)
hwExpMapExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExpMapExpIndex.setStatus("current")


class _HwExpMapDscpValue_Type(Integer32):
    """Custom type hwExpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwExpMapDscpValue_Type.__name__ = "Integer32"
_HwExpMapDscpValue_Object = MibTableColumn
hwExpMapDscpValue = _HwExpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 3),
    _HwExpMapDscpValue_Type()
)
hwExpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExpMapDscpValue.setStatus("current")


class _HwExpMapExpValue_Type(Integer32):
    """Custom type hwExpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwExpMapExpValue_Type.__name__ = "Integer32"
_HwExpMapExpValue_Object = MibTableColumn
hwExpMapExpValue = _HwExpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 4),
    _HwExpMapExpValue_Type()
)
hwExpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExpMapExpValue.setStatus("current")


class _HwExpMapCosValue_Type(Integer32):
    """Custom type hwExpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwExpMapCosValue_Type.__name__ = "Integer32"
_HwExpMapCosValue_Object = MibTableColumn
hwExpMapCosValue = _HwExpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 5),
    _HwExpMapCosValue_Type()
)
hwExpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExpMapCosValue.setStatus("current")


class _HwExpMapLocalPrecedence_Type(Integer32):
    """Custom type hwExpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwExpMapLocalPrecedence_Type.__name__ = "Integer32"
_HwExpMapLocalPrecedence_Object = MibTableColumn
hwExpMapLocalPrecedence = _HwExpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 6),
    _HwExpMapLocalPrecedence_Type()
)
hwExpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExpMapLocalPrecedence.setStatus("current")


class _HwExpMapDropPrecedence_Type(Integer32):
    """Custom type hwExpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwExpMapDropPrecedence_Type.__name__ = "Integer32"
_HwExpMapDropPrecedence_Object = MibTableColumn
hwExpMapDropPrecedence = _HwExpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 23, 1, 7),
    _HwExpMapDropPrecedence_Type()
)
hwExpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwExpMapDropPrecedence.setStatus("current")
_HwLocalPrecedenceMapTable_Object = MibTable
hwLocalPrecedenceMapTable = _HwLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 24)
)
if mibBuilder.loadTexts:
    hwLocalPrecedenceMapTable.setStatus("current")
_HwLocalPrecedenceMapEntry_Object = MibTableRow
hwLocalPrecedenceMapEntry = _HwLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 24, 1)
)
hwLocalPrecedenceMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwLocalPrecedenceMapConformLevel"),
    (0, "HUAWEI-LswQos-MIB", "hwLocalPrecedenceMapLocalPrecedenceIndex"),
)
if mibBuilder.loadTexts:
    hwLocalPrecedenceMapEntry.setStatus("current")


class _HwLocalPrecedenceMapConformLevel_Type(Integer32):
    """Custom type hwLocalPrecedenceMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwLocalPrecedenceMapConformLevel_Type.__name__ = "Integer32"
_HwLocalPrecedenceMapConformLevel_Object = MibTableColumn
hwLocalPrecedenceMapConformLevel = _HwLocalPrecedenceMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 24, 1, 1),
    _HwLocalPrecedenceMapConformLevel_Type()
)
hwLocalPrecedenceMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalPrecedenceMapConformLevel.setStatus("current")


class _HwLocalPrecedenceMapLocalPrecedenceIndex_Type(Integer32):
    """Custom type hwLocalPrecedenceMapLocalPrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwLocalPrecedenceMapLocalPrecedenceIndex_Type.__name__ = "Integer32"
_HwLocalPrecedenceMapLocalPrecedenceIndex_Object = MibTableColumn
hwLocalPrecedenceMapLocalPrecedenceIndex = _HwLocalPrecedenceMapLocalPrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 24, 1, 2),
    _HwLocalPrecedenceMapLocalPrecedenceIndex_Type()
)
hwLocalPrecedenceMapLocalPrecedenceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalPrecedenceMapLocalPrecedenceIndex.setStatus("current")


class _HwLocalPrecedenceMapCosValue_Type(Integer32):
    """Custom type hwLocalPrecedenceMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwLocalPrecedenceMapCosValue_Type.__name__ = "Integer32"
_HwLocalPrecedenceMapCosValue_Object = MibTableColumn
hwLocalPrecedenceMapCosValue = _HwLocalPrecedenceMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 24, 1, 3),
    _HwLocalPrecedenceMapCosValue_Type()
)
hwLocalPrecedenceMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalPrecedenceMapCosValue.setStatus("current")
_HwPortWredTable_Object = MibTable
hwPortWredTable = _HwPortWredTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25)
)
if mibBuilder.loadTexts:
    hwPortWredTable.setStatus("current")
_HwPortWredEntry_Object = MibTableRow
hwPortWredEntry = _HwPortWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25, 1)
)
hwPortWredEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwPortWredIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwPortWredQueueID"),
)
if mibBuilder.loadTexts:
    hwPortWredEntry.setStatus("current")
_HwPortWredIfIndex_Type = Integer32
_HwPortWredIfIndex_Object = MibTableColumn
hwPortWredIfIndex = _HwPortWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25, 1, 1),
    _HwPortWredIfIndex_Type()
)
hwPortWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortWredIfIndex.setStatus("current")


class _HwPortWredQueueID_Type(Integer32):
    """Custom type hwPortWredQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPortWredQueueID_Type.__name__ = "Integer32"
_HwPortWredQueueID_Object = MibTableColumn
hwPortWredQueueID = _HwPortWredQueueID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25, 1, 2),
    _HwPortWredQueueID_Type()
)
hwPortWredQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPortWredQueueID.setStatus("current")


class _HwPortWredQueueStartLength_Type(Integer32):
    """Custom type hwPortWredQueueStartLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwPortWredQueueStartLength_Type.__name__ = "Integer32"
_HwPortWredQueueStartLength_Object = MibTableColumn
hwPortWredQueueStartLength = _HwPortWredQueueStartLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25, 1, 3),
    _HwPortWredQueueStartLength_Type()
)
hwPortWredQueueStartLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortWredQueueStartLength.setStatus("current")


class _HwPortWredQueueProbability_Type(Integer32):
    """Custom type hwPortWredQueueProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwPortWredQueueProbability_Type.__name__ = "Integer32"
_HwPortWredQueueProbability_Object = MibTableColumn
hwPortWredQueueProbability = _HwPortWredQueueProbability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 25, 1, 4),
    _HwPortWredQueueProbability_Type()
)
hwPortWredQueueProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortWredQueueProbability.setStatus("current")
_HwMirroringGroupTable_Object = MibTable
hwMirroringGroupTable = _HwMirroringGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26)
)
if mibBuilder.loadTexts:
    hwMirroringGroupTable.setStatus("current")
_HwMirroringGroupEntry_Object = MibTableRow
hwMirroringGroupEntry = _HwMirroringGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26, 1)
)
hwMirroringGroupEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupEntry.setStatus("current")


class _HwMirroringGroupID_Type(Integer32):
    """Custom type hwMirroringGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HwMirroringGroupID_Type.__name__ = "Integer32"
_HwMirroringGroupID_Object = MibTableColumn
hwMirroringGroupID = _HwMirroringGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26, 1, 1),
    _HwMirroringGroupID_Type()
)
hwMirroringGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMirroringGroupID.setStatus("current")


class _HwMirroringGroupType_Type(Integer32):
    """Custom type hwMirroringGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote-destination", 3),
          ("remote-source", 2))
    )


_HwMirroringGroupType_Type.__name__ = "Integer32"
_HwMirroringGroupType_Object = MibTableColumn
hwMirroringGroupType = _HwMirroringGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26, 1, 2),
    _HwMirroringGroupType_Type()
)
hwMirroringGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupType.setStatus("current")


class _HwMirroringGroupStatus_Type(Integer32):
    """Custom type hwMirroringGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HwMirroringGroupStatus_Type.__name__ = "Integer32"
_HwMirroringGroupStatus_Object = MibTableColumn
hwMirroringGroupStatus = _HwMirroringGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26, 1, 3),
    _HwMirroringGroupStatus_Type()
)
hwMirroringGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMirroringGroupStatus.setStatus("current")
_HwMirroringGroupRowStatus_Type = RowStatus
_HwMirroringGroupRowStatus_Object = MibTableColumn
hwMirroringGroupRowStatus = _HwMirroringGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 26, 1, 4),
    _HwMirroringGroupRowStatus_Type()
)
hwMirroringGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupRowStatus.setStatus("current")
_HwMirroringGroupMirrorTable_Object = MibTable
hwMirroringGroupMirrorTable = _HwMirroringGroupMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27)
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorTable.setStatus("current")
_HwMirroringGroupMirrorEntry_Object = MibTableRow
hwMirroringGroupMirrorEntry = _HwMirroringGroupMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1)
)
hwMirroringGroupMirrorEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorEntry.setStatus("current")
_HwMirroringGroupMirrorInboundIfIndexList_Type = OctetString
_HwMirroringGroupMirrorInboundIfIndexList_Object = MibTableColumn
hwMirroringGroupMirrorInboundIfIndexList = _HwMirroringGroupMirrorInboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1, 1),
    _HwMirroringGroupMirrorInboundIfIndexList_Type()
)
hwMirroringGroupMirrorInboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorInboundIfIndexList.setStatus("current")
_HwMirroringGroupMirrorOutboundIfIndexList_Type = OctetString
_HwMirroringGroupMirrorOutboundIfIndexList_Object = MibTableColumn
hwMirroringGroupMirrorOutboundIfIndexList = _HwMirroringGroupMirrorOutboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1, 2),
    _HwMirroringGroupMirrorOutboundIfIndexList_Type()
)
hwMirroringGroupMirrorOutboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorOutboundIfIndexList.setStatus("current")
_HwMirroringGroupMirrorRowStatus_Type = RowStatus
_HwMirroringGroupMirrorRowStatus_Object = MibTableColumn
hwMirroringGroupMirrorRowStatus = _HwMirroringGroupMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1, 3),
    _HwMirroringGroupMirrorRowStatus_Type()
)
hwMirroringGroupMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorRowStatus.setStatus("current")
_HwMirroringGroupMirrorInTypeList_Type = OctetString
_HwMirroringGroupMirrorInTypeList_Object = MibTableColumn
hwMirroringGroupMirrorInTypeList = _HwMirroringGroupMirrorInTypeList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1, 4),
    _HwMirroringGroupMirrorInTypeList_Type()
)
hwMirroringGroupMirrorInTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorInTypeList.setStatus("current")
_HwMirroringGroupMirrorOutTypeList_Type = OctetString
_HwMirroringGroupMirrorOutTypeList_Object = MibTableColumn
hwMirroringGroupMirrorOutTypeList = _HwMirroringGroupMirrorOutTypeList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 27, 1, 5),
    _HwMirroringGroupMirrorOutTypeList_Type()
)
hwMirroringGroupMirrorOutTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorOutTypeList.setStatus("current")
_HwMirroringGroupMonitorTable_Object = MibTable
hwMirroringGroupMonitorTable = _HwMirroringGroupMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 28)
)
if mibBuilder.loadTexts:
    hwMirroringGroupMonitorTable.setStatus("current")
_HwMirroringGroupMonitorEntry_Object = MibTableRow
hwMirroringGroupMonitorEntry = _HwMirroringGroupMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 28, 1)
)
hwMirroringGroupMonitorEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupMonitorEntry.setStatus("current")
_HwMirroringGroupMonitorIfIndex_Type = Integer32
_HwMirroringGroupMonitorIfIndex_Object = MibTableColumn
hwMirroringGroupMonitorIfIndex = _HwMirroringGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 28, 1, 1),
    _HwMirroringGroupMonitorIfIndex_Type()
)
hwMirroringGroupMonitorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMonitorIfIndex.setStatus("current")
_HwMirroringGroupMonitorRowStatus_Type = RowStatus
_HwMirroringGroupMonitorRowStatus_Object = MibTableColumn
hwMirroringGroupMonitorRowStatus = _HwMirroringGroupMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 28, 1, 2),
    _HwMirroringGroupMonitorRowStatus_Type()
)
hwMirroringGroupMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMonitorRowStatus.setStatus("current")
_HwMirroringGroupMonitorType_Type = HwMirrorOrMonitorType
_HwMirroringGroupMonitorType_Object = MibTableColumn
hwMirroringGroupMonitorType = _HwMirroringGroupMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 28, 1, 3),
    _HwMirroringGroupMonitorType_Type()
)
hwMirroringGroupMonitorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMonitorType.setStatus("current")
_HwMirroringGroupReflectorTable_Object = MibTable
hwMirroringGroupReflectorTable = _HwMirroringGroupReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 29)
)
if mibBuilder.loadTexts:
    hwMirroringGroupReflectorTable.setStatus("current")
_HwMirroringGroupReflectorEntry_Object = MibTableRow
hwMirroringGroupReflectorEntry = _HwMirroringGroupReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 29, 1)
)
hwMirroringGroupReflectorEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupReflectorEntry.setStatus("current")
_HwMirroringGroupReflectorIfIndex_Type = Integer32
_HwMirroringGroupReflectorIfIndex_Object = MibTableColumn
hwMirroringGroupReflectorIfIndex = _HwMirroringGroupReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 29, 1, 1),
    _HwMirroringGroupReflectorIfIndex_Type()
)
hwMirroringGroupReflectorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupReflectorIfIndex.setStatus("current")
_HwMirroringGroupReflectorRowStatus_Type = RowStatus
_HwMirroringGroupReflectorRowStatus_Object = MibTableColumn
hwMirroringGroupReflectorRowStatus = _HwMirroringGroupReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 29, 1, 2),
    _HwMirroringGroupReflectorRowStatus_Type()
)
hwMirroringGroupReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupReflectorRowStatus.setStatus("current")
_HwMirroringGroupRprobeVlanTable_Object = MibTable
hwMirroringGroupRprobeVlanTable = _HwMirroringGroupRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 30)
)
if mibBuilder.loadTexts:
    hwMirroringGroupRprobeVlanTable.setStatus("current")
_HwMirroringGroupRprobeVlanEntry_Object = MibTableRow
hwMirroringGroupRprobeVlanEntry = _HwMirroringGroupRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 30, 1)
)
hwMirroringGroupRprobeVlanEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupRprobeVlanEntry.setStatus("current")


class _HwMirroringGroupRprobeVlanID_Type(Integer32):
    """Custom type hwMirroringGroupRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMirroringGroupRprobeVlanID_Type.__name__ = "Integer32"
_HwMirroringGroupRprobeVlanID_Object = MibTableColumn
hwMirroringGroupRprobeVlanID = _HwMirroringGroupRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 30, 1, 1),
    _HwMirroringGroupRprobeVlanID_Type()
)
hwMirroringGroupRprobeVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupRprobeVlanID.setStatus("current")
_HwMirroringGroupRprobeVlanRowStatus_Type = RowStatus
_HwMirroringGroupRprobeVlanRowStatus_Object = MibTableColumn
hwMirroringGroupRprobeVlanRowStatus = _HwMirroringGroupRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 30, 1, 2),
    _HwMirroringGroupRprobeVlanRowStatus_Type()
)
hwMirroringGroupRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupRprobeVlanRowStatus.setStatus("current")
_HwMirroringGroupMirrorMacTable_Object = MibTable
hwMirroringGroupMirrorMacTable = _HwMirroringGroupMirrorMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31)
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorMacTable.setStatus("current")
_HwMirroringGroupMirrorMacEntry_Object = MibTableRow
hwMirroringGroupMirrorMacEntry = _HwMirroringGroupMirrorMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31, 1)
)
hwMirroringGroupMirrorMacEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupMirrorMacSeq"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorMacEntry.setStatus("current")
_HwMirroringGroupMirrorMacSeq_Type = Integer32
_HwMirroringGroupMirrorMacSeq_Object = MibTableColumn
hwMirroringGroupMirrorMacSeq = _HwMirroringGroupMirrorMacSeq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31, 1, 1),
    _HwMirroringGroupMirrorMacSeq_Type()
)
hwMirroringGroupMirrorMacSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorMacSeq.setStatus("current")
_HwMirroringGroupMirrorMac_Type = MacAddress
_HwMirroringGroupMirrorMac_Object = MibTableColumn
hwMirroringGroupMirrorMac = _HwMirroringGroupMirrorMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31, 1, 2),
    _HwMirroringGroupMirrorMac_Type()
)
hwMirroringGroupMirrorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorMac.setStatus("current")


class _HwMirrorMacVlanID_Type(Integer32):
    """Custom type hwMirrorMacVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMirrorMacVlanID_Type.__name__ = "Integer32"
_HwMirrorMacVlanID_Object = MibTableColumn
hwMirrorMacVlanID = _HwMirrorMacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31, 1, 3),
    _HwMirrorMacVlanID_Type()
)
hwMirrorMacVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirrorMacVlanID.setStatus("current")
_HwMirroringGroupMirroMacStatus_Type = RowStatus
_HwMirroringGroupMirroMacStatus_Object = MibTableColumn
hwMirroringGroupMirroMacStatus = _HwMirroringGroupMirroMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 31, 1, 4),
    _HwMirroringGroupMirroMacStatus_Type()
)
hwMirroringGroupMirroMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirroMacStatus.setStatus("current")
_HwMirroringGroupMirrorVlanTable_Object = MibTable
hwMirroringGroupMirrorVlanTable = _HwMirroringGroupMirrorVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32)
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorVlanTable.setStatus("current")
_HwMirroringGroupMirrorVlanEntry_Object = MibTableRow
hwMirroringGroupMirrorVlanEntry = _HwMirroringGroupMirrorVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32, 1)
)
hwMirroringGroupMirrorVlanEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupID"),
    (0, "HUAWEI-LswQos-MIB", "hwMirroringGroupMirrorVlanSeq"),
)
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorVlanEntry.setStatus("current")
_HwMirroringGroupMirrorVlanSeq_Type = Integer32
_HwMirroringGroupMirrorVlanSeq_Object = MibTableColumn
hwMirroringGroupMirrorVlanSeq = _HwMirroringGroupMirrorVlanSeq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32, 1, 1),
    _HwMirroringGroupMirrorVlanSeq_Type()
)
hwMirroringGroupMirrorVlanSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorVlanSeq.setStatus("current")


class _HwMirroringGroupMirrorVlanID_Type(Integer32):
    """Custom type hwMirroringGroupMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMirroringGroupMirrorVlanID_Type.__name__ = "Integer32"
_HwMirroringGroupMirrorVlanID_Object = MibTableColumn
hwMirroringGroupMirrorVlanID = _HwMirroringGroupMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32, 1, 2),
    _HwMirroringGroupMirrorVlanID_Type()
)
hwMirroringGroupMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorVlanID.setStatus("current")


class _HwMirroringGroupMirrorVlanDirection_Type(Integer32):
    """Custom type hwMirroringGroupMirrorVlanDirection based on Integer32"""
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
          ("inbound", 1),
          ("outbound", 2))
    )


_HwMirroringGroupMirrorVlanDirection_Type.__name__ = "Integer32"
_HwMirroringGroupMirrorVlanDirection_Object = MibTableColumn
hwMirroringGroupMirrorVlanDirection = _HwMirroringGroupMirrorVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32, 1, 3),
    _HwMirroringGroupMirrorVlanDirection_Type()
)
hwMirroringGroupMirrorVlanDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirrorVlanDirection.setStatus("current")
_HwMirroringGroupMirroVlanStatus_Type = RowStatus
_HwMirroringGroupMirroVlanStatus_Object = MibTableColumn
hwMirroringGroupMirroVlanStatus = _HwMirroringGroupMirroVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 32, 1, 4),
    _HwMirroringGroupMirroVlanStatus_Type()
)
hwMirroringGroupMirroVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMirroringGroupMirroVlanStatus.setStatus("current")
_HwPortTrustTable_Object = MibTable
hwPortTrustTable = _HwPortTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33)
)
if mibBuilder.loadTexts:
    hwPortTrustTable.setStatus("current")
_HwPortTrustEntry_Object = MibTableRow
hwPortTrustEntry = _HwPortTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33, 1)
)
hwPortTrustEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwPortTrustIfIndex"),
)
if mibBuilder.loadTexts:
    hwPortTrustEntry.setStatus("current")
_HwPortTrustIfIndex_Type = Integer32
_HwPortTrustIfIndex_Object = MibTableColumn
hwPortTrustIfIndex = _HwPortTrustIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33, 1, 1),
    _HwPortTrustIfIndex_Type()
)
hwPortTrustIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortTrustIfIndex.setStatus("current")


class _HwPortTrustTrustType_Type(Integer32):
    """Custom type hwPortTrustTrustType based on Integer32"""
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
        *(("cos", 2),
          ("dscp", 3),
          ("port", 1))
    )


_HwPortTrustTrustType_Type.__name__ = "Integer32"
_HwPortTrustTrustType_Object = MibTableColumn
hwPortTrustTrustType = _HwPortTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33, 1, 2),
    _HwPortTrustTrustType_Type()
)
hwPortTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortTrustTrustType.setStatus("current")


class _HwPortTrustOvercastType_Type(Integer32):
    """Custom type hwPortTrustOvercastType based on Integer32"""
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
        *(("noOvercast", 1),
          ("overcastCOS", 3),
          ("overcastDSCP", 2))
    )


_HwPortTrustOvercastType_Type.__name__ = "Integer32"
_HwPortTrustOvercastType_Object = MibTableColumn
hwPortTrustOvercastType = _HwPortTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33, 1, 3),
    _HwPortTrustOvercastType_Type()
)
hwPortTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortTrustOvercastType.setStatus("current")


class _HwPortTrustReset_Type(Integer32):
    """Custom type hwPortTrustReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwPortTrustReset_Type.__name__ = "Integer32"
_HwPortTrustReset_Object = MibTableColumn
hwPortTrustReset = _HwPortTrustReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 33, 1, 4),
    _HwPortTrustReset_Type()
)
hwPortTrustReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortTrustReset.setStatus("current")
_HwRemarkVlanIDTable_Object = MibTable
hwRemarkVlanIDTable = _HwRemarkVlanIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34)
)
if mibBuilder.loadTexts:
    hwRemarkVlanIDTable.setStatus("current")
_HwRemarkVlanIDEntry_Object = MibTableRow
hwRemarkVlanIDEntry = _HwRemarkVlanIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1)
)
hwRemarkVlanIDEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwRemarkVlanIDAclIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRemarkVlanIDIfIndex"),
    (0, "HUAWEI-LswQos-MIB", "hwRemarkVlanIDVlanID"),
    (0, "HUAWEI-LswQos-MIB", "hwRemarkVlanIDDirection"),
)
if mibBuilder.loadTexts:
    hwRemarkVlanIDEntry.setStatus("current")


class _HwRemarkVlanIDAclIndex_Type(Integer32):
    """Custom type hwRemarkVlanIDAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HwRemarkVlanIDAclIndex_Type.__name__ = "Integer32"
_HwRemarkVlanIDAclIndex_Object = MibTableColumn
hwRemarkVlanIDAclIndex = _HwRemarkVlanIDAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 1),
    _HwRemarkVlanIDAclIndex_Type()
)
hwRemarkVlanIDAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemarkVlanIDAclIndex.setStatus("current")
_HwRemarkVlanIDIfIndex_Type = Integer32
_HwRemarkVlanIDIfIndex_Object = MibTableColumn
hwRemarkVlanIDIfIndex = _HwRemarkVlanIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 2),
    _HwRemarkVlanIDIfIndex_Type()
)
hwRemarkVlanIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemarkVlanIDIfIndex.setStatus("current")


class _HwRemarkVlanIDVlanID_Type(Integer32):
    """Custom type hwRemarkVlanIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRemarkVlanIDVlanID_Type.__name__ = "Integer32"
_HwRemarkVlanIDVlanID_Object = MibTableColumn
hwRemarkVlanIDVlanID = _HwRemarkVlanIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 3),
    _HwRemarkVlanIDVlanID_Type()
)
hwRemarkVlanIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemarkVlanIDVlanID.setStatus("current")


class _HwRemarkVlanIDDirection_Type(Integer32):
    """Custom type hwRemarkVlanIDDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("invalid", 0),
          ("output", 2))
    )


_HwRemarkVlanIDDirection_Type.__name__ = "Integer32"
_HwRemarkVlanIDDirection_Object = MibTableColumn
hwRemarkVlanIDDirection = _HwRemarkVlanIDDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 4),
    _HwRemarkVlanIDDirection_Type()
)
hwRemarkVlanIDDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRemarkVlanIDDirection.setStatus("current")


class _HwRemarkVlanIDUserAclNum_Type(Integer32):
    """Custom type hwRemarkVlanIDUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRemarkVlanIDUserAclNum_Type.__name__ = "Integer32"
_HwRemarkVlanIDUserAclNum_Object = MibTableColumn
hwRemarkVlanIDUserAclNum = _HwRemarkVlanIDUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 5),
    _HwRemarkVlanIDUserAclNum_Type()
)
hwRemarkVlanIDUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDUserAclNum.setStatus("current")


class _HwRemarkVlanIDUserAclRule_Type(Integer32):
    """Custom type hwRemarkVlanIDUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRemarkVlanIDUserAclRule_Type.__name__ = "Integer32"
_HwRemarkVlanIDUserAclRule_Object = MibTableColumn
hwRemarkVlanIDUserAclRule = _HwRemarkVlanIDUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 6),
    _HwRemarkVlanIDUserAclRule_Type()
)
hwRemarkVlanIDUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDUserAclRule.setStatus("current")


class _HwRemarkVlanIDIpAclNum_Type(Integer32):
    """Custom type hwRemarkVlanIDIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRemarkVlanIDIpAclNum_Type.__name__ = "Integer32"
_HwRemarkVlanIDIpAclNum_Object = MibTableColumn
hwRemarkVlanIDIpAclNum = _HwRemarkVlanIDIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 7),
    _HwRemarkVlanIDIpAclNum_Type()
)
hwRemarkVlanIDIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDIpAclNum.setStatus("current")


class _HwRemarkVlanIDIpAclRule_Type(Integer32):
    """Custom type hwRemarkVlanIDIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRemarkVlanIDIpAclRule_Type.__name__ = "Integer32"
_HwRemarkVlanIDIpAclRule_Object = MibTableColumn
hwRemarkVlanIDIpAclRule = _HwRemarkVlanIDIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 8),
    _HwRemarkVlanIDIpAclRule_Type()
)
hwRemarkVlanIDIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDIpAclRule.setStatus("current")


class _HwRemarkVlanIDLinkAclNum_Type(Integer32):
    """Custom type hwRemarkVlanIDLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HwRemarkVlanIDLinkAclNum_Type.__name__ = "Integer32"
_HwRemarkVlanIDLinkAclNum_Object = MibTableColumn
hwRemarkVlanIDLinkAclNum = _HwRemarkVlanIDLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 9),
    _HwRemarkVlanIDLinkAclNum_Type()
)
hwRemarkVlanIDLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDLinkAclNum.setStatus("current")


class _HwRemarkVlanIDLinkAclRule_Type(Integer32):
    """Custom type hwRemarkVlanIDLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwRemarkVlanIDLinkAclRule_Type.__name__ = "Integer32"
_HwRemarkVlanIDLinkAclRule_Object = MibTableColumn
hwRemarkVlanIDLinkAclRule = _HwRemarkVlanIDLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 10),
    _HwRemarkVlanIDLinkAclRule_Type()
)
hwRemarkVlanIDLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDLinkAclRule.setStatus("current")


class _HwRemarkVlanIDRemarkVlanID_Type(Integer32):
    """Custom type hwRemarkVlanIDRemarkVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwRemarkVlanIDRemarkVlanID_Type.__name__ = "Integer32"
_HwRemarkVlanIDRemarkVlanID_Object = MibTableColumn
hwRemarkVlanIDRemarkVlanID = _HwRemarkVlanIDRemarkVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 11),
    _HwRemarkVlanIDRemarkVlanID_Type()
)
hwRemarkVlanIDRemarkVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDRemarkVlanID.setStatus("current")


class _HwRemarkVlanIDPacketType_Type(Integer32):
    """Custom type hwRemarkVlanIDPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("tagged", 2),
          ("untagged", 3))
    )


_HwRemarkVlanIDPacketType_Type.__name__ = "Integer32"
_HwRemarkVlanIDPacketType_Object = MibTableColumn
hwRemarkVlanIDPacketType = _HwRemarkVlanIDPacketType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 12),
    _HwRemarkVlanIDPacketType_Type()
)
hwRemarkVlanIDPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDPacketType.setStatus("current")
_HwRemarkVlanIDRowStatus_Type = RowStatus
_HwRemarkVlanIDRowStatus_Object = MibTableColumn
hwRemarkVlanIDRowStatus = _HwRemarkVlanIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 34, 1, 13),
    _HwRemarkVlanIDRowStatus_Type()
)
hwRemarkVlanIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwRemarkVlanIDRowStatus.setStatus("current")
_HwCosToDscpMapTable_Object = MibTable
hwCosToDscpMapTable = _HwCosToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 35)
)
if mibBuilder.loadTexts:
    hwCosToDscpMapTable.setStatus("current")
_HwCosToDscpMapEntry_Object = MibTableRow
hwCosToDscpMapEntry = _HwCosToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 35, 1)
)
hwCosToDscpMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwCosToDscpMapCosIndex"),
)
if mibBuilder.loadTexts:
    hwCosToDscpMapEntry.setStatus("current")


class _HwCosToDscpMapCosIndex_Type(Integer32):
    """Custom type hwCosToDscpMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwCosToDscpMapCosIndex_Type.__name__ = "Integer32"
_HwCosToDscpMapCosIndex_Object = MibTableColumn
hwCosToDscpMapCosIndex = _HwCosToDscpMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 35, 1, 1),
    _HwCosToDscpMapCosIndex_Type()
)
hwCosToDscpMapCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCosToDscpMapCosIndex.setStatus("current")


class _HwCosToDscpMapDscpValue_Type(Integer32):
    """Custom type hwCosToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwCosToDscpMapDscpValue_Type.__name__ = "Integer32"
_HwCosToDscpMapDscpValue_Object = MibTableColumn
hwCosToDscpMapDscpValue = _HwCosToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 35, 1, 2),
    _HwCosToDscpMapDscpValue_Type()
)
hwCosToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCosToDscpMapDscpValue.setStatus("current")


class _HwCosToDscpMapReSet_Type(Integer32):
    """Custom type hwCosToDscpMapReSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwCosToDscpMapReSet_Type.__name__ = "Integer32"
_HwCosToDscpMapReSet_Object = MibTableColumn
hwCosToDscpMapReSet = _HwCosToDscpMapReSet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 35, 1, 3),
    _HwCosToDscpMapReSet_Type()
)
hwCosToDscpMapReSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCosToDscpMapReSet.setStatus("current")
_HwDscpToLocalPreMapTable_Object = MibTable
hwDscpToLocalPreMapTable = _HwDscpToLocalPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 36)
)
if mibBuilder.loadTexts:
    hwDscpToLocalPreMapTable.setStatus("current")
_HwDscpToLocalPreMapEntry_Object = MibTableRow
hwDscpToLocalPreMapEntry = _HwDscpToLocalPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 36, 1)
)
hwDscpToLocalPreMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDscpToLocalPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hwDscpToLocalPreMapEntry.setStatus("current")


class _HwDscpToLocalPreMapDscpIndex_Type(Integer32):
    """Custom type hwDscpToLocalPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpToLocalPreMapDscpIndex_Type.__name__ = "Integer32"
_HwDscpToLocalPreMapDscpIndex_Object = MibTableColumn
hwDscpToLocalPreMapDscpIndex = _HwDscpToLocalPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 36, 1, 1),
    _HwDscpToLocalPreMapDscpIndex_Type()
)
hwDscpToLocalPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDscpToLocalPreMapDscpIndex.setStatus("current")


class _HwDscpToLocalPreMapLocalPreVal_Type(Integer32):
    """Custom type hwDscpToLocalPreMapLocalPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDscpToLocalPreMapLocalPreVal_Type.__name__ = "Integer32"
_HwDscpToLocalPreMapLocalPreVal_Object = MibTableColumn
hwDscpToLocalPreMapLocalPreVal = _HwDscpToLocalPreMapLocalPreVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 36, 1, 2),
    _HwDscpToLocalPreMapLocalPreVal_Type()
)
hwDscpToLocalPreMapLocalPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToLocalPreMapLocalPreVal.setStatus("current")


class _HwDscpToLocalPreMapReset_Type(Integer32):
    """Custom type hwDscpToLocalPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDscpToLocalPreMapReset_Type.__name__ = "Integer32"
_HwDscpToLocalPreMapReset_Object = MibTableColumn
hwDscpToLocalPreMapReset = _HwDscpToLocalPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 36, 1, 3),
    _HwDscpToLocalPreMapReset_Type()
)
hwDscpToLocalPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToLocalPreMapReset.setStatus("current")
_HwDscpToDropPreMapTable_Object = MibTable
hwDscpToDropPreMapTable = _HwDscpToDropPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 37)
)
if mibBuilder.loadTexts:
    hwDscpToDropPreMapTable.setStatus("current")
_HwDscpToDropPreMapEntry_Object = MibTableRow
hwDscpToDropPreMapEntry = _HwDscpToDropPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 37, 1)
)
hwDscpToDropPreMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDscpToDropPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hwDscpToDropPreMapEntry.setStatus("current")


class _HwDscpToDropPreMapDscpIndex_Type(Integer32):
    """Custom type hwDscpToDropPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpToDropPreMapDscpIndex_Type.__name__ = "Integer32"
_HwDscpToDropPreMapDscpIndex_Object = MibTableColumn
hwDscpToDropPreMapDscpIndex = _HwDscpToDropPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 37, 1, 1),
    _HwDscpToDropPreMapDscpIndex_Type()
)
hwDscpToDropPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDscpToDropPreMapDscpIndex.setStatus("current")


class _HwDscpToDropPreMapDropPreVal_Type(Integer32):
    """Custom type hwDscpToDropPreMapDropPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwDscpToDropPreMapDropPreVal_Type.__name__ = "Integer32"
_HwDscpToDropPreMapDropPreVal_Object = MibTableColumn
hwDscpToDropPreMapDropPreVal = _HwDscpToDropPreMapDropPreVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 37, 1, 2),
    _HwDscpToDropPreMapDropPreVal_Type()
)
hwDscpToDropPreMapDropPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToDropPreMapDropPreVal.setStatus("current")


class _HwDscpToDropPreMapReset_Type(Integer32):
    """Custom type hwDscpToDropPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDscpToDropPreMapReset_Type.__name__ = "Integer32"
_HwDscpToDropPreMapReset_Object = MibTableColumn
hwDscpToDropPreMapReset = _HwDscpToDropPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 37, 1, 3),
    _HwDscpToDropPreMapReset_Type()
)
hwDscpToDropPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToDropPreMapReset.setStatus("current")
_HwDscpToCosMapTable_Object = MibTable
hwDscpToCosMapTable = _HwDscpToCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 38)
)
if mibBuilder.loadTexts:
    hwDscpToCosMapTable.setStatus("current")
_HwDscpToCosMapEntry_Object = MibTableRow
hwDscpToCosMapEntry = _HwDscpToCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 38, 1)
)
hwDscpToCosMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDscpToCosMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hwDscpToCosMapEntry.setStatus("current")


class _HwDscpToCosMapDscpIndex_Type(Integer32):
    """Custom type hwDscpToCosMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpToCosMapDscpIndex_Type.__name__ = "Integer32"
_HwDscpToCosMapDscpIndex_Object = MibTableColumn
hwDscpToCosMapDscpIndex = _HwDscpToCosMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 38, 1, 1),
    _HwDscpToCosMapDscpIndex_Type()
)
hwDscpToCosMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDscpToCosMapDscpIndex.setStatus("current")


class _HwDscpToCosMapCosValue_Type(Integer32):
    """Custom type hwDscpToCosMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDscpToCosMapCosValue_Type.__name__ = "Integer32"
_HwDscpToCosMapCosValue_Object = MibTableColumn
hwDscpToCosMapCosValue = _HwDscpToCosMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 38, 1, 2),
    _HwDscpToCosMapCosValue_Type()
)
hwDscpToCosMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToCosMapCosValue.setStatus("current")


class _HwDscpToCosMapReset_Type(Integer32):
    """Custom type hwDscpToCosMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDscpToCosMapReset_Type.__name__ = "Integer32"
_HwDscpToCosMapReset_Object = MibTableColumn
hwDscpToCosMapReset = _HwDscpToCosMapReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 38, 1, 3),
    _HwDscpToCosMapReset_Type()
)
hwDscpToCosMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToCosMapReset.setStatus("current")
_HwDscpToDscpMapTable_Object = MibTable
hwDscpToDscpMapTable = _HwDscpToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 39)
)
if mibBuilder.loadTexts:
    hwDscpToDscpMapTable.setStatus("current")
_HwDscpToDscpMapEntry_Object = MibTableRow
hwDscpToDscpMapEntry = _HwDscpToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 39, 1)
)
hwDscpToDscpMapEntry.setIndexNames(
    (0, "HUAWEI-LswQos-MIB", "hwDscpToDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hwDscpToDscpMapEntry.setStatus("current")


class _HwDscpToDscpMapDscpIndex_Type(Integer32):
    """Custom type hwDscpToDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpToDscpMapDscpIndex_Type.__name__ = "Integer32"
_HwDscpToDscpMapDscpIndex_Object = MibTableColumn
hwDscpToDscpMapDscpIndex = _HwDscpToDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 39, 1, 1),
    _HwDscpToDscpMapDscpIndex_Type()
)
hwDscpToDscpMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDscpToDscpMapDscpIndex.setStatus("current")


class _HwDscpToDscpMapDscpValue_Type(Integer32):
    """Custom type hwDscpToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HwDscpToDscpMapDscpValue_Type.__name__ = "Integer32"
_HwDscpToDscpMapDscpValue_Object = MibTableColumn
hwDscpToDscpMapDscpValue = _HwDscpToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 39, 1, 2),
    _HwDscpToDscpMapDscpValue_Type()
)
hwDscpToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToDscpMapDscpValue.setStatus("current")


class _HwDscpToDscpMapReset_Type(Integer32):
    """Custom type hwDscpToDscpMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwDscpToDscpMapReset_Type.__name__ = "Integer32"
_HwDscpToDscpMapReset_Object = MibTableColumn
hwDscpToDscpMapReset = _HwDscpToDscpMapReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 16, 2, 39, 1, 3),
    _HwDscpToDscpMapReset_Type()
)
hwDscpToDscpMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDscpToDscpMapReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LswQos-MIB",
    **{"HwMirrorOrMonitorType": HwMirrorOrMonitorType,
       "hwLswQosAclMib": hwLswQosAclMib,
       "hwLswQosMibObject": hwLswQosMibObject,
       "hwPriorityTrustMode": hwPriorityTrustMode,
       "hwPortMonitorBothIfIndex": hwPortMonitorBothIfIndex,
       "hwQueueTable": hwQueueTable,
       "hwQueueEntry": hwQueueEntry,
       "hwQueueIfIndex": hwQueueIfIndex,
       "hwQueueScheduleMode": hwQueueScheduleMode,
       "hwQueueWeight1": hwQueueWeight1,
       "hwQueueWeight2": hwQueueWeight2,
       "hwQueueWeight3": hwQueueWeight3,
       "hwQueueWeight4": hwQueueWeight4,
       "hwQueueMaxDelay": hwQueueMaxDelay,
       "hwQueueWeight5": hwQueueWeight5,
       "hwQueueWeight6": hwQueueWeight6,
       "hwQueueWeight7": hwQueueWeight7,
       "hwQueueWeight8": hwQueueWeight8,
       "hwRateLimitTable": hwRateLimitTable,
       "hwRateLimitEntry": hwRateLimitEntry,
       "hwRateLimitAclIndex": hwRateLimitAclIndex,
       "hwRateLimitIfIndex": hwRateLimitIfIndex,
       "hwRateLimitVlanID": hwRateLimitVlanID,
       "hwRateLimitDirection": hwRateLimitDirection,
       "hwRateLimitUserAclNum": hwRateLimitUserAclNum,
       "hwRateLimitUserAclRule": hwRateLimitUserAclRule,
       "hwRateLimitIpAclNum": hwRateLimitIpAclNum,
       "hwRateLimitIpAclRule": hwRateLimitIpAclRule,
       "hwRateLimitLinkAclNum": hwRateLimitLinkAclNum,
       "hwRateLimitLinkAclRule": hwRateLimitLinkAclRule,
       "hwRateLimitTargetRateMbps": hwRateLimitTargetRateMbps,
       "hwRateLimitTargetRateKbps": hwRateLimitTargetRateKbps,
       "hwRateLimitPeakRate": hwRateLimitPeakRate,
       "hwRateLimitCIR": hwRateLimitCIR,
       "hwRateLimitCBS": hwRateLimitCBS,
       "hwRateLimitEBS": hwRateLimitEBS,
       "hwRateLimitPIR": hwRateLimitPIR,
       "hwRateLimitConformLocalPre": hwRateLimitConformLocalPre,
       "hwRateLimitConformActionType": hwRateLimitConformActionType,
       "hwRateLimitExceedActionType": hwRateLimitExceedActionType,
       "hwRateLimitExceedDscp": hwRateLimitExceedDscp,
       "hwRateLimitRuntime": hwRateLimitRuntime,
       "hwRateLimitRowStatus": hwRateLimitRowStatus,
       "hwRateLimitExceedCos": hwRateLimitExceedCos,
       "hwRateLimitConformCos": hwRateLimitConformCos,
       "hwRateLimitConformDscp": hwRateLimitConformDscp,
       "hwRateLimitMeterStatByteCount": hwRateLimitMeterStatByteCount,
       "hwRateLimitMeterStatByteXCount": hwRateLimitMeterStatByteXCount,
       "hwRateLimitMeterStatState": hwRateLimitMeterStatState,
       "hwPriorityTable": hwPriorityTable,
       "hwPriorityEntry": hwPriorityEntry,
       "hwPriorityAclIndex": hwPriorityAclIndex,
       "hwPriorityIfIndex": hwPriorityIfIndex,
       "hwPriorityVlanID": hwPriorityVlanID,
       "hwPriorityDirection": hwPriorityDirection,
       "hwPriorityUserAclNum": hwPriorityUserAclNum,
       "hwPriorityUserAclRule": hwPriorityUserAclRule,
       "hwPriorityIpAclNum": hwPriorityIpAclNum,
       "hwPriorityIpAclRule": hwPriorityIpAclRule,
       "hwPriorityLinkAclNum": hwPriorityLinkAclNum,
       "hwPriorityLinkAclRule": hwPriorityLinkAclRule,
       "hwPriorityDscp": hwPriorityDscp,
       "hwPriorityIpPre": hwPriorityIpPre,
       "hwPriorityIpPreFromCos": hwPriorityIpPreFromCos,
       "hwPriorityCos": hwPriorityCos,
       "hwPriorityCosFromIpPre": hwPriorityCosFromIpPre,
       "hwPriorityLocalPre": hwPriorityLocalPre,
       "hwPriorityPolicedServiceType": hwPriorityPolicedServiceType,
       "hwPriorityPolicedServiceDscp": hwPriorityPolicedServiceDscp,
       "hwPriorityPolicedServiceExp": hwPriorityPolicedServiceExp,
       "hwPriorityPolicedServiceCos": hwPriorityPolicedServiceCos,
       "hwPriorityPolicedServiceLoaclPre": hwPriorityPolicedServiceLoaclPre,
       "hwPriorityPolicedServiceDropPriority": hwPriorityPolicedServiceDropPriority,
       "hwPriorityRuntime": hwPriorityRuntime,
       "hwPriorityRowStatus": hwPriorityRowStatus,
       "hwRedirectTable": hwRedirectTable,
       "hwRedirectEntry": hwRedirectEntry,
       "hwRedirectAclIndex": hwRedirectAclIndex,
       "hwRedirectIfIndex": hwRedirectIfIndex,
       "hwRedirectVlanID": hwRedirectVlanID,
       "hwRedirectDirection": hwRedirectDirection,
       "hwRedirectUserAclNum": hwRedirectUserAclNum,
       "hwRedirectUserAclRule": hwRedirectUserAclRule,
       "hwRedirectIpAclNum": hwRedirectIpAclNum,
       "hwRedirectIpAclRule": hwRedirectIpAclRule,
       "hwRedirectLinkAclNum": hwRedirectLinkAclNum,
       "hwRedirectLinkAclRule": hwRedirectLinkAclRule,
       "hwRedirectToCpu": hwRedirectToCpu,
       "hwRedirectToIfIndex": hwRedirectToIfIndex,
       "hwRedirectToNextHop1": hwRedirectToNextHop1,
       "hwRedirectToNextHop2": hwRedirectToNextHop2,
       "hwRedirectRuntime": hwRedirectRuntime,
       "hwRedirectRowStatus": hwRedirectRowStatus,
       "hwRedirectToSlotNo": hwRedirectToSlotNo,
       "hwRedirectRemarkedDSCP": hwRedirectRemarkedDSCP,
       "hwRedirectRemarkedPri": hwRedirectRemarkedPri,
       "hwRedirectRemarkedTos": hwRedirectRemarkedTos,
       "hwRedirectToNextHop3": hwRedirectToNextHop3,
       "hwRedirectTargetVlanID": hwRedirectTargetVlanID,
       "hwRedirectMode": hwRedirectMode,
       "hwRedirectToNestedVlanID": hwRedirectToNestedVlanID,
       "hwRedirectToModifiedVlanID": hwRedirectToModifiedVlanID,
       "hwStatisticTable": hwStatisticTable,
       "hwStatisticEntry": hwStatisticEntry,
       "hwStatisticAclIndex": hwStatisticAclIndex,
       "hwStatisticIfIndex": hwStatisticIfIndex,
       "hwStatisticVlanID": hwStatisticVlanID,
       "hwStatisticDirection": hwStatisticDirection,
       "hwStatisticUserAclNum": hwStatisticUserAclNum,
       "hwStatisticUserAclRule": hwStatisticUserAclRule,
       "hwStatisticIpAclNum": hwStatisticIpAclNum,
       "hwStatisticIpAclRule": hwStatisticIpAclRule,
       "hwStatisticLinkAclNum": hwStatisticLinkAclNum,
       "hwStatisticLinkAclRule": hwStatisticLinkAclRule,
       "hwStatisticRuntime": hwStatisticRuntime,
       "hwStatisticPacketCount": hwStatisticPacketCount,
       "hwStatisticByteCount": hwStatisticByteCount,
       "hwStatisticCountClear": hwStatisticCountClear,
       "hwStatisticRowStatus": hwStatisticRowStatus,
       "hwStatisticPacketXCount": hwStatisticPacketXCount,
       "hwStatisticByteXCount": hwStatisticByteXCount,
       "hwMirrorTable": hwMirrorTable,
       "hwMirrorEntry": hwMirrorEntry,
       "hwMirrorAclIndex": hwMirrorAclIndex,
       "hwMirrorIfIndex": hwMirrorIfIndex,
       "hwMirrorVlanID": hwMirrorVlanID,
       "hwMirrorDirection": hwMirrorDirection,
       "hwMirrorUserAclNum": hwMirrorUserAclNum,
       "hwMirrorUserAclRule": hwMirrorUserAclRule,
       "hwMirrorIpAclNum": hwMirrorIpAclNum,
       "hwMirrorIpAclRule": hwMirrorIpAclRule,
       "hwMirrorLinkAclNum": hwMirrorLinkAclNum,
       "hwMirrorLinkAclRule": hwMirrorLinkAclRule,
       "hwMirrorToIfIndex": hwMirrorToIfIndex,
       "hwMirrorToCpu": hwMirrorToCpu,
       "hwMirrorRuntime": hwMirrorRuntime,
       "hwMirrorRowStatus": hwMirrorRowStatus,
       "hwMirrorToGroup": hwMirrorToGroup,
       "hwPortMirrorTable": hwPortMirrorTable,
       "hwPortMirrorEntry": hwPortMirrorEntry,
       "hwPortMirrorIfIndex": hwPortMirrorIfIndex,
       "hwPortMirrorDirection": hwPortMirrorDirection,
       "hwPortMirrorRowStatus": hwPortMirrorRowStatus,
       "hwLineRateTable": hwLineRateTable,
       "hwLineRateEntry": hwLineRateEntry,
       "hwLineRateIfIndex": hwLineRateIfIndex,
       "hwLineRateDirection": hwLineRateDirection,
       "hwLineRateValue": hwLineRateValue,
       "hwLineRateRowStatus": hwLineRateRowStatus,
       "hwBandwidthTable": hwBandwidthTable,
       "hwBandwidthEntry": hwBandwidthEntry,
       "hwBandwidthAclIndex": hwBandwidthAclIndex,
       "hwBandwidthIfIndex": hwBandwidthIfIndex,
       "hwBandwidthVlanID": hwBandwidthVlanID,
       "hwBandwidthDirection": hwBandwidthDirection,
       "hwBandwidthIpAclNum": hwBandwidthIpAclNum,
       "hwBandwidthIpAclRule": hwBandwidthIpAclRule,
       "hwBandwidthLinkAclNum": hwBandwidthLinkAclNum,
       "hwBandwidthLinkAclRule": hwBandwidthLinkAclRule,
       "hwBandwidthMinGuaranteedWidth": hwBandwidthMinGuaranteedWidth,
       "hwBandwidthMaxGuaranteedWidth": hwBandwidthMaxGuaranteedWidth,
       "hwBandwidthWeight": hwBandwidthWeight,
       "hwBandwidthRuntime": hwBandwidthRuntime,
       "hwBandwidthRowStatus": hwBandwidthRowStatus,
       "hwRedTable": hwRedTable,
       "hwRedEntry": hwRedEntry,
       "hwRedAclIndex": hwRedAclIndex,
       "hwRedIfIndex": hwRedIfIndex,
       "hwRedVlanID": hwRedVlanID,
       "hwRedDirection": hwRedDirection,
       "hwRedIpAclNum": hwRedIpAclNum,
       "hwRedIpAclRule": hwRedIpAclRule,
       "hwRedLinkAclNum": hwRedLinkAclNum,
       "hwRedLinkAclRule": hwRedLinkAclRule,
       "hwRedStartQueueLen": hwRedStartQueueLen,
       "hwRedStopQueueLen": hwRedStopQueueLen,
       "hwRedProbability": hwRedProbability,
       "hwRedRuntime": hwRedRuntime,
       "hwRedRowStatus": hwRedRowStatus,
       "hwMirrorGroupTable": hwMirrorGroupTable,
       "hwMirrorGroupEntry": hwMirrorGroupEntry,
       "hwMirrorGroupID": hwMirrorGroupID,
       "hwMirrorGroupDirection": hwMirrorGroupDirection,
       "hwMirrorGroupMirrorIfIndexList": hwMirrorGroupMirrorIfIndexList,
       "hwMirrorGroupMonitorIfIndex": hwMirrorGroupMonitorIfIndex,
       "hwMirrorGroupRowStatus": hwMirrorGroupRowStatus,
       "hwFlowtempTable": hwFlowtempTable,
       "hwFlowtempEntry": hwFlowtempEntry,
       "hwFlowtempIndex": hwFlowtempIndex,
       "hwFlowtempIpProtocol": hwFlowtempIpProtocol,
       "hwFlowtempTcpFlag": hwFlowtempTcpFlag,
       "hwFlowtempSPort": hwFlowtempSPort,
       "hwFlowtempDPort": hwFlowtempDPort,
       "hwFlowtempIcmpType": hwFlowtempIcmpType,
       "hwFlowtempIcmpCode": hwFlowtempIcmpCode,
       "hwFlowtempFragment": hwFlowtempFragment,
       "hwFlowtempDscp": hwFlowtempDscp,
       "hwFlowtempIpPre": hwFlowtempIpPre,
       "hwFlowtempTos": hwFlowtempTos,
       "hwFlowtempSIp": hwFlowtempSIp,
       "hwFlowtempSIpMask": hwFlowtempSIpMask,
       "hwFlowtempDIp": hwFlowtempDIp,
       "hwFlowtempDIpMask": hwFlowtempDIpMask,
       "hwFlowtempEthProtocol": hwFlowtempEthProtocol,
       "hwFlowtempSMac": hwFlowtempSMac,
       "hwFlowtempSMacMask": hwFlowtempSMacMask,
       "hwFlowtempDMac": hwFlowtempDMac,
       "hwFlowtempDMacMask": hwFlowtempDMacMask,
       "hwFlowtempVpn": hwFlowtempVpn,
       "hwFlowtempRowStatus": hwFlowtempRowStatus,
       "hwFlowtempVlanId": hwFlowtempVlanId,
       "hwFlowtempCos": hwFlowtempCos,
       "hwFlowtempEnableTable": hwFlowtempEnableTable,
       "hwFlowtempEnableEntry": hwFlowtempEnableEntry,
       "hwFlowtempEnableIfIndex": hwFlowtempEnableIfIndex,
       "hwFlowtempEnableVlanID": hwFlowtempEnableVlanID,
       "hwFlowtempEnableFlowtempIndex": hwFlowtempEnableFlowtempIndex,
       "hwTrafficShapeTable": hwTrafficShapeTable,
       "hwTrafficShapeEntry": hwTrafficShapeEntry,
       "hwTrafficShapeIfIndex": hwTrafficShapeIfIndex,
       "hwTrafficShapeQueueId": hwTrafficShapeQueueId,
       "hwTrafficShapeMaxRate": hwTrafficShapeMaxRate,
       "hwTrafficShapeBurstSize": hwTrafficShapeBurstSize,
       "hwTrafficShapeBufferLimit": hwTrafficShapeBufferLimit,
       "hwTrafficShapeRowStatus": hwTrafficShapeRowStatus,
       "hwPortQueueTable": hwPortQueueTable,
       "hwPortQueueEntry": hwPortQueueEntry,
       "hwPortQueueIfIndex": hwPortQueueIfIndex,
       "hwPortQueueQueueID": hwPortQueueQueueID,
       "hwPortQueueWrrPriority": hwPortQueueWrrPriority,
       "hwPortQueueWeight": hwPortQueueWeight,
       "hwDropModeTable": hwDropModeTable,
       "hwDropModeEntry": hwDropModeEntry,
       "hwDropModeIfIndex": hwDropModeIfIndex,
       "hwDropModeMode": hwDropModeMode,
       "hwDropModeWredIndex": hwDropModeWredIndex,
       "hwWredTable": hwWredTable,
       "hwWredEntry": hwWredEntry,
       "hwWredIndex": hwWredIndex,
       "hwWredQueueId": hwWredQueueId,
       "hwWredGreenMinThreshold": hwWredGreenMinThreshold,
       "hwWredGreenMaxThreshold": hwWredGreenMaxThreshold,
       "hwWredGreenMaxProb": hwWredGreenMaxProb,
       "hwWredYellowMinThreshold": hwWredYellowMinThreshold,
       "hwWredYellowMaxThreshold": hwWredYellowMaxThreshold,
       "hwWredYellowMaxProb": hwWredYellowMaxProb,
       "hwWredRedMinThreshold": hwWredRedMinThreshold,
       "hwWredRedMaxThreshold": hwWredRedMaxThreshold,
       "hwWredRedMaxProb": hwWredRedMaxProb,
       "hwWredExponent": hwWredExponent,
       "hwCosToLocalPrecedenceMapTable": hwCosToLocalPrecedenceMapTable,
       "hwCosToLocalPrecedenceMapEntry": hwCosToLocalPrecedenceMapEntry,
       "hwCosToLocalPrecedenceMapCosIndex": hwCosToLocalPrecedenceMapCosIndex,
       "hwCosToLocalPrecedenceMapLocalPrecedenceValue": hwCosToLocalPrecedenceMapLocalPrecedenceValue,
       "hwCosToDropPrecedenceMapTable": hwCosToDropPrecedenceMapTable,
       "hwCosToDropPrecedenceMapEntry": hwCosToDropPrecedenceMapEntry,
       "hwCosToDropPrecedenceMapCosIndex": hwCosToDropPrecedenceMapCosIndex,
       "hwCosToDropPrecedenceMapDropPrecedenceValue": hwCosToDropPrecedenceMapDropPrecedenceValue,
       "hwDscpMapTable": hwDscpMapTable,
       "hwDscpMapEntry": hwDscpMapEntry,
       "hwDscpMapConformLevel": hwDscpMapConformLevel,
       "hwDscpMapDscpIndex": hwDscpMapDscpIndex,
       "hwDscpMapDscpValue": hwDscpMapDscpValue,
       "hwDscpMapExpValue": hwDscpMapExpValue,
       "hwDscpMapCosValue": hwDscpMapCosValue,
       "hwDscpMapLocalPrecedence": hwDscpMapLocalPrecedence,
       "hwDscpMapDropPrecedence": hwDscpMapDropPrecedence,
       "hwExpMapTable": hwExpMapTable,
       "hwExpMapEntry": hwExpMapEntry,
       "hwExpMapConformLevel": hwExpMapConformLevel,
       "hwExpMapExpIndex": hwExpMapExpIndex,
       "hwExpMapDscpValue": hwExpMapDscpValue,
       "hwExpMapExpValue": hwExpMapExpValue,
       "hwExpMapCosValue": hwExpMapCosValue,
       "hwExpMapLocalPrecedence": hwExpMapLocalPrecedence,
       "hwExpMapDropPrecedence": hwExpMapDropPrecedence,
       "hwLocalPrecedenceMapTable": hwLocalPrecedenceMapTable,
       "hwLocalPrecedenceMapEntry": hwLocalPrecedenceMapEntry,
       "hwLocalPrecedenceMapConformLevel": hwLocalPrecedenceMapConformLevel,
       "hwLocalPrecedenceMapLocalPrecedenceIndex": hwLocalPrecedenceMapLocalPrecedenceIndex,
       "hwLocalPrecedenceMapCosValue": hwLocalPrecedenceMapCosValue,
       "hwPortWredTable": hwPortWredTable,
       "hwPortWredEntry": hwPortWredEntry,
       "hwPortWredIfIndex": hwPortWredIfIndex,
       "hwPortWredQueueID": hwPortWredQueueID,
       "hwPortWredQueueStartLength": hwPortWredQueueStartLength,
       "hwPortWredQueueProbability": hwPortWredQueueProbability,
       "hwMirroringGroupTable": hwMirroringGroupTable,
       "hwMirroringGroupEntry": hwMirroringGroupEntry,
       "hwMirroringGroupID": hwMirroringGroupID,
       "hwMirroringGroupType": hwMirroringGroupType,
       "hwMirroringGroupStatus": hwMirroringGroupStatus,
       "hwMirroringGroupRowStatus": hwMirroringGroupRowStatus,
       "hwMirroringGroupMirrorTable": hwMirroringGroupMirrorTable,
       "hwMirroringGroupMirrorEntry": hwMirroringGroupMirrorEntry,
       "hwMirroringGroupMirrorInboundIfIndexList": hwMirroringGroupMirrorInboundIfIndexList,
       "hwMirroringGroupMirrorOutboundIfIndexList": hwMirroringGroupMirrorOutboundIfIndexList,
       "hwMirroringGroupMirrorRowStatus": hwMirroringGroupMirrorRowStatus,
       "hwMirroringGroupMirrorInTypeList": hwMirroringGroupMirrorInTypeList,
       "hwMirroringGroupMirrorOutTypeList": hwMirroringGroupMirrorOutTypeList,
       "hwMirroringGroupMonitorTable": hwMirroringGroupMonitorTable,
       "hwMirroringGroupMonitorEntry": hwMirroringGroupMonitorEntry,
       "hwMirroringGroupMonitorIfIndex": hwMirroringGroupMonitorIfIndex,
       "hwMirroringGroupMonitorRowStatus": hwMirroringGroupMonitorRowStatus,
       "hwMirroringGroupMonitorType": hwMirroringGroupMonitorType,
       "hwMirroringGroupReflectorTable": hwMirroringGroupReflectorTable,
       "hwMirroringGroupReflectorEntry": hwMirroringGroupReflectorEntry,
       "hwMirroringGroupReflectorIfIndex": hwMirroringGroupReflectorIfIndex,
       "hwMirroringGroupReflectorRowStatus": hwMirroringGroupReflectorRowStatus,
       "hwMirroringGroupRprobeVlanTable": hwMirroringGroupRprobeVlanTable,
       "hwMirroringGroupRprobeVlanEntry": hwMirroringGroupRprobeVlanEntry,
       "hwMirroringGroupRprobeVlanID": hwMirroringGroupRprobeVlanID,
       "hwMirroringGroupRprobeVlanRowStatus": hwMirroringGroupRprobeVlanRowStatus,
       "hwMirroringGroupMirrorMacTable": hwMirroringGroupMirrorMacTable,
       "hwMirroringGroupMirrorMacEntry": hwMirroringGroupMirrorMacEntry,
       "hwMirroringGroupMirrorMacSeq": hwMirroringGroupMirrorMacSeq,
       "hwMirroringGroupMirrorMac": hwMirroringGroupMirrorMac,
       "hwMirrorMacVlanID": hwMirrorMacVlanID,
       "hwMirroringGroupMirroMacStatus": hwMirroringGroupMirroMacStatus,
       "hwMirroringGroupMirrorVlanTable": hwMirroringGroupMirrorVlanTable,
       "hwMirroringGroupMirrorVlanEntry": hwMirroringGroupMirrorVlanEntry,
       "hwMirroringGroupMirrorVlanSeq": hwMirroringGroupMirrorVlanSeq,
       "hwMirroringGroupMirrorVlanID": hwMirroringGroupMirrorVlanID,
       "hwMirroringGroupMirrorVlanDirection": hwMirroringGroupMirrorVlanDirection,
       "hwMirroringGroupMirroVlanStatus": hwMirroringGroupMirroVlanStatus,
       "hwPortTrustTable": hwPortTrustTable,
       "hwPortTrustEntry": hwPortTrustEntry,
       "hwPortTrustIfIndex": hwPortTrustIfIndex,
       "hwPortTrustTrustType": hwPortTrustTrustType,
       "hwPortTrustOvercastType": hwPortTrustOvercastType,
       "hwPortTrustReset": hwPortTrustReset,
       "hwRemarkVlanIDTable": hwRemarkVlanIDTable,
       "hwRemarkVlanIDEntry": hwRemarkVlanIDEntry,
       "hwRemarkVlanIDAclIndex": hwRemarkVlanIDAclIndex,
       "hwRemarkVlanIDIfIndex": hwRemarkVlanIDIfIndex,
       "hwRemarkVlanIDVlanID": hwRemarkVlanIDVlanID,
       "hwRemarkVlanIDDirection": hwRemarkVlanIDDirection,
       "hwRemarkVlanIDUserAclNum": hwRemarkVlanIDUserAclNum,
       "hwRemarkVlanIDUserAclRule": hwRemarkVlanIDUserAclRule,
       "hwRemarkVlanIDIpAclNum": hwRemarkVlanIDIpAclNum,
       "hwRemarkVlanIDIpAclRule": hwRemarkVlanIDIpAclRule,
       "hwRemarkVlanIDLinkAclNum": hwRemarkVlanIDLinkAclNum,
       "hwRemarkVlanIDLinkAclRule": hwRemarkVlanIDLinkAclRule,
       "hwRemarkVlanIDRemarkVlanID": hwRemarkVlanIDRemarkVlanID,
       "hwRemarkVlanIDPacketType": hwRemarkVlanIDPacketType,
       "hwRemarkVlanIDRowStatus": hwRemarkVlanIDRowStatus,
       "hwCosToDscpMapTable": hwCosToDscpMapTable,
       "hwCosToDscpMapEntry": hwCosToDscpMapEntry,
       "hwCosToDscpMapCosIndex": hwCosToDscpMapCosIndex,
       "hwCosToDscpMapDscpValue": hwCosToDscpMapDscpValue,
       "hwCosToDscpMapReSet": hwCosToDscpMapReSet,
       "hwDscpToLocalPreMapTable": hwDscpToLocalPreMapTable,
       "hwDscpToLocalPreMapEntry": hwDscpToLocalPreMapEntry,
       "hwDscpToLocalPreMapDscpIndex": hwDscpToLocalPreMapDscpIndex,
       "hwDscpToLocalPreMapLocalPreVal": hwDscpToLocalPreMapLocalPreVal,
       "hwDscpToLocalPreMapReset": hwDscpToLocalPreMapReset,
       "hwDscpToDropPreMapTable": hwDscpToDropPreMapTable,
       "hwDscpToDropPreMapEntry": hwDscpToDropPreMapEntry,
       "hwDscpToDropPreMapDscpIndex": hwDscpToDropPreMapDscpIndex,
       "hwDscpToDropPreMapDropPreVal": hwDscpToDropPreMapDropPreVal,
       "hwDscpToDropPreMapReset": hwDscpToDropPreMapReset,
       "hwDscpToCosMapTable": hwDscpToCosMapTable,
       "hwDscpToCosMapEntry": hwDscpToCosMapEntry,
       "hwDscpToCosMapDscpIndex": hwDscpToCosMapDscpIndex,
       "hwDscpToCosMapCosValue": hwDscpToCosMapCosValue,
       "hwDscpToCosMapReset": hwDscpToCosMapReset,
       "hwDscpToDscpMapTable": hwDscpToDscpMapTable,
       "hwDscpToDscpMapEntry": hwDscpToDscpMapEntry,
       "hwDscpToDscpMapDscpIndex": hwDscpToDscpMapDscpIndex,
       "hwDscpToDscpMapDscpValue": hwDscpToDscpMapDscpValue,
       "hwDscpToDscpMapReset": hwDscpToDscpMapReset}
)
