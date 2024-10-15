# SNMP MIB module (HPN-ICF-LswQos-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswQos-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:58 2024
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

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

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

hpnicfLswQosAclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16)
)
hpnicfLswQosAclMib.setRevisions(
        ("2002-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMirrorOrMonitorType(Integer32, TextualConvention):
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

_HpnicfLswQosMibObject_ObjectIdentity = ObjectIdentity
hpnicfLswQosMibObject = _HpnicfLswQosMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2)
)


class _HpnicfPriorityTrustMode_Type(Integer32):
    """Custom type hpnicfPriorityTrustMode based on Integer32"""
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


_HpnicfPriorityTrustMode_Type.__name__ = "Integer32"
_HpnicfPriorityTrustMode_Object = MibScalar
hpnicfPriorityTrustMode = _HpnicfPriorityTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 1),
    _HpnicfPriorityTrustMode_Type()
)
hpnicfPriorityTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPriorityTrustMode.setStatus("current")


class _HpnicfPortMonitorBothIfIndex_Type(Integer32):
    """Custom type hpnicfPortMonitorBothIfIndex based on Integer32"""
    defaultValue = 0


_HpnicfPortMonitorBothIfIndex_Object = MibScalar
hpnicfPortMonitorBothIfIndex = _HpnicfPortMonitorBothIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 2),
    _HpnicfPortMonitorBothIfIndex_Type()
)
hpnicfPortMonitorBothIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortMonitorBothIfIndex.setStatus("current")
_HpnicfQueueTable_Object = MibTable
hpnicfQueueTable = _HpnicfQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfQueueTable.setStatus("current")
_HpnicfQueueEntry_Object = MibTableRow
hpnicfQueueEntry = _HpnicfQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1)
)
hpnicfQueueEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfQueueIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfQueueEntry.setStatus("current")
_HpnicfQueueIfIndex_Type = Integer32
_HpnicfQueueIfIndex_Object = MibTableColumn
hpnicfQueueIfIndex = _HpnicfQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 1),
    _HpnicfQueueIfIndex_Type()
)
hpnicfQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfQueueIfIndex.setStatus("current")


class _HpnicfQueueScheduleMode_Type(Integer32):
    """Custom type hpnicfQueueScheduleMode based on Integer32"""
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


_HpnicfQueueScheduleMode_Type.__name__ = "Integer32"
_HpnicfQueueScheduleMode_Object = MibTableColumn
hpnicfQueueScheduleMode = _HpnicfQueueScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 2),
    _HpnicfQueueScheduleMode_Type()
)
hpnicfQueueScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueScheduleMode.setStatus("current")
_HpnicfQueueWeight1_Type = Integer32
_HpnicfQueueWeight1_Object = MibTableColumn
hpnicfQueueWeight1 = _HpnicfQueueWeight1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 3),
    _HpnicfQueueWeight1_Type()
)
hpnicfQueueWeight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight1.setStatus("current")
_HpnicfQueueWeight2_Type = Integer32
_HpnicfQueueWeight2_Object = MibTableColumn
hpnicfQueueWeight2 = _HpnicfQueueWeight2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 4),
    _HpnicfQueueWeight2_Type()
)
hpnicfQueueWeight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight2.setStatus("current")
_HpnicfQueueWeight3_Type = Integer32
_HpnicfQueueWeight3_Object = MibTableColumn
hpnicfQueueWeight3 = _HpnicfQueueWeight3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 5),
    _HpnicfQueueWeight3_Type()
)
hpnicfQueueWeight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight3.setStatus("current")
_HpnicfQueueWeight4_Type = Integer32
_HpnicfQueueWeight4_Object = MibTableColumn
hpnicfQueueWeight4 = _HpnicfQueueWeight4_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 6),
    _HpnicfQueueWeight4_Type()
)
hpnicfQueueWeight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight4.setStatus("current")


class _HpnicfQueueMaxDelay_Type(Integer32):
    """Custom type hpnicfQueueMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfQueueMaxDelay_Type.__name__ = "Integer32"
_HpnicfQueueMaxDelay_Object = MibTableColumn
hpnicfQueueMaxDelay = _HpnicfQueueMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 7),
    _HpnicfQueueMaxDelay_Type()
)
hpnicfQueueMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueMaxDelay.setStatus("current")
_HpnicfQueueWeight5_Type = Integer32
_HpnicfQueueWeight5_Object = MibTableColumn
hpnicfQueueWeight5 = _HpnicfQueueWeight5_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 8),
    _HpnicfQueueWeight5_Type()
)
hpnicfQueueWeight5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight5.setStatus("current")
_HpnicfQueueWeight6_Type = Integer32
_HpnicfQueueWeight6_Object = MibTableColumn
hpnicfQueueWeight6 = _HpnicfQueueWeight6_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 9),
    _HpnicfQueueWeight6_Type()
)
hpnicfQueueWeight6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight6.setStatus("current")
_HpnicfQueueWeight7_Type = Integer32
_HpnicfQueueWeight7_Object = MibTableColumn
hpnicfQueueWeight7 = _HpnicfQueueWeight7_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 10),
    _HpnicfQueueWeight7_Type()
)
hpnicfQueueWeight7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight7.setStatus("current")
_HpnicfQueueWeight8_Type = Integer32
_HpnicfQueueWeight8_Object = MibTableColumn
hpnicfQueueWeight8 = _HpnicfQueueWeight8_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 3, 1, 11),
    _HpnicfQueueWeight8_Type()
)
hpnicfQueueWeight8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfQueueWeight8.setStatus("current")
_HpnicfRateLimitTable_Object = MibTable
hpnicfRateLimitTable = _HpnicfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfRateLimitTable.setStatus("current")
_HpnicfRateLimitEntry_Object = MibTableRow
hpnicfRateLimitEntry = _HpnicfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1)
)
hpnicfRateLimitEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRateLimitAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRateLimitIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRateLimitVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRateLimitDirection"),
)
if mibBuilder.loadTexts:
    hpnicfRateLimitEntry.setStatus("current")


class _HpnicfRateLimitAclIndex_Type(Integer32):
    """Custom type hpnicfRateLimitAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfRateLimitAclIndex_Type.__name__ = "Integer32"
_HpnicfRateLimitAclIndex_Object = MibTableColumn
hpnicfRateLimitAclIndex = _HpnicfRateLimitAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 1),
    _HpnicfRateLimitAclIndex_Type()
)
hpnicfRateLimitAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitAclIndex.setStatus("current")
_HpnicfRateLimitIfIndex_Type = Integer32
_HpnicfRateLimitIfIndex_Object = MibTableColumn
hpnicfRateLimitIfIndex = _HpnicfRateLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 2),
    _HpnicfRateLimitIfIndex_Type()
)
hpnicfRateLimitIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitIfIndex.setStatus("current")


class _HpnicfRateLimitVlanID_Type(Integer32):
    """Custom type hpnicfRateLimitVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRateLimitVlanID_Type.__name__ = "Integer32"
_HpnicfRateLimitVlanID_Object = MibTableColumn
hpnicfRateLimitVlanID = _HpnicfRateLimitVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 3),
    _HpnicfRateLimitVlanID_Type()
)
hpnicfRateLimitVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitVlanID.setStatus("current")


class _HpnicfRateLimitDirection_Type(Integer32):
    """Custom type hpnicfRateLimitDirection based on Integer32"""
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


_HpnicfRateLimitDirection_Type.__name__ = "Integer32"
_HpnicfRateLimitDirection_Object = MibTableColumn
hpnicfRateLimitDirection = _HpnicfRateLimitDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 4),
    _HpnicfRateLimitDirection_Type()
)
hpnicfRateLimitDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitDirection.setStatus("current")


class _HpnicfRateLimitUserAclNum_Type(Integer32):
    """Custom type hpnicfRateLimitUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRateLimitUserAclNum_Type.__name__ = "Integer32"
_HpnicfRateLimitUserAclNum_Object = MibTableColumn
hpnicfRateLimitUserAclNum = _HpnicfRateLimitUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 5),
    _HpnicfRateLimitUserAclNum_Type()
)
hpnicfRateLimitUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitUserAclNum.setStatus("current")


class _HpnicfRateLimitUserAclRule_Type(Integer32):
    """Custom type hpnicfRateLimitUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRateLimitUserAclRule_Type.__name__ = "Integer32"
_HpnicfRateLimitUserAclRule_Object = MibTableColumn
hpnicfRateLimitUserAclRule = _HpnicfRateLimitUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 6),
    _HpnicfRateLimitUserAclRule_Type()
)
hpnicfRateLimitUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitUserAclRule.setStatus("current")


class _HpnicfRateLimitIpAclNum_Type(Integer32):
    """Custom type hpnicfRateLimitIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRateLimitIpAclNum_Type.__name__ = "Integer32"
_HpnicfRateLimitIpAclNum_Object = MibTableColumn
hpnicfRateLimitIpAclNum = _HpnicfRateLimitIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 7),
    _HpnicfRateLimitIpAclNum_Type()
)
hpnicfRateLimitIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitIpAclNum.setStatus("current")


class _HpnicfRateLimitIpAclRule_Type(Integer32):
    """Custom type hpnicfRateLimitIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRateLimitIpAclRule_Type.__name__ = "Integer32"
_HpnicfRateLimitIpAclRule_Object = MibTableColumn
hpnicfRateLimitIpAclRule = _HpnicfRateLimitIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 8),
    _HpnicfRateLimitIpAclRule_Type()
)
hpnicfRateLimitIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitIpAclRule.setStatus("current")


class _HpnicfRateLimitLinkAclNum_Type(Integer32):
    """Custom type hpnicfRateLimitLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRateLimitLinkAclNum_Type.__name__ = "Integer32"
_HpnicfRateLimitLinkAclNum_Object = MibTableColumn
hpnicfRateLimitLinkAclNum = _HpnicfRateLimitLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 9),
    _HpnicfRateLimitLinkAclNum_Type()
)
hpnicfRateLimitLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitLinkAclNum.setStatus("current")


class _HpnicfRateLimitLinkAclRule_Type(Integer32):
    """Custom type hpnicfRateLimitLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRateLimitLinkAclRule_Type.__name__ = "Integer32"
_HpnicfRateLimitLinkAclRule_Object = MibTableColumn
hpnicfRateLimitLinkAclRule = _HpnicfRateLimitLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 10),
    _HpnicfRateLimitLinkAclRule_Type()
)
hpnicfRateLimitLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitLinkAclRule.setStatus("current")
_HpnicfRateLimitTargetRateMbps_Type = Integer32
_HpnicfRateLimitTargetRateMbps_Object = MibTableColumn
hpnicfRateLimitTargetRateMbps = _HpnicfRateLimitTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 11),
    _HpnicfRateLimitTargetRateMbps_Type()
)
hpnicfRateLimitTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitTargetRateMbps.setStatus("current")
_HpnicfRateLimitTargetRateKbps_Type = Integer32
_HpnicfRateLimitTargetRateKbps_Object = MibTableColumn
hpnicfRateLimitTargetRateKbps = _HpnicfRateLimitTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 12),
    _HpnicfRateLimitTargetRateKbps_Type()
)
hpnicfRateLimitTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitTargetRateKbps.setStatus("current")


class _HpnicfRateLimitPeakRate_Type(Integer32):
    """Custom type hpnicfRateLimitPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_HpnicfRateLimitPeakRate_Type.__name__ = "Integer32"
_HpnicfRateLimitPeakRate_Object = MibTableColumn
hpnicfRateLimitPeakRate = _HpnicfRateLimitPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 13),
    _HpnicfRateLimitPeakRate_Type()
)
hpnicfRateLimitPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitPeakRate.setStatus("current")


class _HpnicfRateLimitCIR_Type(Integer32):
    """Custom type hpnicfRateLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HpnicfRateLimitCIR_Type.__name__ = "Integer32"
_HpnicfRateLimitCIR_Object = MibTableColumn
hpnicfRateLimitCIR = _HpnicfRateLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 14),
    _HpnicfRateLimitCIR_Type()
)
hpnicfRateLimitCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitCIR.setStatus("current")


class _HpnicfRateLimitCBS_Type(Integer32):
    """Custom type hpnicfRateLimitCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_HpnicfRateLimitCBS_Type.__name__ = "Integer32"
_HpnicfRateLimitCBS_Object = MibTableColumn
hpnicfRateLimitCBS = _HpnicfRateLimitCBS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 15),
    _HpnicfRateLimitCBS_Type()
)
hpnicfRateLimitCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitCBS.setStatus("current")


class _HpnicfRateLimitEBS_Type(Integer32):
    """Custom type hpnicfRateLimitEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_HpnicfRateLimitEBS_Type.__name__ = "Integer32"
_HpnicfRateLimitEBS_Object = MibTableColumn
hpnicfRateLimitEBS = _HpnicfRateLimitEBS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 16),
    _HpnicfRateLimitEBS_Type()
)
hpnicfRateLimitEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitEBS.setStatus("current")


class _HpnicfRateLimitPIR_Type(Integer32):
    """Custom type hpnicfRateLimitPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_HpnicfRateLimitPIR_Type.__name__ = "Integer32"
_HpnicfRateLimitPIR_Object = MibTableColumn
hpnicfRateLimitPIR = _HpnicfRateLimitPIR_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 17),
    _HpnicfRateLimitPIR_Type()
)
hpnicfRateLimitPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitPIR.setStatus("current")


class _HpnicfRateLimitConformLocalPre_Type(Integer32):
    """Custom type hpnicfRateLimitConformLocalPre based on Integer32"""
    defaultValue = 1


_HpnicfRateLimitConformLocalPre_Object = MibTableColumn
hpnicfRateLimitConformLocalPre = _HpnicfRateLimitConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 18),
    _HpnicfRateLimitConformLocalPre_Type()
)
hpnicfRateLimitConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitConformLocalPre.setStatus("current")


class _HpnicfRateLimitConformActionType_Type(Integer32):
    """Custom type hpnicfRateLimitConformActionType based on Integer32"""
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


_HpnicfRateLimitConformActionType_Type.__name__ = "Integer32"
_HpnicfRateLimitConformActionType_Object = MibTableColumn
hpnicfRateLimitConformActionType = _HpnicfRateLimitConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 19),
    _HpnicfRateLimitConformActionType_Type()
)
hpnicfRateLimitConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitConformActionType.setStatus("current")


class _HpnicfRateLimitExceedActionType_Type(Integer32):
    """Custom type hpnicfRateLimitExceedActionType based on Integer32"""
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


_HpnicfRateLimitExceedActionType_Type.__name__ = "Integer32"
_HpnicfRateLimitExceedActionType_Object = MibTableColumn
hpnicfRateLimitExceedActionType = _HpnicfRateLimitExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 20),
    _HpnicfRateLimitExceedActionType_Type()
)
hpnicfRateLimitExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitExceedActionType.setStatus("current")


class _HpnicfRateLimitExceedDscp_Type(Integer32):
    """Custom type hpnicfRateLimitExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRateLimitExceedDscp_Type.__name__ = "Integer32"
_HpnicfRateLimitExceedDscp_Object = MibTableColumn
hpnicfRateLimitExceedDscp = _HpnicfRateLimitExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 21),
    _HpnicfRateLimitExceedDscp_Type()
)
hpnicfRateLimitExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitExceedDscp.setStatus("current")
_HpnicfRateLimitRuntime_Type = TruthValue
_HpnicfRateLimitRuntime_Object = MibTableColumn
hpnicfRateLimitRuntime = _HpnicfRateLimitRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 22),
    _HpnicfRateLimitRuntime_Type()
)
hpnicfRateLimitRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRateLimitRuntime.setStatus("current")
_HpnicfRateLimitRowStatus_Type = RowStatus
_HpnicfRateLimitRowStatus_Object = MibTableColumn
hpnicfRateLimitRowStatus = _HpnicfRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 23),
    _HpnicfRateLimitRowStatus_Type()
)
hpnicfRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitRowStatus.setStatus("current")


class _HpnicfRateLimitExceedCos_Type(Integer32):
    """Custom type hpnicfRateLimitExceedCos based on Integer32"""
    defaultValue = 255


_HpnicfRateLimitExceedCos_Object = MibTableColumn
hpnicfRateLimitExceedCos = _HpnicfRateLimitExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 24),
    _HpnicfRateLimitExceedCos_Type()
)
hpnicfRateLimitExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitExceedCos.setStatus("current")


class _HpnicfRateLimitConformCos_Type(Integer32):
    """Custom type hpnicfRateLimitConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRateLimitConformCos_Type.__name__ = "Integer32"
_HpnicfRateLimitConformCos_Object = MibTableColumn
hpnicfRateLimitConformCos = _HpnicfRateLimitConformCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 25),
    _HpnicfRateLimitConformCos_Type()
)
hpnicfRateLimitConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitConformCos.setStatus("current")


class _HpnicfRateLimitConformDscp_Type(Integer32):
    """Custom type hpnicfRateLimitConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRateLimitConformDscp_Type.__name__ = "Integer32"
_HpnicfRateLimitConformDscp_Object = MibTableColumn
hpnicfRateLimitConformDscp = _HpnicfRateLimitConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 26),
    _HpnicfRateLimitConformDscp_Type()
)
hpnicfRateLimitConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitConformDscp.setStatus("current")
_HpnicfRateLimitMeterStatByteCount_Type = Counter64
_HpnicfRateLimitMeterStatByteCount_Object = MibTableColumn
hpnicfRateLimitMeterStatByteCount = _HpnicfRateLimitMeterStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 27),
    _HpnicfRateLimitMeterStatByteCount_Type()
)
hpnicfRateLimitMeterStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRateLimitMeterStatByteCount.setStatus("current")
_HpnicfRateLimitMeterStatByteXCount_Type = Counter64
_HpnicfRateLimitMeterStatByteXCount_Object = MibTableColumn
hpnicfRateLimitMeterStatByteXCount = _HpnicfRateLimitMeterStatByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 28),
    _HpnicfRateLimitMeterStatByteXCount_Type()
)
hpnicfRateLimitMeterStatByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRateLimitMeterStatByteXCount.setStatus("current")


class _HpnicfRateLimitMeterStatState_Type(Integer32):
    """Custom type hpnicfRateLimitMeterStatState based on Integer32"""
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


_HpnicfRateLimitMeterStatState_Type.__name__ = "Integer32"
_HpnicfRateLimitMeterStatState_Object = MibTableColumn
hpnicfRateLimitMeterStatState = _HpnicfRateLimitMeterStatState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 4, 1, 29),
    _HpnicfRateLimitMeterStatState_Type()
)
hpnicfRateLimitMeterStatState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRateLimitMeterStatState.setStatus("current")
_HpnicfPriorityTable_Object = MibTable
hpnicfPriorityTable = _HpnicfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5)
)
if mibBuilder.loadTexts:
    hpnicfPriorityTable.setStatus("current")
_HpnicfPriorityEntry_Object = MibTableRow
hpnicfPriorityEntry = _HpnicfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1)
)
hpnicfPriorityEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPriorityAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPriorityIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPriorityVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPriorityDirection"),
)
if mibBuilder.loadTexts:
    hpnicfPriorityEntry.setStatus("current")


class _HpnicfPriorityAclIndex_Type(Integer32):
    """Custom type hpnicfPriorityAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfPriorityAclIndex_Type.__name__ = "Integer32"
_HpnicfPriorityAclIndex_Object = MibTableColumn
hpnicfPriorityAclIndex = _HpnicfPriorityAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 1),
    _HpnicfPriorityAclIndex_Type()
)
hpnicfPriorityAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityAclIndex.setStatus("current")
_HpnicfPriorityIfIndex_Type = Integer32
_HpnicfPriorityIfIndex_Object = MibTableColumn
hpnicfPriorityIfIndex = _HpnicfPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 2),
    _HpnicfPriorityIfIndex_Type()
)
hpnicfPriorityIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityIfIndex.setStatus("current")


class _HpnicfPriorityVlanID_Type(Integer32):
    """Custom type hpnicfPriorityVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfPriorityVlanID_Type.__name__ = "Integer32"
_HpnicfPriorityVlanID_Object = MibTableColumn
hpnicfPriorityVlanID = _HpnicfPriorityVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 3),
    _HpnicfPriorityVlanID_Type()
)
hpnicfPriorityVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityVlanID.setStatus("current")


class _HpnicfPriorityDirection_Type(Integer32):
    """Custom type hpnicfPriorityDirection based on Integer32"""
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


_HpnicfPriorityDirection_Type.__name__ = "Integer32"
_HpnicfPriorityDirection_Object = MibTableColumn
hpnicfPriorityDirection = _HpnicfPriorityDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 4),
    _HpnicfPriorityDirection_Type()
)
hpnicfPriorityDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityDirection.setStatus("current")


class _HpnicfPriorityUserAclNum_Type(Integer32):
    """Custom type hpnicfPriorityUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfPriorityUserAclNum_Type.__name__ = "Integer32"
_HpnicfPriorityUserAclNum_Object = MibTableColumn
hpnicfPriorityUserAclNum = _HpnicfPriorityUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 5),
    _HpnicfPriorityUserAclNum_Type()
)
hpnicfPriorityUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityUserAclNum.setStatus("current")


class _HpnicfPriorityUserAclRule_Type(Integer32):
    """Custom type hpnicfPriorityUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPriorityUserAclRule_Type.__name__ = "Integer32"
_HpnicfPriorityUserAclRule_Object = MibTableColumn
hpnicfPriorityUserAclRule = _HpnicfPriorityUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 6),
    _HpnicfPriorityUserAclRule_Type()
)
hpnicfPriorityUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityUserAclRule.setStatus("current")


class _HpnicfPriorityIpAclNum_Type(Integer32):
    """Custom type hpnicfPriorityIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfPriorityIpAclNum_Type.__name__ = "Integer32"
