# SNMP MIB module (LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:41 2024
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

(lhnModules,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG",
    "lhnModules")

(lhnNusCommonClustering,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-MIB",
    "lhnNusCommonClustering")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lhnNusCommonClusteringModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 1, 1, 14)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClusPermissionBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_ClusMgmtGroupName_Type = OctetString
_ClusMgmtGroupName_Object = MibScalar
clusMgmtGroupName = _ClusMgmtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 1),
    _ClusMgmtGroupName_Type()
)
clusMgmtGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupName.setStatus("current")
_ClusMgmtGroupIsEnabled_Type = TruthValue
_ClusMgmtGroupIsEnabled_Object = MibScalar
clusMgmtGroupIsEnabled = _ClusMgmtGroupIsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 2),
    _ClusMgmtGroupIsEnabled_Type()
)
clusMgmtGroupIsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupIsEnabled.setStatus("current")
_ClusMgmtGroupQuorum_Type = Integer32
_ClusMgmtGroupQuorum_Object = MibScalar
clusMgmtGroupQuorum = _ClusMgmtGroupQuorum_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 3),
    _ClusMgmtGroupQuorum_Type()
)
clusMgmtGroupQuorum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusMgmtGroupQuorum.setStatus("current")
_ClusMgmtGroupDescription_Type = OctetString
_ClusMgmtGroupDescription_Object = MibScalar
clusMgmtGroupDescription = _ClusMgmtGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 4),
    _ClusMgmtGroupDescription_Type()
)
clusMgmtGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusMgmtGroupDescription.setStatus("current")
_ClusMgmtGroupActiveManagerCount_Type = Integer32
_ClusMgmtGroupActiveManagerCount_Object = MibScalar
clusMgmtGroupActiveManagerCount = _ClusMgmtGroupActiveManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 5),
    _ClusMgmtGroupActiveManagerCount_Type()
)
clusMgmtGroupActiveManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupActiveManagerCount.setStatus("current")
_ClusMgmtGroupManagerCount_Type = Integer32
_ClusMgmtGroupManagerCount_Object = MibScalar
clusMgmtGroupManagerCount = _ClusMgmtGroupManagerCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 6),
    _ClusMgmtGroupManagerCount_Type()
)
clusMgmtGroupManagerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusMgmtGroupManagerCount.setStatus("current")
_ClusManagerTable_Object = MibTable
clusManagerTable = _ClusManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7)
)
if mibBuilder.loadTexts:
    clusManagerTable.setStatus("current")
_ClusManagerEntry_Object = MibTableRow
clusManagerEntry = _ClusManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1)
)
clusManagerEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusManagerIndex"),
)
if mibBuilder.loadTexts:
    clusManagerEntry.setStatus("current")
_ClusManagerIndex_Type = Integer32
_ClusManagerIndex_Object = MibTableColumn
clusManagerIndex = _ClusManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 1),
    _ClusManagerIndex_Type()
)
clusManagerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusManagerIndex.setStatus("current")
_ClusManagerName_Type = OctetString
_ClusManagerName_Object = MibTableColumn
clusManagerName = _ClusManagerName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 2),
    _ClusManagerName_Type()
)
clusManagerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerName.setStatus("current")
_ClusManagerVersion_Type = OctetString
_ClusManagerVersion_Object = MibTableColumn
clusManagerVersion = _ClusManagerVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 3),
    _ClusManagerVersion_Type()
)
clusManagerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerVersion.setStatus("current")
_ClusManagerHostSerialNo_Type = OctetString
_ClusManagerHostSerialNo_Object = MibTableColumn
clusManagerHostSerialNo = _ClusManagerHostSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 4),
    _ClusManagerHostSerialNo_Type()
)
clusManagerHostSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusManagerHostSerialNo.setStatus("current")


class _ClusManagerStatus_Type(Integer32):
    """Custom type clusManagerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ClusManagerStatus_Type.__name__ = "Integer32"
_ClusManagerStatus_Object = MibTableColumn
clusManagerStatus = _ClusManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 5),
    _ClusManagerStatus_Type()
)
clusManagerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusManagerStatus.setStatus("current")
_ClusManagerIsVirtual_Type = TruthValue
_ClusManagerIsVirtual_Object = MibTableColumn
clusManagerIsVirtual = _ClusManagerIsVirtual_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 7),
    _ClusManagerIsVirtual_Type()
)
clusManagerIsVirtual.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusManagerIsVirtual.setStatus("current")
_ClusManagerRowStatus_Type = RowStatus
_ClusManagerRowStatus_Object = MibTableColumn
clusManagerRowStatus = _ClusManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 7, 1, 8),
    _ClusManagerRowStatus_Type()
)
clusManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusManagerRowStatus.setStatus("current")
_ClusModuleCount_Type = Integer32
_ClusModuleCount_Object = MibScalar
clusModuleCount = _ClusModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 8),
    _ClusModuleCount_Type()
)
clusModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleCount.setStatus("current")
_ClusModuleTable_Object = MibTable
clusModuleTable = _ClusModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9)
)
if mibBuilder.loadTexts:
    clusModuleTable.setStatus("current")
_ClusModuleEntry_Object = MibTableRow
clusModuleEntry = _ClusModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1)
)
clusModuleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusModuleIndex"),
)
if mibBuilder.loadTexts:
    clusModuleEntry.setStatus("current")
_ClusModuleIndex_Type = Integer32
_ClusModuleIndex_Object = MibTableColumn
clusModuleIndex = _ClusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 1),
    _ClusModuleIndex_Type()
)
clusModuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleIndex.setStatus("current")
_ClusModuleName_Type = OctetString
_ClusModuleName_Object = MibTableColumn
clusModuleName = _ClusModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 2),
    _ClusModuleName_Type()
)
clusModuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleName.setStatus("current")
_ClusModuleVersion_Type = OctetString
_ClusModuleVersion_Object = MibTableColumn
clusModuleVersion = _ClusModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 3),
    _ClusModuleVersion_Type()
)
clusModuleVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleVersion.setStatus("current")
_ClusModuleSerialNo_Type = OctetString
_ClusModuleSerialNo_Object = MibTableColumn
clusModuleSerialNo = _ClusModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 4),
    _ClusModuleSerialNo_Type()
)
clusModuleSerialNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleSerialNo.setStatus("current")
_ClusModuleTotalSize_Type = Counter64
_ClusModuleTotalSize_Object = MibTableColumn
clusModuleTotalSize = _ClusModuleTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 5),
    _ClusModuleTotalSize_Type()
)
clusModuleTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleTotalSize.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleTotalSize.setUnits("kbytes")
_ClusModuleAvailSize_Type = Counter64
_ClusModuleAvailSize_Object = MibTableColumn
clusModuleAvailSize = _ClusModuleAvailSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 6),
    _ClusModuleAvailSize_Type()
)
clusModuleAvailSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleAvailSize.setStatus("current")
if mibBuilder.loadTexts:
    clusModuleAvailSize.setUnits("kbytes")
_ClusModuleIsManager_Type = TruthValue
_ClusModuleIsManager_Object = MibTableColumn
clusModuleIsManager = _ClusModuleIsManager_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 7),
    _ClusModuleIsManager_Type()
)
clusModuleIsManager.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleIsManager.setStatus("current")
_ClusModuleRaidConfiguration_Type = OctetString
_ClusModuleRaidConfiguration_Object = MibTableColumn
clusModuleRaidConfiguration = _ClusModuleRaidConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 8),
    _ClusModuleRaidConfiguration_Type()
)
clusModuleRaidConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleRaidConfiguration.setStatus("current")
_ClusModuleRaidStatus_Type = OctetString
_ClusModuleRaidStatus_Object = MibTableColumn
clusModuleRaidStatus = _ClusModuleRaidStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 9),
    _ClusModuleRaidStatus_Type()
)
clusModuleRaidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleRaidStatus.setStatus("current")


class _ClusModuleStorageStatus_Type(Integer32):
    """Custom type clusModuleStorageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ClusModuleStorageStatus_Type.__name__ = "Integer32"
