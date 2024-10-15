# SNMP MIB module (HUAWEI-LOAD-BACKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-LOAD-BACKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:35 2024
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

(hwFrameIndex,
 hwSlotIndex) = mibBuilder.importSymbols(
    "HUAWEI-DEVICE-MIB",
    "hwFrameIndex",
    "hwSlotIndex")

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

(HWPCBType,) = mibBuilder.importSymbols(
    "HUAWEI-TC-MIB",
    "HWPCBType")

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

hwLoadBackup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwLoadBackupMon_ObjectIdentity = ObjectIdentity
hwLoadBackupMon = _HwLoadBackupMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1)
)
_HwLoadParaTable_Object = MibTable
hwLoadParaTable = _HwLoadParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwLoadParaTable.setStatus("current")
_HwLoadParaEntry_Object = MibTableRow
hwLoadParaEntry = _HwLoadParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1)
)
hwLoadParaEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwLoadParaEntry.setStatus("current")
_HwLoadServerIpAddr_Type = IpAddress
_HwLoadServerIpAddr_Object = MibTableColumn
hwLoadServerIpAddr = _HwLoadServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 1),
    _HwLoadServerIpAddr_Type()
)
hwLoadServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadServerIpAddr.setStatus("current")


class _HwLoadMode_Type(Integer32):
    """Custom type hwLoadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 3),
          ("modem", 2),
          ("other", 255),
          ("smbLoadAnyBoards", 4),
          ("tftp", 1))
    )


_HwLoadMode_Type.__name__ = "Integer32"
_HwLoadMode_Object = MibTableColumn
hwLoadMode = _HwLoadMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 2),
    _HwLoadMode_Type()
)
hwLoadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadMode.setStatus("current")


class _HwLoadFileName_Type(DisplayString):
    """Custom type hwLoadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwLoadFileName_Type.__name__ = "DisplayString"
_HwLoadFileName_Object = MibTableColumn
hwLoadFileName = _HwLoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 3),
    _HwLoadFileName_Type()
)
hwLoadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadFileName.setStatus("current")


class _HwLoadContent_Type(Integer32):
    """Custom type hwLoadContent based on Integer32"""
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
              22,
              23,
              24,
              40,
              41,
              42,
              45,
              46,
              49,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("configuration", 2),
          ("configurationCli", 42),
          ("configurationEfs", 41),
          ("configurationIni", 40),
          ("cpeDrive", 7),
          ("license", 49),
          ("logciPa", 20),
          ("logicAfc", 14),
          ("logicCpld", 12),
          ("logicFpga", 11),
          ("logicPci", 13),
          ("patch", 3),
          ("program", 1),
          ("programApp", 10),
          ("programBios", 9),
          ("programBootFile", 19),
          ("programBsp", 24),
          ("programCurrent", 45),
          ("programDataFlow", 18),
          ("programDatabase", 8),
          ("programExtendedBios", 51),
          ("programFirmware", 16),
          ("programHelp", 17),
          ("programMicroCode", 15),
          ("programOther", 46),
          ("programchipset", 50),
          ("resGeneral", 6),
          ("resLocal", 5),
          ("shellMacro", 4),
          ("webExp", 21),
          ("webHelp", 23),
          ("webNev", 22))
    )


_HwLoadContent_Type.__name__ = "Integer32"
_HwLoadContent_Object = MibTableColumn
hwLoadContent = _HwLoadContent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 4),
    _HwLoadContent_Type()
)
hwLoadContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadContent.setStatus("current")
_HwLoadBoardType_Type = HWPCBType
_HwLoadBoardType_Object = MibTableColumn
hwLoadBoardType = _HwLoadBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 5),
    _HwLoadBoardType_Type()
)
hwLoadBoardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadBoardType.setStatus("current")
_HwPortId_Type = Integer32
_HwPortId_Object = MibTableColumn
hwPortId = _HwPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 6),
    _HwPortId_Type()
)
hwPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortId.setStatus("current")


