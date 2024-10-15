# SNMP MIB module (PIM-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PIM-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:44 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pimStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 157)
)
pimStdMIB.setRevisions(
        ("2007-11-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PimMode(Integer32, TextualConvention):
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



class PimGroupMappingOriginType(Integer32, TextualConvention):
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
        *(("autoRP", 5),
          ("bsr", 4),
          ("configRp", 2),
          ("configSsm", 3),
          ("embedded", 6),
          ("fixed", 1),
          ("other", 7))
    )



# MIB Managed Objects in the order of their OIDs

_PimNotifications_ObjectIdentity = ObjectIdentity
pimNotifications = _PimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 157, 0)
)
_Pim_ObjectIdentity = ObjectIdentity
pim = _Pim_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 157, 1)
)
_PimInterfaceTable_Object = MibTable
pimInterfaceTable = _PimInterfaceTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1)
)
if mibBuilder.loadTexts:
    pimInterfaceTable.setStatus("current")
_PimInterfaceEntry_Object = MibTableRow
pimInterfaceEntry = _PimInterfaceEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1)
)
pimInterfaceEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimInterfaceIfIndex"),
    (0, "PIM-STD-MIB", "pimInterfaceIPVersion"),
)
if mibBuilder.loadTexts:
    pimInterfaceEntry.setStatus("current")
_PimInterfaceIfIndex_Type = InterfaceIndex
_PimInterfaceIfIndex_Object = MibTableColumn
pimInterfaceIfIndex = _PimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 1),
    _PimInterfaceIfIndex_Type()
)
pimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimInterfaceIfIndex.setStatus("current")
_PimInterfaceIPVersion_Type = InetVersion
_PimInterfaceIPVersion_Object = MibTableColumn
pimInterfaceIPVersion = _PimInterfaceIPVersion_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 2),
    _PimInterfaceIPVersion_Type()
)
pimInterfaceIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimInterfaceIPVersion.setStatus("current")
_PimInterfaceAddressType_Type = InetAddressType
_PimInterfaceAddressType_Object = MibTableColumn
pimInterfaceAddressType = _PimInterfaceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 3),
    _PimInterfaceAddressType_Type()
)
pimInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceAddressType.setStatus("current")


class _PimInterfaceAddress_Type(InetAddress):
    """Custom type pimInterfaceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInterfaceAddress_Type.__name__ = "InetAddress"
_PimInterfaceAddress_Object = MibTableColumn
pimInterfaceAddress = _PimInterfaceAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 4),
    _PimInterfaceAddress_Type()
)
pimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceAddress.setStatus("current")
_PimInterfaceGenerationIDValue_Type = Unsigned32
_PimInterfaceGenerationIDValue_Object = MibTableColumn
pimInterfaceGenerationIDValue = _PimInterfaceGenerationIDValue_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 5),
    _PimInterfaceGenerationIDValue_Type()
)
pimInterfaceGenerationIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceGenerationIDValue.setStatus("current")


class _PimInterfaceDR_Type(InetAddress):
    """Custom type pimInterfaceDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInterfaceDR_Type.__name__ = "InetAddress"
_PimInterfaceDR_Object = MibTableColumn
pimInterfaceDR = _PimInterfaceDR_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 6),
    _PimInterfaceDR_Type()
)
pimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceDR.setStatus("current")


class _PimInterfaceDRPriority_Type(Unsigned32):
    """Custom type pimInterfaceDRPriority based on Unsigned32"""
    defaultValue = 1


_PimInterfaceDRPriority_Object = MibTableColumn
pimInterfaceDRPriority = _PimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 7),
    _PimInterfaceDRPriority_Type()
)
pimInterfaceDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceDRPriority.setStatus("current")
_PimInterfaceDRPriorityEnabled_Type = TruthValue
_PimInterfaceDRPriorityEnabled_Object = MibTableColumn
pimInterfaceDRPriorityEnabled = _PimInterfaceDRPriorityEnabled_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 8),
    _PimInterfaceDRPriorityEnabled_Type()
)
pimInterfaceDRPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceDRPriorityEnabled.setStatus("current")


class _PimInterfaceHelloInterval_Type(Unsigned32):
    """Custom type pimInterfaceHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_PimInterfaceHelloInterval_Type.__name__ = "Unsigned32"
_PimInterfaceHelloInterval_Object = MibTableColumn
pimInterfaceHelloInterval = _PimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 9),
    _PimInterfaceHelloInterval_Type()
)
pimInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceHelloInterval.setUnits("seconds")


class _PimInterfaceTrigHelloInterval_Type(Unsigned32):
    """Custom type pimInterfaceTrigHelloInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_PimInterfaceTrigHelloInterval_Type.__name__ = "Unsigned32"
_PimInterfaceTrigHelloInterval_Object = MibTableColumn
pimInterfaceTrigHelloInterval = _PimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 10),
    _PimInterfaceTrigHelloInterval_Type()
)
pimInterfaceTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceTrigHelloInterval.setUnits("seconds")


class _PimInterfaceHelloHoldtime_Type(Unsigned32):
    """Custom type pimInterfaceHelloHoldtime based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceHelloHoldtime_Type.__name__ = "Unsigned32"
_PimInterfaceHelloHoldtime_Object = MibTableColumn
pimInterfaceHelloHoldtime = _PimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 11),
    _PimInterfaceHelloHoldtime_Type()
)
pimInterfaceHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceHelloHoldtime.setUnits("seconds")


class _PimInterfaceJoinPruneInterval_Type(Unsigned32):
    """Custom type pimInterfaceJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_PimInterfaceJoinPruneInterval_Type.__name__ = "Unsigned32"
_PimInterfaceJoinPruneInterval_Object = MibTableColumn
pimInterfaceJoinPruneInterval = _PimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 12),
    _PimInterfaceJoinPruneInterval_Type()
)
pimInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneInterval.setUnits("seconds")


class _PimInterfaceJoinPruneHoldtime_Type(Unsigned32):
    """Custom type pimInterfaceJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceJoinPruneHoldtime_Type.__name__ = "Unsigned32"
_PimInterfaceJoinPruneHoldtime_Object = MibTableColumn
pimInterfaceJoinPruneHoldtime = _PimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 13),
    _PimInterfaceJoinPruneHoldtime_Type()
)
pimInterfaceJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _PimInterfaceDFElectionRobustness_Type(Unsigned32):
    """Custom type pimInterfaceDFElectionRobustness based on Unsigned32"""
    defaultValue = 3


_PimInterfaceDFElectionRobustness_Object = MibTableColumn
pimInterfaceDFElectionRobustness = _PimInterfaceDFElectionRobustness_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 14),
    _PimInterfaceDFElectionRobustness_Type()
)
pimInterfaceDFElectionRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceDFElectionRobustness.setStatus("current")
_PimInterfaceLanDelayEnabled_Type = TruthValue
_PimInterfaceLanDelayEnabled_Object = MibTableColumn
pimInterfaceLanDelayEnabled = _PimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 15),
    _PimInterfaceLanDelayEnabled_Type()
)
pimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceLanDelayEnabled.setStatus("current")


class _PimInterfacePropagationDelay_Type(Unsigned32):
    """Custom type pimInterfacePropagationDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PimInterfacePropagationDelay_Type.__name__ = "Unsigned32"
_PimInterfacePropagationDelay_Object = MibTableColumn
pimInterfacePropagationDelay = _PimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 16),
    _PimInterfacePropagationDelay_Type()
)
pimInterfacePropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfacePropagationDelay.setUnits("milliseconds")


class _PimInterfaceOverrideInterval_Type(Unsigned32):
    """Custom type pimInterfaceOverrideInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceOverrideInterval_Type.__name__ = "Unsigned32"
_PimInterfaceOverrideInterval_Object = MibTableColumn
pimInterfaceOverrideInterval = _PimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 17),
    _PimInterfaceOverrideInterval_Type()
)
pimInterfaceOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceOverrideInterval.setUnits("milliseconds")


class _PimInterfaceEffectPropagDelay_Type(Unsigned32):
    """Custom type pimInterfaceEffectPropagDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PimInterfaceEffectPropagDelay_Type.__name__ = "Unsigned32"
_PimInterfaceEffectPropagDelay_Object = MibTableColumn
pimInterfaceEffectPropagDelay = _PimInterfaceEffectPropagDelay_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 18),
    _PimInterfaceEffectPropagDelay_Type()
)
pimInterfaceEffectPropagDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceEffectPropagDelay.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceEffectPropagDelay.setUnits("milliseconds")


class _PimInterfaceEffectOverrideIvl_Type(Unsigned32):
    """Custom type pimInterfaceEffectOverrideIvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceEffectOverrideIvl_Type.__name__ = "Unsigned32"
_PimInterfaceEffectOverrideIvl_Object = MibTableColumn
pimInterfaceEffectOverrideIvl = _PimInterfaceEffectOverrideIvl_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 19),
    _PimInterfaceEffectOverrideIvl_Type()
)
pimInterfaceEffectOverrideIvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceEffectOverrideIvl.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceEffectOverrideIvl.setUnits("milliseconds")
_PimInterfaceSuppressionEnabled_Type = TruthValue
_PimInterfaceSuppressionEnabled_Object = MibTableColumn
pimInterfaceSuppressionEnabled = _PimInterfaceSuppressionEnabled_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 20),
    _PimInterfaceSuppressionEnabled_Type()
)
pimInterfaceSuppressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceSuppressionEnabled.setStatus("current")
_PimInterfaceBidirCapable_Type = TruthValue
_PimInterfaceBidirCapable_Object = MibTableColumn
pimInterfaceBidirCapable = _PimInterfaceBidirCapable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 21),
    _PimInterfaceBidirCapable_Type()
)
pimInterfaceBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceBidirCapable.setStatus("current")


class _PimInterfaceDomainBorder_Type(TruthValue):
    """Custom type pimInterfaceDomainBorder based on TruthValue"""


_PimInterfaceDomainBorder_Object = MibTableColumn
pimInterfaceDomainBorder = _PimInterfaceDomainBorder_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 22),
    _PimInterfaceDomainBorder_Type()
)
pimInterfaceDomainBorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceDomainBorder.setStatus("current")


class _PimInterfaceStubInterface_Type(TruthValue):
    """Custom type pimInterfaceStubInterface based on TruthValue"""


_PimInterfaceStubInterface_Object = MibTableColumn
pimInterfaceStubInterface = _PimInterfaceStubInterface_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 23),
    _PimInterfaceStubInterface_Type()
)
pimInterfaceStubInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceStubInterface.setStatus("current")


class _PimInterfacePruneLimitInterval_Type(Unsigned32):
    """Custom type pimInterfacePruneLimitInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfacePruneLimitInterval_Type.__name__ = "Unsigned32"
_PimInterfacePruneLimitInterval_Object = MibTableColumn
pimInterfacePruneLimitInterval = _PimInterfacePruneLimitInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 24),
    _PimInterfacePruneLimitInterval_Type()
)
pimInterfacePruneLimitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfacePruneLimitInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfacePruneLimitInterval.setUnits("seconds")


class _PimInterfaceGraftRetryInterval_Type(Unsigned32):
    """Custom type pimInterfaceGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceGraftRetryInterval_Type.__name__ = "Unsigned32"
_PimInterfaceGraftRetryInterval_Object = MibTableColumn
pimInterfaceGraftRetryInterval = _PimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 25),
    _PimInterfaceGraftRetryInterval_Type()
)
pimInterfaceGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceGraftRetryInterval.setUnits("seconds")
_PimInterfaceSRPriorityEnabled_Type = TruthValue
_PimInterfaceSRPriorityEnabled_Object = MibTableColumn
pimInterfaceSRPriorityEnabled = _PimInterfaceSRPriorityEnabled_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 26),
    _PimInterfaceSRPriorityEnabled_Type()
)
pimInterfaceSRPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceSRPriorityEnabled.setStatus("current")
_PimInterfaceStatus_Type = RowStatus
_PimInterfaceStatus_Object = MibTableColumn
pimInterfaceStatus = _PimInterfaceStatus_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 27),
    _PimInterfaceStatus_Type()
)
pimInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceStatus.setStatus("current")


class _PimInterfaceStorageType_Type(StorageType):
    """Custom type pimInterfaceStorageType based on StorageType"""


_PimInterfaceStorageType_Object = MibTableColumn
pimInterfaceStorageType = _PimInterfaceStorageType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 1, 1, 28),
    _PimInterfaceStorageType_Type()
)
pimInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimInterfaceStorageType.setStatus("current")
_PimNeighborTable_Object = MibTable
pimNeighborTable = _PimNeighborTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2)
)
if mibBuilder.loadTexts:
    pimNeighborTable.setStatus("current")
_PimNeighborEntry_Object = MibTableRow
pimNeighborEntry = _PimNeighborEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1)
)
pimNeighborEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimNeighborIfIndex"),
    (0, "PIM-STD-MIB", "pimNeighborAddressType"),
    (0, "PIM-STD-MIB", "pimNeighborAddress"),
)
if mibBuilder.loadTexts:
    pimNeighborEntry.setStatus("current")
_PimNeighborIfIndex_Type = InterfaceIndex
_PimNeighborIfIndex_Object = MibTableColumn
pimNeighborIfIndex = _PimNeighborIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 1),
    _PimNeighborIfIndex_Type()
)
pimNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborIfIndex.setStatus("current")
_PimNeighborAddressType_Type = InetAddressType
_PimNeighborAddressType_Object = MibTableColumn
pimNeighborAddressType = _PimNeighborAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 2),
    _PimNeighborAddressType_Type()
)
pimNeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborAddressType.setStatus("current")


class _PimNeighborAddress_Type(InetAddress):
    """Custom type pimNeighborAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimNeighborAddress_Type.__name__ = "InetAddress"
