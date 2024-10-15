# SNMP MIB module (ALCATEL-IND1-PIM-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-PIM-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:45 2024
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

(routingIND1Pim,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Pim")

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

alaPimStdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2)
)
alaPimStdMIB.setRevisions(
        ("2007-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaPimMode(Integer32, TextualConvention):
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



class AlaPimGroupMappingOriginType(Integer32, TextualConvention):
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

_AlaPimNotifications_ObjectIdentity = ObjectIdentity
alaPimNotifications = _AlaPimNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0)
)
_AlaPim_ObjectIdentity = ObjectIdentity
alaPim = _AlaPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1)
)
_AlaPimInterfaceTable_Object = MibTable
alaPimInterfaceTable = _AlaPimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaPimInterfaceTable.setStatus("current")
_AlaPimInterfaceEntry_Object = MibTableRow
alaPimInterfaceEntry = _AlaPimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1)
)
alaPimInterfaceEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceIfIndex"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceIPVersion"),
)
if mibBuilder.loadTexts:
    alaPimInterfaceEntry.setStatus("current")
_AlaPimInterfaceIfIndex_Type = InterfaceIndex
_AlaPimInterfaceIfIndex_Object = MibTableColumn
alaPimInterfaceIfIndex = _AlaPimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 1),
    _AlaPimInterfaceIfIndex_Type()
)
alaPimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimInterfaceIfIndex.setStatus("current")
_AlaPimInterfaceIPVersion_Type = InetVersion
_AlaPimInterfaceIPVersion_Object = MibTableColumn
alaPimInterfaceIPVersion = _AlaPimInterfaceIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 2),
    _AlaPimInterfaceIPVersion_Type()
)
alaPimInterfaceIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimInterfaceIPVersion.setStatus("current")
_AlaPimInterfaceAddressType_Type = InetAddressType
_AlaPimInterfaceAddressType_Object = MibTableColumn
alaPimInterfaceAddressType = _AlaPimInterfaceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 3),
    _AlaPimInterfaceAddressType_Type()
)
alaPimInterfaceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceAddressType.setStatus("current")


class _AlaPimInterfaceAddress_Type(InetAddress):
    """Custom type alaPimInterfaceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInterfaceAddress_Type.__name__ = "InetAddress"
_AlaPimInterfaceAddress_Object = MibTableColumn
alaPimInterfaceAddress = _AlaPimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 4),
    _AlaPimInterfaceAddress_Type()
)
alaPimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceAddress.setStatus("current")
_AlaPimInterfaceGenerationIDValue_Type = Unsigned32
_AlaPimInterfaceGenerationIDValue_Object = MibTableColumn
alaPimInterfaceGenerationIDValue = _AlaPimInterfaceGenerationIDValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 5),
    _AlaPimInterfaceGenerationIDValue_Type()
)
alaPimInterfaceGenerationIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceGenerationIDValue.setStatus("current")


class _AlaPimInterfaceDR_Type(InetAddress):
    """Custom type alaPimInterfaceDR based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInterfaceDR_Type.__name__ = "InetAddress"
_AlaPimInterfaceDR_Object = MibTableColumn
alaPimInterfaceDR = _AlaPimInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 6),
    _AlaPimInterfaceDR_Type()
)
alaPimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceDR.setStatus("current")


class _AlaPimInterfaceDRPriority_Type(Unsigned32):
    """Custom type alaPimInterfaceDRPriority based on Unsigned32"""
    defaultValue = 1


_AlaPimInterfaceDRPriority_Object = MibTableColumn
alaPimInterfaceDRPriority = _AlaPimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 7),
    _AlaPimInterfaceDRPriority_Type()
)
alaPimInterfaceDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceDRPriority.setStatus("current")
_AlaPimInterfaceDRPriorityEnabled_Type = TruthValue
_AlaPimInterfaceDRPriorityEnabled_Object = MibTableColumn
alaPimInterfaceDRPriorityEnabled = _AlaPimInterfaceDRPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 8),
    _AlaPimInterfaceDRPriorityEnabled_Type()
)
alaPimInterfaceDRPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceDRPriorityEnabled.setStatus("current")


class _AlaPimInterfaceHelloInterval_Type(Unsigned32):
    """Custom type alaPimInterfaceHelloInterval based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AlaPimInterfaceHelloInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfaceHelloInterval_Object = MibTableColumn
alaPimInterfaceHelloInterval = _AlaPimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 9),
    _AlaPimInterfaceHelloInterval_Type()
)
alaPimInterfaceHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceHelloInterval.setUnits("seconds")


class _AlaPimInterfaceTrigHelloInterval_Type(Unsigned32):
    """Custom type alaPimInterfaceTrigHelloInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AlaPimInterfaceTrigHelloInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfaceTrigHelloInterval_Object = MibTableColumn
alaPimInterfaceTrigHelloInterval = _AlaPimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 10),
    _AlaPimInterfaceTrigHelloInterval_Type()
)
alaPimInterfaceTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceTrigHelloInterval.setUnits("seconds")


class _AlaPimInterfaceHelloHoldtime_Type(Unsigned32):
    """Custom type alaPimInterfaceHelloHoldtime based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceHelloHoldtime_Type.__name__ = "Unsigned32"
_AlaPimInterfaceHelloHoldtime_Object = MibTableColumn
alaPimInterfaceHelloHoldtime = _AlaPimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 11),
    _AlaPimInterfaceHelloHoldtime_Type()
)
alaPimInterfaceHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceHelloHoldtime.setUnits("seconds")


class _AlaPimInterfaceJoinPruneInterval_Type(Unsigned32):
    """Custom type alaPimInterfaceJoinPruneInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18000),
    )


_AlaPimInterfaceJoinPruneInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfaceJoinPruneInterval_Object = MibTableColumn
alaPimInterfaceJoinPruneInterval = _AlaPimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 12),
    _AlaPimInterfaceJoinPruneInterval_Type()
)
alaPimInterfaceJoinPruneInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceJoinPruneInterval.setUnits("seconds")


class _AlaPimInterfaceJoinPruneHoldtime_Type(Unsigned32):
    """Custom type alaPimInterfaceJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceJoinPruneHoldtime_Type.__name__ = "Unsigned32"
_AlaPimInterfaceJoinPruneHoldtime_Object = MibTableColumn
alaPimInterfaceJoinPruneHoldtime = _AlaPimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 13),
    _AlaPimInterfaceJoinPruneHoldtime_Type()
)
alaPimInterfaceJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _AlaPimInterfaceDFElectionRobustness_Type(Unsigned32):
    """Custom type alaPimInterfaceDFElectionRobustness based on Unsigned32"""
    defaultValue = 3


_AlaPimInterfaceDFElectionRobustness_Object = MibTableColumn
alaPimInterfaceDFElectionRobustness = _AlaPimInterfaceDFElectionRobustness_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 14),
    _AlaPimInterfaceDFElectionRobustness_Type()
)
alaPimInterfaceDFElectionRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceDFElectionRobustness.setStatus("current")
_AlaPimInterfaceLanDelayEnabled_Type = TruthValue
_AlaPimInterfaceLanDelayEnabled_Object = MibTableColumn
alaPimInterfaceLanDelayEnabled = _AlaPimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 15),
    _AlaPimInterfaceLanDelayEnabled_Type()
)
alaPimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceLanDelayEnabled.setStatus("current")


class _AlaPimInterfacePropagationDelay_Type(Unsigned32):
    """Custom type alaPimInterfacePropagationDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AlaPimInterfacePropagationDelay_Type.__name__ = "Unsigned32"
_AlaPimInterfacePropagationDelay_Object = MibTableColumn
alaPimInterfacePropagationDelay = _AlaPimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 16),
    _AlaPimInterfacePropagationDelay_Type()
)
alaPimInterfacePropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfacePropagationDelay.setUnits("milliseconds")


class _AlaPimInterfaceOverrideInterval_Type(Unsigned32):
    """Custom type alaPimInterfaceOverrideInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceOverrideInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfaceOverrideInterval_Object = MibTableColumn
alaPimInterfaceOverrideInterval = _AlaPimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 17),
    _AlaPimInterfaceOverrideInterval_Type()
)
alaPimInterfaceOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceOverrideInterval.setUnits("milliseconds")


class _AlaPimInterfaceEffectPropagDelay_Type(Unsigned32):
    """Custom type alaPimInterfaceEffectPropagDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AlaPimInterfaceEffectPropagDelay_Type.__name__ = "Unsigned32"
_AlaPimInterfaceEffectPropagDelay_Object = MibTableColumn
alaPimInterfaceEffectPropagDelay = _AlaPimInterfaceEffectPropagDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 18),
    _AlaPimInterfaceEffectPropagDelay_Type()
)
alaPimInterfaceEffectPropagDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceEffectPropagDelay.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceEffectPropagDelay.setUnits("milliseconds")


class _AlaPimInterfaceEffectOverrideIvl_Type(Unsigned32):
    """Custom type alaPimInterfaceEffectOverrideIvl based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceEffectOverrideIvl_Type.__name__ = "Unsigned32"
_AlaPimInterfaceEffectOverrideIvl_Object = MibTableColumn
alaPimInterfaceEffectOverrideIvl = _AlaPimInterfaceEffectOverrideIvl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 19),
    _AlaPimInterfaceEffectOverrideIvl_Type()
)
alaPimInterfaceEffectOverrideIvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceEffectOverrideIvl.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceEffectOverrideIvl.setUnits("milliseconds")
_AlaPimInterfaceSuppressionEnabled_Type = TruthValue
_AlaPimInterfaceSuppressionEnabled_Object = MibTableColumn
alaPimInterfaceSuppressionEnabled = _AlaPimInterfaceSuppressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 20),
    _AlaPimInterfaceSuppressionEnabled_Type()
)
alaPimInterfaceSuppressionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceSuppressionEnabled.setStatus("current")
_AlaPimInterfaceBidirCapable_Type = TruthValue
_AlaPimInterfaceBidirCapable_Object = MibTableColumn
alaPimInterfaceBidirCapable = _AlaPimInterfaceBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 21),
    _AlaPimInterfaceBidirCapable_Type()
)
alaPimInterfaceBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceBidirCapable.setStatus("current")


class _AlaPimInterfaceDomainBorder_Type(TruthValue):
    """Custom type alaPimInterfaceDomainBorder based on TruthValue"""


_AlaPimInterfaceDomainBorder_Object = MibTableColumn
alaPimInterfaceDomainBorder = _AlaPimInterfaceDomainBorder_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 22),
    _AlaPimInterfaceDomainBorder_Type()
)
alaPimInterfaceDomainBorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceDomainBorder.setStatus("current")


class _AlaPimInterfaceStubInterface_Type(TruthValue):
    """Custom type alaPimInterfaceStubInterface based on TruthValue"""


_AlaPimInterfaceStubInterface_Object = MibTableColumn
alaPimInterfaceStubInterface = _AlaPimInterfaceStubInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 23),
    _AlaPimInterfaceStubInterface_Type()
)
alaPimInterfaceStubInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceStubInterface.setStatus("current")


class _AlaPimInterfacePruneLimitInterval_Type(Unsigned32):
    """Custom type alaPimInterfacePruneLimitInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfacePruneLimitInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfacePruneLimitInterval_Object = MibTableColumn
alaPimInterfacePruneLimitInterval = _AlaPimInterfacePruneLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 24),
    _AlaPimInterfacePruneLimitInterval_Type()
)
alaPimInterfacePruneLimitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfacePruneLimitInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfacePruneLimitInterval.setUnits("seconds")


class _AlaPimInterfaceGraftRetryInterval_Type(Unsigned32):
    """Custom type alaPimInterfaceGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceGraftRetryInterval_Type.__name__ = "Unsigned32"
_AlaPimInterfaceGraftRetryInterval_Object = MibTableColumn
alaPimInterfaceGraftRetryInterval = _AlaPimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 25),
    _AlaPimInterfaceGraftRetryInterval_Type()
)
alaPimInterfaceGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceGraftRetryInterval.setUnits("seconds")
_AlaPimInterfaceSRPriorityEnabled_Type = TruthValue
_AlaPimInterfaceSRPriorityEnabled_Object = MibTableColumn
alaPimInterfaceSRPriorityEnabled = _AlaPimInterfaceSRPriorityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 26),
    _AlaPimInterfaceSRPriorityEnabled_Type()
)
alaPimInterfaceSRPriorityEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceSRPriorityEnabled.setStatus("current")
_AlaPimInterfaceStatus_Type = RowStatus
_AlaPimInterfaceStatus_Object = MibTableColumn
alaPimInterfaceStatus = _AlaPimInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 27),
    _AlaPimInterfaceStatus_Type()
)
alaPimInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceStatus.setStatus("current")


class _AlaPimInterfaceStorageType_Type(StorageType):
    """Custom type alaPimInterfaceStorageType based on StorageType"""


_AlaPimInterfaceStorageType_Object = MibTableColumn
alaPimInterfaceStorageType = _AlaPimInterfaceStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 1, 1, 28),
    _AlaPimInterfaceStorageType_Type()
)
alaPimInterfaceStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimInterfaceStorageType.setStatus("current")
_AlaPimNeighborTable_Object = MibTable
alaPimNeighborTable = _AlaPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    alaPimNeighborTable.setStatus("current")
_AlaPimNeighborEntry_Object = MibTableRow
alaPimNeighborEntry = _AlaPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1)
)
alaPimNeighborEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborIfIndex"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborAddress"),
)
if mibBuilder.loadTexts:
    alaPimNeighborEntry.setStatus("current")
_AlaPimNeighborIfIndex_Type = InterfaceIndex
_AlaPimNeighborIfIndex_Object = MibTableColumn
alaPimNeighborIfIndex = _AlaPimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 1),
    _AlaPimNeighborIfIndex_Type()
)
alaPimNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNeighborIfIndex.setStatus("current")
_AlaPimNeighborAddressType_Type = InetAddressType
_AlaPimNeighborAddressType_Object = MibTableColumn
alaPimNeighborAddressType = _AlaPimNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 2),
    _AlaPimNeighborAddressType_Type()
)
alaPimNeighborAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNeighborAddressType.setStatus("current")


class _AlaPimNeighborAddress_Type(InetAddress):
    """Custom type alaPimNeighborAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimNeighborAddress_Type.__name__ = "InetAddress"
