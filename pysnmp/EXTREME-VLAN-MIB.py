# SNMP MIB module (EXTREME-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(PortList,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "PortList",
    "extremeAgent")

(extremeSlotNumber,) = mibBuilder.importSymbols(
    "EXTREME-SYSTEM-MIB",
    "extremeSlotNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2)
)


# Types definitions



class ExtremeVlanType(Integer32):
    """Custom type ExtremeVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlanLayer2", 1)
    )





class ExtremeVlanEncapsType(Integer32):
    """Custom type ExtremeVlanEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlanEncaps8021q", 1)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeVlanGroup_ObjectIdentity = ObjectIdentity
extremeVlanGroup = _ExtremeVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1)
)
_ExtremeVlanGlobalMappingTable_Object = MibTable
extremeVlanGlobalMappingTable = _ExtremeVlanGlobalMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    extremeVlanGlobalMappingTable.setStatus("deprecated")
_ExtremeVlanGlobalMappingEntry_Object = MibTableRow
extremeVlanGlobalMappingEntry = _ExtremeVlanGlobalMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 1, 1)
)
extremeVlanGlobalMappingEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanGlobalMappingIdentifier"),
)
if mibBuilder.loadTexts:
    extremeVlanGlobalMappingEntry.setStatus("current")


class _ExtremeVlanGlobalMappingIdentifier_Type(Integer32):
    """Custom type extremeVlanGlobalMappingIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeVlanGlobalMappingIdentifier_Type.__name__ = "Integer32"
_ExtremeVlanGlobalMappingIdentifier_Object = MibTableColumn
extremeVlanGlobalMappingIdentifier = _ExtremeVlanGlobalMappingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 1, 1, 1),
    _ExtremeVlanGlobalMappingIdentifier_Type()
)
extremeVlanGlobalMappingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanGlobalMappingIdentifier.setStatus("current")
_ExtremeVlanGlobalMappingIfIndex_Type = Integer32
_ExtremeVlanGlobalMappingIfIndex_Object = MibTableColumn
extremeVlanGlobalMappingIfIndex = _ExtremeVlanGlobalMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 1, 1, 2),
    _ExtremeVlanGlobalMappingIfIndex_Type()
)
extremeVlanGlobalMappingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanGlobalMappingIfIndex.setStatus("current")
_ExtremeVlanIfTable_Object = MibTable
extremeVlanIfTable = _ExtremeVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    extremeVlanIfTable.setStatus("current")
_ExtremeVlanIfEntry_Object = MibTableRow
extremeVlanIfEntry = _ExtremeVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1)
)
extremeVlanIfEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanIfEntry.setStatus("current")
_ExtremeVlanIfIndex_Type = Integer32
_ExtremeVlanIfIndex_Object = MibTableColumn
extremeVlanIfIndex = _ExtremeVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 1),
    _ExtremeVlanIfIndex_Type()
)
extremeVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIfIndex.setStatus("current")


class _ExtremeVlanIfDescr_Type(DisplayString):
    """Custom type extremeVlanIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVlanIfDescr_Type.__name__ = "DisplayString"
_ExtremeVlanIfDescr_Object = MibTableColumn
extremeVlanIfDescr = _ExtremeVlanIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 2),
    _ExtremeVlanIfDescr_Type()
)
extremeVlanIfDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIfDescr.setStatus("current")
_ExtremeVlanIfType_Type = ExtremeVlanType
_ExtremeVlanIfType_Object = MibTableColumn
extremeVlanIfType = _ExtremeVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 3),
    _ExtremeVlanIfType_Type()
)
extremeVlanIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIfType.setStatus("current")


