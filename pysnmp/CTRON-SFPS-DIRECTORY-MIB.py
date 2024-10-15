# SNMP MIB module (CTRON-SFPS-DIRECTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-DIRECTORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:22 2024
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

(sfpsDirFilterAPI,
 sfpsServiceCenter,
 sfpsTopologyAliases,
 sfpsTopologyDAPI,
 sfpsTopologyDAPITest,
 sfpsTopologyDirStats,
 sfpsTopologyNodes,
 sfpsTopologyRemoteNodes) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsDirFilterAPI",
    "sfpsServiceCenter",
    "sfpsTopologyAliases",
    "sfpsTopologyDAPI",
    "sfpsTopologyDAPITest",
    "sfpsTopologyDirStats",
    "sfpsTopologyNodes",
    "sfpsTopologyRemoteNodes")

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



class SfpsSwitchPort(Integer32):
    """Custom type SfpsSwitchPort based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsServiceCenterDirectoryTable_Object = MibTable
sfpsServiceCenterDirectoryTable = _SfpsServiceCenterDirectoryTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3)
)
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryTable.setStatus("mandatory")
_SfpsServiceCenterDirectoryEntry_Object = MibTableRow
sfpsServiceCenterDirectoryEntry = _SfpsServiceCenterDirectoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1)
)
sfpsServiceCenterDirectoryEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsServiceCenterDirectoryHashLeaf"),
)
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryEntry.setStatus("mandatory")
_SfpsServiceCenterDirectoryHashLeaf_Type = HexInteger
_SfpsServiceCenterDirectoryHashLeaf_Object = MibTableColumn
sfpsServiceCenterDirectoryHashLeaf = _SfpsServiceCenterDirectoryHashLeaf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 1),
    _SfpsServiceCenterDirectoryHashLeaf_Type()
)
sfpsServiceCenterDirectoryHashLeaf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryHashLeaf.setStatus("mandatory")
_SfpsServiceCenterDirectoryMetric_Type = Integer32
_SfpsServiceCenterDirectoryMetric_Object = MibTableColumn
sfpsServiceCenterDirectoryMetric = _SfpsServiceCenterDirectoryMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 2),
    _SfpsServiceCenterDirectoryMetric_Type()
)
sfpsServiceCenterDirectoryMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryMetric.setStatus("mandatory")
_SfpsServiceCenterDirectoryName_Type = DisplayString
_SfpsServiceCenterDirectoryName_Object = MibTableColumn
sfpsServiceCenterDirectoryName = _SfpsServiceCenterDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 3),
    _SfpsServiceCenterDirectoryName_Type()
)
sfpsServiceCenterDirectoryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryName.setStatus("mandatory")


class _SfpsServiceCenterDirectoryOperStatus_Type(Integer32):
    """Custom type sfpsServiceCenterDirectoryOperStatus based on Integer32"""
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
        *(("kStatusFaulted", 4),
          ("kStatusHalted", 2),
          ("kStatusNotStarted", 5),
          ("kStatusPending", 3),
          ("kStatusRunning", 1))
    )


_SfpsServiceCenterDirectoryOperStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterDirectoryOperStatus_Object = MibTableColumn
sfpsServiceCenterDirectoryOperStatus = _SfpsServiceCenterDirectoryOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 4),
    _SfpsServiceCenterDirectoryOperStatus_Type()
)
sfpsServiceCenterDirectoryOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryOperStatus.setStatus("mandatory")


class _SfpsServiceCenterDirectoryAdminStatus_Type(Integer32):
    """Custom type sfpsServiceCenterDirectoryAdminStatus based on Integer32"""
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
          ("enable", 3),
          ("other", 1))
    )


_SfpsServiceCenterDirectoryAdminStatus_Type.__name__ = "Integer32"
_SfpsServiceCenterDirectoryAdminStatus_Object = MibTableColumn
sfpsServiceCenterDirectoryAdminStatus = _SfpsServiceCenterDirectoryAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 5),
    _SfpsServiceCenterDirectoryAdminStatus_Type()
)
sfpsServiceCenterDirectoryAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryAdminStatus.setStatus("mandatory")
_SfpsServiceCenterDirectoryStatusTime_Type = TimeTicks
_SfpsServiceCenterDirectoryStatusTime_Object = MibTableColumn
sfpsServiceCenterDirectoryStatusTime = _SfpsServiceCenterDirectoryStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 6),
    _SfpsServiceCenterDirectoryStatusTime_Type()
)
sfpsServiceCenterDirectoryStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryStatusTime.setStatus("mandatory")
_SfpsServiceCenterDirectoryRequests_Type = Integer32
_SfpsServiceCenterDirectoryRequests_Object = MibTableColumn
sfpsServiceCenterDirectoryRequests = _SfpsServiceCenterDirectoryRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 7),
    _SfpsServiceCenterDirectoryRequests_Type()
)
sfpsServiceCenterDirectoryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryRequests.setStatus("mandatory")
_SfpsServiceCenterDirectoryResponses_Type = Integer32
_SfpsServiceCenterDirectoryResponses_Object = MibTableColumn
sfpsServiceCenterDirectoryResponses = _SfpsServiceCenterDirectoryResponses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 4, 3, 1, 8),
    _SfpsServiceCenterDirectoryResponses_Type()
)
sfpsServiceCenterDirectoryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsServiceCenterDirectoryResponses.setStatus("mandatory")
_SfpsNodeTable_Object = MibTable
sfpsNodeTable = _SfpsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsNodeTable.setStatus("mandatory")
_SfpsNodeTableEntry_Object = MibTableRow
sfpsNodeTableEntry = _SfpsNodeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1)
)
sfpsNodeTableEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsNodeTableBaseHash"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsNodeTableHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsNodeTableEntry.setStatus("mandatory")
_SfpsNodeTableBaseHash_Type = Integer32
_SfpsNodeTableBaseHash_Object = MibTableColumn
sfpsNodeTableBaseHash = _SfpsNodeTableBaseHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 1),
    _SfpsNodeTableBaseHash_Type()
)
sfpsNodeTableBaseHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableBaseHash.setStatus("mandatory")
_SfpsNodeTableHashIndex_Type = Integer32
_SfpsNodeTableHashIndex_Object = MibTableColumn
sfpsNodeTableHashIndex = _SfpsNodeTableHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 2),
    _SfpsNodeTableHashIndex_Type()
)
sfpsNodeTableHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableHashIndex.setStatus("mandatory")
_SfpsNodeTableSwitchType_Type = DisplayString
_SfpsNodeTableSwitchType_Object = MibTableColumn
sfpsNodeTableSwitchType = _SfpsNodeTableSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 3),
    _SfpsNodeTableSwitchType_Type()
)
sfpsNodeTableSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableSwitchType.setStatus("mandatory")
_SfpsNodeTableSwitchAddress_Type = DisplayString
_SfpsNodeTableSwitchAddress_Object = MibTableColumn
sfpsNodeTableSwitchAddress = _SfpsNodeTableSwitchAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 4),
    _SfpsNodeTableSwitchAddress_Type()
)
sfpsNodeTableSwitchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableSwitchAddress.setStatus("mandatory")
_SfpsNodeTablePort_Type = Integer32
_SfpsNodeTablePort_Object = MibTableColumn
sfpsNodeTablePort = _SfpsNodeTablePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 5),
    _SfpsNodeTablePort_Type()
)
sfpsNodeTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTablePort.setStatus("mandatory")
_SfpsNodeTableBaseType_Type = DisplayString
_SfpsNodeTableBaseType_Object = MibTableColumn
sfpsNodeTableBaseType = _SfpsNodeTableBaseType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 6),
    _SfpsNodeTableBaseType_Type()
)
sfpsNodeTableBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableBaseType.setStatus("mandatory")
_SfpsNodeTableBaseAddress_Type = DisplayString
_SfpsNodeTableBaseAddress_Object = MibTableColumn
sfpsNodeTableBaseAddress = _SfpsNodeTableBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 7),
    _SfpsNodeTableBaseAddress_Type()
)
sfpsNodeTableBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableBaseAddress.setStatus("mandatory")
_SfpsNodeTableEntryType_Type = DisplayString
_SfpsNodeTableEntryType_Object = MibTableColumn
sfpsNodeTableEntryType = _SfpsNodeTableEntryType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 8),
    _SfpsNodeTableEntryType_Type()
)
sfpsNodeTableEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableEntryType.setStatus("mandatory")
_SfpsNodeTableCallTag_Type = HexInteger
_SfpsNodeTableCallTag_Object = MibTableColumn
sfpsNodeTableCallTag = _SfpsNodeTableCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 9),
    _SfpsNodeTableCallTag_Type()
)
sfpsNodeTableCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableCallTag.setStatus("mandatory")
_SfpsNodeTableLastHeard_Type = TimeTicks
_SfpsNodeTableLastHeard_Object = MibTableColumn
sfpsNodeTableLastHeard = _SfpsNodeTableLastHeard_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 10),
    _SfpsNodeTableLastHeard_Type()
)
sfpsNodeTableLastHeard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableLastHeard.setStatus("mandatory")
_SfpsNodeTableAge_Type = TimeTicks
_SfpsNodeTableAge_Object = MibTableColumn
sfpsNodeTableAge = _SfpsNodeTableAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 11),
    _SfpsNodeTableAge_Type()
)
sfpsNodeTableAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableAge.setStatus("mandatory")
_SfpsNodeTableAliasCount_Type = Integer32
_SfpsNodeTableAliasCount_Object = MibTableColumn
sfpsNodeTableAliasCount = _SfpsNodeTableAliasCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 12),
    _SfpsNodeTableAliasCount_Type()
)
sfpsNodeTableAliasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableAliasCount.setStatus("mandatory")
_SfpsNodeTableVlanCount_Type = Integer32
_SfpsNodeTableVlanCount_Object = MibTableColumn
sfpsNodeTableVlanCount = _SfpsNodeTableVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 13),
    _SfpsNodeTableVlanCount_Type()
)
sfpsNodeTableVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableVlanCount.setStatus("mandatory")


class _SfpsNodeTableNodeLocked_Type(Integer32):
    """Custom type sfpsNodeTableNodeLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsNodeTableNodeLocked_Type.__name__ = "Integer32"
_SfpsNodeTableNodeLocked_Object = MibTableColumn
sfpsNodeTableNodeLocked = _SfpsNodeTableNodeLocked_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 14),
    _SfpsNodeTableNodeLocked_Type()
)
sfpsNodeTableNodeLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableNodeLocked.setStatus("mandatory")