_AlaPimNeighborAddress_Object = MibTableColumn
alaPimNeighborAddress = _AlaPimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 3),
    _AlaPimNeighborAddress_Type()
)
alaPimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNeighborAddress.setStatus("current")
_AlaPimNeighborGenerationIDPresent_Type = TruthValue
_AlaPimNeighborGenerationIDPresent_Object = MibTableColumn
alaPimNeighborGenerationIDPresent = _AlaPimNeighborGenerationIDPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 4),
    _AlaPimNeighborGenerationIDPresent_Type()
)
alaPimNeighborGenerationIDPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborGenerationIDPresent.setStatus("current")
_AlaPimNeighborGenerationIDValue_Type = Unsigned32
_AlaPimNeighborGenerationIDValue_Object = MibTableColumn
alaPimNeighborGenerationIDValue = _AlaPimNeighborGenerationIDValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 5),
    _AlaPimNeighborGenerationIDValue_Type()
)
alaPimNeighborGenerationIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborGenerationIDValue.setStatus("current")
_AlaPimNeighborUpTime_Type = TimeTicks
_AlaPimNeighborUpTime_Object = MibTableColumn
alaPimNeighborUpTime = _AlaPimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 6),
    _AlaPimNeighborUpTime_Type()
)
alaPimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborUpTime.setStatus("current")
_AlaPimNeighborExpiryTime_Type = TimeTicks
_AlaPimNeighborExpiryTime_Object = MibTableColumn
alaPimNeighborExpiryTime = _AlaPimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 7),
    _AlaPimNeighborExpiryTime_Type()
)
alaPimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborExpiryTime.setStatus("current")
_AlaPimNeighborDRPriorityPresent_Type = TruthValue
_AlaPimNeighborDRPriorityPresent_Object = MibTableColumn
alaPimNeighborDRPriorityPresent = _AlaPimNeighborDRPriorityPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 8),
    _AlaPimNeighborDRPriorityPresent_Type()
)
alaPimNeighborDRPriorityPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborDRPriorityPresent.setStatus("current")
_AlaPimNeighborDRPriority_Type = Unsigned32
_AlaPimNeighborDRPriority_Object = MibTableColumn
alaPimNeighborDRPriority = _AlaPimNeighborDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 9),
    _AlaPimNeighborDRPriority_Type()
)
alaPimNeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborDRPriority.setStatus("current")
_AlaPimNeighborLanPruneDelayPresent_Type = TruthValue
_AlaPimNeighborLanPruneDelayPresent_Object = MibTableColumn
alaPimNeighborLanPruneDelayPresent = _AlaPimNeighborLanPruneDelayPresent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 10),
    _AlaPimNeighborLanPruneDelayPresent_Type()
)
alaPimNeighborLanPruneDelayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborLanPruneDelayPresent.setStatus("current")
_AlaPimNeighborTBit_Type = TruthValue
_AlaPimNeighborTBit_Object = MibTableColumn
alaPimNeighborTBit = _AlaPimNeighborTBit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 11),
    _AlaPimNeighborTBit_Type()
)
alaPimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborTBit.setStatus("current")


class _AlaPimNeighborPropagationDelay_Type(Unsigned32):
    """Custom type alaPimNeighborPropagationDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AlaPimNeighborPropagationDelay_Type.__name__ = "Unsigned32"
_AlaPimNeighborPropagationDelay_Object = MibTableColumn
alaPimNeighborPropagationDelay = _AlaPimNeighborPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 12),
    _AlaPimNeighborPropagationDelay_Type()
)
alaPimNeighborPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborPropagationDelay.setStatus("current")


class _AlaPimNeighborOverrideInterval_Type(Unsigned32):
    """Custom type alaPimNeighborOverrideInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimNeighborOverrideInterval_Type.__name__ = "Unsigned32"
_AlaPimNeighborOverrideInterval_Object = MibTableColumn
alaPimNeighborOverrideInterval = _AlaPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 13),
    _AlaPimNeighborOverrideInterval_Type()
)
alaPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborOverrideInterval.setStatus("current")
_AlaPimNeighborBidirCapable_Type = TruthValue
_AlaPimNeighborBidirCapable_Object = MibTableColumn
alaPimNeighborBidirCapable = _AlaPimNeighborBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 14),
    _AlaPimNeighborBidirCapable_Type()
)
alaPimNeighborBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborBidirCapable.setStatus("current")
_AlaPimNeighborSRCapable_Type = TruthValue
_AlaPimNeighborSRCapable_Object = MibTableColumn
alaPimNeighborSRCapable = _AlaPimNeighborSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 2, 1, 15),
    _AlaPimNeighborSRCapable_Type()
)
alaPimNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborSRCapable.setStatus("current")
_AlaPimNbrSecAddressTable_Object = MibTable
alaPimNbrSecAddressTable = _AlaPimNbrSecAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alaPimNbrSecAddressTable.setStatus("current")
_AlaPimNbrSecAddressEntry_Object = MibTableRow
alaPimNbrSecAddressEntry = _AlaPimNbrSecAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3, 1)
)
alaPimNbrSecAddressEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNbrSecAddressIfIndex"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNbrSecAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNbrSecAddressPrimary"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimNbrSecAddress"),
)
if mibBuilder.loadTexts:
    alaPimNbrSecAddressEntry.setStatus("current")
_AlaPimNbrSecAddressIfIndex_Type = InterfaceIndex
_AlaPimNbrSecAddressIfIndex_Object = MibTableColumn
alaPimNbrSecAddressIfIndex = _AlaPimNbrSecAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3, 1, 1),
    _AlaPimNbrSecAddressIfIndex_Type()
)
alaPimNbrSecAddressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNbrSecAddressIfIndex.setStatus("current")
_AlaPimNbrSecAddressType_Type = InetAddressType
_AlaPimNbrSecAddressType_Object = MibTableColumn
alaPimNbrSecAddressType = _AlaPimNbrSecAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3, 1, 2),
    _AlaPimNbrSecAddressType_Type()
)
alaPimNbrSecAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNbrSecAddressType.setStatus("current")


class _AlaPimNbrSecAddressPrimary_Type(InetAddress):
    """Custom type alaPimNbrSecAddressPrimary based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimNbrSecAddressPrimary_Type.__name__ = "InetAddress"
_AlaPimNbrSecAddressPrimary_Object = MibTableColumn
alaPimNbrSecAddressPrimary = _AlaPimNbrSecAddressPrimary_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3, 1, 3),
    _AlaPimNbrSecAddressPrimary_Type()
)
alaPimNbrSecAddressPrimary.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimNbrSecAddressPrimary.setStatus("current")


class _AlaPimNbrSecAddress_Type(InetAddress):
    """Custom type alaPimNbrSecAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimNbrSecAddress_Type.__name__ = "InetAddress"
_AlaPimNbrSecAddress_Object = MibTableColumn
alaPimNbrSecAddress = _AlaPimNbrSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 3, 1, 4),
    _AlaPimNbrSecAddress_Type()
)
alaPimNbrSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNbrSecAddress.setStatus("current")
_AlaPimStarGTable_Object = MibTable
alaPimStarGTable = _AlaPimStarGTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alaPimStarGTable.setStatus("current")
_AlaPimStarGEntry_Object = MibTableRow
alaPimStarGEntry = _AlaPimStarGEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1)
)
alaPimStarGEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGGrpAddress"),
)
if mibBuilder.loadTexts:
    alaPimStarGEntry.setStatus("current")
_AlaPimStarGAddressType_Type = InetAddressType
_AlaPimStarGAddressType_Object = MibTableColumn
alaPimStarGAddressType = _AlaPimStarGAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 1),
    _AlaPimStarGAddressType_Type()
)
alaPimStarGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStarGAddressType.setStatus("current")


class _AlaPimStarGGrpAddress_Type(InetAddress):
    """Custom type alaPimStarGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGGrpAddress_Type.__name__ = "InetAddress"
_AlaPimStarGGrpAddress_Object = MibTableColumn
alaPimStarGGrpAddress = _AlaPimStarGGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 2),
    _AlaPimStarGGrpAddress_Type()
)
alaPimStarGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStarGGrpAddress.setStatus("current")
_AlaPimStarGUpTime_Type = TimeTicks
_AlaPimStarGUpTime_Object = MibTableColumn
alaPimStarGUpTime = _AlaPimStarGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 3),
    _AlaPimStarGUpTime_Type()
)
alaPimStarGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGUpTime.setStatus("current")
_AlaPimStarGPimMode_Type = AlaPimMode
_AlaPimStarGPimMode_Object = MibTableColumn
alaPimStarGPimMode = _AlaPimStarGPimMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 4),
    _AlaPimStarGPimMode_Type()
)
alaPimStarGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGPimMode.setStatus("current")
_AlaPimStarGRPAddressType_Type = InetAddressType
_AlaPimStarGRPAddressType_Object = MibTableColumn
alaPimStarGRPAddressType = _AlaPimStarGRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 5),
    _AlaPimStarGRPAddressType_Type()
)
alaPimStarGRPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPAddressType.setStatus("current")


class _AlaPimStarGRPAddress_Type(InetAddress):
    """Custom type alaPimStarGRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGRPAddress_Type.__name__ = "InetAddress"
_AlaPimStarGRPAddress_Object = MibTableColumn
alaPimStarGRPAddress = _AlaPimStarGRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 6),
    _AlaPimStarGRPAddress_Type()
)
alaPimStarGRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPAddress.setStatus("current")
_AlaPimStarGPimModeOrigin_Type = AlaPimGroupMappingOriginType
_AlaPimStarGPimModeOrigin_Object = MibTableColumn
alaPimStarGPimModeOrigin = _AlaPimStarGPimModeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 7),
    _AlaPimStarGPimModeOrigin_Type()
)
alaPimStarGPimModeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGPimModeOrigin.setStatus("current")
_AlaPimStarGRPIsLocal_Type = TruthValue
_AlaPimStarGRPIsLocal_Object = MibTableColumn
alaPimStarGRPIsLocal = _AlaPimStarGRPIsLocal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 8),
    _AlaPimStarGRPIsLocal_Type()
)
alaPimStarGRPIsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPIsLocal.setStatus("current")


class _AlaPimStarGUpstreamJoinState_Type(Integer32):
    """Custom type alaPimStarGUpstreamJoinState based on Integer32"""
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


_AlaPimStarGUpstreamJoinState_Type.__name__ = "Integer32"
_AlaPimStarGUpstreamJoinState_Object = MibTableColumn
alaPimStarGUpstreamJoinState = _AlaPimStarGUpstreamJoinState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 9),
    _AlaPimStarGUpstreamJoinState_Type()
)
alaPimStarGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGUpstreamJoinState.setStatus("current")
_AlaPimStarGUpstreamJoinTimer_Type = TimeTicks
_AlaPimStarGUpstreamJoinTimer_Object = MibTableColumn
alaPimStarGUpstreamJoinTimer = _AlaPimStarGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 10),
    _AlaPimStarGUpstreamJoinTimer_Type()
)
alaPimStarGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGUpstreamJoinTimer.setStatus("current")
_AlaPimStarGUpstreamNeighborType_Type = InetAddressType
_AlaPimStarGUpstreamNeighborType_Object = MibTableColumn
alaPimStarGUpstreamNeighborType = _AlaPimStarGUpstreamNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 11),
    _AlaPimStarGUpstreamNeighborType_Type()
)
alaPimStarGUpstreamNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGUpstreamNeighborType.setStatus("current")


class _AlaPimStarGUpstreamNeighbor_Type(InetAddress):
    """Custom type alaPimStarGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGUpstreamNeighbor_Type.__name__ = "InetAddress"
_AlaPimStarGUpstreamNeighbor_Object = MibTableColumn
alaPimStarGUpstreamNeighbor = _AlaPimStarGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 12),
    _AlaPimStarGUpstreamNeighbor_Type()
)
alaPimStarGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGUpstreamNeighbor.setStatus("current")
_AlaPimStarGRPFIfIndex_Type = InterfaceIndexOrZero
_AlaPimStarGRPFIfIndex_Object = MibTableColumn
alaPimStarGRPFIfIndex = _AlaPimStarGRPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 13),
    _AlaPimStarGRPFIfIndex_Type()
)
alaPimStarGRPFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFIfIndex.setStatus("current")
_AlaPimStarGRPFNextHopType_Type = InetAddressType
_AlaPimStarGRPFNextHopType_Object = MibTableColumn
alaPimStarGRPFNextHopType = _AlaPimStarGRPFNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 14),
    _AlaPimStarGRPFNextHopType_Type()
)
alaPimStarGRPFNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFNextHopType.setStatus("current")


class _AlaPimStarGRPFNextHop_Type(InetAddress):
    """Custom type alaPimStarGRPFNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGRPFNextHop_Type.__name__ = "InetAddress"
