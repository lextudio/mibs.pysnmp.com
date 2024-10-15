# SNMP MIB module (HP-MPE-XL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-MPE-XL
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:36 2024
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

(Timeticks,) = mibBuilder.importSymbols(
    "RFC1155-SMI",
    "Timeticks")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_General_ObjectIdentity = ObjectIdentity
general = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1)
)
_MpeXLSystem_ObjectIdentity = ObjectIdentity
mpeXLSystem = _MpeXLSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3)
)
_Volume_ObjectIdentity = ObjectIdentity
volume = _Volume_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1)
)
_VolumeMounted_Type = Integer32
_VolumeMounted_Object = MibScalar
volumeMounted = _VolumeMounted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 1),
    _VolumeMounted_Type()
)
volumeMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeMounted.setStatus("mandatory")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("mandatory")
_VolumeEntry_Object = MibTableRow
volumeEntry = _VolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1)
)
volumeEntry.setIndexNames(
    (0, "HP-MPE-XL", "volumeName"),
)
if mibBuilder.loadTexts:
    volumeEntry.setStatus("mandatory")
_VolumeLDEV_Type = Integer32
_VolumeLDEV_Object = MibTableColumn
volumeLDEV = _VolumeLDEV_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 1),
    _VolumeLDEV_Type()
)
volumeLDEV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLDEV.setStatus("mandatory")
_VolumeName_Type = DisplayString
_VolumeName_Object = MibTableColumn
volumeName = _VolumeName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 2),
    _VolumeName_Type()
)
volumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeName.setStatus("mandatory")
_VolumeDriveType_Type = DisplayString
_VolumeDriveType_Object = MibTableColumn
volumeDriveType = _VolumeDriveType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 3),
    _VolumeDriveType_Type()
)
volumeDriveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDriveType.setStatus("mandatory")
_VolumeSectorSize_Type = Integer32
_VolumeSectorSize_Object = MibTableColumn
volumeSectorSize = _VolumeSectorSize_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 4),
    _VolumeSectorSize_Type()
)
volumeSectorSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSectorSize.setStatus("mandatory")


