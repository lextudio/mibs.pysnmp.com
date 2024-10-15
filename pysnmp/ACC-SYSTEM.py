# SNMP MIB module (ACC-SYSTEM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SYSTEM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:41 2024
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

(DisplayString,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "accBRG")

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
 NotificationType,
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
    "NotificationType",
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

_AccSystem_ObjectIdentity = ObjectIdentity
accSystem = _AccSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1)
)
_AccSysInfo_ObjectIdentity = ObjectIdentity
accSysInfo = _AccSysInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1)
)
_AccUnitName_Type = DisplayString
_AccUnitName_Object = MibScalar
accUnitName = _AccUnitName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 1),
    _AccUnitName_Type()
)
accUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUnitName.setStatus("mandatory")
_AccRomId_Type = DisplayString
_AccRomId_Object = MibScalar
accRomId = _AccRomId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 2),
    _AccRomId_Type()
)
accRomId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRomId.setStatus("mandatory")
_AccSwVersion_Type = DisplayString
_AccSwVersion_Object = MibScalar
accSwVersion = _AccSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 3),
    _AccSwVersion_Type()
)
accSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSwVersion.setStatus("mandatory")
_AccReset_Type = Integer32
_AccReset_Object = MibScalar
accReset = _AccReset_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 4),
    _AccReset_Type()
)
accReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accReset.setStatus("mandatory")
_AccMemStatTable_Object = MibTable
accMemStatTable = _AccMemStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    accMemStatTable.setStatus("mandatory")
_AccMemStatEntry_Object = MibTableRow
accMemStatEntry = _AccMemStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1)
)
accMemStatEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol4"),
)
if mibBuilder.loadTexts:
    accMemStatEntry.setStatus("mandatory")
_AccMemBlkEntSize_Type = Integer32
_AccMemBlkEntSize_Object = MibTableColumn
accMemBlkEntSize = _AccMemBlkEntSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 1),
    _AccMemBlkEntSize_Type()
)
accMemBlkEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntSize.setStatus("mandatory")
_AccMemBlkEntTotal_Type = Integer32
_AccMemBlkEntTotal_Object = MibTableColumn
accMemBlkEntTotal = _AccMemBlkEntTotal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 2),
    _AccMemBlkEntTotal_Type()
)
accMemBlkEntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntTotal.setStatus("mandatory")
_AccMemBlkEntMax_Type = Gauge32
_AccMemBlkEntMax_Object = MibTableColumn
accMemBlkEntMax = _AccMemBlkEntMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 3),
    _AccMemBlkEntMax_Type()
)
accMemBlkEntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntMax.setStatus("mandatory")
_AccMemBlkEntInUse_Type = Gauge32
_AccMemBlkEntInUse_Object = MibTableColumn
accMemBlkEntInUse = _AccMemBlkEntInUse_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 4),
    _AccMemBlkEntInUse_Type()
)
accMemBlkEntInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntInUse.setStatus("mandatory")
_AccMemBlkEntFails_Type = Counter32
_AccMemBlkEntFails_Object = MibTableColumn
accMemBlkEntFails = _AccMemBlkEntFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 5),
    _AccMemBlkEntFails_Type()
)
accMemBlkEntFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntFails.setStatus("mandatory")
_AccMemBlkEntType_Type = Integer32
_AccMemBlkEntType_Object = MibTableColumn
accMemBlkEntType = _AccMemBlkEntType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 6),
    _AccMemBlkEntType_Type()
)
accMemBlkEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntType.setStatus("mandatory")
_AccMemBlkEntAllocs_Type = Counter32
_AccMemBlkEntAllocs_Object = MibTableColumn
accMemBlkEntAllocs = _AccMemBlkEntAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 7),
    _AccMemBlkEntAllocs_Type()
)
accMemBlkEntAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntAllocs.setStatus("mandatory")
_AccMemBlkEntInitial_Type = Integer32
_AccMemBlkEntInitial_Object = MibTableColumn
accMemBlkEntInitial = _AccMemBlkEntInitial_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 8),
    _AccMemBlkEntInitial_Type()
)
accMemBlkEntInitial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntInitial.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_AccNvm_ObjectIdentity = ObjectIdentity
accNvm = _AccNvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6)
)
_AccNvmTotalBlks_Type = Integer32
_AccNvmTotalBlks_Object = MibScalar
accNvmTotalBlks = _AccNvmTotalBlks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 1),
    _AccNvmTotalBlks_Type()
)
accNvmTotalBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmTotalBlks.setStatus("mandatory")
_AccNvmBlkSize_Type = Integer32
_AccNvmBlkSize_Object = MibScalar
accNvmBlkSize = _AccNvmBlkSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 2),
    _AccNvmBlkSize_Type()
)
accNvmBlkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmBlkSize.setStatus("mandatory")
_AccNvmDirSize_Type = Integer32
_AccNvmDirSize_Object = MibScalar
accNvmDirSize = _AccNvmDirSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 3),
    _AccNvmDirSize_Type()
)
accNvmDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmDirSize.setStatus("mandatory")
_AccNvmFreeBlks_Type = Integer32
_AccNvmFreeBlks_Object = MibScalar
accNvmFreeBlks = _AccNvmFreeBlks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 4),
    _AccNvmFreeBlks_Type()
)
accNvmFreeBlks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmFreeBlks.setStatus("mandatory")
_AccNvmFileNumber_Type = Integer32
_AccNvmFileNumber_Object = MibScalar
accNvmFileNumber = _AccNvmFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 5),
    _AccNvmFileNumber_Type()
)
accNvmFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmFileNumber.setStatus("mandatory")
_AccNvmFileName_Type = OctetString
_AccNvmFileName_Object = MibScalar
accNvmFileName = _AccNvmFileName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 6),
    _AccNvmFileName_Type()
)
accNvmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmFileName.setStatus("mandatory")
_AccNvmFileSize_Type = Integer32
_AccNvmFileSize_Object = MibScalar
accNvmFileSize = _AccNvmFileSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 6, 7),
    _AccNvmFileSize_Type()
)
accNvmFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accNvmFileSize.setStatus("mandatory")
_AccSysConfigInfo_ObjectIdentity = ObjectIdentity
accSysConfigInfo = _AccSysConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 7)
)


class _AccConfiguration_Type(Integer32):
    """Custom type accConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("default", 3),
          ("load", 2),
          ("save", 1))
    )


_AccConfiguration_Type.__name__ = "Integer32"
_AccConfiguration_Object = MibScalar
accConfiguration = _AccConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 7, 1),
    _AccConfiguration_Type()
)
accConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accConfiguration.setStatus("mandatory")


class _AccConfigurationStatus_Type(Integer32):
    """Custom type accConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 2),
          ("saved", 1))
    )


_AccConfigurationStatus_Type.__name__ = "Integer32"
_AccConfigurationStatus_Object = MibScalar
accConfigurationStatus = _AccConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 7, 2),
    _AccConfigurationStatus_Type()
)
accConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accConfigurationStatus.setStatus("mandatory")
_AccScriptHalt_Type = Integer32
_AccScriptHalt_Object = MibScalar
accScriptHalt = _AccScriptHalt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 8),
    _AccScriptHalt_Type()
)
accScriptHalt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accScriptHalt.setStatus("mandatory")
_AccScriptCont_ObjectIdentity = ObjectIdentity
accScriptCont = _AccScriptCont_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 9)
)
_AccScriptContServer_Type = IpAddress
_AccScriptContServer_Object = MibScalar
accScriptContServer = _AccScriptContServer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 9, 1),
    _AccScriptContServer_Type()
)
accScriptContServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accScriptContServer.setStatus("mandatory")
_AccScriptContFile_Type = DisplayString
_AccScriptContFile_Object = MibScalar
accScriptContFile = _AccScriptContFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 9, 2),
    _AccScriptContFile_Type()
)
accScriptContFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accScriptContFile.setStatus("mandatory")
_AccSysUpgradeCmd_Type = OctetString
_AccSysUpgradeCmd_Object = MibScalar
accSysUpgradeCmd = _AccSysUpgradeCmd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 10),
    _AccSysUpgradeCmd_Type()
)
accSysUpgradeCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysUpgradeCmd.setStatus("mandatory")


class _AccSysHWType_Type(Integer32):
    """Custom type accSysHWType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("acc4100", 0),
          ("acc4100R", 1),
          ("acc4200", 2),
          ("amazon", 7),
          ("danube", 9),
          ("infotron", 4),
          ("nile", 5),
          ("tahoe", 8),
          ("tigris", 6),
          ("ub8000", 3))
    )


_AccSysHWType_Type.__name__ = "Integer32"
_AccSysHWType_Object = MibScalar
accSysHWType = _AccSysHWType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 11),
    _AccSysHWType_Type()
)
accSysHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysHWType.setStatus("mandatory")


class _AccSysProcType_Type(Integer32):
    """Custom type accSysProcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              96)
        )
    )
    namedValues = NamedValues(
        *(("motorola-68000", 0),
          ("motorola-68010", 16),
          ("motorola-68020", 32),
          ("motorola-68030", 48),
          ("motorola-68040", 64),
          ("motorola-68060", 96))
    )


_AccSysProcType_Type.__name__ = "Integer32"
_AccSysProcType_Object = MibScalar
accSysProcType = _AccSysProcType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 12),
    _AccSysProcType_Type()
)
accSysProcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysProcType.setStatus("mandatory")
_AccSysLocalRam_Type = Integer32
_AccSysLocalRam_Object = MibScalar
accSysLocalRam = _AccSysLocalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 13),
    _AccSysLocalRam_Type()
)
accSysLocalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysLocalRam.setStatus("mandatory")
_AccSysGlobalRam_Type = Integer32
_AccSysGlobalRam_Object = MibScalar
accSysGlobalRam = _AccSysGlobalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 14),
    _AccSysGlobalRam_Type()
)
accSysGlobalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysGlobalRam.setStatus("mandatory")


