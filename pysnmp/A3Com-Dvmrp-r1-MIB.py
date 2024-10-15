# SNMP MIB module (A3COM-DVMRP-R1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-DVMRP-R1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:12 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_BrouterMIB_ObjectIdentity = ObjectIdentity
brouterMIB = _BrouterMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2)
)
_A3ComDVMRP_ObjectIdentity = ObjectIdentity
a3ComDVMRP = _A3ComDVMRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 28)
)
_A3ComDvmrpSConfig_ObjectIdentity = ObjectIdentity
a3ComDvmrpSConfig = _A3ComDvmrpSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1)
)


class _A3ComDvmrpCacheTime_Type(Integer32):
    """Custom type a3ComDvmrpCacheTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_A3ComDvmrpCacheTime_Type.__name__ = "Integer32"
_A3ComDvmrpCacheTime_Object = MibScalar
a3ComDvmrpCacheTime = _A3ComDvmrpCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 1),
    _A3ComDvmrpCacheTime_Type()
)
a3ComDvmrpCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpCacheTime.setStatus("mandatory")


class _A3ComDvmrpPrune_Type(Integer32):
    """Custom type a3ComDvmrpPrune based on Integer32"""
    defaultValue = 1

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


_A3ComDvmrpPrune_Type.__name__ = "Integer32"
_A3ComDvmrpPrune_Object = MibScalar
a3ComDvmrpPrune = _A3ComDvmrpPrune_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 2),
    _A3ComDvmrpPrune_Type()
)
a3ComDvmrpPrune.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpPrune.setStatus("mandatory")


class _A3ComDvmrpUpdateTime_Type(Integer32):
    """Custom type a3ComDvmrpUpdateTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 5400),
    )


_A3ComDvmrpUpdateTime_Type.__name__ = "Integer32"
_A3ComDvmrpUpdateTime_Object = MibScalar
a3ComDvmrpUpdateTime = _A3ComDvmrpUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 3),
    _A3ComDvmrpUpdateTime_Type()
)
a3ComDvmrpUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpUpdateTime.setStatus("mandatory")


class _A3ComDvmrpMospfPolicy_Type(Integer32):
    """Custom type a3ComDvmrpMospfPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mospf", 1),
          ("noMospf", 2))
    )


_A3ComDvmrpMospfPolicy_Type.__name__ = "Integer32"
_A3ComDvmrpMospfPolicy_Object = MibScalar
a3ComDvmrpMospfPolicy = _A3ComDvmrpMospfPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 4),
    _A3ComDvmrpMospfPolicy_Type()
)
a3ComDvmrpMospfPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfPolicy.setStatus("mandatory")


class _A3ComDvmrpDestGroupPolicy_Type(Integer32):
    """Custom type a3ComDvmrpDestGroupPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destGroup", 1),
          ("noDestGroup", 2))
    )


_A3ComDvmrpDestGroupPolicy_Type.__name__ = "Integer32"
_A3ComDvmrpDestGroupPolicy_Object = MibScalar
a3ComDvmrpDestGroupPolicy = _A3ComDvmrpDestGroupPolicy_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 1, 5),
    _A3ComDvmrpDestGroupPolicy_Type()
)
a3ComDvmrpDestGroupPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupPolicy.setStatus("mandatory")
_A3ComDvmrpCConfig_ObjectIdentity = ObjectIdentity
a3ComDvmrpCConfig = _A3ComDvmrpCConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2)
)
_A3ComDvmrpPortTable_Object = MibTable
a3ComDvmrpPortTable = _A3ComDvmrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1)
)
if mibBuilder.loadTexts:
    a3ComDvmrpPortTable.setStatus("mandatory")
_A3ComDvmrpPortEntry_Object = MibTableRow
a3ComDvmrpPortEntry = _A3ComDvmrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1)
)
a3ComDvmrpPortEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpPortIndex"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpPortEntry.setStatus("mandatory")
_A3ComDvmrpPortIndex_Type = Integer32
_A3ComDvmrpPortIndex_Object = MibTableColumn
a3ComDvmrpPortIndex = _A3ComDvmrpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 1),
    _A3ComDvmrpPortIndex_Type()
)
a3ComDvmrpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpPortIndex.setStatus("mandatory")


class _A3ComDvmrpPortControl_Type(Integer32):
    """Custom type a3ComDvmrpPortControl based on Integer32"""
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


_A3ComDvmrpPortControl_Type.__name__ = "Integer32"
_A3ComDvmrpPortControl_Object = MibTableColumn
a3ComDvmrpPortControl = _A3ComDvmrpPortControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 2),
    _A3ComDvmrpPortControl_Type()
)
a3ComDvmrpPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpPortControl.setStatus("mandatory")


class _A3ComDvmrpPortMetric_Type(Integer32):
    """Custom type a3ComDvmrpPortMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_A3ComDvmrpPortMetric_Type.__name__ = "Integer32"
_A3ComDvmrpPortMetric_Object = MibTableColumn
a3ComDvmrpPortMetric = _A3ComDvmrpPortMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 3),
    _A3ComDvmrpPortMetric_Type()
)
a3ComDvmrpPortMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpPortMetric.setStatus("mandatory")


class _A3ComDvmrpPortRateLimit_Type(Integer32):
    """Custom type a3ComDvmrpPortRateLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_A3ComDvmrpPortRateLimit_Type.__name__ = "Integer32"
_A3ComDvmrpPortRateLimit_Object = MibTableColumn
a3ComDvmrpPortRateLimit = _A3ComDvmrpPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 4),
    _A3ComDvmrpPortRateLimit_Type()
)
a3ComDvmrpPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpPortRateLimit.setStatus("mandatory")


class _A3ComDvmrpPortAggregateCtrl_Type(Integer32):
    """Custom type a3ComDvmrpPortAggregateCtrl based on Integer32"""
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