_ClusModuleStorageStatus_Object = MibTableColumn
clusModuleStorageStatus = _ClusModuleStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 10),
    _ClusModuleStorageStatus_Type()
)
clusModuleStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageStatus.setStatus("current")
_ClusModuleStorageIsReady_Type = TruthValue
_ClusModuleStorageIsReady_Object = MibTableColumn
clusModuleStorageIsReady = _ClusModuleStorageIsReady_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 11),
    _ClusModuleStorageIsReady_Type()
)
clusModuleStorageIsReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleStorageIsReady.setStatus("current")
_ClusModuleCreationTime_Type = DateAndTime
_ClusModuleCreationTime_Object = MibTableColumn
clusModuleCreationTime = _ClusModuleCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 12),
    _ClusModuleCreationTime_Type()
)
clusModuleCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusModuleCreationTime.setStatus("current")
_ClusModuleDescription_Type = OctetString
_ClusModuleDescription_Object = MibTableColumn
clusModuleDescription = _ClusModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 13),
    _ClusModuleDescription_Type()
)
clusModuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusModuleDescription.setStatus("current")
_ClusModuleClusterName_Type = OctetString
_ClusModuleClusterName_Object = MibTableColumn
clusModuleClusterName = _ClusModuleClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 14),
    _ClusModuleClusterName_Type()
)
clusModuleClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusModuleClusterName.setStatus("current")
_ClusModuleRowStatus_Type = RowStatus
_ClusModuleRowStatus_Object = MibTableColumn
clusModuleRowStatus = _ClusModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 9, 1, 15),
    _ClusModuleRowStatus_Type()
)
clusModuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusModuleRowStatus.setStatus("current")
_ClusClusterCount_Type = Integer32
_ClusClusterCount_Object = MibScalar
clusClusterCount = _ClusClusterCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 10),
    _ClusClusterCount_Type()
)
clusClusterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterCount.setStatus("current")
_ClusClusterTable_Object = MibTable
clusClusterTable = _ClusClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11)
)
if mibBuilder.loadTexts:
    clusClusterTable.setStatus("current")
_ClusClusterEntry_Object = MibTableRow
clusClusterEntry = _ClusClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1)
)
clusClusterEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusClusterIndex"),
)
if mibBuilder.loadTexts:
    clusClusterEntry.setStatus("current")
_ClusClusterIndex_Type = Integer32
_ClusClusterIndex_Object = MibTableColumn
clusClusterIndex = _ClusClusterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 1),
    _ClusClusterIndex_Type()
)
clusClusterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterIndex.setStatus("current")
_ClusClusterName_Type = OctetString
_ClusClusterName_Object = MibTableColumn
clusClusterName = _ClusClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 2),
    _ClusClusterName_Type()
)
clusClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusClusterName.setStatus("current")
_ClusClusterModuleCount_Type = Counter32
_ClusClusterModuleCount_Object = MibTableColumn
clusClusterModuleCount = _ClusClusterModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 3),
    _ClusClusterModuleCount_Type()
)
clusClusterModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterModuleCount.setStatus("current")
_ClusClusterVolumeCount_Type = Counter32
_ClusClusterVolumeCount_Object = MibTableColumn
clusClusterVolumeCount = _ClusClusterVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 4),
    _ClusClusterVolumeCount_Type()
)
clusClusterVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusClusterVolumeCount.setStatus("current")
_ClusClusterDescription_Type = OctetString
_ClusClusterDescription_Object = MibTableColumn
clusClusterDescription = _ClusClusterDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 5),
    _ClusClusterDescription_Type()
)
clusClusterDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusClusterDescription.setStatus("current")
_ClusClusterRowStatus_Type = RowStatus
_ClusClusterRowStatus_Object = MibTableColumn
clusClusterRowStatus = _ClusClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 11, 1, 6),
    _ClusClusterRowStatus_Type()
)
clusClusterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterRowStatus.setStatus("current")
_ClusClusterModuleTable_Object = MibTable
clusClusterModuleTable = _ClusClusterModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12)
)
if mibBuilder.loadTexts:
    clusClusterModuleTable.setStatus("current")
_ClusClusterModuleEntry_Object = MibTableRow
clusClusterModuleEntry = _ClusClusterModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1)
)
clusClusterModuleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusClusterModuleIndex"),
)
if mibBuilder.loadTexts:
    clusClusterModuleEntry.setStatus("current")
_ClusClusterModuleIndex_Type = Integer32
_ClusClusterModuleIndex_Object = MibTableColumn
clusClusterModuleIndex = _ClusClusterModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1, 1),
    _ClusClusterModuleIndex_Type()
)
clusClusterModuleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterModuleIndex.setStatus("current")
_ClusClusterModuleName_Type = OctetString
_ClusClusterModuleName_Object = MibTableColumn
clusClusterModuleName = _ClusClusterModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1, 2),
    _ClusClusterModuleName_Type()
)
clusClusterModuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterModuleName.setStatus("current")
_ClusClusterModuleSerialNo_Type = OctetString
_ClusClusterModuleSerialNo_Object = MibTableColumn
clusClusterModuleSerialNo = _ClusClusterModuleSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1, 3),
    _ClusClusterModuleSerialNo_Type()
)
clusClusterModuleSerialNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterModuleSerialNo.setStatus("current")
_ClusClusterModuleIsHotSpare_Type = TruthValue
_ClusClusterModuleIsHotSpare_Object = MibTableColumn
clusClusterModuleIsHotSpare = _ClusClusterModuleIsHotSpare_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1, 4),
    _ClusClusterModuleIsHotSpare_Type()
)
clusClusterModuleIsHotSpare.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterModuleIsHotSpare.setStatus("current")
_ClusClusterModuleRowStatus_Type = RowStatus
_ClusClusterModuleRowStatus_Object = MibTableColumn
clusClusterModuleRowStatus = _ClusClusterModuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 12, 1, 5),
    _ClusClusterModuleRowStatus_Type()
)
clusClusterModuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterModuleRowStatus.setStatus("current")
_ClusVolumeCount_Type = Integer32
_ClusVolumeCount_Object = MibScalar
clusVolumeCount = _ClusVolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 13),
    _ClusVolumeCount_Type()
)
clusVolumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeCount.setStatus("current")
_ClusVolumeTable_Object = MibTable
clusVolumeTable = _ClusVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14)
)
if mibBuilder.loadTexts:
    clusVolumeTable.setStatus("current")
