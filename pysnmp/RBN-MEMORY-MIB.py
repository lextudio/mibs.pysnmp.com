# SNMP MIB module (RBN-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:15 2024
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnKBytes,) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnKBytes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnMemoryMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16)
)
rbnMemoryMib.setRevisions(
        ("2004-03-05 17:00",
         "2002-06-26 00:00",
         "2002-01-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnMemoryMIBNotifications_ObjectIdentity = ObjectIdentity
rbnMemoryMIBNotifications = _RbnMemoryMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 0)
)
_RbnMemoryMIBObjects_ObjectIdentity = ObjectIdentity
rbnMemoryMIBObjects = _RbnMemoryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1)
)
_RbnSmsMemoryTable_Object = MibTable
rbnSmsMemoryTable = _RbnSmsMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSmsMemoryTable.setStatus("obsolete")
_RbnSmsMemoryEntry_Object = MibTableRow
rbnSmsMemoryEntry = _RbnSmsMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1)
)
rbnSmsMemoryEntry.setIndexNames(
    (0, "RBN-MEMORY-MIB", "rbnSmsMemoryIndex"),
)
if mibBuilder.loadTexts:
    rbnSmsMemoryEntry.setStatus("obsolete")


class _RbnSmsMemoryIndex_Type(Unsigned32):
    """Custom type rbnSmsMemoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnSmsMemoryIndex_Type.__name__ = "Unsigned32"
_RbnSmsMemoryIndex_Object = MibTableColumn
rbnSmsMemoryIndex = _RbnSmsMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 1),
    _RbnSmsMemoryIndex_Type()
)
rbnSmsMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSmsMemoryIndex.setStatus("obsolete")


class _RbnSmsMemoryModule_Type(SnmpAdminString):
    """Custom type rbnSmsMemoryModule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnSmsMemoryModule_Type.__name__ = "SnmpAdminString"
_RbnSmsMemoryModule_Object = MibTableColumn
rbnSmsMemoryModule = _RbnSmsMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 2),
    _RbnSmsMemoryModule_Type()
)
rbnSmsMemoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSmsMemoryModule.setStatus("obsolete")


class _RbnSmsMemoryFreeBytes_Type(Unsigned32):
    """Custom type rbnSmsMemoryFreeBytes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnSmsMemoryFreeBytes_Type.__name__ = "Unsigned32"
_RbnSmsMemoryFreeBytes_Object = MibTableColumn
rbnSmsMemoryFreeBytes = _RbnSmsMemoryFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 3),
    _RbnSmsMemoryFreeBytes_Type()
)
rbnSmsMemoryFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSmsMemoryFreeBytes.setStatus("obsolete")


class _RbnSmsMemoryBytesInUse_Type(Unsigned32):
    """Custom type rbnSmsMemoryBytesInUse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnSmsMemoryBytesInUse_Type.__name__ = "Unsigned32"
_RbnSmsMemoryBytesInUse_Object = MibTableColumn
rbnSmsMemoryBytesInUse = _RbnSmsMemoryBytesInUse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 4),
    _RbnSmsMemoryBytesInUse_Type()
)
rbnSmsMemoryBytesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSmsMemoryBytesInUse.setStatus("obsolete")


class _RbnSmsMemoryBlocksInUse_Type(Unsigned32):
    """Custom type rbnSmsMemoryBlocksInUse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnSmsMemoryBlocksInUse_Type.__name__ = "Unsigned32"
_RbnSmsMemoryBlocksInUse_Object = MibTableColumn
rbnSmsMemoryBlocksInUse = _RbnSmsMemoryBlocksInUse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 5),
    _RbnSmsMemoryBlocksInUse_Type()
)
rbnSmsMemoryBlocksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSmsMemoryBlocksInUse.setStatus("obsolete")


class _RbnSmsMemoryCumulBlocks_Type(Unsigned32):
    """Custom type rbnSmsMemoryCumulBlocks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnSmsMemoryCumulBlocks_Type.__name__ = "Unsigned32"