_A3ComDvmrpPortAggregateCtrl_Type.__name__ = "Integer32"
_A3ComDvmrpPortAggregateCtrl_Object = MibTableColumn
a3ComDvmrpPortAggregateCtrl = _A3ComDvmrpPortAggregateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 1, 1, 5),
    _A3ComDvmrpPortAggregateCtrl_Type()
)
a3ComDvmrpPortAggregateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpPortAggregateCtrl.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrTable_Object = MibTable
a3ComDvmrpBoundaryAddrTable = _A3ComDvmrpBoundaryAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2)
)
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrTable.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrEntry_Object = MibTableRow
a3ComDvmrpBoundaryAddrEntry = _A3ComDvmrpBoundaryAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1)
)
a3ComDvmrpBoundaryAddrEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpBoundaryAddrPort"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpBoundaryAddrIpAddr"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrEntry.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrPort_Type = Integer32
_A3ComDvmrpBoundaryAddrPort_Object = MibTableColumn
a3ComDvmrpBoundaryAddrPort = _A3ComDvmrpBoundaryAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 1),
    _A3ComDvmrpBoundaryAddrPort_Type()
)
a3ComDvmrpBoundaryAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrPort.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrIpAddr_Type = IpAddress
_A3ComDvmrpBoundaryAddrIpAddr_Object = MibTableColumn
a3ComDvmrpBoundaryAddrIpAddr = _A3ComDvmrpBoundaryAddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 2),
    _A3ComDvmrpBoundaryAddrIpAddr_Type()
)
a3ComDvmrpBoundaryAddrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrIpAddr.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrMask_Type = IpAddress
_A3ComDvmrpBoundaryAddrMask_Object = MibTableColumn
a3ComDvmrpBoundaryAddrMask = _A3ComDvmrpBoundaryAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 3),
    _A3ComDvmrpBoundaryAddrMask_Type()
)
a3ComDvmrpBoundaryAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrMask.setStatus("mandatory")
_A3ComDvmrpBoundaryAddrStatus_Type = RowStatus
_A3ComDvmrpBoundaryAddrStatus_Object = MibTableColumn
a3ComDvmrpBoundaryAddrStatus = _A3ComDvmrpBoundaryAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 2, 1, 4),
    _A3ComDvmrpBoundaryAddrStatus_Type()
)
a3ComDvmrpBoundaryAddrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpBoundaryAddrStatus.setStatus("mandatory")
_A3ComDvmrpMospfTable_Object = MibTable
a3ComDvmrpMospfTable = _A3ComDvmrpMospfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3)
)
if mibBuilder.loadTexts:
    a3ComDvmrpMospfTable.setStatus("mandatory")
_A3ComDvmrpMospfEntry_Object = MibTableRow
a3ComDvmrpMospfEntry = _A3ComDvmrpMospfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1)
)
a3ComDvmrpMospfEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpMospfIpAddr"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpMospfIpMask"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpMospfEntry.setStatus("mandatory")
_A3ComDvmrpMospfIpAddr_Type = IpAddress
_A3ComDvmrpMospfIpAddr_Object = MibTableColumn
a3ComDvmrpMospfIpAddr = _A3ComDvmrpMospfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 1),
    _A3ComDvmrpMospfIpAddr_Type()
)
a3ComDvmrpMospfIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfIpAddr.setStatus("mandatory")
_A3ComDvmrpMospfIpMask_Type = Integer32
_A3ComDvmrpMospfIpMask_Object = MibTableColumn
a3ComDvmrpMospfIpMask = _A3ComDvmrpMospfIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 2),
    _A3ComDvmrpMospfIpMask_Type()
)
a3ComDvmrpMospfIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfIpMask.setStatus("mandatory")


class _A3ComDvmrpMospfMetric_Type(Integer32):
    """Custom type a3ComDvmrpMospfMetric based on Integer32"""
    defaultValue = 1


_A3ComDvmrpMospfMetric_Object = MibTableColumn
a3ComDvmrpMospfMetric = _A3ComDvmrpMospfMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 3),
    _A3ComDvmrpMospfMetric_Type()
)
a3ComDvmrpMospfMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfMetric.setStatus("mandatory")


class _A3ComDvmrpMospfAction_Type(Integer32):
    """Custom type a3ComDvmrpMospfAction based on Integer32"""
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
        *(("aggregate", 1),
          ("individual", 2),
          ("reject", 3))
    )


_A3ComDvmrpMospfAction_Type.__name__ = "Integer32"
_A3ComDvmrpMospfAction_Object = MibTableColumn
a3ComDvmrpMospfAction = _A3ComDvmrpMospfAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 4),
    _A3ComDvmrpMospfAction_Type()
)
a3ComDvmrpMospfAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfAction.setStatus("mandatory")
_A3ComDvmrpMospfStatus_Type = RowStatus
_A3ComDvmrpMospfStatus_Object = MibTableColumn
a3ComDvmrpMospfStatus = _A3ComDvmrpMospfStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 3, 1, 5),
    _A3ComDvmrpMospfStatus_Type()
)
a3ComDvmrpMospfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpMospfStatus.setStatus("mandatory")
_A3ComDvmrpNeighborTable_Object = MibTable
a3ComDvmrpNeighborTable = _A3ComDvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4)
)
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborTable.setStatus("mandatory")
_A3ComDvmrpNeighborEntry_Object = MibTableRow
a3ComDvmrpNeighborEntry = _A3ComDvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1)
)
a3ComDvmrpNeighborEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborPort"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborType"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNeighborAddr"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborEntry.setStatus("mandatory")
_A3ComDvmrpNeighborPort_Type = Integer32
_A3ComDvmrpNeighborPort_Object = MibTableColumn
a3ComDvmrpNeighborPort = _A3ComDvmrpNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 1),
    _A3ComDvmrpNeighborPort_Type()
)
a3ComDvmrpNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborPort.setStatus("mandatory")