class _ExtremeVlanIfGlobalIdentifier_Type(Integer32):
    """Custom type extremeVlanIfGlobalIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeVlanIfGlobalIdentifier_Type.__name__ = "Integer32"
_ExtremeVlanIfGlobalIdentifier_Object = MibTableColumn
extremeVlanIfGlobalIdentifier = _ExtremeVlanIfGlobalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 4),
    _ExtremeVlanIfGlobalIdentifier_Type()
)
extremeVlanIfGlobalIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIfGlobalIdentifier.setStatus("deprecated")
_ExtremeVlanIfStatus_Type = RowStatus
_ExtremeVlanIfStatus_Object = MibTableColumn
extremeVlanIfStatus = _ExtremeVlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 6),
    _ExtremeVlanIfStatus_Type()
)
extremeVlanIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIfStatus.setStatus("current")
_ExtremeVlanIfIgnoreStpFlag_Type = TruthValue
_ExtremeVlanIfIgnoreStpFlag_Object = MibTableColumn
extremeVlanIfIgnoreStpFlag = _ExtremeVlanIfIgnoreStpFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 7),
    _ExtremeVlanIfIgnoreStpFlag_Type()
)
extremeVlanIfIgnoreStpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVlanIfIgnoreStpFlag.setStatus("current")
_ExtremeVlanIfIgnoreBpduFlag_Type = TruthValue
_ExtremeVlanIfIgnoreBpduFlag_Object = MibTableColumn
extremeVlanIfIgnoreBpduFlag = _ExtremeVlanIfIgnoreBpduFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 8),
    _ExtremeVlanIfIgnoreBpduFlag_Type()
)
extremeVlanIfIgnoreBpduFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVlanIfIgnoreBpduFlag.setStatus("current")
_ExtremeVlanIfLoopbackModeFlag_Type = TruthValue
_ExtremeVlanIfLoopbackModeFlag_Object = MibTableColumn
extremeVlanIfLoopbackModeFlag = _ExtremeVlanIfLoopbackModeFlag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 9),
    _ExtremeVlanIfLoopbackModeFlag_Type()
)
extremeVlanIfLoopbackModeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeVlanIfLoopbackModeFlag.setStatus("current")
_ExtremeVlanIfVlanId_Type = Integer32
_ExtremeVlanIfVlanId_Object = MibTableColumn
extremeVlanIfVlanId = _ExtremeVlanIfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 1, 2, 1, 10),
    _ExtremeVlanIfVlanId_Type()
)
extremeVlanIfVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanIfVlanId.setStatus("current")
_ExtremeVirtualGroup_ObjectIdentity = ObjectIdentity
extremeVirtualGroup = _ExtremeVirtualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 2)
)
_ExtremeNextAvailableVirtIfIndex_Type = Integer32
_ExtremeNextAvailableVirtIfIndex_Object = MibScalar
extremeNextAvailableVirtIfIndex = _ExtremeNextAvailableVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 2, 1),
    _ExtremeNextAvailableVirtIfIndex_Type()
)
extremeNextAvailableVirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeNextAvailableVirtIfIndex.setStatus("current")
_ExtremeEncapsulationGroup_ObjectIdentity = ObjectIdentity
extremeEncapsulationGroup = _ExtremeEncapsulationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3)
)
_ExtremeVlanEncapsIfTable_Object = MibTable
extremeVlanEncapsIfTable = _ExtremeVlanEncapsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    extremeVlanEncapsIfTable.setStatus("current")
_ExtremeVlanEncapsIfEntry_Object = MibTableRow
extremeVlanEncapsIfEntry = _ExtremeVlanEncapsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1, 1)
)
extremeVlanEncapsIfEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanEncapsIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanEncapsIfEntry.setStatus("current")
_ExtremeVlanEncapsIfIndex_Type = Integer32
_ExtremeVlanEncapsIfIndex_Object = MibTableColumn
extremeVlanEncapsIfIndex = _ExtremeVlanEncapsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1, 1, 1),
    _ExtremeVlanEncapsIfIndex_Type()
)
extremeVlanEncapsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanEncapsIfIndex.setStatus("current")
_ExtremeVlanEncapsIfType_Type = ExtremeVlanEncapsType
_ExtremeVlanEncapsIfType_Object = MibTableColumn
extremeVlanEncapsIfType = _ExtremeVlanEncapsIfType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1, 1, 2),
    _ExtremeVlanEncapsIfType_Type()
)
extremeVlanEncapsIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanEncapsIfType.setStatus("current")
_ExtremeVlanEncapsIfTag_Type = Integer32
_ExtremeVlanEncapsIfTag_Object = MibTableColumn
extremeVlanEncapsIfTag = _ExtremeVlanEncapsIfTag_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1, 1, 3),
    _ExtremeVlanEncapsIfTag_Type()
)
extremeVlanEncapsIfTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanEncapsIfTag.setStatus("current")
_ExtremeVlanEncapsIfStatus_Type = RowStatus
_ExtremeVlanEncapsIfStatus_Object = MibTableColumn
extremeVlanEncapsIfStatus = _ExtremeVlanEncapsIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 3, 1, 1, 4),
    _ExtremeVlanEncapsIfStatus_Type()
)
extremeVlanEncapsIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanEncapsIfStatus.setStatus("current")
_ExtremeVlanIpGroup_ObjectIdentity = ObjectIdentity
extremeVlanIpGroup = _ExtremeVlanIpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4)
)
_ExtremeVlanIpTable_Object = MibTable
extremeVlanIpTable = _ExtremeVlanIpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    extremeVlanIpTable.setStatus("current")
_ExtremeVlanIpEntry_Object = MibTableRow
extremeVlanIpEntry = _ExtremeVlanIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1, 1)
)
extremeVlanIpEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanIpEntry.setStatus("current")
_ExtremeVlanIpNetAddress_Type = IpAddress
_ExtremeVlanIpNetAddress_Object = MibTableColumn
extremeVlanIpNetAddress = _ExtremeVlanIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1, 1, 1),
    _ExtremeVlanIpNetAddress_Type()
)
extremeVlanIpNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIpNetAddress.setStatus("current")
_ExtremeVlanIpNetMask_Type = IpAddress
_ExtremeVlanIpNetMask_Object = MibTableColumn
extremeVlanIpNetMask = _ExtremeVlanIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1, 1, 2),
    _ExtremeVlanIpNetMask_Type()
)
extremeVlanIpNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIpNetMask.setStatus("current")
_ExtremeVlanIpStatus_Type = RowStatus
_ExtremeVlanIpStatus_Object = MibTableColumn
extremeVlanIpStatus = _ExtremeVlanIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1, 1, 3),
    _ExtremeVlanIpStatus_Type()
)
extremeVlanIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIpStatus.setStatus("current")
_ExtremeVlanIpForwardingState_Type = TruthValue
_ExtremeVlanIpForwardingState_Object = MibTableColumn
extremeVlanIpForwardingState = _ExtremeVlanIpForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 4, 1, 1, 4),
    _ExtremeVlanIpForwardingState_Type()
)
extremeVlanIpForwardingState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanIpForwardingState.setStatus("current")
_ExtremeProtocolGroup_ObjectIdentity = ObjectIdentity
extremeProtocolGroup = _ExtremeProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5)
)
_ExtremeVlanProtocolTable_Object = MibTable
extremeVlanProtocolTable = _ExtremeVlanProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    extremeVlanProtocolTable.setStatus("current")
_ExtremeVlanProtocolEntry_Object = MibTableRow
extremeVlanProtocolEntry = _ExtremeVlanProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1)
)
extremeVlanProtocolEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanProtocolIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanProtocolIdIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanProtocolEntry.setStatus("current")


class _ExtremeVlanProtocolIndex_Type(Integer32):
    """Custom type extremeVlanProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ExtremeVlanProtocolIndex_Type.__name__ = "Integer32"