class _AccSysPowerSupply_Type(Integer32):
    """Custom type accSysPowerSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dual-both-operational", 2),
          ("dual-one-malfunctioning", 3),
          ("single", 1))
    )


_AccSysPowerSupply_Type.__name__ = "Integer32"
_AccSysPowerSupply_Object = MibScalar
accSysPowerSupply = _AccSysPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 15),
    _AccSysPowerSupply_Type()
)
accSysPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysPowerSupply.setStatus("mandatory")
_AccMemPoolTable_Object = MibTable
accMemPoolTable = _AccMemPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    accMemPoolTable.setStatus("mandatory")
_AccMemPoolEntry_Object = MibTableRow
accMemPoolEntry = _AccMemPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1)
)
accMemPoolEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol8"),
)
if mibBuilder.loadTexts:
    accMemPoolEntry.setStatus("mandatory")
_AccMemPoolName_Type = DisplayString
_AccMemPoolName_Object = MibTableColumn
accMemPoolName = _AccMemPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 1),
    _AccMemPoolName_Type()
)
accMemPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolName.setStatus("mandatory")
_AccMemPoolMaximum_Type = Gauge32
_AccMemPoolMaximum_Object = MibTableColumn
accMemPoolMaximum = _AccMemPoolMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 2),
    _AccMemPoolMaximum_Type()
)
accMemPoolMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolMaximum.setStatus("mandatory")
_AccMemPoolBytes_Type = Gauge32
_AccMemPoolBytes_Object = MibTableColumn
accMemPoolBytes = _AccMemPoolBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 3),
    _AccMemPoolBytes_Type()
)
accMemPoolBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolBytes.setStatus("mandatory")
_AccMemPoolFrags_Type = Gauge32
_AccMemPoolFrags_Object = MibTableColumn
accMemPoolFrags = _AccMemPoolFrags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 4),
    _AccMemPoolFrags_Type()
)
accMemPoolFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolFrags.setStatus("mandatory")
_AccMemPoolAlign_Type = Integer32
_AccMemPoolAlign_Object = MibTableColumn
accMemPoolAlign = _AccMemPoolAlign_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 5),
    _AccMemPoolAlign_Type()
)
accMemPoolAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolAlign.setStatus("mandatory")
_AccMemPoolAllocs_Type = Counter32
_AccMemPoolAllocs_Object = MibTableColumn
accMemPoolAllocs = _AccMemPoolAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 6),
    _AccMemPoolAllocs_Type()
)
accMemPoolAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolAllocs.setStatus("mandatory")
_AccMemPoolFails_Type = Counter32
_AccMemPoolFails_Object = MibTableColumn
accMemPoolFails = _AccMemPoolFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 7),
    _AccMemPoolFails_Type()
)
accMemPoolFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemPoolFails.setStatus("mandatory")
_PysmiFakeCol8_Type = Integer32
_PysmiFakeCol8_Object = MibTableColumn
pysmiFakeCol8 = _PysmiFakeCol8_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 16, 1, 4294967295),
    _PysmiFakeCol8_Type()
)
pysmiFakeCol8.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol8.setStatus("mandatory")
_AccMemAddDblk_Type = Integer32
_AccMemAddDblk_Object = MibScalar
accMemAddDblk = _AccMemAddDblk_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 17),
    _AccMemAddDblk_Type()
)
accMemAddDblk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemAddDblk.setStatus("mandatory")
_AccSlvConfTable_Object = MibTable
accSlvConfTable = _AccSlvConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    accSlvConfTable.setStatus("mandatory")
_AccSlvConfEntry_Object = MibTableRow
accSlvConfEntry = _AccSlvConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1)
)
accSlvConfEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accSlvConfCPUIndex"),
)
if mibBuilder.loadTexts:
    accSlvConfEntry.setStatus("mandatory")
_AccSlvConfCPUIndex_Type = Integer32
_AccSlvConfCPUIndex_Object = MibTableColumn
accSlvConfCPUIndex = _AccSlvConfCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 1),
    _AccSlvConfCPUIndex_Type()
)
accSlvConfCPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfCPUIndex.setStatus("mandatory")
_AccSlvConfCPUID_Type = DisplayString
_AccSlvConfCPUID_Object = MibTableColumn
accSlvConfCPUID = _AccSlvConfCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 2),
    _AccSlvConfCPUID_Type()
)
accSlvConfCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfCPUID.setStatus("mandatory")
_AccSlvConfSysDesc_Type = DisplayString
_AccSlvConfSysDesc_Object = MibTableColumn
accSlvConfSysDesc = _AccSlvConfSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 3),
    _AccSlvConfSysDesc_Type()
)
accSlvConfSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfSysDesc.setStatus("mandatory")
_AccSlvConfSWVers_Type = DisplayString
_AccSlvConfSWVers_Object = MibTableColumn
accSlvConfSWVers = _AccSlvConfSWVers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 4),
    _AccSlvConfSWVers_Type()
)
accSlvConfSWVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfSWVers.setStatus("mandatory")


class _AccSlvConfProcType_Type(Integer32):
    """Custom type accSlvConfProcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64)
        )
    )
    namedValues = NamedValues(
        *(("motorola-68000", 0),
          ("motorola-68010", 16),
          ("motorola-68020", 32),
          ("motorola-68030", 48),
          ("motorola-68040", 64))
    )


_AccSlvConfProcType_Type.__name__ = "Integer32"
_AccSlvConfProcType_Object = MibTableColumn
accSlvConfProcType = _AccSlvConfProcType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 5),
    _AccSlvConfProcType_Type()
)
accSlvConfProcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfProcType.setStatus("mandatory")
_AccSlvConfLocalRam_Type = Integer32
_AccSlvConfLocalRam_Object = MibTableColumn
accSlvConfLocalRam = _AccSlvConfLocalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 6),
    _AccSlvConfLocalRam_Type()
)
accSlvConfLocalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfLocalRam.setStatus("mandatory")
_AccSlvConfGlobalRam_Type = Integer32
_AccSlvConfGlobalRam_Object = MibTableColumn
accSlvConfGlobalRam = _AccSlvConfGlobalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 18, 1, 7),
    _AccSlvConfGlobalRam_Type()
)
accSlvConfGlobalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvConfGlobalRam.setStatus("mandatory")
_AccSlvMemBlkTable_Object = MibTable
accSlvMemBlkTable = _AccSlvMemBlkTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19)
)
if mibBuilder.loadTexts:
    accSlvMemBlkTable.setStatus("mandatory")
_AccSlvMemBlkEntry_Object = MibTableRow
accSlvMemBlkEntry = _AccSlvMemBlkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1)
)
accSlvMemBlkEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol9"),
)
if mibBuilder.loadTexts:
    accSlvMemBlkEntry.setStatus("mandatory")
_AccSlvMemCPUID_Type = DisplayString
_AccSlvMemCPUID_Object = MibTableColumn
accSlvMemCPUID = _AccSlvMemCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 3),
    _AccSlvMemCPUID_Type()
)
accSlvMemCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemCPUID.setStatus("mandatory")
_AccSlvMemBlkEntSize_Type = Integer32
_AccSlvMemBlkEntSize_Object = MibTableColumn
accSlvMemBlkEntSize = _AccSlvMemBlkEntSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 4),
    _AccSlvMemBlkEntSize_Type()
)
accSlvMemBlkEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntSize.setStatus("mandatory")
_AccSlvMemBlkEntTotal_Type = Integer32
_AccSlvMemBlkEntTotal_Object = MibTableColumn
accSlvMemBlkEntTotal = _AccSlvMemBlkEntTotal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 5),
    _AccSlvMemBlkEntTotal_Type()
)
accSlvMemBlkEntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntTotal.setStatus("mandatory")
_AccSlvMemBlkEntMax_Type = Gauge32
_AccSlvMemBlkEntMax_Object = MibTableColumn
accSlvMemBlkEntMax = _AccSlvMemBlkEntMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 6),
    _AccSlvMemBlkEntMax_Type()
)
accSlvMemBlkEntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntMax.setStatus("mandatory")
_AccSlvMemBlkEntInUse_Type = Gauge32
_AccSlvMemBlkEntInUse_Object = MibTableColumn
accSlvMemBlkEntInUse = _AccSlvMemBlkEntInUse_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 7),
    _AccSlvMemBlkEntInUse_Type()
)
accSlvMemBlkEntInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntInUse.setStatus("mandatory")
_AccSlvMemBlkEntFails_Type = Counter32
_AccSlvMemBlkEntFails_Object = MibTableColumn
accSlvMemBlkEntFails = _AccSlvMemBlkEntFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 8),
    _AccSlvMemBlkEntFails_Type()
)
accSlvMemBlkEntFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntFails.setStatus("mandatory")