class _A3ComDvmrpNeighborType_Type(Integer32):
    """Custom type a3ComDvmrpNeighborType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("frame-relay", 4),
          ("x25", 2))
    )


_A3ComDvmrpNeighborType_Type.__name__ = "Integer32"
_A3ComDvmrpNeighborType_Object = MibTableColumn
a3ComDvmrpNeighborType = _A3ComDvmrpNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 2),
    _A3ComDvmrpNeighborType_Type()
)
a3ComDvmrpNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborType.setStatus("mandatory")
_A3ComDvmrpNeighborAddr_Type = PhysAddress
_A3ComDvmrpNeighborAddr_Object = MibTableColumn
a3ComDvmrpNeighborAddr = _A3ComDvmrpNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 3),
    _A3ComDvmrpNeighborAddr_Type()
)
a3ComDvmrpNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborAddr.setStatus("mandatory")
_A3ComDvmrpNeighborStatus_Type = RowStatus
_A3ComDvmrpNeighborStatus_Object = MibTableColumn
a3ComDvmrpNeighborStatus = _A3ComDvmrpNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 4, 1, 4),
    _A3ComDvmrpNeighborStatus_Type()
)
a3ComDvmrpNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpNeighborStatus.setStatus("mandatory")
_A3ComDvmrpTunnelTable_Object = MibTable
a3ComDvmrpTunnelTable = _A3ComDvmrpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5)
)
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelTable.setStatus("mandatory")
_A3ComDvmrpTunnelEntry_Object = MibTableRow
a3ComDvmrpTunnelEntry = _A3ComDvmrpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1)
)
a3ComDvmrpTunnelEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpTunnelId"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelEntry.setStatus("mandatory")
_A3ComDvmrpTunnelId_Type = Integer32
_A3ComDvmrpTunnelId_Object = MibTableColumn
a3ComDvmrpTunnelId = _A3ComDvmrpTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 1),
    _A3ComDvmrpTunnelId_Type()
)
a3ComDvmrpTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelId.setStatus("mandatory")
_A3ComDvmrpTunnelLocalIp_Type = IpAddress
_A3ComDvmrpTunnelLocalIp_Object = MibTableColumn
a3ComDvmrpTunnelLocalIp = _A3ComDvmrpTunnelLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 2),
    _A3ComDvmrpTunnelLocalIp_Type()
)
a3ComDvmrpTunnelLocalIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelLocalIp.setStatus("mandatory")
_A3ComDvmrpTunnelRemoteIp_Type = IpAddress
_A3ComDvmrpTunnelRemoteIp_Object = MibTableColumn
a3ComDvmrpTunnelRemoteIp = _A3ComDvmrpTunnelRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 3),
    _A3ComDvmrpTunnelRemoteIp_Type()
)
a3ComDvmrpTunnelRemoteIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelRemoteIp.setStatus("mandatory")


class _A3ComDvmrpTunnelTtl_Type(Integer32):
    """Custom type a3ComDvmrpTunnelTtl based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_A3ComDvmrpTunnelTtl_Type.__name__ = "Integer32"
_A3ComDvmrpTunnelTtl_Object = MibTableColumn
a3ComDvmrpTunnelTtl = _A3ComDvmrpTunnelTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 4),
    _A3ComDvmrpTunnelTtl_Type()
)
a3ComDvmrpTunnelTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelTtl.setStatus("mandatory")
_A3ComDvmrpTunnelStatus_Type = RowStatus
_A3ComDvmrpTunnelStatus_Object = MibTableColumn
a3ComDvmrpTunnelStatus = _A3ComDvmrpTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 5, 1, 5),
    _A3ComDvmrpTunnelStatus_Type()
)
a3ComDvmrpTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpTunnelStatus.setStatus("mandatory")
_A3ComDvmrpAggreExceptTable_Object = MibTable
a3ComDvmrpAggreExceptTable = _A3ComDvmrpAggreExceptTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6)
)
if mibBuilder.loadTexts:
    a3ComDvmrpAggreExceptTable.setStatus("mandatory")
_A3ComDvmrpAggreExceptEntry_Object = MibTableRow
a3ComDvmrpAggreExceptEntry = _A3ComDvmrpAggreExceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1)
)
a3ComDvmrpAggreExceptEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreExceptIpAddr"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreExceptIpMask"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpAggreExceptEntry.setStatus("mandatory")
_A3ComDvmrpAggreExceptIpAddr_Type = IpAddress
_A3ComDvmrpAggreExceptIpAddr_Object = MibTableColumn
a3ComDvmrpAggreExceptIpAddr = _A3ComDvmrpAggreExceptIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 1),
    _A3ComDvmrpAggreExceptIpAddr_Type()
)
a3ComDvmrpAggreExceptIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreExceptIpAddr.setStatus("mandatory")


class _A3ComDvmrpAggreExceptIpMask_Type(Integer32):
    """Custom type a3ComDvmrpAggreExceptIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_A3ComDvmrpAggreExceptIpMask_Type.__name__ = "Integer32"
_A3ComDvmrpAggreExceptIpMask_Object = MibTableColumn
a3ComDvmrpAggreExceptIpMask = _A3ComDvmrpAggreExceptIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 2),
    _A3ComDvmrpAggreExceptIpMask_Type()
)
a3ComDvmrpAggreExceptIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreExceptIpMask.setStatus("mandatory")
_A3ComDvmrpAggreExceptStatus_Type = RowStatus
_A3ComDvmrpAggreExceptStatus_Object = MibTableColumn
a3ComDvmrpAggreExceptStatus = _A3ComDvmrpAggreExceptStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 6, 1, 3),
    _A3ComDvmrpAggreExceptStatus_Type()
)
a3ComDvmrpAggreExceptStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreExceptStatus.setStatus("mandatory")
_A3ComDvmrpAggreRangeTable_Object = MibTable
a3ComDvmrpAggreRangeTable = _A3ComDvmrpAggreRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7)
)
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeTable.setStatus("mandatory")
_A3ComDvmrpAggreRangeEntry_Object = MibTableRow
a3ComDvmrpAggreRangeEntry = _A3ComDvmrpAggreRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1)
)
a3ComDvmrpAggreRangeEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreRangeIpAddr"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpAggreRangeIpMask"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeEntry.setStatus("mandatory")
_A3ComDvmrpAggreRangeIpAddr_Type = IpAddress
_A3ComDvmrpAggreRangeIpAddr_Object = MibTableColumn
a3ComDvmrpAggreRangeIpAddr = _A3ComDvmrpAggreRangeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 1),
    _A3ComDvmrpAggreRangeIpAddr_Type()
)
a3ComDvmrpAggreRangeIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeIpAddr.setStatus("mandatory")


class _A3ComDvmrpAggreRangeIpMask_Type(Integer32):
    """Custom type a3ComDvmrpAggreRangeIpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_A3ComDvmrpAggreRangeIpMask_Type.__name__ = "Integer32"