class _SfpsNodeTableNodeLocal_Type(Integer32):
    """Custom type sfpsNodeTableNodeLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsNodeTableNodeLocal_Type.__name__ = "Integer32"
_SfpsNodeTableNodeLocal_Object = MibTableColumn
sfpsNodeTableNodeLocal = _SfpsNodeTableNodeLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 15),
    _SfpsNodeTableNodeLocal_Type()
)
sfpsNodeTableNodeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableNodeLocal.setStatus("mandatory")
_SfpsNodeTableSelf_Type = Integer32
_SfpsNodeTableSelf_Object = MibTableColumn
sfpsNodeTableSelf = _SfpsNodeTableSelf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 16),
    _SfpsNodeTableSelf_Type()
)
sfpsNodeTableSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableSelf.setStatus("mandatory")
_SfpsNodeTableNext_Type = Integer32
_SfpsNodeTableNext_Object = MibTableColumn
sfpsNodeTableNext = _SfpsNodeTableNext_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 17),
    _SfpsNodeTableNext_Type()
)
sfpsNodeTableNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTableNext.setStatus("mandatory")
_SfpsNodeTablePrev_Type = Integer32
_SfpsNodeTablePrev_Object = MibTableColumn
sfpsNodeTablePrev = _SfpsNodeTablePrev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 5, 1, 1, 18),
    _SfpsNodeTablePrev_Type()
)
sfpsNodeTablePrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsNodeTablePrev.setStatus("mandatory")
_SfpsAliasTable_Object = MibTable
sfpsAliasTable = _SfpsAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1)
)
if mibBuilder.loadTexts:
    sfpsAliasTable.setStatus("mandatory")
_SfpsAliasTableEntry_Object = MibTableRow
sfpsAliasTableEntry = _SfpsAliasTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1)
)
sfpsAliasTableEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsAliasTableAliasHash"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsAliasTableBaseHash"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsAliasTableHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsAliasTableEntry.setStatus("mandatory")
_SfpsAliasTableAliasHash_Type = Integer32
_SfpsAliasTableAliasHash_Object = MibTableColumn
sfpsAliasTableAliasHash = _SfpsAliasTableAliasHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 1),
    _SfpsAliasTableAliasHash_Type()
)
sfpsAliasTableAliasHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasHash.setStatus("mandatory")
_SfpsAliasTableBaseHash_Type = Integer32
_SfpsAliasTableBaseHash_Object = MibTableColumn
sfpsAliasTableBaseHash = _SfpsAliasTableBaseHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 2),
    _SfpsAliasTableBaseHash_Type()
)
sfpsAliasTableBaseHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableBaseHash.setStatus("mandatory")
_SfpsAliasTableHashIndex_Type = Integer32
_SfpsAliasTableHashIndex_Object = MibTableColumn
sfpsAliasTableHashIndex = _SfpsAliasTableHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 3),
    _SfpsAliasTableHashIndex_Type()
)
sfpsAliasTableHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableHashIndex.setStatus("mandatory")
_SfpsAliasTableSwitchType_Type = DisplayString
_SfpsAliasTableSwitchType_Object = MibTableColumn
sfpsAliasTableSwitchType = _SfpsAliasTableSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 4),
    _SfpsAliasTableSwitchType_Type()
)
sfpsAliasTableSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableSwitchType.setStatus("mandatory")
_SfpsAliasTableSwitchAddress_Type = DisplayString
_SfpsAliasTableSwitchAddress_Object = MibTableColumn
sfpsAliasTableSwitchAddress = _SfpsAliasTableSwitchAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 5),
    _SfpsAliasTableSwitchAddress_Type()
)
sfpsAliasTableSwitchAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableSwitchAddress.setStatus("mandatory")
_SfpsAliasTablePort_Type = Integer32
_SfpsAliasTablePort_Object = MibTableColumn
sfpsAliasTablePort = _SfpsAliasTablePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 6),
    _SfpsAliasTablePort_Type()
)
sfpsAliasTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTablePort.setStatus("mandatory")
_SfpsAliasTableBaseType_Type = DisplayString
_SfpsAliasTableBaseType_Object = MibTableColumn
sfpsAliasTableBaseType = _SfpsAliasTableBaseType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 7),
    _SfpsAliasTableBaseType_Type()
)
sfpsAliasTableBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableBaseType.setStatus("mandatory")
_SfpsAliasTableBaseAddress_Type = DisplayString
_SfpsAliasTableBaseAddress_Object = MibTableColumn
sfpsAliasTableBaseAddress = _SfpsAliasTableBaseAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 8),
    _SfpsAliasTableBaseAddress_Type()
)
sfpsAliasTableBaseAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableBaseAddress.setStatus("mandatory")
_SfpsAliasTableAliasType_Type = DisplayString
_SfpsAliasTableAliasType_Object = MibTableColumn
sfpsAliasTableAliasType = _SfpsAliasTableAliasType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 9),
    _SfpsAliasTableAliasType_Type()
)
sfpsAliasTableAliasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasType.setStatus("mandatory")
_SfpsAliasTableAliasAddress_Type = DisplayString
_SfpsAliasTableAliasAddress_Object = MibTableColumn
sfpsAliasTableAliasAddress = _SfpsAliasTableAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 10),
    _SfpsAliasTableAliasAddress_Type()
)
sfpsAliasTableAliasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasAddress.setStatus("mandatory")
_SfpsAliasTableAliasAge_Type = TimeTicks
_SfpsAliasTableAliasAge_Object = MibTableColumn
sfpsAliasTableAliasAge = _SfpsAliasTableAliasAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 11),
    _SfpsAliasTableAliasAge_Type()
)
sfpsAliasTableAliasAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasAge.setStatus("mandatory")
_SfpsAliasTableSwitchOctets_Type = OctetString
_SfpsAliasTableSwitchOctets_Object = MibTableColumn
sfpsAliasTableSwitchOctets = _SfpsAliasTableSwitchOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 12),
    _SfpsAliasTableSwitchOctets_Type()
)
sfpsAliasTableSwitchOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableSwitchOctets.setStatus("mandatory")
_SfpsAliasTableBaseOctets_Type = OctetString
_SfpsAliasTableBaseOctets_Object = MibTableColumn
sfpsAliasTableBaseOctets = _SfpsAliasTableBaseOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 13),
    _SfpsAliasTableBaseOctets_Type()
)
sfpsAliasTableBaseOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableBaseOctets.setStatus("mandatory")
_SfpsAliasTableAliasOctets_Type = OctetString
_SfpsAliasTableAliasOctets_Object = MibTableColumn
sfpsAliasTableAliasOctets = _SfpsAliasTableAliasOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 14),
    _SfpsAliasTableAliasOctets_Type()
)
sfpsAliasTableAliasOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasOctets.setStatus("mandatory")
_SfpsAliasTableOpaqueTag_Type = OctetString
_SfpsAliasTableOpaqueTag_Object = MibTableColumn
sfpsAliasTableOpaqueTag = _SfpsAliasTableOpaqueTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 15),
    _SfpsAliasTableOpaqueTag_Type()
)
sfpsAliasTableOpaqueTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableOpaqueTag.setStatus("mandatory")


class _SfpsAliasTableVlanPolicy_Type(Integer32):
    """Custom type sfpsAliasTableVlanPolicy based on Integer32"""
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
        *(("autoRegistered", 3),
          ("inherited", 2),
          ("other", 1),
          ("static", 4))
    )


_SfpsAliasTableVlanPolicy_Type.__name__ = "Integer32"
_SfpsAliasTableVlanPolicy_Object = MibTableColumn
sfpsAliasTableVlanPolicy = _SfpsAliasTableVlanPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 16),
    _SfpsAliasTableVlanPolicy_Type()
)
sfpsAliasTableVlanPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableVlanPolicy.setStatus("mandatory")


class _SfpsAliasTableBaseLock_Type(Integer32):
    """Custom type sfpsAliasTableBaseLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsAliasTableBaseLock_Type.__name__ = "Integer32"
_SfpsAliasTableBaseLock_Object = MibTableColumn
sfpsAliasTableBaseLock = _SfpsAliasTableBaseLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 17),
    _SfpsAliasTableBaseLock_Type()
)
sfpsAliasTableBaseLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableBaseLock.setStatus("mandatory")


class _SfpsAliasTableAliasLock_Type(Integer32):
    """Custom type sfpsAliasTableAliasLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsAliasTableAliasLock_Type.__name__ = "Integer32"
_SfpsAliasTableAliasLock_Object = MibTableColumn
sfpsAliasTableAliasLock = _SfpsAliasTableAliasLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 18),
    _SfpsAliasTableAliasLock_Type()
)
sfpsAliasTableAliasLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasLock.setStatus("mandatory")


class _SfpsAliasTableAliasState_Type(Integer32):
    """Custom type sfpsAliasTableAliasState based on Integer32"""
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
        *(("hidden", 4),
          ("local", 3),
          ("other", 1),
          ("remote", 2))
    )


_SfpsAliasTableAliasState_Type.__name__ = "Integer32"
_SfpsAliasTableAliasState_Object = MibTableColumn
sfpsAliasTableAliasState = _SfpsAliasTableAliasState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 19),
    _SfpsAliasTableAliasState_Type()
)
sfpsAliasTableAliasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableAliasState.setStatus("mandatory")
_SfpsAliasTableSelf_Type = Integer32
_SfpsAliasTableSelf_Object = MibTableColumn
sfpsAliasTableSelf = _SfpsAliasTableSelf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 20),
    _SfpsAliasTableSelf_Type()
)
sfpsAliasTableSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableSelf.setStatus("mandatory")
_SfpsAliasTableNext_Type = Integer32
_SfpsAliasTableNext_Object = MibTableColumn
sfpsAliasTableNext = _SfpsAliasTableNext_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 21),
    _SfpsAliasTableNext_Type()
)
sfpsAliasTableNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTableNext.setStatus("mandatory")
_SfpsAliasTablePrev_Type = Integer32
_SfpsAliasTablePrev_Object = MibTableColumn
sfpsAliasTablePrev = _SfpsAliasTablePrev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 1, 1, 22),
    _SfpsAliasTablePrev_Type()
)
sfpsAliasTablePrev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasTablePrev.setStatus("mandatory")
_SfpsAliasDeltaTable_Object = MibTable
sfpsAliasDeltaTable = _SfpsAliasDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2)
)
if mibBuilder.loadTexts:
    sfpsAliasDeltaTable.setStatus("mandatory")
_SfpsAliasDeltaTableEntry_Object = MibTableRow
sfpsAliasDeltaTableEntry = _SfpsAliasDeltaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1)
)
sfpsAliasDeltaTableEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsAliasDeltaTableIndex"),
)
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableEntry.setStatus("mandatory")
_SfpsAliasDeltaTableIndex_Type = Integer32
_SfpsAliasDeltaTableIndex_Object = MibTableColumn
sfpsAliasDeltaTableIndex = _SfpsAliasDeltaTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 1),
    _SfpsAliasDeltaTableIndex_Type()
)
sfpsAliasDeltaTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableIndex.setStatus("mandatory")
_SfpsAliasDeltaTablePort_Type = Integer32
_SfpsAliasDeltaTablePort_Object = MibTableColumn
sfpsAliasDeltaTablePort = _SfpsAliasDeltaTablePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 2),
    _SfpsAliasDeltaTablePort_Type()
)
sfpsAliasDeltaTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTablePort.setStatus("mandatory")
_SfpsAliasDeltaTableBase_Type = SfpsAddress
_SfpsAliasDeltaTableBase_Object = MibTableColumn
sfpsAliasDeltaTableBase = _SfpsAliasDeltaTableBase_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 3),
    _SfpsAliasDeltaTableBase_Type()
)
sfpsAliasDeltaTableBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableBase.setStatus("mandatory")
_SfpsAliasDeltaTableAlias_Type = OctetString
_SfpsAliasDeltaTableAlias_Object = MibTableColumn
sfpsAliasDeltaTableAlias = _SfpsAliasDeltaTableAlias_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 4),
    _SfpsAliasDeltaTableAlias_Type()
)
sfpsAliasDeltaTableAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableAlias.setStatus("mandatory")
_SfpsAliasDeltaTableAliasLength_Type = Integer32
_SfpsAliasDeltaTableAliasLength_Object = MibTableColumn
sfpsAliasDeltaTableAliasLength = _SfpsAliasDeltaTableAliasLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 5),
    _SfpsAliasDeltaTableAliasLength_Type()
)
sfpsAliasDeltaTableAliasLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableAliasLength.setStatus("mandatory")
_SfpsAliasDeltaTableOpaqueTag_Type = OctetString
_SfpsAliasDeltaTableOpaqueTag_Object = MibTableColumn
sfpsAliasDeltaTableOpaqueTag = _SfpsAliasDeltaTableOpaqueTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 6),
    _SfpsAliasDeltaTableOpaqueTag_Type()
)
sfpsAliasDeltaTableOpaqueTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableOpaqueTag.setStatus("mandatory")


class _SfpsAliasDeltaTableAliasState_Type(Integer32):
    """Custom type sfpsAliasDeltaTableAliasState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("added", 2),
          ("deleted", 3),
          ("other", 1))
    )


_SfpsAliasDeltaTableAliasState_Type.__name__ = "Integer32"
_SfpsAliasDeltaTableAliasState_Object = MibTableColumn
sfpsAliasDeltaTableAliasState = _SfpsAliasDeltaTableAliasState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 7),
    _SfpsAliasDeltaTableAliasState_Type()
)
sfpsAliasDeltaTableAliasState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableAliasState.setStatus("mandatory")


class _SfpsAliasDeltaTableNodeLock_Type(Integer32):
    """Custom type sfpsAliasDeltaTableNodeLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_SfpsAliasDeltaTableNodeLock_Type.__name__ = "Integer32"
_SfpsAliasDeltaTableNodeLock_Object = MibTableColumn
sfpsAliasDeltaTableNodeLock = _SfpsAliasDeltaTableNodeLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 8),
    _SfpsAliasDeltaTableNodeLock_Type()
)
sfpsAliasDeltaTableNodeLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableNodeLock.setStatus("mandatory")


class _SfpsAliasDeltaTableAliasLock_Type(Integer32):
    """Custom type sfpsAliasDeltaTableAliasLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )


_SfpsAliasDeltaTableAliasLock_Type.__name__ = "Integer32"
_SfpsAliasDeltaTableAliasLock_Object = MibTableColumn
sfpsAliasDeltaTableAliasLock = _SfpsAliasDeltaTableAliasLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 9),
    _SfpsAliasDeltaTableAliasLock_Type()
)
sfpsAliasDeltaTableAliasLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableAliasLock.setStatus("mandatory")
_SfpsAliasDeltaTableTimestamp_Type = TimeTicks
_SfpsAliasDeltaTableTimestamp_Object = MibTableColumn
sfpsAliasDeltaTableTimestamp = _SfpsAliasDeltaTableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 2, 1, 10),
    _SfpsAliasDeltaTableTimestamp_Type()
)
sfpsAliasDeltaTableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaTableTimestamp.setStatus("mandatory")
_SfpsAliasDeltaCount_Type = Integer32
_SfpsAliasDeltaCount_Object = MibScalar
sfpsAliasDeltaCount = _SfpsAliasDeltaCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 3),
    _SfpsAliasDeltaCount_Type()
)
sfpsAliasDeltaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaCount.setStatus("mandatory")


class _SfpsAliasDeltaSetBack_Type(Integer32):
    """Custom type sfpsAliasDeltaSetBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unlock", 2))
    )


_SfpsAliasDeltaSetBack_Type.__name__ = "Integer32"
_SfpsAliasDeltaSetBack_Object = MibScalar
sfpsAliasDeltaSetBack = _SfpsAliasDeltaSetBack_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 4),
    _SfpsAliasDeltaSetBack_Type()
)
sfpsAliasDeltaSetBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsAliasDeltaSetBack.setStatus("mandatory")


class _SfpsAliasDeltaFullFlag_Type(Integer32):
    """Custom type sfpsAliasDeltaFullFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("unfull", 2))
    )


_SfpsAliasDeltaFullFlag_Type.__name__ = "Integer32"
_SfpsAliasDeltaFullFlag_Object = MibScalar
sfpsAliasDeltaFullFlag = _SfpsAliasDeltaFullFlag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 6, 5),
    _SfpsAliasDeltaFullFlag_Type()
)
sfpsAliasDeltaFullFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAliasDeltaFullFlag.setStatus("mandatory")


