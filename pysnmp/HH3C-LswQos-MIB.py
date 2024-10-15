# SNMP MIB module (HH3C-LswQos-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswQos-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:59 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

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

hh3cLswQosAclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16)
)
hh3cLswQosAclMib.setRevisions(
        ("2002-11-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMirrorOrMonitorType(Integer32, TextualConvention):
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

_Hh3cLswQosMibObject_ObjectIdentity = ObjectIdentity
hh3cLswQosMibObject = _Hh3cLswQosMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2)
)


class _Hh3cPriorityTrustMode_Type(Integer32):
    """Custom type hh3cPriorityTrustMode based on Integer32"""
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


_Hh3cPriorityTrustMode_Type.__name__ = "Integer32"
_Hh3cPriorityTrustMode_Object = MibScalar
hh3cPriorityTrustMode = _Hh3cPriorityTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 1),
    _Hh3cPriorityTrustMode_Type()
)
hh3cPriorityTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPriorityTrustMode.setStatus("current")


class _Hh3cPortMonitorBothIfIndex_Type(Integer32):
    """Custom type hh3cPortMonitorBothIfIndex based on Integer32"""
    defaultValue = 0


_Hh3cPortMonitorBothIfIndex_Object = MibScalar
hh3cPortMonitorBothIfIndex = _Hh3cPortMonitorBothIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 2),
    _Hh3cPortMonitorBothIfIndex_Type()
)
hh3cPortMonitorBothIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortMonitorBothIfIndex.setStatus("current")
_Hh3cQueueTable_Object = MibTable
hh3cQueueTable = _Hh3cQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cQueueTable.setStatus("current")
_Hh3cQueueEntry_Object = MibTableRow
hh3cQueueEntry = _Hh3cQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1)
)
hh3cQueueEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cQueueIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cQueueEntry.setStatus("current")
_Hh3cQueueIfIndex_Type = Integer32
_Hh3cQueueIfIndex_Object = MibTableColumn
hh3cQueueIfIndex = _Hh3cQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 1),
    _Hh3cQueueIfIndex_Type()
)
hh3cQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cQueueIfIndex.setStatus("current")


class _Hh3cQueueScheduleMode_Type(Integer32):
    """Custom type hh3cQueueScheduleMode based on Integer32"""
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


_Hh3cQueueScheduleMode_Type.__name__ = "Integer32"
_Hh3cQueueScheduleMode_Object = MibTableColumn
hh3cQueueScheduleMode = _Hh3cQueueScheduleMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 2),
    _Hh3cQueueScheduleMode_Type()
)
hh3cQueueScheduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueScheduleMode.setStatus("current")
_Hh3cQueueWeight1_Type = Integer32
_Hh3cQueueWeight1_Object = MibTableColumn
hh3cQueueWeight1 = _Hh3cQueueWeight1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 3),
    _Hh3cQueueWeight1_Type()
)
hh3cQueueWeight1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight1.setStatus("current")
_Hh3cQueueWeight2_Type = Integer32
_Hh3cQueueWeight2_Object = MibTableColumn
hh3cQueueWeight2 = _Hh3cQueueWeight2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 4),
    _Hh3cQueueWeight2_Type()
)
hh3cQueueWeight2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight2.setStatus("current")
_Hh3cQueueWeight3_Type = Integer32
_Hh3cQueueWeight3_Object = MibTableColumn
hh3cQueueWeight3 = _Hh3cQueueWeight3_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 5),
    _Hh3cQueueWeight3_Type()
)
hh3cQueueWeight3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight3.setStatus("current")
_Hh3cQueueWeight4_Type = Integer32
_Hh3cQueueWeight4_Object = MibTableColumn
hh3cQueueWeight4 = _Hh3cQueueWeight4_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 6),
    _Hh3cQueueWeight4_Type()
)
hh3cQueueWeight4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight4.setStatus("current")


class _Hh3cQueueMaxDelay_Type(Integer32):
    """Custom type hh3cQueueMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cQueueMaxDelay_Type.__name__ = "Integer32"
_Hh3cQueueMaxDelay_Object = MibTableColumn
hh3cQueueMaxDelay = _Hh3cQueueMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 7),
    _Hh3cQueueMaxDelay_Type()
)
hh3cQueueMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueMaxDelay.setStatus("current")
_Hh3cQueueWeight5_Type = Integer32
_Hh3cQueueWeight5_Object = MibTableColumn
hh3cQueueWeight5 = _Hh3cQueueWeight5_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 8),
    _Hh3cQueueWeight5_Type()
)
hh3cQueueWeight5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight5.setStatus("current")
_Hh3cQueueWeight6_Type = Integer32
_Hh3cQueueWeight6_Object = MibTableColumn
hh3cQueueWeight6 = _Hh3cQueueWeight6_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 9),
    _Hh3cQueueWeight6_Type()
)
hh3cQueueWeight6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight6.setStatus("current")
_Hh3cQueueWeight7_Type = Integer32
_Hh3cQueueWeight7_Object = MibTableColumn
hh3cQueueWeight7 = _Hh3cQueueWeight7_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 10),
    _Hh3cQueueWeight7_Type()
)
hh3cQueueWeight7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight7.setStatus("current")
_Hh3cQueueWeight8_Type = Integer32
_Hh3cQueueWeight8_Object = MibTableColumn
hh3cQueueWeight8 = _Hh3cQueueWeight8_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 3, 1, 11),
    _Hh3cQueueWeight8_Type()
)
hh3cQueueWeight8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cQueueWeight8.setStatus("current")
_Hh3cRateLimitTable_Object = MibTable
hh3cRateLimitTable = _Hh3cRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cRateLimitTable.setStatus("current")
_Hh3cRateLimitEntry_Object = MibTableRow
hh3cRateLimitEntry = _Hh3cRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1)
)
hh3cRateLimitEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cRateLimitAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRateLimitIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRateLimitVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cRateLimitDirection"),
)
if mibBuilder.loadTexts:
    hh3cRateLimitEntry.setStatus("current")


class _Hh3cRateLimitAclIndex_Type(Integer32):
    """Custom type hh3cRateLimitAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cRateLimitAclIndex_Type.__name__ = "Integer32"
_Hh3cRateLimitAclIndex_Object = MibTableColumn
hh3cRateLimitAclIndex = _Hh3cRateLimitAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 1),
    _Hh3cRateLimitAclIndex_Type()
)
hh3cRateLimitAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitAclIndex.setStatus("current")
_Hh3cRateLimitIfIndex_Type = Integer32
_Hh3cRateLimitIfIndex_Object = MibTableColumn
hh3cRateLimitIfIndex = _Hh3cRateLimitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 2),
    _Hh3cRateLimitIfIndex_Type()
)
hh3cRateLimitIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitIfIndex.setStatus("current")


class _Hh3cRateLimitVlanID_Type(Integer32):
    """Custom type hh3cRateLimitVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRateLimitVlanID_Type.__name__ = "Integer32"
_Hh3cRateLimitVlanID_Object = MibTableColumn
hh3cRateLimitVlanID = _Hh3cRateLimitVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 3),
    _Hh3cRateLimitVlanID_Type()
)
hh3cRateLimitVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitVlanID.setStatus("current")


class _Hh3cRateLimitDirection_Type(Integer32):
    """Custom type hh3cRateLimitDirection based on Integer32"""
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


_Hh3cRateLimitDirection_Type.__name__ = "Integer32"
_Hh3cRateLimitDirection_Object = MibTableColumn
hh3cRateLimitDirection = _Hh3cRateLimitDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 4),
    _Hh3cRateLimitDirection_Type()
)
hh3cRateLimitDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitDirection.setStatus("current")


class _Hh3cRateLimitUserAclNum_Type(Integer32):
    """Custom type hh3cRateLimitUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRateLimitUserAclNum_Type.__name__ = "Integer32"
_Hh3cRateLimitUserAclNum_Object = MibTableColumn
hh3cRateLimitUserAclNum = _Hh3cRateLimitUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 5),
    _Hh3cRateLimitUserAclNum_Type()
)
hh3cRateLimitUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitUserAclNum.setStatus("current")


class _Hh3cRateLimitUserAclRule_Type(Integer32):
    """Custom type hh3cRateLimitUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRateLimitUserAclRule_Type.__name__ = "Integer32"
_Hh3cRateLimitUserAclRule_Object = MibTableColumn
hh3cRateLimitUserAclRule = _Hh3cRateLimitUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 6),
    _Hh3cRateLimitUserAclRule_Type()
)
hh3cRateLimitUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitUserAclRule.setStatus("current")


class _Hh3cRateLimitIpAclNum_Type(Integer32):
    """Custom type hh3cRateLimitIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRateLimitIpAclNum_Type.__name__ = "Integer32"
_Hh3cRateLimitIpAclNum_Object = MibTableColumn
hh3cRateLimitIpAclNum = _Hh3cRateLimitIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 7),
    _Hh3cRateLimitIpAclNum_Type()
)
hh3cRateLimitIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitIpAclNum.setStatus("current")


class _Hh3cRateLimitIpAclRule_Type(Integer32):
    """Custom type hh3cRateLimitIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRateLimitIpAclRule_Type.__name__ = "Integer32"
_Hh3cRateLimitIpAclRule_Object = MibTableColumn
hh3cRateLimitIpAclRule = _Hh3cRateLimitIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 8),
    _Hh3cRateLimitIpAclRule_Type()
)
hh3cRateLimitIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitIpAclRule.setStatus("current")


class _Hh3cRateLimitLinkAclNum_Type(Integer32):
    """Custom type hh3cRateLimitLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRateLimitLinkAclNum_Type.__name__ = "Integer32"
_Hh3cRateLimitLinkAclNum_Object = MibTableColumn
hh3cRateLimitLinkAclNum = _Hh3cRateLimitLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 9),
    _Hh3cRateLimitLinkAclNum_Type()
)
hh3cRateLimitLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitLinkAclNum.setStatus("current")


class _Hh3cRateLimitLinkAclRule_Type(Integer32):
    """Custom type hh3cRateLimitLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRateLimitLinkAclRule_Type.__name__ = "Integer32"
_Hh3cRateLimitLinkAclRule_Object = MibTableColumn
hh3cRateLimitLinkAclRule = _Hh3cRateLimitLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 10),
    _Hh3cRateLimitLinkAclRule_Type()
)
hh3cRateLimitLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitLinkAclRule.setStatus("current")
_Hh3cRateLimitTargetRateMbps_Type = Integer32
_Hh3cRateLimitTargetRateMbps_Object = MibTableColumn
hh3cRateLimitTargetRateMbps = _Hh3cRateLimitTargetRateMbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 11),
    _Hh3cRateLimitTargetRateMbps_Type()
)
hh3cRateLimitTargetRateMbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitTargetRateMbps.setStatus("current")
_Hh3cRateLimitTargetRateKbps_Type = Integer32
_Hh3cRateLimitTargetRateKbps_Object = MibTableColumn
hh3cRateLimitTargetRateKbps = _Hh3cRateLimitTargetRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 12),
    _Hh3cRateLimitTargetRateKbps_Type()
)
hh3cRateLimitTargetRateKbps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitTargetRateKbps.setStatus("current")


class _Hh3cRateLimitPeakRate_Type(Integer32):
    """Custom type hh3cRateLimitPeakRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(64, 8388608),
    )


_Hh3cRateLimitPeakRate_Type.__name__ = "Integer32"
_Hh3cRateLimitPeakRate_Object = MibTableColumn
hh3cRateLimitPeakRate = _Hh3cRateLimitPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 13),
    _Hh3cRateLimitPeakRate_Type()
)
hh3cRateLimitPeakRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitPeakRate.setStatus("current")


class _Hh3cRateLimitCIR_Type(Integer32):
    """Custom type hh3cRateLimitCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_Hh3cRateLimitCIR_Type.__name__ = "Integer32"
_Hh3cRateLimitCIR_Object = MibTableColumn
hh3cRateLimitCIR = _Hh3cRateLimitCIR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 14),
    _Hh3cRateLimitCIR_Type()
)
hh3cRateLimitCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitCIR.setStatus("current")


class _Hh3cRateLimitCBS_Type(Integer32):
    """Custom type hh3cRateLimitCBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_Hh3cRateLimitCBS_Type.__name__ = "Integer32"
_Hh3cRateLimitCBS_Object = MibTableColumn
hh3cRateLimitCBS = _Hh3cRateLimitCBS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 15),
    _Hh3cRateLimitCBS_Type()
)
hh3cRateLimitCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitCBS.setStatus("current")


class _Hh3cRateLimitEBS_Type(Integer32):
    """Custom type hh3cRateLimitEBS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 268435455),
    )


_Hh3cRateLimitEBS_Type.__name__ = "Integer32"
_Hh3cRateLimitEBS_Object = MibTableColumn
hh3cRateLimitEBS = _Hh3cRateLimitEBS_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 16),
    _Hh3cRateLimitEBS_Type()
)
hh3cRateLimitEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitEBS.setStatus("current")


class _Hh3cRateLimitPIR_Type(Integer32):
    """Custom type hh3cRateLimitPIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34120000),
    )


_Hh3cRateLimitPIR_Type.__name__ = "Integer32"
_Hh3cRateLimitPIR_Object = MibTableColumn
hh3cRateLimitPIR = _Hh3cRateLimitPIR_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 17),
    _Hh3cRateLimitPIR_Type()
)
hh3cRateLimitPIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitPIR.setStatus("current")


class _Hh3cRateLimitConformLocalPre_Type(Integer32):
    """Custom type hh3cRateLimitConformLocalPre based on Integer32"""
    defaultValue = 1


_Hh3cRateLimitConformLocalPre_Object = MibTableColumn
hh3cRateLimitConformLocalPre = _Hh3cRateLimitConformLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 18),
    _Hh3cRateLimitConformLocalPre_Type()
)
hh3cRateLimitConformLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitConformLocalPre.setStatus("current")


class _Hh3cRateLimitConformActionType_Type(Integer32):
    """Custom type hh3cRateLimitConformActionType based on Integer32"""
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


_Hh3cRateLimitConformActionType_Type.__name__ = "Integer32"
_Hh3cRateLimitConformActionType_Object = MibTableColumn
hh3cRateLimitConformActionType = _Hh3cRateLimitConformActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 19),
    _Hh3cRateLimitConformActionType_Type()
)
hh3cRateLimitConformActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitConformActionType.setStatus("current")


class _Hh3cRateLimitExceedActionType_Type(Integer32):
    """Custom type hh3cRateLimitExceedActionType based on Integer32"""
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


_Hh3cRateLimitExceedActionType_Type.__name__ = "Integer32"
_Hh3cRateLimitExceedActionType_Object = MibTableColumn
hh3cRateLimitExceedActionType = _Hh3cRateLimitExceedActionType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 20),
    _Hh3cRateLimitExceedActionType_Type()
)
hh3cRateLimitExceedActionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitExceedActionType.setStatus("current")


class _Hh3cRateLimitExceedDscp_Type(Integer32):
    """Custom type hh3cRateLimitExceedDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRateLimitExceedDscp_Type.__name__ = "Integer32"
_Hh3cRateLimitExceedDscp_Object = MibTableColumn
hh3cRateLimitExceedDscp = _Hh3cRateLimitExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 21),
    _Hh3cRateLimitExceedDscp_Type()
)
hh3cRateLimitExceedDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitExceedDscp.setStatus("current")
_Hh3cRateLimitRuntime_Type = TruthValue
_Hh3cRateLimitRuntime_Object = MibTableColumn
hh3cRateLimitRuntime = _Hh3cRateLimitRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 22),
    _Hh3cRateLimitRuntime_Type()
)
hh3cRateLimitRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRateLimitRuntime.setStatus("current")
_Hh3cRateLimitRowStatus_Type = RowStatus
_Hh3cRateLimitRowStatus_Object = MibTableColumn
hh3cRateLimitRowStatus = _Hh3cRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 23),
    _Hh3cRateLimitRowStatus_Type()
)
hh3cRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitRowStatus.setStatus("current")


class _Hh3cRateLimitExceedCos_Type(Integer32):
    """Custom type hh3cRateLimitExceedCos based on Integer32"""
    defaultValue = 255


_Hh3cRateLimitExceedCos_Object = MibTableColumn
hh3cRateLimitExceedCos = _Hh3cRateLimitExceedCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 24),
    _Hh3cRateLimitExceedCos_Type()
)
hh3cRateLimitExceedCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitExceedCos.setStatus("current")


class _Hh3cRateLimitConformCos_Type(Integer32):
    """Custom type hh3cRateLimitConformCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRateLimitConformCos_Type.__name__ = "Integer32"
_Hh3cRateLimitConformCos_Object = MibTableColumn
hh3cRateLimitConformCos = _Hh3cRateLimitConformCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 25),
    _Hh3cRateLimitConformCos_Type()
)
hh3cRateLimitConformCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitConformCos.setStatus("current")


class _Hh3cRateLimitConformDscp_Type(Integer32):
    """Custom type hh3cRateLimitConformDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRateLimitConformDscp_Type.__name__ = "Integer32"
_Hh3cRateLimitConformDscp_Object = MibTableColumn
hh3cRateLimitConformDscp = _Hh3cRateLimitConformDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 26),
    _Hh3cRateLimitConformDscp_Type()
)
hh3cRateLimitConformDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitConformDscp.setStatus("current")
_Hh3cRateLimitMeterStatByteCount_Type = Counter64
_Hh3cRateLimitMeterStatByteCount_Object = MibTableColumn
hh3cRateLimitMeterStatByteCount = _Hh3cRateLimitMeterStatByteCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 27),
    _Hh3cRateLimitMeterStatByteCount_Type()
)
hh3cRateLimitMeterStatByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRateLimitMeterStatByteCount.setStatus("current")
_Hh3cRateLimitMeterStatByteXCount_Type = Counter64
_Hh3cRateLimitMeterStatByteXCount_Object = MibTableColumn
hh3cRateLimitMeterStatByteXCount = _Hh3cRateLimitMeterStatByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 28),
    _Hh3cRateLimitMeterStatByteXCount_Type()
)
hh3cRateLimitMeterStatByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRateLimitMeterStatByteXCount.setStatus("current")


class _Hh3cRateLimitMeterStatState_Type(Integer32):
    """Custom type hh3cRateLimitMeterStatState based on Integer32"""
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


_Hh3cRateLimitMeterStatState_Type.__name__ = "Integer32"
_Hh3cRateLimitMeterStatState_Object = MibTableColumn
hh3cRateLimitMeterStatState = _Hh3cRateLimitMeterStatState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 4, 1, 29),
    _Hh3cRateLimitMeterStatState_Type()
)
hh3cRateLimitMeterStatState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRateLimitMeterStatState.setStatus("current")
_Hh3cPriorityTable_Object = MibTable
hh3cPriorityTable = _Hh3cPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5)
)
if mibBuilder.loadTexts:
    hh3cPriorityTable.setStatus("current")
_Hh3cPriorityEntry_Object = MibTableRow
hh3cPriorityEntry = _Hh3cPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1)
)
hh3cPriorityEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cPriorityAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cPriorityIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cPriorityVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cPriorityDirection"),
)
if mibBuilder.loadTexts:
    hh3cPriorityEntry.setStatus("current")


class _Hh3cPriorityAclIndex_Type(Integer32):
    """Custom type hh3cPriorityAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cPriorityAclIndex_Type.__name__ = "Integer32"
_Hh3cPriorityAclIndex_Object = MibTableColumn
hh3cPriorityAclIndex = _Hh3cPriorityAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 1),
    _Hh3cPriorityAclIndex_Type()
)
hh3cPriorityAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityAclIndex.setStatus("current")
_Hh3cPriorityIfIndex_Type = Integer32
_Hh3cPriorityIfIndex_Object = MibTableColumn
hh3cPriorityIfIndex = _Hh3cPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 2),
    _Hh3cPriorityIfIndex_Type()
)
hh3cPriorityIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityIfIndex.setStatus("current")


class _Hh3cPriorityVlanID_Type(Integer32):
    """Custom type hh3cPriorityVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cPriorityVlanID_Type.__name__ = "Integer32"
_Hh3cPriorityVlanID_Object = MibTableColumn
hh3cPriorityVlanID = _Hh3cPriorityVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 3),
    _Hh3cPriorityVlanID_Type()
)
hh3cPriorityVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityVlanID.setStatus("current")


class _Hh3cPriorityDirection_Type(Integer32):
    """Custom type hh3cPriorityDirection based on Integer32"""
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


_Hh3cPriorityDirection_Type.__name__ = "Integer32"
_Hh3cPriorityDirection_Object = MibTableColumn
hh3cPriorityDirection = _Hh3cPriorityDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 4),
    _Hh3cPriorityDirection_Type()
)
hh3cPriorityDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityDirection.setStatus("current")


class _Hh3cPriorityUserAclNum_Type(Integer32):
    """Custom type hh3cPriorityUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cPriorityUserAclNum_Type.__name__ = "Integer32"
_Hh3cPriorityUserAclNum_Object = MibTableColumn
hh3cPriorityUserAclNum = _Hh3cPriorityUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 5),
    _Hh3cPriorityUserAclNum_Type()
)
hh3cPriorityUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityUserAclNum.setStatus("current")


class _Hh3cPriorityUserAclRule_Type(Integer32):
    """Custom type hh3cPriorityUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPriorityUserAclRule_Type.__name__ = "Integer32"
_Hh3cPriorityUserAclRule_Object = MibTableColumn
hh3cPriorityUserAclRule = _Hh3cPriorityUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 6),
    _Hh3cPriorityUserAclRule_Type()
)
hh3cPriorityUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityUserAclRule.setStatus("current")


class _Hh3cPriorityIpAclNum_Type(Integer32):
    """Custom type hh3cPriorityIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cPriorityIpAclNum_Type.__name__ = "Integer32"
_Hh3cPriorityIpAclNum_Object = MibTableColumn
hh3cPriorityIpAclNum = _Hh3cPriorityIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 7),
    _Hh3cPriorityIpAclNum_Type()
)
hh3cPriorityIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityIpAclNum.setStatus("current")