_A3ComDvmrpAggreRangeIpMask_Object = MibTableColumn
a3ComDvmrpAggreRangeIpMask = _A3ComDvmrpAggreRangeIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 2),
    _A3ComDvmrpAggreRangeIpMask_Type()
)
a3ComDvmrpAggreRangeIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeIpMask.setStatus("mandatory")


class _A3ComDvmrpAggreRangeMetric_Type(Integer32):
    """Custom type a3ComDvmrpAggreRangeMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_A3ComDvmrpAggreRangeMetric_Type.__name__ = "Integer32"
_A3ComDvmrpAggreRangeMetric_Object = MibTableColumn
a3ComDvmrpAggreRangeMetric = _A3ComDvmrpAggreRangeMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 3),
    _A3ComDvmrpAggreRangeMetric_Type()
)
a3ComDvmrpAggreRangeMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeMetric.setStatus("mandatory")
_A3ComDvmrpAggreRangeStatus_Type = RowStatus
_A3ComDvmrpAggreRangeStatus_Object = MibTableColumn
a3ComDvmrpAggreRangeStatus = _A3ComDvmrpAggreRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 7, 1, 4),
    _A3ComDvmrpAggreRangeStatus_Type()
)
a3ComDvmrpAggreRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpAggreRangeStatus.setStatus("mandatory")
_A3ComDvmrpDestGroupTable_Object = MibTable
a3ComDvmrpDestGroupTable = _A3ComDvmrpDestGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8)
)
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupTable.setStatus("mandatory")
_A3ComDvmrpDestGroupEntry_Object = MibTableRow
a3ComDvmrpDestGroupEntry = _A3ComDvmrpDestGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1)
)
a3ComDvmrpDestGroupEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpDestGroupIpAddr"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpDestGroupIpMask"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupEntry.setStatus("mandatory")
_A3ComDvmrpDestGroupIpAddr_Type = IpAddress
_A3ComDvmrpDestGroupIpAddr_Object = MibTableColumn
a3ComDvmrpDestGroupIpAddr = _A3ComDvmrpDestGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 1),
    _A3ComDvmrpDestGroupIpAddr_Type()
)
a3ComDvmrpDestGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupIpAddr.setStatus("mandatory")
_A3ComDvmrpDestGroupIpMask_Type = Integer32
_A3ComDvmrpDestGroupIpMask_Object = MibTableColumn
a3ComDvmrpDestGroupIpMask = _A3ComDvmrpDestGroupIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 2),
    _A3ComDvmrpDestGroupIpMask_Type()
)
a3ComDvmrpDestGroupIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupIpMask.setStatus("mandatory")


class _A3ComDvmrpDestGroupAction_Type(Integer32):
    """Custom type a3ComDvmrpDestGroupAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_A3ComDvmrpDestGroupAction_Type.__name__ = "Integer32"
_A3ComDvmrpDestGroupAction_Object = MibTableColumn
a3ComDvmrpDestGroupAction = _A3ComDvmrpDestGroupAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 3),
    _A3ComDvmrpDestGroupAction_Type()
)
a3ComDvmrpDestGroupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupAction.setStatus("mandatory")
_A3ComDvmrpDestGroupStatus_Type = RowStatus
_A3ComDvmrpDestGroupStatus_Object = MibTableColumn
a3ComDvmrpDestGroupStatus = _A3ComDvmrpDestGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 2, 8, 1, 4),
    _A3ComDvmrpDestGroupStatus_Type()
)
a3ComDvmrpDestGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComDvmrpDestGroupStatus.setStatus("mandatory")
_A3ComDvmrpData_ObjectIdentity = ObjectIdentity
a3ComDvmrpData = _A3ComDvmrpData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3)
)
_A3ComDvmrpRouteTable_Object = MibTable
a3ComDvmrpRouteTable = _A3ComDvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1)
)
if mibBuilder.loadTexts:
    a3ComDvmrpRouteTable.setStatus("mandatory")