_ExtremeVlanProtocolIndex_Object = MibTableColumn
extremeVlanProtocolIndex = _ExtremeVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 1),
    _ExtremeVlanProtocolIndex_Type()
)
extremeVlanProtocolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolIndex.setStatus("current")


class _ExtremeVlanProtocolIdIndex_Type(Integer32):
    """Custom type extremeVlanProtocolIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_ExtremeVlanProtocolIdIndex_Type.__name__ = "Integer32"
_ExtremeVlanProtocolIdIndex_Object = MibTableColumn
extremeVlanProtocolIdIndex = _ExtremeVlanProtocolIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 2),
    _ExtremeVlanProtocolIdIndex_Type()
)
extremeVlanProtocolIdIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolIdIndex.setStatus("current")


class _ExtremeVlanProtocolName_Type(DisplayString):
    """Custom type extremeVlanProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ExtremeVlanProtocolName_Type.__name__ = "DisplayString"
_ExtremeVlanProtocolName_Object = MibTableColumn
extremeVlanProtocolName = _ExtremeVlanProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 3),
    _ExtremeVlanProtocolName_Type()
)
extremeVlanProtocolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolName.setStatus("current")


class _ExtremeVlanProtocolDllEncapsType_Type(Integer32):
    """Custom type extremeVlanProtocolDllEncapsType based on Integer32"""
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
        *(("any", 1),
          ("ethertype", 2),
          ("llc", 3),
          ("llcSnapEthertype", 4),
          ("none", 5))
    )


_ExtremeVlanProtocolDllEncapsType_Type.__name__ = "Integer32"
_ExtremeVlanProtocolDllEncapsType_Object = MibTableColumn
extremeVlanProtocolDllEncapsType = _ExtremeVlanProtocolDllEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 4),
    _ExtremeVlanProtocolDllEncapsType_Type()
)
extremeVlanProtocolDllEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolDllEncapsType.setStatus("current")