_PimNeighborAddress_Object = MibTableColumn
pimNeighborAddress = _PimNeighborAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 3),
    _PimNeighborAddress_Type()
)
pimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNeighborAddress.setStatus("current")
_PimNeighborGenerationIDPresent_Type = TruthValue
_PimNeighborGenerationIDPresent_Object = MibTableColumn
pimNeighborGenerationIDPresent = _PimNeighborGenerationIDPresent_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 4),
    _PimNeighborGenerationIDPresent_Type()
)
pimNeighborGenerationIDPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborGenerationIDPresent.setStatus("current")
_PimNeighborGenerationIDValue_Type = Unsigned32
_PimNeighborGenerationIDValue_Object = MibTableColumn
pimNeighborGenerationIDValue = _PimNeighborGenerationIDValue_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 5),
    _PimNeighborGenerationIDValue_Type()
)
pimNeighborGenerationIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborGenerationIDValue.setStatus("current")
_PimNeighborUpTime_Type = TimeTicks
_PimNeighborUpTime_Object = MibTableColumn
pimNeighborUpTime = _PimNeighborUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 6),
    _PimNeighborUpTime_Type()
)
pimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborUpTime.setStatus("current")
_PimNeighborExpiryTime_Type = TimeTicks
_PimNeighborExpiryTime_Object = MibTableColumn
pimNeighborExpiryTime = _PimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 7),
    _PimNeighborExpiryTime_Type()
)
pimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborExpiryTime.setStatus("current")
_PimNeighborDRPriorityPresent_Type = TruthValue
_PimNeighborDRPriorityPresent_Object = MibTableColumn
pimNeighborDRPriorityPresent = _PimNeighborDRPriorityPresent_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 8),
    _PimNeighborDRPriorityPresent_Type()
)
pimNeighborDRPriorityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborDRPriorityPresent.setStatus("current")
_PimNeighborDRPriority_Type = Unsigned32
_PimNeighborDRPriority_Object = MibTableColumn
pimNeighborDRPriority = _PimNeighborDRPriority_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 9),
    _PimNeighborDRPriority_Type()
)
pimNeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborDRPriority.setStatus("current")
_PimNeighborLanPruneDelayPresent_Type = TruthValue
_PimNeighborLanPruneDelayPresent_Object = MibTableColumn
pimNeighborLanPruneDelayPresent = _PimNeighborLanPruneDelayPresent_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 10),
    _PimNeighborLanPruneDelayPresent_Type()
)
pimNeighborLanPruneDelayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborLanPruneDelayPresent.setStatus("current")
_PimNeighborTBit_Type = TruthValue
_PimNeighborTBit_Object = MibTableColumn
pimNeighborTBit = _PimNeighborTBit_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 11),
    _PimNeighborTBit_Type()
)
pimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborTBit.setStatus("current")


class _PimNeighborPropagationDelay_Type(Unsigned32):
    """Custom type pimNeighborPropagationDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_PimNeighborPropagationDelay_Type.__name__ = "Unsigned32"
_PimNeighborPropagationDelay_Object = MibTableColumn
pimNeighborPropagationDelay = _PimNeighborPropagationDelay_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 12),
    _PimNeighborPropagationDelay_Type()
)
pimNeighborPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborPropagationDelay.setStatus("current")


class _PimNeighborOverrideInterval_Type(Unsigned32):
    """Custom type pimNeighborOverrideInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimNeighborOverrideInterval_Type.__name__ = "Unsigned32"
_PimNeighborOverrideInterval_Object = MibTableColumn
pimNeighborOverrideInterval = _PimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 13),
    _PimNeighborOverrideInterval_Type()
)
pimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborOverrideInterval.setStatus("current")
_PimNeighborBidirCapable_Type = TruthValue
_PimNeighborBidirCapable_Object = MibTableColumn
pimNeighborBidirCapable = _PimNeighborBidirCapable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 14),
    _PimNeighborBidirCapable_Type()
)
pimNeighborBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborBidirCapable.setStatus("current")
_PimNeighborSRCapable_Type = TruthValue
_PimNeighborSRCapable_Object = MibTableColumn
pimNeighborSRCapable = _PimNeighborSRCapable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 2, 1, 15),
    _PimNeighborSRCapable_Type()
)
pimNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborSRCapable.setStatus("current")
_PimNbrSecAddressTable_Object = MibTable
pimNbrSecAddressTable = _PimNbrSecAddressTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3)
)
if mibBuilder.loadTexts:
    pimNbrSecAddressTable.setStatus("current")
_PimNbrSecAddressEntry_Object = MibTableRow
pimNbrSecAddressEntry = _PimNbrSecAddressEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3, 1)
)
pimNbrSecAddressEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimNbrSecAddressIfIndex"),
    (0, "PIM-STD-MIB", "pimNbrSecAddressType"),
    (0, "PIM-STD-MIB", "pimNbrSecAddressPrimary"),
    (0, "PIM-STD-MIB", "pimNbrSecAddress"),
)
if mibBuilder.loadTexts:
    pimNbrSecAddressEntry.setStatus("current")
_PimNbrSecAddressIfIndex_Type = InterfaceIndex
_PimNbrSecAddressIfIndex_Object = MibTableColumn
pimNbrSecAddressIfIndex = _PimNbrSecAddressIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3, 1, 1),
    _PimNbrSecAddressIfIndex_Type()
)
pimNbrSecAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNbrSecAddressIfIndex.setStatus("current")
_PimNbrSecAddressType_Type = InetAddressType
_PimNbrSecAddressType_Object = MibTableColumn
pimNbrSecAddressType = _PimNbrSecAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3, 1, 2),
    _PimNbrSecAddressType_Type()
)
pimNbrSecAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNbrSecAddressType.setStatus("current")


class _PimNbrSecAddressPrimary_Type(InetAddress):
    """Custom type pimNbrSecAddressPrimary based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimNbrSecAddressPrimary_Type.__name__ = "InetAddress"
_PimNbrSecAddressPrimary_Object = MibTableColumn
pimNbrSecAddressPrimary = _PimNbrSecAddressPrimary_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3, 1, 3),
    _PimNbrSecAddressPrimary_Type()
)
pimNbrSecAddressPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimNbrSecAddressPrimary.setStatus("current")


class _PimNbrSecAddress_Type(InetAddress):
    """Custom type pimNbrSecAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimNbrSecAddress_Type.__name__ = "InetAddress"
_PimNbrSecAddress_Object = MibTableColumn
pimNbrSecAddress = _PimNbrSecAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 3, 1, 4),
    _PimNbrSecAddress_Type()
)
pimNbrSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNbrSecAddress.setStatus("current")
_PimStarGTable_Object = MibTable
pimStarGTable = _PimStarGTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4)
)
if mibBuilder.loadTexts:
    pimStarGTable.setStatus("current")
_PimStarGEntry_Object = MibTableRow
pimStarGEntry = _PimStarGEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1)
)
pimStarGEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimStarGAddressType"),
    (0, "PIM-STD-MIB", "pimStarGGrpAddress"),
)
if mibBuilder.loadTexts:
    pimStarGEntry.setStatus("current")
_PimStarGAddressType_Type = InetAddressType
_PimStarGAddressType_Object = MibTableColumn
pimStarGAddressType = _PimStarGAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 1),
    _PimStarGAddressType_Type()
)
pimStarGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStarGAddressType.setStatus("current")


class _PimStarGGrpAddress_Type(InetAddress):
    """Custom type pimStarGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGGrpAddress_Type.__name__ = "InetAddress"
_PimStarGGrpAddress_Object = MibTableColumn
pimStarGGrpAddress = _PimStarGGrpAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 2),
    _PimStarGGrpAddress_Type()
)
pimStarGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStarGGrpAddress.setStatus("current")
_PimStarGUpTime_Type = TimeTicks
_PimStarGUpTime_Object = MibTableColumn
pimStarGUpTime = _PimStarGUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 3),
    _PimStarGUpTime_Type()
)
pimStarGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGUpTime.setStatus("current")


class _PimStarGPimMode_Type(PimMode):
    """Custom type pimStarGPimMode based on PimMode"""
    subtypeSpec = PimMode.subtypeSpec
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


_PimStarGPimMode_Type.__name__ = "PimMode"
_PimStarGPimMode_Object = MibTableColumn
pimStarGPimMode = _PimStarGPimMode_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 4),
    _PimStarGPimMode_Type()
)
pimStarGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGPimMode.setStatus("current")
_PimStarGRPAddressType_Type = InetAddressType
_PimStarGRPAddressType_Object = MibTableColumn
pimStarGRPAddressType = _PimStarGRPAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 5),
    _PimStarGRPAddressType_Type()
)
pimStarGRPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPAddressType.setStatus("current")


class _PimStarGRPAddress_Type(InetAddress):
    """Custom type pimStarGRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGRPAddress_Type.__name__ = "InetAddress"
_PimStarGRPAddress_Object = MibTableColumn
pimStarGRPAddress = _PimStarGRPAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 6),
    _PimStarGRPAddress_Type()
)
pimStarGRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPAddress.setStatus("current")
_PimStarGPimModeOrigin_Type = PimGroupMappingOriginType
_PimStarGPimModeOrigin_Object = MibTableColumn
pimStarGPimModeOrigin = _PimStarGPimModeOrigin_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 7),
    _PimStarGPimModeOrigin_Type()
)
pimStarGPimModeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGPimModeOrigin.setStatus("current")
_PimStarGRPIsLocal_Type = TruthValue
_PimStarGRPIsLocal_Object = MibTableColumn
pimStarGRPIsLocal = _PimStarGRPIsLocal_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 8),
    _PimStarGRPIsLocal_Type()
)
pimStarGRPIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPIsLocal.setStatus("current")


class _PimStarGUpstreamJoinState_Type(Integer32):
    """Custom type pimStarGUpstreamJoinState based on Integer32"""
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


_PimStarGUpstreamJoinState_Type.__name__ = "Integer32"
_PimStarGUpstreamJoinState_Object = MibTableColumn
pimStarGUpstreamJoinState = _PimStarGUpstreamJoinState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 9),
    _PimStarGUpstreamJoinState_Type()
)
pimStarGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGUpstreamJoinState.setStatus("current")
_PimStarGUpstreamJoinTimer_Type = TimeTicks
_PimStarGUpstreamJoinTimer_Object = MibTableColumn
pimStarGUpstreamJoinTimer = _PimStarGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 10),
    _PimStarGUpstreamJoinTimer_Type()
)
pimStarGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGUpstreamJoinTimer.setStatus("current")
_PimStarGUpstreamNeighborType_Type = InetAddressType
_PimStarGUpstreamNeighborType_Object = MibTableColumn
pimStarGUpstreamNeighborType = _PimStarGUpstreamNeighborType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 11),
    _PimStarGUpstreamNeighborType_Type()
)
pimStarGUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGUpstreamNeighborType.setStatus("current")


class _PimStarGUpstreamNeighbor_Type(InetAddress):
    """Custom type pimStarGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGUpstreamNeighbor_Type.__name__ = "InetAddress"
_PimStarGUpstreamNeighbor_Object = MibTableColumn
pimStarGUpstreamNeighbor = _PimStarGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 12),
    _PimStarGUpstreamNeighbor_Type()
)
pimStarGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGUpstreamNeighbor.setStatus("current")
_PimStarGRPFIfIndex_Type = InterfaceIndexOrZero
_PimStarGRPFIfIndex_Object = MibTableColumn
pimStarGRPFIfIndex = _PimStarGRPFIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 13),
    _PimStarGRPFIfIndex_Type()
)
pimStarGRPFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFIfIndex.setStatus("current")
_PimStarGRPFNextHopType_Type = InetAddressType
_PimStarGRPFNextHopType_Object = MibTableColumn
pimStarGRPFNextHopType = _PimStarGRPFNextHopType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 14),
    _PimStarGRPFNextHopType_Type()
)
pimStarGRPFNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFNextHopType.setStatus("current")


class _PimStarGRPFNextHop_Type(InetAddress):
    """Custom type pimStarGRPFNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGRPFNextHop_Type.__name__ = "InetAddress"
_PimStarGRPFNextHop_Object = MibTableColumn
pimStarGRPFNextHop = _PimStarGRPFNextHop_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 15),
    _PimStarGRPFNextHop_Type()
)
pimStarGRPFNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFNextHop.setStatus("current")
_PimStarGRPFRouteProtocol_Type = IANAipRouteProtocol
_PimStarGRPFRouteProtocol_Object = MibTableColumn
pimStarGRPFRouteProtocol = _PimStarGRPFRouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 16),
    _PimStarGRPFRouteProtocol_Type()
)
pimStarGRPFRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFRouteProtocol.setStatus("current")


class _PimStarGRPFRouteAddress_Type(InetAddress):
    """Custom type pimStarGRPFRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGRPFRouteAddress_Type.__name__ = "InetAddress"
_PimStarGRPFRouteAddress_Object = MibTableColumn
pimStarGRPFRouteAddress = _PimStarGRPFRouteAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 17),
    _PimStarGRPFRouteAddress_Type()
)
pimStarGRPFRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFRouteAddress.setStatus("current")
_PimStarGRPFRoutePrefixLength_Type = InetAddressPrefixLength
_PimStarGRPFRoutePrefixLength_Object = MibTableColumn
pimStarGRPFRoutePrefixLength = _PimStarGRPFRoutePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 18),
    _PimStarGRPFRoutePrefixLength_Type()
)
pimStarGRPFRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFRoutePrefixLength.setStatus("current")


class _PimStarGRPFRouteMetricPref_Type(Unsigned32):
    """Custom type pimStarGRPFRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PimStarGRPFRouteMetricPref_Type.__name__ = "Unsigned32"
_PimStarGRPFRouteMetricPref_Object = MibTableColumn
pimStarGRPFRouteMetricPref = _PimStarGRPFRouteMetricPref_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 19),
    _PimStarGRPFRouteMetricPref_Type()
)
pimStarGRPFRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFRouteMetricPref.setStatus("current")
_PimStarGRPFRouteMetric_Type = Unsigned32
_PimStarGRPFRouteMetric_Object = MibTableColumn
pimStarGRPFRouteMetric = _PimStarGRPFRouteMetric_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 4, 1, 20),
    _PimStarGRPFRouteMetric_Type()
)
pimStarGRPFRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGRPFRouteMetric.setStatus("current")
_PimStarGITable_Object = MibTable
pimStarGITable = _PimStarGITable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5)
)
if mibBuilder.loadTexts:
    pimStarGITable.setStatus("current")
_PimStarGIEntry_Object = MibTableRow
pimStarGIEntry = _PimStarGIEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1)
)
pimStarGIEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimStarGAddressType"),
    (0, "PIM-STD-MIB", "pimStarGGrpAddress"),
    (0, "PIM-STD-MIB", "pimStarGIIfIndex"),
)
if mibBuilder.loadTexts:
    pimStarGIEntry.setStatus("current")
_PimStarGIIfIndex_Type = InterfaceIndex
_PimStarGIIfIndex_Object = MibTableColumn
pimStarGIIfIndex = _PimStarGIIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 1),
    _PimStarGIIfIndex_Type()
)
pimStarGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStarGIIfIndex.setStatus("current")
_PimStarGIUpTime_Type = TimeTicks
_PimStarGIUpTime_Object = MibTableColumn
pimStarGIUpTime = _PimStarGIUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 2),
    _PimStarGIUpTime_Type()
)
pimStarGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIUpTime.setStatus("current")
_PimStarGILocalMembership_Type = TruthValue
_PimStarGILocalMembership_Object = MibTableColumn
pimStarGILocalMembership = _PimStarGILocalMembership_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 3),
    _PimStarGILocalMembership_Type()
)
pimStarGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGILocalMembership.setStatus("current")


class _PimStarGIJoinPruneState_Type(Integer32):
    """Custom type pimStarGIJoinPruneState based on Integer32"""
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


