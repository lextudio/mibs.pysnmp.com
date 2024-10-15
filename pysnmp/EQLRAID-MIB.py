# SNMP MIB module (EQLRAID-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLRAID-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:10 2024
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

(eqlGroupId,) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "eqlGroupId")

(eqlDriveGroupIndex,
 eqlMemberIndex) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlDriveGroupIndex",
    "eqlMemberIndex")

(eqlStoragePoolIndex,) = mibBuilder.importSymbols(
    "EQLSTORAGEPOOL-MIB",
    "eqlStoragePoolIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eqlRAIDModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 10)
)
eqlRAIDModule.setRevisions(
        ("2002-11-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlRAIDObjects_ObjectIdentity = ObjectIdentity
eqlRAIDObjects = _EqlRAIDObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1)
)
_EqlRAIDDeviceTable_Object = MibTable
eqlRAIDDeviceTable = _EqlRAIDDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1)
)
if mibBuilder.loadTexts:
    eqlRAIDDeviceTable.setStatus("current")
_EqlRAIDDeviceEntry_Object = MibTableRow
eqlRAIDDeviceEntry = _EqlRAIDDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1)
)
eqlRAIDDeviceEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"),
)
if mibBuilder.loadTexts:
    eqlRAIDDeviceEntry.setStatus("current")
_EqlRAIDDeviceLUNIndex_Type = Integer32
_EqlRAIDDeviceLUNIndex_Object = MibTableColumn
eqlRAIDDeviceLUNIndex = _EqlRAIDDeviceLUNIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 1),
    _EqlRAIDDeviceLUNIndex_Type()
)
eqlRAIDDeviceLUNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLUNIndex.setStatus("current")
_EqlRAIDDeviceLUN_Type = Integer32
_EqlRAIDDeviceLUN_Object = MibTableColumn
eqlRAIDDeviceLUN = _EqlRAIDDeviceLUN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 2),
    _EqlRAIDDeviceLUN_Type()
)
eqlRAIDDeviceLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLUN.setStatus("current")


class _EqlRAIDDeviceOperStatus_Type(Integer32):
    """Custom type eqlRAIDDeviceOperStatus based on Integer32"""
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
        *(("dataLoss", 2),
          ("degraded", 4),
          ("failed", 5),
          ("noDevice", 1),
          ("nominal", 3))
    )


_EqlRAIDDeviceOperStatus_Type.__name__ = "Integer32"
_EqlRAIDDeviceOperStatus_Object = MibTableColumn
eqlRAIDDeviceOperStatus = _EqlRAIDDeviceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 3),
    _EqlRAIDDeviceOperStatus_Type()
)
eqlRAIDDeviceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceOperStatus.setStatus("current")