_RbnSmsMemoryCumulBlocks_Object = MibTableColumn
rbnSmsMemoryCumulBlocks = _RbnSmsMemoryCumulBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 1, 1, 6),
    _RbnSmsMemoryCumulBlocks_Type()
)
rbnSmsMemoryCumulBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSmsMemoryCumulBlocks.setStatus("obsolete")
_RbnMemoryTable_Object = MibTable
rbnMemoryTable = _RbnMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rbnMemoryTable.setStatus("current")
_RbnMemoryEntry_Object = MibTableRow
rbnMemoryEntry = _RbnMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1)
)
rbnMemoryEntry.setIndexNames(
    (0, "RBN-MEMORY-MIB", "rbnMemoryIndex"),
)
if mibBuilder.loadTexts:
    rbnMemoryEntry.setStatus("current")


class _RbnMemoryIndex_Type(Unsigned32):
    """Custom type rbnMemoryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnMemoryIndex_Type.__name__ = "Unsigned32"
_RbnMemoryIndex_Object = MibTableColumn
rbnMemoryIndex = _RbnMemoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 1),
    _RbnMemoryIndex_Type()
)
rbnMemoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMemoryIndex.setStatus("current")


class _RbnMemoryModule_Type(SnmpAdminString):
    """Custom type rbnMemoryModule based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbnMemoryModule_Type.__name__ = "SnmpAdminString"
_RbnMemoryModule_Object = MibTableColumn
rbnMemoryModule = _RbnMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 2),
    _RbnMemoryModule_Type()
)
rbnMemoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMemoryModule.setStatus("current")
_RbnMemoryFreeKBytes_Type = RbnKBytes
_RbnMemoryFreeKBytes_Object = MibTableColumn
rbnMemoryFreeKBytes = _RbnMemoryFreeKBytes_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 3),
    _RbnMemoryFreeKBytes_Type()
)
rbnMemoryFreeKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMemoryFreeKBytes.setStatus("current")
if mibBuilder.loadTexts:
    rbnMemoryFreeKBytes.setUnits("KBytes")
_RbnMemoryKBytesInUse_Type = RbnKBytes
_RbnMemoryKBytesInUse_Object = MibTableColumn
rbnMemoryKBytesInUse = _RbnMemoryKBytesInUse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 4),
    _RbnMemoryKBytesInUse_Type()
)
rbnMemoryKBytesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMemoryKBytesInUse.setStatus("current")
if mibBuilder.loadTexts:
    rbnMemoryKBytesInUse.setUnits("KBytes")


class _RbnMemoryBlocksInUse_Type(Unsigned32):
    """Custom type rbnMemoryBlocksInUse based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnMemoryBlocksInUse_Type.__name__ = "Unsigned32"
_RbnMemoryBlocksInUse_Object = MibTableColumn
rbnMemoryBlocksInUse = _RbnMemoryBlocksInUse_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 5),
    _RbnMemoryBlocksInUse_Type()
)
rbnMemoryBlocksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMemoryBlocksInUse.setStatus("current")


class _RbnMemoryCumulBlocks_Type(Unsigned32):
    """Custom type rbnMemoryCumulBlocks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_RbnMemoryCumulBlocks_Type.__name__ = "Unsigned32"
_RbnMemoryCumulBlocks_Object = MibTableColumn
rbnMemoryCumulBlocks = _RbnMemoryCumulBlocks_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 1, 2, 1, 6),
    _RbnMemoryCumulBlocks_Type()
)
rbnMemoryCumulBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMemoryCumulBlocks.setStatus("current")
_RbnMemoryMIBConformance_ObjectIdentity = ObjectIdentity
rbnMemoryMIBConformance = _RbnMemoryMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2)
)
_RbnSmsMemoryCompliances_ObjectIdentity = ObjectIdentity
rbnSmsMemoryCompliances = _RbnSmsMemoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 1)
)
_RbnSmsMemoryGroups_ObjectIdentity = ObjectIdentity
rbnSmsMemoryGroups = _RbnSmsMemoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 2)
)
_RbnMemoryCompliances_ObjectIdentity = ObjectIdentity
rbnMemoryCompliances = _RbnMemoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 3)
)
_RbnMemoryGroups_ObjectIdentity = ObjectIdentity
rbnMemoryGroups = _RbnMemoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 4)
)