_ClusVolumeEntry_Object = MibTableRow
clusVolumeEntry = _ClusVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1)
)
clusVolumeEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeEntry.setStatus("current")
_ClusVolumeIndex_Type = Integer32
_ClusVolumeIndex_Object = MibTableColumn
clusVolumeIndex = _ClusVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 1),
    _ClusVolumeIndex_Type()
)
clusVolumeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeIndex.setStatus("current")
_ClusVolumeName_Type = OctetString
_ClusVolumeName_Object = MibTableColumn
clusVolumeName = _ClusVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 2),
    _ClusVolumeName_Type()
)
clusVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeName.setStatus("current")
_ClusVolumeCreationTime_Type = DateAndTime
_ClusVolumeCreationTime_Object = MibTableColumn
clusVolumeCreationTime = _ClusVolumeCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 3),
    _ClusVolumeCreationTime_Type()
)
clusVolumeCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeCreationTime.setStatus("current")
_ClusVolumeDescription_Type = OctetString
_ClusVolumeDescription_Object = MibTableColumn
clusVolumeDescription = _ClusVolumeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 4),
    _ClusVolumeDescription_Type()
)
clusVolumeDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeDescription.setStatus("current")
_ClusVolumeSize_Type = Counter64
_ClusVolumeSize_Object = MibTableColumn
clusVolumeSize = _ClusVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 5),
    _ClusVolumeSize_Type()
)
clusVolumeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSize.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSize.setUnits("kbytes")
_ClusVolumeSoftThreshold_Type = Counter64
_ClusVolumeSoftThreshold_Object = MibTableColumn
clusVolumeSoftThreshold = _ClusVolumeSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 6),
    _ClusVolumeSoftThreshold_Type()
)
clusVolumeSoftThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSoftThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSoftThreshold.setUnits("kbytes")
_ClusVolumeHardThreshold_Type = Counter64
_ClusVolumeHardThreshold_Object = MibTableColumn
clusVolumeHardThreshold = _ClusVolumeHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 7),
    _ClusVolumeHardThreshold_Type()
)
clusVolumeHardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeHardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeHardThreshold.setUnits("kbytes")
_ClusVolumeReplicaCount_Type = Counter32
_ClusVolumeReplicaCount_Object = MibTableColumn
clusVolumeReplicaCount = _ClusVolumeReplicaCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 8),
    _ClusVolumeReplicaCount_Type()
)
clusVolumeReplicaCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeReplicaCount.setStatus("current")
_ClusVolumeSnapshotCount_Type = Counter32
_ClusVolumeSnapshotCount_Object = MibTableColumn
clusVolumeSnapshotCount = _ClusVolumeSnapshotCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 9),
    _ClusVolumeSnapshotCount_Type()
)
clusVolumeSnapshotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCount.setStatus("current")
_ClusVolumeACLCount_Type = Counter32
_ClusVolumeACLCount_Object = MibTableColumn
clusVolumeACLCount = _ClusVolumeACLCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 10),
    _ClusVolumeACLCount_Type()
)
clusVolumeACLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeACLCount.setStatus("current")
_ClusVolumeClusterName_Type = OctetString
_ClusVolumeClusterName_Object = MibTableColumn
clusVolumeClusterName = _ClusVolumeClusterName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 11),
    _ClusVolumeClusterName_Type()
)
clusVolumeClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeClusterName.setStatus("current")
_ClusVolumeIsSoftThresholdExceeded_Type = TruthValue
_ClusVolumeIsSoftThresholdExceeded_Object = MibTableColumn
clusVolumeIsSoftThresholdExceeded = _ClusVolumeIsSoftThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 13),
    _ClusVolumeIsSoftThresholdExceeded_Type()
)
clusVolumeIsSoftThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsSoftThresholdExceeded.setStatus("current")
_ClusVolumeIsHardThresholdExceeded_Type = TruthValue
_ClusVolumeIsHardThresholdExceeded_Object = MibTableColumn
clusVolumeIsHardThresholdExceeded = _ClusVolumeIsHardThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 14),
    _ClusVolumeIsHardThresholdExceeded_Type()
)
clusVolumeIsHardThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsHardThresholdExceeded.setStatus("current")


