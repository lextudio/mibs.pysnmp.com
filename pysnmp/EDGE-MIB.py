# SNMP MIB module (EDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:33 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Edge_ObjectIdentity = ObjectIdentity
edge = _Edge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24)
)
_EdgeServerStat_ObjectIdentity = ObjectIdentity
edgeServerStat = _EdgeServerStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1)
)
_EdgeServerStatTable_Object = MibTable
edgeServerStatTable = _EdgeServerStatTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    edgeServerStatTable.setStatus("mandatory")
_EdgeServerStatEntry_Object = MibTableRow
edgeServerStatEntry = _EdgeServerStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1)
)
edgeServerStatEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeSsIndex"),
)
if mibBuilder.loadTexts:
    edgeServerStatEntry.setStatus("mandatory")
_EdgeSsIndex_Type = Integer32
_EdgeSsIndex_Object = MibTableColumn
edgeSsIndex = _EdgeSsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 1),
    _EdgeSsIndex_Type()
)
edgeSsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsIndex.setStatus("mandatory")
_EdgeSsProcessorTime_Type = Integer32
_EdgeSsProcessorTime_Object = MibTableColumn
edgeSsProcessorTime = _EdgeSsProcessorTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 2),
    _EdgeSsProcessorTime_Type()
)
edgeSsProcessorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsProcessorTime.setStatus("mandatory")
_EdgeSsInterruptPerSec_Type = Integer32
_EdgeSsInterruptPerSec_Object = MibTableColumn
edgeSsInterruptPerSec = _EdgeSsInterruptPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 3),
    _EdgeSsInterruptPerSec_Type()
)
edgeSsInterruptPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsInterruptPerSec.setStatus("mandatory")
_EdgeSsDiskPercentUsed_Type = Integer32
_EdgeSsDiskPercentUsed_Object = MibTableColumn
edgeSsDiskPercentUsed = _EdgeSsDiskPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 4),
    _EdgeSsDiskPercentUsed_Type()
)
edgeSsDiskPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsDiskPercentUsed.setStatus("mandatory")
_EdgeSsFreeMegabytes_Type = Integer32
_EdgeSsFreeMegabytes_Object = MibTableColumn
edgeSsFreeMegabytes = _EdgeSsFreeMegabytes_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 5),
    _EdgeSsFreeMegabytes_Type()
)
edgeSsFreeMegabytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsFreeMegabytes.setStatus("mandatory")
_EdgeSsPercentDiskTime_Type = Integer32
_EdgeSsPercentDiskTime_Object = MibTableColumn
edgeSsPercentDiskTime = _EdgeSsPercentDiskTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 6),
    _EdgeSsPercentDiskTime_Type()
)
edgeSsPercentDiskTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsPercentDiskTime.setStatus("mandatory")
_EdgeSsPercentDiskReadTime_Type = Integer32
_EdgeSsPercentDiskReadTime_Object = MibTableColumn
edgeSsPercentDiskReadTime = _EdgeSsPercentDiskReadTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 7),
    _EdgeSsPercentDiskReadTime_Type()
)
edgeSsPercentDiskReadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsPercentDiskReadTime.setStatus("mandatory")
_EdgeSsPercentDiskWriteTime_Type = Integer32
_EdgeSsPercentDiskWriteTime_Object = MibTableColumn
edgeSsPercentDiskWriteTime = _EdgeSsPercentDiskWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 8),
    _EdgeSsPercentDiskWriteTime_Type()
)
edgeSsPercentDiskWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsPercentDiskWriteTime.setStatus("mandatory")
_EdgeSsMemoryPercentUsed_Type = Integer32
_EdgeSsMemoryPercentUsed_Object = MibTableColumn
edgeSsMemoryPercentUsed = _EdgeSsMemoryPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 9),
    _EdgeSsMemoryPercentUsed_Type()
)
edgeSsMemoryPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsMemoryPercentUsed.setStatus("mandatory")
_EdgeSsPageFaultsPerSec_Type = Integer32
_EdgeSsPageFaultsPerSec_Object = MibTableColumn
edgeSsPageFaultsPerSec = _EdgeSsPageFaultsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 10),
    _EdgeSsPageFaultsPerSec_Type()
)
edgeSsPageFaultsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsPageFaultsPerSec.setStatus("mandatory")


class _EdgeSsInfrastructManufacturer_Type(DisplayString):
    """Custom type edgeSsInfrastructManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EdgeSsInfrastructManufacturer_Type.__name__ = "DisplayString"
_EdgeSsInfrastructManufacturer_Object = MibTableColumn
edgeSsInfrastructManufacturer = _EdgeSsInfrastructManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 11),
    _EdgeSsInfrastructManufacturer_Type()
)
edgeSsInfrastructManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsInfrastructManufacturer.setStatus("mandatory")


class _EdgeSsedgeTechnology_Type(DisplayString):
    """Custom type edgeSsedgeTechnology based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EdgeSsedgeTechnology_Type.__name__ = "DisplayString"
_EdgeSsedgeTechnology_Object = MibTableColumn
edgeSsedgeTechnology = _EdgeSsedgeTechnology_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 12),
    _EdgeSsedgeTechnology_Type()
)
edgeSsedgeTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsedgeTechnology.setStatus("mandatory")