class _Hh3cPriorityIpAclRule_Type(Integer32):
    """Custom type hh3cPriorityIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPriorityIpAclRule_Type.__name__ = "Integer32"
_Hh3cPriorityIpAclRule_Object = MibTableColumn
hh3cPriorityIpAclRule = _Hh3cPriorityIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 8),
    _Hh3cPriorityIpAclRule_Type()
)
hh3cPriorityIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityIpAclRule.setStatus("current")


class _Hh3cPriorityLinkAclNum_Type(Integer32):
    """Custom type hh3cPriorityLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cPriorityLinkAclNum_Type.__name__ = "Integer32"
_Hh3cPriorityLinkAclNum_Object = MibTableColumn
hh3cPriorityLinkAclNum = _Hh3cPriorityLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 9),
    _Hh3cPriorityLinkAclNum_Type()
)
hh3cPriorityLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityLinkAclNum.setStatus("current")


class _Hh3cPriorityLinkAclRule_Type(Integer32):
    """Custom type hh3cPriorityLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cPriorityLinkAclRule_Type.__name__ = "Integer32"
_Hh3cPriorityLinkAclRule_Object = MibTableColumn
hh3cPriorityLinkAclRule = _Hh3cPriorityLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 10),
    _Hh3cPriorityLinkAclRule_Type()
)
hh3cPriorityLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityLinkAclRule.setStatus("current")


class _Hh3cPriorityDscp_Type(Integer32):
    """Custom type hh3cPriorityDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityDscp_Type.__name__ = "Integer32"
_Hh3cPriorityDscp_Object = MibTableColumn
hh3cPriorityDscp = _Hh3cPriorityDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 11),
    _Hh3cPriorityDscp_Type()
)
hh3cPriorityDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityDscp.setStatus("current")


class _Hh3cPriorityIpPre_Type(Integer32):
    """Custom type hh3cPriorityIpPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityIpPre_Type.__name__ = "Integer32"
_Hh3cPriorityIpPre_Object = MibTableColumn
hh3cPriorityIpPre = _Hh3cPriorityIpPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 12),
    _Hh3cPriorityIpPre_Type()
)
hh3cPriorityIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityIpPre.setStatus("current")


class _Hh3cPriorityIpPreFromCos_Type(TruthValue):
    """Custom type hh3cPriorityIpPreFromCos based on TruthValue"""
    defaultValue = 2


_Hh3cPriorityIpPreFromCos_Object = MibTableColumn
hh3cPriorityIpPreFromCos = _Hh3cPriorityIpPreFromCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 13),
    _Hh3cPriorityIpPreFromCos_Type()
)
hh3cPriorityIpPreFromCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityIpPreFromCos.setStatus("current")


class _Hh3cPriorityCos_Type(Integer32):
    """Custom type hh3cPriorityCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityCos_Type.__name__ = "Integer32"
_Hh3cPriorityCos_Object = MibTableColumn
hh3cPriorityCos = _Hh3cPriorityCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 14),
    _Hh3cPriorityCos_Type()
)
hh3cPriorityCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityCos.setStatus("current")


class _Hh3cPriorityCosFromIpPre_Type(TruthValue):
    """Custom type hh3cPriorityCosFromIpPre based on TruthValue"""
    defaultValue = 2


_Hh3cPriorityCosFromIpPre_Object = MibTableColumn
hh3cPriorityCosFromIpPre = _Hh3cPriorityCosFromIpPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 15),
    _Hh3cPriorityCosFromIpPre_Type()
)
hh3cPriorityCosFromIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityCosFromIpPre.setStatus("current")


class _Hh3cPriorityLocalPre_Type(Integer32):
    """Custom type hh3cPriorityLocalPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityLocalPre_Type.__name__ = "Integer32"
_Hh3cPriorityLocalPre_Object = MibTableColumn
hh3cPriorityLocalPre = _Hh3cPriorityLocalPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 16),
    _Hh3cPriorityLocalPre_Type()
)
hh3cPriorityLocalPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityLocalPre.setStatus("current")


class _Hh3cPriorityPolicedServiceType_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceType based on Integer32"""
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


_Hh3cPriorityPolicedServiceType_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceType_Object = MibTableColumn
hh3cPriorityPolicedServiceType = _Hh3cPriorityPolicedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 17),
    _Hh3cPriorityPolicedServiceType_Type()
)
hh3cPriorityPolicedServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceType.setStatus("current")


class _Hh3cPriorityPolicedServiceDscp_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceDscp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityPolicedServiceDscp_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceDscp_Object = MibTableColumn
hh3cPriorityPolicedServiceDscp = _Hh3cPriorityPolicedServiceDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 18),
    _Hh3cPriorityPolicedServiceDscp_Type()
)
hh3cPriorityPolicedServiceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceDscp.setStatus("current")


class _Hh3cPriorityPolicedServiceExp_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceExp based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityPolicedServiceExp_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceExp_Object = MibTableColumn
hh3cPriorityPolicedServiceExp = _Hh3cPriorityPolicedServiceExp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 19),
    _Hh3cPriorityPolicedServiceExp_Type()
)
hh3cPriorityPolicedServiceExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceExp.setStatus("current")


class _Hh3cPriorityPolicedServiceCos_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceCos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityPolicedServiceCos_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceCos_Object = MibTableColumn
hh3cPriorityPolicedServiceCos = _Hh3cPriorityPolicedServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 20),
    _Hh3cPriorityPolicedServiceCos_Type()
)
hh3cPriorityPolicedServiceCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceCos.setStatus("current")


class _Hh3cPriorityPolicedServiceLoaclPre_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceLoaclPre based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityPolicedServiceLoaclPre_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceLoaclPre_Object = MibTableColumn
hh3cPriorityPolicedServiceLoaclPre = _Hh3cPriorityPolicedServiceLoaclPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 21),
    _Hh3cPriorityPolicedServiceLoaclPre_Type()
)
hh3cPriorityPolicedServiceLoaclPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceLoaclPre.setStatus("current")


class _Hh3cPriorityPolicedServiceDropPriority_Type(Integer32):
    """Custom type hh3cPriorityPolicedServiceDropPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
        ValueRangeConstraint(255, 255),
    )


_Hh3cPriorityPolicedServiceDropPriority_Type.__name__ = "Integer32"
_Hh3cPriorityPolicedServiceDropPriority_Object = MibTableColumn
hh3cPriorityPolicedServiceDropPriority = _Hh3cPriorityPolicedServiceDropPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 22),
    _Hh3cPriorityPolicedServiceDropPriority_Type()
)
hh3cPriorityPolicedServiceDropPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityPolicedServiceDropPriority.setStatus("current")
_Hh3cPriorityRuntime_Type = TruthValue
_Hh3cPriorityRuntime_Object = MibTableColumn
hh3cPriorityRuntime = _Hh3cPriorityRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 23),
    _Hh3cPriorityRuntime_Type()
)
hh3cPriorityRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPriorityRuntime.setStatus("current")
_Hh3cPriorityRowStatus_Type = RowStatus
_Hh3cPriorityRowStatus_Object = MibTableColumn
hh3cPriorityRowStatus = _Hh3cPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 5, 1, 24),
    _Hh3cPriorityRowStatus_Type()
)
hh3cPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPriorityRowStatus.setStatus("current")
_Hh3cRedirectTable_Object = MibTable
hh3cRedirectTable = _Hh3cRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cRedirectTable.setStatus("current")
_Hh3cRedirectEntry_Object = MibTableRow
hh3cRedirectEntry = _Hh3cRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1)
)
hh3cRedirectEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cRedirectAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRedirectIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRedirectVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cRedirectDirection"),
)
if mibBuilder.loadTexts:
    hh3cRedirectEntry.setStatus("current")


class _Hh3cRedirectAclIndex_Type(Integer32):
    """Custom type hh3cRedirectAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cRedirectAclIndex_Type.__name__ = "Integer32"
_Hh3cRedirectAclIndex_Object = MibTableColumn
hh3cRedirectAclIndex = _Hh3cRedirectAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 1),
    _Hh3cRedirectAclIndex_Type()
)
hh3cRedirectAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectAclIndex.setStatus("current")
_Hh3cRedirectIfIndex_Type = Integer32
_Hh3cRedirectIfIndex_Object = MibTableColumn
hh3cRedirectIfIndex = _Hh3cRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 2),
    _Hh3cRedirectIfIndex_Type()
)
hh3cRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectIfIndex.setStatus("current")


class _Hh3cRedirectVlanID_Type(Integer32):
    """Custom type hh3cRedirectVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRedirectVlanID_Type.__name__ = "Integer32"
_Hh3cRedirectVlanID_Object = MibTableColumn
hh3cRedirectVlanID = _Hh3cRedirectVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 3),
    _Hh3cRedirectVlanID_Type()
)
hh3cRedirectVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectVlanID.setStatus("current")


class _Hh3cRedirectDirection_Type(Integer32):
    """Custom type hh3cRedirectDirection based on Integer32"""
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


_Hh3cRedirectDirection_Type.__name__ = "Integer32"
_Hh3cRedirectDirection_Object = MibTableColumn
hh3cRedirectDirection = _Hh3cRedirectDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 4),
    _Hh3cRedirectDirection_Type()
)
hh3cRedirectDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectDirection.setStatus("current")


class _Hh3cRedirectUserAclNum_Type(Integer32):
    """Custom type hh3cRedirectUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRedirectUserAclNum_Type.__name__ = "Integer32"
_Hh3cRedirectUserAclNum_Object = MibTableColumn
hh3cRedirectUserAclNum = _Hh3cRedirectUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 5),
    _Hh3cRedirectUserAclNum_Type()
)
hh3cRedirectUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectUserAclNum.setStatus("current")


class _Hh3cRedirectUserAclRule_Type(Integer32):
    """Custom type hh3cRedirectUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRedirectUserAclRule_Type.__name__ = "Integer32"
_Hh3cRedirectUserAclRule_Object = MibTableColumn
hh3cRedirectUserAclRule = _Hh3cRedirectUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 6),
    _Hh3cRedirectUserAclRule_Type()
)
hh3cRedirectUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectUserAclRule.setStatus("current")


class _Hh3cRedirectIpAclNum_Type(Integer32):
    """Custom type hh3cRedirectIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRedirectIpAclNum_Type.__name__ = "Integer32"
_Hh3cRedirectIpAclNum_Object = MibTableColumn
hh3cRedirectIpAclNum = _Hh3cRedirectIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 7),
    _Hh3cRedirectIpAclNum_Type()
)
hh3cRedirectIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectIpAclNum.setStatus("current")


class _Hh3cRedirectIpAclRule_Type(Integer32):
    """Custom type hh3cRedirectIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRedirectIpAclRule_Type.__name__ = "Integer32"
_Hh3cRedirectIpAclRule_Object = MibTableColumn
hh3cRedirectIpAclRule = _Hh3cRedirectIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 8),
    _Hh3cRedirectIpAclRule_Type()
)
hh3cRedirectIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectIpAclRule.setStatus("current")


class _Hh3cRedirectLinkAclNum_Type(Integer32):
    """Custom type hh3cRedirectLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRedirectLinkAclNum_Type.__name__ = "Integer32"
_Hh3cRedirectLinkAclNum_Object = MibTableColumn
hh3cRedirectLinkAclNum = _Hh3cRedirectLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 9),
    _Hh3cRedirectLinkAclNum_Type()
)
hh3cRedirectLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectLinkAclNum.setStatus("current")


class _Hh3cRedirectLinkAclRule_Type(Integer32):
    """Custom type hh3cRedirectLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRedirectLinkAclRule_Type.__name__ = "Integer32"
_Hh3cRedirectLinkAclRule_Object = MibTableColumn
hh3cRedirectLinkAclRule = _Hh3cRedirectLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 10),
    _Hh3cRedirectLinkAclRule_Type()
)
hh3cRedirectLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectLinkAclRule.setStatus("current")


class _Hh3cRedirectToCpu_Type(TruthValue):
    """Custom type hh3cRedirectToCpu based on TruthValue"""
    defaultValue = 2


_Hh3cRedirectToCpu_Object = MibTableColumn
hh3cRedirectToCpu = _Hh3cRedirectToCpu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 11),
    _Hh3cRedirectToCpu_Type()
)
hh3cRedirectToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToCpu.setStatus("current")
_Hh3cRedirectToIfIndex_Type = Integer32
_Hh3cRedirectToIfIndex_Object = MibTableColumn
hh3cRedirectToIfIndex = _Hh3cRedirectToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 12),
    _Hh3cRedirectToIfIndex_Type()
)
hh3cRedirectToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToIfIndex.setStatus("current")
_Hh3cRedirectToNextHop1_Type = IpAddress
_Hh3cRedirectToNextHop1_Object = MibTableColumn
hh3cRedirectToNextHop1 = _Hh3cRedirectToNextHop1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 13),
    _Hh3cRedirectToNextHop1_Type()
)
hh3cRedirectToNextHop1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToNextHop1.setStatus("current")
_Hh3cRedirectToNextHop2_Type = IpAddress
_Hh3cRedirectToNextHop2_Object = MibTableColumn
hh3cRedirectToNextHop2 = _Hh3cRedirectToNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 14),
    _Hh3cRedirectToNextHop2_Type()
)
hh3cRedirectToNextHop2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToNextHop2.setStatus("current")
_Hh3cRedirectRuntime_Type = TruthValue
_Hh3cRedirectRuntime_Object = MibTableColumn
hh3cRedirectRuntime = _Hh3cRedirectRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 15),
    _Hh3cRedirectRuntime_Type()
)
hh3cRedirectRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRedirectRuntime.setStatus("current")
_Hh3cRedirectRowStatus_Type = RowStatus
_Hh3cRedirectRowStatus_Object = MibTableColumn
hh3cRedirectRowStatus = _Hh3cRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 16),
    _Hh3cRedirectRowStatus_Type()
)
hh3cRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectRowStatus.setStatus("current")


class _Hh3cRedirectToSlotNo_Type(Integer32):
    """Custom type hh3cRedirectToSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cRedirectToSlotNo_Type.__name__ = "Integer32"
_Hh3cRedirectToSlotNo_Object = MibTableColumn
hh3cRedirectToSlotNo = _Hh3cRedirectToSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 17),
    _Hh3cRedirectToSlotNo_Type()
)
hh3cRedirectToSlotNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToSlotNo.setStatus("current")


class _Hh3cRedirectRemarkedDSCP_Type(Integer32):
    """Custom type hh3cRedirectRemarkedDSCP based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRedirectRemarkedDSCP_Type.__name__ = "Integer32"
_Hh3cRedirectRemarkedDSCP_Object = MibTableColumn
hh3cRedirectRemarkedDSCP = _Hh3cRedirectRemarkedDSCP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 18),
    _Hh3cRedirectRemarkedDSCP_Type()
)
hh3cRedirectRemarkedDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectRemarkedDSCP.setStatus("current")


class _Hh3cRedirectRemarkedPri_Type(Integer32):
    """Custom type hh3cRedirectRemarkedPri based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRedirectRemarkedPri_Type.__name__ = "Integer32"
_Hh3cRedirectRemarkedPri_Object = MibTableColumn
hh3cRedirectRemarkedPri = _Hh3cRedirectRemarkedPri_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 19),
    _Hh3cRedirectRemarkedPri_Type()
)
hh3cRedirectRemarkedPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectRemarkedPri.setStatus("current")


class _Hh3cRedirectRemarkedTos_Type(Integer32):
    """Custom type hh3cRedirectRemarkedTos based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
        ValueRangeConstraint(255, 255),
    )


_Hh3cRedirectRemarkedTos_Type.__name__ = "Integer32"
_Hh3cRedirectRemarkedTos_Object = MibTableColumn
hh3cRedirectRemarkedTos = _Hh3cRedirectRemarkedTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 20),
    _Hh3cRedirectRemarkedTos_Type()
)
hh3cRedirectRemarkedTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectRemarkedTos.setStatus("current")
_Hh3cRedirectToNextHop3_Type = IpAddress
_Hh3cRedirectToNextHop3_Object = MibTableColumn
hh3cRedirectToNextHop3 = _Hh3cRedirectToNextHop3_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 21),
    _Hh3cRedirectToNextHop3_Type()
)
hh3cRedirectToNextHop3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToNextHop3.setStatus("current")


class _Hh3cRedirectTargetVlanID_Type(Integer32):
    """Custom type hh3cRedirectTargetVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRedirectTargetVlanID_Type.__name__ = "Integer32"
_Hh3cRedirectTargetVlanID_Object = MibTableColumn
hh3cRedirectTargetVlanID = _Hh3cRedirectTargetVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 22),
    _Hh3cRedirectTargetVlanID_Type()
)
hh3cRedirectTargetVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectTargetVlanID.setStatus("current")


class _Hh3cRedirectMode_Type(Integer32):
    """Custom type hh3cRedirectMode based on Integer32"""
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


_Hh3cRedirectMode_Type.__name__ = "Integer32"
_Hh3cRedirectMode_Object = MibTableColumn
hh3cRedirectMode = _Hh3cRedirectMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 23),
    _Hh3cRedirectMode_Type()
)
hh3cRedirectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectMode.setStatus("current")


class _Hh3cRedirectToNestedVlanID_Type(Integer32):
    """Custom type hh3cRedirectToNestedVlanID based on Integer32"""
    defaultValue = 0


_Hh3cRedirectToNestedVlanID_Object = MibTableColumn
hh3cRedirectToNestedVlanID = _Hh3cRedirectToNestedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 24),
    _Hh3cRedirectToNestedVlanID_Type()
)
hh3cRedirectToNestedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToNestedVlanID.setStatus("current")


class _Hh3cRedirectToModifiedVlanID_Type(Integer32):
    """Custom type hh3cRedirectToModifiedVlanID based on Integer32"""
    defaultValue = 0


_Hh3cRedirectToModifiedVlanID_Object = MibTableColumn
hh3cRedirectToModifiedVlanID = _Hh3cRedirectToModifiedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 6, 1, 25),
    _Hh3cRedirectToModifiedVlanID_Type()
)
hh3cRedirectToModifiedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedirectToModifiedVlanID.setStatus("current")
_Hh3cStatisticTable_Object = MibTable
hh3cStatisticTable = _Hh3cStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cStatisticTable.setStatus("current")
_Hh3cStatisticEntry_Object = MibTableRow
hh3cStatisticEntry = _Hh3cStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1)
)
hh3cStatisticEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cStatisticAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cStatisticIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cStatisticVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cStatisticDirection"),
)
if mibBuilder.loadTexts:
    hh3cStatisticEntry.setStatus("current")


class _Hh3cStatisticAclIndex_Type(Integer32):
    """Custom type hh3cStatisticAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cStatisticAclIndex_Type.__name__ = "Integer32"
_Hh3cStatisticAclIndex_Object = MibTableColumn
hh3cStatisticAclIndex = _Hh3cStatisticAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 1),
    _Hh3cStatisticAclIndex_Type()
)
hh3cStatisticAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticAclIndex.setStatus("current")
_Hh3cStatisticIfIndex_Type = Integer32
_Hh3cStatisticIfIndex_Object = MibTableColumn
hh3cStatisticIfIndex = _Hh3cStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 2),
    _Hh3cStatisticIfIndex_Type()
)
hh3cStatisticIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticIfIndex.setStatus("current")


class _Hh3cStatisticVlanID_Type(Integer32):
    """Custom type hh3cStatisticVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cStatisticVlanID_Type.__name__ = "Integer32"
_Hh3cStatisticVlanID_Object = MibTableColumn
hh3cStatisticVlanID = _Hh3cStatisticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 3),
    _Hh3cStatisticVlanID_Type()
)
hh3cStatisticVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticVlanID.setStatus("current")


class _Hh3cStatisticDirection_Type(Integer32):
    """Custom type hh3cStatisticDirection based on Integer32"""
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


_Hh3cStatisticDirection_Type.__name__ = "Integer32"
_Hh3cStatisticDirection_Object = MibTableColumn
hh3cStatisticDirection = _Hh3cStatisticDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 4),
    _Hh3cStatisticDirection_Type()
)
hh3cStatisticDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticDirection.setStatus("current")


class _Hh3cStatisticUserAclNum_Type(Integer32):
    """Custom type hh3cStatisticUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cStatisticUserAclNum_Type.__name__ = "Integer32"
_Hh3cStatisticUserAclNum_Object = MibTableColumn
hh3cStatisticUserAclNum = _Hh3cStatisticUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 5),
    _Hh3cStatisticUserAclNum_Type()
)
hh3cStatisticUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticUserAclNum.setStatus("current")


class _Hh3cStatisticUserAclRule_Type(Integer32):
    """Custom type hh3cStatisticUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cStatisticUserAclRule_Type.__name__ = "Integer32"
_Hh3cStatisticUserAclRule_Object = MibTableColumn
hh3cStatisticUserAclRule = _Hh3cStatisticUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 6),
    _Hh3cStatisticUserAclRule_Type()
)
hh3cStatisticUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticUserAclRule.setStatus("current")


class _Hh3cStatisticIpAclNum_Type(Integer32):
    """Custom type hh3cStatisticIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cStatisticIpAclNum_Type.__name__ = "Integer32"
_Hh3cStatisticIpAclNum_Object = MibTableColumn
hh3cStatisticIpAclNum = _Hh3cStatisticIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 7),
    _Hh3cStatisticIpAclNum_Type()
)
hh3cStatisticIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticIpAclNum.setStatus("current")


class _Hh3cStatisticIpAclRule_Type(Integer32):
    """Custom type hh3cStatisticIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cStatisticIpAclRule_Type.__name__ = "Integer32"
_Hh3cStatisticIpAclRule_Object = MibTableColumn
hh3cStatisticIpAclRule = _Hh3cStatisticIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 8),
    _Hh3cStatisticIpAclRule_Type()
)
hh3cStatisticIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticIpAclRule.setStatus("current")


