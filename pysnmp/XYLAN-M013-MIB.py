# SNMP MIB module (XYLAN-M013-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-M013-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:07 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanM013Arch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanM013Arch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_M013ProvisioningGroup_ObjectIdentity = ObjectIdentity
m013ProvisioningGroup = _M013ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1)
)
_M013ProvisioningTable_Object = MibTable
m013ProvisioningTable = _M013ProvisioningTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1)
)
if mibBuilder.loadTexts:
    m013ProvisioningTable.setStatus("mandatory")
_M013ProvisioningEntry_Object = MibTableRow
m013ProvisioningEntry = _M013ProvisioningEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1)
)
m013ProvisioningEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013SlotIndex"),
    (0, "XYLAN-M013-MIB", "m013LogicalPortIndex"),
)
if mibBuilder.loadTexts:
    m013ProvisioningEntry.setStatus("mandatory")


class _M013SlotIndex_Type(Integer32):
    """Custom type m013SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013SlotIndex_Type.__name__ = "Integer32"
_M013SlotIndex_Object = MibTableColumn
m013SlotIndex = _M013SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 1),
    _M013SlotIndex_Type()
)
m013SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013SlotIndex.setStatus("mandatory")


class _M013LogicalPortIndex_Type(Integer32):
    """Custom type m013LogicalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013LogicalPortIndex_Type.__name__ = "Integer32"
_M013LogicalPortIndex_Object = MibTableColumn
m013LogicalPortIndex = _M013LogicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 2),
    _M013LogicalPortIndex_Type()
)
m013LogicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013LogicalPortIndex.setStatus("mandatory")


class _M013Description_Type(DisplayString):
    """Custom type m013Description based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013Description_Type.__name__ = "DisplayString"
_M013Description_Object = MibTableColumn
m013Description = _M013Description_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 3),
    _M013Description_Type()
)
m013Description.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Description.setStatus("mandatory")


class _M013Ds3PortIndex_Type(Integer32):
    """Custom type m013Ds3PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_M013Ds3PortIndex_Type.__name__ = "Integer32"
_M013Ds3PortIndex_Object = MibTableColumn
m013Ds3PortIndex = _M013Ds3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 4),
    _M013Ds3PortIndex_Type()
)
m013Ds3PortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Ds3PortIndex.setStatus("mandatory")


class _M013Ds1Fraction_Type(Integer32):
    """Custom type m013Ds1Fraction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_M013Ds1Fraction_Type.__name__ = "Integer32"
_M013Ds1Fraction_Object = MibTableColumn
m013Ds1Fraction = _M013Ds1Fraction_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 5),
    _M013Ds1Fraction_Type()
)
m013Ds1Fraction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Ds1Fraction.setStatus("mandatory")


class _M013Ds0Mask_Type(Integer32):
    """Custom type m013Ds0Mask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_M013Ds0Mask_Type.__name__ = "Integer32"
_M013Ds0Mask_Object = MibTableColumn
m013Ds0Mask = _M013Ds0Mask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 6),
    _M013Ds0Mask_Type()
)
m013Ds0Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Ds0Mask.setStatus("mandatory")


class _M013IfIndex_Type(Integer32):
    """Custom type m013IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10001, 18192),
    )


_M013IfIndex_Type.__name__ = "Integer32"
_M013IfIndex_Object = MibTableColumn
m013IfIndex = _M013IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 7),
    _M013IfIndex_Type()
)
m013IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013IfIndex.setStatus("mandatory")


class _M013Protocol_Type(Integer32):
    """Custom type m013Protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fr", 1),
          ("ppp", 2))
    )


_M013Protocol_Type.__name__ = "Integer32"
_M013Protocol_Object = MibTableColumn
m013Protocol = _M013Protocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 8),
    _M013Protocol_Type()
)
m013Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Protocol.setStatus("mandatory")


class _M013EntryStatus_Type(Integer32):
    """Custom type m013EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_M013EntryStatus_Type.__name__ = "Integer32"
_M013EntryStatus_Object = MibTableColumn
m013EntryStatus = _M013EntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 1, 1, 1, 9),
    _M013EntryStatus_Type()
)
m013EntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013EntryStatus.setStatus("mandatory")
_M013ServiceGroup_ObjectIdentity = ObjectIdentity
m013ServiceGroup = _M013ServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2)
)
_M013ServiceTable_Object = MibTable
m013ServiceTable = _M013ServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1)
)
if mibBuilder.loadTexts:
    m013ServiceTable.setStatus("mandatory")
_M013ServiceEntry_Object = MibTableRow
m013ServiceEntry = _M013ServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1)
)
m013ServiceEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013ServiceSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013ServiceLogicalPortIndex"),
    (0, "XYLAN-M013-MIB", "m013ServiceNumber"),
    (0, "XYLAN-M013-MIB", "m013ServiceType"),
)
if mibBuilder.loadTexts:
    m013ServiceEntry.setStatus("mandatory")


class _M013ServiceSlotIndex_Type(Integer32):
    """Custom type m013ServiceSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013ServiceSlotIndex_Type.__name__ = "Integer32"
_M013ServiceSlotIndex_Object = MibTableColumn
m013ServiceSlotIndex = _M013ServiceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 1),
    _M013ServiceSlotIndex_Type()
)
m013ServiceSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceSlotIndex.setStatus("mandatory")


class _M013ServiceLogicalPortIndex_Type(Integer32):
    """Custom type m013ServiceLogicalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013ServiceLogicalPortIndex_Type.__name__ = "Integer32"
_M013ServiceLogicalPortIndex_Object = MibTableColumn
m013ServiceLogicalPortIndex = _M013ServiceLogicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 2),
    _M013ServiceLogicalPortIndex_Type()
)
m013ServiceLogicalPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceLogicalPortIndex.setStatus("mandatory")


class _M013ServiceNumber_Type(Integer32):
    """Custom type m013ServiceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_M013ServiceNumber_Type.__name__ = "Integer32"
_M013ServiceNumber_Object = MibTableColumn
m013ServiceNumber = _M013ServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 3),
    _M013ServiceNumber_Type()
)
m013ServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013ServiceNumber.setStatus("mandatory")


class _M013ServiceTableEntryType_Type(Integer32):
    """Custom type m013ServiceTableEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_M013ServiceTableEntryType_Type.__name__ = "Integer32"
_M013ServiceTableEntryType_Object = MibTableColumn
m013ServiceTableEntryType = _M013ServiceTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 4),
    _M013ServiceTableEntryType_Type()
)
m013ServiceTableEntryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceTableEntryType.setStatus("mandatory")


class _M013ServiceDescription_Type(DisplayString):
    """Custom type m013ServiceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013ServiceDescription_Type.__name__ = "DisplayString"
_M013ServiceDescription_Object = MibTableColumn
m013ServiceDescription = _M013ServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 5),
    _M013ServiceDescription_Type()
)
m013ServiceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceDescription.setStatus("mandatory")


class _M013ServiceType_Type(Integer32):
    """Custom type m013ServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 6),
          ("trunking", 4))
    )


_M013ServiceType_Type.__name__ = "Integer32"
_M013ServiceType_Object = MibTableColumn
m013ServiceType = _M013ServiceType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 6),
    _M013ServiceType_Type()
)
m013ServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceType.setStatus("mandatory")


class _M013ServiceOperStatus_Type(Integer32):
    """Custom type m013ServiceOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013ServiceOperStatus_Type.__name__ = "Integer32"
_M013ServiceOperStatus_Object = MibTableColumn
m013ServiceOperStatus = _M013ServiceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 7),
    _M013ServiceOperStatus_Type()
)
m013ServiceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013ServiceOperStatus.setStatus("mandatory")


class _M013ServiceAdminStatus_Type(Integer32):
    """Custom type m013ServiceAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_M013ServiceAdminStatus_Type.__name__ = "Integer32"
_M013ServiceAdminStatus_Object = MibTableColumn
m013ServiceAdminStatus = _M013ServiceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 8),
    _M013ServiceAdminStatus_Type()
)
m013ServiceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceAdminStatus.setStatus("mandatory")


class _M013ServiceVirtualCircuit_Type(Integer32):
    """Custom type m013ServiceVirtualCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_M013ServiceVirtualCircuit_Type.__name__ = "Integer32"
_M013ServiceVirtualCircuit_Object = MibTableColumn
m013ServiceVirtualCircuit = _M013ServiceVirtualCircuit_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 9),
    _M013ServiceVirtualCircuit_Type()
)
m013ServiceVirtualCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceVirtualCircuit.setStatus("mandatory")


class _M013ServiceVlans_Type(OctetString):
    """Custom type m013ServiceVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_M013ServiceVlans_Type.__name__ = "OctetString"
_M013ServiceVlans_Object = MibTableColumn
m013ServiceVlans = _M013ServiceVlans_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 10),
    _M013ServiceVlans_Type()
)
m013ServiceVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceVlans.setStatus("mandatory")


class _M013ServiceBridgingMode_Type(Integer32):
    """Custom type m013ServiceBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_M013ServiceBridgingMode_Type.__name__ = "Integer32"
_M013ServiceBridgingMode_Object = MibTableColumn
m013ServiceBridgingMode = _M013ServiceBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 2, 1, 1, 11),
    _M013ServiceBridgingMode_Type()
)
m013ServiceBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013ServiceBridgingMode.setStatus("mandatory")
_M013FrxPortGroup_ObjectIdentity = ObjectIdentity
m013FrxPortGroup = _M013FrxPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3)
)
_M013FrxPortTable_Object = MibTable
m013FrxPortTable = _M013FrxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1)
)
if mibBuilder.loadTexts:
    m013FrxPortTable.setStatus("mandatory")
_M013FrxPortEntry_Object = MibTableRow
m013FrxPortEntry = _M013FrxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1)
)
m013FrxPortEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013FrxPortSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013FrxPortPortIndex"),
)
if mibBuilder.loadTexts:
    m013FrxPortEntry.setStatus("mandatory")


class _M013FrxPortSlotIndex_Type(Integer32):
    """Custom type m013FrxPortSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013FrxPortSlotIndex_Type.__name__ = "Integer32"
_M013FrxPortSlotIndex_Object = MibTableColumn
m013FrxPortSlotIndex = _M013FrxPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 1),
    _M013FrxPortSlotIndex_Type()
)
m013FrxPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxPortSlotIndex.setStatus("mandatory")


class _M013FrxPortPortIndex_Type(Integer32):
    """Custom type m013FrxPortPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013FrxPortPortIndex_Type.__name__ = "Integer32"
_M013FrxPortPortIndex_Object = MibTableColumn
m013FrxPortPortIndex = _M013FrxPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 2),
    _M013FrxPortPortIndex_Type()
)
m013FrxPortPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxPortPortIndex.setStatus("mandatory")


class _M013FrxPortDescription_Type(DisplayString):
    """Custom type m013FrxPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013FrxPortDescription_Type.__name__ = "DisplayString"
_M013FrxPortDescription_Object = MibTableColumn
m013FrxPortDescription = _M013FrxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 3),
    _M013FrxPortDescription_Type()
)
m013FrxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDescription.setStatus("mandatory")


class _M013FrxPortAdminStatus_Type(Integer32):
    """Custom type m013FrxPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013FrxPortAdminStatus_Type.__name__ = "Integer32"
_M013FrxPortAdminStatus_Object = MibTableColumn
m013FrxPortAdminStatus = _M013FrxPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 4),
    _M013FrxPortAdminStatus_Type()
)
m013FrxPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortAdminStatus.setStatus("mandatory")


class _M013FrxPortDefaultIpRoutingAdminStatus_Type(Integer32):
    """Custom type m013FrxPortDefaultIpRoutingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013FrxPortDefaultIpRoutingAdminStatus_Type.__name__ = "Integer32"
_M013FrxPortDefaultIpRoutingAdminStatus_Object = MibTableColumn
m013FrxPortDefaultIpRoutingAdminStatus = _M013FrxPortDefaultIpRoutingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 5),
    _M013FrxPortDefaultIpRoutingAdminStatus_Type()
)
m013FrxPortDefaultIpRoutingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDefaultIpRoutingAdminStatus.setStatus("mandatory")


class _M013FrxPortDefaultBridgingAdminStatus_Type(Integer32):
    """Custom type m013FrxPortDefaultBridgingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013FrxPortDefaultBridgingAdminStatus_Type.__name__ = "Integer32"
