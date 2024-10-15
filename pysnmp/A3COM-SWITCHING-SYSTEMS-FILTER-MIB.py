# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-SWITCHING-SYSTEMS-FILTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:49 2024
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





class A3ComFilterPortType(Integer32):
    """Custom type A3ComFilterPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_SwitchingSystemsMibs_ObjectIdentity = ObjectIdentity
switchingSystemsMibs = _SwitchingSystemsMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29)
)
_A3ComSwitchingSystemsMib_ObjectIdentity = ObjectIdentity
a3ComSwitchingSystemsMib = _A3ComSwitchingSystemsMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4)
)
_A3ComFilterGroup_ObjectIdentity = ObjectIdentity
a3ComFilterGroup = _A3ComFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20)
)
_A3ComFilterAddressGroup_ObjectIdentity = ObjectIdentity
a3ComFilterAddressGroup = _A3ComFilterAddressGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1)
)
_A3ComFilterAddressGroupNextAvailableIndex_Type = Integer32
_A3ComFilterAddressGroupNextAvailableIndex_Object = MibScalar
a3ComFilterAddressGroupNextAvailableIndex = _A3ComFilterAddressGroupNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 1),
    _A3ComFilterAddressGroupNextAvailableIndex_Type()
)
a3ComFilterAddressGroupNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupNextAvailableIndex.setStatus("mandatory")
_A3ComFilterAddressGroupCount_Type = Integer32
_A3ComFilterAddressGroupCount_Object = MibScalar
a3ComFilterAddressGroupCount = _A3ComFilterAddressGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 2),
    _A3ComFilterAddressGroupCount_Type()
)
a3ComFilterAddressGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupCount.setStatus("mandatory")
_A3ComFilterAddressGroupTable_Object = MibTable
a3ComFilterAddressGroupTable = _A3ComFilterAddressGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3)
)
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupTable.setStatus("mandatory")
_A3ComFilterAddressGroupEntry_Object = MibTableRow
a3ComFilterAddressGroupEntry = _A3ComFilterAddressGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1)
)
a3ComFilterAddressGroupEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressGroupId"),
)
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupEntry.setStatus("mandatory")


class _A3ComFilterAddressGroupId_Type(Integer32):
    """Custom type a3ComFilterAddressGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFilterAddressGroupId_Type.__name__ = "Integer32"
_A3ComFilterAddressGroupId_Object = MibTableColumn
a3ComFilterAddressGroupId = _A3ComFilterAddressGroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 1),
    _A3ComFilterAddressGroupId_Type()
)
a3ComFilterAddressGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupId.setStatus("mandatory")
_A3ComFilterAddressGroupMaskId_Type = Integer32
_A3ComFilterAddressGroupMaskId_Object = MibTableColumn
a3ComFilterAddressGroupMaskId = _A3ComFilterAddressGroupMaskId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 2),
    _A3ComFilterAddressGroupMaskId_Type()
)
a3ComFilterAddressGroupMaskId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupMaskId.setStatus("mandatory")


class _A3ComFilterAddressGroupBridgeMask_Type(OctetString):
    """Custom type a3ComFilterAddressGroupBridgeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_A3ComFilterAddressGroupBridgeMask_Type.__name__ = "OctetString"
_A3ComFilterAddressGroupBridgeMask_Object = MibTableColumn
a3ComFilterAddressGroupBridgeMask = _A3ComFilterAddressGroupBridgeMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 3),
    _A3ComFilterAddressGroupBridgeMask_Type()
)
a3ComFilterAddressGroupBridgeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupBridgeMask.setStatus("mandatory")


class _A3ComFilterAddressGroupName_Type(DisplayString):
    """Custom type a3ComFilterAddressGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComFilterAddressGroupName_Type.__name__ = "DisplayString"
_A3ComFilterAddressGroupName_Object = MibTableColumn
a3ComFilterAddressGroupName = _A3ComFilterAddressGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 4),
    _A3ComFilterAddressGroupName_Type()
)
a3ComFilterAddressGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupName.setStatus("mandatory")
_A3ComFilterAddressGroupStatus_Type = RowStatus
_A3ComFilterAddressGroupStatus_Object = MibTableColumn
a3ComFilterAddressGroupStatus = _A3ComFilterAddressGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 3, 1, 5),
    _A3ComFilterAddressGroupStatus_Type()
)
a3ComFilterAddressGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterAddressGroupStatus.setStatus("mandatory")
_A3ComFilterAddressTable_Object = MibTable
a3ComFilterAddressTable = _A3ComFilterAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4)
)
if mibBuilder.loadTexts:
    a3ComFilterAddressTable.setStatus("mandatory")