_PimStarGIJoinPruneState_Type.__name__ = "Integer32"
_PimStarGIJoinPruneState_Object = MibTableColumn
pimStarGIJoinPruneState = _PimStarGIJoinPruneState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 4),
    _PimStarGIJoinPruneState_Type()
)
pimStarGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIJoinPruneState.setStatus("current")
_PimStarGIPrunePendingTimer_Type = TimeTicks
_PimStarGIPrunePendingTimer_Object = MibTableColumn
pimStarGIPrunePendingTimer = _PimStarGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 5),
    _PimStarGIPrunePendingTimer_Type()
)
pimStarGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIPrunePendingTimer.setStatus("current")
_PimStarGIJoinExpiryTimer_Type = TimeTicks
_PimStarGIJoinExpiryTimer_Object = MibTableColumn
pimStarGIJoinExpiryTimer = _PimStarGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 6),
    _PimStarGIJoinExpiryTimer_Type()
)
pimStarGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIJoinExpiryTimer.setStatus("current")


class _PimStarGIAssertState_Type(Integer32):
    """Custom type pimStarGIAssertState based on Integer32"""
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


_PimStarGIAssertState_Type.__name__ = "Integer32"
_PimStarGIAssertState_Object = MibTableColumn
pimStarGIAssertState = _PimStarGIAssertState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 7),
    _PimStarGIAssertState_Type()
)
pimStarGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertState.setStatus("current")
_PimStarGIAssertTimer_Type = TimeTicks
_PimStarGIAssertTimer_Object = MibTableColumn
pimStarGIAssertTimer = _PimStarGIAssertTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 8),
    _PimStarGIAssertTimer_Type()
)
pimStarGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertTimer.setStatus("current")
_PimStarGIAssertWinnerAddressType_Type = InetAddressType
_PimStarGIAssertWinnerAddressType_Object = MibTableColumn
pimStarGIAssertWinnerAddressType = _PimStarGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 9),
    _PimStarGIAssertWinnerAddressType_Type()
)
pimStarGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertWinnerAddressType.setStatus("current")


class _PimStarGIAssertWinnerAddress_Type(InetAddress):
    """Custom type pimStarGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStarGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_PimStarGIAssertWinnerAddress_Object = MibTableColumn
pimStarGIAssertWinnerAddress = _PimStarGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 10),
    _PimStarGIAssertWinnerAddress_Type()
)
pimStarGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertWinnerAddress.setStatus("current")


class _PimStarGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type pimStarGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PimStarGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_PimStarGIAssertWinnerMetricPref_Object = MibTableColumn
pimStarGIAssertWinnerMetricPref = _PimStarGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 11),
    _PimStarGIAssertWinnerMetricPref_Type()
)
pimStarGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertWinnerMetricPref.setStatus("current")
_PimStarGIAssertWinnerMetric_Type = Unsigned32
_PimStarGIAssertWinnerMetric_Object = MibTableColumn
pimStarGIAssertWinnerMetric = _PimStarGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 5, 1, 12),
    _PimStarGIAssertWinnerMetric_Type()
)
pimStarGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIAssertWinnerMetric.setStatus("current")
_PimSGTable_Object = MibTable
pimSGTable = _PimSGTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6)
)
if mibBuilder.loadTexts:
    pimSGTable.setStatus("current")
_PimSGEntry_Object = MibTableRow
pimSGEntry = _PimSGEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1)
)
pimSGEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimSGAddressType"),
    (0, "PIM-STD-MIB", "pimSGGrpAddress"),
    (0, "PIM-STD-MIB", "pimSGSrcAddress"),
)
if mibBuilder.loadTexts:
    pimSGEntry.setStatus("current")
_PimSGAddressType_Type = InetAddressType
_PimSGAddressType_Object = MibTableColumn
pimSGAddressType = _PimSGAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 1),
    _PimSGAddressType_Type()
)
pimSGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGAddressType.setStatus("current")


class _PimSGGrpAddress_Type(InetAddress):
    """Custom type pimSGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGGrpAddress_Type.__name__ = "InetAddress"
_PimSGGrpAddress_Object = MibTableColumn
pimSGGrpAddress = _PimSGGrpAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 2),
    _PimSGGrpAddress_Type()
)
pimSGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGGrpAddress.setStatus("current")


class _PimSGSrcAddress_Type(InetAddress):
    """Custom type pimSGSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGSrcAddress_Type.__name__ = "InetAddress"
_PimSGSrcAddress_Object = MibTableColumn
pimSGSrcAddress = _PimSGSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 3),
    _PimSGSrcAddress_Type()
)
pimSGSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGSrcAddress.setStatus("current")
_PimSGUpTime_Type = TimeTicks
_PimSGUpTime_Object = MibTableColumn
pimSGUpTime = _PimSGUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 4),
    _PimSGUpTime_Type()
)
pimSGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpTime.setStatus("current")


class _PimSGPimMode_Type(PimMode):
    """Custom type pimSGPimMode based on PimMode"""
    subtypeSpec = PimMode.subtypeSpec
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


_PimSGPimMode_Type.__name__ = "PimMode"
_PimSGPimMode_Object = MibTableColumn
pimSGPimMode = _PimSGPimMode_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 5),
    _PimSGPimMode_Type()
)
pimSGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGPimMode.setStatus("current")


class _PimSGUpstreamJoinState_Type(Integer32):
    """Custom type pimSGUpstreamJoinState based on Integer32"""
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


_PimSGUpstreamJoinState_Type.__name__ = "Integer32"
_PimSGUpstreamJoinState_Object = MibTableColumn
pimSGUpstreamJoinState = _PimSGUpstreamJoinState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 6),
    _PimSGUpstreamJoinState_Type()
)
pimSGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpstreamJoinState.setStatus("current")
_PimSGUpstreamJoinTimer_Type = TimeTicks
_PimSGUpstreamJoinTimer_Object = MibTableColumn
pimSGUpstreamJoinTimer = _PimSGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 7),
    _PimSGUpstreamJoinTimer_Type()
)
pimSGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpstreamJoinTimer.setStatus("current")


class _PimSGUpstreamNeighbor_Type(InetAddress):
    """Custom type pimSGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGUpstreamNeighbor_Type.__name__ = "InetAddress"
_PimSGUpstreamNeighbor_Object = MibTableColumn
pimSGUpstreamNeighbor = _PimSGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 8),
    _PimSGUpstreamNeighbor_Type()
)
pimSGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpstreamNeighbor.setStatus("current")
_PimSGRPFIfIndex_Type = InterfaceIndexOrZero
_PimSGRPFIfIndex_Object = MibTableColumn
pimSGRPFIfIndex = _PimSGRPFIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 9),
    _PimSGRPFIfIndex_Type()
)
pimSGRPFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFIfIndex.setStatus("current")
_PimSGRPFNextHopType_Type = InetAddressType
_PimSGRPFNextHopType_Object = MibTableColumn
pimSGRPFNextHopType = _PimSGRPFNextHopType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 10),
    _PimSGRPFNextHopType_Type()
)
pimSGRPFNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFNextHopType.setStatus("current")


class _PimSGRPFNextHop_Type(InetAddress):
    """Custom type pimSGRPFNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGRPFNextHop_Type.__name__ = "InetAddress"
_PimSGRPFNextHop_Object = MibTableColumn
pimSGRPFNextHop = _PimSGRPFNextHop_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 11),
    _PimSGRPFNextHop_Type()
)
pimSGRPFNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFNextHop.setStatus("current")
_PimSGRPFRouteProtocol_Type = IANAipRouteProtocol
_PimSGRPFRouteProtocol_Object = MibTableColumn
pimSGRPFRouteProtocol = _PimSGRPFRouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 12),
    _PimSGRPFRouteProtocol_Type()
)
pimSGRPFRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFRouteProtocol.setStatus("current")


class _PimSGRPFRouteAddress_Type(InetAddress):
    """Custom type pimSGRPFRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGRPFRouteAddress_Type.__name__ = "InetAddress"
_PimSGRPFRouteAddress_Object = MibTableColumn
pimSGRPFRouteAddress = _PimSGRPFRouteAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 13),
    _PimSGRPFRouteAddress_Type()
)
pimSGRPFRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFRouteAddress.setStatus("current")
_PimSGRPFRoutePrefixLength_Type = InetAddressPrefixLength
_PimSGRPFRoutePrefixLength_Object = MibTableColumn
pimSGRPFRoutePrefixLength = _PimSGRPFRoutePrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 14),
    _PimSGRPFRoutePrefixLength_Type()
)
pimSGRPFRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFRoutePrefixLength.setStatus("current")


class _PimSGRPFRouteMetricPref_Type(Unsigned32):
    """Custom type pimSGRPFRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PimSGRPFRouteMetricPref_Type.__name__ = "Unsigned32"
_PimSGRPFRouteMetricPref_Object = MibTableColumn
pimSGRPFRouteMetricPref = _PimSGRPFRouteMetricPref_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 15),
    _PimSGRPFRouteMetricPref_Type()
)
pimSGRPFRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFRouteMetricPref.setStatus("current")
_PimSGRPFRouteMetric_Type = Unsigned32
_PimSGRPFRouteMetric_Object = MibTableColumn
pimSGRPFRouteMetric = _PimSGRPFRouteMetric_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 16),
    _PimSGRPFRouteMetric_Type()
)
pimSGRPFRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPFRouteMetric.setStatus("current")
_PimSGSPTBit_Type = TruthValue
_PimSGSPTBit_Object = MibTableColumn
pimSGSPTBit = _PimSGSPTBit_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 17),
    _PimSGSPTBit_Type()
)
pimSGSPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGSPTBit.setStatus("current")
_PimSGKeepaliveTimer_Type = TimeTicks
_PimSGKeepaliveTimer_Object = MibTableColumn
pimSGKeepaliveTimer = _PimSGKeepaliveTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 18),
    _PimSGKeepaliveTimer_Type()
)
pimSGKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGKeepaliveTimer.setStatus("current")


class _PimSGDRRegisterState_Type(Integer32):
    """Custom type pimSGDRRegisterState based on Integer32"""
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


_PimSGDRRegisterState_Type.__name__ = "Integer32"
_PimSGDRRegisterState_Object = MibTableColumn
pimSGDRRegisterState = _PimSGDRRegisterState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 19),
    _PimSGDRRegisterState_Type()
)
pimSGDRRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGDRRegisterState.setStatus("current")
_PimSGDRRegisterStopTimer_Type = TimeTicks
_PimSGDRRegisterStopTimer_Object = MibTableColumn
pimSGDRRegisterStopTimer = _PimSGDRRegisterStopTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 20),
    _PimSGDRRegisterStopTimer_Type()
)
pimSGDRRegisterStopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGDRRegisterStopTimer.setStatus("current")
_PimSGRPRegisterPMBRAddressType_Type = InetAddressType
_PimSGRPRegisterPMBRAddressType_Object = MibTableColumn
pimSGRPRegisterPMBRAddressType = _PimSGRPRegisterPMBRAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 21),
    _PimSGRPRegisterPMBRAddressType_Type()
)
pimSGRPRegisterPMBRAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPRegisterPMBRAddressType.setStatus("current")


class _PimSGRPRegisterPMBRAddress_Type(InetAddress):
    """Custom type pimSGRPRegisterPMBRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGRPRegisterPMBRAddress_Type.__name__ = "InetAddress"
_PimSGRPRegisterPMBRAddress_Object = MibTableColumn
pimSGRPRegisterPMBRAddress = _PimSGRPRegisterPMBRAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 22),
    _PimSGRPRegisterPMBRAddress_Type()
)
pimSGRPRegisterPMBRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRPRegisterPMBRAddress.setStatus("current")


class _PimSGUpstreamPruneState_Type(Integer32):
    """Custom type pimSGUpstreamPruneState based on Integer32"""
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


_PimSGUpstreamPruneState_Type.__name__ = "Integer32"
_PimSGUpstreamPruneState_Object = MibTableColumn
pimSGUpstreamPruneState = _PimSGUpstreamPruneState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 23),
    _PimSGUpstreamPruneState_Type()
)
pimSGUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpstreamPruneState.setStatus("current")
_PimSGUpstreamPruneLimitTimer_Type = TimeTicks
_PimSGUpstreamPruneLimitTimer_Object = MibTableColumn
pimSGUpstreamPruneLimitTimer = _PimSGUpstreamPruneLimitTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 24),
    _PimSGUpstreamPruneLimitTimer_Type()
)
pimSGUpstreamPruneLimitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGUpstreamPruneLimitTimer.setStatus("current")


class _PimSGOriginatorState_Type(Integer32):
    """Custom type pimSGOriginatorState based on Integer32"""
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


_PimSGOriginatorState_Type.__name__ = "Integer32"
_PimSGOriginatorState_Object = MibTableColumn
pimSGOriginatorState = _PimSGOriginatorState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 25),
    _PimSGOriginatorState_Type()
)
pimSGOriginatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGOriginatorState.setStatus("current")
_PimSGSourceActiveTimer_Type = TimeTicks
_PimSGSourceActiveTimer_Object = MibTableColumn
pimSGSourceActiveTimer = _PimSGSourceActiveTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 26),
    _PimSGSourceActiveTimer_Type()
)
pimSGSourceActiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGSourceActiveTimer.setStatus("current")
_PimSGStateRefreshTimer_Type = TimeTicks
_PimSGStateRefreshTimer_Object = MibTableColumn
pimSGStateRefreshTimer = _PimSGStateRefreshTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 6, 1, 27),
    _PimSGStateRefreshTimer_Type()
)
pimSGStateRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGStateRefreshTimer.setStatus("current")
_PimSGITable_Object = MibTable
pimSGITable = _PimSGITable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7)
)
if mibBuilder.loadTexts:
    pimSGITable.setStatus("current")
_PimSGIEntry_Object = MibTableRow
pimSGIEntry = _PimSGIEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1)
)
pimSGIEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimSGAddressType"),
    (0, "PIM-STD-MIB", "pimSGGrpAddress"),
    (0, "PIM-STD-MIB", "pimSGSrcAddress"),
    (0, "PIM-STD-MIB", "pimSGIIfIndex"),
)
if mibBuilder.loadTexts:
    pimSGIEntry.setStatus("current")
_PimSGIIfIndex_Type = InterfaceIndex
_PimSGIIfIndex_Object = MibTableColumn
pimSGIIfIndex = _PimSGIIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 1),
    _PimSGIIfIndex_Type()
)
pimSGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGIIfIndex.setStatus("current")
_PimSGIUpTime_Type = TimeTicks
_PimSGIUpTime_Object = MibTableColumn
pimSGIUpTime = _PimSGIUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 2),
    _PimSGIUpTime_Type()
)
pimSGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIUpTime.setStatus("current")
_PimSGILocalMembership_Type = TruthValue
_PimSGILocalMembership_Object = MibTableColumn
pimSGILocalMembership = _PimSGILocalMembership_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 3),
    _PimSGILocalMembership_Type()
)
pimSGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGILocalMembership.setStatus("current")


class _PimSGIJoinPruneState_Type(Integer32):
    """Custom type pimSGIJoinPruneState based on Integer32"""
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


