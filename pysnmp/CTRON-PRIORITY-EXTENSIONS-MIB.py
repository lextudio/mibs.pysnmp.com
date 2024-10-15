# SNMP MIB module (CTRON-PRIORITY-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-PRIORITY-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:08 2024
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

(ctPriorityExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctPriorityExt")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtPriorityExtTxQueue_ObjectIdentity = ObjectIdentity
ctPriorityExtTxQueue = _CtPriorityExtTxQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1)
)
_CtPriorityExtTXQueueTable_Object = MibTable
ctPriorityExtTXQueueTable = _CtPriorityExtTXQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    ctPriorityExtTXQueueTable.setStatus("mandatory")
_CtPriorityExtTXQueueEntry_Object = MibTableRow
ctPriorityExtTXQueueEntry = _CtPriorityExtTXQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1)
)
ctPriorityExtTXQueueEntry.setIndexNames(
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtSlotNum"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtInterfaceNum"),
)
if mibBuilder.loadTexts:
    ctPriorityExtTXQueueEntry.setStatus("mandatory")
_CtPriorityExtSlotNum_Type = Integer32
_CtPriorityExtSlotNum_Object = MibTableColumn
ctPriorityExtSlotNum = _CtPriorityExtSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 1),
    _CtPriorityExtSlotNum_Type()
)
ctPriorityExtSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtSlotNum.setStatus("mandatory")
_CtPriorityExtInterfaceNum_Type = Integer32
_CtPriorityExtInterfaceNum_Object = MibTableColumn
ctPriorityExtInterfaceNum = _CtPriorityExtInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 2),
    _CtPriorityExtInterfaceNum_Type()
)
ctPriorityExtInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtInterfaceNum.setStatus("mandatory")


class _CtPriorityExtNumTXQueues_Type(Integer32):
    """Custom type ctPriorityExtNumTXQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CtPriorityExtNumTXQueues_Type.__name__ = "Integer32"
_CtPriorityExtNumTXQueues_Object = MibTableColumn
ctPriorityExtNumTXQueues = _CtPriorityExtNumTXQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 1, 1, 1, 3),
    _CtPriorityExtNumTXQueues_Type()
)
ctPriorityExtNumTXQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtNumTXQueues.setStatus("mandatory")
_CtPriorityExtMACConfig_ObjectIdentity = ObjectIdentity
ctPriorityExtMACConfig = _CtPriorityExtMACConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2)
)


class _CtPriorityExtMACStatus_Type(Integer32):
    """Custom type ctPriorityExtMACStatus based on Integer32"""
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


_CtPriorityExtMACStatus_Type.__name__ = "Integer32"
_CtPriorityExtMACStatus_Object = MibScalar
ctPriorityExtMACStatus = _CtPriorityExtMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 1),
    _CtPriorityExtMACStatus_Type()
)
ctPriorityExtMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtMACStatus.setStatus("mandatory")
_CtPriorityExtNumMACEntries_Type = Integer32
_CtPriorityExtNumMACEntries_Object = MibScalar
ctPriorityExtNumMACEntries = _CtPriorityExtNumMACEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 2),
    _CtPriorityExtNumMACEntries_Type()
)
ctPriorityExtNumMACEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtNumMACEntries.setStatus("mandatory")
_CtPriorityExtMaxNumMACEntries_Type = Integer32
_CtPriorityExtMaxNumMACEntries_Object = MibScalar
ctPriorityExtMaxNumMACEntries = _CtPriorityExtMaxNumMACEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 3),
    _CtPriorityExtMaxNumMACEntries_Type()
)
ctPriorityExtMaxNumMACEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtMaxNumMACEntries.setStatus("mandatory")
_CtPriorityExtMaxNumPktTypesPerMACEntry_Type = Integer32
_CtPriorityExtMaxNumPktTypesPerMACEntry_Object = MibScalar
ctPriorityExtMaxNumPktTypesPerMACEntry = _CtPriorityExtMaxNumPktTypesPerMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 4),
    _CtPriorityExtMaxNumPktTypesPerMACEntry_Type()
)
ctPriorityExtMaxNumPktTypesPerMACEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtMaxNumPktTypesPerMACEntry.setStatus("mandatory")
_CtPriorityExtMACTable_Object = MibTable
ctPriorityExtMACTable = _CtPriorityExtMACTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5)
)
if mibBuilder.loadTexts:
    ctPriorityExtMACTable.setStatus("mandatory")
_CtPriorityExtMACEntry_Object = MibTableRow
ctPriorityExtMACEntry = _CtPriorityExtMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1)
)
ctPriorityExtMACEntry.setIndexNames(
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACAddr"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtAddrType"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACPktType"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtMACVlanId"),
)
if mibBuilder.loadTexts:
    ctPriorityExtMACEntry.setStatus("mandatory")
_CtPriorityExtMACAddr_Type = PhysAddress
_CtPriorityExtMACAddr_Object = MibTableColumn
ctPriorityExtMACAddr = _CtPriorityExtMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 1),
    _CtPriorityExtMACAddr_Type()
)
ctPriorityExtMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtMACAddr.setStatus("mandatory")


class _CtPriorityExtAddrType_Type(Integer32):
    """Custom type ctPriorityExtAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("destAddr", 1),
          ("destOrSource", 3),
          ("srcAddr", 2))
    )