class _ClusVolumeReplicationStatus_Type(Integer32):
    """Custom type clusVolumeReplicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("normal", 1))
    )


_ClusVolumeReplicationStatus_Type.__name__ = "Integer32"
_ClusVolumeReplicationStatus_Object = MibTableColumn
clusVolumeReplicationStatus = _ClusVolumeReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 15),
    _ClusVolumeReplicationStatus_Type()
)
clusVolumeReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeReplicationStatus.setStatus("current")
_ClusVolumeIsRemoteIPCopy_Type = TruthValue
_ClusVolumeIsRemoteIPCopy_Object = MibTableColumn
clusVolumeIsRemoteIPCopy = _ClusVolumeIsRemoteIPCopy_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 16),
    _ClusVolumeIsRemoteIPCopy_Type()
)
clusVolumeIsRemoteIPCopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeIsRemoteIPCopy.setStatus("current")
_ClusVolumeRemoteIPCopyFailureMessage_Type = OctetString
_ClusVolumeRemoteIPCopyFailureMessage_Object = MibTableColumn
clusVolumeRemoteIPCopyFailureMessage = _ClusVolumeRemoteIPCopyFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 17),
    _ClusVolumeRemoteIPCopyFailureMessage_Type()
)
clusVolumeRemoteIPCopyFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeRemoteIPCopyFailureMessage.setStatus("current")
_ClusVolumeRowStatus_Type = RowStatus
_ClusVolumeRowStatus_Object = MibTableColumn
clusVolumeRowStatus = _ClusVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 14, 1, 18),
    _ClusVolumeRowStatus_Type()
)
clusVolumeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeRowStatus.setStatus("current")
_ClusVolumeACLTable_Object = MibTable
clusVolumeACLTable = _ClusVolumeACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15)
)
if mibBuilder.loadTexts:
    clusVolumeACLTable.setStatus("current")
_ClusVolumeACLEntry_Object = MibTableRow
clusVolumeACLEntry = _ClusVolumeACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15, 1)
)
clusVolumeACLEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeACLIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeACLEntry.setStatus("current")
_ClusVolumeACLIndex_Type = Integer32
_ClusVolumeACLIndex_Object = MibTableColumn
clusVolumeACLIndex = _ClusVolumeACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15, 1, 1),
    _ClusVolumeACLIndex_Type()
)
clusVolumeACLIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeACLIndex.setStatus("current")
_ClusVolumeACLAuthGroup_Type = OctetString
_ClusVolumeACLAuthGroup_Object = MibTableColumn
clusVolumeACLAuthGroup = _ClusVolumeACLAuthGroup_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15, 1, 2),
    _ClusVolumeACLAuthGroup_Type()
)
clusVolumeACLAuthGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeACLAuthGroup.setStatus("current")
_ClusVolumeACLPermissions_Type = ClusPermissionBits
_ClusVolumeACLPermissions_Object = MibTableColumn
clusVolumeACLPermissions = _ClusVolumeACLPermissions_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15, 1, 3),
    _ClusVolumeACLPermissions_Type()
)
clusVolumeACLPermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeACLPermissions.setStatus("current")
_ClusVolumeACLRowStatus_Type = RowStatus
_ClusVolumeACLRowStatus_Object = MibTableColumn
clusVolumeACLRowStatus = _ClusVolumeACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 15, 1, 4),
    _ClusVolumeACLRowStatus_Type()
)
clusVolumeACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeACLRowStatus.setStatus("current")
_ClusClusterVolumeTable_Object = MibTable
clusClusterVolumeTable = _ClusClusterVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 16)
)
if mibBuilder.loadTexts:
    clusClusterVolumeTable.setStatus("current")
_ClusClusterVolumeEntry_Object = MibTableRow
clusClusterVolumeEntry = _ClusClusterVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 16, 1)
)
clusClusterVolumeEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusClusterIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusClusterVolumeIndex"),
)
if mibBuilder.loadTexts:
    clusClusterVolumeEntry.setStatus("current")
_ClusClusterVolumeIndex_Type = Integer32
_ClusClusterVolumeIndex_Object = MibTableColumn
clusClusterVolumeIndex = _ClusClusterVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 16, 1, 1),
    _ClusClusterVolumeIndex_Type()
)
clusClusterVolumeIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterVolumeIndex.setStatus("current")
_ClusClusterVolumeName_Type = OctetString
_ClusClusterVolumeName_Object = MibTableColumn
clusClusterVolumeName = _ClusClusterVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 16, 1, 2),
    _ClusClusterVolumeName_Type()
)
clusClusterVolumeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterVolumeName.setStatus("current")
_ClusClusterVolumeRowStatus_Type = RowStatus
_ClusClusterVolumeRowStatus_Object = MibTableColumn
clusClusterVolumeRowStatus = _ClusClusterVolumeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 16, 1, 3),
    _ClusClusterVolumeRowStatus_Type()
)
clusClusterVolumeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusClusterVolumeRowStatus.setStatus("current")
_ClusVolumeSnapshotTable_Object = MibTable
clusVolumeSnapshotTable = _ClusVolumeSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17)
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotTable.setStatus("current")
_ClusVolumeSnapshotEntry_Object = MibTableRow
clusVolumeSnapshotEntry = _ClusVolumeSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1)
)
clusVolumeSnapshotEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeSnapshotIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotEntry.setStatus("current")
_ClusVolumeSnapshotIndex_Type = Integer32
_ClusVolumeSnapshotIndex_Object = MibTableColumn
clusVolumeSnapshotIndex = _ClusVolumeSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 1),
    _ClusVolumeSnapshotIndex_Type()
)
clusVolumeSnapshotIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIndex.setStatus("current")
_ClusVolumeSnapshotName_Type = OctetString
_ClusVolumeSnapshotName_Object = MibTableColumn
clusVolumeSnapshotName = _ClusVolumeSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 2),
    _ClusVolumeSnapshotName_Type()
)
clusVolumeSnapshotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotName.setStatus("current")
_ClusVolumeSnapshotCreationTime_Type = DateAndTime
_ClusVolumeSnapshotCreationTime_Object = MibTableColumn
clusVolumeSnapshotCreationTime = _ClusVolumeSnapshotCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 3),
    _ClusVolumeSnapshotCreationTime_Type()
)
clusVolumeSnapshotCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCreationTime.setStatus("current")
_ClusVolumeSnapshotDescription_Type = OctetString
_ClusVolumeSnapshotDescription_Object = MibTableColumn
clusVolumeSnapshotDescription = _ClusVolumeSnapshotDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 4),
    _ClusVolumeSnapshotDescription_Type()
)
clusVolumeSnapshotDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotDescription.setStatus("current")
_ClusVolumeSnapshotSize_Type = Counter64
_ClusVolumeSnapshotSize_Object = MibTableColumn
clusVolumeSnapshotSize = _ClusVolumeSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 5),
    _ClusVolumeSnapshotSize_Type()
)
clusVolumeSnapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSize.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSize.setUnits("kbytes")
_ClusVolumeSnapshotSoftThreshold_Type = Counter64
_ClusVolumeSnapshotSoftThreshold_Object = MibTableColumn
clusVolumeSnapshotSoftThreshold = _ClusVolumeSnapshotSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 6),
    _ClusVolumeSnapshotSoftThreshold_Type()
)
clusVolumeSnapshotSoftThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSoftThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotSoftThreshold.setUnits("kbytes")
_ClusVolumeSnapshotHardThreshold_Type = Counter64
_ClusVolumeSnapshotHardThreshold_Object = MibTableColumn
clusVolumeSnapshotHardThreshold = _ClusVolumeSnapshotHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 7),
    _ClusVolumeSnapshotHardThreshold_Type()
)
clusVolumeSnapshotHardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotHardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotHardThreshold.setUnits("kbytes")
_ClusVolumeSnapshotACLCount_Type = Counter32
_ClusVolumeSnapshotACLCount_Object = MibTableColumn
clusVolumeSnapshotACLCount = _ClusVolumeSnapshotACLCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 8),
    _ClusVolumeSnapshotACLCount_Type()
)
clusVolumeSnapshotACLCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLCount.setStatus("current")
_ClusVolumeSnapshotScheduleName_Type = OctetString
_ClusVolumeSnapshotScheduleName_Object = MibTableColumn
clusVolumeSnapshotScheduleName = _ClusVolumeSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 10),
    _ClusVolumeSnapshotScheduleName_Type()
)
clusVolumeSnapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotScheduleName.setStatus("current")
_ClusVolumeSnapshotIsSoftThresholdExceeded_Type = TruthValue
_ClusVolumeSnapshotIsSoftThresholdExceeded_Object = MibTableColumn
clusVolumeSnapshotIsSoftThresholdExceeded = _ClusVolumeSnapshotIsSoftThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 12),
    _ClusVolumeSnapshotIsSoftThresholdExceeded_Type()
)
clusVolumeSnapshotIsSoftThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsSoftThresholdExceeded.setStatus("current")
_ClusVolumeSnapshotIsHardThresholdExceeded_Type = TruthValue
_ClusVolumeSnapshotIsHardThresholdExceeded_Object = MibTableColumn
clusVolumeSnapshotIsHardThresholdExceeded = _ClusVolumeSnapshotIsHardThresholdExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 13),
    _ClusVolumeSnapshotIsHardThresholdExceeded_Type()
)
clusVolumeSnapshotIsHardThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotIsHardThresholdExceeded.setStatus("current")


class _ClusVolumeSnapshotReplicationStatus_Type(Integer32):
    """Custom type clusVolumeSnapshotReplicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faulty", 2),
          ("normal", 1))
    )


_ClusVolumeSnapshotReplicationStatus_Type.__name__ = "Integer32"
_ClusVolumeSnapshotReplicationStatus_Object = MibTableColumn
clusVolumeSnapshotReplicationStatus = _ClusVolumeSnapshotReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 14),
    _ClusVolumeSnapshotReplicationStatus_Type()
)
clusVolumeSnapshotReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotReplicationStatus.setStatus("current")