_PimSGIJoinPruneState_Type.__name__ = "Integer32"
_PimSGIJoinPruneState_Object = MibTableColumn
pimSGIJoinPruneState = _PimSGIJoinPruneState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 4),
    _PimSGIJoinPruneState_Type()
)
pimSGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIJoinPruneState.setStatus("current")
_PimSGIPrunePendingTimer_Type = TimeTicks
_PimSGIPrunePendingTimer_Object = MibTableColumn
pimSGIPrunePendingTimer = _PimSGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 5),
    _PimSGIPrunePendingTimer_Type()
)
pimSGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIPrunePendingTimer.setStatus("current")
_PimSGIJoinExpiryTimer_Type = TimeTicks
_PimSGIJoinExpiryTimer_Object = MibTableColumn
pimSGIJoinExpiryTimer = _PimSGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 6),
    _PimSGIJoinExpiryTimer_Type()
)
pimSGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIJoinExpiryTimer.setStatus("current")


class _PimSGIAssertState_Type(Integer32):
    """Custom type pimSGIAssertState based on Integer32"""
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


_PimSGIAssertState_Type.__name__ = "Integer32"
_PimSGIAssertState_Object = MibTableColumn
pimSGIAssertState = _PimSGIAssertState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 7),
    _PimSGIAssertState_Type()
)
pimSGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertState.setStatus("current")
_PimSGIAssertTimer_Type = TimeTicks
_PimSGIAssertTimer_Object = MibTableColumn
pimSGIAssertTimer = _PimSGIAssertTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 8),
    _PimSGIAssertTimer_Type()
)
pimSGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertTimer.setStatus("current")
_PimSGIAssertWinnerAddressType_Type = InetAddressType
_PimSGIAssertWinnerAddressType_Object = MibTableColumn
pimSGIAssertWinnerAddressType = _PimSGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 9),
    _PimSGIAssertWinnerAddressType_Type()
)
pimSGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertWinnerAddressType.setStatus("current")


class _PimSGIAssertWinnerAddress_Type(InetAddress):
    """Custom type pimSGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_PimSGIAssertWinnerAddress_Object = MibTableColumn
pimSGIAssertWinnerAddress = _PimSGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 10),
    _PimSGIAssertWinnerAddress_Type()
)
pimSGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertWinnerAddress.setStatus("current")


class _PimSGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type pimSGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PimSGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_PimSGIAssertWinnerMetricPref_Object = MibTableColumn
pimSGIAssertWinnerMetricPref = _PimSGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 11),
    _PimSGIAssertWinnerMetricPref_Type()
)
pimSGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertWinnerMetricPref.setStatus("current")
_PimSGIAssertWinnerMetric_Type = Unsigned32
_PimSGIAssertWinnerMetric_Object = MibTableColumn
pimSGIAssertWinnerMetric = _PimSGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 7, 1, 12),
    _PimSGIAssertWinnerMetric_Type()
)
pimSGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIAssertWinnerMetric.setStatus("current")
_PimSGRptTable_Object = MibTable
pimSGRptTable = _PimSGRptTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8)
)
if mibBuilder.loadTexts:
    pimSGRptTable.setStatus("current")
_PimSGRptEntry_Object = MibTableRow
pimSGRptEntry = _PimSGRptEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8, 1)
)
pimSGRptEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimStarGAddressType"),
    (0, "PIM-STD-MIB", "pimStarGGrpAddress"),
    (0, "PIM-STD-MIB", "pimSGRptSrcAddress"),
)
if mibBuilder.loadTexts:
    pimSGRptEntry.setStatus("current")


class _PimSGRptSrcAddress_Type(InetAddress):
    """Custom type pimSGRptSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimSGRptSrcAddress_Type.__name__ = "InetAddress"
_PimSGRptSrcAddress_Object = MibTableColumn
pimSGRptSrcAddress = _PimSGRptSrcAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8, 1, 1),
    _PimSGRptSrcAddress_Type()
)
pimSGRptSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGRptSrcAddress.setStatus("current")
_PimSGRptUpTime_Type = TimeTicks
_PimSGRptUpTime_Object = MibTableColumn
pimSGRptUpTime = _PimSGRptUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8, 1, 2),
    _PimSGRptUpTime_Type()
)
pimSGRptUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptUpTime.setStatus("current")


class _PimSGRptUpstreamPruneState_Type(Integer32):
    """Custom type pimSGRptUpstreamPruneState based on Integer32"""
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


_PimSGRptUpstreamPruneState_Type.__name__ = "Integer32"
_PimSGRptUpstreamPruneState_Object = MibTableColumn
pimSGRptUpstreamPruneState = _PimSGRptUpstreamPruneState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8, 1, 3),
    _PimSGRptUpstreamPruneState_Type()
)
pimSGRptUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptUpstreamPruneState.setStatus("current")
_PimSGRptUpstreamOverrideTimer_Type = TimeTicks
_PimSGRptUpstreamOverrideTimer_Object = MibTableColumn
pimSGRptUpstreamOverrideTimer = _PimSGRptUpstreamOverrideTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 8, 1, 4),
    _PimSGRptUpstreamOverrideTimer_Type()
)
pimSGRptUpstreamOverrideTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptUpstreamOverrideTimer.setStatus("current")
_PimSGRptITable_Object = MibTable
pimSGRptITable = _PimSGRptITable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9)
)
if mibBuilder.loadTexts:
    pimSGRptITable.setStatus("current")
_PimSGRptIEntry_Object = MibTableRow
pimSGRptIEntry = _PimSGRptIEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1)
)
pimSGRptIEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimStarGAddressType"),
    (0, "PIM-STD-MIB", "pimStarGGrpAddress"),
    (0, "PIM-STD-MIB", "pimSGRptSrcAddress"),
    (0, "PIM-STD-MIB", "pimSGRptIIfIndex"),
)
if mibBuilder.loadTexts:
    pimSGRptIEntry.setStatus("current")
_PimSGRptIIfIndex_Type = InterfaceIndex
_PimSGRptIIfIndex_Object = MibTableColumn
pimSGRptIIfIndex = _PimSGRptIIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 1),
    _PimSGRptIIfIndex_Type()
)
pimSGRptIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimSGRptIIfIndex.setStatus("current")
_PimSGRptIUpTime_Type = TimeTicks
_PimSGRptIUpTime_Object = MibTableColumn
pimSGRptIUpTime = _PimSGRptIUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 2),
    _PimSGRptIUpTime_Type()
)
pimSGRptIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptIUpTime.setStatus("current")
_PimSGRptILocalMembership_Type = TruthValue
_PimSGRptILocalMembership_Object = MibTableColumn
pimSGRptILocalMembership = _PimSGRptILocalMembership_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 3),
    _PimSGRptILocalMembership_Type()
)
pimSGRptILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptILocalMembership.setStatus("current")


class _PimSGRptIJoinPruneState_Type(Integer32):
    """Custom type pimSGRptIJoinPruneState based on Integer32"""
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


_PimSGRptIJoinPruneState_Type.__name__ = "Integer32"
_PimSGRptIJoinPruneState_Object = MibTableColumn
pimSGRptIJoinPruneState = _PimSGRptIJoinPruneState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 4),
    _PimSGRptIJoinPruneState_Type()
)
pimSGRptIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptIJoinPruneState.setStatus("current")
_PimSGRptIPrunePendingTimer_Type = TimeTicks
_PimSGRptIPrunePendingTimer_Object = MibTableColumn
pimSGRptIPrunePendingTimer = _PimSGRptIPrunePendingTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 5),
    _PimSGRptIPrunePendingTimer_Type()
)
pimSGRptIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptIPrunePendingTimer.setStatus("current")
_PimSGRptIPruneExpiryTimer_Type = TimeTicks
_PimSGRptIPruneExpiryTimer_Object = MibTableColumn
pimSGRptIPruneExpiryTimer = _PimSGRptIPruneExpiryTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 9, 1, 6),
    _PimSGRptIPruneExpiryTimer_Type()
)
pimSGRptIPruneExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptIPruneExpiryTimer.setStatus("current")
_PimBidirDFElectionTable_Object = MibTable
pimBidirDFElectionTable = _PimBidirDFElectionTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10)
)
if mibBuilder.loadTexts:
    pimBidirDFElectionTable.setStatus("current")
_PimBidirDFElectionEntry_Object = MibTableRow
pimBidirDFElectionEntry = _PimBidirDFElectionEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1)
)
pimBidirDFElectionEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimBidirDFElectionAddressType"),
    (0, "PIM-STD-MIB", "pimBidirDFElectionRPAddress"),
    (0, "PIM-STD-MIB", "pimBidirDFElectionIfIndex"),
)
if mibBuilder.loadTexts:
    pimBidirDFElectionEntry.setStatus("current")
_PimBidirDFElectionAddressType_Type = InetAddressType
_PimBidirDFElectionAddressType_Object = MibTableColumn
pimBidirDFElectionAddressType = _PimBidirDFElectionAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 1),
    _PimBidirDFElectionAddressType_Type()
)
pimBidirDFElectionAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBidirDFElectionAddressType.setStatus("current")


class _PimBidirDFElectionRPAddress_Type(InetAddress):
    """Custom type pimBidirDFElectionRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBidirDFElectionRPAddress_Type.__name__ = "InetAddress"
_PimBidirDFElectionRPAddress_Object = MibTableColumn
pimBidirDFElectionRPAddress = _PimBidirDFElectionRPAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 2),
    _PimBidirDFElectionRPAddress_Type()
)
pimBidirDFElectionRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBidirDFElectionRPAddress.setStatus("current")
_PimBidirDFElectionIfIndex_Type = InterfaceIndex
_PimBidirDFElectionIfIndex_Object = MibTableColumn
pimBidirDFElectionIfIndex = _PimBidirDFElectionIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 3),
    _PimBidirDFElectionIfIndex_Type()
)
pimBidirDFElectionIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimBidirDFElectionIfIndex.setStatus("current")
_PimBidirDFElectionWinnerAddressType_Type = InetAddressType
_PimBidirDFElectionWinnerAddressType_Object = MibTableColumn
pimBidirDFElectionWinnerAddressType = _PimBidirDFElectionWinnerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 4),
    _PimBidirDFElectionWinnerAddressType_Type()
)
pimBidirDFElectionWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionWinnerAddressType.setStatus("current")


class _PimBidirDFElectionWinnerAddress_Type(InetAddress):
    """Custom type pimBidirDFElectionWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimBidirDFElectionWinnerAddress_Type.__name__ = "InetAddress"
_PimBidirDFElectionWinnerAddress_Object = MibTableColumn
pimBidirDFElectionWinnerAddress = _PimBidirDFElectionWinnerAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 5),
    _PimBidirDFElectionWinnerAddress_Type()
)
pimBidirDFElectionWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionWinnerAddress.setStatus("current")
_PimBidirDFElectionWinnerUpTime_Type = TimeTicks
_PimBidirDFElectionWinnerUpTime_Object = MibTableColumn
pimBidirDFElectionWinnerUpTime = _PimBidirDFElectionWinnerUpTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 6),
    _PimBidirDFElectionWinnerUpTime_Type()
)
pimBidirDFElectionWinnerUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionWinnerUpTime.setStatus("current")
_PimBidirDFElectionWinnerMetricPref_Type = Unsigned32
_PimBidirDFElectionWinnerMetricPref_Object = MibTableColumn
pimBidirDFElectionWinnerMetricPref = _PimBidirDFElectionWinnerMetricPref_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 7),
    _PimBidirDFElectionWinnerMetricPref_Type()
)
pimBidirDFElectionWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionWinnerMetricPref.setStatus("current")
_PimBidirDFElectionWinnerMetric_Type = Unsigned32
_PimBidirDFElectionWinnerMetric_Object = MibTableColumn
pimBidirDFElectionWinnerMetric = _PimBidirDFElectionWinnerMetric_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 8),
    _PimBidirDFElectionWinnerMetric_Type()
)
pimBidirDFElectionWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionWinnerMetric.setStatus("current")


class _PimBidirDFElectionState_Type(Integer32):
    """Custom type pimBidirDFElectionState based on Integer32"""
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
        *(("dfBackoff", 4),
          ("dfLose", 2),
          ("dfOffer", 1),
          ("dfWinner", 3))
    )


_PimBidirDFElectionState_Type.__name__ = "Integer32"
_PimBidirDFElectionState_Object = MibTableColumn
pimBidirDFElectionState = _PimBidirDFElectionState_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 9),
    _PimBidirDFElectionState_Type()
)
pimBidirDFElectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionState.setStatus("current")
_PimBidirDFElectionStateTimer_Type = TimeTicks
_PimBidirDFElectionStateTimer_Object = MibTableColumn
pimBidirDFElectionStateTimer = _PimBidirDFElectionStateTimer_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 10, 1, 10),
    _PimBidirDFElectionStateTimer_Type()
)
pimBidirDFElectionStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimBidirDFElectionStateTimer.setStatus("current")
_PimStaticRPTable_Object = MibTable
pimStaticRPTable = _PimStaticRPTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11)
)
if mibBuilder.loadTexts:
    pimStaticRPTable.setStatus("current")
_PimStaticRPEntry_Object = MibTableRow
pimStaticRPEntry = _PimStaticRPEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1)
)
pimStaticRPEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimStaticRPAddressType"),
    (0, "PIM-STD-MIB", "pimStaticRPGrpAddress"),
    (0, "PIM-STD-MIB", "pimStaticRPGrpPrefixLength"),
)
if mibBuilder.loadTexts:
    pimStaticRPEntry.setStatus("current")
_PimStaticRPAddressType_Type = InetAddressType
_PimStaticRPAddressType_Object = MibTableColumn
pimStaticRPAddressType = _PimStaticRPAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 1),
    _PimStaticRPAddressType_Type()
)
pimStaticRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStaticRPAddressType.setStatus("current")


class _PimStaticRPGrpAddress_Type(InetAddress):
    """Custom type pimStaticRPGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStaticRPGrpAddress_Type.__name__ = "InetAddress"
_PimStaticRPGrpAddress_Object = MibTableColumn
pimStaticRPGrpAddress = _PimStaticRPGrpAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 2),
    _PimStaticRPGrpAddress_Type()
)
pimStaticRPGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStaticRPGrpAddress.setStatus("current")


class _PimStaticRPGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type pimStaticRPGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_PimStaticRPGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_PimStaticRPGrpPrefixLength_Object = MibTableColumn
pimStaticRPGrpPrefixLength = _PimStaticRPGrpPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 3),
    _PimStaticRPGrpPrefixLength_Type()
)
pimStaticRPGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimStaticRPGrpPrefixLength.setStatus("current")


class _PimStaticRPRPAddress_Type(InetAddress):
    """Custom type pimStaticRPRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimStaticRPRPAddress_Type.__name__ = "InetAddress"