class _EdgeSsCurrentSwLoadRevision_Type(DisplayString):
    """Custom type edgeSsCurrentSwLoadRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EdgeSsCurrentSwLoadRevision_Type.__name__ = "DisplayString"
_EdgeSsCurrentSwLoadRevision_Object = MibTableColumn
edgeSsCurrentSwLoadRevision = _EdgeSsCurrentSwLoadRevision_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 13),
    _EdgeSsCurrentSwLoadRevision_Type()
)
edgeSsCurrentSwLoadRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsCurrentSwLoadRevision.setStatus("mandatory")


class _EdgeSsPreviousSwLoadRevision_Type(DisplayString):
    """Custom type edgeSsPreviousSwLoadRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EdgeSsPreviousSwLoadRevision_Type.__name__ = "DisplayString"
_EdgeSsPreviousSwLoadRevision_Object = MibTableColumn
edgeSsPreviousSwLoadRevision = _EdgeSsPreviousSwLoadRevision_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 14),
    _EdgeSsPreviousSwLoadRevision_Type()
)
edgeSsPreviousSwLoadRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsPreviousSwLoadRevision.setStatus("mandatory")


class _EdgeSsHwLoadRevision_Type(DisplayString):
    """Custom type edgeSsHwLoadRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_EdgeSsHwLoadRevision_Type.__name__ = "DisplayString"
_EdgeSsHwLoadRevision_Object = MibTableColumn
edgeSsHwLoadRevision = _EdgeSsHwLoadRevision_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 15),
    _EdgeSsHwLoadRevision_Type()
)
edgeSsHwLoadRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsHwLoadRevision.setStatus("mandatory")


class _EdgeSsComputerName_Type(DisplayString):
    """Custom type edgeSsComputerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EdgeSsComputerName_Type.__name__ = "DisplayString"
_EdgeSsComputerName_Object = MibTableColumn
edgeSsComputerName = _EdgeSsComputerName_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 16),
    _EdgeSsComputerName_Type()
)
edgeSsComputerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeSsComputerName.setStatus("mandatory")
_EdgeSsSysUpTime_Type = Counter32
_EdgeSsSysUpTime_Object = MibTableColumn
edgeSsSysUpTime = _EdgeSsSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 1, 1, 1, 17),
    _EdgeSsSysUpTime_Type()
)
edgeSsSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeSsSysUpTime.setStatus("mandatory")
_EdgeCfgDebugLevel_ObjectIdentity = ObjectIdentity
edgeCfgDebugLevel = _EdgeCfgDebugLevel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2)
)
_EdgeCfgDebugLevelTable_Object = MibTable
edgeCfgDebugLevelTable = _EdgeCfgDebugLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    edgeCfgDebugLevelTable.setStatus("mandatory")
_EdgeCfgDebugLevelEntry_Object = MibTableRow
edgeCfgDebugLevelEntry = _EdgeCfgDebugLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1)
)
edgeCfgDebugLevelEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeCfgDbgIndex"),
)
if mibBuilder.loadTexts:
    edgeCfgDebugLevelEntry.setStatus("mandatory")
_EdgeCfgDbgIndex_Type = Integer32
_EdgeCfgDbgIndex_Object = MibTableColumn
edgeCfgDbgIndex = _EdgeCfgDbgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 1),
    _EdgeCfgDbgIndex_Type()
)
edgeCfgDbgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCfgDbgIndex.setStatus("mandatory")


class _EdgeCfgDbgIp_Type(Integer32):
    """Custom type edgeCfgDbgIp based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgIp_Type.__name__ = "Integer32"
_EdgeCfgDbgIp_Object = MibTableColumn
edgeCfgDbgIp = _EdgeCfgDbgIp_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 2),
    _EdgeCfgDbgIp_Type()
)
edgeCfgDbgIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgIp.setStatus("mandatory")


class _EdgeCfgDbgPPP_Type(Integer32):
    """Custom type edgeCfgDbgPPP based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgPPP_Type.__name__ = "Integer32"
_EdgeCfgDbgPPP_Object = MibTableColumn
edgeCfgDbgPPP = _EdgeCfgDbgPPP_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 3),
    _EdgeCfgDbgPPP_Type()
)
edgeCfgDbgPPP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgPPP.setStatus("mandatory")


class _EdgeCfgDbgTDM_Type(Integer32):
    """Custom type edgeCfgDbgTDM based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgTDM_Type.__name__ = "Integer32"
_EdgeCfgDbgTDM_Object = MibTableColumn
edgeCfgDbgTDM = _EdgeCfgDbgTDM_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 4),
    _EdgeCfgDbgTDM_Type()
)
edgeCfgDbgTDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgTDM.setStatus("mandatory")


class _EdgeCfgDbgFrameService_Type(Integer32):
    """Custom type edgeCfgDbgFrameService based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgFrameService_Type.__name__ = "Integer32"
_EdgeCfgDbgFrameService_Object = MibTableColumn
edgeCfgDbgFrameService = _EdgeCfgDbgFrameService_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 5),
    _EdgeCfgDbgFrameService_Type()
)
edgeCfgDbgFrameService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgFrameService.setStatus("mandatory")