class _AccSlvMemBlkEntType_Type(Integer32):
    """Custom type accSlvMemBlkEntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("cblk", 3),
          ("dblk", 1),
          ("fast", 9),
          ("global", 11),
          ("local", 10),
          ("mblk", 2),
          ("reserved", 12))
    )


_AccSlvMemBlkEntType_Type.__name__ = "Integer32"
_AccSlvMemBlkEntType_Object = MibTableColumn
accSlvMemBlkEntType = _AccSlvMemBlkEntType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 9),
    _AccSlvMemBlkEntType_Type()
)
accSlvMemBlkEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntType.setStatus("mandatory")
_AccSlvMemBlkEntAllocs_Type = Counter32
_AccSlvMemBlkEntAllocs_Object = MibTableColumn
accSlvMemBlkEntAllocs = _AccSlvMemBlkEntAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 10),
    _AccSlvMemBlkEntAllocs_Type()
)
accSlvMemBlkEntAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemBlkEntAllocs.setStatus("mandatory")
_PysmiFakeCol9_Type = Integer32
_PysmiFakeCol9_Object = MibTableColumn
pysmiFakeCol9 = _PysmiFakeCol9_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 19, 1, 4294967295),
    _PysmiFakeCol9_Type()
)
pysmiFakeCol9.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol9.setStatus("mandatory")
_AccSlvMemPool_ObjectIdentity = ObjectIdentity
accSlvMemPool = _AccSlvMemPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20)
)
_AccSlvMemPoolTable_Object = MibTable
accSlvMemPoolTable = _AccSlvMemPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    accSlvMemPoolTable.setStatus("mandatory")
_AccSlvMemPoolEntry_Object = MibTableRow
accSlvMemPoolEntry = _AccSlvMemPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1)
)
accSlvMemPoolEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol10"),
    (0, "ACC-SYSTEM", "pysmiFakeCol11"),
)
if mibBuilder.loadTexts:
    accSlvMemPoolEntry.setStatus("mandatory")
_AccSlvMemPoolCPUID_Type = DisplayString
_AccSlvMemPoolCPUID_Object = MibTableColumn
accSlvMemPoolCPUID = _AccSlvMemPoolCPUID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 1),
    _AccSlvMemPoolCPUID_Type()
)
accSlvMemPoolCPUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolCPUID.setStatus("mandatory")
_AccSlvMemPoolName_Type = DisplayString
_AccSlvMemPoolName_Object = MibTableColumn
accSlvMemPoolName = _AccSlvMemPoolName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 2),
    _AccSlvMemPoolName_Type()
)
accSlvMemPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolName.setStatus("mandatory")
_AccSlvMemPoolMaximum_Type = Gauge32
_AccSlvMemPoolMaximum_Object = MibTableColumn
accSlvMemPoolMaximum = _AccSlvMemPoolMaximum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 3),
    _AccSlvMemPoolMaximum_Type()
)
accSlvMemPoolMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolMaximum.setStatus("mandatory")
_AccSlvMemPoolBytes_Type = Gauge32
_AccSlvMemPoolBytes_Object = MibTableColumn
accSlvMemPoolBytes = _AccSlvMemPoolBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 4),
    _AccSlvMemPoolBytes_Type()
)
accSlvMemPoolBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolBytes.setStatus("mandatory")
_AccSlvMemPoolFrags_Type = Gauge32
_AccSlvMemPoolFrags_Object = MibTableColumn
accSlvMemPoolFrags = _AccSlvMemPoolFrags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 5),
    _AccSlvMemPoolFrags_Type()
)
accSlvMemPoolFrags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolFrags.setStatus("mandatory")
_AccSlvMemPoolAlign_Type = Integer32
_AccSlvMemPoolAlign_Object = MibTableColumn
accSlvMemPoolAlign = _AccSlvMemPoolAlign_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 6),
    _AccSlvMemPoolAlign_Type()
)
accSlvMemPoolAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolAlign.setStatus("mandatory")
_AccSlvMemPoolAllocs_Type = Counter32
_AccSlvMemPoolAllocs_Object = MibTableColumn
accSlvMemPoolAllocs = _AccSlvMemPoolAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 7),
    _AccSlvMemPoolAllocs_Type()
)
accSlvMemPoolAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolAllocs.setStatus("mandatory")
_AccSlvMemPoolFails_Type = Counter32
_AccSlvMemPoolFails_Object = MibTableColumn
accSlvMemPoolFails = _AccSlvMemPoolFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 8),
    _AccSlvMemPoolFails_Type()
)
accSlvMemPoolFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvMemPoolFails.setStatus("mandatory")
_PysmiFakeCol11_Type = Integer32
_PysmiFakeCol11_Object = MibTableColumn
pysmiFakeCol11 = _PysmiFakeCol11_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 4294967294),
    _PysmiFakeCol11_Type()
)
pysmiFakeCol11.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol11.setStatus("mandatory")
_PysmiFakeCol10_Type = Integer32
_PysmiFakeCol10_Object = MibTableColumn
pysmiFakeCol10 = _PysmiFakeCol10_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 20, 1, 1, 4294967295),
    _PysmiFakeCol10_Type()
)
pysmiFakeCol10.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol10.setStatus("mandatory")
_AccSlvSysTable_Object = MibTable
accSlvSysTable = _AccSlvSysTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    accSlvSysTable.setStatus("mandatory")
_AccSlvSysEntry_Object = MibTableRow
accSlvSysEntry = _AccSlvSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21, 1)
)
accSlvSysEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol12"),
)
if mibBuilder.loadTexts:
    accSlvSysEntry.setStatus("mandatory")
_AccSlvSysUpTime_Type = TimeTicks
_AccSlvSysUpTime_Object = MibTableColumn
accSlvSysUpTime = _AccSlvSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21, 1, 1),
    _AccSlvSysUpTime_Type()
)
accSlvSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvSysUpTime.setStatus("mandatory")
_AccSlvSysCpuAvgShort_Type = Integer32
_AccSlvSysCpuAvgShort_Object = MibTableColumn
accSlvSysCpuAvgShort = _AccSlvSysCpuAvgShort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21, 1, 2),
    _AccSlvSysCpuAvgShort_Type()
)
accSlvSysCpuAvgShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvSysCpuAvgShort.setStatus("mandatory")
_AccSlvSysCpuAvgLong_Type = Integer32
_AccSlvSysCpuAvgLong_Object = MibTableColumn
accSlvSysCpuAvgLong = _AccSlvSysCpuAvgLong_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21, 1, 3),
    _AccSlvSysCpuAvgLong_Type()
)
accSlvSysCpuAvgLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlvSysCpuAvgLong.setStatus("mandatory")
_PysmiFakeCol12_Type = Integer32
_PysmiFakeCol12_Object = MibTableColumn
pysmiFakeCol12 = _PysmiFakeCol12_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 21, 1, 4294967295),
    _PysmiFakeCol12_Type()
)
pysmiFakeCol12.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol12.setStatus("mandatory")
_AccMem_ObjectIdentity = ObjectIdentity
accMem = _AccMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22)
)
_AccMemDblkIncTable_Object = MibTable
accMemDblkIncTable = _AccMemDblkIncTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 1)
)
if mibBuilder.loadTexts:
    accMemDblkIncTable.setStatus("mandatory")
_AccMemDblkIncEntry_Object = MibTableRow
accMemDblkIncEntry = _AccMemDblkIncEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 1, 1)
)
accMemDblkIncEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accMemDblkIndex"),
)
if mibBuilder.loadTexts:
    accMemDblkIncEntry.setStatus("mandatory")
_AccMemDblkIndex_Type = Integer32
_AccMemDblkIndex_Object = MibTableColumn
accMemDblkIndex = _AccMemDblkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 1, 1, 1),
    _AccMemDblkIndex_Type()
)
accMemDblkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemDblkIndex.setStatus("mandatory")
_AccMemDblkSize_Type = Integer32
_AccMemDblkSize_Object = MibTableColumn
accMemDblkSize = _AccMemDblkSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 1, 1, 2),
    _AccMemDblkSize_Type()
)
accMemDblkSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemDblkSize.setStatus("mandatory")
_AccMemDblkIncrement_Type = Integer32
_AccMemDblkIncrement_Object = MibTableColumn
accMemDblkIncrement = _AccMemDblkIncrement_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 1, 1, 3),
    _AccMemDblkIncrement_Type()
)
accMemDblkIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMemDblkIncrement.setStatus("mandatory")
_AccOpt_ObjectIdentity = ObjectIdentity
accOpt = _AccOpt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2)
)


class _AccMemEMEStatus_Type(Integer32):
    """Custom type accMemEMEStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccMemEMEStatus_Type.__name__ = "Integer32"
_AccMemEMEStatus_Object = MibScalar
accMemEMEStatus = _AccMemEMEStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 1),
    _AccMemEMEStatus_Type()
)
accMemEMEStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMemEMEStatus.setStatus("mandatory")
_AccMemEMEMaxReclMem_Type = Integer32
_AccMemEMEMaxReclMem_Object = MibScalar
accMemEMEMaxReclMem = _AccMemEMEMaxReclMem_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 2),
    _AccMemEMEMaxReclMem_Type()
)
accMemEMEMaxReclMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemEMEMaxReclMem.setStatus("mandatory")
_AccMemEMECurReclMem_Type = Integer32
_AccMemEMECurReclMem_Object = MibScalar
accMemEMECurReclMem = _AccMemEMECurReclMem_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 3),
    _AccMemEMECurReclMem_Type()
)
accMemEMECurReclMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemEMECurReclMem.setStatus("mandatory")
_AccMemOptTable_Object = MibTable
accMemOptTable = _AccMemOptTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4)
)
if mibBuilder.loadTexts:
    accMemOptTable.setStatus("mandatory")
_AccMemOptEntry_Object = MibTableRow
accMemOptEntry = _AccMemOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4, 1)
)
accMemOptEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accMemOptimiserFeature"),
)
if mibBuilder.loadTexts:
    accMemOptEntry.setStatus("mandatory")
_AccMemOptimiserFeature_Type = OctetString
_AccMemOptimiserFeature_Object = MibTableColumn
accMemOptimiserFeature = _AccMemOptimiserFeature_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4, 1, 1),
    _AccMemOptimiserFeature_Type()
)
accMemOptimiserFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemOptimiserFeature.setStatus("mandatory")
_AccMemOptimiserMemory_Type = Integer32
_AccMemOptimiserMemory_Object = MibTableColumn
accMemOptimiserMemory = _AccMemOptimiserMemory_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4, 1, 2),
    _AccMemOptimiserMemory_Type()
)
accMemOptimiserMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemOptimiserMemory.setStatus("mandatory")


class _AccMemOptimiserPref_Type(Integer32):
    """Custom type accMemOptimiserPref based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 3),
          ("reclaim", 1),
          ("use", 2))
    )


_AccMemOptimiserPref_Type.__name__ = "Integer32"
_AccMemOptimiserPref_Object = MibTableColumn
accMemOptimiserPref = _AccMemOptimiserPref_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4, 1, 3),
    _AccMemOptimiserPref_Type()
)
accMemOptimiserPref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMemOptimiserPref.setStatus("mandatory")


class _AccMemOptimiserStatus_Type(Integer32):
    """Custom type accMemOptimiserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inuse", 2),
          ("reclaimed", 1))
    )