_CtPriorityExtAddrType_Type.__name__ = "Integer32"
_CtPriorityExtAddrType_Object = MibTableColumn
ctPriorityExtAddrType = _CtPriorityExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 2),
    _CtPriorityExtAddrType_Type()
)
ctPriorityExtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtAddrType.setStatus("mandatory")
_CtPriorityExtMACPktType_Type = Integer32
_CtPriorityExtMACPktType_Object = MibTableColumn
ctPriorityExtMACPktType = _CtPriorityExtMACPktType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 3),
    _CtPriorityExtMACPktType_Type()
)
ctPriorityExtMACPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtMACPktType.setStatus("mandatory")
_CtPriorityExtMACVlanId_Type = Integer32
_CtPriorityExtMACVlanId_Object = MibTableColumn
ctPriorityExtMACVlanId = _CtPriorityExtMACVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 4),
    _CtPriorityExtMACVlanId_Type()
)
ctPriorityExtMACVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtMACVlanId.setStatus("mandatory")


class _CtPriorityExtMACPriority_Type(Integer32):
    """Custom type ctPriorityExtMACPriority based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("delete", 100),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_CtPriorityExtMACPriority_Type.__name__ = "Integer32"
_CtPriorityExtMACPriority_Object = MibTableColumn
ctPriorityExtMACPriority = _CtPriorityExtMACPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 2, 5, 1, 5),
    _CtPriorityExtMACPriority_Type()
)
ctPriorityExtMACPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtMACPriority.setStatus("mandatory")
_CtPriorityExtPktTypeConfig_ObjectIdentity = ObjectIdentity
ctPriorityExtPktTypeConfig = _CtPriorityExtPktTypeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3)
)


class _CtPriorityExtPktTypeStatus_Type(Integer32):
    """Custom type ctPriorityExtPktTypeStatus based on Integer32"""
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


_CtPriorityExtPktTypeStatus_Type.__name__ = "Integer32"
_CtPriorityExtPktTypeStatus_Object = MibScalar
ctPriorityExtPktTypeStatus = _CtPriorityExtPktTypeStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 1),
    _CtPriorityExtPktTypeStatus_Type()
)
ctPriorityExtPktTypeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtPktTypeStatus.setStatus("mandatory")
_CtPriorityExtNumPktTypeEntries_Type = Integer32
_CtPriorityExtNumPktTypeEntries_Object = MibScalar
ctPriorityExtNumPktTypeEntries = _CtPriorityExtNumPktTypeEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 2),
    _CtPriorityExtNumPktTypeEntries_Type()
)
ctPriorityExtNumPktTypeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtNumPktTypeEntries.setStatus("mandatory")
_CtPriorityExtMaxNumPktTypeEntries_Type = Integer32
_CtPriorityExtMaxNumPktTypeEntries_Object = MibScalar
ctPriorityExtMaxNumPktTypeEntries = _CtPriorityExtMaxNumPktTypeEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 3),
    _CtPriorityExtMaxNumPktTypeEntries_Type()
)
ctPriorityExtMaxNumPktTypeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtMaxNumPktTypeEntries.setStatus("mandatory")
_CtPriorityExtPktTypeTable_Object = MibTable
ctPriorityExtPktTypeTable = _CtPriorityExtPktTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4)
)
if mibBuilder.loadTexts:
    ctPriorityExtPktTypeTable.setStatus("mandatory")
_CtPriorityExtPktTypeEntry_Object = MibTableRow
ctPriorityExtPktTypeEntry = _CtPriorityExtPktTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1)
)
ctPriorityExtPktTypeEntry.setIndexNames(
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPktType"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPktTypeVlanId"),
)
if mibBuilder.loadTexts:
    ctPriorityExtPktTypeEntry.setStatus("mandatory")
_CtPriorityExtPktType_Type = Integer32
_CtPriorityExtPktType_Object = MibTableColumn
ctPriorityExtPktType = _CtPriorityExtPktType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 1),
    _CtPriorityExtPktType_Type()
)
ctPriorityExtPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtPktType.setStatus("mandatory")
_CtPriorityExtPktTypeVlanId_Type = Integer32
_CtPriorityExtPktTypeVlanId_Object = MibTableColumn
ctPriorityExtPktTypeVlanId = _CtPriorityExtPktTypeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 2),
    _CtPriorityExtPktTypeVlanId_Type()
)
ctPriorityExtPktTypeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtPktTypeVlanId.setStatus("mandatory")


class _CtPriorityExtPktTypePriority_Type(Integer32):
    """Custom type ctPriorityExtPktTypePriority based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("delete", 100),
          ("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_CtPriorityExtPktTypePriority_Type.__name__ = "Integer32"
_CtPriorityExtPktTypePriority_Object = MibTableColumn
ctPriorityExtPktTypePriority = _CtPriorityExtPktTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 3, 4, 1, 3),
    _CtPriorityExtPktTypePriority_Type()
)
ctPriorityExtPktTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtPktTypePriority.setStatus("mandatory")
_CtPriorityExtPortConfig_ObjectIdentity = ObjectIdentity
ctPriorityExtPortConfig = _CtPriorityExtPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4)
)


