# SNMP MIB module (HUAWEI-PIM-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PIM-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:31 2024
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

(IANAipRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipRouteProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetVersion")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hwPimStdMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4)
)
hwPimStdMib.setRevisions(
        ("2014-07-01 00:00",
         "2014-06-20 00:00",
         "2013-05-06 00:00",
         "2007-04-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWPimMode(Integer32, TextualConvention):
    status = "current"
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
        *(("asm", 3),
          ("bidir", 4),
          ("dm", 5),
          ("none", 1),
          ("other", 6),
          ("ssm", 2))
    )



class HWPimGroupMappingOriginType(Integer32, TextualConvention):
    status = "current"
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
        *(("autoRp", 5),
          ("bsr", 4),
          ("configRp", 2),
          ("configSsm", 3),
          ("embedded", 6),
          ("fixed", 1),
          ("other", 7))
    )



class HWPimCtlMsgState(Integer32, TextualConvention):
    status = "current"
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
        *(("filter", 4),
          ("invalid", 3),
          ("recv", 1),
          ("sent", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwMcast_ObjectIdentity = ObjectIdentity
hwMcast = _HwMcast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149)
)
_HwPimNotifications_ObjectIdentity = ObjectIdentity
hwPimNotifications = _HwPimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0)
)
_HwPim_ObjectIdentity = ObjectIdentity
hwPim = _HwPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1)
)
_HwPimInterfaceTable_Object = MibTable
hwPimInterfaceTable = _HwPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwPimInterfaceTable.setStatus("current")
_HwPimInterfaceEntry_Object = MibTableRow
hwPimInterfaceEntry = _HwPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1)
)
hwPimInterfaceEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimInterfaceIfIndex"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimInterfaceIpVersion"),
)
if mibBuilder.loadTexts:
    hwPimInterfaceEntry.setStatus("current")
_HwPimInterfaceIfIndex_Type = InterfaceIndex
_HwPimInterfaceIfIndex_Object = MibTableColumn
hwPimInterfaceIfIndex = _HwPimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 1),
    _HwPimInterfaceIfIndex_Type()
)
hwPimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimInterfaceIfIndex.setStatus("current")
_HwPimInterfaceIpVersion_Type = InetVersion
_HwPimInterfaceIpVersion_Object = MibTableColumn
hwPimInterfaceIpVersion = _HwPimInterfaceIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 2),
    _HwPimInterfaceIpVersion_Type()
)
hwPimInterfaceIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimInterfaceIpVersion.setStatus("current")
_HwPimInterfaceAddressType_Type = InetAddressType
_HwPimInterfaceAddressType_Object = MibTableColumn
hwPimInterfaceAddressType = _HwPimInterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 3),
    _HwPimInterfaceAddressType_Type()
)
hwPimInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceAddressType.setStatus("current")


class _HwPimInterfaceAddress_Type(InetAddress):
    """Custom type hwPimInterfaceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInterfaceAddress_Type.__name__ = "InetAddress"
_HwPimInterfaceAddress_Object = MibTableColumn
hwPimInterfaceAddress = _HwPimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 4),
    _HwPimInterfaceAddress_Type()
)
hwPimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceAddress.setStatus("current")
_HwPimInterfaceGenerationIdValue_Type = Unsigned32
_HwPimInterfaceGenerationIdValue_Object = MibTableColumn
hwPimInterfaceGenerationIdValue = _HwPimInterfaceGenerationIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 5),
    _HwPimInterfaceGenerationIdValue_Type()
)
hwPimInterfaceGenerationIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceGenerationIdValue.setStatus("current")


class _HwPimInterfaceDr_Type(InetAddress):
    """Custom type hwPimInterfaceDr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInterfaceDr_Type.__name__ = "InetAddress"
_HwPimInterfaceDr_Object = MibTableColumn
hwPimInterfaceDr = _HwPimInterfaceDr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 6),
    _HwPimInterfaceDr_Type()
)
hwPimInterfaceDr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceDr.setStatus("current")


class _HwPimInterfaceDrPriority_Type(Unsigned32):
    """Custom type hwPimInterfaceDrPriority based on Unsigned32"""
    defaultValue = 1


_HwPimInterfaceDrPriority_Object = MibTableColumn
hwPimInterfaceDrPriority = _HwPimInterfaceDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 7),
    _HwPimInterfaceDrPriority_Type()
)
hwPimInterfaceDrPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceDrPriority.setStatus("current")
_HwPimInterfaceDrPriorityEnabled_Type = TruthValue
_HwPimInterfaceDrPriorityEnabled_Object = MibTableColumn
hwPimInterfaceDrPriorityEnabled = _HwPimInterfaceDrPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 8),
    _HwPimInterfaceDrPriorityEnabled_Type()
)
hwPimInterfaceDrPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceDrPriorityEnabled.setStatus("current")


class _HwPimInterfaceHelloInterval_Type(Unsigned32):
    """Custom type hwPimInterfaceHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_HwPimInterfaceHelloInterval_Type.__name__ = "Unsigned32"
_HwPimInterfaceHelloInterval_Object = MibTableColumn
hwPimInterfaceHelloInterval = _HwPimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 9),
    _HwPimInterfaceHelloInterval_Type()
)
hwPimInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceHelloInterval.setUnits("seconds")


class _HwPimInterfaceTrigHelloInterval_Type(Unsigned32):
    """Custom type hwPimInterfaceTrigHelloInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwPimInterfaceTrigHelloInterval_Type.__name__ = "Unsigned32"
_HwPimInterfaceTrigHelloInterval_Object = MibTableColumn
hwPimInterfaceTrigHelloInterval = _HwPimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 10),
    _HwPimInterfaceTrigHelloInterval_Type()
)
hwPimInterfaceTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceTrigHelloInterval.setUnits("seconds")


class _HwPimInterfaceHelloHoldtime_Type(Unsigned32):
    """Custom type hwPimInterfaceHelloHoldtime based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceHelloHoldtime_Type.__name__ = "Unsigned32"
_HwPimInterfaceHelloHoldtime_Object = MibTableColumn
hwPimInterfaceHelloHoldtime = _HwPimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 11),
    _HwPimInterfaceHelloHoldtime_Type()
)
hwPimInterfaceHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceHelloHoldtime.setUnits("seconds")


class _HwPimInterfaceJoinPruneInterval_Type(Unsigned32):
    """Custom type hwPimInterfaceJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_HwPimInterfaceJoinPruneInterval_Type.__name__ = "Unsigned32"
_HwPimInterfaceJoinPruneInterval_Object = MibTableColumn
hwPimInterfaceJoinPruneInterval = _HwPimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 12),
    _HwPimInterfaceJoinPruneInterval_Type()
)
hwPimInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceJoinPruneInterval.setUnits("seconds")


class _HwPimInterfaceJoinPruneHoldtime_Type(Unsigned32):
    """Custom type hwPimInterfaceJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceJoinPruneHoldtime_Type.__name__ = "Unsigned32"
_HwPimInterfaceJoinPruneHoldtime_Object = MibTableColumn
hwPimInterfaceJoinPruneHoldtime = _HwPimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 13),
    _HwPimInterfaceJoinPruneHoldtime_Type()
)
hwPimInterfaceJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _HwPimInterfaceDfElectionRobustness_Type(Unsigned32):
    """Custom type hwPimInterfaceDfElectionRobustness based on Unsigned32"""
    defaultValue = 3


_HwPimInterfaceDfElectionRobustness_Object = MibTableColumn
hwPimInterfaceDfElectionRobustness = _HwPimInterfaceDfElectionRobustness_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 14),
    _HwPimInterfaceDfElectionRobustness_Type()
)
hwPimInterfaceDfElectionRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceDfElectionRobustness.setStatus("current")
_HwPimInterfaceLanDelayEnabled_Type = TruthValue
_HwPimInterfaceLanDelayEnabled_Object = MibTableColumn
hwPimInterfaceLanDelayEnabled = _HwPimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 15),
    _HwPimInterfaceLanDelayEnabled_Type()
)
hwPimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceLanDelayEnabled.setStatus("current")


class _HwPimInterfacePropagationDelay_Type(Unsigned32):
    """Custom type hwPimInterfacePropagationDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwPimInterfacePropagationDelay_Type.__name__ = "Unsigned32"
_HwPimInterfacePropagationDelay_Object = MibTableColumn
hwPimInterfacePropagationDelay = _HwPimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 16),
    _HwPimInterfacePropagationDelay_Type()
)
hwPimInterfacePropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfacePropagationDelay.setUnits("milliseconds")


class _HwPimInterfaceOverrideInterval_Type(Unsigned32):
    """Custom type hwPimInterfaceOverrideInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceOverrideInterval_Type.__name__ = "Unsigned32"
_HwPimInterfaceOverrideInterval_Object = MibTableColumn
hwPimInterfaceOverrideInterval = _HwPimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 17),
    _HwPimInterfaceOverrideInterval_Type()
)
hwPimInterfaceOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceOverrideInterval.setUnits("milliseconds")


class _HwPimInterfaceEffectPropagDelay_Type(Unsigned32):
    """Custom type hwPimInterfaceEffectPropagDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwPimInterfaceEffectPropagDelay_Type.__name__ = "Unsigned32"
_HwPimInterfaceEffectPropagDelay_Object = MibTableColumn
hwPimInterfaceEffectPropagDelay = _HwPimInterfaceEffectPropagDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 18),
    _HwPimInterfaceEffectPropagDelay_Type()
)
hwPimInterfaceEffectPropagDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceEffectPropagDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceEffectPropagDelay.setUnits("milliseconds")


class _HwPimInterfaceEffectOverrideIvl_Type(Unsigned32):
    """Custom type hwPimInterfaceEffectOverrideIvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceEffectOverrideIvl_Type.__name__ = "Unsigned32"
_HwPimInterfaceEffectOverrideIvl_Object = MibTableColumn
hwPimInterfaceEffectOverrideIvl = _HwPimInterfaceEffectOverrideIvl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 19),
    _HwPimInterfaceEffectOverrideIvl_Type()
)
hwPimInterfaceEffectOverrideIvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceEffectOverrideIvl.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceEffectOverrideIvl.setUnits("milliseconds")
_HwPimInterfaceSuppressionEnabled_Type = TruthValue
_HwPimInterfaceSuppressionEnabled_Object = MibTableColumn
hwPimInterfaceSuppressionEnabled = _HwPimInterfaceSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 20),
    _HwPimInterfaceSuppressionEnabled_Type()
)
hwPimInterfaceSuppressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceSuppressionEnabled.setStatus("current")
_HwPimInterfaceBidirCapable_Type = TruthValue
_HwPimInterfaceBidirCapable_Object = MibTableColumn
hwPimInterfaceBidirCapable = _HwPimInterfaceBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 21),
    _HwPimInterfaceBidirCapable_Type()
)
hwPimInterfaceBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceBidirCapable.setStatus("current")


class _HwPimInterfaceDomainBorder_Type(TruthValue):
    """Custom type hwPimInterfaceDomainBorder based on TruthValue"""


_HwPimInterfaceDomainBorder_Object = MibTableColumn
hwPimInterfaceDomainBorder = _HwPimInterfaceDomainBorder_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 22),
    _HwPimInterfaceDomainBorder_Type()
)
hwPimInterfaceDomainBorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceDomainBorder.setStatus("current")


class _HwPimInterfaceStubInterface_Type(TruthValue):
    """Custom type hwPimInterfaceStubInterface based on TruthValue"""


_HwPimInterfaceStubInterface_Object = MibTableColumn
hwPimInterfaceStubInterface = _HwPimInterfaceStubInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 23),
    _HwPimInterfaceStubInterface_Type()
)
hwPimInterfaceStubInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceStubInterface.setStatus("current")


class _HwPimInterfacePruneLimitInterval_Type(Unsigned32):
    """Custom type hwPimInterfacePruneLimitInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfacePruneLimitInterval_Type.__name__ = "Unsigned32"
_HwPimInterfacePruneLimitInterval_Object = MibTableColumn
hwPimInterfacePruneLimitInterval = _HwPimInterfacePruneLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 24),
    _HwPimInterfacePruneLimitInterval_Type()
)
hwPimInterfacePruneLimitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfacePruneLimitInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfacePruneLimitInterval.setUnits("seconds")


class _HwPimInterfaceGraftRetryInterval_Type(Unsigned32):
    """Custom type hwPimInterfaceGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceGraftRetryInterval_Type.__name__ = "Unsigned32"
_HwPimInterfaceGraftRetryInterval_Object = MibTableColumn
hwPimInterfaceGraftRetryInterval = _HwPimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 25),
    _HwPimInterfaceGraftRetryInterval_Type()
)
hwPimInterfaceGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceGraftRetryInterval.setUnits("seconds")
_HwPimInterfaceSrPriorityEnabled_Type = TruthValue
_HwPimInterfaceSrPriorityEnabled_Object = MibTableColumn
hwPimInterfaceSrPriorityEnabled = _HwPimInterfaceSrPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 26),
    _HwPimInterfaceSrPriorityEnabled_Type()
)
hwPimInterfaceSrPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceSrPriorityEnabled.setStatus("current")
_HwPimInterfaceStatus_Type = RowStatus
_HwPimInterfaceStatus_Object = MibTableColumn
hwPimInterfaceStatus = _HwPimInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 27),
    _HwPimInterfaceStatus_Type()
)
hwPimInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceStatus.setStatus("current")


class _HwPimInterfaceStorageType_Type(StorageType):
    """Custom type hwPimInterfaceStorageType based on StorageType"""


_HwPimInterfaceStorageType_Object = MibTableColumn
hwPimInterfaceStorageType = _HwPimInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 28),
    _HwPimInterfaceStorageType_Type()
)
hwPimInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPimInterfaceStorageType.setStatus("current")


class _HwPimInterfaceName_Type(DisplayString):
    """Custom type hwPimInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPimInterfaceName_Type.__name__ = "DisplayString"
_HwPimInterfaceName_Object = MibTableColumn
hwPimInterfaceName = _HwPimInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 1, 1, 29),
    _HwPimInterfaceName_Type()
)
hwPimInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimInterfaceName.setStatus("current")
_HwPimNeighborTable_Object = MibTable
hwPimNeighborTable = _HwPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hwPimNeighborTable.setStatus("current")
_HwPimNeighborEntry_Object = MibTableRow
hwPimNeighborEntry = _HwPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1)
)
hwPimNeighborEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNeighborIfIndex"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNeighborAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    hwPimNeighborEntry.setStatus("current")
_HwPimNeighborIfIndex_Type = InterfaceIndex
_HwPimNeighborIfIndex_Object = MibTableColumn
hwPimNeighborIfIndex = _HwPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 1),
    _HwPimNeighborIfIndex_Type()
)
hwPimNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNeighborIfIndex.setStatus("current")
_HwPimNeighborAddressType_Type = InetAddressType
_HwPimNeighborAddressType_Object = MibTableColumn
hwPimNeighborAddressType = _HwPimNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 2),
    _HwPimNeighborAddressType_Type()
)
hwPimNeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNeighborAddressType.setStatus("current")