_AccMemOptimiserStatus_Type.__name__ = "Integer32"
_AccMemOptimiserStatus_Object = MibTableColumn
accMemOptimiserStatus = _AccMemOptimiserStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 22, 2, 4, 1, 4),
    _AccMemOptimiserStatus_Type()
)
accMemOptimiserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemOptimiserStatus.setStatus("mandatory")
_AccMacro_ObjectIdentity = ObjectIdentity
accMacro = _AccMacro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 23)
)


class _AccMacroExecute_Type(Integer32):
    """Custom type accMacroExecute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipx-dial-filter", 2),
          ("none", 1))
    )


_AccMacroExecute_Type.__name__ = "Integer32"
_AccMacroExecute_Object = MibScalar
accMacroExecute = _AccMacroExecute_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 23, 1),
    _AccMacroExecute_Type()
)
accMacroExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMacroExecute.setStatus("mandatory")
_AccSwRegistrationKey_Type = DisplayString
_AccSwRegistrationKey_Object = MibScalar
accSwRegistrationKey = _AccSwRegistrationKey_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 24),
    _AccSwRegistrationKey_Type()
)
accSwRegistrationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSwRegistrationKey.setStatus("mandatory")
_AccMACAddr_ObjectIdentity = ObjectIdentity
accMACAddr = _AccMACAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 25)
)
_AccSysMACAddrUser_Type = OctetString
_AccSysMACAddrUser_Object = MibScalar
accSysMACAddrUser = _AccSysMACAddrUser_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 25, 1),
    _AccSysMACAddrUser_Type()
)
accSysMACAddrUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSysMACAddrUser.setStatus("mandatory")
_AccSysMessage_ObjectIdentity = ObjectIdentity
accSysMessage = _AccSysMessage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26)
)
_AccSysMsgInfo_ObjectIdentity = ObjectIdentity
accSysMsgInfo = _AccSysMsgInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1)
)


class _AccSysMsgLevel_Type(Integer32):
    """Custom type accSysMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccSysMsgLevel_Type.__name__ = "Integer32"
_AccSysMsgLevel_Object = MibScalar
accSysMsgLevel = _AccSysMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1, 1),
    _AccSysMsgLevel_Type()
)
accSysMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSysMsgLevel.setStatus("mandatory")


class _AccWinDefLenNetman_Type(Integer32):
    """Custom type accWinDefLenNetman based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 65535),
    )


_AccWinDefLenNetman_Type.__name__ = "Integer32"
_AccWinDefLenNetman_Object = MibScalar
accWinDefLenNetman = _AccWinDefLenNetman_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1, 2),
    _AccWinDefLenNetman_Type()
)
accWinDefLenNetman.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accWinDefLenNetman.setStatus("mandatory")


class _AccWinDefLenPublic_Type(Integer32):
    """Custom type accWinDefLenPublic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 65535),
    )


_AccWinDefLenPublic_Type.__name__ = "Integer32"
_AccWinDefLenPublic_Object = MibScalar
accWinDefLenPublic = _AccWinDefLenPublic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1, 3),
    _AccWinDefLenPublic_Type()
)
accWinDefLenPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accWinDefLenPublic.setStatus("mandatory")


class _AccWinDefWidNetman_Type(Integer32):
    """Custom type accWinDefWidNetman based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 512),
    )


_AccWinDefWidNetman_Type.__name__ = "Integer32"
_AccWinDefWidNetman_Object = MibScalar
accWinDefWidNetman = _AccWinDefWidNetman_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1, 4),
    _AccWinDefWidNetman_Type()
)
accWinDefWidNetman.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accWinDefWidNetman.setStatus("mandatory")


class _AccWinDefWidPublic_Type(Integer32):
    """Custom type accWinDefWidPublic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 512),
    )


_AccWinDefWidPublic_Type.__name__ = "Integer32"
_AccWinDefWidPublic_Object = MibScalar
accWinDefWidPublic = _AccWinDefWidPublic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 1, 5),
    _AccWinDefWidPublic_Type()
)
accWinDefWidPublic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accWinDefWidPublic.setStatus("mandatory")
_AccUserInfo_ObjectIdentity = ObjectIdentity
accUserInfo = _AccUserInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 2)
)
_AccUserTrapMsgEntry_Type = DisplayString
_AccUserTrapMsgEntry_Object = MibScalar
accUserTrapMsgEntry = _AccUserTrapMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 26, 2, 1),
    _AccUserTrapMsgEntry_Type()
)
accUserTrapMsgEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUserTrapMsgEntry.setStatus("mandatory")
_AccVirtualPort_ObjectIdentity = ObjectIdentity
accVirtualPort = _AccVirtualPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 30)
)
_AccVirtualPortGeneral_ObjectIdentity = ObjectIdentity
accVirtualPortGeneral = _AccVirtualPortGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 30, 1)
)


class _AccVirtualPortCount_Type(Integer32):
    """Custom type accVirtualPortCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AccVirtualPortCount_Type.__name__ = "Integer32"
_AccVirtualPortCount_Object = MibScalar
accVirtualPortCount = _AccVirtualPortCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 30, 1, 1),
    _AccVirtualPortCount_Type()
)
accVirtualPortCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVirtualPortCount.setStatus("mandatory")


class _AccVirtualPortXotCount_Type(Integer32):
    """Custom type accVirtualPortXotCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AccVirtualPortXotCount_Type.__name__ = "Integer32"
_AccVirtualPortXotCount_Object = MibScalar
accVirtualPortXotCount = _AccVirtualPortXotCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 30, 1, 2),
    _AccVirtualPortXotCount_Type()
)
accVirtualPortXotCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accVirtualPortXotCount.setStatus("mandatory")
_AccSystemGracefulShutdown_ObjectIdentity = ObjectIdentity
accSystemGracefulShutdown = _AccSystemGracefulShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 32)
)


class _AccSystemGracefulShutdownState_Type(Integer32):
    """Custom type accSystemGracefulShutdownState based on Integer32"""
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


_AccSystemGracefulShutdownState_Type.__name__ = "Integer32"
_AccSystemGracefulShutdownState_Object = MibScalar
accSystemGracefulShutdownState = _AccSystemGracefulShutdownState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 32, 1),
    _AccSystemGracefulShutdownState_Type()
)
accSystemGracefulShutdownState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemGracefulShutdownState.setStatus("mandatory")


class _AccSystemGracefulShutdownTO_Type(Integer32):
    """Custom type accSystemGracefulShutdownTO based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_AccSystemGracefulShutdownTO_Type.__name__ = "Integer32"
_AccSystemGracefulShutdownTO_Object = MibScalar
accSystemGracefulShutdownTO = _AccSystemGracefulShutdownTO_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 32, 2),
    _AccSystemGracefulShutdownTO_Type()
)
accSystemGracefulShutdownTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemGracefulShutdownTO.setStatus("mandatory")
_AccSystemAuthGeneral_ObjectIdentity = ObjectIdentity
accSystemAuthGeneral = _AccSystemAuthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 33)
)


class _AccSystemAuthMode_Type(Integer32):
    """Custom type accSystemAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_AccSystemAuthMode_Type.__name__ = "Integer32"
_AccSystemAuthMode_Object = MibScalar
accSystemAuthMode = _AccSystemAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 33, 1),
    _AccSystemAuthMode_Type()
)
accSystemAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemAuthMode.setStatus("mandatory")
_AccSystemAuthAccessPart_Type = DisplayString
_AccSystemAuthAccessPart_Object = MibScalar
accSystemAuthAccessPart = _AccSystemAuthAccessPart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 33, 2),
    _AccSystemAuthAccessPart_Type()
)
accSystemAuthAccessPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemAuthAccessPart.setStatus("mandatory")
_AccSystemAccess_ObjectIdentity = ObjectIdentity
accSystemAccess = _AccSystemAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 34)
)


class _AccPscopeEnable_Type(Integer32):
    """Custom type accPscopeEnable based on Integer32"""
    defaultValue = 1

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


_AccPscopeEnable_Type.__name__ = "Integer32"
_AccPscopeEnable_Object = MibScalar
accPscopeEnable = _AccPscopeEnable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 34, 1),
    _AccPscopeEnable_Type()
)
accPscopeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPscopeEnable.setStatus("mandatory")
_AccDBscopeCntl_Type = Integer32
_AccDBscopeCntl_Object = MibScalar
accDBscopeCntl = _AccDBscopeCntl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 34, 2),
    _AccDBscopeCntl_Type()
)
accDBscopeCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDBscopeCntl.setStatus("mandatory")
_AccSessionCtrl_ObjectIdentity = ObjectIdentity
accSessionCtrl = _AccSessionCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 2)
)
_AccLogin_Type = DisplayString
_AccLogin_Object = MibScalar
accLogin = _AccLogin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 2, 1),
    _AccLogin_Type()
)
accLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLogin.setStatus("mandatory")
_AccLogout_Type = DisplayString
_AccLogout_Object = MibScalar
accLogout = _AccLogout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 2, 2),
    _AccLogout_Type()
)
accLogout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLogout.setStatus("mandatory")
_AccLoginTimeout_Type = TimeTicks
_AccLoginTimeout_Object = MibScalar
accLoginTimeout = _AccLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 2, 3),
    _AccLoginTimeout_Type()
)
accLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLoginTimeout.setStatus("mandatory")
_AccTrapTable_Object = MibTable
accTrapTable = _AccTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    accTrapTable.setStatus("mandatory")
_AccTrapEntry_Object = MibTableRow
accTrapEntry = _AccTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 3, 1)
)
accTrapEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accTrapAddr"),
)
if mibBuilder.loadTexts:
    accTrapEntry.setStatus("mandatory")