class _EqlRAIDDeviceUUID_Type(OctetString):
    """Custom type eqlRAIDDeviceUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlRAIDDeviceUUID_Type.__name__ = "OctetString"
_EqlRAIDDeviceUUID_Object = MibTableColumn
eqlRAIDDeviceUUID = _EqlRAIDDeviceUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 4),
    _EqlRAIDDeviceUUID_Type()
)
eqlRAIDDeviceUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceUUID.setStatus("current")
_EqlRAIDDeviceDriveCount_Type = Integer32
_EqlRAIDDeviceDriveCount_Object = MibTableColumn
eqlRAIDDeviceDriveCount = _EqlRAIDDeviceDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 5),
    _EqlRAIDDeviceDriveCount_Type()
)
eqlRAIDDeviceDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceDriveCount.setStatus("current")


class _EqlRAIDDeviceLayoutOperStatus_Type(Integer32):
    """Custom type eqlRAIDDeviceLayoutOperStatus based on Integer32"""
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
        *(("expInProgress", 3),
          ("expSuspended", 2),
          ("noOp", 1),
          ("swapInProgress", 5),
          ("swapSuspended", 4))
    )


_EqlRAIDDeviceLayoutOperStatus_Type.__name__ = "Integer32"
_EqlRAIDDeviceLayoutOperStatus_Object = MibTableColumn
eqlRAIDDeviceLayoutOperStatus = _EqlRAIDDeviceLayoutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 6),
    _EqlRAIDDeviceLayoutOperStatus_Type()
)
eqlRAIDDeviceLayoutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLayoutOperStatus.setStatus("current")
_EqlRAIDDeviceLayoutSectPerSU_Type = Integer32
_EqlRAIDDeviceLayoutSectPerSU_Object = MibTableColumn
eqlRAIDDeviceLayoutSectPerSU = _EqlRAIDDeviceLayoutSectPerSU_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 7),
    _EqlRAIDDeviceLayoutSectPerSU_Type()
)
eqlRAIDDeviceLayoutSectPerSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLayoutSectPerSU.setStatus("current")
_EqlRAIDDeviceLUNCapacity_Type = Counter64
_EqlRAIDDeviceLUNCapacity_Object = MibTableColumn
eqlRAIDDeviceLUNCapacity = _EqlRAIDDeviceLUNCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 8),
    _EqlRAIDDeviceLUNCapacity_Type()
)
eqlRAIDDeviceLUNCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLUNCapacity.setStatus("current")
_EqlRAIDDeviceLostBlocks_Type = Integer32
_EqlRAIDDeviceLostBlocks_Object = MibTableColumn
eqlRAIDDeviceLostBlocks = _EqlRAIDDeviceLostBlocks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 9),
    _EqlRAIDDeviceLostBlocks_Type()
)
eqlRAIDDeviceLostBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceLostBlocks.setStatus("current")
_EqlRAIDDeviceOutIOOps_Type = Integer32
_EqlRAIDDeviceOutIOOps_Object = MibTableColumn
eqlRAIDDeviceOutIOOps = _EqlRAIDDeviceOutIOOps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 10),
    _EqlRAIDDeviceOutIOOps_Type()
)
eqlRAIDDeviceOutIOOps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceOutIOOps.setStatus("current")
_EqlRAIDDeviceCacheWrites_Type = Integer32
_EqlRAIDDeviceCacheWrites_Object = MibTableColumn
eqlRAIDDeviceCacheWrites = _EqlRAIDDeviceCacheWrites_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 11),
    _EqlRAIDDeviceCacheWrites_Type()
)
eqlRAIDDeviceCacheWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceCacheWrites.setStatus("current")
_EqlRAIDDeviceCacheReads_Type = Integer32
_EqlRAIDDeviceCacheReads_Object = MibTableColumn
eqlRAIDDeviceCacheReads = _EqlRAIDDeviceCacheReads_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 12),
    _EqlRAIDDeviceCacheReads_Type()
)
eqlRAIDDeviceCacheReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceCacheReads.setStatus("current")
_EqlRAIDDeviceCompCacheWrites_Type = Counter64
_EqlRAIDDeviceCompCacheWrites_Object = MibTableColumn
eqlRAIDDeviceCompCacheWrites = _EqlRAIDDeviceCompCacheWrites_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 13),
    _EqlRAIDDeviceCompCacheWrites_Type()
)
eqlRAIDDeviceCompCacheWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceCompCacheWrites.setStatus("current")
_EqlRAIDDeviceCompCacheReads_Type = Counter64
_EqlRAIDDeviceCompCacheReads_Object = MibTableColumn
eqlRAIDDeviceCompCacheReads = _EqlRAIDDeviceCompCacheReads_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 14),
    _EqlRAIDDeviceCompCacheReads_Type()
)
eqlRAIDDeviceCompCacheReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceCompCacheReads.setStatus("current")
_EqlRAIDDeviceSectWritten_Type = Counter64
_EqlRAIDDeviceSectWritten_Object = MibTableColumn
eqlRAIDDeviceSectWritten = _EqlRAIDDeviceSectWritten_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 15),
    _EqlRAIDDeviceSectWritten_Type()
)
eqlRAIDDeviceSectWritten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceSectWritten.setStatus("current")
_EqlRAIDDeviceSectRead_Type = Counter64
_EqlRAIDDeviceSectRead_Object = MibTableColumn
eqlRAIDDeviceSectRead = _EqlRAIDDeviceSectRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 16),
    _EqlRAIDDeviceSectRead_Type()
)
eqlRAIDDeviceSectRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceSectRead.setStatus("current")
_EqlRAIDDeviceStoragePoolIndex_Type = Unsigned32
_EqlRAIDDeviceStoragePoolIndex_Object = MibTableColumn
eqlRAIDDeviceStoragePoolIndex = _EqlRAIDDeviceStoragePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 17),
    _EqlRAIDDeviceStoragePoolIndex_Type()
)
eqlRAIDDeviceStoragePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlRAIDDeviceStoragePoolIndex.setStatus("current")
_EqlRAIDDeviceDriveGroupIndex_Type = Unsigned32
_EqlRAIDDeviceDriveGroupIndex_Object = MibTableColumn
eqlRAIDDeviceDriveGroupIndex = _EqlRAIDDeviceDriveGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 18),
    _EqlRAIDDeviceDriveGroupIndex_Type()
)
eqlRAIDDeviceDriveGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlRAIDDeviceDriveGroupIndex.setStatus("current")
_EqlRAIDLayoutTable_Object = MibTable
eqlRAIDLayoutTable = _EqlRAIDLayoutTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2)
)
if mibBuilder.loadTexts:
    eqlRAIDLayoutTable.setStatus("current")
_EqlRAIDLayoutEntry_Object = MibTableRow
eqlRAIDLayoutEntry = _EqlRAIDLayoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1)
)
eqlRAIDLayoutEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"),
)
if mibBuilder.loadTexts:
    eqlRAIDLayoutEntry.setStatus("current")


class _EqlRAIDLayoutIndex_Type(Integer32):
    """Custom type eqlRAIDLayoutIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2))
    )