_M013FrxPortDefaultBridgingAdminStatus_Object = MibTableColumn
m013FrxPortDefaultBridgingAdminStatus = _M013FrxPortDefaultBridgingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 6),
    _M013FrxPortDefaultBridgingAdminStatus_Type()
)
m013FrxPortDefaultBridgingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDefaultBridgingAdminStatus.setStatus("mandatory")


class _M013FrxPortDefaultBridgingVLAN_Type(Integer32):
    """Custom type m013FrxPortDefaultBridgingVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_M013FrxPortDefaultBridgingVLAN_Type.__name__ = "Integer32"
_M013FrxPortDefaultBridgingVLAN_Object = MibTableColumn
m013FrxPortDefaultBridgingVLAN = _M013FrxPortDefaultBridgingVLAN_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 7),
    _M013FrxPortDefaultBridgingVLAN_Type()
)
m013FrxPortDefaultBridgingVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDefaultBridgingVLAN.setStatus("mandatory")


class _M013FrxPortDefaultBridgingMode_Type(Integer32):
    """Custom type m013FrxPortDefaultBridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_M013FrxPortDefaultBridgingMode_Type.__name__ = "Integer32"
_M013FrxPortDefaultBridgingMode_Object = MibTableColumn
m013FrxPortDefaultBridgingMode = _M013FrxPortDefaultBridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 8),
    _M013FrxPortDefaultBridgingMode_Type()
)
m013FrxPortDefaultBridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDefaultBridgingMode.setStatus("mandatory")


class _M013FrxPortDynamicVCCreation_Type(Integer32):
    """Custom type m013FrxPortDynamicVCCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013FrxPortDynamicVCCreation_Type.__name__ = "Integer32"
_M013FrxPortDynamicVCCreation_Object = MibTableColumn
m013FrxPortDynamicVCCreation = _M013FrxPortDynamicVCCreation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 3, 1, 1, 9),
    _M013FrxPortDynamicVCCreation_Type()
)
m013FrxPortDynamicVCCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxPortDynamicVCCreation.setStatus("mandatory")
_M013FrxVcControlGroup_ObjectIdentity = ObjectIdentity
m013FrxVcControlGroup = _M013FrxVcControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4)
)
_M013FrxVcControlTable_Object = MibTable
m013FrxVcControlTable = _M013FrxVcControlTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1)
)
if mibBuilder.loadTexts:
    m013FrxVcControlTable.setStatus("mandatory")
_M013FrxVcControlEntry_Object = MibTableRow
m013FrxVcControlEntry = _M013FrxVcControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1, 1)
)
m013FrxVcControlEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013FrxVcControlSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013FrxVcControlPortIndex"),
    (0, "XYLAN-M013-MIB", "m013FrxVcControlDlci"),
)
if mibBuilder.loadTexts:
    m013FrxVcControlEntry.setStatus("mandatory")


class _M013FrxVcControlSlotIndex_Type(Integer32):
    """Custom type m013FrxVcControlSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013FrxVcControlSlotIndex_Type.__name__ = "Integer32"
_M013FrxVcControlSlotIndex_Object = MibTableColumn
m013FrxVcControlSlotIndex = _M013FrxVcControlSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1, 1, 1),
    _M013FrxVcControlSlotIndex_Type()
)
m013FrxVcControlSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcControlSlotIndex.setStatus("mandatory")


class _M013FrxVcControlPortIndex_Type(Integer32):
    """Custom type m013FrxVcControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013FrxVcControlPortIndex_Type.__name__ = "Integer32"
_M013FrxVcControlPortIndex_Object = MibTableColumn
m013FrxVcControlPortIndex = _M013FrxVcControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1, 1, 2),
    _M013FrxVcControlPortIndex_Type()
)
m013FrxVcControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcControlPortIndex.setStatus("mandatory")


class _M013FrxVcControlDlci_Type(Integer32):
    """Custom type m013FrxVcControlDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013FrxVcControlDlci_Type.__name__ = "Integer32"
_M013FrxVcControlDlci_Object = MibTableColumn
m013FrxVcControlDlci = _M013FrxVcControlDlci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1, 1, 3),
    _M013FrxVcControlDlci_Type()
)
m013FrxVcControlDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcControlDlci.setStatus("mandatory")


class _M013FrxVcControlIpRoutingAdminStatus_Type(Integer32):
    """Custom type m013FrxVcControlIpRoutingAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013FrxVcControlIpRoutingAdminStatus_Type.__name__ = "Integer32"
_M013FrxVcControlIpRoutingAdminStatus_Object = MibTableColumn
m013FrxVcControlIpRoutingAdminStatus = _M013FrxVcControlIpRoutingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 4, 1, 1, 4),
    _M013FrxVcControlIpRoutingAdminStatus_Type()
)
m013FrxVcControlIpRoutingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013FrxVcControlIpRoutingAdminStatus.setStatus("mandatory")
_M013FrxVcStatsGroup_ObjectIdentity = ObjectIdentity
m013FrxVcStatsGroup = _M013FrxVcStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5)
)
_M013FrxVcStatsTable_Object = MibTable
m013FrxVcStatsTable = _M013FrxVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1)
)
if mibBuilder.loadTexts:
    m013FrxVcStatsTable.setStatus("mandatory")
_M013FrxVcStatsEntry_Object = MibTableRow
m013FrxVcStatsEntry = _M013FrxVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1)
)
m013FrxVcStatsEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013FrxVcStatsSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013FrxVcStatsPortIndex"),
    (0, "XYLAN-M013-MIB", "m013FrxVcStatsDlci"),
)
if mibBuilder.loadTexts:
    m013FrxVcStatsEntry.setStatus("mandatory")


class _M013FrxVcStatsSlotIndex_Type(Integer32):
    """Custom type m013FrxVcStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013FrxVcStatsSlotIndex_Type.__name__ = "Integer32"
_M013FrxVcStatsSlotIndex_Object = MibTableColumn
m013FrxVcStatsSlotIndex = _M013FrxVcStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 1),
    _M013FrxVcStatsSlotIndex_Type()
)
m013FrxVcStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsSlotIndex.setStatus("mandatory")


class _M013FrxVcStatsPortIndex_Type(Integer32):
    """Custom type m013FrxVcStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013FrxVcStatsPortIndex_Type.__name__ = "Integer32"
_M013FrxVcStatsPortIndex_Object = MibTableColumn
m013FrxVcStatsPortIndex = _M013FrxVcStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 2),
    _M013FrxVcStatsPortIndex_Type()
)
m013FrxVcStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsPortIndex.setStatus("mandatory")


class _M013FrxVcStatsDlci_Type(Integer32):
    """Custom type m013FrxVcStatsDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_M013FrxVcStatsDlci_Type.__name__ = "Integer32"