_A3ComFilterAddressEntry_Object = MibTableRow
a3ComFilterAddressEntry = _A3ComFilterAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1)
)
a3ComFilterAddressEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressId"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterAddressAddress"),
)
if mibBuilder.loadTexts:
    a3ComFilterAddressEntry.setStatus("mandatory")


class _A3ComFilterAddressId_Type(Integer32):
    """Custom type a3ComFilterAddressId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFilterAddressId_Type.__name__ = "Integer32"
_A3ComFilterAddressId_Object = MibTableColumn
a3ComFilterAddressId = _A3ComFilterAddressId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 1),
    _A3ComFilterAddressId_Type()
)
a3ComFilterAddressId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterAddressId.setStatus("mandatory")
_A3ComFilterAddressAddress_Type = PhysAddress
_A3ComFilterAddressAddress_Object = MibTableColumn
a3ComFilterAddressAddress = _A3ComFilterAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 2),
    _A3ComFilterAddressAddress_Type()
)
a3ComFilterAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterAddressAddress.setStatus("mandatory")
_A3ComFilterAddressStatus_Type = RowStatus
_A3ComFilterAddressStatus_Object = MibTableColumn
a3ComFilterAddressStatus = _A3ComFilterAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 1, 4, 1, 3),
    _A3ComFilterAddressStatus_Type()
)
a3ComFilterAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterAddressStatus.setStatus("mandatory")
_A3ComFilterPortGroup_ObjectIdentity = ObjectIdentity
a3ComFilterPortGroup = _A3ComFilterPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2)
)
_A3ComFilterPortGroupNextAvailableIndex_Type = Integer32
_A3ComFilterPortGroupNextAvailableIndex_Object = MibScalar
a3ComFilterPortGroupNextAvailableIndex = _A3ComFilterPortGroupNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 1),
    _A3ComFilterPortGroupNextAvailableIndex_Type()
)
a3ComFilterPortGroupNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupNextAvailableIndex.setStatus("mandatory")
_A3ComFilterPortGroupCount_Type = Integer32
_A3ComFilterPortGroupCount_Object = MibScalar
a3ComFilterPortGroupCount = _A3ComFilterPortGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 2),
    _A3ComFilterPortGroupCount_Type()
)
a3ComFilterPortGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupCount.setStatus("mandatory")
_A3ComFilterPortGroupTable_Object = MibTable
a3ComFilterPortGroupTable = _A3ComFilterPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3)
)
if mibBuilder.loadTexts:
    a3ComFilterPortGroupTable.setStatus("mandatory")
_A3ComFilterPortGroupEntry_Object = MibTableRow
a3ComFilterPortGroupEntry = _A3ComFilterPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1)
)
a3ComFilterPortGroupEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortGroupId"),
)
if mibBuilder.loadTexts:
    a3ComFilterPortGroupEntry.setStatus("mandatory")


class _A3ComFilterPortGroupId_Type(Integer32):
    """Custom type a3ComFilterPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFilterPortGroupId_Type.__name__ = "Integer32"
_A3ComFilterPortGroupId_Object = MibTableColumn
a3ComFilterPortGroupId = _A3ComFilterPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 1),
    _A3ComFilterPortGroupId_Type()
)
a3ComFilterPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupId.setStatus("mandatory")
_A3ComFilterPortGroupMaskId_Type = Integer32
_A3ComFilterPortGroupMaskId_Object = MibTableColumn
a3ComFilterPortGroupMaskId = _A3ComFilterPortGroupMaskId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 2),
    _A3ComFilterPortGroupMaskId_Type()
)
a3ComFilterPortGroupMaskId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupMaskId.setStatus("mandatory")
_A3ComFilterPortGroupBridgeNumber_Type = Integer32
_A3ComFilterPortGroupBridgeNumber_Object = MibTableColumn
a3ComFilterPortGroupBridgeNumber = _A3ComFilterPortGroupBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 3),
    _A3ComFilterPortGroupBridgeNumber_Type()
)
a3ComFilterPortGroupBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupBridgeNumber.setStatus("mandatory")