class _SfpsDAPITestVerb_Type(Integer32):
    """Custom type sfpsDAPITestVerb based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("ageDirectory", 7),
          ("delete", 3),
          ("fillDirectory", 6),
          ("mapVlanOffPort", 9),
          ("mapVlanOnPort", 8),
          ("multiResolve", 5),
          ("other", 1),
          ("resolve", 4))
    )


_SfpsDAPITestVerb_Type.__name__ = "Integer32"
_SfpsDAPITestVerb_Object = MibScalar
sfpsDAPITestVerb = _SfpsDAPITestVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 1),
    _SfpsDAPITestVerb_Type()
)
sfpsDAPITestVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestVerb.setStatus("mandatory")
_SfpsDAPITestSwitchMac_Type = SfpsAddress
_SfpsDAPITestSwitchMac_Object = MibScalar
sfpsDAPITestSwitchMac = _SfpsDAPITestSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 2),
    _SfpsDAPITestSwitchMac_Type()
)
sfpsDAPITestSwitchMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestSwitchMac.setStatus("mandatory")
_SfpsDAPITestPort_Type = SfpsSwitchPort
_SfpsDAPITestPort_Object = MibScalar
sfpsDAPITestPort = _SfpsDAPITestPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 3),
    _SfpsDAPITestPort_Type()
)
sfpsDAPITestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestPort.setStatus("mandatory")


class _SfpsDAPITestAddrOneTag_Type(Integer32):
    """Custom type sfpsDAPITestAddrOneTag based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("atDDP", 11),
          ("empty", 12),
          ("hostName", 14),
          ("inetIP", 7),
          ("inetIPMask", 16),
          ("inetRIP", 9),
          ("inetRPC", 8),
          ("inetUDP", 5),
          ("inetYP", 4),
          ("ipxIpx", 6),
          ("ipxRIP", 3),
          ("ipxRip8022", 20),
          ("ipxRipEnet", 22),
          ("ipxRipSnap", 21),
          ("ipxSap", 2),
          ("ipxSap8022", 17),
          ("ipxSapEnet", 19),
          ("ipxSapSnap", 18),
          ("macDX", 1),
          ("macDXMcast", 10),
          ("netBiosName", 15),
          ("vlan", 13))
    )


_SfpsDAPITestAddrOneTag_Type.__name__ = "Integer32"
_SfpsDAPITestAddrOneTag_Object = MibScalar
sfpsDAPITestAddrOneTag = _SfpsDAPITestAddrOneTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 4),
    _SfpsDAPITestAddrOneTag_Type()
)
sfpsDAPITestAddrOneTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestAddrOneTag.setStatus("mandatory")
_SfpsDAPITestAddrOneValue_Type = DisplayString
_SfpsDAPITestAddrOneValue_Object = MibScalar
sfpsDAPITestAddrOneValue = _SfpsDAPITestAddrOneValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 5),
    _SfpsDAPITestAddrOneValue_Type()
)
sfpsDAPITestAddrOneValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestAddrOneValue.setStatus("mandatory")


class _SfpsDAPITestAddrTwoTag_Type(Integer32):
    """Custom type sfpsDAPITestAddrTwoTag based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("atDDP", 11),
          ("empty", 12),
          ("hostName", 14),
          ("inetIP", 7),
          ("inetIPMask", 16),
          ("inetRIP", 9),
          ("inetRPC", 8),
          ("inetUDP", 5),
          ("inetYP", 4),
          ("ipxIpx", 6),
          ("ipxRIP", 3),
          ("ipxRip8022", 20),
          ("ipxRipEnet", 22),
          ("ipxRipSnap", 21),
          ("ipxSap", 2),
          ("ipxSap8022", 17),
          ("ipxSapEnet", 19),
          ("ipxSapSnap", 18),
          ("macDX", 1),
          ("macDXMcast", 10),
          ("netBiosName", 15),
          ("vlan", 13))
    )


_SfpsDAPITestAddrTwoTag_Type.__name__ = "Integer32"
_SfpsDAPITestAddrTwoTag_Object = MibScalar
sfpsDAPITestAddrTwoTag = _SfpsDAPITestAddrTwoTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 6),
    _SfpsDAPITestAddrTwoTag_Type()
)
sfpsDAPITestAddrTwoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestAddrTwoTag.setStatus("mandatory")
_SfpsDAPITestAddrTwoValue_Type = DisplayString
_SfpsDAPITestAddrTwoValue_Object = MibScalar
sfpsDAPITestAddrTwoValue = _SfpsDAPITestAddrTwoValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 7),
    _SfpsDAPITestAddrTwoValue_Type()
)
sfpsDAPITestAddrTwoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestAddrTwoValue.setStatus("mandatory")
_SfpsDAPITestCallTag_Type = Integer32
_SfpsDAPITestCallTag_Object = MibScalar
sfpsDAPITestCallTag = _SfpsDAPITestCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 8),
    _SfpsDAPITestCallTag_Type()
)
sfpsDAPITestCallTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPITestCallTag.setStatus("mandatory")
_SfpsDAPITestOutputTable_Object = MibTable
sfpsDAPITestOutputTable = _SfpsDAPITestOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9)
)
if mibBuilder.loadTexts:
    sfpsDAPITestOutputTable.setStatus("mandatory")
_SfpsDAPITestOutputEntry_Object = MibTableRow
sfpsDAPITestOutputEntry = _SfpsDAPITestOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1)
)
sfpsDAPITestOutputEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDAPITestOutputIndex"),
)
if mibBuilder.loadTexts:
    sfpsDAPITestOutputEntry.setStatus("mandatory")
_SfpsDAPITestOutputIndex_Type = Integer32
_SfpsDAPITestOutputIndex_Object = MibTableColumn
sfpsDAPITestOutputIndex = _SfpsDAPITestOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 1),
    _SfpsDAPITestOutputIndex_Type()
)
sfpsDAPITestOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputIndex.setStatus("mandatory")
_SfpsDAPITestOutputSwitchMac_Type = SfpsAddress
_SfpsDAPITestOutputSwitchMac_Object = MibTableColumn
sfpsDAPITestOutputSwitchMac = _SfpsDAPITestOutputSwitchMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 2),
    _SfpsDAPITestOutputSwitchMac_Type()
)
sfpsDAPITestOutputSwitchMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputSwitchMac.setStatus("mandatory")
_SfpsDAPITestOutputPort_Type = Integer32
_SfpsDAPITestOutputPort_Object = MibTableColumn
sfpsDAPITestOutputPort = _SfpsDAPITestOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 3),
    _SfpsDAPITestOutputPort_Type()
)
sfpsDAPITestOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputPort.setStatus("mandatory")


class _SfpsDAPITestOutputAddrOneTag_Type(Integer32):
    """Custom type sfpsDAPITestOutputAddrOneTag based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("atDDP", 11),
          ("empty", 12),
          ("hostName", 14),
          ("inetIP", 7),
          ("inetIPMask", 16),
          ("inetRIP", 9),
          ("inetRPC", 8),
          ("inetUDP", 5),
          ("inetYP", 4),
          ("ipxIpx", 6),
          ("ipxRIP", 3),
          ("ipxRip8022", 20),
          ("ipxRipEnet", 22),
          ("ipxRipSnap", 21),
          ("ipxSap", 2),
          ("ipxSap8022", 17),
          ("ipxSapEnet", 19),
          ("ipxSapSnap", 18),
          ("macDX", 1),
          ("macDXMcast", 10),
          ("netBiosName", 15),
          ("vlan", 13))
    )


_SfpsDAPITestOutputAddrOneTag_Type.__name__ = "Integer32"
_SfpsDAPITestOutputAddrOneTag_Object = MibTableColumn
sfpsDAPITestOutputAddrOneTag = _SfpsDAPITestOutputAddrOneTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 4),
    _SfpsDAPITestOutputAddrOneTag_Type()
)
sfpsDAPITestOutputAddrOneTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputAddrOneTag.setStatus("mandatory")
_SfpsDAPITestOutputAddrOneValue_Type = DisplayString
_SfpsDAPITestOutputAddrOneValue_Object = MibTableColumn
sfpsDAPITestOutputAddrOneValue = _SfpsDAPITestOutputAddrOneValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 5),
    _SfpsDAPITestOutputAddrOneValue_Type()
)
sfpsDAPITestOutputAddrOneValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputAddrOneValue.setStatus("mandatory")


class _SfpsDAPITestOutputAddrTwoTag_Type(Integer32):
    """Custom type sfpsDAPITestOutputAddrTwoTag based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("atDDP", 11),
          ("empty", 12),
          ("hostName", 14),
          ("inetIP", 7),
          ("inetIPMask", 16),
          ("inetRIP", 9),
          ("inetRPC", 8),
          ("inetUDP", 5),
          ("inetYP", 4),
          ("ipxIpx", 6),
          ("ipxRIP", 3),
          ("ipxRip8022", 20),
          ("ipxRipEnet", 22),
          ("ipxRipSnap", 21),
          ("ipxSap", 2),
          ("ipxSap8022", 17),
          ("ipxSapEnet", 19),
          ("ipxSapSnap", 18),
          ("macDX", 1),
          ("macDXMcast", 10),
          ("netBiosName", 15),
          ("vlan", 13))
    )


_SfpsDAPITestOutputAddrTwoTag_Type.__name__ = "Integer32"
_SfpsDAPITestOutputAddrTwoTag_Object = MibTableColumn
sfpsDAPITestOutputAddrTwoTag = _SfpsDAPITestOutputAddrTwoTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 6),
    _SfpsDAPITestOutputAddrTwoTag_Type()
)
sfpsDAPITestOutputAddrTwoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputAddrTwoTag.setStatus("mandatory")
_SfpsDAPITestOutputAddrTwoValue_Type = DisplayString
_SfpsDAPITestOutputAddrTwoValue_Object = MibTableColumn
sfpsDAPITestOutputAddrTwoValue = _SfpsDAPITestOutputAddrTwoValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 7),
    _SfpsDAPITestOutputAddrTwoValue_Type()
)
sfpsDAPITestOutputAddrTwoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputAddrTwoValue.setStatus("mandatory")
_SfpsDAPITestOutputCallTag_Type = Integer32
_SfpsDAPITestOutputCallTag_Object = MibTableColumn
sfpsDAPITestOutputCallTag = _SfpsDAPITestOutputCallTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 9, 9, 1, 8),
    _SfpsDAPITestOutputCallTag_Type()
)
sfpsDAPITestOutputCallTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDAPITestOutputCallTag.setStatus("mandatory")


class _SfpsDAPIVerb_Type(Integer32):
    """Custom type sfpsDAPIVerb based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("ageAliases", 12),
          ("ageNodes", 11),
          ("clearPort", 4),
          ("clearPortLocals", 5),
          ("clearSwitchRefs", 6),
          ("delete", 3),
          ("lockNode", 7),
          ("other", 1),
          ("restrictPort", 9),
          ("unlockNode", 8),
          ("unrestrictPort", 10))
    )