class _ExtremeVlanProtocolId_Type(Integer32):
    """Custom type extremeVlanProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ExtremeVlanProtocolId_Type.__name__ = "Integer32"
_ExtremeVlanProtocolId_Object = MibTableColumn
extremeVlanProtocolId = _ExtremeVlanProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 5),
    _ExtremeVlanProtocolId_Type()
)
extremeVlanProtocolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolId.setStatus("current")
_ExtremeVlanProtocolStatus_Type = RowStatus
_ExtremeVlanProtocolStatus_Object = MibTableColumn
extremeVlanProtocolStatus = _ExtremeVlanProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 1, 1, 6),
    _ExtremeVlanProtocolStatus_Type()
)
extremeVlanProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolStatus.setStatus("current")
_ExtremeVlanProtocolVlanTable_Object = MibTable
extremeVlanProtocolVlanTable = _ExtremeVlanProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    extremeVlanProtocolVlanTable.setStatus("current")
_ExtremeVlanProtocolVlanEntry_Object = MibTableRow
extremeVlanProtocolVlanEntry = _ExtremeVlanProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 2, 1)
)
extremeVlanProtocolVlanEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanProtocolVlanIfIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanProtocolVlanEntry.setStatus("current")
_ExtremeVlanProtocolVlanIfIndex_Type = Integer32
_ExtremeVlanProtocolVlanIfIndex_Object = MibTableColumn
extremeVlanProtocolVlanIfIndex = _ExtremeVlanProtocolVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 2, 1, 1),
    _ExtremeVlanProtocolVlanIfIndex_Type()
)
extremeVlanProtocolVlanIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolVlanIfIndex.setStatus("current")
_ExtremeVlanProtocolVlanProtocolIndex_Type = Integer32
_ExtremeVlanProtocolVlanProtocolIndex_Object = MibTableColumn
extremeVlanProtocolVlanProtocolIndex = _ExtremeVlanProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 2, 1, 2),
    _ExtremeVlanProtocolVlanProtocolIndex_Type()
)
extremeVlanProtocolVlanProtocolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolVlanProtocolIndex.setStatus("current")
_ExtremeVlanProtocolVlanStatus_Type = RowStatus
_ExtremeVlanProtocolVlanStatus_Object = MibTableColumn
extremeVlanProtocolVlanStatus = _ExtremeVlanProtocolVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 5, 2, 1, 3),
    _ExtremeVlanProtocolVlanStatus_Type()
)
extremeVlanProtocolVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanProtocolVlanStatus.setStatus("current")
_ExtremeVlanOpaqueGroup_ObjectIdentity = ObjectIdentity
extremeVlanOpaqueGroup = _ExtremeVlanOpaqueGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 6)
)
_ExtremeVlanOpaqueTable_Object = MibTable
extremeVlanOpaqueTable = _ExtremeVlanOpaqueTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    extremeVlanOpaqueTable.setStatus("current")
_ExtremeVlanOpaqueEntry_Object = MibTableRow
extremeVlanOpaqueEntry = _ExtremeVlanOpaqueEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 6, 1, 1)
)
extremeVlanOpaqueEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
    (0, "EXTREME-SYSTEM-MIB", "extremeSlotNumber"),
)
if mibBuilder.loadTexts:
    extremeVlanOpaqueEntry.setStatus("current")
_ExtremeVlanOpaqueTaggedPorts_Type = PortList
_ExtremeVlanOpaqueTaggedPorts_Object = MibTableColumn
extremeVlanOpaqueTaggedPorts = _ExtremeVlanOpaqueTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 6, 1, 1, 1),
    _ExtremeVlanOpaqueTaggedPorts_Type()
)
extremeVlanOpaqueTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanOpaqueTaggedPorts.setStatus("current")
_ExtremeVlanOpaqueUntaggedPorts_Type = PortList
_ExtremeVlanOpaqueUntaggedPorts_Object = MibTableColumn
extremeVlanOpaqueUntaggedPorts = _ExtremeVlanOpaqueUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 6, 1, 1, 2),
    _ExtremeVlanOpaqueUntaggedPorts_Type()
)
extremeVlanOpaqueUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanOpaqueUntaggedPorts.setStatus("current")
_ExtremeVlanStackGroup_ObjectIdentity = ObjectIdentity
extremeVlanStackGroup = _ExtremeVlanStackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 7)
)
_ExtremeVlanStackTable_Object = MibTable
extremeVlanStackTable = _ExtremeVlanStackTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 7, 1)
)
if mibBuilder.loadTexts:
    extremeVlanStackTable.setStatus("current")
_ExtremeVlanStackEntry_Object = MibTableRow
extremeVlanStackEntry = _ExtremeVlanStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 7, 1, 1)
)
extremeVlanStackEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanStackHigherLayer"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanStackLowerLayer"),
)
if mibBuilder.loadTexts:
    extremeVlanStackEntry.setStatus("current")
_ExtremeVlanStackHigherLayer_Type = Integer32
_ExtremeVlanStackHigherLayer_Object = MibTableColumn
extremeVlanStackHigherLayer = _ExtremeVlanStackHigherLayer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 7, 1, 1, 1),
    _ExtremeVlanStackHigherLayer_Type()
)
extremeVlanStackHigherLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanStackHigherLayer.setStatus("current")
_ExtremeVlanStackLowerLayer_Type = Integer32
_ExtremeVlanStackLowerLayer_Object = MibTableColumn
extremeVlanStackLowerLayer = _ExtremeVlanStackLowerLayer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 7, 1, 1, 2),
    _ExtremeVlanStackLowerLayer_Type()
)
extremeVlanStackLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanStackLowerLayer.setStatus("current")
_ExtremeVlanStatsGroup_ObjectIdentity = ObjectIdentity
extremeVlanStatsGroup = _ExtremeVlanStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8)
)
_ExtremeVlanL2StatsTable_Object = MibTable
extremeVlanL2StatsTable = _ExtremeVlanL2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    extremeVlanL2StatsTable.setStatus("current")
_ExtremeVlanL2StatsEntry_Object = MibTableRow
extremeVlanL2StatsEntry = _ExtremeVlanL2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1)
)
extremeVlanL2StatsEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanL2StatsEntry.setStatus("current")


class _ExtremeVlanL2StatsIfDescr_Type(DisplayString):
    """Custom type extremeVlanL2StatsIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ExtremeVlanL2StatsIfDescr_Type.__name__ = "DisplayString"