_A3ComDvmrpRouteEntry_Object = MibTableRow
a3ComDvmrpRouteEntry = _A3ComDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1)
)
a3ComDvmrpRouteEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpRouteSource"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpRouteEntry.setStatus("mandatory")
_A3ComDvmrpRouteSource_Type = IpAddress
_A3ComDvmrpRouteSource_Object = MibTableColumn
a3ComDvmrpRouteSource = _A3ComDvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 1),
    _A3ComDvmrpRouteSource_Type()
)
a3ComDvmrpRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteSource.setStatus("mandatory")
_A3ComDvmrpRouteMask_Type = IpAddress
_A3ComDvmrpRouteMask_Object = MibTableColumn
a3ComDvmrpRouteMask = _A3ComDvmrpRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 2),
    _A3ComDvmrpRouteMask_Type()
)
a3ComDvmrpRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteMask.setStatus("mandatory")
_A3ComDvmrpRoutePreHop_Type = IpAddress
_A3ComDvmrpRoutePreHop_Object = MibTableColumn
a3ComDvmrpRoutePreHop = _A3ComDvmrpRoutePreHop_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 3),
    _A3ComDvmrpRoutePreHop_Type()
)
a3ComDvmrpRoutePreHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRoutePreHop.setStatus("mandatory")
_A3ComDvmrpRouteMetric_Type = Integer32
_A3ComDvmrpRouteMetric_Object = MibTableColumn
a3ComDvmrpRouteMetric = _A3ComDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 4),
    _A3ComDvmrpRouteMetric_Type()
)
a3ComDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteMetric.setStatus("mandatory")
_A3ComDvmrpRoutePort_Type = Integer32
_A3ComDvmrpRoutePort_Object = MibTableColumn
a3ComDvmrpRoutePort = _A3ComDvmrpRoutePort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 5),
    _A3ComDvmrpRoutePort_Type()
)
a3ComDvmrpRoutePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRoutePort.setStatus("mandatory")


class _A3ComDvmrpRouteType_Type(Integer32):
    """Custom type a3ComDvmrpRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("other", 1),
          ("remote", 3))
    )


_A3ComDvmrpRouteType_Type.__name__ = "Integer32"
_A3ComDvmrpRouteType_Object = MibTableColumn
a3ComDvmrpRouteType = _A3ComDvmrpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 6),
    _A3ComDvmrpRouteType_Type()
)
a3ComDvmrpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteType.setStatus("mandatory")


class _A3ComDvmrpRouteStatus_Type(Integer32):
    """Custom type a3ComDvmrpRouteStatus based on Integer32"""
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
        *(("down", 3),
          ("garbage-collection", 5),
          ("hold-down", 4),
          ("other", 1),
          ("up", 2))
    )


_A3ComDvmrpRouteStatus_Type.__name__ = "Integer32"
_A3ComDvmrpRouteStatus_Object = MibTableColumn
a3ComDvmrpRouteStatus = _A3ComDvmrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 7),
    _A3ComDvmrpRouteStatus_Type()
)
a3ComDvmrpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteStatus.setStatus("mandatory")


class _A3ComDvmrpRouteProtocol_Type(Integer32):
    """Custom type a3ComDvmrpRouteProtocol based on Integer32"""
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
        *(("cbt", 5),
          ("dvmrp", 3),
          ("mospf", 4),
          ("other", 1),
          ("pim", 6),
          ("static", 2))
    )


_A3ComDvmrpRouteProtocol_Type.__name__ = "Integer32"
_A3ComDvmrpRouteProtocol_Object = MibTableColumn
a3ComDvmrpRouteProtocol = _A3ComDvmrpRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 8),
    _A3ComDvmrpRouteProtocol_Type()
)
a3ComDvmrpRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteProtocol.setStatus("mandatory")
_A3ComDvmrpRouteTtl_Type = Integer32
_A3ComDvmrpRouteTtl_Object = MibTableColumn
a3ComDvmrpRouteTtl = _A3ComDvmrpRouteTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 9),
    _A3ComDvmrpRouteTtl_Type()
)
a3ComDvmrpRouteTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteTtl.setStatus("mandatory")
_A3ComDvmrpRouteChild_Type = OctetString
_A3ComDvmrpRouteChild_Object = MibTableColumn
a3ComDvmrpRouteChild = _A3ComDvmrpRouteChild_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 10),
    _A3ComDvmrpRouteChild_Type()
)
a3ComDvmrpRouteChild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteChild.setStatus("mandatory")
_A3ComDvmrpRouteChildTunnel_Type = OctetString
_A3ComDvmrpRouteChildTunnel_Object = MibTableColumn
a3ComDvmrpRouteChildTunnel = _A3ComDvmrpRouteChildTunnel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 11),
    _A3ComDvmrpRouteChildTunnel_Type()
)
a3ComDvmrpRouteChildTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteChildTunnel.setStatus("mandatory")
_A3ComDvmrpRouteLeaf_Type = OctetString
_A3ComDvmrpRouteLeaf_Object = MibTableColumn
a3ComDvmrpRouteLeaf = _A3ComDvmrpRouteLeaf_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 12),
    _A3ComDvmrpRouteLeaf_Type()
)
a3ComDvmrpRouteLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteLeaf.setStatus("mandatory")
_A3ComDvmrpRouteLeafTunnel_Type = OctetString
_A3ComDvmrpRouteLeafTunnel_Object = MibTableColumn
a3ComDvmrpRouteLeafTunnel = _A3ComDvmrpRouteLeafTunnel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 1, 1, 13),
    _A3ComDvmrpRouteLeafTunnel_Type()
)
a3ComDvmrpRouteLeafTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpRouteLeafTunnel.setStatus("mandatory")
_A3ComDvmrpForwardTable_Object = MibTable
a3ComDvmrpForwardTable = _A3ComDvmrpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2)
)
if mibBuilder.loadTexts:
    a3ComDvmrpForwardTable.setStatus("mandatory")
_A3ComDvmrpForwardEntry_Object = MibTableRow
a3ComDvmrpForwardEntry = _A3ComDvmrpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1)
)
a3ComDvmrpForwardEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpForwardSource"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpForwardGroup"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpForwardEntry.setStatus("mandatory")
_A3ComDvmrpForwardSource_Type = IpAddress
_A3ComDvmrpForwardSource_Object = MibTableColumn
a3ComDvmrpForwardSource = _A3ComDvmrpForwardSource_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 1),
    _A3ComDvmrpForwardSource_Type()
)
a3ComDvmrpForwardSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardSource.setStatus("mandatory")
_A3ComDvmrpForwardGroup_Type = IpAddress
_A3ComDvmrpForwardGroup_Object = MibTableColumn
a3ComDvmrpForwardGroup = _A3ComDvmrpForwardGroup_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 2),
    _A3ComDvmrpForwardGroup_Type()
)
a3ComDvmrpForwardGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardGroup.setStatus("mandatory")
_A3ComDvmrpForwardTtl_Type = Integer32
_A3ComDvmrpForwardTtl_Object = MibTableColumn
a3ComDvmrpForwardTtl = _A3ComDvmrpForwardTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 3),
    _A3ComDvmrpForwardTtl_Type()
)
a3ComDvmrpForwardTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardTtl.setStatus("mandatory")
_A3ComDvmrpForwardInPort_Type = Integer32
_A3ComDvmrpForwardInPort_Object = MibTableColumn
a3ComDvmrpForwardInPort = _A3ComDvmrpForwardInPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 4),
    _A3ComDvmrpForwardInPort_Type()
)
a3ComDvmrpForwardInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardInPort.setStatus("mandatory")
_A3ComDvmrpForwardOutPorts_Type = OctetString
_A3ComDvmrpForwardOutPorts_Object = MibTableColumn
a3ComDvmrpForwardOutPorts = _A3ComDvmrpForwardOutPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 5),
    _A3ComDvmrpForwardOutPorts_Type()
)
a3ComDvmrpForwardOutPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardOutPorts.setStatus("mandatory")
_A3ComDvmrpForwardOutPortsTunnel_Type = OctetString
_A3ComDvmrpForwardOutPortsTunnel_Object = MibTableColumn
a3ComDvmrpForwardOutPortsTunnel = _A3ComDvmrpForwardOutPortsTunnel_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 6),
    _A3ComDvmrpForwardOutPortsTunnel_Type()
)
a3ComDvmrpForwardOutPortsTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardOutPortsTunnel.setStatus("mandatory")


class _A3ComDvmrpForwardScoped_Type(Integer32):
    """Custom type a3ComDvmrpForwardScoped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpForwardScoped_Type.__name__ = "Integer32"