_SfpsDAPIVerb_Type.__name__ = "Integer32"
_SfpsDAPIVerb_Object = MibScalar
sfpsDAPIVerb = _SfpsDAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 1),
    _SfpsDAPIVerb_Type()
)
sfpsDAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPIVerb.setStatus("mandatory")
_SfpsDAPIPort_Type = Integer32
_SfpsDAPIPort_Object = MibScalar
sfpsDAPIPort = _SfpsDAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 2),
    _SfpsDAPIPort_Type()
)
sfpsDAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPIPort.setStatus("mandatory")
_SfpsDAPINodeType_Type = OctetString
_SfpsDAPINodeType_Object = MibScalar
sfpsDAPINodeType = _SfpsDAPINodeType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 3),
    _SfpsDAPINodeType_Type()
)
sfpsDAPINodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPINodeType.setStatus("mandatory")
_SfpsDAPINodeValue_Type = OctetString
_SfpsDAPINodeValue_Object = MibScalar
sfpsDAPINodeValue = _SfpsDAPINodeValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 4),
    _SfpsDAPINodeValue_Type()
)
sfpsDAPINodeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPINodeValue.setStatus("mandatory")
_SfpsDAPIAliasType_Type = OctetString
_SfpsDAPIAliasType_Object = MibScalar
sfpsDAPIAliasType = _SfpsDAPIAliasType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 5),
    _SfpsDAPIAliasType_Type()
)
sfpsDAPIAliasType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPIAliasType.setStatus("mandatory")
_SfpsDAPIAliasValue_Type = OctetString
_SfpsDAPIAliasValue_Object = MibScalar
sfpsDAPIAliasValue = _SfpsDAPIAliasValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 6),
    _SfpsDAPIAliasValue_Type()
)
sfpsDAPIAliasValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPIAliasValue.setStatus("mandatory")
_SfpsDAPIAge_Type = Integer32
_SfpsDAPIAge_Object = MibScalar
sfpsDAPIAge = _SfpsDAPIAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 10, 7),
    _SfpsDAPIAge_Type()
)
sfpsDAPIAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDAPIAge.setStatus("mandatory")
_SfpsTopologyDirStatsTotalUsage_Type = Integer32
_SfpsTopologyDirStatsTotalUsage_Object = MibScalar
sfpsTopologyDirStatsTotalUsage = _SfpsTopologyDirStatsTotalUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 1),
    _SfpsTopologyDirStatsTotalUsage_Type()
)
sfpsTopologyDirStatsTotalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsTotalUsage.setStatus("mandatory")
_SfpsTopologyDirStatsDynamicUsage_Type = Integer32
_SfpsTopologyDirStatsDynamicUsage_Object = MibScalar
sfpsTopologyDirStatsDynamicUsage = _SfpsTopologyDirStatsDynamicUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 2),
    _SfpsTopologyDirStatsDynamicUsage_Type()
)
sfpsTopologyDirStatsDynamicUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsDynamicUsage.setStatus("mandatory")
_SfpsTopologyDirStatsNumOfNodes_Type = Integer32
_SfpsTopologyDirStatsNumOfNodes_Object = MibScalar
sfpsTopologyDirStatsNumOfNodes = _SfpsTopologyDirStatsNumOfNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 3),
    _SfpsTopologyDirStatsNumOfNodes_Type()
)
sfpsTopologyDirStatsNumOfNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumOfNodes.setStatus("mandatory")
_SfpsTopologyDirStatsNodeUsage_Type = Integer32
_SfpsTopologyDirStatsNodeUsage_Object = MibScalar
sfpsTopologyDirStatsNodeUsage = _SfpsTopologyDirStatsNodeUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 4),
    _SfpsTopologyDirStatsNodeUsage_Type()
)
sfpsTopologyDirStatsNodeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeUsage.setStatus("mandatory")
_SfpsTopologyDirStatsNumLocalNodes_Type = Integer32
_SfpsTopologyDirStatsNumLocalNodes_Object = MibScalar
sfpsTopologyDirStatsNumLocalNodes = _SfpsTopologyDirStatsNumLocalNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 5),
    _SfpsTopologyDirStatsNumLocalNodes_Type()
)
sfpsTopologyDirStatsNumLocalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumLocalNodes.setStatus("mandatory")
_SfpsTopologyDirStatsLocalNodeUsage_Type = Integer32
_SfpsTopologyDirStatsLocalNodeUsage_Object = MibScalar
sfpsTopologyDirStatsLocalNodeUsage = _SfpsTopologyDirStatsLocalNodeUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 6),
    _SfpsTopologyDirStatsLocalNodeUsage_Type()
)
sfpsTopologyDirStatsLocalNodeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsLocalNodeUsage.setStatus("mandatory")
_SfpsTopologyDirStatsMaxLocalNodes_Type = Integer32
_SfpsTopologyDirStatsMaxLocalNodes_Object = MibScalar
sfpsTopologyDirStatsMaxLocalNodes = _SfpsTopologyDirStatsMaxLocalNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 7),
    _SfpsTopologyDirStatsMaxLocalNodes_Type()
)
sfpsTopologyDirStatsMaxLocalNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsMaxLocalNodes.setStatus("mandatory")
_SfpsTopologyDirStatsNumRemoteNodes_Type = Integer32
_SfpsTopologyDirStatsNumRemoteNodes_Object = MibScalar
sfpsTopologyDirStatsNumRemoteNodes = _SfpsTopologyDirStatsNumRemoteNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 8),
    _SfpsTopologyDirStatsNumRemoteNodes_Type()
)
sfpsTopologyDirStatsNumRemoteNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumRemoteNodes.setStatus("mandatory")
_SfpsTopologyDirStatsRemoteNodeUsage_Type = Integer32
_SfpsTopologyDirStatsRemoteNodeUsage_Object = MibScalar
sfpsTopologyDirStatsRemoteNodeUsage = _SfpsTopologyDirStatsRemoteNodeUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 9),
    _SfpsTopologyDirStatsRemoteNodeUsage_Type()
)
sfpsTopologyDirStatsRemoteNodeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsRemoteNodeUsage.setStatus("mandatory")
_SfpsTopologyDirStatsMaxRemoteNodes_Type = Integer32
_SfpsTopologyDirStatsMaxRemoteNodes_Object = MibScalar
sfpsTopologyDirStatsMaxRemoteNodes = _SfpsTopologyDirStatsMaxRemoteNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 10),
    _SfpsTopologyDirStatsMaxRemoteNodes_Type()
)
sfpsTopologyDirStatsMaxRemoteNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsMaxRemoteNodes.setStatus("mandatory")
_SfpsTopologyDirStatsNumOfAliases_Type = Integer32
_SfpsTopologyDirStatsNumOfAliases_Object = MibScalar
sfpsTopologyDirStatsNumOfAliases = _SfpsTopologyDirStatsNumOfAliases_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 11),
    _SfpsTopologyDirStatsNumOfAliases_Type()
)
sfpsTopologyDirStatsNumOfAliases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumOfAliases.setStatus("mandatory")
_SfpsTopologyDirStatsAliasUsage_Type = Integer32
_SfpsTopologyDirStatsAliasUsage_Object = MibScalar
sfpsTopologyDirStatsAliasUsage = _SfpsTopologyDirStatsAliasUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 12),
    _SfpsTopologyDirStatsAliasUsage_Type()
)
sfpsTopologyDirStatsAliasUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasUsage.setStatus("mandatory")
_SfpsDirAliasStatsTable_Object = MibTable
sfpsDirAliasStatsTable = _SfpsDirAliasStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13)
)
if mibBuilder.loadTexts:
    sfpsDirAliasStatsTable.setStatus("mandatory")
_SfpsDirAliasStatsEntry_Object = MibTableRow
sfpsDirAliasStatsEntry = _SfpsDirAliasStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1)
)
sfpsDirAliasStatsEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirAliasStatsAliasType"),
)
if mibBuilder.loadTexts:
    sfpsDirAliasStatsEntry.setStatus("mandatory")
_SfpsDirAliasStatsAliasType_Type = Integer32
_SfpsDirAliasStatsAliasType_Object = MibTableColumn
sfpsDirAliasStatsAliasType = _SfpsDirAliasStatsAliasType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1, 1),
    _SfpsDirAliasStatsAliasType_Type()
)
sfpsDirAliasStatsAliasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirAliasStatsAliasType.setStatus("mandatory")
_SfpsDirAliasStatsAliasName_Type = DisplayString
_SfpsDirAliasStatsAliasName_Object = MibTableColumn
sfpsDirAliasStatsAliasName = _SfpsDirAliasStatsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1, 2),
    _SfpsDirAliasStatsAliasName_Type()
)
sfpsDirAliasStatsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirAliasStatsAliasName.setStatus("mandatory")
_SfpsDirAliasStatsNumOfAliases_Type = Integer32
_SfpsDirAliasStatsNumOfAliases_Object = MibTableColumn
sfpsDirAliasStatsNumOfAliases = _SfpsDirAliasStatsNumOfAliases_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1, 3),
    _SfpsDirAliasStatsNumOfAliases_Type()
)
sfpsDirAliasStatsNumOfAliases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirAliasStatsNumOfAliases.setStatus("mandatory")
_SfpsDirAliasStatsAliasUsage_Type = Integer32
_SfpsDirAliasStatsAliasUsage_Object = MibTableColumn
sfpsDirAliasStatsAliasUsage = _SfpsDirAliasStatsAliasUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1, 4),
    _SfpsDirAliasStatsAliasUsage_Type()
)
sfpsDirAliasStatsAliasUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirAliasStatsAliasUsage.setStatus("mandatory")
_SfpsDirAliasStatsMaxAliases_Type = Integer32
_SfpsDirAliasStatsMaxAliases_Object = MibTableColumn
sfpsDirAliasStatsMaxAliases = _SfpsDirAliasStatsMaxAliases_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 13, 1, 5),
    _SfpsDirAliasStatsMaxAliases_Type()
)
sfpsDirAliasStatsMaxAliases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirAliasStatsMaxAliases.setStatus("mandatory")
_SfpsTopologyDirStatsStaticUsage_Type = Integer32
_SfpsTopologyDirStatsStaticUsage_Object = MibScalar
sfpsTopologyDirStatsStaticUsage = _SfpsTopologyDirStatsStaticUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 14),
    _SfpsTopologyDirStatsStaticUsage_Type()
)
sfpsTopologyDirStatsStaticUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsStaticUsage.setStatus("mandatory")
_SfpsTopologyDirStatsObjectsUsage_Type = Integer32
_SfpsTopologyDirStatsObjectsUsage_Object = MibScalar
sfpsTopologyDirStatsObjectsUsage = _SfpsTopologyDirStatsObjectsUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 15),
    _SfpsTopologyDirStatsObjectsUsage_Type()
)
sfpsTopologyDirStatsObjectsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsObjectsUsage.setStatus("mandatory")
_SfpsTopologyDirStatsNodeTableSize_Type = Integer32
_SfpsTopologyDirStatsNodeTableSize_Object = MibScalar
sfpsTopologyDirStatsNodeTableSize = _SfpsTopologyDirStatsNodeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 16),
    _SfpsTopologyDirStatsNodeTableSize_Type()
)
sfpsTopologyDirStatsNodeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeTableSize.setStatus("mandatory")
_SfpsTopologyDirStatsNodeTableUsage_Type = Integer32
_SfpsTopologyDirStatsNodeTableUsage_Object = MibScalar
sfpsTopologyDirStatsNodeTableUsage = _SfpsTopologyDirStatsNodeTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 17),
    _SfpsTopologyDirStatsNodeTableUsage_Type()
)
sfpsTopologyDirStatsNodeTableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeTableUsage.setStatus("mandatory")
_SfpsTopologyDirStatsAliasTableSize_Type = Integer32
_SfpsTopologyDirStatsAliasTableSize_Object = MibScalar
sfpsTopologyDirStatsAliasTableSize = _SfpsTopologyDirStatsAliasTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 18),
    _SfpsTopologyDirStatsAliasTableSize_Type()
)
sfpsTopologyDirStatsAliasTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasTableSize.setStatus("mandatory")
_SfpsTopologyDirStatsAliasTableUsage_Type = Integer32
_SfpsTopologyDirStatsAliasTableUsage_Object = MibScalar
sfpsTopologyDirStatsAliasTableUsage = _SfpsTopologyDirStatsAliasTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 19),
    _SfpsTopologyDirStatsAliasTableUsage_Type()
)
sfpsTopologyDirStatsAliasTableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasTableUsage.setStatus("mandatory")
_SfpsTopologyDirStatsNodeCollisions_Type = Integer32
_SfpsTopologyDirStatsNodeCollisions_Object = MibScalar
sfpsTopologyDirStatsNodeCollisions = _SfpsTopologyDirStatsNodeCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 20),
    _SfpsTopologyDirStatsNodeCollisions_Type()
)
sfpsTopologyDirStatsNodeCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeCollisions.setStatus("mandatory")
_SfpsTopologyDirStatsNodeLongestChain_Type = Integer32
_SfpsTopologyDirStatsNodeLongestChain_Object = MibScalar
sfpsTopologyDirStatsNodeLongestChain = _SfpsTopologyDirStatsNodeLongestChain_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 21),
    _SfpsTopologyDirStatsNodeLongestChain_Type()
)
sfpsTopologyDirStatsNodeLongestChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeLongestChain.setStatus("mandatory")
_SfpsTopologyDirStatsAliasCollisions_Type = Integer32
_SfpsTopologyDirStatsAliasCollisions_Object = MibScalar
sfpsTopologyDirStatsAliasCollisions = _SfpsTopologyDirStatsAliasCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 22),
    _SfpsTopologyDirStatsAliasCollisions_Type()
)
sfpsTopologyDirStatsAliasCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasCollisions.setStatus("mandatory")
_SfpsTopologyDirStatsAliasLongestChain_Type = Integer32
_SfpsTopologyDirStatsAliasLongestChain_Object = MibScalar
sfpsTopologyDirStatsAliasLongestChain = _SfpsTopologyDirStatsAliasLongestChain_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 23),
    _SfpsTopologyDirStatsAliasLongestChain_Type()
)
sfpsTopologyDirStatsAliasLongestChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasLongestChain.setStatus("mandatory")
_SfpsTopologyDirStatsLocalAddsRefused_Type = Integer32
_SfpsTopologyDirStatsLocalAddsRefused_Object = MibScalar
sfpsTopologyDirStatsLocalAddsRefused = _SfpsTopologyDirStatsLocalAddsRefused_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 24),
    _SfpsTopologyDirStatsLocalAddsRefused_Type()
)
sfpsTopologyDirStatsLocalAddsRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsLocalAddsRefused.setStatus("mandatory")
_SfpsTopologyDirStatsAliasRemotesReplaced_Type = Integer32
_SfpsTopologyDirStatsAliasRemotesReplaced_Object = MibScalar
sfpsTopologyDirStatsAliasRemotesReplaced = _SfpsTopologyDirStatsAliasRemotesReplaced_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 25),
    _SfpsTopologyDirStatsAliasRemotesReplaced_Type()
)
sfpsTopologyDirStatsAliasRemotesReplaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasRemotesReplaced.setStatus("mandatory")
_SfpsTopologyDirStatsAliasMultiPortClears_Type = Integer32
_SfpsTopologyDirStatsAliasMultiPortClears_Object = MibScalar
sfpsTopologyDirStatsAliasMultiPortClears = _SfpsTopologyDirStatsAliasMultiPortClears_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 26),
    _SfpsTopologyDirStatsAliasMultiPortClears_Type()
)
sfpsTopologyDirStatsAliasMultiPortClears.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsAliasMultiPortClears.setStatus("mandatory")
_SfpsTopologyDirStatsReservedForRemoteNodes_Type = Integer32
_SfpsTopologyDirStatsReservedForRemoteNodes_Object = MibScalar
sfpsTopologyDirStatsReservedForRemoteNodes = _SfpsTopologyDirStatsReservedForRemoteNodes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 27),
    _SfpsTopologyDirStatsReservedForRemoteNodes_Type()
)
sfpsTopologyDirStatsReservedForRemoteNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsReservedForRemoteNodes.setStatus("mandatory")
_SfpsTopologyDirStatsNumSwitches_Type = Integer32
_SfpsTopologyDirStatsNumSwitches_Object = MibScalar
sfpsTopologyDirStatsNumSwitches = _SfpsTopologyDirStatsNumSwitches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 28),
    _SfpsTopologyDirStatsNumSwitches_Type()
)
sfpsTopologyDirStatsNumSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumSwitches.setStatus("mandatory")
_SfpsTopologyDirStatsSwitchUsage_Type = Integer32
_SfpsTopologyDirStatsSwitchUsage_Object = MibScalar
sfpsTopologyDirStatsSwitchUsage = _SfpsTopologyDirStatsSwitchUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 29),
    _SfpsTopologyDirStatsSwitchUsage_Type()
)
sfpsTopologyDirStatsSwitchUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsSwitchUsage.setStatus("mandatory")
_SfpsTopologyDirStatsMaxSwitches_Type = Integer32
_SfpsTopologyDirStatsMaxSwitches_Object = MibScalar
sfpsTopologyDirStatsMaxSwitches = _SfpsTopologyDirStatsMaxSwitches_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 30),
    _SfpsTopologyDirStatsMaxSwitches_Type()
)
sfpsTopologyDirStatsMaxSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsMaxSwitches.setStatus("mandatory")
_SfpsTopologyDirStatsSwitchTableSize_Type = Integer32
_SfpsTopologyDirStatsSwitchTableSize_Object = MibScalar
sfpsTopologyDirStatsSwitchTableSize = _SfpsTopologyDirStatsSwitchTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 31),
    _SfpsTopologyDirStatsSwitchTableSize_Type()
)
sfpsTopologyDirStatsSwitchTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsSwitchTableSize.setStatus("mandatory")
_SfpsTopologyDirStatsSwitchTableUsage_Type = Integer32
_SfpsTopologyDirStatsSwitchTableUsage_Object = MibScalar
sfpsTopologyDirStatsSwitchTableUsage = _SfpsTopologyDirStatsSwitchTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 32),
    _SfpsTopologyDirStatsSwitchTableUsage_Type()
)
sfpsTopologyDirStatsSwitchTableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsSwitchTableUsage.setStatus("mandatory")
_SfpsTopologyDirStatsSwitchLookups_Type = Integer32
_SfpsTopologyDirStatsSwitchLookups_Object = MibScalar
sfpsTopologyDirStatsSwitchLookups = _SfpsTopologyDirStatsSwitchLookups_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 33),
    _SfpsTopologyDirStatsSwitchLookups_Type()
)
sfpsTopologyDirStatsSwitchLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsSwitchLookups.setStatus("mandatory")
_SfpsTopologyDirStatsSwitchCacheHits_Type = Integer32
_SfpsTopologyDirStatsSwitchCacheHits_Object = MibScalar
sfpsTopologyDirStatsSwitchCacheHits = _SfpsTopologyDirStatsSwitchCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 34),
    _SfpsTopologyDirStatsSwitchCacheHits_Type()
)
sfpsTopologyDirStatsSwitchCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsSwitchCacheHits.setStatus("mandatory")
_SfpsTopologyDirStatsNumVlans_Type = Integer32
_SfpsTopologyDirStatsNumVlans_Object = MibScalar
sfpsTopologyDirStatsNumVlans = _SfpsTopologyDirStatsNumVlans_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 35),
    _SfpsTopologyDirStatsNumVlans_Type()
)
sfpsTopologyDirStatsNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNumVlans.setStatus("mandatory")
_SfpsTopologyDirStatsVlanUsage_Type = Integer32
_SfpsTopologyDirStatsVlanUsage_Object = MibScalar
sfpsTopologyDirStatsVlanUsage = _SfpsTopologyDirStatsVlanUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 36),
    _SfpsTopologyDirStatsVlanUsage_Type()
)
sfpsTopologyDirStatsVlanUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsVlanUsage.setStatus("mandatory")
_SfpsTopologyDirStatsMaxVlans_Type = Integer32
_SfpsTopologyDirStatsMaxVlans_Object = MibScalar
sfpsTopologyDirStatsMaxVlans = _SfpsTopologyDirStatsMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 37),
    _SfpsTopologyDirStatsMaxVlans_Type()
)
sfpsTopologyDirStatsMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsMaxVlans.setStatus("mandatory")
_SfpsTopologyDirStatsVlanTableSize_Type = Integer32
_SfpsTopologyDirStatsVlanTableSize_Object = MibScalar
sfpsTopologyDirStatsVlanTableSize = _SfpsTopologyDirStatsVlanTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 38),
    _SfpsTopologyDirStatsVlanTableSize_Type()
)
sfpsTopologyDirStatsVlanTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsVlanTableSize.setStatus("mandatory")
_SfpsTopologyDirStatsVlanTableUsage_Type = Integer32
_SfpsTopologyDirStatsVlanTableUsage_Object = MibScalar
sfpsTopologyDirStatsVlanTableUsage = _SfpsTopologyDirStatsVlanTableUsage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 39),
    _SfpsTopologyDirStatsVlanTableUsage_Type()
)
sfpsTopologyDirStatsVlanTableUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsVlanTableUsage.setStatus("mandatory")
_SfpsTopologyDirStatsVlanLookups_Type = Integer32
_SfpsTopologyDirStatsVlanLookups_Object = MibScalar
sfpsTopologyDirStatsVlanLookups = _SfpsTopologyDirStatsVlanLookups_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 40),
    _SfpsTopologyDirStatsVlanLookups_Type()
)
sfpsTopologyDirStatsVlanLookups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsVlanLookups.setStatus("mandatory")
_SfpsTopologyDirStatsVlanCacheHits_Type = Integer32
_SfpsTopologyDirStatsVlanCacheHits_Object = MibScalar
sfpsTopologyDirStatsVlanCacheHits = _SfpsTopologyDirStatsVlanCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 41),
    _SfpsTopologyDirStatsVlanCacheHits_Type()
)
sfpsTopologyDirStatsVlanCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsVlanCacheHits.setStatus("mandatory")
_SfpsTopologyDirStatsNodeAliasMax_Type = Integer32
_SfpsTopologyDirStatsNodeAliasMax_Object = MibScalar
sfpsTopologyDirStatsNodeAliasMax = _SfpsTopologyDirStatsNodeAliasMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 42),
    _SfpsTopologyDirStatsNodeAliasMax_Type()
)
sfpsTopologyDirStatsNodeAliasMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsNodeAliasMax.setStatus("mandatory")
_SfpsTopologyDirStatsLocalAliasRefused_Type = Integer32
_SfpsTopologyDirStatsLocalAliasRefused_Object = MibScalar
sfpsTopologyDirStatsLocalAliasRefused = _SfpsTopologyDirStatsLocalAliasRefused_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 43),
    _SfpsTopologyDirStatsLocalAliasRefused_Type()
)
sfpsTopologyDirStatsLocalAliasRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsLocalAliasRefused.setStatus("mandatory")
_SfpsTopologyDirStatsRemoteAliasRemoved_Type = Integer32
_SfpsTopologyDirStatsRemoteAliasRemoved_Object = MibScalar
sfpsTopologyDirStatsRemoteAliasRemoved = _SfpsTopologyDirStatsRemoteAliasRemoved_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 11, 44),
    _SfpsTopologyDirStatsRemoteAliasRemoved_Type()
)
sfpsTopologyDirStatsRemoteAliasRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsTopologyDirStatsRemoteAliasRemoved.setStatus("mandatory")