_HpnicfPriorityIpAclNum_Object = MibTableColumn
hpnicfPriorityIpAclNum = _HpnicfPriorityIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 7),
    _HpnicfPriorityIpAclNum_Type()
)
hpnicfPriorityIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityIpAclNum.setStatus("current")


class _HpnicfPriorityIpAclRule_Type(Integer32):
    """Custom type hpnicfPriorityIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPriorityIpAclRule_Type.__name__ = "Integer32"
_HpnicfPriorityIpAclRule_Object = MibTableColumn
hpnicfPriorityIpAclRule = _HpnicfPriorityIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 8),
    _HpnicfPriorityIpAclRule_Type()
)
hpnicfPriorityIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityIpAclRule.setStatus("current")


class _HpnicfPriorityLinkAclNum_Type(Integer32):
    """Custom type hpnicfPriorityLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfPriorityLinkAclNum_Type.__name__ = "Integer32"
_HpnicfPriorityLinkAclNum_Object = MibTableColumn
hpnicfPriorityLinkAclNum = _HpnicfPriorityLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 9),
    _HpnicfPriorityLinkAclNum_Type()
)
hpnicfPriorityLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityLinkAclNum.setStatus("current")


class _HpnicfPriorityLinkAclRule_Type(Integer32):
    """Custom type hpnicfPriorityLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfPriorityLinkAclRule_Type.__name__ = "Integer32"
_HpnicfPriorityLinkAclRule_Object = MibTableColumn
hpnicfPriorityLinkAclRule = _HpnicfPriorityLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 10),
    _HpnicfPriorityLinkAclRule_Type()
)
hpnicfPriorityLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityLinkAclRule.setStatus("current")


class _HpnicfPriorityDscp_Type(Integer32):
    """Custom type hpnicfPriorityDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityDscp_Type.__name__ = "Integer32"
_HpnicfPriorityDscp_Object = MibTableColumn
hpnicfPriorityDscp = _HpnicfPriorityDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 11),
    _HpnicfPriorityDscp_Type()
)
hpnicfPriorityDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityDscp.setStatus("current")


class _HpnicfPriorityIpPre_Type(Integer32):
    """Custom type hpnicfPriorityIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityIpPre_Type.__name__ = "Integer32"
_HpnicfPriorityIpPre_Object = MibTableColumn
hpnicfPriorityIpPre = _HpnicfPriorityIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 12),
    _HpnicfPriorityIpPre_Type()
)
hpnicfPriorityIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityIpPre.setStatus("current")


class _HpnicfPriorityIpPreFromCos_Type(TruthValue):
    """Custom type hpnicfPriorityIpPreFromCos based on TruthValue"""
    defaultValue = 2


_HpnicfPriorityIpPreFromCos_Object = MibTableColumn
hpnicfPriorityIpPreFromCos = _HpnicfPriorityIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 13),
    _HpnicfPriorityIpPreFromCos_Type()
)
hpnicfPriorityIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityIpPreFromCos.setStatus("current")


class _HpnicfPriorityCos_Type(Integer32):
    """Custom type hpnicfPriorityCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityCos_Type.__name__ = "Integer32"
_HpnicfPriorityCos_Object = MibTableColumn
hpnicfPriorityCos = _HpnicfPriorityCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 14),
    _HpnicfPriorityCos_Type()
)
hpnicfPriorityCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityCos.setStatus("current")


class _HpnicfPriorityCosFromIpPre_Type(TruthValue):
    """Custom type hpnicfPriorityCosFromIpPre based on TruthValue"""
    defaultValue = 2


_HpnicfPriorityCosFromIpPre_Object = MibTableColumn
hpnicfPriorityCosFromIpPre = _HpnicfPriorityCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 15),
    _HpnicfPriorityCosFromIpPre_Type()
)
hpnicfPriorityCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityCosFromIpPre.setStatus("current")


class _HpnicfPriorityLocalPre_Type(Integer32):
    """Custom type hpnicfPriorityLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityLocalPre_Type.__name__ = "Integer32"
_HpnicfPriorityLocalPre_Object = MibTableColumn
hpnicfPriorityLocalPre = _HpnicfPriorityLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 16),
    _HpnicfPriorityLocalPre_Type()
)
hpnicfPriorityLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityLocalPre.setStatus("current")


class _HpnicfPriorityPolicedServiceType_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceType based on Integer32"""
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


_HpnicfPriorityPolicedServiceType_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceType_Object = MibTableColumn
hpnicfPriorityPolicedServiceType = _HpnicfPriorityPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 17),
    _HpnicfPriorityPolicedServiceType_Type()
)
hpnicfPriorityPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceType.setStatus("current")


class _HpnicfPriorityPolicedServiceDscp_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityPolicedServiceDscp_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceDscp_Object = MibTableColumn
hpnicfPriorityPolicedServiceDscp = _HpnicfPriorityPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 18),
    _HpnicfPriorityPolicedServiceDscp_Type()
)
hpnicfPriorityPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceDscp.setStatus("current")


class _HpnicfPriorityPolicedServiceExp_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityPolicedServiceExp_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceExp_Object = MibTableColumn
hpnicfPriorityPolicedServiceExp = _HpnicfPriorityPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 19),
    _HpnicfPriorityPolicedServiceExp_Type()
)
hpnicfPriorityPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceExp.setStatus("current")


class _HpnicfPriorityPolicedServiceCos_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityPolicedServiceCos_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceCos_Object = MibTableColumn
hpnicfPriorityPolicedServiceCos = _HpnicfPriorityPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 20),
    _HpnicfPriorityPolicedServiceCos_Type()
)
hpnicfPriorityPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceCos.setStatus("current")


class _HpnicfPriorityPolicedServiceLoaclPre_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceLoaclPre_Object = MibTableColumn
hpnicfPriorityPolicedServiceLoaclPre = _HpnicfPriorityPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 21),
    _HpnicfPriorityPolicedServiceLoaclPre_Type()
)
hpnicfPriorityPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceLoaclPre.setStatus("current")


class _HpnicfPriorityPolicedServiceDropPriority_Type(Integer32):
    """Custom type hpnicfPriorityPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_HpnicfPriorityPolicedServiceDropPriority_Type.__name__ = "Integer32"
_HpnicfPriorityPolicedServiceDropPriority_Object = MibTableColumn
hpnicfPriorityPolicedServiceDropPriority = _HpnicfPriorityPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 22),
    _HpnicfPriorityPolicedServiceDropPriority_Type()
)
hpnicfPriorityPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityPolicedServiceDropPriority.setStatus("current")
_HpnicfPriorityRuntime_Type = TruthValue
_HpnicfPriorityRuntime_Object = MibTableColumn
hpnicfPriorityRuntime = _HpnicfPriorityRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 23),
    _HpnicfPriorityRuntime_Type()
)
hpnicfPriorityRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPriorityRuntime.setStatus("current")
_HpnicfPriorityRowStatus_Type = RowStatus
_HpnicfPriorityRowStatus_Object = MibTableColumn
hpnicfPriorityRowStatus = _HpnicfPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 5, 1, 24),
    _HpnicfPriorityRowStatus_Type()
)
hpnicfPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPriorityRowStatus.setStatus("current")
_HpnicfRedirectTable_Object = MibTable
hpnicfRedirectTable = _HpnicfRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfRedirectTable.setStatus("current")
_HpnicfRedirectEntry_Object = MibTableRow
hpnicfRedirectEntry = _HpnicfRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1)
)
hpnicfRedirectEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedirectAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedirectIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedirectVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedirectDirection"),
)
if mibBuilder.loadTexts:
    hpnicfRedirectEntry.setStatus("current")


class _HpnicfRedirectAclIndex_Type(Integer32):
    """Custom type hpnicfRedirectAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfRedirectAclIndex_Type.__name__ = "Integer32"
_HpnicfRedirectAclIndex_Object = MibTableColumn
hpnicfRedirectAclIndex = _HpnicfRedirectAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 1),
    _HpnicfRedirectAclIndex_Type()
)
hpnicfRedirectAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectAclIndex.setStatus("current")
_HpnicfRedirectIfIndex_Type = Integer32
_HpnicfRedirectIfIndex_Object = MibTableColumn
hpnicfRedirectIfIndex = _HpnicfRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 2),
    _HpnicfRedirectIfIndex_Type()
)
hpnicfRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectIfIndex.setStatus("current")


class _HpnicfRedirectVlanID_Type(Integer32):
    """Custom type hpnicfRedirectVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRedirectVlanID_Type.__name__ = "Integer32"
_HpnicfRedirectVlanID_Object = MibTableColumn
hpnicfRedirectVlanID = _HpnicfRedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 3),
    _HpnicfRedirectVlanID_Type()
)
hpnicfRedirectVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectVlanID.setStatus("current")


class _HpnicfRedirectDirection_Type(Integer32):
    """Custom type hpnicfRedirectDirection based on Integer32"""
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


_HpnicfRedirectDirection_Type.__name__ = "Integer32"
_HpnicfRedirectDirection_Object = MibTableColumn
hpnicfRedirectDirection = _HpnicfRedirectDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 4),
    _HpnicfRedirectDirection_Type()
)
hpnicfRedirectDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectDirection.setStatus("current")


class _HpnicfRedirectUserAclNum_Type(Integer32):
    """Custom type hpnicfRedirectUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRedirectUserAclNum_Type.__name__ = "Integer32"
_HpnicfRedirectUserAclNum_Object = MibTableColumn
hpnicfRedirectUserAclNum = _HpnicfRedirectUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 5),
    _HpnicfRedirectUserAclNum_Type()
)
hpnicfRedirectUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectUserAclNum.setStatus("current")


class _HpnicfRedirectUserAclRule_Type(Integer32):
    """Custom type hpnicfRedirectUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRedirectUserAclRule_Type.__name__ = "Integer32"
_HpnicfRedirectUserAclRule_Object = MibTableColumn
hpnicfRedirectUserAclRule = _HpnicfRedirectUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 6),
    _HpnicfRedirectUserAclRule_Type()
)
hpnicfRedirectUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectUserAclRule.setStatus("current")


class _HpnicfRedirectIpAclNum_Type(Integer32):
    """Custom type hpnicfRedirectIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRedirectIpAclNum_Type.__name__ = "Integer32"
_HpnicfRedirectIpAclNum_Object = MibTableColumn
hpnicfRedirectIpAclNum = _HpnicfRedirectIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 7),
    _HpnicfRedirectIpAclNum_Type()
)
hpnicfRedirectIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectIpAclNum.setStatus("current")


class _HpnicfRedirectIpAclRule_Type(Integer32):
    """Custom type hpnicfRedirectIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRedirectIpAclRule_Type.__name__ = "Integer32"
_HpnicfRedirectIpAclRule_Object = MibTableColumn
hpnicfRedirectIpAclRule = _HpnicfRedirectIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 8),
    _HpnicfRedirectIpAclRule_Type()
)
hpnicfRedirectIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectIpAclRule.setStatus("current")


class _HpnicfRedirectLinkAclNum_Type(Integer32):
    """Custom type hpnicfRedirectLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRedirectLinkAclNum_Type.__name__ = "Integer32"
_HpnicfRedirectLinkAclNum_Object = MibTableColumn
hpnicfRedirectLinkAclNum = _HpnicfRedirectLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 9),
    _HpnicfRedirectLinkAclNum_Type()
)
hpnicfRedirectLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectLinkAclNum.setStatus("current")


class _HpnicfRedirectLinkAclRule_Type(Integer32):
    """Custom type hpnicfRedirectLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRedirectLinkAclRule_Type.__name__ = "Integer32"
_HpnicfRedirectLinkAclRule_Object = MibTableColumn
hpnicfRedirectLinkAclRule = _HpnicfRedirectLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 10),
    _HpnicfRedirectLinkAclRule_Type()
)
hpnicfRedirectLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectLinkAclRule.setStatus("current")


class _HpnicfRedirectToCpu_Type(TruthValue):
    """Custom type hpnicfRedirectToCpu based on TruthValue"""
    defaultValue = 2


_HpnicfRedirectToCpu_Object = MibTableColumn
hpnicfRedirectToCpu = _HpnicfRedirectToCpu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 11),
    _HpnicfRedirectToCpu_Type()
)
hpnicfRedirectToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToCpu.setStatus("current")
_HpnicfRedirectToIfIndex_Type = Integer32
_HpnicfRedirectToIfIndex_Object = MibTableColumn
hpnicfRedirectToIfIndex = _HpnicfRedirectToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 12),
    _HpnicfRedirectToIfIndex_Type()
)
hpnicfRedirectToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToIfIndex.setStatus("current")
_HpnicfRedirectToNextHop1_Type = IpAddress
_HpnicfRedirectToNextHop1_Object = MibTableColumn
hpnicfRedirectToNextHop1 = _HpnicfRedirectToNextHop1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 13),
    _HpnicfRedirectToNextHop1_Type()
)
hpnicfRedirectToNextHop1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToNextHop1.setStatus("current")
_HpnicfRedirectToNextHop2_Type = IpAddress
_HpnicfRedirectToNextHop2_Object = MibTableColumn
hpnicfRedirectToNextHop2 = _HpnicfRedirectToNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 14),
    _HpnicfRedirectToNextHop2_Type()
)
hpnicfRedirectToNextHop2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToNextHop2.setStatus("current")
_HpnicfRedirectRuntime_Type = TruthValue
_HpnicfRedirectRuntime_Object = MibTableColumn
hpnicfRedirectRuntime = _HpnicfRedirectRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 15),
    _HpnicfRedirectRuntime_Type()
)
hpnicfRedirectRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRedirectRuntime.setStatus("current")
_HpnicfRedirectRowStatus_Type = RowStatus
_HpnicfRedirectRowStatus_Object = MibTableColumn
hpnicfRedirectRowStatus = _HpnicfRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 16),
    _HpnicfRedirectRowStatus_Type()
)
hpnicfRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectRowStatus.setStatus("current")


class _HpnicfRedirectToSlotNo_Type(Integer32):
    """Custom type hpnicfRedirectToSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfRedirectToSlotNo_Type.__name__ = "Integer32"
_HpnicfRedirectToSlotNo_Object = MibTableColumn
hpnicfRedirectToSlotNo = _HpnicfRedirectToSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 17),
    _HpnicfRedirectToSlotNo_Type()
)
hpnicfRedirectToSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToSlotNo.setStatus("current")


class _HpnicfRedirectRemarkedDSCP_Type(Integer32):
    """Custom type hpnicfRedirectRemarkedDSCP based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRedirectRemarkedDSCP_Type.__name__ = "Integer32"
_HpnicfRedirectRemarkedDSCP_Object = MibTableColumn
hpnicfRedirectRemarkedDSCP = _HpnicfRedirectRemarkedDSCP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 18),
    _HpnicfRedirectRemarkedDSCP_Type()
)
hpnicfRedirectRemarkedDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectRemarkedDSCP.setStatus("current")


class _HpnicfRedirectRemarkedPri_Type(Integer32):
    """Custom type hpnicfRedirectRemarkedPri based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRedirectRemarkedPri_Type.__name__ = "Integer32"
_HpnicfRedirectRemarkedPri_Object = MibTableColumn
hpnicfRedirectRemarkedPri = _HpnicfRedirectRemarkedPri_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 19),
    _HpnicfRedirectRemarkedPri_Type()
)
hpnicfRedirectRemarkedPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectRemarkedPri.setStatus("current")


class _HpnicfRedirectRemarkedTos_Type(Integer32):
    """Custom type hpnicfRedirectRemarkedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_HpnicfRedirectRemarkedTos_Type.__name__ = "Integer32"
_HpnicfRedirectRemarkedTos_Object = MibTableColumn
hpnicfRedirectRemarkedTos = _HpnicfRedirectRemarkedTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 20),
    _HpnicfRedirectRemarkedTos_Type()
)
hpnicfRedirectRemarkedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectRemarkedTos.setStatus("current")
_HpnicfRedirectToNextHop3_Type = IpAddress
_HpnicfRedirectToNextHop3_Object = MibTableColumn
hpnicfRedirectToNextHop3 = _HpnicfRedirectToNextHop3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 21),
    _HpnicfRedirectToNextHop3_Type()
)
hpnicfRedirectToNextHop3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToNextHop3.setStatus("current")


class _HpnicfRedirectTargetVlanID_Type(Integer32):
    """Custom type hpnicfRedirectTargetVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRedirectTargetVlanID_Type.__name__ = "Integer32"
_HpnicfRedirectTargetVlanID_Object = MibTableColumn
hpnicfRedirectTargetVlanID = _HpnicfRedirectTargetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 22),
    _HpnicfRedirectTargetVlanID_Type()
)
hpnicfRedirectTargetVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectTargetVlanID.setStatus("current")


class _HpnicfRedirectMode_Type(Integer32):
    """Custom type hpnicfRedirectMode based on Integer32"""
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


_HpnicfRedirectMode_Type.__name__ = "Integer32"
_HpnicfRedirectMode_Object = MibTableColumn
hpnicfRedirectMode = _HpnicfRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 23),
    _HpnicfRedirectMode_Type()
)
hpnicfRedirectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectMode.setStatus("current")


class _HpnicfRedirectToNestedVlanID_Type(Integer32):
    """Custom type hpnicfRedirectToNestedVlanID based on Integer32"""
    defaultValue = 0


_HpnicfRedirectToNestedVlanID_Object = MibTableColumn
hpnicfRedirectToNestedVlanID = _HpnicfRedirectToNestedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 24),
    _HpnicfRedirectToNestedVlanID_Type()
)
hpnicfRedirectToNestedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToNestedVlanID.setStatus("current")


class _HpnicfRedirectToModifiedVlanID_Type(Integer32):
    """Custom type hpnicfRedirectToModifiedVlanID based on Integer32"""
    defaultValue = 0


_HpnicfRedirectToModifiedVlanID_Object = MibTableColumn
hpnicfRedirectToModifiedVlanID = _HpnicfRedirectToModifiedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 6, 1, 25),
    _HpnicfRedirectToModifiedVlanID_Type()
)
hpnicfRedirectToModifiedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedirectToModifiedVlanID.setStatus("current")
_HpnicfStatisticTable_Object = MibTable
hpnicfStatisticTable = _HpnicfStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfStatisticTable.setStatus("current")
_HpnicfStatisticEntry_Object = MibTableRow
hpnicfStatisticEntry = _HpnicfStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1)
)
hpnicfStatisticEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfStatisticAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfStatisticIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfStatisticVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfStatisticDirection"),
)
if mibBuilder.loadTexts:
    hpnicfStatisticEntry.setStatus("current")


class _HpnicfStatisticAclIndex_Type(Integer32):
    """Custom type hpnicfStatisticAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfStatisticAclIndex_Type.__name__ = "Integer32"
_HpnicfStatisticAclIndex_Object = MibTableColumn
hpnicfStatisticAclIndex = _HpnicfStatisticAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 1),
    _HpnicfStatisticAclIndex_Type()
)
hpnicfStatisticAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticAclIndex.setStatus("current")
_HpnicfStatisticIfIndex_Type = Integer32
_HpnicfStatisticIfIndex_Object = MibTableColumn
hpnicfStatisticIfIndex = _HpnicfStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 2),
    _HpnicfStatisticIfIndex_Type()
)
hpnicfStatisticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticIfIndex.setStatus("current")


class _HpnicfStatisticVlanID_Type(Integer32):
    """Custom type hpnicfStatisticVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfStatisticVlanID_Type.__name__ = "Integer32"
_HpnicfStatisticVlanID_Object = MibTableColumn
hpnicfStatisticVlanID = _HpnicfStatisticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 3),
    _HpnicfStatisticVlanID_Type()
)
hpnicfStatisticVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticVlanID.setStatus("current")


class _HpnicfStatisticDirection_Type(Integer32):
    """Custom type hpnicfStatisticDirection based on Integer32"""
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


_HpnicfStatisticDirection_Type.__name__ = "Integer32"
_HpnicfStatisticDirection_Object = MibTableColumn
hpnicfStatisticDirection = _HpnicfStatisticDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 4),
    _HpnicfStatisticDirection_Type()
)
hpnicfStatisticDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticDirection.setStatus("current")


class _HpnicfStatisticUserAclNum_Type(Integer32):
    """Custom type hpnicfStatisticUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfStatisticUserAclNum_Type.__name__ = "Integer32"
_HpnicfStatisticUserAclNum_Object = MibTableColumn
hpnicfStatisticUserAclNum = _HpnicfStatisticUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 5),
    _HpnicfStatisticUserAclNum_Type()
)
hpnicfStatisticUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticUserAclNum.setStatus("current")


class _HpnicfStatisticUserAclRule_Type(Integer32):
    """Custom type hpnicfStatisticUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfStatisticUserAclRule_Type.__name__ = "Integer32"
_HpnicfStatisticUserAclRule_Object = MibTableColumn
hpnicfStatisticUserAclRule = _HpnicfStatisticUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 6),
    _HpnicfStatisticUserAclRule_Type()
)
hpnicfStatisticUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticUserAclRule.setStatus("current")


class _HpnicfStatisticIpAclNum_Type(Integer32):
    """Custom type hpnicfStatisticIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfStatisticIpAclNum_Type.__name__ = "Integer32"
_HpnicfStatisticIpAclNum_Object = MibTableColumn
hpnicfStatisticIpAclNum = _HpnicfStatisticIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 7),
    _HpnicfStatisticIpAclNum_Type()
)
hpnicfStatisticIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticIpAclNum.setStatus("current")


class _HpnicfStatisticIpAclRule_Type(Integer32):
    """Custom type hpnicfStatisticIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfStatisticIpAclRule_Type.__name__ = "Integer32"
_HpnicfStatisticIpAclRule_Object = MibTableColumn
hpnicfStatisticIpAclRule = _HpnicfStatisticIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 8),
    _HpnicfStatisticIpAclRule_Type()
)
hpnicfStatisticIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticIpAclRule.setStatus("current")