class _Hh3cStatisticLinkAclNum_Type(Integer32):
    """Custom type hh3cStatisticLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cStatisticLinkAclNum_Type.__name__ = "Integer32"
_Hh3cStatisticLinkAclNum_Object = MibTableColumn
hh3cStatisticLinkAclNum = _Hh3cStatisticLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 9),
    _Hh3cStatisticLinkAclNum_Type()
)
hh3cStatisticLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticLinkAclNum.setStatus("current")


class _Hh3cStatisticLinkAclRule_Type(Integer32):
    """Custom type hh3cStatisticLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cStatisticLinkAclRule_Type.__name__ = "Integer32"
_Hh3cStatisticLinkAclRule_Object = MibTableColumn
hh3cStatisticLinkAclRule = _Hh3cStatisticLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 10),
    _Hh3cStatisticLinkAclRule_Type()
)
hh3cStatisticLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticLinkAclRule.setStatus("current")
_Hh3cStatisticRuntime_Type = TruthValue
_Hh3cStatisticRuntime_Object = MibTableColumn
hh3cStatisticRuntime = _Hh3cStatisticRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 11),
    _Hh3cStatisticRuntime_Type()
)
hh3cStatisticRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStatisticRuntime.setStatus("current")
_Hh3cStatisticPacketCount_Type = Counter64
_Hh3cStatisticPacketCount_Object = MibTableColumn
hh3cStatisticPacketCount = _Hh3cStatisticPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 12),
    _Hh3cStatisticPacketCount_Type()
)
hh3cStatisticPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStatisticPacketCount.setStatus("current")
_Hh3cStatisticByteCount_Type = Counter64
_Hh3cStatisticByteCount_Object = MibTableColumn
hh3cStatisticByteCount = _Hh3cStatisticByteCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 13),
    _Hh3cStatisticByteCount_Type()
)
hh3cStatisticByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStatisticByteCount.setStatus("current")


class _Hh3cStatisticCountClear_Type(Integer32):
    """Custom type hh3cStatisticCountClear based on Integer32"""
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


_Hh3cStatisticCountClear_Type.__name__ = "Integer32"
_Hh3cStatisticCountClear_Object = MibTableColumn
hh3cStatisticCountClear = _Hh3cStatisticCountClear_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 14),
    _Hh3cStatisticCountClear_Type()
)
hh3cStatisticCountClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cStatisticCountClear.setStatus("current")
_Hh3cStatisticRowStatus_Type = RowStatus
_Hh3cStatisticRowStatus_Object = MibTableColumn
hh3cStatisticRowStatus = _Hh3cStatisticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 15),
    _Hh3cStatisticRowStatus_Type()
)
hh3cStatisticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cStatisticRowStatus.setStatus("current")
_Hh3cStatisticPacketXCount_Type = Counter64
_Hh3cStatisticPacketXCount_Object = MibTableColumn
hh3cStatisticPacketXCount = _Hh3cStatisticPacketXCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 16),
    _Hh3cStatisticPacketXCount_Type()
)
hh3cStatisticPacketXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStatisticPacketXCount.setStatus("current")
_Hh3cStatisticByteXCount_Type = Counter64
_Hh3cStatisticByteXCount_Object = MibTableColumn
hh3cStatisticByteXCount = _Hh3cStatisticByteXCount_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 7, 1, 17),
    _Hh3cStatisticByteXCount_Type()
)
hh3cStatisticByteXCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cStatisticByteXCount.setStatus("current")
_Hh3cMirrorTable_Object = MibTable
hh3cMirrorTable = _Hh3cMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cMirrorTable.setStatus("current")
_Hh3cMirrorEntry_Object = MibTableRow
hh3cMirrorEntry = _Hh3cMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1)
)
hh3cMirrorEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirrorAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cMirrorIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cMirrorVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cMirrorDirection"),
)
if mibBuilder.loadTexts:
    hh3cMirrorEntry.setStatus("current")


class _Hh3cMirrorAclIndex_Type(Integer32):
    """Custom type hh3cMirrorAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cMirrorAclIndex_Type.__name__ = "Integer32"
_Hh3cMirrorAclIndex_Object = MibTableColumn
hh3cMirrorAclIndex = _Hh3cMirrorAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 1),
    _Hh3cMirrorAclIndex_Type()
)
hh3cMirrorAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorAclIndex.setStatus("current")
_Hh3cMirrorIfIndex_Type = Integer32
_Hh3cMirrorIfIndex_Object = MibTableColumn
hh3cMirrorIfIndex = _Hh3cMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 2),
    _Hh3cMirrorIfIndex_Type()
)
hh3cMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorIfIndex.setStatus("current")


class _Hh3cMirrorVlanID_Type(Integer32):
    """Custom type hh3cMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cMirrorVlanID_Type.__name__ = "Integer32"
_Hh3cMirrorVlanID_Object = MibTableColumn
hh3cMirrorVlanID = _Hh3cMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 3),
    _Hh3cMirrorVlanID_Type()
)
hh3cMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorVlanID.setStatus("current")


class _Hh3cMirrorDirection_Type(Integer32):
    """Custom type hh3cMirrorDirection based on Integer32"""
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


_Hh3cMirrorDirection_Type.__name__ = "Integer32"
_Hh3cMirrorDirection_Object = MibTableColumn
hh3cMirrorDirection = _Hh3cMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 4),
    _Hh3cMirrorDirection_Type()
)
hh3cMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorDirection.setStatus("current")


class _Hh3cMirrorUserAclNum_Type(Integer32):
    """Custom type hh3cMirrorUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cMirrorUserAclNum_Type.__name__ = "Integer32"
_Hh3cMirrorUserAclNum_Object = MibTableColumn
hh3cMirrorUserAclNum = _Hh3cMirrorUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 5),
    _Hh3cMirrorUserAclNum_Type()
)
hh3cMirrorUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorUserAclNum.setStatus("current")


class _Hh3cMirrorUserAclRule_Type(Integer32):
    """Custom type hh3cMirrorUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMirrorUserAclRule_Type.__name__ = "Integer32"
_Hh3cMirrorUserAclRule_Object = MibTableColumn
hh3cMirrorUserAclRule = _Hh3cMirrorUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 6),
    _Hh3cMirrorUserAclRule_Type()
)
hh3cMirrorUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorUserAclRule.setStatus("current")


class _Hh3cMirrorIpAclNum_Type(Integer32):
    """Custom type hh3cMirrorIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cMirrorIpAclNum_Type.__name__ = "Integer32"
_Hh3cMirrorIpAclNum_Object = MibTableColumn
hh3cMirrorIpAclNum = _Hh3cMirrorIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 7),
    _Hh3cMirrorIpAclNum_Type()
)
hh3cMirrorIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorIpAclNum.setStatus("current")


class _Hh3cMirrorIpAclRule_Type(Integer32):
    """Custom type hh3cMirrorIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMirrorIpAclRule_Type.__name__ = "Integer32"
_Hh3cMirrorIpAclRule_Object = MibTableColumn
hh3cMirrorIpAclRule = _Hh3cMirrorIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 8),
    _Hh3cMirrorIpAclRule_Type()
)
hh3cMirrorIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorIpAclRule.setStatus("current")


class _Hh3cMirrorLinkAclNum_Type(Integer32):
    """Custom type hh3cMirrorLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cMirrorLinkAclNum_Type.__name__ = "Integer32"
_Hh3cMirrorLinkAclNum_Object = MibTableColumn
hh3cMirrorLinkAclNum = _Hh3cMirrorLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 9),
    _Hh3cMirrorLinkAclNum_Type()
)
hh3cMirrorLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorLinkAclNum.setStatus("current")


class _Hh3cMirrorLinkAclRule_Type(Integer32):
    """Custom type hh3cMirrorLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cMirrorLinkAclRule_Type.__name__ = "Integer32"
_Hh3cMirrorLinkAclRule_Object = MibTableColumn
hh3cMirrorLinkAclRule = _Hh3cMirrorLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 10),
    _Hh3cMirrorLinkAclRule_Type()
)
hh3cMirrorLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorLinkAclRule.setStatus("current")
_Hh3cMirrorToIfIndex_Type = Integer32
_Hh3cMirrorToIfIndex_Object = MibTableColumn
hh3cMirrorToIfIndex = _Hh3cMirrorToIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 11),
    _Hh3cMirrorToIfIndex_Type()
)
hh3cMirrorToIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorToIfIndex.setStatus("current")
_Hh3cMirrorToCpu_Type = TruthValue
_Hh3cMirrorToCpu_Object = MibTableColumn
hh3cMirrorToCpu = _Hh3cMirrorToCpu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 12),
    _Hh3cMirrorToCpu_Type()
)
hh3cMirrorToCpu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorToCpu.setStatus("current")
_Hh3cMirrorRuntime_Type = TruthValue
_Hh3cMirrorRuntime_Object = MibTableColumn
hh3cMirrorRuntime = _Hh3cMirrorRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 13),
    _Hh3cMirrorRuntime_Type()
)
hh3cMirrorRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorRuntime.setStatus("current")
_Hh3cMirrorRowStatus_Type = RowStatus
_Hh3cMirrorRowStatus_Object = MibTableColumn
hh3cMirrorRowStatus = _Hh3cMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 14),
    _Hh3cMirrorRowStatus_Type()
)
hh3cMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorRowStatus.setStatus("current")
_Hh3cMirrorToGroup_Type = Integer32
_Hh3cMirrorToGroup_Object = MibTableColumn
hh3cMirrorToGroup = _Hh3cMirrorToGroup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 8, 1, 15),
    _Hh3cMirrorToGroup_Type()
)
hh3cMirrorToGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorToGroup.setStatus("current")
_Hh3cPortMirrorTable_Object = MibTable
hh3cPortMirrorTable = _Hh3cPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 9)
)
if mibBuilder.loadTexts:
    hh3cPortMirrorTable.setStatus("current")
_Hh3cPortMirrorEntry_Object = MibTableRow
hh3cPortMirrorEntry = _Hh3cPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 9, 1)
)
hh3cPortMirrorEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cPortMirrorIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortMirrorEntry.setStatus("current")
_Hh3cPortMirrorIfIndex_Type = Integer32
_Hh3cPortMirrorIfIndex_Object = MibTableColumn
hh3cPortMirrorIfIndex = _Hh3cPortMirrorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 9, 1, 1),
    _Hh3cPortMirrorIfIndex_Type()
)
hh3cPortMirrorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortMirrorIfIndex.setStatus("current")


class _Hh3cPortMirrorDirection_Type(Integer32):
    """Custom type hh3cPortMirrorDirection based on Integer32"""
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


_Hh3cPortMirrorDirection_Type.__name__ = "Integer32"
_Hh3cPortMirrorDirection_Object = MibTableColumn
hh3cPortMirrorDirection = _Hh3cPortMirrorDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 9, 1, 2),
    _Hh3cPortMirrorDirection_Type()
)
hh3cPortMirrorDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortMirrorDirection.setStatus("current")
_Hh3cPortMirrorRowStatus_Type = RowStatus
_Hh3cPortMirrorRowStatus_Object = MibTableColumn
hh3cPortMirrorRowStatus = _Hh3cPortMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 9, 1, 3),
    _Hh3cPortMirrorRowStatus_Type()
)
hh3cPortMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortMirrorRowStatus.setStatus("current")
_Hh3cLineRateTable_Object = MibTable
hh3cLineRateTable = _Hh3cLineRateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10)
)
if mibBuilder.loadTexts:
    hh3cLineRateTable.setStatus("current")
_Hh3cLineRateEntry_Object = MibTableRow
hh3cLineRateEntry = _Hh3cLineRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10, 1)
)
hh3cLineRateEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cLineRateIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cLineRateDirection"),
)
if mibBuilder.loadTexts:
    hh3cLineRateEntry.setStatus("current")
_Hh3cLineRateIfIndex_Type = Integer32
_Hh3cLineRateIfIndex_Object = MibTableColumn
hh3cLineRateIfIndex = _Hh3cLineRateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10, 1, 1),
    _Hh3cLineRateIfIndex_Type()
)
hh3cLineRateIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLineRateIfIndex.setStatus("current")


class _Hh3cLineRateDirection_Type(Integer32):
    """Custom type hh3cLineRateDirection based on Integer32"""
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


_Hh3cLineRateDirection_Type.__name__ = "Integer32"
_Hh3cLineRateDirection_Object = MibTableColumn
hh3cLineRateDirection = _Hh3cLineRateDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10, 1, 2),
    _Hh3cLineRateDirection_Type()
)
hh3cLineRateDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLineRateDirection.setStatus("current")
_Hh3cLineRateValue_Type = Integer32
_Hh3cLineRateValue_Object = MibTableColumn
hh3cLineRateValue = _Hh3cLineRateValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10, 1, 3),
    _Hh3cLineRateValue_Type()
)
hh3cLineRateValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLineRateValue.setStatus("current")
_Hh3cLineRateRowStatus_Type = RowStatus
_Hh3cLineRateRowStatus_Object = MibTableColumn
hh3cLineRateRowStatus = _Hh3cLineRateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 10, 1, 4),
    _Hh3cLineRateRowStatus_Type()
)
hh3cLineRateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cLineRateRowStatus.setStatus("current")
_Hh3cBandwidthTable_Object = MibTable
hh3cBandwidthTable = _Hh3cBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11)
)
if mibBuilder.loadTexts:
    hh3cBandwidthTable.setStatus("current")
_Hh3cBandwidthEntry_Object = MibTableRow
hh3cBandwidthEntry = _Hh3cBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1)
)
hh3cBandwidthEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cBandwidthAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cBandwidthIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cBandwidthVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cBandwidthDirection"),
)
if mibBuilder.loadTexts:
    hh3cBandwidthEntry.setStatus("current")


class _Hh3cBandwidthAclIndex_Type(Integer32):
    """Custom type hh3cBandwidthAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cBandwidthAclIndex_Type.__name__ = "Integer32"
_Hh3cBandwidthAclIndex_Object = MibTableColumn
hh3cBandwidthAclIndex = _Hh3cBandwidthAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 1),
    _Hh3cBandwidthAclIndex_Type()
)
hh3cBandwidthAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthAclIndex.setStatus("current")
_Hh3cBandwidthIfIndex_Type = Integer32
_Hh3cBandwidthIfIndex_Object = MibTableColumn
hh3cBandwidthIfIndex = _Hh3cBandwidthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 2),
    _Hh3cBandwidthIfIndex_Type()
)
hh3cBandwidthIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthIfIndex.setStatus("current")


class _Hh3cBandwidthVlanID_Type(Integer32):
    """Custom type hh3cBandwidthVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cBandwidthVlanID_Type.__name__ = "Integer32"
_Hh3cBandwidthVlanID_Object = MibTableColumn
hh3cBandwidthVlanID = _Hh3cBandwidthVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 3),
    _Hh3cBandwidthVlanID_Type()
)
hh3cBandwidthVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthVlanID.setStatus("current")


class _Hh3cBandwidthDirection_Type(Integer32):
    """Custom type hh3cBandwidthDirection based on Integer32"""
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


_Hh3cBandwidthDirection_Type.__name__ = "Integer32"
_Hh3cBandwidthDirection_Object = MibTableColumn
hh3cBandwidthDirection = _Hh3cBandwidthDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 4),
    _Hh3cBandwidthDirection_Type()
)
hh3cBandwidthDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthDirection.setStatus("current")


class _Hh3cBandwidthIpAclNum_Type(Integer32):
    """Custom type hh3cBandwidthIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cBandwidthIpAclNum_Type.__name__ = "Integer32"
_Hh3cBandwidthIpAclNum_Object = MibTableColumn
hh3cBandwidthIpAclNum = _Hh3cBandwidthIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 5),
    _Hh3cBandwidthIpAclNum_Type()
)
hh3cBandwidthIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthIpAclNum.setStatus("current")


class _Hh3cBandwidthIpAclRule_Type(Integer32):
    """Custom type hh3cBandwidthIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cBandwidthIpAclRule_Type.__name__ = "Integer32"
_Hh3cBandwidthIpAclRule_Object = MibTableColumn
hh3cBandwidthIpAclRule = _Hh3cBandwidthIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 6),
    _Hh3cBandwidthIpAclRule_Type()
)
hh3cBandwidthIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthIpAclRule.setStatus("current")


class _Hh3cBandwidthLinkAclNum_Type(Integer32):
    """Custom type hh3cBandwidthLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cBandwidthLinkAclNum_Type.__name__ = "Integer32"
_Hh3cBandwidthLinkAclNum_Object = MibTableColumn
hh3cBandwidthLinkAclNum = _Hh3cBandwidthLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 7),
    _Hh3cBandwidthLinkAclNum_Type()
)
hh3cBandwidthLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthLinkAclNum.setStatus("current")


class _Hh3cBandwidthLinkAclRule_Type(Integer32):
    """Custom type hh3cBandwidthLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cBandwidthLinkAclRule_Type.__name__ = "Integer32"
_Hh3cBandwidthLinkAclRule_Object = MibTableColumn
hh3cBandwidthLinkAclRule = _Hh3cBandwidthLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 8),
    _Hh3cBandwidthLinkAclRule_Type()
)
hh3cBandwidthLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cBandwidthLinkAclRule.setStatus("current")


class _Hh3cBandwidthMinGuaranteedWidth_Type(Integer32):
    """Custom type hh3cBandwidthMinGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_Hh3cBandwidthMinGuaranteedWidth_Type.__name__ = "Integer32"
_Hh3cBandwidthMinGuaranteedWidth_Object = MibTableColumn
hh3cBandwidthMinGuaranteedWidth = _Hh3cBandwidthMinGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 9),
    _Hh3cBandwidthMinGuaranteedWidth_Type()
)
hh3cBandwidthMinGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBandwidthMinGuaranteedWidth.setStatus("current")


class _Hh3cBandwidthMaxGuaranteedWidth_Type(Integer32):
    """Custom type hh3cBandwidthMaxGuaranteedWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388608),
    )


_Hh3cBandwidthMaxGuaranteedWidth_Type.__name__ = "Integer32"
_Hh3cBandwidthMaxGuaranteedWidth_Object = MibTableColumn
hh3cBandwidthMaxGuaranteedWidth = _Hh3cBandwidthMaxGuaranteedWidth_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 10),
    _Hh3cBandwidthMaxGuaranteedWidth_Type()
)
hh3cBandwidthMaxGuaranteedWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBandwidthMaxGuaranteedWidth.setStatus("current")


class _Hh3cBandwidthWeight_Type(Integer32):
    """Custom type hh3cBandwidthWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cBandwidthWeight_Type.__name__ = "Integer32"
_Hh3cBandwidthWeight_Object = MibTableColumn
hh3cBandwidthWeight = _Hh3cBandwidthWeight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 11),
    _Hh3cBandwidthWeight_Type()
)
hh3cBandwidthWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBandwidthWeight.setStatus("current")
_Hh3cBandwidthRuntime_Type = TruthValue
_Hh3cBandwidthRuntime_Object = MibTableColumn
hh3cBandwidthRuntime = _Hh3cBandwidthRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 12),
    _Hh3cBandwidthRuntime_Type()
)
hh3cBandwidthRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cBandwidthRuntime.setStatus("current")
_Hh3cBandwidthRowStatus_Type = RowStatus
_Hh3cBandwidthRowStatus_Object = MibTableColumn
hh3cBandwidthRowStatus = _Hh3cBandwidthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 11, 1, 13),
    _Hh3cBandwidthRowStatus_Type()
)
hh3cBandwidthRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBandwidthRowStatus.setStatus("current")
_Hh3cRedTable_Object = MibTable
hh3cRedTable = _Hh3cRedTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12)
)
if mibBuilder.loadTexts:
    hh3cRedTable.setStatus("current")
_Hh3cRedEntry_Object = MibTableRow
hh3cRedEntry = _Hh3cRedEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1)
)
hh3cRedEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cRedAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRedIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRedVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cRedDirection"),
)
if mibBuilder.loadTexts:
    hh3cRedEntry.setStatus("current")


class _Hh3cRedAclIndex_Type(Integer32):
    """Custom type hh3cRedAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cRedAclIndex_Type.__name__ = "Integer32"
_Hh3cRedAclIndex_Object = MibTableColumn
hh3cRedAclIndex = _Hh3cRedAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 1),
    _Hh3cRedAclIndex_Type()
)
hh3cRedAclIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedAclIndex.setStatus("current")
_Hh3cRedIfIndex_Type = Integer32
_Hh3cRedIfIndex_Object = MibTableColumn
hh3cRedIfIndex = _Hh3cRedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 2),
    _Hh3cRedIfIndex_Type()
)
hh3cRedIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedIfIndex.setStatus("current")


class _Hh3cRedVlanID_Type(Integer32):
    """Custom type hh3cRedVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRedVlanID_Type.__name__ = "Integer32"
_Hh3cRedVlanID_Object = MibTableColumn
hh3cRedVlanID = _Hh3cRedVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 3),
    _Hh3cRedVlanID_Type()
)
hh3cRedVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedVlanID.setStatus("current")


class _Hh3cRedDirection_Type(Integer32):
    """Custom type hh3cRedDirection based on Integer32"""
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


_Hh3cRedDirection_Type.__name__ = "Integer32"
_Hh3cRedDirection_Object = MibTableColumn
hh3cRedDirection = _Hh3cRedDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 4),
    _Hh3cRedDirection_Type()
)
hh3cRedDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedDirection.setStatus("current")


class _Hh3cRedIpAclNum_Type(Integer32):
    """Custom type hh3cRedIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRedIpAclNum_Type.__name__ = "Integer32"
_Hh3cRedIpAclNum_Object = MibTableColumn
hh3cRedIpAclNum = _Hh3cRedIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 5),
    _Hh3cRedIpAclNum_Type()
)
hh3cRedIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedIpAclNum.setStatus("current")


class _Hh3cRedIpAclRule_Type(Integer32):
    """Custom type hh3cRedIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRedIpAclRule_Type.__name__ = "Integer32"
_Hh3cRedIpAclRule_Object = MibTableColumn
hh3cRedIpAclRule = _Hh3cRedIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 6),
    _Hh3cRedIpAclRule_Type()
)
hh3cRedIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedIpAclRule.setStatus("current")


class _Hh3cRedLinkAclNum_Type(Integer32):
    """Custom type hh3cRedLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRedLinkAclNum_Type.__name__ = "Integer32"