_PimStaticRPRPAddress_Object = MibTableColumn
pimStaticRPRPAddress = _PimStaticRPRPAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 4),
    _PimStaticRPRPAddress_Type()
)
pimStaticRPRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPRPAddress.setStatus("current")


class _PimStaticRPPimMode_Type(PimMode):
    """Custom type pimStaticRPPimMode based on PimMode"""
    defaultValue = 3

    subtypeSpec = PimMode.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("asm", 3),
          ("bidir", 4),
          ("ssm", 2))
    )


_PimStaticRPPimMode_Type.__name__ = "PimMode"
_PimStaticRPPimMode_Object = MibTableColumn
pimStaticRPPimMode = _PimStaticRPPimMode_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 5),
    _PimStaticRPPimMode_Type()
)
pimStaticRPPimMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPPimMode.setStatus("current")


class _PimStaticRPOverrideDynamic_Type(TruthValue):
    """Custom type pimStaticRPOverrideDynamic based on TruthValue"""


_PimStaticRPOverrideDynamic_Object = MibTableColumn
pimStaticRPOverrideDynamic = _PimStaticRPOverrideDynamic_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 6),
    _PimStaticRPOverrideDynamic_Type()
)
pimStaticRPOverrideDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPOverrideDynamic.setStatus("current")
_PimStaticRPPrecedence_Type = Unsigned32
_PimStaticRPPrecedence_Object = MibTableColumn
pimStaticRPPrecedence = _PimStaticRPPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 7),
    _PimStaticRPPrecedence_Type()
)
pimStaticRPPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPPrecedence.setStatus("current")
_PimStaticRPRowStatus_Type = RowStatus
_PimStaticRPRowStatus_Object = MibTableColumn
pimStaticRPRowStatus = _PimStaticRPRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 8),
    _PimStaticRPRowStatus_Type()
)
pimStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPRowStatus.setStatus("current")


class _PimStaticRPStorageType_Type(StorageType):
    """Custom type pimStaticRPStorageType based on StorageType"""


_PimStaticRPStorageType_Object = MibTableColumn
pimStaticRPStorageType = _PimStaticRPStorageType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 11, 1, 9),
    _PimStaticRPStorageType_Type()
)
pimStaticRPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimStaticRPStorageType.setStatus("current")
_PimAnycastRPSetTable_Object = MibTable
pimAnycastRPSetTable = _PimAnycastRPSetTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12)
)
if mibBuilder.loadTexts:
    pimAnycastRPSetTable.setStatus("current")
_PimAnycastRPSetEntry_Object = MibTableRow
pimAnycastRPSetEntry = _PimAnycastRPSetEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1)
)
pimAnycastRPSetEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimAnycastRPSetAddressType"),
    (0, "PIM-STD-MIB", "pimAnycastRPSetAnycastAddress"),
    (0, "PIM-STD-MIB", "pimAnycastRPSetRouterAddress"),
)
if mibBuilder.loadTexts:
    pimAnycastRPSetEntry.setStatus("current")
_PimAnycastRPSetAddressType_Type = InetAddressType
_PimAnycastRPSetAddressType_Object = MibTableColumn
pimAnycastRPSetAddressType = _PimAnycastRPSetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 1),
    _PimAnycastRPSetAddressType_Type()
)
pimAnycastRPSetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimAnycastRPSetAddressType.setStatus("current")


class _PimAnycastRPSetAnycastAddress_Type(InetAddress):
    """Custom type pimAnycastRPSetAnycastAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimAnycastRPSetAnycastAddress_Type.__name__ = "InetAddress"
_PimAnycastRPSetAnycastAddress_Object = MibTableColumn
pimAnycastRPSetAnycastAddress = _PimAnycastRPSetAnycastAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 2),
    _PimAnycastRPSetAnycastAddress_Type()
)
pimAnycastRPSetAnycastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimAnycastRPSetAnycastAddress.setStatus("current")


class _PimAnycastRPSetRouterAddress_Type(InetAddress):
    """Custom type pimAnycastRPSetRouterAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimAnycastRPSetRouterAddress_Type.__name__ = "InetAddress"
_PimAnycastRPSetRouterAddress_Object = MibTableColumn
pimAnycastRPSetRouterAddress = _PimAnycastRPSetRouterAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 3),
    _PimAnycastRPSetRouterAddress_Type()
)
pimAnycastRPSetRouterAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimAnycastRPSetRouterAddress.setStatus("current")
_PimAnycastRPSetLocalRouter_Type = TruthValue
_PimAnycastRPSetLocalRouter_Object = MibTableColumn
pimAnycastRPSetLocalRouter = _PimAnycastRPSetLocalRouter_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 4),
    _PimAnycastRPSetLocalRouter_Type()
)
pimAnycastRPSetLocalRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimAnycastRPSetLocalRouter.setStatus("current")
_PimAnycastRPSetRowStatus_Type = RowStatus
_PimAnycastRPSetRowStatus_Object = MibTableColumn
pimAnycastRPSetRowStatus = _PimAnycastRPSetRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 5),
    _PimAnycastRPSetRowStatus_Type()
)
pimAnycastRPSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimAnycastRPSetRowStatus.setStatus("current")


class _PimAnycastRPSetStorageType_Type(StorageType):
    """Custom type pimAnycastRPSetStorageType based on StorageType"""


_PimAnycastRPSetStorageType_Object = MibTableColumn
pimAnycastRPSetStorageType = _PimAnycastRPSetStorageType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 12, 1, 6),
    _PimAnycastRPSetStorageType_Type()
)
pimAnycastRPSetStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pimAnycastRPSetStorageType.setStatus("current")
_PimGroupMappingTable_Object = MibTable
pimGroupMappingTable = _PimGroupMappingTable_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13)
)
if mibBuilder.loadTexts:
    pimGroupMappingTable.setStatus("current")
_PimGroupMappingEntry_Object = MibTableRow
pimGroupMappingEntry = _PimGroupMappingEntry_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1)
)
pimGroupMappingEntry.setIndexNames(
    (0, "PIM-STD-MIB", "pimGroupMappingOrigin"),
    (0, "PIM-STD-MIB", "pimGroupMappingAddressType"),
    (0, "PIM-STD-MIB", "pimGroupMappingGrpAddress"),
    (0, "PIM-STD-MIB", "pimGroupMappingGrpPrefixLength"),
    (0, "PIM-STD-MIB", "pimGroupMappingRPAddressType"),
    (0, "PIM-STD-MIB", "pimGroupMappingRPAddress"),
)
if mibBuilder.loadTexts:
    pimGroupMappingEntry.setStatus("current")
_PimGroupMappingOrigin_Type = PimGroupMappingOriginType
_PimGroupMappingOrigin_Object = MibTableColumn
pimGroupMappingOrigin = _PimGroupMappingOrigin_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 1),
    _PimGroupMappingOrigin_Type()
)
pimGroupMappingOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingOrigin.setStatus("current")
_PimGroupMappingAddressType_Type = InetAddressType
_PimGroupMappingAddressType_Object = MibTableColumn
pimGroupMappingAddressType = _PimGroupMappingAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 2),
    _PimGroupMappingAddressType_Type()
)
pimGroupMappingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingAddressType.setStatus("current")


class _PimGroupMappingGrpAddress_Type(InetAddress):
    """Custom type pimGroupMappingGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimGroupMappingGrpAddress_Type.__name__ = "InetAddress"
_PimGroupMappingGrpAddress_Object = MibTableColumn
pimGroupMappingGrpAddress = _PimGroupMappingGrpAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 3),
    _PimGroupMappingGrpAddress_Type()
)
pimGroupMappingGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingGrpAddress.setStatus("current")


class _PimGroupMappingGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type pimGroupMappingGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_PimGroupMappingGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_PimGroupMappingGrpPrefixLength_Object = MibTableColumn
pimGroupMappingGrpPrefixLength = _PimGroupMappingGrpPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 4),
    _PimGroupMappingGrpPrefixLength_Type()
)
pimGroupMappingGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingGrpPrefixLength.setStatus("current")
_PimGroupMappingRPAddressType_Type = InetAddressType
_PimGroupMappingRPAddressType_Object = MibTableColumn
pimGroupMappingRPAddressType = _PimGroupMappingRPAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 5),
    _PimGroupMappingRPAddressType_Type()
)
pimGroupMappingRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingRPAddressType.setStatus("current")


class _PimGroupMappingRPAddress_Type(InetAddress):
    """Custom type pimGroupMappingRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimGroupMappingRPAddress_Type.__name__ = "InetAddress"
_PimGroupMappingRPAddress_Object = MibTableColumn
pimGroupMappingRPAddress = _PimGroupMappingRPAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 6),
    _PimGroupMappingRPAddress_Type()
)
pimGroupMappingRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pimGroupMappingRPAddress.setStatus("current")
_PimGroupMappingPimMode_Type = PimMode
_PimGroupMappingPimMode_Object = MibTableColumn
pimGroupMappingPimMode = _PimGroupMappingPimMode_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 7),
    _PimGroupMappingPimMode_Type()
)
pimGroupMappingPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimGroupMappingPimMode.setStatus("current")
_PimGroupMappingPrecedence_Type = Unsigned32
_PimGroupMappingPrecedence_Object = MibTableColumn
pimGroupMappingPrecedence = _PimGroupMappingPrecedence_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 13, 1, 8),
    _PimGroupMappingPrecedence_Type()
)
pimGroupMappingPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimGroupMappingPrecedence.setStatus("current")


class _PimKeepalivePeriod_Type(Unsigned32):
    """Custom type pimKeepalivePeriod based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimKeepalivePeriod_Type.__name__ = "Unsigned32"
_PimKeepalivePeriod_Object = MibScalar
pimKeepalivePeriod = _PimKeepalivePeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 14),
    _PimKeepalivePeriod_Type()
)
pimKeepalivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimKeepalivePeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimKeepalivePeriod.setUnits("seconds")


class _PimRegisterSuppressionTime_Type(Unsigned32):
    """Custom type pimRegisterSuppressionTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimRegisterSuppressionTime_Type.__name__ = "Unsigned32"
_PimRegisterSuppressionTime_Object = MibScalar
pimRegisterSuppressionTime = _PimRegisterSuppressionTime_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 15),
    _PimRegisterSuppressionTime_Type()
)
pimRegisterSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimRegisterSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    pimRegisterSuppressionTime.setUnits("seconds")
_PimStarGEntries_Type = Gauge32
_PimStarGEntries_Object = MibScalar
pimStarGEntries = _PimStarGEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 16),
    _PimStarGEntries_Type()
)
pimStarGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGEntries.setStatus("current")
_PimStarGIEntries_Type = Gauge32
_PimStarGIEntries_Object = MibScalar
pimStarGIEntries = _PimStarGIEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 17),
    _PimStarGIEntries_Type()
)
pimStarGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimStarGIEntries.setStatus("current")
_PimSGEntries_Type = Gauge32
_PimSGEntries_Object = MibScalar
pimSGEntries = _PimSGEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 18),
    _PimSGEntries_Type()
)
pimSGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGEntries.setStatus("current")
_PimSGIEntries_Type = Gauge32
_PimSGIEntries_Object = MibScalar
pimSGIEntries = _PimSGIEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 19),
    _PimSGIEntries_Type()
)
pimSGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGIEntries.setStatus("current")
_PimSGRptEntries_Type = Gauge32
_PimSGRptEntries_Object = MibScalar
pimSGRptEntries = _PimSGRptEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 20),
    _PimSGRptEntries_Type()
)
pimSGRptEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptEntries.setStatus("current")
_PimSGRptIEntries_Type = Gauge32
_PimSGRptIEntries_Object = MibScalar
pimSGRptIEntries = _PimSGRptIEntries_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 21),
    _PimSGRptIEntries_Type()
)
pimSGRptIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimSGRptIEntries.setStatus("current")
_PimOutAsserts_Type = Counter64
_PimOutAsserts_Object = MibScalar
pimOutAsserts = _PimOutAsserts_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 22),
    _PimOutAsserts_Type()
)
pimOutAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimOutAsserts.setStatus("current")
_PimInAsserts_Type = Counter64
_PimInAsserts_Object = MibScalar
pimInAsserts = _PimInAsserts_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 23),
    _PimInAsserts_Type()
)
pimInAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInAsserts.setStatus("current")
_PimLastAssertInterface_Type = InterfaceIndexOrZero
_PimLastAssertInterface_Object = MibScalar
pimLastAssertInterface = _PimLastAssertInterface_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 24),
    _PimLastAssertInterface_Type()
)
pimLastAssertInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimLastAssertInterface.setStatus("current")
_PimLastAssertGroupAddressType_Type = InetAddressType
_PimLastAssertGroupAddressType_Object = MibScalar
pimLastAssertGroupAddressType = _PimLastAssertGroupAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 25),
    _PimLastAssertGroupAddressType_Type()
)
pimLastAssertGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimLastAssertGroupAddressType.setStatus("current")


class _PimLastAssertGroupAddress_Type(InetAddress):
    """Custom type pimLastAssertGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimLastAssertGroupAddress_Type.__name__ = "InetAddress"
_PimLastAssertGroupAddress_Object = MibScalar
pimLastAssertGroupAddress = _PimLastAssertGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 26),
    _PimLastAssertGroupAddress_Type()
)
pimLastAssertGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimLastAssertGroupAddress.setStatus("current")
_PimLastAssertSourceAddressType_Type = InetAddressType
_PimLastAssertSourceAddressType_Object = MibScalar
pimLastAssertSourceAddressType = _PimLastAssertSourceAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 27),
    _PimLastAssertSourceAddressType_Type()
)
pimLastAssertSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimLastAssertSourceAddressType.setStatus("current")


class _PimLastAssertSourceAddress_Type(InetAddress):
    """Custom type pimLastAssertSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimLastAssertSourceAddress_Type.__name__ = "InetAddress"
_PimLastAssertSourceAddress_Object = MibScalar
pimLastAssertSourceAddress = _PimLastAssertSourceAddress_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 28),
    _PimLastAssertSourceAddress_Type()
)
pimLastAssertSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimLastAssertSourceAddress.setStatus("current")


class _PimNeighborLossNotificationPeriod_Type(Unsigned32):
    """Custom type pimNeighborLossNotificationPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimNeighborLossNotificationPeriod_Type.__name__ = "Unsigned32"
_PimNeighborLossNotificationPeriod_Object = MibScalar
pimNeighborLossNotificationPeriod = _PimNeighborLossNotificationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 29),
    _PimNeighborLossNotificationPeriod_Type()
)
pimNeighborLossNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimNeighborLossNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimNeighborLossNotificationPeriod.setUnits("seconds")
_PimNeighborLossCount_Type = Counter32
_PimNeighborLossCount_Object = MibScalar
pimNeighborLossCount = _PimNeighborLossCount_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 30),
    _PimNeighborLossCount_Type()
)
pimNeighborLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimNeighborLossCount.setStatus("current")


class _PimInvalidRegisterNotificationPeriod_Type(Unsigned32):
    """Custom type pimInvalidRegisterNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_PimInvalidRegisterNotificationPeriod_Type.__name__ = "Unsigned32"