class _HpnicfStatisticLinkAclNum_Type(Integer32):
    """Custom type hpnicfStatisticLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfStatisticLinkAclNum_Type.__name__ = "Integer32"
_HpnicfStatisticLinkAclNum_Object = MibTableColumn
hpnicfStatisticLinkAclNum = _HpnicfStatisticLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 9),
    _HpnicfStatisticLinkAclNum_Type()
)
hpnicfStatisticLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticLinkAclNum.setStatus("current")


class _HpnicfStatisticLinkAclRule_Type(Integer32):
    """Custom type hpnicfStatisticLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfStatisticLinkAclRule_Type.__name__ = "Integer32"
_HpnicfStatisticLinkAclRule_Object = MibTableColumn
hpnicfStatisticLinkAclRule = _HpnicfStatisticLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 10),
    _HpnicfStatisticLinkAclRule_Type()
)
hpnicfStatisticLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticLinkAclRule.setStatus("current")
_HpnicfStatisticRuntime_Type = TruthValue
_HpnicfStatisticRuntime_Object = MibTableColumn
hpnicfStatisticRuntime = _HpnicfStatisticRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 11),
    _HpnicfStatisticRuntime_Type()
)
hpnicfStatisticRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStatisticRuntime.setStatus("current")
_HpnicfStatisticPacketCount_Type = Counter64
_HpnicfStatisticPacketCount_Object = MibTableColumn
hpnicfStatisticPacketCount = _HpnicfStatisticPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 12),
    _HpnicfStatisticPacketCount_Type()
)
hpnicfStatisticPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStatisticPacketCount.setStatus("current")
_HpnicfStatisticByteCount_Type = Counter64
_HpnicfStatisticByteCount_Object = MibTableColumn
hpnicfStatisticByteCount = _HpnicfStatisticByteCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 13),
    _HpnicfStatisticByteCount_Type()
)
hpnicfStatisticByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStatisticByteCount.setStatus("current")


class _HpnicfStatisticCountClear_Type(Integer32):
    """Custom type hpnicfStatisticCountClear based on Integer32"""
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


_HpnicfStatisticCountClear_Type.__name__ = "Integer32"
_HpnicfStatisticCountClear_Object = MibTableColumn
hpnicfStatisticCountClear = _HpnicfStatisticCountClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 14),
    _HpnicfStatisticCountClear_Type()
)
hpnicfStatisticCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfStatisticCountClear.setStatus("current")
_HpnicfStatisticRowStatus_Type = RowStatus
_HpnicfStatisticRowStatus_Object = MibTableColumn
hpnicfStatisticRowStatus = _HpnicfStatisticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 15),
    _HpnicfStatisticRowStatus_Type()
)
hpnicfStatisticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfStatisticRowStatus.setStatus("current")
_HpnicfStatisticPacketXCount_Type = Counter64
_HpnicfStatisticPacketXCount_Object = MibTableColumn
hpnicfStatisticPacketXCount = _HpnicfStatisticPacketXCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 16),
    _HpnicfStatisticPacketXCount_Type()
)
hpnicfStatisticPacketXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStatisticPacketXCount.setStatus("current")
_HpnicfStatisticByteXCount_Type = Counter64
_HpnicfStatisticByteXCount_Object = MibTableColumn
hpnicfStatisticByteXCount = _HpnicfStatisticByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 7, 1, 17),
    _HpnicfStatisticByteXCount_Type()
)
hpnicfStatisticByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfStatisticByteXCount.setStatus("current")
_HpnicfMirrorTable_Object = MibTable
hpnicfMirrorTable = _HpnicfMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfMirrorTable.setStatus("current")
_HpnicfMirrorEntry_Object = MibTableRow
hpnicfMirrorEntry = _HpnicfMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1)
)
hpnicfMirrorEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirrorAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirrorIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirrorVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirrorDirection"),
)
if mibBuilder.loadTexts:
    hpnicfMirrorEntry.setStatus("current")


class _HpnicfMirrorAclIndex_Type(Integer32):
    """Custom type hpnicfMirrorAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfMirrorAclIndex_Type.__name__ = "Integer32"
_HpnicfMirrorAclIndex_Object = MibTableColumn
hpnicfMirrorAclIndex = _HpnicfMirrorAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 1),
    _HpnicfMirrorAclIndex_Type()
)
hpnicfMirrorAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorAclIndex.setStatus("current")
_HpnicfMirrorIfIndex_Type = Integer32
_HpnicfMirrorIfIndex_Object = MibTableColumn
hpnicfMirrorIfIndex = _HpnicfMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 2),
    _HpnicfMirrorIfIndex_Type()
)
hpnicfMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorIfIndex.setStatus("current")


class _HpnicfMirrorVlanID_Type(Integer32):
    """Custom type hpnicfMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfMirrorVlanID_Type.__name__ = "Integer32"
_HpnicfMirrorVlanID_Object = MibTableColumn
hpnicfMirrorVlanID = _HpnicfMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 3),
    _HpnicfMirrorVlanID_Type()
)
hpnicfMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorVlanID.setStatus("current")


class _HpnicfMirrorDirection_Type(Integer32):
    """Custom type hpnicfMirrorDirection based on Integer32"""
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


_HpnicfMirrorDirection_Type.__name__ = "Integer32"
_HpnicfMirrorDirection_Object = MibTableColumn
hpnicfMirrorDirection = _HpnicfMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 4),
    _HpnicfMirrorDirection_Type()
)
hpnicfMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorDirection.setStatus("current")


class _HpnicfMirrorUserAclNum_Type(Integer32):
    """Custom type hpnicfMirrorUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfMirrorUserAclNum_Type.__name__ = "Integer32"
_HpnicfMirrorUserAclNum_Object = MibTableColumn
hpnicfMirrorUserAclNum = _HpnicfMirrorUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 5),
    _HpnicfMirrorUserAclNum_Type()
)
hpnicfMirrorUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorUserAclNum.setStatus("current")


class _HpnicfMirrorUserAclRule_Type(Integer32):
    """Custom type hpnicfMirrorUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMirrorUserAclRule_Type.__name__ = "Integer32"
_HpnicfMirrorUserAclRule_Object = MibTableColumn
hpnicfMirrorUserAclRule = _HpnicfMirrorUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 6),
    _HpnicfMirrorUserAclRule_Type()
)
hpnicfMirrorUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorUserAclRule.setStatus("current")


class _HpnicfMirrorIpAclNum_Type(Integer32):
    """Custom type hpnicfMirrorIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfMirrorIpAclNum_Type.__name__ = "Integer32"
_HpnicfMirrorIpAclNum_Object = MibTableColumn
hpnicfMirrorIpAclNum = _HpnicfMirrorIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 7),
    _HpnicfMirrorIpAclNum_Type()
)
hpnicfMirrorIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorIpAclNum.setStatus("current")


class _HpnicfMirrorIpAclRule_Type(Integer32):
    """Custom type hpnicfMirrorIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMirrorIpAclRule_Type.__name__ = "Integer32"
_HpnicfMirrorIpAclRule_Object = MibTableColumn
hpnicfMirrorIpAclRule = _HpnicfMirrorIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 8),
    _HpnicfMirrorIpAclRule_Type()
)
hpnicfMirrorIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorIpAclRule.setStatus("current")


class _HpnicfMirrorLinkAclNum_Type(Integer32):
    """Custom type hpnicfMirrorLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfMirrorLinkAclNum_Type.__name__ = "Integer32"
_HpnicfMirrorLinkAclNum_Object = MibTableColumn
hpnicfMirrorLinkAclNum = _HpnicfMirrorLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 9),
    _HpnicfMirrorLinkAclNum_Type()
)
hpnicfMirrorLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorLinkAclNum.setStatus("current")


class _HpnicfMirrorLinkAclRule_Type(Integer32):
    """Custom type hpnicfMirrorLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfMirrorLinkAclRule_Type.__name__ = "Integer32"
_HpnicfMirrorLinkAclRule_Object = MibTableColumn
hpnicfMirrorLinkAclRule = _HpnicfMirrorLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 10),
    _HpnicfMirrorLinkAclRule_Type()
)
hpnicfMirrorLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorLinkAclRule.setStatus("current")
_HpnicfMirrorToIfIndex_Type = Integer32
_HpnicfMirrorToIfIndex_Object = MibTableColumn
hpnicfMirrorToIfIndex = _HpnicfMirrorToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 11),
    _HpnicfMirrorToIfIndex_Type()
)
hpnicfMirrorToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorToIfIndex.setStatus("current")
_HpnicfMirrorToCpu_Type = TruthValue
_HpnicfMirrorToCpu_Object = MibTableColumn
hpnicfMirrorToCpu = _HpnicfMirrorToCpu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 12),
    _HpnicfMirrorToCpu_Type()
)
hpnicfMirrorToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorToCpu.setStatus("current")
_HpnicfMirrorRuntime_Type = TruthValue
_HpnicfMirrorRuntime_Object = MibTableColumn
hpnicfMirrorRuntime = _HpnicfMirrorRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 13),
    _HpnicfMirrorRuntime_Type()
)
hpnicfMirrorRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMirrorRuntime.setStatus("current")
_HpnicfMirrorRowStatus_Type = RowStatus
_HpnicfMirrorRowStatus_Object = MibTableColumn
hpnicfMirrorRowStatus = _HpnicfMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 14),
    _HpnicfMirrorRowStatus_Type()
)
hpnicfMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorRowStatus.setStatus("current")
_HpnicfMirrorToGroup_Type = Integer32
_HpnicfMirrorToGroup_Object = MibTableColumn
hpnicfMirrorToGroup = _HpnicfMirrorToGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 8, 1, 15),
    _HpnicfMirrorToGroup_Type()
)
hpnicfMirrorToGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorToGroup.setStatus("current")
_HpnicfPortMirrorTable_Object = MibTable
hpnicfPortMirrorTable = _HpnicfPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 9)
)
if mibBuilder.loadTexts:
    hpnicfPortMirrorTable.setStatus("current")
_HpnicfPortMirrorEntry_Object = MibTableRow
hpnicfPortMirrorEntry = _HpnicfPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 9, 1)
)
hpnicfPortMirrorEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortMirrorIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortMirrorEntry.setStatus("current")
_HpnicfPortMirrorIfIndex_Type = Integer32
_HpnicfPortMirrorIfIndex_Object = MibTableColumn
hpnicfPortMirrorIfIndex = _HpnicfPortMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 9, 1, 1),
    _HpnicfPortMirrorIfIndex_Type()
)
hpnicfPortMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortMirrorIfIndex.setStatus("current")


class _HpnicfPortMirrorDirection_Type(Integer32):
    """Custom type hpnicfPortMirrorDirection based on Integer32"""
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


_HpnicfPortMirrorDirection_Type.__name__ = "Integer32"
_HpnicfPortMirrorDirection_Object = MibTableColumn
hpnicfPortMirrorDirection = _HpnicfPortMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 9, 1, 2),
    _HpnicfPortMirrorDirection_Type()
)
hpnicfPortMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortMirrorDirection.setStatus("current")
_HpnicfPortMirrorRowStatus_Type = RowStatus
_HpnicfPortMirrorRowStatus_Object = MibTableColumn
hpnicfPortMirrorRowStatus = _HpnicfPortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 9, 1, 3),
    _HpnicfPortMirrorRowStatus_Type()
)
hpnicfPortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortMirrorRowStatus.setStatus("current")
_HpnicfLineRateTable_Object = MibTable
hpnicfLineRateTable = _HpnicfLineRateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10)
)
if mibBuilder.loadTexts:
    hpnicfLineRateTable.setStatus("current")
_HpnicfLineRateEntry_Object = MibTableRow
hpnicfLineRateEntry = _HpnicfLineRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10, 1)
)
hpnicfLineRateEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfLineRateIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfLineRateDirection"),
)
if mibBuilder.loadTexts:
    hpnicfLineRateEntry.setStatus("current")
_HpnicfLineRateIfIndex_Type = Integer32
_HpnicfLineRateIfIndex_Object = MibTableColumn
hpnicfLineRateIfIndex = _HpnicfLineRateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10, 1, 1),
    _HpnicfLineRateIfIndex_Type()
)
hpnicfLineRateIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLineRateIfIndex.setStatus("current")


class _HpnicfLineRateDirection_Type(Integer32):
    """Custom type hpnicfLineRateDirection based on Integer32"""
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


_HpnicfLineRateDirection_Type.__name__ = "Integer32"
_HpnicfLineRateDirection_Object = MibTableColumn
hpnicfLineRateDirection = _HpnicfLineRateDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10, 1, 2),
    _HpnicfLineRateDirection_Type()
)
hpnicfLineRateDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLineRateDirection.setStatus("current")
_HpnicfLineRateValue_Type = Integer32
_HpnicfLineRateValue_Object = MibTableColumn
hpnicfLineRateValue = _HpnicfLineRateValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10, 1, 3),
    _HpnicfLineRateValue_Type()
)
hpnicfLineRateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLineRateValue.setStatus("current")
_HpnicfLineRateRowStatus_Type = RowStatus
_HpnicfLineRateRowStatus_Object = MibTableColumn
hpnicfLineRateRowStatus = _HpnicfLineRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 10, 1, 4),
    _HpnicfLineRateRowStatus_Type()
)
hpnicfLineRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfLineRateRowStatus.setStatus("current")
_HpnicfBandwidthTable_Object = MibTable
hpnicfBandwidthTable = _HpnicfBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11)
)
if mibBuilder.loadTexts:
    hpnicfBandwidthTable.setStatus("current")
_HpnicfBandwidthEntry_Object = MibTableRow
hpnicfBandwidthEntry = _HpnicfBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1)
)
hpnicfBandwidthEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfBandwidthAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfBandwidthIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfBandwidthVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfBandwidthDirection"),
)
if mibBuilder.loadTexts:
    hpnicfBandwidthEntry.setStatus("current")


class _HpnicfBandwidthAclIndex_Type(Integer32):
    """Custom type hpnicfBandwidthAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfBandwidthAclIndex_Type.__name__ = "Integer32"
_HpnicfBandwidthAclIndex_Object = MibTableColumn
hpnicfBandwidthAclIndex = _HpnicfBandwidthAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 1),
    _HpnicfBandwidthAclIndex_Type()
)
hpnicfBandwidthAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthAclIndex.setStatus("current")
_HpnicfBandwidthIfIndex_Type = Integer32
_HpnicfBandwidthIfIndex_Object = MibTableColumn
hpnicfBandwidthIfIndex = _HpnicfBandwidthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 2),
    _HpnicfBandwidthIfIndex_Type()
)
hpnicfBandwidthIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthIfIndex.setStatus("current")


class _HpnicfBandwidthVlanID_Type(Integer32):
    """Custom type hpnicfBandwidthVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfBandwidthVlanID_Type.__name__ = "Integer32"
_HpnicfBandwidthVlanID_Object = MibTableColumn
hpnicfBandwidthVlanID = _HpnicfBandwidthVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 3),
    _HpnicfBandwidthVlanID_Type()
)
hpnicfBandwidthVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthVlanID.setStatus("current")


class _HpnicfBandwidthDirection_Type(Integer32):
    """Custom type hpnicfBandwidthDirection based on Integer32"""
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


_HpnicfBandwidthDirection_Type.__name__ = "Integer32"
_HpnicfBandwidthDirection_Object = MibTableColumn
hpnicfBandwidthDirection = _HpnicfBandwidthDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 4),
    _HpnicfBandwidthDirection_Type()
)
hpnicfBandwidthDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthDirection.setStatus("current")


class _HpnicfBandwidthIpAclNum_Type(Integer32):
    """Custom type hpnicfBandwidthIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfBandwidthIpAclNum_Type.__name__ = "Integer32"
_HpnicfBandwidthIpAclNum_Object = MibTableColumn
hpnicfBandwidthIpAclNum = _HpnicfBandwidthIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 5),
    _HpnicfBandwidthIpAclNum_Type()
)
hpnicfBandwidthIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthIpAclNum.setStatus("current")


class _HpnicfBandwidthIpAclRule_Type(Integer32):
    """Custom type hpnicfBandwidthIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfBandwidthIpAclRule_Type.__name__ = "Integer32"
_HpnicfBandwidthIpAclRule_Object = MibTableColumn
hpnicfBandwidthIpAclRule = _HpnicfBandwidthIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 6),
    _HpnicfBandwidthIpAclRule_Type()
)
hpnicfBandwidthIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthIpAclRule.setStatus("current")


class _HpnicfBandwidthLinkAclNum_Type(Integer32):
    """Custom type hpnicfBandwidthLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfBandwidthLinkAclNum_Type.__name__ = "Integer32"
_HpnicfBandwidthLinkAclNum_Object = MibTableColumn
hpnicfBandwidthLinkAclNum = _HpnicfBandwidthLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 7),
    _HpnicfBandwidthLinkAclNum_Type()
)
hpnicfBandwidthLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthLinkAclNum.setStatus("current")


class _HpnicfBandwidthLinkAclRule_Type(Integer32):
    """Custom type hpnicfBandwidthLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfBandwidthLinkAclRule_Type.__name__ = "Integer32"
_HpnicfBandwidthLinkAclRule_Object = MibTableColumn
hpnicfBandwidthLinkAclRule = _HpnicfBandwidthLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 8),
    _HpnicfBandwidthLinkAclRule_Type()
)
hpnicfBandwidthLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfBandwidthLinkAclRule.setStatus("current")


class _HpnicfBandwidthMinGuaranteedWidth_Type(Integer32):
    """Custom type hpnicfBandwidthMinGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_HpnicfBandwidthMinGuaranteedWidth_Type.__name__ = "Integer32"
_HpnicfBandwidthMinGuaranteedWidth_Object = MibTableColumn
hpnicfBandwidthMinGuaranteedWidth = _HpnicfBandwidthMinGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 9),
    _HpnicfBandwidthMinGuaranteedWidth_Type()
)
hpnicfBandwidthMinGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBandwidthMinGuaranteedWidth.setStatus("current")


class _HpnicfBandwidthMaxGuaranteedWidth_Type(Integer32):
    """Custom type hpnicfBandwidthMaxGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_HpnicfBandwidthMaxGuaranteedWidth_Type.__name__ = "Integer32"
_HpnicfBandwidthMaxGuaranteedWidth_Object = MibTableColumn
hpnicfBandwidthMaxGuaranteedWidth = _HpnicfBandwidthMaxGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 10),
    _HpnicfBandwidthMaxGuaranteedWidth_Type()
)
hpnicfBandwidthMaxGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBandwidthMaxGuaranteedWidth.setStatus("current")


class _HpnicfBandwidthWeight_Type(Integer32):
    """Custom type hpnicfBandwidthWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfBandwidthWeight_Type.__name__ = "Integer32"
_HpnicfBandwidthWeight_Object = MibTableColumn
hpnicfBandwidthWeight = _HpnicfBandwidthWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 11),
    _HpnicfBandwidthWeight_Type()
)
hpnicfBandwidthWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBandwidthWeight.setStatus("current")
_HpnicfBandwidthRuntime_Type = TruthValue
_HpnicfBandwidthRuntime_Object = MibTableColumn
hpnicfBandwidthRuntime = _HpnicfBandwidthRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 12),
    _HpnicfBandwidthRuntime_Type()
)
hpnicfBandwidthRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfBandwidthRuntime.setStatus("current")
_HpnicfBandwidthRowStatus_Type = RowStatus
_HpnicfBandwidthRowStatus_Object = MibTableColumn
hpnicfBandwidthRowStatus = _HpnicfBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 11, 1, 13),
    _HpnicfBandwidthRowStatus_Type()
)
hpnicfBandwidthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBandwidthRowStatus.setStatus("current")
_HpnicfRedTable_Object = MibTable
hpnicfRedTable = _HpnicfRedTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12)
)
if mibBuilder.loadTexts:
    hpnicfRedTable.setStatus("current")
_HpnicfRedEntry_Object = MibTableRow
hpnicfRedEntry = _HpnicfRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1)
)
hpnicfRedEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRedDirection"),
)
if mibBuilder.loadTexts:
    hpnicfRedEntry.setStatus("current")


class _HpnicfRedAclIndex_Type(Integer32):
    """Custom type hpnicfRedAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfRedAclIndex_Type.__name__ = "Integer32"
_HpnicfRedAclIndex_Object = MibTableColumn
hpnicfRedAclIndex = _HpnicfRedAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 1),
    _HpnicfRedAclIndex_Type()
)
hpnicfRedAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedAclIndex.setStatus("current")
_HpnicfRedIfIndex_Type = Integer32
_HpnicfRedIfIndex_Object = MibTableColumn
hpnicfRedIfIndex = _HpnicfRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 2),
    _HpnicfRedIfIndex_Type()
)
hpnicfRedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedIfIndex.setStatus("current")


class _HpnicfRedVlanID_Type(Integer32):
    """Custom type hpnicfRedVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRedVlanID_Type.__name__ = "Integer32"
_HpnicfRedVlanID_Object = MibTableColumn
hpnicfRedVlanID = _HpnicfRedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 3),
    _HpnicfRedVlanID_Type()
)
hpnicfRedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedVlanID.setStatus("current")


class _HpnicfRedDirection_Type(Integer32):
    """Custom type hpnicfRedDirection based on Integer32"""
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


_HpnicfRedDirection_Type.__name__ = "Integer32"
_HpnicfRedDirection_Object = MibTableColumn
hpnicfRedDirection = _HpnicfRedDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 4),
    _HpnicfRedDirection_Type()
)
hpnicfRedDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedDirection.setStatus("current")


class _HpnicfRedIpAclNum_Type(Integer32):
    """Custom type hpnicfRedIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRedIpAclNum_Type.__name__ = "Integer32"
_HpnicfRedIpAclNum_Object = MibTableColumn
hpnicfRedIpAclNum = _HpnicfRedIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 5),
    _HpnicfRedIpAclNum_Type()
)
hpnicfRedIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedIpAclNum.setStatus("current")