_Hh3cRedLinkAclNum_Object = MibTableColumn
hh3cRedLinkAclNum = _Hh3cRedLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 7),
    _Hh3cRedLinkAclNum_Type()
)
hh3cRedLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedLinkAclNum.setStatus("current")


class _Hh3cRedLinkAclRule_Type(Integer32):
    """Custom type hh3cRedLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRedLinkAclRule_Type.__name__ = "Integer32"
_Hh3cRedLinkAclRule_Object = MibTableColumn
hh3cRedLinkAclRule = _Hh3cRedLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 8),
    _Hh3cRedLinkAclRule_Type()
)
hh3cRedLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRedLinkAclRule.setStatus("current")


class _Hh3cRedStartQueueLen_Type(Integer32):
    """Custom type hh3cRedStartQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_Hh3cRedStartQueueLen_Type.__name__ = "Integer32"
_Hh3cRedStartQueueLen_Object = MibTableColumn
hh3cRedStartQueueLen = _Hh3cRedStartQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 9),
    _Hh3cRedStartQueueLen_Type()
)
hh3cRedStartQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRedStartQueueLen.setStatus("current")


class _Hh3cRedStopQueueLen_Type(Integer32):
    """Custom type hh3cRedStopQueueLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262128),
    )


_Hh3cRedStopQueueLen_Type.__name__ = "Integer32"
_Hh3cRedStopQueueLen_Object = MibTableColumn
hh3cRedStopQueueLen = _Hh3cRedStopQueueLen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 10),
    _Hh3cRedStopQueueLen_Type()
)
hh3cRedStopQueueLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRedStopQueueLen.setStatus("current")


class _Hh3cRedProbability_Type(Integer32):
    """Custom type hh3cRedProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cRedProbability_Type.__name__ = "Integer32"
_Hh3cRedProbability_Object = MibTableColumn
hh3cRedProbability = _Hh3cRedProbability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 11),
    _Hh3cRedProbability_Type()
)
hh3cRedProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRedProbability.setStatus("current")
_Hh3cRedRuntime_Type = TruthValue
_Hh3cRedRuntime_Object = MibTableColumn
hh3cRedRuntime = _Hh3cRedRuntime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 12),
    _Hh3cRedRuntime_Type()
)
hh3cRedRuntime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cRedRuntime.setStatus("current")
_Hh3cRedRowStatus_Type = RowStatus
_Hh3cRedRowStatus_Object = MibTableColumn
hh3cRedRowStatus = _Hh3cRedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 12, 1, 13),
    _Hh3cRedRowStatus_Type()
)
hh3cRedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cRedRowStatus.setStatus("current")
_Hh3cMirrorGroupTable_Object = MibTable
hh3cMirrorGroupTable = _Hh3cMirrorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13)
)
if mibBuilder.loadTexts:
    hh3cMirrorGroupTable.setStatus("current")
_Hh3cMirrorGroupEntry_Object = MibTableRow
hh3cMirrorGroupEntry = _Hh3cMirrorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1)
)
hh3cMirrorGroupEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirrorGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirrorGroupEntry.setStatus("current")


class _Hh3cMirrorGroupID_Type(Integer32):
    """Custom type hh3cMirrorGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cMirrorGroupID_Type.__name__ = "Integer32"
_Hh3cMirrorGroupID_Object = MibTableColumn
hh3cMirrorGroupID = _Hh3cMirrorGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1, 1),
    _Hh3cMirrorGroupID_Type()
)
hh3cMirrorGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirrorGroupID.setStatus("current")


class _Hh3cMirrorGroupDirection_Type(Integer32):
    """Custom type hh3cMirrorGroupDirection based on Integer32"""
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


_Hh3cMirrorGroupDirection_Type.__name__ = "Integer32"
_Hh3cMirrorGroupDirection_Object = MibTableColumn
hh3cMirrorGroupDirection = _Hh3cMirrorGroupDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1, 2),
    _Hh3cMirrorGroupDirection_Type()
)
hh3cMirrorGroupDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMirrorGroupDirection.setStatus("current")


class _Hh3cMirrorGroupMirrorIfIndexList_Type(OctetString):
    """Custom type hh3cMirrorGroupMirrorIfIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_Hh3cMirrorGroupMirrorIfIndexList_Type.__name__ = "OctetString"
_Hh3cMirrorGroupMirrorIfIndexList_Object = MibTableColumn
hh3cMirrorGroupMirrorIfIndexList = _Hh3cMirrorGroupMirrorIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1, 3),
    _Hh3cMirrorGroupMirrorIfIndexList_Type()
)
hh3cMirrorGroupMirrorIfIndexList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMirrorGroupMirrorIfIndexList.setStatus("current")
_Hh3cMirrorGroupMonitorIfIndex_Type = Integer32
_Hh3cMirrorGroupMonitorIfIndex_Object = MibTableColumn
hh3cMirrorGroupMonitorIfIndex = _Hh3cMirrorGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1, 4),
    _Hh3cMirrorGroupMonitorIfIndex_Type()
)
hh3cMirrorGroupMonitorIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMirrorGroupMonitorIfIndex.setStatus("current")
_Hh3cMirrorGroupRowStatus_Type = RowStatus
_Hh3cMirrorGroupRowStatus_Object = MibTableColumn
hh3cMirrorGroupRowStatus = _Hh3cMirrorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 13, 1, 5),
    _Hh3cMirrorGroupRowStatus_Type()
)
hh3cMirrorGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMirrorGroupRowStatus.setStatus("current")
_Hh3cFlowtempTable_Object = MibTable
hh3cFlowtempTable = _Hh3cFlowtempTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14)
)
if mibBuilder.loadTexts:
    hh3cFlowtempTable.setStatus("current")
_Hh3cFlowtempEntry_Object = MibTableRow
hh3cFlowtempEntry = _Hh3cFlowtempEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1)
)
hh3cFlowtempEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cFlowtempIndex"),
)
if mibBuilder.loadTexts:
    hh3cFlowtempEntry.setStatus("current")


class _Hh3cFlowtempIndex_Type(Integer32):
    """Custom type hh3cFlowtempIndex based on Integer32"""
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


_Hh3cFlowtempIndex_Type.__name__ = "Integer32"
_Hh3cFlowtempIndex_Object = MibTableColumn
hh3cFlowtempIndex = _Hh3cFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 1),
    _Hh3cFlowtempIndex_Type()
)
hh3cFlowtempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlowtempIndex.setStatus("current")
_Hh3cFlowtempIpProtocol_Type = TruthValue
_Hh3cFlowtempIpProtocol_Object = MibTableColumn
hh3cFlowtempIpProtocol = _Hh3cFlowtempIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 2),
    _Hh3cFlowtempIpProtocol_Type()
)
hh3cFlowtempIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempIpProtocol.setStatus("current")
_Hh3cFlowtempTcpFlag_Type = TruthValue
_Hh3cFlowtempTcpFlag_Object = MibTableColumn
hh3cFlowtempTcpFlag = _Hh3cFlowtempTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 3),
    _Hh3cFlowtempTcpFlag_Type()
)
hh3cFlowtempTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempTcpFlag.setStatus("current")
_Hh3cFlowtempSPort_Type = TruthValue
_Hh3cFlowtempSPort_Object = MibTableColumn
hh3cFlowtempSPort = _Hh3cFlowtempSPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 4),
    _Hh3cFlowtempSPort_Type()
)
hh3cFlowtempSPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempSPort.setStatus("current")
_Hh3cFlowtempDPort_Type = TruthValue
_Hh3cFlowtempDPort_Object = MibTableColumn
hh3cFlowtempDPort = _Hh3cFlowtempDPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 5),
    _Hh3cFlowtempDPort_Type()
)
hh3cFlowtempDPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDPort.setStatus("current")
_Hh3cFlowtempIcmpType_Type = TruthValue
_Hh3cFlowtempIcmpType_Object = MibTableColumn
hh3cFlowtempIcmpType = _Hh3cFlowtempIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 6),
    _Hh3cFlowtempIcmpType_Type()
)
hh3cFlowtempIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempIcmpType.setStatus("current")
_Hh3cFlowtempIcmpCode_Type = TruthValue
_Hh3cFlowtempIcmpCode_Object = MibTableColumn
hh3cFlowtempIcmpCode = _Hh3cFlowtempIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 7),
    _Hh3cFlowtempIcmpCode_Type()
)
hh3cFlowtempIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempIcmpCode.setStatus("current")
_Hh3cFlowtempFragment_Type = TruthValue
_Hh3cFlowtempFragment_Object = MibTableColumn
hh3cFlowtempFragment = _Hh3cFlowtempFragment_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 8),
    _Hh3cFlowtempFragment_Type()
)
hh3cFlowtempFragment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempFragment.setStatus("current")
_Hh3cFlowtempDscp_Type = TruthValue
_Hh3cFlowtempDscp_Object = MibTableColumn
hh3cFlowtempDscp = _Hh3cFlowtempDscp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 9),
    _Hh3cFlowtempDscp_Type()
)
hh3cFlowtempDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDscp.setStatus("current")
_Hh3cFlowtempIpPre_Type = TruthValue
_Hh3cFlowtempIpPre_Object = MibTableColumn
hh3cFlowtempIpPre = _Hh3cFlowtempIpPre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 10),
    _Hh3cFlowtempIpPre_Type()
)
hh3cFlowtempIpPre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempIpPre.setStatus("current")
_Hh3cFlowtempTos_Type = TruthValue
_Hh3cFlowtempTos_Object = MibTableColumn
hh3cFlowtempTos = _Hh3cFlowtempTos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 11),
    _Hh3cFlowtempTos_Type()
)
hh3cFlowtempTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempTos.setStatus("current")
_Hh3cFlowtempSIp_Type = TruthValue
_Hh3cFlowtempSIp_Object = MibTableColumn
hh3cFlowtempSIp = _Hh3cFlowtempSIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 12),
    _Hh3cFlowtempSIp_Type()
)
hh3cFlowtempSIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempSIp.setStatus("current")
_Hh3cFlowtempSIpMask_Type = IpAddress
_Hh3cFlowtempSIpMask_Object = MibTableColumn
hh3cFlowtempSIpMask = _Hh3cFlowtempSIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 13),
    _Hh3cFlowtempSIpMask_Type()
)
hh3cFlowtempSIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempSIpMask.setStatus("current")
_Hh3cFlowtempDIp_Type = TruthValue
_Hh3cFlowtempDIp_Object = MibTableColumn
hh3cFlowtempDIp = _Hh3cFlowtempDIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 14),
    _Hh3cFlowtempDIp_Type()
)
hh3cFlowtempDIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDIp.setStatus("current")
_Hh3cFlowtempDIpMask_Type = IpAddress
_Hh3cFlowtempDIpMask_Object = MibTableColumn
hh3cFlowtempDIpMask = _Hh3cFlowtempDIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 15),
    _Hh3cFlowtempDIpMask_Type()
)
hh3cFlowtempDIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDIpMask.setStatus("current")
_Hh3cFlowtempEthProtocol_Type = TruthValue
_Hh3cFlowtempEthProtocol_Object = MibTableColumn
hh3cFlowtempEthProtocol = _Hh3cFlowtempEthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 16),
    _Hh3cFlowtempEthProtocol_Type()
)
hh3cFlowtempEthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempEthProtocol.setStatus("current")
_Hh3cFlowtempSMac_Type = TruthValue
_Hh3cFlowtempSMac_Object = MibTableColumn
hh3cFlowtempSMac = _Hh3cFlowtempSMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 17),
    _Hh3cFlowtempSMac_Type()
)
hh3cFlowtempSMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempSMac.setStatus("current")
_Hh3cFlowtempSMacMask_Type = MacAddress
_Hh3cFlowtempSMacMask_Object = MibTableColumn
hh3cFlowtempSMacMask = _Hh3cFlowtempSMacMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 18),
    _Hh3cFlowtempSMacMask_Type()
)
hh3cFlowtempSMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempSMacMask.setStatus("current")
_Hh3cFlowtempDMac_Type = TruthValue
_Hh3cFlowtempDMac_Object = MibTableColumn
hh3cFlowtempDMac = _Hh3cFlowtempDMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 19),
    _Hh3cFlowtempDMac_Type()
)
hh3cFlowtempDMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDMac.setStatus("current")
_Hh3cFlowtempDMacMask_Type = MacAddress
_Hh3cFlowtempDMacMask_Object = MibTableColumn
hh3cFlowtempDMacMask = _Hh3cFlowtempDMacMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 20),
    _Hh3cFlowtempDMacMask_Type()
)
hh3cFlowtempDMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempDMacMask.setStatus("current")
_Hh3cFlowtempVpn_Type = TruthValue
_Hh3cFlowtempVpn_Object = MibTableColumn
hh3cFlowtempVpn = _Hh3cFlowtempVpn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 21),
    _Hh3cFlowtempVpn_Type()
)
hh3cFlowtempVpn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempVpn.setStatus("current")
_Hh3cFlowtempRowStatus_Type = RowStatus
_Hh3cFlowtempRowStatus_Object = MibTableColumn
hh3cFlowtempRowStatus = _Hh3cFlowtempRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 22),
    _Hh3cFlowtempRowStatus_Type()
)
hh3cFlowtempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempRowStatus.setStatus("current")
_Hh3cFlowtempVlanId_Type = TruthValue
_Hh3cFlowtempVlanId_Object = MibTableColumn
hh3cFlowtempVlanId = _Hh3cFlowtempVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 23),
    _Hh3cFlowtempVlanId_Type()
)
hh3cFlowtempVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempVlanId.setStatus("current")
_Hh3cFlowtempCos_Type = TruthValue
_Hh3cFlowtempCos_Object = MibTableColumn
hh3cFlowtempCos = _Hh3cFlowtempCos_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 14, 1, 24),
    _Hh3cFlowtempCos_Type()
)
hh3cFlowtempCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempCos.setStatus("current")
_Hh3cFlowtempEnableTable_Object = MibTable
hh3cFlowtempEnableTable = _Hh3cFlowtempEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 15)
)
if mibBuilder.loadTexts:
    hh3cFlowtempEnableTable.setStatus("current")
_Hh3cFlowtempEnableEntry_Object = MibTableRow
hh3cFlowtempEnableEntry = _Hh3cFlowtempEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 15, 1)
)
hh3cFlowtempEnableEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cFlowtempEnableIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cFlowtempEnableVlanID"),
)
if mibBuilder.loadTexts:
    hh3cFlowtempEnableEntry.setStatus("current")
_Hh3cFlowtempEnableIfIndex_Type = Integer32
_Hh3cFlowtempEnableIfIndex_Object = MibTableColumn
hh3cFlowtempEnableIfIndex = _Hh3cFlowtempEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 15, 1, 1),
    _Hh3cFlowtempEnableIfIndex_Type()
)
hh3cFlowtempEnableIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempEnableIfIndex.setStatus("current")


class _Hh3cFlowtempEnableVlanID_Type(Integer32):
    """Custom type hh3cFlowtempEnableVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cFlowtempEnableVlanID_Type.__name__ = "Integer32"
_Hh3cFlowtempEnableVlanID_Object = MibTableColumn
hh3cFlowtempEnableVlanID = _Hh3cFlowtempEnableVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 15, 1, 2),
    _Hh3cFlowtempEnableVlanID_Type()
)
hh3cFlowtempEnableVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFlowtempEnableVlanID.setStatus("current")


class _Hh3cFlowtempEnableFlowtempIndex_Type(Integer32):
    """Custom type hh3cFlowtempEnableFlowtempIndex based on Integer32"""
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


_Hh3cFlowtempEnableFlowtempIndex_Type.__name__ = "Integer32"
_Hh3cFlowtempEnableFlowtempIndex_Object = MibTableColumn
hh3cFlowtempEnableFlowtempIndex = _Hh3cFlowtempEnableFlowtempIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 15, 1, 3),
    _Hh3cFlowtempEnableFlowtempIndex_Type()
)
hh3cFlowtempEnableFlowtempIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlowtempEnableFlowtempIndex.setStatus("current")
_Hh3cTrafficShapeTable_Object = MibTable
hh3cTrafficShapeTable = _Hh3cTrafficShapeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16)
)
if mibBuilder.loadTexts:
    hh3cTrafficShapeTable.setStatus("current")
_Hh3cTrafficShapeEntry_Object = MibTableRow
hh3cTrafficShapeEntry = _Hh3cTrafficShapeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1)
)
hh3cTrafficShapeEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cTrafficShapeIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cTrafficShapeQueueId"),
)
if mibBuilder.loadTexts:
    hh3cTrafficShapeEntry.setStatus("current")
_Hh3cTrafficShapeIfIndex_Type = Integer32
_Hh3cTrafficShapeIfIndex_Object = MibTableColumn
hh3cTrafficShapeIfIndex = _Hh3cTrafficShapeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 1),
    _Hh3cTrafficShapeIfIndex_Type()
)
hh3cTrafficShapeIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeIfIndex.setStatus("current")


class _Hh3cTrafficShapeQueueId_Type(Integer32):
    """Custom type hh3cTrafficShapeQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hh3cTrafficShapeQueueId_Type.__name__ = "Integer32"
_Hh3cTrafficShapeQueueId_Object = MibTableColumn
hh3cTrafficShapeQueueId = _Hh3cTrafficShapeQueueId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 2),
    _Hh3cTrafficShapeQueueId_Type()
)
hh3cTrafficShapeQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeQueueId.setStatus("current")
_Hh3cTrafficShapeMaxRate_Type = Integer32
_Hh3cTrafficShapeMaxRate_Object = MibTableColumn
hh3cTrafficShapeMaxRate = _Hh3cTrafficShapeMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 3),
    _Hh3cTrafficShapeMaxRate_Type()
)
hh3cTrafficShapeMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeMaxRate.setStatus("current")
_Hh3cTrafficShapeBurstSize_Type = Integer32
_Hh3cTrafficShapeBurstSize_Object = MibTableColumn
hh3cTrafficShapeBurstSize = _Hh3cTrafficShapeBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 4),
    _Hh3cTrafficShapeBurstSize_Type()
)
hh3cTrafficShapeBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeBurstSize.setStatus("current")


class _Hh3cTrafficShapeBufferLimit_Type(Integer32):
    """Custom type hh3cTrafficShapeBufferLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(16, 8000),
    )


_Hh3cTrafficShapeBufferLimit_Type.__name__ = "Integer32"
_Hh3cTrafficShapeBufferLimit_Object = MibTableColumn
hh3cTrafficShapeBufferLimit = _Hh3cTrafficShapeBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 5),
    _Hh3cTrafficShapeBufferLimit_Type()
)
hh3cTrafficShapeBufferLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeBufferLimit.setStatus("current")
_Hh3cTrafficShapeRowStatus_Type = RowStatus
_Hh3cTrafficShapeRowStatus_Object = MibTableColumn
hh3cTrafficShapeRowStatus = _Hh3cTrafficShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 16, 1, 6),
    _Hh3cTrafficShapeRowStatus_Type()
)
hh3cTrafficShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrafficShapeRowStatus.setStatus("current")
_Hh3cPortQueueTable_Object = MibTable
hh3cPortQueueTable = _Hh3cPortQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17)
)
if mibBuilder.loadTexts:
    hh3cPortQueueTable.setStatus("current")
_Hh3cPortQueueEntry_Object = MibTableRow
hh3cPortQueueEntry = _Hh3cPortQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17, 1)
)
hh3cPortQueueEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cPortQueueIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cPortQueueQueueID"),
)
if mibBuilder.loadTexts:
    hh3cPortQueueEntry.setStatus("current")
_Hh3cPortQueueIfIndex_Type = Integer32
_Hh3cPortQueueIfIndex_Object = MibTableColumn
hh3cPortQueueIfIndex = _Hh3cPortQueueIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17, 1, 1),
    _Hh3cPortQueueIfIndex_Type()
)
hh3cPortQueueIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortQueueIfIndex.setStatus("current")


class _Hh3cPortQueueQueueID_Type(Integer32):
    """Custom type hh3cPortQueueQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cPortQueueQueueID_Type.__name__ = "Integer32"
_Hh3cPortQueueQueueID_Object = MibTableColumn
hh3cPortQueueQueueID = _Hh3cPortQueueQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17, 1, 2),
    _Hh3cPortQueueQueueID_Type()
)
hh3cPortQueueQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortQueueQueueID.setStatus("current")


class _Hh3cPortQueueWrrPriority_Type(Integer32):
    """Custom type hh3cPortQueueWrrPriority based on Integer32"""
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


_Hh3cPortQueueWrrPriority_Type.__name__ = "Integer32"
_Hh3cPortQueueWrrPriority_Object = MibTableColumn
hh3cPortQueueWrrPriority = _Hh3cPortQueueWrrPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17, 1, 3),
    _Hh3cPortQueueWrrPriority_Type()
)
hh3cPortQueueWrrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortQueueWrrPriority.setStatus("current")


class _Hh3cPortQueueWeight_Type(Integer32):
    """Custom type hh3cPortQueueWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 255),
    )


_Hh3cPortQueueWeight_Type.__name__ = "Integer32"
_Hh3cPortQueueWeight_Object = MibTableColumn
hh3cPortQueueWeight = _Hh3cPortQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 17, 1, 4),
    _Hh3cPortQueueWeight_Type()
)
hh3cPortQueueWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortQueueWeight.setStatus("current")
_Hh3cDropModeTable_Object = MibTable
hh3cDropModeTable = _Hh3cDropModeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 18)
)
if mibBuilder.loadTexts:
    hh3cDropModeTable.setStatus("current")
_Hh3cDropModeEntry_Object = MibTableRow
hh3cDropModeEntry = _Hh3cDropModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 18, 1)
)
hh3cDropModeEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDropModeIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cDropModeEntry.setStatus("current")
_Hh3cDropModeIfIndex_Type = Integer32
_Hh3cDropModeIfIndex_Object = MibTableColumn
hh3cDropModeIfIndex = _Hh3cDropModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 18, 1, 1),
    _Hh3cDropModeIfIndex_Type()
)
hh3cDropModeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDropModeIfIndex.setStatus("current")


class _Hh3cDropModeMode_Type(Integer32):
    """Custom type hh3cDropModeMode based on Integer32"""
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


_Hh3cDropModeMode_Type.__name__ = "Integer32"
_Hh3cDropModeMode_Object = MibTableColumn
hh3cDropModeMode = _Hh3cDropModeMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 18, 1, 2),
    _Hh3cDropModeMode_Type()
)
hh3cDropModeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDropModeMode.setStatus("current")


class _Hh3cDropModeWredIndex_Type(Integer32):
    """Custom type hh3cDropModeWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Hh3cDropModeWredIndex_Type.__name__ = "Integer32"