class _SfpsDirFilterAPILockAdmin_Type(Integer32):
    """Custom type sfpsDirFilterAPILockAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lock", 2),
          ("other", 1),
          ("unlock", 3))
    )


_SfpsDirFilterAPILockAdmin_Type.__name__ = "Integer32"
_SfpsDirFilterAPILockAdmin_Object = MibScalar
sfpsDirFilterAPILockAdmin = _SfpsDirFilterAPILockAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 1),
    _SfpsDirFilterAPILockAdmin_Type()
)
sfpsDirFilterAPILockAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirFilterAPILockAdmin.setStatus("mandatory")


class _SfpsDirFilterAPILockStatus_Type(Integer32):
    """Custom type sfpsDirFilterAPILockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("other", 1),
          ("unlocked", 3))
    )


_SfpsDirFilterAPILockStatus_Type.__name__ = "Integer32"
_SfpsDirFilterAPILockStatus_Object = MibScalar
sfpsDirFilterAPILockStatus = _SfpsDirFilterAPILockStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 2),
    _SfpsDirFilterAPILockStatus_Type()
)
sfpsDirFilterAPILockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAPILockStatus.setStatus("mandatory")
_SfpsDirFilterAPILockCount_Type = Integer32
_SfpsDirFilterAPILockCount_Object = MibScalar
sfpsDirFilterAPILockCount = _SfpsDirFilterAPILockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 3),
    _SfpsDirFilterAPILockCount_Type()
)
sfpsDirFilterAPILockCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirFilterAPILockCount.setStatus("mandatory")
_SfpsDirFilterAPIValueType_Type = DisplayString
_SfpsDirFilterAPIValueType_Object = MibScalar
sfpsDirFilterAPIValueType = _SfpsDirFilterAPIValueType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 4),
    _SfpsDirFilterAPIValueType_Type()
)
sfpsDirFilterAPIValueType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirFilterAPIValueType.setStatus("mandatory")
_SfpsDirFilterAPIValue_Type = DisplayString
_SfpsDirFilterAPIValue_Object = MibScalar
sfpsDirFilterAPIValue = _SfpsDirFilterAPIValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 5),
    _SfpsDirFilterAPIValue_Type()
)
sfpsDirFilterAPIValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirFilterAPIValue.setStatus("mandatory")
_SfpsDirFilterAPILockTimeOut_Type = Integer32
_SfpsDirFilterAPILockTimeOut_Object = MibScalar
sfpsDirFilterAPILockTimeOut = _SfpsDirFilterAPILockTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 6),
    _SfpsDirFilterAPILockTimeOut_Type()
)
sfpsDirFilterAPILockTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsDirFilterAPILockTimeOut.setStatus("mandatory")
_SfpsDirFilterAPILockTimeElapsed_Type = Integer32
_SfpsDirFilterAPILockTimeElapsed_Object = MibScalar
sfpsDirFilterAPILockTimeElapsed = _SfpsDirFilterAPILockTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 1, 7),
    _SfpsDirFilterAPILockTimeElapsed_Type()
)
sfpsDirFilterAPILockTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAPILockTimeElapsed.setStatus("mandatory")
_SfpsDirFilterNodeTable_Object = MibTable
sfpsDirFilterNodeTable = _SfpsDirFilterNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2)
)
if mibBuilder.loadTexts:
    sfpsDirFilterNodeTable.setStatus("mandatory")
_SfpsDirFilterNodeEntry_Object = MibTableRow
sfpsDirFilterNodeEntry = _SfpsDirFilterNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1)
)
sfpsDirFilterNodeEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterNodeLockCount"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterNodeNodeIndex"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterNodeLinkIndex"),
)
if mibBuilder.loadTexts:
    sfpsDirFilterNodeEntry.setStatus("mandatory")
_SfpsDirFilterNodeLockCount_Type = Integer32
_SfpsDirFilterNodeLockCount_Object = MibTableColumn
sfpsDirFilterNodeLockCount = _SfpsDirFilterNodeLockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 1),
    _SfpsDirFilterNodeLockCount_Type()
)
sfpsDirFilterNodeLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLockCount.setStatus("mandatory")
_SfpsDirFilterNodeNodeIndex_Type = Integer32
_SfpsDirFilterNodeNodeIndex_Object = MibTableColumn
sfpsDirFilterNodeNodeIndex = _SfpsDirFilterNodeNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 2),
    _SfpsDirFilterNodeNodeIndex_Type()
)
sfpsDirFilterNodeNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeIndex.setStatus("mandatory")
_SfpsDirFilterNodeLinkIndex_Type = Integer32
_SfpsDirFilterNodeLinkIndex_Object = MibTableColumn
sfpsDirFilterNodeLinkIndex = _SfpsDirFilterNodeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 3),
    _SfpsDirFilterNodeLinkIndex_Type()
)
sfpsDirFilterNodeLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkIndex.setStatus("mandatory")
_SfpsDirFilterNodeNodeCount_Type = Integer32
_SfpsDirFilterNodeNodeCount_Object = MibTableColumn
sfpsDirFilterNodeNodeCount = _SfpsDirFilterNodeNodeCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 4),
    _SfpsDirFilterNodeNodeCount_Type()
)
sfpsDirFilterNodeNodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeCount.setStatus("mandatory")
_SfpsDirFilterNodeLinkCount_Type = Integer32
_SfpsDirFilterNodeLinkCount_Object = MibTableColumn
sfpsDirFilterNodeLinkCount = _SfpsDirFilterNodeLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 5),
    _SfpsDirFilterNodeLinkCount_Type()
)
sfpsDirFilterNodeLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkCount.setStatus("mandatory")
_SfpsDirFilterNodeDomainName_Type = DisplayString
_SfpsDirFilterNodeDomainName_Object = MibTableColumn
sfpsDirFilterNodeDomainName = _SfpsDirFilterNodeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 6),
    _SfpsDirFilterNodeDomainName_Type()
)
sfpsDirFilterNodeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeDomainName.setStatus("mandatory")
_SfpsDirFilterNodeChassisType_Type = DisplayString
_SfpsDirFilterNodeChassisType_Object = MibTableColumn
sfpsDirFilterNodeChassisType = _SfpsDirFilterNodeChassisType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 7),
    _SfpsDirFilterNodeChassisType_Type()
)
sfpsDirFilterNodeChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeChassisType.setStatus("mandatory")
_SfpsDirFilterNodeChassisLoad_Type = DisplayString
_SfpsDirFilterNodeChassisLoad_Object = MibTableColumn
sfpsDirFilterNodeChassisLoad = _SfpsDirFilterNodeChassisLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 8),
    _SfpsDirFilterNodeChassisLoad_Type()
)
sfpsDirFilterNodeChassisLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeChassisLoad.setStatus("mandatory")
_SfpsDirFilterNodeSwitchType_Type = DisplayString
_SfpsDirFilterNodeSwitchType_Object = MibTableColumn
sfpsDirFilterNodeSwitchType = _SfpsDirFilterNodeSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 9),
    _SfpsDirFilterNodeSwitchType_Type()
)
sfpsDirFilterNodeSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeSwitchType.setStatus("mandatory")
_SfpsDirFilterNodeSwitchLoad_Type = DisplayString
_SfpsDirFilterNodeSwitchLoad_Object = MibTableColumn
sfpsDirFilterNodeSwitchLoad = _SfpsDirFilterNodeSwitchLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 10),
    _SfpsDirFilterNodeSwitchLoad_Type()
)
sfpsDirFilterNodeSwitchLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeSwitchLoad.setStatus("mandatory")
_SfpsDirFilterNodeInPort_Type = Integer32
_SfpsDirFilterNodeInPort_Object = MibTableColumn
sfpsDirFilterNodeInPort = _SfpsDirFilterNodeInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 11),
    _SfpsDirFilterNodeInPort_Type()
)
sfpsDirFilterNodeInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeInPort.setStatus("mandatory")
_SfpsDirFilterNodeBaseType_Type = DisplayString
_SfpsDirFilterNodeBaseType_Object = MibTableColumn
sfpsDirFilterNodeBaseType = _SfpsDirFilterNodeBaseType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 12),
    _SfpsDirFilterNodeBaseType_Type()
)
sfpsDirFilterNodeBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeBaseType.setStatus("mandatory")
_SfpsDirFilterNodeBaseLoad_Type = DisplayString
_SfpsDirFilterNodeBaseLoad_Object = MibTableColumn
sfpsDirFilterNodeBaseLoad = _SfpsDirFilterNodeBaseLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 13),
    _SfpsDirFilterNodeBaseLoad_Type()
)
sfpsDirFilterNodeBaseLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeBaseLoad.setStatus("mandatory")
_SfpsDirFilterNodeNodeState_Type = Integer32
_SfpsDirFilterNodeNodeState_Object = MibTableColumn
sfpsDirFilterNodeNodeState = _SfpsDirFilterNodeNodeState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 14),
    _SfpsDirFilterNodeNodeState_Type()
)
sfpsDirFilterNodeNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeState.setStatus("mandatory")
_SfpsDirFilterNodeNodeAge_Type = TimeTicks
_SfpsDirFilterNodeNodeAge_Object = MibTableColumn
sfpsDirFilterNodeNodeAge = _SfpsDirFilterNodeNodeAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 15),
    _SfpsDirFilterNodeNodeAge_Type()
)
sfpsDirFilterNodeNodeAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeAge.setStatus("mandatory")