class _HwPimNeighborAddress_Type(InetAddress):
    """Custom type hwPimNeighborAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimNeighborAddress_Type.__name__ = "InetAddress"
_HwPimNeighborAddress_Object = MibTableColumn
hwPimNeighborAddress = _HwPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 3),
    _HwPimNeighborAddress_Type()
)
hwPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNeighborAddress.setStatus("current")
_HwPimNeighborGenerationIdPresent_Type = TruthValue
_HwPimNeighborGenerationIdPresent_Object = MibTableColumn
hwPimNeighborGenerationIdPresent = _HwPimNeighborGenerationIdPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 4),
    _HwPimNeighborGenerationIdPresent_Type()
)
hwPimNeighborGenerationIdPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborGenerationIdPresent.setStatus("current")
_HwPimNeighborGenerationIdValue_Type = Unsigned32
_HwPimNeighborGenerationIdValue_Object = MibTableColumn
hwPimNeighborGenerationIdValue = _HwPimNeighborGenerationIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 5),
    _HwPimNeighborGenerationIdValue_Type()
)
hwPimNeighborGenerationIdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborGenerationIdValue.setStatus("current")
_HwPimNeighborUpTime_Type = TimeTicks
_HwPimNeighborUpTime_Object = MibTableColumn
hwPimNeighborUpTime = _HwPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 6),
    _HwPimNeighborUpTime_Type()
)
hwPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborUpTime.setStatus("current")
_HwPimNeighborExpiryTime_Type = TimeTicks
_HwPimNeighborExpiryTime_Object = MibTableColumn
hwPimNeighborExpiryTime = _HwPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 7),
    _HwPimNeighborExpiryTime_Type()
)
hwPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborExpiryTime.setStatus("current")
_HwPimNeighborDrPriorityPresent_Type = TruthValue
_HwPimNeighborDrPriorityPresent_Object = MibTableColumn
hwPimNeighborDrPriorityPresent = _HwPimNeighborDrPriorityPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 8),
    _HwPimNeighborDrPriorityPresent_Type()
)
hwPimNeighborDrPriorityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborDrPriorityPresent.setStatus("current")
_HwPimNeighborDrPriority_Type = Unsigned32
_HwPimNeighborDrPriority_Object = MibTableColumn
hwPimNeighborDrPriority = _HwPimNeighborDrPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 9),
    _HwPimNeighborDrPriority_Type()
)
hwPimNeighborDrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborDrPriority.setStatus("current")
_HwPimNeighborLanPruneDelayPresent_Type = TruthValue
_HwPimNeighborLanPruneDelayPresent_Object = MibTableColumn
hwPimNeighborLanPruneDelayPresent = _HwPimNeighborLanPruneDelayPresent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 10),
    _HwPimNeighborLanPruneDelayPresent_Type()
)
hwPimNeighborLanPruneDelayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborLanPruneDelayPresent.setStatus("current")
_HwPimNeighborTBit_Type = TruthValue
_HwPimNeighborTBit_Object = MibTableColumn
hwPimNeighborTBit = _HwPimNeighborTBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 11),
    _HwPimNeighborTBit_Type()
)
hwPimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborTBit.setStatus("current")


class _HwPimNeighborPropagationDelay_Type(Unsigned32):
    """Custom type hwPimNeighborPropagationDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwPimNeighborPropagationDelay_Type.__name__ = "Unsigned32"
_HwPimNeighborPropagationDelay_Object = MibTableColumn
hwPimNeighborPropagationDelay = _HwPimNeighborPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 12),
    _HwPimNeighborPropagationDelay_Type()
)
hwPimNeighborPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborPropagationDelay.setStatus("current")


class _HwPimNeighborOverrideInterval_Type(Unsigned32):
    """Custom type hwPimNeighborOverrideInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimNeighborOverrideInterval_Type.__name__ = "Unsigned32"
_HwPimNeighborOverrideInterval_Object = MibTableColumn
hwPimNeighborOverrideInterval = _HwPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 13),
    _HwPimNeighborOverrideInterval_Type()
)
hwPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborOverrideInterval.setStatus("current")
_HwPimNeighborBidirCapable_Type = TruthValue
_HwPimNeighborBidirCapable_Object = MibTableColumn
hwPimNeighborBidirCapable = _HwPimNeighborBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 14),
    _HwPimNeighborBidirCapable_Type()
)
hwPimNeighborBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborBidirCapable.setStatus("current")
_HwPimNeighborSrCapable_Type = TruthValue
_HwPimNeighborSrCapable_Object = MibTableColumn
hwPimNeighborSrCapable = _HwPimNeighborSrCapable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 15),
    _HwPimNeighborSrCapable_Type()
)
hwPimNeighborSrCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborSrCapable.setStatus("current")


class _HwPimNeighborIfName_Type(DisplayString):
    """Custom type hwPimNeighborIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwPimNeighborIfName_Type.__name__ = "DisplayString"
_HwPimNeighborIfName_Object = MibTableColumn
hwPimNeighborIfName = _HwPimNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 2, 1, 16),
    _HwPimNeighborIfName_Type()
)
hwPimNeighborIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimNeighborIfName.setStatus("current")
_HwPimNbrSecAddressTable_Object = MibTable
hwPimNbrSecAddressTable = _HwPimNbrSecAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hwPimNbrSecAddressTable.setStatus("current")
_HwPimNbrSecAddressEntry_Object = MibTableRow
hwPimNbrSecAddressEntry = _HwPimNbrSecAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3, 1)
)
hwPimNbrSecAddressEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNbrSecAddressIfIndex"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNbrSecAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNbrSecAddressPrimary"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimNbrSecAddress"),
)
if mibBuilder.loadTexts:
    hwPimNbrSecAddressEntry.setStatus("current")
_HwPimNbrSecAddressIfIndex_Type = InterfaceIndex
_HwPimNbrSecAddressIfIndex_Object = MibTableColumn
hwPimNbrSecAddressIfIndex = _HwPimNbrSecAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3, 1, 1),
    _HwPimNbrSecAddressIfIndex_Type()
)
hwPimNbrSecAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNbrSecAddressIfIndex.setStatus("current")
_HwPimNbrSecAddressType_Type = InetAddressType
_HwPimNbrSecAddressType_Object = MibTableColumn
hwPimNbrSecAddressType = _HwPimNbrSecAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3, 1, 2),
    _HwPimNbrSecAddressType_Type()
)
hwPimNbrSecAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNbrSecAddressType.setStatus("current")


class _HwPimNbrSecAddressPrimary_Type(InetAddress):
    """Custom type hwPimNbrSecAddressPrimary based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimNbrSecAddressPrimary_Type.__name__ = "InetAddress"
_HwPimNbrSecAddressPrimary_Object = MibTableColumn
hwPimNbrSecAddressPrimary = _HwPimNbrSecAddressPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3, 1, 3),
    _HwPimNbrSecAddressPrimary_Type()
)
hwPimNbrSecAddressPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimNbrSecAddressPrimary.setStatus("current")


class _HwPimNbrSecAddress_Type(InetAddress):
    """Custom type hwPimNbrSecAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimNbrSecAddress_Type.__name__ = "InetAddress"
_HwPimNbrSecAddress_Object = MibTableColumn
hwPimNbrSecAddress = _HwPimNbrSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 3, 1, 4),
    _HwPimNbrSecAddress_Type()
)
hwPimNbrSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNbrSecAddress.setStatus("current")
_HwPimStarGTable_Object = MibTable
hwPimStarGTable = _HwPimStarGTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4)
)
if mibBuilder.loadTexts:
    hwPimStarGTable.setStatus("current")
_HwPimStarGEntry_Object = MibTableRow
hwPimStarGEntry = _HwPimStarGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1)
)
hwPimStarGEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGGrpAddress"),
)
if mibBuilder.loadTexts:
    hwPimStarGEntry.setStatus("current")
_HwPimStarGAddressType_Type = InetAddressType
_HwPimStarGAddressType_Object = MibTableColumn
hwPimStarGAddressType = _HwPimStarGAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 1),
    _HwPimStarGAddressType_Type()
)
hwPimStarGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimStarGAddressType.setStatus("current")


class _HwPimStarGGrpAddress_Type(InetAddress):
    """Custom type hwPimStarGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGGrpAddress_Type.__name__ = "InetAddress"
_HwPimStarGGrpAddress_Object = MibTableColumn
hwPimStarGGrpAddress = _HwPimStarGGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 2),
    _HwPimStarGGrpAddress_Type()
)
hwPimStarGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimStarGGrpAddress.setStatus("current")
_HwPimStarGUpTime_Type = TimeTicks
_HwPimStarGUpTime_Object = MibTableColumn
hwPimStarGUpTime = _HwPimStarGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 3),
    _HwPimStarGUpTime_Type()
)
hwPimStarGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGUpTime.setStatus("current")


class _HwPimStarGPimMode_Type(HWPimMode):
    """Custom type hwPimStarGPimMode based on HWPimMode"""
    subtypeSpec = HWPimMode.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asm", 3),
          ("bidir", 4))
    )


_HwPimStarGPimMode_Type.__name__ = "HWPimMode"
_HwPimStarGPimMode_Object = MibTableColumn
hwPimStarGPimMode = _HwPimStarGPimMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 4),
    _HwPimStarGPimMode_Type()
)
hwPimStarGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGPimMode.setStatus("current")
_HwPimStarGRpAddressType_Type = InetAddressType
_HwPimStarGRpAddressType_Object = MibTableColumn
hwPimStarGRpAddressType = _HwPimStarGRpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 5),
    _HwPimStarGRpAddressType_Type()
)
hwPimStarGRpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpAddressType.setStatus("current")


class _HwPimStarGRpAddress_Type(InetAddress):
    """Custom type hwPimStarGRpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGRpAddress_Type.__name__ = "InetAddress"
_HwPimStarGRpAddress_Object = MibTableColumn
hwPimStarGRpAddress = _HwPimStarGRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 6),
    _HwPimStarGRpAddress_Type()
)
hwPimStarGRpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpAddress.setStatus("current")
_HwPimStarGPimModeOrigin_Type = HWPimGroupMappingOriginType
_HwPimStarGPimModeOrigin_Object = MibTableColumn
hwPimStarGPimModeOrigin = _HwPimStarGPimModeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 7),
    _HwPimStarGPimModeOrigin_Type()
)
hwPimStarGPimModeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGPimModeOrigin.setStatus("current")
_HwPimStarGRpIsLocal_Type = TruthValue
_HwPimStarGRpIsLocal_Object = MibTableColumn
hwPimStarGRpIsLocal = _HwPimStarGRpIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 8),
    _HwPimStarGRpIsLocal_Type()
)
hwPimStarGRpIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpIsLocal.setStatus("current")


class _HwPimStarGUpstreamJoinState_Type(Integer32):
    """Custom type hwPimStarGUpstreamJoinState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 2),
          ("notJoined", 1))
    )


_HwPimStarGUpstreamJoinState_Type.__name__ = "Integer32"
_HwPimStarGUpstreamJoinState_Object = MibTableColumn
hwPimStarGUpstreamJoinState = _HwPimStarGUpstreamJoinState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 9),
    _HwPimStarGUpstreamJoinState_Type()
)
hwPimStarGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGUpstreamJoinState.setStatus("current")
_HwPimStarGUpstreamJoinTimer_Type = TimeTicks
_HwPimStarGUpstreamJoinTimer_Object = MibTableColumn
hwPimStarGUpstreamJoinTimer = _HwPimStarGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 10),
    _HwPimStarGUpstreamJoinTimer_Type()
)
hwPimStarGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGUpstreamJoinTimer.setStatus("current")
_HwPimStarGUpstreamNeighborType_Type = InetAddressType
_HwPimStarGUpstreamNeighborType_Object = MibTableColumn
hwPimStarGUpstreamNeighborType = _HwPimStarGUpstreamNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 11),
    _HwPimStarGUpstreamNeighborType_Type()
)
hwPimStarGUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGUpstreamNeighborType.setStatus("current")


class _HwPimStarGUpstreamNeighbor_Type(InetAddress):
    """Custom type hwPimStarGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGUpstreamNeighbor_Type.__name__ = "InetAddress"
_HwPimStarGUpstreamNeighbor_Object = MibTableColumn
hwPimStarGUpstreamNeighbor = _HwPimStarGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 12),
    _HwPimStarGUpstreamNeighbor_Type()
)
hwPimStarGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGUpstreamNeighbor.setStatus("current")
_HwPimStarGRpfIfIndex_Type = InterfaceIndexOrZero
_HwPimStarGRpfIfIndex_Object = MibTableColumn
hwPimStarGRpfIfIndex = _HwPimStarGRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 13),
    _HwPimStarGRpfIfIndex_Type()
)
hwPimStarGRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfIfIndex.setStatus("current")
_HwPimStarGRpfNextHopType_Type = InetAddressType
_HwPimStarGRpfNextHopType_Object = MibTableColumn
hwPimStarGRpfNextHopType = _HwPimStarGRpfNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 14),
    _HwPimStarGRpfNextHopType_Type()
)
hwPimStarGRpfNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfNextHopType.setStatus("current")


class _HwPimStarGRpfNextHop_Type(InetAddress):
    """Custom type hwPimStarGRpfNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGRpfNextHop_Type.__name__ = "InetAddress"
_HwPimStarGRpfNextHop_Object = MibTableColumn
hwPimStarGRpfNextHop = _HwPimStarGRpfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 15),
    _HwPimStarGRpfNextHop_Type()
)
hwPimStarGRpfNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfNextHop.setStatus("current")
_HwPimStarGRpfRouteProtocol_Type = IANAipRouteProtocol
_HwPimStarGRpfRouteProtocol_Object = MibTableColumn
hwPimStarGRpfRouteProtocol = _HwPimStarGRpfRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 16),
    _HwPimStarGRpfRouteProtocol_Type()
)
hwPimStarGRpfRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfRouteProtocol.setStatus("current")


class _HwPimStarGRpfRouteAddress_Type(InetAddress):
    """Custom type hwPimStarGRpfRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGRpfRouteAddress_Type.__name__ = "InetAddress"
_HwPimStarGRpfRouteAddress_Object = MibTableColumn
hwPimStarGRpfRouteAddress = _HwPimStarGRpfRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 17),
    _HwPimStarGRpfRouteAddress_Type()
)
hwPimStarGRpfRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfRouteAddress.setStatus("current")
_HwPimStarGRpfRoutePrefixLength_Type = InetAddressPrefixLength
_HwPimStarGRpfRoutePrefixLength_Object = MibTableColumn
hwPimStarGRpfRoutePrefixLength = _HwPimStarGRpfRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 18),
    _HwPimStarGRpfRoutePrefixLength_Type()
)
hwPimStarGRpfRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfRoutePrefixLength.setStatus("current")