class _EdgeCfgDbgPacketBus_Type(Integer32):
    """Custom type edgeCfgDbgPacketBus based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgPacketBus_Type.__name__ = "Integer32"
_EdgeCfgDbgPacketBus_Object = MibTableColumn
edgeCfgDbgPacketBus = _EdgeCfgDbgPacketBus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 6),
    _EdgeCfgDbgPacketBus_Type()
)
edgeCfgDbgPacketBus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgPacketBus.setStatus("mandatory")


class _EdgeCfgDbgCallControl_Type(Integer32):
    """Custom type edgeCfgDbgCallControl based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgCallControl_Type.__name__ = "Integer32"
_EdgeCfgDbgCallControl_Object = MibTableColumn
edgeCfgDbgCallControl = _EdgeCfgDbgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 7),
    _EdgeCfgDbgCallControl_Type()
)
edgeCfgDbgCallControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgCallControl.setStatus("mandatory")


class _EdgeCfgDbgDataTransfer_Type(Integer32):
    """Custom type edgeCfgDbgDataTransfer based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgDataTransfer_Type.__name__ = "Integer32"
_EdgeCfgDbgDataTransfer_Object = MibTableColumn
edgeCfgDbgDataTransfer = _EdgeCfgDbgDataTransfer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 8),
    _EdgeCfgDbgDataTransfer_Type()
)
edgeCfgDbgDataTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgDataTransfer.setStatus("mandatory")


class _EdgeCfgDbgCompression_Type(Integer32):
    """Custom type edgeCfgDbgCompression based on Integer32"""
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
        *(("high", 4),
          ("medium", 3),
          ("minimum", 2),
          ("none", 1))
    )


_EdgeCfgDbgCompression_Type.__name__ = "Integer32"
_EdgeCfgDbgCompression_Object = MibTableColumn
edgeCfgDbgCompression = _EdgeCfgDbgCompression_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 2, 1, 1, 9),
    _EdgeCfgDbgCompression_Type()
)
edgeCfgDbgCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCfgDbgCompression.setStatus("mandatory")
_EdgeMemUtlTrap_ObjectIdentity = ObjectIdentity
edgeMemUtlTrap = _EdgeMemUtlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3)
)
_EdgeMemUtlTrapTable_Object = MibTable
edgeMemUtlTrapTable = _EdgeMemUtlTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1)
)
if mibBuilder.loadTexts:
    edgeMemUtlTrapTable.setStatus("mandatory")
_EdgeMemUtlTrapEntry_Object = MibTableRow
edgeMemUtlTrapEntry = _EdgeMemUtlTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1)
)
edgeMemUtlTrapEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeMemUtlTrIndex"),
)
if mibBuilder.loadTexts:
    edgeMemUtlTrapEntry.setStatus("mandatory")
_EdgeMemUtlTrIndex_Type = Integer32
_EdgeMemUtlTrIndex_Object = MibTableColumn
edgeMemUtlTrIndex = _EdgeMemUtlTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 1),
    _EdgeMemUtlTrIndex_Type()
)
edgeMemUtlTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeMemUtlTrIndex.setStatus("mandatory")


class _EdgeMemUtlTrMrgOperStatus_Type(Integer32):
    """Custom type edgeMemUtlTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeMemUtlTrMrgOperStatus_Type.__name__ = "Integer32"
_EdgeMemUtlTrMrgOperStatus_Object = MibTableColumn
edgeMemUtlTrMrgOperStatus = _EdgeMemUtlTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 2),
    _EdgeMemUtlTrMrgOperStatus_Type()
)
edgeMemUtlTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrMrgOperStatus.setStatus("mandatory")


class _EdgeMemUtlTrNonOperStatus_Type(Integer32):
    """Custom type edgeMemUtlTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeMemUtlTrNonOperStatus_Type.__name__ = "Integer32"
_EdgeMemUtlTrNonOperStatus_Object = MibTableColumn
edgeMemUtlTrNonOperStatus = _EdgeMemUtlTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 3),
    _EdgeMemUtlTrNonOperStatus_Type()
)
edgeMemUtlTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrNonOperStatus.setStatus("mandatory")


class _EdgeMemUtlTrClearStatus_Type(Integer32):
    """Custom type edgeMemUtlTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeMemUtlTrClearStatus_Type.__name__ = "Integer32"