class _SfpsDirFilterNodeNodeLock_Type(Integer32):
    """Custom type sfpsDirFilterNodeNodeLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked-to-port", 2),
          ("unlocked", 1))
    )


_SfpsDirFilterNodeNodeLock_Type.__name__ = "Integer32"
_SfpsDirFilterNodeNodeLock_Object = MibTableColumn
sfpsDirFilterNodeNodeLock = _SfpsDirFilterNodeNodeLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 16),
    _SfpsDirFilterNodeNodeLock_Type()
)
sfpsDirFilterNodeNodeLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeLock.setStatus("mandatory")
_SfpsDirFilterNodeLinkType_Type = DisplayString
_SfpsDirFilterNodeLinkType_Object = MibTableColumn
sfpsDirFilterNodeLinkType = _SfpsDirFilterNodeLinkType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 17),
    _SfpsDirFilterNodeLinkType_Type()
)
sfpsDirFilterNodeLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkType.setStatus("mandatory")
_SfpsDirFilterNodeLinkLoad_Type = DisplayString
_SfpsDirFilterNodeLinkLoad_Object = MibTableColumn
sfpsDirFilterNodeLinkLoad = _SfpsDirFilterNodeLinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 18),
    _SfpsDirFilterNodeLinkLoad_Type()
)
sfpsDirFilterNodeLinkLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkLoad.setStatus("mandatory")
_SfpsDirFilterNodeLinkAge_Type = TimeTicks
_SfpsDirFilterNodeLinkAge_Object = MibTableColumn
sfpsDirFilterNodeLinkAge = _SfpsDirFilterNodeLinkAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 19),
    _SfpsDirFilterNodeLinkAge_Type()
)
sfpsDirFilterNodeLinkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkAge.setStatus("mandatory")


class _SfpsDirFilterNodeLinkLock_Type(Integer32):
    """Custom type sfpsDirFilterNodeLinkLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked-to-node", 2),
          ("unlocked", 1))
    )


_SfpsDirFilterNodeLinkLock_Type.__name__ = "Integer32"
_SfpsDirFilterNodeLinkLock_Object = MibTableColumn
sfpsDirFilterNodeLinkLock = _SfpsDirFilterNodeLinkLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 20),
    _SfpsDirFilterNodeLinkLock_Type()
)
sfpsDirFilterNodeLinkLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkLock.setStatus("mandatory")


class _SfpsDirFilterNodeVlanLearned_Type(Integer32):
    """Custom type sfpsDirFilterNodeVlanLearned based on Integer32"""
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
        *(("autoReg", 3),
          ("inherit", 2),
          ("other", 1),
          ("static", 4))
    )


_SfpsDirFilterNodeVlanLearned_Type.__name__ = "Integer32"
_SfpsDirFilterNodeVlanLearned_Object = MibTableColumn
sfpsDirFilterNodeVlanLearned = _SfpsDirFilterNodeVlanLearned_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 21),
    _SfpsDirFilterNodeVlanLearned_Type()
)
sfpsDirFilterNodeVlanLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeVlanLearned.setStatus("mandatory")
_SfpsDirFilterNodeOpaqueTag_Type = OctetString
_SfpsDirFilterNodeOpaqueTag_Object = MibTableColumn
sfpsDirFilterNodeOpaqueTag = _SfpsDirFilterNodeOpaqueTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 22),
    _SfpsDirFilterNodeOpaqueTag_Type()
)
sfpsDirFilterNodeOpaqueTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeOpaqueTag.setStatus("mandatory")
_SfpsDirFilterNodeChassisOctets_Type = OctetString
_SfpsDirFilterNodeChassisOctets_Object = MibTableColumn
sfpsDirFilterNodeChassisOctets = _SfpsDirFilterNodeChassisOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 23),
    _SfpsDirFilterNodeChassisOctets_Type()
)
sfpsDirFilterNodeChassisOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeChassisOctets.setStatus("mandatory")
_SfpsDirFilterNodeSwitchOctets_Type = OctetString
_SfpsDirFilterNodeSwitchOctets_Object = MibTableColumn
sfpsDirFilterNodeSwitchOctets = _SfpsDirFilterNodeSwitchOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 24),
    _SfpsDirFilterNodeSwitchOctets_Type()
)
sfpsDirFilterNodeSwitchOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeSwitchOctets.setStatus("mandatory")
_SfpsDirFilterNodeNodeOctets_Type = OctetString
_SfpsDirFilterNodeNodeOctets_Object = MibTableColumn
sfpsDirFilterNodeNodeOctets = _SfpsDirFilterNodeNodeOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 25),
    _SfpsDirFilterNodeNodeOctets_Type()
)
sfpsDirFilterNodeNodeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeOctets.setStatus("mandatory")
_SfpsDirFilterNodeLinkOctets_Type = OctetString
_SfpsDirFilterNodeLinkOctets_Object = MibTableColumn
sfpsDirFilterNodeLinkOctets = _SfpsDirFilterNodeLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 26),
    _SfpsDirFilterNodeLinkOctets_Type()
)
sfpsDirFilterNodeLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkOctets.setStatus("mandatory")


class _SfpsDirFilterNodeNodeLocal_Type(Integer32):
    """Custom type sfpsDirFilterNodeNodeLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsDirFilterNodeNodeLocal_Type.__name__ = "Integer32"
_SfpsDirFilterNodeNodeLocal_Object = MibTableColumn
sfpsDirFilterNodeNodeLocal = _SfpsDirFilterNodeNodeLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 27),
    _SfpsDirFilterNodeNodeLocal_Type()
)
sfpsDirFilterNodeNodeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeNodeLocal.setStatus("mandatory")


class _SfpsDirFilterNodeLinkState_Type(Integer32):
    """Custom type sfpsDirFilterNodeLinkState based on Integer32"""
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
        *(("hidden", 4),
          ("local", 3),
          ("other", 1),
          ("remote", 2))
    )


_SfpsDirFilterNodeLinkState_Type.__name__ = "Integer32"
_SfpsDirFilterNodeLinkState_Object = MibTableColumn
sfpsDirFilterNodeLinkState = _SfpsDirFilterNodeLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 2, 1, 28),
    _SfpsDirFilterNodeLinkState_Type()
)
sfpsDirFilterNodeLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterNodeLinkState.setStatus("mandatory")
_SfpsDirFilterAliasTable_Object = MibTable
sfpsDirFilterAliasTable = _SfpsDirFilterAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3)
)
if mibBuilder.loadTexts:
    sfpsDirFilterAliasTable.setStatus("mandatory")
_SfpsDirFilterAliasEntry_Object = MibTableRow
sfpsDirFilterAliasEntry = _SfpsDirFilterAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1)
)
sfpsDirFilterAliasEntry.setIndexNames(
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterAliasLockCount"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterAliasAliasHash"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterAliasBaseHash"),
    (0, "CTRON-SFPS-DIRECTORY-MIB", "sfpsDirFilterAliasHashIndex"),
)
if mibBuilder.loadTexts:
    sfpsDirFilterAliasEntry.setStatus("mandatory")
_SfpsDirFilterAliasLockCount_Type = Integer32
_SfpsDirFilterAliasLockCount_Object = MibTableColumn
sfpsDirFilterAliasLockCount = _SfpsDirFilterAliasLockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 1),
    _SfpsDirFilterAliasLockCount_Type()
)
sfpsDirFilterAliasLockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLockCount.setStatus("mandatory")
_SfpsDirFilterAliasAliasHash_Type = Integer32
_SfpsDirFilterAliasAliasHash_Object = MibTableColumn
sfpsDirFilterAliasAliasHash = _SfpsDirFilterAliasAliasHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 2),
    _SfpsDirFilterAliasAliasHash_Type()
)
sfpsDirFilterAliasAliasHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasAliasHash.setStatus("mandatory")
_SfpsDirFilterAliasBaseHash_Type = Integer32
_SfpsDirFilterAliasBaseHash_Object = MibTableColumn
sfpsDirFilterAliasBaseHash = _SfpsDirFilterAliasBaseHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 3),
    _SfpsDirFilterAliasBaseHash_Type()
)
sfpsDirFilterAliasBaseHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasBaseHash.setStatus("mandatory")
_SfpsDirFilterAliasHashIndex_Type = Integer32
_SfpsDirFilterAliasHashIndex_Object = MibTableColumn
sfpsDirFilterAliasHashIndex = _SfpsDirFilterAliasHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 4),
    _SfpsDirFilterAliasHashIndex_Type()
)
sfpsDirFilterAliasHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasHashIndex.setStatus("mandatory")
_SfpsDirFilterAliasDomain_Type = DisplayString
_SfpsDirFilterAliasDomain_Object = MibTableColumn
sfpsDirFilterAliasDomain = _SfpsDirFilterAliasDomain_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 5),
    _SfpsDirFilterAliasDomain_Type()
)
sfpsDirFilterAliasDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasDomain.setStatus("mandatory")
_SfpsDirFilterAliasChassisType_Type = DisplayString
_SfpsDirFilterAliasChassisType_Object = MibTableColumn
sfpsDirFilterAliasChassisType = _SfpsDirFilterAliasChassisType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 6),
    _SfpsDirFilterAliasChassisType_Type()
)
sfpsDirFilterAliasChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasChassisType.setStatus("mandatory")
_SfpsDirFilterAliasChassisLoad_Type = DisplayString
_SfpsDirFilterAliasChassisLoad_Object = MibTableColumn
sfpsDirFilterAliasChassisLoad = _SfpsDirFilterAliasChassisLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 7),
    _SfpsDirFilterAliasChassisLoad_Type()
)
sfpsDirFilterAliasChassisLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasChassisLoad.setStatus("mandatory")
_SfpsDirFilterAliasSwitchType_Type = DisplayString
_SfpsDirFilterAliasSwitchType_Object = MibTableColumn
sfpsDirFilterAliasSwitchType = _SfpsDirFilterAliasSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 8),
    _SfpsDirFilterAliasSwitchType_Type()
)
sfpsDirFilterAliasSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasSwitchType.setStatus("mandatory")
_SfpsDirFilterAliasSwitchLoad_Type = DisplayString
_SfpsDirFilterAliasSwitchLoad_Object = MibTableColumn
sfpsDirFilterAliasSwitchLoad = _SfpsDirFilterAliasSwitchLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 9),
    _SfpsDirFilterAliasSwitchLoad_Type()
)
sfpsDirFilterAliasSwitchLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasSwitchLoad.setStatus("mandatory")
_SfpsDirFilterAliasInPort_Type = Integer32
_SfpsDirFilterAliasInPort_Object = MibTableColumn
sfpsDirFilterAliasInPort = _SfpsDirFilterAliasInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 10),
    _SfpsDirFilterAliasInPort_Type()
)
sfpsDirFilterAliasInPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasInPort.setStatus("mandatory")
_SfpsDirFilterAliasBaseType_Type = DisplayString
_SfpsDirFilterAliasBaseType_Object = MibTableColumn
sfpsDirFilterAliasBaseType = _SfpsDirFilterAliasBaseType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 11),
    _SfpsDirFilterAliasBaseType_Type()
)
sfpsDirFilterAliasBaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasBaseType.setStatus("mandatory")
_SfpsDirFilterAliasBaseLoad_Type = DisplayString
_SfpsDirFilterAliasBaseLoad_Object = MibTableColumn
sfpsDirFilterAliasBaseLoad = _SfpsDirFilterAliasBaseLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 12),
    _SfpsDirFilterAliasBaseLoad_Type()
)
sfpsDirFilterAliasBaseLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasBaseLoad.setStatus("mandatory")
_SfpsDirFilterAliasNodeState_Type = Integer32
_SfpsDirFilterAliasNodeState_Object = MibTableColumn
sfpsDirFilterAliasNodeState = _SfpsDirFilterAliasNodeState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 13),
    _SfpsDirFilterAliasNodeState_Type()
)
sfpsDirFilterAliasNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasNodeState.setStatus("mandatory")
_SfpsDirFilterAliasNodeAge_Type = TimeTicks
_SfpsDirFilterAliasNodeAge_Object = MibTableColumn
sfpsDirFilterAliasNodeAge = _SfpsDirFilterAliasNodeAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 14),
    _SfpsDirFilterAliasNodeAge_Type()
)
sfpsDirFilterAliasNodeAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasNodeAge.setStatus("mandatory")


class _SfpsDirFilterAliasNodeLock_Type(Integer32):
    """Custom type sfpsDirFilterAliasNodeLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked-to-port", 2),
          ("unlocked", 1))
    )