_AlaPimStarGRPFNextHop_Object = MibTableColumn
alaPimStarGRPFNextHop = _AlaPimStarGRPFNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 15),
    _AlaPimStarGRPFNextHop_Type()
)
alaPimStarGRPFNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFNextHop.setStatus("current")
_AlaPimStarGRPFRouteProtocol_Type = IANAipRouteProtocol
_AlaPimStarGRPFRouteProtocol_Object = MibTableColumn
alaPimStarGRPFRouteProtocol = _AlaPimStarGRPFRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 16),
    _AlaPimStarGRPFRouteProtocol_Type()
)
alaPimStarGRPFRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFRouteProtocol.setStatus("current")


class _AlaPimStarGRPFRouteAddress_Type(InetAddress):
    """Custom type alaPimStarGRPFRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGRPFRouteAddress_Type.__name__ = "InetAddress"
_AlaPimStarGRPFRouteAddress_Object = MibTableColumn
alaPimStarGRPFRouteAddress = _AlaPimStarGRPFRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 17),
    _AlaPimStarGRPFRouteAddress_Type()
)
alaPimStarGRPFRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFRouteAddress.setStatus("current")
_AlaPimStarGRPFRoutePrefixLength_Type = InetAddressPrefixLength
_AlaPimStarGRPFRoutePrefixLength_Object = MibTableColumn
alaPimStarGRPFRoutePrefixLength = _AlaPimStarGRPFRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 18),
    _AlaPimStarGRPFRoutePrefixLength_Type()
)
alaPimStarGRPFRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFRoutePrefixLength.setStatus("current")


class _AlaPimStarGRPFRouteMetricPref_Type(Unsigned32):
    """Custom type alaPimStarGRPFRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimStarGRPFRouteMetricPref_Type.__name__ = "Unsigned32"
_AlaPimStarGRPFRouteMetricPref_Object = MibTableColumn
alaPimStarGRPFRouteMetricPref = _AlaPimStarGRPFRouteMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 19),
    _AlaPimStarGRPFRouteMetricPref_Type()
)
alaPimStarGRPFRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFRouteMetricPref.setStatus("current")
_AlaPimStarGRPFRouteMetric_Type = Unsigned32
_AlaPimStarGRPFRouteMetric_Object = MibTableColumn
alaPimStarGRPFRouteMetric = _AlaPimStarGRPFRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 4, 1, 20),
    _AlaPimStarGRPFRouteMetric_Type()
)
alaPimStarGRPFRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGRPFRouteMetric.setStatus("current")
_AlaPimStarGITable_Object = MibTable
alaPimStarGITable = _AlaPimStarGITable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5)
)
if mibBuilder.loadTexts:
    alaPimStarGITable.setStatus("current")
_AlaPimStarGIEntry_Object = MibTableRow
alaPimStarGIEntry = _AlaPimStarGIEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1)
)
alaPimStarGIEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIIfIndex"),
)
if mibBuilder.loadTexts:
    alaPimStarGIEntry.setStatus("current")
_AlaPimStarGIIfIndex_Type = InterfaceIndex
_AlaPimStarGIIfIndex_Object = MibTableColumn
alaPimStarGIIfIndex = _AlaPimStarGIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 1),
    _AlaPimStarGIIfIndex_Type()
)
alaPimStarGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStarGIIfIndex.setStatus("current")
_AlaPimStarGIUpTime_Type = TimeTicks
_AlaPimStarGIUpTime_Object = MibTableColumn
alaPimStarGIUpTime = _AlaPimStarGIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 2),
    _AlaPimStarGIUpTime_Type()
)
alaPimStarGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIUpTime.setStatus("current")
_AlaPimStarGILocalMembership_Type = TruthValue
_AlaPimStarGILocalMembership_Object = MibTableColumn
alaPimStarGILocalMembership = _AlaPimStarGILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 3),
    _AlaPimStarGILocalMembership_Type()
)
alaPimStarGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGILocalMembership.setStatus("current")


class _AlaPimStarGIJoinPruneState_Type(Integer32):
    """Custom type alaPimStarGIJoinPruneState based on Integer32"""
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


_AlaPimStarGIJoinPruneState_Type.__name__ = "Integer32"
_AlaPimStarGIJoinPruneState_Object = MibTableColumn
alaPimStarGIJoinPruneState = _AlaPimStarGIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 4),
    _AlaPimStarGIJoinPruneState_Type()
)
alaPimStarGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIJoinPruneState.setStatus("current")
_AlaPimStarGIPrunePendingTimer_Type = TimeTicks
_AlaPimStarGIPrunePendingTimer_Object = MibTableColumn
alaPimStarGIPrunePendingTimer = _AlaPimStarGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 5),
    _AlaPimStarGIPrunePendingTimer_Type()
)
alaPimStarGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIPrunePendingTimer.setStatus("current")
_AlaPimStarGIJoinExpiryTimer_Type = TimeTicks
_AlaPimStarGIJoinExpiryTimer_Object = MibTableColumn
alaPimStarGIJoinExpiryTimer = _AlaPimStarGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 6),
    _AlaPimStarGIJoinExpiryTimer_Type()
)
alaPimStarGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIJoinExpiryTimer.setStatus("current")


class _AlaPimStarGIAssertState_Type(Integer32):
    """Custom type alaPimStarGIAssertState based on Integer32"""
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


_AlaPimStarGIAssertState_Type.__name__ = "Integer32"
_AlaPimStarGIAssertState_Object = MibTableColumn
alaPimStarGIAssertState = _AlaPimStarGIAssertState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 7),
    _AlaPimStarGIAssertState_Type()
)
alaPimStarGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertState.setStatus("current")
_AlaPimStarGIAssertTimer_Type = TimeTicks
_AlaPimStarGIAssertTimer_Object = MibTableColumn
alaPimStarGIAssertTimer = _AlaPimStarGIAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 8),
    _AlaPimStarGIAssertTimer_Type()
)
alaPimStarGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertTimer.setStatus("current")
_AlaPimStarGIAssertWinnerAddressType_Type = InetAddressType
_AlaPimStarGIAssertWinnerAddressType_Object = MibTableColumn
alaPimStarGIAssertWinnerAddressType = _AlaPimStarGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 9),
    _AlaPimStarGIAssertWinnerAddressType_Type()
)
alaPimStarGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertWinnerAddressType.setStatus("current")


class _AlaPimStarGIAssertWinnerAddress_Type(InetAddress):
    """Custom type alaPimStarGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStarGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_AlaPimStarGIAssertWinnerAddress_Object = MibTableColumn
alaPimStarGIAssertWinnerAddress = _AlaPimStarGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 10),
    _AlaPimStarGIAssertWinnerAddress_Type()
)
alaPimStarGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertWinnerAddress.setStatus("current")


class _AlaPimStarGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type alaPimStarGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimStarGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_AlaPimStarGIAssertWinnerMetricPref_Object = MibTableColumn
alaPimStarGIAssertWinnerMetricPref = _AlaPimStarGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 11),
    _AlaPimStarGIAssertWinnerMetricPref_Type()
)
alaPimStarGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertWinnerMetricPref.setStatus("current")
_AlaPimStarGIAssertWinnerMetric_Type = Unsigned32
_AlaPimStarGIAssertWinnerMetric_Object = MibTableColumn
alaPimStarGIAssertWinnerMetric = _AlaPimStarGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 5, 1, 12),
    _AlaPimStarGIAssertWinnerMetric_Type()
)
alaPimStarGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIAssertWinnerMetric.setStatus("current")
_AlaPimSGTable_Object = MibTable
alaPimSGTable = _AlaPimSGTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    alaPimSGTable.setStatus("current")
_AlaPimSGEntry_Object = MibTableRow
alaPimSGEntry = _AlaPimSGEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1)
)
alaPimSGEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGSrcAddress"),
)
if mibBuilder.loadTexts:
    alaPimSGEntry.setStatus("current")
_AlaPimSGAddressType_Type = InetAddressType
_AlaPimSGAddressType_Object = MibTableColumn
alaPimSGAddressType = _AlaPimSGAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 1),
    _AlaPimSGAddressType_Type()
)
alaPimSGAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGAddressType.setStatus("current")


class _AlaPimSGGrpAddress_Type(InetAddress):
    """Custom type alaPimSGGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGGrpAddress_Type.__name__ = "InetAddress"
_AlaPimSGGrpAddress_Object = MibTableColumn
alaPimSGGrpAddress = _AlaPimSGGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 2),
    _AlaPimSGGrpAddress_Type()
)
alaPimSGGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGGrpAddress.setStatus("current")


class _AlaPimSGSrcAddress_Type(InetAddress):
    """Custom type alaPimSGSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGSrcAddress_Type.__name__ = "InetAddress"
_AlaPimSGSrcAddress_Object = MibTableColumn
alaPimSGSrcAddress = _AlaPimSGSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 3),
    _AlaPimSGSrcAddress_Type()
)
alaPimSGSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGSrcAddress.setStatus("current")
_AlaPimSGUpTime_Type = TimeTicks
_AlaPimSGUpTime_Object = MibTableColumn
alaPimSGUpTime = _AlaPimSGUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 4),
    _AlaPimSGUpTime_Type()
)
alaPimSGUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpTime.setStatus("current")
_AlaPimSGPimMode_Type = AlaPimMode
_AlaPimSGPimMode_Object = MibTableColumn
alaPimSGPimMode = _AlaPimSGPimMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 5),
    _AlaPimSGPimMode_Type()
)
alaPimSGPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGPimMode.setStatus("current")


class _AlaPimSGUpstreamJoinState_Type(Integer32):
    """Custom type alaPimSGUpstreamJoinState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("joined", 2),
          ("notApplicable", 0),
          ("notJoined", 1))
    )


_AlaPimSGUpstreamJoinState_Type.__name__ = "Integer32"
_AlaPimSGUpstreamJoinState_Object = MibTableColumn
alaPimSGUpstreamJoinState = _AlaPimSGUpstreamJoinState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 6),
    _AlaPimSGUpstreamJoinState_Type()
)
alaPimSGUpstreamJoinState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpstreamJoinState.setStatus("current")
_AlaPimSGUpstreamJoinTimer_Type = TimeTicks
_AlaPimSGUpstreamJoinTimer_Object = MibTableColumn
alaPimSGUpstreamJoinTimer = _AlaPimSGUpstreamJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 7),
    _AlaPimSGUpstreamJoinTimer_Type()
)
alaPimSGUpstreamJoinTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpstreamJoinTimer.setStatus("current")


class _AlaPimSGUpstreamNeighbor_Type(InetAddress):
    """Custom type alaPimSGUpstreamNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGUpstreamNeighbor_Type.__name__ = "InetAddress"
_AlaPimSGUpstreamNeighbor_Object = MibTableColumn
alaPimSGUpstreamNeighbor = _AlaPimSGUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 8),
    _AlaPimSGUpstreamNeighbor_Type()
)
alaPimSGUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpstreamNeighbor.setStatus("current")
_AlaPimSGRPFIfIndex_Type = InterfaceIndexOrZero
_AlaPimSGRPFIfIndex_Object = MibTableColumn
alaPimSGRPFIfIndex = _AlaPimSGRPFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 9),
    _AlaPimSGRPFIfIndex_Type()
)
alaPimSGRPFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFIfIndex.setStatus("current")
_AlaPimSGRPFNextHopType_Type = InetAddressType
_AlaPimSGRPFNextHopType_Object = MibTableColumn
alaPimSGRPFNextHopType = _AlaPimSGRPFNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 10),
    _AlaPimSGRPFNextHopType_Type()
)
alaPimSGRPFNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFNextHopType.setStatus("current")


class _AlaPimSGRPFNextHop_Type(InetAddress):
    """Custom type alaPimSGRPFNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGRPFNextHop_Type.__name__ = "InetAddress"
_AlaPimSGRPFNextHop_Object = MibTableColumn
alaPimSGRPFNextHop = _AlaPimSGRPFNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 11),
    _AlaPimSGRPFNextHop_Type()
)
alaPimSGRPFNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFNextHop.setStatus("current")
_AlaPimSGRPFRouteProtocol_Type = IANAipRouteProtocol
_AlaPimSGRPFRouteProtocol_Object = MibTableColumn
alaPimSGRPFRouteProtocol = _AlaPimSGRPFRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 12),
    _AlaPimSGRPFRouteProtocol_Type()
)
alaPimSGRPFRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFRouteProtocol.setStatus("current")