_M013FrxVcStatsDlci_Object = MibTableColumn
m013FrxVcStatsDlci = _M013FrxVcStatsDlci_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 3),
    _M013FrxVcStatsDlci_Type()
)
m013FrxVcStatsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsDlci.setStatus("mandatory")
_M013FrxVcStatsTxIPOctets_Type = Counter32
_M013FrxVcStatsTxIPOctets_Object = MibTableColumn
m013FrxVcStatsTxIPOctets = _M013FrxVcStatsTxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 4),
    _M013FrxVcStatsTxIPOctets_Type()
)
m013FrxVcStatsTxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxIPOctets.setStatus("mandatory")
_M013FrxVcStatsTxIPFrames_Type = Counter32
_M013FrxVcStatsTxIPFrames_Object = MibTableColumn
m013FrxVcStatsTxIPFrames = _M013FrxVcStatsTxIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 5),
    _M013FrxVcStatsTxIPFrames_Type()
)
m013FrxVcStatsTxIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxIPFrames.setStatus("mandatory")
_M013FrxVcStatsRxIPOctets_Type = Counter32
_M013FrxVcStatsRxIPOctets_Object = MibTableColumn
m013FrxVcStatsRxIPOctets = _M013FrxVcStatsRxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 6),
    _M013FrxVcStatsRxIPOctets_Type()
)
m013FrxVcStatsRxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxIPOctets.setStatus("mandatory")
_M013FrxVcStatsRxIPFrames_Type = Counter32
_M013FrxVcStatsRxIPFrames_Object = MibTableColumn
m013FrxVcStatsRxIPFrames = _M013FrxVcStatsRxIPFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 7),
    _M013FrxVcStatsRxIPFrames_Type()
)
m013FrxVcStatsRxIPFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxIPFrames.setStatus("mandatory")
_M013FrxVcStatsTxIPXOctets_Type = Counter32
_M013FrxVcStatsTxIPXOctets_Object = MibTableColumn
m013FrxVcStatsTxIPXOctets = _M013FrxVcStatsTxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 8),
    _M013FrxVcStatsTxIPXOctets_Type()
)
m013FrxVcStatsTxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxIPXOctets.setStatus("mandatory")
_M013FrxVcStatsTxIPXFrames_Type = Counter32
_M013FrxVcStatsTxIPXFrames_Object = MibTableColumn
m013FrxVcStatsTxIPXFrames = _M013FrxVcStatsTxIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 9),
    _M013FrxVcStatsTxIPXFrames_Type()
)
m013FrxVcStatsTxIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxIPXFrames.setStatus("mandatory")
_M013FrxVcStatsRxIPXOctets_Type = Counter32
_M013FrxVcStatsRxIPXOctets_Object = MibTableColumn
m013FrxVcStatsRxIPXOctets = _M013FrxVcStatsRxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 10),
    _M013FrxVcStatsRxIPXOctets_Type()
)
m013FrxVcStatsRxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxIPXOctets.setStatus("mandatory")
_M013FrxVcStatsRxIPXFrames_Type = Counter32
_M013FrxVcStatsRxIPXFrames_Object = MibTableColumn
m013FrxVcStatsRxIPXFrames = _M013FrxVcStatsRxIPXFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 11),
    _M013FrxVcStatsRxIPXFrames_Type()
)
m013FrxVcStatsRxIPXFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxIPXFrames.setStatus("mandatory")
_M013FrxVcStatsTxBPDUOctets_Type = Counter32
_M013FrxVcStatsTxBPDUOctets_Object = MibTableColumn
m013FrxVcStatsTxBPDUOctets = _M013FrxVcStatsTxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 12),
    _M013FrxVcStatsTxBPDUOctets_Type()
)
m013FrxVcStatsTxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxBPDUOctets.setStatus("mandatory")
_M013FrxVcStatsTxBPDUFrames_Type = Counter32
_M013FrxVcStatsTxBPDUFrames_Object = MibTableColumn
m013FrxVcStatsTxBPDUFrames = _M013FrxVcStatsTxBPDUFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 13),
    _M013FrxVcStatsTxBPDUFrames_Type()
)
m013FrxVcStatsTxBPDUFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxBPDUFrames.setStatus("mandatory")
_M013FrxVcStatsRxBPDUOctets_Type = Counter32
_M013FrxVcStatsRxBPDUOctets_Object = MibTableColumn
m013FrxVcStatsRxBPDUOctets = _M013FrxVcStatsRxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 14),
    _M013FrxVcStatsRxBPDUOctets_Type()
)
m013FrxVcStatsRxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxBPDUOctets.setStatus("mandatory")
_M013FrxVcStatsRxBPDUFrames_Type = Counter32
_M013FrxVcStatsRxBPDUFrames_Object = MibTableColumn
m013FrxVcStatsRxBPDUFrames = _M013FrxVcStatsRxBPDUFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 15),
    _M013FrxVcStatsRxBPDUFrames_Type()
)
m013FrxVcStatsRxBPDUFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxBPDUFrames.setStatus("mandatory")
_M013FrxVcStatsTxEthernetOctets_Type = Counter32
_M013FrxVcStatsTxEthernetOctets_Object = MibTableColumn
m013FrxVcStatsTxEthernetOctets = _M013FrxVcStatsTxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 16),
    _M013FrxVcStatsTxEthernetOctets_Type()
)
m013FrxVcStatsTxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxEthernetOctets.setStatus("mandatory")
_M013FrxVcStatsTxEthernetFrames_Type = Counter32
_M013FrxVcStatsTxEthernetFrames_Object = MibTableColumn
m013FrxVcStatsTxEthernetFrames = _M013FrxVcStatsTxEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 17),
    _M013FrxVcStatsTxEthernetFrames_Type()
)
m013FrxVcStatsTxEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxEthernetFrames.setStatus("mandatory")
_M013FrxVcStatsRxEthernetOctets_Type = Counter32
_M013FrxVcStatsRxEthernetOctets_Object = MibTableColumn
m013FrxVcStatsRxEthernetOctets = _M013FrxVcStatsRxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 18),
    _M013FrxVcStatsRxEthernetOctets_Type()
)
m013FrxVcStatsRxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxEthernetOctets.setStatus("mandatory")
_M013FrxVcStatsRxEthernetFrames_Type = Counter32
_M013FrxVcStatsRxEthernetFrames_Object = MibTableColumn
m013FrxVcStatsRxEthernetFrames = _M013FrxVcStatsRxEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 19),
    _M013FrxVcStatsRxEthernetFrames_Type()
)
m013FrxVcStatsRxEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxEthernetFrames.setStatus("mandatory")
_M013FrxVcStatsTx8025Octets_Type = Counter32
_M013FrxVcStatsTx8025Octets_Object = MibTableColumn
m013FrxVcStatsTx8025Octets = _M013FrxVcStatsTx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 20),
    _M013FrxVcStatsTx8025Octets_Type()
)
m013FrxVcStatsTx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTx8025Octets.setStatus("mandatory")
_M013FrxVcStatsTx8025Frames_Type = Counter32
_M013FrxVcStatsTx8025Frames_Object = MibTableColumn
m013FrxVcStatsTx8025Frames = _M013FrxVcStatsTx8025Frames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 21),
    _M013FrxVcStatsTx8025Frames_Type()
)
m013FrxVcStatsTx8025Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTx8025Frames.setStatus("mandatory")
_M013FrxVcStatsRx8025Octets_Type = Counter32
_M013FrxVcStatsRx8025Octets_Object = MibTableColumn
m013FrxVcStatsRx8025Octets = _M013FrxVcStatsRx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 22),
    _M013FrxVcStatsRx8025Octets_Type()
)
m013FrxVcStatsRx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRx8025Octets.setStatus("mandatory")
_M013FrxVcStatsRx8025Frames_Type = Counter32
_M013FrxVcStatsRx8025Frames_Object = MibTableColumn
m013FrxVcStatsRx8025Frames = _M013FrxVcStatsRx8025Frames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 23),
    _M013FrxVcStatsRx8025Frames_Type()
)
m013FrxVcStatsRx8025Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRx8025Frames.setStatus("mandatory")
_M013FrxVcStatsTxFDDIOctets_Type = Counter32
_M013FrxVcStatsTxFDDIOctets_Object = MibTableColumn
m013FrxVcStatsTxFDDIOctets = _M013FrxVcStatsTxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 24),
    _M013FrxVcStatsTxFDDIOctets_Type()
)
m013FrxVcStatsTxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxFDDIOctets.setStatus("mandatory")
_M013FrxVcStatsTxFDDIFrames_Type = Counter32
_M013FrxVcStatsTxFDDIFrames_Object = MibTableColumn
m013FrxVcStatsTxFDDIFrames = _M013FrxVcStatsTxFDDIFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 25),
    _M013FrxVcStatsTxFDDIFrames_Type()
)
m013FrxVcStatsTxFDDIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsTxFDDIFrames.setStatus("mandatory")
_M013FrxVcStatsRxFDDIOctets_Type = Counter32
_M013FrxVcStatsRxFDDIOctets_Object = MibTableColumn
m013FrxVcStatsRxFDDIOctets = _M013FrxVcStatsRxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 26),
    _M013FrxVcStatsRxFDDIOctets_Type()
)
m013FrxVcStatsRxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxFDDIOctets.setStatus("mandatory")
_M013FrxVcStatsRxFDDIFrames_Type = Counter32
_M013FrxVcStatsRxFDDIFrames_Object = MibTableColumn
m013FrxVcStatsRxFDDIFrames = _M013FrxVcStatsRxFDDIFrames_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 5, 1, 1, 27),
    _M013FrxVcStatsRxFDDIFrames_Type()
)
m013FrxVcStatsRxFDDIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013FrxVcStatsRxFDDIFrames.setStatus("mandatory")
_M013PppxConfigGroup_ObjectIdentity = ObjectIdentity
m013PppxConfigGroup = _M013PppxConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6)
)
_M013PppxConfigTable_Object = MibTable
m013PppxConfigTable = _M013PppxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1)
)
if mibBuilder.loadTexts:
    m013PppxConfigTable.setStatus("mandatory")
_M013PppxConfigEntry_Object = MibTableRow
m013PppxConfigEntry = _M013PppxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1)
)
m013PppxConfigEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013PppxConfigSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013PppxConfigPortIndex"),
)
if mibBuilder.loadTexts:
    m013PppxConfigEntry.setStatus("mandatory")


class _M013PppxConfigSlotIndex_Type(Integer32):
    """Custom type m013PppxConfigSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013PppxConfigSlotIndex_Type.__name__ = "Integer32"
_M013PppxConfigSlotIndex_Object = MibTableColumn
m013PppxConfigSlotIndex = _M013PppxConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 1),
    _M013PppxConfigSlotIndex_Type()
)
m013PppxConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxConfigSlotIndex.setStatus("mandatory")


class _M013PppxConfigPortIndex_Type(Integer32):
    """Custom type m013PppxConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013PppxConfigPortIndex_Type.__name__ = "Integer32"
_M013PppxConfigPortIndex_Object = MibTableColumn
m013PppxConfigPortIndex = _M013PppxConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 2),
    _M013PppxConfigPortIndex_Type()
)
m013PppxConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxConfigPortIndex.setStatus("mandatory")


class _M013PppxConfigDescription_Type(DisplayString):
    """Custom type m013PppxConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013PppxConfigDescription_Type.__name__ = "DisplayString"
_M013PppxConfigDescription_Object = MibTableColumn
m013PppxConfigDescription = _M013PppxConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 3),
    _M013PppxConfigDescription_Type()
)
m013PppxConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigDescription.setStatus("mandatory")


class _M013PppxConfigAdminStatus_Type(Integer32):
    """Custom type m013PppxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_M013PppxConfigAdminStatus_Type.__name__ = "Integer32"
_M013PppxConfigAdminStatus_Object = MibTableColumn
m013PppxConfigAdminStatus = _M013PppxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 4),
    _M013PppxConfigAdminStatus_Type()
)
m013PppxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigAdminStatus.setStatus("mandatory")


class _M013PppxConfigMode_Type(Integer32):
    """Custom type m013PppxConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multilink", 2),
          ("normal", 1))
    )


_M013PppxConfigMode_Type.__name__ = "Integer32"
_M013PppxConfigMode_Object = MibTableColumn
m013PppxConfigMode = _M013PppxConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 5),
    _M013PppxConfigMode_Type()
)
m013PppxConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigMode.setStatus("mandatory")


class _M013PppxConfigIpConfigAdminStatus_Type(Integer32):
    """Custom type m013PppxConfigIpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_M013PppxConfigIpConfigAdminStatus_Type.__name__ = "Integer32"
_M013PppxConfigIpConfigAdminStatus_Object = MibTableColumn
m013PppxConfigIpConfigAdminStatus = _M013PppxConfigIpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 6),
    _M013PppxConfigIpConfigAdminStatus_Type()
)
m013PppxConfigIpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigIpConfigAdminStatus.setStatus("mandatory")


class _M013PppxConfigBcpConfigAdminStatus_Type(Integer32):
    """Custom type m013PppxConfigBcpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_M013PppxConfigBcpConfigAdminStatus_Type.__name__ = "Integer32"
_M013PppxConfigBcpConfigAdminStatus_Object = MibTableColumn
m013PppxConfigBcpConfigAdminStatus = _M013PppxConfigBcpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 7),
    _M013PppxConfigBcpConfigAdminStatus_Type()
)
m013PppxConfigBcpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigBcpConfigAdminStatus.setStatus("mandatory")


class _M013PppxConfigIpxConfigAdminStatus_Type(Integer32):
    """Custom type m013PppxConfigIpxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_M013PppxConfigIpxConfigAdminStatus_Type.__name__ = "Integer32"
_M013PppxConfigIpxConfigAdminStatus_Object = MibTableColumn
m013PppxConfigIpxConfigAdminStatus = _M013PppxConfigIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 8),
    _M013PppxConfigIpxConfigAdminStatus_Type()
)
m013PppxConfigIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigIpxConfigAdminStatus.setStatus("mandatory")
_M013PppxConfigRemoteIpAddress_Type = IpAddress
_M013PppxConfigRemoteIpAddress_Object = MibTableColumn
m013PppxConfigRemoteIpAddress = _M013PppxConfigRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 9),
    _M013PppxConfigRemoteIpAddress_Type()
)
m013PppxConfigRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigRemoteIpAddress.setStatus("mandatory")


class _M013PppxConfigAuthenticationType_Type(Integer32):
    """Custom type m013PppxConfigAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("none", 1),
          ("pap", 2))
    )


_M013PppxConfigAuthenticationType_Type.__name__ = "Integer32"
_M013PppxConfigAuthenticationType_Object = MibTableColumn
m013PppxConfigAuthenticationType = _M013PppxConfigAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 10),
    _M013PppxConfigAuthenticationType_Type()
)
m013PppxConfigAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigAuthenticationType.setStatus("mandatory")


class _M013PppxConfigUserIdToRemote_Type(DisplayString):
    """Custom type m013PppxConfigUserIdToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013PppxConfigUserIdToRemote_Type.__name__ = "DisplayString"
_M013PppxConfigUserIdToRemote_Object = MibTableColumn
m013PppxConfigUserIdToRemote = _M013PppxConfigUserIdToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 11),
    _M013PppxConfigUserIdToRemote_Type()
)
m013PppxConfigUserIdToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigUserIdToRemote.setStatus("mandatory")


class _M013PppxConfigPasswordToRemote_Type(DisplayString):
    """Custom type m013PppxConfigPasswordToRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013PppxConfigPasswordToRemote_Type.__name__ = "DisplayString"
_M013PppxConfigPasswordToRemote_Object = MibTableColumn
m013PppxConfigPasswordToRemote = _M013PppxConfigPasswordToRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 12),
    _M013PppxConfigPasswordToRemote_Type()
)
m013PppxConfigPasswordToRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigPasswordToRemote.setStatus("mandatory")


class _M013PppxConfigUserIdFromRemote_Type(DisplayString):
    """Custom type m013PppxConfigUserIdFromRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013PppxConfigUserIdFromRemote_Type.__name__ = "DisplayString"
_M013PppxConfigUserIdFromRemote_Object = MibTableColumn
m013PppxConfigUserIdFromRemote = _M013PppxConfigUserIdFromRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 13),
    _M013PppxConfigUserIdFromRemote_Type()
)
m013PppxConfigUserIdFromRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigUserIdFromRemote.setStatus("mandatory")


class _M013PppxConfigPasswordFromRemote_Type(DisplayString):
    """Custom type m013PppxConfigPasswordFromRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013PppxConfigPasswordFromRemote_Type.__name__ = "DisplayString"
_M013PppxConfigPasswordFromRemote_Object = MibTableColumn
m013PppxConfigPasswordFromRemote = _M013PppxConfigPasswordFromRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 14),
    _M013PppxConfigPasswordFromRemote_Type()
)
m013PppxConfigPasswordFromRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigPasswordFromRemote.setStatus("mandatory")


class _M013PppxConfigMaxFailureCount_Type(Integer32):
    """Custom type m013PppxConfigMaxFailureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013PppxConfigMaxFailureCount_Type.__name__ = "Integer32"