class _A3ComFilterPortGroupName_Type(DisplayString):
    """Custom type a3ComFilterPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_A3ComFilterPortGroupName_Type.__name__ = "DisplayString"
_A3ComFilterPortGroupName_Object = MibTableColumn
a3ComFilterPortGroupName = _A3ComFilterPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 4),
    _A3ComFilterPortGroupName_Type()
)
a3ComFilterPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupName.setStatus("mandatory")
_A3ComFilterPortGroupStatus_Type = RowStatus
_A3ComFilterPortGroupStatus_Object = MibTableColumn
a3ComFilterPortGroupStatus = _A3ComFilterPortGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 3, 1, 5),
    _A3ComFilterPortGroupStatus_Type()
)
a3ComFilterPortGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterPortGroupStatus.setStatus("mandatory")
_A3ComFilterPortTable_Object = MibTable
a3ComFilterPortTable = _A3ComFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4)
)
if mibBuilder.loadTexts:
    a3ComFilterPortTable.setStatus("mandatory")
_A3ComFilterPortEntry_Object = MibTableRow
a3ComFilterPortEntry = _A3ComFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1)
)
a3ComFilterPortEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortId"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortType"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComFilterPortPort"),
)
if mibBuilder.loadTexts:
    a3ComFilterPortEntry.setStatus("mandatory")


class _A3ComFilterPortId_Type(Integer32):
    """Custom type a3ComFilterPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFilterPortId_Type.__name__ = "Integer32"
_A3ComFilterPortId_Object = MibTableColumn
a3ComFilterPortId = _A3ComFilterPortId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 1),
    _A3ComFilterPortId_Type()
)
a3ComFilterPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortId.setStatus("mandatory")
_A3ComFilterPortType_Type = A3ComFilterPortType
_A3ComFilterPortType_Object = MibTableColumn
a3ComFilterPortType = _A3ComFilterPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 2),
    _A3ComFilterPortType_Type()
)
a3ComFilterPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortType.setStatus("mandatory")


class _A3ComFilterPortPort_Type(Integer32):
    """Custom type a3ComFilterPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComFilterPortPort_Type.__name__ = "Integer32"
_A3ComFilterPortPort_Object = MibTableColumn
a3ComFilterPortPort = _A3ComFilterPortPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 3),
    _A3ComFilterPortPort_Type()
)
a3ComFilterPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComFilterPortPort.setStatus("mandatory")
_A3ComFilterPortStatus_Type = RowStatus
_A3ComFilterPortStatus_Object = MibTableColumn
a3ComFilterPortStatus = _A3ComFilterPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 2, 4, 1, 4),
    _A3ComFilterPortStatus_Type()
)
a3ComFilterPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComFilterPortStatus.setStatus("mandatory")
_A3ComBridgeFilterGroup_ObjectIdentity = ObjectIdentity
a3ComBridgeFilterGroup = _A3ComBridgeFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3)
)
_A3ComBridgeFilterNextAvailableIndex_Type = Integer32
_A3ComBridgeFilterNextAvailableIndex_Object = MibScalar
a3ComBridgeFilterNextAvailableIndex = _A3ComBridgeFilterNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 1),
    _A3ComBridgeFilterNextAvailableIndex_Type()
)
a3ComBridgeFilterNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterNextAvailableIndex.setStatus("mandatory")
_A3ComBridgeFilterCount_Type = Integer32
_A3ComBridgeFilterCount_Object = MibScalar
a3ComBridgeFilterCount = _A3ComBridgeFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 2),
    _A3ComBridgeFilterCount_Type()
)
a3ComBridgeFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterCount.setStatus("mandatory")
_A3ComBridgeFilterTable_Object = MibTable
a3ComBridgeFilterTable = _A3ComBridgeFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3)
)
if mibBuilder.loadTexts:
    a3ComBridgeFilterTable.setStatus("mandatory")
_A3ComBridgeFilterEntry_Object = MibTableRow
a3ComBridgeFilterEntry = _A3ComBridgeFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1)
)
a3ComBridgeFilterEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComBridgeFilterId"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComBridgeFilterBridgeNumber"),
)
if mibBuilder.loadTexts:
    a3ComBridgeFilterEntry.setStatus("mandatory")


class _A3ComBridgeFilterId_Type(Integer32):
    """Custom type a3ComBridgeFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComBridgeFilterId_Type.__name__ = "Integer32"
_A3ComBridgeFilterId_Object = MibTableColumn
a3ComBridgeFilterId = _A3ComBridgeFilterId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 1),
    _A3ComBridgeFilterId_Type()
)
a3ComBridgeFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterId.setStatus("mandatory")


class _A3ComBridgeFilterBridgeNumber_Type(Integer32):
    """Custom type a3ComBridgeFilterBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComBridgeFilterBridgeNumber_Type.__name__ = "Integer32"
_A3ComBridgeFilterBridgeNumber_Object = MibTableColumn
a3ComBridgeFilterBridgeNumber = _A3ComBridgeFilterBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 2),
    _A3ComBridgeFilterBridgeNumber_Type()
)
a3ComBridgeFilterBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterBridgeNumber.setStatus("mandatory")


class _A3ComBridgeFilterName_Type(DisplayString):
    """Custom type a3ComBridgeFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_A3ComBridgeFilterName_Type.__name__ = "DisplayString"