class _AlaPimSGRPFRouteAddress_Type(InetAddress):
    """Custom type alaPimSGRPFRouteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGRPFRouteAddress_Type.__name__ = "InetAddress"
_AlaPimSGRPFRouteAddress_Object = MibTableColumn
alaPimSGRPFRouteAddress = _AlaPimSGRPFRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 13),
    _AlaPimSGRPFRouteAddress_Type()
)
alaPimSGRPFRouteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFRouteAddress.setStatus("current")
_AlaPimSGRPFRoutePrefixLength_Type = InetAddressPrefixLength
_AlaPimSGRPFRoutePrefixLength_Object = MibTableColumn
alaPimSGRPFRoutePrefixLength = _AlaPimSGRPFRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 14),
    _AlaPimSGRPFRoutePrefixLength_Type()
)
alaPimSGRPFRoutePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFRoutePrefixLength.setStatus("current")


class _AlaPimSGRPFRouteMetricPref_Type(Unsigned32):
    """Custom type alaPimSGRPFRouteMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimSGRPFRouteMetricPref_Type.__name__ = "Unsigned32"
_AlaPimSGRPFRouteMetricPref_Object = MibTableColumn
alaPimSGRPFRouteMetricPref = _AlaPimSGRPFRouteMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 15),
    _AlaPimSGRPFRouteMetricPref_Type()
)
alaPimSGRPFRouteMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFRouteMetricPref.setStatus("current")
_AlaPimSGRPFRouteMetric_Type = Unsigned32
_AlaPimSGRPFRouteMetric_Object = MibTableColumn
alaPimSGRPFRouteMetric = _AlaPimSGRPFRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 16),
    _AlaPimSGRPFRouteMetric_Type()
)
alaPimSGRPFRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPFRouteMetric.setStatus("current")
_AlaPimSGSPTBit_Type = TruthValue
_AlaPimSGSPTBit_Object = MibTableColumn
alaPimSGSPTBit = _AlaPimSGSPTBit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 17),
    _AlaPimSGSPTBit_Type()
)
alaPimSGSPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGSPTBit.setStatus("current")
_AlaPimSGKeepaliveTimer_Type = TimeTicks
_AlaPimSGKeepaliveTimer_Object = MibTableColumn
alaPimSGKeepaliveTimer = _AlaPimSGKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 18),
    _AlaPimSGKeepaliveTimer_Type()
)
alaPimSGKeepaliveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGKeepaliveTimer.setStatus("current")


class _AlaPimSGDRRegisterState_Type(Integer32):
    """Custom type alaPimSGDRRegisterState based on Integer32"""
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


_AlaPimSGDRRegisterState_Type.__name__ = "Integer32"
_AlaPimSGDRRegisterState_Object = MibTableColumn
alaPimSGDRRegisterState = _AlaPimSGDRRegisterState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 19),
    _AlaPimSGDRRegisterState_Type()
)
alaPimSGDRRegisterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGDRRegisterState.setStatus("current")
_AlaPimSGDRRegisterStopTimer_Type = TimeTicks
_AlaPimSGDRRegisterStopTimer_Object = MibTableColumn
alaPimSGDRRegisterStopTimer = _AlaPimSGDRRegisterStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 20),
    _AlaPimSGDRRegisterStopTimer_Type()
)
alaPimSGDRRegisterStopTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGDRRegisterStopTimer.setStatus("current")
_AlaPimSGRPRegisterPMBRAddressType_Type = InetAddressType
_AlaPimSGRPRegisterPMBRAddressType_Object = MibTableColumn
alaPimSGRPRegisterPMBRAddressType = _AlaPimSGRPRegisterPMBRAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 21),
    _AlaPimSGRPRegisterPMBRAddressType_Type()
)
alaPimSGRPRegisterPMBRAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPRegisterPMBRAddressType.setStatus("current")


class _AlaPimSGRPRegisterPMBRAddress_Type(InetAddress):
    """Custom type alaPimSGRPRegisterPMBRAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGRPRegisterPMBRAddress_Type.__name__ = "InetAddress"
_AlaPimSGRPRegisterPMBRAddress_Object = MibTableColumn
alaPimSGRPRegisterPMBRAddress = _AlaPimSGRPRegisterPMBRAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 22),
    _AlaPimSGRPRegisterPMBRAddress_Type()
)
alaPimSGRPRegisterPMBRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRPRegisterPMBRAddress.setStatus("current")


class _AlaPimSGUpstreamPruneState_Type(Integer32):
    """Custom type alaPimSGUpstreamPruneState based on Integer32"""
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
        *(("ackpending", 2),
          ("forwarding", 1),
          ("notApplicable", 0),
          ("pruned", 3))
    )


_AlaPimSGUpstreamPruneState_Type.__name__ = "Integer32"
_AlaPimSGUpstreamPruneState_Object = MibTableColumn
alaPimSGUpstreamPruneState = _AlaPimSGUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 23),
    _AlaPimSGUpstreamPruneState_Type()
)
alaPimSGUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpstreamPruneState.setStatus("current")
_AlaPimSGUpstreamPruneLimitTimer_Type = TimeTicks
_AlaPimSGUpstreamPruneLimitTimer_Object = MibTableColumn
alaPimSGUpstreamPruneLimitTimer = _AlaPimSGUpstreamPruneLimitTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 24),
    _AlaPimSGUpstreamPruneLimitTimer_Type()
)
alaPimSGUpstreamPruneLimitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGUpstreamPruneLimitTimer.setStatus("current")


class _AlaPimSGOriginatorState_Type(Integer32):
    """Custom type alaPimSGOriginatorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("notOriginator", 1),
          ("originator", 2))
    )


_AlaPimSGOriginatorState_Type.__name__ = "Integer32"
_AlaPimSGOriginatorState_Object = MibTableColumn
alaPimSGOriginatorState = _AlaPimSGOriginatorState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 25),
    _AlaPimSGOriginatorState_Type()
)
alaPimSGOriginatorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGOriginatorState.setStatus("current")
_AlaPimSGSourceActiveTimer_Type = TimeTicks
_AlaPimSGSourceActiveTimer_Object = MibTableColumn
alaPimSGSourceActiveTimer = _AlaPimSGSourceActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 26),
    _AlaPimSGSourceActiveTimer_Type()
)
alaPimSGSourceActiveTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGSourceActiveTimer.setStatus("current")
_AlaPimSGStateRefreshTimer_Type = TimeTicks
_AlaPimSGStateRefreshTimer_Object = MibTableColumn
alaPimSGStateRefreshTimer = _AlaPimSGStateRefreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 6, 1, 27),
    _AlaPimSGStateRefreshTimer_Type()
)
alaPimSGStateRefreshTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGStateRefreshTimer.setStatus("current")
_AlaPimSGITable_Object = MibTable
alaPimSGITable = _AlaPimSGITable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7)
)
if mibBuilder.loadTexts:
    alaPimSGITable.setStatus("current")
_AlaPimSGIEntry_Object = MibTableRow
alaPimSGIEntry = _AlaPimSGIEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1)
)
alaPimSGIEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGSrcAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIIfIndex"),
)
if mibBuilder.loadTexts:
    alaPimSGIEntry.setStatus("current")
_AlaPimSGIIfIndex_Type = InterfaceIndex
_AlaPimSGIIfIndex_Object = MibTableColumn
alaPimSGIIfIndex = _AlaPimSGIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 1),
    _AlaPimSGIIfIndex_Type()
)
alaPimSGIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGIIfIndex.setStatus("current")
_AlaPimSGIUpTime_Type = TimeTicks
_AlaPimSGIUpTime_Object = MibTableColumn
alaPimSGIUpTime = _AlaPimSGIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 2),
    _AlaPimSGIUpTime_Type()
)
alaPimSGIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIUpTime.setStatus("current")
_AlaPimSGILocalMembership_Type = TruthValue
_AlaPimSGILocalMembership_Object = MibTableColumn
alaPimSGILocalMembership = _AlaPimSGILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 3),
    _AlaPimSGILocalMembership_Type()
)
alaPimSGILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGILocalMembership.setStatus("current")


class _AlaPimSGIJoinPruneState_Type(Integer32):
    """Custom type alaPimSGIJoinPruneState based on Integer32"""
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


_AlaPimSGIJoinPruneState_Type.__name__ = "Integer32"
_AlaPimSGIJoinPruneState_Object = MibTableColumn
alaPimSGIJoinPruneState = _AlaPimSGIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 4),
    _AlaPimSGIJoinPruneState_Type()
)
alaPimSGIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIJoinPruneState.setStatus("current")
_AlaPimSGIPrunePendingTimer_Type = TimeTicks
_AlaPimSGIPrunePendingTimer_Object = MibTableColumn
alaPimSGIPrunePendingTimer = _AlaPimSGIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 5),
    _AlaPimSGIPrunePendingTimer_Type()
)
alaPimSGIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIPrunePendingTimer.setStatus("current")
_AlaPimSGIJoinExpiryTimer_Type = TimeTicks
_AlaPimSGIJoinExpiryTimer_Object = MibTableColumn
alaPimSGIJoinExpiryTimer = _AlaPimSGIJoinExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 6),
    _AlaPimSGIJoinExpiryTimer_Type()
)
alaPimSGIJoinExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIJoinExpiryTimer.setStatus("current")


class _AlaPimSGIAssertState_Type(Integer32):
    """Custom type alaPimSGIAssertState based on Integer32"""
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


_AlaPimSGIAssertState_Type.__name__ = "Integer32"
_AlaPimSGIAssertState_Object = MibTableColumn
alaPimSGIAssertState = _AlaPimSGIAssertState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 7),
    _AlaPimSGIAssertState_Type()
)
alaPimSGIAssertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertState.setStatus("current")
_AlaPimSGIAssertTimer_Type = TimeTicks
_AlaPimSGIAssertTimer_Object = MibTableColumn
alaPimSGIAssertTimer = _AlaPimSGIAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 8),
    _AlaPimSGIAssertTimer_Type()
)
alaPimSGIAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertTimer.setStatus("current")
_AlaPimSGIAssertWinnerAddressType_Type = InetAddressType
_AlaPimSGIAssertWinnerAddressType_Object = MibTableColumn
alaPimSGIAssertWinnerAddressType = _AlaPimSGIAssertWinnerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 9),
    _AlaPimSGIAssertWinnerAddressType_Type()
)
alaPimSGIAssertWinnerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertWinnerAddressType.setStatus("current")


class _AlaPimSGIAssertWinnerAddress_Type(InetAddress):
    """Custom type alaPimSGIAssertWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGIAssertWinnerAddress_Type.__name__ = "InetAddress"
_AlaPimSGIAssertWinnerAddress_Object = MibTableColumn
alaPimSGIAssertWinnerAddress = _AlaPimSGIAssertWinnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 10),
    _AlaPimSGIAssertWinnerAddress_Type()
)
alaPimSGIAssertWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertWinnerAddress.setStatus("current")


class _AlaPimSGIAssertWinnerMetricPref_Type(Unsigned32):
    """Custom type alaPimSGIAssertWinnerMetricPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AlaPimSGIAssertWinnerMetricPref_Type.__name__ = "Unsigned32"
_AlaPimSGIAssertWinnerMetricPref_Object = MibTableColumn
alaPimSGIAssertWinnerMetricPref = _AlaPimSGIAssertWinnerMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 11),
    _AlaPimSGIAssertWinnerMetricPref_Type()
)
alaPimSGIAssertWinnerMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertWinnerMetricPref.setStatus("current")
_AlaPimSGIAssertWinnerMetric_Type = Unsigned32
_AlaPimSGIAssertWinnerMetric_Object = MibTableColumn
alaPimSGIAssertWinnerMetric = _AlaPimSGIAssertWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 7, 1, 12),
    _AlaPimSGIAssertWinnerMetric_Type()
)
alaPimSGIAssertWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIAssertWinnerMetric.setStatus("current")
_AlaPimSGRptTable_Object = MibTable
alaPimSGRptTable = _AlaPimSGRptTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8)
)
if mibBuilder.loadTexts:
    alaPimSGRptTable.setStatus("current")
_AlaPimSGRptEntry_Object = MibTableRow
alaPimSGRptEntry = _AlaPimSGRptEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8, 1)
)
alaPimSGRptEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptSrcAddress"),
)
if mibBuilder.loadTexts:
    alaPimSGRptEntry.setStatus("current")