class _HpnicfRedIpAclRule_Type(Integer32):
    """Custom type hpnicfRedIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRedIpAclRule_Type.__name__ = "Integer32"
_HpnicfRedIpAclRule_Object = MibTableColumn
hpnicfRedIpAclRule = _HpnicfRedIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 6),
    _HpnicfRedIpAclRule_Type()
)
hpnicfRedIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedIpAclRule.setStatus("current")


class _HpnicfRedLinkAclNum_Type(Integer32):
    """Custom type hpnicfRedLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRedLinkAclNum_Type.__name__ = "Integer32"
_HpnicfRedLinkAclNum_Object = MibTableColumn
hpnicfRedLinkAclNum = _HpnicfRedLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 7),
    _HpnicfRedLinkAclNum_Type()
)
hpnicfRedLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedLinkAclNum.setStatus("current")


class _HpnicfRedLinkAclRule_Type(Integer32):
    """Custom type hpnicfRedLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRedLinkAclRule_Type.__name__ = "Integer32"
_HpnicfRedLinkAclRule_Object = MibTableColumn
hpnicfRedLinkAclRule = _HpnicfRedLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 8),
    _HpnicfRedLinkAclRule_Type()
)
hpnicfRedLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRedLinkAclRule.setStatus("current")


class _HpnicfRedStartQueueLen_Type(Integer32):
    """Custom type hpnicfRedStartQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_HpnicfRedStartQueueLen_Type.__name__ = "Integer32"
_HpnicfRedStartQueueLen_Object = MibTableColumn
hpnicfRedStartQueueLen = _HpnicfRedStartQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 9),
    _HpnicfRedStartQueueLen_Type()
)
hpnicfRedStartQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRedStartQueueLen.setStatus("current")


class _HpnicfRedStopQueueLen_Type(Integer32):
    """Custom type hpnicfRedStopQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_HpnicfRedStopQueueLen_Type.__name__ = "Integer32"
_HpnicfRedStopQueueLen_Object = MibTableColumn
hpnicfRedStopQueueLen = _HpnicfRedStopQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 10),
    _HpnicfRedStopQueueLen_Type()
)
hpnicfRedStopQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRedStopQueueLen.setStatus("current")


class _HpnicfRedProbability_Type(Integer32):
    """Custom type hpnicfRedProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfRedProbability_Type.__name__ = "Integer32"
_HpnicfRedProbability_Object = MibTableColumn
hpnicfRedProbability = _HpnicfRedProbability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 11),
    _HpnicfRedProbability_Type()
)
hpnicfRedProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRedProbability.setStatus("current")
_HpnicfRedRuntime_Type = TruthValue
_HpnicfRedRuntime_Object = MibTableColumn
hpnicfRedRuntime = _HpnicfRedRuntime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 12),
    _HpnicfRedRuntime_Type()
)
hpnicfRedRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRedRuntime.setStatus("current")
_HpnicfRedRowStatus_Type = RowStatus
_HpnicfRedRowStatus_Object = MibTableColumn
hpnicfRedRowStatus = _HpnicfRedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 12, 1, 13),
    _HpnicfRedRowStatus_Type()
)
hpnicfRedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfRedRowStatus.setStatus("current")
_HpnicfMirrorGroupTable_Object = MibTable
hpnicfMirrorGroupTable = _HpnicfMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13)
)
if mibBuilder.loadTexts:
    hpnicfMirrorGroupTable.setStatus("current")
_HpnicfMirrorGroupEntry_Object = MibTableRow
hpnicfMirrorGroupEntry = _HpnicfMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1)
)
hpnicfMirrorGroupEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirrorGroupEntry.setStatus("current")


class _HpnicfMirrorGroupID_Type(Integer32):
    """Custom type hpnicfMirrorGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfMirrorGroupID_Type.__name__ = "Integer32"
_HpnicfMirrorGroupID_Object = MibTableColumn
hpnicfMirrorGroupID = _HpnicfMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1, 1),
    _HpnicfMirrorGroupID_Type()
)
hpnicfMirrorGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMirrorGroupID.setStatus("current")


class _HpnicfMirrorGroupDirection_Type(Integer32):
    """Custom type hpnicfMirrorGroupDirection based on Integer32"""
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


_HpnicfMirrorGroupDirection_Type.__name__ = "Integer32"
_HpnicfMirrorGroupDirection_Object = MibTableColumn
hpnicfMirrorGroupDirection = _HpnicfMirrorGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1, 2),
    _HpnicfMirrorGroupDirection_Type()
)
hpnicfMirrorGroupDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMirrorGroupDirection.setStatus("current")


class _HpnicfMirrorGroupMirrorIfIndexList_Type(OctetString):
    """Custom type hpnicfMirrorGroupMirrorIfIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_HpnicfMirrorGroupMirrorIfIndexList_Type.__name__ = "OctetString"
_HpnicfMirrorGroupMirrorIfIndexList_Object = MibTableColumn
hpnicfMirrorGroupMirrorIfIndexList = _HpnicfMirrorGroupMirrorIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1, 3),
    _HpnicfMirrorGroupMirrorIfIndexList_Type()
)
hpnicfMirrorGroupMirrorIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMirrorGroupMirrorIfIndexList.setStatus("current")
_HpnicfMirrorGroupMonitorIfIndex_Type = Integer32
_HpnicfMirrorGroupMonitorIfIndex_Object = MibTableColumn
hpnicfMirrorGroupMonitorIfIndex = _HpnicfMirrorGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1, 4),
    _HpnicfMirrorGroupMonitorIfIndex_Type()
)
hpnicfMirrorGroupMonitorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMirrorGroupMonitorIfIndex.setStatus("current")
_HpnicfMirrorGroupRowStatus_Type = RowStatus
_HpnicfMirrorGroupRowStatus_Object = MibTableColumn
hpnicfMirrorGroupRowStatus = _HpnicfMirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 13, 1, 5),
    _HpnicfMirrorGroupRowStatus_Type()
)
hpnicfMirrorGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMirrorGroupRowStatus.setStatus("current")
_HpnicfFlowtempTable_Object = MibTable
hpnicfFlowtempTable = _HpnicfFlowtempTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14)
)
if mibBuilder.loadTexts:
    hpnicfFlowtempTable.setStatus("current")
_HpnicfFlowtempEntry_Object = MibTableRow
hpnicfFlowtempEntry = _HpnicfFlowtempEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1)
)
hpnicfFlowtempEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfFlowtempIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFlowtempEntry.setStatus("current")


class _HpnicfFlowtempIndex_Type(Integer32):
    """Custom type hpnicfFlowtempIndex based on Integer32"""
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


_HpnicfFlowtempIndex_Type.__name__ = "Integer32"
_HpnicfFlowtempIndex_Object = MibTableColumn
hpnicfFlowtempIndex = _HpnicfFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 1),
    _HpnicfFlowtempIndex_Type()
)
hpnicfFlowtempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlowtempIndex.setStatus("current")
_HpnicfFlowtempIpProtocol_Type = TruthValue
_HpnicfFlowtempIpProtocol_Object = MibTableColumn
hpnicfFlowtempIpProtocol = _HpnicfFlowtempIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 2),
    _HpnicfFlowtempIpProtocol_Type()
)
hpnicfFlowtempIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempIpProtocol.setStatus("current")
_HpnicfFlowtempTcpFlag_Type = TruthValue
_HpnicfFlowtempTcpFlag_Object = MibTableColumn
hpnicfFlowtempTcpFlag = _HpnicfFlowtempTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 3),
    _HpnicfFlowtempTcpFlag_Type()
)
hpnicfFlowtempTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempTcpFlag.setStatus("current")
_HpnicfFlowtempSPort_Type = TruthValue
_HpnicfFlowtempSPort_Object = MibTableColumn
hpnicfFlowtempSPort = _HpnicfFlowtempSPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 4),
    _HpnicfFlowtempSPort_Type()
)
hpnicfFlowtempSPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempSPort.setStatus("current")
_HpnicfFlowtempDPort_Type = TruthValue
_HpnicfFlowtempDPort_Object = MibTableColumn
hpnicfFlowtempDPort = _HpnicfFlowtempDPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 5),
    _HpnicfFlowtempDPort_Type()
)
hpnicfFlowtempDPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDPort.setStatus("current")
_HpnicfFlowtempIcmpType_Type = TruthValue
_HpnicfFlowtempIcmpType_Object = MibTableColumn
hpnicfFlowtempIcmpType = _HpnicfFlowtempIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 6),
    _HpnicfFlowtempIcmpType_Type()
)
hpnicfFlowtempIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempIcmpType.setStatus("current")
_HpnicfFlowtempIcmpCode_Type = TruthValue
_HpnicfFlowtempIcmpCode_Object = MibTableColumn
hpnicfFlowtempIcmpCode = _HpnicfFlowtempIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 7),
    _HpnicfFlowtempIcmpCode_Type()
)
hpnicfFlowtempIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempIcmpCode.setStatus("current")
_HpnicfFlowtempFragment_Type = TruthValue
_HpnicfFlowtempFragment_Object = MibTableColumn
hpnicfFlowtempFragment = _HpnicfFlowtempFragment_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 8),
    _HpnicfFlowtempFragment_Type()
)
hpnicfFlowtempFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempFragment.setStatus("current")
_HpnicfFlowtempDscp_Type = TruthValue
_HpnicfFlowtempDscp_Object = MibTableColumn
hpnicfFlowtempDscp = _HpnicfFlowtempDscp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 9),
    _HpnicfFlowtempDscp_Type()
)
hpnicfFlowtempDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDscp.setStatus("current")
_HpnicfFlowtempIpPre_Type = TruthValue
_HpnicfFlowtempIpPre_Object = MibTableColumn
hpnicfFlowtempIpPre = _HpnicfFlowtempIpPre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 10),
    _HpnicfFlowtempIpPre_Type()
)
hpnicfFlowtempIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempIpPre.setStatus("current")
_HpnicfFlowtempTos_Type = TruthValue
_HpnicfFlowtempTos_Object = MibTableColumn
hpnicfFlowtempTos = _HpnicfFlowtempTos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 11),
    _HpnicfFlowtempTos_Type()
)
hpnicfFlowtempTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempTos.setStatus("current")
_HpnicfFlowtempSIp_Type = TruthValue
_HpnicfFlowtempSIp_Object = MibTableColumn
hpnicfFlowtempSIp = _HpnicfFlowtempSIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 12),
    _HpnicfFlowtempSIp_Type()
)
hpnicfFlowtempSIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempSIp.setStatus("current")
_HpnicfFlowtempSIpMask_Type = IpAddress
_HpnicfFlowtempSIpMask_Object = MibTableColumn
hpnicfFlowtempSIpMask = _HpnicfFlowtempSIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 13),
    _HpnicfFlowtempSIpMask_Type()
)
hpnicfFlowtempSIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempSIpMask.setStatus("current")
_HpnicfFlowtempDIp_Type = TruthValue
_HpnicfFlowtempDIp_Object = MibTableColumn
hpnicfFlowtempDIp = _HpnicfFlowtempDIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 14),
    _HpnicfFlowtempDIp_Type()
)
hpnicfFlowtempDIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDIp.setStatus("current")
_HpnicfFlowtempDIpMask_Type = IpAddress
_HpnicfFlowtempDIpMask_Object = MibTableColumn
hpnicfFlowtempDIpMask = _HpnicfFlowtempDIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 15),
    _HpnicfFlowtempDIpMask_Type()
)
hpnicfFlowtempDIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDIpMask.setStatus("current")
_HpnicfFlowtempEthProtocol_Type = TruthValue
_HpnicfFlowtempEthProtocol_Object = MibTableColumn
hpnicfFlowtempEthProtocol = _HpnicfFlowtempEthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 16),
    _HpnicfFlowtempEthProtocol_Type()
)
hpnicfFlowtempEthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempEthProtocol.setStatus("current")
_HpnicfFlowtempSMac_Type = TruthValue
_HpnicfFlowtempSMac_Object = MibTableColumn
hpnicfFlowtempSMac = _HpnicfFlowtempSMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 17),
    _HpnicfFlowtempSMac_Type()
)
hpnicfFlowtempSMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempSMac.setStatus("current")
_HpnicfFlowtempSMacMask_Type = MacAddress
_HpnicfFlowtempSMacMask_Object = MibTableColumn
hpnicfFlowtempSMacMask = _HpnicfFlowtempSMacMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 18),
    _HpnicfFlowtempSMacMask_Type()
)
hpnicfFlowtempSMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempSMacMask.setStatus("current")
_HpnicfFlowtempDMac_Type = TruthValue
_HpnicfFlowtempDMac_Object = MibTableColumn
hpnicfFlowtempDMac = _HpnicfFlowtempDMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 19),
    _HpnicfFlowtempDMac_Type()
)
hpnicfFlowtempDMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDMac.setStatus("current")
_HpnicfFlowtempDMacMask_Type = MacAddress
_HpnicfFlowtempDMacMask_Object = MibTableColumn
hpnicfFlowtempDMacMask = _HpnicfFlowtempDMacMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 20),
    _HpnicfFlowtempDMacMask_Type()
)
hpnicfFlowtempDMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempDMacMask.setStatus("current")
_HpnicfFlowtempVpn_Type = TruthValue
_HpnicfFlowtempVpn_Object = MibTableColumn
hpnicfFlowtempVpn = _HpnicfFlowtempVpn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 21),
    _HpnicfFlowtempVpn_Type()
)
hpnicfFlowtempVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempVpn.setStatus("current")
_HpnicfFlowtempRowStatus_Type = RowStatus
_HpnicfFlowtempRowStatus_Object = MibTableColumn
hpnicfFlowtempRowStatus = _HpnicfFlowtempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 22),
    _HpnicfFlowtempRowStatus_Type()
)
hpnicfFlowtempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempRowStatus.setStatus("current")
_HpnicfFlowtempVlanId_Type = TruthValue
_HpnicfFlowtempVlanId_Object = MibTableColumn
hpnicfFlowtempVlanId = _HpnicfFlowtempVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 23),
    _HpnicfFlowtempVlanId_Type()
)
hpnicfFlowtempVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempVlanId.setStatus("current")
_HpnicfFlowtempCos_Type = TruthValue
_HpnicfFlowtempCos_Object = MibTableColumn
hpnicfFlowtempCos = _HpnicfFlowtempCos_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 14, 1, 24),
    _HpnicfFlowtempCos_Type()
)
hpnicfFlowtempCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempCos.setStatus("current")
_HpnicfFlowtempEnableTable_Object = MibTable
hpnicfFlowtempEnableTable = _HpnicfFlowtempEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 15)
)
if mibBuilder.loadTexts:
    hpnicfFlowtempEnableTable.setStatus("current")
_HpnicfFlowtempEnableEntry_Object = MibTableRow
hpnicfFlowtempEnableEntry = _HpnicfFlowtempEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 15, 1)
)
hpnicfFlowtempEnableEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfFlowtempEnableIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfFlowtempEnableVlanID"),
)
if mibBuilder.loadTexts:
    hpnicfFlowtempEnableEntry.setStatus("current")
_HpnicfFlowtempEnableIfIndex_Type = Integer32
_HpnicfFlowtempEnableIfIndex_Object = MibTableColumn
hpnicfFlowtempEnableIfIndex = _HpnicfFlowtempEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 15, 1, 1),
    _HpnicfFlowtempEnableIfIndex_Type()
)
hpnicfFlowtempEnableIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempEnableIfIndex.setStatus("current")


class _HpnicfFlowtempEnableVlanID_Type(Integer32):
    """Custom type hpnicfFlowtempEnableVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfFlowtempEnableVlanID_Type.__name__ = "Integer32"
_HpnicfFlowtempEnableVlanID_Object = MibTableColumn
hpnicfFlowtempEnableVlanID = _HpnicfFlowtempEnableVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 15, 1, 2),
    _HpnicfFlowtempEnableVlanID_Type()
)
hpnicfFlowtempEnableVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFlowtempEnableVlanID.setStatus("current")


class _HpnicfFlowtempEnableFlowtempIndex_Type(Integer32):
    """Custom type hpnicfFlowtempEnableFlowtempIndex based on Integer32"""
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


_HpnicfFlowtempEnableFlowtempIndex_Type.__name__ = "Integer32"
_HpnicfFlowtempEnableFlowtempIndex_Object = MibTableColumn
hpnicfFlowtempEnableFlowtempIndex = _HpnicfFlowtempEnableFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 15, 1, 3),
    _HpnicfFlowtempEnableFlowtempIndex_Type()
)
hpnicfFlowtempEnableFlowtempIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFlowtempEnableFlowtempIndex.setStatus("current")
_HpnicfTrafficShapeTable_Object = MibTable
hpnicfTrafficShapeTable = _HpnicfTrafficShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16)
)
if mibBuilder.loadTexts:
    hpnicfTrafficShapeTable.setStatus("current")
_HpnicfTrafficShapeEntry_Object = MibTableRow
hpnicfTrafficShapeEntry = _HpnicfTrafficShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1)
)
hpnicfTrafficShapeEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfTrafficShapeIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfTrafficShapeQueueId"),
)
if mibBuilder.loadTexts:
    hpnicfTrafficShapeEntry.setStatus("current")
_HpnicfTrafficShapeIfIndex_Type = Integer32
_HpnicfTrafficShapeIfIndex_Object = MibTableColumn
hpnicfTrafficShapeIfIndex = _HpnicfTrafficShapeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 1),
    _HpnicfTrafficShapeIfIndex_Type()
)
hpnicfTrafficShapeIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeIfIndex.setStatus("current")


class _HpnicfTrafficShapeQueueId_Type(Integer32):
    """Custom type hpnicfTrafficShapeQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_HpnicfTrafficShapeQueueId_Type.__name__ = "Integer32"
_HpnicfTrafficShapeQueueId_Object = MibTableColumn
hpnicfTrafficShapeQueueId = _HpnicfTrafficShapeQueueId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 2),
    _HpnicfTrafficShapeQueueId_Type()
)
hpnicfTrafficShapeQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeQueueId.setStatus("current")
_HpnicfTrafficShapeMaxRate_Type = Integer32
_HpnicfTrafficShapeMaxRate_Object = MibTableColumn
hpnicfTrafficShapeMaxRate = _HpnicfTrafficShapeMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 3),
    _HpnicfTrafficShapeMaxRate_Type()
)
hpnicfTrafficShapeMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeMaxRate.setStatus("current")
_HpnicfTrafficShapeBurstSize_Type = Integer32
_HpnicfTrafficShapeBurstSize_Object = MibTableColumn
hpnicfTrafficShapeBurstSize = _HpnicfTrafficShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 4),
    _HpnicfTrafficShapeBurstSize_Type()
)
hpnicfTrafficShapeBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeBurstSize.setStatus("current")


class _HpnicfTrafficShapeBufferLimit_Type(Integer32):
    """Custom type hpnicfTrafficShapeBufferLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 8000),
    )


_HpnicfTrafficShapeBufferLimit_Type.__name__ = "Integer32"
_HpnicfTrafficShapeBufferLimit_Object = MibTableColumn
hpnicfTrafficShapeBufferLimit = _HpnicfTrafficShapeBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 5),
    _HpnicfTrafficShapeBufferLimit_Type()
)
hpnicfTrafficShapeBufferLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeBufferLimit.setStatus("current")
_HpnicfTrafficShapeRowStatus_Type = RowStatus
_HpnicfTrafficShapeRowStatus_Object = MibTableColumn
hpnicfTrafficShapeRowStatus = _HpnicfTrafficShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 16, 1, 6),
    _HpnicfTrafficShapeRowStatus_Type()
)
hpnicfTrafficShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrafficShapeRowStatus.setStatus("current")
_HpnicfPortQueueTable_Object = MibTable
hpnicfPortQueueTable = _HpnicfPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17)
)
if mibBuilder.loadTexts:
    hpnicfPortQueueTable.setStatus("current")
_HpnicfPortQueueEntry_Object = MibTableRow
hpnicfPortQueueEntry = _HpnicfPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17, 1)
)
hpnicfPortQueueEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortQueueIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortQueueQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfPortQueueEntry.setStatus("current")
_HpnicfPortQueueIfIndex_Type = Integer32
_HpnicfPortQueueIfIndex_Object = MibTableColumn
hpnicfPortQueueIfIndex = _HpnicfPortQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17, 1, 1),
    _HpnicfPortQueueIfIndex_Type()
)
hpnicfPortQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortQueueIfIndex.setStatus("current")


class _HpnicfPortQueueQueueID_Type(Integer32):
    """Custom type hpnicfPortQueueQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfPortQueueQueueID_Type.__name__ = "Integer32"
_HpnicfPortQueueQueueID_Object = MibTableColumn
hpnicfPortQueueQueueID = _HpnicfPortQueueQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17, 1, 2),
    _HpnicfPortQueueQueueID_Type()
)
hpnicfPortQueueQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortQueueQueueID.setStatus("current")


class _HpnicfPortQueueWrrPriority_Type(Integer32):
    """Custom type hpnicfPortQueueWrrPriority based on Integer32"""
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


_HpnicfPortQueueWrrPriority_Type.__name__ = "Integer32"
_HpnicfPortQueueWrrPriority_Object = MibTableColumn
hpnicfPortQueueWrrPriority = _HpnicfPortQueueWrrPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17, 1, 3),
    _HpnicfPortQueueWrrPriority_Type()
)
hpnicfPortQueueWrrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortQueueWrrPriority.setStatus("current")


