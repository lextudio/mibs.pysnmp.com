# SNMP MIB module (CTRON-IF-REMAP-2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-IF-REMAP-2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:54 2024
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

(ctIFRemap2,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctIFRemap2")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtIFRemap2Config_ObjectIdentity = ObjectIdentity
ctIFRemap2Config = _CtIFRemap2Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1)
)
_CtIFRemap2Table_Object = MibTable
ctIFRemap2Table = _CtIFRemap2Table_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ctIFRemap2Table.setStatus("mandatory")
_CtIFRemap2Entry_Object = MibTableRow
ctIFRemap2Entry = _CtIFRemap2Entry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1)
)
ctIFRemap2Entry.setIndexNames(
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourceSlot"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SourcePort"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestSlot"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2DestPort"),
)
if mibBuilder.loadTexts:
    ctIFRemap2Entry.setStatus("mandatory")
_CtIFRemap2SourceSlot_Type = Integer32
_CtIFRemap2SourceSlot_Object = MibTableColumn
ctIFRemap2SourceSlot = _CtIFRemap2SourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 1),
    _CtIFRemap2SourceSlot_Type()
)
ctIFRemap2SourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2SourceSlot.setStatus("mandatory")
_CtIFRemap2SourcePort_Type = Integer32
_CtIFRemap2SourcePort_Object = MibTableColumn
ctIFRemap2SourcePort = _CtIFRemap2SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 2),
    _CtIFRemap2SourcePort_Type()
)
ctIFRemap2SourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2SourcePort.setStatus("mandatory")
_CtIFRemap2DestSlot_Type = Integer32
_CtIFRemap2DestSlot_Object = MibTableColumn
ctIFRemap2DestSlot = _CtIFRemap2DestSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 3),
    _CtIFRemap2DestSlot_Type()
)
ctIFRemap2DestSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2DestSlot.setStatus("mandatory")
_CtIFRemap2DestPort_Type = Integer32
_CtIFRemap2DestPort_Object = MibTableColumn
ctIFRemap2DestPort = _CtIFRemap2DestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 4),
    _CtIFRemap2DestPort_Type()
)
ctIFRemap2DestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2DestPort.setStatus("mandatory")


class _CtIFRemap2Status_Type(Integer32):
    """Custom type ctIFRemap2Status based on Integer32"""
    defaultValue = 1

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


_CtIFRemap2Status_Type.__name__ = "Integer32"
_CtIFRemap2Status_Object = MibTableColumn
ctIFRemap2Status = _CtIFRemap2Status_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 5),
    _CtIFRemap2Status_Type()
)
ctIFRemap2Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIFRemap2Status.setStatus("mandatory")


class _CtIFRemap2PhysicalErrors_Type(Integer32):
    """Custom type ctIFRemap2PhysicalErrors based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_CtIFRemap2PhysicalErrors_Type.__name__ = "Integer32"
_CtIFRemap2PhysicalErrors_Object = MibTableColumn
ctIFRemap2PhysicalErrors = _CtIFRemap2PhysicalErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 6),
    _CtIFRemap2PhysicalErrors_Type()
)
ctIFRemap2PhysicalErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIFRemap2PhysicalErrors.setStatus("mandatory")


class _CtIFRemap2EgressType_Type(Integer32):
    """Custom type ctIFRemap2EgressType based on Integer32"""
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
        *(("alwaysTagged", 2),
          ("alwaysUntagged", 3),
          ("normal", 1))
    )


_CtIFRemap2EgressType_Type.__name__ = "Integer32"
_CtIFRemap2EgressType_Object = MibTableColumn
ctIFRemap2EgressType = _CtIFRemap2EgressType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 1, 1, 7),
    _CtIFRemap2EgressType_Type()
)
ctIFRemap2EgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIFRemap2EgressType.setStatus("mandatory")
_CtIFRemap2PortTable_Object = MibTable
ctIFRemap2PortTable = _CtIFRemap2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    ctIFRemap2PortTable.setStatus("mandatory")
_CtIFRemap2PortEntry_Object = MibTableRow
ctIFRemap2PortEntry = _CtIFRemap2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1)
)
ctIFRemap2PortEntry.setIndexNames(
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortSlot"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2PortIndex"),
)
if mibBuilder.loadTexts:
    ctIFRemap2PortEntry.setStatus("mandatory")
_CtIFRemap2PortSlot_Type = Integer32
_CtIFRemap2PortSlot_Object = MibTableColumn
ctIFRemap2PortSlot = _CtIFRemap2PortSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 1),
    _CtIFRemap2PortSlot_Type()
)
ctIFRemap2PortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2PortSlot.setStatus("mandatory")
_CtIFRemap2PortIndex_Type = Integer32
_CtIFRemap2PortIndex_Object = MibTableColumn
ctIFRemap2PortIndex = _CtIFRemap2PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 2),
    _CtIFRemap2PortIndex_Type()
)
ctIFRemap2PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2PortIndex.setStatus("mandatory")
_CtIFRemap2PortReference_Type = ObjectIdentifier
_CtIFRemap2PortReference_Object = MibTableColumn
ctIFRemap2PortReference = _CtIFRemap2PortReference_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 3),
    _CtIFRemap2PortReference_Type()
)
ctIFRemap2PortReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2PortReference.setStatus("mandatory")


class _CtIFRemap2PhysErrsCapable_Type(Integer32):
    """Custom type ctIFRemap2PhysErrsCapable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_CtIFRemap2PhysErrsCapable_Type.__name__ = "Integer32"