_EqlRAIDLayoutIndex_Type.__name__ = "Integer32"
_EqlRAIDLayoutIndex_Object = MibTableColumn
eqlRAIDLayoutIndex = _EqlRAIDLayoutIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 1),
    _EqlRAIDLayoutIndex_Type()
)
eqlRAIDLayoutIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutIndex.setStatus("current")


class _EqlRAIDLayoutOperStatus_Type(Integer32):
    """Custom type eqlRAIDLayoutOperStatus based on Integer32"""
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
        *(("degraded", 5),
          ("failed", 3),
          ("noDevice", 1),
          ("noLayout", 2),
          ("nominal", 4))
    )


_EqlRAIDLayoutOperStatus_Type.__name__ = "Integer32"
_EqlRAIDLayoutOperStatus_Object = MibTableColumn
eqlRAIDLayoutOperStatus = _EqlRAIDLayoutOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 2),
    _EqlRAIDLayoutOperStatus_Type()
)
eqlRAIDLayoutOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutOperStatus.setStatus("current")
_EqlRAIDLayoutNumParityGrp_Type = Integer32
_EqlRAIDLayoutNumParityGrp_Object = MibTableColumn
eqlRAIDLayoutNumParityGrp = _EqlRAIDLayoutNumParityGrp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 3),
    _EqlRAIDLayoutNumParityGrp_Type()
)
eqlRAIDLayoutNumParityGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutNumParityGrp.setStatus("current")