_PimInvalidRegisterNotificationPeriod_Object = MibScalar
pimInvalidRegisterNotificationPeriod = _PimInvalidRegisterNotificationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 31),
    _PimInvalidRegisterNotificationPeriod_Type()
)
pimInvalidRegisterNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimInvalidRegisterNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimInvalidRegisterNotificationPeriod.setUnits("seconds")
_PimInvalidRegisterMsgsRcvd_Type = Counter32
_PimInvalidRegisterMsgsRcvd_Object = MibScalar
pimInvalidRegisterMsgsRcvd = _PimInvalidRegisterMsgsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 32),
    _PimInvalidRegisterMsgsRcvd_Type()
)
pimInvalidRegisterMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidRegisterMsgsRcvd.setStatus("current")
_PimInvalidRegisterAddressType_Type = InetAddressType
_PimInvalidRegisterAddressType_Object = MibScalar
pimInvalidRegisterAddressType = _PimInvalidRegisterAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 33),
    _PimInvalidRegisterAddressType_Type()
)
pimInvalidRegisterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidRegisterAddressType.setStatus("current")


class _PimInvalidRegisterOrigin_Type(InetAddress):
    """Custom type pimInvalidRegisterOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidRegisterOrigin_Type.__name__ = "InetAddress"
_PimInvalidRegisterOrigin_Object = MibScalar
pimInvalidRegisterOrigin = _PimInvalidRegisterOrigin_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 34),
    _PimInvalidRegisterOrigin_Type()
)
pimInvalidRegisterOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidRegisterOrigin.setStatus("current")


class _PimInvalidRegisterGroup_Type(InetAddress):
    """Custom type pimInvalidRegisterGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidRegisterGroup_Type.__name__ = "InetAddress"
_PimInvalidRegisterGroup_Object = MibScalar
pimInvalidRegisterGroup = _PimInvalidRegisterGroup_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 35),
    _PimInvalidRegisterGroup_Type()
)
pimInvalidRegisterGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidRegisterGroup.setStatus("current")


class _PimInvalidRegisterRp_Type(InetAddress):
    """Custom type pimInvalidRegisterRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidRegisterRp_Type.__name__ = "InetAddress"
_PimInvalidRegisterRp_Object = MibScalar
pimInvalidRegisterRp = _PimInvalidRegisterRp_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 36),
    _PimInvalidRegisterRp_Type()
)
pimInvalidRegisterRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidRegisterRp.setStatus("current")


class _PimInvalidJoinPruneNotificationPeriod_Type(Unsigned32):
    """Custom type pimInvalidJoinPruneNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_PimInvalidJoinPruneNotificationPeriod_Type.__name__ = "Unsigned32"
_PimInvalidJoinPruneNotificationPeriod_Object = MibScalar
pimInvalidJoinPruneNotificationPeriod = _PimInvalidJoinPruneNotificationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 37),
    _PimInvalidJoinPruneNotificationPeriod_Type()
)
pimInvalidJoinPruneNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneNotificationPeriod.setUnits("seconds")
_PimInvalidJoinPruneMsgsRcvd_Type = Counter32
_PimInvalidJoinPruneMsgsRcvd_Object = MibScalar
pimInvalidJoinPruneMsgsRcvd = _PimInvalidJoinPruneMsgsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 38),
    _PimInvalidJoinPruneMsgsRcvd_Type()
)
pimInvalidJoinPruneMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneMsgsRcvd.setStatus("current")
_PimInvalidJoinPruneAddressType_Type = InetAddressType
_PimInvalidJoinPruneAddressType_Object = MibScalar
pimInvalidJoinPruneAddressType = _PimInvalidJoinPruneAddressType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 39),
    _PimInvalidJoinPruneAddressType_Type()
)
pimInvalidJoinPruneAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneAddressType.setStatus("current")


class _PimInvalidJoinPruneOrigin_Type(InetAddress):
    """Custom type pimInvalidJoinPruneOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidJoinPruneOrigin_Type.__name__ = "InetAddress"
_PimInvalidJoinPruneOrigin_Object = MibScalar
pimInvalidJoinPruneOrigin = _PimInvalidJoinPruneOrigin_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 40),
    _PimInvalidJoinPruneOrigin_Type()
)
pimInvalidJoinPruneOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneOrigin.setStatus("current")


class _PimInvalidJoinPruneGroup_Type(InetAddress):
    """Custom type pimInvalidJoinPruneGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidJoinPruneGroup_Type.__name__ = "InetAddress"
_PimInvalidJoinPruneGroup_Object = MibScalar
pimInvalidJoinPruneGroup = _PimInvalidJoinPruneGroup_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 41),
    _PimInvalidJoinPruneGroup_Type()
)
pimInvalidJoinPruneGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneGroup.setStatus("current")


class _PimInvalidJoinPruneRp_Type(InetAddress):
    """Custom type pimInvalidJoinPruneRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_PimInvalidJoinPruneRp_Type.__name__ = "InetAddress"
_PimInvalidJoinPruneRp_Object = MibScalar
pimInvalidJoinPruneRp = _PimInvalidJoinPruneRp_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 42),
    _PimInvalidJoinPruneRp_Type()
)
pimInvalidJoinPruneRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInvalidJoinPruneRp.setStatus("current")


class _PimRPMappingNotificationPeriod_Type(Unsigned32):
    """Custom type pimRPMappingNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimRPMappingNotificationPeriod_Type.__name__ = "Unsigned32"
_PimRPMappingNotificationPeriod_Object = MibScalar
pimRPMappingNotificationPeriod = _PimRPMappingNotificationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 43),
    _PimRPMappingNotificationPeriod_Type()
)
pimRPMappingNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimRPMappingNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimRPMappingNotificationPeriod.setUnits("seconds")
_PimRPMappingChangeCount_Type = Counter32
_PimRPMappingChangeCount_Object = MibScalar
pimRPMappingChangeCount = _PimRPMappingChangeCount_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 44),
    _PimRPMappingChangeCount_Type()
)
pimRPMappingChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimRPMappingChangeCount.setStatus("current")


class _PimInterfaceElectionNotificationPeriod_Type(Unsigned32):
    """Custom type pimInterfaceElectionNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimInterfaceElectionNotificationPeriod_Type.__name__ = "Unsigned32"
_PimInterfaceElectionNotificationPeriod_Object = MibScalar
pimInterfaceElectionNotificationPeriod = _PimInterfaceElectionNotificationPeriod_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 45),
    _PimInterfaceElectionNotificationPeriod_Type()
)
pimInterfaceElectionNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimInterfaceElectionNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    pimInterfaceElectionNotificationPeriod.setUnits("seconds")
_PimInterfaceElectionWinCount_Type = Counter32
_PimInterfaceElectionWinCount_Object = MibScalar
pimInterfaceElectionWinCount = _PimInterfaceElectionWinCount_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 46),
    _PimInterfaceElectionWinCount_Type()
)
pimInterfaceElectionWinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pimInterfaceElectionWinCount.setStatus("current")


class _PimRefreshInterval_Type(Unsigned32):
    """Custom type pimRefreshInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PimRefreshInterval_Type.__name__ = "Unsigned32"
_PimRefreshInterval_Object = MibScalar
pimRefreshInterval = _PimRefreshInterval_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 47),
    _PimRefreshInterval_Type()
)
pimRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    pimRefreshInterval.setUnits("seconds")


class _PimDeviceConfigStorageType_Type(StorageType):
    """Custom type pimDeviceConfigStorageType based on StorageType"""


_PimDeviceConfigStorageType_Object = MibScalar
pimDeviceConfigStorageType = _PimDeviceConfigStorageType_Object(
    (1, 3, 6, 1, 2, 1, 157, 1, 48),
    _PimDeviceConfigStorageType_Type()
)
pimDeviceConfigStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimDeviceConfigStorageType.setStatus("current")
_PimMIBConformance_ObjectIdentity = ObjectIdentity
pimMIBConformance = _PimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 157, 2)
)
_PimMIBCompliances_ObjectIdentity = ObjectIdentity
pimMIBCompliances = _PimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 157, 2, 1)
)
_PimMIBGroups_ObjectIdentity = ObjectIdentity
pimMIBGroups = _PimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 157, 2, 2)
)

# Managed Objects groups

pimTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 1)
)
pimTopologyGroup.setObjects(
      *(("PIM-STD-MIB", "pimInterfaceAddressType"),
        ("PIM-STD-MIB", "pimInterfaceAddress"),
        ("PIM-STD-MIB", "pimInterfaceGenerationIDValue"),
        ("PIM-STD-MIB", "pimInterfaceDR"),
        ("PIM-STD-MIB", "pimInterfaceDRPriorityEnabled"),
        ("PIM-STD-MIB", "pimInterfaceHelloHoldtime"),
        ("PIM-STD-MIB", "pimInterfaceJoinPruneHoldtime"),
        ("PIM-STD-MIB", "pimInterfaceLanDelayEnabled"),
        ("PIM-STD-MIB", "pimInterfaceEffectPropagDelay"),
        ("PIM-STD-MIB", "pimInterfaceEffectOverrideIvl"),
        ("PIM-STD-MIB", "pimInterfaceSuppressionEnabled"),
        ("PIM-STD-MIB", "pimInterfaceBidirCapable"),
        ("PIM-STD-MIB", "pimNeighborGenerationIDPresent"),
        ("PIM-STD-MIB", "pimNeighborGenerationIDValue"),
        ("PIM-STD-MIB", "pimNeighborUpTime"),
        ("PIM-STD-MIB", "pimNeighborExpiryTime"),
        ("PIM-STD-MIB", "pimNeighborDRPriorityPresent"),
        ("PIM-STD-MIB", "pimNeighborDRPriority"),
        ("PIM-STD-MIB", "pimNeighborLanPruneDelayPresent"),
        ("PIM-STD-MIB", "pimNeighborTBit"),
        ("PIM-STD-MIB", "pimNeighborPropagationDelay"),
        ("PIM-STD-MIB", "pimNeighborOverrideInterval"),
        ("PIM-STD-MIB", "pimNeighborBidirCapable"),
        ("PIM-STD-MIB", "pimNbrSecAddress"))
)
if mibBuilder.loadTexts:
    pimTopologyGroup.setStatus("current")

pimTuningParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 3)
)
pimTuningParametersGroup.setObjects(
      *(("PIM-STD-MIB", "pimKeepalivePeriod"),
        ("PIM-STD-MIB", "pimRegisterSuppressionTime"),
        ("PIM-STD-MIB", "pimInterfaceDRPriority"),
        ("PIM-STD-MIB", "pimInterfaceHelloInterval"),
        ("PIM-STD-MIB", "pimInterfaceTrigHelloInterval"),
        ("PIM-STD-MIB", "pimInterfaceJoinPruneInterval"),
        ("PIM-STD-MIB", "pimInterfacePropagationDelay"),
        ("PIM-STD-MIB", "pimInterfaceOverrideInterval"),
        ("PIM-STD-MIB", "pimInterfaceDomainBorder"),
        ("PIM-STD-MIB", "pimInterfaceStubInterface"),
        ("PIM-STD-MIB", "pimInterfaceStatus"),
        ("PIM-STD-MIB", "pimInterfaceStorageType"))
)
if mibBuilder.loadTexts:
    pimTuningParametersGroup.setStatus("current")

pimRouterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 4)
)
pimRouterStatisticsGroup.setObjects(
      *(("PIM-STD-MIB", "pimStarGEntries"),
        ("PIM-STD-MIB", "pimStarGIEntries"),
        ("PIM-STD-MIB", "pimSGEntries"),
        ("PIM-STD-MIB", "pimSGIEntries"),
        ("PIM-STD-MIB", "pimSGRptEntries"),
        ("PIM-STD-MIB", "pimSGRptIEntries"))
)
if mibBuilder.loadTexts:
    pimRouterStatisticsGroup.setStatus("current")

pimSsmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 5)
)
pimSsmGroup.setObjects(
      *(("PIM-STD-MIB", "pimSGUpTime"),
        ("PIM-STD-MIB", "pimSGPimMode"),
        ("PIM-STD-MIB", "pimSGUpstreamJoinState"),
        ("PIM-STD-MIB", "pimSGUpstreamJoinTimer"),
        ("PIM-STD-MIB", "pimSGUpstreamNeighbor"),
        ("PIM-STD-MIB", "pimSGRPFIfIndex"),
        ("PIM-STD-MIB", "pimSGRPFNextHopType"),
        ("PIM-STD-MIB", "pimSGRPFNextHop"),
        ("PIM-STD-MIB", "pimSGRPFRouteProtocol"),
        ("PIM-STD-MIB", "pimSGRPFRouteAddress"),
        ("PIM-STD-MIB", "pimSGRPFRoutePrefixLength"),
        ("PIM-STD-MIB", "pimSGRPFRouteMetricPref"),
        ("PIM-STD-MIB", "pimSGRPFRouteMetric"),
        ("PIM-STD-MIB", "pimSGSPTBit"),
        ("PIM-STD-MIB", "pimSGKeepaliveTimer"),
        ("PIM-STD-MIB", "pimSGDRRegisterState"),
        ("PIM-STD-MIB", "pimSGDRRegisterStopTimer"),
        ("PIM-STD-MIB", "pimSGRPRegisterPMBRAddressType"),
        ("PIM-STD-MIB", "pimSGRPRegisterPMBRAddress"),
        ("PIM-STD-MIB", "pimSGIUpTime"),
        ("PIM-STD-MIB", "pimSGILocalMembership"),
        ("PIM-STD-MIB", "pimSGIJoinPruneState"),
        ("PIM-STD-MIB", "pimSGIPrunePendingTimer"),
        ("PIM-STD-MIB", "pimSGIJoinExpiryTimer"),
        ("PIM-STD-MIB", "pimSGIAssertState"),
        ("PIM-STD-MIB", "pimSGIAssertTimer"),
        ("PIM-STD-MIB", "pimSGIAssertWinnerAddressType"),
        ("PIM-STD-MIB", "pimSGIAssertWinnerAddress"),
        ("PIM-STD-MIB", "pimSGIAssertWinnerMetricPref"),
        ("PIM-STD-MIB", "pimSGIAssertWinnerMetric"))
)
if mibBuilder.loadTexts:
    pimSsmGroup.setStatus("current")

pimRPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 6)
)
pimRPConfigGroup.setObjects(
      *(("PIM-STD-MIB", "pimStaticRPRPAddress"),
        ("PIM-STD-MIB", "pimStaticRPPimMode"),
        ("PIM-STD-MIB", "pimStaticRPOverrideDynamic"),
        ("PIM-STD-MIB", "pimStaticRPRowStatus"),
        ("PIM-STD-MIB", "pimStaticRPStorageType"),
        ("PIM-STD-MIB", "pimGroupMappingPimMode"),
        ("PIM-STD-MIB", "pimGroupMappingPrecedence"))
)
if mibBuilder.loadTexts:
    pimRPConfigGroup.setStatus("current")

pimSmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 7)
)
pimSmGroup.setObjects(
      *(("PIM-STD-MIB", "pimStarGUpTime"),
        ("PIM-STD-MIB", "pimStarGPimMode"),
        ("PIM-STD-MIB", "pimStarGRPAddressType"),
        ("PIM-STD-MIB", "pimStarGRPAddress"),
        ("PIM-STD-MIB", "pimStarGPimModeOrigin"),
        ("PIM-STD-MIB", "pimStarGRPIsLocal"),
        ("PIM-STD-MIB", "pimStarGUpstreamJoinState"),
        ("PIM-STD-MIB", "pimStarGUpstreamJoinTimer"),
        ("PIM-STD-MIB", "pimStarGUpstreamNeighborType"),
        ("PIM-STD-MIB", "pimStarGUpstreamNeighbor"),
        ("PIM-STD-MIB", "pimStarGRPFIfIndex"),
        ("PIM-STD-MIB", "pimStarGRPFNextHopType"),
        ("PIM-STD-MIB", "pimStarGRPFNextHop"),
        ("PIM-STD-MIB", "pimStarGRPFRouteProtocol"),
        ("PIM-STD-MIB", "pimStarGRPFRouteAddress"),
        ("PIM-STD-MIB", "pimStarGRPFRoutePrefixLength"),
        ("PIM-STD-MIB", "pimStarGRPFRouteMetricPref"),
        ("PIM-STD-MIB", "pimStarGRPFRouteMetric"),
        ("PIM-STD-MIB", "pimStarGIUpTime"),
        ("PIM-STD-MIB", "pimStarGILocalMembership"),
        ("PIM-STD-MIB", "pimStarGIJoinPruneState"),
        ("PIM-STD-MIB", "pimStarGIPrunePendingTimer"),
        ("PIM-STD-MIB", "pimStarGIJoinExpiryTimer"),
        ("PIM-STD-MIB", "pimStarGIAssertState"),
        ("PIM-STD-MIB", "pimStarGIAssertTimer"),
        ("PIM-STD-MIB", "pimStarGIAssertWinnerAddressType"),
        ("PIM-STD-MIB", "pimStarGIAssertWinnerAddress"),
        ("PIM-STD-MIB", "pimStarGIAssertWinnerMetricPref"),
        ("PIM-STD-MIB", "pimStarGIAssertWinnerMetric"),
        ("PIM-STD-MIB", "pimSGRptUpTime"),
        ("PIM-STD-MIB", "pimSGRptUpstreamPruneState"),
        ("PIM-STD-MIB", "pimSGRptUpstreamOverrideTimer"),
        ("PIM-STD-MIB", "pimSGRptIUpTime"),
        ("PIM-STD-MIB", "pimSGRptILocalMembership"),
        ("PIM-STD-MIB", "pimSGRptIJoinPruneState"),
        ("PIM-STD-MIB", "pimSGRptIPrunePendingTimer"),
        ("PIM-STD-MIB", "pimSGRptIPruneExpiryTimer"))
)
if mibBuilder.loadTexts:
    pimSmGroup.setStatus("current")

pimBidirGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 8)
)
pimBidirGroup.setObjects(
      *(("PIM-STD-MIB", "pimInterfaceDFElectionRobustness"),
        ("PIM-STD-MIB", "pimBidirDFElectionWinnerAddressType"),
        ("PIM-STD-MIB", "pimBidirDFElectionWinnerAddress"),
        ("PIM-STD-MIB", "pimBidirDFElectionWinnerUpTime"),
        ("PIM-STD-MIB", "pimBidirDFElectionWinnerMetricPref"),
        ("PIM-STD-MIB", "pimBidirDFElectionWinnerMetric"),
        ("PIM-STD-MIB", "pimBidirDFElectionState"),
        ("PIM-STD-MIB", "pimBidirDFElectionStateTimer"))
)
if mibBuilder.loadTexts:
    pimBidirGroup.setStatus("current")

pimAnycastRpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 9)
)
pimAnycastRpGroup.setObjects(
      *(("PIM-STD-MIB", "pimAnycastRPSetLocalRouter"),
        ("PIM-STD-MIB", "pimAnycastRPSetRowStatus"),
        ("PIM-STD-MIB", "pimAnycastRPSetStorageType"))
)
if mibBuilder.loadTexts:
    pimAnycastRpGroup.setStatus("current")

pimStaticRPPrecedenceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 10)
)
pimStaticRPPrecedenceGroup.setObjects(
    ("PIM-STD-MIB", "pimStaticRPPrecedence")
)
if mibBuilder.loadTexts:
    pimStaticRPPrecedenceGroup.setStatus("current")

pimNetMgmtNotificationObjects = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 11)
)
pimNetMgmtNotificationObjects.setObjects(
      *(("PIM-STD-MIB", "pimInvalidRegisterNotificationPeriod"),
        ("PIM-STD-MIB", "pimInvalidRegisterMsgsRcvd"),
        ("PIM-STD-MIB", "pimInvalidRegisterAddressType"),
        ("PIM-STD-MIB", "pimInvalidRegisterOrigin"),
        ("PIM-STD-MIB", "pimInvalidRegisterGroup"),
        ("PIM-STD-MIB", "pimInvalidRegisterRp"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneNotificationPeriod"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneMsgsRcvd"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneAddressType"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneOrigin"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneGroup"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneRp"),
        ("PIM-STD-MIB", "pimRPMappingNotificationPeriod"),
        ("PIM-STD-MIB", "pimRPMappingChangeCount"),
        ("PIM-STD-MIB", "pimInterfaceElectionNotificationPeriod"),
        ("PIM-STD-MIB", "pimInterfaceElectionWinCount"))
)
if mibBuilder.loadTexts:
    pimNetMgmtNotificationObjects.setStatus("current")

pimDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 13)
)
pimDiagnosticsGroup.setObjects(
      *(("PIM-STD-MIB", "pimInAsserts"),
        ("PIM-STD-MIB", "pimOutAsserts"),
        ("PIM-STD-MIB", "pimLastAssertInterface"),
        ("PIM-STD-MIB", "pimLastAssertGroupAddressType"),
        ("PIM-STD-MIB", "pimLastAssertGroupAddress"),
        ("PIM-STD-MIB", "pimLastAssertSourceAddressType"),
        ("PIM-STD-MIB", "pimLastAssertSourceAddress"),
        ("PIM-STD-MIB", "pimNeighborLossNotificationPeriod"),
        ("PIM-STD-MIB", "pimNeighborLossCount"))
)
if mibBuilder.loadTexts:
    pimDiagnosticsGroup.setStatus("current")

pimDmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 14)
)
pimDmGroup.setObjects(
      *(("PIM-STD-MIB", "pimRefreshInterval"),
        ("PIM-STD-MIB", "pimInterfacePruneLimitInterval"),
        ("PIM-STD-MIB", "pimInterfaceGraftRetryInterval"),
        ("PIM-STD-MIB", "pimInterfaceSRPriorityEnabled"),
        ("PIM-STD-MIB", "pimNeighborSRCapable"),
        ("PIM-STD-MIB", "pimSGUpstreamPruneState"),
        ("PIM-STD-MIB", "pimSGUpstreamPruneLimitTimer"),
        ("PIM-STD-MIB", "pimSGOriginatorState"),
        ("PIM-STD-MIB", "pimSGSourceActiveTimer"),
        ("PIM-STD-MIB", "pimSGStateRefreshTimer"))
)
if mibBuilder.loadTexts:
    pimDmGroup.setStatus("current")

pimDeviceStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 15)
)
pimDeviceStorageGroup.setObjects(
    ("PIM-STD-MIB", "pimDeviceConfigStorageType")
)
if mibBuilder.loadTexts:
    pimDeviceStorageGroup.setStatus("current")


# Notification objects

pimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 2, 1, 157, 0, 1)
)
pimNeighborLoss.setObjects(
    ("PIM-STD-MIB", "pimNeighborUpTime")
)
if mibBuilder.loadTexts:
    pimNeighborLoss.setStatus(
        "current"
    )

pimInvalidRegister = NotificationType(
    (1, 3, 6, 1, 2, 1, 157, 0, 2)
)
pimInvalidRegister.setObjects(
      *(("PIM-STD-MIB", "pimGroupMappingPimMode"),
        ("PIM-STD-MIB", "pimInvalidRegisterAddressType"),
        ("PIM-STD-MIB", "pimInvalidRegisterOrigin"),
        ("PIM-STD-MIB", "pimInvalidRegisterGroup"),
        ("PIM-STD-MIB", "pimInvalidRegisterRp"))
)
if mibBuilder.loadTexts:
    pimInvalidRegister.setStatus(
        "current"
    )

pimInvalidJoinPrune = NotificationType(
    (1, 3, 6, 1, 2, 1, 157, 0, 3)
)
pimInvalidJoinPrune.setObjects(
      *(("PIM-STD-MIB", "pimGroupMappingPimMode"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneAddressType"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneOrigin"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneGroup"),
        ("PIM-STD-MIB", "pimInvalidJoinPruneRp"),
        ("PIM-STD-MIB", "pimNeighborUpTime"))
)
if mibBuilder.loadTexts:
    pimInvalidJoinPrune.setStatus(
        "current"
    )

pimRPMappingChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 157, 0, 4)
)
pimRPMappingChange.setObjects(
      *(("PIM-STD-MIB", "pimGroupMappingPimMode"),
        ("PIM-STD-MIB", "pimGroupMappingPrecedence"))
)
if mibBuilder.loadTexts:
    pimRPMappingChange.setStatus(
        "current"
    )

pimInterfaceElection = NotificationType(
    (1, 3, 6, 1, 2, 1, 157, 0, 5)
)
pimInterfaceElection.setObjects(
      *(("PIM-STD-MIB", "pimInterfaceAddressType"),
        ("PIM-STD-MIB", "pimInterfaceAddress"))
)
if mibBuilder.loadTexts:
    pimInterfaceElection.setStatus(
        "current"
    )


# Notifications groups

pimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 2)
)
pimNotificationGroup.setObjects(
    ("PIM-STD-MIB", "pimNeighborLoss")
)
if mibBuilder.loadTexts:
    pimNotificationGroup.setStatus(
        "current"
    )

pimNetMgmtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 157, 2, 2, 12)
)
pimNetMgmtNotificationGroup.setObjects(
      *(("PIM-STD-MIB", "pimInvalidRegister"),
        ("PIM-STD-MIB", "pimInvalidJoinPrune"),
        ("PIM-STD-MIB", "pimRPMappingChange"),
        ("PIM-STD-MIB", "pimInterfaceElection"))
)
if mibBuilder.loadTexts:
    pimNetMgmtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pimMIBComplianceAsm = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 157, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pimMIBComplianceAsm.setStatus(
        "current"
    )

pimMIBComplianceBidir = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 157, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pimMIBComplianceBidir.setStatus(
        "current"
    )

pimMIBComplianceSsm = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 157, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pimMIBComplianceSsm.setStatus(
        "current"
    )

