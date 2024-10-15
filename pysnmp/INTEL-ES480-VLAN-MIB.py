# SNMP MIB module (INTEL-ES480-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-ES480-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:37 2024
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

(es480tAgent,) = mibBuilder.importSymbols(
    "INTEL-ES480-MIB",
    "es480tAgent")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

es480tVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2)
)


# Types definitions



class Es480tSwitchVlanType(Integer32):
    """Custom type Es480tSwitchVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("vlanLayer2", 1)
    )





class Es480tSwitchVlanEncapsType(Integer32):
    """Custom type Es480tSwitchVlanEncapsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("vlanEncaps8021q", 2)
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Es480tVlanGroup_ObjectIdentity = ObjectIdentity
es480tVlanGroup = _Es480tVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1)
)
_Es480tVlanIfTable_Object = MibTable
es480tVlanIfTable = _Es480tVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2)
)
if mibBuilder.loadTexts:
    es480tVlanIfTable.setStatus("mandatory")
_Es480tVlanIfEntry_Object = MibTableRow
es480tVlanIfEntry = _Es480tVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1)
)
es480tVlanIfEntry.setIndexNames(
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanIfIndex"),
)
if mibBuilder.loadTexts:
    es480tVlanIfEntry.setStatus("mandatory")
_Es480tVlanIfIndex_Type = Integer32
_Es480tVlanIfIndex_Object = MibTableColumn
es480tVlanIfIndex = _Es480tVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1, 1),
    _Es480tVlanIfIndex_Type()
)
es480tVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanIfIndex.setStatus("mandatory")


class _Es480tVlanIfDescr_Type(DisplayString):
    """Custom type es480tVlanIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Es480tVlanIfDescr_Type.__name__ = "DisplayString"
_Es480tVlanIfDescr_Object = MibTableColumn
es480tVlanIfDescr = _Es480tVlanIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1, 2),
    _Es480tVlanIfDescr_Type()
)
es480tVlanIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanIfDescr.setStatus("mandatory")
_Es480tVlanIfType_Type = Es480tSwitchVlanType
_Es480tVlanIfType_Object = MibTableColumn
es480tVlanIfType = _Es480tVlanIfType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1, 3),
    _Es480tVlanIfType_Type()
)
es480tVlanIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanIfType.setStatus("mandatory")


class _Es480tVlanIfGlobalIdentifier_Type(Integer32):
    """Custom type es480tVlanIfGlobalIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es480tVlanIfGlobalIdentifier_Type.__name__ = "Integer32"
_Es480tVlanIfGlobalIdentifier_Object = MibTableColumn
es480tVlanIfGlobalIdentifier = _Es480tVlanIfGlobalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1, 4),
    _Es480tVlanIfGlobalIdentifier_Type()
)
es480tVlanIfGlobalIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanIfGlobalIdentifier.setStatus("mandatory")
_Es480tVlanIfStatus_Type = RowStatus
_Es480tVlanIfStatus_Object = MibTableColumn
es480tVlanIfStatus = _Es480tVlanIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 1, 2, 1, 6),
    _Es480tVlanIfStatus_Type()
)
es480tVlanIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanIfStatus.setStatus("mandatory")
_Es480tVirtualGroup_ObjectIdentity = ObjectIdentity
es480tVirtualGroup = _Es480tVirtualGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 2)
)
_Es480tNextAvailableVirtIfIndex_Type = Integer32
_Es480tNextAvailableVirtIfIndex_Object = MibScalar
es480tNextAvailableVirtIfIndex = _Es480tNextAvailableVirtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 2, 1),
    _Es480tNextAvailableVirtIfIndex_Type()
)
es480tNextAvailableVirtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es480tNextAvailableVirtIfIndex.setStatus("mandatory")
_Es480tEncapsulationGroup_ObjectIdentity = ObjectIdentity
es480tEncapsulationGroup = _Es480tEncapsulationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3)
)
_Es480tVlanEncapsIfTable_Object = MibTable
es480tVlanEncapsIfTable = _Es480tVlanEncapsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1)
)
if mibBuilder.loadTexts:
    es480tVlanEncapsIfTable.setStatus("mandatory")
_Es480tVlanEncapsIfEntry_Object = MibTableRow
es480tVlanEncapsIfEntry = _Es480tVlanEncapsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1, 1)
)
es480tVlanEncapsIfEntry.setIndexNames(
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanEncapsIfIndex"),
)
if mibBuilder.loadTexts:
    es480tVlanEncapsIfEntry.setStatus("mandatory")