_EdgeMemUtlTrClearStatus_Object = MibTableColumn
edgeMemUtlTrClearStatus = _EdgeMemUtlTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 4),
    _EdgeMemUtlTrClearStatus_Type()
)
edgeMemUtlTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrClearStatus.setStatus("mandatory")
_EdgeMemUtlTrMrgOperThreshCnt_Type = Integer32
_EdgeMemUtlTrMrgOperThreshCnt_Object = MibTableColumn
edgeMemUtlTrMrgOperThreshCnt = _EdgeMemUtlTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 5),
    _EdgeMemUtlTrMrgOperThreshCnt_Type()
)
edgeMemUtlTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrMrgOperThreshCnt.setStatus("mandatory")
_EdgeMemUtlTrNonOperThreshCnt_Type = Integer32
_EdgeMemUtlTrNonOperThreshCnt_Object = MibTableColumn
edgeMemUtlTrNonOperThreshCnt = _EdgeMemUtlTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 6),
    _EdgeMemUtlTrNonOperThreshCnt_Type()
)
edgeMemUtlTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrNonOperThreshCnt.setStatus("mandatory")
_EdgeMemUtlTrClearThreshCnt_Type = Integer32
_EdgeMemUtlTrClearThreshCnt_Object = MibTableColumn
edgeMemUtlTrClearThreshCnt = _EdgeMemUtlTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 7),
    _EdgeMemUtlTrClearThreshCnt_Type()
)
edgeMemUtlTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrClearThreshCnt.setStatus("mandatory")
_EdgeMemUtlTrMrgOperThreshTimer_Type = Integer32
_EdgeMemUtlTrMrgOperThreshTimer_Object = MibTableColumn
edgeMemUtlTrMrgOperThreshTimer = _EdgeMemUtlTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 8),
    _EdgeMemUtlTrMrgOperThreshTimer_Type()
)
edgeMemUtlTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrMrgOperThreshTimer.setStatus("mandatory")
_EdgeMemUtlTrNonOperThreshTimer_Type = Integer32
_EdgeMemUtlTrNonOperThreshTimer_Object = MibTableColumn
edgeMemUtlTrNonOperThreshTimer = _EdgeMemUtlTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 9),
    _EdgeMemUtlTrNonOperThreshTimer_Type()
)
edgeMemUtlTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrNonOperThreshTimer.setStatus("mandatory")
_EdgeMemUtlTrClearThreshTimer_Type = Integer32
_EdgeMemUtlTrClearThreshTimer_Object = MibTableColumn
edgeMemUtlTrClearThreshTimer = _EdgeMemUtlTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 10),
    _EdgeMemUtlTrClearThreshTimer_Type()
)
edgeMemUtlTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeMemUtlTrClearThreshTimer.setStatus("mandatory")


class _EdgeMemUtlTrStatus_Type(Integer32):
    """Custom type edgeMemUtlTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_EdgeMemUtlTrStatus_Type.__name__ = "Integer32"
_EdgeMemUtlTrStatus_Object = MibTableColumn
edgeMemUtlTrStatus = _EdgeMemUtlTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 3, 1, 1, 11),
    _EdgeMemUtlTrStatus_Type()
)
edgeMemUtlTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeMemUtlTrStatus.setStatus("mandatory")
_EdgeCpuUtlTrap_ObjectIdentity = ObjectIdentity
edgeCpuUtlTrap = _EdgeCpuUtlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4)
)
_EdgeCpuUtlTrapTable_Object = MibTable
edgeCpuUtlTrapTable = _EdgeCpuUtlTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1)
)
if mibBuilder.loadTexts:
    edgeCpuUtlTrapTable.setStatus("mandatory")
_EdgeCpuUtlTrapEntry_Object = MibTableRow
edgeCpuUtlTrapEntry = _EdgeCpuUtlTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1)
)
edgeCpuUtlTrapEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeCpuUtlTrIndex"),
)
if mibBuilder.loadTexts:
    edgeCpuUtlTrapEntry.setStatus("mandatory")
_EdgeCpuUtlTrIndex_Type = Integer32
_EdgeCpuUtlTrIndex_Object = MibTableColumn
edgeCpuUtlTrIndex = _EdgeCpuUtlTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 1),
    _EdgeCpuUtlTrIndex_Type()
)
edgeCpuUtlTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCpuUtlTrIndex.setStatus("mandatory")


class _EdgeCpuUtlTrMrgOperStatus_Type(Integer32):
    """Custom type edgeCpuUtlTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeCpuUtlTrMrgOperStatus_Type.__name__ = "Integer32"
_EdgeCpuUtlTrMrgOperStatus_Object = MibTableColumn
edgeCpuUtlTrMrgOperStatus = _EdgeCpuUtlTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 2),
    _EdgeCpuUtlTrMrgOperStatus_Type()
)
edgeCpuUtlTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrMrgOperStatus.setStatus("mandatory")


class _EdgeCpuUtlTrNonOperStatus_Type(Integer32):
    """Custom type edgeCpuUtlTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeCpuUtlTrNonOperStatus_Type.__name__ = "Integer32"
_EdgeCpuUtlTrNonOperStatus_Object = MibTableColumn
edgeCpuUtlTrNonOperStatus = _EdgeCpuUtlTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 3),
    _EdgeCpuUtlTrNonOperStatus_Type()
)
edgeCpuUtlTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrNonOperStatus.setStatus("mandatory")


class _EdgeCpuUtlTrClearStatus_Type(Integer32):
    """Custom type edgeCpuUtlTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeCpuUtlTrClearStatus_Type.__name__ = "Integer32"