class _VolumeType_Type(Integer32):
    """Custom type volumeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonSystem", 2),
          ("system", 1))
    )


_VolumeType_Type.__name__ = "Integer32"
_VolumeType_Object = MibTableColumn
volumeType = _VolumeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 5),
    _VolumeType_Type()
)
volumeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeType.setStatus("mandatory")
_VolumeCapacity_Type = Integer32
_VolumeCapacity_Object = MibTableColumn
volumeCapacity = _VolumeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 6),
    _VolumeCapacity_Type()
)
volumeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeCapacity.setStatus("mandatory")
_VolumeMPEOverhead_Type = Integer32
_VolumeMPEOverhead_Object = MibTableColumn
volumeMPEOverhead = _VolumeMPEOverhead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 7),
    _VolumeMPEOverhead_Type()
)
volumeMPEOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeMPEOverhead.setStatus("mandatory")
_VolumeMPETransOverhead_Type = Integer32
_VolumeMPETransOverhead_Object = MibTableColumn
volumeMPETransOverhead = _VolumeMPETransOverhead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 8),
    _VolumeMPETransOverhead_Type()
)
volumeMPETransOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeMPETransOverhead.setStatus("mandatory")
_VolumeMPEConfigMaxTrans_Type = Integer32
_VolumeMPEConfigMaxTrans_Object = MibTableColumn
volumeMPEConfigMaxTrans = _VolumeMPEConfigMaxTrans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 9),
    _VolumeMPEConfigMaxTrans_Type()
)
volumeMPEConfigMaxTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeMPEConfigMaxTrans.setStatus("mandatory")
_VolumeDirSpaceOverhead_Type = Integer32
_VolumeDirSpaceOverhead_Object = MibTableColumn
volumeDirSpaceOverhead = _VolumeDirSpaceOverhead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 10),
    _VolumeDirSpaceOverhead_Type()
)
volumeDirSpaceOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeDirSpaceOverhead.setStatus("mandatory")
_VolumeFileLabelOverhead_Type = Integer32
_VolumeFileLabelOverhead_Object = MibTableColumn
volumeFileLabelOverhead = _VolumeFileLabelOverhead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 11),
    _VolumeFileLabelOverhead_Type()
)
volumeFileLabelOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeFileLabelOverhead.setStatus("mandatory")
_VolumeTransactionMgmtOverhead_Type = Integer32
_VolumeTransactionMgmtOverhead_Object = MibTableColumn
volumeTransactionMgmtOverhead = _VolumeTransactionMgmtOverhead_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 12),
    _VolumeTransactionMgmtOverhead_Type()
)
volumeTransactionMgmtOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTransactionMgmtOverhead.setStatus("mandatory")
_VolumeSpoolFileDiscUsage_Type = Integer32
_VolumeSpoolFileDiscUsage_Object = MibTableColumn
volumeSpoolFileDiscUsage = _VolumeSpoolFileDiscUsage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 13),
    _VolumeSpoolFileDiscUsage_Type()
)
volumeSpoolFileDiscUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeSpoolFileDiscUsage.setStatus("mandatory")
_VolumePermFiles_Type = Integer32
_VolumePermFiles_Object = MibTableColumn
volumePermFiles = _VolumePermFiles_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 14),
    _VolumePermFiles_Type()
)
volumePermFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumePermFiles.setStatus("mandatory")
_VolumeTempFiles_Type = Integer32
_VolumeTempFiles_Object = MibTableColumn
volumeTempFiles = _VolumeTempFiles_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 15),
    _VolumeTempFiles_Type()
)
volumeTempFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTempFiles.setStatus("mandatory")
_VolumeTotalFreeSpace_Type = Integer32
_VolumeTotalFreeSpace_Object = MibTableColumn
volumeTotalFreeSpace = _VolumeTotalFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 16),
    _VolumeTotalFreeSpace_Type()
)
volumeTotalFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTotalFreeSpace.setStatus("mandatory")
_VolumeLargestContigFree_Type = Integer32
_VolumeLargestContigFree_Object = MibTableColumn
volumeLargestContigFree = _VolumeLargestContigFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 17),
    _VolumeLargestContigFree_Type()
)
volumeLargestContigFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeLargestContigFree.setStatus("mandatory")
_VolumePercentUtilized_Type = Integer32
_VolumePercentUtilized_Object = MibTableColumn
volumePercentUtilized = _VolumePercentUtilized_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 1, 2, 1, 18),
    _VolumePercentUtilized_Type()
)
volumePercentUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumePercentUtilized.setStatus("mandatory")
_Processor_ObjectIdentity = ObjectIdentity
processor = _Processor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2)
)
_NumActive_Type = Integer32
_NumActive_Object = MibScalar
numActive = _NumActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 1),
    _NumActive_Type()
)
numActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numActive.setStatus("mandatory")
_NumPresent_Type = Integer32
_NumPresent_Object = MibScalar
numPresent = _NumPresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 2),
    _NumPresent_Type()
)
numPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPresent.setStatus("mandatory")


class _ProcessorMIstate_Type(Integer32):
    """Custom type processorMIstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ProcessorMIstate_Type.__name__ = "Integer32"
_ProcessorMIstate_Object = MibScalar
processorMIstate = _ProcessorMIstate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 3),
    _ProcessorMIstate_Type()
)
processorMIstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    processorMIstate.setStatus("mandatory")
_CpuUtilization_Type = Integer32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 1, 3, 2, 4),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-MPE-XL",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "general": general,
       "mpeXLSystem": mpeXLSystem,
       "volume": volume,
       "volumeMounted": volumeMounted,
       "volumeTable": volumeTable,
       "volumeEntry": volumeEntry,
       "volumeLDEV": volumeLDEV,
       "volumeName": volumeName,
       "volumeDriveType": volumeDriveType,
       "volumeSectorSize": volumeSectorSize,
       "volumeType": volumeType,
       "volumeCapacity": volumeCapacity,
       "volumeMPEOverhead": volumeMPEOverhead,
       "volumeMPETransOverhead": volumeMPETransOverhead,
       "volumeMPEConfigMaxTrans": volumeMPEConfigMaxTrans,
       "volumeDirSpaceOverhead": volumeDirSpaceOverhead,
       "volumeFileLabelOverhead": volumeFileLabelOverhead,
       "volumeTransactionMgmtOverhead": volumeTransactionMgmtOverhead,
       "volumeSpoolFileDiscUsage": volumeSpoolFileDiscUsage,
       "volumePermFiles": volumePermFiles,
       "volumeTempFiles": volumeTempFiles,
       "volumeTotalFreeSpace": volumeTotalFreeSpace,
       "volumeLargestContigFree": volumeLargestContigFree,
       "volumePercentUtilized": volumePercentUtilized,
       "processor": processor,
       "numActive": numActive,
       "numPresent": numPresent,
       "processorMIstate": processorMIstate,
       "cpuUtilization": cpuUtilization}
)