# Managed Objects groups

rbnSmsMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 2, 1)
)
rbnSmsMemoryGroup.setObjects(
      *(("RBN-MEMORY-MIB", "rbnSmsMemoryModule"),
        ("RBN-MEMORY-MIB", "rbnSmsMemoryFreeBytes"),
        ("RBN-MEMORY-MIB", "rbnSmsMemoryBytesInUse"),
        ("RBN-MEMORY-MIB", "rbnSmsMemoryBlocksInUse"),
        ("RBN-MEMORY-MIB", "rbnSmsMemoryCumulBlocks"))
)
if mibBuilder.loadTexts:
    rbnSmsMemoryGroup.setStatus("obsolete")

rbnMemoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 4, 1)
)
rbnMemoryGroup.setObjects(
      *(("RBN-MEMORY-MIB", "rbnMemoryModule"),
        ("RBN-MEMORY-MIB", "rbnMemoryFreeKBytes"),
        ("RBN-MEMORY-MIB", "rbnMemoryKBytesInUse"),
        ("RBN-MEMORY-MIB", "rbnMemoryBlocksInUse"),
        ("RBN-MEMORY-MIB", "rbnMemoryCumulBlocks"))
)
if mibBuilder.loadTexts:
    rbnMemoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnSmsMemoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSmsMemoryCompliance.setStatus(
        "obsolete"
    )

rbnMemoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 16, 2, 3, 1)
)
if mibBuilder.loadTexts:
    rbnMemoryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-MEMORY-MIB",
    **{"rbnMemoryMib": rbnMemoryMib,
       "rbnMemoryMIBNotifications": rbnMemoryMIBNotifications,
       "rbnMemoryMIBObjects": rbnMemoryMIBObjects,
       "rbnSmsMemoryTable": rbnSmsMemoryTable,
       "rbnSmsMemoryEntry": rbnSmsMemoryEntry,
       "rbnSmsMemoryIndex": rbnSmsMemoryIndex,
       "rbnSmsMemoryModule": rbnSmsMemoryModule,
       "rbnSmsMemoryFreeBytes": rbnSmsMemoryFreeBytes,
       "rbnSmsMemoryBytesInUse": rbnSmsMemoryBytesInUse,
       "rbnSmsMemoryBlocksInUse": rbnSmsMemoryBlocksInUse,
       "rbnSmsMemoryCumulBlocks": rbnSmsMemoryCumulBlocks,
       "rbnMemoryTable": rbnMemoryTable,
       "rbnMemoryEntry": rbnMemoryEntry,
       "rbnMemoryIndex": rbnMemoryIndex,
       "rbnMemoryModule": rbnMemoryModule,
       "rbnMemoryFreeKBytes": rbnMemoryFreeKBytes,
       "rbnMemoryKBytesInUse": rbnMemoryKBytesInUse,
       "rbnMemoryBlocksInUse": rbnMemoryBlocksInUse,
       "rbnMemoryCumulBlocks": rbnMemoryCumulBlocks,
       "rbnMemoryMIBConformance": rbnMemoryMIBConformance,
       "rbnSmsMemoryCompliances": rbnSmsMemoryCompliances,
       "rbnSmsMemoryCompliance": rbnSmsMemoryCompliance,
       "rbnSmsMemoryGroups": rbnSmsMemoryGroups,
       "rbnSmsMemoryGroup": rbnSmsMemoryGroup,
       "rbnMemoryCompliances": rbnMemoryCompliances,
       "rbnMemoryCompliance": rbnMemoryCompliance,
       "rbnMemoryGroups": rbnMemoryGroups,
       "rbnMemoryGroup": rbnMemoryGroup}
)