_M013PppxConfigMaxFailureCount_Object = MibTableColumn
m013PppxConfigMaxFailureCount = _M013PppxConfigMaxFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 15),
    _M013PppxConfigMaxFailureCount_Type()
)
m013PppxConfigMaxFailureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigMaxFailureCount.setStatus("mandatory")


class _M013PppxConfigMaxConfigureCount_Type(Integer32):
    """Custom type m013PppxConfigMaxConfigureCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013PppxConfigMaxConfigureCount_Type.__name__ = "Integer32"
_M013PppxConfigMaxConfigureCount_Object = MibTableColumn
m013PppxConfigMaxConfigureCount = _M013PppxConfigMaxConfigureCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 16),
    _M013PppxConfigMaxConfigureCount_Type()
)
m013PppxConfigMaxConfigureCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigMaxConfigureCount.setStatus("mandatory")


class _M013PppxConfigMaxTerminateCount_Type(Integer32):
    """Custom type m013PppxConfigMaxTerminateCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013PppxConfigMaxTerminateCount_Type.__name__ = "Integer32"
_M013PppxConfigMaxTerminateCount_Object = MibTableColumn
m013PppxConfigMaxTerminateCount = _M013PppxConfigMaxTerminateCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 17),
    _M013PppxConfigMaxTerminateCount_Type()
)
m013PppxConfigMaxTerminateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigMaxTerminateCount.setStatus("mandatory")


class _M013PppxConfigRetryTimeout_Type(Integer32):
    """Custom type m013PppxConfigRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013PppxConfigRetryTimeout_Type.__name__ = "Integer32"
_M013PppxConfigRetryTimeout_Object = MibTableColumn
m013PppxConfigRetryTimeout = _M013PppxConfigRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 6, 1, 1, 18),
    _M013PppxConfigRetryTimeout_Type()
)
m013PppxConfigRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013PppxConfigRetryTimeout.setStatus("mandatory")
_M013PppxCpGroup_ObjectIdentity = ObjectIdentity
m013PppxCpGroup = _M013PppxCpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7)
)
_M013PppxCpTable_Object = MibTable
m013PppxCpTable = _M013PppxCpTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1)
)
if mibBuilder.loadTexts:
    m013PppxCpTable.setStatus("mandatory")
_M013PppxCpEntry_Object = MibTableRow
m013PppxCpEntry = _M013PppxCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1)
)
m013PppxCpEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013PppxCpSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013PppxCpPortIndex"),
)
if mibBuilder.loadTexts:
    m013PppxCpEntry.setStatus("mandatory")


class _M013PppxCpSlotIndex_Type(Integer32):
    """Custom type m013PppxCpSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_M013PppxCpSlotIndex_Type.__name__ = "Integer32"
_M013PppxCpSlotIndex_Object = MibTableColumn
m013PppxCpSlotIndex = _M013PppxCpSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 1),
    _M013PppxCpSlotIndex_Type()
)
m013PppxCpSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpSlotIndex.setStatus("mandatory")


class _M013PppxCpPortIndex_Type(Integer32):
    """Custom type m013PppxCpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013PppxCpPortIndex_Type.__name__ = "Integer32"
_M013PppxCpPortIndex_Object = MibTableColumn
m013PppxCpPortIndex = _M013PppxCpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 2),
    _M013PppxCpPortIndex_Type()
)
m013PppxCpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpPortIndex.setStatus("mandatory")


class _M013PppxCpIpOperStatus_Type(Integer32):
    """Custom type m013PppxCpIpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_M013PppxCpIpOperStatus_Type.__name__ = "Integer32"
_M013PppxCpIpOperStatus_Object = MibTableColumn
m013PppxCpIpOperStatus = _M013PppxCpIpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 3),
    _M013PppxCpIpOperStatus_Type()
)
m013PppxCpIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpIpOperStatus.setStatus("mandatory")


class _M013PppxCpIpxOperStatus_Type(Integer32):
    """Custom type m013PppxCpIpxOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_M013PppxCpIpxOperStatus_Type.__name__ = "Integer32"
_M013PppxCpIpxOperStatus_Object = MibTableColumn
m013PppxCpIpxOperStatus = _M013PppxCpIpxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 4),
    _M013PppxCpIpxOperStatus_Type()
)
m013PppxCpIpxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpIpxOperStatus.setStatus("mandatory")


class _M013PppxCpBcpOperStatus_Type(Integer32):
    """Custom type m013PppxCpBcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_M013PppxCpBcpOperStatus_Type.__name__ = "Integer32"
_M013PppxCpBcpOperStatus_Object = MibTableColumn
m013PppxCpBcpOperStatus = _M013PppxCpBcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 5),
    _M013PppxCpBcpOperStatus_Type()
)
m013PppxCpBcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpBcpOperStatus.setStatus("mandatory")
_M013PppxCpTxLcpPackets_Type = Counter32
_M013PppxCpTxLcpPackets_Object = MibTableColumn
m013PppxCpTxLcpPackets = _M013PppxCpTxLcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 6),
    _M013PppxCpTxLcpPackets_Type()
)
m013PppxCpTxLcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpTxLcpPackets.setStatus("mandatory")
_M013PppxCpRxLcpPackets_Type = Counter32
_M013PppxCpRxLcpPackets_Object = MibTableColumn
m013PppxCpRxLcpPackets = _M013PppxCpRxLcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 7),
    _M013PppxCpRxLcpPackets_Type()
)
m013PppxCpRxLcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpRxLcpPackets.setStatus("mandatory")
_M013PppxCpTxIpcpPackets_Type = Counter32
_M013PppxCpTxIpcpPackets_Object = MibTableColumn
m013PppxCpTxIpcpPackets = _M013PppxCpTxIpcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 8),
    _M013PppxCpTxIpcpPackets_Type()
)
m013PppxCpTxIpcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpTxIpcpPackets.setStatus("mandatory")
_M013PppxCpRxIpcpPackets_Type = Counter32
_M013PppxCpRxIpcpPackets_Object = MibTableColumn
m013PppxCpRxIpcpPackets = _M013PppxCpRxIpcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 9),
    _M013PppxCpRxIpcpPackets_Type()
)
m013PppxCpRxIpcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpRxIpcpPackets.setStatus("mandatory")
_M013PppxCpTxIpxcpPackets_Type = Counter32
_M013PppxCpTxIpxcpPackets_Object = MibTableColumn
m013PppxCpTxIpxcpPackets = _M013PppxCpTxIpxcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 10),
    _M013PppxCpTxIpxcpPackets_Type()
)
m013PppxCpTxIpxcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpTxIpxcpPackets.setStatus("mandatory")
_M013PppxCpRxIpxcpPackets_Type = Counter32
_M013PppxCpRxIpxcpPackets_Object = MibTableColumn
m013PppxCpRxIpxcpPackets = _M013PppxCpRxIpxcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 11),
    _M013PppxCpRxIpxcpPackets_Type()
)
m013PppxCpRxIpxcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpRxIpxcpPackets.setStatus("mandatory")
_M013PppxCpTxBcpPackets_Type = Counter32
_M013PppxCpTxBcpPackets_Object = MibTableColumn
m013PppxCpTxBcpPackets = _M013PppxCpTxBcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 12),
    _M013PppxCpTxBcpPackets_Type()
)
m013PppxCpTxBcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpTxBcpPackets.setStatus("mandatory")
_M013PppxCpRxBcpPackets_Type = Counter32
_M013PppxCpRxBcpPackets_Object = MibTableColumn
m013PppxCpRxBcpPackets = _M013PppxCpRxBcpPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 7, 1, 1, 13),
    _M013PppxCpRxBcpPackets_Type()
)
m013PppxCpRxBcpPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxCpRxBcpPackets.setStatus("mandatory")
_M013PppxStatsGroup_ObjectIdentity = ObjectIdentity
m013PppxStatsGroup = _M013PppxStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8)
)
_M013PppxStatsTable_Object = MibTable
m013PppxStatsTable = _M013PppxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1)
)
if mibBuilder.loadTexts:
    m013PppxStatsTable.setStatus("mandatory")
_M013PppxStatsEntry_Object = MibTableRow
m013PppxStatsEntry = _M013PppxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1)
)
m013PppxStatsEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013PppxStatsSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013PppxStatsPortIndex"),
)
if mibBuilder.loadTexts:
    m013PppxStatsEntry.setStatus("mandatory")


class _M013PppxStatsSlotIndex_Type(Integer32):
    """Custom type m013PppxStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_M013PppxStatsSlotIndex_Type.__name__ = "Integer32"
_M013PppxStatsSlotIndex_Object = MibTableColumn
m013PppxStatsSlotIndex = _M013PppxStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 1),
    _M013PppxStatsSlotIndex_Type()
)
m013PppxStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsSlotIndex.setStatus("mandatory")


class _M013PppxStatsPortIndex_Type(Integer32):
    """Custom type m013PppxStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013PppxStatsPortIndex_Type.__name__ = "Integer32"