class _HwLoadProcess_Type(Integer32):
    """Custom type hwLoadProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwLoadProcess_Type.__name__ = "Integer32"
_HwLoadProcess_Object = MibTableColumn
hwLoadProcess = _HwLoadProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 7),
    _HwLoadProcess_Type()
)
hwLoadProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLoadProcess.setStatus("current")


class _HwLoadUserName_Type(DisplayString):
    """Custom type hwLoadUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwLoadUserName_Type.__name__ = "DisplayString"
_HwLoadUserName_Object = MibTableColumn
hwLoadUserName = _HwLoadUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 8),
    _HwLoadUserName_Type()
)
hwLoadUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadUserName.setStatus("current")


class _HwLoadPassword_Type(DisplayString):
    """Custom type hwLoadPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwLoadPassword_Type.__name__ = "DisplayString"
_HwLoadPassword_Object = MibTableColumn
hwLoadPassword = _HwLoadPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 1, 1, 9),
    _HwLoadPassword_Type()
)
hwLoadPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLoadPassword.setStatus("current")
_HwBackupParaTable_Object = MibTable
hwBackupParaTable = _HwBackupParaTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hwBackupParaTable.setStatus("current")
_HwBackupParaEntry_Object = MibTableRow
hwBackupParaEntry = _HwBackupParaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1)
)
hwBackupParaEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwBackupParaEntry.setStatus("current")
_HwBackupServerIpAddr_Type = IpAddress
_HwBackupServerIpAddr_Object = MibTableColumn
hwBackupServerIpAddr = _HwBackupServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 1),
    _HwBackupServerIpAddr_Type()
)
hwBackupServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupServerIpAddr.setStatus("current")


class _HwBackupMode_Type(Integer32):
    """Custom type hwBackupMode based on Integer32"""
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
        *(("ftp", 3),
          ("modem", 2),
          ("other", 4),
          ("tftp", 1))
    )


_HwBackupMode_Type.__name__ = "Integer32"
_HwBackupMode_Object = MibTableColumn
hwBackupMode = _HwBackupMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 2),
    _HwBackupMode_Type()
)
hwBackupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupMode.setStatus("current")


class _HwBackupFileName_Type(DisplayString):
    """Custom type hwBackupFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HwBackupFileName_Type.__name__ = "DisplayString"
_HwBackupFileName_Object = MibTableColumn
hwBackupFileName = _HwBackupFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 3),
    _HwBackupFileName_Type()
)
hwBackupFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupFileName.setStatus("current")


class _HwBackupContent_Type(Integer32):
    """Custom type hwBackupContent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              40,
              41,
              42,
              45,
              46,
              47,
              49,
              51,
              60)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 5),
          ("bcdcInfo", 47),
          ("bill", 4),
          ("boardinfo", 60),
          ("configuration", 1),
          ("configurationCli", 42),
          ("configurationEfs", 41),
          ("configurationIni", 40),
          ("license", 49),
          ("log", 3),
          ("logciPa", 30),
          ("logicAfc", 25),
          ("logicCpld", 23),
          ("logicFpga", 22),
          ("logicPci", 24),
          ("patch", 18),
          ("program", 15),
          ("programApp", 21),
          ("programBios", 20),
          ("programBootFile", 29),
          ("programBsp", 34),
          ("programCurrent", 45),
          ("programDataFlow", 28),
          ("programDatabase", 19),
          ("programExtendedBios", 51),
          ("programFireware", 27),
          ("programMicroCode", 26),
          ("programOther", 46),
          ("resgeneral", 17),
          ("reslocal", 16),
          ("shellMacro", 2),
          ("webExp", 31),
          ("webHelp", 33),
          ("webNev", 32))
    )


_HwBackupContent_Type.__name__ = "Integer32"
_HwBackupContent_Object = MibTableColumn
hwBackupContent = _HwBackupContent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 4),
    _HwBackupContent_Type()
)
hwBackupContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupContent.setStatus("current")


class _HwBackupProcess_Type(Integer32):
    """Custom type hwBackupProcess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBackupProcess_Type.__name__ = "Integer32"