_EdgeCpuUtlTrClearStatus_Object = MibTableColumn
edgeCpuUtlTrClearStatus = _EdgeCpuUtlTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 4),
    _EdgeCpuUtlTrClearStatus_Type()
)
edgeCpuUtlTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrClearStatus.setStatus("mandatory")
_EdgeCpuUtlTrMrgOperThreshCnt_Type = Integer32
_EdgeCpuUtlTrMrgOperThreshCnt_Object = MibTableColumn
edgeCpuUtlTrMrgOperThreshCnt = _EdgeCpuUtlTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 5),
    _EdgeCpuUtlTrMrgOperThreshCnt_Type()
)
edgeCpuUtlTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrMrgOperThreshCnt.setStatus("mandatory")
_EdgeCpuUtlTrNonOperThreshCnt_Type = Integer32
_EdgeCpuUtlTrNonOperThreshCnt_Object = MibTableColumn
edgeCpuUtlTrNonOperThreshCnt = _EdgeCpuUtlTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 6),
    _EdgeCpuUtlTrNonOperThreshCnt_Type()
)
edgeCpuUtlTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrNonOperThreshCnt.setStatus("mandatory")
_EdgeCpuUtlTrClearThreshCnt_Type = Integer32
_EdgeCpuUtlTrClearThreshCnt_Object = MibTableColumn
edgeCpuUtlTrClearThreshCnt = _EdgeCpuUtlTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 7),
    _EdgeCpuUtlTrClearThreshCnt_Type()
)
edgeCpuUtlTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrClearThreshCnt.setStatus("mandatory")
_EdgeCpuUtlTrMrgOperThreshTimer_Type = Integer32
_EdgeCpuUtlTrMrgOperThreshTimer_Object = MibTableColumn
edgeCpuUtlTrMrgOperThreshTimer = _EdgeCpuUtlTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 8),
    _EdgeCpuUtlTrMrgOperThreshTimer_Type()
)
edgeCpuUtlTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrMrgOperThreshTimer.setStatus("mandatory")
_EdgeCpuUtlTrNonOperThreshTimer_Type = Integer32
_EdgeCpuUtlTrNonOperThreshTimer_Object = MibTableColumn
edgeCpuUtlTrNonOperThreshTimer = _EdgeCpuUtlTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 9),
    _EdgeCpuUtlTrNonOperThreshTimer_Type()
)
edgeCpuUtlTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrNonOperThreshTimer.setStatus("mandatory")
_EdgeCpuUtlTrClearThreshTimer_Type = Integer32
_EdgeCpuUtlTrClearThreshTimer_Object = MibTableColumn
edgeCpuUtlTrClearThreshTimer = _EdgeCpuUtlTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 10),
    _EdgeCpuUtlTrClearThreshTimer_Type()
)
edgeCpuUtlTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCpuUtlTrClearThreshTimer.setStatus("mandatory")


class _EdgeCpuUtlTrStatus_Type(Integer32):
    """Custom type edgeCpuUtlTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_EdgeCpuUtlTrStatus_Type.__name__ = "Integer32"
_EdgeCpuUtlTrStatus_Object = MibTableColumn
edgeCpuUtlTrStatus = _EdgeCpuUtlTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 4, 1, 1, 11),
    _EdgeCpuUtlTrStatus_Type()
)
edgeCpuUtlTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCpuUtlTrStatus.setStatus("mandatory")
_EdgeDskUtlTrap_ObjectIdentity = ObjectIdentity
edgeDskUtlTrap = _EdgeDskUtlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5)
)
_EdgeDskUtlTrapTable_Object = MibTable
edgeDskUtlTrapTable = _EdgeDskUtlTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1)
)
if mibBuilder.loadTexts:
    edgeDskUtlTrapTable.setStatus("mandatory")
_EdgeDskUtlTrapEntry_Object = MibTableRow
edgeDskUtlTrapEntry = _EdgeDskUtlTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1)
)
edgeDskUtlTrapEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeDskUtlTrIndex"),
)
if mibBuilder.loadTexts:
    edgeDskUtlTrapEntry.setStatus("mandatory")
_EdgeDskUtlTrIndex_Type = Integer32
_EdgeDskUtlTrIndex_Object = MibTableColumn
edgeDskUtlTrIndex = _EdgeDskUtlTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 1),
    _EdgeDskUtlTrIndex_Type()
)
edgeDskUtlTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeDskUtlTrIndex.setStatus("mandatory")


class _EdgeDskUtlTrMrgOperStatus_Type(Integer32):
    """Custom type edgeDskUtlTrMrgOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeDskUtlTrMrgOperStatus_Type.__name__ = "Integer32"
_EdgeDskUtlTrMrgOperStatus_Object = MibTableColumn
edgeDskUtlTrMrgOperStatus = _EdgeDskUtlTrMrgOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 2),
    _EdgeDskUtlTrMrgOperStatus_Type()
)
edgeDskUtlTrMrgOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrMrgOperStatus.setStatus("mandatory")


class _EdgeDskUtlTrNonOperStatus_Type(Integer32):
    """Custom type edgeDskUtlTrNonOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeDskUtlTrNonOperStatus_Type.__name__ = "Integer32"
_EdgeDskUtlTrNonOperStatus_Object = MibTableColumn
edgeDskUtlTrNonOperStatus = _EdgeDskUtlTrNonOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 3),
    _EdgeDskUtlTrNonOperStatus_Type()
)
edgeDskUtlTrNonOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrNonOperStatus.setStatus("mandatory")


class _EdgeDskUtlTrClearStatus_Type(Integer32):
    """Custom type edgeDskUtlTrClearStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableTraps", 2),
          ("enableTraps", 1))
    )