_CtIFRemap2PhysErrsCapable_Object = MibTableColumn
ctIFRemap2PhysErrsCapable = _CtIFRemap2PhysErrsCapable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 2, 1, 4),
    _CtIFRemap2PhysErrsCapable_Type()
)
ctIFRemap2PhysErrsCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2PhysErrsCapable.setStatus("mandatory")
_CtIFRemap2SlotTable_Object = MibTable
ctIFRemap2SlotTable = _CtIFRemap2SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    ctIFRemap2SlotTable.setStatus("mandatory")
_CtIFRemap2SlotEntry_Object = MibTableRow
ctIFRemap2SlotEntry = _CtIFRemap2SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1)
)
ctIFRemap2SlotEntry.setIndexNames(
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2SlotIndex"),
)
if mibBuilder.loadTexts:
    ctIFRemap2SlotEntry.setStatus("mandatory")
_CtIFRemap2SlotIndex_Type = Integer32
_CtIFRemap2SlotIndex_Object = MibTableColumn
ctIFRemap2SlotIndex = _CtIFRemap2SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 1),
    _CtIFRemap2SlotIndex_Type()
)
ctIFRemap2SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2SlotIndex.setStatus("mandatory")
_CtIFRemap2SlotMaxRemaps_Type = Integer32
_CtIFRemap2SlotMaxRemaps_Object = MibTableColumn
ctIFRemap2SlotMaxRemaps = _CtIFRemap2SlotMaxRemaps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 2),
    _CtIFRemap2SlotMaxRemaps_Type()
)
ctIFRemap2SlotMaxRemaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2SlotMaxRemaps.setStatus("mandatory")
_CtIFRemap2SlotMaxRemoteDests_Type = Integer32
_CtIFRemap2SlotMaxRemoteDests_Object = MibTableColumn
ctIFRemap2SlotMaxRemoteDests = _CtIFRemap2SlotMaxRemoteDests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 3, 1, 3),
    _CtIFRemap2SlotMaxRemoteDests_Type()
)
ctIFRemap2SlotMaxRemoteDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2SlotMaxRemoteDests.setStatus("mandatory")
_CtIFRemap2VlanTable_Object = MibTable
ctIFRemap2VlanTable = _CtIFRemap2VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    ctIFRemap2VlanTable.setStatus("mandatory")
_CtIFRemap2VlanEntry_Object = MibTableRow
ctIFRemap2VlanEntry = _CtIFRemap2VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1)
)
ctIFRemap2VlanEntry.setIndexNames(
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceSlot"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanSourceVlan"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestSlot"),
    (0, "CTRON-IF-REMAP-2-MIB", "ctIFRemap2VlanDestPort"),
)
if mibBuilder.loadTexts:
    ctIFRemap2VlanEntry.setStatus("mandatory")