_ExtremeVlanL2StatsIfDescr_Object = MibTableColumn
extremeVlanL2StatsIfDescr = _ExtremeVlanL2StatsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1, 1),
    _ExtremeVlanL2StatsIfDescr_Type()
)
extremeVlanL2StatsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanL2StatsIfDescr.setStatus("current")
_ExtremeVlanL2StatsPktsToCpu_Type = Counter64
_ExtremeVlanL2StatsPktsToCpu_Object = MibTableColumn
extremeVlanL2StatsPktsToCpu = _ExtremeVlanL2StatsPktsToCpu_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1, 2),
    _ExtremeVlanL2StatsPktsToCpu_Type()
)
extremeVlanL2StatsPktsToCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanL2StatsPktsToCpu.setStatus("current")
_ExtremeVlanL2StatsPktsLearnt_Type = Counter64
_ExtremeVlanL2StatsPktsLearnt_Object = MibTableColumn
extremeVlanL2StatsPktsLearnt = _ExtremeVlanL2StatsPktsLearnt_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1, 3),
    _ExtremeVlanL2StatsPktsLearnt_Type()
)
extremeVlanL2StatsPktsLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanL2StatsPktsLearnt.setStatus("current")
_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Type = Counter64
_ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Object = MibTableColumn
extremeVlanL2StatsIgmpCtrlPktsSnooped = _ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1, 4),
    _ExtremeVlanL2StatsIgmpCtrlPktsSnooped_Type()
)
extremeVlanL2StatsIgmpCtrlPktsSnooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanL2StatsIgmpCtrlPktsSnooped.setStatus("current")
_ExtremeVlanL2StatsIgmpDataPktsSwitched_Type = Counter64
_ExtremeVlanL2StatsIgmpDataPktsSwitched_Object = MibTableColumn
extremeVlanL2StatsIgmpDataPktsSwitched = _ExtremeVlanL2StatsIgmpDataPktsSwitched_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 8, 1, 1, 5),
    _ExtremeVlanL2StatsIgmpDataPktsSwitched_Type()
)
extremeVlanL2StatsIgmpDataPktsSwitched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanL2StatsIgmpDataPktsSwitched.setStatus("current")
_ExtremeVlanAggregationGroup_ObjectIdentity = ObjectIdentity
extremeVlanAggregationGroup = _ExtremeVlanAggregationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9)
)
_ExtremeVlanAggregationTable_Object = MibTable
extremeVlanAggregationTable = _ExtremeVlanAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    extremeVlanAggregationTable.setStatus("current")
_ExtremeVlanAggregationEntry_Object = MibTableRow
extremeVlanAggregationEntry = _ExtremeVlanAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1)
)
extremeVlanAggregationEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanAggregationSuperVlanIfIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanAggregationSubVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanAggregationEntry.setStatus("current")
_ExtremeVlanAggregationSuperVlanIfIndex_Type = Integer32
_ExtremeVlanAggregationSuperVlanIfIndex_Object = MibTableColumn
extremeVlanAggregationSuperVlanIfIndex = _ExtremeVlanAggregationSuperVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 1),
    _ExtremeVlanAggregationSuperVlanIfIndex_Type()
)
extremeVlanAggregationSuperVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanAggregationSuperVlanIfIndex.setStatus("current")
_ExtremeVlanAggregationSubVlanIfIndex_Type = Integer32
_ExtremeVlanAggregationSubVlanIfIndex_Object = MibTableColumn
extremeVlanAggregationSubVlanIfIndex = _ExtremeVlanAggregationSubVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 2),
    _ExtremeVlanAggregationSubVlanIfIndex_Type()
)
extremeVlanAggregationSubVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanAggregationSubVlanIfIndex.setStatus("current")
_ExtremeVlanAggregationSubVlanStartIpNetAddress_Type = IpAddress
_ExtremeVlanAggregationSubVlanStartIpNetAddress_Object = MibTableColumn
extremeVlanAggregationSubVlanStartIpNetAddress = _ExtremeVlanAggregationSubVlanStartIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 3),
    _ExtremeVlanAggregationSubVlanStartIpNetAddress_Type()
)
extremeVlanAggregationSubVlanStartIpNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanAggregationSubVlanStartIpNetAddress.setStatus("current")
_ExtremeVlanAggregationSubVlanStartIpNetMask_Type = IpAddress
_ExtremeVlanAggregationSubVlanStartIpNetMask_Object = MibTableColumn
extremeVlanAggregationSubVlanStartIpNetMask = _ExtremeVlanAggregationSubVlanStartIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 4),
    _ExtremeVlanAggregationSubVlanStartIpNetMask_Type()
)
extremeVlanAggregationSubVlanStartIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanAggregationSubVlanStartIpNetMask.setStatus("current")
_ExtremeVlanAggregationSubVlanEndIpNetAddress_Type = IpAddress
_ExtremeVlanAggregationSubVlanEndIpNetAddress_Object = MibTableColumn
extremeVlanAggregationSubVlanEndIpNetAddress = _ExtremeVlanAggregationSubVlanEndIpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 5),
    _ExtremeVlanAggregationSubVlanEndIpNetAddress_Type()
)
extremeVlanAggregationSubVlanEndIpNetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanAggregationSubVlanEndIpNetAddress.setStatus("current")
_ExtremeVlanAggregationSubVlanEndIpNetMask_Type = IpAddress
_ExtremeVlanAggregationSubVlanEndIpNetMask_Object = MibTableColumn
extremeVlanAggregationSubVlanEndIpNetMask = _ExtremeVlanAggregationSubVlanEndIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 6),
    _ExtremeVlanAggregationSubVlanEndIpNetMask_Type()
)
extremeVlanAggregationSubVlanEndIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanAggregationSubVlanEndIpNetMask.setStatus("current")
_ExtremeVlanAggregationStatus_Type = RowStatus
_ExtremeVlanAggregationStatus_Object = MibTableColumn
extremeVlanAggregationStatus = _ExtremeVlanAggregationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 1, 1, 7),
    _ExtremeVlanAggregationStatus_Type()
)
extremeVlanAggregationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanAggregationStatus.setStatus("current")
_ExtremeVlanAggregationConfigTable_Object = MibTable
extremeVlanAggregationConfigTable = _ExtremeVlanAggregationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 2)
)
if mibBuilder.loadTexts:
    extremeVlanAggregationConfigTable.setStatus("current")