class _EqlRAIDLayoutParityType_Type(Integer32):
    """Custom type eqlRAIDLayoutParityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5,
              10,
              50)
        )
    )
    namedValues = NamedValues(
        *(("raid1", 1),
          ("raid10", 10),
          ("raid5", 5),
          ("raid50", 50),
          ("stripe", 0))
    )


_EqlRAIDLayoutParityType_Type.__name__ = "Integer32"
_EqlRAIDLayoutParityType_Object = MibTableColumn
eqlRAIDLayoutParityType = _EqlRAIDLayoutParityType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 4),
    _EqlRAIDLayoutParityType_Type()
)
eqlRAIDLayoutParityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutParityType.setStatus("current")
_EqlRAIDLayoutBeginLBA_Type = Counter64
_EqlRAIDLayoutBeginLBA_Object = MibTableColumn
eqlRAIDLayoutBeginLBA = _EqlRAIDLayoutBeginLBA_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 5),
    _EqlRAIDLayoutBeginLBA_Type()
)
eqlRAIDLayoutBeginLBA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutBeginLBA.setStatus("current")
_EqlRAIDLayoutLength_Type = Counter64
_EqlRAIDLayoutLength_Object = MibTableColumn
eqlRAIDLayoutLength = _EqlRAIDLayoutLength_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 6),
    _EqlRAIDLayoutLength_Type()
)
eqlRAIDLayoutLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDLayoutLength.setStatus("current")
_EqlRAIDParityGroupTable_Object = MibTable
eqlRAIDParityGroupTable = _EqlRAIDParityGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3)
)
if mibBuilder.loadTexts:
    eqlRAIDParityGroupTable.setStatus("current")
_EqlRAIDParityGroupEntry_Object = MibTableRow
eqlRAIDParityGroupEntry = _EqlRAIDParityGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1)
)
eqlRAIDParityGroupEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"),
    (0, "EQLRAID-MIB", "eqlParityGrpIndex"),
)
if mibBuilder.loadTexts:
    eqlRAIDParityGroupEntry.setStatus("current")
_EqlParityGrpIndex_Type = Integer32
_EqlParityGrpIndex_Object = MibTableColumn
eqlParityGrpIndex = _EqlParityGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 1),
    _EqlParityGrpIndex_Type()
)
eqlParityGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpIndex.setStatus("current")


class _EqlParityGrpOperStatus_Type(Integer32):
    """Custom type eqlParityGrpOperStatus based on Integer32"""
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
        *(("degraded", 4),
          ("failed", 5),
          ("noDevice", 1),
          ("noGroup", 3),
          ("noLayout", 2),
          ("nominal", 6))
    )


_EqlParityGrpOperStatus_Type.__name__ = "Integer32"
_EqlParityGrpOperStatus_Object = MibTableColumn
eqlParityGrpOperStatus = _EqlParityGrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 2),
    _EqlParityGrpOperStatus_Type()
)
eqlParityGrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpOperStatus.setStatus("current")
_EqlParityGrpDriveCount_Type = Integer32
_EqlParityGrpDriveCount_Object = MibTableColumn
eqlParityGrpDriveCount = _EqlParityGrpDriveCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 3),
    _EqlParityGrpDriveCount_Type()
)
eqlParityGrpDriveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpDriveCount.setStatus("current")


class _EqlParityGrpOperation_Type(Integer32):
    """Custom type eqlParityGrpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 3),
          ("reconstruct", 2),
          ("verify", 1))
    )


_EqlParityGrpOperation_Type.__name__ = "Integer32"
_EqlParityGrpOperation_Object = MibTableColumn
eqlParityGrpOperation = _EqlParityGrpOperation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 4),
    _EqlParityGrpOperation_Type()
)
eqlParityGrpOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpOperation.setStatus("current")
_EqlParityGrpReconstChkpt_Type = Counter64
_EqlParityGrpReconstChkpt_Object = MibTableColumn
eqlParityGrpReconstChkpt = _EqlParityGrpReconstChkpt_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 5),
    _EqlParityGrpReconstChkpt_Type()
)
eqlParityGrpReconstChkpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpReconstChkpt.setStatus("current")
_EqlParityGrpVerifyChkpt_Type = Counter64
_EqlParityGrpVerifyChkpt_Object = MibTableColumn
eqlParityGrpVerifyChkpt = _EqlParityGrpVerifyChkpt_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 6),
    _EqlParityGrpVerifyChkpt_Type()
)
eqlParityGrpVerifyChkpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlParityGrpVerifyChkpt.setStatus("current")
_EqlRAIDDriveTable_Object = MibTable
eqlRAIDDriveTable = _EqlRAIDDriveTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4)
)
if mibBuilder.loadTexts:
    eqlRAIDDriveTable.setStatus("current")
_EqlRAIDDriveEntry_Object = MibTableRow
eqlRAIDDriveEntry = _EqlRAIDDriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1)
)
eqlRAIDDriveEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDDriveDriveLUNIndex"),
)
if mibBuilder.loadTexts:
    eqlRAIDDriveEntry.setStatus("current")
_EqlRAIDDriveDriveLUNIndex_Type = Integer32
_EqlRAIDDriveDriveLUNIndex_Object = MibTableColumn
eqlRAIDDriveDriveLUNIndex = _EqlRAIDDriveDriveLUNIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 1),
    _EqlRAIDDriveDriveLUNIndex_Type()
)
eqlRAIDDriveDriveLUNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDriveDriveLUNIndex.setStatus("current")
_EqlRAIDDriveDriveLUN_Type = Integer32
_EqlRAIDDriveDriveLUN_Object = MibTableColumn
eqlRAIDDriveDriveLUN = _EqlRAIDDriveDriveLUN_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 2),
    _EqlRAIDDriveDriveLUN_Type()
)
eqlRAIDDriveDriveLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDriveDriveLUN.setStatus("current")