class _HwPimStarGRpfRouteMetricPref_Type(Unsigned32):
    """Custom type hwPimStarGRpfRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPimStarGRpfRouteMetricPref_Type.__name__ = "Unsigned32"
_HwPimStarGRpfRouteMetricPref_Object = MibTableColumn
hwPimStarGRpfRouteMetricPref = _HwPimStarGRpfRouteMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 19),
    _HwPimStarGRpfRouteMetricPref_Type()
)
hwPimStarGRpfRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfRouteMetricPref.setStatus("current")
_HwPimStarGRpfRouteMetric_Type = Unsigned32
_HwPimStarGRpfRouteMetric_Object = MibTableColumn
hwPimStarGRpfRouteMetric = _HwPimStarGRpfRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 4, 1, 20),
    _HwPimStarGRpfRouteMetric_Type()
)
hwPimStarGRpfRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGRpfRouteMetric.setStatus("current")
_HwPimStarGITable_Object = MibTable
hwPimStarGITable = _HwPimStarGITable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5)
)
if mibBuilder.loadTexts:
    hwPimStarGITable.setStatus("current")
_HwPimStarGIEntry_Object = MibTableRow
hwPimStarGIEntry = _HwPimStarGIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1)
)
hwPimStarGIEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGIIfIndex"),
)
if mibBuilder.loadTexts:
    hwPimStarGIEntry.setStatus("current")
_HwPimStarGIIfIndex_Type = InterfaceIndex
_HwPimStarGIIfIndex_Object = MibTableColumn
hwPimStarGIIfIndex = _HwPimStarGIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 1),
    _HwPimStarGIIfIndex_Type()
)
hwPimStarGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimStarGIIfIndex.setStatus("current")
_HwPimStarGIUpTime_Type = TimeTicks
_HwPimStarGIUpTime_Object = MibTableColumn
hwPimStarGIUpTime = _HwPimStarGIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 2),
    _HwPimStarGIUpTime_Type()
)
hwPimStarGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIUpTime.setStatus("current")
_HwPimStarGILocalMembership_Type = TruthValue
_HwPimStarGILocalMembership_Object = MibTableColumn
hwPimStarGILocalMembership = _HwPimStarGILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 3),
    _HwPimStarGILocalMembership_Type()
)
hwPimStarGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGILocalMembership.setStatus("current")


class _HwPimStarGIJoinPruneState_Type(Integer32):
    """Custom type hwPimStarGIJoinPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("join", 2),
          ("noInfo", 1),
          ("prunePending", 3))
    )


_HwPimStarGIJoinPruneState_Type.__name__ = "Integer32"
_HwPimStarGIJoinPruneState_Object = MibTableColumn
hwPimStarGIJoinPruneState = _HwPimStarGIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 4),
    _HwPimStarGIJoinPruneState_Type()
)
hwPimStarGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIJoinPruneState.setStatus("current")
_HwPimStarGIPrunePendingTimer_Type = TimeTicks
_HwPimStarGIPrunePendingTimer_Object = MibTableColumn
hwPimStarGIPrunePendingTimer = _HwPimStarGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 5),
    _HwPimStarGIPrunePendingTimer_Type()
)
hwPimStarGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIPrunePendingTimer.setStatus("current")
_HwPimStarGIJoinExpiryTimer_Type = TimeTicks
_HwPimStarGIJoinExpiryTimer_Object = MibTableColumn
hwPimStarGIJoinExpiryTimer = _HwPimStarGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 6),
    _HwPimStarGIJoinExpiryTimer_Type()
)
hwPimStarGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIJoinExpiryTimer.setStatus("current")


class _HwPimStarGIAssertState_Type(Integer32):
    """Custom type hwPimStarGIAssertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iAmAssertLoser", 3),
          ("iAmAssertWinner", 2),
          ("noInfo", 1))
    )


_HwPimStarGIAssertState_Type.__name__ = "Integer32"
_HwPimStarGIAssertState_Object = MibTableColumn
hwPimStarGIAssertState = _HwPimStarGIAssertState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 7),
    _HwPimStarGIAssertState_Type()
)
hwPimStarGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertState.setStatus("current")
_HwPimStarGIAssertTimer_Type = TimeTicks
_HwPimStarGIAssertTimer_Object = MibTableColumn
hwPimStarGIAssertTimer = _HwPimStarGIAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 8),
    _HwPimStarGIAssertTimer_Type()
)
hwPimStarGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertTimer.setStatus("current")
_HwPimStarGIAssertWinnerAddressType_Type = InetAddressType
_HwPimStarGIAssertWinnerAddressType_Object = MibTableColumn
hwPimStarGIAssertWinnerAddressType = _HwPimStarGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 9),
    _HwPimStarGIAssertWinnerAddressType_Type()
)
hwPimStarGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertWinnerAddressType.setStatus("current")


class _HwPimStarGIAssertWinnerAddress_Type(InetAddress):
    """Custom type hwPimStarGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimStarGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_HwPimStarGIAssertWinnerAddress_Object = MibTableColumn
hwPimStarGIAssertWinnerAddress = _HwPimStarGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 10),
    _HwPimStarGIAssertWinnerAddress_Type()
)
hwPimStarGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertWinnerAddress.setStatus("current")


class _HwPimStarGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type hwPimStarGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPimStarGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_HwPimStarGIAssertWinnerMetricPref_Object = MibTableColumn
hwPimStarGIAssertWinnerMetricPref = _HwPimStarGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 11),
    _HwPimStarGIAssertWinnerMetricPref_Type()
)
hwPimStarGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertWinnerMetricPref.setStatus("current")
_HwPimStarGIAssertWinnerMetric_Type = Unsigned32
_HwPimStarGIAssertWinnerMetric_Object = MibTableColumn
hwPimStarGIAssertWinnerMetric = _HwPimStarGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 5, 1, 12),
    _HwPimStarGIAssertWinnerMetric_Type()
)
hwPimStarGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIAssertWinnerMetric.setStatus("current")
_HwPimSGTable_Object = MibTable
hwPimSGTable = _HwPimSGTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6)
)
if mibBuilder.loadTexts:
    hwPimSGTable.setStatus("current")
_HwPimSGEntry_Object = MibTableRow
hwPimSGEntry = _HwPimSGEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1)
)
hwPimSGEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGSrcAddress"),
)
if mibBuilder.loadTexts:
    hwPimSGEntry.setStatus("current")
_HwPimSGAddressType_Type = InetAddressType
_HwPimSGAddressType_Object = MibTableColumn
hwPimSGAddressType = _HwPimSGAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 1),
    _HwPimSGAddressType_Type()
)
hwPimSGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGAddressType.setStatus("current")


class _HwPimSGGrpAddress_Type(InetAddress):
    """Custom type hwPimSGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGGrpAddress_Type.__name__ = "InetAddress"
_HwPimSGGrpAddress_Object = MibTableColumn
hwPimSGGrpAddress = _HwPimSGGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 2),
    _HwPimSGGrpAddress_Type()
)
hwPimSGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGGrpAddress.setStatus("current")


class _HwPimSGSrcAddress_Type(InetAddress):
    """Custom type hwPimSGSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGSrcAddress_Type.__name__ = "InetAddress"
_HwPimSGSrcAddress_Object = MibTableColumn
hwPimSGSrcAddress = _HwPimSGSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 3),
    _HwPimSGSrcAddress_Type()
)
hwPimSGSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGSrcAddress.setStatus("current")
_HwPimSGUpTime_Type = TimeTicks
_HwPimSGUpTime_Object = MibTableColumn
hwPimSGUpTime = _HwPimSGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 4),
    _HwPimSGUpTime_Type()
)
hwPimSGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpTime.setStatus("current")


class _HwPimSGPimMode_Type(HWPimMode):
    """Custom type hwPimSGPimMode based on HWPimMode"""
    subtypeSpec = HWPimMode.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asm", 3),
          ("ssm", 2))
    )


_HwPimSGPimMode_Type.__name__ = "HWPimMode"
_HwPimSGPimMode_Object = MibTableColumn
hwPimSGPimMode = _HwPimSGPimMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 5),
    _HwPimSGPimMode_Type()
)
hwPimSGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGPimMode.setStatus("current")


class _HwPimSGUpstreamJoinState_Type(Integer32):
    """Custom type hwPimSGUpstreamJoinState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 2),
          ("notJoined", 1))
    )


_HwPimSGUpstreamJoinState_Type.__name__ = "Integer32"
_HwPimSGUpstreamJoinState_Object = MibTableColumn
hwPimSGUpstreamJoinState = _HwPimSGUpstreamJoinState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 6),
    _HwPimSGUpstreamJoinState_Type()
)
hwPimSGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpstreamJoinState.setStatus("current")
_HwPimSGUpstreamJoinTimer_Type = TimeTicks
_HwPimSGUpstreamJoinTimer_Object = MibTableColumn
hwPimSGUpstreamJoinTimer = _HwPimSGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 7),
    _HwPimSGUpstreamJoinTimer_Type()
)
hwPimSGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpstreamJoinTimer.setStatus("current")


class _HwPimSGUpstreamNeighbor_Type(InetAddress):
    """Custom type hwPimSGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGUpstreamNeighbor_Type.__name__ = "InetAddress"
_HwPimSGUpstreamNeighbor_Object = MibTableColumn
hwPimSGUpstreamNeighbor = _HwPimSGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 8),
    _HwPimSGUpstreamNeighbor_Type()
)
hwPimSGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpstreamNeighbor.setStatus("current")
_HwPimSGRpfIfIndex_Type = InterfaceIndexOrZero
_HwPimSGRpfIfIndex_Object = MibTableColumn
hwPimSGRpfIfIndex = _HwPimSGRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 9),
    _HwPimSGRpfIfIndex_Type()
)
hwPimSGRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfIfIndex.setStatus("current")
_HwPimSGRpfNextHopType_Type = InetAddressType
_HwPimSGRpfNextHopType_Object = MibTableColumn
hwPimSGRpfNextHopType = _HwPimSGRpfNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 10),
    _HwPimSGRpfNextHopType_Type()
)
hwPimSGRpfNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfNextHopType.setStatus("current")


class _HwPimSGRpfNextHop_Type(InetAddress):
    """Custom type hwPimSGRpfNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGRpfNextHop_Type.__name__ = "InetAddress"
_HwPimSGRpfNextHop_Object = MibTableColumn
hwPimSGRpfNextHop = _HwPimSGRpfNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 11),
    _HwPimSGRpfNextHop_Type()
)
hwPimSGRpfNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfNextHop.setStatus("current")
_HwPimSGRpfRouteProtocol_Type = IANAipRouteProtocol
_HwPimSGRpfRouteProtocol_Object = MibTableColumn
hwPimSGRpfRouteProtocol = _HwPimSGRpfRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 12),
    _HwPimSGRpfRouteProtocol_Type()
)
hwPimSGRpfRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfRouteProtocol.setStatus("current")


class _HwPimSGRpfRouteAddress_Type(InetAddress):
    """Custom type hwPimSGRpfRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGRpfRouteAddress_Type.__name__ = "InetAddress"
_HwPimSGRpfRouteAddress_Object = MibTableColumn
hwPimSGRpfRouteAddress = _HwPimSGRpfRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 13),
    _HwPimSGRpfRouteAddress_Type()
)
hwPimSGRpfRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfRouteAddress.setStatus("current")
_HwPimSGRpfRoutePrefixLength_Type = InetAddressPrefixLength
_HwPimSGRpfRoutePrefixLength_Object = MibTableColumn
hwPimSGRpfRoutePrefixLength = _HwPimSGRpfRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 14),
    _HwPimSGRpfRoutePrefixLength_Type()
)
hwPimSGRpfRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfRoutePrefixLength.setStatus("current")


class _HwPimSGRpfRouteMetricPref_Type(Unsigned32):
    """Custom type hwPimSGRpfRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPimSGRpfRouteMetricPref_Type.__name__ = "Unsigned32"
_HwPimSGRpfRouteMetricPref_Object = MibTableColumn
hwPimSGRpfRouteMetricPref = _HwPimSGRpfRouteMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 15),
    _HwPimSGRpfRouteMetricPref_Type()
)
hwPimSGRpfRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfRouteMetricPref.setStatus("current")
_HwPimSGRpfRouteMetric_Type = Unsigned32
_HwPimSGRpfRouteMetric_Object = MibTableColumn
hwPimSGRpfRouteMetric = _HwPimSGRpfRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 16),
    _HwPimSGRpfRouteMetric_Type()
)
hwPimSGRpfRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpfRouteMetric.setStatus("current")
_HwPimSGSptBit_Type = TruthValue
_HwPimSGSptBit_Object = MibTableColumn
hwPimSGSptBit = _HwPimSGSptBit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 17),
    _HwPimSGSptBit_Type()
)
hwPimSGSptBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGSptBit.setStatus("current")
_HwPimSGKeepaliveTimer_Type = TimeTicks
_HwPimSGKeepaliveTimer_Object = MibTableColumn
hwPimSGKeepaliveTimer = _HwPimSGKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 18),
    _HwPimSGKeepaliveTimer_Type()
)
hwPimSGKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGKeepaliveTimer.setStatus("current")


class _HwPimSGDrRegisterState_Type(Integer32):
    """Custom type hwPimSGDrRegisterState based on Integer32"""
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
        *(("join", 2),
          ("joinPending", 3),
          ("noInfo", 1),
          ("prune", 4))
    )


_HwPimSGDrRegisterState_Type.__name__ = "Integer32"
_HwPimSGDrRegisterState_Object = MibTableColumn
hwPimSGDrRegisterState = _HwPimSGDrRegisterState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 19),
    _HwPimSGDrRegisterState_Type()
)
hwPimSGDrRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGDrRegisterState.setStatus("current")
_HwPimSGDrRegisterStopTimer_Type = TimeTicks
_HwPimSGDrRegisterStopTimer_Object = MibTableColumn
hwPimSGDrRegisterStopTimer = _HwPimSGDrRegisterStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 20),
    _HwPimSGDrRegisterStopTimer_Type()
)
hwPimSGDrRegisterStopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGDrRegisterStopTimer.setStatus("current")
_HwPimSGRpRegisterPmbrAddressType_Type = InetAddressType
_HwPimSGRpRegisterPmbrAddressType_Object = MibTableColumn
hwPimSGRpRegisterPmbrAddressType = _HwPimSGRpRegisterPmbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 21),
    _HwPimSGRpRegisterPmbrAddressType_Type()
)
hwPimSGRpRegisterPmbrAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpRegisterPmbrAddressType.setStatus("current")


class _HwPimSGRpRegisterPmbrAddress_Type(InetAddress):
    """Custom type hwPimSGRpRegisterPmbrAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGRpRegisterPmbrAddress_Type.__name__ = "InetAddress"
_HwPimSGRpRegisterPmbrAddress_Object = MibTableColumn
hwPimSGRpRegisterPmbrAddress = _HwPimSGRpRegisterPmbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 22),
    _HwPimSGRpRegisterPmbrAddress_Type()
)
hwPimSGRpRegisterPmbrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRpRegisterPmbrAddress.setStatus("current")


class _HwPimSGUpstreamPruneState_Type(Integer32):
    """Custom type hwPimSGUpstreamPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ackpending", 2),
          ("forwarding", 1),
          ("pruned", 3))
    )


_HwPimSGUpstreamPruneState_Type.__name__ = "Integer32"
_HwPimSGUpstreamPruneState_Object = MibTableColumn
hwPimSGUpstreamPruneState = _HwPimSGUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 23),
    _HwPimSGUpstreamPruneState_Type()
)
hwPimSGUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpstreamPruneState.setStatus("current")
_HwPimSGUpstreamPruneLimitTimer_Type = TimeTicks
_HwPimSGUpstreamPruneLimitTimer_Object = MibTableColumn
hwPimSGUpstreamPruneLimitTimer = _HwPimSGUpstreamPruneLimitTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 24),
    _HwPimSGUpstreamPruneLimitTimer_Type()
)
hwPimSGUpstreamPruneLimitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGUpstreamPruneLimitTimer.setStatus("current")


class _HwPimSGOriginatorState_Type(Integer32):
    """Custom type hwPimSGOriginatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOriginator", 1),
          ("originator", 2))
    )