_AccTrapAddr_Type = IpAddress
_AccTrapAddr_Object = MibTableColumn
accTrapAddr = _AccTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 3, 1, 1),
    _AccTrapAddr_Type()
)
accTrapAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapAddr.setStatus("mandatory")


class _AccTrapSeverity_Type(Integer32):
    """Custom type accTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccTrapSeverity_Type.__name__ = "Integer32"
_AccTrapSeverity_Object = MibTableColumn
accTrapSeverity = _AccTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 3, 1, 2),
    _AccTrapSeverity_Type()
)
accTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapSeverity.setStatus("mandatory")
_AccClock_ObjectIdentity = ObjectIdentity
accClock = _AccClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4)
)
_AccDate_Type = OctetString
_AccDate_Object = MibScalar
accDate = _AccDate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 1),
    _AccDate_Type()
)
accDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDate.setStatus("deprecated")
_AccUToffset_Type = OctetString
_AccUToffset_Object = MibScalar
accUToffset = _AccUToffset_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 2),
    _AccUToffset_Type()
)
accUToffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accUToffset.setStatus("mandatory")
_AccSysBootTime_Type = OctetString
_AccSysBootTime_Object = MibScalar
accSysBootTime = _AccSysBootTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 3),
    _AccSysBootTime_Type()
)
accSysBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysBootTime.setStatus("deprecated")
_AccSysCpuAvgShort_Type = Integer32
_AccSysCpuAvgShort_Object = MibScalar
accSysCpuAvgShort = _AccSysCpuAvgShort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 4),
    _AccSysCpuAvgShort_Type()
)
accSysCpuAvgShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysCpuAvgShort.setStatus("mandatory")
_AccSysCpuAvgLong_Type = Integer32
_AccSysCpuAvgLong_Object = MibScalar
accSysCpuAvgLong = _AccSysCpuAvgLong_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 5),
    _AccSysCpuAvgLong_Type()
)
accSysCpuAvgLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysCpuAvgLong.setStatus("mandatory")


class _AccSysDataSwitchStatus_Type(Integer32):
    """Custom type accSysDataSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccSysDataSwitchStatus_Type.__name__ = "Integer32"
_AccSysDataSwitchStatus_Object = MibScalar
accSysDataSwitchStatus = _AccSysDataSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 6),
    _AccSysDataSwitchStatus_Type()
)
accSysDataSwitchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysDataSwitchStatus.setStatus("mandatory")
_AccSysLastConfig_Type = TimeTicks
_AccSysLastConfig_Object = MibScalar
accSysLastConfig = _AccSysLastConfig_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 8),
    _AccSysLastConfig_Type()
)
accSysLastConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSysLastConfig.setStatus("mandatory")
_AccDateY2K_Type = OctetString
_AccDateY2K_Object = MibScalar
accDateY2K = _AccDateY2K_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 10),
    _AccDateY2K_Type()
)
accDateY2K.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDateY2K.setStatus("mandatory")
_AccSysBootTimeY2K_Type = OctetString
_AccSysBootTimeY2K_Object = MibScalar
accSysBootTimeY2K = _AccSysBootTimeY2K_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 11),
    _AccSysBootTimeY2K_Type()
)
accSysBootTimeY2K.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysBootTimeY2K.setStatus("mandatory")


class _AccDay_Type(Integer32):
    """Custom type accDay based on Integer32"""
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
        *(("fri", 4),
          ("sat", 5),
          ("sun", 6),
          ("thu", 3),
          ("tue", 1),
          ("wed", 2))
    )


_AccDay_Type.__name__ = "Integer32"
_AccDay_Object = MibScalar
accDay = _AccDay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 4, 12),
    _AccDay_Type()
)
accDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDay.setStatus("mandatory")
_AccAccessTable_Object = MibTable
accAccessTable = _AccAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    accAccessTable.setStatus("mandatory")
_AccAccessEntry_Object = MibTableRow
accAccessEntry = _AccAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6, 1)
)
accAccessEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accAccessAddr"),
    (0, "ACC-SYSTEM", "accAccessNetMask"),
    (0, "ACC-SYSTEM", "accAccessUdpPort"),
)
if mibBuilder.loadTexts:
    accAccessEntry.setStatus("mandatory")
_AccAccessCmty_Type = DisplayString
_AccAccessCmty_Object = MibTableColumn
accAccessCmty = _AccAccessCmty_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6, 1, 1),
    _AccAccessCmty_Type()
)
accAccessCmty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessCmty.setStatus("mandatory")
_AccAccessAddr_Type = IpAddress
_AccAccessAddr_Object = MibTableColumn
accAccessAddr = _AccAccessAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6, 1, 2),
    _AccAccessAddr_Type()
)
accAccessAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessAddr.setStatus("mandatory")
_AccAccessNetMask_Type = IpAddress
_AccAccessNetMask_Object = MibTableColumn
accAccessNetMask = _AccAccessNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6, 1, 3),
    _AccAccessNetMask_Type()
)
accAccessNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessNetMask.setStatus("mandatory")
_AccAccessUdpPort_Type = Integer32
_AccAccessUdpPort_Object = MibTableColumn
accAccessUdpPort = _AccAccessUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 6, 1, 4),
    _AccAccessUdpPort_Type()
)
accAccessUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAccessUdpPort.setStatus("mandatory")
_AccReload_Type = TimeTicks
_AccReload_Object = MibScalar
accReload = _AccReload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 7),
    _AccReload_Type()
)
accReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accReload.setStatus("mandatory")
_AccIfNames_ObjectIdentity = ObjectIdentity
accIfNames = _AccIfNames_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8)
)
_AccIfNumNames_Type = Integer32
_AccIfNumNames_Object = MibScalar
accIfNumNames = _AccIfNumNames_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 1),
    _AccIfNumNames_Type()
)
accIfNumNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIfNumNames.setStatus("mandatory")
_AccIfNameTable_Object = MibTable
accIfNameTable = _AccIfNameTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    accIfNameTable.setStatus("mandatory")
_AccIfNameEntry_Object = MibTableRow
accIfNameEntry = _AccIfNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 2, 1)
)
accIfNameEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accIfNameIndex"),
)
if mibBuilder.loadTexts:
    accIfNameEntry.setStatus("mandatory")
_AccIfNameIndex_Type = Integer32
_AccIfNameIndex_Object = MibTableColumn
accIfNameIndex = _AccIfNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 2, 1, 1),
    _AccIfNameIndex_Type()
)
accIfNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIfNameIndex.setStatus("mandatory")
_AccIfName_Type = DisplayString
_AccIfName_Object = MibTableColumn
accIfName = _AccIfName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 2, 1, 2),
    _AccIfName_Type()
)
accIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIfName.setStatus("mandatory")
_AccIfNameDefault_Type = DisplayString
_AccIfNameDefault_Object = MibTableColumn
accIfNameDefault = _AccIfNameDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 8, 2, 1, 3),
    _AccIfNameDefault_Type()
)
accIfNameDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIfNameDefault.setStatus("mandatory")
_AccIfGroupTable_Object = MibTable
accIfGroupTable = _AccIfGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    accIfGroupTable.setStatus("mandatory")
_AccIfGroupEntry_Object = MibTableRow
accIfGroupEntry = _AccIfGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1)
)
accIfGroupEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accIFGroupIndex"),
)
if mibBuilder.loadTexts:
    accIfGroupEntry.setStatus("mandatory")
_AccIFGroupIndex_Type = Integer32
_AccIFGroupIndex_Object = MibTableColumn
accIFGroupIndex = _AccIFGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 1),
    _AccIFGroupIndex_Type()
)
accIFGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupIndex.setStatus("mandatory")
_AccIFGroupName_Type = DisplayString
_AccIFGroupName_Object = MibTableColumn
accIFGroupName = _AccIFGroupName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 2),
    _AccIFGroupName_Type()
)
accIFGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupName.setStatus("mandatory")


class _AccIFGroupType_Type(Integer32):
    """Custom type accIFGroupType based on Integer32"""
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
        *(("bridge-port", 2),
          ("dial-port", 3),
          ("multi-link", 4),
          ("physical-port", 1))
    )


_AccIFGroupType_Type.__name__ = "Integer32"
_AccIFGroupType_Object = MibTableColumn
accIFGroupType = _AccIFGroupType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 3),
    _AccIFGroupType_Type()
)
accIFGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupType.setStatus("mandatory")
_AccIFGroupIndexBase_Type = Integer32
_AccIFGroupIndexBase_Object = MibTableColumn
accIFGroupIndexBase = _AccIFGroupIndexBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 4),
    _AccIFGroupIndexBase_Type()
)
accIFGroupIndexBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupIndexBase.setStatus("mandatory")
_AccIFGroupIndexMax_Type = Integer32
_AccIFGroupIndexMax_Object = MibTableColumn
accIFGroupIndexMax = _AccIFGroupIndexMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 5),
    _AccIFGroupIndexMax_Type()
)
accIFGroupIndexMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupIndexMax.setStatus("mandatory")
_AccIFGroupNameDefault_Type = DisplayString
_AccIFGroupNameDefault_Object = MibTableColumn
accIFGroupNameDefault = _AccIFGroupNameDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 9, 1, 6),
    _AccIFGroupNameDefault_Type()
)
accIFGroupNameDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIFGroupNameDefault.setStatus("mandatory")
_AccTrapLog_ObjectIdentity = ObjectIdentity
accTrapLog = _AccTrapLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10)
)


class _AccTrapLogLevel_Type(Integer32):
    """Custom type accTrapLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccTrapLogLevel_Type.__name__ = "Integer32"
_AccTrapLogLevel_Object = MibScalar
accTrapLogLevel = _AccTrapLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 1),
    _AccTrapLogLevel_Type()
)
accTrapLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapLogLevel.setStatus("mandatory")


class _AccTrapLogSaveAction_Type(Integer32):
    """Custom type accTrapLogSaveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("save-now", 1)
    )