_EdgeDskUtlTrClearStatus_Type.__name__ = "Integer32"
_EdgeDskUtlTrClearStatus_Object = MibTableColumn
edgeDskUtlTrClearStatus = _EdgeDskUtlTrClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 4),
    _EdgeDskUtlTrClearStatus_Type()
)
edgeDskUtlTrClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrClearStatus.setStatus("mandatory")
_EdgeDskUtlTrMrgOperThreshCnt_Type = Integer32
_EdgeDskUtlTrMrgOperThreshCnt_Object = MibTableColumn
edgeDskUtlTrMrgOperThreshCnt = _EdgeDskUtlTrMrgOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 5),
    _EdgeDskUtlTrMrgOperThreshCnt_Type()
)
edgeDskUtlTrMrgOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrMrgOperThreshCnt.setStatus("mandatory")
_EdgeDskUtlTrNonOperThreshCnt_Type = Integer32
_EdgeDskUtlTrNonOperThreshCnt_Object = MibTableColumn
edgeDskUtlTrNonOperThreshCnt = _EdgeDskUtlTrNonOperThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 6),
    _EdgeDskUtlTrNonOperThreshCnt_Type()
)
edgeDskUtlTrNonOperThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrNonOperThreshCnt.setStatus("mandatory")
_EdgeDskUtlTrClearThreshCnt_Type = Integer32
_EdgeDskUtlTrClearThreshCnt_Object = MibTableColumn
edgeDskUtlTrClearThreshCnt = _EdgeDskUtlTrClearThreshCnt_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 7),
    _EdgeDskUtlTrClearThreshCnt_Type()
)
edgeDskUtlTrClearThreshCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrClearThreshCnt.setStatus("mandatory")
_EdgeDskUtlTrMrgOperThreshTimer_Type = Integer32
_EdgeDskUtlTrMrgOperThreshTimer_Object = MibTableColumn
edgeDskUtlTrMrgOperThreshTimer = _EdgeDskUtlTrMrgOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 8),
    _EdgeDskUtlTrMrgOperThreshTimer_Type()
)
edgeDskUtlTrMrgOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrMrgOperThreshTimer.setStatus("mandatory")
_EdgeDskUtlTrNonOperThreshTimer_Type = Integer32
_EdgeDskUtlTrNonOperThreshTimer_Object = MibTableColumn
edgeDskUtlTrNonOperThreshTimer = _EdgeDskUtlTrNonOperThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 9),
    _EdgeDskUtlTrNonOperThreshTimer_Type()
)
edgeDskUtlTrNonOperThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrNonOperThreshTimer.setStatus("mandatory")
_EdgeDskUtlTrClearThreshTimer_Type = Integer32
_EdgeDskUtlTrClearThreshTimer_Object = MibTableColumn
edgeDskUtlTrClearThreshTimer = _EdgeDskUtlTrClearThreshTimer_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 10),
    _EdgeDskUtlTrClearThreshTimer_Type()
)
edgeDskUtlTrClearThreshTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeDskUtlTrClearThreshTimer.setStatus("mandatory")


class _EdgeDskUtlTrStatus_Type(Integer32):
    """Custom type edgeDskUtlTrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("marginallyOperational", 2),
          ("nonOperational", 3),
          ("operational", 1))
    )


_EdgeDskUtlTrStatus_Type.__name__ = "Integer32"
_EdgeDskUtlTrStatus_Object = MibTableColumn
edgeDskUtlTrStatus = _EdgeDskUtlTrStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 5, 1, 1, 11),
    _EdgeDskUtlTrStatus_Type()
)
edgeDskUtlTrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeDskUtlTrStatus.setStatus("mandatory")
_EdgeCmd_ObjectIdentity = ObjectIdentity
edgeCmd = _EdgeCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6)
)
_EdgeCmdTable_Object = MibTable
edgeCmdTable = _EdgeCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1)
)
if mibBuilder.loadTexts:
    edgeCmdTable.setStatus("mandatory")
_EdgeCmdEntry_Object = MibTableRow
edgeCmdEntry = _EdgeCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1)
)
edgeCmdEntry.setIndexNames(
    (0, "EDGE-MIB", "edgeCmdIndex"),
)
if mibBuilder.loadTexts:
    edgeCmdEntry.setStatus("mandatory")
_EdgeCmdIndex_Type = Integer32
_EdgeCmdIndex_Object = MibTableColumn
edgeCmdIndex = _EdgeCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 1),
    _EdgeCmdIndex_Type()
)
edgeCmdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCmdIndex.setStatus("mandatory")


class _EdgeCmdMgtStationId_Type(OctetString):
    """Custom type edgeCmdMgtStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_EdgeCmdMgtStationId_Type.__name__ = "OctetString"