_A3ComBridgeFilterName_Object = MibTableColumn
a3ComBridgeFilterName = _A3ComBridgeFilterName_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 3),
    _A3ComBridgeFilterName_Type()
)
a3ComBridgeFilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterName.setStatus("mandatory")


class _A3ComBridgeFilterProgram_Type(DisplayString):
    """Custom type a3ComBridgeFilterProgram based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_A3ComBridgeFilterProgram_Type.__name__ = "DisplayString"
_A3ComBridgeFilterProgram_Object = MibTableColumn
a3ComBridgeFilterProgram = _A3ComBridgeFilterProgram_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 4),
    _A3ComBridgeFilterProgram_Type()
)
a3ComBridgeFilterProgram.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComBridgeFilterProgram.setStatus("mandatory")
_A3ComBridgeFilterStatus_Type = RowStatus
_A3ComBridgeFilterStatus_Object = MibTableColumn
a3ComBridgeFilterStatus = _A3ComBridgeFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 3, 1, 5),
    _A3ComBridgeFilterStatus_Type()
)
a3ComBridgeFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComBridgeFilterStatus.setStatus("mandatory")
_A3ComPortFilterTable_Object = MibTable
a3ComPortFilterTable = _A3ComPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4)
)
if mibBuilder.loadTexts:
    a3ComPortFilterTable.setStatus("mandatory")
_A3ComPortFilterEntry_Object = MibTableRow
a3ComPortFilterEntry = _A3ComPortFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1)
)
a3ComPortFilterEntry.setIndexNames(
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterId"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgeNumber"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgePortType"),
    (0, "A3COM-SWITCHING-SYSTEMS-FILTER-MIB", "a3ComPortFilterBridgePortPort"),
)
if mibBuilder.loadTexts:
    a3ComPortFilterEntry.setStatus("mandatory")


class _A3ComPortFilterId_Type(Integer32):
    """Custom type a3ComPortFilterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComPortFilterId_Type.__name__ = "Integer32"
_A3ComPortFilterId_Object = MibTableColumn
a3ComPortFilterId = _A3ComPortFilterId_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 1),
    _A3ComPortFilterId_Type()
)
a3ComPortFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortFilterId.setStatus("mandatory")


class _A3ComPortFilterBridgeNumber_Type(Integer32):
    """Custom type a3ComPortFilterBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComPortFilterBridgeNumber_Type.__name__ = "Integer32"
_A3ComPortFilterBridgeNumber_Object = MibTableColumn
a3ComPortFilterBridgeNumber = _A3ComPortFilterBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 2),
    _A3ComPortFilterBridgeNumber_Type()
)
a3ComPortFilterBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortFilterBridgeNumber.setStatus("mandatory")
_A3ComPortFilterBridgePortType_Type = A3ComFilterPortType
_A3ComPortFilterBridgePortType_Object = MibTableColumn
a3ComPortFilterBridgePortType = _A3ComPortFilterBridgePortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 3),
    _A3ComPortFilterBridgePortType_Type()
)
a3ComPortFilterBridgePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortFilterBridgePortType.setStatus("mandatory")


class _A3ComPortFilterBridgePortPort_Type(Integer32):
    """Custom type a3ComPortFilterBridgePortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_A3ComPortFilterBridgePortPort_Type.__name__ = "Integer32"