_AccTrapLogSaveAction_Type.__name__ = "Integer32"
_AccTrapLogSaveAction_Object = MibScalar
accTrapLogSaveAction = _AccTrapLogSaveAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 2),
    _AccTrapLogSaveAction_Type()
)
accTrapLogSaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapLogSaveAction.setStatus("mandatory")


class _AccTrapLogBufSize_Type(Integer32):
    """Custom type accTrapLogBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AccTrapLogBufSize_Type.__name__ = "Integer32"
_AccTrapLogBufSize_Object = MibScalar
accTrapLogBufSize = _AccTrapLogBufSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 3),
    _AccTrapLogBufSize_Type()
)
accTrapLogBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapLogBufSize.setStatus("mandatory")
_AccTrapLogTable_Object = MibTable
accTrapLogTable = _AccTrapLogTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    accTrapLogTable.setStatus("mandatory")
_AccTrapLogEntry_Object = MibTableRow
accTrapLogEntry = _AccTrapLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1)
)
accTrapLogEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol5"),
)
if mibBuilder.loadTexts:
    accTrapLogEntry.setStatus("mandatory")
_AccTrapLogTblTime_Type = TimeTicks
_AccTrapLogTblTime_Object = MibTableColumn
accTrapLogTblTime = _AccTrapLogTblTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 1),
    _AccTrapLogTblTime_Type()
)
accTrapLogTblTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogTblTime.setStatus("mandatory")


class _AccTrapLogTblType_Type(Integer32):
    """Custom type accTrapLogTblType based on Integer32"""
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
        *(("trap-authent-fail", 5),
          ("trap-coldstart", 1),
          ("trap-egpnborloss", 6),
          ("trap-enterprise", 7),
          ("trap-linkdown", 3),
          ("trap-linkup", 4),
          ("trap-warmstart", 2))
    )


_AccTrapLogTblType_Type.__name__ = "Integer32"
_AccTrapLogTblType_Object = MibTableColumn
accTrapLogTblType = _AccTrapLogTblType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 2),
    _AccTrapLogTblType_Type()
)
accTrapLogTblType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogTblType.setStatus("mandatory")


class _AccTrapLogTblLevel_Type(Integer32):
    """Custom type accTrapLogTblLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccTrapLogTblLevel_Type.__name__ = "Integer32"
_AccTrapLogTblLevel_Object = MibTableColumn
accTrapLogTblLevel = _AccTrapLogTblLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 3),
    _AccTrapLogTblLevel_Type()
)
accTrapLogTblLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogTblLevel.setStatus("mandatory")
_AccTrapLogTblData_Type = DisplayString
_AccTrapLogTblData_Object = MibTableColumn
accTrapLogTblData = _AccTrapLogTblData_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 4),
    _AccTrapLogTblData_Type()
)
accTrapLogTblData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogTblData.setStatus("mandatory")
_AccTrapLogSeqNum_Type = Counter32
_AccTrapLogSeqNum_Object = MibTableColumn
accTrapLogSeqNum = _AccTrapLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 6),
    _AccTrapLogSeqNum_Type()
)
accTrapLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogSeqNum.setStatus("mandatory")


class _AccTrapLogSeverityType_Type(Integer32):
    """Custom type accTrapLogSeverityType based on Integer32"""
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
        *(("clear", 5),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4))
    )


_AccTrapLogSeverityType_Type.__name__ = "Integer32"
_AccTrapLogSeverityType_Object = MibTableColumn
accTrapLogSeverityType = _AccTrapLogSeverityType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 7),
    _AccTrapLogSeverityType_Type()
)
accTrapLogSeverityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogSeverityType.setStatus("mandatory")
_AccTrapLogEnterpriseOID_Type = ObjectIdentifier
_AccTrapLogEnterpriseOID_Object = MibTableColumn
accTrapLogEnterpriseOID = _AccTrapLogEnterpriseOID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 8),
    _AccTrapLogEnterpriseOID_Type()
)
accTrapLogEnterpriseOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogEnterpriseOID.setStatus("mandatory")
_AccSpecificTrapNum_Type = Integer32
_AccSpecificTrapNum_Object = MibTableColumn
accSpecificTrapNum = _AccSpecificTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 9),
    _AccSpecificTrapNum_Type()
)
accSpecificTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSpecificTrapNum.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 4, 1, 4294967295),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_AccTrapLogSumTable_Object = MibTable
accTrapLogSumTable = _AccTrapLogSumTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    accTrapLogSumTable.setStatus("mandatory")
_AccTrapLogSumEntry_Object = MibTableRow
accTrapLogSumEntry = _AccTrapLogSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5, 1)
)
accTrapLogSumEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol6"),
)
if mibBuilder.loadTexts:
    accTrapLogSumEntry.setStatus("mandatory")
_AccTrapLogSumTime_Type = TimeTicks
_AccTrapLogSumTime_Object = MibTableColumn
accTrapLogSumTime = _AccTrapLogSumTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5, 1, 1),
    _AccTrapLogSumTime_Type()
)
accTrapLogSumTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogSumTime.setStatus("mandatory")


class _AccTrapLogSumType_Type(Integer32):
    """Custom type accTrapLogSumType based on Integer32"""
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
        *(("authent-fail", 5),
          ("coldstart", 1),
          ("egpnborloss", 6),
          ("enterprise", 7),
          ("linkdown", 3),
          ("linkup", 4),
          ("warmstart", 2))
    )


_AccTrapLogSumType_Type.__name__ = "Integer32"
_AccTrapLogSumType_Object = MibTableColumn
accTrapLogSumType = _AccTrapLogSumType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5, 1, 2),
    _AccTrapLogSumType_Type()
)
accTrapLogSumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogSumType.setStatus("mandatory")
_AccTrapLogSumData_Type = DisplayString
_AccTrapLogSumData_Object = MibTableColumn
accTrapLogSumData = _AccTrapLogSumData_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5, 1, 3),
    _AccTrapLogSumData_Type()
)
accTrapLogSumData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrapLogSumData.setStatus("mandatory")
_PysmiFakeCol6_Type = Integer32
_PysmiFakeCol6_Object = MibTableColumn
pysmiFakeCol6 = _PysmiFakeCol6_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 10, 5, 1, 4294967295),
    _PysmiFakeCol6_Type()
)
pysmiFakeCol6.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol6.setStatus("mandatory")
_AccSeepTable_Object = MibTable
accSeepTable = _AccSeepTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    accSeepTable.setStatus("mandatory")
_AccSeepEntry_Object = MibTableRow
accSeepEntry = _AccSeepEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1)
)
accSeepEntry.setIndexNames(
    (0, "ACC-SYSTEM", "pysmiFakeCol7"),
)
if mibBuilder.loadTexts:
    accSeepEntry.setStatus("mandatory")
_AccSeepEntrySlot_Type = DisplayString
_AccSeepEntrySlot_Object = MibTableColumn
accSeepEntrySlot = _AccSeepEntrySlot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 1),
    _AccSeepEntrySlot_Type()
)
accSeepEntrySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntrySlot.setStatus("mandatory")
_AccSeepEntryType_Type = DisplayString
_AccSeepEntryType_Object = MibTableColumn
accSeepEntryType = _AccSeepEntryType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 2),
    _AccSeepEntryType_Type()
)
accSeepEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntryType.setStatus("mandatory")
_AccSeepEntrySerial_Type = DisplayString
_AccSeepEntrySerial_Object = MibTableColumn
accSeepEntrySerial = _AccSeepEntrySerial_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 3),
    _AccSeepEntrySerial_Type()
)
accSeepEntrySerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntrySerial.setStatus("mandatory")
_AccSeepEntryAssembly_Type = DisplayString
_AccSeepEntryAssembly_Object = MibTableColumn
accSeepEntryAssembly = _AccSeepEntryAssembly_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 4),
    _AccSeepEntryAssembly_Type()
)
accSeepEntryAssembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntryAssembly.setStatus("mandatory")
_AccSeepEntryRev_Type = DisplayString
_AccSeepEntryRev_Object = MibTableColumn
accSeepEntryRev = _AccSeepEntryRev_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 5),
    _AccSeepEntryRev_Type()
)
accSeepEntryRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntryRev.setStatus("mandatory")
_AccSeepEntryDate_Type = DisplayString
_AccSeepEntryDate_Object = MibTableColumn
accSeepEntryDate = _AccSeepEntryDate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 6),
    _AccSeepEntryDate_Type()
)
accSeepEntryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSeepEntryDate.setStatus("mandatory")
_PysmiFakeCol7_Type = Integer32
_PysmiFakeCol7_Object = MibTableColumn
pysmiFakeCol7 = _PysmiFakeCol7_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 13, 1, 4294967295),
    _PysmiFakeCol7_Type()
)
pysmiFakeCol7.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol7.setStatus("mandatory")
_AccStandbyInfo_ObjectIdentity = ObjectIdentity
accStandbyInfo = _AccStandbyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14)
)
_AccStandbySysDescr_Type = DisplayString
_AccStandbySysDescr_Object = MibScalar
accStandbySysDescr = _AccStandbySysDescr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 1),
    _AccStandbySysDescr_Type()
)
accStandbySysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySysDescr.setStatus("mandatory")
_AccStandbySoftwareVersion_Type = DisplayString
_AccStandbySoftwareVersion_Object = MibScalar
accStandbySoftwareVersion = _AccStandbySoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 2),
    _AccStandbySoftwareVersion_Type()
)
accStandbySoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySoftwareVersion.setStatus("mandatory")