_A3ComDvmrpForwardScoped_Object = MibTableColumn
a3ComDvmrpForwardScoped = _A3ComDvmrpForwardScoped_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 7),
    _A3ComDvmrpForwardScoped_Type()
)
a3ComDvmrpForwardScoped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardScoped.setStatus("mandatory")


class _A3ComDvmrpForwardPruneSent_Type(Integer32):
    """Custom type a3ComDvmrpForwardPruneSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpForwardPruneSent_Type.__name__ = "Integer32"
_A3ComDvmrpForwardPruneSent_Object = MibTableColumn
a3ComDvmrpForwardPruneSent = _A3ComDvmrpForwardPruneSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 2, 1, 8),
    _A3ComDvmrpForwardPruneSent_Type()
)
a3ComDvmrpForwardPruneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpForwardPruneSent.setStatus("mandatory")
_A3ComDvmrpNbrRouterTable_Object = MibTable
a3ComDvmrpNbrRouterTable = _A3ComDvmrpNbrRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3)
)
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterTable.setStatus("mandatory")
_A3ComDvmrpNbrRouterEntry_Object = MibTableRow
a3ComDvmrpNbrRouterEntry = _A3ComDvmrpNbrRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1)
)
a3ComDvmrpNbrRouterEntry.setIndexNames(
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNbrRouterPort"),
    (0, "A3COM-DVMRP-R1-MIB", "a3ComDvmrpNbrRouterIpAddr"),
)
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterEntry.setStatus("mandatory")
_A3ComDvmrpNbrRouterPort_Type = Integer32
_A3ComDvmrpNbrRouterPort_Object = MibTableColumn
a3ComDvmrpNbrRouterPort = _A3ComDvmrpNbrRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 1),
    _A3ComDvmrpNbrRouterPort_Type()
)
a3ComDvmrpNbrRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterPort.setStatus("mandatory")
_A3ComDvmrpNbrRouterIpAddr_Type = IpAddress
_A3ComDvmrpNbrRouterIpAddr_Object = MibTableColumn
a3ComDvmrpNbrRouterIpAddr = _A3ComDvmrpNbrRouterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 2),
    _A3ComDvmrpNbrRouterIpAddr_Type()
)
a3ComDvmrpNbrRouterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterIpAddr.setStatus("mandatory")
_A3ComDvmrpNbrRouterGenId_Type = Integer32
_A3ComDvmrpNbrRouterGenId_Object = MibTableColumn
a3ComDvmrpNbrRouterGenId = _A3ComDvmrpNbrRouterGenId_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 3),
    _A3ComDvmrpNbrRouterGenId_Type()
)
a3ComDvmrpNbrRouterGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterGenId.setStatus("mandatory")
_A3ComDvmrpNbrRouterVerProtocol_Type = Integer32
_A3ComDvmrpNbrRouterVerProtocol_Object = MibTableColumn
a3ComDvmrpNbrRouterVerProtocol = _A3ComDvmrpNbrRouterVerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 4),
    _A3ComDvmrpNbrRouterVerProtocol_Type()
)
a3ComDvmrpNbrRouterVerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterVerProtocol.setStatus("mandatory")
_A3ComDvmrpNbrRouterVerMrouted_Type = Integer32
_A3ComDvmrpNbrRouterVerMrouted_Object = MibTableColumn
a3ComDvmrpNbrRouterVerMrouted = _A3ComDvmrpNbrRouterVerMrouted_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 5),
    _A3ComDvmrpNbrRouterVerMrouted_Type()
)
a3ComDvmrpNbrRouterVerMrouted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterVerMrouted.setStatus("mandatory")
_A3ComDvmrpNbrRouterTtl_Type = Integer32
_A3ComDvmrpNbrRouterTtl_Object = MibTableColumn
a3ComDvmrpNbrRouterTtl = _A3ComDvmrpNbrRouterTtl_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 6),
    _A3ComDvmrpNbrRouterTtl_Type()
)
a3ComDvmrpNbrRouterTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterTtl.setStatus("mandatory")


class _A3ComDvmrpNbrRouterLeafStatus_Type(Integer32):
    """Custom type a3ComDvmrpNbrRouterLeafStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpNbrRouterLeafStatus_Type.__name__ = "Integer32"