class _AlaPimSGRptSrcAddress_Type(InetAddress):
    """Custom type alaPimSGRptSrcAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimSGRptSrcAddress_Type.__name__ = "InetAddress"
_AlaPimSGRptSrcAddress_Object = MibTableColumn
alaPimSGRptSrcAddress = _AlaPimSGRptSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8, 1, 1),
    _AlaPimSGRptSrcAddress_Type()
)
alaPimSGRptSrcAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGRptSrcAddress.setStatus("current")
_AlaPimSGRptUpTime_Type = TimeTicks
_AlaPimSGRptUpTime_Object = MibTableColumn
alaPimSGRptUpTime = _AlaPimSGRptUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8, 1, 2),
    _AlaPimSGRptUpTime_Type()
)
alaPimSGRptUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptUpTime.setStatus("current")


class _AlaPimSGRptUpstreamPruneState_Type(Integer32):
    """Custom type alaPimSGRptUpstreamPruneState based on Integer32"""
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


_AlaPimSGRptUpstreamPruneState_Type.__name__ = "Integer32"
_AlaPimSGRptUpstreamPruneState_Object = MibTableColumn
alaPimSGRptUpstreamPruneState = _AlaPimSGRptUpstreamPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8, 1, 3),
    _AlaPimSGRptUpstreamPruneState_Type()
)
alaPimSGRptUpstreamPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptUpstreamPruneState.setStatus("current")
_AlaPimSGRptUpstreamOverrideTimer_Type = TimeTicks
_AlaPimSGRptUpstreamOverrideTimer_Object = MibTableColumn
alaPimSGRptUpstreamOverrideTimer = _AlaPimSGRptUpstreamOverrideTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 8, 1, 4),
    _AlaPimSGRptUpstreamOverrideTimer_Type()
)
alaPimSGRptUpstreamOverrideTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptUpstreamOverrideTimer.setStatus("current")
_AlaPimSGRptITable_Object = MibTable
alaPimSGRptITable = _AlaPimSGRptITable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9)
)
if mibBuilder.loadTexts:
    alaPimSGRptITable.setStatus("current")
_AlaPimSGRptIEntry_Object = MibTableRow
alaPimSGRptIEntry = _AlaPimSGRptIEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1)
)
alaPimSGRptIEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptSrcAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIIfIndex"),
)
if mibBuilder.loadTexts:
    alaPimSGRptIEntry.setStatus("current")
_AlaPimSGRptIIfIndex_Type = InterfaceIndex
_AlaPimSGRptIIfIndex_Object = MibTableColumn
alaPimSGRptIIfIndex = _AlaPimSGRptIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 1),
    _AlaPimSGRptIIfIndex_Type()
)
alaPimSGRptIIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimSGRptIIfIndex.setStatus("current")
_AlaPimSGRptIUpTime_Type = TimeTicks
_AlaPimSGRptIUpTime_Object = MibTableColumn
alaPimSGRptIUpTime = _AlaPimSGRptIUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 2),
    _AlaPimSGRptIUpTime_Type()
)
alaPimSGRptIUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptIUpTime.setStatus("current")
_AlaPimSGRptILocalMembership_Type = TruthValue
_AlaPimSGRptILocalMembership_Object = MibTableColumn
alaPimSGRptILocalMembership = _AlaPimSGRptILocalMembership_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 3),
    _AlaPimSGRptILocalMembership_Type()
)
alaPimSGRptILocalMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptILocalMembership.setStatus("current")


class _AlaPimSGRptIJoinPruneState_Type(Integer32):
    """Custom type alaPimSGRptIJoinPruneState based on Integer32"""
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


_AlaPimSGRptIJoinPruneState_Type.__name__ = "Integer32"
_AlaPimSGRptIJoinPruneState_Object = MibTableColumn
alaPimSGRptIJoinPruneState = _AlaPimSGRptIJoinPruneState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 4),
    _AlaPimSGRptIJoinPruneState_Type()
)
alaPimSGRptIJoinPruneState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptIJoinPruneState.setStatus("current")
_AlaPimSGRptIPrunePendingTimer_Type = TimeTicks
_AlaPimSGRptIPrunePendingTimer_Object = MibTableColumn
alaPimSGRptIPrunePendingTimer = _AlaPimSGRptIPrunePendingTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 5),
    _AlaPimSGRptIPrunePendingTimer_Type()
)
alaPimSGRptIPrunePendingTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptIPrunePendingTimer.setStatus("current")
_AlaPimSGRptIPruneExpiryTimer_Type = TimeTicks
_AlaPimSGRptIPruneExpiryTimer_Object = MibTableColumn
alaPimSGRptIPruneExpiryTimer = _AlaPimSGRptIPruneExpiryTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 9, 1, 6),
    _AlaPimSGRptIPruneExpiryTimer_Type()
)
alaPimSGRptIPruneExpiryTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptIPruneExpiryTimer.setStatus("current")
_AlaPimStaticRPTable_Object = MibTable
alaPimStaticRPTable = _AlaPimStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11)
)
if mibBuilder.loadTexts:
    alaPimStaticRPTable.setStatus("current")
_AlaPimStaticRPEntry_Object = MibTableRow
alaPimStaticRPEntry = _AlaPimStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1)
)
alaPimStaticRPEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPGrpPrefixLength"),
)
if mibBuilder.loadTexts:
    alaPimStaticRPEntry.setStatus("current")
_AlaPimStaticRPAddressType_Type = InetAddressType
_AlaPimStaticRPAddressType_Object = MibTableColumn
alaPimStaticRPAddressType = _AlaPimStaticRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 1),
    _AlaPimStaticRPAddressType_Type()
)
alaPimStaticRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStaticRPAddressType.setStatus("current")


class _AlaPimStaticRPGrpAddress_Type(InetAddress):
    """Custom type alaPimStaticRPGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStaticRPGrpAddress_Type.__name__ = "InetAddress"
_AlaPimStaticRPGrpAddress_Object = MibTableColumn
alaPimStaticRPGrpAddress = _AlaPimStaticRPGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 2),
    _AlaPimStaticRPGrpAddress_Type()
)
alaPimStaticRPGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStaticRPGrpAddress.setStatus("current")


class _AlaPimStaticRPGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaPimStaticRPGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaPimStaticRPGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaPimStaticRPGrpPrefixLength_Object = MibTableColumn
alaPimStaticRPGrpPrefixLength = _AlaPimStaticRPGrpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 3),
    _AlaPimStaticRPGrpPrefixLength_Type()
)
alaPimStaticRPGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimStaticRPGrpPrefixLength.setStatus("current")


class _AlaPimStaticRPRPAddress_Type(InetAddress):
    """Custom type alaPimStaticRPRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimStaticRPRPAddress_Type.__name__ = "InetAddress"
_AlaPimStaticRPRPAddress_Object = MibTableColumn
alaPimStaticRPRPAddress = _AlaPimStaticRPRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 4),
    _AlaPimStaticRPRPAddress_Type()
)
alaPimStaticRPRPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPRPAddress.setStatus("current")


class _AlaPimStaticRPPimMode_Type(AlaPimMode):
    """Custom type alaPimStaticRPPimMode based on AlaPimMode"""


_AlaPimStaticRPPimMode_Object = MibTableColumn
alaPimStaticRPPimMode = _AlaPimStaticRPPimMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 5),
    _AlaPimStaticRPPimMode_Type()
)
alaPimStaticRPPimMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPPimMode.setStatus("current")


class _AlaPimStaticRPOverrideDynamic_Type(TruthValue):
    """Custom type alaPimStaticRPOverrideDynamic based on TruthValue"""


_AlaPimStaticRPOverrideDynamic_Object = MibTableColumn
alaPimStaticRPOverrideDynamic = _AlaPimStaticRPOverrideDynamic_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 6),
    _AlaPimStaticRPOverrideDynamic_Type()
)
alaPimStaticRPOverrideDynamic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPOverrideDynamic.setStatus("current")
_AlaPimStaticRPPrecedence_Type = Unsigned32
_AlaPimStaticRPPrecedence_Object = MibTableColumn
alaPimStaticRPPrecedence = _AlaPimStaticRPPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 7),
    _AlaPimStaticRPPrecedence_Type()
)
alaPimStaticRPPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPPrecedence.setStatus("current")
_AlaPimStaticRPRowStatus_Type = RowStatus
_AlaPimStaticRPRowStatus_Object = MibTableColumn
alaPimStaticRPRowStatus = _AlaPimStaticRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 8),
    _AlaPimStaticRPRowStatus_Type()
)
alaPimStaticRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPRowStatus.setStatus("current")


class _AlaPimStaticRPStorageType_Type(StorageType):
    """Custom type alaPimStaticRPStorageType based on StorageType"""


_AlaPimStaticRPStorageType_Object = MibTableColumn
alaPimStaticRPStorageType = _AlaPimStaticRPStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 11, 1, 9),
    _AlaPimStaticRPStorageType_Type()
)
alaPimStaticRPStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaPimStaticRPStorageType.setStatus("current")
_AlaPimGroupMappingTable_Object = MibTable
alaPimGroupMappingTable = _AlaPimGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13)
)
if mibBuilder.loadTexts:
    alaPimGroupMappingTable.setStatus("current")
_AlaPimGroupMappingEntry_Object = MibTableRow
alaPimGroupMappingEntry = _AlaPimGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1)
)
alaPimGroupMappingEntry.setIndexNames(
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingOrigin"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingGrpAddress"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingGrpPrefixLength"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingRPAddressType"),
    (0, "ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingRPAddress"),
)
if mibBuilder.loadTexts:
    alaPimGroupMappingEntry.setStatus("current")
_AlaPimGroupMappingOrigin_Type = AlaPimGroupMappingOriginType
_AlaPimGroupMappingOrigin_Object = MibTableColumn
alaPimGroupMappingOrigin = _AlaPimGroupMappingOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 1),
    _AlaPimGroupMappingOrigin_Type()
)
alaPimGroupMappingOrigin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingOrigin.setStatus("current")
_AlaPimGroupMappingAddressType_Type = InetAddressType
_AlaPimGroupMappingAddressType_Object = MibTableColumn
alaPimGroupMappingAddressType = _AlaPimGroupMappingAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 2),
    _AlaPimGroupMappingAddressType_Type()
)
alaPimGroupMappingAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingAddressType.setStatus("current")


class _AlaPimGroupMappingGrpAddress_Type(InetAddress):
    """Custom type alaPimGroupMappingGrpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimGroupMappingGrpAddress_Type.__name__ = "InetAddress"
_AlaPimGroupMappingGrpAddress_Object = MibTableColumn
alaPimGroupMappingGrpAddress = _AlaPimGroupMappingGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 3),
    _AlaPimGroupMappingGrpAddress_Type()
)
alaPimGroupMappingGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingGrpAddress.setStatus("current")


class _AlaPimGroupMappingGrpPrefixLength_Type(InetAddressPrefixLength):
    """Custom type alaPimGroupMappingGrpPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_AlaPimGroupMappingGrpPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_AlaPimGroupMappingGrpPrefixLength_Object = MibTableColumn
alaPimGroupMappingGrpPrefixLength = _AlaPimGroupMappingGrpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 4),
    _AlaPimGroupMappingGrpPrefixLength_Type()
)
alaPimGroupMappingGrpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingGrpPrefixLength.setStatus("current")
_AlaPimGroupMappingRPAddressType_Type = InetAddressType
_AlaPimGroupMappingRPAddressType_Object = MibTableColumn
alaPimGroupMappingRPAddressType = _AlaPimGroupMappingRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 5),
    _AlaPimGroupMappingRPAddressType_Type()
)
alaPimGroupMappingRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingRPAddressType.setStatus("current")


class _AlaPimGroupMappingRPAddress_Type(InetAddress):
    """Custom type alaPimGroupMappingRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimGroupMappingRPAddress_Type.__name__ = "InetAddress"
_AlaPimGroupMappingRPAddress_Object = MibTableColumn
alaPimGroupMappingRPAddress = _AlaPimGroupMappingRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 6),
    _AlaPimGroupMappingRPAddress_Type()
)
alaPimGroupMappingRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaPimGroupMappingRPAddress.setStatus("current")
_AlaPimGroupMappingPimMode_Type = AlaPimMode
_AlaPimGroupMappingPimMode_Object = MibTableColumn
alaPimGroupMappingPimMode = _AlaPimGroupMappingPimMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 7),
    _AlaPimGroupMappingPimMode_Type()
)
alaPimGroupMappingPimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimGroupMappingPimMode.setStatus("current")
_AlaPimGroupMappingPrecedence_Type = Unsigned32
_AlaPimGroupMappingPrecedence_Object = MibTableColumn
alaPimGroupMappingPrecedence = _AlaPimGroupMappingPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 13, 1, 8),
    _AlaPimGroupMappingPrecedence_Type()
)
alaPimGroupMappingPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimGroupMappingPrecedence.setStatus("current")


class _AlaPimKeepalivePeriod_Type(Unsigned32):
    """Custom type alaPimKeepalivePeriod based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimKeepalivePeriod_Type.__name__ = "Unsigned32"
_AlaPimKeepalivePeriod_Object = MibScalar
alaPimKeepalivePeriod = _AlaPimKeepalivePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 14),
    _AlaPimKeepalivePeriod_Type()
)
alaPimKeepalivePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimKeepalivePeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimKeepalivePeriod.setUnits("seconds")


class _AlaPimRegisterSuppressionTime_Type(Unsigned32):
    """Custom type alaPimRegisterSuppressionTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimRegisterSuppressionTime_Type.__name__ = "Unsigned32"
_AlaPimRegisterSuppressionTime_Object = MibScalar
alaPimRegisterSuppressionTime = _AlaPimRegisterSuppressionTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 15),
    _AlaPimRegisterSuppressionTime_Type()
)
alaPimRegisterSuppressionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimRegisterSuppressionTime.setStatus("current")
if mibBuilder.loadTexts:
    alaPimRegisterSuppressionTime.setUnits("seconds")