_EdgeCmdMgtStationId_Object = MibTableColumn
edgeCmdMgtStationId = _EdgeCmdMgtStationId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 2),
    _EdgeCmdMgtStationId_Type()
)
edgeCmdMgtStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCmdMgtStationId.setStatus("mandatory")
_EdgeCmdReqId_Type = Integer32
_EdgeCmdReqId_Object = MibTableColumn
edgeCmdReqId = _EdgeCmdReqId_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 3),
    _EdgeCmdReqId_Type()
)
edgeCmdReqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCmdReqId.setStatus("mandatory")


class _EdgeCmdFunction_Type(Integer32):
    """Custom type edgeCmdFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("bulkfileUpload", 9),
          ("noCommand", 1),
          ("softwareReset", 7))
    )


_EdgeCmdFunction_Type.__name__ = "Integer32"
_EdgeCmdFunction_Object = MibTableColumn
edgeCmdFunction = _EdgeCmdFunction_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 4),
    _EdgeCmdFunction_Type()
)
edgeCmdFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCmdFunction.setStatus("mandatory")


class _EdgeCmdForce_Type(Integer32):
    """Custom type edgeCmdForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force", 1),
          ("noForce", 2))
    )


_EdgeCmdForce_Type.__name__ = "Integer32"
_EdgeCmdForce_Object = MibTableColumn
edgeCmdForce = _EdgeCmdForce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 5),
    _EdgeCmdForce_Type()
)
edgeCmdForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCmdForce.setStatus("mandatory")
_EdgeCmdParam_Type = OctetString
_EdgeCmdParam_Object = MibTableColumn
edgeCmdParam = _EdgeCmdParam_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 6),
    _EdgeCmdParam_Type()
)
edgeCmdParam.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    edgeCmdParam.setStatus("mandatory")


class _EdgeCmdResult_Type(Integer32):
    """Custom type edgeCmdResult based on Integer32"""
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
        *(("aborted", 6),
          ("failed", 7),
          ("inProgress", 3),
          ("none", 1),
          ("notSupported", 4),
          ("success", 2),
          ("unAbleToRun", 5))
    )


_EdgeCmdResult_Type.__name__ = "Integer32"
_EdgeCmdResult_Object = MibTableColumn
edgeCmdResult = _EdgeCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 7),
    _EdgeCmdResult_Type()
)
edgeCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCmdResult.setStatus("mandatory")