class _ClusVolumeSnapshotType_Type(Integer32):
    """Custom type clusVolumeSnapshotType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("remote", 2))
    )


_ClusVolumeSnapshotType_Type.__name__ = "Integer32"
_ClusVolumeSnapshotType_Object = MibTableColumn
clusVolumeSnapshotType = _ClusVolumeSnapshotType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 15),
    _ClusVolumeSnapshotType_Type()
)
clusVolumeSnapshotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotType.setStatus("current")


class _ClusVolumeSnapshotCopyProgress_Type(Integer32):
    """Custom type clusVolumeSnapshotCopyProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ClusVolumeSnapshotCopyProgress_Type.__name__ = "Integer32"
_ClusVolumeSnapshotCopyProgress_Object = MibTableColumn
clusVolumeSnapshotCopyProgress = _ClusVolumeSnapshotCopyProgress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 16),
    _ClusVolumeSnapshotCopyProgress_Type()
)
clusVolumeSnapshotCopyProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCopyProgress.setStatus("current")
if mibBuilder.loadTexts:
    clusVolumeSnapshotCopyProgress.setUnits("%")
_ClusVolumeSnapshotRowStatus_Type = RowStatus
_ClusVolumeSnapshotRowStatus_Object = MibTableColumn
clusVolumeSnapshotRowStatus = _ClusVolumeSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 17, 1, 17),
    _ClusVolumeSnapshotRowStatus_Type()
)
clusVolumeSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeSnapshotRowStatus.setStatus("current")
_ClusVolumeSnapshotACLTable_Object = MibTable
clusVolumeSnapshotACLTable = _ClusVolumeSnapshotACLTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18)
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLTable.setStatus("current")
_ClusVolumeSnapshotACLEntry_Object = MibTableRow
clusVolumeSnapshotACLEntry = _ClusVolumeSnapshotACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18, 1)
)
clusVolumeSnapshotACLEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeSnapshotIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusVolumeSnapshotACLIndex"),
)
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLEntry.setStatus("current")
_ClusVolumeSnapshotACLIndex_Type = Integer32
_ClusVolumeSnapshotACLIndex_Object = MibTableColumn
clusVolumeSnapshotACLIndex = _ClusVolumeSnapshotACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18, 1, 1),
    _ClusVolumeSnapshotACLIndex_Type()
)
clusVolumeSnapshotACLIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLIndex.setStatus("current")
_ClusVolumeSnapshotACLAuthGroup_Type = OctetString
_ClusVolumeSnapshotACLAuthGroup_Object = MibTableColumn
clusVolumeSnapshotACLAuthGroup = _ClusVolumeSnapshotACLAuthGroup_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18, 1, 2),
    _ClusVolumeSnapshotACLAuthGroup_Type()
)
clusVolumeSnapshotACLAuthGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLAuthGroup.setStatus("current")
_ClusVolumeSnapshotACLPermission_Type = ClusPermissionBits
_ClusVolumeSnapshotACLPermission_Object = MibScalar
clusVolumeSnapshotACLPermission = _ClusVolumeSnapshotACLPermission_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18, 1, 3),
    _ClusVolumeSnapshotACLPermission_Type()
)
clusVolumeSnapshotACLPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLPermission.setStatus("current")
_ClusVolumeSnapshotACLRowStatus_Type = RowStatus
_ClusVolumeSnapshotACLRowStatus_Object = MibTableColumn
clusVolumeSnapshotACLRowStatus = _ClusVolumeSnapshotACLRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 18, 1, 4),
    _ClusVolumeSnapshotACLRowStatus_Type()
)
clusVolumeSnapshotACLRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusVolumeSnapshotACLRowStatus.setStatus("current")
_ClusAuthGroupCount_Type = Integer32
_ClusAuthGroupCount_Object = MibScalar
clusAuthGroupCount = _ClusAuthGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 19),
    _ClusAuthGroupCount_Type()
)
clusAuthGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusAuthGroupCount.setStatus("current")
_ClusAuthGroupTable_Object = MibTable
clusAuthGroupTable = _ClusAuthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20)
)
if mibBuilder.loadTexts:
    clusAuthGroupTable.setStatus("current")
_ClusAuthGroupEntry_Object = MibTableRow
clusAuthGroupEntry = _ClusAuthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1)
)
clusAuthGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusAuthGroupIndex"),
)
if mibBuilder.loadTexts:
    clusAuthGroupEntry.setStatus("current")
_ClusAuthGroupIndex_Type = Integer32
_ClusAuthGroupIndex_Object = MibTableColumn
clusAuthGroupIndex = _ClusAuthGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 1),
    _ClusAuthGroupIndex_Type()
)
clusAuthGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupIndex.setStatus("current")
_ClusAuthGroupName_Type = OctetString
_ClusAuthGroupName_Object = MibTableColumn
clusAuthGroupName = _ClusAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 2),
    _ClusAuthGroupName_Type()
)
clusAuthGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupName.setStatus("current")
_ClusAuthGroupDescription_Type = OctetString
_ClusAuthGroupDescription_Object = MibTableColumn
clusAuthGroupDescription = _ClusAuthGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 3),
    _ClusAuthGroupDescription_Type()
)
clusAuthGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupDescription.setStatus("current")
_ClusAuthGroupAcceptAll_Type = TruthValue
_ClusAuthGroupAcceptAll_Object = MibTableColumn
clusAuthGroupAcceptAll = _ClusAuthGroupAcceptAll_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 4),
    _ClusAuthGroupAcceptAll_Type()
)
clusAuthGroupAcceptAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusAuthGroupAcceptAll.setStatus("current")
_ClusAuthGroupAcceptNone_Type = TruthValue
_ClusAuthGroupAcceptNone_Object = MibTableColumn
clusAuthGroupAcceptNone = _ClusAuthGroupAcceptNone_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 5),
    _ClusAuthGroupAcceptNone_Type()
)
clusAuthGroupAcceptNone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusAuthGroupAcceptNone.setStatus("current")
_ClusAuthGroupAcceptSubnet_Type = TruthValue
_ClusAuthGroupAcceptSubnet_Object = MibTableColumn
clusAuthGroupAcceptSubnet = _ClusAuthGroupAcceptSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 6),
    _ClusAuthGroupAcceptSubnet_Type()
)
clusAuthGroupAcceptSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusAuthGroupAcceptSubnet.setStatus("current")
_ClusAuthGroupSubnetCount_Type = Counter32
_ClusAuthGroupSubnetCount_Object = MibScalar
clusAuthGroupSubnetCount = _ClusAuthGroupSubnetCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 7),
    _ClusAuthGroupSubnetCount_Type()
)
clusAuthGroupSubnetCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupSubnetCount.setStatus("current")
_ClusAuthGroupRowStatus_Type = RowStatus
_ClusAuthGroupRowStatus_Object = MibTableColumn
clusAuthGroupRowStatus = _ClusAuthGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 20, 1, 8),
    _ClusAuthGroupRowStatus_Type()
)
clusAuthGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupRowStatus.setStatus("current")
_ClusAuthGroupSubnetTable_Object = MibTable
clusAuthGroupSubnetTable = _ClusAuthGroupSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21)
)
if mibBuilder.loadTexts:
    clusAuthGroupSubnetTable.setStatus("current")