class _AccStandbySysProcType_Type(Integer32):
    """Custom type accStandbySysProcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            257
        )
    )
    namedValues = NamedValues(
        ("mips-idt", 257)
    )


_AccStandbySysProcType_Type.__name__ = "Integer32"
_AccStandbySysProcType_Object = MibScalar
accStandbySysProcType = _AccStandbySysProcType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 3),
    _AccStandbySysProcType_Type()
)
accStandbySysProcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySysProcType.setStatus("mandatory")
_AccStandbySysLocalRam_Type = Integer32
_AccStandbySysLocalRam_Object = MibScalar
accStandbySysLocalRam = _AccStandbySysLocalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 4),
    _AccStandbySysLocalRam_Type()
)
accStandbySysLocalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySysLocalRam.setStatus("mandatory")
_AccStandbySysGlobalRam_Type = Integer32
_AccStandbySysGlobalRam_Object = MibScalar
accStandbySysGlobalRam = _AccStandbySysGlobalRam_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 5),
    _AccStandbySysGlobalRam_Type()
)
accStandbySysGlobalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySysGlobalRam.setStatus("mandatory")


class _AccStandbyFsVolStatus_Type(Integer32):
    """Custom type accStandbyFsVolStatus based on Integer32"""
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
        *(("checking", 3),
          ("not-available", 2),
          ("not-synchronized", 4),
          ("synchronized", 1))
    )


_AccStandbyFsVolStatus_Type.__name__ = "Integer32"
_AccStandbyFsVolStatus_Object = MibScalar
accStandbyFsVolStatus = _AccStandbyFsVolStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 6),
    _AccStandbyFsVolStatus_Type()
)
accStandbyFsVolStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbyFsVolStatus.setStatus("mandatory")


class _AccStandbyFsCfgStatus_Type(Integer32):
    """Custom type accStandbyFsCfgStatus based on Integer32"""
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
        *(("checking", 3),
          ("not-available", 2),
          ("not-synchronized", 4),
          ("synchronized", 1))
    )


_AccStandbyFsCfgStatus_Type.__name__ = "Integer32"
_AccStandbyFsCfgStatus_Object = MibScalar
accStandbyFsCfgStatus = _AccStandbyFsCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 7),
    _AccStandbyFsCfgStatus_Type()
)
accStandbyFsCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbyFsCfgStatus.setStatus("mandatory")
_AccStandbyFsLoadFtkFile_Type = DisplayString
_AccStandbyFsLoadFtkFile_Object = MibScalar
accStandbyFsLoadFtkFile = _AccStandbyFsLoadFtkFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 8),
    _AccStandbyFsLoadFtkFile_Type()
)
accStandbyFsLoadFtkFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbyFsLoadFtkFile.setStatus("mandatory")
_AccStandbyFsLoadAplFile_Type = DisplayString
_AccStandbyFsLoadAplFile_Object = MibScalar
accStandbyFsLoadAplFile = _AccStandbyFsLoadAplFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 9),
    _AccStandbyFsLoadAplFile_Type()
)
accStandbyFsLoadAplFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbyFsLoadAplFile.setStatus("mandatory")
_AccStandbyFsLoadDiaFile_Type = DisplayString
_AccStandbyFsLoadDiaFile_Object = MibScalar
accStandbyFsLoadDiaFile = _AccStandbyFsLoadDiaFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 10),
    _AccStandbyFsLoadDiaFile_Type()
)
accStandbyFsLoadDiaFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbyFsLoadDiaFile.setStatus("mandatory")
_AccStandbySysHwVers_Type = DisplayString
_AccStandbySysHwVers_Object = MibScalar
accStandbySysHwVers = _AccStandbySysHwVers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 14, 11),
    _AccStandbySysHwVers_Type()
)
accStandbySysHwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStandbySysHwVers.setStatus("mandatory")
_AccSyslogTable_Object = MibTable
accSyslogTable = _AccSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 15)
)
if mibBuilder.loadTexts:
    accSyslogTable.setStatus("mandatory")
_AccSyslogEntry_Object = MibTableRow
accSyslogEntry = _AccSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 15, 1)
)
accSyslogEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accSyslogAddr"),
)
if mibBuilder.loadTexts:
    accSyslogEntry.setStatus("mandatory")
_AccSyslogAddr_Type = IpAddress
_AccSyslogAddr_Object = MibTableColumn
accSyslogAddr = _AccSyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 15, 1, 1),
    _AccSyslogAddr_Type()
)
accSyslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSyslogAddr.setStatus("mandatory")


class _AccSyslogSeverity_Type(Integer32):
    """Custom type accSyslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccSyslogSeverity_Type.__name__ = "Integer32"
_AccSyslogSeverity_Object = MibTableColumn
accSyslogSeverity = _AccSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 15, 1, 2),
    _AccSyslogSeverity_Type()
)
accSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSyslogSeverity.setStatus("mandatory")


class _AccSyslogFacility_Type(Integer32):
    """Custom type accSyslogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AccSyslogFacility_Type.__name__ = "Integer32"
_AccSyslogFacility_Object = MibTableColumn
accSyslogFacility = _AccSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 15, 1, 3),
    _AccSyslogFacility_Type()
)
accSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSyslogFacility.setStatus("mandatory")
_AccIcpTraps_ObjectIdentity = ObjectIdentity
accIcpTraps = _AccIcpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 16)
)
_AccIcpTrapMsg_Type = DisplayString
_AccIcpTrapMsg_Object = MibScalar
accIcpTrapMsg = _AccIcpTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 16, 1),
    _AccIcpTrapMsg_Type()
)
accIcpTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIcpTrapMsg.setStatus("mandatory")


class _AccTrapSequencingStatus_Type(Integer32):
    """Custom type accTrapSequencingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AccTrapSequencingStatus_Type.__name__ = "Integer32"
_AccTrapSequencingStatus_Object = MibScalar
accTrapSequencingStatus = _AccTrapSequencingStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 18),
    _AccTrapSequencingStatus_Type()
)
accTrapSequencingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrapSequencingStatus.setStatus("mandatory")
_AccSystemServiceTable_Object = MibTable
accSystemServiceTable = _AccSystemServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    accSystemServiceTable.setStatus("mandatory")
_AccSystemServiceEntry_Object = MibTableRow
accSystemServiceEntry = _AccSystemServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 26, 1)
)
accSystemServiceEntry.setIndexNames(
    (0, "ACC-SYSTEM", "accSystemService"),
)
if mibBuilder.loadTexts:
    accSystemServiceEntry.setStatus("mandatory")


