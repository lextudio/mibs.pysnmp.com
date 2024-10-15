# SNMP MIB module (ACC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-MIB
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(egpNeighAddr,
 ipRouteDest) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "egpNeighAddr",
    "ipRouteDest")

(atportIndex,) = mibBuilder.importSymbols(
    "RFC1243-MIB",
    "atportIndex")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class SmdsAddress(OctetString):
    """Custom type SmdsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class CallAddress(DisplayString):
    """Custom type CallAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )





class BackupPort(Integer32):
    """Custom type BackupPort based on Integer32"""




class PhysicalPort(Integer32):
    """Custom type PhysicalPort based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Acc_ObjectIdentity = ObjectIdentity
acc = _Acc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5)
)
_AccSBAR_ObjectIdentity = ObjectIdentity
accSBAR = _AccSBAR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1)
)
_AccBRG_ObjectIdentity = ObjectIdentity
accBRG = _AccBRG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1)
)
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
_AccMemStatTbl_Object = MibTableRow
accMemStatTbl = _AccMemStatTbl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5)
)
accMemStatTbl.setIndexNames(
    (0, "ACC-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accMemStatTbl.setStatus("mandatory")
_AccMemBlkEntSize_Type = Integer32
_AccMemBlkEntSize_Object = MibTableColumn
accMemBlkEntSize = _AccMemBlkEntSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 1),
    _AccMemBlkEntSize_Type()
)
accMemBlkEntSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntSize.setStatus("mandatory")
_AccMemBlkEntTotal_Type = Integer32
_AccMemBlkEntTotal_Object = MibTableColumn
accMemBlkEntTotal = _AccMemBlkEntTotal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 2),
    _AccMemBlkEntTotal_Type()
)
accMemBlkEntTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntTotal.setStatus("mandatory")
_AccMemBlkEntMax_Type = Gauge32
_AccMemBlkEntMax_Object = MibTableColumn
accMemBlkEntMax = _AccMemBlkEntMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 3),
    _AccMemBlkEntMax_Type()
)
accMemBlkEntMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntMax.setStatus("mandatory")
_AccMemBlkEntInUse_Type = Gauge32
_AccMemBlkEntInUse_Object = MibTableColumn
accMemBlkEntInUse = _AccMemBlkEntInUse_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 4),
    _AccMemBlkEntInUse_Type()
)
accMemBlkEntInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntInUse.setStatus("mandatory")
_AccMemBlkEntFails_Type = Counter32
_AccMemBlkEntFails_Object = MibTableColumn
accMemBlkEntFails = _AccMemBlkEntFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 5),
    _AccMemBlkEntFails_Type()
)
accMemBlkEntFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntFails.setStatus("mandatory")
_AccMemBlkEntType_Type = Integer32
_AccMemBlkEntType_Object = MibTableColumn
accMemBlkEntType = _AccMemBlkEntType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 6),
    _AccMemBlkEntType_Type()
)
accMemBlkEntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntType.setStatus("mandatory")
_AccMemBlkEntAllocs_Type = Counter32
_AccMemBlkEntAllocs_Object = MibTableColumn
accMemBlkEntAllocs = _AccMemBlkEntAllocs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 7),
    _AccMemBlkEntAllocs_Type()
)
accMemBlkEntAllocs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMemBlkEntAllocs.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 5, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
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
_AccGifnoc_Type = OctetString
_AccGifnoc_Object = MibScalar
accGifnoc = _AccGifnoc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 10),
    _AccGifnoc_Type()
)
accGifnoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accGifnoc.setStatus("mandatory")
_AccSysHWType_Type = Integer32
_AccSysHWType_Object = MibScalar
accSysHWType = _AccSysHWType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 1, 1, 11),
    _AccSysHWType_Type()
)
accSysHWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSysHWType.setStatus("mandatory")
_AccSysProcType_Type = Integer32
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
    (0, "ACC-MIB", "accMemPoolName"),
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
    (0, "ACC-MIB", "accTrapAddr"),
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
    accDate.setStatus("mandatory")
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
    accSysBootTime.setStatus("mandatory")
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
    (0, "ACC-MIB", "accAccessAddr"),
    (0, "ACC-MIB", "accAccessNetMask"),
    (0, "ACC-MIB", "accAccessUdpPort"),
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
    (0, "ACC-MIB", "accIfNameIndex"),
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
    (0, "ACC-MIB", "accIFGroupIndex"),
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
_AccStp_ObjectIdentity = ObjectIdentity
accStp = _AccStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2)
)


class _AccStpPriority_Type(Integer32):
    """Custom type accStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccStpPriority_Type.__name__ = "Integer32"
_AccStpPriority_Object = MibScalar
accStpPriority = _AccStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 1),
    _AccStpPriority_Type()
)
accStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpPriority.setStatus("mandatory")
_AccStpId_Type = OctetString
_AccStpId_Object = MibScalar
accStpId = _AccStpId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 2),
    _AccStpId_Type()
)
accStpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpId.setStatus("mandatory")
_AccStpBrAddr_Type = OctetString
_AccStpBrAddr_Object = MibScalar
accStpBrAddr = _AccStpBrAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 3),
    _AccStpBrAddr_Type()
)
accStpBrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpBrAddr.setStatus("mandatory")


class _AccStpMode_Type(Integer32):
    """Custom type accStpMode based on Integer32"""
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


_AccStpMode_Type.__name__ = "Integer32"
_AccStpMode_Object = MibScalar
accStpMode = _AccStpMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 4),
    _AccStpMode_Type()
)
accStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMode.setStatus("mandatory")
_AccStpFilterTime_Type = TimeTicks
_AccStpFilterTime_Object = MibScalar
accStpFilterTime = _AccStpFilterTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 5),
    _AccStpFilterTime_Type()
)
accStpFilterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpFilterTime.setStatus("mandatory")
_AccStpMcastAddr_Type = OctetString
_AccStpMcastAddr_Object = MibScalar
accStpMcastAddr = _AccStpMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 6),
    _AccStpMcastAddr_Type()
)
accStpMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMcastAddr.setStatus("mandatory")


class _AccStpTopChangeDet_Type(Integer32):
    """Custom type accStpTopChangeDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccStpTopChangeDet_Type.__name__ = "Integer32"
_AccStpTopChangeDet_Object = MibScalar
accStpTopChangeDet = _AccStpTopChangeDet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 7),
    _AccStpTopChangeDet_Type()
)
accStpTopChangeDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeDet.setStatus("mandatory")


class _AccStpTopChange_Type(Integer32):
    """Custom type accStpTopChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccStpTopChange_Type.__name__ = "Integer32"
_AccStpTopChange_Object = MibScalar
accStpTopChange = _AccStpTopChange_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 8),
    _AccStpTopChange_Type()
)
accStpTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChange.setStatus("mandatory")
_AccStpTopChangeTimer_Type = TimeTicks
_AccStpTopChangeTimer_Object = MibScalar
accStpTopChangeTimer = _AccStpTopChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 9),
    _AccStpTopChangeTimer_Type()
)
accStpTopChangeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeTimer.setStatus("mandatory")
_AccStpDesRoot_Type = OctetString
_AccStpDesRoot_Object = MibScalar
accStpDesRoot = _AccStpDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 10),
    _AccStpDesRoot_Type()
)
accStpDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpDesRoot.setStatus("mandatory")
_AccStpRootPathCost_Type = Integer32
_AccStpRootPathCost_Object = MibScalar
accStpRootPathCost = _AccStpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 11),
    _AccStpRootPathCost_Type()
)
accStpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpRootPathCost.setStatus("mandatory")
_AccStpRootPort_Type = OctetString
_AccStpRootPort_Object = MibScalar
accStpRootPort = _AccStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 12),
    _AccStpRootPort_Type()
)
accStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpRootPort.setStatus("mandatory")


class _AccStpMaxAge_Type(Integer32):
    """Custom type accStpMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_AccStpMaxAge_Type.__name__ = "Integer32"
_AccStpMaxAge_Object = MibScalar
accStpMaxAge = _AccStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 13),
    _AccStpMaxAge_Type()
)
accStpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMaxAge.setStatus("mandatory")


class _AccStpHelloTime_Type(Integer32):
    """Custom type accStpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1800),
    )


_AccStpHelloTime_Type.__name__ = "Integer32"
_AccStpHelloTime_Object = MibScalar
accStpHelloTime = _AccStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 14),
    _AccStpHelloTime_Type()
)
accStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpHelloTime.setStatus("mandatory")


class _AccStpForwardDelay_Type(Integer32):
    """Custom type accStpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AccStpForwardDelay_Type.__name__ = "Integer32"
_AccStpForwardDelay_Object = MibScalar
accStpForwardDelay = _AccStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 15),
    _AccStpForwardDelay_Type()
)
accStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpForwardDelay.setStatus("mandatory")
_AccStpUpTime_Type = TimeTicks
_AccStpUpTime_Object = MibScalar
accStpUpTime = _AccStpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 16),
    _AccStpUpTime_Type()
)
accStpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpUpTime.setStatus("mandatory")
_AccStpTopChangeCnts_Type = Counter32
_AccStpTopChangeCnts_Object = MibScalar
accStpTopChangeCnts = _AccStpTopChangeCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 17),
    _AccStpTopChangeCnts_Type()
)
accStpTopChangeCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeCnts.setStatus("mandatory")
_AccBrPort_ObjectIdentity = ObjectIdentity
accBrPort = _AccBrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3)
)
_AccBrPortInfo_ObjectIdentity = ObjectIdentity
accBrPortInfo = _AccBrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1)
)
_AccBrPortStats_ObjectIdentity = ObjectIdentity
accBrPortStats = _AccBrPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1)
)
_AccBrPortInNUcastPkts_Type = Counter32
_AccBrPortInNUcastPkts_Object = MibScalar
accBrPortInNUcastPkts = _AccBrPortInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 1),
    _AccBrPortInNUcastPkts_Type()
)
accBrPortInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInNUcastPkts.setStatus("mandatory")
_AccBrPortInUcastPkts_Type = Counter32
_AccBrPortInUcastPkts_Object = MibScalar
accBrPortInUcastPkts = _AccBrPortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 2),
    _AccBrPortInUcastPkts_Type()
)
accBrPortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInUcastPkts.setStatus("mandatory")
_AccBrPortInDupPkts_Type = Counter32
_AccBrPortInDupPkts_Object = MibScalar
accBrPortInDupPkts = _AccBrPortInDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 3),
    _AccBrPortInDupPkts_Type()
)
accBrPortInDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInDupPkts.setStatus("mandatory")
_AccBrPortOutNUcastPkts_Type = Counter32
_AccBrPortOutNUcastPkts_Object = MibScalar
accBrPortOutNUcastPkts = _AccBrPortOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 4),
    _AccBrPortOutNUcastPkts_Type()
)
accBrPortOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutNUcastPkts.setStatus("mandatory")
_AccBrPortOutUcastPkts_Type = Counter32
_AccBrPortOutUcastPkts_Object = MibScalar
accBrPortOutUcastPkts = _AccBrPortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 5),
    _AccBrPortOutUcastPkts_Type()
)
accBrPortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutUcastPkts.setStatus("mandatory")
_AccBrPortStpInPkts_Type = Counter32
_AccBrPortStpInPkts_Object = MibScalar
accBrPortStpInPkts = _AccBrPortStpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 6),
    _AccBrPortStpInPkts_Type()
)
accBrPortStpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpInPkts.setStatus("mandatory")
_AccBrPortStpOutPkts_Type = Counter32
_AccBrPortStpOutPkts_Object = MibScalar
accBrPortStpOutPkts = _AccBrPortStpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 7),
    _AccBrPortStpOutPkts_Type()
)
accBrPortStpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpOutPkts.setStatus("mandatory")
_AccBrPortOutDelayDiscPkts_Type = Counter32
_AccBrPortOutDelayDiscPkts_Object = MibScalar
accBrPortOutDelayDiscPkts = _AccBrPortOutDelayDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 8),
    _AccBrPortOutDelayDiscPkts_Type()
)
accBrPortOutDelayDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutDelayDiscPkts.setStatus("mandatory")
_AccBrPortOutPrioDiscPkts_Type = Counter32
_AccBrPortOutPrioDiscPkts_Object = MibScalar
accBrPortOutPrioDiscPkts = _AccBrPortOutPrioDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 9),
    _AccBrPortOutPrioDiscPkts_Type()
)
accBrPortOutPrioDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutPrioDiscPkts.setStatus("mandatory")
_AccBrPortOutQLen_Type = Gauge32
_AccBrPortOutQLen_Object = MibScalar
accBrPortOutQLen = _AccBrPortOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 10),
    _AccBrPortOutQLen_Type()
)
accBrPortOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutQLen.setStatus("mandatory")
_AccBrPortInDiscPkts_Type = Counter32
_AccBrPortInDiscPkts_Object = MibScalar
accBrPortInDiscPkts = _AccBrPortInDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 11),
    _AccBrPortInDiscPkts_Type()
)
accBrPortInDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInDiscPkts.setStatus("mandatory")


class _AccBrPortStpPriority_Type(Integer32):
    """Custom type accBrPortStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBrPortStpPriority_Type.__name__ = "Integer32"
_AccBrPortStpPriority_Object = MibScalar
accBrPortStpPriority = _AccBrPortStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 2),
    _AccBrPortStpPriority_Type()
)
accBrPortStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortStpPriority.setStatus("mandatory")
_AccBrPortId_Type = OctetString
_AccBrPortId_Object = MibScalar
accBrPortId = _AccBrPortId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 3),
    _AccBrPortId_Type()
)
accBrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortId.setStatus("mandatory")


class _AccBrPortState_Type(Integer32):
    """Custom type accBrPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccBrPortState_Type.__name__ = "Integer32"
_AccBrPortState_Object = MibScalar
accBrPortState = _AccBrPortState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 5),
    _AccBrPortState_Type()
)
accBrPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortState.setStatus("mandatory")


class _AccBrPortStpPathCost_Type(Integer32):
    """Custom type accBrPortStpPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrPortStpPathCost_Type.__name__ = "Integer32"
_AccBrPortStpPathCost_Object = MibScalar
accBrPortStpPathCost = _AccBrPortStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 6),
    _AccBrPortStpPathCost_Type()
)
accBrPortStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortStpPathCost.setStatus("mandatory")
_AccBrPortStpDesRoot_Type = OctetString
_AccBrPortStpDesRoot_Object = MibScalar
accBrPortStpDesRoot = _AccBrPortStpDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 7),
    _AccBrPortStpDesRoot_Type()
)
accBrPortStpDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesRoot.setStatus("mandatory")


class _AccBrPortStpDesCost_Type(Integer32):
    """Custom type accBrPortStpDesCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrPortStpDesCost_Type.__name__ = "Integer32"
_AccBrPortStpDesCost_Object = MibScalar
accBrPortStpDesCost = _AccBrPortStpDesCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 8),
    _AccBrPortStpDesCost_Type()
)
accBrPortStpDesCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesCost.setStatus("mandatory")
_AccBrPortStpDesBridge_Type = OctetString
_AccBrPortStpDesBridge_Object = MibScalar
accBrPortStpDesBridge = _AccBrPortStpDesBridge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 9),
    _AccBrPortStpDesBridge_Type()
)
accBrPortStpDesBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesBridge.setStatus("mandatory")
_AccBrPortStpDesPort_Type = OctetString
_AccBrPortStpDesPort_Object = MibScalar
accBrPortStpDesPort = _AccBrPortStpDesPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 10),
    _AccBrPortStpDesPort_Type()
)
accBrPortStpDesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesPort.setStatus("mandatory")


class _AccBrPortAdminStatus_Type(Integer32):
    """Custom type accBrPortAdminStatus based on Integer32"""
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


_AccBrPortAdminStatus_Type.__name__ = "Integer32"
_AccBrPortAdminStatus_Object = MibScalar
accBrPortAdminStatus = _AccBrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 11),
    _AccBrPortAdminStatus_Type()
)
accBrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortAdminStatus.setStatus("mandatory")
_AccBrPortLine_Type = Integer32
_AccBrPortLine_Object = MibScalar
accBrPortLine = _AccBrPortLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 12),
    _AccBrPortLine_Type()
)
accBrPortLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortLine.setStatus("mandatory")


class _AccBrPortProtocol_Type(Integer32):
    """Custom type accBrPortProtocol based on Integer32"""
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
        *(("enet", 1),
          ("ffr", 4),
          ("lapb", 3),
          ("other", 5),
          ("x25", 2))
    )


_AccBrPortProtocol_Type.__name__ = "Integer32"
_AccBrPortProtocol_Object = MibScalar
accBrPortProtocol = _AccBrPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 13),
    _AccBrPortProtocol_Type()
)
accBrPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortProtocol.setStatus("mandatory")
_AccBrPortFrDlci_Type = Integer32
_AccBrPortFrDlci_Object = MibScalar
accBrPortFrDlci = _AccBrPortFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 14),
    _AccBrPortFrDlci_Type()
)
accBrPortFrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortFrDlci.setStatus("mandatory")
_AccBrPortIndex_Type = Integer32
_AccBrPortIndex_Object = MibScalar
accBrPortIndex = _AccBrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 15),
    _AccBrPortIndex_Type()
)
accBrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortIndex.setStatus("mandatory")


class _AccBrPortXBridgeStatus_Type(Integer32):
    """Custom type accBrPortXBridgeStatus based on Integer32"""
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


_AccBrPortXBridgeStatus_Type.__name__ = "Integer32"
_AccBrPortXBridgeStatus_Object = MibScalar
accBrPortXBridgeStatus = _AccBrPortXBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 16),
    _AccBrPortXBridgeStatus_Type()
)
accBrPortXBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortXBridgeStatus.setStatus("mandatory")
_AccBridge_ObjectIdentity = ObjectIdentity
accBridge = _AccBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4)
)


class _AccBrFdbTimeout_Type(Integer32):
    """Custom type accBrFdbTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AccBrFdbTimeout_Type.__name__ = "Integer32"
_AccBrFdbTimeout_Object = MibScalar
accBrFdbTimeout = _AccBrFdbTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 1),
    _AccBrFdbTimeout_Type()
)
accBrFdbTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbTimeout.setStatus("mandatory")


class _AccBrFdbLearnMode_Type(Integer32):
    """Custom type accBrFdbLearnMode based on Integer32"""
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


_AccBrFdbLearnMode_Type.__name__ = "Integer32"
_AccBrFdbLearnMode_Object = MibScalar
accBrFdbLearnMode = _AccBrFdbLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 2),
    _AccBrFdbLearnMode_Type()
)
accBrFdbLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbLearnMode.setStatus("mandatory")
_AccBrFdbRamCurrSize_Type = Integer32
_AccBrFdbRamCurrSize_Object = MibScalar
accBrFdbRamCurrSize = _AccBrFdbRamCurrSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 3),
    _AccBrFdbRamCurrSize_Type()
)
accBrFdbRamCurrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbRamCurrSize.setStatus("mandatory")


class _AccBrFdbRamMaxSize_Type(Integer32):
    """Custom type accBrFdbRamMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024),
    )


_AccBrFdbRamMaxSize_Type.__name__ = "Integer32"
_AccBrFdbRamMaxSize_Object = MibScalar
accBrFdbRamMaxSize = _AccBrFdbRamMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 5),
    _AccBrFdbRamMaxSize_Type()
)
accBrFdbRamMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbRamMaxSize.setStatus("mandatory")
_AccBrFdbNvmMaxSize_Type = Integer32
_AccBrFdbNvmMaxSize_Object = MibScalar
accBrFdbNvmMaxSize = _AccBrFdbNvmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 6),
    _AccBrFdbNvmMaxSize_Type()
)
accBrFdbNvmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbNvmMaxSize.setStatus("mandatory")
_AccBrFdbTable_Object = MibTable
accBrFdbTable = _AccBrFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    accBrFdbTable.setStatus("mandatory")
_AccBrFdbEntry_Object = MibTableRow
accBrFdbEntry = _AccBrFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1)
)
accBrFdbEntry.setIndexNames(
    (0, "ACC-MIB", "accBrFdbEntMacAddr"),
)
if mibBuilder.loadTexts:
    accBrFdbEntry.setStatus("mandatory")
_AccBrFdbEntMacAddr_Type = OctetString
_AccBrFdbEntMacAddr_Object = MibTableColumn
accBrFdbEntMacAddr = _AccBrFdbEntMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 1),
    _AccBrFdbEntMacAddr_Type()
)
accBrFdbEntMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntMacAddr.setStatus("mandatory")


class _AccBrFdbEntDisp_Type(Integer32):
    """Custom type accBrFdbEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AccBrFdbEntDisp_Type.__name__ = "Integer32"
_AccBrFdbEntDisp_Object = MibTableColumn
accBrFdbEntDisp = _AccBrFdbEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 2),
    _AccBrFdbEntDisp_Type()
)
accBrFdbEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntDisp.setStatus("mandatory")
_AccBrFdbEntPort_Type = Integer32
_AccBrFdbEntPort_Object = MibTableColumn
accBrFdbEntPort = _AccBrFdbEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 3),
    _AccBrFdbEntPort_Type()
)
accBrFdbEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFdbEntPort.setStatus("mandatory")
_AccBrFdbEntTimer_Type = Integer32
_AccBrFdbEntTimer_Object = MibTableColumn
accBrFdbEntTimer = _AccBrFdbEntTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 7, 1, 4),
    _AccBrFdbEntTimer_Type()
)
accBrFdbEntTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFdbEntTimer.setStatus("mandatory")
_AccBrFpTable_Object = MibTable
accBrFpTable = _AccBrFpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    accBrFpTable.setStatus("mandatory")
_AccBrFpEntry_Object = MibTableRow
accBrFpEntry = _AccBrFpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1)
)
accBrFpEntry.setIndexNames(
    (0, "ACC-MIB", "accBrFpIndex"),
)
if mibBuilder.loadTexts:
    accBrFpEntry.setStatus("mandatory")
_AccBrFpIndex_Type = Integer32
_AccBrFpIndex_Object = MibTableColumn
accBrFpIndex = _AccBrFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 1),
    _AccBrFpIndex_Type()
)
accBrFpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpIndex.setStatus("mandatory")


class _AccBrFpProt_Type(Integer32):
    """Custom type accBrFpProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrFpProt_Type.__name__ = "Integer32"
_AccBrFpProt_Object = MibTableColumn
accBrFpProt = _AccBrFpProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 2),
    _AccBrFpProt_Type()
)
accBrFpProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpProt.setStatus("mandatory")


class _AccBrFpPrio_Type(Integer32):
    """Custom type accBrFpPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccBrFpPrio_Type.__name__ = "Integer32"
_AccBrFpPrio_Object = MibTableColumn
accBrFpPrio = _AccBrFpPrio_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 8, 1, 3),
    _AccBrFpPrio_Type()
)
accBrFpPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpPrio.setStatus("mandatory")


class _AccBrFpPriDefault_Type(Integer32):
    """Custom type accBrFpPriDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccBrFpPriDefault_Type.__name__ = "Integer32"
_AccBrFpPriDefault_Object = MibScalar
accBrFpPriDefault = _AccBrFpPriDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 9),
    _AccBrFpPriDefault_Type()
)
accBrFpPriDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFpPriDefault.setStatus("mandatory")


class _AccBrNumPorts_Type(Integer32):
    """Custom type accBrNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_AccBrNumPorts_Type.__name__ = "Integer32"
_AccBrNumPorts_Object = MibScalar
accBrNumPorts = _AccBrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 10),
    _AccBrNumPorts_Type()
)
accBrNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrNumPorts.setStatus("mandatory")


class _AccBrCompress_Type(Integer32):
    """Custom type accBrCompress based on Integer32"""
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


_AccBrCompress_Type.__name__ = "Integer32"
_AccBrCompress_Object = MibScalar
accBrCompress = _AccBrCompress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 11),
    _AccBrCompress_Type()
)
accBrCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrCompress.setStatus("mandatory")
_AccBrPortX25Table_ObjectIdentity = ObjectIdentity
accBrPortX25Table = _AccBrPortX25Table_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14)
)
_AccBrPortX25Entry_ObjectIdentity = ObjectIdentity
accBrPortX25Entry = _AccBrPortX25Entry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1)
)


class _AccBrPortX25FacIndex_Type(Integer32):
    """Custom type accBrPortX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBrPortX25FacIndex_Type.__name__ = "Integer32"
_AccBrPortX25FacIndex_Object = MibScalar
accBrPortX25FacIndex = _AccBrPortX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 14, 1, 7),
    _AccBrPortX25FacIndex_Type()
)
accBrPortX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortX25FacIndex.setStatus("mandatory")


class _AccBrMode_Type(Integer32):
    """Custom type accBrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("off", 2),
          ("passive", 3))
    )


_AccBrMode_Type.__name__ = "Integer32"
_AccBrMode_Object = MibScalar
accBrMode = _AccBrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 15),
    _AccBrMode_Type()
)
accBrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrMode.setStatus("mandatory")


class _AccBrFilterMode_Type(Integer32):
    """Custom type accBrFilterMode based on Integer32"""
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


_AccBrFilterMode_Type.__name__ = "Integer32"
_AccBrFilterMode_Object = MibScalar
accBrFilterMode = _AccBrFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 16),
    _AccBrFilterMode_Type()
)
accBrFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterMode.setStatus("mandatory")


class _AccBrFilterDefault_Type(Integer32):
    """Custom type accBrFilterDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFilterDefault_Type.__name__ = "Integer32"
_AccBrFilterDefault_Object = MibScalar
accBrFilterDefault = _AccBrFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 17),
    _AccBrFilterDefault_Type()
)
accBrFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterDefault.setStatus("mandatory")
_AccBrFilterTable_Object = MibTable
accBrFilterTable = _AccBrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18)
)
if mibBuilder.loadTexts:
    accBrFilterTable.setStatus("deprecated")
_AccBrFilterEntry_Object = MibTableRow
accBrFilterEntry = _AccBrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1)
)
accBrFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accBrFilterEntDstMacAddr"),
    (0, "ACC-MIB", "accBrFilterEntSrcMacAddr"),
    (0, "ACC-MIB", "accBrFilterEntPort"),
    (0, "ACC-MIB", "accBrFilterEntLogicalOp"),
    (0, "ACC-MIB", "accBrFilterEntProtocol"),
)
if mibBuilder.loadTexts:
    accBrFilterEntry.setStatus("deprecated")
_AccBrFilterEntDstMacAddr_Type = OctetString
_AccBrFilterEntDstMacAddr_Object = MibTableColumn
accBrFilterEntDstMacAddr = _AccBrFilterEntDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 1),
    _AccBrFilterEntDstMacAddr_Type()
)
accBrFilterEntDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntDstMacAddr.setStatus("deprecated")
_AccBrFilterEntSrcMacAddr_Type = OctetString
_AccBrFilterEntSrcMacAddr_Object = MibTableColumn
accBrFilterEntSrcMacAddr = _AccBrFilterEntSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 2),
    _AccBrFilterEntSrcMacAddr_Type()
)
accBrFilterEntSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntSrcMacAddr.setStatus("deprecated")


class _AccBrFilterEntDisp_Type(Integer32):
    """Custom type accBrFilterEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFilterEntDisp_Type.__name__ = "Integer32"
_AccBrFilterEntDisp_Object = MibTableColumn
accBrFilterEntDisp = _AccBrFilterEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 3),
    _AccBrFilterEntDisp_Type()
)
accBrFilterEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntDisp.setStatus("deprecated")
_AccBrFilterEntPort_Type = Integer32
_AccBrFilterEntPort_Object = MibTableColumn
accBrFilterEntPort = _AccBrFilterEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 4),
    _AccBrFilterEntPort_Type()
)
accBrFilterEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntPort.setStatus("deprecated")


class _AccBrFilterEntLogicalOp_Type(Integer32):
    """Custom type accBrFilterEntLogicalOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("equal", 2),
          ("notequal", 3))
    )


_AccBrFilterEntLogicalOp_Type.__name__ = "Integer32"
_AccBrFilterEntLogicalOp_Object = MibTableColumn
accBrFilterEntLogicalOp = _AccBrFilterEntLogicalOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 5),
    _AccBrFilterEntLogicalOp_Type()
)
accBrFilterEntLogicalOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntLogicalOp.setStatus("deprecated")
_AccBrFilterEntProtocol_Type = OctetString
_AccBrFilterEntProtocol_Object = MibTableColumn
accBrFilterEntProtocol = _AccBrFilterEntProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 6),
    _AccBrFilterEntProtocol_Type()
)
accBrFilterEntProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFilterEntProtocol.setStatus("deprecated")
_AccBrFilterDiscards_Type = Integer32
_AccBrFilterDiscards_Object = MibTableColumn
accBrFilterDiscards = _AccBrFilterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 7),
    _AccBrFilterDiscards_Type()
)
accBrFilterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFilterDiscards.setStatus("deprecated")
_AccBrFilterEntries_Type = Integer32
_AccBrFilterEntries_Object = MibTableColumn
accBrFilterEntries = _AccBrFilterEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 18, 1, 8),
    _AccBrFilterEntries_Type()
)
accBrFilterEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFilterEntries.setStatus("deprecated")
_AccBrFiltIITable_Object = MibTable
accBrFiltIITable = _AccBrFiltIITable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19)
)
if mibBuilder.loadTexts:
    accBrFiltIITable.setStatus("mandatory")
_AccBrFiltIIEntry_Object = MibTableRow
accBrFiltIIEntry = _AccBrFiltIIEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1)
)
accBrFiltIIEntry.setIndexNames(
    (0, "ACC-MIB", "accBrFiltIIEntDstMacAddr"),
    (0, "ACC-MIB", "accBrFiltIIEntDstMacAddrMask"),
    (0, "ACC-MIB", "accBrFiltIIEntSrcMacAddr"),
    (0, "ACC-MIB", "accBrFiltIIEntSrcMacAddrMask"),
    (0, "ACC-MIB", "accBrFiltIIEntPort"),
    (0, "ACC-MIB", "accBrFiltIIEntLogicalOp"),
    (0, "ACC-MIB", "accBrFiltIIEntProtocol"),
)
if mibBuilder.loadTexts:
    accBrFiltIIEntry.setStatus("mandatory")


class _AccBrFiltIIEntDstMacAddr_Type(OctetString):
    """Custom type accBrFiltIIEntDstMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccBrFiltIIEntDstMacAddr_Type.__name__ = "OctetString"
_AccBrFiltIIEntDstMacAddr_Object = MibTableColumn
accBrFiltIIEntDstMacAddr = _AccBrFiltIIEntDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 1),
    _AccBrFiltIIEntDstMacAddr_Type()
)
accBrFiltIIEntDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDstMacAddr.setStatus("mandatory")


class _AccBrFiltIIEntSrcMacAddr_Type(OctetString):
    """Custom type accBrFiltIIEntSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccBrFiltIIEntSrcMacAddr_Type.__name__ = "OctetString"
_AccBrFiltIIEntSrcMacAddr_Object = MibTableColumn
accBrFiltIIEntSrcMacAddr = _AccBrFiltIIEntSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 2),
    _AccBrFiltIIEntSrcMacAddr_Type()
)
accBrFiltIIEntSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntSrcMacAddr.setStatus("mandatory")


class _AccBrFiltIIEntDisp_Type(Integer32):
    """Custom type accBrFiltIIEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccBrFiltIIEntDisp_Type.__name__ = "Integer32"
_AccBrFiltIIEntDisp_Object = MibTableColumn
accBrFiltIIEntDisp = _AccBrFiltIIEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 3),
    _AccBrFiltIIEntDisp_Type()
)
accBrFiltIIEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDisp.setStatus("mandatory")
_AccBrFiltIIEntPort_Type = Integer32
_AccBrFiltIIEntPort_Object = MibTableColumn
accBrFiltIIEntPort = _AccBrFiltIIEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 4),
    _AccBrFiltIIEntPort_Type()
)
accBrFiltIIEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntPort.setStatus("mandatory")


class _AccBrFiltIIEntLogicalOp_Type(Integer32):
    """Custom type accBrFiltIIEntLogicalOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("equal", 2),
          ("notequal", 3))
    )


_AccBrFiltIIEntLogicalOp_Type.__name__ = "Integer32"
_AccBrFiltIIEntLogicalOp_Object = MibTableColumn
accBrFiltIIEntLogicalOp = _AccBrFiltIIEntLogicalOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 5),
    _AccBrFiltIIEntLogicalOp_Type()
)
accBrFiltIIEntLogicalOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntLogicalOp.setStatus("mandatory")


class _AccBrFiltIIEntProtocol_Type(OctetString):
    """Custom type accBrFiltIIEntProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AccBrFiltIIEntProtocol_Type.__name__ = "OctetString"
_AccBrFiltIIEntProtocol_Object = MibTableColumn
accBrFiltIIEntProtocol = _AccBrFiltIIEntProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 6),
    _AccBrFiltIIEntProtocol_Type()
)
accBrFiltIIEntProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntProtocol.setStatus("mandatory")


class _AccBrFiltIIEntDstMacAddrMask_Type(OctetString):
    """Custom type accBrFiltIIEntDstMacAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccBrFiltIIEntDstMacAddrMask_Type.__name__ = "OctetString"
_AccBrFiltIIEntDstMacAddrMask_Object = MibTableColumn
accBrFiltIIEntDstMacAddrMask = _AccBrFiltIIEntDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 7),
    _AccBrFiltIIEntDstMacAddrMask_Type()
)
accBrFiltIIEntDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntDstMacAddrMask.setStatus("mandatory")


class _AccBrFiltIIEntSrcMacAddrMask_Type(OctetString):
    """Custom type accBrFiltIIEntSrcMacAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccBrFiltIIEntSrcMacAddrMask_Type.__name__ = "OctetString"
_AccBrFiltIIEntSrcMacAddrMask_Object = MibTableColumn
accBrFiltIIEntSrcMacAddrMask = _AccBrFiltIIEntSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 8),
    _AccBrFiltIIEntSrcMacAddrMask_Type()
)
accBrFiltIIEntSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntSrcMacAddrMask.setStatus("mandatory")
_AccBrFiltIIEntStatus_Type = Integer32
_AccBrFiltIIEntStatus_Object = MibTableColumn
accBrFiltIIEntStatus = _AccBrFiltIIEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 19, 1, 9),
    _AccBrFiltIIEntStatus_Type()
)
accBrFiltIIEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrFiltIIEntStatus.setStatus("mandatory")
_AccBrFiltIIDiscards_Type = Integer32
_AccBrFiltIIDiscards_Object = MibScalar
accBrFiltIIDiscards = _AccBrFiltIIDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 20),
    _AccBrFiltIIDiscards_Type()
)
accBrFiltIIDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFiltIIDiscards.setStatus("mandatory")
_AccBrFiltIIEntries_Type = Integer32
_AccBrFiltIIEntries_Object = MibScalar
accBrFiltIIEntries = _AccBrFiltIIEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 21),
    _AccBrFiltIIEntries_Type()
)
accBrFiltIIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrFiltIIEntries.setStatus("mandatory")


class _AccFdbWhichAddr_Type(Integer32):
    """Custom type accFdbWhichAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 1),
          ("source", 2))
    )


_AccFdbWhichAddr_Type.__name__ = "Integer32"
_AccFdbWhichAddr_Object = MibScalar
accFdbWhichAddr = _AccFdbWhichAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 4, 22),
    _AccFdbWhichAddr_Type()
)
accFdbWhichAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFdbWhichAddr.setStatus("mandatory")
_AccSlot_ObjectIdentity = ObjectIdentity
accSlot = _AccSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5)
)
_AccSlotTable_Object = MibTable
accSlotTable = _AccSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    accSlotTable.setStatus("mandatory")
_AccSlotEntry_Object = MibTableRow
accSlotEntry = _AccSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1)
)
accSlotEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accSlotEntry.setStatus("mandatory")
_AccSlotLastChange_Type = OctetString
_AccSlotLastChange_Object = MibTableColumn
accSlotLastChange = _AccSlotLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 9),
    _AccSlotLastChange_Type()
)
accSlotLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotLastChange.setStatus("mandatory")
_AccSlotInPkts_Type = Counter32
_AccSlotInPkts_Object = MibTableColumn
accSlotInPkts = _AccSlotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 11),
    _AccSlotInPkts_Type()
)
accSlotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotInPkts.setStatus("mandatory")
_AccSlotOutPkts_Type = Counter32
_AccSlotOutPkts_Object = MibTableColumn
accSlotOutPkts = _AccSlotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 17),
    _AccSlotOutPkts_Type()
)
accSlotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotOutPkts.setStatus("mandatory")
_AccSlotNumChanges_Type = Counter32
_AccSlotNumChanges_Object = MibTableColumn
accSlotNumChanges = _AccSlotNumChanges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 21),
    _AccSlotNumChanges_Type()
)
accSlotNumChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotNumChanges.setStatus("mandatory")


class _AccSlotProtocol_Type(Integer32):
    """Custom type accSlotProtocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dial", 10),
          ("enet", 1),
          ("fddi", 9),
          ("ffr", 4),
          ("lapb", 3),
          ("multilink", 11),
          ("other", 5),
          ("ppp", 8),
          ("smds", 7),
          ("token-ring", 6),
          ("x25", 2))
    )


_AccSlotProtocol_Type.__name__ = "Integer32"
_AccSlotProtocol_Object = MibTableColumn
accSlotProtocol = _AccSlotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 22),
    _AccSlotProtocol_Type()
)
accSlotProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotProtocol.setStatus("mandatory")


class _AccSlotClockMode_Type(Integer32):
    """Custom type accSlotClockMode based on Integer32"""
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
        *(("ext1", 2),
          ("ext2", 4),
          ("int", 5),
          ("pp", 3),
          ("slave", 6),
          ("unknown", 1))
    )


_AccSlotClockMode_Type.__name__ = "Integer32"
_AccSlotClockMode_Object = MibTableColumn
accSlotClockMode = _AccSlotClockMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 23),
    _AccSlotClockMode_Type()
)
accSlotClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotClockMode.setStatus("mandatory")


class _AccSlotQueueMode_Type(Integer32):
    """Custom type accSlotQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("express", 1),
          ("precedence", 2))
    )


_AccSlotQueueMode_Type.__name__ = "Integer32"
_AccSlotQueueMode_Object = MibTableColumn
accSlotQueueMode = _AccSlotQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 24),
    _AccSlotQueueMode_Type()
)
accSlotQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotQueueMode.setStatus("mandatory")


class _AccSlotDialProcedure_Type(Integer32):
    """Custom type accSlotDialProcedure based on Integer32"""
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
        *(("direct", 2),
          ("dtr", 4),
          ("hayes", 7),
          ("isdn", 5),
          ("lan", 1),
          ("v25", 6),
          ("x21", 3))
    )


_AccSlotDialProcedure_Type.__name__ = "Integer32"
_AccSlotDialProcedure_Object = MibTableColumn
accSlotDialProcedure = _AccSlotDialProcedure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 25),
    _AccSlotDialProcedure_Type()
)
accSlotDialProcedure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotDialProcedure.setStatus("mandatory")


class _AccSlotResyncMode_Type(Integer32):
    """Custom type accSlotResyncMode based on Integer32"""
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


_AccSlotResyncMode_Type.__name__ = "Integer32"
_AccSlotResyncMode_Object = MibTableColumn
accSlotResyncMode = _AccSlotResyncMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 26),
    _AccSlotResyncMode_Type()
)
accSlotResyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotResyncMode.setStatus("mandatory")


class _AccSlotCompressMode_Type(Integer32):
    """Custom type accSlotCompressMode based on Integer32"""
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


_AccSlotCompressMode_Type.__name__ = "Integer32"
_AccSlotCompressMode_Object = MibTableColumn
accSlotCompressMode = _AccSlotCompressMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 27),
    _AccSlotCompressMode_Type()
)
accSlotCompressMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMode.setStatus("mandatory")
_AccSlotCompressV42bisP1_Type = Integer32
_AccSlotCompressV42bisP1_Object = MibTableColumn
accSlotCompressV42bisP1 = _AccSlotCompressV42bisP1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 29),
    _AccSlotCompressV42bisP1_Type()
)
accSlotCompressV42bisP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotCompressV42bisP1.setStatus("mandatory")
_AccSlotCompressV42bisP2_Type = Integer32
_AccSlotCompressV42bisP2_Object = MibTableColumn
accSlotCompressV42bisP2 = _AccSlotCompressV42bisP2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 30),
    _AccSlotCompressV42bisP2_Type()
)
accSlotCompressV42bisP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSlotCompressV42bisP2.setStatus("mandatory")


class _AccSlotCompressDcs221P1_Type(Integer32):
    """Custom type accSlotCompressDcs221P1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccSlotCompressDcs221P1_Type.__name__ = "Integer32"
_AccSlotCompressDcs221P1_Object = MibTableColumn
accSlotCompressDcs221P1 = _AccSlotCompressDcs221P1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 31),
    _AccSlotCompressDcs221P1_Type()
)
accSlotCompressDcs221P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressDcs221P1.setStatus("mandatory")


class _AccSlotSevereCongPct_Type(Integer32):
    """Custom type accSlotSevereCongPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AccSlotSevereCongPct_Type.__name__ = "Integer32"
_AccSlotSevereCongPct_Object = MibTableColumn
accSlotSevereCongPct = _AccSlotSevereCongPct_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 32),
    _AccSlotSevereCongPct_Type()
)
accSlotSevereCongPct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotSevereCongPct.setStatus("mandatory")
_AccSlotDialAddress_Type = DisplayString
_AccSlotDialAddress_Object = MibTableColumn
accSlotDialAddress = _AccSlotDialAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 33),
    _AccSlotDialAddress_Type()
)
accSlotDialAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotDialAddress.setStatus("mandatory")


class _AccSlotCompressRevision_Type(Integer32):
    """Custom type accSlotCompressRevision based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("new", 2),
          ("old", 1))
    )


_AccSlotCompressRevision_Type.__name__ = "Integer32"
_AccSlotCompressRevision_Object = MibTableColumn
accSlotCompressRevision = _AccSlotCompressRevision_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 34),
    _AccSlotCompressRevision_Type()
)
accSlotCompressRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressRevision.setStatus("mandatory")


class _AccSlotCompressMaxStreams_Type(Integer32):
    """Custom type accSlotCompressMaxStreams based on Integer32"""
    defaultValue = 1


_AccSlotCompressMaxStreams_Object = MibTableColumn
accSlotCompressMaxStreams = _AccSlotCompressMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 35),
    _AccSlotCompressMaxStreams_Type()
)
accSlotCompressMaxStreams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMaxStreams.setStatus("mandatory")
_AccSlotCompressMessageLevel_Type = Integer32
_AccSlotCompressMessageLevel_Object = MibTableColumn
accSlotCompressMessageLevel = _AccSlotCompressMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 36),
    _AccSlotCompressMessageLevel_Type()
)
accSlotCompressMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotCompressMessageLevel.setStatus("mandatory")


class _AccSlotIfType_Type(Integer32):
    """Custom type accSlotIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 44),
    )


_AccSlotIfType_Type.__name__ = "Integer32"
_AccSlotIfType_Object = MibTableColumn
accSlotIfType = _AccSlotIfType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 5, 2, 1, 37),
    _AccSlotIfType_Type()
)
accSlotIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSlotIfType.setStatus("mandatory")
_AccCompress_ObjectIdentity = ObjectIdentity
accCompress = _AccCompress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6)
)
_AccCompressDialNeighborTable_Object = MibTable
accCompressDialNeighborTable = _AccCompressDialNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    accCompressDialNeighborTable.setStatus("mandatory")
_AccCompressDialNeighborEntry_Object = MibTableRow
accCompressDialNeighborEntry = _AccCompressDialNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1)
)
accCompressDialNeighborEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressDialNeighborIfIndex"),
    (0, "ACC-MIB", "accCompressDialNeighborCallAddress"),
)
if mibBuilder.loadTexts:
    accCompressDialNeighborEntry.setStatus("mandatory")
_AccCompressDialNeighborIfIndex_Type = Integer32
_AccCompressDialNeighborIfIndex_Object = MibTableColumn
accCompressDialNeighborIfIndex = _AccCompressDialNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 1),
    _AccCompressDialNeighborIfIndex_Type()
)
accCompressDialNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialNeighborIfIndex.setStatus("mandatory")
_AccCompressDialNeighborCallAddress_Type = DisplayString
_AccCompressDialNeighborCallAddress_Object = MibTableColumn
accCompressDialNeighborCallAddress = _AccCompressDialNeighborCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 2),
    _AccCompressDialNeighborCallAddress_Type()
)
accCompressDialNeighborCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialNeighborCallAddress.setStatus("mandatory")


class _AccCompressDialNeighborStatus_Type(Integer32):
    """Custom type accCompressDialNeighborStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 2),
          ("on", 1))
    )


_AccCompressDialNeighborStatus_Type.__name__ = "Integer32"
_AccCompressDialNeighborStatus_Object = MibTableColumn
accCompressDialNeighborStatus = _AccCompressDialNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 1, 1, 3),
    _AccCompressDialNeighborStatus_Type()
)
accCompressDialNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressDialNeighborStatus.setStatus("mandatory")
_AccCompressFfrNeighborTable_Object = MibTable
accCompressFfrNeighborTable = _AccCompressFfrNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    accCompressFfrNeighborTable.setStatus("mandatory")
_AccCompressFfrNeighborEntry_Object = MibTableRow
accCompressFfrNeighborEntry = _AccCompressFfrNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1)
)
accCompressFfrNeighborEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressFfrNeighborIfIndex"),
    (0, "ACC-MIB", "accCompressFfrNeighborDlci"),
)
if mibBuilder.loadTexts:
    accCompressFfrNeighborEntry.setStatus("mandatory")
_AccCompressFfrNeighborIfIndex_Type = Integer32
_AccCompressFfrNeighborIfIndex_Object = MibTableColumn
accCompressFfrNeighborIfIndex = _AccCompressFfrNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 1),
    _AccCompressFfrNeighborIfIndex_Type()
)
accCompressFfrNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrNeighborIfIndex.setStatus("mandatory")
_AccCompressFfrNeighborDlci_Type = Integer32
_AccCompressFfrNeighborDlci_Object = MibTableColumn
accCompressFfrNeighborDlci = _AccCompressFfrNeighborDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 2),
    _AccCompressFfrNeighborDlci_Type()
)
accCompressFfrNeighborDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrNeighborDlci.setStatus("mandatory")


class _AccCompressFfrNeighborStatus_Type(Integer32):
    """Custom type accCompressFfrNeighborStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 1),
          ("on", 2))
    )


_AccCompressFfrNeighborStatus_Type.__name__ = "Integer32"
_AccCompressFfrNeighborStatus_Object = MibTableColumn
accCompressFfrNeighborStatus = _AccCompressFfrNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 2, 1, 3),
    _AccCompressFfrNeighborStatus_Type()
)
accCompressFfrNeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressFfrNeighborStatus.setStatus("mandatory")
_AccCompressX25NeighborTable_Object = MibTable
accCompressX25NeighborTable = _AccCompressX25NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    accCompressX25NeighborTable.setStatus("mandatory")
_AccCompressX25NeighborEntry_Object = MibTableRow
accCompressX25NeighborEntry = _AccCompressX25NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1)
)
accCompressX25NeighborEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressX25NeighborIfIndex"),
    (0, "ACC-MIB", "accCompressX25NeighborAddress"),
)
if mibBuilder.loadTexts:
    accCompressX25NeighborEntry.setStatus("mandatory")
_AccCompressX25NeighborIfIndex_Type = Integer32
_AccCompressX25NeighborIfIndex_Object = MibTableColumn
accCompressX25NeighborIfIndex = _AccCompressX25NeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 1),
    _AccCompressX25NeighborIfIndex_Type()
)
accCompressX25NeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25NeighborIfIndex.setStatus("mandatory")
_AccCompressX25NeighborAddress_Type = DisplayString
_AccCompressX25NeighborAddress_Object = MibTableColumn
accCompressX25NeighborAddress = _AccCompressX25NeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 2),
    _AccCompressX25NeighborAddress_Type()
)
accCompressX25NeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25NeighborAddress.setStatus("mandatory")


class _AccCompressX25NeighborStatus_Type(Integer32):
    """Custom type accCompressX25NeighborStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 128),
          ("off", 1),
          ("on", 2))
    )


_AccCompressX25NeighborStatus_Type.__name__ = "Integer32"
_AccCompressX25NeighborStatus_Object = MibTableColumn
accCompressX25NeighborStatus = _AccCompressX25NeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 3, 1, 3),
    _AccCompressX25NeighborStatus_Type()
)
accCompressX25NeighborStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCompressX25NeighborStatus.setStatus("mandatory")
_AccCompressDialStatTable_Object = MibTable
accCompressDialStatTable = _AccCompressDialStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    accCompressDialStatTable.setStatus("mandatory")
_AccCompressDialStatEntry_Object = MibTableRow
accCompressDialStatEntry = _AccCompressDialStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1)
)
accCompressDialStatEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressDialStatIfIndex"),
)
if mibBuilder.loadTexts:
    accCompressDialStatEntry.setStatus("mandatory")
_AccCompressDialStatIfIndex_Type = Integer32
_AccCompressDialStatIfIndex_Object = MibTableColumn
accCompressDialStatIfIndex = _AccCompressDialStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 1),
    _AccCompressDialStatIfIndex_Type()
)
accCompressDialStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatIfIndex.setStatus("mandatory")
_AccCompressDialStatCallAddress_Type = OctetString
_AccCompressDialStatCallAddress_Object = MibTableColumn
accCompressDialStatCallAddress = _AccCompressDialStatCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 2),
    _AccCompressDialStatCallAddress_Type()
)
accCompressDialStatCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatCallAddress.setStatus("mandatory")


class _AccCompressDialStatStatus_Type(Integer32):
    """Custom type accCompressDialStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressDialStatStatus_Type.__name__ = "Integer32"
_AccCompressDialStatStatus_Object = MibTableColumn
accCompressDialStatStatus = _AccCompressDialStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 3),
    _AccCompressDialStatStatus_Type()
)
accCompressDialStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatStatus.setStatus("mandatory")
_AccCompressDialStatOctetsIns_Type = Counter32
_AccCompressDialStatOctetsIns_Object = MibTableColumn
accCompressDialStatOctetsIns = _AccCompressDialStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 4),
    _AccCompressDialStatOctetsIns_Type()
)
accCompressDialStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatOctetsIns.setStatus("mandatory")
_AccCompressDialStatOctetsOuts_Type = Counter32
_AccCompressDialStatOctetsOuts_Object = MibTableColumn
accCompressDialStatOctetsOuts = _AccCompressDialStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 5),
    _AccCompressDialStatOctetsOuts_Type()
)
accCompressDialStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatOctetsOuts.setStatus("mandatory")
_AccCompressDialStatPacketsIns_Type = Counter32
_AccCompressDialStatPacketsIns_Object = MibTableColumn
accCompressDialStatPacketsIns = _AccCompressDialStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 6),
    _AccCompressDialStatPacketsIns_Type()
)
accCompressDialStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatPacketsIns.setStatus("mandatory")
_AccCompressDialStatPacketsOuts_Type = Counter32
_AccCompressDialStatPacketsOuts_Object = MibTableColumn
accCompressDialStatPacketsOuts = _AccCompressDialStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 7),
    _AccCompressDialStatPacketsOuts_Type()
)
accCompressDialStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatPacketsOuts.setStatus("mandatory")
_AccCompressDialStatUnCompIns_Type = Counter32
_AccCompressDialStatUnCompIns_Object = MibTableColumn
accCompressDialStatUnCompIns = _AccCompressDialStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 8),
    _AccCompressDialStatUnCompIns_Type()
)
accCompressDialStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatUnCompIns.setStatus("mandatory")
_AccCompressDialStatUnCompOuts_Type = Counter32
_AccCompressDialStatUnCompOuts_Object = MibTableColumn
accCompressDialStatUnCompOuts = _AccCompressDialStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 9),
    _AccCompressDialStatUnCompOuts_Type()
)
accCompressDialStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatUnCompOuts.setStatus("mandatory")
_AccCompressDialStatAvgCompIn_Type = Gauge32
_AccCompressDialStatAvgCompIn_Object = MibTableColumn
accCompressDialStatAvgCompIn = _AccCompressDialStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 10),
    _AccCompressDialStatAvgCompIn_Type()
)
accCompressDialStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatAvgCompIn.setStatus("mandatory")
_AccCompressDialStatAvgCompOut_Type = Gauge32
_AccCompressDialStatAvgCompOut_Object = MibTableColumn
accCompressDialStatAvgCompOut = _AccCompressDialStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 11),
    _AccCompressDialStatAvgCompOut_Type()
)
accCompressDialStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatAvgCompOut.setStatus("mandatory")
_AccCompressDialStatHdrErrors_Type = Counter32
_AccCompressDialStatHdrErrors_Object = MibTableColumn
accCompressDialStatHdrErrors = _AccCompressDialStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 12),
    _AccCompressDialStatHdrErrors_Type()
)
accCompressDialStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatHdrErrors.setStatus("mandatory")
_AccCompressDialStatResyncs_Type = Counter32
_AccCompressDialStatResyncs_Object = MibTableColumn
accCompressDialStatResyncs = _AccCompressDialStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 13),
    _AccCompressDialStatResyncs_Type()
)
accCompressDialStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatResyncs.setStatus("mandatory")
_AccCompressDialStatNoEndMarks_Type = Counter32
_AccCompressDialStatNoEndMarks_Object = MibTableColumn
accCompressDialStatNoEndMarks = _AccCompressDialStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 14),
    _AccCompressDialStatNoEndMarks_Type()
)
accCompressDialStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatNoEndMarks.setStatus("mandatory")
_AccCompressDialStatNoBufAvails_Type = Counter32
_AccCompressDialStatNoBufAvails_Object = MibTableColumn
accCompressDialStatNoBufAvails = _AccCompressDialStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 4, 1, 15),
    _AccCompressDialStatNoBufAvails_Type()
)
accCompressDialStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressDialStatNoBufAvails.setStatus("mandatory")
_AccCompressFfrStatTable_Object = MibTable
accCompressFfrStatTable = _AccCompressFfrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    accCompressFfrStatTable.setStatus("mandatory")
_AccCompressFfrStatEntry_Object = MibTableRow
accCompressFfrStatEntry = _AccCompressFfrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1)
)
accCompressFfrStatEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressFfrStatIfIndex"),
    (0, "ACC-MIB", "accCompressFfrStatDlci"),
)
if mibBuilder.loadTexts:
    accCompressFfrStatEntry.setStatus("mandatory")
_AccCompressFfrStatIfIndex_Type = Integer32
_AccCompressFfrStatIfIndex_Object = MibTableColumn
accCompressFfrStatIfIndex = _AccCompressFfrStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 1),
    _AccCompressFfrStatIfIndex_Type()
)
accCompressFfrStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatIfIndex.setStatus("mandatory")
_AccCompressFfrStatDlci_Type = Integer32
_AccCompressFfrStatDlci_Object = MibTableColumn
accCompressFfrStatDlci = _AccCompressFfrStatDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 2),
    _AccCompressFfrStatDlci_Type()
)
accCompressFfrStatDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatDlci.setStatus("mandatory")


class _AccCompressFfrStatStatus_Type(Integer32):
    """Custom type accCompressFfrStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressFfrStatStatus_Type.__name__ = "Integer32"
_AccCompressFfrStatStatus_Object = MibTableColumn
accCompressFfrStatStatus = _AccCompressFfrStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 3),
    _AccCompressFfrStatStatus_Type()
)
accCompressFfrStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatStatus.setStatus("mandatory")
_AccCompressFfrStatOctetsIns_Type = Counter32
_AccCompressFfrStatOctetsIns_Object = MibTableColumn
accCompressFfrStatOctetsIns = _AccCompressFfrStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 4),
    _AccCompressFfrStatOctetsIns_Type()
)
accCompressFfrStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatOctetsIns.setStatus("mandatory")
_AccCompressFfrStatOctetsOuts_Type = Counter32
_AccCompressFfrStatOctetsOuts_Object = MibTableColumn
accCompressFfrStatOctetsOuts = _AccCompressFfrStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 5),
    _AccCompressFfrStatOctetsOuts_Type()
)
accCompressFfrStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatOctetsOuts.setStatus("mandatory")
_AccCompressFfrStatPacketsIns_Type = Counter32
_AccCompressFfrStatPacketsIns_Object = MibTableColumn
accCompressFfrStatPacketsIns = _AccCompressFfrStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 6),
    _AccCompressFfrStatPacketsIns_Type()
)
accCompressFfrStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatPacketsIns.setStatus("mandatory")
_AccCompressFfrStatPacketsOuts_Type = Counter32
_AccCompressFfrStatPacketsOuts_Object = MibTableColumn
accCompressFfrStatPacketsOuts = _AccCompressFfrStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 7),
    _AccCompressFfrStatPacketsOuts_Type()
)
accCompressFfrStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatPacketsOuts.setStatus("mandatory")
_AccCompressFfrStatUnCompIns_Type = Counter32
_AccCompressFfrStatUnCompIns_Object = MibTableColumn
accCompressFfrStatUnCompIns = _AccCompressFfrStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 8),
    _AccCompressFfrStatUnCompIns_Type()
)
accCompressFfrStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatUnCompIns.setStatus("mandatory")
_AccCompressFfrStatUnCompOuts_Type = Counter32
_AccCompressFfrStatUnCompOuts_Object = MibTableColumn
accCompressFfrStatUnCompOuts = _AccCompressFfrStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 9),
    _AccCompressFfrStatUnCompOuts_Type()
)
accCompressFfrStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatUnCompOuts.setStatus("mandatory")
_AccCompressFfrStatAvgCompIn_Type = Gauge32
_AccCompressFfrStatAvgCompIn_Object = MibTableColumn
accCompressFfrStatAvgCompIn = _AccCompressFfrStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 10),
    _AccCompressFfrStatAvgCompIn_Type()
)
accCompressFfrStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatAvgCompIn.setStatus("mandatory")
_AccCompressFfrStatAvgCompOut_Type = Gauge32
_AccCompressFfrStatAvgCompOut_Object = MibTableColumn
accCompressFfrStatAvgCompOut = _AccCompressFfrStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 11),
    _AccCompressFfrStatAvgCompOut_Type()
)
accCompressFfrStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatAvgCompOut.setStatus("mandatory")
_AccCompressFfrStatHdrErrors_Type = Counter32
_AccCompressFfrStatHdrErrors_Object = MibTableColumn
accCompressFfrStatHdrErrors = _AccCompressFfrStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 12),
    _AccCompressFfrStatHdrErrors_Type()
)
accCompressFfrStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatHdrErrors.setStatus("mandatory")
_AccCompressFfrStatResyncs_Type = Counter32
_AccCompressFfrStatResyncs_Object = MibTableColumn
accCompressFfrStatResyncs = _AccCompressFfrStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 13),
    _AccCompressFfrStatResyncs_Type()
)
accCompressFfrStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatResyncs.setStatus("mandatory")
_AccCompressFfrStatNoEndMarks_Type = Counter32
_AccCompressFfrStatNoEndMarks_Object = MibTableColumn
accCompressFfrStatNoEndMarks = _AccCompressFfrStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 14),
    _AccCompressFfrStatNoEndMarks_Type()
)
accCompressFfrStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatNoEndMarks.setStatus("mandatory")
_AccCompressFfrStatNoBufAvails_Type = Counter32
_AccCompressFfrStatNoBufAvails_Object = MibTableColumn
accCompressFfrStatNoBufAvails = _AccCompressFfrStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 5, 1, 15),
    _AccCompressFfrStatNoBufAvails_Type()
)
accCompressFfrStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressFfrStatNoBufAvails.setStatus("mandatory")
_AccCompressX25StatTable_Object = MibTable
accCompressX25StatTable = _AccCompressX25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    accCompressX25StatTable.setStatus("mandatory")
_AccCompressX25StatEntry_Object = MibTableRow
accCompressX25StatEntry = _AccCompressX25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1)
)
accCompressX25StatEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressX25StatIfIndex"),
    (0, "ACC-MIB", "accCompressX25StatAddress"),
)
if mibBuilder.loadTexts:
    accCompressX25StatEntry.setStatus("mandatory")
_AccCompressX25StatIfIndex_Type = Integer32
_AccCompressX25StatIfIndex_Object = MibTableColumn
accCompressX25StatIfIndex = _AccCompressX25StatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 1),
    _AccCompressX25StatIfIndex_Type()
)
accCompressX25StatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatIfIndex.setStatus("mandatory")
_AccCompressX25StatAddress_Type = OctetString
_AccCompressX25StatAddress_Object = MibTableColumn
accCompressX25StatAddress = _AccCompressX25StatAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 2),
    _AccCompressX25StatAddress_Type()
)
accCompressX25StatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAddress.setStatus("mandatory")


class _AccCompressX25StatStatus_Type(Integer32):
    """Custom type accCompressX25StatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressX25StatStatus_Type.__name__ = "Integer32"
_AccCompressX25StatStatus_Object = MibTableColumn
accCompressX25StatStatus = _AccCompressX25StatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 3),
    _AccCompressX25StatStatus_Type()
)
accCompressX25StatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatStatus.setStatus("mandatory")
_AccCompressX25StatOctetsIns_Type = Counter32
_AccCompressX25StatOctetsIns_Object = MibTableColumn
accCompressX25StatOctetsIns = _AccCompressX25StatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 4),
    _AccCompressX25StatOctetsIns_Type()
)
accCompressX25StatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatOctetsIns.setStatus("mandatory")
_AccCompressX25StatOctetsOuts_Type = Counter32
_AccCompressX25StatOctetsOuts_Object = MibTableColumn
accCompressX25StatOctetsOuts = _AccCompressX25StatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 5),
    _AccCompressX25StatOctetsOuts_Type()
)
accCompressX25StatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatOctetsOuts.setStatus("mandatory")
_AccCompressX25StatPacketsIns_Type = Counter32
_AccCompressX25StatPacketsIns_Object = MibTableColumn
accCompressX25StatPacketsIns = _AccCompressX25StatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 6),
    _AccCompressX25StatPacketsIns_Type()
)
accCompressX25StatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatPacketsIns.setStatus("mandatory")
_AccCompressX25StatPacketsOuts_Type = Counter32
_AccCompressX25StatPacketsOuts_Object = MibTableColumn
accCompressX25StatPacketsOuts = _AccCompressX25StatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 7),
    _AccCompressX25StatPacketsOuts_Type()
)
accCompressX25StatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatPacketsOuts.setStatus("mandatory")
_AccCompressX25StatUnCompIns_Type = Counter32
_AccCompressX25StatUnCompIns_Object = MibTableColumn
accCompressX25StatUnCompIns = _AccCompressX25StatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 8),
    _AccCompressX25StatUnCompIns_Type()
)
accCompressX25StatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatUnCompIns.setStatus("mandatory")
_AccCompressX25StatUnCompOuts_Type = Counter32
_AccCompressX25StatUnCompOuts_Object = MibTableColumn
accCompressX25StatUnCompOuts = _AccCompressX25StatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 9),
    _AccCompressX25StatUnCompOuts_Type()
)
accCompressX25StatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatUnCompOuts.setStatus("mandatory")
_AccCompressX25StatAvgCompIn_Type = Gauge32
_AccCompressX25StatAvgCompIn_Object = MibTableColumn
accCompressX25StatAvgCompIn = _AccCompressX25StatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 10),
    _AccCompressX25StatAvgCompIn_Type()
)
accCompressX25StatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAvgCompIn.setStatus("mandatory")
_AccCompressX25StatAvgCompOut_Type = Gauge32
_AccCompressX25StatAvgCompOut_Object = MibTableColumn
accCompressX25StatAvgCompOut = _AccCompressX25StatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 11),
    _AccCompressX25StatAvgCompOut_Type()
)
accCompressX25StatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatAvgCompOut.setStatus("mandatory")
_AccCompressX25StatHdrErrors_Type = Counter32
_AccCompressX25StatHdrErrors_Object = MibTableColumn
accCompressX25StatHdrErrors = _AccCompressX25StatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 12),
    _AccCompressX25StatHdrErrors_Type()
)
accCompressX25StatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatHdrErrors.setStatus("mandatory")
_AccCompressX25StatResyncs_Type = Counter32
_AccCompressX25StatResyncs_Object = MibTableColumn
accCompressX25StatResyncs = _AccCompressX25StatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 13),
    _AccCompressX25StatResyncs_Type()
)
accCompressX25StatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatResyncs.setStatus("mandatory")
_AccCompressX25StatNoEndMarks_Type = Counter32
_AccCompressX25StatNoEndMarks_Object = MibTableColumn
accCompressX25StatNoEndMarks = _AccCompressX25StatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 14),
    _AccCompressX25StatNoEndMarks_Type()
)
accCompressX25StatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatNoEndMarks.setStatus("mandatory")
_AccCompressX25StatNoBufAvails_Type = Counter32
_AccCompressX25StatNoBufAvails_Object = MibTableColumn
accCompressX25StatNoBufAvails = _AccCompressX25StatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 6, 1, 15),
    _AccCompressX25StatNoBufAvails_Type()
)
accCompressX25StatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressX25StatNoBufAvails.setStatus("mandatory")
_AccCompressPhysStatTable_Object = MibTable
accCompressPhysStatTable = _AccCompressPhysStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7)
)
if mibBuilder.loadTexts:
    accCompressPhysStatTable.setStatus("mandatory")
_AccCompressPhysStatEntry_Object = MibTableRow
accCompressPhysStatEntry = _AccCompressPhysStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1)
)
accCompressPhysStatEntry.setIndexNames(
    (0, "ACC-MIB", "accCompressPhysStatIfIndex"),
)
if mibBuilder.loadTexts:
    accCompressPhysStatEntry.setStatus("mandatory")
_AccCompressPhysStatIfIndex_Type = Integer32
_AccCompressPhysStatIfIndex_Object = MibTableColumn
accCompressPhysStatIfIndex = _AccCompressPhysStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 1),
    _AccCompressPhysStatIfIndex_Type()
)
accCompressPhysStatIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatIfIndex.setStatus("mandatory")


class _AccCompressPhysStatStatus_Type(Integer32):
    """Custom type accCompressPhysStatStatus based on Integer32"""
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
        *(("conn", 2),
          ("disc", 1),
          ("resync", 4),
          ("sync", 3))
    )


_AccCompressPhysStatStatus_Type.__name__ = "Integer32"
_AccCompressPhysStatStatus_Object = MibTableColumn
accCompressPhysStatStatus = _AccCompressPhysStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 2),
    _AccCompressPhysStatStatus_Type()
)
accCompressPhysStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatStatus.setStatus("mandatory")
_AccCompressPhysStatOctetsIns_Type = Counter32
_AccCompressPhysStatOctetsIns_Object = MibTableColumn
accCompressPhysStatOctetsIns = _AccCompressPhysStatOctetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 3),
    _AccCompressPhysStatOctetsIns_Type()
)
accCompressPhysStatOctetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatOctetsIns.setStatus("mandatory")
_AccCompressPhysStatOctetsOuts_Type = Counter32
_AccCompressPhysStatOctetsOuts_Object = MibTableColumn
accCompressPhysStatOctetsOuts = _AccCompressPhysStatOctetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 4),
    _AccCompressPhysStatOctetsOuts_Type()
)
accCompressPhysStatOctetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatOctetsOuts.setStatus("mandatory")
_AccCompressPhysStatPacketsIns_Type = Counter32
_AccCompressPhysStatPacketsIns_Object = MibTableColumn
accCompressPhysStatPacketsIns = _AccCompressPhysStatPacketsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 5),
    _AccCompressPhysStatPacketsIns_Type()
)
accCompressPhysStatPacketsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatPacketsIns.setStatus("mandatory")
_AccCompressPhysStatPacketsOuts_Type = Counter32
_AccCompressPhysStatPacketsOuts_Object = MibTableColumn
accCompressPhysStatPacketsOuts = _AccCompressPhysStatPacketsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 6),
    _AccCompressPhysStatPacketsOuts_Type()
)
accCompressPhysStatPacketsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatPacketsOuts.setStatus("mandatory")
_AccCompressPhysStatUnCompIns_Type = Counter32
_AccCompressPhysStatUnCompIns_Object = MibTableColumn
accCompressPhysStatUnCompIns = _AccCompressPhysStatUnCompIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 7),
    _AccCompressPhysStatUnCompIns_Type()
)
accCompressPhysStatUnCompIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatUnCompIns.setStatus("mandatory")
_AccCompressPhysStatUnCompOuts_Type = Counter32
_AccCompressPhysStatUnCompOuts_Object = MibTableColumn
accCompressPhysStatUnCompOuts = _AccCompressPhysStatUnCompOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 8),
    _AccCompressPhysStatUnCompOuts_Type()
)
accCompressPhysStatUnCompOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatUnCompOuts.setStatus("mandatory")
_AccCompressPhysStatAvgCompIn_Type = Gauge32
_AccCompressPhysStatAvgCompIn_Object = MibTableColumn
accCompressPhysStatAvgCompIn = _AccCompressPhysStatAvgCompIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 9),
    _AccCompressPhysStatAvgCompIn_Type()
)
accCompressPhysStatAvgCompIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatAvgCompIn.setStatus("mandatory")
_AccCompressPhysStatAvgCompOut_Type = Gauge32
_AccCompressPhysStatAvgCompOut_Object = MibTableColumn
accCompressPhysStatAvgCompOut = _AccCompressPhysStatAvgCompOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 10),
    _AccCompressPhysStatAvgCompOut_Type()
)
accCompressPhysStatAvgCompOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatAvgCompOut.setStatus("mandatory")
_AccCompressPhysStatHdrErrors_Type = Counter32
_AccCompressPhysStatHdrErrors_Object = MibTableColumn
accCompressPhysStatHdrErrors = _AccCompressPhysStatHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 11),
    _AccCompressPhysStatHdrErrors_Type()
)
accCompressPhysStatHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatHdrErrors.setStatus("mandatory")
_AccCompressPhysStatResyncs_Type = Counter32
_AccCompressPhysStatResyncs_Object = MibTableColumn
accCompressPhysStatResyncs = _AccCompressPhysStatResyncs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 12),
    _AccCompressPhysStatResyncs_Type()
)
accCompressPhysStatResyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatResyncs.setStatus("mandatory")
_AccCompressPhysStatNoEndMarks_Type = Counter32
_AccCompressPhysStatNoEndMarks_Object = MibTableColumn
accCompressPhysStatNoEndMarks = _AccCompressPhysStatNoEndMarks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 13),
    _AccCompressPhysStatNoEndMarks_Type()
)
accCompressPhysStatNoEndMarks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatNoEndMarks.setStatus("mandatory")
_AccCompressPhysStatNoBufAvails_Type = Counter32
_AccCompressPhysStatNoBufAvails_Object = MibTableColumn
accCompressPhysStatNoBufAvails = _AccCompressPhysStatNoBufAvails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 6, 7, 1, 14),
    _AccCompressPhysStatNoBufAvails_Type()
)
accCompressPhysStatNoBufAvails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCompressPhysStatNoBufAvails.setStatus("mandatory")
_AccLapb_ObjectIdentity = ObjectIdentity
accLapb = _AccLapb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7)
)
_AccLapbNum_Type = Integer32
_AccLapbNum_Object = MibScalar
accLapbNum = _AccLapbNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 1),
    _AccLapbNum_Type()
)
accLapbNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbNum.setStatus("mandatory")
_AccLapbParmTable_Object = MibTable
accLapbParmTable = _AccLapbParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    accLapbParmTable.setStatus("mandatory")
_AccLapbParmEntry_Object = MibTableRow
accLapbParmEntry = _AccLapbParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1)
)
accLapbParmEntry.setIndexNames(
    (0, "ACC-MIB", "accLapbIndex"),
)
if mibBuilder.loadTexts:
    accLapbParmEntry.setStatus("mandatory")
_AccLapbIndex_Type = Integer32
_AccLapbIndex_Object = MibTableColumn
accLapbIndex = _AccLapbIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 1),
    _AccLapbIndex_Type()
)
accLapbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbIndex.setStatus("mandatory")


class _AccLapbType_Type(Integer32):
    """Custom type accLapbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccLapbType_Type.__name__ = "Integer32"
_AccLapbType_Object = MibTableColumn
accLapbType = _AccLapbType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 2),
    _AccLapbType_Type()
)
accLapbType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbType.setStatus("mandatory")


class _AccLapbT1Timer_Type(Integer32):
    """Custom type accLapbT1Timer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_AccLapbT1Timer_Type.__name__ = "Integer32"
_AccLapbT1Timer_Object = MibTableColumn
accLapbT1Timer = _AccLapbT1Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 3),
    _AccLapbT1Timer_Type()
)
accLapbT1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbT1Timer.setStatus("mandatory")


class _AccLapbN2Count_Type(Integer32):
    """Custom type accLapbN2Count based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 20),
    )


_AccLapbN2Count_Type.__name__ = "Integer32"
_AccLapbN2Count_Object = MibTableColumn
accLapbN2Count = _AccLapbN2Count_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 4),
    _AccLapbN2Count_Type()
)
accLapbN2Count.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbN2Count.setStatus("mandatory")


class _AccLapbFrameWindow_Type(Integer32):
    """Custom type accLapbFrameWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_AccLapbFrameWindow_Type.__name__ = "Integer32"
_AccLapbFrameWindow_Object = MibTableColumn
accLapbFrameWindow = _AccLapbFrameWindow_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 5),
    _AccLapbFrameWindow_Type()
)
accLapbFrameWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbFrameWindow.setStatus("mandatory")


class _AccLapbFlags_Type(Integer32):
    """Custom type accLapbFlags based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccLapbFlags_Type.__name__ = "Integer32"
_AccLapbFlags_Object = MibTableColumn
accLapbFlags = _AccLapbFlags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 6),
    _AccLapbFlags_Type()
)
accLapbFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accLapbFlags.setStatus("mandatory")


class _AccHdlcRrPolling_Type(Integer32):
    """Custom type accHdlcRrPolling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32000),
    )


_AccHdlcRrPolling_Type.__name__ = "Integer32"
_AccHdlcRrPolling_Object = MibTableColumn
accHdlcRrPolling = _AccHdlcRrPolling_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 7),
    _AccHdlcRrPolling_Type()
)
accHdlcRrPolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcRrPolling.setStatus("mandatory")


class _AccHdlcFCS_Type(Integer32):
    """Custom type accHdlcFCS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccitt-16", 1),
          ("ccitt-32", 2))
    )


_AccHdlcFCS_Type.__name__ = "Integer32"
_AccHdlcFCS_Object = MibTableColumn
accHdlcFCS = _AccHdlcFCS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 2, 1, 8),
    _AccHdlcFCS_Type()
)
accHdlcFCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accHdlcFCS.setStatus("mandatory")
_AccLapbStatTable_Object = MibTable
accLapbStatTable = _AccLapbStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    accLapbStatTable.setStatus("mandatory")
_AccLapbStatEntry_Object = MibTableRow
accLapbStatEntry = _AccLapbStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1)
)
accLapbStatEntry.setIndexNames(
    (0, "ACC-MIB", "accLapbStatIndex"),
)
if mibBuilder.loadTexts:
    accLapbStatEntry.setStatus("mandatory")
_AccLapbStatIndex_Type = Integer32
_AccLapbStatIndex_Object = MibTableColumn
accLapbStatIndex = _AccLapbStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 1),
    _AccLapbStatIndex_Type()
)
accLapbStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatIndex.setStatus("mandatory")
_AccLapbStatBadFCSIns_Type = Counter32
_AccLapbStatBadFCSIns_Object = MibTableColumn
accLapbStatBadFCSIns = _AccLapbStatBadFCSIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 2),
    _AccLapbStatBadFCSIns_Type()
)
accLapbStatBadFCSIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatBadFCSIns.setStatus("mandatory")
_AccLapbStatFRMRIns_Type = Counter32
_AccLapbStatFRMRIns_Object = MibTableColumn
accLapbStatFRMRIns = _AccLapbStatFRMRIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 3),
    _AccLapbStatFRMRIns_Type()
)
accLapbStatFRMRIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatFRMRIns.setStatus("mandatory")
_AccLapbStatT1Timeouts_Type = Counter32
_AccLapbStatT1Timeouts_Object = MibTableColumn
accLapbStatT1Timeouts = _AccLapbStatT1Timeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 4),
    _AccLapbStatT1Timeouts_Type()
)
accLapbStatT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatT1Timeouts.setStatus("mandatory")
_AccLapbStatREJIns_Type = Counter32
_AccLapbStatREJIns_Object = MibTableColumn
accLapbStatREJIns = _AccLapbStatREJIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 5),
    _AccLapbStatREJIns_Type()
)
accLapbStatREJIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatREJIns.setStatus("mandatory")
_AccLapbStatREJOuts_Type = Counter32
_AccLapbStatREJOuts_Object = MibTableColumn
accLapbStatREJOuts = _AccLapbStatREJOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 6),
    _AccLapbStatREJOuts_Type()
)
accLapbStatREJOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatREJOuts.setStatus("mandatory")
_AccLapbStatShortIns_Type = Counter32
_AccLapbStatShortIns_Object = MibTableColumn
accLapbStatShortIns = _AccLapbStatShortIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 7, 3, 1, 7),
    _AccLapbStatShortIns_Type()
)
accLapbStatShortIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accLapbStatShortIns.setStatus("mandatory")
_AccEnet_ObjectIdentity = ObjectIdentity
accEnet = _AccEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8)
)
_AccEnetNum_Type = Integer32
_AccEnetNum_Object = MibScalar
accEnetNum = _AccEnetNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 1),
    _AccEnetNum_Type()
)
accEnetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetNum.setStatus("mandatory")
_AccEnetParmTable_Object = MibTable
accEnetParmTable = _AccEnetParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    accEnetParmTable.setStatus("mandatory")
_AccEnetParmEntry_Object = MibTableRow
accEnetParmEntry = _AccEnetParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1)
)
accEnetParmEntry.setIndexNames(
    (0, "ACC-MIB", "accEnetPortNo"),
)
if mibBuilder.loadTexts:
    accEnetParmEntry.setStatus("mandatory")
_AccEnetPortNo_Type = Integer32
_AccEnetPortNo_Object = MibTableColumn
accEnetPortNo = _AccEnetPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 2, 1, 1),
    _AccEnetPortNo_Type()
)
accEnetPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetPortNo.setStatus("mandatory")
_AccEnetStatTable_Object = MibTable
accEnetStatTable = _AccEnetStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3)
)
if mibBuilder.loadTexts:
    accEnetStatTable.setStatus("mandatory")
_AccEnetStatEntry_Object = MibTableRow
accEnetStatEntry = _AccEnetStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1)
)
accEnetStatEntry.setIndexNames(
    (0, "ACC-MIB", "accEnetIndex"),
)
if mibBuilder.loadTexts:
    accEnetStatEntry.setStatus("mandatory")
_AccEnetIndex_Type = Integer32
_AccEnetIndex_Object = MibTableColumn
accEnetIndex = _AccEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 1),
    _AccEnetIndex_Type()
)
accEnetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetIndex.setStatus("mandatory")
_AccEnetStatCRCErrs_Type = Counter32
_AccEnetStatCRCErrs_Object = MibTableColumn
accEnetStatCRCErrs = _AccEnetStatCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 2),
    _AccEnetStatCRCErrs_Type()
)
accEnetStatCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatCRCErrs.setStatus("mandatory")
_AccEnetStatAlignErrs_Type = Counter32
_AccEnetStatAlignErrs_Object = MibTableColumn
accEnetStatAlignErrs = _AccEnetStatAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 3),
    _AccEnetStatAlignErrs_Type()
)
accEnetStatAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatAlignErrs.setStatus("mandatory")
_AccEnetStatOutColls_Type = Counter32
_AccEnetStatOutColls_Object = MibTableColumn
accEnetStatOutColls = _AccEnetStatOutColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 4),
    _AccEnetStatOutColls_Type()
)
accEnetStatOutColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatOutColls.setStatus("mandatory")
_AccEnetStatJabberConds_Type = Counter32
_AccEnetStatJabberConds_Object = MibTableColumn
accEnetStatJabberConds = _AccEnetStatJabberConds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 5),
    _AccEnetStatJabberConds_Type()
)
accEnetStatJabberConds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatJabberConds.setStatus("mandatory")
_AccEnetStatCarrierLosts_Type = Counter32
_AccEnetStatCarrierLosts_Object = MibTableColumn
accEnetStatCarrierLosts = _AccEnetStatCarrierLosts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 6),
    _AccEnetStatCarrierLosts_Type()
)
accEnetStatCarrierLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatCarrierLosts.setStatus("mandatory")
_AccEnetStatHeartbeatErrs_Type = Counter32
_AccEnetStatHeartbeatErrs_Object = MibTableColumn
accEnetStatHeartbeatErrs = _AccEnetStatHeartbeatErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 7),
    _AccEnetStatHeartbeatErrs_Type()
)
accEnetStatHeartbeatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatHeartbeatErrs.setStatus("mandatory")
_AccEnetStatGiants_Type = Counter32
_AccEnetStatGiants_Object = MibTableColumn
accEnetStatGiants = _AccEnetStatGiants_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 8),
    _AccEnetStatGiants_Type()
)
accEnetStatGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatGiants.setStatus("mandatory")
_AccEnetStatOneRetrys_Type = Counter32
_AccEnetStatOneRetrys_Object = MibTableColumn
accEnetStatOneRetrys = _AccEnetStatOneRetrys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 9),
    _AccEnetStatOneRetrys_Type()
)
accEnetStatOneRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatOneRetrys.setStatus("mandatory")
_AccEnetStatMultRetrys_Type = Counter32
_AccEnetStatMultRetrys_Object = MibTableColumn
accEnetStatMultRetrys = _AccEnetStatMultRetrys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 10),
    _AccEnetStatMultRetrys_Type()
)
accEnetStatMultRetrys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatMultRetrys.setStatus("mandatory")
_AccEnetStatLateColls_Type = Counter32
_AccEnetStatLateColls_Object = MibTableColumn
accEnetStatLateColls = _AccEnetStatLateColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 11),
    _AccEnetStatLateColls_Type()
)
accEnetStatLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetStatLateColls.setStatus("mandatory")
_AccEnetChipCrashes_Type = Counter32
_AccEnetChipCrashes_Object = MibTableColumn
accEnetChipCrashes = _AccEnetChipCrashes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 8, 3, 1, 12),
    _AccEnetChipCrashes_Type()
)
accEnetChipCrashes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetChipCrashes.setStatus("mandatory")
_AccMultilink_ObjectIdentity = ObjectIdentity
accMultilink = _AccMultilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9)
)
_AccMultilinkParameterTable_Object = MibTable
accMultilinkParameterTable = _AccMultilinkParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    accMultilinkParameterTable.setStatus("mandatory")
_AccMultilinkParameterEntry_Object = MibTableRow
accMultilinkParameterEntry = _AccMultilinkParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1)
)
accMultilinkParameterEntry.setIndexNames(
    (0, "ACC-MIB", "accMultilinkParameterIndex"),
)
if mibBuilder.loadTexts:
    accMultilinkParameterEntry.setStatus("mandatory")
_AccMultilinkParameterIndex_Type = Integer32
_AccMultilinkParameterIndex_Object = MibTableColumn
accMultilinkParameterIndex = _AccMultilinkParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 1),
    _AccMultilinkParameterIndex_Type()
)
accMultilinkParameterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterIndex.setStatus("mandatory")
_AccMultilinkParameterIfIndex_Type = Integer32
_AccMultilinkParameterIfIndex_Object = MibTableColumn
accMultilinkParameterIfIndex = _AccMultilinkParameterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 2),
    _AccMultilinkParameterIfIndex_Type()
)
accMultilinkParameterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterIfIndex.setStatus("mandatory")


class _AccMultilinkParameterMessageLevel_Type(Integer32):
    """Custom type accMultilinkParameterMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccMultilinkParameterMessageLevel_Type.__name__ = "Integer32"
_AccMultilinkParameterMessageLevel_Object = MibTableColumn
accMultilinkParameterMessageLevel = _AccMultilinkParameterMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 3),
    _AccMultilinkParameterMessageLevel_Type()
)
accMultilinkParameterMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterMessageLevel.setStatus("mandatory")


class _AccMultilinkParameterAdminState_Type(Integer32):
    """Custom type accMultilinkParameterAdminState based on Integer32"""
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


_AccMultilinkParameterAdminState_Type.__name__ = "Integer32"
_AccMultilinkParameterAdminState_Object = MibTableColumn
accMultilinkParameterAdminState = _AccMultilinkParameterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 5),
    _AccMultilinkParameterAdminState_Type()
)
accMultilinkParameterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterAdminState.setStatus("mandatory")


class _AccMultilinkParameterOperState_Type(Integer32):
    """Custom type accMultilinkParameterOperState based on Integer32"""
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
        *(("disabled", 6),
          ("down", 1),
          ("seq-received-ok", 3),
          ("seq-send-ok", 4),
          ("starting", 2),
          ("up", 5))
    )


_AccMultilinkParameterOperState_Type.__name__ = "Integer32"
_AccMultilinkParameterOperState_Object = MibTableColumn
accMultilinkParameterOperState = _AccMultilinkParameterOperState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 6),
    _AccMultilinkParameterOperState_Type()
)
accMultilinkParameterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkParameterOperState.setStatus("mandatory")


class _AccMultilinkParameterEncapsulation_Type(Integer32):
    """Custom type accMultilinkParameterEncapsulation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acc", 1),
          ("acc-new", 3),
          ("ietf-ppp", 2))
    )


_AccMultilinkParameterEncapsulation_Type.__name__ = "Integer32"
_AccMultilinkParameterEncapsulation_Object = MibTableColumn
accMultilinkParameterEncapsulation = _AccMultilinkParameterEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 7),
    _AccMultilinkParameterEncapsulation_Type()
)
accMultilinkParameterEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterEncapsulation.setStatus("mandatory")
_AccMultilinkParameterPhysicalPort_Type = DisplayString
_AccMultilinkParameterPhysicalPort_Object = MibTableColumn
accMultilinkParameterPhysicalPort = _AccMultilinkParameterPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 9),
    _AccMultilinkParameterPhysicalPort_Type()
)
accMultilinkParameterPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkParameterPhysicalPort.setStatus("mandatory")
_AccMlTable_Object = MibTable
accMlTable = _AccMlTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    accMlTable.setStatus("mandatory")
_AccMlEntry_Object = MibTableRow
accMlEntry = _AccMlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2, 1)
)
accMlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accMlEntry.setStatus("mandatory")


class _AccMlAdminStatus_Type(Integer32):
    """Custom type accMlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("undefined", 3))
    )


_AccMlAdminStatus_Type.__name__ = "Integer32"
_AccMlAdminStatus_Object = MibTableColumn
accMlAdminStatus = _AccMlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2, 1, 7),
    _AccMlAdminStatus_Type()
)
accMlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlAdminStatus.setStatus("mandatory")
_AccMultilinkStatTable_Object = MibTable
accMultilinkStatTable = _AccMultilinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    accMultilinkStatTable.setStatus("mandatory")
_AccMultilinkStatEntry_Object = MibTableRow
accMultilinkStatEntry = _AccMultilinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1)
)
accMultilinkStatEntry.setIndexNames(
    (0, "ACC-MIB", "accMultilinkStatIndex"),
)
if mibBuilder.loadTexts:
    accMultilinkStatEntry.setStatus("mandatory")
_AccMultilinkStatIndex_Type = Integer32
_AccMultilinkStatIndex_Object = MibTableColumn
accMultilinkStatIndex = _AccMultilinkStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 1),
    _AccMultilinkStatIndex_Type()
)
accMultilinkStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatIndex.setStatus("mandatory")
_AccMultilinkStatRcvInSeqs_Type = Counter32
_AccMultilinkStatRcvInSeqs_Object = MibTableColumn
accMultilinkStatRcvInSeqs = _AccMultilinkStatRcvInSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 2),
    _AccMultilinkStatRcvInSeqs_Type()
)
accMultilinkStatRcvInSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvInSeqs.setStatus("mandatory")
_AccMultilinkStatRcvOutSeqs_Type = Counter32
_AccMultilinkStatRcvOutSeqs_Object = MibTableColumn
accMultilinkStatRcvOutSeqs = _AccMultilinkStatRcvOutSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 3),
    _AccMultilinkStatRcvOutSeqs_Type()
)
accMultilinkStatRcvOutSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvOutSeqs.setStatus("mandatory")
_AccMultilinkStatRcvOutWindows_Type = Counter32
_AccMultilinkStatRcvOutWindows_Object = MibTableColumn
accMultilinkStatRcvOutWindows = _AccMultilinkStatRcvOutWindows_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 4),
    _AccMultilinkStatRcvOutWindows_Type()
)
accMultilinkStatRcvOutWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvOutWindows.setStatus("mandatory")
_AccMultilinkStatRcvSeqBreaks_Type = Counter32
_AccMultilinkStatRcvSeqBreaks_Object = MibTableColumn
accMultilinkStatRcvSeqBreaks = _AccMultilinkStatRcvSeqBreaks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 5),
    _AccMultilinkStatRcvSeqBreaks_Type()
)
accMultilinkStatRcvSeqBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvSeqBreaks.setStatus("mandatory")
_AccMultilinkStatRcvWrongEncaps_Type = Counter32
_AccMultilinkStatRcvWrongEncaps_Object = MibTableColumn
accMultilinkStatRcvWrongEncaps = _AccMultilinkStatRcvWrongEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 6),
    _AccMultilinkStatRcvWrongEncaps_Type()
)
accMultilinkStatRcvWrongEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvWrongEncaps.setStatus("mandatory")
_AccMultilinkStatRcvPendings_Type = Counter32
_AccMultilinkStatRcvPendings_Object = MibTableColumn
accMultilinkStatRcvPendings = _AccMultilinkStatRcvPendings_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 7),
    _AccMultilinkStatRcvPendings_Type()
)
accMultilinkStatRcvPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvPendings.setStatus("mandatory")
_AccMultilinkStatRcvRingColls_Type = Counter32
_AccMultilinkStatRcvRingColls_Object = MibTableColumn
accMultilinkStatRcvRingColls = _AccMultilinkStatRcvRingColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 8),
    _AccMultilinkStatRcvRingColls_Type()
)
accMultilinkStatRcvRingColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvRingColls.setStatus("mandatory")
_AccMultilinkStatSendEncapFails_Type = Counter32
_AccMultilinkStatSendEncapFails_Object = MibTableColumn
accMultilinkStatSendEncapFails = _AccMultilinkStatSendEncapFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 9),
    _AccMultilinkStatSendEncapFails_Type()
)
accMultilinkStatSendEncapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendEncapFails.setStatus("mandatory")
_AccMultilinkStackTable_Object = MibTable
accMultilinkStackTable = _AccMultilinkStackTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    accMultilinkStackTable.setStatus("mandatory")
_AccMultilinkStackEntry_Object = MibTableRow
accMultilinkStackEntry = _AccMultilinkStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1)
)
accMultilinkStackEntry.setIndexNames(
    (0, "ACC-MIB", "accMultilinkStackGroup"),
    (0, "ACC-MIB", "accMultilinkStackInterface"),
)
if mibBuilder.loadTexts:
    accMultilinkStackEntry.setStatus("mandatory")
_AccMultilinkStackGroup_Type = Integer32
_AccMultilinkStackGroup_Object = MibTableColumn
accMultilinkStackGroup = _AccMultilinkStackGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1, 1),
    _AccMultilinkStackGroup_Type()
)
accMultilinkStackGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkStackGroup.setStatus("mandatory")
_AccMultilinkStackInterface_Type = Integer32
_AccMultilinkStackInterface_Object = MibTableColumn
accMultilinkStackInterface = _AccMultilinkStackInterface_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1, 2),
    _AccMultilinkStackInterface_Type()
)
accMultilinkStackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkStackInterface.setStatus("mandatory")
_AccAsPort_ObjectIdentity = ObjectIdentity
accAsPort = _AccAsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10)
)
_AccConsole_ObjectIdentity = ObjectIdentity
accConsole = _AccConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2)
)
_AccConsoleParms_ObjectIdentity = ObjectIdentity
accConsoleParms = _AccConsoleParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1)
)
_AccConsoleSpeed_Type = Integer32
_AccConsoleSpeed_Object = MibScalar
accConsoleSpeed = _AccConsoleSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 10, 2, 1, 5),
    _AccConsoleSpeed_Type()
)
accConsoleSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accConsoleSpeed.setStatus("mandatory")
_AccArp_ObjectIdentity = ObjectIdentity
accArp = _AccArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11)
)


class _AccArpTimeout_Type(Integer32):
    """Custom type accArpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AccArpTimeout_Type.__name__ = "Integer32"
_AccArpTimeout_Object = MibScalar
accArpTimeout = _AccArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 1),
    _AccArpTimeout_Type()
)
accArpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpTimeout.setStatus("mandatory")
_AccArpTable_Object = MibTable
accArpTable = _AccArpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    accArpTable.setStatus("mandatory")
_AccArpEntry_Object = MibTableRow
accArpEntry = _AccArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1)
)
accArpEntry.setIndexNames(
    (0, "ACC-MIB", "accArpNetAddress"),
)
if mibBuilder.loadTexts:
    accArpEntry.setStatus("mandatory")


class _AccArpPhysAddress_Type(OctetString):
    """Custom type accArpPhysAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccArpPhysAddress_Type.__name__ = "OctetString"
_AccArpPhysAddress_Object = MibTableColumn
accArpPhysAddress = _AccArpPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 1),
    _AccArpPhysAddress_Type()
)
accArpPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpPhysAddress.setStatus("mandatory")
_AccArpNetAddress_Type = IpAddress
_AccArpNetAddress_Object = MibTableColumn
accArpNetAddress = _AccArpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 2),
    _AccArpNetAddress_Type()
)
accArpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpNetAddress.setStatus("mandatory")


class _AccArpEntStatus_Type(Integer32):
    """Custom type accArpEntStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("apepending", 16),
          ("confirmpending", 64),
          ("confirmsrpending", 128),
          ("dynamic", 2),
          ("ourbox", 4),
          ("pending", 1),
          ("permanent", 8),
          ("stepending", 32))
    )


_AccArpEntStatus_Type.__name__ = "Integer32"
_AccArpEntStatus_Object = MibTableColumn
accArpEntStatus = _AccArpEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 2, 1, 3),
    _AccArpEntStatus_Type()
)
accArpEntStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpEntStatus.setStatus("mandatory")


class _AccArpType_Type(Integer32):
    """Custom type accArpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AccArpType_Type.__name__ = "Integer32"
_AccArpType_Object = MibScalar
accArpType = _AccArpType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 3),
    _AccArpType_Type()
)
accArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpType.setStatus("mandatory")
_AccArpReqRcvds_Type = Counter32
_AccArpReqRcvds_Object = MibScalar
accArpReqRcvds = _AccArpReqRcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 4),
    _AccArpReqRcvds_Type()
)
accArpReqRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpReqRcvds.setStatus("mandatory")
_AccArpReqSents_Type = Counter32
_AccArpReqSents_Object = MibScalar
accArpReqSents = _AccArpReqSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 5),
    _AccArpReqSents_Type()
)
accArpReqSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpReqSents.setStatus("mandatory")
_AccArpRspRcvds_Type = Counter32
_AccArpRspRcvds_Object = MibScalar
accArpRspRcvds = _AccArpRspRcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 6),
    _AccArpRspRcvds_Type()
)
accArpRspRcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpRspRcvds.setStatus("mandatory")
_AccArpRspSents_Type = Counter32
_AccArpRspSents_Object = MibScalar
accArpRspSents = _AccArpRspSents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 7),
    _AccArpRspSents_Type()
)
accArpRspSents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpRspSents.setStatus("mandatory")
_AccArpInErrs_Type = Counter32
_AccArpInErrs_Object = MibScalar
accArpInErrs = _AccArpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 8),
    _AccArpInErrs_Type()
)
accArpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpInErrs.setStatus("mandatory")
_AccArpOutErrs_Type = Counter32
_AccArpOutErrs_Object = MibScalar
accArpOutErrs = _AccArpOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 9),
    _AccArpOutErrs_Type()
)
accArpOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpOutErrs.setStatus("mandatory")
_AccArpUnknownProtos_Type = Counter32
_AccArpUnknownProtos_Object = MibScalar
accArpUnknownProtos = _AccArpUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 10),
    _AccArpUnknownProtos_Type()
)
accArpUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accArpUnknownProtos.setStatus("mandatory")


class _AccArpPromiscuous_Type(Integer32):
    """Custom type accArpPromiscuous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonpromiscuous", 2),
          ("promiscuous", 1))
    )


_AccArpPromiscuous_Type.__name__ = "Integer32"
_AccArpPromiscuous_Object = MibScalar
accArpPromiscuous = _AccArpPromiscuous_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 11),
    _AccArpPromiscuous_Type()
)
accArpPromiscuous.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpPromiscuous.setStatus("mandatory")


class _AccArpRefresh_Type(Integer32):
    """Custom type accArpRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norefresh", 2),
          ("refresh", 1))
    )


_AccArpRefresh_Type.__name__ = "Integer32"
_AccArpRefresh_Object = MibScalar
accArpRefresh = _AccArpRefresh_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 11, 12),
    _AccArpRefresh_Type()
)
accArpRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accArpRefresh.setStatus("mandatory")
_AccIpRoutingTable_Object = MibTable
accIpRoutingTable = _AccIpRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    accIpRoutingTable.setStatus("mandatory")
_AccIpRoutingEntry_Object = MibTableRow
accIpRoutingEntry = _AccIpRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12, 1)
)
accIpRoutingEntry.setIndexNames(
    (0, "RFC1213-MIB", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    accIpRoutingEntry.setStatus("mandatory")
_AccIpRouteDestSubnet_Type = IpAddress
_AccIpRouteDestSubnet_Object = MibTableColumn
accIpRouteDestSubnet = _AccIpRouteDestSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 12, 1, 2),
    _AccIpRouteDestSubnet_Type()
)
accIpRouteDestSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpRouteDestSubnet.setStatus("mandatory")
_AccProbe_ObjectIdentity = ObjectIdentity
accProbe = _AccProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 13)
)
_AccProbeAddr_Type = OctetString
_AccProbeAddr_Object = MibScalar
accProbeAddr = _AccProbeAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 13, 1),
    _AccProbeAddr_Type()
)
accProbeAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accProbeAddr.setStatus("mandatory")
_AccProbeData_Type = Integer32
_AccProbeData_Object = MibScalar
accProbeData = _AccProbeData_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 13, 2),
    _AccProbeData_Type()
)
accProbeData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accProbeData.setStatus("mandatory")
_AccIpAddrTable_Object = MibTable
accIpAddrTable = _AccIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    accIpAddrTable.setStatus("mandatory")
_AccIpAddrEntry_Object = MibTableRow
accIpAddrEntry = _AccIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1)
)
accIpAddrEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    accIpAddrEntry.setStatus("mandatory")
_AccIpAddrMtu_Type = Integer32
_AccIpAddrMtu_Object = MibTableColumn
accIpAddrMtu = _AccIpAddrMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 1),
    _AccIpAddrMtu_Type()
)
accIpAddrMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAddrMtu.setStatus("mandatory")


class _AccIpAddrSecurityType_Type(Integer32):
    """Custom type accIpAddrSecurityType based on Integer32"""
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
        *(("basic", 2),
          ("none", 1),
          ("strip", 3))
    )


_AccIpAddrSecurityType_Type.__name__ = "Integer32"
_AccIpAddrSecurityType_Object = MibTableColumn
accIpAddrSecurityType = _AccIpAddrSecurityType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 2),
    _AccIpAddrSecurityType_Type()
)
accIpAddrSecurityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAddrSecurityType.setStatus("mandatory")
_AccIpAddrSecurityClass_Type = Integer32
_AccIpAddrSecurityClass_Object = MibTableColumn
accIpAddrSecurityClass = _AccIpAddrSecurityClass_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 3),
    _AccIpAddrSecurityClass_Type()
)
accIpAddrSecurityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAddrSecurityClass.setStatus("mandatory")
_AccIpAddrSecurityAuth_Type = OctetString
_AccIpAddrSecurityAuth_Object = MibTableColumn
accIpAddrSecurityAuth = _AccIpAddrSecurityAuth_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 4),
    _AccIpAddrSecurityAuth_Type()
)
accIpAddrSecurityAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAddrSecurityAuth.setStatus("mandatory")
_AccIpAddrBcastAddr_Type = IpAddress
_AccIpAddrBcastAddr_Object = MibTableColumn
accIpAddrBcastAddr = _AccIpAddrBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 5),
    _AccIpAddrBcastAddr_Type()
)
accIpAddrBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAddrBcastAddr.setStatus("mandatory")


class _AccIpAdEntMetric_Type(Integer32):
    """Custom type accIpAdEntMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AccIpAdEntMetric_Type.__name__ = "Integer32"
_AccIpAdEntMetric_Object = MibTableColumn
accIpAdEntMetric = _AccIpAdEntMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 6),
    _AccIpAdEntMetric_Type()
)
accIpAdEntMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAdEntMetric.setStatus("mandatory")


class _AccIpAdEntPreference_Type(Integer32):
    """Custom type accIpAdEntPreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 1))
    )


_AccIpAdEntPreference_Type.__name__ = "Integer32"
_AccIpAdEntPreference_Object = MibTableColumn
accIpAdEntPreference = _AccIpAdEntPreference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 14, 1, 7),
    _AccIpAdEntPreference_Type()
)
accIpAdEntPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpAdEntPreference.setStatus("mandatory")
_AccEgp_ObjectIdentity = ObjectIdentity
accEgp = _AccEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15)
)
_AccEgpNeighTable_Object = MibTable
accEgpNeighTable = _AccEgpNeighTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    accEgpNeighTable.setStatus("mandatory")
_AccEgpNeighEntry_Object = MibTableRow
accEgpNeighEntry = _AccEgpNeighEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1, 1)
)
accEgpNeighEntry.setIndexNames(
    (0, "RFC1213-MIB", "egpNeighAddr"),
)
if mibBuilder.loadTexts:
    accEgpNeighEntry.setStatus("mandatory")
_AccEgpUptime_Type = TimeTicks
_AccEgpUptime_Object = MibTableColumn
accEgpUptime = _AccEgpUptime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1, 1, 1),
    _AccEgpUptime_Type()
)
accEgpUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpUptime.setStatus("mandatory")
_AccEgpFAS_Type = Integer32
_AccEgpFAS_Object = MibTableColumn
accEgpFAS = _AccEgpFAS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1, 1, 2),
    _AccEgpFAS_Type()
)
accEgpFAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpFAS.setStatus("mandatory")
_AccEgpSndSeqs_Type = Counter32
_AccEgpSndSeqs_Object = MibTableColumn
accEgpSndSeqs = _AccEgpSndSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1, 1, 3),
    _AccEgpSndSeqs_Type()
)
accEgpSndSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpSndSeqs.setStatus("mandatory")
_AccEgpRcvSeqs_Type = Counter32
_AccEgpRcvSeqs_Object = MibTableColumn
accEgpRcvSeqs = _AccEgpRcvSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 1, 1, 4),
    _AccEgpRcvSeqs_Type()
)
accEgpRcvSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpRcvSeqs.setStatus("mandatory")


class _AccEgpAdminStatus_Type(Integer32):
    """Custom type accEgpAdminStatus based on Integer32"""
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


_AccEgpAdminStatus_Type.__name__ = "Integer32"
_AccEgpAdminStatus_Object = MibScalar
accEgpAdminStatus = _AccEgpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 2),
    _AccEgpAdminStatus_Type()
)
accEgpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEgpAdminStatus.setStatus("mandatory")


class _AccEgpASNumber_Type(Integer32):
    """Custom type accEgpASNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccEgpASNumber_Type.__name__ = "Integer32"
_AccEgpASNumber_Object = MibScalar
accEgpASNumber = _AccEgpASNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 3),
    _AccEgpASNumber_Type()
)
accEgpASNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEgpASNumber.setStatus("mandatory")


class _AccEgpMetric_Type(Integer32):
    """Custom type accEgpMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccEgpMetric_Type.__name__ = "Integer32"
_AccEgpMetric_Object = MibScalar
accEgpMetric = _AccEgpMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 4),
    _AccEgpMetric_Type()
)
accEgpMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEgpMetric.setStatus("mandatory")
_AccEgpInErrMsgs_Type = Counter32
_AccEgpInErrMsgs_Object = MibScalar
accEgpInErrMsgs = _AccEgpInErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 5),
    _AccEgpInErrMsgs_Type()
)
accEgpInErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpInErrMsgs.setStatus("mandatory")
_AccEgpOutErrMsgs_Type = Counter32
_AccEgpOutErrMsgs_Object = MibScalar
accEgpOutErrMsgs = _AccEgpOutErrMsgs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 6),
    _AccEgpOutErrMsgs_Type()
)
accEgpOutErrMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpOutErrMsgs.setStatus("mandatory")
_AccEgpStateChanges_Type = Counter32
_AccEgpStateChanges_Object = MibScalar
accEgpStateChanges = _AccEgpStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 7),
    _AccEgpStateChanges_Type()
)
accEgpStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpStateChanges.setStatus("mandatory")
_AccEgpLastChange_Type = TimeTicks
_AccEgpLastChange_Object = MibScalar
accEgpLastChange = _AccEgpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 15, 8),
    _AccEgpLastChange_Type()
)
accEgpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEgpLastChange.setStatus("mandatory")
_AccRip_ObjectIdentity = ObjectIdentity
accRip = _AccRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16)
)


class _AccRipAdminStatus_Type(Integer32):
    """Custom type accRipAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extended", 3),
          ("off", 2),
          ("on", 1))
    )


_AccRipAdminStatus_Type.__name__ = "Integer32"
_AccRipAdminStatus_Object = MibScalar
accRipAdminStatus = _AccRipAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 1),
    _AccRipAdminStatus_Type()
)
accRipAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipAdminStatus.setStatus("mandatory")
_AccRipUpdateTimer_Type = TimeTicks
_AccRipUpdateTimer_Object = MibScalar
accRipUpdateTimer = _AccRipUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 2),
    _AccRipUpdateTimer_Type()
)
accRipUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipUpdateTimer.setStatus("mandatory")


class _AccRipGateway_Type(Integer32):
    """Custom type accRipGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extended", 3),
          ("off", 2),
          ("on", 1))
    )


_AccRipGateway_Type.__name__ = "Integer32"
_AccRipGateway_Object = MibScalar
accRipGateway = _AccRipGateway_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 3),
    _AccRipGateway_Type()
)
accRipGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipGateway.setStatus("mandatory")


class _AccRipMetric_Type(Integer32):
    """Custom type accRipMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AccRipMetric_Type.__name__ = "Integer32"
_AccRipMetric_Object = MibScalar
accRipMetric = _AccRipMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 4),
    _AccRipMetric_Type()
)
accRipMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipMetric.setStatus("mandatory")
_AccRipNeighborList_ObjectIdentity = ObjectIdentity
accRipNeighborList = _AccRipNeighborList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5)
)
_AccRipNeighbor_Type = IpAddress
_AccRipNeighbor_Object = MibScalar
accRipNeighbor = _AccRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5, 1),
    _AccRipNeighbor_Type()
)
accRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRipNeighbor.setStatus("mandatory")
_AccRipNeighborIfindex_Type = Integer32
_AccRipNeighborIfindex_Object = MibScalar
accRipNeighborIfindex = _AccRipNeighborIfindex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 5, 2),
    _AccRipNeighborIfindex_Type()
)
accRipNeighborIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipNeighborIfindex.setStatus("mandatory")
_AccRipInCmdCnts_Type = Counter32
_AccRipInCmdCnts_Object = MibScalar
accRipInCmdCnts = _AccRipInCmdCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 6),
    _AccRipInCmdCnts_Type()
)
accRipInCmdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInCmdCnts.setStatus("mandatory")
_AccRipInRspCnts_Type = Counter32
_AccRipInRspCnts_Object = MibScalar
accRipInRspCnts = _AccRipInRspCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 7),
    _AccRipInRspCnts_Type()
)
accRipInRspCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInRspCnts.setStatus("mandatory")
_AccRipInErrors_Type = Counter32
_AccRipInErrors_Object = MibScalar
accRipInErrors = _AccRipInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 8),
    _AccRipInErrors_Type()
)
accRipInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipInErrors.setStatus("mandatory")
_AccRipOutCmdCnts_Type = Counter32
_AccRipOutCmdCnts_Object = MibScalar
accRipOutCmdCnts = _AccRipOutCmdCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 9),
    _AccRipOutCmdCnts_Type()
)
accRipOutCmdCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipOutCmdCnts.setStatus("mandatory")
_AccRipOutRspCounts_Type = Counter32
_AccRipOutRspCounts_Object = MibScalar
accRipOutRspCounts = _AccRipOutRspCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 16, 10),
    _AccRipOutRspCounts_Type()
)
accRipOutRspCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accRipOutRspCounts.setStatus("mandatory")
_AccX25_ObjectIdentity = ObjectIdentity
accX25 = _AccX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17)
)
_AccX25AtTable_Object = MibTable
accX25AtTable = _AccX25AtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1)
)
if mibBuilder.loadTexts:
    accX25AtTable.setStatus("mandatory")
_AccX25AtEntry_Object = MibTableRow
accX25AtEntry = _AccX25AtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1)
)
accX25AtEntry.setIndexNames(
    (0, "ACC-MIB", "accX25AtIfIndex"),
    (0, "ACC-MIB", "accX25AtIpAddress"),
)
if mibBuilder.loadTexts:
    accX25AtEntry.setStatus("mandatory")
_AccX25AtIfIndex_Type = Integer32
_AccX25AtIfIndex_Object = MibTableColumn
accX25AtIfIndex = _AccX25AtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 1),
    _AccX25AtIfIndex_Type()
)
accX25AtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtIfIndex.setStatus("mandatory")
_AccX25AtIpAddress_Type = IpAddress
_AccX25AtIpAddress_Object = MibTableColumn
accX25AtIpAddress = _AccX25AtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 2),
    _AccX25AtIpAddress_Type()
)
accX25AtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtIpAddress.setStatus("mandatory")
_AccX25AtNetInOutAddr_Type = DisplayString
_AccX25AtNetInOutAddr_Object = MibTableColumn
accX25AtNetInOutAddr = _AccX25AtNetInOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 3),
    _AccX25AtNetInOutAddr_Type()
)
accX25AtNetInOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetInOutAddr.setStatus("mandatory")
_AccX25AtNetInAddr_Type = DisplayString
_AccX25AtNetInAddr_Object = MibTableColumn
accX25AtNetInAddr = _AccX25AtNetInAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 4),
    _AccX25AtNetInAddr_Type()
)
accX25AtNetInAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetInAddr.setStatus("mandatory")


class _AccX25AtNetFacIndex_Type(Integer32):
    """Custom type accX25AtNetFacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccX25AtNetFacIndex_Type.__name__ = "Integer32"
_AccX25AtNetFacIndex_Object = MibTableColumn
accX25AtNetFacIndex = _AccX25AtNetFacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 1, 1, 5),
    _AccX25AtNetFacIndex_Type()
)
accX25AtNetFacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AtNetFacIndex.setStatus("mandatory")
_AccX25SubnetParmTable_Object = MibTable
accX25SubnetParmTable = _AccX25SubnetParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2)
)
if mibBuilder.loadTexts:
    accX25SubnetParmTable.setStatus("mandatory")
_AccX25SubnetParmEntry_Object = MibTableRow
accX25SubnetParmEntry = _AccX25SubnetParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1)
)
accX25SubnetParmEntry.setIndexNames(
    (0, "ACC-MIB", "accX25SubnetAddr"),
)
if mibBuilder.loadTexts:
    accX25SubnetParmEntry.setStatus("mandatory")
_AccX25SubnetAddr_Type = IpAddress
_AccX25SubnetAddr_Object = MibTableColumn
accX25SubnetAddr = _AccX25SubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 1),
    _AccX25SubnetAddr_Type()
)
accX25SubnetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SubnetAddr.setStatus("mandatory")


class _AccX25Facility_Type(Integer32):
    """Custom type accX25Facility based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("std", 2))
    )


_AccX25Facility_Type.__name__ = "Integer32"
_AccX25Facility_Object = MibTableColumn
accX25Facility = _AccX25Facility_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 2),
    _AccX25Facility_Type()
)
accX25Facility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Facility.setStatus("mandatory")


class _AccX25PktNegot_Type(Integer32):
    """Custom type accX25PktNegot based on Integer32"""
    defaultValue = 0


_AccX25PktNegot_Object = MibTableColumn
accX25PktNegot = _AccX25PktNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 3),
    _AccX25PktNegot_Type()
)
accX25PktNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktNegot.setStatus("mandatory")


class _AccX25WindowNegot_Type(Integer32):
    """Custom type accX25WindowNegot based on Integer32"""
    defaultValue = 0


_AccX25WindowNegot_Object = MibTableColumn
accX25WindowNegot = _AccX25WindowNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 2, 1, 4),
    _AccX25WindowNegot_Type()
)
accX25WindowNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25WindowNegot.setStatus("mandatory")
_AccX25PortParmTable_Object = MibTable
accX25PortParmTable = _AccX25PortParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3)
)
if mibBuilder.loadTexts:
    accX25PortParmTable.setStatus("mandatory")
_AccX25PortParmEntry_Object = MibTableRow
accX25PortParmEntry = _AccX25PortParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1)
)
accX25PortParmEntry.setIndexNames(
    (0, "ACC-MIB", "accX25PortParmIndex"),
)
if mibBuilder.loadTexts:
    accX25PortParmEntry.setStatus("mandatory")
_AccX25PortParmIndex_Type = Integer32
_AccX25PortParmIndex_Object = MibTableColumn
accX25PortParmIndex = _AccX25PortParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 1),
    _AccX25PortParmIndex_Type()
)
accX25PortParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25PortParmIndex.setStatus("mandatory")


class _AccX25AddrMode_Type(Integer32):
    """Custom type accX25AddrMode based on Integer32"""
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
        *(("bfe", 3),
          ("ddn", 2),
          ("table", 1))
    )


_AccX25AddrMode_Type.__name__ = "Integer32"
_AccX25AddrMode_Object = MibTableColumn
accX25AddrMode = _AccX25AddrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 2),
    _AccX25AddrMode_Type()
)
accX25AddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25AddrMode.setStatus("mandatory")


class _AccX25PktSize_Type(Integer32):
    """Custom type accX25PktSize based on Integer32"""
    defaultValue = 128


_AccX25PktSize_Object = MibTableColumn
accX25PktSize = _AccX25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 3),
    _AccX25PktSize_Type()
)
accX25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktSize.setStatus("mandatory")


class _AccX25PktWind_Type(Integer32):
    """Custom type accX25PktWind based on Integer32"""
    defaultValue = 2


_AccX25PktWind_Object = MibTableColumn
accX25PktWind = _AccX25PktWind_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 4),
    _AccX25PktWind_Type()
)
accX25PktWind.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PktWind.setStatus("mandatory")


class _AccX25SvcNumber_Type(Integer32):
    """Custom type accX25SvcNumber based on Integer32"""
    defaultValue = 256


_AccX25SvcNumber_Object = MibTableColumn
accX25SvcNumber = _AccX25SvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 5),
    _AccX25SvcNumber_Type()
)
accX25SvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcNumber.setStatus("mandatory")


class _AccX25SvcBase_Type(Integer32):
    """Custom type accX25SvcBase based on Integer32"""
    defaultValue = 1


_AccX25SvcBase_Object = MibTableColumn
accX25SvcBase = _AccX25SvcBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 6),
    _AccX25SvcBase_Type()
)
accX25SvcBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcBase.setStatus("mandatory")


class _AccX25ExtendClr_Type(Integer32):
    """Custom type accX25ExtendClr based on Integer32"""
    defaultValue = 2

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


_AccX25ExtendClr_Type.__name__ = "Integer32"
_AccX25ExtendClr_Object = MibTableColumn
accX25ExtendClr = _AccX25ExtendClr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 7),
    _AccX25ExtendClr_Type()
)
accX25ExtendClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25ExtendClr.setStatus("mandatory")


class _AccX25ExtendSeq_Type(Integer32):
    """Custom type accX25ExtendSeq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("normal", 1))
    )


_AccX25ExtendSeq_Type.__name__ = "Integer32"
_AccX25ExtendSeq_Object = MibTableColumn
accX25ExtendSeq = _AccX25ExtendSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 8),
    _AccX25ExtendSeq_Type()
)
accX25ExtendSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25ExtendSeq.setStatus("mandatory")


class _AccX25IdleMin_Type(TimeTicks):
    """Custom type accX25IdleMin based on TimeTicks"""
    defaultValue = 30000


_AccX25IdleMin_Object = MibTableColumn
accX25IdleMin = _AccX25IdleMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 9),
    _AccX25IdleMin_Type()
)
accX25IdleMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleMin.setStatus("mandatory")


class _AccX25IdleMax_Type(TimeTicks):
    """Custom type accX25IdleMax based on TimeTicks"""
    defaultValue = 180000


_AccX25IdleMax_Object = MibTableColumn
accX25IdleMax = _AccX25IdleMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 10),
    _AccX25IdleMax_Type()
)
accX25IdleMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleMax.setStatus("mandatory")


class _AccX25IdleScale_Type(TimeTicks):
    """Custom type accX25IdleScale based on TimeTicks"""
    defaultValue = 1000


_AccX25IdleScale_Object = MibTableColumn
accX25IdleScale = _AccX25IdleScale_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 11),
    _AccX25IdleScale_Type()
)
accX25IdleScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25IdleScale.setStatus("mandatory")


class _AccX25SvcMax_Type(Integer32):
    """Custom type accX25SvcMax based on Integer32"""
    defaultValue = 1


_AccX25SvcMax_Object = MibTableColumn
accX25SvcMax = _AccX25SvcMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 12),
    _AccX25SvcMax_Type()
)
accX25SvcMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcMax.setStatus("mandatory")


class _AccX25SvcLimit_Type(Integer32):
    """Custom type accX25SvcLimit based on Integer32"""
    defaultValue = 256


_AccX25SvcLimit_Object = MibTableColumn
accX25SvcLimit = _AccX25SvcLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 13),
    _AccX25SvcLimit_Type()
)
accX25SvcLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcLimit.setStatus("mandatory")


class _AccX25OpenThresh_Type(Integer32):
    """Custom type accX25OpenThresh based on Integer32"""
    defaultValue = 3


_AccX25OpenThresh_Object = MibTableColumn
accX25OpenThresh = _AccX25OpenThresh_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 14),
    _AccX25OpenThresh_Type()
)
accX25OpenThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OpenThresh.setStatus("mandatory")


class _AccX25SvcMin_Type(Integer32):
    """Custom type accX25SvcMin based on Integer32"""
    defaultValue = 0


_AccX25SvcMin_Object = MibTableColumn
accX25SvcMin = _AccX25SvcMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 15),
    _AccX25SvcMin_Type()
)
accX25SvcMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcMin.setStatus("mandatory")


class _AccX25SvcDelay_Type(Integer32):
    """Custom type accX25SvcDelay based on Integer32"""
    defaultValue = 5


_AccX25SvcDelay_Object = MibTableColumn
accX25SvcDelay = _AccX25SvcDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 16),
    _AccX25SvcDelay_Type()
)
accX25SvcDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SvcDelay.setStatus("mandatory")


class _AccX25InitBackoff_Type(Integer32):
    """Custom type accX25InitBackoff based on Integer32"""
    defaultValue = 15


_AccX25InitBackoff_Object = MibTableColumn
accX25InitBackoff = _AccX25InitBackoff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 17),
    _AccX25InitBackoff_Type()
)
accX25InitBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25InitBackoff.setStatus("mandatory")


class _AccX25MaxBackoff_Type(Integer32):
    """Custom type accX25MaxBackoff based on Integer32"""
    defaultValue = 86400


_AccX25MaxBackoff_Object = MibTableColumn
accX25MaxBackoff = _AccX25MaxBackoff_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 18),
    _AccX25MaxBackoff_Type()
)
accX25MaxBackoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25MaxBackoff.setStatus("mandatory")


class _AccX25OurAddress_Type(DisplayString):
    """Custom type accX25OurAddress based on DisplayString"""
    defaultHexValue = "0"


_AccX25OurAddress_Object = MibTableColumn
accX25OurAddress = _AccX25OurAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 19),
    _AccX25OurAddress_Type()
)
accX25OurAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OurAddress.setStatus("mandatory")


class _AccX25PvcBase_Type(Integer32):
    """Custom type accX25PvcBase based on Integer32"""
    defaultValue = 0


_AccX25PvcBase_Object = MibTableColumn
accX25PvcBase = _AccX25PvcBase_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 20),
    _AccX25PvcBase_Type()
)
accX25PvcBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcBase.setStatus("mandatory")


class _AccX25PvcNumber_Type(Integer32):
    """Custom type accX25PvcNumber based on Integer32"""
    defaultValue = 0


_AccX25PvcNumber_Object = MibTableColumn
accX25PvcNumber = _AccX25PvcNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 21),
    _AccX25PvcNumber_Type()
)
accX25PvcNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcNumber.setStatus("mandatory")


class _AccX25Tx0Timer_Type(TimeTicks):
    """Custom type accX25Tx0Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx0Timer_Object = MibTableColumn
accX25Tx0Timer = _AccX25Tx0Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 22),
    _AccX25Tx0Timer_Type()
)
accX25Tx0Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx0Timer.setStatus("mandatory")


class _AccX25Tx1Timer_Type(TimeTicks):
    """Custom type accX25Tx1Timer based on TimeTicks"""
    defaultValue = 20000


_AccX25Tx1Timer_Object = MibTableColumn
accX25Tx1Timer = _AccX25Tx1Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 23),
    _AccX25Tx1Timer_Type()
)
accX25Tx1Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx1Timer.setStatus("mandatory")


class _AccX25Tx2Timer_Type(TimeTicks):
    """Custom type accX25Tx2Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx2Timer_Object = MibTableColumn
accX25Tx2Timer = _AccX25Tx2Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 24),
    _AccX25Tx2Timer_Type()
)
accX25Tx2Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx2Timer.setStatus("mandatory")


class _AccX25Tx3Timer_Type(TimeTicks):
    """Custom type accX25Tx3Timer based on TimeTicks"""
    defaultValue = 18000


_AccX25Tx3Timer_Object = MibTableColumn
accX25Tx3Timer = _AccX25Tx3Timer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 3, 1, 25),
    _AccX25Tx3Timer_Type()
)
accX25Tx3Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25Tx3Timer.setStatus("mandatory")
_AccX25PktStatTable_Object = MibTable
accX25PktStatTable = _AccX25PktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4)
)
if mibBuilder.loadTexts:
    accX25PktStatTable.setStatus("mandatory")
_AccX25PktStatEntry_Object = MibTableRow
accX25PktStatEntry = _AccX25PktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1)
)
accX25PktStatEntry.setIndexNames(
    (0, "ACC-MIB", "accX25PktIndex"),
)
if mibBuilder.loadTexts:
    accX25PktStatEntry.setStatus("mandatory")
_AccX25PktIndex_Type = Integer32
_AccX25PktIndex_Object = MibTableColumn
accX25PktIndex = _AccX25PktIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 1),
    _AccX25PktIndex_Type()
)
accX25PktIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25PktIndex.setStatus("mandatory")
_AccX25RcvDiags_Type = Counter32
_AccX25RcvDiags_Object = MibTableColumn
accX25RcvDiags = _AccX25RcvDiags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 2),
    _AccX25RcvDiags_Type()
)
accX25RcvDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvDiags.setStatus("mandatory")
_AccX25RcvRestartReqs_Type = Counter32
_AccX25RcvRestartReqs_Object = MibTableColumn
accX25RcvRestartReqs = _AccX25RcvRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 3),
    _AccX25RcvRestartReqs_Type()
)
accX25RcvRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRestartReqs.setStatus("mandatory")
_AccX25RcvRestartConfs_Type = Counter32
_AccX25RcvRestartConfs_Object = MibTableColumn
accX25RcvRestartConfs = _AccX25RcvRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 4),
    _AccX25RcvRestartConfs_Type()
)
accX25RcvRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRestartConfs.setStatus("mandatory")
_AccX25RcvCallReqs_Type = Counter32
_AccX25RcvCallReqs_Object = MibTableColumn
accX25RcvCallReqs = _AccX25RcvCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 5),
    _AccX25RcvCallReqs_Type()
)
accX25RcvCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvCallReqs.setStatus("mandatory")
_AccX25RcvCallAccs_Type = Counter32
_AccX25RcvCallAccs_Object = MibTableColumn
accX25RcvCallAccs = _AccX25RcvCallAccs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 6),
    _AccX25RcvCallAccs_Type()
)
accX25RcvCallAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvCallAccs.setStatus("mandatory")
_AccX25RcvClrReqs_Type = Counter32
_AccX25RcvClrReqs_Object = MibTableColumn
accX25RcvClrReqs = _AccX25RcvClrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 7),
    _AccX25RcvClrReqs_Type()
)
accX25RcvClrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvClrReqs.setStatus("mandatory")
_AccX25RcvClrConfs_Type = Counter32
_AccX25RcvClrConfs_Object = MibTableColumn
accX25RcvClrConfs = _AccX25RcvClrConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 8),
    _AccX25RcvClrConfs_Type()
)
accX25RcvClrConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvClrConfs.setStatus("mandatory")
_AccX25RcvResetReqs_Type = Counter32
_AccX25RcvResetReqs_Object = MibTableColumn
accX25RcvResetReqs = _AccX25RcvResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 9),
    _AccX25RcvResetReqs_Type()
)
accX25RcvResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvResetReqs.setStatus("mandatory")
_AccX25RcvResetConfs_Type = Counter32
_AccX25RcvResetConfs_Object = MibTableColumn
accX25RcvResetConfs = _AccX25RcvResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 10),
    _AccX25RcvResetConfs_Type()
)
accX25RcvResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvResetConfs.setStatus("mandatory")
_AccX25RcvInts_Type = Counter32
_AccX25RcvInts_Object = MibTableColumn
accX25RcvInts = _AccX25RcvInts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 11),
    _AccX25RcvInts_Type()
)
accX25RcvInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvInts.setStatus("mandatory")
_AccX25RcvIntConfs_Type = Counter32
_AccX25RcvIntConfs_Object = MibTableColumn
accX25RcvIntConfs = _AccX25RcvIntConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 12),
    _AccX25RcvIntConfs_Type()
)
accX25RcvIntConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvIntConfs.setStatus("mandatory")
_AccX25RcvRRs_Type = Counter32
_AccX25RcvRRs_Object = MibTableColumn
accX25RcvRRs = _AccX25RcvRRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 13),
    _AccX25RcvRRs_Type()
)
accX25RcvRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRRs.setStatus("mandatory")
_AccX25RcvRNRs_Type = Counter32
_AccX25RcvRNRs_Object = MibTableColumn
accX25RcvRNRs = _AccX25RcvRNRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 14),
    _AccX25RcvRNRs_Type()
)
accX25RcvRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvRNRs.setStatus("mandatory")
_AccX25RcvDatas_Type = Counter32
_AccX25RcvDatas_Object = MibTableColumn
accX25RcvDatas = _AccX25RcvDatas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 15),
    _AccX25RcvDatas_Type()
)
accX25RcvDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25RcvDatas.setStatus("mandatory")
_AccX25XmtDiags_Type = Counter32
_AccX25XmtDiags_Object = MibTableColumn
accX25XmtDiags = _AccX25XmtDiags_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 16),
    _AccX25XmtDiags_Type()
)
accX25XmtDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtDiags.setStatus("mandatory")
_AccX25XmtRestartReqs_Type = Counter32
_AccX25XmtRestartReqs_Object = MibTableColumn
accX25XmtRestartReqs = _AccX25XmtRestartReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 17),
    _AccX25XmtRestartReqs_Type()
)
accX25XmtRestartReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRestartReqs.setStatus("mandatory")
_AccX25XmtRestartConfs_Type = Counter32
_AccX25XmtRestartConfs_Object = MibTableColumn
accX25XmtRestartConfs = _AccX25XmtRestartConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 18),
    _AccX25XmtRestartConfs_Type()
)
accX25XmtRestartConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRestartConfs.setStatus("mandatory")
_AccX25XmtCallReqs_Type = Counter32
_AccX25XmtCallReqs_Object = MibTableColumn
accX25XmtCallReqs = _AccX25XmtCallReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 19),
    _AccX25XmtCallReqs_Type()
)
accX25XmtCallReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtCallReqs.setStatus("mandatory")
_AccX25XmtCallAccs_Type = Counter32
_AccX25XmtCallAccs_Object = MibTableColumn
accX25XmtCallAccs = _AccX25XmtCallAccs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 20),
    _AccX25XmtCallAccs_Type()
)
accX25XmtCallAccs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtCallAccs.setStatus("mandatory")
_AccX25XmtClrReqs_Type = Counter32
_AccX25XmtClrReqs_Object = MibTableColumn
accX25XmtClrReqs = _AccX25XmtClrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 21),
    _AccX25XmtClrReqs_Type()
)
accX25XmtClrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtClrReqs.setStatus("mandatory")
_AccX25XmtClrConfs_Type = Counter32
_AccX25XmtClrConfs_Object = MibTableColumn
accX25XmtClrConfs = _AccX25XmtClrConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 22),
    _AccX25XmtClrConfs_Type()
)
accX25XmtClrConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtClrConfs.setStatus("mandatory")
_AccX25XmtResetReqs_Type = Counter32
_AccX25XmtResetReqs_Object = MibTableColumn
accX25XmtResetReqs = _AccX25XmtResetReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 23),
    _AccX25XmtResetReqs_Type()
)
accX25XmtResetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtResetReqs.setStatus("mandatory")
_AccX25XmtResetConfs_Type = Counter32
_AccX25XmtResetConfs_Object = MibTableColumn
accX25XmtResetConfs = _AccX25XmtResetConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 24),
    _AccX25XmtResetConfs_Type()
)
accX25XmtResetConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtResetConfs.setStatus("mandatory")
_AccX25XmtInts_Type = Counter32
_AccX25XmtInts_Object = MibTableColumn
accX25XmtInts = _AccX25XmtInts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 25),
    _AccX25XmtInts_Type()
)
accX25XmtInts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtInts.setStatus("mandatory")
_AccX25XmtIntConfs_Type = Counter32
_AccX25XmtIntConfs_Object = MibTableColumn
accX25XmtIntConfs = _AccX25XmtIntConfs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 26),
    _AccX25XmtIntConfs_Type()
)
accX25XmtIntConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtIntConfs.setStatus("mandatory")
_AccX25XmtRRs_Type = Counter32
_AccX25XmtRRs_Object = MibTableColumn
accX25XmtRRs = _AccX25XmtRRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 27),
    _AccX25XmtRRs_Type()
)
accX25XmtRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRRs.setStatus("mandatory")
_AccX25XmtRNRs_Type = Counter32
_AccX25XmtRNRs_Object = MibTableColumn
accX25XmtRNRs = _AccX25XmtRNRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 28),
    _AccX25XmtRNRs_Type()
)
accX25XmtRNRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtRNRs.setStatus("mandatory")
_AccX25XmtDatas_Type = Counter32
_AccX25XmtDatas_Object = MibTableColumn
accX25XmtDatas = _AccX25XmtDatas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 29),
    _AccX25XmtDatas_Type()
)
accX25XmtDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25XmtDatas.setStatus("mandatory")
_AccX25OpenSvcCounts_Type = Counter32
_AccX25OpenSvcCounts_Object = MibTableColumn
accX25OpenSvcCounts = _AccX25OpenSvcCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 4, 1, 30),
    _AccX25OpenSvcCounts_Type()
)
accX25OpenSvcCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25OpenSvcCounts.setStatus("mandatory")
_AccX25OptFacTable_Object = MibTable
accX25OptFacTable = _AccX25OptFacTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5)
)
if mibBuilder.loadTexts:
    accX25OptFacTable.setStatus("mandatory")
_AccX25OptFacEntry_Object = MibTableRow
accX25OptFacEntry = _AccX25OptFacEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1)
)
accX25OptFacEntry.setIndexNames(
    (0, "ACC-MIB", "accX25OptFacIndex"),
)
if mibBuilder.loadTexts:
    accX25OptFacEntry.setStatus("mandatory")
_AccX25OptFacIndex_Type = Integer32
_AccX25OptFacIndex_Object = MibTableColumn
accX25OptFacIndex = _AccX25OptFacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1, 1),
    _AccX25OptFacIndex_Type()
)
accX25OptFacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OptFacIndex.setStatus("mandatory")
_AccX25OptFacString_Type = OctetString
_AccX25OptFacString_Object = MibTableColumn
accX25OptFacString = _AccX25OptFacString_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 5, 1, 2),
    _AccX25OptFacString_Type()
)
accX25OptFacString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25OptFacString.setStatus("mandatory")
_AccX25PvcAddrTable_Object = MibTable
accX25PvcAddrTable = _AccX25PvcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6)
)
if mibBuilder.loadTexts:
    accX25PvcAddrTable.setStatus("mandatory")
_AccX25PvcAddrEntry_Object = MibTableRow
accX25PvcAddrEntry = _AccX25PvcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1)
)
accX25PvcAddrEntry.setIndexNames(
    (0, "ACC-MIB", "accX25PvcLine"),
    (0, "ACC-MIB", "accX25PvcAddrLcid"),
)
if mibBuilder.loadTexts:
    accX25PvcAddrEntry.setStatus("mandatory")
_AccX25PvcLine_Type = Integer32
_AccX25PvcLine_Object = MibTableColumn
accX25PvcLine = _AccX25PvcLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 1),
    _AccX25PvcLine_Type()
)
accX25PvcLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcLine.setStatus("mandatory")
_AccX25PvcAddrLcid_Type = Integer32
_AccX25PvcAddrLcid_Object = MibTableColumn
accX25PvcAddrLcid = _AccX25PvcAddrLcid_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 2),
    _AccX25PvcAddrLcid_Type()
)
accX25PvcAddrLcid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcAddrLcid.setStatus("mandatory")
_AccX25PvcAddrString_Type = DisplayString
_AccX25PvcAddrString_Object = MibTableColumn
accX25PvcAddrString = _AccX25PvcAddrString_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 3),
    _AccX25PvcAddrString_Type()
)
accX25PvcAddrString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcAddrString.setStatus("mandatory")


class _AccX25PvcProtocol_Type(Integer32):
    """Custom type accX25PvcProtocol based on Integer32"""
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
        *(("appletalk", 2),
          ("bridging", 6),
          ("decnet", 3),
          ("idp", 4),
          ("ip", 1),
          ("ipx", 5),
          ("sourcerouting", 7))
    )


_AccX25PvcProtocol_Type.__name__ = "Integer32"
_AccX25PvcProtocol_Object = MibTableColumn
accX25PvcProtocol = _AccX25PvcProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 6, 1, 4),
    _AccX25PvcProtocol_Type()
)
accX25PvcProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25PvcProtocol.setStatus("mandatory")
_AccX25ErrorTable_Object = MibTable
accX25ErrorTable = _AccX25ErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7)
)
if mibBuilder.loadTexts:
    accX25ErrorTable.setStatus("mandatory")
_AccX25ErrorEntry_Object = MibTableRow
accX25ErrorEntry = _AccX25ErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1)
)
accX25ErrorEntry.setIndexNames(
    (0, "ACC-MIB", "accX25ErrorLine"),
    (0, "ACC-MIB", "accX25ErrorUpTime"),
    (0, "ACC-MIB", "accX25ErrorSeq"),
)
if mibBuilder.loadTexts:
    accX25ErrorEntry.setStatus("mandatory")
_AccX25ErrorLine_Type = Integer32
_AccX25ErrorLine_Object = MibTableColumn
accX25ErrorLine = _AccX25ErrorLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 1),
    _AccX25ErrorLine_Type()
)
accX25ErrorLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorLine.setStatus("mandatory")
_AccX25ErrorUpTime_Type = TimeTicks
_AccX25ErrorUpTime_Object = MibTableColumn
accX25ErrorUpTime = _AccX25ErrorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 2),
    _AccX25ErrorUpTime_Type()
)
accX25ErrorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorUpTime.setStatus("mandatory")
_AccX25ErrorSeq_Type = Integer32
_AccX25ErrorSeq_Object = MibTableColumn
accX25ErrorSeq = _AccX25ErrorSeq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 3),
    _AccX25ErrorSeq_Type()
)
accX25ErrorSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorSeq.setStatus("mandatory")


class _AccX25ErrorState_Type(Integer32):
    """Custom type accX25ErrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25ErrorState_Type.__name__ = "Integer32"
_AccX25ErrorState_Object = MibTableColumn
accX25ErrorState = _AccX25ErrorState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 4),
    _AccX25ErrorState_Type()
)
accX25ErrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25ErrorState.setStatus("mandatory")
_AccX25ErrorProtocol_Type = Integer32
_AccX25ErrorProtocol_Object = MibTableColumn
accX25ErrorProtocol = _AccX25ErrorProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 5),
    _AccX25ErrorProtocol_Type()
)
accX25ErrorProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorProtocol.setStatus("mandatory")
_AccX25ErrorCause_Type = Integer32
_AccX25ErrorCause_Object = MibTableColumn
accX25ErrorCause = _AccX25ErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 6),
    _AccX25ErrorCause_Type()
)
accX25ErrorCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorCause.setStatus("mandatory")
_AccX25ErrorDiag_Type = Integer32
_AccX25ErrorDiag_Object = MibTableColumn
accX25ErrorDiag = _AccX25ErrorDiag_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 7),
    _AccX25ErrorDiag_Type()
)
accX25ErrorDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorDiag.setStatus("mandatory")
_AccX25ErrorPacket_Type = OctetString
_AccX25ErrorPacket_Object = MibTableColumn
accX25ErrorPacket = _AccX25ErrorPacket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 7, 1, 8),
    _AccX25ErrorPacket_Type()
)
accX25ErrorPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25ErrorPacket.setStatus("mandatory")
_AccX25Switch_ObjectIdentity = ObjectIdentity
accX25Switch = _AccX25Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8)
)


class _AccX25SwitchStatus_Type(Integer32):
    """Custom type accX25SwitchStatus based on Integer32"""
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


_AccX25SwitchStatus_Type.__name__ = "Integer32"
_AccX25SwitchStatus_Object = MibScalar
accX25SwitchStatus = _AccX25SwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 1),
    _AccX25SwitchStatus_Type()
)
accX25SwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchStatus.setStatus("mandatory")
_AccX25SwitchConnections_Type = Gauge32
_AccX25SwitchConnections_Object = MibScalar
accX25SwitchConnections = _AccX25SwitchConnections_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 2),
    _AccX25SwitchConnections_Type()
)
accX25SwitchConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnections.setStatus("mandatory")
_AccX25SwitchCallSucceeds_Type = Counter32
_AccX25SwitchCallSucceeds_Object = MibScalar
accX25SwitchCallSucceeds = _AccX25SwitchCallSucceeds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 3),
    _AccX25SwitchCallSucceeds_Type()
)
accX25SwitchCallSucceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchCallSucceeds.setStatus("mandatory")
_AccX25SwitchCallFails_Type = Counter32
_AccX25SwitchCallFails_Object = MibScalar
accX25SwitchCallFails = _AccX25SwitchCallFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 4),
    _AccX25SwitchCallFails_Type()
)
accX25SwitchCallFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchCallFails.setStatus("mandatory")
_AccX25SwitchConnTable_Object = MibTable
accX25SwitchConnTable = _AccX25SwitchConnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5)
)
if mibBuilder.loadTexts:
    accX25SwitchConnTable.setStatus("mandatory")
_AccX25SwitchConnEntry_Object = MibTableRow
accX25SwitchConnEntry = _AccX25SwitchConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1)
)
accX25SwitchConnEntry.setIndexNames(
    (0, "ACC-MIB", "accX25SwitchConnCallingIfIndex"),
    (0, "ACC-MIB", "accX25SwitchConnCallingIndex"),
)
if mibBuilder.loadTexts:
    accX25SwitchConnEntry.setStatus("mandatory")
_AccX25SwitchConnCallingIfIndex_Type = Integer32
_AccX25SwitchConnCallingIfIndex_Object = MibTableColumn
accX25SwitchConnCallingIfIndex = _AccX25SwitchConnCallingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 1),
    _AccX25SwitchConnCallingIfIndex_Type()
)
accX25SwitchConnCallingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingIfIndex.setStatus("mandatory")
_AccX25SwitchConnCallingIndex_Type = Integer32
_AccX25SwitchConnCallingIndex_Object = MibTableColumn
accX25SwitchConnCallingIndex = _AccX25SwitchConnCallingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 2),
    _AccX25SwitchConnCallingIndex_Type()
)
accX25SwitchConnCallingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingIndex.setStatus("mandatory")


class _AccX25SwitchConnCallingType_Type(Integer32):
    """Custom type accX25SwitchConnCallingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("x25", 2))
    )


_AccX25SwitchConnCallingType_Type.__name__ = "Integer32"
_AccX25SwitchConnCallingType_Object = MibTableColumn
accX25SwitchConnCallingType = _AccX25SwitchConnCallingType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 3),
    _AccX25SwitchConnCallingType_Type()
)
accX25SwitchConnCallingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingType.setStatus("mandatory")
_AccX25SwitchConnCallingX121Addr_Type = OctetString
_AccX25SwitchConnCallingX121Addr_Object = MibTableColumn
accX25SwitchConnCallingX121Addr = _AccX25SwitchConnCallingX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 4),
    _AccX25SwitchConnCallingX121Addr_Type()
)
accX25SwitchConnCallingX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingX121Addr.setStatus("mandatory")
_AccX25SwitchConnCallingPkts_Type = Counter32
_AccX25SwitchConnCallingPkts_Object = MibTableColumn
accX25SwitchConnCallingPkts = _AccX25SwitchConnCallingPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 5),
    _AccX25SwitchConnCallingPkts_Type()
)
accX25SwitchConnCallingPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingPkts.setStatus("mandatory")
_AccX25SwitchConnCallingOctets_Type = Counter32
_AccX25SwitchConnCallingOctets_Object = MibTableColumn
accX25SwitchConnCallingOctets = _AccX25SwitchConnCallingOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 6),
    _AccX25SwitchConnCallingOctets_Type()
)
accX25SwitchConnCallingOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCallingOctets.setStatus("mandatory")
_AccX25SwitchConnCalledIfIndex_Type = Integer32
_AccX25SwitchConnCalledIfIndex_Object = MibTableColumn
accX25SwitchConnCalledIfIndex = _AccX25SwitchConnCalledIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 7),
    _AccX25SwitchConnCalledIfIndex_Type()
)
accX25SwitchConnCalledIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledIfIndex.setStatus("mandatory")
_AccX25SwitchConnCalledIndex_Type = Integer32
_AccX25SwitchConnCalledIndex_Object = MibTableColumn
accX25SwitchConnCalledIndex = _AccX25SwitchConnCalledIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 8),
    _AccX25SwitchConnCalledIndex_Type()
)
accX25SwitchConnCalledIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledIndex.setStatus("mandatory")


class _AccX25SwitchConnCalledType_Type(Integer32):
    """Custom type accX25SwitchConnCalledType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tcp", 3),
          ("x25", 2))
    )


_AccX25SwitchConnCalledType_Type.__name__ = "Integer32"
_AccX25SwitchConnCalledType_Object = MibTableColumn
accX25SwitchConnCalledType = _AccX25SwitchConnCalledType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 9),
    _AccX25SwitchConnCalledType_Type()
)
accX25SwitchConnCalledType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledType.setStatus("mandatory")
_AccX25SwitchConnCalledX121Addr_Type = OctetString
_AccX25SwitchConnCalledX121Addr_Object = MibTableColumn
accX25SwitchConnCalledX121Addr = _AccX25SwitchConnCalledX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 10),
    _AccX25SwitchConnCalledX121Addr_Type()
)
accX25SwitchConnCalledX121Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledX121Addr.setStatus("mandatory")
_AccX25SwitchConnCalledPkts_Type = Counter32
_AccX25SwitchConnCalledPkts_Object = MibTableColumn
accX25SwitchConnCalledPkts = _AccX25SwitchConnCalledPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 11),
    _AccX25SwitchConnCalledPkts_Type()
)
accX25SwitchConnCalledPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledPkts.setStatus("mandatory")
_AccX25SwitchConnCalledOctets_Type = Counter32
_AccX25SwitchConnCalledOctets_Object = MibTableColumn
accX25SwitchConnCalledOctets = _AccX25SwitchConnCalledOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 12),
    _AccX25SwitchConnCalledOctets_Type()
)
accX25SwitchConnCalledOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnCalledOctets.setStatus("mandatory")


class _AccX25SwitchConnState_Type(Integer32):
    """Custom type accX25SwitchConnState based on Integer32"""
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
        *(("calling", 2),
          ("clearing", 3),
          ("open", 1),
          ("resetting", 4))
    )


_AccX25SwitchConnState_Type.__name__ = "Integer32"
_AccX25SwitchConnState_Object = MibTableColumn
accX25SwitchConnState = _AccX25SwitchConnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 5, 1, 13),
    _AccX25SwitchConnState_Type()
)
accX25SwitchConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accX25SwitchConnState.setStatus("mandatory")
_AccX25SwitchAddrTransTable_Object = MibTable
accX25SwitchAddrTransTable = _AccX25SwitchAddrTransTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6)
)
if mibBuilder.loadTexts:
    accX25SwitchAddrTransTable.setStatus("mandatory")
_AccX25SwitchAddrTransEntry_Object = MibTableRow
accX25SwitchAddrTransEntry = _AccX25SwitchAddrTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1)
)
accX25SwitchAddrTransEntry.setIndexNames(
    (0, "ACC-MIB", "accX25SwitchAddrTransIfIndex"),
    (0, "ACC-MIB", "accX25SwitchAddrTransDir"),
    (0, "ACC-MIB", "accX25SwitchAddrTransType"),
    (0, "ACC-MIB", "accX25SwitchAddrTransPattern"),
)
if mibBuilder.loadTexts:
    accX25SwitchAddrTransEntry.setStatus("mandatory")
_AccX25SwitchAddrTransIfIndex_Type = Integer32
_AccX25SwitchAddrTransIfIndex_Object = MibTableColumn
accX25SwitchAddrTransIfIndex = _AccX25SwitchAddrTransIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 1),
    _AccX25SwitchAddrTransIfIndex_Type()
)
accX25SwitchAddrTransIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransIfIndex.setStatus("mandatory")


class _AccX25SwitchAddrTransDir_Type(Integer32):
    """Custom type accX25SwitchAddrTransDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_AccX25SwitchAddrTransDir_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransDir_Object = MibTableColumn
accX25SwitchAddrTransDir = _AccX25SwitchAddrTransDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 2),
    _AccX25SwitchAddrTransDir_Type()
)
accX25SwitchAddrTransDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransDir.setStatus("mandatory")


class _AccX25SwitchAddrTransType_Type(Integer32):
    """Custom type accX25SwitchAddrTransType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("called", 1),
          ("calling", 2))
    )


_AccX25SwitchAddrTransType_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransType_Object = MibTableColumn
accX25SwitchAddrTransType = _AccX25SwitchAddrTransType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 3),
    _AccX25SwitchAddrTransType_Type()
)
accX25SwitchAddrTransType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransType.setStatus("mandatory")
_AccX25SwitchAddrTransPattern_Type = DisplayString
_AccX25SwitchAddrTransPattern_Object = MibTableColumn
accX25SwitchAddrTransPattern = _AccX25SwitchAddrTransPattern_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 4),
    _AccX25SwitchAddrTransPattern_Type()
)
accX25SwitchAddrTransPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransPattern.setStatus("mandatory")
_AccX25SwitchAddrTransReplace_Type = DisplayString
_AccX25SwitchAddrTransReplace_Object = MibTableColumn
accX25SwitchAddrTransReplace = _AccX25SwitchAddrTransReplace_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 5),
    _AccX25SwitchAddrTransReplace_Type()
)
accX25SwitchAddrTransReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransReplace.setStatus("mandatory")


class _AccX25SwitchAddrTransStatus_Type(Integer32):
    """Custom type accX25SwitchAddrTransStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchAddrTransStatus_Type.__name__ = "Integer32"
_AccX25SwitchAddrTransStatus_Object = MibTableColumn
accX25SwitchAddrTransStatus = _AccX25SwitchAddrTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 6, 1, 6),
    _AccX25SwitchAddrTransStatus_Type()
)
accX25SwitchAddrTransStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchAddrTransStatus.setStatus("mandatory")
_AccX25SwitchRouteTable_Object = MibTable
accX25SwitchRouteTable = _AccX25SwitchRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7)
)
if mibBuilder.loadTexts:
    accX25SwitchRouteTable.setStatus("mandatory")
_AccX25SwitchRouteEntry_Object = MibTableRow
accX25SwitchRouteEntry = _AccX25SwitchRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1)
)
accX25SwitchRouteEntry.setIndexNames(
    (0, "ACC-MIB", "accX25SwitchRoutePattern"),
)
if mibBuilder.loadTexts:
    accX25SwitchRouteEntry.setStatus("mandatory")
_AccX25SwitchRoutePattern_Type = OctetString
_AccX25SwitchRoutePattern_Object = MibTableColumn
accX25SwitchRoutePattern = _AccX25SwitchRoutePattern_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 1),
    _AccX25SwitchRoutePattern_Type()
)
accX25SwitchRoutePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRoutePattern.setStatus("mandatory")
_AccX25SwitchRouteIfIndex_Type = Integer32
_AccX25SwitchRouteIfIndex_Object = MibTableColumn
accX25SwitchRouteIfIndex = _AccX25SwitchRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 2),
    _AccX25SwitchRouteIfIndex_Type()
)
accX25SwitchRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRouteIfIndex.setStatus("mandatory")


class _AccX25SwitchRouteStatus_Type(Integer32):
    """Custom type accX25SwitchRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchRouteStatus_Type.__name__ = "Integer32"
_AccX25SwitchRouteStatus_Object = MibTableColumn
accX25SwitchRouteStatus = _AccX25SwitchRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 7, 1, 3),
    _AccX25SwitchRouteStatus_Type()
)
accX25SwitchRouteStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchRouteStatus.setStatus("mandatory")
_AccX25SwitchExtRtTable_Object = MibTable
accX25SwitchExtRtTable = _AccX25SwitchExtRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8)
)
if mibBuilder.loadTexts:
    accX25SwitchExtRtTable.setStatus("mandatory")
_AccX25SwitchExtRtEntry_Object = MibTableRow
accX25SwitchExtRtEntry = _AccX25SwitchExtRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1)
)
accX25SwitchExtRtEntry.setIndexNames(
    (0, "ACC-MIB", "accX25SwitchExtRtIndex"),
)
if mibBuilder.loadTexts:
    accX25SwitchExtRtEntry.setStatus("mandatory")
_AccX25SwitchExtRtIndex_Type = Integer32
_AccX25SwitchExtRtIndex_Object = MibTableColumn
accX25SwitchExtRtIndex = _AccX25SwitchExtRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 1),
    _AccX25SwitchExtRtIndex_Type()
)
accX25SwitchExtRtIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIndex.setStatus("mandatory")
_AccX25SwitchExtRtIfIn_Type = Integer32
_AccX25SwitchExtRtIfIn_Object = MibTableColumn
accX25SwitchExtRtIfIn = _AccX25SwitchExtRtIfIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 2),
    _AccX25SwitchExtRtIfIn_Type()
)
accX25SwitchExtRtIfIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIfIn.setStatus("mandatory")
_AccX25SwitchExtRtAddr_Type = OctetString
_AccX25SwitchExtRtAddr_Object = MibTableColumn
accX25SwitchExtRtAddr = _AccX25SwitchExtRtAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 3),
    _AccX25SwitchExtRtAddr_Type()
)
accX25SwitchExtRtAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtAddr.setStatus("mandatory")
_AccX25SwitchExtRtCUD_Type = OctetString
_AccX25SwitchExtRtCUD_Object = MibTableColumn
accX25SwitchExtRtCUD = _AccX25SwitchExtRtCUD_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 4),
    _AccX25SwitchExtRtCUD_Type()
)
accX25SwitchExtRtCUD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtCUD.setStatus("mandatory")


class _AccX25SwitchExtRtDisp_Type(Integer32):
    """Custom type accX25SwitchExtRtDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("reject", 3),
          ("switch", 1))
    )


_AccX25SwitchExtRtDisp_Type.__name__ = "Integer32"
_AccX25SwitchExtRtDisp_Object = MibTableColumn
accX25SwitchExtRtDisp = _AccX25SwitchExtRtDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 5),
    _AccX25SwitchExtRtDisp_Type()
)
accX25SwitchExtRtDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtDisp.setStatus("mandatory")
_AccX25SwitchExtRtIfOut_Type = Integer32
_AccX25SwitchExtRtIfOut_Object = MibTableColumn
accX25SwitchExtRtIfOut = _AccX25SwitchExtRtIfOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 6),
    _AccX25SwitchExtRtIfOut_Type()
)
accX25SwitchExtRtIfOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtIfOut.setStatus("mandatory")


class _AccX25SwitchExtRtStatus_Type(Integer32):
    """Custom type accX25SwitchExtRtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccX25SwitchExtRtStatus_Type.__name__ = "Integer32"
_AccX25SwitchExtRtStatus_Object = MibTableColumn
accX25SwitchExtRtStatus = _AccX25SwitchExtRtStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 17, 8, 8, 1, 7),
    _AccX25SwitchExtRtStatus_Type()
)
accX25SwitchExtRtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accX25SwitchExtRtStatus.setStatus("mandatory")
_AccIpFilter_ObjectIdentity = ObjectIdentity
accIpFilter = _AccIpFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18)
)


class _AccIpSrcRouting_Type(Integer32):
    """Custom type accIpSrcRouting based on Integer32"""
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


_AccIpSrcRouting_Type.__name__ = "Integer32"
_AccIpSrcRouting_Object = MibScalar
accIpSrcRouting = _AccIpSrcRouting_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 1),
    _AccIpSrcRouting_Type()
)
accIpSrcRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpSrcRouting.setStatus("mandatory")
_AccIpFiltTable_Object = MibTable
accIpFiltTable = _AccIpFiltTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2)
)
if mibBuilder.loadTexts:
    accIpFiltTable.setStatus("deprecated")
_AccIpFiltEntry_Object = MibTableRow
accIpFiltEntry = _AccIpFiltEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1)
)
accIpFiltEntry.setIndexNames(
    (0, "ACC-MIB", "accIpFiltDAddr"),
    (0, "ACC-MIB", "accIpFiltDNetMask"),
    (0, "ACC-MIB", "accIpFiltSAddr"),
    (0, "ACC-MIB", "accIpFiltSNetMask"),
    (0, "ACC-MIB", "accIpFiltParm"),
    (0, "ACC-MIB", "accIpFiltDisp"),
)
if mibBuilder.loadTexts:
    accIpFiltEntry.setStatus("deprecated")
_AccIpFiltDAddr_Type = IpAddress
_AccIpFiltDAddr_Object = MibTableColumn
accIpFiltDAddr = _AccIpFiltDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 1),
    _AccIpFiltDAddr_Type()
)
accIpFiltDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDAddr.setStatus("deprecated")
_AccIpFiltDNetMask_Type = IpAddress
_AccIpFiltDNetMask_Object = MibTableColumn
accIpFiltDNetMask = _AccIpFiltDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 2),
    _AccIpFiltDNetMask_Type()
)
accIpFiltDNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDNetMask.setStatus("deprecated")
_AccIpFiltSAddr_Type = IpAddress
_AccIpFiltSAddr_Object = MibTableColumn
accIpFiltSAddr = _AccIpFiltSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 3),
    _AccIpFiltSAddr_Type()
)
accIpFiltSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltSAddr.setStatus("deprecated")
_AccIpFiltSNetMask_Type = IpAddress
_AccIpFiltSNetMask_Object = MibTableColumn
accIpFiltSNetMask = _AccIpFiltSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 4),
    _AccIpFiltSNetMask_Type()
)
accIpFiltSNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltSNetMask.setStatus("deprecated")
_AccIpFiltParm_Type = OctetString
_AccIpFiltParm_Object = MibTableColumn
accIpFiltParm = _AccIpFiltParm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 5),
    _AccIpFiltParm_Type()
)
accIpFiltParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltParm.setStatus("deprecated")


class _AccIpFiltDisp_Type(Integer32):
    """Custom type accIpFiltDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccIpFiltDisp_Type.__name__ = "Integer32"
_AccIpFiltDisp_Object = MibTableColumn
accIpFiltDisp = _AccIpFiltDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 2, 1, 6),
    _AccIpFiltDisp_Type()
)
accIpFiltDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpFiltDisp.setStatus("deprecated")


class _OIpSubDirBcast_Type(Integer32):
    """Custom type oIpSubDirBcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcast", 1),
          ("nobcast", 2))
    )


_OIpSubDirBcast_Type.__name__ = "Integer32"
_OIpSubDirBcast_Object = MibScalar
oIpSubDirBcast = _OIpSubDirBcast_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 4),
    _OIpSubDirBcast_Type()
)
oIpSubDirBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oIpSubDirBcast.setStatus("mandatory")
_AccIpIfFiltDispTable_Object = MibTable
accIpIfFiltDispTable = _AccIpIfFiltDispTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5)
)
if mibBuilder.loadTexts:
    accIpIfFiltDispTable.setStatus("mandatory")
_AccIpIfFiltDispEntry_Object = MibTableRow
accIpIfFiltDispEntry = _AccIpIfFiltDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1)
)
accIpIfFiltDispEntry.setIndexNames(
    (0, "ACC-MIB", "accIpIfFiltDispIfIndex"),
    (0, "ACC-MIB", "accIpIfFiltDispPktDir"),
    (0, "ACC-MIB", "accIpIfFiltDispSeqNum"),
)
if mibBuilder.loadTexts:
    accIpIfFiltDispEntry.setStatus("mandatory")
_AccIpIfFiltDispIfIndex_Type = Integer32
_AccIpIfFiltDispIfIndex_Object = MibTableColumn
accIpIfFiltDispIfIndex = _AccIpIfFiltDispIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 1),
    _AccIpIfFiltDispIfIndex_Type()
)
accIpIfFiltDispIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispIfIndex.setStatus("mandatory")


class _AccIpIfFiltDispPktDir_Type(Integer32):
    """Custom type accIpIfFiltDispPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpIfFiltDispPktDir_Type.__name__ = "Integer32"
_AccIpIfFiltDispPktDir_Object = MibTableColumn
accIpIfFiltDispPktDir = _AccIpIfFiltDispPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 2),
    _AccIpIfFiltDispPktDir_Type()
)
accIpIfFiltDispPktDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispPktDir.setStatus("mandatory")
_AccIpIfFiltDispSeqNum_Type = Integer32
_AccIpIfFiltDispSeqNum_Object = MibTableColumn
accIpIfFiltDispSeqNum = _AccIpIfFiltDispSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 3),
    _AccIpIfFiltDispSeqNum_Type()
)
accIpIfFiltDispSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSeqNum.setStatus("mandatory")
_AccIpIfFiltDispDAddr_Type = IpAddress
_AccIpIfFiltDispDAddr_Object = MibTableColumn
accIpIfFiltDispDAddr = _AccIpIfFiltDispDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 4),
    _AccIpIfFiltDispDAddr_Type()
)
accIpIfFiltDispDAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDAddr.setStatus("mandatory")
_AccIpIfFiltDispDNetMask_Type = IpAddress
_AccIpIfFiltDispDNetMask_Object = MibTableColumn
accIpIfFiltDispDNetMask = _AccIpIfFiltDispDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 5),
    _AccIpIfFiltDispDNetMask_Type()
)
accIpIfFiltDispDNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDNetMask.setStatus("mandatory")
_AccIpIfFiltDispSAddr_Type = IpAddress
_AccIpIfFiltDispSAddr_Object = MibTableColumn
accIpIfFiltDispSAddr = _AccIpIfFiltDispSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 6),
    _AccIpIfFiltDispSAddr_Type()
)
accIpIfFiltDispSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSAddr.setStatus("mandatory")
_AccIpIfFiltDispSNetMask_Type = IpAddress
_AccIpIfFiltDispSNetMask_Object = MibTableColumn
accIpIfFiltDispSNetMask = _AccIpIfFiltDispSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 7),
    _AccIpIfFiltDispSNetMask_Type()
)
accIpIfFiltDispSNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispSNetMask.setStatus("mandatory")


class _AccIpIfFiltDispOp1_Type(Integer32):
    """Custom type accIpIfFiltDispOp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 3),
          ("none", 1),
          ("not-equal", 2))
    )


_AccIpIfFiltDispOp1_Type.__name__ = "Integer32"
_AccIpIfFiltDispOp1_Object = MibTableColumn
accIpIfFiltDispOp1 = _AccIpIfFiltDispOp1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 8),
    _AccIpIfFiltDispOp1_Type()
)
accIpIfFiltDispOp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispOp1.setStatus("mandatory")


class _AccIpIfFiltDispProtocol_Type(Integer32):
    """Custom type accIpIfFiltDispProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpIfFiltDispProtocol_Type.__name__ = "Integer32"
_AccIpIfFiltDispProtocol_Object = MibTableColumn
accIpIfFiltDispProtocol = _AccIpIfFiltDispProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 9),
    _AccIpIfFiltDispProtocol_Type()
)
accIpIfFiltDispProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispProtocol.setStatus("mandatory")


class _AccIpIfFiltDispOp2_Type(Integer32):
    """Custom type accIpIfFiltDispOp2 based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dst-equal", 13),
          ("dst-greater-than", 12),
          ("dst-less-than", 11),
          ("dst-not-equal", 10),
          ("equal", 5),
          ("greater-than", 4),
          ("less-than", 3),
          ("none", 1),
          ("not-equal", 2),
          ("src-equal", 9),
          ("src-greater-than", 8),
          ("src-less-than", 7),
          ("src-not-equal", 6))
    )


_AccIpIfFiltDispOp2_Type.__name__ = "Integer32"
_AccIpIfFiltDispOp2_Object = MibTableColumn
accIpIfFiltDispOp2 = _AccIpIfFiltDispOp2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 10),
    _AccIpIfFiltDispOp2_Type()
)
accIpIfFiltDispOp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispOp2.setStatus("mandatory")


class _AccIpIfFiltDispUDPTCPPort_Type(Integer32):
    """Custom type accIpIfFiltDispUDPTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccIpIfFiltDispUDPTCPPort_Type.__name__ = "Integer32"
_AccIpIfFiltDispUDPTCPPort_Object = MibTableColumn
accIpIfFiltDispUDPTCPPort = _AccIpIfFiltDispUDPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 11),
    _AccIpIfFiltDispUDPTCPPort_Type()
)
accIpIfFiltDispUDPTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispUDPTCPPort.setStatus("mandatory")


class _AccIpIfFiltDispDispos_Type(Integer32):
    """Custom type accIpIfFiltDispDispos based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 5),
          ("log", 2),
          ("lowPriority", 4),
          ("normalPriority", 3))
    )


_AccIpIfFiltDispDispos_Type.__name__ = "Integer32"
_AccIpIfFiltDispDispos_Object = MibTableColumn
accIpIfFiltDispDispos = _AccIpIfFiltDispDispos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 12),
    _AccIpIfFiltDispDispos_Type()
)
accIpIfFiltDispDispos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispDispos.setStatus("mandatory")
_AccIpIfFiltDispMatches_Type = Counter32
_AccIpIfFiltDispMatches_Object = MibTableColumn
accIpIfFiltDispMatches = _AccIpIfFiltDispMatches_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 13),
    _AccIpIfFiltDispMatches_Type()
)
accIpIfFiltDispMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispMatches.setStatus("mandatory")
_AccIpIfFiltDispLastMatchTime_Type = TimeTicks
_AccIpIfFiltDispLastMatchTime_Object = MibTableColumn
accIpIfFiltDispLastMatchTime = _AccIpIfFiltDispLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 14),
    _AccIpIfFiltDispLastMatchTime_Type()
)
accIpIfFiltDispLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispLastMatchTime.setStatus("mandatory")
_AccIpIfFiltDispMatchPkt_Type = OctetString
_AccIpIfFiltDispMatchPkt_Object = MibTableColumn
accIpIfFiltDispMatchPkt = _AccIpIfFiltDispMatchPkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 5, 1, 15),
    _AccIpIfFiltDispMatchPkt_Type()
)
accIpIfFiltDispMatchPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltDispMatchPkt.setStatus("mandatory")
_AccIpIfFiltEditTable_Object = MibTable
accIpIfFiltEditTable = _AccIpIfFiltEditTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6)
)
if mibBuilder.loadTexts:
    accIpIfFiltEditTable.setStatus("mandatory")
_AccIpIfFiltEditEntry_Object = MibTableRow
accIpIfFiltEditEntry = _AccIpIfFiltEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1)
)
accIpIfFiltEditEntry.setIndexNames(
    (0, "ACC-MIB", "accIpIfFiltEditIndex"),
)
if mibBuilder.loadTexts:
    accIpIfFiltEditEntry.setStatus("mandatory")
_AccIpIfFiltEditIndex_Type = Integer32
_AccIpIfFiltEditIndex_Object = MibTableColumn
accIpIfFiltEditIndex = _AccIpIfFiltEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 1),
    _AccIpIfFiltEditIndex_Type()
)
accIpIfFiltEditIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpIfFiltEditIndex.setStatus("mandatory")


class _AccIpIfFiltEditAction_Type(Integer32):
    """Custom type accIpIfFiltEditAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccIpIfFiltEditAction_Type.__name__ = "Integer32"
_AccIpIfFiltEditAction_Object = MibTableColumn
accIpIfFiltEditAction = _AccIpIfFiltEditAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 2),
    _AccIpIfFiltEditAction_Type()
)
accIpIfFiltEditAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditAction.setStatus("mandatory")
_AccIpIfFiltEditIfIndex_Type = Integer32
_AccIpIfFiltEditIfIndex_Object = MibTableColumn
accIpIfFiltEditIfIndex = _AccIpIfFiltEditIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 3),
    _AccIpIfFiltEditIfIndex_Type()
)
accIpIfFiltEditIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditIfIndex.setStatus("mandatory")


class _AccIpIfFiltEditPktDir_Type(Integer32):
    """Custom type accIpIfFiltEditPktDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("global", 3),
          ("input", 1),
          ("output", 2))
    )


_AccIpIfFiltEditPktDir_Type.__name__ = "Integer32"
_AccIpIfFiltEditPktDir_Object = MibTableColumn
accIpIfFiltEditPktDir = _AccIpIfFiltEditPktDir_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 4),
    _AccIpIfFiltEditPktDir_Type()
)
accIpIfFiltEditPktDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditPktDir.setStatus("mandatory")
_AccIpIfFiltEditDAddr_Type = IpAddress
_AccIpIfFiltEditDAddr_Object = MibTableColumn
accIpIfFiltEditDAddr = _AccIpIfFiltEditDAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 5),
    _AccIpIfFiltEditDAddr_Type()
)
accIpIfFiltEditDAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDAddr.setStatus("mandatory")
_AccIpIfFiltEditDNetMask_Type = IpAddress
_AccIpIfFiltEditDNetMask_Object = MibTableColumn
accIpIfFiltEditDNetMask = _AccIpIfFiltEditDNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 6),
    _AccIpIfFiltEditDNetMask_Type()
)
accIpIfFiltEditDNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDNetMask.setStatus("mandatory")
_AccIpIfFiltEditSAddr_Type = IpAddress
_AccIpIfFiltEditSAddr_Object = MibTableColumn
accIpIfFiltEditSAddr = _AccIpIfFiltEditSAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 7),
    _AccIpIfFiltEditSAddr_Type()
)
accIpIfFiltEditSAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditSAddr.setStatus("mandatory")
_AccIpIfFiltEditSNetMask_Type = IpAddress
_AccIpIfFiltEditSNetMask_Object = MibTableColumn
accIpIfFiltEditSNetMask = _AccIpIfFiltEditSNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 8),
    _AccIpIfFiltEditSNetMask_Type()
)
accIpIfFiltEditSNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditSNetMask.setStatus("mandatory")


class _AccIpIfFiltEditOp1_Type(Integer32):
    """Custom type accIpIfFiltEditOp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("equal", 2),
          ("none", 1),
          ("not-equal", 3))
    )


_AccIpIfFiltEditOp1_Type.__name__ = "Integer32"
_AccIpIfFiltEditOp1_Object = MibTableColumn
accIpIfFiltEditOp1 = _AccIpIfFiltEditOp1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 9),
    _AccIpIfFiltEditOp1_Type()
)
accIpIfFiltEditOp1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditOp1.setStatus("mandatory")


class _AccIpIfFiltEditProtocol_Type(Integer32):
    """Custom type accIpIfFiltEditProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpIfFiltEditProtocol_Type.__name__ = "Integer32"
_AccIpIfFiltEditProtocol_Object = MibTableColumn
accIpIfFiltEditProtocol = _AccIpIfFiltEditProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 10),
    _AccIpIfFiltEditProtocol_Type()
)
accIpIfFiltEditProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditProtocol.setStatus("mandatory")


class _AccIpIfFiltEditOp2_Type(Integer32):
    """Custom type accIpIfFiltEditOp2 based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("dst-equal", 6),
          ("dst-greater-than", 9),
          ("dst-less-than", 8),
          ("dst-not-equal", 7),
          ("equal", 2),
          ("greater-than", 5),
          ("less-than", 4),
          ("none", 1),
          ("not-equal", 3),
          ("src-equal", 10),
          ("src-greater-than", 13),
          ("src-less-than", 12),
          ("src-not-equal", 11))
    )


_AccIpIfFiltEditOp2_Type.__name__ = "Integer32"
_AccIpIfFiltEditOp2_Object = MibTableColumn
accIpIfFiltEditOp2 = _AccIpIfFiltEditOp2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 11),
    _AccIpIfFiltEditOp2_Type()
)
accIpIfFiltEditOp2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditOp2.setStatus("mandatory")


class _AccIpIfFiltEditUDPTCPPort_Type(Integer32):
    """Custom type accIpIfFiltEditUDPTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccIpIfFiltEditUDPTCPPort_Type.__name__ = "Integer32"
_AccIpIfFiltEditUDPTCPPort_Object = MibTableColumn
accIpIfFiltEditUDPTCPPort = _AccIpIfFiltEditUDPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 12),
    _AccIpIfFiltEditUDPTCPPort_Type()
)
accIpIfFiltEditUDPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditUDPTCPPort.setStatus("mandatory")


class _AccIpIfFiltEditDispos_Type(Integer32):
    """Custom type accIpIfFiltEditDispos based on Integer32"""
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
        *(("discard", 1),
          ("highPriority", 5),
          ("log", 2),
          ("lowPriority", 4),
          ("normalPriority", 3))
    )


_AccIpIfFiltEditDispos_Type.__name__ = "Integer32"
_AccIpIfFiltEditDispos_Object = MibTableColumn
accIpIfFiltEditDispos = _AccIpIfFiltEditDispos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 18, 6, 1, 13),
    _AccIpIfFiltEditDispos_Type()
)
accIpIfFiltEditDispos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpIfFiltEditDispos.setStatus("mandatory")
_AccDn_ObjectIdentity = ObjectIdentity
accDn = _AccDn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19)
)
_AccDnNumber_Type = Integer32
_AccDnNumber_Object = MibScalar
accDnNumber = _AccDnNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 1),
    _AccDnNumber_Type()
)
accDnNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnNumber.setStatus("mandatory")
_AccDnID_Type = Integer32
_AccDnID_Object = MibScalar
accDnID = _AccDnID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 2),
    _AccDnID_Type()
)
accDnID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnID.setStatus("mandatory")


class _AccDnMaxNode_Type(Integer32):
    """Custom type accDnMaxNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AccDnMaxNode_Type.__name__ = "Integer32"
_AccDnMaxNode_Object = MibScalar
accDnMaxNode = _AccDnMaxNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 3),
    _AccDnMaxNode_Type()
)
accDnMaxNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxNode.setStatus("mandatory")


class _AccDnMaxArea_Type(Integer32):
    """Custom type accDnMaxArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AccDnMaxArea_Type.__name__ = "Integer32"
_AccDnMaxArea_Object = MibScalar
accDnMaxArea = _AccDnMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 4),
    _AccDnMaxArea_Type()
)
accDnMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxArea.setStatus("mandatory")


class _AccDnMaxAdjRtr_Type(Integer32):
    """Custom type accDnMaxAdjRtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AccDnMaxAdjRtr_Type.__name__ = "Integer32"
_AccDnMaxAdjRtr_Object = MibScalar
accDnMaxAdjRtr = _AccDnMaxAdjRtr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 5),
    _AccDnMaxAdjRtr_Type()
)
accDnMaxAdjRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxAdjRtr.setStatus("mandatory")


class _AccDnMaxEndNode_Type(Integer32):
    """Custom type accDnMaxEndNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_AccDnMaxEndNode_Type.__name__ = "Integer32"
_AccDnMaxEndNode_Object = MibScalar
accDnMaxEndNode = _AccDnMaxEndNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 6),
    _AccDnMaxEndNode_Type()
)
accDnMaxEndNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxEndNode.setStatus("mandatory")


class _AccDnMaxLocHop_Type(Integer32):
    """Custom type accDnMaxLocHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AccDnMaxLocHop_Type.__name__ = "Integer32"
_AccDnMaxLocHop_Object = MibScalar
accDnMaxLocHop = _AccDnMaxLocHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 7),
    _AccDnMaxLocHop_Type()
)
accDnMaxLocHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxLocHop.setStatus("mandatory")


class _AccDnMaxLocCost_Type(Integer32):
    """Custom type accDnMaxLocCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnMaxLocCost_Type.__name__ = "Integer32"
_AccDnMaxLocCost_Object = MibScalar
accDnMaxLocCost = _AccDnMaxLocCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 8),
    _AccDnMaxLocCost_Type()
)
accDnMaxLocCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxLocCost.setStatus("mandatory")


class _AccDnMaxVisit_Type(Integer32):
    """Custom type accDnMaxVisit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_AccDnMaxVisit_Type.__name__ = "Integer32"
_AccDnMaxVisit_Object = MibScalar
accDnMaxVisit = _AccDnMaxVisit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 9),
    _AccDnMaxVisit_Type()
)
accDnMaxVisit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxVisit.setStatus("mandatory")


class _AccDnMaxForHop_Type(Integer32):
    """Custom type accDnMaxForHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AccDnMaxForHop_Type.__name__ = "Integer32"
_AccDnMaxForHop_Object = MibScalar
accDnMaxForHop = _AccDnMaxForHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 10),
    _AccDnMaxForHop_Type()
)
accDnMaxForHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxForHop.setStatus("mandatory")


class _AccDnMaxForCost_Type(Integer32):
    """Custom type accDnMaxForCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnMaxForCost_Type.__name__ = "Integer32"
_AccDnMaxForCost_Object = MibScalar
accDnMaxForCost = _AccDnMaxForCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 11),
    _AccDnMaxForCost_Type()
)
accDnMaxForCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxForCost.setStatus("mandatory")
_AccDnBCT1_Type = TimeTicks
_AccDnBCT1_Object = MibScalar
accDnBCT1 = _AccDnBCT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 12),
    _AccDnBCT1_Type()
)
accDnBCT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnBCT1.setStatus("mandatory")
_AccDnT1_Type = TimeTicks
_AccDnT1_Object = MibScalar
accDnT1 = _AccDnT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 13),
    _AccDnT1_Type()
)
accDnT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnT1.setStatus("mandatory")


class _AccDnMsgLev_Type(Integer32):
    """Custom type accDnMsgLev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccDnMsgLev_Type.__name__ = "Integer32"
_AccDnMsgLev_Object = MibScalar
accDnMsgLev = _AccDnMsgLev_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 14),
    _AccDnMsgLev_Type()
)
accDnMsgLev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMsgLev.setStatus("mandatory")


class _AccDnNodeState_Type(Integer32):
    """Custom type accDnNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 2),
          ("level2", 3),
          ("off", 1))
    )


_AccDnNodeState_Type.__name__ = "Integer32"
_AccDnNodeState_Object = MibScalar
accDnNodeState = _AccDnNodeState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 15),
    _AccDnNodeState_Type()
)
accDnNodeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnNodeState.setStatus("mandatory")
_AccDnUnreachs_Type = Counter32
_AccDnUnreachs_Object = MibScalar
accDnUnreachs = _AccDnUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 16),
    _AccDnUnreachs_Type()
)
accDnUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnUnreachs.setStatus("mandatory")
_AccDnVisitXcds_Type = Counter32
_AccDnVisitXcds_Object = MibScalar
accDnVisitXcds = _AccDnVisitXcds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 17),
    _AccDnVisitXcds_Type()
)
accDnVisitXcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnVisitXcds.setStatus("mandatory")
_AccDnBadNodes_Type = Counter32
_AccDnBadNodes_Object = MibScalar
accDnBadNodes = _AccDnBadNodes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 18),
    _AccDnBadNodes_Type()
)
accDnBadNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnBadNodes.setStatus("mandatory")
_AccDnPktOsizes_Type = Counter32
_AccDnPktOsizes_Object = MibScalar
accDnPktOsizes = _AccDnPktOsizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 19),
    _AccDnPktOsizes_Type()
)
accDnPktOsizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnPktOsizes.setStatus("mandatory")
_AccDnFmtErrs_Type = Counter32
_AccDnFmtErrs_Object = MibScalar
accDnFmtErrs = _AccDnFmtErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 20),
    _AccDnFmtErrs_Type()
)
accDnFmtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnFmtErrs.setStatus("mandatory")
_AccDnCktTable_Object = MibTable
accDnCktTable = _AccDnCktTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21)
)
if mibBuilder.loadTexts:
    accDnCktTable.setStatus("mandatory")
_AccDnCktEntry_Object = MibTableRow
accDnCktEntry = _AccDnCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1)
)
accDnCktEntry.setIndexNames(
    (0, "ACC-MIB", "accDnCktIndex"),
)
if mibBuilder.loadTexts:
    accDnCktEntry.setStatus("mandatory")
_AccDnCktIndex_Type = Integer32
_AccDnCktIndex_Object = MibTableColumn
accDnCktIndex = _AccDnCktIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 1),
    _AccDnCktIndex_Type()
)
accDnCktIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktIndex.setStatus("mandatory")


class _AccDnCktStatus_Type(Integer32):
    """Custom type accDnCktStatus based on Integer32"""
    defaultValue = 2

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


_AccDnCktStatus_Type.__name__ = "Integer32"
_AccDnCktStatus_Object = MibTableColumn
accDnCktStatus = _AccDnCktStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 2),
    _AccDnCktStatus_Type()
)
accDnCktStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktStatus.setStatus("mandatory")


class _AccDnCktState_Type(Integer32):
    """Custom type accDnCktState based on Integer32"""
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
        *(("down", 2),
          ("shut", 3),
          ("start", 4),
          ("test", 5),
          ("up", 1))
    )


_AccDnCktState_Type.__name__ = "Integer32"
_AccDnCktState_Object = MibTableColumn
accDnCktState = _AccDnCktState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 3),
    _AccDnCktState_Type()
)
accDnCktState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnCktState.setStatus("mandatory")


class _AccDnCktCost_Type(Integer32):
    """Custom type accDnCktCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_AccDnCktCost_Type.__name__ = "Integer32"
_AccDnCktCost_Object = MibTableColumn
accDnCktCost = _AccDnCktCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 4),
    _AccDnCktCost_Type()
)
accDnCktCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktCost.setStatus("mandatory")


class _AccDnMaxRtr_Type(Integer32):
    """Custom type accDnMaxRtr based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AccDnMaxRtr_Type.__name__ = "Integer32"
_AccDnMaxRtr_Object = MibTableColumn
accDnMaxRtr = _AccDnMaxRtr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 5),
    _AccDnMaxRtr_Type()
)
accDnMaxRtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnMaxRtr.setStatus("mandatory")


class _AccDnHelloInt_Type(TimeTicks):
    """Custom type accDnHelloInt based on TimeTicks"""
    defaultValue = 15


_AccDnHelloInt_Object = MibTableColumn
accDnHelloInt = _AccDnHelloInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 6),
    _AccDnHelloInt_Type()
)
accDnHelloInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnHelloInt.setStatus("mandatory")


class _AccDnRtrPriority_Type(Integer32):
    """Custom type accDnRtrPriority based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnRtrPriority_Type.__name__ = "Integer32"
_AccDnRtrPriority_Object = MibTableColumn
accDnRtrPriority = _AccDnRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 7),
    _AccDnRtrPriority_Type()
)
accDnRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRtrPriority.setStatus("mandatory")
_AccDnDesRtrId_Type = OctetString
_AccDnDesRtrId_Object = MibTableColumn
accDnDesRtrId = _AccDnDesRtrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 8),
    _AccDnDesRtrId_Type()
)
accDnDesRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnDesRtrId.setStatus("mandatory")


class _AccDnDesRtrPrio_Type(Integer32):
    """Custom type accDnDesRtrPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnDesRtrPrio_Type.__name__ = "Integer32"
_AccDnDesRtrPrio_Object = MibTableColumn
accDnDesRtrPrio = _AccDnDesRtrPrio_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 9),
    _AccDnDesRtrPrio_Type()
)
accDnDesRtrPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnDesRtrPrio.setStatus("mandatory")
_AccDnTrnPktRecs_Type = Counter32
_AccDnTrnPktRecs_Object = MibTableColumn
accDnTrnPktRecs = _AccDnTrnPktRecs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 10),
    _AccDnTrnPktRecs_Type()
)
accDnTrnPktRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnTrnPktRecs.setStatus("mandatory")
_AccDnTrnPktSnds_Type = Counter32
_AccDnTrnPktSnds_Object = MibTableColumn
accDnTrnPktSnds = _AccDnTrnPktSnds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 11),
    _AccDnTrnPktSnds_Type()
)
accDnTrnPktSnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnTrnPktSnds.setStatus("mandatory")
_AccDnEndNodePktRecs_Type = Counter32
_AccDnEndNodePktRecs_Object = MibTableColumn
accDnEndNodePktRecs = _AccDnEndNodePktRecs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 12),
    _AccDnEndNodePktRecs_Type()
)
accDnEndNodePktRecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnEndNodePktRecs.setStatus("mandatory")
_AccDnEndNodePktSnds_Type = Counter32
_AccDnEndNodePktSnds_Object = MibTableColumn
accDnEndNodePktSnds = _AccDnEndNodePktSnds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 13),
    _AccDnEndNodePktSnds_Type()
)
accDnEndNodePktSnds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnEndNodePktSnds.setStatus("mandatory")
_AccDnCktDowns_Type = Counter32
_AccDnCktDowns_Object = MibTableColumn
accDnCktDowns = _AccDnCktDowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 14),
    _AccDnCktDowns_Type()
)
accDnCktDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnCktDowns.setStatus("mandatory")


class _AccDnCktType_Type(Integer32):
    """Custom type accDnCktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              9,
              16,
              129,
              130,
              131)
        )
    )
    namedValues = NamedValues(
        *(("enet", 6),
          ("fr", 131),
          ("lapb", 16),
          ("mlink", 129),
          ("trn", 9),
          ("x25", 130))
    )


_AccDnCktType_Type.__name__ = "Integer32"
_AccDnCktType_Object = MibTableColumn
accDnCktType = _AccDnCktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 15),
    _AccDnCktType_Type()
)
accDnCktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktType.setStatus("mandatory")


class _AccDnCktPort_Type(Integer32):
    """Custom type accDnCktPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2),
          ("j3", 3))
    )


_AccDnCktPort_Type.__name__ = "Integer32"
_AccDnCktPort_Object = MibTableColumn
accDnCktPort = _AccDnCktPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 16),
    _AccDnCktPort_Type()
)
accDnCktPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnCktPort.setStatus("mandatory")
_AccDnX25InOutAddr_Type = DisplayString
_AccDnX25InOutAddr_Object = MibTableColumn
accDnX25InOutAddr = _AccDnX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 17),
    _AccDnX25InOutAddr_Type()
)
accDnX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25InOutAddr.setStatus("mandatory")
_AccDnX25InAddr_Type = DisplayString
_AccDnX25InAddr_Object = MibTableColumn
accDnX25InAddr = _AccDnX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 18),
    _AccDnX25InAddr_Type()
)
accDnX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25InAddr.setStatus("mandatory")
_AccDnX25Idle_Type = TimeTicks
_AccDnX25Idle_Object = MibTableColumn
accDnX25Idle = _AccDnX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 19),
    _AccDnX25Idle_Type()
)
accDnX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25Idle.setStatus("mandatory")


class _AccDnX25PktVal_Type(Integer32):
    """Custom type accDnX25PktVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccDnX25PktVal_Type.__name__ = "Integer32"
_AccDnX25PktVal_Object = MibTableColumn
accDnX25PktVal = _AccDnX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 20),
    _AccDnX25PktVal_Type()
)
accDnX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25PktVal.setStatus("mandatory")


class _AccDnX25PktWin_Type(Integer32):
    """Custom type accDnX25PktWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccDnX25PktWin_Type.__name__ = "Integer32"
_AccDnX25PktWin_Object = MibTableColumn
accDnX25PktWin = _AccDnX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 21),
    _AccDnX25PktWin_Type()
)
accDnX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25PktWin.setStatus("mandatory")


class _AccDnEntryStatus_Type(Integer32):
    """Custom type accDnEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDnEntryStatus_Type.__name__ = "Integer32"
_AccDnEntryStatus_Object = MibTableColumn
accDnEntryStatus = _AccDnEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 22),
    _AccDnEntryStatus_Type()
)
accDnEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnEntryStatus.setStatus("mandatory")


class _AccDnX25FacIndex_Type(Integer32):
    """Custom type accDnX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccDnX25FacIndex_Type.__name__ = "Integer32"
_AccDnX25FacIndex_Object = MibTableColumn
accDnX25FacIndex = _AccDnX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 21, 1, 23),
    _AccDnX25FacIndex_Type()
)
accDnX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnX25FacIndex.setStatus("mandatory")
_AccDnRtTable_Object = MibTable
accDnRtTable = _AccDnRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22)
)
if mibBuilder.loadTexts:
    accDnRtTable.setStatus("mandatory")
_AccDnRtEntry_Object = MibTableRow
accDnRtEntry = _AccDnRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1)
)
accDnRtEntry.setIndexNames(
    (0, "ACC-MIB", "accDnRtNode"),
)
if mibBuilder.loadTexts:
    accDnRtEntry.setStatus("mandatory")
_AccDnRtNode_Type = Integer32
_AccDnRtNode_Object = MibTableColumn
accDnRtNode = _AccDnRtNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 1),
    _AccDnRtNode_Type()
)
accDnRtNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtNode.setStatus("mandatory")
_AccDnRtHops_Type = Integer32
_AccDnRtHops_Object = MibTableColumn
accDnRtHops = _AccDnRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 2),
    _AccDnRtHops_Type()
)
accDnRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtHops.setStatus("mandatory")
_AccDnRtCost_Type = Integer32
_AccDnRtCost_Object = MibTableColumn
accDnRtCost = _AccDnRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 3),
    _AccDnRtCost_Type()
)
accDnRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtCost.setStatus("mandatory")
_AccDnRtCkt_Type = Integer32
_AccDnRtCkt_Object = MibTableColumn
accDnRtCkt = _AccDnRtCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 4),
    _AccDnRtCkt_Type()
)
accDnRtCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtCkt.setStatus("mandatory")
_AccDnRtNextHop_Type = Integer32
_AccDnRtNextHop_Object = MibTableColumn
accDnRtNextHop = _AccDnRtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 22, 1, 5),
    _AccDnRtNextHop_Type()
)
accDnRtNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnRtNextHop.setStatus("mandatory")
_AccDnAreaTable_Object = MibTable
accDnAreaTable = _AccDnAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23)
)
if mibBuilder.loadTexts:
    accDnAreaTable.setStatus("mandatory")
_AccDnAreaEntry_Object = MibTableRow
accDnAreaEntry = _AccDnAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1)
)
accDnAreaEntry.setIndexNames(
    (0, "ACC-MIB", "accDnAreaArea"),
)
if mibBuilder.loadTexts:
    accDnAreaEntry.setStatus("mandatory")
_AccDnAreaArea_Type = Integer32
_AccDnAreaArea_Object = MibTableColumn
accDnAreaArea = _AccDnAreaArea_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 1),
    _AccDnAreaArea_Type()
)
accDnAreaArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaArea.setStatus("mandatory")
_AccDnAreaHops_Type = Integer32
_AccDnAreaHops_Object = MibTableColumn
accDnAreaHops = _AccDnAreaHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 2),
    _AccDnAreaHops_Type()
)
accDnAreaHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaHops.setStatus("mandatory")
_AccDnAreaCost_Type = Integer32
_AccDnAreaCost_Object = MibTableColumn
accDnAreaCost = _AccDnAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 3),
    _AccDnAreaCost_Type()
)
accDnAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaCost.setStatus("mandatory")
_AccDnAreaCkt_Type = Integer32
_AccDnAreaCkt_Object = MibTableColumn
accDnAreaCkt = _AccDnAreaCkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 4),
    _AccDnAreaCkt_Type()
)
accDnAreaCkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaCkt.setStatus("mandatory")
_AccDnAreaNextHop_Type = Integer32
_AccDnAreaNextHop_Object = MibTableColumn
accDnAreaNextHop = _AccDnAreaNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 23, 1, 5),
    _AccDnAreaNextHop_Type()
)
accDnAreaNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAreaNextHop.setStatus("mandatory")
_AccDnRouteFilterTable_Object = MibTable
accDnRouteFilterTable = _AccDnRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24)
)
if mibBuilder.loadTexts:
    accDnRouteFilterTable.setStatus("mandatory")
_AccDnRouteFilterEntry_Object = MibTableRow
accDnRouteFilterEntry = _AccDnRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1)
)
accDnRouteFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accDnRouteFilterAdj"),
    (0, "ACC-MIB", "accDnRouteFilterNode"),
)
if mibBuilder.loadTexts:
    accDnRouteFilterEntry.setStatus("mandatory")


class _AccDnRouteFilterAdj_Type(Integer32):
    """Custom type accDnRouteFilterAdj based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnRouteFilterAdj_Type.__name__ = "Integer32"
_AccDnRouteFilterAdj_Object = MibTableColumn
accDnRouteFilterAdj = _AccDnRouteFilterAdj_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 1),
    _AccDnRouteFilterAdj_Type()
)
accDnRouteFilterAdj.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterAdj.setStatus("mandatory")


class _AccDnRouteFilterNode_Type(Integer32):
    """Custom type accDnRouteFilterNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnRouteFilterNode_Type.__name__ = "Integer32"
_AccDnRouteFilterNode_Object = MibTableColumn
accDnRouteFilterNode = _AccDnRouteFilterNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 2),
    _AccDnRouteFilterNode_Type()
)
accDnRouteFilterNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterNode.setStatus("mandatory")


class _AccDnRouteFilterDisposition_Type(Integer32):
    """Custom type accDnRouteFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccDnRouteFilterDisposition_Type.__name__ = "Integer32"
_AccDnRouteFilterDisposition_Object = MibTableColumn
accDnRouteFilterDisposition = _AccDnRouteFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 3),
    _AccDnRouteFilterDisposition_Type()
)
accDnRouteFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterDisposition.setStatus("mandatory")


class _AccDnRouteFilterEntStat_Type(Integer32):
    """Custom type accDnRouteFilterEntStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccDnRouteFilterEntStat_Type.__name__ = "Integer32"
_AccDnRouteFilterEntStat_Object = MibTableColumn
accDnRouteFilterEntStat = _AccDnRouteFilterEntStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 24, 1, 4),
    _AccDnRouteFilterEntStat_Type()
)
accDnRouteFilterEntStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnRouteFilterEntStat.setStatus("mandatory")
_AccDnForwardFilterTable_Object = MibTable
accDnForwardFilterTable = _AccDnForwardFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25)
)
if mibBuilder.loadTexts:
    accDnForwardFilterTable.setStatus("mandatory")
_AccDnForwardFilterEntry_Object = MibTableRow
accDnForwardFilterEntry = _AccDnForwardFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1)
)
accDnForwardFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accDnForwardFilterDest"),
    (0, "ACC-MIB", "accDnForwardFilterSource"),
)
if mibBuilder.loadTexts:
    accDnForwardFilterEntry.setStatus("mandatory")


class _AccDnForwardFilterDest_Type(Integer32):
    """Custom type accDnForwardFilterDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnForwardFilterDest_Type.__name__ = "Integer32"
_AccDnForwardFilterDest_Object = MibTableColumn
accDnForwardFilterDest = _AccDnForwardFilterDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 1),
    _AccDnForwardFilterDest_Type()
)
accDnForwardFilterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterDest.setStatus("mandatory")


class _AccDnForwardFilterSource_Type(Integer32):
    """Custom type accDnForwardFilterSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnForwardFilterSource_Type.__name__ = "Integer32"
_AccDnForwardFilterSource_Object = MibTableColumn
accDnForwardFilterSource = _AccDnForwardFilterSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 2),
    _AccDnForwardFilterSource_Type()
)
accDnForwardFilterSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterSource.setStatus("mandatory")


class _AccDnForwardFilterDisposition_Type(Integer32):
    """Custom type accDnForwardFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccDnForwardFilterDisposition_Type.__name__ = "Integer32"
_AccDnForwardFilterDisposition_Object = MibTableColumn
accDnForwardFilterDisposition = _AccDnForwardFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 3),
    _AccDnForwardFilterDisposition_Type()
)
accDnForwardFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterDisposition.setStatus("mandatory")


class _AccDnForwardFilterEntStat_Type(Integer32):
    """Custom type accDnForwardFilterEntStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccDnForwardFilterEntStat_Type.__name__ = "Integer32"
_AccDnForwardFilterEntStat_Object = MibTableColumn
accDnForwardFilterEntStat = _AccDnForwardFilterEntStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 25, 1, 4),
    _AccDnForwardFilterEntStat_Type()
)
accDnForwardFilterEntStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDnForwardFilterEntStat.setStatus("mandatory")
_AccDnAdjTable_Object = MibTable
accDnAdjTable = _AccDnAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26)
)
if mibBuilder.loadTexts:
    accDnAdjTable.setStatus("mandatory")
_AccDnAdjEntry_Object = MibTableRow
accDnAdjEntry = _AccDnAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1)
)
accDnAdjEntry.setIndexNames(
    (0, "ACC-MIB", "accDnAdjNode"),
)
if mibBuilder.loadTexts:
    accDnAdjEntry.setStatus("mandatory")


class _AccDnAdjNode_Type(Integer32):
    """Custom type accDnAdjNode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDnAdjNode_Type.__name__ = "Integer32"
_AccDnAdjNode_Object = MibTableColumn
accDnAdjNode = _AccDnAdjNode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 1),
    _AccDnAdjNode_Type()
)
accDnAdjNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjNode.setStatus("mandatory")


class _AccDnAdjType_Type(Integer32):
    """Custom type accDnAdjType based on Integer32"""
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
        *(("endNode", 4),
          ("level1", 3),
          ("level2", 2),
          ("level2Only", 1))
    )


_AccDnAdjType_Type.__name__ = "Integer32"
_AccDnAdjType_Object = MibTableColumn
accDnAdjType = _AccDnAdjType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 2),
    _AccDnAdjType_Type()
)
accDnAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjType.setStatus("mandatory")
_AccDnAdjCircuit_Type = Integer32
_AccDnAdjCircuit_Object = MibTableColumn
accDnAdjCircuit = _AccDnAdjCircuit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 3),
    _AccDnAdjCircuit_Type()
)
accDnAdjCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjCircuit.setStatus("mandatory")


class _AccDnAdjState_Type(Integer32):
    """Custom type accDnAdjState based on Integer32"""
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
        *(("circuitFailed", 3),
          ("initializing", 2),
          ("timedOut", 4),
          ("up", 1))
    )


_AccDnAdjState_Type.__name__ = "Integer32"
_AccDnAdjState_Object = MibTableColumn
accDnAdjState = _AccDnAdjState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 19, 26, 1, 4),
    _AccDnAdjState_Type()
)
accDnAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDnAdjState.setStatus("mandatory")
_AccFr_ObjectIdentity = ObjectIdentity
accFr = _AccFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20)
)
_AccFrAtTable_Object = MibTable
accFrAtTable = _AccFrAtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1)
)
if mibBuilder.loadTexts:
    accFrAtTable.setStatus("mandatory")
_AccFrAtEntry_Object = MibTableRow
accFrAtEntry = _AccFrAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1)
)
accFrAtEntry.setIndexNames(
    (0, "ACC-MIB", "accFrAtIfIndex"),
    (0, "ACC-MIB", "accFrIpAddress"),
)
if mibBuilder.loadTexts:
    accFrAtEntry.setStatus("mandatory")
_AccFrAtIfIndex_Type = Integer32
_AccFrAtIfIndex_Object = MibTableColumn
accFrAtIfIndex = _AccFrAtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 1),
    _AccFrAtIfIndex_Type()
)
accFrAtIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrAtIfIndex.setStatus("mandatory")
_AccFrIpAddress_Type = IpAddress
_AccFrIpAddress_Object = MibTableColumn
accFrIpAddress = _AccFrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 2),
    _AccFrIpAddress_Type()
)
accFrIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrIpAddress.setStatus("mandatory")
_AccFrDLCI_Type = Integer32
_AccFrDLCI_Object = MibTableColumn
accFrDLCI = _AccFrDLCI_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 3),
    _AccFrDLCI_Type()
)
accFrDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDLCI.setStatus("mandatory")


class _AccFrStatus_Type(Integer32):
    """Custom type accFrStatus based on Integer32"""
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
        *(("confirm-pending", 3),
          ("dynamic", 2),
          ("not-connected", 4),
          ("permanent", 1))
    )


_AccFrStatus_Type.__name__ = "Integer32"
_AccFrStatus_Object = MibTableColumn
accFrStatus = _AccFrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 1, 1, 4),
    _AccFrStatus_Type()
)
accFrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrStatus.setStatus("mandatory")
_AccFrStatTable_Object = MibTable
accFrStatTable = _AccFrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2)
)
if mibBuilder.loadTexts:
    accFrStatTable.setStatus("mandatory")
_AccFrStatEntry_Object = MibTableRow
accFrStatEntry = _AccFrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1)
)
accFrStatEntry.setIndexNames(
    (0, "ACC-MIB", "accFrIndex"),
)
if mibBuilder.loadTexts:
    accFrStatEntry.setStatus("mandatory")
_AccFrIndex_Type = Integer32
_AccFrIndex_Object = MibTableColumn
accFrIndex = _AccFrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 1),
    _AccFrIndex_Type()
)
accFrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrIndex.setStatus("mandatory")
_AccFrStatRcvDrops_Type = Counter32
_AccFrStatRcvDrops_Object = MibTableColumn
accFrStatRcvDrops = _AccFrStatRcvDrops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 2),
    _AccFrStatRcvDrops_Type()
)
accFrStatRcvDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRcvDrops.setStatus("mandatory")
_AccFrStatShorts_Type = Counter32
_AccFrStatShorts_Object = MibTableColumn
accFrStatShorts = _AccFrStatShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 3),
    _AccFrStatShorts_Type()
)
accFrStatShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatShorts.setStatus("mandatory")
_AccFrStatIllDlcis_Type = Counter32
_AccFrStatIllDlcis_Object = MibTableColumn
accFrStatIllDlcis = _AccFrStatIllDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 4),
    _AccFrStatIllDlcis_Type()
)
accFrStatIllDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatIllDlcis.setStatus("mandatory")
_AccFrStatUnkDlcis_Type = Counter32
_AccFrStatUnkDlcis_Object = MibTableColumn
accFrStatUnkDlcis = _AccFrStatUnkDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 5),
    _AccFrStatUnkDlcis_Type()
)
accFrStatUnkDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkDlcis.setStatus("mandatory")
_AccFrStatUnkProtos_Type = Counter32
_AccFrStatUnkProtos_Object = MibTableColumn
accFrStatUnkProtos = _AccFrStatUnkProtos_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 6),
    _AccFrStatUnkProtos_Type()
)
accFrStatUnkProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkProtos.setStatus("mandatory")
_AccFrStatRsrvDlcis_Type = Counter32
_AccFrStatRsrvDlcis_Object = MibTableColumn
accFrStatRsrvDlcis = _AccFrStatRsrvDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 7),
    _AccFrStatRsrvDlcis_Type()
)
accFrStatRsrvDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRsrvDlcis.setStatus("mandatory")
_AccFrStatXmtDrops_Type = Counter32
_AccFrStatXmtDrops_Object = MibTableColumn
accFrStatXmtDrops = _AccFrStatXmtDrops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 8),
    _AccFrStatXmtDrops_Type()
)
accFrStatXmtDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatXmtDrops.setStatus("mandatory")
_AccFrStatErrTime_Type = TimeTicks
_AccFrStatErrTime_Object = MibTableColumn
accFrStatErrTime = _AccFrStatErrTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 9),
    _AccFrStatErrTime_Type()
)
accFrStatErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrTime.setStatus("mandatory")


class _AccFrStatErrType_Type(Integer32):
    """Custom type accFrStatErrType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 11),
          ("dlcmiSequenceErr", 13),
          ("dlcmiUnknownIE", 12),
          ("dlcmiUnknownRpt", 14),
          ("illDlci", 3),
          ("illegalDLCI", 10),
          ("rcvDrop", 1),
          ("receiveLong", 9),
          ("rsrvDlci", 6),
          ("short", 2),
          ("unkDlci", 4),
          ("unkProto", 5),
          ("unknownError", 8),
          ("xmtDrop", 7))
    )


_AccFrStatErrType_Type.__name__ = "Integer32"
_AccFrStatErrType_Object = MibTableColumn
accFrStatErrType = _AccFrStatErrType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 10),
    _AccFrStatErrType_Type()
)
accFrStatErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrType.setStatus("mandatory")
_AccFrStatErrDlci_Type = Integer32
_AccFrStatErrDlci_Object = MibTableColumn
accFrStatErrDlci = _AccFrStatErrDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 11),
    _AccFrStatErrDlci_Type()
)
accFrStatErrDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrDlci.setStatus("mandatory")
_AccFrStatErrProto_Type = Integer32
_AccFrStatErrProto_Object = MibTableColumn
accFrStatErrProto = _AccFrStatErrProto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 12),
    _AccFrStatErrProto_Type()
)
accFrStatErrProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatErrProto.setStatus("mandatory")


class _AccFrLinkState_Type(Integer32):
    """Custom type accFrLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("idle", 3),
          ("up", 2))
    )


_AccFrLinkState_Type.__name__ = "Integer32"
_AccFrLinkState_Object = MibTableColumn
accFrLinkState = _AccFrLinkState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 13),
    _AccFrLinkState_Type()
)
accFrLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrLinkState.setStatus("mandatory")
_AccFrStatUnks_Type = Counter32
_AccFrStatUnks_Object = MibTableColumn
accFrStatUnks = _AccFrStatUnks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 14),
    _AccFrStatUnks_Type()
)
accFrStatUnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnks.setStatus("mandatory")
_AccFrStatRcvLongs_Type = Counter32
_AccFrStatRcvLongs_Object = MibTableColumn
accFrStatRcvLongs = _AccFrStatRcvLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 15),
    _AccFrStatRcvLongs_Type()
)
accFrStatRcvLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatRcvLongs.setStatus("mandatory")
_AccFrStatIlgDlcis_Type = Counter32
_AccFrStatIlgDlcis_Object = MibTableColumn
accFrStatIlgDlcis = _AccFrStatIlgDlcis_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 16),
    _AccFrStatIlgDlcis_Type()
)
accFrStatIlgDlcis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatIlgDlcis.setStatus("mandatory")
_AccFrStatProtoErrs_Type = Counter32
_AccFrStatProtoErrs_Object = MibTableColumn
accFrStatProtoErrs = _AccFrStatProtoErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 17),
    _AccFrStatProtoErrs_Type()
)
accFrStatProtoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatProtoErrs.setStatus("mandatory")
_AccFrStatUnkIes_Type = Counter32
_AccFrStatUnkIes_Object = MibTableColumn
accFrStatUnkIes = _AccFrStatUnkIes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 18),
    _AccFrStatUnkIes_Type()
)
accFrStatUnkIes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkIes.setStatus("mandatory")
_AccFrStatSeqErrs_Type = Counter32
_AccFrStatSeqErrs_Object = MibTableColumn
accFrStatSeqErrs = _AccFrStatSeqErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 19),
    _AccFrStatSeqErrs_Type()
)
accFrStatSeqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatSeqErrs.setStatus("mandatory")
_AccFrStatUnkRpts_Type = Counter32
_AccFrStatUnkRpts_Object = MibTableColumn
accFrStatUnkRpts = _AccFrStatUnkRpts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 2, 1, 20),
    _AccFrStatUnkRpts_Type()
)
accFrStatUnkRpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrStatUnkRpts.setStatus("mandatory")
_AccFrParmTable_Object = MibTable
accFrParmTable = _AccFrParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3)
)
if mibBuilder.loadTexts:
    accFrParmTable.setStatus("mandatory")
_AccFrParmEntry_Object = MibTableRow
accFrParmEntry = _AccFrParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1)
)
accFrParmEntry.setIndexNames(
    (0, "ACC-MIB", "accFrParmIndex"),
)
if mibBuilder.loadTexts:
    accFrParmEntry.setStatus("mandatory")
_AccFrParmIndex_Type = Integer32
_AccFrParmIndex_Object = MibTableColumn
accFrParmIndex = _AccFrParmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 1),
    _AccFrParmIndex_Type()
)
accFrParmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrParmIndex.setStatus("mandatory")


class _AccFrParmAddrFmt_Type(Integer32):
    """Custom type accFrParmAddrFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("draft-q922", 2),
          ("q921", 1),
          ("q922", 3))
    )


_AccFrParmAddrFmt_Type.__name__ = "Integer32"
_AccFrParmAddrFmt_Object = MibTableColumn
accFrParmAddrFmt = _AccFrParmAddrFmt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 2),
    _AccFrParmAddrFmt_Type()
)
accFrParmAddrFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmAddrFmt.setStatus("mandatory")


class _AccFrParmAddrLen_Type(Integer32):
    """Custom type accFrParmAddrLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_AccFrParmAddrLen_Type.__name__ = "Integer32"
_AccFrParmAddrLen_Object = MibTableColumn
accFrParmAddrLen = _AccFrParmAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 3),
    _AccFrParmAddrLen_Type()
)
accFrParmAddrLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmAddrLen.setStatus("mandatory")


class _AccFrParmEncap_Type(Integer32):
    """Custom type accFrParmEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("early", 1),
          ("ietf", 2))
    )


_AccFrParmEncap_Type.__name__ = "Integer32"
_AccFrParmEncap_Object = MibTableColumn
accFrParmEncap = _AccFrParmEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 4),
    _AccFrParmEncap_Type()
)
accFrParmEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrParmEncap.setStatus("mandatory")


class _AccFrDlcmiState_Type(Integer32):
    """Custom type accFrDlcmiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexd", 3),
          ("lmi", 2),
          ("off", 1))
    )


_AccFrDlcmiState_Type.__name__ = "Integer32"
_AccFrDlcmiState_Object = MibTableColumn
accFrDlcmiState = _AccFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 5),
    _AccFrDlcmiState_Type()
)
accFrDlcmiState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiState.setStatus("mandatory")


class _AccFrDlcmiPollInt_Type(Integer32):
    """Custom type accFrDlcmiPollInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AccFrDlcmiPollInt_Type.__name__ = "Integer32"
_AccFrDlcmiPollInt_Object = MibTableColumn
accFrDlcmiPollInt = _AccFrDlcmiPollInt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 6),
    _AccFrDlcmiPollInt_Type()
)
accFrDlcmiPollInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiPollInt.setStatus("mandatory")


class _AccFrDlcmiFullStatEnq_Type(Integer32):
    """Custom type accFrDlcmiFullStatEnq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccFrDlcmiFullStatEnq_Type.__name__ = "Integer32"
_AccFrDlcmiFullStatEnq_Object = MibTableColumn
accFrDlcmiFullStatEnq = _AccFrDlcmiFullStatEnq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 7),
    _AccFrDlcmiFullStatEnq_Type()
)
accFrDlcmiFullStatEnq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiFullStatEnq.setStatus("mandatory")


class _AccFrDlcmiErrThres_Type(Integer32):
    """Custom type accFrDlcmiErrThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccFrDlcmiErrThres_Type.__name__ = "Integer32"
_AccFrDlcmiErrThres_Object = MibTableColumn
accFrDlcmiErrThres = _AccFrDlcmiErrThres_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 8),
    _AccFrDlcmiErrThres_Type()
)
accFrDlcmiErrThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiErrThres.setStatus("mandatory")


class _AccFrDlcmiMonEvents_Type(Integer32):
    """Custom type accFrDlcmiMonEvents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AccFrDlcmiMonEvents_Type.__name__ = "Integer32"
_AccFrDlcmiMonEvents_Object = MibTableColumn
accFrDlcmiMonEvents = _AccFrDlcmiMonEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 9),
    _AccFrDlcmiMonEvents_Type()
)
accFrDlcmiMonEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiMonEvents.setStatus("mandatory")


class _AccFrDlcmiType_Type(Integer32):
    """Custom type accFrDlcmiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("user", 1))
    )


_AccFrDlcmiType_Type.__name__ = "Integer32"
_AccFrDlcmiType_Object = MibTableColumn
accFrDlcmiType = _AccFrDlcmiType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 10),
    _AccFrDlcmiType_Type()
)
accFrDlcmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiType.setStatus("mandatory")


class _AccFrDlcmiIdleTimer_Type(Integer32):
    """Custom type accFrDlcmiIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccFrDlcmiIdleTimer_Type.__name__ = "Integer32"
_AccFrDlcmiIdleTimer_Object = MibTableColumn
accFrDlcmiIdleTimer = _AccFrDlcmiIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 3, 1, 11),
    _AccFrDlcmiIdleTimer_Type()
)
accFrDlcmiIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFrDlcmiIdleTimer.setStatus("mandatory")
_AccFrCktTable_Object = MibTable
accFrCktTable = _AccFrCktTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4)
)
if mibBuilder.loadTexts:
    accFrCktTable.setStatus("mandatory")
_AccFrCktEntry_Object = MibTableRow
accFrCktEntry = _AccFrCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1)
)
accFrCktEntry.setIndexNames(
    (0, "ACC-MIB", "accFrCktIfIndex"),
)
if mibBuilder.loadTexts:
    accFrCktEntry.setStatus("mandatory")
_AccFrCktIfIndex_Type = Integer32
_AccFrCktIfIndex_Object = MibTableColumn
accFrCktIfIndex = _AccFrCktIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 1),
    _AccFrCktIfIndex_Type()
)
accFrCktIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktIfIndex.setStatus("mandatory")
_AccFrCktDlci_Type = Integer32
_AccFrCktDlci_Object = MibTableColumn
accFrCktDlci = _AccFrCktDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 2),
    _AccFrCktDlci_Type()
)
accFrCktDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktDlci.setStatus("mandatory")


class _AccFrCktState_Type(Integer32):
    """Custom type accFrCktState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_AccFrCktState_Type.__name__ = "Integer32"
_AccFrCktState_Object = MibTableColumn
accFrCktState = _AccFrCktState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 3),
    _AccFrCktState_Type()
)
accFrCktState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktState.setStatus("mandatory")
_AccFrCktFECNrcvds_Type = Counter32
_AccFrCktFECNrcvds_Object = MibTableColumn
accFrCktFECNrcvds = _AccFrCktFECNrcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 4),
    _AccFrCktFECNrcvds_Type()
)
accFrCktFECNrcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFECNrcvds.setStatus("mandatory")
_AccFrCktBECNrcvds_Type = Counter32
_AccFrCktBECNrcvds_Object = MibTableColumn
accFrCktBECNrcvds = _AccFrCktBECNrcvds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 5),
    _AccFrCktBECNrcvds_Type()
)
accFrCktBECNrcvds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktBECNrcvds.setStatus("mandatory")
_AccFrCktFrameXmts_Type = Counter32
_AccFrCktFrameXmts_Object = MibTableColumn
accFrCktFrameXmts = _AccFrCktFrameXmts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 6),
    _AccFrCktFrameXmts_Type()
)
accFrCktFrameXmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFrameXmts.setStatus("mandatory")
_AccFrCktOctetXmts_Type = Counter32
_AccFrCktOctetXmts_Object = MibTableColumn
accFrCktOctetXmts = _AccFrCktOctetXmts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 7),
    _AccFrCktOctetXmts_Type()
)
accFrCktOctetXmts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktOctetXmts.setStatus("mandatory")
_AccFrCktFrameRcvs_Type = Counter32
_AccFrCktFrameRcvs_Object = MibTableColumn
accFrCktFrameRcvs = _AccFrCktFrameRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 8),
    _AccFrCktFrameRcvs_Type()
)
accFrCktFrameRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktFrameRcvs.setStatus("mandatory")
_AccFrCktOctetRcvs_Type = Counter32
_AccFrCktOctetRcvs_Object = MibTableColumn
accFrCktOctetRcvs = _AccFrCktOctetRcvs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 9),
    _AccFrCktOctetRcvs_Type()
)
accFrCktOctetRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktOctetRcvs.setStatus("mandatory")
_AccFrCktCreateTime_Type = TimeTicks
_AccFrCktCreateTime_Object = MibTableColumn
accFrCktCreateTime = _AccFrCktCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 10),
    _AccFrCktCreateTime_Type()
)
accFrCktCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktCreateTime.setStatus("mandatory")
_AccFrCktChangeTime_Type = TimeTicks
_AccFrCktChangeTime_Object = MibTableColumn
accFrCktChangeTime = _AccFrCktChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 11),
    _AccFrCktChangeTime_Type()
)
accFrCktChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFrCktChangeTime.setStatus("mandatory")


class _AccFfrCktLoop_Type(Integer32):
    """Custom type accFfrCktLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loop", 2),
          ("normal", 1))
    )


_AccFfrCktLoop_Type.__name__ = "Integer32"
_AccFfrCktLoop_Object = MibTableColumn
accFfrCktLoop = _AccFfrCktLoop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 4, 1, 12),
    _AccFfrCktLoop_Type()
)
accFfrCktLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrCktLoop.setStatus("mandatory")
_AccFfrSwitchParameterTable_Object = MibTable
accFfrSwitchParameterTable = _AccFfrSwitchParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5)
)
if mibBuilder.loadTexts:
    accFfrSwitchParameterTable.setStatus("mandatory")
_AccFfrSwitchParameterEntry_Object = MibTableRow
accFfrSwitchParameterEntry = _AccFfrSwitchParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1)
)
accFfrSwitchParameterEntry.setIndexNames(
    (0, "ACC-MIB", "accFfrSwitchIfindex1"),
    (0, "ACC-MIB", "accFfrSwitchDlci1"),
)
if mibBuilder.loadTexts:
    accFfrSwitchParameterEntry.setStatus("mandatory")
_AccFfrSwitchIfindex1_Type = Integer32
_AccFfrSwitchIfindex1_Object = MibTableColumn
accFfrSwitchIfindex1 = _AccFfrSwitchIfindex1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 1),
    _AccFfrSwitchIfindex1_Type()
)
accFfrSwitchIfindex1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchIfindex1.setStatus("mandatory")
_AccFfrSwitchDlci1_Type = Integer32
_AccFfrSwitchDlci1_Object = MibTableColumn
accFfrSwitchDlci1 = _AccFfrSwitchDlci1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 2),
    _AccFfrSwitchDlci1_Type()
)
accFfrSwitchDlci1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchDlci1.setStatus("mandatory")
_AccFfrSwitchIfindex2_Type = Integer32
_AccFfrSwitchIfindex2_Object = MibTableColumn
accFfrSwitchIfindex2 = _AccFfrSwitchIfindex2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 3),
    _AccFfrSwitchIfindex2_Type()
)
accFfrSwitchIfindex2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchIfindex2.setStatus("mandatory")
_AccFfrSwitchDlci2_Type = Integer32
_AccFfrSwitchDlci2_Object = MibTableColumn
accFfrSwitchDlci2 = _AccFfrSwitchDlci2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 4),
    _AccFfrSwitchDlci2_Type()
)
accFfrSwitchDlci2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchDlci2.setStatus("mandatory")


class _AccFfrSwitchStatus_Type(Integer32):
    """Custom type accFfrSwitchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 128),
          ("disable", 2),
          ("enable", 1))
    )


_AccFfrSwitchStatus_Type.__name__ = "Integer32"
_AccFfrSwitchStatus_Object = MibTableColumn
accFfrSwitchStatus = _AccFfrSwitchStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 20, 5, 1, 5),
    _AccFfrSwitchStatus_Type()
)
accFfrSwitchStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accFfrSwitchStatus.setStatus("mandatory")
_AccXns_ObjectIdentity = ObjectIdentity
accXns = _AccXns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21)
)
_AccXnsParms_ObjectIdentity = ObjectIdentity
accXnsParms = _AccXnsParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1)
)


class _AccXnsAdStat_Type(Integer32):
    """Custom type accXnsAdStat based on Integer32"""
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


_AccXnsAdStat_Type.__name__ = "Integer32"
_AccXnsAdStat_Object = MibScalar
accXnsAdStat = _AccXnsAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 1),
    _AccXnsAdStat_Type()
)
accXnsAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsAdStat.setStatus("mandatory")


class _AccXnsCkSum_Type(Integer32):
    """Custom type accXnsCkSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("header", 3),
          ("off", 1),
          ("packet", 2))
    )


_AccXnsCkSum_Type.__name__ = "Integer32"
_AccXnsCkSum_Object = MibScalar
accXnsCkSum = _AccXnsCkSum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 2),
    _AccXnsCkSum_Type()
)
accXnsCkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsCkSum.setStatus("mandatory")


class _AccXnsSpltHorz_Type(Integer32):
    """Custom type accXnsSpltHorz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("poison", 3),
          ("simple", 2))
    )


_AccXnsSpltHorz_Type.__name__ = "Integer32"
_AccXnsSpltHorz_Object = MibScalar
accXnsSpltHorz = _AccXnsSpltHorz_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 3),
    _AccXnsSpltHorz_Type()
)
accXnsSpltHorz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsSpltHorz.setStatus("mandatory")


class _AccXnsAllNets_Type(Integer32):
    """Custom type accXnsAllNets based on Integer32"""
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


_AccXnsAllNets_Type.__name__ = "Integer32"
_AccXnsAllNets_Object = MibScalar
accXnsAllNets = _AccXnsAllNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 4),
    _AccXnsAllNets_Type()
)
accXnsAllNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsAllNets.setStatus("mandatory")


class _AccXnsMode_Type(Integer32):
    """Custom type accXnsMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ub", 2),
          ("xns", 1))
    )


_AccXnsMode_Type.__name__ = "Integer32"
_AccXnsMode_Object = MibScalar
accXnsMode = _AccXnsMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 1, 5),
    _AccXnsMode_Type()
)
accXnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsMode.setStatus("mandatory")
_AccXnsNetTable_Object = MibTable
accXnsNetTable = _AccXnsNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2)
)
if mibBuilder.loadTexts:
    accXnsNetTable.setStatus("mandatory")
_AccXnsNetEntry_Object = MibTableRow
accXnsNetEntry = _AccXnsNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1)
)
accXnsNetEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsNetPort"),
)
if mibBuilder.loadTexts:
    accXnsNetEntry.setStatus("mandatory")
_AccXnsNetPort_Type = Integer32
_AccXnsNetPort_Object = MibTableColumn
accXnsNetPort = _AccXnsNetPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 1),
    _AccXnsNetPort_Type()
)
accXnsNetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetPort.setStatus("mandatory")
_AccXnsNetNumber_Type = OctetString
_AccXnsNetNumber_Object = MibTableColumn
accXnsNetNumber = _AccXnsNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 2),
    _AccXnsNetNumber_Type()
)
accXnsNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetNumber.setStatus("mandatory")


class _AccXnsNetType_Type(Integer32):
    """Custom type accXnsNetType based on Integer32"""
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
        *(("enet", 1),
          ("ffr", 5),
          ("lapb", 3),
          ("token-ring", 2),
          ("x25", 4))
    )


_AccXnsNetType_Type.__name__ = "Integer32"
_AccXnsNetType_Object = MibTableColumn
accXnsNetType = _AccXnsNetType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 3),
    _AccXnsNetType_Type()
)
accXnsNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetType.setStatus("mandatory")


class _AccXnsNetEncap_Type(Integer32):
    """Custom type accXnsNetEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccXnsNetEncap_Type.__name__ = "Integer32"
_AccXnsNetEncap_Object = MibTableColumn
accXnsNetEncap = _AccXnsNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 4),
    _AccXnsNetEncap_Type()
)
accXnsNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetEncap.setStatus("mandatory")


class _AccXnsNetSlot_Type(Integer32):
    """Custom type accXnsNetSlot based on Integer32"""
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
        *(("b1", 4),
          ("j1", 1),
          ("j2", 2),
          ("j3", 3))
    )


_AccXnsNetSlot_Type.__name__ = "Integer32"
_AccXnsNetSlot_Object = MibTableColumn
accXnsNetSlot = _AccXnsNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 5),
    _AccXnsNetSlot_Type()
)
accXnsNetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetSlot.setStatus("mandatory")


class _AccXnsNetAdStat_Type(Integer32):
    """Custom type accXnsNetAdStat based on Integer32"""
    defaultValue = 1

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


_AccXnsNetAdStat_Type.__name__ = "Integer32"
_AccXnsNetAdStat_Object = MibTableColumn
accXnsNetAdStat = _AccXnsNetAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 6),
    _AccXnsNetAdStat_Type()
)
accXnsNetAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetAdStat.setStatus("mandatory")


class _AccXnsNetMtu_Type(Integer32):
    """Custom type accXnsNetMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_AccXnsNetMtu_Type.__name__ = "Integer32"
_AccXnsNetMtu_Object = MibTableColumn
accXnsNetMtu = _AccXnsNetMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 7),
    _AccXnsNetMtu_Type()
)
accXnsNetMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetMtu.setStatus("mandatory")


class _AccXnsNetUpdate_Type(TimeTicks):
    """Custom type accXnsNetUpdate based on TimeTicks"""
    defaultValue = 1500


_AccXnsNetUpdate_Object = MibTableColumn
accXnsNetUpdate = _AccXnsNetUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 8),
    _AccXnsNetUpdate_Type()
)
accXnsNetUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUpdate.setStatus("mandatory")


class _AccXnsNetHops_Type(Integer32):
    """Custom type accXnsNetHops based on Integer32"""
    defaultValue = 1


_AccXnsNetHops_Object = MibTableColumn
accXnsNetHops = _AccXnsNetHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 9),
    _AccXnsNetHops_Type()
)
accXnsNetHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetHops.setStatus("mandatory")
_AccXnsNetCost_Type = Integer32
_AccXnsNetCost_Object = MibTableColumn
accXnsNetCost = _AccXnsNetCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 10),
    _AccXnsNetCost_Type()
)
accXnsNetCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetCost.setStatus("mandatory")
_AccXnsNetX25InOutAddr_Type = DisplayString
_AccXnsNetX25InOutAddr_Object = MibTableColumn
accXnsNetX25InOutAddr = _AccXnsNetX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 11),
    _AccXnsNetX25InOutAddr_Type()
)
accXnsNetX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25InOutAddr.setStatus("mandatory")
_AccXnsNetX25InAddr_Type = DisplayString
_AccXnsNetX25InAddr_Object = MibTableColumn
accXnsNetX25InAddr = _AccXnsNetX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 12),
    _AccXnsNetX25InAddr_Type()
)
accXnsNetX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25InAddr.setStatus("mandatory")


class _AccXnsNetX25Idle_Type(TimeTicks):
    """Custom type accXnsNetX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccXnsNetX25Idle_Object = MibTableColumn
accXnsNetX25Idle = _AccXnsNetX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 13),
    _AccXnsNetX25Idle_Type()
)
accXnsNetX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25Idle.setStatus("mandatory")


class _AccXnsNetX25PktVal_Type(Integer32):
    """Custom type accXnsNetX25PktVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccXnsNetX25PktVal_Type.__name__ = "Integer32"
_AccXnsNetX25PktVal_Object = MibTableColumn
accXnsNetX25PktVal = _AccXnsNetX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 14),
    _AccXnsNetX25PktVal_Type()
)
accXnsNetX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25PktVal.setStatus("mandatory")


class _AccXnsNetX25PktWin_Type(Integer32):
    """Custom type accXnsNetX25PktWin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccXnsNetX25PktWin_Type.__name__ = "Integer32"
_AccXnsNetX25PktWin_Object = MibTableColumn
accXnsNetX25PktWin = _AccXnsNetX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 15),
    _AccXnsNetX25PktWin_Type()
)
accXnsNetX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25PktWin.setStatus("mandatory")


class _AccXnsNetEntryStat_Type(Integer32):
    """Custom type accXnsNetEntryStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccXnsNetEntryStat_Type.__name__ = "Integer32"
_AccXnsNetEntryStat_Object = MibTableColumn
accXnsNetEntryStat = _AccXnsNetEntryStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 16),
    _AccXnsNetEntryStat_Type()
)
accXnsNetEntryStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetEntryStat.setStatus("mandatory")
_AccXnsNetUbUpdate_Type = TimeTicks
_AccXnsNetUbUpdate_Object = MibTableColumn
accXnsNetUbUpdate = _AccXnsNetUbUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 17),
    _AccXnsNetUbUpdate_Type()
)
accXnsNetUbUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbUpdate.setStatus("mandatory")


class _AccXnsNetUbTtl_Type(TimeTicks):
    """Custom type accXnsNetUbTtl based on TimeTicks"""
    defaultValue = 1500


_AccXnsNetUbTtl_Object = MibTableColumn
accXnsNetUbTtl = _AccXnsNetUbTtl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 18),
    _AccXnsNetUbTtl_Type()
)
accXnsNetUbTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbTtl.setStatus("mandatory")
_AccXnsNetUbQT1_Type = TimeTicks
_AccXnsNetUbQT1_Object = MibTableColumn
accXnsNetUbQT1 = _AccXnsNetUbQT1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 19),
    _AccXnsNetUbQT1_Type()
)
accXnsNetUbQT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbQT1.setStatus("mandatory")
_AccXnsNetUbQT2_Type = TimeTicks
_AccXnsNetUbQT2_Object = MibTableColumn
accXnsNetUbQT2 = _AccXnsNetUbQT2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 20),
    _AccXnsNetUbQT2_Type()
)
accXnsNetUbQT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetUbQT2.setStatus("mandatory")
_AccXnsNetFncAddr_Type = OctetString
_AccXnsNetFncAddr_Object = MibTableColumn
accXnsNetFncAddr = _AccXnsNetFncAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 21),
    _AccXnsNetFncAddr_Type()
)
accXnsNetFncAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFncAddr.setStatus("mandatory")


class _AccXnsNetSrMode_Type(Integer32):
    """Custom type accXnsNetSrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ape", 2),
          ("off", 1),
          ("spe", 3))
    )


_AccXnsNetSrMode_Type.__name__ = "Integer32"
_AccXnsNetSrMode_Object = MibTableColumn
accXnsNetSrMode = _AccXnsNetSrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 22),
    _AccXnsNetSrMode_Type()
)
accXnsNetSrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetSrMode.setStatus("mandatory")


class _AccXnsNetX25FacIndex_Type(Integer32):
    """Custom type accXnsNetX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccXnsNetX25FacIndex_Type.__name__ = "Integer32"
_AccXnsNetX25FacIndex_Object = MibTableColumn
accXnsNetX25FacIndex = _AccXnsNetX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 23),
    _AccXnsNetX25FacIndex_Type()
)
accXnsNetX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetX25FacIndex.setStatus("mandatory")
_AccXnsNetDlci_Type = Integer32
_AccXnsNetDlci_Object = MibTableColumn
accXnsNetDlci = _AccXnsNetDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 2, 1, 24),
    _AccXnsNetDlci_Type()
)
accXnsNetDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetDlci.setStatus("mandatory")
_AccXnsRouteTable_Object = MibTable
accXnsRouteTable = _AccXnsRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3)
)
if mibBuilder.loadTexts:
    accXnsRouteTable.setStatus("mandatory")
_AccXnsRouteEntry_Object = MibTableRow
accXnsRouteEntry = _AccXnsRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1)
)
accXnsRouteEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsRtDest"),
)
if mibBuilder.loadTexts:
    accXnsRouteEntry.setStatus("mandatory")
_AccXnsRtDest_Type = OctetString
_AccXnsRtDest_Object = MibTableColumn
accXnsRtDest = _AccXnsRtDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 1),
    _AccXnsRtDest_Type()
)
accXnsRtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtDest.setStatus("mandatory")
_AccXnsRtNxtNet_Type = OctetString
_AccXnsRtNxtNet_Object = MibTableColumn
accXnsRtNxtNet = _AccXnsRtNxtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 2),
    _AccXnsRtNxtNet_Type()
)
accXnsRtNxtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtNxtNet.setStatus("mandatory")
_AccXnsRtRouter_Type = OctetString
_AccXnsRtRouter_Object = MibTableColumn
accXnsRtRouter = _AccXnsRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 3),
    _AccXnsRtRouter_Type()
)
accXnsRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtRouter.setStatus("mandatory")
_AccXnsRtHops_Type = Integer32
_AccXnsRtHops_Object = MibTableColumn
accXnsRtHops = _AccXnsRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 4),
    _AccXnsRtHops_Type()
)
accXnsRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtHops.setStatus("mandatory")
_AccXnsRtCost_Type = Integer32
_AccXnsRtCost_Object = MibTableColumn
accXnsRtCost = _AccXnsRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 5),
    _AccXnsRtCost_Type()
)
accXnsRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtCost.setStatus("mandatory")


class _AccXnsRtType_Type(Integer32):
    """Custom type accXnsRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("public", 1),
          ("static", 3))
    )


_AccXnsRtType_Type.__name__ = "Integer32"
_AccXnsRtType_Object = MibTableColumn
accXnsRtType = _AccXnsRtType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 6),
    _AccXnsRtType_Type()
)
accXnsRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtType.setStatus("mandatory")


class _AccXnsRtOwner_Type(Integer32):
    """Custom type accXnsRtOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lli", 1),
          ("nms", 2),
          ("rip", 3))
    )


_AccXnsRtOwner_Type.__name__ = "Integer32"
_AccXnsRtOwner_Object = MibTableColumn
accXnsRtOwner = _AccXnsRtOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 7),
    _AccXnsRtOwner_Type()
)
accXnsRtOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtOwner.setStatus("mandatory")
_AccXnsRtAge_Type = TimeTicks
_AccXnsRtAge_Object = MibTableColumn
accXnsRtAge = _AccXnsRtAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 8),
    _AccXnsRtAge_Type()
)
accXnsRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtAge.setStatus("mandatory")
_AccXnsRtPort_Type = Integer32
_AccXnsRtPort_Object = MibTableColumn
accXnsRtPort = _AccXnsRtPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 3, 1, 9),
    _AccXnsRtPort_Type()
)
accXnsRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRtPort.setStatus("mandatory")
_AccXnsRipStat_ObjectIdentity = ObjectIdentity
accXnsRipStat = _AccXnsRipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4)
)
_AccXnsRipReqIns_Type = Counter32
_AccXnsRipReqIns_Object = MibScalar
accXnsRipReqIns = _AccXnsRipReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 1),
    _AccXnsRipReqIns_Type()
)
accXnsRipReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipReqIns.setStatus("mandatory")
_AccXnsRipRespIns_Type = Counter32
_AccXnsRipRespIns_Object = MibScalar
accXnsRipRespIns = _AccXnsRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 2),
    _AccXnsRipRespIns_Type()
)
accXnsRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipRespIns.setStatus("mandatory")
_AccXnsRipReqOuts_Type = Counter32
_AccXnsRipReqOuts_Object = MibScalar
accXnsRipReqOuts = _AccXnsRipReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 3),
    _AccXnsRipReqOuts_Type()
)
accXnsRipReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipReqOuts.setStatus("mandatory")
_AccXnsRipRespOuts_Type = Counter32
_AccXnsRipRespOuts_Object = MibScalar
accXnsRipRespOuts = _AccXnsRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 4),
    _AccXnsRipRespOuts_Type()
)
accXnsRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipRespOuts.setStatus("mandatory")
_AccXnsRipInErrs_Type = Counter32
_AccXnsRipInErrs_Object = MibScalar
accXnsRipInErrs = _AccXnsRipInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 5),
    _AccXnsRipInErrs_Type()
)
accXnsRipInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipInErrs.setStatus("mandatory")
_AccXnsRipOutErrs_Type = Counter32
_AccXnsRipOutErrs_Object = MibScalar
accXnsRipOutErrs = _AccXnsRipOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 4, 6),
    _AccXnsRipOutErrs_Type()
)
accXnsRipOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsRipOutErrs.setStatus("mandatory")
_AccXnsNodeStat_ObjectIdentity = ObjectIdentity
accXnsNodeStat = _AccXnsNodeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5)
)
_AccXnsLocalIns_Type = Counter32
_AccXnsLocalIns_Object = MibScalar
accXnsLocalIns = _AccXnsLocalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 1),
    _AccXnsLocalIns_Type()
)
accXnsLocalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsLocalIns.setStatus("mandatory")
_AccXnsLocalOuts_Type = Counter32
_AccXnsLocalOuts_Object = MibScalar
accXnsLocalOuts = _AccXnsLocalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 2),
    _AccXnsLocalOuts_Type()
)
accXnsLocalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsLocalOuts.setStatus("mandatory")
_AccXnsNoSockets_Type = Counter32
_AccXnsNoSockets_Object = MibScalar
accXnsNoSockets = _AccXnsNoSockets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 3),
    _AccXnsNoSockets_Type()
)
accXnsNoSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNoSockets.setStatus("mandatory")
_AccXnsNoRoutes_Type = Counter32
_AccXnsNoRoutes_Object = MibScalar
accXnsNoRoutes = _AccXnsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 4),
    _AccXnsNoRoutes_Type()
)
accXnsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNoRoutes.setStatus("mandatory")
_AccXnsNodeInErrs_Type = Counter32
_AccXnsNodeInErrs_Object = MibScalar
accXnsNodeInErrs = _AccXnsNodeInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 5),
    _AccXnsNodeInErrs_Type()
)
accXnsNodeInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsNodeInErrs.setStatus("mandatory")
_AccXnsOutErrs_Type = Counter32
_AccXnsOutErrs_Object = MibScalar
accXnsOutErrs = _AccXnsOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 6),
    _AccXnsOutErrs_Type()
)
accXnsOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsOutErrs.setStatus("mandatory")
_AccXnsAllNetsIns_Type = Counter32
_AccXnsAllNetsIns_Object = MibScalar
accXnsAllNetsIns = _AccXnsAllNetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 7),
    _AccXnsAllNetsIns_Type()
)
accXnsAllNetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsIns.setStatus("mandatory")
_AccXnsAllNetsOuts_Type = Counter32
_AccXnsAllNetsOuts_Object = MibScalar
accXnsAllNetsOuts = _AccXnsAllNetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 8),
    _AccXnsAllNetsOuts_Type()
)
accXnsAllNetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsOuts.setStatus("mandatory")
_AccXnsAllNetsErrs_Type = Counter32
_AccXnsAllNetsErrs_Object = MibScalar
accXnsAllNetsErrs = _AccXnsAllNetsErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 5, 9),
    _AccXnsAllNetsErrs_Type()
)
accXnsAllNetsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsAllNetsErrs.setStatus("mandatory")
_AccXnsPortStatTable_Object = MibTable
accXnsPortStatTable = _AccXnsPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6)
)
if mibBuilder.loadTexts:
    accXnsPortStatTable.setStatus("mandatory")
_AccXnsPortStatEntry_Object = MibTableRow
accXnsPortStatEntry = _AccXnsPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1)
)
accXnsPortStatEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsPortNumber"),
)
if mibBuilder.loadTexts:
    accXnsPortStatEntry.setStatus("mandatory")
_AccXnsPortNumber_Type = Integer32
_AccXnsPortNumber_Object = MibTableColumn
accXnsPortNumber = _AccXnsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 1),
    _AccXnsPortNumber_Type()
)
accXnsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNumber.setStatus("mandatory")
_AccXnsPortTotalIns_Type = Counter32
_AccXnsPortTotalIns_Object = MibTableColumn
accXnsPortTotalIns = _AccXnsPortTotalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 2),
    _AccXnsPortTotalIns_Type()
)
accXnsPortTotalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTotalIns.setStatus("mandatory")
_AccXnsPorFwdReqIns_Type = Counter32
_AccXnsPorFwdReqIns_Object = MibTableColumn
accXnsPorFwdReqIns = _AccXnsPorFwdReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 3),
    _AccXnsPorFwdReqIns_Type()
)
accXnsPorFwdReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPorFwdReqIns.setStatus("mandatory")
_AccXnsPortNoFwdRts_Type = Counter32
_AccXnsPortNoFwdRts_Object = MibTableColumn
accXnsPortNoFwdRts = _AccXnsPortNoFwdRts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 4),
    _AccXnsPortNoFwdRts_Type()
)
accXnsPortNoFwdRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNoFwdRts.setStatus("mandatory")
_AccXnsPortTotalOuts_Type = Counter32
_AccXnsPortTotalOuts_Object = MibTableColumn
accXnsPortTotalOuts = _AccXnsPortTotalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 5),
    _AccXnsPortTotalOuts_Type()
)
accXnsPortTotalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTotalOuts.setStatus("mandatory")
_AccXnsPortHopCnts_Type = Counter32
_AccXnsPortHopCnts_Object = MibTableColumn
accXnsPortHopCnts = _AccXnsPortHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 6),
    _AccXnsPortHopCnts_Type()
)
accXnsPortHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortHopCnts.setStatus("mandatory")
_AccXnsPortNotForMes_Type = Counter32
_AccXnsPortNotForMes_Object = MibTableColumn
accXnsPortNotForMes = _AccXnsPortNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 7),
    _AccXnsPortNotForMes_Type()
)
accXnsPortNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortNotForMes.setStatus("mandatory")
_AccXnsPortFwdReqOuts_Type = Counter32
_AccXnsPortFwdReqOuts_Object = MibTableColumn
accXnsPortFwdReqOuts = _AccXnsPortFwdReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 8),
    _AccXnsPortFwdReqOuts_Type()
)
accXnsPortFwdReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortFwdReqOuts.setStatus("mandatory")
_AccXnsPortFwdErrs_Type = Counter32
_AccXnsPortFwdErrs_Object = MibTableColumn
accXnsPortFwdErrs = _AccXnsPortFwdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 9),
    _AccXnsPortFwdErrs_Type()
)
accXnsPortFwdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortFwdErrs.setStatus("mandatory")
_AccXnsPortInErrs_Type = Counter32
_AccXnsPortInErrs_Object = MibTableColumn
accXnsPortInErrs = _AccXnsPortInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 10),
    _AccXnsPortInErrs_Type()
)
accXnsPortInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortInErrs.setStatus("mandatory")
_AccXnsPortTooShorts_Type = Counter32
_AccXnsPortTooShorts_Object = MibTableColumn
accXnsPortTooShorts = _AccXnsPortTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 11),
    _AccXnsPortTooShorts_Type()
)
accXnsPortTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTooShorts.setStatus("mandatory")
_AccXnsPortCkSums_Type = Counter32
_AccXnsPortCkSums_Object = MibTableColumn
accXnsPortCkSums = _AccXnsPortCkSums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 12),
    _AccXnsPortCkSums_Type()
)
accXnsPortCkSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortCkSums.setStatus("mandatory")
_AccXnsPortTooLongs_Type = Counter32
_AccXnsPortTooLongs_Object = MibTableColumn
accXnsPortTooLongs = _AccXnsPortTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 13),
    _AccXnsPortTooLongs_Type()
)
accXnsPortTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortTooLongs.setStatus("mandatory")
_AccXnsPortOutErrs_Type = Counter32
_AccXnsPortOutErrs_Object = MibTableColumn
accXnsPortOutErrs = _AccXnsPortOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 14),
    _AccXnsPortOutErrs_Type()
)
accXnsPortOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortOutErrs.setStatus("mandatory")


class _AccXnsPortOpState_Type(Integer32):
    """Custom type accXnsPortOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccXnsPortOpState_Type.__name__ = "Integer32"
_AccXnsPortOpState_Object = MibTableColumn
accXnsPortOpState = _AccXnsPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 6, 1, 15),
    _AccXnsPortOpState_Type()
)
accXnsPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsPortOpState.setStatus("mandatory")
_AccXnsUbNbrTable_Object = MibTable
accXnsUbNbrTable = _AccXnsUbNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7)
)
if mibBuilder.loadTexts:
    accXnsUbNbrTable.setStatus("mandatory")
_AccXnsUbNbrEntry_Object = MibTableRow
accXnsUbNbrEntry = _AccXnsUbNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1)
)
accXnsUbNbrEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsUbnRmtNet"),
    (0, "ACC-MIB", "accXnsUbnLclNet"),
    (0, "ACC-MIB", "accXnsUbnRouter"),
)
if mibBuilder.loadTexts:
    accXnsUbNbrEntry.setStatus("mandatory")
_AccXnsUbnRmtNet_Type = OctetString
_AccXnsUbnRmtNet_Object = MibTableColumn
accXnsUbnRmtNet = _AccXnsUbnRmtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 1),
    _AccXnsUbnRmtNet_Type()
)
accXnsUbnRmtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnRmtNet.setStatus("mandatory")
_AccXnsUbnLclNet_Type = OctetString
_AccXnsUbnLclNet_Object = MibTableColumn
accXnsUbnLclNet = _AccXnsUbnLclNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 2),
    _AccXnsUbnLclNet_Type()
)
accXnsUbnLclNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnLclNet.setStatus("mandatory")
_AccXnsUbnRouter_Type = OctetString
_AccXnsUbnRouter_Object = MibTableColumn
accXnsUbnRouter = _AccXnsUbnRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 3),
    _AccXnsUbnRouter_Type()
)
accXnsUbnRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnRouter.setStatus("mandatory")
_AccXnsUbnHops_Type = Integer32
_AccXnsUbnHops_Object = MibTableColumn
accXnsUbnHops = _AccXnsUbnHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 4),
    _AccXnsUbnHops_Type()
)
accXnsUbnHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnHops.setStatus("mandatory")
_AccXnsUbnCost_Type = Integer32
_AccXnsUbnCost_Object = MibTableColumn
accXnsUbnCost = _AccXnsUbnCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 5),
    _AccXnsUbnCost_Type()
)
accXnsUbnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnCost.setStatus("mandatory")


class _AccXnsUbnState_Type(Integer32):
    """Custom type accXnsUbnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccXnsUbnState_Type.__name__ = "Integer32"
_AccXnsUbnState_Object = MibTableColumn
accXnsUbnState = _AccXnsUbnState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 6),
    _AccXnsUbnState_Type()
)
accXnsUbnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnState.setStatus("mandatory")
_AccXnsUbnTtl_Type = TimeTicks
_AccXnsUbnTtl_Object = MibTableColumn
accXnsUbnTtl = _AccXnsUbnTtl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 7, 1, 7),
    _AccXnsUbnTtl_Type()
)
accXnsUbnTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbnTtl.setStatus("mandatory")
_AccXnsUbRip_ObjectIdentity = ObjectIdentity
accXnsUbRip = _AccXnsUbRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8)
)
_AccXnsUbRipRespIns_Type = Counter32
_AccXnsUbRipRespIns_Object = MibScalar
accXnsUbRipRespIns = _AccXnsUbRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 1),
    _AccXnsUbRipRespIns_Type()
)
accXnsUbRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRespIns.setStatus("mandatory")
_AccXnsUbRipHelloIns_Type = Counter32
_AccXnsUbRipHelloIns_Object = MibScalar
accXnsUbRipHelloIns = _AccXnsUbRipHelloIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 2),
    _AccXnsUbRipHelloIns_Type()
)
accXnsUbRipHelloIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipHelloIns.setStatus("mandatory")
_AccXnsUbRipConHelIns_Type = Counter32
_AccXnsUbRipConHelIns_Object = MibScalar
accXnsUbRipConHelIns = _AccXnsUbRipConHelIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 3),
    _AccXnsUbRipConHelIns_Type()
)
accXnsUbRipConHelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipConHelIns.setStatus("mandatory")
_AccXnsUbRipUnConHelIns_Type = Counter32
_AccXnsUbRipUnConHelIns_Object = MibScalar
accXnsUbRipUnConHelIns = _AccXnsUbRipUnConHelIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 4),
    _AccXnsUbRipUnConHelIns_Type()
)
accXnsUbRipUnConHelIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipUnConHelIns.setStatus("mandatory")
_AccXnsUbRipRedirIns_Type = Counter32
_AccXnsUbRipRedirIns_Object = MibScalar
accXnsUbRipRedirIns = _AccXnsUbRipRedirIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 5),
    _AccXnsUbRipRedirIns_Type()
)
accXnsUbRipRedirIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRedirIns.setStatus("mandatory")
_AccXnsUbRipRespOuts_Type = Counter32
_AccXnsUbRipRespOuts_Object = MibScalar
accXnsUbRipRespOuts = _AccXnsUbRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 6),
    _AccXnsUbRipRespOuts_Type()
)
accXnsUbRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRespOuts.setStatus("mandatory")
_AccXnsUbRipHelloOuts_Type = Counter32
_AccXnsUbRipHelloOuts_Object = MibScalar
accXnsUbRipHelloOuts = _AccXnsUbRipHelloOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 7),
    _AccXnsUbRipHelloOuts_Type()
)
accXnsUbRipHelloOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipHelloOuts.setStatus("mandatory")
_AccXnsUbRipConHelOuts_Type = Counter32
_AccXnsUbRipConHelOuts_Object = MibScalar
accXnsUbRipConHelOuts = _AccXnsUbRipConHelOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 8),
    _AccXnsUbRipConHelOuts_Type()
)
accXnsUbRipConHelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipConHelOuts.setStatus("mandatory")
_AccXnsUbRipUnConHelOuts_Type = Counter32
_AccXnsUbRipUnConHelOuts_Object = MibScalar
accXnsUbRipUnConHelOuts = _AccXnsUbRipUnConHelOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 9),
    _AccXnsUbRipUnConHelOuts_Type()
)
accXnsUbRipUnConHelOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipUnConHelOuts.setStatus("mandatory")
_AccXnsUbRipRedirOuts_Type = Counter32
_AccXnsUbRipRedirOuts_Object = MibScalar
accXnsUbRipRedirOuts = _AccXnsUbRipRedirOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 10),
    _AccXnsUbRipRedirOuts_Type()
)
accXnsUbRipRedirOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbRipRedirOuts.setStatus("mandatory")
_AccXnsUbNoRoutes_Type = Counter32
_AccXnsUbNoRoutes_Object = MibScalar
accXnsUbNoRoutes = _AccXnsUbNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 11),
    _AccXnsUbNoRoutes_Type()
)
accXnsUbNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbNoRoutes.setStatus("mandatory")
_AccXnsUbInErrs_Type = Counter32
_AccXnsUbInErrs_Object = MibScalar
accXnsUbInErrs = _AccXnsUbInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 12),
    _AccXnsUbInErrs_Type()
)
accXnsUbInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbInErrs.setStatus("mandatory")
_AccXnsUbOutErrs_Type = Counter32
_AccXnsUbOutErrs_Object = MibScalar
accXnsUbOutErrs = _AccXnsUbOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 8, 13),
    _AccXnsUbOutErrs_Type()
)
accXnsUbOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accXnsUbOutErrs.setStatus("mandatory")
_AccXnsRouteFilters_ObjectIdentity = ObjectIdentity
accXnsRouteFilters = _AccXnsRouteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9)
)


class _AccXnsRteFltrDefaultAction_Type(Integer32):
    """Custom type accXnsRteFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccXnsRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsRteFltrDefaultAction_Object = MibScalar
accXnsRteFltrDefaultAction = _AccXnsRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 1),
    _AccXnsRteFltrDefaultAction_Type()
)
accXnsRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrDefaultAction.setStatus("mandatory")
_AccXnsRteNbrTable_Object = MibTable
accXnsRteNbrTable = _AccXnsRteNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2)
)
if mibBuilder.loadTexts:
    accXnsRteNbrTable.setStatus("mandatory")
_AccXnsRteNbrEntry_Object = MibTableRow
accXnsRteNbrEntry = _AccXnsRteNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1)
)
accXnsRteNbrEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsRteNbrId"),
)
if mibBuilder.loadTexts:
    accXnsRteNbrEntry.setStatus("mandatory")
_AccXnsRteNbrId_Type = OctetString
_AccXnsRteNbrId_Object = MibTableColumn
accXnsRteNbrId = _AccXnsRteNbrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 1),
    _AccXnsRteNbrId_Type()
)
accXnsRteNbrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrId.setStatus("mandatory")


class _AccXnsRteNbrAction_Type(Integer32):
    """Custom type accXnsRteNbrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccXnsRteNbrAction_Type.__name__ = "Integer32"
_AccXnsRteNbrAction_Object = MibTableColumn
accXnsRteNbrAction = _AccXnsRteNbrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 2),
    _AccXnsRteNbrAction_Type()
)
accXnsRteNbrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrAction.setStatus("mandatory")


class _AccXnsRteNbrStatus_Type(Integer32):
    """Custom type accXnsRteNbrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccXnsRteNbrStatus_Type.__name__ = "Integer32"
_AccXnsRteNbrStatus_Object = MibTableColumn
accXnsRteNbrStatus = _AccXnsRteNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 2, 1, 3),
    _AccXnsRteNbrStatus_Type()
)
accXnsRteNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteNbrStatus.setStatus("mandatory")
_AccXnsRteFltrTable_Object = MibTable
accXnsRteFltrTable = _AccXnsRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3)
)
if mibBuilder.loadTexts:
    accXnsRteFltrTable.setStatus("mandatory")
_AccXnsRteFltrEntry_Object = MibTableRow
accXnsRteFltrEntry = _AccXnsRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1)
)
accXnsRteFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsRteFltrNeighbor"),
    (0, "ACC-MIB", "accXnsRteFltrNetwork"),
)
if mibBuilder.loadTexts:
    accXnsRteFltrEntry.setStatus("mandatory")
_AccXnsRteFltrNeighbor_Type = OctetString
_AccXnsRteFltrNeighbor_Object = MibTableColumn
accXnsRteFltrNeighbor = _AccXnsRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 1),
    _AccXnsRteFltrNeighbor_Type()
)
accXnsRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrNeighbor.setStatus("mandatory")
_AccXnsRteFltrNetwork_Type = OctetString
_AccXnsRteFltrNetwork_Object = MibTableColumn
accXnsRteFltrNetwork = _AccXnsRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 2),
    _AccXnsRteFltrNetwork_Type()
)
accXnsRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrNetwork.setStatus("mandatory")


class _AccXnsRteFltrAction_Type(Integer32):
    """Custom type accXnsRteFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccXnsRteFltrAction_Type.__name__ = "Integer32"
_AccXnsRteFltrAction_Object = MibTableColumn
accXnsRteFltrAction = _AccXnsRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 3),
    _AccXnsRteFltrAction_Type()
)
accXnsRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrAction.setStatus("mandatory")


class _AccXnsRteFltrStatus_Type(Integer32):
    """Custom type accXnsRteFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccXnsRteFltrStatus_Type.__name__ = "Integer32"
_AccXnsRteFltrStatus_Object = MibTableColumn
accXnsRteFltrStatus = _AccXnsRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 9, 3, 1, 4),
    _AccXnsRteFltrStatus_Type()
)
accXnsRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsRteFltrStatus.setStatus("mandatory")
_AccXnsNetworkFilters_ObjectIdentity = ObjectIdentity
accXnsNetworkFilters = _AccXnsNetworkFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10)
)


class _AccXnsNetFltrDefaultAction_Type(Integer32):
    """Custom type accXnsNetFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccXnsNetFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsNetFltrDefaultAction_Object = MibScalar
accXnsNetFltrDefaultAction = _AccXnsNetFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 1),
    _AccXnsNetFltrDefaultAction_Type()
)
accXnsNetFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDefaultAction.setStatus("mandatory")
_OldXnsNetFltrTable_Object = MibTable
oldXnsNetFltrTable = _OldXnsNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2)
)
if mibBuilder.loadTexts:
    oldXnsNetFltrTable.setStatus("deprecated")
_OldXnsNetFltrEntry_Object = MibTableRow
oldXnsNetFltrEntry = _OldXnsNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1)
)
oldXnsNetFltrEntry.setIndexNames(
    (0, "ACC-MIB", "oldXnsNetFltrDestination"),
    (0, "ACC-MIB", "oldXnsNetFltrSource"),
)
if mibBuilder.loadTexts:
    oldXnsNetFltrEntry.setStatus("deprecated")
_OldXnsNetFltrDestination_Type = OctetString
_OldXnsNetFltrDestination_Object = MibTableColumn
oldXnsNetFltrDestination = _OldXnsNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 1),
    _OldXnsNetFltrDestination_Type()
)
oldXnsNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrDestination.setStatus("deprecated")
_OldXnsNetFltrSource_Type = OctetString
_OldXnsNetFltrSource_Object = MibTableColumn
oldXnsNetFltrSource = _OldXnsNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 2),
    _OldXnsNetFltrSource_Type()
)
oldXnsNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrSource.setStatus("deprecated")


class _OldXnsNetFltrAction_Type(Integer32):
    """Custom type oldXnsNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OldXnsNetFltrAction_Type.__name__ = "Integer32"
_OldXnsNetFltrAction_Object = MibTableColumn
oldXnsNetFltrAction = _OldXnsNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 3),
    _OldXnsNetFltrAction_Type()
)
oldXnsNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrAction.setStatus("deprecated")


class _OldXnsNetFltrStatus_Type(Integer32):
    """Custom type oldXnsNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_OldXnsNetFltrStatus_Type.__name__ = "Integer32"
_OldXnsNetFltrStatus_Object = MibTableColumn
oldXnsNetFltrStatus = _OldXnsNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 2, 1, 4),
    _OldXnsNetFltrStatus_Type()
)
oldXnsNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldXnsNetFltrStatus.setStatus("deprecated")
_AccXnsNetFltrTable_Object = MibTable
accXnsNetFltrTable = _AccXnsNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3)
)
if mibBuilder.loadTexts:
    accXnsNetFltrTable.setStatus("mandatory")
_AccXnsNetFltrEntry_Object = MibTableRow
accXnsNetFltrEntry = _AccXnsNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1)
)
accXnsNetFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsNetFltrDestination"),
    (0, "ACC-MIB", "accXnsNetFltrSource"),
    (0, "ACC-MIB", "accXnsNetFltrDestSkt"),
    (0, "ACC-MIB", "accXnsNetFltrSrcSkt"),
    (0, "ACC-MIB", "accXnsNetFltrPktType"),
)
if mibBuilder.loadTexts:
    accXnsNetFltrEntry.setStatus("mandatory")
_AccXnsNetFltrDestination_Type = OctetString
_AccXnsNetFltrDestination_Object = MibTableColumn
accXnsNetFltrDestination = _AccXnsNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 1),
    _AccXnsNetFltrDestination_Type()
)
accXnsNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDestination.setStatus("mandatory")
_AccXnsNetFltrSource_Type = OctetString
_AccXnsNetFltrSource_Object = MibTableColumn
accXnsNetFltrSource = _AccXnsNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 2),
    _AccXnsNetFltrSource_Type()
)
accXnsNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrSource.setStatus("mandatory")


class _AccXnsNetFltrAction_Type(Integer32):
    """Custom type accXnsNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccXnsNetFltrAction_Type.__name__ = "Integer32"
_AccXnsNetFltrAction_Object = MibTableColumn
accXnsNetFltrAction = _AccXnsNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 3),
    _AccXnsNetFltrAction_Type()
)
accXnsNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrAction.setStatus("mandatory")


class _AccXnsNetFltrStatus_Type(Integer32):
    """Custom type accXnsNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccXnsNetFltrStatus_Type.__name__ = "Integer32"
_AccXnsNetFltrStatus_Object = MibTableColumn
accXnsNetFltrStatus = _AccXnsNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 4),
    _AccXnsNetFltrStatus_Type()
)
accXnsNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrStatus.setStatus("mandatory")
_AccXnsNetFltrDestSkt_Type = OctetString
_AccXnsNetFltrDestSkt_Object = MibTableColumn
accXnsNetFltrDestSkt = _AccXnsNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 5),
    _AccXnsNetFltrDestSkt_Type()
)
accXnsNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrDestSkt.setStatus("mandatory")
_AccXnsNetFltrSrcSkt_Type = OctetString
_AccXnsNetFltrSrcSkt_Object = MibTableColumn
accXnsNetFltrSrcSkt = _AccXnsNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 6),
    _AccXnsNetFltrSrcSkt_Type()
)
accXnsNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrSrcSkt.setStatus("mandatory")
_AccXnsNetFltrPktType_Type = Integer32
_AccXnsNetFltrPktType_Object = MibTableColumn
accXnsNetFltrPktType = _AccXnsNetFltrPktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 10, 3, 1, 7),
    _AccXnsNetFltrPktType_Type()
)
accXnsNetFltrPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsNetFltrPktType.setStatus("mandatory")
_AccXnsHostFilters_ObjectIdentity = ObjectIdentity
accXnsHostFilters = _AccXnsHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11)
)


class _AccXnsHostFltrDefaultAction_Type(Integer32):
    """Custom type accXnsHostFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccXnsHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccXnsHostFltrDefaultAction_Object = MibScalar
accXnsHostFltrDefaultAction = _AccXnsHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 1),
    _AccXnsHostFltrDefaultAction_Type()
)
accXnsHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrDefaultAction.setStatus("mandatory")
_AccXnsHostFltrTable_Object = MibTable
accXnsHostFltrTable = _AccXnsHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2)
)
if mibBuilder.loadTexts:
    accXnsHostFltrTable.setStatus("mandatory")
_AccXnsHostFltrEntry_Object = MibTableRow
accXnsHostFltrEntry = _AccXnsHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1)
)
accXnsHostFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accXnsHostFltrId"),
    (0, "ACC-MIB", "accXnsHostFltrSocket"),
    (0, "ACC-MIB", "accXnsHostFltrPepClient"),
)
if mibBuilder.loadTexts:
    accXnsHostFltrEntry.setStatus("mandatory")
_AccXnsHostFltrId_Type = OctetString
_AccXnsHostFltrId_Object = MibTableColumn
accXnsHostFltrId = _AccXnsHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 1),
    _AccXnsHostFltrId_Type()
)
accXnsHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrId.setStatus("mandatory")
_AccXnsHostFltrSocket_Type = OctetString
_AccXnsHostFltrSocket_Object = MibTableColumn
accXnsHostFltrSocket = _AccXnsHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 2),
    _AccXnsHostFltrSocket_Type()
)
accXnsHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrSocket.setStatus("mandatory")
_AccXnsHostFltrPepClient_Type = OctetString
_AccXnsHostFltrPepClient_Object = MibTableColumn
accXnsHostFltrPepClient = _AccXnsHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 3),
    _AccXnsHostFltrPepClient_Type()
)
accXnsHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrPepClient.setStatus("mandatory")


class _AccXnsHostFltrAction_Type(Integer32):
    """Custom type accXnsHostFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccXnsHostFltrAction_Type.__name__ = "Integer32"
_AccXnsHostFltrAction_Object = MibTableColumn
accXnsHostFltrAction = _AccXnsHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 4),
    _AccXnsHostFltrAction_Type()
)
accXnsHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrAction.setStatus("mandatory")


class _AccXnsHostFltrStatus_Type(Integer32):
    """Custom type accXnsHostFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccXnsHostFltrStatus_Type.__name__ = "Integer32"
_AccXnsHostFltrStatus_Object = MibTableColumn
accXnsHostFltrStatus = _AccXnsHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 21, 11, 2, 1, 5),
    _AccXnsHostFltrStatus_Type()
)
accXnsHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXnsHostFltrStatus.setStatus("mandatory")
_AccIpx_ObjectIdentity = ObjectIdentity
accIpx = _AccIpx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22)
)
_AccIpxParms_ObjectIdentity = ObjectIdentity
accIpxParms = _AccIpxParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1)
)


class _AccIpxAdStat_Type(Integer32):
    """Custom type accIpxAdStat based on Integer32"""
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


_AccIpxAdStat_Type.__name__ = "Integer32"
_AccIpxAdStat_Object = MibScalar
accIpxAdStat = _AccIpxAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 1),
    _AccIpxAdStat_Type()
)
accIpxAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxAdStat.setStatus("mandatory")


class _AccIpxCkSum_Type(Integer32):
    """Custom type accIpxCkSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("header", 3),
          ("off", 1),
          ("packet", 2))
    )


_AccIpxCkSum_Type.__name__ = "Integer32"
_AccIpxCkSum_Object = MibScalar
accIpxCkSum = _AccIpxCkSum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 2),
    _AccIpxCkSum_Type()
)
accIpxCkSum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxCkSum.setStatus("mandatory")


class _AccIpxSpltHorz_Type(Integer32):
    """Custom type accIpxSpltHorz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("poison", 3),
          ("simple", 2))
    )


_AccIpxSpltHorz_Type.__name__ = "Integer32"
_AccIpxSpltHorz_Object = MibScalar
accIpxSpltHorz = _AccIpxSpltHorz_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 3),
    _AccIpxSpltHorz_Type()
)
accIpxSpltHorz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSpltHorz.setStatus("mandatory")


class _AccIpxAllNets_Type(Integer32):
    """Custom type accIpxAllNets based on Integer32"""
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


_AccIpxAllNets_Type.__name__ = "Integer32"
_AccIpxAllNets_Object = MibScalar
accIpxAllNets = _AccIpxAllNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 4),
    _AccIpxAllNets_Type()
)
accIpxAllNets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxAllNets.setStatus("mandatory")


class _AccIpxMode_Type(Integer32):
    """Custom type accIpxMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipx", 1),
          ("repeat", 3),
          ("ub", 2))
    )


_AccIpxMode_Type.__name__ = "Integer32"
_AccIpxMode_Object = MibScalar
accIpxMode = _AccIpxMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 5),
    _AccIpxMode_Type()
)
accIpxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxMode.setStatus("mandatory")


class _AccIpxWdFilter_Type(Integer32):
    """Custom type accIpxWdFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AccIpxWdFilter_Type.__name__ = "Integer32"
_AccIpxWdFilter_Object = MibScalar
accIpxWdFilter = _AccIpxWdFilter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 1, 6),
    _AccIpxWdFilter_Type()
)
accIpxWdFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdFilter.setStatus("mandatory")
_AccIpxNetTable_Object = MibTable
accIpxNetTable = _AccIpxNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2)
)
if mibBuilder.loadTexts:
    accIpxNetTable.setStatus("mandatory")
_AccIpxNetEntry_Object = MibTableRow
accIpxNetEntry = _AccIpxNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1)
)
accIpxNetEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxNetPort"),
)
if mibBuilder.loadTexts:
    accIpxNetEntry.setStatus("mandatory")
_AccIpxNetPort_Type = Integer32
_AccIpxNetPort_Object = MibTableColumn
accIpxNetPort = _AccIpxNetPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 1),
    _AccIpxNetPort_Type()
)
accIpxNetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetPort.setStatus("mandatory")
_AccIpxNetNumber_Type = OctetString
_AccIpxNetNumber_Object = MibTableColumn
accIpxNetNumber = _AccIpxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 2),
    _AccIpxNetNumber_Type()
)
accIpxNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetNumber.setStatus("mandatory")


class _AccIpxNetType_Type(Integer32):
    """Custom type accIpxNetType based on Integer32"""
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
        *(("dial", 8),
          ("enet", 1),
          ("fddi", 7),
          ("frame-relay", 5),
          ("lapb", 3),
          ("multilink", 9),
          ("ppp", 6),
          ("token-ring", 2),
          ("x25", 4))
    )


_AccIpxNetType_Type.__name__ = "Integer32"
_AccIpxNetType_Object = MibTableColumn
accIpxNetType = _AccIpxNetType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 3),
    _AccIpxNetType_Type()
)
accIpxNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetType.setStatus("mandatory")


class _AccIpxNetEncap_Type(Integer32):
    """Custom type accIpxNetEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccIpxNetEncap_Type.__name__ = "Integer32"
_AccIpxNetEncap_Object = MibTableColumn
accIpxNetEncap = _AccIpxNetEncap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 4),
    _AccIpxNetEncap_Type()
)
accIpxNetEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetEncap.setStatus("mandatory")


class _AccIpxNetSlot_Type(Integer32):
    """Custom type accIpxNetSlot based on Integer32"""
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
        *(("b1", 4),
          ("j1", 1),
          ("j2", 2),
          ("j3", 3))
    )


_AccIpxNetSlot_Type.__name__ = "Integer32"
_AccIpxNetSlot_Object = MibTableColumn
accIpxNetSlot = _AccIpxNetSlot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 5),
    _AccIpxNetSlot_Type()
)
accIpxNetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetSlot.setStatus("mandatory")


class _AccIpxNetAdStat_Type(Integer32):
    """Custom type accIpxNetAdStat based on Integer32"""
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


_AccIpxNetAdStat_Type.__name__ = "Integer32"
_AccIpxNetAdStat_Object = MibTableColumn
accIpxNetAdStat = _AccIpxNetAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 6),
    _AccIpxNetAdStat_Type()
)
accIpxNetAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetAdStat.setStatus("mandatory")


class _AccIpxNetMtu_Type(Integer32):
    """Custom type accIpxNetMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(576, 65535),
    )


_AccIpxNetMtu_Type.__name__ = "Integer32"
_AccIpxNetMtu_Object = MibTableColumn
accIpxNetMtu = _AccIpxNetMtu_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 7),
    _AccIpxNetMtu_Type()
)
accIpxNetMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetMtu.setStatus("mandatory")


class _AccIpxNetUpdate_Type(TimeTicks):
    """Custom type accIpxNetUpdate based on TimeTicks"""
    defaultValue = 1500


_AccIpxNetUpdate_Object = MibTableColumn
accIpxNetUpdate = _AccIpxNetUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 8),
    _AccIpxNetUpdate_Type()
)
accIpxNetUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetUpdate.setStatus("mandatory")


class _AccIpxNetHops_Type(Integer32):
    """Custom type accIpxNetHops based on Integer32"""
    defaultValue = 1


_AccIpxNetHops_Object = MibTableColumn
accIpxNetHops = _AccIpxNetHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 9),
    _AccIpxNetHops_Type()
)
accIpxNetHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetHops.setStatus("mandatory")


class _AccIpxNetCost_Type(Integer32):
    """Custom type accIpxNetCost based on Integer32"""
    defaultValue = 1


_AccIpxNetCost_Object = MibTableColumn
accIpxNetCost = _AccIpxNetCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 10),
    _AccIpxNetCost_Type()
)
accIpxNetCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetCost.setStatus("mandatory")
_AccIpxNetX25InOutAddr_Type = DisplayString
_AccIpxNetX25InOutAddr_Object = MibTableColumn
accIpxNetX25InOutAddr = _AccIpxNetX25InOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 11),
    _AccIpxNetX25InOutAddr_Type()
)
accIpxNetX25InOutAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25InOutAddr.setStatus("mandatory")
_AccIpxNetX25InAddr_Type = DisplayString
_AccIpxNetX25InAddr_Object = MibTableColumn
accIpxNetX25InAddr = _AccIpxNetX25InAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 12),
    _AccIpxNetX25InAddr_Type()
)
accIpxNetX25InAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25InAddr.setStatus("mandatory")


class _AccIpxNetX25Idle_Type(TimeTicks):
    """Custom type accIpxNetX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccIpxNetX25Idle_Object = MibTableColumn
accIpxNetX25Idle = _AccIpxNetX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 13),
    _AccIpxNetX25Idle_Type()
)
accIpxNetX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25Idle.setStatus("mandatory")


class _AccIpxNetX25PktVal_Type(Integer32):
    """Custom type accIpxNetX25PktVal based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_AccIpxNetX25PktVal_Type.__name__ = "Integer32"
_AccIpxNetX25PktVal_Object = MibTableColumn
accIpxNetX25PktVal = _AccIpxNetX25PktVal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 14),
    _AccIpxNetX25PktVal_Type()
)
accIpxNetX25PktVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25PktVal.setStatus("mandatory")


class _AccIpxNetX25PktWin_Type(Integer32):
    """Custom type accIpxNetX25PktWin based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccIpxNetX25PktWin_Type.__name__ = "Integer32"
_AccIpxNetX25PktWin_Object = MibTableColumn
accIpxNetX25PktWin = _AccIpxNetX25PktWin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 15),
    _AccIpxNetX25PktWin_Type()
)
accIpxNetX25PktWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25PktWin.setStatus("mandatory")


class _AccIpxNetEntryStat_Type(Integer32):
    """Custom type accIpxNetEntryStat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccIpxNetEntryStat_Type.__name__ = "Integer32"
_AccIpxNetEntryStat_Object = MibTableColumn
accIpxNetEntryStat = _AccIpxNetEntryStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 16),
    _AccIpxNetEntryStat_Type()
)
accIpxNetEntryStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetEntryStat.setStatus("mandatory")
_AccIpxNetFncAddr_Type = OctetString
_AccIpxNetFncAddr_Object = MibTableColumn
accIpxNetFncAddr = _AccIpxNetFncAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 17),
    _AccIpxNetFncAddr_Type()
)
accIpxNetFncAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFncAddr.setStatus("mandatory")


class _AccIpxNetSrMode_Type(Integer32):
    """Custom type accIpxNetSrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AccIpxNetSrMode_Type.__name__ = "Integer32"
_AccIpxNetSrMode_Object = MibTableColumn
accIpxNetSrMode = _AccIpxNetSrMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 18),
    _AccIpxNetSrMode_Type()
)
accIpxNetSrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetSrMode.setStatus("mandatory")


class _AccIpxNetX25FacIndex_Type(Integer32):
    """Custom type accIpxNetX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIpxNetX25FacIndex_Type.__name__ = "Integer32"
_AccIpxNetX25FacIndex_Object = MibTableColumn
accIpxNetX25FacIndex = _AccIpxNetX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 19),
    _AccIpxNetX25FacIndex_Type()
)
accIpxNetX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetX25FacIndex.setStatus("mandatory")
_AccIpxNetDlci_Type = Integer32
_AccIpxNetDlci_Object = MibTableColumn
accIpxNetDlci = _AccIpxNetDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 20),
    _AccIpxNetDlci_Type()
)
accIpxNetDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetDlci.setStatus("mandatory")


class _AccIpxNetWdState_Type(Integer32):
    """Custom type accIpxNetWdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("discard", 2),
          ("proxy", 3))
    )


_AccIpxNetWdState_Type.__name__ = "Integer32"
_AccIpxNetWdState_Object = MibTableColumn
accIpxNetWdState = _AccIpxNetWdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 2, 1, 21),
    _AccIpxNetWdState_Type()
)
accIpxNetWdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetWdState.setStatus("mandatory")
_AccIpxRtTable_Object = MibTable
accIpxRtTable = _AccIpxRtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3)
)
if mibBuilder.loadTexts:
    accIpxRtTable.setStatus("mandatory")
_AccIpxRtEntry_Object = MibTableRow
accIpxRtEntry = _AccIpxRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1)
)
accIpxRtEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxRtDest"),
)
if mibBuilder.loadTexts:
    accIpxRtEntry.setStatus("mandatory")
_AccIpxRtDest_Type = OctetString
_AccIpxRtDest_Object = MibTableColumn
accIpxRtDest = _AccIpxRtDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 1),
    _AccIpxRtDest_Type()
)
accIpxRtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtDest.setStatus("mandatory")
_AccIpxRtNxtNet_Type = OctetString
_AccIpxRtNxtNet_Object = MibTableColumn
accIpxRtNxtNet = _AccIpxRtNxtNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 2),
    _AccIpxRtNxtNet_Type()
)
accIpxRtNxtNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtNxtNet.setStatus("mandatory")
_AccIpxRtRouter_Type = OctetString
_AccIpxRtRouter_Object = MibTableColumn
accIpxRtRouter = _AccIpxRtRouter_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 3),
    _AccIpxRtRouter_Type()
)
accIpxRtRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtRouter.setStatus("mandatory")
_AccIpxRtHops_Type = Integer32
_AccIpxRtHops_Object = MibTableColumn
accIpxRtHops = _AccIpxRtHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 4),
    _AccIpxRtHops_Type()
)
accIpxRtHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtHops.setStatus("mandatory")
_AccIpxRtCost_Type = Integer32
_AccIpxRtCost_Object = MibTableColumn
accIpxRtCost = _AccIpxRtCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 5),
    _AccIpxRtCost_Type()
)
accIpxRtCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtCost.setStatus("mandatory")


class _AccIpxRtType_Type(Integer32):
    """Custom type accIpxRtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("public", 1),
          ("static", 3))
    )


_AccIpxRtType_Type.__name__ = "Integer32"
_AccIpxRtType_Object = MibTableColumn
accIpxRtType = _AccIpxRtType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 6),
    _AccIpxRtType_Type()
)
accIpxRtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtType.setStatus("mandatory")


class _AccIpxRtOwner_Type(Integer32):
    """Custom type accIpxRtOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lli", 1),
          ("nms", 2),
          ("rip", 3))
    )


_AccIpxRtOwner_Type.__name__ = "Integer32"
_AccIpxRtOwner_Object = MibTableColumn
accIpxRtOwner = _AccIpxRtOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 7),
    _AccIpxRtOwner_Type()
)
accIpxRtOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtOwner.setStatus("mandatory")
_AccIpxRtAge_Type = TimeTicks
_AccIpxRtAge_Object = MibTableColumn
accIpxRtAge = _AccIpxRtAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 8),
    _AccIpxRtAge_Type()
)
accIpxRtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtAge.setStatus("mandatory")
_AccIpxRtPort_Type = Integer32
_AccIpxRtPort_Object = MibTableColumn
accIpxRtPort = _AccIpxRtPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 3, 1, 9),
    _AccIpxRtPort_Type()
)
accIpxRtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRtPort.setStatus("mandatory")
_AccIpxRipStat_ObjectIdentity = ObjectIdentity
accIpxRipStat = _AccIpxRipStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4)
)
_AccIpxRipReqIns_Type = Counter32
_AccIpxRipReqIns_Object = MibScalar
accIpxRipReqIns = _AccIpxRipReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 1),
    _AccIpxRipReqIns_Type()
)
accIpxRipReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipReqIns.setStatus("mandatory")
_AccIpxRipRespIns_Type = Counter32
_AccIpxRipRespIns_Object = MibScalar
accIpxRipRespIns = _AccIpxRipRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 2),
    _AccIpxRipRespIns_Type()
)
accIpxRipRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipRespIns.setStatus("mandatory")
_AccIpxRipReqOuts_Type = Counter32
_AccIpxRipReqOuts_Object = MibScalar
accIpxRipReqOuts = _AccIpxRipReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 3),
    _AccIpxRipReqOuts_Type()
)
accIpxRipReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipReqOuts.setStatus("mandatory")
_AccIpxRipRespOuts_Type = Counter32
_AccIpxRipRespOuts_Object = MibScalar
accIpxRipRespOuts = _AccIpxRipRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 4),
    _AccIpxRipRespOuts_Type()
)
accIpxRipRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipRespOuts.setStatus("mandatory")
_AccIpxRipErrIns_Type = Counter32
_AccIpxRipErrIns_Object = MibScalar
accIpxRipErrIns = _AccIpxRipErrIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 5),
    _AccIpxRipErrIns_Type()
)
accIpxRipErrIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipErrIns.setStatus("mandatory")
_AccIpxRipErrOuts_Type = Counter32
_AccIpxRipErrOuts_Object = MibScalar
accIpxRipErrOuts = _AccIpxRipErrOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 4, 6),
    _AccIpxRipErrOuts_Type()
)
accIpxRipErrOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxRipErrOuts.setStatus("mandatory")
_AccIpxNodeStat_ObjectIdentity = ObjectIdentity
accIpxNodeStat = _AccIpxNodeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5)
)
_AccIpxLocalIns_Type = Counter32
_AccIpxLocalIns_Object = MibScalar
accIpxLocalIns = _AccIpxLocalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 1),
    _AccIpxLocalIns_Type()
)
accIpxLocalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxLocalIns.setStatus("mandatory")
_AccIpxLocalOuts_Type = Counter32
_AccIpxLocalOuts_Object = MibScalar
accIpxLocalOuts = _AccIpxLocalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 2),
    _AccIpxLocalOuts_Type()
)
accIpxLocalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxLocalOuts.setStatus("mandatory")
_AccIpxNoSockets_Type = Counter32
_AccIpxNoSockets_Object = MibScalar
accIpxNoSockets = _AccIpxNoSockets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 3),
    _AccIpxNoSockets_Type()
)
accIpxNoSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNoSockets.setStatus("mandatory")
_AccIpxNoRoutes_Type = Counter32
_AccIpxNoRoutes_Object = MibScalar
accIpxNoRoutes = _AccIpxNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 4),
    _AccIpxNoRoutes_Type()
)
accIpxNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNoRoutes.setStatus("mandatory")
_AccIpxNodeInErrs_Type = Counter32
_AccIpxNodeInErrs_Object = MibScalar
accIpxNodeInErrs = _AccIpxNodeInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 5),
    _AccIpxNodeInErrs_Type()
)
accIpxNodeInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxNodeInErrs.setStatus("mandatory")
_AccIpxOutErrs_Type = Counter32
_AccIpxOutErrs_Object = MibScalar
accIpxOutErrs = _AccIpxOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 6),
    _AccIpxOutErrs_Type()
)
accIpxOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxOutErrs.setStatus("mandatory")
_AccIpxAllNetsIns_Type = Counter32
_AccIpxAllNetsIns_Object = MibScalar
accIpxAllNetsIns = _AccIpxAllNetsIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 7),
    _AccIpxAllNetsIns_Type()
)
accIpxAllNetsIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsIns.setStatus("mandatory")
_AccIpxAllNetsOuts_Type = Counter32
_AccIpxAllNetsOuts_Object = MibScalar
accIpxAllNetsOuts = _AccIpxAllNetsOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 8),
    _AccIpxAllNetsOuts_Type()
)
accIpxAllNetsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsOuts.setStatus("mandatory")
_AccIpxAllNetsErrs_Type = Counter32
_AccIpxAllNetsErrs_Object = MibScalar
accIpxAllNetsErrs = _AccIpxAllNetsErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 5, 9),
    _AccIpxAllNetsErrs_Type()
)
accIpxAllNetsErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxAllNetsErrs.setStatus("mandatory")
_AccIpxPortStatTable_Object = MibTable
accIpxPortStatTable = _AccIpxPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6)
)
if mibBuilder.loadTexts:
    accIpxPortStatTable.setStatus("mandatory")
_AccIpxPortStatEntry_Object = MibTableRow
accIpxPortStatEntry = _AccIpxPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1)
)
accIpxPortStatEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxPortNumber"),
)
if mibBuilder.loadTexts:
    accIpxPortStatEntry.setStatus("mandatory")
_AccIpxPortNumber_Type = Integer32
_AccIpxPortNumber_Object = MibTableColumn
accIpxPortNumber = _AccIpxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 1),
    _AccIpxPortNumber_Type()
)
accIpxPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNumber.setStatus("mandatory")
_AccIpxPortTotalIns_Type = Counter32
_AccIpxPortTotalIns_Object = MibTableColumn
accIpxPortTotalIns = _AccIpxPortTotalIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 2),
    _AccIpxPortTotalIns_Type()
)
accIpxPortTotalIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTotalIns.setStatus("mandatory")
_AccIpxPorFwdReqIns_Type = Counter32
_AccIpxPorFwdReqIns_Object = MibTableColumn
accIpxPorFwdReqIns = _AccIpxPorFwdReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 3),
    _AccIpxPorFwdReqIns_Type()
)
accIpxPorFwdReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPorFwdReqIns.setStatus("mandatory")
_AccIpxPortNoFwdRts_Type = Counter32
_AccIpxPortNoFwdRts_Object = MibTableColumn
accIpxPortNoFwdRts = _AccIpxPortNoFwdRts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 4),
    _AccIpxPortNoFwdRts_Type()
)
accIpxPortNoFwdRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNoFwdRts.setStatus("mandatory")
_AccIpxPortTotalOuts_Type = Counter32
_AccIpxPortTotalOuts_Object = MibTableColumn
accIpxPortTotalOuts = _AccIpxPortTotalOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 5),
    _AccIpxPortTotalOuts_Type()
)
accIpxPortTotalOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTotalOuts.setStatus("mandatory")
_AccIpxPortHopCnts_Type = Counter32
_AccIpxPortHopCnts_Object = MibTableColumn
accIpxPortHopCnts = _AccIpxPortHopCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 6),
    _AccIpxPortHopCnts_Type()
)
accIpxPortHopCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortHopCnts.setStatus("mandatory")
_AccIpxPortNotForMes_Type = Counter32
_AccIpxPortNotForMes_Object = MibTableColumn
accIpxPortNotForMes = _AccIpxPortNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 7),
    _AccIpxPortNotForMes_Type()
)
accIpxPortNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortNotForMes.setStatus("mandatory")
_AccIpxPortFwdReqOuts_Type = Counter32
_AccIpxPortFwdReqOuts_Object = MibTableColumn
accIpxPortFwdReqOuts = _AccIpxPortFwdReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 8),
    _AccIpxPortFwdReqOuts_Type()
)
accIpxPortFwdReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortFwdReqOuts.setStatus("mandatory")
_AccIpxPortFwdErrs_Type = Counter32
_AccIpxPortFwdErrs_Object = MibTableColumn
accIpxPortFwdErrs = _AccIpxPortFwdErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 9),
    _AccIpxPortFwdErrs_Type()
)
accIpxPortFwdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortFwdErrs.setStatus("mandatory")
_AccIpxPortInErrs_Type = Counter32
_AccIpxPortInErrs_Object = MibTableColumn
accIpxPortInErrs = _AccIpxPortInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 10),
    _AccIpxPortInErrs_Type()
)
accIpxPortInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortInErrs.setStatus("mandatory")
_AccIpxPortTooShorts_Type = Counter32
_AccIpxPortTooShorts_Object = MibTableColumn
accIpxPortTooShorts = _AccIpxPortTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 11),
    _AccIpxPortTooShorts_Type()
)
accIpxPortTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTooShorts.setStatus("mandatory")
_AccIpxPortCkSums_Type = Counter32
_AccIpxPortCkSums_Object = MibTableColumn
accIpxPortCkSums = _AccIpxPortCkSums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 12),
    _AccIpxPortCkSums_Type()
)
accIpxPortCkSums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortCkSums.setStatus("mandatory")
_AccIpxPortTooLongs_Type = Counter32
_AccIpxPortTooLongs_Object = MibTableColumn
accIpxPortTooLongs = _AccIpxPortTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 13),
    _AccIpxPortTooLongs_Type()
)
accIpxPortTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortTooLongs.setStatus("mandatory")
_AccIpxPortOutErrs_Type = Counter32
_AccIpxPortOutErrs_Object = MibTableColumn
accIpxPortOutErrs = _AccIpxPortOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 14),
    _AccIpxPortOutErrs_Type()
)
accIpxPortOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortOutErrs.setStatus("mandatory")


class _AccIpxPortOpState_Type(Integer32):
    """Custom type accIpxPortOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AccIpxPortOpState_Type.__name__ = "Integer32"
_AccIpxPortOpState_Object = MibTableColumn
accIpxPortOpState = _AccIpxPortOpState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 6, 1, 15),
    _AccIpxPortOpState_Type()
)
accIpxPortOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxPortOpState.setStatus("mandatory")
_AccIpxSapStat_ObjectIdentity = ObjectIdentity
accIpxSapStat = _AccIpxSapStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7)
)
_AccIpxSapReqIns_Type = Counter32
_AccIpxSapReqIns_Object = MibScalar
accIpxSapReqIns = _AccIpxSapReqIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 1),
    _AccIpxSapReqIns_Type()
)
accIpxSapReqIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapReqIns.setStatus("mandatory")
_AccIpxSapReqOuts_Type = Counter32
_AccIpxSapReqOuts_Object = MibScalar
accIpxSapReqOuts = _AccIpxSapReqOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 2),
    _AccIpxSapReqOuts_Type()
)
accIpxSapReqOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapReqOuts.setStatus("mandatory")
_AccIpxSapRespIns_Type = Counter32
_AccIpxSapRespIns_Object = MibScalar
accIpxSapRespIns = _AccIpxSapRespIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 3),
    _AccIpxSapRespIns_Type()
)
accIpxSapRespIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapRespIns.setStatus("mandatory")
_AccIpxSapRespOuts_Type = Counter32
_AccIpxSapRespOuts_Object = MibScalar
accIpxSapRespOuts = _AccIpxSapRespOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 4),
    _AccIpxSapRespOuts_Type()
)
accIpxSapRespOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapRespOuts.setStatus("mandatory")
_AccIpxSapGetNearIns_Type = Counter32
_AccIpxSapGetNearIns_Object = MibScalar
accIpxSapGetNearIns = _AccIpxSapGetNearIns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 5),
    _AccIpxSapGetNearIns_Type()
)
accIpxSapGetNearIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapGetNearIns.setStatus("mandatory")
_AccIpxSapGetNearOuts_Type = Counter32
_AccIpxSapGetNearOuts_Object = MibScalar
accIpxSapGetNearOuts = _AccIpxSapGetNearOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 6),
    _AccIpxSapGetNearOuts_Type()
)
accIpxSapGetNearOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapGetNearOuts.setStatus("mandatory")
_AccIpxSapNoRoutes_Type = Counter32
_AccIpxSapNoRoutes_Object = MibScalar
accIpxSapNoRoutes = _AccIpxSapNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 7),
    _AccIpxSapNoRoutes_Type()
)
accIpxSapNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNoRoutes.setStatus("mandatory")
_AccIpxSapNotBests_Type = Counter32
_AccIpxSapNotBests_Object = MibScalar
accIpxSapNotBests = _AccIpxSapNotBests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 8),
    _AccIpxSapNotBests_Type()
)
accIpxSapNotBests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNotBests.setStatus("mandatory")
_AccIpxSapNoServers_Type = Counter32
_AccIpxSapNoServers_Object = MibScalar
accIpxSapNoServers = _AccIpxSapNoServers_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 9),
    _AccIpxSapNoServers_Type()
)
accIpxSapNoServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapNoServers.setStatus("mandatory")
_AccIpxSapInErrs_Type = Counter32
_AccIpxSapInErrs_Object = MibScalar
accIpxSapInErrs = _AccIpxSapInErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 10),
    _AccIpxSapInErrs_Type()
)
accIpxSapInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapInErrs.setStatus("mandatory")
_AccIpxSapOutErrs_Type = Counter32
_AccIpxSapOutErrs_Object = MibScalar
accIpxSapOutErrs = _AccIpxSapOutErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 7, 11),
    _AccIpxSapOutErrs_Type()
)
accIpxSapOutErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSapOutErrs.setStatus("mandatory")
_AccIpxSrvTable_Object = MibTable
accIpxSrvTable = _AccIpxSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8)
)
if mibBuilder.loadTexts:
    accIpxSrvTable.setStatus("mandatory")
_AccIpxSrvEntry_Object = MibTableRow
accIpxSrvEntry = _AccIpxSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1)
)
accIpxSrvEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxSrvType"),
    (0, "ACC-MIB", "accIpxSrvName"),
)
if mibBuilder.loadTexts:
    accIpxSrvEntry.setStatus("mandatory")
_AccIpxSrvName_Type = DisplayString
_AccIpxSrvName_Object = MibTableColumn
accIpxSrvName = _AccIpxSrvName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 1),
    _AccIpxSrvName_Type()
)
accIpxSrvName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvName.setStatus("mandatory")
_AccIpxSrvType_Type = OctetString
_AccIpxSrvType_Object = MibTableColumn
accIpxSrvType = _AccIpxSrvType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 2),
    _AccIpxSrvType_Type()
)
accIpxSrvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvType.setStatus("mandatory")
_AccIpxSrvHost_Type = OctetString
_AccIpxSrvHost_Object = MibTableColumn
accIpxSrvHost = _AccIpxSrvHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 3),
    _AccIpxSrvHost_Type()
)
accIpxSrvHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvHost.setStatus("mandatory")
_AccIpxSrvHops_Type = Integer32
_AccIpxSrvHops_Object = MibTableColumn
accIpxSrvHops = _AccIpxSrvHops_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 4),
    _AccIpxSrvHops_Type()
)
accIpxSrvHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvHops.setStatus("mandatory")


class _AccIpxSrvOwner_Type(Integer32):
    """Custom type accIpxSrvOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nms", 1),
          ("sap", 2))
    )


_AccIpxSrvOwner_Type.__name__ = "Integer32"
_AccIpxSrvOwner_Object = MibTableColumn
accIpxSrvOwner = _AccIpxSrvOwner_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 5),
    _AccIpxSrvOwner_Type()
)
accIpxSrvOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvOwner.setStatus("mandatory")
_AccIpxSrvAge_Type = TimeTicks
_AccIpxSrvAge_Object = MibTableColumn
accIpxSrvAge = _AccIpxSrvAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 8, 1, 6),
    _AccIpxSrvAge_Type()
)
accIpxSrvAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIpxSrvAge.setStatus("mandatory")
_AccIpxRouteFilters_ObjectIdentity = ObjectIdentity
accIpxRouteFilters = _AccIpxRouteFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9)
)


class _AccIpxRteFltrDefaultAction_Type(Integer32):
    """Custom type accIpxRteFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxRteFltrDefaultAction_Object = MibScalar
accIpxRteFltrDefaultAction = _AccIpxRteFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 1),
    _AccIpxRteFltrDefaultAction_Type()
)
accIpxRteFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrDefaultAction.setStatus("mandatory")
_AccIpxRteNbrTable_Object = MibTable
accIpxRteNbrTable = _AccIpxRteNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2)
)
if mibBuilder.loadTexts:
    accIpxRteNbrTable.setStatus("mandatory")
_AccIpxRteNbrEntry_Object = MibTableRow
accIpxRteNbrEntry = _AccIpxRteNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1)
)
accIpxRteNbrEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxRteNbrId"),
)
if mibBuilder.loadTexts:
    accIpxRteNbrEntry.setStatus("mandatory")
_AccIpxRteNbrId_Type = OctetString
_AccIpxRteNbrId_Object = MibTableColumn
accIpxRteNbrId = _AccIpxRteNbrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 1),
    _AccIpxRteNbrId_Type()
)
accIpxRteNbrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrId.setStatus("mandatory")


class _AccIpxRteNbrAction_Type(Integer32):
    """Custom type accIpxRteNbrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteNbrAction_Type.__name__ = "Integer32"
_AccIpxRteNbrAction_Object = MibTableColumn
accIpxRteNbrAction = _AccIpxRteNbrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 2),
    _AccIpxRteNbrAction_Type()
)
accIpxRteNbrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrAction.setStatus("mandatory")


class _AccIpxRteNbrStatus_Type(Integer32):
    """Custom type accIpxRteNbrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxRteNbrStatus_Type.__name__ = "Integer32"
_AccIpxRteNbrStatus_Object = MibTableColumn
accIpxRteNbrStatus = _AccIpxRteNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 2, 1, 3),
    _AccIpxRteNbrStatus_Type()
)
accIpxRteNbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteNbrStatus.setStatus("mandatory")
_AccIpxRteFltrTable_Object = MibTable
accIpxRteFltrTable = _AccIpxRteFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3)
)
if mibBuilder.loadTexts:
    accIpxRteFltrTable.setStatus("mandatory")
_AccIpxRteFltrEntry_Object = MibTableRow
accIpxRteFltrEntry = _AccIpxRteFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1)
)
accIpxRteFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxRteFltrNeighbor"),
    (0, "ACC-MIB", "accIpxRteFltrNetwork"),
)
if mibBuilder.loadTexts:
    accIpxRteFltrEntry.setStatus("mandatory")
_AccIpxRteFltrNeighbor_Type = OctetString
_AccIpxRteFltrNeighbor_Object = MibTableColumn
accIpxRteFltrNeighbor = _AccIpxRteFltrNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 1),
    _AccIpxRteFltrNeighbor_Type()
)
accIpxRteFltrNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrNeighbor.setStatus("mandatory")
_AccIpxRteFltrNetwork_Type = OctetString
_AccIpxRteFltrNetwork_Object = MibTableColumn
accIpxRteFltrNetwork = _AccIpxRteFltrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 2),
    _AccIpxRteFltrNetwork_Type()
)
accIpxRteFltrNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrNetwork.setStatus("mandatory")


class _AccIpxRteFltrAction_Type(Integer32):
    """Custom type accIpxRteFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxRteFltrAction_Type.__name__ = "Integer32"
_AccIpxRteFltrAction_Object = MibTableColumn
accIpxRteFltrAction = _AccIpxRteFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 3),
    _AccIpxRteFltrAction_Type()
)
accIpxRteFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrAction.setStatus("mandatory")


class _AccIpxRteFltrStatus_Type(Integer32):
    """Custom type accIpxRteFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxRteFltrStatus_Type.__name__ = "Integer32"
_AccIpxRteFltrStatus_Object = MibTableColumn
accIpxRteFltrStatus = _AccIpxRteFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 9, 3, 1, 4),
    _AccIpxRteFltrStatus_Type()
)
accIpxRteFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxRteFltrStatus.setStatus("mandatory")
_AccIpxNetworkFilters_ObjectIdentity = ObjectIdentity
accIpxNetworkFilters = _AccIpxNetworkFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10)
)


class _AccIpxNetFltrDefaultAction_Type(Integer32):
    """Custom type accIpxNetFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccIpxNetFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxNetFltrDefaultAction_Object = MibScalar
accIpxNetFltrDefaultAction = _AccIpxNetFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 1),
    _AccIpxNetFltrDefaultAction_Type()
)
accIpxNetFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDefaultAction.setStatus("mandatory")
_OldIpxNetFltrTable_Object = MibTable
oldIpxNetFltrTable = _OldIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2)
)
if mibBuilder.loadTexts:
    oldIpxNetFltrTable.setStatus("deprecated")
_OldIpxNetFltrEntry_Object = MibTableRow
oldIpxNetFltrEntry = _OldIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1)
)
oldIpxNetFltrEntry.setIndexNames(
    (0, "ACC-MIB", "oldIpxNetFltrDestination"),
    (0, "ACC-MIB", "oldIpxNetFltrSource"),
)
if mibBuilder.loadTexts:
    oldIpxNetFltrEntry.setStatus("deprecated")
_OldIpxNetFltrDestination_Type = OctetString
_OldIpxNetFltrDestination_Object = MibTableColumn
oldIpxNetFltrDestination = _OldIpxNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 1),
    _OldIpxNetFltrDestination_Type()
)
oldIpxNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrDestination.setStatus("deprecated")
_OldIpxNetFltrSource_Type = OctetString
_OldIpxNetFltrSource_Object = MibTableColumn
oldIpxNetFltrSource = _OldIpxNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 2),
    _OldIpxNetFltrSource_Type()
)
oldIpxNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrSource.setStatus("deprecated")


class _OldIpxNetFltrAction_Type(Integer32):
    """Custom type oldIpxNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_OldIpxNetFltrAction_Type.__name__ = "Integer32"
_OldIpxNetFltrAction_Object = MibTableColumn
oldIpxNetFltrAction = _OldIpxNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 3),
    _OldIpxNetFltrAction_Type()
)
oldIpxNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrAction.setStatus("deprecated")


class _OldIpxNetFltrStatus_Type(Integer32):
    """Custom type oldIpxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_OldIpxNetFltrStatus_Type.__name__ = "Integer32"
_OldIpxNetFltrStatus_Object = MibTableColumn
oldIpxNetFltrStatus = _OldIpxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 2, 1, 4),
    _OldIpxNetFltrStatus_Type()
)
oldIpxNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oldIpxNetFltrStatus.setStatus("deprecated")
_AccIpxNetFltrTable_Object = MibTable
accIpxNetFltrTable = _AccIpxNetFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3)
)
if mibBuilder.loadTexts:
    accIpxNetFltrTable.setStatus("mandatory")
_AccIpxNetFltrEntry_Object = MibTableRow
accIpxNetFltrEntry = _AccIpxNetFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1)
)
accIpxNetFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxNetFltrDestination"),
    (0, "ACC-MIB", "accIpxNetFltrSource"),
    (0, "ACC-MIB", "accIpxNetFltrDestSkt"),
    (0, "ACC-MIB", "accIpxNetFltrSrcSkt"),
    (0, "ACC-MIB", "accIpxNetFltrPktType"),
)
if mibBuilder.loadTexts:
    accIpxNetFltrEntry.setStatus("mandatory")
_AccIpxNetFltrDestination_Type = OctetString
_AccIpxNetFltrDestination_Object = MibTableColumn
accIpxNetFltrDestination = _AccIpxNetFltrDestination_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 1),
    _AccIpxNetFltrDestination_Type()
)
accIpxNetFltrDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDestination.setStatus("mandatory")
_AccIpxNetFltrSource_Type = OctetString
_AccIpxNetFltrSource_Object = MibTableColumn
accIpxNetFltrSource = _AccIpxNetFltrSource_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 2),
    _AccIpxNetFltrSource_Type()
)
accIpxNetFltrSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrSource.setStatus("mandatory")


class _AccIpxNetFltrAction_Type(Integer32):
    """Custom type accIpxNetFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccIpxNetFltrAction_Type.__name__ = "Integer32"
_AccIpxNetFltrAction_Object = MibTableColumn
accIpxNetFltrAction = _AccIpxNetFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 3),
    _AccIpxNetFltrAction_Type()
)
accIpxNetFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrAction.setStatus("mandatory")


class _AccIpxNetFltrStatus_Type(Integer32):
    """Custom type accIpxNetFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxNetFltrStatus_Type.__name__ = "Integer32"
_AccIpxNetFltrStatus_Object = MibTableColumn
accIpxNetFltrStatus = _AccIpxNetFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 4),
    _AccIpxNetFltrStatus_Type()
)
accIpxNetFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrStatus.setStatus("mandatory")
_AccIpxNetFltrDestSkt_Type = OctetString
_AccIpxNetFltrDestSkt_Object = MibTableColumn
accIpxNetFltrDestSkt = _AccIpxNetFltrDestSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 5),
    _AccIpxNetFltrDestSkt_Type()
)
accIpxNetFltrDestSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrDestSkt.setStatus("mandatory")
_AccIpxNetFltrSrcSkt_Type = OctetString
_AccIpxNetFltrSrcSkt_Object = MibTableColumn
accIpxNetFltrSrcSkt = _AccIpxNetFltrSrcSkt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 6),
    _AccIpxNetFltrSrcSkt_Type()
)
accIpxNetFltrSrcSkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrSrcSkt.setStatus("mandatory")
_AccIpxNetFltrPktType_Type = Integer32
_AccIpxNetFltrPktType_Object = MibTableColumn
accIpxNetFltrPktType = _AccIpxNetFltrPktType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 10, 3, 1, 7),
    _AccIpxNetFltrPktType_Type()
)
accIpxNetFltrPktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxNetFltrPktType.setStatus("mandatory")
_AccIpxHostFilters_ObjectIdentity = ObjectIdentity
accIpxHostFilters = _AccIpxHostFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11)
)


class _AccIpxHostFltrDefaultAction_Type(Integer32):
    """Custom type accIpxHostFltrDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccIpxHostFltrDefaultAction_Type.__name__ = "Integer32"
_AccIpxHostFltrDefaultAction_Object = MibScalar
accIpxHostFltrDefaultAction = _AccIpxHostFltrDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 1),
    _AccIpxHostFltrDefaultAction_Type()
)
accIpxHostFltrDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrDefaultAction.setStatus("mandatory")
_AccIpxHostFltrTable_Object = MibTable
accIpxHostFltrTable = _AccIpxHostFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2)
)
if mibBuilder.loadTexts:
    accIpxHostFltrTable.setStatus("mandatory")
_AccIpxHostFltrEntry_Object = MibTableRow
accIpxHostFltrEntry = _AccIpxHostFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1)
)
accIpxHostFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxHostFltrId"),
    (0, "ACC-MIB", "accIpxHostFltrSocket"),
    (0, "ACC-MIB", "accIpxHostFltrPepClient"),
)
if mibBuilder.loadTexts:
    accIpxHostFltrEntry.setStatus("mandatory")
_AccIpxHostFltrId_Type = OctetString
_AccIpxHostFltrId_Object = MibTableColumn
accIpxHostFltrId = _AccIpxHostFltrId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 1),
    _AccIpxHostFltrId_Type()
)
accIpxHostFltrId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrId.setStatus("mandatory")
_AccIpxHostFltrSocket_Type = OctetString
_AccIpxHostFltrSocket_Object = MibTableColumn
accIpxHostFltrSocket = _AccIpxHostFltrSocket_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 2),
    _AccIpxHostFltrSocket_Type()
)
accIpxHostFltrSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrSocket.setStatus("mandatory")
_AccIpxHostFltrPepClient_Type = OctetString
_AccIpxHostFltrPepClient_Object = MibTableColumn
accIpxHostFltrPepClient = _AccIpxHostFltrPepClient_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 3),
    _AccIpxHostFltrPepClient_Type()
)
accIpxHostFltrPepClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrPepClient.setStatus("mandatory")


class _AccIpxHostFltrAction_Type(Integer32):
    """Custom type accIpxHostFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccIpxHostFltrAction_Type.__name__ = "Integer32"
_AccIpxHostFltrAction_Object = MibTableColumn
accIpxHostFltrAction = _AccIpxHostFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 4),
    _AccIpxHostFltrAction_Type()
)
accIpxHostFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrAction.setStatus("mandatory")


class _AccIpxHostFltrStatus_Type(Integer32):
    """Custom type accIpxHostFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxHostFltrStatus_Type.__name__ = "Integer32"
_AccIpxHostFltrStatus_Object = MibTableColumn
accIpxHostFltrStatus = _AccIpxHostFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 11, 2, 1, 5),
    _AccIpxHostFltrStatus_Type()
)
accIpxHostFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxHostFltrStatus.setStatus("mandatory")
_AccIpxSapFilters_ObjectIdentity = ObjectIdentity
accIpxSapFilters = _AccIpxSapFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12)
)


class _AccIpxSapFltrDefault_Type(Integer32):
    """Custom type accIpxSapFltrDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxSapFltrDefault_Type.__name__ = "Integer32"
_AccIpxSapFltrDefault_Object = MibScalar
accIpxSapFltrDefault = _AccIpxSapFltrDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 1),
    _AccIpxSapFltrDefault_Type()
)
accIpxSapFltrDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrDefault.setStatus("mandatory")
_AccIpxSapFltrTable_Object = MibTable
accIpxSapFltrTable = _AccIpxSapFltrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2)
)
if mibBuilder.loadTexts:
    accIpxSapFltrTable.setStatus("mandatory")
_AccIpxSapFltrEntry_Object = MibTableRow
accIpxSapFltrEntry = _AccIpxSapFltrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1)
)
accIpxSapFltrEntry.setIndexNames(
    (0, "ACC-MIB", "accIpxSapFltrSrvType"),
    (0, "ACC-MIB", "accIpxSapFltrSrvName"),
)
if mibBuilder.loadTexts:
    accIpxSapFltrEntry.setStatus("mandatory")
_AccIpxSapFltrSrvType_Type = OctetString
_AccIpxSapFltrSrvType_Object = MibTableColumn
accIpxSapFltrSrvType = _AccIpxSapFltrSrvType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 1),
    _AccIpxSapFltrSrvType_Type()
)
accIpxSapFltrSrvType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrSrvType.setStatus("mandatory")
_AccIpxSapFltrSrvName_Type = OctetString
_AccIpxSapFltrSrvName_Object = MibTableColumn
accIpxSapFltrSrvName = _AccIpxSapFltrSrvName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 2),
    _AccIpxSapFltrSrvName_Type()
)
accIpxSapFltrSrvName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrSrvName.setStatus("mandatory")


class _AccIpxSapFltrAction_Type(Integer32):
    """Custom type accIpxSapFltrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccIpxSapFltrAction_Type.__name__ = "Integer32"
_AccIpxSapFltrAction_Object = MibTableColumn
accIpxSapFltrAction = _AccIpxSapFltrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 3),
    _AccIpxSapFltrAction_Type()
)
accIpxSapFltrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrAction.setStatus("mandatory")


class _AccIpxSapFltrStatus_Type(Integer32):
    """Custom type accIpxSapFltrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccIpxSapFltrStatus_Type.__name__ = "Integer32"
_AccIpxSapFltrStatus_Object = MibTableColumn
accIpxSapFltrStatus = _AccIpxSapFltrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 12, 2, 1, 4),
    _AccIpxSapFltrStatus_Type()
)
accIpxSapFltrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxSapFltrStatus.setStatus("mandatory")
_AccIpxNetWdParms_ObjectIdentity = ObjectIdentity
accIpxNetWdParms = _AccIpxNetWdParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13)
)


class _AccIpxWdProxyDuration_Type(Integer32):
    """Custom type accIpxWdProxyDuration based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AccIpxWdProxyDuration_Type.__name__ = "Integer32"
_AccIpxWdProxyDuration_Object = MibScalar
accIpxWdProxyDuration = _AccIpxWdProxyDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 1),
    _AccIpxWdProxyDuration_Type()
)
accIpxWdProxyDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdProxyDuration.setStatus("mandatory")


class _AccIpxWdHoldPeriod_Type(Integer32):
    """Custom type accIpxWdHoldPeriod based on Integer32"""
    defaultValue = 960

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(960, 60600),
    )


_AccIpxWdHoldPeriod_Type.__name__ = "Integer32"
_AccIpxWdHoldPeriod_Object = MibScalar
accIpxWdHoldPeriod = _AccIpxWdHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 2),
    _AccIpxWdHoldPeriod_Type()
)
accIpxWdHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdHoldPeriod.setStatus("mandatory")


class _AccIpxWdMaxSessions_Type(Integer32):
    """Custom type accIpxWdMaxSessions based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AccIpxWdMaxSessions_Type.__name__ = "Integer32"
_AccIpxWdMaxSessions_Object = MibScalar
accIpxWdMaxSessions = _AccIpxWdMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 3),
    _AccIpxWdMaxSessions_Type()
)
accIpxWdMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdMaxSessions.setStatus("mandatory")


class _AccIpxWdDiagLevel_Type(Integer32):
    """Custom type accIpxWdDiagLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccIpxWdDiagLevel_Type.__name__ = "Integer32"
_AccIpxWdDiagLevel_Object = MibScalar
accIpxWdDiagLevel = _AccIpxWdDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 22, 13, 4),
    _AccIpxWdDiagLevel_Type()
)
accIpxWdDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpxWdDiagLevel.setStatus("mandatory")
_IpMultiPathTable_Object = MibTable
ipMultiPathTable = _IpMultiPathTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23)
)
if mibBuilder.loadTexts:
    ipMultiPathTable.setStatus("mandatory")
_IpMultiPathEntry_Object = MibTableRow
ipMultiPathEntry = _IpMultiPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1)
)
ipMultiPathEntry.setIndexNames(
    (0, "ACC-MIB", "ipMultiPathDest"),
    (0, "ACC-MIB", "ipMultiPathPolicy"),
    (0, "ACC-MIB", "ipMultiPathNextHop"),
)
if mibBuilder.loadTexts:
    ipMultiPathEntry.setStatus("mandatory")
_IpMultiPathDest_Type = IpAddress
_IpMultiPathDest_Object = MibTableColumn
ipMultiPathDest = _IpMultiPathDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 1),
    _IpMultiPathDest_Type()
)
ipMultiPathDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathDest.setStatus("mandatory")
_IpMultiPathPolicy_Type = Integer32
_IpMultiPathPolicy_Object = MibTableColumn
ipMultiPathPolicy = _IpMultiPathPolicy_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 2),
    _IpMultiPathPolicy_Type()
)
ipMultiPathPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathPolicy.setStatus("mandatory")
_IpMultiPathIfIndex_Type = Integer32
_IpMultiPathIfIndex_Object = MibTableColumn
ipMultiPathIfIndex = _IpMultiPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 3),
    _IpMultiPathIfIndex_Type()
)
ipMultiPathIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathIfIndex.setStatus("mandatory")
_IpMultiPathMask_Type = IpAddress
_IpMultiPathMask_Object = MibTableColumn
ipMultiPathMask = _IpMultiPathMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 4),
    _IpMultiPathMask_Type()
)
ipMultiPathMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathMask.setStatus("mandatory")
_IpMultiPathNextHop_Type = IpAddress
_IpMultiPathNextHop_Object = MibTableColumn
ipMultiPathNextHop = _IpMultiPathNextHop_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 5),
    _IpMultiPathNextHop_Type()
)
ipMultiPathNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathNextHop.setStatus("mandatory")
_IpMultiPathMetric_Type = Integer32
_IpMultiPathMetric_Object = MibTableColumn
ipMultiPathMetric = _IpMultiPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 6),
    _IpMultiPathMetric_Type()
)
ipMultiPathMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathMetric.setStatus("mandatory")


class _IpMultiPathType_Type(Integer32):
    """Custom type ipMultiPathType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_IpMultiPathType_Type.__name__ = "Integer32"
_IpMultiPathType_Object = MibTableColumn
ipMultiPathType = _IpMultiPathType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 7),
    _IpMultiPathType_Type()
)
ipMultiPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathType.setStatus("mandatory")


class _IpMultiPathProto_Type(Integer32):
    """Custom type ipMultiPathProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              13)
        )
    )
    namedValues = NamedValues(
        *(("egp", 5),
          ("icmp", 4),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpMultiPathProto_Type.__name__ = "Integer32"
_IpMultiPathProto_Object = MibTableColumn
ipMultiPathProto = _IpMultiPathProto_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 8),
    _IpMultiPathProto_Type()
)
ipMultiPathProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathProto.setStatus("mandatory")
_IpMultiPathAge_Type = Integer32
_IpMultiPathAge_Object = MibTableColumn
ipMultiPathAge = _IpMultiPathAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 23, 1, 9),
    _IpMultiPathAge_Type()
)
ipMultiPathAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMultiPathAge.setStatus("mandatory")
_AccTr_ObjectIdentity = ObjectIdentity
accTr = _AccTr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24)
)
_AccTrNumber_Type = Integer32
_AccTrNumber_Object = MibScalar
accTrNumber = _AccTrNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 1),
    _AccTrNumber_Type()
)
accTrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrNumber.setStatus("mandatory")
_AccTrTable_Object = MibTable
accTrTable = _AccTrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2)
)
if mibBuilder.loadTexts:
    accTrTable.setStatus("mandatory")
_AccTrEntry_Object = MibTableRow
accTrEntry = _AccTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1)
)
accTrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    accTrEntry.setStatus("mandatory")


class _AccTrEarlyRelease_Type(Integer32):
    """Custom type accTrEarlyRelease based on Integer32"""
    defaultValue = 1

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


_AccTrEarlyRelease_Type.__name__ = "Integer32"
_AccTrEarlyRelease_Object = MibTableColumn
accTrEarlyRelease = _AccTrEarlyRelease_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1, 2),
    _AccTrEarlyRelease_Type()
)
accTrEarlyRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrEarlyRelease.setStatus("mandatory")
_AccTrMACAddr_Type = OctetString
_AccTrMACAddr_Object = MibTableColumn
accTrMACAddr = _AccTrMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1, 3),
    _AccTrMACAddr_Type()
)
accTrMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrMACAddr.setStatus("mandatory")
_AccTrDefaultRingId_Type = Integer32
_AccTrDefaultRingId_Object = MibTableColumn
accTrDefaultRingId = _AccTrDefaultRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1, 4),
    _AccTrDefaultRingId_Type()
)
accTrDefaultRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accTrDefaultRingId.setStatus("mandatory")
_AccTrActiveRingId_Type = Integer32
_AccTrActiveRingId_Object = MibTableColumn
accTrActiveRingId = _AccTrActiveRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1, 5),
    _AccTrActiveRingId_Type()
)
accTrActiveRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrActiveRingId.setStatus("mandatory")


class _AccTrRingSrvStatus_Type(Integer32):
    """Custom type accTrRingSrvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("found", 1),
          ("not-found", 2))
    )


_AccTrRingSrvStatus_Type.__name__ = "Integer32"
_AccTrRingSrvStatus_Object = MibTableColumn
accTrRingSrvStatus = _AccTrRingSrvStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 24, 2, 1, 6),
    _AccTrRingSrvStatus_Type()
)
accTrRingSrvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTrRingSrvStatus.setStatus("mandatory")
_AccSr_ObjectIdentity = ObjectIdentity
accSr = _AccSr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25)
)
_AccSrBridge_ObjectIdentity = ObjectIdentity
accSrBridge = _AccSrBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1)
)
_AccSrBridgeId_Type = Integer32
_AccSrBridgeId_Object = MibScalar
accSrBridgeId = _AccSrBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 1),
    _AccSrBridgeId_Type()
)
accSrBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrBridgeId.setStatus("mandatory")
_AccSrVirRingId_Type = Integer32
_AccSrVirRingId_Object = MibScalar
accSrVirRingId = _AccSrVirRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 2),
    _AccSrVirRingId_Type()
)
accSrVirRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrVirRingId.setStatus("mandatory")
_AccSrHopLimit_Type = Integer32
_AccSrHopLimit_Object = MibScalar
accSrHopLimit = _AccSrHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 3),
    _AccSrHopLimit_Type()
)
accSrHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrHopLimit.setStatus("mandatory")


class _AccSrSingleRtBcast_Type(Integer32):
    """Custom type accSrSingleRtBcast based on Integer32"""
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


_AccSrSingleRtBcast_Type.__name__ = "Integer32"
_AccSrSingleRtBcast_Object = MibScalar
accSrSingleRtBcast = _AccSrSingleRtBcast_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 4),
    _AccSrSingleRtBcast_Type()
)
accSrSingleRtBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrSingleRtBcast.setStatus("mandatory")


class _AccSrNumPorts_Type(Integer32):
    """Custom type accSrNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_AccSrNumPorts_Type.__name__ = "Integer32"
_AccSrNumPorts_Object = MibScalar
accSrNumPorts = _AccSrNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 5),
    _AccSrNumPorts_Type()
)
accSrNumPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrNumPorts.setStatus("mandatory")
_AccSrRifTimer_Type = Integer32
_AccSrRifTimer_Object = MibScalar
accSrRifTimer = _AccSrRifTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 6),
    _AccSrRifTimer_Type()
)
accSrRifTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRifTimer.setStatus("mandatory")
_AccSrSdsInterval_Type = TimeTicks
_AccSrSdsInterval_Object = MibScalar
accSrSdsInterval = _AccSrSdsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 1, 7),
    _AccSrSdsInterval_Type()
)
accSrSdsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrSdsInterval.setStatus("mandatory")
_AccSrPortParmTable_Object = MibTable
accSrPortParmTable = _AccSrPortParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2)
)
if mibBuilder.loadTexts:
    accSrPortParmTable.setStatus("mandatory")
_AccSrPortParmEntry_Object = MibTableRow
accSrPortParmEntry = _AccSrPortParmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1)
)
accSrPortParmEntry.setIndexNames(
    (0, "ACC-MIB", "accSrParmsIndex"),
)
if mibBuilder.loadTexts:
    accSrPortParmEntry.setStatus("mandatory")
_AccSrParmsIndex_Type = Integer32
_AccSrParmsIndex_Object = MibTableColumn
accSrParmsIndex = _AccSrParmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 1),
    _AccSrParmsIndex_Type()
)
accSrParmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrParmsIndex.setStatus("mandatory")


class _AccSrAdminStatus_Type(Integer32):
    """Custom type accSrAdminStatus based on Integer32"""
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


_AccSrAdminStatus_Type.__name__ = "Integer32"
_AccSrAdminStatus_Object = MibTableColumn
accSrAdminStatus = _AccSrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 2),
    _AccSrAdminStatus_Type()
)
accSrAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrAdminStatus.setStatus("mandatory")


class _AccSrOperStatus_Type(Integer32):
    """Custom type accSrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("forwarding", 1))
    )


_AccSrOperStatus_Type.__name__ = "Integer32"
_AccSrOperStatus_Object = MibTableColumn
accSrOperStatus = _AccSrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 3),
    _AccSrOperStatus_Type()
)
accSrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrOperStatus.setStatus("mandatory")


class _AccSrPortProtocol_Type(Integer32):
    """Custom type accSrPortProtocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dial", 10),
          ("enet", 1),
          ("fddi", 9),
          ("ffr", 4),
          ("lapb", 3),
          ("multilink", 11),
          ("other", 5),
          ("ppp", 8),
          ("smds", 7),
          ("token-ring", 6),
          ("x25", 2))
    )


_AccSrPortProtocol_Type.__name__ = "Integer32"
_AccSrPortProtocol_Object = MibTableColumn
accSrPortProtocol = _AccSrPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 4),
    _AccSrPortProtocol_Type()
)
accSrPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortProtocol.setStatus("mandatory")
_AccSrPortLine_Type = Integer32
_AccSrPortLine_Object = MibTableColumn
accSrPortLine = _AccSrPortLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 5),
    _AccSrPortLine_Type()
)
accSrPortLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortLine.setStatus("mandatory")
_AccSrPortFrDlci_Type = Integer32
_AccSrPortFrDlci_Object = MibTableColumn
accSrPortFrDlci = _AccSrPortFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 6),
    _AccSrPortFrDlci_Type()
)
accSrPortFrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortFrDlci.setStatus("mandatory")


class _AccSrPortXBridgeStatus_Type(Integer32):
    """Custom type accSrPortXBridgeStatus based on Integer32"""
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


_AccSrPortXBridgeStatus_Type.__name__ = "Integer32"
_AccSrPortXBridgeStatus_Object = MibTableColumn
accSrPortXBridgeStatus = _AccSrPortXBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 7),
    _AccSrPortXBridgeStatus_Type()
)
accSrPortXBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortXBridgeStatus.setStatus("mandatory")
_AccSrPortVirRingId_Type = Integer32
_AccSrPortVirRingId_Object = MibTableColumn
accSrPortVirRingId = _AccSrPortVirRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 8),
    _AccSrPortVirRingId_Type()
)
accSrPortVirRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortVirRingId.setStatus("mandatory")


class _AccSrPortSrMethod_Type(Integer32):
    """Custom type accSrPortSrMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sr1", 1),
          ("sr2", 2))
    )


_AccSrPortSrMethod_Type.__name__ = "Integer32"
_AccSrPortSrMethod_Object = MibTableColumn
accSrPortSrMethod = _AccSrPortSrMethod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 2, 1, 9),
    _AccSrPortSrMethod_Type()
)
accSrPortSrMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortSrMethod.setStatus("mandatory")
_AccSrPortStatsTable_Object = MibTable
accSrPortStatsTable = _AccSrPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3)
)
if mibBuilder.loadTexts:
    accSrPortStatsTable.setStatus("mandatory")
_AccSrPortStatsEntry_Object = MibTableRow
accSrPortStatsEntry = _AccSrPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1)
)
accSrPortStatsEntry.setIndexNames(
    (0, "ACC-MIB", "accStatsIndex"),
)
if mibBuilder.loadTexts:
    accSrPortStatsEntry.setStatus("mandatory")
_AccStatsIndex_Type = Integer32
_AccStatsIndex_Object = MibTableColumn
accStatsIndex = _AccStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 1),
    _AccStatsIndex_Type()
)
accStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStatsIndex.setStatus("mandatory")
_AccInBcastPkts_Type = Counter32
_AccInBcastPkts_Object = MibTableColumn
accInBcastPkts = _AccInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 2),
    _AccInBcastPkts_Type()
)
accInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInBcastPkts.setStatus("mandatory")
_AccInUcastPkts_Type = Counter32
_AccInUcastPkts_Object = MibTableColumn
accInUcastPkts = _AccInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 3),
    _AccInUcastPkts_Type()
)
accInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInUcastPkts.setStatus("mandatory")
_AccOutBcastPkts_Type = Counter32
_AccOutBcastPkts_Object = MibTableColumn
accOutBcastPkts = _AccOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 4),
    _AccOutBcastPkts_Type()
)
accOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutBcastPkts.setStatus("mandatory")
_AccOutUcastPkts_Type = Counter32
_AccOutUcastPkts_Object = MibTableColumn
accOutUcastPkts = _AccOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 5),
    _AccOutUcastPkts_Type()
)
accOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutUcastPkts.setStatus("mandatory")
_AccInSDSPkts_Type = Counter32
_AccInSDSPkts_Object = MibTableColumn
accInSDSPkts = _AccInSDSPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 6),
    _AccInSDSPkts_Type()
)
accInSDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInSDSPkts.setStatus("mandatory")
_AccInAPEPkts_Type = Counter32
_AccInAPEPkts_Object = MibTableColumn
accInAPEPkts = _AccInAPEPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 7),
    _AccInAPEPkts_Type()
)
accInAPEPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInAPEPkts.setStatus("mandatory")
_AccOutSDSPkts_Type = Counter32
_AccOutSDSPkts_Object = MibTableColumn
accOutSDSPkts = _AccOutSDSPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 8),
    _AccOutSDSPkts_Type()
)
accOutSDSPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutSDSPkts.setStatus("mandatory")
_AccOutAPEPkts_Type = Counter32
_AccOutAPEPkts_Object = MibTableColumn
accOutAPEPkts = _AccOutAPEPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 9),
    _AccOutAPEPkts_Type()
)
accOutAPEPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutAPEPkts.setStatus("mandatory")
_AccInDiscPkts_Type = Counter32
_AccInDiscPkts_Object = MibTableColumn
accInDiscPkts = _AccInDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 10),
    _AccInDiscPkts_Type()
)
accInDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInDiscPkts.setStatus("mandatory")
_AccOutDelayDiscPkts_Type = Counter32
_AccOutDelayDiscPkts_Object = MibTableColumn
accOutDelayDiscPkts = _AccOutDelayDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 11),
    _AccOutDelayDiscPkts_Type()
)
accOutDelayDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutDelayDiscPkts.setStatus("mandatory")
_AccOutPrioDiscPkts_Type = Counter32
_AccOutPrioDiscPkts_Object = MibTableColumn
accOutPrioDiscPkts = _AccOutPrioDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 12),
    _AccOutPrioDiscPkts_Type()
)
accOutPrioDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutPrioDiscPkts.setStatus("mandatory")
_AccInMcastPkts_Type = Counter32
_AccInMcastPkts_Object = MibTableColumn
accInMcastPkts = _AccInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 13),
    _AccInMcastPkts_Type()
)
accInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accInMcastPkts.setStatus("mandatory")
_AccOutMcastPkts_Type = Counter32
_AccOutMcastPkts_Object = MibTableColumn
accOutMcastPkts = _AccOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 3, 1, 14),
    _AccOutMcastPkts_Type()
)
accOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accOutMcastPkts.setStatus("mandatory")
_AccSrRouteTable_Object = MibTable
accSrRouteTable = _AccSrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4)
)
if mibBuilder.loadTexts:
    accSrRouteTable.setStatus("mandatory")
_AccSrRouteEntry_Object = MibTableRow
accSrRouteEntry = _AccSrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4, 1)
)
accSrRouteEntry.setIndexNames(
    (0, "ACC-MIB", "accSrRtDest"),
)
if mibBuilder.loadTexts:
    accSrRouteEntry.setStatus("mandatory")
_AccSrRtDest_Type = OctetString
_AccSrRtDest_Object = MibTableColumn
accSrRtDest = _AccSrRtDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4, 1, 1),
    _AccSrRtDest_Type()
)
accSrRtDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrRtDest.setStatus("mandatory")
_AccSrRtControl_Type = Integer32
_AccSrRtControl_Object = MibTableColumn
accSrRtControl = _AccSrRtControl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4, 1, 2),
    _AccSrRtControl_Type()
)
accSrRtControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrRtControl.setStatus("mandatory")
_AccSrRtDesc_Type = OctetString
_AccSrRtDesc_Object = MibTableColumn
accSrRtDesc = _AccSrRtDesc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4, 1, 3),
    _AccSrRtDesc_Type()
)
accSrRtDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrRtDesc.setStatus("mandatory")
_AccSrRtIfIndex_Type = Integer32
_AccSrRtIfIndex_Object = MibTableColumn
accSrRtIfIndex = _AccSrRtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 4, 1, 4),
    _AccSrRtIfIndex_Type()
)
accSrRtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrRtIfIndex.setStatus("mandatory")
_AccSrFilterTable_Object = MibTable
accSrFilterTable = _AccSrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 5)
)
if mibBuilder.loadTexts:
    accSrFilterTable.setStatus("deprecated")
_AccSrFilterEntry_Object = MibTableRow
accSrFilterEntry = _AccSrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 5, 1)
)
accSrFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accSrFilterDest"),
    (0, "ACC-MIB", "accSrFilterSrc"),
)
if mibBuilder.loadTexts:
    accSrFilterEntry.setStatus("deprecated")
_AccSrFilterDest_Type = OctetString
_AccSrFilterDest_Object = MibTableColumn
accSrFilterDest = _AccSrFilterDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 5, 1, 1),
    _AccSrFilterDest_Type()
)
accSrFilterDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFilterDest.setStatus("deprecated")
_AccSrFilterSrc_Type = OctetString
_AccSrFilterSrc_Object = MibTableColumn
accSrFilterSrc = _AccSrFilterSrc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 5, 1, 2),
    _AccSrFilterSrc_Type()
)
accSrFilterSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFilterSrc.setStatus("deprecated")


class _AccSrFilterAction_Type(Integer32):
    """Custom type accSrFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccSrFilterAction_Type.__name__ = "Integer32"
_AccSrFilterAction_Object = MibTableColumn
accSrFilterAction = _AccSrFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 5, 1, 3),
    _AccSrFilterAction_Type()
)
accSrFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFilterAction.setStatus("deprecated")
_AccSrFpTable_Object = MibTable
accSrFpTable = _AccSrFpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 6)
)
if mibBuilder.loadTexts:
    accSrFpTable.setStatus("mandatory")
_AccSrFpEntry_Object = MibTableRow
accSrFpEntry = _AccSrFpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 6, 1)
)
accSrFpEntry.setIndexNames(
    (0, "ACC-MIB", "accSrFpIndex"),
)
if mibBuilder.loadTexts:
    accSrFpEntry.setStatus("mandatory")
_AccSrFpIndex_Type = Integer32
_AccSrFpIndex_Object = MibTableColumn
accSrFpIndex = _AccSrFpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 6, 1, 1),
    _AccSrFpIndex_Type()
)
accSrFpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFpIndex.setStatus("mandatory")


class _AccSrFpProt_Type(Integer32):
    """Custom type accSrFpProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccSrFpProt_Type.__name__ = "Integer32"
_AccSrFpProt_Object = MibTableColumn
accSrFpProt = _AccSrFpProt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 6, 1, 2),
    _AccSrFpProt_Type()
)
accSrFpProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFpProt.setStatus("mandatory")


class _AccSrFpPrio_Type(Integer32):
    """Custom type accSrFpPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccSrFpPrio_Type.__name__ = "Integer32"
_AccSrFpPrio_Object = MibTableColumn
accSrFpPrio = _AccSrFpPrio_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 6, 1, 3),
    _AccSrFpPrio_Type()
)
accSrFpPrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFpPrio.setStatus("mandatory")
_AccSrFpDefaults_ObjectIdentity = ObjectIdentity
accSrFpDefaults = _AccSrFpDefaults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 7)
)


class _AccSrFpPriDefault_Type(Integer32):
    """Custom type accSrFpPriDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccSrFpPriDefault_Type.__name__ = "Integer32"
_AccSrFpPriDefault_Object = MibScalar
accSrFpPriDefault = _AccSrFpPriDefault_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 7, 1),
    _AccSrFpPriDefault_Type()
)
accSrFpPriDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFpPriDefault.setStatus("mandatory")
_AccSrPortFRTable_Object = MibTable
accSrPortFRTable = _AccSrPortFRTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 9)
)
if mibBuilder.loadTexts:
    accSrPortFRTable.setStatus("mandatory")
_AccSrPortFREntry_Object = MibTableRow
accSrPortFREntry = _AccSrPortFREntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 9, 1)
)
accSrPortFREntry.setIndexNames(
    (0, "ACC-MIB", "accSrPortFRport"),
)
if mibBuilder.loadTexts:
    accSrPortFREntry.setStatus("mandatory")
_AccSrPortFRport_Type = Integer32
_AccSrPortFRport_Object = MibTableColumn
accSrPortFRport = _AccSrPortFRport_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 9, 1, 1),
    _AccSrPortFRport_Type()
)
accSrPortFRport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrPortFRport.setStatus("mandatory")
_AccSrPortFRdlci_Type = Integer32
_AccSrPortFRdlci_Object = MibTableColumn
accSrPortFRdlci = _AccSrPortFRdlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 9, 1, 2),
    _AccSrPortFRdlci_Type()
)
accSrPortFRdlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortFRdlci.setStatus("mandatory")


class _AccSrPortFRencap_Type(Integer32):
    """Custom type accSrPortFRencap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("en1", 1),
          ("en2", 2))
    )


_AccSrPortFRencap_Type.__name__ = "Integer32"
_AccSrPortFRencap_Object = MibTableColumn
accSrPortFRencap = _AccSrPortFRencap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 9, 1, 3),
    _AccSrPortFRencap_Type()
)
accSrPortFRencap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortFRencap.setStatus("mandatory")
_AccSrPortX25Table_Object = MibTable
accSrPortX25Table = _AccSrPortX25Table_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10)
)
if mibBuilder.loadTexts:
    accSrPortX25Table.setStatus("mandatory")
_AccSrPortX25Entry_Object = MibTableRow
accSrPortX25Entry = _AccSrPortX25Entry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1)
)
accSrPortX25Entry.setIndexNames(
    (0, "ACC-MIB", "accSrPortX25port"),
)
if mibBuilder.loadTexts:
    accSrPortX25Entry.setStatus("mandatory")
_AccSrPortX25port_Type = Integer32
_AccSrPortX25port_Object = MibTableColumn
accSrPortX25port = _AccSrPortX25port_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 1),
    _AccSrPortX25port_Type()
)
accSrPortX25port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrPortX25port.setStatus("mandatory")
_AccSrPortX25addr1_Type = Integer32
_AccSrPortX25addr1_Object = MibTableColumn
accSrPortX25addr1 = _AccSrPortX25addr1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 2),
    _AccSrPortX25addr1_Type()
)
accSrPortX25addr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25addr1.setStatus("mandatory")
_AccSrPortX25addr2_Type = Integer32
_AccSrPortX25addr2_Object = MibTableColumn
accSrPortX25addr2 = _AccSrPortX25addr2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 3),
    _AccSrPortX25addr2_Type()
)
accSrPortX25addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25addr2.setStatus("mandatory")
_AccSrPortX25idleTime_Type = Integer32
_AccSrPortX25idleTime_Object = MibTableColumn
accSrPortX25idleTime = _AccSrPortX25idleTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 4),
    _AccSrPortX25idleTime_Type()
)
accSrPortX25idleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25idleTime.setStatus("mandatory")
_AccSrPortX25pktNegot_Type = Integer32
_AccSrPortX25pktNegot_Object = MibTableColumn
accSrPortX25pktNegot = _AccSrPortX25pktNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 5),
    _AccSrPortX25pktNegot_Type()
)
accSrPortX25pktNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25pktNegot.setStatus("mandatory")
_AccSrPortX25windowNegot_Type = Integer32
_AccSrPortX25windowNegot_Object = MibTableColumn
accSrPortX25windowNegot = _AccSrPortX25windowNegot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 6),
    _AccSrPortX25windowNegot_Type()
)
accSrPortX25windowNegot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25windowNegot.setStatus("mandatory")


class _AccSrPortX25FacIndex_Type(Integer32):
    """Custom type accSrPortX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccSrPortX25FacIndex_Type.__name__ = "Integer32"
_AccSrPortX25FacIndex_Object = MibTableColumn
accSrPortX25FacIndex = _AccSrPortX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 10, 1, 7),
    _AccSrPortX25FacIndex_Type()
)
accSrPortX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrPortX25FacIndex.setStatus("mandatory")
_AccSrStp_ObjectIdentity = ObjectIdentity
accSrStp = _AccSrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11)
)
_AccSrStpBridge_ObjectIdentity = ObjectIdentity
accSrStpBridge = _AccSrStpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1)
)


class _AccSrStpPriority_Type(Integer32):
    """Custom type accSrStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccSrStpPriority_Type.__name__ = "Integer32"
_AccSrStpPriority_Object = MibScalar
accSrStpPriority = _AccSrStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 1),
    _AccSrStpPriority_Type()
)
accSrStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpPriority.setStatus("mandatory")
_AccSrStpId_Type = OctetString
_AccSrStpId_Object = MibScalar
accSrStpId = _AccSrStpId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 2),
    _AccSrStpId_Type()
)
accSrStpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpId.setStatus("mandatory")
_AccSrStpBrAddr_Type = OctetString
_AccSrStpBrAddr_Object = MibScalar
accSrStpBrAddr = _AccSrStpBrAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 3),
    _AccSrStpBrAddr_Type()
)
accSrStpBrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpBrAddr.setStatus("mandatory")


class _AccSrStpMode_Type(Integer32):
    """Custom type accSrStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blue", 3),
          ("ieee", 1),
          ("manual", 2))
    )


_AccSrStpMode_Type.__name__ = "Integer32"
_AccSrStpMode_Object = MibScalar
accSrStpMode = _AccSrStpMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 4),
    _AccSrStpMode_Type()
)
accSrStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpMode.setStatus("mandatory")
_AccSrStpFilterTime_Type = TimeTicks
_AccSrStpFilterTime_Object = MibScalar
accSrStpFilterTime = _AccSrStpFilterTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 5),
    _AccSrStpFilterTime_Type()
)
accSrStpFilterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpFilterTime.setStatus("mandatory")
_AccSrStpMcastAddr_Type = OctetString
_AccSrStpMcastAddr_Object = MibScalar
accSrStpMcastAddr = _AccSrStpMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 6),
    _AccSrStpMcastAddr_Type()
)
accSrStpMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpMcastAddr.setStatus("mandatory")
_AccSrStpTopChangeDet_Type = Integer32
_AccSrStpTopChangeDet_Object = MibScalar
accSrStpTopChangeDet = _AccSrStpTopChangeDet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 7),
    _AccSrStpTopChangeDet_Type()
)
accSrStpTopChangeDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpTopChangeDet.setStatus("mandatory")
_AccSrStpTopChange_Type = Integer32
_AccSrStpTopChange_Object = MibScalar
accSrStpTopChange = _AccSrStpTopChange_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 8),
    _AccSrStpTopChange_Type()
)
accSrStpTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpTopChange.setStatus("mandatory")
_AccSrStpTopChangeTimer_Type = TimeTicks
_AccSrStpTopChangeTimer_Object = MibScalar
accSrStpTopChangeTimer = _AccSrStpTopChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 9),
    _AccSrStpTopChangeTimer_Type()
)
accSrStpTopChangeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpTopChangeTimer.setStatus("mandatory")
_AccSrStpDesRoot_Type = OctetString
_AccSrStpDesRoot_Object = MibScalar
accSrStpDesRoot = _AccSrStpDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 10),
    _AccSrStpDesRoot_Type()
)
accSrStpDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpDesRoot.setStatus("mandatory")
_AccSrStpRootPathCost_Type = Integer32
_AccSrStpRootPathCost_Object = MibScalar
accSrStpRootPathCost = _AccSrStpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 11),
    _AccSrStpRootPathCost_Type()
)
accSrStpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpRootPathCost.setStatus("mandatory")
_AccSrStpRootPort_Type = OctetString
_AccSrStpRootPort_Object = MibScalar
accSrStpRootPort = _AccSrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 12),
    _AccSrStpRootPort_Type()
)
accSrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpRootPort.setStatus("mandatory")


class _AccSrStpMaxAge_Type(Integer32):
    """Custom type accSrStpMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_AccSrStpMaxAge_Type.__name__ = "Integer32"
_AccSrStpMaxAge_Object = MibScalar
accSrStpMaxAge = _AccSrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 13),
    _AccSrStpMaxAge_Type()
)
accSrStpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpMaxAge.setStatus("mandatory")


class _AccSrStpHelloTime_Type(Integer32):
    """Custom type accSrStpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1800),
    )


_AccSrStpHelloTime_Type.__name__ = "Integer32"
_AccSrStpHelloTime_Object = MibScalar
accSrStpHelloTime = _AccSrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 14),
    _AccSrStpHelloTime_Type()
)
accSrStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpHelloTime.setStatus("mandatory")


class _AccSrStpForwardDelay_Type(Integer32):
    """Custom type accSrStpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AccSrStpForwardDelay_Type.__name__ = "Integer32"
_AccSrStpForwardDelay_Object = MibScalar
accSrStpForwardDelay = _AccSrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 15),
    _AccSrStpForwardDelay_Type()
)
accSrStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpForwardDelay.setStatus("mandatory")
_AccSrStpUpTime_Type = TimeTicks
_AccSrStpUpTime_Object = MibScalar
accSrStpUpTime = _AccSrStpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 16),
    _AccSrStpUpTime_Type()
)
accSrStpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpUpTime.setStatus("mandatory")
_AccSrStpTopChangeCnts_Type = Counter32
_AccSrStpTopChangeCnts_Object = MibScalar
accSrStpTopChangeCnts = _AccSrStpTopChangeCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 1, 17),
    _AccSrStpTopChangeCnts_Type()
)
accSrStpTopChangeCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpTopChangeCnts.setStatus("mandatory")
_AccSrStpPortParms_ObjectIdentity = ObjectIdentity
accSrStpPortParms = _AccSrStpPortParms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2)
)
_AccSrStpPortState_Type = Integer32
_AccSrStpPortState_Object = MibScalar
accSrStpPortState = _AccSrStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 1),
    _AccSrStpPortState_Type()
)
accSrStpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortState.setStatus("mandatory")


class _AccSrStpPortPathCost_Type(Integer32):
    """Custom type accSrStpPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccSrStpPortPathCost_Type.__name__ = "Integer32"
_AccSrStpPortPathCost_Object = MibScalar
accSrStpPortPathCost = _AccSrStpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 2),
    _AccSrStpPortPathCost_Type()
)
accSrStpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpPortPathCost.setStatus("mandatory")
_AccSrStpPortDesRoot_Type = OctetString
_AccSrStpPortDesRoot_Object = MibScalar
accSrStpPortDesRoot = _AccSrStpPortDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 3),
    _AccSrStpPortDesRoot_Type()
)
accSrStpPortDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortDesRoot.setStatus("mandatory")


class _AccSrStpPortDesCost_Type(Integer32):
    """Custom type accSrStpPortDesCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccSrStpPortDesCost_Type.__name__ = "Integer32"
_AccSrStpPortDesCost_Object = MibScalar
accSrStpPortDesCost = _AccSrStpPortDesCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 4),
    _AccSrStpPortDesCost_Type()
)
accSrStpPortDesCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortDesCost.setStatus("mandatory")
_AccSrStpPortDesBridge_Type = OctetString
_AccSrStpPortDesBridge_Object = MibScalar
accSrStpPortDesBridge = _AccSrStpPortDesBridge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 5),
    _AccSrStpPortDesBridge_Type()
)
accSrStpPortDesBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortDesBridge.setStatus("mandatory")
_AccSrStpPortDesPort_Type = OctetString
_AccSrStpPortDesPort_Object = MibScalar
accSrStpPortDesPort = _AccSrStpPortDesPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 6),
    _AccSrStpPortDesPort_Type()
)
accSrStpPortDesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortDesPort.setStatus("mandatory")


class _AccSrStpPortPriority_Type(Integer32):
    """Custom type accSrStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccSrStpPortPriority_Type.__name__ = "Integer32"
_AccSrStpPortPriority_Object = MibScalar
accSrStpPortPriority = _AccSrStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 7),
    _AccSrStpPortPriority_Type()
)
accSrStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpPortPriority.setStatus("mandatory")
_AccSrStpPortInPkts_Type = Counter32
_AccSrStpPortInPkts_Object = MibScalar
accSrStpPortInPkts = _AccSrStpPortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 8),
    _AccSrStpPortInPkts_Type()
)
accSrStpPortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortInPkts.setStatus("mandatory")
_AccSrStpPortOutPkts_Type = Counter32
_AccSrStpPortOutPkts_Object = MibScalar
accSrStpPortOutPkts = _AccSrStpPortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 9),
    _AccSrStpPortOutPkts_Type()
)
accSrStpPortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrStpPortOutPkts.setStatus("mandatory")


class _AccSrStpPortAdmin_Type(Integer32):
    """Custom type accSrStpPortAdmin based on Integer32"""
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


_AccSrStpPortAdmin_Type.__name__ = "Integer32"
_AccSrStpPortAdmin_Object = MibScalar
accSrStpPortAdmin = _AccSrStpPortAdmin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 11, 2, 10),
    _AccSrStpPortAdmin_Type()
)
accSrStpPortAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrStpPortAdmin.setStatus("mandatory")
_AccSrRingTable_Object = MibTable
accSrRingTable = _AccSrRingTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12)
)
if mibBuilder.loadTexts:
    accSrRingTable.setStatus("mandatory")
_AccSrRingEntry_Object = MibTableRow
accSrRingEntry = _AccSrRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1)
)
accSrRingEntry.setIndexNames(
    (0, "ACC-MIB", "accSrRingTblRingID"),
    (0, "ACC-MIB", "accSrRingTblBridgeID"),
)
if mibBuilder.loadTexts:
    accSrRingEntry.setStatus("mandatory")


class _AccSrRingTblRingID_Type(Integer32):
    """Custom type accSrRingTblRingID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AccSrRingTblRingID_Type.__name__ = "Integer32"
_AccSrRingTblRingID_Object = MibTableColumn
accSrRingTblRingID = _AccSrRingTblRingID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 1),
    _AccSrRingTblRingID_Type()
)
accSrRingTblRingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrRingTblRingID.setStatus("mandatory")


class _AccSrRingTblBridgeID_Type(Integer32):
    """Custom type accSrRingTblBridgeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AccSrRingTblBridgeID_Type.__name__ = "Integer32"
_AccSrRingTblBridgeID_Object = MibTableColumn
accSrRingTblBridgeID = _AccSrRingTblBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 2),
    _AccSrRingTblBridgeID_Type()
)
accSrRingTblBridgeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRingTblBridgeID.setStatus("mandatory")
_AccSrRingTblPortIndex_Type = Integer32
_AccSrRingTblPortIndex_Object = MibTableColumn
accSrRingTblPortIndex = _AccSrRingTblPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 3),
    _AccSrRingTblPortIndex_Type()
)
accSrRingTblPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRingTblPortIndex.setStatus("mandatory")
_AccSrRingTblMetric_Type = Integer32
_AccSrRingTblMetric_Object = MibTableColumn
accSrRingTblMetric = _AccSrRingTblMetric_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 4),
    _AccSrRingTblMetric_Type()
)
accSrRingTblMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRingTblMetric.setStatus("mandatory")
_AccSrRingTblAge_Type = Integer32
_AccSrRingTblAge_Object = MibTableColumn
accSrRingTblAge = _AccSrRingTblAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 5),
    _AccSrRingTblAge_Type()
)
accSrRingTblAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRingTblAge.setStatus("mandatory")
_AccSrRingTblNbrMacAddr_Type = OctetString
_AccSrRingTblNbrMacAddr_Object = MibTableColumn
accSrRingTblNbrMacAddr = _AccSrRingTblNbrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 12, 1, 6),
    _AccSrRingTblNbrMacAddr_Type()
)
accSrRingTblNbrMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrRingTblNbrMacAddr.setStatus("mandatory")
_AccSrFiltIITable_Object = MibTable
accSrFiltIITable = _AccSrFiltIITable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13)
)
if mibBuilder.loadTexts:
    accSrFiltIITable.setStatus("mandatory")
_AccSrFiltIIEntry_Object = MibTableRow
accSrFiltIIEntry = _AccSrFiltIIEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1)
)
accSrFiltIIEntry.setIndexNames(
    (0, "ACC-MIB", "accSrFiltIIEntDstMacAddr"),
    (0, "ACC-MIB", "accSrFiltIIEntDstMacAddrMask"),
    (0, "ACC-MIB", "accSrFiltIIEntSrcMacAddr"),
    (0, "ACC-MIB", "accSrFiltIIEntSrcMacAddrMask"),
    (0, "ACC-MIB", "accSrFiltIIEntPort"),
    (0, "ACC-MIB", "accSrFiltIIEntLogicalOp"),
    (0, "ACC-MIB", "accSrFiltIIEntProtocol"),
)
if mibBuilder.loadTexts:
    accSrFiltIIEntry.setStatus("mandatory")


class _AccSrFiltIIEntDstMacAddr_Type(OctetString):
    """Custom type accSrFiltIIEntDstMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccSrFiltIIEntDstMacAddr_Type.__name__ = "OctetString"
_AccSrFiltIIEntDstMacAddr_Object = MibTableColumn
accSrFiltIIEntDstMacAddr = _AccSrFiltIIEntDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 1),
    _AccSrFiltIIEntDstMacAddr_Type()
)
accSrFiltIIEntDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntDstMacAddr.setStatus("mandatory")


class _AccSrFiltIIEntSrcMacAddr_Type(OctetString):
    """Custom type accSrFiltIIEntSrcMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccSrFiltIIEntSrcMacAddr_Type.__name__ = "OctetString"
_AccSrFiltIIEntSrcMacAddr_Object = MibTableColumn
accSrFiltIIEntSrcMacAddr = _AccSrFiltIIEntSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 2),
    _AccSrFiltIIEntSrcMacAddr_Type()
)
accSrFiltIIEntSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntSrcMacAddr.setStatus("mandatory")


class _AccSrFiltIIEntDisp_Type(Integer32):
    """Custom type accSrFiltIIEntDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("forward", 1))
    )


_AccSrFiltIIEntDisp_Type.__name__ = "Integer32"
_AccSrFiltIIEntDisp_Object = MibTableColumn
accSrFiltIIEntDisp = _AccSrFiltIIEntDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 3),
    _AccSrFiltIIEntDisp_Type()
)
accSrFiltIIEntDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntDisp.setStatus("mandatory")
_AccSrFiltIIEntPort_Type = Integer32
_AccSrFiltIIEntPort_Object = MibTableColumn
accSrFiltIIEntPort = _AccSrFiltIIEntPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 4),
    _AccSrFiltIIEntPort_Type()
)
accSrFiltIIEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntPort.setStatus("mandatory")


class _AccSrFiltIIEntLogicalOp_Type(Integer32):
    """Custom type accSrFiltIIEntLogicalOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("equal", 2),
          ("notequal", 3))
    )


_AccSrFiltIIEntLogicalOp_Type.__name__ = "Integer32"
_AccSrFiltIIEntLogicalOp_Object = MibTableColumn
accSrFiltIIEntLogicalOp = _AccSrFiltIIEntLogicalOp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 5),
    _AccSrFiltIIEntLogicalOp_Type()
)
accSrFiltIIEntLogicalOp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntLogicalOp.setStatus("mandatory")


class _AccSrFiltIIEntProtocol_Type(OctetString):
    """Custom type accSrFiltIIEntProtocol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AccSrFiltIIEntProtocol_Type.__name__ = "OctetString"
_AccSrFiltIIEntProtocol_Object = MibTableColumn
accSrFiltIIEntProtocol = _AccSrFiltIIEntProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 6),
    _AccSrFiltIIEntProtocol_Type()
)
accSrFiltIIEntProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntProtocol.setStatus("mandatory")


class _AccSrFiltIIEntDstMacAddrMask_Type(OctetString):
    """Custom type accSrFiltIIEntDstMacAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccSrFiltIIEntDstMacAddrMask_Type.__name__ = "OctetString"
_AccSrFiltIIEntDstMacAddrMask_Object = MibTableColumn
accSrFiltIIEntDstMacAddrMask = _AccSrFiltIIEntDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 7),
    _AccSrFiltIIEntDstMacAddrMask_Type()
)
accSrFiltIIEntDstMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntDstMacAddrMask.setStatus("mandatory")


class _AccSrFiltIIEntSrcMacAddrMask_Type(OctetString):
    """Custom type accSrFiltIIEntSrcMacAddrMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_AccSrFiltIIEntSrcMacAddrMask_Type.__name__ = "OctetString"
_AccSrFiltIIEntSrcMacAddrMask_Object = MibTableColumn
accSrFiltIIEntSrcMacAddrMask = _AccSrFiltIIEntSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 13, 1, 8),
    _AccSrFiltIIEntSrcMacAddrMask_Type()
)
accSrFiltIIEntSrcMacAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSrFiltIIEntSrcMacAddrMask.setStatus("mandatory")
_AccSrFiltIIDiscards_Type = Integer32
_AccSrFiltIIDiscards_Object = MibScalar
accSrFiltIIDiscards = _AccSrFiltIIDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 14),
    _AccSrFiltIIDiscards_Type()
)
accSrFiltIIDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrFiltIIDiscards.setStatus("mandatory")
_AccSrFiltIIEntries_Type = Integer32
_AccSrFiltIIEntries_Object = MibScalar
accSrFiltIIEntries = _AccSrFiltIIEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 25, 15),
    _AccSrFiltIIEntries_Type()
)
accSrFiltIIEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSrFiltIIEntries.setStatus("mandatory")
_AccSMDS_ObjectIdentity = ObjectIdentity
accSMDS = _AccSMDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26)
)
_AccSmdsPortTable_Object = MibTable
accSmdsPortTable = _AccSmdsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1)
)
if mibBuilder.loadTexts:
    accSmdsPortTable.setStatus("mandatory")
_AccSmdsPortEntry_Object = MibTableRow
accSmdsPortEntry = _AccSmdsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1)
)
accSmdsPortEntry.setIndexNames(
    (0, "ACC-MIB", "accSmdsPortIndex"),
)
if mibBuilder.loadTexts:
    accSmdsPortEntry.setStatus("mandatory")


class _AccSmdsPortIndex_Type(Integer32):
    """Custom type accSmdsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccSmdsPortIndex_Type.__name__ = "Integer32"
_AccSmdsPortIndex_Object = MibTableColumn
accSmdsPortIndex = _AccSmdsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1, 1),
    _AccSmdsPortIndex_Type()
)
accSmdsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSmdsPortIndex.setStatus("mandatory")
_AccSmdsPortIA_Type = SmdsAddress
_AccSmdsPortIA_Object = MibTableColumn
accSmdsPortIA = _AccSmdsPortIA_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 1, 1, 2),
    _AccSmdsPortIA_Type()
)
accSmdsPortIA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSmdsPortIA.setStatus("mandatory")
_AccSipL3Table_Object = MibTable
accSipL3Table = _AccSipL3Table_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2)
)
if mibBuilder.loadTexts:
    accSipL3Table.setStatus("mandatory")
_AccSipL3Entry_Object = MibTableRow
accSipL3Entry = _AccSipL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1)
)
accSipL3Entry.setIndexNames(
    (0, "ACC-MIB", "accSipL3Index"),
)
if mibBuilder.loadTexts:
    accSipL3Entry.setStatus("mandatory")


class _AccSipL3Index_Type(Integer32):
    """Custom type accSipL3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccSipL3Index_Type.__name__ = "Integer32"
_AccSipL3Index_Object = MibTableColumn
accSipL3Index = _AccSipL3Index_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 1),
    _AccSipL3Index_Type()
)
accSipL3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3Index.setStatus("mandatory")
_AccSipL3RcvIAs_Type = Counter32
_AccSipL3RcvIAs_Object = MibTableColumn
accSipL3RcvIAs = _AccSipL3RcvIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 2),
    _AccSipL3RcvIAs_Type()
)
accSipL3RcvIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3RcvIAs.setStatus("mandatory")
_AccSipL3RcvGAs_Type = Counter32
_AccSipL3RcvGAs_Object = MibTableColumn
accSipL3RcvGAs = _AccSipL3RcvGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 3),
    _AccSipL3RcvGAs_Type()
)
accSipL3RcvGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3RcvGAs.setStatus("mandatory")
_AccSipL3UnkIAs_Type = Counter32
_AccSipL3UnkIAs_Object = MibTableColumn
accSipL3UnkIAs = _AccSipL3UnkIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 4),
    _AccSipL3UnkIAs_Type()
)
accSipL3UnkIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3UnkIAs.setStatus("mandatory")
_AccSipL3UnkGAs_Type = Counter32
_AccSipL3UnkGAs_Object = MibTableColumn
accSipL3UnkGAs = _AccSipL3UnkGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 5),
    _AccSipL3UnkGAs_Type()
)
accSipL3UnkGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3UnkGAs.setStatus("mandatory")
_AccSipL3SndIAs_Type = Counter32
_AccSipL3SndIAs_Object = MibTableColumn
accSipL3SndIAs = _AccSipL3SndIAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 6),
    _AccSipL3SndIAs_Type()
)
accSipL3SndIAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3SndIAs.setStatus("mandatory")
_AccSipL3SndGAs_Type = Counter32
_AccSipL3SndGAs_Object = MibTableColumn
accSipL3SndGAs = _AccSipL3SndGAs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 7),
    _AccSipL3SndGAs_Type()
)
accSipL3SndGAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3SndGAs.setStatus("mandatory")
_AccSipL3Errors_Type = Counter32
_AccSipL3Errors_Object = MibTableColumn
accSipL3Errors = _AccSipL3Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 8),
    _AccSipL3Errors_Type()
)
accSipL3Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3Errors.setStatus("mandatory")
_AccSipL3InvAddrs_Type = Counter32
_AccSipL3InvAddrs_Object = MibTableColumn
accSipL3InvAddrs = _AccSipL3InvAddrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 26, 2, 1, 9),
    _AccSipL3InvAddrs_Type()
)
accSipL3InvAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSipL3InvAddrs.setStatus("mandatory")
_AccRload_ObjectIdentity = ObjectIdentity
accRload = _AccRload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27)
)
_AccRlSourceTable_Object = MibTable
accRlSourceTable = _AccRlSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1)
)
if mibBuilder.loadTexts:
    accRlSourceTable.setStatus("mandatory")
_AccRlSourceEntry_Object = MibTableRow
accRlSourceEntry = _AccRlSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1)
)
accRlSourceEntry.setIndexNames(
    (0, "ACC-MIB", "accRlPriority"),
)
if mibBuilder.loadTexts:
    accRlSourceEntry.setStatus("mandatory")
_AccRlHostAddr_Type = IpAddress
_AccRlHostAddr_Object = MibTableColumn
accRlHostAddr = _AccRlHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 1),
    _AccRlHostAddr_Type()
)
accRlHostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlHostAddr.setStatus("mandatory")
_AccRlFilename_Type = DisplayString
_AccRlFilename_Object = MibTableColumn
accRlFilename = _AccRlFilename_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 2),
    _AccRlFilename_Type()
)
accRlFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlFilename.setStatus("mandatory")
_AccRlPriority_Type = Integer32
_AccRlPriority_Object = MibTableColumn
accRlPriority = _AccRlPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 1, 1, 3),
    _AccRlPriority_Type()
)
accRlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accRlPriority.setStatus("mandatory")


class _AccNetload_Type(Integer32):
    """Custom type accNetload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccNetload_Type.__name__ = "Integer32"
_AccNetload_Object = MibScalar
accNetload = _AccNetload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 2),
    _AccNetload_Type()
)
accNetload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accNetload.setStatus("mandatory")


class _AccDownload_Type(Integer32):
    """Custom type accDownload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccDownload_Type.__name__ = "Integer32"
_AccDownload_Object = MibScalar
accDownload = _AccDownload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 3),
    _AccDownload_Type()
)
accDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDownload.setStatus("mandatory")


class _AccPromload_Type(Integer32):
    """Custom type accPromload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("other", 2))
    )


_AccPromload_Type.__name__ = "Integer32"
_AccPromload_Object = MibScalar
accPromload = _AccPromload_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 4),
    _AccPromload_Type()
)
accPromload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPromload.setStatus("mandatory")
_AccCfgLoad_ObjectIdentity = ObjectIdentity
accCfgLoad = _AccCfgLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5)
)
_AccCfgHost_Type = IpAddress
_AccCfgHost_Object = MibScalar
accCfgHost = _AccCfgHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 1),
    _AccCfgHost_Type()
)
accCfgHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgHost.setStatus("mandatory")
_AccCfgFile_Type = DisplayString
_AccCfgFile_Object = MibScalar
accCfgFile = _AccCfgFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 2),
    _AccCfgFile_Type()
)
accCfgFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgFile.setStatus("mandatory")


class _AccCfgDisp_Type(Integer32):
    """Custom type accCfgDisp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("execute", 3),
          ("reload", 2),
          ("reset", 1))
    )


_AccCfgDisp_Type.__name__ = "Integer32"
_AccCfgDisp_Object = MibScalar
accCfgDisp = _AccCfgDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 5, 3),
    _AccCfgDisp_Type()
)
accCfgDisp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCfgDisp.setStatus("mandatory")
_AccTftpStat_ObjectIdentity = ObjectIdentity
accTftpStat = _AccTftpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6)
)


class _AccTftpStatus_Type(Integer32):
    """Custom type accTftpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("downloading", 2),
          ("idle", 3),
          ("uploading", 1))
    )


_AccTftpStatus_Type.__name__ = "Integer32"
_AccTftpStatus_Object = MibScalar
accTftpStatus = _AccTftpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 1),
    _AccTftpStatus_Type()
)
accTftpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpStatus.setStatus("mandatory")
_AccTftpLocalFile_Type = DisplayString
_AccTftpLocalFile_Object = MibScalar
accTftpLocalFile = _AccTftpLocalFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 2),
    _AccTftpLocalFile_Type()
)
accTftpLocalFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpLocalFile.setStatus("mandatory")
_AccTftpRemoteFile_Type = DisplayString
_AccTftpRemoteFile_Object = MibScalar
accTftpRemoteFile = _AccTftpRemoteFile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 3),
    _AccTftpRemoteFile_Type()
)
accTftpRemoteFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpRemoteFile.setStatus("mandatory")
_AccTftpOctetsTransferred_Type = Integer32
_AccTftpOctetsTransferred_Object = MibScalar
accTftpOctetsTransferred = _AccTftpOctetsTransferred_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 4),
    _AccTftpOctetsTransferred_Type()
)
accTftpOctetsTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpOctetsTransferred.setStatus("mandatory")
_AccTftpLastMsg_Type = DisplayString
_AccTftpLastMsg_Object = MibScalar
accTftpLastMsg = _AccTftpLastMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 6, 5),
    _AccTftpLastMsg_Type()
)
accTftpLastMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpLastMsg.setStatus("mandatory")
_AccTftpCmd_ObjectIdentity = ObjectIdentity
accTftpCmd = _AccTftpCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7)
)


class _AccTftpCmdReq_Type(Integer32):
    """Custom type accTftpCmdReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("get", 1)
    )


_AccTftpCmdReq_Type.__name__ = "Integer32"
_AccTftpCmdReq_Object = MibScalar
accTftpCmdReq = _AccTftpCmdReq_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 1),
    _AccTftpCmdReq_Type()
)
accTftpCmdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdReq.setStatus("mandatory")
_AccTftpCmdHost_Type = IpAddress
_AccTftpCmdHost_Object = MibScalar
accTftpCmdHost = _AccTftpCmdHost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 2),
    _AccTftpCmdHost_Type()
)
accTftpCmdHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdHost.setStatus("mandatory")
_AccTftpCmdRemote_Type = DisplayString
_AccTftpCmdRemote_Object = MibScalar
accTftpCmdRemote = _AccTftpCmdRemote_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 3),
    _AccTftpCmdRemote_Type()
)
accTftpCmdRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdRemote.setStatus("mandatory")
_AccTftpCmdLocal_Type = DisplayString
_AccTftpCmdLocal_Object = MibScalar
accTftpCmdLocal = _AccTftpCmdLocal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 27, 7, 4),
    _AccTftpCmdLocal_Type()
)
accTftpCmdLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accTftpCmdLocal.setStatus("mandatory")
_AccAt_ObjectIdentity = ObjectIdentity
accAt = _AccAt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28)
)
_AccAtNode_ObjectIdentity = ObjectIdentity
accAtNode = _AccAtNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1)
)


class _AccAtNodeAdState_Type(Integer32):
    """Custom type accAtNodeAdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 1))
    )


_AccAtNodeAdState_Type.__name__ = "Integer32"
_AccAtNodeAdState_Object = MibScalar
accAtNodeAdState = _AccAtNodeAdState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 1),
    _AccAtNodeAdState_Type()
)
accAtNodeAdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeAdState.setStatus("mandatory")


class _AccAtNodeChecksum_Type(Integer32):
    """Custom type accAtNodeChecksum based on Integer32"""
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


_AccAtNodeChecksum_Type.__name__ = "Integer32"
_AccAtNodeChecksum_Object = MibScalar
accAtNodeChecksum = _AccAtNodeChecksum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 2),
    _AccAtNodeChecksum_Type()
)
accAtNodeChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeChecksum.setStatus("mandatory")
_AccAtNodeAarpExpire_Type = TimeTicks
_AccAtNodeAarpExpire_Object = MibScalar
accAtNodeAarpExpire = _AccAtNodeAarpExpire_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 1, 3),
    _AccAtNodeAarpExpire_Type()
)
accAtNodeAarpExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNodeAarpExpire.setStatus("mandatory")
_AccAtAarpTable_Object = MibTable
accAtAarpTable = _AccAtAarpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2)
)
if mibBuilder.loadTexts:
    accAtAarpTable.setStatus("mandatory")
_AccAtAarpEntry_Object = MibTableRow
accAtAarpEntry = _AccAtAarpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1)
)
accAtAarpEntry.setIndexNames(
    (0, "ACC-MIB", "accAtAarpTabPort"),
    (0, "ACC-MIB", "accAtAarpTabNetAddr"),
)
if mibBuilder.loadTexts:
    accAtAarpEntry.setStatus("mandatory")


class _AccAtAarpTabPort_Type(Integer32):
    """Custom type accAtAarpTabPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtAarpTabPort_Type.__name__ = "Integer32"
_AccAtAarpTabPort_Object = MibTableColumn
accAtAarpTabPort = _AccAtAarpTabPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 1),
    _AccAtAarpTabPort_Type()
)
accAtAarpTabPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabPort.setStatus("mandatory")
_AccAtAarpTabMacAddr_Type = OctetString
_AccAtAarpTabMacAddr_Object = MibTableColumn
accAtAarpTabMacAddr = _AccAtAarpTabMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 2),
    _AccAtAarpTabMacAddr_Type()
)
accAtAarpTabMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabMacAddr.setStatus("mandatory")
_AccAtAarpTabNetAddr_Type = OctetString
_AccAtAarpTabNetAddr_Object = MibTableColumn
accAtAarpTabNetAddr = _AccAtAarpTabNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 3),
    _AccAtAarpTabNetAddr_Type()
)
accAtAarpTabNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabNetAddr.setStatus("mandatory")


class _AccAtAarpTabStatus_Type(Integer32):
    """Custom type accAtAarpTabStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("pending", 3),
          ("static", 2))
    )


_AccAtAarpTabStatus_Type.__name__ = "Integer32"
_AccAtAarpTabStatus_Object = MibTableColumn
accAtAarpTabStatus = _AccAtAarpTabStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 2, 1, 4),
    _AccAtAarpTabStatus_Type()
)
accAtAarpTabStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpTabStatus.setStatus("mandatory")
_AccAtAarpStatsTable_Object = MibTable
accAtAarpStatsTable = _AccAtAarpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3)
)
if mibBuilder.loadTexts:
    accAtAarpStatsTable.setStatus("mandatory")
_AccAtAarpStatsEntry_Object = MibTableRow
accAtAarpStatsEntry = _AccAtAarpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1)
)
accAtAarpStatsEntry.setIndexNames(
    (0, "ACC-MIB", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtAarpStatsEntry.setStatus("mandatory")
_AccAtAarpStatsInRequests_Type = Counter32
_AccAtAarpStatsInRequests_Object = MibTableColumn
accAtAarpStatsInRequests = _AccAtAarpStatsInRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 1),
    _AccAtAarpStatsInRequests_Type()
)
accAtAarpStatsInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInRequests.setStatus("mandatory")
_AccAtAarpStatsInResponses_Type = Counter32
_AccAtAarpStatsInResponses_Object = MibTableColumn
accAtAarpStatsInResponses = _AccAtAarpStatsInResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 2),
    _AccAtAarpStatsInResponses_Type()
)
accAtAarpStatsInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInResponses.setStatus("mandatory")
_AccAtAarpStatsInProbes_Type = Counter32
_AccAtAarpStatsInProbes_Object = MibTableColumn
accAtAarpStatsInProbes = _AccAtAarpStatsInProbes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 3),
    _AccAtAarpStatsInProbes_Type()
)
accAtAarpStatsInProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInProbes.setStatus("mandatory")
_AccAtAarpStatsOutRequests_Type = Counter32
_AccAtAarpStatsOutRequests_Object = MibTableColumn
accAtAarpStatsOutRequests = _AccAtAarpStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 4),
    _AccAtAarpStatsOutRequests_Type()
)
accAtAarpStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutRequests.setStatus("mandatory")
_AccAtAarpStatsOutResponses_Type = Counter32
_AccAtAarpStatsOutResponses_Object = MibTableColumn
accAtAarpStatsOutResponses = _AccAtAarpStatsOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 5),
    _AccAtAarpStatsOutResponses_Type()
)
accAtAarpStatsOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutResponses.setStatus("mandatory")
_AccAtAarpStatsOutProbes_Type = Counter32
_AccAtAarpStatsOutProbes_Object = MibTableColumn
accAtAarpStatsOutProbes = _AccAtAarpStatsOutProbes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 6),
    _AccAtAarpStatsOutProbes_Type()
)
accAtAarpStatsOutProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutProbes.setStatus("mandatory")
_AccAtAarpStatsNoReplys_Type = Counter32
_AccAtAarpStatsNoReplys_Object = MibTableColumn
accAtAarpStatsNoReplys = _AccAtAarpStatsNoReplys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 7),
    _AccAtAarpStatsNoReplys_Type()
)
accAtAarpStatsNoReplys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsNoReplys.setStatus("mandatory")
_AccAtAarpStatsExpires_Type = Counter32
_AccAtAarpStatsExpires_Object = MibTableColumn
accAtAarpStatsExpires = _AccAtAarpStatsExpires_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 8),
    _AccAtAarpStatsExpires_Type()
)
accAtAarpStatsExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsExpires.setStatus("mandatory")
_AccAtAarpStatsDiscards_Type = Counter32
_AccAtAarpStatsDiscards_Object = MibTableColumn
accAtAarpStatsDiscards = _AccAtAarpStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 9),
    _AccAtAarpStatsDiscards_Type()
)
accAtAarpStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsDiscards.setStatus("mandatory")
_AccAtAarpStatsInErrors_Type = Counter32
_AccAtAarpStatsInErrors_Object = MibTableColumn
accAtAarpStatsInErrors = _AccAtAarpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 10),
    _AccAtAarpStatsInErrors_Type()
)
accAtAarpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsInErrors.setStatus("mandatory")
_AccAtAarpStatsOutErrors_Type = Counter32
_AccAtAarpStatsOutErrors_Object = MibTableColumn
accAtAarpStatsOutErrors = _AccAtAarpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 3, 1, 11),
    _AccAtAarpStatsOutErrors_Type()
)
accAtAarpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAarpStatsOutErrors.setStatus("mandatory")
_AccAtAdbStats_ObjectIdentity = ObjectIdentity
accAtAdbStats = _AccAtAdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4)
)
_AccAtAdbStatsCacheds_Type = Counter32
_AccAtAdbStatsCacheds_Object = MibScalar
accAtAdbStatsCacheds = _AccAtAdbStatsCacheds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 1),
    _AccAtAdbStatsCacheds_Type()
)
accAtAdbStatsCacheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsCacheds.setStatus("mandatory")
_AccAtAdbStatsRotates_Type = Counter32
_AccAtAdbStatsRotates_Object = MibScalar
accAtAdbStatsRotates = _AccAtAdbStatsRotates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 2),
    _AccAtAdbStatsRotates_Type()
)
accAtAdbStatsRotates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsRotates.setStatus("mandatory")
_AccAtAdbStatsNoEntries_Type = Counter32
_AccAtAdbStatsNoEntries_Object = MibScalar
accAtAdbStatsNoEntries = _AccAtAdbStatsNoEntries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 3),
    _AccAtAdbStatsNoEntries_Type()
)
accAtAdbStatsNoEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsNoEntries.setStatus("mandatory")
_AccAtAdbStatsAdds_Type = Counter32
_AccAtAdbStatsAdds_Object = MibScalar
accAtAdbStatsAdds = _AccAtAdbStatsAdds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 4),
    _AccAtAdbStatsAdds_Type()
)
accAtAdbStatsAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsAdds.setStatus("mandatory")
_AccAtAdbStatsUpdates_Type = Counter32
_AccAtAdbStatsUpdates_Object = MibScalar
accAtAdbStatsUpdates = _AccAtAdbStatsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 5),
    _AccAtAdbStatsUpdates_Type()
)
accAtAdbStatsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsUpdates.setStatus("mandatory")
_AccAtAdbStatsDeletes_Type = Counter32
_AccAtAdbStatsDeletes_Object = MibScalar
accAtAdbStatsDeletes = _AccAtAdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 6),
    _AccAtAdbStatsDeletes_Type()
)
accAtAdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsDeletes.setStatus("mandatory")
_AccAtAdbStatsTrims_Type = Counter32
_AccAtAdbStatsTrims_Object = MibScalar
accAtAdbStatsTrims = _AccAtAdbStatsTrims_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 7),
    _AccAtAdbStatsTrims_Type()
)
accAtAdbStatsTrims.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsTrims.setStatus("mandatory")
_AccAtAdbStatsDiscards_Type = Counter32
_AccAtAdbStatsDiscards_Object = MibScalar
accAtAdbStatsDiscards = _AccAtAdbStatsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 4, 8),
    _AccAtAdbStatsDiscards_Type()
)
accAtAdbStatsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAdbStatsDiscards.setStatus("mandatory")
_AccAtDdpStats_ObjectIdentity = ObjectIdentity
accAtDdpStats = _AccAtDdpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5)
)
_AccAtDdpStatsNoOutRoutes_Type = Counter32
_AccAtDdpStatsNoOutRoutes_Object = MibScalar
accAtDdpStatsNoOutRoutes = _AccAtDdpStatsNoOutRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 1),
    _AccAtDdpStatsNoOutRoutes_Type()
)
accAtDdpStatsNoOutRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsNoOutRoutes.setStatus("mandatory")
_AccAtDdpStatsInErrors_Type = Counter32
_AccAtDdpStatsInErrors_Object = MibScalar
accAtDdpStatsInErrors = _AccAtDdpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 2),
    _AccAtDdpStatsInErrors_Type()
)
accAtDdpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsInErrors.setStatus("mandatory")
_AccAtDdpStatsOutErrors_Type = Counter32
_AccAtDdpStatsOutErrors_Object = MibScalar
accAtDdpStatsOutErrors = _AccAtDdpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 5, 3),
    _AccAtDdpStatsOutErrors_Type()
)
accAtDdpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtDdpStatsOutErrors.setStatus("mandatory")
_AccAtNetTable_Object = MibTable
accAtNetTable = _AccAtNetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6)
)
if mibBuilder.loadTexts:
    accAtNetTable.setStatus("mandatory")
_AccAtNetEntry_Object = MibTableRow
accAtNetEntry = _AccAtNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1)
)
accAtNetEntry.setIndexNames(
    (0, "RFC1243-MIB", "atportIndex"),
)
if mibBuilder.loadTexts:
    accAtNetEntry.setStatus("mandatory")


class _AccAtNetTabProtocol_Type(Integer32):
    """Custom type accAtNetTabProtocol based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("dial", 11),
          ("ethertalk1", 1),
          ("ethertalk2", 2),
          ("fddi", 8),
          ("framerelay", 6),
          ("lapb", 4),
          ("multilinkgroup", 12),
          ("ppp", 7),
          ("tokentalk", 3),
          ("x25", 5))
    )


_AccAtNetTabProtocol_Type.__name__ = "Integer32"
_AccAtNetTabProtocol_Object = MibTableColumn
accAtNetTabProtocol = _AccAtNetTabProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 1),
    _AccAtNetTabProtocol_Type()
)
accAtNetTabProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabProtocol.setStatus("mandatory")


class _AccAtNetTabRtmpIncr_Type(Integer32):
    """Custom type accAtNetTabRtmpIncr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AccAtNetTabRtmpIncr_Type.__name__ = "Integer32"
_AccAtNetTabRtmpIncr_Object = MibTableColumn
accAtNetTabRtmpIncr = _AccAtNetTabRtmpIncr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 2),
    _AccAtNetTabRtmpIncr_Type()
)
accAtNetTabRtmpIncr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabRtmpIncr.setStatus("mandatory")


class _AccAtNetTabRtmpSend_Type(TimeTicks):
    """Custom type accAtNetTabRtmpSend based on TimeTicks"""
    defaultValue = 1000


_AccAtNetTabRtmpSend_Object = MibTableColumn
accAtNetTabRtmpSend = _AccAtNetTabRtmpSend_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 3),
    _AccAtNetTabRtmpSend_Type()
)
accAtNetTabRtmpSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabRtmpSend.setStatus("mandatory")
_AccAtNetTabX25Addr1_Type = OctetString
_AccAtNetTabX25Addr1_Object = MibTableColumn
accAtNetTabX25Addr1 = _AccAtNetTabX25Addr1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 4),
    _AccAtNetTabX25Addr1_Type()
)
accAtNetTabX25Addr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Addr1.setStatus("mandatory")
_AccAtNetTabX25Addr2_Type = OctetString
_AccAtNetTabX25Addr2_Object = MibTableColumn
accAtNetTabX25Addr2 = _AccAtNetTabX25Addr2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 5),
    _AccAtNetTabX25Addr2_Type()
)
accAtNetTabX25Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Addr2.setStatus("mandatory")


class _AccAtNetTabX25Idle_Type(TimeTicks):
    """Custom type accAtNetTabX25Idle based on TimeTicks"""
    defaultValue = 30000


_AccAtNetTabX25Idle_Object = MibTableColumn
accAtNetTabX25Idle = _AccAtNetTabX25Idle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 6),
    _AccAtNetTabX25Idle_Type()
)
accAtNetTabX25Idle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25Idle.setStatus("mandatory")


class _AccAtNetTabX25PktSize_Type(Integer32):
    """Custom type accAtNetTabX25PktSize based on Integer32"""
    defaultValue = 0


_AccAtNetTabX25PktSize_Object = MibTableColumn
accAtNetTabX25PktSize = _AccAtNetTabX25PktSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 7),
    _AccAtNetTabX25PktSize_Type()
)
accAtNetTabX25PktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25PktSize.setStatus("mandatory")


class _AccAtNetTabX25WinSize_Type(Integer32):
    """Custom type accAtNetTabX25WinSize based on Integer32"""
    defaultValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AccAtNetTabX25WinSize_Type.__name__ = "Integer32"
_AccAtNetTabX25WinSize_Object = MibTableColumn
accAtNetTabX25WinSize = _AccAtNetTabX25WinSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 8),
    _AccAtNetTabX25WinSize_Type()
)
accAtNetTabX25WinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25WinSize.setStatus("mandatory")


class _AccAtNetTabX25FacIndex_Type(Integer32):
    """Custom type accAtNetTabX25FacIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtNetTabX25FacIndex_Type.__name__ = "Integer32"
_AccAtNetTabX25FacIndex_Object = MibTableColumn
accAtNetTabX25FacIndex = _AccAtNetTabX25FacIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 6, 1, 9),
    _AccAtNetTabX25FacIndex_Type()
)
accAtNetTabX25FacIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtNetTabX25FacIndex.setStatus("mandatory")
_AccAtPortTable_Object = MibTable
accAtPortTable = _AccAtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7)
)
if mibBuilder.loadTexts:
    accAtPortTable.setStatus("mandatory")
_AccAtPortEntry_Object = MibTableRow
accAtPortEntry = _AccAtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1)
)
accAtPortEntry.setIndexNames(
    (0, "ACC-MIB", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtPortEntry.setStatus("mandatory")


class _AccAtPortTabIndex_Type(Integer32):
    """Custom type accAtPortTabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtPortTabIndex_Type.__name__ = "Integer32"
_AccAtPortTabIndex_Object = MibTableColumn
accAtPortTabIndex = _AccAtPortTabIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 1),
    _AccAtPortTabIndex_Type()
)
accAtPortTabIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabIndex.setStatus("mandatory")
_AccAtPortTabNetAddr_Type = OctetString
_AccAtPortTabNetAddr_Object = MibTableColumn
accAtPortTabNetAddr = _AccAtPortTabNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 2),
    _AccAtPortTabNetAddr_Type()
)
accAtPortTabNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabNetAddr.setStatus("mandatory")


class _AccAtPortTabState_Type(Integer32):
    """Custom type accAtPortTabState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("error", 11),
          ("probe1", 3),
          ("probe2", 6),
          ("query", 7),
          ("ready", 8),
          ("start1", 2),
          ("start2", 4),
          ("stop1", 10),
          ("stop2", 9),
          ("up", 5))
    )


_AccAtPortTabState_Type.__name__ = "Integer32"
_AccAtPortTabState_Object = MibTableColumn
accAtPortTabState = _AccAtPortTabState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 3),
    _AccAtPortTabState_Type()
)
accAtPortTabState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabState.setStatus("mandatory")
_AccAtPortTabDescr_Type = DisplayString
_AccAtPortTabDescr_Object = MibTableColumn
accAtPortTabDescr = _AccAtPortTabDescr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 4),
    _AccAtPortTabDescr_Type()
)
accAtPortTabDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabDescr.setStatus("mandatory")
_AccAtPortTabErrCode_Type = Integer32
_AccAtPortTabErrCode_Object = MibTableColumn
accAtPortTabErrCode = _AccAtPortTabErrCode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 5),
    _AccAtPortTabErrCode_Type()
)
accAtPortTabErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrCode.setStatus("mandatory")
_AccAtPortTabErrTime_Type = TimeTicks
_AccAtPortTabErrTime_Object = MibTableColumn
accAtPortTabErrTime = _AccAtPortTabErrTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 6),
    _AccAtPortTabErrTime_Type()
)
accAtPortTabErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrTime.setStatus("mandatory")
_AccAtPortTabErrAddr_Type = OctetString
_AccAtPortTabErrAddr_Object = MibTableColumn
accAtPortTabErrAddr = _AccAtPortTabErrAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 7),
    _AccAtPortTabErrAddr_Type()
)
accAtPortTabErrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrAddr.setStatus("mandatory")
_AccAtPortTabErrDescr_Type = DisplayString
_AccAtPortTabErrDescr_Object = MibTableColumn
accAtPortTabErrDescr = _AccAtPortTabErrDescr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 8),
    _AccAtPortTabErrDescr_Type()
)
accAtPortTabErrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrDescr.setStatus("mandatory")
_AccAtPortTabErrCount_Type = Integer32
_AccAtPortTabErrCount_Object = MibTableColumn
accAtPortTabErrCount = _AccAtPortTabErrCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 7, 1, 9),
    _AccAtPortTabErrCount_Type()
)
accAtPortTabErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortTabErrCount.setStatus("mandatory")
_AccAtPortStatsTable_Object = MibTable
accAtPortStatsTable = _AccAtPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8)
)
if mibBuilder.loadTexts:
    accAtPortStatsTable.setStatus("mandatory")
_AccAtPortStatsEntry_Object = MibTableRow
accAtPortStatsEntry = _AccAtPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1)
)
accAtPortStatsEntry.setIndexNames(
    (0, "ACC-MIB", "accAtPortTabIndex"),
)
if mibBuilder.loadTexts:
    accAtPortStatsEntry.setStatus("mandatory")
_AccAtPortStatsInTotals_Type = Counter32
_AccAtPortStatsInTotals_Object = MibTableColumn
accAtPortStatsInTotals = _AccAtPortStatsInTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 1),
    _AccAtPortStatsInTotals_Type()
)
accAtPortStatsInTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInTotals.setStatus("mandatory")
_AccAtPortStatsInShorts_Type = Counter32
_AccAtPortStatsInShorts_Object = MibTableColumn
accAtPortStatsInShorts = _AccAtPortStatsInShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 2),
    _AccAtPortStatsInShorts_Type()
)
accAtPortStatsInShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInShorts.setStatus("mandatory")
_AccAtPortStatsNotForMes_Type = Counter32
_AccAtPortStatsNotForMes_Object = MibTableColumn
accAtPortStatsNotForMes = _AccAtPortStatsNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 3),
    _AccAtPortStatsNotForMes_Type()
)
accAtPortStatsNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNotForMes.setStatus("mandatory")
_AccAtPortStatsTooShorts_Type = Counter32
_AccAtPortStatsTooShorts_Object = MibTableColumn
accAtPortStatsTooShorts = _AccAtPortStatsTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 4),
    _AccAtPortStatsTooShorts_Type()
)
accAtPortStatsTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsTooShorts.setStatus("mandatory")
_AccAtPortStatsTooLongs_Type = Counter32
_AccAtPortStatsTooLongs_Object = MibTableColumn
accAtPortStatsTooLongs = _AccAtPortStatsTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 5),
    _AccAtPortStatsTooLongs_Type()
)
accAtPortStatsTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsTooLongs.setStatus("mandatory")
_AccAtPortStatsChksums_Type = Counter32
_AccAtPortStatsChksums_Object = MibTableColumn
accAtPortStatsChksums = _AccAtPortStatsChksums_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 6),
    _AccAtPortStatsChksums_Type()
)
accAtPortStatsChksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsChksums.setStatus("mandatory")
_AccAtPortStatsNotMyNets_Type = Counter32
_AccAtPortStatsNotMyNets_Object = MibTableColumn
accAtPortStatsNotMyNets = _AccAtPortStatsNotMyNets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 7),
    _AccAtPortStatsNotMyNets_Type()
)
accAtPortStatsNotMyNets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNotMyNets.setStatus("mandatory")
_AccAtPortStatsInFwdReqs_Type = Counter32
_AccAtPortStatsInFwdReqs_Object = MibTableColumn
accAtPortStatsInFwdReqs = _AccAtPortStatsInFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 8),
    _AccAtPortStatsInFwdReqs_Type()
)
accAtPortStatsInFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInFwdReqs.setStatus("mandatory")
_AccAtPortStatsFwdBcasts_Type = Counter32
_AccAtPortStatsFwdBcasts_Object = MibTableColumn
accAtPortStatsFwdBcasts = _AccAtPortStatsFwdBcasts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 9),
    _AccAtPortStatsFwdBcasts_Type()
)
accAtPortStatsFwdBcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsFwdBcasts.setStatus("mandatory")
_AccAtPortStatsNoFwdRoutes_Type = Counter32
_AccAtPortStatsNoFwdRoutes_Object = MibTableColumn
accAtPortStatsNoFwdRoutes = _AccAtPortStatsNoFwdRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 10),
    _AccAtPortStatsNoFwdRoutes_Type()
)
accAtPortStatsNoFwdRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsNoFwdRoutes.setStatus("mandatory")
_AccAtPortStatsHopCounts_Type = Counter32
_AccAtPortStatsHopCounts_Object = MibTableColumn
accAtPortStatsHopCounts = _AccAtPortStatsHopCounts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 11),
    _AccAtPortStatsHopCounts_Type()
)
accAtPortStatsHopCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsHopCounts.setStatus("mandatory")
_AccAtPortStatsReflects_Type = Counter32
_AccAtPortStatsReflects_Object = MibTableColumn
accAtPortStatsReflects = _AccAtPortStatsReflects_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 12),
    _AccAtPortStatsReflects_Type()
)
accAtPortStatsReflects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsReflects.setStatus("mandatory")
_AccAtPortStatsOutTotals_Type = Counter32
_AccAtPortStatsOutTotals_Object = MibTableColumn
accAtPortStatsOutTotals = _AccAtPortStatsOutTotals_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 13),
    _AccAtPortStatsOutTotals_Type()
)
accAtPortStatsOutTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutTotals.setStatus("mandatory")
_AccAtPortStatsOutShorts_Type = Counter32
_AccAtPortStatsOutShorts_Object = MibTableColumn
accAtPortStatsOutShorts = _AccAtPortStatsOutShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 14),
    _AccAtPortStatsOutShorts_Type()
)
accAtPortStatsOutShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutShorts.setStatus("mandatory")
_AccAtPortStatsOutFwdReqs_Type = Counter32
_AccAtPortStatsOutFwdReqs_Object = MibTableColumn
accAtPortStatsOutFwdReqs = _AccAtPortStatsOutFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 15),
    _AccAtPortStatsOutFwdReqs_Type()
)
accAtPortStatsOutFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutFwdReqs.setStatus("mandatory")
_AccAtPortStatsInErrors_Type = Counter32
_AccAtPortStatsInErrors_Object = MibTableColumn
accAtPortStatsInErrors = _AccAtPortStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 16),
    _AccAtPortStatsInErrors_Type()
)
accAtPortStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsInErrors.setStatus("mandatory")
_AccAtPortStatsOutErrors_Type = Counter32
_AccAtPortStatsOutErrors_Object = MibTableColumn
accAtPortStatsOutErrors = _AccAtPortStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 8, 1, 17),
    _AccAtPortStatsOutErrors_Type()
)
accAtPortStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtPortStatsOutErrors.setStatus("mandatory")
_AccAtRtmpStats_ObjectIdentity = ObjectIdentity
accAtRtmpStats = _AccAtRtmpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9)
)
_AccAtRtmpStatsInRequests_Type = Counter32
_AccAtRtmpStatsInRequests_Object = MibScalar
accAtRtmpStatsInRequests = _AccAtRtmpStatsInRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 1),
    _AccAtRtmpStatsInRequests_Type()
)
accAtRtmpStatsInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInRequests.setStatus("mandatory")
_AccAtRtmpStatsInDataReqs_Type = Counter32
_AccAtRtmpStatsInDataReqs_Object = MibScalar
accAtRtmpStatsInDataReqs = _AccAtRtmpStatsInDataReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 2),
    _AccAtRtmpStatsInDataReqs_Type()
)
accAtRtmpStatsInDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInDataReqs.setStatus("mandatory")
_AccAtRtmpStatsInResponses_Type = Counter32
_AccAtRtmpStatsInResponses_Object = MibScalar
accAtRtmpStatsInResponses = _AccAtRtmpStatsInResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 3),
    _AccAtRtmpStatsInResponses_Type()
)
accAtRtmpStatsInResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInResponses.setStatus("mandatory")
_AccAtRtmpStatsInDataResps_Type = Counter32
_AccAtRtmpStatsInDataResps_Object = MibScalar
accAtRtmpStatsInDataResps = _AccAtRtmpStatsInDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 4),
    _AccAtRtmpStatsInDataResps_Type()
)
accAtRtmpStatsInDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInDataResps.setStatus("mandatory")
_AccAtRtmpStatsOutRequests_Type = Counter32
_AccAtRtmpStatsOutRequests_Object = MibScalar
accAtRtmpStatsOutRequests = _AccAtRtmpStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 5),
    _AccAtRtmpStatsOutRequests_Type()
)
accAtRtmpStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutRequests.setStatus("mandatory")
_AccAtRtmpStatsOutDataReqs_Type = Counter32
_AccAtRtmpStatsOutDataReqs_Object = MibScalar
accAtRtmpStatsOutDataReqs = _AccAtRtmpStatsOutDataReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 6),
    _AccAtRtmpStatsOutDataReqs_Type()
)
accAtRtmpStatsOutDataReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutDataReqs.setStatus("mandatory")
_AccAtRtmpStatsOutResponses_Type = Counter32
_AccAtRtmpStatsOutResponses_Object = MibScalar
accAtRtmpStatsOutResponses = _AccAtRtmpStatsOutResponses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 7),
    _AccAtRtmpStatsOutResponses_Type()
)
accAtRtmpStatsOutResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutResponses.setStatus("mandatory")
_AccAtRtmpStatsOutDataResps_Type = Counter32
_AccAtRtmpStatsOutDataResps_Object = MibScalar
accAtRtmpStatsOutDataResps = _AccAtRtmpStatsOutDataResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 8),
    _AccAtRtmpStatsOutDataResps_Type()
)
accAtRtmpStatsOutDataResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutDataResps.setStatus("mandatory")
_AccAtRtmpStatsNetConflicts_Type = Counter32
_AccAtRtmpStatsNetConflicts_Object = MibScalar
accAtRtmpStatsNetConflicts = _AccAtRtmpStatsNetConflicts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 9),
    _AccAtRtmpStatsNetConflicts_Type()
)
accAtRtmpStatsNetConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsNetConflicts.setStatus("mandatory")
_AccAtRtmpStatsInErrors_Type = Counter32
_AccAtRtmpStatsInErrors_Object = MibScalar
accAtRtmpStatsInErrors = _AccAtRtmpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 10),
    _AccAtRtmpStatsInErrors_Type()
)
accAtRtmpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsInErrors.setStatus("mandatory")
_AccAtRtmpStatsOutErrors_Type = Counter32
_AccAtRtmpStatsOutErrors_Object = MibScalar
accAtRtmpStatsOutErrors = _AccAtRtmpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 9, 11),
    _AccAtRtmpStatsOutErrors_Type()
)
accAtRtmpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRtmpStatsOutErrors.setStatus("mandatory")
_AccAtRdbStats_ObjectIdentity = ObjectIdentity
accAtRdbStats = _AccAtRdbStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10)
)
_AccAtRdbStatsCacheds_Type = Counter32
_AccAtRdbStatsCacheds_Object = MibScalar
accAtRdbStatsCacheds = _AccAtRdbStatsCacheds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 1),
    _AccAtRdbStatsCacheds_Type()
)
accAtRdbStatsCacheds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsCacheds.setStatus("mandatory")
_AccAtRdbStatsSearchs_Type = Counter32
_AccAtRdbStatsSearchs_Object = MibScalar
accAtRdbStatsSearchs = _AccAtRdbStatsSearchs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 2),
    _AccAtRdbStatsSearchs_Type()
)
accAtRdbStatsSearchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsSearchs.setStatus("mandatory")
_AccAtRdbStatsNoRoutes_Type = Counter32
_AccAtRdbStatsNoRoutes_Object = MibScalar
accAtRdbStatsNoRoutes = _AccAtRdbStatsNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 3),
    _AccAtRdbStatsNoRoutes_Type()
)
accAtRdbStatsNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsNoRoutes.setStatus("mandatory")
_AccAtRdbStatsAdds_Type = Counter32
_AccAtRdbStatsAdds_Object = MibScalar
accAtRdbStatsAdds = _AccAtRdbStatsAdds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 4),
    _AccAtRdbStatsAdds_Type()
)
accAtRdbStatsAdds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsAdds.setStatus("mandatory")
_AccAtRdbStatsUpdates_Type = Counter32
_AccAtRdbStatsUpdates_Object = MibScalar
accAtRdbStatsUpdates = _AccAtRdbStatsUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 5),
    _AccAtRdbStatsUpdates_Type()
)
accAtRdbStatsUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsUpdates.setStatus("mandatory")
_AccAtRdbStatsDeletes_Type = Counter32
_AccAtRdbStatsDeletes_Object = MibScalar
accAtRdbStatsDeletes = _AccAtRdbStatsDeletes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 10, 6),
    _AccAtRdbStatsDeletes_Type()
)
accAtRdbStatsDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtRdbStatsDeletes.setStatus("mandatory")
_AccAtNbpStats_ObjectIdentity = ObjectIdentity
accAtNbpStats = _AccAtNbpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11)
)
_AccAtNbpStatsInBrReqs_Type = Counter32
_AccAtNbpStatsInBrReqs_Object = MibScalar
accAtNbpStatsInBrReqs = _AccAtNbpStatsInBrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 1),
    _AccAtNbpStatsInBrReqs_Type()
)
accAtNbpStatsInBrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInBrReqs.setStatus("mandatory")
_AccAtNbpStatsInLkUpReqs_Type = Counter32
_AccAtNbpStatsInLkUpReqs_Object = MibScalar
accAtNbpStatsInLkUpReqs = _AccAtNbpStatsInLkUpReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 2),
    _AccAtNbpStatsInLkUpReqs_Type()
)
accAtNbpStatsInLkUpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInLkUpReqs.setStatus("mandatory")
_AccAtNbpStatsInLkUpResps_Type = Counter32
_AccAtNbpStatsInLkUpResps_Object = MibScalar
accAtNbpStatsInLkUpResps = _AccAtNbpStatsInLkUpResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 3),
    _AccAtNbpStatsInLkUpResps_Type()
)
accAtNbpStatsInLkUpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInLkUpResps.setStatus("mandatory")
_AccAtNbpStatsInFwdReqs_Type = Counter32
_AccAtNbpStatsInFwdReqs_Object = MibScalar
accAtNbpStatsInFwdReqs = _AccAtNbpStatsInFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 4),
    _AccAtNbpStatsInFwdReqs_Type()
)
accAtNbpStatsInFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInFwdReqs.setStatus("mandatory")
_AccAtNbpStatsOutBrReqs_Type = Counter32
_AccAtNbpStatsOutBrReqs_Object = MibScalar
accAtNbpStatsOutBrReqs = _AccAtNbpStatsOutBrReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 5),
    _AccAtNbpStatsOutBrReqs_Type()
)
accAtNbpStatsOutBrReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutBrReqs.setStatus("mandatory")
_AccAtNbpStatsOutLkUpReqs_Type = Counter32
_AccAtNbpStatsOutLkUpReqs_Object = MibScalar
accAtNbpStatsOutLkUpReqs = _AccAtNbpStatsOutLkUpReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 6),
    _AccAtNbpStatsOutLkUpReqs_Type()
)
accAtNbpStatsOutLkUpReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutLkUpReqs.setStatus("mandatory")
_AccAtNbpStatsOutLkUpResps_Type = Counter32
_AccAtNbpStatsOutLkUpResps_Object = MibScalar
accAtNbpStatsOutLkUpResps = _AccAtNbpStatsOutLkUpResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 7),
    _AccAtNbpStatsOutLkUpResps_Type()
)
accAtNbpStatsOutLkUpResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutLkUpResps.setStatus("mandatory")
_AccAtNbpStatsOutFwdReqs_Type = Counter32
_AccAtNbpStatsOutFwdReqs_Object = MibScalar
accAtNbpStatsOutFwdReqs = _AccAtNbpStatsOutFwdReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 8),
    _AccAtNbpStatsOutFwdReqs_Type()
)
accAtNbpStatsOutFwdReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutFwdReqs.setStatus("mandatory")
_AccAtNbpStatsNoZones_Type = Counter32
_AccAtNbpStatsNoZones_Object = MibScalar
accAtNbpStatsNoZones = _AccAtNbpStatsNoZones_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 9),
    _AccAtNbpStatsNoZones_Type()
)
accAtNbpStatsNoZones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsNoZones.setStatus("mandatory")
_AccAtNbpStatsInErrors_Type = Counter32
_AccAtNbpStatsInErrors_Object = MibScalar
accAtNbpStatsInErrors = _AccAtNbpStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 10),
    _AccAtNbpStatsInErrors_Type()
)
accAtNbpStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsInErrors.setStatus("mandatory")
_AccAtNbpStatsOutErrors_Type = Counter32
_AccAtNbpStatsOutErrors_Object = MibScalar
accAtNbpStatsOutErrors = _AccAtNbpStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 11, 11),
    _AccAtNbpStatsOutErrors_Type()
)
accAtNbpStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtNbpStatsOutErrors.setStatus("mandatory")
_AccAtZipStats_ObjectIdentity = ObjectIdentity
accAtZipStats = _AccAtZipStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12)
)
_AccAtZipStatsInQuerys_Type = Counter32
_AccAtZipStatsInQuerys_Object = MibScalar
accAtZipStatsInQuerys = _AccAtZipStatsInQuerys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 1),
    _AccAtZipStatsInQuerys_Type()
)
accAtZipStatsInQuerys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInQuerys.setStatus("mandatory")
_AccAtZipStatsInReplies_Type = Counter32
_AccAtZipStatsInReplies_Object = MibScalar
accAtZipStatsInReplies = _AccAtZipStatsInReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 2),
    _AccAtZipStatsInReplies_Type()
)
accAtZipStatsInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInReplies.setStatus("mandatory")
_AccAtZipStatsInExtReplies_Type = Counter32
_AccAtZipStatsInExtReplies_Object = MibScalar
accAtZipStatsInExtReplies = _AccAtZipStatsInExtReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 3),
    _AccAtZipStatsInExtReplies_Type()
)
accAtZipStatsInExtReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInExtReplies.setStatus("mandatory")
_AccAtZipStatsInInfoReqs_Type = Counter32
_AccAtZipStatsInInfoReqs_Object = MibScalar
accAtZipStatsInInfoReqs = _AccAtZipStatsInInfoReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 4),
    _AccAtZipStatsInInfoReqs_Type()
)
accAtZipStatsInInfoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInInfoReqs.setStatus("mandatory")
_AccAtZipStatsInInfoReps_Type = Counter32
_AccAtZipStatsInInfoReps_Object = MibScalar
accAtZipStatsInInfoReps = _AccAtZipStatsInInfoReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 5),
    _AccAtZipStatsInInfoReps_Type()
)
accAtZipStatsInInfoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInInfoReps.setStatus("mandatory")
_AccAtZipStatsInTakeDowns_Type = Counter32
_AccAtZipStatsInTakeDowns_Object = MibScalar
accAtZipStatsInTakeDowns = _AccAtZipStatsInTakeDowns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 6),
    _AccAtZipStatsInTakeDowns_Type()
)
accAtZipStatsInTakeDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInTakeDowns.setStatus("mandatory")
_AccAtZipStatsInBringUps_Type = Counter32
_AccAtZipStatsInBringUps_Object = MibScalar
accAtZipStatsInBringUps = _AccAtZipStatsInBringUps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 7),
    _AccAtZipStatsInBringUps_Type()
)
accAtZipStatsInBringUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInBringUps.setStatus("mandatory")
_AccAtZipStatsInNotifies_Type = Counter32
_AccAtZipStatsInNotifies_Object = MibScalar
accAtZipStatsInNotifies = _AccAtZipStatsInNotifies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 8),
    _AccAtZipStatsInNotifies_Type()
)
accAtZipStatsInNotifies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInNotifies.setStatus("mandatory")
_AccAtZipStatsInGetZLReqs_Type = Counter32
_AccAtZipStatsInGetZLReqs_Object = MibScalar
accAtZipStatsInGetZLReqs = _AccAtZipStatsInGetZLReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 9),
    _AccAtZipStatsInGetZLReqs_Type()
)
accAtZipStatsInGetZLReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetZLReqs.setStatus("mandatory")
_AccAtZipStatsInGetLZReqs_Type = Counter32
_AccAtZipStatsInGetLZReqs_Object = MibScalar
accAtZipStatsInGetLZReqs = _AccAtZipStatsInGetLZReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 10),
    _AccAtZipStatsInGetLZReqs_Type()
)
accAtZipStatsInGetLZReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetLZReqs.setStatus("mandatory")
_AccAtZipStatsInGetMZReqs_Type = Counter32
_AccAtZipStatsInGetMZReqs_Object = MibScalar
accAtZipStatsInGetMZReqs = _AccAtZipStatsInGetMZReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 11),
    _AccAtZipStatsInGetMZReqs_Type()
)
accAtZipStatsInGetMZReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInGetMZReqs.setStatus("mandatory")
_AccAtZipStatsOutQueries_Type = Counter32
_AccAtZipStatsOutQueries_Object = MibScalar
accAtZipStatsOutQueries = _AccAtZipStatsOutQueries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 12),
    _AccAtZipStatsOutQueries_Type()
)
accAtZipStatsOutQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutQueries.setStatus("mandatory")
_AccAtZipStatsOutReplies_Type = Counter32
_AccAtZipStatsOutReplies_Object = MibScalar
accAtZipStatsOutReplies = _AccAtZipStatsOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 13),
    _AccAtZipStatsOutReplies_Type()
)
accAtZipStatsOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutReplies.setStatus("mandatory")
_AccAtZipStatsOutExtReplies_Type = Counter32
_AccAtZipStatsOutExtReplies_Object = MibScalar
accAtZipStatsOutExtReplies = _AccAtZipStatsOutExtReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 14),
    _AccAtZipStatsOutExtReplies_Type()
)
accAtZipStatsOutExtReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutExtReplies.setStatus("mandatory")
_AccAtZipStatsOutInfoReqs_Type = Counter32
_AccAtZipStatsOutInfoReqs_Object = MibScalar
accAtZipStatsOutInfoReqs = _AccAtZipStatsOutInfoReqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 15),
    _AccAtZipStatsOutInfoReqs_Type()
)
accAtZipStatsOutInfoReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutInfoReqs.setStatus("mandatory")
_AccAtZipStatsOutInfoReps_Type = Counter32
_AccAtZipStatsOutInfoReps_Object = MibScalar
accAtZipStatsOutInfoReps = _AccAtZipStatsOutInfoReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 16),
    _AccAtZipStatsOutInfoReps_Type()
)
accAtZipStatsOutInfoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutInfoReps.setStatus("mandatory")
_AccAtZipStatsOutGetZLReps_Type = Counter32
_AccAtZipStatsOutGetZLReps_Object = MibScalar
accAtZipStatsOutGetZLReps = _AccAtZipStatsOutGetZLReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 17),
    _AccAtZipStatsOutGetZLReps_Type()
)
accAtZipStatsOutGetZLReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetZLReps.setStatus("mandatory")
_AccAtZipStatsOutGetLZReps_Type = Counter32
_AccAtZipStatsOutGetLZReps_Object = MibScalar
accAtZipStatsOutGetLZReps = _AccAtZipStatsOutGetLZReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 18),
    _AccAtZipStatsOutGetLZReps_Type()
)
accAtZipStatsOutGetLZReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetLZReps.setStatus("mandatory")
_AccAtZipStatsOutGetMZReps_Type = Counter32
_AccAtZipStatsOutGetMZReps_Object = MibScalar
accAtZipStatsOutGetMZReps = _AccAtZipStatsOutGetMZReps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 19),
    _AccAtZipStatsOutGetMZReps_Type()
)
accAtZipStatsOutGetMZReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutGetMZReps.setStatus("mandatory")
_AccAtZipStatsZoneConflicts_Type = Counter32
_AccAtZipStatsZoneConflicts_Object = MibScalar
accAtZipStatsZoneConflicts = _AccAtZipStatsZoneConflicts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 20),
    _AccAtZipStatsZoneConflicts_Type()
)
accAtZipStatsZoneConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsZoneConflicts.setStatus("mandatory")
_AccAtZipStatsInErrors_Type = Counter32
_AccAtZipStatsInErrors_Object = MibScalar
accAtZipStatsInErrors = _AccAtZipStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 21),
    _AccAtZipStatsInErrors_Type()
)
accAtZipStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsInErrors.setStatus("mandatory")
_AccAtZipStatsOutErrors_Type = Counter32
_AccAtZipStatsOutErrors_Object = MibScalar
accAtZipStatsOutErrors = _AccAtZipStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 12, 22),
    _AccAtZipStatsOutErrors_Type()
)
accAtZipStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZipStatsOutErrors.setStatus("mandatory")
_AccAtAepStats_ObjectIdentity = ObjectIdentity
accAtAepStats = _AccAtAepStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13)
)
_AccAtAepStatsInErrors_Type = Counter32
_AccAtAepStatsInErrors_Object = MibScalar
accAtAepStatsInErrors = _AccAtAepStatsInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13, 1),
    _AccAtAepStatsInErrors_Type()
)
accAtAepStatsInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAepStatsInErrors.setStatus("mandatory")
_AccAtAepStatsOutErrors_Type = Counter32
_AccAtAepStatsOutErrors_Object = MibScalar
accAtAepStatsOutErrors = _AccAtAepStatsOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 13, 2),
    _AccAtAepStatsOutErrors_Type()
)
accAtAepStatsOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtAepStatsOutErrors.setStatus("mandatory")
_AccAtZoneListTable_Object = MibTable
accAtZoneListTable = _AccAtZoneListTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14)
)
if mibBuilder.loadTexts:
    accAtZoneListTable.setStatus("mandatory")
_AccAtZoneListEntry_Object = MibTableRow
accAtZoneListEntry = _AccAtZoneListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1)
)
accAtZoneListEntry.setIndexNames(
    (0, "ACC-MIB", "accAtZoneListPort"),
    (0, "ACC-MIB", "accAtZoneListName"),
)
if mibBuilder.loadTexts:
    accAtZoneListEntry.setStatus("mandatory")


class _AccAtZoneListPort_Type(Integer32):
    """Custom type accAtZoneListPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccAtZoneListPort_Type.__name__ = "Integer32"
_AccAtZoneListPort_Object = MibTableColumn
accAtZoneListPort = _AccAtZoneListPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 1),
    _AccAtZoneListPort_Type()
)
accAtZoneListPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneListPort.setStatus("mandatory")


class _AccAtZoneListStatus_Type(Integer32):
    """Custom type accAtZoneListStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("default", 2),
          ("invalid", 3))
    )


_AccAtZoneListStatus_Type.__name__ = "Integer32"
_AccAtZoneListStatus_Object = MibTableColumn
accAtZoneListStatus = _AccAtZoneListStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 2),
    _AccAtZoneListStatus_Type()
)
accAtZoneListStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtZoneListStatus.setStatus("mandatory")
_AccAtZoneListName_Type = DisplayString
_AccAtZoneListName_Object = MibTableColumn
accAtZoneListName = _AccAtZoneListName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 14, 1, 3),
    _AccAtZoneListName_Type()
)
accAtZoneListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneListName.setStatus("mandatory")
_AccAtZoneBynameTable_Object = MibTable
accAtZoneBynameTable = _AccAtZoneBynameTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15)
)
if mibBuilder.loadTexts:
    accAtZoneBynameTable.setStatus("mandatory")
_AccAtZoneBynameEntry_Object = MibTableRow
accAtZoneBynameEntry = _AccAtZoneBynameEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1)
)
accAtZoneBynameEntry.setIndexNames(
    (0, "ACC-MIB", "accAtZoneBynameNetMin"),
    (0, "ACC-MIB", "accAtZoneBynameName"),
)
if mibBuilder.loadTexts:
    accAtZoneBynameEntry.setStatus("mandatory")
_AccAtZoneBynameNetMin_Type = OctetString
_AccAtZoneBynameNetMin_Object = MibTableColumn
accAtZoneBynameNetMin = _AccAtZoneBynameNetMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 1),
    _AccAtZoneBynameNetMin_Type()
)
accAtZoneBynameNetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameNetMin.setStatus("mandatory")
_AccAtZoneBynameNetMax_Type = OctetString
_AccAtZoneBynameNetMax_Object = MibTableColumn
accAtZoneBynameNetMax = _AccAtZoneBynameNetMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 2),
    _AccAtZoneBynameNetMax_Type()
)
accAtZoneBynameNetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameNetMax.setStatus("mandatory")
_AccAtZoneBynameName_Type = DisplayString
_AccAtZoneBynameName_Object = MibTableColumn
accAtZoneBynameName = _AccAtZoneBynameName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 15, 1, 3),
    _AccAtZoneBynameName_Type()
)
accAtZoneBynameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynameName.setStatus("mandatory")
_AccAtZoneBynetTable_Object = MibTable
accAtZoneBynetTable = _AccAtZoneBynetTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16)
)
if mibBuilder.loadTexts:
    accAtZoneBynetTable.setStatus("mandatory")
_AccAtZoneBynetEntry_Object = MibTableRow
accAtZoneBynetEntry = _AccAtZoneBynetEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1)
)
accAtZoneBynetEntry.setIndexNames(
    (0, "ACC-MIB", "accAtZoneBynameNetMin"),
    (0, "ACC-MIB", "accAtZoneBynameName"),
)
if mibBuilder.loadTexts:
    accAtZoneBynetEntry.setStatus("mandatory")
_AccAtZoneBynetNetMin_Type = OctetString
_AccAtZoneBynetNetMin_Object = MibTableColumn
accAtZoneBynetNetMin = _AccAtZoneBynetNetMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 1),
    _AccAtZoneBynetNetMin_Type()
)
accAtZoneBynetNetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetNetMin.setStatus("mandatory")
_AccAtZoneBynetNetMax_Type = OctetString
_AccAtZoneBynetNetMax_Object = MibTableColumn
accAtZoneBynetNetMax = _AccAtZoneBynetNetMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 2),
    _AccAtZoneBynetNetMax_Type()
)
accAtZoneBynetNetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetNetMax.setStatus("mandatory")
_AccAtZoneBynetName_Type = DisplayString
_AccAtZoneBynetName_Object = MibTableColumn
accAtZoneBynetName = _AccAtZoneBynetName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 16, 1, 3),
    _AccAtZoneBynetName_Type()
)
accAtZoneBynetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAtZoneBynetName.setStatus("mandatory")
_AccAtForwardFilterTable_Object = MibTable
accAtForwardFilterTable = _AccAtForwardFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17)
)
if mibBuilder.loadTexts:
    accAtForwardFilterTable.setStatus("mandatory")
_AccAtForwardFilterEntry_Object = MibTableRow
accAtForwardFilterEntry = _AccAtForwardFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1)
)
accAtForwardFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accAtForwardFilterToMin"),
    (0, "ACC-MIB", "accAtForwardFilterToMax"),
    (0, "ACC-MIB", "accAtForwardFilterFromMin"),
    (0, "ACC-MIB", "accAtForwardFilterFromMax"),
    (0, "ACC-MIB", "accAtForwardFilterSocketMin"),
    (0, "ACC-MIB", "accAtForwardFilterSocketMax"),
    (0, "ACC-MIB", "accAtForwardFilterType"),
)
if mibBuilder.loadTexts:
    accAtForwardFilterEntry.setStatus("mandatory")
_AccAtForwardFilterToMin_Type = OctetString
_AccAtForwardFilterToMin_Object = MibTableColumn
accAtForwardFilterToMin = _AccAtForwardFilterToMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 1),
    _AccAtForwardFilterToMin_Type()
)
accAtForwardFilterToMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterToMin.setStatus("mandatory")
_AccAtForwardFilterToMax_Type = OctetString
_AccAtForwardFilterToMax_Object = MibTableColumn
accAtForwardFilterToMax = _AccAtForwardFilterToMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 2),
    _AccAtForwardFilterToMax_Type()
)
accAtForwardFilterToMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterToMax.setStatus("mandatory")
_AccAtForwardFilterFromMin_Type = OctetString
_AccAtForwardFilterFromMin_Object = MibTableColumn
accAtForwardFilterFromMin = _AccAtForwardFilterFromMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 3),
    _AccAtForwardFilterFromMin_Type()
)
accAtForwardFilterFromMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterFromMin.setStatus("mandatory")
_AccAtForwardFilterFromMax_Type = OctetString
_AccAtForwardFilterFromMax_Object = MibTableColumn
accAtForwardFilterFromMax = _AccAtForwardFilterFromMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 4),
    _AccAtForwardFilterFromMax_Type()
)
accAtForwardFilterFromMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterFromMax.setStatus("mandatory")


class _AccAtForwardFilterSocketMin_Type(Integer32):
    """Custom type accAtForwardFilterSocketMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtForwardFilterSocketMin_Type.__name__ = "Integer32"
_AccAtForwardFilterSocketMin_Object = MibTableColumn
accAtForwardFilterSocketMin = _AccAtForwardFilterSocketMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 5),
    _AccAtForwardFilterSocketMin_Type()
)
accAtForwardFilterSocketMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterSocketMin.setStatus("mandatory")


class _AccAtForwardFilterSocketMax_Type(Integer32):
    """Custom type accAtForwardFilterSocketMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccAtForwardFilterSocketMax_Type.__name__ = "Integer32"
_AccAtForwardFilterSocketMax_Object = MibTableColumn
accAtForwardFilterSocketMax = _AccAtForwardFilterSocketMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 6),
    _AccAtForwardFilterSocketMax_Type()
)
accAtForwardFilterSocketMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterSocketMax.setStatus("mandatory")


class _AccAtForwardFilterType_Type(Integer32):
    """Custom type accAtForwardFilterType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("adsp", 7),
          ("aep", 4),
          ("any", 1),
          ("atp", 3),
          ("nbp", 2),
          ("nbpBroadcast", 8),
          ("nbpForwardRequest", 11),
          ("nbpRequest", 9),
          ("nbpResponse", 10),
          ("rtmp", 5),
          ("zip", 6))
    )


_AccAtForwardFilterType_Type.__name__ = "Integer32"
_AccAtForwardFilterType_Object = MibTableColumn
accAtForwardFilterType = _AccAtForwardFilterType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 7),
    _AccAtForwardFilterType_Type()
)
accAtForwardFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterType.setStatus("mandatory")


class _AccAtForwardFilterDisposition_Type(Integer32):
    """Custom type accAtForwardFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AccAtForwardFilterDisposition_Type.__name__ = "Integer32"
_AccAtForwardFilterDisposition_Object = MibTableColumn
accAtForwardFilterDisposition = _AccAtForwardFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 8),
    _AccAtForwardFilterDisposition_Type()
)
accAtForwardFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterDisposition.setStatus("mandatory")


class _AccAtForwardFilterStatus_Type(Integer32):
    """Custom type accAtForwardFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccAtForwardFilterStatus_Type.__name__ = "Integer32"
_AccAtForwardFilterStatus_Object = MibTableColumn
accAtForwardFilterStatus = _AccAtForwardFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 17, 1, 9),
    _AccAtForwardFilterStatus_Type()
)
accAtForwardFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtForwardFilterStatus.setStatus("mandatory")
_AccAtRouteFilterTable_Object = MibTable
accAtRouteFilterTable = _AccAtRouteFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18)
)
if mibBuilder.loadTexts:
    accAtRouteFilterTable.setStatus("mandatory")
_AccAtRouteFilterEntry_Object = MibTableRow
accAtRouteFilterEntry = _AccAtRouteFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1)
)
accAtRouteFilterEntry.setIndexNames(
    (0, "ACC-MIB", "accAtRouteFilterRouterMin"),
    (0, "ACC-MIB", "accAtRouteFilterRouterMax"),
    (0, "ACC-MIB", "accAtRouteFilterRangeMin"),
    (0, "ACC-MIB", "accAtRouteFilterRangeMax"),
)
if mibBuilder.loadTexts:
    accAtRouteFilterEntry.setStatus("mandatory")
_AccAtRouteFilterRouterMin_Type = OctetString
_AccAtRouteFilterRouterMin_Object = MibTableColumn
accAtRouteFilterRouterMin = _AccAtRouteFilterRouterMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 1),
    _AccAtRouteFilterRouterMin_Type()
)
accAtRouteFilterRouterMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRouterMin.setStatus("mandatory")
_AccAtRouteFilterRouterMax_Type = OctetString
_AccAtRouteFilterRouterMax_Object = MibTableColumn
accAtRouteFilterRouterMax = _AccAtRouteFilterRouterMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 2),
    _AccAtRouteFilterRouterMax_Type()
)
accAtRouteFilterRouterMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRouterMax.setStatus("mandatory")
_AccAtRouteFilterRangeMin_Type = OctetString
_AccAtRouteFilterRangeMin_Object = MibTableColumn
accAtRouteFilterRangeMin = _AccAtRouteFilterRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 3),
    _AccAtRouteFilterRangeMin_Type()
)
accAtRouteFilterRangeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRangeMin.setStatus("mandatory")
_AccAtRouteFilterRangeMax_Type = OctetString
_AccAtRouteFilterRangeMax_Object = MibTableColumn
accAtRouteFilterRangeMax = _AccAtRouteFilterRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 4),
    _AccAtRouteFilterRangeMax_Type()
)
accAtRouteFilterRangeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterRangeMax.setStatus("mandatory")


class _AccAtRouteFilterDisposition_Type(Integer32):
    """Custom type accAtRouteFilterDisposition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("reject", 2))
    )


_AccAtRouteFilterDisposition_Type.__name__ = "Integer32"
_AccAtRouteFilterDisposition_Object = MibTableColumn
accAtRouteFilterDisposition = _AccAtRouteFilterDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 5),
    _AccAtRouteFilterDisposition_Type()
)
accAtRouteFilterDisposition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterDisposition.setStatus("mandatory")


class _AccAtRouteFilterStatus_Type(Integer32):
    """Custom type accAtRouteFilterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_AccAtRouteFilterStatus_Type.__name__ = "Integer32"
_AccAtRouteFilterStatus_Object = MibTableColumn
accAtRouteFilterStatus = _AccAtRouteFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 28, 18, 1, 6),
    _AccAtRouteFilterStatus_Type()
)
accAtRouteFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAtRouteFilterStatus.setStatus("mandatory")
_AccBootp_ObjectIdentity = ObjectIdentity
accBootp = _AccBootp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29)
)
_AccBootServerOld_ObjectIdentity = ObjectIdentity
accBootServerOld = _AccBootServerOld_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 1)
)
_AccBootpServerOld_Type = IpAddress
_AccBootpServerOld_Object = MibScalar
accBootpServerOld = _AccBootpServerOld_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 1, 1),
    _AccBootpServerOld_Type()
)
accBootpServerOld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootpServerOld.setStatus("mandatory")


class _AccBootMode_Type(Integer32):
    """Custom type accBootMode based on Integer32"""
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
        *(("automatic", 1),
          ("default", 4),
          ("forced", 2),
          ("off", 3))
    )


_AccBootMode_Type.__name__ = "Integer32"
_AccBootMode_Object = MibScalar
accBootMode = _AccBootMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 2),
    _AccBootMode_Type()
)
accBootMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootMode.setStatus("mandatory")


class _AccBootState_Type(Integer32):
    """Custom type accBootState based on Integer32"""
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
        *(("complete", 6),
          ("configuring", 5),
          ("disabled", 2),
          ("failed", 7),
          ("initial", 1),
          ("requesting", 3),
          ("waiting", 4))
    )


_AccBootState_Type.__name__ = "Integer32"
_AccBootState_Object = MibScalar
accBootState = _AccBootState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 3),
    _AccBootState_Type()
)
accBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootState.setStatus("mandatory")
_AccBootyiaddr_Type = IpAddress
_AccBootyiaddr_Object = MibScalar
accBootyiaddr = _AccBootyiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 4),
    _AccBootyiaddr_Type()
)
accBootyiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootyiaddr.setStatus("mandatory")
_AccBootsiaddr_Type = IpAddress
_AccBootsiaddr_Object = MibScalar
accBootsiaddr = _AccBootsiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 5),
    _AccBootsiaddr_Type()
)
accBootsiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootsiaddr.setStatus("mandatory")
_AccBootsname_Type = DisplayString
_AccBootsname_Object = MibScalar
accBootsname = _AccBootsname_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 6),
    _AccBootsname_Type()
)
accBootsname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootsname.setStatus("mandatory")
_AccBootgiaddr_Type = IpAddress
_AccBootgiaddr_Object = MibScalar
accBootgiaddr = _AccBootgiaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 7),
    _AccBootgiaddr_Type()
)
accBootgiaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootgiaddr.setStatus("deprecated")
_AccBootfile_Type = DisplayString
_AccBootfile_Object = MibScalar
accBootfile = _AccBootfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 8),
    _AccBootfile_Type()
)
accBootfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootfile.setStatus("mandatory")
_AccBootInterface_Type = Integer32
_AccBootInterface_Object = MibScalar
accBootInterface = _AccBootInterface_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 9),
    _AccBootInterface_Type()
)
accBootInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootInterface.setStatus("mandatory")
_AccBootSentRequests_Type = Counter32
_AccBootSentRequests_Object = MibScalar
accBootSentRequests = _AccBootSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 10),
    _AccBootSentRequests_Type()
)
accBootSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootSentRequests.setStatus("mandatory")
_AccBootReceivedReplies_Type = Counter32
_AccBootReceivedReplies_Object = MibScalar
accBootReceivedReplies = _AccBootReceivedReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 11),
    _AccBootReceivedReplies_Type()
)
accBootReceivedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootReceivedReplies.setStatus("mandatory")
_AccBootDiscardedReplies_Type = Counter32
_AccBootDiscardedReplies_Object = MibScalar
accBootDiscardedReplies = _AccBootDiscardedReplies_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 12),
    _AccBootDiscardedReplies_Type()
)
accBootDiscardedReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootDiscardedReplies.setStatus("mandatory")
_AccBootServerTable_Object = MibTable
accBootServerTable = _AccBootServerTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13)
)
if mibBuilder.loadTexts:
    accBootServerTable.setStatus("mandatory")
_AccBootServerEntry_Object = MibTableRow
accBootServerEntry = _AccBootServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1)
)
accBootServerEntry.setIndexNames(
    (0, "ACC-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    accBootServerEntry.setStatus("mandatory")
_AccBootServerIPAddr_Type = IpAddress
_AccBootServerIPAddr_Object = MibTableColumn
accBootServerIPAddr = _AccBootServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1, 1),
    _AccBootServerIPAddr_Type()
)
accBootServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBootServerIPAddr.setStatus("mandatory")
_PysmiFakeCol3_Type = IpAddress
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 13, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_AccBootg1iaddr_Type = IpAddress
_AccBootg1iaddr_Object = MibScalar
accBootg1iaddr = _AccBootg1iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 14),
    _AccBootg1iaddr_Type()
)
accBootg1iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg1iaddr.setStatus("mandatory")
_AccBootg2iaddr_Type = IpAddress
_AccBootg2iaddr_Object = MibScalar
accBootg2iaddr = _AccBootg2iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 15),
    _AccBootg2iaddr_Type()
)
accBootg2iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg2iaddr.setStatus("mandatory")
_AccBootg3iaddr_Type = IpAddress
_AccBootg3iaddr_Object = MibScalar
accBootg3iaddr = _AccBootg3iaddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 29, 16),
    _AccBootg3iaddr_Type()
)
accBootg3iaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBootg3iaddr.setStatus("mandatory")
_AccPing_ObjectIdentity = ObjectIdentity
accPing = _AccPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30)
)
_AccPingDest_Type = IpAddress
_AccPingDest_Object = MibScalar
accPingDest = _AccPingDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 1),
    _AccPingDest_Type()
)
accPingDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDest.setStatus("mandatory")


class _AccPingReqCnt_Type(Integer32):
    """Custom type accPingReqCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AccPingReqCnt_Type.__name__ = "Integer32"
_AccPingReqCnt_Object = MibScalar
accPingReqCnt = _AccPingReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 2),
    _AccPingReqCnt_Type()
)
accPingReqCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingReqCnt.setStatus("mandatory")


class _AccPingDataMin_Type(Integer32):
    """Custom type accPingDataMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_AccPingDataMin_Type.__name__ = "Integer32"
_AccPingDataMin_Object = MibScalar
accPingDataMin = _AccPingDataMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 3),
    _AccPingDataMin_Type()
)
accPingDataMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDataMin.setStatus("mandatory")


class _AccPingDataMax_Type(Integer32):
    """Custom type accPingDataMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_AccPingDataMax_Type.__name__ = "Integer32"
_AccPingDataMax_Object = MibScalar
accPingDataMax = _AccPingDataMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 4),
    _AccPingDataMax_Type()
)
accPingDataMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDataMax.setStatus("mandatory")


class _AccPingTimeMin_Type(Integer32):
    """Custom type accPingTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AccPingTimeMin_Type.__name__ = "Integer32"
_AccPingTimeMin_Object = MibScalar
accPingTimeMin = _AccPingTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 5),
    _AccPingTimeMin_Type()
)
accPingTimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingTimeMin.setStatus("mandatory")


class _AccPingTimeMax_Type(Integer32):
    """Custom type accPingTimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AccPingTimeMax_Type.__name__ = "Integer32"
_AccPingTimeMax_Object = MibScalar
accPingTimeMax = _AccPingTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 6),
    _AccPingTimeMax_Type()
)
accPingTimeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingTimeMax.setStatus("mandatory")
_AccPingSndPkts_Type = Counter32
_AccPingSndPkts_Object = MibScalar
accPingSndPkts = _AccPingSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 7),
    _AccPingSndPkts_Type()
)
accPingSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingSndPkts.setStatus("mandatory")
_AccPingSndBytes_Type = Counter32
_AccPingSndBytes_Object = MibScalar
accPingSndBytes = _AccPingSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 8),
    _AccPingSndBytes_Type()
)
accPingSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingSndBytes.setStatus("mandatory")
_AccPingRcvPkts_Type = Counter32
_AccPingRcvPkts_Object = MibScalar
accPingRcvPkts = _AccPingRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 9),
    _AccPingRcvPkts_Type()
)
accPingRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvPkts.setStatus("mandatory")
_AccPingRcvBytes_Type = Counter32
_AccPingRcvBytes_Object = MibScalar
accPingRcvBytes = _AccPingRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 10),
    _AccPingRcvBytes_Type()
)
accPingRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvBytes.setStatus("mandatory")
_AccPingRcvOKs_Type = Counter32
_AccPingRcvOKs_Object = MibScalar
accPingRcvOKs = _AccPingRcvOKs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 11),
    _AccPingRcvOKs_Type()
)
accPingRcvOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvOKs.setStatus("mandatory")
_AccPingRcvBads_Type = Counter32
_AccPingRcvBads_Object = MibScalar
accPingRcvBads = _AccPingRcvBads_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 12),
    _AccPingRcvBads_Type()
)
accPingRcvBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvBads.setStatus("mandatory")
_AccPingDelayMin_Type = Integer32
_AccPingDelayMin_Object = MibScalar
accPingDelayMin = _AccPingDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 13),
    _AccPingDelayMin_Type()
)
accPingDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayMin.setStatus("mandatory")
_AccPingDelayMax_Type = Integer32
_AccPingDelayMax_Object = MibScalar
accPingDelayMax = _AccPingDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 14),
    _AccPingDelayMax_Type()
)
accPingDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayMax.setStatus("mandatory")
_AccPingDelayAvg_Type = Integer32
_AccPingDelayAvg_Object = MibScalar
accPingDelayAvg = _AccPingDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 15),
    _AccPingDelayAvg_Type()
)
accPingDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayAvg.setStatus("mandatory")
_AccDial_ObjectIdentity = ObjectIdentity
accDial = _AccDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31)
)
_AccDialBackupTable_Object = MibTable
accDialBackupTable = _AccDialBackupTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1)
)
if mibBuilder.loadTexts:
    accDialBackupTable.setStatus("mandatory")
_AccDialBackupEntry_Object = MibTableRow
accDialBackupEntry = _AccDialBackupEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1)
)
accDialBackupEntry.setIndexNames(
    (0, "ACC-MIB", "accDialBackupPrimary"),
)
if mibBuilder.loadTexts:
    accDialBackupEntry.setStatus("mandatory")
_AccDialBackupPort_Type = BackupPort
_AccDialBackupPort_Object = MibTableColumn
accDialBackupPort = _AccDialBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 1),
    _AccDialBackupPort_Type()
)
accDialBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupPort.setStatus("mandatory")
_AccDialBackupPrimary_Type = PhysicalPort
_AccDialBackupPrimary_Object = MibTableColumn
accDialBackupPrimary = _AccDialBackupPrimary_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 2),
    _AccDialBackupPrimary_Type()
)
accDialBackupPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialBackupPrimary.setStatus("mandatory")


class _AccDialBackupControl_Type(Integer32):
    """Custom type accDialBackupControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demand", 3),
          ("master", 1),
          ("slave", 2))
    )


_AccDialBackupControl_Type.__name__ = "Integer32"
_AccDialBackupControl_Object = MibTableColumn
accDialBackupControl = _AccDialBackupControl_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 3),
    _AccDialBackupControl_Type()
)
accDialBackupControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupControl.setStatus("mandatory")


class _AccDialBackupRetry_Type(Integer32):
    """Custom type accDialBackupRetry based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccDialBackupRetry_Type.__name__ = "Integer32"
_AccDialBackupRetry_Object = MibTableColumn
accDialBackupRetry = _AccDialBackupRetry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 4),
    _AccDialBackupRetry_Type()
)
accDialBackupRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupRetry.setStatus("mandatory")


class _AccDialBackupDamp_Type(Integer32):
    """Custom type accDialBackupDamp based on Integer32"""
    defaultValue = 3


_AccDialBackupDamp_Object = MibTableColumn
accDialBackupDamp = _AccDialBackupDamp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 5),
    _AccDialBackupDamp_Type()
)
accDialBackupDamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupDamp.setStatus("mandatory")


class _AccDialBackupCallCongestion_Type(Integer32):
    """Custom type accDialBackupCallCongestion based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AccDialBackupCallCongestion_Type.__name__ = "Integer32"
_AccDialBackupCallCongestion_Object = MibTableColumn
accDialBackupCallCongestion = _AccDialBackupCallCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 6),
    _AccDialBackupCallCongestion_Type()
)
accDialBackupCallCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallCongestion.setStatus("mandatory")


class _AccDialBackupClearCongestion_Type(Integer32):
    """Custom type accDialBackupClearCongestion based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AccDialBackupClearCongestion_Type.__name__ = "Integer32"
_AccDialBackupClearCongestion_Object = MibTableColumn
accDialBackupClearCongestion = _AccDialBackupClearCongestion_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 7),
    _AccDialBackupClearCongestion_Type()
)
accDialBackupClearCongestion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupClearCongestion.setStatus("mandatory")


class _AccDialBackupCallError_Type(Integer32):
    """Custom type accDialBackupCallError based on Integer32"""
    defaultValue = 5


_AccDialBackupCallError_Object = MibTableColumn
accDialBackupCallError = _AccDialBackupCallError_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 8),
    _AccDialBackupCallError_Type()
)
accDialBackupCallError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallError.setStatus("mandatory")
_AccDialBackupCallAddress_Type = CallAddress
_AccDialBackupCallAddress_Object = MibTableColumn
accDialBackupCallAddress = _AccDialBackupCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 9),
    _AccDialBackupCallAddress_Type()
)
accDialBackupCallAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupCallAddress.setStatus("mandatory")


class _AccDialBackupStatus_Type(Integer32):
    """Custom type accDialBackupStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccDialBackupStatus_Type.__name__ = "Integer32"
_AccDialBackupStatus_Object = MibTableColumn
accDialBackupStatus = _AccDialBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 10),
    _AccDialBackupStatus_Type()
)
accDialBackupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupStatus.setStatus("mandatory")


class _AccDialBackupState_Type(Integer32):
    """Custom type accDialBackupState based on Integer32"""
    defaultValue = 6

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
        *(("backup", 4),
          ("clear", 6),
          ("congestIn", 2),
          ("congestOut", 1),
          ("errors", 3),
          ("manual", 5))
    )


_AccDialBackupState_Type.__name__ = "Integer32"
_AccDialBackupState_Object = MibTableColumn
accDialBackupState = _AccDialBackupState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 1, 1, 11),
    _AccDialBackupState_Type()
)
accDialBackupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialBackupState.setStatus("mandatory")
_AccDialPortTable_Object = MibTable
accDialPortTable = _AccDialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2)
)
if mibBuilder.loadTexts:
    accDialPortTable.setStatus("mandatory")
_AccDialPortEntry_Object = MibTableRow
accDialPortEntry = _AccDialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1)
)
accDialPortEntry.setIndexNames(
    (0, "ACC-MIB", "accDialPortIndex"),
)
if mibBuilder.loadTexts:
    accDialPortEntry.setStatus("mandatory")
_AccDialPortIndex_Type = Integer32
_AccDialPortIndex_Object = MibTableColumn
accDialPortIndex = _AccDialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 1),
    _AccDialPortIndex_Type()
)
accDialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortIndex.setStatus("mandatory")


class _AccDialPortContents_Type(Integer32):
    """Custom type accDialPortContents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialPortContents_Type.__name__ = "Integer32"
_AccDialPortContents_Object = MibTableColumn
accDialPortContents = _AccDialPortContents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 2),
    _AccDialPortContents_Type()
)
accDialPortContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortContents.setStatus("mandatory")


class _AccDialPortStationType_Type(Integer32):
    """Custom type accDialPortStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demand", 3),
          ("master", 1),
          ("slave", 2))
    )


_AccDialPortStationType_Type.__name__ = "Integer32"
_AccDialPortStationType_Object = MibTableColumn
accDialPortStationType = _AccDialPortStationType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 3),
    _AccDialPortStationType_Type()
)
accDialPortStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortStationType.setStatus("mandatory")


class _AccDialPortAdminState_Type(Integer32):
    """Custom type accDialPortAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_AccDialPortAdminState_Type.__name__ = "Integer32"
_AccDialPortAdminState_Object = MibTableColumn
accDialPortAdminState = _AccDialPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 4),
    _AccDialPortAdminState_Type()
)
accDialPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortAdminState.setStatus("mandatory")


class _AccDialPortCallState_Type(Integer32):
    """Custom type accDialPortCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("call", 2),
          ("clear", 1))
    )


_AccDialPortCallState_Type.__name__ = "Integer32"
_AccDialPortCallState_Object = MibTableColumn
accDialPortCallState = _AccDialPortCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 5),
    _AccDialPortCallState_Type()
)
accDialPortCallState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortCallState.setStatus("mandatory")
_AccDialPortRetryInterval_Type = TimeTicks
_AccDialPortRetryInterval_Object = MibTableColumn
accDialPortRetryInterval = _AccDialPortRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 6),
    _AccDialPortRetryInterval_Type()
)
accDialPortRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortRetryInterval.setStatus("mandatory")
_AccDialPortRetryCount_Type = Integer32
_AccDialPortRetryCount_Object = MibTableColumn
accDialPortRetryCount = _AccDialPortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 7),
    _AccDialPortRetryCount_Type()
)
accDialPortRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortRetryCount.setStatus("mandatory")
_AccDialPortClearingInterv_Type = TimeTicks
_AccDialPortClearingInterv_Object = MibTableColumn
accDialPortClearingInterv = _AccDialPortClearingInterv_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 8),
    _AccDialPortClearingInterv_Type()
)
accDialPortClearingInterv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortClearingInterv.setStatus("mandatory")
_AccDialPortMessageLevel_Type = Integer32
_AccDialPortMessageLevel_Object = MibTableColumn
accDialPortMessageLevel = _AccDialPortMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 9),
    _AccDialPortMessageLevel_Type()
)
accDialPortMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortMessageLevel.setStatus("mandatory")
_AccDialPortPhysicalPort_Type = Integer32
_AccDialPortPhysicalPort_Object = MibTableColumn
accDialPortPhysicalPort = _AccDialPortPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 10),
    _AccDialPortPhysicalPort_Type()
)
accDialPortPhysicalPort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialPortPhysicalPort.setStatus("mandatory")
_AccDialPortCallAddress_Type = OctetString
_AccDialPortCallAddress_Object = MibTableColumn
accDialPortCallAddress = _AccDialPortCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 11),
    _AccDialPortCallAddress_Type()
)
accDialPortCallAddress.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialPortCallAddress.setStatus("mandatory")
_AccDialPortPhysicalPortStr_Type = OctetString
_AccDialPortPhysicalPortStr_Object = MibTableColumn
accDialPortPhysicalPortStr = _AccDialPortPhysicalPortStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 12),
    _AccDialPortPhysicalPortStr_Type()
)
accDialPortPhysicalPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortPhysicalPortStr.setStatus("mandatory")
_AccDialPortCallAddressStr_Type = OctetString
_AccDialPortCallAddressStr_Object = MibTableColumn
accDialPortCallAddressStr = _AccDialPortCallAddressStr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 13),
    _AccDialPortCallAddressStr_Type()
)
accDialPortCallAddressStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortCallAddressStr.setStatus("mandatory")
_AccDialPortPassword_Type = OctetString
_AccDialPortPassword_Object = MibTableColumn
accDialPortPassword = _AccDialPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 14),
    _AccDialPortPassword_Type()
)
accDialPortPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialPortPassword.setStatus("mandatory")
_AccDialPortName_Type = OctetString
_AccDialPortName_Object = MibTableColumn
accDialPortName = _AccDialPortName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 2, 1, 15),
    _AccDialPortName_Type()
)
accDialPortName.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialPortName.setStatus("mandatory")
_AccDialPortStatTable_Object = MibTable
accDialPortStatTable = _AccDialPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3)
)
if mibBuilder.loadTexts:
    accDialPortStatTable.setStatus("mandatory")
_AccDialPortStatEntry_Object = MibTableRow
accDialPortStatEntry = _AccDialPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1)
)
accDialPortStatEntry.setIndexNames(
    (0, "ACC-MIB", "accDialPortStatIndex"),
)
if mibBuilder.loadTexts:
    accDialPortStatEntry.setStatus("mandatory")
_AccDialPortStatIndex_Type = Integer32
_AccDialPortStatIndex_Object = MibTableColumn
accDialPortStatIndex = _AccDialPortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 1),
    _AccDialPortStatIndex_Type()
)
accDialPortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatIndex.setStatus("mandatory")
_AccDialPortStatActPhysPort_Type = Integer32
_AccDialPortStatActPhysPort_Object = MibTableColumn
accDialPortStatActPhysPort = _AccDialPortStatActPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 2),
    _AccDialPortStatActPhysPort_Type()
)
accDialPortStatActPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatActPhysPort.setStatus("mandatory")
_AccDialPortStatState_Type = Integer32
_AccDialPortStatState_Object = MibTableColumn
accDialPortStatState = _AccDialPortStatState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 3),
    _AccDialPortStatState_Type()
)
accDialPortStatState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialPortStatState.setStatus("mandatory")
_AccDialPortStatTrigFwdr_Type = Integer32
_AccDialPortStatTrigFwdr_Object = MibTableColumn
accDialPortStatTrigFwdr = _AccDialPortStatTrigFwdr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 4),
    _AccDialPortStatTrigFwdr_Type()
)
accDialPortStatTrigFwdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigFwdr.setStatus("mandatory")
_AccDialPortStatElapsedTime_Type = TimeTicks
_AccDialPortStatElapsedTime_Object = MibTableColumn
accDialPortStatElapsedTime = _AccDialPortStatElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 5),
    _AccDialPortStatElapsedTime_Type()
)
accDialPortStatElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatElapsedTime.setStatus("mandatory")
_AccDialPortStatTrigSrcAddr_Type = OctetString
_AccDialPortStatTrigSrcAddr_Object = MibTableColumn
accDialPortStatTrigSrcAddr = _AccDialPortStatTrigSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 6),
    _AccDialPortStatTrigSrcAddr_Type()
)
accDialPortStatTrigSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigSrcAddr.setStatus("mandatory")
_AccDialPortStatTrigCallAddr_Type = OctetString
_AccDialPortStatTrigCallAddr_Object = MibTableColumn
accDialPortStatTrigCallAddr = _AccDialPortStatTrigCallAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 7),
    _AccDialPortStatTrigCallAddr_Type()
)
accDialPortStatTrigCallAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatTrigCallAddr.setStatus("mandatory")
_AccDialPortStatSuccessOut_Type = Integer32
_AccDialPortStatSuccessOut_Object = MibTableColumn
accDialPortStatSuccessOut = _AccDialPortStatSuccessOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 8),
    _AccDialPortStatSuccessOut_Type()
)
accDialPortStatSuccessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatSuccessOut.setStatus("mandatory")
_AccDialPortStatUnsuccessOut_Type = Integer32
_AccDialPortStatUnsuccessOut_Object = MibTableColumn
accDialPortStatUnsuccessOut = _AccDialPortStatUnsuccessOut_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 9),
    _AccDialPortStatUnsuccessOut_Type()
)
accDialPortStatUnsuccessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatUnsuccessOut.setStatus("mandatory")
_AccDialPortStatSuccessIn_Type = Integer32
_AccDialPortStatSuccessIn_Object = MibTableColumn
accDialPortStatSuccessIn = _AccDialPortStatSuccessIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 10),
    _AccDialPortStatSuccessIn_Type()
)
accDialPortStatSuccessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatSuccessIn.setStatus("mandatory")
_AccDialPortStatUnsuccessIn_Type = Integer32
_AccDialPortStatUnsuccessIn_Object = MibTableColumn
accDialPortStatUnsuccessIn = _AccDialPortStatUnsuccessIn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 3, 1, 11),
    _AccDialPortStatUnsuccessIn_Type()
)
accDialPortStatUnsuccessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accDialPortStatUnsuccessIn.setStatus("mandatory")
_AccDialOrigAtTable_Object = MibTable
accDialOrigAtTable = _AccDialOrigAtTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4)
)
if mibBuilder.loadTexts:
    accDialOrigAtTable.setStatus("mandatory")
_AccDialOrigAtEntry_Object = MibTableRow
accDialOrigAtEntry = _AccDialOrigAtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1)
)
accDialOrigAtEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigAtDestStart"),
    (0, "ACC-MIB", "accDialOrigAtDestEnd"),
    (0, "ACC-MIB", "accDialOrigAtSourceStart"),
    (0, "ACC-MIB", "accDialOrigAtSourceEnd"),
)
if mibBuilder.loadTexts:
    accDialOrigAtEntry.setStatus("mandatory")


class _AccDialOrigAtStatus_Type(Integer32):
    """Custom type accDialOrigAtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigAtStatus_Type.__name__ = "Integer32"
_AccDialOrigAtStatus_Object = MibTableColumn
accDialOrigAtStatus = _AccDialOrigAtStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 1),
    _AccDialOrigAtStatus_Type()
)
accDialOrigAtStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigAtStatus.setStatus("mandatory")
_AccDialOrigAtDestStart_Type = OctetString
_AccDialOrigAtDestStart_Object = MibTableColumn
accDialOrigAtDestStart = _AccDialOrigAtDestStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 2),
    _AccDialOrigAtDestStart_Type()
)
accDialOrigAtDestStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtDestStart.setStatus("mandatory")
_AccDialOrigAtDestEnd_Type = OctetString
_AccDialOrigAtDestEnd_Object = MibTableColumn
accDialOrigAtDestEnd = _AccDialOrigAtDestEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 3),
    _AccDialOrigAtDestEnd_Type()
)
accDialOrigAtDestEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtDestEnd.setStatus("mandatory")
_AccDialOrigAtSourceStart_Type = OctetString
_AccDialOrigAtSourceStart_Object = MibTableColumn
accDialOrigAtSourceStart = _AccDialOrigAtSourceStart_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 4),
    _AccDialOrigAtSourceStart_Type()
)
accDialOrigAtSourceStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtSourceStart.setStatus("mandatory")
_AccDialOrigAtSourceEnd_Type = OctetString
_AccDialOrigAtSourceEnd_Object = MibTableColumn
accDialOrigAtSourceEnd = _AccDialOrigAtSourceEnd_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 5),
    _AccDialOrigAtSourceEnd_Type()
)
accDialOrigAtSourceEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtSourceEnd.setStatus("mandatory")


class _AccDialOrigAtTraffic_Type(Integer32):
    """Custom type accDialOrigAtTraffic based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("adsp", 7),
          ("aep", 4),
          ("any", 1),
          ("atp", 3),
          ("nbp", 2),
          ("nbpbroadcast", 8),
          ("nbpforwardreq", 11),
          ("nbplookup", 9),
          ("nbpreply", 10),
          ("rtmp", 5),
          ("zip", 6))
    )


_AccDialOrigAtTraffic_Type.__name__ = "Integer32"
_AccDialOrigAtTraffic_Object = MibTableColumn
accDialOrigAtTraffic = _AccDialOrigAtTraffic_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 6),
    _AccDialOrigAtTraffic_Type()
)
accDialOrigAtTraffic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtTraffic.setStatus("mandatory")


class _AccDialOrigAtAction_Type(Integer32):
    """Custom type accDialOrigAtAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigAtAction_Type.__name__ = "Integer32"
_AccDialOrigAtAction_Object = MibTableColumn
accDialOrigAtAction = _AccDialOrigAtAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 4, 1, 7),
    _AccDialOrigAtAction_Type()
)
accDialOrigAtAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigAtAction.setStatus("mandatory")
_AccDialOrigDnTable_Object = MibTable
accDialOrigDnTable = _AccDialOrigDnTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5)
)
if mibBuilder.loadTexts:
    accDialOrigDnTable.setStatus("mandatory")
_AccDialOrigDnEntry_Object = MibTableRow
accDialOrigDnEntry = _AccDialOrigDnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1)
)
accDialOrigDnEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigDnDestAddr"),
    (0, "ACC-MIB", "accDialOrigDnSourceAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigDnEntry.setStatus("mandatory")


class _AccDialOrigDnStatus_Type(Integer32):
    """Custom type accDialOrigDnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigDnStatus_Type.__name__ = "Integer32"
_AccDialOrigDnStatus_Object = MibTableColumn
accDialOrigDnStatus = _AccDialOrigDnStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 1),
    _AccDialOrigDnStatus_Type()
)
accDialOrigDnStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigDnStatus.setStatus("mandatory")


class _AccDialOrigDnDestAddr_Type(Integer32):
    """Custom type accDialOrigDnDestAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDialOrigDnDestAddr_Type.__name__ = "Integer32"
_AccDialOrigDnDestAddr_Object = MibTableColumn
accDialOrigDnDestAddr = _AccDialOrigDnDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 2),
    _AccDialOrigDnDestAddr_Type()
)
accDialOrigDnDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnDestAddr.setStatus("mandatory")


class _AccDialOrigDnSourceAddr_Type(Integer32):
    """Custom type accDialOrigDnSourceAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccDialOrigDnSourceAddr_Type.__name__ = "Integer32"
_AccDialOrigDnSourceAddr_Object = MibTableColumn
accDialOrigDnSourceAddr = _AccDialOrigDnSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 3),
    _AccDialOrigDnSourceAddr_Type()
)
accDialOrigDnSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnSourceAddr.setStatus("mandatory")


class _AccDialOrigDnAction_Type(Integer32):
    """Custom type accDialOrigDnAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigDnAction_Type.__name__ = "Integer32"
_AccDialOrigDnAction_Object = MibTableColumn
accDialOrigDnAction = _AccDialOrigDnAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 5, 1, 4),
    _AccDialOrigDnAction_Type()
)
accDialOrigDnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigDnAction.setStatus("mandatory")
_AccDialOrigBrTable_Object = MibTable
accDialOrigBrTable = _AccDialOrigBrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6)
)
if mibBuilder.loadTexts:
    accDialOrigBrTable.setStatus("mandatory")
_AccDialOrigBrEntry_Object = MibTableRow
accDialOrigBrEntry = _AccDialOrigBrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1)
)
accDialOrigBrEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigBrDestMacAddr"),
    (0, "ACC-MIB", "accDialOrigBrSourceMacAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigBrEntry.setStatus("mandatory")


class _AccDialOrigBrStatus_Type(Integer32):
    """Custom type accDialOrigBrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigBrStatus_Type.__name__ = "Integer32"
_AccDialOrigBrStatus_Object = MibTableColumn
accDialOrigBrStatus = _AccDialOrigBrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 1),
    _AccDialOrigBrStatus_Type()
)
accDialOrigBrStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigBrStatus.setStatus("mandatory")
_AccDialOrigBrDestMacAddr_Type = OctetString
_AccDialOrigBrDestMacAddr_Object = MibTableColumn
accDialOrigBrDestMacAddr = _AccDialOrigBrDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 2),
    _AccDialOrigBrDestMacAddr_Type()
)
accDialOrigBrDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrDestMacAddr.setStatus("mandatory")
_AccDialOrigBrSourceMacAddr_Type = OctetString
_AccDialOrigBrSourceMacAddr_Object = MibTableColumn
accDialOrigBrSourceMacAddr = _AccDialOrigBrSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 3),
    _AccDialOrigBrSourceMacAddr_Type()
)
accDialOrigBrSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrSourceMacAddr.setStatus("mandatory")


class _AccDialOrigBrAction_Type(Integer32):
    """Custom type accDialOrigBrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigBrAction_Type.__name__ = "Integer32"
_AccDialOrigBrAction_Object = MibTableColumn
accDialOrigBrAction = _AccDialOrigBrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 6, 1, 4),
    _AccDialOrigBrAction_Type()
)
accDialOrigBrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigBrAction.setStatus("mandatory")
_AccDialOrigIdpTable_Object = MibTable
accDialOrigIdpTable = _AccDialOrigIdpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7)
)
if mibBuilder.loadTexts:
    accDialOrigIdpTable.setStatus("mandatory")
_AccDialOrigIdpEntry_Object = MibTableRow
accDialOrigIdpEntry = _AccDialOrigIdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1)
)
accDialOrigIdpEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigIdpDestNet"),
    (0, "ACC-MIB", "accDialOrigIdpSourceNet"),
)
if mibBuilder.loadTexts:
    accDialOrigIdpEntry.setStatus("mandatory")


class _AccDialOrigIdpStatus_Type(Integer32):
    """Custom type accDialOrigIdpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIdpStatus_Type.__name__ = "Integer32"
_AccDialOrigIdpStatus_Object = MibTableColumn
accDialOrigIdpStatus = _AccDialOrigIdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 1),
    _AccDialOrigIdpStatus_Type()
)
accDialOrigIdpStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigIdpStatus.setStatus("mandatory")
_AccDialOrigIdpDestNet_Type = OctetString
_AccDialOrigIdpDestNet_Object = MibTableColumn
accDialOrigIdpDestNet = _AccDialOrigIdpDestNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 2),
    _AccDialOrigIdpDestNet_Type()
)
accDialOrigIdpDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpDestNet.setStatus("mandatory")
_AccDialOrigIdpSourceNet_Type = OctetString
_AccDialOrigIdpSourceNet_Object = MibTableColumn
accDialOrigIdpSourceNet = _AccDialOrigIdpSourceNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 3),
    _AccDialOrigIdpSourceNet_Type()
)
accDialOrigIdpSourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpSourceNet.setStatus("mandatory")


class _AccDialOrigIdpAction_Type(Integer32):
    """Custom type accDialOrigIdpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIdpAction_Type.__name__ = "Integer32"
_AccDialOrigIdpAction_Object = MibTableColumn
accDialOrigIdpAction = _AccDialOrigIdpAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 7, 1, 4),
    _AccDialOrigIdpAction_Type()
)
accDialOrigIdpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIdpAction.setStatus("mandatory")
_AccDialOrigIpTable_Object = MibTable
accDialOrigIpTable = _AccDialOrigIpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8)
)
if mibBuilder.loadTexts:
    accDialOrigIpTable.setStatus("mandatory")
_AccDialOrigIpEntry_Object = MibTableRow
accDialOrigIpEntry = _AccDialOrigIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1)
)
accDialOrigIpEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigIpDestAddr"),
    (0, "ACC-MIB", "accDialOrigIpDestMask"),
    (0, "ACC-MIB", "accDialOrigIpSourceAddr"),
    (0, "ACC-MIB", "accDialOrigIpSourceMask"),
    (0, "ACC-MIB", "accDialOrigIpParm"),
)
if mibBuilder.loadTexts:
    accDialOrigIpEntry.setStatus("mandatory")


class _AccDialOrigIpStatus_Type(Integer32):
    """Custom type accDialOrigIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIpStatus_Type.__name__ = "Integer32"
_AccDialOrigIpStatus_Object = MibTableColumn
accDialOrigIpStatus = _AccDialOrigIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 1),
    _AccDialOrigIpStatus_Type()
)
accDialOrigIpStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigIpStatus.setStatus("mandatory")
_AccDialOrigIpDestAddr_Type = IpAddress
_AccDialOrigIpDestAddr_Object = MibTableColumn
accDialOrigIpDestAddr = _AccDialOrigIpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 2),
    _AccDialOrigIpDestAddr_Type()
)
accDialOrigIpDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpDestAddr.setStatus("mandatory")
_AccDialOrigIpDestMask_Type = IpAddress
_AccDialOrigIpDestMask_Object = MibTableColumn
accDialOrigIpDestMask = _AccDialOrigIpDestMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 3),
    _AccDialOrigIpDestMask_Type()
)
accDialOrigIpDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpDestMask.setStatus("mandatory")
_AccDialOrigIpSourceAddr_Type = IpAddress
_AccDialOrigIpSourceAddr_Object = MibTableColumn
accDialOrigIpSourceAddr = _AccDialOrigIpSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 4),
    _AccDialOrigIpSourceAddr_Type()
)
accDialOrigIpSourceAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpSourceAddr.setStatus("mandatory")
_AccDialOrigIpSourceMask_Type = IpAddress
_AccDialOrigIpSourceMask_Object = MibTableColumn
accDialOrigIpSourceMask = _AccDialOrigIpSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 5),
    _AccDialOrigIpSourceMask_Type()
)
accDialOrigIpSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpSourceMask.setStatus("mandatory")
_AccDialOrigIpParm_Type = OctetString
_AccDialOrigIpParm_Object = MibTableColumn
accDialOrigIpParm = _AccDialOrigIpParm_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 6),
    _AccDialOrigIpParm_Type()
)
accDialOrigIpParm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpParm.setStatus("mandatory")


class _AccDialOrigIpAction_Type(Integer32):
    """Custom type accDialOrigIpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIpAction_Type.__name__ = "Integer32"
_AccDialOrigIpAction_Object = MibTableColumn
accDialOrigIpAction = _AccDialOrigIpAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 8, 1, 7),
    _AccDialOrigIpAction_Type()
)
accDialOrigIpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpAction.setStatus("mandatory")
_AccDialOrigIpxTable_Object = MibTable
accDialOrigIpxTable = _AccDialOrigIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9)
)
if mibBuilder.loadTexts:
    accDialOrigIpxTable.setStatus("mandatory")
_AccDialOrigIpxEntry_Object = MibTableRow
accDialOrigIpxEntry = _AccDialOrigIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1)
)
accDialOrigIpxEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigIpxDestNet"),
    (0, "ACC-MIB", "accDialOrigIpxSourceNet"),
)
if mibBuilder.loadTexts:
    accDialOrigIpxEntry.setStatus("mandatory")


class _AccDialOrigIpxStatus_Type(Integer32):
    """Custom type accDialOrigIpxStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigIpxStatus_Type.__name__ = "Integer32"
_AccDialOrigIpxStatus_Object = MibTableColumn
accDialOrigIpxStatus = _AccDialOrigIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 1),
    _AccDialOrigIpxStatus_Type()
)
accDialOrigIpxStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigIpxStatus.setStatus("mandatory")
_AccDialOrigIpxDestNet_Type = OctetString
_AccDialOrigIpxDestNet_Object = MibTableColumn
accDialOrigIpxDestNet = _AccDialOrigIpxDestNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 2),
    _AccDialOrigIpxDestNet_Type()
)
accDialOrigIpxDestNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxDestNet.setStatus("mandatory")
_AccDialOrigIpxSourceNet_Type = OctetString
_AccDialOrigIpxSourceNet_Object = MibTableColumn
accDialOrigIpxSourceNet = _AccDialOrigIpxSourceNet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 3),
    _AccDialOrigIpxSourceNet_Type()
)
accDialOrigIpxSourceNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxSourceNet.setStatus("mandatory")


class _AccDialOrigIpxAction_Type(Integer32):
    """Custom type accDialOrigIpxAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigIpxAction_Type.__name__ = "Integer32"
_AccDialOrigIpxAction_Object = MibTableColumn
accDialOrigIpxAction = _AccDialOrigIpxAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 9, 1, 4),
    _AccDialOrigIpxAction_Type()
)
accDialOrigIpxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigIpxAction.setStatus("mandatory")
_AccDialOrigSrTable_Object = MibTable
accDialOrigSrTable = _AccDialOrigSrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10)
)
if mibBuilder.loadTexts:
    accDialOrigSrTable.setStatus("mandatory")
_AccDialOrigSrEntry_Object = MibTableRow
accDialOrigSrEntry = _AccDialOrigSrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1)
)
accDialOrigSrEntry.setIndexNames(
    (0, "ACC-MIB", "accDialOrigSrDestMacAddr"),
    (0, "ACC-MIB", "accDialOrigSrSourceMacAddr"),
)
if mibBuilder.loadTexts:
    accDialOrigSrEntry.setStatus("mandatory")


class _AccDialOrigSrStatus_Type(Integer32):
    """Custom type accDialOrigSrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_AccDialOrigSrStatus_Type.__name__ = "Integer32"
_AccDialOrigSrStatus_Object = MibTableColumn
accDialOrigSrStatus = _AccDialOrigSrStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 1),
    _AccDialOrigSrStatus_Type()
)
accDialOrigSrStatus.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    accDialOrigSrStatus.setStatus("mandatory")
_AccDialOrigSrDestMacAddr_Type = OctetString
_AccDialOrigSrDestMacAddr_Object = MibTableColumn
accDialOrigSrDestMacAddr = _AccDialOrigSrDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 2),
    _AccDialOrigSrDestMacAddr_Type()
)
accDialOrigSrDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrDestMacAddr.setStatus("mandatory")
_AccDialOrigSrSourceMacAddr_Type = OctetString
_AccDialOrigSrSourceMacAddr_Object = MibTableColumn
accDialOrigSrSourceMacAddr = _AccDialOrigSrSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 3),
    _AccDialOrigSrSourceMacAddr_Type()
)
accDialOrigSrSourceMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrSourceMacAddr.setStatus("mandatory")


class _AccDialOrigSrAction_Type(Integer32):
    """Custom type accDialOrigSrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("disallow", 2))
    )


_AccDialOrigSrAction_Type.__name__ = "Integer32"
_AccDialOrigSrAction_Object = MibTableColumn
accDialOrigSrAction = _AccDialOrigSrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 31, 10, 1, 4),
    _AccDialOrigSrAction_Type()
)
accDialOrigSrAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accDialOrigSrAction.setStatus("mandatory")
_AccPpp_ObjectIdentity = ObjectIdentity
accPpp = _AccPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32)
)
_AccPppLinkTable_Object = MibTable
accPppLinkTable = _AccPppLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    accPppLinkTable.setStatus("mandatory")
_AccPppLinkEntry_Object = MibTableRow
accPppLinkEntry = _AccPppLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1)
)
accPppLinkEntry.setIndexNames(
    (0, "ACC-MIB", "accPppLinkIndex"),
)
if mibBuilder.loadTexts:
    accPppLinkEntry.setStatus("mandatory")
_AccPppLinkIndex_Type = Integer32
_AccPppLinkIndex_Object = MibTableColumn
accPppLinkIndex = _AccPppLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 1),
    _AccPppLinkIndex_Type()
)
accPppLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkIndex.setStatus("mandatory")
_AccPppLinkPhysicalIndex_Type = Integer32
_AccPppLinkPhysicalIndex_Object = MibTableColumn
accPppLinkPhysicalIndex = _AccPppLinkPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 2),
    _AccPppLinkPhysicalIndex_Type()
)
accPppLinkPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPhysicalIndex.setStatus("mandatory")
_AccPppLinkBadAddresses_Type = Counter32
_AccPppLinkBadAddresses_Object = MibTableColumn
accPppLinkBadAddresses = _AccPppLinkBadAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 3),
    _AccPppLinkBadAddresses_Type()
)
accPppLinkBadAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadAddresses.setStatus("mandatory")
_AccPppLinkBadControls_Type = Counter32
_AccPppLinkBadControls_Object = MibTableColumn
accPppLinkBadControls = _AccPppLinkBadControls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 4),
    _AccPppLinkBadControls_Type()
)
accPppLinkBadControls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadControls.setStatus("mandatory")
_AccPppLinkPacketTooLongs_Type = Counter32
_AccPppLinkPacketTooLongs_Object = MibTableColumn
accPppLinkPacketTooLongs = _AccPppLinkPacketTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 5),
    _AccPppLinkPacketTooLongs_Type()
)
accPppLinkPacketTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketTooLongs.setStatus("mandatory")
_AccPppLinkBadFCSs_Type = Counter32
_AccPppLinkBadFCSs_Object = MibTableColumn
accPppLinkBadFCSs = _AccPppLinkBadFCSs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 6),
    _AccPppLinkBadFCSs_Type()
)
accPppLinkBadFCSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkBadFCSs.setStatus("mandatory")
_AccPppLinkLocalMRU_Type = Integer32
_AccPppLinkLocalMRU_Object = MibTableColumn
accPppLinkLocalMRU = _AccPppLinkLocalMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 7),
    _AccPppLinkLocalMRU_Type()
)
accPppLinkLocalMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalMRU.setStatus("mandatory")
_AccPppLinkRemoteMRU_Type = Integer32
_AccPppLinkRemoteMRU_Object = MibTableColumn
accPppLinkRemoteMRU = _AccPppLinkRemoteMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 8),
    _AccPppLinkRemoteMRU_Type()
)
accPppLinkRemoteMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteMRU.setStatus("mandatory")
_AccPppLinkLocalToPeerACCMap_Type = OctetString
_AccPppLinkLocalToPeerACCMap_Object = MibTableColumn
accPppLinkLocalToPeerACCMap = _AccPppLinkLocalToPeerACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 9),
    _AccPppLinkLocalToPeerACCMap_Type()
)
accPppLinkLocalToPeerACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToPeerACCMap.setStatus("mandatory")
_AccPppLinkPeerToLocalACCMap_Type = OctetString
_AccPppLinkPeerToLocalACCMap_Object = MibTableColumn
accPppLinkPeerToLocalACCMap = _AccPppLinkPeerToLocalACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 10),
    _AccPppLinkPeerToLocalACCMap_Type()
)
accPppLinkPeerToLocalACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPeerToLocalACCMap.setStatus("mandatory")
_AccPppLinkLocalToRemotePC_Type = Integer32
_AccPppLinkLocalToRemotePC_Object = MibTableColumn
accPppLinkLocalToRemotePC = _AccPppLinkLocalToRemotePC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 11),
    _AccPppLinkLocalToRemotePC_Type()
)
accPppLinkLocalToRemotePC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToRemotePC.setStatus("mandatory")
_AccPppLinkRemoteToLocalPC_Type = Integer32
_AccPppLinkRemoteToLocalPC_Object = MibTableColumn
accPppLinkRemoteToLocalPC = _AccPppLinkRemoteToLocalPC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 12),
    _AccPppLinkRemoteToLocalPC_Type()
)
accPppLinkRemoteToLocalPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteToLocalPC.setStatus("mandatory")
_AccPppLinkLocalToRemoteAC_Type = Integer32
_AccPppLinkLocalToRemoteAC_Object = MibTableColumn
accPppLinkLocalToRemoteAC = _AccPppLinkLocalToRemoteAC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 13),
    _AccPppLinkLocalToRemoteAC_Type()
)
accPppLinkLocalToRemoteAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkLocalToRemoteAC.setStatus("mandatory")
_AccPppLinkRemoteToLocalAC_Type = Integer32
_AccPppLinkRemoteToLocalAC_Object = MibTableColumn
accPppLinkRemoteToLocalAC = _AccPppLinkRemoteToLocalAC_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 14),
    _AccPppLinkRemoteToLocalAC_Type()
)
accPppLinkRemoteToLocalAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkRemoteToLocalAC.setStatus("mandatory")
_AccPppLinkTransmit32BitFcs_Type = Integer32
_AccPppLinkTransmit32BitFcs_Object = MibTableColumn
accPppLinkTransmit32BitFcs = _AccPppLinkTransmit32BitFcs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 15),
    _AccPppLinkTransmit32BitFcs_Type()
)
accPppLinkTransmit32BitFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkTransmit32BitFcs.setStatus("mandatory")
_AccPppLinkReceive32BitFcs_Type = Integer32
_AccPppLinkReceive32BitFcs_Object = MibTableColumn
accPppLinkReceive32BitFcs = _AccPppLinkReceive32BitFcs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 16),
    _AccPppLinkReceive32BitFcs_Type()
)
accPppLinkReceive32BitFcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkReceive32BitFcs.setStatus("mandatory")


class _AccPppLinkOperStatus_Type(Integer32):
    """Custom type accPppLinkOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppLinkOperStatus_Type.__name__ = "Integer32"
_AccPppLinkOperStatus_Object = MibTableColumn
accPppLinkOperStatus = _AccPppLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 17),
    _AccPppLinkOperStatus_Type()
)
accPppLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkOperStatus.setStatus("mandatory")
_AccPppLinkPacketTooShorts_Type = Counter32
_AccPppLinkPacketTooShorts_Object = MibTableColumn
accPppLinkPacketTooShorts = _AccPppLinkPacketTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 18),
    _AccPppLinkPacketTooShorts_Type()
)
accPppLinkPacketTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketTooShorts.setStatus("mandatory")
_AccPppLinkUnknownProtocols_Type = Counter32
_AccPppLinkUnknownProtocols_Object = MibTableColumn
accPppLinkUnknownProtocols = _AccPppLinkUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 19),
    _AccPppLinkUnknownProtocols_Type()
)
accPppLinkUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkUnknownProtocols.setStatus("mandatory")
_AccPppLinkPacketInDiscards_Type = Counter32
_AccPppLinkPacketInDiscards_Object = MibTableColumn
accPppLinkPacketInDiscards = _AccPppLinkPacketInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 20),
    _AccPppLinkPacketInDiscards_Type()
)
accPppLinkPacketInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketInDiscards.setStatus("mandatory")
_AccPppLinkPacketOutDiscards_Type = Counter32
_AccPppLinkPacketOutDiscards_Object = MibTableColumn
accPppLinkPacketOutDiscards = _AccPppLinkPacketOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 1, 1, 21),
    _AccPppLinkPacketOutDiscards_Type()
)
accPppLinkPacketOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkPacketOutDiscards.setStatus("mandatory")
_AccPppLcpConfigTable_Object = MibTable
accPppLcpConfigTable = _AccPppLcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2)
)
if mibBuilder.loadTexts:
    accPppLcpConfigTable.setStatus("mandatory")
_AccPppLcpConfigEntry_Object = MibTableRow
accPppLcpConfigEntry = _AccPppLcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1)
)
accPppLcpConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppLcpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppLcpConfigEntry.setStatus("mandatory")
_AccPppLcpConfigIndex_Type = Integer32
_AccPppLcpConfigIndex_Object = MibTableColumn
accPppLcpConfigIndex = _AccPppLcpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 1),
    _AccPppLcpConfigIndex_Type()
)
accPppLcpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigIndex.setStatus("mandatory")


class _AccPppLcpConfigInitialMRU_Type(Integer32):
    """Custom type accPppLcpConfigInitialMRU based on Integer32"""
    defaultValue = 1500


_AccPppLcpConfigInitialMRU_Object = MibTableColumn
accPppLcpConfigInitialMRU = _AccPppLcpConfigInitialMRU_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 2),
    _AccPppLcpConfigInitialMRU_Type()
)
accPppLcpConfigInitialMRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigInitialMRU.setStatus("mandatory")
_AccPppLcpConfigReceiveACCMap_Type = OctetString
_AccPppLcpConfigReceiveACCMap_Object = MibTableColumn
accPppLcpConfigReceiveACCMap = _AccPppLcpConfigReceiveACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 3),
    _AccPppLcpConfigReceiveACCMap_Type()
)
accPppLcpConfigReceiveACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigReceiveACCMap.setStatus("mandatory")
_AccPppLinkConfigXmitACCMap_Type = OctetString
_AccPppLinkConfigXmitACCMap_Object = MibTableColumn
accPppLinkConfigXmitACCMap = _AccPppLinkConfigXmitACCMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 4),
    _AccPppLinkConfigXmitACCMap_Type()
)
accPppLinkConfigXmitACCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLinkConfigXmitACCMap.setStatus("mandatory")


class _AccPppLcpConfigMagicNumber_Type(Integer32):
    """Custom type accPppLcpConfigMagicNumber based on Integer32"""
    defaultValue = 1

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


_AccPppLcpConfigMagicNumber_Type.__name__ = "Integer32"
_AccPppLcpConfigMagicNumber_Object = MibTableColumn
accPppLcpConfigMagicNumber = _AccPppLcpConfigMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 5),
    _AccPppLcpConfigMagicNumber_Type()
)
accPppLcpConfigMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfigMagicNumber.setStatus("mandatory")
_AccPppLcpConfig32BitFCS_Type = Integer32
_AccPppLcpConfig32BitFCS_Object = MibTableColumn
accPppLcpConfig32BitFCS = _AccPppLcpConfig32BitFCS_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 6),
    _AccPppLcpConfig32BitFCS_Type()
)
accPppLcpConfig32BitFCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLcpConfig32BitFCS.setStatus("mandatory")


class _AccPppLcpRestartTimer_Type(Integer32):
    """Custom type accPppLcpRestartTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_AccPppLcpRestartTimer_Type.__name__ = "Integer32"
_AccPppLcpRestartTimer_Object = MibTableColumn
accPppLcpRestartTimer = _AccPppLcpRestartTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 7),
    _AccPppLcpRestartTimer_Type()
)
accPppLcpRestartTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpRestartTimer.setStatus("mandatory")


class _AccPppLcpMaxTerminate_Type(Integer32):
    """Custom type accPppLcpMaxTerminate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxTerminate_Type.__name__ = "Integer32"
_AccPppLcpMaxTerminate_Object = MibTableColumn
accPppLcpMaxTerminate = _AccPppLcpMaxTerminate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 8),
    _AccPppLcpMaxTerminate_Type()
)
accPppLcpMaxTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxTerminate.setStatus("mandatory")


class _AccPppLcpMaxConfigure_Type(Integer32):
    """Custom type accPppLcpMaxConfigure based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxConfigure_Type.__name__ = "Integer32"
_AccPppLcpMaxConfigure_Object = MibTableColumn
accPppLcpMaxConfigure = _AccPppLcpMaxConfigure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 9),
    _AccPppLcpMaxConfigure_Type()
)
accPppLcpMaxConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxConfigure.setStatus("mandatory")


class _AccPppLcpMaxFailure_Type(Integer32):
    """Custom type accPppLcpMaxFailure based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccPppLcpMaxFailure_Type.__name__ = "Integer32"
_AccPppLcpMaxFailure_Object = MibTableColumn
accPppLcpMaxFailure = _AccPppLcpMaxFailure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 10),
    _AccPppLcpMaxFailure_Type()
)
accPppLcpMaxFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMaxFailure.setStatus("mandatory")


class _AccPppLcpMonInterval_Type(Integer32):
    """Custom type accPppLcpMonInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AccPppLcpMonInterval_Type.__name__ = "Integer32"
_AccPppLcpMonInterval_Object = MibTableColumn
accPppLcpMonInterval = _AccPppLcpMonInterval_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 11),
    _AccPppLcpMonInterval_Type()
)
accPppLcpMonInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonInterval.setStatus("mandatory")


class _AccPppLcpMonEvents_Type(Integer32):
    """Custom type accPppLcpMonEvents based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccPppLcpMonEvents_Type.__name__ = "Integer32"
_AccPppLcpMonEvents_Object = MibTableColumn
accPppLcpMonEvents = _AccPppLcpMonEvents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 12),
    _AccPppLcpMonEvents_Type()
)
accPppLcpMonEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonEvents.setStatus("mandatory")


class _AccPppLcpMonThreshold_Type(Integer32):
    """Custom type accPppLcpMonThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AccPppLcpMonThreshold_Type.__name__ = "Integer32"
_AccPppLcpMonThreshold_Object = MibTableColumn
accPppLcpMonThreshold = _AccPppLcpMonThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 13),
    _AccPppLcpMonThreshold_Type()
)
accPppLcpMonThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpMonThreshold.setStatus("mandatory")


class _AccPppLcpAdminStatus_Type(Integer32):
    """Custom type accPppLcpAdminStatus based on Integer32"""
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


_AccPppLcpAdminStatus_Type.__name__ = "Integer32"
_AccPppLcpAdminStatus_Object = MibTableColumn
accPppLcpAdminStatus = _AccPppLcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 2, 1, 14),
    _AccPppLcpAdminStatus_Type()
)
accPppLcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLcpAdminStatus.setStatus("mandatory")
_AccPppLqrTable_Object = MibTable
accPppLqrTable = _AccPppLqrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3)
)
if mibBuilder.loadTexts:
    accPppLqrTable.setStatus("mandatory")
_AccPppLqrEntry_Object = MibTableRow
accPppLqrEntry = _AccPppLqrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1)
)
accPppLqrEntry.setIndexNames(
    (0, "ACC-MIB", "accPppLqrIndex"),
)
if mibBuilder.loadTexts:
    accPppLqrEntry.setStatus("mandatory")
_AccPppLqrIndex_Type = Integer32
_AccPppLqrIndex_Object = MibTableColumn
accPppLqrIndex = _AccPppLqrIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 1),
    _AccPppLqrIndex_Type()
)
accPppLqrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrIndex.setStatus("mandatory")


class _AccPppLqrQuality_Type(Integer32):
    """Custom type accPppLqrQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_AccPppLqrQuality_Type.__name__ = "Integer32"
_AccPppLqrQuality_Object = MibTableColumn
accPppLqrQuality = _AccPppLqrQuality_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 2),
    _AccPppLqrQuality_Type()
)
accPppLqrQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrQuality.setStatus("mandatory")
_AccPppLqrInGoodOctets_Type = Counter32
_AccPppLqrInGoodOctets_Object = MibTableColumn
accPppLqrInGoodOctets = _AccPppLqrInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 3),
    _AccPppLqrInGoodOctets_Type()
)
accPppLqrInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrInGoodOctets.setStatus("mandatory")
_AccPppLqrLocalPeriod_Type = Integer32
_AccPppLqrLocalPeriod_Object = MibTableColumn
accPppLqrLocalPeriod = _AccPppLqrLocalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 4),
    _AccPppLqrLocalPeriod_Type()
)
accPppLqrLocalPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrLocalPeriod.setStatus("mandatory")
_AccPppLqrRemotePeriod_Type = Integer32
_AccPppLqrRemotePeriod_Object = MibTableColumn
accPppLqrRemotePeriod = _AccPppLqrRemotePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 5),
    _AccPppLqrRemotePeriod_Type()
)
accPppLqrRemotePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrRemotePeriod.setStatus("mandatory")
_AccPppLqrOutLQRs_Type = Counter32
_AccPppLqrOutLQRs_Object = MibTableColumn
accPppLqrOutLQRs = _AccPppLqrOutLQRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 6),
    _AccPppLqrOutLQRs_Type()
)
accPppLqrOutLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrOutLQRs.setStatus("mandatory")
_AccPppLqrInLQRs_Type = Counter32
_AccPppLqrInLQRs_Object = MibTableColumn
accPppLqrInLQRs = _AccPppLqrInLQRs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 3, 1, 7),
    _AccPppLqrInLQRs_Type()
)
accPppLqrInLQRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrInLQRs.setStatus("mandatory")
_AccPppLqrConfigTable_Object = MibTable
accPppLqrConfigTable = _AccPppLqrConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4)
)
if mibBuilder.loadTexts:
    accPppLqrConfigTable.setStatus("mandatory")
_AccPppLqrConfigEntry_Object = MibTableRow
accPppLqrConfigEntry = _AccPppLqrConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1)
)
accPppLqrConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppLqrConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppLqrConfigEntry.setStatus("mandatory")
_AccPppLqrConfigIndex_Type = Integer32
_AccPppLqrConfigIndex_Object = MibTableColumn
accPppLqrConfigIndex = _AccPppLqrConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 1),
    _AccPppLqrConfigIndex_Type()
)
accPppLqrConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppLqrConfigIndex.setStatus("mandatory")


class _AccPppLqrConfigPeriod_Type(Integer32):
    """Custom type accPppLqrConfigPeriod based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483648),
    )


_AccPppLqrConfigPeriod_Type.__name__ = "Integer32"
_AccPppLqrConfigPeriod_Object = MibTableColumn
accPppLqrConfigPeriod = _AccPppLqrConfigPeriod_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 2),
    _AccPppLqrConfigPeriod_Type()
)
accPppLqrConfigPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLqrConfigPeriod.setStatus("mandatory")


class _AccPppLqrConfigStatus_Type(Integer32):
    """Custom type accPppLqrConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppLqrConfigStatus_Type.__name__ = "Integer32"
_AccPppLqrConfigStatus_Object = MibTableColumn
accPppLqrConfigStatus = _AccPppLqrConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 4, 1, 3),
    _AccPppLqrConfigStatus_Type()
)
accPppLqrConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppLqrConfigStatus.setStatus("mandatory")
_AccPppIpcpTable_Object = MibTable
accPppIpcpTable = _AccPppIpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5)
)
if mibBuilder.loadTexts:
    accPppIpcpTable.setStatus("mandatory")
_AccPppIpcpEntry_Object = MibTableRow
accPppIpcpEntry = _AccPppIpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1)
)
accPppIpcpEntry.setIndexNames(
    (0, "ACC-MIB", "accPppIpcpIndex"),
)
if mibBuilder.loadTexts:
    accPppIpcpEntry.setStatus("mandatory")
_AccPppIpcpIndex_Type = Integer32
_AccPppIpcpIndex_Object = MibTableColumn
accPppIpcpIndex = _AccPppIpcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 1),
    _AccPppIpcpIndex_Type()
)
accPppIpcpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpIndex.setStatus("mandatory")


class _AccPppIpcpLocalToRemoteCompressionProtocol_Type(Integer32):
    """Custom type accPppIpcpLocalToRemoteCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpLocalToRemoteCompressionProtocol_Type.__name__ = "Integer32"
_AccPppIpcpLocalToRemoteCompressionProtocol_Object = MibTableColumn
accPppIpcpLocalToRemoteCompressionProtocol = _AccPppIpcpLocalToRemoteCompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 2),
    _AccPppIpcpLocalToRemoteCompressionProtocol_Type()
)
accPppIpcpLocalToRemoteCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpLocalToRemoteCompressionProtocol.setStatus("mandatory")


class _AccPppIpcpRemoteToLocalCompressionProtocol_Type(Integer32):
    """Custom type accPppIpcpRemoteToLocalCompressionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpRemoteToLocalCompressionProtocol_Type.__name__ = "Integer32"
_AccPppIpcpRemoteToLocalCompressionProtocol_Object = MibTableColumn
accPppIpcpRemoteToLocalCompressionProtocol = _AccPppIpcpRemoteToLocalCompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 3),
    _AccPppIpcpRemoteToLocalCompressionProtocol_Type()
)
accPppIpcpRemoteToLocalCompressionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpRemoteToLocalCompressionProtocol.setStatus("mandatory")


class _AccPppIpcpRemoteMaxSlotId_Type(Integer32):
    """Custom type accPppIpcpRemoteMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccPppIpcpRemoteMaxSlotId_Type.__name__ = "Integer32"
_AccPppIpcpRemoteMaxSlotId_Object = MibTableColumn
accPppIpcpRemoteMaxSlotId = _AccPppIpcpRemoteMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 4),
    _AccPppIpcpRemoteMaxSlotId_Type()
)
accPppIpcpRemoteMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpRemoteMaxSlotId.setStatus("mandatory")


class _AccPppIpcpLocalMaxSlotId_Type(Integer32):
    """Custom type accPppIpcpLocalMaxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccPppIpcpLocalMaxSlotId_Type.__name__ = "Integer32"
_AccPppIpcpLocalMaxSlotId_Object = MibTableColumn
accPppIpcpLocalMaxSlotId = _AccPppIpcpLocalMaxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 5),
    _AccPppIpcpLocalMaxSlotId_Type()
)
accPppIpcpLocalMaxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpLocalMaxSlotId.setStatus("mandatory")


class _AccPppIpOperStatus_Type(Integer32):
    """Custom type accPppIpOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppIpOperStatus_Type.__name__ = "Integer32"
_AccPppIpOperStatus_Object = MibTableColumn
accPppIpOperStatus = _AccPppIpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 5, 1, 6),
    _AccPppIpOperStatus_Type()
)
accPppIpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpOperStatus.setStatus("mandatory")
_AccPppIpcpConfigTable_Object = MibTable
accPppIpcpConfigTable = _AccPppIpcpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6)
)
if mibBuilder.loadTexts:
    accPppIpcpConfigTable.setStatus("mandatory")
_AccPppIpcpConfigEntry_Object = MibTableRow
accPppIpcpConfigEntry = _AccPppIpcpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1)
)
accPppIpcpConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppIpcpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppIpcpConfigEntry.setStatus("mandatory")
_AccPppIpcpConfigIndex_Type = Integer32
_AccPppIpcpConfigIndex_Object = MibTableColumn
accPppIpcpConfigIndex = _AccPppIpcpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 1),
    _AccPppIpcpConfigIndex_Type()
)
accPppIpcpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpcpConfigIndex.setStatus("mandatory")


class _AccPppIpcpConfigCompression_Type(Integer32):
    """Custom type accPppIpcpConfigCompression based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vj-tcp", 2))
    )


_AccPppIpcpConfigCompression_Type.__name__ = "Integer32"
_AccPppIpcpConfigCompression_Object = MibTableColumn
accPppIpcpConfigCompression = _AccPppIpcpConfigCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 2),
    _AccPppIpcpConfigCompression_Type()
)
accPppIpcpConfigCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpcpConfigCompression.setStatus("mandatory")


class _AccPppIpcpConfigStatus_Type(Integer32):
    """Custom type accPppIpcpConfigStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppIpcpConfigStatus_Type.__name__ = "Integer32"
_AccPppIpcpConfigStatus_Object = MibTableColumn
accPppIpcpConfigStatus = _AccPppIpcpConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 6, 1, 3),
    _AccPppIpcpConfigStatus_Type()
)
accPppIpcpConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpcpConfigStatus.setStatus("mandatory")
_AccPppBncpTable_Object = MibTable
accPppBncpTable = _AccPppBncpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7)
)
if mibBuilder.loadTexts:
    accPppBncpTable.setStatus("mandatory")
_AccPppBncpEntry_Object = MibTableRow
accPppBncpEntry = _AccPppBncpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1)
)
accPppBncpEntry.setIndexNames(
    (0, "ACC-MIB", "accPppBncpIndex"),
)
if mibBuilder.loadTexts:
    accPppBncpEntry.setStatus("mandatory")
_AccPppBncpIndex_Type = Integer32
_AccPppBncpIndex_Object = MibTableColumn
accPppBncpIndex = _AccPppBncpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 1),
    _AccPppBncpIndex_Type()
)
accPppBncpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpIndex.setStatus("mandatory")


class _AccPppBncpLocalToRemoteTinygramCompression_Type(Integer32):
    """Custom type accPppBncpLocalToRemoteTinygramCompression based on Integer32"""
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


_AccPppBncpLocalToRemoteTinygramCompression_Type.__name__ = "Integer32"
_AccPppBncpLocalToRemoteTinygramCompression_Object = MibTableColumn
accPppBncpLocalToRemoteTinygramCompression = _AccPppBncpLocalToRemoteTinygramCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 2),
    _AccPppBncpLocalToRemoteTinygramCompression_Type()
)
accPppBncpLocalToRemoteTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpLocalToRemoteTinygramCompression.setStatus("mandatory")


class _AccPppBncpRemoteToLocalTinygramCompression_Type(Integer32):
    """Custom type accPppBncpRemoteToLocalTinygramCompression based on Integer32"""
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


_AccPppBncpRemoteToLocalTinygramCompression_Type.__name__ = "Integer32"
_AccPppBncpRemoteToLocalTinygramCompression_Object = MibTableColumn
accPppBncpRemoteToLocalTinygramCompression = _AccPppBncpRemoteToLocalTinygramCompression_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 3),
    _AccPppBncpRemoteToLocalTinygramCompression_Type()
)
accPppBncpRemoteToLocalTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpRemoteToLocalTinygramCompression.setStatus("mandatory")


class _AccPppBncpLocalToRemoteLanId_Type(Integer32):
    """Custom type accPppBncpLocalToRemoteLanId based on Integer32"""
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


_AccPppBncpLocalToRemoteLanId_Type.__name__ = "Integer32"
_AccPppBncpLocalToRemoteLanId_Object = MibTableColumn
accPppBncpLocalToRemoteLanId = _AccPppBncpLocalToRemoteLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 4),
    _AccPppBncpLocalToRemoteLanId_Type()
)
accPppBncpLocalToRemoteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpLocalToRemoteLanId.setStatus("mandatory")


class _AccPppBncpRemoteToLocalLanId_Type(Integer32):
    """Custom type accPppBncpRemoteToLocalLanId based on Integer32"""
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


_AccPppBncpRemoteToLocalLanId_Type.__name__ = "Integer32"
_AccPppBncpRemoteToLocalLanId_Object = MibTableColumn
accPppBncpRemoteToLocalLanId = _AccPppBncpRemoteToLocalLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 7, 1, 5),
    _AccPppBncpRemoteToLocalLanId_Type()
)
accPppBncpRemoteToLocalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpRemoteToLocalLanId.setStatus("mandatory")
_AccPppBncpConfigTable_Object = MibTable
accPppBncpConfigTable = _AccPppBncpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8)
)
if mibBuilder.loadTexts:
    accPppBncpConfigTable.setStatus("mandatory")
_AccPppBncpConfigEntry_Object = MibTableRow
accPppBncpConfigEntry = _AccPppBncpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1)
)
accPppBncpConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppBncpConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppBncpConfigEntry.setStatus("mandatory")
_AccPppBncpConfigIndex_Type = Integer32
_AccPppBncpConfigIndex_Object = MibTableColumn
accPppBncpConfigIndex = _AccPppBncpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 1),
    _AccPppBncpConfigIndex_Type()
)
accPppBncpConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppBncpConfigIndex.setStatus("mandatory")


class _AccPppBncpConfigTinygram_Type(Integer32):
    """Custom type accPppBncpConfigTinygram based on Integer32"""
    defaultValue = 2

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


_AccPppBncpConfigTinygram_Type.__name__ = "Integer32"
_AccPppBncpConfigTinygram_Object = MibTableColumn
accPppBncpConfigTinygram = _AccPppBncpConfigTinygram_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 2),
    _AccPppBncpConfigTinygram_Type()
)
accPppBncpConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigTinygram.setStatus("mandatory")


class _AccPppBncpConfigRingId_Type(Integer32):
    """Custom type accPppBncpConfigRingId based on Integer32"""
    defaultValue = 1

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


_AccPppBncpConfigRingId_Type.__name__ = "Integer32"
_AccPppBncpConfigRingId_Object = MibTableColumn
accPppBncpConfigRingId = _AccPppBncpConfigRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 3),
    _AccPppBncpConfigRingId_Type()
)
accPppBncpConfigRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigRingId.setStatus("mandatory")


class _AccPppBncpConfigLineId_Type(Integer32):
    """Custom type accPppBncpConfigLineId based on Integer32"""
    defaultValue = 1

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


_AccPppBncpConfigLineId_Type.__name__ = "Integer32"
_AccPppBncpConfigLineId_Object = MibTableColumn
accPppBncpConfigLineId = _AccPppBncpConfigLineId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 4),
    _AccPppBncpConfigLineId_Type()
)
accPppBncpConfigLineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigLineId.setStatus("mandatory")


class _AccPppBncpConfigLanId_Type(Integer32):
    """Custom type accPppBncpConfigLanId based on Integer32"""
    defaultValue = 1

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


_AccPppBncpConfigLanId_Type.__name__ = "Integer32"
_AccPppBncpConfigLanId_Object = MibTableColumn
accPppBncpConfigLanId = _AccPppBncpConfigLanId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 5),
    _AccPppBncpConfigLanId_Type()
)
accPppBncpConfigLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigLanId.setStatus("mandatory")


class _AccPppBncpConfigAdminStatus_Type(Integer32):
    """Custom type accPppBncpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppBncpConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppBncpConfigAdminStatus_Object = MibTableColumn
accPppBncpConfigAdminStatus = _AccPppBncpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 8, 1, 6),
    _AccPppBncpConfigAdminStatus_Type()
)
accPppBncpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppBncpConfigAdminStatus.setStatus("mandatory")
_AccPppXnsTable_Object = MibTable
accPppXnsTable = _AccPppXnsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9)
)
if mibBuilder.loadTexts:
    accPppXnsTable.setStatus("mandatory")
_AccPppXnsEntry_Object = MibTableRow
accPppXnsEntry = _AccPppXnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1)
)
accPppXnsEntry.setIndexNames(
    (0, "ACC-MIB", "accPppXnsIndex"),
)
if mibBuilder.loadTexts:
    accPppXnsEntry.setStatus("mandatory")
_AccPppXnsIndex_Type = Integer32
_AccPppXnsIndex_Object = MibTableColumn
accPppXnsIndex = _AccPppXnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1, 1),
    _AccPppXnsIndex_Type()
)
accPppXnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsIndex.setStatus("mandatory")


class _AccPppXnsOperStatus_Type(Integer32):
    """Custom type accPppXnsOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppXnsOperStatus_Type.__name__ = "Integer32"
_AccPppXnsOperStatus_Object = MibTableColumn
accPppXnsOperStatus = _AccPppXnsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 9, 1, 2),
    _AccPppXnsOperStatus_Type()
)
accPppXnsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsOperStatus.setStatus("mandatory")
_AccPppXnsConfigTable_Object = MibTable
accPppXnsConfigTable = _AccPppXnsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10)
)
if mibBuilder.loadTexts:
    accPppXnsConfigTable.setStatus("mandatory")
_AccPppXnsConfigEntry_Object = MibTableRow
accPppXnsConfigEntry = _AccPppXnsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1)
)
accPppXnsConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppXnsConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppXnsConfigEntry.setStatus("mandatory")
_AccPppXnsConfigIndex_Type = Integer32
_AccPppXnsConfigIndex_Object = MibTableColumn
accPppXnsConfigIndex = _AccPppXnsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1, 1),
    _AccPppXnsConfigIndex_Type()
)
accPppXnsConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppXnsConfigIndex.setStatus("mandatory")


class _AccPppXnsConfigAdminStatus_Type(Integer32):
    """Custom type accPppXnsConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppXnsConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppXnsConfigAdminStatus_Object = MibTableColumn
accPppXnsConfigAdminStatus = _AccPppXnsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 10, 1, 3),
    _AccPppXnsConfigAdminStatus_Type()
)
accPppXnsConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppXnsConfigAdminStatus.setStatus("mandatory")
_AccPppIpxTable_Object = MibTable
accPppIpxTable = _AccPppIpxTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11)
)
if mibBuilder.loadTexts:
    accPppIpxTable.setStatus("mandatory")
_AccPppIpxEntry_Object = MibTableRow
accPppIpxEntry = _AccPppIpxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1)
)
accPppIpxEntry.setIndexNames(
    (0, "ACC-MIB", "accPppIpxIndex"),
)
if mibBuilder.loadTexts:
    accPppIpxEntry.setStatus("mandatory")
_AccPppIpxIndex_Type = Integer32
_AccPppIpxIndex_Object = MibTableColumn
accPppIpxIndex = _AccPppIpxIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1, 1),
    _AccPppIpxIndex_Type()
)
accPppIpxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxIndex.setStatus("mandatory")


class _AccPppIpxOperStatus_Type(Integer32):
    """Custom type accPppIpxOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppIpxOperStatus_Type.__name__ = "Integer32"
_AccPppIpxOperStatus_Object = MibTableColumn
accPppIpxOperStatus = _AccPppIpxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 11, 1, 2),
    _AccPppIpxOperStatus_Type()
)
accPppIpxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxOperStatus.setStatus("mandatory")
_AccPppIpxConfigTable_Object = MibTable
accPppIpxConfigTable = _AccPppIpxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12)
)
if mibBuilder.loadTexts:
    accPppIpxConfigTable.setStatus("mandatory")
_AccPppIpxConfigEntry_Object = MibTableRow
accPppIpxConfigEntry = _AccPppIpxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1)
)
accPppIpxConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppIpxConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppIpxConfigEntry.setStatus("mandatory")
_AccPppIpxConfigIndex_Type = Integer32
_AccPppIpxConfigIndex_Object = MibTableColumn
accPppIpxConfigIndex = _AccPppIpxConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1, 1),
    _AccPppIpxConfigIndex_Type()
)
accPppIpxConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppIpxConfigIndex.setStatus("mandatory")


class _AccPppIpxConfigAdminStatus_Type(Integer32):
    """Custom type accPppIpxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppIpxConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppIpxConfigAdminStatus_Object = MibTableColumn
accPppIpxConfigAdminStatus = _AccPppIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 12, 1, 3),
    _AccPppIpxConfigAdminStatus_Type()
)
accPppIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppIpxConfigAdminStatus.setStatus("mandatory")
_AccPppAppleTable_Object = MibTable
accPppAppleTable = _AccPppAppleTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13)
)
if mibBuilder.loadTexts:
    accPppAppleTable.setStatus("mandatory")
_AccPppAppleEntry_Object = MibTableRow
accPppAppleEntry = _AccPppAppleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1)
)
accPppAppleEntry.setIndexNames(
    (0, "ACC-MIB", "accPppAppleIndex"),
)
if mibBuilder.loadTexts:
    accPppAppleEntry.setStatus("mandatory")
_AccPppAppleIndex_Type = Integer32
_AccPppAppleIndex_Object = MibTableColumn
accPppAppleIndex = _AccPppAppleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1, 1),
    _AccPppAppleIndex_Type()
)
accPppAppleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleIndex.setStatus("mandatory")


class _AccPppAppleOperStatus_Type(Integer32):
    """Custom type accPppAppleOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppAppleOperStatus_Type.__name__ = "Integer32"
_AccPppAppleOperStatus_Object = MibTableColumn
accPppAppleOperStatus = _AccPppAppleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 13, 1, 2),
    _AccPppAppleOperStatus_Type()
)
accPppAppleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleOperStatus.setStatus("mandatory")
_AccPppAppleConfigTable_Object = MibTable
accPppAppleConfigTable = _AccPppAppleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14)
)
if mibBuilder.loadTexts:
    accPppAppleConfigTable.setStatus("mandatory")
_AccPppAppleConfigEntry_Object = MibTableRow
accPppAppleConfigEntry = _AccPppAppleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1)
)
accPppAppleConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppAppleConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppAppleConfigEntry.setStatus("mandatory")
_AccPppAppleConfigIndex_Type = Integer32
_AccPppAppleConfigIndex_Object = MibTableColumn
accPppAppleConfigIndex = _AccPppAppleConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1, 1),
    _AccPppAppleConfigIndex_Type()
)
accPppAppleConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppAppleConfigIndex.setStatus("mandatory")


class _AccPppAppleConfigAdminStatus_Type(Integer32):
    """Custom type accPppAppleConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppAppleConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppAppleConfigAdminStatus_Object = MibTableColumn
accPppAppleConfigAdminStatus = _AccPppAppleConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 14, 1, 3),
    _AccPppAppleConfigAdminStatus_Type()
)
accPppAppleConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppAppleConfigAdminStatus.setStatus("mandatory")
_AccPppDecTable_Object = MibTable
accPppDecTable = _AccPppDecTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15)
)
if mibBuilder.loadTexts:
    accPppDecTable.setStatus("mandatory")
_AccPppDecEntry_Object = MibTableRow
accPppDecEntry = _AccPppDecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1)
)
accPppDecEntry.setIndexNames(
    (0, "ACC-MIB", "accPppDecIndex"),
)
if mibBuilder.loadTexts:
    accPppDecEntry.setStatus("mandatory")
_AccPppDecIndex_Type = Integer32
_AccPppDecIndex_Object = MibTableColumn
accPppDecIndex = _AccPppDecIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1, 1),
    _AccPppDecIndex_Type()
)
accPppDecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecIndex.setStatus("mandatory")


class _AccPppDecOperStatus_Type(Integer32):
    """Custom type accPppDecOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppDecOperStatus_Type.__name__ = "Integer32"
_AccPppDecOperStatus_Object = MibTableColumn
accPppDecOperStatus = _AccPppDecOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 15, 1, 2),
    _AccPppDecOperStatus_Type()
)
accPppDecOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecOperStatus.setStatus("mandatory")
_AccPppDecConfigTable_Object = MibTable
accPppDecConfigTable = _AccPppDecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16)
)
if mibBuilder.loadTexts:
    accPppDecConfigTable.setStatus("mandatory")
_AccPppDecConfigEntry_Object = MibTableRow
accPppDecConfigEntry = _AccPppDecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1)
)
accPppDecConfigEntry.setIndexNames(
    (0, "ACC-MIB", "accPppDecConfigIndex"),
)
if mibBuilder.loadTexts:
    accPppDecConfigEntry.setStatus("mandatory")
_AccPppDecConfigIndex_Type = Integer32
_AccPppDecConfigIndex_Object = MibTableColumn
accPppDecConfigIndex = _AccPppDecConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1, 1),
    _AccPppDecConfigIndex_Type()
)
accPppDecConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppDecConfigIndex.setStatus("mandatory")


class _AccPppDecConfigAdminStatus_Type(Integer32):
    """Custom type accPppDecConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AccPppDecConfigAdminStatus_Type.__name__ = "Integer32"
_AccPppDecConfigAdminStatus_Object = MibTableColumn
accPppDecConfigAdminStatus = _AccPppDecConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 16, 1, 3),
    _AccPppDecConfigAdminStatus_Type()
)
accPppDecConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppDecConfigAdminStatus.setStatus("mandatory")
_AccPppProtocolTable_Object = MibTable
accPppProtocolTable = _AccPppProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17)
)
if mibBuilder.loadTexts:
    accPppProtocolTable.setStatus("mandatory")
_AccPppProtocolEntry_Object = MibTableRow
accPppProtocolEntry = _AccPppProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1)
)
accPppProtocolEntry.setIndexNames(
    (0, "ACC-MIB", "accPppProtocolIndex"),
)
if mibBuilder.loadTexts:
    accPppProtocolEntry.setStatus("mandatory")
_AccPppProtocolIndex_Type = Integer32
_AccPppProtocolIndex_Object = MibTableColumn
accPppProtocolIndex = _AccPppProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 1),
    _AccPppProtocolIndex_Type()
)
accPppProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolIndex.setStatus("mandatory")


class _AccPppProtocolProtocol_Type(Integer32):
    """Custom type accPppProtocolProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(33,
              35,
              37,
              39,
              41,
              43,
              49,
              53,
              61,
              253)
        )
    )
    namedValues = NamedValues(
        *(("appletalk", 41),
          ("bridge", 49),
          ("ccp", 253),
          ("decnet", 39),
          ("idp", 37),
          ("ip", 33),
          ("ipx", 43),
          ("multilink", 61),
          ("osi", 35),
          ("vines", 53))
    )


_AccPppProtocolProtocol_Type.__name__ = "Integer32"
_AccPppProtocolProtocol_Object = MibTableColumn
accPppProtocolProtocol = _AccPppProtocolProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 2),
    _AccPppProtocolProtocol_Type()
)
accPppProtocolProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolProtocol.setStatus("mandatory")


class _AccPppProtocolAdminStatus_Type(Integer32):
    """Custom type accPppProtocolAdminStatus based on Integer32"""
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


_AccPppProtocolAdminStatus_Type.__name__ = "Integer32"
_AccPppProtocolAdminStatus_Object = MibTableColumn
accPppProtocolAdminStatus = _AccPppProtocolAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 3),
    _AccPppProtocolAdminStatus_Type()
)
accPppProtocolAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolAdminStatus.setStatus("mandatory")


class _AccPppProtocolOperStatus_Type(Integer32):
    """Custom type accPppProtocolOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("ack-rcvd", 8),
          ("ack-sent", 9),
          ("closed", 3),
          ("closing", 5),
          ("initial", 1),
          ("opened", 10),
          ("req-sent", 7),
          ("starting", 2),
          ("stopped", 4),
          ("stopping", 6))
    )


_AccPppProtocolOperStatus_Type.__name__ = "Integer32"
_AccPppProtocolOperStatus_Object = MibTableColumn
accPppProtocolOperStatus = _AccPppProtocolOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 17, 1, 4),
    _AccPppProtocolOperStatus_Type()
)
accPppProtocolOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPppProtocolOperStatus.setStatus("mandatory")
_AccPppMsg_ObjectIdentity = ObjectIdentity
accPppMsg = _AccPppMsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 18)
)


class _AccPppMsgLevel_Type(Integer32):
    """Custom type accPppMsgLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccPppMsgLevel_Type.__name__ = "Integer32"
_AccPppMsgLevel_Object = MibScalar
accPppMsgLevel = _AccPppMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 32, 18, 1),
    _AccPppMsgLevel_Type()
)
accPppMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPppMsgLevel.setStatus("mandatory")
_AccFlash_ObjectIdentity = ObjectIdentity
accFlash = _AccFlash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33)
)
_AccFlashTable_Object = MibTable
accFlashTable = _AccFlashTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1)
)
if mibBuilder.loadTexts:
    accFlashTable.setStatus("mandatory")
_AccFlashEntry_Object = MibTableRow
accFlashEntry = _AccFlashEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1, 1)
)
accFlashEntry.setIndexNames(
    (0, "ACC-MIB", "accFlashIndex"),
)
if mibBuilder.loadTexts:
    accFlashEntry.setStatus("mandatory")
_AccFlashIndex_Type = Integer32
_AccFlashIndex_Object = MibTableColumn
accFlashIndex = _AccFlashIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1, 1, 1),
    _AccFlashIndex_Type()
)
accFlashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFlashIndex.setStatus("mandatory")


class _AccFlashFiDisp_Type(Integer32):
    """Custom type accFlashFiDisp based on Integer32"""
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
        *(("boot-flash", 2),
          ("boot-rom", 1),
          ("invalid", 4),
          ("valid", 3))
    )


_AccFlashFiDisp_Type.__name__ = "Integer32"
_AccFlashFiDisp_Object = MibTableColumn
accFlashFiDisp = _AccFlashFiDisp_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1, 1, 2),
    _AccFlashFiDisp_Type()
)
accFlashFiDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFlashFiDisp.setStatus("mandatory")
_AccFlashCksum_Type = Integer32
_AccFlashCksum_Object = MibTableColumn
accFlashCksum = _AccFlashCksum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1, 1, 3),
    _AccFlashCksum_Type()
)
accFlashCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFlashCksum.setStatus("mandatory")
_AccFlashLength_Type = Integer32
_AccFlashLength_Object = MibTableColumn
accFlashLength = _AccFlashLength_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 33, 1, 1, 4),
    _AccFlashLength_Type()
)
accFlashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accFlashLength.setStatus("mandatory")
_AccXBr_ObjectIdentity = ObjectIdentity
accXBr = _AccXBr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34)
)
_AccXBridge_ObjectIdentity = ObjectIdentity
accXBridge = _AccXBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1)
)


class _AccXBridgeStatus_Type(Integer32):
    """Custom type accXBridgeStatus based on Integer32"""
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


_AccXBridgeStatus_Type.__name__ = "Integer32"
_AccXBridgeStatus_Object = MibScalar
accXBridgeStatus = _AccXBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1, 1),
    _AccXBridgeStatus_Type()
)
accXBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXBridgeStatus.setStatus("mandatory")
_AccXBridgeRingId_Type = Integer32
_AccXBridgeRingId_Object = MibScalar
accXBridgeRingId = _AccXBridgeRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1, 2),
    _AccXBridgeRingId_Type()
)
accXBridgeRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXBridgeRingId.setStatus("mandatory")
_AccExtProtImp_ObjectIdentity = ObjectIdentity
accExtProtImp = _AccExtProtImp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35)
)
_AccExtProtImpTable_Object = MibTable
accExtProtImpTable = _AccExtProtImpTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1)
)
if mibBuilder.loadTexts:
    accExtProtImpTable.setStatus("mandatory")
_AccExtProtImpEntry_Object = MibTableRow
accExtProtImpEntry = _AccExtProtImpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1)
)
accExtProtImpEntry.setIndexNames(
    (0, "ACC-MIB", "accExtProtImpProtocol"),
)
if mibBuilder.loadTexts:
    accExtProtImpEntry.setStatus("mandatory")


class _AccExtProtImpProtocol_Type(Integer32):
    """Custom type accExtProtImpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("rip", 1),
          ("static", 3))
    )


_AccExtProtImpProtocol_Type.__name__ = "Integer32"
_AccExtProtImpProtocol_Object = MibTableColumn
accExtProtImpProtocol = _AccExtProtImpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1, 1),
    _AccExtProtImpProtocol_Type()
)
accExtProtImpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accExtProtImpProtocol.setStatus("mandatory")


class _AccExtProtImpAllowed_Type(Integer32):
    """Custom type accExtProtImpAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccExtProtImpAllowed_Type.__name__ = "Integer32"
_AccExtProtImpAllowed_Object = MibTableColumn
accExtProtImpAllowed = _AccExtProtImpAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 35, 1, 1, 2),
    _AccExtProtImpAllowed_Type()
)
accExtProtImpAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accExtProtImpAllowed.setStatus("mandatory")
_AccIsdn_ObjectIdentity = ObjectIdentity
accIsdn = _AccIsdn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36)
)
_AccIsdnDsl_ObjectIdentity = ObjectIdentity
accIsdnDsl = _AccIsdnDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 1)
)


class _AccIsdnDslIndex_Type(Integer32):
    """Custom type accIsdnDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnDslIndex_Type.__name__ = "Integer32"
_AccIsdnDslIndex_Object = MibTableColumn
accIsdnDslIndex = _AccIsdnDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 1, 1),
    _AccIsdnDslIndex_Type()
)
accIsdnDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnDslIndex.setStatus("deprecated")
_AccIsdnSubTable_Object = MibTable
accIsdnSubTable = _AccIsdnSubTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2)
)
if mibBuilder.loadTexts:
    accIsdnSubTable.setStatus("deprecated")
_AccIsdnSubEntry_Object = MibTableRow
accIsdnSubEntry = _AccIsdnSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1)
)
accIsdnSubEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnSubEntry.setStatus("deprecated")


class _AccIsdnSubSwitchType_Type(Integer32):
    """Custom type accIsdnSubSwitchType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("bri-1tr6", 8),
          ("bri-5ess", 2),
          ("bri-ccitt", 10),
          ("bri-dms100", 3),
          ("bri-kdd", 6),
          ("bri-net3", 1),
          ("bri-ni1", 9),
          ("bri-ntt", 7),
          ("bri-vn2", 4),
          ("bri-vn3", 5))
    )


_AccIsdnSubSwitchType_Type.__name__ = "Integer32"
_AccIsdnSubSwitchType_Object = MibTableColumn
accIsdnSubSwitchType = _AccIsdnSubSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 1),
    _AccIsdnSubSwitchType_Type()
)
accIsdnSubSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubSwitchType.setStatus("deprecated")


class _AccIsdnSubChannelMode_Type(Integer32):
    """Custom type accIsdnSubChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cm-1b-plus-d", 1),
          ("cm-1h-plus-d", 3),
          ("cm-2b-plus-d", 2))
    )


_AccIsdnSubChannelMode_Type.__name__ = "Integer32"
_AccIsdnSubChannelMode_Object = MibTableColumn
accIsdnSubChannelMode = _AccIsdnSubChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 2),
    _AccIsdnSubChannelMode_Type()
)
accIsdnSubChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubChannelMode.setStatus("deprecated")


class _AccIsdnSubAdminStatus_Type(Integer32):
    """Custom type accIsdnSubAdminStatus based on Integer32"""
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


_AccIsdnSubAdminStatus_Type.__name__ = "Integer32"
_AccIsdnSubAdminStatus_Object = MibTableColumn
accIsdnSubAdminStatus = _AccIsdnSubAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 3),
    _AccIsdnSubAdminStatus_Type()
)
accIsdnSubAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubAdminStatus.setStatus("deprecated")


class _AccIsdnSubDiagLevel_Type(Integer32):
    """Custom type accIsdnSubDiagLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AccIsdnSubDiagLevel_Type.__name__ = "Integer32"
_AccIsdnSubDiagLevel_Object = MibTableColumn
accIsdnSubDiagLevel = _AccIsdnSubDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 4),
    _AccIsdnSubDiagLevel_Type()
)
accIsdnSubDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubDiagLevel.setStatus("deprecated")


class _AccIsdnSubManualTei_Type(Integer32):
    """Custom type accIsdnSubManualTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AccIsdnSubManualTei_Type.__name__ = "Integer32"
_AccIsdnSubManualTei_Object = MibTableColumn
accIsdnSubManualTei = _AccIsdnSubManualTei_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 2, 1, 5),
    _AccIsdnSubManualTei_Type()
)
accIsdnSubManualTei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSubManualTei.setStatus("deprecated")
_AccIsdnStatTable_Object = MibTable
accIsdnStatTable = _AccIsdnStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3)
)
if mibBuilder.loadTexts:
    accIsdnStatTable.setStatus("deprecated")
_AccIsdnStatEntry_Object = MibTableRow
accIsdnStatEntry = _AccIsdnStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1)
)
accIsdnStatEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnStatEntry.setStatus("deprecated")
_AccIsdnStatHdlcInPackets_Type = Counter32
_AccIsdnStatHdlcInPackets_Object = MibTableColumn
accIsdnStatHdlcInPackets = _AccIsdnStatHdlcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 1),
    _AccIsdnStatHdlcInPackets_Type()
)
accIsdnStatHdlcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInPackets.setStatus("deprecated")
_AccIsdnStatHdlcInOctets_Type = Counter32
_AccIsdnStatHdlcInOctets_Object = MibTableColumn
accIsdnStatHdlcInOctets = _AccIsdnStatHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 2),
    _AccIsdnStatHdlcInOctets_Type()
)
accIsdnStatHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInOctets.setStatus("deprecated")
_AccIsdnStatHdlcInErrors_Type = Counter32
_AccIsdnStatHdlcInErrors_Object = MibTableColumn
accIsdnStatHdlcInErrors = _AccIsdnStatHdlcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 3),
    _AccIsdnStatHdlcInErrors_Type()
)
accIsdnStatHdlcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInErrors.setStatus("deprecated")
_AccIsdnStatHdlcInDiscs_Type = Counter32
_AccIsdnStatHdlcInDiscs_Object = MibTableColumn
accIsdnStatHdlcInDiscs = _AccIsdnStatHdlcInDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 4),
    _AccIsdnStatHdlcInDiscs_Type()
)
accIsdnStatHdlcInDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcInDiscs.setStatus("deprecated")
_AccIsdnStatHdlcOutPackets_Type = Counter32
_AccIsdnStatHdlcOutPackets_Object = MibTableColumn
accIsdnStatHdlcOutPackets = _AccIsdnStatHdlcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 5),
    _AccIsdnStatHdlcOutPackets_Type()
)
accIsdnStatHdlcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutPackets.setStatus("deprecated")
_AccIsdnStatHdlcOutOctets_Type = Counter32
_AccIsdnStatHdlcOutOctets_Object = MibTableColumn
accIsdnStatHdlcOutOctets = _AccIsdnStatHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 6),
    _AccIsdnStatHdlcOutOctets_Type()
)
accIsdnStatHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutOctets.setStatus("deprecated")
_AccIsdnStatHdlcOutErrors_Type = Counter32
_AccIsdnStatHdlcOutErrors_Object = MibTableColumn
accIsdnStatHdlcOutErrors = _AccIsdnStatHdlcOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 7),
    _AccIsdnStatHdlcOutErrors_Type()
)
accIsdnStatHdlcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutErrors.setStatus("deprecated")
_AccIsdnStatHdlcOutDiscs_Type = Counter32
_AccIsdnStatHdlcOutDiscs_Object = MibTableColumn
accIsdnStatHdlcOutDiscs = _AccIsdnStatHdlcOutDiscs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 8),
    _AccIsdnStatHdlcOutDiscs_Type()
)
accIsdnStatHdlcOutDiscs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatHdlcOutDiscs.setStatus("deprecated")
_AccIsdnStatLapdUnsolicResps_Type = Counter32
_AccIsdnStatLapdUnsolicResps_Object = MibTableColumn
accIsdnStatLapdUnsolicResps = _AccIsdnStatLapdUnsolicResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 9),
    _AccIsdnStatLapdUnsolicResps_Type()
)
accIsdnStatLapdUnsolicResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdUnsolicResps.setStatus("deprecated")
_AccIsdnStatLapdPeerSabmes_Type = Counter32
_AccIsdnStatLapdPeerSabmes_Object = MibTableColumn
accIsdnStatLapdPeerSabmes = _AccIsdnStatLapdPeerSabmes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 10),
    _AccIsdnStatLapdPeerSabmes_Type()
)
accIsdnStatLapdPeerSabmes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdPeerSabmes.setStatus("deprecated")
_AccIsdnStatLapdN200Errors_Type = Counter32
_AccIsdnStatLapdN200Errors_Object = MibTableColumn
accIsdnStatLapdN200Errors = _AccIsdnStatLapdN200Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 11),
    _AccIsdnStatLapdN200Errors_Type()
)
accIsdnStatLapdN200Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdN200Errors.setStatus("deprecated")
_AccIsdnStatLapdNrSeqErrors_Type = Counter32
_AccIsdnStatLapdNrSeqErrors_Object = MibTableColumn
accIsdnStatLapdNrSeqErrors = _AccIsdnStatLapdNrSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 12),
    _AccIsdnStatLapdNrSeqErrors_Type()
)
accIsdnStatLapdNrSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdNrSeqErrors.setStatus("deprecated")
_AccIsdnStatLapdRecvdFrmrs_Type = Counter32
_AccIsdnStatLapdRecvdFrmrs_Object = MibTableColumn
accIsdnStatLapdRecvdFrmrs = _AccIsdnStatLapdRecvdFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 13),
    _AccIsdnStatLapdRecvdFrmrs_Type()
)
accIsdnStatLapdRecvdFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdRecvdFrmrs.setStatus("deprecated")
_AccIsdnStatLapdCntlErrors_Type = Counter32
_AccIsdnStatLapdCntlErrors_Object = MibTableColumn
accIsdnStatLapdCntlErrors = _AccIsdnStatLapdCntlErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 14),
    _AccIsdnStatLapdCntlErrors_Type()
)
accIsdnStatLapdCntlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdCntlErrors.setStatus("deprecated")
_AccIsdnStatLapdInfoErrors_Type = Counter32
_AccIsdnStatLapdInfoErrors_Object = MibTableColumn
accIsdnStatLapdInfoErrors = _AccIsdnStatLapdInfoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 15),
    _AccIsdnStatLapdInfoErrors_Type()
)
accIsdnStatLapdInfoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdInfoErrors.setStatus("deprecated")
_AccIsdnStatLapdWrongSizes_Type = Counter32
_AccIsdnStatLapdWrongSizes_Object = MibTableColumn
accIsdnStatLapdWrongSizes = _AccIsdnStatLapdWrongSizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 16),
    _AccIsdnStatLapdWrongSizes_Type()
)
accIsdnStatLapdWrongSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdWrongSizes.setStatus("deprecated")
_AccIsdnStatLapdN201Errors_Type = Counter32
_AccIsdnStatLapdN201Errors_Object = MibTableColumn
accIsdnStatLapdN201Errors = _AccIsdnStatLapdN201Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 17),
    _AccIsdnStatLapdN201Errors_Type()
)
accIsdnStatLapdN201Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLapdN201Errors.setStatus("deprecated")
_AccIsdnStatCallsOriginateds_Type = Counter32
_AccIsdnStatCallsOriginateds_Object = MibTableColumn
accIsdnStatCallsOriginateds = _AccIsdnStatCallsOriginateds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 18),
    _AccIsdnStatCallsOriginateds_Type()
)
accIsdnStatCallsOriginateds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsOriginateds.setStatus("deprecated")
_AccIsdnStatCallsOfferreds_Type = Counter32
_AccIsdnStatCallsOfferreds_Object = MibTableColumn
accIsdnStatCallsOfferreds = _AccIsdnStatCallsOfferreds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 19),
    _AccIsdnStatCallsOfferreds_Type()
)
accIsdnStatCallsOfferreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsOfferreds.setStatus("deprecated")
_AccIsdnStatCallsAnswereds_Type = Counter32
_AccIsdnStatCallsAnswereds_Object = MibTableColumn
accIsdnStatCallsAnswereds = _AccIsdnStatCallsAnswereds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 20),
    _AccIsdnStatCallsAnswereds_Type()
)
accIsdnStatCallsAnswereds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsAnswereds.setStatus("deprecated")
_AccIsdnStatCallsAccepteds_Type = Counter32
_AccIsdnStatCallsAccepteds_Object = MibTableColumn
accIsdnStatCallsAccepteds = _AccIsdnStatCallsAccepteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 21),
    _AccIsdnStatCallsAccepteds_Type()
)
accIsdnStatCallsAccepteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsAccepteds.setStatus("deprecated")
_AccIsdnStatCallsCompleteds_Type = Counter32
_AccIsdnStatCallsCompleteds_Object = MibTableColumn
accIsdnStatCallsCompleteds = _AccIsdnStatCallsCompleteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 22),
    _AccIsdnStatCallsCompleteds_Type()
)
accIsdnStatCallsCompleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsCompleteds.setStatus("deprecated")
_AccIsdnStatCallsCleareds_Type = Counter32
_AccIsdnStatCallsCleareds_Object = MibTableColumn
accIsdnStatCallsCleareds = _AccIsdnStatCallsCleareds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 23),
    _AccIsdnStatCallsCleareds_Type()
)
accIsdnStatCallsCleareds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatCallsCleareds.setStatus("deprecated")


class _AccIsdnStatDslOperStatus_Type(Integer32):
    """Custom type accIsdnStatDslOperStatus based on Integer32"""
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
        *(("activated", 3),
          ("established", 4),
          ("inactive", 1),
          ("waiting", 2))
    )


_AccIsdnStatDslOperStatus_Type.__name__ = "Integer32"
_AccIsdnStatDslOperStatus_Object = MibTableColumn
accIsdnStatDslOperStatus = _AccIsdnStatDslOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 24),
    _AccIsdnStatDslOperStatus_Type()
)
accIsdnStatDslOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatDslOperStatus.setStatus("deprecated")


class _AccIsdnStatLastCauses_Type(Integer32):
    """Custom type accIsdnStatLastCauses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnStatLastCauses_Type.__name__ = "Integer32"
_AccIsdnStatLastCauses_Object = MibTableColumn
accIsdnStatLastCauses = _AccIsdnStatLastCauses_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 3, 1, 25),
    _AccIsdnStatLastCauses_Type()
)
accIsdnStatLastCauses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnStatLastCauses.setStatus("deprecated")
_AccIsdnCallTable_Object = MibTable
accIsdnCallTable = _AccIsdnCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4)
)
if mibBuilder.loadTexts:
    accIsdnCallTable.setStatus("deprecated")
_AccIsdnCallEntry_Object = MibTableRow
accIsdnCallEntry = _AccIsdnCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1)
)
accIsdnCallEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnCallDslIndex"),
    (0, "ACC-MIB", "accIsdnCallIdentifier"),
)
if mibBuilder.loadTexts:
    accIsdnCallEntry.setStatus("deprecated")


class _AccIsdnCallIdentifier_Type(Integer32):
    """Custom type accIsdnCallIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AccIsdnCallIdentifier_Type.__name__ = "Integer32"
_AccIsdnCallIdentifier_Object = MibTableColumn
accIsdnCallIdentifier = _AccIsdnCallIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 1),
    _AccIsdnCallIdentifier_Type()
)
accIsdnCallIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallIdentifier.setStatus("deprecated")


class _AccIsdnCallReference_Type(Integer32):
    """Custom type accIsdnCallReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AccIsdnCallReference_Type.__name__ = "Integer32"
_AccIsdnCallReference_Object = MibTableColumn
accIsdnCallReference = _AccIsdnCallReference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 2),
    _AccIsdnCallReference_Type()
)
accIsdnCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallReference.setStatus("deprecated")


class _AccIsdnCallChannelId_Type(Integer32):
    """Custom type accIsdnCallChannelId based on Integer32"""
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
        *(("b1", 2),
          ("b2", 3),
          ("h0", 4),
          ("none", 1))
    )


_AccIsdnCallChannelId_Type.__name__ = "Integer32"
_AccIsdnCallChannelId_Object = MibTableColumn
accIsdnCallChannelId = _AccIsdnCallChannelId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 3),
    _AccIsdnCallChannelId_Type()
)
accIsdnCallChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallChannelId.setStatus("deprecated")


class _AccIsdnCallIfIndex_Type(Integer32):
    """Custom type accIsdnCallIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2))
    )


_AccIsdnCallIfIndex_Type.__name__ = "Integer32"
_AccIsdnCallIfIndex_Object = MibTableColumn
accIsdnCallIfIndex = _AccIsdnCallIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 4),
    _AccIsdnCallIfIndex_Type()
)
accIsdnCallIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallIfIndex.setStatus("deprecated")


class _AccIsdnCallInfoRate_Type(Integer32):
    """Custom type accIsdnCallInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              17,
              18,
              20,
              22,
              24)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("r-1536k", 22),
          ("r-1920k", 24),
          ("r-2x64k", 18),
          ("r-384k", 20),
          ("r-64k", 17))
    )


_AccIsdnCallInfoRate_Type.__name__ = "Integer32"
_AccIsdnCallInfoRate_Object = MibTableColumn
accIsdnCallInfoRate = _AccIsdnCallInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 5),
    _AccIsdnCallInfoRate_Type()
)
accIsdnCallInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallInfoRate.setStatus("deprecated")


class _AccIsdnCallState_Type(Integer32):
    """Custom type accIsdnCallState based on Integer32"""
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
        *(("connected", 6),
          ("disconnected", 1),
          ("incoming", 2),
          ("outgoing", 3),
          ("releaseing", 5),
          ("routing", 4))
    )


_AccIsdnCallState_Type.__name__ = "Integer32"
_AccIsdnCallState_Object = MibTableColumn
accIsdnCallState = _AccIsdnCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 6),
    _AccIsdnCallState_Type()
)
accIsdnCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallState.setStatus("deprecated")


class _AccIsdnCallCause_Type(Integer32):
    """Custom type accIsdnCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnCallCause_Type.__name__ = "Integer32"
_AccIsdnCallCause_Object = MibTableColumn
accIsdnCallCause = _AccIsdnCallCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 7),
    _AccIsdnCallCause_Type()
)
accIsdnCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallCause.setStatus("deprecated")


class _AccIsdnCallOrigin_Type(Integer32):
    """Custom type accIsdnCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network", 3),
          ("none", 1),
          ("terminal", 2))
    )


_AccIsdnCallOrigin_Type.__name__ = "Integer32"
_AccIsdnCallOrigin_Object = MibTableColumn
accIsdnCallOrigin = _AccIsdnCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 8),
    _AccIsdnCallOrigin_Type()
)
accIsdnCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallOrigin.setStatus("deprecated")
_AccIsdnCallAddress_Type = OctetString
_AccIsdnCallAddress_Object = MibTableColumn
accIsdnCallAddress = _AccIsdnCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 9),
    _AccIsdnCallAddress_Type()
)
accIsdnCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallAddress.setStatus("deprecated")


class _AccIsdnCallDslIndex_Type(Integer32):
    """Custom type accIsdnCallDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnCallDslIndex_Type.__name__ = "Integer32"
_AccIsdnCallDslIndex_Object = MibTableColumn
accIsdnCallDslIndex = _AccIsdnCallDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 4, 1, 10),
    _AccIsdnCallDslIndex_Type()
)
accIsdnCallDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnCallDslIndex.setStatus("deprecated")
_AccIsdnTest_ObjectIdentity = ObjectIdentity
accIsdnTest = _AccIsdnTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5)
)


class _AccIsdnTestIfIndex_Type(Integer32):
    """Custom type accIsdnTestIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("j1", 1),
          ("j2", 2))
    )


_AccIsdnTestIfIndex_Type.__name__ = "Integer32"
_AccIsdnTestIfIndex_Object = MibScalar
accIsdnTestIfIndex = _AccIsdnTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 1),
    _AccIsdnTestIfIndex_Type()
)
accIsdnTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestIfIndex.setStatus("mandatory")
_AccIsdnTestAddress_Type = OctetString
_AccIsdnTestAddress_Object = MibScalar
accIsdnTestAddress = _AccIsdnTestAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 2),
    _AccIsdnTestAddress_Type()
)
accIsdnTestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestAddress.setStatus("mandatory")


class _AccIsdnTestCommand_Type(Integer32):
    """Custom type accIsdnTestCommand based on Integer32"""
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
        *(("accept", 2),
          ("activate", 10),
          ("call", 5),
          ("clear", 6),
          ("deactivate", 11),
          ("disconnect", 7),
          ("display", 12),
          ("ignore", 4),
          ("loop", 8),
          ("normal", 1),
          ("reject", 3),
          ("unloop", 9))
    )


_AccIsdnTestCommand_Type.__name__ = "Integer32"
_AccIsdnTestCommand_Object = MibScalar
accIsdnTestCommand = _AccIsdnTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 3),
    _AccIsdnTestCommand_Type()
)
accIsdnTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestCommand.setStatus("mandatory")


class _AccIsdnTestProceed_Type(Integer32):
    """Custom type accIsdnTestProceed based on Integer32"""
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
        *(("accept", 2),
          ("ignore", 4),
          ("normal", 1),
          ("reject", 3))
    )


_AccIsdnTestProceed_Type.__name__ = "Integer32"
_AccIsdnTestProceed_Object = MibScalar
accIsdnTestProceed = _AccIsdnTestProceed_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 4),
    _AccIsdnTestProceed_Type()
)
accIsdnTestProceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnTestProceed.setStatus("mandatory")


class _AccIsdnTestRegName_Type(Integer32):
    """Custom type accIsdnTestRegName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AccIsdnTestRegName_Type.__name__ = "Integer32"
_AccIsdnTestRegName_Object = MibScalar
accIsdnTestRegName = _AccIsdnTestRegName_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 5),
    _AccIsdnTestRegName_Type()
)
accIsdnTestRegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestRegName.setStatus("mandatory")


class _AccIsdnTestRegValue_Type(Integer32):
    """Custom type accIsdnTestRegValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnTestRegValue_Type.__name__ = "Integer32"
_AccIsdnTestRegValue_Object = MibScalar
accIsdnTestRegValue = _AccIsdnTestRegValue_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 5, 6),
    _AccIsdnTestRegValue_Type()
)
accIsdnTestRegValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnTestRegValue.setStatus("mandatory")
_AccIsdnxSubTable_Object = MibTable
accIsdnxSubTable = _AccIsdnxSubTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6)
)
if mibBuilder.loadTexts:
    accIsdnxSubTable.setStatus("mandatory")
_AccIsdnxSubEntry_Object = MibTableRow
accIsdnxSubEntry = _AccIsdnxSubEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1)
)
accIsdnxSubEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnxSubDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnxSubEntry.setStatus("mandatory")


class _AccIsdnxSubDslIndex_Type(Integer32):
    """Custom type accIsdnxSubDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccIsdnxSubDslIndex_Type.__name__ = "Integer32"
_AccIsdnxSubDslIndex_Object = MibTableColumn
accIsdnxSubDslIndex = _AccIsdnxSubDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 1),
    _AccIsdnxSubDslIndex_Type()
)
accIsdnxSubDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubDslIndex.setStatus("mandatory")


class _AccIsdnxSubSwitchType_Type(Integer32):
    """Custom type accIsdnxSubSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_AccIsdnxSubSwitchType_Type.__name__ = "Integer32"
_AccIsdnxSubSwitchType_Object = MibTableColumn
accIsdnxSubSwitchType = _AccIsdnxSubSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 2),
    _AccIsdnxSubSwitchType_Type()
)
accIsdnxSubSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubSwitchType.setStatus("mandatory")


class _AccIsdnxSubChanConfig_Type(Integer32):
    """Custom type accIsdnxSubChanConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AccIsdnxSubChanConfig_Type.__name__ = "Integer32"
_AccIsdnxSubChanConfig_Object = MibTableColumn
accIsdnxSubChanConfig = _AccIsdnxSubChanConfig_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 3),
    _AccIsdnxSubChanConfig_Type()
)
accIsdnxSubChanConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubChanConfig.setStatus("mandatory")


class _AccIsdnxSubAdminStatus_Type(Integer32):
    """Custom type accIsdnxSubAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AccIsdnxSubAdminStatus_Type.__name__ = "Integer32"
_AccIsdnxSubAdminStatus_Object = MibTableColumn
accIsdnxSubAdminStatus = _AccIsdnxSubAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 4),
    _AccIsdnxSubAdminStatus_Type()
)
accIsdnxSubAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubAdminStatus.setStatus("mandatory")


class _AccIsdnxSubDiagLevel_Type(Integer32):
    """Custom type accIsdnxSubDiagLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AccIsdnxSubDiagLevel_Type.__name__ = "Integer32"
_AccIsdnxSubDiagLevel_Object = MibTableColumn
accIsdnxSubDiagLevel = _AccIsdnxSubDiagLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 5),
    _AccIsdnxSubDiagLevel_Type()
)
accIsdnxSubDiagLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubDiagLevel.setStatus("mandatory")


class _AccIsdnxSubManualTei_Type(Integer32):
    """Custom type accIsdnxSubManualTei based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AccIsdnxSubManualTei_Type.__name__ = "Integer32"
_AccIsdnxSubManualTei_Object = MibTableColumn
accIsdnxSubManualTei = _AccIsdnxSubManualTei_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 6),
    _AccIsdnxSubManualTei_Type()
)
accIsdnxSubManualTei.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubManualTei.setStatus("mandatory")


class _AccIsdnxSubOperStatus_Type(Integer32):
    """Custom type accIsdnxSubOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AccIsdnxSubOperStatus_Type.__name__ = "Integer32"
_AccIsdnxSubOperStatus_Object = MibTableColumn
accIsdnxSubOperStatus = _AccIsdnxSubOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 7),
    _AccIsdnxSubOperStatus_Type()
)
accIsdnxSubOperStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnxSubOperStatus.setStatus("mandatory")


class _AccIsdnxSubNumNfas_Type(Integer32):
    """Custom type accIsdnxSubNumNfas based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxSubNumNfas_Type.__name__ = "Integer32"
_AccIsdnxSubNumNfas_Object = MibTableColumn
accIsdnxSubNumNfas = _AccIsdnxSubNumNfas_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 8),
    _AccIsdnxSubNumNfas_Type()
)
accIsdnxSubNumNfas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubNumNfas.setStatus("mandatory")


class _AccIsdnxSubLastCause_Type(Integer32):
    """Custom type accIsdnxSubLastCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxSubLastCause_Type.__name__ = "Integer32"
_AccIsdnxSubLastCause_Object = MibTableColumn
accIsdnxSubLastCause = _AccIsdnxSubLastCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 6, 1, 9),
    _AccIsdnxSubLastCause_Type()
)
accIsdnxSubLastCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxSubLastCause.setStatus("mandatory")
_AccIsdnxStatTable_Object = MibTable
accIsdnxStatTable = _AccIsdnxStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7)
)
if mibBuilder.loadTexts:
    accIsdnxStatTable.setStatus("mandatory")
_AccIsdnxStatEntry_Object = MibTableRow
accIsdnxStatEntry = _AccIsdnxStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1)
)
accIsdnxStatEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnxStatDslIndex"),
)
if mibBuilder.loadTexts:
    accIsdnxStatEntry.setStatus("mandatory")


class _AccIsdnxStatDslIndex_Type(Integer32):
    """Custom type accIsdnxStatDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccIsdnxStatDslIndex_Type.__name__ = "Integer32"
_AccIsdnxStatDslIndex_Object = MibTableColumn
accIsdnxStatDslIndex = _AccIsdnxStatDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 1),
    _AccIsdnxStatDslIndex_Type()
)
accIsdnxStatDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatDslIndex.setStatus("mandatory")
_AccIsdnxStatHdlcInPackets_Type = Counter32
_AccIsdnxStatHdlcInPackets_Object = MibTableColumn
accIsdnxStatHdlcInPackets = _AccIsdnxStatHdlcInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 2),
    _AccIsdnxStatHdlcInPackets_Type()
)
accIsdnxStatHdlcInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInPackets.setStatus("mandatory")
_AccIsdnxStatHdlcInOctets_Type = Counter32
_AccIsdnxStatHdlcInOctets_Object = MibTableColumn
accIsdnxStatHdlcInOctets = _AccIsdnxStatHdlcInOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 3),
    _AccIsdnxStatHdlcInOctets_Type()
)
accIsdnxStatHdlcInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInOctets.setStatus("mandatory")
_AccIsdnxStatHdlcInErrors_Type = Counter32
_AccIsdnxStatHdlcInErrors_Object = MibTableColumn
accIsdnxStatHdlcInErrors = _AccIsdnxStatHdlcInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 4),
    _AccIsdnxStatHdlcInErrors_Type()
)
accIsdnxStatHdlcInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInErrors.setStatus("mandatory")
_AccIsdnxStatHdlcInDiscards_Type = Counter32
_AccIsdnxStatHdlcInDiscards_Object = MibTableColumn
accIsdnxStatHdlcInDiscards = _AccIsdnxStatHdlcInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 5),
    _AccIsdnxStatHdlcInDiscards_Type()
)
accIsdnxStatHdlcInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcInDiscards.setStatus("mandatory")
_AccIsdnxStatHdlcOutPackets_Type = Counter32
_AccIsdnxStatHdlcOutPackets_Object = MibTableColumn
accIsdnxStatHdlcOutPackets = _AccIsdnxStatHdlcOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 6),
    _AccIsdnxStatHdlcOutPackets_Type()
)
accIsdnxStatHdlcOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutPackets.setStatus("mandatory")
_AccIsdnxStatHdlcOutOctets_Type = Counter32
_AccIsdnxStatHdlcOutOctets_Object = MibTableColumn
accIsdnxStatHdlcOutOctets = _AccIsdnxStatHdlcOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 7),
    _AccIsdnxStatHdlcOutOctets_Type()
)
accIsdnxStatHdlcOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutOctets.setStatus("mandatory")
_AccIsdnxStatHdlcOutErrors_Type = Counter32
_AccIsdnxStatHdlcOutErrors_Object = MibTableColumn
accIsdnxStatHdlcOutErrors = _AccIsdnxStatHdlcOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 8),
    _AccIsdnxStatHdlcOutErrors_Type()
)
accIsdnxStatHdlcOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutErrors.setStatus("mandatory")
_AccIsdnxStatHdlcOutDiscards_Type = Counter32
_AccIsdnxStatHdlcOutDiscards_Object = MibTableColumn
accIsdnxStatHdlcOutDiscards = _AccIsdnxStatHdlcOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 9),
    _AccIsdnxStatHdlcOutDiscards_Type()
)
accIsdnxStatHdlcOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatHdlcOutDiscards.setStatus("mandatory")
_AccIsdnxStatLapdUnsolicResps_Type = Counter32
_AccIsdnxStatLapdUnsolicResps_Object = MibTableColumn
accIsdnxStatLapdUnsolicResps = _AccIsdnxStatLapdUnsolicResps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 10),
    _AccIsdnxStatLapdUnsolicResps_Type()
)
accIsdnxStatLapdUnsolicResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdUnsolicResps.setStatus("mandatory")
_AccIsdnxStatLapdPeerSabmes_Type = Counter32
_AccIsdnxStatLapdPeerSabmes_Object = MibTableColumn
accIsdnxStatLapdPeerSabmes = _AccIsdnxStatLapdPeerSabmes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 11),
    _AccIsdnxStatLapdPeerSabmes_Type()
)
accIsdnxStatLapdPeerSabmes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdPeerSabmes.setStatus("mandatory")
_AccIsdnxStatLapdN200Errors_Type = Counter32
_AccIsdnxStatLapdN200Errors_Object = MibTableColumn
accIsdnxStatLapdN200Errors = _AccIsdnxStatLapdN200Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 12),
    _AccIsdnxStatLapdN200Errors_Type()
)
accIsdnxStatLapdN200Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdN200Errors.setStatus("mandatory")
_AccIsdnxStatLapdNrSeqErrors_Type = Counter32
_AccIsdnxStatLapdNrSeqErrors_Object = MibTableColumn
accIsdnxStatLapdNrSeqErrors = _AccIsdnxStatLapdNrSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 13),
    _AccIsdnxStatLapdNrSeqErrors_Type()
)
accIsdnxStatLapdNrSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdNrSeqErrors.setStatus("mandatory")
_AccIsdnxStatLapdRecvdFrmrs_Type = Counter32
_AccIsdnxStatLapdRecvdFrmrs_Object = MibTableColumn
accIsdnxStatLapdRecvdFrmrs = _AccIsdnxStatLapdRecvdFrmrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 14),
    _AccIsdnxStatLapdRecvdFrmrs_Type()
)
accIsdnxStatLapdRecvdFrmrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdRecvdFrmrs.setStatus("mandatory")
_AccIsdnxStatLapdCntlErrors_Type = Counter32
_AccIsdnxStatLapdCntlErrors_Object = MibTableColumn
accIsdnxStatLapdCntlErrors = _AccIsdnxStatLapdCntlErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 15),
    _AccIsdnxStatLapdCntlErrors_Type()
)
accIsdnxStatLapdCntlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdCntlErrors.setStatus("mandatory")
_AccIsdnxStatLapdInfoErrors_Type = Counter32
_AccIsdnxStatLapdInfoErrors_Object = MibTableColumn
accIsdnxStatLapdInfoErrors = _AccIsdnxStatLapdInfoErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 16),
    _AccIsdnxStatLapdInfoErrors_Type()
)
accIsdnxStatLapdInfoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdInfoErrors.setStatus("mandatory")
_AccIsdnxStatLapdWrongSizes_Type = Counter32
_AccIsdnxStatLapdWrongSizes_Object = MibTableColumn
accIsdnxStatLapdWrongSizes = _AccIsdnxStatLapdWrongSizes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 17),
    _AccIsdnxStatLapdWrongSizes_Type()
)
accIsdnxStatLapdWrongSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdWrongSizes.setStatus("mandatory")
_AccIsdnxStatLapdN201Errors_Type = Counter32
_AccIsdnxStatLapdN201Errors_Object = MibTableColumn
accIsdnxStatLapdN201Errors = _AccIsdnxStatLapdN201Errors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 18),
    _AccIsdnxStatLapdN201Errors_Type()
)
accIsdnxStatLapdN201Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatLapdN201Errors.setStatus("mandatory")
_AccIsdnxStatCallOriginateds_Type = Counter32
_AccIsdnxStatCallOriginateds_Object = MibTableColumn
accIsdnxStatCallOriginateds = _AccIsdnxStatCallOriginateds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 19),
    _AccIsdnxStatCallOriginateds_Type()
)
accIsdnxStatCallOriginateds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallOriginateds.setStatus("mandatory")
_AccIsdnxStatCallOfferreds_Type = Counter32
_AccIsdnxStatCallOfferreds_Object = MibTableColumn
accIsdnxStatCallOfferreds = _AccIsdnxStatCallOfferreds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 20),
    _AccIsdnxStatCallOfferreds_Type()
)
accIsdnxStatCallOfferreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallOfferreds.setStatus("mandatory")
_AccIsdnxStatCallRouteds_Type = Counter32
_AccIsdnxStatCallRouteds_Object = MibTableColumn
accIsdnxStatCallRouteds = _AccIsdnxStatCallRouteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 21),
    _AccIsdnxStatCallRouteds_Type()
)
accIsdnxStatCallRouteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallRouteds.setStatus("mandatory")
_AccIsdnxStatCallAccepteds_Type = Counter32
_AccIsdnxStatCallAccepteds_Object = MibTableColumn
accIsdnxStatCallAccepteds = _AccIsdnxStatCallAccepteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 22),
    _AccIsdnxStatCallAccepteds_Type()
)
accIsdnxStatCallAccepteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallAccepteds.setStatus("mandatory")
_AccIsdnxStatCallCompleteds_Type = Counter32
_AccIsdnxStatCallCompleteds_Object = MibTableColumn
accIsdnxStatCallCompleteds = _AccIsdnxStatCallCompleteds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 23),
    _AccIsdnxStatCallCompleteds_Type()
)
accIsdnxStatCallCompleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallCompleteds.setStatus("mandatory")
_AccIsdnxStatCallCleareds_Type = Counter32
_AccIsdnxStatCallCleareds_Object = MibTableColumn
accIsdnxStatCallCleareds = _AccIsdnxStatCallCleareds_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 7, 1, 24),
    _AccIsdnxStatCallCleareds_Type()
)
accIsdnxStatCallCleareds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxStatCallCleareds.setStatus("mandatory")
_AccIsdnxCallTable_Object = MibTable
accIsdnxCallTable = _AccIsdnxCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8)
)
if mibBuilder.loadTexts:
    accIsdnxCallTable.setStatus("mandatory")
_AccIsdnxCallEntry_Object = MibTableRow
accIsdnxCallEntry = _AccIsdnxCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1)
)
accIsdnxCallEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnxCallDslIndex"),
    (0, "ACC-MIB", "accIsdnxCallReference"),
    (0, "ACC-MIB", "accIsdnxCallOrigin"),
)
if mibBuilder.loadTexts:
    accIsdnxCallEntry.setStatus("mandatory")


class _AccIsdnxCallDslIndex_Type(Integer32):
    """Custom type accIsdnxCallDslIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccIsdnxCallDslIndex_Type.__name__ = "Integer32"
_AccIsdnxCallDslIndex_Object = MibTableColumn
accIsdnxCallDslIndex = _AccIsdnxCallDslIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 1),
    _AccIsdnxCallDslIndex_Type()
)
accIsdnxCallDslIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallDslIndex.setStatus("mandatory")


class _AccIsdnxCallReference_Type(Integer32):
    """Custom type accIsdnxCallReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AccIsdnxCallReference_Type.__name__ = "Integer32"
_AccIsdnxCallReference_Object = MibTableColumn
accIsdnxCallReference = _AccIsdnxCallReference_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 2),
    _AccIsdnxCallReference_Type()
)
accIsdnxCallReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallReference.setStatus("mandatory")


class _AccIsdnxCallOrigin_Type(Integer32):
    """Custom type accIsdnxCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AccIsdnxCallOrigin_Type.__name__ = "Integer32"
_AccIsdnxCallOrigin_Object = MibTableColumn
accIsdnxCallOrigin = _AccIsdnxCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 3),
    _AccIsdnxCallOrigin_Type()
)
accIsdnxCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallOrigin.setStatus("mandatory")


class _AccIsdnxCallCircuitIndex_Type(Integer32):
    """Custom type accIsdnxCallCircuitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AccIsdnxCallCircuitIndex_Type.__name__ = "Integer32"
_AccIsdnxCallCircuitIndex_Object = MibTableColumn
accIsdnxCallCircuitIndex = _AccIsdnxCallCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 4),
    _AccIsdnxCallCircuitIndex_Type()
)
accIsdnxCallCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallCircuitIndex.setStatus("mandatory")


class _AccIsdnxCallInfoRate_Type(Integer32):
    """Custom type accIsdnxCallInfoRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_AccIsdnxCallInfoRate_Type.__name__ = "Integer32"
_AccIsdnxCallInfoRate_Object = MibTableColumn
accIsdnxCallInfoRate = _AccIsdnxCallInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 5),
    _AccIsdnxCallInfoRate_Type()
)
accIsdnxCallInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallInfoRate.setStatus("mandatory")


class _AccIsdnxCallState_Type(Integer32):
    """Custom type accIsdnxCallState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AccIsdnxCallState_Type.__name__ = "Integer32"
_AccIsdnxCallState_Object = MibTableColumn
accIsdnxCallState = _AccIsdnxCallState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 6),
    _AccIsdnxCallState_Type()
)
accIsdnxCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallState.setStatus("mandatory")


class _AccIsdnxCallCause_Type(Integer32):
    """Custom type accIsdnxCallCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccIsdnxCallCause_Type.__name__ = "Integer32"
_AccIsdnxCallCause_Object = MibTableColumn
accIsdnxCallCause = _AccIsdnxCallCause_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 7),
    _AccIsdnxCallCause_Type()
)
accIsdnxCallCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallCause.setStatus("mandatory")
_AccIsdnxCallAddress_Type = OctetString
_AccIsdnxCallAddress_Object = MibTableColumn
accIsdnxCallAddress = _AccIsdnxCallAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 8),
    _AccIsdnxCallAddress_Type()
)
accIsdnxCallAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallAddress.setStatus("mandatory")


class _AccIsdnxCallInfoType_Type(Integer32):
    """Custom type accIsdnxCallInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AccIsdnxCallInfoType_Type.__name__ = "Integer32"
_AccIsdnxCallInfoType_Object = MibTableColumn
accIsdnxCallInfoType = _AccIsdnxCallInfoType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 9),
    _AccIsdnxCallInfoType_Type()
)
accIsdnxCallInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallInfoType.setStatus("mandatory")
_AccIsdnxCallSlotMap_Type = Integer32
_AccIsdnxCallSlotMap_Object = MibTableColumn
accIsdnxCallSlotMap = _AccIsdnxCallSlotMap_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 8, 1, 10),
    _AccIsdnxCallSlotMap_Type()
)
accIsdnxCallSlotMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accIsdnxCallSlotMap.setStatus("mandatory")
_AccIsdnSpidTable_Object = MibTable
accIsdnSpidTable = _AccIsdnSpidTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9)
)
if mibBuilder.loadTexts:
    accIsdnSpidTable.setStatus("mandatory")
_AccIsdnSpidEntry_Object = MibTableRow
accIsdnSpidEntry = _AccIsdnSpidEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1)
)
accIsdnSpidEntry.setIndexNames(
    (0, "ACC-MIB", "accIsdnSpidIndex"),
)
if mibBuilder.loadTexts:
    accIsdnSpidEntry.setStatus("mandatory")
_AccIsdnSpidIndex_Type = Integer32
_AccIsdnSpidIndex_Object = MibTableColumn
accIsdnSpidIndex = _AccIsdnSpidIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1, 1),
    _AccIsdnSpidIndex_Type()
)
accIsdnSpidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    accIsdnSpidIndex.setStatus("mandatory")
_AccIsdnSpidValue_Type = DisplayString
_AccIsdnSpidValue_Object = MibTableColumn
accIsdnSpidValue = _AccIsdnSpidValue_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 36, 9, 1, 2),
    _AccIsdnSpidValue_Type()
)
accIsdnSpidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIsdnSpidValue.setStatus("mandatory")
_AccV25_ObjectIdentity = ObjectIdentity
accV25 = _AccV25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37)
)
_AccV25StatTable_Object = MibTable
accV25StatTable = _AccV25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1)
)
if mibBuilder.loadTexts:
    accV25StatTable.setStatus("mandatory")
_AccV25StatEntry_Object = MibTableRow
accV25StatEntry = _AccV25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1)
)
accV25StatEntry.setIndexNames(
    (0, "ACC-MIB", "accV25IntIndex"),
)
if mibBuilder.loadTexts:
    accV25StatEntry.setStatus("mandatory")
_AccV25IntIndex_Type = Integer32
_AccV25IntIndex_Object = MibTableColumn
accV25IntIndex = _AccV25IntIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 1),
    _AccV25IntIndex_Type()
)
accV25IntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25IntIndex.setStatus("mandatory")


class _AccV25CurState_Type(Integer32):
    """Custom type accV25CurState based on Integer32"""
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
        *(("call-connected", 5),
          ("clear-by-dte", 7),
          ("data-transfer", 6),
          ("dialogue", 3),
          ("dialogue-pending", 2),
          ("dte-not-ready", 1),
          ("handshaking", 4))
    )


_AccV25CurState_Type.__name__ = "Integer32"
_AccV25CurState_Object = MibTableColumn
accV25CurState = _AccV25CurState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 2),
    _AccV25CurState_Type()
)
accV25CurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CurState.setStatus("mandatory")


class _AccV25DTRSignal_Type(Integer32):
    """Custom type accV25DTRSignal based on Integer32"""
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


_AccV25DTRSignal_Type.__name__ = "Integer32"
_AccV25DTRSignal_Object = MibTableColumn
accV25DTRSignal = _AccV25DTRSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 3),
    _AccV25DTRSignal_Type()
)
accV25DTRSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25DTRSignal.setStatus("mandatory")


class _AccV25DSRSignal_Type(Integer32):
    """Custom type accV25DSRSignal based on Integer32"""
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


_AccV25DSRSignal_Type.__name__ = "Integer32"
_AccV25DSRSignal_Object = MibTableColumn
accV25DSRSignal = _AccV25DSRSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 4),
    _AccV25DSRSignal_Type()
)
accV25DSRSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25DSRSignal.setStatus("mandatory")


class _AccV25CTSSignal_Type(Integer32):
    """Custom type accV25CTSSignal based on Integer32"""
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


_AccV25CTSSignal_Type.__name__ = "Integer32"
_AccV25CTSSignal_Object = MibTableColumn
accV25CTSSignal = _AccV25CTSSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 5),
    _AccV25CTSSignal_Type()
)
accV25CTSSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CTSSignal.setStatus("mandatory")
_AccV25CallAttempts_Type = Integer32
_AccV25CallAttempts_Object = MibTableColumn
accV25CallAttempts = _AccV25CallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 6),
    _AccV25CallAttempts_Type()
)
accV25CallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CallAttempts.setStatus("mandatory")
_AccV25CallSuccess_Type = Integer32
_AccV25CallSuccess_Object = MibTableColumn
accV25CallSuccess = _AccV25CallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 7),
    _AccV25CallSuccess_Type()
)
accV25CallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CallSuccess.setStatus("mandatory")
_AccEnetHub_ObjectIdentity = ObjectIdentity
accEnetHub = _AccEnetHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39)
)
_AccEnetHubStatTable_Object = MibTable
accEnetHubStatTable = _AccEnetHubStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1)
)
if mibBuilder.loadTexts:
    accEnetHubStatTable.setStatus("mandatory")
_AccEnetHubStatEntry_Object = MibTableRow
accEnetHubStatEntry = _AccEnetHubStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1)
)
accEnetHubStatEntry.setIndexNames(
    (0, "ACC-MIB", "accEnetPortIndex"),
    (0, "ACC-MIB", "accEnetHubIndex"),
)
if mibBuilder.loadTexts:
    accEnetHubStatEntry.setStatus("mandatory")
_AccEnetPortIndex_Type = Integer32
_AccEnetPortIndex_Object = MibTableColumn
accEnetPortIndex = _AccEnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 1),
    _AccEnetPortIndex_Type()
)
accEnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetPortIndex.setStatus("mandatory")
_AccEnetHubIndex_Type = Integer32
_AccEnetHubIndex_Object = MibTableColumn
accEnetHubIndex = _AccEnetHubIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 2),
    _AccEnetHubIndex_Type()
)
accEnetHubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubIndex.setStatus("mandatory")


class _AccEnetHubAdStatus_Type(Integer32):
    """Custom type accEnetHubAdStatus based on Integer32"""
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


_AccEnetHubAdStatus_Type.__name__ = "Integer32"
_AccEnetHubAdStatus_Object = MibTableColumn
accEnetHubAdStatus = _AccEnetHubAdStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 3),
    _AccEnetHubAdStatus_Type()
)
accEnetHubAdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accEnetHubAdStatus.setStatus("mandatory")


class _AccEnetHubOpStatus_Type(Integer32):
    """Custom type accEnetHubOpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disabled", 3),
          ("partitioned", 2))
    )


_AccEnetHubOpStatus_Type.__name__ = "Integer32"
_AccEnetHubOpStatus_Object = MibTableColumn
accEnetHubOpStatus = _AccEnetHubOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 4),
    _AccEnetHubOpStatus_Type()
)
accEnetHubOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubOpStatus.setStatus("mandatory")


class _AccEnetHubBitError_Type(Integer32):
    """Custom type accEnetHubBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AccEnetHubBitError_Type.__name__ = "Integer32"
_AccEnetHubBitError_Object = MibTableColumn
accEnetHubBitError = _AccEnetHubBitError_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 5),
    _AccEnetHubBitError_Type()
)
accEnetHubBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubBitError.setStatus("mandatory")


class _AccEnetHubLinkTest_Type(Integer32):
    """Custom type accEnetHubLinkTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("pass", 1))
    )


_AccEnetHubLinkTest_Type.__name__ = "Integer32"
_AccEnetHubLinkTest_Object = MibTableColumn
accEnetHubLinkTest = _AccEnetHubLinkTest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 39, 1, 1, 6),
    _AccEnetHubLinkTest_Type()
)
accEnetHubLinkTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accEnetHubLinkTest.setStatus("mandatory")
_AccUnNumIP_ObjectIdentity = ObjectIdentity
accUnNumIP = _AccUnNumIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40)
)
_AccIpNetSrcAddrTable_Object = MibTable
accIpNetSrcAddrTable = _AccIpNetSrcAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40, 1)
)
if mibBuilder.loadTexts:
    accIpNetSrcAddrTable.setStatus("mandatory")
_AccIpNetSrcAddrEntry_Object = MibTableRow
accIpNetSrcAddrEntry = _AccIpNetSrcAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40, 1, 1)
)
accIpNetSrcAddrEntry.setIndexNames(
    (0, "ACC-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    accIpNetSrcAddrEntry.setStatus("mandatory")
_AccIpNetSrcIfIndex_Type = Integer32
_AccIpNetSrcIfIndex_Object = MibTableColumn
accIpNetSrcIfIndex = _AccIpNetSrcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40, 1, 1, 1),
    _AccIpNetSrcIfIndex_Type()
)
accIpNetSrcIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNetSrcIfIndex.setStatus("mandatory")
_AccIpNetSrcAddress_Type = IpAddress
_AccIpNetSrcAddress_Object = MibTableColumn
accIpNetSrcAddress = _AccIpNetSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40, 1, 1, 2),
    _AccIpNetSrcAddress_Type()
)
accIpNetSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accIpNetSrcAddress.setStatus("mandatory")
_PysmiFakeCol2_Type = IpAddress
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 40, 1, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-MIB",
    **{"DisplayString": DisplayString,
       "SmdsAddress": SmdsAddress,
       "CallAddress": CallAddress,
       "BackupPort": BackupPort,
       "PhysicalPort": PhysicalPort,
       "acc": acc,
       "accSBAR": accSBAR,
       "accBRG": accBRG,
       "accSystem": accSystem,
       "accSysInfo": accSysInfo,
       "accUnitName": accUnitName,
       "accRomId": accRomId,
       "accSwVersion": accSwVersion,
       "accReset": accReset,
       "accMemStatTbl": accMemStatTbl,
       "accMemBlkEntSize": accMemBlkEntSize,
       "accMemBlkEntTotal": accMemBlkEntTotal,
       "accMemBlkEntMax": accMemBlkEntMax,
       "accMemBlkEntInUse": accMemBlkEntInUse,
       "accMemBlkEntFails": accMemBlkEntFails,
       "accMemBlkEntType": accMemBlkEntType,
       "accMemBlkEntAllocs": accMemBlkEntAllocs,
       "pysmiFakeCol1": pysmiFakeCol1,
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
       "accGifnoc": accGifnoc,
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
       "accIfGroupTable": accIfGroupTable,
       "accIfGroupEntry": accIfGroupEntry,
       "accIFGroupIndex": accIFGroupIndex,
       "accIFGroupName": accIFGroupName,
       "accIFGroupType": accIFGroupType,
       "accIFGroupIndexBase": accIFGroupIndexBase,
       "accIFGroupIndexMax": accIFGroupIndexMax,
       "accStp": accStp,
       "accStpPriority": accStpPriority,
       "accStpId": accStpId,
       "accStpBrAddr": accStpBrAddr,
       "accStpMode": accStpMode,
       "accStpFilterTime": accStpFilterTime,
       "accStpMcastAddr": accStpMcastAddr,
       "accStpTopChangeDet": accStpTopChangeDet,
       "accStpTopChange": accStpTopChange,
       "accStpTopChangeTimer": accStpTopChangeTimer,
       "accStpDesRoot": accStpDesRoot,
       "accStpRootPathCost": accStpRootPathCost,
       "accStpRootPort": accStpRootPort,
       "accStpMaxAge": accStpMaxAge,
       "accStpHelloTime": accStpHelloTime,
       "accStpForwardDelay": accStpForwardDelay,
       "accStpUpTime": accStpUpTime,
       "accStpTopChangeCnts": accStpTopChangeCnts,
       "accBrPort": accBrPort,
       "accBrPortInfo": accBrPortInfo,
       "accBrPortStats": accBrPortStats,
       "accBrPortInNUcastPkts": accBrPortInNUcastPkts,
       "accBrPortInUcastPkts": accBrPortInUcastPkts,
       "accBrPortInDupPkts": accBrPortInDupPkts,
       "accBrPortOutNUcastPkts": accBrPortOutNUcastPkts,
       "accBrPortOutUcastPkts": accBrPortOutUcastPkts,
       "accBrPortStpInPkts": accBrPortStpInPkts,
       "accBrPortStpOutPkts": accBrPortStpOutPkts,
       "accBrPortOutDelayDiscPkts": accBrPortOutDelayDiscPkts,
       "accBrPortOutPrioDiscPkts": accBrPortOutPrioDiscPkts,
       "accBrPortOutQLen": accBrPortOutQLen,
       "accBrPortInDiscPkts": accBrPortInDiscPkts,
       "accBrPortStpPriority": accBrPortStpPriority,
       "accBrPortId": accBrPortId,
       "accBrPortState": accBrPortState,
       "accBrPortStpPathCost": accBrPortStpPathCost,
       "accBrPortStpDesRoot": accBrPortStpDesRoot,
       "accBrPortStpDesCost": accBrPortStpDesCost,
       "accBrPortStpDesBridge": accBrPortStpDesBridge,
       "accBrPortStpDesPort": accBrPortStpDesPort,
       "accBrPortAdminStatus": accBrPortAdminStatus,
       "accBrPortLine": accBrPortLine,
       "accBrPortProtocol": accBrPortProtocol,
       "accBrPortFrDlci": accBrPortFrDlci,
       "accBrPortIndex": accBrPortIndex,
       "accBrPortXBridgeStatus": accBrPortXBridgeStatus,
       "accBridge": accBridge,
       "accBrFdbTimeout": accBrFdbTimeout,
       "accBrFdbLearnMode": accBrFdbLearnMode,
       "accBrFdbRamCurrSize": accBrFdbRamCurrSize,
       "accBrFdbRamMaxSize": accBrFdbRamMaxSize,
       "accBrFdbNvmMaxSize": accBrFdbNvmMaxSize,
       "accBrFdbTable": accBrFdbTable,
       "accBrFdbEntry": accBrFdbEntry,
       "accBrFdbEntMacAddr": accBrFdbEntMacAddr,
       "accBrFdbEntDisp": accBrFdbEntDisp,
       "accBrFdbEntPort": accBrFdbEntPort,
       "accBrFdbEntTimer": accBrFdbEntTimer,
       "accBrFpTable": accBrFpTable,
       "accBrFpEntry": accBrFpEntry,
       "accBrFpIndex": accBrFpIndex,
       "accBrFpProt": accBrFpProt,
       "accBrFpPrio": accBrFpPrio,
       "accBrFpPriDefault": accBrFpPriDefault,
       "accBrNumPorts": accBrNumPorts,
       "accBrCompress": accBrCompress,
       "accBrPortX25Table": accBrPortX25Table,
       "accBrPortX25Entry": accBrPortX25Entry,
       "accBrPortX25FacIndex": accBrPortX25FacIndex,
       "accBrMode": accBrMode,
       "accBrFilterMode": accBrFilterMode,
       "accBrFilterDefault": accBrFilterDefault,
       "accBrFilterTable": accBrFilterTable,
       "accBrFilterEntry": accBrFilterEntry,
       "accBrFilterEntDstMacAddr": accBrFilterEntDstMacAddr,
       "accBrFilterEntSrcMacAddr": accBrFilterEntSrcMacAddr,
       "accBrFilterEntDisp": accBrFilterEntDisp,
       "accBrFilterEntPort": accBrFilterEntPort,
       "accBrFilterEntLogicalOp": accBrFilterEntLogicalOp,
       "accBrFilterEntProtocol": accBrFilterEntProtocol,
       "accBrFilterDiscards": accBrFilterDiscards,
       "accBrFilterEntries": accBrFilterEntries,
       "accBrFiltIITable": accBrFiltIITable,
       "accBrFiltIIEntry": accBrFiltIIEntry,
       "accBrFiltIIEntDstMacAddr": accBrFiltIIEntDstMacAddr,
       "accBrFiltIIEntSrcMacAddr": accBrFiltIIEntSrcMacAddr,
       "accBrFiltIIEntDisp": accBrFiltIIEntDisp,
       "accBrFiltIIEntPort": accBrFiltIIEntPort,
       "accBrFiltIIEntLogicalOp": accBrFiltIIEntLogicalOp,
       "accBrFiltIIEntProtocol": accBrFiltIIEntProtocol,
       "accBrFiltIIEntDstMacAddrMask": accBrFiltIIEntDstMacAddrMask,
       "accBrFiltIIEntSrcMacAddrMask": accBrFiltIIEntSrcMacAddrMask,
       "accBrFiltIIEntStatus": accBrFiltIIEntStatus,
       "accBrFiltIIDiscards": accBrFiltIIDiscards,
       "accBrFiltIIEntries": accBrFiltIIEntries,
       "accFdbWhichAddr": accFdbWhichAddr,
       "accSlot": accSlot,
       "accSlotTable": accSlotTable,
       "accSlotEntry": accSlotEntry,
       "accSlotLastChange": accSlotLastChange,
       "accSlotInPkts": accSlotInPkts,
       "accSlotOutPkts": accSlotOutPkts,
       "accSlotNumChanges": accSlotNumChanges,
       "accSlotProtocol": accSlotProtocol,
       "accSlotClockMode": accSlotClockMode,
       "accSlotQueueMode": accSlotQueueMode,
       "accSlotDialProcedure": accSlotDialProcedure,
       "accSlotResyncMode": accSlotResyncMode,
       "accSlotCompressMode": accSlotCompressMode,
       "accSlotCompressV42bisP1": accSlotCompressV42bisP1,
       "accSlotCompressV42bisP2": accSlotCompressV42bisP2,
       "accSlotCompressDcs221P1": accSlotCompressDcs221P1,
       "accSlotSevereCongPct": accSlotSevereCongPct,
       "accSlotDialAddress": accSlotDialAddress,
       "accSlotCompressRevision": accSlotCompressRevision,
       "accSlotCompressMaxStreams": accSlotCompressMaxStreams,
       "accSlotCompressMessageLevel": accSlotCompressMessageLevel,
       "accSlotIfType": accSlotIfType,
       "accCompress": accCompress,
       "accCompressDialNeighborTable": accCompressDialNeighborTable,
       "accCompressDialNeighborEntry": accCompressDialNeighborEntry,
       "accCompressDialNeighborIfIndex": accCompressDialNeighborIfIndex,
       "accCompressDialNeighborCallAddress": accCompressDialNeighborCallAddress,
       "accCompressDialNeighborStatus": accCompressDialNeighborStatus,
       "accCompressFfrNeighborTable": accCompressFfrNeighborTable,
       "accCompressFfrNeighborEntry": accCompressFfrNeighborEntry,
       "accCompressFfrNeighborIfIndex": accCompressFfrNeighborIfIndex,
       "accCompressFfrNeighborDlci": accCompressFfrNeighborDlci,
       "accCompressFfrNeighborStatus": accCompressFfrNeighborStatus,
       "accCompressX25NeighborTable": accCompressX25NeighborTable,
       "accCompressX25NeighborEntry": accCompressX25NeighborEntry,
       "accCompressX25NeighborIfIndex": accCompressX25NeighborIfIndex,
       "accCompressX25NeighborAddress": accCompressX25NeighborAddress,
       "accCompressX25NeighborStatus": accCompressX25NeighborStatus,
       "accCompressDialStatTable": accCompressDialStatTable,
       "accCompressDialStatEntry": accCompressDialStatEntry,
       "accCompressDialStatIfIndex": accCompressDialStatIfIndex,
       "accCompressDialStatCallAddress": accCompressDialStatCallAddress,
       "accCompressDialStatStatus": accCompressDialStatStatus,
       "accCompressDialStatOctetsIns": accCompressDialStatOctetsIns,
       "accCompressDialStatOctetsOuts": accCompressDialStatOctetsOuts,
       "accCompressDialStatPacketsIns": accCompressDialStatPacketsIns,
       "accCompressDialStatPacketsOuts": accCompressDialStatPacketsOuts,
       "accCompressDialStatUnCompIns": accCompressDialStatUnCompIns,
       "accCompressDialStatUnCompOuts": accCompressDialStatUnCompOuts,
       "accCompressDialStatAvgCompIn": accCompressDialStatAvgCompIn,
       "accCompressDialStatAvgCompOut": accCompressDialStatAvgCompOut,
       "accCompressDialStatHdrErrors": accCompressDialStatHdrErrors,
       "accCompressDialStatResyncs": accCompressDialStatResyncs,
       "accCompressDialStatNoEndMarks": accCompressDialStatNoEndMarks,
       "accCompressDialStatNoBufAvails": accCompressDialStatNoBufAvails,
       "accCompressFfrStatTable": accCompressFfrStatTable,
       "accCompressFfrStatEntry": accCompressFfrStatEntry,
       "accCompressFfrStatIfIndex": accCompressFfrStatIfIndex,
       "accCompressFfrStatDlci": accCompressFfrStatDlci,
       "accCompressFfrStatStatus": accCompressFfrStatStatus,
       "accCompressFfrStatOctetsIns": accCompressFfrStatOctetsIns,
       "accCompressFfrStatOctetsOuts": accCompressFfrStatOctetsOuts,
       "accCompressFfrStatPacketsIns": accCompressFfrStatPacketsIns,
       "accCompressFfrStatPacketsOuts": accCompressFfrStatPacketsOuts,
       "accCompressFfrStatUnCompIns": accCompressFfrStatUnCompIns,
       "accCompressFfrStatUnCompOuts": accCompressFfrStatUnCompOuts,
       "accCompressFfrStatAvgCompIn": accCompressFfrStatAvgCompIn,
       "accCompressFfrStatAvgCompOut": accCompressFfrStatAvgCompOut,
       "accCompressFfrStatHdrErrors": accCompressFfrStatHdrErrors,
       "accCompressFfrStatResyncs": accCompressFfrStatResyncs,
       "accCompressFfrStatNoEndMarks": accCompressFfrStatNoEndMarks,
       "accCompressFfrStatNoBufAvails": accCompressFfrStatNoBufAvails,
       "accCompressX25StatTable": accCompressX25StatTable,
       "accCompressX25StatEntry": accCompressX25StatEntry,
       "accCompressX25StatIfIndex": accCompressX25StatIfIndex,
       "accCompressX25StatAddress": accCompressX25StatAddress,
       "accCompressX25StatStatus": accCompressX25StatStatus,
       "accCompressX25StatOctetsIns": accCompressX25StatOctetsIns,
       "accCompressX25StatOctetsOuts": accCompressX25StatOctetsOuts,
       "accCompressX25StatPacketsIns": accCompressX25StatPacketsIns,
       "accCompressX25StatPacketsOuts": accCompressX25StatPacketsOuts,
       "accCompressX25StatUnCompIns": accCompressX25StatUnCompIns,
       "accCompressX25StatUnCompOuts": accCompressX25StatUnCompOuts,
       "accCompressX25StatAvgCompIn": accCompressX25StatAvgCompIn,
       "accCompressX25StatAvgCompOut": accCompressX25StatAvgCompOut,
       "accCompressX25StatHdrErrors": accCompressX25StatHdrErrors,
       "accCompressX25StatResyncs": accCompressX25StatResyncs,
       "accCompressX25StatNoEndMarks": accCompressX25StatNoEndMarks,
       "accCompressX25StatNoBufAvails": accCompressX25StatNoBufAvails,
       "accCompressPhysStatTable": accCompressPhysStatTable,
       "accCompressPhysStatEntry": accCompressPhysStatEntry,
       "accCompressPhysStatIfIndex": accCompressPhysStatIfIndex,
       "accCompressPhysStatStatus": accCompressPhysStatStatus,
       "accCompressPhysStatOctetsIns": accCompressPhysStatOctetsIns,
       "accCompressPhysStatOctetsOuts": accCompressPhysStatOctetsOuts,
       "accCompressPhysStatPacketsIns": accCompressPhysStatPacketsIns,
       "accCompressPhysStatPacketsOuts": accCompressPhysStatPacketsOuts,
       "accCompressPhysStatUnCompIns": accCompressPhysStatUnCompIns,
       "accCompressPhysStatUnCompOuts": accCompressPhysStatUnCompOuts,
       "accCompressPhysStatAvgCompIn": accCompressPhysStatAvgCompIn,
       "accCompressPhysStatAvgCompOut": accCompressPhysStatAvgCompOut,
       "accCompressPhysStatHdrErrors": accCompressPhysStatHdrErrors,
       "accCompressPhysStatResyncs": accCompressPhysStatResyncs,
       "accCompressPhysStatNoEndMarks": accCompressPhysStatNoEndMarks,
       "accCompressPhysStatNoBufAvails": accCompressPhysStatNoBufAvails,
       "accLapb": accLapb,
       "accLapbNum": accLapbNum,
       "accLapbParmTable": accLapbParmTable,
       "accLapbParmEntry": accLapbParmEntry,
       "accLapbIndex": accLapbIndex,
       "accLapbType": accLapbType,
       "accLapbT1Timer": accLapbT1Timer,
       "accLapbN2Count": accLapbN2Count,
       "accLapbFrameWindow": accLapbFrameWindow,
       "accLapbFlags": accLapbFlags,
       "accHdlcRrPolling": accHdlcRrPolling,
       "accHdlcFCS": accHdlcFCS,
       "accLapbStatTable": accLapbStatTable,
       "accLapbStatEntry": accLapbStatEntry,
       "accLapbStatIndex": accLapbStatIndex,
       "accLapbStatBadFCSIns": accLapbStatBadFCSIns,
       "accLapbStatFRMRIns": accLapbStatFRMRIns,
       "accLapbStatT1Timeouts": accLapbStatT1Timeouts,
       "accLapbStatREJIns": accLapbStatREJIns,
       "accLapbStatREJOuts": accLapbStatREJOuts,
       "accLapbStatShortIns": accLapbStatShortIns,
       "accEnet": accEnet,
       "accEnetNum": accEnetNum,
       "accEnetParmTable": accEnetParmTable,
       "accEnetParmEntry": accEnetParmEntry,
       "accEnetPortNo": accEnetPortNo,
       "accEnetStatTable": accEnetStatTable,
       "accEnetStatEntry": accEnetStatEntry,
       "accEnetIndex": accEnetIndex,
       "accEnetStatCRCErrs": accEnetStatCRCErrs,
       "accEnetStatAlignErrs": accEnetStatAlignErrs,
       "accEnetStatOutColls": accEnetStatOutColls,
       "accEnetStatJabberConds": accEnetStatJabberConds,
       "accEnetStatCarrierLosts": accEnetStatCarrierLosts,
       "accEnetStatHeartbeatErrs": accEnetStatHeartbeatErrs,
       "accEnetStatGiants": accEnetStatGiants,
       "accEnetStatOneRetrys": accEnetStatOneRetrys,
       "accEnetStatMultRetrys": accEnetStatMultRetrys,
       "accEnetStatLateColls": accEnetStatLateColls,
       "accEnetChipCrashes": accEnetChipCrashes,
       "accMultilink": accMultilink,
       "accMultilinkParameterTable": accMultilinkParameterTable,
       "accMultilinkParameterEntry": accMultilinkParameterEntry,
       "accMultilinkParameterIndex": accMultilinkParameterIndex,
       "accMultilinkParameterIfIndex": accMultilinkParameterIfIndex,
       "accMultilinkParameterMessageLevel": accMultilinkParameterMessageLevel,
       "accMultilinkParameterAdminState": accMultilinkParameterAdminState,
       "accMultilinkParameterOperState": accMultilinkParameterOperState,
       "accMultilinkParameterEncapsulation": accMultilinkParameterEncapsulation,
       "accMultilinkParameterPhysicalPort": accMultilinkParameterPhysicalPort,
       "accMlTable": accMlTable,
       "accMlEntry": accMlEntry,
       "accMlAdminStatus": accMlAdminStatus,
       "accMultilinkStatTable": accMultilinkStatTable,
       "accMultilinkStatEntry": accMultilinkStatEntry,
       "accMultilinkStatIndex": accMultilinkStatIndex,
       "accMultilinkStatRcvInSeqs": accMultilinkStatRcvInSeqs,
       "accMultilinkStatRcvOutSeqs": accMultilinkStatRcvOutSeqs,
       "accMultilinkStatRcvOutWindows": accMultilinkStatRcvOutWindows,
       "accMultilinkStatRcvSeqBreaks": accMultilinkStatRcvSeqBreaks,
       "accMultilinkStatRcvWrongEncaps": accMultilinkStatRcvWrongEncaps,
       "accMultilinkStatRcvPendings": accMultilinkStatRcvPendings,
       "accMultilinkStatRcvRingColls": accMultilinkStatRcvRingColls,
       "accMultilinkStatSendEncapFails": accMultilinkStatSendEncapFails,
       "accMultilinkStackTable": accMultilinkStackTable,
       "accMultilinkStackEntry": accMultilinkStackEntry,
       "accMultilinkStackGroup": accMultilinkStackGroup,
       "accMultilinkStackInterface": accMultilinkStackInterface,
       "accAsPort": accAsPort,
       "accConsole": accConsole,
       "accConsoleParms": accConsoleParms,
       "accConsoleSpeed": accConsoleSpeed,
       "accArp": accArp,
       "accArpTimeout": accArpTimeout,
       "accArpTable": accArpTable,
       "accArpEntry": accArpEntry,
       "accArpPhysAddress": accArpPhysAddress,
       "accArpNetAddress": accArpNetAddress,
       "accArpEntStatus": accArpEntStatus,
       "accArpType": accArpType,
       "accArpReqRcvds": accArpReqRcvds,
       "accArpReqSents": accArpReqSents,
       "accArpRspRcvds": accArpRspRcvds,
       "accArpRspSents": accArpRspSents,
       "accArpInErrs": accArpInErrs,
       "accArpOutErrs": accArpOutErrs,
       "accArpUnknownProtos": accArpUnknownProtos,
       "accArpPromiscuous": accArpPromiscuous,
       "accArpRefresh": accArpRefresh,
       "accIpRoutingTable": accIpRoutingTable,
       "accIpRoutingEntry": accIpRoutingEntry,
       "accIpRouteDestSubnet": accIpRouteDestSubnet,
       "accProbe": accProbe,
       "accProbeAddr": accProbeAddr,
       "accProbeData": accProbeData,
       "accIpAddrTable": accIpAddrTable,
       "accIpAddrEntry": accIpAddrEntry,
       "accIpAddrMtu": accIpAddrMtu,
       "accIpAddrSecurityType": accIpAddrSecurityType,
       "accIpAddrSecurityClass": accIpAddrSecurityClass,
       "accIpAddrSecurityAuth": accIpAddrSecurityAuth,
       "accIpAddrBcastAddr": accIpAddrBcastAddr,
       "accIpAdEntMetric": accIpAdEntMetric,
       "accIpAdEntPreference": accIpAdEntPreference,
       "accEgp": accEgp,
       "accEgpNeighTable": accEgpNeighTable,
       "accEgpNeighEntry": accEgpNeighEntry,
       "accEgpUptime": accEgpUptime,
       "accEgpFAS": accEgpFAS,
       "accEgpSndSeqs": accEgpSndSeqs,
       "accEgpRcvSeqs": accEgpRcvSeqs,
       "accEgpAdminStatus": accEgpAdminStatus,
       "accEgpASNumber": accEgpASNumber,
       "accEgpMetric": accEgpMetric,
       "accEgpInErrMsgs": accEgpInErrMsgs,
       "accEgpOutErrMsgs": accEgpOutErrMsgs,
       "accEgpStateChanges": accEgpStateChanges,
       "accEgpLastChange": accEgpLastChange,
       "accRip": accRip,
       "accRipAdminStatus": accRipAdminStatus,
       "accRipUpdateTimer": accRipUpdateTimer,
       "accRipGateway": accRipGateway,
       "accRipMetric": accRipMetric,
       "accRipNeighborList": accRipNeighborList,
       "accRipNeighbor": accRipNeighbor,
       "accRipNeighborIfindex": accRipNeighborIfindex,
       "accRipInCmdCnts": accRipInCmdCnts,
       "accRipInRspCnts": accRipInRspCnts,
       "accRipInErrors": accRipInErrors,
       "accRipOutCmdCnts": accRipOutCmdCnts,
       "accRipOutRspCounts": accRipOutRspCounts,
       "accX25": accX25,
       "accX25AtTable": accX25AtTable,
       "accX25AtEntry": accX25AtEntry,
       "accX25AtIfIndex": accX25AtIfIndex,
       "accX25AtIpAddress": accX25AtIpAddress,
       "accX25AtNetInOutAddr": accX25AtNetInOutAddr,
       "accX25AtNetInAddr": accX25AtNetInAddr,
       "accX25AtNetFacIndex": accX25AtNetFacIndex,
       "accX25SubnetParmTable": accX25SubnetParmTable,
       "accX25SubnetParmEntry": accX25SubnetParmEntry,
       "accX25SubnetAddr": accX25SubnetAddr,
       "accX25Facility": accX25Facility,
       "accX25PktNegot": accX25PktNegot,
       "accX25WindowNegot": accX25WindowNegot,
       "accX25PortParmTable": accX25PortParmTable,
       "accX25PortParmEntry": accX25PortParmEntry,
       "accX25PortParmIndex": accX25PortParmIndex,
       "accX25AddrMode": accX25AddrMode,
       "accX25PktSize": accX25PktSize,
       "accX25PktWind": accX25PktWind,
       "accX25SvcNumber": accX25SvcNumber,
       "accX25SvcBase": accX25SvcBase,
       "accX25ExtendClr": accX25ExtendClr,
       "accX25ExtendSeq": accX25ExtendSeq,
       "accX25IdleMin": accX25IdleMin,
       "accX25IdleMax": accX25IdleMax,
       "accX25IdleScale": accX25IdleScale,
       "accX25SvcMax": accX25SvcMax,
       "accX25SvcLimit": accX25SvcLimit,
       "accX25OpenThresh": accX25OpenThresh,
       "accX25SvcMin": accX25SvcMin,
       "accX25SvcDelay": accX25SvcDelay,
       "accX25InitBackoff": accX25InitBackoff,
       "accX25MaxBackoff": accX25MaxBackoff,
       "accX25OurAddress": accX25OurAddress,
       "accX25PvcBase": accX25PvcBase,
       "accX25PvcNumber": accX25PvcNumber,
       "accX25Tx0Timer": accX25Tx0Timer,
       "accX25Tx1Timer": accX25Tx1Timer,
       "accX25Tx2Timer": accX25Tx2Timer,
       "accX25Tx3Timer": accX25Tx3Timer,
       "accX25PktStatTable": accX25PktStatTable,
       "accX25PktStatEntry": accX25PktStatEntry,
       "accX25PktIndex": accX25PktIndex,
       "accX25RcvDiags": accX25RcvDiags,
       "accX25RcvRestartReqs": accX25RcvRestartReqs,
       "accX25RcvRestartConfs": accX25RcvRestartConfs,
       "accX25RcvCallReqs": accX25RcvCallReqs,
       "accX25RcvCallAccs": accX25RcvCallAccs,
       "accX25RcvClrReqs": accX25RcvClrReqs,
       "accX25RcvClrConfs": accX25RcvClrConfs,
       "accX25RcvResetReqs": accX25RcvResetReqs,
       "accX25RcvResetConfs": accX25RcvResetConfs,
       "accX25RcvInts": accX25RcvInts,
       "accX25RcvIntConfs": accX25RcvIntConfs,
       "accX25RcvRRs": accX25RcvRRs,
       "accX25RcvRNRs": accX25RcvRNRs,
       "accX25RcvDatas": accX25RcvDatas,
       "accX25XmtDiags": accX25XmtDiags,
       "accX25XmtRestartReqs": accX25XmtRestartReqs,
       "accX25XmtRestartConfs": accX25XmtRestartConfs,
       "accX25XmtCallReqs": accX25XmtCallReqs,
       "accX25XmtCallAccs": accX25XmtCallAccs,
       "accX25XmtClrReqs": accX25XmtClrReqs,
       "accX25XmtClrConfs": accX25XmtClrConfs,
       "accX25XmtResetReqs": accX25XmtResetReqs,
       "accX25XmtResetConfs": accX25XmtResetConfs,
       "accX25XmtInts": accX25XmtInts,
       "accX25XmtIntConfs": accX25XmtIntConfs,
       "accX25XmtRRs": accX25XmtRRs,
       "accX25XmtRNRs": accX25XmtRNRs,
       "accX25XmtDatas": accX25XmtDatas,
       "accX25OpenSvcCounts": accX25OpenSvcCounts,
       "accX25OptFacTable": accX25OptFacTable,
       "accX25OptFacEntry": accX25OptFacEntry,
       "accX25OptFacIndex": accX25OptFacIndex,
       "accX25OptFacString": accX25OptFacString,
       "accX25PvcAddrTable": accX25PvcAddrTable,
       "accX25PvcAddrEntry": accX25PvcAddrEntry,
       "accX25PvcLine": accX25PvcLine,
       "accX25PvcAddrLcid": accX25PvcAddrLcid,
       "accX25PvcAddrString": accX25PvcAddrString,
       "accX25PvcProtocol": accX25PvcProtocol,
       "accX25ErrorTable": accX25ErrorTable,
       "accX25ErrorEntry": accX25ErrorEntry,
       "accX25ErrorLine": accX25ErrorLine,
       "accX25ErrorUpTime": accX25ErrorUpTime,
       "accX25ErrorSeq": accX25ErrorSeq,
       "accX25ErrorState": accX25ErrorState,
       "accX25ErrorProtocol": accX25ErrorProtocol,
       "accX25ErrorCause": accX25ErrorCause,
       "accX25ErrorDiag": accX25ErrorDiag,
       "accX25ErrorPacket": accX25ErrorPacket,
       "accX25Switch": accX25Switch,
       "accX25SwitchStatus": accX25SwitchStatus,
       "accX25SwitchConnections": accX25SwitchConnections,
       "accX25SwitchCallSucceeds": accX25SwitchCallSucceeds,
       "accX25SwitchCallFails": accX25SwitchCallFails,
       "accX25SwitchConnTable": accX25SwitchConnTable,
       "accX25SwitchConnEntry": accX25SwitchConnEntry,
       "accX25SwitchConnCallingIfIndex": accX25SwitchConnCallingIfIndex,
       "accX25SwitchConnCallingIndex": accX25SwitchConnCallingIndex,
       "accX25SwitchConnCallingType": accX25SwitchConnCallingType,
       "accX25SwitchConnCallingX121Addr": accX25SwitchConnCallingX121Addr,
       "accX25SwitchConnCallingPkts": accX25SwitchConnCallingPkts,
       "accX25SwitchConnCallingOctets": accX25SwitchConnCallingOctets,
       "accX25SwitchConnCalledIfIndex": accX25SwitchConnCalledIfIndex,
       "accX25SwitchConnCalledIndex": accX25SwitchConnCalledIndex,
       "accX25SwitchConnCalledType": accX25SwitchConnCalledType,
       "accX25SwitchConnCalledX121Addr": accX25SwitchConnCalledX121Addr,
       "accX25SwitchConnCalledPkts": accX25SwitchConnCalledPkts,
       "accX25SwitchConnCalledOctets": accX25SwitchConnCalledOctets,
       "accX25SwitchConnState": accX25SwitchConnState,
       "accX25SwitchAddrTransTable": accX25SwitchAddrTransTable,
       "accX25SwitchAddrTransEntry": accX25SwitchAddrTransEntry,
       "accX25SwitchAddrTransIfIndex": accX25SwitchAddrTransIfIndex,
       "accX25SwitchAddrTransDir": accX25SwitchAddrTransDir,
       "accX25SwitchAddrTransType": accX25SwitchAddrTransType,
       "accX25SwitchAddrTransPattern": accX25SwitchAddrTransPattern,
       "accX25SwitchAddrTransReplace": accX25SwitchAddrTransReplace,
       "accX25SwitchAddrTransStatus": accX25SwitchAddrTransStatus,
       "accX25SwitchRouteTable": accX25SwitchRouteTable,
       "accX25SwitchRouteEntry": accX25SwitchRouteEntry,
       "accX25SwitchRoutePattern": accX25SwitchRoutePattern,
       "accX25SwitchRouteIfIndex": accX25SwitchRouteIfIndex,
       "accX25SwitchRouteStatus": accX25SwitchRouteStatus,
       "accX25SwitchExtRtTable": accX25SwitchExtRtTable,
       "accX25SwitchExtRtEntry": accX25SwitchExtRtEntry,
       "accX25SwitchExtRtIndex": accX25SwitchExtRtIndex,
       "accX25SwitchExtRtIfIn": accX25SwitchExtRtIfIn,
       "accX25SwitchExtRtAddr": accX25SwitchExtRtAddr,
       "accX25SwitchExtRtCUD": accX25SwitchExtRtCUD,
       "accX25SwitchExtRtDisp": accX25SwitchExtRtDisp,
       "accX25SwitchExtRtIfOut": accX25SwitchExtRtIfOut,
       "accX25SwitchExtRtStatus": accX25SwitchExtRtStatus,
       "accIpFilter": accIpFilter,
       "accIpSrcRouting": accIpSrcRouting,
       "accIpFiltTable": accIpFiltTable,
       "accIpFiltEntry": accIpFiltEntry,
       "accIpFiltDAddr": accIpFiltDAddr,
       "accIpFiltDNetMask": accIpFiltDNetMask,
       "accIpFiltSAddr": accIpFiltSAddr,
       "accIpFiltSNetMask": accIpFiltSNetMask,
       "accIpFiltParm": accIpFiltParm,
       "accIpFiltDisp": accIpFiltDisp,
       "oIpSubDirBcast": oIpSubDirBcast,
       "accIpIfFiltDispTable": accIpIfFiltDispTable,
       "accIpIfFiltDispEntry": accIpIfFiltDispEntry,
       "accIpIfFiltDispIfIndex": accIpIfFiltDispIfIndex,
       "accIpIfFiltDispPktDir": accIpIfFiltDispPktDir,
       "accIpIfFiltDispSeqNum": accIpIfFiltDispSeqNum,
       "accIpIfFiltDispDAddr": accIpIfFiltDispDAddr,
       "accIpIfFiltDispDNetMask": accIpIfFiltDispDNetMask,
       "accIpIfFiltDispSAddr": accIpIfFiltDispSAddr,
       "accIpIfFiltDispSNetMask": accIpIfFiltDispSNetMask,
       "accIpIfFiltDispOp1": accIpIfFiltDispOp1,
       "accIpIfFiltDispProtocol": accIpIfFiltDispProtocol,
       "accIpIfFiltDispOp2": accIpIfFiltDispOp2,
       "accIpIfFiltDispUDPTCPPort": accIpIfFiltDispUDPTCPPort,
       "accIpIfFiltDispDispos": accIpIfFiltDispDispos,
       "accIpIfFiltDispMatches": accIpIfFiltDispMatches,
       "accIpIfFiltDispLastMatchTime": accIpIfFiltDispLastMatchTime,
       "accIpIfFiltDispMatchPkt": accIpIfFiltDispMatchPkt,
       "accIpIfFiltEditTable": accIpIfFiltEditTable,
       "accIpIfFiltEditEntry": accIpIfFiltEditEntry,
       "accIpIfFiltEditIndex": accIpIfFiltEditIndex,
       "accIpIfFiltEditAction": accIpIfFiltEditAction,
       "accIpIfFiltEditIfIndex": accIpIfFiltEditIfIndex,
       "accIpIfFiltEditPktDir": accIpIfFiltEditPktDir,
       "accIpIfFiltEditDAddr": accIpIfFiltEditDAddr,
       "accIpIfFiltEditDNetMask": accIpIfFiltEditDNetMask,
       "accIpIfFiltEditSAddr": accIpIfFiltEditSAddr,
       "accIpIfFiltEditSNetMask": accIpIfFiltEditSNetMask,
       "accIpIfFiltEditOp1": accIpIfFiltEditOp1,
       "accIpIfFiltEditProtocol": accIpIfFiltEditProtocol,
       "accIpIfFiltEditOp2": accIpIfFiltEditOp2,
       "accIpIfFiltEditUDPTCPPort": accIpIfFiltEditUDPTCPPort,
       "accIpIfFiltEditDispos": accIpIfFiltEditDispos,
       "accDn": accDn,
       "accDnNumber": accDnNumber,
       "accDnID": accDnID,
       "accDnMaxNode": accDnMaxNode,
       "accDnMaxArea": accDnMaxArea,
       "accDnMaxAdjRtr": accDnMaxAdjRtr,
       "accDnMaxEndNode": accDnMaxEndNode,
       "accDnMaxLocHop": accDnMaxLocHop,
       "accDnMaxLocCost": accDnMaxLocCost,
       "accDnMaxVisit": accDnMaxVisit,
       "accDnMaxForHop": accDnMaxForHop,
       "accDnMaxForCost": accDnMaxForCost,
       "accDnBCT1": accDnBCT1,
       "accDnT1": accDnT1,
       "accDnMsgLev": accDnMsgLev,
       "accDnNodeState": accDnNodeState,
       "accDnUnreachs": accDnUnreachs,
       "accDnVisitXcds": accDnVisitXcds,
       "accDnBadNodes": accDnBadNodes,
       "accDnPktOsizes": accDnPktOsizes,
       "accDnFmtErrs": accDnFmtErrs,
       "accDnCktTable": accDnCktTable,
       "accDnCktEntry": accDnCktEntry,
       "accDnCktIndex": accDnCktIndex,
       "accDnCktStatus": accDnCktStatus,
       "accDnCktState": accDnCktState,
       "accDnCktCost": accDnCktCost,
       "accDnMaxRtr": accDnMaxRtr,
       "accDnHelloInt": accDnHelloInt,
       "accDnRtrPriority": accDnRtrPriority,
       "accDnDesRtrId": accDnDesRtrId,
       "accDnDesRtrPrio": accDnDesRtrPrio,
       "accDnTrnPktRecs": accDnTrnPktRecs,
       "accDnTrnPktSnds": accDnTrnPktSnds,
       "accDnEndNodePktRecs": accDnEndNodePktRecs,
       "accDnEndNodePktSnds": accDnEndNodePktSnds,
       "accDnCktDowns": accDnCktDowns,
       "accDnCktType": accDnCktType,
       "accDnCktPort": accDnCktPort,
       "accDnX25InOutAddr": accDnX25InOutAddr,
       "accDnX25InAddr": accDnX25InAddr,
       "accDnX25Idle": accDnX25Idle,
       "accDnX25PktVal": accDnX25PktVal,
       "accDnX25PktWin": accDnX25PktWin,
       "accDnEntryStatus": accDnEntryStatus,
       "accDnX25FacIndex": accDnX25FacIndex,
       "accDnRtTable": accDnRtTable,
       "accDnRtEntry": accDnRtEntry,
       "accDnRtNode": accDnRtNode,
       "accDnRtHops": accDnRtHops,
       "accDnRtCost": accDnRtCost,
       "accDnRtCkt": accDnRtCkt,
       "accDnRtNextHop": accDnRtNextHop,
       "accDnAreaTable": accDnAreaTable,
       "accDnAreaEntry": accDnAreaEntry,
       "accDnAreaArea": accDnAreaArea,
       "accDnAreaHops": accDnAreaHops,
       "accDnAreaCost": accDnAreaCost,
       "accDnAreaCkt": accDnAreaCkt,
       "accDnAreaNextHop": accDnAreaNextHop,
       "accDnRouteFilterTable": accDnRouteFilterTable,
       "accDnRouteFilterEntry": accDnRouteFilterEntry,
       "accDnRouteFilterAdj": accDnRouteFilterAdj,
       "accDnRouteFilterNode": accDnRouteFilterNode,
       "accDnRouteFilterDisposition": accDnRouteFilterDisposition,
       "accDnRouteFilterEntStat": accDnRouteFilterEntStat,
       "accDnForwardFilterTable": accDnForwardFilterTable,
       "accDnForwardFilterEntry": accDnForwardFilterEntry,
       "accDnForwardFilterDest": accDnForwardFilterDest,
       "accDnForwardFilterSource": accDnForwardFilterSource,
       "accDnForwardFilterDisposition": accDnForwardFilterDisposition,
       "accDnForwardFilterEntStat": accDnForwardFilterEntStat,
       "accDnAdjTable": accDnAdjTable,
       "accDnAdjEntry": accDnAdjEntry,
       "accDnAdjNode": accDnAdjNode,
       "accDnAdjType": accDnAdjType,
       "accDnAdjCircuit": accDnAdjCircuit,
       "accDnAdjState": accDnAdjState,
       "accFr": accFr,
       "accFrAtTable": accFrAtTable,
       "accFrAtEntry": accFrAtEntry,
       "accFrAtIfIndex": accFrAtIfIndex,
       "accFrIpAddress": accFrIpAddress,
       "accFrDLCI": accFrDLCI,
       "accFrStatus": accFrStatus,
       "accFrStatTable": accFrStatTable,
       "accFrStatEntry": accFrStatEntry,
       "accFrIndex": accFrIndex,
       "accFrStatRcvDrops": accFrStatRcvDrops,
       "accFrStatShorts": accFrStatShorts,
       "accFrStatIllDlcis": accFrStatIllDlcis,
       "accFrStatUnkDlcis": accFrStatUnkDlcis,
       "accFrStatUnkProtos": accFrStatUnkProtos,
       "accFrStatRsrvDlcis": accFrStatRsrvDlcis,
       "accFrStatXmtDrops": accFrStatXmtDrops,
       "accFrStatErrTime": accFrStatErrTime,
       "accFrStatErrType": accFrStatErrType,
       "accFrStatErrDlci": accFrStatErrDlci,
       "accFrStatErrProto": accFrStatErrProto,
       "accFrLinkState": accFrLinkState,
       "accFrStatUnks": accFrStatUnks,
       "accFrStatRcvLongs": accFrStatRcvLongs,
       "accFrStatIlgDlcis": accFrStatIlgDlcis,
       "accFrStatProtoErrs": accFrStatProtoErrs,
       "accFrStatUnkIes": accFrStatUnkIes,
       "accFrStatSeqErrs": accFrStatSeqErrs,
       "accFrStatUnkRpts": accFrStatUnkRpts,
       "accFrParmTable": accFrParmTable,
       "accFrParmEntry": accFrParmEntry,
       "accFrParmIndex": accFrParmIndex,
       "accFrParmAddrFmt": accFrParmAddrFmt,
       "accFrParmAddrLen": accFrParmAddrLen,
       "accFrParmEncap": accFrParmEncap,
       "accFrDlcmiState": accFrDlcmiState,
       "accFrDlcmiPollInt": accFrDlcmiPollInt,
       "accFrDlcmiFullStatEnq": accFrDlcmiFullStatEnq,
       "accFrDlcmiErrThres": accFrDlcmiErrThres,
       "accFrDlcmiMonEvents": accFrDlcmiMonEvents,
       "accFrDlcmiType": accFrDlcmiType,
       "accFrDlcmiIdleTimer": accFrDlcmiIdleTimer,
       "accFrCktTable": accFrCktTable,
       "accFrCktEntry": accFrCktEntry,
       "accFrCktIfIndex": accFrCktIfIndex,
       "accFrCktDlci": accFrCktDlci,
       "accFrCktState": accFrCktState,
       "accFrCktFECNrcvds": accFrCktFECNrcvds,
       "accFrCktBECNrcvds": accFrCktBECNrcvds,
       "accFrCktFrameXmts": accFrCktFrameXmts,
       "accFrCktOctetXmts": accFrCktOctetXmts,
       "accFrCktFrameRcvs": accFrCktFrameRcvs,
       "accFrCktOctetRcvs": accFrCktOctetRcvs,
       "accFrCktCreateTime": accFrCktCreateTime,
       "accFrCktChangeTime": accFrCktChangeTime,
       "accFfrCktLoop": accFfrCktLoop,
       "accFfrSwitchParameterTable": accFfrSwitchParameterTable,
       "accFfrSwitchParameterEntry": accFfrSwitchParameterEntry,
       "accFfrSwitchIfindex1": accFfrSwitchIfindex1,
       "accFfrSwitchDlci1": accFfrSwitchDlci1,
       "accFfrSwitchIfindex2": accFfrSwitchIfindex2,
       "accFfrSwitchDlci2": accFfrSwitchDlci2,
       "accFfrSwitchStatus": accFfrSwitchStatus,
       "accXns": accXns,
       "accXnsParms": accXnsParms,
       "accXnsAdStat": accXnsAdStat,
       "accXnsCkSum": accXnsCkSum,
       "accXnsSpltHorz": accXnsSpltHorz,
       "accXnsAllNets": accXnsAllNets,
       "accXnsMode": accXnsMode,
       "accXnsNetTable": accXnsNetTable,
       "accXnsNetEntry": accXnsNetEntry,
       "accXnsNetPort": accXnsNetPort,
       "accXnsNetNumber": accXnsNetNumber,
       "accXnsNetType": accXnsNetType,
       "accXnsNetEncap": accXnsNetEncap,
       "accXnsNetSlot": accXnsNetSlot,
       "accXnsNetAdStat": accXnsNetAdStat,
       "accXnsNetMtu": accXnsNetMtu,
       "accXnsNetUpdate": accXnsNetUpdate,
       "accXnsNetHops": accXnsNetHops,
       "accXnsNetCost": accXnsNetCost,
       "accXnsNetX25InOutAddr": accXnsNetX25InOutAddr,
       "accXnsNetX25InAddr": accXnsNetX25InAddr,
       "accXnsNetX25Idle": accXnsNetX25Idle,
       "accXnsNetX25PktVal": accXnsNetX25PktVal,
       "accXnsNetX25PktWin": accXnsNetX25PktWin,
       "accXnsNetEntryStat": accXnsNetEntryStat,
       "accXnsNetUbUpdate": accXnsNetUbUpdate,
       "accXnsNetUbTtl": accXnsNetUbTtl,
       "accXnsNetUbQT1": accXnsNetUbQT1,
       "accXnsNetUbQT2": accXnsNetUbQT2,
       "accXnsNetFncAddr": accXnsNetFncAddr,
       "accXnsNetSrMode": accXnsNetSrMode,
       "accXnsNetX25FacIndex": accXnsNetX25FacIndex,
       "accXnsNetDlci": accXnsNetDlci,
       "accXnsRouteTable": accXnsRouteTable,
       "accXnsRouteEntry": accXnsRouteEntry,
       "accXnsRtDest": accXnsRtDest,
       "accXnsRtNxtNet": accXnsRtNxtNet,
       "accXnsRtRouter": accXnsRtRouter,
       "accXnsRtHops": accXnsRtHops,
       "accXnsRtCost": accXnsRtCost,
       "accXnsRtType": accXnsRtType,
       "accXnsRtOwner": accXnsRtOwner,
       "accXnsRtAge": accXnsRtAge,
       "accXnsRtPort": accXnsRtPort,
       "accXnsRipStat": accXnsRipStat,
       "accXnsRipReqIns": accXnsRipReqIns,
       "accXnsRipRespIns": accXnsRipRespIns,
       "accXnsRipReqOuts": accXnsRipReqOuts,
       "accXnsRipRespOuts": accXnsRipRespOuts,
       "accXnsRipInErrs": accXnsRipInErrs,
       "accXnsRipOutErrs": accXnsRipOutErrs,
       "accXnsNodeStat": accXnsNodeStat,
       "accXnsLocalIns": accXnsLocalIns,
       "accXnsLocalOuts": accXnsLocalOuts,
       "accXnsNoSockets": accXnsNoSockets,
       "accXnsNoRoutes": accXnsNoRoutes,
       "accXnsNodeInErrs": accXnsNodeInErrs,
       "accXnsOutErrs": accXnsOutErrs,
       "accXnsAllNetsIns": accXnsAllNetsIns,
       "accXnsAllNetsOuts": accXnsAllNetsOuts,
       "accXnsAllNetsErrs": accXnsAllNetsErrs,
       "accXnsPortStatTable": accXnsPortStatTable,
       "accXnsPortStatEntry": accXnsPortStatEntry,
       "accXnsPortNumber": accXnsPortNumber,
       "accXnsPortTotalIns": accXnsPortTotalIns,
       "accXnsPorFwdReqIns": accXnsPorFwdReqIns,
       "accXnsPortNoFwdRts": accXnsPortNoFwdRts,
       "accXnsPortTotalOuts": accXnsPortTotalOuts,
       "accXnsPortHopCnts": accXnsPortHopCnts,
       "accXnsPortNotForMes": accXnsPortNotForMes,
       "accXnsPortFwdReqOuts": accXnsPortFwdReqOuts,
       "accXnsPortFwdErrs": accXnsPortFwdErrs,
       "accXnsPortInErrs": accXnsPortInErrs,
       "accXnsPortTooShorts": accXnsPortTooShorts,
       "accXnsPortCkSums": accXnsPortCkSums,
       "accXnsPortTooLongs": accXnsPortTooLongs,
       "accXnsPortOutErrs": accXnsPortOutErrs,
       "accXnsPortOpState": accXnsPortOpState,
       "accXnsUbNbrTable": accXnsUbNbrTable,
       "accXnsUbNbrEntry": accXnsUbNbrEntry,
       "accXnsUbnRmtNet": accXnsUbnRmtNet,
       "accXnsUbnLclNet": accXnsUbnLclNet,
       "accXnsUbnRouter": accXnsUbnRouter,
       "accXnsUbnHops": accXnsUbnHops,
       "accXnsUbnCost": accXnsUbnCost,
       "accXnsUbnState": accXnsUbnState,
       "accXnsUbnTtl": accXnsUbnTtl,
       "accXnsUbRip": accXnsUbRip,
       "accXnsUbRipRespIns": accXnsUbRipRespIns,
       "accXnsUbRipHelloIns": accXnsUbRipHelloIns,
       "accXnsUbRipConHelIns": accXnsUbRipConHelIns,
       "accXnsUbRipUnConHelIns": accXnsUbRipUnConHelIns,
       "accXnsUbRipRedirIns": accXnsUbRipRedirIns,
       "accXnsUbRipRespOuts": accXnsUbRipRespOuts,
       "accXnsUbRipHelloOuts": accXnsUbRipHelloOuts,
       "accXnsUbRipConHelOuts": accXnsUbRipConHelOuts,
       "accXnsUbRipUnConHelOuts": accXnsUbRipUnConHelOuts,
       "accXnsUbRipRedirOuts": accXnsUbRipRedirOuts,
       "accXnsUbNoRoutes": accXnsUbNoRoutes,
       "accXnsUbInErrs": accXnsUbInErrs,
       "accXnsUbOutErrs": accXnsUbOutErrs,
       "accXnsRouteFilters": accXnsRouteFilters,
       "accXnsRteFltrDefaultAction": accXnsRteFltrDefaultAction,
       "accXnsRteNbrTable": accXnsRteNbrTable,
       "accXnsRteNbrEntry": accXnsRteNbrEntry,
       "accXnsRteNbrId": accXnsRteNbrId,
       "accXnsRteNbrAction": accXnsRteNbrAction,
       "accXnsRteNbrStatus": accXnsRteNbrStatus,
       "accXnsRteFltrTable": accXnsRteFltrTable,
       "accXnsRteFltrEntry": accXnsRteFltrEntry,
       "accXnsRteFltrNeighbor": accXnsRteFltrNeighbor,
       "accXnsRteFltrNetwork": accXnsRteFltrNetwork,
       "accXnsRteFltrAction": accXnsRteFltrAction,
       "accXnsRteFltrStatus": accXnsRteFltrStatus,
       "accXnsNetworkFilters": accXnsNetworkFilters,
       "accXnsNetFltrDefaultAction": accXnsNetFltrDefaultAction,
       "oldXnsNetFltrTable": oldXnsNetFltrTable,
       "oldXnsNetFltrEntry": oldXnsNetFltrEntry,
       "oldXnsNetFltrDestination": oldXnsNetFltrDestination,
       "oldXnsNetFltrSource": oldXnsNetFltrSource,
       "oldXnsNetFltrAction": oldXnsNetFltrAction,
       "oldXnsNetFltrStatus": oldXnsNetFltrStatus,
       "accXnsNetFltrTable": accXnsNetFltrTable,
       "accXnsNetFltrEntry": accXnsNetFltrEntry,
       "accXnsNetFltrDestination": accXnsNetFltrDestination,
       "accXnsNetFltrSource": accXnsNetFltrSource,
       "accXnsNetFltrAction": accXnsNetFltrAction,
       "accXnsNetFltrStatus": accXnsNetFltrStatus,
       "accXnsNetFltrDestSkt": accXnsNetFltrDestSkt,
       "accXnsNetFltrSrcSkt": accXnsNetFltrSrcSkt,
       "accXnsNetFltrPktType": accXnsNetFltrPktType,
       "accXnsHostFilters": accXnsHostFilters,
       "accXnsHostFltrDefaultAction": accXnsHostFltrDefaultAction,
       "accXnsHostFltrTable": accXnsHostFltrTable,
       "accXnsHostFltrEntry": accXnsHostFltrEntry,
       "accXnsHostFltrId": accXnsHostFltrId,
       "accXnsHostFltrSocket": accXnsHostFltrSocket,
       "accXnsHostFltrPepClient": accXnsHostFltrPepClient,
       "accXnsHostFltrAction": accXnsHostFltrAction,
       "accXnsHostFltrStatus": accXnsHostFltrStatus,
       "accIpx": accIpx,
       "accIpxParms": accIpxParms,
       "accIpxAdStat": accIpxAdStat,
       "accIpxCkSum": accIpxCkSum,
       "accIpxSpltHorz": accIpxSpltHorz,
       "accIpxAllNets": accIpxAllNets,
       "accIpxMode": accIpxMode,
       "accIpxWdFilter": accIpxWdFilter,
       "accIpxNetTable": accIpxNetTable,
       "accIpxNetEntry": accIpxNetEntry,
       "accIpxNetPort": accIpxNetPort,
       "accIpxNetNumber": accIpxNetNumber,
       "accIpxNetType": accIpxNetType,
       "accIpxNetEncap": accIpxNetEncap,
       "accIpxNetSlot": accIpxNetSlot,
       "accIpxNetAdStat": accIpxNetAdStat,
       "accIpxNetMtu": accIpxNetMtu,
       "accIpxNetUpdate": accIpxNetUpdate,
       "accIpxNetHops": accIpxNetHops,
       "accIpxNetCost": accIpxNetCost,
       "accIpxNetX25InOutAddr": accIpxNetX25InOutAddr,
       "accIpxNetX25InAddr": accIpxNetX25InAddr,
       "accIpxNetX25Idle": accIpxNetX25Idle,
       "accIpxNetX25PktVal": accIpxNetX25PktVal,
       "accIpxNetX25PktWin": accIpxNetX25PktWin,
       "accIpxNetEntryStat": accIpxNetEntryStat,
       "accIpxNetFncAddr": accIpxNetFncAddr,
       "accIpxNetSrMode": accIpxNetSrMode,
       "accIpxNetX25FacIndex": accIpxNetX25FacIndex,
       "accIpxNetDlci": accIpxNetDlci,
       "accIpxNetWdState": accIpxNetWdState,
       "accIpxRtTable": accIpxRtTable,
       "accIpxRtEntry": accIpxRtEntry,
       "accIpxRtDest": accIpxRtDest,
       "accIpxRtNxtNet": accIpxRtNxtNet,
       "accIpxRtRouter": accIpxRtRouter,
       "accIpxRtHops": accIpxRtHops,
       "accIpxRtCost": accIpxRtCost,
       "accIpxRtType": accIpxRtType,
       "accIpxRtOwner": accIpxRtOwner,
       "accIpxRtAge": accIpxRtAge,
       "accIpxRtPort": accIpxRtPort,
       "accIpxRipStat": accIpxRipStat,
       "accIpxRipReqIns": accIpxRipReqIns,
       "accIpxRipRespIns": accIpxRipRespIns,
       "accIpxRipReqOuts": accIpxRipReqOuts,
       "accIpxRipRespOuts": accIpxRipRespOuts,
       "accIpxRipErrIns": accIpxRipErrIns,
       "accIpxRipErrOuts": accIpxRipErrOuts,
       "accIpxNodeStat": accIpxNodeStat,
       "accIpxLocalIns": accIpxLocalIns,
       "accIpxLocalOuts": accIpxLocalOuts,
       "accIpxNoSockets": accIpxNoSockets,
       "accIpxNoRoutes": accIpxNoRoutes,
       "accIpxNodeInErrs": accIpxNodeInErrs,
       "accIpxOutErrs": accIpxOutErrs,
       "accIpxAllNetsIns": accIpxAllNetsIns,
       "accIpxAllNetsOuts": accIpxAllNetsOuts,
       "accIpxAllNetsErrs": accIpxAllNetsErrs,
       "accIpxPortStatTable": accIpxPortStatTable,
       "accIpxPortStatEntry": accIpxPortStatEntry,
       "accIpxPortNumber": accIpxPortNumber,
       "accIpxPortTotalIns": accIpxPortTotalIns,
       "accIpxPorFwdReqIns": accIpxPorFwdReqIns,
       "accIpxPortNoFwdRts": accIpxPortNoFwdRts,
       "accIpxPortTotalOuts": accIpxPortTotalOuts,
       "accIpxPortHopCnts": accIpxPortHopCnts,
       "accIpxPortNotForMes": accIpxPortNotForMes,
       "accIpxPortFwdReqOuts": accIpxPortFwdReqOuts,
       "accIpxPortFwdErrs": accIpxPortFwdErrs,
       "accIpxPortInErrs": accIpxPortInErrs,
       "accIpxPortTooShorts": accIpxPortTooShorts,
       "accIpxPortCkSums": accIpxPortCkSums,
       "accIpxPortTooLongs": accIpxPortTooLongs,
       "accIpxPortOutErrs": accIpxPortOutErrs,
       "accIpxPortOpState": accIpxPortOpState,
       "accIpxSapStat": accIpxSapStat,
       "accIpxSapReqIns": accIpxSapReqIns,
       "accIpxSapReqOuts": accIpxSapReqOuts,
       "accIpxSapRespIns": accIpxSapRespIns,
       "accIpxSapRespOuts": accIpxSapRespOuts,
       "accIpxSapGetNearIns": accIpxSapGetNearIns,
       "accIpxSapGetNearOuts": accIpxSapGetNearOuts,
       "accIpxSapNoRoutes": accIpxSapNoRoutes,
       "accIpxSapNotBests": accIpxSapNotBests,
       "accIpxSapNoServers": accIpxSapNoServers,
       "accIpxSapInErrs": accIpxSapInErrs,
       "accIpxSapOutErrs": accIpxSapOutErrs,
       "accIpxSrvTable": accIpxSrvTable,
       "accIpxSrvEntry": accIpxSrvEntry,
       "accIpxSrvName": accIpxSrvName,
       "accIpxSrvType": accIpxSrvType,
       "accIpxSrvHost": accIpxSrvHost,
       "accIpxSrvHops": accIpxSrvHops,
       "accIpxSrvOwner": accIpxSrvOwner,
       "accIpxSrvAge": accIpxSrvAge,
       "accIpxRouteFilters": accIpxRouteFilters,
       "accIpxRteFltrDefaultAction": accIpxRteFltrDefaultAction,
       "accIpxRteNbrTable": accIpxRteNbrTable,
       "accIpxRteNbrEntry": accIpxRteNbrEntry,
       "accIpxRteNbrId": accIpxRteNbrId,
       "accIpxRteNbrAction": accIpxRteNbrAction,
       "accIpxRteNbrStatus": accIpxRteNbrStatus,
       "accIpxRteFltrTable": accIpxRteFltrTable,
       "accIpxRteFltrEntry": accIpxRteFltrEntry,
       "accIpxRteFltrNeighbor": accIpxRteFltrNeighbor,
       "accIpxRteFltrNetwork": accIpxRteFltrNetwork,
       "accIpxRteFltrAction": accIpxRteFltrAction,
       "accIpxRteFltrStatus": accIpxRteFltrStatus,
       "accIpxNetworkFilters": accIpxNetworkFilters,
       "accIpxNetFltrDefaultAction": accIpxNetFltrDefaultAction,
       "oldIpxNetFltrTable": oldIpxNetFltrTable,
       "oldIpxNetFltrEntry": oldIpxNetFltrEntry,
       "oldIpxNetFltrDestination": oldIpxNetFltrDestination,
       "oldIpxNetFltrSource": oldIpxNetFltrSource,
       "oldIpxNetFltrAction": oldIpxNetFltrAction,
       "oldIpxNetFltrStatus": oldIpxNetFltrStatus,
       "accIpxNetFltrTable": accIpxNetFltrTable,
       "accIpxNetFltrEntry": accIpxNetFltrEntry,
       "accIpxNetFltrDestination": accIpxNetFltrDestination,
       "accIpxNetFltrSource": accIpxNetFltrSource,
       "accIpxNetFltrAction": accIpxNetFltrAction,
       "accIpxNetFltrStatus": accIpxNetFltrStatus,
       "accIpxNetFltrDestSkt": accIpxNetFltrDestSkt,
       "accIpxNetFltrSrcSkt": accIpxNetFltrSrcSkt,
       "accIpxNetFltrPktType": accIpxNetFltrPktType,
       "accIpxHostFilters": accIpxHostFilters,
       "accIpxHostFltrDefaultAction": accIpxHostFltrDefaultAction,
       "accIpxHostFltrTable": accIpxHostFltrTable,
       "accIpxHostFltrEntry": accIpxHostFltrEntry,
       "accIpxHostFltrId": accIpxHostFltrId,
       "accIpxHostFltrSocket": accIpxHostFltrSocket,
       "accIpxHostFltrPepClient": accIpxHostFltrPepClient,
       "accIpxHostFltrAction": accIpxHostFltrAction,
       "accIpxHostFltrStatus": accIpxHostFltrStatus,
       "accIpxSapFilters": accIpxSapFilters,
       "accIpxSapFltrDefault": accIpxSapFltrDefault,
       "accIpxSapFltrTable": accIpxSapFltrTable,
       "accIpxSapFltrEntry": accIpxSapFltrEntry,
       "accIpxSapFltrSrvType": accIpxSapFltrSrvType,
       "accIpxSapFltrSrvName": accIpxSapFltrSrvName,
       "accIpxSapFltrAction": accIpxSapFltrAction,
       "accIpxSapFltrStatus": accIpxSapFltrStatus,
       "accIpxNetWdParms": accIpxNetWdParms,
       "accIpxWdProxyDuration": accIpxWdProxyDuration,
       "accIpxWdHoldPeriod": accIpxWdHoldPeriod,
       "accIpxWdMaxSessions": accIpxWdMaxSessions,
       "accIpxWdDiagLevel": accIpxWdDiagLevel,
       "ipMultiPathTable": ipMultiPathTable,
       "ipMultiPathEntry": ipMultiPathEntry,
       "ipMultiPathDest": ipMultiPathDest,
       "ipMultiPathPolicy": ipMultiPathPolicy,
       "ipMultiPathIfIndex": ipMultiPathIfIndex,
       "ipMultiPathMask": ipMultiPathMask,
       "ipMultiPathNextHop": ipMultiPathNextHop,
       "ipMultiPathMetric": ipMultiPathMetric,
       "ipMultiPathType": ipMultiPathType,
       "ipMultiPathProto": ipMultiPathProto,
       "ipMultiPathAge": ipMultiPathAge,
       "accTr": accTr,
       "accTrNumber": accTrNumber,
       "accTrTable": accTrTable,
       "accTrEntry": accTrEntry,
       "accTrEarlyRelease": accTrEarlyRelease,
       "accTrMACAddr": accTrMACAddr,
       "accTrDefaultRingId": accTrDefaultRingId,
       "accTrActiveRingId": accTrActiveRingId,
       "accTrRingSrvStatus": accTrRingSrvStatus,
       "accSr": accSr,
       "accSrBridge": accSrBridge,
       "accSrBridgeId": accSrBridgeId,
       "accSrVirRingId": accSrVirRingId,
       "accSrHopLimit": accSrHopLimit,
       "accSrSingleRtBcast": accSrSingleRtBcast,
       "accSrNumPorts": accSrNumPorts,
       "accSrRifTimer": accSrRifTimer,
       "accSrSdsInterval": accSrSdsInterval,
       "accSrPortParmTable": accSrPortParmTable,
       "accSrPortParmEntry": accSrPortParmEntry,
       "accSrParmsIndex": accSrParmsIndex,
       "accSrAdminStatus": accSrAdminStatus,
       "accSrOperStatus": accSrOperStatus,
       "accSrPortProtocol": accSrPortProtocol,
       "accSrPortLine": accSrPortLine,
       "accSrPortFrDlci": accSrPortFrDlci,
       "accSrPortXBridgeStatus": accSrPortXBridgeStatus,
       "accSrPortVirRingId": accSrPortVirRingId,
       "accSrPortSrMethod": accSrPortSrMethod,
       "accSrPortStatsTable": accSrPortStatsTable,
       "accSrPortStatsEntry": accSrPortStatsEntry,
       "accStatsIndex": accStatsIndex,
       "accInBcastPkts": accInBcastPkts,
       "accInUcastPkts": accInUcastPkts,
       "accOutBcastPkts": accOutBcastPkts,
       "accOutUcastPkts": accOutUcastPkts,
       "accInSDSPkts": accInSDSPkts,
       "accInAPEPkts": accInAPEPkts,
       "accOutSDSPkts": accOutSDSPkts,
       "accOutAPEPkts": accOutAPEPkts,
       "accInDiscPkts": accInDiscPkts,
       "accOutDelayDiscPkts": accOutDelayDiscPkts,
       "accOutPrioDiscPkts": accOutPrioDiscPkts,
       "accInMcastPkts": accInMcastPkts,
       "accOutMcastPkts": accOutMcastPkts,
       "accSrRouteTable": accSrRouteTable,
       "accSrRouteEntry": accSrRouteEntry,
       "accSrRtDest": accSrRtDest,
       "accSrRtControl": accSrRtControl,
       "accSrRtDesc": accSrRtDesc,
       "accSrRtIfIndex": accSrRtIfIndex,
       "accSrFilterTable": accSrFilterTable,
       "accSrFilterEntry": accSrFilterEntry,
       "accSrFilterDest": accSrFilterDest,
       "accSrFilterSrc": accSrFilterSrc,
       "accSrFilterAction": accSrFilterAction,
       "accSrFpTable": accSrFpTable,
       "accSrFpEntry": accSrFpEntry,
       "accSrFpIndex": accSrFpIndex,
       "accSrFpProt": accSrFpProt,
       "accSrFpPrio": accSrFpPrio,
       "accSrFpDefaults": accSrFpDefaults,
       "accSrFpPriDefault": accSrFpPriDefault,
       "accSrPortFRTable": accSrPortFRTable,
       "accSrPortFREntry": accSrPortFREntry,
       "accSrPortFRport": accSrPortFRport,
       "accSrPortFRdlci": accSrPortFRdlci,
       "accSrPortFRencap": accSrPortFRencap,
       "accSrPortX25Table": accSrPortX25Table,
       "accSrPortX25Entry": accSrPortX25Entry,
       "accSrPortX25port": accSrPortX25port,
       "accSrPortX25addr1": accSrPortX25addr1,
       "accSrPortX25addr2": accSrPortX25addr2,
       "accSrPortX25idleTime": accSrPortX25idleTime,
       "accSrPortX25pktNegot": accSrPortX25pktNegot,
       "accSrPortX25windowNegot": accSrPortX25windowNegot,
       "accSrPortX25FacIndex": accSrPortX25FacIndex,
       "accSrStp": accSrStp,
       "accSrStpBridge": accSrStpBridge,
       "accSrStpPriority": accSrStpPriority,
       "accSrStpId": accSrStpId,
       "accSrStpBrAddr": accSrStpBrAddr,
       "accSrStpMode": accSrStpMode,
       "accSrStpFilterTime": accSrStpFilterTime,
       "accSrStpMcastAddr": accSrStpMcastAddr,
       "accSrStpTopChangeDet": accSrStpTopChangeDet,
       "accSrStpTopChange": accSrStpTopChange,
       "accSrStpTopChangeTimer": accSrStpTopChangeTimer,
       "accSrStpDesRoot": accSrStpDesRoot,
       "accSrStpRootPathCost": accSrStpRootPathCost,
       "accSrStpRootPort": accSrStpRootPort,
       "accSrStpMaxAge": accSrStpMaxAge,
       "accSrStpHelloTime": accSrStpHelloTime,
       "accSrStpForwardDelay": accSrStpForwardDelay,
       "accSrStpUpTime": accSrStpUpTime,
       "accSrStpTopChangeCnts": accSrStpTopChangeCnts,
       "accSrStpPortParms": accSrStpPortParms,
       "accSrStpPortState": accSrStpPortState,
       "accSrStpPortPathCost": accSrStpPortPathCost,
       "accSrStpPortDesRoot": accSrStpPortDesRoot,
       "accSrStpPortDesCost": accSrStpPortDesCost,
       "accSrStpPortDesBridge": accSrStpPortDesBridge,
       "accSrStpPortDesPort": accSrStpPortDesPort,
       "accSrStpPortPriority": accSrStpPortPriority,
       "accSrStpPortInPkts": accSrStpPortInPkts,
       "accSrStpPortOutPkts": accSrStpPortOutPkts,
       "accSrStpPortAdmin": accSrStpPortAdmin,
       "accSrRingTable": accSrRingTable,
       "accSrRingEntry": accSrRingEntry,
       "accSrRingTblRingID": accSrRingTblRingID,
       "accSrRingTblBridgeID": accSrRingTblBridgeID,
       "accSrRingTblPortIndex": accSrRingTblPortIndex,
       "accSrRingTblMetric": accSrRingTblMetric,
       "accSrRingTblAge": accSrRingTblAge,
       "accSrRingTblNbrMacAddr": accSrRingTblNbrMacAddr,
       "accSrFiltIITable": accSrFiltIITable,
       "accSrFiltIIEntry": accSrFiltIIEntry,
       "accSrFiltIIEntDstMacAddr": accSrFiltIIEntDstMacAddr,
       "accSrFiltIIEntSrcMacAddr": accSrFiltIIEntSrcMacAddr,
       "accSrFiltIIEntDisp": accSrFiltIIEntDisp,
       "accSrFiltIIEntPort": accSrFiltIIEntPort,
       "accSrFiltIIEntLogicalOp": accSrFiltIIEntLogicalOp,
       "accSrFiltIIEntProtocol": accSrFiltIIEntProtocol,
       "accSrFiltIIEntDstMacAddrMask": accSrFiltIIEntDstMacAddrMask,
       "accSrFiltIIEntSrcMacAddrMask": accSrFiltIIEntSrcMacAddrMask,
       "accSrFiltIIDiscards": accSrFiltIIDiscards,
       "accSrFiltIIEntries": accSrFiltIIEntries,
       "accSMDS": accSMDS,
       "accSmdsPortTable": accSmdsPortTable,
       "accSmdsPortEntry": accSmdsPortEntry,
       "accSmdsPortIndex": accSmdsPortIndex,
       "accSmdsPortIA": accSmdsPortIA,
       "accSipL3Table": accSipL3Table,
       "accSipL3Entry": accSipL3Entry,
       "accSipL3Index": accSipL3Index,
       "accSipL3RcvIAs": accSipL3RcvIAs,
       "accSipL3RcvGAs": accSipL3RcvGAs,
       "accSipL3UnkIAs": accSipL3UnkIAs,
       "accSipL3UnkGAs": accSipL3UnkGAs,
       "accSipL3SndIAs": accSipL3SndIAs,
       "accSipL3SndGAs": accSipL3SndGAs,
       "accSipL3Errors": accSipL3Errors,
       "accSipL3InvAddrs": accSipL3InvAddrs,
       "accRload": accRload,
       "accRlSourceTable": accRlSourceTable,
       "accRlSourceEntry": accRlSourceEntry,
       "accRlHostAddr": accRlHostAddr,
       "accRlFilename": accRlFilename,
       "accRlPriority": accRlPriority,
       "accNetload": accNetload,
       "accDownload": accDownload,
       "accPromload": accPromload,
       "accCfgLoad": accCfgLoad,
       "accCfgHost": accCfgHost,
       "accCfgFile": accCfgFile,
       "accCfgDisp": accCfgDisp,
       "accTftpStat": accTftpStat,
       "accTftpStatus": accTftpStatus,
       "accTftpLocalFile": accTftpLocalFile,
       "accTftpRemoteFile": accTftpRemoteFile,
       "accTftpOctetsTransferred": accTftpOctetsTransferred,
       "accTftpLastMsg": accTftpLastMsg,
       "accTftpCmd": accTftpCmd,
       "accTftpCmdReq": accTftpCmdReq,
       "accTftpCmdHost": accTftpCmdHost,
       "accTftpCmdRemote": accTftpCmdRemote,
       "accTftpCmdLocal": accTftpCmdLocal,
       "accAt": accAt,
       "accAtNode": accAtNode,
       "accAtNodeAdState": accAtNodeAdState,
       "accAtNodeChecksum": accAtNodeChecksum,
       "accAtNodeAarpExpire": accAtNodeAarpExpire,
       "accAtAarpTable": accAtAarpTable,
       "accAtAarpEntry": accAtAarpEntry,
       "accAtAarpTabPort": accAtAarpTabPort,
       "accAtAarpTabMacAddr": accAtAarpTabMacAddr,
       "accAtAarpTabNetAddr": accAtAarpTabNetAddr,
       "accAtAarpTabStatus": accAtAarpTabStatus,
       "accAtAarpStatsTable": accAtAarpStatsTable,
       "accAtAarpStatsEntry": accAtAarpStatsEntry,
       "accAtAarpStatsInRequests": accAtAarpStatsInRequests,
       "accAtAarpStatsInResponses": accAtAarpStatsInResponses,
       "accAtAarpStatsInProbes": accAtAarpStatsInProbes,
       "accAtAarpStatsOutRequests": accAtAarpStatsOutRequests,
       "accAtAarpStatsOutResponses": accAtAarpStatsOutResponses,
       "accAtAarpStatsOutProbes": accAtAarpStatsOutProbes,
       "accAtAarpStatsNoReplys": accAtAarpStatsNoReplys,
       "accAtAarpStatsExpires": accAtAarpStatsExpires,
       "accAtAarpStatsDiscards": accAtAarpStatsDiscards,
       "accAtAarpStatsInErrors": accAtAarpStatsInErrors,
       "accAtAarpStatsOutErrors": accAtAarpStatsOutErrors,
       "accAtAdbStats": accAtAdbStats,
       "accAtAdbStatsCacheds": accAtAdbStatsCacheds,
       "accAtAdbStatsRotates": accAtAdbStatsRotates,
       "accAtAdbStatsNoEntries": accAtAdbStatsNoEntries,
       "accAtAdbStatsAdds": accAtAdbStatsAdds,
       "accAtAdbStatsUpdates": accAtAdbStatsUpdates,
       "accAtAdbStatsDeletes": accAtAdbStatsDeletes,
       "accAtAdbStatsTrims": accAtAdbStatsTrims,
       "accAtAdbStatsDiscards": accAtAdbStatsDiscards,
       "accAtDdpStats": accAtDdpStats,
       "accAtDdpStatsNoOutRoutes": accAtDdpStatsNoOutRoutes,
       "accAtDdpStatsInErrors": accAtDdpStatsInErrors,
       "accAtDdpStatsOutErrors": accAtDdpStatsOutErrors,
       "accAtNetTable": accAtNetTable,
       "accAtNetEntry": accAtNetEntry,
       "accAtNetTabProtocol": accAtNetTabProtocol,
       "accAtNetTabRtmpIncr": accAtNetTabRtmpIncr,
       "accAtNetTabRtmpSend": accAtNetTabRtmpSend,
       "accAtNetTabX25Addr1": accAtNetTabX25Addr1,
       "accAtNetTabX25Addr2": accAtNetTabX25Addr2,
       "accAtNetTabX25Idle": accAtNetTabX25Idle,
       "accAtNetTabX25PktSize": accAtNetTabX25PktSize,
       "accAtNetTabX25WinSize": accAtNetTabX25WinSize,
       "accAtNetTabX25FacIndex": accAtNetTabX25FacIndex,
       "accAtPortTable": accAtPortTable,
       "accAtPortEntry": accAtPortEntry,
       "accAtPortTabIndex": accAtPortTabIndex,
       "accAtPortTabNetAddr": accAtPortTabNetAddr,
       "accAtPortTabState": accAtPortTabState,
       "accAtPortTabDescr": accAtPortTabDescr,
       "accAtPortTabErrCode": accAtPortTabErrCode,
       "accAtPortTabErrTime": accAtPortTabErrTime,
       "accAtPortTabErrAddr": accAtPortTabErrAddr,
       "accAtPortTabErrDescr": accAtPortTabErrDescr,
       "accAtPortTabErrCount": accAtPortTabErrCount,
       "accAtPortStatsTable": accAtPortStatsTable,
       "accAtPortStatsEntry": accAtPortStatsEntry,
       "accAtPortStatsInTotals": accAtPortStatsInTotals,
       "accAtPortStatsInShorts": accAtPortStatsInShorts,
       "accAtPortStatsNotForMes": accAtPortStatsNotForMes,
       "accAtPortStatsTooShorts": accAtPortStatsTooShorts,
       "accAtPortStatsTooLongs": accAtPortStatsTooLongs,
       "accAtPortStatsChksums": accAtPortStatsChksums,
       "accAtPortStatsNotMyNets": accAtPortStatsNotMyNets,
       "accAtPortStatsInFwdReqs": accAtPortStatsInFwdReqs,
       "accAtPortStatsFwdBcasts": accAtPortStatsFwdBcasts,
       "accAtPortStatsNoFwdRoutes": accAtPortStatsNoFwdRoutes,
       "accAtPortStatsHopCounts": accAtPortStatsHopCounts,
       "accAtPortStatsReflects": accAtPortStatsReflects,
       "accAtPortStatsOutTotals": accAtPortStatsOutTotals,
       "accAtPortStatsOutShorts": accAtPortStatsOutShorts,
       "accAtPortStatsOutFwdReqs": accAtPortStatsOutFwdReqs,
       "accAtPortStatsInErrors": accAtPortStatsInErrors,
       "accAtPortStatsOutErrors": accAtPortStatsOutErrors,
       "accAtRtmpStats": accAtRtmpStats,
       "accAtRtmpStatsInRequests": accAtRtmpStatsInRequests,
       "accAtRtmpStatsInDataReqs": accAtRtmpStatsInDataReqs,
       "accAtRtmpStatsInResponses": accAtRtmpStatsInResponses,
       "accAtRtmpStatsInDataResps": accAtRtmpStatsInDataResps,
       "accAtRtmpStatsOutRequests": accAtRtmpStatsOutRequests,
       "accAtRtmpStatsOutDataReqs": accAtRtmpStatsOutDataReqs,
       "accAtRtmpStatsOutResponses": accAtRtmpStatsOutResponses,
       "accAtRtmpStatsOutDataResps": accAtRtmpStatsOutDataResps,
       "accAtRtmpStatsNetConflicts": accAtRtmpStatsNetConflicts,
       "accAtRtmpStatsInErrors": accAtRtmpStatsInErrors,
       "accAtRtmpStatsOutErrors": accAtRtmpStatsOutErrors,
       "accAtRdbStats": accAtRdbStats,
       "accAtRdbStatsCacheds": accAtRdbStatsCacheds,
       "accAtRdbStatsSearchs": accAtRdbStatsSearchs,
       "accAtRdbStatsNoRoutes": accAtRdbStatsNoRoutes,
       "accAtRdbStatsAdds": accAtRdbStatsAdds,
       "accAtRdbStatsUpdates": accAtRdbStatsUpdates,
       "accAtRdbStatsDeletes": accAtRdbStatsDeletes,
       "accAtNbpStats": accAtNbpStats,
       "accAtNbpStatsInBrReqs": accAtNbpStatsInBrReqs,
       "accAtNbpStatsInLkUpReqs": accAtNbpStatsInLkUpReqs,
       "accAtNbpStatsInLkUpResps": accAtNbpStatsInLkUpResps,
       "accAtNbpStatsInFwdReqs": accAtNbpStatsInFwdReqs,
       "accAtNbpStatsOutBrReqs": accAtNbpStatsOutBrReqs,
       "accAtNbpStatsOutLkUpReqs": accAtNbpStatsOutLkUpReqs,
       "accAtNbpStatsOutLkUpResps": accAtNbpStatsOutLkUpResps,
       "accAtNbpStatsOutFwdReqs": accAtNbpStatsOutFwdReqs,
       "accAtNbpStatsNoZones": accAtNbpStatsNoZones,
       "accAtNbpStatsInErrors": accAtNbpStatsInErrors,
       "accAtNbpStatsOutErrors": accAtNbpStatsOutErrors,
       "accAtZipStats": accAtZipStats,
       "accAtZipStatsInQuerys": accAtZipStatsInQuerys,
       "accAtZipStatsInReplies": accAtZipStatsInReplies,
       "accAtZipStatsInExtReplies": accAtZipStatsInExtReplies,
       "accAtZipStatsInInfoReqs": accAtZipStatsInInfoReqs,
       "accAtZipStatsInInfoReps": accAtZipStatsInInfoReps,
       "accAtZipStatsInTakeDowns": accAtZipStatsInTakeDowns,
       "accAtZipStatsInBringUps": accAtZipStatsInBringUps,
       "accAtZipStatsInNotifies": accAtZipStatsInNotifies,
       "accAtZipStatsInGetZLReqs": accAtZipStatsInGetZLReqs,
       "accAtZipStatsInGetLZReqs": accAtZipStatsInGetLZReqs,
       "accAtZipStatsInGetMZReqs": accAtZipStatsInGetMZReqs,
       "accAtZipStatsOutQueries": accAtZipStatsOutQueries,
       "accAtZipStatsOutReplies": accAtZipStatsOutReplies,
       "accAtZipStatsOutExtReplies": accAtZipStatsOutExtReplies,
       "accAtZipStatsOutInfoReqs": accAtZipStatsOutInfoReqs,
       "accAtZipStatsOutInfoReps": accAtZipStatsOutInfoReps,
       "accAtZipStatsOutGetZLReps": accAtZipStatsOutGetZLReps,
       "accAtZipStatsOutGetLZReps": accAtZipStatsOutGetLZReps,
       "accAtZipStatsOutGetMZReps": accAtZipStatsOutGetMZReps,
       "accAtZipStatsZoneConflicts": accAtZipStatsZoneConflicts,
       "accAtZipStatsInErrors": accAtZipStatsInErrors,
       "accAtZipStatsOutErrors": accAtZipStatsOutErrors,
       "accAtAepStats": accAtAepStats,
       "accAtAepStatsInErrors": accAtAepStatsInErrors,
       "accAtAepStatsOutErrors": accAtAepStatsOutErrors,
       "accAtZoneListTable": accAtZoneListTable,
       "accAtZoneListEntry": accAtZoneListEntry,
       "accAtZoneListPort": accAtZoneListPort,
       "accAtZoneListStatus": accAtZoneListStatus,
       "accAtZoneListName": accAtZoneListName,
       "accAtZoneBynameTable": accAtZoneBynameTable,
       "accAtZoneBynameEntry": accAtZoneBynameEntry,
       "accAtZoneBynameNetMin": accAtZoneBynameNetMin,
       "accAtZoneBynameNetMax": accAtZoneBynameNetMax,
       "accAtZoneBynameName": accAtZoneBynameName,
       "accAtZoneBynetTable": accAtZoneBynetTable,
       "accAtZoneBynetEntry": accAtZoneBynetEntry,
       "accAtZoneBynetNetMin": accAtZoneBynetNetMin,
       "accAtZoneBynetNetMax": accAtZoneBynetNetMax,
       "accAtZoneBynetName": accAtZoneBynetName,
       "accAtForwardFilterTable": accAtForwardFilterTable,
       "accAtForwardFilterEntry": accAtForwardFilterEntry,
       "accAtForwardFilterToMin": accAtForwardFilterToMin,
       "accAtForwardFilterToMax": accAtForwardFilterToMax,
       "accAtForwardFilterFromMin": accAtForwardFilterFromMin,
       "accAtForwardFilterFromMax": accAtForwardFilterFromMax,
       "accAtForwardFilterSocketMin": accAtForwardFilterSocketMin,
       "accAtForwardFilterSocketMax": accAtForwardFilterSocketMax,
       "accAtForwardFilterType": accAtForwardFilterType,
       "accAtForwardFilterDisposition": accAtForwardFilterDisposition,
       "accAtForwardFilterStatus": accAtForwardFilterStatus,
       "accAtRouteFilterTable": accAtRouteFilterTable,
       "accAtRouteFilterEntry": accAtRouteFilterEntry,
       "accAtRouteFilterRouterMin": accAtRouteFilterRouterMin,
       "accAtRouteFilterRouterMax": accAtRouteFilterRouterMax,
       "accAtRouteFilterRangeMin": accAtRouteFilterRangeMin,
       "accAtRouteFilterRangeMax": accAtRouteFilterRangeMax,
       "accAtRouteFilterDisposition": accAtRouteFilterDisposition,
       "accAtRouteFilterStatus": accAtRouteFilterStatus,
       "accBootp": accBootp,
       "accBootServerOld": accBootServerOld,
       "accBootpServerOld": accBootpServerOld,
       "accBootMode": accBootMode,
       "accBootState": accBootState,
       "accBootyiaddr": accBootyiaddr,
       "accBootsiaddr": accBootsiaddr,
       "accBootsname": accBootsname,
       "accBootgiaddr": accBootgiaddr,
       "accBootfile": accBootfile,
       "accBootInterface": accBootInterface,
       "accBootSentRequests": accBootSentRequests,
       "accBootReceivedReplies": accBootReceivedReplies,
       "accBootDiscardedReplies": accBootDiscardedReplies,
       "accBootServerTable": accBootServerTable,
       "accBootServerEntry": accBootServerEntry,
       "accBootServerIPAddr": accBootServerIPAddr,
       "pysmiFakeCol3": pysmiFakeCol3,
       "accBootg1iaddr": accBootg1iaddr,
       "accBootg2iaddr": accBootg2iaddr,
       "accBootg3iaddr": accBootg3iaddr,
       "accPing": accPing,
       "accPingDest": accPingDest,
       "accPingReqCnt": accPingReqCnt,
       "accPingDataMin": accPingDataMin,
       "accPingDataMax": accPingDataMax,
       "accPingTimeMin": accPingTimeMin,
       "accPingTimeMax": accPingTimeMax,
       "accPingSndPkts": accPingSndPkts,
       "accPingSndBytes": accPingSndBytes,
       "accPingRcvPkts": accPingRcvPkts,
       "accPingRcvBytes": accPingRcvBytes,
       "accPingRcvOKs": accPingRcvOKs,
       "accPingRcvBads": accPingRcvBads,
       "accPingDelayMin": accPingDelayMin,
       "accPingDelayMax": accPingDelayMax,
       "accPingDelayAvg": accPingDelayAvg,
       "accDial": accDial,
       "accDialBackupTable": accDialBackupTable,
       "accDialBackupEntry": accDialBackupEntry,
       "accDialBackupPort": accDialBackupPort,
       "accDialBackupPrimary": accDialBackupPrimary,
       "accDialBackupControl": accDialBackupControl,
       "accDialBackupRetry": accDialBackupRetry,
       "accDialBackupDamp": accDialBackupDamp,
       "accDialBackupCallCongestion": accDialBackupCallCongestion,
       "accDialBackupClearCongestion": accDialBackupClearCongestion,
       "accDialBackupCallError": accDialBackupCallError,
       "accDialBackupCallAddress": accDialBackupCallAddress,
       "accDialBackupStatus": accDialBackupStatus,
       "accDialBackupState": accDialBackupState,
       "accDialPortTable": accDialPortTable,
       "accDialPortEntry": accDialPortEntry,
       "accDialPortIndex": accDialPortIndex,
       "accDialPortContents": accDialPortContents,
       "accDialPortStationType": accDialPortStationType,
       "accDialPortAdminState": accDialPortAdminState,
       "accDialPortCallState": accDialPortCallState,
       "accDialPortRetryInterval": accDialPortRetryInterval,
       "accDialPortRetryCount": accDialPortRetryCount,
       "accDialPortClearingInterv": accDialPortClearingInterv,
       "accDialPortMessageLevel": accDialPortMessageLevel,
       "accDialPortPhysicalPort": accDialPortPhysicalPort,
       "accDialPortCallAddress": accDialPortCallAddress,
       "accDialPortPhysicalPortStr": accDialPortPhysicalPortStr,
       "accDialPortCallAddressStr": accDialPortCallAddressStr,
       "accDialPortPassword": accDialPortPassword,
       "accDialPortName": accDialPortName,
       "accDialPortStatTable": accDialPortStatTable,
       "accDialPortStatEntry": accDialPortStatEntry,
       "accDialPortStatIndex": accDialPortStatIndex,
       "accDialPortStatActPhysPort": accDialPortStatActPhysPort,
       "accDialPortStatState": accDialPortStatState,
       "accDialPortStatTrigFwdr": accDialPortStatTrigFwdr,
       "accDialPortStatElapsedTime": accDialPortStatElapsedTime,
       "accDialPortStatTrigSrcAddr": accDialPortStatTrigSrcAddr,
       "accDialPortStatTrigCallAddr": accDialPortStatTrigCallAddr,
       "accDialPortStatSuccessOut": accDialPortStatSuccessOut,
       "accDialPortStatUnsuccessOut": accDialPortStatUnsuccessOut,
       "accDialPortStatSuccessIn": accDialPortStatSuccessIn,
       "accDialPortStatUnsuccessIn": accDialPortStatUnsuccessIn,
       "accDialOrigAtTable": accDialOrigAtTable,
       "accDialOrigAtEntry": accDialOrigAtEntry,
       "accDialOrigAtStatus": accDialOrigAtStatus,
       "accDialOrigAtDestStart": accDialOrigAtDestStart,
       "accDialOrigAtDestEnd": accDialOrigAtDestEnd,
       "accDialOrigAtSourceStart": accDialOrigAtSourceStart,
       "accDialOrigAtSourceEnd": accDialOrigAtSourceEnd,
       "accDialOrigAtTraffic": accDialOrigAtTraffic,
       "accDialOrigAtAction": accDialOrigAtAction,
       "accDialOrigDnTable": accDialOrigDnTable,
       "accDialOrigDnEntry": accDialOrigDnEntry,
       "accDialOrigDnStatus": accDialOrigDnStatus,
       "accDialOrigDnDestAddr": accDialOrigDnDestAddr,
       "accDialOrigDnSourceAddr": accDialOrigDnSourceAddr,
       "accDialOrigDnAction": accDialOrigDnAction,
       "accDialOrigBrTable": accDialOrigBrTable,
       "accDialOrigBrEntry": accDialOrigBrEntry,
       "accDialOrigBrStatus": accDialOrigBrStatus,
       "accDialOrigBrDestMacAddr": accDialOrigBrDestMacAddr,
       "accDialOrigBrSourceMacAddr": accDialOrigBrSourceMacAddr,
       "accDialOrigBrAction": accDialOrigBrAction,
       "accDialOrigIdpTable": accDialOrigIdpTable,
       "accDialOrigIdpEntry": accDialOrigIdpEntry,
       "accDialOrigIdpStatus": accDialOrigIdpStatus,
       "accDialOrigIdpDestNet": accDialOrigIdpDestNet,
       "accDialOrigIdpSourceNet": accDialOrigIdpSourceNet,
       "accDialOrigIdpAction": accDialOrigIdpAction,
       "accDialOrigIpTable": accDialOrigIpTable,
       "accDialOrigIpEntry": accDialOrigIpEntry,
       "accDialOrigIpStatus": accDialOrigIpStatus,
       "accDialOrigIpDestAddr": accDialOrigIpDestAddr,
       "accDialOrigIpDestMask": accDialOrigIpDestMask,
       "accDialOrigIpSourceAddr": accDialOrigIpSourceAddr,
       "accDialOrigIpSourceMask": accDialOrigIpSourceMask,
       "accDialOrigIpParm": accDialOrigIpParm,
       "accDialOrigIpAction": accDialOrigIpAction,
       "accDialOrigIpxTable": accDialOrigIpxTable,
       "accDialOrigIpxEntry": accDialOrigIpxEntry,
       "accDialOrigIpxStatus": accDialOrigIpxStatus,
       "accDialOrigIpxDestNet": accDialOrigIpxDestNet,
       "accDialOrigIpxSourceNet": accDialOrigIpxSourceNet,
       "accDialOrigIpxAction": accDialOrigIpxAction,
       "accDialOrigSrTable": accDialOrigSrTable,
       "accDialOrigSrEntry": accDialOrigSrEntry,
       "accDialOrigSrStatus": accDialOrigSrStatus,
       "accDialOrigSrDestMacAddr": accDialOrigSrDestMacAddr,
       "accDialOrigSrSourceMacAddr": accDialOrigSrSourceMacAddr,
       "accDialOrigSrAction": accDialOrigSrAction,
       "accPpp": accPpp,
       "accPppLinkTable": accPppLinkTable,
       "accPppLinkEntry": accPppLinkEntry,
       "accPppLinkIndex": accPppLinkIndex,
       "accPppLinkPhysicalIndex": accPppLinkPhysicalIndex,
       "accPppLinkBadAddresses": accPppLinkBadAddresses,
       "accPppLinkBadControls": accPppLinkBadControls,
       "accPppLinkPacketTooLongs": accPppLinkPacketTooLongs,
       "accPppLinkBadFCSs": accPppLinkBadFCSs,
       "accPppLinkLocalMRU": accPppLinkLocalMRU,
       "accPppLinkRemoteMRU": accPppLinkRemoteMRU,
       "accPppLinkLocalToPeerACCMap": accPppLinkLocalToPeerACCMap,
       "accPppLinkPeerToLocalACCMap": accPppLinkPeerToLocalACCMap,
       "accPppLinkLocalToRemotePC": accPppLinkLocalToRemotePC,
       "accPppLinkRemoteToLocalPC": accPppLinkRemoteToLocalPC,
       "accPppLinkLocalToRemoteAC": accPppLinkLocalToRemoteAC,
       "accPppLinkRemoteToLocalAC": accPppLinkRemoteToLocalAC,
       "accPppLinkTransmit32BitFcs": accPppLinkTransmit32BitFcs,
       "accPppLinkReceive32BitFcs": accPppLinkReceive32BitFcs,
       "accPppLinkOperStatus": accPppLinkOperStatus,
       "accPppLinkPacketTooShorts": accPppLinkPacketTooShorts,
       "accPppLinkUnknownProtocols": accPppLinkUnknownProtocols,
       "accPppLinkPacketInDiscards": accPppLinkPacketInDiscards,
       "accPppLinkPacketOutDiscards": accPppLinkPacketOutDiscards,
       "accPppLcpConfigTable": accPppLcpConfigTable,
       "accPppLcpConfigEntry": accPppLcpConfigEntry,
       "accPppLcpConfigIndex": accPppLcpConfigIndex,
       "accPppLcpConfigInitialMRU": accPppLcpConfigInitialMRU,
       "accPppLcpConfigReceiveACCMap": accPppLcpConfigReceiveACCMap,
       "accPppLinkConfigXmitACCMap": accPppLinkConfigXmitACCMap,
       "accPppLcpConfigMagicNumber": accPppLcpConfigMagicNumber,
       "accPppLcpConfig32BitFCS": accPppLcpConfig32BitFCS,
       "accPppLcpRestartTimer": accPppLcpRestartTimer,
       "accPppLcpMaxTerminate": accPppLcpMaxTerminate,
       "accPppLcpMaxConfigure": accPppLcpMaxConfigure,
       "accPppLcpMaxFailure": accPppLcpMaxFailure,
       "accPppLcpMonInterval": accPppLcpMonInterval,
       "accPppLcpMonEvents": accPppLcpMonEvents,
       "accPppLcpMonThreshold": accPppLcpMonThreshold,
       "accPppLcpAdminStatus": accPppLcpAdminStatus,
       "accPppLqrTable": accPppLqrTable,
       "accPppLqrEntry": accPppLqrEntry,
       "accPppLqrIndex": accPppLqrIndex,
       "accPppLqrQuality": accPppLqrQuality,
       "accPppLqrInGoodOctets": accPppLqrInGoodOctets,
       "accPppLqrLocalPeriod": accPppLqrLocalPeriod,
       "accPppLqrRemotePeriod": accPppLqrRemotePeriod,
       "accPppLqrOutLQRs": accPppLqrOutLQRs,
       "accPppLqrInLQRs": accPppLqrInLQRs,
       "accPppLqrConfigTable": accPppLqrConfigTable,
       "accPppLqrConfigEntry": accPppLqrConfigEntry,
       "accPppLqrConfigIndex": accPppLqrConfigIndex,
       "accPppLqrConfigPeriod": accPppLqrConfigPeriod,
       "accPppLqrConfigStatus": accPppLqrConfigStatus,
       "accPppIpcpTable": accPppIpcpTable,
       "accPppIpcpEntry": accPppIpcpEntry,
       "accPppIpcpIndex": accPppIpcpIndex,
       "accPppIpcpLocalToRemoteCompressionProtocol": accPppIpcpLocalToRemoteCompressionProtocol,
       "accPppIpcpRemoteToLocalCompressionProtocol": accPppIpcpRemoteToLocalCompressionProtocol,
       "accPppIpcpRemoteMaxSlotId": accPppIpcpRemoteMaxSlotId,
       "accPppIpcpLocalMaxSlotId": accPppIpcpLocalMaxSlotId,
       "accPppIpOperStatus": accPppIpOperStatus,
       "accPppIpcpConfigTable": accPppIpcpConfigTable,
       "accPppIpcpConfigEntry": accPppIpcpConfigEntry,
       "accPppIpcpConfigIndex": accPppIpcpConfigIndex,
       "accPppIpcpConfigCompression": accPppIpcpConfigCompression,
       "accPppIpcpConfigStatus": accPppIpcpConfigStatus,
       "accPppBncpTable": accPppBncpTable,
       "accPppBncpEntry": accPppBncpEntry,
       "accPppBncpIndex": accPppBncpIndex,
       "accPppBncpLocalToRemoteTinygramCompression": accPppBncpLocalToRemoteTinygramCompression,
       "accPppBncpRemoteToLocalTinygramCompression": accPppBncpRemoteToLocalTinygramCompression,
       "accPppBncpLocalToRemoteLanId": accPppBncpLocalToRemoteLanId,
       "accPppBncpRemoteToLocalLanId": accPppBncpRemoteToLocalLanId,
       "accPppBncpConfigTable": accPppBncpConfigTable,
       "accPppBncpConfigEntry": accPppBncpConfigEntry,
       "accPppBncpConfigIndex": accPppBncpConfigIndex,
       "accPppBncpConfigTinygram": accPppBncpConfigTinygram,
       "accPppBncpConfigRingId": accPppBncpConfigRingId,
       "accPppBncpConfigLineId": accPppBncpConfigLineId,
       "accPppBncpConfigLanId": accPppBncpConfigLanId,
       "accPppBncpConfigAdminStatus": accPppBncpConfigAdminStatus,
       "accPppXnsTable": accPppXnsTable,
       "accPppXnsEntry": accPppXnsEntry,
       "accPppXnsIndex": accPppXnsIndex,
       "accPppXnsOperStatus": accPppXnsOperStatus,
       "accPppXnsConfigTable": accPppXnsConfigTable,
       "accPppXnsConfigEntry": accPppXnsConfigEntry,
       "accPppXnsConfigIndex": accPppXnsConfigIndex,
       "accPppXnsConfigAdminStatus": accPppXnsConfigAdminStatus,
       "accPppIpxTable": accPppIpxTable,
       "accPppIpxEntry": accPppIpxEntry,
       "accPppIpxIndex": accPppIpxIndex,
       "accPppIpxOperStatus": accPppIpxOperStatus,
       "accPppIpxConfigTable": accPppIpxConfigTable,
       "accPppIpxConfigEntry": accPppIpxConfigEntry,
       "accPppIpxConfigIndex": accPppIpxConfigIndex,
       "accPppIpxConfigAdminStatus": accPppIpxConfigAdminStatus,
       "accPppAppleTable": accPppAppleTable,
       "accPppAppleEntry": accPppAppleEntry,
       "accPppAppleIndex": accPppAppleIndex,
       "accPppAppleOperStatus": accPppAppleOperStatus,
       "accPppAppleConfigTable": accPppAppleConfigTable,
       "accPppAppleConfigEntry": accPppAppleConfigEntry,
       "accPppAppleConfigIndex": accPppAppleConfigIndex,
       "accPppAppleConfigAdminStatus": accPppAppleConfigAdminStatus,
       "accPppDecTable": accPppDecTable,
       "accPppDecEntry": accPppDecEntry,
       "accPppDecIndex": accPppDecIndex,
       "accPppDecOperStatus": accPppDecOperStatus,
       "accPppDecConfigTable": accPppDecConfigTable,
       "accPppDecConfigEntry": accPppDecConfigEntry,
       "accPppDecConfigIndex": accPppDecConfigIndex,
       "accPppDecConfigAdminStatus": accPppDecConfigAdminStatus,
       "accPppProtocolTable": accPppProtocolTable,
       "accPppProtocolEntry": accPppProtocolEntry,
       "accPppProtocolIndex": accPppProtocolIndex,
       "accPppProtocolProtocol": accPppProtocolProtocol,
       "accPppProtocolAdminStatus": accPppProtocolAdminStatus,
       "accPppProtocolOperStatus": accPppProtocolOperStatus,
       "accPppMsg": accPppMsg,
       "accPppMsgLevel": accPppMsgLevel,
       "accFlash": accFlash,
       "accFlashTable": accFlashTable,
       "accFlashEntry": accFlashEntry,
       "accFlashIndex": accFlashIndex,
       "accFlashFiDisp": accFlashFiDisp,
       "accFlashCksum": accFlashCksum,
       "accFlashLength": accFlashLength,
       "accXBr": accXBr,
       "accXBridge": accXBridge,
       "accXBridgeStatus": accXBridgeStatus,
       "accXBridgeRingId": accXBridgeRingId,
       "accExtProtImp": accExtProtImp,
       "accExtProtImpTable": accExtProtImpTable,
       "accExtProtImpEntry": accExtProtImpEntry,
       "accExtProtImpProtocol": accExtProtImpProtocol,
       "accExtProtImpAllowed": accExtProtImpAllowed,
       "accIsdn": accIsdn,
       "accIsdnDsl": accIsdnDsl,
       "accIsdnDslIndex": accIsdnDslIndex,
       "accIsdnSubTable": accIsdnSubTable,
       "accIsdnSubEntry": accIsdnSubEntry,
       "accIsdnSubSwitchType": accIsdnSubSwitchType,
       "accIsdnSubChannelMode": accIsdnSubChannelMode,
       "accIsdnSubAdminStatus": accIsdnSubAdminStatus,
       "accIsdnSubDiagLevel": accIsdnSubDiagLevel,
       "accIsdnSubManualTei": accIsdnSubManualTei,
       "accIsdnStatTable": accIsdnStatTable,
       "accIsdnStatEntry": accIsdnStatEntry,
       "accIsdnStatHdlcInPackets": accIsdnStatHdlcInPackets,
       "accIsdnStatHdlcInOctets": accIsdnStatHdlcInOctets,
       "accIsdnStatHdlcInErrors": accIsdnStatHdlcInErrors,
       "accIsdnStatHdlcInDiscs": accIsdnStatHdlcInDiscs,
       "accIsdnStatHdlcOutPackets": accIsdnStatHdlcOutPackets,
       "accIsdnStatHdlcOutOctets": accIsdnStatHdlcOutOctets,
       "accIsdnStatHdlcOutErrors": accIsdnStatHdlcOutErrors,
       "accIsdnStatHdlcOutDiscs": accIsdnStatHdlcOutDiscs,
       "accIsdnStatLapdUnsolicResps": accIsdnStatLapdUnsolicResps,
       "accIsdnStatLapdPeerSabmes": accIsdnStatLapdPeerSabmes,
       "accIsdnStatLapdN200Errors": accIsdnStatLapdN200Errors,
       "accIsdnStatLapdNrSeqErrors": accIsdnStatLapdNrSeqErrors,
       "accIsdnStatLapdRecvdFrmrs": accIsdnStatLapdRecvdFrmrs,
       "accIsdnStatLapdCntlErrors": accIsdnStatLapdCntlErrors,
       "accIsdnStatLapdInfoErrors": accIsdnStatLapdInfoErrors,
       "accIsdnStatLapdWrongSizes": accIsdnStatLapdWrongSizes,
       "accIsdnStatLapdN201Errors": accIsdnStatLapdN201Errors,
       "accIsdnStatCallsOriginateds": accIsdnStatCallsOriginateds,
       "accIsdnStatCallsOfferreds": accIsdnStatCallsOfferreds,
       "accIsdnStatCallsAnswereds": accIsdnStatCallsAnswereds,
       "accIsdnStatCallsAccepteds": accIsdnStatCallsAccepteds,
       "accIsdnStatCallsCompleteds": accIsdnStatCallsCompleteds,
       "accIsdnStatCallsCleareds": accIsdnStatCallsCleareds,
       "accIsdnStatDslOperStatus": accIsdnStatDslOperStatus,
       "accIsdnStatLastCauses": accIsdnStatLastCauses,
       "accIsdnCallTable": accIsdnCallTable,
       "accIsdnCallEntry": accIsdnCallEntry,
       "accIsdnCallIdentifier": accIsdnCallIdentifier,
       "accIsdnCallReference": accIsdnCallReference,
       "accIsdnCallChannelId": accIsdnCallChannelId,
       "accIsdnCallIfIndex": accIsdnCallIfIndex,
       "accIsdnCallInfoRate": accIsdnCallInfoRate,
       "accIsdnCallState": accIsdnCallState,
       "accIsdnCallCause": accIsdnCallCause,
       "accIsdnCallOrigin": accIsdnCallOrigin,
       "accIsdnCallAddress": accIsdnCallAddress,
       "accIsdnCallDslIndex": accIsdnCallDslIndex,
       "accIsdnTest": accIsdnTest,
       "accIsdnTestIfIndex": accIsdnTestIfIndex,
       "accIsdnTestAddress": accIsdnTestAddress,
       "accIsdnTestCommand": accIsdnTestCommand,
       "accIsdnTestProceed": accIsdnTestProceed,
       "accIsdnTestRegName": accIsdnTestRegName,
       "accIsdnTestRegValue": accIsdnTestRegValue,
       "accIsdnxSubTable": accIsdnxSubTable,
       "accIsdnxSubEntry": accIsdnxSubEntry,
       "accIsdnxSubDslIndex": accIsdnxSubDslIndex,
       "accIsdnxSubSwitchType": accIsdnxSubSwitchType,
       "accIsdnxSubChanConfig": accIsdnxSubChanConfig,
       "accIsdnxSubAdminStatus": accIsdnxSubAdminStatus,
       "accIsdnxSubDiagLevel": accIsdnxSubDiagLevel,
       "accIsdnxSubManualTei": accIsdnxSubManualTei,
       "accIsdnxSubOperStatus": accIsdnxSubOperStatus,
       "accIsdnxSubNumNfas": accIsdnxSubNumNfas,
       "accIsdnxSubLastCause": accIsdnxSubLastCause,
       "accIsdnxStatTable": accIsdnxStatTable,
       "accIsdnxStatEntry": accIsdnxStatEntry,
       "accIsdnxStatDslIndex": accIsdnxStatDslIndex,
       "accIsdnxStatHdlcInPackets": accIsdnxStatHdlcInPackets,
       "accIsdnxStatHdlcInOctets": accIsdnxStatHdlcInOctets,
       "accIsdnxStatHdlcInErrors": accIsdnxStatHdlcInErrors,
       "accIsdnxStatHdlcInDiscards": accIsdnxStatHdlcInDiscards,
       "accIsdnxStatHdlcOutPackets": accIsdnxStatHdlcOutPackets,
       "accIsdnxStatHdlcOutOctets": accIsdnxStatHdlcOutOctets,
       "accIsdnxStatHdlcOutErrors": accIsdnxStatHdlcOutErrors,
       "accIsdnxStatHdlcOutDiscards": accIsdnxStatHdlcOutDiscards,
       "accIsdnxStatLapdUnsolicResps": accIsdnxStatLapdUnsolicResps,
       "accIsdnxStatLapdPeerSabmes": accIsdnxStatLapdPeerSabmes,
       "accIsdnxStatLapdN200Errors": accIsdnxStatLapdN200Errors,
       "accIsdnxStatLapdNrSeqErrors": accIsdnxStatLapdNrSeqErrors,
       "accIsdnxStatLapdRecvdFrmrs": accIsdnxStatLapdRecvdFrmrs,
       "accIsdnxStatLapdCntlErrors": accIsdnxStatLapdCntlErrors,
       "accIsdnxStatLapdInfoErrors": accIsdnxStatLapdInfoErrors,
       "accIsdnxStatLapdWrongSizes": accIsdnxStatLapdWrongSizes,
       "accIsdnxStatLapdN201Errors": accIsdnxStatLapdN201Errors,
       "accIsdnxStatCallOriginateds": accIsdnxStatCallOriginateds,
       "accIsdnxStatCallOfferreds": accIsdnxStatCallOfferreds,
       "accIsdnxStatCallRouteds": accIsdnxStatCallRouteds,
       "accIsdnxStatCallAccepteds": accIsdnxStatCallAccepteds,
       "accIsdnxStatCallCompleteds": accIsdnxStatCallCompleteds,
       "accIsdnxStatCallCleareds": accIsdnxStatCallCleareds,
       "accIsdnxCallTable": accIsdnxCallTable,
       "accIsdnxCallEntry": accIsdnxCallEntry,
       "accIsdnxCallDslIndex": accIsdnxCallDslIndex,
       "accIsdnxCallReference": accIsdnxCallReference,
       "accIsdnxCallOrigin": accIsdnxCallOrigin,
       "accIsdnxCallCircuitIndex": accIsdnxCallCircuitIndex,
       "accIsdnxCallInfoRate": accIsdnxCallInfoRate,
       "accIsdnxCallState": accIsdnxCallState,
       "accIsdnxCallCause": accIsdnxCallCause,
       "accIsdnxCallAddress": accIsdnxCallAddress,
       "accIsdnxCallInfoType": accIsdnxCallInfoType,
       "accIsdnxCallSlotMap": accIsdnxCallSlotMap,
       "accIsdnSpidTable": accIsdnSpidTable,
       "accIsdnSpidEntry": accIsdnSpidEntry,
       "accIsdnSpidIndex": accIsdnSpidIndex,
       "accIsdnSpidValue": accIsdnSpidValue,
       "accV25": accV25,
       "accV25StatTable": accV25StatTable,
       "accV25StatEntry": accV25StatEntry,
       "accV25IntIndex": accV25IntIndex,
       "accV25CurState": accV25CurState,
       "accV25DTRSignal": accV25DTRSignal,
       "accV25DSRSignal": accV25DSRSignal,
       "accV25CTSSignal": accV25CTSSignal,
       "accV25CallAttempts": accV25CallAttempts,
       "accV25CallSuccess": accV25CallSuccess,
       "accEnetHub": accEnetHub,
       "accEnetHubStatTable": accEnetHubStatTable,
       "accEnetHubStatEntry": accEnetHubStatEntry,
       "accEnetPortIndex": accEnetPortIndex,
       "accEnetHubIndex": accEnetHubIndex,
       "accEnetHubAdStatus": accEnetHubAdStatus,
       "accEnetHubOpStatus": accEnetHubOpStatus,
       "accEnetHubBitError": accEnetHubBitError,
       "accEnetHubLinkTest": accEnetHubLinkTest,
       "accUnNumIP": accUnNumIP,
       "accIpNetSrcAddrTable": accIpNetSrcAddrTable,
       "accIpNetSrcAddrEntry": accIpNetSrcAddrEntry,
       "accIpNetSrcIfIndex": accIpNetSrcIfIndex,
       "accIpNetSrcAddress": accIpNetSrcAddress,
       "pysmiFakeCol2": pysmiFakeCol2}
)