_Es480tVlanEncapsIfIndex_Type = Integer32
_Es480tVlanEncapsIfIndex_Object = MibTableColumn
es480tVlanEncapsIfIndex = _Es480tVlanEncapsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1, 1, 1),
    _Es480tVlanEncapsIfIndex_Type()
)
es480tVlanEncapsIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanEncapsIfIndex.setStatus("mandatory")
_Es480tVlanEncapsIfType_Type = Es480tSwitchVlanEncapsType
_Es480tVlanEncapsIfType_Object = MibTableColumn
es480tVlanEncapsIfType = _Es480tVlanEncapsIfType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1, 1, 2),
    _Es480tVlanEncapsIfType_Type()
)
es480tVlanEncapsIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanEncapsIfType.setStatus("mandatory")
_Es480tVlanEncapsIfTag_Type = Integer32
_Es480tVlanEncapsIfTag_Object = MibTableColumn
es480tVlanEncapsIfTag = _Es480tVlanEncapsIfTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1, 1, 3),
    _Es480tVlanEncapsIfTag_Type()
)
es480tVlanEncapsIfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanEncapsIfTag.setStatus("mandatory")
_Es480tVlanEncapsIfStatus_Type = RowStatus
_Es480tVlanEncapsIfStatus_Object = MibTableColumn
es480tVlanEncapsIfStatus = _Es480tVlanEncapsIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 3, 1, 1, 4),
    _Es480tVlanEncapsIfStatus_Type()
)
es480tVlanEncapsIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanEncapsIfStatus.setStatus("mandatory")
_Es480tProtocolGroup_ObjectIdentity = ObjectIdentity
es480tProtocolGroup = _Es480tProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5)
)
_Es480tVlanProtocolTable_Object = MibTable
es480tVlanProtocolTable = _Es480tVlanProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1)
)
if mibBuilder.loadTexts:
    es480tVlanProtocolTable.setStatus("mandatory")
_Es480tVlanProtocolEntry_Object = MibTableRow
es480tVlanProtocolEntry = _Es480tVlanProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1)
)
es480tVlanProtocolEntry.setIndexNames(
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanProtocolIndex"),
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanProtocolIdIndex"),
)
if mibBuilder.loadTexts:
    es480tVlanProtocolEntry.setStatus("mandatory")


class _Es480tVlanProtocolIndex_Type(Integer32):
    """Custom type es480tVlanProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Es480tVlanProtocolIndex_Type.__name__ = "Integer32"
_Es480tVlanProtocolIndex_Object = MibTableColumn
es480tVlanProtocolIndex = _Es480tVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 1),
    _Es480tVlanProtocolIndex_Type()
)
es480tVlanProtocolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolIndex.setStatus("mandatory")


class _Es480tVlanProtocolIdIndex_Type(Integer32):
    """Custom type es480tVlanProtocolIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Es480tVlanProtocolIdIndex_Type.__name__ = "Integer32"
_Es480tVlanProtocolIdIndex_Object = MibTableColumn
es480tVlanProtocolIdIndex = _Es480tVlanProtocolIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 2),
    _Es480tVlanProtocolIdIndex_Type()
)
es480tVlanProtocolIdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolIdIndex.setStatus("mandatory")


class _Es480tVlanProtocolName_Type(DisplayString):
    """Custom type es480tVlanProtocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Es480tVlanProtocolName_Type.__name__ = "DisplayString"
_Es480tVlanProtocolName_Object = MibTableColumn
es480tVlanProtocolName = _Es480tVlanProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 3),
    _Es480tVlanProtocolName_Type()
)
es480tVlanProtocolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolName.setStatus("mandatory")


class _Es480tVlanProtocolDllEncapsType_Type(Integer32):
    """Custom type es480tVlanProtocolDllEncapsType based on Integer32"""
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
        *(("any", 1),
          ("ethertype", 2),
          ("llc", 3),
          ("llcSnapEthertype", 4))
    )


_Es480tVlanProtocolDllEncapsType_Type.__name__ = "Integer32"
_Es480tVlanProtocolDllEncapsType_Object = MibTableColumn
es480tVlanProtocolDllEncapsType = _Es480tVlanProtocolDllEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 4),
    _Es480tVlanProtocolDllEncapsType_Type()
)
es480tVlanProtocolDllEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolDllEncapsType.setStatus("mandatory")


class _Es480tVlanProtocolId_Type(Integer32):
    """Custom type es480tVlanProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Es480tVlanProtocolId_Type.__name__ = "Integer32"
_Es480tVlanProtocolId_Object = MibTableColumn
es480tVlanProtocolId = _Es480tVlanProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 5),
    _Es480tVlanProtocolId_Type()
)
es480tVlanProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolId.setStatus("mandatory")
_Es480tVlanProtocolStatus_Type = RowStatus
_Es480tVlanProtocolStatus_Object = MibTableColumn
es480tVlanProtocolStatus = _Es480tVlanProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 1, 1, 6),
    _Es480tVlanProtocolStatus_Type()
)
es480tVlanProtocolStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolStatus.setStatus("mandatory")
_Es480tVlanProtocolVlanTable_Object = MibTable
es480tVlanProtocolVlanTable = _Es480tVlanProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 2)
)
if mibBuilder.loadTexts:
    es480tVlanProtocolVlanTable.setStatus("mandatory")