_ClusAuthGroupSubnetEntry_Object = MibTableRow
clusAuthGroupSubnetEntry = _ClusAuthGroupSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21, 1)
)
clusAuthGroupSubnetEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusAuthGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusAuthGroupNetmaskIndex"),
)
if mibBuilder.loadTexts:
    clusAuthGroupSubnetEntry.setStatus("current")
_ClusAuthGroupSubnetIndex_Type = Integer32
_ClusAuthGroupSubnetIndex_Object = MibTableColumn
clusAuthGroupSubnetIndex = _ClusAuthGroupSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21, 1, 1),
    _ClusAuthGroupSubnetIndex_Type()
)
clusAuthGroupSubnetIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupSubnetIndex.setStatus("current")
_ClusAuthGroupSubnetAddress_Type = IpAddress
_ClusAuthGroupSubnetAddress_Object = MibTableColumn
clusAuthGroupSubnetAddress = _ClusAuthGroupSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21, 1, 2),
    _ClusAuthGroupSubnetAddress_Type()
)
clusAuthGroupSubnetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusAuthGroupSubnetAddress.setStatus("current")
_ClusAuthGroupSubnetMask_Type = IpAddress
_ClusAuthGroupSubnetMask_Object = MibTableColumn
clusAuthGroupSubnetMask = _ClusAuthGroupSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21, 1, 3),
    _ClusAuthGroupSubnetMask_Type()
)
clusAuthGroupSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusAuthGroupSubnetMask.setStatus("current")
_ClusAuthGroupSubnetRowStatus_Type = RowStatus
_ClusAuthGroupSubnetRowStatus_Object = MibTableColumn
clusAuthGroupSubnetRowStatus = _ClusAuthGroupSubnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 21, 1, 4),
    _ClusAuthGroupSubnetRowStatus_Type()
)
clusAuthGroupSubnetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusAuthGroupSubnetRowStatus.setStatus("current")


class _ClusCommunicationMode_Type(Integer32):
    """Custom type clusCommunicationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 1),
          ("multicastAndUnicast", 3),
          ("unicast", 2))
    )


_ClusCommunicationMode_Type.__name__ = "Integer32"
_ClusCommunicationMode_Object = MibScalar
clusCommunicationMode = _ClusCommunicationMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 22),
    _ClusCommunicationMode_Type()
)
clusCommunicationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusCommunicationMode.setStatus("current")
_ClusUnicastHostCount_Type = Integer32
_ClusUnicastHostCount_Object = MibScalar
clusUnicastHostCount = _ClusUnicastHostCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 23),
    _ClusUnicastHostCount_Type()
)
clusUnicastHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusUnicastHostCount.setStatus("current")
_ClusUnicastHostTable_Object = MibTable
clusUnicastHostTable = _ClusUnicastHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 24)
)
if mibBuilder.loadTexts:
    clusUnicastHostTable.setStatus("current")
_ClusUnicastHostEntry_Object = MibTableRow
clusUnicastHostEntry = _ClusUnicastHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 24, 1)
)
clusUnicastHostEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusUnicastHostIndex"),
)
if mibBuilder.loadTexts:
    clusUnicastHostEntry.setStatus("current")
_ClusUnicastHostIndex_Type = Integer32
_ClusUnicastHostIndex_Object = MibTableColumn
clusUnicastHostIndex = _ClusUnicastHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 24, 1, 1),
    _ClusUnicastHostIndex_Type()
)
clusUnicastHostIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusUnicastHostIndex.setStatus("current")
_ClusUnicastHostName_Type = OctetString
_ClusUnicastHostName_Object = MibTableColumn
clusUnicastHostName = _ClusUnicastHostName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 24, 1, 2),
    _ClusUnicastHostName_Type()
)
clusUnicastHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusUnicastHostName.setStatus("current")
_ClusUnicastHostRowStatus_Type = RowStatus
_ClusUnicastHostRowStatus_Object = MibTableColumn
clusUnicastHostRowStatus = _ClusUnicastHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 24, 1, 3),
    _ClusUnicastHostRowStatus_Type()
)
clusUnicastHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusUnicastHostRowStatus.setStatus("current")
_ClusSnapshotScheduleCount_Type = Integer32
_ClusSnapshotScheduleCount_Object = MibScalar
clusSnapshotScheduleCount = _ClusSnapshotScheduleCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 25),
    _ClusSnapshotScheduleCount_Type()
)
clusSnapshotScheduleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleCount.setStatus("current")
_ClusSnapshotScheduleTable_Object = MibTable
clusSnapshotScheduleTable = _ClusSnapshotScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26)
)
if mibBuilder.loadTexts:
    clusSnapshotScheduleTable.setStatus("current")
_ClusSnapshotScheduleEntry_Object = MibTableRow
clusSnapshotScheduleEntry = _ClusSnapshotScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1)
)
clusSnapshotScheduleEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB", "clusSnapshotScheduleIndex"),
)
if mibBuilder.loadTexts:
    clusSnapshotScheduleEntry.setStatus("current")
_ClusSnapshotScheduleIndex_Type = Integer32
_ClusSnapshotScheduleIndex_Object = MibTableColumn
clusSnapshotScheduleIndex = _ClusSnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 1),
    _ClusSnapshotScheduleIndex_Type()
)
clusSnapshotScheduleIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusSnapshotScheduleIndex.setStatus("current")
_ClusSnapshotScheduleName_Type = OctetString
_ClusSnapshotScheduleName_Object = MibTableColumn
clusSnapshotScheduleName = _ClusSnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 2),
    _ClusSnapshotScheduleName_Type()
)
clusSnapshotScheduleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusSnapshotScheduleName.setStatus("current")
_ClusSnapshotScheduleDescription_Type = OctetString
_ClusSnapshotScheduleDescription_Object = MibTableColumn
clusSnapshotScheduleDescription = _ClusSnapshotScheduleDescription_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 3),
    _ClusSnapshotScheduleDescription_Type()
)
clusSnapshotScheduleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleDescription.setStatus("current")
_ClusSnapshotScheduleSoftThreshold_Type = Counter64
_ClusSnapshotScheduleSoftThreshold_Object = MibTableColumn
clusSnapshotScheduleSoftThreshold = _ClusSnapshotScheduleSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 4),
    _ClusSnapshotScheduleSoftThreshold_Type()
)
clusSnapshotScheduleSoftThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleSoftThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleSoftThreshold.setUnits("kbytes")
_ClusSnapshotScheduleHardThreshold_Type = Counter64
_ClusSnapshotScheduleHardThreshold_Object = MibTableColumn
clusSnapshotScheduleHardThreshold = _ClusSnapshotScheduleHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 5),
    _ClusSnapshotScheduleHardThreshold_Type()
)
clusSnapshotScheduleHardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleHardThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleHardThreshold.setUnits("kbytes")
_ClusSnapshotScheduleFirstCreationTime_Type = DateAndTime
_ClusSnapshotScheduleFirstCreationTime_Object = MibTableColumn
clusSnapshotScheduleFirstCreationTime = _ClusSnapshotScheduleFirstCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 6),
    _ClusSnapshotScheduleFirstCreationTime_Type()
)
clusSnapshotScheduleFirstCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFirstCreationTime.setStatus("current")
_ClusSnapshotScheduleFrequency_Type = Counter32
_ClusSnapshotScheduleFrequency_Object = MibTableColumn
clusSnapshotScheduleFrequency = _ClusSnapshotScheduleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 7),
    _ClusSnapshotScheduleFrequency_Type()
)
clusSnapshotScheduleFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFrequency.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFrequency.setUnits("seconds")
_ClusSnapshotScheduleVolumeName_Type = OctetString
_ClusSnapshotScheduleVolumeName_Object = MibTableColumn
clusSnapshotScheduleVolumeName = _ClusSnapshotScheduleVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 8),
    _ClusSnapshotScheduleVolumeName_Type()
)
clusSnapshotScheduleVolumeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusSnapshotScheduleVolumeName.setStatus("current")


class _ClusSnapshotScheduleRetainType_Type(Integer32):
    """Custom type clusSnapshotScheduleRetainType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byNumber", 2),
          ("byTime", 1))
    )