_HwPimSGOriginatorState_Type.__name__ = "Integer32"
_HwPimSGOriginatorState_Object = MibTableColumn
hwPimSGOriginatorState = _HwPimSGOriginatorState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 25),
    _HwPimSGOriginatorState_Type()
)
hwPimSGOriginatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGOriginatorState.setStatus("current")
_HwPimSGSourceActiveTimer_Type = TimeTicks
_HwPimSGSourceActiveTimer_Object = MibTableColumn
hwPimSGSourceActiveTimer = _HwPimSGSourceActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 26),
    _HwPimSGSourceActiveTimer_Type()
)
hwPimSGSourceActiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGSourceActiveTimer.setStatus("current")
_HwPimSGStateRefreshTimer_Type = TimeTicks
_HwPimSGStateRefreshTimer_Object = MibTableColumn
hwPimSGStateRefreshTimer = _HwPimSGStateRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 6, 1, 27),
    _HwPimSGStateRefreshTimer_Type()
)
hwPimSGStateRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGStateRefreshTimer.setStatus("current")
_HwPimSGITable_Object = MibTable
hwPimSGITable = _HwPimSGITable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7)
)
if mibBuilder.loadTexts:
    hwPimSGITable.setStatus("current")
_HwPimSGIEntry_Object = MibTableRow
hwPimSGIEntry = _HwPimSGIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1)
)
hwPimSGIEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGSrcAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGIIfIndex"),
)
if mibBuilder.loadTexts:
    hwPimSGIEntry.setStatus("current")
_HwPimSGIIfIndex_Type = InterfaceIndex
_HwPimSGIIfIndex_Object = MibTableColumn
hwPimSGIIfIndex = _HwPimSGIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 1),
    _HwPimSGIIfIndex_Type()
)
hwPimSGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGIIfIndex.setStatus("current")
_HwPimSGIUpTime_Type = TimeTicks
_HwPimSGIUpTime_Object = MibTableColumn
hwPimSGIUpTime = _HwPimSGIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 2),
    _HwPimSGIUpTime_Type()
)
hwPimSGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIUpTime.setStatus("current")
_HwPimSGILocalMembership_Type = TruthValue
_HwPimSGILocalMembership_Object = MibTableColumn
hwPimSGILocalMembership = _HwPimSGILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 3),
    _HwPimSGILocalMembership_Type()
)
hwPimSGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGILocalMembership.setStatus("current")


class _HwPimSGIJoinPruneState_Type(Integer32):
    """Custom type hwPimSGIJoinPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("join", 2),
          ("noInfo", 1),
          ("prunePending", 3))
    )


_HwPimSGIJoinPruneState_Type.__name__ = "Integer32"
_HwPimSGIJoinPruneState_Object = MibTableColumn
hwPimSGIJoinPruneState = _HwPimSGIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 4),
    _HwPimSGIJoinPruneState_Type()
)
hwPimSGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIJoinPruneState.setStatus("current")
_HwPimSGIPrunePendingTimer_Type = TimeTicks
_HwPimSGIPrunePendingTimer_Object = MibTableColumn
hwPimSGIPrunePendingTimer = _HwPimSGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 5),
    _HwPimSGIPrunePendingTimer_Type()
)
hwPimSGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIPrunePendingTimer.setStatus("current")
_HwPimSGIJoinExpiryTimer_Type = TimeTicks
_HwPimSGIJoinExpiryTimer_Object = MibTableColumn
hwPimSGIJoinExpiryTimer = _HwPimSGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 6),
    _HwPimSGIJoinExpiryTimer_Type()
)
hwPimSGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIJoinExpiryTimer.setStatus("current")


class _HwPimSGIAssertState_Type(Integer32):
    """Custom type hwPimSGIAssertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iAmAssertLoser", 3),
          ("iAmAssertWinner", 2),
          ("noInfo", 1))
    )


_HwPimSGIAssertState_Type.__name__ = "Integer32"
_HwPimSGIAssertState_Object = MibTableColumn
hwPimSGIAssertState = _HwPimSGIAssertState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 7),
    _HwPimSGIAssertState_Type()
)
hwPimSGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertState.setStatus("current")
_HwPimSGIAssertTimer_Type = TimeTicks
_HwPimSGIAssertTimer_Object = MibTableColumn
hwPimSGIAssertTimer = _HwPimSGIAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 8),
    _HwPimSGIAssertTimer_Type()
)
hwPimSGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertTimer.setStatus("current")
_HwPimSGIAssertWinnerAddressType_Type = InetAddressType
_HwPimSGIAssertWinnerAddressType_Object = MibTableColumn
hwPimSGIAssertWinnerAddressType = _HwPimSGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 9),
    _HwPimSGIAssertWinnerAddressType_Type()
)
hwPimSGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertWinnerAddressType.setStatus("current")


class _HwPimSGIAssertWinnerAddress_Type(InetAddress):
    """Custom type hwPimSGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_HwPimSGIAssertWinnerAddress_Object = MibTableColumn
hwPimSGIAssertWinnerAddress = _HwPimSGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 10),
    _HwPimSGIAssertWinnerAddress_Type()
)
hwPimSGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertWinnerAddress.setStatus("current")


class _HwPimSGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type hwPimSGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwPimSGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_HwPimSGIAssertWinnerMetricPref_Object = MibTableColumn
hwPimSGIAssertWinnerMetricPref = _HwPimSGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 11),
    _HwPimSGIAssertWinnerMetricPref_Type()
)
hwPimSGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertWinnerMetricPref.setStatus("current")
_HwPimSGIAssertWinnerMetric_Type = Unsigned32
_HwPimSGIAssertWinnerMetric_Object = MibTableColumn
hwPimSGIAssertWinnerMetric = _HwPimSGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 7, 1, 12),
    _HwPimSGIAssertWinnerMetric_Type()
)
hwPimSGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIAssertWinnerMetric.setStatus("current")
_HwPimSGRptTable_Object = MibTable
hwPimSGRptTable = _HwPimSGRptTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8)
)
if mibBuilder.loadTexts:
    hwPimSGRptTable.setStatus("current")
_HwPimSGRptEntry_Object = MibTableRow
hwPimSGRptEntry = _HwPimSGRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8, 1)
)
hwPimSGRptEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGRptSrcAddress"),
)
if mibBuilder.loadTexts:
    hwPimSGRptEntry.setStatus("current")


class _HwPimSGRptSrcAddress_Type(InetAddress):
    """Custom type hwPimSGRptSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimSGRptSrcAddress_Type.__name__ = "InetAddress"
_HwPimSGRptSrcAddress_Object = MibTableColumn
hwPimSGRptSrcAddress = _HwPimSGRptSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8, 1, 1),
    _HwPimSGRptSrcAddress_Type()
)
hwPimSGRptSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGRptSrcAddress.setStatus("current")
_HwPimSGRptUpTime_Type = TimeTicks
_HwPimSGRptUpTime_Object = MibTableColumn
hwPimSGRptUpTime = _HwPimSGRptUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8, 1, 2),
    _HwPimSGRptUpTime_Type()
)
hwPimSGRptUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptUpTime.setStatus("current")


class _HwPimSGRptUpstreamPruneState_Type(Integer32):
    """Custom type hwPimSGRptUpstreamPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPruned", 3),
          ("pruned", 2),
          ("rptNotJoined", 1))
    )


_HwPimSGRptUpstreamPruneState_Type.__name__ = "Integer32"
_HwPimSGRptUpstreamPruneState_Object = MibTableColumn
hwPimSGRptUpstreamPruneState = _HwPimSGRptUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8, 1, 3),
    _HwPimSGRptUpstreamPruneState_Type()
)
hwPimSGRptUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptUpstreamPruneState.setStatus("current")
_HwPimSGRptUpstreamOverrideTimer_Type = TimeTicks
_HwPimSGRptUpstreamOverrideTimer_Object = MibTableColumn
hwPimSGRptUpstreamOverrideTimer = _HwPimSGRptUpstreamOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 8, 1, 4),
    _HwPimSGRptUpstreamOverrideTimer_Type()
)
hwPimSGRptUpstreamOverrideTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptUpstreamOverrideTimer.setStatus("current")
_HwPimSGRptITable_Object = MibTable
hwPimSGRptITable = _HwPimSGRptITable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9)
)
if mibBuilder.loadTexts:
    hwPimSGRptITable.setStatus("current")
_HwPimSGRptIEntry_Object = MibTableRow
hwPimSGRptIEntry = _HwPimSGRptIEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1)
)
hwPimSGRptIEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimStarGGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGRptSrcAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimSGRptIIfIndex"),
)
if mibBuilder.loadTexts:
    hwPimSGRptIEntry.setStatus("current")
_HwPimSGRptIIfIndex_Type = InterfaceIndex
_HwPimSGRptIIfIndex_Object = MibTableColumn
hwPimSGRptIIfIndex = _HwPimSGRptIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 1),
    _HwPimSGRptIIfIndex_Type()
)
hwPimSGRptIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimSGRptIIfIndex.setStatus("current")
_HwPimSGRptIUpTime_Type = TimeTicks
_HwPimSGRptIUpTime_Object = MibTableColumn
hwPimSGRptIUpTime = _HwPimSGRptIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 2),
    _HwPimSGRptIUpTime_Type()
)
hwPimSGRptIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptIUpTime.setStatus("current")
_HwPimSGRptILocalMembership_Type = TruthValue
_HwPimSGRptILocalMembership_Object = MibTableColumn
hwPimSGRptILocalMembership = _HwPimSGRptILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 3),
    _HwPimSGRptILocalMembership_Type()
)
hwPimSGRptILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptILocalMembership.setStatus("current")


class _HwPimSGRptIJoinPruneState_Type(Integer32):
    """Custom type hwPimSGRptIJoinPruneState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 1),
          ("prune", 2),
          ("prunePending", 3))
    )


_HwPimSGRptIJoinPruneState_Type.__name__ = "Integer32"
_HwPimSGRptIJoinPruneState_Object = MibTableColumn
hwPimSGRptIJoinPruneState = _HwPimSGRptIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 4),
    _HwPimSGRptIJoinPruneState_Type()
)
hwPimSGRptIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptIJoinPruneState.setStatus("current")
_HwPimSGRptIPrunePendingTimer_Type = TimeTicks
_HwPimSGRptIPrunePendingTimer_Object = MibTableColumn
hwPimSGRptIPrunePendingTimer = _HwPimSGRptIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 5),
    _HwPimSGRptIPrunePendingTimer_Type()
)
hwPimSGRptIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptIPrunePendingTimer.setStatus("current")
_HwPimSGRptIPruneExpiryTimer_Type = TimeTicks
_HwPimSGRptIPruneExpiryTimer_Object = MibTableColumn
hwPimSGRptIPruneExpiryTimer = _HwPimSGRptIPruneExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 9, 1, 6),
    _HwPimSGRptIPruneExpiryTimer_Type()
)
hwPimSGRptIPruneExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptIPruneExpiryTimer.setStatus("current")
_HwPimGroupMappingTable_Object = MibTable
hwPimGroupMappingTable = _HwPimGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13)
)
if mibBuilder.loadTexts:
    hwPimGroupMappingTable.setStatus("current")
_HwPimGroupMappingEntry_Object = MibTableRow
hwPimGroupMappingEntry = _HwPimGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1)
)
hwPimGroupMappingEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingOrigin"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingGrpAddress"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingGrpPrefixLength"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingRpAddressType"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGroupMappingRpAddress"),
)
if mibBuilder.loadTexts:
    hwPimGroupMappingEntry.setStatus("current")
_HwPimGroupMappingOrigin_Type = HWPimGroupMappingOriginType
_HwPimGroupMappingOrigin_Object = MibTableColumn
hwPimGroupMappingOrigin = _HwPimGroupMappingOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 1),
    _HwPimGroupMappingOrigin_Type()
)
hwPimGroupMappingOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingOrigin.setStatus("current")
_HwPimGroupMappingAddressType_Type = InetAddressType
_HwPimGroupMappingAddressType_Object = MibTableColumn
hwPimGroupMappingAddressType = _HwPimGroupMappingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 2),
    _HwPimGroupMappingAddressType_Type()
)
hwPimGroupMappingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingAddressType.setStatus("current")


class _HwPimGroupMappingGrpAddress_Type(InetAddress):
    """Custom type hwPimGroupMappingGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimGroupMappingGrpAddress_Type.__name__ = "InetAddress"
_HwPimGroupMappingGrpAddress_Object = MibTableColumn
hwPimGroupMappingGrpAddress = _HwPimGroupMappingGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 3),
    _HwPimGroupMappingGrpAddress_Type()
)
hwPimGroupMappingGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingGrpAddress.setStatus("current")


class _HwPimGroupMappingGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type hwPimGroupMappingGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_HwPimGroupMappingGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_HwPimGroupMappingGrpPrefixLength_Object = MibTableColumn
hwPimGroupMappingGrpPrefixLength = _HwPimGroupMappingGrpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 4),
    _HwPimGroupMappingGrpPrefixLength_Type()
)
hwPimGroupMappingGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingGrpPrefixLength.setStatus("current")
_HwPimGroupMappingRpAddressType_Type = InetAddressType
_HwPimGroupMappingRpAddressType_Object = MibTableColumn
hwPimGroupMappingRpAddressType = _HwPimGroupMappingRpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 5),
    _HwPimGroupMappingRpAddressType_Type()
)
hwPimGroupMappingRpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingRpAddressType.setStatus("current")


class _HwPimGroupMappingRpAddress_Type(InetAddress):
    """Custom type hwPimGroupMappingRpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimGroupMappingRpAddress_Type.__name__ = "InetAddress"
_HwPimGroupMappingRpAddress_Object = MibTableColumn
hwPimGroupMappingRpAddress = _HwPimGroupMappingRpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 6),
    _HwPimGroupMappingRpAddress_Type()
)
hwPimGroupMappingRpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGroupMappingRpAddress.setStatus("current")
_HwPimGroupMappingPimMode_Type = HWPimMode
_HwPimGroupMappingPimMode_Object = MibTableColumn
hwPimGroupMappingPimMode = _HwPimGroupMappingPimMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 7),
    _HwPimGroupMappingPimMode_Type()
)
hwPimGroupMappingPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGroupMappingPimMode.setStatus("current")
_HwPimGroupMappingPrecedence_Type = Unsigned32
_HwPimGroupMappingPrecedence_Object = MibTableColumn
hwPimGroupMappingPrecedence = _HwPimGroupMappingPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 13, 1, 8),
    _HwPimGroupMappingPrecedence_Type()
)
hwPimGroupMappingPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGroupMappingPrecedence.setStatus("current")


class _HwPimKeepalivePeriod_Type(Unsigned32):
    """Custom type hwPimKeepalivePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimKeepalivePeriod_Type.__name__ = "Unsigned32"
_HwPimKeepalivePeriod_Object = MibScalar
hwPimKeepalivePeriod = _HwPimKeepalivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 14),
    _HwPimKeepalivePeriod_Type()
)
hwPimKeepalivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimKeepalivePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimKeepalivePeriod.setUnits("seconds")


class _HwPimRegisterSuppressionTime_Type(Unsigned32):
    """Custom type hwPimRegisterSuppressionTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimRegisterSuppressionTime_Type.__name__ = "Unsigned32"