_Hh3cDropModeWredIndex_Object = MibTableColumn
hh3cDropModeWredIndex = _Hh3cDropModeWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 18, 1, 3),
    _Hh3cDropModeWredIndex_Type()
)
hh3cDropModeWredIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDropModeWredIndex.setStatus("current")
_Hh3cWredTable_Object = MibTable
hh3cWredTable = _Hh3cWredTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19)
)
if mibBuilder.loadTexts:
    hh3cWredTable.setStatus("current")
_Hh3cWredEntry_Object = MibTableRow
hh3cWredEntry = _Hh3cWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1)
)
hh3cWredEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cWredIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cWredQueueId"),
)
if mibBuilder.loadTexts:
    hh3cWredEntry.setStatus("current")


class _Hh3cWredIndex_Type(Integer32):
    """Custom type hh3cWredIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Hh3cWredIndex_Type.__name__ = "Integer32"
_Hh3cWredIndex_Object = MibTableColumn
hh3cWredIndex = _Hh3cWredIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 1),
    _Hh3cWredIndex_Type()
)
hh3cWredIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWredIndex.setStatus("current")


class _Hh3cWredQueueId_Type(Integer32):
    """Custom type hh3cWredQueueId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cWredQueueId_Type.__name__ = "Integer32"
_Hh3cWredQueueId_Object = MibTableColumn
hh3cWredQueueId = _Hh3cWredQueueId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 2),
    _Hh3cWredQueueId_Type()
)
hh3cWredQueueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cWredQueueId.setStatus("current")


class _Hh3cWredGreenMinThreshold_Type(Integer32):
    """Custom type hh3cWredGreenMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredGreenMinThreshold_Type.__name__ = "Integer32"
_Hh3cWredGreenMinThreshold_Object = MibTableColumn
hh3cWredGreenMinThreshold = _Hh3cWredGreenMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 3),
    _Hh3cWredGreenMinThreshold_Type()
)
hh3cWredGreenMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredGreenMinThreshold.setStatus("current")


class _Hh3cWredGreenMaxThreshold_Type(Integer32):
    """Custom type hh3cWredGreenMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredGreenMaxThreshold_Type.__name__ = "Integer32"
_Hh3cWredGreenMaxThreshold_Object = MibTableColumn
hh3cWredGreenMaxThreshold = _Hh3cWredGreenMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 4),
    _Hh3cWredGreenMaxThreshold_Type()
)
hh3cWredGreenMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredGreenMaxThreshold.setStatus("current")


class _Hh3cWredGreenMaxProb_Type(Integer32):
    """Custom type hh3cWredGreenMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cWredGreenMaxProb_Type.__name__ = "Integer32"
_Hh3cWredGreenMaxProb_Object = MibTableColumn
hh3cWredGreenMaxProb = _Hh3cWredGreenMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 5),
    _Hh3cWredGreenMaxProb_Type()
)
hh3cWredGreenMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredGreenMaxProb.setStatus("current")


class _Hh3cWredYellowMinThreshold_Type(Integer32):
    """Custom type hh3cWredYellowMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredYellowMinThreshold_Type.__name__ = "Integer32"
_Hh3cWredYellowMinThreshold_Object = MibTableColumn
hh3cWredYellowMinThreshold = _Hh3cWredYellowMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 6),
    _Hh3cWredYellowMinThreshold_Type()
)
hh3cWredYellowMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredYellowMinThreshold.setStatus("current")


class _Hh3cWredYellowMaxThreshold_Type(Integer32):
    """Custom type hh3cWredYellowMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredYellowMaxThreshold_Type.__name__ = "Integer32"
_Hh3cWredYellowMaxThreshold_Object = MibTableColumn
hh3cWredYellowMaxThreshold = _Hh3cWredYellowMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 7),
    _Hh3cWredYellowMaxThreshold_Type()
)
hh3cWredYellowMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredYellowMaxThreshold.setStatus("current")


class _Hh3cWredYellowMaxProb_Type(Integer32):
    """Custom type hh3cWredYellowMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cWredYellowMaxProb_Type.__name__ = "Integer32"
_Hh3cWredYellowMaxProb_Object = MibTableColumn
hh3cWredYellowMaxProb = _Hh3cWredYellowMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 8),
    _Hh3cWredYellowMaxProb_Type()
)
hh3cWredYellowMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredYellowMaxProb.setStatus("current")


class _Hh3cWredRedMinThreshold_Type(Integer32):
    """Custom type hh3cWredRedMinThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredRedMinThreshold_Type.__name__ = "Integer32"
_Hh3cWredRedMinThreshold_Object = MibTableColumn
hh3cWredRedMinThreshold = _Hh3cWredRedMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 9),
    _Hh3cWredRedMinThreshold_Type()
)
hh3cWredRedMinThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredRedMinThreshold.setStatus("current")


class _Hh3cWredRedMaxThreshold_Type(Integer32):
    """Custom type hh3cWredRedMaxThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cWredRedMaxThreshold_Type.__name__ = "Integer32"
_Hh3cWredRedMaxThreshold_Object = MibTableColumn
hh3cWredRedMaxThreshold = _Hh3cWredRedMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 10),
    _Hh3cWredRedMaxThreshold_Type()
)
hh3cWredRedMaxThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredRedMaxThreshold.setStatus("current")


class _Hh3cWredRedMaxProb_Type(Integer32):
    """Custom type hh3cWredRedMaxProb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cWredRedMaxProb_Type.__name__ = "Integer32"
_Hh3cWredRedMaxProb_Object = MibTableColumn
hh3cWredRedMaxProb = _Hh3cWredRedMaxProb_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 11),
    _Hh3cWredRedMaxProb_Type()
)
hh3cWredRedMaxProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredRedMaxProb.setStatus("current")


class _Hh3cWredExponent_Type(Integer32):
    """Custom type hh3cWredExponent based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cWredExponent_Type.__name__ = "Integer32"
_Hh3cWredExponent_Object = MibTableColumn
hh3cWredExponent = _Hh3cWredExponent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 19, 1, 12),
    _Hh3cWredExponent_Type()
)
hh3cWredExponent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cWredExponent.setStatus("current")
_Hh3cCosToLocalPrecedenceMapTable_Object = MibTable
hh3cCosToLocalPrecedenceMapTable = _Hh3cCosToLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 20)
)
if mibBuilder.loadTexts:
    hh3cCosToLocalPrecedenceMapTable.setStatus("current")
_Hh3cCosToLocalPrecedenceMapEntry_Object = MibTableRow
hh3cCosToLocalPrecedenceMapEntry = _Hh3cCosToLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 20, 1)
)
hh3cCosToLocalPrecedenceMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cCosToLocalPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hh3cCosToLocalPrecedenceMapEntry.setStatus("current")


class _Hh3cCosToLocalPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hh3cCosToLocalPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cCosToLocalPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_Hh3cCosToLocalPrecedenceMapCosIndex_Object = MibTableColumn
hh3cCosToLocalPrecedenceMapCosIndex = _Hh3cCosToLocalPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 20, 1, 1),
    _Hh3cCosToLocalPrecedenceMapCosIndex_Type()
)
hh3cCosToLocalPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCosToLocalPrecedenceMapCosIndex.setStatus("current")


class _Hh3cCosToLocalPrecedenceMapLocalPrecedenceValue_Type(Integer32):
    """Custom type hh3cCosToLocalPrecedenceMapLocalPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cCosToLocalPrecedenceMapLocalPrecedenceValue_Type.__name__ = "Integer32"
_Hh3cCosToLocalPrecedenceMapLocalPrecedenceValue_Object = MibTableColumn
hh3cCosToLocalPrecedenceMapLocalPrecedenceValue = _Hh3cCosToLocalPrecedenceMapLocalPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 20, 1, 2),
    _Hh3cCosToLocalPrecedenceMapLocalPrecedenceValue_Type()
)
hh3cCosToLocalPrecedenceMapLocalPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCosToLocalPrecedenceMapLocalPrecedenceValue.setStatus("current")
_Hh3cCosToDropPrecedenceMapTable_Object = MibTable
hh3cCosToDropPrecedenceMapTable = _Hh3cCosToDropPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 21)
)
if mibBuilder.loadTexts:
    hh3cCosToDropPrecedenceMapTable.setStatus("current")
_Hh3cCosToDropPrecedenceMapEntry_Object = MibTableRow
hh3cCosToDropPrecedenceMapEntry = _Hh3cCosToDropPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 21, 1)
)
hh3cCosToDropPrecedenceMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cCosToDropPrecedenceMapCosIndex"),
)
if mibBuilder.loadTexts:
    hh3cCosToDropPrecedenceMapEntry.setStatus("current")


class _Hh3cCosToDropPrecedenceMapCosIndex_Type(Integer32):
    """Custom type hh3cCosToDropPrecedenceMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cCosToDropPrecedenceMapCosIndex_Type.__name__ = "Integer32"
_Hh3cCosToDropPrecedenceMapCosIndex_Object = MibTableColumn
hh3cCosToDropPrecedenceMapCosIndex = _Hh3cCosToDropPrecedenceMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 21, 1, 1),
    _Hh3cCosToDropPrecedenceMapCosIndex_Type()
)
hh3cCosToDropPrecedenceMapCosIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cCosToDropPrecedenceMapCosIndex.setStatus("current")


class _Hh3cCosToDropPrecedenceMapDropPrecedenceValue_Type(Integer32):
    """Custom type hh3cCosToDropPrecedenceMapDropPrecedenceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cCosToDropPrecedenceMapDropPrecedenceValue_Type.__name__ = "Integer32"
_Hh3cCosToDropPrecedenceMapDropPrecedenceValue_Object = MibTableColumn
hh3cCosToDropPrecedenceMapDropPrecedenceValue = _Hh3cCosToDropPrecedenceMapDropPrecedenceValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 21, 1, 2),
    _Hh3cCosToDropPrecedenceMapDropPrecedenceValue_Type()
)
hh3cCosToDropPrecedenceMapDropPrecedenceValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCosToDropPrecedenceMapDropPrecedenceValue.setStatus("current")
_Hh3cDscpMapTable_Object = MibTable
hh3cDscpMapTable = _Hh3cDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22)
)
if mibBuilder.loadTexts:
    hh3cDscpMapTable.setStatus("current")
_Hh3cDscpMapEntry_Object = MibTableRow
hh3cDscpMapEntry = _Hh3cDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1)
)
hh3cDscpMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDscpMapConformLevel"),
    (0, "HH3C-LswQos-MIB", "hh3cDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hh3cDscpMapEntry.setStatus("current")


class _Hh3cDscpMapConformLevel_Type(Integer32):
    """Custom type hh3cDscpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cDscpMapConformLevel_Type.__name__ = "Integer32"
_Hh3cDscpMapConformLevel_Object = MibTableColumn
hh3cDscpMapConformLevel = _Hh3cDscpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 1),
    _Hh3cDscpMapConformLevel_Type()
)
hh3cDscpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDscpMapConformLevel.setStatus("current")


class _Hh3cDscpMapDscpIndex_Type(Integer32):
    """Custom type hh3cDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpMapDscpIndex_Type.__name__ = "Integer32"
_Hh3cDscpMapDscpIndex_Object = MibTableColumn
hh3cDscpMapDscpIndex = _Hh3cDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 2),
    _Hh3cDscpMapDscpIndex_Type()
)
hh3cDscpMapDscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDscpMapDscpIndex.setStatus("current")


class _Hh3cDscpMapDscpValue_Type(Integer32):
    """Custom type hh3cDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpMapDscpValue_Type.__name__ = "Integer32"
_Hh3cDscpMapDscpValue_Object = MibTableColumn
hh3cDscpMapDscpValue = _Hh3cDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 3),
    _Hh3cDscpMapDscpValue_Type()
)
hh3cDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpMapDscpValue.setStatus("current")


class _Hh3cDscpMapExpValue_Type(Integer32):
    """Custom type hh3cDscpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDscpMapExpValue_Type.__name__ = "Integer32"
_Hh3cDscpMapExpValue_Object = MibTableColumn
hh3cDscpMapExpValue = _Hh3cDscpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 4),
    _Hh3cDscpMapExpValue_Type()
)
hh3cDscpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpMapExpValue.setStatus("current")


class _Hh3cDscpMapCosValue_Type(Integer32):
    """Custom type hh3cDscpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDscpMapCosValue_Type.__name__ = "Integer32"
_Hh3cDscpMapCosValue_Object = MibTableColumn
hh3cDscpMapCosValue = _Hh3cDscpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 5),
    _Hh3cDscpMapCosValue_Type()
)
hh3cDscpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpMapCosValue.setStatus("current")


class _Hh3cDscpMapLocalPrecedence_Type(Integer32):
    """Custom type hh3cDscpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDscpMapLocalPrecedence_Type.__name__ = "Integer32"
_Hh3cDscpMapLocalPrecedence_Object = MibTableColumn
hh3cDscpMapLocalPrecedence = _Hh3cDscpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 6),
    _Hh3cDscpMapLocalPrecedence_Type()
)
hh3cDscpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpMapLocalPrecedence.setStatus("current")


class _Hh3cDscpMapDropPrecedence_Type(Integer32):
    """Custom type hh3cDscpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cDscpMapDropPrecedence_Type.__name__ = "Integer32"
_Hh3cDscpMapDropPrecedence_Object = MibTableColumn
hh3cDscpMapDropPrecedence = _Hh3cDscpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 22, 1, 7),
    _Hh3cDscpMapDropPrecedence_Type()
)
hh3cDscpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpMapDropPrecedence.setStatus("current")
_Hh3cExpMapTable_Object = MibTable
hh3cExpMapTable = _Hh3cExpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23)
)
if mibBuilder.loadTexts:
    hh3cExpMapTable.setStatus("current")
_Hh3cExpMapEntry_Object = MibTableRow
hh3cExpMapEntry = _Hh3cExpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1)
)
hh3cExpMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cExpMapConformLevel"),
    (0, "HH3C-LswQos-MIB", "hh3cExpMapExpIndex"),
)
if mibBuilder.loadTexts:
    hh3cExpMapEntry.setStatus("current")


class _Hh3cExpMapConformLevel_Type(Integer32):
    """Custom type hh3cExpMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cExpMapConformLevel_Type.__name__ = "Integer32"
_Hh3cExpMapConformLevel_Object = MibTableColumn
hh3cExpMapConformLevel = _Hh3cExpMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 1),
    _Hh3cExpMapConformLevel_Type()
)
hh3cExpMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cExpMapConformLevel.setStatus("current")


class _Hh3cExpMapExpIndex_Type(Integer32):
    """Custom type hh3cExpMapExpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cExpMapExpIndex_Type.__name__ = "Integer32"
_Hh3cExpMapExpIndex_Object = MibTableColumn
hh3cExpMapExpIndex = _Hh3cExpMapExpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 2),
    _Hh3cExpMapExpIndex_Type()
)
hh3cExpMapExpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cExpMapExpIndex.setStatus("current")


class _Hh3cExpMapDscpValue_Type(Integer32):
    """Custom type hh3cExpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cExpMapDscpValue_Type.__name__ = "Integer32"
_Hh3cExpMapDscpValue_Object = MibTableColumn
hh3cExpMapDscpValue = _Hh3cExpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 3),
    _Hh3cExpMapDscpValue_Type()
)
hh3cExpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpMapDscpValue.setStatus("current")


class _Hh3cExpMapExpValue_Type(Integer32):
    """Custom type hh3cExpMapExpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cExpMapExpValue_Type.__name__ = "Integer32"
_Hh3cExpMapExpValue_Object = MibTableColumn
hh3cExpMapExpValue = _Hh3cExpMapExpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 4),
    _Hh3cExpMapExpValue_Type()
)
hh3cExpMapExpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpMapExpValue.setStatus("current")


class _Hh3cExpMapCosValue_Type(Integer32):
    """Custom type hh3cExpMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cExpMapCosValue_Type.__name__ = "Integer32"
_Hh3cExpMapCosValue_Object = MibTableColumn
hh3cExpMapCosValue = _Hh3cExpMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 5),
    _Hh3cExpMapCosValue_Type()
)
hh3cExpMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpMapCosValue.setStatus("current")


class _Hh3cExpMapLocalPrecedence_Type(Integer32):
    """Custom type hh3cExpMapLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cExpMapLocalPrecedence_Type.__name__ = "Integer32"
_Hh3cExpMapLocalPrecedence_Object = MibTableColumn
hh3cExpMapLocalPrecedence = _Hh3cExpMapLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 6),
    _Hh3cExpMapLocalPrecedence_Type()
)
hh3cExpMapLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpMapLocalPrecedence.setStatus("current")


class _Hh3cExpMapDropPrecedence_Type(Integer32):
    """Custom type hh3cExpMapDropPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cExpMapDropPrecedence_Type.__name__ = "Integer32"
_Hh3cExpMapDropPrecedence_Object = MibTableColumn
hh3cExpMapDropPrecedence = _Hh3cExpMapDropPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 23, 1, 7),
    _Hh3cExpMapDropPrecedence_Type()
)
hh3cExpMapDropPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cExpMapDropPrecedence.setStatus("current")
_Hh3cLocalPrecedenceMapTable_Object = MibTable
hh3cLocalPrecedenceMapTable = _Hh3cLocalPrecedenceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 24)
)
if mibBuilder.loadTexts:
    hh3cLocalPrecedenceMapTable.setStatus("current")
_Hh3cLocalPrecedenceMapEntry_Object = MibTableRow
hh3cLocalPrecedenceMapEntry = _Hh3cLocalPrecedenceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 24, 1)
)
hh3cLocalPrecedenceMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cLocalPrecedenceMapConformLevel"),
    (0, "HH3C-LswQos-MIB", "hh3cLocalPrecedenceMapLocalPrecedenceIndex"),
)
if mibBuilder.loadTexts:
    hh3cLocalPrecedenceMapEntry.setStatus("current")


class _Hh3cLocalPrecedenceMapConformLevel_Type(Integer32):
    """Custom type hh3cLocalPrecedenceMapConformLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cLocalPrecedenceMapConformLevel_Type.__name__ = "Integer32"
_Hh3cLocalPrecedenceMapConformLevel_Object = MibTableColumn
hh3cLocalPrecedenceMapConformLevel = _Hh3cLocalPrecedenceMapConformLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 24, 1, 1),
    _Hh3cLocalPrecedenceMapConformLevel_Type()
)
hh3cLocalPrecedenceMapConformLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cLocalPrecedenceMapConformLevel.setStatus("current")


class _Hh3cLocalPrecedenceMapLocalPrecedenceIndex_Type(Integer32):
    """Custom type hh3cLocalPrecedenceMapLocalPrecedenceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cLocalPrecedenceMapLocalPrecedenceIndex_Type.__name__ = "Integer32"
_Hh3cLocalPrecedenceMapLocalPrecedenceIndex_Object = MibTableColumn
hh3cLocalPrecedenceMapLocalPrecedenceIndex = _Hh3cLocalPrecedenceMapLocalPrecedenceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 24, 1, 2),
    _Hh3cLocalPrecedenceMapLocalPrecedenceIndex_Type()
)
hh3cLocalPrecedenceMapLocalPrecedenceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLocalPrecedenceMapLocalPrecedenceIndex.setStatus("current")


class _Hh3cLocalPrecedenceMapCosValue_Type(Integer32):
    """Custom type hh3cLocalPrecedenceMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cLocalPrecedenceMapCosValue_Type.__name__ = "Integer32"
_Hh3cLocalPrecedenceMapCosValue_Object = MibTableColumn
hh3cLocalPrecedenceMapCosValue = _Hh3cLocalPrecedenceMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 24, 1, 3),
    _Hh3cLocalPrecedenceMapCosValue_Type()
)
hh3cLocalPrecedenceMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cLocalPrecedenceMapCosValue.setStatus("current")
_Hh3cPortWredTable_Object = MibTable
hh3cPortWredTable = _Hh3cPortWredTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25)
)
if mibBuilder.loadTexts:
    hh3cPortWredTable.setStatus("current")
_Hh3cPortWredEntry_Object = MibTableRow
hh3cPortWredEntry = _Hh3cPortWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25, 1)
)
hh3cPortWredEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cPortWredIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cPortWredQueueID"),
)
if mibBuilder.loadTexts:
    hh3cPortWredEntry.setStatus("current")
_Hh3cPortWredIfIndex_Type = Integer32
_Hh3cPortWredIfIndex_Object = MibTableColumn
hh3cPortWredIfIndex = _Hh3cPortWredIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25, 1, 1),
    _Hh3cPortWredIfIndex_Type()
)
hh3cPortWredIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortWredIfIndex.setStatus("current")


class _Hh3cPortWredQueueID_Type(Integer32):
    """Custom type hh3cPortWredQueueID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cPortWredQueueID_Type.__name__ = "Integer32"
_Hh3cPortWredQueueID_Object = MibTableColumn
hh3cPortWredQueueID = _Hh3cPortWredQueueID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25, 1, 2),
    _Hh3cPortWredQueueID_Type()
)
hh3cPortWredQueueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPortWredQueueID.setStatus("current")


class _Hh3cPortWredQueueStartLength_Type(Integer32):
    """Custom type hh3cPortWredQueueStartLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_Hh3cPortWredQueueStartLength_Type.__name__ = "Integer32"
_Hh3cPortWredQueueStartLength_Object = MibTableColumn
hh3cPortWredQueueStartLength = _Hh3cPortWredQueueStartLength_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25, 1, 3),
    _Hh3cPortWredQueueStartLength_Type()
)
hh3cPortWredQueueStartLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortWredQueueStartLength.setStatus("current")