class _CtPriorityExtPortStatus_Type(Integer32):
    """Custom type ctPriorityExtPortStatus based on Integer32"""
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


_CtPriorityExtPortStatus_Type.__name__ = "Integer32"
_CtPriorityExtPortStatus_Object = MibScalar
ctPriorityExtPortStatus = _CtPriorityExtPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 1),
    _CtPriorityExtPortStatus_Type()
)
ctPriorityExtPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtPortStatus.setStatus("mandatory")
_CtPriorityExtPortTable_Object = MibTable
ctPriorityExtPortTable = _CtPriorityExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2)
)
if mibBuilder.loadTexts:
    ctPriorityExtPortTable.setStatus("mandatory")
_CtPriorityExtPortEntry_Object = MibTableRow
ctPriorityExtPortEntry = _CtPriorityExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1)
)
ctPriorityExtPortEntry.setIndexNames(
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPortSlotNum"),
    (0, "CTRON-PRIORITY-EXTENSIONS-MIB", "ctPriorityExtPortInterfaceNum"),
)
if mibBuilder.loadTexts:
    ctPriorityExtPortEntry.setStatus("mandatory")
_CtPriorityExtPortSlotNum_Type = Integer32
_CtPriorityExtPortSlotNum_Object = MibTableColumn
ctPriorityExtPortSlotNum = _CtPriorityExtPortSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 1),
    _CtPriorityExtPortSlotNum_Type()
)
ctPriorityExtPortSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtPortSlotNum.setStatus("mandatory")
_CtPriorityExtPortInterfaceNum_Type = Integer32
_CtPriorityExtPortInterfaceNum_Object = MibTableColumn
ctPriorityExtPortInterfaceNum = _CtPriorityExtPortInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 2),
    _CtPriorityExtPortInterfaceNum_Type()
)
ctPriorityExtPortInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctPriorityExtPortInterfaceNum.setStatus("mandatory")