_HwBackupProcess_Object = MibTableColumn
hwBackupProcess = _HwBackupProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 5),
    _HwBackupProcess_Type()
)
hwBackupProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupProcess.setStatus("current")


class _HwBackupUserName_Type(DisplayString):
    """Custom type hwBackupUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBackupUserName_Type.__name__ = "DisplayString"
_HwBackupUserName_Object = MibTableColumn
hwBackupUserName = _HwBackupUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 6),
    _HwBackupUserName_Type()
)
hwBackupUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupUserName.setStatus("current")


class _HwBackupPassword_Type(DisplayString):
    """Custom type hwBackupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HwBackupPassword_Type.__name__ = "DisplayString"
_HwBackupPassword_Object = MibTableColumn
hwBackupPassword = _HwBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 7),
    _HwBackupPassword_Type()
)
hwBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupPassword.setStatus("current")
_HwBackupBoardType_Type = HWPCBType
_HwBackupBoardType_Object = MibTableColumn
hwBackupBoardType = _HwBackupBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 2, 1, 8),
    _HwBackupBoardType_Type()
)
hwBackupBoardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupBoardType.setStatus("current")
_SnmpTraps_ObjectIdentity = ObjectIdentity
snmpTraps = _SnmpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3)
)
_HwLoadAndBackupTrapsOID_ObjectIdentity = ObjectIdentity
hwLoadAndBackupTrapsOID = _HwLoadAndBackupTrapsOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0)
)
_HwTrapCauseOids_ObjectIdentity = ObjectIdentity
hwTrapCauseOids = _HwTrapCauseOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1)
)
_HwTrapLoadBackupResult_ObjectIdentity = ObjectIdentity
hwTrapLoadBackupResult = _HwTrapLoadBackupResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 1)
)
_HwTrapLoadResult_Type = Integer32
_HwTrapLoadResult_Object = MibScalar
hwTrapLoadResult = _HwTrapLoadResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 1, 1),
    _HwTrapLoadResult_Type()
)
hwTrapLoadResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTrapLoadResult.setStatus("current")
_HwTrapBackupResult_Type = Integer32
_HwTrapBackupResult_Object = MibScalar
hwTrapBackupResult = _HwTrapBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 1, 2),
    _HwTrapBackupResult_Type()
)
hwTrapBackupResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTrapBackupResult.setStatus("current")


class _HwCopyAndSaveResult_Type(Integer32):
    """Custom type hwCopyAndSaveResult based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("copyDeviceBusy", 8),
          ("copyDeviceError", 10),
          ("copyDeviceFull", 12),
          ("copyDeviceNotProgrammable", 11),
          ("copyDeviceOpenError", 9),
          ("copyFileChecksumError", 15),
          ("copyFileOpenError", 13),
          ("copyFileTransferError", 14),
          ("copyInProgress", 1),
          ("copyInvalidDestName", 6),
          ("copyInvalidOperation", 3),
          ("copyInvalidProtocol", 4),
          ("copyInvalidServerAddress", 7),
          ("copyInvalidSourceName", 5),
          ("copyNoMemory", 16),
          ("copyOperationSuccess", 2),
          ("copyUnknownFailure", 17))
    )


_HwCopyAndSaveResult_Type.__name__ = "Integer32"
_HwCopyAndSaveResult_Object = MibScalar
hwCopyAndSaveResult = _HwCopyAndSaveResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 1, 3),
    _HwCopyAndSaveResult_Type()
)
hwCopyAndSaveResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwCopyAndSaveResult.setStatus("current")
_HwTrapEventCauses_ObjectIdentity = ObjectIdentity
hwTrapEventCauses = _HwTrapEventCauses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 2)
)


class _HwConfEventCause_Type(Integer32):
    """Custom type hwConfEventCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confChangedDirect", 1),
          ("confChangedDuration", 3),
          ("confSaved", 2))
    )