class _AccSystemService_Type(Integer32):
    """Custom type accSystemService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("http", 3),
          ("telnet", 1),
          ("tftp", 2))
    )


_AccSystemService_Type.__name__ = "Integer32"
_AccSystemService_Object = MibTableColumn
accSystemService = _AccSystemService_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 26, 1, 1),
    _AccSystemService_Type()
)
accSystemService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemService.setStatus("mandatory")
_AccSystemPort_Type = Integer32
_AccSystemPort_Object = MibTableColumn
accSystemPort = _AccSystemPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 26, 1, 2),
    _AccSystemPort_Type()
)
accSystemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSystemPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accIcpInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 16, 0, 1)
)
accIcpInfoTrap.setObjects(
      *(("ACC-SYSTEM", "accIcpTrapMsg"),
        ("ACC-SYSTEM", "accSlvConfCPUID"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accIcpInfoTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SYSTEM",
    **{"accSystem": accSystem,
       "accSysInfo": accSysInfo,
       "accUnitName": accUnitName,
       "accRomId": accRomId,
       "accSwVersion": accSwVersion,
       "accReset": accReset,
       "accMemStatTable": accMemStatTable,
       "accMemStatEntry": accMemStatEntry,
       "accMemBlkEntSize": accMemBlkEntSize,
       "accMemBlkEntTotal": accMemBlkEntTotal,
       "accMemBlkEntMax": accMemBlkEntMax,
       "accMemBlkEntInUse": accMemBlkEntInUse,
       "accMemBlkEntFails": accMemBlkEntFails,
       "accMemBlkEntType": accMemBlkEntType,
       "accMemBlkEntAllocs": accMemBlkEntAllocs,
       "accMemBlkEntInitial": accMemBlkEntInitial,
       "pysmiFakeCol4": pysmiFakeCol4,
       "accNvm": accNvm,
       "accNvmTotalBlks": accNvmTotalBlks,
       "accNvmBlkSize": accNvmBlkSize,
       "accNvmDirSize": accNvmDirSize,
       "accNvmFreeBlks": accNvmFreeBlks,
       "accNvmFileNumber": accNvmFileNumber,
       "accNvmFileName": accNvmFileName,
       "accNvmFileSize": accNvmFileSize,
       "accSysConfigInfo": accSysConfigInfo,
       "accConfiguration": accConfiguration,
       "accConfigurationStatus": accConfigurationStatus,
       "accScriptHalt": accScriptHalt,
       "accScriptCont": accScriptCont,
       "accScriptContServer": accScriptContServer,
       "accScriptContFile": accScriptContFile,
       "accSysUpgradeCmd": accSysUpgradeCmd,
       "accSysHWType": accSysHWType,
       "accSysProcType": accSysProcType,
       "accSysLocalRam": accSysLocalRam,
       "accSysGlobalRam": accSysGlobalRam,
       "accSysPowerSupply": accSysPowerSupply,
       "accMemPoolTable": accMemPoolTable,
       "accMemPoolEntry": accMemPoolEntry,
       "accMemPoolName": accMemPoolName,
       "accMemPoolMaximum": accMemPoolMaximum,
       "accMemPoolBytes": accMemPoolBytes,
       "accMemPoolFrags": accMemPoolFrags,
       "accMemPoolAlign": accMemPoolAlign,
       "accMemPoolAllocs": accMemPoolAllocs,
       "accMemPoolFails": accMemPoolFails,
       "pysmiFakeCol8": pysmiFakeCol8,
       "accMemAddDblk": accMemAddDblk,
       "accSlvConfTable": accSlvConfTable,
       "accSlvConfEntry": accSlvConfEntry,
       "accSlvConfCPUIndex": accSlvConfCPUIndex,
       "accSlvConfCPUID": accSlvConfCPUID,
       "accSlvConfSysDesc": accSlvConfSysDesc,
       "accSlvConfSWVers": accSlvConfSWVers,
       "accSlvConfProcType": accSlvConfProcType,
       "accSlvConfLocalRam": accSlvConfLocalRam,
       "accSlvConfGlobalRam": accSlvConfGlobalRam,
       "accSlvMemBlkTable": accSlvMemBlkTable,
       "accSlvMemBlkEntry": accSlvMemBlkEntry,
       "accSlvMemCPUID": accSlvMemCPUID,
       "accSlvMemBlkEntSize": accSlvMemBlkEntSize,
       "accSlvMemBlkEntTotal": accSlvMemBlkEntTotal,
       "accSlvMemBlkEntMax": accSlvMemBlkEntMax,
       "accSlvMemBlkEntInUse": accSlvMemBlkEntInUse,
       "accSlvMemBlkEntFails": accSlvMemBlkEntFails,
       "accSlvMemBlkEntType": accSlvMemBlkEntType,
       "accSlvMemBlkEntAllocs": accSlvMemBlkEntAllocs,
       "pysmiFakeCol9": pysmiFakeCol9,
       "accSlvMemPool": accSlvMemPool,
       "accSlvMemPoolTable": accSlvMemPoolTable,
       "accSlvMemPoolEntry": accSlvMemPoolEntry,
       "accSlvMemPoolCPUID": accSlvMemPoolCPUID,
       "accSlvMemPoolName": accSlvMemPoolName,
       "accSlvMemPoolMaximum": accSlvMemPoolMaximum,
       "accSlvMemPoolBytes": accSlvMemPoolBytes,
       "accSlvMemPoolFrags": accSlvMemPoolFrags,
       "accSlvMemPoolAlign": accSlvMemPoolAlign,
       "accSlvMemPoolAllocs": accSlvMemPoolAllocs,
       "accSlvMemPoolFails": accSlvMemPoolFails,
       "pysmiFakeCol11": pysmiFakeCol11,
       "pysmiFakeCol10": pysmiFakeCol10,
       "accSlvSysTable": accSlvSysTable,
       "accSlvSysEntry": accSlvSysEntry,
       "accSlvSysUpTime": accSlvSysUpTime,
       "accSlvSysCpuAvgShort": accSlvSysCpuAvgShort,
       "accSlvSysCpuAvgLong": accSlvSysCpuAvgLong,
       "pysmiFakeCol12": pysmiFakeCol12,
       "accMem": accMem,
       "accMemDblkIncTable": accMemDblkIncTable,
       "accMemDblkIncEntry": accMemDblkIncEntry,
       "accMemDblkIndex": accMemDblkIndex,
       "accMemDblkSize": accMemDblkSize,
       "accMemDblkIncrement": accMemDblkIncrement,
       "accOpt": accOpt,
       "accMemEMEStatus": accMemEMEStatus,
       "accMemEMEMaxReclMem": accMemEMEMaxReclMem,
       "accMemEMECurReclMem": accMemEMECurReclMem,
       "accMemOptTable": accMemOptTable,
       "accMemOptEntry": accMemOptEntry,
       "accMemOptimiserFeature": accMemOptimiserFeature,
       "accMemOptimiserMemory": accMemOptimiserMemory,
       "accMemOptimiserPref": accMemOptimiserPref,
       "accMemOptimiserStatus": accMemOptimiserStatus,
       "accMacro": accMacro,
       "accMacroExecute": accMacroExecute,
       "accSwRegistrationKey": accSwRegistrationKey,
       "accMACAddr": accMACAddr,
       "accSysMACAddrUser": accSysMACAddrUser,
       "accSysMessage": accSysMessage,
       "accSysMsgInfo": accSysMsgInfo,
       "accSysMsgLevel": accSysMsgLevel,
       "accWinDefLenNetman": accWinDefLenNetman,
       "accWinDefLenPublic": accWinDefLenPublic,
       "accWinDefWidNetman": accWinDefWidNetman,
       "accWinDefWidPublic": accWinDefWidPublic,
       "accUserInfo": accUserInfo,
       "accUserTrapMsgEntry": accUserTrapMsgEntry,
       "accVirtualPort": accVirtualPort,
       "accVirtualPortGeneral": accVirtualPortGeneral,
       "accVirtualPortCount": accVirtualPortCount,
       "accVirtualPortXotCount": accVirtualPortXotCount,
       "accSystemGracefulShutdown": accSystemGracefulShutdown,
       "accSystemGracefulShutdownState": accSystemGracefulShutdownState,
       "accSystemGracefulShutdownTO": accSystemGracefulShutdownTO,
       "accSystemAuthGeneral": accSystemAuthGeneral,
       "accSystemAuthMode": accSystemAuthMode,
       "accSystemAuthAccessPart": accSystemAuthAccessPart,
       "accSystemAccess": accSystemAccess,
       "accPscopeEnable": accPscopeEnable,
       "accDBscopeCntl": accDBscopeCntl,
       "accSessionCtrl": accSessionCtrl,
       "accLogin": accLogin,
       "accLogout": accLogout,
       "accLoginTimeout": accLoginTimeout,
       "accTrapTable": accTrapTable,
       "accTrapEntry": accTrapEntry,
       "accTrapAddr": accTrapAddr,
       "accTrapSeverity": accTrapSeverity,
       "accClock": accClock,
       "accDate": accDate,
       "accUToffset": accUToffset,
       "accSysBootTime": accSysBootTime,
       "accSysCpuAvgShort": accSysCpuAvgShort,
       "accSysCpuAvgLong": accSysCpuAvgLong,
       "accSysDataSwitchStatus": accSysDataSwitchStatus,
       "accSysLastConfig": accSysLastConfig,
       "accDateY2K": accDateY2K,
       "accSysBootTimeY2K": accSysBootTimeY2K,
       "accDay": accDay,
       "accAccessTable": accAccessTable,
       "accAccessEntry": accAccessEntry,
       "accAccessCmty": accAccessCmty,
       "accAccessAddr": accAccessAddr,
       "accAccessNetMask": accAccessNetMask,
       "accAccessUdpPort": accAccessUdpPort,
       "accReload": accReload,
       "accIfNames": accIfNames,
       "accIfNumNames": accIfNumNames,
       "accIfNameTable": accIfNameTable,
       "accIfNameEntry": accIfNameEntry,
       "accIfNameIndex": accIfNameIndex,
       "accIfName": accIfName,
       "accIfNameDefault": accIfNameDefault,
       "accIfGroupTable": accIfGroupTable,
       "accIfGroupEntry": accIfGroupEntry,
       "accIFGroupIndex": accIFGroupIndex,
       "accIFGroupName": accIFGroupName,
       "accIFGroupType": accIFGroupType,
       "accIFGroupIndexBase": accIFGroupIndexBase,
       "accIFGroupIndexMax": accIFGroupIndexMax,
       "accIFGroupNameDefault": accIFGroupNameDefault,
       "accTrapLog": accTrapLog,
       "accTrapLogLevel": accTrapLogLevel,
       "accTrapLogSaveAction": accTrapLogSaveAction,
       "accTrapLogBufSize": accTrapLogBufSize,
       "accTrapLogTable": accTrapLogTable,
       "accTrapLogEntry": accTrapLogEntry,
       "accTrapLogTblTime": accTrapLogTblTime,
       "accTrapLogTblType": accTrapLogTblType,
       "accTrapLogTblLevel": accTrapLogTblLevel,
       "accTrapLogTblData": accTrapLogTblData,
       "accTrapLogSeqNum": accTrapLogSeqNum,
       "accTrapLogSeverityType": accTrapLogSeverityType,
       "accTrapLogEnterpriseOID": accTrapLogEnterpriseOID,
       "accSpecificTrapNum": accSpecificTrapNum,
       "pysmiFakeCol5": pysmiFakeCol5,
       "accTrapLogSumTable": accTrapLogSumTable,
       "accTrapLogSumEntry": accTrapLogSumEntry,
       "accTrapLogSumTime": accTrapLogSumTime,
       "accTrapLogSumType": accTrapLogSumType,
       "accTrapLogSumData": accTrapLogSumData,
       "pysmiFakeCol6": pysmiFakeCol6,
       "accSeepTable": accSeepTable,
       "accSeepEntry": accSeepEntry,
       "accSeepEntrySlot": accSeepEntrySlot,
       "accSeepEntryType": accSeepEntryType,
       "accSeepEntrySerial": accSeepEntrySerial,
       "accSeepEntryAssembly": accSeepEntryAssembly,
       "accSeepEntryRev": accSeepEntryRev,
       "accSeepEntryDate": accSeepEntryDate,
       "pysmiFakeCol7": pysmiFakeCol7,
       "accStandbyInfo": accStandbyInfo,
       "accStandbySysDescr": accStandbySysDescr,
       "accStandbySoftwareVersion": accStandbySoftwareVersion,
       "accStandbySysProcType": accStandbySysProcType,
       "accStandbySysLocalRam": accStandbySysLocalRam,
       "accStandbySysGlobalRam": accStandbySysGlobalRam,
       "accStandbyFsVolStatus": accStandbyFsVolStatus,
       "accStandbyFsCfgStatus": accStandbyFsCfgStatus,
       "accStandbyFsLoadFtkFile": accStandbyFsLoadFtkFile,
       "accStandbyFsLoadAplFile": accStandbyFsLoadAplFile,
       "accStandbyFsLoadDiaFile": accStandbyFsLoadDiaFile,
       "accStandbySysHwVers": accStandbySysHwVers,
       "accSyslogTable": accSyslogTable,
       "accSyslogEntry": accSyslogEntry,
       "accSyslogAddr": accSyslogAddr,
       "accSyslogSeverity": accSyslogSeverity,
       "accSyslogFacility": accSyslogFacility,
       "accIcpTraps": accIcpTraps,
       "accIcpInfoTrap": accIcpInfoTrap,
       "accIcpTrapMsg": accIcpTrapMsg,
       "accTrapSequencingStatus": accTrapSequencingStatus,
       "accSystemServiceTable": accSystemServiceTable,
       "accSystemServiceEntry": accSystemServiceEntry,
       "accSystemService": accSystemService,
       "accSystemPort": accSystemPort}
)