_Es480tVlanProtocolVlanEntry_Object = MibTableRow
es480tVlanProtocolVlanEntry = _Es480tVlanProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 2, 1)
)
es480tVlanProtocolVlanEntry.setIndexNames(
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanProtocolVlanIfIndex"),
    (0, "INTEL-ES480-VLAN-MIB", "es480tVlanProtocolVlanProtocolIndex"),
)
if mibBuilder.loadTexts:
    es480tVlanProtocolVlanEntry.setStatus("mandatory")
_Es480tVlanProtocolVlanIfIndex_Type = Integer32
_Es480tVlanProtocolVlanIfIndex_Object = MibTableColumn
es480tVlanProtocolVlanIfIndex = _Es480tVlanProtocolVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 2, 1, 1),
    _Es480tVlanProtocolVlanIfIndex_Type()
)
es480tVlanProtocolVlanIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolVlanIfIndex.setStatus("mandatory")
_Es480tVlanProtocolVlanProtocolIndex_Type = Integer32
_Es480tVlanProtocolVlanProtocolIndex_Object = MibTableColumn
es480tVlanProtocolVlanProtocolIndex = _Es480tVlanProtocolVlanProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 2, 1, 2),
    _Es480tVlanProtocolVlanProtocolIndex_Type()
)
es480tVlanProtocolVlanProtocolIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolVlanProtocolIndex.setStatus("mandatory")
_Es480tVlanProtocolVlanStatus_Type = RowStatus
_Es480tVlanProtocolVlanStatus_Object = MibTableColumn
es480tVlanProtocolVlanStatus = _Es480tVlanProtocolVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 60, 2, 5, 2, 1, 3),
    _Es480tVlanProtocolVlanStatus_Type()
)
es480tVlanProtocolVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es480tVlanProtocolVlanStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-ES480-VLAN-MIB",
    **{"Es480tSwitchVlanType": Es480tSwitchVlanType,
       "Es480tSwitchVlanEncapsType": Es480tSwitchVlanEncapsType,
       "es480tVlan": es480tVlan,
       "es480tVlanGroup": es480tVlanGroup,
       "es480tVlanIfTable": es480tVlanIfTable,
       "es480tVlanIfEntry": es480tVlanIfEntry,
       "es480tVlanIfIndex": es480tVlanIfIndex,
       "es480tVlanIfDescr": es480tVlanIfDescr,
       "es480tVlanIfType": es480tVlanIfType,
       "es480tVlanIfGlobalIdentifier": es480tVlanIfGlobalIdentifier,
       "es480tVlanIfStatus": es480tVlanIfStatus,
       "es480tVirtualGroup": es480tVirtualGroup,
       "es480tNextAvailableVirtIfIndex": es480tNextAvailableVirtIfIndex,
       "es480tEncapsulationGroup": es480tEncapsulationGroup,
       "es480tVlanEncapsIfTable": es480tVlanEncapsIfTable,
       "es480tVlanEncapsIfEntry": es480tVlanEncapsIfEntry,
       "es480tVlanEncapsIfIndex": es480tVlanEncapsIfIndex,
       "es480tVlanEncapsIfType": es480tVlanEncapsIfType,
       "es480tVlanEncapsIfTag": es480tVlanEncapsIfTag,
       "es480tVlanEncapsIfStatus": es480tVlanEncapsIfStatus,
       "es480tProtocolGroup": es480tProtocolGroup,
       "es480tVlanProtocolTable": es480tVlanProtocolTable,
       "es480tVlanProtocolEntry": es480tVlanProtocolEntry,
       "es480tVlanProtocolIndex": es480tVlanProtocolIndex,
       "es480tVlanProtocolIdIndex": es480tVlanProtocolIdIndex,
       "es480tVlanProtocolName": es480tVlanProtocolName,
       "es480tVlanProtocolDllEncapsType": es480tVlanProtocolDllEncapsType,
       "es480tVlanProtocolId": es480tVlanProtocolId,
       "es480tVlanProtocolStatus": es480tVlanProtocolStatus,
       "es480tVlanProtocolVlanTable": es480tVlanProtocolVlanTable,
       "es480tVlanProtocolVlanEntry": es480tVlanProtocolVlanEntry,
       "es480tVlanProtocolVlanIfIndex": es480tVlanProtocolVlanIfIndex,
       "es480tVlanProtocolVlanProtocolIndex": es480tVlanProtocolVlanProtocolIndex,
       "es480tVlanProtocolVlanStatus": es480tVlanProtocolVlanStatus}
)