class _HpnicfPortQueueWeight_Type(Integer32):
    """Custom type hpnicfPortQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_HpnicfPortQueueWeight_Type.__name__ = "Integer32"
_HpnicfPortQueueWeight_Object = MibTableColumn
hpnicfPortQueueWeight = _HpnicfPortQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 17, 1, 4),
    _HpnicfPortQueueWeight_Type()
)
hpnicfPortQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortQueueWeight.setStatus("current")
_HpnicfDropModeTable_Object = MibTable
hpnicfDropModeTable = _HpnicfDropModeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 18)
)
if mibBuilder.loadTexts:
    hpnicfDropModeTable.setStatus("current")
_HpnicfDropModeEntry_Object = MibTableRow
hpnicfDropModeEntry = _HpnicfDropModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 18, 1)
)
hpnicfDropModeEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDropModeIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDropModeEntry.setStatus("current")
_HpnicfDropModeIfIndex_Type = Integer32
_HpnicfDropModeIfIndex_Object = MibTableColumn
hpnicfDropModeIfIndex = _HpnicfDropModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 18, 1, 1),
    _HpnicfDropModeIfIndex_Type()
)
hpnicfDropModeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDropModeIfIndex.setStatus("current")


class _HpnicfDropModeMode_Type(Integer32):
    """Custom type hpnicfDropModeMode based on Integer32"""
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


_HpnicfDropModeMode_Type.__name__ = "Integer32"
_HpnicfDropModeMode_Object = MibTableColumn
hpnicfDropModeMode = _HpnicfDropModeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 18, 1, 2),
    _HpnicfDropModeMode_Type()
)
hpnicfDropModeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDropModeMode.setStatus("current")


class _HpnicfDropModeWredIndex_Type(Integer32):
    """Custom type hpnicfDropModeWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HpnicfDropModeWredIndex_Type.__name__ = "Integer32"
_HpnicfDropModeWredIndex_Object = MibTableColumn
hpnicfDropModeWredIndex = _HpnicfDropModeWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 18, 1, 3),
    _HpnicfDropModeWredIndex_Type()
)
hpnicfDropModeWredIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDropModeWredIndex.setStatus("current")
_HpnicfWredTable_Object = MibTable
hpnicfWredTable = _HpnicfWredTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19)
)
if mibBuilder.loadTexts:
    hpnicfWredTable.setStatus("current")
_HpnicfWredEntry_Object = MibTableRow
hpnicfWredEntry = _HpnicfWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1)
)
hpnicfWredEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfWredIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfWredQueueId"),
)
if mibBuilder.loadTexts:
    hpnicfWredEntry.setStatus("current")


class _HpnicfWredIndex_Type(Integer32):
    """Custom type hpnicfWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_HpnicfWredIndex_Type.__name__ = "Integer32"
_HpnicfWredIndex_Object = MibTableColumn
hpnicfWredIndex = _HpnicfWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 1),
    _HpnicfWredIndex_Type()
)
hpnicfWredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWredIndex.setStatus("current")


class _HpnicfWredQueueId_Type(Integer32):
    """Custom type hpnicfWredQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfWredQueueId_Type.__name__ = "Integer32"
_HpnicfWredQueueId_Object = MibTableColumn
hpnicfWredQueueId = _HpnicfWredQueueId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 2),
    _HpnicfWredQueueId_Type()
)
hpnicfWredQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfWredQueueId.setStatus("current")


class _HpnicfWredGreenMinThreshold_Type(Integer32):
    """Custom type hpnicfWredGreenMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredGreenMinThreshold_Type.__name__ = "Integer32"
_HpnicfWredGreenMinThreshold_Object = MibTableColumn
hpnicfWredGreenMinThreshold = _HpnicfWredGreenMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 3),
    _HpnicfWredGreenMinThreshold_Type()
)
hpnicfWredGreenMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredGreenMinThreshold.setStatus("current")


class _HpnicfWredGreenMaxThreshold_Type(Integer32):
    """Custom type hpnicfWredGreenMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredGreenMaxThreshold_Type.__name__ = "Integer32"
_HpnicfWredGreenMaxThreshold_Object = MibTableColumn
hpnicfWredGreenMaxThreshold = _HpnicfWredGreenMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 4),
    _HpnicfWredGreenMaxThreshold_Type()
)
hpnicfWredGreenMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredGreenMaxThreshold.setStatus("current")


class _HpnicfWredGreenMaxProb_Type(Integer32):
    """Custom type hpnicfWredGreenMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfWredGreenMaxProb_Type.__name__ = "Integer32"
_HpnicfWredGreenMaxProb_Object = MibTableColumn
hpnicfWredGreenMaxProb = _HpnicfWredGreenMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 5),
    _HpnicfWredGreenMaxProb_Type()
)
hpnicfWredGreenMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredGreenMaxProb.setStatus("current")


class _HpnicfWredYellowMinThreshold_Type(Integer32):
    """Custom type hpnicfWredYellowMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredYellowMinThreshold_Type.__name__ = "Integer32"
_HpnicfWredYellowMinThreshold_Object = MibTableColumn
hpnicfWredYellowMinThreshold = _HpnicfWredYellowMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 6),
    _HpnicfWredYellowMinThreshold_Type()
)
hpnicfWredYellowMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredYellowMinThreshold.setStatus("current")


class _HpnicfWredYellowMaxThreshold_Type(Integer32):
    """Custom type hpnicfWredYellowMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredYellowMaxThreshold_Type.__name__ = "Integer32"
_HpnicfWredYellowMaxThreshold_Object = MibTableColumn
hpnicfWredYellowMaxThreshold = _HpnicfWredYellowMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 7),
    _HpnicfWredYellowMaxThreshold_Type()
)
hpnicfWredYellowMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredYellowMaxThreshold.setStatus("current")


class _HpnicfWredYellowMaxProb_Type(Integer32):
    """Custom type hpnicfWredYellowMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfWredYellowMaxProb_Type.__name__ = "Integer32"
_HpnicfWredYellowMaxProb_Object = MibTableColumn
hpnicfWredYellowMaxProb = _HpnicfWredYellowMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 8),
    _HpnicfWredYellowMaxProb_Type()
)
hpnicfWredYellowMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredYellowMaxProb.setStatus("current")


class _HpnicfWredRedMinThreshold_Type(Integer32):
    """Custom type hpnicfWredRedMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredRedMinThreshold_Type.__name__ = "Integer32"
_HpnicfWredRedMinThreshold_Object = MibTableColumn
hpnicfWredRedMinThreshold = _HpnicfWredRedMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 9),
    _HpnicfWredRedMinThreshold_Type()
)
hpnicfWredRedMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredRedMinThreshold.setStatus("current")


class _HpnicfWredRedMaxThreshold_Type(Integer32):
    """Custom type hpnicfWredRedMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfWredRedMaxThreshold_Type.__name__ = "Integer32"
_HpnicfWredRedMaxThreshold_Object = MibTableColumn
hpnicfWredRedMaxThreshold = _HpnicfWredRedMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 10),
    _HpnicfWredRedMaxThreshold_Type()
)
hpnicfWredRedMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredRedMaxThreshold.setStatus("current")


class _HpnicfWredRedMaxProb_Type(Integer32):
    """Custom type hpnicfWredRedMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfWredRedMaxProb_Type.__name__ = "Integer32"
_HpnicfWredRedMaxProb_Object = MibTableColumn
hpnicfWredRedMaxProb = _HpnicfWredRedMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 11),
    _HpnicfWredRedMaxProb_Type()
)
hpnicfWredRedMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredRedMaxProb.setStatus("current")


class _HpnicfWredExponent_Type(Integer32):
    """Custom type hpnicfWredExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfWredExponent_Type.__name__ = "Integer32"
_HpnicfWredExponent_Object = MibTableColumn
hpnicfWredExponent = _HpnicfWredExponent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 19, 1, 12),
    _HpnicfWredExponent_Type()
)
hpnicfWredExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfWredExponent.setStatus("current")
_HpnicfCosToLocalPrecedenceMapTable_Object = MibTable
hpnicfCosToLocalPrecedenceMapTable = _HpnicfCosToLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 20)
)
if mibBuilder.loadTexts:
    hpnicfCosToLocalPrecedenceMapTable.setStatus("current")
_HpnicfCosToLocalPrecedenceMapEntry_Object = MibTableRow
hpnicfCosToLocalPrecedenceMapEntry = _HpnicfCosToLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 20, 1)
)
hpnicfCosToLocalPrecedenceMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfCosToLocalPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCosToLocalPrecedenceMapEntry.setStatus("current")


class _HpnicfCosToLocalPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hpnicfCosToLocalPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfCosToLocalPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_HpnicfCosToLocalPrecedenceMapCosIndex_Object = MibTableColumn
hpnicfCosToLocalPrecedenceMapCosIndex = _HpnicfCosToLocalPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 20, 1, 1),
    _HpnicfCosToLocalPrecedenceMapCosIndex_Type()
)
hpnicfCosToLocalPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCosToLocalPrecedenceMapCosIndex.setStatus("current")


class _HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type(Integer32):
    """Custom type hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type.__name__ = "Integer32"
_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Object = MibTableColumn
hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue = _HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 20, 1, 2),
    _HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type()
)
hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue.setStatus("current")
_HpnicfCosToDropPrecedenceMapTable_Object = MibTable
hpnicfCosToDropPrecedenceMapTable = _HpnicfCosToDropPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 21)
)
if mibBuilder.loadTexts:
    hpnicfCosToDropPrecedenceMapTable.setStatus("current")
_HpnicfCosToDropPrecedenceMapEntry_Object = MibTableRow
hpnicfCosToDropPrecedenceMapEntry = _HpnicfCosToDropPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 21, 1)
)
hpnicfCosToDropPrecedenceMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfCosToDropPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCosToDropPrecedenceMapEntry.setStatus("current")


class _HpnicfCosToDropPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hpnicfCosToDropPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfCosToDropPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_HpnicfCosToDropPrecedenceMapCosIndex_Object = MibTableColumn
hpnicfCosToDropPrecedenceMapCosIndex = _HpnicfCosToDropPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 21, 1, 1),
    _HpnicfCosToDropPrecedenceMapCosIndex_Type()
)
hpnicfCosToDropPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfCosToDropPrecedenceMapCosIndex.setStatus("current")


class _HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type(Integer32):
    """Custom type hpnicfCosToDropPrecedenceMapDropPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type.__name__ = "Integer32"
_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Object = MibTableColumn
hpnicfCosToDropPrecedenceMapDropPrecedenceValue = _HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 21, 1, 2),
    _HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type()
)
hpnicfCosToDropPrecedenceMapDropPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCosToDropPrecedenceMapDropPrecedenceValue.setStatus("current")
_HpnicfDscpMapTable_Object = MibTable
hpnicfDscpMapTable = _HpnicfDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22)
)
if mibBuilder.loadTexts:
    hpnicfDscpMapTable.setStatus("current")
_HpnicfDscpMapEntry_Object = MibTableRow
hpnicfDscpMapEntry = _HpnicfDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1)
)
hpnicfDscpMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpMapConformLevel"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDscpMapEntry.setStatus("current")


class _HpnicfDscpMapConformLevel_Type(Integer32):
    """Custom type hpnicfDscpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfDscpMapConformLevel_Type.__name__ = "Integer32"
_HpnicfDscpMapConformLevel_Object = MibTableColumn
hpnicfDscpMapConformLevel = _HpnicfDscpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 1),
    _HpnicfDscpMapConformLevel_Type()
)
hpnicfDscpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDscpMapConformLevel.setStatus("current")


class _HpnicfDscpMapDscpIndex_Type(Integer32):
    """Custom type hpnicfDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpMapDscpIndex_Type.__name__ = "Integer32"
_HpnicfDscpMapDscpIndex_Object = MibTableColumn
hpnicfDscpMapDscpIndex = _HpnicfDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 2),
    _HpnicfDscpMapDscpIndex_Type()
)
hpnicfDscpMapDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDscpMapDscpIndex.setStatus("current")


class _HpnicfDscpMapDscpValue_Type(Integer32):
    """Custom type hpnicfDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpMapDscpValue_Type.__name__ = "Integer32"
_HpnicfDscpMapDscpValue_Object = MibTableColumn
hpnicfDscpMapDscpValue = _HpnicfDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 3),
    _HpnicfDscpMapDscpValue_Type()
)
hpnicfDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpMapDscpValue.setStatus("current")


class _HpnicfDscpMapExpValue_Type(Integer32):
    """Custom type hpnicfDscpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDscpMapExpValue_Type.__name__ = "Integer32"
_HpnicfDscpMapExpValue_Object = MibTableColumn
hpnicfDscpMapExpValue = _HpnicfDscpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 4),
    _HpnicfDscpMapExpValue_Type()
)
hpnicfDscpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpMapExpValue.setStatus("current")


class _HpnicfDscpMapCosValue_Type(Integer32):
    """Custom type hpnicfDscpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDscpMapCosValue_Type.__name__ = "Integer32"
_HpnicfDscpMapCosValue_Object = MibTableColumn
hpnicfDscpMapCosValue = _HpnicfDscpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 5),
    _HpnicfDscpMapCosValue_Type()
)
hpnicfDscpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpMapCosValue.setStatus("current")


class _HpnicfDscpMapLocalPrecedence_Type(Integer32):
    """Custom type hpnicfDscpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDscpMapLocalPrecedence_Type.__name__ = "Integer32"
_HpnicfDscpMapLocalPrecedence_Object = MibTableColumn
hpnicfDscpMapLocalPrecedence = _HpnicfDscpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 6),
    _HpnicfDscpMapLocalPrecedence_Type()
)
hpnicfDscpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpMapLocalPrecedence.setStatus("current")


class _HpnicfDscpMapDropPrecedence_Type(Integer32):
    """Custom type hpnicfDscpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfDscpMapDropPrecedence_Type.__name__ = "Integer32"
_HpnicfDscpMapDropPrecedence_Object = MibTableColumn
hpnicfDscpMapDropPrecedence = _HpnicfDscpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 22, 1, 7),
    _HpnicfDscpMapDropPrecedence_Type()
)
hpnicfDscpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpMapDropPrecedence.setStatus("current")
_HpnicfExpMapTable_Object = MibTable
hpnicfExpMapTable = _HpnicfExpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23)
)
if mibBuilder.loadTexts:
    hpnicfExpMapTable.setStatus("current")
_HpnicfExpMapEntry_Object = MibTableRow
hpnicfExpMapEntry = _HpnicfExpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1)
)
hpnicfExpMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfExpMapConformLevel"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfExpMapExpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfExpMapEntry.setStatus("current")


class _HpnicfExpMapConformLevel_Type(Integer32):
    """Custom type hpnicfExpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfExpMapConformLevel_Type.__name__ = "Integer32"
_HpnicfExpMapConformLevel_Object = MibTableColumn
hpnicfExpMapConformLevel = _HpnicfExpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 1),
    _HpnicfExpMapConformLevel_Type()
)
hpnicfExpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfExpMapConformLevel.setStatus("current")


class _HpnicfExpMapExpIndex_Type(Integer32):
    """Custom type hpnicfExpMapExpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfExpMapExpIndex_Type.__name__ = "Integer32"
_HpnicfExpMapExpIndex_Object = MibTableColumn
hpnicfExpMapExpIndex = _HpnicfExpMapExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 2),
    _HpnicfExpMapExpIndex_Type()
)
hpnicfExpMapExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfExpMapExpIndex.setStatus("current")


class _HpnicfExpMapDscpValue_Type(Integer32):
    """Custom type hpnicfExpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfExpMapDscpValue_Type.__name__ = "Integer32"
_HpnicfExpMapDscpValue_Object = MibTableColumn
hpnicfExpMapDscpValue = _HpnicfExpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 3),
    _HpnicfExpMapDscpValue_Type()
)
hpnicfExpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpMapDscpValue.setStatus("current")


class _HpnicfExpMapExpValue_Type(Integer32):
    """Custom type hpnicfExpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfExpMapExpValue_Type.__name__ = "Integer32"
_HpnicfExpMapExpValue_Object = MibTableColumn
hpnicfExpMapExpValue = _HpnicfExpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 4),
    _HpnicfExpMapExpValue_Type()
)
hpnicfExpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpMapExpValue.setStatus("current")


class _HpnicfExpMapCosValue_Type(Integer32):
    """Custom type hpnicfExpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfExpMapCosValue_Type.__name__ = "Integer32"
_HpnicfExpMapCosValue_Object = MibTableColumn
hpnicfExpMapCosValue = _HpnicfExpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 5),
    _HpnicfExpMapCosValue_Type()
)
hpnicfExpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpMapCosValue.setStatus("current")


class _HpnicfExpMapLocalPrecedence_Type(Integer32):
    """Custom type hpnicfExpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfExpMapLocalPrecedence_Type.__name__ = "Integer32"
_HpnicfExpMapLocalPrecedence_Object = MibTableColumn
hpnicfExpMapLocalPrecedence = _HpnicfExpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 6),
    _HpnicfExpMapLocalPrecedence_Type()
)
hpnicfExpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpMapLocalPrecedence.setStatus("current")


class _HpnicfExpMapDropPrecedence_Type(Integer32):
    """Custom type hpnicfExpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfExpMapDropPrecedence_Type.__name__ = "Integer32"
_HpnicfExpMapDropPrecedence_Object = MibTableColumn
hpnicfExpMapDropPrecedence = _HpnicfExpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 23, 1, 7),
    _HpnicfExpMapDropPrecedence_Type()
)
hpnicfExpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfExpMapDropPrecedence.setStatus("current")
_HpnicfLocalPrecedenceMapTable_Object = MibTable
hpnicfLocalPrecedenceMapTable = _HpnicfLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 24)
)
if mibBuilder.loadTexts:
    hpnicfLocalPrecedenceMapTable.setStatus("current")
_HpnicfLocalPrecedenceMapEntry_Object = MibTableRow
hpnicfLocalPrecedenceMapEntry = _HpnicfLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 24, 1)
)
hpnicfLocalPrecedenceMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfLocalPrecedenceMapConformLevel"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfLocalPrecedenceMapLocalPrecedenceIndex"),
)
if mibBuilder.loadTexts:
    hpnicfLocalPrecedenceMapEntry.setStatus("current")


class _HpnicfLocalPrecedenceMapConformLevel_Type(Integer32):
    """Custom type hpnicfLocalPrecedenceMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfLocalPrecedenceMapConformLevel_Type.__name__ = "Integer32"
_HpnicfLocalPrecedenceMapConformLevel_Object = MibTableColumn
hpnicfLocalPrecedenceMapConformLevel = _HpnicfLocalPrecedenceMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 24, 1, 1),
    _HpnicfLocalPrecedenceMapConformLevel_Type()
)
hpnicfLocalPrecedenceMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfLocalPrecedenceMapConformLevel.setStatus("current")


class _HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type(Integer32):
    """Custom type hpnicfLocalPrecedenceMapLocalPrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type.__name__ = "Integer32"
_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Object = MibTableColumn
hpnicfLocalPrecedenceMapLocalPrecedenceIndex = _HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 24, 1, 2),
    _HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type()
)
hpnicfLocalPrecedenceMapLocalPrecedenceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLocalPrecedenceMapLocalPrecedenceIndex.setStatus("current")


class _HpnicfLocalPrecedenceMapCosValue_Type(Integer32):
    """Custom type hpnicfLocalPrecedenceMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfLocalPrecedenceMapCosValue_Type.__name__ = "Integer32"
_HpnicfLocalPrecedenceMapCosValue_Object = MibTableColumn
hpnicfLocalPrecedenceMapCosValue = _HpnicfLocalPrecedenceMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 24, 1, 3),
    _HpnicfLocalPrecedenceMapCosValue_Type()
)
hpnicfLocalPrecedenceMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfLocalPrecedenceMapCosValue.setStatus("current")
_HpnicfPortWredTable_Object = MibTable
hpnicfPortWredTable = _HpnicfPortWredTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25)
)
if mibBuilder.loadTexts:
    hpnicfPortWredTable.setStatus("current")
_HpnicfPortWredEntry_Object = MibTableRow
hpnicfPortWredEntry = _HpnicfPortWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25, 1)
)
hpnicfPortWredEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortWredIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortWredQueueID"),
)
if mibBuilder.loadTexts:
    hpnicfPortWredEntry.setStatus("current")
_HpnicfPortWredIfIndex_Type = Integer32
_HpnicfPortWredIfIndex_Object = MibTableColumn
hpnicfPortWredIfIndex = _HpnicfPortWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25, 1, 1),
    _HpnicfPortWredIfIndex_Type()
)
hpnicfPortWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortWredIfIndex.setStatus("current")


class _HpnicfPortWredQueueID_Type(Integer32):
    """Custom type hpnicfPortWredQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfPortWredQueueID_Type.__name__ = "Integer32"
_HpnicfPortWredQueueID_Object = MibTableColumn
hpnicfPortWredQueueID = _HpnicfPortWredQueueID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25, 1, 2),
    _HpnicfPortWredQueueID_Type()
)
hpnicfPortWredQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPortWredQueueID.setStatus("current")


class _HpnicfPortWredQueueStartLength_Type(Integer32):
    """Custom type hpnicfPortWredQueueStartLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HpnicfPortWredQueueStartLength_Type.__name__ = "Integer32"
_HpnicfPortWredQueueStartLength_Object = MibTableColumn
hpnicfPortWredQueueStartLength = _HpnicfPortWredQueueStartLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25, 1, 3),
    _HpnicfPortWredQueueStartLength_Type()
)
hpnicfPortWredQueueStartLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortWredQueueStartLength.setStatus("current")


class _HpnicfPortWredQueueProbability_Type(Integer32):
    """Custom type hpnicfPortWredQueueProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfPortWredQueueProbability_Type.__name__ = "Integer32"
_HpnicfPortWredQueueProbability_Object = MibTableColumn
hpnicfPortWredQueueProbability = _HpnicfPortWredQueueProbability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 25, 1, 4),
    _HpnicfPortWredQueueProbability_Type()
)
hpnicfPortWredQueueProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortWredQueueProbability.setStatus("current")
_HpnicfMirroringGroupTable_Object = MibTable
hpnicfMirroringGroupTable = _HpnicfMirroringGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupTable.setStatus("current")
_HpnicfMirroringGroupEntry_Object = MibTableRow
hpnicfMirroringGroupEntry = _HpnicfMirroringGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26, 1)
)
hpnicfMirroringGroupEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupEntry.setStatus("current")