class _EqlRAIDDriveOperStatus_Type(Integer32):
    """Custom type eqlRAIDDriveOperStatus based on Integer32"""
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
        *(("active", 2),
          ("failed", 3),
          ("noDrive", 1),
          ("reconstruct", 5),
          ("spare", 7),
          ("swap", 6),
          ("tooSmall", 4))
    )


_EqlRAIDDriveOperStatus_Type.__name__ = "Integer32"
_EqlRAIDDriveOperStatus_Object = MibTableColumn
eqlRAIDDriveOperStatus = _EqlRAIDDriveOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 3),
    _EqlRAIDDriveOperStatus_Type()
)
eqlRAIDDriveOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDriveOperStatus.setStatus("current")


class _EqlRAIDDriveUUID_Type(OctetString):
    """Custom type eqlRAIDDriveUUID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EqlRAIDDriveUUID_Type.__name__ = "OctetString"
_EqlRAIDDriveUUID_Object = MibTableColumn
eqlRAIDDriveUUID = _EqlRAIDDriveUUID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 4),
    _EqlRAIDDriveUUID_Type()
)
eqlRAIDDriveUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDriveUUID.setStatus("current")


class _EqlRAIDDiskIndex_Type(Integer32):
    """Custom type eqlRAIDDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_EqlRAIDDiskIndex_Type.__name__ = "Integer32"
_EqlRAIDDiskIndex_Object = MibTableColumn
eqlRAIDDiskIndex = _EqlRAIDDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 5),
    _EqlRAIDDiskIndex_Type()
)
eqlRAIDDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDiskIndex.setStatus("current")
_EqlRAIDDeviceIndex_Type = Integer32
_EqlRAIDDeviceIndex_Object = MibTableColumn
eqlRAIDDeviceIndex = _EqlRAIDDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 6),
    _EqlRAIDDeviceIndex_Type()
)
eqlRAIDDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlRAIDDeviceIndex.setStatus("current")
_EqlStoragePoolRAIDLUNTable_Object = MibTable
eqlStoragePoolRAIDLUNTable = _EqlStoragePoolRAIDLUNTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 5)
)
if mibBuilder.loadTexts:
    eqlStoragePoolRAIDLUNTable.setStatus("current")