_M013PppxStatsPortIndex_Object = MibTableColumn
m013PppxStatsPortIndex = _M013PppxStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 2),
    _M013PppxStatsPortIndex_Type()
)
m013PppxStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsPortIndex.setStatus("mandatory")
_M013PppxStatsTxIPOctets_Type = Counter32
_M013PppxStatsTxIPOctets_Object = MibTableColumn
m013PppxStatsTxIPOctets = _M013PppxStatsTxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 3),
    _M013PppxStatsTxIPOctets_Type()
)
m013PppxStatsTxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxIPOctets.setStatus("mandatory")
_M013PppxStatsTxIPPackets_Type = Counter32
_M013PppxStatsTxIPPackets_Object = MibTableColumn
m013PppxStatsTxIPPackets = _M013PppxStatsTxIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 4),
    _M013PppxStatsTxIPPackets_Type()
)
m013PppxStatsTxIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxIPPackets.setStatus("mandatory")
_M013PppxStatsRxIPOctets_Type = Counter32
_M013PppxStatsRxIPOctets_Object = MibTableColumn
m013PppxStatsRxIPOctets = _M013PppxStatsRxIPOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 5),
    _M013PppxStatsRxIPOctets_Type()
)
m013PppxStatsRxIPOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxIPOctets.setStatus("mandatory")
_M013PppxStatsRxIPPackets_Type = Counter32
_M013PppxStatsRxIPPackets_Object = MibTableColumn
m013PppxStatsRxIPPackets = _M013PppxStatsRxIPPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 6),
    _M013PppxStatsRxIPPackets_Type()
)
m013PppxStatsRxIPPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxIPPackets.setStatus("mandatory")
_M013PppxStatsTxIPXOctets_Type = Counter32
_M013PppxStatsTxIPXOctets_Object = MibTableColumn
m013PppxStatsTxIPXOctets = _M013PppxStatsTxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 7),
    _M013PppxStatsTxIPXOctets_Type()
)
m013PppxStatsTxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxIPXOctets.setStatus("mandatory")
_M013PppxStatsTxIPXPackets_Type = Counter32
_M013PppxStatsTxIPXPackets_Object = MibTableColumn
m013PppxStatsTxIPXPackets = _M013PppxStatsTxIPXPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 8),
    _M013PppxStatsTxIPXPackets_Type()
)
m013PppxStatsTxIPXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxIPXPackets.setStatus("mandatory")
_M013PppxStatsRxIPXOctets_Type = Counter32
_M013PppxStatsRxIPXOctets_Object = MibTableColumn
m013PppxStatsRxIPXOctets = _M013PppxStatsRxIPXOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 9),
    _M013PppxStatsRxIPXOctets_Type()
)
m013PppxStatsRxIPXOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxIPXOctets.setStatus("mandatory")
_M013PppxStatsRxIPXPackets_Type = Counter32
_M013PppxStatsRxIPXPackets_Object = MibTableColumn
m013PppxStatsRxIPXPackets = _M013PppxStatsRxIPXPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 10),
    _M013PppxStatsRxIPXPackets_Type()
)
m013PppxStatsRxIPXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxIPXPackets.setStatus("mandatory")
_M013PppxStatsTxBPDUOctets_Type = Counter32
_M013PppxStatsTxBPDUOctets_Object = MibTableColumn
m013PppxStatsTxBPDUOctets = _M013PppxStatsTxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 11),
    _M013PppxStatsTxBPDUOctets_Type()
)
m013PppxStatsTxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxBPDUOctets.setStatus("mandatory")
_M013PppxStatsTxBPDUPackets_Type = Counter32
_M013PppxStatsTxBPDUPackets_Object = MibTableColumn
m013PppxStatsTxBPDUPackets = _M013PppxStatsTxBPDUPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 12),
    _M013PppxStatsTxBPDUPackets_Type()
)
m013PppxStatsTxBPDUPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxBPDUPackets.setStatus("mandatory")
_M013PppxStatsRxBPDUOctets_Type = Counter32
_M013PppxStatsRxBPDUOctets_Object = MibTableColumn
m013PppxStatsRxBPDUOctets = _M013PppxStatsRxBPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 13),
    _M013PppxStatsRxBPDUOctets_Type()
)
m013PppxStatsRxBPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxBPDUOctets.setStatus("mandatory")
_M013PppxStatsRxBPDUPackets_Type = Counter32
_M013PppxStatsRxBPDUPackets_Object = MibTableColumn
m013PppxStatsRxBPDUPackets = _M013PppxStatsRxBPDUPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 14),
    _M013PppxStatsRxBPDUPackets_Type()
)
m013PppxStatsRxBPDUPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxBPDUPackets.setStatus("mandatory")
_M013PppxStatsTxEthernetOctets_Type = Counter32
_M013PppxStatsTxEthernetOctets_Object = MibTableColumn
m013PppxStatsTxEthernetOctets = _M013PppxStatsTxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 15),
    _M013PppxStatsTxEthernetOctets_Type()
)
m013PppxStatsTxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxEthernetOctets.setStatus("mandatory")
_M013PppxStatsTxEthernetPackets_Type = Counter32
_M013PppxStatsTxEthernetPackets_Object = MibTableColumn
m013PppxStatsTxEthernetPackets = _M013PppxStatsTxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 16),
    _M013PppxStatsTxEthernetPackets_Type()
)
m013PppxStatsTxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxEthernetPackets.setStatus("mandatory")
_M013PppxStatsRxEthernetOctets_Type = Counter32
_M013PppxStatsRxEthernetOctets_Object = MibTableColumn
m013PppxStatsRxEthernetOctets = _M013PppxStatsRxEthernetOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 17),
    _M013PppxStatsRxEthernetOctets_Type()
)
m013PppxStatsRxEthernetOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxEthernetOctets.setStatus("mandatory")
_M013PppxStatsRxEthernetPackets_Type = Counter32
_M013PppxStatsRxEthernetPackets_Object = MibTableColumn
m013PppxStatsRxEthernetPackets = _M013PppxStatsRxEthernetPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 18),
    _M013PppxStatsRxEthernetPackets_Type()
)
m013PppxStatsRxEthernetPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxEthernetPackets.setStatus("mandatory")
_M013PppxStatsTx8025Octets_Type = Counter32
_M013PppxStatsTx8025Octets_Object = MibTableColumn
m013PppxStatsTx8025Octets = _M013PppxStatsTx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 19),
    _M013PppxStatsTx8025Octets_Type()
)
m013PppxStatsTx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTx8025Octets.setStatus("mandatory")
_M013PppxStatsTx8025Packets_Type = Counter32
_M013PppxStatsTx8025Packets_Object = MibTableColumn
m013PppxStatsTx8025Packets = _M013PppxStatsTx8025Packets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 20),
    _M013PppxStatsTx8025Packets_Type()
)
m013PppxStatsTx8025Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTx8025Packets.setStatus("mandatory")
_M013PppxStatsRx8025Octets_Type = Counter32
_M013PppxStatsRx8025Octets_Object = MibTableColumn
m013PppxStatsRx8025Octets = _M013PppxStatsRx8025Octets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 21),
    _M013PppxStatsRx8025Octets_Type()
)
m013PppxStatsRx8025Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRx8025Octets.setStatus("mandatory")
_M013PppxStatsRx8025Packets_Type = Counter32
_M013PppxStatsRx8025Packets_Object = MibTableColumn
m013PppxStatsRx8025Packets = _M013PppxStatsRx8025Packets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 22),
    _M013PppxStatsRx8025Packets_Type()
)
m013PppxStatsRx8025Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRx8025Packets.setStatus("mandatory")
_M013PppxStatsTxFDDIOctets_Type = Counter32
_M013PppxStatsTxFDDIOctets_Object = MibTableColumn
m013PppxStatsTxFDDIOctets = _M013PppxStatsTxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 23),
    _M013PppxStatsTxFDDIOctets_Type()
)
m013PppxStatsTxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxFDDIOctets.setStatus("mandatory")
_M013PppxStatsTxFDDIPackets_Type = Counter32
_M013PppxStatsTxFDDIPackets_Object = MibTableColumn
m013PppxStatsTxFDDIPackets = _M013PppxStatsTxFDDIPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 24),
    _M013PppxStatsTxFDDIPackets_Type()
)
m013PppxStatsTxFDDIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsTxFDDIPackets.setStatus("mandatory")
_M013PppxStatsRxFDDIOctets_Type = Counter32
_M013PppxStatsRxFDDIOctets_Object = MibTableColumn
m013PppxStatsRxFDDIOctets = _M013PppxStatsRxFDDIOctets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 25),
    _M013PppxStatsRxFDDIOctets_Type()
)
m013PppxStatsRxFDDIOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxFDDIOctets.setStatus("mandatory")
_M013PppxStatsRxFDDIPackets_Type = Counter32
_M013PppxStatsRxFDDIPackets_Object = MibTableColumn
m013PppxStatsRxFDDIPackets = _M013PppxStatsRxFDDIPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 8, 1, 1, 26),
    _M013PppxStatsRxFDDIPackets_Type()
)
m013PppxStatsRxFDDIPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013PppxStatsRxFDDIPackets.setStatus("mandatory")
_M013IPRouterGroup_ObjectIdentity = ObjectIdentity
m013IPRouterGroup = _M013IPRouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9)
)
_M013IPRouterIfTable_Object = MibTable
m013IPRouterIfTable = _M013IPRouterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1)
)
if mibBuilder.loadTexts:
    m013IPRouterIfTable.setStatus("mandatory")
_M013IPRouterIfEntry_Object = MibTableRow
m013IPRouterIfEntry = _M013IPRouterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1)
)
m013IPRouterIfEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013IPRouterIfSlotIndex"),
    (0, "XYLAN-M013-MIB", "m013IPRouterIfLogicalPortIndex"),
    (0, "XYLAN-M013-MIB", "m013IPRouterIfAddress"),
)
if mibBuilder.loadTexts:
    m013IPRouterIfEntry.setStatus("mandatory")


class _M013IPRouterIfSlotIndex_Type(Integer32):
    """Custom type m013IPRouterIfSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_M013IPRouterIfSlotIndex_Type.__name__ = "Integer32"
_M013IPRouterIfSlotIndex_Object = MibTableColumn
m013IPRouterIfSlotIndex = _M013IPRouterIfSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 1),
    _M013IPRouterIfSlotIndex_Type()
)
m013IPRouterIfSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013IPRouterIfSlotIndex.setStatus("mandatory")


class _M013IPRouterIfLogicalPortIndex_Type(Integer32):
    """Custom type m013IPRouterIfLogicalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_M013IPRouterIfLogicalPortIndex_Type.__name__ = "Integer32"
_M013IPRouterIfLogicalPortIndex_Object = MibTableColumn
m013IPRouterIfLogicalPortIndex = _M013IPRouterIfLogicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 2),
    _M013IPRouterIfLogicalPortIndex_Type()
)
m013IPRouterIfLogicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013IPRouterIfLogicalPortIndex.setStatus("mandatory")
_M013IPRouterIfAddress_Type = IpAddress
_M013IPRouterIfAddress_Object = MibTableColumn
m013IPRouterIfAddress = _M013IPRouterIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 3),
    _M013IPRouterIfAddress_Type()
)
m013IPRouterIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013IPRouterIfAddress.setStatus("mandatory")
_M013IPRouterIfSubNetMask_Type = IpAddress
_M013IPRouterIfSubNetMask_Object = MibTableColumn
m013IPRouterIfSubNetMask = _M013IPRouterIfSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 4),
    _M013IPRouterIfSubNetMask_Type()
)
m013IPRouterIfSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfSubNetMask.setStatus("mandatory")
_M013IPRouterIfBcastAddress_Type = IpAddress
_M013IPRouterIfBcastAddress_Object = MibTableColumn
m013IPRouterIfBcastAddress = _M013IPRouterIfBcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 5),
    _M013IPRouterIfBcastAddress_Type()
)
m013IPRouterIfBcastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfBcastAddress.setStatus("mandatory")


class _M013IPRouterIfDescription_Type(DisplayString):
    """Custom type m013IPRouterIfDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_M013IPRouterIfDescription_Type.__name__ = "DisplayString"
_M013IPRouterIfDescription_Object = MibTableColumn
m013IPRouterIfDescription = _M013IPRouterIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 6),
    _M013IPRouterIfDescription_Type()
)
m013IPRouterIfDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfDescription.setStatus("optional")


class _M013IPRouterIfAdmStatus_Type(Integer32):
    """Custom type m013IPRouterIfAdmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_M013IPRouterIfAdmStatus_Type.__name__ = "Integer32"
_M013IPRouterIfAdmStatus_Object = MibTableColumn
m013IPRouterIfAdmStatus = _M013IPRouterIfAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 7),
    _M013IPRouterIfAdmStatus_Type()
)
m013IPRouterIfAdmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfAdmStatus.setStatus("mandatory")


class _M013IPRouterIfOperStatus_Type(Integer32):
    """Custom type m013IPRouterIfOperStatus based on Integer32"""
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


_M013IPRouterIfOperStatus_Type.__name__ = "Integer32"
_M013IPRouterIfOperStatus_Object = MibTableColumn
m013IPRouterIfOperStatus = _M013IPRouterIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 8),
    _M013IPRouterIfOperStatus_Type()
)
m013IPRouterIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013IPRouterIfOperStatus.setStatus("mandatory")


class _M013IPRouterIfFramingType_Type(Integer32):
    """Custom type m013IPRouterIfFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("snap", 2))
    )


_M013IPRouterIfFramingType_Type.__name__ = "Integer32"
_M013IPRouterIfFramingType_Object = MibTableColumn
m013IPRouterIfFramingType = _M013IPRouterIfFramingType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 9),
    _M013IPRouterIfFramingType_Type()
)
m013IPRouterIfFramingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfFramingType.setStatus("mandatory")
_M013IPRouterIfMtu_Type = Integer32
_M013IPRouterIfMtu_Object = MibTableColumn
m013IPRouterIfMtu = _M013IPRouterIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 10),
    _M013IPRouterIfMtu_Type()
)
m013IPRouterIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfMtu.setStatus("mandatory")


class _M013IPRouterIfProtocol_Type(OctetString):
    """Custom type m013IPRouterIfProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_M013IPRouterIfProtocol_Type.__name__ = "OctetString"
_M013IPRouterIfProtocol_Object = MibTableColumn
m013IPRouterIfProtocol = _M013IPRouterIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 9, 1, 1, 11),
    _M013IPRouterIfProtocol_Type()
)
m013IPRouterIfProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013IPRouterIfProtocol.setStatus("mandatory")
_M013Dsx3Group_ObjectIdentity = ObjectIdentity
m013Dsx3Group = _M013Dsx3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10)
)
_M013Dsx3ConfigTable_Object = MibTable
m013Dsx3ConfigTable = _M013Dsx3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1)
)
if mibBuilder.loadTexts:
    m013Dsx3ConfigTable.setStatus("mandatory")