_A3ComDvmrpNbrRouterLeafStatus_Object = MibTableColumn
a3ComDvmrpNbrRouterLeafStatus = _A3ComDvmrpNbrRouterLeafStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 7),
    _A3ComDvmrpNbrRouterLeafStatus_Type()
)
a3ComDvmrpNbrRouterLeafStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterLeafStatus.setStatus("mandatory")


class _A3ComDvmrpNbrRouterPruneStatus_Type(Integer32):
    """Custom type a3ComDvmrpNbrRouterPruneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpNbrRouterPruneStatus_Type.__name__ = "Integer32"
_A3ComDvmrpNbrRouterPruneStatus_Object = MibTableColumn
a3ComDvmrpNbrRouterPruneStatus = _A3ComDvmrpNbrRouterPruneStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 8),
    _A3ComDvmrpNbrRouterPruneStatus_Type()
)
a3ComDvmrpNbrRouterPruneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterPruneStatus.setStatus("mandatory")


class _A3ComDvmrpNbrRouterGenIdStatus_Type(Integer32):
    """Custom type a3ComDvmrpNbrRouterGenIdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpNbrRouterGenIdStatus_Type.__name__ = "Integer32"
_A3ComDvmrpNbrRouterGenIdStatus_Object = MibTableColumn
a3ComDvmrpNbrRouterGenIdStatus = _A3ComDvmrpNbrRouterGenIdStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 9),
    _A3ComDvmrpNbrRouterGenIdStatus_Type()
)
a3ComDvmrpNbrRouterGenIdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterGenIdStatus.setStatus("mandatory")