_SfpsDirFilterAliasNodeLock_Type.__name__ = "Integer32"
_SfpsDirFilterAliasNodeLock_Object = MibTableColumn
sfpsDirFilterAliasNodeLock = _SfpsDirFilterAliasNodeLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 15),
    _SfpsDirFilterAliasNodeLock_Type()
)
sfpsDirFilterAliasNodeLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasNodeLock.setStatus("mandatory")
_SfpsDirFilterAliasLinkType_Type = DisplayString
_SfpsDirFilterAliasLinkType_Object = MibTableColumn
sfpsDirFilterAliasLinkType = _SfpsDirFilterAliasLinkType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 16),
    _SfpsDirFilterAliasLinkType_Type()
)
sfpsDirFilterAliasLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkType.setStatus("mandatory")
_SfpsDirFilterAliasLinkLoad_Type = DisplayString
_SfpsDirFilterAliasLinkLoad_Object = MibTableColumn
sfpsDirFilterAliasLinkLoad = _SfpsDirFilterAliasLinkLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 17),
    _SfpsDirFilterAliasLinkLoad_Type()
)
sfpsDirFilterAliasLinkLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkLoad.setStatus("mandatory")
_SfpsDirFilterAliasLinkAge_Type = TimeTicks
_SfpsDirFilterAliasLinkAge_Object = MibTableColumn
sfpsDirFilterAliasLinkAge = _SfpsDirFilterAliasLinkAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 18),
    _SfpsDirFilterAliasLinkAge_Type()
)
sfpsDirFilterAliasLinkAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkAge.setStatus("mandatory")


class _SfpsDirFilterAliasLinkLock_Type(Integer32):
    """Custom type sfpsDirFilterAliasLinkLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked-to-node", 2),
          ("unlocked", 1))
    )


_SfpsDirFilterAliasLinkLock_Type.__name__ = "Integer32"
_SfpsDirFilterAliasLinkLock_Object = MibTableColumn
sfpsDirFilterAliasLinkLock = _SfpsDirFilterAliasLinkLock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 19),
    _SfpsDirFilterAliasLinkLock_Type()
)
sfpsDirFilterAliasLinkLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkLock.setStatus("mandatory")


class _SfpsDirFilterAliasVlanLearned_Type(Integer32):
    """Custom type sfpsDirFilterAliasVlanLearned based on Integer32"""
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
        *(("amr", 3),
          ("inherited", 2),
          ("other", 1),
          ("static", 4))
    )


_SfpsDirFilterAliasVlanLearned_Type.__name__ = "Integer32"
_SfpsDirFilterAliasVlanLearned_Object = MibTableColumn
sfpsDirFilterAliasVlanLearned = _SfpsDirFilterAliasVlanLearned_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 20),
    _SfpsDirFilterAliasVlanLearned_Type()
)
sfpsDirFilterAliasVlanLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasVlanLearned.setStatus("mandatory")
_SfpsDirFilterAliasOpaqueTag_Type = OctetString
_SfpsDirFilterAliasOpaqueTag_Object = MibTableColumn
sfpsDirFilterAliasOpaqueTag = _SfpsDirFilterAliasOpaqueTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 21),
    _SfpsDirFilterAliasOpaqueTag_Type()
)
sfpsDirFilterAliasOpaqueTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasOpaqueTag.setStatus("mandatory")
_SfpsDirFilterAliasChassisOctets_Type = OctetString
_SfpsDirFilterAliasChassisOctets_Object = MibTableColumn
sfpsDirFilterAliasChassisOctets = _SfpsDirFilterAliasChassisOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 22),
    _SfpsDirFilterAliasChassisOctets_Type()
)
sfpsDirFilterAliasChassisOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasChassisOctets.setStatus("mandatory")
_SfpsDirFilterAliasSwitchOctets_Type = OctetString
_SfpsDirFilterAliasSwitchOctets_Object = MibTableColumn
sfpsDirFilterAliasSwitchOctets = _SfpsDirFilterAliasSwitchOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 23),
    _SfpsDirFilterAliasSwitchOctets_Type()
)
sfpsDirFilterAliasSwitchOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasSwitchOctets.setStatus("mandatory")
_SfpsDirFilterAliasNodeOctets_Type = OctetString
_SfpsDirFilterAliasNodeOctets_Object = MibTableColumn
sfpsDirFilterAliasNodeOctets = _SfpsDirFilterAliasNodeOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 24),
    _SfpsDirFilterAliasNodeOctets_Type()
)
sfpsDirFilterAliasNodeOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasNodeOctets.setStatus("mandatory")
_SfpsDirFilterAliasLinkOctets_Type = OctetString
_SfpsDirFilterAliasLinkOctets_Object = MibTableColumn
sfpsDirFilterAliasLinkOctets = _SfpsDirFilterAliasLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 25),
    _SfpsDirFilterAliasLinkOctets_Type()
)
sfpsDirFilterAliasLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkOctets.setStatus("mandatory")


class _SfpsDirFilterAliasNodeLocal_Type(Integer32):
    """Custom type sfpsDirFilterAliasNodeLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_SfpsDirFilterAliasNodeLocal_Type.__name__ = "Integer32"
_SfpsDirFilterAliasNodeLocal_Object = MibTableColumn
sfpsDirFilterAliasNodeLocal = _SfpsDirFilterAliasNodeLocal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 26),
    _SfpsDirFilterAliasNodeLocal_Type()
)
sfpsDirFilterAliasNodeLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasNodeLocal.setStatus("mandatory")


class _SfpsDirFilterAliasLinkState_Type(Integer32):
    """Custom type sfpsDirFilterAliasLinkState based on Integer32"""
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
        *(("hidden", 4),
          ("local", 3),
          ("other", 1),
          ("remote", 2))
    )