_M013Dsx3ConfigEntry_Object = MibTableRow
m013Dsx3ConfigEntry = _M013Dsx3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1)
)
m013Dsx3ConfigEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013Dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    m013Dsx3ConfigEntry.setStatus("mandatory")


class _M013Dsx3LineIndex_Type(Integer32):
    """Custom type m013Dsx3LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013Dsx3LineIndex_Type.__name__ = "Integer32"
_M013Dsx3LineIndex_Object = MibTableColumn
m013Dsx3LineIndex = _M013Dsx3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 1),
    _M013Dsx3LineIndex_Type()
)
m013Dsx3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3LineIndex.setStatus("mandatory")


class _M013Dsx3ChannelizedMode_Type(Integer32):
    """Custom type m013Dsx3ChannelizedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3ChannelizedMode_Type.__name__ = "Integer32"
_M013Dsx3ChannelizedMode_Object = MibTableColumn
m013Dsx3ChannelizedMode = _M013Dsx3ChannelizedMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 2),
    _M013Dsx3ChannelizedMode_Type()
)
m013Dsx3ChannelizedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3ChannelizedMode.setStatus("mandatory")


class _M013Dsx3MdlEIC_Type(OctetString):
    """Custom type m013Dsx3MdlEIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_M013Dsx3MdlEIC_Type.__name__ = "OctetString"
_M013Dsx3MdlEIC_Object = MibTableColumn
m013Dsx3MdlEIC = _M013Dsx3MdlEIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 3),
    _M013Dsx3MdlEIC_Type()
)
m013Dsx3MdlEIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlEIC.setStatus("mandatory")


class _M013Dsx3MdlLIC_Type(OctetString):
    """Custom type m013Dsx3MdlLIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_M013Dsx3MdlLIC_Type.__name__ = "OctetString"
_M013Dsx3MdlLIC_Object = MibTableColumn
m013Dsx3MdlLIC = _M013Dsx3MdlLIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 4),
    _M013Dsx3MdlLIC_Type()
)
m013Dsx3MdlLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlLIC.setStatus("mandatory")


class _M013Dsx3MdlFIC_Type(OctetString):
    """Custom type m013Dsx3MdlFIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_M013Dsx3MdlFIC_Type.__name__ = "OctetString"
_M013Dsx3MdlFIC_Object = MibTableColumn
m013Dsx3MdlFIC = _M013Dsx3MdlFIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 5),
    _M013Dsx3MdlFIC_Type()
)
m013Dsx3MdlFIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlFIC.setStatus("mandatory")


class _M013Dsx3MdlUNIT_Type(OctetString):
    """Custom type m013Dsx3MdlUNIT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_M013Dsx3MdlUNIT_Type.__name__ = "OctetString"
_M013Dsx3MdlUNIT_Object = MibTableColumn
m013Dsx3MdlUNIT = _M013Dsx3MdlUNIT_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 6),
    _M013Dsx3MdlUNIT_Type()
)
m013Dsx3MdlUNIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlUNIT.setStatus("mandatory")


class _M013Dsx3MdlPFI_Type(OctetString):
    """Custom type m013Dsx3MdlPFI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3MdlPFI_Type.__name__ = "OctetString"
_M013Dsx3MdlPFI_Object = MibTableColumn
m013Dsx3MdlPFI = _M013Dsx3MdlPFI_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 7),
    _M013Dsx3MdlPFI_Type()
)
m013Dsx3MdlPFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlPFI.setStatus("mandatory")


class _M013Dsx3MdlPortIdleSignalCode_Type(OctetString):
    """Custom type m013Dsx3MdlPortIdleSignalCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3MdlPortIdleSignalCode_Type.__name__ = "OctetString"
_M013Dsx3MdlPortIdleSignalCode_Object = MibTableColumn
m013Dsx3MdlPortIdleSignalCode = _M013Dsx3MdlPortIdleSignalCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 8),
    _M013Dsx3MdlPortIdleSignalCode_Type()
)
m013Dsx3MdlPortIdleSignalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlPortIdleSignalCode.setStatus("mandatory")


class _M013Dsx3MdlGenerator_Type(OctetString):
    """Custom type m013Dsx3MdlGenerator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3MdlGenerator_Type.__name__ = "OctetString"
_M013Dsx3MdlGenerator_Object = MibTableColumn
m013Dsx3MdlGenerator = _M013Dsx3MdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 9),
    _M013Dsx3MdlGenerator_Type()
)
m013Dsx3MdlGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlGenerator.setStatus("mandatory")


class _M013Dsx3MdlTransmitPath_Type(Integer32):
    """Custom type m013Dsx3MdlTransmitPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3MdlTransmitPath_Type.__name__ = "Integer32"
_M013Dsx3MdlTransmitPath_Object = MibTableColumn
m013Dsx3MdlTransmitPath = _M013Dsx3MdlTransmitPath_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 10),
    _M013Dsx3MdlTransmitPath_Type()
)
m013Dsx3MdlTransmitPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlTransmitPath.setStatus("mandatory")


class _M013Dsx3MdlTransmitIdleSignal_Type(Integer32):
    """Custom type m013Dsx3MdlTransmitIdleSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3MdlTransmitIdleSignal_Type.__name__ = "Integer32"
_M013Dsx3MdlTransmitIdleSignal_Object = MibTableColumn
m013Dsx3MdlTransmitIdleSignal = _M013Dsx3MdlTransmitIdleSignal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 11),
    _M013Dsx3MdlTransmitIdleSignal_Type()
)
m013Dsx3MdlTransmitIdleSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlTransmitIdleSignal.setStatus("mandatory")


class _M013Dsx3MdlTransmitTestSignal_Type(Integer32):
    """Custom type m013Dsx3MdlTransmitTestSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3MdlTransmitTestSignal_Type.__name__ = "Integer32"
_M013Dsx3MdlTransmitTestSignal_Object = MibTableColumn
m013Dsx3MdlTransmitTestSignal = _M013Dsx3MdlTransmitTestSignal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 12),
    _M013Dsx3MdlTransmitTestSignal_Type()
)
m013Dsx3MdlTransmitTestSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3MdlTransmitTestSignal.setStatus("mandatory")


class _M013Dsx3FEACEnable_Type(Integer32):
    """Custom type m013Dsx3FEACEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3FEACEnable_Type.__name__ = "Integer32"
_M013Dsx3FEACEnable_Object = MibTableColumn
m013Dsx3FEACEnable = _M013Dsx3FEACEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 13),
    _M013Dsx3FEACEnable_Type()
)
m013Dsx3FEACEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3FEACEnable.setStatus("mandatory")


class _M013Dsx3REIEnable_Type(Integer32):
    """Custom type m013Dsx3REIEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3REIEnable_Type.__name__ = "Integer32"
_M013Dsx3REIEnable_Object = MibTableColumn
m013Dsx3REIEnable = _M013Dsx3REIEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 14),
    _M013Dsx3REIEnable_Type()
)
m013Dsx3REIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3REIEnable.setStatus("mandatory")


class _M013Dsx3RxMdlEnable_Type(Integer32):
    """Custom type m013Dsx3RxMdlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx3RxMdlEnable_Type.__name__ = "Integer32"
_M013Dsx3RxMdlEnable_Object = MibTableColumn
m013Dsx3RxMdlEnable = _M013Dsx3RxMdlEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 15),
    _M013Dsx3RxMdlEnable_Type()
)
m013Dsx3RxMdlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlEnable.setStatus("mandatory")


class _M013Dsx3RxMdlEIC_Type(OctetString):
    """Custom type m013Dsx3RxMdlEIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_M013Dsx3RxMdlEIC_Type.__name__ = "OctetString"
_M013Dsx3RxMdlEIC_Object = MibTableColumn
m013Dsx3RxMdlEIC = _M013Dsx3RxMdlEIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 16),
    _M013Dsx3RxMdlEIC_Type()
)
m013Dsx3RxMdlEIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlEIC.setStatus("mandatory")


class _M013Dsx3RxMdlLIC_Type(OctetString):
    """Custom type m013Dsx3RxMdlLIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_M013Dsx3RxMdlLIC_Type.__name__ = "OctetString"
_M013Dsx3RxMdlLIC_Object = MibTableColumn
m013Dsx3RxMdlLIC = _M013Dsx3RxMdlLIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 17),
    _M013Dsx3RxMdlLIC_Type()
)
m013Dsx3RxMdlLIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlLIC.setStatus("mandatory")


class _M013Dsx3RxMdlFIC_Type(OctetString):
    """Custom type m013Dsx3RxMdlFIC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_M013Dsx3RxMdlFIC_Type.__name__ = "OctetString"
_M013Dsx3RxMdlFIC_Object = MibTableColumn
m013Dsx3RxMdlFIC = _M013Dsx3RxMdlFIC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 18),
    _M013Dsx3RxMdlFIC_Type()
)
m013Dsx3RxMdlFIC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlFIC.setStatus("mandatory")


class _M013Dsx3RxMdlUNIT_Type(OctetString):
    """Custom type m013Dsx3RxMdlUNIT based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_M013Dsx3RxMdlUNIT_Type.__name__ = "OctetString"
_M013Dsx3RxMdlUNIT_Object = MibTableColumn
m013Dsx3RxMdlUNIT = _M013Dsx3RxMdlUNIT_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 19),
    _M013Dsx3RxMdlUNIT_Type()
)
m013Dsx3RxMdlUNIT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlUNIT.setStatus("mandatory")


class _M013Dsx3RxMdlPFI_Type(OctetString):
    """Custom type m013Dsx3RxMdlPFI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3RxMdlPFI_Type.__name__ = "OctetString"
_M013Dsx3RxMdlPFI_Object = MibTableColumn
m013Dsx3RxMdlPFI = _M013Dsx3RxMdlPFI_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 20),
    _M013Dsx3RxMdlPFI_Type()
)
m013Dsx3RxMdlPFI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlPFI.setStatus("mandatory")


class _M013Dsx3RxMdlPortIdleSignalCode_Type(OctetString):
    """Custom type m013Dsx3RxMdlPortIdleSignalCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3RxMdlPortIdleSignalCode_Type.__name__ = "OctetString"
_M013Dsx3RxMdlPortIdleSignalCode_Object = MibTableColumn
m013Dsx3RxMdlPortIdleSignalCode = _M013Dsx3RxMdlPortIdleSignalCode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 21),
    _M013Dsx3RxMdlPortIdleSignalCode_Type()
)
m013Dsx3RxMdlPortIdleSignalCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlPortIdleSignalCode.setStatus("mandatory")


class _M013Dsx3RxMdlGenerator_Type(OctetString):
    """Custom type m013Dsx3RxMdlGenerator based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 38),
    )


_M013Dsx3RxMdlGenerator_Type.__name__ = "OctetString"
_M013Dsx3RxMdlGenerator_Object = MibTableColumn
m013Dsx3RxMdlGenerator = _M013Dsx3RxMdlGenerator_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 22),
    _M013Dsx3RxMdlGenerator_Type()
)
m013Dsx3RxMdlGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3RxMdlGenerator.setStatus("mandatory")