_A3ComPortFilterBridgePortPort_Object = MibTableColumn
a3ComPortFilterBridgePortPort = _A3ComPortFilterBridgePortPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 4),
    _A3ComPortFilterBridgePortPort_Type()
)
a3ComPortFilterBridgePortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    a3ComPortFilterBridgePortPort.setStatus("mandatory")
_A3ComPortFilterPktProcessPath_Type = Integer32
_A3ComPortFilterPktProcessPath_Object = MibTableColumn
a3ComPortFilterPktProcessPath = _A3ComPortFilterPktProcessPath_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 5),
    _A3ComPortFilterPktProcessPath_Type()
)
a3ComPortFilterPktProcessPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortFilterPktProcessPath.setStatus("mandatory")
_A3ComPortFilterStatus_Type = RowStatus
_A3ComPortFilterStatus_Object = MibTableColumn
a3ComPortFilterStatus = _A3ComPortFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 29, 4, 20, 3, 4, 1, 6),
    _A3ComPortFilterStatus_Type()
)
a3ComPortFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    a3ComPortFilterStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-FILTER-MIB",
    **{"RowStatus": RowStatus,
       "A3ComFilterPortType": A3ComFilterPortType,
       "a3Com": a3Com,
       "switchingSystemsMibs": switchingSystemsMibs,
       "a3ComSwitchingSystemsMib": a3ComSwitchingSystemsMib,
       "a3ComFilterGroup": a3ComFilterGroup,
       "a3ComFilterAddressGroup": a3ComFilterAddressGroup,
       "a3ComFilterAddressGroupNextAvailableIndex": a3ComFilterAddressGroupNextAvailableIndex,
       "a3ComFilterAddressGroupCount": a3ComFilterAddressGroupCount,
       "a3ComFilterAddressGroupTable": a3ComFilterAddressGroupTable,
       "a3ComFilterAddressGroupEntry": a3ComFilterAddressGroupEntry,
       "a3ComFilterAddressGroupId": a3ComFilterAddressGroupId,
       "a3ComFilterAddressGroupMaskId": a3ComFilterAddressGroupMaskId,
       "a3ComFilterAddressGroupBridgeMask": a3ComFilterAddressGroupBridgeMask,
       "a3ComFilterAddressGroupName": a3ComFilterAddressGroupName,
       "a3ComFilterAddressGroupStatus": a3ComFilterAddressGroupStatus,
       "a3ComFilterAddressTable": a3ComFilterAddressTable,
       "a3ComFilterAddressEntry": a3ComFilterAddressEntry,
       "a3ComFilterAddressId": a3ComFilterAddressId,
       "a3ComFilterAddressAddress": a3ComFilterAddressAddress,
       "a3ComFilterAddressStatus": a3ComFilterAddressStatus,
       "a3ComFilterPortGroup": a3ComFilterPortGroup,
       "a3ComFilterPortGroupNextAvailableIndex": a3ComFilterPortGroupNextAvailableIndex,
       "a3ComFilterPortGroupCount": a3ComFilterPortGroupCount,
       "a3ComFilterPortGroupTable": a3ComFilterPortGroupTable,
       "a3ComFilterPortGroupEntry": a3ComFilterPortGroupEntry,
       "a3ComFilterPortGroupId": a3ComFilterPortGroupId,
       "a3ComFilterPortGroupMaskId": a3ComFilterPortGroupMaskId,
       "a3ComFilterPortGroupBridgeNumber": a3ComFilterPortGroupBridgeNumber,
       "a3ComFilterPortGroupName": a3ComFilterPortGroupName,
       "a3ComFilterPortGroupStatus": a3ComFilterPortGroupStatus,
       "a3ComFilterPortTable": a3ComFilterPortTable,
       "a3ComFilterPortEntry": a3ComFilterPortEntry,
       "a3ComFilterPortId": a3ComFilterPortId,
       "a3ComFilterPortType": a3ComFilterPortType,
       "a3ComFilterPortPort": a3ComFilterPortPort,
       "a3ComFilterPortStatus": a3ComFilterPortStatus,
       "a3ComBridgeFilterGroup": a3ComBridgeFilterGroup,
       "a3ComBridgeFilterNextAvailableIndex": a3ComBridgeFilterNextAvailableIndex,
       "a3ComBridgeFilterCount": a3ComBridgeFilterCount,
       "a3ComBridgeFilterTable": a3ComBridgeFilterTable,
       "a3ComBridgeFilterEntry": a3ComBridgeFilterEntry,
       "a3ComBridgeFilterId": a3ComBridgeFilterId,
       "a3ComBridgeFilterBridgeNumber": a3ComBridgeFilterBridgeNumber,
       "a3ComBridgeFilterName": a3ComBridgeFilterName,
       "a3ComBridgeFilterProgram": a3ComBridgeFilterProgram,
       "a3ComBridgeFilterStatus": a3ComBridgeFilterStatus,
       "a3ComPortFilterTable": a3ComPortFilterTable,
       "a3ComPortFilterEntry": a3ComPortFilterEntry,
       "a3ComPortFilterId": a3ComPortFilterId,
       "a3ComPortFilterBridgeNumber": a3ComPortFilterBridgeNumber,
       "a3ComPortFilterBridgePortType": a3ComPortFilterBridgePortType,
       "a3ComPortFilterBridgePortPort": a3ComPortFilterBridgePortPort,
       "a3ComPortFilterPktProcessPath": a3ComPortFilterPktProcessPath,
       "a3ComPortFilterStatus": a3ComPortFilterStatus}
)