_ClusSnapshotScheduleRetainType_Type.__name__ = "Integer32"
_ClusSnapshotScheduleRetainType_Object = MibTableColumn
clusSnapshotScheduleRetainType = _ClusSnapshotScheduleRetainType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 9),
    _ClusSnapshotScheduleRetainType_Type()
)
clusSnapshotScheduleRetainType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainType.setStatus("current")
_ClusSnapshotScheduleRetainCount_Type = Counter32
_ClusSnapshotScheduleRetainCount_Object = MibTableColumn
clusSnapshotScheduleRetainCount = _ClusSnapshotScheduleRetainCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 10),
    _ClusSnapshotScheduleRetainCount_Type()
)
clusSnapshotScheduleRetainCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainCount.setStatus("current")
_ClusSnapshotScheduleRetainTime_Type = Counter32
_ClusSnapshotScheduleRetainTime_Object = MibTableColumn
clusSnapshotScheduleRetainTime = _ClusSnapshotScheduleRetainTime_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 11),
    _ClusSnapshotScheduleRetainTime_Type()
)
clusSnapshotScheduleRetainTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainTime.setStatus("current")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRetainTime.setUnits("seconds")


class _ClusSnapshotScheduleType_Type(Integer32):
    """Custom type clusSnapshotScheduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("primary", 2),
          ("remote", 3))
    )


_ClusSnapshotScheduleType_Type.__name__ = "Integer32"
_ClusSnapshotScheduleType_Object = MibTableColumn
clusSnapshotScheduleType = _ClusSnapshotScheduleType_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 13),
    _ClusSnapshotScheduleType_Type()
)
clusSnapshotScheduleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusSnapshotScheduleType.setStatus("current")
_ClusSnapshotScheduleFailureMessage_Type = OctetString
_ClusSnapshotScheduleFailureMessage_Object = MibTableColumn
clusSnapshotScheduleFailureMessage = _ClusSnapshotScheduleFailureMessage_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 14),
    _ClusSnapshotScheduleFailureMessage_Type()
)
clusSnapshotScheduleFailureMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusSnapshotScheduleFailureMessage.setStatus("current")
_ClusSnapshotScheduleRowStatus_Type = RowStatus
_ClusSnapshotScheduleRowStatus_Object = MibTableColumn
clusSnapshotScheduleRowStatus = _ClusSnapshotScheduleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 12, 26, 1, 15),
    _ClusSnapshotScheduleRowStatus_Type()
)
clusSnapshotScheduleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    clusSnapshotScheduleRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB",
    **{"ClusPermissionBits": ClusPermissionBits,
       "lhnNusCommonClusteringModule": lhnNusCommonClusteringModule,
       "clusMgmtGroupName": clusMgmtGroupName,
       "clusMgmtGroupIsEnabled": clusMgmtGroupIsEnabled,
       "clusMgmtGroupQuorum": clusMgmtGroupQuorum,
       "clusMgmtGroupDescription": clusMgmtGroupDescription,
       "clusMgmtGroupActiveManagerCount": clusMgmtGroupActiveManagerCount,
       "clusMgmtGroupManagerCount": clusMgmtGroupManagerCount,
       "clusManagerTable": clusManagerTable,
       "clusManagerEntry": clusManagerEntry,
       "clusManagerIndex": clusManagerIndex,
       "clusManagerName": clusManagerName,
       "clusManagerVersion": clusManagerVersion,
       "clusManagerHostSerialNo": clusManagerHostSerialNo,
       "clusManagerStatus": clusManagerStatus,
       "clusManagerIsVirtual": clusManagerIsVirtual,
       "clusManagerRowStatus": clusManagerRowStatus,
       "clusModuleCount": clusModuleCount,
       "clusModuleTable": clusModuleTable,
       "clusModuleEntry": clusModuleEntry,
       "clusModuleIndex": clusModuleIndex,
       "clusModuleName": clusModuleName,
       "clusModuleVersion": clusModuleVersion,
       "clusModuleSerialNo": clusModuleSerialNo,
       "clusModuleTotalSize": clusModuleTotalSize,
       "clusModuleAvailSize": clusModuleAvailSize,
       "clusModuleIsManager": clusModuleIsManager,
       "clusModuleRaidConfiguration": clusModuleRaidConfiguration,
       "clusModuleRaidStatus": clusModuleRaidStatus,
       "clusModuleStorageStatus": clusModuleStorageStatus,
       "clusModuleStorageIsReady": clusModuleStorageIsReady,
       "clusModuleCreationTime": clusModuleCreationTime,
       "clusModuleDescription": clusModuleDescription,
       "clusModuleClusterName": clusModuleClusterName,
       "clusModuleRowStatus": clusModuleRowStatus,
       "clusClusterCount": clusClusterCount,
       "clusClusterTable": clusClusterTable,
       "clusClusterEntry": clusClusterEntry,
       "clusClusterIndex": clusClusterIndex,
       "clusClusterName": clusClusterName,
       "clusClusterModuleCount": clusClusterModuleCount,
       "clusClusterVolumeCount": clusClusterVolumeCount,
       "clusClusterDescription": clusClusterDescription,
       "clusClusterRowStatus": clusClusterRowStatus,
       "clusClusterModuleTable": clusClusterModuleTable,
       "clusClusterModuleEntry": clusClusterModuleEntry,
       "clusClusterModuleIndex": clusClusterModuleIndex,
       "clusClusterModuleName": clusClusterModuleName,
       "clusClusterModuleSerialNo": clusClusterModuleSerialNo,
       "clusClusterModuleIsHotSpare": clusClusterModuleIsHotSpare,
       "clusClusterModuleRowStatus": clusClusterModuleRowStatus,
       "clusVolumeCount": clusVolumeCount,
       "clusVolumeTable": clusVolumeTable,
       "clusVolumeEntry": clusVolumeEntry,
       "clusVolumeIndex": clusVolumeIndex,
       "clusVolumeName": clusVolumeName,
       "clusVolumeCreationTime": clusVolumeCreationTime,
       "clusVolumeDescription": clusVolumeDescription,
       "clusVolumeSize": clusVolumeSize,
       "clusVolumeSoftThreshold": clusVolumeSoftThreshold,
       "clusVolumeHardThreshold": clusVolumeHardThreshold,
       "clusVolumeReplicaCount": clusVolumeReplicaCount,
       "clusVolumeSnapshotCount": clusVolumeSnapshotCount,
       "clusVolumeACLCount": clusVolumeACLCount,
       "clusVolumeClusterName": clusVolumeClusterName,
       "clusVolumeIsSoftThresholdExceeded": clusVolumeIsSoftThresholdExceeded,
       "clusVolumeIsHardThresholdExceeded": clusVolumeIsHardThresholdExceeded,
       "clusVolumeReplicationStatus": clusVolumeReplicationStatus,
       "clusVolumeIsRemoteIPCopy": clusVolumeIsRemoteIPCopy,
       "clusVolumeRemoteIPCopyFailureMessage": clusVolumeRemoteIPCopyFailureMessage,
       "clusVolumeRowStatus": clusVolumeRowStatus,
       "clusVolumeACLTable": clusVolumeACLTable,
       "clusVolumeACLEntry": clusVolumeACLEntry,
       "clusVolumeACLIndex": clusVolumeACLIndex,
       "clusVolumeACLAuthGroup": clusVolumeACLAuthGroup,
       "clusVolumeACLPermissions": clusVolumeACLPermissions,
       "clusVolumeACLRowStatus": clusVolumeACLRowStatus,
       "clusClusterVolumeTable": clusClusterVolumeTable,
       "clusClusterVolumeEntry": clusClusterVolumeEntry,
       "clusClusterVolumeIndex": clusClusterVolumeIndex,
       "clusClusterVolumeName": clusClusterVolumeName,
       "clusClusterVolumeRowStatus": clusClusterVolumeRowStatus,
       "clusVolumeSnapshotTable": clusVolumeSnapshotTable,
       "clusVolumeSnapshotEntry": clusVolumeSnapshotEntry,
       "clusVolumeSnapshotIndex": clusVolumeSnapshotIndex,
       "clusVolumeSnapshotName": clusVolumeSnapshotName,
       "clusVolumeSnapshotCreationTime": clusVolumeSnapshotCreationTime,
       "clusVolumeSnapshotDescription": clusVolumeSnapshotDescription,
       "clusVolumeSnapshotSize": clusVolumeSnapshotSize,
       "clusVolumeSnapshotSoftThreshold": clusVolumeSnapshotSoftThreshold,
       "clusVolumeSnapshotHardThreshold": clusVolumeSnapshotHardThreshold,
       "clusVolumeSnapshotACLCount": clusVolumeSnapshotACLCount,
       "clusVolumeSnapshotScheduleName": clusVolumeSnapshotScheduleName,
       "clusVolumeSnapshotIsSoftThresholdExceeded": clusVolumeSnapshotIsSoftThresholdExceeded,
       "clusVolumeSnapshotIsHardThresholdExceeded": clusVolumeSnapshotIsHardThresholdExceeded,
       "clusVolumeSnapshotReplicationStatus": clusVolumeSnapshotReplicationStatus,
       "clusVolumeSnapshotType": clusVolumeSnapshotType,
       "clusVolumeSnapshotCopyProgress": clusVolumeSnapshotCopyProgress,
       "clusVolumeSnapshotRowStatus": clusVolumeSnapshotRowStatus,
       "clusVolumeSnapshotACLTable": clusVolumeSnapshotACLTable,
       "clusVolumeSnapshotACLEntry": clusVolumeSnapshotACLEntry,
       "clusVolumeSnapshotACLIndex": clusVolumeSnapshotACLIndex,
       "clusVolumeSnapshotACLAuthGroup": clusVolumeSnapshotACLAuthGroup,
       "clusVolumeSnapshotACLPermission": clusVolumeSnapshotACLPermission,
       "clusVolumeSnapshotACLRowStatus": clusVolumeSnapshotACLRowStatus,
       "clusAuthGroupCount": clusAuthGroupCount,
       "clusAuthGroupTable": clusAuthGroupTable,
       "clusAuthGroupEntry": clusAuthGroupEntry,
       "clusAuthGroupIndex": clusAuthGroupIndex,
       "clusAuthGroupName": clusAuthGroupName,
       "clusAuthGroupDescription": clusAuthGroupDescription,
       "clusAuthGroupAcceptAll": clusAuthGroupAcceptAll,
       "clusAuthGroupAcceptNone": clusAuthGroupAcceptNone,
       "clusAuthGroupAcceptSubnet": clusAuthGroupAcceptSubnet,
       "clusAuthGroupSubnetCount": clusAuthGroupSubnetCount,
       "clusAuthGroupRowStatus": clusAuthGroupRowStatus,
       "clusAuthGroupSubnetTable": clusAuthGroupSubnetTable,
       "clusAuthGroupSubnetEntry": clusAuthGroupSubnetEntry,
       "clusAuthGroupSubnetIndex": clusAuthGroupSubnetIndex,
       "clusAuthGroupSubnetAddress": clusAuthGroupSubnetAddress,
       "clusAuthGroupSubnetMask": clusAuthGroupSubnetMask,
       "clusAuthGroupSubnetRowStatus": clusAuthGroupSubnetRowStatus,
       "clusCommunicationMode": clusCommunicationMode,
       "clusUnicastHostCount": clusUnicastHostCount,
       "clusUnicastHostTable": clusUnicastHostTable,
       "clusUnicastHostEntry": clusUnicastHostEntry,
       "clusUnicastHostIndex": clusUnicastHostIndex,
       "clusUnicastHostName": clusUnicastHostName,
       "clusUnicastHostRowStatus": clusUnicastHostRowStatus,
       "clusSnapshotScheduleCount": clusSnapshotScheduleCount,
       "clusSnapshotScheduleTable": clusSnapshotScheduleTable,
       "clusSnapshotScheduleEntry": clusSnapshotScheduleEntry,
       "clusSnapshotScheduleIndex": clusSnapshotScheduleIndex,
       "clusSnapshotScheduleName": clusSnapshotScheduleName,
       "clusSnapshotScheduleDescription": clusSnapshotScheduleDescription,
       "clusSnapshotScheduleSoftThreshold": clusSnapshotScheduleSoftThreshold,
       "clusSnapshotScheduleHardThreshold": clusSnapshotScheduleHardThreshold,
       "clusSnapshotScheduleFirstCreationTime": clusSnapshotScheduleFirstCreationTime,
       "clusSnapshotScheduleFrequency": clusSnapshotScheduleFrequency,
       "clusSnapshotScheduleVolumeName": clusSnapshotScheduleVolumeName,
       "clusSnapshotScheduleRetainType": clusSnapshotScheduleRetainType,
       "clusSnapshotScheduleRetainCount": clusSnapshotScheduleRetainCount,
       "clusSnapshotScheduleRetainTime": clusSnapshotScheduleRetainTime,
       "clusSnapshotScheduleType": clusSnapshotScheduleType,
       "clusSnapshotScheduleFailureMessage": clusSnapshotScheduleFailureMessage,
       "clusSnapshotScheduleRowStatus": clusSnapshotScheduleRowStatus}
)