class _HpnicfMirroringGroupID_Type(Integer32):
    """Custom type hpnicfMirroringGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HpnicfMirroringGroupID_Type.__name__ = "Integer32"
_HpnicfMirroringGroupID_Object = MibTableColumn
hpnicfMirroringGroupID = _HpnicfMirroringGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26, 1, 1),
    _HpnicfMirroringGroupID_Type()
)
hpnicfMirroringGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupID.setStatus("current")


class _HpnicfMirroringGroupType_Type(Integer32):
    """Custom type hpnicfMirroringGroupType based on Integer32"""
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


_HpnicfMirroringGroupType_Type.__name__ = "Integer32"
_HpnicfMirroringGroupType_Object = MibTableColumn
hpnicfMirroringGroupType = _HpnicfMirroringGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26, 1, 2),
    _HpnicfMirroringGroupType_Type()
)
hpnicfMirroringGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupType.setStatus("current")


class _HpnicfMirroringGroupStatus_Type(Integer32):
    """Custom type hpnicfMirroringGroupStatus based on Integer32"""
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


_HpnicfMirroringGroupStatus_Type.__name__ = "Integer32"
_HpnicfMirroringGroupStatus_Object = MibTableColumn
hpnicfMirroringGroupStatus = _HpnicfMirroringGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26, 1, 3),
    _HpnicfMirroringGroupStatus_Type()
)
hpnicfMirroringGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupStatus.setStatus("current")
_HpnicfMirroringGroupRowStatus_Type = RowStatus
_HpnicfMirroringGroupRowStatus_Object = MibTableColumn
hpnicfMirroringGroupRowStatus = _HpnicfMirroringGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 26, 1, 4),
    _HpnicfMirroringGroupRowStatus_Type()
)
hpnicfMirroringGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupRowStatus.setStatus("current")
_HpnicfMirroringGroupMirrorTable_Object = MibTable
hpnicfMirroringGroupMirrorTable = _HpnicfMirroringGroupMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorTable.setStatus("current")
_HpnicfMirroringGroupMirrorEntry_Object = MibTableRow
hpnicfMirroringGroupMirrorEntry = _HpnicfMirroringGroupMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1)
)
hpnicfMirroringGroupMirrorEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorEntry.setStatus("current")
_HpnicfMirroringGroupMirrorInboundIfIndexList_Type = OctetString
_HpnicfMirroringGroupMirrorInboundIfIndexList_Object = MibTableColumn
hpnicfMirroringGroupMirrorInboundIfIndexList = _HpnicfMirroringGroupMirrorInboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1, 1),
    _HpnicfMirroringGroupMirrorInboundIfIndexList_Type()
)
hpnicfMirroringGroupMirrorInboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorInboundIfIndexList.setStatus("current")
_HpnicfMirroringGroupMirrorOutboundIfIndexList_Type = OctetString
_HpnicfMirroringGroupMirrorOutboundIfIndexList_Object = MibTableColumn
hpnicfMirroringGroupMirrorOutboundIfIndexList = _HpnicfMirroringGroupMirrorOutboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1, 2),
    _HpnicfMirroringGroupMirrorOutboundIfIndexList_Type()
)
hpnicfMirroringGroupMirrorOutboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorOutboundIfIndexList.setStatus("current")
_HpnicfMirroringGroupMirrorRowStatus_Type = RowStatus
_HpnicfMirroringGroupMirrorRowStatus_Object = MibTableColumn
hpnicfMirroringGroupMirrorRowStatus = _HpnicfMirroringGroupMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1, 3),
    _HpnicfMirroringGroupMirrorRowStatus_Type()
)
hpnicfMirroringGroupMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorRowStatus.setStatus("current")
_HpnicfMirroringGroupMirrorInTypeList_Type = OctetString
_HpnicfMirroringGroupMirrorInTypeList_Object = MibTableColumn
hpnicfMirroringGroupMirrorInTypeList = _HpnicfMirroringGroupMirrorInTypeList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1, 4),
    _HpnicfMirroringGroupMirrorInTypeList_Type()
)
hpnicfMirroringGroupMirrorInTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorInTypeList.setStatus("current")
_HpnicfMirroringGroupMirrorOutTypeList_Type = OctetString
_HpnicfMirroringGroupMirrorOutTypeList_Object = MibTableColumn
hpnicfMirroringGroupMirrorOutTypeList = _HpnicfMirroringGroupMirrorOutTypeList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 27, 1, 5),
    _HpnicfMirroringGroupMirrorOutTypeList_Type()
)
hpnicfMirroringGroupMirrorOutTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorOutTypeList.setStatus("current")
_HpnicfMirroringGroupMonitorTable_Object = MibTable
hpnicfMirroringGroupMonitorTable = _HpnicfMirroringGroupMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 28)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMonitorTable.setStatus("current")
_HpnicfMirroringGroupMonitorEntry_Object = MibTableRow
hpnicfMirroringGroupMonitorEntry = _HpnicfMirroringGroupMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 28, 1)
)
hpnicfMirroringGroupMonitorEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMonitorEntry.setStatus("current")
_HpnicfMirroringGroupMonitorIfIndex_Type = Integer32
_HpnicfMirroringGroupMonitorIfIndex_Object = MibTableColumn
hpnicfMirroringGroupMonitorIfIndex = _HpnicfMirroringGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 28, 1, 1),
    _HpnicfMirroringGroupMonitorIfIndex_Type()
)
hpnicfMirroringGroupMonitorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMonitorIfIndex.setStatus("current")
_HpnicfMirroringGroupMonitorRowStatus_Type = RowStatus
_HpnicfMirroringGroupMonitorRowStatus_Object = MibTableColumn
hpnicfMirroringGroupMonitorRowStatus = _HpnicfMirroringGroupMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 28, 1, 2),
    _HpnicfMirroringGroupMonitorRowStatus_Type()
)
hpnicfMirroringGroupMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMonitorRowStatus.setStatus("current")
_HpnicfMirroringGroupMonitorType_Type = HpnicfMirrorOrMonitorType
_HpnicfMirroringGroupMonitorType_Object = MibTableColumn
hpnicfMirroringGroupMonitorType = _HpnicfMirroringGroupMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 28, 1, 3),
    _HpnicfMirroringGroupMonitorType_Type()
)
hpnicfMirroringGroupMonitorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMonitorType.setStatus("current")
_HpnicfMirroringGroupReflectorTable_Object = MibTable
hpnicfMirroringGroupReflectorTable = _HpnicfMirroringGroupReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 29)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupReflectorTable.setStatus("current")
_HpnicfMirroringGroupReflectorEntry_Object = MibTableRow
hpnicfMirroringGroupReflectorEntry = _HpnicfMirroringGroupReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 29, 1)
)
hpnicfMirroringGroupReflectorEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupReflectorEntry.setStatus("current")
_HpnicfMirroringGroupReflectorIfIndex_Type = Integer32
_HpnicfMirroringGroupReflectorIfIndex_Object = MibTableColumn
hpnicfMirroringGroupReflectorIfIndex = _HpnicfMirroringGroupReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 29, 1, 1),
    _HpnicfMirroringGroupReflectorIfIndex_Type()
)
hpnicfMirroringGroupReflectorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupReflectorIfIndex.setStatus("current")
_HpnicfMirroringGroupReflectorRowStatus_Type = RowStatus
_HpnicfMirroringGroupReflectorRowStatus_Object = MibTableColumn
hpnicfMirroringGroupReflectorRowStatus = _HpnicfMirroringGroupReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 29, 1, 2),
    _HpnicfMirroringGroupReflectorRowStatus_Type()
)
hpnicfMirroringGroupReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupReflectorRowStatus.setStatus("current")
_HpnicfMirroringGroupRprobeVlanTable_Object = MibTable
hpnicfMirroringGroupRprobeVlanTable = _HpnicfMirroringGroupRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 30)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupRprobeVlanTable.setStatus("current")
_HpnicfMirroringGroupRprobeVlanEntry_Object = MibTableRow
hpnicfMirroringGroupRprobeVlanEntry = _HpnicfMirroringGroupRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 30, 1)
)
hpnicfMirroringGroupRprobeVlanEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupRprobeVlanEntry.setStatus("current")


class _HpnicfMirroringGroupRprobeVlanID_Type(Integer32):
    """Custom type hpnicfMirroringGroupRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfMirroringGroupRprobeVlanID_Type.__name__ = "Integer32"
_HpnicfMirroringGroupRprobeVlanID_Object = MibTableColumn
hpnicfMirroringGroupRprobeVlanID = _HpnicfMirroringGroupRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 30, 1, 1),
    _HpnicfMirroringGroupRprobeVlanID_Type()
)
hpnicfMirroringGroupRprobeVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupRprobeVlanID.setStatus("current")
_HpnicfMirroringGroupRprobeVlanRowStatus_Type = RowStatus
_HpnicfMirroringGroupRprobeVlanRowStatus_Object = MibTableColumn
hpnicfMirroringGroupRprobeVlanRowStatus = _HpnicfMirroringGroupRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 30, 1, 2),
    _HpnicfMirroringGroupRprobeVlanRowStatus_Type()
)
hpnicfMirroringGroupRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupRprobeVlanRowStatus.setStatus("current")
_HpnicfMirroringGroupMirrorMacTable_Object = MibTable
hpnicfMirroringGroupMirrorMacTable = _HpnicfMirroringGroupMirrorMacTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorMacTable.setStatus("current")
_HpnicfMirroringGroupMirrorMacEntry_Object = MibTableRow
hpnicfMirroringGroupMirrorMacEntry = _HpnicfMirroringGroupMirrorMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31, 1)
)
hpnicfMirroringGroupMirrorMacEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupMirrorMacSeq"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorMacEntry.setStatus("current")
_HpnicfMirroringGroupMirrorMacSeq_Type = Integer32
_HpnicfMirroringGroupMirrorMacSeq_Object = MibTableColumn
hpnicfMirroringGroupMirrorMacSeq = _HpnicfMirroringGroupMirrorMacSeq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31, 1, 1),
    _HpnicfMirroringGroupMirrorMacSeq_Type()
)
hpnicfMirroringGroupMirrorMacSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorMacSeq.setStatus("current")
_HpnicfMirroringGroupMirrorMac_Type = MacAddress
_HpnicfMirroringGroupMirrorMac_Object = MibTableColumn
hpnicfMirroringGroupMirrorMac = _HpnicfMirroringGroupMirrorMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31, 1, 2),
    _HpnicfMirroringGroupMirrorMac_Type()
)
hpnicfMirroringGroupMirrorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorMac.setStatus("current")


class _HpnicfMirrorMacVlanID_Type(Integer32):
    """Custom type hpnicfMirrorMacVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfMirrorMacVlanID_Type.__name__ = "Integer32"
_HpnicfMirrorMacVlanID_Object = MibTableColumn
hpnicfMirrorMacVlanID = _HpnicfMirrorMacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31, 1, 3),
    _HpnicfMirrorMacVlanID_Type()
)
hpnicfMirrorMacVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirrorMacVlanID.setStatus("current")
_HpnicfMirroringGroupMirroMacStatus_Type = RowStatus
_HpnicfMirroringGroupMirroMacStatus_Object = MibTableColumn
hpnicfMirroringGroupMirroMacStatus = _HpnicfMirroringGroupMirroMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 31, 1, 4),
    _HpnicfMirroringGroupMirroMacStatus_Type()
)
hpnicfMirroringGroupMirroMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirroMacStatus.setStatus("current")
_HpnicfMirroringGroupMirrorVlanTable_Object = MibTable
hpnicfMirroringGroupMirrorVlanTable = _HpnicfMirroringGroupMirrorVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32)
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorVlanTable.setStatus("current")
_HpnicfMirroringGroupMirrorVlanEntry_Object = MibTableRow
hpnicfMirroringGroupMirrorVlanEntry = _HpnicfMirroringGroupMirrorVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32, 1)
)
hpnicfMirroringGroupMirrorVlanEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfMirroringGroupMirrorVlanSeq"),
)
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorVlanEntry.setStatus("current")
_HpnicfMirroringGroupMirrorVlanSeq_Type = Integer32
_HpnicfMirroringGroupMirrorVlanSeq_Object = MibTableColumn
hpnicfMirroringGroupMirrorVlanSeq = _HpnicfMirroringGroupMirrorVlanSeq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32, 1, 1),
    _HpnicfMirroringGroupMirrorVlanSeq_Type()
)
hpnicfMirroringGroupMirrorVlanSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorVlanSeq.setStatus("current")


class _HpnicfMirroringGroupMirrorVlanID_Type(Integer32):
    """Custom type hpnicfMirroringGroupMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfMirroringGroupMirrorVlanID_Type.__name__ = "Integer32"
_HpnicfMirroringGroupMirrorVlanID_Object = MibTableColumn
hpnicfMirroringGroupMirrorVlanID = _HpnicfMirroringGroupMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32, 1, 2),
    _HpnicfMirroringGroupMirrorVlanID_Type()
)
hpnicfMirroringGroupMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorVlanID.setStatus("current")


class _HpnicfMirroringGroupMirrorVlanDirection_Type(Integer32):
    """Custom type hpnicfMirroringGroupMirrorVlanDirection based on Integer32"""
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


_HpnicfMirroringGroupMirrorVlanDirection_Type.__name__ = "Integer32"
_HpnicfMirroringGroupMirrorVlanDirection_Object = MibTableColumn
hpnicfMirroringGroupMirrorVlanDirection = _HpnicfMirroringGroupMirrorVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32, 1, 3),
    _HpnicfMirroringGroupMirrorVlanDirection_Type()
)
hpnicfMirroringGroupMirrorVlanDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirrorVlanDirection.setStatus("current")
_HpnicfMirroringGroupMirroVlanStatus_Type = RowStatus
_HpnicfMirroringGroupMirroVlanStatus_Object = MibTableColumn
hpnicfMirroringGroupMirroVlanStatus = _HpnicfMirroringGroupMirroVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 32, 1, 4),
    _HpnicfMirroringGroupMirroVlanStatus_Type()
)
hpnicfMirroringGroupMirroVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMirroringGroupMirroVlanStatus.setStatus("current")
_HpnicfPortTrustTable_Object = MibTable
hpnicfPortTrustTable = _HpnicfPortTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33)
)
if mibBuilder.loadTexts:
    hpnicfPortTrustTable.setStatus("current")
_HpnicfPortTrustEntry_Object = MibTableRow
hpnicfPortTrustEntry = _HpnicfPortTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33, 1)
)
hpnicfPortTrustEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfPortTrustIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortTrustEntry.setStatus("current")
_HpnicfPortTrustIfIndex_Type = Integer32
_HpnicfPortTrustIfIndex_Object = MibTableColumn
hpnicfPortTrustIfIndex = _HpnicfPortTrustIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33, 1, 1),
    _HpnicfPortTrustIfIndex_Type()
)
hpnicfPortTrustIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortTrustIfIndex.setStatus("current")


class _HpnicfPortTrustTrustType_Type(Integer32):
    """Custom type hpnicfPortTrustTrustType based on Integer32"""
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


_HpnicfPortTrustTrustType_Type.__name__ = "Integer32"
_HpnicfPortTrustTrustType_Object = MibTableColumn
hpnicfPortTrustTrustType = _HpnicfPortTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33, 1, 2),
    _HpnicfPortTrustTrustType_Type()
)
hpnicfPortTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortTrustTrustType.setStatus("current")


class _HpnicfPortTrustOvercastType_Type(Integer32):
    """Custom type hpnicfPortTrustOvercastType based on Integer32"""
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


_HpnicfPortTrustOvercastType_Type.__name__ = "Integer32"
_HpnicfPortTrustOvercastType_Object = MibTableColumn
hpnicfPortTrustOvercastType = _HpnicfPortTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33, 1, 3),
    _HpnicfPortTrustOvercastType_Type()
)
hpnicfPortTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortTrustOvercastType.setStatus("current")


class _HpnicfPortTrustReset_Type(Integer32):
    """Custom type hpnicfPortTrustReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfPortTrustReset_Type.__name__ = "Integer32"
_HpnicfPortTrustReset_Object = MibTableColumn
hpnicfPortTrustReset = _HpnicfPortTrustReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 33, 1, 4),
    _HpnicfPortTrustReset_Type()
)
hpnicfPortTrustReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPortTrustReset.setStatus("current")
_HpnicfRemarkVlanIDTable_Object = MibTable
hpnicfRemarkVlanIDTable = _HpnicfRemarkVlanIDTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34)
)
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDTable.setStatus("current")
_HpnicfRemarkVlanIDEntry_Object = MibTableRow
hpnicfRemarkVlanIDEntry = _HpnicfRemarkVlanIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1)
)
hpnicfRemarkVlanIDEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRemarkVlanIDAclIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRemarkVlanIDIfIndex"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRemarkVlanIDVlanID"),
    (0, "HPN-ICF-LswQos-MIB", "hpnicfRemarkVlanIDDirection"),
)
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDEntry.setStatus("current")


class _HpnicfRemarkVlanIDAclIndex_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_HpnicfRemarkVlanIDAclIndex_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDAclIndex_Object = MibTableColumn
hpnicfRemarkVlanIDAclIndex = _HpnicfRemarkVlanIDAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 1),
    _HpnicfRemarkVlanIDAclIndex_Type()
)
hpnicfRemarkVlanIDAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDAclIndex.setStatus("current")
_HpnicfRemarkVlanIDIfIndex_Type = Integer32
_HpnicfRemarkVlanIDIfIndex_Object = MibTableColumn
hpnicfRemarkVlanIDIfIndex = _HpnicfRemarkVlanIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 2),
    _HpnicfRemarkVlanIDIfIndex_Type()
)
hpnicfRemarkVlanIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDIfIndex.setStatus("current")


class _HpnicfRemarkVlanIDVlanID_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRemarkVlanIDVlanID_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDVlanID_Object = MibTableColumn
hpnicfRemarkVlanIDVlanID = _HpnicfRemarkVlanIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 3),
    _HpnicfRemarkVlanIDVlanID_Type()
)
hpnicfRemarkVlanIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDVlanID.setStatus("current")


class _HpnicfRemarkVlanIDDirection_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDDirection based on Integer32"""
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


_HpnicfRemarkVlanIDDirection_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDDirection_Object = MibTableColumn
hpnicfRemarkVlanIDDirection = _HpnicfRemarkVlanIDDirection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 4),
    _HpnicfRemarkVlanIDDirection_Type()
)
hpnicfRemarkVlanIDDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDDirection.setStatus("current")


class _HpnicfRemarkVlanIDUserAclNum_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRemarkVlanIDUserAclNum_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDUserAclNum_Object = MibTableColumn
hpnicfRemarkVlanIDUserAclNum = _HpnicfRemarkVlanIDUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 5),
    _HpnicfRemarkVlanIDUserAclNum_Type()
)
hpnicfRemarkVlanIDUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDUserAclNum.setStatus("current")


class _HpnicfRemarkVlanIDUserAclRule_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRemarkVlanIDUserAclRule_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDUserAclRule_Object = MibTableColumn
hpnicfRemarkVlanIDUserAclRule = _HpnicfRemarkVlanIDUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 6),
    _HpnicfRemarkVlanIDUserAclRule_Type()
)
hpnicfRemarkVlanIDUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDUserAclRule.setStatus("current")


class _HpnicfRemarkVlanIDIpAclNum_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRemarkVlanIDIpAclNum_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDIpAclNum_Object = MibTableColumn
hpnicfRemarkVlanIDIpAclNum = _HpnicfRemarkVlanIDIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 7),
    _HpnicfRemarkVlanIDIpAclNum_Type()
)
hpnicfRemarkVlanIDIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDIpAclNum.setStatus("current")


class _HpnicfRemarkVlanIDIpAclRule_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRemarkVlanIDIpAclRule_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDIpAclRule_Object = MibTableColumn
hpnicfRemarkVlanIDIpAclRule = _HpnicfRemarkVlanIDIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 8),
    _HpnicfRemarkVlanIDIpAclRule_Type()
)
hpnicfRemarkVlanIDIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDIpAclRule.setStatus("current")


class _HpnicfRemarkVlanIDLinkAclNum_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_HpnicfRemarkVlanIDLinkAclNum_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDLinkAclNum_Object = MibTableColumn
hpnicfRemarkVlanIDLinkAclNum = _HpnicfRemarkVlanIDLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 9),
    _HpnicfRemarkVlanIDLinkAclNum_Type()
)
hpnicfRemarkVlanIDLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDLinkAclNum.setStatus("current")


class _HpnicfRemarkVlanIDLinkAclRule_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRemarkVlanIDLinkAclRule_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDLinkAclRule_Object = MibTableColumn
hpnicfRemarkVlanIDLinkAclRule = _HpnicfRemarkVlanIDLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 10),
    _HpnicfRemarkVlanIDLinkAclRule_Type()
)
hpnicfRemarkVlanIDLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDLinkAclRule.setStatus("current")


class _HpnicfRemarkVlanIDRemarkVlanID_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDRemarkVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfRemarkVlanIDRemarkVlanID_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDRemarkVlanID_Object = MibTableColumn
hpnicfRemarkVlanIDRemarkVlanID = _HpnicfRemarkVlanIDRemarkVlanID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 11),
    _HpnicfRemarkVlanIDRemarkVlanID_Type()
)
hpnicfRemarkVlanIDRemarkVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDRemarkVlanID.setStatus("current")


class _HpnicfRemarkVlanIDPacketType_Type(Integer32):
    """Custom type hpnicfRemarkVlanIDPacketType based on Integer32"""
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