class _M013Dsx3RemoteStatus_Type(Integer32):
    """Custom type m013Dsx3RemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_M013Dsx3RemoteStatus_Type.__name__ = "Integer32"
_M013Dsx3RemoteStatus_Object = MibTableColumn
m013Dsx3RemoteStatus = _M013Dsx3RemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 23),
    _M013Dsx3RemoteStatus_Type()
)
m013Dsx3RemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3RemoteStatus.setStatus("mandatory")
_M013Dsx3RemoteStatusLastChange_Type = Integer32
_M013Dsx3RemoteStatusLastChange_Object = MibTableColumn
m013Dsx3RemoteStatusLastChange = _M013Dsx3RemoteStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 24),
    _M013Dsx3RemoteStatusLastChange_Type()
)
m013Dsx3RemoteStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3RemoteStatusLastChange.setStatus("mandatory")
_M013Dsx3LedStatus_Type = Integer32
_M013Dsx3LedStatus_Object = MibTableColumn
m013Dsx3LedStatus = _M013Dsx3LedStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 25),
    _M013Dsx3LedStatus_Type()
)
m013Dsx3LedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3LedStatus.setStatus("mandatory")
_M013Dsx3Ds1StatsEnableMask_Type = Integer32
_M013Dsx3Ds1StatsEnableMask_Object = MibTableColumn
m013Dsx3Ds1StatsEnableMask = _M013Dsx3Ds1StatsEnableMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 1, 1, 26),
    _M013Dsx3Ds1StatsEnableMask_Type()
)
m013Dsx3Ds1StatsEnableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx3Ds1StatsEnableMask.setStatus("mandatory")
_M013Dsx3StatsTable_Object = MibTable
m013Dsx3StatsTable = _M013Dsx3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 2)
)
if mibBuilder.loadTexts:
    m013Dsx3StatsTable.setStatus("mandatory")
_M013Dsx3StatsEntry_Object = MibTableRow
m013Dsx3StatsEntry = _M013Dsx3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 2, 1)
)
m013Dsx3StatsEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013Dsx3StatsLineIndex"),
)
if mibBuilder.loadTexts:
    m013Dsx3StatsEntry.setStatus("mandatory")


class _M013Dsx3StatsLineIndex_Type(Integer32):
    """Custom type m013Dsx3StatsLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013Dsx3StatsLineIndex_Type.__name__ = "Integer32"
_M013Dsx3StatsLineIndex_Object = MibTableColumn
m013Dsx3StatsLineIndex = _M013Dsx3StatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 2, 1, 1),
    _M013Dsx3StatsLineIndex_Type()
)
m013Dsx3StatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3StatsLineIndex.setStatus("mandatory")
_M013Dsx3StatsRxREI_Type = Counter32
_M013Dsx3StatsRxREI_Object = MibTableColumn
m013Dsx3StatsRxREI = _M013Dsx3StatsRxREI_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 2, 1, 2),
    _M013Dsx3StatsRxREI_Type()
)
m013Dsx3StatsRxREI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3StatsRxREI.setStatus("mandatory")


class _M013Dsx3StatsRxFEAC_Type(Integer32):
    """Custom type m013Dsx3StatsRxFEAC based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsx3CommonEquipmentFailure", 8),
          ("dsx3DS1NonServiceAffectingEquipFailure", 11),
          ("dsx3DS1ServiceAffectingEquipmentFailure", 10),
          ("dsx3DS3AISreceived", 5),
          ("dsx3DS3EquipmentFailure", 2),
          ("dsx3DS3IDLEreceived", 6),
          ("dsx3DS3LOS", 3),
          ("dsx3DS3LoopbackReceived", 9),
          ("dsx3DS3NonServiceAffectingEquipFailure", 7),
          ("dsx3DS3OutofFrame", 4),
          ("dsx3MultipleDS1sLOS", 13),
          ("dsx3NoFEAC", 1),
          ("dsx3SingleDS1LOS", 12),
          ("dsx3UnknownCode", 14),
          ("dsx3UnsupportedCode", 15))
    )


_M013Dsx3StatsRxFEAC_Type.__name__ = "Integer32"
_M013Dsx3StatsRxFEAC_Object = MibTableColumn
m013Dsx3StatsRxFEAC = _M013Dsx3StatsRxFEAC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 10, 2, 1, 3),
    _M013Dsx3StatsRxFEAC_Type()
)
m013Dsx3StatsRxFEAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx3StatsRxFEAC.setStatus("mandatory")
_M013Dsx1Group_ObjectIdentity = ObjectIdentity
m013Dsx1Group = _M013Dsx1Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11)
)
_M013Dsx1ConfigTable_Object = MibTable
m013Dsx1ConfigTable = _M013Dsx1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1)
)
if mibBuilder.loadTexts:
    m013Dsx1ConfigTable.setStatus("mandatory")
_M013Dsx1ConfigEntry_Object = MibTableRow
m013Dsx1ConfigEntry = _M013Dsx1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1)
)
m013Dsx1ConfigEntry.setIndexNames(
    (0, "XYLAN-M013-MIB", "m013Dsx3LineIndex"),
)
if mibBuilder.loadTexts:
    m013Dsx1ConfigEntry.setStatus("mandatory")


class _M013Dsx1LineIndex_Type(Integer32):
    """Custom type m013Dsx1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_M013Dsx1LineIndex_Type.__name__ = "Integer32"
_M013Dsx1LineIndex_Object = MibTableColumn
m013Dsx1LineIndex = _M013Dsx1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 1),
    _M013Dsx1LineIndex_Type()
)
m013Dsx1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx1LineIndex.setStatus("mandatory")


class _M013Dsx1T1BertPattern_Type(Integer32):
    """Custom type m013Dsx1T1BertPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_M013Dsx1T1BertPattern_Type.__name__ = "Integer32"
_M013Dsx1T1BertPattern_Object = MibTableColumn
m013Dsx1T1BertPattern = _M013Dsx1T1BertPattern_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 2),
    _M013Dsx1T1BertPattern_Type()
)
m013Dsx1T1BertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx1T1BertPattern.setStatus("mandatory")
_M013Dsx1T1BertInterval_Type = Integer32
_M013Dsx1T1BertInterval_Object = MibTableColumn
m013Dsx1T1BertInterval = _M013Dsx1T1BertInterval_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 3),
    _M013Dsx1T1BertInterval_Type()
)
m013Dsx1T1BertInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx1T1BertInterval.setStatus("mandatory")


class _M013Dsx1T1BertFraming_Type(Integer32):
    """Custom type m013Dsx1T1BertFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noframing", 2),
          ("useframing", 1))
    )


_M013Dsx1T1BertFraming_Type.__name__ = "Integer32"
_M013Dsx1T1BertFraming_Object = MibTableColumn
m013Dsx1T1BertFraming = _M013Dsx1T1BertFraming_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 4),
    _M013Dsx1T1BertFraming_Type()
)
m013Dsx1T1BertFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx1T1BertFraming.setStatus("mandatory")


class _M013Dsx1T1BertTestEnable_Type(Integer32):
    """Custom type m013Dsx1T1BertTestEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_M013Dsx1T1BertTestEnable_Type.__name__ = "Integer32"
_M013Dsx1T1BertTestEnable_Object = MibTableColumn
m013Dsx1T1BertTestEnable = _M013Dsx1T1BertTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 5),
    _M013Dsx1T1BertTestEnable_Type()
)
m013Dsx1T1BertTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m013Dsx1T1BertTestEnable.setStatus("mandatory")


class _M013Dsx1RemoteStatus_Type(Integer32):
    """Custom type m013Dsx1RemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_M013Dsx1RemoteStatus_Type.__name__ = "Integer32"