_AlaPimStarGEntries_Type = Gauge32
_AlaPimStarGEntries_Object = MibScalar
alaPimStarGEntries = _AlaPimStarGEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 16),
    _AlaPimStarGEntries_Type()
)
alaPimStarGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGEntries.setStatus("current")
_AlaPimStarGIEntries_Type = Gauge32
_AlaPimStarGIEntries_Object = MibScalar
alaPimStarGIEntries = _AlaPimStarGIEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 17),
    _AlaPimStarGIEntries_Type()
)
alaPimStarGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimStarGIEntries.setStatus("current")
_AlaPimSGEntries_Type = Gauge32
_AlaPimSGEntries_Object = MibScalar
alaPimSGEntries = _AlaPimSGEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 18),
    _AlaPimSGEntries_Type()
)
alaPimSGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGEntries.setStatus("current")
_AlaPimSGIEntries_Type = Gauge32
_AlaPimSGIEntries_Object = MibScalar
alaPimSGIEntries = _AlaPimSGIEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 19),
    _AlaPimSGIEntries_Type()
)
alaPimSGIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGIEntries.setStatus("current")
_AlaPimSGRptEntries_Type = Gauge32
_AlaPimSGRptEntries_Object = MibScalar
alaPimSGRptEntries = _AlaPimSGRptEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 20),
    _AlaPimSGRptEntries_Type()
)
alaPimSGRptEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptEntries.setStatus("current")
_AlaPimSGRptIEntries_Type = Gauge32
_AlaPimSGRptIEntries_Object = MibScalar
alaPimSGRptIEntries = _AlaPimSGRptIEntries_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 21),
    _AlaPimSGRptIEntries_Type()
)
alaPimSGRptIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimSGRptIEntries.setStatus("current")
_AlaPimOutAsserts_Type = Counter64
_AlaPimOutAsserts_Object = MibScalar
alaPimOutAsserts = _AlaPimOutAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 22),
    _AlaPimOutAsserts_Type()
)
alaPimOutAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimOutAsserts.setStatus("current")
_AlaPimInAsserts_Type = Counter64
_AlaPimInAsserts_Object = MibScalar
alaPimInAsserts = _AlaPimInAsserts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 23),
    _AlaPimInAsserts_Type()
)
alaPimInAsserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInAsserts.setStatus("current")
_AlaPimLastAssertInterface_Type = InterfaceIndexOrZero
_AlaPimLastAssertInterface_Object = MibScalar
alaPimLastAssertInterface = _AlaPimLastAssertInterface_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 24),
    _AlaPimLastAssertInterface_Type()
)
alaPimLastAssertInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimLastAssertInterface.setStatus("current")
_AlaPimLastAssertGroupAddressType_Type = InetAddressType
_AlaPimLastAssertGroupAddressType_Object = MibScalar
alaPimLastAssertGroupAddressType = _AlaPimLastAssertGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 25),
    _AlaPimLastAssertGroupAddressType_Type()
)
alaPimLastAssertGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimLastAssertGroupAddressType.setStatus("current")


class _AlaPimLastAssertGroupAddress_Type(InetAddress):
    """Custom type alaPimLastAssertGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimLastAssertGroupAddress_Type.__name__ = "InetAddress"
_AlaPimLastAssertGroupAddress_Object = MibScalar
alaPimLastAssertGroupAddress = _AlaPimLastAssertGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 26),
    _AlaPimLastAssertGroupAddress_Type()
)
alaPimLastAssertGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimLastAssertGroupAddress.setStatus("current")
_AlaPimLastAssertSourceAddressType_Type = InetAddressType
_AlaPimLastAssertSourceAddressType_Object = MibScalar
alaPimLastAssertSourceAddressType = _AlaPimLastAssertSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 27),
    _AlaPimLastAssertSourceAddressType_Type()
)
alaPimLastAssertSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimLastAssertSourceAddressType.setStatus("current")


class _AlaPimLastAssertSourceAddress_Type(InetAddress):
    """Custom type alaPimLastAssertSourceAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimLastAssertSourceAddress_Type.__name__ = "InetAddress"
_AlaPimLastAssertSourceAddress_Object = MibScalar
alaPimLastAssertSourceAddress = _AlaPimLastAssertSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 28),
    _AlaPimLastAssertSourceAddress_Type()
)
alaPimLastAssertSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimLastAssertSourceAddress.setStatus("current")


class _AlaPimNeighborLossNotificationPeriod_Type(Unsigned32):
    """Custom type alaPimNeighborLossNotificationPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimNeighborLossNotificationPeriod_Type.__name__ = "Unsigned32"
_AlaPimNeighborLossNotificationPeriod_Object = MibScalar
alaPimNeighborLossNotificationPeriod = _AlaPimNeighborLossNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 29),
    _AlaPimNeighborLossNotificationPeriod_Type()
)
alaPimNeighborLossNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimNeighborLossNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimNeighborLossNotificationPeriod.setUnits("seconds")
_AlaPimNeighborLossCount_Type = Counter32
_AlaPimNeighborLossCount_Object = MibScalar
alaPimNeighborLossCount = _AlaPimNeighborLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 30),
    _AlaPimNeighborLossCount_Type()
)
alaPimNeighborLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimNeighborLossCount.setStatus("current")


class _AlaPimInvalidRegisterNotificationPeriod_Type(Unsigned32):
    """Custom type alaPimInvalidRegisterNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AlaPimInvalidRegisterNotificationPeriod_Type.__name__ = "Unsigned32"
_AlaPimInvalidRegisterNotificationPeriod_Object = MibScalar
alaPimInvalidRegisterNotificationPeriod = _AlaPimInvalidRegisterNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 31),
    _AlaPimInvalidRegisterNotificationPeriod_Type()
)
alaPimInvalidRegisterNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterNotificationPeriod.setUnits("seconds")
_AlaPimInvalidRegisterMsgsRcvd_Type = Counter32
_AlaPimInvalidRegisterMsgsRcvd_Object = MibScalar
alaPimInvalidRegisterMsgsRcvd = _AlaPimInvalidRegisterMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 32),
    _AlaPimInvalidRegisterMsgsRcvd_Type()
)
alaPimInvalidRegisterMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterMsgsRcvd.setStatus("current")
_AlaPimInvalidRegisterAddressType_Type = InetAddressType
_AlaPimInvalidRegisterAddressType_Object = MibScalar
alaPimInvalidRegisterAddressType = _AlaPimInvalidRegisterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 33),
    _AlaPimInvalidRegisterAddressType_Type()
)
alaPimInvalidRegisterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterAddressType.setStatus("current")


class _AlaPimInvalidRegisterOrigin_Type(InetAddress):
    """Custom type alaPimInvalidRegisterOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidRegisterOrigin_Type.__name__ = "InetAddress"
_AlaPimInvalidRegisterOrigin_Object = MibScalar
alaPimInvalidRegisterOrigin = _AlaPimInvalidRegisterOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 34),
    _AlaPimInvalidRegisterOrigin_Type()
)
alaPimInvalidRegisterOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterOrigin.setStatus("current")


class _AlaPimInvalidRegisterGroup_Type(InetAddress):
    """Custom type alaPimInvalidRegisterGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidRegisterGroup_Type.__name__ = "InetAddress"
_AlaPimInvalidRegisterGroup_Object = MibScalar
alaPimInvalidRegisterGroup = _AlaPimInvalidRegisterGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 35),
    _AlaPimInvalidRegisterGroup_Type()
)
alaPimInvalidRegisterGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterGroup.setStatus("current")


class _AlaPimInvalidRegisterRp_Type(InetAddress):
    """Custom type alaPimInvalidRegisterRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidRegisterRp_Type.__name__ = "InetAddress"
_AlaPimInvalidRegisterRp_Object = MibScalar
alaPimInvalidRegisterRp = _AlaPimInvalidRegisterRp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 36),
    _AlaPimInvalidRegisterRp_Type()
)
alaPimInvalidRegisterRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidRegisterRp.setStatus("current")


class _AlaPimInvalidJoinPruneNotificationPeriod_Type(Unsigned32):
    """Custom type alaPimInvalidJoinPruneNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AlaPimInvalidJoinPruneNotificationPeriod_Type.__name__ = "Unsigned32"
_AlaPimInvalidJoinPruneNotificationPeriod_Object = MibScalar
alaPimInvalidJoinPruneNotificationPeriod = _AlaPimInvalidJoinPruneNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 37),
    _AlaPimInvalidJoinPruneNotificationPeriod_Type()
)
alaPimInvalidJoinPruneNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneNotificationPeriod.setUnits("seconds")
_AlaPimInvalidJoinPruneMsgsRcvd_Type = Counter32
_AlaPimInvalidJoinPruneMsgsRcvd_Object = MibScalar
alaPimInvalidJoinPruneMsgsRcvd = _AlaPimInvalidJoinPruneMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 38),
    _AlaPimInvalidJoinPruneMsgsRcvd_Type()
)
alaPimInvalidJoinPruneMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneMsgsRcvd.setStatus("current")
_AlaPimInvalidJoinPruneAddressType_Type = InetAddressType
_AlaPimInvalidJoinPruneAddressType_Object = MibScalar
alaPimInvalidJoinPruneAddressType = _AlaPimInvalidJoinPruneAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 39),
    _AlaPimInvalidJoinPruneAddressType_Type()
)
alaPimInvalidJoinPruneAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneAddressType.setStatus("current")


class _AlaPimInvalidJoinPruneOrigin_Type(InetAddress):
    """Custom type alaPimInvalidJoinPruneOrigin based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidJoinPruneOrigin_Type.__name__ = "InetAddress"
_AlaPimInvalidJoinPruneOrigin_Object = MibScalar
alaPimInvalidJoinPruneOrigin = _AlaPimInvalidJoinPruneOrigin_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 40),
    _AlaPimInvalidJoinPruneOrigin_Type()
)
alaPimInvalidJoinPruneOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneOrigin.setStatus("current")


class _AlaPimInvalidJoinPruneGroup_Type(InetAddress):
    """Custom type alaPimInvalidJoinPruneGroup based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidJoinPruneGroup_Type.__name__ = "InetAddress"
_AlaPimInvalidJoinPruneGroup_Object = MibScalar
alaPimInvalidJoinPruneGroup = _AlaPimInvalidJoinPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 41),
    _AlaPimInvalidJoinPruneGroup_Type()
)
alaPimInvalidJoinPruneGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneGroup.setStatus("current")


class _AlaPimInvalidJoinPruneRp_Type(InetAddress):
    """Custom type alaPimInvalidJoinPruneRp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_AlaPimInvalidJoinPruneRp_Type.__name__ = "InetAddress"
_AlaPimInvalidJoinPruneRp_Object = MibScalar
alaPimInvalidJoinPruneRp = _AlaPimInvalidJoinPruneRp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 42),
    _AlaPimInvalidJoinPruneRp_Type()
)
alaPimInvalidJoinPruneRp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInvalidJoinPruneRp.setStatus("current")


class _AlaPimRPMappingNotificationPeriod_Type(Unsigned32):
    """Custom type alaPimRPMappingNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimRPMappingNotificationPeriod_Type.__name__ = "Unsigned32"
_AlaPimRPMappingNotificationPeriod_Object = MibScalar
alaPimRPMappingNotificationPeriod = _AlaPimRPMappingNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 43),
    _AlaPimRPMappingNotificationPeriod_Type()
)
alaPimRPMappingNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimRPMappingNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimRPMappingNotificationPeriod.setUnits("seconds")
_AlaPimRPMappingChangeCount_Type = Counter32
_AlaPimRPMappingChangeCount_Object = MibScalar
alaPimRPMappingChangeCount = _AlaPimRPMappingChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 44),
    _AlaPimRPMappingChangeCount_Type()
)
alaPimRPMappingChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimRPMappingChangeCount.setStatus("current")


class _AlaPimInterfaceElectionNotificationPeriod_Type(Unsigned32):
    """Custom type alaPimInterfaceElectionNotificationPeriod based on Unsigned32"""
    defaultValue = 65535

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimInterfaceElectionNotificationPeriod_Type.__name__ = "Unsigned32"
_AlaPimInterfaceElectionNotificationPeriod_Object = MibScalar
alaPimInterfaceElectionNotificationPeriod = _AlaPimInterfaceElectionNotificationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 45),
    _AlaPimInterfaceElectionNotificationPeriod_Type()
)
alaPimInterfaceElectionNotificationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimInterfaceElectionNotificationPeriod.setStatus("current")
if mibBuilder.loadTexts:
    alaPimInterfaceElectionNotificationPeriod.setUnits("seconds")
_AlaPimInterfaceElectionWinCount_Type = Counter32
_AlaPimInterfaceElectionWinCount_Object = MibScalar
alaPimInterfaceElectionWinCount = _AlaPimInterfaceElectionWinCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 46),
    _AlaPimInterfaceElectionWinCount_Type()
)
alaPimInterfaceElectionWinCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaPimInterfaceElectionWinCount.setStatus("current")