_ExtremeVlanAggregationConfigEntry_Object = MibTableRow
extremeVlanAggregationConfigEntry = _ExtremeVlanAggregationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 2, 1)
)
extremeVlanAggregationConfigEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanAggregationConfigSuperVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanAggregationConfigEntry.setStatus("current")
_ExtremeVlanAggregationConfigSuperVlanIfIndex_Type = Integer32
_ExtremeVlanAggregationConfigSuperVlanIfIndex_Object = MibTableColumn
extremeVlanAggregationConfigSuperVlanIfIndex = _ExtremeVlanAggregationConfigSuperVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 2, 1, 1),
    _ExtremeVlanAggregationConfigSuperVlanIfIndex_Type()
)
extremeVlanAggregationConfigSuperVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanAggregationConfigSuperVlanIfIndex.setStatus("current")
_ExtremeVlanAggregationConfigSubVlanProxyEnable_Type = TruthValue
_ExtremeVlanAggregationConfigSubVlanProxyEnable_Object = MibTableColumn
extremeVlanAggregationConfigSubVlanProxyEnable = _ExtremeVlanAggregationConfigSubVlanProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 9, 2, 1, 2),
    _ExtremeVlanAggregationConfigSubVlanProxyEnable_Type()
)
extremeVlanAggregationConfigSubVlanProxyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanAggregationConfigSubVlanProxyEnable.setStatus("current")
_ExtremeVlanTranslationGroup_ObjectIdentity = ObjectIdentity
extremeVlanTranslationGroup = _ExtremeVlanTranslationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10)
)
_ExtremeVlanTranslationTable_Object = MibTable
extremeVlanTranslationTable = _ExtremeVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    extremeVlanTranslationTable.setStatus("current")
_ExtremeVlanTranslationEntry_Object = MibTableRow
extremeVlanTranslationEntry = _ExtremeVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10, 1, 1)
)
extremeVlanTranslationEntry.setIndexNames(
    (0, "EXTREME-VLAN-MIB", "extremeVlanTranslationSuperVlanIfIndex"),
    (0, "EXTREME-VLAN-MIB", "extremeVlanTranslationMemberVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeVlanTranslationEntry.setStatus("current")
_ExtremeVlanTranslationSuperVlanIfIndex_Type = Integer32
_ExtremeVlanTranslationSuperVlanIfIndex_Object = MibTableColumn
extremeVlanTranslationSuperVlanIfIndex = _ExtremeVlanTranslationSuperVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10, 1, 1, 1),
    _ExtremeVlanTranslationSuperVlanIfIndex_Type()
)
extremeVlanTranslationSuperVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanTranslationSuperVlanIfIndex.setStatus("current")
_ExtremeVlanTranslationMemberVlanIfIndex_Type = Integer32
_ExtremeVlanTranslationMemberVlanIfIndex_Object = MibTableColumn
extremeVlanTranslationMemberVlanIfIndex = _ExtremeVlanTranslationMemberVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10, 1, 1, 2),
    _ExtremeVlanTranslationMemberVlanIfIndex_Type()
)
extremeVlanTranslationMemberVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeVlanTranslationMemberVlanIfIndex.setStatus("current")
_ExtremeVlanTranslationStatus_Type = RowStatus
_ExtremeVlanTranslationStatus_Object = MibTableColumn
extremeVlanTranslationStatus = _ExtremeVlanTranslationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 2, 10, 1, 1, 3),
    _ExtremeVlanTranslationStatus_Type()
)
extremeVlanTranslationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeVlanTranslationStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-VLAN-MIB",
    **{"ExtremeVlanType": ExtremeVlanType,
       "ExtremeVlanEncapsType": ExtremeVlanEncapsType,
       "extremeVlan": extremeVlan,
       "extremeVlanGroup": extremeVlanGroup,
       "extremeVlanGlobalMappingTable": extremeVlanGlobalMappingTable,
       "extremeVlanGlobalMappingEntry": extremeVlanGlobalMappingEntry,
       "extremeVlanGlobalMappingIdentifier": extremeVlanGlobalMappingIdentifier,
       "extremeVlanGlobalMappingIfIndex": extremeVlanGlobalMappingIfIndex,
       "extremeVlanIfTable": extremeVlanIfTable,
       "extremeVlanIfEntry": extremeVlanIfEntry,
       "extremeVlanIfIndex": extremeVlanIfIndex,
       "extremeVlanIfDescr": extremeVlanIfDescr,
       "extremeVlanIfType": extremeVlanIfType,
       "extremeVlanIfGlobalIdentifier": extremeVlanIfGlobalIdentifier,
       "extremeVlanIfStatus": extremeVlanIfStatus,
       "extremeVlanIfIgnoreStpFlag": extremeVlanIfIgnoreStpFlag,
       "extremeVlanIfIgnoreBpduFlag": extremeVlanIfIgnoreBpduFlag,
       "extremeVlanIfLoopbackModeFlag": extremeVlanIfLoopbackModeFlag,
       "extremeVlanIfVlanId": extremeVlanIfVlanId,
       "extremeVirtualGroup": extremeVirtualGroup,
       "extremeNextAvailableVirtIfIndex": extremeNextAvailableVirtIfIndex,
       "extremeEncapsulationGroup": extremeEncapsulationGroup,
       "extremeVlanEncapsIfTable": extremeVlanEncapsIfTable,
       "extremeVlanEncapsIfEntry": extremeVlanEncapsIfEntry,
       "extremeVlanEncapsIfIndex": extremeVlanEncapsIfIndex,
       "extremeVlanEncapsIfType": extremeVlanEncapsIfType,
       "extremeVlanEncapsIfTag": extremeVlanEncapsIfTag,
       "extremeVlanEncapsIfStatus": extremeVlanEncapsIfStatus,
       "extremeVlanIpGroup": extremeVlanIpGroup,
       "extremeVlanIpTable": extremeVlanIpTable,
       "extremeVlanIpEntry": extremeVlanIpEntry,
       "extremeVlanIpNetAddress": extremeVlanIpNetAddress,
       "extremeVlanIpNetMask": extremeVlanIpNetMask,
       "extremeVlanIpStatus": extremeVlanIpStatus,
       "extremeVlanIpForwardingState": extremeVlanIpForwardingState,
       "extremeProtocolGroup": extremeProtocolGroup,
       "extremeVlanProtocolTable": extremeVlanProtocolTable,
       "extremeVlanProtocolEntry": extremeVlanProtocolEntry,
       "extremeVlanProtocolIndex": extremeVlanProtocolIndex,
       "extremeVlanProtocolIdIndex": extremeVlanProtocolIdIndex,
       "extremeVlanProtocolName": extremeVlanProtocolName,
       "extremeVlanProtocolDllEncapsType": extremeVlanProtocolDllEncapsType,
       "extremeVlanProtocolId": extremeVlanProtocolId,
       "extremeVlanProtocolStatus": extremeVlanProtocolStatus,
       "extremeVlanProtocolVlanTable": extremeVlanProtocolVlanTable,
       "extremeVlanProtocolVlanEntry": extremeVlanProtocolVlanEntry,
       "extremeVlanProtocolVlanIfIndex": extremeVlanProtocolVlanIfIndex,
       "extremeVlanProtocolVlanProtocolIndex": extremeVlanProtocolVlanProtocolIndex,
       "extremeVlanProtocolVlanStatus": extremeVlanProtocolVlanStatus,
       "extremeVlanOpaqueGroup": extremeVlanOpaqueGroup,
       "extremeVlanOpaqueTable": extremeVlanOpaqueTable,
       "extremeVlanOpaqueEntry": extremeVlanOpaqueEntry,
       "extremeVlanOpaqueTaggedPorts": extremeVlanOpaqueTaggedPorts,
       "extremeVlanOpaqueUntaggedPorts": extremeVlanOpaqueUntaggedPorts,
       "extremeVlanStackGroup": extremeVlanStackGroup,
       "extremeVlanStackTable": extremeVlanStackTable,
       "extremeVlanStackEntry": extremeVlanStackEntry,
       "extremeVlanStackHigherLayer": extremeVlanStackHigherLayer,
       "extremeVlanStackLowerLayer": extremeVlanStackLowerLayer,
       "extremeVlanStatsGroup": extremeVlanStatsGroup,
       "extremeVlanL2StatsTable": extremeVlanL2StatsTable,
       "extremeVlanL2StatsEntry": extremeVlanL2StatsEntry,
       "extremeVlanL2StatsIfDescr": extremeVlanL2StatsIfDescr,
       "extremeVlanL2StatsPktsToCpu": extremeVlanL2StatsPktsToCpu,
       "extremeVlanL2StatsPktsLearnt": extremeVlanL2StatsPktsLearnt,
       "extremeVlanL2StatsIgmpCtrlPktsSnooped": extremeVlanL2StatsIgmpCtrlPktsSnooped,
       "extremeVlanL2StatsIgmpDataPktsSwitched": extremeVlanL2StatsIgmpDataPktsSwitched,
       "extremeVlanAggregationGroup": extremeVlanAggregationGroup,
       "extremeVlanAggregationTable": extremeVlanAggregationTable,
       "extremeVlanAggregationEntry": extremeVlanAggregationEntry,
       "extremeVlanAggregationSuperVlanIfIndex": extremeVlanAggregationSuperVlanIfIndex,
       "extremeVlanAggregationSubVlanIfIndex": extremeVlanAggregationSubVlanIfIndex,
       "extremeVlanAggregationSubVlanStartIpNetAddress": extremeVlanAggregationSubVlanStartIpNetAddress,
       "extremeVlanAggregationSubVlanStartIpNetMask": extremeVlanAggregationSubVlanStartIpNetMask,
       "extremeVlanAggregationSubVlanEndIpNetAddress": extremeVlanAggregationSubVlanEndIpNetAddress,
       "extremeVlanAggregationSubVlanEndIpNetMask": extremeVlanAggregationSubVlanEndIpNetMask,
       "extremeVlanAggregationStatus": extremeVlanAggregationStatus,
       "extremeVlanAggregationConfigTable": extremeVlanAggregationConfigTable,
       "extremeVlanAggregationConfigEntry": extremeVlanAggregationConfigEntry,
       "extremeVlanAggregationConfigSuperVlanIfIndex": extremeVlanAggregationConfigSuperVlanIfIndex,
       "extremeVlanAggregationConfigSubVlanProxyEnable": extremeVlanAggregationConfigSubVlanProxyEnable,
       "extremeVlanTranslationGroup": extremeVlanTranslationGroup,
       "extremeVlanTranslationTable": extremeVlanTranslationTable,
       "extremeVlanTranslationEntry": extremeVlanTranslationEntry,
       "extremeVlanTranslationSuperVlanIfIndex": extremeVlanTranslationSuperVlanIfIndex,
       "extremeVlanTranslationMemberVlanIfIndex": extremeVlanTranslationMemberVlanIfIndex,
       "extremeVlanTranslationStatus": extremeVlanTranslationStatus}
)