class _Hh3cPortWredQueueProbability_Type(Integer32):
    """Custom type hh3cPortWredQueueProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPortWredQueueProbability_Type.__name__ = "Integer32"
_Hh3cPortWredQueueProbability_Object = MibTableColumn
hh3cPortWredQueueProbability = _Hh3cPortWredQueueProbability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 25, 1, 4),
    _Hh3cPortWredQueueProbability_Type()
)
hh3cPortWredQueueProbability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortWredQueueProbability.setStatus("current")
_Hh3cMirroringGroupTable_Object = MibTable
hh3cMirroringGroupTable = _Hh3cMirroringGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupTable.setStatus("current")
_Hh3cMirroringGroupEntry_Object = MibTableRow
hh3cMirroringGroupEntry = _Hh3cMirroringGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26, 1)
)
hh3cMirroringGroupEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupEntry.setStatus("current")


class _Hh3cMirroringGroupID_Type(Integer32):
    """Custom type hh3cMirroringGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Hh3cMirroringGroupID_Type.__name__ = "Integer32"
_Hh3cMirroringGroupID_Object = MibTableColumn
hh3cMirroringGroupID = _Hh3cMirroringGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26, 1, 1),
    _Hh3cMirroringGroupID_Type()
)
hh3cMirroringGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirroringGroupID.setStatus("current")


class _Hh3cMirroringGroupType_Type(Integer32):
    """Custom type hh3cMirroringGroupType based on Integer32"""
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


_Hh3cMirroringGroupType_Type.__name__ = "Integer32"
_Hh3cMirroringGroupType_Object = MibTableColumn
hh3cMirroringGroupType = _Hh3cMirroringGroupType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26, 1, 2),
    _Hh3cMirroringGroupType_Type()
)
hh3cMirroringGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupType.setStatus("current")


class _Hh3cMirroringGroupStatus_Type(Integer32):
    """Custom type hh3cMirroringGroupStatus based on Integer32"""
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


_Hh3cMirroringGroupStatus_Type.__name__ = "Integer32"
_Hh3cMirroringGroupStatus_Object = MibTableColumn
hh3cMirroringGroupStatus = _Hh3cMirroringGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26, 1, 3),
    _Hh3cMirroringGroupStatus_Type()
)
hh3cMirroringGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMirroringGroupStatus.setStatus("current")
_Hh3cMirroringGroupRowStatus_Type = RowStatus
_Hh3cMirroringGroupRowStatus_Object = MibTableColumn
hh3cMirroringGroupRowStatus = _Hh3cMirroringGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 26, 1, 4),
    _Hh3cMirroringGroupRowStatus_Type()
)
hh3cMirroringGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupRowStatus.setStatus("current")
_Hh3cMirroringGroupMirrorTable_Object = MibTable
hh3cMirroringGroupMirrorTable = _Hh3cMirroringGroupMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorTable.setStatus("current")
_Hh3cMirroringGroupMirrorEntry_Object = MibTableRow
hh3cMirroringGroupMirrorEntry = _Hh3cMirroringGroupMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1)
)
hh3cMirroringGroupMirrorEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorEntry.setStatus("current")
_Hh3cMirroringGroupMirrorInboundIfIndexList_Type = OctetString
_Hh3cMirroringGroupMirrorInboundIfIndexList_Object = MibTableColumn
hh3cMirroringGroupMirrorInboundIfIndexList = _Hh3cMirroringGroupMirrorInboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1, 1),
    _Hh3cMirroringGroupMirrorInboundIfIndexList_Type()
)
hh3cMirroringGroupMirrorInboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorInboundIfIndexList.setStatus("current")
_Hh3cMirroringGroupMirrorOutboundIfIndexList_Type = OctetString
_Hh3cMirroringGroupMirrorOutboundIfIndexList_Object = MibTableColumn
hh3cMirroringGroupMirrorOutboundIfIndexList = _Hh3cMirroringGroupMirrorOutboundIfIndexList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1, 2),
    _Hh3cMirroringGroupMirrorOutboundIfIndexList_Type()
)
hh3cMirroringGroupMirrorOutboundIfIndexList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorOutboundIfIndexList.setStatus("current")
_Hh3cMirroringGroupMirrorRowStatus_Type = RowStatus
_Hh3cMirroringGroupMirrorRowStatus_Object = MibTableColumn
hh3cMirroringGroupMirrorRowStatus = _Hh3cMirroringGroupMirrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1, 3),
    _Hh3cMirroringGroupMirrorRowStatus_Type()
)
hh3cMirroringGroupMirrorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorRowStatus.setStatus("current")
_Hh3cMirroringGroupMirrorInTypeList_Type = OctetString
_Hh3cMirroringGroupMirrorInTypeList_Object = MibTableColumn
hh3cMirroringGroupMirrorInTypeList = _Hh3cMirroringGroupMirrorInTypeList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1, 4),
    _Hh3cMirroringGroupMirrorInTypeList_Type()
)
hh3cMirroringGroupMirrorInTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorInTypeList.setStatus("current")
_Hh3cMirroringGroupMirrorOutTypeList_Type = OctetString
_Hh3cMirroringGroupMirrorOutTypeList_Object = MibTableColumn
hh3cMirroringGroupMirrorOutTypeList = _Hh3cMirroringGroupMirrorOutTypeList_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 27, 1, 5),
    _Hh3cMirroringGroupMirrorOutTypeList_Type()
)
hh3cMirroringGroupMirrorOutTypeList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorOutTypeList.setStatus("current")
_Hh3cMirroringGroupMonitorTable_Object = MibTable
hh3cMirroringGroupMonitorTable = _Hh3cMirroringGroupMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 28)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMonitorTable.setStatus("current")
_Hh3cMirroringGroupMonitorEntry_Object = MibTableRow
hh3cMirroringGroupMonitorEntry = _Hh3cMirroringGroupMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 28, 1)
)
hh3cMirroringGroupMonitorEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMonitorEntry.setStatus("current")
_Hh3cMirroringGroupMonitorIfIndex_Type = Integer32
_Hh3cMirroringGroupMonitorIfIndex_Object = MibTableColumn
hh3cMirroringGroupMonitorIfIndex = _Hh3cMirroringGroupMonitorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 28, 1, 1),
    _Hh3cMirroringGroupMonitorIfIndex_Type()
)
hh3cMirroringGroupMonitorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMonitorIfIndex.setStatus("current")
_Hh3cMirroringGroupMonitorRowStatus_Type = RowStatus
_Hh3cMirroringGroupMonitorRowStatus_Object = MibTableColumn
hh3cMirroringGroupMonitorRowStatus = _Hh3cMirroringGroupMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 28, 1, 2),
    _Hh3cMirroringGroupMonitorRowStatus_Type()
)
hh3cMirroringGroupMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMonitorRowStatus.setStatus("current")
_Hh3cMirroringGroupMonitorType_Type = Hh3cMirrorOrMonitorType
_Hh3cMirroringGroupMonitorType_Object = MibTableColumn
hh3cMirroringGroupMonitorType = _Hh3cMirroringGroupMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 28, 1, 3),
    _Hh3cMirroringGroupMonitorType_Type()
)
hh3cMirroringGroupMonitorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMonitorType.setStatus("current")
_Hh3cMirroringGroupReflectorTable_Object = MibTable
hh3cMirroringGroupReflectorTable = _Hh3cMirroringGroupReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 29)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupReflectorTable.setStatus("current")
_Hh3cMirroringGroupReflectorEntry_Object = MibTableRow
hh3cMirroringGroupReflectorEntry = _Hh3cMirroringGroupReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 29, 1)
)
hh3cMirroringGroupReflectorEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupReflectorEntry.setStatus("current")
_Hh3cMirroringGroupReflectorIfIndex_Type = Integer32
_Hh3cMirroringGroupReflectorIfIndex_Object = MibTableColumn
hh3cMirroringGroupReflectorIfIndex = _Hh3cMirroringGroupReflectorIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 29, 1, 1),
    _Hh3cMirroringGroupReflectorIfIndex_Type()
)
hh3cMirroringGroupReflectorIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupReflectorIfIndex.setStatus("current")
_Hh3cMirroringGroupReflectorRowStatus_Type = RowStatus
_Hh3cMirroringGroupReflectorRowStatus_Object = MibTableColumn
hh3cMirroringGroupReflectorRowStatus = _Hh3cMirroringGroupReflectorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 29, 1, 2),
    _Hh3cMirroringGroupReflectorRowStatus_Type()
)
hh3cMirroringGroupReflectorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupReflectorRowStatus.setStatus("current")
_Hh3cMirroringGroupRprobeVlanTable_Object = MibTable
hh3cMirroringGroupRprobeVlanTable = _Hh3cMirroringGroupRprobeVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 30)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupRprobeVlanTable.setStatus("current")
_Hh3cMirroringGroupRprobeVlanEntry_Object = MibTableRow
hh3cMirroringGroupRprobeVlanEntry = _Hh3cMirroringGroupRprobeVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 30, 1)
)
hh3cMirroringGroupRprobeVlanEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupRprobeVlanEntry.setStatus("current")


class _Hh3cMirroringGroupRprobeVlanID_Type(Integer32):
    """Custom type hh3cMirroringGroupRprobeVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cMirroringGroupRprobeVlanID_Type.__name__ = "Integer32"
_Hh3cMirroringGroupRprobeVlanID_Object = MibTableColumn
hh3cMirroringGroupRprobeVlanID = _Hh3cMirroringGroupRprobeVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 30, 1, 1),
    _Hh3cMirroringGroupRprobeVlanID_Type()
)
hh3cMirroringGroupRprobeVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupRprobeVlanID.setStatus("current")
_Hh3cMirroringGroupRprobeVlanRowStatus_Type = RowStatus
_Hh3cMirroringGroupRprobeVlanRowStatus_Object = MibTableColumn
hh3cMirroringGroupRprobeVlanRowStatus = _Hh3cMirroringGroupRprobeVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 30, 1, 2),
    _Hh3cMirroringGroupRprobeVlanRowStatus_Type()
)
hh3cMirroringGroupRprobeVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupRprobeVlanRowStatus.setStatus("current")
_Hh3cMirroringGroupMirrorMacTable_Object = MibTable
hh3cMirroringGroupMirrorMacTable = _Hh3cMirroringGroupMirrorMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorMacTable.setStatus("current")
_Hh3cMirroringGroupMirrorMacEntry_Object = MibTableRow
hh3cMirroringGroupMirrorMacEntry = _Hh3cMirroringGroupMirrorMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31, 1)
)
hh3cMirroringGroupMirrorMacEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupMirrorMacSeq"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorMacEntry.setStatus("current")
_Hh3cMirroringGroupMirrorMacSeq_Type = Integer32
_Hh3cMirroringGroupMirrorMacSeq_Object = MibTableColumn
hh3cMirroringGroupMirrorMacSeq = _Hh3cMirroringGroupMirrorMacSeq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31, 1, 1),
    _Hh3cMirroringGroupMirrorMacSeq_Type()
)
hh3cMirroringGroupMirrorMacSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorMacSeq.setStatus("current")
_Hh3cMirroringGroupMirrorMac_Type = MacAddress
_Hh3cMirroringGroupMirrorMac_Object = MibTableColumn
hh3cMirroringGroupMirrorMac = _Hh3cMirroringGroupMirrorMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31, 1, 2),
    _Hh3cMirroringGroupMirrorMac_Type()
)
hh3cMirroringGroupMirrorMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorMac.setStatus("current")


class _Hh3cMirrorMacVlanID_Type(Integer32):
    """Custom type hh3cMirrorMacVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cMirrorMacVlanID_Type.__name__ = "Integer32"
_Hh3cMirrorMacVlanID_Object = MibTableColumn
hh3cMirrorMacVlanID = _Hh3cMirrorMacVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31, 1, 3),
    _Hh3cMirrorMacVlanID_Type()
)
hh3cMirrorMacVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirrorMacVlanID.setStatus("current")
_Hh3cMirroringGroupMirroMacStatus_Type = RowStatus
_Hh3cMirroringGroupMirroMacStatus_Object = MibTableColumn
hh3cMirroringGroupMirroMacStatus = _Hh3cMirroringGroupMirroMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 31, 1, 4),
    _Hh3cMirroringGroupMirroMacStatus_Type()
)
hh3cMirroringGroupMirroMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirroMacStatus.setStatus("current")
_Hh3cMirroringGroupMirrorVlanTable_Object = MibTable
hh3cMirroringGroupMirrorVlanTable = _Hh3cMirroringGroupMirrorVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32)
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorVlanTable.setStatus("current")
_Hh3cMirroringGroupMirrorVlanEntry_Object = MibTableRow
hh3cMirroringGroupMirrorVlanEntry = _Hh3cMirroringGroupMirrorVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32, 1)
)
hh3cMirroringGroupMirrorVlanEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupID"),
    (0, "HH3C-LswQos-MIB", "hh3cMirroringGroupMirrorVlanSeq"),
)
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorVlanEntry.setStatus("current")
_Hh3cMirroringGroupMirrorVlanSeq_Type = Integer32
_Hh3cMirroringGroupMirrorVlanSeq_Object = MibTableColumn
hh3cMirroringGroupMirrorVlanSeq = _Hh3cMirroringGroupMirrorVlanSeq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32, 1, 1),
    _Hh3cMirroringGroupMirrorVlanSeq_Type()
)
hh3cMirroringGroupMirrorVlanSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorVlanSeq.setStatus("current")


class _Hh3cMirroringGroupMirrorVlanID_Type(Integer32):
    """Custom type hh3cMirroringGroupMirrorVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cMirroringGroupMirrorVlanID_Type.__name__ = "Integer32"
_Hh3cMirroringGroupMirrorVlanID_Object = MibTableColumn
hh3cMirroringGroupMirrorVlanID = _Hh3cMirroringGroupMirrorVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32, 1, 2),
    _Hh3cMirroringGroupMirrorVlanID_Type()
)
hh3cMirroringGroupMirrorVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorVlanID.setStatus("current")


class _Hh3cMirroringGroupMirrorVlanDirection_Type(Integer32):
    """Custom type hh3cMirroringGroupMirrorVlanDirection based on Integer32"""
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


_Hh3cMirroringGroupMirrorVlanDirection_Type.__name__ = "Integer32"
_Hh3cMirroringGroupMirrorVlanDirection_Object = MibTableColumn
hh3cMirroringGroupMirrorVlanDirection = _Hh3cMirroringGroupMirrorVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32, 1, 3),
    _Hh3cMirroringGroupMirrorVlanDirection_Type()
)
hh3cMirroringGroupMirrorVlanDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirrorVlanDirection.setStatus("current")
_Hh3cMirroringGroupMirroVlanStatus_Type = RowStatus
_Hh3cMirroringGroupMirroVlanStatus_Object = MibTableColumn
hh3cMirroringGroupMirroVlanStatus = _Hh3cMirroringGroupMirroVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 32, 1, 4),
    _Hh3cMirroringGroupMirroVlanStatus_Type()
)
hh3cMirroringGroupMirroVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMirroringGroupMirroVlanStatus.setStatus("current")
_Hh3cPortTrustTable_Object = MibTable
hh3cPortTrustTable = _Hh3cPortTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33)
)
if mibBuilder.loadTexts:
    hh3cPortTrustTable.setStatus("current")
_Hh3cPortTrustEntry_Object = MibTableRow
hh3cPortTrustEntry = _Hh3cPortTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33, 1)
)
hh3cPortTrustEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cPortTrustIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortTrustEntry.setStatus("current")
_Hh3cPortTrustIfIndex_Type = Integer32
_Hh3cPortTrustIfIndex_Object = MibTableColumn
hh3cPortTrustIfIndex = _Hh3cPortTrustIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33, 1, 1),
    _Hh3cPortTrustIfIndex_Type()
)
hh3cPortTrustIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortTrustIfIndex.setStatus("current")


class _Hh3cPortTrustTrustType_Type(Integer32):
    """Custom type hh3cPortTrustTrustType based on Integer32"""
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


_Hh3cPortTrustTrustType_Type.__name__ = "Integer32"
_Hh3cPortTrustTrustType_Object = MibTableColumn
hh3cPortTrustTrustType = _Hh3cPortTrustTrustType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33, 1, 2),
    _Hh3cPortTrustTrustType_Type()
)
hh3cPortTrustTrustType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortTrustTrustType.setStatus("current")


class _Hh3cPortTrustOvercastType_Type(Integer32):
    """Custom type hh3cPortTrustOvercastType based on Integer32"""
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


_Hh3cPortTrustOvercastType_Type.__name__ = "Integer32"
_Hh3cPortTrustOvercastType_Object = MibTableColumn
hh3cPortTrustOvercastType = _Hh3cPortTrustOvercastType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33, 1, 3),
    _Hh3cPortTrustOvercastType_Type()
)
hh3cPortTrustOvercastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortTrustOvercastType.setStatus("current")


class _Hh3cPortTrustReset_Type(Integer32):
    """Custom type hh3cPortTrustReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cPortTrustReset_Type.__name__ = "Integer32"
_Hh3cPortTrustReset_Object = MibTableColumn
hh3cPortTrustReset = _Hh3cPortTrustReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 33, 1, 4),
    _Hh3cPortTrustReset_Type()
)
hh3cPortTrustReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPortTrustReset.setStatus("current")
_Hh3cRemarkVlanIDTable_Object = MibTable
hh3cRemarkVlanIDTable = _Hh3cRemarkVlanIDTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34)
)
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDTable.setStatus("current")
_Hh3cRemarkVlanIDEntry_Object = MibTableRow
hh3cRemarkVlanIDEntry = _Hh3cRemarkVlanIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1)
)
hh3cRemarkVlanIDEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cRemarkVlanIDAclIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRemarkVlanIDIfIndex"),
    (0, "HH3C-LswQos-MIB", "hh3cRemarkVlanIDVlanID"),
    (0, "HH3C-LswQos-MIB", "hh3cRemarkVlanIDDirection"),
)
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDEntry.setStatus("current")


class _Hh3cRemarkVlanIDAclIndex_Type(Integer32):
    """Custom type hh3cRemarkVlanIDAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2999),
    )


_Hh3cRemarkVlanIDAclIndex_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDAclIndex_Object = MibTableColumn
hh3cRemarkVlanIDAclIndex = _Hh3cRemarkVlanIDAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 1),
    _Hh3cRemarkVlanIDAclIndex_Type()
)
hh3cRemarkVlanIDAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDAclIndex.setStatus("current")
_Hh3cRemarkVlanIDIfIndex_Type = Integer32
_Hh3cRemarkVlanIDIfIndex_Object = MibTableColumn
hh3cRemarkVlanIDIfIndex = _Hh3cRemarkVlanIDIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 2),
    _Hh3cRemarkVlanIDIfIndex_Type()
)
hh3cRemarkVlanIDIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDIfIndex.setStatus("current")


class _Hh3cRemarkVlanIDVlanID_Type(Integer32):
    """Custom type hh3cRemarkVlanIDVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRemarkVlanIDVlanID_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDVlanID_Object = MibTableColumn
hh3cRemarkVlanIDVlanID = _Hh3cRemarkVlanIDVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 3),
    _Hh3cRemarkVlanIDVlanID_Type()
)
hh3cRemarkVlanIDVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDVlanID.setStatus("current")


class _Hh3cRemarkVlanIDDirection_Type(Integer32):
    """Custom type hh3cRemarkVlanIDDirection based on Integer32"""
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


_Hh3cRemarkVlanIDDirection_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDDirection_Object = MibTableColumn
hh3cRemarkVlanIDDirection = _Hh3cRemarkVlanIDDirection_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 4),
    _Hh3cRemarkVlanIDDirection_Type()
)
hh3cRemarkVlanIDDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDDirection.setStatus("current")


class _Hh3cRemarkVlanIDUserAclNum_Type(Integer32):
    """Custom type hh3cRemarkVlanIDUserAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5000, 5999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRemarkVlanIDUserAclNum_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDUserAclNum_Object = MibTableColumn
hh3cRemarkVlanIDUserAclNum = _Hh3cRemarkVlanIDUserAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 5),
    _Hh3cRemarkVlanIDUserAclNum_Type()
)
hh3cRemarkVlanIDUserAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDUserAclNum.setStatus("current")


class _Hh3cRemarkVlanIDUserAclRule_Type(Integer32):
    """Custom type hh3cRemarkVlanIDUserAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRemarkVlanIDUserAclRule_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDUserAclRule_Object = MibTableColumn
hh3cRemarkVlanIDUserAclRule = _Hh3cRemarkVlanIDUserAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 6),
    _Hh3cRemarkVlanIDUserAclRule_Type()
)
hh3cRemarkVlanIDUserAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDUserAclRule.setStatus("current")


class _Hh3cRemarkVlanIDIpAclNum_Type(Integer32):
    """Custom type hh3cRemarkVlanIDIpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRemarkVlanIDIpAclNum_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDIpAclNum_Object = MibTableColumn
hh3cRemarkVlanIDIpAclNum = _Hh3cRemarkVlanIDIpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 7),
    _Hh3cRemarkVlanIDIpAclNum_Type()
)
hh3cRemarkVlanIDIpAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDIpAclNum.setStatus("current")


class _Hh3cRemarkVlanIDIpAclRule_Type(Integer32):
    """Custom type hh3cRemarkVlanIDIpAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRemarkVlanIDIpAclRule_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDIpAclRule_Object = MibTableColumn
hh3cRemarkVlanIDIpAclRule = _Hh3cRemarkVlanIDIpAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 8),
    _Hh3cRemarkVlanIDIpAclRule_Type()
)
hh3cRemarkVlanIDIpAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDIpAclRule.setStatus("current")