_HwConfEventCause_Type.__name__ = "Integer32"
_HwConfEventCause_Object = MibScalar
hwConfEventCause = _HwConfEventCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 1, 2, 1),
    _HwConfEventCause_Type()
)
hwConfEventCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwConfEventCause.setStatus("current")
_HwBackupAndRestoreConfig_ObjectIdentity = ObjectIdentity
hwBackupAndRestoreConfig = _HwBackupAndRestoreConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 4)
)


class _HwBackupAndRestore_Type(Integer32):
    """Custom type hwBackupAndRestore based on Integer32"""
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
        *(("copyFlashToMem", 2),
          ("copyHardDiskToMem", 4),
          ("copyMemToFlash", 1),
          ("copyMemToHardDisk", 3))
    )


_HwBackupAndRestore_Type.__name__ = "Integer32"
_HwBackupAndRestore_Object = MibScalar
hwBackupAndRestore = _HwBackupAndRestore_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 4, 1),
    _HwBackupAndRestore_Type()
)
hwBackupAndRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBackupAndRestore.setStatus("current")
_HwPatch_ObjectIdentity = ObjectIdentity
hwPatch = _HwPatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2)
)
_HwPatchTable_Object = MibTable
hwPatchTable = _HwPatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    hwPatchTable.setStatus("current")
_HwPatchEntry_Object = MibTableRow
hwPatchEntry = _HwPatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1)
)
hwPatchEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
    (0, "HUAWEI-LOAD-BACKUP-MIB", "hwPatchId"),
)
if mibBuilder.loadTexts:
    hwPatchEntry.setStatus("current")


class _HwPatchId_Type(Unsigned32):
    """Custom type hwPatchId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwPatchId_Type.__name__ = "Unsigned32"
_HwPatchId_Object = MibTableColumn
hwPatchId = _HwPatchId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 1),
    _HwPatchId_Type()
)
hwPatchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPatchId.setStatus("current")


class _HwPatchDescription_Type(DisplayString):
    """Custom type hwPatchDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwPatchDescription_Type.__name__ = "DisplayString"
_HwPatchDescription_Object = MibTableColumn
hwPatchDescription = _HwPatchDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 2),
    _HwPatchDescription_Type()
)
hwPatchDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchDescription.setStatus("current")
_HwPatchFuncNum_Type = Integer32
_HwPatchFuncNum_Object = MibTableColumn
hwPatchFuncNum = _HwPatchFuncNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 3),
    _HwPatchFuncNum_Type()
)
hwPatchFuncNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchFuncNum.setStatus("current")
_HwPatchTextLen_Type = Integer32
_HwPatchTextLen_Object = MibTableColumn
hwPatchTextLen = _HwPatchTextLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 4),
    _HwPatchTextLen_Type()
)
hwPatchTextLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchTextLen.setStatus("current")
_HwPatchDataLen_Type = Integer32
_HwPatchDataLen_Object = MibTableColumn
hwPatchDataLen = _HwPatchDataLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 5),
    _HwPatchDataLen_Type()
)
hwPatchDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchDataLen.setStatus("current")