_HpnicfRemarkVlanIDPacketType_Type.__name__ = "Integer32"
_HpnicfRemarkVlanIDPacketType_Object = MibTableColumn
hpnicfRemarkVlanIDPacketType = _HpnicfRemarkVlanIDPacketType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 12),
    _HpnicfRemarkVlanIDPacketType_Type()
)
hpnicfRemarkVlanIDPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDPacketType.setStatus("current")
_HpnicfRemarkVlanIDRowStatus_Type = RowStatus
_HpnicfRemarkVlanIDRowStatus_Object = MibTableColumn
hpnicfRemarkVlanIDRowStatus = _HpnicfRemarkVlanIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 34, 1, 13),
    _HpnicfRemarkVlanIDRowStatus_Type()
)
hpnicfRemarkVlanIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRemarkVlanIDRowStatus.setStatus("current")
_HpnicfCosToDscpMapTable_Object = MibTable
hpnicfCosToDscpMapTable = _HpnicfCosToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 35)
)
if mibBuilder.loadTexts:
    hpnicfCosToDscpMapTable.setStatus("current")
_HpnicfCosToDscpMapEntry_Object = MibTableRow
hpnicfCosToDscpMapEntry = _HpnicfCosToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 35, 1)
)
hpnicfCosToDscpMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfCosToDscpMapCosIndex"),
)
if mibBuilder.loadTexts:
    hpnicfCosToDscpMapEntry.setStatus("current")


class _HpnicfCosToDscpMapCosIndex_Type(Integer32):
    """Custom type hpnicfCosToDscpMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfCosToDscpMapCosIndex_Type.__name__ = "Integer32"
_HpnicfCosToDscpMapCosIndex_Object = MibTableColumn
hpnicfCosToDscpMapCosIndex = _HpnicfCosToDscpMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 35, 1, 1),
    _HpnicfCosToDscpMapCosIndex_Type()
)
hpnicfCosToDscpMapCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfCosToDscpMapCosIndex.setStatus("current")


class _HpnicfCosToDscpMapDscpValue_Type(Integer32):
    """Custom type hpnicfCosToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfCosToDscpMapDscpValue_Type.__name__ = "Integer32"
_HpnicfCosToDscpMapDscpValue_Object = MibTableColumn
hpnicfCosToDscpMapDscpValue = _HpnicfCosToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 35, 1, 2),
    _HpnicfCosToDscpMapDscpValue_Type()
)
hpnicfCosToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCosToDscpMapDscpValue.setStatus("current")


class _HpnicfCosToDscpMapReSet_Type(Integer32):
    """Custom type hpnicfCosToDscpMapReSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfCosToDscpMapReSet_Type.__name__ = "Integer32"
_HpnicfCosToDscpMapReSet_Object = MibTableColumn
hpnicfCosToDscpMapReSet = _HpnicfCosToDscpMapReSet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 35, 1, 3),
    _HpnicfCosToDscpMapReSet_Type()
)
hpnicfCosToDscpMapReSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfCosToDscpMapReSet.setStatus("current")
_HpnicfDscpToLocalPreMapTable_Object = MibTable
hpnicfDscpToLocalPreMapTable = _HpnicfDscpToLocalPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 36)
)
if mibBuilder.loadTexts:
    hpnicfDscpToLocalPreMapTable.setStatus("current")
_HpnicfDscpToLocalPreMapEntry_Object = MibTableRow
hpnicfDscpToLocalPreMapEntry = _HpnicfDscpToLocalPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 36, 1)
)
hpnicfDscpToLocalPreMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpToLocalPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDscpToLocalPreMapEntry.setStatus("current")


class _HpnicfDscpToLocalPreMapDscpIndex_Type(Integer32):
    """Custom type hpnicfDscpToLocalPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpToLocalPreMapDscpIndex_Type.__name__ = "Integer32"
_HpnicfDscpToLocalPreMapDscpIndex_Object = MibTableColumn
hpnicfDscpToLocalPreMapDscpIndex = _HpnicfDscpToLocalPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 36, 1, 1),
    _HpnicfDscpToLocalPreMapDscpIndex_Type()
)
hpnicfDscpToLocalPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDscpToLocalPreMapDscpIndex.setStatus("current")


class _HpnicfDscpToLocalPreMapLocalPreVal_Type(Integer32):
    """Custom type hpnicfDscpToLocalPreMapLocalPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDscpToLocalPreMapLocalPreVal_Type.__name__ = "Integer32"
_HpnicfDscpToLocalPreMapLocalPreVal_Object = MibTableColumn
hpnicfDscpToLocalPreMapLocalPreVal = _HpnicfDscpToLocalPreMapLocalPreVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 36, 1, 2),
    _HpnicfDscpToLocalPreMapLocalPreVal_Type()
)
hpnicfDscpToLocalPreMapLocalPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToLocalPreMapLocalPreVal.setStatus("current")


class _HpnicfDscpToLocalPreMapReset_Type(Integer32):
    """Custom type hpnicfDscpToLocalPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDscpToLocalPreMapReset_Type.__name__ = "Integer32"
_HpnicfDscpToLocalPreMapReset_Object = MibTableColumn
hpnicfDscpToLocalPreMapReset = _HpnicfDscpToLocalPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 36, 1, 3),
    _HpnicfDscpToLocalPreMapReset_Type()
)
hpnicfDscpToLocalPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToLocalPreMapReset.setStatus("current")
_HpnicfDscpToDropPreMapTable_Object = MibTable
hpnicfDscpToDropPreMapTable = _HpnicfDscpToDropPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 37)
)
if mibBuilder.loadTexts:
    hpnicfDscpToDropPreMapTable.setStatus("current")
_HpnicfDscpToDropPreMapEntry_Object = MibTableRow
hpnicfDscpToDropPreMapEntry = _HpnicfDscpToDropPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 37, 1)
)
hpnicfDscpToDropPreMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpToDropPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDscpToDropPreMapEntry.setStatus("current")


class _HpnicfDscpToDropPreMapDscpIndex_Type(Integer32):
    """Custom type hpnicfDscpToDropPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpToDropPreMapDscpIndex_Type.__name__ = "Integer32"
_HpnicfDscpToDropPreMapDscpIndex_Object = MibTableColumn
hpnicfDscpToDropPreMapDscpIndex = _HpnicfDscpToDropPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 37, 1, 1),
    _HpnicfDscpToDropPreMapDscpIndex_Type()
)
hpnicfDscpToDropPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDscpToDropPreMapDscpIndex.setStatus("current")


class _HpnicfDscpToDropPreMapDropPreVal_Type(Integer32):
    """Custom type hpnicfDscpToDropPreMapDropPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HpnicfDscpToDropPreMapDropPreVal_Type.__name__ = "Integer32"
_HpnicfDscpToDropPreMapDropPreVal_Object = MibTableColumn
hpnicfDscpToDropPreMapDropPreVal = _HpnicfDscpToDropPreMapDropPreVal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 37, 1, 2),
    _HpnicfDscpToDropPreMapDropPreVal_Type()
)
hpnicfDscpToDropPreMapDropPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToDropPreMapDropPreVal.setStatus("current")


class _HpnicfDscpToDropPreMapReset_Type(Integer32):
    """Custom type hpnicfDscpToDropPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDscpToDropPreMapReset_Type.__name__ = "Integer32"
_HpnicfDscpToDropPreMapReset_Object = MibTableColumn
hpnicfDscpToDropPreMapReset = _HpnicfDscpToDropPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 37, 1, 3),
    _HpnicfDscpToDropPreMapReset_Type()
)
hpnicfDscpToDropPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToDropPreMapReset.setStatus("current")
_HpnicfDscpToCosMapTable_Object = MibTable
hpnicfDscpToCosMapTable = _HpnicfDscpToCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 38)
)
if mibBuilder.loadTexts:
    hpnicfDscpToCosMapTable.setStatus("current")
_HpnicfDscpToCosMapEntry_Object = MibTableRow
hpnicfDscpToCosMapEntry = _HpnicfDscpToCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 38, 1)
)
hpnicfDscpToCosMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpToCosMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDscpToCosMapEntry.setStatus("current")


class _HpnicfDscpToCosMapDscpIndex_Type(Integer32):
    """Custom type hpnicfDscpToCosMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpToCosMapDscpIndex_Type.__name__ = "Integer32"
_HpnicfDscpToCosMapDscpIndex_Object = MibTableColumn
hpnicfDscpToCosMapDscpIndex = _HpnicfDscpToCosMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 38, 1, 1),
    _HpnicfDscpToCosMapDscpIndex_Type()
)
hpnicfDscpToCosMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDscpToCosMapDscpIndex.setStatus("current")


class _HpnicfDscpToCosMapCosValue_Type(Integer32):
    """Custom type hpnicfDscpToCosMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HpnicfDscpToCosMapCosValue_Type.__name__ = "Integer32"
_HpnicfDscpToCosMapCosValue_Object = MibTableColumn
hpnicfDscpToCosMapCosValue = _HpnicfDscpToCosMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 38, 1, 2),
    _HpnicfDscpToCosMapCosValue_Type()
)
hpnicfDscpToCosMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToCosMapCosValue.setStatus("current")


class _HpnicfDscpToCosMapReset_Type(Integer32):
    """Custom type hpnicfDscpToCosMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDscpToCosMapReset_Type.__name__ = "Integer32"
_HpnicfDscpToCosMapReset_Object = MibTableColumn
hpnicfDscpToCosMapReset = _HpnicfDscpToCosMapReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 38, 1, 3),
    _HpnicfDscpToCosMapReset_Type()
)
hpnicfDscpToCosMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToCosMapReset.setStatus("current")
_HpnicfDscpToDscpMapTable_Object = MibTable
hpnicfDscpToDscpMapTable = _HpnicfDscpToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 39)
)
if mibBuilder.loadTexts:
    hpnicfDscpToDscpMapTable.setStatus("current")
_HpnicfDscpToDscpMapEntry_Object = MibTableRow
hpnicfDscpToDscpMapEntry = _HpnicfDscpToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 39, 1)
)
hpnicfDscpToDscpMapEntry.setIndexNames(
    (0, "HPN-ICF-LswQos-MIB", "hpnicfDscpToDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDscpToDscpMapEntry.setStatus("current")


class _HpnicfDscpToDscpMapDscpIndex_Type(Integer32):
    """Custom type hpnicfDscpToDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpToDscpMapDscpIndex_Type.__name__ = "Integer32"
_HpnicfDscpToDscpMapDscpIndex_Object = MibTableColumn
hpnicfDscpToDscpMapDscpIndex = _HpnicfDscpToDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 39, 1, 1),
    _HpnicfDscpToDscpMapDscpIndex_Type()
)
hpnicfDscpToDscpMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDscpToDscpMapDscpIndex.setStatus("current")


class _HpnicfDscpToDscpMapDscpValue_Type(Integer32):
    """Custom type hpnicfDscpToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_HpnicfDscpToDscpMapDscpValue_Type.__name__ = "Integer32"
_HpnicfDscpToDscpMapDscpValue_Object = MibTableColumn
hpnicfDscpToDscpMapDscpValue = _HpnicfDscpToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 39, 1, 2),
    _HpnicfDscpToDscpMapDscpValue_Type()
)
hpnicfDscpToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToDscpMapDscpValue.setStatus("current")