class _EdgeCmdCode_Type(Integer32):
    """Custom type edgeCmdCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              6,
              8,
              12,
              20,
              22,
              25,
              58,
              73)
        )
    )
    namedValues = NamedValues(
        *(("deviceDisabled", 22),
          ("noError", 1),
          ("noResponse", 12),
          ("pendingSoftwareDownload", 73),
          ("slotEmpty", 8),
          ("testFailed", 25),
          ("unable", 2),
          ("unrecognizedCommand", 6),
          ("unsupportedCommand", 20),
          ("userInterfaceActive", 58))
    )


_EdgeCmdCode_Type.__name__ = "Integer32"
_EdgeCmdCode_Object = MibTableColumn
edgeCmdCode = _EdgeCmdCode_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 24, 6, 1, 1, 8),
    _EdgeCmdCode_Type()
)
edgeCmdCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    edgeCmdCode.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDGE-MIB",
    **{"usr": usr,
       "nas": nas,
       "edge": edge,
       "edgeServerStat": edgeServerStat,
       "edgeServerStatTable": edgeServerStatTable,
       "edgeServerStatEntry": edgeServerStatEntry,
       "edgeSsIndex": edgeSsIndex,
       "edgeSsProcessorTime": edgeSsProcessorTime,
       "edgeSsInterruptPerSec": edgeSsInterruptPerSec,
       "edgeSsDiskPercentUsed": edgeSsDiskPercentUsed,
       "edgeSsFreeMegabytes": edgeSsFreeMegabytes,
       "edgeSsPercentDiskTime": edgeSsPercentDiskTime,
       "edgeSsPercentDiskReadTime": edgeSsPercentDiskReadTime,
       "edgeSsPercentDiskWriteTime": edgeSsPercentDiskWriteTime,
       "edgeSsMemoryPercentUsed": edgeSsMemoryPercentUsed,
       "edgeSsPageFaultsPerSec": edgeSsPageFaultsPerSec,
       "edgeSsInfrastructManufacturer": edgeSsInfrastructManufacturer,
       "edgeSsedgeTechnology": edgeSsedgeTechnology,
       "edgeSsCurrentSwLoadRevision": edgeSsCurrentSwLoadRevision,
       "edgeSsPreviousSwLoadRevision": edgeSsPreviousSwLoadRevision,
       "edgeSsHwLoadRevision": edgeSsHwLoadRevision,
       "edgeSsComputerName": edgeSsComputerName,
       "edgeSsSysUpTime": edgeSsSysUpTime,
       "edgeCfgDebugLevel": edgeCfgDebugLevel,
       "edgeCfgDebugLevelTable": edgeCfgDebugLevelTable,
       "edgeCfgDebugLevelEntry": edgeCfgDebugLevelEntry,
       "edgeCfgDbgIndex": edgeCfgDbgIndex,
       "edgeCfgDbgIp": edgeCfgDbgIp,
       "edgeCfgDbgPPP": edgeCfgDbgPPP,
       "edgeCfgDbgTDM": edgeCfgDbgTDM,
       "edgeCfgDbgFrameService": edgeCfgDbgFrameService,
       "edgeCfgDbgPacketBus": edgeCfgDbgPacketBus,
       "edgeCfgDbgCallControl": edgeCfgDbgCallControl,
       "edgeCfgDbgDataTransfer": edgeCfgDbgDataTransfer,
       "edgeCfgDbgCompression": edgeCfgDbgCompression,
       "edgeMemUtlTrap": edgeMemUtlTrap,
       "edgeMemUtlTrapTable": edgeMemUtlTrapTable,
       "edgeMemUtlTrapEntry": edgeMemUtlTrapEntry,
       "edgeMemUtlTrIndex": edgeMemUtlTrIndex,
       "edgeMemUtlTrMrgOperStatus": edgeMemUtlTrMrgOperStatus,
       "edgeMemUtlTrNonOperStatus": edgeMemUtlTrNonOperStatus,
       "edgeMemUtlTrClearStatus": edgeMemUtlTrClearStatus,
       "edgeMemUtlTrMrgOperThreshCnt": edgeMemUtlTrMrgOperThreshCnt,
       "edgeMemUtlTrNonOperThreshCnt": edgeMemUtlTrNonOperThreshCnt,
       "edgeMemUtlTrClearThreshCnt": edgeMemUtlTrClearThreshCnt,
       "edgeMemUtlTrMrgOperThreshTimer": edgeMemUtlTrMrgOperThreshTimer,
       "edgeMemUtlTrNonOperThreshTimer": edgeMemUtlTrNonOperThreshTimer,
       "edgeMemUtlTrClearThreshTimer": edgeMemUtlTrClearThreshTimer,
       "edgeMemUtlTrStatus": edgeMemUtlTrStatus,
       "edgeCpuUtlTrap": edgeCpuUtlTrap,
       "edgeCpuUtlTrapTable": edgeCpuUtlTrapTable,
       "edgeCpuUtlTrapEntry": edgeCpuUtlTrapEntry,
       "edgeCpuUtlTrIndex": edgeCpuUtlTrIndex,
       "edgeCpuUtlTrMrgOperStatus": edgeCpuUtlTrMrgOperStatus,
       "edgeCpuUtlTrNonOperStatus": edgeCpuUtlTrNonOperStatus,
       "edgeCpuUtlTrClearStatus": edgeCpuUtlTrClearStatus,
       "edgeCpuUtlTrMrgOperThreshCnt": edgeCpuUtlTrMrgOperThreshCnt,
       "edgeCpuUtlTrNonOperThreshCnt": edgeCpuUtlTrNonOperThreshCnt,
       "edgeCpuUtlTrClearThreshCnt": edgeCpuUtlTrClearThreshCnt,
       "edgeCpuUtlTrMrgOperThreshTimer": edgeCpuUtlTrMrgOperThreshTimer,
       "edgeCpuUtlTrNonOperThreshTimer": edgeCpuUtlTrNonOperThreshTimer,
       "edgeCpuUtlTrClearThreshTimer": edgeCpuUtlTrClearThreshTimer,
       "edgeCpuUtlTrStatus": edgeCpuUtlTrStatus,
       "edgeDskUtlTrap": edgeDskUtlTrap,
       "edgeDskUtlTrapTable": edgeDskUtlTrapTable,
       "edgeDskUtlTrapEntry": edgeDskUtlTrapEntry,
       "edgeDskUtlTrIndex": edgeDskUtlTrIndex,
       "edgeDskUtlTrMrgOperStatus": edgeDskUtlTrMrgOperStatus,
       "edgeDskUtlTrNonOperStatus": edgeDskUtlTrNonOperStatus,
       "edgeDskUtlTrClearStatus": edgeDskUtlTrClearStatus,
       "edgeDskUtlTrMrgOperThreshCnt": edgeDskUtlTrMrgOperThreshCnt,
       "edgeDskUtlTrNonOperThreshCnt": edgeDskUtlTrNonOperThreshCnt,
       "edgeDskUtlTrClearThreshCnt": edgeDskUtlTrClearThreshCnt,
       "edgeDskUtlTrMrgOperThreshTimer": edgeDskUtlTrMrgOperThreshTimer,
       "edgeDskUtlTrNonOperThreshTimer": edgeDskUtlTrNonOperThreshTimer,
       "edgeDskUtlTrClearThreshTimer": edgeDskUtlTrClearThreshTimer,
       "edgeDskUtlTrStatus": edgeDskUtlTrStatus,
       "edgeCmd": edgeCmd,
       "edgeCmdTable": edgeCmdTable,
       "edgeCmdEntry": edgeCmdEntry,
       "edgeCmdIndex": edgeCmdIndex,
       "edgeCmdMgtStationId": edgeCmdMgtStationId,
       "edgeCmdReqId": edgeCmdReqId,
       "edgeCmdFunction": edgeCmdFunction,
       "edgeCmdForce": edgeCmdForce,
       "edgeCmdParam": edgeCmdParam,
       "edgeCmdResult": edgeCmdResult,
       "edgeCmdCode": edgeCmdCode}
)