class _HwPatchType_Type(Integer32):
    """Custom type hwPatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("temporary", 2))
    )


_HwPatchType_Type.__name__ = "Integer32"
_HwPatchType_Object = MibTableColumn
hwPatchType = _HwPatchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 6),
    _HwPatchType_Type()
)
hwPatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchType.setStatus("current")


class _HwPatchAdminStatus_Type(Integer32):
    """Custom type hwPatchAdminStatus based on Integer32"""
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
        *(("active", 1),
          ("deactive", 2),
          ("remove", 3),
          ("running", 4))
    )


_HwPatchAdminStatus_Type.__name__ = "Integer32"
_HwPatchAdminStatus_Object = MibTableColumn
hwPatchAdminStatus = _HwPatchAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 7),
    _HwPatchAdminStatus_Type()
)
hwPatchAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPatchAdminStatus.setStatus("current")


class _HwPatchOperState_Type(Integer32):
    """Custom type hwPatchOperState based on Integer32"""
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
        *(("patchActive", 1),
          ("patchDeActive", 2),
          ("patchInit", 3),
          ("patchRunning", 4),
          ("patchload", 5))
    )


_HwPatchOperState_Type.__name__ = "Integer32"
_HwPatchOperState_Object = MibTableColumn
hwPatchOperState = _HwPatchOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 1, 1, 8),
    _HwPatchOperState_Type()
)
hwPatchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchOperState.setStatus("current")
_HwPatchStatTable_Object = MibTable
hwPatchStatTable = _HwPatchStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2)
)
if mibBuilder.loadTexts:
    hwPatchStatTable.setStatus("current")
_HwPatchStatEntry_Object = MibTableRow
hwPatchStatEntry = _HwPatchStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1)
)
hwPatchStatEntry.setIndexNames(
    (0, "HUAWEI-DEVICE-MIB", "hwFrameIndex"),
    (0, "HUAWEI-DEVICE-MIB", "hwSlotIndex"),
)
if mibBuilder.loadTexts:
    hwPatchStatEntry.setStatus("current")
_HwPatchStatNumMax_Type = Integer32
_HwPatchStatNumMax_Object = MibTableColumn
hwPatchStatNumMax = _HwPatchStatNumMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1, 1),
    _HwPatchStatNumMax_Type()
)
hwPatchStatNumMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStatNumMax.setStatus("current")
_HwPatchStatTextMax_Type = Integer32
_HwPatchStatTextMax_Object = MibTableColumn
hwPatchStatTextMax = _HwPatchStatTextMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1, 2),
    _HwPatchStatTextMax_Type()
)
hwPatchStatTextMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStatTextMax.setStatus("current")
_HwPatchStatDataMax_Type = Integer32
_HwPatchStatDataMax_Object = MibTableColumn
hwPatchStatDataMax = _HwPatchStatDataMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1, 3),
    _HwPatchStatDataMax_Type()
)
hwPatchStatDataMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStatDataMax.setStatus("current")
_HwPatchStatTextUsed_Type = Integer32
_HwPatchStatTextUsed_Object = MibTableColumn
hwPatchStatTextUsed = _HwPatchStatTextUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1, 4),
    _HwPatchStatTextUsed_Type()
)
hwPatchStatTextUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStatTextUsed.setStatus("current")
_HwPatchStatDataUsed_Type = Integer32
_HwPatchStatDataUsed_Object = MibTableColumn
hwPatchStatDataUsed = _HwPatchStatDataUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 2, 2, 1, 5),
    _HwPatchStatDataUsed_Type()
)
hwPatchStatDataUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPatchStatDataUsed.setStatus("current")
_HwLoadBackupConformance_ObjectIdentity = ObjectIdentity
hwLoadBackupConformance = _HwLoadBackupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3)
)
_HwLoadBackupCompliances_ObjectIdentity = ObjectIdentity
hwLoadBackupCompliances = _HwLoadBackupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 1)
)
_HwLoadBackupObjectGroups_ObjectIdentity = ObjectIdentity
hwLoadBackupObjectGroups = _HwLoadBackupObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2)
)

# Managed Objects groups

hwLoadParaTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 1)
)
hwLoadParaTableGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwLoadServerIpAddr"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadMode"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadFileName"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadContent"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadBoardType"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPortId"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadProcess"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadUserName"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadPassword"))
)
if mibBuilder.loadTexts:
    hwLoadParaTableGroup.setStatus("current")

hwBackupParaTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 2)
)
hwBackupParaTableGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwBackupServerIpAddr"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupMode"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupFileName"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupContent"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupProcess"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupUserName"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupPassword"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupBoardType"))
)
if mibBuilder.loadTexts:
    hwBackupParaTableGroup.setStatus("current")

hwTrapEventCausesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 3)
)
hwTrapEventCausesGroup.setObjects(
    ("HUAWEI-LOAD-BACKUP-MIB", "hwConfEventCause")
)
if mibBuilder.loadTexts:
    hwTrapEventCausesGroup.setStatus("current")

hwTrapLoadBackupResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 4)
)
hwTrapLoadBackupResultGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwTrapLoadResult"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwTrapBackupResult"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwCopyAndSaveResult"))
)
if mibBuilder.loadTexts:
    hwTrapLoadBackupResultGroup.setStatus("current")

hwBackupAndRestoreConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 6)
)
hwBackupAndRestoreConfigGroup.setObjects(
    ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupAndRestore")
)
if mibBuilder.loadTexts:
    hwBackupAndRestoreConfigGroup.setStatus("current")

hwPatchTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 7)
)
hwPatchTableGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwPatchDescription"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchFuncNum"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchTextLen"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchDataLen"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchType"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchAdminStatus"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchOperState"))
)
if mibBuilder.loadTexts:
    hwPatchTableGroup.setStatus("current")

hwPatchStatTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 8)
)
hwPatchStatTableGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwPatchStatNumMax"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchStatTextMax"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchStatDataMax"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchStatTextUsed"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwPatchStatDataUsed"))
)
if mibBuilder.loadTexts:
    hwPatchStatTableGroup.setStatus("current")


# Notification objects

hwBackupFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 1)
)
hwBackupFailAlarm.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwTrapBackupResult"))
)
if mibBuilder.loadTexts:
    hwBackupFailAlarm.setStatus(
        "current"
    )

hwLoadFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 2)
)
hwLoadFailAlarm.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwTrapLoadResult"))
)
if mibBuilder.loadTexts:
    hwLoadFailAlarm.setStatus(
        "current"
    )

hwBackupFailAlarmSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 3)
)
hwBackupFailAlarmSuccess.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"))
)
if mibBuilder.loadTexts:
    hwBackupFailAlarmSuccess.setStatus(
        "current"
    )

hwLoadFailAlarmSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 4)
)
hwLoadFailAlarmSuccess.setObjects(
      *(("HUAWEI-DEVICE-MIB", "hwFrameIndex"),
        ("HUAWEI-DEVICE-MIB", "hwSlotIndex"))
)
if mibBuilder.loadTexts:
    hwLoadFailAlarmSuccess.setStatus(
        "current"
    )

hwCopyAndSaveFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 5)
)
hwCopyAndSaveFail.setObjects(
    ("HUAWEI-LOAD-BACKUP-MIB", "hwCopyAndSaveResult")
)
if mibBuilder.loadTexts:
    hwCopyAndSaveFail.setStatus(
        "current"
    )

hwCopyAndSaveSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    hwCopyAndSaveSuccess.setStatus(
        "current"
    )

hwConfigurationChangedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 1, 3, 0, 7)
)
hwConfigurationChangedEvent.setObjects(
    ("HUAWEI-LOAD-BACKUP-MIB", "hwConfEventCause")
)
if mibBuilder.loadTexts:
    hwConfigurationChangedEvent.setStatus(
        "current"
    )


# Notifications groups

hwTrapLoadBackupTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 2, 5)
)
hwTrapLoadBackupTrapsGroup.setObjects(
      *(("HUAWEI-LOAD-BACKUP-MIB", "hwBackupFailAlarm"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadFailAlarm"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwBackupFailAlarmSuccess"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwLoadFailAlarmSuccess"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwCopyAndSaveFail"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwCopyAndSaveSuccess"),
        ("HUAWEI-LOAD-BACKUP-MIB", "hwConfigurationChangedEvent"))
)
if mibBuilder.loadTexts:
    hwTrapLoadBackupTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwLoadBackupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwLoadBackupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-LOAD-BACKUP-MIB",
    **{"hwLoadBackup": hwLoadBackup,
       "hwLoadBackupMon": hwLoadBackupMon,
       "hwLoadParaTable": hwLoadParaTable,
       "hwLoadParaEntry": hwLoadParaEntry,
       "hwLoadServerIpAddr": hwLoadServerIpAddr,
       "hwLoadMode": hwLoadMode,
       "hwLoadFileName": hwLoadFileName,
       "hwLoadContent": hwLoadContent,
       "hwLoadBoardType": hwLoadBoardType,
       "hwPortId": hwPortId,
       "hwLoadProcess": hwLoadProcess,
       "hwLoadUserName": hwLoadUserName,
       "hwLoadPassword": hwLoadPassword,
       "hwBackupParaTable": hwBackupParaTable,
       "hwBackupParaEntry": hwBackupParaEntry,
       "hwBackupServerIpAddr": hwBackupServerIpAddr,
       "hwBackupMode": hwBackupMode,
       "hwBackupFileName": hwBackupFileName,
       "hwBackupContent": hwBackupContent,
       "hwBackupProcess": hwBackupProcess,
       "hwBackupUserName": hwBackupUserName,
       "hwBackupPassword": hwBackupPassword,
       "hwBackupBoardType": hwBackupBoardType,
       "snmpTraps": snmpTraps,
       "hwLoadAndBackupTrapsOID": hwLoadAndBackupTrapsOID,
       "hwBackupFailAlarm": hwBackupFailAlarm,
       "hwLoadFailAlarm": hwLoadFailAlarm,
       "hwBackupFailAlarmSuccess": hwBackupFailAlarmSuccess,
       "hwLoadFailAlarmSuccess": hwLoadFailAlarmSuccess,
       "hwCopyAndSaveFail": hwCopyAndSaveFail,
       "hwCopyAndSaveSuccess": hwCopyAndSaveSuccess,
       "hwConfigurationChangedEvent": hwConfigurationChangedEvent,
       "hwTrapCauseOids": hwTrapCauseOids,
       "hwTrapLoadBackupResult": hwTrapLoadBackupResult,
       "hwTrapLoadResult": hwTrapLoadResult,
       "hwTrapBackupResult": hwTrapBackupResult,
       "hwCopyAndSaveResult": hwCopyAndSaveResult,
       "hwTrapEventCauses": hwTrapEventCauses,
       "hwConfEventCause": hwConfEventCause,
       "hwBackupAndRestoreConfig": hwBackupAndRestoreConfig,
       "hwBackupAndRestore": hwBackupAndRestore,
       "hwPatch": hwPatch,
       "hwPatchTable": hwPatchTable,
       "hwPatchEntry": hwPatchEntry,
       "hwPatchId": hwPatchId,
       "hwPatchDescription": hwPatchDescription,
       "hwPatchFuncNum": hwPatchFuncNum,
       "hwPatchTextLen": hwPatchTextLen,
       "hwPatchDataLen": hwPatchDataLen,
       "hwPatchType": hwPatchType,
       "hwPatchAdminStatus": hwPatchAdminStatus,
       "hwPatchOperState": hwPatchOperState,
       "hwPatchStatTable": hwPatchStatTable,
       "hwPatchStatEntry": hwPatchStatEntry,
       "hwPatchStatNumMax": hwPatchStatNumMax,
       "hwPatchStatTextMax": hwPatchStatTextMax,
       "hwPatchStatDataMax": hwPatchStatDataMax,
       "hwPatchStatTextUsed": hwPatchStatTextUsed,
       "hwPatchStatDataUsed": hwPatchStatDataUsed,
       "hwLoadBackupConformance": hwLoadBackupConformance,
       "hwLoadBackupCompliances": hwLoadBackupCompliances,
       "hwLoadBackupCompliance": hwLoadBackupCompliance,
       "hwLoadBackupObjectGroups": hwLoadBackupObjectGroups,
       "hwLoadParaTableGroup": hwLoadParaTableGroup,
       "hwBackupParaTableGroup": hwBackupParaTableGroup,
       "hwTrapEventCausesGroup": hwTrapEventCausesGroup,
       "hwTrapLoadBackupResultGroup": hwTrapLoadBackupResultGroup,
       "hwTrapLoadBackupTrapsGroup": hwTrapLoadBackupTrapsGroup,
       "hwBackupAndRestoreConfigGroup": hwBackupAndRestoreConfigGroup,
       "hwPatchTableGroup": hwPatchTableGroup,
       "hwPatchStatTableGroup": hwPatchStatTableGroup}
)