_SfpsDirFilterAliasLinkState_Type.__name__ = "Integer32"
_SfpsDirFilterAliasLinkState_Object = MibTableColumn
sfpsDirFilterAliasLinkState = _SfpsDirFilterAliasLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 3, 13, 3, 1, 27),
    _SfpsDirFilterAliasLinkState_Type()
)
sfpsDirFilterAliasLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsDirFilterAliasLinkState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-DIRECTORY-MIB",
    **{"SfpsSwitchPort": SfpsSwitchPort,
       "SfpsAddress": SfpsAddress,
       "HexInteger": HexInteger,
       "sfpsServiceCenterDirectoryTable": sfpsServiceCenterDirectoryTable,
       "sfpsServiceCenterDirectoryEntry": sfpsServiceCenterDirectoryEntry,
       "sfpsServiceCenterDirectoryHashLeaf": sfpsServiceCenterDirectoryHashLeaf,
       "sfpsServiceCenterDirectoryMetric": sfpsServiceCenterDirectoryMetric,
       "sfpsServiceCenterDirectoryName": sfpsServiceCenterDirectoryName,
       "sfpsServiceCenterDirectoryOperStatus": sfpsServiceCenterDirectoryOperStatus,
       "sfpsServiceCenterDirectoryAdminStatus": sfpsServiceCenterDirectoryAdminStatus,
       "sfpsServiceCenterDirectoryStatusTime": sfpsServiceCenterDirectoryStatusTime,
       "sfpsServiceCenterDirectoryRequests": sfpsServiceCenterDirectoryRequests,
       "sfpsServiceCenterDirectoryResponses": sfpsServiceCenterDirectoryResponses,
       "sfpsNodeTable": sfpsNodeTable,
       "sfpsNodeTableEntry": sfpsNodeTableEntry,
       "sfpsNodeTableBaseHash": sfpsNodeTableBaseHash,
       "sfpsNodeTableHashIndex": sfpsNodeTableHashIndex,
       "sfpsNodeTableSwitchType": sfpsNodeTableSwitchType,
       "sfpsNodeTableSwitchAddress": sfpsNodeTableSwitchAddress,
       "sfpsNodeTablePort": sfpsNodeTablePort,
       "sfpsNodeTableBaseType": sfpsNodeTableBaseType,
       "sfpsNodeTableBaseAddress": sfpsNodeTableBaseAddress,
       "sfpsNodeTableEntryType": sfpsNodeTableEntryType,
       "sfpsNodeTableCallTag": sfpsNodeTableCallTag,
       "sfpsNodeTableLastHeard": sfpsNodeTableLastHeard,
       "sfpsNodeTableAge": sfpsNodeTableAge,
       "sfpsNodeTableAliasCount": sfpsNodeTableAliasCount,
       "sfpsNodeTableVlanCount": sfpsNodeTableVlanCount,
       "sfpsNodeTableNodeLocked": sfpsNodeTableNodeLocked,
       "sfpsNodeTableNodeLocal": sfpsNodeTableNodeLocal,
       "sfpsNodeTableSelf": sfpsNodeTableSelf,
       "sfpsNodeTableNext": sfpsNodeTableNext,
       "sfpsNodeTablePrev": sfpsNodeTablePrev,
       "sfpsAliasTable": sfpsAliasTable,
       "sfpsAliasTableEntry": sfpsAliasTableEntry,
       "sfpsAliasTableAliasHash": sfpsAliasTableAliasHash,
       "sfpsAliasTableBaseHash": sfpsAliasTableBaseHash,
       "sfpsAliasTableHashIndex": sfpsAliasTableHashIndex,
       "sfpsAliasTableSwitchType": sfpsAliasTableSwitchType,
       "sfpsAliasTableSwitchAddress": sfpsAliasTableSwitchAddress,
       "sfpsAliasTablePort": sfpsAliasTablePort,
       "sfpsAliasTableBaseType": sfpsAliasTableBaseType,
       "sfpsAliasTableBaseAddress": sfpsAliasTableBaseAddress,
       "sfpsAliasTableAliasType": sfpsAliasTableAliasType,
       "sfpsAliasTableAliasAddress": sfpsAliasTableAliasAddress,
       "sfpsAliasTableAliasAge": sfpsAliasTableAliasAge,
       "sfpsAliasTableSwitchOctets": sfpsAliasTableSwitchOctets,
       "sfpsAliasTableBaseOctets": sfpsAliasTableBaseOctets,
       "sfpsAliasTableAliasOctets": sfpsAliasTableAliasOctets,
       "sfpsAliasTableOpaqueTag": sfpsAliasTableOpaqueTag,
       "sfpsAliasTableVlanPolicy": sfpsAliasTableVlanPolicy,
       "sfpsAliasTableBaseLock": sfpsAliasTableBaseLock,
       "sfpsAliasTableAliasLock": sfpsAliasTableAliasLock,
       "sfpsAliasTableAliasState": sfpsAliasTableAliasState,
       "sfpsAliasTableSelf": sfpsAliasTableSelf,
       "sfpsAliasTableNext": sfpsAliasTableNext,
       "sfpsAliasTablePrev": sfpsAliasTablePrev,
       "sfpsAliasDeltaTable": sfpsAliasDeltaTable,
       "sfpsAliasDeltaTableEntry": sfpsAliasDeltaTableEntry,
       "sfpsAliasDeltaTableIndex": sfpsAliasDeltaTableIndex,
       "sfpsAliasDeltaTablePort": sfpsAliasDeltaTablePort,
       "sfpsAliasDeltaTableBase": sfpsAliasDeltaTableBase,
       "sfpsAliasDeltaTableAlias": sfpsAliasDeltaTableAlias,
       "sfpsAliasDeltaTableAliasLength": sfpsAliasDeltaTableAliasLength,
       "sfpsAliasDeltaTableOpaqueTag": sfpsAliasDeltaTableOpaqueTag,
       "sfpsAliasDeltaTableAliasState": sfpsAliasDeltaTableAliasState,
       "sfpsAliasDeltaTableNodeLock": sfpsAliasDeltaTableNodeLock,
       "sfpsAliasDeltaTableAliasLock": sfpsAliasDeltaTableAliasLock,
       "sfpsAliasDeltaTableTimestamp": sfpsAliasDeltaTableTimestamp,
       "sfpsAliasDeltaCount": sfpsAliasDeltaCount,
       "sfpsAliasDeltaSetBack": sfpsAliasDeltaSetBack,
       "sfpsAliasDeltaFullFlag": sfpsAliasDeltaFullFlag,
       "sfpsDAPITestVerb": sfpsDAPITestVerb,
       "sfpsDAPITestSwitchMac": sfpsDAPITestSwitchMac,
       "sfpsDAPITestPort": sfpsDAPITestPort,
       "sfpsDAPITestAddrOneTag": sfpsDAPITestAddrOneTag,
       "sfpsDAPITestAddrOneValue": sfpsDAPITestAddrOneValue,
       "sfpsDAPITestAddrTwoTag": sfpsDAPITestAddrTwoTag,
       "sfpsDAPITestAddrTwoValue": sfpsDAPITestAddrTwoValue,
       "sfpsDAPITestCallTag": sfpsDAPITestCallTag,
       "sfpsDAPITestOutputTable": sfpsDAPITestOutputTable,
       "sfpsDAPITestOutputEntry": sfpsDAPITestOutputEntry,
       "sfpsDAPITestOutputIndex": sfpsDAPITestOutputIndex,
       "sfpsDAPITestOutputSwitchMac": sfpsDAPITestOutputSwitchMac,
       "sfpsDAPITestOutputPort": sfpsDAPITestOutputPort,
       "sfpsDAPITestOutputAddrOneTag": sfpsDAPITestOutputAddrOneTag,
       "sfpsDAPITestOutputAddrOneValue": sfpsDAPITestOutputAddrOneValue,
       "sfpsDAPITestOutputAddrTwoTag": sfpsDAPITestOutputAddrTwoTag,
       "sfpsDAPITestOutputAddrTwoValue": sfpsDAPITestOutputAddrTwoValue,
       "sfpsDAPITestOutputCallTag": sfpsDAPITestOutputCallTag,
       "sfpsDAPIVerb": sfpsDAPIVerb,
       "sfpsDAPIPort": sfpsDAPIPort,
       "sfpsDAPINodeType": sfpsDAPINodeType,
       "sfpsDAPINodeValue": sfpsDAPINodeValue,
       "sfpsDAPIAliasType": sfpsDAPIAliasType,
       "sfpsDAPIAliasValue": sfpsDAPIAliasValue,
       "sfpsDAPIAge": sfpsDAPIAge,
       "sfpsTopologyDirStatsTotalUsage": sfpsTopologyDirStatsTotalUsage,
       "sfpsTopologyDirStatsDynamicUsage": sfpsTopologyDirStatsDynamicUsage,
       "sfpsTopologyDirStatsNumOfNodes": sfpsTopologyDirStatsNumOfNodes,
       "sfpsTopologyDirStatsNodeUsage": sfpsTopologyDirStatsNodeUsage,
       "sfpsTopologyDirStatsNumLocalNodes": sfpsTopologyDirStatsNumLocalNodes,
       "sfpsTopologyDirStatsLocalNodeUsage": sfpsTopologyDirStatsLocalNodeUsage,
       "sfpsTopologyDirStatsMaxLocalNodes": sfpsTopologyDirStatsMaxLocalNodes,
       "sfpsTopologyDirStatsNumRemoteNodes": sfpsTopologyDirStatsNumRemoteNodes,
       "sfpsTopologyDirStatsRemoteNodeUsage": sfpsTopologyDirStatsRemoteNodeUsage,
       "sfpsTopologyDirStatsMaxRemoteNodes": sfpsTopologyDirStatsMaxRemoteNodes,
       "sfpsTopologyDirStatsNumOfAliases": sfpsTopologyDirStatsNumOfAliases,
       "sfpsTopologyDirStatsAliasUsage": sfpsTopologyDirStatsAliasUsage,
       "sfpsDirAliasStatsTable": sfpsDirAliasStatsTable,
       "sfpsDirAliasStatsEntry": sfpsDirAliasStatsEntry,
       "sfpsDirAliasStatsAliasType": sfpsDirAliasStatsAliasType,
       "sfpsDirAliasStatsAliasName": sfpsDirAliasStatsAliasName,
       "sfpsDirAliasStatsNumOfAliases": sfpsDirAliasStatsNumOfAliases,
       "sfpsDirAliasStatsAliasUsage": sfpsDirAliasStatsAliasUsage,
       "sfpsDirAliasStatsMaxAliases": sfpsDirAliasStatsMaxAliases,
       "sfpsTopologyDirStatsStaticUsage": sfpsTopologyDirStatsStaticUsage,
       "sfpsTopologyDirStatsObjectsUsage": sfpsTopologyDirStatsObjectsUsage,
       "sfpsTopologyDirStatsNodeTableSize": sfpsTopologyDirStatsNodeTableSize,
       "sfpsTopologyDirStatsNodeTableUsage": sfpsTopologyDirStatsNodeTableUsage,
       "sfpsTopologyDirStatsAliasTableSize": sfpsTopologyDirStatsAliasTableSize,
       "sfpsTopologyDirStatsAliasTableUsage": sfpsTopologyDirStatsAliasTableUsage,
       "sfpsTopologyDirStatsNodeCollisions": sfpsTopologyDirStatsNodeCollisions,
       "sfpsTopologyDirStatsNodeLongestChain": sfpsTopologyDirStatsNodeLongestChain,
       "sfpsTopologyDirStatsAliasCollisions": sfpsTopologyDirStatsAliasCollisions,
       "sfpsTopologyDirStatsAliasLongestChain": sfpsTopologyDirStatsAliasLongestChain,
       "sfpsTopologyDirStatsLocalAddsRefused": sfpsTopologyDirStatsLocalAddsRefused,
       "sfpsTopologyDirStatsAliasRemotesReplaced": sfpsTopologyDirStatsAliasRemotesReplaced,
       "sfpsTopologyDirStatsAliasMultiPortClears": sfpsTopologyDirStatsAliasMultiPortClears,
       "sfpsTopologyDirStatsReservedForRemoteNodes": sfpsTopologyDirStatsReservedForRemoteNodes,
       "sfpsTopologyDirStatsNumSwitches": sfpsTopologyDirStatsNumSwitches,
       "sfpsTopologyDirStatsSwitchUsage": sfpsTopologyDirStatsSwitchUsage,
       "sfpsTopologyDirStatsMaxSwitches": sfpsTopologyDirStatsMaxSwitches,
       "sfpsTopologyDirStatsSwitchTableSize": sfpsTopologyDirStatsSwitchTableSize,
       "sfpsTopologyDirStatsSwitchTableUsage": sfpsTopologyDirStatsSwitchTableUsage,
       "sfpsTopologyDirStatsSwitchLookups": sfpsTopologyDirStatsSwitchLookups,
       "sfpsTopologyDirStatsSwitchCacheHits": sfpsTopologyDirStatsSwitchCacheHits,
       "sfpsTopologyDirStatsNumVlans": sfpsTopologyDirStatsNumVlans,
       "sfpsTopologyDirStatsVlanUsage": sfpsTopologyDirStatsVlanUsage,
       "sfpsTopologyDirStatsMaxVlans": sfpsTopologyDirStatsMaxVlans,
       "sfpsTopologyDirStatsVlanTableSize": sfpsTopologyDirStatsVlanTableSize,
       "sfpsTopologyDirStatsVlanTableUsage": sfpsTopologyDirStatsVlanTableUsage,
       "sfpsTopologyDirStatsVlanLookups": sfpsTopologyDirStatsVlanLookups,
       "sfpsTopologyDirStatsVlanCacheHits": sfpsTopologyDirStatsVlanCacheHits,
       "sfpsTopologyDirStatsNodeAliasMax": sfpsTopologyDirStatsNodeAliasMax,
       "sfpsTopologyDirStatsLocalAliasRefused": sfpsTopologyDirStatsLocalAliasRefused,
       "sfpsTopologyDirStatsRemoteAliasRemoved": sfpsTopologyDirStatsRemoteAliasRemoved,
       "sfpsDirFilterAPILockAdmin": sfpsDirFilterAPILockAdmin,
       "sfpsDirFilterAPILockStatus": sfpsDirFilterAPILockStatus,
       "sfpsDirFilterAPILockCount": sfpsDirFilterAPILockCount,
       "sfpsDirFilterAPIValueType": sfpsDirFilterAPIValueType,
       "sfpsDirFilterAPIValue": sfpsDirFilterAPIValue,
       "sfpsDirFilterAPILockTimeOut": sfpsDirFilterAPILockTimeOut,
       "sfpsDirFilterAPILockTimeElapsed": sfpsDirFilterAPILockTimeElapsed,
       "sfpsDirFilterNodeTable": sfpsDirFilterNodeTable,
       "sfpsDirFilterNodeEntry": sfpsDirFilterNodeEntry,
       "sfpsDirFilterNodeLockCount": sfpsDirFilterNodeLockCount,
       "sfpsDirFilterNodeNodeIndex": sfpsDirFilterNodeNodeIndex,
       "sfpsDirFilterNodeLinkIndex": sfpsDirFilterNodeLinkIndex,
       "sfpsDirFilterNodeNodeCount": sfpsDirFilterNodeNodeCount,
       "sfpsDirFilterNodeLinkCount": sfpsDirFilterNodeLinkCount,
       "sfpsDirFilterNodeDomainName": sfpsDirFilterNodeDomainName,
       "sfpsDirFilterNodeChassisType": sfpsDirFilterNodeChassisType,
       "sfpsDirFilterNodeChassisLoad": sfpsDirFilterNodeChassisLoad,
       "sfpsDirFilterNodeSwitchType": sfpsDirFilterNodeSwitchType,
       "sfpsDirFilterNodeSwitchLoad": sfpsDirFilterNodeSwitchLoad,
       "sfpsDirFilterNodeInPort": sfpsDirFilterNodeInPort,
       "sfpsDirFilterNodeBaseType": sfpsDirFilterNodeBaseType,
       "sfpsDirFilterNodeBaseLoad": sfpsDirFilterNodeBaseLoad,
       "sfpsDirFilterNodeNodeState": sfpsDirFilterNodeNodeState,
       "sfpsDirFilterNodeNodeAge": sfpsDirFilterNodeNodeAge,
       "sfpsDirFilterNodeNodeLock": sfpsDirFilterNodeNodeLock,
       "sfpsDirFilterNodeLinkType": sfpsDirFilterNodeLinkType,
       "sfpsDirFilterNodeLinkLoad": sfpsDirFilterNodeLinkLoad,
       "sfpsDirFilterNodeLinkAge": sfpsDirFilterNodeLinkAge,
       "sfpsDirFilterNodeLinkLock": sfpsDirFilterNodeLinkLock,
       "sfpsDirFilterNodeVlanLearned": sfpsDirFilterNodeVlanLearned,
       "sfpsDirFilterNodeOpaqueTag": sfpsDirFilterNodeOpaqueTag,
       "sfpsDirFilterNodeChassisOctets": sfpsDirFilterNodeChassisOctets,
       "sfpsDirFilterNodeSwitchOctets": sfpsDirFilterNodeSwitchOctets,
       "sfpsDirFilterNodeNodeOctets": sfpsDirFilterNodeNodeOctets,
       "sfpsDirFilterNodeLinkOctets": sfpsDirFilterNodeLinkOctets,
       "sfpsDirFilterNodeNodeLocal": sfpsDirFilterNodeNodeLocal,
       "sfpsDirFilterNodeLinkState": sfpsDirFilterNodeLinkState,
       "sfpsDirFilterAliasTable": sfpsDirFilterAliasTable,
       "sfpsDirFilterAliasEntry": sfpsDirFilterAliasEntry,
       "sfpsDirFilterAliasLockCount": sfpsDirFilterAliasLockCount,
       "sfpsDirFilterAliasAliasHash": sfpsDirFilterAliasAliasHash,
       "sfpsDirFilterAliasBaseHash": sfpsDirFilterAliasBaseHash,
       "sfpsDirFilterAliasHashIndex": sfpsDirFilterAliasHashIndex,
       "sfpsDirFilterAliasDomain": sfpsDirFilterAliasDomain,
       "sfpsDirFilterAliasChassisType": sfpsDirFilterAliasChassisType,
       "sfpsDirFilterAliasChassisLoad": sfpsDirFilterAliasChassisLoad,
       "sfpsDirFilterAliasSwitchType": sfpsDirFilterAliasSwitchType,
       "sfpsDirFilterAliasSwitchLoad": sfpsDirFilterAliasSwitchLoad,
       "sfpsDirFilterAliasInPort": sfpsDirFilterAliasInPort,
       "sfpsDirFilterAliasBaseType": sfpsDirFilterAliasBaseType,
       "sfpsDirFilterAliasBaseLoad": sfpsDirFilterAliasBaseLoad,
       "sfpsDirFilterAliasNodeState": sfpsDirFilterAliasNodeState,
       "sfpsDirFilterAliasNodeAge": sfpsDirFilterAliasNodeAge,
       "sfpsDirFilterAliasNodeLock": sfpsDirFilterAliasNodeLock,
       "sfpsDirFilterAliasLinkType": sfpsDirFilterAliasLinkType,
       "sfpsDirFilterAliasLinkLoad": sfpsDirFilterAliasLinkLoad,
       "sfpsDirFilterAliasLinkAge": sfpsDirFilterAliasLinkAge,
       "sfpsDirFilterAliasLinkLock": sfpsDirFilterAliasLinkLock,
       "sfpsDirFilterAliasVlanLearned": sfpsDirFilterAliasVlanLearned,
       "sfpsDirFilterAliasOpaqueTag": sfpsDirFilterAliasOpaqueTag,
       "sfpsDirFilterAliasChassisOctets": sfpsDirFilterAliasChassisOctets,
       "sfpsDirFilterAliasSwitchOctets": sfpsDirFilterAliasSwitchOctets,
       "sfpsDirFilterAliasNodeOctets": sfpsDirFilterAliasNodeOctets,
       "sfpsDirFilterAliasLinkOctets": sfpsDirFilterAliasLinkOctets,
       "sfpsDirFilterAliasNodeLocal": sfpsDirFilterAliasNodeLocal,
       "sfpsDirFilterAliasLinkState": sfpsDirFilterAliasLinkState}
)