class _CtPriorityExtPortPriority_Type(Integer32):
    """Custom type ctPriorityExtPortPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 1),
          ("priority1", 2),
          ("priority2", 3),
          ("priority3", 4),
          ("priority4", 5),
          ("priority5", 6),
          ("priority6", 7),
          ("priority7", 8))
    )


_CtPriorityExtPortPriority_Type.__name__ = "Integer32"
_CtPriorityExtPortPriority_Object = MibTableColumn
ctPriorityExtPortPriority = _CtPriorityExtPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 3),
    _CtPriorityExtPortPriority_Type()
)
ctPriorityExtPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtPortPriority.setStatus("mandatory")


class _CtPriorityExtFwdInboundPriority_Type(Integer32):
    """Custom type ctPriorityExtFwdInboundPriority based on Integer32"""
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


_CtPriorityExtFwdInboundPriority_Type.__name__ = "Integer32"
_CtPriorityExtFwdInboundPriority_Object = MibTableColumn
ctPriorityExtFwdInboundPriority = _CtPriorityExtFwdInboundPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 4, 2, 1, 4),
    _CtPriorityExtFwdInboundPriority_Type()
)
ctPriorityExtFwdInboundPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctPriorityExtFwdInboundPriority.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-PRIORITY-EXTENSIONS-MIB",
    **{"ctPriorityExtTxQueue": ctPriorityExtTxQueue,
       "ctPriorityExtTXQueueTable": ctPriorityExtTXQueueTable,
       "ctPriorityExtTXQueueEntry": ctPriorityExtTXQueueEntry,
       "ctPriorityExtSlotNum": ctPriorityExtSlotNum,
       "ctPriorityExtInterfaceNum": ctPriorityExtInterfaceNum,
       "ctPriorityExtNumTXQueues": ctPriorityExtNumTXQueues,
       "ctPriorityExtMACConfig": ctPriorityExtMACConfig,
       "ctPriorityExtMACStatus": ctPriorityExtMACStatus,
       "ctPriorityExtNumMACEntries": ctPriorityExtNumMACEntries,
       "ctPriorityExtMaxNumMACEntries": ctPriorityExtMaxNumMACEntries,
       "ctPriorityExtMaxNumPktTypesPerMACEntry": ctPriorityExtMaxNumPktTypesPerMACEntry,
       "ctPriorityExtMACTable": ctPriorityExtMACTable,
       "ctPriorityExtMACEntry": ctPriorityExtMACEntry,
       "ctPriorityExtMACAddr": ctPriorityExtMACAddr,
       "ctPriorityExtAddrType": ctPriorityExtAddrType,
       "ctPriorityExtMACPktType": ctPriorityExtMACPktType,
       "ctPriorityExtMACVlanId": ctPriorityExtMACVlanId,
       "ctPriorityExtMACPriority": ctPriorityExtMACPriority,
       "ctPriorityExtPktTypeConfig": ctPriorityExtPktTypeConfig,
       "ctPriorityExtPktTypeStatus": ctPriorityExtPktTypeStatus,
       "ctPriorityExtNumPktTypeEntries": ctPriorityExtNumPktTypeEntries,
       "ctPriorityExtMaxNumPktTypeEntries": ctPriorityExtMaxNumPktTypeEntries,
       "ctPriorityExtPktTypeTable": ctPriorityExtPktTypeTable,
       "ctPriorityExtPktTypeEntry": ctPriorityExtPktTypeEntry,
       "ctPriorityExtPktType": ctPriorityExtPktType,
       "ctPriorityExtPktTypeVlanId": ctPriorityExtPktTypeVlanId,
       "ctPriorityExtPktTypePriority": ctPriorityExtPktTypePriority,
       "ctPriorityExtPortConfig": ctPriorityExtPortConfig,
       "ctPriorityExtPortStatus": ctPriorityExtPortStatus,
       "ctPriorityExtPortTable": ctPriorityExtPortTable,
       "ctPriorityExtPortEntry": ctPriorityExtPortEntry,
       "ctPriorityExtPortSlotNum": ctPriorityExtPortSlotNum,
       "ctPriorityExtPortInterfaceNum": ctPriorityExtPortInterfaceNum,
       "ctPriorityExtPortPriority": ctPriorityExtPortPriority,
       "ctPriorityExtFwdInboundPriority": ctPriorityExtFwdInboundPriority}
)