_HwPimRegisterSuppressionTime_Object = MibScalar
hwPimRegisterSuppressionTime = _HwPimRegisterSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 15),
    _HwPimRegisterSuppressionTime_Type()
)
hwPimRegisterSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimRegisterSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    hwPimRegisterSuppressionTime.setUnits("seconds")
_HwPimStarGEntries_Type = Gauge32
_HwPimStarGEntries_Object = MibScalar
hwPimStarGEntries = _HwPimStarGEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 16),
    _HwPimStarGEntries_Type()
)
hwPimStarGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGEntries.setStatus("current")
_HwPimStarGIEntries_Type = Gauge32
_HwPimStarGIEntries_Object = MibScalar
hwPimStarGIEntries = _HwPimStarGIEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 17),
    _HwPimStarGIEntries_Type()
)
hwPimStarGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimStarGIEntries.setStatus("current")
_HwPimSGEntries_Type = Gauge32
_HwPimSGEntries_Object = MibScalar
hwPimSGEntries = _HwPimSGEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 18),
    _HwPimSGEntries_Type()
)
hwPimSGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGEntries.setStatus("current")
_HwPimSGIEntries_Type = Gauge32
_HwPimSGIEntries_Object = MibScalar
hwPimSGIEntries = _HwPimSGIEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 19),
    _HwPimSGIEntries_Type()
)
hwPimSGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGIEntries.setStatus("current")
_HwPimSGRptEntries_Type = Gauge32
_HwPimSGRptEntries_Object = MibScalar
hwPimSGRptEntries = _HwPimSGRptEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 20),
    _HwPimSGRptEntries_Type()
)
hwPimSGRptEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptEntries.setStatus("current")
_HwPimSGRptIEntries_Type = Gauge32
_HwPimSGRptIEntries_Object = MibScalar
hwPimSGRptIEntries = _HwPimSGRptIEntries_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 21),
    _HwPimSGRptIEntries_Type()
)
hwPimSGRptIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimSGRptIEntries.setStatus("current")
_HwPimOutAsserts_Type = Counter64
_HwPimOutAsserts_Object = MibScalar
hwPimOutAsserts = _HwPimOutAsserts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 22),
    _HwPimOutAsserts_Type()
)
hwPimOutAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimOutAsserts.setStatus("current")
_HwPimInAsserts_Type = Counter64
_HwPimInAsserts_Object = MibScalar
hwPimInAsserts = _HwPimInAsserts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 23),
    _HwPimInAsserts_Type()
)
hwPimInAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInAsserts.setStatus("current")
_HwPimLastAssertInterface_Type = InterfaceIndexOrZero
_HwPimLastAssertInterface_Object = MibScalar
hwPimLastAssertInterface = _HwPimLastAssertInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 24),
    _HwPimLastAssertInterface_Type()
)
hwPimLastAssertInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimLastAssertInterface.setStatus("current")
_HwPimLastAssertGroupAddressType_Type = InetAddressType
_HwPimLastAssertGroupAddressType_Object = MibScalar
hwPimLastAssertGroupAddressType = _HwPimLastAssertGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 25),
    _HwPimLastAssertGroupAddressType_Type()
)
hwPimLastAssertGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimLastAssertGroupAddressType.setStatus("current")


class _HwPimLastAssertGroupAddress_Type(InetAddress):
    """Custom type hwPimLastAssertGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimLastAssertGroupAddress_Type.__name__ = "InetAddress"
_HwPimLastAssertGroupAddress_Object = MibScalar
hwPimLastAssertGroupAddress = _HwPimLastAssertGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 26),
    _HwPimLastAssertGroupAddress_Type()
)
hwPimLastAssertGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimLastAssertGroupAddress.setStatus("current")
_HwPimLastAssertSourceAddressType_Type = InetAddressType
_HwPimLastAssertSourceAddressType_Object = MibScalar
hwPimLastAssertSourceAddressType = _HwPimLastAssertSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 27),
    _HwPimLastAssertSourceAddressType_Type()
)
hwPimLastAssertSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimLastAssertSourceAddressType.setStatus("current")


class _HwPimLastAssertSourceAddress_Type(InetAddress):
    """Custom type hwPimLastAssertSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimLastAssertSourceAddress_Type.__name__ = "InetAddress"
_HwPimLastAssertSourceAddress_Object = MibScalar
hwPimLastAssertSourceAddress = _HwPimLastAssertSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 28),
    _HwPimLastAssertSourceAddress_Type()
)
hwPimLastAssertSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimLastAssertSourceAddress.setStatus("current")


class _HwPimNeighborLossNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimNeighborLossNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimNeighborLossNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimNeighborLossNotificationPeriod_Object = MibScalar
hwPimNeighborLossNotificationPeriod = _HwPimNeighborLossNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 29),
    _HwPimNeighborLossNotificationPeriod_Type()
)
hwPimNeighborLossNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimNeighborLossNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimNeighborLossNotificationPeriod.setUnits("seconds")
_HwPimNeighborLossCount_Type = Counter32
_HwPimNeighborLossCount_Object = MibScalar
hwPimNeighborLossCount = _HwPimNeighborLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 30),
    _HwPimNeighborLossCount_Type()
)
hwPimNeighborLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborLossCount.setStatus("current")


class _HwPimInvalidRegisterNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimInvalidRegisterNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_HwPimInvalidRegisterNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimInvalidRegisterNotificationPeriod_Object = MibScalar
hwPimInvalidRegisterNotificationPeriod = _HwPimInvalidRegisterNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 31),
    _HwPimInvalidRegisterNotificationPeriod_Type()
)
hwPimInvalidRegisterNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterNotificationPeriod.setUnits("seconds")
_HwPimInvalidRegisterMsgsRcvd_Type = Counter32
_HwPimInvalidRegisterMsgsRcvd_Object = MibScalar
hwPimInvalidRegisterMsgsRcvd = _HwPimInvalidRegisterMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 32),
    _HwPimInvalidRegisterMsgsRcvd_Type()
)
hwPimInvalidRegisterMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterMsgsRcvd.setStatus("current")
_HwPimInvalidRegisterAddressType_Type = InetAddressType
_HwPimInvalidRegisterAddressType_Object = MibScalar
hwPimInvalidRegisterAddressType = _HwPimInvalidRegisterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 33),
    _HwPimInvalidRegisterAddressType_Type()
)
hwPimInvalidRegisterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterAddressType.setStatus("current")


class _HwPimInvalidRegisterOrigin_Type(InetAddress):
    """Custom type hwPimInvalidRegisterOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidRegisterOrigin_Type.__name__ = "InetAddress"
_HwPimInvalidRegisterOrigin_Object = MibScalar
hwPimInvalidRegisterOrigin = _HwPimInvalidRegisterOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 34),
    _HwPimInvalidRegisterOrigin_Type()
)
hwPimInvalidRegisterOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterOrigin.setStatus("current")


class _HwPimInvalidRegisterGroup_Type(InetAddress):
    """Custom type hwPimInvalidRegisterGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidRegisterGroup_Type.__name__ = "InetAddress"
_HwPimInvalidRegisterGroup_Object = MibScalar
hwPimInvalidRegisterGroup = _HwPimInvalidRegisterGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 35),
    _HwPimInvalidRegisterGroup_Type()
)
hwPimInvalidRegisterGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterGroup.setStatus("current")


class _HwPimInvalidRegisterRp_Type(InetAddress):
    """Custom type hwPimInvalidRegisterRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidRegisterRp_Type.__name__ = "InetAddress"
_HwPimInvalidRegisterRp_Object = MibScalar
hwPimInvalidRegisterRp = _HwPimInvalidRegisterRp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 36),
    _HwPimInvalidRegisterRp_Type()
)
hwPimInvalidRegisterRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidRegisterRp.setStatus("current")


class _HwPimInvalidJoinPruneNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimInvalidJoinPruneNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_HwPimInvalidJoinPruneNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimInvalidJoinPruneNotificationPeriod_Object = MibScalar
hwPimInvalidJoinPruneNotificationPeriod = _HwPimInvalidJoinPruneNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 37),
    _HwPimInvalidJoinPruneNotificationPeriod_Type()
)
hwPimInvalidJoinPruneNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneNotificationPeriod.setUnits("seconds")
_HwPimInvalidJoinPruneMsgsRcvd_Type = Counter32
_HwPimInvalidJoinPruneMsgsRcvd_Object = MibScalar
hwPimInvalidJoinPruneMsgsRcvd = _HwPimInvalidJoinPruneMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 38),
    _HwPimInvalidJoinPruneMsgsRcvd_Type()
)
hwPimInvalidJoinPruneMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneMsgsRcvd.setStatus("current")
_HwPimInvalidJoinPruneAddressType_Type = InetAddressType
_HwPimInvalidJoinPruneAddressType_Object = MibScalar
hwPimInvalidJoinPruneAddressType = _HwPimInvalidJoinPruneAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 39),
    _HwPimInvalidJoinPruneAddressType_Type()
)
hwPimInvalidJoinPruneAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneAddressType.setStatus("current")


class _HwPimInvalidJoinPruneOrigin_Type(InetAddress):
    """Custom type hwPimInvalidJoinPruneOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidJoinPruneOrigin_Type.__name__ = "InetAddress"
_HwPimInvalidJoinPruneOrigin_Object = MibScalar
hwPimInvalidJoinPruneOrigin = _HwPimInvalidJoinPruneOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 40),
    _HwPimInvalidJoinPruneOrigin_Type()
)
hwPimInvalidJoinPruneOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneOrigin.setStatus("current")


class _HwPimInvalidJoinPruneGroup_Type(InetAddress):
    """Custom type hwPimInvalidJoinPruneGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidJoinPruneGroup_Type.__name__ = "InetAddress"
_HwPimInvalidJoinPruneGroup_Object = MibScalar
hwPimInvalidJoinPruneGroup = _HwPimInvalidJoinPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 41),
    _HwPimInvalidJoinPruneGroup_Type()
)
hwPimInvalidJoinPruneGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneGroup.setStatus("current")


class _HwPimInvalidJoinPruneRp_Type(InetAddress):
    """Custom type hwPimInvalidJoinPruneRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimInvalidJoinPruneRp_Type.__name__ = "InetAddress"
_HwPimInvalidJoinPruneRp_Object = MibScalar
hwPimInvalidJoinPruneRp = _HwPimInvalidJoinPruneRp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 42),
    _HwPimInvalidJoinPruneRp_Type()
)
hwPimInvalidJoinPruneRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInvalidJoinPruneRp.setStatus("current")


class _HwPimRpMappingNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimRpMappingNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimRpMappingNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimRpMappingNotificationPeriod_Object = MibScalar
hwPimRpMappingNotificationPeriod = _HwPimRpMappingNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 43),
    _HwPimRpMappingNotificationPeriod_Type()
)
hwPimRpMappingNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimRpMappingNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimRpMappingNotificationPeriod.setUnits("seconds")
_HwPimRpMappingChangeCount_Type = Counter32
_HwPimRpMappingChangeCount_Object = MibScalar
hwPimRpMappingChangeCount = _HwPimRpMappingChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 44),
    _HwPimRpMappingChangeCount_Type()
)
hwPimRpMappingChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimRpMappingChangeCount.setStatus("current")


class _HwPimInterfaceElectionNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimInterfaceElectionNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimInterfaceElectionNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimInterfaceElectionNotificationPeriod_Object = MibScalar
hwPimInterfaceElectionNotificationPeriod = _HwPimInterfaceElectionNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 45),
    _HwPimInterfaceElectionNotificationPeriod_Type()
)
hwPimInterfaceElectionNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimInterfaceElectionNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimInterfaceElectionNotificationPeriod.setUnits("seconds")
_HwPimInterfaceElectionWinCount_Type = Counter32
_HwPimInterfaceElectionWinCount_Object = MibScalar
hwPimInterfaceElectionWinCount = _HwPimInterfaceElectionWinCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 46),
    _HwPimInterfaceElectionWinCount_Type()
)
hwPimInterfaceElectionWinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceElectionWinCount.setStatus("current")


class _HwPimRefreshInterval_Type(Unsigned32):
    """Custom type hwPimRefreshInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimRefreshInterval_Type.__name__ = "Unsigned32"
_HwPimRefreshInterval_Object = MibScalar
hwPimRefreshInterval = _HwPimRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 47),
    _HwPimRefreshInterval_Type()
)
hwPimRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwPimRefreshInterval.setUnits("seconds")
_HwPimDeviceConfigStorageType_Type = StorageType
_HwPimDeviceConfigStorageType_Object = MibScalar
hwPimDeviceConfigStorageType = _HwPimDeviceConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 48),
    _HwPimDeviceConfigStorageType_Type()
)
hwPimDeviceConfigStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimDeviceConfigStorageType.setStatus("current")
_HwPimNeighborAddCount_Type = Counter32
_HwPimNeighborAddCount_Object = MibScalar
hwPimNeighborAddCount = _HwPimNeighborAddCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 49),
    _HwPimNeighborAddCount_Type()
)
hwPimNeighborAddCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimNeighborAddCount.setStatus("current")


class _HwPimNeighborAddNotificationPeriod_Type(Unsigned32):
    """Custom type hwPimNeighborAddNotificationPeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwPimNeighborAddNotificationPeriod_Type.__name__ = "Unsigned32"
_HwPimNeighborAddNotificationPeriod_Object = MibScalar
hwPimNeighborAddNotificationPeriod = _HwPimNeighborAddNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 50),
    _HwPimNeighborAddNotificationPeriod_Type()
)
hwPimNeighborAddNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPimNeighborAddNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwPimNeighborAddNotificationPeriod.setUnits("seconds")
_HwPimGRStartTime_Type = TimeStamp
_HwPimGRStartTime_Object = MibScalar
hwPimGRStartTime = _HwPimGRStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 51),
    _HwPimGRStartTime_Type()
)
hwPimGRStartTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimGRStartTime.setStatus("obsolete")


class _HwPimGRInterval_Type(Unsigned32):
    """Custom type hwPimGRInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 3600),
    )


_HwPimGRInterval_Type.__name__ = "Unsigned32"
_HwPimGRInterval_Object = MibScalar
hwPimGRInterval = _HwPimGRInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 52),
    _HwPimGRInterval_Type()
)
hwPimGRInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimGRInterval.setStatus("obsolete")
_HwPimGREndTime_Type = TimeStamp
_HwPimGREndTime_Object = MibScalar
hwPimGREndTime = _HwPimGREndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 53),
    _HwPimGREndTime_Type()
)
hwPimGREndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimGREndTime.setStatus("obsolete")
_HwPimMrtLimitAddressType_Type = InetAddressType
_HwPimMrtLimitAddressType_Object = MibScalar
hwPimMrtLimitAddressType = _HwPimMrtLimitAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 54),
    _HwPimMrtLimitAddressType_Type()
)
hwPimMrtLimitAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimMrtLimitAddressType.setStatus("current")


class _HwPimMrtLimitSource_Type(InetAddress):
    """Custom type hwPimMrtLimitSource based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimMrtLimitSource_Type.__name__ = "InetAddress"
_HwPimMrtLimitSource_Object = MibScalar
hwPimMrtLimitSource = _HwPimMrtLimitSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 55),
    _HwPimMrtLimitSource_Type()
)
hwPimMrtLimitSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimMrtLimitSource.setStatus("current")