class _HpnicfDscpToDscpMapReset_Type(Integer32):
    """Custom type hpnicfDscpToDscpMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpnicfDscpToDscpMapReset_Type.__name__ = "Integer32"
_HpnicfDscpToDscpMapReset_Object = MibTableColumn
hpnicfDscpToDscpMapReset = _HpnicfDscpToDscpMapReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 16, 2, 39, 1, 3),
    _HpnicfDscpToDscpMapReset_Type()
)
hpnicfDscpToDscpMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDscpToDscpMapReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswQos-MIB",
    **{"HpnicfMirrorOrMonitorType": HpnicfMirrorOrMonitorType,
       "hpnicfLswQosAclMib": hpnicfLswQosAclMib,
       "hpnicfLswQosMibObject": hpnicfLswQosMibObject,
       "hpnicfPriorityTrustMode": hpnicfPriorityTrustMode,
       "hpnicfPortMonitorBothIfIndex": hpnicfPortMonitorBothIfIndex,
       "hpnicfQueueTable": hpnicfQueueTable,
       "hpnicfQueueEntry": hpnicfQueueEntry,
       "hpnicfQueueIfIndex": hpnicfQueueIfIndex,
       "hpnicfQueueScheduleMode": hpnicfQueueScheduleMode,
       "hpnicfQueueWeight1": hpnicfQueueWeight1,
       "hpnicfQueueWeight2": hpnicfQueueWeight2,
       "hpnicfQueueWeight3": hpnicfQueueWeight3,
       "hpnicfQueueWeight4": hpnicfQueueWeight4,
       "hpnicfQueueMaxDelay": hpnicfQueueMaxDelay,
       "hpnicfQueueWeight5": hpnicfQueueWeight5,
       "hpnicfQueueWeight6": hpnicfQueueWeight6,
       "hpnicfQueueWeight7": hpnicfQueueWeight7,
       "hpnicfQueueWeight8": hpnicfQueueWeight8,
       "hpnicfRateLimitTable": hpnicfRateLimitTable,
       "hpnicfRateLimitEntry": hpnicfRateLimitEntry,
       "hpnicfRateLimitAclIndex": hpnicfRateLimitAclIndex,
       "hpnicfRateLimitIfIndex": hpnicfRateLimitIfIndex,
       "hpnicfRateLimitVlanID": hpnicfRateLimitVlanID,
       "hpnicfRateLimitDirection": hpnicfRateLimitDirection,
       "hpnicfRateLimitUserAclNum": hpnicfRateLimitUserAclNum,
       "hpnicfRateLimitUserAclRule": hpnicfRateLimitUserAclRule,
       "hpnicfRateLimitIpAclNum": hpnicfRateLimitIpAclNum,
       "hpnicfRateLimitIpAclRule": hpnicfRateLimitIpAclRule,
       "hpnicfRateLimitLinkAclNum": hpnicfRateLimitLinkAclNum,
       "hpnicfRateLimitLinkAclRule": hpnicfRateLimitLinkAclRule,
       "hpnicfRateLimitTargetRateMbps": hpnicfRateLimitTargetRateMbps,
       "hpnicfRateLimitTargetRateKbps": hpnicfRateLimitTargetRateKbps,
       "hpnicfRateLimitPeakRate": hpnicfRateLimitPeakRate,
       "hpnicfRateLimitCIR": hpnicfRateLimitCIR,
       "hpnicfRateLimitCBS": hpnicfRateLimitCBS,
       "hpnicfRateLimitEBS": hpnicfRateLimitEBS,
       "hpnicfRateLimitPIR": hpnicfRateLimitPIR,
       "hpnicfRateLimitConformLocalPre": hpnicfRateLimitConformLocalPre,
       "hpnicfRateLimitConformActionType": hpnicfRateLimitConformActionType,
       "hpnicfRateLimitExceedActionType": hpnicfRateLimitExceedActionType,
       "hpnicfRateLimitExceedDscp": hpnicfRateLimitExceedDscp,
       "hpnicfRateLimitRuntime": hpnicfRateLimitRuntime,
       "hpnicfRateLimitRowStatus": hpnicfRateLimitRowStatus,
       "hpnicfRateLimitExceedCos": hpnicfRateLimitExceedCos,
       "hpnicfRateLimitConformCos": hpnicfRateLimitConformCos,
       "hpnicfRateLimitConformDscp": hpnicfRateLimitConformDscp,
       "hpnicfRateLimitMeterStatByteCount": hpnicfRateLimitMeterStatByteCount,
       "hpnicfRateLimitMeterStatByteXCount": hpnicfRateLimitMeterStatByteXCount,
       "hpnicfRateLimitMeterStatState": hpnicfRateLimitMeterStatState,
       "hpnicfPriorityTable": hpnicfPriorityTable,
       "hpnicfPriorityEntry": hpnicfPriorityEntry,
       "hpnicfPriorityAclIndex": hpnicfPriorityAclIndex,
       "hpnicfPriorityIfIndex": hpnicfPriorityIfIndex,
       "hpnicfPriorityVlanID": hpnicfPriorityVlanID,
       "hpnicfPriorityDirection": hpnicfPriorityDirection,
       "hpnicfPriorityUserAclNum": hpnicfPriorityUserAclNum,
       "hpnicfPriorityUserAclRule": hpnicfPriorityUserAclRule,
       "hpnicfPriorityIpAclNum": hpnicfPriorityIpAclNum,
       "hpnicfPriorityIpAclRule": hpnicfPriorityIpAclRule,
       "hpnicfPriorityLinkAclNum": hpnicfPriorityLinkAclNum,
       "hpnicfPriorityLinkAclRule": hpnicfPriorityLinkAclRule,
       "hpnicfPriorityDscp": hpnicfPriorityDscp,
       "hpnicfPriorityIpPre": hpnicfPriorityIpPre,
       "hpnicfPriorityIpPreFromCos": hpnicfPriorityIpPreFromCos,
       "hpnicfPriorityCos": hpnicfPriorityCos,
       "hpnicfPriorityCosFromIpPre": hpnicfPriorityCosFromIpPre,
       "hpnicfPriorityLocalPre": hpnicfPriorityLocalPre,
       "hpnicfPriorityPolicedServiceType": hpnicfPriorityPolicedServiceType,
       "hpnicfPriorityPolicedServiceDscp": hpnicfPriorityPolicedServiceDscp,
       "hpnicfPriorityPolicedServiceExp": hpnicfPriorityPolicedServiceExp,
       "hpnicfPriorityPolicedServiceCos": hpnicfPriorityPolicedServiceCos,
       "hpnicfPriorityPolicedServiceLoaclPre": hpnicfPriorityPolicedServiceLoaclPre,
       "hpnicfPriorityPolicedServiceDropPriority": hpnicfPriorityPolicedServiceDropPriority,
       "hpnicfPriorityRuntime": hpnicfPriorityRuntime,
       "hpnicfPriorityRowStatus": hpnicfPriorityRowStatus,
       "hpnicfRedirectTable": hpnicfRedirectTable,
       "hpnicfRedirectEntry": hpnicfRedirectEntry,
       "hpnicfRedirectAclIndex": hpnicfRedirectAclIndex,
       "hpnicfRedirectIfIndex": hpnicfRedirectIfIndex,
       "hpnicfRedirectVlanID": hpnicfRedirectVlanID,
       "hpnicfRedirectDirection": hpnicfRedirectDirection,
       "hpnicfRedirectUserAclNum": hpnicfRedirectUserAclNum,
       "hpnicfRedirectUserAclRule": hpnicfRedirectUserAclRule,
       "hpnicfRedirectIpAclNum": hpnicfRedirectIpAclNum,
       "hpnicfRedirectIpAclRule": hpnicfRedirectIpAclRule,
       "hpnicfRedirectLinkAclNum": hpnicfRedirectLinkAclNum,
       "hpnicfRedirectLinkAclRule": hpnicfRedirectLinkAclRule,
       "hpnicfRedirectToCpu": hpnicfRedirectToCpu,
       "hpnicfRedirectToIfIndex": hpnicfRedirectToIfIndex,
       "hpnicfRedirectToNextHop1": hpnicfRedirectToNextHop1,
       "hpnicfRedirectToNextHop2": hpnicfRedirectToNextHop2,
       "hpnicfRedirectRuntime": hpnicfRedirectRuntime,
       "hpnicfRedirectRowStatus": hpnicfRedirectRowStatus,
       "hpnicfRedirectToSlotNo": hpnicfRedirectToSlotNo,
       "hpnicfRedirectRemarkedDSCP": hpnicfRedirectRemarkedDSCP,
       "hpnicfRedirectRemarkedPri": hpnicfRedirectRemarkedPri,
       "hpnicfRedirectRemarkedTos": hpnicfRedirectRemarkedTos,
       "hpnicfRedirectToNextHop3": hpnicfRedirectToNextHop3,
       "hpnicfRedirectTargetVlanID": hpnicfRedirectTargetVlanID,
       "hpnicfRedirectMode": hpnicfRedirectMode,
       "hpnicfRedirectToNestedVlanID": hpnicfRedirectToNestedVlanID,
       "hpnicfRedirectToModifiedVlanID": hpnicfRedirectToModifiedVlanID,
       "hpnicfStatisticTable": hpnicfStatisticTable,
       "hpnicfStatisticEntry": hpnicfStatisticEntry,
       "hpnicfStatisticAclIndex": hpnicfStatisticAclIndex,
       "hpnicfStatisticIfIndex": hpnicfStatisticIfIndex,
       "hpnicfStatisticVlanID": hpnicfStatisticVlanID,
       "hpnicfStatisticDirection": hpnicfStatisticDirection,
       "hpnicfStatisticUserAclNum": hpnicfStatisticUserAclNum,
       "hpnicfStatisticUserAclRule": hpnicfStatisticUserAclRule,
       "hpnicfStatisticIpAclNum": hpnicfStatisticIpAclNum,
       "hpnicfStatisticIpAclRule": hpnicfStatisticIpAclRule,
       "hpnicfStatisticLinkAclNum": hpnicfStatisticLinkAclNum,
       "hpnicfStatisticLinkAclRule": hpnicfStatisticLinkAclRule,
       "hpnicfStatisticRuntime": hpnicfStatisticRuntime,
       "hpnicfStatisticPacketCount": hpnicfStatisticPacketCount,
       "hpnicfStatisticByteCount": hpnicfStatisticByteCount,
       "hpnicfStatisticCountClear": hpnicfStatisticCountClear,
       "hpnicfStatisticRowStatus": hpnicfStatisticRowStatus,
       "hpnicfStatisticPacketXCount": hpnicfStatisticPacketXCount,
       "hpnicfStatisticByteXCount": hpnicfStatisticByteXCount,
       "hpnicfMirrorTable": hpnicfMirrorTable,
       "hpnicfMirrorEntry": hpnicfMirrorEntry,
       "hpnicfMirrorAclIndex": hpnicfMirrorAclIndex,
       "hpnicfMirrorIfIndex": hpnicfMirrorIfIndex,
       "hpnicfMirrorVlanID": hpnicfMirrorVlanID,
       "hpnicfMirrorDirection": hpnicfMirrorDirection,
       "hpnicfMirrorUserAclNum": hpnicfMirrorUserAclNum,
       "hpnicfMirrorUserAclRule": hpnicfMirrorUserAclRule,
       "hpnicfMirrorIpAclNum": hpnicfMirrorIpAclNum,
       "hpnicfMirrorIpAclRule": hpnicfMirrorIpAclRule,
       "hpnicfMirrorLinkAclNum": hpnicfMirrorLinkAclNum,
       "hpnicfMirrorLinkAclRule": hpnicfMirrorLinkAclRule,
       "hpnicfMirrorToIfIndex": hpnicfMirrorToIfIndex,
       "hpnicfMirrorToCpu": hpnicfMirrorToCpu,
       "hpnicfMirrorRuntime": hpnicfMirrorRuntime,
       "hpnicfMirrorRowStatus": hpnicfMirrorRowStatus,
       "hpnicfMirrorToGroup": hpnicfMirrorToGroup,
       "hpnicfPortMirrorTable": hpnicfPortMirrorTable,
       "hpnicfPortMirrorEntry": hpnicfPortMirrorEntry,
       "hpnicfPortMirrorIfIndex": hpnicfPortMirrorIfIndex,
       "hpnicfPortMirrorDirection": hpnicfPortMirrorDirection,
       "hpnicfPortMirrorRowStatus": hpnicfPortMirrorRowStatus,
       "hpnicfLineRateTable": hpnicfLineRateTable,
       "hpnicfLineRateEntry": hpnicfLineRateEntry,
       "hpnicfLineRateIfIndex": hpnicfLineRateIfIndex,
       "hpnicfLineRateDirection": hpnicfLineRateDirection,
       "hpnicfLineRateValue": hpnicfLineRateValue,
       "hpnicfLineRateRowStatus": hpnicfLineRateRowStatus,
       "hpnicfBandwidthTable": hpnicfBandwidthTable,
       "hpnicfBandwidthEntry": hpnicfBandwidthEntry,
       "hpnicfBandwidthAclIndex": hpnicfBandwidthAclIndex,
       "hpnicfBandwidthIfIndex": hpnicfBandwidthIfIndex,
       "hpnicfBandwidthVlanID": hpnicfBandwidthVlanID,
       "hpnicfBandwidthDirection": hpnicfBandwidthDirection,
       "hpnicfBandwidthIpAclNum": hpnicfBandwidthIpAclNum,
       "hpnicfBandwidthIpAclRule": hpnicfBandwidthIpAclRule,
       "hpnicfBandwidthLinkAclNum": hpnicfBandwidthLinkAclNum,
       "hpnicfBandwidthLinkAclRule": hpnicfBandwidthLinkAclRule,
       "hpnicfBandwidthMinGuaranteedWidth": hpnicfBandwidthMinGuaranteedWidth,
       "hpnicfBandwidthMaxGuaranteedWidth": hpnicfBandwidthMaxGuaranteedWidth,
       "hpnicfBandwidthWeight": hpnicfBandwidthWeight,
       "hpnicfBandwidthRuntime": hpnicfBandwidthRuntime,
       "hpnicfBandwidthRowStatus": hpnicfBandwidthRowStatus,
       "hpnicfRedTable": hpnicfRedTable,
       "hpnicfRedEntry": hpnicfRedEntry,
       "hpnicfRedAclIndex": hpnicfRedAclIndex,
       "hpnicfRedIfIndex": hpnicfRedIfIndex,
       "hpnicfRedVlanID": hpnicfRedVlanID,
       "hpnicfRedDirection": hpnicfRedDirection,
       "hpnicfRedIpAclNum": hpnicfRedIpAclNum,
       "hpnicfRedIpAclRule": hpnicfRedIpAclRule,
       "hpnicfRedLinkAclNum": hpnicfRedLinkAclNum,
       "hpnicfRedLinkAclRule": hpnicfRedLinkAclRule,
       "hpnicfRedStartQueueLen": hpnicfRedStartQueueLen,
       "hpnicfRedStopQueueLen": hpnicfRedStopQueueLen,
       "hpnicfRedProbability": hpnicfRedProbability,
       "hpnicfRedRuntime": hpnicfRedRuntime,
       "hpnicfRedRowStatus": hpnicfRedRowStatus,
       "hpnicfMirrorGroupTable": hpnicfMirrorGroupTable,
       "hpnicfMirrorGroupEntry": hpnicfMirrorGroupEntry,
       "hpnicfMirrorGroupID": hpnicfMirrorGroupID,
       "hpnicfMirrorGroupDirection": hpnicfMirrorGroupDirection,
       "hpnicfMirrorGroupMirrorIfIndexList": hpnicfMirrorGroupMirrorIfIndexList,
       "hpnicfMirrorGroupMonitorIfIndex": hpnicfMirrorGroupMonitorIfIndex,
       "hpnicfMirrorGroupRowStatus": hpnicfMirrorGroupRowStatus,
       "hpnicfFlowtempTable": hpnicfFlowtempTable,
       "hpnicfFlowtempEntry": hpnicfFlowtempEntry,
       "hpnicfFlowtempIndex": hpnicfFlowtempIndex,
       "hpnicfFlowtempIpProtocol": hpnicfFlowtempIpProtocol,
       "hpnicfFlowtempTcpFlag": hpnicfFlowtempTcpFlag,
       "hpnicfFlowtempSPort": hpnicfFlowtempSPort,
       "hpnicfFlowtempDPort": hpnicfFlowtempDPort,
       "hpnicfFlowtempIcmpType": hpnicfFlowtempIcmpType,
       "hpnicfFlowtempIcmpCode": hpnicfFlowtempIcmpCode,
       "hpnicfFlowtempFragment": hpnicfFlowtempFragment,
       "hpnicfFlowtempDscp": hpnicfFlowtempDscp,
       "hpnicfFlowtempIpPre": hpnicfFlowtempIpPre,
       "hpnicfFlowtempTos": hpnicfFlowtempTos,
       "hpnicfFlowtempSIp": hpnicfFlowtempSIp,
       "hpnicfFlowtempSIpMask": hpnicfFlowtempSIpMask,
       "hpnicfFlowtempDIp": hpnicfFlowtempDIp,
       "hpnicfFlowtempDIpMask": hpnicfFlowtempDIpMask,
       "hpnicfFlowtempEthProtocol": hpnicfFlowtempEthProtocol,
       "hpnicfFlowtempSMac": hpnicfFlowtempSMac,
       "hpnicfFlowtempSMacMask": hpnicfFlowtempSMacMask,
       "hpnicfFlowtempDMac": hpnicfFlowtempDMac,
       "hpnicfFlowtempDMacMask": hpnicfFlowtempDMacMask,
       "hpnicfFlowtempVpn": hpnicfFlowtempVpn,
       "hpnicfFlowtempRowStatus": hpnicfFlowtempRowStatus,
       "hpnicfFlowtempVlanId": hpnicfFlowtempVlanId,
       "hpnicfFlowtempCos": hpnicfFlowtempCos,
       "hpnicfFlowtempEnableTable": hpnicfFlowtempEnableTable,
       "hpnicfFlowtempEnableEntry": hpnicfFlowtempEnableEntry,
       "hpnicfFlowtempEnableIfIndex": hpnicfFlowtempEnableIfIndex,
       "hpnicfFlowtempEnableVlanID": hpnicfFlowtempEnableVlanID,
       "hpnicfFlowtempEnableFlowtempIndex": hpnicfFlowtempEnableFlowtempIndex,
       "hpnicfTrafficShapeTable": hpnicfTrafficShapeTable,
       "hpnicfTrafficShapeEntry": hpnicfTrafficShapeEntry,
       "hpnicfTrafficShapeIfIndex": hpnicfTrafficShapeIfIndex,
       "hpnicfTrafficShapeQueueId": hpnicfTrafficShapeQueueId,
       "hpnicfTrafficShapeMaxRate": hpnicfTrafficShapeMaxRate,
       "hpnicfTrafficShapeBurstSize": hpnicfTrafficShapeBurstSize,
       "hpnicfTrafficShapeBufferLimit": hpnicfTrafficShapeBufferLimit,
       "hpnicfTrafficShapeRowStatus": hpnicfTrafficShapeRowStatus,
       "hpnicfPortQueueTable": hpnicfPortQueueTable,
       "hpnicfPortQueueEntry": hpnicfPortQueueEntry,
       "hpnicfPortQueueIfIndex": hpnicfPortQueueIfIndex,
       "hpnicfPortQueueQueueID": hpnicfPortQueueQueueID,
       "hpnicfPortQueueWrrPriority": hpnicfPortQueueWrrPriority,
       "hpnicfPortQueueWeight": hpnicfPortQueueWeight,
       "hpnicfDropModeTable": hpnicfDropModeTable,
       "hpnicfDropModeEntry": hpnicfDropModeEntry,
       "hpnicfDropModeIfIndex": hpnicfDropModeIfIndex,
       "hpnicfDropModeMode": hpnicfDropModeMode,
       "hpnicfDropModeWredIndex": hpnicfDropModeWredIndex,
       "hpnicfWredTable": hpnicfWredTable,
       "hpnicfWredEntry": hpnicfWredEntry,
       "hpnicfWredIndex": hpnicfWredIndex,
       "hpnicfWredQueueId": hpnicfWredQueueId,
       "hpnicfWredGreenMinThreshold": hpnicfWredGreenMinThreshold,
       "hpnicfWredGreenMaxThreshold": hpnicfWredGreenMaxThreshold,
       "hpnicfWredGreenMaxProb": hpnicfWredGreenMaxProb,
       "hpnicfWredYellowMinThreshold": hpnicfWredYellowMinThreshold,
       "hpnicfWredYellowMaxThreshold": hpnicfWredYellowMaxThreshold,
       "hpnicfWredYellowMaxProb": hpnicfWredYellowMaxProb,
       "hpnicfWredRedMinThreshold": hpnicfWredRedMinThreshold,
       "hpnicfWredRedMaxThreshold": hpnicfWredRedMaxThreshold,
       "hpnicfWredRedMaxProb": hpnicfWredRedMaxProb,
       "hpnicfWredExponent": hpnicfWredExponent,
       "hpnicfCosToLocalPrecedenceMapTable": hpnicfCosToLocalPrecedenceMapTable,
       "hpnicfCosToLocalPrecedenceMapEntry": hpnicfCosToLocalPrecedenceMapEntry,
       "hpnicfCosToLocalPrecedenceMapCosIndex": hpnicfCosToLocalPrecedenceMapCosIndex,
       "hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue": hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue,
       "hpnicfCosToDropPrecedenceMapTable": hpnicfCosToDropPrecedenceMapTable,
       "hpnicfCosToDropPrecedenceMapEntry": hpnicfCosToDropPrecedenceMapEntry,
       "hpnicfCosToDropPrecedenceMapCosIndex": hpnicfCosToDropPrecedenceMapCosIndex,
       "hpnicfCosToDropPrecedenceMapDropPrecedenceValue": hpnicfCosToDropPrecedenceMapDropPrecedenceValue,
       "hpnicfDscpMapTable": hpnicfDscpMapTable,
       "hpnicfDscpMapEntry": hpnicfDscpMapEntry,
       "hpnicfDscpMapConformLevel": hpnicfDscpMapConformLevel,
       "hpnicfDscpMapDscpIndex": hpnicfDscpMapDscpIndex,
       "hpnicfDscpMapDscpValue": hpnicfDscpMapDscpValue,
       "hpnicfDscpMapExpValue": hpnicfDscpMapExpValue,
       "hpnicfDscpMapCosValue": hpnicfDscpMapCosValue,
       "hpnicfDscpMapLocalPrecedence": hpnicfDscpMapLocalPrecedence,
       "hpnicfDscpMapDropPrecedence": hpnicfDscpMapDropPrecedence,
       "hpnicfExpMapTable": hpnicfExpMapTable,
       "hpnicfExpMapEntry": hpnicfExpMapEntry,
       "hpnicfExpMapConformLevel": hpnicfExpMapConformLevel,
       "hpnicfExpMapExpIndex": hpnicfExpMapExpIndex,
       "hpnicfExpMapDscpValue": hpnicfExpMapDscpValue,
       "hpnicfExpMapExpValue": hpnicfExpMapExpValue,
       "hpnicfExpMapCosValue": hpnicfExpMapCosValue,
       "hpnicfExpMapLocalPrecedence": hpnicfExpMapLocalPrecedence,
       "hpnicfExpMapDropPrecedence": hpnicfExpMapDropPrecedence,
       "hpnicfLocalPrecedenceMapTable": hpnicfLocalPrecedenceMapTable,
       "hpnicfLocalPrecedenceMapEntry": hpnicfLocalPrecedenceMapEntry,
       "hpnicfLocalPrecedenceMapConformLevel": hpnicfLocalPrecedenceMapConformLevel,
       "hpnicfLocalPrecedenceMapLocalPrecedenceIndex": hpnicfLocalPrecedenceMapLocalPrecedenceIndex,
       "hpnicfLocalPrecedenceMapCosValue": hpnicfLocalPrecedenceMapCosValue,
       "hpnicfPortWredTable": hpnicfPortWredTable,
       "hpnicfPortWredEntry": hpnicfPortWredEntry,
       "hpnicfPortWredIfIndex": hpnicfPortWredIfIndex,
       "hpnicfPortWredQueueID": hpnicfPortWredQueueID,
       "hpnicfPortWredQueueStartLength": hpnicfPortWredQueueStartLength,
       "hpnicfPortWredQueueProbability": hpnicfPortWredQueueProbability,
       "hpnicfMirroringGroupTable": hpnicfMirroringGroupTable,
       "hpnicfMirroringGroupEntry": hpnicfMirroringGroupEntry,
       "hpnicfMirroringGroupID": hpnicfMirroringGroupID,
       "hpnicfMirroringGroupType": hpnicfMirroringGroupType,
       "hpnicfMirroringGroupStatus": hpnicfMirroringGroupStatus,
       "hpnicfMirroringGroupRowStatus": hpnicfMirroringGroupRowStatus,
       "hpnicfMirroringGroupMirrorTable": hpnicfMirroringGroupMirrorTable,
       "hpnicfMirroringGroupMirrorEntry": hpnicfMirroringGroupMirrorEntry,
       "hpnicfMirroringGroupMirrorInboundIfIndexList": hpnicfMirroringGroupMirrorInboundIfIndexList,
       "hpnicfMirroringGroupMirrorOutboundIfIndexList": hpnicfMirroringGroupMirrorOutboundIfIndexList,
       "hpnicfMirroringGroupMirrorRowStatus": hpnicfMirroringGroupMirrorRowStatus,
       "hpnicfMirroringGroupMirrorInTypeList": hpnicfMirroringGroupMirrorInTypeList,
       "hpnicfMirroringGroupMirrorOutTypeList": hpnicfMirroringGroupMirrorOutTypeList,
       "hpnicfMirroringGroupMonitorTable": hpnicfMirroringGroupMonitorTable,
       "hpnicfMirroringGroupMonitorEntry": hpnicfMirroringGroupMonitorEntry,
       "hpnicfMirroringGroupMonitorIfIndex": hpnicfMirroringGroupMonitorIfIndex,
       "hpnicfMirroringGroupMonitorRowStatus": hpnicfMirroringGroupMonitorRowStatus,
       "hpnicfMirroringGroupMonitorType": hpnicfMirroringGroupMonitorType,
       "hpnicfMirroringGroupReflectorTable": hpnicfMirroringGroupReflectorTable,
       "hpnicfMirroringGroupReflectorEntry": hpnicfMirroringGroupReflectorEntry,
       "hpnicfMirroringGroupReflectorIfIndex": hpnicfMirroringGroupReflectorIfIndex,
       "hpnicfMirroringGroupReflectorRowStatus": hpnicfMirroringGroupReflectorRowStatus,
       "hpnicfMirroringGroupRprobeVlanTable": hpnicfMirroringGroupRprobeVlanTable,
       "hpnicfMirroringGroupRprobeVlanEntry": hpnicfMirroringGroupRprobeVlanEntry,
       "hpnicfMirroringGroupRprobeVlanID": hpnicfMirroringGroupRprobeVlanID,
       "hpnicfMirroringGroupRprobeVlanRowStatus": hpnicfMirroringGroupRprobeVlanRowStatus,
       "hpnicfMirroringGroupMirrorMacTable": hpnicfMirroringGroupMirrorMacTable,
       "hpnicfMirroringGroupMirrorMacEntry": hpnicfMirroringGroupMirrorMacEntry,
       "hpnicfMirroringGroupMirrorMacSeq": hpnicfMirroringGroupMirrorMacSeq,
       "hpnicfMirroringGroupMirrorMac": hpnicfMirroringGroupMirrorMac,
       "hpnicfMirrorMacVlanID": hpnicfMirrorMacVlanID,
       "hpnicfMirroringGroupMirroMacStatus": hpnicfMirroringGroupMirroMacStatus,
       "hpnicfMirroringGroupMirrorVlanTable": hpnicfMirroringGroupMirrorVlanTable,
       "hpnicfMirroringGroupMirrorVlanEntry": hpnicfMirroringGroupMirrorVlanEntry,
       "hpnicfMirroringGroupMirrorVlanSeq": hpnicfMirroringGroupMirrorVlanSeq,
       "hpnicfMirroringGroupMirrorVlanID": hpnicfMirroringGroupMirrorVlanID,
       "hpnicfMirroringGroupMirrorVlanDirection": hpnicfMirroringGroupMirrorVlanDirection,
       "hpnicfMirroringGroupMirroVlanStatus": hpnicfMirroringGroupMirroVlanStatus,
       "hpnicfPortTrustTable": hpnicfPortTrustTable,
       "hpnicfPortTrustEntry": hpnicfPortTrustEntry,
       "hpnicfPortTrustIfIndex": hpnicfPortTrustIfIndex,
       "hpnicfPortTrustTrustType": hpnicfPortTrustTrustType,
       "hpnicfPortTrustOvercastType": hpnicfPortTrustOvercastType,
       "hpnicfPortTrustReset": hpnicfPortTrustReset,
       "hpnicfRemarkVlanIDTable": hpnicfRemarkVlanIDTable,
       "hpnicfRemarkVlanIDEntry": hpnicfRemarkVlanIDEntry,
       "hpnicfRemarkVlanIDAclIndex": hpnicfRemarkVlanIDAclIndex,
       "hpnicfRemarkVlanIDIfIndex": hpnicfRemarkVlanIDIfIndex,
       "hpnicfRemarkVlanIDVlanID": hpnicfRemarkVlanIDVlanID,
       "hpnicfRemarkVlanIDDirection": hpnicfRemarkVlanIDDirection,
       "hpnicfRemarkVlanIDUserAclNum": hpnicfRemarkVlanIDUserAclNum,
       "hpnicfRemarkVlanIDUserAclRule": hpnicfRemarkVlanIDUserAclRule,
       "hpnicfRemarkVlanIDIpAclNum": hpnicfRemarkVlanIDIpAclNum,
       "hpnicfRemarkVlanIDIpAclRule": hpnicfRemarkVlanIDIpAclRule,
       "hpnicfRemarkVlanIDLinkAclNum": hpnicfRemarkVlanIDLinkAclNum,
       "hpnicfRemarkVlanIDLinkAclRule": hpnicfRemarkVlanIDLinkAclRule,
       "hpnicfRemarkVlanIDRemarkVlanID": hpnicfRemarkVlanIDRemarkVlanID,
       "hpnicfRemarkVlanIDPacketType": hpnicfRemarkVlanIDPacketType,
       "hpnicfRemarkVlanIDRowStatus": hpnicfRemarkVlanIDRowStatus,
       "hpnicfCosToDscpMapTable": hpnicfCosToDscpMapTable,
       "hpnicfCosToDscpMapEntry": hpnicfCosToDscpMapEntry,
       "hpnicfCosToDscpMapCosIndex": hpnicfCosToDscpMapCosIndex,
       "hpnicfCosToDscpMapDscpValue": hpnicfCosToDscpMapDscpValue,
       "hpnicfCosToDscpMapReSet": hpnicfCosToDscpMapReSet,
       "hpnicfDscpToLocalPreMapTable": hpnicfDscpToLocalPreMapTable,
       "hpnicfDscpToLocalPreMapEntry": hpnicfDscpToLocalPreMapEntry,
       "hpnicfDscpToLocalPreMapDscpIndex": hpnicfDscpToLocalPreMapDscpIndex,
       "hpnicfDscpToLocalPreMapLocalPreVal": hpnicfDscpToLocalPreMapLocalPreVal,
       "hpnicfDscpToLocalPreMapReset": hpnicfDscpToLocalPreMapReset,
       "hpnicfDscpToDropPreMapTable": hpnicfDscpToDropPreMapTable,
       "hpnicfDscpToDropPreMapEntry": hpnicfDscpToDropPreMapEntry,
       "hpnicfDscpToDropPreMapDscpIndex": hpnicfDscpToDropPreMapDscpIndex,
       "hpnicfDscpToDropPreMapDropPreVal": hpnicfDscpToDropPreMapDropPreVal,
       "hpnicfDscpToDropPreMapReset": hpnicfDscpToDropPreMapReset,
       "hpnicfDscpToCosMapTable": hpnicfDscpToCosMapTable,
       "hpnicfDscpToCosMapEntry": hpnicfDscpToCosMapEntry,
       "hpnicfDscpToCosMapDscpIndex": hpnicfDscpToCosMapDscpIndex,
       "hpnicfDscpToCosMapCosValue": hpnicfDscpToCosMapCosValue,
       "hpnicfDscpToCosMapReset": hpnicfDscpToCosMapReset,
       "hpnicfDscpToDscpMapTable": hpnicfDscpToDscpMapTable,
       "hpnicfDscpToDscpMapEntry": hpnicfDscpToDscpMapEntry,
       "hpnicfDscpToDscpMapDscpIndex": hpnicfDscpToDscpMapDscpIndex,
       "hpnicfDscpToDscpMapDscpValue": hpnicfDscpToDscpMapDscpValue,
       "hpnicfDscpToDscpMapReset": hpnicfDscpToDscpMapReset}
)