class _Hh3cRemarkVlanIDLinkAclNum_Type(Integer32):
    """Custom type hh3cRemarkVlanIDLinkAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4000, 4999),
        ValueRangeConstraint(10000, 12999),
    )


_Hh3cRemarkVlanIDLinkAclNum_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDLinkAclNum_Object = MibTableColumn
hh3cRemarkVlanIDLinkAclNum = _Hh3cRemarkVlanIDLinkAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 9),
    _Hh3cRemarkVlanIDLinkAclNum_Type()
)
hh3cRemarkVlanIDLinkAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDLinkAclNum.setStatus("current")


class _Hh3cRemarkVlanIDLinkAclRule_Type(Integer32):
    """Custom type hh3cRemarkVlanIDLinkAclRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cRemarkVlanIDLinkAclRule_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDLinkAclRule_Object = MibTableColumn
hh3cRemarkVlanIDLinkAclRule = _Hh3cRemarkVlanIDLinkAclRule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 10),
    _Hh3cRemarkVlanIDLinkAclRule_Type()
)
hh3cRemarkVlanIDLinkAclRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDLinkAclRule.setStatus("current")


class _Hh3cRemarkVlanIDRemarkVlanID_Type(Integer32):
    """Custom type hh3cRemarkVlanIDRemarkVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cRemarkVlanIDRemarkVlanID_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDRemarkVlanID_Object = MibTableColumn
hh3cRemarkVlanIDRemarkVlanID = _Hh3cRemarkVlanIDRemarkVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 11),
    _Hh3cRemarkVlanIDRemarkVlanID_Type()
)
hh3cRemarkVlanIDRemarkVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDRemarkVlanID.setStatus("current")


class _Hh3cRemarkVlanIDPacketType_Type(Integer32):
    """Custom type hh3cRemarkVlanIDPacketType based on Integer32"""
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


_Hh3cRemarkVlanIDPacketType_Type.__name__ = "Integer32"
_Hh3cRemarkVlanIDPacketType_Object = MibTableColumn
hh3cRemarkVlanIDPacketType = _Hh3cRemarkVlanIDPacketType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 12),
    _Hh3cRemarkVlanIDPacketType_Type()
)
hh3cRemarkVlanIDPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDPacketType.setStatus("current")
_Hh3cRemarkVlanIDRowStatus_Type = RowStatus
_Hh3cRemarkVlanIDRowStatus_Object = MibTableColumn
hh3cRemarkVlanIDRowStatus = _Hh3cRemarkVlanIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 34, 1, 13),
    _Hh3cRemarkVlanIDRowStatus_Type()
)
hh3cRemarkVlanIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cRemarkVlanIDRowStatus.setStatus("current")
_Hh3cCosToDscpMapTable_Object = MibTable
hh3cCosToDscpMapTable = _Hh3cCosToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 35)
)
if mibBuilder.loadTexts:
    hh3cCosToDscpMapTable.setStatus("current")
_Hh3cCosToDscpMapEntry_Object = MibTableRow
hh3cCosToDscpMapEntry = _Hh3cCosToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 35, 1)
)
hh3cCosToDscpMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cCosToDscpMapCosIndex"),
)
if mibBuilder.loadTexts:
    hh3cCosToDscpMapEntry.setStatus("current")


class _Hh3cCosToDscpMapCosIndex_Type(Integer32):
    """Custom type hh3cCosToDscpMapCosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cCosToDscpMapCosIndex_Type.__name__ = "Integer32"
_Hh3cCosToDscpMapCosIndex_Object = MibTableColumn
hh3cCosToDscpMapCosIndex = _Hh3cCosToDscpMapCosIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 35, 1, 1),
    _Hh3cCosToDscpMapCosIndex_Type()
)
hh3cCosToDscpMapCosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cCosToDscpMapCosIndex.setStatus("current")


class _Hh3cCosToDscpMapDscpValue_Type(Integer32):
    """Custom type hh3cCosToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cCosToDscpMapDscpValue_Type.__name__ = "Integer32"
_Hh3cCosToDscpMapDscpValue_Object = MibTableColumn
hh3cCosToDscpMapDscpValue = _Hh3cCosToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 35, 1, 2),
    _Hh3cCosToDscpMapDscpValue_Type()
)
hh3cCosToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCosToDscpMapDscpValue.setStatus("current")


class _Hh3cCosToDscpMapReSet_Type(Integer32):
    """Custom type hh3cCosToDscpMapReSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cCosToDscpMapReSet_Type.__name__ = "Integer32"
_Hh3cCosToDscpMapReSet_Object = MibTableColumn
hh3cCosToDscpMapReSet = _Hh3cCosToDscpMapReSet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 35, 1, 3),
    _Hh3cCosToDscpMapReSet_Type()
)
hh3cCosToDscpMapReSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cCosToDscpMapReSet.setStatus("current")
_Hh3cDscpToLocalPreMapTable_Object = MibTable
hh3cDscpToLocalPreMapTable = _Hh3cDscpToLocalPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 36)
)
if mibBuilder.loadTexts:
    hh3cDscpToLocalPreMapTable.setStatus("current")
_Hh3cDscpToLocalPreMapEntry_Object = MibTableRow
hh3cDscpToLocalPreMapEntry = _Hh3cDscpToLocalPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 36, 1)
)
hh3cDscpToLocalPreMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDscpToLocalPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hh3cDscpToLocalPreMapEntry.setStatus("current")


class _Hh3cDscpToLocalPreMapDscpIndex_Type(Integer32):
    """Custom type hh3cDscpToLocalPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpToLocalPreMapDscpIndex_Type.__name__ = "Integer32"
_Hh3cDscpToLocalPreMapDscpIndex_Object = MibTableColumn
hh3cDscpToLocalPreMapDscpIndex = _Hh3cDscpToLocalPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 36, 1, 1),
    _Hh3cDscpToLocalPreMapDscpIndex_Type()
)
hh3cDscpToLocalPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDscpToLocalPreMapDscpIndex.setStatus("current")


class _Hh3cDscpToLocalPreMapLocalPreVal_Type(Integer32):
    """Custom type hh3cDscpToLocalPreMapLocalPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDscpToLocalPreMapLocalPreVal_Type.__name__ = "Integer32"
_Hh3cDscpToLocalPreMapLocalPreVal_Object = MibTableColumn
hh3cDscpToLocalPreMapLocalPreVal = _Hh3cDscpToLocalPreMapLocalPreVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 36, 1, 2),
    _Hh3cDscpToLocalPreMapLocalPreVal_Type()
)
hh3cDscpToLocalPreMapLocalPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToLocalPreMapLocalPreVal.setStatus("current")


class _Hh3cDscpToLocalPreMapReset_Type(Integer32):
    """Custom type hh3cDscpToLocalPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDscpToLocalPreMapReset_Type.__name__ = "Integer32"
_Hh3cDscpToLocalPreMapReset_Object = MibTableColumn
hh3cDscpToLocalPreMapReset = _Hh3cDscpToLocalPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 36, 1, 3),
    _Hh3cDscpToLocalPreMapReset_Type()
)
hh3cDscpToLocalPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToLocalPreMapReset.setStatus("current")
_Hh3cDscpToDropPreMapTable_Object = MibTable
hh3cDscpToDropPreMapTable = _Hh3cDscpToDropPreMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 37)
)
if mibBuilder.loadTexts:
    hh3cDscpToDropPreMapTable.setStatus("current")
_Hh3cDscpToDropPreMapEntry_Object = MibTableRow
hh3cDscpToDropPreMapEntry = _Hh3cDscpToDropPreMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 37, 1)
)
hh3cDscpToDropPreMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDscpToDropPreMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hh3cDscpToDropPreMapEntry.setStatus("current")


class _Hh3cDscpToDropPreMapDscpIndex_Type(Integer32):
    """Custom type hh3cDscpToDropPreMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpToDropPreMapDscpIndex_Type.__name__ = "Integer32"
_Hh3cDscpToDropPreMapDscpIndex_Object = MibTableColumn
hh3cDscpToDropPreMapDscpIndex = _Hh3cDscpToDropPreMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 37, 1, 1),
    _Hh3cDscpToDropPreMapDscpIndex_Type()
)
hh3cDscpToDropPreMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDscpToDropPreMapDscpIndex.setStatus("current")


class _Hh3cDscpToDropPreMapDropPreVal_Type(Integer32):
    """Custom type hh3cDscpToDropPreMapDropPreVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hh3cDscpToDropPreMapDropPreVal_Type.__name__ = "Integer32"
_Hh3cDscpToDropPreMapDropPreVal_Object = MibTableColumn
hh3cDscpToDropPreMapDropPreVal = _Hh3cDscpToDropPreMapDropPreVal_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 37, 1, 2),
    _Hh3cDscpToDropPreMapDropPreVal_Type()
)
hh3cDscpToDropPreMapDropPreVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToDropPreMapDropPreVal.setStatus("current")


class _Hh3cDscpToDropPreMapReset_Type(Integer32):
    """Custom type hh3cDscpToDropPreMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDscpToDropPreMapReset_Type.__name__ = "Integer32"
_Hh3cDscpToDropPreMapReset_Object = MibTableColumn
hh3cDscpToDropPreMapReset = _Hh3cDscpToDropPreMapReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 37, 1, 3),
    _Hh3cDscpToDropPreMapReset_Type()
)
hh3cDscpToDropPreMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToDropPreMapReset.setStatus("current")
_Hh3cDscpToCosMapTable_Object = MibTable
hh3cDscpToCosMapTable = _Hh3cDscpToCosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 38)
)
if mibBuilder.loadTexts:
    hh3cDscpToCosMapTable.setStatus("current")
_Hh3cDscpToCosMapEntry_Object = MibTableRow
hh3cDscpToCosMapEntry = _Hh3cDscpToCosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 38, 1)
)
hh3cDscpToCosMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDscpToCosMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hh3cDscpToCosMapEntry.setStatus("current")


class _Hh3cDscpToCosMapDscpIndex_Type(Integer32):
    """Custom type hh3cDscpToCosMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpToCosMapDscpIndex_Type.__name__ = "Integer32"
_Hh3cDscpToCosMapDscpIndex_Object = MibTableColumn
hh3cDscpToCosMapDscpIndex = _Hh3cDscpToCosMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 38, 1, 1),
    _Hh3cDscpToCosMapDscpIndex_Type()
)
hh3cDscpToCosMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDscpToCosMapDscpIndex.setStatus("current")


class _Hh3cDscpToCosMapCosValue_Type(Integer32):
    """Custom type hh3cDscpToCosMapCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hh3cDscpToCosMapCosValue_Type.__name__ = "Integer32"
_Hh3cDscpToCosMapCosValue_Object = MibTableColumn
hh3cDscpToCosMapCosValue = _Hh3cDscpToCosMapCosValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 38, 1, 2),
    _Hh3cDscpToCosMapCosValue_Type()
)
hh3cDscpToCosMapCosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToCosMapCosValue.setStatus("current")


class _Hh3cDscpToCosMapReset_Type(Integer32):
    """Custom type hh3cDscpToCosMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDscpToCosMapReset_Type.__name__ = "Integer32"
_Hh3cDscpToCosMapReset_Object = MibTableColumn
hh3cDscpToCosMapReset = _Hh3cDscpToCosMapReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 38, 1, 3),
    _Hh3cDscpToCosMapReset_Type()
)
hh3cDscpToCosMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToCosMapReset.setStatus("current")
_Hh3cDscpToDscpMapTable_Object = MibTable
hh3cDscpToDscpMapTable = _Hh3cDscpToDscpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 39)
)
if mibBuilder.loadTexts:
    hh3cDscpToDscpMapTable.setStatus("current")
_Hh3cDscpToDscpMapEntry_Object = MibTableRow
hh3cDscpToDscpMapEntry = _Hh3cDscpToDscpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 39, 1)
)
hh3cDscpToDscpMapEntry.setIndexNames(
    (0, "HH3C-LswQos-MIB", "hh3cDscpToDscpMapDscpIndex"),
)
if mibBuilder.loadTexts:
    hh3cDscpToDscpMapEntry.setStatus("current")


class _Hh3cDscpToDscpMapDscpIndex_Type(Integer32):
    """Custom type hh3cDscpToDscpMapDscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpToDscpMapDscpIndex_Type.__name__ = "Integer32"
_Hh3cDscpToDscpMapDscpIndex_Object = MibTableColumn
hh3cDscpToDscpMapDscpIndex = _Hh3cDscpToDscpMapDscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 39, 1, 1),
    _Hh3cDscpToDscpMapDscpIndex_Type()
)
hh3cDscpToDscpMapDscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDscpToDscpMapDscpIndex.setStatus("current")


class _Hh3cDscpToDscpMapDscpValue_Type(Integer32):
    """Custom type hh3cDscpToDscpMapDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Hh3cDscpToDscpMapDscpValue_Type.__name__ = "Integer32"
_Hh3cDscpToDscpMapDscpValue_Object = MibTableColumn
hh3cDscpToDscpMapDscpValue = _Hh3cDscpToDscpMapDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 39, 1, 2),
    _Hh3cDscpToDscpMapDscpValue_Type()
)
hh3cDscpToDscpMapDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToDscpMapDscpValue.setStatus("current")


class _Hh3cDscpToDscpMapReset_Type(Integer32):
    """Custom type hh3cDscpToDscpMapReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Hh3cDscpToDscpMapReset_Type.__name__ = "Integer32"