_M013Dsx1RemoteStatus_Object = MibTableColumn
m013Dsx1RemoteStatus = _M013Dsx1RemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 6),
    _M013Dsx1RemoteStatus_Type()
)
m013Dsx1RemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx1RemoteStatus.setStatus("mandatory")
_M013Dsx1RemoteStatusLastChange_Type = Integer32
_M013Dsx1RemoteStatusLastChange_Object = MibTableColumn
m013Dsx1RemoteStatusLastChange = _M013Dsx1RemoteStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 25, 11, 1, 1, 7),
    _M013Dsx1RemoteStatusLastChange_Type()
)
m013Dsx1RemoteStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m013Dsx1RemoteStatusLastChange.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-M013-MIB",
    **{"m013ProvisioningGroup": m013ProvisioningGroup,
       "m013ProvisioningTable": m013ProvisioningTable,
       "m013ProvisioningEntry": m013ProvisioningEntry,
       "m013SlotIndex": m013SlotIndex,
       "m013LogicalPortIndex": m013LogicalPortIndex,
       "m013Description": m013Description,
       "m013Ds3PortIndex": m013Ds3PortIndex,
       "m013Ds1Fraction": m013Ds1Fraction,
       "m013Ds0Mask": m013Ds0Mask,
       "m013IfIndex": m013IfIndex,
       "m013Protocol": m013Protocol,
       "m013EntryStatus": m013EntryStatus,
       "m013ServiceGroup": m013ServiceGroup,
       "m013ServiceTable": m013ServiceTable,
       "m013ServiceEntry": m013ServiceEntry,
       "m013ServiceSlotIndex": m013ServiceSlotIndex,
       "m013ServiceLogicalPortIndex": m013ServiceLogicalPortIndex,
       "m013ServiceNumber": m013ServiceNumber,
       "m013ServiceTableEntryType": m013ServiceTableEntryType,
       "m013ServiceDescription": m013ServiceDescription,
       "m013ServiceType": m013ServiceType,
       "m013ServiceOperStatus": m013ServiceOperStatus,
       "m013ServiceAdminStatus": m013ServiceAdminStatus,
       "m013ServiceVirtualCircuit": m013ServiceVirtualCircuit,
       "m013ServiceVlans": m013ServiceVlans,
       "m013ServiceBridgingMode": m013ServiceBridgingMode,
       "m013FrxPortGroup": m013FrxPortGroup,
       "m013FrxPortTable": m013FrxPortTable,
       "m013FrxPortEntry": m013FrxPortEntry,
       "m013FrxPortSlotIndex": m013FrxPortSlotIndex,
       "m013FrxPortPortIndex": m013FrxPortPortIndex,
       "m013FrxPortDescription": m013FrxPortDescription,
       "m013FrxPortAdminStatus": m013FrxPortAdminStatus,
       "m013FrxPortDefaultIpRoutingAdminStatus": m013FrxPortDefaultIpRoutingAdminStatus,
       "m013FrxPortDefaultBridgingAdminStatus": m013FrxPortDefaultBridgingAdminStatus,
       "m013FrxPortDefaultBridgingVLAN": m013FrxPortDefaultBridgingVLAN,
       "m013FrxPortDefaultBridgingMode": m013FrxPortDefaultBridgingMode,
       "m013FrxPortDynamicVCCreation": m013FrxPortDynamicVCCreation,
       "m013FrxVcControlGroup": m013FrxVcControlGroup,
       "m013FrxVcControlTable": m013FrxVcControlTable,
       "m013FrxVcControlEntry": m013FrxVcControlEntry,
       "m013FrxVcControlSlotIndex": m013FrxVcControlSlotIndex,
       "m013FrxVcControlPortIndex": m013FrxVcControlPortIndex,
       "m013FrxVcControlDlci": m013FrxVcControlDlci,
       "m013FrxVcControlIpRoutingAdminStatus": m013FrxVcControlIpRoutingAdminStatus,
       "m013FrxVcStatsGroup": m013FrxVcStatsGroup,
       "m013FrxVcStatsTable": m013FrxVcStatsTable,
       "m013FrxVcStatsEntry": m013FrxVcStatsEntry,
       "m013FrxVcStatsSlotIndex": m013FrxVcStatsSlotIndex,
       "m013FrxVcStatsPortIndex": m013FrxVcStatsPortIndex,
       "m013FrxVcStatsDlci": m013FrxVcStatsDlci,
       "m013FrxVcStatsTxIPOctets": m013FrxVcStatsTxIPOctets,
       "m013FrxVcStatsTxIPFrames": m013FrxVcStatsTxIPFrames,
       "m013FrxVcStatsRxIPOctets": m013FrxVcStatsRxIPOctets,
       "m013FrxVcStatsRxIPFrames": m013FrxVcStatsRxIPFrames,
       "m013FrxVcStatsTxIPXOctets": m013FrxVcStatsTxIPXOctets,
       "m013FrxVcStatsTxIPXFrames": m013FrxVcStatsTxIPXFrames,
       "m013FrxVcStatsRxIPXOctets": m013FrxVcStatsRxIPXOctets,
       "m013FrxVcStatsRxIPXFrames": m013FrxVcStatsRxIPXFrames,
       "m013FrxVcStatsTxBPDUOctets": m013FrxVcStatsTxBPDUOctets,
       "m013FrxVcStatsTxBPDUFrames": m013FrxVcStatsTxBPDUFrames,
       "m013FrxVcStatsRxBPDUOctets": m013FrxVcStatsRxBPDUOctets,
       "m013FrxVcStatsRxBPDUFrames": m013FrxVcStatsRxBPDUFrames,
       "m013FrxVcStatsTxEthernetOctets": m013FrxVcStatsTxEthernetOctets,
       "m013FrxVcStatsTxEthernetFrames": m013FrxVcStatsTxEthernetFrames,
       "m013FrxVcStatsRxEthernetOctets": m013FrxVcStatsRxEthernetOctets,
       "m013FrxVcStatsRxEthernetFrames": m013FrxVcStatsRxEthernetFrames,
       "m013FrxVcStatsTx8025Octets": m013FrxVcStatsTx8025Octets,
       "m013FrxVcStatsTx8025Frames": m013FrxVcStatsTx8025Frames,
       "m013FrxVcStatsRx8025Octets": m013FrxVcStatsRx8025Octets,
       "m013FrxVcStatsRx8025Frames": m013FrxVcStatsRx8025Frames,
       "m013FrxVcStatsTxFDDIOctets": m013FrxVcStatsTxFDDIOctets,
       "m013FrxVcStatsTxFDDIFrames": m013FrxVcStatsTxFDDIFrames,
       "m013FrxVcStatsRxFDDIOctets": m013FrxVcStatsRxFDDIOctets,
       "m013FrxVcStatsRxFDDIFrames": m013FrxVcStatsRxFDDIFrames,
       "m013PppxConfigGroup": m013PppxConfigGroup,
       "m013PppxConfigTable": m013PppxConfigTable,
       "m013PppxConfigEntry": m013PppxConfigEntry,
       "m013PppxConfigSlotIndex": m013PppxConfigSlotIndex,
       "m013PppxConfigPortIndex": m013PppxConfigPortIndex,
       "m013PppxConfigDescription": m013PppxConfigDescription,
       "m013PppxConfigAdminStatus": m013PppxConfigAdminStatus,
       "m013PppxConfigMode": m013PppxConfigMode,
       "m013PppxConfigIpConfigAdminStatus": m013PppxConfigIpConfigAdminStatus,
       "m013PppxConfigBcpConfigAdminStatus": m013PppxConfigBcpConfigAdminStatus,
       "m013PppxConfigIpxConfigAdminStatus": m013PppxConfigIpxConfigAdminStatus,
       "m013PppxConfigRemoteIpAddress": m013PppxConfigRemoteIpAddress,
       "m013PppxConfigAuthenticationType": m013PppxConfigAuthenticationType,
       "m013PppxConfigUserIdToRemote": m013PppxConfigUserIdToRemote,
       "m013PppxConfigPasswordToRemote": m013PppxConfigPasswordToRemote,
       "m013PppxConfigUserIdFromRemote": m013PppxConfigUserIdFromRemote,
       "m013PppxConfigPasswordFromRemote": m013PppxConfigPasswordFromRemote,
       "m013PppxConfigMaxFailureCount": m013PppxConfigMaxFailureCount,
       "m013PppxConfigMaxConfigureCount": m013PppxConfigMaxConfigureCount,
       "m013PppxConfigMaxTerminateCount": m013PppxConfigMaxTerminateCount,
       "m013PppxConfigRetryTimeout": m013PppxConfigRetryTimeout,
       "m013PppxCpGroup": m013PppxCpGroup,
       "m013PppxCpTable": m013PppxCpTable,
       "m013PppxCpEntry": m013PppxCpEntry,
       "m013PppxCpSlotIndex": m013PppxCpSlotIndex,
       "m013PppxCpPortIndex": m013PppxCpPortIndex,
       "m013PppxCpIpOperStatus": m013PppxCpIpOperStatus,
       "m013PppxCpIpxOperStatus": m013PppxCpIpxOperStatus,
       "m013PppxCpBcpOperStatus": m013PppxCpBcpOperStatus,
       "m013PppxCpTxLcpPackets": m013PppxCpTxLcpPackets,
       "m013PppxCpRxLcpPackets": m013PppxCpRxLcpPackets,
       "m013PppxCpTxIpcpPackets": m013PppxCpTxIpcpPackets,
       "m013PppxCpRxIpcpPackets": m013PppxCpRxIpcpPackets,
       "m013PppxCpTxIpxcpPackets": m013PppxCpTxIpxcpPackets,
       "m013PppxCpRxIpxcpPackets": m013PppxCpRxIpxcpPackets,
       "m013PppxCpTxBcpPackets": m013PppxCpTxBcpPackets,
       "m013PppxCpRxBcpPackets": m013PppxCpRxBcpPackets,
       "m013PppxStatsGroup": m013PppxStatsGroup,
       "m013PppxStatsTable": m013PppxStatsTable,
       "m013PppxStatsEntry": m013PppxStatsEntry,
       "m013PppxStatsSlotIndex": m013PppxStatsSlotIndex,
       "m013PppxStatsPortIndex": m013PppxStatsPortIndex,
       "m013PppxStatsTxIPOctets": m013PppxStatsTxIPOctets,
       "m013PppxStatsTxIPPackets": m013PppxStatsTxIPPackets,
       "m013PppxStatsRxIPOctets": m013PppxStatsRxIPOctets,
       "m013PppxStatsRxIPPackets": m013PppxStatsRxIPPackets,
       "m013PppxStatsTxIPXOctets": m013PppxStatsTxIPXOctets,
       "m013PppxStatsTxIPXPackets": m013PppxStatsTxIPXPackets,
       "m013PppxStatsRxIPXOctets": m013PppxStatsRxIPXOctets,
       "m013PppxStatsRxIPXPackets": m013PppxStatsRxIPXPackets,
       "m013PppxStatsTxBPDUOctets": m013PppxStatsTxBPDUOctets,
       "m013PppxStatsTxBPDUPackets": m013PppxStatsTxBPDUPackets,
       "m013PppxStatsRxBPDUOctets": m013PppxStatsRxBPDUOctets,
       "m013PppxStatsRxBPDUPackets": m013PppxStatsRxBPDUPackets,
       "m013PppxStatsTxEthernetOctets": m013PppxStatsTxEthernetOctets,
       "m013PppxStatsTxEthernetPackets": m013PppxStatsTxEthernetPackets,
       "m013PppxStatsRxEthernetOctets": m013PppxStatsRxEthernetOctets,
       "m013PppxStatsRxEthernetPackets": m013PppxStatsRxEthernetPackets,
       "m013PppxStatsTx8025Octets": m013PppxStatsTx8025Octets,
       "m013PppxStatsTx8025Packets": m013PppxStatsTx8025Packets,
       "m013PppxStatsRx8025Octets": m013PppxStatsRx8025Octets,
       "m013PppxStatsRx8025Packets": m013PppxStatsRx8025Packets,
       "m013PppxStatsTxFDDIOctets": m013PppxStatsTxFDDIOctets,
       "m013PppxStatsTxFDDIPackets": m013PppxStatsTxFDDIPackets,
       "m013PppxStatsRxFDDIOctets": m013PppxStatsRxFDDIOctets,
       "m013PppxStatsRxFDDIPackets": m013PppxStatsRxFDDIPackets,
       "m013IPRouterGroup": m013IPRouterGroup,
       "m013IPRouterIfTable": m013IPRouterIfTable,
       "m013IPRouterIfEntry": m013IPRouterIfEntry,
       "m013IPRouterIfSlotIndex": m013IPRouterIfSlotIndex,
       "m013IPRouterIfLogicalPortIndex": m013IPRouterIfLogicalPortIndex,
       "m013IPRouterIfAddress": m013IPRouterIfAddress,
       "m013IPRouterIfSubNetMask": m013IPRouterIfSubNetMask,
       "m013IPRouterIfBcastAddress": m013IPRouterIfBcastAddress,
       "m013IPRouterIfDescription": m013IPRouterIfDescription,
       "m013IPRouterIfAdmStatus": m013IPRouterIfAdmStatus,
       "m013IPRouterIfOperStatus": m013IPRouterIfOperStatus,
       "m013IPRouterIfFramingType": m013IPRouterIfFramingType,
       "m013IPRouterIfMtu": m013IPRouterIfMtu,
       "m013IPRouterIfProtocol": m013IPRouterIfProtocol,
       "m013Dsx3Group": m013Dsx3Group,
       "m013Dsx3ConfigTable": m013Dsx3ConfigTable,
       "m013Dsx3ConfigEntry": m013Dsx3ConfigEntry,
       "m013Dsx3LineIndex": m013Dsx3LineIndex,
       "m013Dsx3ChannelizedMode": m013Dsx3ChannelizedMode,
       "m013Dsx3MdlEIC": m013Dsx3MdlEIC,
       "m013Dsx3MdlLIC": m013Dsx3MdlLIC,
       "m013Dsx3MdlFIC": m013Dsx3MdlFIC,
       "m013Dsx3MdlUNIT": m013Dsx3MdlUNIT,
       "m013Dsx3MdlPFI": m013Dsx3MdlPFI,
       "m013Dsx3MdlPortIdleSignalCode": m013Dsx3MdlPortIdleSignalCode,
       "m013Dsx3MdlGenerator": m013Dsx3MdlGenerator,
       "m013Dsx3MdlTransmitPath": m013Dsx3MdlTransmitPath,
       "m013Dsx3MdlTransmitIdleSignal": m013Dsx3MdlTransmitIdleSignal,
       "m013Dsx3MdlTransmitTestSignal": m013Dsx3MdlTransmitTestSignal,
       "m013Dsx3FEACEnable": m013Dsx3FEACEnable,
       "m013Dsx3REIEnable": m013Dsx3REIEnable,
       "m013Dsx3RxMdlEnable": m013Dsx3RxMdlEnable,
       "m013Dsx3RxMdlEIC": m013Dsx3RxMdlEIC,
       "m013Dsx3RxMdlLIC": m013Dsx3RxMdlLIC,
       "m013Dsx3RxMdlFIC": m013Dsx3RxMdlFIC,
       "m013Dsx3RxMdlUNIT": m013Dsx3RxMdlUNIT,
       "m013Dsx3RxMdlPFI": m013Dsx3RxMdlPFI,
       "m013Dsx3RxMdlPortIdleSignalCode": m013Dsx3RxMdlPortIdleSignalCode,
       "m013Dsx3RxMdlGenerator": m013Dsx3RxMdlGenerator,
       "m013Dsx3RemoteStatus": m013Dsx3RemoteStatus,
       "m013Dsx3RemoteStatusLastChange": m013Dsx3RemoteStatusLastChange,
       "m013Dsx3LedStatus": m013Dsx3LedStatus,
       "m013Dsx3Ds1StatsEnableMask": m013Dsx3Ds1StatsEnableMask,
       "m013Dsx3StatsTable": m013Dsx3StatsTable,
       "m013Dsx3StatsEntry": m013Dsx3StatsEntry,
       "m013Dsx3StatsLineIndex": m013Dsx3StatsLineIndex,
       "m013Dsx3StatsRxREI": m013Dsx3StatsRxREI,
       "m013Dsx3StatsRxFEAC": m013Dsx3StatsRxFEAC,
       "m013Dsx1Group": m013Dsx1Group,
       "m013Dsx1ConfigTable": m013Dsx1ConfigTable,
       "m013Dsx1ConfigEntry": m013Dsx1ConfigEntry,
       "m013Dsx1LineIndex": m013Dsx1LineIndex,
       "m013Dsx1T1BertPattern": m013Dsx1T1BertPattern,
       "m013Dsx1T1BertInterval": m013Dsx1T1BertInterval,
       "m013Dsx1T1BertFraming": m013Dsx1T1BertFraming,
       "m013Dsx1T1BertTestEnable": m013Dsx1T1BertTestEnable,
       "m013Dsx1RemoteStatus": m013Dsx1RemoteStatus,
       "m013Dsx1RemoteStatusLastChange": m013Dsx1RemoteStatusLastChange}
)