class _A3ComDvmrpNbrRouterMtraceStatus_Type(Integer32):
    """Custom type a3ComDvmrpNbrRouterMtraceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_A3ComDvmrpNbrRouterMtraceStatus_Type.__name__ = "Integer32"
_A3ComDvmrpNbrRouterMtraceStatus_Object = MibTableColumn
a3ComDvmrpNbrRouterMtraceStatus = _A3ComDvmrpNbrRouterMtraceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 2, 28, 3, 3, 1, 10),
    _A3ComDvmrpNbrRouterMtraceStatus_Type()
)
a3ComDvmrpNbrRouterMtraceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComDvmrpNbrRouterMtraceStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-DVMRP-R1-MIB",
    **{"RowStatus": RowStatus,
       "a3Com": a3Com,
       "brouterMIB": brouterMIB,
       "a3ComDVMRP": a3ComDVMRP,
       "a3ComDvmrpSConfig": a3ComDvmrpSConfig,
       "a3ComDvmrpCacheTime": a3ComDvmrpCacheTime,
       "a3ComDvmrpPrune": a3ComDvmrpPrune,
       "a3ComDvmrpUpdateTime": a3ComDvmrpUpdateTime,
       "a3ComDvmrpMospfPolicy": a3ComDvmrpMospfPolicy,
       "a3ComDvmrpDestGroupPolicy": a3ComDvmrpDestGroupPolicy,
       "a3ComDvmrpCConfig": a3ComDvmrpCConfig,
       "a3ComDvmrpPortTable": a3ComDvmrpPortTable,
       "a3ComDvmrpPortEntry": a3ComDvmrpPortEntry,
       "a3ComDvmrpPortIndex": a3ComDvmrpPortIndex,
       "a3ComDvmrpPortControl": a3ComDvmrpPortControl,
       "a3ComDvmrpPortMetric": a3ComDvmrpPortMetric,
       "a3ComDvmrpPortRateLimit": a3ComDvmrpPortRateLimit,
       "a3ComDvmrpPortAggregateCtrl": a3ComDvmrpPortAggregateCtrl,
       "a3ComDvmrpBoundaryAddrTable": a3ComDvmrpBoundaryAddrTable,
       "a3ComDvmrpBoundaryAddrEntry": a3ComDvmrpBoundaryAddrEntry,
       "a3ComDvmrpBoundaryAddrPort": a3ComDvmrpBoundaryAddrPort,
       "a3ComDvmrpBoundaryAddrIpAddr": a3ComDvmrpBoundaryAddrIpAddr,
       "a3ComDvmrpBoundaryAddrMask": a3ComDvmrpBoundaryAddrMask,
       "a3ComDvmrpBoundaryAddrStatus": a3ComDvmrpBoundaryAddrStatus,
       "a3ComDvmrpMospfTable": a3ComDvmrpMospfTable,
       "a3ComDvmrpMospfEntry": a3ComDvmrpMospfEntry,
       "a3ComDvmrpMospfIpAddr": a3ComDvmrpMospfIpAddr,
       "a3ComDvmrpMospfIpMask": a3ComDvmrpMospfIpMask,
       "a3ComDvmrpMospfMetric": a3ComDvmrpMospfMetric,
       "a3ComDvmrpMospfAction": a3ComDvmrpMospfAction,
       "a3ComDvmrpMospfStatus": a3ComDvmrpMospfStatus,
       "a3ComDvmrpNeighborTable": a3ComDvmrpNeighborTable,
       "a3ComDvmrpNeighborEntry": a3ComDvmrpNeighborEntry,
       "a3ComDvmrpNeighborPort": a3ComDvmrpNeighborPort,
       "a3ComDvmrpNeighborType": a3ComDvmrpNeighborType,
       "a3ComDvmrpNeighborAddr": a3ComDvmrpNeighborAddr,
       "a3ComDvmrpNeighborStatus": a3ComDvmrpNeighborStatus,
       "a3ComDvmrpTunnelTable": a3ComDvmrpTunnelTable,
       "a3ComDvmrpTunnelEntry": a3ComDvmrpTunnelEntry,
       "a3ComDvmrpTunnelId": a3ComDvmrpTunnelId,
       "a3ComDvmrpTunnelLocalIp": a3ComDvmrpTunnelLocalIp,
       "a3ComDvmrpTunnelRemoteIp": a3ComDvmrpTunnelRemoteIp,
       "a3ComDvmrpTunnelTtl": a3ComDvmrpTunnelTtl,
       "a3ComDvmrpTunnelStatus": a3ComDvmrpTunnelStatus,
       "a3ComDvmrpAggreExceptTable": a3ComDvmrpAggreExceptTable,
       "a3ComDvmrpAggreExceptEntry": a3ComDvmrpAggreExceptEntry,
       "a3ComDvmrpAggreExceptIpAddr": a3ComDvmrpAggreExceptIpAddr,
       "a3ComDvmrpAggreExceptIpMask": a3ComDvmrpAggreExceptIpMask,
       "a3ComDvmrpAggreExceptStatus": a3ComDvmrpAggreExceptStatus,
       "a3ComDvmrpAggreRangeTable": a3ComDvmrpAggreRangeTable,
       "a3ComDvmrpAggreRangeEntry": a3ComDvmrpAggreRangeEntry,
       "a3ComDvmrpAggreRangeIpAddr": a3ComDvmrpAggreRangeIpAddr,
       "a3ComDvmrpAggreRangeIpMask": a3ComDvmrpAggreRangeIpMask,
       "a3ComDvmrpAggreRangeMetric": a3ComDvmrpAggreRangeMetric,
       "a3ComDvmrpAggreRangeStatus": a3ComDvmrpAggreRangeStatus,
       "a3ComDvmrpDestGroupTable": a3ComDvmrpDestGroupTable,
       "a3ComDvmrpDestGroupEntry": a3ComDvmrpDestGroupEntry,
       "a3ComDvmrpDestGroupIpAddr": a3ComDvmrpDestGroupIpAddr,
       "a3ComDvmrpDestGroupIpMask": a3ComDvmrpDestGroupIpMask,
       "a3ComDvmrpDestGroupAction": a3ComDvmrpDestGroupAction,
       "a3ComDvmrpDestGroupStatus": a3ComDvmrpDestGroupStatus,
       "a3ComDvmrpData": a3ComDvmrpData,
       "a3ComDvmrpRouteTable": a3ComDvmrpRouteTable,
       "a3ComDvmrpRouteEntry": a3ComDvmrpRouteEntry,
       "a3ComDvmrpRouteSource": a3ComDvmrpRouteSource,
       "a3ComDvmrpRouteMask": a3ComDvmrpRouteMask,
       "a3ComDvmrpRoutePreHop": a3ComDvmrpRoutePreHop,
       "a3ComDvmrpRouteMetric": a3ComDvmrpRouteMetric,
       "a3ComDvmrpRoutePort": a3ComDvmrpRoutePort,
       "a3ComDvmrpRouteType": a3ComDvmrpRouteType,
       "a3ComDvmrpRouteStatus": a3ComDvmrpRouteStatus,
       "a3ComDvmrpRouteProtocol": a3ComDvmrpRouteProtocol,
       "a3ComDvmrpRouteTtl": a3ComDvmrpRouteTtl,
       "a3ComDvmrpRouteChild": a3ComDvmrpRouteChild,
       "a3ComDvmrpRouteChildTunnel": a3ComDvmrpRouteChildTunnel,
       "a3ComDvmrpRouteLeaf": a3ComDvmrpRouteLeaf,
       "a3ComDvmrpRouteLeafTunnel": a3ComDvmrpRouteLeafTunnel,
       "a3ComDvmrpForwardTable": a3ComDvmrpForwardTable,
       "a3ComDvmrpForwardEntry": a3ComDvmrpForwardEntry,
       "a3ComDvmrpForwardSource": a3ComDvmrpForwardSource,
       "a3ComDvmrpForwardGroup": a3ComDvmrpForwardGroup,
       "a3ComDvmrpForwardTtl": a3ComDvmrpForwardTtl,
       "a3ComDvmrpForwardInPort": a3ComDvmrpForwardInPort,
       "a3ComDvmrpForwardOutPorts": a3ComDvmrpForwardOutPorts,
       "a3ComDvmrpForwardOutPortsTunnel": a3ComDvmrpForwardOutPortsTunnel,
       "a3ComDvmrpForwardScoped": a3ComDvmrpForwardScoped,
       "a3ComDvmrpForwardPruneSent": a3ComDvmrpForwardPruneSent,
       "a3ComDvmrpNbrRouterTable": a3ComDvmrpNbrRouterTable,
       "a3ComDvmrpNbrRouterEntry": a3ComDvmrpNbrRouterEntry,
       "a3ComDvmrpNbrRouterPort": a3ComDvmrpNbrRouterPort,
       "a3ComDvmrpNbrRouterIpAddr": a3ComDvmrpNbrRouterIpAddr,
       "a3ComDvmrpNbrRouterGenId": a3ComDvmrpNbrRouterGenId,
       "a3ComDvmrpNbrRouterVerProtocol": a3ComDvmrpNbrRouterVerProtocol,
       "a3ComDvmrpNbrRouterVerMrouted": a3ComDvmrpNbrRouterVerMrouted,
       "a3ComDvmrpNbrRouterTtl": a3ComDvmrpNbrRouterTtl,
       "a3ComDvmrpNbrRouterLeafStatus": a3ComDvmrpNbrRouterLeafStatus,
       "a3ComDvmrpNbrRouterPruneStatus": a3ComDvmrpNbrRouterPruneStatus,
       "a3ComDvmrpNbrRouterGenIdStatus": a3ComDvmrpNbrRouterGenIdStatus,
       "a3ComDvmrpNbrRouterMtraceStatus": a3ComDvmrpNbrRouterMtraceStatus}
)