_Hh3cDscpToDscpMapReset_Object = MibTableColumn
hh3cDscpToDscpMapReset = _Hh3cDscpToDscpMapReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 16, 2, 39, 1, 3),
    _Hh3cDscpToDscpMapReset_Type()
)
hh3cDscpToDscpMapReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDscpToDscpMapReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswQos-MIB",
    **{"Hh3cMirrorOrMonitorType": Hh3cMirrorOrMonitorType,
       "hh3cLswQosAclMib": hh3cLswQosAclMib,
       "hh3cLswQosMibObject": hh3cLswQosMibObject,
       "hh3cPriorityTrustMode": hh3cPriorityTrustMode,
       "hh3cPortMonitorBothIfIndex": hh3cPortMonitorBothIfIndex,
       "hh3cQueueTable": hh3cQueueTable,
       "hh3cQueueEntry": hh3cQueueEntry,
       "hh3cQueueIfIndex": hh3cQueueIfIndex,
       "hh3cQueueScheduleMode": hh3cQueueScheduleMode,
       "hh3cQueueWeight1": hh3cQueueWeight1,
       "hh3cQueueWeight2": hh3cQueueWeight2,
       "hh3cQueueWeight3": hh3cQueueWeight3,
       "hh3cQueueWeight4": hh3cQueueWeight4,
       "hh3cQueueMaxDelay": hh3cQueueMaxDelay,
       "hh3cQueueWeight5": hh3cQueueWeight5,
       "hh3cQueueWeight6": hh3cQueueWeight6,
       "hh3cQueueWeight7": hh3cQueueWeight7,
       "hh3cQueueWeight8": hh3cQueueWeight8,
       "hh3cRateLimitTable": hh3cRateLimitTable,
       "hh3cRateLimitEntry": hh3cRateLimitEntry,
       "hh3cRateLimitAclIndex": hh3cRateLimitAclIndex,
       "hh3cRateLimitIfIndex": hh3cRateLimitIfIndex,
       "hh3cRateLimitVlanID": hh3cRateLimitVlanID,
       "hh3cRateLimitDirection": hh3cRateLimitDirection,
       "hh3cRateLimitUserAclNum": hh3cRateLimitUserAclNum,
       "hh3cRateLimitUserAclRule": hh3cRateLimitUserAclRule,
       "hh3cRateLimitIpAclNum": hh3cRateLimitIpAclNum,
       "hh3cRateLimitIpAclRule": hh3cRateLimitIpAclRule,
       "hh3cRateLimitLinkAclNum": hh3cRateLimitLinkAclNum,
       "hh3cRateLimitLinkAclRule": hh3cRateLimitLinkAclRule,
       "hh3cRateLimitTargetRateMbps": hh3cRateLimitTargetRateMbps,
       "hh3cRateLimitTargetRateKbps": hh3cRateLimitTargetRateKbps,
       "hh3cRateLimitPeakRate": hh3cRateLimitPeakRate,
       "hh3cRateLimitCIR": hh3cRateLimitCIR,
       "hh3cRateLimitCBS": hh3cRateLimitCBS,
       "hh3cRateLimitEBS": hh3cRateLimitEBS,
       "hh3cRateLimitPIR": hh3cRateLimitPIR,
       "hh3cRateLimitConformLocalPre": hh3cRateLimitConformLocalPre,
       "hh3cRateLimitConformActionType": hh3cRateLimitConformActionType,
       "hh3cRateLimitExceedActionType": hh3cRateLimitExceedActionType,
       "hh3cRateLimitExceedDscp": hh3cRateLimitExceedDscp,
       "hh3cRateLimitRuntime": hh3cRateLimitRuntime,
       "hh3cRateLimitRowStatus": hh3cRateLimitRowStatus,
       "hh3cRateLimitExceedCos": hh3cRateLimitExceedCos,
       "hh3cRateLimitConformCos": hh3cRateLimitConformCos,
       "hh3cRateLimitConformDscp": hh3cRateLimitConformDscp,
       "hh3cRateLimitMeterStatByteCount": hh3cRateLimitMeterStatByteCount,
       "hh3cRateLimitMeterStatByteXCount": hh3cRateLimitMeterStatByteXCount,
       "hh3cRateLimitMeterStatState": hh3cRateLimitMeterStatState,
       "hh3cPriorityTable": hh3cPriorityTable,
       "hh3cPriorityEntry": hh3cPriorityEntry,
       "hh3cPriorityAclIndex": hh3cPriorityAclIndex,
       "hh3cPriorityIfIndex": hh3cPriorityIfIndex,
       "hh3cPriorityVlanID": hh3cPriorityVlanID,
       "hh3cPriorityDirection": hh3cPriorityDirection,
       "hh3cPriorityUserAclNum": hh3cPriorityUserAclNum,
       "hh3cPriorityUserAclRule": hh3cPriorityUserAclRule,
       "hh3cPriorityIpAclNum": hh3cPriorityIpAclNum,
       "hh3cPriorityIpAclRule": hh3cPriorityIpAclRule,
       "hh3cPriorityLinkAclNum": hh3cPriorityLinkAclNum,
       "hh3cPriorityLinkAclRule": hh3cPriorityLinkAclRule,
       "hh3cPriorityDscp": hh3cPriorityDscp,
       "hh3cPriorityIpPre": hh3cPriorityIpPre,
       "hh3cPriorityIpPreFromCos": hh3cPriorityIpPreFromCos,
       "hh3cPriorityCos": hh3cPriorityCos,
       "hh3cPriorityCosFromIpPre": hh3cPriorityCosFromIpPre,
       "hh3cPriorityLocalPre": hh3cPriorityLocalPre,
       "hh3cPriorityPolicedServiceType": hh3cPriorityPolicedServiceType,
       "hh3cPriorityPolicedServiceDscp": hh3cPriorityPolicedServiceDscp,
       "hh3cPriorityPolicedServiceExp": hh3cPriorityPolicedServiceExp,
       "hh3cPriorityPolicedServiceCos": hh3cPriorityPolicedServiceCos,
       "hh3cPriorityPolicedServiceLoaclPre": hh3cPriorityPolicedServiceLoaclPre,
       "hh3cPriorityPolicedServiceDropPriority": hh3cPriorityPolicedServiceDropPriority,
       "hh3cPriorityRuntime": hh3cPriorityRuntime,
       "hh3cPriorityRowStatus": hh3cPriorityRowStatus,
       "hh3cRedirectTable": hh3cRedirectTable,
       "hh3cRedirectEntry": hh3cRedirectEntry,
       "hh3cRedirectAclIndex": hh3cRedirectAclIndex,
       "hh3cRedirectIfIndex": hh3cRedirectIfIndex,
       "hh3cRedirectVlanID": hh3cRedirectVlanID,
       "hh3cRedirectDirection": hh3cRedirectDirection,
       "hh3cRedirectUserAclNum": hh3cRedirectUserAclNum,
       "hh3cRedirectUserAclRule": hh3cRedirectUserAclRule,
       "hh3cRedirectIpAclNum": hh3cRedirectIpAclNum,
       "hh3cRedirectIpAclRule": hh3cRedirectIpAclRule,
       "hh3cRedirectLinkAclNum": hh3cRedirectLinkAclNum,
       "hh3cRedirectLinkAclRule": hh3cRedirectLinkAclRule,
       "hh3cRedirectToCpu": hh3cRedirectToCpu,
       "hh3cRedirectToIfIndex": hh3cRedirectToIfIndex,
       "hh3cRedirectToNextHop1": hh3cRedirectToNextHop1,
       "hh3cRedirectToNextHop2": hh3cRedirectToNextHop2,
       "hh3cRedirectRuntime": hh3cRedirectRuntime,
       "hh3cRedirectRowStatus": hh3cRedirectRowStatus,
       "hh3cRedirectToSlotNo": hh3cRedirectToSlotNo,
       "hh3cRedirectRemarkedDSCP": hh3cRedirectRemarkedDSCP,
       "hh3cRedirectRemarkedPri": hh3cRedirectRemarkedPri,
       "hh3cRedirectRemarkedTos": hh3cRedirectRemarkedTos,
       "hh3cRedirectToNextHop3": hh3cRedirectToNextHop3,
       "hh3cRedirectTargetVlanID": hh3cRedirectTargetVlanID,
       "hh3cRedirectMode": hh3cRedirectMode,
       "hh3cRedirectToNestedVlanID": hh3cRedirectToNestedVlanID,
       "hh3cRedirectToModifiedVlanID": hh3cRedirectToModifiedVlanID,
       "hh3cStatisticTable": hh3cStatisticTable,
       "hh3cStatisticEntry": hh3cStatisticEntry,
       "hh3cStatisticAclIndex": hh3cStatisticAclIndex,
       "hh3cStatisticIfIndex": hh3cStatisticIfIndex,
       "hh3cStatisticVlanID": hh3cStatisticVlanID,
       "hh3cStatisticDirection": hh3cStatisticDirection,
       "hh3cStatisticUserAclNum": hh3cStatisticUserAclNum,
       "hh3cStatisticUserAclRule": hh3cStatisticUserAclRule,
       "hh3cStatisticIpAclNum": hh3cStatisticIpAclNum,
       "hh3cStatisticIpAclRule": hh3cStatisticIpAclRule,
       "hh3cStatisticLinkAclNum": hh3cStatisticLinkAclNum,
       "hh3cStatisticLinkAclRule": hh3cStatisticLinkAclRule,
       "hh3cStatisticRuntime": hh3cStatisticRuntime,
       "hh3cStatisticPacketCount": hh3cStatisticPacketCount,
       "hh3cStatisticByteCount": hh3cStatisticByteCount,
       "hh3cStatisticCountClear": hh3cStatisticCountClear,
       "hh3cStatisticRowStatus": hh3cStatisticRowStatus,
       "hh3cStatisticPacketXCount": hh3cStatisticPacketXCount,
       "hh3cStatisticByteXCount": hh3cStatisticByteXCount,
       "hh3cMirrorTable": hh3cMirrorTable,
       "hh3cMirrorEntry": hh3cMirrorEntry,
       "hh3cMirrorAclIndex": hh3cMirrorAclIndex,
       "hh3cMirrorIfIndex": hh3cMirrorIfIndex,
       "hh3cMirrorVlanID": hh3cMirrorVlanID,
       "hh3cMirrorDirection": hh3cMirrorDirection,
       "hh3cMirrorUserAclNum": hh3cMirrorUserAclNum,
       "hh3cMirrorUserAclRule": hh3cMirrorUserAclRule,
       "hh3cMirrorIpAclNum": hh3cMirrorIpAclNum,
       "hh3cMirrorIpAclRule": hh3cMirrorIpAclRule,
       "hh3cMirrorLinkAclNum": hh3cMirrorLinkAclNum,
       "hh3cMirrorLinkAclRule": hh3cMirrorLinkAclRule,
       "hh3cMirrorToIfIndex": hh3cMirrorToIfIndex,
       "hh3cMirrorToCpu": hh3cMirrorToCpu,
       "hh3cMirrorRuntime": hh3cMirrorRuntime,
       "hh3cMirrorRowStatus": hh3cMirrorRowStatus,
       "hh3cMirrorToGroup": hh3cMirrorToGroup,
       "hh3cPortMirrorTable": hh3cPortMirrorTable,
       "hh3cPortMirrorEntry": hh3cPortMirrorEntry,
       "hh3cPortMirrorIfIndex": hh3cPortMirrorIfIndex,
       "hh3cPortMirrorDirection": hh3cPortMirrorDirection,
       "hh3cPortMirrorRowStatus": hh3cPortMirrorRowStatus,
       "hh3cLineRateTable": hh3cLineRateTable,
       "hh3cLineRateEntry": hh3cLineRateEntry,
       "hh3cLineRateIfIndex": hh3cLineRateIfIndex,
       "hh3cLineRateDirection": hh3cLineRateDirection,
       "hh3cLineRateValue": hh3cLineRateValue,
       "hh3cLineRateRowStatus": hh3cLineRateRowStatus,
       "hh3cBandwidthTable": hh3cBandwidthTable,
       "hh3cBandwidthEntry": hh3cBandwidthEntry,
       "hh3cBandwidthAclIndex": hh3cBandwidthAclIndex,
       "hh3cBandwidthIfIndex": hh3cBandwidthIfIndex,
       "hh3cBandwidthVlanID": hh3cBandwidthVlanID,
       "hh3cBandwidthDirection": hh3cBandwidthDirection,
       "hh3cBandwidthIpAclNum": hh3cBandwidthIpAclNum,
       "hh3cBandwidthIpAclRule": hh3cBandwidthIpAclRule,
       "hh3cBandwidthLinkAclNum": hh3cBandwidthLinkAclNum,
       "hh3cBandwidthLinkAclRule": hh3cBandwidthLinkAclRule,
       "hh3cBandwidthMinGuaranteedWidth": hh3cBandwidthMinGuaranteedWidth,
       "hh3cBandwidthMaxGuaranteedWidth": hh3cBandwidthMaxGuaranteedWidth,
       "hh3cBandwidthWeight": hh3cBandwidthWeight,
       "hh3cBandwidthRuntime": hh3cBandwidthRuntime,
       "hh3cBandwidthRowStatus": hh3cBandwidthRowStatus,
       "hh3cRedTable": hh3cRedTable,
       "hh3cRedEntry": hh3cRedEntry,
       "hh3cRedAclIndex": hh3cRedAclIndex,
       "hh3cRedIfIndex": hh3cRedIfIndex,
       "hh3cRedVlanID": hh3cRedVlanID,
       "hh3cRedDirection": hh3cRedDirection,
       "hh3cRedIpAclNum": hh3cRedIpAclNum,
       "hh3cRedIpAclRule": hh3cRedIpAclRule,
       "hh3cRedLinkAclNum": hh3cRedLinkAclNum,
       "hh3cRedLinkAclRule": hh3cRedLinkAclRule,
       "hh3cRedStartQueueLen": hh3cRedStartQueueLen,
       "hh3cRedStopQueueLen": hh3cRedStopQueueLen,
       "hh3cRedProbability": hh3cRedProbability,
       "hh3cRedRuntime": hh3cRedRuntime,
       "hh3cRedRowStatus": hh3cRedRowStatus,
       "hh3cMirrorGroupTable": hh3cMirrorGroupTable,
       "hh3cMirrorGroupEntry": hh3cMirrorGroupEntry,
       "hh3cMirrorGroupID": hh3cMirrorGroupID,
       "hh3cMirrorGroupDirection": hh3cMirrorGroupDirection,
       "hh3cMirrorGroupMirrorIfIndexList": hh3cMirrorGroupMirrorIfIndexList,
       "hh3cMirrorGroupMonitorIfIndex": hh3cMirrorGroupMonitorIfIndex,
       "hh3cMirrorGroupRowStatus": hh3cMirrorGroupRowStatus,
       "hh3cFlowtempTable": hh3cFlowtempTable,
       "hh3cFlowtempEntry": hh3cFlowtempEntry,
       "hh3cFlowtempIndex": hh3cFlowtempIndex,
       "hh3cFlowtempIpProtocol": hh3cFlowtempIpProtocol,
       "hh3cFlowtempTcpFlag": hh3cFlowtempTcpFlag,
       "hh3cFlowtempSPort": hh3cFlowtempSPort,
       "hh3cFlowtempDPort": hh3cFlowtempDPort,
       "hh3cFlowtempIcmpType": hh3cFlowtempIcmpType,
       "hh3cFlowtempIcmpCode": hh3cFlowtempIcmpCode,
       "hh3cFlowtempFragment": hh3cFlowtempFragment,
       "hh3cFlowtempDscp": hh3cFlowtempDscp,
       "hh3cFlowtempIpPre": hh3cFlowtempIpPre,
       "hh3cFlowtempTos": hh3cFlowtempTos,
       "hh3cFlowtempSIp": hh3cFlowtempSIp,
       "hh3cFlowtempSIpMask": hh3cFlowtempSIpMask,
       "hh3cFlowtempDIp": hh3cFlowtempDIp,
       "hh3cFlowtempDIpMask": hh3cFlowtempDIpMask,
       "hh3cFlowtempEthProtocol": hh3cFlowtempEthProtocol,
       "hh3cFlowtempSMac": hh3cFlowtempSMac,
       "hh3cFlowtempSMacMask": hh3cFlowtempSMacMask,
       "hh3cFlowtempDMac": hh3cFlowtempDMac,
       "hh3cFlowtempDMacMask": hh3cFlowtempDMacMask,
       "hh3cFlowtempVpn": hh3cFlowtempVpn,
       "hh3cFlowtempRowStatus": hh3cFlowtempRowStatus,
       "hh3cFlowtempVlanId": hh3cFlowtempVlanId,
       "hh3cFlowtempCos": hh3cFlowtempCos,
       "hh3cFlowtempEnableTable": hh3cFlowtempEnableTable,
       "hh3cFlowtempEnableEntry": hh3cFlowtempEnableEntry,
       "hh3cFlowtempEnableIfIndex": hh3cFlowtempEnableIfIndex,
       "hh3cFlowtempEnableVlanID": hh3cFlowtempEnableVlanID,
       "hh3cFlowtempEnableFlowtempIndex": hh3cFlowtempEnableFlowtempIndex,
       "hh3cTrafficShapeTable": hh3cTrafficShapeTable,
       "hh3cTrafficShapeEntry": hh3cTrafficShapeEntry,
       "hh3cTrafficShapeIfIndex": hh3cTrafficShapeIfIndex,
       "hh3cTrafficShapeQueueId": hh3cTrafficShapeQueueId,
       "hh3cTrafficShapeMaxRate": hh3cTrafficShapeMaxRate,
       "hh3cTrafficShapeBurstSize": hh3cTrafficShapeBurstSize,
       "hh3cTrafficShapeBufferLimit": hh3cTrafficShapeBufferLimit,
       "hh3cTrafficShapeRowStatus": hh3cTrafficShapeRowStatus,
       "hh3cPortQueueTable": hh3cPortQueueTable,
       "hh3cPortQueueEntry": hh3cPortQueueEntry,
       "hh3cPortQueueIfIndex": hh3cPortQueueIfIndex,
       "hh3cPortQueueQueueID": hh3cPortQueueQueueID,
       "hh3cPortQueueWrrPriority": hh3cPortQueueWrrPriority,
       "hh3cPortQueueWeight": hh3cPortQueueWeight,
       "hh3cDropModeTable": hh3cDropModeTable,
       "hh3cDropModeEntry": hh3cDropModeEntry,
       "hh3cDropModeIfIndex": hh3cDropModeIfIndex,
       "hh3cDropModeMode": hh3cDropModeMode,
       "hh3cDropModeWredIndex": hh3cDropModeWredIndex,
       "hh3cWredTable": hh3cWredTable,
       "hh3cWredEntry": hh3cWredEntry,
       "hh3cWredIndex": hh3cWredIndex,
       "hh3cWredQueueId": hh3cWredQueueId,
       "hh3cWredGreenMinThreshold": hh3cWredGreenMinThreshold,
       "hh3cWredGreenMaxThreshold": hh3cWredGreenMaxThreshold,
       "hh3cWredGreenMaxProb": hh3cWredGreenMaxProb,
       "hh3cWredYellowMinThreshold": hh3cWredYellowMinThreshold,
       "hh3cWredYellowMaxThreshold": hh3cWredYellowMaxThreshold,
       "hh3cWredYellowMaxProb": hh3cWredYellowMaxProb,
       "hh3cWredRedMinThreshold": hh3cWredRedMinThreshold,
       "hh3cWredRedMaxThreshold": hh3cWredRedMaxThreshold,
       "hh3cWredRedMaxProb": hh3cWredRedMaxProb,
       "hh3cWredExponent": hh3cWredExponent,
       "hh3cCosToLocalPrecedenceMapTable": hh3cCosToLocalPrecedenceMapTable,
       "hh3cCosToLocalPrecedenceMapEntry": hh3cCosToLocalPrecedenceMapEntry,
       "hh3cCosToLocalPrecedenceMapCosIndex": hh3cCosToLocalPrecedenceMapCosIndex,
       "hh3cCosToLocalPrecedenceMapLocalPrecedenceValue": hh3cCosToLocalPrecedenceMapLocalPrecedenceValue,
       "hh3cCosToDropPrecedenceMapTable": hh3cCosToDropPrecedenceMapTable,
       "hh3cCosToDropPrecedenceMapEntry": hh3cCosToDropPrecedenceMapEntry,
       "hh3cCosToDropPrecedenceMapCosIndex": hh3cCosToDropPrecedenceMapCosIndex,
       "hh3cCosToDropPrecedenceMapDropPrecedenceValue": hh3cCosToDropPrecedenceMapDropPrecedenceValue,
       "hh3cDscpMapTable": hh3cDscpMapTable,
       "hh3cDscpMapEntry": hh3cDscpMapEntry,
       "hh3cDscpMapConformLevel": hh3cDscpMapConformLevel,
       "hh3cDscpMapDscpIndex": hh3cDscpMapDscpIndex,
       "hh3cDscpMapDscpValue": hh3cDscpMapDscpValue,
       "hh3cDscpMapExpValue": hh3cDscpMapExpValue,
       "hh3cDscpMapCosValue": hh3cDscpMapCosValue,
       "hh3cDscpMapLocalPrecedence": hh3cDscpMapLocalPrecedence,
       "hh3cDscpMapDropPrecedence": hh3cDscpMapDropPrecedence,
       "hh3cExpMapTable": hh3cExpMapTable,
       "hh3cExpMapEntry": hh3cExpMapEntry,
       "hh3cExpMapConformLevel": hh3cExpMapConformLevel,
       "hh3cExpMapExpIndex": hh3cExpMapExpIndex,
       "hh3cExpMapDscpValue": hh3cExpMapDscpValue,
       "hh3cExpMapExpValue": hh3cExpMapExpValue,
       "hh3cExpMapCosValue": hh3cExpMapCosValue,
       "hh3cExpMapLocalPrecedence": hh3cExpMapLocalPrecedence,
       "hh3cExpMapDropPrecedence": hh3cExpMapDropPrecedence,
       "hh3cLocalPrecedenceMapTable": hh3cLocalPrecedenceMapTable,
       "hh3cLocalPrecedenceMapEntry": hh3cLocalPrecedenceMapEntry,
       "hh3cLocalPrecedenceMapConformLevel": hh3cLocalPrecedenceMapConformLevel,
       "hh3cLocalPrecedenceMapLocalPrecedenceIndex": hh3cLocalPrecedenceMapLocalPrecedenceIndex,
       "hh3cLocalPrecedenceMapCosValue": hh3cLocalPrecedenceMapCosValue,
       "hh3cPortWredTable": hh3cPortWredTable,
       "hh3cPortWredEntry": hh3cPortWredEntry,
       "hh3cPortWredIfIndex": hh3cPortWredIfIndex,
       "hh3cPortWredQueueID": hh3cPortWredQueueID,
       "hh3cPortWredQueueStartLength": hh3cPortWredQueueStartLength,
       "hh3cPortWredQueueProbability": hh3cPortWredQueueProbability,
       "hh3cMirroringGroupTable": hh3cMirroringGroupTable,
       "hh3cMirroringGroupEntry": hh3cMirroringGroupEntry,
       "hh3cMirroringGroupID": hh3cMirroringGroupID,
       "hh3cMirroringGroupType": hh3cMirroringGroupType,
       "hh3cMirroringGroupStatus": hh3cMirroringGroupStatus,
       "hh3cMirroringGroupRowStatus": hh3cMirroringGroupRowStatus,
       "hh3cMirroringGroupMirrorTable": hh3cMirroringGroupMirrorTable,
       "hh3cMirroringGroupMirrorEntry": hh3cMirroringGroupMirrorEntry,
       "hh3cMirroringGroupMirrorInboundIfIndexList": hh3cMirroringGroupMirrorInboundIfIndexList,
       "hh3cMirroringGroupMirrorOutboundIfIndexList": hh3cMirroringGroupMirrorOutboundIfIndexList,
       "hh3cMirroringGroupMirrorRowStatus": hh3cMirroringGroupMirrorRowStatus,
       "hh3cMirroringGroupMirrorInTypeList": hh3cMirroringGroupMirrorInTypeList,
       "hh3cMirroringGroupMirrorOutTypeList": hh3cMirroringGroupMirrorOutTypeList,
       "hh3cMirroringGroupMonitorTable": hh3cMirroringGroupMonitorTable,
       "hh3cMirroringGroupMonitorEntry": hh3cMirroringGroupMonitorEntry,
       "hh3cMirroringGroupMonitorIfIndex": hh3cMirroringGroupMonitorIfIndex,
       "hh3cMirroringGroupMonitorRowStatus": hh3cMirroringGroupMonitorRowStatus,
       "hh3cMirroringGroupMonitorType": hh3cMirroringGroupMonitorType,
       "hh3cMirroringGroupReflectorTable": hh3cMirroringGroupReflectorTable,
       "hh3cMirroringGroupReflectorEntry": hh3cMirroringGroupReflectorEntry,
       "hh3cMirroringGroupReflectorIfIndex": hh3cMirroringGroupReflectorIfIndex,
       "hh3cMirroringGroupReflectorRowStatus": hh3cMirroringGroupReflectorRowStatus,
       "hh3cMirroringGroupRprobeVlanTable": hh3cMirroringGroupRprobeVlanTable,
       "hh3cMirroringGroupRprobeVlanEntry": hh3cMirroringGroupRprobeVlanEntry,
       "hh3cMirroringGroupRprobeVlanID": hh3cMirroringGroupRprobeVlanID,
       "hh3cMirroringGroupRprobeVlanRowStatus": hh3cMirroringGroupRprobeVlanRowStatus,
       "hh3cMirroringGroupMirrorMacTable": hh3cMirroringGroupMirrorMacTable,
       "hh3cMirroringGroupMirrorMacEntry": hh3cMirroringGroupMirrorMacEntry,
       "hh3cMirroringGroupMirrorMacSeq": hh3cMirroringGroupMirrorMacSeq,
       "hh3cMirroringGroupMirrorMac": hh3cMirroringGroupMirrorMac,
       "hh3cMirrorMacVlanID": hh3cMirrorMacVlanID,
       "hh3cMirroringGroupMirroMacStatus": hh3cMirroringGroupMirroMacStatus,
       "hh3cMirroringGroupMirrorVlanTable": hh3cMirroringGroupMirrorVlanTable,
       "hh3cMirroringGroupMirrorVlanEntry": hh3cMirroringGroupMirrorVlanEntry,
       "hh3cMirroringGroupMirrorVlanSeq": hh3cMirroringGroupMirrorVlanSeq,
       "hh3cMirroringGroupMirrorVlanID": hh3cMirroringGroupMirrorVlanID,
       "hh3cMirroringGroupMirrorVlanDirection": hh3cMirroringGroupMirrorVlanDirection,
       "hh3cMirroringGroupMirroVlanStatus": hh3cMirroringGroupMirroVlanStatus,
       "hh3cPortTrustTable": hh3cPortTrustTable,
       "hh3cPortTrustEntry": hh3cPortTrustEntry,
       "hh3cPortTrustIfIndex": hh3cPortTrustIfIndex,
       "hh3cPortTrustTrustType": hh3cPortTrustTrustType,
       "hh3cPortTrustOvercastType": hh3cPortTrustOvercastType,
       "hh3cPortTrustReset": hh3cPortTrustReset,
       "hh3cRemarkVlanIDTable": hh3cRemarkVlanIDTable,
       "hh3cRemarkVlanIDEntry": hh3cRemarkVlanIDEntry,
       "hh3cRemarkVlanIDAclIndex": hh3cRemarkVlanIDAclIndex,
       "hh3cRemarkVlanIDIfIndex": hh3cRemarkVlanIDIfIndex,
       "hh3cRemarkVlanIDVlanID": hh3cRemarkVlanIDVlanID,
       "hh3cRemarkVlanIDDirection": hh3cRemarkVlanIDDirection,
       "hh3cRemarkVlanIDUserAclNum": hh3cRemarkVlanIDUserAclNum,
       "hh3cRemarkVlanIDUserAclRule": hh3cRemarkVlanIDUserAclRule,
       "hh3cRemarkVlanIDIpAclNum": hh3cRemarkVlanIDIpAclNum,
       "hh3cRemarkVlanIDIpAclRule": hh3cRemarkVlanIDIpAclRule,
       "hh3cRemarkVlanIDLinkAclNum": hh3cRemarkVlanIDLinkAclNum,
       "hh3cRemarkVlanIDLinkAclRule": hh3cRemarkVlanIDLinkAclRule,
       "hh3cRemarkVlanIDRemarkVlanID": hh3cRemarkVlanIDRemarkVlanID,
       "hh3cRemarkVlanIDPacketType": hh3cRemarkVlanIDPacketType,
       "hh3cRemarkVlanIDRowStatus": hh3cRemarkVlanIDRowStatus,
       "hh3cCosToDscpMapTable": hh3cCosToDscpMapTable,
       "hh3cCosToDscpMapEntry": hh3cCosToDscpMapEntry,
       "hh3cCosToDscpMapCosIndex": hh3cCosToDscpMapCosIndex,
       "hh3cCosToDscpMapDscpValue": hh3cCosToDscpMapDscpValue,
       "hh3cCosToDscpMapReSet": hh3cCosToDscpMapReSet,
       "hh3cDscpToLocalPreMapTable": hh3cDscpToLocalPreMapTable,
       "hh3cDscpToLocalPreMapEntry": hh3cDscpToLocalPreMapEntry,
       "hh3cDscpToLocalPreMapDscpIndex": hh3cDscpToLocalPreMapDscpIndex,
       "hh3cDscpToLocalPreMapLocalPreVal": hh3cDscpToLocalPreMapLocalPreVal,
       "hh3cDscpToLocalPreMapReset": hh3cDscpToLocalPreMapReset,
       "hh3cDscpToDropPreMapTable": hh3cDscpToDropPreMapTable,
       "hh3cDscpToDropPreMapEntry": hh3cDscpToDropPreMapEntry,
       "hh3cDscpToDropPreMapDscpIndex": hh3cDscpToDropPreMapDscpIndex,
       "hh3cDscpToDropPreMapDropPreVal": hh3cDscpToDropPreMapDropPreVal,
       "hh3cDscpToDropPreMapReset": hh3cDscpToDropPreMapReset,
       "hh3cDscpToCosMapTable": hh3cDscpToCosMapTable,
       "hh3cDscpToCosMapEntry": hh3cDscpToCosMapEntry,
       "hh3cDscpToCosMapDscpIndex": hh3cDscpToCosMapDscpIndex,
       "hh3cDscpToCosMapCosValue": hh3cDscpToCosMapCosValue,
       "hh3cDscpToCosMapReset": hh3cDscpToCosMapReset,
       "hh3cDscpToDscpMapTable": hh3cDscpToDscpMapTable,
       "hh3cDscpToDscpMapEntry": hh3cDscpToDscpMapEntry,
       "hh3cDscpToDscpMapDscpIndex": hh3cDscpToDscpMapDscpIndex,
       "hh3cDscpToDscpMapDscpValue": hh3cDscpToDscpMapDscpValue,
       "hh3cDscpToDscpMapReset": hh3cDscpToDscpMapReset}
)