class _HwPimMrtLimitGroup_Type(InetAddress):
    """Custom type hwPimMrtLimitGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimMrtLimitGroup_Type.__name__ = "InetAddress"
_HwPimMrtLimitGroup_Object = MibScalar
hwPimMrtLimitGroup = _HwPimMrtLimitGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 56),
    _HwPimMrtLimitGroup_Type()
)
hwPimMrtLimitGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimMrtLimitGroup.setStatus("current")
_HwPimInstanceID_Type = Unsigned32
_HwPimInstanceID_Object = MibScalar
hwPimInstanceID = _HwPimInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 57),
    _HwPimInstanceID_Type()
)
hwPimInstanceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimInstanceID.setStatus("current")
_HwPimInterfaceCtlMsgCountTable_Object = MibTable
hwPimInterfaceCtlMsgCountTable = _HwPimInterfaceCtlMsgCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58)
)
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountTable.setStatus("current")
_HwPimInterfaceCtlMsgCountEntry_Object = MibTableRow
hwPimInterfaceCtlMsgCountEntry = _HwPimInterfaceCtlMsgCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1)
)
hwPimInterfaceCtlMsgCountEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimInterfaceCtlMsgCountIfIndex"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimInterfaceCtlMsgCountIpVersion"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimInterfaceCtlMsgCountMsgState"),
)
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountEntry.setStatus("current")
_HwPimInterfaceCtlMsgCountIfIndex_Type = InterfaceIndex
_HwPimInterfaceCtlMsgCountIfIndex_Object = MibTableColumn
hwPimInterfaceCtlMsgCountIfIndex = _HwPimInterfaceCtlMsgCountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 1),
    _HwPimInterfaceCtlMsgCountIfIndex_Type()
)
hwPimInterfaceCtlMsgCountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountIfIndex.setStatus("current")
_HwPimInterfaceCtlMsgCountIpVersion_Type = InetVersion
_HwPimInterfaceCtlMsgCountIpVersion_Object = MibTableColumn
hwPimInterfaceCtlMsgCountIpVersion = _HwPimInterfaceCtlMsgCountIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 2),
    _HwPimInterfaceCtlMsgCountIpVersion_Type()
)
hwPimInterfaceCtlMsgCountIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountIpVersion.setStatus("current")
_HwPimInterfaceCtlMsgCountMsgState_Type = HWPimCtlMsgState
_HwPimInterfaceCtlMsgCountMsgState_Object = MibTableColumn
hwPimInterfaceCtlMsgCountMsgState = _HwPimInterfaceCtlMsgCountMsgState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 3),
    _HwPimInterfaceCtlMsgCountMsgState_Type()
)
hwPimInterfaceCtlMsgCountMsgState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountMsgState.setStatus("current")
_HwPimInterfaceCtlMsgCountAssert_Type = Unsigned32
_HwPimInterfaceCtlMsgCountAssert_Object = MibTableColumn
hwPimInterfaceCtlMsgCountAssert = _HwPimInterfaceCtlMsgCountAssert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 4),
    _HwPimInterfaceCtlMsgCountAssert_Type()
)
hwPimInterfaceCtlMsgCountAssert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountAssert.setStatus("current")
_HwPimInterfaceCtlMsgCountHello_Type = Unsigned32
_HwPimInterfaceCtlMsgCountHello_Object = MibTableColumn
hwPimInterfaceCtlMsgCountHello = _HwPimInterfaceCtlMsgCountHello_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 5),
    _HwPimInterfaceCtlMsgCountHello_Type()
)
hwPimInterfaceCtlMsgCountHello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountHello.setStatus("current")
_HwPimInterfaceCtlMsgCountJoinPrune_Type = Unsigned32
_HwPimInterfaceCtlMsgCountJoinPrune_Object = MibTableColumn
hwPimInterfaceCtlMsgCountJoinPrune = _HwPimInterfaceCtlMsgCountJoinPrune_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 6),
    _HwPimInterfaceCtlMsgCountJoinPrune_Type()
)
hwPimInterfaceCtlMsgCountJoinPrune.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountJoinPrune.setStatus("current")
_HwPimInterfaceCtlMsgCountBsr_Type = Unsigned32
_HwPimInterfaceCtlMsgCountBsr_Object = MibTableColumn
hwPimInterfaceCtlMsgCountBsr = _HwPimInterfaceCtlMsgCountBsr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 58, 1, 7),
    _HwPimInterfaceCtlMsgCountBsr_Type()
)
hwPimInterfaceCtlMsgCountBsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimInterfaceCtlMsgCountBsr.setStatus("current")
_HwPimGlobalCtlMsgCountTable_Object = MibTable
hwPimGlobalCtlMsgCountTable = _HwPimGlobalCtlMsgCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59)
)
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountTable.setStatus("current")
_HwPimGlobalCtlMsgCountEntry_Object = MibTableRow
hwPimGlobalCtlMsgCountEntry = _HwPimGlobalCtlMsgCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1)
)
hwPimGlobalCtlMsgCountEntry.setIndexNames(
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGlobalCtlMsgCountIpVersion"),
    (0, "HUAWEI-PIM-STD-MIB", "hwPimGlobalCtlMsgCountMsgState"),
)
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountEntry.setStatus("current")
_HwPimGlobalCtlMsgCountIpVersion_Type = InetVersion
_HwPimGlobalCtlMsgCountIpVersion_Object = MibTableColumn
hwPimGlobalCtlMsgCountIpVersion = _HwPimGlobalCtlMsgCountIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 1),
    _HwPimGlobalCtlMsgCountIpVersion_Type()
)
hwPimGlobalCtlMsgCountIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountIpVersion.setStatus("current")
_HwPimGlobalCtlMsgCountMsgState_Type = HWPimCtlMsgState
_HwPimGlobalCtlMsgCountMsgState_Object = MibTableColumn
hwPimGlobalCtlMsgCountMsgState = _HwPimGlobalCtlMsgCountMsgState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 2),
    _HwPimGlobalCtlMsgCountMsgState_Type()
)
hwPimGlobalCtlMsgCountMsgState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountMsgState.setStatus("current")
_HwPimGlobalCtlMsgCountRegister_Type = Unsigned32
_HwPimGlobalCtlMsgCountRegister_Object = MibTableColumn
hwPimGlobalCtlMsgCountRegister = _HwPimGlobalCtlMsgCountRegister_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 3),
    _HwPimGlobalCtlMsgCountRegister_Type()
)
hwPimGlobalCtlMsgCountRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountRegister.setStatus("current")
_HwPimGlobalCtlMsgCountRegisterStop_Type = Unsigned32
_HwPimGlobalCtlMsgCountRegisterStop_Object = MibTableColumn
hwPimGlobalCtlMsgCountRegisterStop = _HwPimGlobalCtlMsgCountRegisterStop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 4),
    _HwPimGlobalCtlMsgCountRegisterStop_Type()
)
hwPimGlobalCtlMsgCountRegisterStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountRegisterStop.setStatus("current")
_HwPimGlobalCtlMsgCountProbe_Type = Unsigned32
_HwPimGlobalCtlMsgCountProbe_Object = MibTableColumn
hwPimGlobalCtlMsgCountProbe = _HwPimGlobalCtlMsgCountProbe_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 5),
    _HwPimGlobalCtlMsgCountProbe_Type()
)
hwPimGlobalCtlMsgCountProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountProbe.setStatus("current")
_HwPimGlobalCtlMsgCountCrp_Type = Unsigned32
_HwPimGlobalCtlMsgCountCrp_Object = MibTableColumn
hwPimGlobalCtlMsgCountCrp = _HwPimGlobalCtlMsgCountCrp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 59, 1, 6),
    _HwPimGlobalCtlMsgCountCrp_Type()
)
hwPimGlobalCtlMsgCountCrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPimGlobalCtlMsgCountCrp.setStatus("current")
_HwPimInstanceName_Type = DisplayString
_HwPimInstanceName_Object = MibScalar
hwPimInstanceName = _HwPimInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 60),
    _HwPimInstanceName_Type()
)
hwPimInstanceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimInstanceName.setStatus("current")


class _HwPimNeighborNotificationReason_Type(Integer32):
    """Custom type hwPimNeighborNotificationReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 100),
          ("alarmTimeOut", 6),
          ("bfdSessionDown", 8),
          ("holdTimeExpired", 1),
          ("interfaceIsDown", 3),
          ("neighbourIsDeleted", 5),
          ("notReceiveHelloForALongTime", 2),
          ("receiveHelloAgain", 4),
          ("receiveHelloHoldTimeZero", 7),
          ("userOperation", 9))
    )


_HwPimNeighborNotificationReason_Type.__name__ = "Integer32"
_HwPimNeighborNotificationReason_Object = MibScalar
hwPimNeighborNotificationReason = _HwPimNeighborNotificationReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 61),
    _HwPimNeighborNotificationReason_Type()
)
hwPimNeighborNotificationReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimNeighborNotificationReason.setStatus("current")
_HwPimNotificationAddressType_Type = InetAddressType
_HwPimNotificationAddressType_Object = MibScalar
hwPimNotificationAddressType = _HwPimNotificationAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 62),
    _HwPimNotificationAddressType_Type()
)
hwPimNotificationAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimNotificationAddressType.setStatus("current")


class _HwPimStarGCurrentCount_Type(Unsigned32):
    """Custom type hwPimStarGCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwPimStarGCurrentCount_Type.__name__ = "Unsigned32"
_HwPimStarGCurrentCount_Object = MibScalar
hwPimStarGCurrentCount = _HwPimStarGCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 63),
    _HwPimStarGCurrentCount_Type()
)
hwPimStarGCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimStarGCurrentCount.setStatus("current")


class _HwPimStarGTotalCount_Type(Unsigned32):
    """Custom type hwPimStarGTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwPimStarGTotalCount_Type.__name__ = "Unsigned32"
_HwPimStarGTotalCount_Object = MibScalar
hwPimStarGTotalCount = _HwPimStarGTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 64),
    _HwPimStarGTotalCount_Type()
)
hwPimStarGTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimStarGTotalCount.setStatus("current")


class _HwPimStarGThreshold_Type(Unsigned32):
    """Custom type hwPimStarGThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwPimStarGThreshold_Type.__name__ = "Unsigned32"
_HwPimStarGThreshold_Object = MibScalar
hwPimStarGThreshold = _HwPimStarGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 65),
    _HwPimStarGThreshold_Type()
)
hwPimStarGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimStarGThreshold.setStatus("current")


class _HwPimSGCurrentCount_Type(Unsigned32):
    """Custom type hwPimSGCurrentCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwPimSGCurrentCount_Type.__name__ = "Unsigned32"
_HwPimSGCurrentCount_Object = MibScalar
hwPimSGCurrentCount = _HwPimSGCurrentCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 66),
    _HwPimSGCurrentCount_Type()
)
hwPimSGCurrentCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimSGCurrentCount.setStatus("current")


class _HwPimSGTotalCount_Type(Unsigned32):
    """Custom type hwPimSGTotalCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 262144),
    )


_HwPimSGTotalCount_Type.__name__ = "Unsigned32"
_HwPimSGTotalCount_Object = MibScalar
hwPimSGTotalCount = _HwPimSGTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 67),
    _HwPimSGTotalCount_Type()
)
hwPimSGTotalCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimSGTotalCount.setStatus("current")


class _HwPimSGThreshold_Type(Unsigned32):
    """Custom type hwPimSGThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwPimSGThreshold_Type.__name__ = "Unsigned32"
_HwPimSGThreshold_Object = MibScalar
hwPimSGThreshold = _HwPimSGThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 68),
    _HwPimSGThreshold_Type()
)
hwPimSGThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimSGThreshold.setStatus("current")


class _HwPimNotificationSrcAddr_Type(InetAddress):
    """Custom type hwPimNotificationSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimNotificationSrcAddr_Type.__name__ = "InetAddress"
_HwPimNotificationSrcAddr_Object = MibScalar
hwPimNotificationSrcAddr = _HwPimNotificationSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 69),
    _HwPimNotificationSrcAddr_Type()
)
hwPimNotificationSrcAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimNotificationSrcAddr.setStatus("current")


class _HwPimNotificationGrpAddr_Type(InetAddress):
    """Custom type hwPimNotificationGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HwPimNotificationGrpAddr_Type.__name__ = "InetAddress"
_HwPimNotificationGrpAddr_Object = MibScalar
hwPimNotificationGrpAddr = _HwPimNotificationGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 1, 70),
    _HwPimNotificationGrpAddr_Type()
)
hwPimNotificationGrpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPimNotificationGrpAddr.setStatus("current")
_HwPimMibConformance_ObjectIdentity = ObjectIdentity
hwPimMibConformance = _HwPimMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2)
)
_HwPimMibCompliances_ObjectIdentity = ObjectIdentity
hwPimMibCompliances = _HwPimMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 1)
)
_HwPimMibGroups_ObjectIdentity = ObjectIdentity
hwPimMibGroups = _HwPimMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2)
)

# Managed Objects groups

hwPimTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 1)
)
hwPimTopologyGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimInterfaceAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceGenerationIdValue"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceDr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceDrPriorityEnabled"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceHelloHoldtime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceJoinPruneHoldtime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceLanDelayEnabled"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceEffectPropagDelay"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceEffectOverrideIvl"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceSuppressionEnabled"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceBidirCapable"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborGenerationIdPresent"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborGenerationIdValue"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborExpiryTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborDrPriorityPresent"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborDrPriority"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborLanPruneDelayPresent"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborTBit"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborPropagationDelay"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborOverrideInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborBidirCapable"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNbrSecAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborIfName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceName"))
)
if mibBuilder.loadTexts:
    hwPimTopologyGroup.setStatus("current")

hwPimTuningParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 3)
)
hwPimTuningParametersGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimKeepalivePeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimRegisterSuppressionTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceDrPriority"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceHelloInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceTrigHelloInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceJoinPruneInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfacePropagationDelay"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceOverrideInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceDomainBorder"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceStubInterface"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceStatus"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceStorageType"))
)
if mibBuilder.loadTexts:
    hwPimTuningParametersGroup.setStatus("current")

hwPimRouterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 4)
)
hwPimRouterStatisticsGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimStarGEntries"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIEntries"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGEntries"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIEntries"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptEntries"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptIEntries"))
)
if mibBuilder.loadTexts:
    hwPimRouterStatisticsGroup.setStatus("current")

hwPimSsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 5)
)
hwPimSsmGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimSGUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGUpstreamJoinState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGUpstreamJoinTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGUpstreamNeighbor"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfIfIndex"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfNextHopType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfNextHop"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfRouteProtocol"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfRouteAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfRoutePrefixLength"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfRouteMetricPref"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpfRouteMetric"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGSptBit"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGKeepaliveTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGDrRegisterState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGDrRegisterStopTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpRegisterPmbrAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRpRegisterPmbrAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGILocalMembership"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIJoinPruneState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIPrunePendingTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIJoinExpiryTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertWinnerAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertWinnerAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertWinnerMetricPref"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGIAssertWinnerMetric"))
)
if mibBuilder.loadTexts:
    hwPimSsmGroup.setStatus("current")

hwPimRpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 6)
)
hwPimRpConfigGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPrecedence"))
)
if mibBuilder.loadTexts:
    hwPimRpConfigGroup.setStatus("current")

hwPimSmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 7)
)
hwPimSmGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimStarGUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGPimModeOrigin"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpIsLocal"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGUpstreamJoinState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGUpstreamJoinTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGUpstreamNeighborType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGUpstreamNeighbor"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfIfIndex"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfNextHopType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfNextHop"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfRouteProtocol"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfRouteAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfRoutePrefixLength"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfRouteMetricPref"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGRpfRouteMetric"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGILocalMembership"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIJoinPruneState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIPrunePendingTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIJoinExpiryTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertWinnerAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertWinnerAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertWinnerMetricPref"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGIAssertWinnerMetric"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptUpstreamPruneState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptUpstreamOverrideTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptIUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptILocalMembership"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptIJoinPruneState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptIPrunePendingTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGRptIPruneExpiryTimer"))
)
if mibBuilder.loadTexts:
    hwPimSmGroup.setStatus("current")

hwPimBidirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 8)
)
hwPimBidirGroup.setObjects(
    ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceDfElectionRobustness")
)
if mibBuilder.loadTexts:
    hwPimBidirGroup.setStatus("current")

hwPimNetMgmtNotificationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 11)
)
hwPimNetMgmtNotificationObjects.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterMsgsRcvd"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterOrigin"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterRp"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneMsgsRcvd"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneOrigin"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneRp"),
        ("HUAWEI-PIM-STD-MIB", "hwPimRpMappingNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimRpMappingChangeCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceElectionNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceElectionWinCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborAddNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborAddCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGRStartTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGRInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGREndTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitSource"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborNotificationReason"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGTotalCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGTotalCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationSrcAddr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationGrpAddr"))
)
if mibBuilder.loadTexts:
    hwPimNetMgmtNotificationObjects.setStatus("current")

hwPimDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 13)
)
hwPimDiagnosticsGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimInAsserts"),
        ("HUAWEI-PIM-STD-MIB", "hwPimOutAsserts"),
        ("HUAWEI-PIM-STD-MIB", "hwPimLastAssertInterface"),
        ("HUAWEI-PIM-STD-MIB", "hwPimLastAssertGroupAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimLastAssertGroupAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimLastAssertSourceAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimLastAssertSourceAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborLossNotificationPeriod"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborLossCount"))
)
if mibBuilder.loadTexts:
    hwPimDiagnosticsGroup.setStatus("current")

hwPimDmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 14)
)
hwPimDmGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimRefreshInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfacePruneLimitInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceGraftRetryInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceSrPriorityEnabled"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborSrCapable"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGUpstreamPruneState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGUpstreamPruneLimitTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGOriginatorState"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGSourceActiveTimer"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGStateRefreshTimer"))
)
if mibBuilder.loadTexts:
    hwPimDmGroup.setStatus("current")

hwPimDeviceStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 15)
)
hwPimDeviceStorageGroup.setObjects(
    ("HUAWEI-PIM-STD-MIB", "hwPimDeviceConfigStorageType")
)
if mibBuilder.loadTexts:
    hwPimDeviceStorageGroup.setStatus("current")


# Notification objects

hwPimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 1)
)
hwPimNeighborLoss.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNeighborUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborIfName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborNotificationReason"))
)
if mibBuilder.loadTexts:
    hwPimNeighborLoss.setStatus(
        "current"
    )

hwPimInvalidRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 2)
)
hwPimInvalidRegister.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterOrigin"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegisterRp"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimInvalidRegister.setStatus(
        "current"
    )

hwPimInvalidJoinPrune = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 3)
)
hwPimInvalidJoinPrune.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneOrigin"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPruneRp"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborUpTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborIfName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimInvalidJoinPrune.setStatus(
        "current"
    )

hwPimRpMappingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 4)
)
hwPimRpMappingChange.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPimMode"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGroupMappingPrecedence"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimRpMappingChange.setStatus(
        "current"
    )

hwPimInterfaceElection = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 5)
)
hwPimInterfaceElection.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimInterfaceAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceAddress"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimInterfaceElection.setStatus(
        "current"
    )

hwPimNeighborAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 6)
)
hwPimNeighborAdd.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNeighborExpiryTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimNeighborAdd.setStatus(
        "current"
    )

hwPimGRStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 7)
)
hwPimGRStart.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGRStartTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGRInterval"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"))
)
if mibBuilder.loadTexts:
    hwPimGRStart.setStatus(
        "obsolete"
    )

hwPimGREnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 8)
)
hwPimGREnd.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimGREndTime"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"))
)
if mibBuilder.loadTexts:
    hwPimGREnd.setStatus(
        "obsolete"
    )

hwPimMrtLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 9)
)
hwPimMrtLimit.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitSource"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimMrtLimit.setStatus(
        "current"
    )

hwPimNeighborUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 10)
)
hwPimNeighborUnavailable.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNeighborIfName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborNotificationReason"))
)
if mibBuilder.loadTexts:
    hwPimNeighborUnavailable.setStatus(
        "current"
    )

hwPimNeighborUnavailableClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 11)
)
hwPimNeighborUnavailableClear.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNeighborIfName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborNotificationReason"))
)
if mibBuilder.loadTexts:
    hwPimNeighborUnavailableClear.setStatus(
        "current"
    )

hwPimMrtLimitClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 12)
)
hwPimMrtLimitClear.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitSource"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitGroup"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceID"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimMrtLimitClear.setStatus(
        "current"
    )

hwPimStarGThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 13)
)
hwPimStarGThresholdExceed.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGTotalCount"))
)
if mibBuilder.loadTexts:
    hwPimStarGThresholdExceed.setStatus(
        "current"
    )

hwPimStarGThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 14)
)
hwPimStarGThresholdExceedClear.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGTotalCount"))
)
if mibBuilder.loadTexts:
    hwPimStarGThresholdExceedClear.setStatus(
        "current"
    )

hwPimStarGExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 15)
)
hwPimStarGExceed.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationSrcAddr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationGrpAddr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGTotalCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimStarGExceed.setStatus(
        "current"
    )

hwPimStarGExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 16)
)
hwPimStarGExceedClear.setObjects(
    ("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType")
)
if mibBuilder.loadTexts:
    hwPimStarGExceedClear.setStatus(
        "current"
    )

hwPimSGThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 17)
)
hwPimSGThresholdExceed.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwPimSGThresholdExceed.setStatus(
        "current"
    )

hwPimSGThresholdExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 18)
)
hwPimSGThresholdExceedClear.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGCurrentCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGThreshold"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGTotalCount"))
)
if mibBuilder.loadTexts:
    hwPimSGThresholdExceedClear.setStatus(
        "current"
    )

hwPimSGExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 19)
)
hwPimSGExceed.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationSrcAddr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNotificationGrpAddr"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGTotalCount"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInstanceName"))
)
if mibBuilder.loadTexts:
    hwPimSGExceed.setStatus(
        "current"
    )

hwPimSGExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 0, 20)
)
hwPimSGExceedClear.setObjects(
    ("HUAWEI-PIM-STD-MIB", "hwPimNotificationAddressType")
)
if mibBuilder.loadTexts:
    hwPimSGExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwPimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 2)
)
hwPimNotificationGroup.setObjects(
    ("HUAWEI-PIM-STD-MIB", "hwPimNeighborLoss")
)
if mibBuilder.loadTexts:
    hwPimNotificationGroup.setStatus(
        "current"
    )

hwPimNetMgmtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 2, 12)
)
hwPimNetMgmtNotificationGroup.setObjects(
      *(("HUAWEI-PIM-STD-MIB", "hwPimInvalidRegister"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInvalidJoinPrune"),
        ("HUAWEI-PIM-STD-MIB", "hwPimRpMappingChange"),
        ("HUAWEI-PIM-STD-MIB", "hwPimInterfaceElection"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborAdd"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGRStart"),
        ("HUAWEI-PIM-STD-MIB", "hwPimGREnd"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimit"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborUnavailable"),
        ("HUAWEI-PIM-STD-MIB", "hwPimNeighborUnavailableClear"),
        ("HUAWEI-PIM-STD-MIB", "hwPimMrtLimitClear"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGThresholdExceed"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGThresholdExceedClear"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGExceed"),
        ("HUAWEI-PIM-STD-MIB", "hwPimStarGExceedClear"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGThresholdExceed"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGThresholdExceedClear"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGExceed"),
        ("HUAWEI-PIM-STD-MIB", "hwPimSGExceedClear"))
)
if mibBuilder.loadTexts:
    hwPimNetMgmtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwPimMibComplianceAsm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwPimMibComplianceAsm.setStatus(
        "current"
    )

hwPimMibComplianceBidir = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwPimMibComplianceBidir.setStatus(
        "current"
    )

hwPimMibComplianceSsm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwPimMibComplianceSsm.setStatus(
        "current"
    )

hwPimMibComplianceDm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 149, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwPimMibComplianceDm.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PIM-STD-MIB",
    **{"HWPimMode": HWPimMode,
       "HWPimGroupMappingOriginType": HWPimGroupMappingOriginType,
       "HWPimCtlMsgState": HWPimCtlMsgState,
       "hwMcast": hwMcast,
       "hwPimStdMib": hwPimStdMib,
       "hwPimNotifications": hwPimNotifications,
       "hwPimNeighborLoss": hwPimNeighborLoss,
       "hwPimInvalidRegister": hwPimInvalidRegister,
       "hwPimInvalidJoinPrune": hwPimInvalidJoinPrune,
       "hwPimRpMappingChange": hwPimRpMappingChange,
       "hwPimInterfaceElection": hwPimInterfaceElection,
       "hwPimNeighborAdd": hwPimNeighborAdd,
       "hwPimGRStart": hwPimGRStart,
       "hwPimGREnd": hwPimGREnd,
       "hwPimMrtLimit": hwPimMrtLimit,
       "hwPimNeighborUnavailable": hwPimNeighborUnavailable,
       "hwPimNeighborUnavailableClear": hwPimNeighborUnavailableClear,
       "hwPimMrtLimitClear": hwPimMrtLimitClear,
       "hwPimStarGThresholdExceed": hwPimStarGThresholdExceed,
       "hwPimStarGThresholdExceedClear": hwPimStarGThresholdExceedClear,
       "hwPimStarGExceed": hwPimStarGExceed,
       "hwPimStarGExceedClear": hwPimStarGExceedClear,
       "hwPimSGThresholdExceed": hwPimSGThresholdExceed,
       "hwPimSGThresholdExceedClear": hwPimSGThresholdExceedClear,
       "hwPimSGExceed": hwPimSGExceed,
       "hwPimSGExceedClear": hwPimSGExceedClear,
       "hwPim": hwPim,
       "hwPimInterfaceTable": hwPimInterfaceTable,
       "hwPimInterfaceEntry": hwPimInterfaceEntry,
       "hwPimInterfaceIfIndex": hwPimInterfaceIfIndex,
       "hwPimInterfaceIpVersion": hwPimInterfaceIpVersion,
       "hwPimInterfaceAddressType": hwPimInterfaceAddressType,
       "hwPimInterfaceAddress": hwPimInterfaceAddress,
       "hwPimInterfaceGenerationIdValue": hwPimInterfaceGenerationIdValue,
       "hwPimInterfaceDr": hwPimInterfaceDr,
       "hwPimInterfaceDrPriority": hwPimInterfaceDrPriority,
       "hwPimInterfaceDrPriorityEnabled": hwPimInterfaceDrPriorityEnabled,
       "hwPimInterfaceHelloInterval": hwPimInterfaceHelloInterval,
       "hwPimInterfaceTrigHelloInterval": hwPimInterfaceTrigHelloInterval,
       "hwPimInterfaceHelloHoldtime": hwPimInterfaceHelloHoldtime,
       "hwPimInterfaceJoinPruneInterval": hwPimInterfaceJoinPruneInterval,
       "hwPimInterfaceJoinPruneHoldtime": hwPimInterfaceJoinPruneHoldtime,
       "hwPimInterfaceDfElectionRobustness": hwPimInterfaceDfElectionRobustness,
       "hwPimInterfaceLanDelayEnabled": hwPimInterfaceLanDelayEnabled,
       "hwPimInterfacePropagationDelay": hwPimInterfacePropagationDelay,
       "hwPimInterfaceOverrideInterval": hwPimInterfaceOverrideInterval,
       "hwPimInterfaceEffectPropagDelay": hwPimInterfaceEffectPropagDelay,
       "hwPimInterfaceEffectOverrideIvl": hwPimInterfaceEffectOverrideIvl,
       "hwPimInterfaceSuppressionEnabled": hwPimInterfaceSuppressionEnabled,
       "hwPimInterfaceBidirCapable": hwPimInterfaceBidirCapable,
       "hwPimInterfaceDomainBorder": hwPimInterfaceDomainBorder,
       "hwPimInterfaceStubInterface": hwPimInterfaceStubInterface,
       "hwPimInterfacePruneLimitInterval": hwPimInterfacePruneLimitInterval,
       "hwPimInterfaceGraftRetryInterval": hwPimInterfaceGraftRetryInterval,
       "hwPimInterfaceSrPriorityEnabled": hwPimInterfaceSrPriorityEnabled,
       "hwPimInterfaceStatus": hwPimInterfaceStatus,
       "hwPimInterfaceStorageType": hwPimInterfaceStorageType,
       "hwPimInterfaceName": hwPimInterfaceName,
       "hwPimNeighborTable": hwPimNeighborTable,
       "hwPimNeighborEntry": hwPimNeighborEntry,
       "hwPimNeighborIfIndex": hwPimNeighborIfIndex,
       "hwPimNeighborAddressType": hwPimNeighborAddressType,
       "hwPimNeighborAddress": hwPimNeighborAddress,
       "hwPimNeighborGenerationIdPresent": hwPimNeighborGenerationIdPresent,
       "hwPimNeighborGenerationIdValue": hwPimNeighborGenerationIdValue,
       "hwPimNeighborUpTime": hwPimNeighborUpTime,
       "hwPimNeighborExpiryTime": hwPimNeighborExpiryTime,
       "hwPimNeighborDrPriorityPresent": hwPimNeighborDrPriorityPresent,
       "hwPimNeighborDrPriority": hwPimNeighborDrPriority,
       "hwPimNeighborLanPruneDelayPresent": hwPimNeighborLanPruneDelayPresent,
       "hwPimNeighborTBit": hwPimNeighborTBit,
       "hwPimNeighborPropagationDelay": hwPimNeighborPropagationDelay,
       "hwPimNeighborOverrideInterval": hwPimNeighborOverrideInterval,
       "hwPimNeighborBidirCapable": hwPimNeighborBidirCapable,
       "hwPimNeighborSrCapable": hwPimNeighborSrCapable,
       "hwPimNeighborIfName": hwPimNeighborIfName,
       "hwPimNbrSecAddressTable": hwPimNbrSecAddressTable,
       "hwPimNbrSecAddressEntry": hwPimNbrSecAddressEntry,
       "hwPimNbrSecAddressIfIndex": hwPimNbrSecAddressIfIndex,
       "hwPimNbrSecAddressType": hwPimNbrSecAddressType,
       "hwPimNbrSecAddressPrimary": hwPimNbrSecAddressPrimary,
       "hwPimNbrSecAddress": hwPimNbrSecAddress,
       "hwPimStarGTable": hwPimStarGTable,
       "hwPimStarGEntry": hwPimStarGEntry,
       "hwPimStarGAddressType": hwPimStarGAddressType,
       "hwPimStarGGrpAddress": hwPimStarGGrpAddress,
       "hwPimStarGUpTime": hwPimStarGUpTime,
       "hwPimStarGPimMode": hwPimStarGPimMode,
       "hwPimStarGRpAddressType": hwPimStarGRpAddressType,
       "hwPimStarGRpAddress": hwPimStarGRpAddress,
       "hwPimStarGPimModeOrigin": hwPimStarGPimModeOrigin,
       "hwPimStarGRpIsLocal": hwPimStarGRpIsLocal,
       "hwPimStarGUpstreamJoinState": hwPimStarGUpstreamJoinState,
       "hwPimStarGUpstreamJoinTimer": hwPimStarGUpstreamJoinTimer,
       "hwPimStarGUpstreamNeighborType": hwPimStarGUpstreamNeighborType,
       "hwPimStarGUpstreamNeighbor": hwPimStarGUpstreamNeighbor,
       "hwPimStarGRpfIfIndex": hwPimStarGRpfIfIndex,
       "hwPimStarGRpfNextHopType": hwPimStarGRpfNextHopType,
       "hwPimStarGRpfNextHop": hwPimStarGRpfNextHop,
       "hwPimStarGRpfRouteProtocol": hwPimStarGRpfRouteProtocol,
       "hwPimStarGRpfRouteAddress": hwPimStarGRpfRouteAddress,
       "hwPimStarGRpfRoutePrefixLength": hwPimStarGRpfRoutePrefixLength,
       "hwPimStarGRpfRouteMetricPref": hwPimStarGRpfRouteMetricPref,
       "hwPimStarGRpfRouteMetric": hwPimStarGRpfRouteMetric,
       "hwPimStarGITable": hwPimStarGITable,
       "hwPimStarGIEntry": hwPimStarGIEntry,
       "hwPimStarGIIfIndex": hwPimStarGIIfIndex,
       "hwPimStarGIUpTime": hwPimStarGIUpTime,
       "hwPimStarGILocalMembership": hwPimStarGILocalMembership,
       "hwPimStarGIJoinPruneState": hwPimStarGIJoinPruneState,
       "hwPimStarGIPrunePendingTimer": hwPimStarGIPrunePendingTimer,
       "hwPimStarGIJoinExpiryTimer": hwPimStarGIJoinExpiryTimer,
       "hwPimStarGIAssertState": hwPimStarGIAssertState,
       "hwPimStarGIAssertTimer": hwPimStarGIAssertTimer,
       "hwPimStarGIAssertWinnerAddressType": hwPimStarGIAssertWinnerAddressType,
       "hwPimStarGIAssertWinnerAddress": hwPimStarGIAssertWinnerAddress,
       "hwPimStarGIAssertWinnerMetricPref": hwPimStarGIAssertWinnerMetricPref,
       "hwPimStarGIAssertWinnerMetric": hwPimStarGIAssertWinnerMetric,
       "hwPimSGTable": hwPimSGTable,
       "hwPimSGEntry": hwPimSGEntry,
       "hwPimSGAddressType": hwPimSGAddressType,
       "hwPimSGGrpAddress": hwPimSGGrpAddress,
       "hwPimSGSrcAddress": hwPimSGSrcAddress,
       "hwPimSGUpTime": hwPimSGUpTime,
       "hwPimSGPimMode": hwPimSGPimMode,
       "hwPimSGUpstreamJoinState": hwPimSGUpstreamJoinState,
       "hwPimSGUpstreamJoinTimer": hwPimSGUpstreamJoinTimer,
       "hwPimSGUpstreamNeighbor": hwPimSGUpstreamNeighbor,
       "hwPimSGRpfIfIndex": hwPimSGRpfIfIndex,
       "hwPimSGRpfNextHopType": hwPimSGRpfNextHopType,
       "hwPimSGRpfNextHop": hwPimSGRpfNextHop,
       "hwPimSGRpfRouteProtocol": hwPimSGRpfRouteProtocol,
       "hwPimSGRpfRouteAddress": hwPimSGRpfRouteAddress,
       "hwPimSGRpfRoutePrefixLength": hwPimSGRpfRoutePrefixLength,
       "hwPimSGRpfRouteMetricPref": hwPimSGRpfRouteMetricPref,
       "hwPimSGRpfRouteMetric": hwPimSGRpfRouteMetric,
       "hwPimSGSptBit": hwPimSGSptBit,
       "hwPimSGKeepaliveTimer": hwPimSGKeepaliveTimer,
       "hwPimSGDrRegisterState": hwPimSGDrRegisterState,
       "hwPimSGDrRegisterStopTimer": hwPimSGDrRegisterStopTimer,
       "hwPimSGRpRegisterPmbrAddressType": hwPimSGRpRegisterPmbrAddressType,
       "hwPimSGRpRegisterPmbrAddress": hwPimSGRpRegisterPmbrAddress,
       "hwPimSGUpstreamPruneState": hwPimSGUpstreamPruneState,
       "hwPimSGUpstreamPruneLimitTimer": hwPimSGUpstreamPruneLimitTimer,
       "hwPimSGOriginatorState": hwPimSGOriginatorState,
       "hwPimSGSourceActiveTimer": hwPimSGSourceActiveTimer,
       "hwPimSGStateRefreshTimer": hwPimSGStateRefreshTimer,
       "hwPimSGITable": hwPimSGITable,
       "hwPimSGIEntry": hwPimSGIEntry,
       "hwPimSGIIfIndex": hwPimSGIIfIndex,
       "hwPimSGIUpTime": hwPimSGIUpTime,
       "hwPimSGILocalMembership": hwPimSGILocalMembership,
       "hwPimSGIJoinPruneState": hwPimSGIJoinPruneState,
       "hwPimSGIPrunePendingTimer": hwPimSGIPrunePendingTimer,
       "hwPimSGIJoinExpiryTimer": hwPimSGIJoinExpiryTimer,
       "hwPimSGIAssertState": hwPimSGIAssertState,
       "hwPimSGIAssertTimer": hwPimSGIAssertTimer,
       "hwPimSGIAssertWinnerAddressType": hwPimSGIAssertWinnerAddressType,
       "hwPimSGIAssertWinnerAddress": hwPimSGIAssertWinnerAddress,
       "hwPimSGIAssertWinnerMetricPref": hwPimSGIAssertWinnerMetricPref,
       "hwPimSGIAssertWinnerMetric": hwPimSGIAssertWinnerMetric,
       "hwPimSGRptTable": hwPimSGRptTable,
       "hwPimSGRptEntry": hwPimSGRptEntry,
       "hwPimSGRptSrcAddress": hwPimSGRptSrcAddress,
       "hwPimSGRptUpTime": hwPimSGRptUpTime,
       "hwPimSGRptUpstreamPruneState": hwPimSGRptUpstreamPruneState,
       "hwPimSGRptUpstreamOverrideTimer": hwPimSGRptUpstreamOverrideTimer,
       "hwPimSGRptITable": hwPimSGRptITable,
       "hwPimSGRptIEntry": hwPimSGRptIEntry,
       "hwPimSGRptIIfIndex": hwPimSGRptIIfIndex,
       "hwPimSGRptIUpTime": hwPimSGRptIUpTime,
       "hwPimSGRptILocalMembership": hwPimSGRptILocalMembership,
       "hwPimSGRptIJoinPruneState": hwPimSGRptIJoinPruneState,
       "hwPimSGRptIPrunePendingTimer": hwPimSGRptIPrunePendingTimer,
       "hwPimSGRptIPruneExpiryTimer": hwPimSGRptIPruneExpiryTimer,
       "hwPimGroupMappingTable": hwPimGroupMappingTable,
       "hwPimGroupMappingEntry": hwPimGroupMappingEntry,
       "hwPimGroupMappingOrigin": hwPimGroupMappingOrigin,
       "hwPimGroupMappingAddressType": hwPimGroupMappingAddressType,
       "hwPimGroupMappingGrpAddress": hwPimGroupMappingGrpAddress,
       "hwPimGroupMappingGrpPrefixLength": hwPimGroupMappingGrpPrefixLength,
       "hwPimGroupMappingRpAddressType": hwPimGroupMappingRpAddressType,
       "hwPimGroupMappingRpAddress": hwPimGroupMappingRpAddress,
       "hwPimGroupMappingPimMode": hwPimGroupMappingPimMode,
       "hwPimGroupMappingPrecedence": hwPimGroupMappingPrecedence,
       "hwPimKeepalivePeriod": hwPimKeepalivePeriod,
       "hwPimRegisterSuppressionTime": hwPimRegisterSuppressionTime,
       "hwPimStarGEntries": hwPimStarGEntries,
       "hwPimStarGIEntries": hwPimStarGIEntries,
       "hwPimSGEntries": hwPimSGEntries,
       "hwPimSGIEntries": hwPimSGIEntries,
       "hwPimSGRptEntries": hwPimSGRptEntries,
       "hwPimSGRptIEntries": hwPimSGRptIEntries,
       "hwPimOutAsserts": hwPimOutAsserts,
       "hwPimInAsserts": hwPimInAsserts,
       "hwPimLastAssertInterface": hwPimLastAssertInterface,
       "hwPimLastAssertGroupAddressType": hwPimLastAssertGroupAddressType,
       "hwPimLastAssertGroupAddress": hwPimLastAssertGroupAddress,
       "hwPimLastAssertSourceAddressType": hwPimLastAssertSourceAddressType,
       "hwPimLastAssertSourceAddress": hwPimLastAssertSourceAddress,
       "hwPimNeighborLossNotificationPeriod": hwPimNeighborLossNotificationPeriod,
       "hwPimNeighborLossCount": hwPimNeighborLossCount,
       "hwPimInvalidRegisterNotificationPeriod": hwPimInvalidRegisterNotificationPeriod,
       "hwPimInvalidRegisterMsgsRcvd": hwPimInvalidRegisterMsgsRcvd,
       "hwPimInvalidRegisterAddressType": hwPimInvalidRegisterAddressType,
       "hwPimInvalidRegisterOrigin": hwPimInvalidRegisterOrigin,
       "hwPimInvalidRegisterGroup": hwPimInvalidRegisterGroup,
       "hwPimInvalidRegisterRp": hwPimInvalidRegisterRp,
       "hwPimInvalidJoinPruneNotificationPeriod": hwPimInvalidJoinPruneNotificationPeriod,
       "hwPimInvalidJoinPruneMsgsRcvd": hwPimInvalidJoinPruneMsgsRcvd,
       "hwPimInvalidJoinPruneAddressType": hwPimInvalidJoinPruneAddressType,
       "hwPimInvalidJoinPruneOrigin": hwPimInvalidJoinPruneOrigin,
       "hwPimInvalidJoinPruneGroup": hwPimInvalidJoinPruneGroup,
       "hwPimInvalidJoinPruneRp": hwPimInvalidJoinPruneRp,
       "hwPimRpMappingNotificationPeriod": hwPimRpMappingNotificationPeriod,
       "hwPimRpMappingChangeCount": hwPimRpMappingChangeCount,
       "hwPimInterfaceElectionNotificationPeriod": hwPimInterfaceElectionNotificationPeriod,
       "hwPimInterfaceElectionWinCount": hwPimInterfaceElectionWinCount,
       "hwPimRefreshInterval": hwPimRefreshInterval,
       "hwPimDeviceConfigStorageType": hwPimDeviceConfigStorageType,
       "hwPimNeighborAddCount": hwPimNeighborAddCount,
       "hwPimNeighborAddNotificationPeriod": hwPimNeighborAddNotificationPeriod,
       "hwPimGRStartTime": hwPimGRStartTime,
       "hwPimGRInterval": hwPimGRInterval,
       "hwPimGREndTime": hwPimGREndTime,
       "hwPimMrtLimitAddressType": hwPimMrtLimitAddressType,
       "hwPimMrtLimitSource": hwPimMrtLimitSource,
       "hwPimMrtLimitGroup": hwPimMrtLimitGroup,
       "hwPimInstanceID": hwPimInstanceID,
       "hwPimInterfaceCtlMsgCountTable": hwPimInterfaceCtlMsgCountTable,
       "hwPimInterfaceCtlMsgCountEntry": hwPimInterfaceCtlMsgCountEntry,
       "hwPimInterfaceCtlMsgCountIfIndex": hwPimInterfaceCtlMsgCountIfIndex,
       "hwPimInterfaceCtlMsgCountIpVersion": hwPimInterfaceCtlMsgCountIpVersion,
       "hwPimInterfaceCtlMsgCountMsgState": hwPimInterfaceCtlMsgCountMsgState,
       "hwPimInterfaceCtlMsgCountAssert": hwPimInterfaceCtlMsgCountAssert,
       "hwPimInterfaceCtlMsgCountHello": hwPimInterfaceCtlMsgCountHello,
       "hwPimInterfaceCtlMsgCountJoinPrune": hwPimInterfaceCtlMsgCountJoinPrune,
       "hwPimInterfaceCtlMsgCountBsr": hwPimInterfaceCtlMsgCountBsr,
       "hwPimGlobalCtlMsgCountTable": hwPimGlobalCtlMsgCountTable,
       "hwPimGlobalCtlMsgCountEntry": hwPimGlobalCtlMsgCountEntry,
       "hwPimGlobalCtlMsgCountIpVersion": hwPimGlobalCtlMsgCountIpVersion,
       "hwPimGlobalCtlMsgCountMsgState": hwPimGlobalCtlMsgCountMsgState,
       "hwPimGlobalCtlMsgCountRegister": hwPimGlobalCtlMsgCountRegister,
       "hwPimGlobalCtlMsgCountRegisterStop": hwPimGlobalCtlMsgCountRegisterStop,
       "hwPimGlobalCtlMsgCountProbe": hwPimGlobalCtlMsgCountProbe,
       "hwPimGlobalCtlMsgCountCrp": hwPimGlobalCtlMsgCountCrp,
       "hwPimInstanceName": hwPimInstanceName,
       "hwPimNeighborNotificationReason": hwPimNeighborNotificationReason,
       "hwPimNotificationAddressType": hwPimNotificationAddressType,
       "hwPimStarGCurrentCount": hwPimStarGCurrentCount,
       "hwPimStarGTotalCount": hwPimStarGTotalCount,
       "hwPimStarGThreshold": hwPimStarGThreshold,
       "hwPimSGCurrentCount": hwPimSGCurrentCount,
       "hwPimSGTotalCount": hwPimSGTotalCount,
       "hwPimSGThreshold": hwPimSGThreshold,
       "hwPimNotificationSrcAddr": hwPimNotificationSrcAddr,
       "hwPimNotificationGrpAddr": hwPimNotificationGrpAddr,
       "hwPimMibConformance": hwPimMibConformance,
       "hwPimMibCompliances": hwPimMibCompliances,
       "hwPimMibComplianceAsm": hwPimMibComplianceAsm,
       "hwPimMibComplianceBidir": hwPimMibComplianceBidir,
       "hwPimMibComplianceSsm": hwPimMibComplianceSsm,
       "hwPimMibComplianceDm": hwPimMibComplianceDm,
       "hwPimMibGroups": hwPimMibGroups,
       "hwPimTopologyGroup": hwPimTopologyGroup,
       "hwPimNotificationGroup": hwPimNotificationGroup,
       "hwPimTuningParametersGroup": hwPimTuningParametersGroup,
       "hwPimRouterStatisticsGroup": hwPimRouterStatisticsGroup,
       "hwPimSsmGroup": hwPimSsmGroup,
       "hwPimRpConfigGroup": hwPimRpConfigGroup,
       "hwPimSmGroup": hwPimSmGroup,
       "hwPimBidirGroup": hwPimBidirGroup,
       "hwPimNetMgmtNotificationObjects": hwPimNetMgmtNotificationObjects,
       "hwPimNetMgmtNotificationGroup": hwPimNetMgmtNotificationGroup,
       "hwPimDiagnosticsGroup": hwPimDiagnosticsGroup,
       "hwPimDmGroup": hwPimDmGroup,
       "hwPimDeviceStorageGroup": hwPimDeviceStorageGroup}
)