pimMIBComplianceDm = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 157, 2, 1, 4)
)
if mibBuilder.loadTexts:
    pimMIBComplianceDm.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIM-STD-MIB",
    **{"PimMode": PimMode,
       "PimGroupMappingOriginType": PimGroupMappingOriginType,
       "pimStdMIB": pimStdMIB,
       "pimNotifications": pimNotifications,
       "pimNeighborLoss": pimNeighborLoss,
       "pimInvalidRegister": pimInvalidRegister,
       "pimInvalidJoinPrune": pimInvalidJoinPrune,
       "pimRPMappingChange": pimRPMappingChange,
       "pimInterfaceElection": pimInterfaceElection,
       "pim": pim,
       "pimInterfaceTable": pimInterfaceTable,
       "pimInterfaceEntry": pimInterfaceEntry,
       "pimInterfaceIfIndex": pimInterfaceIfIndex,
       "pimInterfaceIPVersion": pimInterfaceIPVersion,
       "pimInterfaceAddressType": pimInterfaceAddressType,
       "pimInterfaceAddress": pimInterfaceAddress,
       "pimInterfaceGenerationIDValue": pimInterfaceGenerationIDValue,
       "pimInterfaceDR": pimInterfaceDR,
       "pimInterfaceDRPriority": pimInterfaceDRPriority,
       "pimInterfaceDRPriorityEnabled": pimInterfaceDRPriorityEnabled,
       "pimInterfaceHelloInterval": pimInterfaceHelloInterval,
       "pimInterfaceTrigHelloInterval": pimInterfaceTrigHelloInterval,
       "pimInterfaceHelloHoldtime": pimInterfaceHelloHoldtime,
       "pimInterfaceJoinPruneInterval": pimInterfaceJoinPruneInterval,
       "pimInterfaceJoinPruneHoldtime": pimInterfaceJoinPruneHoldtime,
       "pimInterfaceDFElectionRobustness": pimInterfaceDFElectionRobustness,
       "pimInterfaceLanDelayEnabled": pimInterfaceLanDelayEnabled,
       "pimInterfacePropagationDelay": pimInterfacePropagationDelay,
       "pimInterfaceOverrideInterval": pimInterfaceOverrideInterval,
       "pimInterfaceEffectPropagDelay": pimInterfaceEffectPropagDelay,
       "pimInterfaceEffectOverrideIvl": pimInterfaceEffectOverrideIvl,
       "pimInterfaceSuppressionEnabled": pimInterfaceSuppressionEnabled,
       "pimInterfaceBidirCapable": pimInterfaceBidirCapable,
       "pimInterfaceDomainBorder": pimInterfaceDomainBorder,
       "pimInterfaceStubInterface": pimInterfaceStubInterface,
       "pimInterfacePruneLimitInterval": pimInterfacePruneLimitInterval,
       "pimInterfaceGraftRetryInterval": pimInterfaceGraftRetryInterval,
       "pimInterfaceSRPriorityEnabled": pimInterfaceSRPriorityEnabled,
       "pimInterfaceStatus": pimInterfaceStatus,
       "pimInterfaceStorageType": pimInterfaceStorageType,
       "pimNeighborTable": pimNeighborTable,
       "pimNeighborEntry": pimNeighborEntry,
       "pimNeighborIfIndex": pimNeighborIfIndex,
       "pimNeighborAddressType": pimNeighborAddressType,
       "pimNeighborAddress": pimNeighborAddress,
       "pimNeighborGenerationIDPresent": pimNeighborGenerationIDPresent,
       "pimNeighborGenerationIDValue": pimNeighborGenerationIDValue,
       "pimNeighborUpTime": pimNeighborUpTime,
       "pimNeighborExpiryTime": pimNeighborExpiryTime,
       "pimNeighborDRPriorityPresent": pimNeighborDRPriorityPresent,
       "pimNeighborDRPriority": pimNeighborDRPriority,
       "pimNeighborLanPruneDelayPresent": pimNeighborLanPruneDelayPresent,
       "pimNeighborTBit": pimNeighborTBit,
       "pimNeighborPropagationDelay": pimNeighborPropagationDelay,
       "pimNeighborOverrideInterval": pimNeighborOverrideInterval,
       "pimNeighborBidirCapable": pimNeighborBidirCapable,
       "pimNeighborSRCapable": pimNeighborSRCapable,
       "pimNbrSecAddressTable": pimNbrSecAddressTable,
       "pimNbrSecAddressEntry": pimNbrSecAddressEntry,
       "pimNbrSecAddressIfIndex": pimNbrSecAddressIfIndex,
       "pimNbrSecAddressType": pimNbrSecAddressType,
       "pimNbrSecAddressPrimary": pimNbrSecAddressPrimary,
       "pimNbrSecAddress": pimNbrSecAddress,
       "pimStarGTable": pimStarGTable,
       "pimStarGEntry": pimStarGEntry,
       "pimStarGAddressType": pimStarGAddressType,
       "pimStarGGrpAddress": pimStarGGrpAddress,
       "pimStarGUpTime": pimStarGUpTime,
       "pimStarGPimMode": pimStarGPimMode,
       "pimStarGRPAddressType": pimStarGRPAddressType,
       "pimStarGRPAddress": pimStarGRPAddress,
       "pimStarGPimModeOrigin": pimStarGPimModeOrigin,
       "pimStarGRPIsLocal": pimStarGRPIsLocal,
       "pimStarGUpstreamJoinState": pimStarGUpstreamJoinState,
       "pimStarGUpstreamJoinTimer": pimStarGUpstreamJoinTimer,
       "pimStarGUpstreamNeighborType": pimStarGUpstreamNeighborType,
       "pimStarGUpstreamNeighbor": pimStarGUpstreamNeighbor,
       "pimStarGRPFIfIndex": pimStarGRPFIfIndex,
       "pimStarGRPFNextHopType": pimStarGRPFNextHopType,
       "pimStarGRPFNextHop": pimStarGRPFNextHop,
       "pimStarGRPFRouteProtocol": pimStarGRPFRouteProtocol,
       "pimStarGRPFRouteAddress": pimStarGRPFRouteAddress,
       "pimStarGRPFRoutePrefixLength": pimStarGRPFRoutePrefixLength,
       "pimStarGRPFRouteMetricPref": pimStarGRPFRouteMetricPref,
       "pimStarGRPFRouteMetric": pimStarGRPFRouteMetric,
       "pimStarGITable": pimStarGITable,
       "pimStarGIEntry": pimStarGIEntry,
       "pimStarGIIfIndex": pimStarGIIfIndex,
       "pimStarGIUpTime": pimStarGIUpTime,
       "pimStarGILocalMembership": pimStarGILocalMembership,
       "pimStarGIJoinPruneState": pimStarGIJoinPruneState,
       "pimStarGIPrunePendingTimer": pimStarGIPrunePendingTimer,
       "pimStarGIJoinExpiryTimer": pimStarGIJoinExpiryTimer,
       "pimStarGIAssertState": pimStarGIAssertState,
       "pimStarGIAssertTimer": pimStarGIAssertTimer,
       "pimStarGIAssertWinnerAddressType": pimStarGIAssertWinnerAddressType,
       "pimStarGIAssertWinnerAddress": pimStarGIAssertWinnerAddress,
       "pimStarGIAssertWinnerMetricPref": pimStarGIAssertWinnerMetricPref,
       "pimStarGIAssertWinnerMetric": pimStarGIAssertWinnerMetric,
       "pimSGTable": pimSGTable,
       "pimSGEntry": pimSGEntry,
       "pimSGAddressType": pimSGAddressType,
       "pimSGGrpAddress": pimSGGrpAddress,
       "pimSGSrcAddress": pimSGSrcAddress,
       "pimSGUpTime": pimSGUpTime,
       "pimSGPimMode": pimSGPimMode,
       "pimSGUpstreamJoinState": pimSGUpstreamJoinState,
       "pimSGUpstreamJoinTimer": pimSGUpstreamJoinTimer,
       "pimSGUpstreamNeighbor": pimSGUpstreamNeighbor,
       "pimSGRPFIfIndex": pimSGRPFIfIndex,
       "pimSGRPFNextHopType": pimSGRPFNextHopType,
       "pimSGRPFNextHop": pimSGRPFNextHop,
       "pimSGRPFRouteProtocol": pimSGRPFRouteProtocol,
       "pimSGRPFRouteAddress": pimSGRPFRouteAddress,
       "pimSGRPFRoutePrefixLength": pimSGRPFRoutePrefixLength,
       "pimSGRPFRouteMetricPref": pimSGRPFRouteMetricPref,
       "pimSGRPFRouteMetric": pimSGRPFRouteMetric,
       "pimSGSPTBit": pimSGSPTBit,
       "pimSGKeepaliveTimer": pimSGKeepaliveTimer,
       "pimSGDRRegisterState": pimSGDRRegisterState,
       "pimSGDRRegisterStopTimer": pimSGDRRegisterStopTimer,
       "pimSGRPRegisterPMBRAddressType": pimSGRPRegisterPMBRAddressType,
       "pimSGRPRegisterPMBRAddress": pimSGRPRegisterPMBRAddress,
       "pimSGUpstreamPruneState": pimSGUpstreamPruneState,
       "pimSGUpstreamPruneLimitTimer": pimSGUpstreamPruneLimitTimer,
       "pimSGOriginatorState": pimSGOriginatorState,
       "pimSGSourceActiveTimer": pimSGSourceActiveTimer,
       "pimSGStateRefreshTimer": pimSGStateRefreshTimer,
       "pimSGITable": pimSGITable,
       "pimSGIEntry": pimSGIEntry,
       "pimSGIIfIndex": pimSGIIfIndex,
       "pimSGIUpTime": pimSGIUpTime,
       "pimSGILocalMembership": pimSGILocalMembership,
       "pimSGIJoinPruneState": pimSGIJoinPruneState,
       "pimSGIPrunePendingTimer": pimSGIPrunePendingTimer,
       "pimSGIJoinExpiryTimer": pimSGIJoinExpiryTimer,
       "pimSGIAssertState": pimSGIAssertState,
       "pimSGIAssertTimer": pimSGIAssertTimer,
       "pimSGIAssertWinnerAddressType": pimSGIAssertWinnerAddressType,
       "pimSGIAssertWinnerAddress": pimSGIAssertWinnerAddress,
       "pimSGIAssertWinnerMetricPref": pimSGIAssertWinnerMetricPref,
       "pimSGIAssertWinnerMetric": pimSGIAssertWinnerMetric,
       "pimSGRptTable": pimSGRptTable,
       "pimSGRptEntry": pimSGRptEntry,
       "pimSGRptSrcAddress": pimSGRptSrcAddress,
       "pimSGRptUpTime": pimSGRptUpTime,
       "pimSGRptUpstreamPruneState": pimSGRptUpstreamPruneState,
       "pimSGRptUpstreamOverrideTimer": pimSGRptUpstreamOverrideTimer,
       "pimSGRptITable": pimSGRptITable,
       "pimSGRptIEntry": pimSGRptIEntry,
       "pimSGRptIIfIndex": pimSGRptIIfIndex,
       "pimSGRptIUpTime": pimSGRptIUpTime,
       "pimSGRptILocalMembership": pimSGRptILocalMembership,
       "pimSGRptIJoinPruneState": pimSGRptIJoinPruneState,
       "pimSGRptIPrunePendingTimer": pimSGRptIPrunePendingTimer,
       "pimSGRptIPruneExpiryTimer": pimSGRptIPruneExpiryTimer,
       "pimBidirDFElectionTable": pimBidirDFElectionTable,
       "pimBidirDFElectionEntry": pimBidirDFElectionEntry,
       "pimBidirDFElectionAddressType": pimBidirDFElectionAddressType,
       "pimBidirDFElectionRPAddress": pimBidirDFElectionRPAddress,
       "pimBidirDFElectionIfIndex": pimBidirDFElectionIfIndex,
       "pimBidirDFElectionWinnerAddressType": pimBidirDFElectionWinnerAddressType,
       "pimBidirDFElectionWinnerAddress": pimBidirDFElectionWinnerAddress,
       "pimBidirDFElectionWinnerUpTime": pimBidirDFElectionWinnerUpTime,
       "pimBidirDFElectionWinnerMetricPref": pimBidirDFElectionWinnerMetricPref,
       "pimBidirDFElectionWinnerMetric": pimBidirDFElectionWinnerMetric,
       "pimBidirDFElectionState": pimBidirDFElectionState,
       "pimBidirDFElectionStateTimer": pimBidirDFElectionStateTimer,
       "pimStaticRPTable": pimStaticRPTable,
       "pimStaticRPEntry": pimStaticRPEntry,
       "pimStaticRPAddressType": pimStaticRPAddressType,
       "pimStaticRPGrpAddress": pimStaticRPGrpAddress,
       "pimStaticRPGrpPrefixLength": pimStaticRPGrpPrefixLength,
       "pimStaticRPRPAddress": pimStaticRPRPAddress,
       "pimStaticRPPimMode": pimStaticRPPimMode,
       "pimStaticRPOverrideDynamic": pimStaticRPOverrideDynamic,
       "pimStaticRPPrecedence": pimStaticRPPrecedence,
       "pimStaticRPRowStatus": pimStaticRPRowStatus,
       "pimStaticRPStorageType": pimStaticRPStorageType,
       "pimAnycastRPSetTable": pimAnycastRPSetTable,
       "pimAnycastRPSetEntry": pimAnycastRPSetEntry,
       "pimAnycastRPSetAddressType": pimAnycastRPSetAddressType,
       "pimAnycastRPSetAnycastAddress": pimAnycastRPSetAnycastAddress,
       "pimAnycastRPSetRouterAddress": pimAnycastRPSetRouterAddress,
       "pimAnycastRPSetLocalRouter": pimAnycastRPSetLocalRouter,
       "pimAnycastRPSetRowStatus": pimAnycastRPSetRowStatus,
       "pimAnycastRPSetStorageType": pimAnycastRPSetStorageType,
       "pimGroupMappingTable": pimGroupMappingTable,
       "pimGroupMappingEntry": pimGroupMappingEntry,
       "pimGroupMappingOrigin": pimGroupMappingOrigin,
       "pimGroupMappingAddressType": pimGroupMappingAddressType,
       "pimGroupMappingGrpAddress": pimGroupMappingGrpAddress,
       "pimGroupMappingGrpPrefixLength": pimGroupMappingGrpPrefixLength,
       "pimGroupMappingRPAddressType": pimGroupMappingRPAddressType,
       "pimGroupMappingRPAddress": pimGroupMappingRPAddress,
       "pimGroupMappingPimMode": pimGroupMappingPimMode,
       "pimGroupMappingPrecedence": pimGroupMappingPrecedence,
       "pimKeepalivePeriod": pimKeepalivePeriod,
       "pimRegisterSuppressionTime": pimRegisterSuppressionTime,
       "pimStarGEntries": pimStarGEntries,
       "pimStarGIEntries": pimStarGIEntries,
       "pimSGEntries": pimSGEntries,
       "pimSGIEntries": pimSGIEntries,
       "pimSGRptEntries": pimSGRptEntries,
       "pimSGRptIEntries": pimSGRptIEntries,
       "pimOutAsserts": pimOutAsserts,
       "pimInAsserts": pimInAsserts,
       "pimLastAssertInterface": pimLastAssertInterface,
       "pimLastAssertGroupAddressType": pimLastAssertGroupAddressType,
       "pimLastAssertGroupAddress": pimLastAssertGroupAddress,
       "pimLastAssertSourceAddressType": pimLastAssertSourceAddressType,
       "pimLastAssertSourceAddress": pimLastAssertSourceAddress,
       "pimNeighborLossNotificationPeriod": pimNeighborLossNotificationPeriod,
       "pimNeighborLossCount": pimNeighborLossCount,
       "pimInvalidRegisterNotificationPeriod": pimInvalidRegisterNotificationPeriod,
       "pimInvalidRegisterMsgsRcvd": pimInvalidRegisterMsgsRcvd,
       "pimInvalidRegisterAddressType": pimInvalidRegisterAddressType,
       "pimInvalidRegisterOrigin": pimInvalidRegisterOrigin,
       "pimInvalidRegisterGroup": pimInvalidRegisterGroup,
       "pimInvalidRegisterRp": pimInvalidRegisterRp,
       "pimInvalidJoinPruneNotificationPeriod": pimInvalidJoinPruneNotificationPeriod,
       "pimInvalidJoinPruneMsgsRcvd": pimInvalidJoinPruneMsgsRcvd,
       "pimInvalidJoinPruneAddressType": pimInvalidJoinPruneAddressType,
       "pimInvalidJoinPruneOrigin": pimInvalidJoinPruneOrigin,
       "pimInvalidJoinPruneGroup": pimInvalidJoinPruneGroup,
       "pimInvalidJoinPruneRp": pimInvalidJoinPruneRp,
       "pimRPMappingNotificationPeriod": pimRPMappingNotificationPeriod,
       "pimRPMappingChangeCount": pimRPMappingChangeCount,
       "pimInterfaceElectionNotificationPeriod": pimInterfaceElectionNotificationPeriod,
       "pimInterfaceElectionWinCount": pimInterfaceElectionWinCount,
       "pimRefreshInterval": pimRefreshInterval,
       "pimDeviceConfigStorageType": pimDeviceConfigStorageType,
       "pimMIBConformance": pimMIBConformance,
       "pimMIBCompliances": pimMIBCompliances,
       "pimMIBComplianceAsm": pimMIBComplianceAsm,
       "pimMIBComplianceBidir": pimMIBComplianceBidir,
       "pimMIBComplianceSsm": pimMIBComplianceSsm,
       "pimMIBComplianceDm": pimMIBComplianceDm,
       "pimMIBGroups": pimMIBGroups,
       "pimTopologyGroup": pimTopologyGroup,
       "pimNotificationGroup": pimNotificationGroup,
       "pimTuningParametersGroup": pimTuningParametersGroup,
       "pimRouterStatisticsGroup": pimRouterStatisticsGroup,
       "pimSsmGroup": pimSsmGroup,
       "pimRPConfigGroup": pimRPConfigGroup,
       "pimSmGroup": pimSmGroup,
       "pimBidirGroup": pimBidirGroup,
       "pimAnycastRpGroup": pimAnycastRpGroup,
       "pimStaticRPPrecedenceGroup": pimStaticRPPrecedenceGroup,
       "pimNetMgmtNotificationObjects": pimNetMgmtNotificationObjects,
       "pimNetMgmtNotificationGroup": pimNetMgmtNotificationGroup,
       "pimDiagnosticsGroup": pimDiagnosticsGroup,
       "pimDmGroup": pimDmGroup,
       "pimDeviceStorageGroup": pimDeviceStorageGroup}
)