_EqlStoragePoolRAIDLUNEntry_Object = MibTableRow
eqlStoragePoolRAIDLUNEntry = _EqlStoragePoolRAIDLUNEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1)
)
eqlStoragePoolRAIDLUNEntry.setIndexNames(
    (0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLMEMBER-MIB", "eqlDriveGroupIndex"),
    (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"),
)
if mibBuilder.loadTexts:
    eqlStoragePoolRAIDLUNEntry.setStatus("current")
_EqlStoragePoolRAIDLUNfoo_Type = Integer32
_EqlStoragePoolRAIDLUNfoo_Object = MibTableColumn
eqlStoragePoolRAIDLUNfoo = _EqlStoragePoolRAIDLUNfoo_Object(
    (1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1, 1),
    _EqlStoragePoolRAIDLUNfoo_Type()
)
eqlStoragePoolRAIDLUNfoo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlStoragePoolRAIDLUNfoo.setStatus("current")
_EqlRAIDNotifications_ObjectIdentity = ObjectIdentity
eqlRAIDNotifications = _EqlRAIDNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 10, 2)
)
_EqlRAIDConformance_ObjectIdentity = ObjectIdentity
eqlRAIDConformance = _EqlRAIDConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 10, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLRAID-MIB",
    **{"eqlRAIDModule": eqlRAIDModule,
       "eqlRAIDObjects": eqlRAIDObjects,
       "eqlRAIDDeviceTable": eqlRAIDDeviceTable,
       "eqlRAIDDeviceEntry": eqlRAIDDeviceEntry,
       "eqlRAIDDeviceLUNIndex": eqlRAIDDeviceLUNIndex,
       "eqlRAIDDeviceLUN": eqlRAIDDeviceLUN,
       "eqlRAIDDeviceOperStatus": eqlRAIDDeviceOperStatus,
       "eqlRAIDDeviceUUID": eqlRAIDDeviceUUID,
       "eqlRAIDDeviceDriveCount": eqlRAIDDeviceDriveCount,
       "eqlRAIDDeviceLayoutOperStatus": eqlRAIDDeviceLayoutOperStatus,
       "eqlRAIDDeviceLayoutSectPerSU": eqlRAIDDeviceLayoutSectPerSU,
       "eqlRAIDDeviceLUNCapacity": eqlRAIDDeviceLUNCapacity,
       "eqlRAIDDeviceLostBlocks": eqlRAIDDeviceLostBlocks,
       "eqlRAIDDeviceOutIOOps": eqlRAIDDeviceOutIOOps,
       "eqlRAIDDeviceCacheWrites": eqlRAIDDeviceCacheWrites,
       "eqlRAIDDeviceCacheReads": eqlRAIDDeviceCacheReads,
       "eqlRAIDDeviceCompCacheWrites": eqlRAIDDeviceCompCacheWrites,
       "eqlRAIDDeviceCompCacheReads": eqlRAIDDeviceCompCacheReads,
       "eqlRAIDDeviceSectWritten": eqlRAIDDeviceSectWritten,
       "eqlRAIDDeviceSectRead": eqlRAIDDeviceSectRead,
       "eqlRAIDDeviceStoragePoolIndex": eqlRAIDDeviceStoragePoolIndex,
       "eqlRAIDDeviceDriveGroupIndex": eqlRAIDDeviceDriveGroupIndex,
       "eqlRAIDLayoutTable": eqlRAIDLayoutTable,
       "eqlRAIDLayoutEntry": eqlRAIDLayoutEntry,
       "eqlRAIDLayoutIndex": eqlRAIDLayoutIndex,
       "eqlRAIDLayoutOperStatus": eqlRAIDLayoutOperStatus,
       "eqlRAIDLayoutNumParityGrp": eqlRAIDLayoutNumParityGrp,
       "eqlRAIDLayoutParityType": eqlRAIDLayoutParityType,
       "eqlRAIDLayoutBeginLBA": eqlRAIDLayoutBeginLBA,
       "eqlRAIDLayoutLength": eqlRAIDLayoutLength,
       "eqlRAIDParityGroupTable": eqlRAIDParityGroupTable,
       "eqlRAIDParityGroupEntry": eqlRAIDParityGroupEntry,
       "eqlParityGrpIndex": eqlParityGrpIndex,
       "eqlParityGrpOperStatus": eqlParityGrpOperStatus,
       "eqlParityGrpDriveCount": eqlParityGrpDriveCount,
       "eqlParityGrpOperation": eqlParityGrpOperation,
       "eqlParityGrpReconstChkpt": eqlParityGrpReconstChkpt,
       "eqlParityGrpVerifyChkpt": eqlParityGrpVerifyChkpt,
       "eqlRAIDDriveTable": eqlRAIDDriveTable,
       "eqlRAIDDriveEntry": eqlRAIDDriveEntry,
       "eqlRAIDDriveDriveLUNIndex": eqlRAIDDriveDriveLUNIndex,
       "eqlRAIDDriveDriveLUN": eqlRAIDDriveDriveLUN,
       "eqlRAIDDriveOperStatus": eqlRAIDDriveOperStatus,
       "eqlRAIDDriveUUID": eqlRAIDDriveUUID,
       "eqlRAIDDiskIndex": eqlRAIDDiskIndex,
       "eqlRAIDDeviceIndex": eqlRAIDDeviceIndex,
       "eqlStoragePoolRAIDLUNTable": eqlStoragePoolRAIDLUNTable,
       "eqlStoragePoolRAIDLUNEntry": eqlStoragePoolRAIDLUNEntry,
       "eqlStoragePoolRAIDLUNfoo": eqlStoragePoolRAIDLUNfoo,
       "eqlRAIDNotifications": eqlRAIDNotifications,
       "eqlRAIDConformance": eqlRAIDConformance}
)