_CtIFRemap2VlanSourceSlot_Type = Integer32
_CtIFRemap2VlanSourceSlot_Object = MibTableColumn
ctIFRemap2VlanSourceSlot = _CtIFRemap2VlanSourceSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 1),
    _CtIFRemap2VlanSourceSlot_Type()
)
ctIFRemap2VlanSourceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2VlanSourceSlot.setStatus("mandatory")
_CtIFRemap2VlanSourceVlan_Type = Integer32
_CtIFRemap2VlanSourceVlan_Object = MibTableColumn
ctIFRemap2VlanSourceVlan = _CtIFRemap2VlanSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 2),
    _CtIFRemap2VlanSourceVlan_Type()
)
ctIFRemap2VlanSourceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2VlanSourceVlan.setStatus("mandatory")
_CtIFRemap2VlanDestSlot_Type = Integer32
_CtIFRemap2VlanDestSlot_Object = MibTableColumn
ctIFRemap2VlanDestSlot = _CtIFRemap2VlanDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 3),
    _CtIFRemap2VlanDestSlot_Type()
)
ctIFRemap2VlanDestSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2VlanDestSlot.setStatus("mandatory")
_CtIFRemap2VlanDestPort_Type = Integer32
_CtIFRemap2VlanDestPort_Object = MibTableColumn
ctIFRemap2VlanDestPort = _CtIFRemap2VlanDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 4),
    _CtIFRemap2VlanDestPort_Type()
)
ctIFRemap2VlanDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIFRemap2VlanDestPort.setStatus("mandatory")


class _CtIFRemap2VlanStatus_Type(Integer32):
    """Custom type ctIFRemap2VlanStatus based on Integer32"""
    defaultValue = 1

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


_CtIFRemap2VlanStatus_Type.__name__ = "Integer32"
_CtIFRemap2VlanStatus_Object = MibTableColumn
ctIFRemap2VlanStatus = _CtIFRemap2VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 5),
    _CtIFRemap2VlanStatus_Type()
)
ctIFRemap2VlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIFRemap2VlanStatus.setStatus("mandatory")


class _CtIFRemap2VlanEgressType_Type(Integer32):
    """Custom type ctIFRemap2VlanEgressType based on Integer32"""
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
        *(("alwaysTagged", 2),
          ("alwaysUntagged", 3),
          ("received", 1))
    )


_CtIFRemap2VlanEgressType_Type.__name__ = "Integer32"
_CtIFRemap2VlanEgressType_Object = MibTableColumn
ctIFRemap2VlanEgressType = _CtIFRemap2VlanEgressType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14, 1, 4, 1, 6),
    _CtIFRemap2VlanEgressType_Type()
)
ctIFRemap2VlanEgressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIFRemap2VlanEgressType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IF-REMAP-2-MIB",
    **{"ctIFRemap2Config": ctIFRemap2Config,
       "ctIFRemap2Table": ctIFRemap2Table,
       "ctIFRemap2Entry": ctIFRemap2Entry,
       "ctIFRemap2SourceSlot": ctIFRemap2SourceSlot,
       "ctIFRemap2SourcePort": ctIFRemap2SourcePort,
       "ctIFRemap2DestSlot": ctIFRemap2DestSlot,
       "ctIFRemap2DestPort": ctIFRemap2DestPort,
       "ctIFRemap2Status": ctIFRemap2Status,
       "ctIFRemap2PhysicalErrors": ctIFRemap2PhysicalErrors,
       "ctIFRemap2EgressType": ctIFRemap2EgressType,
       "ctIFRemap2PortTable": ctIFRemap2PortTable,
       "ctIFRemap2PortEntry": ctIFRemap2PortEntry,
       "ctIFRemap2PortSlot": ctIFRemap2PortSlot,
       "ctIFRemap2PortIndex": ctIFRemap2PortIndex,
       "ctIFRemap2PortReference": ctIFRemap2PortReference,
       "ctIFRemap2PhysErrsCapable": ctIFRemap2PhysErrsCapable,
       "ctIFRemap2SlotTable": ctIFRemap2SlotTable,
       "ctIFRemap2SlotEntry": ctIFRemap2SlotEntry,
       "ctIFRemap2SlotIndex": ctIFRemap2SlotIndex,
       "ctIFRemap2SlotMaxRemaps": ctIFRemap2SlotMaxRemaps,
       "ctIFRemap2SlotMaxRemoteDests": ctIFRemap2SlotMaxRemoteDests,
       "ctIFRemap2VlanTable": ctIFRemap2VlanTable,
       "ctIFRemap2VlanEntry": ctIFRemap2VlanEntry,
       "ctIFRemap2VlanSourceSlot": ctIFRemap2VlanSourceSlot,
       "ctIFRemap2VlanSourceVlan": ctIFRemap2VlanSourceVlan,
       "ctIFRemap2VlanDestSlot": ctIFRemap2VlanDestSlot,
       "ctIFRemap2VlanDestPort": ctIFRemap2VlanDestPort,
       "ctIFRemap2VlanStatus": ctIFRemap2VlanStatus,
       "ctIFRemap2VlanEgressType": ctIFRemap2VlanEgressType}
)