class _AlaPimRefreshInterval_Type(Unsigned32):
    """Custom type alaPimRefreshInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlaPimRefreshInterval_Type.__name__ = "Unsigned32"
_AlaPimRefreshInterval_Object = MibScalar
alaPimRefreshInterval = _AlaPimRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 47),
    _AlaPimRefreshInterval_Type()
)
alaPimRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaPimRefreshInterval.setUnits("seconds")


class _AlaPimDeviceConfigStorageType_Type(StorageType):
    """Custom type alaPimDeviceConfigStorageType based on StorageType"""


_AlaPimDeviceConfigStorageType_Object = MibScalar
alaPimDeviceConfigStorageType = _AlaPimDeviceConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 1, 48),
    _AlaPimDeviceConfigStorageType_Type()
)
alaPimDeviceConfigStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaPimDeviceConfigStorageType.setStatus("current")
_AlaPimMIBConformance_ObjectIdentity = ObjectIdentity
alaPimMIBConformance = _AlaPimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2)
)
_AlaPimMIBCompliances_ObjectIdentity = ObjectIdentity
alaPimMIBCompliances = _AlaPimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 1)
)
_AlaPimMIBGroups_ObjectIdentity = ObjectIdentity
alaPimMIBGroups = _AlaPimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2)
)

# Managed Objects groups

alaPimTopologyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 1)
)
alaPimTopologyGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceGenerationIDValue"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceDR"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceDRPriorityEnabled"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceHelloHoldtime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceJoinPruneHoldtime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceLanDelayEnabled"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceEffectPropagDelay"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceEffectOverrideIvl"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceSuppressionEnabled"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceBidirCapable"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborGenerationIDPresent"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborGenerationIDValue"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborExpiryTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborDRPriorityPresent"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborDRPriority"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborLanPruneDelayPresent"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborTBit"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborPropagationDelay"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborOverrideInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborBidirCapable"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNbrSecAddress"))
)
if mibBuilder.loadTexts:
    alaPimTopologyGroup.setStatus("current")

alaPimTuningParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 3)
)
alaPimTuningParametersGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimKeepalivePeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimRegisterSuppressionTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceDRPriority"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceHelloInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceTrigHelloInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceJoinPruneInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfacePropagationDelay"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceOverrideInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceDomainBorder"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceStubInterface"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceStatus"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceStorageType"))
)
if mibBuilder.loadTexts:
    alaPimTuningParametersGroup.setStatus("current")

alaPimRouterStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 4)
)
alaPimRouterStatisticsGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGEntries"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIEntries"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGEntries"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIEntries"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptEntries"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIEntries"))
)
if mibBuilder.loadTexts:
    alaPimRouterStatisticsGroup.setStatus("current")

alaPimSsmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 5)
)
alaPimSsmGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpstreamJoinState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpstreamJoinTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpstreamNeighbor"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFIfIndex"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFNextHopType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFNextHop"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFRouteProtocol"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFRouteAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFRoutePrefixLength"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFRouteMetricPref"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPFRouteMetric"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGSPTBit"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGKeepaliveTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGDRRegisterState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGDRRegisterStopTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPRegisterPMBRAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRPRegisterPMBRAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGILocalMembership"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIJoinPruneState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIPrunePendingTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIJoinExpiryTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertWinnerAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertWinnerAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertWinnerMetricPref"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGIAssertWinnerMetric"))
)
if mibBuilder.loadTexts:
    alaPimSsmGroup.setStatus("current")

alaPimRPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 6)
)
alaPimRPConfigGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPRPAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPOverrideDynamic"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPRowStatus"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPStorageType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPrecedence"))
)
if mibBuilder.loadTexts:
    alaPimRPConfigGroup.setStatus("current")

alaPimSmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 7)
)
alaPimSmGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGPimModeOrigin"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPIsLocal"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGUpstreamJoinState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGUpstreamJoinTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGUpstreamNeighborType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGUpstreamNeighbor"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFIfIndex"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFNextHopType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFNextHop"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFRouteProtocol"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFRouteAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFRoutePrefixLength"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFRouteMetricPref"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGRPFRouteMetric"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGILocalMembership"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIJoinPruneState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIPrunePendingTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIJoinExpiryTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertWinnerAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertWinnerAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertWinnerMetricPref"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStarGIAssertWinnerMetric"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptUpstreamPruneState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptUpstreamOverrideTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIUpTime"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptILocalMembership"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIJoinPruneState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIPrunePendingTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGRptIPruneExpiryTimer"))
)
if mibBuilder.loadTexts:
    alaPimSmGroup.setStatus("current")

alaPimStaticRPPrecedenceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 10)
)
alaPimStaticRPPrecedenceGroup.setObjects(
    ("ALCATEL-IND1-PIM-STD-MIB", "alaPimStaticRPPrecedence")
)
if mibBuilder.loadTexts:
    alaPimStaticRPPrecedenceGroup.setStatus("current")

alaPimNetMgmtNotificationObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 11)
)
alaPimNetMgmtNotificationObjects.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterNotificationPeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterMsgsRcvd"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterOrigin"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterGroup"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterRp"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneNotificationPeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneMsgsRcvd"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneOrigin"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneGroup"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneRp"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimRPMappingNotificationPeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimRPMappingChangeCount"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceElectionNotificationPeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceElectionWinCount"))
)
if mibBuilder.loadTexts:
    alaPimNetMgmtNotificationObjects.setStatus("current")

alaPimDiagnosticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 13)
)
alaPimDiagnosticsGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimInAsserts"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimOutAsserts"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimLastAssertInterface"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimLastAssertGroupAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimLastAssertGroupAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimLastAssertSourceAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimLastAssertSourceAddress"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborLossNotificationPeriod"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborLossCount"))
)
if mibBuilder.loadTexts:
    alaPimDiagnosticsGroup.setStatus("current")

alaPimDmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 14)
)
alaPimDmGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimRefreshInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfacePruneLimitInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceGraftRetryInterval"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceSRPriorityEnabled"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborSRCapable"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpstreamPruneState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGUpstreamPruneLimitTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGOriginatorState"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGSourceActiveTimer"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimSGStateRefreshTimer"))
)
if mibBuilder.loadTexts:
    alaPimDmGroup.setStatus("current")

alaPimDeviceStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 15)
)
alaPimDeviceStorageGroup.setObjects(
    ("ALCATEL-IND1-PIM-STD-MIB", "alaPimDeviceConfigStorageType")
)
if mibBuilder.loadTexts:
    alaPimDeviceStorageGroup.setStatus("current")


# Notification objects

alaPimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0, 1)
)
alaPimNeighborLoss.setObjects(
    ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborUpTime")
)
if mibBuilder.loadTexts:
    alaPimNeighborLoss.setStatus(
        "current"
    )

alaPimInvalidRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0, 2)
)
alaPimInvalidRegister.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterOrigin"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterGroup"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegisterRp"))
)
if mibBuilder.loadTexts:
    alaPimInvalidRegister.setStatus(
        "current"
    )

alaPimInvalidJoinPrune = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0, 3)
)
alaPimInvalidJoinPrune.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneOrigin"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneGroup"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPruneRp"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborUpTime"))
)
if mibBuilder.loadTexts:
    alaPimInvalidJoinPrune.setStatus(
        "current"
    )

alaPimRPMappingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0, 4)
)
alaPimRPMappingChange.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPimMode"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimGroupMappingPrecedence"))
)
if mibBuilder.loadTexts:
    alaPimRPMappingChange.setStatus(
        "current"
    )

alaPimInterfaceElection = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 0, 5)
)
alaPimInterfaceElection.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceAddressType"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceAddress"))
)
if mibBuilder.loadTexts:
    alaPimInterfaceElection.setStatus(
        "current"
    )


# Notifications groups

alaPimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 2)
)
alaPimNotificationGroup.setObjects(
    ("ALCATEL-IND1-PIM-STD-MIB", "alaPimNeighborLoss")
)
if mibBuilder.loadTexts:
    alaPimNotificationGroup.setStatus(
        "current"
    )

alaPimNetMgmtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 2, 12)
)
alaPimNetMgmtNotificationGroup.setObjects(
      *(("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidRegister"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInvalidJoinPrune"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimRPMappingChange"),
        ("ALCATEL-IND1-PIM-STD-MIB", "alaPimInterfaceElection"))
)
if mibBuilder.loadTexts:
    alaPimNetMgmtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaPimMIBComplianceAsm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaPimMIBComplianceAsm.setStatus(
        "current"
    )

alaPimMIBComplianceSsm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    alaPimMIBComplianceSsm.setStatus(
        "current"
    )

alaPimMIBComplianceDm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 6, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    alaPimMIBComplianceDm.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-PIM-STD-MIB",
    **{"AlaPimMode": AlaPimMode,
       "AlaPimGroupMappingOriginType": AlaPimGroupMappingOriginType,
       "alaPimStdMIB": alaPimStdMIB,
       "alaPimNotifications": alaPimNotifications,
       "alaPimNeighborLoss": alaPimNeighborLoss,
       "alaPimInvalidRegister": alaPimInvalidRegister,
       "alaPimInvalidJoinPrune": alaPimInvalidJoinPrune,
       "alaPimRPMappingChange": alaPimRPMappingChange,
       "alaPimInterfaceElection": alaPimInterfaceElection,
       "alaPim": alaPim,
       "alaPimInterfaceTable": alaPimInterfaceTable,
       "alaPimInterfaceEntry": alaPimInterfaceEntry,
       "alaPimInterfaceIfIndex": alaPimInterfaceIfIndex,
       "alaPimInterfaceIPVersion": alaPimInterfaceIPVersion,
       "alaPimInterfaceAddressType": alaPimInterfaceAddressType,
       "alaPimInterfaceAddress": alaPimInterfaceAddress,
       "alaPimInterfaceGenerationIDValue": alaPimInterfaceGenerationIDValue,
       "alaPimInterfaceDR": alaPimInterfaceDR,
       "alaPimInterfaceDRPriority": alaPimInterfaceDRPriority,
       "alaPimInterfaceDRPriorityEnabled": alaPimInterfaceDRPriorityEnabled,
       "alaPimInterfaceHelloInterval": alaPimInterfaceHelloInterval,
       "alaPimInterfaceTrigHelloInterval": alaPimInterfaceTrigHelloInterval,
       "alaPimInterfaceHelloHoldtime": alaPimInterfaceHelloHoldtime,
       "alaPimInterfaceJoinPruneInterval": alaPimInterfaceJoinPruneInterval,
       "alaPimInterfaceJoinPruneHoldtime": alaPimInterfaceJoinPruneHoldtime,
       "alaPimInterfaceDFElectionRobustness": alaPimInterfaceDFElectionRobustness,
       "alaPimInterfaceLanDelayEnabled": alaPimInterfaceLanDelayEnabled,
       "alaPimInterfacePropagationDelay": alaPimInterfacePropagationDelay,
       "alaPimInterfaceOverrideInterval": alaPimInterfaceOverrideInterval,
       "alaPimInterfaceEffectPropagDelay": alaPimInterfaceEffectPropagDelay,
       "alaPimInterfaceEffectOverrideIvl": alaPimInterfaceEffectOverrideIvl,
       "alaPimInterfaceSuppressionEnabled": alaPimInterfaceSuppressionEnabled,
       "alaPimInterfaceBidirCapable": alaPimInterfaceBidirCapable,
       "alaPimInterfaceDomainBorder": alaPimInterfaceDomainBorder,
       "alaPimInterfaceStubInterface": alaPimInterfaceStubInterface,
       "alaPimInterfacePruneLimitInterval": alaPimInterfacePruneLimitInterval,
       "alaPimInterfaceGraftRetryInterval": alaPimInterfaceGraftRetryInterval,
       "alaPimInterfaceSRPriorityEnabled": alaPimInterfaceSRPriorityEnabled,
       "alaPimInterfaceStatus": alaPimInterfaceStatus,
       "alaPimInterfaceStorageType": alaPimInterfaceStorageType,
       "alaPimNeighborTable": alaPimNeighborTable,
       "alaPimNeighborEntry": alaPimNeighborEntry,
       "alaPimNeighborIfIndex": alaPimNeighborIfIndex,
       "alaPimNeighborAddressType": alaPimNeighborAddressType,
       "alaPimNeighborAddress": alaPimNeighborAddress,
       "alaPimNeighborGenerationIDPresent": alaPimNeighborGenerationIDPresent,
       "alaPimNeighborGenerationIDValue": alaPimNeighborGenerationIDValue,
       "alaPimNeighborUpTime": alaPimNeighborUpTime,
       "alaPimNeighborExpiryTime": alaPimNeighborExpiryTime,
       "alaPimNeighborDRPriorityPresent": alaPimNeighborDRPriorityPresent,
       "alaPimNeighborDRPriority": alaPimNeighborDRPriority,
       "alaPimNeighborLanPruneDelayPresent": alaPimNeighborLanPruneDelayPresent,
       "alaPimNeighborTBit": alaPimNeighborTBit,
       "alaPimNeighborPropagationDelay": alaPimNeighborPropagationDelay,
       "alaPimNeighborOverrideInterval": alaPimNeighborOverrideInterval,
       "alaPimNeighborBidirCapable": alaPimNeighborBidirCapable,
       "alaPimNeighborSRCapable": alaPimNeighborSRCapable,
       "alaPimNbrSecAddressTable": alaPimNbrSecAddressTable,
       "alaPimNbrSecAddressEntry": alaPimNbrSecAddressEntry,
       "alaPimNbrSecAddressIfIndex": alaPimNbrSecAddressIfIndex,
       "alaPimNbrSecAddressType": alaPimNbrSecAddressType,
       "alaPimNbrSecAddressPrimary": alaPimNbrSecAddressPrimary,
       "alaPimNbrSecAddress": alaPimNbrSecAddress,
       "alaPimStarGTable": alaPimStarGTable,
       "alaPimStarGEntry": alaPimStarGEntry,
       "alaPimStarGAddressType": alaPimStarGAddressType,
       "alaPimStarGGrpAddress": alaPimStarGGrpAddress,
       "alaPimStarGUpTime": alaPimStarGUpTime,
       "alaPimStarGPimMode": alaPimStarGPimMode,
       "alaPimStarGRPAddressType": alaPimStarGRPAddressType,
       "alaPimStarGRPAddress": alaPimStarGRPAddress,
       "alaPimStarGPimModeOrigin": alaPimStarGPimModeOrigin,
       "alaPimStarGRPIsLocal": alaPimStarGRPIsLocal,
       "alaPimStarGUpstreamJoinState": alaPimStarGUpstreamJoinState,
       "alaPimStarGUpstreamJoinTimer": alaPimStarGUpstreamJoinTimer,
       "alaPimStarGUpstreamNeighborType": alaPimStarGUpstreamNeighborType,
       "alaPimStarGUpstreamNeighbor": alaPimStarGUpstreamNeighbor,
       "alaPimStarGRPFIfIndex": alaPimStarGRPFIfIndex,
       "alaPimStarGRPFNextHopType": alaPimStarGRPFNextHopType,
       "alaPimStarGRPFNextHop": alaPimStarGRPFNextHop,
       "alaPimStarGRPFRouteProtocol": alaPimStarGRPFRouteProtocol,
       "alaPimStarGRPFRouteAddress": alaPimStarGRPFRouteAddress,
       "alaPimStarGRPFRoutePrefixLength": alaPimStarGRPFRoutePrefixLength,
       "alaPimStarGRPFRouteMetricPref": alaPimStarGRPFRouteMetricPref,
       "alaPimStarGRPFRouteMetric": alaPimStarGRPFRouteMetric,
       "alaPimStarGITable": alaPimStarGITable,
       "alaPimStarGIEntry": alaPimStarGIEntry,
       "alaPimStarGIIfIndex": alaPimStarGIIfIndex,
       "alaPimStarGIUpTime": alaPimStarGIUpTime,
       "alaPimStarGILocalMembership": alaPimStarGILocalMembership,
       "alaPimStarGIJoinPruneState": alaPimStarGIJoinPruneState,
       "alaPimStarGIPrunePendingTimer": alaPimStarGIPrunePendingTimer,
       "alaPimStarGIJoinExpiryTimer": alaPimStarGIJoinExpiryTimer,
       "alaPimStarGIAssertState": alaPimStarGIAssertState,
       "alaPimStarGIAssertTimer": alaPimStarGIAssertTimer,
       "alaPimStarGIAssertWinnerAddressType": alaPimStarGIAssertWinnerAddressType,
       "alaPimStarGIAssertWinnerAddress": alaPimStarGIAssertWinnerAddress,
       "alaPimStarGIAssertWinnerMetricPref": alaPimStarGIAssertWinnerMetricPref,
       "alaPimStarGIAssertWinnerMetric": alaPimStarGIAssertWinnerMetric,
       "alaPimSGTable": alaPimSGTable,
       "alaPimSGEntry": alaPimSGEntry,
       "alaPimSGAddressType": alaPimSGAddressType,
       "alaPimSGGrpAddress": alaPimSGGrpAddress,
       "alaPimSGSrcAddress": alaPimSGSrcAddress,
       "alaPimSGUpTime": alaPimSGUpTime,
       "alaPimSGPimMode": alaPimSGPimMode,
       "alaPimSGUpstreamJoinState": alaPimSGUpstreamJoinState,
       "alaPimSGUpstreamJoinTimer": alaPimSGUpstreamJoinTimer,
       "alaPimSGUpstreamNeighbor": alaPimSGUpstreamNeighbor,
       "alaPimSGRPFIfIndex": alaPimSGRPFIfIndex,
       "alaPimSGRPFNextHopType": alaPimSGRPFNextHopType,
       "alaPimSGRPFNextHop": alaPimSGRPFNextHop,
       "alaPimSGRPFRouteProtocol": alaPimSGRPFRouteProtocol,
       "alaPimSGRPFRouteAddress": alaPimSGRPFRouteAddress,
       "alaPimSGRPFRoutePrefixLength": alaPimSGRPFRoutePrefixLength,
       "alaPimSGRPFRouteMetricPref": alaPimSGRPFRouteMetricPref,
       "alaPimSGRPFRouteMetric": alaPimSGRPFRouteMetric,
       "alaPimSGSPTBit": alaPimSGSPTBit,
       "alaPimSGKeepaliveTimer": alaPimSGKeepaliveTimer,
       "alaPimSGDRRegisterState": alaPimSGDRRegisterState,
       "alaPimSGDRRegisterStopTimer": alaPimSGDRRegisterStopTimer,
       "alaPimSGRPRegisterPMBRAddressType": alaPimSGRPRegisterPMBRAddressType,
       "alaPimSGRPRegisterPMBRAddress": alaPimSGRPRegisterPMBRAddress,
       "alaPimSGUpstreamPruneState": alaPimSGUpstreamPruneState,
       "alaPimSGUpstreamPruneLimitTimer": alaPimSGUpstreamPruneLimitTimer,
       "alaPimSGOriginatorState": alaPimSGOriginatorState,
       "alaPimSGSourceActiveTimer": alaPimSGSourceActiveTimer,
       "alaPimSGStateRefreshTimer": alaPimSGStateRefreshTimer,
       "alaPimSGITable": alaPimSGITable,
       "alaPimSGIEntry": alaPimSGIEntry,
       "alaPimSGIIfIndex": alaPimSGIIfIndex,
       "alaPimSGIUpTime": alaPimSGIUpTime,
       "alaPimSGILocalMembership": alaPimSGILocalMembership,
       "alaPimSGIJoinPruneState": alaPimSGIJoinPruneState,
       "alaPimSGIPrunePendingTimer": alaPimSGIPrunePendingTimer,
       "alaPimSGIJoinExpiryTimer": alaPimSGIJoinExpiryTimer,
       "alaPimSGIAssertState": alaPimSGIAssertState,
       "alaPimSGIAssertTimer": alaPimSGIAssertTimer,
       "alaPimSGIAssertWinnerAddressType": alaPimSGIAssertWinnerAddressType,
       "alaPimSGIAssertWinnerAddress": alaPimSGIAssertWinnerAddress,
       "alaPimSGIAssertWinnerMetricPref": alaPimSGIAssertWinnerMetricPref,
       "alaPimSGIAssertWinnerMetric": alaPimSGIAssertWinnerMetric,
       "alaPimSGRptTable": alaPimSGRptTable,
       "alaPimSGRptEntry": alaPimSGRptEntry,
       "alaPimSGRptSrcAddress": alaPimSGRptSrcAddress,
       "alaPimSGRptUpTime": alaPimSGRptUpTime,
       "alaPimSGRptUpstreamPruneState": alaPimSGRptUpstreamPruneState,
       "alaPimSGRptUpstreamOverrideTimer": alaPimSGRptUpstreamOverrideTimer,
       "alaPimSGRptITable": alaPimSGRptITable,
       "alaPimSGRptIEntry": alaPimSGRptIEntry,
       "alaPimSGRptIIfIndex": alaPimSGRptIIfIndex,
       "alaPimSGRptIUpTime": alaPimSGRptIUpTime,
       "alaPimSGRptILocalMembership": alaPimSGRptILocalMembership,
       "alaPimSGRptIJoinPruneState": alaPimSGRptIJoinPruneState,
       "alaPimSGRptIPrunePendingTimer": alaPimSGRptIPrunePendingTimer,
       "alaPimSGRptIPruneExpiryTimer": alaPimSGRptIPruneExpiryTimer,
       "alaPimStaticRPTable": alaPimStaticRPTable,
       "alaPimStaticRPEntry": alaPimStaticRPEntry,
       "alaPimStaticRPAddressType": alaPimStaticRPAddressType,
       "alaPimStaticRPGrpAddress": alaPimStaticRPGrpAddress,
       "alaPimStaticRPGrpPrefixLength": alaPimStaticRPGrpPrefixLength,
       "alaPimStaticRPRPAddress": alaPimStaticRPRPAddress,
       "alaPimStaticRPPimMode": alaPimStaticRPPimMode,
       "alaPimStaticRPOverrideDynamic": alaPimStaticRPOverrideDynamic,
       "alaPimStaticRPPrecedence": alaPimStaticRPPrecedence,
       "alaPimStaticRPRowStatus": alaPimStaticRPRowStatus,
       "alaPimStaticRPStorageType": alaPimStaticRPStorageType,
       "alaPimGroupMappingTable": alaPimGroupMappingTable,
       "alaPimGroupMappingEntry": alaPimGroupMappingEntry,
       "alaPimGroupMappingOrigin": alaPimGroupMappingOrigin,
       "alaPimGroupMappingAddressType": alaPimGroupMappingAddressType,
       "alaPimGroupMappingGrpAddress": alaPimGroupMappingGrpAddress,
       "alaPimGroupMappingGrpPrefixLength": alaPimGroupMappingGrpPrefixLength,
       "alaPimGroupMappingRPAddressType": alaPimGroupMappingRPAddressType,
       "alaPimGroupMappingRPAddress": alaPimGroupMappingRPAddress,
       "alaPimGroupMappingPimMode": alaPimGroupMappingPimMode,
       "alaPimGroupMappingPrecedence": alaPimGroupMappingPrecedence,
       "alaPimKeepalivePeriod": alaPimKeepalivePeriod,
       "alaPimRegisterSuppressionTime": alaPimRegisterSuppressionTime,
       "alaPimStarGEntries": alaPimStarGEntries,
       "alaPimStarGIEntries": alaPimStarGIEntries,
       "alaPimSGEntries": alaPimSGEntries,
       "alaPimSGIEntries": alaPimSGIEntries,
       "alaPimSGRptEntries": alaPimSGRptEntries,
       "alaPimSGRptIEntries": alaPimSGRptIEntries,
       "alaPimOutAsserts": alaPimOutAsserts,
       "alaPimInAsserts": alaPimInAsserts,
       "alaPimLastAssertInterface": alaPimLastAssertInterface,
       "alaPimLastAssertGroupAddressType": alaPimLastAssertGroupAddressType,
       "alaPimLastAssertGroupAddress": alaPimLastAssertGroupAddress,
       "alaPimLastAssertSourceAddressType": alaPimLastAssertSourceAddressType,
       "alaPimLastAssertSourceAddress": alaPimLastAssertSourceAddress,
       "alaPimNeighborLossNotificationPeriod": alaPimNeighborLossNotificationPeriod,
       "alaPimNeighborLossCount": alaPimNeighborLossCount,
       "alaPimInvalidRegisterNotificationPeriod": alaPimInvalidRegisterNotificationPeriod,
       "alaPimInvalidRegisterMsgsRcvd": alaPimInvalidRegisterMsgsRcvd,
       "alaPimInvalidRegisterAddressType": alaPimInvalidRegisterAddressType,
       "alaPimInvalidRegisterOrigin": alaPimInvalidRegisterOrigin,
       "alaPimInvalidRegisterGroup": alaPimInvalidRegisterGroup,
       "alaPimInvalidRegisterRp": alaPimInvalidRegisterRp,
       "alaPimInvalidJoinPruneNotificationPeriod": alaPimInvalidJoinPruneNotificationPeriod,
       "alaPimInvalidJoinPruneMsgsRcvd": alaPimInvalidJoinPruneMsgsRcvd,
       "alaPimInvalidJoinPruneAddressType": alaPimInvalidJoinPruneAddressType,
       "alaPimInvalidJoinPruneOrigin": alaPimInvalidJoinPruneOrigin,
       "alaPimInvalidJoinPruneGroup": alaPimInvalidJoinPruneGroup,
       "alaPimInvalidJoinPruneRp": alaPimInvalidJoinPruneRp,
       "alaPimRPMappingNotificationPeriod": alaPimRPMappingNotificationPeriod,
       "alaPimRPMappingChangeCount": alaPimRPMappingChangeCount,
       "alaPimInterfaceElectionNotificationPeriod": alaPimInterfaceElectionNotificationPeriod,
       "alaPimInterfaceElectionWinCount": alaPimInterfaceElectionWinCount,
       "alaPimRefreshInterval": alaPimRefreshInterval,
       "alaPimDeviceConfigStorageType": alaPimDeviceConfigStorageType,
       "alaPimMIBConformance": alaPimMIBConformance,
       "alaPimMIBCompliances": alaPimMIBCompliances,
       "alaPimMIBComplianceAsm": alaPimMIBComplianceAsm,
       "alaPimMIBComplianceSsm": alaPimMIBComplianceSsm,
       "alaPimMIBComplianceDm": alaPimMIBComplianceDm,
       "alaPimMIBGroups": alaPimMIBGroups,
       "alaPimTopologyGroup": alaPimTopologyGroup,
       "alaPimNotificationGroup": alaPimNotificationGroup,
       "alaPimTuningParametersGroup": alaPimTuningParametersGroup,
       "alaPimRouterStatisticsGroup": alaPimRouterStatisticsGroup,
       "alaPimSsmGroup": alaPimSsmGroup,
       "alaPimRPConfigGroup": alaPimRPConfigGroup,
       "alaPimSmGroup": alaPimSmGroup,
       "alaPimStaticRPPrecedenceGroup": alaPimStaticRPPrecedenceGroup,
       "alaPimNetMgmtNotificationObjects": alaPimNetMgmtNotificationObjects,
       "alaPimNetMgmtNotificationGroup": alaPimNetMgmtNotificationGroup,
       "alaPimDiagnosticsGroup": alaPimDiagnosticsGroup,
       "alaPimDmGroup": alaPimDmGroup,
       "alaPimDeviceStorageGroup": alaPimDeviceStorageGroup}
)
